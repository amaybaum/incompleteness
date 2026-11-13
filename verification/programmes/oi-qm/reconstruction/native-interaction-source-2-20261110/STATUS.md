# Status note: NATIVE-INT-SRC-2 native boundary write and retention

This note gives the current standing of `SOURCE-SCREEN.md` in this directory. It does not change
that file, whose text is the accepted text.

## Accepted record and reviews

- **Record.** `SOURCE-SCREEN.md`, blob `1daf3861642ceb96c5f3564acdb6a1670209f516`, SHA-256
  `ab92a7403861b72a787fb04a18c67af4c81f89b4e4ffc3cb2a061d8f5932865e`, 162 lines. Final commit
  `862a493d4a22d42a3b123a53af5bdb778603d5d7` (PR #1223), on source snapshot D
  `cac5d26441dd33e9348151487e4df7b547195481`, an ancestor of `main`.
- **Full review.** ACCEPT WITH NITS (three nonblocking notes) at
  `9f046595a709e7422c470484f439f9a82eab515a`, which carried blob
  `ae92161f5308a12edee198b34824bd3a7fb511d4`: `REVIEW-5840000380.md`.
- **Focused review.** ACCEPT at `862a493d4a22d42a3b123a53af5bdb778603d5d7`: `REVIEW-5840019359.md`.
  It checks that the +4/-3 diff from `9f046595` closes the three notes and changes nothing else.
- **Nature of the reviews.** Both are by the same separate non-author Codex agent
  (`review_native_int_src_2`), relayed verbatim from the `amaybaum` account. They are AI-agent
  reviews, not human reviews, GitHub approvals or owner integration decisions.
- **Authority.** #866 comment 6763916830 (`amaybaum`, 2026-11-10T09:33:50Z): one paper-only native
  interaction source assessment with Codex as writer and a separate non-author reviewer.

## What the record supports, and at what strength

- **Negative, scoped: STOPPED / UNSOURCED.** For the selected binary SM ring and its declared
  two-site, two-slice observer, the inspected sources identify no native producer of the selectable
  request and common ready precursor that the boundary-write-and-retention process needs. The
  screen stops at that first link.
- Within the selected rule, the boundary coupling and one-tick retention in the previous-time field
  are derived on paper; the conditional history and the whole outgoing state follow from the
  existing preparation-loading and physical-interface records.
- Evidence: source inspection and bounded exact hand algebra, conditional on the selected rule, the
  supplied source law and the declared projection.
- Not established: a universal impossibility, the absence of other native processes, or any
  physical source. The physical-source gate is not passed.

**Claim supported by this record:** "For the selected binary SM ring and its declared
two-site, two-slice observer, the existing boundary-write-and-retention process is unsourced: the
inspected sources supply no native producer of its selectable request and common ready precursor
(negative, bounded to this process and source packet; not a no-go; physical-source gate not
passed)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #866. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
2026-11-13T21:44:54Z), states that "Model acceptance is evidence of review, not independent
mathematical verification", and that "A remediation plan does not authorize new work. It may state
that the obligation remains open." This plan authorizes no work. Each gap below remains open until
the evidence or decision named for it is recorded on `main`.

Here "partially verified" means reviewed by at least one separate AI-agent reviewer, or resting in
part on kernel-checked statements, without independent mathematical verification of the result;
"exploratory" means not reviewed by anyone but its writer.

- **Independently verified:** none.
- **Known-invalid:** none stated.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Stopped / unsourced: no native producer of the selectable request and common ready precursor in the inspected sources | partially verified; bounded to this process and source packet | Source inspection of the six source rows of §2, with two AI-agent reviews | An independent check of the source inspection | A human review of the inspected sources recorded on `main` |
| Boundary coupling and one-tick retention, within the selected rule | partially verified; conditional on the selected rule, the supplied source law and the declared projection | Bounded exact hand algebra, with two AI-agent reviews | Independent mathematical verification | An independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| Conditional history and outgoing state | partially verified | Follow from the preparation-loading and physical-interface records | Independent validation of those records as premises (§A.46 item 7) | A recorded validation of each premise on `main` |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

The items listed as not established are not results of the record; they remain under #866.

## Dependencies

| Reference | Classification |
| --- | --- |
| #866, #1169 and comments 6763916830, 6763928950 | Provenance: accountability and authorization. |
| #1223 comment 6846037655 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| NATIVE-PRED-1 and NATIVE-FACTOR-SRC-1 reviews | Provenance, each separately; no result is used. |
| The six source rows of §2, at D | Support on `main`. |
| Fredkin and Toffoli (1982) | External primary source for the comparator description only. |
| Reviews 5840000380 and 5840019359 | Support on `main` through the two review records. The commits they review become reachable from `main` only through a merge commit (neither squash nor rebase), which keeps them ancestors of `main`. |
| References inside the review bodies (sandbox paths, CI run ids, the reviewers' own authorization statements, GitHub links pinned at PR commits) | Provenance. Each verdict rests on the record blob named in the header. |

## Source drift from D to `main` (`911a5cb6`)

Five of the six cited sources are byte-identical on `main`. `papers/SM.md` changed. In §3.1 the
first sentence was reworded: Main defines one coupling graph `G_φ` over all states, and a state-varying graph needs an update outside linearity (A5). Later §3.1
passages not used here were also revised: the lattice Bisognano–Wichmann lemma and its proof, the
discrete Einstein equation and its proof, and the self-consistency, lattice-correction and η = 1/4
paragraphs. SM also changed outside §3.1. The bijectivity paragraph (:106) and the explicit ring
construction (:112), which are what the record uses, are byte-identical at D and on `main`.

## Superseded lines in the accepted text

- Line 4, "independent non-author review is a separate gate", and line 162, "Independent review
  must check ...": that review is recorded in the two review records.
- Line 24, "relative links resolve to those same, unchanged files in this draft": on `main` the
  relative link to `papers/SM.md` resolves to its current version. The blob ids in §2 identify the
  versions cited.
- Line 160, "this draft itself establishes nothing on main": the landing makes the record and its
  reviews verifiable from `main`.
- In `REVIEW-5840000380.md`, the relay preamble's "a focused diff-only check is pending": that check
  is `REVIEW-5840019359.md`.

## Landing

- **Mode.** Merge commit (neither squash nor rebase), so that `9f046595` and `862a493d`, the commits
  the reviews name, remain ancestors of `main`.
- **Basis.** Landed by the owner's merge decision, recorded in the merge record #1223 comment
  6846037655 (`amaybaum`, 2026-11-13T06:34:24Z): "merge #1223 with its named claim". §A.46 item 2's
  first condition, that an established claim needs the record, holds only for a claim that meets
  item 1's verification standard. The claim above rests on source inspection and bounded exact hand
  algebra with two AI-agent reviews. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
  2026-11-13T21:44:54Z), states "Model acceptance is evidence of review, not independent
  mathematical verification." The record carries no computation, and no record on `main` depended on
  it at `911a5cb6`, so the landing meets none of item 2's conditions. The merge record names no
  owner exception. Under the ruling, until the §A.46 amendment it calls for is adopted, "a landing
  that meets none of the existing conditions needs an explicit, recorded owner exception". The
  record's landing basis is therefore open until that amendment is adopted or such an exception is
  recorded. The record is preserved on `main`, not established (§A.46 item 1). Its removal is not
  automatic and is governed by item 6. The accountable Issue is #866.
- **Owner record.** Landing package: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z).
