---
type: speaker
brand: XSA Labs
model: Vanguard
slug: xsa-labs-vanguard
category: bookshelf
status: current
price_usd_pair: 995
price_checked: 2026-10-11
home_trial_days: 30
no_hassle_return: false
trial_seller: "XSA Labs"
trial_terms: "30 days, return shipping unclear, restocking fee: 20%"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 8.5
min_impedance_hz: 160
impedance_flag: null
epdr_min_ohm: null
sensitivity_db_2v83: 81.8
sensitivity_claimed_db: 83.0
f3_hz: 77
f6_hz: 59
lw_deviation_db: 4.2
on_axis_deviation_db: 4.8
hor_beamwidth_deg: 116
ver_beamwidth_deg: 117
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: 1.8
thd_96db_pct: 7.0
pref_score: 2.7
pref_score_sub: 5.5
woofer_in: 5.1
tweeter_type: dome
port: sealed
dimensions_mm: 305x191x203
weight_kg: 5.1
critic_consensus: Subjective reviewers (Stereo Times, TNT-Audio) praise integration, imaging and value; ASR's Klippel data shows a coloured midrange hill, weak bass and low sensitivity.
user_consensus: null
sources: [asr-xsa-labs-vanguard, mfr-xsa-labs-vanguard, stereotimes-xsa-labs-vanguard, tntaudio-xsa-labs-vanguard, users-xsa-labs-vanguard, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "82 Hz (-3 dB), 70 Hz (-6 dB) to 22 kHz (-3 dB), 4pi anechoic (maker, via review)"
primary_measurement: asr-xsa-labs-vanguard
measurement_count: 1
---

## Summary
The XSA Labs Vanguard is a sealed 2-way (130 mm paper woofer, 28 mm silk dome) sold direct at about $995 per pair, styled as an LS3/5a-inspired monitor. ASR's Klippel data shows a coloured response (listening window ±4.2 dB) with a broad hill from about 700 Hz to 3 kHz, low sensitivity (81.8 dB) and f3 near 77 Hz. Directivity is wide and fairly even, so EQ helps a lot. Non-measuring reviewers like its imaging and midrange; it suits near-field listeners who prefer that voicing and accept a sub or EQ. Status is current (maker says in stock) but the maker page could not be fetched directly.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 81.8 dB (low) | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | computed (scripts/cta2034.py v2); claimed 83 dB per [mfr-xsa-labs-vanguard](../sources/mfr-xsa-labs-vanguard.md) |
| Listening-window deviation | ±4.2 dB, 300 Hz-10 kHz (coloured) | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | computed |
| On-axis deviation | ±4.8 dB | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | computed |
| f3 / f6 | 77 / 59 Hz (needs a sub) | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | computed; maker claims 82 / 70 Hz |
| Min impedance | 8.5 Ω @ ~160 Hz; peak ~26 Ω @ ~75 Hz | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | graph-read (approx.) |
| THD 86 dB @1 m | ~1.8% (100-200 Hz) | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | graph-read (approx.), highest in 100 Hz-10 kHz |
| THD 96 dB @1 m | ~7% at ~100 Hz; ~2.8% near 2 kHz | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) | A | graph-read (approx.) |
| Preference score | 2.7 (no sub) / 5.5 (with sub) | [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid; ignores distortion/output |
| Crossover | not stated as a single frequency | [stereotimes-xsa-labs-vanguard](../sources/stereotimes-xsa-labs-vanguard.md) | D | designer: woofer runs to ~5.5 kHz, Harsch topology |

## Directivity
Horizontal -6 dB beamwidth ~116°, vertical ~117°: wide, helped by similar-size drivers. DI is minor-discontinuity (ERDI residual 1.3 dB); SPDI rises from 5.2 dB at 1 kHz to 8.8 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.5 dB (under the 3 dB flag). On-axis minus listening window above 4 kHz is +0.9 dB, so either aim works; ASR notes a 4-5 kHz notch and suggested toe-in toward the listener, while Stereo Times preferred no toe-in (Tier D). Vertically stay on tweeter axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No max-SPL or compression test. ASR's plots (graph-read) show about 1.8% THD at 86 dB in the upper bass, rising to about 7% near 100 Hz at 96 dB, with the 1-3 kHz region elevated because the woofer plays high; Amir heard ticking only when pushed hard and judged one speaker loud enough. Low sensitivity plus sealed bass means modest levels in small rooms. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Easy load: 8.5 Ω minimum near 160 Hz, ~26 Ω peak at the 75 Hz box resonance, gentle phase (ASR, graph-read). Above the IEC floor of 6.4 Ω; no flag. EPDR not computed. Low sensitivity means moderate power (35-150 W reported as usable, Tier D). See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-xsa-labs-vanguard](../sources/asr-xsa-labs-vanguard.md) (ASR, Tier D listening): sound inoffensive but bass-light; needed EQ; "cannot recommend".
- [stereotimes-xsa-labs-vanguard](../sources/stereotimes-xsa-labs-vanguard.md) (Stereo Times, Greg Voth): wide, deep imaging; surprising bass depth for size; wants to buy a pair.
- [tntaudio-xsa-labs-vanguard](../sources/tntaudio-xsa-labs-vanguard.md) (TNT-Audio, M.L. Gneier): integrated, smooth extended top end; strong on acoustic music; strained when very loud.

## User reviews
No owner reports found. Eleven ASR forum reactions, none confirmed owners (anecdotal): 7 of 11 criticise the crossover/tonal design ([users-xsa-labs-vanguard](../sources/users-xsa-labs-vanguard.md)). QC: one unverified second-hand claim of woofer unit-to-unit variation.

## Conflicts
- Tier A vs D: ASR measures a coloured, bass-light response and rejects it; two subjective reviewers praise tonal balance and bass depth. Not resolved; measurement governs ranking.
- Sensitivity: 81.8 dB computed vs 83 dB claimed (1.2 dB).
- f3: 77 Hz measured vs 82 Hz claimed (-3 dB); within 5 Hz.
- Maker's own foam-core prototype measurement (shown by ASR) differs from production measurement.
- Maker site not directly verified; price/status via reviews and a search summary.

## Related
[XSA Labs](../brands/xsa-labs.md) · [Ascend Acoustics Sierra-1 V2](ascend-acoustics-sierra-1-v2.md) · Ascend Acoustics Luna Mini-Monitor · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
