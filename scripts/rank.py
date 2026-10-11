"""Generate ranking/comparison pages from data/speakers.csv (never by eye — Claude.md §5 Query).

Usage: python3 -I scripts/rank.py
Writes:
  wiki/comparisons/ranked-by-price-band.md
  wiki/comparisons/impedance-honesty.md
  wiki/comparisons/sensitivity-claims-vs-measured.md
Hand-written commentary lives in each page's "## Notes" section, which is preserved between regenerations.
"""
import csv
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMP = ROOT / "wiki" / "comparisons"
BANDS = [(0, 300, "< $300"), (300, 600, "$300–600"), (600, 1200, "$600–1,200"),
         (1200, 2500, "$1,200–2,500"), (2500, 10 ** 9, "> $2,500")]


def f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def d(v, dec=1, pre="", post=""):
    return "—" if v is None else f"{pre}{v:.{dec}f}{post}"


def keep_notes(path):
    if path.exists():
        t = path.read_text()
        if "## Notes" in t:
            return t[t.index("## Notes"):].split("\n## Related")[0].rstrip() + "\n"
    return "## Notes\n_(none yet)_\n"


def rig(r):
    p = (r.get("primary_measurement") or "").split("-")[0]
    tier_b = {"napilopez", "archimago", "ageve", "mtg90", "mab", "nuyes", "stereophile", "hifinews", "hifiworld", "avmentor"}
    return {"eac": "EAC", "asr": "ASR", "audioholics": "Audioholics", "soundstage": "NRC", "nrc": "NRC"}.get(p, p) + (" (B)" if p in tier_b else "")


def lw_label(x):
    if x is None:
        return ""
    return "excellent" if x <= 1.5 else "good" if x <= 2.5 else "fair" if x <= 3.5 else "coloured"


def f3_label(x):
    if x is None:
        return ""
    return "excellent" if x < 45 else "good" if x <= 60 else "modest" if x <= 75 else "needs sub"


def page(path, slug, title, summary, intro, body, related):
    notes = keep_notes(path)
    path.write_text("\n".join([
        "---", "type: comparison", f"slug: {slug}", f"summary: {summary}", "generated_by: scripts/rank.py",
        "last_updated: 2026-10-11", "---", f"# {title}", "", intro, "", body, "", notes, "## Related", related, ""]))


