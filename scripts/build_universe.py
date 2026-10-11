"""Build wiki/comparisons/candidate-universe.md from Discover inputs and ingest verdicts.

Usage: python3 -I scripts/build_universe.py <scratch_dir>
Inputs:
  data/spinorama-passive-bookshelf.json        (spinorama Tier A/B/C passive bookshelf list)
  <scratch>/enrich/merged.json                  (quick-pass enrichment, unverified)
  <scratch>/ingest/packets.json                 (packets sent to ingest)
  <scratch>/ingest/results/*.json               (verified verdicts from ingest agents; authoritative)
Also writes data/candidate-universe.csv.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from slug import slugify  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def money(v):
    try:
        return f"${int(round(float(v))):,}"
    except (TypeError, ValueError):
        return "—"


def main(scratch):
    scratch = Path(scratch)
    spin = json.load(open(ROOT / "data" / "spinorama-passive-bookshelf.json"))
    enr = {r["name"]: r for r in json.load(open(scratch / "enrich" / "merged.json"))}
    packets = {p["slug"]: p for p in json.load(open(scratch / "ingest" / "packets.json"))}
    results = {}
    for f in (scratch / "ingest" / "results").glob("*.json"):
        try:
            r = json.load(open(f))
            results[r.get("slug") or f.stem] = r
        except Exception as e:  # noqa: BLE001
            print(f"bad sidecar {f}: {e}", file=sys.stderr)
    pages = {p.stem for p in (ROOT / "wiki" / "speakers").glob("*.md")}

    rows = []
    seen = set()
    for p in packets.values():
        r = results.get(p["slug"], {})
        urls = [m["review"] for m in p.get("measurements", []) if m.get("review")] + list(p.get("tier_a_hints") or [])
        tiers = sorted({m["tier"] for m in p.get("measurements", [])})
        verdict = r.get("verdict") or "not-verified"
        tier_ab = "y" if tiers or r.get("tier_ab_available") else ("n" if verdict == "no-tier-ab" or p["kind"] == "lineup" else "?")
        rows.append({
            "brand": p["brand"], "model": p["model"], "slug": p["slug"],
            "price": r.get("price_usd_pair") if r else None,
            "nominal": r.get("nominal_impedance_ohm"),
            "tier_ab": tier_ab, "tiers": "/".join(tiers) or ("A/B" if r.get("tier_ab_available") else ""),
            "verdict": verdict, "reason": r.get("reason") or "", "successor": r.get("successor") or "",
            "page": p["slug"] in pages, "urls": urls[:3], "origin": p["kind"],
        })
        if p.get("spinorama_name"):
            seen.add(p["spinorama_name"])

    # spinorama Tier A/B rows not sent to ingest (excluded at enrichment triage)
    for s in spin:
        if s["name"] in seen or s["best_tier"] not in "AB":
            continue
        e = enr.get(s["name"], {})
        z = e.get("nominal_impedance_ohm")
        if e.get("is_passive") is False:
            verdict, reason = "out-of-scope", "powered/active (quick pass)"
        elif e.get("is_diy"):
            verdict, reason = "diy", "DIY design/kit"
        elif e.get("status") == "discontinued":
            verdict, reason = "discontinued", "quick pass (unverified)"
        else:
            verdict, reason = "out-of-scope", f"rated {z} Ω (quick pass)"
        rows.append({
            "brand": s["brand"], "model": s["model"], "slug": slugify(f"{s['brand']} {s['model']}"),
            "price": e.get("price_usd_pair"), "nominal": z, "tier_ab": "y",
            "tiers": "/".join(sorted({m["tier"] for m in s["measurements"] if m["tier"] in "AB"})),
            "verdict": verdict, "reason": reason + ((" — " + e["notes"]) if e.get("notes") else ""),
            "successor": e.get("successor") or "", "page": False,
            "urls": [m["review"] for m in s["measurements"] if m["tier"] in "AB" and m.get("review")][:3],
            "origin": "spinorama",
        })

    def table(rs, cols):
        hdr = "| " + " | ".join(c for c, _ in cols) + " |\n|" + "---|" * len(cols) + "\n"
        return hdr + "\n".join("| " + " | ".join(fn(r) for _, fn in cols) + " |" for r in rs) + "\n"

    link = lambda r: f"[[{r['slug']}]]" if r["page"] else r["model"]  # noqa: E731
    urls = lambda r: " ".join(f"[{i + 1}]({u})" for i, u in enumerate(r["urls"])) or "—"  # noqa: E731
    base = [("Brand", lambda r: r["brand"]), ("Model", link), ("Price/pr", lambda r: money(r["price"])),
            ("Rated Ω", lambda r: str(r["nominal"] or "—")), ("Tier A/B data", lambda r: r["tier_ab"] + (f" ({r['tiers']})" if r["tiers"] else "")),
            ("Sources", urls)]
    groups = [
        ("In scope — ingested (speaker page exists)", lambda r: r["verdict"] == "in-scope" and r["page"], base),
        ("In scope — no Tier A/B measurement found", lambda r: r["verdict"] == "no-tier-ab", base[:5] + [("Note", lambda r: r["reason"][:80])]),
        ("Not yet verified", lambda r: r["verdict"] in ("not-verified",) or (r["verdict"] == "in-scope" and not r["page"]), base),
        ("Discontinued (excluded from rankings)", lambda r: r["verdict"] == "discontinued", base[:5] + [("Successor", lambda r: r["successor"] or "—")]),
        ("Out of scope (impedance, form factor, powered)", lambda r: r["verdict"] == "out-of-scope", base[:5] + [("Reason", lambda r: r["reason"][:90])]),
        ("DIY designs and kits (listed, not ranked)", lambda r: r["verdict"] == "diy", base[:5]),
    ]
    n_scope = sum(1 for r in rows if r["verdict"] in ("in-scope", "no-tier-ab"))
    n_tier = sum(1 for r in rows if r["verdict"] == "in-scope" and r["tier_ab"] == "y")
    md = ["---", "type: comparison", "slug: candidate-universe",
          f"summary: Discover output — {len(rows)} models screened, {n_scope} in scope, {n_tier} with Tier A/B data",
          "last_updated: 2026-10-11", "---", "# Candidate universe", "",
          "Built by `scripts/build_universe.py` from the [[spinorama-org]] passive-bookshelf list (Tier A/B entries), "
          "manufacturer lineup sweeps of about 40 brands, and the scope verdicts written by ingest. Ingest verdicts were checked "
          "against manufacturer spec pages and US retailers on 2026-10-11. Rows marked \"quick pass\" were excluded "
          "on a first search pass and not re-verified, so treat them as provisional. Scope: passive, rated 6 or 8 Ω, "
          "bookshelf or standmount, sold new in the US (Claude.md §2).", "",
          f"**Counts:** {len(rows)} screened · {n_scope} in scope · {n_tier} in scope with Tier A/B data.", ""]
    for title, pred, cols in groups:
        rs = sorted([r for r in rows if pred(r)], key=lambda r: (r["brand"].lower(), r["model"].lower()))
        md += [f"## {title} ({len(rs)})", "", table(rs, cols) if rs else "_None._\n"]
    md += ["## Related", "[[overview]] · [[spinorama-org]] · [[active-alternatives]]", ""]
    (ROOT / "wiki" / "comparisons" / "candidate-universe.md").write_text("\n".join(md))
    with open(ROOT / "data" / "candidate-universe.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["brand", "model", "slug", "price_usd_pair", "nominal_ohm", "tier_ab", "tiers", "verdict", "reason", "successor", "page", "urls"])
        for r in rows:
            w.writerow([r["brand"], r["model"], r["slug"], r["price"], r["nominal"], r["tier_ab"], r["tiers"], r["verdict"],
                        r["reason"], r["successor"], r["page"], " ".join(r["urls"])])
    print(f"universe: {len(rows)} rows, in scope {n_scope}, with tier A/B {n_tier}")


def finalize_links():
    """Generated text uses [[slug]]; convert to GitHub-renderable relative links."""
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    import wikilinks_to_md
    wikilinks_to_md.main()


if __name__ == "__main__":
    main(sys.argv[1])
    finalize_links()
