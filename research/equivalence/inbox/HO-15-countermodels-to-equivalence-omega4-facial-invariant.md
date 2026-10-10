# HO-15 (v1) — countermodels → equivalence: Aut(Ω₄), its orbits, and why the facial invariant cannot source K∞-Trans

**From** `research/countermodels` (round 2, node C9). **To** `research/equivalence` (K∞-Trans; the single-system seams;
draft S4). Written by the coordinator from the source thread's committed record; version 1, 2026-10-10.

## Statements and labels

1. **Aut(Ω₄) = O(3) × ℤ₂** for `Ω₄ = {(x, s) ∈ ℝ³ × ℝ : |x|⁴ + s⁴ ≤ 1}` (all affine automorphisms), by unique
   factorization of `det Hess(|x|⁴ + s⁴) = 2304 s²|x|⁶` under the chain rule; Ω₄ is strictly convex, so its extreme
   points are its boundary points. Label: CONDITIONAL ([W] NOTES-C9 C9.1; [X] `c9_omega4` A1–A4, CC1; the determinant,
   the chain-rule instance, the irreducibility rank and the (counter)controls independently confirmed, `indep_checkC2`
   X5).
2. **The orbits of Aut(Ω₄) on the pure states are the level sets of `s⁴`**: a one-parameter family of closed orbits;
   no transitivity, no dense orbit. With the landed single-system theorems TransitiveBody.lean:602
   `exists_affine_image_eq_eball` and DenseOrbit.lean:174 `exists_affine_image_eq_eball_of_dense` (CERTIFIED at L)
   this is the direct form of Ω₄'s exclusion. Label: CONDITIONAL (item 1).
3. **The exact analogue of the pair-level facial invariant** `c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}` is
   `c*(ω) = dim span{e ∈ V₊* : e(ω) = 0}` (the face of the effect cone exposed by a pure state). It is constant, equal to
   1, on every body with a `C¹` boundary — on Ω₄ exactly as on the ball; 2 at the edge of a cylinder; 9 on `Q3`
   (`d = 4`); 15 / 9 / 10 on K(Z_F). Label: CONDITIONAL ([W] C9.3; [X] F1, CC2, CC3).
4. **Ω₄'s non-transitivity is visible at second order**: the rank of the second fundamental form is 3 (generic), 2 on
   the equator `s = 0`, 0 at the poles; the ball has 3 everywhere. Label: CONDITIONAL ([X] S1; affine invariance of the
   rank [L], not checked).
5. **Ω₄'s state cone is not linearly isomorphic to its dual** (the polar `{|y|^{4/3} + |t|^{4/3} ≤ 1}` is not `C²` at
   `(1, 0)` while `∂Ω₄` is real-analytic): no inner product makes it self-dual. Label: CONDITIONAL ([W] C9.5; [X] P1).

**Assumption-watch marker.** "All pure states have the same facial structure" (constancy of `c*`, the single-system form
of the invariant that excludes the finite-defect exotic pair cones from T) holds on Ω₄ as on the ball, so it cannot
source K∞-Trans. A source of K∞-Trans has to constrain second-order data or the automorphism group itself. A premise
that Ω₄ violates — self-duality of the state cone (item 5) — excludes Ω₄; whether such a premise, with the other
single-system seams, implies K∞-Trans is not decided.

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `e6d42cab` (round-2 commits `d8a1461b` … `e6d42cab`) |
| proposal | `research/countermodels/handoff-proposals/HP2-omega4-facial-invariant-KinfTrans.md`, sha256 `fd74c70641fcb3860d8a2a56b3e465a51440d6990082f9bf56c02507f7a57507` |
| results | `research/countermodels/RESULTS.md` sha256 `c377b73a0dba242ed20c55d6202168cbf7f548d08a4fa1b41f081e60959192eb` (rows C9.1 … C9.7); `NOTES-C9.md` `95863161587c36a05005f876b73bcab94a6fcbfb469ce08ef680997a4a5d849b` |
| script, output | `experiments/c9_omega4.py` `656c999204ef31658bdff33708959becbe5c425d873d7cc53b8ea47be5d5b3f5` / `.out` `88c5fc06f31b35152d41b1debf11c10ccf3a4828ea6265e19a8f7af4e58832e2` (run 1 12/12, `VERDICT C9-OMEGA4-EXACT`, replay identical) |
| coordinator audit | `research/AUDITS/2026-10-10-round2/AUDIT-COUNTERMODELS-R2.md` (X5; the factorization argument read) |

## What the receiving thread may assume

Items 1–5 at their labels; the marker as a constraint on candidate sources of K∞-Trans (draft S4's non-inference rule
and HP-1's wording). Item 2 supersedes nothing: it agrees with R-E2.5 and the coordinator's round-1 curvature check,
giving the whole automorphism group rather than the non-existence of a transitive family.

## What it may not assume

Nothing here is CERTIFIED except the two cited kernel theorems; Ω₄ is a single-system body and nothing here bears on
the pair cone directly; item 4's affine invariance is [L].

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-15 v1` and records in its `LOG.md`
whether and how it relies on it.
