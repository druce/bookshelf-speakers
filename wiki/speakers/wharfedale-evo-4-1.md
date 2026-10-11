---
type: speaker
brand: Wharfedale
model: EVO 4.1
slug: wharfedale-evo-4-1
status: current
price_usd_pair: 649
price_checked: 2026-10-11
nominal_impedance_ohm: 8
min_impedance_ohm: 3.2
min_impedance_hz: 250
impedance_flag: effectively-4ohm
epdr_min_ohm: null
sensitivity_db_2v83: 85.9
sensitivity_claimed_db: 87.0
f3_hz: 74
f6_hz: 46
lw_deviation_db: 2.5
on_axis_deviation_db: 2.7
hor_beamwidth_deg: 133
ver_beamwidth_deg: 62
di_smoothness: minor-discontinuity
crossover_hz: 2900
max_spl_db: null
thd_86db_pct: null
thd_96db_pct: null
pref_score: 4.5
pref_score_sub: 6.6
woofer_in: 5
tweeter_type: AMT
port: rear
dimensions_mm: 335x211x284
weight_kg: 7.8
critic_consensus: Only ASR (Tier D listening) reviewed; found bright, forward treble from a tweeter resonance and did not recommend it.
user_consensus: null
sources: [asr-wharfedale-evo-4-1, mfr-wharfedale-evo-4-1, users-wharfedale-evo-4-1, spinorama-org]
last_updated: 2026-10-11
claimed_fr: "64 Hz-22 kHz (±3 dB); 55 Hz at -6 dB"
primary_measurement: asr-wharfedale-evo-4-1
measurement_count: 1
image_url: "https://www.wharfedaleusa.com/cdn/shop/products/EVO4.1_Standard_Black_3_grande.png?v=1605120868"
---
<!-- photo -->
<img src="https://www.wharfedaleusa.com/cdn/shop/products/EVO4.1_Standard_Black_3_grande.png?v=1605120868" alt="Wharfedale EVO 4.1" width="360">

*Photo: [wharfedaleusa.com](https://www.wharfedaleusa.com/products/evo4-1-bookshelf-speaker) product image, linked rather than hosted here; checked 2026-10-11.*
<!-- /photo -->

## Summary
The Wharfedale EVO 4.1 is a 5" Kevlar-woofer, AMT-tweeter two-way standmount rated "8 Ω compatible" by the maker. On ASR's Klippel it shows a shelved-down bass, a broad tweeter resonance near 3.8 kHz, and strong upper-treble beaming, giving a listening window of ±2.5 dB and a preference score of 4.5. Impedance dips to 3.2 Ω, so it is effectively a 4 Ω load. ASR did not recommend it; suits only buyers who value its cabinet finish and will EQ or accept a forward treble.

## Measurements
| Metric | Value | Source | Tier | Note |
|---|---|---|---|---|
| Sensitivity (2.83 V/1 m) | 85.9 dB (average) | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) | A | computed (scripts/cta2034.py v2); claimed 87 dB per [mfr-wharfedale-evo-4-1](../sources/mfr-wharfedale-evo-4-1.md) |
| Listening-window deviation | ±2.5 dB, 300 Hz-10 kHz (good, at the limit) | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) | A | computed |
| On-axis deviation | ±2.7 dB | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) | A | computed |
| f3 / f6 | 74 / 46 Hz (modest) | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) | A | computed; shelved bass |
| Min impedance | 3.2 Ω, broad minimum ~100-300 Hz | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) | A | stated on graph; frequency graph-read (approx.) |
| Preference score | 4.5 (no sub) / 6.6 (with sub) | [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) via [spinorama-org](../sources/spinorama-org.md) | A | coarse aid only |
| Crossover | 2.9 kHz | [mfr-wharfedale-evo-4-1](../sources/mfr-wharfedale-evo-4-1.md) | C | claimed |

## Directivity
Horizontal -6 dB beamwidth about 133°, vertical about 62° (tall AMT beams vertically). DI is minor-discontinuity (ERDI residual 1.3 dB); SPDI rises from 4.7 dB at 1 kHz to 10.7 dB at 10 kHz, i.e. upper-treble off-axis response drops quickly. Early-reflection dip near 1.5 kHz is 1.7 dB, under the 3 dB flag. On-axis minus listening window above 4 kHz is +1.0 dB, borderline: slightly less toe-in is reasonable, though ASR found the response about 10° off tweeter axis slightly smoother. See [directivity-index](../concepts/directivity-index.md), [early-reflections](../concepts/early-reflections.md).

## Output & distortion
No compression or max-SPL test; maker claims 104 dB peak (unverified). ASR's THD plots are in dB, so no % values are entered. At 86 dB ASR labelled it "Good" (THD peaks near 100-150 Hz and around 2 kHz); at 96 dB ASR labelled it "Very unhappy", with heavy bass distortion and a 2-4 kHz rise tied to the tweeter resonance. ASR heard severe sub-bass distortion at medium-high levels and advises a high-pass filter. Best for small rooms at moderate levels. See [compression-and-max-spl](../concepts/compression-and-max-spl.md).

## Amplifier load
Maker says "8 Ω compatible", min 3.5 Ω claimed. ASR shows 3.2 Ω minimum (flag `effectively-4ohm`), a broad dip across 100-300 Hz, a ~18.6 Ω peak near 80 Hz, and phase swinging roughly ±40-50° (graph-read). EPDR not computed. Use an amplifier stable into 4 Ω. See [impedance-and-epdr](../concepts/impedance-and-epdr.md).

## Critic reviews
- [asr-wharfedale-evo-4-1](../sources/asr-wharfedale-evo-4-1.md) (ASR, Tier D listening): untreated sound was hyper-detailed and bright, vocals unnaturally forward; EQ did not make it enjoyable; preferred the Revel M16; not recommended.
No other professional review of this model was found.

## User reviews
Six owner reports, anecdotal ([users-wharfedale-evo-4-1](../sources/users-wharfedale-evo-4-1.md)): 5 positive (3 are incentivised Best Buy reviews), 1 finds vocals dull/boxed in. No QC problems reported.

## Conflicts
- Sensitivity: 85.9 dB computed vs 86.3 dB (MZKM, ASR thread) vs 87 dB claimed; within ~1 dB.
- Preference score: 4.5/6.6 (spinorama.org) vs 4.8/6.8 (ASR thread post); used spinorama.org figure.
- Bass: claimed 64 Hz (±3 dB) and 55 Hz (-6 dB) vs measured f3 74 Hz, f6 46 Hz; shelved response complicates the comparison.
- Minimum impedance: claimed 3.5 Ω vs measured 3.2 Ω; consistent.
- Port type: ASR says a downward-firing passive radiator; the maker describes a slot-loaded profiled port at the base. Recorded as `rear` (down-firing).
- Price: $649 at maker-direct (list $799); Crutchfield snippet showed $699, not verified live.

## Related
[Wharfedale](../brands/wharfedale.md) · Wharfedale Linton 85th Anniversary · [Revel M16](revel-m16.md) · [spinorama](../concepts/spinorama.md) · [preference-score](../concepts/preference-score.md)
