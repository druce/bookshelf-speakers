"""Set `wall_mount` frontmatter (after `port`) from data/wall-mount.json; unknown speakers get null.

Values: none | keyhole | threaded-insert | bracket-included | on-wall-design | null
data/wall-mount.json: {slug: {"value": ..., "source": "<source slug or note>", "note": "..."}}
Usage: python3 -I scripts/set_wall_mount.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    wm = json.loads((ROOT / "data" / "wall-mount.json").read_text())
    n = 0
    for p in (ROOT / "wiki" / "speakers").glob("*.md"):
        t = p.read_text()
        _, fm, body = t.split("---", 2)
        cat = re.search(r"^category:\s*(\S+)", fm, re.M)
        v = (wm.get(p.stem) or {}).get("value")
        if v is None and cat and cat.group(1) == "on-wall":
            v = "on-wall-design"
        fm = re.sub(r"^wall_mount:.*\n", "", fm, flags=re.M)
        line = f"wall_mount: {json.dumps(v)}\n"
        if re.search(r"^port:.*$", fm, re.M):
            fm = re.sub(r"^(port:.*\n)", r"\1" + line, fm, count=1, flags=re.M)
        else:
            fm = fm.rstrip("\n") + "\n" + line
        p.write_text("---" + fm + "---" + body)
        n += v is not None
    print(f"wall_mount set on {n} pages")


if __name__ == "__main__":
    main()
