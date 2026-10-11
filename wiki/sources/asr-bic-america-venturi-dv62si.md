---
type: source
slug: asr-bic-america-venturi-dv62si
title: "BIC America DV62si Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/bic-america-dv62si-bookshelf-speaker-review.14918/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-07-25
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-bic-america-venturi-dv62si.md
raw_data: raw/spinorama/BIC America Venturi DV62si/asr/
assets: [raw/assets/asr-bic-america-venturi-dv62si-impedance.png, raw/assets/asr-bic-america-venturi-dv62si-thd.png]
speakers: [bic-america-venturi-dv62si]
---
# ASR: BIC DV62si review (2020-07-25)

## Summary
Klippel NFS test of a loaned pair (about $120 on Amazon at the time). Amir found uneven response with strongly elevated highs, directivity "out of control" (the worst horizontal directivity plot he had seen) and distortion at 96 dB across the band. He liked the large woofer's ability to play loud and warm, but does not recommend it.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 87.0 dB | computed, scripts/cta2034.py v2 from raw Klippel export; not stated in review |
| lw_deviation_db | ±3.5 dB | computed; 300 Hz-10 kHz |
| on_axis_deviation_db | ±4.1 dB | computed |
| f3_hz / f6_hz | 80 / 70 Hz | computed |
| lw_dip_above_f3 | -3.3 dB @ 219 Hz | computed |
| hor / ver beamwidth | 111 / 122 deg | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.3 dB) | computed |
| er_dip_1_5khz_db | 5.2 dB | computed; ASR sees a ~3 kHz dip that depends on room absorption |
| on_minus_lw_4_10k_db | +0.6 dB | computed |
| spdi_1k / 10k | 5.0 / 6.7 dB | computed |
| pref_score / with sub | 2.4 / 5.3 | spinorama.org computation (2.42 / 5.34) |
| min_impedance_ohm | ~5.8 Ω @ ~10 kHz | graph-read (approx.); the graph's own annotation says "min impedance = 7 ohm" (flat ~7 Ω at 50-400 Hz) |
| impedance peaks | ~34 Ω @ ~23 Hz, ~28 Ω @ ~95 Hz (port tuning) | graph-read (approx.) |
| thd_86db_pct | ~1.7 % peak at ~1.8 kHz | graph-read (approx.), relative THD plot; most of 100 Hz-10 kHz is below 0.8 %; the 1.8 kHz step is the woofer breakup region |
| thd_96db_pct | ~1.9 % | graph-read (approx.), peaks near 130 Hz and 9 kHz; about 0.3-1.7 % elsewhere ("distortion everywhere") |
| crossover | ~3.5 kHz | ASR says he read this elsewhere; woofer runs to ~7 kHz |

## Method notes
Klippel NFS, 700+ points, tweeter-centre axis, 78 F. Review shows relative THD (percent) at 86 and 96 dB SPL at 1 m in a non-anechoic setup; no Audio Precision test and no compression/max-SPL test. Impedance read from the plot image.

## Reliability notes
Single loaned sample (member-owned); build quality remarks (glued tweeter rattle reports) are secondhand from Amazon. Subjective listening: highs stand out and seem "high-resolution" at first, then sharp and lisping; EQ to fix left grit (Tier D).

## Related
[BIC America Venturi DV62si](../speakers/bic-america-venturi-dv62si.md) · [asr](../reviewers/asr.md) · [BIC America](../brands/bic-america.md) · [spinorama-org](spinorama-org.md)
