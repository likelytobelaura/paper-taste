"""Heuristic research-quality score for a paper or blog post.

This is the cheap first pass that runs on every new item. It reads only metadata and the
abstract (or post text), so it measures *evidence of thoroughness* — ablations, baselines,
variance, released code, length, venue, community attention, novelty — and penalises hype.
The deeper judgement happens when an agent applies TASTE.md to the shortlist.
"""

import math
import re
from datetime import datetime, timezone

# (label, regex, weight). Each matched label counts once.
RIGOR = [
    ("ablations", r"\bablat", 1.0),
    ("strong baselines", r"\b(baselines?|compute[- ]matched|tuned baselines?|fair comparison)\b", 0.6),
    ("multiple benchmarks", r"\bacross (\d+|several|multiple|diverse) (benchmarks|datasets|tasks|domains|environments|languages|model families)", 0.8),
    ("model-scale sweep", r"\b(scaling (law|laws|behavio|trend)|across (model )?scales|from \d+(\.\d+)?[mb] to \d+(\.\d+)?[mb]|\d+[mb]\s*(to|-|–)\s*\d+[mb] parameters)", 0.9),
    ("variance / significance", r"\b(random seeds|multiple seeds|\d+ seeds|confidence intervals?|standard (error|deviation)|error bars|statistically significant|bootstrap)", 1.0),
    ("theory", r"\b(we prove|theorem|provabl[ye]|upper bound|lower bound|convergence (rate|guarantee)|tight bound)", 0.8),
    ("mechanistic / causal analysis", r"\b(mechanis|causal(ly)? (intervention|analysis|effect)|we (explain|identify) why|interpretab|circuit)", 0.7),
    ("controlled experiments", r"\b(controlled (experiment|study|setting)s?|systematic(ally)? (study|evaluat|analy)|isolat(e|es|ing) the effect)", 0.8),
    ("reproduction / replication", r"\b(reproduc(e|ing|tion)|replicat(e|ing|ion))\b", 0.6),
    ("negative results / limitations", r"\b(fails? to|does not (improve|help|generalize|transfer)|limitations?|negative result|surprisingly,? (no|does not))", 0.7),
    ("human evaluation", r"\b(human (evaluation|study|raters|annotators|preference)|user study)", 0.5),
    ("contamination check", r"\b(contaminat|held[- ]out|leakage)", 0.5),
    ("quantified effect", r"\b\d+(\.\d+)?\s?(%|x|×|percentage points|pp)\b", 0.4),
]
ARTIFACTS = [
    ("code released", r"(github\.com/|gitlab\.com/|code (is|will be) (publicly )?(available|released)|open[- ]source[sd]? (our |the )?(code|implementation))", 1.0),
    ("weights/data released", r"(huggingface\.co/|we (release|open-source)|publicly release|release (our|the) (data|dataset|models?|weights|benchmark))", 0.8),
]
HYPE = re.compile(
    r"\b(revolutioni[sz]|groundbreaking|game[- ]chang|paradigm shift|unprecedented|unparalleled|remarkabl[ey]|"
    r"astonishing|incredibl[ey]|superhuman|agi\b|first[- ]ever|by a (large|wide) margin|dramatically|"
    r"significantly outperforms all|is all you need|unlock(s|ing)? the (full )?potential)", re.I)
VENUE = re.compile(
    r"\b(neurips|nips|icml|iclr|colt|aistats|uai|acl|emnlp|naacl|coling|colm|cvpr|iccv|eccv|aaai|ijcai|kdd|"
    r"tmlr|jmlr|nature|science|rss|corl|icra|siggraph)\b", re.I)
VENUE_ACCEPTED = re.compile(r"\b(accepted|to appear|camera[- ]ready|published|oral|spotlight|main conference)\b", re.I)
WORKSHOP = re.compile(r"\bworkshop\b", re.I)
PAGES = re.compile(r"(\d+)\s*pages", re.I)
FIGURES = re.compile(r"(\d+)\s*figures", re.I)
SURVEY = re.compile(r"\b(a survey|survey of|a review|literature review|tutorial|position paper|perspective|primer)\b", re.I)
NOT_RESEARCH = re.compile(
    r"\b(pricing|now available|generally available|partnership|partners with|customer story|case study|"
    r"webinar|hiring|join us|conference recap|announc(e|es|ing) (our|the) (new )?(app|product|plan)|"
    r"podcast|newsletter|roundup|links for|introducing [A-Z][a-z]+ (for|in) (business|enterprise|teams)|"
    r"foundation as a|platinum member|acquires|expands to|joins the)\b", re.I)
# "Acme cuts costs 76x with GPT-6" / "How Acme uses Claude to ..." — customer stories.
CUSTOMER = re.compile(
    r"\b(with|using|uses|use) (openai|chatgpt|codex|gpt-[\w.]+|claude|gemini|our models?)\b|"
    r"\b(cuts|halves|helps|brings|turns|streamlines?|reorganized|triples|doubles) .{0,60}\b(with|using)\b", re.I)
RESEARCH_WORDS = re.compile(
    r"\b(we (find|show|study|train|evaluate|measure|investigate|propose)|experiment|ablat|benchmark|dataset|"
    r"paper|arxiv|results|analysis|interpretab|alignment|scaling|training|evaluation|theorem|model behavio|"
    r"research|learning|reasoning|safety|world model|simulation|robot|language models?|discover|scientific|"
    r"architecture|inference|kernel|optimi[sz]|reinforcement|agents?\b|monitor|red[- ]team)", re.I)

TIER_PRIOR = {1: 0.9, 2: 0.65, 3: 0.4}


