# NOTES-C11 — an explicit exotic cone for the order-384 group of HO-14

Node C11 (round 3). Base L = `9f9f8257`; branch `research/countermodels`. Object (HO-14 v1, received 2026-10-10T23:59Z):
`G₃₈₄ = ⟨cnot, actT R_z(π/2), actT cyc3⟩`, the kernel's `cnot` with the octahedral rotations of the target token.
Conventions as in NOTES-C1/C2 and C8: tables 4×4 (index 0 the unit), `ipW` the entrywise sum, `pauliW` a construction
and comparison tool ([D] at L), never a premise; matrix normalization `d = I − cP_h` (`P_h = hh†`, `|h| = 1`) for a
defect, with table `z = E00/2 − (c/8)T_h` (`pauliW(z) = d/8`; `c = 2` is the Bell-type defect `z_g` of C4);
`K(Z) = (Q3 ∩ Z*) + cone Z`; `C_P = P₀⊗I + P₁⊗P` (control-first controlled Pauli; `C_X = CNOT`). For a unit vector `v`
with coefficient matrix `Ψ(v)`, `λ_max(v) = (1 + √(1 − 4|det Ψ(v)|²))/2` is its largest product overlap; `v` is maximally
entangled iff `|det Ψ(v)|² = 1/4`. Open cap of `d = I − cP_h`: `U = {v : |⟨h|v̂⟩|² > 1/c}`; open co-cap
`W = {v : |⟨h|v̂⟩|² > 1 − 1/c}` (`U ⊆ W` for `c ≤ 2`). Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C11 script (2026-10-11T00:11:33Z, `date -u`)

Scratchpad exploration before this point was numerical and is not evidence (orbit sizes, overlaps, a rounding search
for a seed, a numerical pair test of the criterion in 3 below). Predictions, each to be confirmed or refuted by an exact
script whose decision rule is fixed in its header:

1. **The group.** As signed permutations of the sixteen table coordinates, `G₃₈₄` has order 384 (HO-14's value,
   recomputed with my own closure). Its unitary lift has Gaussian-rational representatives (generators `CNOT`, `I⊗S`
   with `S = diag(1, i)`, `I⊗U_J` with `U_J = (I − i(X + Y + Z))/2`), 384 classes modulo `{±1, ±i}`, `Ad` a bijection
   onto the signed-permutation group. Every element is block-diagonal in the control basis,
   `U = P₀⊗A + P₁⊗ωPA` with `A` one of the 24 one-qubit Cliffords (mod phase), `ω ∈ {±1, ±i}`, `P ∈ {I, X, Y, Z}`:
   24 · 4 · 4 = 384.
2. **No Bell-type defect survives (Theorem C11-B).** For all `a, b ∈ ℂ²` and `g = |0⟩⊗a + |1⟩⊗b`:
   `Σ_{P ∈ {X, Y, Z}} |det Ψ(C_P g)|² = |a|²|b|² + |⟨a|b⟩|²` (a polynomial identity). For maximally entangled `g` the sum is
   `1/4`; so at most one of `C_X g, C_Y g, C_Z g` is maximally entangled (and then the other two are products), and one
   has `|det Ψ|² ≤ 1/12`. `C_Y = Ad(I⊗S)·cnot·Ad(I⊗S)⁻¹`, `C_Z` (through `cyc3`) lie in `G₃₈₄`. Consequence: the image of every
   Bell-type defect under some element of `G₃₈₄` leaves `maxCone` (pairing `≤ −√(2/3)` in matrix normalization with a
   product), so **no `G₃₈₄`-invariant cone with H1–H3 contains a Bell-type defect**; in particular no invariant
   pairwise-orthogonal Bell set exists, and the Theorem-S route is closed (stronger than the "non-orthogonal pair"
   obstruction the node anticipated). Already `⟨cnot, actT R_z(π/2)⟩` excludes them. Countercontrol: under `⟨cnot⟩`
   alone the `C2` Bell defects keep a Bell-type orbit.
