# NOTES-C18 — explicit cones where rank-one surgeries with a common `c` fail

Round-4 node C18, opened 2026-10-11T04:55Z (`date -u`), while C17's second design run was queued. Targets (HO-25 items 4
and 5): B3.C's case B — `G_B = T³ ⋊ ⟨cnot, g′⟩` on the basis `b₁ … b₄` of NOTES-C13 R0, eigenline group
`Π = ⟨(12), (34)⟩` (a double transposition, so every orbit has an orthogonal pair, C13-Π) — and stage 4's torus node S2
with G16 — `G_S2 = closure⟨T², cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` on `B = (|0+⟩, |0−⟩, |1+⟩, |1−⟩)` (C13-S2). Attempts, in the
order the node fixes: (1) surgeries with two or more values of `c`; (2) rank-two defects; (3) a non-surgery construction
(a Π-invariant perturbation of `Q3`, self-dual for a modified inner product, HO-19 item 3's filter as the hint). A FAILED
attempt is recorded as a result. Conventions as in NOTES-C11 and NOTES-C13; `K(Z) = (Q ∩ Z*) + cone Z`, defects
`d = I − cP_h`, H1 = `SEP ⊆ K`, H3 = self-duality under `tr(AB)`.

Hypothesis classification (standing rule 1): the three attempts are cone geometry for two fixed groups; the groups'
invariance is the hypothesis under test ((b)-instances for the operations generating them), H1 and H3 are the
introduced conditions of the composite-cone question (H1–H3, not OI premises), and no OI inventory item is used.

## S0 — predictions and decision rules, written before the first run of any C18 script (2026-10-11T04:55Z, `date -u`)

### Attempt 1 — two or more values of `c`

Written claim to be tested (Lemma C18-1, the max-`c` orthogonal pair): *let `Z` be any set of defects `I − c_lP_{h_l}`
with every `c_l ∈ (1, 2)`, containing `d_h`, `d_{h′}` with `h ⊥ h′` and `c_h = c_{h′} = c* = max_l c_l`. Then `K(Z)` is not
self-dual.* With `λ = (c* − 1)/(4 − 2c*)` and `y = P_h + λd_{h′}` the pairing with any `d_l` is
`⟨y, d_l⟩ = c*(1 − s_{hl}) + (c* − c_l)(s_{hl} + λ) + λc*c_l s_{h′l} ≥ 0` (an identity), `⟨y, d_h⟩ = 0`, every
`⟨d_l, d_h⟩ ≥ 4 − c_l − c* > 0`, and `h′†yh′ = λ(1 − c*) < 0`. Since every `G_B`-orbit and every `G_S2`-orbit carries an
orthogonal pair and `c` is constant on orbits, the orbit of largest `c` supplies the pair.

Checks of `experiments/c18_attempts.py` for this attempt: A1-id (the identity, symbolically in `c*, c_l, s, s′`);
A1-B (case B: `h = (2, 1, 0, 0)/√5`, `h′ = (1, −2, 0, 0)/√5` in `b̂` coordinates, `h′ = D·CNOT h`; two orbits with
`c* = 51/50` and `c₂ = 101/100`; the witness's pairings with sample defects of both orbits computed from matrices,
equal to the identity and `≥ 0`; `h′†yh′ < 0`); A1-S2 (the same with `h = 3|0+⟩ + |1−⟩`, `h′ = (I⊗Z)h`, and a second
orbit); A1-cc (countercontrol: two values of `c` on one orbit, the witness built on the smaller `c` has a negative
pairing with the larger-`c` copy of `d_h`); A1-Bell (S2 only: a mixture containing the Bell circles `C1 ∪ C2` at
`c = 2`, where the lemma does not apply — the witness on the circle `3|0+⟩ + w|1−⟩` at `21/20` pairs negatively with
the Bell defect at `w = 1`, while on the orbit of `(1, 1, 1, i)/2` (partner `(Z⊗I)h`) every Bell pairing is `≥ (c* − 1)/2`).

Predictions: all pass; A1-Bell gives one negative and one nonnegative family. Decision rule: if A1-id, A1-B, A1-S2 and
A1-cc pass, attempt 1 is **FAILED** for case B outright (no orbit of `G_B` is admissible at `c = 2`, C16.2) and for S2
with G16 whenever every orbit has `c < 2`; the S2 mixtures with the Bell circles are recorded as decided where the
witness survives and OPEN otherwise. If A1-id or a control fails, the lemma is withdrawn and the attempt stays OPEN.

### Attempt 2 — rank-two defects

Two readings, both tested. (a) **Rank-two negative part** (`d = I − c₁P_{h₁} − c₂P_{h₂}`, `h₁ ⊥ h₂`, `c_i > 1`; more
generally any `d` with two negative eigenvalues). Written claim (Lemma C18-2): on `ℂ²⊗ℂ²` every two-dimensional subspace
contains a product vector (the determinant restricted to it is a binary quadratic form), so `d` is not block-positive,
`d ∉ SEP*`, and no cone with H1 and H3 contains `d`, for any group. (b) **Rank-two subtracted part, one negative
eigenvalue** (`d = I − R`, `R = cP_h + aP_k`, `h ⊥ k`, `c > 1 > a ≥ 0`). The only sufficiency theorem in hand is the engine
`selfDual_of_local` (C17); written claims: its local condition fails for any pair of defects whose negative
eigenvectors are orthogonal and whose pairing is positive, so the engine needs zero pairing on every such pair; zero
pairing needs `tr R ≥ 2` and the engine's single-defect condition needs `tr R ≤ 2`, so `a = 2 − c` (balanced) and the
planes `span(h, k)` of orthogonal partners must be orthogonal. For case B this can be met: `h = (2, 3, 0, 6)/7` in `b̂`
coordinates has exactly the orthogonal partners `D·σ̃h` (`σ = (12)(34)`, `d₂ = −d₁`), and `k ∝ (2/7, 3/7, 0, −13/42)` makes
every such pair orthogonal plane-wise. Checks: A2a (an exact product vector in the negative plane of
`I − c₁P_{h₁} − c₂P_{h₂}` for a Bell pair and for a non-Bell pair, `p†dp < 0`; control: a rank-one defect within H1 has
`p†dp ≥ 0` at the maximising product); A2b-partners (the partner set of `h` exactly: no partner from `e`, `(12)`, `(34)`;
the `(12)(34)` family `d₂ = −d₁`); A2b-zero (the four overlaps `⟨h|gk⟩`, `⟨k|gh⟩`, `⟨k|gk⟩`, `⟨h|gh⟩` vanish identically on
that family, symbolically); A2b-near (the engine's local condition fails for a nearby pair `d`, `UdU†`,
`U = diag(e^{iθ}, 1, 1, 1)` with a small Gaussian-rational phase: an exact `u` in the cap of `d` and `x ⊥ u` with
`x†(UdU†)x < 0`; control: at `U = I` the same `x` gives `x†dx > 0`).

Predictions: all pass. Decision rule: A2a passing ⇒ reading (a) **FAILED** for every group (H1). A2b passing ⇒ reading
(b) **FAILED as a construction**: the engine cannot certify a balanced rank-two surgery on a torus orbit whose generator
couples `h` and `k`; the non-self-duality of such surgeries is not shown and is recorded OPEN. If A2b-zero fails, the
partner analysis is wrong and reading (b) is OPEN.

### Attempt 3 — a Π-invariant perturbation of `Q3`

Reading: cones `A(Q3)` for an invertible linear `A` commuting with the group's action on `Herm(4)`, self-dual either
for `tr(AB)` directly or for a modified inner product `tr(X M(Y))` (`M` positive definite, commuting with the group) and
then transported by the filter `M^{1/2}`. Written claims (Lemma C18-3): (i) `A(Q3)` is self-dual for `tr` iff `A*A` is a
positive self-adjoint automorphism of `Q3`, i.e. `X ↦ SXS` with `S > 0`, so `A(Q3) = U(Q3)` for an orthogonal `U`; a cone
self-dual for `M` is `M^{-1/2}` of a `tr`-self-dual cone, so the filter adds nothing; (ii) for both groups the diagonal
subgroup has six inequivalent irreducible off-diagonal blocks, so a commuting orthogonal `U` is `O ⊕` (a Schur multiplier
by a unimodular `M`); (iii) every eigenline projector is in `G·SEP ⊆ K` (case B: `b₁, b₃` products, `b₂ = CNOT b₁`,
`b₄ = g′b₃`; S2: `B` is a product basis), so `O⁻¹` maps each `e_k` to a nonnegative unit vector: a permutation `τ`; the
2×2 minors at a product with full support force `p_{τj}p_{τk} ≥ p_jp_k`, so `τ = e`; then PSD at that product forces `M`
to be a coboundary and `U(Q3) = Q3`. Also (iv) the `T`-slice of any invariant self-dual cone with H1 is `ℝ⁴₊` (all four
eigenline projectors are in it). Checks: A3-perm (for each permutation `τ ≠ e` commuting with `Π` an exact product
violating `p_{τj}p_{τk} ≥ p_jp_k`, both groups); A3-schur (the non-coboundary multiplier `M₁₂ = −1` gives a non-PSD image
of an exact full-support product; control: a coboundary multiplier keeps it PSD); A3-irr (the six off-diagonal
characters of the diagonal subgroups pairwise inequivalent, both groups); A3-slice (the eigenline projectors as images
of products under group elements, exactly).

Predictions: all pass. Decision rule: all pass ⇒ attempt 3 **FAILED** for commuting linear perturbations (with or
without the modified inner product); non-linear constructions are not attempted and the explicit-cone question for both
nodes is recorded OPEN, existence staying at claim (D) [A] (HO-10, C13.6) for case B and at EXOTIC-E for S2 with G16.

`VERDICT C18-EXACT` iff every check gives the predicted outcome, the controls included.

## Runs (written 2026-10-11T05:03Z, `date -u`)

- Run 1 (05:01:20Z): 12/13, `VERDICT C18-FAIL`. The failing check was A3-perm, on an auxiliary prediction of this S0:
  "centralizers of order 8" for both groups. For case B the centralizer of `Π = ⟨(12), (34)⟩` in `S₄` is `Π` itself
  (order 4: a permutation commuting with both transpositions preserves `{1, 2}` and `{3, 4}`); for S2's `(12)(34)` it is
  dihedral of order 8. The substantive part of the check — every non-identity permutation in the centralizer refuted by
  a full-support product — passed in run 1. Kept as `c18_attempts.run1.{py,out,err}`. The prediction "order 8" for case B
  FAILED.
- Run 2 (05:01:41Z): the order assertion corrected to the computed groups (`Π`, and order 8), nothing else changed;
  13/13, `VERDICT C18-EXACT`. Replay byte-identical (`cmp`).
- Parameter choice for A2b-near (the Gaussian-rational phase and the cap point) was made with a float scratch
  computation after S0 and before run 1 (not part of the record); the recorded check is exact.

## Results

### C18-1 — attempt 1, two or more values of `c`: FAILED (route closed) [W + X A1-id, A1-B, A1-S2, A1-cc, A1-Bell]
**Lemma C18-1.** *Let `Z` be any set of defects `I − c_lP_{h_l}` with every `c_l ∈ (1, 2)`, containing `d_h, d_{h′}` with
`h ⊥ h′` and `c_h = c_{h′} = c* = max_l c_l`. Then `K(Z)` is not self-dual.* Proof: `λ = (c* − 1)/(4 − 2c*)`,
`y = P_h + λd_{h′} ∈ Q + cone Z`; for every `d_l`, `⟨y, d_l⟩ = (1 − c_ls_{hl}) + λ(4 − c* − c_l + c*c_ls_{h′l})
= c*(1 − s_{hl}) + (c* − c_l)(s_{hl} + λ) + λc*c_ls_{h′l} ≥ 0` (A1-id, using `1 + λ(4 − 2c*) = c*`), so `y ∈ K*`;
`⟨y, d_h⟩ = 0` while every `⟨d_l, d_h⟩ ≥ 4 − c_l − c* > 0`, so a decomposition `y = q + Σt_kd_k` (`q ∈ Q ∩ Z*`) has `t = 0`
and `y = q ⪰ 0`; but `h′†yh′ = λ(1 − c*)|h′|² < 0`. ∎ (Lemma C13-O is the case of one value of `c`.)
**Corollary.** For `G_B` every invariant rank-one surgery with H1 is non-self-dual, whatever the number of orbits and the
values of `c`: no orbit is admissible at `c = 2` (C16.2), `c` is constant on orbits and its maximum over a compact `Z` is
attained on an orbit, and that orbit has an orthogonal pair (C13-Π). For `G_S2` with G16 the same holds when every orbit
has `c < 2` (every orbit has an orthogonal pair, C13-S2). Exact instances: A1-B (orbits of `(2, 1, 0, 0)` at `51/50` and
`(1, i, 2, 1 + i)` at `101/100`, 33 sample defects, minimum pairing 0, `h′†yh′ = −1/980`), A1-S2 (circle orbit at `21/20`
and the orbit of `(1, 1, 1, i)` at `41/40`, 58 samples, `h′†yh′ = −1/76`). The maximum is load-bearing (A1-cc: on one
orbit with `c ∈ {101/100, 51/50}` the witness built on the smaller value pairs `−199/19800` with the larger copy of `d_h`).
**S2 with the Bell circles.** If `Z` contains `C1 ∪ C2` at `c = 2` (the only orbit admissible there, C16.2) the lemma does
not apply. The witness on the largest `c < 2` survives when its state stays at squared overlap `≤ 1/2` with every Bell
state: on the orbit of `(1, 1, 1, i)/2` (partner `(Z⊗I)h`) at `c* = 11/10` every Bell pairing is
`(c* + 1)/2 − 2s_b + 2λc*s′_b ≥ (c* − 1)/2 = 1/20` (A1-Bell), so those mixtures are not self-dual either; on the circle
orbit `3|0+⟩ + w|1−⟩` at `21/20` the witness pairs `−23/40` with the Bell defect at `w = 1` and leaves `K*`. Mixtures of the
second kind are not decided (OPEN); they carry orthogonal pairs with positive pairing in their `c < 2` part, so neither
S′ nor the engine of C17 applies to them.

### C18-2 — attempt 2, rank-two defects: FAILED [W + X A2a, A2b-partners, A2b-zero, A2b-near]
(a) **Lemma C18-2.** *On `ℂ²⊗ℂ²` a Hermitian `d` with two negative eigenvalues is not block-positive.* The span `W` of two
negative eigenvectors is a 2-plane; `det Ψ` restricted to `W` is a binary quadratic form, which has a nonzero root `p ∈ W`;
`p` is a product and `p†dp < 0`. ∎ Under H1 (`SEP ⊆ K`) and H3 such a `d` lies in no cone, for any group (A2a: the Bell
pair `(|00⟩ + |11⟩, |01⟩ + |10⟩)` and the pair `(3|00⟩ + |11⟩, |01⟩ + 3|10⟩)`, `p†dp = −3/2, −3`; control: the rank-one
defect `I − (10/9)P_{3|00⟩+|11⟩}` is `≥ 0` on 144 products and `0` at `|00⟩`).
(b) **One negative eigenvalue, rank-two subtracted part** (`d = I − R`, `R = cP_h + aP_k`). The engine of C17 needs, for
every pair of defects with positive pairing, `d_k` positive definite on `u^⊥` for every `u` in the cap of `d_j`. For a pair
whose negative eigenvectors are orthogonal, `u = h_j`, `x = h_k` violate it, so the engine needs zero pairing on all such
pairs: `⟨d, d′⟩ = 4 − 2t + tr(RR′)` with `t = tr R` needs `t ≥ 2`, and the engine's condition on a single defect (spectrum
`1 − c, 1 − a, 1, 1`) needs `c − 1 ≤ 1 − a`, i.e. `t ≤ 2`; so `a = 2 − c` (balanced) and `RR′ = 0`: the partners' planes
`span(h, k)` must be orthogonal. For case B this can be met (NEW): `h = (2, 3, 0, 6)/7` in `b̂` coordinates has no
orthogonal partner under `T³`, `cnot` or `g′` (one coefficient dominates: `36 > 4 + 9`, `36 > 6 + 6`, `9 > 4`) and under
`cnot·g′` exactly the family `d₂ = −d₁` (A2b-partners); with `k ∝ (2/7, 3/7, 0, −13/42)` (`⊥ h`) every partner's plane is
orthogonal to `span(h, k)` identically on that family (A2b-zero). But a balanced defect is tight at its cap boundary inside
`span(h, k)`, and a torus generator coupling `h` and `k` breaks the local condition for nearby pairs: with
`U = diag((399 + 40i)/401, 1, 1, 1)`, `c = 3/2`, the cap point `u = h − (83/50)i·k` and `x ⊥ u` in `span(h, k)` give
`x†(UdU†)x = −672234517517/81106356240000 < 0` while `x†dx = 5759/6480000 > 0` and `⟨d, UdU†⟩ > 0` (A2b-near). So the engine
certifies no balanced rank-two surgery on a `T³`-orbit of case B; whether such surgeries are self-dual is not decided
(OPEN), and H1 for them was not examined. No explicit cone results.

