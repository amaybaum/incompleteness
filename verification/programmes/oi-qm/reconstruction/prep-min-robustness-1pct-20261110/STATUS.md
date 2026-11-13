# Status note: PREP-MIN-ROB-1 1% robustness proof

This note gives the current standing of `PROOF.md` in this directory. It does not change that file,
whose text is the accepted text.

## Accepted record and review

- **Record.** `PROOF.md`, blob `fb65973b555e42235787b199bd634018787d1cab`, SHA-256
  `150c49e65e242fd0f0d87256acbc1e6d5174e77a64792c520fbddb7d721abc92`, 438 lines. Final commit
  `ca6c07f8aa149a847a544c02454c04aefada3c87` (PR #1229; contract checkpoint `3569db17`), on
  source snapshot D `cac5d26441dd33e9348151487e4df7b547195481`, an ancestor of `main`.
- **Review.** ACCEPT, no blockers or nits, at `ca6c07f8aa149a847a544c02454c04aefada3c87`:
  `REVIEW-5845916465.md`. Its stated report digest `f7ff2033...` is reproduced from the body.
- **Nature of the review.** A separate non-author Codex agent review
  (`review_prep_min_rob_1pct`), relayed verbatim from the `amaybaum` account. It is an
  AI-agent paper, algebra and source review, not a human review, a GitHub approval or an owner
  integration decision. No result is kernel-checked.
- **Authority.** #1216 comment 6772851768 (`amaybaum`, 2026-11-10T16:25:36Z), emphasis removed:
  "Explicit owner reply in the current Codex session (2026-11-10): “Authorize the bounded 1% paper
  proof.”" It adopts the contract of the scoping proposal, #1216 comment 6769621038.

## What the record supports, and at what strength

- **Conditional mathematical theorem, paper proof, independently reviewed.** On the PREP-MIN model
  (selected binary SM ring, L >= 9, original observer, uniform reference `U_c`) with the complete
  raw history through t = 2 as target and error `max_c TV <= 1/100`, the minimum of `D_2(nu||U)`
  over one common law is:
  - class A (all normalized laws): the exact algebraic value `C_A` of equation (4.4), independent
    of L, attained by the six-atom law (4.3), with `7 < C_A < 184/25` bits;
  - class B (uniform conditionings): `C_B(L) = log2(512M / floor(100M/49))`, `M = 2^(2L-13)`,
    attained by the explicit event (5.3), with `0 < 8 - C_B(L) < 1/32` bit.
- At zero error the same partition gives 15/2 and 8 bits, re-derived in §6 without using the
  PREP-MIN exact proof as a premise.
- Both optima are fitted to the target, and the result holds at the 1% tolerance only.
- Not established: an error-cost curve, a physical memory, energy or resource bound, a sourced
  preparation, or any quantum-mechanical result. The physical-source gate is not passed.

**Claim supported by this record:** "On the fixed PREP-MIN model and complete raw
t = 2 history target, allowing total-variation error at most 1/100 in each setting, the minimum
relative-entropy cost of one common law is the exact algebraic value C_A of (4.4) over all
normalized laws, between 7 and 184/25 bits, and C_B(L) = log2(512M / floor(100M/49)),
M = 2^(2L-13), over uniform conditionings, each attained explicitly (conditional mathematical
theorem, paper proof, independently reviewed; target-fitted; 1% tolerance only; physical-source
gate not passed)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1216. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
2026-11-13T21:44:54Z), states that "Model acceptance is evidence of review, not independent
mathematical verification", and that "A remediation plan does not authorize new work. It may state
that the obligation remains open." This plan authorizes no work. Each gap below remains open until
the evidence or decision named for it is recorded on `main`.

Here "partially verified" means reviewed by at least one separate AI-agent reviewer, or resting in
part on kernel-checked statements, without independent mathematical verification of the result;
"exploratory" means not reviewed by anyone but its writer.

