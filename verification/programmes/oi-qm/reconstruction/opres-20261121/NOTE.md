# OPRES: necessary resources for non-monomial transformations (research note)

**WIP / UNVERIFIED. Paper research only.** Revision r2 answers the independent review of
`35f0aa8a` (#1511 c.7066342291, verdict REVISE). r3 answers the narrow review of `2138732b`
(c.7066421069). r3 has not been re-reviewed. This note walks the
nodes of `PLAN.md`, which was committed before the derivation at `1f926939`. It adopts no premise
or criterion, edits no manuscript or reviewed record, runs no computation and changes no status.
Physical source remains NOT PASSED.

Tracking: Issue #1509; draft PR #1511 (stacked on #1508 at `df520f3b`). Corpus citations are
against `main` at `df6da1c6`. Layers: X exact algebra on paper; P paper argument; K kernel theorem
on `main`, cited and not duplicated.

## 0. Outcome and the three questions

**Outcome (PLAN §4), reported per scope.** The note reports a scoped OBSTRUCTION with two
INCONCLUSIVE extensions. PLAN §4 asks for exactly one outcome; it is applied here to each scope
separately.

- **Representational scope** (the Born form on the configuration basis): **OBSTRUCTION.**
  - Theorem C proves that every protocol realizing a non-monomial unitary transformation, exactly
    or within an explicit distance, contains two elements, possibly the same one:
    - an operation that **creates coherence**: it is not MIO-type, so it maps some diagonal input
      to a non-diagonal output;
    - an operation that **detects coherence**: it is not DIO-type, so the diagonal of its output
      depends on an off-diagonal entry of its input.
  - Control, feedforward, configuration readout, randomness, size and depth cannot replace either
    element.
  - The bound holds on countable carriers. On measurable carriers it holds for the detection half
    in two cases, both for a **nonsingular** bijection with C_V finite:
    - Proposition D, for a normal hidden state;
    - Remark D′, which is Proposition D's setting with the normality of ω dropped. It allows a
      single, possibly non-normal, hidden state ω. When ω is appended, the coexisting algebra is
      ℓ^∞ of a countable set, so no diffuse hidden factor is present. Every appended state after
      it is normal.

    Singular bijections are covered by neither and remain pending (Conjecture D″, which is
    independent of D′).
  - The pair is tight. One-bit teleportation (§4, CC-1) realizes Hadamard exactly with one creator
    (a |+⟩ ancilla) and one detector (a destructive ⟨±| readout). Everything else in it is native.
- **Native status**, (N) as algebra and (I) on KIN, conditional on R-READ: OI's stated
  operations supply neither element (§5).
- **Operational scope** (record laws): **no non-classical resource is shown to be necessary.** The
  necessary operational resources established are all classical. D-W meets exact laws classically,
  in sketch.
- **INCONCLUSIVE.**
  - **U2** (physical): can OI's ontology host a coherence detector and a coherence source?
  - **U1′** (narrow): measurable carriers with a singular bijection, a non-normal hidden state
    with C_V infinite, or several non-normal hidden states. The cases are listed in §6.

**Established.**
- Lemma C; Theorems A′, B and C; Proposition D; Remark D′ (pending review). All are layer X.
- Countercontrol CC-1 (X).
- The route classification (X and P).
- §5's native-membership check (P), with kernel citations at their finite scope.

**Assumed.**
- **KIN**, the Born-form representation on configurations (decision 4). It gives "coherence" and
  "non-monomial" their meaning.
- Countable carriers for A′, B and C. For Proposition D: a nonsingular measurable bijection on a
  standard measure space, a normal hidden state and C_V finite. For Remark D′: the same premises
  with normality dropped. That means nonsingularity, C_V finite, exactly one possibly non-normal
  hidden state, and the algebraic lift of that state. When it is appended, the coexisting algebra
  is ℓ^∞ of a countable set, with no diffuse hidden factor present. Every append after it is
  normal.
- For B and C, fixed coherent resource states (imported).
- **R-READ** (an Assumed reading of READ, #1501): every native readout effect lies in the
  configuration algebra (ℓ^∞ or L^∞).
- For the operational results: EP:77, EP:79 and EP:97; (xiv) beyond its Bell scope
  (Proposition U); H1–H5 (BQ1); and D-W's sketch status.

**Missing.** The earliest unsupported step is a **physical mechanism**, of two kinds:
- a native coherence-detecting operation: one whose Heisenberg dual takes a configuration effect
  outside the configuration algebra;
- a native coherence source, or coherent input.

A non-monomial step (FLOW) is one possible route, and it supplies both. It is not necessary as such.

## 1. Literature (searched first)

| Topic | Source | Relation |
|---|---|---|
| Coherence resource theory | T. Baumgratz, M. Cramer, M. B. Plenio, PRL 113, 140401 (2014); A. Winter, D. Yang, PRL 116, 120404 (2016); review: A. Streltsov, G. Adesso, M. B. Plenio, Rev. Mod. Phys. 89, 041003 (2017) | Theorem A′ is the native-class instance of "free operations create no coherence"; 𝒩 lies in SIO (monomial Kraus) |
| PIO, and MIO ⊋ IO | E. Chitambar, G. Gour, PRL 117, 030401 (2016); PRA 94, 052336 (2016) | MIO contains operations whose Kraus operators are not all CM; used in §3 to show the creator condition is strictly sharper |
| Speakable and unspeakable coherence | I. Marvian, R. W. Spekkens, PRA 94, 052324 (2016) | the basis is fixed physically (configurations) |
| Creating and detecting coherence | T. Theurer, D. Egloff, L. Zhang, M. B. Plenio, PRL 122, 190405 (2019), arXiv:1806.07332; follow-up arXiv:2102.04863 | Direction: CM-decomposable ⇒ IO ⊆ MIO, and RM-decomposable ⇒ DIO. So **leaving MIO implies a non-CM element**, and **leaving DIO implies a non-RM element**. The converse fails for MIO, since MIO ⊋ IO. Theorem C is stated with MIO and DIO. Its mathematics is standard after Theurer et al.; its novelty is relative to the corpus |
| Unitaries from IO plus coherent resources | K. Ben Dana, M. García Díaz, M. Mejatty, A. Winter, PRA 95, 062327 (2017) | IO plus a maximally coherent resource implements arbitrary unitaries. No conflict with B: IO Kraus operators may be non-RM and detect coherence, whereas 𝒩⁺ lies inside DIO (§3, B Scope) |
| Gate teleportation; MBQC | X. Zhou, D. W. Leung, I. L. Chuang, PRA 62, 052316 (2000); R. Raussendorf, H. J. Briegel, PRL 86, 5188 (2001) | CC-1 is one-bit teleportation |
| Classical simulability despite coherence | D. Gottesman, arXiv:quant-ph/9807006 (1998); S. Aaronson, D. Gottesman, PRA 70, 052328 (2004) | the operational layer (§6): coherent dynamics can still be efficiently simulable, so representational and operational necessity differ |
| Norms | M. A. Nielsen, I. L. Chuang, *Quantum Computation and Quantum Information* (2000), §9.2 | trace and diamond norms |

**Corpus.**
- `Main:328` and `:338` (diagonal preservation; the measurable-hidden-carrier corollary).
- `substratumClass_monomial` (`OIBridge/CoherentContinuumSource.lean`:212, K) and
  `gateFlow_not_monomial` (same file, :74, K).
- `substratumGen_not_control` (`StructuralClosure.lean`:330, K) and
  `substratumTheory_not_layerFlowExecutable` (`LiftAudit.lean`:200, K). Both are finite-carrier,
  Kraus-sum, exact no-gos.
- `preservesDiag_conjChannel_of_colMonomial` (`SubstantiveCensus.lean`:654, K) and
  `preservesDiag_sum` (`DiagonalTheory.lean`:84, K). These carry `Fintype`/`Finset`, so their use
  here for countable carriers and countable Kraus families is X, not K.

## 2. Definitions (N1 setup)

Configuration spaces are countable unless stated otherwise. Δ is the conditional expectation onto
the configuration (diagonal) algebra, and (a) fixes the configuration basis. For a bounded
K : ℓ²(X) → ℓ²(Y):
- **CM**: each column K|x⟩ has at most one nonzero entry.
- **RM**: each row ⟨y|K has at most one nonzero entry, equivalently the columns have pairwise
  disjoint supports.
- **Monomial**: both CM and RM.

For a CP, trace-nonincreasing map Φ:
- **Non-creating (MIO-type)** iff Φ∘Δ = Δ∘Φ∘Δ, that is, diagonal inputs give diagonal outputs. Φ
  **creates coherence** iff it is not MIO-type.
- **Non-detecting (DIO-type)** iff Δ∘Φ = Δ∘Φ∘Δ, that is, the output diagonal depends on the input
  only through its diagonal. In the Heisenberg picture: Φ* maps the configuration algebra into the
  configuration algebra. Φ **detects coherence** iff it is not DIO-type.
- **Decomposability.** CM-decomposable implies MIO-type, and RM-decomposable implies DIO-type (for
  RM K, ⟨y|KρK†|y⟩ = |K_{yx}|²ρ_{xx} for the unique x). The first implication is strict
  (MIO ⊋ IO); whether the second is strict is not settled here.

**Classes.**
- **𝒩** consists of:
  - (n1) permutation unitaries of configuration bijections, and diagonal phases;
  - (n2) appending configuration states, or diagonal mixtures of them;
  - (n3) configuration-basis Lüders measurement of any subsystem;
  - (n4) classical feedforward on records;
  - (n5) discard;
  - (n6) postselection on records.

  It allows any finite depth and any countable size.
- **𝒩⁺** is 𝒩 plus (n2⁺): appending a fixed density operator ω of any coherence, the same for every
  input.

## 3. Results

**Lemma C (closure; (N) as algebra; X).**
- CM, RM, MIO-type and DIO-type maps are each closed under composition, under ⊗ id, under partial
  trace, under feedforward of the form Σ_r |r⟩⟨r| ⊗ K_r on configuration records, and under
  restriction to sub-instruments (postselection).
- Every element of (n1), (n3) and (n5) is monomial, so it is both MIO and DIO.
- Appending |x⟩ or a diagonal mixture is MIO and DIO.
- Appending any fixed ω is DIO, since Δ(ρ ⊗ ω) = Δρ ⊗ Δω. It is MIO iff ω is diagonal.
- So 𝒩 ⊆ MIO ∩ DIO, with monomial Kraus operators (SIO), and 𝒩⁺ ⊆ DIO.

*Proof.*
- **CM and RM.**
  - Composition: (AB)|x⟩ = Σ_z B_{zx}A|z⟩, so (AB)|x⟩ has at most one nonzero entry. RM follows
    by transposition.
  - Tensoring: (A ⊗ 1)|x, w⟩ = A|x⟩ ⊗ |w⟩.
  - The isometry |v⟩ ↦ |v⟩ ⊗ |χ⟩ has row (v, h) equal to χ_h⟨v|.
- **MIO.**
  - Diagonal joint states are mixtures of |x⟩⟨x| ⊗ |y⟩⟨y|.
  - The partial trace of a diagonal state is diagonal.
  - Feedforward on a configuration record acts blockwise on a diagonal record.
- **DIO.**
  - Composition: if ΔΦ₁ = ΔΦ₁Δ and ΔΦ₂ = ΔΦ₂Δ, then ΔΦ₂Φ₁ = ΔΦ₂ΔΦ₁ = ΔΦ₂ΔΦ₁Δ = ΔΦ₂Φ₁Δ.
  - Tensoring: Δ_{XY} = Δ_X ⊗ Δ_Y.
  - Partial trace: Tr_Y ∘ Δ_{XY} = Δ_X ∘ Tr_Y.
- Sub-instruments keep each property branchwise. ∎

**Theorem A′ (native class; (N) as algebra on 𝒩, X; its reading "OI's native operations create
no coherence" is (I) on KIN, conditional on R-READ; CONFIRMING).**
- *Statement.* Start from any diagonal joint initial state. It may have arbitrary correlations
  between the visible preparation and the hidden or ancilla systems, so no preparation
  independence is assumed. Then every branch output of every 𝒩-protocol is diagonal.
- *Bound.* For every pure target ψ and every branch output σ,
  ½‖ψψ† − σ‖₁ ≥ sup_{i≠j} |ψ_i ψ_j|. The bound is tight for |+⟩, giving ½. It holds for
  subnormalized branches and is uniform in size, depth and control.
- *Proof.* Lemma C gives MIO. For the bound, take X = e^{iα}|i⟩⟨j| + h.c. with ‖X‖ = 1. Since σ
  has no off-diagonal entries, ‖ψψ† − σ‖₁ ≥ |tr((ψψ† − σ)X)| = 2|ψ_iψ_j|. ∎
- *Grade.* This is the IO/SIO no-creation result, for OI's native class.

**Theorem B (coherent resources without a detector; (I) on KIN, fixed coherent resource states,
countable carriers; X; ELABORATING on S1).** Let Φ be any 𝒩⁺-protocol.
- **(i) Exact.** No branch of Φ on ℂ^{C_V} equals p·Ad_W with p > 0 and W a non-monomial
  unitary.
- **(ii) Approximate.** For every trace-preserving Φ, ‖Φ − Ad_W‖_⋄ ≥ 2κ_row(W), where
  κ_row(W) := sup_i sup_{v≠v′} |W_{iv}W_{iv′}|. For H the bound is 1, out of a maximum of 2.

*Proof.*
- **(i)** The branch is DIO by Lemma C. So p·W†|i⟩⟨i|W is diagonal for each i. A diagonal rank-one
  PSD operator is a multiple of a basis projector, so row i of W has a single nonzero entry. A
  unitary with single-entry rows is monomial. This step is also valid in countable dimension, by
  surjectivity.
- **(ii)** Take ε > 0, and choose i, v, v′ with |W_{iv}W_{iv′}| > κ_row − ε.
  - Let φ_± = (|v⟩ ± e^{iβ}|v′⟩)/√2, with β chosen so that
    ⟨i|Ad_W(φ_+) − Ad_W(φ_−)|i⟩ = 2|W_{iv}W_{iv′}|.
  - DIO gives ⟨i|Φ(φ_+) − Φ(φ_−)|i⟩ = 0.
  - For a traceless Hermitian M, |⟨i|M|i⟩| ≤ ½‖M‖₁. So 2(κ_row − ε) < ‖Φ − Ad_W‖_⋄.
  - Let ε → 0. ∎

*Scope.*
- **S1** is the one-step, no-measurement case of (i).
- **CM-3 of #1508.** The coherent controlled append Σ_v |v⟩⟨v| ⊗ |χ_v⟩ is itself RM, hence DIO,
  so B covers CM-3 without any preceding read. A hidden state assigned as a function of the
  preparation, nonlinearly in a coherent ρ, lies outside every linear (CP) class treated here. The
  route table's "insufficient" holds for the linear model only.
- **Ben Dana et al. (2017).** There is no contradiction. IO plus a maximally coherent resource
  implements arbitrary unitaries because IO Kraus operators may be non-RM, that is, they may detect
  coherence. 𝒩⁺ only ever detects configurations: under any DIO map the diagonal of ρ ⊗ ω depends
  on ρ only through diag ρ, so no resource ω helps.

**Theorem C (necessity, sharp form; (I) on KIN and countable carriers; X; NEW relative to the
corpus).** Let Φ be a trace-preserving protocol, any finite composition with feedforward and
discard of operations O_1, …, O_n. Let W be a unitary on ℂ^{C_V}, and define
κ_col(W) := sup_x sup_{i≠j} |W_{ix}W_{jx}|.
- **(a)** If ‖Φ − Ad_W‖_⋄ < 2κ_col(W), some O_k **creates coherence** (is not MIO-type).
- **(b)** If ‖Φ − Ad_W‖_⋄ < 2κ_row(W), some O_k **detects coherence** (is not DIO-type).
- **(c)** For non-monomial W, κ_col and κ_row are both positive.
- **(d) Exact form, including postselected branches.** A branch p·Ad_W needs a creator and a
  detector unless W is monomial.
- **Corollary.** Every creator is a splitter (non-CM-decomposable), and every detector is a merger
  (non-RM-decomposable). The splitter/merger pair of r1 is therefore implied, but it is strictly
  coarser on the creation side, so the sharp pair is the one stated.

*Proof.*
- **(b)** If no O_k detects coherence, then Φ is DIO (Lemma C), and B(ii)'s argument applies.
- **(a)** If no O_k creates coherence, then Φ is MIO. Take ε > 0, choose x, i, j with
  |W_{ix}W_{jx}| > κ_col − ε, and apply A′'s bound to ψ = W|x⟩:
  ‖Φ(|x⟩⟨x|) − W|x⟩⟨x|W†‖₁ ≥ 2(κ_col − ε). This is at most ‖Φ − Ad_W‖_⋄.
- **(c)** A unitary with single-entry columns, or single-entry rows, is monomial.
- **(d)** Apply the MIO and DIO arguments to the branch. ∎

**Proposition D (detection half on measurable carriers; (I) on KIN, nonsingularity, normality;
X; ELABORATING; proof due to the review sketch, written out here and pending review).**
- *Setting.* C_V is finite. (H, ν) is a standard measure space. T is a measurable bijection of
  C_V × H with measurable inverse, **nonsingular** for (counting × ν). ω is a **normal** state on
  B(L²(H)).
- *Configuration algebras.* For each space, 𝒜 = ℓ^∞(C_V) ⊗̄ L^∞(H), acting by multiplication.
- *Readouts.* Configuration readouts are instruments indexed by **countable** measurable
  partitions, with projections in 𝒜, or more generally instruments whose duals preserve 𝒜. A
  Lüders-type normal instrument for a continuous hidden PVM does not exist and is not included.
- *DIO, Heisenberg form.* On measurable carriers, DIO-type means Φ*(𝒜_out) ⊆ 𝒜_in. A diffuse MASA
  has no normal conditional expectation Δ, so the Schrödinger form is not used.
- *Statement.* Every protocol built from Koopman unitaries U_T of such bijections, appending normal
  states, the readouts above, feedforward on configuration records, discard and postselection has
  a Heisenberg dual Φ* that maps 𝒜_out into 𝒜_in. Theorem B(i) and (ii) then hold verbatim with C_V
  finite.
- *Theorem C(b), measurable form.* If every O_k satisfies O_k*(𝒜) ⊆ 𝒜, then
  ‖Φ − Ad_W‖_⋄ ≥ 2κ_row(W). So within that distance some O_k has a dual that leaves the
  configuration algebra, that is, it detects coherence.
- *Relation to r1's missing lemma.* D **supersedes** the direct-integral RM Kraus lemma that r1
  named as missing, for the detection half: it makes that lemma unnecessary. It does not prove it.
  The direct-integral Kraus statement itself remains unproved, and it is not needed.

*Proof.* Each step is checked in the Heisenberg picture.
1. **Koopman unitaries.** Let (U_T f)(z) = J(z)^{1/2} f(T⁻¹z), with J the Radon–Nikodym derivative
   of the image measure; it exists by nonsingularity. U_T is unitary, and U_T M_g U_T† = M_{g∘T⁻¹}.
   So conjugation maps 𝒜 onto 𝒜. Spectral type plays no role.
2. **Configuration readouts.** These are projections in 𝒜, and their duals multiply within 𝒜.
3. **Discard.** The dual of the partial trace is X ↦ X ⊗ 1, which maps 𝒜 into 𝒜 ⊗̄ 𝒜.
4. **Appending ω.** The dual is the normal slice map id ⊗ ω. It sends M_f, with f ∈
   ℓ^∞(C_V) ⊗̄ L^∞(H), to the multiplication operator v ↦ ω(M_{f(v,·)}) in ℓ^∞(C_V). Normality
   is used for the slice on the von Neumann tensor product. With C_V finite it is not needed for a
   single hidden state appended while no diffuse hidden factor is present (Remark D′).
5. **Feedforward.** Feedforward on configuration records is a direct sum over 𝒜-projections.
6. **Postselection.** Sub-instruments keep the property branchwise.
7. **Conclusion.** Induction gives Φ*(|i⟩⟨i|) ∈ ℓ^∞(C_V), so Φ is DIO on the finite visible space.
   - (ii) follows as in Theorem B: tr(Φ(φ_±)|i⟩⟨i|) = ⟨φ_±|Φ*(|i⟩⟨i|)|φ_±⟩, and this is equal for
     φ_+ and φ_−.
   - (i) follows because Ad_W*(|i⟩⟨i|) = W†|i⟩⟨i|W is diagonal and rank one.
   - No Kraus decomposition and no extremality step is used. ∎

**Remark D′ (Proposition D without normality; (I): KIN on the visible carrier, the algebraic
lift of the hidden state as a state on B(L²(H)), nonsingularity, C_V finite, and configuration
readouts as in D; X; pending independent re-review).**

*Hypotheses.* All of Proposition D's premises are kept except the normality of ω:
- C_V is finite at input and output;
- (H, ν) is a standard measure space, and T is a measurable bijection with measurable inverse that
  is **nonsingular**, so that D's Koopman unitary exists;
- readouts are as in D, on countable partitions.

Finiteness of intermediate visible ancillas is not used. Countability of the hidden index set is not
used either: H is a measure space. ω is a **single** state on B(L²(H)) of the whole hidden carrier,
not necessarily normal, and it is the only such state. **When ω is appended, the coexisting algebra
is ℓ^∞ of a countable set:** visible configurations and ancillas, or configuration states on a
countable hidden set. No diffuse hidden factor is present then. **Every appended state after it is
normal:** a configuration state or a fixed normal ω′.

The condition at the append is used. Suppose a diffuse hidden factor H₁ is present when ω is
appended, whatever H₁'s state. Then σ_ω would have to act on L^∞(H₁) ⊗̄ L^∞(H), which is not
defined for non-normal ω. For a discrete X, ℓ^∞(X) ⊗̄ L^∞(H) admits the pointwise slice
x ↦ ω(f_x). Normal appends after ω are harmless: their slices act after σ_ω in time, which is
before it in the Heisenberg order. A product of two non-normal states also has no canonical
extension to B(L²(H₁) ⊗ L²(H₂)).

*Definitions.*
- For f ∈ ℓ^∞(C_V) ⊗̄ L^∞(H) = ⊕_v L^∞(H) (a finite direct sum, since C_V is finite), f_v ∈ L^∞(H)
  is its v-th section.
- For a single Koopman step, g_v is the v-th section of the indicator of T⁻¹({i} × H), so that
  U_T†(|i⟩⟨i| ⊗ 1)U_T = ⊕_v M_{g_v}.
- The joint state is (ρ ⊗ ω)([X_ab]) := Σ_ab ρ_ba ω(X_ab) on M_n(B(L²(H))). This is ρ composed
  with id_n ⊗ ω. A positive functional is completely positive, so id_n ⊗ ω is CP, and ρ ⊗ ω is a
  state.

*Proof (full induction).*
1. **Factorization.** Split the protocol at the append of ω into Ψ_pre (the steps before it) and
   Ψ_post (the steps after it). The Heisenberg dual is
   **Φ_eff* = Ψ_pre* ∘ σ_ω ∘ Ψ_post***, where:
   - Ψ_post* is the dual of the steps after the append;
   - σ_ω is the slice by ω;
   - Ψ_pre* is the dual of the steps before it.
2. **Ψ_post* stays in the configuration algebras.** D's steps 1 (Koopman, by nonsingularity), 2
   (readouts on countable partitions), 3 (discard), 5 (feedforward) and 6 (postselection) use no
   normality. D's step 4 with the normal appends after ω also maps configuration algebras into
   configuration algebras. By induction over these steps, Ψ_post* maps ℓ^∞(C_V,out) into
   ℓ^∞(X) ⊗̄ L^∞(H), where X is the countable configuration set coexisting with ω at the append.
   The countable sums converge as in D.
3. **The non-normal slice.** σ_ω(f) := (ω(f_x))_x is the pointwise slice over the countable index
   x ∈ X. X covers C_V × (ancilla configurations) when visible ancillas are present at the append.
   It is defined for any positive ω, maps ℓ^∞(X) ⊗̄ L^∞(H) into ℓ^∞(X), and is unital and
   positive. Its range is abelian, so it is completely positive.
4. **The pre-append part.** Ψ_pre* involves no diffuse hidden factor and only configuration
   operations, so it maps ℓ^∞(X) into ℓ^∞(C_V,in) and is ucp. "ω is applied only once" is then
   exact: σ_ω is the unique non-normal slice, and it is followed in the Heisenberg order only by
   Ψ_pre*.
5. **The effective map.** Φ_eff* = Ψ_pre* ∘ σ_ω ∘ Ψ_post* is a ucp map on finite matrices (C_V
   finite at both ends). It sends |i⟩⟨i| to a diagonal matrix, for example Σ_v ω(M_{g_v})|v⟩⟨v| for one Koopman
   step. So Φ_eff is a genuine DIO channel M_n → M_n, every state of which is normal.
6. **Conclusion.** Theorem B(i) and (ii), and Theorem C(b), apply verbatim to Φ_eff, including the
   diamond-norm bound with W on ℂ^{C_V}. Only D's step 4 changes; the remaining steps are
   normality-free. ∎

*Relations.*
- D′ is Proposition D with normality dropped, and nothing else changed. It is not a separate
  "finite visible" case, since D already assumes C_V finite.
- Conjecture D″ (singular T) is independent of D′: D′ does not touch singular bijections. If D″ were
  proved, its embedding would also have to carry a non-normal ω through the enlargement before D′
  could be combined with it. That is the open point D″ already names.

**Conjecture D″ (singular bijections; from the review sketch c.7066421069; not proved).** A singular
measurable bijection T reduces to a nonsingular one by enlarging the reference measure. Set
ν_{k+1} := the H-marginal of Σ_{g ∈ ⟨T⟩} c_g · g_*(counting × ν_k), with positive weights c_g
summing to 1, and ν_∞ := Σ_k 2^{−k} ν_k. Then T would be nonsingular for counting × ν_∞, and L²(ν)
would embed isometrically in L²(ν_∞), so Proposition D would apply on the enlarged space. Not
checked here. The open points are the quasi-invariance of ν_∞, and whether the embedding
intertwines the readouts and the hidden state.

*Creation half on measurable carriers.* A classical hidden law on a measurable carrier is not a
normal state on B(L²(H)) unless it is atomic. Its single-time case is `Main:338` (the
measurable-hidden-carrier corollary). For protocols with classical laws, the process is a classical
stochastic process on configurations, so every output is a law over configurations (P, CONFIRMING).

**Corollary C1 (interface placement; (I) on KIN; X).** Suppose the logical basis is U-rotated,
while preparations and readouts stay native.
- Logical preparation |U i⟩ creates coherence whenever U is non-monomial.
- Logical readout ⟨U i| detects coherence whenever U is non-monomial.

For a unitary, CM ⇔ RM ⇔ monomial (C(c)). Strictly, the effect |U i⟩⟨U i| is non-diagonal iff
column i of U has more than one nonzero entry.

Changing the encoding relocates both elements to the interface; it does not remove them (compare
#1508 CM-2).

## 4. N3: routes classified, and the tightness countercontrol

**CC-1 (one-bit teleportation; layer X, checked by hand and by the reviewer numerically to
1e-15; possible route, and tightness of C).** The steps:
1. Append |+⟩. This is the only creator (n2⁺).
2. Apply CZ, a diagonal phase (n1).
3. Read the input destructively with ⟨±|. This is the only detector. It is MIO, since its output
   space is one-dimensional, and it is not DIO.
4. Apply X^m by feedforward, a native permutation.

For ψ = a|0⟩ + b|1⟩: CZ(ψ ⊗ |+⟩) = a|0⟩|+⟩ + b|1⟩|−⟩.
- Outcome +: ⟨+|_S gives (1/√2)(a|+⟩ + b|−⟩) = (1/√2)Hψ.
- Outcome −: ⟨−|_S gives (1/√2)(a|+⟩ − b|−⟩) = (1/√2)XHψ, and X corrects it.

Both branches yield Hψ exactly, each with p = ½. So one creator and one detector suffice, with
everything else in 𝒩. Theorem C is tight in the number of non-native elements. Diagonal phases
are native here in the sense of (n1) and the kernel's supplied class (`phaseOperator_supplied`).

| Route | Creates coherence? | Detects coherence? | Status |
|---|---|---|---|
| Control, feedforward, randomness, larger carriers, greater depth (inside 𝒩) | no | no | **insufficient** (A′) |
| Fixed coherent resource or hidden states (𝒩⁺) | yes | no | **insufficient alone** (B, D) |
| Coherent controlled append Σ_v \|v⟩⟨v\| ⊗ \|χ_v⟩ (#1508 CM-3) | yes | no (RM) | **insufficient** in the linear model (B, Scope) |
| Preparation-dependent classical hidden laws (PIP dropped) | no | no | **insufficient** (A′ assumes no PIP) |
| Change of logical basis | at preparation | at readout | **relocates** both (C1) |
| Diagonal phases (`PhasesAvailable`) | no | no | **insufficient**: phases are monomial |
| Non-monomial step on the configuration span (FLOW; `gateFlow_not_monomial`, K) | yes | yes | **sufficient**; **not necessary** as such |
| Destructive non-configuration readout (⟨±\|) | no | yes | a possible detector (CC-1) |
| Coherent ancilla plus one non-configuration readout plus feedforward | yes | yes | **verified construction** (CC-1) |
| Measurable carrier: singular bijection; non-normal hidden state with C_V infinite; several non-normal hidden states | — | — | **INCONCLUSIVE (U1′)**, pending Conjecture D″ and the cases of §6 |

**What is necessary (proved, Theorem C):** a coherence creator and a coherence detector.
**What is not necessary:** FLOW specifically.

**Skepticism.** The necessity is not definitional, for three reasons:
- closure under measurement, feedforward, postselection and discard;
- distance bounds that hold uniformly over size and depth;
- the extension of the detection half to measurable carriers.

Each ingredient alone fails: B and D show that a creator without a detector fails, and the MIO
analogue shows that a detector without a creator fails. CC-1 shows that the pair suffices.

## 5. N5: native status (conditional on R-READ)

- **Dynamics.** Substratum update by a bijection, (n1) (`substratumClass_monomial`, K, finite).
- **Preparations, priors, ready cells.** Configurations or laws over them (posit (iv); RES, #1501),
  (n2).
- **Readout and records.** Under R-READ, all native readout effects lie in the configuration
  algebra, (n3).
- **Control.** Configuration controller fields (EP:75–79), (n4).

**Verdict.** **Conditional on R-READ**, OI's stated operations lie in 𝒩. The verdict has three
parts:
- By A′ ((I) on KIN as a reading), they create no Born-form coherence at any size.
- By C, an extension that realizes a non-monomial unitary needs a native coherence creator and a
  native coherence detector.
- The generated-theory counterparts are `substratumGen_not_control` and
  `substratumTheory_not_layerFlowExecutable` (K, finite carriers), with
  `derivedOI_qm_iff_layerFlowExecutable'` (DerivedQ3.lean:222) taking the flow as a hypothesis.
  No formal map is claimed.

**Relation to O1.** QOPS (#1501) records KIN as the earliest import and FLOW as the earliest
unsupported step. OPRES sharpens FLOW into the pair {coherence-creating operation,
coherence-detecting operation}.

## 6. N4: the operational layer, and what stays INCONCLUSIVE

**Operational necessity: all classical ((I) as named; P).**
- Non-atomic uncontrolled variables (L-H′, GA §4).
- Unbounded records (GA §4 N5).
- Ready cells (P5, PR1, #1501).
- Unbounded readout cones (Proposition U, #1504, (I) via (xiv)).
- For efficient hosting of BQP, the failure of one of H1–H5 (BQ1-D, #1498, (I)).

D-W at trivial E (#1506 §4.3, sketch) meets the exact operational laws classically. Gottesman–Knill
shows the converse gap: coherent dynamics can be efficiently classically simulable. So
**representational necessity (C) does not imply operational necessity.** This is conditional on
D-W's sketch.

**INCONCLUSIVE, with the missing premise named.**
- **U1′ (narrowed; the cases listed).** The detection half is settled in three cases:
  - Proposition D: nonsingular measurable bijections with normal hidden states;
  - Remark D′: Proposition D's setting (nonsingular bijection, C_V finite) with exactly one
    possibly non-normal hidden state. No diffuse hidden factor may be present when it is appended,
    and every append after it must be normal;
  - `Main:338`: classical laws.

  What remains INCONCLUSIVE:
  - (i) singular bijections, pending Conjecture D″;
  - (ii) non-normal hidden states when C_V is infinite. A reviewer sketch (c.7067475063), not
    established, suggests this is narrower than it looks. For countable C_V and normal visible ρ
    the joint state is defined for any ω, and it gives Σ_v ρ_vv ω(f_v). What can fail is that the
    output visible marginal is non-normal, which would need a state-space form of the bound;
  - (iii) more than one non-normal hidden state, or a non-normal state appended while a diffuse
    hidden factor is present (outside D′). A later normal diffuse factor coupled by a Koopman step
    is covered by D′;
  - (iv) whatever fails in the reduction of (i).

  It is **not** claimed that the lift is undefined in these cases.
- **U2 (decisive; physical).** Can OI's ontology host a coherence detector, and a creator or
  coherent input? Within 𝒩 they cannot arise (A′, C). They require one of three things:
  - extending Φ beyond a bijection;
  - a native readout effect outside the configuration algebra, against R-READ;
  - a representation in which configurations are not the basis, against (a) and KIN as read here.

  No native derivation of any of these is known.

## 7. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Lemma C | (N) as algebra | X | ELABORATING |
| Theorem A′ | (N) as algebra on 𝒩; reading (I) on KIN, conditional on R-READ | X | CONFIRMING (IO/SIO; `Main:328`) |
| Theorem B | (I): KIN, fixed coherent resource states, countable carriers | X | ELABORATING (S1 extended) |
| Theorem C | (I): KIN, countable carriers | X | NEW relative to the corpus; standard after Theurer et al. |
| Proposition D | (I): KIN, nonsingularity, normality | X | ELABORATING (from the review sketch); supersedes the r1 lemma for the detection half |
| Remark D′ | (I): KIN on the visible carrier; algebraic lift of the hidden state; nonsingularity; C_V finite; readouts as in D | X | ELABORATING, pending independent re-review |
| Conjecture D″ | conjecture | P | open |
| CC-1 | construction using one imported creator and one imported detector | X | POSITIVE (tightness) |
| Corollary C1 | (I): KIN | X | ELABORATING |
| §5 | (N) membership, conditional on R-READ | P, K | CONFIRMING |
| §6 operational | (I): EP, (xiv), H1–H5, D-W sketch | P | CONFIRMING |

**Productivity test (PLAN §4).** Met. The result covers protocols and approximation, and it names
the necessary elements more sharply than FLOW. The outcome is a scoped OBSTRUCTION with
INCONCLUSIVE extensions U1′ and U2.

**Decisive computation.** None is needed. An optimal distance over DIO channels is an SDP; it is
not decisive and is not preregistered.

## 8. For owner decision (nothing adopted)

- **R-READ, stated precisely.** Are all native readout effects in the configuration algebra (ℓ^∞,
  or L^∞)? If not, a native readout detects coherence, and U2 moves from "no detector" to "a
  detector is present; a coherence source is still needed".
  - If that readout includes a **sharp**, destructive, projective readout in a basis **unbiased**
    with respect to the configurations, as in CC-1, then one such readout plus a fixed |+⟩, CZ and
    an X correction realizes H exactly.
  - An unsharp non-diagonal effect, for example diag(½, ½) + ε σ_x, detects coherence but does not
    give exact H.
- **O1 restatement (candidate).** Whether to restate O1 as the pair {a native operation that
  creates coherence (not MIO-type), a native operation that detects coherence (not DIO-type)},
  **possibly one element** (FLOW is both), in place of FLOW alone.
  - The pair is necessary at the Born-form level, (I) on KIN.
  - It is sufficient only together with native diagonal phases and permutations, as in CC-1. The splitter/merger pair of r1 is not proposed, because it is
  over-inclusive on the creation side.

## 9. What this note does not do

It edits no manuscript, no reviewed record and no Issue body. It runs no computation and
dispatches no workflow. It adopts no premise and posts nothing on #1169.
