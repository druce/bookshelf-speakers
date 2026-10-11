---
type: source
slug: asr-avantone-pro-cla-10
title: "Avantone CLA-10 (Yamaha NS-10M Clone) Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/avantone-cla-10-yamaha-ns-10m-clone-review.46954/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2023-08-05
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-avantone-pro-cla-10.md
raw_data: raw/spinorama/Avantone Pro CLA-10/asr/
assets: [raw/assets/asr-avantone-pro-cla-10-impedance.png, raw/assets/asr-avantone-pro-cla-10-thd.png, raw/assets/asr-avantone-pro-cla-10-thd-rel.png]
speakers: [avantone-pro-cla-10]
---
# ASR: Avantone CLA-10 review (2023-08-05)

## Summary
Amir tested a purchased pair ($699 from Amazon, about $750 with tax) on the Klippel NFS and called the response "horribly bad": a large mid-to-treble boost, a narrow resonance near 3.5 kHz, large directivity error and the worst waterfall he had seen. He concludes it is not a faithful NS-10M clone and does not recommend it. Listening notes (Tier D) found it grungy and treble-heavy even after EQ.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 90.2 dB | computed, scripts/cta2034.py v2 from raw Klippel export (claimed 90 dB) |
| lw_deviation_db | ±2.8 dB | computed; 300 Hz-10 kHz |
| on_axis_deviation_db | ±3.3 dB | computed |
| f3_hz / f6_hz | 131 / 95 Hz | computed |
| lw_dip_above_f3 | -3.1 dB @ 284 Hz | computed |
| hor / ver beamwidth | 142 / 110 deg | computed (see method notes: tested on its side) |
| di_smoothness | minor-discontinuity (ERDI residual 1.9 dB) | computed |
| er_dip_1_5khz_db | 0.8 dB | computed |
| on_minus_lw_4_10k_db | +0.7 dB | computed |
| spdi_1k / 10k | 5.7 / 7.8 dB | computed |
| pref_score / with sub | 2.2 / 5.9 | spinorama.org computation (2.23 / 5.87) |
| min_impedance_ohm | 6.8 Ω | stated on ASR impedance graph ("rated 8"); frequency not marked; curve sits near 6.7-7 Ω below 20 Hz, at ~200 Hz and ~6 kHz |
| impedance peak | ~33 Ω @ ~100 Hz | graph-read (approx.); sealed-box resonance |
| THD 86/96 dB | not extracted as % | plotted in dB only; see method notes (approx.) |

## Method notes
Klippel NFS, speaker tested vertically (tweeter-centre reference axis); horizontal and vertical data are transposed for the early-reflection plots, but preference score cannot be transposed so is computed for the as-tested orientation. Reviewer notes that orientation on its side would put the "massive" directivity error in the horizontal plane. THD plots are absolute (dB re 20 µPa) at 86 and 96 dB SPL at 1 m non-anechoic; approx. graph-read: at 86 dB, THD peaks about 46 dB near 100-150 Hz and 1.3 kHz against a ~87-90 dB fundamental (roughly 1% or less); at 96 dB, THD about 65 dB at 60-150 Hz (roughly 2-3%) and 50-57 dB across mids. These were not converted to a defensible single % so frontmatter THD is null. No max-SPL test. Amir compares with Newell/Holland/Newell paper on the Yamaha NS10M, whose anechoic data showed a lesser boost.

## Reliability notes
Single purchased retail sample, no manufacturer involvement. Strongly negative tone; the subjective part is Tier D. A forum member's EQ-based score calculation (1.4 no-EQ) differs from the 2.2 computed here because of different orientation or method; the spinorama.org value is used.

## Related
[[avantone-pro-cla-10]] · [[asr]] · [[avantone-pro]] · [[spinorama-org]]
