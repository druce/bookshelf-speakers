---
type: speaker
brand: Acoustic Energy
model: AE100 Mk2
slug: acoustic-energy-ae100-mk2
status: current
price_usd_pair: 499
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 4.7
min_impedance_hz: 200
impedance_flag: below-iec
epdr_min_ohm: 2.5
sensitivity_db_2v83: 83.6
sensitivity_claimed_db: 87.0
f3_hz: 64
f6_hz: 50
lw_deviation_db: 2.0
on_axis_deviation_db: 2.8
hor_beamwidth_deg: 119
ver_beamwidth_deg: 72
di_smoothness: minor-discontinuity
crossover_hz: 2900
max_spl_db: 102
thd_86db_pct: 1.3
thd_96db_pct: 5.0
pref_score: 5.0
pref_score_sub: 7.2
woofer_in: 5.0
tweeter_type: dome
port: rear
dimensions_mm: 290x165x250
weight_kg: 4.6
critic_consensus: Praised for soundstage, imaging, value and lively sound; caveats are bright lower treble, placement and amplifier sensitivity, and one Klippel-based review finding a hollow midrange.
user_consensus: null
sources: [eac-acoustic-energy-ae100-mk2, stereonet-acoustic-energy-ae100-mk2, ecoustics-acoustic-energy-ae100-mk2, hifireport-acoustic-energy-ae100-mk2, mfr-acoustic-energy-ae100-mk2, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "51 Hz-26 kHz (no tolerance stated)"
primary_measurement: eac-acoustic-energy-ae100-mk2
measurement_count: 1
---

## Summary
The AE100 Mk2 (marketed AE100²) is a 6 Ω, two-way, 5" ported standmount with a 25 mm fabric-dome tweeter on a waveguide, at about $499 per pair. On Erin's Klippel rig it has good, fairly wide directivity but a listening window of ±2.0 dB with a 300-800 Hz dip and a hot tweeter, modest bass (f3 64 Hz) and sensitivity well under the claim. Impedance dips to 4.7 Ω, so it needs a capable amplifier despite the spec. Suits near-wall small-room use with EQ or a warm amplifier; critics are split. US price and stock are lightly evidenced.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.6 dB (low) | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | computed (scripts/cta2034.py v2); claimed 87 dB per [mfr-acoustic-energy-ae100-mk2](../sources/mfr-acoustic-energy-ae100-mk2.md) |
| Listening-window deviation | ±2.0 dB, 300 Hz-10 kHz (good) | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | computed |
| On-axis deviation | ±2.8 dB | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | computed |
| f3 / f6 | 64 / 50 Hz (modest) | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | computed |
| Min impedance | 4.7 Ω above 80 Hz, near ~200 Hz | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | value stated on plot, frequency graph-read |
| EPDR min | 2.5 Ω above 80 Hz | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | stated on plot |
| THD @86 dB | ~1.3% | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | graph-read (approx.); narrow ~2.0% spike near 330 Hz |
| THD @96 dB | ~5.0% | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) | A | graph-read (approx.); peaks near 140 and 330 Hz |
| Preference score | 4.96 (no sub) / 7.18 (with sub) | [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |
| Crossover | 2.9 kHz | [mfr-acoustic-energy-ae100-mk2](../sources/mfr-acoustic-energy-ae100-mk2.md) | C | |

Erin also describes resonances near 300 Hz, 750 Hz and 5 kHz and a tweeter about 3 dB above the midrange.

## Directivity
Horizontal -6 dB beamwidth about 119°, vertical about 72° (narrow vertically, so keep ears near tweeter height). DI has a minor discontinuity (ERDI residual 1.3 dB); SPDI rises from 4.9 dB at 1 kHz to 9.1 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.2 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +1.1 dB, so on-axis is brighter than the window: use little or no toe-in (ecoustics reached the same placement advice). Erin calls the directivity "actually pretty good". See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's tests at 1 m: THD about 1.3% at 86 dB, rising to about 5% at 96 dB in the 140-330 Hz region (all graph-read). Compression at 102 dB stays at about 1.4 dB or less above 100 Hz, but the port region near 50-65 Hz swings from +2.9 to -2.2 dB, so deep notes distort at higher levels. Maker claims 112 dB peak, untested. Fine for small rooms at moderate levels; ecoustics found a 40 W amp ran out of headroom. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal; minimum 4.7 Ω is under the IEC floor of 4.8 Ω, so flagged `below-iec`. Minimum EPDR 2.5 Ω is demanding for a budget speaker; use a stable amp comfortable into 4 Ω. ecoustics found it harder to drive than specs suggest. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [stereonet-acoustic-energy-ae100-mk2](../sources/stereonet-acoustic-energy-ae100-mk2.md) (StereoNET, positive): accurate tonality, good timing and staging; wants 40 W or more.
- [ecoustics-acoustic-energy-ae100-mk2](../sources/ecoustics-acoustic-energy-ae100-mk2.md) (ecoustics, positive with caveats): punchy, precise imaging; bright lower treble, amp- and placement-sensitive.
- [hifireport-acoustic-energy-ae100-mk2](../sources/hifireport-acoustic-energy-ae100-mk2.md) (HiFiReport, very positive): wide stage, warm smooth sound, big gain over Mk1.
- [eac-acoustic-energy-ae100-mk2](../sources/eac-acoustic-energy-ae100-mk2.md) (Erin, Tier D listening): hollow midrange from 300-800 Hz dip and hot tweeter; would pass without EQ.

## User reviews
No user reports ingested yet.

## Conflicts
- Sensitivity: 83.6 dB measured (computed) vs 87 dB claimed (basis unstated); delta about 3.4 dB. Measurement used.
- Critics vs measurements: three listening reviews are positive; Erin's Klippel data and listening are negative on midrange balance. Unresolved; single measured sample.
- Woofer size: 125 mm (maker page) vs 130 mm (maker spec quoted by EAC, ecoustics) vs 105 mm cone measured by StereoNET. Entered 5.0" per maker page.
- Price/status: $499/pair from a 2024 ecoustics Amazon link and a dealer search snippet; Amazon page price not readable, one tool report called it unavailable. Check live stock.

## Related
[Acoustic Energy](../brands/acoustic-energy.md) · [Elac Debut 2.0 B5.2](elac-debut-2-0-b5-2.md) · [Q Acoustics 3030i](q-acoustics-3030i.md) · KEF Q150 · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
