# NOTES-C13 — B3.C's residual region from the cone side

Node C13 (round 3). Object: C10.3's residual region of Conjecture B3.C — compact `G ∋ cnot` whose identity component is
a torus `H₀` with simple spectrum, in which every entangled eigenline is `G`-equivalent to a product eigenline — with
HO-10 v1 (received 2026-10-10T23:59Z) in hand: there B3.C holds at CONJECTURE + claim (D) (existence). Conventions as
in NOTES-C10–C12: `E₊`, `E₋` the `+1`, `−1` eigenspaces of `CNOT` (`E₋ = ℂ|1−⟩`); `b_k` an eigenbasis of `H₀`, `b̂_k`
normalized; `Ω(u, w) = (u₀w₃ + u₃w₀ − u₁w₂ − u₂w₁)/2` the symmetric form with `Ω(v, v) = det Ψ(v)`; `Π` the group of
eigenline permutations induced by `G`; defects `I − cP_h`; Theorem S′ and the cap/co-cap condition (CC) of NOTES-C11.
Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of any C13 script (2026-10-11T00:50:00Z, `date -u`)

Scratchpad exploration before this point was numerical and is not evidence (the basis below, `λ_max` along the orbit
circles, the overlap minimum over the orbit, the S2 circle).

1. **Theorem S′ for arbitrary defect sets.** The proof in NOTES-C11 uses only that an element of `K*` is
   `z + Σ_{k ≤ n} s_kd_k` with finitely many defects (true for any compact `Z` with `tr > 0`: `cone Z` is closed and every
   element is a finite combination), so S′ holds for compact `Z`, including continua; with a common `c` every defect is
   an extreme ray.
2. **The orthogonal-pair obstruction (Lemma C13-O).** For any set `Z` of defects `I − cP_h` with a common `c ∈ (1, 2)`
   containing `h ⊥ h′`: `y = P_h + λd_{h′}`, `λ = (c − 1)/(4 − 2c)`, has `⟨y, d_l⟩ ≥ c(1 − |⟨h|h_l⟩|²) ≥ 0` for every `l`,
   `⟨y, d_h⟩ = 0` and `h′†yh′ < 0`, so `K(Z)` is not self-dual (this also removes the side condition of NOTES-C11 C11-C).
3. **The minimal group has no residual case.** In `G = closure⟨H₀, cnot⟩`, `cnot` induces at most one transposition of
   eigenlines (`dim E₋ = 1`); if it swaps a product eigenline `b₁ = x⊗y` (`⟨b₁|CNOT|b₁⟩ = 0`) with the entangled
   `b₂ = CNOT b₁`, the other two eigenlines span `E₊ ∩ span(b₁, b₂)^⊥`, whose two product lines are not orthogonal: one
   of `b₃, b₄` is an entangled `cnot`-fixed eigenline, and C10.2's single-defect cone is explicit. Exact instance:
   `b₁ = (2, 3)⊗(2, −1 + 2i)`, `b₂ = CNOT b₁`, `b₃ = |0⟩⊗(1 + 2i, 2)`, `b₄ = (10, −5 + 10i, −6 − 12i, −6 − 12i)`
   (entangled, `λ_max(b₄) ≈ 0.7812`), with `K({I − (32/25)P_{b₄}})` explicit. So the residual region needs eigenline
   permutations beyond `cnot`'s.
4. **Dichotomy in the residual region (maximal torus).** With `H₀` the maximal torus of this basis and `Π ∋` `cnot`'s
   transposition `(12)`: either `Π` fixes a product eigenline (only possibility: `Π = S₃` on `{1, 2, 4}`, `b₃` fixed) and
   rank-one orbit surgeries on states dominated by `b₃` satisfy (CC) for small `c` — **an explicit exotic cone with a
   continuum of non-PSD extreme rays**; or `Π` contains a double transposition and every `G`-orbit of states contains an
   orthogonal pair, so by Lemma C13-O no rank-one orbit surgery with a common `c` is self-dual.