3. **A surgery theorem for rank-one defects (Theorem S′).** Let `Z = {d_k = I − c_kP_k}` be finite, `c_k ∈ (1, 2]`, with
   `⟨d_j, d_k⟩ ≥ 0` for all `j, k`. If for every ordered pair `j ≠ k` with `⟨d_j, d_k⟩ > 0` the open cap of `d_j` lies in
   the open co-cap of `d_k` (condition (CC)), then `K(Z)` is closed and self-dual. Proof [W] in this file (a minimal-weight
   decomposition plus the local lemma of SD1). For two defects with `⟨d₁, d₂⟩ > 0`, (CC) in both orders is equivalent to
   `c₁c₂|⟨h₁|h₂⟩|² ≥ (√(c₁ − 1) + √(c₂ − 1))²`, and when it fails an explicit `y = vv† + λd₂ ∈ K* \ K` exists (predicted
   sharp: the pair is self-dual iff the inequality holds). Consistency: for `c₁ = c₂ = 2` it says "never, for distinct
   rays" (C4.1); orthogonal Bell sets have all cross pairings 0 and (CC) is vacuous (Theorem S).
4. **HO-14's `φ₀` is the wrong seed for an explicit surgery.** `φ₀ = (1, 2, 3i, −1 + i)/4` is unreachable (every image has
   `|det Ψ|² ≥ 5/256`, attained), its orbit has 384 distinct rays, and it contains an **orthogonal pair**; hence every
   rank-one surgery on its orbit fails, for every `c` in the H1 window `(1, 1/m]`, with an exact witness.
5. **The explicit cone (EXOTIC-X).** `h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`: orbit of 192 distinct rays (stabilizer of
   order 2), unreachable (`m = max λ_max ≈ 0.9566 < 1`), minimal pairwise squared overlap `25/2048` (no orthogonal pair).
   With `c* = 401/400`: H1 (`c*·m ≤ 1`, checked through a rational inequality), all pairings positive, (CC) for every
   pair (`c*²s ≥ 4(c* − 1)`), so `K* := K(G₃₈₄·d*)`, `d* = I − c*P_{h*}`, is an explicit `G₃₈₄`-invariant self-dual cone with
   H1–H3 and `K* ≠ Q3` — CONDITIONAL on Theorem S′ [W]. Countercontrol: at `c = 301/300` the minimal-overlap pair violates
   (CC) and its two-defect surgery has an exact witness (the criterion is sharp at the pair level).
6. **General corollary [W].** Every finite group of unitary conjugations containing `cnot` admits an explicit exotic
   invariant cone (a rank-one orbit surgery with `c` close to 1 on a state that is unreachable and has no orthogonal
   pair in its orbit; both conditions hold on an open dense set of states). Groups with antiunitary elements need the
   extra condition that no element acts as `h ↦ Uh̄` with `U` antisymmetric (such an element makes every state orthogonal
   to its image). This upgrades stage 4's "every finite group is EXOTIC-E" (Y1.5) to EXOTIC-X for finite unitary groups.
7. **T.** Every cone of 5–6 has finitely many non-PSD extreme rays, so C3.3 (Lemma 3) applies: T fails on them; C3.1's
   open class is untouched.

