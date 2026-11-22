# NONDIO-M2: the non-DIO obstruction with a countably infinite visible carrier and a non-normal hidden state (research record)

**WIP / UNVERIFIED. Paper-only research. It awaits an independent non-author review.** This
record walks the nodes of `PLAN.md`, which was committed before it at `2c733cfd`. It runs no
computation. It edits no manuscript, Lean module, reviewed record or Issue. It adopts no premise,
changes no status and strengthens no manuscript or kernel theorem. No merge is authorized. The
pins, the formulation (F-at), the typings (F-H) and (F-S), and the assumptions are those of
`PLAN.md` §1, §3 and §4. Names without a prefix are this record's. Those prefixed "NN" are
NATIVE-NONDIO's at `ab830621`, and those prefixed "M1" are NONDIO-M1's at `dac9ca3f`.

Revision r2 answers the independent review of `b8cb9451` (#1509 c.7077843705, verdict REVISE).
- R1: the classical reading of the joint-state ambiguity is narrowed to diagonal marginals. The
  reviewer's pair with non-diagonal marginals is added as CX-F′.
- R2: AW-3's attribution is corrected at each pin.
- n1–n5 are applied.

No DIO-type or MIO-type result changes, and nothing is strengthened. `PLAN.md` is unchanged.

**Labels.**
- **ESTABLISHED**: proved on paper here (layer X), or cited at its source's standing: (L) a
  literature theorem, (R) a corpus record. "Established" means established within this record,
  not in the §A.46 sense.
- **ASSUMED**: a named premise.
- **MISSING**: a gap, stated with the node where the branch stopped.
- (N) native, (I) imported.

**Notation.** H_V = ℓ²(C_V), H_Z = ℓ²(Z), and B(ℓ²(C_V × Z)) = B(H_V ⊗ H_Z). For ξ ∈ H_V,
θ_ξ: H_Z → H_V ⊗ H_Z is k ↦ ξ ⊗ k, so ‖θ_ξ‖ = ‖ξ‖. For b ∈ B(H_V ⊗ H_Z),
b_{ξη} := θ_ξ\* b θ_η ∈ B(H_Z); for configurations v, v′ this is the (v, v′) block. Δ_V, Δ_Z and
Δ are the diagonal conditional expectations of B(H_V), B(H_Z) and B(H_V ⊗ H_Z). P_v is the
projection onto |v⟩.

## 0. Outcome

**(F-H): EXTENDS.** M2 as posed in NN N5 and M1 §5 is settled in the Heisenberg typing. The
obstruction is conditional throughout on TB, DEC, KIN-B and LIN, on σ-D at the total carrier, and
on NAT, a named premise that is not adopted (NN M4). Coherence is relative to the configuration
algebra ℓ^∞. Encoded carriers in the sense of T-SUB′ (iv) are outside every statement (NN §0).

**The exact class.** In (F-at), let C_V, Z, C_V′ and Z′ be sets of any cardinality; the case of the
question is C_V countably infinite. Let Φ_o\* be positive, satisfy TB and satisfy σ-D on the total
carrier. Let E: B(ℓ²(C_V × Z)) → B(ℓ²(C_V)) be any positive unital map that leaves the visible
configuration observables unchanged (VC: E(g ⊗ 1) = g for g ∈ ℓ^∞(C_V)). Then:

| Property | Class | Result |
|---|---|---|
| DIO-type of E∘Φ_o\*(· ⊗ 1) | every E with VC, so every hidden state ω, normal or not, appended by σ_ω; also classically correlated hidden priors | **yes** (RED-M2) |
| the slice σ_ω for non-normal ω and infinite C_V | every state ω of B(H_Z) | **exists** (Lemma VS), and is the **only** positive map with the product property PROD (Lemma SL) |
| MIO-type | E = σ_ω with ω = ω∘Δ_Z, normal or not | **yes** (MIO-M2) |
| MIO-type, non-diagonal ω | E = σ_ω, ω ≠ ω∘Δ_Z, and \|C_V\| = \|Z\| | **no** for a configuration bijection of the total carrier (CX-M); the coherence created changes no record law (IDLE-V) |
| record laws | every visible state, every E with VC; every total state | depend only on the configuration law (IDLE-V; M1 IDLE-∞) |

Neither normality of ω, nor finiteness of C_V (FIN-V), nor countability of C_V or Z, nor complete
positivity of E or Φ_o is used. This extends M1 RED-∞ (F-at), stated there for normal ω or finite
C_V, by the proof of §3; RED-∞ itself is not reinterpreted.

**(F-S): INCONCLUSIVE, with BIDUAL-REL missing.** This is the single outcome `PLAN.md` §2 asks for
in this typing. The following partial results are established:
- For a normal visible input ρ and any state ω, exactly one state of B(H_V ⊗ H_Z) has the product
  marginals, namely ρ∘σ_ω (Lemma JU). So every assignment satisfying PROD, linear or not, gives the
  (F-H) output on normal inputs, and is DIO-type there.
- For two non-normal states the joint state is not fixed by its marginals.
  - With diagonal marginals, CX-F gives two diagonal joint states with the same product marginals
    and different configuration laws on ℓ^∞(ℕ × ℕ). That ambiguity is the one of iterated
    ultrafilter limits on a commutative algebra, and is classical.
  - With non-diagonal marginals, CX-F′ gives two joint states with the same product marginals that
    differ on an element of zero diagonal. That ambiguity is not confined to the configuration
    algebra.
- Both slice orders are DIO-type. For a general affine assignment, DIO-type reduces to whether the
  relative commutant ℓ^∞(C_V)′ ∩ B(ℓ²(C_V))\*\* equals the σ-weak closure ℓ^∞(C_V)\*\* of the
  diagonal in the bidual (Proposition BID). **Missing ingredient: BIDUAL-REL.** It is a sufficient
  condition only; no non-DIO assignment is constructed.

**Mathematical existence and physical realizability (N5).**
- A state ω of B(ℓ²(Z)) is normal if and only if its configuration law is completely additive
  (M1 Lemma NRM (a), with a one-point input). For countable Z, a non-normal ω therefore has a
  configuration law that is finitely but not σ-additive.
- Such states exist by Hahn–Banach or by free ultrafilters. Every example here uses a free
  ultrafilter on ℕ.
- Under LAW-σ, no native hidden prior on a countable Z is non-normal, so NN-ω is not realized by
  NAT preparations. Under LAW-fa, native hidden priors are diagonal, μ∘Δ_Z, and for them both
  DIO-type and MIO-type hold. The non-diagonal non-normal states of CX-M, and the non-normal
  visible inputs of the (F-S) residual, are outside LAW in both readings.

**Assumption-watch marker AW-3 (§8).** M1 states that the slice needs FIN-V or a normal ω (M1
Verdict N1, "The slice in S9 needs FIN-V, or normal ω, outside (F-C\*)"; the S9 row). On
B(H_V ⊗ H_Z), the tensor product of two type-I factors, this is false. The vector slice exists for
every state, and it is unique among positive maps with the product property (VS, SL). NN N5
records the same slice as not established (M2), and VS closes that open item. OPRES Remark D′
asserts that σ_ω is not defined on L^∞(H₁) ⊗̄ L^∞(H) for non-normal ω when a diffuse factor H₁ is
present. As a statement about the vector slice this is false too, and it bears on OPRES U1′ (iii).
What is non-canonical is the joint state of two non-normal states. That ambiguity already occurs
in ℓ^∞(ℕ × ℕ) (CX-F), and for non-diagonal marginals it is not confined there (CX-F′).

**MISSING.** BIDUAL-REL (§5); OPRES U1′ (iii) in OPRES's own formulation (AW-3 bears on it, and it is
not checked here); an infinite-C_V form of OPRES Theorem C(b), which is not claimed; the nativeness
of the bijection in CX-M (NN M4); NN M3; M1-b (out of scope).

