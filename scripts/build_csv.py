"""Regenerate data/speakers.csv from wiki/speakers/*.md frontmatter. Never hand-edit the CSV.

Usage: python3 -I scripts/build_csv.py
"""
import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
COLUMNS = [
    "slug", "category", "wall_voiced", "brand", "model", "status", "price_usd_pair", "price_checked", "nominal_impedance_ohm",
    "min_impedance_ohm", "min_impedance_hz", "impedance_flag", "epdr_min_ohm", "sensitivity_db_2v83",
    "sensitivity_claimed_db", "f3_hz", "f6_hz", "lw_deviation_db", "on_axis_deviation_db",
    "hor_beamwidth_deg", "ver_beamwidth_deg", "di_smoothness", "crossover_hz", "max_spl_db",
    "thd_86db_pct", "thd_96db_pct", "pref_score", "pref_score_sub", "woofer_in", "tweeter_type", "port",
    "dimensions_mm", "weight_kg", "critic_consensus", "user_consensus", "sources", "last_updated",
]


def frontmatter(path):
    text = path.read_text()
    if not text.startswith("---"):
        return None
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)


def main():
    rows, extra = [], []
    for p in sorted((ROOT / "wiki" / "speakers").glob("*.md")):
        fm = frontmatter(p)
        if not fm or fm.get("type") != "speaker":
            continue
        for k in fm:
            if k not in COLUMNS and k != "type" and k not in extra:
                extra.append(k)
        rows.append(fm)
    cols = COLUMNS + extra
    out = ROOT / "data" / "speakers.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for fm in rows:
            row = {}
            for c in cols:
                v = fm.get(c)
                if isinstance(v, list):
                    v = ";".join(str(x) for x in v)
                row[c] = "" if v is None else v
            w.writerow(row)
    print(f"wrote {out.relative_to(ROOT)}: {len(rows)} speakers, {len(cols)} columns")


if __name__ == "__main__":
    main()
