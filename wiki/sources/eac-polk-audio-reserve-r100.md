---
type: source
slug: eac-polk-audio-reserve-r100
title: "Polk R100 Bookshelf Speaker Review"
url: https://www.erinsaudiocorner.com/loudspeakers/polk_r100/
author: Erin Fitzgerald
outlet: Erin's Audio Corner
published: 2021-12-09
fetched: 2026-10-11
tier: A
raw: raw/measurements/eac-polk-audio-reserve-r100.md
raw_data: raw/spinorama/Polk Audio Reserve R100/eac/
assets: [raw/assets/eac-polk-audio-reserve-r100-impedance.png, raw/assets/eac-polk-audio-reserve-r100-thd86.png, raw/assets/eac-polk-audio-reserve-r100-thd96.png, raw/assets/eac-polk-audio-reserve-r100-compression.png]
speakers: [polk-audio-reserve-r100]
---
# EAC: Polk R100 review (2021-12-09)

## Summary
Klippel NFS measurement of a single loaned unit (mono listening only). Erin liked the midbass/midrange punch ("small but good studio monitor") but found treble heavy at higher volumes, heavy low-frequency compression at high level, and an unexplained resonance spanning 500 Hz-1 kHz in the nearfield data. He thinks the crossover could have been better.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 85.1 dB | computed, scripts/cta2034.py v2 from raw Klippel export |
| lw_deviation_db | ±1.0 dB | computed |
| on_axis_deviation_db | ±1.1 dB | computed |
| f3 / f6 | 67 / 56 Hz | computed |
| hor / ver beamwidth | 140° / 117° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 1.1 dB) | computed |
| ER dip 1.5 kHz | 2.3 dB | computed |
| on-axis minus LW 4-10 kHz | +0.8 dB | computed |
| SPDI 1 kHz / 10 kHz | 4.9 / 10.0 dB | computed |
| Preference score | 5.46 (no sub) / 7.93 (with sub) | spinorama data pref calc |
| min_impedance_ohm | ~3.6 Ω @ ~250 Hz | graph-read (approx.); also ~4.2 Ω near 3.3 kHz; peaks ~25 Ω at 38 and 90 Hz |
| thd_86db_pct | ~1.6 % | graph-read (approx.); peaks at ~110 Hz and ~6 kHz (2nd harmonic); ~0.9 % spike near 400 Hz |
| thd_96db_pct | ~8 % at ~110 Hz; ~5 % at ~6 kHz | graph-read (approx.); worst of 100 Hz-10 kHz |
| Compression (instantaneous, ref 76 dB) | 96 dB: about -0.5 dB above 100 Hz, up to -2.5 dB near 55 Hz; 102 dB: about -0.5 to -1.5 dB mid/treble, up to -2.8 dB near 170 Hz | graph-read; Erin: "lots of compression in the LF" at high volume |

## Method notes
Klippel NFS, grille off, reference plane between tweeter and woofer (tweeter axis has a 4 kHz dip). Compression test sweeps at 86/96/102 dB @1 m referenced to 76 dB; long-term 2-minute multitone tests at 86 and 96 dB (graphs only, not read). EPDR not published for this review.

## Reliability notes
Single sample, loaned by owner. Erin subjective notes (Tier D): midbass punch, treble becomes too much at high volume (he attributes it to directivity mismatch between woofer and tweeter; estimated in-room shows ~+3 dB HF rise), use a subwoofer. Maker rates a 3.6 Ω minimum, matching the measurement.

## Related
[Polk Audio Reserve R100](../speakers/polk-audio-reserve-r100.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [Polk Audio](../brands/polk-audio.md) · [spinorama-org](spinorama-org.md)
