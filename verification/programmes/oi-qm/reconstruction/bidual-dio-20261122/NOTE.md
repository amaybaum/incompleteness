# BIDUAL-DIO: restrictions of the state-space typing (F-S) and DIO-type (research record)

**WIP / UNVERIFIED. Paper-only research. It awaits an independent non-author review.** This
record walks the nodes of `PLAN.md`, which was committed before it at `741b5816`. It runs no
computation. It edits no manuscript, Lean module, reviewed record or Issue. It adopts no premise,
changes no status and strengthens no manuscript or kernel theorem. No merge is authorized. Names
prefixed "BR" are BIDUAL-REL's at `dda8d67c`, "M2" NONDIO-M2's at `7102e6af`, "M1" NONDIO-M1's at
`dac9ca3f` and "NN" NATIVE-NONDIO's at `ab830621`. Names without a prefix are this record's.

**Labels.**
- **ESTABLISHED**: proved on paper here (layer X), or cited at its source's standing: (L) a
  literature theorem, (R) a corpus record, (M) a statement of `papers/Main.md`. "Established"
  means established within this record, not in the §A.46 sense.
- **ASSUMED**: a named premise.
- **MISSING**: a gap, stated with the node where the branch stopped.

**Notation.** As in BR: A = B(H_V), H_V = ℓ²(C_V), D = ℓ^∞(C_V), Δ_V: A → D the diagonal
conditional expectation, B = B(H_V ⊗ H_Z), H_Z = ℓ²(Z), A\*\* the bidual, D\*\* the σ-weak closure
of D in A\*\*, φ\*\* the normal extension of φ ∈ A\*. z_K ∈ A\*\* is the σ-weak limit of the
increasing finite diagonal projections P_{[0,n)} (the support of the compact operators); it is
central, lies in D\*\*, and z_K A\*\* ≅ B(H_V) (BR §3, Remarks). ν := ω|_{ℓ^∞(Z)} is the
configuration law of the hidden state ω. An *assignment* is a map ρ ↦ Ω_ρ from states of A to
states of B with PROD: Ω_ρ(a ⊗ c) = ρ(a)ω(c). It is *DIO-type in (F-S)* when, for every
instrument of M2's RED-M2 class, the output configuration law depends on ρ only through ρ|_D
(M2 `PLAN.md` §3).

**The two slice orders as maps into A\*\*.** σ_ω: B → A is M2's vector slice ("ω appended to ρ",
Ω_ρ = ρ∘σ_ω). For φ ∈ A\*, σ′_φ: B → B(H_Z) is the vector slice over the first factor
(M2 §5, extended linearly from states), and E′: B → A\*\* is defined by φ\*\*(E′(b)) := ω(σ′_φ(b))
("ρ appended to ω", Ω_ρ = ω∘σ′_ρ). For a central element z of A\*\* with 0 ≤ z ≤ 1, put

E_z := (1 − z)σ_ω + zE′.

## 0. Outcome

**For OI's own visible carrier: DIO-type is restored, by a premise OI states (proof).** The
Definition's finite-capacity clause makes C_V finite (`Main:42`, `Main:46`, Lemma 1). With C_V
finite every state of A is normal, and every assignment with PROD, affine or not, for every
hidden state ω, normal or not, is ρ ↦ ρ∘σ_ω and is DIO-type in (F-S) (Proposition FV). BIDUAL-REL
itself holds trivially there (A\*\* = A). Theorem NDIO needs C_V infinite (CNT-V), which is outside
the Definition. This restriction acts on the carrier, and through it on the visible states; it is
not a restriction of the assignment.

**On CNT-V (a mathematical extension outside the Definition), restriction by restriction:**

| Restriction | Family | Sufficient for DIO-type in (F-S)? | Follows from OI? |
|---|---|---|---|
| FIN-V | normal-state (carrier) | **yes**, every assignment with PROD (FV) | **yes**: `Main:46` (Lemma 1) |
| normal visible inputs | normal-state | **yes**, every assignment (M2 JU) | via FIN-V; on CNT-V only under the reading LAW-σ (not adopted) |
| normal hidden state ω | normal-state | **yes**, every assignment, affine or not (HN′, strengthening BR HN) | not on CNT-V: `Main:60` states DEC for normal states and probabilities, which is the scope of that statement, not a premise on every hidden prior; LAW-σ and A1 would give it, neither adopted |
| covariance under any group of visible unitaries (diagonal unitaries, configuration permutations, all of U(A)) | assignment (symmetry) | **no**: Theorem NDIO's assignment is covariant under all of U(A) (COV) | no statement in the corpus |
| hidden covariance under the stabilizer of ω, or covariance of the family ω ↦ Ω^ω | assignment (symmetry) | **no**: Theorem NDIO's assignment satisfies both (COV) | no statement in the corpus |
| invariance of ω under all permutations of Z | normal-state, through ω | the class is **empty** for Z infinite (PERM); for Z finite, ω is normal and HN′ applies | the finite-representative uniform prior (`Main:58`) has it; it has no infinite-Z analogue |
| covariance under visible dephasing (COV-Δ) | assignment (symmetry under a channel) | **yes** (Proposition DEPH); not implied by covariance under the diagonal unitaries | no statement in the corpus: additional assumption |
| a single global slice order (fixed scalar z) | assignment (slice-order selection) | **yes** (M2 §5; SEL) | no: OI takes the joint preparation as a datum (`Main:48`) and fixes no order; additional assumption |
| sector-wise slice-order selection, z central in A\*\* | assignment (slice-order selection) | **exactly when z ∈ D\*\***, for ω with ν vanishing on finite sets (Theorem SEL); Theorem NDIO is the case z = z_f ∉ D\*\* | no statement in the corpus |

