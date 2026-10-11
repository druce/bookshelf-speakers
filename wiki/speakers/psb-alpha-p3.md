---
type: speaker
brand: PSB
model: Alpha P3
slug: psb-alpha-p3
status: current
price_usd_pair: 349
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.9
min_impedance_hz: 190
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 80.3
sensitivity_claimed_db: 85.0
f3_hz: 62
f6_hz: 56
lw_deviation_db: 3.1
on_axis_deviation_db: 3.4
hor_beamwidth_deg: 134
ver_beamwidth_deg: 83
di_smoothness: minor-discontinuity
crossover_hz: 3000
max_spl_db: null
thd_86db_pct: 2.7
thd_96db_pct: null
pref_score: 3.1
pref_score_sub: 5.6
woofer_in: 4
tweeter_type: dome
port: rear
dimensions_mm: 220x130x174
weight_kg: 2.2
critic_consensus: Launch reviews praised clean, detailed mids and highs and a small footprint but noted little bass below about 60 Hz; ASR's measurements show uneven response with port/woofer resonances and very low sensitivity.
user_consensus: null
sources: [asr-psb-alpha-p3, soundstage-psb-alpha-p3, trustedreviews-psb-alpha-p3, mfr-psb-alpha-p3, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "57-21,000 Hz +/-3 dB on axis; LF cutoff -10 dB 43 Hz"
primary_measurement: asr-psb-alpha-p3
measurement_count: 1
---

## Summary
The PSB Alpha P3 is a very small (220 mm tall) 8 Ω-rated two-way with a 4" woofer, a 0.75" aluminium dome mounted below it and a rear port, around $349 per pair. ASR's Klippel data show a listening window of ±3.1 dB, f3 of 62 Hz, port and woofer resonances breaking through the response, and very low sensitivity (80.3 dB). Impedance dips to about 3.9 Ω, so it behaves like a 4 Ω speaker despite the 8 Ω rating. Early reviewers liked its clarity for the money; measurements suggest it suits only small rooms at modest levels, ideally with a subwoofer.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 80.3 dB (low) | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | computed (scripts/cta2034.py v2); maker claims 85 dB anechoic ([mfr-psb-alpha-p3](../sources/mfr-psb-alpha-p3.md)) |
| Listening-window deviation | ±3.1 dB, 300 Hz-10 kHz (between good and coloured) | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | computed |
| On-axis deviation | ±3.4 dB | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | computed; port/woofer resonances |
| f3 / f6 | 62 / 56 Hz (modest) | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | computed |
| Min impedance | 3.9 Ω @ ~190 Hz | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | graph-read (approx.); maker 4 Ω |
| THD at 86 dB | ~2.7 % (100-300 Hz) | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | graph-read (approx.); narrow >5 % spike ~380 Hz |
| THD at 96 dB | >5 % ~100 Hz-1 kHz | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) | A | graph clips at 5 %; no number entered |
| Preference score | 3.1 (no sub) / 5.6 (with sub) | [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid |
| Crossover | 3 kHz, 4th-order acoustic LR | [mfr-psb-alpha-p3](../sources/mfr-psb-alpha-p3.md) | C | |

## Directivity
Horizontal -6 dB beamwidth about 134°, vertical about 83°. DI classed minor-discontinuity (ERDI residual 1.6 dB); SPDI rises from 1.4 dB at 1 kHz to 8.2 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.3 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.4 dB, so either aim works. ASR notes a typical two-way vertical lobe: put the tweeter (below the woofer) near ear height or slightly below. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
ASR's Klippel plots show about 2-2.7 % THD between 100 and 300 Hz at 86 dB SPL (graph-read), with a narrow spike above 5 % near 380 Hz, and over 5 % across roughly 100 Hz-1 kHz at 96 dB. ASR needed the highest drive level he has tested to reach 86 dB because of low sensitivity, and bass turned tubby when pushed. No compression or max-SPL test. Suitable only for small rooms at moderate volume. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 8 Ω nominal, 4 Ω minimum, but ASR measured about 3.9 Ω near 190 Hz, flagged `effectively-4ohm`, with a large resonance peak near 90 Hz. With 80 dB sensitivity, ASR says it needs a "very stout" amplifier despite its size. EPDR not computed. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [soundstage-psb-alpha-p3](../sources/soundstage-psb-alpha-p3.md) (SoundStage!, Doug Schneider, 2019): very clean mids and highs for the price; nothing below about 60 Hz.
- [trustedreviews-psb-alpha-p3](../sources/trustedreviews-psb-alpha-p3.md) (Trusted Reviews, 2019): poised, agile and refined treble; cool-neutral tone; fuzzy deep bass.
- [asr-psb-alpha-p3](../sources/asr-psb-alpha-p3.md) (ASR, Tier D listening): harsh highs and a vocal resonance until EQ'd; does not recommend.

## User reviews
No user reports ingested yet (Reddit blocked scripted access; retailer and Amazon pages did not yield review text).

## Conflicts
- Sensitivity: claimed 85 dB anechoic vs 80.3 dB computed by Klippel (4.7 dB lower); ASR describes it as 5-6 dB below the average speaker. A forum member's 80.9 dB (300 Hz-3 kHz) agrees.
- Critics at launch (clean, "gem") vs ASR measurements (resonances, harshness): different samples, rig and expectations; unresolved.
- Impedance: maker 4 Ω min vs 3.9 Ω measured; consistent, but triggers the below-4 Ω flag.

## Related
[PSB](../brands/psb.md), [PSB Alpha P5](psb-alpha-p5.md), [PSB Imagine B50](psb-imagine-b50.md), KEF Q150, [Elac Debut 2.0 B5.2](elac-debut-2-0-b5-2.md), [directivity-index](../concepts/directivity-index.md), [impedance-and-epdr](../concepts/impedance-and-epdr.md)
