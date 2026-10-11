---
type: speaker
brand: Vandersteen
model: VLR
slug: vandersteen-vlr
category: bookshelf
status: current
price_usd_pair: 2060
price_checked: 2026-10-11
home_trial_days: null
no_hassle_return: null
trial_seller: null
trial_terms: "no verified authorized US seller policy"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 2.3
min_impedance_hz: 4000
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 81.3
sensitivity_claimed_db: 86.0
f3_hz: 111
f6_hz: 70
lw_deviation_db: 3.4
on_axis_deviation_db: 4.8
hor_beamwidth_deg: 112
ver_beamwidth_deg: 91
di_smoothness: major-discontinuity
crossover_hz: 3500
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 2.6
pref_score_sub: 5.7
woofer_in: 6.5
tweeter_type: coaxial
port: sealed
dimensions_mm: 305x203x292
weight_kg: 10.0
critic_consensus: Tone Audio (2015) praised coherence, imaging and ease of drive; ASR's Klippel review found it badly flawed and unrecommended.
user_consensus: null
sources: [asr-vandersteen-vlr, toneaudio-vandersteen-vlr, users-vandersteen-vlr, mfr-vandersteen-vlr, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "64 Hz - 21 kHz +/-3 dB"
primary_measurement: asr-vandersteen-vlr
measurement_count: 1
---

## Summary
The Vandersteen VLR (sold as VLR Wood) is an 8 Ω nominal sealed monitor with a 6.5" coaxial driver and a first-order 3.5 kHz crossover, listed at $2,060 per pair by the maker. ASR's Klippel data show a ragged, rising on-axis response, sensitivity near 81 dB rather than the claimed 86 dB, bass out by about 111 Hz (f3) and a measured impedance minimum of 2.3 Ω. Preference score is 2.6 (5.7 with sub). It suits nobody who values measured neutrality; fans of the brand and wall-placement use cite coherence, but the data do not support that.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 81.3 dB (low) | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) | A | computed (scripts/cta2034.py v2); claimed 86 dB per [mfr-vandersteen-vlr](../sources/mfr-vandersteen-vlr.md) |
| Listening-window deviation | ±3.4 dB, 300 Hz-10 kHz (borderline coloured) | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) | A | computed |
| On-axis deviation | ±4.8 dB | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) | A | computed |
| f3 / f6 | 111 / 70 Hz (needs a sub) | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) | A | computed; sealed box |
| Min impedance | 2.3 Ω @ ~4 kHz | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) | A | claimed 5 Ω min, 8 Ω nominal |
| Preference score | 2.6 / 5.7 with sub | [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid |
| Crossover | 3.5 kHz first order | [mfr-vandersteen-vlr](../sources/mfr-vandersteen-vlr.md) | C | |

## Directivity
Horizontal -6 dB beamwidth about 112°, vertical about 91°. DI is a major discontinuity (ERDI residual 2.6 dB); ASR notes little directivity control and a large directivity error between 2 and 5 kHz. SPDI rises from 4.7 dB at 1 kHz to 7.8 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.1 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +1.5 dB, so the on-axis response is brighter than the window; aim the speakers slightly off the listener (less toe-in) per the data, though ASR's own on-axis plot is the ragged one. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No max-SPL or compression test. ASR's THD plots are in dB SPL, so no % entered. At 86 dB the harmonic content peaks near 50 Hz and is moderate in the midrange; ASR judged it OK at 86 dB but not at 96 dB, where distortion products in the bass reach roughly 65-80 dB SPL (graph-read, approx.). With 81 dB sensitivity it needs far more power than typical for a given level; suited to small rooms and moderate levels. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Maker rates 8 Ω nominal, 5 Ω minimum. ASR measured 2.3 Ω around 4 kHz (about 19 Ω at 20 Hz), so flagged `effectively-4ohm`. Phase is moderate in the audible band. EPDR not computed. Use an amplifier stable into 2-4 Ω loads. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [toneaudio-vandersteen-vlr](../sources/toneaudio-vandersteen-vlr.md) (TONE Audio, 2015): praised coherence, natural balance and imaging; said it needs rear-wall placement for bass and is easy to drive.
- [asr-vandersteen-vlr](../sources/asr-vandersteen-vlr.md) (ASR, Tier D listening notes): tonal balance swings between loud highs and weak lows; not recommended.

## User reviews
One owner report found, so anecdotal ([users-vandersteen-vlr](../sources/users-vandersteen-vlr.md)): inefficient, little bass away from a wall, lumpy treble; good build and saxophone rendering. No QC problems reported.

## Conflicts
- Sensitivity: 81.3 dB measured (reviewer text "80 dB") vs 86 dB claimed; delta -4.7 dB.
- Minimum impedance: 2.3 Ω measured vs 5 Ω claimed.
- Critics disagree: Tone Audio (2015, manufacturer-hosted reprint) praised treble extension and ease of drive; ASR measured rising treble and a very difficult load.
- Model identity: ASR's "VLR" is assumed to be today's VLR Wood; the maker also sells the pricier VLR CT. ASR price $1,815 (2022) vs $2,060 now.

## Related
[Vandersteen](../brands/vandersteen.md) · [spinorama](../concepts/spinorama.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [preference-score](../concepts/preference-score.md)
