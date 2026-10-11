---
type: speaker
brand: Totem Acoustic
model: Kin One
slug: totem-acoustic-kin-one
category: bookshelf
status: current
price_usd_pair: 599
price_checked: 2026-10-11
nominal_impedance_ohm: 6
min_impedance_ohm: 4.4
min_impedance_hz: 270
impedance_flag: below-iec
epdr_min_ohm: 2.6
sensitivity_db_2v83: 83.1
sensitivity_claimed_db: 89.0
f3_hz: 87
f6_hz: 68
lw_deviation_db: 2.3
on_axis_deviation_db: 2.3
hor_beamwidth_deg: 135
ver_beamwidth_deg: 112
di_smoothness: minor-discontinuity
crossover_hz: null
max_spl_db: null
thd_86db_pct: 1.7
thd_96db_pct: 3.5
pref_score: 3.7
pref_score_sub: 6.6
woofer_in: 4
tweeter_type: dome
port: null
dimensions_mm: 243x127x159
weight_kg: 2.8
critic_consensus: Praised for imaging and rhythm for its size; caveats are a slightly bright upper midrange and the need for a subwoofer and limited loudness in larger rooms (one review, with Kin Amp).
user_consensus: null
sources: [eac-totem-acoustic-kin-one, soundstageaccess-totem-acoustic-kin-one-summary, mfr-totem-acoustic-kin-one, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "65 Hz - 22 kHz ±3 dB (when properly placed)"
primary_measurement: eac-totem-acoustic-kin-one
measurement_count: 1
image_url: "https://totemacoustic.com/wp-content/uploads/2024/08/Totem-KIN-ONE-Satin-White-02a.webp"
---
<!-- photo -->
<img src="https://totemacoustic.com/wp-content/uploads/2024/08/Totem-KIN-ONE-Satin-White-02a.webp" alt="Totem Acoustic Kin One" width="360">

*Photo: [totemacoustic.com](https://totemacoustic.com/product/kin-one/) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Totem Kin One is a very small (about 24 cm tall) two-way with a 4" cone and 1" soft dome, rated 6 Ω and sold at about $599 per pair. On Erin's Klippel it measures only moderately: listening window ±2.3 dB, f3 87 Hz, sensitivity 83.1 dB, and a preference score of 3.7 (6.6 with sub). It needs a subwoofer for any real bass and has limited output. It suits desktops and small rooms at modest levels, ideally with an amplifier that handles a dip to about 4.4 Ω.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 83.1 dB (low) | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | computed (scripts/cta2034.py v2); claimed 89 dB per [mfr-totem-acoustic-kin-one](../sources/mfr-totem-acoustic-kin-one.md) |
| Listening-window deviation | ±2.3 dB, 300 Hz-10 kHz (good) | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | computed (scripts/cta2034.py v2) |
| On-axis deviation | ±2.3 dB (good) | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | computed |
| f3 / f6 | 87 / 68 Hz (needs a sub) | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | computed; anechoic, no room gain |
| Min impedance | 4.4 Ω above 80 Hz, near 270 Hz | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | value from Erin's graph note; frequency graph-read (approx.) |
| Min EPDR | 2.6 Ω above 80 Hz | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | Erin's graph note |
| THD 86 dB @1 m | about 1.7% max, 100 Hz-10 kHz | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | graph-read (approx.); peak near 2 kHz |
| THD 96 dB @1 m | about 3.5% max, 100 Hz-10 kHz | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) | A | graph-read (approx.); peak near 2 kHz |
| Preference score | 3.7 (no sub) / 6.6 (with sub) | [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |

## Directivity
Horizontal -6 dB beamwidth about 135 degrees, vertical about 112 degrees. DI is classed as minor-discontinuity (ERDI residual 1.1 dB); SPDI rises from 2.9 dB at 1 kHz to 8.6 dB at 10 kHz, so directivity at the crossover region is low and widens late. Early-reflection dip near 1.5 kHz is 0.8 dB, well under the 3 dB flag. On-axis minus listening window above 4 kHz is +0.9 dB, so either aim works; Erin's summary mentions a mid-range dip and treble roll-off. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Graph-read THD at 86 dB is about 1.1% near 100 Hz and about 1.7% at a 2 kHz peak; at 96 dB it is about 2% near 100 Hz and about 3.5% at 2-3 kHz, above the 3% note threshold. Erin's compression test (re 76 dB) shows roughly 1 dB or less at 96 dB above 70 Hz but about 1.8 dB near 75 Hz and over 3 dB around 180-230 Hz at 102 dB. No max SPL is stated. Fine for small rooms at moderate levels; SoundStage! Access found it strained at loud levels in a large room. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Rated 6 Ω; measured minimum 4.4 Ω above 80 Hz is below the IEC 80% floor (4.8 Ω), so flagged `below-iec`. EPDR minimum 2.6 Ω with phase within about ±45 degrees: an amplifier stable into 4 Ω is advisable, though the 83 dB sensitivity means volume demands more power than the 89 dB claim suggests. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [soundstageaccess-totem-acoustic-kin-one-summary](../sources/soundstageaccess-totem-acoustic-kin-one-summary.md) (SoundStage! Access, Thom Moon, with Kin Amp): a little bright at times, bass needs a sub, broad stable imaging, strains loudly in a large room; overall very listenable.
- [eac-totem-acoustic-kin-one](../sources/eac-totem-acoustic-kin-one.md) (Erin's Audio Corner, Tier D notes): sounds big for its size, mid-range dip and treble roll-off may call for EQ; place about 12 in from the wall.

## User reviews
No user reports ingested yet.

## Conflicts
- Sensitivity: claimed 89 dB ([mfr-totem-acoustic-kin-one](../sources/mfr-totem-acoustic-kin-one.md)) vs 83.1 dB computed (about 83.4 dB in Erin's video summary): a delta of about 6 dB; the measurement is used.
- Nominal impedance 6 Ω vs measured 4.4 Ω minimum: below-iec flag.
- Price: maker lists $599; The Music Room shows $703.83.

## Related
[Totem Acoustic](../brands/totem-acoustic.md) · [Totem Acoustic Bison Monitor](totem-acoustic-bison-monitor.md) · Totem Acoustic Loon Monitor · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
