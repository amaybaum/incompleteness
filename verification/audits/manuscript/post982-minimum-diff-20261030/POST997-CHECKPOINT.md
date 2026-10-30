# #1005 post-#997 exact-hunk checkpoint — 2026-10-30

**Status: REVIEW / AUDIT NOT YET CERTIFIED.** This is a *forward audit record*, not a new scientific correction, a claim-grade promotion, an independent acceptance, or merge authorization. The research-only draft remains open.

## Endpoints

- Original pre-#982 main: `0d917665d32287e5d0ce649012175f2c7bf75b09`.
- Accepted #994 minimization merge: `986dab5aabbbd419467109e0b9604c8f19901688`.
- #1005's original snapshot: `6e219231483bb404c0d055ab9a447278422a597e`.
- **Refreshed post-#997 main endpoint**: `f6989a27815c4d715223eebf2859422c1231e3f8`.
- After-#994 → refreshed-main comparison: 80 commits / 115 changed files / **559+ / 524−** top-level source lines in `papers/*.md` and `book/*.md`, including the FULL book mirror.
- Pre-#982 → refreshed-main comparison: 167 commits / 266 changed files / **738+ / 716−** top-level source lines by the same count rule.
- Original snapshot → refreshed-main comparison: 23 commits / 34 changed files / **119+ / 117−** source lines. The last two totals are direct net comparisons, not additive change counts.