**Productivity (`PLAN.md` §5): gem.** The output class is ELABORATING, with one NEW
assumption-watch marker (AW-3) (§8).

## 1. Literature and sources

| Topic | Source | Use |
|---|---|---|
| Slice maps on von Neumann tensor products | J. Tomiyama, *Tensor products and projections of norm one in von Neumann algebras*, lecture notes, Univ. of Copenhagen (1970) | context: the slice id ⊗ ω is defined there for normal ω. No theorem is taken from it; Lemmas VS and SL are proved here |
| Kadison–Singer | R. V. Kadison, I. M. Singer, Amer. J. Math. 81, 383–400 (1959); A. Marcus, D. Spielman, N. Srivastava, Ann. of Math. 182, 327–350 (2015) | context only, for BIDUAL-REL (§5). Not used in any proof |
| Ultrafilter limits | classical | CX-F; proved here |

No source is claimed for Lemmas VS, SL, CMP and JU, for RED-M2, MIO-M2, Proposition BID, or for
CX-M and CX-F, all of which are elementary. Any novelty is relative to the corpus.

Corpus records read in full before the walk:
- NONDIO-M1 `PLAN.md` and `NOTE.md` at `dac9ca3f`, and its reviews (#1547 c.7077044631,
  c.7077116712) with their dispositions;
- NATIVE-NONDIO `PLAN.md` and `INVESTIGATION.md` at `ab830621`, and its reviews (#1544
  c.7075473914, c.7075888975, c.7075922740) with their dispositions;
- OPRES `NOTE.md` at `24702c1d`: Proposition D, its proof steps 1–7, Remark D′ and U1′. Its
  reviewer sketch for U1′ (ii) (c.7067475063) is read as OPRES records it.

## 2. N1 (decisive): the slice

**Lemma VS (the vector slice; ESTABLISHED, X).** Let H_V and H_Z be Hilbert spaces of any
dimension and ω any state of B(H_Z), normal or not. For each b ∈ B(H_V ⊗ H_Z) there is exactly one
σ_ω(b) ∈ B(H_V) with

⟨ξ|σ_ω(b)|η⟩ = ω(b_{ξη}) for all ξ, η ∈ H_V.

The map σ_ω is linear, unital, completely positive and of norm 1. It satisfies
- PROD: σ_ω(a ⊗ c) = ω(c) a;
- bimodularity: σ_ω((a ⊗ 1) b (a′ ⊗ 1)) = a σ_ω(b) a′.

*Proof.*
- (ξ, η) ↦ ω(b_{ξη}) is conjugate-linear in ξ, linear in η, and bounded by ‖b‖ ‖ξ‖ ‖η‖, since
  ‖b_{ξη}‖ ≤ ‖θ_ξ‖ ‖b‖ ‖θ_η‖. So it is the form of a unique operator of norm at most ‖b‖.
- For b ≥ 0, b_{ξξ} = θ_ξ\* b θ_ξ ≥ 0, so ⟨ξ|σ_ω(b)|ξ⟩ ≥ 0.
- Complete positivity: M_n(B(H_V ⊗ H_Z)) = B((ℂ^n ⊗ H_V) ⊗ H_Z), and for ξ = ⊕ξ_i, η = ⊕η_j
  one has Σ_{ij} ω((b_{ij})_{ξ_i η_j}) = ω(B_{ξη}) with B = [b_{ij}]. So (σ_ω)_n is the vector
  slice for ℂ^n ⊗ H_V, which is positive by the previous step.
- PROD: (a ⊗ c)_{ξη} = ⟨ξ|a|η⟩ c. Unitality is the case a = 1, c = 1.
- Bimodularity: ((a ⊗ 1) b (a′ ⊗ 1))_{ξη} = b_{a\*ξ, a′η}. ∎

