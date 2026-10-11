---
type: speaker
brand: NHT
model: Super Zero 2.1
slug: nht-super-zero-2-1
category: bookshelf
status: current
price_usd_pair: 270
price_checked: 2026-10-11
home_trial_days: null
no_hassle_return: null
trial_seller: null
trial_terms: "no verified authorized US seller policy"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 4.2
min_impedance_hz: 200
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 83.3
sensitivity_claimed_db: 87.0
f3_hz: 97
f6_hz: 82
lw_deviation_db: 1.9
on_axis_deviation_db: 2.1
hor_beamwidth_deg: 149
ver_beamwidth_deg: 116
di_smoothness: major-discontinuity
crossover_hz: 2000
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 3.0
pref_score_sub: 6.3
woofer_in: 4.5
tweeter_type: dome
port: sealed
wall_mount: null
dimensions_mm: 229x127x140
weight_kg: 2.6
critic_consensus: Audioholics praised clean, natural highs with a sub; ASR found almost no bass, low sensitivity and a directivity dip; maker says a subwoofer is required.
user_consensus: null
sources: [asr-nht-super-zero-2-1, audioholics-nht-super-zero-2-1, mfr-nht-super-zero-2-1, users-nht-super-zero-2-1, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "85 Hz-20 kHz +/-3 dB"
primary_measurement: asr-nht-super-zero-2-1
measurement_count: 1
---

## Summary
The NHT SuperZero 2.1 is a tiny (9" tall) sealed 2-way with a 4.5" paper woofer and 1" soft dome, sold singly at $134.99 each. It is rated 8 Ω nominal but measured 4.2 Ω minimum. On ASR's Klippel it has essentially no bass (f3 97 Hz), low sensitivity (83.3 dB) and a major DI discontinuity, though listening-window flatness is respectable (±1.9 dB). It only makes sense with a subwoofer, as a surround, desktop or bench speaker.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.3 dB (low) | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | computed (scripts/cta2034.py v2); claimed 87 dB per [mfr-nht-super-zero-2-1](../sources/mfr-nht-super-zero-2-1.md) |
| Listening-window deviation | ±1.9 dB, 300 Hz-10 kHz (good) | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | computed |
| On-axis deviation | ±2.1 dB (good) | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | computed |
| f3 / f6 | 97 / 82 Hz (needs a sub) | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | computed |
| Min impedance | 4.2 Ω, flat 20-250 Hz | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | graph-read (approx.); IEC floor 6.4 Ω |
| Preference score | 3.0 (no sub) / 6.3 (with sub) | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |
| THD | not entered; see Output & distortion | [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) | A | graph-read (approx.) |

## Directivity
Horizontal beamwidth about 149°, vertical about 116°. DI shows a major discontinuity (ERDI residual 2.3 dB); ASR attributes it to woofer and tweeter beamwidths failing to match around 4-5 kHz, producing a dip in the off-axis response. Early-reflection dip near 1.5 kHz is 3.8 dB, above the 3 dB flag. On-axis minus listening window above 4 kHz is +0.3 dB, so either aim works. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
ASR's graphs (graph-read, approx.) show THD at 86 dB above 5% below about 90 Hz, about 2.7% near 110 Hz and 1.5% by 130-150 Hz, with 1% or less above about 300 Hz; at 96 dB it exceeds 5% from 100-130 Hz and runs 2-2.7% around 200-400 Hz. Not entered in the table because the 100 Hz band edge is dominated by bass roll-off. No max-SPL test. Low output in a small box: suitable only for near-field or small-room use with a subwoofer. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 8 Ω nominal (4.3 Ω min claimed). ASR measured 4.2 Ω from about 20 Hz to 250 Hz with a peak near 40 Ω around 2.4 kHz, below the IEC floor of 6.4 Ω, so flagged `below-iec` (not under 4 Ω). Low sensitivity means it needs more power than its 87 dB claim suggests. EPDR not computed. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [audioholics-nht-super-zero-2-1](../sources/audioholics-nht-super-zero-2-1.md) (Audioholics, 2014, with Super 8 sub): "phenomenal"; natural, airy highs, fairly linear; small-room only.
- [asr-nht-super-zero-2-1](../sources/asr-nht-super-zero-2-1.md) (ASR, Tier D listening): no bass, dead and quiet, weak 2-3 kHz; switched off.

## User reviews
About 5 comments, mostly forum opinion, so anecdotal ([users-nht-super-zero-2-1](../sources/users-nht-super-zero-2-1.md)): 3 say bass is too poor or a sub is essential; 2 suggest surround or bench use. No QC problems reported.

## Conflicts
- Sensitivity: 83.3 dB measured vs 87 dB claimed (about 3.7 dB gap, [mfr-nht-super-zero-2-1](../sources/mfr-nht-super-zero-2-1.md)).
- Min impedance: 4.2 Ω measured vs 4.3 Ω claimed; consistent, but both far below the 6.4 Ω IEC floor for an 8 Ω rating.
- Claimed 85 Hz -3 dB point vs measured f3 97 Hz, f6 82 Hz.
- ASR judged it without a subwoofer; the maker and Audioholics evaluated it with one.
- Price: ASR forum cited $300/pair MSRP in 2020; maker store now lists $134.99 each (MSRP $149.99).

## Related
[NHT](../brands/nht.md) · [NHT C3](nht-c3.md) · Dayton Audio B652-AIR · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
