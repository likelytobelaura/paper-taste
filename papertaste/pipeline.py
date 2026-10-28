"""`update`: fetch new items, score them, keep the best, write data/ and DIGEST.md."""

import json
import tomllib
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import fetch, score
from .fetch import log
from .text import TfIdf, nearest_neighbours, tokens

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ITEMS = DATA / "items"
SEEN = DATA / "seen.json"
HISTORY_DAYS = 60
DROP_FIELDS = ("body_text",)


def load_config(path=None):
    with open(path or ROOT / "sources.toml", "rb") as f:
        return tomllib.load(f)


def load_items(days=None, now=None):
    """Stored items, optionally only those published in the last `days` days."""
    now = now or datetime.now(timezone.utc)
    cutoff = (now - timedelta(days=days)).strftime("%Y-%m-%d") if days else ""
    out = []
    for f in sorted(ITEMS.glob("*.jsonl")):
        if f.stem >= cutoff:
            out += [json.loads(line) for line in f.open() if line.strip()]
    return out


def _doc(item):
    return tokens(item["title"] + " " + item["title"] + " " + item.get("summary", ""))


def run(config=None, use_s2=True, now=None):
    cfg = config or load_config()
    now = now or datetime.now(timezone.utc)
    seen = json.loads(SEEN.read_text()) if SEEN.exists() else {}

    ax = cfg["arxiv"]
    since = (now - timedelta(days=ax["lookback_days"])).replace(hour=0, minute=0, second=0, microsecond=0)
    papers = fetch.fetch_arxiv(ax["categories"], since)
    hf = fetch.fetch_hf_daily(fetch.utc_days(ax["lookback_days"] + 2, now))
    blog_since = now - timedelta(days=cfg.get("blogs", {}).get("lookback_days", 21))
    blogs = fetch.fetch_blogs(cfg.get("blog", []), blog_since, seen)
    n_blogs = len(blogs)
    blogs = [b for b in blogs if score.is_research_post(b)]
    log(f"fetched {len(papers)} arXiv papers, {n_blogs} blog posts ({len(blogs)} research)")

    # Novelty: compare each new item against the batch plus the stored history.
    fresh_ids = {i["id"] for i in papers + blogs}
    history = [i for i in load_items(HISTORY_DAYS, now) if i["id"] not in fresh_ids]
    pool_items = papers + blogs + history
    docs = [_doc(i) for i in pool_items]
    tfidf = TfIdf(docs)
    vecs = [(i["id"], tfidf.vector(d, top=30)) for i, d in zip(pool_items, docs)]
    novelty = nearest_neighbours(vecs[:len(papers) + len(blogs)], vecs)

    def scored(item, s2=None):
        aid = item["id"].removeprefix("arxiv:")
        sig, reasons, flags = score.signals(item, novelty.get(item["id"]), hf.get(aid), s2)
        q = score.quality(item, sig, flags)
        extra = {"hf": hf[aid]} if aid in hf else {}
        return {**{k: v for k, v in item.items() if k not in DROP_FIELDS}, **extra,
                "quality": q, "signals": {k: round(v, 3) for k, v in sig.items()},
                "reasons": reasons, "flags": flags}

    out = [scored(p) for p in papers]
    if use_s2 and out:
        top = sorted(out, key=lambda i: -i["quality"])[:500]
        s2 = fetch.fetch_s2([i["id"].removeprefix("arxiv:") for i in top])
        if s2:
            by_id = {p["id"]: p for p in papers}
            out = [scored(by_id[i["id"]], s2.get(i["id"].removeprefix("arxiv:"))) for i in out]

    # Keep the top fraction of each publication day, plus anything the community picked up.
    by_day = defaultdict(list)
    for i in out:
        by_day[i["published"][:10]].append(i)
    kept = []
    for day_items in by_day.values():
        day_items.sort(key=lambda i: -i["quality"])
        n = max(20, int(len(day_items) * ax.get("keep_fraction", 0.25)))
        kept += [i for k, i in enumerate(day_items) if k < n or i.get("hf", {}).get("upvotes", 0) >= 5]
    kept += [scored(b) for b in blogs]

    write_items(kept, {i["published"][:10] for i in out})
    SEEN.write_text(json.dumps(dict(sorted(seen.items())), indent=0) + "\n")
    write_digest(now)
    log(f"kept {len(kept)} items")
    return kept


def write_items(items, refreshed_days):
    """Merge into data/items/<published-date>.jsonl. Days fully re-fetched this run are rewritten."""
    ITEMS.mkdir(parents=True, exist_ok=True)
    by_day = defaultdict(dict)
    for day in refreshed_days:
        f = ITEMS / f"{day}.jsonl"
        if f.exists():  # keep blog posts; arXiv rows for this day are replaced wholesale
            by_day[day] = {i["id"]: i for i in map(json.loads, f.open()) if i["kind"] == "blog"}
    for i in items:
        day = i["published"][:10]
        if day not in by_day:
            f = ITEMS / f"{day}.jsonl"
            by_day[day] = {r["id"]: r for r in map(json.loads, f.open())} if f.exists() else {}
        by_day[day][i["id"]] = i
    for day, rows in by_day.items():
        ordered = sorted(rows.values(), key=lambda i: (-i["quality"], i["id"]))
        (ITEMS / f"{day}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in ordered))


def top(days=7, n=25, kind=None, now=None, items=None):
    now = now or datetime.now(timezone.utc)
    items = items if items is not None else load_items(days, now)
    items = [i for i in items if kind in (None, i["kind"])]
    return sorted(items, key=lambda i: -score.rank_score(i, now))[:n]


def fmt_item(rank, i, now=None, extra=""):
    when = i["published"][:10]
    who = i["source"] if i["kind"] == "blog" else ", ".join(a["name"] for a in i.get("authors", [])[:3]) + \
        (" et al." if len(i.get("authors", [])) > 3 else "")
    why = "; ".join(i["reasons"][:6]) or "—"
    flags = f" ⚠ {'; '.join(i['flags'])}" if i["flags"] else ""
    summary = i.get("summary", "")
    summary = summary[:280].rsplit(" ", 1)[0] + "…" if len(summary) > 280 else summary
    return (f"{rank}. **[{i['title']}]({i['url']})** — quality {i['quality']:.0f}{extra}  \n"
            f"   {who} · {when}  \n   _why:_ {why}{flags}  \n   > {summary}\n")


def write_digest(now=None):
    now = now or datetime.now(timezone.utc)
    items = load_items(14, now)
    papers = top(7, 25, "paper", now, items)
    blogs = top(14, 12, "blog", now, items)
    lines = [f"# paper-taste digest — {now:%Y-%m-%d}\n",
             "Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from "
             "metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, "
             "and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.\n",
             f"## Papers (last 7 days, {sum(i['kind'] == 'paper' for i in items)} kept in the last 14)\n"]
    lines += [fmt_item(k + 1, i, now) for k, i in enumerate(papers)]
    lines += ["\n## Blog posts & lab write-ups (last 14 days)\n"]
    lines += [fmt_item(k + 1, i, now) for k, i in enumerate(blogs)] or ["_None yet._\n"]
    text = "\n".join(lines)
    (ROOT / "DIGEST.md").write_text(text)
    (DATA / "digests").mkdir(parents=True, exist_ok=True)
    (DATA / "digests" / f"{now:%Y-%m-%d}.md").write_text(text)
