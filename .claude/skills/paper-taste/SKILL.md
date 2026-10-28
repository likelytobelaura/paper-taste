---
name: paper-taste
description: Recommend the best new AI research papers and lab blog posts for the user's repos and interests, using the paper-taste quality index plus a research-taste rubric. Use when asked "what should I read", "any new papers on X", "what's new that's relevant to this repo", or for a weekly reading list.
---

Follow [AGENTS.md](../../../AGENTS.md) in this repo. In short:

1. `git pull` (or `python3 -m papertaste update --no-s2` to rebuild locally).
2. Read the user's repo(s) and write a specific 2–4 sentence interests statement.
3. `python3 -m papertaste recommend --repo <path> --interests "<statement>" -n 40 --json`
4. Apply [TASTE.md](../../../TASTE.md): read the top abstracts critically and the top 5–8 in full.
5. Report 3–7 items in the TASTE.md output format, best first, saying which you read in full.
