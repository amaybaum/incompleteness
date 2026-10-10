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

**Provenance note (added 2026-10-10T23:01Z, `date -u`).** The time in the S0 heading above is an estimate; by file
modification time this section was last written at 22:40:29 UTC, before `c7_ebf_wall.py` run 1 (22:42:03). The header
times inside `c7_ebf_wall.py` and `c7_circle.py` are likewise estimates (LOG, correction entry); the order S0 → script →
run is as stated.

## Runs

| script | runs | final | replay |
|---|---|---|---|
| `c7_ebf_wall.py` | 2 | run 2: 8/8, `VERDICT C7-EBF-WALL-EXACT` (run 1 5/7 kept: a Float from Python-int inputs caught by C1; CC-R's slack identity mis-stated as `−Σp/2`, correct `−Σp/2 − p_s`, conclusion unchanged) | identical (out `43d18e5d…`) |
| `c7_circle.py` | 1 | 7/7, `VERDICT C7-CIRCLE-EXACT` (pre-run edits: B5's orthonormal completion `|0+⟩, |1−⟩`; CC1 by an exact 2×2 determinant) | identical (out `983a6e86…`) |

## Results

### W1 — the canonical closed form over Circ fails [W + X D2]
For an S4-invariant self-dual `C ⊆ Fix` with `O ⊆ C ⊆ O*` put `K^C := (Q3 ∩ π⁻¹(C)) + C` ("diagonal surgery": the whole
slice as defects). It is Ĝ-invariant (`T³_F` fixes `Fix` pointwise, S4 × ℤ₂ preserves `C`), closed (`Q3 ∩ −C = {0}`),
self-positive, contains `A` (`π(A) = O ⊆ C`), so it has H1 and H2 at level (ii); `K^R = K(Z_F)` (`diag_ψ(𝟙 − 2e_s) =
8 pauliW(z_s)`, [X W0]) and `K^{ℝ⁴₊} = Q3`.
**`K^Circ` is not self-dual.** `y_d = (−2, 12, 6, 4)/5` lies on `∂Circ`; its dual ray is `y_d' = (12, −2, 4, 6)/5` and
`u(y_d') = −u(y_d)`, so by the equality case of Cauchy–Schwarz `Circ ∩ y_d'^⊥ = ℝ₊y_d`: `y_d` is an extreme ray [X C1].
With `v = ψ_2 + ψ_3/2` (profile `p = (0, 1, 1/4, 0) ∉ Circ`) and `c₀ = y_d − p ∈ int Circ`, put `y = P_v + diag_ψ(c₀)`.
(i) `y ∈ (K^Circ)*`: for `q ∈ Q3 ∩ π⁻¹(Circ)`, `tr(yq) = tr(P_v q) + ⟨c₀, π(q)⟩ ≥ 0`; for `c ∈ Circ`, `tr(yc) = ⟨y_d, c⟩ ≥ 0`.
(ii) `y ∉ K^Circ`: if `y = q + c`, then `π(q) + c = y_d` with both terms in Circ, so `π(q) ∈ ℝ₊y_d`; `π(q) ≥ 0` and
`y_d` has a negative entry, so `π(q) = 0`, `q = 0`, and `y = c` would be diagonal; but `⟨ψ_2|y|ψ_3⟩ = 1/2` [X D2]. ∎
Countercontrol [X CC-R]: for R no `p ≥ 0, p ≠ 0` has `(𝟙 − 2e_s) − p ∈ R` (the three facet slacks sum to `−Σp/2 − p_s`),
consistent with the self-duality of `K(Z_F) = K^R`.

### W2 — Theorem C7-D: forced non-fixed defects [W + X D2]
*Let `K'` be a `T³_F`-invariant self-dual cone with slice `C = K' ∩ Fix`. Suppose `C` has property (N): a non-PSD extreme
ray `y_d` and a pure `P_v`, `v` with at least two nonzero `ψ`-coordinates, with `y_d − π(P_v) ∈ C`. Then `K'` has a
non-PSD extreme ray outside `Fix`.*
Proof. Suppose every non-PSD extreme ray of `K'` lies in `Fix`; call their set `Z ⊆ C`, and let `P'` be the cone of the
PSD extreme rays, so `K' = P' + cone Z` and `K' = K'* = P'* ∩ Z*`. Put `y = P_v + c₀`, `c₀ = y_d − π(P_v) ∈ C ⊆ K'`.
`y ∈ P'*` (`P' ⊆ Q3`, and `c₀ ∈ K'`), `y ∈ Z*` (`tr(yz) = ⟨y_d, z⟩ ≥ 0`, both in `K'`), so `y ∈ K'`. Write `y` as a sum of
extreme rays `e_i` of `K'`: `Σ π(e_i) = y_d` with `π(e_i) ∈ C`, so `π(e_i) ∈ ℝ₊ y_d`, and `π(e_i) ≠ 0` (for `e ≠ 0` in a
self-positive `T³`-invariant cone, `0 = ⟨e, π(e)⟩ = ∫⟨e, ge⟩dg` would force `e = 0`); `y_d` has a negative entry, so every
`e_i` is non-PSD, hence in `Fix`, hence `y` is diagonal — but `y` has the off-diagonal entries of `P_v`. ∎
**Corollaries.** (a) Every Ĝ-invariant self-dual cone with H1 and slice Circ (every `K_circ`) has non-PSD extreme rays
outside `Fix`; their `T³_F`-orbits have positive dimension, so `K_circ` has a continuum of non-PSD extreme rays off
`Fix`. (b) No surgery `(Q3 ∩ Z*) + cl cone Z` with `Z ⊆ Fix` — finite or infinite — has slice Circ and is self-dual
(this contains W1). (c) R fails (N) [X CC-R]: the theorem is silent for `K(Z_F)`, as it must be.

### W3 — the sandwich and the gap [W + X D4]
Every Ĝ-invariant self-dual `K'` with H1 and slice Circ satisfies `C₀ := A + Circ ⊆ K' ⊆ C₀* = (Q3 + R) ∩ π⁻¹(Circ)`
(`A* = Q3 + R` by NOTES-C2 (e); `C₀` is self-positive since `π(A) = O ⊆ Circ*`). The gap is not empty and carries
incompatible pairs: `P_v` with `v = 5ψ_1 + 3ψ_2 + 3ψ_3 + ψ_4` (a cap state, profile `(25, 9, 9, 1) ∈ Circ \ O`) and
`w = P_u + ½ diag_ψ(−1, 1, 1, 1)`, `u = (ψ_1 − ψ_2 − ψ_3 + ψ_4)/2`, both lie in `C₀*` and `tr(w P_v) = −3`. Hence `C₀*`
is not self-positive, `P_v, w ∈ C₀* \ C₀`, and no `K'` contains both. Each of them is compatible with `C₀` and with its
own Ĝ-orbit (`tr(P_u · g diag_ψ(−1,1,1,1)) = 1/2` for every coordinate permutation, `⟨z, gz⟩ ∈ {0, 4}`; `P_v`'s orbit is
PSD and its profile lies in Circ), so EBF ([A] AUDIT-X) gives a `K'_v ∋ P_v` and a `K'_w ∋ w`, both with slice Circ
(a self-dual slice containing Circ is Circ): **the fibre of the slice map over Circ has at least two members** —
CONDITIONAL on EBF. This is the precise sense in which `K_circ` is a choice, not an object.

### W4 — the fibre over the simplex slice is not {Q3} [W + X D5]
`y5 = u u† + 8 diag_ψ(−1, 1, 1, 1)`, `u = 3ψ_1 + ψ_2 + ψ_3 + ψ_4`: `π(y5) = (1, 9, 9, 9) ≥ 0`, `x†y5x = −12` at
`x = 3ψ_1 − ψ_2 − ψ_3 − ψ_4` (not PSD; at the coefficient 6 instead of 8 the table is PSD [X CC-Q]). Pairings: `y5` pairs
nonnegatively with `A` (`(𝟙 − 2e_1)·O ≥ 0`) and with `ℝ⁴₊` (`π(y5) ≥ 0`); within its Ĝ-orbit `⟨y5, g y5⟩ ≥ 160` (dropping
`|⟨u, gu⟩|² ≥ 0`: `2·8·(−6) + 64·4` when `g` fixes coordinate 1, `8·(10 + 10)` otherwise; the transpose acts on the real
`u` trivially). EBF over `cl cone(A ∪ ℝ⁴₊ ∪ Ĝ·y5)` gives a Ĝ-invariant self-dual `K'_Δ` with H1, slice `ℝ⁴₊` (self-dual,
containing `ℝ⁴₊`) and `K'_Δ ∋ y5 ∉ Q3`: **the fibre over the simplex slice is not {Q3}** — CONDITIONAL on EBF. (C2.8's
first half.) `K'_Δ`'s non-PSD extreme rays all lie off `Fix` (its slice has none).

### W5 — the full Bell-circle surgery fails [X c7_circle]
`Z_circ = {I − 2gg† : g = cos θ ψ_1 + sin θ ψ_3}` (every `g` maximally entangled [X B1]); `cone Z_circ` is a 3-dimensional
Lorentz cone, so `K(Z_circ)` is the natural explicit candidate with a continuum of non-PSD extreme rays. Two members of
`K(Z_circ)*`, `y_i = v_i v_i† + (189/1000) d_{g_i} + I/1000` (rational data), satisfy `Z_circ*` strictly [X B3] and
`tr(y1 y2) = −475586012673053754301/30445958586078125000000 < 0` [X B4]: `K(Z_circ)*` is not self-positive, so
**`K(Z_circ)` is not self-dual**. A unitary `U` maps the circle onto the κ-fixed circle `C2` (`e^{iθ}U g_θ = C2(e^{2iθ})`)
[X B5], so `K(Z_{C2})`, which is κ- and `cnot`-invariant at level (i), is not self-dual either: the natural explicit
continuum cone for the κ node fails. (The data come from a numerical search; the certificate is exact.)

## Verdict on node C7
- **No explicit exotic self-dual cone with a continuum of non-PSD extreme rays was exhibited.** The three natural
  closed forms fail with exact certificates: the diagonal surgery over Circ (W1), every surgery with `T³`-fixed defects
  and slice Circ (W2), the full Bell-circle surgery and its κ-invariant copy (W5).
- **Structural obstruction (W2):** for a slice with property (N) — Circ has it, R does not — the cone's non-PSD extreme
  rays cannot all be `T³`-fixed; the defects must form non-trivial torus orbits. Membership in such a cone then involves
  the pairing of whole orbits, `min_D ⟨X, D Y D†⟩`, a phase-synchronization minimum over the torus, for which no surgery
  formula is available; this is the reason the EBF cones resist closed forms (an explanation, not a theorem).
- **Sandwich with the gap named (W3):** `A + Circ ⊆ K_circ ⊆ (Q3 + R) ∩ π⁻¹(Circ)`, the gap containing cap states and
  non-PSD non-diagonal tables in incompatible pairs; the fibre over Circ has ≥ 2 members, over the simplex ≥ 2 (W4), over
  R exactly one (NOTES-C2).
- **T:** nothing new is exhibited explicitly, so C3.1 remains OPEN. For every `K_circ`, Lemma 1 of NOTES-C3 gives
  `c(P00) = 9`; the `c`-values of its off-`Fix` defects are not determined here.

## Gem classification (§A.31)
- NEW: Theorem C7-D (forced non-fixed defects); the fibre over Circ is not a singleton and the fibre over the simplex is
  not {Q3} (both CONDITIONAL on EBF); the full Bell-circle surgery (and the κ-invariant C2 copy) is not self-dual.
- FAILED constructions kept with certificates: `K^Circ`; `K(Z_circ)`; `K(Z_{C2})`.
- Assumption-watch marker: "an explicit EBF cone is a surgery whose defect set is a continuum" is false for the
  Ĝ-invariant slice Circ in its diagonal form and for Bell circles; any explicit construction must handle non-fixed
  defect orbits.

## What is not claimed
No `K_circ` is exhibited; EBF ([A]) carries W3's and W4's existence statements; the "why no closed form" item is an
explanation; T is not decided for any EBF cone.
