# NOTES-C2 — the structure of K(Z_F)

Node C2 of `README.md`. `K := K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F`, `Z_F = {z_s}`, `pauliW(z_s) = (I − 2P_s)/8`,
`P_s = ψ_sψ_s†`, `{ψ_s}` the orthonormal joint eigenbasis of `X⊗Z`, `Y⊗Y` (real, maximally entangled). Evidence
levels as in NOTES-C1. Script: `experiments/c2_structure.py`. 𝒜 = unitary and antiunitary conjugations; Ĝ :=
`Stab_𝒜(K) = T³_F ⋊ (S4 × Z2)` ([A] Z z1), `T³_F` the unitaries diagonal in `{ψ_s}`. `A := Q3 ∩ Z_F*`.
`Fix` = the tables fixed by `T³_F` (diagonal in `{ψ_s}`, coordinates `d ∈ ℝ⁴`, `ipW` = 4 × the dot product).

## S0 — predictions written before the first run (2026-10-10, before 20:40Z)

- Local stabilizer: `(+,+)` 96 maps (local unitary Cliffords permuting `{P_s}`), `(−,−)` 96 (their transpose
  composites); with SWAP 384 in all. Reason: an element of 𝒜 permutes `{P_s}` iff it maps the algebra
  `span{I, XZ, YY, ZX}` onto itself; for `U ⊗ V` that forces `U, V` Clifford and `π_V = τ π_U τ`, `τ = (1 3)` on axis
  labels, with the signs of `R_V` free up to the determinant: 24 × 4 = 96 per determinant class; SWAP preserves the
  pattern `{(1,3),(2,2),(3,1)}`. Mixed-type (partial-transpose) maps: count not predicted; none is an automorphism.
- The closure with `cnot`: 1536 ([A] Z z1/z4: `|Stab_Cl(Z_F)| = 1536`).
- Extreme rays: the four defects and the pure states `P_v` with `max_s |⟨ψ_s|v⟩|² ≤ 1/2`; no other.
- Facial invariant `c`: 15 on defects, 9 on pure states with all `|c_s|² < 1/2`, 10 with one cap tight, 11 with two.
- Generic orbit sizes: `|G|` for every finite group listed (free action on a generic ray); defects: one orbit of 4
  for every group containing G16, 2 for `⟨cnot⟩`.
- Uniqueness given the symmetry group: expected NO, via the T³-fixed slice (§W6 below).

**Outcome of the predictions:** all confirmed except one: the two-tight value is **10, not 11** (FAILED prediction,
kept): `z_s + z_t = (P_u + P_w)/4` lies in `Herm(v^⊥)` (check E1), so two tight defects add one direction, not two.

## Runs

| run | result | kept as |
|---|---|---|
| 1 | 14/16: S4 tested over all 2304 pairs instead of the 1152 in 𝒜 (my implementation did not match the stated scope); F required the predicted 11 | `c2_structure.run1.*` |
| 2 | 16/16, but the VERDICT text carried the pre-measurement phrase "c = 15/9/10/11" (contradicting the measured 10) | `c2_structure.run2.*` |
| 3 | 16/16, `VERDICT C2-STRUCTURE-EXACT`, verdict text generated from the measurements; every line before the VERDICT identical to run 2 | final; replayed |

## Results

### (a) The symmetry group inside local unitaries, SWAP and the transpose [X S1–S4 + W1]
- Among the 2304 signed-permutation pairs `actC R ∘ actT R′`: exactly 96 of type `(+,+)` (local unitary Cliffords) and
  96 of type `(−,−)` (their composites with the transpose) permute `Z_F`; none of mixed type `(+,−)`, `(−,+)` (the
  partial-transpose type, 192 of which preserve the index pattern but flip the sign product of the three entries and
  send defects to pure tables). With SWAP: **384**. The groups: unitary part 96, with T 192, with T and SWAP 384.
- G16 (16), `⟨G16, SWAP⟩` (48), Gbig (64), `⟨Gbig, SWAP⟩` (192) lie inside; the closure of the local stabilizer with SWAP
  and `cnot` has order **1536**, equal to [A] Z's `|Stab_Cl(Z_F)|`.
