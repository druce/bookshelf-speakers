---
type: source
slug: asr-salk-wow1
title: "Salk WoW1 Bookshelf Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/salk-wow1-bookshelf-speaker-review.14842/
author: amirm
outlet: Audio Science Review
published: 2020-07-21
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-salk-wow1.md
raw_data: raw/spinorama/Salk WoW1/asr/
assets: [raw/assets/asr-salk-wow1-impedance.png, raw/assets/asr-salk-wow1-thd.png, raw/assets/asr-salk-wow1-thd-rel.png]
speakers: [salk-wow1]
---
# ASR: Salk WoW1 review (2020-07-21)

## Summary
Klippel NFS measurement of a custom-finished WoW1 ordered by a member and drop-shipped to Amir. He found very low efficiency, a pronounced 500-700 Hz dip he traces to the port response dropping, directivity error at the crossover, very high bass distortion, and a tweeter that gets unhappy at 96 dB. He could not recommend it without EQ (40 Hz high-pass and a fix for the upper-bass dip).

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 78.2 dB | computed, scripts/cta2034.py v2 from raw Klippel export; spinorama.org lists 78.5 dB (300 Hz-3 kHz); maker claims 82 dB |
| lw_deviation_db | ±3.1 dB | computed, 300 Hz-10 kHz |
| on_axis_deviation_db | ±3.3 dB | computed |
| f3_hz / f6_hz | 54 / 46 Hz | computed |
| hor / ver beamwidth | 154° / 116° | computed |
| di_smoothness | minor-discontinuity (ERDI residual 2.0 dB) | computed |
| er_dip_1_5khz_db | 1.8 dB | computed |
| on_minus_lw_4_10k_db | +0.3 dB | computed |
| spdi 1 kHz / 10 kHz | 5.1 / 6.3 dB | computed |
| pref_score / with sub | 4.39 / 6.59 | spinorama.org computation |
| min_impedance_ohm | about 3.3 Ω around 4-5 kHz (about 4.3 Ω at 20 kHz) | graph-read (approx.); the graph's own annotation says "Min impedance = 6.5 in bass", which is the DC-region value, not the band minimum |
| impedance peaks | about 22 Ω near 30 Hz, 25 Ω near 75 Hz, 27 Ω near 900 Hz; about 6.9 Ω near 180 Hz | graph-read (approx.) |
| thd_86 | about 2.2% near 100 Hz, 1.4% near 120-130 Hz, below 0.5% above 400 Hz | graph-read (approx.); off-scale (>5%) below about 90 Hz |
| thd_96 | off-scale (>5%) below about 140 Hz; 1.0-1.5% from 150 Hz to 400 Hz; rises to about 1.5% near 8 kHz | graph-read (approx.); recorded as null in frontmatter (not a defensible single value) |
| max SPL | not measured; ASR says woofer limiting is gradual | |
| Critique | dip 500-700 Hz from port response; woofer directional while tweeter not at crossover; "Brrrr" bass distortion below 50 Hz | Tier D listening notes; bass "muted, muffled" without EQ |

## Method notes
Klippel NFS, tweeter axis, grille not mentioned, over 1000 points, 80 °F, sea level. Testing at 86 dB SPL was not reached (low efficiency), graph compensated. Port response (green) measured separately; an in-room port experiment was posted later.

## Reliability notes
Single custom-finished sample, drop-shipped; several members suspected a defective sample or wrong crossover and asked for the second unit to be measured. Salk was not reported to have responded in the pages read. ASR's retail price in 2020 was $1,295 (black/white).

## Related
[Salk WoW1](../speakers/salk-wow1.md) · [asr](../reviewers/asr.md) · [Salk](../brands/salk.md) · [spinorama-org](spinorama-org.md)
