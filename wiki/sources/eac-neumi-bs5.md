---
type: source
slug: eac-neumi-bs5
title: "Neumi BS5 Bookshelf Speaker Review (Klippel NFS retest)"
url: https://www.erinsaudiocorner.com/loudspeakers/neumi_bs5_nfs/
author: Erin Fast
outlet: Erin's Audio Corner
published: 2021-12-12
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-neumi-bs5.md
raw_data: raw/spinorama/Neumi BS5/ErinsAudioCorner/
assets: [raw/assets/eac-neumi-bs5-impedance.png, raw/assets/eac-neumi-bs5-thd86.png, raw/assets/eac-neumi-bs5-thd96.png, raw/assets/eac-neumi-bs5-compression.png]
speakers: [neumi-bs5]
---
# EAC: Neumi BS5 NFS retest (2021-12-12)

## Summary
Erin re-measured the 6 Ω, front-ported BS5 on his Klippel near-field scanner after an earlier gated-method review ([eac-neumi-bs5-v1](eac-neumi-bs5-v1.md)). He finds a reasonably neutral speaker marred by port-related midrange dips and a 1-2 kHz resonance, adequate bass for the size (F3 68 Hz, F10 40 Hz) and the need for a subwoofer. He still likes it as a starter speaker at about $109 per pair (at review time).

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 82.5 dB | computed, scripts/cta2034.py v2 (ref level 82.7 dB, 300 Hz-10 kHz) |
| lw_deviation_db | ±3.5 dB | computed; ported configuration |
| on_axis_deviation_db | ±3.5 dB | computed |
| f3 / f6 | 68 / 54 Hz | computed; Erin's text: F3 68 Hz, F10 40 Hz |
| hor / ver beamwidth | 145° / 104° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 2.0 dB) | computed |
| er_dip_1_5khz_db | 1.8 dB | computed |
| on_minus_lw_4_10k_db | +0.8 dB | computed |
| SPDI 1 kHz to 10 kHz | 5.4 to 8.0 dB | computed |
| pref_score / with sub | 3.6 / 6.1 | spinorama.org computation, ported |
| Port stuffed (sealed) variant | LW ±2.3 dB, f3 90 Hz, f6 71 Hz, pref 4.6 / 7.7 | computed; Erin's own "SPINORAMA with the ports stuffed" |
| min_impedance_ohm | about 4.1 Ω near 10-20 kHz; about 5.5 Ω near 200 Hz; about 6.3 Ω near 50 Hz | graph-read (approx.), Klippel H(f) magnitude, level not stated; no EPDR plotted |
| thd_86db_pct | about 2.1% | graph-read (approx.): peak near 370 Hz (-33.5 dB); about 0.9% near 2.1 kHz; <0.5% above 4 kHz |
| thd_96db_pct | about 3.2% | graph-read (approx.): peak near 380 Hz (-30 dB); 1.2-1.4% near 100-250 Hz; THD well above 3% below ~80 Hz |
| Compression (vs 76 dB ref) | 96 dB: at most 0.7 dB above 70 Hz; 102 dB: 1.0-1.5 dB 100-200 Hz, up to 2.6 dB near 75 Hz, ~1 dB loss above 12 kHz | graph-read (approx.) |
| crossover | 2.1 kHz stated by Neumi | per Erin's earlier review; nearfield data agrees |

## Method notes
Klippel NFS, reference plane between midwoofer and tweeter, grille off, port open, speaker described as unchanged since the first review (Neumi confirmed). Erin notes mid-band results differ by about 1.5 dB from the older method. Listening done on-axis at 4 m, 80-95 dB.

## Reliability notes
Single sample supplied by the manufacturer. Erin discloses affiliate links. Spinorama.org pref score computed from this export. Erin's text F3 (68 Hz) matches the computed value.

## Related
[Neumi BS5](../speakers/neumi-bs5.md) · [eac-neumi-bs5-v1](eac-neumi-bs5-v1.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [spinorama-org](spinorama-org.md) · [Neumi](../brands/neumi.md)
