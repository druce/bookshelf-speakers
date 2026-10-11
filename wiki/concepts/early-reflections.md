---
type: concept
slug: early-reflections
last_updated: 2026-10-11
---
# Early reflections (ER)

The **early reflections** curve estimates the sound reaching the listener after one bounce. CTA-2034-A builds it from five groups, energy-averaged:
- **Floor bounce:** −20°, −30°, −40° vertical.
- **Ceiling bounce:** +40°, +50°, +60° vertical.
- **Front wall:** 0°, ±10°, ±20°, ±30° horizontal.
- **Side walls:** ±40° to ±80° horizontal.
- **Rear wall:** ±90° and 180° horizontal.

ER dominates the predicted in-room response together with [[sound-power]]. A smooth ER that follows the LW shape at a gently lower level indicates good off-axis behaviour. A dip near the crossover (typically 1.5–3 kHz) is the classic signature of a woofer beaming before the tweeter takes over.

## Metric used in this wiki: `er_dip_1_5khz_db`
- Computed by `scripts/cta2034.py`: residual of the 1/6-octave ER curve against a straight-line fit in log frequency (300 Hz–10 kHz). The deepest negative residual between 1 and 5 kHz is reported.
- Claude.md §7 flags a dip of more than 3 dB near the crossover.

## Related
[[spinorama]] · [[directivity-index]] · [[listening-window]]
