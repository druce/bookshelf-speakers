---
type: source
slug: asr-nht-c3
title: "NHT C3 Review (3-way speaker)"
url: https://www.audiosciencereview.com/forum/index.php?threads/nht-c3-review-3-way-speaker.20287/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2021-03-04
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-nht-c3.md
raw_data: raw/spinorama/NHT C3/asr/
assets: [raw/assets/asr-nht-c3-impedance.png, raw/assets/asr-nht-c3-thd.png]
speakers: [nht-c3]
---
# ASR: NHT C3 review (2021-03-04)

## Summary
Klippel NFS review of a single sealed C3 bought new by a member (about $391 each on Amazon). Amir found a wavy on-axis response with elevated highs, a dip in the midrange and a broad upper-bass dip, but good directivity and very low distortion at 86 dB. The unit may have had a damaged midrange (dimple); a replacement sample was promised but no re-measure was seen. He recommends it only with EQ.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.1 dB | computed, scripts/cta2034.py v2; reviewer says 82-83 dB in the midrange, 87 dB claim true only for the peaking tweeter |
| lw_deviation_db | 1.8 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | 2.1 dB | computed |
| f3 / f6 | 61 / 52 Hz | computed |
| hor / ver beamwidth | 145 / 111 deg | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.5 dB) | computed |
| er_dip_1_5khz_db | 2.4 dB | computed |
| on_minus_lw_4_10k_db | +0.7 dB | computed |
| pref score | 4.45 / 6.86 (no sub / sub) | spinorama.org |
| min_impedance_ohm | 4.2 ohm @ about 150 Hz | graph title and curve; also peaks about 18 ohm @ 65 Hz and about 19 ohm @ 1 kHz |
| THD 86 dB | about 0.4% or lower above 100 Hz; narrow spike about 0.85% near 4.2 kHz; rises above 4% below 50 Hz | graph-read (approx.) |
| THD 96 dB (plot labelled 94 dB in text) | about 1-1.8% broad 100 Hz-3 kHz with narrow spikes to about 3%; rises past 5% above about 7 kHz | graph-read (approx.); text says "94 dBSPL" while plot title says 96 dB |

## Method notes
Klippel NFS, tweeter reference axis, no grille, 56 F, over 1000 measurements. Speaker is sealed. Reviewer EQ'd highs down and filled the 1-4 kHz and upper-bass dips. Listening notes (Tier D): highs clearly overdone but not obnoxious; dynamics very good; bass a little light; needs more than 50 W.

## Reliability notes
Single sample, possibly damaged midrange; Amir notes measurements elsewhere were much flatter (see [[hometheaterhifi-nht-c3]]). Treat the on-axis wave and dips with caution.

## Related
[[nht-c3]] · [[asr]] · [[nht]] · [[spinorama-org]]
