# BIDUAL-REL: the relative commutant of the diagonal in the bidual of B(ℓ²) (research record)

**WIP / UNVERIFIED. Paper-only research. It awaits an independent non-author review.** This
record walks the nodes of `PLAN.md`, which was committed before it at `c8c455bc`. It runs no
computation. It edits no manuscript, Lean module, reviewed record or Issue. It adopts no premise,
changes no status and strengthens no manuscript or kernel theorem. No merge is authorized. Names
prefixed "M2" are NONDIO-M2's at `7102e6af`; names without a prefix are this record's.

**Labels.**
- **ESTABLISHED**: proved on paper here (layer X), or cited at its source's standing: (L) a
  literature theorem. "Established" means established within this record, not in the §A.46
  sense.
- **ASSUMED**: a named premise.
- **MISSING**: a gap, stated with the node where the branch stopped.

**Notation.** H_V = ℓ²(C_V) with C_V = ℕ, A := B(H_V), D := ℓ^∞(C_V) ⊆ A, and Δ: A → D the
diagonal conditional expectation. H_Z = ℓ²(Z) with Z = ℕ, and B := B(H_V ⊗ H_Z). A\*\* is the
bidual with its von Neumann algebra structure, A ⊆ A\*\* canonically, and D\*\* is the σ-weak
closure of D in A\*\*. For φ ∈ A\*, φ\*\* is its normal extension to A\*\*. σ_ω is the vector slice
of M2 Lemma VS, and σ′_ρ is the vector slice over the first factor (M2 §5).

## 0. Outcome

**BIDUAL-REL: REFUTED** (B1). With C_V countably infinite, D′ ∩ A\*\* ≠ D\*\*: ℓ^∞(C_V)\*\* is not
maximal abelian in B(ℓ²(C_V))\*\*. The witness is a projection s ∈ D′ ∩ A\*\* with s ∉ D\*\*
(Theorem REL). It is constructed from a free ultrafilter, and its proof uses the
Marcus–Spielman–Srivastava solution of the Kadison–Singer problem, for one purpose only: to show
that a certain ultrafilter limit of vector states is pure. The witness lies in the singular part
of A\*\*, as M2 Lemma JU requires.

**Consequence for (F-S): a non-DIO affine assignment exists** (B2). There is an affine assignment
ρ ↦ Ω_ρ, defined on all states of A, satisfying PROD with a diagonal non-normal hidden state ω,
and a single-outcome σ-D instrument satisfying TB (a configuration bijection of the total
carrier), under which two visible inputs with the same configuration law give output
configuration laws 0 and 1 (Theorem NDIO). The assignment uses one slice order on the sector of a
pure singular state f and the other slice order elsewhere. So (F-S) is not DIO-type on the full
class of affine assignments with PROD that M2 Proposition BID addresses. In that class the answer
depends on the assignment.

**What remains DIO-type in (F-S)** (ESTABLISHED):
- every affine assignment with PROD, on normal visible inputs (M2 Lemma JU);
- every affine assignment with PROD when the hidden state ω is normal, on all visible inputs
  (Proposition HN, new here);
- each of the two slice orders, on all inputs (M2 §5).

So a non-DIO assignment needs a non-normal ω and a non-normal visible input. Theorem NDIO has
both. For a fixed assignment, Proposition BID's condition is also necessary (Proposition BID′).

**Mathematical existence and physical realizability.**
- The construction uses free ultrafilters and a theorem proved in ZFC (MSS).
- The hidden state ω of Theorem NDIO is diagonal, so it is admitted under LAW-fa and excluded
  under LAW-σ.
- Of the two inputs, ψ = f∘Δ is diagonal and non-normal (admitted under LAW-fa). f is coherent and
  non-normal, so it is outside LAW in both readings.
- Under LAW-fa, two native (diagonal) visible inputs with the same configuration law are equal
  (M2 §6), so no native pair of inputs witnesses the failure. Under LAW-σ no native input is
  non-normal, and the failure does not arise.
