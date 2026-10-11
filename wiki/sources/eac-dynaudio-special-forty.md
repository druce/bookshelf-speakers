---
type: source
slug: eac-dynaudio-special-forty
title: "Dynaudio Special Forty Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/dynaudio_special_forty/
author: Erin Fellows
outlet: Erin's Audio Corner
published: 2023-08-05
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-dynaudio-special-forty.md
raw_data: raw/spinorama/Dynaudio Special Forty/eac/
assets: [raw/assets/eac-dynaudio-special-forty-impedance.png, raw/assets/eac-dynaudio-special-forty-thd86.png, raw/assets/eac-dynaudio-special-forty-thd96.png, raw/assets/eac-dynaudio-special-forty-compression.png]
speakers: [dynaudio-special-forty]
---
# EAC: Dynaudio Special Forty review (2023-08-05; spinorama dataset dated 2023-11-24)

## Summary
Full Klippel NFS CTA-2034 measurement of a loaned pair (grille off, broken in). The speaker is reasonably flat (listening window +/-2.2 dB) with a modest 83 dB sensitivity, f3 about 52 Hz, and a 6 Ω load that dips to 4.9 Ω with a low EPDR minimum of 2.5 Ω. Harmonic distortion shows a visible bump near 500 Hz and about 2% at 96 dB in the low bass/midbass. The page is data-only; Erin's opinions are in a video not captured here.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 83.2 dB | computed, scripts/cta2034.py v2 from raw Klippel export (ref level 83.0 dB) |
| lw_deviation_db | +/-2.2 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | +/-2.2 dB | computed |
| f3_hz / f6_hz | 52 / 44 Hz | computed |
| hor_beamwidth_deg / ver_beamwidth_deg | 146 / 93 | computed, -6 dB |
| di_smoothness | minor-discontinuity (ERDI residual 1.9 dB) | computed |
| er_dip_1_5khz_db | 3.4 dB | computed; above 3 dB flag |
| on_minus_lw_4_10k_db | +0.7 dB | computed |
| spdi 1 kHz / 10 kHz | 5.7 / 8.5 dB | computed |
| pref_score / pref_score_sub | 4.73 / 6.74 | spinorama.org computation |
| min_impedance_ohm | 4.9 Ω (above 80 Hz) | stated on EAC plot; frequency about 180 Hz graph-read (approx.) |
| epdr_min_ohm | 2.5 Ω (above 80 Hz) | stated on EAC plot, minimum near 120 Hz graph-read |
| impedance phase | about -55 deg near 100 Hz, +/-30 deg elsewhere above 150 Hz | graph-read (approx.) |
| thd_86db_pct | about 0.8% worst case 100 Hz-10 kHz | graph-read (approx.): about -42.5 dB near 110-120 Hz; a ~0.9% (-40.5 dB) narrow peak at ~500 Hz |
| thd_96db_pct | about 2.0% | graph-read (approx.): about -34.5 dB near 80-100 Hz; about 1.3% at 500 Hz peak |
| compression | at 102 dB @1 m: about 1.1 dB near 130 Hz, about 1.5 dB at 40 Hz; at 96 dB: 0.5 dB or less above 100 Hz | graph-read (approx.), referenced to 76 dB |
| MSRP | $2,999/pair | stated on page |

## Method notes
Klippel Near-Field Scanner; reference point at the tweeter, grille off, speaker broken in. Distortion and compression use 86/96/102 dB @ 1 m sweeps; multitone data on the page not extracted. The EAC-stated sensitivity differs slightly from the computed figure; computed used.

## Reliability notes
Single loaned sample (Aegis Distribution). Distortion values are read from graphs. The 4.9 Ω and 2.5 Ω minima are stated on the plot text.

## Related
[[dynaudio-special-forty]] · [[erins-audio-corner]] · [[dynaudio]] · [[spinorama-org]]
