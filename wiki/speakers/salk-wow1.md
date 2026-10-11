---
type: speaker
brand: Salk
model: WoW1
slug: salk-wow1
category: bookshelf
status: current
price_usd_pair: 2595
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.3
min_impedance_hz: 5000
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 78.2
sensitivity_claimed_db: 82.0
f3_hz: 54
f6_hz: 46
lw_deviation_db: 3.1
on_axis_deviation_db: 3.3
hor_beamwidth_deg: 154
ver_beamwidth_deg: 116
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: 2.2
thd_96db_pct: null
pref_score: 4.4
pref_score_sub: 6.6
woofer_in: 4.7
tweeter_type: dome
port: front
dimensions_mm: 273x178x229
weight_kg: null
critic_consensus: null
user_consensus: null
sources: [asr-salk-wow1, mfr-salk-wow1, users-salk-wow1, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "48 Hz-20 kHz ±3 dB"
primary_measurement: asr-salk-wow1
measurement_count: 1
---

## Summary
The Salk WoW1 is a small hand-built, front-ported two-way mini-monitor (Hiquphon 3/4" dome, Seas Excel W12 12 cm magnesium woofer), rated 8 Ω and sold direct at $2,595 per pair. ASR's Klippel test found a listening window of ±3.1 dB, a pronounced 500-700 Hz dip attributed to the port, very low sensitivity (78.2 dB) and heavy bass distortion, and did not recommend it without EQ. Impedance is high in the bass but graph-read near 3.3 Ω in the treble. Suits near-field or small-room use with strong amplification and a subwoofer; the measured sample may have been unrepresentative (unconfirmed).

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 78.2 dB (low) | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | computed (scripts/cta2034.py v2); claimed 82 dB per [mfr-salk-wow1](../sources/mfr-salk-wow1.md) |
| Listening-window deviation | ±3.1 dB, 300 Hz-10 kHz (coloured edge, between good and coloured) | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | computed |
| On-axis deviation | ±3.3 dB | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | computed |
| f3 / f6 | 54 / 46 Hz | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | computed; port response drops in 500-700 Hz region, see Directivity |
| Min impedance | ~3.3 Ω near 4-5 kHz | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | graph-read (approx.); graph label says 6.5 Ω "in bass" |
| THD 86 dB | ~2.2% near 100 Hz | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | graph-read; off-scale below ~90 Hz |
| THD 96 dB | >5% below ~140 Hz; 1-1.5% above | [asr-salk-wow1](../sources/asr-salk-wow1.md) | A | graph-read; null in frontmatter |
| Preference score | 4.4 (no sub) / 6.6 (sub) | [asr-salk-wow1](../sources/asr-salk-wow1.md) via [spinorama-org](../sources/spinorama-org.md) | A | ignores distortion and max output |

## Directivity
Horizontal -6 dB beamwidth about 154°, vertical about 116°, but ASR says the width is uneven. DI shows a minor discontinuity (ERDI residual 2.0 dB); SPDI rises from 5.1 dB at 1 kHz to 6.3 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 1.8 dB, under the 3 dB flag. ASR notes the woofer becoming directional while the tweeter is not at the crossover, adding to the 500-700 Hz dip. On-axis minus listening window above 4 kHz is +0.3 dB, so either aim works. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Distortion is high in the bass: THD about 2.2% near 100 Hz at 86 dB and off the 5% scale below about 90 Hz; at 96 dB it is off-scale below about 140 Hz with the tweeter rising to about 1.5% above 5 kHz. ASR heard "brrr" distortion in the bass and recommends a 40 Hz high-pass; SPL limiting is gradual. Max SPL was not measured. With 78 dB sensitivity and a 4.7" woofer, expect limited output: near-field or small rooms only. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Maker says 8 Ω nominal. Impedance peaks about 22-27 Ω in bass and mids, but the graph-read minimum is about 3.3 Ω around 4-5 kHz, so flagged `effectively-4ohm` (the ASR graph label instead says 6.5 Ω in bass). EPDR was not reported. Low sensitivity means power demand is high (maker suggests 100 W); use a strong amplifier stable into 4 Ω. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
No professional (Tier D) review found. ASR's listening notes ([asr-salk-wow1](../sources/asr-salk-wow1.md), Tier D): bass muted and muffled without EQ, better with vocals and strings; could not recommend; with a 40 Hz high-pass and a dip fix it became "rather enjoyable".

## User reviews
About 2 owner remarks, so anecdotal ([users-salk-wow1](../sources/users-salk-wow1.md)): one owner's near-field measurements show the same lower-midrange sag and notes the low sensitivity; the rest is reaction to the ASR measurements. Several members speculate the tested sample was defective (unconfirmed); Salk's service reputation is praised by 3 members (secondhand). No confirmed QC issues.

## Conflicts
- Sensitivity: 78.2 dB measured (ASR) vs 82 dB claimed (unit not stated by maker); about 4 dB lower than claimed.
- Bass extension: f3 54 Hz computed vs maker -3 dB at 48 Hz (±3 dB tolerance); a speaker designer on ASR puts the real figure near 60 Hz.
- Impedance: ASR graph label "6.5 Ω in bass" vs the graph-read band minimum near 3.3 Ω; treat as a graph-read.
- Single sample: ASR tested one custom-finished unit that members suspected was defective; the second pair was not measured.
- Price: $2,595/pair at Salk (2026) vs $1,295 quoted in 2020; status not stated as in-stock (built to order).
- Weight (23 lb) not specified as each or per pair; left null.

## Related
[Salk](../brands/salk.md) · [Revel M105](revel-m105.md) · [Revel M16](revel-m16.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md) · [sensitivity-normalization](../concepts/sensitivity-normalization.md)
