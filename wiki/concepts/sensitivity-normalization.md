---
type: concept
slug: sensitivity-normalization
last_updated: 2026-10-11
---
# Sensitivity normalization

All sensitivity in this wiki is **dB SPL at 2.83 V, 1 m**, stored as `sensitivity_db_2v83`.

## Why
2.83 V into 8 Ω is 1 W, but into 6 Ω it is 1.33 W (+1.25 dB) and into 4 Ω it is 2 W (+3 dB). Specs quoted per watt flatter low-impedance speakers less than per-volt specs do. Amplifiers are voltage sources, so dB @ 2.83 V is the comparable figure.

## Conversion
- Spec quoted as dB/1 W/1 m with nominal impedance Z: `dB@2.83V = dB@1W + 10·log10(8/Z)`.
- Use the **measured** impedance at the sensitivity band (roughly 500 Hz–2 kHz) when known; otherwise use the nominal rating and say so.

## Measured method in this wiki
`scripts/cta2034.py` reports the mean LW from 300 Hz to 3 kHz of the Klippel export, which is calibrated to 2.83 V / 1 m. This matches spinorama.org's `computed_sensitivity` within about 0.5 dB. Reviewers use other bands (ASR: 300 Hz–3 kHz on-axis; Erin: 300 Hz–3 kHz LW; Stereophile: B-weighted pink-noise estimate), so their figures are recorded alongside, not substituted.

## Interpretation (Claude.md §7)
< 84 dB low · 84–87 average · 88–90 high · > 90 very high. Every 3 dB lower sensitivity doubles the amplifier power needed for the same level.

## Related
[[impedance-and-epdr]] · [[compression-and-max-spl]]
