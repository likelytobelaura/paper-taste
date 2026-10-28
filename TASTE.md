# Research taste rubric

The heuristic score in `data/` only sees metadata and abstracts. This rubric is for the second pass, when
an agent (or a person) actually opens the paper. It is the part that encodes *taste*: we would rather
recommend one paper that changes how you think than ten that add 0.4 points to a leaderboard.

Score each shortlisted item 1–5 on each axis, read the full text for anything that reaches the top 10,
and be willing to demote a paper with a great abstract and a thin experimental section.

## 1. Is there a real, falsifiable claim?
- **5:** One crisp claim you could disprove ("X causes Y under Z"), stated up front and tested directly.
- **3:** A method plus "it works better", with the mechanism left vague.
- **1:** A system/framework description with no claim that could turn out false.

## 2. Is the evidence proportionate to the claim?
- Strong baselines, **tuned with the same budget** as the proposed method (compute-matched, same data).
- Ablations that remove the contribution itself, not just hyperparameters.
- Variance: multiple seeds, confidence intervals, or at least reported spread. A 0.5-point gain with no
  error bars is noise until shown otherwise.
- Holds across scales, datasets, or model families, or is honest that it was only tested at one.
- For evals and benchmarks: contamination checks, held-out splits, validated judges. An LLM-as-judge
  needs agreement numbers against humans.

## 3. Does it explain, not just report?
Mechanistic insight, a clean controlled experiment, a theory that predicts the numbers, or a negative
result that kills a popular idea all count for more than a new SOTA. Ask: *after reading this, would I
design my next experiment differently?*

## 4. Is it new?
- Does it address the obvious prior work (and the concurrent arXiv papers with near-identical abstracts)?
- Is the contribution the idea, or a recombination of three known tricks on a new benchmark?
- The pipeline flags "near-duplicate" and "crowded topic". In a crowded topic, recommend the best paper,
  not all of them.

## 5. Can you build on it?
Code, weights, data, enough detail to reimplement. Reproducibility is a quality signal, not a courtesy.

## 6. Honesty
- Limitations section that names real limitations.
- No hype vocabulary ("revolutionary", "unprecedented", "is all you need") standing in for evidence.
- Qualitative examples that are representative rather than cherry-picked, ideally with failure cases shown.
- Results on closed APIs state model versions and dates.

## Red flags (demote unless the paper rebuts them)
- SOTA by under 1 point with no variance reported
- Baselines copied from other papers rather than rerun under the same setup
- New benchmark where the authors' own method is the only thing that does well
- "We find" claims supported by a single figure of hand-picked examples
- Abstract claims that the experiments section doesn't support
- Prompting-only papers whose result disappears with a stronger base model

## Green flags (promote)
- Pre-registered predictions, or a result the authors clearly didn't expect
- Careful negative results and replications
- Scaling sweeps showing *where* an effect appears or vanishes
- A small, surprising experiment that anyone could rerun in an afternoon
- Blog posts from researchers who show their working: full runs, failed attempts, released notebooks

## Output per recommended item
```
### <title> (<link>)
Verdict: must-read | worth reading | skim | skip    Taste score: <1–5 average>
Claim: <one sentence>
Why it's good: <evidence that convinced you, with section/figure references>
Caveats: <what would make you trust it more>
Why for you: <the connection to the reader's repo or interests, concretely>
```
