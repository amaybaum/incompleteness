# HP-9 — to the countermodels thread and the coordinator: self-duality of the state cone is not a source of K∞-Trans (research only)

From `research/equivalence`, round 3 (node E13; NOTES-E13; R-E13.1–R-E13.4), base L = `9f9f8257`. Answers HO-15 v1's open
question. Nothing here is certified; the non-transitivity steps use two kernel theorems at L.

**Statements.**
1. **Ω⋆ (strongly self-dual, not centrally symmetric).** Ω⋆ = {(X, S) ∈ ℝ³ × ℝ : ‖X‖³ ≤ (1 + S)(1 − S)²}: its cone is the
   power cone `u^{1/3} v^{2/3} ≥ ‖X‖` (`u = T + S`, `v = T − S`), self-dual for `TT' + SS' − (1/3)(TS' + ST') + X·X'`
   (weighted AM–GM), an inner product invariant under every affine automorphism of Ω⋆ (`O(3)` on `X`). Ω⋆ is compact,
   convex, with interior, drivable with `ball3Drive`'s fields extended by `S ↦ S`, has the sharp seed `(1 + S)/2`, is
   strictly convex (so `RelStrictConvex`, singleton faces, capacity ≤ 2), and `KInf1` holds for its full effects; it is
   no ellipsoid, so no body-preserving family is boundary transitive or has a dense boundary orbit
   (TransitiveBody.lean:602, DenseOrbit.lean:174, contrapositive). Label: CONJECTURE (written proof, exact checks).
   Evidence: [X] `experiments/e13_selfdual_body.py` 11/11, replay identical (py `fffa8bb3…`, out `a0063f05…`); [W]
   NOTES-E13 §1.
2. **Ω_cs (self-dual, centrally symmetric).** Ω_cs = {(X, S) : ‖X‖ ≤ F(1 + S, 1 − S)}, `{F ≥ 1}` bounded by a `C¹` chain of
   conic arcs (a circle arc and its polar for `M = diag(4/5, 1/5)` in `(u, v)`, repeated under the boost
   `g(u, v) = (u/4, 4v)`), self-dual for `TT' + SS' + (3/5)(TS' + ST') + X·X'`, centrally symmetric, drivable, strictly
   convex, with a sharp seed; no ellipsoid, hence no boundary-transitive or dense-orbit family. Label: CONJECTURE
   (written proof, exact checks). Evidence: [X] `experiments/e13b_central_selfdual.py` 11/11, replay identical (py
   `c3482560…`, out `24e01a77…`); [W] NOTES-E13 §3.
3. **The lemma.** For a centrally symmetric body with central symmetry `Z` on the cone: a self-dualizing inner product
   invariant under `Z` forces the ellipsoid; otherwise `h = M⁻¹ZᵀMZ` is a non-scalar positive cone automorphism (a
   filter) with `ZhZ = h⁻¹` (in Ω_cs, `h = g` exactly). So central symmetry with strong self-duality (an inner product
   invariant under the reversible transformations, or only under `Z`) gives K∞-Trans. Label: CONJECTURE (written proof).
   Evidence: [W] NOTES-E13 §2; [X] instances B4, XB1 of the second probe.
4. In chart dimension 3 the question is empty (a drive alone forces the ellipsoid, R-E2.6).

**Assumption-watch marker (sharpens HO-15's).** Self-duality of the state cone is not a source of K∞-Trans; its invariant
form is. A proposed OI source of K∞-Trans through self-duality must deliver the invariance of the self-dualizing inner
product under the body's central symmetry (strong self-duality), not the duality alone.

**Proposals.** (a) Countermodels thread: Ω_cs is a ready exact object for the composite-cone work if a self-dual but
non-transitive single-system body is useful there; its filter `g` is explicit. (b) Coordinator: any ROADMAP or overview
wording that lists self-duality among candidate sources of K∞-Trans should carry the marker; draft S4's separation could
be extended to "even with self-duality" only by a later round with a design module for Ω⋆ (the power cone's
self-duality is a two-line inequality, kernel-feasible) — not proposed for S4 as drafted, whose frozen text is
unchanged.

**May not be assumed:** that Ω⋆ or Ω_cs is kernel-checked (no design module was built); anything about the bodies OI
supplies; that strong self-duality is sourced by anything at L.
