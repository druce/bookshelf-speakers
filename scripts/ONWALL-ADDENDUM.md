# On-wall category — addendum to INGEST-PLAYBOOK.md (added 2026-10-11)

Follow scripts/INGEST-PLAYBOOK.md, with these differences.

## Scope gate (on-wall)
In scope for the on-wall category if ALL hold:
- Passive; rated 6 or 8 Ω nominal by the maker (same impedance rule as bookshelf, incl. "8 Ω compatible").
- **Designed and marketed by the maker for on-wall mounting as a main L/R (or LCR) speaker**: slim cabinet with an included or dedicated wall bracket / keyhole, intended to hang flat on the wall. Typical depth ≤ ~150 mm, but deeper is fine if the maker designs it for wall use.
- Excluded: in-wall / in-ceiling (cut-in), dipole/bipole surround-only models, Dolby Atmos elevation/height modules, soundbars, active/powered, ordinary bookshelf speakers that merely have a keyhole (those stay in the bookshelf category).
- Woofer(s) ≤ 8"; no height limit (on-walls are often tall and slim).
- Currently sold new in the US.

## Fields
Speaker page frontmatter: add `category: on-wall` and `wall_voiced: true | false | null` right after `slug`.
- `wall_voiced: true` only if the maker states the crossover/bass is voiced or compensated for wall placement (boundary compensation, "voiced for on-wall", a wall/free-space EQ switch set for wall). `false` if the maker says it is identical to a free-standing model. Otherwise null.
- Record cabinet depth in `dimensions_mm` (H×W×D) as usual. Depth is the key practical spec.

## Measurement interpretation
- A free-field spinorama (ASR/Erin Klippel, NRC chamber) of an on-wall speaker shows its response **without** the wall. Wall-voiced designs will look bass-light below ~300–500 Hz there. On the page, say so explicitly. Do **not** apply the bookshelf f3 labels (excellent/good/modest) to free-field f3 of a wall-voiced speaker; record the number and note "free-field; wall placement adds boundary gain".
- Half-space / baffle measurements (speaker mounted in a large baffle or on a wall) are the right reference for bass; record which kind each source used.
- LW deviation, directivity, distortion and impedance are interpreted as for bookshelf speakers. Directivity matters more on a wall (no toe-in; early side-wall reflections).
- Spinorama-backed packets include `computed` metrics as before.

## Pages and sidecars
- Speaker pages go in wiki/speakers/ like any other; Related should link [[on-wall-speakers]] (the concept page).
- Sidecar: add `"category": "on-wall"` and `"wall_voiced": ...`.
- Lineup packets (no spinorama data): search SoundStage!/NRC, Audioholics, Stereophile, ASR, Erin's Audio Corner, Hi-Fi News for measurements of the exact model; if none → `no-tier-ab`.
