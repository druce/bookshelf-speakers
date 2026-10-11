"""Replace [[slug]] links to speaker slugs that have no page with plain "Brand Model" text.

Usage: python3 -I scripts/unlink_missing.py data/ingest-packets-2026-10-11.json
Only rewrites links whose target is a known screened speaker slug without a wiki page; reports anything else.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINK = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")


def main(packets_path):
    names = {p["slug"]: f"{p['brand']} {p['model']}" for p in json.load(open(packets_path))}
    pages = {p.stem for p in WIKI.rglob("*.md")}
    unknown, fixed = set(), 0
    for p in WIKI.rglob("*.md"):
        t = p.read_text()

        def rep(m):
            nonlocal fixed
            tgt = m.group(1).strip()
            if tgt in pages:
                return m.group(0)
            if tgt in names:
                fixed += 1
                return m.group(2) or names[tgt]
            unknown.add((str(p.relative_to(WIKI)), tgt))
            return m.group(0)

        n = LINK.sub(rep, t)
        if n != t:
            p.write_text(n)
    print(f"unlinked {fixed}")
    for u in sorted(unknown):
        print("UNKNOWN", *u)


if __name__ == "__main__":
    main(sys.argv[1])
