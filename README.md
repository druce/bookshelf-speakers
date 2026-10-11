# Bookshelf Speakers — measured research wiki

An LLM-maintained research wiki (Karpathy "LLM Wiki" pattern) comparing **passive bookshelf/standmount speakers rated 6 or 8 Ω and sold new in the US**. Speakers are compared on measured frequency response, directivity, bass extension, sensitivity, impedance and distortion, and on attributed critic and owner opinion. The schema and operating rules are in [`Claude.md`](Claude.md).

**State (2026-10-11):** 375 models screened, 141 in scope, 89 with Tier A/B measurements and a speaker page. Start at [`wiki/overview.md`](wiki/overview.md) or [`wiki/index.md`](wiki/index.md). Rankings are in [`wiki/comparisons/ranked-by-price-band.md`](wiki/comparisons/ranked-by-price-band.md).

## Layout
- `wiki/`: speakers, brands, sources, reviewers, concepts, comparisons, plus `index.md`, `log.md`, `overview.md`. Pages use `[[wikilinks]]` (Obsidian-compatible).
- `data/speakers.csv`: flat table generated from speaker-page frontmatter (`scripts/build_csv.py`).
- `data/cta2034-metrics.json`: listening-window deviation, f3/f6, beamwidth and DI smoothness, recomputed uniformly from raw Klippel exports with `scripts/cta2034.py`.
- `data/candidate-universe.csv`, `data/ingest-results/`: Discover output and the scope verdict for each candidate.
- `raw/MANIFEST.md`: provenance of every source document. The documents themselves (copies of third-party reviews, forum posts and manufacturer pages) are kept out of the public repo.
- `scripts/`: fetch, compute, build and lint helpers. `scripts/INGEST-PLAYBOOK.md` is the instruction set used for batch ingest.

## Regenerate
```sh
python3 -I scripts/fetch_spin_raw.py "<Speaker>" <key>   # re-download Klippel exports listed in raw/MANIFEST.md
python3 -I scripts/compute_all.py                         # data/cta2034-metrics.json
python3 -I scripts/build_csv.py && python3 -I scripts/rank.py && python3 -I scripts/build_index.py
python3 -I scripts/check_links.py                         # lint: broken links, orphans, frontmatter
```

## Sources and attribution
Measurement data comes from [Audio Science Review](https://www.audiosciencereview.com/) (Klippel data © Audio Science Review LLC, [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)), [Erin's Audio Corner](https://www.erinsaudiocorner.com/), Audioholics, SoundStage!/NRC, Stereophile, Hi-Fi News and others. It is aggregated via [spinorama.org](https://www.spinorama.org/) ([repository](https://github.com/pierreaubert/spinorama)). Each number links to a source page that cites the original URL. Subjective claims are attributed, not asserted.

## License
Because the computed metrics derive from CC BY-NC-SA data, the wiki text and `data/` are released under **CC BY-NC-SA 4.0**. The scripts are MIT-licensed.
