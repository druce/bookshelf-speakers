---
type: speaker
brand: Q Acoustics
model: 3020i
slug: q-acoustics-3020i
status: current
price_usd_pair: 349.96
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 3.9
min_impedance_hz: 250
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 86.1
sensitivity_claimed_db: 88.0
f3_hz: 77
f6_hz: 59
lw_deviation_db: 2.0
on_axis_deviation_db: 2.2
hor_beamwidth_deg: 142
ver_beamwidth_deg: 96
di_smoothness: minor-discontinuity
crossover_hz: 2400
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: 3.3
pref_score: 3.9
pref_score_sub: 6.4
woofer_in: 5.0
tweeter_type: dome
port: rear
dimensions_mm: 278x170x282
weight_kg: 4.8
critic_consensus: Praised by What Hi-Fi? and SoundStage! as a warm, detailed, great-value starter standmount; ASR's Amir found a bright, uneven response with weak woofer distortion performance.
user_consensus: null
sources: [asr-q-acoustics-3020i, nrc-q-acoustics-3020i, mfr-q-acoustics-3020i, whathifi-q-acoustics-3020i, soundstage-q-acoustics-3020i, users-q-acoustics-3020i, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "64 Hz-30 kHz (+3 dB, -6 dB)"
primary_measurement: asr-q-acoustics-3020i
measurement_count: 2
---

## Summary
The 3020i is a 6 Ω, 5" ported two-way standmount with a 22 mm dome tweeter, still sold on Q Acoustics' US site at $349.96 per pair although the 3020c is its newer sibling. On the Klippel it has a good listening-window deviation (±2.0 dB) but a dip around the 2.4 kHz crossover, a 3.5 dB early-reflection dip and a bright top end. Bass is modest (f3 about 77 Hz) and woofer distortion at 96 dB climbs steeply, so it wants a high-pass or a sub for loud listening. It suits small rooms, moderate levels and budget systems.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 86.1 dB (average) | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | computed (scripts/cta2034.py v2) |
| Sensitivity | 85.6 dB | [nrc-q-acoustics-3020i](../sources/nrc-q-acoustics-3020i.md) | A | stated; claimed 88 dB per [mfr-q-acoustics-3020i](../sources/mfr-q-acoustics-3020i.md) |
| Listening-window deviation | ±2.0 dB, 300 Hz-10 kHz (good) | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | computed |
| On-axis deviation | ±2.2 dB (good) | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | computed |
| f3 / f6 | 77 / 59 Hz (needs sub) | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | computed; ASR states ±3.8 dB 64 Hz-20 kHz |
| f3 | ~80 Hz | [nrc-q-acoustics-3020i](../sources/nrc-q-acoustics-3020i.md) | A | graph-read (approx.) |
| Min impedance | 3.9 Ω | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | stated on graph, trough near 250 Hz |
| Min impedance | ~3.5 Ω near 250 Hz | [nrc-q-acoustics-3020i](../sources/nrc-q-acoustics-3020i.md) | A | graph-read (approx.) |
| THD @ 96 dB | ~3.3% near 100 Hz | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) | A | graph-read (approx.); worse below |
| THD+N @ 90 dB | ~3% near 100 Hz, ~1% above 150 Hz | [nrc-q-acoustics-3020i](../sources/nrc-q-acoustics-3020i.md) | A | graph-read (approx.) |
| Preference score | 3.9 (no sub) / 6.4 (with sub) | [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) via [spinorama-org](../sources/spinorama-org.md) | A | 3.86 / 6.38 unrounded; ASR post shows 4.0/6.4 |
| Crossover | 2.4 kHz | [mfr-q-acoustics-3020i](../sources/mfr-q-acoustics-3020i.md) | C | |

## Directivity
Horizontal -6 dB beamwidth about 142°, vertical about 96°. ASR calls horizontal beamwidth narrow and uneven, with woofer and tweeter mismatched at crossover. DI is minor-discontinuity (ERDI residual 1.8 dB); SPDI rises from 5.3 dB at 1 kHz to 8.4 dB at 10 kHz. The early-reflection dip near 1.5 kHz is 3.5 dB, above the 3 dB flag. On-axis minus listening window above 4 kHz is +0.6 dB, so either aim works on the data, though ASR preferred full toe-in (post-EQ). Vertical response is fairly even. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
At 96 dB at 1 m ASR's plot shows woofer distortion above the fundamental below about 45 Hz and roughly 3.3% (graph-read) near 100 Hz; the tweeter is clean. NRC's THD+N at 90 dB is about 3% near 100 Hz and about 1% above 150 Hz. No compression test exists. Amir could play loud without bottoming but advised a high-pass below about 40 Hz. Practical: small rooms and moderate levels. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal. ASR states a 3.9 Ω minimum and NRC about 3.5 Ω (graph-read), so `impedance_flag: effectively-4ohm` (below 4 Ω). EPDR not computed. Maker recommends 25-75 W; use an amplifier stable into 4 Ω. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [whathifi-q-acoustics-3020i](../sources/whathifi-q-acoustics-3020i.md) (What Hi-Fi?): warm, rich, full-bodied bass with refined treble; deep cabinet.
- [soundstage-q-acoustics-3020i](../sources/soundstage-q-acoustics-3020i.md) (SoundStage!, Roger Kanno): natural, open, played louder and lower than expected; compared well with a pricier Axiom M3.
- [asr-q-acoustics-3020i](../sources/asr-q-acoustics-3020i.md) (ASR, Tier D listening): bright on female vocals, not recommended without EQ.

## User reviews
Anecdotal ([users-q-acoustics-3020i](../sources/users-q-acoustics-3020i.md)): 2 listening reports from ASR replies, both mention brightness; no QC problems reported.

## Conflicts
- Sensitivity: claimed 88 dB ([mfr-q-acoustics-3020i](../sources/mfr-q-acoustics-3020i.md)) vs 86.1 dB (ASR) and 85.6 dB (NRC); a 2 dB gap versus the maker; the two Tier A sources agree within 0.5 dB.
- Tonal character: What Hi-Fi? says warm and rich; ASR measures and hears a bright top end. Unresolved.
- Preference score is 3.86 from the spinorama.org computation while ASR's post shows 4.0; both under 0.5 apart.

## Related
[Q Acoustics](../brands/q-acoustics.md) · [Q Acoustics 3030i](q-acoustics-3030i.md) · Q Acoustics 3020c · Q Acoustics 3010i · [Q Acoustics 5020](q-acoustics-5020.md) · [directivity-index](../concepts/directivity-index.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md)
