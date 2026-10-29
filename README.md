# paper-taste

A daily, quality-ranked feed of new AI research, built to be read by **your coding agent** as well as by you.

1. **Scan**. Everything is free, needs no keys, and is listed in [`sources.toml`](sources.toml):
   - **arXiv:** every new submission in 8 core AI categories (cs.LG, cs.CL, cs.AI, cs.CV, stat.ML, cs.NE,
     cs.RO, cs.MA), plus 18 adjacent ones (IR, speech/audio, signal/image processing, security, HCI,
     systems, SE/PL, game theory, optimization, comp-neuro, …) filtered to papers that are about ML.
   - **111 lab, company, academic, and researcher blogs:** Anthropic (research, alignment, red team),
     Transformer Circuits, OpenAI, DeepMind and its safety team, Google Research, Meta AI, Apple ML, NVIDIA,
     Microsoft, Amazon, IBM, Thinking Machines, Goodfire, METR, Redwood, Apollo, Epoch, FAR.AI, UK AISI,
     Transluce, Sakana, Qwen, Liquid, Cohere Labs, Physical Intelligence, Ai2, Stanford CRFM, BAIR, CMU,
     Hazy, vLLM, PyTorch, and individual researchers (Lilian Weng, Karpathy, Olah, Dieleman, Steinhardt,
     Dettmers, Tri Dao, Horace He, Jason Wei, Yi Tay, Neel Nanda, Ben Recht, Ruder, …). Sites without a feed
     are scraped from their index pages.
   - **Shares**: AI-Twitter recaps (AINews) and 12 more newsletters (Import AI, Last Week in AI, Zvi,
     TheSequence, Ben's Bites, The Rundown, …). The X posts they link are resolved for free via FxTwitter.
     Also Hacker News, Reddit (r/MachineLearning, r/LocalLLaMA, r/mlscaling, …), Lobsters, and
     optionally your own X timeline (paid X API).
2. **Filter**: each item gets a 0–100 quality score from visible evidence of thoroughness (ablations,
   tuned baselines, seeds and error bars, scale sweeps, theory, released code, length, venue), community
   attention (HF daily-paper upvotes plus shares on X, in newsletters, and on HN/Reddit/Lobsters),
   novelty against the last 60 days, and a hype penalty.
   Lists are ranked by quality × recency (10-day half-life), so a strong paper rises above a merely new one.
3. **Recommend**: point your agent at this repo and your own repos. It profiles your code, pulls a
   shortlist, then applies the [research-taste rubric](TASTE.md) and reads the top papers in full.

**Today's reading list → [likelytobelaura.github.io/paper-taste](https://likelytobelaura.github.io/paper-taste/)**
(filter it, search it, and type your interests to re-rank it), or as Markdown in [DIGEST.md](DIGEST.md).

## Use it with an agent

Clone it and tell your agent (Claude Code, Codex, Cursor, …):

> Read `paper-taste/AGENTS.md` and recommend new papers for `~/my-project`.

Claude Code picks up the bundled skill (`.claude/skills/paper-taste`) when you work inside this repo.
[AGENTS.md](AGENTS.md) has the full workflow.

## Use it directly

Python ≥ 3.11, standard library only.

```bash
git clone https://github.com/likelytobelaura/paper-taste && cd paper-taste

python3 -m papertaste top --days 7 -n 20                    # best recent work overall
python3 -m papertaste top --kind blog                       # just lab/researcher posts
python3 -m papertaste recommend --repo ~/my-project \
    --interests "RL post-training of LLMs, reward hacking, verifiers"   # matched to you
python3 -m papertaste recommend --repo ~/a --repo ~/b --json         # machine-readable
python3 -m papertaste update                                # re-fetch + re-score (≈1 min)
```

## How the score works

| signal | papers | blogs | what it looks for |
|---|---|---|---|
| rigor | 30% | 25% | ablations, tuned/compute-matched baselines, multi-benchmark, scale sweeps, seeds/CIs, theory, controlled experiments, negative results, contamination checks |
| community | 20% | 15%* | Hugging Face daily-paper upvotes (log-scaled), combined with distinct sharers on X, in newsletters, HN, Reddit, Lobsters |
| novelty | 15% | 15% | TF-IDF distance to the nearest item in the last 60 days |
| depth | 13% | 15% | page/figure count, accepted at a main venue (workshop counts less); post length |
| artifacts | 12% | 5% | code, weights, or data released |
| authors | 10% | – | max author h-index via Semantic Scholar (only when `S2_API_KEY` is set) |
| source tier | – | 40% | prior for the outlet (see `sources.toml`) |
| hype | −12 pts max | | "revolutionary", "unprecedented", "is all you need", … |

\* only when share data is present (it is by default). Missing signals are dropped and the remaining weights renormalised. Each item records the `reasons`
and `flags` behind its score, so you can see why it ranked where it did. Blog posts must pass a
research gate that filters product launches, customer stories, and event recaps.

The heuristic is a prior; the taste comes from the second pass in [TASTE.md](TASTE.md).

## Automation

`.github/workflows/update.yml` runs `update` daily at 03:30 UTC (after the arXiv announcement) and commits
the new `data/` and `DIGEST.md`. Add an `S2_API_KEY` repository secret to enable the author signal.
Each day keeps the top 35% of arXiv papers by quality, plus anything with ≥5 HF upvotes.

## X / AI Twitter

**Free, on by default:** X has no free read API, and Nitter/xcancel have been offline since October 2026.
So paper-taste reads the newsletters that already digest AI Twitter every day:
[AINews](https://news.smol.ai) (now published inside Latent Space), DAIR.AI, and AlphaSignal. It
collects the X posts they link, then looks each one up through [FxTwitter](https://github.com/FxEmbed/FxEmbed)'s
free public API (`api.fxtwitter.com`, no auth) to get its links and like count. Shortened links
(goo.gle, buff.ly, …) are expanded. A typical AINews issue links 80–150 posts. The result reflects
the AI-Twitter consensus rather than your personal timeline. Add or remove recaps under
`[[x.curated_feeds]]` in `sources.toml`.

**Community aggregators** (`[aggregators]`): Hacker News stories with ≥20 points whose title looks
like AI/ML (Algolia API), top weekly posts from AI subreddits (RSS, because Reddit's JSON API now
returns 403 without OAuth, so Reddit contributes submissions but no scores), and Lobsters' `ai`/`ml`
tags. One submission with ≥100 points is enough to pull in a post from an untracked blog.

**Optional, paid: your own timeline.** With X API credentials set, each run also reads new posts
from your home timeline.

From both sources, arXiv, Hugging Face papers, alphaXiv, and blog links are extracted and used three ways:

- **Attention signal:** how many distinct accounts shared an item, with likes as a tiebreaker. For
  papers this is combined with HF upvotes.
- **Candidates the crawl missed:** shared arXiv papers up to 30 days old or outside the crawled categories,
  and posts from blogs not in `sources.toml` once at least 2 accounts share them. These still have to
  pass the research gate.
- **A digest section,** "Shared on X".

Credentials, as env vars or repo secrets:

| mode | variables | reads |
|---|---|---|
| OAuth 1.0a user context (recommended for CI; tokens don't expire) | `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` | your home timeline |
| OAuth 2.0 user token (local runs; expires after 2 h) | `X_USER_TOKEN` | your home timeline |
| App-only bearer token + `[x] list_id` | `X_BEARER_TOKEN` | an X List (e.g. one of AI researchers) |

Get the four OAuth 1.0a values from the X developer console: create an app, give it Read permission,
then generate the Access Token and Secret for your own account.

**Cost:** the X API bills per post read (about $0.005 each in 2026). Runs read at most `[x] max_posts`
(default 200, about $1/day) and never re-read posts from earlier runs.

**Privacy:** `data/` is public, so only aggregates are stored: share counts, likes, and *hashed* sharer
IDs. No post text is stored. Set `public_handles = true` to show @handles instead.

## Layout

```
papertaste/   fetch.py (arXiv, HF, RSS, HTML index pages) · xsource.py (X, newsletters) · social.py (HN, Reddit, Lobsters) · score.py · pipeline.py · recommend.py · cli.py
data/x_state.json   X read cursor + per-item share aggregates (hashed sharers)
data/items/   <published-date>.jsonl, scored items
data/seen.json   first-seen dates for blog posts without machine-readable dates
DIGEST.md     current top list (archived under data/digests/)
TASTE.md      rubric for the agent's second pass
AGENTS.md     instructions for agents
```

`python3 -m papertaste site` rebuilds the page (`site/index.html`) from stored data; `update` does it automatically.

Tests: `python3 -m unittest discover tests`
