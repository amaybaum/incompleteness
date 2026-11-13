# Status note: WAVE-SIGN-1 downstream wording disposition

This note gives the current standing of `DISPOSITION-20261109.md` in this directory. It does not
change that file, whose text is the accepted text.

## Accepted record and review

- **Record.** `DISPOSITION-20261109.md`, blob `db09cefe205bf497ac9042649c802ae9d810cb57`, SHA-256
  `fdc61822136da0b4c5a8674657878ed989f34322dcff487075168b24bb22e2e2`, 113 lines. Added by commit
  `d3e23dca35f9ee583a042ef6e2c9b99bc832c554` (PR #1213) on source snapshot
  `fd539e150759a6ea51ab279aeeac80fc06050ade`, an ancestor of `main`.
- **Review.** ACCEPT, no blocking findings, at `d3e23dca35f9ee583a042ef6e2c9b99bc832c554`:
  `REVIEW-6739544160.md` (PR #1213 comment 6739544160, account `amaybaum`, 2026-11-09T12:01:36Z).
- **Nature of the review record.** It is a summary by the coordinating writer of a separate Codex
  reviewer's verdict, not the reviewer's own report. It identifies the reviewed object by commit
  only, with no blob id and no report digest. The record has a single commit, so that commit fixes
  the reviewed text. It is an AI-agent review, not a human review, a GitHub approval or an owner
  integration decision.
- **Authority.** #1193 comment 6739175078 (`amaybaum`, 2026-11-09T11:41:15Z): paper-only source
  inspection and a disposition packet; "No automatic correction, manuscript/Lean/probe edits, issue
  closure or merge."

## What the record establishes

- **Negative, documentary, exact hand algebra.** For `T_D(p,c) = (c, F(c) + Dp)` with `D`
  invertible, the explicit inverse `(a,b) -> (D^-1(b - F(a)), a)` gives a bijection for every such
  `D`. `D = +I` is a bijection and differs from `D = -I` in odd characteristic. The statement
  "reversibility forces `D = -I_K`" is therefore false. Under slot reversal with linear `F(c) = Ac`,
  equality with the inverse requires `D^2 = I` and `(D + I)A = 0`.
- The four replacement wordings in §3 are proposals. None is adopted.
- Main's binary display and its posited general minus-memory rule are unaffected. The proved
  properties of the minus-memory map stand.
- Not established: a physical derivation selecting either sign, or an exhaustive inventory of
  affected passages.

**Claim supported by this record:** "Bijectivity of the second-order update
`(p,c) -> (c, F(c) + Dp)` holds for every invertible `D`, so reversibility does not force
`D = -I_K`; the four downstream surfaces of the record's §3 (SM:312; ch05:99 with its FULL:1417
mirror; `SecondOrderCircuit.lean:6–10`; `bohr_frequency_probe.py:10008–10009`) that infer it are
documentary errors, and their replacement wording is proposed, not adopted (exact hand algebra,
independently reviewed)."

## Dependencies

| Reference | Classification |
| --- | --- |
| #1193 and comment 6739175078 | Provenance: authorization only. |
| Source blobs and lines cited at `fd539e15` (SM, ch05, FULL, Main, `SecondOrderCircuit.lean`, `bohr_frequency_probe.py`, `OI_Time_Reversal.lean`, `DESIGN.md`, `continuous-time-audit.md`, `a6-instantiation/result.md`) and `ASSESSMENT.md` | Support on `main`: `fd539e15` is an ancestor of `main` and every cited blob resolves there. |
| Review comment 6739544160 | Support on `main` through `REVIEW-6739544160.md`. The commit it names becomes reachable from `main` only through a merge commit (neither squash nor rebase), which keeps it an ancestor of `main`. |
| CI run 42612953149 (named in the review) | Provenance: repository validation only. |
| References inside the review bodies (sandbox paths, CI run ids, the reviewers' own authorization statements, GitHub links pinned at PR commits) | Provenance. Each verdict rests on the record blob named in the header. |

## Source drift from `fd539e15` to `main` (`911a5cb6`)

- `papers/Main.md`: the binary-display paragraph cited at :294 is unchanged at :292. Posit-ledger
  item (xiii), cited at :726, is verbatim at :724; elsewhere the ledger paragraph was revised
  (items (ii), (iii), (v), (x) and the closing count) and adds item (xiv).
- The false inference is still present on `main` at `papers/SM.md:312`,
  `book/ch05-gauge-structure.md:99`, `book/The-Incompleteness-of-Observation-FULL.md:1417`,
  `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean:6-10` (blob `4eacbb09`, unchanged),
  `verification/lean/bohr_frequency_probe.py:10008` and
  `verification/audits/physical-realization/continuous-time-audit.md:40`, and in the generated
  `SM.tex` and FULL `.tex`. The record's finding is therefore current.
- Sites not listed in the record, for any future correction inventory:
  - from the review's nonblocking note N1, two legacy-frozen passages,
    `verification/programmes/substratum/a6-background-independence/preregistration.md:106` and
    `verification/programmes/substratum/a6-instantiation/preregistration.md:182`;
  - `verification/README.md:497` ("Reversibility forces the previous-slice coefficient to `-1` in
    SM's general second-order form"), present at `fd539e15` and on `main`, found by neither the
    record nor the review.

## Superseded lines in the accepted text

- Lines 3-4, "submitted for separate independent review", and lines 112-113, "Independent
  exact-head review precedes the owner decision": the review has taken place (`REVIEW-6739544160.md`).

## Landing

- **Mode.** Merge commit (neither squash nor rebase), so that `d3e23dca`, the commit the review
  names, remains an ancestor of `main`.
- **Basis.** An established claim needs the record (§A.46 item 2): the claim above. No record on
  `main` depends on this one at `911a5cb6`.
- **Owner record.** Landing package: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z).
