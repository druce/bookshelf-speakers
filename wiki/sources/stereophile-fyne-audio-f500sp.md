---
type: source
slug: stereophile-fyne-audio-f500sp
title: "Fyne Audio F500SP loudspeaker Measurements (Sidebar 3)"
url: https://stereophile.com/content/fyne-audio-f500sp-loudspeaker-measurements
author: John Atkinson
outlet: Stereophile
published: 2022-02-02
fetched: 2026-10-11
tier: B
raw: raw/measurements/stereophile-fyne-audio-f500sp.md
assets: [raw/assets/stereophile-fyne-audio-f500sp-impedance.jpg]
speakers: [fyne-audio-f500sp]
---
# Stereophile: Fyne Audio F500SP measurements (2022-02-02)

## Summary
John Atkinson's quasi-anechoic MLSSA measurements of the F500SP. Sensitivity came out about 3 dB under Fyne's 90 dB claim, impedance never drops below 5 Ω but EPDR falls to 2.3 Ω near 121 Hz, and the coaxial tweeter produces narrow peaks and dips above 5 kHz. The tweeter sits roughly 2 dB above the woofer's midrange level.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 87 dB(B) / 2.83 V / 1 m | reviewer's estimate; claimed 90 dB per [mfr-fyne-audio-f500sp](mfr-fyne-audio-f500sp.md) |
| min_impedance_ohm | 5.0 Ω, 157-203 Hz | stated in text |
| impedance above 6 Ω | "almost all the audioband" | stated in text |
| epdr_min_ohm | 2.32 Ω @ 121 Hz | stated; EPDR below 3 Ω from 111-161 Hz, above 4 Ω through treble |
| port tuning | ~53 Hz | from impedance saddle |
| acoustic crossover | ~1.5 kHz | woofer/tweeter crossing on tweeter axis (maker states 1.7 kHz) |
| tweeter balance | ~+2 dB vs woofer | reviewer wording "a couple of dB higher" |
| tweeter fundamental | 29 kHz | |
| f3 / f6, LW deviation, beamwidth | not stated | graphs only; not entered |
| THD / max SPL | not measured | |

Other findings: tweeter output above 5 kHz disturbed by narrow peaks and dips (suspected reflections off the woofer cone circumference); side-panel resonant modes low in level; spectral decay generally clean apart from three narrow ridges in the mid-to-high treble; tweeter in negative polarity, arrives after the woofer; off-axis behaviour complex where on-axis peaks and dips occur; reviewer suggests experimenting with toe-in.

## Method notes
DRA Labs MLSSA with Earthworks preamp and DPA 4006 mic for farfield (grille off, 50" on tweeter axis, 30 degree horizontal window average); Earthworks QTC-40 for nearfield; impedance via Dayton DATS V2. Response below ~300 Hz is a nearfield splice, so the upper-bass boost is a technique artifact. Gated, so lower confidence below ~300 Hz.

## Reliability notes
Single sample (review loaner). Values are from text; the impedance figure was also saved (raw/assets/stereophile-fyne-audio-f500sp-impedance.jpg) but the text figures were used. No numeric spinorama metrics (f3, LW deviation, beamwidth) are published.

## Related
[Fyne Audio F500SP](../speakers/fyne-audio-f500sp.md) · [stereophile](../reviewers/stereophile.md) · [Fyne Audio](../brands/fyne-audio.md)
