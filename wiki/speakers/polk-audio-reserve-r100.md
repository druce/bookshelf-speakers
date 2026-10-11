---
type: speaker
brand: Polk Audio
model: Reserve R100
slug: polk-audio-reserve-r100
status: current
price_usd_pair: 559
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.6
min_impedance_hz: 250
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 85.1
sensitivity_claimed_db: 86.0
f3_hz: 67
f6_hz: 56
lw_deviation_db: 1.0
on_axis_deviation_db: 1.1
hor_beamwidth_deg: 140
ver_beamwidth_deg: 117
di_smoothness: minor-discontinuity
crossover_hz: 2700
max_spl_db: null
thd_86db_pct: 1.6
thd_96db_pct: 8.0
pref_score: 5.5
pref_score_sub: 7.9
woofer_in: 5.25
tweeter_type: dome
port: rear
dimensions_mm: 324x166x260
weight_kg: 5.5
critic_consensus: Thin coverage; one blog praises imaging and smooth, detailed treble, with limited deep bass.
user_consensus: null
sources: [eac-polk-audio-reserve-r100, mfr-polk-audio-reserve-r100, darksidevinyl-polk-audio-reserve-r100, users-polk-audio-reserve-r100, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "44 Hz-50 kHz overall; 58 Hz-39 kHz (-3 dB)"
primary_measurement: eac-polk-audio-reserve-r100
measurement_count: 1
---

## Summary
The Polk Reserve R100 is a 5.25" rear-ported (X-Port) standmount with a 1" Pinnacle ring radiator, sold at about $559/pair. Polk lists 8/6/4 Ω amplifier compatibility with a 3.6 Ω minimum and gives no explicit nominal rating; it is entered as 8 Ω under the "8 Ω compatible" rule and the measured minimum triggers the `effectively-4ohm` flag. On the Klippel it has a very flat listening window (±1.0 dB) but modest bass (f3 67 Hz), strong compression at high level and a sizeable distortion hump near 110 Hz. Suits small rooms at moderate levels with a sub or a 4 Ω-capable amp.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 85.1 dB (average) | [[eac-polk-audio-reserve-r100]] | A | computed (scripts/cta2034.py v2); claimed 86 dB in [[mfr-polk-audio-reserve-r100]] |
| Listening-window deviation | ±1.0 dB, 300 Hz-10 kHz (excellent) | [[eac-polk-audio-reserve-r100]] | A | computed |
| On-axis deviation | ±1.1 dB | [[eac-polk-audio-reserve-r100]] | A | computed |
| f3 / f6 | 67 / 56 Hz (modest) | [[eac-polk-audio-reserve-r100]] | A | computed; claimed -3 dB 58 Hz |
| Min impedance | ~3.6 Ω @ ~250 Hz | [[eac-polk-audio-reserve-r100]] | A | graph-read (approx.); maker also states 3.6 Ω |
| Preference score | 5.5 (no sub) / 7.9 (with sub) | [[eac-polk-audio-reserve-r100]] via [[spinorama-org]] | A | 5.46 / 7.93 raw |
| THD 86 dB @1 m | ~1.6 % | [[eac-polk-audio-reserve-r100]] | A | graph-read (approx.), highest across 100 Hz-10 kHz |
| THD 96 dB @1 m | ~8 % (110 Hz), ~5 % (6 kHz) | [[eac-polk-audio-reserve-r100]] | A | graph-read (approx.) |
| Crossover | 2.7 kHz | [[mfr-polk-audio-reserve-r100]] | C | |

## Directivity
Horizontal -6 dB beamwidth about 140°, vertical about 117°. DI is a minor discontinuity (ERDI residual 1.1 dB); SPDI rises from 4.9 dB at 1 kHz to 10.0 dB at 10 kHz, so the ring tweeter beams in the top octaves. Early-reflection dip near 1.5 kHz is 2.3 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.8 dB, so either aim works; Erin found treble becomes too prominent at high volume and said angling off-axis helped only a little. See [[directivity-index]], [[early-reflections]].

## Output & distortion
Erin's graphs (approximate): THD at 86 dB about 1.6 % at ~110 Hz and ~6 kHz; at 96 dB about 8 % near 110 Hz and 5 % near 6 kHz, well above the 3 % threshold in [[compression-and-max-spl]]. Compression at 102 dB reaches about -2.8 dB near 170 Hz and large LF losses below 80 Hz; Erin advises a subwoofer. No max-SPL figure stated. Fine for moderate listening in small rooms, not for loud levels in large ones.

## Amplifier load
Maker: 8/6/4 Ω compatible, 3.6 Ω minimum. Measured minimum about 3.6 Ω around 250 Hz (also ~4 Ω above 3 kHz), impedance peaks ~25 Ω at 38 and 90 Hz, phase moderate. EPDR not published. Flag `effectively-4ohm`; use an amp stable into 4 Ω. See [[impedance-and-epdr]].

## Critic reviews
- [[darksidevinyl-polk-audio-reserve-r100]] (Darkside Vinyl, hobbyist blog): impressive imaging, smooth and detailed treble, vocals well separated.
- [[eac-polk-audio-reserve-r100]] (Erin's Audio Corner, Tier D notes): punchy midbass/midrange like a small studio monitor, treble heavy at high volume, needs a sub.

## User reviews
About 5 thin reports, so anecdotal ([[users-polk-audio-reserve-r100]]): 1 dealer audition found it clean and not bright; 2 posters preferred the R200 for bass/price. No QC or reliability problems found.

## Conflicts
- Claimed -3 dB limit 58 Hz vs measured f3 67 Hz (9 Hz difference); claimed 86 dB vs 85.1 dB measured.
- Nominal impedance not stated by Polk; one forum owner calls it a "4 ohm" speaker (hearsay).
- Price: Polk shows $559 (list $699); Erin cited ~$650 in 2021.

## Related
[[polk-audio]] · [[polk-audio-reserve-r200]] · Polk Audio Signature Elite ES15 · [[spinorama]] · [[preference-score]]
