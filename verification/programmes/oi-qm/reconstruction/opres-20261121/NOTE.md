# OPRES: necessary resources for non-monomial transformations (research note)

**WIP / UNVERIFIED. Paper research only; not reviewed.** This note walks the nodes of `PLAN.md`
(committed before the derivation, at `1f926939`). It adopts no premise or criterion, edits no
manuscript or reviewed record, runs no computation and changes no status. Physical source remains
NOT PASSED.

Tracking: Issue #1509; draft PR #1511 (stacked on #1508 at `df520f3b`). Base for corpus citations:
`main` at `df6da1c6`. Layers: X exact algebra on paper; P paper argument; K kernel theorem on `main`,
cited and not duplicated.

## 0. Outcome and the three questions

**Outcome (PLAN §4).**
- **Representational scope** (Born form on the configuration basis, countable carriers):
  **OBSTRUCTION.** Theorem C proves that every protocol realizing a non-monomial unitary
  transformation, exactly or within an explicit distance, contains two kinds of element: a
  **splitter**, an operation with no column-monomial Kraus decomposition, and a **merger**, an
  operation with no row-monomial Kraus decomposition. They may be the same element. Control,
  feedforward, configuration readout, randomness, size and depth cannot replace either.
- **Native status:** OI's stated operations supply neither (Theorem A′, §5). The unavoidable
  additional premise, for this class, is a native physical operation that merges distinct
  configurations coherently, together with a coherence source. That is a physical premise.
  Theorem C shows that mathematics inside the class cannot supply it.
- **Operational scope** (record laws): **no non-classical resource is shown to be necessary.** The
  necessary operational resources established are classical: non-atomic uncontrolled variables,
  unbounded records, ready cells and unbounded readout cones. Exact laws are met classically by D-W,
  in sketch.
- **INCONCLUSIVE** on two points, each with its missing premise named in §6: uncountable hidden
  carriers, and whether OI's ontology can host a merger.

**Established.**
- Lemma C, Theorems A′, B and C, and Corollary C1. All are exact algebra on paper (X), with
  explicit approximation bounds.
- The route classification of §4: necessary, merely possible, or insufficient (X and P).
- §5's native-membership check (P, with K citations).

**Assumed.**
- **KIN:** the Born-form representation on configurations (decision 4). It is what gives
  "non-monomial" its meaning.
