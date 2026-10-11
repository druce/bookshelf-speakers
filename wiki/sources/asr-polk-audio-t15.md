---
type: source
slug: asr-polk-audio-t15
title: "Polk T15 Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/polk-t15-bookshelf-speaker-review.11720/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-02-26
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-polk-audio-t15.md
raw_data: raw/spinorama/Polk Audio T15/asr/
assets: [raw/assets/asr-polk-audio-t15-impedance.png, raw/assets/asr-polk-audio-t15-thd.png]
speakers: [polk-audio-t15]
---
# ASR: Polk T15 review (2020-02-26)

## Summary
Klippel NFS measurement of a purchased pair (about $70). Amir finds a severe 3-6 kHz hole on axis from woofer/tweeter cancellation, large on/off-axis variation, resonances and a distortion peak near 400 Hz. Listening on a desk was "not horrible" but he does not recommend it and points to the Pioneer SP-BS22-LR instead.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 88.7 dB | computed, scripts/cta2034.py v2 from raw Klippel export; reviewer states none |
| lw_deviation_db | ±7.1 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±9.2 dB | computed |
| f3_hz / f6_hz | 88 / 73 Hz | computed |
| hor / ver beamwidth | 133° / 129° | computed |
| di_smoothness | major-discontinuity (ERDI residual 2.2 dB) | computed |
| er_dip_1_5khz_db | 6.2 dB | computed; flag over 3 dB |
| on_minus_lw_4_10k_db | -0.9 dB | computed |
| pref_score / with sub | 0.34 / 3.39 | spinorama.org; ASR post shows 0.3 / 3.3 |
| min_impedance_ohm | ~4.1 Ω @ ~60 Hz and ~250 Hz | graph-read (approx.); curve is also ~3.9 Ω near 20 kHz and ~3.7 Ω below 20 Hz; reviewer says "close to 4 ohms", maker says 6-8 Ω range |
| thd | not recorded as 86/96 dB | plot has no stated level; reads ~3.4 % near 80-95 Hz and a narrow ~4.5 % spike near 400 Hz, ~1-1.5 % at 500 Hz-1 kHz |
| Critique | on-axis dip 3-6 kHz; listen above or below tweeter axis; resonances; "distortion peak near 400 Hz" ghost heard in sweeps | Tier D/analysis text |

## Method notes
Klippel NFS, tweeter axis, grille off. Vertical sweeps show the +/-20° axes are flatter than on-axis; ASR advises placing above or below ear level. Distortion plot is labelled "gated/in-room" with no SPL.

## Reliability notes
Single sample purchased by the reviewer. Impedance and THD are graph-read.

## Related
[[polk-audio-t15]] · [[asr]] · [[polk-audio]] · [[spinorama-org]]