### C18-3 — attempt 3, a Π-invariant perturbation of `Q3`: FAILED for commuting linear perturbations [W + L + X A3-*]
**Lemma C18-3.** *(i) For invertible linear `A` on `Herm(4)`, `A(Q3)` is self-dual for `tr(AB)` iff `A*A ∈ Aut(Q3)`; then
`A(Q3) = U(Q3)` with `U = A(A*A)^{-1/2}` orthogonal. (ii) A cone self-dual for `tr(X M(Y))` (`M` positive definite) is
`M^{-1/2}` of a `tr`-self-dual cone, so the filter adds nothing beyond (i). (iii) If `A` commutes with `G_B` (or with
`G_S2`) and `A(Q3)` has H1, then `A(Q3) = Q3`.* Proof: (i) `(AQ)* = A^{-*}Q`, so `AQ = (AQ)*` iff `A*A Q = Q`; a positive
definite self-adjoint element of `Aut(Q3)` has its square root in `Aut(Q3)` (polar decomposition of the automorphism
group of a symmetric cone [L: Faraut–Korányi, Analysis on Symmetric Cones, Ch. I]), so `A(Q3) = U((A*A)^{1/2}Q3) = U(Q3)`.
(ii) `K = M^{-1}K*` gives `(M^{1/2}K)* = M^{1/2}K`. (iii) `A*A` commutes with the group, hence so does `U`. The diagonal
subgroup (case B: `T³`; S2: `⟨T², cnot, Z⊗I⟩`) has six pairwise inequivalent non-real characters on the off-diagonal
blocks (A3-irr), so `U = O ⊕ S_M` with `O` orthogonal on the diagonal and `S_M` the Schur multiplier by a unimodular
Hermitian `M`. Every eigenline projector lies in `G·SEP ⊆ U(Q3)` (A3-slice), so `O⁻¹e_k ≥ 0` for each `k`: `O⁻¹` is a
permutation `τ` commuting with the eigenline action. At a product with full support the 2×2 minors of `U⁻¹(P_p)` give
`p_{τ(j)}p_{τ(k)} ≥ p_jp_k`; every `τ ≠ e` of the centralizer is refuted by an exact product (A3-perm). With `τ = e`,
`U⁻¹(P_p) = D_xM̄D_x†` is PSD iff `M ⪰ 0`, i.e. `M` is a coboundary `vv†` and `U = Ad(diag v)`, so `U(Q3) = Q3` (A3-schur:
`M₁₂ = −1` gives a negative 3×3 minor; a coboundary gives a rank-one image). ∎ Also: the slice of every invariant
self-dual cone with H1 is `ℝ⁴₊` for both groups (all four eigenline projectors are in it), so slice-based constructions
(C2.6's `K_circ` type) cannot differ from `Q3` on the slice here. Non-linear constructions were not attempted.

## Verdict on node C18
- The three attempts the node fixes all FAIL for case B and for S2 with G16, each with a scoped reason: several values of
  `c` do not evade the orthogonal-pair obstruction (Lemma C18-1; S2 mixtures with the Bell circles partly OPEN); rank-two
  negative parts are excluded by H1 (Lemma C18-2), and balanced rank-two defects, which can be arranged to have zero
  pairing on every orthogonal pair (NEW for case B), lose the strict room the engine needs on the torus continuum;
  commuting linear perturbations of `Q3` are `Q3` (Lemma C18-3).
- Explicit cones for case B and for S2 with G16 remain OPEN. Existence stays where it was: case B CONDITIONAL on claim (D)
  [A] (HO-10 item 2, C13.6), S2 with G16 EXOTIC-E. No new explicit cone, so nothing new for C21.

## Gem classification (§A.31)
- NEW: Lemma C18-1 (the obstruction survives any re-weighting by `c`; the orbit of largest `c` carries it); Lemma C18-2;
  balanced rank-two defects with orthogonal partner planes for case B, and the tightness mechanism that defeats them on a
  torus continuum; Lemma C18-3 and the forced slice `ℝ⁴₊`.
- Assumption-watch marker: "an explicit cone needs only a better choice of defects or weights" — for a group with a
  continuum of orbit points and orthogonal pairs in every orbit, the available sufficiency engine needs zero pairing on
  orthogonal pairs and strict room at cap boundaries at once; rank-one defects give the second, balanced ones the first.
  A construction for these nodes needs a sufficiency argument of another kind.

## What is not claimed
No kernel statement (the engine is C17's design module; Lemmas C18-1 to C18-3 are [W]); non-self-duality of balanced
rank-two surgeries; S2 mixtures with the Bell circles where the witness leaves `K*`; non-linear perturbations of `Q3`;
anything about OI's composite cone beyond the two group nodes.
