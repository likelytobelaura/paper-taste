"""X (Twitter) as a source: papers and posts AI Twitter, or the people you follow, are sharing.

Free by default: reads AI-X recap newsletters (AINews etc.) and resolves the posts they link via
FxTwitter (see fetch_curated). With X API credentials it also reads your own home timeline.

The timeline path reads the authenticated user's home timeline (or an X List) through the X API v2, pulls out
arXiv / Hugging Face papers / blog links, and keeps per-item mention aggregates. Only aggregates
are stored (distinct sharers, likes, a few public handles) — never post text.

Credentials (any one; checked in this order):
  X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET   OAuth 1.0a user context (home timeline;
                                                                  tokens don't expire, so this suits CI)
  X_USER_TOKEN                                                    OAuth 2.0 user access token (home timeline)
  X_BEARER_TOKEN + [x] list_id in sources.toml                    app-only, reads an X List instead
The X API bills per post read, so each run reads at most [x] max_posts, newest first, and never
re-reads posts older than the previous run.
"""

import base64
import hashlib
import hmac
import json
import math
import os
import re
import secrets
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

from .fetch import http_get, log

API = "https://api.x.com/2"
ARXIV_LINK = re.compile(r"(?:arxiv\.org/(?:abs|pdf|html)/|huggingface\.co/papers/|alphaxiv\.org/(?:abs/)?)"
                        r"(\d{4}\.\d{4,5})", re.I)


def _oauth1_header(method, url, params, key, secret, token, token_secret, nonce=None, timestamp=None):
    oauth = {"oauth_consumer_key": key, "oauth_nonce": nonce or secrets.token_hex(16),
             "oauth_signature_method": "HMAC-SHA1", "oauth_timestamp": str(timestamp or int(time.time())),
             "oauth_token": token, "oauth_version": "1.0"}
    q = lambda s: urllib.parse.quote(str(s), safe="~")
    base_params = "&".join(f"{q(k)}={q(v)}" for k, v in sorted({**params, **oauth}.items()))
    base = "&".join([method, q(url), q(base_params)])
    sig = hmac.new(f"{q(secret)}&{q(token_secret)}".encode(), base.encode(), hashlib.sha1).digest()
    oauth["oauth_signature"] = base64.b64encode(sig).decode()
    return "OAuth " + ", ".join(f'{q(k)}="{q(v)}"' for k, v in sorted(oauth.items()))


def credentials(env=None):
    env = os.environ if env is None else env
    o1 = [env.get(k) for k in ("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_TOKEN_SECRET")]
    if all(o1):
        return {"mode": "oauth1", "keys": o1}
    if env.get("X_USER_TOKEN"):
        return {"mode": "user", "token": env["X_USER_TOKEN"]}
    if env.get("X_BEARER_TOKEN"):
        return {"mode": "app", "token": env["X_BEARER_TOKEN"]}
    return None


def _get(path, params, creds):
    url = f"{API}{path}"
    if creds["mode"] == "oauth1":
        auth = _oauth1_header("GET", url, params, *creds["keys"])
    else:
        auth = f"Bearer {creds['token']}"
    full = f"{url}?{urllib.parse.urlencode(params)}" if params else url
    return json.loads(http_get(full, headers={"Authorization": auth}, retries=2, backoff=15))


def fetch_posts(cfg, creds, since_id=None, start_time=None):
    """Newest-first posts with link entities, at most cfg['max_posts']. Returns (posts, users, newest_id)."""
    max_posts = cfg.get("max_posts", 200)
    if creds["mode"] == "app":
        if not cfg.get("list_id"):
            raise ValueError("X_BEARER_TOKEN reads an X List: set [x] list_id in sources.toml")
        path = f"/lists/{cfg['list_id']}/tweets"
    else:
        me = _get("/users/me", {}, creds)["data"]["id"]
        path = f"/users/{me}/timelines/reverse_chronological"
    params = {"max_results": 100, "tweet.fields": "created_at,public_metrics,entities,author_id,referenced_tweets",
              "expansions": "author_id", "user.fields": "username,public_metrics"}
    if creds["mode"] != "app":  # the list endpoint takes neither
        if since_id:
            params["since_id"] = since_id
        elif start_time:
            params["start_time"] = start_time
    posts, users, token = [], {}, None
    while len(posts) < max_posts:
        params["max_results"] = max(5, min(100, max_posts - len(posts)))
        if token:
            params["pagination_token"] = token
        page = _get(path, params, creds)
        posts += page.get("data", [])
        users.update({u["id"]: u for u in page.get("includes", {}).get("users", [])})
        token = page.get("meta", {}).get("next_token")
        if not token:
            break
        if creds["mode"] == "app" and since_id and any(p["id"] <= since_id for p in page.get("data", [])):
            break
    posts = posts[:max_posts]
    if since_id and creds["mode"] == "app":
        posts = [p for p in posts if int(p["id"]) > int(since_id)]
    newest = max((p["id"] for p in posts), key=int, default=since_id)
    return posts, users, newest


