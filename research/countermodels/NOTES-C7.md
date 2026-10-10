# NOTES-C7 — the EBF wall

Node C7 (round 2). Base L = `9f9f8257`; branch `research/countermodels`. Conventions as in NOTES-C1/C2 and the
coordinator's `indep_checkC.py`: tables 4×4, `pauliW(z_s) = (I − 2P_s)/8`, `ψ_s` the cap vectors (real, orthonormal,
maximally entangled), `T³_F` the unitaries diagonal in `{ψ_s}`, `π` the Haar projection onto `Fix` (the matrices
diagonal in `{ψ_s}`, coordinates `d ∈ ℝ⁴`), `R = cone{𝟙 − 2e_s} = {d : d_s ≤ Σd/2}` (the slice of K(Z_F)),
`O = cone{e_s + e_t}`, `Circ = {d : Σd/2 ≥ |d − (Σd/4)𝟙|}`, `A = Q3 ∩ Z_F* = Q3 ∩ π⁻¹(R)`. Pairing: `tr(XY)` on
`Herm(4)` (`ipW` is `4 tr` on `pauliW` images, so duals agree). Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C7 script (2026-10-10T22:41Z)

Exploration before this point was numerical, in the scratchpad, and is not evidence; it suggested the following, each
to be confirmed or refuted by an exact script whose decision rule is fixed in its header.

1. **The canonical closed form over Circ fails.** The diagonal surgery `K^C := (Q3 ∩ π⁻¹(C)) + C` is Ĝ-invariant,
   closed, self-positive and contains `A` for every S4-invariant self-dual `C` with `O ⊆ C ⊆ O*`; `K^R = K(Z_F)`,
   `K^{ℝ⁴₊} = Q3`. Predicted: `K^Circ` is **not** self-dual, with the exact witness `y = P_v + diag_ψ(c₀)`,
   `v = ψ_2 + ψ_3/2`, `c₀ = (−2/5, 7/5, 19/20, 4/5)`, `π(y) = y_d = (−2, 12, 6, 4)/5` an extreme ray of Circ:
   `y ∈ (K^Circ)* \ K^Circ`.
2. **Forced non-fixed defects (Theorem C7-D).** Every `T³_F`-invariant self-dual cone whose slice is Circ has a non-PSD
   extreme ray outside `Fix`; the same witness drives the proof. Predicted countercontrol: for the slice R no such
   witness exists (no `p ≥ 0`, `p ≠ 0` with `(𝟙 − 2e_s) − p ∈ R`), consistent with K(Z_F).
3. **The sandwich has a gap with incompatible pairs.** `C₀ = A + Circ ⊆ K' ⊆ C₀* = (Q3 + R) ∩ π⁻¹(Circ)` for every
   Ĝ-invariant self-dual `K'` with H1 and slice Circ. Predicted exact witnesses: the cap state `P_v`,
   `v = 5ψ_1 + 3ψ_2 + 3ψ_3 + ψ_4` (profile `(25, 9, 9, 1)/44 ∈ Circ`, outside `O`), and
   `w = P_u + ½ diag_ψ(−1, 1, 1, 1)`, `u = (ψ_1 − ψ_2 − ψ_3 + ψ_4)/2`: both in `C₀*`, `tr(w P_v) = −3`. Predicted
   consequence (with EBF [A]): the fibre of the slice map over Circ has at least two members.
4. **The fibre over the simplex slice is not {Q3}.** Predicted seed: `y = uu† + 8 diag_ψ(−1, 1, 1, 1)`,
   `u = 3ψ_1 + ψ_2 + ψ_3 + ψ_4`: non-PSD, `π(y) = (1, 9, 9, 9) ≥ 0`, and `A ∪ ℝ⁴₊ ∪ Ĝ·y` pairwise nonnegative; with EBF
   a Ĝ-invariant self-dual `K'_Δ ≠ Q3` with slice `ℝ⁴₊` (C2.8, first half).
5. **The full-circle Bell surgery is not self-dual** (natural continuum candidate; the defects of a great circle of
   maximally entangled states in a 2-dimensional subspace span a 3-dimensional Lorentz cone). Numerical exploration
   found pairs in `K(Z)*` with negative pairing of order `10⁻³`; an exact pair is to be found and certified.
6. **T for the cones of this node:** none of 1–5 exhibits a self-dual cone explicitly, so C3.1 is predicted to remain
   OPEN.
