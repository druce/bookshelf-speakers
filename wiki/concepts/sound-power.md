---
type: concept
slug: sound-power
last_updated: 2026-10-11
---
# Sound power (SP)

**Sound power** is the area-weighted energy average of all 70 spinorama points. It represents the total acoustic energy the speaker pumps into the room, which shapes the reverberant field and the perceived "room sound". CTA-2034-A weights each angle by the share of the sphere it represents. 90° points carry the most weight; on-axis and 180° carry the least.

The SP curve of a conventional forward-firing speaker slopes downward as frequency rises, because the speaker becomes more directional. Smoothness of that slope matters more than its steepness. Bumps in SP that are absent from the LW show off-axis resonances or crossover discontinuities.

`scripts/cta2034.py` uses the weights published in the spinorama.org implementation: 0.000604 (0°) rising to 0.019629 (90°), mirrored for 100–180°.

## Related
[spinorama](spinorama.md) · [directivity-index](directivity-index.md) · [early-reflections](early-reflections.md)