Reproduction: [pre-#982 → current](https://github.com/amaybaum/incompleteness/compare/0d917665d32287e5d0ce649012175f2c7bf75b09...f6989a27815c4d715223eebf2859422c1231e3f8) and [post-#994 → current](https://github.com/amaybaum/incompleteness/compare/986dab5aabbbd419467109e0b9604c8f19901688...f6989a27815c4d715223eebf2859422c1231e3f8).

## Complete *textual inventory* at that endpoint, not a substantive scientific certificate

Five companion files enumerate **370 exact contiguous net changed-line hunks** with old/new SHA+line anchors and side-by-side excerpts across **32 top-level maintained source documents**; the FULL Markdown book is excluded as a duplicate of chapter text:

- `HUNKS-PAPERS-A.md` — 81 hunks in Complexity, Computation, Explainer, GR and Juno.
- `HUNKS-PAPERS-B.md` — 133 hunks in Main, Methodology, SM, Structure and Substratum.
- `HUNKS-BOOK-A.md` — 55 hunks in README, appendices, bibliography and ch00–ch02.
- `HUNKS-BOOK-B.md` — 69 hunks in ch03–ch12 (changed chapters only).
- `HUNKS-BOOK-C.md` — 32 hunks in ch13, ch14, ch18, ch19, glossary and preface.

**Correction to the initial review:** the 11 standalone `---` → `***` substitutions in `papers/Complexity.md` and two in `papers/Juno.md` are **REQUIRED (documented Pandoc-formatting safety)**, not excess. `AGENTS.md` build instructions explicitly require `***` over `---` to prevent silent Pandoc table-layout corruption; the Complexity exception was [independently accepted on #997](https://github.com/amaybaum/incompleteness/pull/997#issuecomment-6514996762) and the Juno exception was [explicitly applied on #999](https://github.com/amaybaum/incompleteness/pull/999#issuecomment-6504621056). The previously opened [issue #1006](https://github.com/amaybaum/incompleteness/issues/1006) was based on an incorrect reviewer premise and is closed as not planned. Do not revert these formatting-safety edits.

All **370 net source hunks** have a provisional disposition and an exact-source anchor in `TRIAGE-370.md`, with source-finding explanation in six detailed workpapers. The categories are:

- **13 REQUIRED:** `---`→`***` Pandoc safety changes in Complexity/Juno, approved under #997/#999 and explicitly required by AGENTS.md.
- **335 PROVISIONAL REQUIRED (scientific/status claim scope):** each has a named triggering problem and relevant corrective PR in `MAIN-33`, `SM-32`, `METHODOLOGY-35`, `BOOK-CH03-30`, `OTHER-PAPERS-101` and `OTHER-BOOK-126`. The necessity of a **correction** is provisionally supported; exact replacement *wording* and corpus-wide effects are **not independently certified**.
- **22 UNDECIDED:** potentially wider lexical/narrative/bibliography choices. Strongest review candidate: optional uniform-random permutation numerical illustration and two Erdős–Turán bibliography references, independently judged non-load-bearing in the earlier #999 minimum-change discussion; [issue #1008](https://github.com/amaybaum/incompleteness/issues/1008) requests a scoped disposition. Retain the Landau citation and exact return bounds.

The provenance map `PR-PROVENANCE-370.md` matches 324 hunks to source PR-added text and explicitly routes 46 by source/manual evidence. **No row is independently certified solely by prefix matching, and no independent 370-hunk minimum-change verdict has been received on #1005.**

Previous author-side statuses (130 partially reviewed / 227 untouched) are superseded by this **full preliminary triage**, not by an acceptance. Retained prior PR scoped mathematical source reviews remain valuable provenance, but #1005 still needs its own independent cumulative review and exact-head CI. All five original untruncated source diff inventories remain authoritative for line anchors.

| Corrective source PR | Primary scientific trigger to check; do not undo merely for brevity |
 | Primary scientific trigger to check; do not undo merely for brevity |
|---|---|
| [#995](https://github.com/amaybaum/incompleteness/pull/995) | Unsupported Theorems 1–6 graph citations, integer-rank and Gromov scope |
| [#998](https://github.com/amaybaum/incompleteness/pull/998) | Unsupported regress termination, all-interface gauge claims and fixed-interface coherent identity |
| [#999](https://github.com/amaybaum/incompleteness/pull/999) | False universal recurrence time estimates, unproved stationary/ergodic measure reduction and map-specific distinctions |
| [#1000](https://github.com/amaybaum/incompleteness/pull/1000) | Bell setting/readout/completion premises and quantum kinematic assumptions |
| [#997](https://github.com/amaybaum/incompleteness/pull/997) | A4 integer lattice rank, conditional E5–E7 selection and downstream consequences |

All 32 net-changed top-level Markdown source paths appear in at least one of these five correction PRs' changed-file inventories, but their PR diffs are not identical to the net baseline diff, and that coverage **does not** certify minimality. The separate older #994 hunk reports retain their earlier scoped value.

## Separate source defect

[Issue #1004](https://github.com/amaybaum/incompleteness/issues/1004) identifies an unchanged pre-#982 contradiction concerning physical QCD `barθ`. It is a valid source correction, but **not** evidence of unnecessary edits introduced by #982 or these later PRs.

## Acceptance gate for #1005

1. An independent reviewer must validate or revise **all 370 provisional dispositions**, paying special attention to the 22 UNDECIDED text-scope items. For every scientific correction, examine the named triggering defect, proof or counterexample, smallest safe replacement and only essential downstream propagation; return explicit `REQUIRED`, `EXCESS-RESTORE`, `NEW-RESULT-REVIEW` or `UNDECIDED` with the exact file:line and reason. Text inventories and PR-prefix matching are navigation evidence, **not** an independent acceptance.
2. Check necessary downstream propagation in Main, seven core papers as applicable, Explainer, book chapters, FULL mirror, Lean names and statuses; do not count generated TeX/PDF as distinct conceptual edits. Preserve legitimate correct passages.
3. Retain the 13 verified Pandoc-safety changes and their source/approval links; independently review any other alleged excess before minimal source correction. #1004 is separately routed.
4. Confirm updated endpoint, exact audit SHA, independent review and current-head green checks. A past success on #1005's earlier head does not certify this head.
5. Only then consider making the PR ready/merging, with the owner's exact-SHA approval. **No Introduction release or Explainer retirement is authorized by this checkpoint.**

**Verdict:** complete author-side provisional source inventory with 22 unresolved minimum-wording questions, but **minimum-diff NOT independently certified**. This is not a basis for closing the audit, promoting science, or proceeding as if the source-survival gate is complete.
