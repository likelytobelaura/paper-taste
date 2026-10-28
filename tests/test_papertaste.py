import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from papertaste import fetch, pipeline, recommend, score

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
