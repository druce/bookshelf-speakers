---
type: speaker
brand: Role Audio
model: Skiff
slug: role-audio-skiff
status: current
price_usd_pair: 495
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 7.7
min_impedance_hz: 350
impedance_flag: null
epdr_min_ohm: null
sensitivity_db_2v83: 80.6
sensitivity_claimed_db: 88.0
f3_hz: 143
f6_hz: 126
lw_deviation_db: 3.9
on_axis_deviation_db: 5.0
hor_beamwidth_deg: 129
ver_beamwidth_deg: 128
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: -0.5
pref_score_sub: 3.6
woofer_in: 3.5
tweeter_type: null
port: sealed
dimensions_mm: 152x102x127
weight_kg: 1.6
critic_consensus: Praised for midrange purity, coherence and imaging as a near-field/desktop speaker; limited bass and output, subwoofer advised.
user_consensus: null
sources: [asr-role-audio-skiff, mfr-role-audio-skiff, enjoythemusic-role-audio-skiff, boundforsound-role-audio-skiff, users-role-audio-skiff, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "90 Hz-20 kHz (maker page); 125 Hz-20 kHz (-6 dB) per ASR/Bound for Sound"
primary_measurement: asr-role-audio-skiff
measurement_count: 1
---

## Summary
The Role Audio Skiff is a 6x4x5 in sealed micro speaker with a single 3.5" full-range driver and no crossover, rated 8 Ω and sold direct at $495 per pair. It is a desktop monitor rather than a conventional bookshelf speaker, kept in scope under the desktop-monitor rule. ASR's Klippel test found at least four driver resonances, listening-window deviation of ±3.9 dB, f3 about 143 Hz, sensitivity 80.6 dB versus 88 dB claimed, and distortion before 86 dB, and did not recommend it. Older critic reviews like its midrange coherence and imaging when used near-field with a subwoofer.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 80.6 dB (low) | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | computed (scripts/cta2034.py v2); claimed 88 dB/1 W per [mfr-role-audio-skiff](../sources/mfr-role-audio-skiff.md), equal to 88 dB at 2.83 V for 8 Ω nominal |
| Listening-window deviation | ±3.9 dB, 300 Hz-10 kHz (coloured) | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | computed |
| On-axis deviation | ±5.0 dB | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | computed |
| f3 / f6 | 143 / 126 Hz (needs a sub) | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | computed |
| Min impedance | 7.7 Ω | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | ASR graph label; ~350 Hz graph-read; 38 Ω peak near 180 Hz |
| THD at 80 / 83 dB | up to ~2.2% / ~2.9% near 4.5 kHz; >5% below ~200 Hz | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) | A | graph-read; not 86/96 dB, so frontmatter null |
| Preference score | -0.5 (no sub) / 3.6 (sub) | [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) via [spinorama-org](../sources/spinorama-org.md) | A | ignores distortion and max output |

## Directivity
Horizontal -6 dB beamwidth about 129°, vertical about 128°, but ASR describes beamwidth and directivity as highly variable in both planes, with a DI dip where a crossover would normally be. DI shows a minor discontinuity (ERDI residual 1.6 dB); SPDI rises from 2.5 dB at 1 kHz to 10.5 dB at 10 kHz (strong top-octave beaming, as Bound for Sound also noted). Early-reflection dip near 1.5 kHz is 1.7 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.7 dB, so either aim works, though critics advise listening on-axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
ASR could not reach 86 dB SPL at 1 m: the speaker made odd sounds and compressed first, so distortion was run at 80 and 83 dB, where THD is above 5% below about 200 Hz and reaches about 2-3% near 4.5 kHz. Response is flat to DC, so a high-pass is advisable. Practical output is for near-field desktop listening only. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
8 Ω nominal; ASR's label says 7.7 Ω minimum (maker states 6.5 Ω minimum), no flag. Impedance is high and smooth (peak about 38 Ω at the box resonance), a benign load; but with 80.6 dB sensitivity it needs real power for any level. EPDR not reported. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [boundforsound-role-audio-skiff](../sources/boundforsound-role-audio-skiff.md) (Bound for Sound, via the maker): crisp, silky midrange to lower treble; subwoofer-friendly; wide placement tolerance.
- [enjoythemusic-role-audio-skiff](../sources/enjoythemusic-role-audio-skiff.md) (Enjoy the Music, 2006): linear, disappearing imaging, needs a subwoofer and a strong amp.
- [asr-role-audio-skiff](../sources/asr-role-audio-skiff.md) (ASR, Tier D listening notes): "screechy" until heavily EQ'd; bass upsets it; not recommended.

## User reviews
No owner reports found; ASR replies (about 5 members) mostly question the price and the measured response ([users-role-audio-skiff](../sources/users-role-audio-skiff.md)); about 4 members remarked on a crooked blank serial label on the reviewed sample (cosmetic, one sample). Anecdotal.

## Conflicts
- Sensitivity: 80.6 dB measured (a forum member computed 81.1 dB) vs 88 dB claimed; about 7 dB lower.
- Bass extension: f3 143 / f6 126 Hz vs maker 90 Hz-20 kHz (or 125 Hz at -6 dB, depending on page).
- Critics (2006 Enjoy the Music; Bound for Sound hosted by the maker) describe a linear response, whereas ASR measured four strong resonances.
- Status: the maker's price list is live but main-site and Amazon availability could not be verified; ASR (2023) says it is still sold.

## Related
[Role Audio](../brands/role-audio.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md) · [sensitivity-normalization](../concepts/sensitivity-normalization.md)
