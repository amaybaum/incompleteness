# Status note: OA-1, one fixed deterministic substratum and its operations

This note gives the current standing of `OA-1-REPORT-r5.md` in this directory. It does not change
that file or any other file here; r5 is the accepted text.

## Accepted record and reviews

- **Record.** `OA-1-REPORT-r5.md`, blob `5a16b213ebe96846e53072bf1cac226e455f9f72`, SHA-256
  `75a0e997446a9c0167a95ce3ed81da22155ecd0966359d494791ee6353d33fd1`, 730 lines. Committed at
  `09240c92688469a4668c56efb25eaa50f8c07938` (PR #1265). Source snapshot `main` at
  `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, an ancestor of `main`.
- **Review trail.** `OA-1-REPORT.md` (r1) to `OA-1-REPORT-r4.md` are the earlier revisions. They stay
  unchanged because the reviews, `OA-2-REPORT-*.md` and `OA-3-REPORT-*.md` cite their lines.
  - `REVIEW-OA-1.md`: r1, ACCEPT WITH CHANGES.
  - `REVIEW-OA-1-r2.md`: r2, REVISE.
  - `REVIEW-OA-1-r3.md`: r3, ACCEPT WITH NITS.
  - `DELTA-REVIEW-OA-1-r4.md`: the r3 → r4 delta, ACCEPT WITH CHANGES (E1–E9); "Recheck of r5", ACCEPT
    WITH CHANGES (R1–R7); "Re-check of R1–R7", ACCEPT after two mechanical edits.
  - `OBJECTS.md` ties each reviewed working copy to its committed blob.
- **The accepted blob and the re-checked text.** The re-check names working-copy blob
  `602fe3af` and specifies two final edits: digit-only changes to the
  §13 change map, and a replacement for the sentence at :5. Undoing exactly those edits in the
  committed r5 reproduces `602fe3af` byte for byte. This check was made by the package writer; it is
  not a review.
- **Nature of the reviews.** Separate read-only, paper-only AI-agent reviews; `REVIEW-OA-1.md` records
  the reviewer as of the same model family as the author. They are not human reviews, GitHub
  approvals or owner decisions. Nothing in the record is kernel-checked; its [K] items are Lean
  statements on `main`, read and not rebuilt in this unit.
- **Authority.**
  - Unit: #1169 comment 6829742537 (`amaybaum`, 2026-11-12T16:40:37Z). The owner's choice is "A:
    observer–apparatus (#1169)", and the unit is "One bounded, paper-only investigation."
  - Scope and writer: #1169 comment 6829898892 (`amaybaum`, 2026-11-12T16:46:43Z). The scope is "Fold
    into OA-1 (Recommended)", and the writer is "This Claude session (Recommended)".
  - Delta review: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z), item 1: "Run all
    three (Recommended)".
  - Acceptance record: #1169 comment 6842046488 (`amaybaum`, 2026-11-13T02:30:51Z): "OA-1: the delta
    review is complete, and r5 is accepted."

  Emphasis is removed from the quotations.

## What the record establishes

- **Paper-level research findings, independently agent-reviewed, not adopted.** They are hand
  derivations ([W]) on manuscript statements ([P]), Lean statements on `main` ([K]) and research
  records not independently established ([R]). The record changes no manuscript claim.
- **Gap 2, classical control.** Under one affine `φ` acting on every cell, a stored setting acts on
  a carrier only by translation. This is a measure-free property of the map (D5, D7), one paper
  proof re-derived twice. Fredkin bijections supply control, so the restriction is specific to the
  gauge-derived affine class. It is the earliest failure that holds under every measure.
- **Gap 1, preparation.** It is classical and measure-relative. Under the global counting measure
  μ-G, posited through ledger item (iv), with "held" a function of the present visible
  configuration, a selected hidden carrier cannot be held together with its choice record, for every
  bijection (D2 applied to N1-S). A ready-cell supply (MP-0a) or the history-record convention
  (MP-0b) resolves it classically. Under μ-O and μ-R, knowing a carrier can be native and selecting
  one is open.
- **Gap 3, quantum operations.** The configuration-level interface is capped for every rule [K].
  Operations beyond it remain open; impossibility is not shown.
- **The owner's key test** is supported at paper level: gaps 1 and 2 can be resolved by classical
  means, and gap 3 remains open. The qubit-tier failure of the classical control `𝔖_F` is
  established under the configuration-level interface only.
- **Conditional.** N3's fixed read and backaction hold only given half-known meters, a posit
  (apparatus-1 SA-1(c), P2) that costs D3 under μ-G.
- **Not established.** D8, an unreviewed candidate; N1-S under μ-O and μ-R; R-nl; sufficiency of
  MP-0 to MP-2; any manuscript, premise or status change.

**Claim supported by this record:** "For one fixed deterministic substratum setup with OI's
gauge-derived affine rule class, a stored setting acts on a carrier only by translation, under
every measure (a classical-control gap specific to the affine class); under the posited global
counting measure, with held records a function of the present visible configuration, a selected
hidden carrier cannot be held together with its choice record (a classical, measure-relative
preparation gap that a ready-cell supply or a history-record convention resolves); the
configuration-level interface is capped for every rule, and quantum operations beyond it remain
open, not shown impossible (paper-level research findings: hand derivations with independent
AI-agent reviews; Lean statements read on `main`, not rebuilt; not adopted; no manuscript claim
affected)."

## Dependencies

| Reference | Classification |
| --- | --- |
| `papers/Main.md` and `verification/lean-mathlib/OIBridge/` lines at `fb733b4a` | Support on `main`; see source drift. |
| Records under `reconstruction/` (MECH-1, MECH-2, minacc-1, apparatus-1, obsmu, mathcon1-polc, operational-quotient v3) | Support on `main`, unchanged since `fb733b4a`. They are [R] records, so statements that rest on them carry [R] (§A.46 item 7). |
| TUNE-1, cited from `research/tune-1-20261111` at `d47a6377` (:30) | Support on `main`, as [R]. `d47a6377` is an ancestor of `main` (#1237), and `drafts/tune-1-20261111/` is byte-identical on `main`. |
| #1169 comments 6829742537, 6829898892, 6841795465, 6842046488 | Governance provenance, quoted above. |
| #1169 comment 6829596317 (the FH→SOURCE-1 trace, §8) | Provenance. It is the object §8 checks; each verdict there rests on Lean and manuscript lines on `main`. |
| #1169 comment 6831588323 (§10A, the owner's next question) | Governance provenance. §10A is not part of OA-1's results. |
| Commits `066be3b1`, `815d6a8e`, `5fec0966` and `09240c92` on this PR's branch, named in the reviews | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| Working-copy blob ids in `DELTA-REVIEW-OA-1-r4.md` (:279 and :389, `29af14191b6f…`; :388, `602fe3af4d34…`) | Not objects in the repository, so §A.42 item 3 is not met for these two ids. `602fe3af` is reproduced as stated above; `29af1419` (r5 before R1–R7) was not retained. No verdict rests on these objects beyond the committed blob. |
| Other references inside the reviews (session paths, the reviewers' authorization statements, `origin/main` commits) | Provenance. Each verdict rests on the blobs `OBJECTS.md` records. |

## Source drift from `fb733b4a` to `main` (`62bdc2cf`)

- `verification/lean-mathlib/` and every cited record are unchanged.
- In `papers/Main.md`, Main:60 adds the source of visible finiteness ("from the finite-capacity
  clause of the Definition"); `S` finite still holds.
- In the Main:724 posit ledger, items (i), (ii) and (iv)–(xiv) are verbatim. Item (iii) and the
  paragraph after (xiv) are reworded (determinism → injectivity; visible finiteness "stipulated per
  moment rather than derived"). The record cites items (ii), (iv), (vii), (xiii) and (xiv).
- Main also changed at :36, :90, :151 and :700. Every other cited Main line is unchanged.

## Superseded lines in the accepted text

- Lines 3 and 11, "WIP / UNVERIFIED": these are the working labels of the draft. The record's
  standing is as stated in this note.
- Line 53, "nothing is landed on `main` or adopted": the landing puts the record on `main`. It
  remains unadopted.
- Line 23, "The unit ends with an owner decision checkpoint": the acceptance record is #1169
  comment 6842046488, and the merge is the owner's separate decision.

## Landing

- **Together.** OA-2 and OA-3 in this PR cite `OA-1-REPORT-r4.md` by line. All four units land in one
  merge. The r4 lines they cite are unchanged in r5, except the §2A N3 rows (r4:267–268). Those rows
  fall inside the cited range r4:236–270, which OA-2 and OA-3 use only for the typing of the three
  measures.
- **Mode.** Merge commit (neither squash nor rebase), so that `09240c92` and the other commits the
  reviews name remain ancestors of `main`. The branch commits carry "(WIP, not for merge)" in their
  messages; those were labels on the working checkpoints.
- **Basis.** §A.46 item 2: the record supports the claim above, at the strength stated. No record on
  `main` depends on it at `62bdc2cf`. The accountable Issue is #1169.
- **Owner record.** Landing package: #1265 comment 6846206075 (`amaybaum`, 2026-11-13T06:44:20Z):
  "Prepare after sequence (Recommended)"; the PR "then lands only after a separate owner merge
  decision, as a merge commit."
