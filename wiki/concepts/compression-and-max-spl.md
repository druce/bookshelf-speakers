---
type: concept
slug: compression-and-max-spl
last_updated: 2026-10-11
---
# Compression and maximum SPL

Small speakers run out of output before their amplifiers do. Two limits apply:
1. **Excursion**: the woofer or port reaches its mechanical or air-velocity limit. This shows as rising low-frequency distortion and port noise, mostly below about 100 Hz.
2. **Thermal compression**: the voice coil heats, resistance rises, and output falls below what the input voltage predicts.

## How reviewers measure it
- **Erin's Audio Corner** sweeps at rising levels (76 → 96/102 dB @ 1 m) and plots compression as deviation from the expected level. Erin also reports max SPL with a 3 dB compression or 10% THD criterion, often split by band.
- **ASR** publishes THD at 86 and 96 dB @ 1 m (since about 2020). Max SPL is not standardised there.
- **Audioholics** runs CEA-2010-style burst tests on some speakers.

## Fields in this wiki
- `max_spl_db`: max SPL @ 1 m before ≥ 3 dB compression or audible distortion. The speaker page must state the method, the band, and whose test it is.
- `thd_86db_pct` and `thd_96db_pct`: THD at 86 or 96 dB SPL @ 1 m, as a typical value over 100 Hz–10 kHz. Values read off a graph are marked "graph-read" in the source page.

## Practical translation
SPL falls about 6 dB per doubling of distance in free field; in typical rooms it falls 3–5 dB. At 3 m, a pair gives roughly 3–5 dB less than 1 m single-speaker figures, offset by pair summation (+3 to +6 dB). For 85 dB peaks at the seat (loud listening), a bookshelf speaker typically needs about 100 dB clean at 1 m.

## Interpretation (Claude.md §7)
THD < 1% above 100 Hz at 86 dB is clean. Note where it rises above 3% at 96 dB.

## Related
[[sensitivity-normalization]] · [[impedance-and-epdr]] · [[bass-extension-vs-room-gain]]
