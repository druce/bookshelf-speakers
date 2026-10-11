# Speaker ingest playbook (for subagents)

You are ingesting sources for a research wiki about **passive bookshelf/standmount speakers rated 6 Ω or 8 Ω, currently sold new in the US**. Repo: `/Users/drucev/projects/speakers`. Today: **2026-10-11**. First read `/Users/drucev/projects/speakers/CLAUDE.md` (the wiki schema). This playbook adds batch-specific rules; where they conflict, this playbook wins for mechanics (file names, what you may edit), CLAUDE.md wins for evidence standards.

You receive a list of **packets** (one per speaker). Process them in order. Run all python with `python3 -I` from the repo root (`cd /Users/drucev/projects/speakers && python3 -I scripts/...`).

## What you may write
- `raw/measurements/`, `raw/reviews-critic/`, `raw/reviews-user/`, `raw/manufacturer/`, `raw/assets/` — new files only, via the scripts below (or Write for user-review clips). Never modify an existing raw file.
- `wiki/sources/<slug>.md` — new source pages for documents you ingested.
- `wiki/speakers/<slug>.md` — the speaker page, only for speakers that pass the scope gate.
- `<SCRATCH>/ingest/results/<speaker-slug>.json` — one result sidecar per packet (ALWAYS, including out-of-scope).
- Do NOT edit: CLAUDE.md, wiki/index.md, wiki/log.md, wiki/overview.md, wiki/brands/*, wiki/reviewers/*, wiki/concepts/*, wiki/comparisons/*, data/*, scripts/*. Do not run git. The coordinator does all of that.

`<SCRATCH>` = `/private/tmp/claude-501/-Users-drucev-projects-speakers/5da6b019-6539-47ac-a871-7bcf3a564d85/scratchpad`

## Tools/scripts
- `python3 -I scripts/fetch_raw.py <url> <folder> <name> [--date YYYY-MM-DD] [--author A] [--title T]` → saves `raw/<folder>/<name>.md` with header (title, URL, author, publication date, fetch date) and lists image URLs at the bottom. For ASR it saves only the first post (the review). Exit code 2 = already exists (fine, reuse it). If the site blocks scripted fetches (403/JS), use WebFetch with a prompt asking for the full text verbatim-as-possible, then Write it to the raw path with the same header format plus a line `- Capture: WebFetch (model-extracted, not verbatim)`.
- `python3 -I scripts/fetch_asset.py <image-url> <name>` → saves into `raw/assets/`. Use for impedance and distortion/compression graphs (data-carrying), then **look at the image with the Read tool** to read values. Name assets `<source-slug>-impedance`, `<source-slug>-thd`, etc.
- WebSearch / WebFetch for finding pages.

## Per-packet procedure

### Step 1 — Scope gate (always first)
Verify from the **manufacturer's product/spec page** (save it: `fetch_raw.py <url> manufacturer mfr-<speaker-slug>`), plus one US retailer page if needed for status/price:
- passive? nominal impedance as rated by the manufacturer (spec page, manual or spec sheet). 6 or 8 Ω → in scope; 4 Ω (or "4–8 Ω") → out of scope. If the maker gives no nominal figure but says "8 Ω compatible" (e.g. Polk) and nowhere rates it 4 Ω → in scope with `nominal_impedance_ohm: 8` and a note "maker states 8 Ω compatible; no explicit nominal". If nothing is stated anywhere → in scope only if a Tier A/B review reports the maker's rating as 6/8 Ω; otherwise `out-of-scope`, reason "nominal impedance not stated".
- bookshelf/standmount, woofer ≤ 8", height ≤ ~18" (457 mm) cabinet (integrated stands/plinths: judge the cabinet; note it);
- **currently sold new in the US**: listed as current on the maker's US site, or in stock/orderable new at an authorized US retailer (Crutchfield, Audio Advice, World Wide Stereo, Best Buy, Amazon sold-by-brand, B&H, Upscale Audio, manufacturer-direct). If the maker lists it as discontinued/legacy, or a successor has replaced it and only clearance remnants exist → `discontinued`.
- US street price for a PAIR (double per-each prices; say which retailer).
Packet `unverified_hints` came from a quick, error-prone search pass — use them as leads only, never as evidence.

Verdicts: `in-scope` | `out-of-scope` (with reason) | `discontinued` (with successor if known) | `no-tier-ab` (lineup packets only: in scope but no Tier A/B measurement exists anywhere you can find).
If verdict ≠ in-scope: write the sidecar and stop for this packet (keep the manufacturer raw file if saved). Do not create source or speaker pages.

### Step 2 — Measurements (Tier A/B)
**Spinorama packets** include `measurements[]` (key, origin, tier, review URL, pref scores, and `computed` = metrics from `scripts/cta2034.py` run on the raw Klippel data already saved under `raw/spinorama/<spinorama_name>/<key>/`). `primary_measurement` is the one to use for frontmatter.
- For each Tier A/B measurement with a review URL: fetch the review to `raw/measurements/<origin>-<speaker-slug>.md` (origin slugs: `asr`, `eac`, `audioholics`, `princeton`, other misc-* → strip `misc-`). If two measurements share an origin (e.g. eac-v1 / eac-v2 or grille on/off), one raw file per distinct URL; suffix the name (`eac-<slug>-v2`).
- Read the review fully. Extract: stated sensitivity, impedance minimum (+ frequency), EPDR, phase remarks, THD at 86/96 dB, compression/max SPL results (EAC), port noise, crossover, reviewer conclusions. If impedance/distortion values are only in graphs, download those graphs with `fetch_asset.py` and read them visually. Mark such numbers **graph-read (approx.)** in the source page.
- THD convention for `thd_86db_pct` / `thd_96db_pct`: the **highest THD across 100 Hz–10 kHz** at that level (excluding single narrow spikes, which you mention separately). If the review only shows graphs in dB or by harmonic and you cannot read a defensible % → null.
- `max_spl_db`: only if the source states a max SPL / compression limit; write the method in the speaker page (e.g. "EAC: ≤3 dB compression at 102 dB @1 m above 80 Hz").
- **Lineup packets** have no spinorama data. Search for Tier A/B measurements: SoundStage!/NRC measurements pages ("<model> measurements soundstage"), Stereophile measurements sidebar, Audioholics measurements, Hi-Fi News lab report, ASR, Erin. `tier_a_hints` may contain leads. If none exist → verdict `no-tier-ab`, stop. If some exist, ingest them as above (values read from text/graphs; f3/LW deviation only if stated or clearly readable — never estimate from memory).
- Also, for spinorama packets with price ≥ $1,000/pair, do one search for a Stereophile or SoundStage/NRC measurement of the same model and ingest it if it exists (adds a second rig → conflicts check).

### Step 3 — Critic reviews (Tier D)
Find up to **3** professional reviews of this exact model (prefer: Stereophile, SoundStage!, Audioholics, What Hi-Fi?, Hi-Fi News, The Absolute Sound, Sound & Vision, Darko.Audio, Hi-Fi Choice, Audio Science-adjacent pro outlets; YouTube-only reviews are acceptable only with a text transcript/article). Save each to `raw/reviews-critic/<outlet-slug>-<speaker-slug>.md`. Extract attributed claims: tonal balance, bass, imaging, dynamics, verdict/rating. If ASR/Erin's subjective listening notes exist, they are also Tier D — attribute them as such (no separate raw file needed; cite the measurement source page).

### Step 4 — User reviews (Tier E)
Spend at most ~4 fetches. Sources: the ASR review thread (later replies — `fetch_raw.py <thread-url>page-2 ... --all-posts` saves all posts on that page), Reddit (r/BudgetAudiophile, r/audiophile; use `old.reddit.com` URLs or WebFetch), Crutchfield/Audio Advice/Best Buy/Amazon review summaries, AVS Forum / Audiokarma threads. Write ONE clip file `raw/reviews-user/users-<speaker-slug>-2026-10-11.md` (header: title, URLs list, author "various", publication date range, fetch date) containing short paraphrased notes per report (≤15-word quotes), each with its URL and an id. Count independent reports per theme. Patterns need ≥3 independent reports; <5 total reports = "anecdotal". Separately note QC/reliability reports (failures, sample variation, finish defects).

### Step 5 — Source pages: `wiki/sources/<source-slug>.md`
Source slug = raw file name without `.md` (e.g. `asr-revel-m16`, `eac-kef-q150`, `stereophile-kef-ls50-meta`, `whathifi-kef-q150`, `users-kef-q150`, `mfr-kef-q150`). Template:

```markdown
---
type: source
slug: asr-revel-m16
title: "Revel M16 Speaker Review"
url: https://...
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-03-05
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-revel-m16.md
raw_data: raw/spinorama/Revel M16/asr/     # only for spinorama-backed measurements
assets: [raw/assets/asr-revel-m16-impedance.png]
speakers: [revel-m16]
---
# ASR: Revel M16 review (2020-03-05)

## Summary
2–4 sentences.

## Extracted values
| Field | Value | Note |
|---|---|---|
| lw_deviation_db | ±1.4 dB | computed, scripts/cta2034.py v2 from raw Klippel export |
| min_impedance_ohm | 4.2 Ω @ 180 Hz | graph-read (approx.) |
...

## Method notes
Rig, grille, reference axis, gating/LF limits, sample provenance.

## Reliability notes
Single sample? Loaner? Conflicts of interest disclosed? Any doubt about values.

## Related
[[revel-m16]] · [[asr]] · [[revel]]
```
For critic sources, "Extracted values" becomes "Key claims" (attributed, paraphrased). For `users-*`, list themes with counts. For `mfr-*`, list specs (claimed sensitivity — and its 2.83 V conversion if stated per watt — claimed FR as text, crossover, drivers, dims, weight, nominal/min impedance, price/status evidence).

Reviewer wikilinks allowed: `[[asr]] [[erins-audio-corner]] [[audioholics]] [[soundstage-nrc]] [[stereophile]] [[princeton-3d3a]] [[spinorama-org]]`. For other outlets do not wikilink the outlet (plain text). Brand link: `[[<brand_slug>]]` (the coordinator creates brand pages).

### Step 6 — Speaker page: `wiki/speakers/<speaker-slug>.md`
Exact frontmatter keys from CLAUDE.md §4, in that order, then these extra keys: `claimed_fr` (text or null), `primary_measurement` (source slug used for spinorama-derived fields), `measurement_count` (number of Tier A/B source pages). Rules:
- `price_checked: 2026-10-11`, `last_updated: 2026-10-11`, `status: current`.
- Spinorama-derived fields (`sensitivity_db_2v83`, `f3_hz`, `f6_hz`, `lw_deviation_db`, `on_axis_deviation_db`, `hor_beamwidth_deg`, `ver_beamwidth_deg`, `di_smoothness`) come from the packet's `computed` block of the **primary** measurement. Exception: if computed sensitivity differs from the reviewer's stated sensitivity by > 2 dB, the export may be normalized — use the reviewer's value and explain in Conflicts.
- `pref_score` / `pref_score_sub`: from the primary measurement's packet values (spinorama.org computation). null if absent.
- `min_impedance_ohm`/`_hz`, `epdr_min_ohm`, THD, `max_spl_db`: best Tier A source (then B). Never from the manufacturer.
- `impedance_flag`: `effectively-4ohm` if min < 4.0; else `below-iec` if min < 0.8 × nominal; else null. (Use measured min only.)
- `sensitivity_claimed_db`: manufacturer figure normalized to 2.83 V (state conversion in the mfr source page).
- `crossover_hz`, `woofer_in`, `tweeter_type` (dome|ribbon|AMT|coaxial — use `coaxial` for Uni-Q/concentric), `port` (rear|front|sealed|passive-radiator — `rear` for down/bottom-firing too, note it), `dimensions_mm` as "HxWxD" string, `weight_kg` (each): manufacturer spec.
- `critic_consensus`, `user_consensus`: one line each, or null if no data.
- `sources`: list of all source slugs for this speaker (plus `spinorama-org` when spinorama data used).
- Use one decimal place for dB and Ω. Units per CLAUDE.md §8.

Body sections exactly as CLAUDE.md §4 (Summary, Measurements, Directivity, Output & distortion, Amplifier load, Critic reviews, User reviews, Conflicts, Related). Keep under ~800 words. Requirements:
- **Measurements** table: Metric | Value | Source | Tier | Note — every measured value, each linking its source page `[[asr-revel-m16]]`; computed values say "computed (scripts/cta2034.py v2)". Include values from every Tier A/B measurement (not just primary) when there are several; differences > (sensitivity 1 dB, f3 5 Hz, LW dev 0.5 dB, min impedance 0.5 Ω) go to Conflicts. Include pref scores. Apply CLAUDE.md §7 labels (e.g. "±1.4 dB — excellent").
- **Directivity**: use `hor/ver_beamwidth_deg`, `di_smoothness` (+`erdi_max_residual_db`), `er_dip_1_5khz_db` (flag if > 3 dB), `spdi_1k_db`→`spdi_10k_db`, and toe-in from `on_minus_lw_4_10k_db` (> +1 dB: on-axis brighter than window → less toe-in / axes crossing in front; < −1 dB: aim at listener; otherwise either). Mention `lw_dip_above_f3_*` if present (in Measurements or here). Link [[directivity-index]], [[early-reflections]].
- **Output & distortion**: THD, compression, max SPL; practical room-size/level implication per [[compression-and-max-spl]]. If no data, say so.
- **Amplifier load**: per [[impedance-and-epdr]] guidance.
- **Critic reviews**: "- [[whathifi-kef-q150]] (What Hi-Fi?, 5/5): described bass as …". Attributed, paraphrased.
- **User reviews**: patterns with counts per Step 4, QC separately. If none found: "No user reports ingested yet."
- **Conflicts**: disagreements (Tier A vs A, measurement vs manufacturer claim deltas e.g. claimed 88 dB vs measured 85.0 dB, sample differences). "None noted." if none.
- **Related**: `[[<brand_slug>]]`, sibling/competitor speaker slugs from the packet list you were given (only slugs in `ALL_SLUGS` file `<SCRATCH>/ingest/all_slugs.txt`), relevant concept pages.
- Quotes ≤15 words; otherwise paraphrase. Every number traceable to a source page. Never guess: null + say "not measured".

### Step 7 — Sidecar `<SCRATCH>/ingest/results/<speaker-slug>.json`
```json
{
 "slug": "revel-m16", "brand": "Revel", "model": "M16", "brand_slug": "revel",
 "verdict": "in-scope", "reason": null, "successor": null,
 "nominal_impedance_ohm": 6, "status": "current", "price_usd_pair": 900, "price_source": "https://...",
 "tier_ab_available": true,
 "pages_created": ["wiki/speakers/revel-m16.md", "wiki/sources/asr-revel-m16.md"],
 "raw_saved": ["raw/measurements/asr-revel-m16.md"],
 "index_line": "- [[revel-m16]] — 6 Ω, LW ±1.4 dB, f3 57 Hz, pref 5.1 (ASR)",
 "source_index_lines": ["- [[asr-revel-m16]] — ASR Klippel review, 2020-03-05 (Tier A)"],
 "brand_notes": "facts useful for the brand page: lineup position, QC reports, design traits, with source slugs",
 "takeaways": ["3–6 bullets of key findings"],
 "conflicts": ["..."],
 "log_bullets": ["Created speakers/revel-m16, sources/asr-revel-m16, ...", "Conflict: ..."]
}
```
For non-in-scope verdicts include slug, brand, model, verdict, reason, successor, nominal_impedance_ohm, status, price_usd_pair, price_source, tier_ab_available (true/false/null), raw_saved, and an `evidence` URL list.

## Quality bar
- Never fabricate a source, URL, quote, rating or number. If a fetch fails, say so in the sidecar and skip it.
- Prefer fewer, solid sources over many thin ones. Typical budget per in-scope speaker: ~12–25 tool calls.
- Finish every packet you were given. Your final reply: one line per packet: `slug — verdict — pages created count — notable issue`.

## Practical notes (from pilot)
- Always single-quote URLs in shell commands (ASR attachment URLs contain `?`; Dropbox URLs contain `%28`). `fetch_asset.py` works for ASR attachments and Erin's Dropbox images when quoted.
- Erin's pages show the date in the body ("Monday, Jun 19, 2023"); pass `--date` to fetch_raw.py.
- Crutchfield often blocks scripted fetches; try Audio Advice, World Wide Stereo, Best Buy, Amazon, B&H, or the maker's store instead.
- Audioholics/Sound & Vision measurement reviews go in `raw/measurements/` (not reviews-critic) when they contain measurements.
- If ASR's distortion plot does not state the SPL, leave thd_86/96 null but describe it in Output & distortion (as the pilot did).
