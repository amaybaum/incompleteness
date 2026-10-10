# Thread Y (EXCLUSION), stage 4 — Q-EX, the exclusion side — RESULT (research only)

Governing texts: `PROTOCOL-STAGE4.md` (`d3da2811…`) and the texts it names; the coordinator's amendment received
mid-work (NOTES N2: erratum on CNOT's block form; the owner's provenance requirement). Base L = `9f9f8257…`,
read-only. Evidence levels kept apart: [K] certified at L (file:line), [D] design module, [W] written argument,
[X] exact computation (instance-scoped unless lifted by [W]), [N] numerical (guidance only), [L] unverified literature.
Labels for "K = Q3" follow amendment 2. EXOTIC-X = an exact cone exhibited; EXOTIC-E = existence by EBF with the
seed exhibited exactly (never merged with EXOTIC-X).

## 0. Answer

**The two criteria close into one dichotomy.** For any node whose symmetry group, together with `cnot`, generates
a compact group Ĝ of unitary or antiunitary conjugations: the node is UNIQUE iff Ĝ carries the pure product states
onto every pure state, and EXOTIC-E iff some pure state φ₀ is unreachable. The exotic direction uses the cap defect
`e = (I − cφ₀φ₀†)/8` with `1 < c ≤ min(2, 1/m)`, where m < 1 is φ₀'s largest overlap with the compact reachable set;
`cone(Ĝ·SEP ∪ Ĝ·e)` is subdual and EBF extends it [W + X y1]. The protocol's Bell-type criterion is the case c = 2.
Its "open zone" (unreachable, but no Bell-type defect) is not undecided: every node in it is EXOTIC-E, S3's instance
among them (y4 cc2).

