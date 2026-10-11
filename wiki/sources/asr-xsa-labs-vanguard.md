---
type: source
slug: asr-xsa-labs-vanguard
title: "XSA Labs Vanguard Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/xsa-labs-vanguard-speaker-review.46629/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2023-07-23
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-xsa-labs-vanguard.md
raw_data: raw/spinorama/XSA Labs Vanguard/asr/
assets: [raw/assets/asr-xsa-labs-vanguard-impedance.png, raw/assets/asr-xsa-labs-vanguard-thd.png]
speakers: [xsa-labs-vanguard]
---
# ASR: XSA Labs Vanguard review (2023-07-23)

## Summary
Klippel NFS review of a loaned US$999 sealed 2-way. Amir found a broad 700 Hz-3 kHz hill, notches, very low sensitivity and little bass, traced it to a wide tweeter/woofer overlap, and could not recommend it. Directivity is decent because the drivers are similar in size, so EQ helps a lot.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 81.8 dB | computed, scripts/cta2034.py v2 from raw Klippel export; reviewer says "80 dB or even lower" at places |
| lw_deviation_db | ±4.2 dB | computed |
| on_axis_deviation_db | ±4.8 dB | computed |
| f3 / f6 | 77 / 59 Hz | computed |
| hor / ver beamwidth | 116 / 117 deg | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.3 dB) | computed |
| er_dip_1_5khz_db | 2.5 dB | computed |
| on_minus_lw_4_10k | +0.9 dB | computed |
| SPDI 1 kHz / 10 kHz | 5.2 / 8.8 dB | computed |
| pref_score / with sub | 2.73 / 5.48 | spinorama.org |
| min_impedance_ohm | 8.5 Ω @ ~160 Hz | graph-read (approx.); ASR plot label "Low impedance = 8.5 ohm"; peak ~26 Ω @ ~75 Hz |
| thd_86db_pct | ~1.8% (100-200 Hz region) | graph-read (approx.); ~1.4% near 1.7 kHz |
| thd_96db_pct | ~7% at ~100 Hz, ~5% at 200 Hz, ~2.8% near 2 kHz | graph-read (approx.) |
| crossover | not stated by ASR | designer says woofer runs to ~5.5 kHz (see [stereotimes-xsa-labs-vanguard](stereotimes-xsa-labs-vanguard.md)) |

## Method notes
Klippel NFS, no grille, sealed cabinet (no port). Distortion plots are in dB relative to fundamental at 86 and 96 dB SPL @1 m, converted to % by reading fundamental and THD curves. EQ experiments (Tier D listening): Amir needed lower-treble cut and bass lift to reach acceptable balance; distortion audible only as ticking when pushed hard; one speaker was "plenty loud".

## Reliability notes
Single loaned sample (from a member), bamboo finish. A forum member recalled a designer comment about woofer unit-to-unit variation; unverified. The designer's own foam-core prototype measurement shown by the company differs from production.

## Related
[XSA Labs Vanguard](../speakers/xsa-labs-vanguard.md) · [asr](../reviewers/asr.md) · [spinorama-org](spinorama-org.md) · [XSA Labs](../brands/xsa-labs.md)
