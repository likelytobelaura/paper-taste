import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from papertaste import fetch, pipeline, recommend, score, xsource

NOW = datetime(2026, 10, 28, 12, tzinfo=timezone.utc)


def paper(summary, title="A paper", comment="", **kw):
    return {"id": "arxiv:2610.00001", "kind": "paper", "source": "arXiv", "title": title, "summary": summary,
            "comment": comment, "url": "u", "published": NOW.isoformat(), "authors": [], **kw}


def quality(item, novelty=(0.1, 0), hf=None):
    sig, _, flags = score.signals(item, novelty, hf)
    return score.quality(item, sig, flags)


class ScoreTest(unittest.TestCase):
    def test_rigorous_beats_hype(self):
        rigorous = paper("We run controlled experiments across 6 benchmarks and 3 model scales from 125M to 7B "
                         "parameters, with ablations and 5 random seeds; we report confidence intervals. "
                         "Code is available at github.com/x/y. The method fails to help at the smallest scale.",
                         comment="38 pages, 21 figures. Accepted at ICLR 2027")
        hype = paper("We propose a revolutionary, groundbreaking method with unprecedented performance that "
                     "outperforms all prior work by a large margin, unlocking the full potential of LLMs.")
        self.assertGreater(quality(rigorous), quality(hype) + 25)

    def test_reasons_and_flags_are_reported(self):
        sig, reasons, flags = score.signals(paper("We ablate everything. Unprecedented."), (0.7, 0))
        self.assertIn("ablations", reasons)
        self.assertTrue(any(f.startswith("hype") for f in flags))
        self.assertTrue(any(f.startswith("near-duplicate") for f in flags))

    def test_community_attention_raises_quality(self):
        p = paper("We study X with baselines.")
        self.assertGreater(quality(p, hf={"upvotes": 120}), quality(p, hf={"upvotes": 0}))

    def test_novelty_matters(self):
        p = paper("We study X with baselines.")
        self.assertGreater(quality(p, novelty=(0.1, 0)), quality(p, novelty=(0.6, 9)))

    def test_workshop_counts_less_than_main_venue(self):
        main = paper("x" * 600, comment="Accepted at NeurIPS 2026")
        ws = paper("x" * 600, comment="Accepted at NeurIPS 2026 workshop on Y")
        self.assertGreater(quality(main), quality(ws))

    def test_recency_ranks_new_over_old_at_equal_quality(self):
        new = {"quality": 60, "published": NOW.isoformat()}
        old = {"quality": 60, "published": (NOW - timedelta(days=20)).isoformat()}
        self.assertAlmostEqual(score.rank_score(old, NOW) / score.rank_score(new, NOW), 0.25, places=3)

    def test_research_gate(self):
        def post(title, summary="", tier=3, body=""):
            return {"title": title, "summary": summary, "tier": tier, "body_text": body, "body_chars": len(body)}
        self.assertFalse(score.is_research_post(post("Acme cuts costs 76x with GPT-6.1")))
        self.assertFalse(score.is_research_post(post("Nebius joins the PyTorch Foundation as a Platinum Member")))
        self.assertTrue(score.is_research_post(post("Untitled", tier=1)))
        self.assertTrue(score.is_research_post(
            post("Genie 4", "A new world model for interactive simulation research", tier=3)))
        long_marketing = "Our customers love the new dashboard. " * 100
        self.assertFalse(score.is_research_post(post("Spring update", tier=2, body=long_marketing)))


RSS = b"""<?xml version="1.0"?><rss version="2.0"><channel>
<item><title>New post &amp; results</title><link>https://ex.org/a</link>
<pubDate>Tue, 27 Oct 2026 10:00:00 GMT</pubDate><description>&lt;p&gt;We find X.&lt;/p&gt;</description></item>
<item><title>Old</title><link>https://ex.org/b</link><pubDate>Tue, 01 Sep 2026 10:00:00 GMT</pubDate></item>
</channel></rss>"""
ATOM = b"""<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
<entry><title>Atom post</title><link rel="alternate" href="https://ex.org/c"/>
<published>2026-10-26T00:00:00Z</published><summary>Hello</summary></entry></feed>"""