def post_links(post):
    for u in (post.get("entities") or {}).get("urls") or []:
        link = u.get("unwound_url") or u.get("expanded_url") or u.get("url")
        if link:
            yield link
    yield from re.findall(r"https?://\S+", post.get("text", ""))


def item_key(link):
    """Map a shared link to a paper-taste item id, or None."""
    m = ARXIV_LINK.search(link)
    if m:
        return f"arxiv:{m.group(1)}"
    host_path = re.sub(r"^https?://(www\.)?", "", link.split("?")[0].split("#")[0]).rstrip("/")
    not_articles = ("x.com", "twitter.com", "t.co", "youtu", "github.com", "huggingface.co", "forms.gle",
                    "docs.google.com", "linkedin.com", "instagram.com", "threads.", "discord.", "apps.apple.com",
                    "play.google.com", "pic.x.com", "lu.ma", "luma.com", "colab.research.google.com",
                    "drive.google.com", "imgur.com", "i.redd.it", "v.redd.it", "reddit.com", "redd.it",
                    "news.ycombinator.com", "lobste.rs", "bsky.app", "open.spotify.com", "podcasts.apple.com")
    if host_path.count("/") >= 1 and not host_path.startswith(not_articles):
        return "blog:" + host_path
    return None


def merge_mentions(mentions, posts, users, now, public_handles=False):
    """Fold posts into {item_id: {"by": {sharer: likes}, "first_seen": iso, "url": link}}.

    Sharers are stored as short hashes unless public_handles is set: the data directory is
    public, and the set of accounts someone follows shouldn't be published by default.
    """
    # Keyed hash: a plain hash of a handle can be reversed by hashing candidate handles.
    salt = (os.environ.get("X_API_SECRET") or os.environ.get("X_BEARER_TOKEN") or "").encode()
    for p in posts:
        handle = (users.get(p.get("author_id")) or {}).get("username") or p.get("author_id", "?")
        if ":" in handle:  # platform-prefixed public submission (hn:…, reddit:…, nl:…), not a person you follow
            sharer = handle
        else:
            sharer = handle if public_handles else \
                "#" + hmac.new(salt, handle.lower().encode(), hashlib.sha256).hexdigest()[:10]
        likes = (p.get("public_metrics") or {}).get("like_count", 0)
        keys = {}
        for link in post_links(p):
            key = item_key(link)
            if key:
                keys.setdefault(key, link)
        for key, link in keys.items():
            m = mentions.setdefault(key, {"by": {}, "first_seen": now.isoformat(), "url": link})
            m["by"][sharer] = max(m["by"].get(sharer, 0), likes)
    return mentions


def prune(mentions, now, days=30):
    cutoff = (now - timedelta(days=days)).isoformat()
    return {k: v for k, v in mentions.items() if v["first_seen"] >= cutoff}


PLATFORMS = {"hn": "Hacker News", "reddit": "Reddit", "lobsters": "Lobsters", "nl": "newsletters"}
# reason prefixes that mark an item as socially shared (used for the digest section)
SOCIAL_REASONS = ("shared on X", "Hacker News:", "Reddit:", "Lobsters:", "in newsletters:")


def signal(mention):
    """(0..1 attention, [reasons]): distinct sharers matter most, likes/points break ties."""
    if not mention:
        return 0.0, []
    by = mention["by"]
    raw = len(by) + 0.5 * math.log1p(sum(by.values())) / math.log(10)
    groups = {}
    for sharer, score in by.items():
        plat = sharer.split(":", 1)[0] if ":" in sharer else "x"
        groups.setdefault(plat, []).append((sharer, score))
    reasons = []
    if "x" in groups:
        named = [h for h, _ in sorted(groups["x"], key=lambda hs: -hs[1]) if not h.startswith("#")][:3]
        who = f" ({', '.join('@' + h for h in named)})" if named else ""
        n = len(groups["x"])
        reasons.append(f"shared on X by {n} account{'s' * (n != 1)}{who}")
    for plat in ("hn", "reddit", "lobsters"):
        if plat in groups:
            pts, n = sum(s for _, s in groups[plat]), len(groups[plat])
            reasons.append(f"{PLATFORMS[plat]}: {n} submission{'s' * (n != 1)}" + (f", {pts} points" if pts else ""))
    if "nl" in groups:
        reasons.append("in newsletters: " + ", ".join(s.split(":", 1)[1] for s, _ in groups["nl"]))
    return min(1.0, math.log1p(raw) / math.log1p(8)), reasons


# ---------- free path: AI-X recap newsletters, resolved through FxTwitter ----------
#
# Newsletters like AINews (Latent Space) read AI Twitter every day and link the posts that
# mattered. Each linked post is looked up on api.fxtwitter.com (free, no auth) to get its links
# and like count. You get the AI-X consensus rather than your own timeline, at no cost.

