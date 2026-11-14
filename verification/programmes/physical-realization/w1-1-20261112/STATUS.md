# Status note: W1-1, can existing physics supply W1?

This note gives the current standing of `W1-1-REPORT-r4.md` in this directory. It does not change
that file or any other file here; r4 is the accepted text. The substitutions `OBJECTS.md` records are
separate from this note.

## Accepted record and reviews

- **Record.** `W1-1-REPORT-r4.md`, blob `8bf646292f54c649a2927a579675d04ad8d21462`, SHA-256
  `2436f5d127484dee1d5c9bf6d95f6417b6d60eef27598f1e48e214f2491313b2`, 404 lines. The reviewed and
  accepted bytes, committed at `6ca9656216effa9413da4075debbb7ca708360aa` (PR #1265), differ from
  these on line 383 only; `OBJECTS.md`, section "Committed bytes differ from the reviewed working copies", gives
  their blob and SHA-256 and how to restore them. The checks stated below were made on the
  reviewed bytes. Source snapshot `main` at
  `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, an ancestor of `main`.
- **Review trail.** `W1-1-REPORT.md` (r1) to `W1-1-REPORT-r3.md` are the earlier revisions. They stay
  unchanged, apart from the substitutions `OBJECTS.md` records, which keep every line number,
  because the reviews cite their lines.
  - `REVIEW-W1-1.md`: r1, ACCEPT WITH CHANGES (F1–F12).
  - `REVIEW-W1-1-r2.md`: r2, ACCEPT WITH NITS (N1–N7).
  - `DELTA-REVIEW-W1-1-r3.md`: the r2 → r3 delta, ACCEPT WITH CHANGES (E1–E10); "Diff check of r4",
    ACCEPT WITH CHANGES (D1, D2); confirmation of r4 blob `34b1a16f`, ACCEPT. The confirmation names
    the reviewed blob, as committed at `6ca96562`.
  - `OBJECTS.md` ties each reviewed working copy to its committed blob. Its section
    "Committed bytes differ from the reviewed working copies" gives the reviewed and committed bytes of
    each file committed with a substitution.
- **Nature of the reviews.** Separate read-only, paper-only AI-agent reviews; not human reviews,
  GitHub approvals or owner decisions. The record's derivations are by hand and not machine-checked.
  Its literature is recalled from memory, and the record states that no verdict rests on it.
- **Authority.**
  - Unit: #1245 comment 6829744096 (`amaybaum`, 2026-11-12T16:40:41Z). The owner's choice is "B: W1
    entropy slope (#1245)", and the unit is "One independent, paper-only investigation."
  - Readings: #1245 comment 6828106610 (`amaybaum`, 2026-11-12T15:37:35Z): "W1: L current, C
    alternative".
  - Delta review: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z), item 1: "Run all
    three (Recommended)".
  - Acceptance record: #1245 comment 6841976574 (`amaybaum`, 2026-11-13T02:26:13Z): "W1-1: the delta
    review is complete, and r4 is accepted."

  Emphasis is removed from the quotations.

## What the record supports, and at what strength

- **Paper-level research findings, not adopted.** They are hand derivations, independently
  agent-reviewed, on manuscript statements and one Lean statement read on `main`. The reviews place
  the verdict on the consistency axis, moving no correctness band (§A.23; `REVIEW-W1-1.md`:246–247,
  `DELTA-REVIEW-W1-1-r3.md`:213). The record changes no manuscript claim.
- **Verdict: W1 is an additional physical assumption, not a derived result.** None of the candidate
  mechanisms tested establishes W1 or a sufficient condition for it:
  - thermalization, ETH and (EM);
  - typicality and maximum entropy;
  - holographic and capacity bounds;
  - the equivalence principle and Jacobson's argument;
  - Unruh/Hawking universality;
  - exact or causal decoupling.

  Each fixes a state rather than the count, uses ħ, needs a premise that restates W1 or H-inert (or
  is stronger than it), or needs the distinct open premise of C6(a). The candidate list is not
  proven exhaustive.
- **C6(a), the gap route.** A deep sector whose thermally accessible configurations are collective
  is a distinct sufficient condition. It is open for the finite substratum. In the real lift of the
  linear rule (|α| < 1/d) it fails, with r ≈ +7×10⁵⁹ under reading L (CE-RL).
- **N2.** The lattice identity is exact. Its first-order form and the reading-L and reading-C
  equivalences hold under the hypotheses the record lists. H-add and W1′ in de Sitter form are not
  jointly realized by local cells (CE-F, CE-M).
- **Comparison with H-count (reading L).** GR:58's setting with H-count implies W1-0 and W1-min(L);
  the converse fails, by a witness that violates H-count at second order.
- **§A.29.** A W1 excess with 1 + r > 0 is absorbed into σ, so W1 has no test inside the
  calibration in that regime. For r ≤ −1 the β_E > 0 premise of GR:186/:210 is removed, and for
  r < −1 `counting_passive`'s Monotone-Ω hypothesis fails.
- **Findings on the manuscript surfaces** (ELABORATING). The ħ condition lists and Main's posit
  ledger do not carry the assumed conserved real-valued energy shell (W1-0). This is recorded, not
  applied. W1-add (GR:86 against GR:70/:74) is also recorded, not resolved.

**Claim supported by this record:** "Within OI's present premises, none of the candidate
mechanisms tested (thermalization, ETH and (EM); typicality and maximum entropy; holographic and
capacity bounds; the equivalence principle and Jacobson's argument; Unruh/Hawking universality;
exact or causal decoupling) establishes W1, the equality of the whole hidden sector's shell
entropy–energy slope with the boundary-count slope, or a sufficient condition for it; the one
distinct sufficient route found, a deep sector whose thermally accessible configurations are
collective, is open for the finite substratum and fails in the real lift of the linear rule; W1
is therefore an additional physical assumption, not a derived result (paper-level hand
derivations with independent AI-agent reviews, not machine-checked; the candidate list is not
proven exhaustive; consistency axis only; no manuscript claim affected)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1245. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
2026-11-13T21:44:54Z), states that "Model acceptance is evidence of review, not independent
mathematical verification", and that "A remediation plan does not authorize new work. It may state
that the obligation remains open." This plan authorizes no work. Each gap below remains open until
the evidence or decision named for it is recorded on `main`.

Here "partially verified" means reviewed by at least one separate AI-agent reviewer, or resting in
part on kernel-checked statements, without independent mathematical verification of the result;
"exploratory" means a result not reviewed by anyone but its writer, or a proposal that
claims no result.

- **Independently verified:** none of the record's own results. `counting_passive`
  (`verification/lean-mathlib/OIBridge/ThermalOrientation.lean:256`, imported by `OIBridge.lean`) is
  a kernel theorem on `main` (r4:328); the record reads its statement and does not rebuild it.
- **Known-invalid:** none stated.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Verdict: none of the tested mechanisms establishes W1 | partially verified; the candidate list is not proven exhaustive; consistency axis only | Paper-level hand derivation with independent AI-agent reviews, not machine-checked | Independent mathematical verification of each candidate's exclusion | An independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| C6(a) fails in the real lift of the linear rule (CE-RL) | partially verified | Paper-level hand derivation with independent AI-agent reviews, not machine-checked | Independent verification of CE-RL and its value of r | As for the verdict |
| N2 lattice identity | partially verified | Paper-level hand derivation, exact as a lattice identity, with independent AI-agent reviews | Independent mathematical verification | As for the verdict |
| N2 first-order form and reading-L/C equivalences; CE-F, CE-M | partially verified; conditional on the hypotheses of r4:331 | Paper-level hand derivation with independent AI-agent reviews, not machine-checked | Independent mathematical verification | As for the verdict |
| Comparison with H-count (reading L) | partially verified | Paper-level hand derivation with independent AI-agent reviews, not machine-checked | Independent mathematical verification of both directions | As for the verdict |
| §A.29 calibration findings | partially verified | Paper-level hand derivation with independent AI-agent reviews, not machine-checked | Independent mathematical verification | As for the verdict |
| Findings on the manuscript surfaces (W1-0, W1-add) | partially verified; recorded, not applied | Reading of manuscript lines, AI-agent reviewed | An independent check of the cited lines | A human review recorded on `main`; any manuscript change needs its own owner authorization |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

C6(a) for the finite substratum is open; it is not a result of the record and remains under #1245.

## Dependencies

| Reference | Classification |
| --- | --- |
| `papers/GR.md`, `Main.md`, `SM.md`, `Substratum.md` and `Structure.md` lines at `fb733b4a` | Support on `main`; see source drift. |
| `verification/lean-mathlib/OIBridge/ThermalOrientation.lean:256` (`counting_passive`) | Support on `main`, unchanged; statement read, not rebuilt in this unit. |
| #1245 comment 6818970549 (CE-L, CE-X, the stability criterion, σ-absorption, and the hypotheses H-inert, H-eq and W1′) | Provenance for their first statement. The record re-derives what it uses on paper: ρ and the stability criterion in §3, CE-L and CE-X in §4, and σ-absorption in §7. That support lands with the record. The record calls the comment "not established in the §A.46 sense" (:104), and the hypotheses are stated in §3 as proposals. |
| #1244 comment 6817396025 and #1245 comment 6818970549 (the statement of W1) | Provenance. §3 states W1 from GR:98 and GR:100. |
| #1245 comment 6818702013 (L ≠ 0 at site-local cuts, C6(b)) | Provenance. GR:128 on `main` states that L ≠ 0 at every cut where a boundary site has a deep neighbour. |
| #1245 comments 6829744096, 6828106610, 6841976574; #1169 comment 6841795465 | Governance provenance, quoted above. |
| #1265 comment 6848447181 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| Commits `5fec0966` and `6ca96562` on this PR's branch, named in the review | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| Working-copy blob id `72800573` in `DELTA-REVIEW-W1-1-r3.md` (:228, :270) | Named by its first 8 characters in the committed file, which closes the §A.42 item 3 gap by abbreviation: the abbreviated id names a session working copy that was not kept. Reverting exactly the four hunks the confirmation names in the reviewed r4 (`34b1a16f`, committed at `6ca96562`) reproduces it byte for byte; the package writer made this check. The confirmation itself names the reviewed blob `34b1a16f`, as committed at `6ca96562`. |
| Other references inside the reviews (session paths, `origin/main` commits) | Provenance. Each verdict rests on the blobs `OBJECTS.md` records. |

## Source drift from `fb733b4a` to `main` (`62bdc2cf`)

- `ThermalOrientation.lean` is unchanged.
- In `papers/GR.md`, the condition lists at :88, :466 and :623 add H-Hawking (i), local boost
  structure at the horizon and the symmetric detailed-balance rate ratio. None adds a conserved
  energy shell or a real-valued energy, so the W1-0 finding stands. GR:316 also changed and is not
  cited. Every other cited GR line is unchanged.
- In `papers/Main.md`, Main:60 adds the source of visible finiteness. The Main:724 ledger rewords
  items (ii) and (iii) and its closing paragraph. Neither change adds a real-energy posit.
- The cited `papers/SM.md` (:292–296, :811, :1227) and `papers/Substratum.md` (:257, :268) lines are
  unchanged.
- `papers/Structure.md` :205/:305 are at :206/:306 on `main`, as the record notes (:356).

## Superseded lines in the accepted text

- Line 377, "r4 applies its required edits. An owner checkpoint is required before any use": the
  confirmation of r4 is recorded in `DELTA-REVIEW-W1-1-r3.md`, and the owner's acceptance record is
  #1245 comment 6841976574. Use of the record as a premise remains subject to §A.46 item 7.

## Landing

- **Together.** W1-1 has no dependency on the OA units. It lands in the same merge as them.
- **Mode.** Merge commit (neither squash nor rebase), so that `6ca96562` and the other commits the
  review names remain ancestors of `main`. The branch commits carry "(WIP, not for merge)" in their
  messages; those were labels on the working checkpoints.
- **Basis.** Landed by the owner's merge decision "Merge now (Recommended)", recorded in the merge
  record #1265 comment 6848447181 (`amaybaum`, 2026-11-13T08:54:09Z, edited 09:07:32Z), which states
  "What landed: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4, as research records on their stated scope. No
  claim is promoted." The landing meets none of §A.46 item 2's conditions: no established claim
  needs the record, it carries no computation, and no record on `main` depended on it at `62bdc2cf`.
  The merge record names no owner exception. Under the owner's ruling, #1169 comment 6865680499
  (`amaybaum`, 2026-11-13T21:44:54Z), until the §A.46 amendment it calls for is adopted, "a landing
  that meets none of the existing conditions needs an explicit, recorded owner exception". The
  record's landing basis is therefore open until that amendment is adopted or such an exception is
  recorded. The record is preserved on `main`, not established (§A.46 item 1). Its removal is not
  automatic and is governed by item 6. The accountable Issue is #1245.
- **Owner record.** Landing package: #1265 comment 6846206075 (`amaybaum`, 2026-11-13T06:44:20Z):
  "Prepare after sequence (Recommended)"; the PR "then lands only after a separate owner merge
  decision, as a merge commit."
