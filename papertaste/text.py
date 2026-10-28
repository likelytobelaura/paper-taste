"""Tokenizing, TF-IDF vectors and sparse cosine similarity (stdlib only)."""

import html
import math
import re
from collections import Counter, defaultdict

STOP = set("""
a about above after again against all also am an and any are as at be because been before being
below between both but by can could did do does doing down during each few for from further had has
have having he her here hers him his how i if in into is it its itself just me more most my no nor not
now of off on once only or other our ours out over own same she should so some such than that the
their them then there these they this those through to too under until up very was we were what when
where which while who whom why will with you your yours via using use used uses based new paper
propose proposed proposes approach method methods model models show shows shown results result
however may one two three well within without toward towards work study present presents
introduce introduces existing different given various several often make makes made thus whether
first second also include includes including further many much less across able achieve achieves
https http www com org html github arxiv pdf abs
""".split())

TOKEN = re.compile(r"[a-z][a-z0-9]+(?:-[a-z0-9]+)*")
TAG = re.compile(r"<[^>]+>")
SPACE = re.compile(r"\s+")
CAMEL = re.compile(r"(?<=[a-z])(?=[A-Z])")


def strip_html(text):
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", text or "")
    return SPACE.sub(" ", html.unescape(TAG.sub(" ", text))).strip()


def tokens(text, bigrams=True):
    words = [w for w in TOKEN.findall(text.lower()) if len(w) > 2 and w not in STOP]
    if bigrams:
        words += [a + "_" + b for a, b in zip(words, words[1:])]
    return words


def split_identifier(name):
    """trainStepFn / train_step_fn -> 'train step fn'."""
    return " ".join(CAMEL.sub(" ", name).replace("_", " ").split())


class TfIdf:
    def __init__(self, docs):
        df = Counter()
        for toks in docs:
            df.update(set(toks))
        self.n = len(docs)
        self.df = df
        self.idf = {t: math.log((1 + self.n) / (1 + c)) + 1 for t, c in df.items()}
        self.default_idf = math.log(1 + self.n) + 1

    def vector(self, toks, top=None):
        tf = Counter(toks)
        vec = {t: (1 + math.log(c)) * self.idf.get(t, self.default_idf) for t, c in tf.items()}
        if top and len(vec) > top:
            vec = dict(sorted(vec.items(), key=lambda kv: -kv[1])[:top])
        norm = math.sqrt(sum(w * w for w in vec.values())) or 1.0
        return {t: w / norm for t, w in vec.items()}


def cosine(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum(w * b.get(t, 0.0) for t, w in a.items())


def nearest_neighbours(queries, pool, skip_same=True):
    """For each query vector, the max cosine against pool vectors and how many exceed 0.3.

    Vectors are truncated (TfIdf.vector(top=...)) so an inverted index keeps this fast.
    queries/pool: lists of (key, vec). Returns {key: (max_sim, n_close)}.
    """
    index = defaultdict(list)
    for j, (_, vec) in enumerate(pool):
        for t, w in vec.items():
            index[t].append((j, w))
    out = {}
    for key, vec in queries:
        acc = defaultdict(float)
        for t, w in vec.items():
            for j, w2 in index.get(t, ()):
                acc[j] += w * w2
        sims = [s for j, s in acc.items() if not (skip_same and pool[j][0] == key)]
        out[key] = (max(sims, default=0.0), sum(1 for s in sims if s > 0.3))
    return out
