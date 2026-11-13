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
  - `OBJECTS.md` ties each reviewed working copy to its committed blob. Its section
    "Committed bytes differ from the reviewed working copies" gives the reviewed and committed bytes of
    `REVIEW-OA-1.md` and `DELTA-REVIEW-OA-1-r4.md`. r5 is committed with its reviewed bytes.
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

## What the record supports, and at what strength

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
  means, and gap 3 remains open. The qubit-tier failure of the classical control `𝔖_F` holds
  under the configuration-level interface only (r5:610).
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
open, not shown impossible (paper-level research findings: hand derivations, partly on research
records not independently established, with independent AI-agent reviews; Lean statements read on `main`, not rebuilt; not adopted; no manuscript claim
affected)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1169. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
2026-11-13T21:44:54Z), states that "Model acceptance is evidence of review, not independent
mathematical verification", and that "A remediation plan does not authorize new work. It may state
that the obligation remains open." This plan authorizes no work. Each gap below remains open until
the evidence or decision named for it is recorded on `main`.

Here "partially verified" means reviewed by at least one separate AI-agent reviewer, or resting in
part on kernel-checked statements, without independent mathematical verification of the result;
"exploratory" means not reviewed by anyone but its writer.

- **Independently verified:** none of the record's own results. Its [K] items are Lean statements
  on `main`, read by the record and not rebuilt (r5:37).
- **Known-invalid:** none stated.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Gap 2, classical control (D5, D7) | partially verified | One paper proof [R] + [W], re-derived twice at the same layer (MECH-1 Lemma A [R]; TUNE-1 Lemma A-T [W]); AI-agent reviews, with [W] items reviewed only by a model of the author's family (r5:656) | Independent mathematical verification of D5 and D7 | An independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| Gap 1, preparation under μ-G (D2 applied to N1-S) | partially verified; conditional on μ-G, posited through ledger item (iv) | Paper derivation [W], reviewed only by a model of the author's family (r5:656) | Independent mathematical verification of D2 and its application to N1-S | As for gap 2; the posit stays a named premise |
| Gap 3, the configuration-level cap [K] | partially verified | Lean statements on `main` [K], read and not rebuilt; their reading as this cap is reviewed paper text | An independent check that the cited Lean statements give the cap as stated | A kernel theorem stating the cap in the record's terms, or a human review recorded on `main` |
| The owner's key test | partially verified | Gaps 1–3 above | As for gaps 1–3 | As for gaps 1–3 |
| N3, fixed read and backaction | partially verified; conditional on half-known meters (apparatus-1 SA-1(c), P2) | Paper derivation [W], reviewed only by a model of the author's family (r5:656) | Independent mathematical verification | As for gap 2; the posit stays a named premise |
| Statements resting on [R] records (MECH-1, MECH-2, minacc-1, apparatus-1, obsmu, mathcon1-polc, operational-quotient v3, TUNE-1) | partially verified | Research records not independently established | Independent validation of each [R] premise used (§A.46 item 7) | A recorded validation of that premise on `main`, or the statement narrowed to carry it as a named condition |
| D8 | exploratory | An unreviewed candidate | Review and verification | A review and an independent verification recorded on `main` |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

The items listed as not established (N1-S under μ-O and μ-R, R-nl, sufficiency of MP-0 to MP-2)
are open questions, not results of the record; they remain under #1169.

## Dependencies

| Reference | Classification |
| --- | --- |
| `papers/Main.md` and `verification/lean-mathlib/OIBridge/` lines at `fb733b4a` | Support on `main`; see source drift. |
| Records under `reconstruction/` (MECH-1, MECH-2, minacc-1, apparatus-1, obsmu, mathcon1-polc, operational-quotient v3) | Support on `main`, unchanged since `fb733b4a`. They are [R] records, so statements that rest on them carry [R] (§A.46 item 7). |
| TUNE-1, cited from `research/tune-1-20261111` at `d47a6377` (:30) | Support on `main`, as [R]. `d47a6377` is an ancestor of `main` (#1237), and `drafts/tune-1-20261111/` is byte-identical on `main`. |
| #1169 comments 6829742537, 6829898892, 6841795465, 6842046488 | Governance provenance, quoted above. |
| #1169 comment 6829596317 (the FH→SOURCE-1 trace, §8) | Provenance. It is the object §8 checks; each verdict there rests on Lean and manuscript lines on `main`. |
| #1265 comment 6848447181 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| #1169 comment 6831588323 (§10A, the owner's next question) | Governance provenance. §10A is not part of OA-1's results. |
| Commits `066be3b1`, `815d6a8e`, `5fec0966` and `09240c92` on this PR's branch, named in the reviews | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| Working-copy blob ids in `DELTA-REVIEW-OA-1-r4.md` (:279 and :389, `29af1419`; :388, `602fe3af`) | Named by their first 8 characters in the committed file, which closes the §A.42 item 3 gap by abbreviation: the abbreviated ids name session working copies that were not kept. `602fe3af` is reproduced as stated above; `29af1419` (r5 before R1–R7) was not retained. No verdict rests on these objects beyond the committed blob. |
| Other references inside the reviews (session paths, the reviewers' authorization statements, `origin/main` commits) | Provenance. Each verdict rests on the blobs `OBJECTS.md` records. |

## Source drift from `fb733b4a` to `main` (`62bdc2cf`)

- `verification/lean-mathlib/` and every cited record are unchanged.
- In `papers/Main.md`, Main:60 adds the source of visible finiteness ("from the finite-capacity
  clause of the Definition"); `S` finite still holds.
- In the Main:724 posit ledger, items (i) and (iv)–(xiv) are verbatim. Item (ii) adds the source of
  the observer's finiteness ("from the finite-capacity clause of the Definition"); its total-finiteness
  posit is unchanged. Item (iii) and the paragraph after (xiv) are reworded (determinism →
  injectivity; visible finiteness "stipulated per moment rather than derived"). The record cites
  items (ii), (iv), (vii), (xiii) and (xiv).
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
- **Basis.** Landed by the owner's merge decision "Merge now (Recommended)", recorded in the merge
  record #1265 comment 6848447181 (`amaybaum`, 2026-11-13T08:54:09Z, edited 09:07:32Z), which states
  "What landed: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4, as research records on their stated scope. No
  claim is promoted." The landing meets none of §A.46 item 2's conditions: no established claim
  needs the record, it carries no computation, and no record on `main` depended on it at `62bdc2cf`;
  OA-2 and OA-3, landed in the same merge, cite it. The merge record names no owner exception. Under
  the owner's ruling, #1169 comment 6865680499 (`amaybaum`, 2026-11-13T21:44:54Z), until the §A.46
  amendment it calls for is adopted, "a landing that meets none of the existing conditions needs an
  explicit, recorded owner exception". The record's landing basis is therefore open until that
  amendment is adopted or such an exception is recorded. The record is preserved on `main`, not
  established (§A.46 item 1). Its removal is not automatic and is governed by item 6. The
  accountable Issue is #1169.
- **Owner record.** Landing package: #1265 comment 6846206075 (`amaybaum`, 2026-11-13T06:44:20Z):
  "Prepare after sequence (Recommended)"; the PR "then lands only after a separate owner merge
  decision, as a merge commit."
