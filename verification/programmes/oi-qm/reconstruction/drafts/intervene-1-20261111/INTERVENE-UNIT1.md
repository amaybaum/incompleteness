# INTERVENE-1, unit 1: which operations do OI's own rules make physically available?

**WIP / UNVERIFIED.** This is a paper-only unit for #1169, owner-approved on 2026-11-11 in the coordinating session. It authorizes nothing. It adopts no physical premise, edits no manuscript, writes nothing to git or GitHub, and computes no OI mechanism. It has not been independently reviewed. Its only computations are the generic exact checks X1–X5 in `checks.py` in this directory, run with `python3 -I -B`.

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

The coordinator asked for two cases to be kept apart:
- **(i) absent from OI itself:** no intervention class consistent with Main's posits supplies the operation;
- **(ii) interface-scoped:** the operation is absent only under the access model currently assumed.

Each verdict says which case it is in, and names the posit the line between them depends on.

**The dividing posit, P-CONF.** The substratum is a finite set Ω of configurations. φ is a bijection of Ω. Physical states are probability laws on Ω, with no amplitude-bearing state.
- Sources: Main:44 (Definition), Main:56 (Lemma 3 and its measure remark), Main:62 (the bijective finite representative is a representation choice, and total finiteness is a physical posit carried in the ledger, Main:726ff), and Main:720 ("the hidden sector is a classical substratum — a finite set with a deterministic bijection").
- Status: **posited.**

Every case-(i) statement below is conditional on P-CONF and on nothing about an observer access model.

| Question | Verdict | Case | Scope |
|---|---|---|---|
| **NX-1, route C** (the identified carrier is the configuration carrier; no memory outside it) | **Fails** | **(i)**, given P-CONF | Every dynamics φ, every partition, every prior and every adaptive protocol in the native class 𝒩 (§1). Every complex-linear extension ("lift") of the induced maps to matrices. Every ε. Finite carriers. (T2) |
| **NX-1, route E_f** (a fixed, linear, injective identification of encoded states with configuration laws, under H-LIFT) | **Fails** | **(i)**, given P-CONF, H-LIFT and the linear identification | Same scope as route C. This restates MECH-2's Lemma F(b), generalized as APPROX r2 proposed, with its premise discharged for all of 𝒩. (T3) |
| **NX-1, routes C-dyn / E_r** (memory outside the identified carrier; nonlinear ψ-ontic register encodings) | **Not decided; not the operative question** | Neither | No classical class is fixed for E_r. Main's simulator realizes the laws there (Main:566–602), and the remaining gap is *selection* (Main:602, "What remains is selection"). No operational lemma is missing; what is missing is a selection principle (§4, Q6). |
| **FI-1 as stated** (∃ a non-monomial admissible operator at level one in the generating class) | **Indeterminate, and irreducibly so** | Inherently interface-relative | FI-1 is not an invariant of the generated theory (T5). `genTheory CM` and `substratumTheory` are equal on every carrier, and FI-1 holds for the first and fails for the second. FI-1 is therefore not fixed by 𝒩 or by any availability data. Under the kernel's minimal sourcing (`permClass`, least architecture containing the exchanges, `permClass_le_of_exchanges`), FI-1 **fails**, and that failure is case (ii). |
| **FI-1ᵘ**, the theory-invariant sharpening of FI-1 (§1.4): an admissible **isometric** non-monomial step at level one | **Fails** | **(i)**, given P-CONF | Every lift faithful to 𝒩 (T4). In architecture-generated theories FI-1ᵘ is equivalent to NX-1 on route C up to level bookkeeping (T7). |

**Decisive lemma.** The negative verdicts all rest on T1 (native nonnegativity). Every branch of every native intervention acts on configuration laws as an entrywise nonnegative matrix. Hence:
- every linear lift of it preserves diagonal states (T2);
- every linear frame encoding of it is nonnegative (T3).

