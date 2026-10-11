"""Run cta2034.compute over every raw/spinorama/<Speaker>/<key>/ directory and write data/cta2034-metrics.json.

Usage: python3 -I scripts/compute_all.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cta2034  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def main():
    out = {}
    for d in sorted((ROOT / "raw" / "spinorama").glob("*/*/")):
        if not (d / "SPL Horizontal.txt").exists():
            continue
        name, key = d.parent.name, d.name
        try:
            out.setdefault(name, {})[key] = cta2034.compute(d)
        except Exception as e:  # noqa: BLE001
            out.setdefault(name, {})[key] = {"error": str(e)}
            print(f"ERROR {name}/{key}: {e}", file=sys.stderr)
    dest = ROOT / "data" / "cta2034-metrics.json"
    dest.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"wrote {dest.relative_to(ROOT)}: {sum(len(v) for v in out.values())} measurements")


if __name__ == "__main__":
    main()
