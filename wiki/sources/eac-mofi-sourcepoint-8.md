---
type: source
slug: eac-mofi-sourcepoint-8
title: "MoFi SourcePoint 8 Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/mofi_8/
author: Erin (Erin's Audio Corner)
outlet: Erin's Audio Corner
published: 2023-12-20
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-mofi-sourcepoint-8.md
raw_data: raw/spinorama/MoFi SourcePoint 8/eac/
assets: [raw/assets/eac-mofi-sourcepoint-8-impedance.png, raw/assets/eac-mofi-sourcepoint-8-thd86.png, raw/assets/eac-mofi-sourcepoint-8-thd96.png, raw/assets/eac-mofi-sourcepoint-8-compression.png]
speakers: [mofi-sourcepoint-8]
---
# EAC: MoFi SourcePoint 8 review (2023-12-20)

## Summary
Klippel NFS measurement of a manufacturer-loaned pair, grille off. Erin finds it neutral, with no high-frequency lift (unlike the SourcePoint 10) and slightly less bass extension, and says he likes it a lot. Data show smooth, wide directivity, low compression and moderate low-frequency distortion.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 85.9 dB (0°), 85.6 dB (15°) | computed, scripts/cta2034.py v2 from raw Klippel export; claimed 87 dB |
| lw_deviation_db | ±1.3 dB (0° ref) / ±2.0 dB (15° ref) | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±1.9 dB (0°) / ±1.8 dB (15°) | computed |
| f3 / f6 | 52 / 47 Hz (0°); 50 / 46 Hz (15°) | computed |
| hor / ver beamwidth | 122° / 117° (0°); 109° / 116° (15°) | computed |
| di_smoothness | smooth (ERDI residual 0.8 dB) | computed |
| er_dip_1_5khz | 1.4 dB (0°), 1.3 dB (15°) | computed |
| on_minus_lw_4_10k | +0.6 dB (0°), +2.4 dB (15°) | computed |
| SPDI 1 kHz / 10 kHz | 4.6 / 8.4 dB (0°) | computed |
| pref score | 5.15 (no sub) / 7.28 (sub) at 0°; 5.23 / 7.37 at 15° | spinorama.org computation |
| min_impedance_ohm | 8.0 Ω ("above 80 Hz" per plot note); curve saddle ~8 Ω near 55 Hz | graph-read (approx.); maker claims 6.4 Ω min |
| epdr_min_ohm | 4.3 Ω (above 80 Hz) | stated on plot |
| impedance peak | ~76 Ω near 1.8 kHz (crossover region) | graph-read (approx.) |
| thd_86db_pct | ~2.2% worst across 100 Hz-10 kHz (at ~100 Hz); falls below 0.5% by 1 kHz | graph-read (approx.) from dB plot (-33 dB) |
| thd_96db_pct | ~6.5% worst (at ~100 Hz, -23.5 dB); ~2% at 200 Hz, under 0.5% by about 700 Hz-1 kHz; broad rise to ~1.1% near 5.5 kHz (-39 dB) | graph-read (approx.) |
| compression | at most ~0.5 dB above 100 Hz at 102 dB @1 m (referenced to 76 dB); up to ~1.4 dB dip near 53 Hz at 96 dB, ~1.1 dB at 102 dB | graph-read (approx.); port-tuning region |

## Method notes
Klippel Near-Field Scanner, grille off, reference at tweeter (0°) with a second set referenced 15° off-axis. Speaker broken in. Distortion at 86/96 dB at 1 m; compression test: 2.7 s log sweeps at 76/86/96/102 dB; multitone distortion also provided (not read). Pref scores differ slightly by axis (5.15 vs 5.23).

## Reliability notes
Single manufacturer-loaned sample; no payment, maker did not preview. Review text is brief; the video carries the discussion. Erin's text says the sound "is subjectively better than" the SourcePoint 10 (Tier D opinion).

## Related
[[mofi-sourcepoint-8]] · [[erins-audio-corner]] · [[mofi]] · [[spinorama-org]]
