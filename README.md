# Session bundle — May 21, 2026 (updated post-third-sweep)

Contains all files modified during the May 21, 2026 session.
Session entry: §B.2.145 of OI_MASTER.md (with third-sweep addendum at end).

## Layout

```
incompleteness-2.1.0/book/   — drop-in replacements for the book repo
    bibliography.md          — 6 entries swapped/added, closing notes updated
    ch09-universality.md     — §248 sentence rewritten (two correct citations)
    ch16-medicine.md         — in-text citation updated (line 264)
    ch17-bioinformatics.md   — in-text citation updated (line 92)
    appendix-c-objections.md — §88 Tetin citation dropped
    The-Incompleteness-of-Observation-FULL.md   — flat-concat regenerated
    The-Incompleteness-of-Observation-FULL.tex  — pandoc-regenerated
    The-Incompleteness-of-Observation-FULL.pdf  — xelatex 3-pass, 405pp

working-docs/                — kept private
    OI_MASTER.md             — §B.8.9 added, §B.2.145 added (with third-sweep addendum)
    PENDING-CITATIONS-MEMO.md — initial decision memo (start-of-session)
    PENDING-SECOND-SWEEP-MEMO.md — second-sweep memo (closes remaining entries)
```

## What changed in the book

**Bibliography — 6 entries resolved in this session:**

| Old (placeholder)     | New (resolved)                                    |
|-----------------------|---------------------------------------------------|
| Bertini, S., et al. 2025 | Bertini, N. R., Novaes, von Marttens, & Shapiro 2025 (arXiv:2509.24026) |
| Bauer, K., et al. 2020   | Zhang et al. 2020 (Oncogene 39:4770-4779) |
| Marek, M., et al. 2022   | Tontsch-Grunt et al. 2022 (Br. J. Cancer 127:577-586) |
| Pyhel, F., et al. 2024   | Roohani, Huang, & Leskovec 2024 (Nat. Biotechnol. 42:927-935, GEARS) |
| Chen, Penington, & Salzetta 2024 | Chen, C.-H., & Penington (2024), arXiv:2406.02116 |
| Tetin 2024               | (entry removed; surrounding refs carry the claim) |
| (new)                    | Wilson-Gerow, Dugad, & Chen 2024 (PRD 110:045002) |

**In-text propagation:**
- ch09-universality.md §248: "Wilson-Gerow and Verlinde (2024), Chen, Penington, and Salzetta (2024)" → "Wilson-Gerow, Dugad, and Chen (2024), Chen and Penington (2024)"
- ch16-medicine.md §264: "Bauer et al. 2020; Marek et al. 2022" → "Zhang et al. 2020; Tontsch-Grunt et al. 2022"
- ch17-bioinformatics.md §92: "Pyhel et al. 2024" → "Roohani et al. 2024"
- appendix-c-objections.md §88: "Barandes 2024, Liu 2024, Tetin 2024, others" → "Barandes 2024, Liu 2024, others"
- ch04, ch07: no change required (Bertini in-text uses surname-only)

**Bibliography closing notes:** updated to record both second and third sweeps,
including the two remaining author-gated entries (Hayashi-Takagi → Saxton
candidate; Garcia-Manero NCT01305499 → Prebet et al. 2014 candidate).

**FULL.{md,tex,pdf}:** regenerated via pandoc + xelatex. 405pp (unchanged).

## What changed in OI_MASTER

**§B.8.9 (new):** Implications threads — seven thought-experiment threads
(T1-T7) with pruning rule and DFS priority ordering.

**§B.2.145 (new):** Session entry. Originally covered two arcs (bibliography +
implications); third-sweep addendum extends with the citation closures detailed
above. Records the methodological lesson: alternate-angle search (co-authorship
overlap, name-conflation hypothesis testing, registry lookups) closed entries
that repeated topic-keyword searches couldn't.

§C HANDOFF section remains the May 19 handoff — refreshing it is a separate
pass.

## v2.0.10 release status

**Blocked on:** 2 one-line author confirmations.

1. *Hayashi-Takagi et al. 2023 → Saxton, Morisaki, Krapf, Kimura, & Stasevich
   (2023), Sci. Adv. 9: eadh4819.* Strong candidate; topic match exact;
   co-authorship overlap with already-cited Stasevich 2014.
2. *Garcia-Manero NCT01305499 → Prebet et al. (2014), J. Clin. Oncol. 32:
   1242-1248.* Strong candidate; in-text "scheduling as primary endpoint" claim
   fits the published E1905 trial exactly; Garcia-Manero is co-author.

**Collaborator-dependent (unchanged):**
- Diakonakou-Wallace (2024)
- Wallden (2024)

**Other §C.3 items unchanged:**
- Item 2 (philosopher's check on V ⊊ S): no progress
- Item 4 (Juno external-input items): no progress

## See also

- `PENDING-SECOND-SWEEP-MEMO.md` for the detailed rationale on each of the 5
  final entries and the recommended resolution paths.
- `PENDING-CITATIONS-MEMO.md` for the start-of-session decision memo (covers
  the original 8 pending entries).
