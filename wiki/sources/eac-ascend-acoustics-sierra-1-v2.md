---
type: source
slug: eac-ascend-acoustics-sierra-1-v2
title: "Ascend Acoustics Sierra-1 V2 Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/ascend_sierra_1_v2/
author: Erin Fabian
outlet: Erin's Audio Corner
published: 2023-11-24
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-ascend-acoustics-sierra-1-v2.md
raw_data: raw/spinorama/Ascend Acoustics Sierra 1 V2/eac/
assets: [raw/assets/eac-ascend-acoustics-sierra-1-v2-impedance.png, raw/assets/eac-ascend-acoustics-sierra-1-v2-thd86.png, raw/assets/eac-ascend-acoustics-sierra-1-v2-thd96.png, raw/assets/eac-ascend-acoustics-sierra-1-v2-compression.png]
speakers: [ascend-acoustics-sierra-1-v2]
---
# Erin's Audio Corner: Ascend Sierra-1 V2 (2023-11-24)

## Summary
Klippel NFS measurement of a manufacturer-loaned Sierra-1 V2 (about $998/pair). Erin calls it one of the best in-room neutrality results he has measured, with in-room bass to about 40-50 Hz. Impedance is high (7 Ω minimum above 80 Hz) but EPDR dips to 3.5 Ω. Main limit is output: compression and distortion rise above roughly 90 dB at 4 m. Maker saw the data before release.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 81.1 dB | computed, scripts/cta2034.py v2 from raw Klippel export |
| lw_deviation_db | ±1.6 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±2.1 dB | computed |
| f3_hz / f6_hz | 52 / 44 Hz | computed |
| hor / ver beamwidth | 151° / 103° | computed |
| di_smoothness | smooth (ERDI residual 1.0 dB) | computed |
| er_dip_1_5khz_db | 0.8 dB | computed |
| pref_score / with sub | 6.38 / 8.39 | spinorama.org computation |
| min_impedance_ohm | 7.0 Ω (above 80 Hz) | stated on plot; curve minimum ~7 Ω near 200 Hz and at 20 kHz |
| epdr_min_ohm | 3.5 Ω (above 80 Hz) | stated on plot annotation |
| thd_86db_pct | ~1.4 % at 100 Hz | graph-read (approx.) from dB-relative plot (about -37 dB); about 0.7 % at 150 Hz, under 0.4 % above 300 Hz |
| thd_96db_pct | ~5 % at 100 Hz | graph-read (approx.) (about -26 dB); about 1.8 % at 200 Hz, 0.5-0.6 % near 500 Hz-1.5 kHz |
| compression | 96 dB: up to about -0.7 dB above 100 Hz; 102 dB: about -3 dB near 150-170 Hz | graph-read (approx.), referenced to 76 dB at 1 m; 96 dB shows -2.3 dB at 40 Hz |
| max_spl_db | 96 dB @1 m | derived: stays within 3 dB compression at 96 dB; 102 dB exceeds 3 dB near 150 Hz |

## Method notes
Klippel NFS, reference at tweeter, grille off, broken-in. Distortion and compression tests are non-anechoic near-field sweeps. Erin compares it with the Dynaudio Emit 20 (more bass and output) and Revel M16 (bassier, slightly less linear). He hears a mild 1.5 dB shelf around 2-4 kHz and notes beaming above 8 kHz (no waveguide). Tier D opinions are his.

## Reliability notes
Loaner from the maker, who also owns a Klippel NFS and previewed the data; Erin reports no payment. Impedance annotation values are text from the plot; THD and compression are graph-read.

## Related
[Ascend Acoustics Sierra-1 V2](../speakers/ascend-acoustics-sierra-1-v2.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [Ascend Acoustics](../brands/ascend-acoustics.md) · [spinorama-org](spinorama-org.md)
