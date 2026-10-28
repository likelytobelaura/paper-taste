"""Community aggregators (Hacker News, Reddit, Lobsters) as attention signals.

Each submission becomes a "post" in the same shape xsource uses, with author_id prefixed by the
platform ("hn:123", "reddit:abc"), so items shared there join the same mention aggregates as X.
All endpoints are free and unauthenticated; any that fail are skipped.
"""

import json
import re
import time
import urllib.parse
from datetime import timedelta

from .fetch import http_get, log

LINK = re.compile(r'https?://[^\s<>"\')\]]+')
# Hacker News and Lobsters cover everything; keep submissions that look like AI/ML.
AI_TERMS = re.compile(
    r"\b(ai|ml|llms?|gpt[\w.-]*|claude|gemini|llama|qwen|deepseek|mistral|transformers?|neural|deep learning|"
    r"machine learning|language models?|diffusion|reinforcement learning|rlhf|agents?|agentic|inference|"
    r"fine[- ]?tun\w*|embeddings?|tokeni[sz]\w*|interpretability|alignment|benchmarks?|arxiv|openai|anthropic|"
    r"deepmind|hugging ?face|pytorch|jax|cuda|gpus?|attention|reasoning|multimodal|vision models?|robotics?)\b", re.I)


def _post(sharer, url, score, text=""):
    urls = [url] if url else []
    urls += LINK.findall(text or "")
    return {"id": sharer, "author_id": sharer, "public_metrics": {"like_count": score or 0},
            "entities": {"urls": [{"expanded_url": u} for u in urls]}}


def hacker_news(since, min_points=20, max_pages=10):
    """Stories since `since` with at least `min_points`, via the Algolia HN API."""
    posts = []
    for page in range(max_pages):
        params = urllib.parse.urlencode({
            "tags": "story", "hitsPerPage": 100, "page": page,
            "numericFilters": f"created_at_i>{int(since.timestamp())},points>={min_points}"})
        rows = json.loads(http_get(f"https://hn.algolia.com/api/v1/search_by_date?{params}"))
        posts += [_post(f"hn:{h['objectID']}", h.get("url"), h.get("points"), h.get("story_text"))
                  for h in rows.get("hits", []) if AI_TERMS.search(f"{h.get('title', '')} {h.get('url') or ''}")]
        if page + 1 >= rows.get("nbPages", 0):
            break
    return posts


def reddit(subreddits, window="week"):
    """Top posts per subreddit via RSS (the JSON API now returns 403 without OAuth). RSS carries
    no scores, so Reddit contributes submissions, not points."""
    from .fetch import ATOM, _parse_xml
    posts = []
    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/top/.rss?t={window}"
        try:
            root = _parse_xml(http_get(url, headers={"User-Agent": "paper-taste/0.1 (research feed)"},
                                       retries=3, backoff=20))
        except Exception as e:
            log(f"reddit r/{sub}: {getattr(e, 'code', e)}")
            continue
        for e in root.iter(f"{ATOM}entry"):
            rid = e.findtext(f"{ATOM}id", "").rsplit("_", 1)[-1]
            body = e.findtext(f"{ATOM}content") or ""
            links = [u for u in re.findall(r'href="(https?://[^"]+)"', body)
                     if "reddit.com" not in u and "redd.it" not in u]
            posts.append(_post(f"reddit:{rid}", None, 0, " ".join(links)))
        time.sleep(4)  # Reddit rate-limits unauthenticated readers quickly
    return posts


def lobsters(tags):
    posts = []
    for tag in tags:
        try:
            rows = json.loads(http_get(f"https://lobste.rs/t/{tag}.json"))
        except Exception as e:
            log(f"lobsters {tag}: {getattr(e, 'code', e)}")
            continue
        posts += [_post(f"lobsters:{r['short_id']}", r.get("url"), r.get("score"), r.get("description"))
                  for r in rows if AI_TERMS.search(f"{r.get('title', '')} {r.get('url') or ''}")]
    return posts


def fetch_all(cfg, now):
    """All configured aggregators -> list of posts."""
    since = now - timedelta(days=cfg.get("lookback_days", 4))
    jobs = [
        ("hacker news", lambda: hacker_news(since, cfg.get("hn_min_points", 20))) if cfg.get("hacker_news", True) else None,
        ("reddit", lambda: reddit(cfg.get("reddit", []))) if cfg.get("reddit") else None,
        ("lobsters", lambda: lobsters(cfg.get("lobsters", []))) if cfg.get("lobsters") else None,
    ]
    posts = []
    for name, job in filter(None, jobs):
        try:
            got = job()
            log(f"{name}: {len(got)} submissions")
            posts += got
        except Exception as e:
            log(f"{name}: FAILED {type(e).__name__}: {e}")
    return posts
