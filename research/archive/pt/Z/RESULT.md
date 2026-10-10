# Thread Z (COUNTERMODELS) — stage 4, Q-EX — RESULT (research only)

Protocol: `PROTOCOL-STAGE4.md` (`d3da2811…`) with the texts it names; coordinator's amendment (erratum in the
reachability sketch; groups stated with identity component and component group) recorded in NOTES N1. Base L =
`9f9f8257…` (read-only). Evidence levels: [K] certified at L, [W] written argument, [X] exact computation
(instance-scoped unless lifted by [W]), [N, numerical] guidance only, [L, unverified]. Notation: `ρ(w) = pauliW w`,
`⟨w,v⟩ = ipW w v = 4 tr ρ(w)ρ(v)`; `T_ψ` the pure table of ψ; `R(Ĝ) = Ĝ·{pure products}`;
`f(ψ) = max_{φ∈R}|⟨ψ|φ⟩|²`; Bell-type defect `e_ψ = E00/2 − T_ψ/4`; `K(Z) = (Q3 ∩ Z*) + cone Z`.

## 0. Answer

**Bottom line.** Every node assigned to Z is EXOTIC: S0, S1, S2, S3 (the protocol's `actC Rx(θ)`), and every
finite extension of G16. So is the target-z variant (record). In each, a cone satisfying H1–H3 and invariant
under the node's group need not be Q3. The cone is explicit where the node's group fixes a finite orthogonal Bell
orbit (K(Z_F)); elsewhere it exists by EBF over a seed exhibited exactly, with its overlap bound proved on the
whole reachable set. The one UNIQUE node Z found is a record node, S3-g (below). Four findings change the picture
the protocol drew:
- **(D) The gap between the two criteria is empty** [W over X], for compact Ĝ ⊆ Aut(Q3) ∩ O(ipW) containing cnot:
  EXOTIC(existence) ⟺ R(Ĝ) ≠ all pure states ⟺ criterion 1 fails. For ψ ∉ R the seed is
  `αE00 − T_ψ/4` with `α = max(1/2, f(ψ)) < 1`: `ρ` has eigenvalue `(α−1)/4 < 0`,
  `⟨e, T_φ⟩ = α − |⟨ψ|φ⟩|²`, `⟨e, ge⟩ = α² − α/2 + |⟨ψ|gψ⟩|²/4 ≥ 0`. Reachability alone decides every symmetry
  node; the protocol's "middle regime" is exotic (it is S3).
- **The finite-extension conjecture is REFUTED** [W over X]. `G_H = ⟨G16, Ad(I⊗H)⟩` (finite, order 128, inside
  `⟨G16, actT SO(3)⟩`) and the even Clifford group `G_Cl` (order 23040) admit no Bell-type defect. Both are still
  EXOTIC(existence) by (D), with exact seeds. In fact every finite group is EXOTIC(existence) [W].
- **Node S3 depends on the axis** [W + X]. For a control rotation about `n`, `cnot(n·σ⊗I) = n·σ⊗P₊ + n′·σ⊗P₋`
  with `n′ = (−n_x, −n_y, n_z)`. For a target rotation about `m`,
  `cnot(I⊗m·σ) = |0⟩⟨0|⊗m·σ + |1⟩⟨1|⊗m″·σ` with `m″ = (m_x, −m_y, −m_z)`.
  - Equatorial axes (control) and axes ⊥ x (target) generate a 2-torus. EXOTIC(existence) is proved exactly for
    control x and target z, by conjugation for control y, and [W] by the same invariant pattern for the rest.
  - Every other axis that does not commute with cnot generates su(2) on one sector. Every pure state is then
    reachable, and the node is **UNIQUE** by criterion 1.
  - So a node strictly weaker than S4 already forces Q3, and S4 is not a minimal UNIQUE node. This is a
    cross-thread note; thread Y decides UNIQUE nodes.
- **The explicit torus-invariant cone (stage 3's open item) is not obtained; the natural candidate fails exactly.**
  - The only G16⋊T²-invariant Bell-type surgery, `K_T`, satisfies H1 and the node's invariance but is not
    self-dual: an exact pair `y, w ∈ K_T*` has `ipW(y, w) = −24/625`.
  - Two Bell-type defects at squared overlap `c ∈ (0, 1/2)` already break the surgery: `tr(yw) = c − 1/(4c)`.
  - Stage 3's [N] "no violation" guidance (x7 N4) never sampled these elements.

| node | group: identity component; component group | verdict | countermodel / seed (exact) | evidence |
|---|---|---|---|---|
| S0 `G16` | trivial; G16 (16) | EXOTIC | `K(Z_F)` (stage 3, re-checked) | [W+X] stage 3; z1 |
| S1 `⟨G16, SWAP⟩` | trivial; order 48 | **EXOTIC** | `K(Z_F)`; its full stabilizer in 𝒜 = {Ad U, Ad U∘T} is `T³_F ⋊ ⟨G16,SWAP⟩`: identity component T³_F (unitaries diagonal in the basis {ψ_s}, dim 3, non-local), component group S4×Z2 (48) | [W+X] z1 |
| S2 `⟨actC Rz ∘ actT Rx, G16⟩` | T²_c (dim 2); G16/⟨Ad(Z⊗I)⟩ (8) | **EXOTIC(existence)**; explicit cone UNRESOLVED | seed: Bell defects `e_φ`, φ on the circles `C1 = {(\|0+⟩+e^{iγ}\|1−⟩)/√2}`, `C2 = {(\|0−⟩+e^{iγ}\|1+⟩)/√2}` (exactly the Bell seeds of S2; F at C1(0)); also admissible for `⟨T³, G16⟩` (T³ ∋ cnot, e^{iχZ⊗X}, dim 3) | [W] EBF over [X] z2c; K_T refuted [X] z2e |
| S3 `⟨G16, actC Rx(θ)⟩` | T²_x = exp span{X⊗I, X⊗X} (dim 2); G16 (16) | **EXOTIC(existence)**; no Bell-type defect | `(7/8)E00 − T_ψ/4`, ψ = (15,−1,7,7)/18, `f(ψ) = 1/2 + 5√137/162 ≤ 7/8` | [W+X] z3 |
| S3-z (record) `⟨G16, actT Rz(θ)⟩` | T²_z = exp span{I⊗Z, Z⊗Z} (2); order 4 | **EXOTIC(existence)** | `(24/25)E00 − T_ψ/4`, ψ = (7,4,0,4)/9 | [W+X] z5 |
| S3-g (record) generic axis, e.g. `actC R_{(3,0,4)/5}(θ)` or `actT R_{(3,4,0)/5}(θ)` | contains `{I⊗P₊ + V⊗P₋}` / `{\|0⟩⟨0\|⊗I + \|1⟩⟨1\|⊗V}`, V ∈ SU(2) (algebra dim 4) | **UNIQUE** (criterion 1) | none can exist | [W+X] z5 |
| FE: subgroups of `Stab_Cl(Z_F)` (order 1536), e.g. Gbig (64), ⟨Gbig, SWAP⟩ (192) | finite | **EXOTIC** | `K(Z_F)` | [X] z1, z4 |
| FE `G_S = ⟨G16, Ad(S⊗I)⟩` (32) | finite | **EXOTIC(existence)** | Bell seed e_F (orbit of 8, not orthogonal) | [W+X] z4 |
| FE `G_H = ⟨G16, Ad(I⊗H)⟩` (128) | finite | **EXOTIC(existence)**; no Bell-type defect | `(9/10)E00 − T_ψa/4`, ψa = (15,−1,7,7)/18, m = 4160/6561 | [W+X] z4 |
| FE `G_Cl` (Clifford ∪ Clifford∘T, 23040) | finite | **EXOTIC(existence)**; no Bell-type defect | `(99/100)E00 − T_ψa/4`, m = 6272/6561 | [W+X] z4 |
| FE, every finite group ⊇ G16 | finite | **EXOTIC(existence)** | (D): R is a finite union of 4-dim sets | [W] |
| S4, S5, H, T, F, V, C | — | not decided by Z (thread Y / record); Z has no countermodel for them | — | — |

(m = max over the group of the squared token-1 Bloch length of the image; f = (1 + √m)/2.)

**Excluded, with scope.**
- No G16⋊T²_c-invariant surgery with Bell-type defects is self-dual. The only candidate is `K_T`, and it fails.
- A plain surgery with two Bell-type defects at squared overlap in (0, 1/2) is never self-dual.
- No Bell-type defect exists for S3, `G_H`, `G_Cl`, or any group containing `G_H`.
- K(Z_F) is not invariant under any one-parameter group of local maps.

Scope: the pair carrier `W 3`, with H1–H3 as fixed at stage 3 and invariance under the stated group. Every
existence result goes through EBF [W, audited at stage 3]. Nothing here concerns other carriers or non-symmetry
conditions.

**Necessity evidence for thread Y's UNIQUE nodes.** Every lattice symmetry node strictly weaker than S4 that Z
examined is EXOTIC, except the generic-axis S3-g, which is itself UNIQUE. Finite extensions and the
commuting/equatorial one-parameter extensions are never UNIQUE. So among symmetry conditions, the minimal UNIQUE
candidates are "cnot + one generic one-parameter local rotation group" (S3-g); the rest of the minimality question
is Y's.

## 1. Node by node

### 1.0 The two criteria, re-derived, and claim D (NOTES N3)
- **Criterion 1** (reachability ⇒ UNIQUE) is correct as stated, for any group. A Ĝ-invariant K ⊇ SEP contains
  `cone R(Ĝ)`. If R is every pure state, `K ⊇ Q3`, and H3 gives `K = K* ⊆ Q3* = Q3` [K JordanClassification.lean:84].
- **Criterion 2** (Bell-type defect ⇒ EXOTIC via EBF) is correct. The identities used are
  `⟨e_ψ,e_φ⟩ = |⟨ψ|φ⟩|²/4`, `⟨e_ψ, T_φ⟩ = 1/2 − |⟨ψ|φ⟩|²` and `ρ(e_ψ) = (I − 2ψψ*)/8` (re-verified exactly in z1 C1).
  The overlap bound on R is equivalent to "`U⁻¹ψ` is maximally entangled for every g = Ad(U)(∘T) in Ĝ", because
  the largest squared Schmidt coefficient is ≥ 1/2, with equality iff the state is maximally entangled.
- **Claim D** [W; seed identities exact in z3 R4, z4 F5, z5 T2]. Take ψ ∉ R. R is compact, so `f(ψ) < 1`. With
  `α = max(1/2, f(ψ))`, the seed `C = cone(Ĝ·SEP ∪ Ĝ·(αE00 − T_ψ/4))` is:
  - Ĝ-invariant and subdual, by the three identities in §0;
  - closed, since its generating set is compact and lies in `⟨E00, ·⟩ > 0` (`⟨E00, e⟩ = α − 1/4`);
  - compact-group admissible (Ĝ fixes E00).

  EBF then gives a Ĝ-invariant self-dual `K ⊇ C` with `K ∋ e ∉ Q3`. Conversely, an exotic Ĝ-invariant K contains
  some `e ∉ Q3` that pairs nonnegatively with R and with its own orbit. The dimension corollary [W]: if
  `dim R(Ĝ) < 6`, the node is EXOTIC(existence). This holds for every finite group (R is a finite union of
  images of `S²×S²`) and every torus node below.

### 1.1 S0 (G16) — EXOTIC, explicit (stage 3, re-checked)
- z1 re-establishes the certificates of `K(Z_F)`: `ρ(e_s) = (I − 2ψ_sψ_s*)/8` with `ψ_s = (1, s1s2, s1, −s2)/2`,
  Gram `I/4`, `⟨e_t, T_s⟩ = ∓1/2`.
- H1 holds by the symbolic identity `2(1 − x·M_s y) = |x − M_s y|² + (1 − |x|²) + (1 − |y|²)`.
- The landed cnot equals Ad(CNOT) on all 16 basis tables, and `|G16| = 16`.
- H3 rests on stage 3's Theorem S / SD2 (audited).

### 1.2 S1 (token exchange) — EXOTIC, explicit, the same cone (z1)
- SWAP = Ad(SWAP) (exact). `SWAP ∉ G16`, `|⟨G16, SWAP⟩| = 48`, `|⟨Gbig, SWAP⟩| = 192`.
- SWAP permutes `Z_F` by `s ↦ (s1s2, s2)`, and every element of both groups maps `Z_F` onto `Z_F`. Every element
  is a unitary or antiunitary conjugation, so it preserves Q3. Hence `K(Z_F)` is invariant: H1–H3 and S1 hold.
- **Exact symmetry group of K(Z_F)** [W over X].
  - A map in 𝒜 preserving K(Z_F) permutes its non-PSD extreme rays, and these are exactly the four defects (a
    decomposition `e_s = q + Σλ_t e_t` with `q ∈ Q3 ∩ Z_F*` forces `λ_s = 1`, `q = 0`, `λ_t = 0`).
  - So `Stab_𝒜(K(Z_F)) = {Ad(U)(∘T) : U monomial in {ψ_s}} = T³_F ⋊ ⟨G16, SWAP⟩`.
  - Its identity component T³_F is 3-dimensional. A generic element has operator Schmidt rank 4, and T³_F meets
    the local unitaries only in Paulis.
  - The action of `⟨G16, SWAP⟩` on the four defects has image S4 and kernel {id, T}. So `⟨G16, SWAP⟩` meets T³_F
    trivially and represents every component exactly once.
- Countercontrols rejected: SWAP moves `K(E0)` (`ipW(P_v, E0) = 3/13 ≥ 0`, `ipW(P_v, SWAP E0) = −5/13`) and
  `K({F, cnot F})` (`ipW(T_(1,−1), SWAP cnot F) = −1/2`). A control partial transpose fails the Aut(Q3) test.
  `Ad(H⊗I)` does not permute `Z_F`.

### 1.3 S2 (the commuting torus with G16) — EXOTIC(existence); the explicit cone attempted and refuted (z2a–z2e)
- **Group** [W over X z2c].
  - Take B = (|0+⟩, |1−⟩, |0−⟩, |1+⟩), the |a⟩_Z|b⟩_X product basis. In B, CNOT = diag(1,−1,1,1)
    (= I⊗P₊ + Z⊗P₋, the amendment's erratum, checked), and `Rz(θ)⊗Rx(φ)` is diagonal and commutes with it.
  - G16's unitary part (8 mod phase) meets T²_c only in {I, Z⊗I}.
  - Hence Ĝ_S2 = T²_c·G16: identity component T²_c (dim 2), component group G16/⟨Ad(Z⊗I)⟩ (order 8).
  - The larger torus T³ of all B-diagonal unitaries contains cnot and e^{iχZ⊗X}.
- **Bell-type seeds = exactly C1 ∪ C2** [W over X A6].
  - Let `A = c00c11` and `B = c01c10` in the product basis, so det = A − B. The torus fixes A and B; CNOT sends
    (A, B) to (−A, B); Z⊗I, I⊗Z and T send it to (−A, −B), (B, A) and (Ā, B̄).
  - An orbit of maximally entangled states needs `|A − B| = |A + B| = 1/2`. The parallelogram identity then gives
    `|A|² + |B|² = 1/4`, AM–GM gives `|A| + |B| ≤ 1/2`, so `AB = 0`, and equality in AM–GM puts ψ on C1 or C2.
  - Z_F's four ψ_s are the points γ ∈ {0, π} of C1 and C2.
- **EBF seed, exact.**
  - Every generator maps C1 ∪ C2 into itself (symbolic γ), and every point and its CNOT image is maximally
    entangled (`|det|² = 1/4`). So `|⟨φ|g p⟩|² ≤ 1/2` holds on all of R(Ĝ_S2): the overlap bound is proved, not
    sampled.
  - EBF ⇒ an exotic Ĝ_S2-invariant self-dual K. The circles are T³-invariant, so this holds also for ⟨T³, G16⟩.
- **Residual for an explicit cone** [W].
  - Torus-fixed tables span {E00, E30, E01, E31}, which are diagonal in the product basis. So a torus-fixed
    non-PSD table pairs negatively with a product, and every exotic invariant K contains a continuous family of
    non-PSD elements.
  - With Bell-type defects the only invariant family is C1 ∪ C2, giving the candidate
    `K_T = (Q3 ∩ D*) + cone D`. In B its defect cones are the Lorentz cones
    `L1 = {−uE12 − ūE21 + Λ(E33+E44) : |u| ≤ Λ}` and L2 (z2e S1); `L1* = {2|y12| ≤ y33 + y44}`.
- **K_T is not self-dual** [X z2e S2–S5; matrices in B].
  - `y = [[1,1,c1,0],[1,1,c2,0],[c̄1,c̄2,1,0],[0,0,0,1]]`, with `c1 = (1+2i)/5` and `c2 = (2−i)/5`.
  - y ∈ K_T*: `y = q0 + ℓ1(u0, 7/17)`, with `q0` PSD (characteristic-polynomial signs) and
    `|u0|² = 1613/10000 ≤ 49/289`; `2|y12| = y33 + y44`; and `y34 = 0`.
  - The dual witness: `w = vv* + ℓ1(ζ, 17)`, with `v = (1, −(4+3i)/5, 157i/125, 0)` and
    `ζ = 530899/31250 + 3i/5`. Here `|ζ| ≤ 17`, `2|w12| = w33 + w44`, `w34 = 0`, so w ∈ K_T*.
  - `tr(yw) = −6/625`; in table form `ipW = −24/625`. So `K_T*` is not self-positive: K_T (and the one-circle
    surgery K′) is not self-dual.
  - Independent route: y ∉ K′ because the constraints force x = q12 ∈ [0,1] and Λ = 1 − x, and then
    `x·det S(x) = −(x³ − x + 2/5) < 0`.
- **Pair obstruction** [X z2e P1–P2]. For two Bell-type defects at squared overlap c, `y = P_l + d_j/(4c)` and
  `w = P_j + d_l/(4c)` lie in `K*` and give `tr(yw) = c − 1/(4c)`, symbolically. At c = 9/25 this is −301/900.
  Controls: the orthogonal pair (SD2) is excluded from the construction; `c = 16/25` gives `+399/1600`.
- **Guidance** [N] (z2a, z2b, z2d): numerical margins for the circle and for the square and triangle subsets are
  negative (controls green). The 34-parameter dual-witness search missed the narrow exact witness above, which
  was derived by hand from the reduced dual problem (NOTES N6).
- **Verdict.** S2 is EXOTIC(existence). The explicit cone is UNRESOLVED. Open: non-surgery constructions, or
  surgeries with non-Bell seeds `αE00 − T_ψ/4`, α > 1/2 (finite pairs of those fail too: NOTES N5 / [W]).

### 1.4 S3 (`actC Rx(θ)` with G16) — EXOTIC(existence), no Bell-type defect; the axis dependence (z3, z5)
- **Group** [X z3 G1–G4].
  - `CNOT(X⊗I)CNOT = X⊗X`, and the two commute; G16 normalizes the torus. So the identity component is
    `T²_x = exp span{−iX⊗I/2, −iX⊗X/2}` (it contains Ad(X⊗I) and Ad(I⊗X)), and the component group is G16
    (order 16), because G16 ∩ T²_x = {id}.
  - In V = H⊗H, CNOT permutes |+−⟩ ↔ |−−⟩. This follows from the amendment's CNOT = I⊗P₊ + Z⊗P₋; the sketch's
    I⊗P₊ + X⊗P₋ is not CNOT (checked).
- **Reachable set** [W over X R1–R3].
  - R = T²_x·SEP ∪ T²_x·CNOT·SEP. In V-coefficients, products have `A = B` (A = c++c−−, B = c+−c−+) and CNOT
    products have `A′ = B′` (A′ = c++c+−, B′ = c−+c−−). The torus multiplies all four by phases.
  - So `R ⊆ {|A| = |B|} ∪ {|A′| = |B′|}`, which has dimension ≤ 5.
  - The overlap is given exactly by `f = max_k (1 + √(1 − 4(|A_k| − |B_k|)²))/2` (Schmidt + the torus phase).
- **Seed.** ψ = (15, −1, 7, 7)/18 has V-coefficients (7/9, 4/9, 0, 4/9), so `|A| = |A′| = 28/81` and
  `B = B′ = 0`. Then `f(ψ) = 1/2 + 5√137/162 ≤ 7/8`, and `e = (7/8)E00 − T_ψ/4` with `ρ(e)ψ = −ψ/32`. The
  checked instances give ⟨e, T_φ⟩ = 13/72, 293/648, 83/648 ≥ 0.
- **No Bell-type defect** [W + X R5]. AM–GM leaves only (|++⟩ + e^{iγ}|−−⟩)/√2 and (|+−⟩ + e^{iγ}|−+⟩)/√2, and
  CNOT maps both to products. Criterion 2 is silent; claim D decides the node.
- **Target-z variant** [X z5 T1–T2]. T²_z = exp span{I⊗Z, Z⊗Z}, with G16 ∩ T²_z = {I, Ad(ZI), Ad(IZ), Ad(ZZ)}.
  The same invariant structure holds in the computational basis. ψ = (7,4,0,4)/9 is unreachable, with
  f ≈ 0.959 ≤ 24/25.
- **Axis dependence** [X z5 L1–L3 + W].
  - Lie algebras generated with cnot: control x → 2, control z → 1, control (3,0,4)/5 → 4 ⊇ su(2)⊗P₋;
    target x → 1, target z → 2, target (3,4,0)/5 → 4 ⊇ |1⟩⟨1|⊗su(2).
  - With su(2)⊗P₋, every `ψ = ψ₊⊗|+⟩ + ψ₋⊗|−⟩` is `(I⊗P₊ + V⊗P₋)(a⊗b)` for a = ψ₊/|ψ₊| and suitable b, V. For
    instance `exp(i(π/4)Y⊗P₋)` reaches the S3-unreachable ψ_a.
  - So the generic-axis node is UNIQUE by criterion 1. Q3 satisfies it (retention). This uses the standard fact
    that one-parameter subgroups generate the analytic subgroup of their Lie algebra, and that a closed K is
    invariant under the closure. The equivalent-by-conjugation statement for `actC Ry(θ)` (via Ad(S⊗I), which
    commutes with cnot and normalizes G16) is [W].

### 1.5 Finite extensions (z4; NOTES N10)
- Orders: |G_H| = 128, |G_S| = 32, |G_Cl| = 23040, |Stab_Cl(Z_F)| = 1536 ⊇ ⟨G16, SWAP⟩, ⟨Gbig, SWAP⟩.
- **The conjecture is refuted** [W over X F3]. A maximally entangled ψ has table `E00 + Σ C_ij E_ij` with C
  orthogonal ([W]: `ψ = (I⊗U)Φ⁺`). The token marginals of `cnot T` and `cnot·Ad(I⊗H) T` contain C11, C21, C31.
  Keeping the orbit maximally entangled would kill the first column of C, which is impossible.
- **Seeds** [X F5]: G_H: ψa, m = 4160/6561, α = 9/10. G_Cl: ψa, m = 6272/6561, α = 99/100. Controls: a product
  has m = 1 in every group; α = 1/2 is inadmissible for G_H.
- **G_S** (a quarter turn of the S2 torus): ψ_F is a Bell seed (m = 0). Its orbit is 8 defects with off-diagonal
  ipW ∈ {0, 1/8}, so it is not orthogonal: EXOTIC(existence), explicit cone open. The orbit is the square subset
  of the circles; z2a's [N] margins for the square are negative, i.e. the plain surgery is expected to fail (not
  certified).
- **K(Z_F)** is explicit for every subgroup of Stab_Cl(Z_F) [X F6, z1].

### 1.6 Structural nodes (H, T, F, V, C) and S4, S5
Not decided by Z: thread Y decides them, or the lattice records them. Remarks only:
- Every explicit countermodel here is a surgery cone, non-homogeneous by stage 3's [W + L] row.
- Within 𝒜, `Stab(K(Z_F))` maps pure states to pure states and defects to defects, so it is not transitive on
  normalized extreme rays (relevant to T, scoped to 𝒜).
- V: stage 3's K({F, cnot F}) stands.
- S4 and S5 contain S3-g, so they are UNIQUE if Y's checks hold; Z has no countermodel there.

## 2. Ledger — certified versus added

| item | class | anchor / evidence | used in |
|---|---|---|---|
| `W 3`, `hom`, `prodState`, `pairVal`, `maxCone`, `actT`, `actC`, `NativeGate` | [K] | CompositeDimension.lean:97, 100, 161, 164, 186, 198, 201, 218–225 | all |
| `sgn`, `pc`, `pt`, `cnotFun`, `cnot` (= Ad(CNOT), control first) | [K] + [X] | CompositeDimension.lean:741–788; z1 A1 | all |
| `phiW` | [K] | CompositeDimension.lean:1220 | z1 CC3 |
| PSD self-duality (Q3 = dualW Q3) | [K] | JordanClassification.lean:84; OperationalRigidity.lean:917 | criterion 1, claim D, surgeries |
| G16 = ⟨cnot, Ad(ZI), Ad(IZ), T⟩ (order 16; equal to the even native class) | [X] stage 3 (audited), re-checked | AUDIT-X H2b–d; z1 B1 | all nodes |
| K(Z_F), Theorem S / SD2, the self-duality characterization, EBF | [W] stage 3, audited | AUDIT-X, AUDIT-U | S0, S1, FE; every existence result |
| criterion 1, criterion 2 (re-derived), claim D, the dimension corollary | [W], added | §1.0; NOTES N3 | all nodes |
| stabilizer of K(Z_F) in 𝒜; extreme-ray argument | [W over X], added | §1.2; z1 C4–C5 | S1 statement |
| Bell-seed classification for S2; pair obstruction; circle-surgery certificate | [W over X] / [X], added | z2c A6, z2e | S2 |
| S3 group, invariants, seed; no Bell-type defect | [W over X], added | z3 | S3 |
| conjecture refutation; Clifford-type orders and seeds | [W over X], added | z4 | FE |
| axis classification (Lie closures, reachability) | [X] + [W], added | z5; NOTES N11 | S3-g, S3-z |
| Schmidt decomposition (largest coefficient = (1 + √(1 − 4|det|²))/2 = (1 + |r|)/2) | standard [W] | used in z3, z4, z5 | f, m |
| analytic subgroup generated by one-parameter subgroups; closure invariance | standard Lie theory [W] | NOTES N12 | S3-g |
| orthogonality of the correlation block of a maximally entangled state | standard [W] | §1.5 | conjecture |
| numerical explorations | [N] | z2a, z2b, z2d | guidance only, never in a verdict |

**Flagged premises and where they enter.** Each node's symmetry group is the candidate P under test, so it
enters only as the class restriction of that node. The flagged groups are the torus (S2), the one-parameter
rotations (S3, S3-z, S3-g), SWAP (S1), and the Clifford-type and Hadamard extensions (FE). Countermodels with more
symmetry are still countermodels. In no node does a flagged premise enter a uniqueness proof, except S3-g's
UNIQUE, where the candidate itself (invariance under a generic one-parameter local rotation group) is the named
premise. No forbidden premise is used anywhere: not IE1, IE2, Q3/PSD as a premise, local operations on entangled
states as an assumption, frame covariance, the region tower, or (o) steps. Q3 appears only as model material and
in verification.

## 3. What is not claimed
- **No explicit cone at S2, S3, S3-z, G_S, G_H, G_Cl.** Those are EXOTIC(existence) through EBF, a
  non-constructive theorem [W, audited at stage 3]. Only the seeds are exhibited, exactly.
- **No statement about S4, S5, H, T, F, V, C** beyond §1.6. The minimality of UNIQUE nodes is thread Y's. S3-g is
  reported as a cross-thread note. Z did not check the target-axis analogue of the reachability construction
  beyond the Lie closure (z5 L2) and the [W] argument.
- **S3 is decided for `actC Rx(θ)`** (exact) and `actC Ry(θ)` (by conjugation, [W]), and the target-z variant
  exactly. Other target axes ⊥ x and the general equatorial control axis are [W] by the same invariant pattern,
  not computed.
- **The pair obstruction** is claimed for two Bell-type defects with c ∈ (0, 1/2) (symbolic) and at c = 9/25
  (exact). For c ≥ 1/2 nothing is claimed. The circle obstruction is claimed for the two-circle and one-circle
  surgeries over the full circles. Finite subsets of the circles (square, triangle) are [N] only, except the
  c = 1/4 triangle pair, which is covered by the pair identity.
- **[N] scripts certify nothing.** In particular "the square surgery fails" is guidance.
- **No Lean, no kernel claim.** Bands unchanged: this is consistency-axis work. No label of the certified corpus
  changes.
- **Scope of EXOTIC**: relative to H1–H3 as fixed at stage 3 plus the stated group invariance on the pair carrier
  W 3. It is not a claim about other carriers or about non-symmetry observer-native conditions.

## 4. Evidence log
- Every script was run as `python3 -I -B <script>` from `pt/Z/`, with stdout in `<name>.out` and stderr plus an
  appended `exit N` line in `<name>.err`.
- Every final script was replayed into `<name>.replay.{out,err}`; `cmp` found stdout and stderr byte-identical,
  9/9.
- Decision rules were fixed in each header before the first run. Pre-run edits are recorded in NOTES: z2c (an A5
  label swap and CC1 text), z5 (a garbled header line), z2e (a rewrite of the P1/S1 identity lines before run 1).
- Every successful `.err` is `exit 0` (`28d3b9e8…`).

| script | role | checks | verdict line | runs | sha256 script | sha256 .out (= replay) |
|---|---|---|---|---|---|---|
| `z1_swap.py` | S1, S0 re-check, stabilizer | 11/11, CC 4/4 | `VERDICT S1-EXOTIC …` | 2 | `ac2dbb18e0bb09d36a55ff20fa36307dc4eb1b77599d3ede9483afae3d5472e9` | `4bfa0d85fc4462db21723b502a2a4ae37131656e77d97b5313a6100bb939a284` |
| `z2a_circle_N.py` | [N] circle and finite subsets | controls green | `SUMMARY [N, numerical]` | 1 | `1b1f4f172e891c89b78265de9dd87c0168e18ce4d49d0b4d8ac492725d973b89` | `cb4c4a8f788d8ac3ddda1c9cf1d2589ee6df3aea3a1df4c9e4ca1f1e75497d66` |
| `z2b_sep_N.py` | [N] separating-pair search | control green | `SUMMARY [N, numerical]` | 1 | `0589cd421c824e052d05036dda639cbdf17c49fb47898c5563260cc4702d2efe` | `e00caf4dd2f03ee458ecc2d8db1f3c708fc2066d9892088bfa5e4bbe1723d916` |
| `z2c_s2_struct.py` | S2 group, circles, seeds | 8/8, CC 3/3 | `VERDICT S2-STRUCT-EXACT` | 1 | `84736b6877a87c578f5af647acc749685bac43a7ec052e063259d1aac202c2e8` | `087a458e09d511ca51939c9e4059c3a0ab058376c6218b63461b5817bf4937ba` |
| `z2d_dual_N.py` | [N] dual-witness search | control green | `SUMMARY [N, numerical]` | 1 | `2040984dee5a3ad2c5ab37f99b5f0b927f1bdcf713fc675314f43fdddf0127a3` | `e9cb9e2dba06a5ef11b6ead934d59241d54ae14d5874d2f62550cebc0f898b6a` |
| `z2e_s2_surgery.py` | pair and circle-surgery obstructions | 7/7, CC 4/4 | `VERDICT S2-SURGERY-NOT-SELF-DUAL …` | 2 | `ec0bcc149d5c3c87d96bd95d0978c9cd019571271394625bfeafe6ed9a881189` | `9a4d465d27bb71c22ba14ac0ac3a1da23c3e5350ac5049e4f9669fa3e0975cf5` |
| `z3_s3.py` | S3 group, reachability, seed | 9/9, CC 4/4 | `VERDICT S3-EXOTIC-EXISTENCE …` | 1 | `55f6a1abcbc4237c3dd8912fc87314be1ee5096a48b4911a84033936047c9c2f` | `fe4e2791d8e042ba87e1d6b4379e844e6a9ead5595a7ab2c5223ecaf0de97672` |
| `z4_fe.py` | finite extensions, conjecture | 6/6, CC 4/4 | `VERDICT FE-CONJECTURE-REFUTED …` | 1 | `40c00f0262f69151b0618fcc370c796a931f29bd32b03648ff88eca1d4d07714` | `9b83565234a5acfbd2fa08f23b0e175654eb2674f8546350f7c465ee22c1898f` |
| `z5_axes.py` | axis classification, S3-z | 5/5, CC 3/3 | `VERDICT AXES-CLASSIFIED …` | 1 | `91cdcfafdbd5eac59abafafdca2ad46337063cafd1159e3a5fa855a38b9149d3` | `e583a0f87763b07af36ee4507a8573c07dbb4137ff3545c3e16e980f7276f05a` |

**Kept failed runs.**
- `z1_swap.run1.{py,out,err}`: all checks passed and every countercontrol was rejected; then the SUMMARY line
  crashed on a sum over sympy booleans (exit 1). The flags were coerced with `bool`; run 2's first 19 lines are
  identical to run 1's. Hashes: script `57aa7fa3854fff41684f7f97d4c0539635691ac84febee95560deba5d1564229`, out
  `4840130b4fdcefffd7d4a9abf14a08c04e2d287a7f443c283be0d53181e92fed`, err
  `4418fafe070110d02fe540339550f7f77f45777ff00ac940afea4c56c2a1aa43`.
- `z2e_s2_surgery.run1.{py,out,err}`: no output; killed after 10 CPU-minutes in a symbolic trigonometric
  simplification (exit 143). P1 was re-parametrized rationally. Hashes: script
  `807a41afc53e3ded09ff21e0cb91d0cd5169fa5d9bbe73a86d73797c2b2ca216`, out (empty)
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, err
  `e55d5e90c4a84d29acf2f9741b027790a0be9960826145a08e3c943f05379edf`.

**Records.** `NOTES.md` `8d5e8815a0cc6ae3e02d6e0cb55c816ddfe2e684707ca8241716e1190d85412e` (frozen, 323 lines);
`.start_marker` `a51825c93c3a685be8b24d9215a8896dc0c197d5c9fdf5d45148acdc500b9b73`.

## 5. Integrity
- **Start (14:24:43Z).** `pt/Z/` did not exist. It was created empty and `.start_marker` was written first. Its
  checks: the six `pt/` manifests and `audit/stage3-inputs/ns.manifest.sha256` (from its own directory) exit 0
  with no output. Base HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`, `status --porcelain` empty
  (GIT_OPTIONAL_LOCKS=0), no bytecode under `base/`.
- **Protocol hashes.** The brief names seven files and says "eight". The eighth is `PROTOCOL-NS.md`
  (`4f61891f…`, counted among the stage-3 protocol files by the integration note); it was checked by hash only.
  All eight matched, and every sidecar verified.
- **Amendment.** The coordinator's amendment arrived during the run and is recorded verbatim in NOTES N1. The
  protocol file is unchanged.
- **End (15:56:27Z).** The same manifests are OK; HEAD, status and bytecode (`base/`, `Z/`) are unchanged; the
  eight protocol hashes are unchanged.
- **Sweep.** No file under `pt/` is newer than the start marker outside `Z/`, `Y/`, `audit/` and
  `audit*-replay/`. The top-level listing still holds the 51 start names; later mtimes appear only on `Y/`
  (sibling, excluded), `Z/` and `audit/` (coordinator, excluded). No anomaly; nothing quarantined.
- **Reads.**
  - Read: the governing texts in the prescribed order, the stage-3 record, `base/AGENTS.md` and
    `CompositeDimension.lean` (transcription), and `X/x7_numeric.py` (to see what stage 3's N4 sampled).
  - Not read: `pt/Y/`, `audit/stage3-inputs/OWNER-*`, `audit/reviews/`, `audit/aborted-launches/`.
- **Writes and limits.** Writes went only to `pt/Z/`. No git write, branch, push, PR, CI, GitHub, network, URL
  fetch, publication or sub-agent was used. Git commands were read-only (`rev-parse`, `status`).