**For FI-1, there is no missing lemma; the gap is a missing definition.** Neither Main, nor the Substratum paper, nor the kernel contains an *admissibility criterion*: a rule fixing which Kraus operators are "physical" from native content. The kernel takes the class 𝓘 as data, and the observer sourcing picks the least architecture by convention. Without such a rule, FI-1 is not a question about OI's physics.

**What would make NX-1 hold.** Only a revision of P-CONF. Its states would have to carry amplitudes (or another non-law content), or the identification would have to leave the linear-law routes. Candidates Q1–Q6 are in §4. None is adopted.

**Relation to the corpus.** T2 strengthens the scope of an existing negative: APPROX r2's route-C failure and BRIDGE's "not supplied by the stated read/write access" were interface-scoped, and T2 removes that scope. T5 is a new structural finding, the §A.31 classification **NEW**: FI-1 as formulated is not theory-invariant. T6 and the lift-underdetermination reading **elaborate** Main:720 ("The substratum alone does not fix the classification. Restricted to inputs diagonal in a fixed basis, every two-step process admits a classical-memory decomposition") and Main:590 (phases "as a stated intervention principle"). Correctness bands are unchanged: these are consistency results, and §A.23 applies.

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

### 1.2 Definition

𝒩 is the set of finite outcome-indexed families (T_a)_a of linear maps on ℝ^Ω, for any finite Ω satisfying H1–H4, that are generated from four kinds of step by sequential composition, outcome-dependent continuation and coarse-graining:
- the permutation matrix of φ^t, for t ∈ ℕ (this covers φ^{-1}, since φ has finite order);
- attachment ⊗ν of a fixed law ν (H5);
- record projectors D_k = diag(1_{r=k}) (H6);
- marginalization (H7).

A **branch** is one T_a. The **induced map** on a subsystem is the attach, run, discard composite.

### 1.3 Completeness of 𝒩 relative to the posits

This is the *available ≠ derived* boundary. Under H1–H4 nothing exists but configurations and φ.
- An embedded observer's "act" is part of the configuration trajectory: H4 and H8.
- What it can know or condition on is a configuration record: H6.
- Any process it brings about therefore maps laws by pushforward along φ^t, conditioning on records, mixing over prepared registers and marginalization.

So every physical process of an embedded observer under P-CONF induces a member of 𝒩 [A, given P-CONF]. **No observer access model is assumed.** The kernel's read/write access (`obsTheory`), the cell posits of QP class N and MECH-2's operation set are each special cases.

The kernel's availability predicate (`FiniteOperationalTheory.availExt`, OB/OperationalAssembly.lean:599) is **not** used as a source of operations. It is uninterpreted until a class 𝓘 is fixed through `genTheory` (OB/ImplementationLocality.lean:852). Its isometric step `InstAvail.op` requires Kᴴ K = 1 (:268–272), and that requirement is a modeling rule, not a native derivation.

### 1.4 Lifts, faithfulness, and FI-1ᵘ

Route C treats an operation as a ℂ-linear map Φ on `Matrix Ω Ω ℂ`. Native states are the diagonal matrices diag(μ).
- **Lift.** A lift of a native branch T is any linear Φ with Φ(diag μ) = diag(Tμ) for every law μ.
- **Faithful theory.** A `FiniteOperationalTheory` is faithful to 𝒩 when every branch of every available family, at every level, is a lift of a branch of 𝒩. Faithfulness is the precise form of "available only if derived from the posits".
- **FI-1** (BRIDGE-UNIT1 §5.1 [D, accepted]; the conclusion of K `exists_nonMonomial_of_layerFlowExecutable`): ∃ K on S×Fin 1 with 𝓘 K and ¬IsMonomial K, for the generating architecture 𝓘.
- **FI-1ᵘ:** the same, with Kᴴ K = 1 added. Equivalently, `InstAvail.op K` applies, so conj K is an available level-one operation.
- **NX-1** (APPROX r2 §4.2 [D, under review]): some valid native procedure induces a transformation at an ε-independent positive distance from the route's classical class. On route C that class is `PreservesDiag` (OB/DiagonalTheory.lean:68). On E_f it is the maps with an entrywise nonnegative frame matrix.

