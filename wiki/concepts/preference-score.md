---
type: concept
slug: preference-score
last_updated: 2026-10-11
---
# Preference score (Olive model)

Sean Olive's 2004 regression model (AES Convention Paper 6190/6113) predicts blind-listening preference from spinorama-derived metrics:

`Pref = 12.69 − 2.49·NBD_ON − 2.99·NBD_PIR − 4.31·LFX + 2.32·SM_PIR`

- **NBD**: narrow-band deviation, i.e. ripple, of the on-axis and predicted in-room curves.
- **LFX**: log10 of low-frequency extension, the −6 dB point of the sound power relative to the LW.
- **SM_PIR**: smoothness (r²) of the predicted in-room response slope.

"With sub" (`pref_score_sub`) replaces LFX with an ideal 14.5 Hz extension, isolating everything except bass.

## How this wiki uses it (Claude.md §3, §7)
- Values come from [[spinorama-org]]'s computation for each Tier A measurement. When a speaker has several measurements, the value from the source in its frontmatter is used; the others go in the Measurements table.
- Differences under 0.5 are not meaningful. The score ignores distortion, max output, [[impedance-and-epdr]], and sample variation. It is a coarse ranking aid, never the ranking itself.
- The model was trained mostly on 2004-era speakers in one room. Bass extension dominates the no-sub score, so small bookshelf speakers are structurally penalised; compare them on `pref_score_sub`.

## Related
[[spinorama]] · [[listening-window]] · [[bass-extension-vs-room-gain]]
