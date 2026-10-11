---
type: speaker
brand: Paradigm
model: Founder 40B
slug: paradigm-founder-40b
status: current
price_usd_pair: 2399.98
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.5
min_impedance_hz: 200
impedance_flag: effectively-4ohm
epdr_min_ohm: 1.8
sensitivity_db_2v83: 87.2
sensitivity_claimed_db: 89.0
f3_hz: 70
f6_hz: 53
lw_deviation_db: null
on_axis_deviation_db: null
hor_beamwidth_deg: null
ver_beamwidth_deg: null
di_smoothness: null
crossover_hz: 1600
max_spl_db: null
thd_86db_pct: 0.4
thd_96db_pct: 1.0
pref_score: 4.9
pref_score_sub: 7.1
woofer_in: 6
tweeter_type: dome
port: rear
dimensions_mm: 368x197x320
weight_kg: 11.3
critic_consensus: Praised for imaging, soundstage, dynamics and surprising bass for size; minor notes of midband cuppiness, forward highs and a low impedance.
user_consensus: null
sources: [mfr-paradigm-founder-40b, eac-paradigm-founder-40b, whathifi-paradigm-founder-40b, audiophilia-paradigm-founder-40b, stereonet-paradigm-founder-40b, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "±2 dB 69 Hz-23 kHz on-axis; 41 Hz (DIN)"
primary_measurement: eac-paradigm-founder-40b
measurement_count: 2
image_url: "https://www.paradigm.com/3592-large_default/founder-40b.jpg"
---
<!-- photo -->
<img src="https://www.paradigm.com/3592-large_default/founder-40b.jpg" alt="Paradigm Founder 40B" width="360">

*Photo: [paradigm.com](https://www.paradigm.com/en/passive/founder-40b) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Paradigm Founder 40B is a 2-way ported standmount with a 6" AL-MAG woofer and a 1" ceramic-coated dome in a large waveguide, priced at $1,199.99 each ($2,399.98 per pair). Paradigm rates it "compatible with 8 ohms" ([mfr-paradigm-founder-40b](../sources/mfr-paradigm-founder-40b.md)), but Erin measured a 3.5 Ω minimum with a 1.8 Ω EPDR, so it is flagged `effectively-4ohm`. Klippel data show wide, constant directivity, an upward-tilting on-axis treble and modest bass (f3 about 70 Hz), with low distortion and little compression. It suits small-to-medium rooms with a sub and an amplifier comfortable at 4 Ω.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 87.2 dB (average) | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) via [spinorama-org](../sources/spinorama-org.md) | A | 300 Hz-3 kHz average; graph also reads ~88 dB |
| Sensitivity | 88.5 dB | [whathifi-paradigm-founder-40b](../sources/whathifi-paradigm-founder-40b.md) | B | Newport Test Labs; claimed 89 dB anechoic |
| f3 / f6 | 70 / 53 Hz (modest) | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) via [spinorama-org](../sources/spinorama-org.md) | A | reported by spinorama.org (30° dataset page); consistent with graph |
| Frequency response | 75 Hz-23 kHz ±4 dB | [whathifi-paradigm-founder-40b](../sources/whathifi-paradigm-founder-40b.md) | B | in-room LF spliced to anechoic HF |
| Listening-window deviation | not computed; 1.7 dB over 300 Hz-5 kHz | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) via [spinorama-org](../sources/spinorama-org.md) | A | band differs from §7 standard, so not entered in frontmatter |
| Min impedance | 3.5 Ω above 80 Hz (~200 Hz) | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) | A | plot annotation; frequency graph-read |
| Min impedance | ~3.1 Ω @ ~210 Hz | [whathifi-paradigm-founder-40b](../sources/whathifi-paradigm-founder-40b.md) | B | lab text |
| EPDR (min) | 1.8 Ω above 80 Hz | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) | A | plot annotation |
| THD 86 dB | ~0.4 % worst case, near 100 Hz (clean) | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) | A | graph-read (approx.) |
| THD 96 dB | ~1.0 % worst case, near 120 Hz | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) | A | graph-read (approx.) |
| Preference score | 4.9 (no sub) / 7.1 (with sub) | [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) via [spinorama-org](../sources/spinorama-org.md) | A | not meaningful to <0.5 |
| Crossover | 1.6 kHz claimed; ~2.8 kHz electrical measured | [mfr-paradigm-founder-40b](../sources/mfr-paradigm-founder-40b.md); [whathifi-paradigm-founder-40b](../sources/whathifi-paradigm-founder-40b.md) | C / B | |

