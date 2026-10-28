"""Fetch candidate items from arXiv, Hugging Face daily papers, blog feeds and blog index pages."""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

from .text import strip_html

UA = "paper-taste/0.1 (+https://github.com/likelytobelaura/paper-taste)"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
CONTENT = "{http://purl.org/rss/1.0/modules/content/}"
DC = "{http://purl.org/dc/elements/1.1/}"


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def http_get(url, data=None, headers=None, timeout=45, retries=3, backoff=5):
    hdrs = {"User-Agent": UA, **(headers or {})}
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            code = getattr(e, "code", None)
            if code in (400, 401, 403, 404, 410) or attempt == retries - 1:
                raise
            time.sleep(backoff * (attempt + 1))


def parse_date(s):
    if not s:
        return None
    s = s.strip()
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        try:
            d = parsedate_to_datetime(s)
        except (TypeError, ValueError):
            for fmt in ("%b %d, %Y", "%B %d, %Y", "%Y-%m-%d", "%d %B %Y", "%d %b %Y"):
                try:
                    d = datetime.strptime(s, fmt)
                    break
                except ValueError:
                    continue
            else:
                return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


# ---------- arXiv ----------

def fetch_arxiv(categories, since, page=500, max_pages=30):
    """All v1 submissions in `categories` published at or after `since`, newest first."""
    query = " OR ".join(f"cat:{c}" for c in categories)
    items, seen = [], set()
    for p in range(max_pages):
        params = urllib.parse.urlencode({
            "search_query": query, "sortBy": "submittedDate", "sortOrder": "descending",
            "start": p * page, "max_results": page,
        })
        entries = []
        for attempt in range(3):  # the API occasionally returns an empty page mid-listing
            root = ET.fromstring(http_get(f"https://export.arxiv.org/api/query?{params}", timeout=90))
            entries = root.findall(f"{ATOM}entry")
            if entries:
                break
            time.sleep(5)
        if not entries:
            break
        oldest = None
        for e in entries:
            it = _arxiv_entry(e)
            oldest = it["published"]
            if it["published"] >= since.isoformat() and it["id"] not in seen:
                seen.add(it["id"])
                items.append(it)
        log(f"arxiv page {p}: {len(entries)} entries, oldest {oldest[:10]}, kept {len(items)}")
        if oldest < since.isoformat():
            break
        time.sleep(3)  # arXiv API etiquette
    return items


def _arxiv_entry(e):
    raw_id = e.findtext(f"{ATOM}id", "").rsplit("/abs/", 1)[-1]
    aid = re.sub(r"v\d+$", "", raw_id)
    authors = []
    for a in e.findall(f"{ATOM}author"):
        name = a.findtext(f"{ATOM}name", "").strip()
        aff = [x.text.strip() for x in a.findall(f"{ARXIV}affiliation") if x.text]
        authors.append({"name": name, **({"affiliation": aff} if aff else {})})
    prim = e.find(f"{ARXIV}primary_category")
    return {
        "id": f"arxiv:{aid}",
        "kind": "paper",
        "source": "arXiv",
        "title": " ".join(e.findtext(f"{ATOM}title", "").split()),
        "summary": " ".join(e.findtext(f"{ATOM}summary", "").split()),
        "url": f"https://arxiv.org/abs/{aid}",
        "pdf": f"https://arxiv.org/pdf/{aid}",
        "published": parse_date(e.findtext(f"{ATOM}published")).isoformat(),
        "authors": authors,
        "comment": " ".join((e.findtext(f"{ARXIV}comment") or "").split()),
        "categories": [c.get("term") for c in e.findall(f"{ATOM}category")],
        "primary_category": prim.get("term") if prim is not None else None,
    }


# ---------- Hugging Face daily papers ----------

def fetch_hf_daily(days):
    """{arxiv_id: {...}} for papers featured on HF daily papers on each of the given dates."""
    out = {}
    for day in days:
        url = f"https://huggingface.co/api/daily_papers?date={day}&limit=100"
        try:
            rows = json.loads(http_get(url))
        except Exception as e:
            log(f"hf daily {day}: {e}")
            continue
        for r in rows:
            p = r.get("paper") or {}
            if not p.get("id"):
                continue
            org = (r.get("organization") or p.get("organization") or {})
            prev = out.get(p["id"], {})
            out[p["id"]] = {
                "upvotes": max(p.get("upvotes") or 0, prev.get("upvotes", 0)),
                "github": p.get("githubRepo") or prev.get("github"),
                "github_stars": p.get("githubStars") or prev.get("github_stars"),
                "project_page": p.get("projectPage") or prev.get("project_page"),
                "org": org.get("fullname") or org.get("name") or prev.get("org"),
                "comments": r.get("numComments") or 0,
            }
        log(f"hf daily {day}: {len(rows)} papers")
    return out


