---
type: source
slug: eac-svs-prime-bookshelf
title: "SVS Prime Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/svs_prime_bookshelf/
author: Erin Fortin
outlet: Erin's Audio Corner
published: 2022-11-16
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-svs-prime-bookshelf.md
raw_data: raw/spinorama/SVS Prime Bookshelf/eac/
assets: [raw/assets/eac-svs-prime-bookshelf-impedance.png, raw/assets/eac-svs-prime-bookshelf-thd86.png, raw/assets/eac-svs-prime-bookshelf-thd96.png, raw/assets/eac-svs-prime-bookshelf-compression.png]
speakers: [svs-prime-bookshelf]
---
# EAC: SVS Prime Bookshelf review (2022-11-16)

## Summary
Klippel NFS measurement of a loaned pair. Erin found the midrange forward and the treble bright on-axis (aiming out about 30 degrees helps highs; a 3 dB cut at 1-2 kHz fixes the forwardness), with a diffraction dip at 3-5 kHz horizontally and larger vertical directivity problems from the driver spacing. Output and distortion are reasonable for the size and the build is good. Impedance dips to 3.9 ohm.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 86.6 dB | computed, scripts/cta2034.py v2 from raw Klippel export; maker 87 dB |
| lw_deviation_db | +/-2.3 dB | computed (300 Hz-10 kHz) |
| on_axis_deviation_db | +/-2.6 dB | computed |
| f3 / f6 | 70 / 58 Hz | computed |
| hor / ver beamwidth | 144 / 115 deg | computed (-6 dB, 1-10 kHz) |
| di_smoothness | minor-discontinuity | ERDI residual 1.7 dB, computed |
| er_dip_1_5khz_db | 0.9 dB | computed |
| on_minus_lw_4_10k_db | +0.3 dB | computed |
| SPDI 1 kHz / 10 kHz | 5.6 / 7.8 dB | computed |
| pref_score / with sub | 5.17 / 7.78 | spinorama.org style, from packet |
| min_impedance_ohm | 3.9 ohm (above 80 Hz), near 200 Hz | stated on graph annotation; frequency graph-read (approx.); 4.2 ohm near 52 Hz |
| epdr_min_ohm | 2.2 ohm (above 80 Hz) | stated on graph annotation; near 120 Hz graph-read |
| thd_86db_pct | about 0.7% max, 100 Hz-10 kHz | graph-read (approx.); peak -43 dB near 1.3 kHz |
| thd_96db_pct | about 1.3% max, excluding spike; 2.5% narrow peak near 250 Hz | graph-read (approx.); about -38 dB broad, -32 dB at 250 Hz |
| compression | 102 dB @ 1 m: up to about 1.7 dB loss near 60 Hz, about 1 dB or less elsewhere above 100 Hz | graph-read; 96 dB: up to about 1.1 dB near 57 Hz |
| port | rear (1.7 in, per maker) | |

## Method notes
Klippel Near-Field Scanner, reference at the tweeter, grille off; THD at 86/96 dB at 1 m; instantaneous compression test referenced to 76 dB with 86/96/102 dB sweeps; multitone distortion also provided (not read). Price quoted then as about $600-700 per pair.

## Reliability notes
Single loaner sample from SVS; manufacturer did not preview the review. Distortion and compression numbers are graph-read.

## Related
[SVS Prime Bookshelf](../speakers/svs-prime-bookshelf.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [SVS](../brands/svs.md) · [spinorama-org](spinorama-org.md)
