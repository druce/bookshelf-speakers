"""Quote scalar frontmatter values that break YAML (e.g. unquoted text containing ': ').

Usage: python3 -I scripts/fix_frontmatter.py [paths...]   (default: wiki/**/*.md)
Only touches files whose frontmatter fails to parse; only rewrites offending `key: value` lines.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LINE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s(.*)$")


def fix(path):
    text = path.read_text()
    if not text.startswith("---"):
        return False
    _, fm, body = text.split("---", 2)
    try:
        yaml.safe_load(fm)
        return False
    except yaml.YAMLError:
        pass
    out = []
    for line in fm.split("\n"):
        m = LINE.match(line)
        if m:
            key, val = m.groups()
            v = val.strip()
            if v and v[0] not in "\"'[{|>" and not re.fullmatch(r"-?[\d.]+|null|true|false", v):
                try:
                    ok = isinstance(yaml.safe_load(f"k: {v}"), dict)
                except yaml.YAMLError:
                    ok = False
                if not ok:
                    line = f"{key}: {json.dumps(v, ensure_ascii=False)}"
        out.append(line)
    new_fm = "\n".join(out)
    yaml.safe_load(new_fm)  # raise if still broken
    path.write_text("---" + new_fm + "---" + body)
    return True


if __name__ == "__main__":
    paths = [Path(p) for p in sys.argv[1:]] or list((ROOT / "wiki").rglob("*.md"))
    for p in paths:
        try:
            if fix(p):
                print(f"fixed {p}")
        except Exception as e:  # noqa: BLE001
            print(f"STILL BROKEN {p}: {e}")