*Relations.*
- σ_ω(1 ⊗ c) = ω(c)1, so σ_ω is normal if and only if ω is.
- For normal ω, σ_ω is normal and is the normal slice id ⊗ ω. Write ω = Σ_k λ_k ⟨e_k|·|e_k⟩, with
  (e_k) orthonormal, λ_k ≥ 0 and Σ_k λ_k = 1, and let V_k ξ := ξ ⊗ e_k. Then
  ⟨ξ|V_k\* b V_k|η⟩ = ⟨e_k|b_{ξη}|e_k⟩, so σ_ω = Σ_k λ_k V_k\*(·)V_k. This is a norm-convergent sum
  of normal maps, hence normal. The normal slice is positive and satisfies PROD, so Lemma SL
  identifies the two.
- For C_V finite it is id_n ⊗ ω. On ℓ^∞(C_V × Z) it is the pointwise slice
  f ↦ (ω(M_{f(v,·)}))_v of OPRES D′ step 3, since (M_f)_{vv′} = δ_{vv′} M_{f(v,·)}. M1 §5 records
  this pointwise slice as canonical for every ω; Lemma VS extends it off the diagonal.

**Lemma SL (uniqueness; ESTABLISHED, X).** Let E: B(H_V ⊗ H_Z) → B(H_V) be positive and linear,
with E(1) = 1 and E(|ξ⟩⟨ξ| ⊗ c) = ω(c)|ξ⟩⟨ξ| for every unit vector ξ and every c. In particular,
any positive E with PROD qualifies. Then E = σ_ω.

*Proof.* Fix a unit ξ, put ψ_ξ := ⟨ξ|E(·)|ξ⟩ and P_ξ := |ξ⟩⟨ξ| ⊗ 1.
- ψ_ξ is a state, and ψ_ξ(P_ξ) = ω(1) = 1.
- Cauchy–Schwarz gives ψ_ξ((1 − P_ξ)b) = 0 = ψ_ξ(b(1 − P_ξ)), so ψ_ξ(b) = ψ_ξ(P_ξ b P_ξ).
- P_ξ b P_ξ = |ξ⟩⟨ξ| ⊗ b_{ξξ}, so ψ_ξ(b) = ω(b_{ξξ}) = ⟨ξ|σ_ω(b)|ξ⟩.
- A bounded operator on a complex Hilbert space is fixed by its quadratic form (polarization). ∎

*Corollary SL′ (ESTABLISHED, X).* The map a ⊗ c ↦ ω(c)a on the minimal tensor product
B(H_V) ⊗_min B(H_Z) has exactly one positive extension to B(H_V ⊗ H_Z) with values in B(H_V),
namely σ_ω. Existence is Lemma VS (σ_ω is norm-continuous and agrees on elementary tensors);
uniqueness is Lemma SL.

**Circularity test (`PLAN.md` N1).** PROD fixes E on elementary tensors, and VC fixes E on
ℓ^∞(C_V) ⊗ 1. Neither mentions Φ_o. For C_V = Z = ℕ, ℓ^∞(C_V × Z) is not contained in the norm
closure of the algebraic tensor product: the two states of CX-F (§5) agree on elementary tensors,
and so on that closure, but differ on M_{1_{v<z}}. So DIO-type of the visible instrument does not
follow from either condition by linearity and continuity; it is derived in §3 through Lemma CMP.
Both conditions are admitted.

**Verdict N1.** In (F-H) the slice exists for every state ω and every visible carrier, and it is
forced by positivity and PROD. The obstruction named in NN N5 (M2) and M1 §5 is not present in
this typing.

## 3. N2: DIO-type of the visible instrument

**Lemma CMP (compression; ESTABLISHED, X).** Let 𝒜 and ℬ be unital C\*-algebras, E: 𝒜 → ℬ positive
and unital, and P ∈ 𝒜 a projection with E(P) = q a projection. If x ∈ 𝒜 commutes with P, then
E(x) commutes with q, and E(PxP) = qE(x)q.

*Proof.*
- For y ≥ 0 in the corner P𝒜P, 0 ≤ y ≤ ‖y‖P gives 0 ≤ E(y) ≤ ‖y‖q. So (1 − q)E(y)(1 − q) = 0,
  hence E(y)^{1/2}(1 − q) = 0 and E(y) = qE(y)q. Every element of the corner is a combination of
  four positive ones, so E(PxP) = qE(PxP)q for every x.
- The same holds for 1 − P, with E(1 − P) = 1 − q.
- If x commutes with P, then x = PxP + (1 − P)x(1 − P), so
  E(x) = qE(PxP)q + (1 − q)E((1 − P)x(1 − P))(1 − q). This commutes with q, and qE(x)q = E(PxP). ∎

This is the mechanism of M1 Lemma P, applied to a unital positive map. It needs neither
2-positivity nor normality, and ℬ may be a bidual (used in §5).

**Theorem RED-M2 (ESTABLISHED, X; (I) on KIN-B, LIN, TB, VC; (N) σ-D).** Let C_V, Z, C_V′, Z′ be
sets of any cardinality. Let Φ_o\*: B(ℓ²(C_V′ × Z′)) → B(ℓ²(C_V × Z)) be positive, satisfy TB and
satisfy σ-D with maps f_o: D_o → C_V′ × Z′, and write π_V for the projection onto C_V′. Let
E: B(ℓ²(C_V × Z)) → B(ℓ²(C_V)) be positive, unital and VC. Put Φ^V_o\*(a) := E(Φ_o\*(a ⊗ 1)).
Then:
- (i) Φ^V_o\*(ℓ^∞(C_V′)) ⊆ ℓ^∞(C_V): every visible branch is DIO-type.
- (ii) Σ_{o∈O′} Φ^V_o\*(1) ≤ 1 for every finite O′, and each Φ^V_o\*(1) lies in ℓ^∞(C_V).
- (iii) For E = σ_ω: Φ^V_o\*(M_g)(v) = ω(M_{h_v}), where
  h_v(z) := 1_{D_o}(v, z) g(π_V f_o(v, z)).

