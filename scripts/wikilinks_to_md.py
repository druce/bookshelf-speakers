"""Convert [[slug]] / [[slug|text]] wikilinks under wiki/ into relative markdown links that render on GitHub
(and still work in Obsidian). Run as the last step of every build; idempotent.

- Speaker pages link as their "Brand Model", brand pages as their name; everything else keeps the slug as text
  (or the alias after `|`).
- Links to screened speakers that have no page (known from data/ingest-packets-*.json) become plain text.
- Unknown targets are left as [[...]] and reported, so check_links.py flags them.

Usage: python3 -I scripts/wikilinks_to_md.py
"""
import glob
import json
import os
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]*))?\]\]")


def frontmatter(path):
    t = path.read_text()
    if t.startswith("---"):
        try:
            return yaml.safe_load(t.split("---", 2)[1]) or {}
        except yaml.YAMLError:
            return {}
    return {}


def build_maps():
    pages, labels = {}, {}
    for p in WIKI.rglob("*.md"):
        pages[p.stem] = p
        if p.parent.name in ("speakers", "brands"):
            fm = frontmatter(p)
            if fm.get("type") == "speaker" and fm.get("brand") and fm.get("model"):
                labels[p.stem] = f"{fm['brand']} {fm['model']}"
            elif fm.get("type") == "brand" and fm.get("name"):
                labels[p.stem] = str(fm["name"])
    unpaged = {}
    for f in glob.glob(str(ROOT / "data" / "ingest-packets-*.json")):
        for pk in json.load(open(f)):
            unpaged[pk["slug"]] = f"{pk['brand']} {pk['model']}"
    return pages, labels, unpaged


def convert_text(text, src, pages, labels, unpaged, unknown):
    def rep(m):
        slug, alias = m.group(1).strip(), m.group(2)
        if slug in pages:
            rel = os.path.relpath(pages[slug], src.parent).replace(os.sep, "/")
            label = (alias or labels.get(slug) or slug).replace("[", "(").replace("]", ")")
            return f"[{label}]({rel})"
        if slug in unpaged:
            return alias or unpaged[slug]
        unknown.add((str(src.relative_to(WIKI)), slug))
        return m.group(0)

    # do not touch fenced code blocks or inline code
    parts = re.split(r"(```.*?```|`[^`\n]*`)", text, flags=re.S)
    return "".join(p if i % 2 else WIKILINK.sub(rep, p) for i, p in enumerate(parts))


def main():
    pages, labels, unpaged = build_maps()
    unknown, changed = set(), 0
    for p in WIKI.rglob("*.md"):
        t = p.read_text()
        if t.startswith("---"):
            _, fm, body = t.split("---", 2)
            new = "---" + fm + "---" + convert_text(body, p, pages, labels, unpaged, unknown)
        else:
            new = convert_text(t, p, pages, labels, unpaged, unknown)
        if new != t:
            p.write_text(new)
            changed += 1
    print(f"converted links in {changed} files")
    for u in sorted(unknown):
        print("UNKNOWN", *u)


if __name__ == "__main__":
    main()
