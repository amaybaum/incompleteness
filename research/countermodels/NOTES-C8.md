# NOTES-C8 — non-orthogonal Bell-type sets with three or more members

Node C8 (round 2; C4.4's first open item). Bell-type defects in matrix normalization: `d_g = I − 2gg†` (`= 8 pauliW(z_g)`),
`g` maximally entangled; `K(Z) = (Q3 ∩ Z*) + cone Z`; `⟨d_g, d_h⟩ = 4|⟨g|h⟩|² ≥ 0`. Cap vectors are written in the
`ψ` basis of NOTES-C2; real combinations of `ψ_1, ψ_3` (and of `ψ_2, ψ_4`) are maximally entangled, as is
`(3ψ_1 + 4iψ_2)/5`. A **Bell circle** is the set of maximally entangled states in a 2-dimensional subspace spanned by two
independent ones (a great circle of its Bloch sphere). Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of `c8_bell_sets.py` (2026-10-10T23:04Z)

Scratchpad exploration (numerical, not evidence): minimizing `⟨y₁, y₂⟩` over pairs in `K(Z)*` gave negative values for
line triples (`c = 0.2, 0.4, 0.6`), the regular triangle, square and pentagon on a Bell circle; `0` for an orthogonal
triple (control) and `−0.093` for a pair at `c = 1/2` (control). Random sampling of `K(Z)*` had missed every one of these
witnesses, so it is not used.

1. **Witness lemma (C8-L).** If `v, x ∈ ℂ⁴` and `λ ≥ 0` on the defects non-orthogonal to `d₁` satisfy (L1)
   `⟨vv† + Σλ_k d_k, d₁⟩ = 0`, (L2) `⟨vv†, d_k⟩ ≥ 0` for every `k ≠ 1`, (L3) `x†(vv† + Σλ_k d_k)x < 0`, (L4) `x†d_j x ≥ 0`
   for every `j ≠ 1` with `g_j ⊥ g₁`, then `y = vv† + Σλ_k d_k ∈ K(Z)* \ K(Z)`.
2. **Construction.** For a non-orthogonal pair `g₁, g₂` (`c = |⟨g₁|g₂⟩|² ∈ (0, 1)`), `W = span(g₁, g₂)`, a unit `e ∈ W^⊥`,
   `v = g₁ + εe`, `λ = (1 − ε²)/(4c)` on `g₂`, `x = g₂ − (⟨g₁|g₂⟩/ε)e`: (L1) holds, (L3) holds iff `ε² > c`, (L2) holds for
   every cap vector in `W` iff `ε² ≥ 2c_k − 1`, and for one outside `W` when `e ⊥ Π_{W^⊥}g_k`. Predicted: every Bell
   **triple** with a non-orthogonal pair and every finite set on one Bell circle with a non-orthogonal pair is not
   self-dual; exact instances: line triples at `c = 16/25` and `9/25`, the regular triangle (trine), the square, the
   regular hexagon, a triple with its third vector outside `W` non-orthogonal to `g₁`, and one with it outside `W`
   orthogonal to `g₁`.
3. Countercontrols: below the window (`ε² < 2c − 1`) (L2) fails for the line triple at `c = 16/25`; for `Z_F`
   (orthogonal) (L1) is unsatisfiable (`⟨d_k, d₁⟩ = 0` for all `k ≠ 1`).
4. Predicted OPEN: sets of four or more members not on one Bell circle whose `W^⊥`-projections are not parallel
   (conjecture: still not self-dual); the full Bell circle (a continuum) is handled separately (C7 prediction 5).