*Proof.*
- By M1 DET-at (i), Φ_o\*(M_g ⊗ 1) = Φ_o\*(M_{g∘π_V}) = M_h, with h(v, z) = 1_{D_o}(v, z)
  g(π_V f_o(v, z)), which lies in ℓ^∞(C_V × Z). DET-at holds for every cardinality, and σ-D makes
  Φ_o\* normal (M1 NRM-D).
- For a projection Q ∈ ℓ^∞(C_V), Q ⊗ 1 and M_h are multiplication operators, so they commute, and
  E(Q ⊗ 1) = Q by VC. Lemma CMP shows that E(M_h) commutes with Q.
- The projections of ℓ^∞(C_V) have norm-dense span, so E(M_h) ∈ ℓ^∞(C_V)′ ∩ B(H_V). This is
  ℓ^∞(C_V) for a set C_V of any cardinality: if T commutes with every P_v, then
  P_v T P_w = T P_v P_w = 0 for v ≠ w, so T is diagonal, and bounded diagonal operators are
  multiplication operators. This gives (i).
- (ii) Σ_{O′} Φ^V_o\*(1) = E(Σ_{O′} Φ_o\*(1)) ≤ E(1) = 1 by TB and positivity, and each term lies in
  ℓ^∞(C_V) by (i) with g = 1.
- (iii) ⟨v|σ_ω(M_h)|v′⟩ = ω((M_h)_{vv′}) = δ_{vv′} ω(M_{h(v,·)}). ∎

*What is not used.* Normality of ω and of E; finiteness or countability of C_V and Z; PROD (VC
suffices); complete positivity of E or Φ_o.

*Example of VC without PROD (ESTABLISHED, X; trivial instance).* For any family (ω_v)_{v∈C_V} of
states of B(H_Z), E(b) := Σ_v ω_v(b_{vv}) P_v is positive and unital, and E(g ⊗ 1) = g. It appends
a hidden prior correlated with the visible configuration. Its values lie in ℓ^∞(C_V) for every b,
so it also dephases the visible input, and RED-M2 holds for it trivially. It shows only that VC is
strictly weaker than PROD. It is not a non-trivial instance of RED-M2.

**Corollary IDLE-V (ESTABLISHED, X).** For every visible state ρ, normal or not, and every E with
VC:
- the probability of outcome o is ρ(Φ^V_o\*(1)), with Φ^V_o\*(1) ∈ ℓ^∞(C_V);
- the joint law of outcome and visible output configuration is ρ∘Φ^V_o\*|_{ℓ^∞(C_V′)}.

Both depend on ρ only through ρ|ℓ^∞(C_V). Two visible inputs with the same configuration law are
not distinguished by any native visible instrument. For the total carrier, M1 IDLE-∞ (R) gives the
same for every state of B(ℓ²(C_V × Z)).

**Verdict N2: YES** for the class of RED-M2: every visible instrument obtained from a positive
extension satisfying TB and σ-D, through any positive unital append with VC, is DIO-type. No
counterexample exists inside that class.

## 4. N3: MIO-type and creation

**Theorem MIO-M2 (ESTABLISHED, X).** In RED-M2 with E = σ_ω and ω = ω∘Δ_Z, normal or not,
Δ_V Φ^V_o\* = Δ_V Φ^V_o\* Δ_V′: every visible branch is MIO-type in Heisenberg form.

*Proof.*
- (Δb)_{vv′} = δ_{vv′} Δ_Z(b_{vv}), since Δb = Σ_{(v,z)} P_{(v,z)} b P_{(v,z)} σ-weakly and
  b ↦ b_{vv} is normal. With ω = ω∘Δ_Z this gives σ_ω(Δb) = Δ_V σ_ω(b).
- Δ(a ⊗ 1) = Δ_V′(a) ⊗ 1, and M1 DET-at (ii) gives Δ Φ_o\* = Δ Φ_o\* Δ.
- So Δ_V σ_ω Φ_o\*(a ⊗ 1) = σ_ω Δ Φ_o\*(Δ_V′(a) ⊗ 1) = Δ_V σ_ω Φ_o\*(Δ_V′(a) ⊗ 1). ∎

**Counterexample CX-M (a non-diagonal ω creates; ESTABLISHED, X, using a free ultrafilter).**
- *The hidden state.* Let Z = ℕ, let 𝒰 be a free ultrafilter on ℕ, and put
  ξ_n := (|2n⟩ + |2n + 1⟩)/√2 and ω(b) := lim_{n→𝒰} ⟨ξ_n|b|ξ_n⟩.
  - ω is a state, and it vanishes on every finite-rank operator because ξ_n → 0 weakly. So
    Σ_z ω(P_z) = 0 ≠ 1, and ω is not normal (M1 NRM (a)).
  - K := Σ_n (|2n⟩⟨2n + 1| + |2n + 1⟩⟨2n|) has norm 1, ω(K) = 1 and Δ_Z K = 0, so
    ω ≠ ω∘Δ_Z.
- *The total action.* Let C_V = C_V′ = ℕ and Z′ = Z, let β: C_V → Z be a bijection, B the unitary
  |v⟩ ↦ |β(v)⟩, and f(v, z) := (β^{-1}(z), β(v)), a bijection of the total carrier. Its
  permutation unitary U(ξ ⊗ k) = B\*k ⊗ Bξ gives Φ\*(b) = U\* b U. This map is positive (indeed
  CP), normal, satisfies TB with equality, and satisfies σ-D with f_o = f.