- **(e):** countable carriers.
- For B and C only, the imported **fixed coherent resource states**, product with the input.
- **R-READ:** native readouts are configuration-basis. This is a reading of READ (#1501), not
  stated there in these words.
- Operational results: the EP-schema clauses EP:77, EP:79 and EP:97, (xiv) beyond its Bell scope
  (Proposition U), H1–H5 (BQ1), and D-W's sketch status.

**Missing.**
- The earliest unsupported step is a **physical mechanism**: a native merger, plus a splitter or a
  native coherence source. A non-monomial step (FLOW) is one possible route that supplies both. It
  is not necessary as such.
- **Mathematics:** the uncountable-carrier extension of Lemma C (§6).

## 1. Literature (searched first)

| Topic | Source | Relation |
|---|---|---|
| Coherence resource theory; incoherent operations | T. Baumgratz, M. Cramer, M. B. Plenio, PRL 113, 140401 (2014); A. Winter, D. Yang, PRL 116, 120404 (2016); review: A. Streltsov, G. Adesso, M. B. Plenio, Rev. Mod. Phys. 89, 041003 (2017) | Theorem A′ is the native-class instance of "free operations cannot create coherence" |
| Physically incoherent operations (PIO) | E. Chitambar, G. Gour, PRL 117, 030401 (2016) and PRA 94, 052336 (2016) | 𝒩 is PIO-like: permutations, incoherent ancillas, incoherent measurements, classical processing |
| Speakable and unspeakable coherence | I. Marvian, R. W. Spekkens, PRA 94, 052324 (2016) | the basis is fixed physically (configurations), assumption (a) |
| Creation against detection of coherence | T. Theurer, D. Egloff, L. Zhang, M. B. Plenio, PRL 122, 190405 (2019), arXiv:1806.07332; follow-up arXiv:2102.04863 | Theorem C's splitter and merger are Kraus-level sufficient conditions for leaving their creation-free (MIO-type) and detection-free (DIO-type) classes. Row-monomial implies Δ∘Φ = Δ∘Φ∘Δ. No formal equivalence is claimed |
| Measurement-based computation | R. Raussendorf, H. J. Briegel, PRL 86, 5188 (2001) | a possible route: coherent resource plus non-configuration readouts plus feedforward (§4) |
| Gate teleportation | X. Zhou, D. W. Leung, I. L. Chuang, PRA 62, 052316 (2000) | possible routes using readouts in rotated bases |
| Trace-distance and fidelity bounds | M. A. Nielsen, I. L. Chuang, *Quantum Computation and Quantum Information* (2000), §9.2 | standard norms used in the bounds |

**Corpus.**
- `Main:328` and `:338` (diagonal preservation, finite and measurable).
- `substratumClass_monomial` (`OIBridge/CoherentContinuumSource.lean`:212, K).
- `gateFlow_not_monomial` (same file, :74, K): the fractional-time flow is non-monomial.
- `substratumGen_not_control` (`StructuralClosure.lean`:330, K).
- `substratumTheory_not_layerFlowExecutable` (`LiftAudit.lean`:200, K).
- `preservesDiag_conjChannel_of_colMonomial` (`SubstantiveCensus.lean`:654, K).
- `preservesDiag_sum` (`DiagonalTheory.lean`:84, K).

## 2. Definitions (N1 setup)

Configuration spaces X, Y are countable, and ℓ²(X) has its point basis (assumption (a): the
configuration basis is fixed). For a bounded linear map K : ℓ²(X) → ℓ²(Y):

- K is **column-monomial (CM, splitter-free)** iff each column K|x⟩ has at most one nonzero entry.
- K is **row-monomial (RM, merger-free)** iff each row ⟨y|K has at most one nonzero entry.
  Equivalently, the columns have pairwise disjoint supports.
- K is **monomial** iff it is both.

A CP map, or an instrument branch, is **CM-decomposable** (respectively **RM-decomposable**) iff it
has a Kraus decomposition, finite or countable, all of whose operators are CM (respectively RM).

**Operation classes.**
- **𝒩 (native, in Born form).** Generated by:
  - (n1) the permutation unitary of a bijection of a configuration set, and diagonal phases;
  - (n2) appending a system in a configuration state |x⟩, or in a classical (diagonal) mixture of
    them (ready cells, hidden priors);
  - (n3) configuration-basis Lüders measurement of any subsystem, with recording;
  - (n4) classical feedforward on recorded outcomes;
  - (n5) discard (partial trace);
  - (n6) postselection on recorded outcomes.

  𝒩 is taken with any finite depth and any countable size.
- **𝒩⁺.** 𝒩 plus (n2⁺): appending a system in a **fixed** density operator ω of any coherence, the
  same for every input (product).

## 3. Results

**Lemma C (closure; (N) as algebra; X).**
1. CM maps are closed under composition, tensoring with the identity, and restriction to
   sub-families.
2. RM maps are closed under the same three operations.
3. Every Kraus operator of (n1), (n3) and (n5) is monomial: a permutation or phase, a basis
   projection, or ⟨a| on a factor.
4. Appending |x⟩ is monomial. Appending a fixed pure |χ⟩, the isometry |v⟩ ↦ |v⟩ ⊗ |χ⟩, is RM. It
   is CM only if χ is a basis vector up to a phase.
5. Mixed ancillas decompose into pure ones. Feedforward and postselection produce Kraus operators
   that are products of the elements' Kraus operators, or sub-families of them.
6. Hence every branch of an 𝒩-protocol is CM- and RM-decomposable, and every branch of an
   𝒩⁺-protocol is RM-decomposable.

*Proof.*
- CM: (AB)|x⟩ = Σ_z B_{zx} A|z⟩. If B|x⟩ has its only nonzero entry at z₀ and A|z₀⟩ has at most one
  nonzero entry, then (AB)|x⟩ has at most one.
- RM: apply the same argument to rows, by transposition.
- Tensoring: (A ⊗ 1)|x, w⟩ = A|x⟩ ⊗ |w⟩, and likewise for rows.
- The isometry |v⟩ ↦ |v⟩ ⊗ |χ⟩ has row (v, h) equal to χ_h⟨v|, a single nonzero.
- Items 5 and 6 then follow by induction on the protocol. ∎

**Theorem A′ (native class; (N); X; CONFIRMING).** Let any joint initial state of all systems be
diagonal in the configuration basis, with arbitrary correlations between the visible preparation
and hidden or ancilla systems, so no preparation independence is assumed. Then every branch output
of every 𝒩-protocol is diagonal.

For every pure target ψ and every branch output σ, ½‖ψψ† − σ‖₁ ≥ max_{i≠j} |ψ_i ψ_j|. For |+⟩
the bound is ½. It is uniform in carrier size, depth and control.

*Proof.*
- Each Kraus operator is CM (Lemma C), so conjugation preserves diagonality
  (`preservesDiag_conjChannel_of_colMonomial`, K). Sums preserve it too (`preservesDiag_sum`, K).
  Partial trace of a diagonal state is diagonal.
- For the bound: let M = ψψ† − σ. Take X = e^{iα}|i⟩⟨j| + h.c., with ‖X‖ = 1, so
  ‖M‖₁ ≥ |tr(MX)| = 2|ψ_i ψ_j̄|. ∎

*Grade.* This is the coherence resource theory's "free operations create no coherence", in OI's
native class (CONFIRMING; `Main:328`). Its content for OI is in §5: native states are laws over
configurations, so native operations alone never produce Born-form coherence. Coherence in the
`Sub:249` family enters only through representational coherent inputs ρ_V.

**Theorem B (coherent resources without a merger; (I) on KIN, fixed resource states, (e); X;
ELABORATING on S1).**
- (i) No branch of any 𝒩⁺-protocol on ℂ^{C_V} equals p·Ad_W, with p > 0 and W a non-monomial
  unitary. This holds at any depth, with measurement, feedforward, discard and postselection.
- (ii) For every trace-preserving 𝒩⁺-protocol channel Φ,
  ‖Φ − Ad_W‖_⋄ ≥ 2 κ_row(W), where κ_row(W) := max_i max_{v≠v′} |W_{iv} W_{iv′}|.
  For W = H, κ_row = ½, so ‖Φ − Ad_H‖_⋄ ≥ 1.

*Proof.*
- (i) The branch p·Ad_W has Kraus rank one, so every Kraus decomposition of it consists of
  multiples of W. By Lemma C one decomposition is RM. So W is RM. A unitary with single-entry rows
  is monomial, which is a contradiction.
- (ii) An RM Kraus operator K gives ⟨i|KρK†|i⟩ = |K_{iv}|² ρ_{vv} for the unique v. So the
  diagonal of Φ(ρ) depends on the diagonal of ρ only.
  - Pick i, v, v′ attaining κ_row. Let φ_± = (|v⟩ ± e^{iβ}|v′⟩)/√2, with β chosen so that
    |W_{iv} + e^{iβ}W_{iv′}|² − |W_{iv} − e^{iβ}W_{iv′}|² = 4|W_{iv}W_{iv′}|.
  - Then ⟨i|Ad_W(φ_+) − Ad_W(φ_−)|i⟩ = 2κ_row, while ⟨i|Φ(φ_+) − Φ(φ_−)|i⟩ = 0.
  - For a traceless Hermitian M, |⟨i|M|i⟩| ≤ ½‖M‖₁. Hence
    2κ_row ≤ ½‖(Ad_W − Φ)(φ_+)‖₁ + ½‖(Ad_W − Φ)(φ_−)‖₁ ≤ ‖Ad_W − Φ‖_⋄. ∎

*Scope.* S1 is the one-step, no-measurement case of (i). B adds protocols, measurement,
feedforward, postselection and approximation. CM-3 of #1508 lies in 𝒩⁺ preceded by a
configuration read: its Kraus operators have a single nonzero column, hence are RM. So it is
covered, and it cannot give Ad_H on coherent inputs.

**Theorem C (necessity; (I) on KIN and (e); X; NEW relative to the corpus).** Let a
trace-preserving protocol be any finite composition, with feedforward and discard, of operations
O_1, …, O_n on countable configuration spaces in Born form. Let W be a unitary on ℂ^{C_V}, and put
κ_col(W) := max_x max_{i≠j} |W_{ix} W_{jx}|.
- (a) If ‖Φ − Ad_W‖_⋄ < 2κ_col(W), some O_k has no CM decomposition: it is a splitter.
- (b) If ‖Φ − Ad_W‖_⋄ < 2κ_row(W), some O_k has no RM decomposition: it is a merger.
- (c) For W non-monomial, κ_col and κ_row are both positive. A unitary with single-entry columns,
  or with single-entry rows, is monomial.

So any exact realization, and any realization better than the stated distances, contains a
splitter **and** a merger, possibly the same element. For postselected branches, the exact form is
the same: no branch p·Ad_W unless W is both CM and RM (B(i) and its column analogue).

*Proof.*
- (b) If every O_k is RM-decomposable, so is Φ (Lemma C), and B(ii) gives the bound.
- (a) If every O_k is CM-decomposable, Φ preserves diagonality. Pick x, i, j attaining κ_col.
  Then ‖Φ(|x⟩⟨x|) − W|x⟩⟨x|W†‖₁ ≥ 2|W_{ix}W_{jx}|, by the bound of A′ applied to ψ = W|x⟩. That
  quantity is at most ‖Φ − Ad_W‖_⋄.
- (c) A unitary's columns are nonzero. If every column has one entry, W is monomial. Rows likewise.
  ∎

**Corollary C1 (interface placement; (I) on KIN; X).** Suppose the logical basis is rotated by a
unitary U, dropping (a) at the logical level, while preparations and readouts stay native
configuration operations. Logical preparation |U i⟩ from a configuration is then a splitter
whenever U is not CM. Logical readout ⟨U i| is a merger whenever U is not RM. Changing the encoding
moves the two elements to the interface; it does not remove them. The equivalence of the swap X
with H (#1508 CM-2) shows this placement explicitly.

## 4. N3: routes classified

| Route | Splitter? | Merger? | Status |
|---|---|---|---|
| Control, feedforward, classical randomness, larger carriers, greater depth (inside 𝒩) | no | no | **insufficient** (A′) |
| Fixed coherent resource or hidden states (𝒩⁺) | yes | no | **insufficient alone** (B); a possible splitter |
| Preparation-dependent coherent hidden states (#1508 CM-3) | yes, on configuration inputs only | no | **insufficient** for coherent inputs (B, Scope) |
| Preparation-dependent classical hidden laws (PIP dropped) | no | no | **insufficient** (A′ assumes no PIP) |
| Change of logical basis | moved to preparation | moved to readout | **relocates** both elements (C1) |
| Diagonal phases (`PhasesAvailable`) | no | no | **insufficient**: phases are monomial |
| Non-monomial step on the configuration span (FLOW; `gateFlow_not_monomial`, K) | yes | yes | **sufficient** (trivially); **not necessary** as such |
| Destructive readout in a non-configuration basis (⟨±\| on an ancilla) | no | yes | a possible merger |
| Retained Lüders readout onto a superposition (\|+⟩⟨+\|) | yes | yes | a possible splitter and merger |
| Coherent resource plus non-configuration readouts plus feedforward (MBQC) | yes | yes | **possible route** (literature; not checked here) |
| Uncountable hidden carrier with a non-classical state | — | — | **INCONCLUSIVE** (§6) |

**What is necessary (proved, Theorem C):** a splitter and a merger. **What is not necessary:** FLOW
specifically. A coherent resource state combined with a non-configuration readout is an alternative
(possible route).

**Skepticism.** Is the necessity trivial by definition? Monomiality of the target is defined
entrywise, but two parts of C are not definitional:
- closure under measurement, feedforward, postselection and discard;
- distance bounds that hold uniformly over size and depth, at any carrier.

The independence of the two ingredients is shown by B (splitter without merger) and by the
column analogue (merger without splitter). Neither alone suffices.

## 5. N5: native status

- **Dynamics.** The substratum update is a bijection, type (n1). `substratumClass_monomial` (K)
  records that the substratum operator class is monomial.
- **Preparations, priors and ready cells.** These are configurations or probability laws over them
  (posit (iv); RES, #1501). Their Born form is diagonal, type (n2).
- **Readout and records.** READ reads visible configurations, and records are configurations
  (R-READ), type (n3).
- **Control.** Controller fields are configurations loaded by programs (EP:75–79), giving
  classical feedforward, type (n4).
- **Verdict ((N) membership, P with K citations).** OI's stated operations lie in 𝒩. By
  Theorem A′, they generate no Born-form coherence, exactly or within the stated bound, at any size.
  By Theorem C, any extension realizing a non-monomial unitary needs a **native merger and a native
  splitter**. The kernel no-gos are the generated-theory counterparts: `substratumGen_not_control`
  and `substratumTheory_not_layerFlowExecutable` (K), with `derivedOI_qm_iff_layerFlowExecutable'`
  (DerivedQ3.lean:222) taking the flow as a hypothesis. No formal map between them and Theorem C
  is claimed.
- **Relation to O1 and the earliest links.** In QOPS (#1501), KIN is the earliest import and FLOW
  the earliest unsupported physical step. OPRES sharpens FLOW into the pair {splitter, merger}.
  FLOW supplies both at once. A coherence source together with a non-configuration readout is the
  other kind of route.

## 6. N4: the operational layer, and what stays INCONCLUSIVE

**Operational necessity, all classical ((I) as named; P).** For exact operational laws on
`J_exact`:
- the law of U is non-atomic (L-H′, GA §4: EP:77, EP:79, EP:97);
- record capacity is unbounded (GA §4 N5);
- ready cells are a physical input under a uniform law (P5 and PR1, #1501);
- on a site-factorized finite-range substratum, readout cones are unbounded (Proposition U, #1504,
  (I) via (xiv));
- for efficient hosting of BQP, one of H1–H5 must fail (contrapositive of BQ1-D, #1498, (I)).

D-W at trivial E (#1506 §4.3; GA §2.2, sketch) meets the exact operational laws with classical
resources only. So **no non-classical resource is shown to be operationally necessary**, conditional
on that sketch. Interference is necessary for the representational target, not for record laws.
This keeps the D-W distinction of #1508 explicit: D-W and I-ε (`Main:574–610`) approximate or match
record laws, not Born-form channels, so they do not conflict with Theorems B and C.

**INCONCLUSIVE, with the missing premise named.**
- **(U1) Uncountable hidden carriers.** The missing lemma is a direct-integral form of Lemma C.
  Composition operators of measurable bijections on L²(V × H, ν), with partial trace taken in
  pointwise Kraus fields, would have to be shown RM, and the extremality step of B(i) carried to
  integral decompositions. Plausible, not proved. A Koopman representation of an ergodic map can
  have continuous spectrum, so the countable argument does not transfer verbatim.
- **(U2) Whether OI's ontology can host a merger.** This is the decisive open premise, and it is
  physical, not mathematical. Within 𝒩 it cannot arise (A′, C). It requires extending Φ beyond a
  bijection on configurations (a non-monomial step), or extending readout beyond configurations
  (a non-configuration measurement, against R-READ), or a representation in which configurations
  are not the basis (against (a) and KIN as read here). No native derivation of any of these is
  known.

## 7. Classification (§A.31) and productivity

| Item | Label | Layer | Class |
|---|---|---|---|
| Lemma C | (N), algebra | X | ELABORATING |
| Theorem A′ | (N) | X, K | CONFIRMING (`Main:328`; coherence resource theory) |
| Theorem B | (I): KIN, fixed coherent resource states, (e) | X | ELABORATING (S1 extended to protocols, with a bound) |
| Theorem C | (I): KIN, (e) | X | NEW relative to the corpus |
| Corollary C1 | (I): KIN | X | ELABORATING (#1508 CM-2) |
| Route table | as per row | X, P | — |
| §5 native membership | (N), reading R-READ | P, K | CONFIRMING |
| §6 operational | (I): EP, (xiv), H1–H5, D-W sketch | P | CONFIRMING |

**Productivity test (PLAN §4).** Met. The result covers protocols and approximation, and it names
the necessary element more sharply than FLOW: a splitter and a merger, either possibly being FLOW.
The outcome is OBSTRUCTION at the representational scope for countable carriers. It is
INCONCLUSIVE on U1 and U2. The fixed point is not reached, and review is needed before further
nodes.

**Decisive computation.** None is needed. The bounds are explicit. An optimal distance from Ad_H
over RM channels could be computed by a semidefinite program; it is not decisive and is not
preregistered.

## 8. For owner decision (nothing adopted)

- Whether R-READ (native readouts are configuration-basis) is the intended reading of READ. If a
  native readout could project onto superpositions of configurations, it would be a merger, and U2
  would change.
- Whether the O1 obligation should be restated as the pair {native splitter, native merger} rather
  than FLOW alone.

## 9. What this note does not do

It edits no manuscript, no reviewed record and no Issue body. It runs no computation and
dispatches no workflow. It adopts no premise and posts nothing on #1169.
