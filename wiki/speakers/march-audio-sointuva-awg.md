---
type: speaker
brand: March Audio
model: Sointuva AWG
slug: march-audio-sointuva-awg
status: current
price_usd_pair: 4100
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 3.0
min_impedance_hz: 180
impedance_flag: effectively-4ohm
epdr_min_ohm: 1.5
sensitivity_db_2v83: 81.2
sensitivity_claimed_db: 83.0
f3_hz: 37
f6_hz: 32
lw_deviation_db: 1.5
on_axis_deviation_db: 1.2
hor_beamwidth_deg: 121
ver_beamwidth_deg: 95
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: 102
thd_86db_pct: 0.8
thd_96db_pct: 0.9
pref_score: 6.95
pref_score_sub: 8.45
woofer_in: 6.5
tweeter_type: dome
port: passive-radiator
dimensions_mm: 450x240x220
weight_kg: null
critic_consensus: null
user_consensus: null
sources: [eac-march-audio-sointuva-awg, mfr-march-audio-sointuva-awg, users-march-audio-sointuva-awg, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "50 Hz-18 kHz ±1.2 dB; 37 Hz-19 kHz ±3.0 dB (F3 37 Hz)"
primary_measurement: eac-march-audio-sointuva-awg
measurement_count: 1
image_url: "https://marchaudio.com/wp-content/uploads/2023/11/Sointuva-AWG-TAs-blackwwod.webp"
---
<!-- photo -->
<img src="https://marchaudio.com/wp-content/uploads/2023/11/Sointuva-AWG-TAs-blackwwod.webp" alt="March Audio Sointuva AWG" width="360">

*Photo: [marchaudio.com](https://marchaudio.com/product/sointuva-awg-stand-mount-speaker/) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Sointuva AWG is a made-to-order Australian 6 Ω standmount using a 6.5" Purifi aluminium woofer, a beryllium-dome tweeter on a waveguide and dual rear passive radiators. On Erin's Klippel it is very flat (listening window ±1.5 dB), reaches f3 of 37 Hz (outstanding for a standmount) and shows low distortion and almost no compression at 102 dB. The costs are low sensitivity (81.2 dB computed) and a brutal impedance (about 3 Ω minimum, EPDR 1.5 Ω), so it needs a strong, 4 Ω-stable amplifier. It must be aimed about 7° above the tweeter. Price is high (about $4,100 per pair) and US purchase is manufacturer-direct only (US shipping not verified).

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 81.2 dB (low) | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | computed (scripts/cta2034.py v2); claimed 83.0 dB in [mfr-march-audio-sointuva-awg](../sources/mfr-march-audio-sointuva-awg.md) |
| Listening-window deviation | ±1.5 dB, 300 Hz-10 kHz (excellent) | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | computed; reference axis 7° above tweeter |
| On-axis deviation | ±1.2 dB | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | computed |
| f3 / f6 | 37 / 32 Hz (excellent) | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | computed, anechoic; maker claims 37 / 33 Hz |
| Min impedance | ~3.0 Ω above 80 Hz | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | graph-read (approx.); maker claims 3.4 Ω @168 Hz |
| Min EPDR | 1.5 Ω | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | stated on plot, above 80 Hz |
| THD 86 dB | ~0.8% worst, ~100 Hz | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | graph-read (approx.); clean above 600 Hz |
| THD 96 dB | ~0.9% worst, ~100 Hz and ~9.5 kHz | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | graph-read (approx.) |
| Compression at 102 dB | under ~0.6 dB above 80 Hz | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) | A | graph-read; test ceiling, not a limit |
| Preference score | 6.95 (no sub) / 8.45 (with sub) | [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) via [spinorama-org](../sources/spinorama-org.md) | A | differences under 0.5 not meaningful |

## Directivity
Horizontal -6 dB beamwidth about 121°, vertical about 95°. Erin notes roughly ±70° up to 4 kHz, then narrowing from the waveguide. DI is a minor discontinuity (ERDI residual 1.1 dB); SPDI rises from 5.6 dB at 1 kHz to 10.0 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 1.2 dB, well under the 3 dB flag. On-axis minus listening window above 4 kHz is +1.2 dB: on-axis is slightly brighter than the window, so less toe-in or axes crossing in front is favoured; Erin warns that tweeter-height listening dips 2-4 kHz, so sit about 7° above the tweeter. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
THD at 86 dB is about 0.8% at worst (a ~100 Hz peak) and falls to 0.1-0.3% above 600 Hz; at 96 dB it peaks around 0.9% (graph-read, approximate), clean by the section 7 yardstick. Compression at 102 dB @1 m is under about 0.6 dB above 80 Hz, so `max_spl_db: 102` is the test ceiling, not a measured limit. Erin found 100 W adequate but not abundant at 10 ft in a medium room, a consequence of low sensitivity. Suits small to medium rooms at moderate-high levels given adequate power. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal, but the plot reports about 3 Ω minimum (graph-read; maker says 3.4 Ω) and minimum EPDR 1.5 Ω, so flagged `effectively-4ohm`. Impedance peaks near 2.7 kHz (~37 Ω) with phase swinging to -57° near 60 Hz. Needs an amplifier stable into 2-3 Ω with high current; combined with 81 dB sensitivity this is a demanding load. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
No professional review of the AWG (as opposed to the earlier WG) was ingested.
- [eac-march-audio-sointuva-awg](../sources/eac-march-audio-sointuva-awg.md) (Erin's Audio Corner, Tier D listening notes): sounded incredible with no complaints, bass impressive for size; may not need a sub; easy to listen too loudly.

## User reviews
No usable pattern: about 2 owner comments on the ASR thread, anecdotal ([users-march-audio-sointuva-awg](../sources/users-march-audio-sointuva-awg.md)); one says no subwoofer needed. QC: no confirmed problems; an early-batch connector air-seal remark is unverified.

## Conflicts
- Sensitivity: 81.2 dB computed from Erin's Klippel data vs 83.0 dB claimed by the maker (1.8 dB lower); measurement governs.
- Minimum impedance: about 3.0 Ω (Erin plot, graph-read) vs 3.4 Ω @168 Hz claimed by the maker.
- Erin's text cites "F3 of 40 Hz" while computed f3 is 37 Hz and the maker claims 37 Hz.

## Related
[March Audio](../brands/march-audio.md) · March Audio Sointuva · [directivity-index](../concepts/directivity-index.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [compression-and-max-spl](../concepts/compression-and-max-spl.md) · [preference-score](../concepts/preference-score.md)
