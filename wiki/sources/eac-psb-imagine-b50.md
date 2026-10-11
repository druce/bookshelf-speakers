---
type: source
slug: eac-psb-imagine-b50
title: "PSB Audio Imagine B50 Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/psb_b50/
author: Erin Fish
outlet: Erin's Audio Corner
published: 2024-03-30
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-psb-imagine-b50.md
raw_data: raw/spinorama/PSB Imagine B50/eac/
assets: [raw/assets/eac-psb-imagine-b50-impedance.png, raw/assets/eac-psb-imagine-b50-thd86.png, raw/assets/eac-psb-imagine-b50-thd96.png, raw/assets/eac-psb-imagine-b50-compression.png]
speakers: [psb-imagine-b50]
---
# Erin's Audio Corner: PSB Imagine B50 review (2024-03-30)

## Summary
Klippel NFS CTA-2034 measurement of a manufacturer-loaned pair. Erin finds roughly +2.4/-3.2 dB linearity with response "bouncing around" in the midrange, a horizontal directivity mismatch near 4 kHz (tweeter wider than the narrowing mid/woofer), reasonable distortion for the size and modest compression at the highest levels. He prefers the larger PSB T65 tower, and suggests listening slightly above the tweeter axis.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.9 dB | computed, scripts/cta2034.py v2 from raw Klippel export (ref level 83.8 dB) |
| lw_deviation_db | ±2.2 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±2.4 dB | computed |
| f3 / f6 | 64 / 50 Hz | computed |
| hor / ver beamwidth | 132° / 93° | computed |
| di_smoothness | major-discontinuity (ERDI residual 2.2 dB) | computed |
| er_dip_1_5khz_db | 1.8 dB | computed |
| on_minus_lw_4_10k_db | +1.1 dB | computed |
| spdi 1 kHz / 10 kHz | 4.8 / 8.8 dB | computed |
| pref_score / with sub | 4.63 / 6.92 | spinorama.org dataset value |
| Response linearity | -3.23 / +2.36 dB | stated by Erin |
| min impedance | 4.1 Ω above 80 Hz (near 200 Hz) | stated on graph annotation; frequency graph-read (approx.) |
| min EPDR | 2.1 Ω above 80 Hz | stated on graph annotation |
| THD @ 86 dB/1 m | about 0.9% worst case 100 Hz-10 kHz (near 100-200 Hz) | graph-read (approx.); Erin: below 3% down to about 50 Hz |
| THD @ 96 dB/1 m | about 3.1% worst case (near 90-100 Hz); about 2.2% at 200-700 Hz | graph-read (approx.) |
| Compression, 102 dB vs 76 dB reference | within about 1.1 dB above 100 Hz; about -1.7 dB near 60 Hz; +2.4 dB enhancement near 48 Hz (port region) | graph-read (approx.) |
| claimed MSRP | about $700/pair at writing | stated by Erin |

## Method notes
Klippel Near-Field Scanner, reference point at the tweeter, grille off, speaker broken in. Instantaneous compression sweeps at 86/96/102 dB referenced to 76 dB at 1 m; multitone distortion at 70/79/87/96 dB. Impedance measured at 0.10 V RMS.

## Reliability notes
Single manufacturer-loaned pair; Erin states no compensation. Subjective notes are Tier D and attributed to him. Price context has since changed (see [mfr-psb-imagine-b50](mfr-psb-imagine-b50.md)).

## Related
[PSB Imagine B50](../speakers/psb-imagine-b50.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [spinorama-org](spinorama-org.md) · [PSB](../brands/psb.md)