- *The visible instrument.* Φ\*(a ⊗ 1) = 1 ⊗ BaB\*, so Φ^V\*(a) = σ_ω(1 ⊗ BaB\*) = ω(BaB\*)1.
  Every visible input goes to the visible state ω∘Ad_B.
  - It is DIO-type: Φ^V\*(M_g) = ω(M_{g∘β^{-1}})1. RED-M2 applies.
  - It is not MIO-type: Φ^V\*(B\*KB) = 1, while Δ_V(B\*KB) = B\*(Δ_Z K)B = 0.
  - It is not normal, and it sends every normal visible input to a non-normal coherent output.
    This is the case named in the U1′ (ii) sketch that OPRES records, a non-normal output visible
    marginal. The instrument is DIO-type in that case.

CX-M is NN 4d (an appended non-diagonal hidden state creates coherence) on a countably infinite
visible carrier. It is a mathematical construction. Whether a bijection of this kind is a step of
the selected φ is not addressed (NN M4), and ω is outside LAW in both readings (§6). By IDLE-V, the
created coherence changes no record law.

**Verdict N3.** MIO-type holds for every diagonal hidden state, normal or not. For every
non-diagonal ω, CX-M's construction gives a DIO-type, non-MIO-type visible instrument whenever
C_V and Z have the same cardinality.

## 5. N4: the state-space typing (F-S) and joint states

**Lemma JU (a normal visible input fixes the joint state; ESTABLISHED, X).** Let ρ be a normal
state of B(H_V) and ω any state of B(H_Z). Exactly one state Ω of B(H_V ⊗ H_Z) satisfies
Ω(a ⊗ c) = ρ(a)ω(c), namely ρ∘σ_ω.

*Proof.*
- ρ∘σ_ω qualifies by Lemma VS.
- Let Ω qualify. Given ε > 0, take a finite-rank projection Q with ρ(1 − Q) ≤ ε, which exists
  because ρ is normal, and put P := Q ⊗ 1. Then Ω(1 − P) = ρ(1 − Q) ≤ ε, and Cauchy–Schwarz gives
  |Ω(b) − Ω(PbP)| ≤ 2‖b‖ε^{1/2}.
- PbP ∈ B(QH_V ⊗ H_Z), and QH_V is finite-dimensional, so PbP = Σ_{ij} e_{ij} ⊗ c_{ij} for matrix
  units e_{ij} of QH_V. Hence Ω(PbP) = Σ_{ij} ρ(e_{ij}) ω(c_{ij}) is fixed by PROD. As ε → 0, Ω(b)
  is fixed. ∎

*Consequence.* In (F-S), every assignment ρ ↦ Ω_ρ satisfying PROD, linear or not, agrees with
(F-H) on normal visible inputs. Its output configuration law depends only on ρ|ℓ^∞(C_V) there
(RED-M2 with E = σ_ω). This makes OPRES's reviewer sketch for U1′ (ii) precise: for normal visible
ρ the joint state is defined for any ω and gives Σ_v ρ_vv ω(f_v). Lemma JU adds uniqueness.

**Counterexample CX-F (two non-normal marginals do not fix the joint configuration law;
ESTABLISHED, X, using free ultrafilters).** Let C_V = Z = ℕ, let u and w be free ultrafilters on
ℕ, and put ρ_u(a) := lim_{v→u} ⟨v|a|v⟩ and ω_w(c) := lim_{z→w} ⟨z|c|z⟩. Both are diagonal
and non-normal.
Let σ′_ρ: B(H_V ⊗ H_Z) → B(H_Z) be the vector slice over the first factor (Lemma VS with the
factors exchanged).
- Ω_1 := ρ_u∘σ_{ω_w} (ω appended to ρ) and Ω_2 := ω_w∘σ′_{ρ_u} (ρ appended to ω) are states with
  Ω_i(a ⊗ c) = ρ_u(a) ω_w(c).
- For f ∈ ℓ^∞(ℕ × ℕ), Ω_1(M_f) = lim_{v→u} lim_{z→w} f(v, z) and
  Ω_2(M_f) = lim_{z→w} lim_{v→u} f(v, z).
- For f = 1_{v<z}: the set {z : z > v} is cofinite and lies in w, so Ω_1(M_f) = 1; the set
  {v : v < z} is finite and does not lie in u, so Ω_2(M_f) = 0.
- Both are diagonal states: Ω_i∘Δ = Ω_i.

So the joint state of two non-normal states is not fixed by its marginals. For these diagonal
marginals the difference lies in the commutative algebra ℓ^∞(ℕ × ℕ), between two incoherent
states. By Lemma SL, Ω_2 is not ρ_u∘E for any positive E: B(H_V ⊗ H_Z) → B(H_V) with PROD.

**Counterexample CX-F′ (with non-diagonal marginals the ambiguity is not classical; ESTABLISHED,
X, using free ultrafilters; from the review, c.7077843705, R1, checked here).** Let C_V = Z = ℕ,
let ξ_n := (|2n⟩ + |2n + 1⟩)/√2 as in CX-M, let u and w be free ultrafilters, and put
ρ := lim_{n→u} ⟨ξ_n|·|ξ_n⟩ and ω := lim_{m→w} ⟨ξ_m|·|ξ_m⟩.
- Put Ω_1 := ρ∘σ_ω and Ω_2 := ω∘σ′_ρ. Both satisfy PROD. Writing η_{nm} := ξ_n ⊗ ξ_m, Lemma VS gives
  Ω_1(b) = lim_{n→u} lim_{m→w} ⟨η_{nm}|b|η_{nm}⟩, and Ω_2(b) is the same with the limits in the
  other order.
- The η_{nm} are orthonormal, so X := Σ_{n<m} |η_{nm}⟩⟨η_{nm}| is a projection with
  ⟨η_{nm}|X|η_{nm}⟩ = 1_{n<m}.
