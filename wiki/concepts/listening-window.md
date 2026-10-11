---
type: concept
slug: listening-window
last_updated: 2026-10-11
---
# Listening window (LW)

The **listening window** is the energy average of nine measurements: on-axis, ±10° vertical, and ±10°, ±20°, ±30° horizontal. It represents the direct sound reaching listeners spread across a sofa, and is the most important single curve for perceived tonal balance at typical distances.

## Metric used in this wiki: `lw_deviation_db`
- Computed by `scripts/cta2034.py`: LW smoothed to 1/6 octave, then half the peak-to-peak range between 300 Hz and 10 kHz, reported as ±dB.
- Half-range penalises both ripple and overall tilt. A speaker with a deliberate downward tilt scores worse than its ripple alone would suggest; the speaker page notes this when it matters.
- `on_axis_deviation_db` uses the same method on the 0° curve.

## Interpretation (Claude.md §7)
| ±dB (300 Hz–10 kHz) | Rating |
|---|---|
| ≤ 1.5 | Excellent |
| ≤ 2.5 | Good |
| 2.5–3.5 | Fair |
| > 3.5 | Coloured |

Values from other sources (e.g. a reviewer's "±2 dB 200 Hz–15 kHz") use different bands and smoothing and are recorded verbatim, not substituted.

## Related
[spinorama](spinorama.md) · [early-reflections](early-reflections.md) · [preference-score](preference-score.md)