5. **Case A (`Π = S₃`): EXOTIC-X.** `G_A = T³ ⋊ ⟨cnot, g⟩`, `g` the monomial transposition `b̂₁ ↔ b̂₄`;
   `h = (9 + 2i)b₃ + b₁` (weights `p = 85/98` on `b̂₃`, `13/98` on `b̂₁`); its orbit is three circles
   `{√p b̂₃ + √(1 − p)e^{iθ}b̂_j}`, `j ∈ {1, 2, 4}`, product-free (exact), with pairwise squared overlaps
   `≥ min(p², (2p − 1)²) = (36/49)²`; at `c = 251/250`: H1 on each circle (exact; tight, `c·λ_max ≈ 0.9990` on the circle
   through `b₂`), (CC) for all pairs, so `K(G_A·(I − cP_h))` is a `G_A`-invariant self-dual cone with H1–H3, `≠ Q3`,
   whose non-PSD extreme rays form three circles — the first explicit exotic cone with a continuum of non-PSD extreme rays
   (C7.7's question, for this node). Slice `ℝ⁴₊` (all four eigenlines reachable), consistent: `π(d_h) ∈ ℝ⁴₊`.
6. **Case B (`Π = ⟨(12), (34)⟩`): obstruction.** `G_B = T³ ⋊ ⟨cnot, g′⟩`, `g′` the transposition `b̂₃ ↔ b̂₄`: residual
   (`b₂ ~ b₁`, `b₄ ~ b₃`); for the unreachable `h_B = 2b₁ + b₂` the orbit contains `h′ = b₁ − 2b₂ ⊥ h_B`; the exact witness of
   Lemma C13-O; EXOTIC-E stands (HO-10 / claim D).
7. **Corollary for stage 4's torus node S2 (`actC R_z(θ) ∘ actT R_x(φ)`).** Without G16: the orbit of
   `h = 3|0+⟩ + |1−⟩` is the non-Bell circle `{3|0+⟩ + w|1−⟩}` (`cnot` and the torus act by relative phases),
   `λ_max ≡ 9/10`, overlaps `≥ 16/25`; at `c = 21/20` the circle surgery is an explicit exotic cone (C5.3/C5.4: explicit cone
   OPEN — now settled at level (i)). With G16, `Ad(I⊗Z)` induces the double transposition `|0±⟩ ↔ |0∓⟩`, `|1±⟩ ↔ |1∓⟩`
   and the orthogonal-pair obstruction applies (the 2-torus still reaches the orthogonal partner).
8. **T on the continuum cones (preview of C14).** Lemma 2 of NOTES-C3 does not apply to the new cones: the pure members
   of `K` on a defect's null quadric lie in a second quadric (the tangency condition of the neighbouring caps), so they
   have empty interior there; the facial invariant of the defects is predicted `≤ 14`.

(Runs, results and the written proofs follow below this line after the runs.)

## Runs (written 2026-10-11T00:54Z, `date -u`)

| script | runs | final | replay |
|---|---|---|---|
| `c13_residual.py` | 1 (00:53:18Z) | 9/9, `VERDICT C13-RESIDUAL-EXACT` | identical (out `cabe7692…`) |

Pre-run edits (before the first run): R1's kernel statement made a rank statement (the first draft only showed that
`|1−⟩` lies in the kernel), and an unused line removed. Cosmetic, recorded: R1's detail prints `⟨L_A|L_B⟩` as a pair of
Fractions `(9, −6)`, i.e. `9 − 6i`.

## Results

### C13-S — Theorem S′ for arbitrary compact defect sets; extremality [W]
*Theorem S′ (NOTES-C11) holds verbatim for every compact set `Z` of defects `I − c_dP_d` (`c_d ∈ (1, 2]`) with pairwise
pairings `≥ 0` and (CC) for every pair with positive pairing.* Proof: `cone Z` is closed (`Z` compact, `tr d ≥ 2`, so
`0 ∉ conv Z`) and every element of it is a finite combination; so every `y ∈ K* = (Q + cone Z) ∩ Z*` is
`z + Σ_{k ≤ n}s_kd_k`. The minimal-weight argument runs on these finitely many defects; for any `d₀ ∈ Z` (listed or not)
with `⟨q, d₀⟩ < 0`, either `d₀` carries positive weight (local lemma) or `0 ≤ ⟨y, d₀⟩` forces a listed `d_k` with positive
weight and `⟨d_k, d₀⟩ > 0`, and (CC) for `(d₀, d_k)` makes the decrease of `t_k` feasible. ∎
*With a common `c`, every `d ∈ Z` is an extreme ray of `K(Z)`*: if `d₀ = k₁ + k₂`, `k_i = q_i + Σ_j t_{ij}d_j`, then
`T_j := t_{1j} + t_{2j}` satisfies `ΣT_j ≤ 1` (trace) and `Σ_jT_j(1 − c|⟨h₀|h_j⟩|²) ≤ h₀†d₀h₀ = 1 − c` (PSD parts
nonnegative at `h₀`), while the left side is `≥ (1 − c)ΣT_j ≥ 1 − c`; equality forces `q₁ = q₂ = 0` and `T_j > 0` only for
`h_j = h₀`. ∎ So a surgery on a continuum `Z` has a continuum of non-PSD extreme rays.

