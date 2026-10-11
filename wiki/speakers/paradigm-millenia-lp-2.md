---
type: speaker
brand: Paradigm
model: Millenia LP 2
slug: paradigm-millenia-lp-2
category: on-wall
wall_voiced: null
status: current
price_usd_pair: 1200
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: null
min_impedance_hz: null
impedance_flag: null
epdr_min_ohm: null
sensitivity_db_2v83: 86.5
sensitivity_claimed_db: 89.0
f3_hz: 151
f6_hz: 127
lw_deviation_db: 3.7
on_axis_deviation_db: null
hor_beamwidth_deg: null
ver_beamwidth_deg: null
di_smoothness: null
crossover_hz: 2600
max_spl_db: null
thd_86db_pct: 2.1
thd_96db_pct: null
pref_score: 1.0
pref_score_sub: 5.1
woofer_in: 4.5
tweeter_type: dome
port: passive-radiator
dimensions_mm: "635x152x44"
weight_kg: 3.0
critic_consensus: HomeTheaterHifi (2015) liked the clear dialog from a 2 in deep speaker with a sub; the only measurement set finds it bright and bass-light.
user_consensus: "Three ASR forum replies (anecdotal): suited to wall mounting, slightly bright, needs EQ."
sources: [mfr-paradigm-millenia-lp-2, asr-paradigm-millenia-lp-2, spinorama-paradigm-millenia-lp-2, hometheaterhifi-paradigm-millenia-lp-2, users-paradigm-millenia-lp-2, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "+/-3 dB 120 Hz-21 kHz on-axis; 75 Hz (DIN)"
primary_measurement: spinorama-paradigm-millenia-lp-2
measurement_count: 2
---

## Summary
A 1.75 in (44 mm) deep, two-way LCR speaker that hangs flat on a wall with its included bracket (or sits on supplied stands); 8 Ω "compatible" per Paradigm, with two 4.5 in drivers, two passive radiators and a 25 mm dome in an MTM layout. The only measurements are a single hobbyist's gated set (Tier B), which show bass-light, strongly tilted-up treble and poor horizontal directivity when used horizontally. It is a niche choice for where depth is the constraint, and it needs a subwoofer and EQ.

## Measurements
All values are free-field (no wall behind the speaker), from a gated 1 m measurement spliced with near-field below roughly 176 Hz.

| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (300 Hz-3 kHz, 2.83 V / 1 m) | 86.5 dB | [spinorama-paradigm-millenia-lp-2](../sources/spinorama-paradigm-millenia-lp-2.md) | B | maker claims 89 dB anechoic ([mfr-paradigm-millenia-lp-2](../sources/mfr-paradigm-millenia-lp-2.md), Tier C); delta -2.5 dB |
| f3 / f6 | 151 Hz / 127 Hz | [spinorama-paradigm-millenia-lp-2](../sources/spinorama-paradigm-millenia-lp-2.md) | B | free-field; wall placement adds boundary gain; bookshelf f3 labels not applied |
| f3 / f6 (graph-read) | about 125 Hz / about 112 Hz | [asr-paradigm-millenia-lp-2](../sources/asr-paradigm-millenia-lp-2.md) | B | graph-read (approx.) against the 300 Hz level |
| LW deviation 300 Hz-10 kHz | about +/-3.7 dB | [asr-paradigm-millenia-lp-2](../sources/asr-paradigm-millenia-lp-2.md) | B | graph-read (approx.); coloured per the +/-3.5 dB standard; mainly an upward tilt of about 7 dB to 10 kHz |
| Frequency deviation 300 Hz-5 kHz | 3.2 dB | [spinorama-paradigm-millenia-lp-2](../sources/spinorama-paradigm-millenia-lp-2.md) | B | spinorama.org's band, not the wiki's |
| Preference score | 1.0 (no sub) / 5.1 (sub) | [spinorama-paradigm-millenia-lp-2](../sources/spinorama-paradigm-millenia-lp-2.md) | B | ASR thread quotes an earlier 0.3 / 4.4; with EQ 2.5 / 6.2 |
| THD at 86.4 dB @ 1 m | about 2.1 % peak (100 Hz-10 kHz) | [asr-paradigm-millenia-lp-2](../sources/asr-paradigm-millenia-lp-2.md) | B | graph-read (approx.); peak at ~120 Hz where output rolls off; 0.2-0.4 % above 3 kHz |

Because this is a wall-intended design measured away from the wall, treat the weak bass as a free-field result; see [on-wall-speakers](../concepts/on-wall-speakers.md). Paradigm does not state wall voicing, so `wall_voiced` is null; HomeTheaterHifi says Paradigm optimized the design to avoid dramatic boundary gain ([hometheaterhifi-paradigm-millenia-lp-2](../sources/hometheaterhifi-paradigm-millenia-lp-2.md)).

## Directivity
Beamwidth and DI were not computed from raw data. The measurer found horizontal directivity poor when mounted as a center (MTM horizontal, so lobing at the 2.6 kHz crossover) and vertical significantly better, and the elevated response at and above the crossover is the main tonal fault ([asr-paradigm-millenia-lp-2](../sources/asr-paradigm-millenia-lp-2.md)). On a wall there is no toe-in advantage; see [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md). Using it vertically as a left/right speaker is the better-behaved orientation.

## Output & distortion
Only an 86 dB distortion run exists: about 2 % at roughly 120 Hz near the roll-off and about 1.6 % near 230 Hz, so low-frequency distortion is not clean; above 3 kHz it is low. No 96 dB or compression test. Paradigm lists 70 W maximum input. Expect modest output for the size and a need to cross over to a sub; see [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Impedance not measured. Maker says "compatible with 8 ohms" and 15-130 W; with no curve, treat as an unverified 8 Ω load. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [hometheaterhifi-paradigm-millenia-lp-2](../sources/hometheaterhifi-paradigm-millenia-lp-2.md) (HomeTheaterHifi, Jim Milton, 2015): described natural, clear dialog and a focused soundstage with a Seismic 110 sub; recommended it for flat-panel setups.
- [asr-paradigm-millenia-lp-2](../sources/asr-paradigm-millenia-lp-2.md) (hobbyist listening, Tier D): almost no bass and bright; EQ helped; preferred a Revel M55XC.

## User reviews
Three forum replies (anecdotal, under 5): wall-mounted use judged acceptable, slightly bright, less refined than ordinary speakers ([users-paradigm-millenia-lp-2](../sources/users-paradigm-millenia-lp-2.md)). No QC reports.

## Conflicts
- Sensitivity: 86.5 dB measured vs 89 dB claimed anechoic (92 dB "room"); the measured value wins.
- Preference score: 1.0 on spinorama.org now vs 0.3 quoted in the thread from an earlier computation; both are within about 1 point and not meaningful for ranking.
- Tone: HomeTheaterHifi heard no tonal problem, the measurer found a bright, bass-light response; they differ in rig (sub, wall placement) and era.
- Dimensions: the maker page lists inch and cm figures that do not match exactly.

## Related
[Paradigm](../brands/paradigm.md) · [on-wall-speakers](../concepts/on-wall-speakers.md) · [directivity-index](../concepts/directivity-index.md) · [early-reflections](../concepts/early-reflections.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [compression-and-max-spl](../concepts/compression-and-max-spl.md) · [preference-score](../concepts/preference-score.md)
