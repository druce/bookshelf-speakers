---
type: speaker
brand: SVS
model: Prime Bookshelf
slug: svs-prime-bookshelf
category: bookshelf
status: current
price_usd_pair: 699
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.9
min_impedance_hz: 200
impedance_flag: effectively-4ohm
epdr_min_ohm: 2.2
sensitivity_db_2v83: 86.6
sensitivity_claimed_db: 87.0
f3_hz: 70
f6_hz: 58
lw_deviation_db: 2.3
on_axis_deviation_db: 2.6
hor_beamwidth_deg: 144
ver_beamwidth_deg: 115
di_smoothness: minor-discontinuity
crossover_hz: 2300
max_spl_db: null
thd_86db_pct: 0.7
thd_96db_pct: 1.3
pref_score: 5.2
pref_score_sub: 7.8
woofer_in: 6.5
tweeter_type: dome
port: rear
dimensions_mm: 335x203x239
weight_kg: 7.0
critic_consensus: Enthusiast and system reviews found it detailed, well imaged and easy to drive, with a hint of treble emphasis and limited bass below about 48 Hz; Erin found the midrange forward.
user_consensus: "Crutchfield (n=36, 97% 5★, brand-loyal sample): praised clarity and bass for the size; 4 advise a sub; no failures reported."
sources: [eac-svs-prime-bookshelf, mfr-svs-prime-bookshelf, pooraudiophile-svs-prime-bookshelf, soundstageaccess-svs-prime-bookshelf, users-svs-prime-bookshelf, spinorama-org, crutchfield-svs-prime-bookshelf]
last_updated: 2026-10-11
claimed_fr: "48 Hz-25 kHz (+/-3 dB)"
primary_measurement: eac-svs-prime-bookshelf
measurement_count: 1
image_url: "https://www.svsound.com/cdn/shop/files/prime-bookshelf-ba.png?v=1700854540"
---
<!-- photo -->
<img src="https://www.svsound.com/cdn/shop/files/prime-bookshelf-ba.png?v=1700854540" alt="SVS Prime Bookshelf" width="360">

*Photo: [svsound.com](https://www.svsound.com/products/prime-bookshelf) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The SVS Prime Bookshelf is an 8 ohm, ported two-way standmount with a 6.5" woofer and 1" aluminium dome, sold direct and via dealers at about $699 per pair. On Erin's Klippel it shows a good listening window (+/-2.3 dB) and wide directivity, but a forward 1-2 kHz midrange, bright on-axis treble and a measured f3 of 70 Hz, well above the 48 Hz claim. Its impedance falls to 3.9 ohm (flag: `effectively-4ohm`), so the 8 ohm label is optimistic. Suits someone wanting a well-built, wide-dispersion speaker with a sub or EQ.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 86.6 dB (average) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | computed (scripts/cta2034.py v2); claimed 87 dB |
| Listening-window deviation | +/-2.3 dB, 300 Hz-10 kHz (good) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | computed |
| On-axis deviation | +/-2.6 dB | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | computed |
| f3 / f6 | 70 / 58 Hz (modest) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | computed; anechoic, no room gain |
| Min impedance | 3.9 ohm near 200 Hz (above 80 Hz) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | value stated; frequency graph-read (approx.) |
| Min EPDR | 2.2 ohm (above 80 Hz) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | stated on graph |
| THD @ 86 dB / 1 m | about 0.7% max, 100 Hz-10 kHz | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | graph-read (approx.) |
| THD @ 96 dB / 1 m | about 1.3% max; narrow 2.5% peak near 250 Hz | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) | A | graph-read (approx.) |
| Preference score | 5.2 (no sub) / 7.8 (with sub) | [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid; ignores distortion and output |
| Crossover | 2.3 kHz | [mfr-svs-prime-bookshelf](../sources/mfr-svs-prime-bookshelf.md) | C | |

## Directivity
Horizontal -6 dB beamwidth about 144 deg and vertical about 115 deg (wide). DI is a minor discontinuity (ERDI residual 1.7 dB); SPDI rises from 5.6 dB at 1 kHz to 7.8 dB at 10 kHz. Early-reflection dip near 1.5 kHz is only 0.9 dB (no flag). Erin saw a horizontal diffraction dip at 3-5 kHz and more serious vertical issues from driver spacing; width is about +/-70-80 deg until beaming above about 8 kHz. On-axis minus listening window above 4 kHz is +0.3 dB, so either aim works by the numbers, though Erin found the highs brighter on-axis and preferred about 30 deg toe-out of axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Erin's THD is about 0.7% at 86 dB and about 1.3% at 96 dB across 100 Hz-10 kHz (graph-read), with a narrow 2.5% rise near 250 Hz at 96 dB, and rising quickly below about 60 Hz. In the 102 dB compression test loss was about 1.7 dB near 60 Hz and about 1 dB or less elsewhere, so no 3 dB limit was reached; max SPL is not stated. Erin called output good for the size. Fine for small-to-medium rooms; not a high-SPL bass speaker. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
8 ohm nominal, but 3.9 ohm minimum above 80 Hz and EPDR down to 2.2 ohm: a demanding load for its label, flagged `effectively-4ohm`. Phase stays within about +/-45 deg. Use an amplifier stable into 4 ohm; maker says 20-150 W. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [pooraudiophile-svs-prime-bookshelf](../sources/pooraudiophile-svs-prime-bookshelf.md) (Poor Audiophile blog, 2015): detailed, well imaged, drove easily from 50 W; reserved drum impact and extension below 48 Hz.
- [soundstageaccess-svs-prime-bookshelf](../sources/soundstageaccess-svs-prime-bookshelf.md) (SoundStage! Access, 2018, system review): hint of treble emphasis; bass lower than a Wharfedale Diamond 220; easy to drive.
- [eac-svs-prime-bookshelf](../sources/eac-svs-prime-bookshelf.md) (Erin's Audio Corner, Tier D notes): forward midrange and bright treble on-axis; good build and finish.

## User reviews
Crutchfield ([crutchfield-svs-prime-bookshelf](../sources/crutchfield-svs-prime-bookshelf.md); 36 reviews, 35 five-star, hand-tallied; likely brand-loyal sample, six own SVS subs): 15 of 36 praise clear, accurate sound; 8 of 36 say bass is good for the size, 4 of 36 light or sub advised; 3 of 36 praise the off-axis response, in line with the measured 144 degree beamwidth. Earlier: only a maker-hosted 4.9/5 over 175 reviews ([users-svs-prime-bookshelf](../sources/users-svs-prime-bookshelf.md)).

QC/reliability: no defects or failures in 36 reviews.

## Conflicts
- Bass extension: maker claims 48 Hz (+/-3 dB) vs measured f3 of 70 Hz (Tier A anechoic); delta 22 Hz. Maker method unstated; measured value used.
- Impedance: 8 ohm nominal vs 3.9 ohm minimum (about 39% below the 6.4 ohm IEC floor).
- Sensitivity: 87 dB claimed vs 86.6 dB computed; within 1 dB.
- Bass: 8 of 36 Crutchfield reviewers call bass good or tight for the size, versus measured f3 70 Hz against the 48 Hz claim; 4 of 36 advise a sub.

## Related
[SVS](../brands/svs.md) · [SVS Ultra Evolution Bookshelf](svs-ultra-evolution-bookshelf.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [impedance-and-epdr](../concepts/impedance-and-epdr.md) · [compression-and-max-spl](../concepts/compression-and-max-spl.md)
