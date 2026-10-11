---
type: source
slug: asr-hsu-research-mfl-6
title: "HSU MFL-6 Home Theater Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/hsu-mfl-6-home-theater-speaker-review.67955/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2025-12-09
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-hsu-research-mfl-6.md
raw_data: raw/spinorama/Hsu Research MFL-6/asr/
assets: [raw/assets/asr-hsu-research-mfl-6-impedance.png, raw/assets/asr-hsu-research-mfl-6-thd.png]
speakers: [hsu-research-mfl-6]
---
# ASR: HSU MFL-6 review (2025-12-09)

## Summary
Klippel measurement of a $279 sample sent by a member, measured with the microphone at 90° to the baffle (the intended listening axis for the slanted panel). ASR found highly elevated upper treble, woofer resonances causing a discontinuity near 2.5 kHz, distortion fine at 86 dB, a problem at 96 dB, still acceptable at 91 dB, and several impedance resonances. Not recommended; the reviewer suggested EQ down of the top end, or surround/Atmos use.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 85.5 dB | computed, scripts/cta2034.py v2 |
| lw_deviation_db | ±3.8 dB | computed |
| on_axis_deviation_db | ±5.0 dB | computed |
| f3 / f6 | 80 / 52 Hz | computed; gradual roll-off, port open |
| hor / ver beamwidth | 126° / 87° | computed |
| di_smoothness | major-discontinuity (ERDI residual 2.5 dB) | computed |
| er_dip_1_5khz_db | 3.0 dB | computed |
| on_minus_lw_4_10k_db | +1.3 dB | computed |
| SPDI 1 kHz / 10 kHz | 3.3 / 9.8 dB | computed |
| pref score | 3.4 / 5.6 | spinorama.org computation (3.44 / 5.57); an ASR member posted 3.6 / 5.7 |
| min_impedance_ohm | about 4.0 Ω near 200 Hz | graph-read (approx.); ASR label "4 ohm"; second dip about 4.2 Ω near 45 Hz |
| THD 86 dB | "nicely below target" per ASR | graph in dB SPL, no % entered |
| THD 96 dB | "quite high": about 75 dB SPL near 35 Hz, about 70 dB near 250 Hz | graph-read, dB SPL |
| 91 dB sweep | "performed well" per ASR | text |

## Method notes
Klippel NFS, grille off, reference axis rotated so the mic is at 90° to the slanted baffle. ±40° response flattens "a fair bit". Waterfall not run. No listening test.

## Reliability notes
Single sample. Because the reference axis differs from a flat-baffle speaker, deviation figures are not directly comparable with 0° measurements elsewhere.

## Related
[[hsu-research-mfl-6]] · [[asr]] · [[hsu-research]] · [[spinorama-org]]
