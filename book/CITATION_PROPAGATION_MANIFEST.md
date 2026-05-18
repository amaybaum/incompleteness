# Citation Propagation — Modified File Manifest

**Date:** May 18, 2026
**Task:** §C.3 punch-list item P1 — orphan citation resolution
**Baseline:** v2.0.9

## Summary

The 12 orphan in-text citations identified in the book publication-readiness
punch-list (P1) were researched against authoritative sources (arXiv,
INSPIRE-HEP, NASA ADS, PubMed, journal records). 10 of 12 are now fully
resolved and propagated; 2 could not be confirmed and are entered under the
book's existing "pending verification" convention.

## Files in this package

| File | Change |
|------|--------|
| `book/bibliography.md` | 10 verified + 2 pending-flagged entries added across the gravitational-physics, foundations-of-QM, medicine, and bioinformatics sections; citation-completeness note updated. |
| `book/ch09-universality.md` | In-text year correction: Gralla & Wei (2023 -> 2024). |
| `book/ch18-beyond.md` | In-text year correction: Cornish, Spergel, Starkman, & Komatsu (2003 -> 2004). |
| `book/The-Incompleteness-of-Observation-FULL.md` | Consolidated source re-spliced with the updated bibliography and the two in-text fixes. |
| `book/The-Incompleteness-of-Observation-FULL.tex` | Regenerated via pandoc (xelatex pipeline, lmodern suppressed). |
| `book/The-Incompleteness-of-Observation-FULL.pdf` | Recompiled — 404 pp, 0 undefined references. |
| `OI_MASTER.md` | §C.3 item P1 updated from "hard blocker" to "substantially resolved (10/12)"; release note adjusted. |

## Fully resolved (10)

- Abedi, Dykaar, & Afshordi (2017) — Phys. Rev. D 96: 082004; arXiv:1612.00266
- Westerweck et al. (2018) — Phys. Rev. D 97: 124037; arXiv:1712.09966
- Tsang et al. (2018) — Phys. Rev. D 98: 024023; arXiv:1804.04877
- Cornish, Spergel, Starkman, & Komatsu (2004) — Phys. Rev. Lett. 92: 201302; arXiv:astro-ph/0310233
- Slagle & Preskill (2023) — Phys. Rev. A 108: 012217; arXiv:2207.09465
- Gralla & Wei (2024) — Phys. Rev. D 109: 065031; arXiv:2311.11461
- Horvath (2013) — Genome Biology 14: R115; DOI 10.1186/gb-2013-14-10-r115
- Voigt, Tee, & Reinberg (2013) — Genes & Development 27: 1318-1338; DOI 10.1101/gad.219626.113
- Marbach et al. (2009) — J. Comput. Biol. 16: 229-239; DOI 10.1089/cmb.2008.09TT
- Stolovitzky, Monroe, & Califano (2007) — Ann. N.Y. Acad. Sci. 1115: 1-22; DOI 10.1196/annals.1407.021

## Pending verification — author decision required (2)

- "Chen, Penington, & Salzetta (2024)" — no matching paper located. Likely
  intended: Chen, C.-H. & Penington, G. (2024), arXiv:2406.02116; or
  Wilson-Gerow, Dugad, & Chen (2024), Phys. Rev. D 110: 045002.
- "Tetin (2024)" — no matching paper located. Likely intended:
  Pimenta, L. S. (2025), arXiv:2505.08785; or Barandes, J. A. (2024),
  arXiv:2402.16935.

## Open follow-up

- ch09 also cites "Wilson-Gerow and Verlinde (2024)" (not on the original
  P1 list) — verify whether "and Verlinde" is correct.
- Punch-list items P2 (copyedit), P3 (index), P4 (verification of the ~117
  pre-existing bibliography entries) remain.
