---
type: speaker
brand: Hsu Research
model: CCB-8
slug: hsu-research-ccb-8
status: current
price_usd_pair: 778
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.8
min_impedance_hz: 182
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 88.8
sensitivity_claimed_db: 88.0
f3_hz: 59
f6_hz: 54
lw_deviation_db: 5.2
on_axis_deviation_db: 6.0
hor_beamwidth_deg: 106
ver_beamwidth_deg: 112
di_smoothness: minor-discontinuity
crossover_hz: 1500
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 1.6
pref_score_sub: 4.0
woofer_in: 8
tweeter_type: coaxial
port: rear
dimensions_mm: 381x267x305
weight_kg: 10.0
critic_consensus: Audioholics and AV Nirvana praised detail, imaging and dynamics; ASR measured a messy on-axis response and rejected the constant-directivity claim.
user_consensus: null
sources: [mfr-hsu-research-ccb-8, asr-hsu-research-ccb-8, audioholics-hsu-research-ccb-8, avnirvana-hsu-research-ccb-8, users-hsu-research-ccb-8, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "50 Hz-20 kHz +/-2 dB at 15 degrees off axis"
primary_measurement: asr-hsu-research-ccb-8
measurement_count: 2
---

## Summary
The Hsu CCB-8 is an 8" ported coaxial horn speaker (aluminium dome tweeter behind the woofer cone) sold factory-direct at $389 each. It has very high efficiency for a bookshelf (88.8 dB at 2.83 V in ASR's Klippel data) but a rough anechoic response: listening-window deviation ±5.2 dB with a deep notch near 1.7 kHz, and directivity that is not constant. Bass reaches f3 59 Hz (good). Impedance dips to about 3.8 Ω, so it behaves as a 4 Ω speaker despite an "8 Ω" setting recommendation. Suits buyers who value efficiency, off-axis consistency in the bass/midrange and orientation flexibility, and who accept a coloured on-axis response; aiming 15-25° off axis, as the maker advises, helps.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 88.8 dB (high) | [[asr-hsu-research-ccb-8]] | A | computed (scripts/cta2034.py v2) |
| Sensitivity | 93.8 dB half-space (about 87.8 full-space) | [[audioholics-hsu-research-ccb-8]] | A | claimed 94 half-space per [[mfr-hsu-research-ccb-8]] = 88.0 full-space |
| Listening-window deviation | ±5.2 dB (coloured) | [[asr-hsu-research-ccb-8]] | A | computed, 300 Hz-10 kHz |
| On-axis deviation | ±6.0 dB | [[asr-hsu-research-ccb-8]] | A | computed |
| On-axis response | within about ±3 dB to 10 kHz | [[audioholics-hsu-research-ccb-8]] | A | gated 14 ms, 1 m, unsmoothed |
| f3 / f6 | 59 / 54 Hz (good) | [[asr-hsu-research-ccb-8]] | A | computed, both ports open |
| Min impedance | 3.8 Ω @ 182 Hz | [[asr-hsu-research-ccb-8]] | A | graph-read (approx.) |
| Min impedance | 5 Ω near 200 Hz | [[audioholics-hsu-research-ccb-8]] | A | stated in text |
| Preference score | 1.6 (no sub) / 4.0 (with sub) | [[asr-hsu-research-ccb-8]] via [[spinorama-org]] | A | not meaningful to <0.5 |
| Crossover | 1.5 kHz | [[audioholics-hsu-research-ccb-8]] | A | not stated by maker |

## Directivity
Horizontal -6 dB beamwidth about 106°, vertical about 112°. DI rises with frequency (SPDI 6.5 dB at 1 kHz to 10.8 dB at 10 kHz) with a minor discontinuity (ERDI residual 1.9 dB); ASR says it is "anything but constant". The early-reflection dip near 1.5 kHz is 4.8 dB, above the 3 dB flag, matching the 1.7 kHz cancellation. On-axis minus listening window above 4 kHz is +1.6 dB, so on-axis is brighter than the window: less toe-in by the data. Audioholics and the maker, though, recommend 15-25° off axis, where treble flattens; this is not a contradiction for a narrowing-treble horn, but the rig data argue for experimenting. Orientation (vertical/horizontal) barely changes response per Audioholics. See [[directivity-index]], [[early-reflections]].

## Output & distortion
ASR's 86 dB sweep is clean (THD traces roughly 40-47 dB SPL from 50 Hz upward, graph-read, in dB not %, so no % entered). At 96 dB distortion rises sharply, to about 70 dB SPL near 30-40 Hz and 60-65 dB around 130 Hz and 1.3 kHz, and ASR clearly heard distortion in a 101 dB sweep. No compression/max-SPL test exists. Efficiency means modest amplifiers reach loud levels, but expect limits in bass at high output; see [[compression-and-max-spl]].

## Amplifier load
Maker recommends an 8 Ω setting; ASR measured about 3.8 Ω minimum at 182 Hz (flag `effectively-4ohm`); Audioholics measured 5 Ω. Phase angle is moderate near the dip; two high-impedance peaks near 45 and 95 Hz. EPDR not computed. Any stable amp rated for 4 Ω is fine; high efficiency keeps power needs low. See [[impedance-and-epdr]].

## Critic reviews
- [[audioholics-hsu-research-ccb-8]] (Audioholics, 4.5/5 performance, 5/5 value): superb imaging, rich soundstage, hot direct-axis treble; sit 15-25° off axis.
- [[avnirvana-hsu-research-ccb-8]] (AV Nirvana): highly detailed full-range sound, good build quality.
- [[asr-hsu-research-ccb-8]] (ASR, Tier A measurement, no listening): "quite messy"; not recommended.

## User reviews
Five owner comments, all from the maker's own store and all positive, so anecdotal ([[users-hsu-research-ccb-8]]). Four ASR forum replies were critical of the measurements but none from owners. No QC problems reported.

## Conflicts
- Minimum impedance: 3.8 Ω (ASR, graph-read) vs 5 Ω (Audioholics); more than 0.5 Ω apart, different rigs and eras. Flag follows the ASR value.
- Nominal impedance: maker page says 8 Ω recommended setting; Audioholics reports Hsu quoting 6 Ω nominal / 4 Ω min; both are in scope.
- Response: Audioholics found ±3 dB to 10 kHz on axis (gated); ASR finds ±5.2 dB LW with a 1.7 kHz null. Different method (gated vs Klippel), sample years (2017 vs 2025) and smoothing.
- Maker claims "linear responses 15 degrees off axis" and constant directivity; neither source reproduces it.
- Sensitivity: 88.8 (ASR) vs 87.8 (Audioholics, half-space converted) vs 88.0 claimed; within 1 dB.

## Related
[[hsu-research]] · [[hsu-research-mfl-6]] · [[directivity-index]] · [[impedance-and-epdr]] · [[spinorama]] · [[preference-score]]
