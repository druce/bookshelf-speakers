---
type: source
slug: asr-monitor-audio-apex-a10
title: "Monitor Audio Apex A10 Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/monitor-audio-apex-a10-speaker-review.60230/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2025-01-22
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-monitor-audio-apex-a10.md
raw_data: raw/spinorama/Monitor Audio Apex A10/asr/
assets: [raw/assets/asr-monitor-audio-apex-a10-impedance.png, raw/assets/asr-monitor-audio-apex-a10-thd.png]
speakers: [monitor-audio-apex-a10]
---
# ASR: Monitor Audio Apex A10 review (2025-01-22)

## Summary
Klippel NFS review of a member-loaned A10, a compact "lifestyle" home-theatre speaker costing US $750 each per ASR. Amir found a midrange dip, resonances near 1-2 kHz and elevated treble (about 7 dB variation), wider-than-average horizontal dispersion, good power handling at 86 dB but audible and measurable strain at 96 dB. He could not recommend it at the price.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 86.3 dB | computed, scripts/cta2034.py v2 from raw Klippel export; claimed 87 dB |
| lw_deviation_db | ±2.7 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±3.0 dB | computed |
| f3 / f6 | 96 / 77 Hz | computed |
| hor / ver beamwidth | 146° / 107° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.7 dB) | computed |
| er_dip_1_5khz | 2.4 dB | computed |
| on_minus_lw_4_10k | +0.4 dB | computed |
| SPDI 1 kHz / 10 kHz | 4.1 / 8.2 dB | computed |
| pref score | 2.75 (no sub) / 5.92 (sub) | spinorama.org computation |
| min_impedance | ASR label "4 ohm @ 58 Hz"; plot also shows ~3.6 Ω below 10 Hz and ~3.0 Ω near 10-15 kHz | graph-read (approx.) |
| impedance peaks | ~17 Ω @ 32 Hz, ~26 Ω @ 115 Hz, ~11 Ω @ 3 kHz | graph-read (approx.) |
| thd_86db_pct | ~1.5% worst across 100 Hz-10 kHz (near 100 Hz); narrow ~1.8% spike at 2 kHz | graph-read (approx.) |
| thd_96db_pct | ~5% (chart-top) in 100-150 Hz; ~2.5% bumps 300-700 Hz; ~2.9% spike at 2 kHz | graph-read (approx.) |

## Method notes
Klippel NFS, speaker driven on its own; non-anechoic THD plots at 86 and 96 dB. Reviewer annotated the 2 kHz third-order distortion peak as a problem. Listening: bright out of the box; boosting upper bass with EQ made it warmer and more balanced; very faint sub-bass.

## Reliability notes
Single loaned sample. Directivity and distortion plots are as shown; no max SPL test. The THD plot title in the image reads "Monitor Audio Apex 100" (apparent labelling slip on a reused template); the post and file names identify the A10.

## Related
[[monitor-audio-apex-a10]] · [[asr]] · [[monitor-audio]] · [[spinorama-org]]