class FetchTest(unittest.TestCase):
    src = {"name": "Ex", "type": "rss", "url": "https://ex.org/feed", "tier": 2}

    def test_rss_and_atom(self):
        since = NOW - timedelta(days=7)
        with mock.patch.object(fetch, "http_get", return_value=RSS):
            items = fetch.fetch_feed(self.src, since)
        self.assertEqual([i["title"] for i in items], ["New post & results"])
        self.assertEqual(items[0]["summary"], "We find X.")
        with mock.patch.object(fetch, "http_get", return_value=ATOM):
            self.assertEqual(fetch.fetch_feed(self.src, since)[0]["url"], "https://ex.org/c")

    def test_broken_feed_is_repaired(self):
        broken = RSS.replace(b"&amp;", b"&")
        with mock.patch.object(fetch, "http_get", return_value=broken):
            self.assertEqual(len(fetch.fetch_feed(self.src, NOW - timedelta(days=7))), 1)

    def test_html_index_baseline_marks_backlog_old(self):
        src = {"name": "Lab", "type": "html", "url": "https://lab.ai/blog", "link": r"^/blog/[a-z-]+$", "tier": 1}
        index = "".join(f'<a href="/blog/post-{c}">Post {c}</a>' for c in "abcdefghijklmnop").encode()
        yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
        dated = f'<title>Post a | Lab</title><meta property="article:published_time" content="{yesterday}">'.encode()

        def get(url, **kw):
            return index if url.endswith("/blog") else dated if url.endswith("post-a") else b"<p>no date</p>"

        seen = {}
        since = datetime.now(timezone.utc) - timedelta(days=21)
        with mock.patch.object(fetch, "http_get", side_effect=get):
            first = fetch.fetch_html_index(src, since, seen)
            second = fetch.fetch_html_index(src, since, seen)
        self.assertEqual([i["title"] for i in first], ["Post a"])  # site suffix stripped
        self.assertEqual(len([k for k in seen if k.startswith("blog:")]), 16)
        self.assertEqual([i["title"] for i in second], ["Post a"])  # undated backlog never resurfaces as new


