---
type: speaker
brand: Neumi
model: BS5
slug: neumi-bs5
category: bookshelf
status: current
price_usd_pair: null
price_checked: 2026-10-11
home_trial_days: null
no_hassle_return: null
trial_seller: null
trial_terms: "no verified authorized US seller policy"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 6
min_impedance_ohm: 4.1
min_impedance_hz: 20000
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 82.5
sensitivity_claimed_db: 87.3
f3_hz: 68
f6_hz: 54
lw_deviation_db: 3.5
on_axis_deviation_db: 3.5
hor_beamwidth_deg: 145
ver_beamwidth_deg: 104
di_smoothness: minor-discontinuity
crossover_hz: 2100
max_spl_db: 93
thd_86db_pct: 2.1
thd_96db_pct: 3.2
pref_score: 3.6
pref_score_sub: 6.1
woofer_in: 5
tweeter_type: dome
port: front
dimensions_mm: 269x183x216
weight_kg: 3.2
critic_consensus: null
user_consensus: Amazon theme tallies are strongly positive on value and build; caveats are limited bass and no loud playback.
sources: [eac-neumi-bs5, eac-neumi-bs5-v1, mfr-neumi-bs5, users-neumi-bs5, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "50 Hz-20 kHz (typical in-room), no tolerance"
primary_measurement: eac-neumi-bs5
measurement_count: 2
---

## Summary
The Neumi BS5 is a 6 Ω, dual front-ported two-way with a 5" fibreglass woofer and 1" silk dome, sold at budget prices (about $90 in 2020, $109 in 2021, now uncertain). On Erin's Klippel it is only moderately flat (listening window ±3.5 dB) with port-related dips near 800 Hz and 1.6 kHz, modest bass (f3 68 Hz) and low sensitivity (82.5 dB). It measures worse than its 86 dB claim suggests. Suits a bedroom, desk or surround role with a subwoofer. Availability is murky: Amazon's own listing is unavailable.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 82.5 dB (low) | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | computed (scripts/cta2034.py v2) |
| Sensitivity | about 84.2 dB | [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) | A | 2020 gated method, 300 Hz-3 kHz mean |
| Listening-window deviation | ±3.5 dB, 300 Hz-10 kHz (coloured edge) | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | computed; ±2.3 dB with ports stuffed |
| On-axis deviation | ±3.5 dB | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | computed |
| f3 / f6 | 68 / 54 Hz (modest) | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | computed; F10 40 Hz per Erin |
| f3 (2020) | 64 Hz | [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) | A | |
| Min impedance | about 4.1 Ω near 20 kHz | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | graph-read (approx.); about 5.5 Ω near 200 Hz |
| Min impedance (2020) | about 4.6 Ω above 7 kHz | [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) | A | stated |
| THD 86 dB @ 1 m | about 2.1% peak near 370 Hz | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | graph-read (approx.) |
| THD 96 dB @ 1 m | about 3.2% peak near 380 Hz | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) | A | graph-read (approx.); rises sharply below 80 Hz |
| Max SPL | about 93 dB @ 1 m with 80 Hz high-pass; about 82 dB full range | [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) | A | multitone, -20 dB distortion or -3 dB compression limit |
| Preference score | 3.6 (no sub) / 6.1 (with sub) | [eac-neumi-bs5](../sources/eac-neumi-bs5.md) via [spinorama-org](../sources/spinorama-org.md) | A | ports stuffed: 4.6 / 7.7; 2020 data: 4.3 / 6.7; differences over 0.5 |
| Crossover | 2.1 kHz | [mfr-neumi-bs5](../sources/mfr-neumi-bs5.md) | C | as relayed by [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) |

## Directivity
Horizontal -6 dB beamwidth about 145°, vertical about 104°. DI is minor-discontinuity (ERDI residual 2.0 dB); SPDI rises from 5.4 dB at 1 kHz to 8.0 dB at 10 kHz. Early-reflection dip near 1.5 kHz is 1.8 dB, under the 3 dB flag, though Erin sees deep nulls near 800 Hz and 1.6 kHz that he traces to radiation from the front ports. On-axis minus listening window above 4 kHz is +0.8 dB, so either aim works; Erin preferred listening on-axis because the treble was subdued off-axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Distortion is high for the level: about 2.1% at 86 dB and about 3.2% at 96 dB in the mid-band (graph-read), peaking near 370 Hz, with THD well above 3% below 80 Hz at 96 dB. Compression at 102 dB reaches about 2.6 dB near 75 Hz. Erin's 2020 multitone test limits it to about 93 dB @ 1 m with an 80 Hz high-pass and about 82 dB full range; he heard compression at 90-92 dB at 11 ft. Fine for desk or small-room use with a subwoofer, not for loud listening. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 6 Ω; measured minimum about 4.1 Ω in the top octave (low power there), so flagged `below-iec` (floor 4.8 Ω). Impedance is mostly above 5.5 Ω below 5 kHz with a peak near 90 Hz. Erin cautions that some AVRs dislike 6 Ω loads. EPDR not shown. Neumi suggests 15-100 W per channel. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [eac-neumi-bs5](../sources/eac-neumi-bs5.md) (Erin, Tier D listening notes): reasonably neutral sound with port-induced midrange dip and 1-2 kHz resonance; likeable budget starter.
- [eac-neumi-bs5-v1](../sources/eac-neumi-bs5-v1.md) (Erin, 2020): treble slightly subdued, midrange distortion on male vocals at high level, punchy but light bass; good value, better sealed against a wall.
- No outside critic reviews found.

## User reviews
Amazon theme tallies ([users-neumi-bs5](../sources/users-neumi-bs5.md), 419 ratings, 4.7/5; tallies are Amazon's own): 107 of 134 sound-quality mentions positive, 92 of 95 value mentions positive, 24 of 25 build mentions positive. Recurring caveats: not for loud playback, bass thin or muddy (about 3 excerpts). No QC failures reported. Amazon first-party listing currently unavailable.

## Conflicts
- Sensitivity: 82.5 dB (2021 Klippel NFS, computed) vs about 84.2 dB (2020 method) vs claimed 86 dB/1 W, which is about 87.3 dB at 2.83 V for 6 Ω; measured is about 4.8 dB below the claim. Used the NFS value.
- Minimum impedance: about 4.1 Ω (2021, graph-read) vs about 4.6 Ω (2020, stated); 0.5 Ω apart; both below the IEC floor.
- Distortion: Erin's 2020 remark of mostly under 1% at 84 dB mean SPL vs the 2021 graph-read of about 2.1% at 86 dB; different methods and level.
- Claimed 50 Hz-20 kHz in-room vs measured f3 64-68 Hz anechoic (not like for like).
- Price/status: Amazon first-party "Currently unavailable", renewed pair $119.99, third-party new listings around $240-265 in search snippets (unverified); maker still lists it. `price_usd_pair` left null.

## Related
[Neumi](../brands/neumi.md) · [Neumi Silk 4](neumi-silk-4.md) · Micca RB42 · Micca MB42X-G2 · Dayton Audio B652-AIR · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
