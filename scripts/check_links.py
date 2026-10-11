"""Lint helper: report broken links, leftover [[wikilinks]], orphan pages and frontmatter parse errors under wiki/.

Usage: python3 -I scripts/check_links.py
Committed pages use relative markdown links (see scripts/wikilinks_to_md.py); any remaining [[...]] is reported.
"""
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parent.parent / "wiki"
MDLINK = re.compile(r"\[[^\]]*\]\(([^)\s]+\.md)(?:#[^)]*)?\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)[^\]]*\]\]")


def main():
    pages = {p.resolve(): p for p in ROOT.rglob("*.md")}
    inbound = defaultdict(set)
    broken, leftover, bad_fm = [], [], []
    for path in pages.values():
        text = path.read_text()
        if text.startswith("---"):
            try:
                yaml.safe_load(text.split("---", 2)[1])
            except Exception as e:  # noqa: BLE001
                bad_fm.append((path, str(e).splitlines()[0]))
        body = re.sub(r"```.*?```|`[^`\n]*`", "", text, flags=re.S)
        for target in MDLINK.findall(body):
            if target.startswith(("http://", "https://")):
                continue
            t = (path.parent / unquote(target)).resolve()
            if t in pages:
                if t != path.resolve():
                    inbound[t].add(path)
            else:
                broken.append((path.relative_to(ROOT), target))
        for w in WIKILINK.findall(body):
            leftover.append((path.relative_to(ROOT), w))
    special = {"index", "log", "overview"}
    orphans = [p for r, p in pages.items() if p.stem not in special and not inbound[r]]
    print(f"pages: {len(pages)}")
    print(f"broken links: {len(broken)}")
    for p, t in sorted(set(broken)):
        print(f"  {p} -> {t}")
    print(f"unconverted wikilinks: {len(leftover)}")
    for p, t in sorted(set(leftover))[:50]:
        print(f"  {p} -> [[{t}]]")
    print(f"orphans: {len(orphans)}")
    for p in sorted(orphans):
        print(f"  {p.relative_to(ROOT)}")
    print(f"frontmatter errors: {len(bad_fm)}")
    for p, e in bad_fm:
        print(f"  {p.relative_to(ROOT)}: {e}")


if __name__ == "__main__":
    main()