### C13-O — the orthogonal-pair obstruction [W + X R3]
**Lemma C13-O.** *Let `Z` be any set of defects `I − cP_h` with one `c ∈ (1, 2)`, containing `d_h`, `d_{h′}` with `h ⊥ h′`.
Then `K(Z)` is not self-dual.* With `λ = (c − 1)/(4 − 2c)` and `y = P_h + λd_{h′}`: for every `d_l ∈ Z`,
`⟨y, d_l⟩ = (1 − c s_{hl}) + λ(4 − 2c + c²s_{h′l}) = c(1 − s_{hl}) + λc²s_{h′l} ≥ 0` (`s` the squared overlaps), so
`y ∈ K*`; `⟨y, d_h⟩ = 0` and `⟨d_l, d_h⟩ ≥ 4 − 2c > 0` force any decomposition `y = q + Σt_kd_k` to have `t = 0`, but
`h′†yh′ = λ(1 − c)|h′|² < 0`. ∎ [X R3: the identity exactly at sample points, the witness at `c = 101/100` and `3/2`.]
This supersedes the side condition used for `φ₀` in NOTES-C11 C11-C (there `⟨y, d_l⟩ ≥ c(1 − s) ≥ 0` holds outright).
For `c = 2` (Bell) the lemma is void (`λ = ∞`), as Theorem S requires.

