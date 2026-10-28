"""`recommend`: profile the user's repos and rank stored items by relevance x quality."""

import ast
import bisect
import math
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from . import score
from .pipeline import load_items
from .text import TfIdf, cosine, split_identifier, strip_html, tokens

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "env", "__pycache__", "dist", "build", "site-packages",
             ".mypy_cache", ".pytest_cache", ".next", "target", "vendor", "third_party", "wandb", "outputs",
             "checkpoints", "data", "datasets", ".claude", ".idea", ".vscode"}
DOC_EXT = {".md", ".rst", ".txt", ".tex"}
CODE_EXT = {".py", ".ipynb", ".rs", ".go", ".ts", ".js", ".jl", ".cpp", ".cu", ".c", ".h", ".scala", ".java"}
DEP_FILES = {"pyproject.toml", "requirements.txt", "setup.py", "setup.cfg", "environment.yml", "package.json",
             "Cargo.toml", "go.mod"}

# Dependencies say a lot about what a repo is about; map common ones to research vocabulary.
DEP_TOPICS = {
    "torch": "deep learning neural network training", "jax": "deep learning accelerator training",
    "transformers": "transformer language models pretrained", "vllm": "llm inference serving throughput",
    "sglang": "llm inference serving", "trl": "rlhf preference optimization reinforcement learning language models",
    "peft": "parameter efficient fine-tuning lora", "deepspeed": "distributed training large models",
    "accelerate": "distributed training", "flash-attn": "attention kernels efficient attention",
    "triton": "gpu kernels", "bitsandbytes": "quantization", "datasets": "datasets benchmarks",
    "inspect-ai": "evaluation benchmarks llm evals", "lm-eval": "evaluation benchmarks llm",
    "transformer-lens": "mechanistic interpretability circuits activations",
    "transformer_lens": "mechanistic interpretability circuits activations", "nnsight": "interpretability activations",
    "sae-lens": "sparse autoencoders interpretability features", "gymnasium": "reinforcement learning environments",
    "gym": "reinforcement learning environments", "stable-baselines3": "reinforcement learning",
    "diffusers": "diffusion models image generation", "timm": "vision models image classification",
    "torchvision": "computer vision", "opencv-python": "computer vision", "langchain": "llm agents retrieval",
    "llama-index": "retrieval augmented generation", "faiss": "vector search retrieval embeddings",
    "sentence-transformers": "embeddings retrieval", "scanpy": "single-cell genomics", "anndata": "single-cell genomics",
    "rdkit": "molecules chemistry", "pyg": "graph neural networks", "torch-geometric": "graph neural networks",
    "dgl": "graph neural networks", "mujoco": "robotics simulation control", "openai": "llm api agents",
    "anthropic": "llm api agents", "modal": "gpu cloud training", "wandb": "experiment tracking training",
    "levanter": "language model pretraining jax", "haliax": "language model pretraining jax", "ray": "distributed",
    "unsloth": "fine-tuning lora", "mlx": "on-device inference", "ollama": "local llm inference",
    "scikit-learn": "machine learning classical", "xgboost": "gradient boosting tabular", "pymc": "bayesian inference",
    "numpyro": "bayesian inference probabilistic programming", "lightning": "deep learning training",
}


def _read(path, limit=200_000):
    try:
        if path.stat().st_size > limit:
            return ""
        return path.read_text(errors="ignore")
    except OSError:
        return ""


def _python_terms(src):
    """Identifiers, docstrings and comments from Python source — not keywords and syntax."""
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return " ".join(re.findall(r"#\s*(.+)", src))
    parts = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            parts.append(split_identifier(node.name))
            doc = ast.get_docstring(node)
            if doc:
                parts.append(doc)
        elif isinstance(node, ast.Module) and ast.get_docstring(node):
            parts.append(ast.get_docstring(node))
    parts += re.findall(r"#\s*(.+)", src)
    return " ".join(parts)


def profile_text(repo, max_files=400):
    """Weighted bag of words describing a repo: docs x3, deps x2, code identifiers/comments x1."""
    repo = Path(repo).expanduser().resolve()
    docs, code, deps = [], [], []
    n = 0
    for path in sorted(repo.rglob("*"), key=lambda p: (len(p.parts), str(p))):
        if n >= max_files:
            break
        if any(part in SKIP_DIRS or part.startswith(".") for part in path.relative_to(repo).parts[:-1]):
            continue
        if not path.is_file():
            continue
        name, ext = path.name, path.suffix.lower()
        if name in DEP_FILES:
            text = _read(path).lower()
            deps += [topic for dep, topic in DEP_TOPICS.items() if re.search(rf"(^|[\s\"'=,\[]){re.escape(dep)}\b", text)]
        elif ext in DOC_EXT:
            docs.append(strip_html(_read(path))[:20000])
            n += 1
        elif ext == ".py":
            code.append(_python_terms(_read(path)))
            n += 1
        elif ext in CODE_EXT:
            src = _read(path)
            code.append(" ".join(split_identifier(w) for w in re.findall(r"[A-Za-z_][A-Za-z0-9_]{3,}", src)[:3000]))
            n += 1
    return {"docs": " ".join(docs), "deps": " ".join(deps), "code": " ".join(code)}