- **W1 (no non-Clifford local symmetry).** An element of 𝒜 preserving K permutes its non-PSD extreme rays, which are the
  four defects ([A] Z z1, re-derived in W3), hence permutes `{P_s}`, hence maps the commutative algebra
  `span{I, XZ, YY, ZX}` onto itself. For `U ⊗ V` (or its transpose composite) this forces `U XU†`, `UYU†`, `UZU†` and
  the same for `V` into `{±X, ±Y, ±Z}` (the only traceless involutions of the algebra are `±XZ, ±YY, ±ZX`), i.e. `U, V`
  Clifford; S4 checks that, on the Clifford pairs in 𝒜, "permutes `Z_F`" is exactly "preserves the pattern
  `{(1,3),(2,2),(3,1)}`". So the symmetry group of K inside `(LU ⋊ ⟨T⟩) ⋊ ⟨SWAP⟩` is this finite group of order 384
  (192 without SWAP; 96 unitary).

### (b) Extreme rays and orbits [W2–W3 + X E1–E4, O]
- **W2 (the defects are the non-PSD extreme rays).** [A] Z z1: `z_s = q + Σλ_t z_t` with `q ∈ A` forces `λ_s = 1`.
- **W3 (the PSD extreme rays are exactly the pure states `P_v` with `max_s |⟨ψ_s|v⟩|² ≤ 1/2`).**
  (i) Such `P_v` is extreme in K: if `P_v = Σ kᵢ`, `kᵢ = qᵢ + Σλ_{is}z_s`, then `Q := Σqᵢ = P_v − ΣΛ_s z_s` must be PSD;
  averaging `⟨u|·|u⟩` over an orthonormal basis of `v^⊥` gives `−3ΣΛ/8 + Σ_sΛ_s(1 − |⟨ψ_s|v⟩|²)/4 ≤ −ΣΛ/8`, so `Λ = 0`,
  `Q = P_v`, and the `qᵢ` are multiples of `P_v`.
  (ii) No member of `A` of rank ≥ 2 is extreme: in the face `PSD(R)` of `q`, `R = range q`, extremality needs
  `r² − 1` independent tight constraints among the four (`r = 2`: three; `r ≥ 3`: impossible). For `r = 2`, with
  `Π_R ψ_t ψ_t† Π_R = (|r_t|² I + m_t·σ)/2`, the constraint reads `m_t·p ≤ 1 − |r_t|²` on the Bloch vector `p` of
  `q/tr q`; `Σ_t r_t r_t† = Π_R` [X E4] gives `Σ m_t = 0`, `Σ|r_t|² = 2`; three tight constraints sum to
  `−p·m_4 = 1 + |r_4|²`, forcing `|p| ≥ (1 + |r_4|²)/|r_4|² > 1`: impossible in the ball. [X E3]: a rank-2 member with two
  tight constraints is a sum of two pure members.
  (iii) So `A = cone(S)`, `S = {P_v : max_s |⟨ψ_s|v⟩|² ≤ 1/2}`, and the extreme rays of K are `Z_F ∪ S`.
- **The sum of two defects is not on a face spanned by defects** [X E1]: `z_s + z_t = (T_{ψ_u+ψ_w} + T_{ψ_u−ψ_w})/4`, a sum of
  two pure members of K; `cone Z_F` is not a face of K, and `Σ_s z_s = E00`.
- **Reachability** [X E2 + W]: `ψ_s^T Ω ψ_t = diag(1, −1, 1, −1)` for the determinant form `Ω`, so `v = Σ c_s ψ_s` is a
  product iff `Σ_s ±c_s² = 0`; with free phases this is solvable iff `max |c_s|² ≤ 1/2` (polygon inequality). Hence
  `Ĝ · {pure products} = S`: the pure extreme rays of K are exactly the states reachable by its own symmetry group from
  products, and the unreachable states are the four open caps.