- The non-DIO assignment is a mathematical object. NAT does not deliver it, and it is not adopted.

**Productivity (`PLAN.md` §4): gem.** BIDUAL-REL and the (F-S) question for affine PROD
assignments are both decided. The output class is NEW, with assumption-watch marker AW-4 (§6).

## 1. B0: literature

| Topic | Source | Use |
|---|---|---|
| Kadison–Singer problem | R. V. Kadison, I. M. Singer, "Extensions of pure states", Amer. J. Math. 81 (1959), 383–400 | formulation only |
| Its solution | A. W. Marcus, D. A. Spielman, N. Srivastava, "Interlacing families II: Mixed characteristic polynomials and the Kadison–Singer problem", Ann. of Math. 182 (2015), 327–350 | **used (L)**, in Lemma PUR, in the form: every pure state of the diagonal MASA ℓ^∞(ℕ) ⊆ B(ℓ²(ℕ)) has exactly one extension to a state of B(ℓ²(ℕ)). The form is unitarily invariant, so it holds for the diagonal MASA of any orthonormal basis of a separable infinite-dimensional Hilbert space |
| Extension property of MASAs | R. J. Archbold, J. W. Bunce, K. D. Gregson, "Extensions of states of C\*-algebras, II", Proc. Roy. Soc. Edinburgh Sect. A 92 (1982), 113–122; J. Anderson, "Extensions, restrictions, and representations of states on C\*-algebras", Trans. Amer. Math. Soc. 249 (1979), 303–329 | context. Only the abstract of the first was read: an abelian subalgebra with the extension property is a MASA. Neither paper is used in a proof |
| Excision | C. A. Akemann, J. Anderson, G. K. Pedersen, "Excising states of C\*-algebras", Canad. J. Math. 38 (1986), 1239–1260 | context. Not read in full and not used |
| Bidual as enveloping von Neumann algebra | M. Takesaki, *Theory of Operator Algebras I*, Springer (1979), Ch. III §2 | **used (L)**, for standard facts F1–F4 (§2) |

The search found no statement of BIDUAL-REL or of its negation, and no theorem on whether D\*\* is
maximal abelian in A\*\* for a MASA D ⊆ A with the extension property. The search was a web
search, which returned bibliographic records and abstracts; the papers in the context rows were
not read in full. Theorem REL is proved here on paper. Any novelty is relative to the corpus. A
reviewer with library access may find it stated elsewhere.

## 2. Standard facts used (L, Takesaki Ch. III §2)

- **F1.** Every φ ∈ A\* has a unique normal extension φ\*\* to A\*\*. Every bounded linear map
  T: A → A has a normal bitranspose T\*\*: A\*\* → A\*\* extending it.
- **F2.** For a representation π of A, the normal extension π̃: A\*\* → π(A)″ is a surjective
  \*-homomorphism with kernel (1 − z_π)A\*\*, where z_π is a central projection of A\*\* (the
  central support of π). For irreducible π, π(A)″ = B(H_π), so π̃ restricts to an isomorphism
  z_π A\*\* ≅ B(H_π). For a state f with GNS (π_f, H_f, ξ_f), f\*\*(Y) = ⟨ξ_f|π̃_f(Y)|ξ_f⟩ for every
  Y ∈ A\*\*.
- **F3.** Δ\*\* is a normal positive projection of A\*\* onto D\*\*, equal to the identity on D\*\*.
  For φ ∈ A\*, (φ∘Δ)\*\* = φ\*\*∘Δ\*\*, since both sides are normal and agree on A.
- **F4.** D\*\* = (D^⊥)^⊥, with D^⊥ := {φ ∈ A\* : φ|_D = 0} (the bipolar theorem for the
  σ(A\*\*, A\*) topology, which is the σ-weak topology of A\*\*).

## 3. B1 (decisive): BIDUAL-REL

