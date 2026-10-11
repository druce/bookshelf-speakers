# Log

Append-only. Each entry header: `## [YYYY-MM-DD] <op> | <title>`.

## [2026-10-11] setup | Scaffold wiki, concept and reviewer pages, scripts
- Scope widened by the human from 8 Ω only to 6 Ω or 8 Ω nominal; DIY kits are listed but not ranked (Claude.md §2 updated).
- Created the directory tree, 11 concept pages (the 10 from §9 plus [[active-alternatives]]), 6 reviewer pages ([[asr]], [[erins-audio-corner]], [[audioholics]], [[soundstage-nrc]], [[stereophile]], [[princeton-3d3a]]) and the source page [[spinorama-org]].
- Scripts: `build_csv.py`, `check_links.py`, `cta2034.py` (uniform CTA-2034 metrics from raw Klippel exports), `compute_all.py`, `fetch_raw.py`, `fetch_asset.py`, `fetch_spin_raw.py`, `spinorama_candidates.py`, `slug.py`.
- Saved the spinorama.org metadata export (1,133 speakers) to `raw/spinorama/`, plus raw Klippel H/V exports for 189 candidate measurements.