**The exact condition and the missing premise.** For every assignment with PROD, affine or not,
on C_V = Z = ℕ, DIO-type in (F-S) is equivalent to **R-CFG**: the joint configuration law
Ω_ρ|_{ℓ^∞(C_V × Z)} depends on ρ only through ρ|_D (Proposition CFG, both directions proved).
R-CFG is DIO-type restated at the level of the joint state, so it is definitional, not a physical
restriction. Every sufficient restriction of the table implies it. **Missing premise:** a native
rule fixing the joint configuration law of a coherent non-normal visible input with an
independently prepared hidden state. OI states none: its preparations are configurations or laws
over them (LAW), under which no coherent non-normal visible input is native, and its DEC statement
(`Main:60`) is made for normal states.

**Mathematical existence and physical realizability (D6).**
- *Existence.* On CNT-V, a non-DIO affine assignment with PROD exists (BR Theorem NDIO; free
  ultrafilters and Krein–Milman). It is covariant under every visible unitary and under the
  stabilizer of ω, so symmetry does not exclude it.
- *Realizability.* Its behaviour needs four things at once: CNT-V, excluded by `Main:46`; a
  non-normal ω, excluded under LAW-σ and A1 and outside the scope of `Main:60`, admitted (diagonal)
  under LAW-fa; a coherent non-normal visible input, outside LAW in both readings and impossible
  under FIN-V; and an assignment violating R-CFG, which NAT does not deliver. No premise OI
  states delivers any instance of it.

**Productivity (`PLAN.md` §4): gem.** Sufficiency or insufficiency is decided for every restriction
of `PLAN.md` §5 not covered by the restatement, and two hidden assumptions are exposed (AW-5, §7).
Output class NEW for Theorem SEL, COV and Proposition CFG; ELABORATING for HN′, DEPH and PERM;
CONFIRMING for FV.

## 1. D0: corpus and literature

Searched: `papers/*.md`, `book/*.md`, `verification/` (all records) and `verification/lean*/`, for
the cardinality of C_V, normality or σ-additivity of hidden priors and preparations, joint
preparation, slice order, iterated or ultrafilter limits, non-normal or finitely additive states,
and covariance of a preparation or append.

| Topic | Location | What it states |
|---|---|---|
| finiteness of C_V | `Main:42` (Definition: "an observer V ⊊ S — a proper subsystem with finitely many distinguishable internal states"); `Main:46` (Lemma 1: "The finite-capacity clause of the observer definition makes the visible configuration space 𝒞_V finite"); `Main:60` ("only finite visible resolution is a theorem (Lemma 1 …)") | C_V finite, as a consequence of the Definition, independent of total finiteness (A1) |
| other observers | `Main:696` (observer covariance and nested observers) | each partition V ⊊ S is an observer in the sense of the Definition; no infinite visible carrier is introduced |
| joint preparation | `Main:48` (Lemma 2: "a joint preparation may already correlate the two sectors. The reduced law uses that preparation, or its corresponding conditional hidden law") | the joint state or law is a preparation datum; no rule builds it from the visible marginal |
| hidden prior | `Main:58` (a realization "carries its own fixed hidden prior μ_H"; the canonical measure is the uniform probability on the finite carrier, with the uniform conditional law on 𝒞_H) | the hidden prior is a datum; its permutation-invariant default is stated on finite representatives |
| independent adjoined factor (DEC) | `Main:60` ("a Hilbert space of any dimension with a normal state and a unitary or isometry, or a measurable space with a probability and a measurable map"); ledger item (ii), `Main:736` | DEC is stated for normal states and probability measures |
| total finiteness | `Main:736`, ledger item (ii) | an open hypothesis, not adopted |
| non-normal states, ultrafilters, slice order, covariance of an append | `papers/`, `book/`, Lean trees | **no hit**. In `verification/` they occur only in M1, M2 and BR |

*Literature.* No literature theorem is used beyond those BR and M2 cite (bidual facts F1–F4,
Takesaki Ch. III §2). The non-existence of a permutation-invariant finitely additive probability on
an infinite set (PERM) is classical and is proved here. No source is claimed for SEL, COV, CFG,
HN′ or DEPH; any novelty is relative to the corpus.

**Verdict D0.** The corpus fixes C_V finite (`Main:46`), treats the joint preparation as a datum
(`Main:48`), and states DEC for normal states (`Main:60`). It contains no covariance condition on
an append and no slice-order rule.

## 2. D1 (decisive): FIN-V

**Proposition FV (ESTABLISHED, X; (M) `Main:46`).** Let C_V be finite and Z a set of any
cardinality, and let ω be any state of B(H_Z), normal or not. Then:
- (i) every assignment with PROD, affine or not, is ρ ↦ ρ∘σ_ω;
- (ii) it is DIO-type in (F-S) for every instrument of the RED-M2 class;
- (iii) D′ ∩ A\*\* = D\*\*, so BIDUAL-REL holds.

