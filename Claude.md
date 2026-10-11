# CLAUDE.md — Bookshelf Speaker Research Wiki

This repo is an LLM-maintained research wiki (Karpathy "LLM Wiki" pattern) covering **passive, 6- or 8-ohm nominal bookshelf speakers currently sold new**, plus a separately ranked **on-wall** category (§2). Goal: rank and compare them on measured performance — frequency response, directivity/dispersion, maximum output, distortion, sensitivity, impedance — and on aggregated critic and user assessments of sound quality.

You (Claude) write and maintain everything under `wiki/` and `data/`. The human curates sources, directs analysis, and asks questions. `raw/` is read-only to you except when the human asks you to fetch a source into it.

The repo is published publicly at github.com/druce/bookshelf-speakers. Third-party source copies under `raw/` stay local (see §1, Publishing).

---

## 1. Architecture

```
raw/                      # IMMUTABLE source documents. Never edit after saving.
  measurements/           # ASR, Erin's Audio Corner, Audioholics, SoundStage/NRC, Stereophile, etc.
  spinorama/              # CTA-2034 data exports (CSV/txt), spinorama.org pages
  reviews-critic/         # Professional subjective reviews
  reviews-user/           # Forum threads, retailer reviews, Reddit — clipped as markdown
  manufacturer/           # Spec sheets, product pages, manuals
  assets/                 # Downloaded images/graphs referenced by raw docs
wiki/
  index.md                # Catalog of every wiki page, one line each, by category
  log.md                  # Append-only chronological record of operations
  overview.md             # Current state of the research: shortlist, open questions, thesis
  speakers/<brand>-<model>.md     # One page per speaker model (the core entity)
  brands/<brand>.md               # Manufacturer pages: lineup, QC reputation, design philosophy
  sources/<source-slug>.md        # One summary page per ingested raw document
  reviewers/<reviewer>.md         # Methodology, rig, known biases of each measurer/critic
  concepts/<concept>.md           # e.g. spinorama, directivity-index, preference-score, epdr
  comparisons/<slug>.md           # Filed-back query answers, head-to-heads, ranked tables
data/
  speakers.csv                    # Flat table generated from speaker-page frontmatter (see §6)
  cta2034-metrics.json            # Uniform CTA-2034 metrics computed from raw Klippel exports
  spinorama-passive-bookshelf.json# spinorama.org passive bookshelf list with evidence tiers
  candidate-universe.csv          # Discover output (all screened models + verdicts)
  ingest-packets-*.json           # Packets sent to ingest agents (slug, brand, model, measurements)
  ingest-results/<slug>.json      # Per-candidate scope verdict sidecars (authoritative for Discover)
  speaker-images.json             # Product photo URL per slug (hotlinked, not stored)
  wall-mount.json                 # Wall-mount provision per slug, with source
  seller-policies.json            # Verified return/trial policy per seller or maker
  speaker-sellers.json            # Authorized US sellers per speaker (availability snapshot)
scripts/
  INGEST-PLAYBOOK.md              # Instructions for (sub)agent ingest; ONWALL-ADDENDUM.md for on-walls
  fetch_raw.py / fetch_asset.py / fetch_spin_raw.py   # Save sources, graphs, Klippel exports into raw/
  cta2034.py / compute_all.py     # Compute spinorama metrics (method in wiki/concepts/spinorama.md)
  build_csv.py                    # data/speakers.csv
  rank.py                         # ranked-by-price-band, ranked-on-wall, impedance-honesty, sensitivity-claims-vs-measured
  size_table.py                   # size-and-weight comparison
  build_universe.py               # candidate-universe page + CSV
  add_trial.py                    # return/trial frontmatter + returns-and-trials page
  set_wall_mount.py               # wall_mount frontmatter from data/wall-mount.json
  add_photos.py                   # photo block + image_url from data/speaker-images.json
  build_index.py / build_raw_manifest.py
  wikilinks_to_md.py / check_links.py / fix_frontmatter.py   # link conversion and lint helpers
```

**Publishing.** `raw/measurements`, `reviews-critic`, `reviews-user`, `manufacturer`, `assets` and per-speaker `raw/spinorama/*/` folders are gitignored: they are copies of third-party content. Only `raw/MANIFEST.md` (title, URL and fetch date of every raw doc; regenerate with `scripts/build_raw_manifest.py` after each ingest) and the spinorama.org metadata export are committed. Never commit third-party page text, review text or graphs. Product photos are hotlinked with attribution, never downloaded into the repo. Wiki text and data are CC BY-NC-SA 4.0 (ASR data share-alike); scripts MIT.

