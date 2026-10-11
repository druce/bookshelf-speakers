---
type: speaker
brand: Monitor Audio
model: Apex A10
slug: monitor-audio-apex-a10
status: current
price_usd_pair: 1698
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.0
min_impedance_hz: 12000
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 86.3
sensitivity_claimed_db: 87.0
f3_hz: 96
f6_hz: 77
lw_deviation_db: 2.7
on_axis_deviation_db: 3.0
hor_beamwidth_deg: 146
ver_beamwidth_deg: 107
di_smoothness: minor-discontinuity
crossover_hz: 3000
max_spl_db: null
thd_86db_pct: 1.5
thd_96db_pct: 5.0
pref_score: 2.75
pref_score_sub: 5.92
woofer_in: 5.5
tweeter_type: dome
port: front
dimensions_mm: 250x140x140
weight_kg: 3.95
critic_consensus: null
user_consensus: null
sources: [asr-monitor-audio-apex-a10, mfr-monitor-audio-apex-a10, users-monitor-audio-apex-a10, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "60 Hz-35 kHz (±3 dB per Hifiverse)"
primary_measurement: asr-monitor-audio-apex-a10
measurement_count: 1
---

## Summary
The Monitor Audio Apex A10 is a small 8 Ω-rated two-way (5.5" C-CAM woofer, 1" gold dome, front port) in an aluminium cabinet, aimed at home-theatre and design-led installs (stand, wall or ceiling). ASR's Klippel data show a midrange dip, resonances near 1-2 kHz and a bright treble (listening window ±2.7 dB, coloured side of good), with f3 about 96 Hz so a subwoofer is needed. Dispersion is wide horizontally. Impedance is far below the 8 Ω rating. Sold singly at about $750-849 each; the per-pair price here is doubled from one retailer. Hard to recommend on measurements.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 86.3 dB (average) | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | computed (scripts/cta2034.py v2); claimed 87 dB (1 W/1 m = 2.83 V at 8 Ω) per [mfr-monitor-audio-apex-a10](../sources/mfr-monitor-audio-apex-a10.md) |
| Listening-window deviation | ±2.7 dB, 300 Hz-10 kHz (good/borderline, coloured above ±2.5) | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | computed |
| On-axis deviation | ±3.0 dB | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | computed |
| f3 / f6 | 96 / 77 Hz (needs a sub) | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | computed; claimed 60 Hz (tolerance unstated by maker) |
| Min impedance | ~3.0 Ω @ ~12 kHz; ASR label 4 Ω @ 58 Hz | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | graph-read (approx.); ~3.6 Ω below 10 Hz |
| THD at 86 dB | ~1.5% near 100 Hz; 1.8% narrow spike at 2 kHz | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | graph-read (approx.) |
| THD at 96 dB | ~5% near 100-150 Hz (chart top); ~2.9% spike at 2 kHz | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) | A | graph-read (approx.) |
| Preference score | 2.75 (no sub) / 5.92 (sub) | [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) via [spinorama-org](../sources/spinorama-org.md) | A | ignores distortion and max output |
| Max SPL | 110.8 dBA | [mfr-monitor-audio-apex-a10](../sources/mfr-monitor-audio-apex-a10.md) | C | claimed only; not measured |

## Directivity
Horizontal -6 dB beamwidth about 146° (very wide), vertical about 107°. DI shows a minor discontinuity (ERDI residual 1.7 dB); SPDI rises from 4.1 dB at 1 kHz to 8.2 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 2.4 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.4 dB, so aim at the listener's ears; ASR advises aiming the tweeter at ear height because of the usual two-way vertical lobing, and suggests thick carpet to tame floor bounce. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
ASR found power handling excellent at 86 dB but strain both audible and measurable at 96 dB. Graph-read THD: about 1.5% near 100 Hz at 86 dB with a narrow 1.8% spike at 2 kHz (third order); at 96 dB about 5% near 100-150 Hz and broad 1-2.5% bumps through the midrange. Maker claims 110.8 dBA max SPL, which is not tested. Suits small rooms and moderate levels with a subwoofer taking over below about 100 Hz. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Nominal rating 8 Ω, but ASR's plot reaches about 4 Ω at 58 Hz and about 3.0 Ω in the treble (graph-read), so flagged `effectively-4ohm`. Peaks to about 26 Ω near 115 Hz and phase swings of roughly ±50 degrees. EPDR not computed. Use an amplifier or AVR stable into 4 Ω; high-pass at 80-100 Hz with a sub also relieves the low-frequency load. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-monitor-audio-apex-a10](../sources/asr-monitor-audio-apex-a10.md) (ASR, Tier D listening notes): bright out of the box with exaggerated highs; much warmer and more balanced with an upper-bass EQ boost; faint sub-bass; not recommended at the price.
- No professional press review of the current model was ingested.

## User reviews
3 owner reports, anecdotal ([users-monitor-audio-apex-a10](../sources/users-monitor-audio-apex-a10.md)): 2 of 3 describe bright or sharp sound; 1 happy 7.2 owner; 1 thinks the price too high. QC: only a cosmetic note that the white finish yellows in direct sunlight (1 report).

## Conflicts
- Minimum impedance: ASR's plot label says 4 Ω @ 58 Hz, but the curve itself falls to about 3 Ω above 10 kHz (graph-read); I record the lower value and the `effectively-4ohm` flag follows it. Maker claims 8 Ω nominal.
- Sensitivity: 86.3 dB measured vs 87 dB claimed (0.7 dB, within noise).
- Price: ASR $750 each (Jan 2025) vs $849 each at one retailer; per-pair figure uses the latter doubled.

## Related
[Monitor Audio](../brands/monitor-audio.md) · [Monitor Audio Bronze 50 7G](monitor-audio-bronze-50-7g.md) · [directivity-index](../concepts/directivity-index.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [compression-and-max-spl](../concepts/compression-and-max-spl.md)
