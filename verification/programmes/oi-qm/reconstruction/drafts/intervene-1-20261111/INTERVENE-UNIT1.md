# INTERVENE-1, unit 1: which operations do OI's own rules make physically available?

**Draft r2, after ChatGPT review 5857231398 (verdict REVISE, on head `592fede0`), pending re-review. WIP / UNVERIFIED.** This is a paper-only unit for #1169, owner-approved on 2026-11-11 in the coordinating session. It authorizes nothing. It adopts no physical premise, edits no manuscript and computes no OI mechanism. r2 has not been independently reviewed. Its only computations are the generic exact checks X1–X7 in `checks.py` in this directory, run with `python3 -I -B`. `DISPOSITIONS-r2.md` maps each review finding to its change.

Sources were read first-hand at `origin/main` = `cac5d26441dd33e9348151487e4df7b547195481` (2026-11-09). Lean sources were read only; nothing was built. Abbreviations:
- "Main:n" means `papers/Main.md` at line n of that commit.
- "OB/" means `verification/lean-mathlib/OIBridge/`.
- "[K]" means a kernel theorem on `main`. Its statement was read; the build was not rerun.
- "[A]" means a paper argument given in this file.
- "[X]" means an exact generic check in `checks.py`.
- "[D]" means a session draft off `main`. The table in §5 gives its status.

Labels for hypotheses are *justified* (follows from a stated source), *posited* (a stated premise of the corpus), and *open*.

***

## 0. Verdict

**What is and is not shown.** Under a configuration-law ontology, and for procedures whose outside degrees of freedom are prepared independently of the input (H-IND below), no operation changes configuration laws other than by a nonnegative kernel, so no fixed linear identification of states with configuration laws yields a non-diagonal-preserving transformation. This is a conditional result for the diagonal route C and the fixed-linear route E_f. It is not an impossibility result for operational quantum mechanics from deterministic OI: the routes with memory outside the identified carrier (C-dyn) and with nonlinear register encodings (E_r) are not decided.

The coordinator asked for two cases to be kept apart:
- **(i) access-model-independent:** the operation is absent for every procedure consistent with the named hypotheses, whatever the observer's access model;
- **(ii) interface-scoped:** the operation is absent only under the access model currently assumed.

No verdict below is an unconditional statement about OI. Each case-(i) verdict is conditional on three named hypotheses, and on the route:

| Hypothesis | Content | Status |
|---|---|---|
| **P-CONF** | The substratum is a finite set Ω of configurations; φ is a bijection of Ω; physical states are probability laws on Ω, with no amplitude-bearing state (H1–H3, §1.1). | **posited.** Sources: Main:44 (Definition), Main:56 (Lemma 3 and its measure remark), Main:62 (the bijective finite representative is a representation choice, and total finiteness is a physical posit carried in the ledger, Main:726ff), Main:720 ("the hidden sector is a classical substratum — a finite set with a deterministic bijection"). Main:720 also names a coherent-preparation and instrument bridge as open; whether Main's axioms entail H3 is not investigated here (§6). |
| **H4** | The observer, its apparatus and its records are coordinates of the configuration. | justified (Main:44 Definition, Lemma 2) |
| **H-IND** | In each procedure, the conditional law of every degree of freedom outside the identified carrier, given the carrier's configuration at the start, is fixed by the procedure and does not depend on the input law (H11, §1.1). | **posited.** It is the defining condition of route C ("no memory outside the identified carrier"). Where it fails, the route is C-dyn. |

Given these, T0 (§1.3) proves that the class 𝒦 of nonnegative kernel families contains every procedure. Exhaustiveness is therefore a theorem under P-CONF, H4 and H-IND, and a hypothesis-dependent statement otherwise.

| Question | Verdict | Case | Scope |
|---|---|---|---|
| **NX-1, route C** (the identified carrier is the configuration carrier; no memory outside it) | **Fails** | **(i)**, given P-CONF, H4, H-IND | Every dynamics φ, every partition, every fixed prior and every adaptive protocol (T0). Every complex-linear extension ("lift") of the induced maps to matrices. Every ε. Finite carriers. (T2) |
| **NX-1, route E_f** (a fixed, linear, injective identification of encoded states with configuration laws, under H-LIFT) | **Fails** | **(i)**, given P-CONF, H4, H-IND, H-LIFT and the linear identification | Same scope as route C. This restates MECH-2's Lemma F(b), generalized as APPROX r2 proposed, with its premise discharged by T0. (T3) |
| **NX-1, routes C-dyn / E_r** (memory outside the identified carrier; nonlinear ψ-ontic register encodings) | **Not decided** | Neither | No classical class is fixed for E_r here, and T0–T3 do not apply. Main's realization theorem (Main:566) represents the laws of a prescribed instrument family with one prescribed step map per instrument. That shows the laws are representable. It does not source a reusable intervention of an embedded observer that is consistent across preparations, contexts, composition and complete records. Two questions remain open: selection (Main:602, "What remains is selection") and native operational sourcing (§4, Q6). |
| **FI-1 as stated** (∃ a non-monomial admissible operator at level one in the generating class) | **Indeterminate** | Presentation-relative | FI-1 is not an invariant of the generated theory (T5). `genTheory CM` and `substratumTheory` are equal on every carrier (paper proof, not kernel-checked), and FI-1 holds for the first and fails for the second. FI-1 is therefore not fixed by 𝒦 or by any availability data. Under the kernel's minimal sourcing (`permClass`, least architecture containing the exchanges, `permClass_le_of_exchanges`), FI-1 **fails**, and that failure is case (ii). |
| **FI-1ᵘ(T)** (§1.4): an admissible **isometric** non-monomial step on a carrier T; FI-1ᵘ is FI-1ᵘ(S×Fin 1) | **Fails on the system and at every level** | **(i)**, given P-CONF, H4, H-IND | Every theory faithful to 𝒦 (T4). Its relation to NX-1 on route C is level-scoped (T7): an NX-1 branch on a carrier T gives FI-1ᵘ on an iterated-ancilla extension of T and a non-monomial admissible operator on T itself; FI-1ᵘ(T) gives an NX-1 branch on T. Level-one FI-1 follows from NX-1 only for a level-one branch. |