# ---------- Semantic Scholar (optional, needs S2_API_KEY to be reliable) ----------

def fetch_s2(arxiv_ids):
    """{arxiv_id: {"max_h": int, "citations": int}}. Silently partial on rate limits."""
    key = os.environ.get("S2_API_KEY")
    headers = {"content-type": "application/json", **({"x-api-key": key} if key else {})}
    out = {}
    for i in range(0, len(arxiv_ids), 400):
        chunk = arxiv_ids[i:i + 400]
        body = json.dumps({"ids": [f"ARXIV:{a}" for a in chunk]}).encode()
        try:
            rows = json.loads(http_get(
                "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,authors.hIndex",
                data=body, headers=headers, retries=4, backoff=10))
        except Exception as e:
            log(f"semantic scholar: {e} (skipping author signal for {len(arxiv_ids) - i} papers)")
            break
        for aid, row in zip(chunk, rows):
            if row:
                hs = [a.get("hIndex") or 0 for a in row.get("authors") or []]
                out[aid] = {"max_h": max(hs, default=0), "citations": row.get("citationCount") or 0}
        time.sleep(1.5)
    return out


# ---------- blogs ----------

def _parse_xml(raw):
    try:
        return ET.fromstring(raw)
    except ET.ParseError:  # common feed breakage: bare '&' and control characters
        raw = re.sub(rb"&(?!#?\w+;)", b"&amp;", raw)
        return ET.fromstring(re.sub(rb"[\x00-\x08\x0b\x0c\x0e-\x1f]", b"", raw))


def fetch_feed(src, since):
    root = _parse_xml(http_get(src["url"]))
    items = []
    for node in root.iter():
        if node.tag == "item":
            title = node.findtext("title", "")
            link = node.findtext("link", "")
            date = node.findtext("pubDate") or node.findtext(f"{DC}date")
            body = node.findtext(f"{CONTENT}encoded") or node.findtext("description") or ""
            desc = node.findtext("description") or ""
        elif node.tag == f"{ATOM}entry":
            title = node.findtext(f"{ATOM}title", "")
            links = node.findall(f"{ATOM}link")
            alt = [l for l in links if l.get("rel", "alternate") == "alternate"] or links
            link = alt[0].get("href", "") if alt else ""
            date = node.findtext(f"{ATOM}published") or node.findtext(f"{ATOM}updated")
            body = node.findtext(f"{ATOM}content") or node.findtext(f"{ATOM}summary") or ""
            desc = node.findtext(f"{ATOM}summary") or ""
        else:
            continue
        published = parse_date(date)
        if not published or published < since or not link:
            continue
        items.append(_blog_item(src, title, link.strip(), published, desc, body))
    return items


SITE_SUFFIX = re.compile(r"\s+[\\|·–—-]\s+[^\\|·–—-]{2,40}$")


def _blog_item(src, title, link, published, desc, body):
    body_text = strip_html(body)
    summary = strip_html(desc) or body_text
    title = " ".join(strip_html(title).split())
    if src["type"] == "html":  # "<post title> | Lab Name"
        title = SITE_SUFFIX.sub("", title)
    return {
        "id": "blog:" + re.sub(r"^https?://(www\.)?", "", link).rstrip("/"),
        "kind": "blog",
        "source": src["name"],
        "tier": src.get("tier", 3),
        "title": title,
        "summary": summary[:1500],
        "url": link,
        "published": published.isoformat(),
        "body_chars": len(body_text),
        "body_text": body_text[:20000],
    }


META_DATE = re.compile(
    r'(?:property|name|itemprop)="(?:article:published_time|datePublished|date|pubdate|publish-date)"'
    r'\s+content="([^"]+)"|"datePublished"\s*:\s*"([^"]+)"|<time[^>]*datetime="([^"]+)"', re.I)
