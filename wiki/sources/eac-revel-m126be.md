---
type: source
slug: eac-revel-m126be
title: "Revel M126Be Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/revel_m126be/
author: Erin Sandler
outlet: Erin's Audio Corner
published: 2023-06-23
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-revel-m126be.md
raw_data: raw/spinorama/Revel M126Be/eac/
assets: [raw/assets/eac-revel-m126be-impedance.png, raw/assets/eac-revel-m126be-thd86.png, raw/assets/eac-revel-m126be-thd96.png, raw/assets/eac-revel-m126be-compression.png]
speakers: [revel-m126be]
---
# EAC: Revel M126Be review (page dated 2023-06-23)

## Summary
Klippel NFS measurement of a loaned pair, ported (sealed spin also supplied). Erin finds a neutral, wide-radiating speaker with good on-axis and listening-window linearity, minor diffraction ripples near 3 and 7 kHz, and a vertical dip near the 1.7 kHz crossover. Bass is neutral but not deep. Minimum impedance 4.9 Ω and minimum EPDR 3 Ω above 80 Hz. The raw file header shows 2023-12-19 (spinorama.org upload date); the page body is dated Jun 23, 2023.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 85.7 dB | computed, scripts/cta2034.py v2 from raw Klippel export (ref level 85.5 dB) |
| lw_deviation_db | ±1.1 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±1.8 dB | computed |
| f3_hz / f6_hz | 93 / 50 Hz | computed; f3 likely inflated by the deliberate extended bass shelf (reads -3 dB re the midband only near 93 Hz, then flat to ~50 Hz) |
| hor / ver beamwidth | 129° / 109° | computed (-6 dB, typical 1-10 kHz); Erin's text says "60 to 70 degrees wide" (per side) |
| di_smoothness | minor-discontinuity (ERDI residual 1.1 dB) | computed |
| er_dip_1_5khz_db | 1.3 dB | computed |
| on_minus_lw_4_10k_db | +0.6 dB | computed |
| spdi 1 kHz / 10 kHz | 5.5 / 8.1 dB | computed |
| pref_score / with sub | 5.08 / 7.34 | spinorama.org computation for this data |
| min_impedance_ohm | 4.9 Ω above 80 Hz (curve minimum near 170-200 Hz) | stated on the graph legend; frequency graph-read (approx.) |
| epdr_min_ohm | 3.0 Ω above 80 Hz | stated on graph legend |
| impedance phase | about +40° to -40° over 40-200 Hz; peaks 22 Ω near 95 Hz | graph-read (approx.) |
| thd_86db | about 1.7% at 100 Hz (-35.5 dB), falling to about 0.1% by 1 kHz; narrow 0.4% spike near 300 Hz | graph-read (approx.); 1.8 kHz bump about 0.45% |
| thd_96db | about 4.2% at 100 Hz (-27.5 dB), about 0.5-0.6% near 300 Hz and 1.8-2 kHz | graph-read (approx.); rises further below 100 Hz (about 5% near 80 Hz) |
| compression (86/96/102 dB re 76 dB) | within about ±0.8 dB above 100 Hz; enhancement of 0.7/1.4/1.7 dB near 1.7 kHz; at 102 dB up to +2.1 dB near 53 Hz and -1.9 dB near 46 Hz | graph-read (approx.); no ≥3 dB compression at any tested level |
| crossover | 1.7 kHz | Erin text (compression distortion peaks here) |

## Method notes
Klippel NFS, reference point at tweeter, grille off, speaker broken in. Ported is the main configuration; sealed spin included separately. Harmonic distortion at 86 and 96 dB @ 1 m, instantaneous compression sweeps referenced to 76 dB, and multitone distortion at 70/79/87/96 dB (full band and 80 Hz-20 kHz); Erin states multitone distortion stayed under 3%. Distortion and compression graphs were read visually.

## Reliability notes
Single loaned sample (The Screening Room, Colorado Springs), no compensation disclosed. Percentages are graph-read and approximate. Erin attributes possible upper-mid glare to compression-driven distortion near 1.7 kHz.

## Related
[[revel-m126be]] · [[erins-audio-corner]] · [[revel]] · [[spinorama-org]]