def main():
    rows = list(csv.DictReader(open(ROOT / "data" / "speakers.csv")))
    for r in rows:
        for k in ("price_usd_pair", "pref_score", "pref_score_sub", "lw_deviation_db", "f3_hz", "sensitivity_db_2v83",
                  "sensitivity_claimed_db", "min_impedance_ohm", "nominal_impedance_ohm", "thd_96db_pct", "thd_86db_pct",
                  "epdr_min_ohm"):
            r[k] = f(r.get(k))
    cur = [r for r in rows if r["status"] == "current"]

    # 1. ranked by price band
    out = []
    ranked = [r for r in cur if r["pref_score_sub"] is not None]
    unranked = [r for r in cur if r["pref_score_sub"] is None]
    for lo, hi, label in BANDS:
        band = sorted([r for r in ranked if r["price_usd_pair"] is not None and lo <= r["price_usd_pair"] < hi],
                      key=lambda r: (-r["pref_score_sub"], r["price_usd_pair"]))
        out += [f"### {label} per pair ({len(band)} with a preference score)", "",
                "| # | Speaker | $/pr | Pref w/sub | Pref | LW ±dB | f3 Hz | Sens. dB | Min Ω (flag) | THD 96 dB % | Rig | Group |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        if band:
            top = band[0]["pref_score_sub"]
        for i, r in enumerate(band, 1):
            grp = "A" if top - r["pref_score_sub"] < 0.5 else ("B" if top - r["pref_score_sub"] < 1.0 else "")
            flag = {"effectively-4ohm": " ⚑4Ω", "below-iec": " ⚑IEC"}.get(r["impedance_flag"], "")
            out.append(
                f"| {i} | [[{r['slug']}]] | {d(r['price_usd_pair'], 0, '$')} | {d(r['pref_score_sub'])} | {d(r['pref_score'])} | "
                f"{d(r['lw_deviation_db'])} {lw_label(r['lw_deviation_db'])} | {d(r['f3_hz'], 0)} {f3_label(r['f3_hz'])} | "
                f"{d(r['sensitivity_db_2v83'])} | {d(r['min_impedance_ohm'])}{flag} | {d(r['thd_96db_pct'])} | {rig(r)} | {grp} |")
        out.append("")
    out += [f"### In scope but no preference score ({len(unranked)})", "",
            "These are measured by Tier A NRC or Tier B rigs (Stereophile, Hi-Fi News, hobbyists) that do not produce a "
            "full spinorama score. Compare them on their pages, not in this table.", ""]
    out += [", ".join(f"[[{r['slug']}]]" for r in sorted(unranked, key=lambda r: r["slug"]))]
    intro = ("Current, in-scope speakers with a spinorama-derived Olive preference score, sorted by **score with an ideal "
             "subwoofer** within each price band. Small bookshelf speakers are compared fairly on that score because bass "
             "extension dominates the no-sub score ([[preference-score]]). Per Claude.md §7, differences under 0.5 are not "
             "meaningful. Scores from Tier B hobbyist rigs are marked (B) and are less comparable. **Group A** = within 0.5 of the band leader; **Group B** = within 1.0. Rank inside a group is noise. "
             "The score ignores distortion, output and amplifier load, so the table also carries LW deviation "
             "([[listening-window]]), f3 ([[bass-extension-vs-room-gain]]), sensitivity, measured minimum impedance with its "
             "flag ([[impedance-and-epdr]]) and THD at 96 dB. Labels follow Claude.md §7. Generated by `scripts/rank.py` from "
             "`data/speakers.csv`.")
    page(COMP / "ranked-by-price-band.md", "ranked-by-price-band", "Ranked by price band",
         f"{len(ranked)} current speakers with preference scores, grouped by price band; Group A = within 0.5 of band leader",
         intro, "\n".join(out), "[[overview]] · [[candidate-universe]] · [[impedance-honesty]] · [[sensitivity-claims-vs-measured]] · [[preference-score]]")

    # 2. impedance honesty
    zr = sorted([r for r in cur if r["min_impedance_ohm"] is not None], key=lambda r: r["min_impedance_ohm"])
    n_flag = sum(1 for r in zr if r["impedance_flag"])
    n4 = sum(1 for r in zr if r["impedance_flag"] == "effectively-4ohm")
    by_rating = {}
    for z in (6.0, 8.0):
        g = [r for r in zr if r["nominal_impedance_ohm"] == z]
        by_rating[z] = (len(g), sum(1 for r in g if r["impedance_flag"]), sum(1 for r in g if r["impedance_flag"] == "effectively-4ohm"))
    body = ["| Speaker | Rated Ω | Measured min Ω | IEC floor | Flag | EPDR min Ω |", "|---|---|---|---|---|---|"]
    for r in zr:
        body.append(f"| [[{r['slug']}]] | {d(r['nominal_impedance_ohm'], 0)} | {d(r['min_impedance_ohm'])} | "
                    f"{d(0.8 * r['nominal_impedance_ohm']) if r['nominal_impedance_ohm'] else '—'} | {r['impedance_flag'] or '—'} | {d(r['epdr_min_ohm'])} |")
    intro = (f"Measured minimum impedance against each manufacturer's rating, for {len(zr)} current speakers with a measured "
             f"minimum. **{n_flag} of {len(zr)}** fall below the IEC 60268-5 floor of 80% of their rating, and **{n4}** dip "
             f"below 4.0 Ω (`effectively-4ohm`). Of the 8 Ω-rated models, {by_rating[8.0][1]} of {by_rating[8.0][0]} are below the floor "
             f"and {by_rating[8.0][2]} are effectively 4 Ω. Of the 6 Ω-rated models, {by_rating[6.0][1]} of {by_rating[6.0][0]} are below the floor "
             f"and {by_rating[6.0][2]} are effectively 4 Ω. Many minima are graph-read (approximate). See each speaker page "
             "and [[impedance-and-epdr]]. Sorted from lowest minimum up.")
    page(COMP / "impedance-honesty.md", "impedance-honesty", "Impedance honesty: rated vs measured",
         f"{n_flag} of {len(zr)} measured speakers fall below the IEC floor for their rating; {n4} are effectively 4 Ω loads",
         intro, "\n".join(body), "[[impedance-and-epdr]] · [[ranked-by-price-band]] · [[overview]]")

    # 3. sensitivity claims
    sr = [r for r in cur if r["sensitivity_db_2v83"] is not None and r["sensitivity_claimed_db"] is not None]
    for r in sr:
        r["delta"] = r["sensitivity_db_2v83"] - r["sensitivity_claimed_db"]
    sr.sort(key=lambda r: r["delta"])
    deltas = [r["delta"] for r in sr]
    body = ["| Speaker | Claimed dB (2.83 V) | Measured dB (2.83 V) | Δ dB | Measured source |", "|---|---|---|---|---|"]
    for r in sr:
        body.append(f"| [[{r['slug']}]] | {d(r['sensitivity_claimed_db'])} | {d(r['sensitivity_db_2v83'])} | {r['delta']:+.1f} | [[{r['primary_measurement']}]] |")
    intro = (f"Manufacturer sensitivity claims (normalised to 2.83 V where the speaker page converted them) against measured "
             f"sensitivity for {len(sr)} current speakers. Median shortfall **{st.median(deltas):+.1f} dB**; "
             f"{sum(1 for x in deltas if x <= -3)} of {len(sr)} miss their claim by 3 dB or more, and "
             f"{sum(1 for x in deltas if x >= 0)} meet or beat it. Measured values use different bands by source "
             "(computed: mean LW 300 Hz–3 kHz; Stereophile: B-weighted; Hi-Fi News: 500 Hz–8 kHz pink noise), so treat ±1 dB as "
             "noise. Some 'claims' are in-room or half-space figures, e.g. Klipsch. See [[sensitivity-normalization]].")
    page(COMP / "sensitivity-claims-vs-measured.md", "sensitivity-claims-vs-measured", "Sensitivity: claimed vs measured",
         f"Median measured sensitivity is {st.median(deltas):+.1f} dB vs claim across {len(sr)} speakers",
         intro, "\n".join(body), "[[sensitivity-normalization]] · [[ranked-by-price-band]] · [[overview]]")
    print(f"ranked {len(ranked)}, impedance {len(zr)} ({n_flag} flagged, {n4} 4Ω), sensitivity {len(sr)} (median {st.median(deltas):+.1f})")


if __name__ == "__main__":
    main()