**The state f.** Let B_n := {2^n − 1, …, 2^{n+1} − 2} for n ≥ 0. These are consecutive blocks of
length 2^n that partition ℕ. Put e_n := 2^{−n/2} Σ_{k∈B_n} |k⟩. The e_n are orthonormal, and e_n → 0
weakly. Let 𝒰 be a free ultrafilter on ℕ and f(b) := lim_{n→𝒰} ⟨e_n|b|e_n⟩ for b ∈ A.
- f is a state. It vanishes on the compact operators, since ‖ke_n‖ → 0 for compact k.
- On D, f(M_g) = lim_{n→𝒰} 2^{−n} Σ_{k∈B_n} g(k) =: μ(g).
- Write (π_f, H_f, ξ) for its GNS representation and z_f for its central support.

**Lemma PUR (f is pure; ESTABLISHED, X with MSS (L)).** Complete (e_n) to an orthonormal basis
(e_n) ∪ (e′_m) of H_V. The complement of span{e_n} is infinite-dimensional and separable, so the
basis is countable. Let D_e be the operators diagonal in this basis. D_e is a MASA unitarily
equivalent to D. On D_e, f(Σ x_n|e_n⟩⟨e_n| + Σ y_m|e′_m⟩⟨e′_m|) = lim_𝒰 x_n, which is
multiplicative, so f|_{D_e} is a pure state χ. By MSS, f is the only state extending χ. The set
of extensions of χ is a face of the state space: if f = tf_1 + (1 − t)f_2 with 0 < t < 1, then
χ = tf_1|_{D_e} + (1 − t)f_2|_{D_e}, so f_i|_{D_e} = χ, and f_i = f. Hence f is pure. ∎

So π_f is irreducible, and z_f A\*\* ≅ B(H_f) by F2. π_f vanishes on the compact operators, since
‖π_f(k)π_f(a)ξ‖² = f(a\*k\*ka) = 0. So every normal state ρ of A has ρ\*\*(z_f) = 0: π̃_f kills the
σ-weak limit z_K of an increasing approximate unit of the compacts, so z_f z_K = 0, while
ρ\*\*(z_K) = 1.

**Lemma DSJ (f∘Δ has no component in the sector of f; ESTABLISHED, X).** Put ψ := f∘Δ. Then
ψ\*\*(z_f) = 0.

*Proof.*
- *Invariance.* For a unitary u ∈ D, Δ(ubu\*) = uΔ(b)u\* = Δ(b), so ψ∘Ad_u = ψ, and by F1
  ψ\*\*(uYu\*) = ψ\*\*(Y) for Y ∈ A\*\*.
- *The density operator.* Put t := ψ\*\*(z_f) and suppose t > 0. Through z_f A\*\* ≅ B(H_f),
  Y ↦ ψ\*\*(Y) on z_f A\*\* is a normal positive functional on B(H_f). So it is X ↦ tr(ρX) for a
  positive trace-class ρ with tr ρ = t. Since z_f is central and π̃_f(uz_f) = π_f(u), invariance
  gives π_f(u)\*ρπ_f(u) = ρ for every unitary u ∈ D.
- *An eigenvector.* Let λ ∈ (0, t] be the largest eigenvalue of ρ, with unit eigenvector η, so
  ρ ≥ λ|η⟩⟨η|. Put g(b) := ⟨η|π_f(b)|η⟩. For b ≥ 0 in A, λg(b) ≤ tr(ρπ_f(b)) = ψ\*\*(z_f b) ≤ ψ(b),
  since b = z_f b + (1 − z_f)b with both terms positive.
- *A partition.* Fix l ≥ 1 and put L := 2^l. For n ≥ l, split B_n into L consecutive intervals
  B_{n,0}, …, B_{n,L−1} of length 2^{n−l}. Put A_j := ⋃_{n≥l} B_{n,j}, and add B_0 ∪ … ∪ B_{l−1}
  to A_0. Then (A_j) partitions ℕ, and ψ(1_{A_j}) = f(1_{A_j}) = lim_𝒰 |A_j ∩ B_n|/2^n = 1/L, since
  𝒰 is free. So ν_j := g(1_{A_j}) ≤ 1/(λL).