*Proof.*
- A = M_{|C_V|}(ℂ) is finite-dimensional, so every state of A is given by a density matrix and is
  normal.
- (i) is M2 Lemma JU applied to each ρ.
- (ii) is M2 RED-M2 with E = σ_ω, which satisfies VC: the output configuration law is
  ρ(σ_ω(Φ_o\*(M_g ⊗ 1))) with σ_ω(Φ_o\*(M_g ⊗ 1)) ∈ D.
- (iii) A finite-dimensional C\*-algebra is its own bidual, so A\*\* = A and D\*\* = D, and D′ ∩ A = D
  because D is maximal abelian (M2 RED-M2 proof). ∎

**Source in OI.** FIN-V is `Main:46` (Lemma 1), derived there from the finite-capacity clause of
the Definition (`Main:42`). It does not use total finiteness (ledger item (ii)), so it is not
affected by the A1 retirement as recorded in `Main:60`. M1 records it as (N) (M1 `PLAN.md` §4),
and M2 `PLAN.md` §4 drops it as the scope of its question.

*Skepticism on the favourable branch.*
- *Is any OI object a visible carrier with infinitely many configurations?* D0 finds none.
  Nested observers (`Main:696`) are observers in the sense of the Definition. Infinite carriers in
  the corpus are hidden: the measurable hidden carrier of the §3.2 corollary (`Main:60`) and the uncountable
  lattice after A1 (NN M1). OPRES U1′ (ii), NN M2 and M2 pose CNT-V as a mathematical case and cite
  no OI object that realizes it.
- *Does FV need ω normal or Z finite?* No. JU uses only normality of ρ.
- *Does FV need affinity?* No. JU fixes the joint state for each ρ separately, so FV covers
  nonlinear assignments (NN M3) as well.
- *Is FV a restriction of the assignment?* No. It removes the states on which assignments differ.
  On CNT-V, the remaining nodes are needed.

**Verdict D1: SUFFICIENT; follows from OI** (`Main:46`), for every assignment with PROD and every
ω. Theorem NDIO does not survive it. Class CONFIRMING: the boundary was known to M1 and M2; what is
recorded here is that the boundary is a theorem of Main, and that it covers non-affine assignments.

## 3. D2: normal-state restrictions on CNT-V

**(a) Normal visible inputs (ESTABLISHED, X; M2 JU).** If ρ is normal, Ω_ρ = ρ∘σ_ω for every
assignment with PROD, so DIO-type holds on normal inputs.

*Source.* Through FIN-V (D1). On CNT-V, under the reading LAW-σ native inputs are normal; under
LAW-fa native inputs are diagonal and two of them with the same configuration law are equal, so no
native pair witnesses a failure (BR §5). Neither reading is adopted, and a domain restriction of
this kind does not make an assignment DIO-type on all inputs.

**Proposition HN′ (a normal hidden state fixes every assignment; ESTABLISHED, X).** Let ω be
normal and ρ any state of A. Exactly one state Ω of B has Ω(a ⊗ c) = ρ(a)ω(c), namely ρ∘σ_ω.
Hence every assignment with PROD, affine or not, is ρ ↦ ρ∘σ_ω, and is DIO-type in (F-S).

*Proof.* M2 Lemma JU with the two factors exchanged.
- ρ∘σ_ω qualifies (M2 Lemma VS).
- Let Ω qualify and ε > 0. Since ω is normal there is a finite-rank projection Q on H_Z with
  ω(1 − Q) ≤ ε. With P := 1 ⊗ Q, Ω(1 − P) = ω(1 − Q) ≤ ε, and Cauchy–Schwarz gives
  |Ω(b) − Ω(PbP)| ≤ 2‖b‖ε^{1/2}.
- PbP ∈ B(H_V ⊗ QH_Z) with QH_Z finite-dimensional, so PbP = Σ_{ij} c_{ij} ⊗ e_{ij} for matrix
  units e_{ij} of QH_Z, and Ω(PbP) = Σ_{ij} ρ(c_{ij})ω(e_{ij}) is fixed by PROD. Letting ε → 0
  fixes Ω(b).
- DIO-type then follows from RED-M2 with E = σ_ω. ∎

BR Proposition HN proves the conclusion for affine assignments through the map E. HN′ removes
affinity, and shows that for normal ω the two slice orders coincide: ω∘σ′_ρ = ρ∘σ_ω.

*Source.* Not on CNT-V. `Main:60` states DEC, the independent preparation of an adjoined factor,
for "a normal state" or "a probability"; a non-normal ω is outside the scope of that statement,
which does not assert that every hidden prior is normal. LAW-σ would give normality, and total
finiteness (ledger item (ii)) would give Z finite; neither is adopted.

**Verdict D2.** (a) SUFFICIENT; follows from OI through FIN-V only. (b) SUFFICIENT for every
assignment (HN′); an additional assumption on CNT-V.

## 4. D3: covariance

