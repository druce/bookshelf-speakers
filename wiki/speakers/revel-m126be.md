---
type: speaker
brand: Revel
model: M126Be
slug: revel-m126be
status: current
price_usd_pair: 4400
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 4.9
min_impedance_hz: 170
impedance_flag: below-iec
epdr_min_ohm: 3.0
sensitivity_db_2v83: 85.7
sensitivity_claimed_db: 86.0
f3_hz: 93
f6_hz: 50
lw_deviation_db: 1.1
on_axis_deviation_db: 1.8
hor_beamwidth_deg: 129
ver_beamwidth_deg: 109
di_smoothness: minor-discontinuity
crossover_hz: 1700
max_spl_db: 102
thd_86db_pct: 1.7
thd_96db_pct: 4.2
pref_score: 5.1
pref_score_sub: 7.3
woofer_in: 6.5
tweeter_type: dome
port: rear
dimensions_mm: 386x211x262
weight_kg: 10.0
critic_consensus: Praised for neutral tonal balance, exceptional imaging, smooth beryllium treble and clean dynamics; caveats are limited bass depth (needs a sub), a slightly forward/cool voicing and price.
user_consensus: null
sources: [eac-revel-m126be, audioholics-revel-m126be, soundstage-nrc-revel-m126be, soundstage-revel-m126be, tas-revel-m126be, hometheaterhifi-revel-m126be, users-revel-m126be, mfr-revel-m126be, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "54 Hz-44 kHz (-6 dB)"
primary_measurement: eac-revel-m126be
measurement_count: 3
---

## Summary
The Revel Performa M126Be is an 8 Ω nominal two-way, 6.5" ported standmount with a 1" beryllium dome on an acoustic-lens waveguide and a 1.7 kHz crossover. On Erin's Klippel it measures very well (listening window ±1.1 dB, wide and fairly smooth directivity), with a deliberate bass shelf and f6 near 50 Hz. Its impedance dips to about 4.9 Ω, below the IEC 80% floor for an 8 Ω rating, but the phase is mild. Suits buyers wanting a Harman-style neutral, wide-dispersion monitor and willing to pay about $4,400 per pair; a sub is needed below about 50 Hz.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 85.7 dB (average) | [[eac-revel-m126be]] | A | computed (scripts/cta2034.py v2) |
| Sensitivity | 85.25 dB | [[soundstage-nrc-revel-m126be]] | A | 300 Hz-3 kHz listening window |
| Sensitivity | 87.9 dB | [[audioholics-revel-m126be]] | A | gated outdoor; claimed 86 dB per [[mfr-revel-m126be]] |
| Listening-window deviation | ±1.1 dB, 300 Hz-10 kHz (excellent) | [[eac-revel-m126be]] | A | computed |
| On-axis deviation | ±1.8 dB (good) | [[eac-revel-m126be]] | A | computed |
| f3 / f6 | 93 / 50 Hz | [[eac-revel-m126be]] | A | computed; f3 inflated by the bass shelf, see Conflicts |
| Bass knee | a little below 60 Hz; usable below 50 Hz | [[audioholics-revel-m126be]] | A | groundplane, ported |
| Min impedance | 4.9 Ω (above 80 Hz) | [[eac-revel-m126be]] | A | graph legend; ~170 Hz graph-read |
| Min impedance | ~4.5 Ω @ ~200 Hz | [[soundstage-nrc-revel-m126be]] | A | graph-read (approx.) |
| Min impedance | ~6 Ω just above 200 Hz | [[audioholics-revel-m126be]] | A | text |
| Min EPDR | 3.0 Ω (above 80 Hz) | [[eac-revel-m126be]] | A | |
| THD 86 dB @ 1 m | ~1.7% at 100 Hz | [[eac-revel-m126be]] | A | graph-read; highest in 100 Hz-10 kHz |
| THD 96 dB @ 1 m | ~4.2% at 100 Hz | [[eac-revel-m126be]] | A | graph-read |
| THD+N 90 dB @ 2 m | ~4% near 100 Hz | [[soundstage-nrc-revel-m126be]] | A | graph-read; includes noise |
| Compression | no ≥3 dB at 102 dB @ 1 m | [[eac-revel-m126be]] | A | top tested level, so max_spl_db is a lower bound |
| Preference score | 5.1 (no sub) / 7.3 (sub) | [[eac-revel-m126be]] via [[spinorama-org]] | A | not meaningful to <0.5 |
| Crossover | 1.7 kHz | [[mfr-revel-m126be]], [[audioholics-revel-m126be]] | C/A | 2nd-order tweeter, 3rd-order woofer |

## Directivity
Horizontal -6 dB beamwidth about 129°, vertical about 109° (computed). DI is minor-discontinuity (ERDI residual 1.1 dB); SPDI rises from 5.5 dB at 1 kHz to 8.1 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 1.3 dB, under the 3 dB flag. Erin notes a vertical dip near 1.7 kHz, so stay within a few degrees of the tweeter axis. On-axis minus listening window above 4 kHz is +0.6 dB, so either aim works. Audioholics found off-axis behaviour exceptionally flat and a 5 kHz on-axis bump that vanishes beyond 10°. See [[directivity-index]], [[early-reflections]].

## Output & distortion
EAC's 86 dB THD is about 1.7% at 100 Hz and under about 0.5% above 200 Hz; at 96 dB it is about 4.2% at 100 Hz and rises below that, with 0.5-0.6% bumps near 300 Hz and 1.8-2 kHz. Compression is small (within about ±0.8 dB above 100 Hz at 102 dB, +1.7 dB enhancement near 1.7 kHz), so no ≥3 dB compression through 102 dB @ 1 m. Erin links the 1.7 kHz distortion to a possible upper-mid glare. Multitone distortion stayed under 3%. Good for medium rooms at high levels with a sub or high-pass below about 80 Hz. See [[compression-and-max-spl]].

## Amplifier load
8 Ω nominal. Measured minimum 4.9 Ω (EAC), about 4.5 Ω (NRC), below the IEC floor of 6.4 Ω, so flagged `below-iec`; but not below 4 Ω. Min EPDR 3.0 Ω above 80 Hz (reading from the graph legend); phase stays within about ±40°. Audioholics called the load benign. Any competent amplifier will do. See [[impedance-and-epdr]].

## Critic reviews
- [[soundstage-revel-m126be]] (SoundStage!, Reviewers' Choice): even tonal balance, exceptional clarity and imaging; bass clean but not deep.
- [[tas-revel-m126be]] (The Absolute Sound): refined M106 successor, slightly cool and forward, airy non-brittle beryllium treble; bottom octave out of reach.
- [[hometheaterhifi-revel-m126be]] (HomeTheaterHifi): extended smooth treble, no bass trickery, no audible distortion at high levels.
- [[audioholics-revel-m126be]] (Audioholics, 5/5 performance and value): flat wide response, natural sound, imaging; "no real shortcomings".

## User reviews
About 3 reports, so anecdotal ([[users-revel-m126be]]): 2 praise sound quality and dynamics; 1 each mentions needing a sub, strained symphonic peaks, and no perceived soundstage. No QC problems reported.

## Conflicts
- Sensitivity: 85.7 dB (EAC computed) and 85.25 dB (NRC) vs 87.9 dB (Audioholics, gated outdoor) vs 86 dB claimed; the Audioholics figure is >1 dB higher.
- Minimum impedance: 4.9 Ω (EAC) vs about 4.5 Ω (NRC, graph-read) vs about 6 Ω (Audioholics text); >0.5 Ω spread. Flag follows the Tier-A lows.
- f3 93 Hz (computed) is inconsistent with f6 50 Hz and Audioholics' knee near 60 Hz; the extended bass shelf makes f3 misleading, so judge bass by f6.
- Price/status: Revel US lists it, Audio Advice has gloss black in stock at $2,200 each ($4,400/pair) while other finishes show sold out; stock is thin and may be winding down.
- EAC's page date (2023-06-23) differs from the 2023-12-19 spinorama.org date in the raw header.

## Related
[[revel]] · [[revel-m16]] · [[revel-m105]] · [[revel-m106]] · [[kef-ls50-meta]] · [[spinorama]] · [[preference-score]]