- *L vectors.* Put ζ := e^{2πi/L}, u_i := Σ_j ζ^{ij} 1_{A_j} ∈ D for i = 0, …, L − 1, and
  η_i := π_f(u_i)η. These are unit vectors, and by invariance ρ = π_f(u_i)ρπ_f(u_i)\* ≥
  λ|η_i⟩⟨η_i|, so ⟨η_i|ρ|η_i⟩ ≥ λ.
- *Their Gram matrix.* G_{ik} := ⟨η_i|η_k⟩ = g(u_i\*u_k) = Σ_j ζ^{(k−i)j} ν_j. So
  G = Σ_j ν_j w_j w_j\* with w_j := (ζ^{−ij})_i. The w_j are pairwise orthogonal with ‖w_j‖² = L, so
  ‖G‖ = L max_j ν_j ≤ 1/λ.
- *The bound.* Let T: ℂ^L → H_f send the i-th basis vector to η_i. Then T\*T = G and
  TT\* = Σ_i |η_i⟩⟨η_i|. Hence
  λL ≤ Σ_i ⟨η_i|ρ|η_i⟩ = tr(ρTT\*) ≤ ‖G‖ tr ρ ≤ t/λ,
  so t ≥ λ²L. λ does not depend on l, and t ≤ 1, so l with 2^l > 1/λ² gives a contradiction. ∎

**Theorem REL (BIDUAL-REL fails; ESTABLISHED, X, using a free ultrafilter and MSS).** Let P_f be the
projection of H_f onto the closure of π_f(D)ξ, and let s ∈ A\*\* be the element with s = z_f s and
π̃_f(s) = P_f. Then s is a projection, s ∈ D′ ∩ A\*\* and s ∉ D\*\*.

*Proof.*
- s is a projection, since π̃_f is an isomorphism on z_f A\*\*.
- *s commutes with D.* For d ∈ D, ds = (dz_f)s and sd = s(dz_f), with π̃_f(dz_f) = π_f(d). The
  subspace P_f H_f is invariant under the \*-closed set π_f(D), so π_f(d)P_f = P_fπ_f(d). Both ds
  and sd lie in z_f A\*\*, where π̃_f is injective, so ds = sd.
- *f sees s.* f\*\*(s) = ⟨ξ|P_f|ξ⟩ = 1 (F2).
- *s is not in D\*\*.* If s ∈ D\*\*, then Δ\*\*(s) = s (F3), so ψ\*\*(s) = f\*\*(Δ\*\*(s)) = f\*\*(s) = 1.
  But 0 ≤ s ≤ z_f, so ψ\*\*(s) ≤ ψ\*\*(z_f) = 0 (Lemma DSJ). ∎

*Remarks.*
- s corresponds to the D-cyclic subspace of the GNS vector of f, in the irreducible summand
  B(H_f) of A\*\*. It lies in the singular part: s ≤ z_f ≤ 1 − z_K.
- Δ\*\*(s) ∈ D\*\* satisfies f\*\*(Δ\*\*(s)) = 0, so s − Δ\*\*(s) is a non-zero element of the
  relative commutant on which Δ\*\* vanishes.
- *Comparison with the norm level.* M2 RED-M2's step D′ ∩ A = D uses only that D is maximal
  abelian in A. MSS is the stronger statement that pure states of D extend uniquely. Theorem REL
  shows that neither property passes to the bidual. The mechanism is Lemma DSJ: the dephasing f∘Δ
  of a pure state whose configuration law μ admits partitions of measure 1/L for every L has no
  component in the sector of f.

**Verdict B1: REFUTED.**

## 4. B2: the consequence for (F-S)

