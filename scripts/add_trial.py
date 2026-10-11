"""Set home-trial / return-policy frontmatter on speaker pages and build wiki/comparisons/returns-and-trials.md.

Inputs:
  data/seller-policies.json  {seller_slug: {name?, trial_days, free_return_shipping, restocking_fee, opened_ok,
                              conditions, named_trial, policy_url, no_hassle, ...}}
  data/speaker-sellers.json  [{slug, sellers: [{seller, url, status, price_usd_pair}], maker_direct, notes}]

Per speaker, among authorized US sellers not marked "sold out", choose the best policy:
no_hassle first, then the longest trial. Fields written right after `price_checked`:
  home_trial_days, no_hassle_return (true/false/null), trial_seller, trial_terms, trial_checked
"no-hassle" (per the human, 2026-10-11) = >=30 days AND opened, undamaged speakers returnable AND restocking fee
none or LOW (<= MAX_FEE_PCT percent, or a flat fee <= MAX_FLAT_FEE dollars). Return shipping may be paid by the buyer;
it is reported in trial_terms but does not decide no_hassle. Recomputed here from the policy fields, not taken from the
policy agent's own no_hassle guess.

Usage: python3 -I scripts/add_trial.py
"""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MAX_FEE_PCT = 10
MAX_FLAT_FEE = 50
FIELDS = ["home_trial_days", "no_hassle_return", "trial_seller", "trial_terms", "trial_checked"]


def terms(p):
    bits = []
    if p.get("trial_days"):
        bits.append(f"{p['trial_days']} days")
    frs = p.get("free_return_shipping")
    bits.append({True: "free return shipping", False: "buyer pays return shipping", "conditional": "return shipping conditional"}.get(frs, "return shipping unclear"))
    rf = p.get("restocking_fee")
    if rf in (None, ""):
        bits.append("restocking fee unclear")
    elif str(rf).lower() in ("none", "no", "0", "false"):
        bits.append("no restocking fee")
    else:
        bits.append(f"restocking fee: {rf}")
    return ", ".join(bits)


def fee_level(rf):
    """Return ('none'|'low'|'high'|None, text)."""
    if rf is None or str(rf).strip() == "":
        return None
    t = str(rf).lower()
    if t in ("none", "no", "0", "0%", "false") or t.startswith("none") or "no restocking" in t:
        return "none"
    pct = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*%", t)]
    usd = [float(x) for x in re.findall(r"\$\s*(\d+(?:\.\d+)?)", t)]
    if pct:
        return "low" if max(pct) <= MAX_FEE_PCT else "high"
    if usd:
        return "low" if max(usd) <= MAX_FLAT_FEE else "high"
    return None


def no_hassle(p):
    days, opened, lvl = p.get("trial_days"), p.get("opened_ok"), fee_level(p.get("restocking_fee"))
    if (days is not None and days < 30) or opened is False or lvl == "high":
        return False
    if days is None or opened is None or lvl is None:
        return None
    return True


def rank(p):
    nh = no_hassle(p)
    return (1 if nh is True else 0 if nh is None else -1, p.get("trial_days") or 0)