## Directivity
Reported as constant-directivity with wide dispersion; Erin says the upward-tilted on-axis treble remains in room even off-axis, and that the maker recommends listening 30° off-axis (data published at both 0° and 30°). Beamwidth, DI smoothness and early-reflection dip were not computed (no raw spinorama export). The CEA2034 plot shows the listening window rising from about 88 dB near 1 kHz to about 90 dB at 4-6 kHz and the early-reflection curve falling gradually, a smooth DI. In a room without close side walls Erin found best results aiming the speaker straight ahead, which implies little toe-in. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's THD at 86 dB is about 0.4 % at worst between 100 Hz and 10 kHz and about 1.0 % at 96 dB (graph-read, approx.), with 2nd and 3rd harmonics dominating the bass. Swept compression versus 76 dB reference stays within about 0.7 dB at 102 dB @1 m above 100 Hz, with about 1.6 dB enhancement near 52 Hz and 1.1 dB compression at 40 Hz. No compression reached 3 dB at the tested ceiling, so no max SPL is entered. Capable of loud listening in small-to-medium rooms; bass limits arrive first. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Measured minimum 3.5 Ω (Erin) / 3.1 Ω (NTL) between ~190 and 500 Hz, EPDR minimum 1.8 Ω, and a 33 Ω peak near 2.7 kHz. That is below 4 Ω, so the 8 Ω-compatible rating overstates it and the IEC nominal would be 4 Ω (NTL). NTL says phase is benign over the low-impedance band. Use an amplifier stable into 4 Ω with good current; Paradigm suggests 15-150 W. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [whathifi-paradigm-founder-40b](../sources/whathifi-paradigm-founder-40b.md) (What Hi-Fi? reprint of Australian Hi-Fi): uncoloured monitor-like sound, great imaging, surprising bass; lab report positive, lowish impedance noted.
- [stereonet-paradigm-founder-40b](../sources/stereonet-paradigm-founder-40b.md) (StereoNET): punchy, fast, pin-sharp imaging; slight midband cuppiness and warm bass.
- [audiophilia-paradigm-founder-40b](../sources/audiophilia-paradigm-founder-40b.md) (Audiophilia): imaging and soundstage standout, easy to drive; recommended.
- [eac-paradigm-founder-40b](../sources/eac-paradigm-founder-40b.md) (Erin, Tier D notes): good tonality in a large room away from side walls, but needs EQ to tame treble; better with a sub.

## User reviews
No user reports ingested yet (the one Audioholics forum thread found is a purchase question, and the Steve Hoffman forum blocked scripted access).

## Conflicts
- Sensitivity: 87.2 dB (EAC via spinorama.org) vs 88.5 dB (NTL, Tier B) vs 89 dB claimed (unit unstated); difference 1.3 dB. A comparison site quoted 85.9 dB for the same Erin data, which was not verified.
- Min impedance: 3.5 Ω (EAC) vs 3.1 Ω (NTL), within 0.5 Ω; both below 4 Ω, contradicting the "8 ohms" compatibility wording.
- Frequency response: claimed ±2 dB 69 Hz-23 kHz vs NTL ±4 dB 75 Hz-23 kHz; the Klippel on-axis rises ~3 dB in the treble.
- Crossover: 1.6 kHz claimed vs ~2.8 kHz measured electrically by NTL.
- Preference score: 4.89 on the page fetched; a search summary showed 4.99/7.22; used the fetched value.
- spinorama.org lists the 40B as "passive center"; it is a standmount per maker and all reviews.

## Related
[Paradigm](../brands/paradigm.md) · [Paradigm Monitor SE Atom](paradigm-monitor-se-atom.md) · [Paradigm Persona B](paradigm-persona-b.md) · KEF R3 Meta · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
