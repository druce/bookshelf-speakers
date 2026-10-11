---
type: source
slug: asr-psb-alpha-p5
title: "PSB Alpha P5 Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/psb-alpha-p5-speaker-review.15161/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-08-06
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-psb-alpha-p5.md
raw_data: raw/spinorama/PSB Alpha P5/asr/
assets: [raw/assets/asr-psb-alpha-p5-impedance.png, raw/assets/asr-psb-alpha-p5-thd.png, raw/assets/asr-psb-alpha-p5-thd-absolute.png, raw/assets/asr-psb-alpha-p5-compression.png]
speakers: [psb-alpha-p5]
---
# ASR: PSB Alpha P5 review (2020-08-06)

## Summary
Amir bought the P5 on Amazon ($349) and measured it on the Klippel NFS. He found an uneven on-axis response, a prominent rear-port peak that pushes up the response, strong directivity mismatch near the 3 kHz crossover, and high distortion even at 86 dB SPL. He called the result depressing and did not recommend it, while noting Stereophile's own measurements look similar.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.6 dB | computed, scripts/cta2034.py v2; reviewer gives no figure |
| lw_deviation_db | ±2.8 dB | computed |
| on_axis_deviation_db | ±3.1 dB | computed |
| f3_hz / f6_hz | 56 / 50 Hz | computed |
| hor / ver beamwidth | 132 / 106 deg | computed; ASR describes "typical ±50 degree", wider at crossover |
| di_smoothness | major-discontinuity | ERDI residual 2.2 dB; ER dip 1.5 kHz 1.0 dB; on-axis minus LW 4-10 kHz +0.7 dB |
| SPDI 1 kHz / 10 kHz | 5.2 / 7.8 dB | computed |
| pref_score | 4.0 / 6.3 with sub | spinorama.org (3.99 / 6.25) |
| min_impedance_ohm | 3.9 Ω at about 190 Hz | graph-read (approx.); plot annotated "min impedance = 3.9 ohm" |
| thd_86db_pct | about 2.7 % peak near 120-150 Hz; about 2 % near 600 Hz and 1 kHz | graph-read (approx.), 100 Hz-10 kHz; ASR calls it high |
| thd_96db_pct | above 5 % across about 80 Hz-1.5 kHz | graph-read; plot clips at 5 %, no number entered |
| compression (200 Hz) | plot annotated "102 dB SPL @ 1 m"; only 0.45 dB compression at +9.4 dB over 96 dB and 1.6 dB at +15 dB | graph-read; method is ASR's 200 Hz linearity sweep |
| woofer bottoming | woofer bottomed out on a deep-bass track | subjective test |

## Method notes
Klippel NFS, tweeter-centre reference axis, over 800 measurement points (error slightly above 1 % at HF). 80 degF test temperature. Distortion by Klippel KA3 at 86/96 dB; compression by Audio Precision at 200 Hz.

## Reliability notes
Single purchased retail sample (Amazon). Tier-A. Reviewer's listening impressions (warm females, lost male vocals) are Tier D and he concedes bias.

## Related
[[psb-alpha-p5]] · [[stereophile-psb-alpha-p5]] · [[asr]] · [[spinorama-org]] · [[psb]]
