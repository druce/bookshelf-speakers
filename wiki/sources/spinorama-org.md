---
type: source
slug: spinorama-org
title: spinorama.org metadata export and raw measurement repository
url: https://www.spinorama.org/json/metadata.json
author: Pierre Aubert (aggregator); measurements by ASR, Erin's Audio Corner, Audioholics, Princeton 3D3A, vendors, hobbyists
fetched: 2026-10-11
tier: A (for asr/eac/audioholics/princeton entries); B (misc-*); C (vendor)
raw: raw/spinorama/spinorama-metadata-2026-10-11.json
---
# spinorama.org

## Summary
spinorama.org aggregates published CTA-2034 measurements for more than 1,100 loudspeakers and recomputes a uniform set of metrics from the raw data, including the Olive [preference-score](../concepts/preference-score.md) with and without sub, −3/−6 dB points, and directivity estimates. The metadata export (`raw/spinorama/spinorama-metadata-2026-10-11.json`) is the backbone of this wiki's [candidate-universe](../comparisons/candidate-universe.md). The project's GitHub repository holds the raw Klippel horizontal and vertical exports, which `scripts/fetch_spin_raw.py` downloads to `raw/spinorama/<Speaker>/<key>/`.

## Content at fetch date
- 1,133 speakers in total (766 passive, 367 active). 538 have shape `bookshelves`, and 353 are passive bookshelves.
- Of the passive bookshelves, 259 have at least one Tier A measurement (asr, eac, misc-audioholics, princeton), 32 have only Tier B (misc-*), and 62 have only Tier C (vendor or speakerdata2034).
- Per measurement: origin, review URL, publication date, `pref_rating` (pref score, with-sub score, LFX, NBD, SM), estimates (ref −3/−6 dB, directivity), and EQ'd variants.

## Extraction rules used in this wiki
- `pref_score` and `pref_score_sub` are taken from the `pref_rating` block of the measurement the speaker page uses as primary.
- Other spinorama.org estimates are not copied into frontmatter. Directivity, f3 and sensitivity are recomputed with `scripts/cta2034.py` from the raw exports, so every speaker uses the same definition ([listening-window](../concepts/listening-window.md), [directivity-index](../concepts/directivity-index.md), [bass-extension-vs-room-gain](../concepts/bass-extension-vs-room-gain.md)).
- spinorama.org prices are often stale launch prices, so they are not used for `price_usd_pair`.
- The type and shape classification is not always right: several "passive" entries proved to be powered (see [active-alternatives](../concepts/active-alternatives.md)).

## Reliability
- This is an aggregator, so its reliability equals that of each origin.
- spinorama.org cross-checks its computed scores against ASR's published ones, and they agree closely.
- Calibration check (2026-10-11): `scripts/cta2034.py` sensitivity for KEF Q150 (EAC) = 83.6 dB, against spinorama.org's computed 84.0 dB. The f3 values were 51 Hz (script) and 52.7 Hz (spinorama.org); the definitions differ slightly.

## Related
[spinorama](../concepts/spinorama.md) · [asr](../reviewers/asr.md) · [erins-audio-corner](../reviewers/erins-audio-corner.md) · [audioholics](../reviewers/audioholics.md) · [princeton-3d3a](../reviewers/princeton-3d3a.md)
