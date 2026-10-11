---
type: source
slug: asr-paradigm-monitor-se-atom
title: "Paradigm Monitor SE Atom Speaker Review"
url: https://www.audiosciencereview.com/forum/index.php?threads/paradigm-monitor-se-atom-speaker-review.17837/
author: Amir Majidimehr
outlet: Audio Science Review
published: 2020-11-24
fetched: 2026-10-11
tier: A
raw: raw/measurements/asr-paradigm-monitor-se-atom.md
raw_data: raw/spinorama/Paradigm Monitor SE Atom/asr/
assets: [raw/assets/asr-paradigm-monitor-se-atom-impedance.png, raw/assets/asr-paradigm-monitor-se-atom-thd.png]
speakers: [paradigm-monitor-se-atom]
---
# ASR: Paradigm Monitor SE Atom review (2020-11-24)

## Summary
Klippel NFS review of a budget ported bookshelf. Amir found an uneven on-axis response (dip 2-4 kHz, then peaking and a ~15 kHz resonance) but good, parallel directivity, so EQ is easy. Without EQ he could not recommend it; with EQ it is serviceable. Bass is limited, so a sub is needed.

## Extracted values
| Field | Value | Note |
|---|---|---|
| sensitivity_db_2v83 | 84.6 dB | computed, scripts/cta2034.py v2 from raw Klippel export; reviewer states none |
| lw_deviation_db | ±2.1 dB | computed (300 Hz-10 kHz) |
| on_axis_deviation_db | ±3.1 dB | computed |
| f3 / f6 | 57 / 52 Hz | computed |
| hor / ver beamwidth | 128° / 85° | computed |
| di_smoothness | minor-discontinuity | ERDI residual 1.3 dB; ER dip near 1.5 kHz 2.5 dB |
| on_minus_lw_4_10k | +1.4 dB | on-axis brighter than window |
| SPDI 1 kHz / 10 kHz | 5.3 / 8.3 dB | computed |
| pref_score / with sub | 4.13 / 6.50 | spinorama.org computation (packet) |
| min_impedance_ohm | 4.5 Ω | ASR plot annotation "min = 4.5 ohm"; minimum band ~130-250 Hz; DC-region ~4.3 Ω; graph-read (approx.) |
| thd_96db_pct | ~3.9 % worst case near 100 Hz | graph-read (approx.): THD ~69 dB vs fundamental ~97 dB; falls to ~1% by 1 kHz; plot titled 96 dB |
| thd_86db_pct | not shown | |
| crossover | impedance peaks near 2 kHz (~22 Ω) | |
| port | integration "good"; crossover region polluted by port resonance | reviewer remark |

## Method notes
Klippel NFS, reference axis tweeter centre, 60 °F. Distortion plot is a single 96 dB level; relative-THD plot also published. Impedance from Klippel. Listening (Tier D): initially detailed, then bright and "exciting"; needed EQ (cuts at high frequencies and 3 kHz); clean at elevated volume because bass is limited; needs a sub.

## Reliability notes
Single sample sent by a member, price then $239/pair. A forum member's own PIR calculation gave 3.68 no sub / 5.93 with sub versus 4.13 / 6.50 here; spinorama.org figure used.

## Related
[Paradigm Monitor SE Atom](../speakers/paradigm-monitor-se-atom.md) · [asr](../reviewers/asr.md) · [Paradigm](../brands/paradigm.md) · [spinorama-org](spinorama-org.md)
