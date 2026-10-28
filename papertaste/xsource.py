"""X (Twitter) timeline as a source: papers and posts people you follow are sharing.

Reads the authenticated user's home timeline (or an X List) through the X API v2, pulls out
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
    if host_path.count("/") >= 1 and not host_path.startswith(("x.com", "twitter.com", "t.co", "youtu", "github.com")):
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


def signal(mention):
    """0..1 attention score: distinct sharers matter most, likes break ties."""
    if not mention:
        return 0.0, None
    by = mention["by"]
    raw = len(by) + 0.5 * math.log1p(sum(by.values())) / math.log(10)
    named = [h for h in sorted(by, key=lambda h: -by[h]) if not h.startswith("#")][:3]
    who = f" ({', '.join('@' + h for h in named)})" if named else ""
    n = len(by)
    return min(1.0, math.log1p(raw) / math.log1p(8)), f"shared on X by {n} account{'s' * (n != 1)}{who}"


def update(cfg, state, now=None):
    """Read new timeline posts into state['mentions']. Returns state; no-op without credentials."""
    now = now or datetime.now(timezone.utc)
    creds = credentials()
    mentions = prune(state.get("mentions", {}), now)
    if not creds or not cfg.get("enabled", True):
        if not creds:
            log("x: no credentials, using stored mentions only")
        return {**state, "mentions": mentions}
    start = (now - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        posts, users, newest = fetch_posts(cfg, creds, state.get("since_id"), start)
    except Exception as e:
        log(f"x: FAILED {type(e).__name__}: {e}")
        return {**state, "mentions": mentions}
    merge_mentions(mentions, posts, users, now, cfg.get("public_handles", False))
    linked = sum(1 for p in posts if any(item_key(l) for l in post_links(p)))
    log(f"x: read {len(posts)} posts ({creds['mode']}), {linked} with paper/blog links, {len(mentions)} items tracked")
    return {"since_id": newest, "mentions": mentions}