***

## 2. Proofs and counterexamples

**T1 (native nonnegativity) [A].** Every branch in 𝒩 is an entrywise nonnegative matrix on ℝ^Ω. Every complete family sums to a column-stochastic matrix.

*Proof.* The generators are nonnegative: a permutation matrix, ⊗ν with ν ≥ 0, a 0/1 diagonal, and a 0/1 marginal sum. Composites, outcome-dependent continuations and coarse-grained sums of nonnegative matrices are nonnegative. Column sums: permutations, attachment of a probability law and marginalization preserve total mass, and the record projectors for all values of a coordinate sum to the identity. ∎

[X5, the last entry, is a trivial instance only.] This is the premise MECH-2 Lemma F's proof uses, "each operation is a nonnegative matrix on laws" (MECH-2 DESIGN node 2, on `main`). T1 states it for 𝒩 with arbitrary priors, any φ and any partition.

**T2 (route C: NX-1 fails, independently of the lift) [A].** Let Φ be any ℂ-linear lift of a branch T of 𝒩. Then `PreservesDiag Φ`.

*Proof.* `PreservesDiag Φ` quantifies over all complex w (OB/DiagonalTheory.lean:68–69). Write w = Σ_s w_s e_s. Then Φ(diag w) = Σ_s w_s Φ(diag e_s) = Σ_s w_s diag(T e_s) = diag(T w). ∎

So the distance from the classical class is 0 for every lift, every ε and every horizon. The same holds for an induced system map: attaching a law, applying T and the partial trace each send diagonal matrices to diagonal matrices.

Hence NX-1(C) fails for all of 𝒩: **case (i) given P-CONF.** By contrast, APPROX r2 §4.2 and BRIDGE §5.1 derive this failure for configuration-level architectures and for the stated read/write access, which is case (ii). T2 shows the restriction to that interface was not needed.

**T3 (route E_f: NX-1 fails) [A].** Let L be linear and injective with Span(L(encoded states)) = ℝ^{Ω_enc} (informationally complete), and let H-LIFT hold. If a native branch T induces the encoded map E by L∘E = T∘L, then the frame matrix of E is T, which is unique by injectivity and spanning, and T ≥ 0 entrywise by T1. So E lies in the E_f classical class. ∎

This is MECH-2 Lemma F(b), extended from an orthogonal frame to any linear injective frame, as APPROX r2 proposed for the SIC frame. The extension uses only T1 and linearity.

**Control.** The frame matrix of the identity is a permutation. The Hadamard's frame matrix under R1 has minimum entry −1/2 [X5]. The class is therefore non-vacuous, and the target is at positive distance from it, which agrees with APPROX's G3.

**Scope.** Without H-LIFT the carrier law does not fix later statistics (MECH-2 node 7). That case is route C-dyn or E_r, which T3 does not cover.

**T4 (FI-1ᵘ fails for every faithful lift) [A from K and X3].** Suppose a faithful theory had conj K available at level n, with K square, Kᴴ K = 1 and ¬IsMonomial K.
- A unitary is non-monomial exactly when its conjugation fails `PreservesDiag`. One direction is K `preservesDiag_conj_of_monomial` (OB/SubstratumInterface.lean:126). The other is BRIDGE K2 [D, accepted]; for 2×2 it is re-checked in X3, where the off-diagonal of U e₀e₀ᴴ Uᴴ is −A·B·e^{−iφ}, nonzero exactly when both entries of the column are nonzero.
- In general: a non-monomial unitary has a column with two nonzero entries u_i, u_j. Then (K e_c e_cᴴ Kᴴ)_{ij} = u_i ū_j ≠ 0.

