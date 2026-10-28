# paper-taste

A daily, quality-ranked feed of new AI research, built to be read by **your coding agent** as well as by you.

1. **Scan**: every new arXiv submission in cs.LG / cs.CL / cs.AI / cs.CV / stat.ML / cs.NE / cs.RO / cs.MA,
   plus ~35 lab and researcher blogs (Anthropic, Transformer Circuits, DeepMind, Google Research, OpenAI,
   Thinking Machines, Goodfire, METR, Redwood, Lilian Weng, Karpathy, Sander Dieleman, …). See [`sources.toml`](sources.toml).
2. **Filter**: each item gets a 0–100 quality score from visible evidence of thoroughness (ablations,
   tuned baselines, seeds and error bars, scale sweeps, theory, released code, length, venue), community
   attention (Hugging Face daily-paper upvotes), novelty against the last 60 days, and a hype penalty.
   Lists are ranked by quality × recency (10-day half-life), so a strong paper rises above a merely new one.
3. **Recommend**: point your agent at this repo and your own repos. It profiles your code, pulls a
   shortlist, then applies the [research-taste rubric](TASTE.md) and reads the top papers in full.

**Today's list → [DIGEST.md](DIGEST.md)**

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
| community | 20% | – | Hugging Face daily-paper upvotes (log-scaled) |
| novelty | 15% | 15% | TF-IDF distance to the nearest item in the last 60 days |
| depth | 13% | 15% | page/figure count, accepted at a main venue (workshop counts less); post length |
| artifacts | 12% | 5% | code, weights, or data released |
| authors | 10% | – | max author h-index via Semantic Scholar (only when `S2_API_KEY` is set) |
| source tier | – | 40% | prior for the outlet (see `sources.toml`) |
| hype | −12 pts max | | "revolutionary", "unprecedented", "is all you need", … |

Missing signals are dropped and the remaining weights renormalised. Each item records the `reasons`
and `flags` behind its score, so you can see why it ranked where it did. Blog posts must pass a
research gate that filters product launches, customer stories, and event recaps.

The heuristic is a prior; the taste comes from the second pass in [TASTE.md](TASTE.md).

## Automation

`.github/workflows/update.yml` runs `update` daily at 03:30 UTC (after the arXiv announcement) and commits
the new `data/` and `DIGEST.md`. Add an `S2_API_KEY` repository secret to enable the author signal.
Each day keeps the top 35% of arXiv papers by quality, plus anything with ≥5 HF upvotes.

## Layout

```
papertaste/   fetch.py (arXiv, HF, RSS, HTML index pages) · score.py · pipeline.py · recommend.py · cli.py
data/items/   <published-date>.jsonl, scored items
data/seen.json   first-seen dates for blog posts without machine-readable dates
DIGEST.md     current top list (archived under data/digests/)
TASTE.md      rubric for the agent's second pass
AGENTS.md     instructions for agents
```

Tests: `python3 -m unittest discover tests`
