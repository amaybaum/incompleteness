# NOTES-C4 — classification of the Bell-type defect cones

Node C4 of `README.md`, taken on the well-defined subfamily the charter names: defect cones
`K(Z) = (Q3 ∩ Z*) + cone Z` for finite `Z`, here with every member **Bell-type**: `z_g = E00/2 − T_g/4`,
`pauliW(z_g) = (I − 2gg†)/8`, `g` maximally entangled (exactly the defects that lie in `maxCone` with the boundary
spectrum `(−1/8, 1/8, 1/8, 1/8)`; H1 holds for each by the SOS identity). Circles (stage 4 Z, stage 5 C5):
`C1(w) = (|0+⟩ + w|1−⟩)/√2`, `C2(w) = (|0−⟩ + w|1+⟩)/√2`, `|w| = 1`. Script: `experiments/c4_bell_family.py` (run 1:
9/9, `VERDICT C4-BELL-FAMILY-EXACT`; replay identical). Evidence levels as in NOTES-C1.

## Theorem C4 (the classification)

1. **Pairs: self-dual iff orthogonal.** For two distinct Bell-type defects `z₁, z₂`, `K({z₁, z₂})` is self-dual iff
   `⟨g₁|g₂⟩ = 0`. (Stage 4 Z proved non-self-duality for squared overlap `c ∈ (0, 1/2)`; here for every `c ∈ (0, 1)`.)
   [W1 + X B4 at `c = 16/25, 3/4, 9/10`]
2. **Orthogonal sets** (`|Z| ≤ 4`): `K(Z)` is self-dual, contains SEP, and its non-PSD extreme rays are exactly `Z`
   (T6 §3.3's proof and [A] Z z1's extremality argument hold verbatim for any orthonormal Bell-type set), so `K(Z)`
   determines `Z`.
3. **Level (i) (`cnot`).** `cnot z_g` is a Bell-type defect iff `g ∈ C1 ∪ C2` [X B1]; `cnot` acts by `C1(w) ↦ C1(−w)`
   and fixes `C2` pointwise [X B2]; `C1 ⊥ C2` and `|⟨Ck(w)|Ck(w′)⟩|² = |1 + w̄w′|²/4` [X B3]. Hence the `cnot`-invariant
   orthogonal Bell-type cones are exactly `K(A₁ ∪ A₂)` with `A₁ ∈ {∅, {C1(±w)}}`, `A₂ ∈ {∅, {C2(w′)}, {C2(±w′)}}`, not both
   empty: five strata over the torus of parameters `(w, w′)` [X B6, symbolic].
   Up to the `cnot`-commuting symmetries `Ad(diag(1, e^{iα}) ⊗ I)` (which rotate both circles by `e^{iα}`) and the
   transpose (`w ↦ w̄`), the invariants are the stratum and, when both parts are present, the relative phase `(w′/w)²`
   (modulo conjugation).
4. **Level (ii) (G16).** G16-invariance forces both parts present with `w′ = w` (`Ad(I⊗Z)` swaps `C1(w) ↔ C2(w)`) and
   the transpose forces `w̄ ∈ {w, −w}`: exactly two cones, **`K(Z_F)`** (`w = 1`) and **`K(Z_Y)`** (`w = i`)
   [X B5: the G16-orbit on the circles is orthonormal exactly at `w ∈ {±1, ±i}`, eight non-orthogonal points otherwise].
   `K(Z_Y) = Ad(S ⊗ I) K(Z_F)` with `S = diag(1, i)`, and `Ad(S ⊗ I)` normalizes G16 [X B5]: up to the normalizer of the
   level-(ii) group, `K(Z_F)` is unique in the class.
5. **Level (ii) with SWAP.** `SWAP` does not preserve `Z_Y` [X B5], so **`K(Z_F)` is the only member** invariant under
   G16 and SWAP.
6. **Location.** `Q3 = K(∅)` is the closed end of the class (no defect); `K(Z_F)` is the four-defect point with
   `(w′/w)² = 1` at `w = 1`; `K_F2 = K({C1(±1)})`; `K(Z_Y)` the four-defect point at `w = i`; the single-defect members
   `K({z_{C2(w′)}})` are level-(i) cones of the boundary spectrum (`λ₂ = −λ₁`, X's characterization). The members with
   `A₁ = ∅` are invariant under the gate flow κ (node C5).

## Written arguments

- **W1 (pair theorem).** Let `⟨z₁, z₂⟩ > 0` (`= c/4`, `c = |⟨g₁|g₂⟩|² ∈ (0, 1)`). Choose `v` in the open cap of `z₁`
  (`|⟨g₁|v⟩|² > |v|²/2`) and outside the closed cap of `z₂` (possible: take `u ⊥ g₁` and `u ⊥ Π_{g₁^⊥}g₂`, the boundary point
  `(g₁ + u)/√2` has `|⟨g₂|·⟩|² = c/2 < 1/2`; move slightly inside the cap of `z₁`). Put
  `λ = −ipW(T_v, z₁)/ipW(z₁, z₂) > 0` and `y = T_v + λz₂`. Then `y ∈ Q3 + cone Z`, `ipW(y, z₁) = 0`, `ipW(y, z₂) > 0`, so
  `y ∈ K* = (Q3 + cone Z) ∩ Z*`. If `y = q + μ₁z₁ + μ₂z₂` with `q ∈ Q3 ∩ Z*`, then
  `0 ≤ ipW(q, z₁) = −μ₁|z₁|² − μ₂ ipW(z₁, z₂)` forces `μ₁ = μ₂ = 0`, so `y = q` would be PSD; but on `u = Π_{v^⊥} g₂`,
  `u†pauliW(y)u = λ(|u|² − 2|⟨g₂|u⟩|²)/8 < 0` because `|⟨g₂|u⟩|²/|u|² = 1 − |⟨g₂|v⟩|²/|v|² > 1/2`. So `y ∈ K* \ K`. ∎
  The same argument applies to two arbitrary defects with one negative eigenvalue whenever the open cap of `z₁` meets
  `{v : v†pauliW(z₂)⁻¹v > 0}` (the region where `pauliW(z₂)` restricted to `v^⊥` is not PSD); for Bell-type `z₂` that region is
  the complement of its closed cap.
- **W2 (level (ii)).** As in item 4; the orbit computation of B5 is the exact check at `w ∈ {±1, ±i}` and at five generic
  rational points of the circle.

## OPEN in this node
- Finite Bell-type sets with three or more members and some non-orthogonal pair (the pair argument needs `v` outside every
  other closed cap and leaves the coefficients of defects orthogonal to `z₁` free).
- Defect cones with non-Bell defects beyond one defect (X's single-defect characterization covers `|Z| = 1`).
- The classification of all closed self-dual `cnot`-invariant cones with H1 at level (ii): the Bell-type class contains
  exactly `K(Z_F)` (with SWAP), but the EBF cones of stage 4 and `K_circ` (NOTES-C2) lie outside every finite-defect class.

## Gem classification (§A.31)
- NEW: the pair theorem for every overlap (closing stage 4's `c ≥ 1/2` gap); the complete list of level-(i) orthogonal
  Bell-type cones (a five-stratum family over a 2-torus); exactly two level-(ii) members, `K(Z_F)` and its `Ad(S⊗I)`-image
  `K(Z_Y)`, and uniqueness of `K(Z_F)` with SWAP.
- ELABORATING: `cnot` keeps Bell-type defects Bell-type only on `C1 ∪ C2` (the circles of stage 4 S2 and stage 5 κ).