class XTest(unittest.TestCase):
    def test_item_keys(self):
        self.assertEqual(xsource.item_key("https://arxiv.org/abs/2610.12345v2"), "arxiv:2610.12345")
        self.assertEqual(xsource.item_key("https://huggingface.co/papers/2610.12345"), "arxiv:2610.12345")
        self.assertEqual(xsource.item_key("https://www.alphaxiv.org/abs/2610.1234"), "arxiv:2610.1234")
        self.assertEqual(xsource.item_key("https://sander.ai/2026/10/01/post.html?ref=x"),
                         "blog:sander.ai/2026/10/01/post.html")
        self.assertIsNone(xsource.item_key("https://x.com/someone/status/1"))
        self.assertIsNone(xsource.item_key("https://github.com/org/repo"))
        self.assertIsNone(xsource.item_key("https://example.com"))

    def test_mentions_dedupe_and_hash_handles(self):
        users = {"1": {"id": "1", "username": "alice"}, "2": {"id": "2", "username": "bob"}}
        posts = [
            {"id": "10", "author_id": "1", "public_metrics": {"like_count": 50},
             "entities": {"urls": [{"expanded_url": "https://arxiv.org/abs/2610.00001"},
                                   {"expanded_url": "https://arxiv.org/pdf/2610.00001v1"}]}},
            {"id": "11", "author_id": "1", "public_metrics": {"like_count": 5},
             "text": "again https://arxiv.org/abs/2610.00001"},
            {"id": "12", "author_id": "2", "public_metrics": {"like_count": 7},
             "entities": {"urls": [{"unwound_url": "https://huggingface.co/papers/2610.00001"}]}},
        ]
        m = xsource.merge_mentions({}, posts, users, NOW)["arxiv:2610.00001"]
        self.assertEqual(len(m["by"]), 2)
        self.assertEqual(sorted(m["by"].values()), [7, 50])
        self.assertTrue(all(h.startswith("#") for h in m["by"]))  # no handles in public data by default
        self.assertNotIn("alice", xsource.signal(m)[1])
        named = xsource.merge_mentions({}, posts, users, NOW, public_handles=True)["arxiv:2610.00001"]
        self.assertIn("@alice", xsource.signal(named)[1])

    def test_signal_grows_with_sharers(self):
        one = xsource.signal({"by": {"#a": 3}})[0]
        five = xsource.signal({"by": {f"#{k}": 3 for k in range(5)}})[0]
        self.assertGreater(five, one)
        self.assertLessEqual(xsource.signal({"by": {f"#{k}": 10 ** 6 for k in range(500)}})[0], 1.0)
        self.assertEqual(xsource.signal(None), (0.0, None))

    def test_x_attention_raises_quality(self):
        p = paper("We study X with baselines.")
        sig0, _, f0 = score.signals(p, (0.1, 0), None, None, (0.0, None))
        sig1, reasons, f1 = score.signals(p, (0.1, 0), None, None, xsource.signal({"by": {"#a": 9, "#b": 2}}))
        self.assertGreater(score.quality(p, sig1, f1), score.quality(p, sig0, f0))
        self.assertIn("shared on X by 2 accounts", reasons)

    def test_credentials_precedence(self):
        o1 = {"X_API_KEY": "k", "X_API_SECRET": "s", "X_ACCESS_TOKEN": "t", "X_ACCESS_TOKEN_SECRET": "ts"}
        self.assertEqual(xsource.credentials({**o1, "X_BEARER_TOKEN": "b"})["mode"], "oauth1")
        self.assertEqual(xsource.credentials({"X_USER_TOKEN": "u", "X_BEARER_TOKEN": "b"})["mode"], "user")
        self.assertEqual(xsource.credentials({"X_BEARER_TOKEN": "b"})["mode"], "app")
        self.assertIsNone(xsource.credentials({"X_API_KEY": "k"}))

    def test_oauth1_signature_matches_x_docs_example(self):
        # Worked example from X's "Creating a signature" documentation.
        header = xsource._oauth1_header(
            "POST", "https://api.twitter.com/1.1/statuses/update.json",
            {"include_entities": "true", "status": "Hello Ladies + Gentlemen, a signed OAuth request!"},
            "xvz1evFS4wEEPTGEFPHBog", "kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw",
            "370773112-GmHxMAgYyLbNEtIKZeRNFsMKPR9EyMZeS9weJAEb", "LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE",
            nonce="kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg", timestamp=1318622958)
        self.assertIn('oauth_signature="hCtSmYh%2BiHYCEqBWrE7C7hYmtUk%3D"', header)

    def test_fetch_posts_paginates_and_respects_cap(self):
        pages = [
            {"data": [{"id": str(i)} for i in range(300, 200, -1)], "meta": {"next_token": "p2"},
             "includes": {"users": [{"id": "1", "username": "a"}]}},
            {"data": [{"id": str(i)} for i in range(200, 100, -1)], "meta": {"next_token": "p3"}},
        ]
        calls = []

        def fake_get(path, params, creds):
            calls.append((path, dict(params)))
            return {"data": {"id": "42"}} if path == "/users/me" else pages[len(calls) - 2]

        with mock.patch.object(xsource, "_get", side_effect=fake_get):
            posts, users, newest = xsource.fetch_posts({"max_posts": 150}, {"mode": "user", "token": "t"},
                                                        since_id="99")
        self.assertEqual(len(posts), 150)
        self.assertEqual(newest, "300")
        self.assertEqual(calls[1][0], "/users/42/timelines/reverse_chronological")
        self.assertEqual(calls[1][1]["since_id"], "99")
        self.assertEqual(calls[2][1]["max_results"], 50)  # second page only asks for what the cap allows

    def test_untracked_blog_needs_enough_sharers(self):
        now = datetime.now(timezone.utc)
        mentions = {
            "blog:new.blog/post-a": {"by": {"#a": 1, "#b": 2}, "url": "https://new.blog/post-a"},
            "blog:new.blog/post-b": {"by": {"#a": 1}, "url": "https://new.blog/post-b"},
        }

        def page(url, source, tier=3):
            return {"id": "blog:redirected", "kind": "blog", "source": source, "tier": tier,
                    "title": "Scaling laws for X", "summary": "We train models and find results.",
                    "url": url, "published": now.isoformat(), "body_chars": 0, "body_text": ""}

        with mock.patch.object(fetch, "fetch_page_item", side_effect=page) as get, \
                mock.patch.object(pipeline, "load_items", return_value=[]):
            out = pipeline._x_blogs(mentions, [], now - timedelta(days=21), {})
        self.assertEqual([i["id"] for i in out], ["blog:new.blog/post-a"])  # keyed like the mention
        self.assertEqual(get.call_count, 1)

    def test_update_without_credentials_keeps_and_prunes_state(self):
        old = (NOW - timedelta(days=40)).isoformat()
        state = {"since_id": "5", "mentions": {"arxiv:1": {"by": {"#a": 1}, "first_seen": NOW.isoformat()},
                                               "arxiv:2": {"by": {"#a": 1}, "first_seen": old}}}
        with mock.patch.dict("os.environ", {}, clear=True):
            out = xsource.update({}, state, NOW)
        self.assertEqual(list(out["mentions"]), ["arxiv:1"])
        self.assertEqual(out["since_id"], "5")


