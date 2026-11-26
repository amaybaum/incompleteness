# T5-LEDGER-1 (unit A): preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it. Evidence
layer of every result: mathematical derivation on paper. No computation was run and no Lean was
built.

## 1. The record preserved

- **Authoritative report:** `REPORT-r3.md` (revision r3), added by the commit that adds this file.
  - r3 supersedes `REPORT-r2.md` (r2, commit `3775cf3de6d1ccda7d293fb41881f702cac1f787`) and
    `REPORT.md` (r1, commit `8f1ee17db555ee004b0b96db5abafcec9f654f08`). Both are kept unchanged.
  - `CHANGES-r2.md` maps each r1-to-r2 change to its review finding (F1–F13). r2 to r3 changes only
    D1 and D2, as stated in r3's revision note.
  - `PLAN.md` (commit `c6cb9170b38b99067ed3dea4f8fcd188a4d68179`) fixes the questions, decision
    rule, controls, productivity test and stopping rule. It came before every report and is not
    superseded.
- **Accountable Issues:** #1049 and #1217; programme #1169. Guiding pull request: #1595.
- **Owner decisions** (each a #1169 comment posted from the account `amaybaum`, quoting the owner):
  - **Comment 7189139613** (created 2026-11-26T10:16:17Z; owner decision stated as received
    2026-11-26T10:16Z), item 2, lane 1: "Theorem 5 premise ledger (#1049, #1217) | Establish exactly
    which symmetry and additional premises the proof requires." Acceptance criteria: "Produce a
    complete premise ledger distinguishing stated assumptions, derived conditions and unsupported
    steps. Determine whether the full dynamical symmetry is necessary or whether kinetic symmetry
    suffices." Also: "Do not authorize computation or adopt additional premises through the new
    research units."
  - **Comment 7190274734** (created 2026-11-26T11:06:26Z; owner decision stated as received
    2026-11-26T11:06Z), item 1:
    - "Approve final acceptance and preservation of units A, B and C, at their independently
      reviewed revisions, under §A.46 item 8."
    - "Authorize the proposed preservation records, including verification status, remediation
      tables, off-main traces and remaining review nits."
    - "A — Theorem 5 premise ledger (#1595) | Accepted | Apply the two required corrections. Leave
      the two optional nits unapplied."
    - "Where a correction changes a scientific statement, ensure that the authoritative preserved
      record states the corrected result unambiguously rather than leaving a misleading assertion in
      place."
    - "Complete the proposed accuracy checks, integration with main and exact-head CI. Return for
      separate merge approvals."
- **Independent non-author reviews.** These are model reviews by a Claude reviewer agent: evidence
  of review, not independent mathematical verification.
  - **PR #1595 comment 7190042848**, review of r1 at `8f1ee17d`: REVISE (moderate), findings F1–F13.
  - **PR #1595 comment 7190237418**, focused delta review of r2 at `3775cf3d`: ACCEPT WITH NITS.
    - It finds F1–F13 resolved and rechecks the repaired Proposition B by hand.
    - It gives two corrections to apply before landing, D1 and D2, and two optional nits, D3 and D4.
    - It was written by the reviewer agent that wrote the r1 review, resumed. All review evidence
      for this record therefore comes from a single model reviewer.
  - The r3 corrections D1 and D2 have not been reviewed separately.

## 2. Substantive result and its precise scope

**Common scope.** The results concern SM Theorem 5 (SM:340–342) at pinned `main` `353a066f`. The
lane 1 and lane 2 inputs are used as labelled conditional inputs, as reviewed paper derivations. No
claim is made for the Z/q level or for the nonlinear case.

- **Layer M.** Theorem 5's statement is supported by stated premises and exact algebra: H-link with
  m = 1 and its abstract ⊗ℂ; O-equivariance of Σ; distinct values; the kernel-checked decomposition
  6 = T_1 + E + A_1; Schur's lemma. No symmetry of a dynamics is used.
- **Layer Φ, P1.** P1 is a derived condition with U(6) acting through the real lift's J_F
  (Lemma 1). It fails through the site-local J_0. No site-local complex structure that is tamed, or
  cubic-equivariant, commutes with the update ([L2] Proposition 2). P1 holds trivially only on the
  doubled complexification.
- **Layer Φ, P2.** P2 splits into P2a–P2e:
  - **P2a** holds given H-PF.
  - **P2b** needs stationarity under the same scalar linear map, L-SDS (Counterexample 10).
  - **P2c** needs the two-point condensate clause under the on-site reading r1 of SM:374
    (Counterexample 9); under reading r2, SM:374 states it.
  - **P2d** needs SMD, the condition that the state's U(6)-stabilizer equals its second moment's.
  - **P2e** is derived on the linear branch with b = 0 (Proposition D).
- **Proposition A (new).** A mixture of two centred Gaussians meets every stated premise and lane
  2's conditions (L-SDS, TPC, H-PF), yet its U(6)-stabilizer is strictly smaller than U(3)×U(2)×U(1).
  It is proved **on T only, with abs(μ) < 1 or on V_rest, and L ≥ 7**; Z is not claimed.
- **Proposition B (new; one direction only).** On T, with abs(μ) < 1 or V_rest, let a law be
  ergodic for the update and translations, or extremal with O included. If the identity component
  of its U(6)-stabilizer contains U(3)×U(2)×U(1), then the T_1 and E blocks of Σ_n vanish.
- **Proposition C (elaborating).** The observer image of the selected measure has scalar Σ_n, so
  Theorem 5's condensate state is not that image.
- **Q2 (vacuous).** On the class PLAN.md §3 fixes, R-kin implies R-dyn at the observer level
  (Proposition D), so control CC7 failed. Per PLAN.md §5, Q2 is reported as vacuous for the stated
  class, and no verdict sentence of PLAN.md §6 is printed.
  - P2b, P2c (under r1) and P2d fail equally under R-dyn. Their missing content is a condition on
    the state.
  - Outside the stated class, the supplementary analysis of REPORT-r3 §4.3 applies. It uses an
    illustrative surrogate F_λ, and its resonant count is conditional on [L1-Q4]; it lies outside
    the decision rule.
- **#1049.**
  - On the branch as SM:312 states it (linear, no offset), P2e follows from R-kin.
  - Under Φ-dyn, the dependence on b = 0 is carried by that branch premise and returns when an
    offset reaches the observer-level update.
  - Under Φ-kin it does not arise.
  - Q4b and O5 are not decided.
- **#1217.** Layer Φ rests on several premises, and none is derived from stated premises:
  - H-PF (independent of the stated premises, by witness);
  - L-SDS (not stated);
  - TPC (stated under r2, independent under r1);
  - SMD (not stated);
  - at μ = 1, H-ZM or H-top and L-NZM (unit C).
- **Productivity.** The test is met through **G4 only** (Proposition A). G1 is withdrawn, G2 holds
  only through items that also fail under R-dyn, and G3 is not met.
- **"Not stated" classifications** are relative to the reading recorded in REPORT-r3 §12. The
  primary scope was read in full. Six sweep terms had every hit read; six were read through a
  filter.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Every result is a paper derivation checked by the model reviews of §1. The remediation plan below
authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Ledger classifications (S/Dv/U) | REPORT-r3 §2 | partially verified: model-reviewed. U entries relative to the reading of §12 | independent non-model review; a full reading of the six filtered sweep terms | #1217, #1049 | a recorded review; a recorded full reading |
| Lemma 1, 1′; layer M; P2a | §2.1–2.3 | partially verified: hand derivation, model-reviewed | independent non-model review | #1217 | a recorded review |
| Proposition A (T only; abs(μ) < 1 or V_rest; L ≥ 7) | §2.4 | partially verified | independent review; an exact finite control on a small torus; the Z case (O3) | #1217 | review; a control run under a separate authorization with green controls; a Z argument |
| Proposition B (one direction) | §2.5 | partially verified; repaired in r2 and rechecked by the delta review; nit D3 recorded (§7 here) | independent review | #1217 | a recorded review |
| Propositions C and D; supplementary §4.3 | §2.6–2.7, §4.3 | partially verified; F_λ illustrative; resonant count conditional on [L1-Q4]; nit D4 recorded (§7 here) | independent review | #1049, #1217 | a recorded review |
| Q3 independence results (H-PF; TPC under r1) | §5 | partially verified; by witness | independent review | #1217 | a recorded review |
| Control re-derivations CC1–CC3 | §3 | partially verified; inherit lane 2's model reviews | independent non-model verification; lane 2's controls X1–X6, C1–C2 | #1217 | as lane 2 |
| r3 corrections D1, D2 | §6, §10, §12, §13 | applied, not separately reviewed | a delta check of r3 | #1217 | a recorded delta check |
| Preregistration order (PLAN.md before the reports) | §5 here | established from commit timestamps only: `c6cb9170` at 10:32:51Z, `8f1ee17d` at 10:47:59Z | none available from commit order alone | #1217 | none; the limitation stands as stated |
| Open nodes O1–O5; findings for routing 1–8 | §9, §10 | open; routed, not edited | derivation, refutation or owner decision for each | #1217, #1049, #1029; unit C for O1 | a written derivation, a counterexample or an owner decision |

## 4. Off-`main` references (§A.42 item 8)

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7189139613, 7190274734 (owner decisions), 7189143747 (synthesis) | report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| PR #1595 comments 7190042848, 7190237418 (reviews) | report header; §1 here | provenance: evidence of review; no result uses them |
| commits `c6cb9170` (PLAN.md), `8f1ee17d` (r1), `3775cf3d` (r2, CHANGES-r2) and the commit adding REPORT-r3.md and this file | report header; §1 here | support on `main` once the merge of §5 lands: the record's own content and, through `c6cb9170`'s commit time, the preregistration order. Not before |
| commit `353a066f` [P] and all line citations | throughout | support on `main`: [P] is `main`'s head when this record was written; the lane pins `b6c6b80b` are its ancestors |
| lane 1 and lane 2 records, `A5-Q4-STAGE2D.md`, lane 2 PRESERVATION.md, A1-11 `FORWARD-ALGEBRA.md`, `q3-a6-offsets-20261108/ASSESSMENT.md`, `a1-finiteness-classes-20261117/CLASSIFICATION.md`, `a1-09-dependency-census/CENSUS.md`; kernel modules `LinkDecomposition`, `OIBridge`, `A6Instantiation`, `BackgroundIndependence` | §1–§12 of the report | support on `main` at [P]; kernel statements read, not built |
| #1049, #1217, #1029, #1169 | report header, §10 | provenance: accountability and routing |

Support off `main`: none.

## 5. Landing condition

The record is preserved only through a merge commit that keeps `c6cb9170`, `8f1ee17d`, `3775cf3d`
and the commit adding REPORT-r3.md and this file reachable from `main`. A squash merge is excluded.
The commit order of PLAN.md before the reports is part of the record's provenance. Per the owner
decision of 2026-11-26T11:06Z, preservation includes integration with current `main` and exact-head
CI. Merging needs the owner's separate approval (§A.50 item 1).

## 6. Preservation rationale

The report delivers the complete premise ledger of SM Theorem 5's proof that the acceptance
criterion requires:
- it separates the statement (layer M), supported by stated premises and exact algebra, from the
  proof's physical sentences (layer Φ);
- it classifies every item as stated, derived or unsupported, with locations, derivations and
  carried hypotheses.

It answers the symmetry question on the stated class: the full dynamical symmetry follows from the
kinetic one, so the readings do not discriminate there. It locates the proof's remaining gaps in
conditions on the state rather than in the ambient symmetry.

Its §8 classifies as NEW:
- Proposition A: a state meeting every stated premise and lane 2's conditions that defeats the step
  from Σ to the unbroken group, on T with abs(μ) < 1 or V_rest, L ≥ 7;
- Proposition B: on T, no extremal state realizes the conclusion with distinct values;
- the five-step split of SM:342's P2.

It also shows that H-PF, and the two-point clause under r1, are independent of the stated premises,
and it routes eight findings. The result bears on #1049, through the location of the b = 0
dependence, and on #1217, through the number and status of the bridge premises.

## 7. Optional nits recorded, not applied (owner decision of 2026-11-26T11:06Z)

- **D3 (Proposition B, line condition).** REPORT-r3 §2.5 writes "R(w)x ∈ Kx, i.e. R(w)x_χ ∈ S¹x_χ
  for every χ". The correct reading is "hence": the componentwise condition follows from
  Kx ⊆ ∏_χ S¹x_χ but does not imply membership in Kx. The proof uses only the forward direction, so
  Proposition B is unaffected.
- **D4 (F_λ, REPORT-r3 §2.7).** "This is nonzero for every u ≠ 0" holds for the pure cubic,
  N(y)_i = y_i³, which vanishes only at y = 0.
  - For a general odd cubic, the difference (0, −λN(s_L⁻¹u)) is nonzero exactly when N(s_L⁻¹u) ≠ 0.
  - Such u exist for any N that is not identically zero, because s_L is invertible for abs(μ) < 1.
  - The conclusion is unaffected: the global phase R(i) is not a symmetry of F_λ, and R-dyn and
    R-res fail.
  - F_λ is an illustrative surrogate used only outside the decision rule.
