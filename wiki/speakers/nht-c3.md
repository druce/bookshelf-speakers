---
type: speaker
brand: NHT
model: C3
slug: nht-c3
status: current
price_usd_pair: 1250
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 4.2
min_impedance_hz: 150
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 83.1
sensitivity_claimed_db: 87.0
f3_hz: 61
f6_hz: 52
lw_deviation_db: 1.8
on_axis_deviation_db: 2.1
hor_beamwidth_deg: 145
ver_beamwidth_deg: 111
di_smoothness: minor-discontinuity
crossover_hz: 4750
max_spl_db: null
thd_86db_pct: 0.4
thd_96db_pct: null
pref_score: 4.5
pref_score_sub: 6.9
woofer_in: 6.5
tweeter_type: dome
port: sealed
dimensions_mm: 349x191x257
weight_kg: 7.3
critic_consensus: Clear, neutral, fast and well imaged with excellent dispersion, but lean bass that wants a subwoofer; treble can run hot.
user_consensus: null
sources: [asr-nht-c3, hometheaterhifi-nht-c3, soundstage-nht-c3, mfr-nht-c3, users-nht-c3, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "45 Hz-20 kHz (no tolerance stated)"
primary_measurement: asr-nht-c3
measurement_count: 2
---

## Summary
The NHT C3 is a 6 Ω, sealed three-way standmount with a 6.5" aluminium woofer, 2" dome midrange and 1" dome tweeter, sold singly by NHT at $624.99 each. On ASR's Klippel it shows good directivity and very low distortion at 86 dB, but an uneven, elevated on-axis response and low sensitivity (83.1 dB). A second Tier-B bench review found it far flatter. Bass is sealed and modest (f3 61 Hz), so it suits a subwoofer-assisted system and needs an amplifier that is stable into about 4 Ω.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.1 dB (low) | [asr-nht-c3](../sources/asr-nht-c3.md) | A | computed (scripts/cta2034.py v2); reviewer says 82-83 dB midrange |
| Listening-window deviation | ±1.8 dB, 300 Hz-10 kHz (good) | [asr-nht-c3](../sources/asr-nht-c3.md) | A | computed |
| LW (CEA-2034A) | "one of the tightest" seen, no figure | [hometheaterhifi-nht-c3](../sources/hometheaterhifi-nht-c3.md) | B | outdoor measurement |
| On-axis deviation | ±2.1 dB (good) | [asr-nht-c3](../sources/asr-nht-c3.md) | A | computed; reviewer calls it wavy |
| f3 / f6 | 61 / 52 Hz (modest) | [asr-nht-c3](../sources/asr-nht-c3.md) | A | computed |
| f3 | about 65 Hz | [hometheaterhifi-nht-c3](../sources/hometheaterhifi-nht-c3.md) | B | outdoor, 12 dB/oct sealed rolloff |
| Min impedance | 4.2 Ω @ about 150 Hz | [asr-nht-c3](../sources/asr-nht-c3.md) | A | graph-read (approx.); IEC floor for 6 Ω is 4.8 Ω |
| Min impedance | just under 4 Ω, 100-200 Hz | [hometheaterhifi-nht-c3](../sources/hometheaterhifi-nht-c3.md) | B | stated, two samples |
| THD at 86 dB | about 0.4% above 100 Hz (clean); narrow spike about 0.85% near 4.2 kHz | [asr-nht-c3](../sources/asr-nht-c3.md) | A | graph-read (approx.) |
| THD at 96 dB | not entered; about 1-1.8% broad, rising past 5% above about 7 kHz | [asr-nht-c3](../sources/asr-nht-c3.md) | A | graph-read (approx.); text says 94 dB |
| Preference score | 4.5 (no sub) / 6.9 (with sub) | [asr-nht-c3](../sources/asr-nht-c3.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |
| Crossover | 817 Hz / 4750 Hz | [hometheaterhifi-nht-c3](../sources/hometheaterhifi-nht-c3.md) | B | maker figures via reviewer |

## Directivity
Horizontal -6 dB beamwidth about 145°, vertical about 111°; ASR credits the dome midrange for the good directivity, while Secrets measured about 120° coverage to 7 kHz narrowing to 60° in the top octave (different definition). DI is a minor discontinuity (ERDI residual 1.5 dB) and the early-reflection dip near 1.5 kHz is 2.4 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.7 dB, so either aim works on this data, though ASR found the highs overdone and Secrets preferred about 21° toe-in; ASR advises tilting it down if mounted high. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
ASR's Klippel plot shows professional-monitor-level THD at 86 dB (about 0.4% above 100 Hz) but a break-down at 96 dB, especially the tweeter above about 7 kHz (beyond 5%), which ASR said exceeds its threshold; he noted EQ cutting the elevated highs would reduce that. No max-SPL or compression test exists. Fine for moderate levels in small to medium rooms; not for loud listening. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
6 Ω nominal; ASR measured a 4.2 Ω minimum around 150 Hz with high impedance peaks near 65 Hz and 1 kHz, below the IEC 80% floor of 4.8 Ω, so flagged `below-iec`. Secrets reported a similar curve and called it not difficult to drive. Low sensitivity means ASR advises more than 50 W. EPDR not computed. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [hometheaterhifi-nht-c3](../sources/hometheaterhifi-nht-c3.md) (Secrets, Best of 2018): clear, neutral, slightly midrange-forward; superb measured flatness; needs subwoofers for bass.
- [soundstage-nht-c3](../sources/soundstage-nht-c3.md) (SoundStage! Access, Carbon Fiber version): laser-like imaging and speed; lean bass; solid performer.
- [asr-nht-c3](../sources/asr-nht-c3.md) (ASR, Tier D listening): bright without EQ, good dynamics, bass a little light; recommended only with EQ.

## User reviews
Only 2 owner comments found, so anecdotal ([users-nht-c3](../sources/users-nht-c3.md)): both like the sealed bass; one uses it near walls because there is no port. One report that ASR's sample may have been damaged; no other QC issues.

## Conflicts
- Frequency response: ASR (Klippel, one sample) found a wavy, bright on-axis response and a midrange dip, possibly from a dented midrange driver; Secrets (outdoor, two samples) found it "superbly flat". Unresolved; ASR noted a re-measure with a replacement was expected.
- Sensitivity: 83.1 dB measured vs 87 dB claimed ([mfr-nht-c3](../sources/mfr-nht-c3.md)); ASR says 87 dB holds only at the tweeter peak.
- f3 61 Hz (ASR) vs 65 Hz (Secrets): within 5 Hz. Min impedance 4.2 Ω vs just under 4 Ω: within 0.5 Ω.
- Claimed 45 Hz-20 kHz (no tolerance) and "down to 40 Hz" vs measured f3 61 Hz.
- Price: ASR cites $391 each on Amazon in 2021; maker store lists $624.99 each now; Secrets quoted $499 each MSRP in 2018.

## Related
[NHT](../brands/nht.md) · [NHT Super Zero 2.1](nht-super-zero-2-1.md) · [Revel M16](revel-m16.md) · KEF Q150 · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