So conj K is not diagonal-preserving. That contradicts T2 for its native branch. ∎

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
- On diagonal inputs, every branch of `substratumTheory` and of `permTheory` is a native branch.
- The two theories induce the same set of native families: replace each monomial isometric step P·D by P. Conjugation by P·D with |d| = 1 acts on diag(μ) as P does [X4a for the phase alone]. Every constructor preserves diagonals, so restrictions compose.
- Yet `substratumTheory` has `PhasesAvailable` (K `substratumTheory_derivedOI`) and `permTheory` does not (K `permTheory_not_phasesAvailable`).

So whether phases are available is not fixed by 𝒩. This elaborates Main:590 ("as a stated intervention principle rather than a consequence of its finite states and bijective dynamics"). It refines that statement: under P-CONF, the phase principle has no native operational content without a state-mixing operation. That is consistent with K `obligations_independent` (OB/C5Discovery.lean:59).

**T7 (in architecture-generated theories, NX-1(C) and FI-1ᵘ match up to level) [A, induction on `InstAvail`].** Each direction is stated separately (§A.34).
- **(⇒)** Suppose a branch of `genTheory 𝓘 arch S` at level n fails `PreservesDiag`. Then some `op` step in its derivation fails it:
  - `readout` steps are conjugations by reindexed 0/1 diagonals, which preserve diagonals;
  - `coarse` sums, `bind` composites and `discard` (uniform attachment, then partial trace) preserve `PreservesDiag`;
  - so if every `op` step preserved diagonals, the branch would too.
  The offending `op` step is an isometric K ∈ 𝓘 that is not monomial (contrapositive of `preservesDiag_conj_of_monomial`), on a carrier S×Fin n×Fin m₁×… reached through discards. This is FI-1ᵘ at *that* carrier, and at level one when no discard intervenes. It refines APPROX r2's "NX-1 ⇒ a non-monomial admissible operator at some level" by adding "isometric".
