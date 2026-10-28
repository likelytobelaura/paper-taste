# Instructions for agents

You've been pointed at **paper-taste**: a daily-updated, quality-ranked index of new AI research (arXiv
plus lab and researcher blogs). Your job is to surface the few new papers most worth this user's time,
**given their own repos and interests**, and to apply real research taste while doing it.

Requirements: Python ≥ 3.11, stdlib only. No API keys or `pip install` needed.

## Workflow

1. **Get fresh data.** If this is a clone, run `git pull` (a GitHub Action updates `data/` daily). To
   rebuild locally instead: `python3 -m papertaste update --no-s2` (~1 min, network reads only).

2. **Understand the user.** Read the README, docs, and main modules of each repo the user pointed you at.
   Write a 2–4 sentence *interests* statement in research vocabulary: the problems, methods, model
   families, and evaluation settings the repo touches, plus what the user is likely trying to improve.
   Name specific techniques ("Muon optimizer, learning-rate warmup, FP8 training"), not just areas
   ("optimization"). This beats the tool's automatic repo profile by a wide margin.

3. **Get a shortlist.**
   ```bash
   python3 -m papertaste recommend --repo /path/to/their/repo [--repo ...] \
       --interests "<your statement>" --days 14 -n 40 --json
   ```
   Each row carries `quality` (0–100 heuristic), `reasons` (the evidence the heuristic found), `flags`
   (hype, near-duplicate, crowded topic, survey), `match_score`, and `matched_terms`.
   For the best items regardless of fit: `python3 -m papertaste top --days 7 -n 30 --json`
   (`--kind paper` / `--kind blog` to filter).
   If fewer than ~5 relevant hits come back, query the arXiv API for the user's specific topics
   (`https://export.arxiv.org/api/query?search_query=abs:"sparse autoencoder"&sortBy=submittedDate&sortOrder=descending&max_results=50`)
   and treat those results the same way.

4. **Apply taste.** Read [TASTE.md](TASTE.md). For the ~15 most promising shortlisted items, read the
   abstract critically. For the top 5–8, open the full text (`https://arxiv.org/html/<id>`, or the PDF
   if there is no HTML version) and check the experiments: baselines, ablations, variance, scale. Demote
   anything whose evidence doesn't support its abstract, and drop near-duplicates of a better paper.

5. **Report.** Give the user a short ranked list, usually 3–7 items, using the per-item format at the end
   of TASTE.md. Lead with the single paper you'd read first and why. Be explicit about what you read in
   full and what you judged from the abstract alone.

## Notes
- The heuristic `quality` is a prior, not a verdict. It rewards visible evidence of thoroughness and
  community attention (HF daily-paper upvotes) and penalises hype. A great paper with a terse abstract
  can score low; that's what step 4 is for.
- A reason like "shared on X by N accounts" means people on the repo owner's X timeline are sharing
  the item. That's useful attention, but it's attention, not evidence: still check the paper.
  Running `update` with the user's own X credentials (see README) personalises this to their timeline.
- Blog posts and papers are scored on different scales. `recommend` compares them by within-kind
  percentile.
- Data layout: `data/items/<published-date>.jsonl`, one JSON object per line, sorted by quality.
  `DIGEST.md` is the human-readable top list for the last 7 days.
- Don't open PRs or push to this repo on the user's behalf unless they ask. To suggest a new source,
  edit `sources.toml`.