- Each η_{nm} has the four diagonal entries ¼ on {2n, 2n + 1} × {2m, 2m + 1}, so ΔX = ¼ M_f with
  f(v, z) = 1 when ⌊v/2⌋ < ⌊z/2⌋ and 0 otherwise. Then ⟨η_{nm}|ΔX|η_{nm}⟩ = ¼ 1_{n<m}.
- Put Y := X − ΔX, so ΔY = 0. Since {m : m > n} ∈ w and {n : n < m} ∉ u:
  - Ω_1(X) = 1 and Ω_1(ΔX) = ¼, so Ω_1(Y) = ¾;
  - Ω_2(X) = 0 and Ω_2(ΔX) = 0, so Ω_2(Y) = 0.

So Ω_1 − Ω_2 ≠ (Ω_1 − Ω_2)∘Δ. The two joint states differ on an element with zero diagonal, so
their difference is not confined to ℓ^∞(C_V × Z). RED-M2 and the DIO-type of both slice orders are
unaffected, since they concern only the configuration law of the output.

*Both slice orders are DIO-type (ESTABLISHED, X).* The assignment ρ ↦ ρ∘σ_ω is (F-H). For
ρ ↦ ω∘σ′_ρ, which is affine and satisfies PROD, and for diagonal a, σ′_ρ(Φ_o\*(a ⊗ 1)) =
σ′_ρ(M_h) is the multiplication operator z ↦ ρ(M_{h(·,z)}), which depends on ρ only through
ρ|ℓ^∞(C_V). So the output configuration law does too.

**Proposition BID (reduction of the affine case; ESTABLISHED, X).** Let ρ ↦ Ω_ρ be an affine
assignment, on all states of B(H_V), of states of B(H_V ⊗ H_Z) satisfying PROD.
- It extends to a positive linear map L: B(H_V)\* → B(H_V ⊗ H_Z)\*. The restriction to
  B(H_V ⊗ H_Z) of the adjoint, E: B(H_V ⊗ H_Z) → B(H_V)\*\*, is positive and unital, and
  E(a ⊗ c) = ω(c)a, with B(H_V) ⊆ B(H_V)\*\* canonically.
- Lemma CMP with ℬ = B(H_V)\*\* and P = Q ⊗ 1, Q ∈ ℓ^∞(C_V), gives
  E(Φ_o\*(a ⊗ 1)) ∈ ℓ^∞(C_V)′ ∩ B(H_V)\*\* for diagonal a.
- The output configuration law is ρ\*\*(E(Φ_o\*(a ⊗ 1))), with ρ\*\* the normal extension of ρ. On
  ℓ^∞(C_V)\*\*, the σ-weak closure of ℓ^∞(C_V) in the bidual, ρ\*\* is fixed by ρ|ℓ^∞(C_V).

Hence: **if BIDUAL-REL holds, that is, ℓ^∞(C_V)′ ∩ B(ℓ²(C_V))\*\* = ℓ^∞(C_V)\*\*, then every affine
assignment satisfying PROD is DIO-type in (F-S).** ∎

**BIDUAL-REL (MISSING).** It is not settled here whether the relative commutant of the diagonal in
the bidual of B(ℓ²(C_V)) is the bidual of the diagonal, for C_V countably infinite. Multiplication
in the bidual is separately σ-weakly continuous, so ℓ^∞(C_V)′ = (ℓ^∞(C_V)\*\*)′ there, and BIDUAL-REL
is equivalent to ℓ^∞(C_V)\*\* being maximal abelian in B(ℓ²(C_V))\*\*. No literature search was run
on it (audit-method Step 4). In particular, maximality of D\*\* in A\*\* for a MASA D ⊆ A with the
extension property was not searched for. It concerns
only states that vanish on the compact operators, since on normal states Lemma JU already settles
the question. It is a question about the diagonal MASA, adjacent to Kadison–Singer (context, not
used) and to M1-b, which needs separate authorization. BIDUAL-REL is a sufficient condition. Its
failure would not by itself give a non-DIO assignment: that would need an affine assignment with
PROD whose E takes a value outside ℓ^∞(C_V)\*\* on ℓ^∞(C_V × Z), and none is constructed.
Assignments that are not affine on non-normal visible inputs are NN M3.

**Verdict N4: INCONCLUSIVE, with BIDUAL-REL missing.** This is the single (F-S) outcome. The
established partial results are these:
- (F-S) is DIO-type on normal visible inputs, for every assignment with PROD;
- it is DIO-type on all inputs for both slice orders;
- the non-uniqueness of joint states is classical for diagonal marginals (CX-F), and not confined
  to the configuration algebra for non-diagonal ones (CX-F′).

## 6. N5: mathematical existence and physical realizability

- **Characterization (ESTABLISHED, X, from M1 Lemma NRM (a)).** Apply NRM (a) to the positive map
  Φ\*(a) := ω(a)·1 into B(ℂ) (a one-point input carrier). A state ω of B(ℓ²(Z)), Z any set, is
  normal if and only if Σ_z ω(P_z) = 1, that is, if and only if its configuration law ω|ℓ^∞(Z) is
  completely additive. For countable Z this is σ-additivity. A non-normal ω therefore assigns
  weight 1 − Σ_z ω(P_z) > 0 that no configuration carries.
- **Existence (ESTABLISHED, X).** Non-normal states exist on B(ℓ²(Z)) for every infinite Z: a free
  ultrafilter gives one (CX-M, CX-F), and so does Hahn–Banach (M1 CX-1′, CX-1). Each construction
  here uses a choice principle. Whether choice is necessary is not checked here.
