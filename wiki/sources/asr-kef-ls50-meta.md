---
type: source
slug: asr-kef-ls50-meta
title: "KEF LS50 Meta Review (Speaker)"
url: https://www.audiosciencereview.com/forum/index.php?threads/kef-ls50-meta-review-speaker.25574/
author: amirm
outlet: Audio Science Review
published: 2021-08-07
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-kef-ls50-meta.md
raw_data: raw/spinorama/KEF LS50 Meta/asr/
assets: [raw/assets/asr-kef-ls50-meta-impedance.png]
speakers: [kef-ls50-meta]
---
# ASR: KEF LS50 Meta review (2021-08-07)

## Summary
Amir measured a purchased pair on the Klippel NFS and called the spinorama close to perfection, with only some roughness in the crossover region and a bump at 1.5-2 kHz. He flagged low sensitivity (~83 dB), a 3.7 Ω impedance floor and heavy bass distortion, and recommended it with a subwoofer for loud bass. Tier D listening notes: sound "right and very nice"; bass notes distort and crackle when pushed.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.4 dB | computed, scripts/cta2034.py v2; reviewer says "around 83 dB" |
| lw_deviation_db | ±1.6 dB | computed |
| on_axis_deviation_db | ±1.6 dB | computed |
| f3 / f6 | 68 / 48 Hz | computed |
| hor / ver beamwidth | 113° / 108° | computed; reviewer says about ±50° horizontal |
| di_smoothness | smooth (ERDI residual 0.8 dB) | computed |
| er_dip_1_5khz | 2.0 dB | computed |
| on_minus_lw_4_10k | +0.7 dB | computed |
| pref_score | 5.4 / 7.6 with sub | spinorama.org (5.43 / 7.57) |
| min_impedance_ohm | 3.7 Ω | stated; frequency not given in text |
| THD | ~100% at lowest bass even at 86 dB; excellent above 200 Hz | plot level/values not defensibly readable to %; thd fields left to [[eac-kef-ls50-meta]] |

## Method notes
Klippel NFS, reference axis at tweeter centre, over 1000 points. Unit bought by a member and drop-shipped.

## Reliability notes
Single sample. Impedance graph saved (raw/assets/asr-kef-ls50-meta-impedance.png).

## Related
[[kef-ls50-meta]] · [[asr]] · [[kef]] · [[spinorama-org]]
