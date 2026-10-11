---
type: overview
last_updated: 2026-10-11
---
# Overview

**State as of 2026-10-11:** initial build complete. Discover screened **375** models. **141** are in scope (passive, rated 6 or 8 Ω, bookshelf/standmount, sold new in the US). **89** of those have Tier A/B measurements and a speaker page; **52** are in scope but unmeasured. See [[candidate-universe]], with rankings in [[ranked-by-price-band]].

## Thesis so far
1. **Measured accuracy is cheap; amplifier-friendliness is not.** With a subwoofer, the $468 [[ascend-acoustics-cbm-170-se2]] predicts within 0.5 preference points of every band leader up to $4,100 ([[ranked-by-price-band]]). Above about $500 a pair, money buys bass extension, output, finish and an easier load, not predicted tonal preference.
2. **"8 Ω" is mostly marketing.** Of the 83 current speakers with a measured minimum, 66 fall below the IEC floor for their rating and 30 dip under 4 Ω ([[impedance-honesty]]). Among the 21 best-scoring models, only 3 clear the floor: [[elac-debut-2-0-b5-2]], [[ascend-acoustics-sierra-1-v2]] and [[mofi-sourcepoint-8]]. Treat nearly every shortlisted speaker as a 4 Ω-class load when choosing an amplifier ([[impedance-and-epdr]]).
3. **Sensitivity claims run about 2 dB optimistic.** Across 85 speakers the median measured shortfall is −2.0 dB, and many miss by 3 dB or more ([[sensitivity-claims-vs-measured]]). Budget amplifier power from measured figures.
4. **Bass is where bookshelf speakers differ most.** Most Group A models have anechoic f3 of 52–77 Hz. Only [[march-audio-sointuva-awg]] (37 Hz) and [[buchardt-audio-e50]] (42 Hz) are "excellent" by Claude.md §7. Plan on a subwoofer for anything with f3 above 60 Hz ([[bass-extension-vs-room-gain]]).

## Current shortlist (Group A per band; detail and caveats in [[ranked-by-price-band]])
- **< $300:** [[polk-audio-xt20]], [[elac-debut-2-0-b5-2]] (easiest load), [[polk-audio-xt15]], [[neumi-silk-4]]
- **$300–600:** [[ascend-acoustics-cbm-170-se2]], [[polk-audio-reserve-r100]], [[klipsch-rp-500m-ii]]. [[elac-debut-2-0-b6-2]] is the easy-load alternative.
- **$600–1,200:** [[ascend-acoustics-sierra-1-v2]]. Group B: [[svs-prime-bookshelf]], [[klipsch-rp-600m-ii]], [[polk-audio-reserve-r200]].
- **$1,200–2,500:** [[revel-m105]], [[ascend-acoustics-sierra-lx]], [[kef-ls50-meta]], [[revel-m106]], [[elac-uni-fi-reference-ubr62]]
- **> $2,500:** [[march-audio-sointuva-awg]]. Group B: [[buchardt-audio-e50]].

## Open questions (need the human)
- **Buchardt E50** is rated "4/6 Ω" by its maker. It is included as 6 Ω, but should it be in scope?
- **Revel Concerta2/Performa3 status:** Revel lists them, but Audio Advice shows sold-out or "Discontinued" labels. Confirm with a dealer before relying on [[revel-m16]], [[revel-m105]] or [[revel-m106]].
- **"8 Ω compatible" ratings:** Polk, Klipsch, Wharfedale and Paradigm give no explicit nominal. They are scoped in as 8 Ω (rule in Claude.md §2 as applied in ingest). Keep that, or treat them as unrated?
- **Borderline form factors:** [[focal-dome-flax]] (satellite), [[human-speakers-81-dk]] (470 mm tall) and [[role-audio-skiff]] (desktop full-range) were kept in. Cambridge Minx Min12 was excluded.
- **Graph-read values:** about a third of the minimum-impedance and THD figures are read from graphs. The [[salk-wow1]] minimum (3.3 Ω graph-read vs ASR's 6.5 Ω label) needs a human look.

## Data gaps
- **User reviews are thin.** Most pages have fewer than 5 independent owner reports (anecdotal by §7), because Reddit, Crutchfield and AVS blocked scripted fetches. This is the biggest gap for QC and reliability.
- **23 in-scope speakers have no preference score.** They are measured only by NRC graphs or Tier B rigs: B&W 705 S3 and 805 D4 lines, Focal Kanta/Sopra/Theva, ATC SCM7/SCM19, Spendor Classic 3/1, Totem Bison/Signature One and others. See the list in [[ranked-by-price-band]].
- **52 in-scope models have no Tier A/B data.** Several are popular: B&W 606 S3 and 607 S3, Elac Debut 3.0 B5.3, Wharfedale Diamond 12.1i, Dali Sonik 1/3, Q Acoustics 3010i/3020c, Fyne F500S and Dynaudio Emit 10/Evoke. Measurements of a predecessor (Diamond 12.1, SS-CS5, Emit M10) are not carried over.
- **Max SPL** is not comparable across sources (ASR draft compression charts vs EAC's 102 dB test ceiling), so it is not used for ranking ([[compression-and-max-spl]]).

## Suggested next steps
1. Ingest owner reviews in bulk for the shortlisted models, via a logged-in browser for Reddit, Crutchfield and AVS.
2. Watch ASR and Erin for measurements of the unmeasured popular models listed above. The Debut 3.0 B6.3 already has EAC graphs and is paged as [[elac-debut-3-0-b6-3]].
3. Decide the open scope questions above, then re-run [[ranked-by-price-band]] via `scripts/rank.py`.
4. Lint after the next ~10 ingests (Claude.md §5).