Throughout, an affine assignment ρ ↦ Ω_ρ of states of B to the states of A corresponds to a
positive unital map E: B → A\*\* by Ω_ρ = ρ\*\*∘E. In one direction this is M2 Proposition BID; in
the other, ρ ↦ ρ\*\*∘E is affine. PROD reads E(a ⊗ c) = ω(c)a. For a branch Φ_o in M2 RED-M2's
class, M2's DET-at gives Φ_o\*(M_g ⊗ 1) = M_h with h ∈ ℓ^∞(C_V × Z), and the output configuration
law is ρ ↦ ρ\*\*(E(M_h)).

**Proposition BID′ (BID's condition is necessary for a fixed assignment; ESTABLISHED, X, using
Hahn–Banach through F4).** Let E be positive and unital, and h real. Then ρ ↦ ρ\*\*(E(M_h)), on
states of A, depends on ρ only through ρ|_D if and only if E(M_h) ∈ D\*\*.

*Proof.*
- "If" is M2 Proposition BID's last step.
- "Only if." x := E(M_h) is self-adjoint. If x ∉ D\*\*, then by F4 some φ ∈ D^⊥ has φ(x) ≠ 0.
  Its hermitian or skew-hermitian part lies in D^⊥ and is non-zero at x, so φ may be taken
  hermitian. Since φ(1) = 0, the Jordan decomposition φ = φ_+ − φ_− has φ_+(1) = φ_−(1) =: c > 0.
- The states ρ := φ_+/c and ρ′ := φ_−/c agree on D, and ρ\*\*(x) − ρ′\*\*(x) = φ(x)/c ≠ 0. ∎

So a branch is DIO-type in (F-S), for a given assignment, exactly when E(Φ_o\*(M_g ⊗ 1)) ∈ D\*\* for
every g. By M2 Lemma CMP such values always lie in D′ ∩ A\*\*. Theorem REL shows that this set is
strictly larger than D\*\*, so M2's sufficient condition gives no general conclusion. Whether a
value outside D\*\* is attained is a separate question, answered by Theorem NDIO.

**Proposition HN (a normal hidden state forces DIO-type; ESTABLISHED, X).** Let ω be normal, and
let E: B → A\*\* be positive and unital with E(a ⊗ c) = ω(c)a. Then E(M_h) ∈ D for every
h ∈ ℓ^∞(C_V × Z). Hence every affine assignment with PROD and normal ω is DIO-type in (F-S), on
all visible inputs, for every branch in RED-M2's class.

*Proof.*
- Take h real, and ε > 0. Since ω is normal, Σ_z ω(P_z) = 1 (M1 Lemma NRM (a)), so there is a
  finite F ⊆ Z with ω(1 − P_F) ≤ ε. Put P := 1 ⊗ P_F. Then E(1 − P) = ω(1 − P_F)1 ≤ ε1.
- For a state φ of A\*\*, φ∘E is a state of B, and Cauchy–Schwarz gives
  |φ(E((1 − P)b))|² ≤ ε‖b‖². So |φ(E(b) − E(PbP))| ≤ 2√ε‖b‖. For self-adjoint b this gives
  ‖E(b) − E(PbP)‖ ≤ 2√ε‖b‖.
- PM_hP = Σ_{z∈F} M_{h(·,z)} ⊗ P_z is a finite sum of elementary tensors, so
  E(PM_hP) = Σ_{z∈F} ω(P_z) M_{h(·,z)} ∈ D.
- So E(M_h) is a norm limit of elements of D, and lies in D. Complex h follows by linearity. ∎

Together with M2 Lemma JU (normal visible input), a non-DIO assignment needs both a non-normal ω
and a non-normal visible input.

**Construction GLU (gluing a joint state onto the sector of f; ESTABLISHED, X).** Let f be the pure
state of §3, ω any state of B(H_Z), and Ω any state of B with Ω(a ⊗ c) = f(a)ω(c).
- *An isometry.* V: H_f → H_Ω, Vπ_f(a)ξ := π_Ω(a ⊗ 1)ξ_Ω, is well defined and isometric, since
  ‖π_Ω(a ⊗ 1)ξ_Ω‖² = Ω(a\*a ⊗ 1) = f(a\*a).