# Words common in code and READMEs that say nothing about research interests.
GENERIC = set("""
add get set put check run runs running file files path paths dir folder line lines row rows column columns
cell cells table format type types return returns none null true false yes value values key keys item items
list dict string str int float bool number count size length index default optional required define defined
needed need property prefix suffix copy draw date time cap record records read reads write writes load save
static base held minor major variable variables version versions update updates build install setup config
submission submit walk script scripts test tests example examples usage note notes todo readme docs call
calls output outputs input inputs print log logs error errors option options flag flags main init class
object function functions method arg args kwargs param params result final step steps start end stop first
last next prev current old new local remote user users name names id ids url api cli env cpu device card
""".split())


def profile_counts(repos):
    """Weighted term counts across repos: docs > deps > code (identifiers are mostly noise)."""
    counts = Counter()
    for repo in repos:
        p = profile_text(repo)
        for part, w in (("docs", 3.0), ("deps", 2.0), ("code", 0.5)):
            for t in tokens(p[part]):
                counts[t] += w * (1.5 if "_" in t else 1.0)  # bigrams are more specific
    return counts


def profile_vector(counts, tfidf, top=300, min_df=3):
    # Terms nearly every abstract uses ("model", "training") carry no preference. For repo text,
    # also require a few papers to use the term, so stray identifiers don't fill the profile;
    # stated interests keep even a term only one paper matches.
    def specific(t):
        df = tfidf.df.get(t, 0)
        if "_" in t:
            return max(1, min_df - 1) <= df <= 0.15 * tfidf.n and not all(w in GENERIC for w in t.split("_"))
        return t not in GENERIC and min_df <= df <= max(0.04 * tfidf.n, 1)

    vec = {t: (1 + math.log(c)) * tfidf.idf[t] for t, c in counts.items() if specific(t)}
    vec = dict(sorted(vec.items(), key=lambda kv: -kv[1])[:top])
    norm = math.sqrt(sum(w * w for w in vec.values())) or 1.0
    return {t: w / norm for t, w in vec.items()}


def top_terms(vec, n=20):
    return [t.replace("_", " ") for t, _ in sorted(vec.items(), key=lambda kv: -kv[1])[:n]]


def recommend(repos, interests="", days=14, n=15, kind=None, now=None, min_quality=0):
    now = now or datetime.now(timezone.utc)
    items = [i for i in load_items(days, now) if kind in (None, i["kind"]) and i["quality"] >= min_quality]
    if not items:
        return [], []
    docs = [tokens(i["title"] + " " + i["title"] + " " + i.get("summary", "")) for i in items]
    tfidf = TfIdf(docs)
    # Interests are the user's (or their agent's) own words, so they outweigh what the repos imply.
    parts = [(profile_vector(profile_counts(repos), tfidf), 0.35 if interests else 1.0)] if repos else []
    if interests:
        parts.append((profile_vector(Counter(tokens(interests)), tfidf, min_df=1), 0.65 if repos else 1.0))
    prof = Counter()
    for vec, w in parts:
        for t, x in vec.items():
            prof[t] += w * x
    norm = math.sqrt(sum(x * x for x in prof.values())) or 1.0
    prof = {t: x / norm for t, x in prof.items()}
    rel = [cosine(prof, tfidf.vector(d)) for d in docs]
    top_rel = max(rel) or 1.0
    # blog and paper quality are on different scales (source prior vs. abstract evidence): use within-kind percentiles
    qual = {k: sorted(i["quality"] for i in items if i["kind"] == k) for k in ("paper", "blog")}
    out = []
    for i, r, d in zip(items, rel, docs):
        p = r / top_rel
        qs = qual[i["kind"]]
        q = bisect.bisect_left(qs, i["quality"]) / max(1, len(qs) - 1) * score.recency(i["published"], now)
        combined = 0.6 * p + 0.4 * q
        matched = sorted({t for t in set(d) if t in prof}, key=lambda t: -prof[t])[:6]
        out.append({**i, "relevance": round(r, 4), "relevance_norm": round(p, 3),
                    "match_score": round(100 * combined, 1), "matched_terms": [t.replace("_", " ") for t in matched]})
    out.sort(key=lambda i: -i["match_score"])
    return out[:n], top_terms(prof)