- **Independently verified:** none; no result is kernel-checked.
- **Known-invalid:** none stated.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| `C_A` (class A) and `C_B(L)` (class B) at total-variation error at most 1/100, each attained | partially verified; conditional on the fixed PREP-MIN model; target-fitted; 1% tolerance only | Paper proof, with one AI-agent paper, algebra and source review | Independent mathematical verification | A kernel formalization, an exact computation reproducible from `main`, or a human review, recorded on `main` |
| Zero-error endpoint, 15/2 and 8 bits, re-derived in §6 | partially verified | As above | Independent mathematical verification | As above |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

The items listed as not established are not results of the record; they remain under #1216.

## Dependencies

| Reference | Classification |
| --- | --- |
| The three source rows of §1, at D | Support on `main`. |
| #1216 comments 6772851768 and 6769621038 | Governance provenance: authorization and contract, quoted above. |
| PR #1227 review 5843234635 and commit `076b8e6f` (lines 69-71, 325-330, 422-423) | Support for the statement that the zero-error endpoint was accepted. It is on `main` only once PR #1227 lands by merge commit (neither squash nor rebase), so that `076b8e6f` remains an ancestor of `main`, with `PROOF.md` and `REVIEW-5843234635.md` in `prep-min-exact-t2-20261110/`. The 15/2 and 8 values themselves are re-derived in §6. |
| #866, #1220, #1226, #1227, #1228 (scope and ownership) | Provenance and stated nondependencies. |
| #1229 comment 6846556140 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| Review 5845916465 | Support on `main` through `REVIEW-5845916465.md`. The commit it reviews becomes reachable from `main` only through a merge commit (neither squash nor rebase), which keeps it an ancestor of `main`. |
| References inside the review bodies (sandbox paths, CI run ids, the reviewers' own authorization statements, GitHub links pinned at PR commits) | Provenance. Each verdict rests on the record blob named in the header. |

## Source drift from D to `main` (`911a5cb6`)

`preparation-loading.md` and `physical-interface.md` are unchanged. In `papers/SM.md`, §3.1's first
sentence and several later §3.1 passages not used here were revised, and SM also changed outside
§3.1; the ring construction (:112) is unchanged. The record's links pin SM at D.

## Superseded lines in the accepted text

- Line 3, "independent exact-checkpoint review pending", and lines 434-438, "The independent
  reviewer must verify ...": that review is recorded in `REVIEW-5845916465.md`.
- Lines 69-71, "accepted off main", and lines 422-423, "The #1227 exact proof and its model review
  are off-main historical calibration": once PR #1227 lands, they are on `main`.
- Lines 427-428, "This new proof and its required fresh non-author full paper/algebra review are
  currently off main": the landing puts the proof and its review record on `main`.
- Line 10, "… or merge is authorized": the merge is the owner's separate decision.

## Landing

- **Order.** PR #1227 lands first by merge commit (neither squash nor rebase), so that `076b8e6f`
  remains an ancestor of `main`, or together with this PR. Owner record #1169 comment 6841795465
  (`amaybaum`, 2026-11-13T02:14:35Z): "#1229 lands with or after #1227."
- **Mode.** Merge commit (neither squash nor rebase), so that `ca6c07f8`, the commit the review
  names, remains an ancestor of `main`.
- **Basis.** Landed by the owner's merge decision, recorded in the merge record #1229 comment
  6846556140 (`amaybaum`, 2026-11-13T07:06:14Z): "merge #1229 with its named claim". §A.46 item 2's
  first condition, that an established claim needs the record, holds only for a claim that meets
  item 1's verification standard. The claim above rests on a paper proof with one AI-agent review.
  The owner's ruling, #1169 comment 6865680499 (`amaybaum`, 2026-11-13T21:44:54Z), states "Model
  acceptance is evidence of review, not independent mathematical verification." The record carries
  no computation, and no record on `main` depended on it at `911a5cb6`, so the landing meets none of
  item 2's conditions. The merge record names no owner exception. Under the ruling, until the §A.46
  amendment it calls for is adopted, "a landing that meets none of the existing conditions needs an
  explicit, recorded owner exception". The record's landing basis is therefore open until that
  amendment is adopted or such an exception is recorded. The record is preserved on `main`, not
  established (§A.46 item 1). Its removal is not automatic and is governed by item 6. The
  accountable Issue is #1216.
- **Owner record.** Landing package: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z).
