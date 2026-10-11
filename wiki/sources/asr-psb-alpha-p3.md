---
type: source
slug: asr-psb-alpha-p3
title: "PSB Alpha P3 Review (Bookshelf Speaker)"
url: https://www.audiosciencereview.com/forum/index.php?threads/psb-alpha-p3-review-bookshelf-speaker.27498/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2021-10-22
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-psb-alpha-p3.md
raw_data: raw/spinorama/PSB Alpha P3/asr/
assets: [raw/assets/asr-psb-alpha-p3-impedance.png, raw/assets/asr-psb-alpha-p3-thd.png, raw/assets/asr-psb-alpha-p3-thd-relative.png]
speakers: [psb-alpha-p3]
---
# ASR: PSB Alpha P3 review (2021-10-22)

## Summary
Amir measured a loaner P3 (US $249 at the time) on the Klippel NFS and was disappointed: uneven on-axis response with port and woofer resonances breaking through, very low sensitivity (needed the highest drive level he has used to reach 86 dB SPL), and low impedance. He EQ'd the 3-4 kHz region to tame harshness and did not recommend it.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 80.3 dB | computed, scripts/cta2034.py v2; reviewer gives no figure but says 5-6 dB below average |
| lw_deviation_db | ±3.1 dB | computed |
| on_axis_deviation_db | ±3.4 dB | computed |
| f3_hz / f6_hz | 62 / 56 Hz | computed |
| hor / ver beamwidth | 134 / 83 deg | computed |
| di_smoothness | minor-discontinuity | ERDI residual 1.6 dB; ER dip 1.5 kHz 2.3 dB; on-axis minus LW 4-10 kHz +0.4 dB |
| SPDI 1 kHz / 10 kHz | 1.4 / 8.2 dB | computed |
| pref_score | 3.1 / 5.6 with sub | spinorama.org (3.12 / 5.64) |
| min_impedance_ohm | 3.9 Ω at about 190 Hz | graph-read (approx.); plot annotated "Min impedance = 3.9 ohm" |
| thd_86db_pct | about 2.7 % (broad 2-2.7 % over 100-300 Hz) | graph-read (approx.), 100 Hz-10 kHz; a narrow spike above 5 % at about 380 Hz excluded; rises sharply below 70 Hz |
| thd_96db_pct | above 5 % from about 100 Hz to 1 kHz | graph-read; plot clips at 5 %, so no number entered |
| port/woofer resonances | about 400 Hz and 3-4 kHz region | nearfield plot; audible "zing" in sweeps |

## Method notes
Klippel NFS, reference axis tweeter centre, grille off, over 1000 measurement points (about 1 % error). THD at 86 and 96 dB SPL @ 1 m. No compression or max-SPL test. Impedance by Klippel.

## Reliability notes
Single loaned sample. Reviewer's ears were temporarily blocked during listening so he emphasised measurements. A forum member's own spinorama table reports 80.9 dB sensitivity (300 Hz-3 kHz), consistent with 80.3 dB.

## Related
[PSB Alpha P3](../speakers/psb-alpha-p3.md) · [asr](../reviewers/asr.md) · [spinorama-org](spinorama-org.md) · [PSB](../brands/psb.md)