def main():
    pol = json.loads((ROOT / "data" / "seller-policies.json").read_text())
    sel = {r["slug"]: r for r in json.loads((ROOT / "data" / "speaker-sellers.json").read_text())}
    rows = []
    for page in sorted((ROOT / "wiki" / "speakers").glob("*.md")):
        text = page.read_text()
        _, fm_txt, body = text.split("---", 2)
        fm = yaml.safe_load(fm_txt)
        s = sel.get(page.stem, {"sellers": []})
        cands = []
        for x in s.get("sellers", []):
            if (x.get("status") or "").lower() == "sold out":
                continue
            p = pol.get(x["seller"])
            if p:
                cands.append((x["seller"], p, x))
        best = max(cands, key=lambda c: rank(c[1])) if cands else None
        if best:
            slug, p, x = best
            vals = {"home_trial_days": p.get("trial_days"), "no_hassle_return": no_hassle(p),
                    "trial_seller": p.get("name") or slug, "trial_terms": terms(p), "trial_checked": "2026-10-11"}
        else:
            vals = {"home_trial_days": None, "no_hassle_return": None, "trial_seller": None,
                    "trial_terms": "no verified authorized US seller policy", "trial_checked": "2026-10-11"}
        for k in FIELDS:
            fm_txt = re.sub(rf"^{k}:.*\n", "", fm_txt, flags=re.M)
        block = "".join(f"{k}: {json.dumps(vals[k])}\n" for k in FIELDS)
        if re.search(r"^price_checked:.*$", fm_txt, re.M):
            fm_txt = re.sub(r"^(price_checked:.*\n)", r"\1" + block.replace("\\", "\\\\"), fm_txt, count=1, flags=re.M)
        else:
            fm_txt = fm_txt.rstrip("\n") + "\n" + block
        page.write_text("---" + fm_txt + "---" + body)
        rows.append((page.stem, fm, vals, [c[0] for c in cands]))

    # comparison page
    out = ["---", "type: comparison", "slug: returns-and-trials",
           f"summary: In-home trial and return terms for {len(rows)} speakers; {sum(1 for r in rows if r[2]['no_hassle_return'] is True)} have a no-hassle option",
           "generated_by: scripts/add_trial.py", "last_updated: 2026-10-11", "---", "# Returns and in-home trials", "",
           "Whether each speaker can be bought from an authorized US seller with an in-home trial and a **no-hassle return**: "
           "at least 30 days, opened (in-home-used, undamaged) speakers accepted, and no or a low restocking fee (≤10% or a flat fee ≤$50). "
           "Buyer-paid return shipping is allowed; it is shown in the terms because it can cost $50–150 for a pair. "
           "The best qualifying seller is shown. Terms come from each seller's policy page on 2026-10-11; policies change "
           "and often exclude damaged, incomplete or non-original packaging returns. Generated by `scripts/add_trial.py` from "
           "`data/seller-policies.json` and `data/speaker-sellers.json`. Seller availability is a snapshot.", "",
           "## Seller policies", "", "| Seller | Days | Free return shipping | Restocking fee | Named trial | No-hassle | Policy |", "|---|---|---|---|---|---|---|"]
    for k, p in sorted(pol.items(), key=lambda kv: (-(1 if no_hassle(kv[1]) is True else 0), -(kv[1].get("trial_days") or 0))):
        out.append(f"| {p.get('name') or k} | {p.get('trial_days') or '—'} | {p.get('free_return_shipping')} | {p.get('restocking_fee') or '—'} | "
                   f"{'yes' if p.get('named_trial') else '—'} | {no_hassle(p)} | {('[link](' + p['policy_url'] + ')') if p.get('policy_url') else '—'} |")
    out += ["", "## Speakers", "", "| Speaker | No-hassle | Days | Best seller | Terms | Other sellers checked |", "|---|---|---|---|---|---|"]
    for slug, fm, v, c in sorted(rows, key=lambda r: (-(1 if r[2]["no_hassle_return"] is True else 0), -(r[2]["home_trial_days"] or 0), r[0])):
        out.append(f"| [[{slug}]] | {v['no_hassle_return']} | {v['home_trial_days'] or '—'} | {v['trial_seller'] or '—'} | {v['trial_terms']} | {', '.join(c) or '—'} |")
    out += ["", "## Related", "[[overview]] · [[ranked-by-price-band]] · [[candidate-universe]]", ""]
    (ROOT / "wiki" / "comparisons" / "returns-and-trials.md").write_text("\n".join(out))
    n = sum(1 for r in rows if r[2]["no_hassle_return"] is True)
    print(f"{len(rows)} speakers; no-hassle {n}; false {sum(1 for r in rows if r[2]['no_hassle_return'] is False)}; unknown {sum(1 for r in rows if r[2]['no_hassle_return'] is None)}")


if __name__ == "__main__":
    main()
    import sys as _s
    _s.path.insert(0, str(Path(__file__).resolve().parent))
    import wikilinks_to_md
    wikilinks_to_md.main()