- *A sector map.* E_Ω(b) := V\*π_Ω(b)V is a unital completely positive map B → B(H_f), with
  ⟨ξ|E_Ω(b)|ξ⟩ = Ω(b). It satisfies PROD in the sector:
  ⟨π_f(x)ξ|E_Ω(a ⊗ c)|π_f(y)ξ⟩ = Ω(x\*ay ⊗ c) = ω(c)⟨π_f(x)ξ|π_f(a)|π_f(y)ξ⟩.
- *The glued map.* Put E(b) := (1 − z_f)σ_ω(b) + π̃_f^{−1}(E_Ω(b)), where π̃_f^{−1} denotes the
  inverse of z_f A\*\* ≅ B(H_f). E: B → A\*\* is completely positive and unital. Since
  π̃_f^{−1}(π_f(a)) = z_f a, it satisfies E(a ⊗ c) = ω(c)((1 − z_f)a + z_f a) = ω(c)a, which is PROD.
- *Its assignment.* Ω_ρ := ρ\*\*∘E is an affine assignment on all states of A, satisfying PROD:
  - for normal ρ, ρ\*\*(z_f) = 0, so Ω_ρ = ρ∘σ_ω, as M2 Lemma JU requires;
  - Ω_f = Ω, since f\*\*(1 − z_f) = 0;
  - Ω_ψ = ψ∘σ_ω for ψ = f∘Δ, by Lemma DSJ.

  In each case the term killed by a zero value of ρ\*\*(z_f) or ρ\*\*(1 − z_f) vanishes by
  Cauchy–Schwarz.

E takes values in A\*\*, not in A. This is consistent with M2 Lemma SL, which makes σ_ω the only
positive map into A with PROD, and it leaves (F-H) untouched.

**Theorem NDIO (a non-DIO affine assignment; ESTABLISHED, X, using free ultrafilters and MSS).**
- *The hidden state.* Let w be a free ultrafilter on Z = ℕ and ω := lim_{z→w}⟨z|·|z⟩. This is
  diagonal and non-normal.
- *The assignment.* Take Ω := ω∘σ′_f, the slice order that appends f to ω. It satisfies PROD
  (M2 §5). Let E be the glued map of Construction GLU.
- *The instrument.*
  - Let C_V′ = C_V, Z′ = Z and S := {(v, z) : v < z}. S and its complement are countably infinite.
  - Let A_e ⊆ C_V′ be the even numbers, and F: C_V × Z → C_V′ × Z′ a bijection with
    F(S) = A_e × Z′ and F(C_V × Z ∖ S) = (C_V′ ∖ A_e) × Z′.
  - The single-outcome branch Φ\*(b) := U_F\*bU_F, with U_F|x⟩ = |F(x)⟩, is unitary conjugation by
    a configuration permutation. It is normal and completely positive, satisfies TB with equality
    and satisfies σ-D with f_o = F, as in M2 CX-M.
  - Φ\*(M_{1_{A_e}} ⊗ 1) = M_{1_S}.
- *The outcome.* The probability that the visible output configuration lies in A_e is
  p(ρ) = Ω_ρ(M_{1_S}).
  - *Input f.* p(f) = Ω(M_{1_S}) = ω(σ′_f(M_{1_S})). Here σ′_f(M_{1_S}) is multiplication by
    z ↦ f(M_{1_{[0,z)}}) = lim_{n→𝒰} |B_n ∩ [0, z)|/2^n = 0, since B_n lies beyond z for large n.
    So p(f) = 0.
  - *Input ψ = f∘Δ.* p(ψ) = ψ(σ_ω(M_{1_S})). Here σ_ω(M_{1_S}) is multiplication by
    v ↦ lim_{z→w} 1_{z>v} = 1. So p(ψ) = 1.
