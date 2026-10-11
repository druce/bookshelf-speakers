---
type: speaker
brand: Fluance
model: Reference XL8S
slug: fluance-reference-xl8s
category: bookshelf
status: current
price_usd_pair: 179.99
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 6.0
min_impedance_hz: null
impedance_flag: below-iec
epdr_min_ohm: 3.5
sensitivity_db_2v83: 85.0
sensitivity_claimed_db: 85.0
f3_hz: null
f6_hz: 60
lw_deviation_db: null
on_axis_deviation_db: null
hor_beamwidth_deg: null
ver_beamwidth_deg: null
di_smoothness: null
crossover_hz: 3100
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 3.5
pref_score_sub: 5.6
woofer_in: 5.25
tweeter_type: dome
port: front
dimensions_mm: 290x206x229
weight_kg: 5.2
critic_consensus: HomeTheaterHiFi praised value and clear mids; Archimago measured a non-flat, rough response between 1.5 and 8 kHz.
user_consensus: null
sources: [archimago-fluance-reference-xl8s, hometheaterhifi-fluance-reference-xl8s, mfr-fluance-reference-xl8s, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "50 Hz - 20 kHz (no tolerance)"
primary_measurement: archimago-fluance-reference-xl8s
measurement_count: 1
image_url: "https://www.fluance.com/media/catalog/product/cache/6517c62f5899ad6aa0ba23ceb3eeff97/x/l/xl8s-main-white_background-3000.jpg"
---
<!-- photo -->
<img src="https://www.fluance.com/media/catalog/product/cache/6517c62f5899ad6aa0ba23ceb3eeff97/x/l/xl8s-main-white_background-3000.jpg" alt="Fluance Reference XL8S" width="360">

*Photo: [fluance.com](https://www.fluance.com/reference-two-way-bookshelf-surround-speakers) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Fluance Reference XL8S is a $180-per-pair, 5.25" two-way with a 1" silk dome and dual front ports, rated "8 ohm compatible". Archimago's Tier-B qSpin shows a bumpy listening window (90 Hz, 1.2 kHz and 10 kHz accents, roughness at 1.5-8 kHz), roughly 60 Hz -6 dB bass, and modest preference scores. It is an easy load except for a 3.5 Ω EPDR dip near 150 Hz. Suits a desktop or small room with a sub, with caveats about stock: Fluance showed it out of stock.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | ~85 dB (average) | [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) | B | text, 500 Hz-7 kHz average |
| f6 | ~60 Hz (reviewer estimate) | [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) | B | maker claims 50 Hz without tolerance |
| Min impedance | ~6 Ω | [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) | B | text/graph-read (approx.) at 2-3 kHz |
| EPDR min | 3.5 Ω @ ~150 Hz | [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) | B | stated |
| Preference score | 3.5 (no sub) / 5.6 (with sub) | [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) via [spinorama-org](../sources/spinorama-org.md) | B | from digitized data; <0.5 not meaningful |
| LW deviation, f3, beamwidth | not computed | | | no numeric export |
| Crossover | 3.1 kHz | [mfr-fluance-reference-xl8s](../sources/mfr-fluance-reference-xl8s.md) | C | |

## Directivity
No numeric beamwidth. Archimago reports DI bouncing around and dipping near 6 kHz as dispersion widens, then narrowing toward 20 kHz (tweeter beaming). Crossover at 3.1 kHz coincides with a vertical dip near 0°; stay within ±30° horizontally and sit at or slightly below tweeter axis. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
Archimago: THD at about 85 dB stays low (-40 dB = 1%, mostly 3rd harmonic); dynamic linearity within ±1 dB for 70-100 dB bursts; IMD at or below 1% through 80 dB but rising noticeably at 90 dB. No max-SPL test; best at moderate levels in small rooms. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Impedance minimum about 6 Ω (below the IEC 6.4 Ω floor, so flagged `below-iec`, approximate), box resonance 54 Hz, EPDR dips to 3.5 Ω near 150 Hz; Archimago calls it not challenging for modern amps. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [archimago-fluance-reference-xl8s](../sources/archimago-fluance-reference-xl8s.md) (Archimago, measurements): rough 1.5-8 kHz, three accentuations, more resonant than KEF LS50 and Edifier S2000 Mk III.
- [hometheaterhifi-fluance-reference-xl8s](../sources/hometheaterhifi-fluance-reference-xl8s.md) (HomeTheaterHiFi): lush mids, crisp highs, wide stage; limited bass, wants a sub.

## User reviews
No user reports ingested yet.

## Conflicts
- Bass: maker claims 50 Hz; Archimago estimates ~60 Hz at -6 dB.
- Impedance: "8 ohm compatible" claim vs ~6 Ω minimum (below IEC floor) and 3.5 Ω EPDR.
- Status: Fluance US shows Out of Stock; Newegg Business lists $179.99 (cached, stock unverified).
- Duplicate: lineup packet `fluance-reference-2-way-bookshelf` is this same product.

## Related
[Fluance](../brands/fluance.md) · [Fluance HFS Signature](fluance-hfs-signature.md) · [Polk Audio T15](polk-audio-t15.md) · Dayton Audio B652-AIR · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