def _hits(table, text):
    return [(label, w) for label, pat, w in table if re.search(pat, text, re.I)]


def _sat(x, k):
    """Saturating 0..1 transform: x/(x+k)."""
    return x / (x + k) if x > 0 else 0.0


def signals(item, novelty=None, hf=None, s2=None):
    """Compute named 0..1 signals plus human-readable reasons for one item."""
    text = " ".join([item.get("title", ""), item.get("summary", ""), item.get("comment", ""),
                     item.get("body_text", "")[:20000]])
    sig, reasons, flags = {}, [], []

    rigor = _hits(RIGOR, text)
    sig["rigor"] = _sat(sum(w for _, w in rigor), 2.5)
    reasons += [label for label, _ in rigor if label != "quantified effect"]

    arts = _hits(ARTIFACTS, text)
    if hf and hf.get("github"):
        arts.append(("code released", 1.0))
    arts = dict(arts)
    sig["artifacts"] = min(1.0, sum(arts.values()) / 1.5)
    reasons += list(arts)

    hype = sorted({m.group(0).lower() for m in HYPE.finditer(text)})
    sig["hype"] = min(1.0, len(hype) / 3)
    if hype:
        flags.append("hype: " + ", ".join(hype[:4]))

    if item["kind"] == "paper":
        comment = item.get("comment", "")
        pages = max([int(p) for p in PAGES.findall(comment)] or [0])
        figs = max([int(f) for f in FIGURES.findall(comment)] or [0])
        venue = VENUE.search(comment)
        depth = _sat(pages, 15) * 0.7 + _sat(figs, 8) * 0.3 if pages or figs else 0.35
        if venue and VENUE_ACCEPTED.search(comment):
            depth = max(depth, 0.6 if WORKSHOP.search(comment) else 0.9)
            reasons.append(f"accepted: {venue.group(0)}" + (" workshop" if WORKSHOP.search(comment) else ""))
        if pages >= 25:
            reasons.append(f"{pages} pages")
        if len(item.get("summary", "")) < 500:
            depth *= 0.8
        sig["depth"] = depth
        up = (hf or {}).get("upvotes", 0)
        sig["community"] = min(1.0, math.log1p(up) / math.log1p(150))
        if up:
            reasons.append(f"HF daily papers: {up} upvotes")
        if s2:
            sig["authors"] = min(1.0, s2["max_h"] / 60)
            if s2["max_h"] >= 40:
                reasons.append(f"senior author (h-index {s2['max_h']})")
        n_auth = len(item.get("authors", []))
        if n_auth >= 15:
            reasons.append(f"{n_auth}-author team")
    else:
        chars = item.get("body_chars", 0)
        sig["depth"] = _sat(chars, 12000) if chars > 1500 else 0.3
        if chars > 25000:
            reasons.append(f"long-form ({chars // 1000}k chars)")
        sig["source"] = TIER_PRIOR.get(item.get("tier", 3), 0.4)
        reasons.append(f"source tier {item.get('tier', 3)}")

    if novelty is not None:
        max_sim, n_close = novelty
        sig["novelty"] = 1 - min(1.0, max(0.0, (max_sim - 0.15) / 0.5))
        if max_sim > 0.55:
            flags.append(f"near-duplicate of a recent item (sim {max_sim:.2f})")
        elif n_close >= 5:
            flags.append(f"crowded topic ({n_close} similar recent items)")

    if SURVEY.search(item.get("title", "")):
        flags.append("survey/position piece")
    return sig, reasons, flags


WEIGHTS = {
    "paper": {"rigor": 0.30, "artifacts": 0.12, "depth": 0.13, "community": 0.20, "authors": 0.10, "novelty": 0.15},
    "blog": {"source": 0.40, "rigor": 0.25, "artifacts": 0.05, "depth": 0.15, "novelty": 0.15},
}


def quality(item, sig, flags):
    """0..100. Missing signals are dropped and the remaining weights renormalised."""
    weights = {k: w for k, w in WEIGHTS[item["kind"]].items() if k in sig}
    q = sum(sig[k] * w for k, w in weights.items()) / sum(weights.values())
    q -= 0.12 * sig.get("hype", 0)
    if any(f.startswith("survey") for f in flags):
        q -= 0.05
    if any(f.startswith("near-duplicate") for f in flags):
        q -= 0.05
    return round(100 * max(0.0, min(1.0, q)), 1)


def is_research_post(item):
    """Gate for blog posts: tier-1 sources pass unless clearly non-research; others need research language.

    Posts whose feed gives only a one-line summary (and whose page we could not read) are judged on
    title + summary with a lower bar.
    """
    head = item["title"] + " " + item.get("summary", "")[:400]
    if NOT_RESEARCH.search(head) or CUSTOMER.search(item["title"]):
        return False
    tier = item.get("tier", 3)
    if tier == 1:
        return True
    if item.get("body_chars", 0) < 1500:
        return len(RESEARCH_WORDS.findall(head)) >= (1 if tier == 2 else 2)
    text = head + " " + item.get("body_text", "")[:6000]
    return len(RESEARCH_WORDS.findall(text)) >= (4 if tier == 2 else 8)


def recency(published, now=None, half_life_days=10):
    now = now or datetime.now(timezone.utc)
    age = (now - datetime.fromisoformat(published)).total_seconds() / 86400
    return 0.5 ** (max(0.0, age) / half_life_days)


def rank_score(item, now=None, half_life_days=10):
    """What lists are sorted by: quality, decayed by age so new work rises."""
    return item["quality"] * recency(item["published"], now, half_life_days)
