---
type: source
slug: eac-dayton-audio-opal1
title: "Dayton Audio OPAL1 Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/dayton_opal1/
author: Erin Fitzgerald
outlet: Erin's Audio Corner
published: 2024-04-21
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-dayton-audio-opal1.md
raw_data: raw/spinorama/Dayton Audio OPAL1/eac/
assets: [raw/assets/eac-dayton-audio-opal1-impedance.png, raw/assets/eac-dayton-audio-opal1-thd86.png, raw/assets/eac-dayton-audio-opal1-thd96.png, raw/assets/eac-dayton-audio-opal1-compression.png]
speakers: [dayton-audio-opal1]
---
# EAC: Dayton Audio OPAL1 review (2024-04-21)

## Summary
Klippel NFS measurement of a manufacturer-loaned OPAL1 pair. Erin finds a forward, focused sound (bump near 1 kHz, midrange scoop), top end that rolls off quickly off-axis, and very low sensitivity (about 76 dB). Bass extension is good for the size and compression at 102 dB @1 m is mild. The page body is dated 2024-04-21; the dataset metadata lists 2025-01-14.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 75.4 dB | computed, scripts/cta2034.py v2 from raw Klippel export; Erin states 75.7 dB |
| lw_deviation_db | ±2.6 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±3.4 dB | computed |
| f3_hz / f6_hz | 51 / 36 Hz | computed |
| hor / ver beamwidth | 139° / 119° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.9 dB) | computed |
| er_dip_1_5khz_db | 1.1 dB | computed |
| on_minus_lw_4_10k_db | +0.9 dB | computed |
| spdi_1k / spdi_10k | 5.3 / 9.2 dB | computed |
| pref_score / with sub | 5.08 / 6.58 | spinorama.org dataset |
| min_impedance_ohm | 4.5 Ω (above 80 Hz, near 4 kHz) | stated on Erin's impedance plot; frequency graph-read (approx.) |
| epdr_min_ohm | 1.9 Ω (above 80 Hz) | stated on plot |
| thd_86db_pct | ~1.0% (worst, at 100 Hz) | graph-read (approx.): about -40 dB; ~0.5-0.7% from 150 Hz up, ~0.15% near 1-2 kHz |
| thd_96db_pct | ~3.3% (worst, at 100 Hz) | graph-read (approx.): about -29.5 dB; ~1.4% at 200 Hz, ~2% bump near 2.8 kHz |
| compression | 102 dB @1 m: ≤2.8 dB loss (40-100 Hz), about 0.2-1.5 dB above 150 Hz; 96 dB ≤0.6 dB | graph-read (approx.) from linearity plot referenced to 76 dB |
| max_spl note | Manufacturer claims 102 dB at rated power | not measured as max SPL |
| Subjective (Tier D) | forward/focused, midrange scoop, aim at listener | Erin's summary |

## Method notes
Klippel Near-Field Scanner, reference point at tweeter, grille off, broken-in. Compression test: log sweeps at 76/86/96/102 dB @1 m; multitone tests at about 70/79/87/96 dB. Impedance measured at 0.10 V RMS.

## Reliability notes
Single manufacturer-loaned sample; Erin states no compensation. THD/compression values are read from images. Erin quotes both 75.7 dB (summary) and 78.5 dB (manufacturer spec).

## Related
[[dayton-audio-opal1]] · [[erins-audio-corner]] · [[dayton-audio]] · [[spinorama-org]]
