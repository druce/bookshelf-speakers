---
type: source
slug: asr-fluance-hfs-signature
title: "Fluance Signature Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/fluance-signature-bookshelf-speaker-review.16337/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-09-29
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-fluance-hfs-signature.md
raw_data: raw/spinorama/Fluance HFS Signature/asr/
assets: [raw/assets/asr-fluance-hfs-signature-impedance.png, raw/assets/asr-fluance-hfs-signature-thd.png]
speakers: [fluance-hfs-signature]
---
# ASR: Fluance HFS Signature review (2020-09-29)

## Summary
Klippel NFS measurement of a unit Amir bought on sale for $169. He finds serious midrange flaws in both direct sound and directivity, a recessed region that makes a port resonance more audible, and a woofer-dominated distortion problem. He does not recommend it, calling it close to the bottom rating.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 85.8 dB | computed, scripts/cta2034.py v2 from raw Klippel export; forum reply by MZKM states 86.1 dB |
| lw_deviation_db | ±4.5 dB | computed, 300 Hz-10 kHz (coloured) |
| on_axis_deviation_db | ±5.2 dB | computed |
| f3_hz / f6_hz | 74 / 57 Hz | computed |
| hor / ver beamwidth | 145° / 122° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.8 dB) | computed |
| er_dip_1_5khz_db | 4.1 dB | computed; above 3 dB flag |
| on_minus_lw_4_10k_db | +0.5 dB | computed |
| pref_score / with sub | 2.92 / 5.53 | spinorama.org computation; MZKM in thread posts 3.4 / 5.9 |
| min_impedance_ohm | ~3.7 Ω @ ~140 Hz | graph-read (approx.); curve also ~3.9 Ω near 250 Hz, peak ~16 Ω near 105 Hz |
| thd_96db | ~5% near 100-150 Hz | graph-read (approx.), 96 dB test; ~3% spike near 300 Hz; below ~0.5% above 500 Hz |
| thd_86db | not shown | only 96 dB plot posted |
| Subjective (Tier D) | bright; filtering could not fix it | not recommended |

## Method notes
Klippel NFS, tweeter axis, grille off, 800+ points, 76 F. Near vs far field comparison shows mid-frequency problem slightly smaller at 4 m. Distortion plot is absolute level (dB) at 96 dB fundamental; THD % computed from fundamental-to-THD gap by eye.

## Reliability notes
Single purchased sample. Impedance and THD are graph-read only. Amir warns that spikes in the relative-distortion plot are caused by response dips.

## Related
[Fluance HFS Signature](../speakers/fluance-hfs-signature.md) · [asr](../reviewers/asr.md) · [Fluance](../brands/fluance.md) · [spinorama-org](spinorama-org.md)
