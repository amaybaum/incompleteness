# Status note: NATIVE-PREP-SRC-1 quiescent-bank preparation screen

This note gives the current standing of `PREPARATION-SCREEN.md` in this directory. It does not
change that file, whose text is the accepted text.

## Accepted record and review

- **Record.** `PREPARATION-SCREEN.md`, blob `8f1edce39bec7069608d9dc2e34f281a81caa47a`, SHA-256
  `2bce44d2df08fbf2aff213279dd64d041730553ed92a1c9b5c573ec81a5e4239`, 135 lines. Added by commit
  `dbb57b6d68160b5cd32c28aa307d99b2526642a3` (PR #1225) on source snapshot D
  `cac5d26441dd33e9348151487e4df7b547195481`, an ancestor of `main`.
- **Review.** ACCEPT, no required correction, at `dbb57b6d68160b5cd32c28aa307d99b2526642a3`:
  `REVIEW-5840760894.md`.
- **Nature of the review.** A separate non-author Codex agent review (`review_sel_access_1`,
  the same reviewer handle as PR #1224's review, not an author of this record), relayed verbatim
  from the `amaybaum` account. It is an AI-agent review, not a human review, a GitHub approval or an
  owner integration decision.
- **Authority.** #866 comment 6765161496 (`amaybaum`, 2026-11-10T10:37:10Z): "Authorize the bounded
  preparation unit", one source-first preparation screen with a separate review. The record's
  mention of "the current Codex conversation" cannot be checked; the comment is the record of the
  authorization.

## What the record establishes

- **Negative, scoped: STOPPED / UNSOURCED.** For the one quiescent-bank proposal on the selected
  binary SM ring, the inspected sources identify no producer of the ordered bank, its common law or
  the selectable request. The screen stops at that link.
- **Conditional mathematics, exact hand counting.** Given the stipulated bank law `beta_c`: it is
  supported on the eight precursor constraints; it is a strict subensemble of `eta`; relative to
  `U_c` it fixes `r = 2m - 5` additional ordered bits, `m = min(L, 11)`, that is 13, 15 or 17 bits
  for L = 9, 10 or L >= 11, against the eight-bit deficit of `eta`.
- Not established: a minimum over other product sources, a heat, work or memory cost, a success
  probability, a universal obstruction to preparation, or any physical source. The
  physical-source gate is not passed.

**Claim supported by this record:** "For the selected binary SM ring, the quiescent-bank
proposal is unsourced: the inspected sources identify no producer of the bank, its common law or
the selectable request (negative, bounded to this proposal); conditionally on the stipulated bank,
not a minimum over product sources or a physical cost, it meets the eight precursor constraints,
is a strict subensemble of eta and fixes 2m - 5 ordered bits relative to U_c, m = min(L, 11)
(13, 15 or 17 bits for L = 9, 10, >= 11), more than eta's 8 (exact hand counting, independently
reviewed; physical-source gate not passed)."

## Dependencies

| Reference | Classification |
| --- | --- |
| #866, #1169 and comment 6765161496 | Provenance: accountability and authorization. |
| "Earlier stopped reports" and "the concurrent selection review" (line 133) | Provenance. The review confirms that no SEL-ACCESS-1 result is used. |
| The six source rows of §4, at D | Support on `main`. |
| Review 5840760894 | Support on `main` through `REVIEW-5840760894.md`. The commit it reviews becomes reachable from `main` only through a merge commit (neither squash nor rebase), which keeps it an ancestor of `main`. |
| References inside the review bodies (sandbox paths, CI run ids, the reviewers' own authorization statements, GitHub links pinned at PR commits) | Provenance. Each verdict rests on the record blob named in the header. |

## Source drift from D to `main` (`911a5cb6`)

`preparation-loading.md` and `physical-interface.md` are unchanged. Four cited sources changed:

- `papers/SM.md` changed. In §3.1 the first sentence was reworded: Main defines one coupling graph
  `G_φ` over all states, and a state-varying graph needs an update outside linearity (A5). Later §3.1
  passages not used here were also revised: the lattice Bisognano–Wichmann lemma and its proof, the
  discrete Einstein equation and its proof, and the self-consistency, lattice-correction and η = 1/4
  paragraphs. SM also changed outside §3.1. The bijectivity paragraph (:106) and the explicit ring
  construction (:112), which are what the record uses, are byte-identical at D and on `main`.
- `papers/Main.md`: §1.2 and §3.4 changed elsewhere. The remark "the measure as a realization datum"
  (D:60 → `main`:58) gains one sentence on the uniform probability of the bijective carrier. The
  consumed sentence, "a realization in the sense of §3.4 carries its own fixed hidden prior μ_H as part
  of the realization datum", is verbatim. The intervention-dilation theorem (the finite classical
  action-labelled comb) is byte-identical (D:482 → `main`:480).
- `observer-interface-obsmu-20261104/ANALYSIS.md`: the one change is in §4.3; the cited §4.6.2,
  §4.6.3 and §5 are unchanged.
- `book/ch18-beyond.md`: changes lie outside §18.8, the arrow-of-time section cited.

## Superseded lines in the accepted text

- Line 4, "independent non-author review is a separate gate", and line 135, "A separate
  non-author reviewer must check ...": that review is recorded in `REVIEW-5840760894.md`.
- Line 77, "Relative links resolve to the same unchanged files in this draft": on `main` the
  relative links to SM, Main, ANALYSIS and Chapter 18 resolve to their current versions. The blob ids
  in §4 identify the versions cited.
- Line 133, "Before any eventual landing, the exact source reachability and added review/status
  references require their own §A.42 item-8 trace": that trace is the table and drift list above.

## Landing

- **Mode.** Merge commit (neither squash nor rebase), so that `dbb57b6d`, the commit the review
  names, remains an ancestor of `main`.
- **Basis.** An established claim needs the record (§A.46 item 2): the claim above. No record on
  `main` depends on this one at `911a5cb6`.
- **Owner record.** Landing package: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z).
