---
type: source
slug: asr-focal-dome-flax
title: "Focal Dome Flax Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/focal-dome-flax-speaker-review.47510/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2023-08-30
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-focal-dome-flax.md
raw_data: raw/spinorama/Focal Dome Flax/asr/
assets: [raw/assets/asr-focal-dome-flax-impedance.png, raw/assets/asr-focal-dome-flax-thd.png, raw/assets/asr-focal-dome-flax-thd-rel.png]
speakers: [focal-dome-flax]
---
# ASR: Focal Dome Flax review (2023-08-30)

## Summary
Klippel measurement of a loaned white Dome Flax satellite. Treble is elevated and the response is uneven (listening window ±3.2 dB), bass starts near 126 Hz, the small woofer distorts heavily, and impedance dips to 3.3 Ω. Directivity is wide and smooth. Amir does not recommend it.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.0 dB | computed, scripts/cta2034.py v2; reviewer did not state a figure |
| lw_deviation_db | ±3.2 dB | computed |
| on_axis_deviation_db | ±3.2 dB | computed |
| f3_hz / f6_hz | 126 / 105 Hz | computed (sealed 4" woofer) |
| hor / ver beamwidth | 143 / 119 deg | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.2 dB) | computed |
| er_dip_1_5khz_db | 3.7 dB | computed; exceeds 3 dB flag |
| on_minus_lw_4_10k_db | +0.3 dB | computed |
| spdi 1k / 10k | 2.5 / 5.8 dB | computed |
| pref_score / with sub | 1.8 / 5.5 | spinorama.org, 1.76 / 5.48 |
| min_impedance_ohm | 3.3 Ω | stated on ASR graph; lowest region about 270 Hz (graph-read); peak about 22.5 Ω near 135 Hz |
| THD | at 86 dB: off the 5% scale below about 190 Hz, about 2.3% spike at 340 Hz, about 2.5% at 450 Hz, under 0.5% above about 1.5 kHz; at 90 dB markedly worse (about 3.2% near 450 Hz) | graph-read (approx.); ASR limited testing to 90 dB; plot labelled non-anechoic |
| Subjective | forward treble, ugly buzzy upper bass, enclosure vibrates, lower bass absent | Tier D listening notes |

## Method notes
Klippel NFS, grille on, speaker propped almost vertical so measurements are close to on-axis (it tilts up to 20 degrees); reviewer says off-angle performance is worse. Spinorama data from raw export under `raw/spinorama/Focal Dome Flax/asr/`. ASR notes elevated treble from uncorrected woofer energy above crossover.

## Reliability notes
Single loaned sample from a member; unit's bottom cover did not fully close, which a forum member suggested might add buzz. Distortion plot not valid for a non-flat response, per reviewer.

## Related
[Focal Dome Flax](../speakers/focal-dome-flax.md) · [asr](../reviewers/asr.md) · [spinorama-org](spinorama-org.md) · [Focal](../brands/focal.md)
