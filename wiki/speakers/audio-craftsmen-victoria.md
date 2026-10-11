---
type: speaker
brand: Audio Craftsmen
model: Victoria
slug: audio-craftsmen-victoria
category: bookshelf
status: current
price_usd_pair: 3990
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 7.3
min_impedance_hz: 170
impedance_flag: null
epdr_min_ohm: 4.4
sensitivity_db_2v83: 83.4
sensitivity_claimed_db: 88.0
f3_hz: 63
f6_hz: 54
lw_deviation_db: 2.5
on_axis_deviation_db: 2.6
hor_beamwidth_deg: 145
ver_beamwidth_deg: 111
di_smoothness: minor-discontinuity
crossover_hz: 2200
max_spl_db: 102
thd_86db_pct: 1.8
thd_96db_pct: 2.2
pref_score: 4.9
pref_score_sub: 7.3
woofer_in: 6.5
tweeter_type: dome
port: rear
dimensions_mm: 405x230x355
weight_kg: 16.0
critic_consensus: Steve Huff found it refined and smooth; Erin's listening notes found thin midrange and weak bass, so critics are split.
user_consensus: null
sources: [mfr-audio-craftsmen-victoria, eac-audio-craftsmen-victoria, stevehuff-audio-craftsmen-victoria, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "42 Hz-25 kHz ±2 dB"
primary_measurement: eac-audio-craftsmen-victoria
measurement_count: 1
---

## Summary
The Audio Craftsmen Victoria is an 8 Ω, rear-ported, double-walled Canadian standmount with SEAS drivers, sold direct at $3,990 per pair. Erin's Klippel data show a good (±2.5 dB) listening window with a 200-800 Hz midrange dip, modest bass (f3 63 Hz) and only 83.4 dB sensitivity against an 88 dB claim. Dispersion is wide horizontally and narrow vertically. It is an easy load with low distortion at moderate level. Availability is uncertain: the maker page shows it out of stock.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.4 dB (low) | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | computed (scripts/cta2034.py v2); claimed 88 dB in [mfr-audio-craftsmen-victoria](../sources/mfr-audio-craftsmen-victoria.md) |
| Listening-window deviation | ±2.5 dB, 300 Hz-10 kHz (good) | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | computed |
| On-axis deviation | ±2.6 dB (good) | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | computed |
| f3 / f6 | 63 / 54 Hz (modest) | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | computed; Erin quotes 65 Hz F3 |
| Min impedance | 7.3 Ω @ about 170 Hz | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | printed on graph, above 80 Hz |
| Min EPDR | 4.4 Ω | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | above 80 Hz |
| Preference score | 4.9 (no sub) / 7.3 (with sub) | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) via [spinorama-org](../sources/spinorama-org.md) | A | 4.87/7.34 from packet; not meaningful to <0.5 |
| THD 86 dB / 96 dB | about 1.8% / 2.2% near 100 Hz | [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) | A | graph-read (approx.) |

## Directivity
Horizontal -6 dB beamwidth about 145°, vertical about 111°. DI is a minor discontinuity (ERDI residual 1.6 dB); SPDI rises from 5.7 dB at 1 kHz to 9.5 dB at 10 kHz. Early-reflection dip near 1.5 kHz is only 0.6 dB. On-axis minus listening window above 4 kHz is +0.9 dB, so either aim works; Erin notes treble drops off-axis and recommends pointing it at the listener. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's tests: THD about 1.8% near 100 Hz at 86 dB and about 2.2% at 96 dB (graph-read), falling to well under 1% above 1 kHz at 86 dB; THD exceeds 3% at 96 dB below about 70 Hz. Compression stays within about 1.3 dB at 102 dB, with 1.6 dB enhancement near 65 Hz (port region). `max_spl_db: 102` is the highest test level reached, not a limit. Erin traced audible grain near 1 kHz only at very high levels. Fine for small-to-medium rooms; bass below 100 Hz limits loud use. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
8 Ω nominal; 7.3 Ω minimum above 80 Hz, no flag. Minimum EPDR 4.4 Ω near 110 Hz, with phase within about ±40°, so it is moderately easy; a 1.3 kHz impedance peak reaches about 36 Ω. Any competent amplifier works. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [stevehuff-audio-craftsmen-victoria](../sources/stevehuff-audio-craftsmen-victoria.md) (Steve Huff, 2025): refined, smooth, silky mids; "high end bargain".
- [eac-audio-craftsmen-victoria](../sources/eac-audio-craftsmen-victoria.md) (Erin's Audio Corner, Tier D listening notes): thin, slightly hollow midrange, weak bass below 80 Hz, treble dulls off-axis; wide imaging; sub recommended; placement near wall helps.

## User reviews
No user reports ingested yet.

## Conflicts
- Sensitivity: 83.4 dB computed (Erin says about 84 dB) vs 88 dB claimed; about 4.6 dB gap.
- Bass: f3 63 Hz measured vs 42 Hz claimed (claim is ±2 dB, which the measurement does not support).
- Critics split on tonality (Huff smooth and rich vs Erin thin midrange); the Klippel dip at 200-800 Hz supports Erin.
- Preference score: 4.87 (packet) vs 4.92 shown in a spinorama page snippet; trivial difference.
- Status: maker-direct page priced $3,990 but marked out of stock and absent from the maker's all-products list; coordinator should confirm. Earlier prices were $5,500-$5,999.

## Related
[Audio Craftsmen](../brands/audio-craftsmen.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [bass-extension-vs-room-gain](../concepts/bass-extension-vs-room-gain.md)