| node | condition P (with G16) | verdict | evidence | strictly weaker nodes: necessity evidence |
|---|---|---|---|---|
| S0 | G16 | EXOTIC-X | stage 3: K(Z_F) | — |
| S1 | + SWAP (group of order 48) | EXOTIC-E | y5: φ₀ = (1,2,3i,−1+i), c = 517/512 | S0: EXOTIC-X |
| S2 | + torus actC Rz ∘ actT Rx | EXOTIC-E | y5 C2 + [W]: reachable set is G16·SEP | S0 |
| S3 | + actC Rx(θ) (the protocol's instance) | EXOTIC-E | y4: exact certificate, c = 4609/4608; Bell-type route provably unavailable | S0 |
| S4-C, S4-T | + actC SO(3), or + actT SO(3) | **UNIQUE** [W + X]; "K = Q3" CONDITIONAL on (b) | y2: group exact, reachability, controls | S0 (X); S3, LPT, G16 + control Clifford (E) for S4-C; actT Rx, G16 + target Clifford (E) for S4-T |
| S5 | + all local rotations (= IE1) | UNIQUE; CONDITIONAL on (b) | contains S4; y3 B-S5 | S4 is UNIQUE: not minimal |
| finite extensions | LPT = local Paulis + T (64), LPT + SWAP (192), G16 + one-token Clifford (1536 / 768), two-qubit Clifford + T (23040) | EXOTIC-E | y5: one φ₀ for all; [W] every finite group | S0 |
| H | homogeneity | **UNIQUE** [W + X + K + L]; CONDITIONAL on H | y6 H1–H4; [K] Jordan classification | T, F: EXCLUDES-ALL UNRESOLVED |
| T | Aut(K) transitive on extreme rays | EXCLUDES-KNOWN [W + X]; EXCLUDES-ALL UNRESOLVED | y6 T1–T4: invariant c = 15 on defects, 9 on products | — |
| F | perfectness | K(E0) fails F [W + X]; EXCLUDES-ALL UNRESOLVED | y6 F1–F2 | — |
| V | K ∩ V+ = Q3 ∩ V+ | not a selector (record) | stage 3: K({F, cnot F}) | — |
| C | four-token OVL4 | not tested (record) | outside the pair cone | — |
| *record* S3[n] | + one-parameter rotation of one token about n | UNIQUE iff n is not a coordinate axis of the native frame; coordinate axes EXOTIC-E | y3 (18 lines), y4 | S0 |
| *record* drive | native drive (flow through the NOT) on one or both tokens | EXOTIC-E | y3 B-drive, y4; target alone: y5 C2 | S0 |
| *record* R1 | one order-3 rotation of one token about (5,1,1), cnot only | **UNIQUE** [W + X] | y7 | cnot alone: EXOTIC-X (K(E0)) |
| *record* J | the corpus's J (cyc3) on one token | EXOTIC-E | y5 (local Clifford), y7 cc | S0 |

**Minimal UNIQUE nodes.** In the fixed lattice: S4-C and S4-T (every strictly weaker fixed node is EXOTIC with
exact evidence), and H (whose minimality is UNRESOLVED, because the weaker structural nodes T and F are only
EXCLUDES-KNOWN). Once nodes are refined (record), S4 is not minimal. One rotation subgroup of one token suffices iff
its axis is off the native frame's coordinate axes, and so does a single order-3 rotation (R1), whose only proper
sub-extension is EXOTIC-X. A "finite extension" must mean a finite group: one extra symmetry of finite order can
generate an infinite group with cnot whose closure forces Q3.

**Observer-native reading and provenance (owner's requirement).** Every UNIQUE symmetry node consumes operation
(b): rotations act on a token while it belongs to an arbitrary entangled pair, preserving the pair cone. (a), "an
isolated token admits all rotations", is a body symmetry at L [K OrbitGeneration.lean:537]. Its operational
availability is unsourced (K∞-Act, K∞-Drive, K∞-Trans OPEN, ROADMAP.md:68, 1014–1022). (a) does not give (b).
- **(b) is INDEPENDENT of the certified pair premises plus self-duality, relative to L.** K(E0) and K(Z_F) satisfy
  H1, H2 (level (ii) for K(Z_F)) and H3. They violate (b) exactly for S4-C, S4-T, S5, the listed S3[n] axes and R1
  (y2 K1–K2, y3, y7). For any other UNIQUE node the violation follows from that node's UNIQUE proof [W].
- **The corpus records the same gap.** The K2 obligation "local actions compatible with it" is OPEN
  (ROADMAP.md:1001–1005). Idle extension of local rotations to the pair cone "is IE1 itself", and IE1 is unsourced
  (KT4-PREM-1 result.md:171–172, 243). Form is forced but existence is the content, so "valid joint statistics"
  restates closure (EQ2-SYNTHESIS.md:161–167, lead). In the Hilbert-carrier setting, control does not give spectator
  extension [K ReferenceExtension.lean:507]. Observational independence is an added OI⁺ principle not implied by the
  OI core [K CompletedOI.lean:506; GR.md:228].
- **Label.** For S4, S5, S3[n] and R1, "K = Q3" is **CONDITIONAL** on (b) for the node's group. Given H1–H3 the
  principle is equivalent to K = Q3. It is not a restatement: SEP and maxCone satisfy it, while K_gen and the
  exotic cones do not. For H, "K = Q3" is CONDITIONAL on pair-level homogeneity ("every faithful pair state is
  reversibly filtered into every other"). H is absent at L for the pair and is likewise independent of the
  certified premises (the stage-3 cones are not homogeneous) [W + L]. The literal pair transfer of the
  single-system transitivity premise fails for Q3 itself [K TransitiveBody.lean:301 + W]. The faithful analogue is T,
  which is UNRESOLVED as an exclusion.
- **The precise additional freedom.** It is (b) for one local rotation of one token placed off the native frame.
  The corpus's own native drive (the flow through the native NOT) lies exactly on the exceptional set, so its idle
  extension does not force Q3. Idle extension of the drive together with its off-axis conjugate J·flow·J⁻¹ (the
  `J_off_axis` datum of `ElementaryDrivability`, KInfFoundations.lean:264) gives S4 and does force it. Whether
  embedded observation demands (b) is not settled at L: no premise at L supplies it, and the exact countermodels show
  that none of the certified pair premises does.

## 1. Node by node

### Y1 — the two criteria re-derived; the dichotomy (NEW, gem type 2)
Setting: K ⊆ W 3 with H1–H3; P = invariance of K under a set G of maps, each Ad(U) or Ad(U)∘T (U unitary, T the
global transpose); Ĝ = closure in O(16) of ⟨G, cnot⟩, compact, fixing E00 (y1 D1).
1. *Ĝ-invariance.* {g : gK = K} is a group, closed because K is closed; it contains cnot (H2, cnot² = id) and G.
2. *Reachability ⇒ UNIQUE.* Every g ∈ Ĝ maps a pure product to a pure state. If every pure state is reached, K
   contains all of them, hence Q3 (spectral decomposition), and K = K* ⊆ Q3* = Q3 [K JordanClassification.lean:84
   through the dictionary, y1 A1–A2]. This is the protocol's first criterion; it uses no self-duality beyond the last
   step.
3. *Unreachable ⇒ EXOTIC-E (new).* The reachable set R = Ĝ·{pure products} is compact. If φ₀ ∉ R then
   m = max_R |⟨φ₀|φ⟩|² < 1. For 1 < c ≤ min(2, 1/m) put e = table((I − cφ₀φ₀†)/8). Pairings with pure products are
   (1 − c|⟨φ₀|g⁻¹(a⊗b)⟩|²)/2 ≥ 0 (B1). Orbit pairings are (4 − 2c + c²|⟨φ₀|gφ₀⟩|²)/16 ≥ 0 (B2, c ≤ 2). Products pair
   ≥ 0 among themselves. So C = cone(Ĝ·SEP ∪ Ĝ·e) is Ĝ-invariant and subdual. It is closed: it is generated by a
   compact set on which ⟨E00, ·⟩ ≥ min(1, (4 − c)/8) > 0. EBF [W, audited AUDIT-X] gives a Ĝ-invariant self-dual
   K ⊇ C with H1–H3 and P, and ⟨e, P_φ₀⟩ = (1 − c)/2 < 0, so K ≠ Q3. The spectrum of 8e is {1 − c, 1, 1, 1} (B3).
4. *Bell-type criterion = the case c = 2.* By B4 (the largest product overlap of ψ is the top root of
   λ² − λ + |det Ψ|²) it holds iff some maximally entangled ψ has an all-maximally-entangled Ĝ-orbit. The window is
   sharp: c = 5/2 breaks orbit self-positivity (C1); c = 1 gives a PSD table (C3).
5. *Consequences [W].* Every finite Ĝ, and every compact Ĝ of dimension ≤ 1, is EXOTIC-E, because the reachable
   set is a finite union of compact sets of dimension ≤ 5 in the 6-dimensional CP³. UNIQUE needs dim Ĝ ≥ 2.
   `y1_criteria.py`: 13/13.

### Y2 — S4, the generated group exactly (UNIQUE [W + X]; "K = Q3" CONDITIONAL on (b))
- *Dictionary.* actC R(U) = Ad(U⊗I) and actT R(U) = Ad(I⊗U), with R(U) ∈ SO(3), symbolically (G1). In the
  target X-blocks, CNOT = I⊗P₊ + Z⊗P₋, and in the control Z-blocks CNOT = P₀⊗I + P₁⊗X (G2a). The sketch's
  I⊗P₊ + X⊗P₋ is not CNOT (G2b), which confirms the coordinator's erratum.
- *The group.* For g = A⊗P₊ + B⊗P₋ put δ(g) = det A/det B; it is scalar-invariant and multiplicative. δ = +1 on
  SU(2)⊗I and δ = −1 on CNOT (G3). The Lie closure of su(2)⊗I and its CNOT conjugate is su(2)⊗P₊ ⊕ su(2)⊗P₋, of
  dimension 6 (L1).
- *The connected part needs no closure argument.* The word (V⁻¹⊗I)CNOT(V⊗I)CNOT = I⊗P₊ + V⁻¹ZVZ⊗P₋ (G4) has
  V⁻¹ZVZ a rotation about an axis in the XY plane, and such rotations generate SU(2). So the connected group
  C = {U⊗P₊ + V⊗P₋ : U, V ∈ SU(2)} lies in the abstract generated group. Hence
  **Ĝ⁽ⁱ⁾(S4-C) = {Ad(A⊗P₊ + B⊗P₋) : A, B ∈ U(2), det A = ±det B} = C ⊔ C·Ad(I⊗Rx(π/2))**.
- *The second component.* CNOT = [I⊗P₊ + (−iZ)⊗P₋]·[I⊗(P₊ + iP₋)], and Ad(I⊗(P₊ + iP₋)) = actT Rx(π/2) on all 16
  tables (G2c–d). This element lies in the δ = −1 component, outside C (G3: no common phase puts both blocks in
  SU(2)).
- *Level (ii) and the target side.* Ad(Z⊗I) ∈ C. Ad(I⊗Z) (block swap) and T add components, and the Lie algebra is
  unchanged (L3), giving 8 components. Target side: the same structure with P₀, P₁ (L2); at level (ii) only T adds a
  component [W].
- *Reachability [W + X].* Write ψ = u⊗|+⟩ + v⊗|−⟩. If u = 0 or v = 0, ψ is a product. Otherwise ψ = g(a⊗b) with
  a = |0⟩, b = |u||+⟩ + |v||−⟩ and g = U⊗P₊ + V⊗P₋ ∈ C, where U|0⟩ = u/|u| and V|0⟩ = v/|v|. Exact for four targets
  and for the target side (R-*).
- *Countercontrols.* actC Rz(π) and actT Rx(π) give ⟨gE0, E0⟩ = −1 (K1). The order-3 rotation about (1,1,1), on
  either token, moves each defect of Z_F out of K(Z_F), certified by a pure state of K(Z_F) that pairs to −1/2 (K2).
  A commuting generator closes at dimension 1 (L4). Retention is immediate, since unitary conjugations preserve Q3
  (Q1). `y2_s4_group.py`: 19/19.

### Y3 — S3 and the axis refinement (S3: EXOTIC-E; record S3[n])
- *Control axis n.* The generators are (n, n) and (n, n′) in su(2)⊗P₊ ⊕ su(2)⊗P₋, with n′ = Rz(π)n. If n ∦ n′,
  then (0, n − n′) and the commutator (0, n × n′) span the XY directions of the second factor. The closure is then
  ℝn ⊕ su(2), of dimension 4, and it contains {(I, V)}, so every pure state is reachable (take a ∝ u and V a ∝ v).
  If n′ = n (n = ±z), the generator commutes with cnot. If n′ = −n (n ⊥ z), the closure is span{(n,0), (0,n)}, a
  two-torus.
- *Target axis n.* The generators are (n, n̂) with n̂ = Rx(π)n; the axis is exceptional iff n = ±x or n ⊥ x.
- *Level (ii).* T sends n to (nₓ, −n_y, n_z) up to sign, and Ad(I⊗Z) acts on the target by Rz(π). The exceptional
  axes are therefore exactly the coordinate axes of the native frame on either token: x (the NOT nflip's axis),
  z (the corner axis z3) and y.
- *Exact check.* `y3_s3_axes.py` gives 22/22, with labels as predicted for nine axes per token at both levels. It
  also covers the drive on both tokens (dimension 3, abelian), S2's torus (dimension 2, abelian) and S5
  (dimension 15, reachable). Every reachable node moves E0 out of K(E0) and a defect out of K(Z_F) at a rational
  angle.
- *Exposed assumption (gem type 3).* The protocol's S3 sketch ("a two-torus semidirect cnot") is exact only on the
  exceptional set. Its instance actC Rx is exceptional; a generic one-parameter rotation of one token is UNIQUE.

### Y4 — exact certificates on the exceptional set (EXOTIC-E; NEW, gem type 1)
- *Families (level (ii)).* actC Rx, the S3 instance (L = X⊗I, N = X⊗X); actC Ry (Y⊗I, Y⊗X); actT Ry (I⊗Y, Z⊗Y);
  actT Rz (I⊗Z, Z⊗Z); the native drive on both tokens (X⊗I and I⊗X; N = X⊗X).
- *Reduction [W].* Ĝ = T·G16 exactly. The products e^{−iαL}·CNOT e^{−iβL} CNOT cover the torus T, G16 normalizes T
  (F2), and G16 = Loc8 ∪ CNOT·Loc8 (F1). |det Ψ| is invariant under local unitaries and complex conjugation, and CNOT
  exchanges L and N. So min_{g∈Ĝ} |det Ψ(gφ₀)|² = min over β and ψ ∈ {φ₀, CNOTφ₀} of |det Ψ(e^{−iβN}ψ)|². Here
  det Ψ(e^{−iβN}ψ) = cos2β·D − (i/2)sin2β·M (F3), a quadratic form (C,S)Q_ψ(C,S)ᵀ on the unit circle.
- *Certificate.* Q_ψ is positive definite for both ψ and all five families, with φ₀ = (1, 2, 3i, −1+i) (W1). The
  seed is c = 1 + x/8 with x = 4·min(det Q/tr Q)/|φ₀|⁴; it lies inside the window because √(1−x) ≤ 1 − x/2, and the
  exact PSD check confirms it. Values: c = 4609/4608 for actC Rx and the drive, 1541/1536 for actC Ry, 5677/5632 for
  actT Ry, 17409/17408 for actT Rz. Cross-checked on 96 group members per family.
- *Controls.* A reachable state gives det Q = 0 (cc1). For actC Rx, the maximally entangled states whose torus orbit
  stays maximally entangled are |∓⟩|+⟩ + w|±⟩|−⟩, and CNOT sends them to products; (1,1,1,−1) has a torus image with
  product overlap > 1/2 (cc2). So the Bell-type route is provably unavailable for S3. φ₀ itself is reachable for an
  oblique control axis (cc3).
- *Runs.* Run 1 failed on my own rule's discretization of c and is kept (NOTES N6); run 2 gives 16/16.
- *Verdict.* The S3 instance, actC Ry, actT Ry, actT Rz and the drive are EXOTIC-E. Level (i) inherits the verdict,
  since its group is smaller.

### Y5 — S1, S2 and the finite extensions (EXOTIC-E)
- *Groups.* BIG is the two-qubit Clifford group with T, of order 23040, enumerated exactly on primitive
  Gaussian-integer representatives. Its named subgroups: S0 16; S1 48; LPT 64 (= X's Gbig); LPT + SWAP 192;
  G16 + control Clifford 1536; G16 + target Clifford 768. Every generator lies in BIG.
- *Certificate.* φ₀ is entangled in all 23040 images, with d_min = 5/256 (already attained in G16), so c = 517/512.
  Subgroups inherit the seed, because their reachable sets are smaller. S2's torus is local and commutes with cnot,
  so S2's reachable set is G16·SEP [W] (C2).
- *Controls.* |00⟩ and the Bell vector reach a product, giving minimum 0.
- *Verdict.* EXOTIC-E for S1, S2 and every listed finite extension; for every finite group the verdict is [W]
  (Y1.5). Explicit cones and the Bell-type finite-extension conjecture are thread Z's. `y5_finite.py`: 12/12.

### Y6 — H written out; T and F decided for the surgery cones
**H, homogeneity (UNIQUE [W + X + K + L]).** Let K satisfy H1–H3, with Aut(K) transitive on int K.
1. [L1, Koecher–Vinberg] A homogeneous cone that is self-dual for some inner product is symmetric, i.e. the cone of
   squares of a Euclidean Jordan algebra.
2. [L2, Jordan–von Neumann–Wigner, with the decomposition into irreducibles] Each irreducible summand is ℝ₊, L_n,
   Sym_n(ℝ)₊, Herm_n(ℂ)₊, Herm_n(ℍ)₊ or Herm₃(𝕆)₊. At dimension 16 the irreducible types are L16 and Herm₄(ℂ)₊ (H1,
   exact given the list; the control dimensions 15 and 27 return several types).
3. Direct sums are excluded [W + X, X's decomposability argument, AUDIT-X].
4. Lorentz type is excluded [W + X]. In a cone linearly isomorphic to a Lorentz cone, the faces are 0, rays and the
   cone, so a sum of two non-proportional extreme rays is interior. But P00 and P01 are non-proportional extreme rays
   of K (pure products are extreme in maxCone ⊇ K), and ⟨P00 + P01, P11⟩ = 0 with 0 ≠ P11 ∈ K = K*, so P00 + P01 ∈ ∂K
   (H2). This replaces S3's LOR.W route and its [L] input Aut(Lorentz).
5. Herm₄(ℂ) type: K = A(Q3), and self-duality gives S = AᵀA ∈ Aut(Q3). The classification Aut(PSD₄) =
   {X ↦ MXM†, MXᵀM†} is [K + W]. It follows from `orderIso_jordan` [K OperationalRigidity.lean:848] and
   `matrixJordan_unitary_or_transpose` [K JordanClassification.lean:825] applied to Ad(P^{−1/2})∘S with P = S(I) ≻ 0
   (complexified) [W]. Then S^{1/2} ∈ Aut(Q3), K = O(Q3) with O orthogonal, and the local Wigner theorem [W + X,
   stage 3] gives K ∈ {Q3, twin}. Twin fails H2: idW ∈ twin, cnot idW = chainW, and a product effect gives −1/2 (H3;
   [K] K2Guard `cnot_idW`, `chain_value`). So K = Q3.
- *Remaining [L] inputs:* L1 and L2 only. The stage-3 inputs Aut(PSD₄) and Aut(Lorentz) are no longer needed.
- *Retention:* Ad(M) carries I to any positive definite MM† (H4).
- *Stage-3 cones:* they are not homogeneous by the theorem itself [W + L]. Independently, symmetric cones are
  perfect [L] and K(E0) is not (F below).

**T (EXCLUDES-KNOWN; EXCLUDES-ALL UNRESOLVED).**
- *The invariant [W].* Put c(x) = dim span{y ∈ K : ⟨x, y⟩ = 0}. For self-dual K and A ∈ Aut(K), Aᵀ ∈ Aut(K) and
  c(Ax) = c(x), so automorphisms preserve c on extreme rays.
- *K(E0).* E0 is an extreme ray [W] with c(E0) = 15: fifteen independent pure states of Q3 ∩ E0^⊥ lie in K(E0) (T1).
  P00 is an extreme ray with ⟨P00, E0⟩ = 1 > 0, so every y = q + λE0 orthogonal to P00 has λ = 0 and
  q ∈ PSD(|00⟩^⊥), and nine K_gen members give c(P00) = 9 (T2).
- *K(Z_F).* c(z₀) = 15 from z₁, z₂, z₃ and boundary pure states of z₀'s cap, and c(P00) = 9 (T3).
- *Retention.* In Q3 every pure state has c = 9 (T4), consistent with unitary transitivity.
- *Residual.* For every K with H1–H3, c(P00) = 9 [W + X]. The lower bound is span(K_gen ∩ P00^⊥) = Herm(|00⟩^⊥).
  For the upper bound, an element of K_E orthogonal to P00 has ρ vanishing on the |00⟩ row and column: first-order
  conditions of maxCone at |00⟩, together with cnot, which fixes |00⟩ and sends |11⟩ to |10⟩. So under T every
  extreme ray has c = 9. Whether an exotic K with H1–H3 meets this, with transitive automorphisms, is open.

**F (K(E0) fails; EXCLUDES-ALL UNRESOLVED).**
- *The face.* The face of K(E0) exposed by E0 is F₀ = Q3 ∩ E0^⊥, and it spans E0^⊥ (T1). Its dual within E0^⊥ is
  the projection of Q3 along E0 [W: (Q3 ∩ H)^{*H} = (Q3 + ℝE0) ∩ H].
- *Witness.* y = P_f3 − E0 lies in E0^⊥ and pairs ≥ 0 with F₀, but has eigenvalues −1/4 (twice) and 1/4 (twice)
  (F1). So F₀ is not self-dual in its span, and K(E0) is not perfect.
- *Control.* Q3's face exposed by P00 is PSD(|00⟩^⊥), and the same construction (compression) stays in it (F2).
  `y6_structural.py`: 10/10.

### Y7 — record node R1: one extra rotation, no one-parameter group (UNIQUE [W + X]; NEW, gem type 3)
- *Written argument.* Let R ∈ SO(3) have finite order k and act on the control, with R′ = Rz(π)RRz(π). In blocks,
  Γ = ⟨cnot, actC R⟩ is generated by (U, U) and (I, Z). Its first projection is ⟨U⟩, which is finite. The kernel Γ₀
  consists of elements (I, W), and its second projection has index ≤ k in ⟨R, Rz(π)⟩ ∋ R′.
- *Closure.* If ⟨R, R′⟩ is infinite and the axes are non-parallel, its closure is SO(3). A positive-dimensional
  closed subgroup has identity component SO(2)_m or SO(3), since so(3) has no 2-dimensional subalgebra. An
  SO(2)_m-type closure lies in O(2)_m, whose elements of order 3 or 4 rotate about m, which is impossible for two
  non-parallel axes. A closed finite-index subgroup of SO(3) is SO(3).
- *Conclusion.* Hence closure(Γ) ⊇ {(I, V)}, every pure state is reachable, and K = Q3. Infinite order is
  certified by W = RR′ with rational cos(angle) ∉ {0, ±1/2, ±1}: if W^j = 1, then 2cos is a rational algebraic
  integer, hence an integer.
- *Exact (run 2: 4/4).* Order 3 about (5,1,1): cos = 127/162 on the control side, −113/162 on the target side.
  Order 4 about (1,2,2): cos = −31/81. Both stage-3 cones leave themselves. Countercontrol: the corpus's J (cyc3)
  generates with Rz(π) a group of order 12, with cos −1/2, so the criterion does not fire. Run 1 failed on my Z_F
  witness family; the [N] probe y7x and a written congruence argument located the fix (NOTES N7–N8).
- *Minimality.* R1 (order 3) is minimal in its cyclic family: its only proper sub-extension, cnot alone, is
  EXOTIC-X (K(E0)). The quarter-turn's square (a half-turn) is not decided.

### O — observer-native reading and provenance of every UNIQUE node (owner's requirement)
(a) = "an isolated token admits the rotations"; (b) = "they act on the token while it belongs to an arbitrary
entangled pair, preserving the pair cone". All anchors are at L unless marked.

| node | what P says about the observer | (a) at L | (b) at L | "K = Q3" (amendment 2) |
|---|---|---|---|---|
| S4-C / S4-T | local agency, full rotation group of one token | body symmetry: `boundaryTransitive_fullAut3` [K OrbitGeneration.lean:537]; availability unsourced: K∞-Act, K∞-Drive, K∞-Trans OPEN (ROADMAP.md:68, 1014–1022) | not derived; INDEPENDENT of H1–H3 (exact: stage-3 cones) | CONDITIONAL on (b)_S4; equivalent given H1–H3; not a restatement |
| S5 | local agency on both tokens = IE1 [D FourCopyCore.lean:156] | as above | not derived; idle extension of local rotations "is IE1 itself" (KT4-PREM-1 result.md:171–172), unsourced (:243) | CONDITIONAL on IE1; stronger than S4 |
| S3[n], n off-frame (record) | local agency for one rotation axis of one token | the native drive, `ElementaryDrivability` [K def KInfFoundations.lean:264], rotates about the NOT axis (nflip, CompositeDimension.lean:797), which is on-frame | not stated anywhere at L | CONDITIONAL on (b) for that axis |
| R1 (record) | local agency for one discrete off-frame rotation | not stated; the corpus's J (`ball3Drive`, :449) is a local Clifford and is insufficient alone | not stated | CONDITIONAL on (b) for R1 |
| H | pair-level homogeneity: every faithful pair state is reversibly *filtered* into every other (cone automorphisms, not normalization-preserving) | single-system analogue K∞-Trans, `BoundaryTransitive` (OrbitGeneration.lean:79), OPEN (ROADMAP.md:1018) | — (not a local operation) | CONDITIONAL on H, an added Origin-type principle; H independent of H1–H3 [W + L] |

**Why (b) does not follow from (a) at L.**
- *Exact.* The stage-3 cones contain every product of isolated-token states (H1). They carry the certified gate (H2,
  and the level-(ii) class for K(Z_F)) and are self-dual. Yet a rotation of one token moves them out of themselves
  (Y2 K1–K2, Y3, Y7).
- *The corpus.* K2 lists "local actions compatible with [the composite cone]" as OPEN (ROADMAP.md:1001–1005). The
  idle extension of single-system operations has a forced form, but its existence is the content: "valid joint
  statistics for every joint measurement" restates closure, and product effects cannot detect a failure
  (EQ2-SYNTHESIS.md:161–167, audited lead). In the Hilbert-carrier setting the kernel proves that full control
  within a carrier does not give the ability to append a spectator [K ReferenceExtension.lean:507]. It also proves
  that observational independence (inert spectators, GR.md:212 (iii), :228) is independent of the OI core
  [K CompletedOI.lean:506]. Stage 2 classed local agency and frame covariance as flagged routes, with
  FC ⟺ IE1 given hgate (PROTOCOL-STAGE2.md:82–86; S2/RESULT.md:343–354, audited).
- *Label.* (b) must be adopted as an added principle. Relative to L as stated it is INDEPENDENT of the certified
  pair premises together with self-duality.

**The literal transfer of TRB-1's premise is not the pair analogue.** The density-matrix body of Q3 has
non-extreme boundary states (rank 2), and no body-preserving family is boundary transitive on such a body
[K TransitiveBody.lean:301 + W]. So the pair analogue of K∞-Trans must be stated on extreme points, which is T
(UNRESOLVED as an exclusion), or recast as cone homogeneity H (UNIQUE, but about filtering rather than reversible
dynamics).

**The precise freedom, and whether embedded observation demands it.**
- *Within the lattice.* What makes Q3 unique is (b) for one local rotation of one token off the native frame
  (S3[n], R1), or the full rotation group (S4), or structurally H.
- *The native frame.* The axes of nflip (x) and z3 (z) are exactly the exceptional axes. So the drive that the
  corpus attaches to the NOT is the one drive whose idle extension does not suffice (Y4: EXOTIC-E on one or both
  tokens). Idle extension of the drive together with its off-axis conjugate J·flow·J⁻¹ (J_off_axis) contains actC
  SO(3) and suffices [W].
- *At L.* Whether embedded observation demands (b) is UNRESOLVED. Nothing at L supplies it, and the exact
  countermodels show that the certified pair premises with self-duality do not.

**Minimal UNIQUE nodes, with necessity.**
- *Fixed lattice.* S4-C has as strictly weaker nodes S0 (EXOTIC-X, stage 3), S3 (EXOTIC-E, Y4), LPT and G16 +
  control Clifford (EXOTIC-E, Y5). S4-T has S0 and G16 + target Clifford (EXOTIC-E), plus actT Rx (record, EXOTIC-E,
  Y5 C2). Both are minimal.
- *H.* H is UNIQUE, but whether it is minimal is UNRESOLVED. Given H1–H3, H implies T and F [L: symmetric cones are
  perfect, and irreducible ones have extreme-ray-transitive automorphism groups], and T and F are EXCLUDES-KNOWN only.
- *Refined lattice (record).* S4 is not minimal. R1 is minimal in its cyclic family.

### Hard-to-vary review
- *Controls and retention.* Every decisive check has a countercontrol that fails as required. Q3 passes every
  retention test (Y2 Q1, Y3 Q1, H4, T4, F2). The stage-3 cones fail every exclusion claimed for the computed nodes.
- *Predictions beyond the problem.* Each was written in NOTES before the run that checked it: the full axis
  classification (Y3 labels as predicted); EXOTIC-E for the native drive on both tokens (Y4); UNIQUE for a single
  off-frame order-3 rotation (Y7, after a pressure test).
- *Not adjustable.* The cap window is sharp (y1 C1, C3). The certificates fail on reachable states (y4 cc1, y5 cc)
  and on the oblique group (y4 cc3).
- *Skepticism at favourable steps.* R1's failed run was investigated by a probe and a written argument before the
  witness rule changed. S4's group was derived exactly per the erratum, and the provenance of every UNIQUE node was
  tested against the exotic cones.

## 2. Ledger — certified versus added
| item | class | anchor | used in |
|---|---|---|---|
| `W 3`, `hom`, `prodState`, `pairVal`, `maxCone`, `actT`, `actC` | [K] | CompositeDimension.lean:97, 100, 161, 164, 186, 198, 201 | all |
| `sgn`, `pc`, `pt`, `cnot` (transcribed; = Ad(CNOT), y1 A2) | [K] | CompositeDimension.lean:741–786 | all |
| `z3`, `nflip`, `IsNot`, `NativeGate` | [K] | CompositeDimension.lean:793, 797, 210, 218–225 | the native frame (Y3, O) |
| `reflY`, `idW`, `chainW`, `cnot_idW`, `chain_value`; `phiW` | [K] | K2Guard.lean:46, 101, 104, 110, 134; CompositeDimension.lean:1220 | twin fails H2 (H step 5) |
| PSD self-duality | [K] | JordanClassification.lean:84 | Y1.2, H |
| `orderIso_jordan`; `matrixJordan_unitary_or_transpose` | [K] | OperationalRigidity.lean:848; JordanClassification.lean:825 | H step 5 (replaces [L] Aut(PSD₄)) |
| `BoundaryTransitive`, `boundaryTransitive_fullAut3`; `not_boundaryTransitive_of_nonextreme_boundary` | [K] | OrbitGeneration.lean:79, 537; TransitiveBody.lean:301 | O |
| `ElementaryDrivability`, `ball3Drive` | [K] | KInfFoundations.lean:264, 449 | O |
| `control_not_implies_parallelReferenceExtension`; `oiPlus_independence` | [K] | ReferenceExtension.lean:507; CompletedOI.lean:506 | O |
| status of K2, K∞; IE1 unsourced | [A] record | ROADMAP.md:68, 1001–1005, 1014–1022; KT4-PREM-1 result.md:171–172, 191–192, 243 | O |
| `ipW`, `dualW`, `transposeW`; `pauliW`, `Q3`, `twin`; `IE1` | [D] | FourCopyDefs.lean:31, 34, 49; FourCopyPackage.lean:176, 180, 183; FourCopyCore.lean:156 | all; S5 |
| EBF, SD1/SD2, Theorem S, local Wigner, decomposability; the cones K(E0), K(Z_F) | [W + X], audited | AUDIT-X, AUDIT-U | Y1.3, H, all controls |
| dichotomy; S4 group; axis classification; reduction and certificates; finite enumeration; Lorentz exclusion by three products; the invariant c; non-perfectness; R1 | [W] + [X], added here | §1, scripts y1–y7 | all verdicts |
| Koecher–Vinberg; Jordan–von Neumann–Wigner (list, decomposition); symmetric cones perfect (confirmation only) | [L, unverified] | — | H |
| closed-subgroup and Lie-product facts; closed subgroups of SO(3); dimension count | standard [W] | — | Y1, Y2, Y7 |
| numerics | [N] | `y7x_probe` only | guidance; no verdict |

**Flagged premises, and where they enter (as candidates P only).** Local-on-entangled operations: S3[n], S4, S5,
R1, the drive. The torus: S2. Transposes, Cliffords and SWAP: the finite nodes. None enters any proof except as the
named P of the node under test. Q3 and PSD appear only as comparison objects, in verification, and as model
material of EBF seeds. No forbidden premise (IE1, IE2, frame covariance, the region tower, (o) steps) is used as a
premise; IE1 appears only as the node S5 under test.

## 3. What is not claimed
- **EXOTIC-E is existence only** (EBF, non-constructive). No explicit cone is given for S1, S2, S3, the finite
  extensions or the drive; those are thread Z's targets. The exact seeds are shallow (c close to 1).
- **The UNIQUE verdicts are uniqueness given the named P.** "K = Q3" is CONDITIONAL on (b) or on H, never DERIVED.
  Nothing here derives (b) or H.
- **T and F are decided only for the stated cones.** T is decided for K(E0) and K(Z_F), F for K(E0).
  K({F, cnot F}) and K(e_c) were not computed.
- **H rests on [L]** Koecher–Vinberg and Jordan–von Neumann–Wigner; no Mathlib anchor was located.
- **Scope of the exact checks.** The axis classification is exact for nine axes per token and general by [W]. R1 is
  exact for the listed rotations and general by [W]. The quarter-turn's square is not decided. R1 is not claimed to
  be the only minimal form.
- **Standard Lie facts** are used as [W]; nothing is kernel-checked here. No Lean was written. Bands are unchanged
  (consistency-axis work).
- **INDEPENDENT** is relative to the premises certified at L as stated, not to every observer-native extension of
  the framework.

## 4. Evidence log
Every script ran as `python3 -I -B <script>` from `pt/Y/`, with stdout in `<name>.out` and stderr plus an appended
`exit N` line in `<name>.err`. Every final script was replayed into `<name>.replay.{out,err}`; `cmp` found all eight
byte-identical on stdout and stderr. Decision rules were fixed in each header before its first run. Pre-run edits and
the two rule changes after failed runs are recorded in NOTES (N4, N6, N7, N8). Every `.err` is the single line
`exit 0` (`28d3b9e8…`), failed runs included: those failed on their own decision rules, not by crashing.

| script | node | checks | verdict line | runs | replay |
|---|---|---|---|---|---|
| `y1_criteria.py` | Y1 | 13/13 | `VERDICT Y1-CRITERIA-EXACT` | 1 | identical |
| `y2_s4_group.py` | Y2 (S4, S5) | 19/19 | `VERDICT Y2-S4-EXACT` | 1 (pre-run edits) | identical |
| `y3_s3_axes.py` | Y3 (S3, S3[n], combinations) | 22/22 | `VERDICT Y3-AXES-EXACT` | 1 | identical |
| `y4_s3_cert.py` | Y4 (exceptional set) | 16/16 | `VERDICT Y4-CERT-EXACT` | 2 (run 1: 13/16, kept) | identical (run 2) |
| `y5_finite.py` | Y5 (S1, S2, finite) | 12/12 | `VERDICT Y5-FINITE-EXACT` | 1 | identical |
| `y6_structural.py` | Y6 (H, T, F) | 10/10 | `VERDICT Y6-STRUCTURAL-EXACT` | 1 (pre-run edits) | identical |
| `y7_single.py` | Y7 (R1) | 4/4 | `VERDICT Y7-SINGLE-EXACT` | 2 (run 1: 2/4, kept) | identical (run 2) |
| `y7x_probe.py` | [N] guidance for Y7 | none by rule | none | 1 | identical |

**Failed runs, kept.** `y4_s3_cert.run1.*` gave 13/16: its fixed list of cap parameters ended at 513/512, too coarse
for three families that W1 had already certified. The rule was changed to c = 1 + x/8 and the header updated; every
other line of runs 1 and 2 is identical. `y7_single.run1.*` gave 2/4: its K(Z_F) witness family held only the image
cap centre. The [N] probe and a written congruence argument located the fix, a slide toward the cap boundary. The
header was updated before run 2, and lines S-C4 and cc-cyc3 are identical in both runs.

sha256 (every `.err` is `28d3b9e880a77975493dc7e359144c0295a4f694cfe0af4f928c22307bc5c320`; every replay file
carries the hash of its original):
```
fa455b7e2cb38b752047fc040ac764e70851dfdbfc27a2d486a0cccfb16d310a  .start_marker
ae1e54c48e92908f1e66ff0866af62aff8076a6bd2c62a694f8270ba53157f5b  NOTES.md
8d9c81695c32dd266598fb221b2918d3313a2cb4617496a4d5944bf5a77f1d3a  y1_criteria.py
6e7c5de675e3d3bc2b2cf9f3737805a1f5f204794599383f22e6a9fb3fa36f1f  y2_s4_group.py
452d3991f303bb3cb6e1302c54c3bf530a6f1b3f31116326c88b2168bd14c4b5  y3_s3_axes.py
fdea0ea1b6bc4609c098ac2b42b1c256588a04d43c983bf083367832e6976aef  y4_s3_cert.py
5f31fb0e04c2d783a9ddae0526434af6675ac10ca8e9eebf6ea1d039292e8da9  y4_s3_cert.run1.py
32d68344f65681f6bf37d5ed7fcff0048ce8eda52ed87c47e4f5f7854b64f61e  y5_finite.py
acd9cb461c977720233065a410d274b354d90d85f11931884103b176c642df3d  y6_structural.py
b4836718b79954cb46cbb0cbb8ca9e6710701f2a92e9310ef26615568f0e676f  y7_single.py
a114c00ed5efa10cb2e9b51c9c5214b4305045956cd14ee1716d7cacc01a0dd6  y7_single.run1.py
a25c9933f527ddb3b354ef39395c8a4f073c9a595a12413b5db70340363a4318  y7x_probe.py
07c3372e82272f91b596add340206acb05159b11f9b06d51f12091630718f371  y1_criteria.out
671855143c205adadd82daa52ac15d7106753af89f945a42f5e4a32cbbad5c5c  y2_s4_group.out
a1c306c89bdd07242aee327433bdbc8830052daf86f952fca6b42e59baa0e419  y3_s3_axes.out
1f2c7c716cb9dd64a96d5eb1791b24c164672f753150fc7e443a26597d52b450  y4_s3_cert.out
40eb65a06a8041eec5e9aeeeb6188a7b50b88288647ff55bb5d28578ab0eb39b  y4_s3_cert.run1.out
aa7892a2f88a0f9ed8d17c9812a8785043313d88cb30d6bad7f59f4af1ff549c  y5_finite.out
e2b55447dd3e957f997be2561a4d2a343ba46bc4bd4a9571cc973cab986c8283  y6_structural.out
28b4f242eb4c404bd84628fc871596c5a31cceb836a72a5de61d88bc542f1494  y7_single.out
59ee79cad60e46a6407ed19b11bf877f528afd476065063a148ebd428930d22c  y7_single.run1.out
6d0ff2cfb66ea74c3532a04585e04ba51f1682c3e96f7a68c9e96e5b4e6b2a25  y7x_probe.out
```

## 5. Integrity
- **Start (14:24:15Z).** `pt/Y/` did not exist. It was created, and `.start_marker` was written first (sha256
  `fa455b7e…`).
  - The six manifests (`inputs`, `stage1`, `inputs2`, `inputs3`, `stage2`, `inputs4`) and
    `audit/stage3-inputs/ns.manifest.sha256`, checked from its own directory, all gave rc = 0.
  - `git -C pt/base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `status --porcelain` was empty
    (GIT_OPTIONAL_LOCKS=0); no bytecode under `pt/base/`.
  - The seven protocol hashes named in the launch message matched (the message said "eight" and listed seven), and
    so did their sidecars. The STAGE4 sidecar names `pt/PROTOCOL-STAGE4.md` and verifies from the scratchpad
    directory.
- **End (15:22:16Z).** The same checks were all green: the manifests gave rc = 0, HEAD unchanged, status empty, the
  protocol hashes and sidecars unchanged, and no bytecode under `pt/base/` or `pt/Y/`.
- **Sweep.** Files under `pt/` newer than the marker, excluding `Y/`, `Z/`, `audit/` and `audit*-replay/`: only
  `pt/` itself, with mtime 14:24:43Z. The top-level names are the start listing plus `Z/`, the sibling thread created
  after my marker (names and mtimes only; nothing inside `pt/Z/` was read). Accounted for; no anomaly; nothing
  quarantined.
- **Reads.** The governing texts; the stage-1, 2 and 3 records; the design modules; `pt/base/` (read-only:
  `rev-parse`, `status`, file reads). The stage-3 records used were re-hashed and match the integration note.
- **Not read.** `pt/Z/`; `pt/audit/stage3-inputs/OWNER-*` (`ns.manifest.sha256` only checked with `sha256sum -c`, as
  instructed); `pt/audit/reviews/`; `pt/audit/aborted-launches/`.
- **Writes.** Only inside `pt/Y/`.
- **Disclosures.** The tool runner kept a background-task log of the replay loop outside `pt/` (holding only the
  eight REPLAY lines); no command of mine redirected output there. One early version check ran `python3 -c` without
  `-B`; a search found no bytecode newer than the marker in the Python tree. The clock times in NOTES headings N3–N10
  were estimates and are corrected in N11.
- **Limits observed.** No git write, branch, PR, CI, GitHub call, network or URL fetch, publication or sub-agent. The
  sha256 of this file is given in the final report, since a file cannot carry its own hash.
