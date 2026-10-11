---
type: concept
slug: spinorama
last_updated: 2026-10-11
---
# Spinorama (CTA-2034-A)

A **spinorama** is the standard set of curves defined by ANSI/CTA-2034-A (2015), derived from Floyd Toole and Sean Olive's work at the NRC and Harman. A speaker is measured anechoically (or with a Klippel Near-Field Scanner, which computes an anechoic-equivalent far field) at 70 points: every 10° around the horizontal and vertical orbits. Those points are combined into:

| Curve | Built from | What it predicts |
|---|---|---|
| On-axis | 0° | Direct sound for a listener exactly on axis |
| [listening-window](listening-window.md) (LW) | 0°, ±10° V, ±10/20/30° H (energy average) | Direct sound across a typical listening area |
| [early-reflections](early-reflections.md) (ER) | Floor, ceiling, front-, side- and rear-wall bounce angles | First reflections in a typical room |
| [sound-power](sound-power.md) (SP) | All 70 points, area-weighted | Total energy radiated into the room (reverberant field) |
| [directivity-index](directivity-index.md) (SPDI, ERDI) | LW − SP, LW − ER | How directivity changes with frequency |
| Predicted in-room response (PIR) | 0.12·LW + 0.44·ER + 0.44·SP | Approximate steady-state in-room curve at the seat |

## How this wiki uses it
- Spinoramas from Tier A sources ([asr](../reviewers/asr.md), [erins-audio-corner](../reviewers/erins-audio-corner.md), [audioholics](../reviewers/audioholics.md), [soundstage-nrc](../reviewers/soundstage-nrc.md), Princeton 3D3A) are the primary evidence for frequency response and directivity (see Claude.md §3).
- Where raw Klippel H/V exports are available (spinorama.org repository), metrics are recomputed with `scripts/cta2034.py` so every speaker is measured against the same yardstick. Method: energy averages per CTA-2034-A; 1/6-octave smoothing on a 48-points/octave log grid; reference level = mean LW 300 Hz–10 kHz. Source: [spinorama-org](../sources/spinorama-org.md).
- [preference-score](preference-score.md) values are taken from spinorama.org's computation and not recomputed.

## Caveats
- Klippel NFS results are reliable to ~20 Hz; gated or quasi-anechoic measurements (Tier B) lose resolution below ~200–500 Hz.
- Different samples and rigs disagree by ±0.5–1 dB typically; larger differences are recorded as Conflicts.
- A spinorama says nothing about distortion, compression or max output; see [compression-and-max-spl](compression-and-max-spl.md).

## Related
[listening-window](listening-window.md) · [early-reflections](early-reflections.md) · [sound-power](sound-power.md) · [directivity-index](directivity-index.md) · [preference-score](preference-score.md) · [spinorama-org](../sources/spinorama-org.md)
