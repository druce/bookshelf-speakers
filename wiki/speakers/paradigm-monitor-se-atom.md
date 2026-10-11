---
type: speaker
brand: Paradigm
model: Monitor SE Atom
slug: paradigm-monitor-se-atom
category: bookshelf
status: current
price_usd_pair: 399.98
price_checked: 2026-10-11
home_trial_days: 60
no_hassle_return: true
trial_seller: "Crutchfield"
trial_terms: "60 days, buyer pays return shipping, no restocking fee"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 4.5
min_impedance_hz: 200
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 84.6
sensitivity_claimed_db: 86.0
f3_hz: 57
f6_hz: 52
lw_deviation_db: 2.1
on_axis_deviation_db: 3.1
hor_beamwidth_deg: 128
ver_beamwidth_deg: 85
di_smoothness: minor-discontinuity
crossover_hz: 2300
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: 3.9
pref_score: 4.1
pref_score_sub: 6.5
woofer_in: 5.5
tweeter_type: dome
port: rear
dimensions_mm: 324x181x279
weight_kg: 5.4
critic_consensus: Praised by SoundStage! and TONEAudio for balance, wide dispersion and value; ASR measures an uneven, bright on-axis response that needs EQ, and bass is limited.
user_consensus: Six Audio Advice buyers all rate it 5/5 (anecdotal); some ASR commenters expect brightness.
sources: [mfr-paradigm-monitor-se-atom, asr-paradigm-monitor-se-atom, soundstage-paradigm-monitor-se-atom, tonepub-paradigm-monitor-se-atom, audioadvice-paradigm-monitor-se-atom, users-paradigm-monitor-se-atom, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "±3 dB 61 Hz-21 kHz on-axis; 45 Hz (DIN)"
primary_measurement: asr-paradigm-monitor-se-atom
measurement_count: 1
image_url: "https://www.paradigm.com/2518-large_default/monitor-se-atom.jpg"
---
<!-- photo -->
<img src="https://www.paradigm.com/2518-large_default/monitor-se-atom.jpg" alt="Paradigm Monitor SE Atom" width="360">

*Photo: [paradigm.com](https://www.paradigm.com/en/passive/monitor-se-atom) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Paradigm Monitor SE Atom is a small 2-way ported standmount (5.5" woofer, 1" dome) that Paradigm lists at $399.98 per pair, rated "compatible with 8 ohms" ([mfr-paradigm-monitor-se-atom](../sources/mfr-paradigm-monitor-se-atom.md)). On ASR's Klippel it shows good, parallel directivity but an uneven on-axis response with a 2-4 kHz dip, a rising treble and a ~15 kHz resonance, giving a listening-window deviation of ±2.1 dB (good) and a preference score of 4.1. Bass is modest (f3 57 Hz). It suits small rooms and budget systems if you accept a bright top end or use EQ; it is not a high-output speaker.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 84.6 dB (average) | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | computed (scripts/cta2034.py v2); claimed 86 dB anechoic ([mfr-paradigm-monitor-se-atom](../sources/mfr-paradigm-monitor-se-atom.md)) |
| Listening-window deviation | ±2.1 dB, 300 Hz-10 kHz (good) | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | computed (scripts/cta2034.py v2) |
| On-axis deviation | ±3.1 dB | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | computed; between good and coloured |
| f3 / f6 | 57 / 52 Hz (modest) | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | computed |
| Min impedance | 4.5 Ω, ~130-250 Hz | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | graph-read (approx.); ASR annotation |
| Preference score | 4.1 (no sub) / 6.5 (with sub) | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) via [spinorama-org](../sources/spinorama-org.md) | A | not meaningful to <0.5; ignores distortion and output |
| THD at 96 dB | ~3.9 % near 100 Hz | [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) | A | graph-read (approx.) |
| Crossover | 2.3 kHz | [mfr-paradigm-monitor-se-atom](../sources/mfr-paradigm-monitor-se-atom.md) | C | 2nd-order |

## Directivity
Horizontal -6 dB beamwidth about 128°, vertical about 85°. DI is smooth apart from a minor discontinuity (ERDI residual 1.3 dB); SPDI rises from 5.3 dB at 1 kHz to 8.3 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.5 dB, under the 3 dB flag. On-axis is 1.4 dB brighter than the listening window above 4 kHz, so less toe-in or axes crossing in front of the listener tames the treble; ASR advises staying at or just above tweeter height because the vertical response dips near 3-4 kHz below the axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No compression or max-SPL test. ASR's 96 dB distortion plot shows THD rising to roughly 4 % around 100 Hz (graph-read), about 1 % by 1 kHz, and low above 2 kHz; no 86 dB plot was captured. Amir noted clean sound at elevated levels only because the speaker lacks deep bass and the woofer does not bottom out. Suited to small-to-medium rooms at moderate levels; use a sub and high-pass for loud listening. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Maker says "compatible with 8 ohms"; no explicit nominal. ASR's impedance plot shows a 4.5 Ω minimum (4.3 Ω at the lowest frequencies) and peaks near 100 Hz and 2 kHz (~18-22 Ω), so it is below the IEC 80 % floor (6.4 Ω) and flagged `below-iec`, though above 4 Ω. Phase is moderate. EPDR not computed. Any competent amplifier rated for 4-8 Ω handles it; Paradigm suggests 15-100 W. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [soundstage-paradigm-monitor-se-atom](../sources/soundstage-paradigm-monitor-se-atom.md) (SoundStage! Access, Reviewers' Choice): balanced, natural, surprising bass for price; slightly shouty at extreme volume.
- [tonepub-paradigm-monitor-se-atom](../sources/tonepub-paradigm-monitor-se-atom.md) (TONEAudio): wide imaging, easy placement, great value; no deep bass.
- [audioadvice-paradigm-monitor-se-atom](../sources/audioadvice-paradigm-monitor-se-atom.md) (retailer): placement and break-in advice only.
- [asr-paradigm-monitor-se-atom](../sources/asr-paradigm-monitor-se-atom.md) (ASR, Tier D listening notes): detailed at first, then bright and fatiguing; not recommended without EQ, usable with EQ; needs a sub.

## User reviews
About 6 buyer reviews, so anecdotal ([users-paradigm-monitor-se-atom](../sources/users-paradigm-monitor-se-atom.md)): 5 of 5 with text positive on sound; 3 ASR commenters expect or report brightness (mostly older Atom generations or reacting to measurements). No QC or reliability reports.

## Conflicts
- Treble: SoundStage! and TONEAudio describe a natural balance, while ASR measures a rising top end (on-axis +1.4 dB over the listening window above 4 kHz) and found it bright; different listening conditions and no measurements in the critic reviews.
- Sensitivity: claimed 86 dB anechoic (unit not stated) vs 84.6 dB computed, a 1.4 dB shortfall.
- Preference score: 4.13 (spinorama.org) vs 3.68 computed by an ASR member in the thread; the spinorama.org value is used.
- Price: $399.98 per pair at Paradigm and Audio Advice (gloss white shown Unavailable there), versus the $239-298 prices quoted in 2018-2020 reviews.

## Related
[Paradigm](../brands/paradigm.md) · [Paradigm Founder 40B](paradigm-founder-40b.md) · JBL Stage A130 · KEF Q150 · [Elac Debut 2.0 B5.2](elac-debut-2-0-b5-2.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
