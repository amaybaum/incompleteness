# F2-5 — amendment 1: two corrections made before the script existed

This amendment was committed after `RULES.md` and before any script or run existed. It corrects two statements of the
rules. Neither correction depends on a measurement.

1. **K-weyl's composition law.** With `D(x, ξ) = ω^{−2⁻¹ x ξ} Z^ξ X^x`, `ZX = ωXZ` and `⟨z, w⟩ = x ξ' − ξ x'`:
   - `X^x Z^{ξ'} = ω^{−x ξ'} Z^{ξ'} X^x`;
   - `D(z) D(w) = ω^{e} D(z + w)` with `e = −x ξ' + 2⁻¹(x ξ' + x' ξ) = −2⁻¹⟨z, w⟩`.

   The control therefore reads `D(z) D(w) = ω^{−2⁻¹⟨z,w⟩} D(z + w)`. `RULES.md` §4 wrote the exponent with the
   opposite sign. No other statement depends on that sign:
   - the covariance unitary `Σ_z D(Sz) D(z)†` intertwines for either sign when `S` preserves `⟨·,·⟩`;
   - isotropy, and so Lagrangian subspaces, does not depend on the sign.

2. **N-site phase-point operators.** As `RULES.md` §2 stated them, they made OD-AD (i) definitional. They are instead
   defined from the `N`-site Weyl operators and parity, following Gross: `D(x⃗, ξ⃗) = ω^{−2⁻¹ x⃗·ξ⃗} Z^{ξ⃗} X^{x⃗}`,
   `Π|y⃗⟩ = |−y⃗⟩`, `A(z⃗) = D(z⃗) Π D(z⃗)†`. OD-AD (i), `A(z₁, z₂) = A(z₁) ⊗ A(z₂)`, is then a check. OD-COMP and the
   rest of OD-AD use these operators.
