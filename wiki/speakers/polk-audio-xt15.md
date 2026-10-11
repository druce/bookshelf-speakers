---
type: speaker
brand: Polk Audio
model: Monitor XT15
slug: polk-audio-xt15
status: current
price_usd_pair: 149
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 4.0
min_impedance_hz: 250
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 84.4
sensitivity_claimed_db: 86.0
f3_hz: 77
f6_hz: 64
lw_deviation_db: 1.9
on_axis_deviation_db: 2.6
hor_beamwidth_deg: 127
ver_beamwidth_deg: 101
di_smoothness: minor-discontinuity
crossover_hz: 2200
max_spl_db: 102
thd_86db_pct: 0.5
thd_96db_pct: 2.5
pref_score: 4.6
pref_score_sub: 7.3
woofer_in: 5.25
tweeter_type: dome
port: rear
dimensions_mm: 269x165x182
weight_kg: 4.1
critic_consensus: TNT-Audio found it open and articulate with surprisingly strong bass for its size and a plain, slightly light mid-high; good value for a second or first system.
user_consensus: null
sources: [eac-polk-audio-xt15, tntaudio-polk-audio-xt15, mfr-polk-audio-xt15, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "48 Hz-40 kHz (no tolerance); TNT-Audio cites a manual figure of 73 Hz-26 kHz +/-3 dB"
primary_measurement: eac-polk-audio-xt15
measurement_count: 1
---

## Summary
The Monitor XT15 is Polk's smallest Monitor XT model: a 5.25" two-way with a rear port and 1" Terylene dome, now $149 per pair on Polk US. Polk rates it only as compatible with 4- and 8-ohm outputs; it is recorded as 8 Ω compatible, but measured minimum impedance is about 4.0 Ω. Erin's Klippel data show a good listening window (±1.9 dB), minor directivity discontinuity and clean distortion, but low sensitivity (84.4 dB) and limited bass (f3 77 Hz). A useful budget surround or small-room speaker that wants a subwoofer.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 84.4 dB (average, low end) | [[eac-polk-audio-xt15]] | A | computed (scripts/cta2034.py v2); claimed 86 dB per [[mfr-polk-audio-xt15]] |
| Listening-window deviation | ±1.9 dB, 300 Hz-10 kHz (good) | [[eac-polk-audio-xt15]] | A | computed |
| On-axis deviation | ±2.6 dB (good) | [[eac-polk-audio-xt15]] | A | computed |
| f3 / f6 | 77 / 64 Hz (needs a sub) | [[eac-polk-audio-xt15]] | A | computed |
| Min impedance | ~4.0 Ω @ ~250 Hz | [[eac-polk-audio-xt15]] | A | graph-read (approx.); manual cited as 4.1 Ω by [[tntaudio-polk-audio-xt15]] |
| THD at 86 dB | ~0.5 % (clean) | [[eac-polk-audio-xt15]] | A | graph-read; narrow ~0.7 % spike near 310 Hz |
| THD at 96 dB | ~2.5 % | [[eac-polk-audio-xt15]] | A | graph-read; 150-190 Hz, narrow ~3.2 % spike near 195 Hz |
| Compression | ≤2.4 dB at 102 dB, 50 Hz-20 kHz | [[eac-polk-audio-xt15]] | A | graph-read; max_spl ≥102 dB is the test ceiling |
| Preference score | 4.6 (no sub) / 7.3 (with sub) | [[eac-polk-audio-xt15]] via [[spinorama-org]] | A | not meaningful to <0.5 |
| Crossover | 2.2 kHz | [[mfr-polk-audio-xt15]] | C | |

## Directivity
Horizontal -6 dB beamwidth about 127°, vertical about 101°. ERDI residual 1.4 dB (minor discontinuity); SPDI rises from 4.3 dB at 1 kHz to 8.8 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.1 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.8 dB, so either aim works. See [[directivity-index]], [[early-reflections]].

## Output & distortion
THD at 86 dB is about 0.5 % above 100 Hz and at 96 dB about 2.5 % at 150-190 Hz (graph-read). Erin's instant-compression test shows up to about 2.4 dB loss at 102 dB near 70 and 180 Hz, under 1 dB above 700 Hz and no 3 dB point above 50 Hz. With only 84.4 dB sensitivity, reaching 102 dB at 1 m needs roughly 60 W (8 Ω equivalent); suited to small rooms and moderate levels. See [[compression-and-max-spl]].

## Amplifier load
Impedance dips to about 4.0 Ω near 200-300 Hz with peaks near 24 Ω (35 Hz) and 30 Ω (100 Hz); phase stays moderate. Below the IEC 6.4 Ω floor, so `below-iec` (just above the 4 Ω threshold). EPDR not computed. Any competent receiver should cope at modest levels. See [[impedance-and-epdr]].

## Critic reviews
- [[tntaudio-polk-audio-xt15]] (TNT-Audio): open, articulate, crisp mid-high with deep, forceful bass for the size; slightly light in lower vocals, narrow soundstage; preferred over the Eltax Monitor 1.
- [[eac-polk-audio-xt15]]: Erin gave no subjective evaluation in the written page.

## User reviews
No user reports ingested yet.

## Conflicts
- Sensitivity: 84.4 dB measured vs 86 dB claimed (reference unstated, 1 W per Erin); difference of 1.6 dB.
- Bass: f3 77 Hz and f6 64 Hz measured vs 48 Hz claimed FR with no tolerance; TNT-Audio cites a manual ±3 dB figure of 73 Hz, closer to the measured value.
- Impedance: Polk gives 4/8-ohm compatibility only; measured about 4.0 Ω (manual 4.1 Ω per TNT-Audio).
- TNT-Audio praised "deep" bass for the size, which is relative; the measured f3 is 77 Hz.
- Price: Erin quoted about $200/pair in 2022; Polk US now lists $149 (reduced from $179).

## Related
[[polk-audio]] · [[polk-audio-xt20]] · [[polk-audio-t15]] · Polk Audio Signature Elite ES15 · [[spinorama]] · [[preference-score]] · [[impedance-and-epdr]]
