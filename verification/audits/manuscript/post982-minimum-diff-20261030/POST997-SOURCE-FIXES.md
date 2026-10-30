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
- The **live** `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json` included four mirror predicates (two entries plus two blank lines) for those deleted bibliography lines. Re-run the unchanged successor checker against pinned base `ca3a5bb2`, reconcile only its deterministic *forward mutable* result if the source changes justify it, compare `-O` output and all eight must-fail controls. Historical results and checker logic must remain unchanged.
- Require mirror_check, source stamp gate, PDF page-count/text density/missing-glyph checks, release gate and exact-final-head GitHub CI.

## Explicit boundaries

No changes to the Lean proofs, proof grade, SC42 checker logic, original frozen verification reports, `AGENTS.md`, other manuscripts, or the unrelated #1004 strong-CP source issue. The original `TRIAGE-370.md` remains the before/after baseline and is not itself a certificate of the *new* corrected source. New source changes require an independent exact-head verdict and owner merge approval; publication #918 and Explainer retirement remain held.

## Canonical publication rebuild and SC-42 successor outcome

**Writer-side build evidence, not independent scientific certification.** Source-change parent `950039628ac2f26a5dcd0cf11efe14e6bb3a8d90`; successful canonical [publication workflow 41058306062](https://github.com/amaybaum/incompleteness/actions/runs/41058306062); resulting pushed artifact commit [`7b6af62a`](https://github.com/amaybaum/incompleteness/commit/7b6af62a4907893a33d1c2f1c17c06f05c4e63f7). The disposable branch-only workflow was removed in the same commit.

- `sh ./build.sh Complexity` succeeded (35-page PDF); `sh ./build.sh --book` succeeded (558-page PDF). Extracted-text median densities were 2,810 and 3,047 characters/page respectively. This is **automated**, not an independent visual page inspection.
- The canonical book FULL mirror test reported **0 chapter lines absent**. Source stamps **13 matched / 0 unstamped**, and the manuscript voice and claims checks passed. Only the two publication pairs, FULL Markdown, and mutable SC-42 result changed in the artifact commit, apart from removal of the temporary workflow.
- SC-42 successor checker logic and base `ca3a5bb2` were unchanged; normal and optimized JSON outputs were byte-identical, the live successor result is **PASS with 494/494 retained predicates**, and the existing self-test fixture matches with **eight expected-failure controls passing**. Four deleted bibliography-line mirror predicates were removed from the live successor result, not from frozen historical receipts.
- [Ordinary verification run 41058314700](https://github.com/amaybaum/incompleteness/actions/runs/41058314700) was still queued at this checkpoint and targets the *earlier* source head `95003962`. The [bot-commit-triggered run 41060677332](https://github.com/amaybaum/incompleteness/actions/runs/41060677332) on `7b6af62a` concluded `action_required` with no jobs. Neither is evidence of **final-head CI green**.
- **Remaining gates:** fresh ordinary CI success on the eventual exact final PR SHA (including Lean and Mathlib), independent scientific/minimum-diff ACCEPT on that SHA, selected rendered-page visual QA, and explicit owner exact-SHA merge approval. Keep #1005 draft, #918 held and #1004 separate until those gates are satisfied.

## Owner direction and temporary workflow authorization record (2026-10-30)

- The owner asked **“Can we include the manuscript fixes in this PR as well?”** (2026-10-30; exact clock time unavailable in this audit record).
- On **2026-10-30 at 12:42:44 UTC**, the owner wrote **“Ok great let's continue as suggested”** following the combined audit/source-correction proposal. This authorizes continued scoped work broadly, not a file-by-file or workflow-specific procedure.
- On **2026-10-30 at 13:19:50 UTC**, the owner wrote **“Proceed as suggested”** after being shown the source-edit checkpoint and the already triggered temporary publication workflow. This is continuation/acknowledgment, **not** prior explicit consent to dispatch that workflow.
- No separate owner statement explicitly approving creation/dispatch of the temporary workflow before it ran was found. **This is an open provenance/authorization question**, not an inferred approval. The historical workflow was removed at `7b6af62a`; do not create another workflow without explicit authorization or characterize the earlier broad delegated action as explicitly preapproved.

## Independent reviewer REVISE and scoped follow-up

The [independent 2026-10-30 review](https://github.com/amaybaum/incompleteness/pull/1005#issuecomment-6526297181) passed the fixed-interface §5.1 science, canonical build stamps, 35/558-page selected visual QA, SC-42 successor and all bibliography/recurrence removals. Its **REVISE** finding requires a single §5.2 clause: Theorem 23 fixes the **local** lattice/gauge residue uniquely up to gauge **within the stated structural class**, not all microscopic implementations. This clause has now been restored in the source; a new Complexity TeX/PDF build, visual recheck and exact-head CI are mandatory. No other scientific source expansion, Lean changes, #1015 finite-`S` changes or #918 release is authorized.

The 370 historical hunk inventory remains pinned to post-#994 → post-#997 main; these repairs are a separate delta, not invented additional historical rows. Original Complexity :210 did not appear in the net census and stays separately recorded. The review's 25-row sample found 23 correct and 2 generic wrong rationales (Explainer:950 and ch12:221), now routed to [WRITER-22-RESOLUTION.md](./WRITER-22-RESOLUTION.md). **334 provisional science dispositions have not been individually independently checked for word-level minimality.** For 17 semantic old/new alignment anchors, use `git diff -U0 986dab5a f6989a27 -- papers/*.md book/*.md` to distinguish actual hunk starts from annotated semantic anchors; use untruncated `git diff --numstat` rather than limited compare metadata for count totals.

Issue #946's Structure.md:53 unrestricted hidden-cardinality assertion and the related #1015 observer-relative finiteness review remain outside #1005.
