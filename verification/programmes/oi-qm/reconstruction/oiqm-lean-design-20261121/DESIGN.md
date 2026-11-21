# OIQM-LEAN: Lean proof designs for the open P1 links (QM ⊆ OI)

**Standing.** WIP / UNVERIFIED. Research and design record for #1169 (P1, the inclusion QM ⊆ OI). It
contains Lean *designs*: statements, dependencies and proof plans. No `.lean` file is added, nothing
was built, no theorem is proved here, no extension E or sector condition C is adopted, and no status
changes. Every statement below marked "design" is unproved. Base: `origin/main` at `df6da1c6`. Lean
paths are under `verification/lean-mathlib/OIBridge/` and were read at that base. Mathlib is the tag
pinned by `verification/lean-mathlib/lakefile.toml` (`v4.33.0`), and every Mathlib name cited was
checked against that tag's source.

**Inputs read.** The target I, I-1 to I-4: GATE-A-AMEND r4 §5.1 at `3a1c8e97` (branch
`research/gate-a-amendment-1169-20261114`, read only; #1289 closed unmerged). The interface
`J_exact(A)` and the admission schema: `oi-qm-ext-1/endpoints.md` (blob `d9d92e03`, written `EP:n`
below). The owner's ordering for this record (#1169 c.7064859041) is interfaces first, so the order
is: O1 and O3 interfaces (§2, §3), then the target clauses (§4), then O2 (§5).

**Classification used (#1169 c.7064843184).**
- (N): the statement would be a theorem from OI's native assumptions alone.
- (I): the statement is conditional on imported quantum or operational assumptions. Each import is
  named, together with the place where the Lean statement makes it explicit (a hypothesis, a structure
  field, or the type of a field).

No design in this record is (N). §6.2 says why, and where the imports enter first.

**Not overlapped.** The BQP Lean ladder (`research/bqp-p2-20261121`), the Theorem 24 Lean sketch
(`research/thm24-def-20261121`) and the mathematics thread on unbounded carriers
(`research/oiqm-unbounded-20261121`) are cross-references only. None of their content was read or
used here. Nothing in this record depends on the A1 retirement (#1477) having landed. §6.3 marks the
designs that need cardinality neutrality.

## 0. Answers to the three questions

| | Established (with layer) | Assumed (imported) | Missing |
|---|---|---|---|
| O1, coherent operation | [K] Under the closure `DerivedOI`, exact finite endomorphic QM holds iff one layer flow is executable: `derivedOI_qm_iff_layerFlowExecutable'` (DerivedQ3.lean:222). The phase-free form is `oiPlusMin_iff_qm` (MinimalRepertoire.lean:569). The substratum and every configuration-level class execute no such flow (LiftAudit.lean:183, :200). | Complex matrix kinematics (the type of every channel). The closure's `PhasesAvailable` conjunct (RouteB.lean:148, stipulated). Implementation generation of availability. | A native procedure realizing the flow. Before that, the realization relation itself, from native procedures to complex channels, which the kernel lacks entirely (§2.1). |
| O3, preparation, readout and records | [K] The readout form is derived from existence and spectator independence (`readout_is_localLuders`, OperationalAssembly.lean:658). Pure seeds are derived from a uniform attach, a readout, feed-forward and ancilla swaps (`pureSeedPrep_available_of_swap`, :675). | The structure fields of `FiniteOperationalTheory` (:594): uniform attach, readout existence and locality, bind (feed-forward through a retained record) and discard. The trace rule as the native law. | Native procedures for each field. A typed record interface. A native law bridge (§3). |
| I-1 to I-4 | Nothing typed. `J_exact(A)` has no Lean form on `main`, and no module defines a history law over adaptive protocols. | The comparator, which is complex QM by definition (EP:110). E, as a predicate parameter. | The vocabulary of §4.1. The exclusion, by E, of the ψ-complete countermodel of §4.3. |
| O2, one model over unbounded carriers | [K] An implementation class is one rule for every finite carrier, and `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136) gives exact QM on every carrier from one class. The quasilocal completion is unique given its stages (QuasilocalCharacterization.lean:168, `canon_unique`), which is uniqueness and not an equivalence. | The same imports as O1 and O3, plus a spectator law for the infinite remainder. | Single-model law equality across regions, carrier encodings, and spectator inertness of the infinite remainder (§5). |

## 1. What was verified from the status map

The status map relied on is unreviewed. The following of its citations were re-read at `df6da1c6`
and hold as stated:
- L3: GeneralCarrier.lean:93 and :100, and PhysicalCharacterization.lean:295 and :301.
- L4: CarrierGeneralOIPlus.lean:191, :198 and :213, and MinimalRepertoire.lean:569 and :578.
- L5: StructuralClosure.lean:397 and :406, and LiftAudit.lean:117 and :200.
- DerivedQ3.lean:214 and :222.
- Equivalence.lean:422 and :462.
- QuasilocalCharacterization.lean:168, and InstrumentAvailability.lean:335.
- Main:568: the finite-substratum obstruction, whose factorization half is stated for one fixed
  realization with N < ∞ ontic configurations.

One citation adds to the map: `PairFlowEquivalence.qm_iff_derivedOI_pairFlowSourced`
(PairFlowEquivalence.lean:199). It is a kernel-only iff on `Fin 2` between exact QM and `DerivedOI`
plus one sourced real pair flow. It is a third O1 plug point (§2.3).

## 2. D-O1: the typed interface of coherent operation (priority 1)

**Classification: (I).** The interface is the exact statement that a future physical source has to
satisfy. It is not a claim that one exists.

### 2.1 The missing layer: from native procedures to channels

Every existing conditional theorem quantifies over `T : FiniteOperationalTheory S` (OperationalAssembly.lean:594). In such a `T`, availability is a bare predicate on complex-linear maps `Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ`. No kernel object links a native OI procedure, meaning a loading of Ω followed by Φ and a record extraction, to such a map. A physical source therefore cannot plug into `derivedOI_qm_iff_layerFlowExecutable'` until that link is typed. The design types it as a structure whose fields are the imports:

```lean
namespace OIBridge.OIQMInterface
open OperationalAssembly LevelOneSeam MonoidalCompletion

/-- DESIGN. A native operational source on a finite carrier `S`: native procedures at each
ancilla level, their finite outcome sets, and the REALIZATION MAP sending each procedure's
branches to complex channels. The realization map is the import Coh-1 (EP ledger row 1): the
codomain `Matrix … ℂ →ₗ[ℂ] …` is complex matrix kinematics, supplied and not derived. -/
structure NativeSource (S : Type) [Fintype S] [DecidableEq S] where
  Proc  : ℕ → Type                                   -- native procedures on S × Fin n
  Out   : ∀ {n}, Proc n → Type
  [fOut : ∀ {n} (P : Proc n), Fintype (Out P)]
  [dOut : ∀ {n} (P : Proc n), DecidableEq (Out P)]
  branch : ∀ {n} (P : Proc n), Out P →
    (Matrix (S × Fin n) (S × Fin n) ℂ →ₗ[ℂ] Matrix (S × Fin n) (S × Fin n) ℂ)   -- import Coh-1
```

The derived availability is `RealizedExt src n O F := ∃ (P : src.Proc n) (e : src.Out P ≃ O), F = src.branch P ∘ e.symm`. The system-level `avail` is read through the level-one identification already used by `SystemToLevelOne`. A theory `src.toTheory : FiniteOperationalTheory S` is defined by taking `availExt := RealizedExt`. Building it needs exactly the remaining structure fields of `FiniteOperationalTheory`, and those are the O3 obligations (§3). So O3 is typed upstream of O1: no O1 statement can be made about a native source until the O3 fields are supplied.

### 2.2 The O1 obligation, in two forms

Plug point A is the closure plus a layer flow (DerivedQ3). Plug point B is the phase-free minimal repertoire (MinimalRepertoire).

```lean
/-- DESIGN, plug point A. The source supplies the closure and one layer flow of an involution
with a moved configuration. `DerivedOI` (RouteB.lean:148) carries `PhasesAvailable` as a
stipulated conjunct: an IMPORT unless sourced. -/
structure CoherentSourceA (S) [Fintype S] [DecidableEq S] (src : NativeSource S) (O3 : O3Fields src) :
    Prop where
  closure : RouteB.DerivedOI (src.toTheory O3)
  σ : Equiv.Perm S
  invol : ∀ x, σ (σ x) = x
  moved : ∃ x, σ x ≠ x
  flow : LiftAudit.LayerFlowExecutable (src.toTheory O3) σ   -- ∀ n t, availExt n Unit (conj (gateFlow (levelPerm σ n) t))

theorem qm_of_coherentSourceA [Nonempty S] (src) (O3) (h : CoherentSourceA S src O3) :
    ExactAllFiniteEndomorphicQuantumOps (src.toTheory O3)
-- proof: obtain ⟨x, hx⟩ := h.moved; exact DerivedQ3.qm_of_derivedOI_layerFlowExecutable _ h.closure h.invol hx h.flow

/-- DESIGN, plug point B (no phase hypothesis). Implementation locality, embedded observation,
and at every level one continuously driven pair together with all exchanges. -/
structure CoherentSourceB (S) [Fintype S] [DecidableEq S] (src : NativeSource S) (O3 : O3Fields src) :
    Prop where
  locality    : ImplementationLocality (src.toTheory O3)            -- ImplementationLocality.lean:370
  observation : EmbeddedObservation (src.toTheory O3)               -- EmbeddedObservation.lean:123
  rich        : MinimalRepertoire.PhaseFreeRichness (src.toTheory O3) -- MinimalRepertoire.lean:423

theorem qm_of_coherentSourceB [Nonempty S] (src) (O3) (h : CoherentSourceB S src O3) :
    ExactAllFiniteEndomorphicQuantumOps (src.toTheory O3)
-- proof: MinimalRepertoire.qm_of_oiPlusMin _ ⟨h.locality, h.rich, h.observation⟩
```

**The physical content, stated as native existence claims.**
- Under plug point B, `rich` unfolds to the following. For every n with `2 ≤ card (S × Fin n)`
  there is a pair `a ≠ b` such that, for every `t : ℝ`, some `P : src.Proc n` with a one-point
  outcome set has `src.branch P () = conjChannel (flow (transition a b) t)`
  (`flow` is ReachabilitySeam.lean:95 and `transition` is LieRankSource.lean:199). Each exchange
  `conjChannel (permMatrix (Equiv.swap a b))` must likewise be realized.
- Under plug point A, the flow has to be realized only as the *parallel* layer flow
  `gateFlow (levelPerm σ n) t` (LiftAudit.lean:47 and :51), but `PhasesAvailable` is required as
  well.

**A design-level reading (unproved, for review).** The two plug points trade the phases for addressability:
- Plug point A asks for the flow in its context-natural form, the same involution on every ancilla
  copy. That is what `ContextStable` (ImplementationLocality.lean:359) propagates. It then consumes
  the phases to isolate one pair (DerivedQ3 T1 and T2). The necessity of phases on this route is the
  cited `flow_endpoint_refuted` (FlowEndpoint.lean:149).
- Plug point B needs no phase, but asks for a *single* addressable pair at *every* level. Context
  stability alone does not produce that: tensoring with `1` gives n parallel copies, not one pair.
- Whether a context-stable source of a single-level pair flow implies `PhaseFreeRichness` at every
  level is an open design question. It is a candidate first lemma, D-O1.L1, with an unknown answer.

**Hidden assumption exposed (assumption-watch AW-LEAN-1).** `ImplementationLocality` demands `ImplementationGenerated T 𝓘` (ImplementationLocality.lean:352). That is, native availability must *coincide* with the closure `InstAvail 𝓘` of single admissible operators under the rules `op`, `readout`, `coarse` and `bind` (:268). A physical source therefore has to show more than that it realizes the flow. It also has to show that it realizes nothing outside the generated closure, which is a soundness-type closure statement about the whole native repertoire. This conjunct belongs to the interface and is easy to lose when "a source of the flow" is described informally.

### 2.3 Plug point C on Fin 2, and the direction structure

- On `Fin 2`, `qm_iff_derivedOI_pairFlowSourced` (PairFlowEquivalence.lean:199) gives a third plug
  point. `PairFlowSourced` (:48) asks for one real pair flow realized at every level and time.
- The existing iffs keep their kernel direction witnesses (§A.34):
  - for `derivedOI_qm_iff_layerFlowExecutable'`, ⇒ is `layerFlowExecutable_of_control` after
    `physical_of_exactAll`, and ⇐ is `qm_of_derivedOI_layerFlowExecutable`;
  - for `oiPlusMin_iff_qm`, ⇒ is `oiPlusMin_of_qm` and ⇐ is `qm_of_oiPlusMin`.
- The new interface theorems `qm_of_coherentSource{A,B}` are **one-directional by design**. The
  converse, that exact QM yields some native source satisfying the interface, holds trivially with the
  full class (`qm_generated_by_substratum_extension`, StructuralClosure.lean:406, uses `fullClass`).
  It is designed only as the **positive control** D-O1.C+ (`coherentSourceB_of_qm`), which shows that
  the interface is nonvacuous. That control matters: KERNEL-VAC-1 found an interface predicate that
  was empty (`ReadWriteNonvacuity`).
- The **negative control** D-O1.C− uses the substratum source:
  - `substratumTheory_not_layerFlowExecutable` (LiftAudit.lean:200) and `substratumGen_not_control`
    (StructuralClosure.lean:330) show that it fails the flow obligation;
  - `nonnegBounded_verdict` (FrozenSourcing.lean) covers every theory inside the ceiling.

### 2.4 Summary of D-O1

- **Dependencies.**
  - Kernel: MinimalRepertoire, DerivedQ3, RouteB, LiftAudit, ImplementationLocality and
    EmbeddedObservation.
  - Mathlib: only what those modules already import. That includes `Matrix.conjTranspose` and
    `Equiv.Perm`, and `Matrix.unitaryGroup` (Mathlib/LinearAlgebra/UnitaryGroup.lean:60) for the
    unitarity side conditions.
- **Hardest step.** Mathematically nothing: `qm_of_coherentSource{A,B}` are repackagings. The hard
  part of the Lean work is defining `toTheory` so that its fields typecheck. The dependent
  `Out P ≃ O` reindexing of `RealizedExt`, and its interaction with `availExt_coarse` and
  `availExt_bind`, is the only nontrivial proof obligation, and it moves to O3.
- **Expected axioms.** `propext`, `Classical.choice` and `Quot.sound`, as for DerivedQ3. No new
  `axiom`. Every import is a structure field or a hypothesis.
- **What it would establish.** The exact list of native existence claims that would make the existing
  conditional theorems apply to a physical source, with the AW-LEAN-1 coincidence conjunct included.
- **What it would not establish.** Any source; any physical justification of the realization map; the
  phases.
- **Cost.** One small module importing existing ones. Its own elaboration is light, but any Lean work
  runs in CI on the Mathlib bridge (§A.40).

## 3. D-O3: the typed interface of preparation, readout and records (priority 1)

**Classification: (I).** The imports are the following, each a field of `O3Fields`:
- (i) uniform ancilla attach;
- (ii) the existence of a spectator-independent basis readout;
- (iii) feed-forward through a retained classical outcome;
- (iv) attach, run and discard;
- (v) the trace law, as a law bridge.

```lean
/-- DESIGN. The fields a native source must supply before `toTheory` exists. Each mirrors one
field of `FiniteOperationalTheory` (OperationalAssembly.lean:594) and is stated on NATIVE
procedures, with the realized channel read through `src.branch`. -/
structure O3Fields {S} [Fintype S] [DecidableEq S] (src : NativeSource S) where
  idP      : ∀ n, ∃ P : src.Proc n, …  branch P = fun _ => LinearMap.id                    -- avail_id
  coarse   : ∀ n P (f : src.Out P → O'), ∃ P', … coarse-grained branches                    -- availExt_coarse
  bind     : ∀ n P (Q : src.Out P → src.Proc n), ∃ R, … branch R (a, b) = (branch (Q a) b).comp (branch P a)
             -- availExt_bind: RECORD RETENTION is implicit here (the next procedure reads outcome a)
  prep     : ∀ n, (Matrix S S ℂ →ₗ[ℂ] Matrix (S × Fin n) (S × Fin n) ℂ) → Prop              -- prepAvail
  prep_uniform : ∀ n, prep (n + 1) (uniformAttach (n + 1))                                  -- import (i)
  readoutP : ∀ n, src.Proc n
  readout_out : ∀ n, src.Out (readoutP n) ≃ Fin n
  readout_local : ∀ n k, MapSpectatorIndependent (ludersLift k) (branch (readoutP n) …)     -- import (ii)
  discard  : …                                                                               -- import (iv)

/-- DESIGN. The native law bridge (Meas-1, EP ledger rows 8–9): the native probability of branch
`a` of `P` on a native preparation realizing `ρ` is the trace of the realized branch. This is the
Born/trace rule as an IMPORT; deriving it is O6 and is not attempted. -/
structure LawBridge {S} [Fintype S] [DecidableEq S] (src : NativeSource S) where
  nativeProb : ∀ {n} (ρ : Matrix (S × Fin n) (S × Fin n) ℂ) (P : src.Proc n), src.Out P → ℝ
  trace_rule : ∀ {n} ρ P a, ρ.PosSemidef → ρ.trace = 1 →
    nativeProb ρ P a = (Matrix.trace (src.branch P a ρ)).re                                 -- import (v)
```

**What the kernel already removes from the O3 burden.** These are cited, not re-designed.
- A source need not supply the Lüders *form* of its readout. Existence plus spectator independence
  forces it (`readout_is_localLuders`, OperationalAssembly.lean:658).
- A source need not supply a pure ready state.
  - `pureSeedPrep_available_of_swap` (:675) derives `pureAttach` from three things: the uniform
    attach, the readout, and the ancilla swap corrections fed forward on the outcome.
  - The swaps are permutation matrices, which are monomial (`monomial_permMatrix`,
    SubstratumInterface.lean:60). They therefore lie inside `substratumClass`
    (StructuralClosure.lean:162) and need no O1 resource.

**A design-level reading, offered for review against PR1 (`RC/prep-regress-1-20261119/RESULT.md`).**
- The kernel's pure-seed derivation sends the ancilla's entropy into the classical outcome that
  `bind` conditions on. So, in the kernel, the record that `bind` retains is the non-invariant sink
  that PR1 says any escape from its no-ready-state result requires.
- If this reading survives review, O3's preparation obligation reduces to the record obligation. The
  remaining native task is a persistent, re-readable record, which MQ AW-MQ-2 and the M5 decision
  record as not passed, together with feed-forward. A ready-state supply would not be a separate
  task.
- This is a reading of two records against each other. Nothing here proves it.

**Typed records for §4.** `FiniteOperationalTheory` has no record object: outcome labels are only indices, and their retention is presupposed by `availExt_bind`. EP:40 requires five record operations: append, retain, repeated read without change, conditioning, and relabel or coarse-grain. In the history-law vocabulary of §4.1 these are carried by the protocol tree, where later nodes are functions of the whole past, and by the native record map `R`. D-I.R1 is therefore a design obligation: native retention means that `R` restricted to a prefix is invariant under every later step. Without that, the tree semantics silently imports perfect classical memory.

**Directions.** No iff is designed. The O3 fields are the *premises* of the existing structure, so the only direction is O3Fields → `toTheory` exists. **Expected axioms.** Standard three. **Cost.** Small to medium. The `bind` field's dependent outcome types (`Σ`, or `src.Out P × …` via an equivalence) are the hardest typing step.

## 4. D-I: the clauses I-1 to I-4 of the target

**Classification: (I).** The comparator is complex QM by definition (EP:110), and E is a parameter. This is the import structure the target itself prescribes. I-3 says that a clause that is not physically sourced makes the inclusion conditional.

### 4.1 Vocabulary (design; none exists on `main`)

```lean
/-- Carriers of J_exact(A): A × Fin (k+1), matching the indexing of `ExactCompositeQuantumOps`
(AncillaClosure.lean:364). -/
abbrev Car (A : Type) (k : ℕ) := A × Fin (k + 1)

structure DensLabel (S : Type) [Fintype S] [DecidableEq S] where
  ρ : Matrix S S ℂ
  psd : ρ.PosSemidef          -- Matrix.PosSemidef, Mathlib/LinearAlgebra/Matrix/PosDef.lean:59
  tr  : ρ.trace = 1           -- Matrix.trace, Mathlib/LinearAlgebra/Matrix/Trace.lean:45

/-- A finite-outcome endomorphic instrument label, in the normal form of
`IsFiniteEndomorphicKrausInstrument` (KrausSoundness.lean:112). -/
structure InstrLabel (A : Type) [Fintype A] [DecidableEq A] (k m : ℕ) where
  r : ℕ
  K : Fin (r + 1) → Matrix (Car A k) (Car A k) ℂ
  out : Fin (r + 1) → Fin m
  norm : ∑ i, (K i)ᴴ * K i = 1

/-- Finite adaptive protocols with level changes. `attach` uses the fixed join
(A × Fin n) × Fin m ≃ A × Fin (n*m) of EP:33. The tree form makes every later choice a function
of the entire retained past (EP:39–40). -/
inductive Prot (A : Type) [Fintype A] [DecidableEq A] : ℕ → Type
  | stop    {k} : Prot A k
  | inst    {k} (m : ℕ) (L : InstrLabel A k m) (next : Fin m → Prot A k) : Prot A k
  | attach  {k} (m : ℕ) (σ : DensLabel (Fin (m + 1))) (next : Prot A (joinLevel k m)) : Prot A k
  | discard {k} (m : ℕ) (h : k = joinLevel k' m) (next : Prot A k') : Prot A k

/-- Histories of a protocol: the outcome paths of the tree. -/
inductive Hist : Prot A k → Type | …

/-- The comparator law of EP:110, by unnormalized-state propagation: `inst` applies
`instrumentBranch L.K L.out a` (MonoidalCompletion.lean:731), `attach` tensors with σ and
reindexes (`Matrix.kroneckerMap`, Mathlib/LinearAlgebra/Matrix/Kronecker.lean:55; `Matrix.reindex`,
Mathlib/LinearAlgebra/Matrix/Defs.lean:526), `discard` is `ptraceAnc` (OperationalAssembly.lean:453),
and `stop` returns `(Matrix.trace ρ).re`. -/
noncomputable def qLaw : {k : ℕ} → Matrix (Car A k) (Car A k) ℂ → (π : Prot A k) → Hist π → ℝ
```

A native model follows the schema of EP:73–100:

```lean
structure NativeModel (A : Type) [Fintype A] [DecidableEq A] where
  Ω : Type u
  [mΩ : MeasurableSpace Ω]
  Φ : Ω ≃ᵐ Ω                        -- MeasurableEquiv (Mathlib/MeasureTheory/MeasurableSpace/Embedding.lean:179)
  Λs : Type u
  [mΛ : MeasurableSpace Λs]
  μ : ∀ {k}, DensLabel (Car A k) → MeasureTheory.Measure Λs
  [prob : ∀ {k} p, MeasureTheory.IsProbabilityMeasure (μ (k := k) p)]
  ι : ∀ {k}, DensLabel (Car A k) → Prot A k → Λs → Ω     -- loading
  R : ∀ {k} (π : Prot A k), (ℕ → Ω) → Hist π               -- records read off the Φ-orbit (R and τ)

/-- p_M(h | π, p) = μ_p {λ | R π (orbit (ι p π λ)) = h}  (EP:97), via `Measure.map`
(Mathlib/MeasureTheory/Measure/Map.lean:91) or directly. -/
noncomputable def NativeModel.law (M) {k} (p) (π : Prot A k) (h : Hist π) : ℝ :=
  ((M.μ p) {λ | M.R π (fun t => M.Φ^[t] (M.ι p π λ)) = h}).toReal

/-- The admission schema of EP:75–92 as a predicate. Setting independence is
`ProbabilityTheory.IndepFun` (Mathlib/Probability/Independence/Basic.lean:144) of the uncontrolled
restriction U and the fresh setting S; causal-prefix compatibility is the agreement of the laws of
protocols with a common prefix, restricted to that prefix; label coherence is D-I.2 below. -/
def SchemaAdmissible (M : NativeModel A) : Prop := …
```

### 4.2 The clauses

```lean
/-- DESIGN. Target I at one carrier, with E a parameter. -/
def InclusionAt (E : ∀ {A} [Fintype A] [DecidableEq A], NativeModel A → Prop)
    (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] : Prop :=
  ∃ M : NativeModel A, E M ∧ SchemaAdmissible M ∧ CompositionalLoading M ∧
    ∀ (k : ℕ) (p : DensLabel (Car A k)) (π : Prot A k) (h : Hist π), M.law p π h = qLaw p.ρ π h
```

- **I-1, one model per comparison.** Typed by quantifier order: `∃ M` precedes `∀ k p π h`. So one M
  covers every preparation, protocol, history and ancilla level of `J_exact(A)`.
- **Reading to be confirmed: Q_exact(A) has one law.** Under EP:43 and EP:110, `Q_exact(A)` supplies
  the whole interface with the standard trace law, and that law is fixed by the labels. So
  `T ∈ Q_exact(A)` adds no freedom beyond `qLaw`, and `M_{A,T}` is `M_A`. If review confirms this
  reading, I-2's permitted dependence on T is empty, and the parameter map depends on A alone.
- **I-2, one architecture.** The clause is typed as follows:

  ```lean
  structure Arch where
    Par  : Type
    par  : ∀ (A : Type) [Fintype A] [DecidableEq A], Par        -- parameter map: sees A only
    inst : Par → ∀ (A : Type) [Fintype A] [DecidableEq A], NativeModel A
  /-- Label coherence (EP:67, :90): `ι p π` is a fold of π with a FIXED per-primitive
  interpretation, so a label denotes the same procedure wherever it is selected. -/
  def CompositionalLoading (M : NativeModel A) : Prop :=
    ∃ (alg : ProtAlgebra M.Ω), ∀ k p π λ, M.ι p π λ = alg.load p λ (Prot.fold alg π)
  ```

  **Finding D-I.2, a typing limit.** I-2 forbids a parameter map "computed … from the values of
  p_T". Lean functions are extensional, and p_T is a function of the typed labels, the matrices ρ and
  K. So a map that "never computes p_T" cannot be told apart, by any predicate on its graph, from one
  that recomputes p_T from the labels. Only two things are typable: the *signature* restriction (`par`
  sees A, not the law) and *compositionality*. The intensional part of I-2 cannot be stated as a Lean
  predicate. It survives only as I-3's physical-sourcing clause.
- **I-3, physical sourcing.** E is a parameter. A Lean inclusion theorem would have the shape
  `theorem inclusion (hE₁ : Clause₁) … (hEₖ : Clauseₖ) : ∀ A, InclusionAt E A`, in which every
  unsourced clause is a named hypothesis. Lean can make that conditionality explicit but cannot
  discharge it.
- **I-4, exactness.** Equality in `ℝ`, with no ε. "No fixed finite total carrier" is typed by
  imposing no `Fintype M.Ω` and no `Finite M.Λs`. The statement is cardinality-neutral. Two
  necessary conditions follow:
  - **D-I.4a.** `J_exact(A)` contains every ancilla level `k` (EP:41). A single M must therefore
    load unboundedly many ancilla levels, which requires unbounded record and ancilla resources
    already at one A. This is close to a restatement of EP:41, recorded as a scope note, not a gem.
  - **D-I.4b, design lemma.**
    `InclusionAt E A → ¬ (Finite M.Ω ∧ LoadingIgnoresPrep M)`, where `LoadingIgnoresPrep` says that
    `ι p π λ` depends on p only through λ.
    - Proof sketch: under that hypothesis the prepare-and-measure table factors through `Ω`, which is
      Main:568's factorization half. Exactness on a qubit subfamily would then need a bounded
      nonnegative rank, which Main:568 imports from [55].
    - Mathlib has no nonnegative-rank theory: `nonnegRank` and synonyms are absent at `v4.33.0`.
      The step is therefore an import (I), to be carried as a hypothesis or formalized at
      research-grade cost.
    - When the loading may store p in Ω, the lemma gives nothing: storing the density label already
      makes Ω infinite.

### 4.3 Countercontrol D-W: a ψ-complete witness (design; an assumption-watch result)

**Design statement.**
```lean
theorem psiComplete_inclusion (A) [Fintype A] [DecidableEq A] [Nonempty A] :
    InclusionAt (fun _ => True) A
```
Read informally, this says that with E trivial, the typed clauses I-1, I-2 (signature and compositionality), I-4 and the admission schema have a witness for every A.

**Construction sketch.**
- **Seeds.** `Λs := ℕ → unitInterval` with `Measure.infinitePi (fun _ => volume)`.
  - `infinitePi` is at Mathlib/Probability/ProductMeasure.lean:358, with its
    `IsProbabilityMeasure` instance at :381 and `infinitePi_map_restrict` at :377.
  - `volume` on `unitInterval` is the `MeasureSpace I` instance of
    Mathlib/MeasureTheory/Constructions/UnitInterval.lean:26.
- **World configurations and dynamics.** `Ω := ℤ → X`, a bi-infinite trajectory space, with `Φ` the
  shift. The shift is a `MeasurableEquiv` via `MeasurableEquiv.piCongrLeft` (Embedding.lean:496) and
  `Equiv.addRight 1`.
- **Loading.** `ι p π λ` writes the run of the classical simulator from time 0 onward:
  - the current unnormalized state;
  - the program π in isolated controller fields;
  - at step j, outcome a, chosen by comparing seed `λ j` with the cumulative branch weights
    `tr(K_a ρ K_aᴴ)/tr ρ`;
  - the record of outcomes appended.
- **Records.** `R` reads the appended outcomes.
- **Admission.**
  - The seed law μ_p is fixed for p and independent of π.
  - The uncontrolled part is the seed, independent of the setting by construction.
  - Common prefixes consume the same seeds, which gives causal-prefix compatibility.
  - The fold over π gives compositionality.
- **Law equality.** By induction on π. Each step's conditional law is the Born weight, and the
  product of conditionals telescopes to `qLaw`, because the unnormalized propagation of §4.1 is
  multiplicative along the path.

This is the adaptive, infinite-horizon analogue of the clock-and-trajectory construction in `S_imp_D` (Equivalence.lean:422, `Hid := Fin (K+1) × Traj V K` at :365). It is the history-law counterpart of the operation-level `qm_generated_by_substratum_extension` with `fullClass`. In the literature it is the ψ-complete ontological model (Harrigan and Spekkens, Found. Phys. 40 (2010) 125; Beltrametti and Bugajski, J. Phys. A 28 (1995) 3329). Reversibility costs nothing on trajectory space, as in Bennett's logical reversibility (IBM J. Res. Dev. 17 (1973) 525).

**What D-W would establish (classification POSITIVE, by §A.31, pending review).** The typed parts of I carry no content without E:
- I-1, the typable part of I-2, I-4 and the EP schema;
- including reversibility, seed independence and causal prefixes.

Every nontrivial content of I lies in E and I-3: EP:47 (probability tables are not a realization) and EP:92 (lookup tables supplied with quantum outcome probabilities are not physical source evidence). It therefore constrains any future Lean inclusion theorem. A Lean `InclusionAt E A` proved for a candidate E must come with a proof that E excludes `psiComplete` (D-W.C, `¬ E psiCompleteModel`). Otherwise the theorem is the countermodel restated. This makes the obligation in I-3 and EP:102 concrete: admission must be independent of equality to the comparator.

**What it would not establish.** Anything about OI's native dynamics. The witness is a simulator that computes the trace rule inside its hidden dynamics, which is exactly what EP excludes.

**Hardest step.** Measurability of the sampler `λ ↦ outcome path`, a countable composition of threshold maps, by `measurable_pi_lambda` (Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean:597), together with the telescoping identity for conditional measures on cylinder sets.

**Classification and cost.** (I): the simulator uses the comparator's matrices as data, and that import is the point of the countercontrol. Expected axioms: the standard three. Cost: high, from measure theory on infinite products and an induction over an inductive type with dependent histories. CI only. **Needs cardinality neutrality** for its OI reading, because `Ω` is uncountable.

### 4.4 The conditional reduction linking D-O1, D-O3 and I

```lean
/-- DESIGN. If a native model's protocol semantics is the realized-channel semantics of a
native source, the source's theory is exact QM, and the law bridge holds, then the model
matches the comparator. -/
theorem inclusion_of_source [Nonempty A] (M : NativeModel A) (src : ∀ k, NativeSource (Car A k))
    (O3 : …) (hqm : ∀ k, ExactAllFiniteEndomorphicQuantumOps ((src k).toTheory (O3 k)))
    (hsem : RealizedSemantics M src)   -- each label is loaded as a procedure realizing exactly it
    (hlaw : ∀ k, LawBridge (src k)) :
    ∀ k p π h, M.law p π h = qLaw p.ρ π h
```

- **Proof sketch.** Induction on π. `hqm`'s completeness half, `ExactCompositeQuantumOps` read ⇐,
  supplies a procedure for every requested instrument label. `hsem` makes the loaded procedure realize
  exactly that instrument. `hlaw` turns each step's native probability into the trace. Composition is
  the `bind` field.
- **Hardest step.** `hsem`. "Realizes exactly the requested instrument" is a coherence statement
  across the whole tree: the same procedure for the same label everywhere. Stating it is where I-1's
  coherence meets O3's record retention.
- Only completeness of `hqm` is used. Soundness, ⇒, belongs to the sector part S⇒ (§5.2 of r4), not
  to I.
- **Classification.** (I), with three imports: kinematics through `NativeSource.branch`, the trace
  law through `LawBridge`, and the O3 fields.

## 5. D-O2: one exact model over unbounded carriers (one coherent construction)

**Classification: (I).** The imports are those of D-O1 and D-O3, plus the spectator law S-∞ below. **Needs cardinality neutrality.** One Ω has to contain subsystems for every finite A and every ancilla level, so Ω is infinite.

### 5.1 What is already uniform in the kernel (cited)

- `ImplementationClass` (ImplementationLocality.lean:244) is one predicate over *every* finite
  carrier, and `genTheory 𝓘 arch S` (:852) builds the theory on each carrier from that one rule.
- `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136) gives exact QM on every nonempty
  finite carrier from one `QuantumArchitecture 𝓘` (:86). So *across-size coherence at the operation
  level* is already one construction.
- `ContextStable` (ImplementationLocality.lean:359) and `LabelInvariant` (:364) are its compatibility
  maps: adjoining uncoupled factors, and relabelling.
- What is missing is the *single model*: one Ω, one Φ and one loading rule whose restrictions realize
  every carrier's theory and laws together.

### 5.2 The single-model statement

```lean
open RegionTower QuasilocalAlgebra
/-- DESIGN. One native model on configurations `ι → Q` (infinite `ι`), with a parameter map
fixed in advance that assigns to each finite A a region and an encoding, and one theory per
region generated by ONE implementation class. -/
structure CoherentTower (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] where
  dyn   : ReversibleDynamics ι Q                       -- QuasilocalAlgebra.lean:956
  𝓘     : ImplementationClass
  qa    : QuantumArchitecture 𝓘                         -- import: carries O1's DrivesElementary
  site  : ∀ (A : Type) [Fintype A] [DecidableEq A], Finset ι     -- parameter map, sees A only (I-2)
  enc   : ∀ (A : Type) [Fintype A] [DecidableEq A],
            Matrix (Conf (site A) Q) A ℂ                -- isometric encoding, Vᴴ V = 1
  enc_iso : ∀ A …, (enc A)ᴴ * enc A = 1
  model : NativeModel' (ι → Q)                          -- ONE model for every A (Ω = ι → Q or an extension)
  regionSem : ∀ Λ, RealizedSemantics (model.restrict Λ) (genTheory 𝓘 qa.arch (Conf Λ Q))
  spectator : SpectatorInert model                      -- S-∞, below

theorem single_model_inclusion (C : CoherentTower ι Q) [Infinite ι] (hlaw : …) :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (k p π h),
      C.model.law (encodeP C A p) (encodeProt C A π) (encodeHist h) = qLaw p.ρ π h
```

The order of quantifiers, `∃ C` (one tower) before `∀ A`, is the "one model, not one per size" requirement of answer (c)3. Here `site A` and `enc A` are fixed before any law is compared. For example, `site A` can be the first `⌈log_{|Q|} |A|⌉` sites of a fixed enumeration of `ι`, extended by fresh sites for each ancilla level.

### 5.3 The lemma decomposition

1. **O2-a, encoding (pure linear algebra; no native import).**
   - Statement: for an isometry `V : ℂ^A → ℂ^{Conf Λ Q}`, every instrument label on `Car A k` is
     encoded as follows. Branch `i` maps to `V K_i Vᴴ + c_i (1 − V Vᴴ)` with `∑ |c_i|² = 1`, so that
     normalization holds on the whole region.
   - Then `qLaw_Λ (V ρ Vᴴ) (encode π) h = qLaw_A ρ π h` for every ρ, π and h.
   - Ancilla levels and joins go to fresh sites through `inclObs` (RegionTower.lean:123).
   - Mathlib dependencies:
     - `Matrix.trace_mul_comm` (Mathlib/LinearAlgebra/Matrix/Trace.lean:158);
     - `Matrix.trace_kronecker` (Mathlib/LinearAlgebra/Matrix/Kronecker.lean:398);
     - `Matrix.PosSemidef.conjTranspose_mul_mul_same` (Mathlib/LinearAlgebra/Matrix/PosDef.lean:313),
       for positivity of the encoded state.
   - Cost: medium. This lemma is the one part of D-O2 that is a statement of mathematics with no
     native content.
2. **O2-b, region compatibility.** For `Λ ⊆ Λ'`, the region theories agree under `inclObs`. This
   follows from `ContextStable` and `LabelInvariant` after the region reindexing
   `Conf Λ' Q ≃ Conf Λ Q × Conf (Λ' \ Λ) Q`, which is a design obligation with no kernel lemma
   located. The kernel's `stage_inclObs` (QuasilocalAlgebra.lean:700) is the algebra-level version.
3. **O2-c, S-∞, spectator inertness of the infinite remainder.** The native law of a protocol
   supported in Λ does not depend on the configuration outside Λ, after marginalization over the seed
   law of the complement.
   - This is the decoupled-factor question. It is the import of D-O2 and its hardest step.
   - It overlaps the frozen ancilla-invariance lines of #1477's ledger (D369–D373) and the Theorem 24
     thread. **It waits**, and this record designs only its statement.
4. **O2-d, assembly.** Apply `inclusion_of_source` (§4.4) on `site A`, with
   `genTheory_qm_of_quantumArchitecture` supplying `hqm`. Then O2-a transports the result to A, and
   O2-c removes the remainder.

### 5.4 Scope checks (POSITIVE, cited)

- `q3_countermodel` (InstrumentAvailability.lean:335) shows that finite-support availability does not
  entail infinite-support coherent operations. `J_exact(A)` needs only finite-support operations, on
  `site A` and finitely many ancilla sites. So that countermodel does not obstruct D-O2.
- The quasilocal completion (`QuasilocalSystem`, QuasilocalCharacterization.lean:168) is not needed
  for D-O2's law equality, which lives on finite regions. If it is used, it supplies uniqueness given
  the stages (`canon_unique`, `systemEquiv`), *not* an equivalence with "OI_Q". §A.34 applies, and
  D-O2 asserts no iff.
- **Directions.** `single_model_inclusion` is one-directional. No converse is designed.
- **Expected axioms.** The standard three.
- **What it would establish.** Answer (c)3's form of I, conditional on `QuantumArchitecture 𝓘` (O1),
  `RealizedSemantics`, the law bridge (O3) and S-∞.
- **What it would not establish.** Any of those premises. It also says nothing about laws on
  infinite-support operations.
- **Cost.** High overall: O2-a is medium, O2-b and O2-c are high, and O2-c is blocked. All Lean work
  runs in CI.

## 6. Cross-cutting

### 6.1 Registry and census (§A.35)

If any design were later implemented, it would be new modules, one family per design: `OIQMInterface` for D-O1, D-O3 and §4.4; `OIQMTarget` for §4.1–4.2; `PsiComplete` for D-W; and `CoherentTower` for D-O2.
- **Census entry.** Each module needs a family in `verification/lean-manuscript-census.json`. The
  disposition would be `kernel-only` with an empty `manuscript` list, as for `PairFlowEquivalence`.
  The family needs anchors only if a manuscript later cites it.
- **No supersessions.** None of these designs strengthens a theorem inside an existing module, so no
  supersession entry is needed.
- **Mixed families.** If D-O1 were instead added inside DerivedQ3 or MinimalRepertoire, whose
  families are `current` with GR and Main anchors, it would be a change in a manuscript-carried
  family. The §A.35 contract would then require the registry to be updated in the same commit. The
  designs avoid this by using new modules.
- **Frozen docstrings.** No design edits a docstring frozen in #1477's ledger: D282 is in
  FrozenSourcing.lean, D285 in RouteB.lean and D286 in SubstratumSource.lean. New modules import
  these files and leave them unchanged.
- **Gate.** Each new module carries `#print axioms` lines for the release gate.

### 6.2 (N)/(I) summary and the earliest assumed links

| Design | Label | Imports, and where the Lean statement makes them explicit |
|---|---|---|
| D-O1 | (I) | Kinematics: the type of `NativeSource.branch`. Phases: the `DerivedOI` conjunct, plug point A only. Implementation generation: the `ImplementationLocality` field (AW-LEAN-1). O3 fields: a parameter of `toTheory`. |
| D-O3 | (I) | Uniform attach, readout existence and locality, feed-forward with retained records, discard: fields of `O3Fields`. Trace law: `LawBridge.trace_rule`. |
| D-I (§4.1–4.2) | (I) | The comparator `qLaw`, complex QM by definition. E: a predicate parameter. Unsourced clauses: named hypotheses of the inclusion theorem. |
| D-I.4b | (I) | Unbounded qubit nonnegative rank (Main:568 [55]): a hypothesis, since Mathlib has none. |
| D-W | (I) | The comparator's matrices, used as data inside the simulator. That is the point of the countercontrol. |
| §4.4 | (I) | Kinematics, `LawBridge` and `O3Fields` as hypotheses. `hqm` is the O1 output. |
| D-O2 | (I) | `QuantumArchitecture 𝓘`, a structure field carrying O1. `RealizedSemantics`, a field. S-∞, the field `spectator`. O2-a alone is a statement about the comparator, with no native content. |

**Earliest links where a physical mechanism is assumed rather than derived.** In order along the chain from native data to law equality:
1. the realization map from native procedures to complex channels (Coh-1, `NativeSource.branch`),
   before any control question;
2. the native law bridge (`LawBridge`, Meas-1, O6);
3. the O3 fields, uniform attach and readout, and above all record retention inside `bind`;
4. only then coherent operation (O1), and S-∞ for O2.

The existing kernel results all sit downstream of link 1, so a physical source of O1 cannot be stated in Lean without links 1 to 3.

### 6.3 Cardinality neutrality

| Design | Needs cardinality neutrality for its OI reading? |
|---|---|
| D-O1, D-O3, §4.4 at one finite carrier | no: the carriers are finite types and Ω is not referenced |
| D-I §4.1–4.2 | the statement is cardinality-neutral; every witness has an infinite Ω (D-I.4a, D-I.4b) |
| D-W | yes: Ω is uncountable |
| D-O2 | yes: one Ω over infinitely many sites |

### 6.4 §A.31 outcome classification of the findings

- **POSITIVE, pending review: D-W.** It validates I-3 and EP:47 and EP:92 as the load-bearing clauses
  of I. It also constrains every future Lean inclusion theorem, which must carry the exclusion
  `¬ E psiCompleteModel`.
- **NEW, borderline pending review: D-I.2.** The intensional part of I-2 cannot be typed.
- **NEW: AW-LEAN-1.** `ImplementationGenerated` is a coincidence demand on the whole native
  repertoire.
- **ELABORATING: the phase and addressability trade-off between plug points A and B.**
- **ELABORATING, a reading for review: O3's ready-state obligation reduces to records.**
- **CONFIRMING: q3_countermodel and the quasilocal uniqueness** do not obstruct D-O2.

None of these findings is a theorem. Each is a design-level claim awaiting independent review.
