---
type: source
slug: eac-polk-audio-xt15
title: "Polk Monitor XT15 Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/polk_xt15/
author: Erin
outlet: Erin's Audio Corner
published: 2022-01-08
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-polk-audio-xt15.md
raw_data: raw/spinorama/Polk Audio XT15/eac/
assets: [raw/assets/eac-polk-audio-xt15-impedance.png, raw/assets/eac-polk-audio-xt15-thd86.png, raw/assets/eac-polk-audio-xt15-thd96.png, raw/assets/eac-polk-audio-xt15-compression.png]
speakers: [polk-audio-xt15]
---
# Erin's Audio Corner: Polk Monitor XT15 (2022-01-08)

## Summary
Klippel NFS data on a purchased sample, part of a series covering the whole Polk Monitor XT lineup. The written page has no subjective evaluation (it defers to the video). Price quoted as about $200/pair at the time.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 84.4 dB | computed, scripts/cta2034.py v2 from raw Klippel export; claimed 86 dB |
| lw_deviation_db | ±1.9 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±2.6 dB | computed |
| f3_hz / f6_hz | 77 / 64 Hz | computed |
| hor / ver beamwidth | 127° / 101° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.4 dB) | computed |
| er_dip_1_5khz_db | 2.1 dB | computed |
| on_minus_lw_4_10k_db | +0.8 dB | computed |
| spdi | 4.3 dB at 1 kHz to 8.8 dB at 10 kHz | computed |
| pref_score / with sub | 4.56 / 7.31 | spinorama.org |
| min_impedance_ohm | ~4.0 Ω @ ~250 Hz | graph-read (approx.); ~4.5 Ω near 60 Hz; peaks ~24 Ω near 35 Hz and ~30 Ω near 100 Hz; phase within about ±45° |
| thd_86db_pct | ~0.5 % | graph-read (approx.), -46 dB at 100-200 Hz; narrow ~0.7 % (-43 dB) spike near 310 Hz; 100 Hz-10 kHz |
| thd_96db_pct | ~2.5 % | graph-read (approx.), about -32 dB at 150-190 Hz; narrow ~3.2 % (-30 dB) spike near 195 Hz |
| compression | at 96 dB: up to ~1.3 dB near 60 Hz; at 102 dB: ~2.4 dB near 70 Hz and 180 Hz, <1 dB above 700 Hz | graph-read; no point reaches 3 dB above 50 Hz |
| max_spl_db | ≥102 dB @1 m | test ceiling, not a failure point |

## Method notes
Klippel NFS, reference point at the tweeter, grille off. Instant compression test: 2.7 s sweep at 76 dB baseline vs 86, 96, 102 dB. Impedance/THD/compression read from plots.

## Reliability notes
Single purchased sample. Manufacturer specs quoted in the review match [mfr-polk-audio-xt15](mfr-polk-audio-xt15.md). No listening notes.

## Related
[Polk Audio Monitor XT15](../speakers/polk-audio-xt15.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [Polk Audio](../brands/polk-audio.md) · [spinorama-org](spinorama-org.md)
