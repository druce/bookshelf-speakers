---
type: concept
slug: impedance-and-epdr
last_updated: 2026-10-11
---
# Impedance and EPDR

## Nominal vs measured
The **nominal impedance** is a manufacturer's rating. IEC 60268-5 says the minimum of the modulus must not fall below 80% of nominal: 6.4 Ω for 8 Ω, 4.8 Ω for 6 Ω. Many "8 Ω" speakers dip well below that. This wiki records the measured minimum (`min_impedance_ohm`, `min_impedance_hz`) and sets `impedance_flag`:
- `below-iec`: minimum < 80% of rated nominal
- `effectively-4ohm`: minimum < 4.0 Ω

## Phase and EPDR
A load with large phase angle draws more current than its modulus suggests. **EPDR** (equivalent peak dissipation resistance, Keith Howard, *Hi-Fi News* 2006) folds phase into one resistance that would produce the same peak dissipation in a class-B output stage. EPDR is often far below the modulus minimum, e.g. a 4 Ω dip at −45° gives an EPDR near 1.7 Ω. ASR and Stereophile publish EPDR curves for some speakers. Record `epdr_min_ohm` and the frequency where it occurs. Low EPDR in the bass (20–200 Hz), where music carries the most energy, matters most.

## Amplifier guidance used on speaker pages
- Minimum ≥ 5 Ω and EPDR ≥ 3 Ω: any competent amplifier or receiver.
- Minimum 3.5–5 Ω: most separates are fine; budget AV receivers should not be set to the 8 Ω-only mode at high volume.
- Minimum < 3.5 Ω or EPDR < 2 Ω in the bass: choose an amplifier rated into 4 Ω (ideally 2 Ω) with sufficient current.

## Related
[sensitivity-normalization](sensitivity-normalization.md) · [compression-and-max-spl](compression-and-max-spl.md)