class RecommendTest(unittest.TestCase):
    def test_interest_matching(self):
        rows = [
            paper("Sparse autoencoders recover interpretable features from transformer activations; "
                  "we steer the model with these features.", title="SAE features", quality=50.0),
            paper("A new benchmark for robotic grasping with a parallel gripper in cluttered scenes.",
                  title="Grasping benchmark", quality=70.0),
        ] + [paper(f"Filler abstract about topic {k} and dataset {k}.", title=f"Filler {k}", quality=30.0)
             for k in range(20)]
        for k, r in enumerate(rows):
            r["id"] = f"arxiv:2610.{k:05d}"
            r["published"] = datetime.now(timezone.utc).isoformat()
        with tempfile.TemporaryDirectory() as d:
            items_dir = Path(d)
            (items_dir / f"{datetime.now(timezone.utc):%Y-%m-%d}.jsonl").write_text(
                "".join(json.dumps(r) + "\n" for r in rows))
            with mock.patch.object(pipeline, "ITEMS", items_dir):
                out, terms = recommend.recommend([], "sparse autoencoders, interpretable features, steering", n=3)
        self.assertEqual(out[0]["title"], "SAE features")

    def test_repo_profile_reads_docs_and_deps(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "README.md").write_text("# Speedrun\nFast training of small vision models with Muon.")
            Path(d, "requirements.txt").write_text("torch\ntriton\n")
            Path(d, "train.py").write_text('def warmup_schedule():\n    """Linear warmup."""\n')
            Path(d, "node_modules").mkdir()
            Path(d, "node_modules", "junk.md").write_text("ignore me entirely")
            prof = recommend.profile_text(d)
        self.assertIn("Muon", prof["docs"])
        self.assertNotIn("ignore", prof["docs"])
        self.assertIn("gpu kernels", prof["deps"])
        self.assertIn("warmup schedule", prof["code"])


if __name__ == "__main__":
    unittest.main()
