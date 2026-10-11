"""Lint helper: report broken [[wikilinks]], orphan pages, and frontmatter parse errors under wiki/.

Usage: python3 -I scripts/check_links.py
"""
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent / "wiki"
LINK = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")


def main():
    pages = {p.stem: p for p in ROOT.rglob("*.md")}
    inbound = defaultdict(set)
    broken = []
    bad_fm = []
    for slug, p in pages.items():
        text = p.read_text()
        if text.startswith("---"):
            try:
                yaml.safe_load(text.split("---", 2)[1])
            except Exception as e:  # noqa: BLE001
                bad_fm.append((p, str(e).splitlines()[0]))
        for target in LINK.findall(text):
            t = target.strip()
            if t in pages:
                if t != slug:
                    inbound[t].add(slug)
            else:
                broken.append((p.relative_to(ROOT), t))
    special = {"index", "log", "overview"}
    orphans = [s for s in pages if s not in special and not inbound[s]]
    print(f"pages: {len(pages)}")
    print(f"broken links: {len(broken)}")
    for p, t in sorted(set(broken)):
        print(f"  {p} -> [[{t}]]")
    print(f"orphans: {len(orphans)}")
    for s in sorted(orphans):
        print(f"  {pages[s].relative_to(ROOT)}")
    print(f"frontmatter errors: {len(bad_fm)}")
    for p, e in bad_fm:
        print(f"  {p.relative_to(ROOT)}: {e}")


if __name__ == "__main__":
    main()
