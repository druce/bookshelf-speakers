---
type: source
slug: asr-vandersteen-vlr
title: "Vandersteen VLR Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/vandersteen-vlr-speaker-review.35444/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2022-07-04
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-vandersteen-vlr.md
raw_data: raw/spinorama/Vandersteen VLR/asr/
assets: [raw/assets/asr-vandersteen-vlr-impedance.png, raw/assets/asr-vandersteen-vlr-thd.png]
speakers: [vandersteen-vlr]
---
# ASR: Vandersteen VLR review (2022-07-04)

## Summary
Klippel NFS review of a loaned pair ($1,815 per pair at the time). Amir found a rising, ragged on-axis response with sensitivity near 80 dB, large directivity errors between 2 and 5 kHz, and impedance falling to 2.3 Ω. He called it the second most broken speaker he had measured and did not recommend it.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 81.3 dB | computed, scripts/cta2034.py v2 (reviewer text says "just 80 dB") |
| lw_deviation_db | ±3.4 dB | computed |
| on_axis_deviation_db | ±4.8 dB | computed |
| f3 / f6 | 111 / 70 Hz | computed |
| hor / ver beamwidth | 112° / 91° | computed |
| di_smoothness | major-discontinuity (ERDI residual 2.6 dB) | computed |
| er_dip_1_5khz_db | 2.1 dB | computed |
| on_minus_lw_4_10k_db | +1.5 dB | computed |
| SPDI 1 kHz / 10 kHz | 4.7 / 7.8 dB | computed |
| pref_score / with sub | 2.6 / 5.7 | spinorama.org (2.58 / 5.65) |
| min_impedance_ohm | 2.3 Ω @ ~4 kHz | graph cursor label on ASR plot (also read as the minimum) |
| impedance at 20 Hz | ~19 Ω | graph-read (approx.); impedance high at LF |
| THD 86 / 96 dB | not entered | plot is in dB SPL; at 86 dB THD peaks ~60 dB SPL near 50 Hz and ~45 dB SPL near 1.5-2.5 kHz, at 96 dB ~65-80 dB SPL below 400 Hz (graph-read, approx.); no defensible % |
| Port | none (sealed) | ASR confirmed in thread |
| crossover | first order (maker: 3.5 kHz) | |

## Method notes
Klippel NFS, reference axis the tweeter. Grille status not stated in the review (an Audiogon poster, not verified, claims the grille is part of the design). Listening tests mono, subjective (Tier D): male voice barely audible against female voice; loud highs, lacking low frequencies.

## Reliability notes
Single loaned sample. Model name "VLR" taken as the wood-finish VLR sold today as "VLR Wood" (assumption). Impedance minimum is an unusual feature: forum members suspect a series capacitor on the woofer.

## Related
[[vandersteen-vlr]] · [[asr]] · [[vandersteen]] · [[spinorama-org]]