- *The comparison.* ψ|_D = f|_D, since Δ is the identity on D. So two visible inputs with the same
  configuration law give output configuration laws that differ, 0 and 1. The visible instrument is
  not DIO-type in (F-S). By Proposition BID′, E(M_{1_S}) ∈ (D′ ∩ A\*\*) ∖ D\*\*, which is a second
  witness for Theorem REL. ∎

*Reading.*
- Within the sector of f, the assignment uses the slice order "ρ appended to ω". Outside it, it
  uses "ω appended to ρ", which is σ_ω. Each order alone is DIO-type (M2 §5). The failure comes
  from choosing the joint state sector by sector.
- The distinction is between f and its dephasing f∘Δ. For these inputs the instrument is a
  coherence detector, and its detecting power sits in the assignment, not in Φ, which is a
  configuration bijection.

**Verdict B2: a non-DIO affine assignment with PROD exists.** It needs a non-normal ω and a
non-normal visible input (Proposition HN, M2 Lemma JU). The positive results of M2 §5 for the two
slice orders, and of M2 RED-M2 in (F-H), are unaffected.

## 5. B3: existence and realizability

- **Choice principles.** The free ultrafilters 𝒰 and w come from the ultrafilter lemma.
  Proposition BID′ uses Hahn–Banach, through F4. MSS is a theorem of ZFC. Whether any choice
  principle is necessary is not checked.
- **Where the states stand** (LAW-σ and LAW-fa are readings of M2 §6, neither adopted):

  | State | Kind | LAW-σ | LAW-fa |
  |---|---|---|---|
  | ω | diagonal, non-normal | excluded | admitted |
  | ψ = μ∘Δ | diagonal, non-normal | excluded | admitted |
  | f | coherent, non-normal | excluded | excluded |

- **Native inputs.** Under LAW-fa the native visible inputs are diagonal, and two of them with
  the same configuration law are equal, so no native pair witnesses the non-DIO instrument. Under
  LAW-σ there is no native non-normal input.
- **Native appends.** The glued assignment is not delivered by NAT, and no physical preparation
  of f, of its sector or of the assignment is given or assumed. Its existence is mathematical.

**Verdict B3.** The failure of DIO-type in (F-S) is a mathematical fact about the typing. Neither
reading of LAW supplies a native instance of it. Whether non-σ-additive laws are physical is not
decided here.

## 6. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Lemma PUR | MSS (L), free ultrafilter | X, L | ELABORATING |
| Lemma DSJ | — | X | NEW: the dephasing of f carries no weight in the sector of f |
| Theorem REL | free ultrafilter, MSS | X | NEW: decides BIDUAL-REL (refuted) |
| Proposition BID′ | Hahn–Banach | X | ELABORATING: BID's condition is necessary for each assignment |
| Proposition HN | — | X | ELABORATING: normal ω forces DIO-type in (F-S) |
| Construction GLU, Theorem NDIO | free ultrafilters, MSS | X | NEW: (F-S) admits a non-DIO affine assignment with PROD |
| §5 realizability | LAW-σ, LAW-fa readings | X | ELABORATING |

**AW-4 (assumption-watch marker).**
- The extension property of a MASA (MSS for ℓ^∞ ⊆ B(ℓ²)) and its maximality at the norm level do
  not pass to the bidual.
- A state-space typing that admits non-normal inputs and fixes the joint state only through its
  product marginals (PROD) and affinity does not determine the output configuration law. A
  sector-wise choice of joint state can make it depend on coherence.
- A record that reasons from "affine assignment with PROD" to a property of all such assignments
  on non-normal inputs should check whether that property survives Construction GLU.

**Productivity test (`PLAN.md` §4).**
- *Stronger than the restatement:* the restatement is "BIDUAL-REL is open and is sufficient for
  (F-S) DIO-type". This record refutes BIDUAL-REL with a witness, shows that the sufficient
  condition is also necessary for each assignment, and gives a non-DIO assignment.
