---
type: source
slug: asr-revel-m105
title: "Revel M105 Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/revel-m105-bookshelf-speaker-review.14745/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-07-16
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-revel-m105.md
raw_data: raw/spinorama/Revel M105/asr/
assets: [raw/assets/asr-revel-m105-impedance.png, raw/assets/asr-revel-m105-thd.png, raw/assets/asr-revel-m105-compression.png]
speakers: [revel-m105]
---
# ASR: Revel M105 review (2020-07-16)

## Summary
Klippel NFS review of the Performa3 M105 (5.25" two-way, bought via the reviewer's own Harman dealership, disclosed). Amir finds the on-axis response essentially flat apart from a peak near 5 kHz that largely vanishes in the listening window, very clean distortion above about 500 Hz, wide horizontal dispersion and a "room friendly" early-reflection response. He notes impedance is on the low side and recommends a good amplifier. He gave it a strong recommendation as a neutral, low-distortion monitor, and found EQ on the 5 kHz hump and a steep low-frequency roll-off improved it further.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 84.8 dB | computed, scripts/cta2034.py v2 from raw Klippel export; claimed 86 dB |
| lw_deviation_db | ±1.3 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±1.8 dB | computed |
| f3 / f6 | 60 / 54 Hz | computed |
| hor / ver beamwidth | 141° / 111° | computed, -6 dB |
| di_smoothness | minor-discontinuity | ERDI max residual 1.2 dB |
| er_dip_1_5khz_db | 0.4 dB | computed |
| on_minus_lw_4_10k_db | +0.7 dB | computed |
| SPDI 1 kHz / 10 kHz | 5.2 / 8.1 dB | computed |
| pref_score / with sub | 5.8 / 8.2 | spinorama.org computation (5.76 / 8.18) |
| min_impedance_ohm | 3.8 Ω @ ~230 Hz | graph-read (approx.); plot title states 3.8 Ω |
| THD at 96 dB | ~8% at 100 Hz, <0.3% above 500 Hz | graph-read (approx.); 2nd harmonic dominates; 96 dB SPL @1 m stated on plot |
| THD at 86 dB | not shown | |
| Compression at 80 Hz | ~111 dB SPL before compression | graph-read from ASR draft bar chart; threshold not stated |
| Price | US $750 each, $1,500 pair | as stated by reviewer (dealer list) |

## Method notes
Klippel Near-field Scanner, >800 points, tweeter axis reference, no grille, 78 °F. Distortion is Klippel-compensated anechoic THD at 96 dB / 1 m; the 100 Hz value is dominated by woofer displacement and motor non-linearity, which Amir recommends filtering below the passband. Compression test refined to 80 Hz in this review; the M105 beat the M106 (110 dB) and M16 (109 dB) on that chart. A side comparison at 106 dB found little difference from the M106 apart from somewhat more low-frequency distortion in the M105.

## Reliability notes
Single sample purchased through the reviewer's Harman dealership (conflict of interest disclosed by him). Impedance and distortion values are read from graphs. The compression chart is marked draft and its criterion is not defined.

## Related
[Revel M105](../speakers/revel-m105.md) · [asr](../reviewers/asr.md) · [Revel](../brands/revel.md) · [spinorama-org](spinorama-org.md)
