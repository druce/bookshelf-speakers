---
type: source
slug: eac-ps-audio-aspen-fr5
title: "PS Audio Aspen FR5 (Erin's Audio Corner Klippel data via spinorama)"
url: https://www.erinsaudiocorner.com/loudspeakers/ps_audio_aspen_fr5/
author: Erin Fitzgerald
outlet: Erin's Audio Corner
published: 2025-01-14
fetched: 2026-10-11
tier: A
raw: null
raw_data: raw/spinorama/PSAudio aspen FR5/eac-v1-20-degree/
assets: []
speakers: [ps-audio-aspen-fr5]
---
# EAC: PS Audio Aspen FR5 (Klippel data, review page unreachable)

## Summary
Erin's Audio Corner Klippel NFS captures of the FR5 exist in the spinorama.org dataset (two files: `eac-v1-20-degree` and `eac-v1-0-degree`). The review page URL recorded by spinorama (erinsaudiocorner.com/loudspeakers/ps_audio_aspen_fr5/) redirects to the site home page, so no review text, impedance, THD or compression results could be captured. Only values computed from the raw Klippel exports are used here.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 81.3 dB | computed, scripts/cta2034.py v2 (20-degree file; 0-degree file gives 81.6) |
| lw_deviation_db | ±2.7 dB | computed, 300 Hz-10 kHz (both files) |
| on_axis_deviation_db | ±2.6 dB | computed (0-degree file: ±2.7) |
| f3_hz / f6_hz | 51 / 36 Hz | computed (0-degree file: 53 / 37) |
| hor / ver beamwidth | 149 / 95 deg | computed (0-degree file: 145 / 90) |
| di_smoothness | minor-discontinuity | ERDI residual 1.9 dB (0-degree file: major-discontinuity, 2.1 dB) |
| er_dip_1_5khz_db | 3.3 dB | computed (0-degree: 3.2) |
| on_minus_lw_4_10k_db | +0.4 dB | computed (0-degree: +0.7) |
| SPDI 1 kHz / 10 kHz | 4.7 / 7.6 dB | computed (0-degree: 4.9 / 8.3) |
| pref_score | 4.64 (no sub) / 6.26 (with sub) | spinorama.org, 20-degree file; 0-degree file 4.3 / 6.0 |
| spec_impedance (spinorama metadata) | 5.6 Ω | maker minimum, not a measurement |

## Method notes
Klippel NFS export, dB SPL @ 2.83 V / 1 m. The meaning of "20-degree" vs "0-degree" is not documented in the dataset metadata; the 20-degree file is the primary per the packet. The two files agree within 0.3 dB on most metrics (they may be the same sample at different reference orientations or two runs; unknown).

## Reliability notes
Review text was not available, so Erin's own sensitivity, impedance and distortion findings are not captured. SpeakerRanking (aggregator, not ingested) quotes EAC sensitivity near 81.6 dB, consistent with the computed value.

## Related
[PS Audio Aspen FR5](../speakers/ps-audio-aspen-fr5.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [spinorama-org](spinorama-org.md) · [PS Audio](../brands/ps-audio.md)