**Decisive lemmas.** T0: under P-CONF, H4 and H-IND every procedure acts on the carrier's laws by a nonnegative kernel per outcome. T1: the generated class 𝒩 lies in 𝒦. Hence:
- every linear lift of a branch preserves diagonal states (T2);
- every linear frame encoding of a branch is nonnegative (T3).

**For FI-1, the gap is a missing definition.** Neither Main, nor the Substratum paper, nor the kernel contains an *admissibility criterion*: a rule fixing which Kraus operators are "physical" from native content. The kernel takes the class 𝓘 as data, and the observer sourcing picks the least architecture by convention. Without such a rule, FI-1 is not a question about OI's physics.

**What would make NX-1 hold.** On routes C and E_f, at least one of the following has to be given up:
- H3 (states would carry amplitudes or other non-law content), together with a physically sourced non-monomial operation (§4, Q1a and Q1b; the kinematics alone is not sufficient);
- H-IND or H-LIFT (memory outside the identified carrier: route C-dyn);
- the fixed linear identification H10 (route E_r).

The last two retain a classical configuration law. On those routes NX-1 is not decided, and both a selection rule and a native sourcing of the intervention are owed. Candidates Q1–Q6 are in §4. None is adopted.

**Relation to the corpus.** APPROX r2's route-C failure and BRIDGE's "not supplied by the stated read/write access" were scoped to an access model. T0 and T2 replace that scope by the hypotheses P-CONF, H4 and H-IND. T5 is a structural finding, §A.31 classification **NEW**: FI-1 as formulated is not theory-invariant. T6 and the lift-underdetermination reading **elaborate** Main:720 ("The substratum alone does not fix the classification. Restricted to inputs diagonal in a fixed basis, every two-step process admits a classical-memory decomposition") and Main:590 (phases "as a stated intervention principle"). Correctness bands are unchanged: these are consistency results, and §A.23 applies.

***

## 1. The intervention class 𝒩

### 1.1 Hypotheses

