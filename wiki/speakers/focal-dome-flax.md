---
type: speaker
brand: Focal
model: Dome Flax
slug: focal-dome-flax
category: bookshelf
status: current
price_usd_pair: 1378
price_checked: 2026-10-11
home_trial_days: 60
no_hassle_return: true
trial_seller: "Crutchfield"
trial_terms: "60 days, buyer pays return shipping, no restocking fee"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 3.3
min_impedance_hz: 270
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 83.0
sensitivity_claimed_db: 88.0
f3_hz: 126
f6_hz: 105
lw_deviation_db: 3.2
on_axis_deviation_db: 3.2
hor_beamwidth_deg: 143
ver_beamwidth_deg: 119
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 1.8
pref_score_sub: 5.5
woofer_in: 4
tweeter_type: null
port: sealed
dimensions_mm: 171x146x143
weight_kg: 1.9
critic_consensus: ASR (measurement-based) rejects it for uneven response, heavy distortion and no bass; other outlets review it only as part of 5.1 packages.
user_consensus: null
sources: [asr-focal-dome-flax, users-focal-dome-flax, mfr-focal-dome-flax, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "80 Hz-28 kHz (±3 dB)"
primary_measurement: asr-focal-dome-flax
measurement_count: 1
image_url: "https://listenup.com/cdn/shop/files/661efb82-3fa5-454f-9a6f-280ead189978.jpg?v=1778859428"
---
<!-- photo -->
<img src="https://listenup.com/cdn/shop/files/661efb82-3fa5-454f-9a6f-280ead189978.jpg?v=1778859428" alt="Focal Dome Flax" width="360">

*Photo: [listenup.com](https://listenup.com/products/focal-dome-flax-ultra-compact-satellite-speaker-clearance-open-box) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Dôme Flax is a tiny sealed satellite (4" flax woofer, 171 mm tall) sold mainly for home-theater surround and lifestyle use, rated 8 Ω nominal. It is a borderline fit for this wiki's bookshelf scope (included as a passive shelf-capable monitor). On ASR's Klippel data it is poor: listening window ±3.2 dB, an elevated treble, f3 126 Hz, impedance down to 3.3 Ω and very high distortion. Directivity is wide and smooth. It needs a subwoofer and equalisation, and suits shoppers who prioritise appearance over fidelity.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.0 dB (low) | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | computed (scripts/cta2034.py v2); claimed 88 dB (condition unstated) per [mfr-focal-dome-flax](../sources/mfr-focal-dome-flax.md) |
| Listening-window deviation | ±3.2 dB (coloured, near the 3.5 dB limit) | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | computed |
| On-axis deviation | ±3.2 dB | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | computed |
| f3 / f6 | 126 / 105 Hz (needs a sub) | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | computed |
| Min impedance | 3.3 Ω, lowest region about 270 Hz | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | value stated on graph; frequency graph-read |
| Preference score | 1.8 (no sub) / 5.5 (with sub) | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |
| Distortion | see Output & distortion | [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) | A | graph-read |

## Directivity
Horizontal -6 dB beamwidth about 143 degrees, vertical about 119 degrees, wide for a non-coaxial speaker. DI is minor-discontinuity (ERDI residual 1.2 dB); SPDI rises from 2.5 dB at 1 kHz to 5.8 dB at 10 kHz. The early-reflection dip near 1.5 kHz is 3.7 dB, over the 3 dB flag. On-axis minus listening window above 4 kHz is +0.3 dB, so aiming barely matters; ASR tested it nearly upright and says tilting worsens response. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No max-SPL test; ASR limited testing to 90 dB because the woofer distorted so much. At 86 dB the THD plot exceeds the 5% scale below about 190 Hz, with about 2.3-2.5% peaks near 340-450 Hz and under 0.5% above about 1.5 kHz (graph-read; ASR labels it non-anechoic and says it is unreliable with non-flat response), so no single THD value is entered. At 90 dB it is worse. Practically a low-level, high-passed satellite; see [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
8 Ω nominal; ASR shows a 3.3 Ω minimum (flag `effectively-4ohm`) with a sharp 22 Ω resonance peak near 135 Hz and phase within about ±55 degrees. EPDR not computed. Use an amplifier comfortable at 4 Ω, with a high-pass crossover to protect the woofer. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-focal-dome-flax](../sources/asr-focal-dome-flax.md) (ASR, Tier D listening notes): forward treble, buzzy and boomy-then-absent bass; "I can't recommend" it.

## User reviews
Anecdotal only ([users-focal-dome-flax](../sources/users-focal-dome-flax.md)): no owner listening reports found; ASR thread reactions only, with two posts guessing at poor fit and finish from photos.

## Conflicts
- Sensitivity: 83.0 dB (computed) vs 88 dB claimed, a 5 dB gap; the claim's reference condition is not stated and the claim may be per watt or in-room.
- Claimed 80 Hz-28 kHz (±3 dB) vs measured f3 126 Hz and ±3.2 dB window.
- Third-party hint of a rated 4 Ω minimum vs 3.3 Ω measured.
- Price is street per pair (2 x $689, Home Technology Review snippet); MSRP $1,598 pair; page not fetched, so treat as approximate.

## Related
[Focal](../brands/focal.md) · Focal Vestia N°1 · [Focal Theva N°1](focal-theva-n1.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