**Lemma BIM (bimodularity; ESTABLISHED, X).** σ_ω and E′ are positive, unital and satisfy PROD, and
for a, a′ ∈ A, b ∈ B and every unitary W of H_Z with ω∘Ad_W = ω (Ad_W(c) := WcW\*):
- σ_ω((a ⊗ 1)b(a′ ⊗ 1)) = aσ_ω(b)a′ and E′((a ⊗ 1)b(a′ ⊗ 1)) = aE′(b)a′;
- σ_ω(Ad_{1⊗W}(b)) = σ_ω(b) and E′(Ad_{1⊗W}(b)) = E′(b).

Hence, for every central z with 0 ≤ z ≤ 1, E_z is positive, unital, satisfies PROD and has the
same two properties.

*Proof.*
- σ_ω: M2 Lemma VS gives positivity, PROD and bimodularity. For W, the block of Ad_{1⊗W}(b) at
  (ξ, η) is Wb_{ξη}W\*, and ω(Wb_{ξη}W\*) = ω(b_{ξη}).
- E′ is well defined: for fixed b, φ ↦ ω(σ′_φ(b)) is linear and bounded on A\*, so it is an element
  of A\*\*. For b ≥ 0 and every state φ, φ\*\*(E′(b)) = ω(σ′_φ(b)) ≥ 0, and the normal extensions of
  the states of A are the normal states of A\*\*, so E′(b) ≥ 0. PROD: σ′_φ(a ⊗ c) = φ(a)c gives
  φ\*\*(E′(a ⊗ c)) = φ(a)ω(c).
- Bimodularity of E′: write b^{(kl)} := θ′_k\* b θ′_l ∈ A for k, l ∈ H_Z, θ′_k ξ := ξ ⊗ k. Then
  ((a ⊗ 1)b(a′ ⊗ 1))^{(kl)} = a b^{(kl)} a′, so
  φ\*\*(E′((a ⊗ 1)b(a′ ⊗ 1))) = ω(σ′_{φ_{a,a′}}(b)) with φ_{a,a′}(x) := φ(axa′). Both
  y ↦ φ_{a,a′}\*\*(y) and y ↦ φ\*\*(aya′) are normal on A\*\* and agree on A, so this equals
  φ\*\*(aE′(b)a′), for every φ.
- W-invariance of E′: (Ad_{1⊗W}(b))^{(kl)} = b^{(W\*k, W\*l)}, so σ′_φ(Ad_{1⊗W}(b)) = Wσ′_φ(b)W\*,
  and ω∘Ad_W = ω.
- E_z: z is central, so (1 − z)σ_ω(b) and zE′(b) are products of commuting positive elements for
  b ≥ 0. PROD and both properties pass to the convex combination because z commutes with a and
  a′. ∎

