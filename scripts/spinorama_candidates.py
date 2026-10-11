"""List passive bookshelf speakers from a spinorama.org metadata export, with evidence tier per measurement.

Usage: python3 -I scripts/spinorama_candidates.py raw/spinorama/spinorama-metadata-YYYY-MM-DD.json [out.json]
"""
import json
import sys

TIER_A = ("asr", "eac", "misc-audioholics", "princeton")
TIER_B_PREFIX = "misc-"
TIER_C = ("vendor", "misc-speakerdata2034")


def tier(key):
    if key.startswith(TIER_C):
        return "C"
    if key.startswith(TIER_A):
        return "A"
    if key.startswith(TIER_B_PREFIX):
        return "B"
    return "?"


def main(path, out=None):
    meta = json.load(open(path))
    rows = []
    for name, v in meta.items():
        if v.get("type") != "passive" or v.get("shape") != "bookshelves":
            continue
        ms = []
        for key, m in v["measurements"].items():
            pr = m.get("pref_rating", {})
            ms.append({
                "key": key,
                "origin": m.get("origin"),
                "tier": tier(key),
                "review": m.get("review") or next(iter((m.get("reviews") or {}).values()), None),
                "published": m.get("review_published"),
                "pref_score": pr.get("pref_score"),
                "pref_score_sub": pr.get("pref_score_wsub"),
                "spec_impedance": (m.get("specifications") or {}).get("impedance"),
            })
        best = min((m["tier"] for m in ms), default="?")
        rows.append({
            "name": name, "brand": v["brand"], "model": v["model"],
            "price": v.get("price"), "amount": v.get("amount") or v.get("amout"),
            "best_tier": best, "measurements": ms,
        })
    rows.sort(key=lambda r: (r["best_tier"], r["brand"].lower(), r["model"].lower()))
    if out:
        json.dump(rows, open(out, "w"), indent=1, ensure_ascii=False)
    return rows


if __name__ == "__main__":
    rows = main(*sys.argv[1:])
    from collections import Counter
    print(Counter(r["best_tier"] for r in rows))
