---
type: speaker
brand: Human Speakers
model: 81 dk
slug: human-speakers-81-dk
status: current
price_usd_pair: 1397
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 4.2
min_impedance_hz: 113
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 85.4
sensitivity_claimed_db: 90.3
f3_hz: 52
f6_hz: 40
lw_deviation_db: 4.5
on_axis_deviation_db: 4.2
hor_beamwidth_deg: 148
ver_beamwidth_deg: 99
di_smoothness: minor-discontinuity
crossover_hz: 1800
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 2.0
pref_score_sub: 4.0
woofer_in: 8
tweeter_type: null
port: null
dimensions_mm: 470x292x368
weight_kg: 13.2
critic_consensus: null
user_consensus: null
sources: [mfr-human-speakers-81-dk, asr-human-speakers-81-dk, users-human-speakers-81-dk, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "+/-2 dB from 38 Hz to 26 kHz"
primary_measurement: asr-human-speakers-81-dk
measurement_count: 1
image_url: "https://www.humanspeakers.com/human/images/81%20DK%20b.jpg"
---
<!-- photo -->
<img src="https://www.humanspeakers.com/human/images/81%20DK%20b.jpg" alt="Human Speakers 81 dk" width="360">

*Photo: [humanspeakers.com](https://www.humanspeakers.com/human/81dk.htm) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The HUMAN 81 DK is a hand-built two-way with an 8" woofer and a minimalist crossover, from a one-man New Hampshire company, at $1,397 per pair. It is nominally 6 Ω. ASR's Klippel data show an uneven speaker: listening-window deviation ±4.5 dB, a dip near 200 Hz, and a peak, dip and resonance around the 1.8 kHz crossover, plus weak output above 5 kHz. Bass is good (f3 52 Hz) and dispersion is very wide, but distortion at 96 dB is high. At 470 mm tall it slightly exceeds the ~18" guideline and is included with that note. Not a data-supported pick for accuracy.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 85.4 dB (average) | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | computed (scripts/cta2034.py v2) |
| Claimed sensitivity | 89 dB/1 W = about 90.3 dB at 2.83 V (6 Ω) | [mfr-human-speakers-81-dk](../sources/mfr-human-speakers-81-dk.md) | C | converted using the maker's 6 Ω nominal |
| Listening-window deviation | ±4.5 dB (coloured) | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | computed, 300 Hz-10 kHz |
| LW dip above f3 | -3.3 dB at 198 Hz | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | computed |
| On-axis deviation | ±4.2 dB | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | computed |
| f3 / f6 | 52 / 40 Hz (good) | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | computed |
| Min impedance | 4.2 Ω @ 113 Hz | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) | A | graph-read (approx.) |
| Preference score | 2.0 (no sub) / 4.0 (with sub) | [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) via [spinorama-org](../sources/spinorama-org.md) | A | not meaningful to <0.5 |
| Crossover | about 1.8 kHz | [mfr-human-speakers-81-dk](../sources/mfr-human-speakers-81-dk.md) | C | woofer flat to 1,800 Hz per maker |

## Directivity
Horizontal -6 dB beamwidth about 148°, vertical about 99°: very wide, so toe-in is less critical (ASR). DI is a minor discontinuity (ERDI residual 1.9 dB); SPDI 6.8 dB at 1 kHz to 8.5 dB at 10 kHz. The early-reflection dip near 1.5 kHz is 5.7 dB, well above the 3 dB flag, from the crossover-region problem. On-axis minus listening window above 4 kHz is +0.1 dB, so either aim works. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No max-SPL test. ASR's 86 dB sweep shows THD around 50 dB SPL in the 50-300 Hz region (graph-read, dB not %, so no % entered), with a narrow spike near 7 kHz. At 96 dB distortion is "quite high" (about 70 dB SPL from 40-300 Hz and about 68 dB near 2 kHz) and was audible to the reviewer. Treat as suitable for moderate levels; see [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Maker: nominally 6 Ω, 5-6 Ω mid-bass dip, fine with any amp rated for 8 Ω. ASR measured a 4.2 Ω minimum at 113 Hz, below the 4.8 Ω IEC floor for 6 Ω (flag `below-iec`), with resonances above 1 kHz. EPDR not computed. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-human-speakers-81-dk](../sources/asr-human-speakers-81-dk.md) (ASR, measurement only, no listening): "colored and flawed"; not recommended.
No other professional review of the 81 DK was found.

## User reviews
No owner reports of the 81 dk found ([users-human-speakers-81-dk](../sources/users-human-speakers-81-dk.md)).

## Conflicts
- Sensitivity: 85.4 dB measured vs about 90.3 dB claimed (89 dB/1 W at 6 Ω); 4.9 dB gap. Claimed FR ±2 dB 38 Hz-26 kHz is also not borne out (tweeter falls by about 5 kHz).
- Price: ASR cited $1,270 (kit or finished unclear); maker lists $1,397 per pair.
- Maker says the speakers can be called 6 or 8 Ω; 6 Ω used here.

## Related
[Human Speakers](../brands/human-speakers.md) · [directivity-index](../concepts/directivity-index.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [spinorama](../concepts/spinorama.md)