- **LAW-σ (reading; not adopted).** Native hidden priors on a countable Z are configurations or
  σ-additive laws μ over them, so they are μ∘Δ_Z with μ σ-additive: normal and diagonal. Under
  NAT with LAW-σ, NN-ω is not realized by any native hidden prior. Visible preparations are normal
  for the same reason, so the (F-S) residual of §5 does not arise for native inputs.
- **LAW-fa (reading; not adopted).** Native hidden priors are μ∘Δ_Z with μ a state of ℓ^∞(Z). They
  may be non-normal, and they are always diagonal, so RED-M2 and MIO-M2 apply: they are DIO-type and
  MIO-type. Native visible inputs are diagonal as well, so two of them with the same configuration
  law are equal, and the (F-S) question is empty for them.
- **Outside LAW in both readings:** the non-diagonal non-normal ω of CX-M, and coherent non-normal
  visible inputs. Their existence is mathematical. NAT and LAW do not deliver them, and no
  physical preparation of them is given or assumed here.
- **DEC.** An adjoined deep factor with non-configuration dynamics is prepared independently and
  leaves every reduced visible channel unchanged (NN §0, 4e). RED-M2 adds nothing to that, and the
  drop-one example Ad_H stands (§7).

**Verdict N5.** M2's hypothesis is a mathematical case. Under LAW-σ it has no native instance;
under LAW-fa its native instances are diagonal, and for them DIO-type and MIO-type hold. NAT and
LAW do not settle whether non-σ-additive hidden laws are physical; that is not decided here.

## 7. N6: drop-one

| Premise | Dropped | Effect |
|---|---|---|
| σ-D at the total carrier | point determinism only, non-normal total map | **fails**: M1 CX-1′ on C_V = C_V′ = ℕ, with Z a single point and E = id. Put Φ\*(a) := ψ₁(a)\|+⟩⟨+\| + ψ₂(a)\|−⟩⟨−\| + Σ_{v≥2} ⟨v\|a\|v⟩P_v, with \|±⟩ in the span of \|0⟩, \|1⟩ and ψ_i extending free ultrafilters u₁ ≠ u₂ on C_V′. Then Φ\*(1) = 1, every p(y \| x) is 0 or 1, and Φ\*(P_C) is not diagonal for C ∈ u₁ ∖ u₂ |
| TB | the bound on configuration inputs only | **fails**: NN's Ψ(ρ) = 2⟨+\|ρ\|+⟩\|0⟩⟨0\| on two visible configurations, with the identity elsewhere |
| DEC | a unitary deep factor coupled by configuration swaps | **fails**: Ad_H on the visible system (NN 4e) |
| VC | an append that moves visible configurations, E := Ad_W ∘ σ_ω with W a non-monomial unitary of H_V | **fails**: with Φ = id, Φ^V\* = W\*(·)W is not DIO-type. Such an E is a coherent visible operation, outside NAT |
| PROD | VC kept | **not used** for DIO-type (RED-M2). Used for the uniqueness of the slice (SL) and for MIO-M2 |
| normality of ω | — | **not used** |
| FIN-V | — | **not used** |
| countability of C_V or Z | — | **not used** |
| complete positivity of E or Φ_o | — | **not used** |
| diagonal ω, for MIO | a non-diagonal ω | MIO **fails**: CX-M. DIO is unaffected |
| linearity of the assignment, (F-S), normal inputs | — | **not used** (JU) |
| linearity of the assignment, (F-S), non-normal inputs | — | used by Proposition BID; without it the case is NN M3 |
| KIN-B | a rotated logical basis; encoded carriers | as in NN N6: relocated to the interface, or outside the statement |

## 8. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Lemma VS, Lemma SL, Corollary SL′; AW-3 | — | X | **NEW** (assumption-watch): the slice by a non-normal state on B(H_V ⊗ H_Z) exists for an infinite visible carrier and is forced by positivity and PROD |
| Lemma CMP | — | X | ELABORATING: the mechanism of M1 Lemma P for a unital positive map, into any C\*-algebra |
| RED-M2, IDLE-V | (I): KIN-B, LIN, TB, VC; (N): σ-D | X | ELABORATING: decides M2 in (F-H), and weakens PROD to VC |
| MIO-M2 | as RED-M2, with PROD and diagonal ω | X | ELABORATING |
| CX-M | free ultrafilter | X | CONFIRMING: NN 4d on a countably infinite visible carrier |
| Lemma JU | — | X | ELABORATING: uniqueness behind OPRES's U1′ (ii) sketch |
| CX-F | free ultrafilters | X | ELABORATING: locates the non-canonical joint state, and shows it is classical for diagonal marginals |
| CX-F′ | free ultrafilters; from the review | X | ELABORATING: for non-diagonal marginals the joint-state ambiguity is not confined to the configuration algebra |
| Proposition BID; BIDUAL-REL | — | X | BORDERLINE: a reduction to an open question, not a decision |
| §6 realizability | readings LAW-σ, LAW-fa | X, P | ELABORATING |

**AW-3 (assumption-watch marker).** A record that restricts a slice, a reduction or a joint state
to normal hidden states should check whether the tensor product is B(H ⊗ K). There the vector
slice σ_ω exists for every state ω and is the unique positive map with the product property. The
case that is non-canonical is the joint state of two non-normal states. Its ambiguity already
occurs in the configuration algebra (CX-F), and for non-diagonal marginals it is not confined
there (CX-F′).

*Instances at the pins.*
- **M1 at `dac9ca3f`: the premise is stated, and VS refutes it.** "The slice in S9 needs FIN-V, or
  normal ω, outside (F-C\*)" (Verdict N1); the S9 row gives "ω normal, or C_V finite". AW-3 is NEW
  on this instance.
- **NN N5 at `ab830621`: an open item.** "With C_V countably infinite and ω non-normal the slice is
  not established" (M2). VS closes it; no premise is refuted there.
