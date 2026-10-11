---
type: speaker
brand: ATC
model: SCM19
slug: atc-scm19
status: current
price_usd_pair: 3749
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 5.6
min_impedance_hz: 150
impedance_flag: below-iec
epdr_min_ohm: null
sensitivity_db_2v83: 83.0
sensitivity_claimed_db: 85.0
f3_hz: 52
f6_hz: 40
lw_deviation_db: null
on_axis_deviation_db: 2.4
hor_beamwidth_deg: null
ver_beamwidth_deg: null
di_smoothness: null
crossover_hz: 2500
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: null
pref_score_sub: null
woofer_in: 6.0
tweeter_type: dome
port: sealed
dimensions_mm: 438x265x300
weight_kg: 17.8
critic_consensus: Praised for neutrality, dynamics, low-level resolution and tight sealed bass; caveats are no deep bass and a need for a powerful amp.
user_consensus: null
sources: [mfr-atc-scm19, avmentor-atc-scm19, tas-atc-scm19, soundstage-atc-scm19, stereotimes-atc-scm19, users-atc-scm19-2026-10-11]
last_updated: 2026-10-11
claimed_fr: "54 Hz-22 kHz (-6 dB)"
primary_measurement: avmentor-atc-scm19
measurement_count: 1
---

## Summary
The ATC SCM19 is an 8 Ω, sealed, two-way standmount with ATC's own 150 mm "SL" mid/bass driver and 25 mm soft-dome tweeter, hand-built in England. The only measurement found is a Tier-B lab page (AVMentor): low sensitivity around 83 dB, a 5.6 Ω impedance minimum, and wide, even horizontal dispersion with a reasonably smooth response. Critics emphasise neutrality, dynamics and bass quality over depth. It suits listeners with a strong, high-voltage amplifier who sit relatively close; the price is high for its bass extension. No Klippel/spinorama data exists.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | about 83.0 dB (average) | [avmentor-atc-scm19](../sources/avmentor-atc-scm19.md) | B | octave-step average 125 Hz-16 kHz; claimed 85 dB in [mfr-atc-scm19](../sources/mfr-atc-scm19.md) |
| Response deviation | ±2.4 dB summed on-axis | [avmentor-atc-scm19](../sources/avmentor-atc-scm19.md) | B | 1/3-oct smoothing, not CTA-2034 LW; entered as on-axis deviation (good) |
| f3 / f6 | 52 / 40 Hz | [avmentor-atc-scm19](../sources/avmentor-atc-scm19.md) | B | relative to its mid-band level; modest bass per §7 |
| Min impedance | 5.6 Ω @ about 150 Hz | [avmentor-atc-scm19](../sources/avmentor-atc-scm19.md) | B | text value; 50 Ω peak below 100 Hz |
| Phase | +47° to -57° | [avmentor-atc-scm19](../sources/avmentor-atc-scm19.md) | B | |
| Crossover | 2.5 kHz | [mfr-atc-scm19](../sources/mfr-atc-scm19.md) | C | |
| Preference score | not available | | | no spinorama data |

## Directivity
No beamwidth or DI figures. AVMentor reports horizontal response within 3 dB to 8 kHz for ±35°, narrowing above, so toe-in toward the listener is advised and close listening preferred. Vertical response is tight near the 2 kHz crossover: keep the listener at or slightly below tweeter height, not above (listening from below the axis is worse). See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No distortion or compression test found. ATC claims 108 dB max SPL (claimed only, Tier C). Critics report clean loud playback ([stereotimes-atc-scm19](../sources/stereotimes-atc-scm19.md), [soundstage-atc-scm19](../sources/soundstage-atc-scm19.md)), but sensitivity is low so it needs a powerful amp for loud levels in medium rooms. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
8 Ω nominal; measured minimum 5.6 Ω near 150 Hz with a small 13° phase there, so flagged `below-iec` (floor 6.4 Ω). Impedance rises to about 50 Ω below 100 Hz. Low sensitivity means it needs voltage swing more than current; ATC recommends 75-300 W. EPDR not computed. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [tas-atc-scm19](../sources/tas-atc-scm19.md) (The Absolute Sound, Neil Gader, 2014): neutral midband and treble, tight tuneful bass to the upper 40s Hz, "highest recommendation".
- [soundstage-atc-scm19](../sources/soundstage-atc-scm19.md) (SoundStage! Xperience, Wes Marshall, 2016): effortless dynamics, clean at high levels; slight opacity up top.
- [stereotimes-atc-scm19](../sources/stereotimes-atc-scm19.md) (Stereo Times, Allen Edelstein): solid "A", dynamically linear; wanted a bit more bass.

## User reviews
About 9 opinions from two What Hi-Fi? forum threads ([users-atc-scm19-2026-10-11](../sources/users-atc-scm19-2026-10-11.md)), so anecdotal: 3 praise sound/bass dynamics; 4 say it wants a capable amp, 2 call that a myth. No QC issues reported.

## Conflicts
- Sensitivity: about 83 dB measured (Tier B) vs 85 dB claimed; 2 dB lower, same direction as ATC's SCM7 results.
- Bass: AVMentor -6 dB at 40 Hz vs ATC claim of 54 Hz at -6 dB; single Tier-B source, unresolved.
- Revision: reviews cover earlier SCM19 generations ("v2" per SoundStage); ATC's current page and retailers list "SCM19"/"v2" without a clear revision history.
- Price: $3,749 (Sound Approach) vs $4,199 (The Music Room, Music Direct).

## Related
[ATC](../brands/atc.md) · [ATC SCM7](atc-scm7.md) · ATC SCM20PSL · ATC SCM11 · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [sensitivity-normalization](../concepts/sensitivity-normalization.md)
