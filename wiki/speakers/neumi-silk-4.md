---
type: speaker
brand: Neumi
model: Silk 4
slug: neumi-silk-4
category: bookshelf
status: current
price_usd_pair: 190
price_checked: 2026-10-11
home_trial_days: 30
no_hassle_return: null
trial_seller: "Amazon"
trial_terms: "30 days, free return shipping, restocking fee unclear"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 5.7
min_impedance_hz: 270
impedance_flag: below-iec
epdr_min_ohm: 2.9
sensitivity_db_2v83: 82.2
sensitivity_claimed_db: 85.0
f3_hz: 73
f6_hz: 61
lw_deviation_db: 2.4
on_axis_deviation_db: 2.3
hor_beamwidth_deg: 132
ver_beamwidth_deg: 89
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: 1.5
thd_96db_pct: 3.7
pref_score: 4.4
pref_score_sub: 7.1
woofer_in: 4
tweeter_type: dome
port: rear
wall_mount: null
dimensions_mm: 226x140x208
weight_kg: 2.8
critic_consensus: Seen as a smooth, slightly warm and clean small speaker for desks and small rooms; port resonances and limited bass are the caveats.
user_consensus: Amazon summary (only 23 ratings, anecdotal) is positive on sound and value, with bass limited at 4 inches.
sources: [eac-neumi-silk-4, mfr-neumi-silk-4, hifireport-neumi-silk-4, users-neumi-silk-4, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "65 Hz-20 kHz (typical in-room), no tolerance"
primary_measurement: eac-neumi-silk-4
measurement_count: 1
image_url: "https://www.neumitech.com/wp-content/uploads/2024/04/neumi-silk4-main-neumitech.jpg"
---
<!-- photo -->
<img src="https://www.neumitech.com/wp-content/uploads/2024/04/neumi-silk4-main-neumitech.jpg" alt="Neumi Silk 4" width="360">

*Photo: [neumitech.com](https://www.neumitech.com/neumi-silk-4-bookshelf-speakers/) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Neumi Silk 4 is an 8 Ω-rated, rear-ported 4" two-way with a 1" silk dome and waveguide, priced around $190-200 per pair. On Erin's Klippel it has a good listening window (±2.4 dB), minor directivity irregularity, f3 73 Hz and low sensitivity (82.2 dB). Its real impedance sits near 6 Ω, with a low 2.9 Ω EPDR, so it is not truly 8 Ω. Suits desks and small rooms, ideally with a subwoofer or EQ.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 82.2 dB (low) | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | computed (scripts/cta2034.py v2); claimed 85 dB per [mfr-neumi-silk-4](../sources/mfr-neumi-silk-4.md) |
| Listening-window deviation | ±2.4 dB, 300 Hz-10 kHz (good) | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | computed |
| On-axis deviation | ±2.3 dB (good) | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | computed |
| f3 / f6 | 73 / 61 Hz (modest) | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | computed; Erin's text: F3 83 Hz, F10 55 Hz |
| Min impedance | 5.7 Ω above 80 Hz | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | stated on plot; about 270 Hz graph-read |
| Min EPDR | 2.9 Ω above 80 Hz | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | stated on plot |
| THD 86 dB @ 1 m | about 1.5% peak near 110 Hz | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | graph-read (approx.); about 0.5% above 300 Hz |
| THD 96 dB @ 1 m | about 3.7% peak near 115-120 Hz | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) | A | graph-read (approx.) |
| Preference score | 4.4 (no sub) / 7.1 (with sub) | [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) via [spinorama-org](../sources/spinorama-org.md) | A | not meaningful to <0.5 |

## Directivity
Horizontal -6 dB beamwidth about 132°, vertical about 89°. DI shows a minor discontinuity (ERDI residual 1.3 dB); SPDI rises from 4.4 dB at 1 kHz to 8.3 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 1.1 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.9 dB, so either aim works; Erin found treble laid back up close and better balanced when sitting a few feet away. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin calls output surprisingly good for the size. Graph-read THD peaks at about 1.5% (86 dB) and 3.7% (96 dB) near 115 Hz and is lower above 300 Hz; Erin's text says THD stays under 3% at 96 dB until about 60 Hz, which does not match my graph reading (see Conflicts). Compression at 96 dB is under 0.4 dB above 100 Hz; at 102 dB about 1.1 dB near 200 Hz and 2.1 dB near 70 Hz. No max-SPL figure given. Suited to desk or small rooms; Erin advises an 80 Hz crossover to a sub for bass. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 8 Ω but measured 5.7 Ω minimum (floor 6.4 Ω), so `below-iec`; impedance peaks near 48 Hz and 115 Hz (about 27-32 Ω) and EPDR dips to 2.9 Ω near 180 Hz, which is demanding for its size at high levels. Phase stays within about ±55°. Low sensitivity means it needs reasonable power; Neumi suggests 15-80 W. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [eac-neumi-silk-4](../sources/eac-neumi-silk-4.md) (Erin, Tier D notes): positive overall for $150; resonances near 600 Hz and 1 kHz, laid-back treble nearfield, decent bass for size; better with EQ.
- [hifireport-neumi-silk-4](../sources/hifireport-neumi-silk-4.md) (HiFiReport): smooth, slightly warm, clean bass without bloat, good vocals and soundstage; limited dynamics at volume.

## User reviews
Anecdotal ([users-neumi-silk-4](../sources/users-neumi-silk-4.md), 23 Amazon ratings, 4.5/5): 12 of 16 sound-quality mentions positive, 9 of 9 value mentions positive, 2 excerpts say a subwoofer is needed. No QC problems reported.

## Conflicts
- f3: 73 Hz (computed) vs 83 Hz (Erin's text); 10 Hz apart, likely different reference level. Frontmatter uses the computed value.
- Impedance: rated 8 Ω vs measured 5.7 Ω minimum and 2.9 Ω EPDR; flagged `below-iec`.
- Sensitivity: claimed 85.0 dB vs measured 82.2 dB (-2.8 dB).
- THD at 96 dB: graph-read about 3.7% near 115 Hz vs Erin's text "below 3% until about 60 Hz"; graph value used and marked approximate.
- Price: Neumi page $189.99 (assumed per pair), Amazon pair $199.99, Erin about $150 in 2023.

## Related
[Neumi](../brands/neumi.md) · [Neumi BS5](neumi-bs5.md) · Micca RB42 · Dayton Audio B652-AIR · [Elac Debut 2.0 B5.2](elac-debut-2-0-b5-2.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
