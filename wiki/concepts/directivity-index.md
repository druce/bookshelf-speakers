---
type: concept
slug: directivity-index
last_updated: 2026-10-11
---
# Directivity index (DI)

The **directivity index** is how much louder the listening window is than the off-axis energy:
- **SPDI** = LW − [sound-power](sound-power.md)
- **ERDI** = LW − [early-reflections](early-reflections.md)

A typical dome-tweeter bookshelf speaker shows an SPDI of about 3–5 dB at 1 kHz, rising to 8–10 dB at 10 kHz. Waveguides and coaxials keep the DI flatter and more constant through the crossover.

## Metrics used in this wiki
- `di_smoothness` comes from `scripts/cta2034.py`. The ERDI is smoothed to 1/6 octave and fitted with a straight line in log frequency from 500 Hz to 10 kHz, then graded on the maximum absolute residual:
  - < 1.0 dB: **smooth**
  - 1.0–2.0 dB: **minor-discontinuity**
  - > 2.0 dB: **major-discontinuity**
- `spdi_1k_db` and `spdi_10k_db` are recorded in source pages to show how fast directivity rises.
- `hor_beamwidth_deg` and `ver_beamwidth_deg` are full −6 dB angles relative to on-axis, as the median of 1/3-octave points from 1 to 10 kHz. Typical values: 110–130° horizontal for a dome tweeter on a flat baffle, and 70–100° for waveguide or horn designs. Wide dispersion suits a sofa of listeners; narrow dispersion reduces side-wall reflections.

## Toe-in from data
If the on-axis response is brighter than the LW (on-axis rises above about 5 kHz), aim the speakers to cross in front of the listener. If the on-axis is flatter than the ±30° curves, aim them straight at the listener. Speaker pages state which applies.

## Related
[spinorama](spinorama.md) · [early-reflections](early-reflections.md) · [sound-power](sound-power.md) · [preference-score](preference-score.md)