TEXT_DATE = re.compile(r"\b((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]* \d{1,2}, 20\d\d)\b")
META_DESC = re.compile(r'(?:name|property)="(?:og:description|description)"\s+content="([^"]*)"', re.I)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
ANCHOR = re.compile(r'<a\b[^>]*href="([^"#?]+)"[^>]*>(.*?)</a>', re.I | re.S)


def fetch_html_index(src, since, seen, max_new=12):
    """Scrape an index page for post links; open unseen posts to get date + description.

    `seen` maps item id -> first-seen ISO date; it is updated in place so posts without a
    machine-readable date get the date the crawler first noticed them.
    """
    page = http_get(src["url"], headers={"User-Agent": "Mozilla/5.0 " + UA}).decode("utf-8", "replace")
    pattern = re.compile(src["link"])
    links = []
    for href, text in ANCHOR.findall(page):
        if pattern.search(href) and href not in [l for l, _ in links]:
            links.append((href, strip_html(text)))
    now = datetime.now(timezone.utc)
    # First crawl of a source: everything already on the index is old unless the post page
    # itself carries a recent date. Only the first `max_new` links (index pages list newest
    # first) are opened to look for one.
    baseline = f"source:{src['name']}" not in seen
    seen.setdefault(f"source:{src['name']}", now.isoformat())
    items, opened = [], 0
    for href, anchor_text in links:
        url = urllib.parse.urljoin(src["url"], href)
        key = f"blog:{src['name']}|{url}"
        if key in seen and seen[key] < since.isoformat():
            continue
        if opened >= max_new:
            if baseline:
                seen.setdefault(key, "1970-01-01T00:00:00+00:00")
            continue
        opened += 1
        try:
            post = http_get(url, headers={"User-Agent": "Mozilla/5.0 " + UA}).decode("utf-8", "replace")
        except Exception as e:
            log(f"{src['name']}: {url}: {e}")
            continue
        m = META_DATE.search(post)
        published = parse_date(next((g for g in m.groups() if g), None)) if m else None
        if not published:
            t = TEXT_DATE.search(strip_html(post[:200000]))
            published = parse_date(t.group(1).replace("Sept ", "Sep ")) if t else None
        if not published:
            if baseline:  # first crawl of this source: undated posts are old, not new
                seen.setdefault(key, "1970-01-01T00:00:00+00:00")
                continue
            published = parse_date(seen.setdefault(key, now.isoformat()))
        seen.setdefault(key, published.isoformat())
        if published < since:
            continue
        t = TITLE.search(post)
        title = strip_html(t.group(1)) if t else anchor_text
        d = META_DESC.search(post)
        items.append(_blog_item(src, title or anchor_text, url, published, d.group(1) if d else "", post))
    return items


ARTICLE = re.compile(r"(?is)<(article|main)\b[^>]*>(.*)</\1>")


def enrich(item, cache, max_chars=20000):
    """Feeds often carry a one-line summary; read the post itself when the site allows it."""
    if item["url"] in cache:
        text = cache[item["url"]]
    else:
        try:
            page = http_get(item["url"], headers={"User-Agent": "Mozilla/5.0 " + UA}, retries=1, timeout=20)
            page = page.decode("utf-8", "replace")
            m = ARTICLE.search(page)
            text = strip_html(m.group(2) if m else page)[:max_chars]
        except Exception:
            text = ""
        cache[item["url"]] = text
    if len(text) > item["body_chars"]:
        item["body_text"], item["body_chars"] = text, len(text)


def fetch_blogs(sources, since, seen, max_enrich=12):
    from .score import CUSTOMER, NOT_RESEARCH
    items, cache = [], {}
    for src in sources:
        try:
            got = fetch_html_index(src, since, seen) if src["type"] == "html" else fetch_feed(src, since)
            short = [i for i in got if i["body_chars"] < 1500
                     and not NOT_RESEARCH.search(i["title"]) and not CUSTOMER.search(i["title"])]
            for i in short[:max_enrich]:
                enrich(i, cache)
            log(f"{src['name']}: {len(got)} posts since {since.date()}")
            items += got
        except Exception as e:
            log(f"{src['name']}: FAILED {type(e).__name__}: {e}")
    return items


def utc_days(n, end=None):
    end = end or datetime.now(timezone.utc)
    return [(end - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(n)]
