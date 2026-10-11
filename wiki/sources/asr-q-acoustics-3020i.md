---
type: source
slug: asr-q-acoustics-3020i
title: "Q Acoustics 3020i Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/q-acoustics-3020i-bookshelf-speaker-review.14568/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-07-06
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-q-acoustics-3020i.md
raw_data: raw/spinorama/Q Acoustics 3020i/asr/
assets: [raw/assets/asr-q-acoustics-3020i-impedance.png, raw/assets/asr-q-acoustics-3020i-thd.png]
speakers: [q-acoustics-3020i]
---
# ASR: Q Acoustics 3020i review (2020-07-06)

## Summary
Klippel NFS measurement of a pair purchased new (US $315 via Amazon). Amir finds a mostly flat on-axis response with high-frequency rise, a dip at 2-4 kHz around the 2.4 kHz crossover, two narrow resonances (366 Hz noted), mismatched woofer and tweeter beamwidth, and heavy woofer distortion at 96 dB below about 100 Hz. He rated it "not bad" but would not recommend it without EQ (Tier D opinion).

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 86.1 dB | computed, scripts/cta2034.py v2 from raw Klippel export; reviewer states 86 dB |
| lw_deviation_db | ±2.0 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±2.2 dB | computed |
| f3_hz / f6_hz | 77 / 59 Hz | computed; reviewer states ±3.8 dB 64 Hz-20 kHz, ±2.8 dB 80 Hz-20 kHz |
| hor / ver beamwidth | 142° / 96° | computed (reviewer calls horizontal beamwidth "narrow side" and uneven) |
| di_smoothness | minor-discontinuity (ERDI residual 1.8 dB) | computed |
| er_dip_1_5khz_db | 3.5 dB | computed; above the 3 dB flag |
| on_minus_lw_4_10k_db | +0.6 dB | computed |
| spdi 1 kHz / 10 kHz | 5.3 / 8.4 dB | computed |
| pref_score / with sub | 3.86 / 6.38 | spinorama.org computation; reviewer's post shows 4.0 / 6.4 |
| min_impedance_ohm | 3.9 Ω | stated in graph title; trough lies around 200-300 Hz and again near 2.7 kHz (graph-read) |
| thd_96db_pct | ~3.3% | graph-read (approx.): THD about -30 dB relative near 100-110 Hz at 96 dB; THD exceeds fundamental below ~45 Hz (reviewer annotation) |
| thd_86db_pct | not available | only a 96 dB plot was ingested |
| crossover | 2.4 kHz | stated |

## Method notes
Klippel Near-field Scanner, 800+ points, grille off. Distortion plot is at 96 dB SPL at 1 m (dB-V axis). Impedance plot includes phase.

## Reliability notes
Single purchased sample. Amir's "Tier D" listening notes: bright on female vocals ("zing" fixed with a high-frequency shelf), plays loud without woofer bottoming. SoundStage/NRC measurements ([[nrc-q-acoustics-3020i]]) correlate well per the reviewer.

## Related
[[q-acoustics-3020i]] · [[asr]] · [[q-acoustics]] · [[spinorama-org]]