- *(i) Decides:* BIDUAL-REL, and the (F-S) DIO question for the affine PROD class (no). It also
  narrows where DIO-type fails, to non-normal ω together with a non-normal input.
- *(ii) Exposes a hidden assumption:* AW-4.
- **Gem. Output class NEW.**

*Skepticism.* The refutation was checked at each step where a favourable reading could enter:
- the identification z_f A\*\* ≅ B(H_f) needs purity, which rests on MSS;
- the bound t ≥ λ²L uses only ρ ≥ λ|η_i⟩⟨η_i| and ‖G‖ ≤ 1/λ;
- the step from s ∈ D\*\* to ψ\*\*(s) = 1 uses only F3;
- in Theorem NDIO, PROD is verified on all of B(H_V) ⊗ B(H_Z), and normal inputs reproduce σ_ω.

## 7. Drop-one

| Premise | Status |
|---|---|
| a non-normal ω | **needed**: with ω normal every affine PROD assignment is DIO-type (HN) |
| a non-normal visible input | **needed**: on normal inputs the joint state is unique (M2 JU) |
| affinity of the assignment | used to pass to E (M2 BID); without it the case is NN M3 |
| PROD | kept. GLU satisfies it exactly |
| TB, σ-D | satisfied by the instrument, a single configuration bijection; not otherwise used |
| KIN-B, KIN-𝒟, LIN | define the setting: configuration basis, coherence relative to ℓ^∞, positive maps |
| DEC | used only through PROD (the hidden state is appended independently) |
| NAT | not used, not adopted |
| MSS | used only for purity of f (Lemma PUR) |
| complete positivity | not used. GLU and Φ are completely positive, but only positivity is needed |

## 8. ESTABLISHED, ASSUMED, MISSING

**ESTABLISHED** (this record, layer X, unreviewed):
- Lemma PUR (with MSS (L)), Lemma DSJ and Theorem REL: BIDUAL-REL fails for C_V countably
  infinite;
- Proposition BID′: for a fixed affine assignment, M2 BID's condition is necessary as well as
  sufficient;
- Proposition HN: with ω normal, every affine PROD assignment is DIO-type in (F-S);
- Construction GLU and Theorem NDIO: an affine assignment with PROD, a diagonal non-normal ω and a
  σ-D configuration bijection give a visible instrument that is not DIO-type in (F-S);
- the realizability table of §5.

**ASSUMED:**
- (I): KIN-B, KIN-𝒟, LIN, TB, PROD, and the affine (F-S) typing;
- (N): DEC (through PROD) and σ-D (satisfied by the instrument);
- NAT: named, not adopted;
- LAW-σ and LAW-fa: readings, neither adopted;
- (L): MSS, and the standard bidual facts F1–F4.

**MISSING:**
- whether a choice principle is necessary for Theorem REL, and whether purity of f (and so MSS)
  can be avoided;
- whether π_f(D)″ is maximal abelian in B(H_f). This is not needed and not settled;
- whether some physically motivated restriction of (F-S), for example covariance of the
  assignment under the diagonal unitaries or under configuration permutations, or a single
  global slice order, restores DIO-type. No such restriction is proposed or adopted;
- NN M3 (nonlinear assignments), NN M4 (nativeness), M1-b and OPRES U1′: unchanged.

**Stop condition (`PLAN.md` §7).** B1 and B2 are both decided. There is no successor round.

## 9. What this record does not do

It edits no manuscript, Lean module, reviewed record, Issue or file of another track, and no path
in the A1 retirement ledger (`PLAN.md`, A1 ledger check). NONDIO-M2's branch is unchanged. It
adopts no premise, no reading of LAW and no nativeness criterion. It treats no non-normal state as
physically prepared, and it does not assume that infinite state spaces produce quantum
behaviour. It runs no computation.