(Results, runs and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T00:20Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c11_octahedral.py` | 1 (00:17:45–00:18:07Z) | 12/12, `VERDICT C11-OCTAHEDRAL-EXACT` | identical (out `9b4fed7b…`) |

Pre-run edits (before the first run; header re-stamped 00:16:53Z): the cap-edge construction of X1/CC1 (the geodesic
direction must be phase-aligned, `w = conj⟨h_j|h_k⟩·u`; a fixed `t`-grid was replaced by the largest `10⁻⁹`-multiple inside
the cap), dead code removed from the characteristic-polynomial helper, and `table` evaluated through the four nonzero
entries of each Pauli product (speed). No check or decision rule was changed after the run.

## Results

### C11-A — the group [X G1–G3, D0]
`G₃₈₄` is a group of 384 signed permutations of the sixteen coordinates, each fixing `E00`. Its unitary lift (generators
`CNOT`, `I⊗S`, `I⊗U_J`, all Gaussian-rational) is a matrix group of order 1536 = 384 · |{±1, ±i}|, and `Ad` maps its 384
classes bijectively onto the signed-permutation group. Every element is `P₀⊗A + P₁⊗ωPA` (block diagonal in the control
basis) with `A` in 24 classes (the one-qubit Clifford group mod phase) and `ωP` in `{±1, ±i} · {I, X, Y, Z}`, all
`24 · 16` combinations occurring. In words: the octahedral group on the target, together with the "Pauli-twisted"
controlled operations `P₀⊗I + P₁⊗ωP`; in particular `C_X = CNOT`, `C_Y`, `C_Z` and the control phase `S⊗I = (P₀ + iP₁)⊗I`
are elements. It contains no antiunitary element.

### C11-B — no Bell-type defect survives [W + X B1, B2]
**Theorem C11-B.** For all `a, b ∈ ℂ²`, with `g = |0⟩⊗a + |1⟩⊗b` and `C_P g = |0⟩⊗a + |1⟩⊗Pb`,
`Σ_{P ∈ {X, Y, Z}} |det Ψ(C_P g)|² = |a|²|b|² + |⟨a|b⟩|²`.
*Proof.* Lagrange's identity gives `|det Ψ(C_P g)|² = |a|²|Pb|² − |⟨a|P|b⟩|²`, and completeness of the Pauli basis gives
`Σ_{P ∈ {I, X, Y, Z}} |⟨a|P|b⟩|² = 2|a|²|b|²`; subtract. [X B1: the identity expands to 0 symbolically.] ∎
For a maximally entangled unit `g` (`|a|² = |b|² = 1/2`, `⟨a|b⟩ = 0`) the sum is `1/4`, each term is `≤ 1/4`, and a term equals
`1/4` exactly when that image is maximally entangled. Hence at most one of `C_X g, C_Y g, C_Z g` is maximally entangled —
and then the other two are products — and the smallest term is `≤ 1/12`, so that image `u` has
`λ_max(u) ≥ (1 + √(2/3))/2` and its defect `I − 2P_u = Ad(C_P)(I − 2P_g)` pairs `1 − 2λ_max(u) ≤ −√(2/3) < 0` with a pure
product. Since `C_X, C_Y, C_Z ∈ G₃₈₄` [X B1] and every cone with H1 and H3 lies in `maxCone = SEP*`:
**no `G₃₈₄`-invariant cone with H1–H3 contains a Bell-type defect.** In particular no invariant pairwise-orthogonal Bell set
exists and the Theorem-S route of the node is closed — more strongly than "every orbit contains a non-orthogonal pair":
every orbit leaves `maxCone`. `C_X` and `C_Y` already suffice (both maximally entangled would need
`|⟨a|Z|b⟩|² = 1/2 > |a|²|b|²`), i.e. the subgroup `⟨cnot, actT R_z(π/2)⟩`. The instances [X B2]: for `C2(1)`, the four `Z_F`
cap vectors and `C1(i)` the ratios are `(1/4, 0, 0)` (the `C_Y` and `C_Z` images are products; the image defect pairs `−1`
with a product); for `Φ⁺`, `(0, 0, 1/4)`. So `K(Z_F)` is not `G₃₈₄`-invariant (HO-14, HO-11 item 3), here because `C_Y` maps
each of its defects onto `I − 2P_p` with `p` a product. Countercontrol [X CC2]: under `⟨cnot⟩` alone `C2(1)` is fixed.

### Theorem S′ — a surgery theorem for rank-one defects [W]
Setting: `Herm(4)` with `⟨A, B⟩ = tr(AB)` (`ipW` is 4 × this on `pauliW` images, so duals agree); `Q = PSD(4)`, self-dual
[K JordanClassification.lean:84]. `Z = {d_1, …, d_n}`, `d_k = I − c_kP_k`, `P_k = h_kh_k†`, `|h_k| = 1`, `c_k ∈ (1, 2]`;
`U_k`, `W_k` the open cap and co-cap of `d_k`.

**Theorem S′.** *Suppose `⟨d_j, d_k⟩ ≥ 0` for all `j, k`, and (CC): for every ordered pair `j ≠ k` with `⟨d_j, d_k⟩ > 0`,
`U_j ⊆ W_k`. Then `K(Z) = (Q ∩ Z*) + cone Z` is closed and self-dual.*

*Proof.* (1) Closed: `tr d_k = 4 − c_k > 0`, so `Q ∩ (−cone Z) = {0}`, and a sum of closed cones meeting only in this way
is closed. (2) `K ⊆ K*`: the four kinds of pairings are `≥ 0` (`Q` self-dual, `Q ∩ Z*` against `Z`, `Z` against `Z`).
(3) `K* = (Q ∩ Z*)* ∩ Z* = (Q + cone Z) ∩ Z*` (`(A ∩ B)* = cl(A* + B*)`, `Q* = Q`, `(Z*)* = cone Z`, the sum closed by (1)).
(4) Let `y ∈ K*`, `y = z + Σs_kd_k` (`z ⪰ 0`, `s ≥ 0`, `⟨y, d_j⟩ ≥ 0` for all `j`). The set
`F = {t ∈ ℝⁿ : t ≥ 0, y − Σt_kd_k ⪰ 0}` contains `s`, is closed and convex, and is bounded (`Σt_k(4 − c_k) ≤ tr y`). Let `t*`
minimize `Σt_k` on `F` and put `q = y − Σt*_kd_k ⪰ 0`. Suppose `⟨q, d_j⟩ < 0` for some `j`. In a spectral decomposition
`q = Σμ_iu_iu_i†` (`μ_i > 0`) some `u = u_i` has `u†d_ju < 0`, i.e. `u ∈ U_j`; and `ker q ⊆ u^⊥`.
 (a) If `t*_j > 0`: for a unit `x ∈ ker q`, `|⟨h_j|x⟩|² ≤ 1 − |⟨h_j|û⟩|² < 1 − 1/c_j ≤ 1/c_j`, so `x†d_jx > 0`: `d_j` is
 positive definite on `ker q`, hence `q + εd_j ⪰ 0` for small `ε > 0` (the block lemma of SD1, step 6 [A] AUDIT-X), and
 `t* − εe_j ∈ F` has a smaller sum: contradiction.
 (b) If `t*_j = 0`: `0 ≤ ⟨y, d_j⟩ = ⟨q, d_j⟩ + Σ_{k≠j} t*_k⟨d_k, d_j⟩` forces some `k ≠ j` with `t*_k > 0` and
 `⟨d_k, d_j⟩ > 0`. By (CC), `u ∈ U_j ⊆ W_k`, so for a unit `x ∈ ker q`, `|⟨h_k|x⟩|² ≤ 1 − |⟨h_k|û⟩|² < 1/c_k`: `d_k` is positive
 definite on `ker q`, and `t* − εe_k ∈ F` has a smaller sum: contradiction.
 Hence `⟨q, d_j⟩ ≥ 0` for all `j`, and `y = q + Σt*_kd_k ∈ K`. So `K* ⊆ K`, and with (2), `K = K*`. ∎

Remarks. (i) For one defect (CC) is vacuous: this is SD1's sufficiency for defects `I − cP`, `c ∈ (1, 2]`. (ii) For an
orthogonal Bell set every cross pairing is 0, so (CC) is vacuous: Theorem S / SD2 (the two routes agree). (iii) For two
distinct non-orthogonal Bell-type defects (`c = 2`) the cap and co-cap coincide and distinct caps of radius `π/4` are not
nested: (CC) fails, as C4.1 requires. (iv) In Fubini–Study terms (`cos²θ_k = 1/c_k`, `cos²θ_jk = |⟨h_j|h_k⟩|²`), `U_j` and
`W_k` are the open balls of radii `θ_j` about `h_j` and `π/2 − θ_k` about `h_k`, so `U_j ⊆ W_k` iff `θ_jk + θ_j ≤ π/2 − θ_k`,
symmetric in `j, k`; equivalently `c_jc_k|⟨h_j|h_k⟩|² ≥ (√(c_j − 1) + √(c_k − 1))²`, and for equal `c`:
`c²|⟨h_j|h_k⟩|² ≥ 4(c − 1)`. (v) The converse for two defects (failure of (CC) gives an explicit `y ∈ K* \ K`) is node C12.

### C11-C — HO-14's `φ₀` seeds no explicit surgery [X Q1 + W]
`φ₀ = (1, 2, 3i, −1 + i)/4`: every image has `|det Ψ|² ≥ 5/256` (attained), so `φ₀` is unreachable (HO-14's
unreachability recomputed); its orbit has 384 distinct rays; the largest overlap with another ray is `s_max = 233/256`;
and exactly one ray `h_k` of the orbit is orthogonal to `φ₀`. For every `c` in the H1 window `(1, 1/m]`,
`m = (8 + √59)/16`, `1/m = 16(8 − √59)/5 ≈ 1.0203`, put `d_l = I − cP_l` over the orbit and
`y = P_{φ₀} + λd_k`, `λ = (c − 1)/(4 − 2c)`. Then `⟨y, d_{φ₀}⟩ = 0`; `⟨y, d_l⟩ ≥ 1 − c·s_max > 0` for every other `l` because
`1/m < 1/s_max` [X: `(2s_max − 1)² < 1 − 4·5/256`]; `h_k†yh_k = λ(1 − c) < 0`. So `y ∈ K* \ K` (a decomposition
`y = q + Σμ_ld_l` would have `0 = ⟨y, d_{φ₀}⟩ ≥ Σμ_l⟨d_l, d_{φ₀}⟩` with every pairing positive, so `y = q ⪰ 0`): **no rank-one
orbit surgery on `φ₀` is self-dual, for any admissible `c`** [W], exact at `c = 517/512` and `101/100` [X Q1]. `φ₀` still
gives the stage-4 EXOTIC-E seed (claim D [A]: the seed set `G₃₈₄·SEP ∪ G₃₈₄·d` is self-positive for every `c` in the window,
and EBF [A] extends it), but that cone is not the surgery.

### C11-D — the explicit cone (EXOTIC-X) [X X1 + Theorem S′ W]
`h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`. Its `G₃₈₄`-orbit has **192** distinct rays (stabilizer of order 2) and is closed
under the three generators; every ray has `|det Ψ|² ≥ 85/2048` (so `m* = (1 + √(427/512))/2 ≈ 0.9566`, unreachable); the
pairwise squared overlaps lie in `[25/2048, 13/16]` — no orthogonal pair. With `c* = 401/400` (the (CC) bound for the
minimal overlap is `2/(1 + √(2023/2048)) ≈ 1.00307`; the H1 bound `1/m* ≈ 1.0454`):
- **H1**: `1 − 4|det Ψ|² ≤ (2/c* − 1)²` for every ray, i.e. `c*·λ_max ≤ 1`; with `|⟨h|x⊗y⟩|² ≤ λ_max(h)|x|²|y|²` (operator
  norm of `Ψ(h)`, [W]) every product state pairs `≥ 0` with every defect, so `SEP ⊆ Q ∩ Z* ⊆ K`;
- **H2**: `Z* := G₃₈₄·d*` is `G₃₈₄`-invariant and `Q` is unitarily invariant, so `K* := K(Z*)` is `G₃₈₄`-invariant, in particular
  `cnot`-invariant;
- **H3**: all pairings `4 − 2c* + c*²s_jk > 0`, (CC) `c*²s_jk ≥ 4(c* − 1)` for all 18336 pairs [X X1]: Theorem S′;
- **`K* ≠ Q3`**: `d*` has eigenvalue `1 − c* = −1/400`.
Table form: `z* = E00/2 − (c*/8)T_{h*}` (recorded in `c11_octahedral.out`), the orbit of 192 tables under `G₃₈₄`.
**`K(G₃₈₄·z*)` is an explicit `G₃₈₄`-invariant exotic cone with H1–H3 — EXOTIC-X, CONDITIONAL on Theorem S′ [W].** It is the
countermodel HO-14 asked for: H1–H3 with the gate and the native octahedral repertoire on one token do not force `Q3`.
Consequence check of S′ (necessary, not a proof) [X X1]: at the far edge of a cap on the minimal-overlap pair and at the
cap's midpoint, the would-be witness `y = P_v + λd_k` is PSD. Sharpness at the pair level [X CC1]: at `c′ = 301/300`
(above the (CC) bound) the same pair has an exact `y ∈ K({d_j, d_k})* \ K({d_j, d_k})`.

### C11-E — every finite unitary group with `cnot` has an explicit exotic cone [W]
Let `Ĝ` be a finite group of unitary conjugations containing `cnot`. The states whose orbit meets the products form a
finite union of images of the real-6-dimensional product cone in `ℂ⁴ ≅ ℝ⁸`; the states with an orthogonal pair in their
orbit lie in `⋃_{U ∉ ℂI} {h : ⟨h|Uh⟩ = 0}`, a finite union of proper real-algebraic sets (`⟨h|Uh⟩ ≡ 0` would force `U = 0`).
So an open dense set of `h` is unreachable with `s_min(h) > 0`, and any `c ∈ (1, min(1/m(h), 2/(1 + √(1 − s_min(h))))]`
gives, by Theorem S′, an explicit `Ĝ`-invariant exotic cone `K(Ĝ·(I − cP_h))` with H1–H3. This upgrades stage 4's Y1.5
("every finite `Ĝ` is EXOTIC-E", over EBF) to EXOTIC-X for finite unitary groups, CONDITIONAL on S′ only. With antiunitary
elements `h ↦ Uh̄` the same holds provided no such `U` is antisymmetric (`⟨h|Uh̄⟩ = h̄ᵀUh̄` vanishes identically exactly
when `U` is antisymmetric); an antisymmetric one (e.g. `(Y⊗I)∘` conjugation, in the Clifford group with the transpose)
makes every `h` orthogonal to its image, so (CC) fails on every orbit and Theorem S′ gives nothing for that group
(whether every rank-one orbit surgery then fails is not decided here; stage 4's EXOTIC-E stands there).

### C11-F — T on these cones
Each cone of C11-D/E has finitely many non-PSD extreme rays and its pure members contain the complement of finitely
many open caps, so Lemma 3 of NOTES-C3 applies: T fails on all of them (C3.3). C3.1's open class (cones with a continuum
of non-PSD extreme rays) is untouched.

## Verdict on node C11
- The group: order 384, the block form `P₀⊗A + P₁⊗ωPA`, no antiunitary element.
- No invariant orthogonal Bell set exists — the node's first route is closed, for a stronger reason than anticipated:
  every Bell-type defect leaves `maxCone` under `C_Y` or `C_Z` (Theorem C11-B).
- Instead of the EBF seed, an **explicit** invariant exotic cone: the rank-one orbit surgery on `h*` at `c* = 401/400`
  (EXOTIC-X, CONDITIONAL on Theorem S′ [W], a written proof of this round). HO-14's `φ₀` cannot seed one (orthogonal pair).
- General: every finite unitary group with `cnot` is EXOTIC-X (C11-E).

## Gem classification (§A.31)
- NEW: Theorem S′ (self-dual surgery over non-orthogonal, non-Bell defects under the cap/co-cap condition); the explicit
  `G₃₈₄` cone; EXOTIC-X for every finite unitary group (stage 4 had EXOTIC-E); Theorem C11-B (the sum identity) and the
  orthogonal-pair obstruction for `φ₀`.
- Assumption-watch marker: "an explicit cone needs Bell-type (c = 2) defects, so a group without Bell-type defects is
  EXOTIC-E only" (the reading of stage 4's `G_H` / Clifford rows) is false: small-cap defects with nested cap/co-cap
  geometry give explicit self-dual surgeries; the obstruction for finite groups is orthogonality inside an orbit, not the
  absence of Bell-type defects.
- Pressure test of the favourable reading: the proof of S′ re-derived twice; its necessary consequences checked exactly
  at the extreme points of the (CC) margin; its pair-level sharpness checked by an exact witness just past the bound;
  every exact input of the cone (orbit closure, H1 inequality, (CC) for every pair) checked over the whole orbit.

## What is not claimed
No kernel statement; Theorem S′ is [W] (written proof, this round, not audited); the operator-norm bound for H1 is [W]
(standard); EXOTIC-X here means "exhibited exactly, with self-duality from a written theorem", as for K(Z_F) (Theorem S).
Nothing about groups with a continuous part (there a finite defect set cannot be invariant, NOTES-C5 W2).
