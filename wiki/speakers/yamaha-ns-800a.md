---
type: speaker
brand: Yamaha
model: NS-800A
slug: yamaha-ns-800a
status: current
price_usd_pair: 5000
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 4.3
min_impedance_hz: null
impedance_flag: below-iec
epdr_min_ohm: 2.1
sensitivity_db_2v83: 84.6
sensitivity_claimed_db: 86.5
f3_hz: 57
f6_hz: 40
lw_deviation_db: 2.2
on_axis_deviation_db: 2.3
hor_beamwidth_deg: 141
ver_beamwidth_deg: 123
di_smoothness: minor-discontinuity
crossover_hz: 2600
max_spl_db: 102
thd_86db_pct: 0.7
thd_96db_pct: 2.2
pref_score: 4.7
pref_score_sub: 6.4
woofer_in: 6.5
tweeter_type: dome
port: rear
dimensions_mm: 419x232x359
weight_kg: 13.0
critic_consensus: Audioholics (4.5/5) praises balanced sound, imaging, bass for a bookshelf and finish; Erin heard bright treble and weak bass away from walls; price is the main caveat.
user_consensus: null
sources: [eac-yamaha-ns-800a, audioholics-yamaha-ns-800a, mfr-yamaha-ns-800a, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "40 Hz-65 kHz (-10 dB), -100 kHz (-30 dB)"
primary_measurement: eac-yamaha-ns-800a
measurement_count: 2
---

## Summary
The Yamaha NS-800A is a 6 Ω, 2-way, 6.5" bass-reflex standmount (1.25" dome) priced around $5,000 per pair list, with discounted listings lower. On Erin's Klippel it measures well: listening window ±2.2 dB, very wide smooth directivity (141° horizontal) and low distortion, but bass extension is modest (f3 57 Hz, 40 Hz at -6 dB) and sensitivity is below the 86.5 dB claim. Impedance dips to about 4.3 Ω with a 2.1 Ω EPDR, so it wants a stable amplifier. Suits listeners wanting a wide-dispersion, beautifully finished speaker who can accept the price; value is the obvious question.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 84.6 dB (average) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | computed (scripts/cta2034.py v2) |
| Sensitivity | 86.2 dB | [audioholics-yamaha-ns-800a](../sources/audioholics-yamaha-ns-800a.md) | B | stated; claimed 86.5 per [mfr-yamaha-ns-800a](../sources/mfr-yamaha-ns-800a.md) |
| Listening-window deviation | ±2.2 dB, 300 Hz-10 kHz (good) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | computed |
| On-axis deviation | ±2.3 dB (good) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | computed |
| f3 / f6 | 57 / 40 Hz (good) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | computed; Audioholics gated data unreliable below ~110 Hz |
| Port tuning | ~40 Hz | [audioholics-yamaha-ns-800a](../sources/audioholics-yamaha-ns-800a.md) | B | ground-plane |
| Min impedance | 4.3 Ω (above 80 Hz) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | stated on plot; maker claims 3.8 Ω |
| EPDR min | 2.1 Ω (above 80 Hz) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | stated on plot |
| THD 86 dB @1 m | ~0.7% (peak at ~100 Hz) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | graph-read (approx.); clean |
| THD 96 dB @1 m | ~2.2% (at ~100 Hz) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | graph-read (approx.) |
| Compression | ≤~1.3 dB at 102 dB @1 m | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) | A | graph-read; sweep referenced to 76 dB |
| Preference score | 4.7 (no sub) / 6.4 (with sub) | [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid |

## Directivity
Horizontal -6 dB beamwidth ~141°, vertical ~123°: very wide. DI smooth with minor discontinuity (ERDI residual 1.4 dB); SPDI rises from 5.5 dB at 1 kHz to 6.8 dB at 10 kHz. Early-reflection dip at 1.5 kHz is 1.5 dB (no flag). On-axis minus listening window above 4 kHz is +0.6 dB, so toe-in is a taste choice. Audioholics saw mild waistbanding at 1-2 kHz and advised keeping ears within ±10° vertically of the tweeter (tweeter spaced far from woofer). See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's THD is low: roughly 0.7% at 86 dB and 2.2% at 96 dB at the 100 Hz worst point (graph-read), under 1% above ~300 Hz at 96 dB. Instantaneous compression stays within about 1.3 dB even at 102 dB @1 m, so max SPL is at least 102 dB (limit not reached in test). Audioholics nonetheless found dynamic range a bit limited for the price. Fine for small-to-medium rooms and moderate-to-loud levels; sub advisable for large rooms. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal. EAC measured 4.3 Ω minimum (maker says 3.8 Ω) and EPDR 2.1 Ω; 4.3 Ω is under the IEC 80% floor of 4.8 Ω, so flagged `below-iec`. Audioholics judged the load benign ("any amplifier should drive it"). Phase swings roughly +65° to -70° (EAC graph, approx.). EPDR near 2 Ω suggests a stable amp rated for 4 Ω. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [audioholics-yamaha-ns-800a](../sources/audioholics-yamaha-ns-800a.md) (Audioholics, 4.5/5): balanced, accurate; impressive bass for size; excellent imaging; pricey and dynamically limited.
- [eac-yamaha-ns-800a](../sources/eac-yamaha-ns-800a.md) (Erin's Audio Corner, Tier D notes): bright treble, weak bass unless near a wall; EQ helps.

## User reviews
No user reports ingested yet. (Audioholics forum comments reportedly praise the finish; page not retrievable.)

## Conflicts
- Sensitivity: 84.6 dB (EAC computed) vs 86.2 dB (Audioholics) vs 86.5 dB claimed; 1.6 dB spread between measurers, claim exceeds Tier-A figure by 1.9 dB.
- Minimum impedance: 4.3 Ω (EAC) vs 3.8 Ω (maker); Audioholics says it stays above 4 Ω below 20 kHz.
- Tonal balance: Audioholics describes balanced sound with good bass; Erin hears bright treble and weak bass; measurements show a high-treble spike (Audioholics) and f3 57 Hz.
- Price: 4,999.90 list pair vs discounted listings (B&H 1,299.95 each, New-Age 1,699.95 each); pair price used is list.

## Related
[Yamaha](../brands/yamaha.md) · [Elac Debut Reference DBR-62](elac-debut-reference-dbr-62.md) · [Revel M16](revel-m16.md) · [KEF LS50 Meta](kef-ls50-meta.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