**Standard rebuild before commit:** `fix_frontmatter.py` → `set_wall_mount.py` → `add_trial.py` → `add_photos.py` → `build_csv.py` → `rank.py` → `size_table.py` → `build_universe.py <scratch>` (if verdicts changed) → `build_raw_manifest.py` → `build_index.py` → `check_links.py` (must report 0 broken, 0 unconverted, 0 orphans, 0 frontmatter errors).

---

## 2. Scope rules

A speaker is **in scope** if all hold:
- **Passive** (requires external amplifier). Active/powered speakers are out of scope; note notable ones in `wiki/concepts/active-alternatives.md` only.
- **Nominal impedance 6 Ω or 8 Ω** per manufacturer (scope widened from 8 Ω only on 2026-10-11). 4 Ω-nominal models are out of scope. Record measured minimum impedance regardless.
- DIY designs and kits are listed in Discover but excluded from rankings unless the human asks; finished commercial products only.
- **Bookshelf/standmount form factor**: designed for shelf or stand placement, woofer ≤ 8", height ≤ ~18". Desktop monitors count if passive.
- **Currently sold new** (in production or stocked by authorized retailers as of the ingest date). Discontinued models get `status: discontinued` and are retained for reference but excluded from rankings.

**On-wall category (added 2026-10-11).** A second, separately ranked category: passive speakers designed and marketed by the maker for on-wall mounting as main L/R (or LCR) speakers. They are slim cabinets with a dedicated bracket or keyhole, made to hang flat on a wall. The same impedance (6/8 Ω), woofer (≤ 8") and currently-sold rules apply. There is no height limit. Excluded: in-wall/in-ceiling, dipole/bipole surround-only, Atmos modules, soundbars, active, and ordinary bookshelf speakers that merely have a keyhole (those stay `bookshelf`). Every speaker page has `category: bookshelf | on-wall`. On-wall pages add `wall_voiced` (true only if the maker states boundary compensation). Ingest rules: `scripts/ONWALL-ADDENDUM.md`. Interpretation: [[on-wall-speakers]].

**Impedance honesty check.** IEC 60268-5 allows minimum impedance down to 80% of nominal (6.4 Ω for an 8 Ω rating, 4.8 Ω for a 6 Ω rating). Flag any speaker measuring below 80% of its rated nominal as `impedance_flag: below-iec`, and any measuring below 4.0 Ω minimum as `impedance_flag: effectively-4ohm`. Do not drop them from scope; the human decides.

---

## 3. Evidence hierarchy

Weight evidence in this order. Always state which tier a claim comes from.

| Tier | Source type | Use for |
|---|---|---|
| A | Anechoic or Klippel NFS measurements with full CTA-2034 spinorama (ASR, Erin's Audio Corner, Audioholics, NRC via SoundStage) | Frequency response, directivity, sensitivity, bass extension, distortion |
| B | Quasi-anechoic / gated measurements (Stereophile, Hi-Fi News, independent hobbyist with stated method) | Same, with lower confidence below ~300 Hz |
| C | Manufacturer measurements and specs | Only when A/B absent; mark `source_tier: C` |
| D | Professional subjective reviews | Tonal character, imaging, perceived quality |
| E | Aggregated user reviews and forum reports | Reliability, QC, sample variation, long-term satisfaction, placement experience |

Rules:
- **Never let a manufacturer spec override a measurement.** Record both; note the delta.
- **Frequency response claims without tolerance (e.g. "45 Hz–25 kHz") are not data.** Record as `claimed_fr` text only.
- Sensitivity must be normalized to **dB SPL @ 2.83 V / 1 m**. If a source states dB/1 W, convert using measured nominal impedance and note it.
- When two Tier-A sources disagree (different samples, different rigs), record both values, link both source pages, and add the disagreement to the speaker page's `## Conflicts` section. Do not average silently.
- Subjective claims (D/E) are recorded as attributed claims ("Reviewer X described the treble as forward"), never as facts.
- Preference scores (Olive model, as computed by ASR/spinorama.org) are recorded with and without subwoofer, and treated as a coarse ranking aid: they ignore distortion and max output.

---

## 4. Speaker page format

Every `wiki/speakers/*.md` has this frontmatter. Use `null` for unknown; never guess.

```yaml
---
type: speaker
brand: KEF
model: Q150
slug: kef-q150
category: bookshelf        # bookshelf | on-wall
wall_voiced: null          # on-wall only: true | false | null
status: current            # current | discontinued
price_usd_pair: 499        # street price at last check
price_checked: 2026-10-11
image_url: null            # hotlinked product photo (scripts/add_photos.py)
home_trial_days: null      # best return window among authorized US sellers (days)
no_hassle_return: null     # true if >=30 days, opened speakers accepted, restocking fee on a normal return none or low (<=10%, or a flat fee <=$50 or <=~5% of pair price); buyer-paid return shipping allowed
trial_seller: null         # seller offering that best policy
trial_terms: null          # e.g. "60 days, buyer pays return shipping, no restocking fee"
trial_checked: null        # date policies/availability were verified
nominal_impedance_ohm: 8
min_impedance_ohm: null    # measured
min_impedance_hz: null
impedance_flag: null       # null | below-iec | effectively-4ohm
epdr_min_ohm: null         # equivalent peak dissipation resistance, if measured
sensitivity_db_2v83: null  # measured
sensitivity_claimed_db: null
f3_hz: null                # measured -3 dB anechoic
f6_hz: null
lw_deviation_db: null      # listening-window deviation ±dB, 300 Hz–10 kHz
on_axis_deviation_db: null
hor_beamwidth_deg: null    # -6 dB horizontal beamwidth, typical across 1–10 kHz
ver_beamwidth_deg: null
di_smoothness: null        # qualitative: smooth | minor-discontinuity | major-discontinuity
crossover_hz: null
max_spl_db: null           # max SPL @1 m before ≥3 dB compression or audible distortion; state method
thd_86db_pct: null         # THD at 86 dB SPL @1 m, 100 Hz–10 kHz, if available
thd_96db_pct: null
pref_score: null           # Olive preference score, no sub
pref_score_sub: null       # with ideal sub
woofer_in: null
tweeter_type: null         # dome | ribbon | AMT | coaxial
port: null                 # rear | front | sealed | passive-radiator
wall_mount: null           # none | keyhole | threaded-insert | bracket-included | on-wall-design (maker spec, Tier C; or ≥2 owner reports, Tier E)
dimensions_mm: null        # HxWxD
weight_kg: null
critic_consensus: null     # one line
user_consensus: null       # one line
sources: []                # list of wiki/sources slugs
last_updated: 2026-10-11
claimed_fr: null           # maker's FR claim as text (not data)
primary_measurement: null  # source slug whose data fills the spinorama-derived fields
measurement_count: null    # number of Tier A/B source pages
---
```

Field notes:
- **Returns** (`home_trial_days` … `trial_checked`): set only by `scripts/add_trial.py`. The rule: best policy among authorized US sellers currently selling the model new. The fee counted is for a normal return of opened, complete, undamaged speakers in original packaging; fees triggered only by missing packaging or damage don't count. Never hand-edit; update `data/seller-policies.json` (verified from the seller's own policy page, raw copy saved as `raw/manufacturer/policy-<seller>.md`) or `data/speaker-sellers.json`, then re-run. All comparison output goes to [[returns-and-trials]].
- **wall_mount**: from the maker's spec page or manual, a major retailer's spec table (secondary; source `retailer-<name>`, or `retailer-<name>-snippet` when only a search-result snippet could be read — re-verify those first), or ≥2 independent owner reports. Absence of a mention is not `none`; mounting inserts meant only for the maker's floor stand don't count. Record the source in `data/wall-mount.json` and re-run `scripts/set_wall_mount.py`. `null` means not determined (unchecked, or sources silent or conflicting; notes in the JSON), not "no". Rear-ported speakers on a wall gain boundary bass ([[bass-extension-vs-room-gain]]).
- **image_url**: manufacturer product image preferred, then a major retailer. Check visually that it shows the right product, and reject logos, lifestyle shots where the speaker is tiny, or wrong models.

Body sections, in order:
1. `## Summary` — 3–5 sentences: what it is, how it measures, who it suits.
2. `## Measurements` — table of every measured value with source link and tier. Note the measurement method where it changes interpretation (anechoic vs in-room, gated low-frequency cutoff).
3. `## Directivity` — beamwidth, DI behaviour, crossover-region issues, toe-in recommendation from data.
4. `## Output & distortion` — compression and distortion results; practical implication for room size and listening level.
5. `## Amplifier load` — impedance curve notes, phase, EPDR, amplifier guidance.
6. `## Critic reviews` — attributed one-line takeaways, linked.
7. `## User reviews` — patterns only (≥3 independent reports), with counts: "7 of 9 forum reports mention…". Note QC/reliability issues separately.
8. `## Conflicts` — disagreements between sources, unresolved.
9. `## Related` — links to brand, siblings, competitors, comparisons.

Keep pages under ~800 words (~1,000 when owner-review tallies are present). Link generously.

**Photo block.** Directly after the frontmatter, `scripts/add_photos.py` inserts a 360 px `<img>` plus an attribution line between `<!-- photo -->` and `<!-- /photo -->` markers. Don't edit inside the markers; edit `data/speaker-images.json` and re-run.

**Link format.** Committed pages use relative markdown links so they render on GitHub, e.g. `[Polk Audio T15](../speakers/polk-audio-t15.md)` or `[asr-polk-audio-t15](../sources/asr-polk-audio-t15.md)`. While drafting you may write `[[slug]]` or `[[slug|text]]`; `scripts/wikilinks_to_md.py` converts them, labelling speakers "Brand Model" and brands by name, and runs automatically at the end of `build_index.py`, `rank.py` and `build_universe.py`. Run it before every commit. Links to screened models without a page become plain text. `scripts/check_links.py` reports broken links and any leftover `[[...]]`.

---

## 5. Operations

### Discover (build the candidate universe)
Run when the human asks to expand coverage.
1. Search spinorama.org and ASR's speaker review index for passive bookshelf models; search manufacturer lineups for 8 Ω standmounts.
2. Write `wiki/comparisons/candidate-universe.md`: every in-scope model found, with columns: brand, model, price, Tier-A data available (y/n), source URLs.
3. Do not create speaker pages yet. Report count found, count with Tier-A data, and suggested ingest order (Tier-A available first, then by price band).
4. At scale, Discover and Ingest run as batched subagents following `scripts/INGEST-PLAYBOOK.md`: each candidate gets a scope gate (manufacturer spec page plus US availability), then ingest if in scope with Tier A/B data. Each writes a sidecar JSON verdict (`in-scope | out-of-scope | discontinued | no-tier-ab`) that `build_universe.py` uses. Lineup sweeps by brand catch models missing from spinorama.org.

### Ingest (one source at a time by default)
1. If the human gives a URL, fetch it and save to the correct `raw/` subfolder as markdown with a header: title, URL, author, publication date, fetch date. Save graphs to `raw/assets/` when they carry data.
2. Read the source fully. Extract every quantitative value relevant to §4 frontmatter.
3. Briefly report key takeaways to the human (3–6 bullets) before writing, unless the human said to batch.
4. Create `wiki/sources/<slug>.md`: summary, extracted values table, method notes, reliability notes.
5. Create or update each affected `wiki/speakers/*.md`, `wiki/brands/*.md`, `wiki/reviewers/*.md`. Update frontmatter only where the new source is equal or higher tier, or fills a null. Record conflicts.
6. Update `wiki/index.md` and append to `wiki/log.md`.
7. Regenerate `data/speakers.csv` (run the standard rebuild in §1), regenerate `raw/MANIFEST.md`, commit and push.

### Owner reviews (Tier E)
- Retailer reviews are read in full via the logged-in Chrome session (Crutchfield works; Reddit is blocked by the extension; AVS Forum search is mostly classifieds). An in-page digest flags themes, then counts are hand-coded from the full text of every negative or flagged review.
- Save a paraphrased clip (≤15-word quotes, per-review ids, theme tallies, QC section) to `raw/reviews-user/<retailer>-<slug>-<date>.md`, a `wiki/sources/<retailer>-<slug>.md` page, and update the speaker's User reviews section and `user_consensus`.
- Report driver or electrical failures as "k of N". Add Conflicts bullets where owner patterns contradict measurements (e.g. "bass good for size" vs measured f3).

### Returns refresh
Re-verify seller policies and availability at least every 90 days, or when a price/status changes: update `data/seller-policies.json` and `data/speaker-sellers.json`, run `scripts/add_trial.py`, and log it.

A single source commonly touches 5–15 pages. That is expected.

### Query
1. Read `wiki/index.md` first, then the relevant pages. Use `data/speakers.csv` for filtering and ranking questions; compute with a script, never by eye.
2. Answer with citations to wiki pages (and through them to raw sources). State evidence tier for each key number.
3. If the answer is a comparison, ranking, or shortlist worth keeping, file it to `wiki/comparisons/<slug>.md`, add it to the index, and log it.
4. If data gaps limit the answer, say which speakers lack which measurements.

### Lint (run on request, or every ~10 ingests)
Check and report:
- Contradictions between pages, or frontmatter that disagrees with its own body.
- Speakers with no Tier-A/B data; speakers whose price, status or `trial_checked` is >90 days stale.
- Missing `image_url` or `wall_mount` on shortlisted speakers; on-wall pages without `wall_voiced`.
- Unconverted sensitivity figures; impedance flags not set where data supports them.
- Orphan pages (no inbound links), broken links or unconverted `[[...]]`, concepts mentioned ≥3 times without a page.
- Sources ingested but not reflected in speaker pages.
- Suggest next sources to fetch and questions worth investigating.
Append a lint entry to the log with counts of issues found and fixed.

---

## 6. index.md, log.md, speakers.csv

**index.md** — sections: Overview, Speakers (bookshelf, grouped by price band; on-wall listed separately: <$300, $300–600, $600–1,200, $1,200–2,500, >$2,500 per pair), Brands, Comparisons, Concepts, Reviewers, Sources. Each line: `- [Name](path) — one-line summary (key metric or two)`.

**log.md** — append-only. Every entry starts with a parseable header:
```
## [2026-10-11] ingest | ASR review: KEF Q150
## [2026-10-11] query | Best under $600 for 4m listening distance
## [2026-10-12] lint | 4 issues found, 3 fixed
```
Followed by 1–5 bullets: pages created/updated, conflicts noted.

**data/speakers.csv** — generated by `scripts/build_csv.py` from speaker-page frontmatter. One row per speaker, columns match frontmatter keys. Never hand-edit; regenerate after every ingest.

**Generated comparison pages** (regenerate, don't hand-edit outside their `## Notes` section, which is preserved): `ranked-by-price-band` (bookshelf; Group A = within 0.5 pref-with-sub of band leader, Group B = within 1.0), `ranked-on-wall`, `impedance-honesty`, `sensitivity-claims-vs-measured`, `size-and-weight`, `returns-and-trials`, `candidate-universe`. The current shortlist (Group A per band) lives in the Notes of `ranked-by-price-band` and in `overview.md`.

---

## 7. Interpretation standards

Use these when summarizing or ranking. State them when they drive a conclusion.
- **Listening-window flatness**: ±1.5 dB (300 Hz–10 kHz) excellent; ±2.5 dB good; >±3.5 dB coloured.
- **Bass extension (f3, anechoic)**: <45 Hz excellent for bookshelf; 45–60 Hz good; 60–75 Hz modest; >75 Hz needs a sub. Room gain near walls typically adds several dB below ~100 Hz; do not credit it to the speaker.
- **Directivity**: prefer smoothly narrowing DI with no step or dip at the crossover; flag a >3 dB early-reflection dip near crossover.
- **Sensitivity (2.83 V/1 m)**: <84 dB low; 84–87 average; 88–90 high; >90 very high.
- **Distortion**: THD <1% above 100 Hz at 86 dB is clean; note where it rises above 3% at 96 dB.
- **Preference score**: differences <0.5 are not meaningful; never rank on score alone.
- **On-wall speakers**: free-field (anechoic/Klippel) bass figures of wall-voiced designs understate in-use bass. Do not apply the f3 labels above to them, and rank on-walls only against each other.
- Small-sample user reviews (<5) are anecdote; say so. Retailer reviews skew positive and self-selected; weight QC/failure counts more than praise.
- **Max SPL** values are not comparable across reviewers (EAC's 102 dB test ceiling vs ASR draft compression charts). Never rank on `max_spl_db`.
- **No-hassle return** is a buying convenience, not a quality signal; never let it change a ranking.

---

## 8. Conventions

- Slugs: lowercase, hyphenated, `<brand>-<model>` (e.g. `elac-debut-b6-2`). Model generations are separate pages.
- Units: Hz, dB SPL, Ω, mm, kg, USD. One decimal place for dB and Ω.
- Dates ISO 8601.
- Quote sources sparingly (<15 words); paraphrase otherwise. Every number links to its source page.
- Prefer editing an existing page over creating a near-duplicate. Check the index before creating.
- When uncertain whether a value is measured or claimed, mark it claimed.
- Commit to git after each ingest or lint pass with message matching the log header.

---

## 9. Starting state

Initial build order:
1. Create the directory tree, empty `index.md`, `log.md`, `overview.md`, and concept pages for: spinorama, listening-window, early-reflections, sound-power, directivity-index, preference-score, sensitivity-normalization, impedance-and-epdr, compression-and-max-spl, bass-extension-vs-room-gain.
2. Create reviewer pages for ASR, Erin's Audio Corner, Audioholics, SoundStage/NRC, Stereophile, documenting each rig and method.
3. Run **Discover**.
4. Ingest Tier-A sources for the candidate universe, highest data availability first.
