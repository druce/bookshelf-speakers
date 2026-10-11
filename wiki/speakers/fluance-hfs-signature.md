---
type: speaker
brand: Fluance
model: HFS Signature
slug: fluance-hfs-signature
status: current
price_usd_pair: 199.99
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.7
min_impedance_hz: 140
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 85.8
sensitivity_claimed_db: 85.0
f3_hz: 74
f6_hz: 57
lw_deviation_db: 4.5
on_axis_deviation_db: 5.2
hor_beamwidth_deg: 145
ver_beamwidth_deg: 122
di_smoothness: minor-discontinuity
crossover_hz: 2300
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: 5.0
pref_score: 2.9
pref_score_sub: 5.5
woofer_in: 5
tweeter_type: dome
port: front
dimensions_mm: 325x200x209
weight_kg: 4.4
critic_consensus: HomeTheaterHiFi liked it for the price; ASR found it coloured and bright and does not recommend it.
user_consensus: Mixed and anecdotal (4 reports, 2 positive, 2 negative).
sources: [asr-fluance-hfs-signature, hometheaterhifi-fluance-hfs-signature, users-fluance-hfs-signature, mfr-fluance-hfs-signature, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "60 Hz - 20 kHz (no tolerance)"
primary_measurement: asr-fluance-hfs-signature
measurement_count: 1
---

## Summary
The Fluance Signature HFS is a $200-per-pair, 5" two-way with a 1" silk dome and dual front ports, rated "8 ohm compatible". On ASR's Klippel it measures poorly: listening window ±4.5 dB, a midrange hole with a port resonance, early-reflection dip above 3 dB, and bass only to 74 Hz (f3). Impedance falls to about 3.7 Ω, so it behaves as a 4 Ω speaker. It suits only a tight budget with a sub and EQ; better-measuring options exist at similar prices.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 85.8 dB (average) | [[asr-fluance-hfs-signature]] | A | computed (scripts/cta2034.py v2); thread reply states 86.1 dB |
| Listening-window deviation | ±4.5 dB (coloured) | [[asr-fluance-hfs-signature]] | A | computed |
| On-axis deviation | ±5.2 dB | [[asr-fluance-hfs-signature]] | A | computed |
| f3 / f6 | 74 / 57 Hz (needs a sub) | [[asr-fluance-hfs-signature]] | A | computed |
| Preference score | 2.9 (no sub) / 5.5 (with sub) | [[asr-fluance-hfs-signature]] via [[spinorama-org]] | A | thread poster computed 3.4 / 5.9 |
| Min impedance | ~3.7 Ω @ ~140 Hz | [[asr-fluance-hfs-signature]] | A | graph-read (approx.) |
| Crossover | 2.3 kHz | [[mfr-fluance-hfs-signature]] | C | |
| Claimed sensitivity | 85 dB @ 2.83 V | [[mfr-fluance-hfs-signature]] | C | |

## Directivity
Horizontal -6 dB beamwidth about 145°, vertical about 122°. DI has minor discontinuities (ERDI residual 1.8 dB); SPDI rises from 5.1 dB at 1 kHz to 8.9 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 4.1 dB, over the 3 dB flag. ASR calls horizontal directivity uneven and advises tweeter at or above ear height. On-axis minus listening window above 4 kHz is +0.5 dB, so toe-in is not critical. See [[directivity-index]], [[early-reflections]].

## Output & distortion
No max-SPL or compression test. ASR's 96 dB plot shows THD of roughly 5% near 100-150 Hz and about 3% near 300 Hz (graph-read, approx.), falling below ~0.5% above 500 Hz; woofer is the weak point. No 86 dB plot, so `thd_86db_pct` is null. Fine for desktop or small rooms at moderate level, with a high-pass below ~80 Hz advisable. See [[compression-and-max-spl]].

## Amplifier load
Rated 8 ohm compatible, but ASR's curve falls to about 3.7 Ω near 140 Hz, below 4 Ω, so flagged `effectively-4ohm`. Impedance peaks near 16 Ω around 105 Hz; phase is moderate. EPDR not computed. Use an amplifier stable into 4 Ω. See [[impedance-and-epdr]].

## Critic reviews
- [[asr-fluance-hfs-signature]] (ASR, Tier D listening): bright and not rescued by filters; not recommended.
- [[hometheaterhifi-fluance-hfs-signature]] (HomeTheaterHiFi): clear dialogue and good value; lean bass, wants a sub.

## User reviews
Four reports, so anecdotal ([[users-fluance-hfs-signature]]): 2 call treble forward or fatiguing, 2 call it clear and balanced, 1 notes limited bass. No QC or failure reports found.

## Conflicts
- Critics disagree: HomeTheaterHiFi (sponsored sample, listening only) is positive; ASR measurements and listening are negative.
- Sensitivity: 85.8 dB computed vs 86.1 dB posted in thread vs 85 dB claimed; within 1.1 dB.
- Preference score: 2.9 here vs 3.4 posted by a thread member.
- Nominal impedance: "8 ohm compatible" claimed vs ~3.7 Ω measured minimum.
- Status: maker page shows price and a Notify Me button; stock unconfirmed.

## Related
[[fluance]] · [[fluance-reference-xl8s]] · [[polk-audio-t15]] · [[elac-debut-2-0-b5-2]] · [[spinorama]] · [[preference-score]]