STATUS_LINK = re.compile(r"(?:x|twitter)\.com/\w+/status/(\d+)")
SHORTENERS = {"t.co", "goo.gle", "buff.ly", "bit.ly", "ow.ly", "dlvr.it", "lnkd.in", "tinyurl.com", "trib.al",
              "shorturl.at", "rb.gy", "is.gd", "hubs.la", "msft.it", "amzn.to"}


def expand(link):
    """Follow a URL shortener's redirect; other links come back unchanged."""
    host = re.sub(r"^https?://(www\.)?", "", link).split("/")[0].lower()
    if host not in SHORTENERS:
        return link
    try:
        req = urllib.request.Request(link, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.geturl()
    except Exception:
        return link


def fx_post(status_id):
    """One public post via FxTwitter, as {id, author_id, text, public_metrics, entities.urls}, or None."""
    try:
        t = json.loads(http_get(f"https://api.fxtwitter.com/status/{status_id}", retries=2, backoff=5))["tweet"]
    except Exception:
        return None
    urls = []
    for tw in (t, t.get("quote") or {}):
        for f in (tw.get("raw_text") or {}).get("facets") or []:
            if f.get("type") == "url" and (f.get("replacement") or f.get("original")):
                urls.append({"expanded_url": expand(f.get("replacement") or f["original"])})
    return {"id": str(t.get("id", status_id)), "author_id": (t.get("author") or {}).get("screen_name", "?"),
            "text": t.get("text", ""), "public_metrics": {"like_count": t.get("likes") or 0},
            "entities": {"urls": urls}}


def fetch_curated(cfg, state, now):
    """New recap issues -> (posts, users). Marks issues done in state['curated_seen']."""
    from .fetch import CONTENT, _parse_xml, parse_date
    since = now - timedelta(days=cfg.get("curated_lookback_days", 3))
    done = set(state.get("curated_seen", []))
    ids, direct = [], []
    for feed in cfg.get("curated_feeds", []):
        try:
            root = _parse_xml(http_get(feed["url"]))
        except Exception as e:
            log(f"x curated: {feed['name']}: FAILED {e}")
            continue
        for item in root.iter("item"):
            link, title = item.findtext("link", ""), item.findtext("title", "")
            published = parse_date(item.findtext("pubDate"))
            if link in done or not published or published < since or \
                    not title.startswith(feed.get("title_prefix", "")):
                continue
            body = item.findtext(f"{CONTENT}encoded") or item.findtext("description") or ""
            got = list(dict.fromkeys(STATUS_LINK.findall(body))) if feed.get("resolve_x", True) else []
            ids += got
            # papers and articles the newsletter links directly count as one share by the newsletter
            own = re.sub(r"^https?://(www\.)?", "", feed["url"]).split("/")[0]
            direct.append({"id": link, "author_id": f"nl:{feed['name']}", "public_metrics": {"like_count": 0},
                           "entities": {"urls": [{"expanded_url": u} for u in re.findall(r'href="(https?://[^"]+)"', body)
                                                 if own not in u and "substack.com" not in u]}})
            done.add(link)
            log(f"x curated: {feed['name']}: {title[:60]} ({len(got)} posts)")
    ids = list(dict.fromkeys(ids))[:cfg.get("max_lookups", 300)]
    posts = []
    for status_id in ids:
        p = fx_post(status_id)
        if p:
            posts.append(p)
        time.sleep(0.3)  # free community service: be gentle
    state["curated_seen"] = sorted(done)[-200:]
    users = {p["author_id"]: {"username": p["author_id"]} for p in posts + direct}
    log(f"x curated: resolved {len(posts)}/{len(ids)} posts")
    return posts + direct, users


def update(cfg, state, now=None, social_cfg=None):
    """Fold new share data into state['mentions']: recap newsletters, community aggregators
    (social_cfg), and the X timeline if credentialed."""
    now = now or datetime.now(timezone.utc)
    state = {**state, "mentions": prune(state.get("mentions", {}), now)}
    if not cfg.get("enabled", True):
        return state
    mentions, public = state["mentions"], cfg.get("public_handles", False)
    if cfg.get("curated", True) and cfg.get("curated_feeds"):
        try:
            posts, users = fetch_curated(cfg, state, now)
            merge_mentions(mentions, posts, users, now, public)
        except Exception as e:
            log(f"x curated: FAILED {type(e).__name__}: {e}")
    if social_cfg:
        from . import social
        merge_mentions(mentions, social.fetch_all(social_cfg, now), {}, now, public)
    creds = credentials()
    if not creds:
        log("x: no API credentials; timeline skipped (curated recaps only)")
        return state
    start = (now - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        posts, users, newest = fetch_posts(cfg, creds, state.get("since_id"), start)
    except Exception as e:
        log(f"x: FAILED {type(e).__name__}: {e}")
        return state
    merge_mentions(mentions, posts, users, now, public)
    linked = sum(1 for p in posts if any(item_key(l) for l in post_links(p)))
    log(f"x: read {len(posts)} posts ({creds['mode']}), {linked} with paper/blog links, {len(mentions)} items tracked")
    return {**state, "since_id": newest}
