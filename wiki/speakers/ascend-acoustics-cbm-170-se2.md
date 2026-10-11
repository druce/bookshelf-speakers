---
type: speaker
brand: Ascend Acoustics
model: CBM-170 SE2
slug: ascend-acoustics-cbm-170-se2
category: bookshelf
status: current
price_usd_pair: 468
price_checked: 2026-10-11
home_trial_days: 30
no_hassle_return: true
trial_seller: "Ascend Acoustics"
trial_terms: "30 days, buyer pays return shipping, no restocking fee"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 3.4
min_impedance_hz: 218
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 86.5
sensitivity_claimed_db: 87.0
f3_hz: 62
f6_hz: 52
lw_deviation_db: 1.8
on_axis_deviation_db: 2.2
hor_beamwidth_deg: 144
ver_beamwidth_deg: 88
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: 1.0
thd_96db_pct: 2.0
pref_score: 5.7
pref_score_sub: 8.0
woofer_in: 6.5
tweeter_type: dome
port: rear
dimensions_mm: 305x229x241
weight_kg: 6.8
critic_consensus: ASR's Amir called it clean, loud and high-fidelity with a very large soundstage and strongly recommended it; only one Tier-D source so far.
user_consensus: null
sources: [asr-ascend-acoustics-cbm-170-se2, mfr-ascend-acoustics-cbm-170-se2, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "Anechoic 64 Hz-22 kHz ±3 dB; -6 dB at 54 Hz (maker, anechoic); typical in-room 43 Hz-20 kHz (no tolerance)"
primary_measurement: asr-ascend-acoustics-cbm-170-se2
measurement_count: 1
image_url: "https://www.ascendacoustics.com/cdn/shop/files/170SE2pair_grande.png?v=1783137801"
---
<!-- photo -->
<img src="https://www.ascendacoustics.com/cdn/shop/files/170SE2pair_grande.png?v=1783137801" alt="Ascend Acoustics CBM-170 SE2" width="360">

*Photo: [ascendacoustics.com](https://www.ascendacoustics.com/products/cbm-170se2-bookshelf-monitor-pair) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The CBM-170SE2 is Ascend's $468 passive 6.5" ported standmount, a Klippel-optimised redesign of an old budget favourite. On ASR's Klippel it has a good listening window (±1.8 dB), very wide horizontal dispersion without a waveguide, 86.5 dB sensitivity and modest bass (f3 62 Hz). The notable caveat is impedance: it measures 3.4 Ω minimum against an 8 Ω rating, so it is flagged `effectively-4ohm`. Suits budget buyers with a stable amplifier who want wide, room-friendly sound and plan a sub for deep bass.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 86.5 dB (average) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | computed (scripts/cta2034.py v2); maker claims 87 dB anechoic, 91 dB in-room ([mfr-ascend-acoustics-cbm-170-se2](../sources/mfr-ascend-acoustics-cbm-170-se2.md)) |
| Listening-window deviation | ±1.8 dB, 300 Hz-10 kHz (good) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | computed |
| On-axis deviation | ±2.2 dB (good) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | computed; resonance near 900-1000 Hz per ASR |
| f3 / f6 | 62 / 52 Hz (modest) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | computed; maker: -6 dB at 54 Hz |
| Min impedance | ~3.4 Ω @ ~218 Hz | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | graph-read cursor label (approx.) |
| THD 86 dB @1 m | ~1.0 % (100 Hz-10 kHz peak) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | graph-read (approx.), near-field non-anechoic |
| THD 96 dB @1 m | ~2.0 % (peak near 290 Hz) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) | A | graph-read (approx.); 3.7 % near 85 Hz |
| Preference score | 5.7 (no sub) / 8.0 (with sub) | [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) via [spinorama-org](../sources/spinorama-org.md) | A | 5.65 / 8.01; forum member computed 5.8 / 8.2 |
| Crossover | not stated | [mfr-ascend-acoustics-cbm-170-se2](../sources/mfr-ascend-acoustics-cbm-170-se2.md) | C | |

## Directivity
Horizontal -6 dB beamwidth about 144°, vertical about 88°. DI has a minor discontinuity (ERDI residual 1.7 dB); SPDI rises from 5.7 dB at 1 kHz to 8.8 dB at 10 kHz as the tweeter beams. Early-reflection dip near 1.5 kHz is 2.0 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.5 dB, so toe-in is not critical; ASR notes the vertical response is best at tweeter height, and a forum poster suggests 10-15° toe-in with axes crossing in front. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No compression or max-SPL test. ASR's power sweep played the 96 dB signal without trouble and heard distortion at the sweep start only at 101 dB (Tier D note). THD at 86 dB is about 1.0 % at 100 Hz and under 0.6 % above 200 Hz; at 96 dB it reaches about 2 % around 290 Hz and 3.7 % near 85 Hz, with serious non-linearity below 50 Hz (graph-read). Fine for small and medium rooms; the low bass is simply rolled off. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 8 Ω but measured minimum about 3.4 Ω near 218 Hz, below 4 Ω, so `effectively-4ohm`. Impedance peaks near 20 Hz and 80 Hz and a broad 12 Ω hump near 1.7 kHz; ASR called the load "about average" for its class. EPDR not computed. Use a stable amplifier rated for 4 Ω; maker suggests 2-65 W minimum depending on distance. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-ascend-acoustics-cbm-170-se2](../sources/asr-ascend-acoustics-cbm-170-se2.md) (ASR, Tier D listening notes): clean at loud levels, no EQ needed, very large spatial image; "easy strong recommendation".

## User reviews
No user reports ingested yet. The ASR thread (page 2) contained comment and EQ discussion but no owner listening reports.

## Conflicts
- Impedance: 8 Ω rated vs ~3.4 Ω measured (ASR); flagged `effectively-4ohm`.
- Sensitivity: 86.5 dB computed vs 87 dB maker anechoic (within 1 dB) vs 91 dB maker in-room (not comparable).
- Bass: maker -6 dB at 54 Hz vs computed f6 52 Hz (consistent).
- Preference score: 5.65 spinorama.org vs 5.8 posted by a forum member; used the computed figure.
- A forum member noted the sample's label reads "acoustic suspension"; another replied it is a labelling slip, and the maker page says rear-ported.

## Related
[Ascend Acoustics](../brands/ascend-acoustics.md) · [Ascend Acoustics Sierra-1 V2](ascend-acoustics-sierra-1-v2.md) · [Ascend Acoustics Sierra-LX](ascend-acoustics-sierra-lx.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md)
