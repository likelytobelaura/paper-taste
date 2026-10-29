"""`site`: render the reading list as a self-contained web page (site/index.html)."""

import json
from datetime import datetime, timezone
from pathlib import Path

from .pipeline import ROOT, load_items

TEMPLATE = Path(__file__).with_name("site_template.html")
SITE = ROOT / "site"


def page_data(days=14, now=None):
    now = now or datetime.now(timezone.utc)
    rows = []
    for i in load_items(days, now):
        summary = i.get("summary", "")
        rows.append({
            "id": i["id"], "kind": i["kind"], "title": i["title"], "url": i["url"], "source": i.get("source"),
            "authors": [a["name"] for a in i.get("authors", [])[:3]], "n_authors": len(i.get("authors", [])),
            "published": i["published"], "quality": i["quality"], "reasons": i["reasons"], "flags": i["flags"],
            "summary": summary[:700].rsplit(" ", 1)[0] + "…" if len(summary) > 700 else summary,
            **({"github": i["hf"]["github"]} if (i.get("hf") or {}).get("github") else {}),
        })
    rows.sort(key=lambda r: -r["quality"])
    return {"generated": now.strftime("%Y-%m-%d %H:%M UTC"), "items": rows}


def render(days=14, now=None):
    """The page body (title, styles, markup, script) with today's data inlined."""
    data = json.dumps(page_data(days, now), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return TEMPLATE.read_text().replace('/*__DATA__*/{"generated": "", "items": []}', data)


def write(days=14, now=None):
    body = render(days, now)
    SITE.mkdir(exist_ok=True)
    doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
           f"{body.split('<style>')[0]}<style>{body.split('<style>', 1)[1].split('</style>', 1)[0]}</style>\n"
           f"</head>\n<body>\n{body.split('</style>', 1)[1]}\n</body>\n</html>\n")
    (SITE / "index.html").write_text(doc)
    return SITE / "index.html"