**Lemma ID (BR's glued map is E_{z_f}; ESTABLISHED, X).** Let f, ω and E be those of BR
Theorem NDIO (Construction GLU with Ω = ω∘σ′_f). Then E = E_{z_f}.

*Proof.* The term (1 − z_f)σ_ω is common. For the sector term, both π̃_f^{-1}(E_Ω(b)) and
z_f E′(b) lie in z_f A\*\* ≅ B(H_f), and for x, y ∈ A:
- ⟨π_f(x)ξ|E_Ω(b)|π_f(y)ξ⟩ = Ω((x\* ⊗ 1)b(y ⊗ 1)) (BR, Construction GLU);
- ⟨π_f(x)ξ|π̃_f(E′(b))|π_f(y)ξ⟩ = f\*\*(x\*E′(b)y) = f\*\*(E′((x\* ⊗ 1)b(y ⊗ 1)))
  = ω(σ′_f((x\* ⊗ 1)b(y ⊗ 1))) = Ω((x\* ⊗ 1)b(y ⊗ 1)), by F2 and Lemma BIM.

The vectors π_f(x)ξ are dense in H_f, so the two bounded operators agree. ∎

**Proposition COV (covariance does not restore DIO-type; ESTABLISHED, X).** For every central z
with 0 ≤ z ≤ 1, the assignment Ω^{ω}_ρ := ρ\*\*∘E_z satisfies:
- (V) *visible covariance under all of U(A):* Ω_{ρ_u} = Ω_ρ∘Ad_{u⊗1}^{-1} for every unitary u ∈ A,
  where ρ_u := ρ∘Ad_u^{-1};
- (H) *hidden covariance under the stabilizer:* Ω_ρ∘Ad_{1⊗W} = Ω_ρ for every unitary W with
  ω∘Ad_W = ω;
- (F) *covariance of the family:* Ω^{ω∘Ad_W^{-1}}_{ρ_u} = Ω^{ω}_ρ∘Ad_{u⊗W}^{-1} for all unitaries
  u ∈ A and W of H_Z.

In particular, BR Theorem NDIO's assignment, which is E_{z_f} (Lemma ID), satisfies (V), (H) and
(F) and is not DIO-type. Covariance under any group of visible unitaries, and in particular under
the diagonal unitaries U(D) or the configuration permutations of C_V, is therefore not sufficient
for DIO-type in (F-S).

*Proof.*
- (V): ρ_u\*\*(y) = ρ\*\*(u\*yu) for y ∈ A\*\*, since both sides are normal and agree on A. So
  Ω_{ρ_u}(b) = ρ\*\*(u\*E_z(b)u) = ρ\*\*(E_z((u\* ⊗ 1)b(u ⊗ 1))) by Lemma BIM.
- (H) is the W-invariance of Lemma BIM.
- (F): z does not depend on ω. Lemma VS gives σ_{ω∘Ad_W^{-1}}(Ad_{1⊗W}(b)) = σ_ω(b), from the
  block computation of Lemma BIM, and the same computation for σ′ gives the identity for E′.
  Combine with (V). ∎

*Mechanism.* The selection in Theorem NDIO is made by a central projection z_f of A\*\*, and every
Ad_u, u ∈ U(A), fixes the centre pointwise. A covariance condition under visible unitaries
therefore cannot see a sector-wise selection.

*Remark (group covariance and dephasing).* For normal ρ, every E_z gives ρ∘σ_ω (HN′'s mirror,
M2 JU), so covariance and compatibility with Δ_V agree there. For non-normal ρ they separate:
E_{z_f} is U(D)-covariant, while f and f∘Δ_V receive joint states with different configuration
laws (BR Theorem NDIO). Covariance under each diagonal unitary does not yield covariance under
Δ_V, which is not an automorphism.

**Proposition PERM (full hidden permutation invariance is empty; ESTABLISHED, X).** Let Z be
infinite. No state ω of B(H_Z) satisfies ω∘Ad_{W_π} = ω for every permutation π of Z, with
W_π|z⟩ = |π(z)⟩.

*Proof.* ν = ω|_{ℓ^∞(Z)} would be a finitely additive probability on the subsets of Z with
ν(π(X)) = ν(X). For Z = ℕ let A_j be the residues j mod 3, j = 0, 1, 2. Any two subsets X, Y of ℕ
that are infinite with infinite complements are related by a permutation of ℕ. So
ν(A_0) = ν(A_1) = ν(A_2) = ν(A_0 ∪ A_1) = 2ν(A_0), hence ν(A_0) = 0 and ν(ℕ) = 0, a contradiction.
For uncountable Z the same argument applies to a partition into three sets of cardinality |Z|. ∎

For finite Z, the uniform state is invariant and normal, and HN′ applies. Invariance of ω under all
permutations therefore restores DIO-type only by forcing Z finite, which is a normal-state
restriction. The permutation-invariant uniform prior of `Main:58` is stated on finite
representatives; PERM shows that it has no infinite-Z analogue.

**Proposition DEPH (covariance under visible dephasing is sufficient; ESTABLISHED, X).** Let
Δ_V ⊗ id: B → B be the normal map b ↦ Σ_v (P_v ⊗ 1)b(P_v ⊗ 1) (σ-weak sum). Say that an
assignment satisfies **COV-Δ** if Ω_{ρ∘Δ_V} = Ω_ρ∘(Δ_V ⊗ id) for every state ρ. Then:
- (i) COV-Δ is compatible with PROD, and both slice orders satisfy it, for every ω;
- (ii) COV-Δ implies R-CFG (§6), hence DIO-type in (F-S), for every assignment with PROD, affine
  or not;
- (iii) E_z satisfies COV-Δ whenever z ∈ D\*\*; E_{z_f} does not.

*Proof.*
- (i) (Δ_V ⊗ id)(a ⊗ c) = Δ_V(a) ⊗ c, so both sides of COV-Δ have marginals ρ∘Δ_V and ω. For σ_ω,
  the (v, v′) block of (Δ_V ⊗ id)(b) is δ_{vv′}b_{vv}, so σ_ω∘(Δ_V ⊗ id) = Δ_V∘σ_ω. For E′,
  ((Δ_V ⊗ id)(b))^{(kl)} = Δ_V(b^{(kl)}), so σ′_φ∘(Δ_V ⊗ id) = σ′_{φ∘Δ_V}, and
  E′∘(Δ_V ⊗ id) = Δ_V\*\*∘E′ by BR F3.
- (ii) Δ_V ⊗ id fixes ℓ^∞(C_V × Z) pointwise. If ρ|_D = ρ′|_D then ρ∘Δ_V = ρ′∘Δ_V, so
  Ω_ρ(M_h) = Ω_{ρ∘Δ_V}(M_h) = Ω_{ρ′∘Δ_V}(M_h) = Ω_{ρ′}(M_h). This is R-CFG, and Proposition CFG
  (⇐) gives DIO-type.
- (iii) By (i), Ω_{ρ∘Δ_V}(b) = ρ\*\*(Δ_V\*\*(E_z(b))) and Ω_ρ((Δ_V ⊗ id)b) =
  ρ\*\*((1 − z)Δ_V\*\*(σ_ω(b)) + zΔ_V\*\*(E′(b))). Δ_V\*\* is D\*\*-bimodular (it is D-bimodular, and
  both sides are separately σ-weakly continuous), so the two agree when z ∈ D\*\*. E_{z_f} is not
  DIO-type (BR Theorem NDIO), so by (ii) it fails COV-Δ. ∎

*Source.* No statement in the corpus requires a preparation to commute with dephasing (D0). COV-Δ
is an additional assumption, and through (ii) it is at least as strong as R-CFG, which is
DIO-type restated (§6).

**Verdict D3.**
- (a) Visible covariance under any group of unitaries of A: **INSUFFICIENT** (counterexample:
  BR Theorem NDIO, by COV). Not in the corpus.
- (b) Hidden covariance under the stabilizer of ω, and covariance of the family:
  **INSUFFICIENT** (the same counterexample). Not in the corpus. Invariance of ω under all
  permutations: **empty** for Z infinite (PERM); for Z finite it reduces to HN′.
- (c) COV-Δ: **SUFFICIENT** (DEPH), for every assignment. An additional assumption.

## 5. D4: slice-order selection

**(a) A single global slice order.** For a fixed scalar c ∈ [0, 1], E_c = (1 − c)σ_ω + cE′. The
cases c = 0 and c = 1 are the two orders of M2 §5, and each is DIO-type there; c ∈ [0, 1] is the
case z = c1 ∈ D\*\* of Theorem SEL. **SUFFICIENT (ESTABLISHED, X; R M2 §5).**

*Source.* OI takes the joint state or law as a preparation datum (`Main:48`) and contains no rule
that builds it from the visible input by a fixed order (D0). The two orders are two extensions of
PROD to non-normal inputs, which agree on normal inputs (M2 JU). A single global order is an
additional assumption, and which order it fixes does not matter for DIO-type.

**(b) Sector-wise selection.** The class SO is {E_z : z central in A\*\*, 0 ≤ z ≤ 1}. It contains
the two orders (z = 0, 1) and Theorem NDIO (z = z_f, Lemma ID).

**Theorem SEL (ESTABLISHED, X).** Let C_V = Z = ℕ.
- (i) If z ∈ D\*\*, then E_z is DIO-type in (F-S), for every ω and every instrument of the RED-M2
  class.
- (ii) Let ν vanish on finite sets (ω(P_z) = 0 for every z ∈ Z; Theorem NDIO's ω is such). Then for
  S := {(v, z) : v < z},

  E_z(M_{1_S}) = 1 − z(1 − z_K).

  Consequently E_z is DIO-type for the instrument of BR Theorem NDIO if and only if z ∈ D\*\*, and
  then for the whole RED-M2 class.

*Proof.*
- (i) For h ∈ ℓ^∞(C_V × Z), σ_ω(M_h) ∈ D (M2 RED-M2 (iii)). The order E′ is DIO-type (M2 §5), so
  E′(M_h) ∈ D\*\* by BR Proposition BID′. D\*\* is an algebra, so E_z(M_h) = (1 − z)σ_ω(M_h) +
  zE′(M_h) ∈ D\*\*, and ρ\*\* on D\*\* is fixed by ρ|_D (M2 Proposition BID). Every output
  configuration law of the class is of this form, M_h = Φ_o\*(M_g ⊗ 1) (M1 DET-at).
- (ii), the first order: σ_ω(M_{1_S}) is multiplication by v ↦ ν({z : z > v}) = 1, since the
  complement {z ≤ v} is finite.
- (ii), the second order: for a state φ of A, φ\*\*(E′(M_{1_S})) = ω(σ′_φ(M_{1_S})), and σ′_φ(M_{1_S})
  is multiplication by g_φ(z) := φ(P_{[0,z)}) (M2 §5). g_φ increases to
  L := sup_n φ(P_{[0,n)}) = φ\*\*(z_K), by normality of φ\*\*. Given ε > 0, |g_φ − L| ≤ ε off a finite
  set, and ν vanishes on finite sets, so |ν(g_φ) − L| ≤ ε. Hence φ\*\*(E′(M_{1_S})) = φ\*\*(z_K) for
  every state φ, and E′(M_{1_S}) = z_K.
- So E_z(M_{1_S}) = (1 − z) + z z_K.
- *Only if.* If E_z is DIO-type for this instrument, its output law ρ ↦ ρ\*\*(E_z(M_{1_S})) depends
  only on ρ|_D (BR Theorem NDIO: Φ\*(M_{1_{A_e}} ⊗ 1) = M_{1_S}), so E_z(M_{1_S}) ∈ D\*\* by
  BR Proposition BID′, and z(1 − z_K) ∈ D\*\*. z z_K is central in z_K A\*\* ≅ B(H_V), a factor, so
  z z_K = c z_K for a scalar c, and c z_K ∈ D\*\*. Hence z = z(1 − z_K) + z z_K ∈ D\*\*.
- *If* is (i). ∎

*Checks.*
- For z = z_f: f\*\*(z_f) = 1 and f\*\*(z_K) = 0 give p(f) = 0, and ψ\*\*(z_f) = 0 (BR Lemma DSJ)
  gives p(ψ) = 1, as in BR Theorem NDIO. z_f ∉ D\*\*, since otherwise ψ\*\*(z_f) = f\*\*(z_f).
- z_K and 1 − z_K are central and lie in D\*\*, so E_{z_K} and E_{1−z_K} are DIO-type. On
  configuration observables E_{z_K} agrees with σ_ω: for every state φ, x ↦ φ\*\*(z_K x) is the
  normal extension of the normal part of φ, on which the two orders agree (M2 JU).
- For normal ω every E_z equals σ_ω (HN′), and SO collapses to one assignment.

*Source.* No statement in the corpus selects a slice order, globally or sector by sector (D0).
Sector-wise selection with z ∉ D\*\* is a mathematical construction, as BR §5 records for Theorem
NDIO.

**Verdict D4.** (a) A single global slice order: **SUFFICIENT**, an additional assumption. (b)
Sector-wise selection: DIO-type **exactly when z ∈ D\*\*** (for ω with ν vanishing on finite sets);
sufficient for every ω when z ∈ D\*\*. Not in the corpus. **MISSING (not needed):** whether every
central z ∈ D\*\* with 0 ≤ z ≤ 1 is of the form c_1 z_K + c_2(1 − z_K).

## 6. D5: the exact condition

**R-CFG.** The joint configuration law Ω_ρ|_{ℓ^∞(C_V × Z)} depends on ρ only through ρ|_D.
Equivalently, Ω_ρ and Ω_{ρ∘Δ_V} agree on ℓ^∞(C_V × Z) for every state ρ.

**Proposition CFG (ESTABLISHED, X; both directions, §A.34).** Let ρ ↦ Ω_ρ be any assignment with
PROD, affine or not.
- (⇐) If R-CFG holds, the assignment is DIO-type in (F-S) for every instrument of the RED-M2
  class, for C_V, Z, C_V′, Z′ of any cardinality.
- (⇒) Let C_V = Z = C_V′ = Z′ = ℕ. If the assignment is DIO-type for the configuration-bijection
  instruments of the class (single-outcome branches Φ\*(b) = U_F\*bU_F with F a bijection of
  ℕ × ℕ), then R-CFG holds.

*Proof.*
- The equivalence of the two forms: ρ|_D = ρ′|_D if and only if ρ∘Δ_V = ρ′∘Δ_V, and ρ and ρ∘Δ_V
  agree on D.
- (⇐) Every outcome probability and output configuration law of the class is Ω_ρ(M_h) with
  M_h = Φ_o\*(M_g ⊗ 1) ∈ ℓ^∞(C_V × Z) (M1 DET-at).
- (⇒) Fix S ⊆ ℕ × ℕ.
  - If S is finite, M_{1_S} = Σ_{(v,z)∈S} P_v ⊗ P_z and Ω_ρ(M_{1_S}) = Σ_S ρ(P_v)ω(P_z) by PROD.
    If S is cofinite, use 1 − 1_S.
  - If S and its complement are infinite, choose, as in BR Theorem NDIO, a bijection F with
    F(S) = A_e × ℕ and F(complement) = (ℕ ∖ A_e) × ℕ, A_e the even numbers. Then
    Φ\*(M_{1_{A_e}} ⊗ 1) = M_{1_S}, and DIO-type for this instrument says that Ω_ρ(M_{1_S}) depends
    only on ρ|_D.
  - Real h ∈ ℓ^∞(ℕ × ℕ) is a uniform limit of finite real combinations of indicators, and
    |Ω_ρ(M_h) − Ω_ρ(M_{h′})| ≤ ‖h − h′‖_∞. ∎

For an affine assignment, R-CFG is E(ℓ^∞(C_V × Z)) ⊆ D\*\* (BR Proposition BID′).

*Circularity.* R-CFG is DIO-type restated at the level of the joint state: it is equivalent to
the conclusion by Proposition CFG and is not offered as a physical restriction. Every sufficient
restriction of D1–D4 implies it: FV, D2 (a) and HN′ fix Ω_ρ = ρ∘σ_ω where they apply; DEPH (ii)
proves it; SEL (i) gives E_z(ℓ^∞(C_V × Z)) ⊆ D\*\*. Any restriction that excludes Theorem NDIO on
CNT-V must imply R-CFG on the coherent non-normal inputs.

**Does OI supply R-CFG?**
- On normal inputs it holds for every assignment (M2 JU).
- On native inputs it is vacuous: under LAW-fa native inputs are diagonal, and two with the same
  configuration law are equal; under LAW-σ they are normal.
- On coherent non-normal inputs OI states nothing. Such inputs are outside LAW in both readings
  (M2 §6, BR §5). The joint state is a preparation datum (`Main:48`), and DEC is stated for normal
  states (`Main:60`). NAT concerns transitions, not the append of a hidden prior to a visible input.

**Missing premise (precisely).** A rule, native to OI, that fixes the joint configuration law of a
coherent non-normal visible input ρ together with an independently prepared hidden state ω as a
function of (ρ|_D, ω), that is, R-CFG on the non-normal coherent inputs of CNT-V. Under FIN-V
(`Main:46`) the premise is not needed.

**Verdict D5.** DIO-type in (F-S) is **equivalent to R-CFG** (proof, both directions). OI supplies
R-CFG through FIN-V; on CNT-V it is the missing premise named above.

## 7. D6: existence and realizability; classification

**What Theorem NDIO's non-DIO behaviour needs, and where each item stands.**

| Item | Needed by | Under OI's stated premises | LAW-σ | LAW-fa |
|---|---|---|---|---|
| C_V infinite (CNT-V) | BR Theorem REL and Theorem NDIO; FV | excluded by `Main:46` | — | — |
| ω non-normal, ν vanishing on finite sets | HN′; SEL (ii) | outside the scope of `Main:60` (DEC for normal states); total finiteness, not adopted, excludes it | excluded | admitted (diagonal) |
| a coherent non-normal visible input f | M2 JU | not native; impossible under FIN-V | excluded | excluded |
| an assignment violating R-CFG (z ∉ D\*\* in SO) | CFG; SEL | not delivered by NAT; not excluded by any covariance under visible unitaries (COV) | — | — |
| choice principles (free ultrafilters, Krein–Milman) | BR Lemma PUR, Theorem NDIO | — | — | — |

**Mathematical existence.** On CNT-V, a non-DIO affine assignment with PROD exists, and it is
covariant under U(A), under the stabilizer of ω and as a family (COV). **Physical
realizability.** No premise OI states delivers an instance: CNT-V alone is excluded by `Main:46`,
and on CNT-V no native pair of inputs witnesses the failure under either reading of LAW (BR §5).
Whether non-σ-additive hidden laws are physical is not decided here.

**Classification (§A.31).**

| Item | Layer | Class |
|---|---|---|
| Proposition FV | X; (M) `Main:46` | CONFIRMING: the boundary is a theorem of Main; covers non-affine assignments |
| D2 (a) | X; R M2 JU | CONFIRMING |
| Proposition HN′ | X | ELABORATING: BR HN without affinity; the two orders coincide for normal ω |
| Lemma BIM, Lemma ID, Proposition COV | X | NEW: covariance under visible unitaries and hidden stabilizers holds for every sector-wise selection, so it does not restore DIO-type |
| Proposition PERM | X (classical) | ELABORATING: full hidden permutation invariance is empty on infinite Z |
| Proposition DEPH | X | ELABORATING: dephasing covariance is sufficient and is not implied by group covariance |
| Theorem SEL | X | NEW: exact condition z ∈ D\*\* for sector-wise selection |
| Proposition CFG | X | NEW: DIO-type in (F-S) is equivalent to R-CFG, for every assignment |
| D6 table | X, M | ELABORATING |

**AW-5 (assumption-watch marker).**
- A covariance condition under a group of visible unitaries constrains an assignment into A\*\*
  only modulo the centre of A\*\*, since Ad_u fixes the centre pointwise. A record that argues
  from symmetry to a property of an assignment on non-normal inputs should check whether a
  central sector selection satisfies the symmetry and violates the property (COV).
- On non-normal states, covariance under the diagonal unitaries does not give compatibility with
  the dephasing Δ_V (COV, Remark). An argument that passes from one to the other uses normality.
- The restriction that excludes Theorem NDIO for OI's own observers is FIN-V (`Main:46`), a carrier
  restriction. On CNT-V the minimal assignment restriction is R-CFG, which is the conclusion
  restated (CFG).

**Productivity test (`PLAN.md` §4).**
- *Stronger than the restatement:* the restatement covers normal ω for affine assignments, normal
  inputs and each slice order. This record adds FV (every assignment, any ω, from `Main:46`), HN′
  (non-affine), COV (covariance insufficient, with the mechanism), PERM, DEPH, SEL (exact condition)
  and CFG (exact equivalence).
- *(i) Decides:* every restriction of `PLAN.md` §5 has a proof or a counterexample (table in §0).
- *(ii) Exposes hidden assumptions:* AW-5.
- **Gem. Output class NEW.**

*Skepticism on the favourable branches.*
- FV: tested against nested observers and infinite hidden carriers (§2); it uses only normality of
  the visible input, which finite dimension gives.
- COV: the counterexample is BR's own construction, identified with E_{z_f} by an explicit
  matrix-element computation (Lemma ID); covariance is checked on all of U(A), not only on U(D).
- SEL (ii): E′(M_{1_S}) = z_K is checked against every state through its normal extension, and the
  identity reproduces both values of BR Theorem NDIO.
- CFG (⇒) uses only bijection instruments inside the RED-M2 class and PROD for finite sets.

## 8. ESTABLISHED, ASSUMED, MISSING

**ESTABLISHED** (this record, layer X, unreviewed):
- Proposition FV, with FIN-V cited at `Main:46`;
- Proposition HN′;
- Lemmas BIM and ID, Proposition COV, Proposition PERM, Proposition DEPH;
- Theorem SEL;
- Proposition CFG, both directions.

**ASSUMED:**
- (I): KIN-B, KIN-𝒟, LIN, TB, PROD, the (F-S) typing; affinity only where stated (SEL, Lemma ID);
- (N): DEC (through PROD), σ-D (the instrument class);
- NAT, LAW-σ, LAW-fa: named, not adopted;
- (L): BR F1–F4.

**MISSING:**
- on CNT-V, a native rule fixing the joint configuration law of a coherent non-normal visible input
  with an independently prepared hidden state (R-CFG on those inputs), §6;
- whether every central z ∈ D\*\* with 0 ≤ z ≤ 1 is a combination of z_K and 1 − z_K (not needed);
- assignments with PROD outside SO and not satisfying COV-Δ: covered by CFG, not classified
  further;
- NN M4 (nativeness), M1-b, OPRES U1′: unchanged.

**Stop condition (`PLAN.md` §7).** Every restriction of `PLAN.md` §5 has a proof, a counterexample
or a precisely identified missing premise. There is no successor round.

## 9. What this record does not do

It edits no manuscript, Lean module, reviewed record, Issue or file of another track, and no path
in the A1 retirement ledger (`PLAN.md`, A1 ledger check). BR's branch is unchanged. It adopts no
premise, no reading of LAW, no covariance condition and no slice-order rule. It treats no
non-normal state as physically prepared, and it does not assume that infinite state spaces produce
quantum behaviour. It runs no computation.
