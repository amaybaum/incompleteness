# Status note: PREP-MIN exact t=2 preparation-cost proof

This note gives the current standing of `PROOF.md` in this directory. It does not change that file,
whose text is the accepted text.

## Accepted record and review

- **Record.** `PROOF.md`, blob `ee5c01af0a1dd04e95b7216f12b9c791e748c0c1`, SHA-256
  `1d0aa3cd36acb30d498c9253b6b6536b55f6f24bef4ea04dde04f88b4eed01aa`, 412 lines. Final commit
  `076b8e6f951ab20de2ead780099b8a448485cb2e` (PR #1227; definitions checkpoint `bf092e66`), on
  source snapshot D `cac5d26441dd33e9348151487e4df7b547195481`, an ancestor of `main`.
- **Review.** ACCEPT, no findings, at `076b8e6f951ab20de2ead780099b8a448485cb2e`:
  `REVIEW-5843234635.md`. Its stated report digest `40cf7677...` is reproduced from the body.
- **Nature of the review.** A separate non-author Codex agent review
  (`review_prep_min_exact_t2`), relayed verbatim from the `amaybaum` account. It is an
  AI-agent paper and algebra review, not a human review, a GitHub approval or an owner integration
  decision. No result is kernel-checked.
- **Authority.** #1169 comment 6768774955 (`amaybaum`, 2026-11-10T13:37:05Z), emphasis removed:
  "Owner instruction: “Proceed as suggested.” This explicitly settles the three pending PREP-MIN
  choices and authorizes one bounded paper-only mathematical proof with a separate non-author
  independent review". The same comment fixes the target, the two classes and the cost.

## What the record supports, and at what strength

- **Conditional mathematical theorem, paper proof, independently reviewed.** For the selected binary
  SM ring with L >= 9, the original two-site, two-slice observer, the fixed visible root and the
  uniform reference `U_c`, the minimum of `D_2(nu||U)` over one common preparation law that matches
  the declared visible-history law exactly through t = 2 for both settings is 15/2 bits over all
  normalized laws (class A) and 8 bits over uniform conditionings `U(.|E)` (class B). Both minima
  are attained by explicit common laws or events. The internal checks through t = 0 and t = 1 give
  3 and 9/2 bits (A), 3 and 5 bits (B).
- The class-A optimal weights are fitted to the target, and the class-B supports are selected to
  meet it.
- Not established: a physical memory, energy, resource or apparatus bound, a physically sourceable
  preparation, or any result beyond this fixed contract. The physical-source gate is not passed.

**Claim supported by this record:** "On the fixed PREP-MIN contract (selected binary SM
ring, L >= 9, original two-site, two-slice observer, uniform reference U_c), the minimum
relative-entropy cost of one common preparation law that reproduces the declared visible-history law
exactly through t = 2 for both settings is 15/2 bits over all normalized laws and 8 bits over
uniform conditionings, each attained explicitly (conditional mathematical theorem, paper proof,
independently reviewed; target-fitted; not a physical resource bound; physical-source gate not
passed)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1169. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
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
| Minima 15/2 bits (class A) and 8 bits (class B), each attained, with the t = 0 and t = 1 checks | partially verified; conditional on the fixed PREP-MIN contract; target-fitted | Paper proof and exact algebra, with one AI-agent review | Independent mathematical verification | A kernel formalization, an exact computation reproducible from `main`, or a human review, recorded on `main` |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

The items listed as not established are not results of the record; they remain under #1169.

## Dependencies

| Reference | Classification |
| --- | --- |
| The three source rows of §1, at D | Support on `main`. |
| #1169 comment 6768774955 | Governance provenance: authorization and the chosen contract, quoted above. |
| #1169 comment 6767228389 (preliminary calculation) | Revision provenance; its numbers are re-derived in the record. |
| #1226, #1220, #1049/QPHEN | Stated nondependencies. |
| #1227 comment 6846372273 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| Review 5843234635 | Support on `main` through `REVIEW-5843234635.md`. The commit it reviews becomes reachable from `main` only through a merge commit (neither squash nor rebase), which keeps it an ancestor of `main`. |
| References inside the review bodies (sandbox paths, CI run ids, the reviewers' own authorization statements, GitHub links pinned at PR commits) | Provenance. Each verdict rests on the record blob named in the header. |

## Source drift from D to `main` (`911a5cb6`)

`preparation-loading.md` and `physical-interface.md` are unchanged. In `papers/SM.md`, §3.1's first
sentence and several later §3.1 passages not used here were revised, and SM also changed outside
§3.1; the ring construction (:112) is unchanged. The record's links pin SM at D.

## Superseded lines in the accepted text

- Line 3, "independent exact-checkpoint review pending", lines 392-393, "A separate non-author
  exact-checkpoint full paper/algebra review is still required", and lines 409-412, "The reviewer
  must check ...": that review is recorded in `REVIEW-5843234635.md`.
- Lines 405-407, "This branch and its future model-review record are off main": the landing puts the
  proof and its review record on `main`.
- Line 9, "… or merge is authorized": the merge is the owner's separate decision.

## Landing

- **Mode.** Merge commit (neither squash nor rebase), so that `076b8e6f`, the commit the review
  names, remains an ancestor of `main`. PR #1229's record also cites that commit.
- **Order.** PR #1229 lands with or after this PR.
- **Basis.** Landed by the owner's merge decision, recorded in the merge record #1227 comment
  6846372273 (`amaybaum`, 2026-11-13T06:54:51Z): "merge #1227 with its named claim". §A.46 item 2's
  first condition, that an established claim needs the record, holds only for a claim that meets
  item 1's verification standard. The claim above rests on a paper proof with one AI-agent review.
  The owner's ruling, #1169 comment 6865680499 (`amaybaum`, 2026-11-13T21:44:54Z), states "Model
  acceptance is evidence of review, not independent mathematical verification." The record carries
  no computation, and no record on `main` depended on it at `911a5cb6`, so the landing meets none of
  item 2's conditions; the PREP-MIN-ROB-1 record, landed after it by #1229, cites it. The merge
  record names no owner exception. Under the ruling, until the §A.46 amendment it calls for is
  adopted, "a landing that meets none of the existing conditions needs an explicit, recorded owner
  exception". The record's landing basis is therefore open until that amendment is adopted or such
  an exception is recorded. The record is preserved on `main`, not established (§A.46 item 1). Its
  removal is not automatic and is governed by item 6. The accountable Issue is #1169.
- **Owner record.** Landing package: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z).
