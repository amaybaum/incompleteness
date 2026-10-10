# HP2 — countermodels → equivalence (via the coordinator): the facial invariant has no first-order single-system counterpart; an assumption-watch marker for K∞-Trans

**From** `research/countermodels` (node C9, round 2). **Proposed recipient** `research/equivalence` (K∞-Trans, the
single-system seams; HO-7's Ω₄). Proposal only; the coordinator decides whether and how to issue a handoff.

## Statements, each with its label

1. **Aut(Ω₄) = O(3) × ℤ₂** for `Ω₄ = {(x, s) : |x|⁴ + s⁴ ≤ 1}` (all affine automorphisms). Proof by unique factorization
   of `det Hess(|x|⁴ + s⁴) = 2304 s²|x|⁶` under the chain rule. CONDITIONAL ([W] NOTES-C9 C9.1; [X] `c9_omega4` A1–A4,
   CC1).
2. **Its orbits on the pure states (the boundary) are the level sets of `s⁴`**: a one-parameter family of closed orbits.
   The single-system analogue of extreme-ray transitivity fails on Ω₄ exactly, and with it the hypotheses of the kernel
   theorems TransitiveBody.lean:602 and DenseOrbit.lean:174 (CERTIFIED at L, read at L in this round). CONDITIONAL
   (item 1).
3. **The exact analogue of the pair-level facial invariant** `c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}` (self-dual `K`) is
   `c*(ω) = dim span{e ∈ V₊* : e(ω) = 0}` (the face of the effect cone exposed by a pure state). It is constant, equal to
   1, on every body with a `C¹` boundary — on Ω₄ exactly as on the ball; it is 2 at the edge of a cylinder, 9 on Q3
   (`d = 4`), and takes the values 15 / 9 / 10 on K(Z_F). CONDITIONAL ([W] C9.3; [X] F1, CC2, CC3).
4. **Ω₄'s non-transitivity is visible at second order**: the rank of the second fundamental form is 3 (generic), 2
   (equator `s = 0`), 0 (poles); the ball has 3 everywhere. CONDITIONAL ([X] S1; affine invariance of that rank is
   standard differential geometry [L], not checked here).
5. **Ω₄'s state cone is not linearly isomorphic to its dual** (the polar `{|y|^{4/3} + |t|^{4/3} ≤ 1}` is not `C²` at
   `(1, 0)`; `∂Ω₄` is real-analytic): no inner product makes it self-dual. CONDITIONAL ([W] C9.5; [X] P1).

## Assumption-watch marker proposed

"All pure states have the same facial structure" — constancy of `c*`, the single-system form of the invariant that
excludes the finite-defect exotic pair cones from T (countermodels C3.3) — holds on Ω₄ as on the ball, so it cannot
source K∞-Trans. A source of K∞-Trans has to constrain second-order data or the automorphism group itself. A premise that
Ω₄ violates, such as self-duality of the state cone (item 5), excludes Ω₄; whether such a premise, together with the
other single-system seams, implies K∞-Trans is not decided here.

## What the recipient may not assume
Nothing here is CERTIFIED except the two cited kernel theorems at L; items 1–5 are the countermodels thread's written
proofs with exact checks. Ω₄ is a single-system body; nothing here bears on the pair cone directly.

## Evidence
`research/countermodels/NOTES-C9.md`; `experiments/c9_omega4.{py,out}` (run 1 12/12, `VERDICT C9-OMEGA4-EXACT`, replay
identical); RESULTS rows C9.1–C9.7; HO-7 v1 received 2026-10-10T22:08Z (commit d8a1461b).
