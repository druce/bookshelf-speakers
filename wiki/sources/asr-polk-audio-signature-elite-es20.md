---
type: source
slug: asr-polk-audio-signature-elite-es20
title: "Polk Signature Elite ES20 Review (Bookshelf Speaker)"
url: https://www.audiosciencereview.com/forum/index.php?threads/polk-signature-elite-es20-review-bookshelf-speaker.33834/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2022-05-10
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-polk-audio-signature-elite-es20.md
raw_data: raw/spinorama/Polk Audio Signature Elite ES20/asr/
assets: [raw/assets/asr-polk-audio-signature-elite-es20-impedance.png, raw/assets/asr-polk-audio-signature-elite-es20-thd.png]
speakers: [polk-audio-signature-elite-es20]
---
# ASR: Polk Signature Elite ES20 review (2022-05-10)

## Summary
Klippel NFS measurement of a purchased pair ($349 shipped from Amazon). Amir finds reasonable on-axis response with port/cabinet resonances at 600-1000 Hz that show up in impedance and distortion, a directivity dip near 4 kHz, smooth wide horizontal dispersion and unusually deep bass. He recommends it as-is and "hugely" with EQ (a small filter near 600 Hz and a treble shelf).

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 87.2 dB | computed, scripts/cta2034.py v2 from raw Klippel export; reviewer states none; claimed 86 dB per [[mfr-polk-audio-signature-elite-es20]]; ASR forum reply says 88 dB/1 W is about what he measured |
| lw_deviation_db | ±2.2 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±2.2 dB | computed |
| f3_hz / f6_hz | 53 / 44 Hz | computed; reviewer says F10 is nearly 35 Hz |
| hor / ver beamwidth | 143° / 94° | computed |
| di_smoothness | major-discontinuity (ERDI residual 3.2 dB) | computed; reviewer calls horizontal beamwidth smooth and constant |
| er_dip_1_5khz_db | 2.7 dB | computed |
| pref_score / with sub | 4.49 / 6.44 | spinorama.org; a forum member posts 4.7 / 6.6 with corrected ER/PIR |
| min_impedance_ohm | 3.6 Ω @ ~174 Hz | graph-read (approx.), also annotated "Min imp = 3.6 ohm" by reviewer |
| thd_86db_pct | ~0.7 % | graph-read (approx.); highest above 100 Hz, near 600 Hz; 100 Hz-10 kHz. Below 100 Hz it is ~1.7-2.0 % near 60-80 Hz |
| thd_96db_pct | null | graph-read: about 2.3 % peak near 600 Hz and broad 1-2 % at 200-500 Hz, but >4 % at the 100 Hz band edge, so no defensible single figure |
| Critique | port/cabinet resonance 600-1000 Hz, elevated treble | Tier D/analysis text |

## Method notes
Klippel Near-field Scanner, tweeter axis, grille off, about 17 °C. THD plots are labelled 86 dB and 96 dB. Impedance/THD values read by eye from the downloaded plots.

## Reliability notes
Single sample bought by the reviewer. Impedance and THD are graph-read. Listening notes are Tier D (EQ-assisted).

## Related
[[polk-audio-signature-elite-es20]] · [[asr]] · [[polk-audio]] · [[spinorama-org]]
