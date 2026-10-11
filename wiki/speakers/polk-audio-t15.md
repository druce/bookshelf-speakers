---
type: speaker
brand: Polk Audio
model: T15
slug: polk-audio-t15
category: bookshelf
status: current
price_usd_pair: 149
price_checked: 2026-10-11
home_trial_days: 30
no_hassle_return: true
trial_seller: "Polk Audio"
trial_terms: "30 days, free return shipping, no restocking fee"
trial_checked: "2026-10-11"
nominal_impedance_ohm: 8
min_impedance_ohm: 4.1
min_impedance_hz: 250
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 88.7
sensitivity_claimed_db: 89.0
f3_hz: 88
f6_hz: 73
lw_deviation_db: 7.1
on_axis_deviation_db: 9.2
hor_beamwidth_deg: 133
ver_beamwidth_deg: 129
di_smoothness: major-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 0.3
pref_score_sub: 3.4
woofer_in: 5.25
tweeter_type: dome
port: front
wall_mount: "keyhole"
dimensions_mm: 270x165x184
weight_kg: null
critic_consensus: Measures poorly on axis (3-6 kHz hole); Audioholics found it veiled at ear level but decent and wide-sounding 20 degrees above or below; ASR does not recommend it.
user_consensus: null
sources: [asr-polk-audio-t15, audioholics-polk-audio-t15, mfr-polk-audio-t15, users-polk-audio-t15, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "60 Hz-24 kHz; -3 dB limits 65 Hz-20 kHz (T-Series info sheet)"
primary_measurement: asr-polk-audio-t15
measurement_count: 2
image_url: "https://www.polkaudio.com/on/demandware.static/-/Sites-master-catalog-soundunited/default/dw40f16370/polk/PDP_Images/Home-Speakers/Bookshelf/T-Series/T15/T15_Image_angle-right-left.png"
---
<!-- photo -->
<img src="https://www.polkaudio.com/on/demandware.static/-/Sites-master-catalog-soundunited/default/dw40f16370/polk/PDP_Images/Home-Speakers/Bookshelf/T-Series/T15/T15_Image_angle-right-left.png" alt="Polk Audio T15" width="360">

*Photo: [polkaudio.com](https://www.polkaudio.com/en-us/product/home-speakers/bookshelf/t15/112508.html) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The T15 is Polk's $149-per-pair entry bookshelf: a 5.25" woofer with a 0.75" dome in a small front-ported cabinet with a keyhole for wall mounting, rated 8 Ω nominal. It measures badly at ear height: listening window ±7.1 dB, a deep 3-6 kHz cancellation on axis, f3 of 88 Hz and a distortion peak near 400 Hz. Polk says the design intentionally favours placement above or below ear level, as with surrounds. Suits only budget surround or wall-mounted use, preferably with a subwoofer; stereo listening buyers have far better options.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 88.7 dB (high) | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | computed (scripts/cta2034.py v2) |
| Sensitivity | 86.4 dB (average) | [audioholics-polk-audio-t15](../sources/audioholics-polk-audio-t15.md) | B | gated, 2.83 V; claimed 89 dB per [mfr-polk-audio-t15](../sources/mfr-polk-audio-t15.md) |
| Listening-window deviation | ±7.1 dB, 300 Hz-10 kHz (coloured) | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | computed |
| On-axis deviation | ±9.2 dB (coloured) | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | computed |
| f3 / f6 | 88 / 73 Hz (needs a sub) | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | computed; claimed -3 dB 65 Hz |
| Min impedance | ~4.1 Ω @ ~60 and ~250 Hz | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | graph-read (approx.); ~3.9 Ω near 20 kHz |
| THD | not recorded | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) | A | plot level not stated; ~3.4 % near 80-95 Hz, narrow ~4.5 % spike near 400 Hz |
| Preference score | 0.3 (no sub) / 3.4 (with sub) | [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) via [spinorama-org](../sources/spinorama-org.md) | A | not meaningful to <0.5 |

## Directivity
Horizontal -6 dB beamwidth about 133°, vertical about 129°. ERDI residual is 2.2 dB but flagged major-discontinuity; the early-reflection dip near 1.5 kHz is 6.2 dB, well over the 3 dB flag, and the on-axis hole at 3-6 kHz comes from driver cancellation. Both ASR and [audioholics-polk-audio-t15](../sources/audioholics-polk-audio-t15.md) show the response is flatter about 20° above or below the tweeter (ASR notes re-referencing to -20° lifts the score to about 1.4 per a forum member). On-axis minus listening window above 4 kHz is -0.9 dB. Aim above or below the ear rather than level with it; Audioholics reports reasonably uniform horizontal coverage to about 40°. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No max-SPL or compression test. ASR's THD plot (SPL not stated) shows about 3.4 % near 80-95 Hz and a narrow spike of about 4.5 % near 400 Hz, with a "ghost" sweep audible; Audioholics found good dynamic range and no obvious distortion shift when played very loud (Tier D). Fine for modest levels as a surround; not for loud music in a larger room. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Polk rates 8 Ω nominal. ASR's plot shows about 4 Ω through most of the range (about 4.1 Ω near 60 and 250 Hz), below the IEC floor of 6.4 Ω, so `below-iec`; Audioholics judged the 8 Ω rating fair with "swathes" near 6 Ω and benign phase. EPDR not computed. Easy for budget AVRs. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [audioholics-polk-audio-t15](../sources/audioholics-polk-audio-t15.md) (Audioholics, 3.5/5 performance, 4.5/5 value): veiled and "cupped" at ear level, wide stage and decent imaging at 20° elevation; good for budget surrounds.
- [asr-polk-audio-t15](../sources/asr-polk-audio-t15.md) (ASR, Tier D listening notes): not horrible on a desk but measured poorly; recommends the Pioneer SP-BS22-LR instead.

## User reviews
No owner reports ingested; the ASR thread is measurement discussion ([users-polk-audio-t15](../sources/users-polk-audio-t15.md)). Anecdotal at best.

## Conflicts
- Sensitivity: 88.7 dB (ASR computed) vs 86.4 dB (Audioholics, gated) vs 89 dB claimed; the first two differ by more than 1 dB.
- Bass: ASR f3 88 Hz vs maker -3 dB 65 Hz; Audioholics noted overdamped, wall-friendly bass with no f3 stated.
- Impedance: maker 6-8 Ω/8 Ω nominal and Audioholics "fair" vs ASR graph near 4 Ω.
- Frequency response: both reviewers find a 3-5 kHz dip on axis, but Audioholics (gated) judged it fine at 20° above/below, while ASR scores the on-axis curve.

## Related
[Polk Audio](../brands/polk-audio.md) · [Polk Audio Monitor XT15](polk-audio-xt15.md) · Polk Audio Signature Elite ES15 · Pioneer SP-BS22-LR · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
