---
type: speaker
brand: Q Acoustics
model: 5020
slug: q-acoustics-5020
status: current
price_usd_pair: 1199
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 3.4
min_impedance_hz: 250
impedance_flag: effectively-4ohm
epdr_min_ohm: 1.7
sensitivity_db_2v83: 86.7
sensitivity_claimed_db: 87.9
f3_hz: 103
f6_hz: 74
lw_deviation_db: 3.3
on_axis_deviation_db: 3.9
hor_beamwidth_deg: 141
ver_beamwidth_deg: 106
di_smoothness: minor-discontinuity
crossover_hz: 2500
max_spl_db: 102
thd_86db_pct: 0.9
thd_96db_pct: 3.2
pref_score: 3.6
pref_score_sub: 6.6
woofer_in: 5.0
tweeter_type: dome
port: rear
dimensions_mm: 284x180x293
weight_kg: 7.0
critic_consensus: TAS and Trusted Reviews praise a rich, musical, detailed sound; Erin's Audio Corner calls it treble heavy with a crossover that needs refinement.
user_consensus: null
sources: [eac-q-acoustics-5020, mfr-q-acoustics-5020, tas-q-acoustics-5020, trustedreviews-q-acoustics-5020, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "53 Hz-30 kHz (-6 dB)"
primary_measurement: eac-q-acoustics-5020
measurement_count: 1
image_url: "https://www.qacoustics.com/cdn/shop/files/61HvCbxmfhL.jpg?v=1786385327"
---
<!-- photo -->
<img src="https://www.qacoustics.com/cdn/shop/files/61HvCbxmfhL.jpg?v=1786385327" alt="Q Acoustics 5020" width="360">

*Photo: [qacoustics.com](https://www.qacoustics.com/collections/bookshelf-speakers/products/5020-bookshelf-speaker) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The 5020 is a 6 Ω, 5" ported standmount with a 1" sealed dome tweeter, priced at $1,199 per pair on the maker's US site. On Erin's Klippel it is coloured (listening window ±3.3 dB, treble-heavy) with a 3.3 dB early-reflection dip, f3 of 103 Hz and a minimum impedance of 3.4 Ω with EPDR down to 1.7 Ω. Compression is low up to 102 dB above 80 Hz. Reviewers who listened praise its balance and detail, so it measures worse than it is described, and it costs well above the 3020i that Erin found more linear.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 86.7 dB (average) | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | computed (scripts/cta2034.py v2); claimed 87.9 dB per [mfr-q-acoustics-5020](../sources/mfr-q-acoustics-5020.md) |
| Listening-window deviation | ±3.3 dB, 300 Hz-10 kHz (coloured, near the ±3.5 dB line) | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | computed |
| On-axis deviation | ±3.9 dB | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | computed |
| f3 / f6 | 103 / 74 Hz (needs sub) | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | computed; claimed 53 Hz at -6 dB |
| Min impedance | 3.4 Ω above 80 Hz | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | stated on graph |
| Min EPDR | 1.7 Ω above 80 Hz | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | stated on graph |
| THD @ 86 dB | ~0.9% near 100-140 Hz | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | graph-read (approx.), maximum over 100 Hz-10 kHz |
| THD @ 96 dB | ~3.2% near 100-140 Hz | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | graph-read (approx.) |
| Compression | ≤0.7 dB at 102 dB above 100 Hz except ~2.1 dB near 11 kHz | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) | A | graph-read (approx.) |
| Preference score | 3.6 (no sub) / 6.6 (with sub) | [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) via [spinorama-org](../sources/spinorama-org.md) | A | 3.63 / 6.55 |

## Directivity
Horizontal -6 dB beamwidth about 141°, vertical about 106°. DI is minor-discontinuity (ERDI residual 1.7 dB); SPDI rises from 4.6 dB at 1 kHz to 7.7 dB at 10 kHz. The early-reflection dip near 1.5 kHz is 3.3 dB, above the 3 dB flag. On-axis minus listening window above 4 kHz is +0.8 dB, so either aim works; a little toe-in off axis would tame the "treble heavy" tilt Erin describes. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's 86 dB THD peaks at about 0.9% near 100-140 Hz (graph-read), clean per the 1% rule; at 96 dB it reaches about 3.2% there, rising steeply below 65 Hz. Compression stays at or below about 0.7 dB at 102 dB above 100 Hz, with large swings below about 65 Hz (-2.4 to +2.3 dB). max_spl_db 102 is the test ceiling for the band above ~80 Hz, not a measured limit. Fine for small to medium rooms. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal with a 3.4 Ω minimum above 80 Hz and EPDR minimum 1.7 Ω, so flagged `effectively-4ohm`. The EPDR is demanding: use a capable amplifier; the maker's 25-100 W guidance understates the current need. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [tas-q-acoustics-5020](../sources/tas-q-acoustics-5020.md) (The Absolute Sound): flat-sounding balance, great low-level detail, bass rolls off below ~70 Hz.
- [trustedreviews-q-acoustics-5020](../sources/trustedreviews-q-acoustics-5020.md) (Trusted Reviews): rich, warm, powerful, tuneful bass; not the most analytical.
- [eac-q-acoustics-5020](../sources/eac-q-acoustics-5020.md) (Erin, Tier D note): treble heavy; the cheaper 3020i is more linear.

## User reviews
No user reports ingested yet.

## Conflicts
- Tonality: TAS finds the response flat and Trusted Reviews calls it warm; Erin's Klippel data (±3.3 dB, treble heavy) disagrees. Unresolved; different samples and rooms.
- Bass: claimed 53 Hz at -6 dB vs computed f6 74 Hz; TAS also thinks the spec generous.
- Sensitivity: claimed 87.9 dB vs 86.7 dB measured (1.2 dB).

## Related
[Q Acoustics](../brands/q-acoustics.md) · [Q Acoustics 3020i](q-acoustics-3020i.md) · Q Acoustics 5010 · [Q Acoustics 3030i](q-acoustics-3030i.md) · Q Acoustics Concept 30 · [impedance-and-epdr](../concepts/impedance-and-epdr.md)