- **(⇐)** If K ∈ 𝓘 on S×Fin n is a non-monomial isometry (hence unitary), then conj K is available at level n (`InstAvail.op`) and is not diagonal-preserving (T4's argument). This is NX-1(C) at level n.
- **Not claimed:** that FI-1 (without "isometric") implies NX-1. T5 refutes it.

***

## 3. Directional relation table (route C unless stated; §A.34)

| Implication | Status | Witness / counter-witness |
|---|---|---|
| P-CONF ⇒ every induced map is nonnegative on laws | proved [A] | T1 |
| faithful to 𝒩 ⇒ ¬NX-1(C) | proved [A] | T2 |
| ¬NX-1(C) ⇒ faithful to 𝒩 | false | Φ(diag w) = diag(−w) preserves diagonals but is not a native branch [A] |
| faithful (E_f, H-LIFT, linear injective L) ⇒ ¬NX-1(E_f) | proved [A]; = MECH-2 Lemma F(b), generalized | T3 |
| faithful ⇒ ¬FI-1ᵘ | proved [A from K and X3] | T4 |
| faithful ⇒ ¬FI-1 | **false** | `genTheory CM` is faithful and has FI-1 (T5) |
| faithful ⇒ FI-1 | **false** | `permTheory` / `substratumTheory` (T5) |
| NX-1(C) ⇒ FI-1ᵘ (at the carrier of the offending step) | proved [A] | T7 ⇒ |
| FI-1ᵘ at level n ⇒ NX-1(C) at level n | proved [A] | T7 ⇐ |
| NX-1(C) ⇒ FI-1 | proved via FI-1ᵘ ⇒ FI-1 | APPROX r2 [D]; T7 |
| FI-1 ⇒ NX-1(C) | false | CM (APPROX r2 [D]; T5) |
| FI-1 is determined by the generated theory | false | T5 |
| PhasesAvailable is determined by the native restriction | false | T6 |
| layer-flow executability ⇒ NX-1(C) | proved [K composed] | K `gateFlow_half_not_preservesDiag` (OB/LiftAudit.lean:155), `gateFlow_unitary` |
| NX-1(C) ⇒ layer-flow executability | false | K `polarizedTheory_swap_half_level_one` (OB/C5Discovery.lean:325), `polarizedTheory_not_layerFlowExecutable` (OB/PolarizationClosure.lean:395) |
| layer-flow executability is compatible with faithfulness | false | layer-flow executability ⇒ NX-1 ⇒ not faithful (T2) |
| `obsTheory 𝒮` ⊆ `substratumTheory` | [K] `obs_availExt_le_substratum` (OB/SubstratumInterfaceAudit.lean:837) | Both are faithful to 𝒩 [A]. That is case (ii) evidence subsumed by case (i). |

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
- **V:** whether it can be adjusted to fit any outcome.

| ID | Principle | What it supplies | P | I | V | Score |
|---|---|---|---|---|---|---|
| Q1 | **P-AMP:** replace H3; states are vectors in ℂ^Ω and φ is unitary. | NX-1, FI-1ᵘ | (c1) holds as S⇔Q; D's meaning and (c4)'s passive-classical reading change; this contradicts Main:720's structural claim. | none identified beyond QM itself | the unitary is free: adjustable | fails hard-to-vary; it is QM by fiat |
| Q2 | **P-FLOW:** layer gates are time-one points of physical continuous flows that can be stopped at intermediate times. | executability ⇒ NX-1, FI-1ᵘ | Breaks H2's integer time. The output of gateFlow(½) on a configuration is not a law, so it also needs Q1. | none; with the phase it is equivalent to QM (Main:590, K `derivedOI_qm_iff_layerFlowExecutable'`), which is the problem it was built to fix | the continuous time parameter: adjustable | fails; Main:590 already classes this as an "empirical controllability resource" |
| Q3 | **P-POL:** the Weil/polarization identification of the per-site V×V (C5 candidate 2). | NX-1 at level one on the polarized carrier (K `polarizedTheory_swap_half_level_one`); FI-1 | Under a linear law identification, T3 forces nonnegativity, so P-POL must leave route E_f. Its states then need non-law content, i.e. Q1. | yes, a definite consequence: a countable repertoire with no layer flow (K `polGen_countable_upToScalar`, `polarizedTheory_not_layerFlowExecutable`) | fairly rigid (choice of Lagrangian only) | the most hard-to-vary candidate. Its prediction (no continuously tunable operation) is testable against raw-direct data; that comparison is not made here. It still needs a P-CONF revision. |
| Q4 | **P-ADM:** an admissibility rule; the class is the least architecture containing the native isometries and record projectors. | settles FI-1, negatively | all controls preserved; matches the kernel's `permClass_le_of_exchanges` convention | none; it is a convention | canonical | well defined, but supplies no non-classical operation. It removes FI-1's indeterminacy, with FI-1 false. |
| Q5 | **P-NB:** a non-bijective, state-mixing observer coupling (Main:590; OB/StateMixingCoupling.lean:7, "the datum is a postulate"). | NX-1, FI-1ᵘ | Breaks H2 at observer level. Under H3 a non-bijective map of laws is still nonnegative (T1), so P-NB also needs Q1. | none | the datum is free | fails |
| Q6 | **P-SEL:** a selection principle placing the substratum in a ψ-ontic register encoding (route E_r) | not NX-1; it bypasses NX-1 (§0) | consistent with (c1)–(c6) by construction (Main's simulator) | none stated; Main:602 calls this "selection" | depends on the instrument data: adjustable unless the selection is derived | open; not scorable until a selection rule is stated |

**Assumption-watch marker (§A.31 cross-propagation).** Any premise of the form "operation X is available on the configuration carrier" whose content is not fixed by its action on diagonal laws carries no OI-native content under P-CONF. That covers phases, admissible-class membership, and Kraus decompositions. Such a premise should be audited as a choice of lift, not as physics. Candidates to re-check: `PhasesAvailable` in `DerivedOI` (OB/RouteB.lean), `SubstratumAvail` (OB/LiftAudit.lean), and BRIDGE's open source 2 ("whether every realization of the lift's channels is configuration-level").

***

## 5. Off-main references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| APPROX-UNIT1.md r2 [D, under review], session working file (on branch `ccr-9c2ecca4-vkb666` at `820519cf`, `handoff-20261109/1216-approx/`) | NX-1's definition and its route split (C, E_f, E_r, C-dyn); the CM counter-model; NX-1 ⇒ FI-1 | **Support off `main`, a gap.** The NX-1 definition and the route split are used as given. CM's Architecture property and NX-1 ⇒ FI-1ᵘ are re-derived here (T5a, T7), so those links do not rest on it. Under §A.46 item 7 it is an unverified premise until accepted. |
| BRIDGE-UNIT1.md [D, independently accepted], session working file (on branch `ccr-9c2ecca4-vkb666` at `820519cf`, `handoff-20261109/1211-bridge/`) | FI-1's definition; K2 (for unitaries, non-monomial ⇔ state-mixing) | **Support off `main`, a gap.** The FI-1 definition is used as given. K2 is re-derived in general (T4 proof) and checked at 2×2 (X3). |
| ASSESS-1059.md (accepted r6a) and ASSESS-868.md (accepted r3a) | none | **Provenance only.** Named in the task brief; not consulted; no claim uses them. |
| #1224 SEL-ACCESS-1 (PR #1224, off `main`) | motivation in the brief (selection from passive data does not force a repertoire) | **Provenance only.** No claim here uses it. T5 and T6 make a parallel point for active native data, derived independently. |
| #1169, #1216 r2 (issue and comment) | task routing and the Lean anchor list | **Provenance only.** |
| `checks.py`, `checks.out` in this directory | X1–X5 | **Support off `main`, a gap.** The scratch checks back T2–T5's illustrative instances. The main arguments are paper proofs. |
| MECH-2 DESIGN, APPARATUS-1 DESIGN | Lemma F's operation set and proof (T3) | **On `main`** (`verification/programmes/oi-qm/reconstruction/…`). MECH-2's status is "proposal" (its §0). Lemma F's proof is a three-line nonnegativity argument re-derived here as T1/T3. APPARATUS-1 was only skimmed (its section index) and is not used. |
| Substratum.md Prop 24.4 | the passive predictive structure is classical (background) | **On `main`** (`cac5d264`, Substratum.md:331). |

***

## 6. Not done

- **No kernel formalization or build.** T5(c) (`genTheory CM = substratumTheory`), T6 and T7 are paper inductions over `InstAvail`. They are natural kernel targets, and no claim here says they are kernel-checked.
- **Infinite carriers, continuum limits, and the quasilocal completion** (Main:590, last sentence) are not treated. T1 extends to Koopman-type actions of measure-preserving maps on densities (standard), but no literature search was done (audit Step 4 is skipped).
- **Routes C-dyn and E_r** are not decided. A selection principle (Q6) is not formulated.
- **H-LIFT** is used as MECH-2 states it. Its own justification is not re-audited.
- **P-CONF's status is a posit.** Whether Main's two axioms entail H3 (no amplitude-bearing states) rather than posit it is not investigated. That is the precise place where the verdicts in case (i) could become case (ii).
- **No manuscript propagation.** If accepted, T2's scope strengthening and T5's non-invariance bear on GR:270, Main:590 and BRIDGE §5.1's wording of FI-1. A propagation round would be separate.
- **No raw-direct empirical comparison** for Q3's countable-repertoire consequence.
- **X1 and X5's nonnegativity entry** encode the arguments they check, so they are controls, not independent evidence. X2–X4 are independent symbolic checks.