- **OPRES Remark D′ at `24702c1d`: a further instance.** Its hypotheses state that, with a diffuse
  factor H₁ present, "σ_ω would have to act on L^∞(H₁) ⊗̄ L^∞(H), which is not defined for
  non-normal ω". For the vector slice this is false:
  - VS gives σ_ω on B(L²(H₁) ⊗ L²(H)) for every ω;
  - by bimodularity σ_ω(b) commutes with L^∞(H₁) whenever b commutes with L^∞(H₁) ⊗ 1, so
    σ_ω(b) ∈ L^∞(H₁)′ = L^∞(H₁);
  - SL gives uniqueness among positive maps with PROD.

  This bears on OPRES U1′ (iii).
- **Not instances.** OPRES D step 4 ("Normality is used for the slice on the von Neumann tensor
  product") describes D's proof, not the slice's existence. OPRES U1′ (ii) names a different
  obstacle: a non-normal output visible marginal, which would need a state-space form of the
  Theorem C(b) bound.

*Cross-propagation (not settled here).* Lemma VS gives the vector slice B(K ⊗ L²(H, ν)) → B(K) for
every state of B(L²(H, ν)). Lemma CMP gives preservation of any configuration algebra 𝒜 ⊆ B(K)
that is maximal abelian and whose projections the append fixes. Whether this settles U1′ (iii) in
OPRES's own protocol class, with its Theorems B and C(b) on an infinite visible carrier, is not
checked here. U1′ (ii) is not addressed.

**Productivity test (`PLAN.md` §5).**
- *Stronger than the restatement:* the restatement is "RED holds for normal ω or finite C_V; the
  slice for infinite C_V and non-normal ω is not established". This record proves that the slice
  exists and is unique for every ω (VS, SL), and that the visible instrument is DIO-type for every
  append with VC (RED-M2).
- *(i) Decides or narrows:* M2 is decided in (F-H). In (F-S) it is decided on normal visible inputs
  and reduced to BIDUAL-REL on non-normal ones. AW-3 bears on OPRES U1′ (iii), which is not settled.
- *(ii) Exposes a hidden assumption:* AW-3.
- **Gem under `PLAN.md` §5. Output class ELABORATING, with one NEW marker.**

*Skepticism on the favourable branch.* The result extends the obstruction, so the question is
whether VC or PROD smuggles DIO in.
- Neither condition fixes E on ℓ^∞(C_V × Z) (circularity test, §2). The step from VC to DIO-type
  goes through Lemma CMP and the maximality of ℓ^∞(C_V), and RED-M2's proof needs both.
- Weaker hypotheses fail: dropping VC gives the Ad_W example, and dropping σ-D gives CX-1′ (§7).
- The same mechanism does not settle (F-S). There the relative commutant is taken in the bidual,
  where maximality is not available. The record reports that case as INCONCLUSIVE.
- Lemma SL does not remove every non-uniqueness. CX-F exhibits one, for joint states of two
  non-normal states. For diagonal marginals it lies in ℓ^∞(ℕ × ℕ), and for non-diagonal marginals
  it does not (CX-F′).

*Stop condition.* The record stops under the `PLAN.md` §8 condition "answered in both typings of
§3, or each remaining case reported INCONCLUSIVE with its missing ingredient". (F-H) is answered;
(F-S) is INCONCLUSIVE with BIDUAL-REL named, with its normal-input and slice-order results
established. A further node would need BIDUAL-REL, which is adjacent to
M1-b and outside this authorization. The fixed-point condition of `PLAN.md` §8 is not claimed to
be met.

## 9. ESTABLISHED, ASSUMED, MISSING

**ESTABLISHED** (this record, layer X, unreviewed):
- Lemma VS, Lemma SL, Corollary SL′, Lemma CMP and Lemma JU;
- Theorem RED-M2, Corollary IDLE-V and Theorem MIO-M2;
- CX-M, CX-F and CX-F′, each using a free ultrafilter (CX-F′ from the review);
- Proposition BID, as a reduction;
- the characterization of normal states by complete additivity of the configuration law (from M1
  NRM (a)), and the realizability readings of §6;
- the drop-one table (§7).

**ASSUMED:**
- (I): KIN-B, LIN, TB, and VC (the definition of an append); PROD (the definition of "ω
  appended") where stated;
- (N): DEC, DEF, A2, and σ-D at the total carrier, which NAT delivers (M1 §6);
- NAT: (N), a reading of T-SUB′ (ii) and (iii), not adopted;
- LAW-σ and LAW-fa: readings of LAW, neither adopted;
- CNT-V and NN-ω, as the scope of the question.

**MISSING:**
- **BIDUAL-REL** (§5): whether ℓ^∞(C_V)′ ∩ B(ℓ²(C_V))\*\* = ℓ^∞(C_V)\*\*. It is sufficient for (F-S)
  on non-normal visible inputs. It is adjacent to M1-b, which needs separate authorization, and it
  is not attempted.
- **OPRES U1′ (iii)** in OPRES's own formulation: AW-3 bears on it, through Remark D′'s
  diffuse-factor sentence, and it is not checked. U1′ (ii) is a different obstacle and is not
  addressed.
- **An infinite-C_V form of OPRES Theorem C(b)** (the diamond-norm bound): not claimed. DIO-type
  is proved here; no distance bound is.
- **Nativeness of the bijection in CX-M** (NN M4), and **NN M3** (nonlinear state assignments):
  unchanged.
- **M1-b**: out of scope, not walked.

No item here needs computation, and none was run.

## 10. What this record does not do

It edits no manuscript, Lean module, reviewed record, Issue or file of another track, and no path
in the A1 retirement ledger (`PLAN.md`, A1 ledger check). It adopts no premise, no reading of LAW
and no nativeness criterion. It does not treat any non-normal state as physically prepared. It
treats the A1 retirement as not landed, and it says nothing about encoded carriers. It proposes no
successor round.
