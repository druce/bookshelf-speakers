---
type: source
slug: asr-hsu-research-ccb-8
title: "HSU CCB-8 Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/hsu-ccb-8-speaker-review.68131/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2025-12-17
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-hsu-research-ccb-8.md
raw_data: raw/spinorama/Hsu Research CCB-8/asr/
assets: [raw/assets/asr-hsu-research-ccb-8-impedance.png, raw/assets/asr-hsu-research-ccb-8-thd.png, raw/assets/asr-hsu-research-ccb-8-thd101.png]
speakers: [hsu-research-ccb-8]
---
# ASR: HSU CCB-8 review (2025-12-17)

## Summary
Klippel NFS measurement of a drop-shipped sample ($389 each). ASR found a large cancellation around 1.7 kHz, rough directivity that contradicts the "constant directivity" claim, a port/cabinet resonance between 1 and 2 kHz, and impedance a little under 4 Ω. Sensitivity is about 5 dB better than the average speaker ASR tests. Conclusion: not recommended. No listening test.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 88.8 dB | computed, scripts/cta2034.py v2 from raw Klippel export; ASR text: "5 or so dB" above average |
| lw_deviation_db | ±5.2 dB | computed |
| on_axis_deviation_db | ±6.0 dB | computed |
| f3 / f6 | 59 / 54 Hz | computed; ports open (as shipped, partially plugged, instructions followed) |
| hor / ver beamwidth | 106° / 112° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.9 dB) | computed |
| er_dip_1_5khz_db | 4.8 dB | computed |
| on_minus_lw_4_10k_db | +1.6 dB | computed |
| SPDI 1 kHz / 10 kHz | 6.5 / 10.8 dB | computed |
| pref score | 1.6 (no sub) / 4.0 (with sub) | spinorama.org computation (1.62 / 4.04) |
| min_impedance_ohm | 3.8 Ω @ 182 Hz | graph-read (approx.); ASR cursor 3.75 Ω; text "a bit below 4 ohm" |
| THD 86 dB | very low per ASR; graph shows THD about 46 dB SPL near 50 Hz and 130-200 Hz | graph-read, in dB SPL not %; no defensible % entered |
| THD 96 dB / 101 dB | "large increase" at 96 dB; reviewer heard distortion at 101 dB | graph in dB SPL; THD to about 70 dB SPL near 30-40 Hz and 65 dB near 130 Hz |

## Method notes
Klippel Near-field Scanner, magnetic grille removed, 0° reference axis; ASR also showed -20° as a listening alternative following the manual's 15° recommendation. Measured with dual ports open. Distortion plots are SPL-referenced non-anechoic sweeps at 86, 96 and 101 dB at 1 m.

## Reliability notes
Single sample, drop-shipped by a member. Raw Klippel data available. Reviewer had low motivation to listen, so there are no subjective notes.

## Related
[Hsu Research CCB-8](../speakers/hsu-research-ccb-8.md) · [asr](../reviewers/asr.md) · [Hsu Research](../brands/hsu-research.md) · [spinorama-org](spinorama-org.md)
