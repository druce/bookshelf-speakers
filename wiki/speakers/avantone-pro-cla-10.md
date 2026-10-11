---
type: speaker
brand: Avantone Pro
model: CLA-10
slug: avantone-pro-cla-10
status: current
price_usd_pair: 699
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 6.8
min_impedance_hz: null
impedance_flag: null
epdr_min_ohm: null
sensitivity_db_2v83: 90.2
sensitivity_claimed_db: 90.0
f3_hz: 131
f6_hz: 95
lw_deviation_db: 2.8
on_axis_deviation_db: 3.3
hor_beamwidth_deg: 142
ver_beamwidth_deg: 110
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 2.2
pref_score_sub: 5.9
woofer_in: 7
tweeter_type: dome
port: sealed
dimensions_mm: 381.5x215x197.5
weight_kg: 6.3
critic_consensus: Studio-monitor critics find it a faithful NS-10 character (fast mids and bass) but brighter than the original and tiring; not recommended as a sole or neutral reference.
user_consensus: null
sources: [asr-avantone-pro-cla-10, mfr-avantone-pro-cla-10, musictech-avantone-pro-cla-10, soundonsound-avantone-pro-cla-10, users-avantone-pro-cla-10, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "60 Hz-20 kHz (no tolerance stated)"
primary_measurement: asr-avantone-pro-cla-10
measurement_count: 1
---

## Summary
The Avantone Pro CLA-10 Passive is an 8 Ω sealed two-way studio monitor (7" paper-cone woofer, 1.375" dome) built as a clone of the Yamaha NS-10M. On the ASR Klippel it measures poorly for home listening: listening window ±2.8 dB with a broad mid-to-treble boost, a narrow resonance near 3.5 kHz, large directivity error and f3 of 131 Hz. Preference score is 2.2 (5.9 with sub). It is a niche mixing tool for people who want the NS-10 character, not a neutral hi-fi speaker. Sensitivity is high (90.2 dB) and the load is easy.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 90.2 dB (high) | [[asr-avantone-pro-cla-10]] | A | computed (scripts/cta2034.py v2); claimed 90 dB per [[mfr-avantone-pro-cla-10]] |
| Listening-window deviation | ±2.8 dB, 300 Hz-10 kHz (good by number, but broad tilted boost) | [[asr-avantone-pro-cla-10]] | A | computed |
| On-axis deviation | ±3.3 dB | [[asr-avantone-pro-cla-10]] | A | computed |
| f3 / f6 | 131 / 95 Hz (needs a sub) | [[asr-avantone-pro-cla-10]] | A | computed; sealed alignment |
| LW dip above f3 | -3.1 dB @ 284 Hz | [[asr-avantone-pro-cla-10]] | A | computed |
| Min impedance | 6.8 Ω | [[asr-avantone-pro-cla-10]] | A | stated on ASR graph; frequency not marked |
| Impedance peak | ~33 Ω @ ~100 Hz | [[asr-avantone-pro-cla-10]] | A | graph-read (approx.) |
| Preference score | 2.2 (no sub) / 5.9 (with sub) | [[asr-avantone-pro-cla-10]] via [[spinorama-org]] | A | ignores distortion and max output |
| Narrow resonance | ~3.5 kHz | [[asr-avantone-pro-cla-10]] | A | not in near-field, so likely cabinet/diffraction rather than driver |
| Tested orientation | vertical | [[asr-avantone-pro-cla-10]] | A | see Directivity |

## Directivity
Horizontal -6 dB beamwidth about 142 degrees and vertical about 110 degrees, as tested with the speaker upright; DI has a minor discontinuity (ERDI residual 1.9 dB). SPDI rises from 5.7 dB at 1 kHz to 7.8 dB at 10 kHz. Early-reflection dip near 1.5 kHz is only 0.8 dB. ASR calls the directivity error large and says that laying the speaker on its side (the usual studio orientation) puts it in the horizontal plane, so upright is preferable. On-axis minus listening window above 4 kHz is +0.7 dB, so toe-in is not decisive; aiming at the listener is fine. ASR advises absorbing the nearby walls. See [[directivity-index]], [[early-reflections]].

## Output & distortion
No max-SPL test. ASR's THD plots (86 and 96 dB at 1 m, in dB not %) are described by the reviewer as very low bass distortion; at 96 dB, graph-read distortion in the mids and bass is roughly 2-3% (approx.), with "broad distortions" in the most sensitive region per ASR using relative THD. THD fields left null because no defensible % could be read. High sensitivity helps; the sealed 7" limits bass loudness. Suited to small rooms and nearfield use. See [[compression-and-max-spl]].

## Amplifier load
8 Ω nominal; ASR measured a 6.8 Ω minimum, above the IEC 80% floor of 6.4 Ω, so no flag. A sealed-box resonance peaks near 33 Ω at ~100 Hz; phase is moderate (about ±40 degrees). Easy load for any amplifier; the 60 W program rating means avoid very large amps at high gain. EPDR not computed. See [[impedance-and-epdr]].

## Critic reviews
- [[soundonsound-avantone-pro-cla-10]] (Sound On Sound, Phil Ward): "an NS-10 in all but name" but 3-4 dB brighter above 2.5 kHz and tiring; fast, accurate bass.
- [[musictech-avantone-pro-cla-10]] (MusicTech, John Pickford): fair NS10 recreation, but brighter than his originals; clean but limited bass; not a sole monitor.
- [[asr-avantone-pro-cla-10]] (ASR, Tier D listening notes): grungy and treble-heavy; still poor after EQ; not recommended.

## User reviews
Anecdotal ([[users-avantone-pro-cla-10]]): 3 written Thomann reviews (9 ratings, avg 4.9/5) all like the NS10-style sound for the price; about 5 ASR commenters (none stating ownership) call it brighter than or unlike the original. No QC problems reported; SOS notes push-on terminals.

## Conflicts
- Claimed 90 dB vs measured 90.2 dB: consistent.
- Claimed FR 60 Hz-20 kHz vs measured f3 131 / f6 95 Hz: spec has no tolerance and is not data.
- Preference score: 2.2 here vs 1.4 no-EQ posted by a forum member in the ASR thread; spinorama.org computation used.
- Fidelity as an "NS-10 clone": SOS finds bass and mids close but treble 3-4 dB hot; ASR argues the boost is greater than the original's.
- Availability: Sweetwater shows in stock at $699; zZounds only reserve/preorder and ProAudioDesign shows sold out.

## Related
[[avantone-pro]] · Yamaha NS-6490 · [[spinorama]] · [[preference-score]] · [[directivity-index]]
