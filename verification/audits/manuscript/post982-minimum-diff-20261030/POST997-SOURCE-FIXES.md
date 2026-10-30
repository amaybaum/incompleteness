# #1005 bounded source repairs after the post-#997 main reconciliation

**Draft writer evidence, not independent scientific acceptance.** This follows the 370-net-hunk census, pinned to main `f6989a27815c4d715223eebf2859422c1231e3f8` and post-#994 `986dab5aabbbd419467109e0b9604c8f19901688`. The original 370-line inventories remain immutable snapshots of that historical comparison. #1005 now also contains a **separately identifiable source-fix delta** against post-#997 main; these new fixes must not be silently folded into the old census or described as previously merged.

## Forward ancestry

The original audit PR branch predated #997 and was reconciled to post-#997 main through two-parent commit `02d9f4f8015d16af1a0d3ee823b104ace894088b`. Its tree is the then-main tree plus the 16 audit workpapers, retaining all earlier scientific source corrections and publication artifacts. New source correction commits are strictly forward from that source baseline.

## Actual manuscript corrections and minimality

| Trigger | Edited original source | Smallest justified repair / boundaries |
|---|---|---|
| [#946 source-survival finding](https://github.com/amaybaum/incompleteness/issues/946#issuecomment-6521638876), Theorem 24's fixed-interface scope | `papers/Complexity.md` §5.1–§5.2, original lines 200, 204 and 210 | Three paragraphs replaced. Theorem 24 establishes specified data invariance at a fixed interface/preparation, not preservation of every observation or completeness of all physical implementations. State uniform hidden relabelling/coherent, fibre-dependent relabelling/population-only and independently prepared exactly decoupled finite-ancilla cases separately. Preserve the conditional A4/E5–E7 continuum/matter/atomic/chemistry premises and the bounded 16% parameter estimate. Do not alter the already accepted valid local reconstruction theorem. |
| [#1008 minimum-change candidate](https://github.com/amaybaum/incompleteness/issues/1008#issuecomment-6521644548), prior #999 source review | `book/ch18-beyond.md` §18.7 | Delete exactly one optional uniform-random-permutation numerical illustration, which assumes a distribution not adopted for the physical bijection. **Retain** `φ^N=id`, `N\mid\mathrm{lcm}(1,…,|S|)`, Landau `N\le g(|S|)`, `|S|` unknown, and the exact-linear map-specific `N\le |S|-1` bound. |
| Same #1008 | `book/bibliography.md` mathematical foundations | Remove precisely Erdős–Turán 1965 and 1967 entries used for the dropped typical-order excursion. Preserve Landau 1903, all other bibliography and historical SC31/SC42 evidence. |

## Maintained mirror and outputs

- `book/The-Incompleteness-of-Observation-FULL.md` must mirror the deleted optional numerical sentence and two bibliography entries. Complexity is a distinct paper, not a FULL chapter.
- Canonically regenerate only `papers/Complexity.tex` / `.pdf` and the book FULL `.tex` / `.pdf` using `sh ./build.sh Complexity` and `sh ./build.sh --book`; never fake source stamps.
- The **live** `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` includes two mirror predicates for those deleted bibliography lines. Re-run the unchanged successor checker against pinned base `ca3a5bb2`, reconcile only its deterministic *forward mutable* result if the source changes justify it, compare `-O` output and all eight must-fail controls. Historical results and checker logic must remain unchanged.
- Require mirror_check, source stamp gate, PDF page-count/text density/missing-glyph checks, release gate and exact-final-head GitHub CI.

## Explicit boundaries

No changes to the Lean proofs, proof grade, SC42 checker logic, original frozen verification reports, `AGENTS.md`, other manuscripts, or the unrelated #1004 strong-CP source issue. The original `TRIAGE-370.md` remains the before/after baseline and is not itself a certificate of the *new* corrected source. New source changes require an independent exact-head verdict and owner merge approval; publication #918 and Explainer retirement remain held.