- **Orbits** [X O]: on rays, every finite group listed acts freely on a generic pure extreme ray (orbit = |G|: 16, 48,
  64, 192, 96, 192, 384, 1536) and transitively on the four defects (`⟨cnot⟩` alone: orbit 2, CC2). Under Ĝ the orbits of
  pure extreme rays are labelled by the S4-class of the profile `(|⟨ψ_s|v⟩|²)_s` in the octahedron
  `{p ∈ Δ₃ : max p ≤ 1/2}` (the torus fixes the moduli and moves all relative phases); the defects form one orbit.

### (c) Facial structure [X F + W4]
- `c(x) = dim span{y ∈ K : ipW(x, y) = 0}` (the exposed face of `K = K*` at `x`): **15** on the defects, **9** on pure
  states with all `|⟨ψ_s|v⟩|² < 1/2`, **10** on pure states on one or two cap boundaries. Each value is the exact rank of
  explicit face members and equals the sharp upper bound (rank of `Herm(v^⊥)` plus the tight defects; the hyperplane for a
  defect). For a defect the span is `z^⊥` by the null-cone argument of NOTES-C1 W4 (`pauliW(z)` has one negative and three
  positive eigenvalues).
- **W4.** Since automorphisms of a self-dual cone preserve `c` on extreme rays ([A] Y6), every automorphism of K preserves
  the three classes: defects (`c = 15`), interior pure states (`c = 9`), boundary pure states (`c = 10`).

### (d) The full linear automorphism group [W5: W + L + A]
**`Aut(K(Z_F)) = ℝ₊ × (T³_F ⋊ (S4 × Z2))`**, i.e. scalars times Ĝ: no linear automorphism outside `ℝ₊·𝒜`.
Proof. Let `g ∈ Aut(K)`. By W4, `g` maps the interior pure states (an open set of rank-one PSD matrices) to rank-one
matrices; the 2×2 minors of `g(vv†)` are real polynomials in `v ∈ ℂ⁴ ≅ ℝ⁸` vanishing on an open set, hence everywhere, so
`g` maps every rank-one Hermitian matrix to a rank-one one. An invertible linear map of `Herm(4)` preserving rank one is
`X ↦ ±MXM†` or `±MXᵀM†` ([L, unverified]: the linear-preserver theorem for rank-one Hermitian matrices); the sign is `+`
because PSD rank-one goes to PSD rank-one. So `g ∈ Aut(Q3)`; it permutes the defect rays: `M(I − 2P_s)M† = μ_s(I − 2P_{πs})`.
Summing over `s`: `MM† = (Σμ/2)I − Σ_s μ_s P_{πs}`, diagonal in `{ψ_s}` with entries `m_t`; and
`MP_sM† = Σ_t((m_t − μ_s)/2 + μ_s[t = πs])P_t` has rank one, which forces `m_t = μ_s` for all `t ≠ πs`, for each `s`;
hence all `m_t` and all `μ_s` are equal, `MM† ∝ I`, `M ∝` unitary, `g ∈ ℝ₊·𝒜`, and then `g ∈ ℝ₊·Ĝ` ([A] Z z1). ∎
Consequence: `Aut(K)` is compact modulo scalars, of dimension 3 + 1; it is not transitive on extreme rays (three
`c`-classes) and not homogeneous.

### (e) Uniqueness given the symmetry group: NO [W6: W over X U1–U4 + A EBF]
- **The T³-slice.** For a Ĝ-invariant closed convex cone `K′`, `K′ ∩ Fix = π(K′)` (Haar average over `T³_F`), and if `K′`
  is self-dual so is `K′ ∩ Fix` inside `Fix` (for `y ∈ Fix` pairing nonnegatively with `K′ ∩ Fix`, `⟨y, k⟩ = ⟨y, πk⟩ ≥ 0`).
  [X U1]: `K ∩ Fix = cone{𝟙 − 2e_s} = {d : d_s ≤ Σd/2}` (the reversed simplex cone, self-dual), while `Q3 ∩ Fix = ℝ⁴₊`
  (the simplex cone). Every Ĝ-invariant `K′` with H1 contains `cone(Ĝ·SEP) = cone(S) = A` (b), so its slice contains
  `O := diag(A) = cone{e_s + e_t}` [X U4] and lies in `O* = {d : d_s + d_t ≥ 0}`.