| ID | Content | Status | Source |
|---|---|---|---|
| H1 | Ω is finite. | posited (total finiteness) | Main:62; ledger Main:726ff; kernel A1 `Substratum.A1` (OB/SubstratumInterfaceAudit.lean:84) |
| H2 | φ: Ω→Ω is a bijection, applied at integer times only. | posited (representation choice); integer time justified | Main:44 (discrete iteration x_t = φ^t(x_0)), Main:56, Main:62; K `a2_every_substratum` for the second-order form |
| H3 | Physical states are probability laws μ ∈ Δ(Ω); there are no amplitudes. | posited (part of P-CONF) | Main:56 measure remark ("the prior is a realization datum"); Main:720 |
| H4 | The observer is a proper subsystem. Its records are coordinates of the configuration: Ω = Ω_V × Ω_H, extended by registers as needed. | justified | Main:44 Definition, Lemma 2 |
| H5 | Preparation attaches fresh registers in any fixed law. | posited, taken in its broadest form | Main:56 (prior as datum). The kernel grants only uniform attachment (`prepAvail_uniform`, OB/OperationalAssembly.lean:630). Using the broadest form makes the negatives stronger. |
| H6 | Readout conditions on a value of a configuration coordinate: μ ↦ 1_{r=k}·μ. | justified | Main:44; Substratum Prop 24.5; K `internal_branch_eq_blockPart` as summarized at Main:592 (a passive internal observer can only apply record projections) |
| H7 | Discard marginalizes over registers. | justified | Main §1.4, the T_ij formula |
| H8 | Feed-forward and action-labelled control are φ acting on (record ⊗ system). | justified from H1, H2, H4 [A] | Main:564ff, the gluing theorem: one fixed bijection with an intervention register. The read-write families of the stated access are permutations (`ReadWriteFamily`; K `readWriteOperator_eq_perm`, used at OB/RouteB.lean:224), so they are instances of H2 on an enlarged carrier. |
| H9 | Coarse-graining sums outcome branches. | justified | standard |
| H10 | Route: C, or E_f (a linear injective L from encoded states to Δ(Ω_enc), with H-LIFT). | posited per route | APPROX r2 §4.2 [D]; MECH-2 node 2 on `main` |
| H11 | **H-IND.** A procedure fixes a kernel κ(r ∣ s): the conditional law of all degrees of freedom r outside the identified carrier (apparatus, registers, environment, the observer's own state), given the carrier configuration s at the procedure's start. κ is the same for every input law. | posited; the defining condition of route C | APPROX r2 §4.2's route split [D]. H5 is the special case κ(r ∣ s) = ν(r). On E_f, MECH-2's H-LIFT has the corresponding role; the exact relation between H-IND and H-LIFT is not audited here. X7 is a countercontrol: without a fixed κ the output is not a function of the input law. |

### 1.2 Definition

𝒩 is the set of finite outcome-indexed families (T_a)_a of linear maps on ℝ^Ω, for any finite Ω satisfying H1–H4, that are generated from four kinds of step by sequential composition, outcome-dependent continuation and coarse-graining:
- the permutation matrix of φ^t, for t ∈ ℕ (this covers φ^{-1}, since φ has finite order);
- attachment ⊗ν of a fixed law ν (H5);
- record projectors D_k = diag(1_{r=k}) (H6);
- marginalization (H7).

A **branch** is one T_a. The **induced map** on a subsystem is the attach, run, discard composite.

𝒦 is the set of finite outcome-indexed families (T_a)_a of entrywise nonnegative matrices from ℝ^{Ω_S} to ℝ^{Ω_S'} whose sum over a is column-stochastic. 𝒩 ⊆ 𝒦 by T1. The negative results below use only membership in 𝒦.

### 1.3 Exhaustiveness: every procedure induces a member of 𝒦

This is the *available ≠ derived* boundary. T1 is a statement about the defined class 𝒩. That every process an embedded observer can bring about is covered needs a separate argument, which is T0. It holds under the named hypotheses and is not claimed beyond them.

**Procedure.** Under H1–H4 a procedure on an identified carrier with configuration space Ω_S consists of:
- a total configuration space Ω_S × R, where R collects every other degree of freedom (H4);
- a kernel κ(r ∣ s), fixed by the procedure (H-IND);
- the dynamics φ on Ω_S × R (H2). Every act of the observer, including control conditioned on earlier records, is part of φ (H8);
- an outcome a, read from records at any times, and an output carrier configuration s′, read at a time that may depend on earlier records (H6).

**T0 (exhaustiveness under P-CONF, H4, H-IND) [A].** Every procedure induces a family in 𝒦: for an input law μ on Ω_S, the unnormalized law of the output on outcome a is T_a μ, with

T_a(s′ ∣ s) = Σ_r κ(r ∣ s) · 1[f(s, r) = s′] · 1[g(s, r) = a] ≥ 0.

*Proof.* By H3 the state at the start is the law μ(s)κ(r ∣ s) on Ω_S × R. The dynamics is a deterministic map, so the whole trajectory is a function of the initial pair (s, r). Records at any time are coordinates of the trajectory (H4, H6), so the outcome is a function g(s, r), and so is every record-dependent stopping time and the output configuration f(s, r). The joint law of (s′, a) is the pushforward of μ(s)κ(r ∣ s) under (f, g), which is the displayed formula. It is linear in μ because κ does not depend on μ. Each entry is a sum of nonnegative terms, and Σ_a Σ_{s′} T_a(s′ ∣ s) = Σ_r κ(r ∣ s) = 1. ∎

What T0 covers, and what it does not:
- **Adaptive record conditioning** is covered: it is part of φ and of g.
- **Preparation histories** are covered when they fix κ, including a κ correlated with s. A history that makes κ depend on the input law violates H-IND. Then the output is not a function of μ (X7), no linear map on carrier laws is defined, and the case is route C-dyn.
- **Postselection.** T_a is the unnormalized branch, the convention of the kernel's instrument families. The normalized conditional law T_a μ / ‖T_a μ‖₁ is not linear in μ, and it is still a law.
- **Composition.** A multi-step protocol is one procedure from its start. Between two steps that reuse the same outside degrees of freedom, the conditional law of r given s generally depends on μ, so the second step alone need not be a procedure in this sense. Composition inside 𝒩 uses freshly attached registers.
- **No observer access model is assumed.** The kernel's read/write access (`obsTheory`), the cell posits of QP class N and MECH-2's operation set are special cases.
- **Not covered:** a state that is not a law on Ω (failure of H3); a record or apparatus that is not a configuration coordinate (failure of H4); routes C-dyn and E_r.

The kernel's availability predicate (`FiniteOperationalTheory.availExt`, OB/OperationalAssembly.lean:599) is **not** used as a source of operations. It is uninterpreted until a class 𝓘 is fixed through `genTheory` (OB/ImplementationLocality.lean:852). Its isometric step `InstAvail.op` requires Kᴴ K = 1 (:268–272), and that requirement is a modeling rule, not a native derivation.

### 1.4 Lifts, faithfulness, and FI-1ᵘ

Route C treats an operation as a ℂ-linear map Φ on `Matrix Ω Ω ℂ`. Native states are the diagonal matrices diag(μ).
- **Lift.** A lift of a real-linear map T on laws is any ℂ-linear Φ with Φ(diag μ) = diag(Tμ) for every law μ.
- **Faithful theory.** A `FiniteOperationalTheory` is faithful to 𝒦 when every branch of every available family, on the system and at every level, is a lift of a branch of a family in 𝒦. By T0 this is the form of "available only if realized by a procedure" under P-CONF, H4 and H-IND.
- **FI-1** (BRIDGE-UNIT1 §5.1 [D, accepted]; the conclusion of K `exists_nonMonomial_of_layerFlowExecutable`): ∃ K on S×Fin 1 with 𝓘 K and ¬IsMonomial K, for the generating architecture 𝓘.
- **FI-1ᵘ(T):** ∃ K on the carrier T with 𝓘 K, Kᴴ K = 1 and ¬IsMonomial K. Then `InstAvail.op K` applies, so conj K is realized on T. **FI-1ᵘ** without an argument is FI-1ᵘ(S×Fin 1), the isometric form of FI-1. In `genTheory` the system carrier is S and level n is S×Fin n; a derivation that uses `discard` passes through carriers (S×Fin n)×Fin m₁×…, which are not levels.
- **NX-1** (APPROX r2 §4.2 [D, under review]): some valid native procedure induces a transformation at an ε-independent positive distance from the route's classical class. On route C that class is `PreservesDiag` (OB/DiagonalTheory.lean:68). On E_f it is the maps with an entrywise nonnegative frame matrix.

***

## 2. Proofs and counterexamples

**T1 (native nonnegativity) [A].** Every branch in 𝒩 is an entrywise nonnegative matrix on ℝ^Ω. Every complete family sums to a column-stochastic matrix.

*Proof.* The generators are nonnegative: a permutation matrix, ⊗ν with ν ≥ 0, a 0/1 diagonal, and a 0/1 marginal sum. Composites, outcome-dependent continuations and coarse-grained sums of nonnegative matrices are nonnegative. Column sums: permutations, attachment of a probability law and marginalization preserve total mass, and the record projectors for all values of a coordinate sum to the identity. ∎

[X5, the last entry, is a trivial instance only.] This is the premise MECH-2 Lemma F's proof uses, "each operation is a nonnegative matrix on laws" (MECH-2 DESIGN node 2, on `main`). T1 states it for 𝒩 with arbitrary priors, any φ and any partition. T1 concerns the generated class only; T0 (§1.3) is the statement that procedures are covered.

**T2 (route C: NX-1 fails, independently of the lift) [A].** Let Φ be any ℂ-linear lift of a real-linear map T on laws, in particular of a branch of a family in 𝒦. Then `PreservesDiag Φ`.

*Proof.* `PreservesDiag Φ` quantifies over all complex w (OB/DiagonalTheory.lean:68–69). Write w = Σ_s w_s e_s. Then Φ(diag w) = Σ_s w_s Φ(diag e_s) = Σ_s w_s diag(T e_s) = diag(T w). ∎

So the distance from the classical class is 0 for every lift, every ε and every horizon. The same holds for an induced system map: attaching a law, applying T and the partial trace each send diagonal matrices to diagonal matrices.

Hence NX-1(C) fails for every procedure: **case (i), given P-CONF, H4 and H-IND** (T0). By contrast, APPROX r2 §4.2 and BRIDGE §5.1 derive this failure for configuration-level architectures and for the stated read/write access, which is case (ii). T0 and T2 replace the restriction to that interface by the three named hypotheses. T2 uses only the linearity of T on laws, which T0 derives from H-IND.

**T3 (route E_f: NX-1 fails) [A].** Let L be linear and injective with Span(L(encoded states)) = ℝ^{Ω_enc} (informationally complete), and let H-LIFT hold. If a branch T of a family in 𝒦 induces the encoded map E by L∘E = T∘L, then the frame matrix of E is T, which is unique by injectivity and spanning, and T ≥ 0 entrywise (T0; T1 for 𝒩). So E lies in the E_f classical class. ∎

This is MECH-2 Lemma F(b), extended from an orthogonal frame to any linear injective frame, as APPROX r2 proposed for the SIC frame. The extension uses only nonnegativity and linearity.

**Control.** The frame matrix of the identity is a permutation. The Hadamard's frame matrix under R1 has minimum entry −1/2 [X5]. The class is therefore non-vacuous, and the target is at positive distance from it, which agrees with APPROX's G3.

**Scope.** Without H-LIFT the carrier law does not fix later statistics (MECH-2 node 7). That case is route C-dyn or E_r, which T3 does not cover.

**T4 (FI-1ᵘ fails on the system and at every level of a faithful theory) [A from K and X3].** Suppose a theory faithful to 𝒦 had conj K available on the system or at level n, with K square, Kᴴ K = 1 and ¬IsMonomial K.
- A unitary is non-monomial exactly when its conjugation fails `PreservesDiag`. One direction is K `preservesDiag_conj_of_monomial` (OB/SubstratumInterface.lean:126). The other is BRIDGE K2 [D, accepted]; for 2×2 it is re-checked in X3, where the off-diagonal of U e₀e₀ᴴ Uᴴ is −A·B·e^{−iφ}, nonzero exactly when both entries of the column are nonzero.
- In general: a non-monomial unitary has a column with two nonzero entries u_i, u_j. Then (K e_c e_cᴴ Kᴴ)_{ij} = u_i ū_j ≠ 0.

So conj K is not diagonal-preserving. That contradicts T2 for the branch it lifts. ∎

**T5 (FI-1 is not theory-invariant) [A from K, X1 and X2].** Let CM be the column-monomial class: at most one nonzero entry in each column.

(a) **CM is an `Architecture`** (fields at OB/ImplementationLocality.lean:506–516):
- `one`: the identity has one nonzero entry per column.
- `mul`: column j of KL is K·(L e_j) = L_{ij}·K e_i for the single i, which has at most one nonzero entry.
- `smul`: scaling preserves the support.
- `proj`: diagonal matrices are CM.
- `block`: column t of `ancBlock K f e` is column (t,e) of K restricted to rows (·,f), which has at most one nonzero entry.

This re-derives APPROX r2 C1 [D] independently.

(b) **A CM isometry is monomial.** Kᴴ K = 1 gives every column norm 1, so every column has exactly one nonzero entry, of modulus 1. Two columns whose entries sit in the same row r have inner product conj(K_{ra})K_{rb} ≠ 0. So the rows are distinct, the support is a permutation, and K = permMatrix σ · diagonal d. That is `IsMonomial`, which allows any d (OB/SubstratumInterface.lean:75). X1 enumerates supports for n ≤ 4; it encodes the same counting argument and serves as a support-level control, not independent evidence.

(c) **`InstAvail CM T O F ↔ InstAvail substratumClass T O F`, by induction on the constructors** (OB/ImplementationLocality.lean:268–289).
- From substratumClass to CM: `instAvail_mono`, since monomial matrices are CM.
- From CM to substratumClass, constructor by constructor:
  - `op`: K is CM and an isometry, so K is monomial by (b).
  - `readout`: the reindexed `readProj` is a 0/1 diagonal transported by a bijection. It lies in substratumClass by `substratumClass_arch.proj` and `substratumClass_labelInvariant`.
  - `coarse`, `bind`, `discard`: structural.

The `genTheory` fields `avail`, `availExt`, `prepAvail` and `readout` (:852ff) are defined from `InstAvail` and `localLuders` alone. So **`genTheory CM` = `substratumTheory`** (OB/RouteB.lean:284) on every carrier, by propositional extensionality.

(d) **FI-1 holds for CM and fails for substratumClass.** For CM, K = |0⟩(⟨0|+⟨1|)/√2 on S×Fin 1 is CM and not monomial. Its conjugation preserves diagonals [X2, the support equivalence; X4b, an instance]. It is never an isometric step: X4b shows it is not an isometry, and (b) applies. For substratumClass every element is monomial by definition. ∎

Two classes that generate the same theory therefore disagree on FI-1. FI-1 is a property of the presentation, not of what is available. Its operational content is FI-1ᵘ (T4, T7).

This strengthens APPROX r2's "FI-1 ⇏ NX-1" counter-model. That counter-model showed CM fails NX-1. T5 shows CM's theory *is* the substratum theory. Not kernel-checked.

**T6 (the phase principle is invisible on native states) [A from K].**
- On diagonal inputs, every branch of `substratumTheory` and of `permTheory` acts as a branch of a family in 𝒦.
- The two theories induce the same set of families on laws: replace each monomial isometric step P·D by P. Conjugation by P·D with |d| = 1 acts on diag(μ) as P does [X4a for the phase alone]. Every constructor preserves diagonals, so restrictions compose.
- Yet `substratumTheory` has `PhasesAvailable` (K `substratumTheory_derivedOI`) and `permTheory` does not (K `permTheory_not_phasesAvailable`).

So whether phases are available is not fixed by the action on laws. This elaborates Main:590 ("as a stated intervention principle rather than a consequence of its finite states and bijective dynamics"). It refines that statement: under P-CONF, the phase principle has no native operational content without a state-mixing operation. That is consistent with K `obligations_independent` (OB/C5Discovery.lean:59).

**T7 (architecture-generated theories: level-scoped relations between NX-1(C), FI-1ᵘ and FI-1) [A, induction on `InstAvail`].** Let 𝓘 be an `Architecture`. Write T for the carrier of a realized family: S on the system, S×Fin n at level n. The statements are one-directional and are not combined into an equivalence (§A.34).

- **(a) NX-1(C) on T ⇒ FI-1ᵘ on an iterated-ancilla extension of T.** Suppose a branch of a family realized on T fails `PreservesDiag`. Then some `op` step in its derivation fails it:
  - `readout` steps are conjugations by reindexed 0/1 diagonals, which preserve diagonals;
  - `coarse` sums, `bind` composites and `discard` (uniform attachment, then partial trace) preserve `PreservesDiag`;
  - so if every `op` step preserved diagonals, the branch would too.

  The offending `op` step is an isometric K ∈ 𝓘 that is not monomial (contrapositive of `preservesDiag_conj_of_monomial`). Its carrier is T×Fin m₁×…×Fin m_k, where k ≥ 0 is the number of `discard` constructors above the step. This is FI-1ᵘ(T×Fin m₁×…×Fin m_k). It is FI-1ᵘ(T) only when k = 0, and FI-1ᵘ at level one only when in addition T = S×Fin 1. An offending step on an extension need not give an offending branch on T: for 1⊗H on S×Fin 2 the conjugation fails diagonal preservation, and its discard is the identity [X6b].
- **(b) NX-1(C) on T ⇒ a non-monomial admissible operator on T (not necessarily isometric).** *Lemma.* Every branch of a family realized on T is a finite sum Σ_i conj(M_i) with every M_i ∈ 𝓘(T) (the kernel's `Realized`, OB/ImplementationLocality.lean:250). Induction on the constructors:
  - `op`, `readout`: one term, admissible by the constructor's hypothesis;
  - `coarse`: a sum of such sums;
  - `bind`: conj(N)∘conj(M) = conj(NM), admissible by `mul`;
  - `discard`: K `discardWith_uniform_conjChannel` (OB/AncillaClosure.lean:461) gives discard(conj M) = m⁻¹ Σ_{f,e} conj(`ancBlock` M f e) [X6a for S = 2, m = 2], and m⁻¹·conj(B) = conj(m^{−1/2}B), admissible by `block` and `smul`.

  A sum of diagonal-preserving maps preserves diagonals (K `preservesDiag_add`). So a branch on T that fails `PreservesDiag` has a term conj(M) that fails it, and then M is not column-monomial [the entry computation of T4; X2], hence not monomial. With T = S×Fin 1 this is FI-1: **a level-one NX-1 branch gives FI-1.**
- **(c) FI-1ᵘ(T) ⇒ NX-1(C) on T.** If K ∈ 𝓘(T) is a non-monomial isometry (hence unitary), then conj K is realized on T (`InstAvail.op`) and is not diagonal-preserving (T4's argument).
- **Not proved: NX-1(C) ⇒ FI-1 for a branch on the system or at a level n ≠ 1.** (b) gives a non-monomial admissible operator on S or on S×Fin n, not on S×Fin 1. For a branch on the system, the step to level one is `SystemToLevelOne` (OB/LevelOneSeam.lean:116), which is a stated principle; the reverse step, from level one to the system, is the theorem `avail_of_availExt_one` (:107) [K]. Under `SystemToLevelOne` a system NX-1 branch transports to a level-one branch (transport along a bijection of the carrier preserves failure of `PreservesDiag`), and (b) then gives FI-1. Whether `SystemToLevelOne` is derivable for `genTheory` of a relabelling-invariant architecture was not checked. For a level n > 1 no such step is available here. The general implication is open.
- **Not claimed:** that FI-1 (without "isometric") implies NX-1. T5 refutes it.

***

## 3. Directional relation table (route C unless stated; §A.34)

| Implication | Status | Witness / counter-witness |
|---|---|---|
| P-CONF, H4, H-IND ⇒ every procedure induces a family in 𝒦 | proved [A] | T0 |
| 𝒩 ⊆ 𝒦 | proved [A] | T1 |
| P-CONF, H4 without H-IND ⇒ the output is a function of the input law | false | X7 |
| faithful to 𝒦 ⇒ ¬NX-1(C) | proved [A] | T2 |
| ¬NX-1(C) ⇒ faithful to 𝒦 | false | Φ(diag w) = diag(−w) preserves diagonals and lifts no nonnegative matrix [A] |
| faithful (E_f, H-LIFT, linear injective L) ⇒ ¬NX-1(E_f) | proved [A]; = MECH-2 Lemma F(b), generalized | T3 |
| faithful ⇒ ¬FI-1ᵘ(T), T the system or any level | proved [A from K and X3] | T4 |
| faithful ⇒ ¬FI-1 | **false** | `genTheory CM` is faithful and has FI-1 (T5; paper proof) |
| faithful ⇒ FI-1 | **false** | `permTheory` / `substratumTheory` (T5) |
| NX-1(C) on T ⇒ FI-1ᵘ on some T×Fin m₁×…×Fin m_k, k ≥ 0 | proved [A] | T7(a) |
| NX-1(C) on T ⇒ FI-1ᵘ(T) | not proved; the offending isometric step may sit on a proper extension | T7(a) |
| a non-diagonal-preserving isometric step on T×Fin m ⇒ its discard on T fails `PreservesDiag` | false | 1⊗H on S×Fin 2: the discard is the identity (X6b) |
| NX-1(C) on T ⇒ a non-monomial admissible operator on T | proved [A from K `discardWith_uniform_conjChannel`] | T7(b) |
| NX-1(C) at level one ⇒ FI-1 | proved [A] | T7(b) with T = S×Fin 1 |
| NX-1(C) on the system, with `SystemToLevelOne` ⇒ FI-1 | proved [A], conditional on the stated principle `SystemToLevelOne` (OB/LevelOneSeam.lean:116) | T7 |
| NX-1(C) on the system or at level n ≠ 1 ⇒ FI-1 | open | T7 |
| level-one availability ⇒ system availability (after transport) | [K] `avail_of_availExt_one` (OB/LevelOneSeam.lean:107) | |
| FI-1ᵘ(T) ⇒ NX-1(C) on T | proved [A] | T7(c) |
| FI-1 ⇒ NX-1(C) | false | CM (APPROX r2 [D]; T5) |
| FI-1 is determined by the generated theory | false | T5 |
| PhasesAvailable is determined by the native restriction | false | T6 |
| layer-flow executability ⇒ NX-1(C) | proved [K composed] | K `gateFlow_half_not_preservesDiag` (OB/LiftAudit.lean:155), `gateFlow_unitary` |
| NX-1(C) ⇒ layer-flow executability | false | K `polarizedTheory_swap_half_level_one` (OB/C5Discovery.lean:325), `polarizedTheory_not_layerFlowExecutable` (OB/PolarizationClosure.lean:395) |
| layer-flow executability is compatible with faithfulness to 𝒦 | false | layer-flow executability ⇒ NX-1 ⇒ not faithful (T2) |
| `obsTheory 𝒮` ⊆ `substratumTheory` | [K] `obs_availExt_le_substratum` (OB/SubstratumInterfaceAudit.lean:837) | Both are faithful to 𝒦 [A]. That is case (ii) evidence, consistent with the case (i) result under P-CONF, H4 and H-IND. |

***

## 4. Candidate added principles (none adopted; §A.29 scoring)

**Controls any revision must preserve, stated in advance:**
- (c1) S⇔D⇔Q_fb at the finite-law level (Main:602, item 1; K `finite_horizon_equivalence`);
- (c2) C4 ⇔ readout-relevant hidden predictive memory (Main:602, item 2);
- (c3) C3 necessity;
- (c4) Substratum Prop 24.4: the passive quotient and permutation similarity;
- (c5) K `obligations_independent` and `routeB_target`, the separation results;
- (c6) the classical-dimension obstruction (Main:602, item 3).

**Scoring, per §A.29:**
- **P:** which controls it preserves;
- **I:** an independent prediction or postdiction beyond supplying FI-1 or NX-1;
- **S:** what else must be physically sourced before the candidate supplies the operation;
- **V:** whether it can be adjusted to fit any outcome.

| ID | Principle | What it is meant to supply; S | P | I | V | Score |
|---|---|---|---|---|---|---|
| Q1a | **P-AMP (kinematics):** replace H3; states are vectors in ℂ^Ω and φ is unitary. | By itself neither NX-1 nor FI-1ᵘ. With φ the identity or a permutation unitary every step is monomial and preserves diagonals (K `preservesDiag_conj_of_monomial`). **S:** Q1b. | (c1) holds as S⇔Q; D's meaning and (c4)'s passive-classical reading change; this contradicts Main:720's structural claim. | none identified | none needed: it supplies no operation | not sufficient |
| Q1b | **P-AMP-OP:** with Q1a, a non-monomial unitary step that an embedded observer can apply as a controlled operation on the carrier concerned. | NX-1 on that carrier and FI-1ᵘ on it (T7(c)); level-one FI-1 only if the step is at level one. **S:** the step itself, its controllability by the observer, and its reuse across preparations and contexts. | as Q1a | none identified beyond QM itself | the unitary is free: adjustable | fails hard-to-vary; it is QM by fiat |
| Q2 | **P-FLOW:** layer gates are time-one points of physical continuous flows that can be stopped at intermediate times. | executability ⇒ NX-1, FI-1ᵘ | Breaks H2's integer time. gateFlow(½) fails diagonal preservation (K `gateFlow_half_not_preservesDiag`), so on routes C and E_f it lifts no family in 𝒦 (T2). It needs non-law state content (Q1a, with the flow as Q1b) or a route outside C and E_f, where sourcing is open. | none; with the phase it is equivalent to QM (Main:590, K `derivedOI_qm_iff_layerFlowExecutable'`), which is the problem it was built to fix | the continuous time parameter: adjustable | fails; Main:590 already classes this as an "empirical controllability resource" |
| Q3 | **P-POL:** the Weil/polarization identification of the per-site V×V (C5 candidate 2). | NX-1 at level one on the polarized carrier (K `polarizedTheory_swap_half_level_one`); FI-1 | Under a linear law identification, T3 forces nonnegativity, so P-POL must leave route E_f: either its states carry non-law content (Q1a), or the identification is nonlinear (E_r) with the configuration law kept, where sourcing is open. | yes, a definite consequence: a countable repertoire with no layer flow (K `polGen_countable_upToScalar`, `polarizedTheory_not_layerFlowExecutable`) | fairly rigid (choice of Lagrangian only) | the most hard-to-vary candidate. Its prediction (no continuously tunable operation) is testable against raw-direct data; that comparison is not made here. It still needs H3 or the linear identification to be given up. |
| Q4 | **P-ADM:** an admissibility rule; the class is the least architecture containing the native isometries and record projectors. | settles FI-1, negatively | all controls preserved; matches the kernel's `permClass_le_of_exchanges` convention | none; it is a convention | canonical | well defined, but supplies no non-classical operation. It removes FI-1's indeterminacy, with FI-1 false. |
| Q5 | **P-NB:** a non-bijective, state-mixing observer coupling (Main:590; OB/StateMixingCoupling.lean:7, "the datum is a postulate"). | NX-1, FI-1ᵘ | Breaks H2 at observer level. Under H3 and H-IND a non-bijective map of laws is still a nonnegative matrix, so on routes C and E_f P-NB supplies nothing; it needs Q1a or a route outside C and E_f. | none | the datum is free | fails |
| Q6 | **P-SEL:** a selection principle placing the substratum in a ψ-ontic register encoding (route E_r) | Not NX-1 on C or E_f. Whether an analogue of NX-1 holds on E_r is not decided. **S:** a selection rule, and a native sourcing of the intervention as a reusable operation of an embedded observer (consistent across preparations, contexts, composition and complete records). Main's realization theorem prescribes one step map per instrument and does not supply the second. | consistent with (c1)–(c6) for the laws it represents (Main:566) | none stated; Main:602 calls this "selection" | depends on the instrument data: adjustable unless the selection is derived | open; not scorable until a selection rule and a sourcing argument are stated |

**Assumption-watch marker (§A.31 cross-propagation).** Any premise of the form "operation X is available on the configuration carrier" whose content is not fixed by its action on diagonal laws carries no OI-native content under P-CONF, H4 and H-IND. That covers phases, admissible-class membership, and Kraus decompositions. Such a premise should be audited as a choice of lift, not as physics. Candidates to re-check: `PhasesAvailable` in `DerivedOI` (OB/RouteB.lean), `SubstratumAvail` (OB/LiftAudit.lean), and BRIDGE's open source 2 ("whether every realization of the lift's channels is configuration-level").

***

## 5. Off-main references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| APPROX-UNIT1.md r2 [D, under review], session working file (on branch `ccr-9c2ecca4-vkb666` at `820519cf`, `handoff-20261109/1216-approx/`) | NX-1's definition and its route split (C, E_f, E_r, C-dyn); the CM counter-model; NX-1 ⇒ FI-1 | **Support off `main`, a gap.** The NX-1 definition and the route split are used as given. CM's Architecture property and the level-scoped relations between NX-1 and FI-1 are re-derived here (T5a, T7), so those links do not rest on it. r2's unscoped "NX-1 ⇒ FI-1" is not used: T7(b) proves it for a level-one branch only. Under §A.46 item 7 it is an unverified premise until accepted. |
| BRIDGE-UNIT1.md [D, independently accepted], session working file (on branch `ccr-9c2ecca4-vkb666` at `820519cf`, `handoff-20261109/1211-bridge/`) | FI-1's definition; K2 (for unitaries, non-monomial ⇔ state-mixing) | **Support off `main`, a gap.** The FI-1 definition is used as given. K2 is re-derived in general (T4 proof) and checked at 2×2 (X3). |
| ASSESS-1059.md (accepted r6a) and ASSESS-868.md (accepted r3a) | none | **Provenance only.** Named in the task brief; not consulted; no claim uses them. |
| #1224 SEL-ACCESS-1 (PR #1224, off `main`) | motivation in the brief (selection from passive data does not force a repertoire) | **Provenance only.** No claim here uses it. T5 and T6 make a parallel point for active native data, derived independently. |
| #1169, #1216 r2 (issue and comment) | task routing and the Lean anchor list | **Provenance only.** |
| #1216 comment 6793397036 (independent non-author review of APPROX r2) | T7's scope: NX-1 ⇒ FI-1 at level one only; `SystemToLevelOne` a stated principle, `avail_of_availExt_one` a theorem | **Provenance only.** T7(b) derives the level-one statement here, and the two Lean declarations were read on `main` (OB/LevelOneSeam.lean:107, :116). |
| PR #1230 review 5857231398 (ChatGPT, relayed by the owner) | the r2 revisions | **Provenance only.** Each finding was checked against the sources and proofs here; `DISPOSITIONS-r2.md`. |
| `checks.py`, `checks.out` in this directory | X1–X7 | **Support off `main`, a gap.** The checks back illustrative instances and countercontrols of T0, T2–T5 and T7. The main arguments are paper proofs. |
| MECH-2 DESIGN, APPARATUS-1 DESIGN | Lemma F's operation set and proof (T3) | **On `main`** (`verification/programmes/oi-qm/reconstruction/…`). MECH-2's status is "proposal" (its §0). Lemma F's proof is a three-line nonnegativity argument re-derived here as T1/T3. APPARATUS-1 was only skimmed (its section index) and is not used. |
| Substratum.md Prop 24.4 | the passive predictive structure is classical (background) | **On `main`** (`cac5d264`, Substratum.md:331). |

***

## 6. Not done

- **No kernel formalization or build.** T0 is a paper proof. T5(c) (`genTheory CM = substratumTheory`), T6 and T7 are paper inductions over `InstAvail`. They are natural kernel targets, and no claim here says they are kernel-checked.
- **Infinite carriers, continuum limits, and the quasilocal completion** (Main:590, last sentence) are not treated. T1 extends to Koopman-type actions of measure-preserving maps on densities (standard), but no literature search was done (audit Step 4 is skipped).
- **Routes C-dyn and E_r** are not decided. Neither a selection principle nor a native sourcing of a reusable intervention (Q6) is formulated. No verdict here bears on whether such a route succeeds or fails.
- **H-IND's status is a posit.** Whether OI's own account of preparation makes the outside degrees of freedom independent of the input law is not investigated. Where it fails, T0 does not apply.
- **NX-1 ⇒ FI-1 beyond level one** is open (T7), as is the derivability of `SystemToLevelOne` for architecture-generated theories.
- **H-LIFT** is used as MECH-2 states it. Its own justification, and its exact relation to H-IND, are not re-audited.
- **P-CONF's status is a posit.** Whether Main's two axioms entail H3 (no amplitude-bearing states) rather than posit it is not investigated. If H3 is not entailed, the case (i) verdicts hold only relative to it.
- **No manuscript propagation.** If accepted, T2's scope strengthening and T5's non-invariance bear on GR:270, Main:590 and BRIDGE §5.1's wording of FI-1. A propagation round would be separate.
- **No raw-direct empirical comparison** for Q3's countable-repertoire consequence.
- **X1 and X5's nonnegativity entry** encode the arguments they check, so they are controls, not independent evidence. X2–X4 and X6 are independent symbolic checks; X6a re-checks one instance of a kernel theorem. X7 is a two-point countercontrol for H-IND.
