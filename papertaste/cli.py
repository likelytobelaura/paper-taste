import argparse
import json
import sys

from . import pipeline, recommend


def _emit(items, as_json, header="", extra=None):
    if as_json:
        keep = ("id", "kind", "title", "url", "pdf", "source", "published", "quality", "reasons", "flags",
                "summary", "relevance_norm", "match_score", "matched_terms", "hf")
        json.dump([{k: i[k] for k in keep if k in i} for i in items], sys.stdout, indent=1, ensure_ascii=False)
        print()
        return
    if header:
        print(header)
    for k, i in enumerate(items):
        print(pipeline.fmt_item(k + 1, i, extra=extra(i) if extra else ""))


def main(argv=None):
    ap = argparse.ArgumentParser(prog="papertaste", description="Find the best new AI research to read.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    u = sub.add_parser("update", help="fetch + score new arXiv papers and blog posts, write data/ and DIGEST.md")
    u.add_argument("--no-s2", action="store_true", help="skip Semantic Scholar author signal")

    t = sub.add_parser("top", help="best recent items overall")
    t.add_argument("--days", type=int, default=7)
    t.add_argument("-n", type=int, default=20)
    t.add_argument("--kind", choices=["paper", "blog"])
    t.add_argument("--json", action="store_true")

    r = sub.add_parser("recommend", help="best recent items for your repos/interests")
    r.add_argument("--repo", action="append", default=[], help="path to a repo to profile (repeatable)")
    r.add_argument("--interests", default="", help="free-text interests, weighted heavily")
    r.add_argument("--days", type=int, default=14)
    r.add_argument("-n", type=int, default=15)
    r.add_argument("--kind", choices=["paper", "blog"])
    r.add_argument("--min-quality", type=float, default=0)
    r.add_argument("--json", action="store_true")

    a = ap.parse_args(argv)
    if a.cmd == "update":
        pipeline.run(use_s2=not a.no_s2)
    elif a.cmd == "top":
        _emit(pipeline.top(a.days, a.n, a.kind), a.json)
    elif a.cmd == "recommend":
        if not a.repo and not a.interests:
            ap.error("recommend needs --repo and/or --interests")
        items, terms = recommend.recommend(a.repo, a.interests, a.days, a.n, a.kind, min_quality=a.min_quality)
        _emit(items, a.json, header=f"Profile terms: {', '.join(terms)}\n",
              extra=lambda i: f" · match {i['match_score']:.0f} (relevance {i['relevance_norm']:.2f}; "
                              f"{', '.join(i['matched_terms'][:4])})")


if __name__ == "__main__":
    main()