- **A second exotic cone with the same symmetry.** `Circ = {d : Σd/2 ≥ |d − (Σd/4)𝟙|}` is a self-dual S4-invariant cone in
  `Fix` with `O ⊆ Circ ⊆ O*` [X U2]. The seed `C₀ = cone(A ∪ Circ)` is Ĝ-invariant (the torus fixes `Fix` pointwise; S4
  and the transpose preserve Circ and A), closed (`A ∩ −Circ = {0}`: traces), and self-positive (`⟨A, A⟩ ≥ 0`; `⟨a, d⟩ =
  4 Σ_s d_s a_ss ≥ 0` since `diag a ∈ O` and `d ∈ O*`; Circ self-dual). EBF ([A] AUDIT-X; Ĝ compact, `E00` fixed) gives a
  Ĝ-invariant self-dual `K_circ ⊇ C₀`. Then `K_circ ∩ Fix` is self-dual and contains the self-dual Circ, so equals Circ.
  `d1 = (5,1,1,1)/4 ∈ Circ` is not in `K ∩ Fix` and `d2 = (−1,3,3,3)/4 ∈ Circ` is not in `ℝ⁴₊` [X U3]: **`K_circ ≠ K(Z_F)`,
  `K_circ ≠ Q3`.** `K_circ` satisfies H1, H2 at level (ii), SWAP-invariance and every symmetry of K(Z_F); it is
  EXOTIC-E (existence; not exhibited).
- **Surjectivity of the slice map.** The same argument gives, for every S4-invariant self-dual cone `C` in `Fix` with
  `O ⊆ C`, a Ĝ-invariant self-dual `K′` with H1 and `K′ ∩ Fix = C`. Over `C = −Δ` the fibre is `{K(Z_F)}`: such a `K′`
  contains the four defects (they lie in `−Δ`), hence `A + cone Z_F = K(Z_F)`, hence equals it (two self-dual cones, one
  inside the other). Whether the fibre over `Δ` is `{Q3}`, and how large the set of admissible `C` is, is OPEN.
- **Within the surgery class it is unique** [W]: a finite Ĝ-invariant defect set `Z` is `T³_F`-fixed (a connected group
  permuting a finite set fixes it), so each `z ∈ Z` is diagonal, `d = (−a, b, c, e)` up to order; S4-invariance and the
  pairwise orthogonality of Theorem S give `c² + e² = 2ab`, `b² + e² = 2ac`, `b² + c² = 2ae`, whence `b = c = e = a`, i.e.
  `z ∝ z_s`: `K(Z) = K(Z_F)`.

## Gem classification (§A.31)
- NEW: `Aut(K(Z_F)) = ℝ₊ × Ĝ` (no hidden non-orthogonal automorphism; [L] rank-one preserver input named); the pure
  extreme rays of K(Z_F) are exactly the Ĝ-reachable states (`K(Z_F) = cone(Ĝ·SEP) + cone Z_F`); K(Z_F) is not the unique
  exotic cone with its symmetry group (`K_circ`), but it is the unique one whose T³-slice is the reversed simplex.
- ELABORATING: the local symmetry group (384 with SWAP and T), the facial invariant `c ∈ {15, 9, 10}`, `cone Z_F` not a face.
- FAILED prediction kept: `c = 11` on two tight caps (actual 10).
- Assumption-watch marker for C3: the `c`-classes of `K(Z_F)` separate defects from pure states (15 vs 9/10), and in
  every exotic cone met so far the non-PSD extreme rays carry `c ≥ 10`.

## What is not claimed
`K_circ` is not exhibited; the classification of the fibres of the slice map beyond `−Δ` is open; W5 rests on an [L]
input (rank-one preservers), W2 on [A] Z z1, EBF on [A] AUDIT-X.