### C13-M — the minimal group has no residual case [W + X R0, R1]
Let `H₀` be a torus with simple spectrum normalized by `cnot`, `G = closure⟨H₀, cnot⟩`. `cnot` permutes the eigenlines as
an involution, and since `dim E₋ = 1` it has at most one transposition. Suppose it swaps a product eigenline `b₁` with an
entangled one, `b₂ = CNOT b₁`. Then `b₁ − b₂ ∈ E₋`, so `E₋ ⊆ span(b₁, b₂)` and `span(b₃, b₄) ⊆ E₊`; `cnot` fixes `b₃`, `b₄`.
The products in `E₊` are `|0⟩⊗ℂ²` and `ℂ²⊗|+⟩`. Write `b₁ = x⊗y`; `b₂` entangled excludes `x₀ = 0`, `x₁ = 0` and
`y ∝ |±⟩`. Then `|0⟩⊗ℂ²` meets `span(b₃, b₄)` in the line `L_A = |0⟩⊗y^⊥` and `ℂ²⊗|+⟩` in the line `L_B = x^⊥⊗|+⟩`, and
`⟨L_A|L_B⟩ = (x^⊥)₀⟨y^⊥|+⟩ ≠ 0` (`(x^⊥)₀ = 0` would put `x ∝ |0⟩`; `⟨y^⊥|+⟩ = 0` would put `y ∝ |+⟩`) — in the instance
`⟨L_A|L_B⟩ = 9 − 6i` [X R1]. So `span(b₃, b₄)` has no orthonormal product basis: one of `b₃, b₄` is an entangled
`cnot`-fixed eigenline, a one-line `G`-orbit free of products, and C10.2 gives an explicit single-defect cone (instance:
`K({I − (32/25)P_{b₄}})`, H1 exact, spectrum `(−7/25, 1, 1, 1)`, X's condition [A] AUDIT-X). If `cnot` fixes every
eigenline and some eigenline is entangled, C10.2 applies again. **So the residual region of C10.3 is empty for
`G = closure⟨H₀, cnot⟩`; it needs elements of `G` that permute eigenlines beyond `cnot`.**

### C13-Π — a dichotomy in the residual region (maximal torus) [W]
Let `H₀ = T³` be the maximal torus of an eigenbasis, `G = T³ ⋊ Π̃` with `Π ⊆ S₄` the induced eigenline permutations. For
`σ ∈ Π` and a state `h` the overlap `⟨h|Dσ̃h⟩ = Σ_k h̄_kd_k(σ̃h)_k` has free phases `d_k`, so `G·h` contains an orthogonal pair
iff for some `σ ≠ e` the moduli `|h_k||h_{σ⁻¹k}|` satisfy the polygon inequality. (i) A subgroup of `S₄` without a fixed
point contains a double transposition (orbits of sizes `{4}` or `{2, 2}`), and for a double transposition the moduli come
in equal pairs: **every `G`-orbit contains an orthogonal pair**, and by Lemma C13-O no rank-one orbit surgery with a common
`c` is self-dual. (ii) If `Π` fixes an eigenline `k₀`, a state with `|h_{k₀}|² > 1/2` has, for every `σ`,
`|h_{k₀}|² > Σ_{k≠k₀}|h_k||h_{σ⁻¹k}|` (Cauchy–Schwarz), hence all orbit overlaps `≥ (2|h_{k₀}|² − 1)²`: (CC) holds for small
`c`, and if `h` is unreachable S′ gives an explicit cone. In the residual region a `Π`-fixed eigenline is a product.

### C13-A — case A: an explicit exotic cone with a continuum of non-PSD extreme rays [X R2 + W]
`G_A = T³ ⋊ ⟨cnot, g⟩` on the basis of R0 (`b₁ = (2, 3)⊗(2, −1 + 2i)`, `b₂ = CNOT b₁`, `b₃ = |0⟩⊗(1 + 2i, 2)`,
`b₄ = (10, −5 + 10i, −6 − 12i, −6 − 12i)`), `g` the monomial transposition `b̂₁ ↔ b̂₄`: `Π = S₃` on `{1, 2, 4}`, `b₃` (a
product) fixed, the entangled `b₂, b₄` each `G_A`-equivalent to the product `b₁` — a residual case of C10.3, with
identity component `T³` (simple spectrum) and `cnot ∈ G_A`. `h = (9 + 2i)b₃ + b₁` (weight `p = 85/98` on `b̂₃`): its orbit
is the three circles `{√p b̂₃ + √(1 − p)e^{iθ}b̂_j}`, `j ∈ {1, 2, 4}`; on each, `min_θ |det Ψ|² = (1 − p)(2√p A − √(1 − p)B)²`
with `(A², B²) = (9/52, 0), (4/117, 20/117), (5/117, 20/117)`, all positive (product-free: `h` is unreachable) and above the
H1 threshold at `c = 251/250` [X R2]; overlaps within a circle `≥ (2p − 1)²`, between circles `= p²`, so `s_min = (36/49)²`
and (CC) holds. By S′ (compact `Z`) **`K_A := K(G_A·(I − cP_h))` is a `G_A`-invariant self-dual cone with H1–H3, `≠ Q3`,
whose non-PSD extreme rays are three circles** (EXOTIC-X, CONDITIONAL on S′ [W]) — an explicit answer, for this node, to
C7.7 (an explicit exotic self-dual cone with a continuum of non-PSD extreme rays). Its `T³`-slice is `ℝ⁴₊` (all four
eigenlines reachable; `π(d_h) = (21237/24500, 1, 633/4900, 1) ∈ ℝ⁴₊`, consistent). The H1 window is narrow (on the circle
through `b₂`, `c·λ_max ≈ 0.9990` at `c = 251/250`; at `c = 101/100` H1 fails [X CC3]); dominance on the fixed `b₃` is needed
(the orbit of `h_B = 2b₁ + b₂` has an orthogonal pair already under `cnot` [X CC2]).

### C13-B — case B: the obstruction [X R3 + W]
`G_B = T³ ⋊ ⟨cnot, g′⟩`, `g′` the transposition `b̂₃ ↔ b̂₄`: `Π = ⟨(12), (34)⟩`, residual (`b₂ ~ b₁`, `b₄ ~ b₃`). Every
`G_B`-orbit contains an orthogonal pair (C13-Π (i)); for the unreachable `h_B = 2b₁ + b₂` (both orbit circles product-free)
the partner is `h′ = b₁ − 2b₂ = D·CNOT h_B`, and Lemma C13-O's witness is exact [X R3]. **No rank-one orbit surgery with a
common `c` is self-dual for `G_B`**; EXOTIC-E stands (HO-10 item 2, CONDITIONAL on claim (D) [A]). An explicit cone for
`G_B` would need defects of another kind or several values of `c` (not attempted).

### C13-S2 — corollary for stage 4's torus node S2 [X R4 + W]
`T² = {actC R_z(θ) ∘ actT R_x(φ)}` commutes with `cnot` and is diagonal in `(|0+⟩, |0−⟩, |1+⟩, |1−⟩)` with four distinct
characters [X R4]. **Without G16**: the orbit of `h = 3|0+⟩ + |1−⟩` (weights `9/10, 1/10`) under `T² × ⟨cnot⟩` is the
non-Bell circle `{3|0+⟩ + w|1−⟩ : |w| = 1}` (the torus and `cnot` act by the relative phase), with `λ_max ≡ 9/10` and
overlaps `≥ 16/25` [X R4]; at `c = 21/20` H1 (`c·9/10 ≤ 1`) and (CC) hold, so the circle surgery is an explicit
`T²`- and `cnot`-invariant exotic cone (EXOTIC-X, CONDITIONAL on S′ [W]) — C5.3/C5.4's explicit torus cone, at level (i).
Its Bell member (`p = 1/2`, the circle `C1`) fails (CC) (antipodal points orthogonal [X CC1]), consistent with stage 4's
`K_T` and C7.6. **With G16**: `Ad(I⊗Z)` induces the double transposition `|0±⟩ ↔ |0∓⟩`, `|1±⟩ ↔ |1∓⟩` [X R4], the
`G16`-images of the circle are orthogonal to it, and every orbit has orthogonal pairs (the 2-torus reaches them: the two
equal-modulus pairs cancel by one parameter each, by the intermediate value theorem), so Lemma C13-O closes the rank-one
route at level (ii); EXOTIC-E stands there.

### C13-T — T on the continuum cones (bound) [W]
For a defect `d₀` of a circle surgery `K(Z)` (`Z = {U_αd₀U_α†}`, `U_α = e^{iαH}`, `h₀` not an eigenvector of `H`), every
`y` in the exposed face `K ∩ d₀^⊥` is in `Q ∩ Z*` (all pairings with `d₀` are positive) and `α ↦ ⟨y, U_αd₀U_α†⟩ ≥ 0`
vanishes at `α = 0`, so its derivative `⟨y, i[H, d₀]⟩` vanishes: the face lies in the 14-dimensional subspace
`d₀^⊥ ∩ (i[H, d₀])^⊥`, and **`c(d₀) ≤ 14`** (`≤ 15 − k` for a `k`-dimensional torus orbit). With Lemma 1 of NOTES-C3
(`c(P00) = 9` for every cone with H1–H3), T on these cones turns on whether `c(d₀) = 9`; not decided here (node C14).

## Verdict on node C13
- The residual region of C10.3 does not occur for `G = closure⟨H₀, cnot⟩` (C10.2 is explicit there); it needs further
  eigenline permutations, and then a dichotomy: `Π` fixes a (product) eigenline — explicit continuum surgery by S′ (case A,
  exhibited exactly); `Π` contains a double transposition — every orbit has an orthogonal pair and no rank-one orbit
  surgery is self-dual (case B, exact witness); EXOTIC-E (HO-10, claim D) remains the only statement there.
- First explicit exotic cones with a continuum of non-PSD extreme rays: case A (three circles) and the S2 torus node
  without G16 (one circle). C7.7 and C5.4 are answered for these nodes; κ with G16, the S2 node with G16 and `K_circ`
  remain OPEN, each now with the orthogonal-pair obstruction to the rank-one route (`K_circ`: its eigenline group S4
  contains double transpositions).

## Gem classification (§A.31)
- NEW: S′ for continua (the EBF wall is not a wall for groups whose eigenline action fixes a product eigenline); the
  orthogonal-pair obstruction (Lemma C13-O); the minimal-group lemma (the residual region needs more than `cnot`); the
  fixed-point dichotomy for maximal tori; explicit continuum cones for a residual B3.C case and for the torus node S2 at
  level (i).
- Assumption-watch marker: "explicit cones need finitely many defects, so torus nodes are EXOTIC-E only" (the reading of
  C5.3/C7.7) is false; the operative obstruction is an orthogonal pair inside an orbit (double transpositions), not the
  continuum.

## What is not claimed
No kernel statement; S′ (compact form), Lemma C13-O, C13-M, C13-Π and the orbit descriptions are [W] (this round); the
explicit cones are CONDITIONAL on S′. Degenerate 2-tori (C10.3's second item) not attempted; explicit cones for `G_B`, the
S2 node with G16, κ with G16 and `K_circ` remain OPEN.
