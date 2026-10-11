---
type: source
slug: asr-role-audio-skiff
title: "Role Audio Skiff Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/role-audio-skiff-speaker-review.47981/
author: amirm
outlet: Audio Science Review
published: 2023-09-18
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-role-audio-skiff.md
raw_data: raw/spinorama/Role Audio Skiff/asr/
assets: [raw/assets/asr-role-audio-skiff-impedance.png, raw/assets/asr-role-audio-skiff-thd.png]
speakers: [role-audio-skiff]
---
# ASR: Role Audio Skiff review (2023-09-18)

## Summary
Klippel NFS measurement of a loaned single-driver 3.5" micro speaker. Amir found at least four pronounced driver resonances, odd directivity behaviour, very low sensitivity, no bass high-pass (flat to DC) and distortion that set in before 86 dB SPL. EQ with many filters helped but he could not recommend the speaker.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 80.6 dB | computed, scripts/cta2034.py v2 from raw Klippel export; a forum member computed 81.1 dB (300 Hz-3 kHz); maker claims 88 dB/W/m |
| lw_deviation_db | ±3.9 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±5.0 dB | computed |
| f3_hz / f6_hz | 143 / 126 Hz | computed |
| hor / ver beamwidth | 129° / 128° | computed; Amir calls beamwidth "highly variable" |
| di_smoothness | minor-discontinuity (ERDI residual 1.6 dB) | computed |
| er_dip_1_5khz_db | 1.7 dB | computed |
| on_minus_lw_4_10k_db | +0.7 dB | computed |
| spdi 1 kHz / 10 kHz | 2.5 / 10.5 dB | computed |
| pref_score / with sub | -0.47 / 3.61 | spinorama.org computation; forum members posted -1.1 / 3.0 |
| min_impedance_ohm | 7.7 Ω | stated on the ASR graph; band minimum near 350 Hz, curve about 7.2 Ω below 50 Hz (graph-read, approx.); impedance peak about 38 Ω near 180 Hz (sealed-box resonance) |
| impedance phase | roughly -40° to +45° | graph-read (approx.) |
| thd at 80 / 83 dB | not at 86/96 dB; at 80 dB about 3.4% near 220 Hz peak, 0.3-0.8% from 300 Hz-3 kHz, up to about 2.2% near 4.5 kHz; at 83 dB up to about 2.9% near 4.5 kHz; off the 5% scale below about 200 Hz | graph-read (approx.); thd_86/96 left null because the test could not reach 86 dB |
| max SPL | speaker "started to make odd sounds and compress" before 86 dB SPL at 1 m | reviewer text; no number beyond that |
| Critique | four strong resonances, a directivity error where a crossover would normally be; first impression "screechy"; with EQ about 40% of tracks listenable; anything with bass upsets it | Tier D |

## Method notes
Klippel NFS, grille not removable. Reviewer notes the response is flat to DC, so no high-pass protects the small woofer. Maker spec as quoted by ASR: 8 Ω nominal (min 6.5 Ω), 88 dB/1 W/m, 125 Hz-20 kHz (-6 dB), 6x4x5 in, 3.5 lb each.

## Reliability notes
Single loaned sample. Impedance minimum is the reviewer's graph label. Distortion tested at lower levels than usual, so not directly comparable to 86/96 dB THD for other speakers.

## Related
[[role-audio-skiff]] · [[asr]] · [[role-audio]] · [[spinorama-org]]
