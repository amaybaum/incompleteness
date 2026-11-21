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
(`research/oiqm-unbounded-20261121`) are cross-references only. None of their designs is used here. The single exception is the reconciliation the review of this record requested in §5.2: #1504's Proposition U and AW-U2 (reviewed, at `c66625e8`) were read for that purpose only. Nothing in this record depends on the A1 retirement (#1477) having landed. §6.3 marks the
designs that need cardinality neutrality.

## 0. Answers to the three questions

| | Established (with layer) | Assumed (imported) | Missing |
|---|---|---|---|
| O1, coherent operation | [K] Under the closure `DerivedOI`, exact finite endomorphic QM holds iff one layer flow is executable: `derivedOI_qm_iff_layerFlowExecutable'` (DerivedQ3.lean:222). The phase-free form is `oiPlusMin_iff_qm` (MinimalRepertoire.lean:569). The substratum and every configuration-level class execute no such flow (LiftAudit.lean:183, :200). | Complex matrix kinematics (the type of every channel). The closure's `PhasesAvailable` conjunct (RouteB.lean:148, stipulated). Implementation generation of availability. | A native procedure realizing the flow. Before that, a general realization relation from native procedures (with loading, finite outcomes and records) to complex channels. The kernel has only its configuration-level special case, `SubstratumInterface` (§2.1). |
| O3, preparation, readout and records | [K] The readout form is derived from existence and spectator independence (`readout_is_localLuders`, OperationalAssembly.lean:658). Pure seeds are derived from a uniform attach, a readout, feed-forward and ancilla swaps (`pureSeedPrep_available_of_swap`, :675). | The structure fields of `FiniteOperationalTheory` (:594): uniform attach, readout existence and locality, bind (feed-forward through a retained record), discard, system-level availability, and the ancilla swaps that `pureSeedPrep_available_of_swap` consumes. The trace rule as the native law. | Native procedures for each field. A typed record interface. A native law bridge (§3). |
| I-1 to I-4 | Nothing typed. `J_exact(A)` has no Lean form on `main`, and no module defines a history law over adaptive protocols. | The comparator, which is complex QM by definition (EP:110). E, as a predicate parameter. | The vocabulary of §4.1. The exclusion, by E, of the ψ-complete countermodel of §4.3. |
| O2, one model over unbounded carriers | [K] An implementation class is one rule for every finite carrier, and `genTheory_qm_of_quantumArchitecture` (SubstratumSource.lean:136) gives exact QM on every carrier from one class. The quasilocal completion is unique given its stages (QuasilocalCharacterization.lean:168, `canon_unique`), which is uniqueness and not an equivalence. | The same imports as O1 and O3, plus a spectator law for the infinite remainder. | Single-model law equality with operational stage semantics, whose readout cones are unbounded (#1504, Proposition U). Carrier encodings. The operational spectator law S-∞ (§5). |

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

Every existing conditional theorem quantifies over `T : FiniteOperationalTheory S` (OperationalAssembly.lean:594). In such a `T`, availability is a bare predicate on complex-linear maps `Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ`.

**What the kernel already covers.** The kernel has a configuration-level interface from substratum interventions to complex operators:
- `SubstratumInterface.bijectiveOperator` (SubstratumInterface.lean:55) sends a bijective intervention to its permutation matrix.
- `phaseOperator` (:58) sends a declared phase intervention to a diagonal matrix.
- `RouteB.substratumTheory` (RouteB.lean:286) is the `FiniteOperationalTheory` these generate, through `genTheory` and the monomial class.

**What the kernel lacks.** It has no *general* relation from native procedures to channels in which a procedure consists of:
- a loading of Ω;
- an evolution under Φ;
- a finite-outcome record extraction, possibly adaptive.

That relation must also be able to produce non-monomial channels. A physical source of O1 cannot plug into `derivedOI_qm_iff_layerFlowExecutable'` until that general relation is typed. By `configurationLevel_not_layerFlowExecutable` (LiftAudit.lean:183), the configuration-level case cannot carry O1.

**What the NativeSource interface adds** beyond SubstratumInterface:
- (a) procedures whose branches are arbitrary complex-linear maps;
- (b) finite outcome sets with records;
- (c) the O3 fields;
- (d) the law bridge.

The design types this as a structure whose fields are the imports:

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

The derived availability at each ancilla level is
`RealizedExt src n O F := ∃ (P : src.Proc n) (e : src.Out P ≃ O), F = src.branch P ∘ e.symm`.

**The system-level `avail` needs its own definition.** `RealizedExt` does not fix it, and two existing constraints bind it:
- `prepAvail_discard` forces `avail` to contain every `discardWith n P (F a)` for an available preparation `P` and an available family `F`.
- `SystemToLevelOne` (LevelOneSeam.lean:117) and `EmbeddedObservation` constrain it against level one.

The design therefore adds a field `sysProc : Type` with `sysBranch`. It sets `avail O F := RealizedSys F ∨ DiscardInduced F`, where `DiscardInduced` is the closure under `discardWith`. A source that satisfies `SystemToLevelOne` must then prove that this agrees with level one; that is an O3 obligation.

The theory `src.toTheory : FiniteOperationalTheory S` takes `availExt := RealizedExt` together with this `avail`. Building it needs exactly the remaining structure fields of `FiniteOperationalTheory`, and those are the O3 obligations (§3). So O3 is typed upstream of O1: no O1 statement can be made about a native source until the O3 fields are supplied.

### 2.2 The O1 obligation, in two forms

Plug point A is the closure plus a layer flow (DerivedQ3). Plug point B is the phase-free minimal repertoire (MinimalRepertoire).

```lean
/-- DESIGN, plug point A. The source supplies the closure and one layer flow of an involution
with a moved configuration. `DerivedOI` (RouteB.lean:148) carries `PhasesAvailable` as a
stipulated conjunct: an IMPORT unless sourced. -/
/- A `Prop`-valued structure may carry proof fields only, so the involution σ is a parameter,
as in `QuantumArchitecture : Prop` (SubstratumSource.lean:86), and the source asserts
`∃ σ, CoherentSourceA S src O3 σ`. -/
structure CoherentSourceA (S) [Fintype S] [DecidableEq S] (src : NativeSource S) (O3 : O3Fields src)
    (σ : Equiv.Perm S) : Prop where
  closure : RouteB.DerivedOI (src.toTheory O3)
  invol : ∀ x, σ (σ x) = x
  moved : ∃ x, σ x ≠ x
  flow : LiftAudit.LayerFlowExecutable (src.toTheory O3) σ   -- ∀ n t, availExt n Unit (conj (gateFlow (levelPerm σ n) t))

theorem qm_of_coherentSourceA [Nonempty S] (src) (O3) (h : ∃ σ, CoherentSourceA S src O3 σ) :
    ExactAllFiniteEndomorphicQuantumOps (src.toTheory O3)
-- proof: obtain ⟨σ, h⟩ := h; obtain ⟨x, hx⟩ := h.moved
--        exact DerivedQ3.qm_of_derivedOI_layerFlowExecutable _ h.closure h.invol hx h.flow

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

AW-LEAN-1 binds **both** plug points:
- **Plug point A.** `DerivedOI`'s first conjunct is `ReversibleImplementationLocality`
  (MicroscopicReversibility.lean:223). It contains `ImplementationGenerated` and adds `DaggerStable`.
- **Plug point B.** `ImplementationLocality` is a field of `CoherentSourceB` and contains
  `ImplementationGenerated` directly.

Its reach is limited. `ImplementationGenerated` quantifies over levels `N > 0` only. So level 0 and the system-level `avail` (§2.1) lie outside it and are constrained separately, by `SystemToLevelOne` and `prepAvail_discard`.

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
  - **Native-side form (design).** Instantiate the negative control as a `NativeSource` built from
    `SubstratumInterface`:
    - procedures: bijective and phase interventions;
    - branches: `conjChannel (bijectiveOperator σ)` and `conjChannel (phaseOperator d)`.
    
    Design obligation: show that its `toTheory` is `substratumTheory`, or lies inside it. The
    countercontrol then reads directly on the native side.

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
- (v) the trace law, as a law bridge;
- (vi) native realization of the ancilla swap corrections;
- system-level procedures, with their agreement with level one.

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
  sysAvail : …  -- system-level procedures and their agreement with level one (§2.1, SystemToLevelOne)
  swaps    : ∀ n (k k₀ : Fin (n + 1)), ∃ P : src.Proc (n + 1), …
               branch P () = conjChannel (CoherentLift.permMatrix (ancSwap (n + 1) k k₀))     -- import (vi)
             -- the `hswap` premise of `pureSeedPrep_available_of_swap` (OperationalAssembly.lean:675)

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
  - Under `RealizedExt`, though, they remain a native existence claim: the swap channels must be
    available in `toTheory`. That is field (vi), `swaps`. No other listed field supplies it.

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
  -- Measurability. Without these fields `law` is an outer-measure value and need not sum to 1
  -- over histories, so I-4 would compare non-additive quantities. `Hist π` carries ⊤.
  ι_meas : ∀ {k} p (π : Prot A k), Measurable (ι p π)
  R_meas : ∀ {k} (π : Prot A k) (h : Hist π),
             MeasurableSet {x : ℕ → Ω | R π x = h}          -- for the product σ-algebra on ℕ → Ω

/-- p_M(h | π, p) = μ_p {λ | R π (orbit (ι p π λ)) = h}  (EP:97), via `Measure.map`
(Mathlib/MeasureTheory/Measure/Map.lean:91) or directly. -/
noncomputable def NativeModel.law (M) {k} (p) (π : Prot A k) (h : Hist π) : ℝ :=
  ((M.μ p) {λ | M.R π (fun t => (⇑M.Φ)^[t] (M.ι p π λ)) = h}).toReal

/-- The admission schema of EP:75–92 as a predicate. Its clauses, each a design obligation:
(a) U-COMPLETENESS: a declared restriction `U : Ω → Ω_U` onto every uncontrolled variable relevant
    to later outcomes, which cannot discard a hidden correlation (EP:77);
(b) ISOLATION: for fixed p and shared prefix, changing the future program changes only declared
    controller fields, and the law of U under `(ι p π ·)_* μ_p` is the same for every π with that
    prefix until the declared setting interaction (EP:79);
(c) FRESH SETTINGS: `Prot` is extended by a node `setting (S : Fin s) (next : Fin s → Prot A k)`
    with a declared setting law, and `ProbabilityTheory.IndepFun` (Mathlib/Probability/
    Independence/Basic.lean:144) of U and S given p and the retained past (EP:81–88);
(d) CAUSAL PREFIXES: protocols with a common prefix induce the same joint law of U and history on
    that prefix (EP:90);
(e) LABEL COHERENCE: D-I.2 below. -/
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

  **Finding D-I.2, what can be typed (BORDERLINE / ELABORATING).** I-2 forbids a parameter map
  "computed … from the values of p_T".
  - **On one concrete map the clause cannot be typed.** Lean functions are extensional, and p_T is a
    function of the matrices ρ and K. So no predicate on the graph of one loading map on concrete
    matrix labels can tell a map that never computes p_T from one that recomputes it.
  - **On a family of maps it can be typed, as naturality over an abstract label signature.**
    - The signature `LabelSig` has sorts for states and instruments at each level. Its operations
      are sequential composition, tensor or attach, discard, outcome relabelling and
      coarse-graining. It has **no** entry, trace or scalar extraction.
    - The loading is given as a family `ι^𝔐` over every model `𝔐` of `LabelSig`.
    - The family is required to be natural, i.e. to commute with every signature homomorphism
      `𝔐 → 𝔐'`.
    - It is then instantiated at the matrix model for the law comparison:

    ```lean
    structure NaturalLoading (Ω) where
      load : ∀ (𝔐 : LabelSig.Model), 𝔐.State → ProtOver 𝔐 → Λs → Ω
      natural : ∀ {𝔐 𝔐'} (f : LabelSig.Hom 𝔐 𝔐') s π, load 𝔐' (f.state s) (π.map f) = load 𝔐 s π
    ```

  - **Cost and limits.**
    - Lean has no internal parametricity theorem, so `natural` is an explicit hypothesis.
    - Its force depends entirely on `LabelSig` excluding scalar access. That choice of signature is
      E-content (I-3).
  - **Restated finding.** I-2's intensional part is not a predicate on the concrete parameter map,
    but it is statable as naturality over an abstract label interface whose choice belongs to E.
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
    `InclusionAt E A → ¬ (Finite M.Ω ∧ Isolation M)`.
    - The hypothesis `Isolation M` is clause (b) of `SchemaAdmissible`: for fixed p, the law of the
      prepared uncontrolled state is independent of the future measurement π.
    - Proof sketch: with that hypothesis, `B(p, π, h) = ∫ ξ_{π,h} dν_p`, with `ν_p` a law on the
      finite `Ω`. The prepare-and-measure table therefore factors through `Ω`, which is Main:568's
      factorization half, with `N = |Ω|`.
    - The bound holds however p is stored in Ω, because only the π-independence of `ν_p` is used.
    - Without isolation the bound fails: if the loading depends on π, then `ν_{p,π}` does not
      factor, whether or not `ι` ignores p.
    - Exactness on a qubit subfamily would then need a bounded nonnegative rank, which Main:568
      imports from [55].
    - Mathlib has no nonnegative-rank theory: `nonnegRank` and synonyms are absent at `v4.33.0`. The
      step is therefore an import (I), to be carried as a hypothesis or formalized at research-grade
      cost.
    - This is the finite-Ω counterpart of #1504's Proposition U. That result has the same factorizing
      premise, preparation–setting independence, and is likewise labelled (I).

### 4.3 Countercontrol D-W: a ψ-complete witness (design; an assumption-watch result)

**Design statement.**
```lean
theorem psiComplete_inclusion (A) [Fintype A] [DecidableEq A] [Nonempty A] :
    InclusionAt (fun _ => True) A
```
Read informally, this says that with E trivial, the typed clauses I-1, I-2 (signature and compositionality), I-4 and the admission schema have a witness for every A.

**Construction sketch: a stepwise reversible simulator.** This replaces a superseded sketch. A precomputed trajectory on a shift space wrote the outcomes of later instruments into the loaded configuration. Those outcomes depend on the future program, so that sketch violated U-completeness and isolation (`SchemaAdmissible` (a), (b); EP:77, EP:79).

- **Seeds.** `Λs := ℕ → unitInterval` with `Measure.infinitePi (fun _ => volume)`.
  - `infinitePi` is at Mathlib/Probability/ProductMeasure.lean:358, with its
    `IsProbabilityMeasure` instance at :381 and `infinitePi_map_restrict` at :377.
  - `volume` on `unitInterval` is the `MeasureSpace I` instance of
    Mathlib/MeasureTheory/Constructions/UnitInterval.lean:26.
- **World configurations.** `Ω := Tape × Reg × Prog × Rec × Hist × Clock`, where:
  - `Tape := ℕ → unitInterval` is the seed tape, which is U;
  - `Reg` is a simulator register holding the current unnormalized state;
  - `Prog` holds the program π in isolated controller fields;
  - `Rec` is the outcome record;
  - `Hist` is a Bennett history stack of overwritten register values;
  - `Clock : ℤ` is a step counter.
- **Dynamics.** `Φ` performs one reversible step.
  - At clock j it reads the current instruction from `Prog` and the single seed `λ j`.
  - It chooses outcome a by comparing `λ j` with the cumulative branch weights `tr(K_a ρ K_aᴴ)/tr ρ`.
  - It pushes the old register value onto `Hist`, writes the updated register, appends a to `Rec`,
    and increments `Clock`.
  - The step is injective, because the stack keeps the overwritten value. It is made a bijection of Ω
    by the standard two-sided embedding: the domain is extended so that every configuration has a
    unique predecessor (Bennett, IBM J. Res. Dev. 17 (1973) 525). This is a design obligation, at the
    same level of effort as `exists_perm_extending` (Equivalence.lean:60) but on an infinite type.
- **Loading.** `ι p π λ := (λ, init p, π, [], [], 0)`. It writes the seeds, the preparation label and
  the program, and **no outcome**. The uncontrolled restriction is `U ω := tape ω`, whose law is μ_p
  for every π. Changing a future program changes only `Prog`, and the step reads `Prog` only at the
  current instruction.
- **Admission.**
  - (a) U-completeness: the tape is the only uncontrolled variable.
  - (b) Isolation: the law of U does not depend on π.
  - (c) Settings: fresh setting nodes consume seeds from a disjoint subsequence, which gives `IndepFun`.
  - (d) Causal prefixes: common prefixes consume the same seeds.
  - (e) Compositionality: the step interprets each primitive label by a fixed rule.
- **Records.** `R` reads `Rec` along the orbit.
- **Law equality.** By induction on π. Each step's conditional law is the Born weight, and the
  product telescopes to `qLaw`, because the unnormalized propagation of §4.1 is multiplicative along
  the path.

This is the adaptive, infinite-horizon analogue of the clock-and-trajectory construction in `S_imp_D` (Equivalence.lean:422, `Hid := Fin (K+1) × Traj V K` at :365). It is the history-law counterpart of the operation-level `qm_generated_by_substratum_extension` with `fullClass`. In the literature it is the ψ-complete ontological model (Harrigan and Spekkens, Found. Phys. 40 (2010) 125; Beltrametti and Bugajski, J. Phys. A 28 (1995) 3329).

**What D-W would establish (classification POSITIVE, by §A.31, pending review).** It is conditional on two things: this stepwise restatement, and `SchemaAdmissible` being written to include U-completeness and isolation. Given both, the typed parts of I carry no content without a nontrivial E:
- I-1, the typable part of I-2, I-4 and the EP schema;
- including reversibility, seed independence, isolation and causal prefixes.

**What can exclude the witness.** No typable clause of I or of the schema does. Only three EP clauses can, and they act together:
- the requirement that the loading be "built from the candidate's stated admissible preparation procedures" (EP:75);
- the lookup-table clauses (EP:47, EP:92);
- the independence of admission from equality to the comparator (EP:102).

They do so only once E names an admissible procedure class for `ι` and `μ_p` that does not depend on the labels' numeric entries. That is a nontrivial E.

The `NaturalLoading` form of D-I.2 is the typable shape of such an E. The simulator reads matrix entries, so it is not natural over a `LabelSig` without scalar access. It is natural over a signature that includes scalar access. The exclusion therefore rests on the choice of signature, which is E-content, and not on I-2 as typed in §4.2. A Lean `InclusionAt E A` proved for a candidate E must therefore come with D-W.C, `¬ E psiCompleteModel`; otherwise the theorem is the countermodel restated.

**A finite-information condition does not suffice.** `μ_p` may depend on p, so the label's entries can ride in the seed law. A finite-information or finite-support condition on `ι` alone, or on `Reg`, therefore does not exclude the simulator. D-W.C has the right shape, but no candidate E has yet been shown to satisfy it.

**What it would not establish.** Anything about OI's native dynamics. The witness is a simulator that computes the trace rule inside its hidden dynamics, which is exactly what EP excludes.

**Hardest step.** Two parts. First, the two-sided reversible embedding of the injective step on an infinite Ω. Second, measurability of the sampler `λ ↦ outcome path`, a countable composition of threshold maps; this becomes an obligation through the `ι_meas` and `R_meas` fields, by `measurable_pi_lambda` (Mathlib/MeasureTheory/MeasurableSpace/Constructions.lean:597), together with the telescoping identity for conditional measures on cylinder sets.

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
/-- DESIGN. One native model, a parameter map fixed in advance that assigns to each finite A a
region and an encoding, and one theory per region generated by ONE implementation class. Region
semantics is OPERATIONAL: a region Λ is an operational carrier (a stage, as in OI_Q), and the
native procedure interpreting a Λ-label has its own readout cone, which need not lie in Λ and may
grow without bound with the resolution demanded (#1504, Proposition U and AW-U2). -/
structure CoherentTower (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] where
  dyn   : ReversibleDynamics ι Q                       -- QuasilocalAlgebra.lean:956
  𝓘     : ImplementationClass
  qa    : QuantumArchitecture 𝓘                         -- import: carries O1's DrivesElementary
  site  : ∀ (A : Type) [Fintype A] [DecidableEq A], Finset ι     -- parameter map, sees A only (I-2)
  enc   : ∀ (A : Type) [Fintype A] [DecidableEq A],
            Matrix (Conf (site A) Q) A ℂ                -- isometric encoding, Vᴴ V = 1
  enc_iso : ∀ A …, (enc A)ᴴ * enc A = 1
  model : NativeModel' Ω                                -- ONE model for every A; Ω ⊇ (ι → Q) plus records and seeds
  cone  : ∀ {Λ}, model.Proc Λ → Finset ι                -- readout cone of a native procedure; NOT required ⊆ Λ
  opSem : ∀ Λ, RealizedSemantics model (genTheory 𝓘 qa.arch (Conf Λ Q))   -- operational, per stage
  spectator : SpectatorInert model                      -- S-∞, §5.3 item 3

theorem single_model_inclusion (C : CoherentTower ι Q) [Infinite ι] (hlaw : …) :
    ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] (k p π h),
      C.model.law (encodeP C A p) (encodeProt C A π) (encodeHist h) = qLaw p.ρ π h
```

The superseded form had a field `regionSem : ∀ Λ, RealizedSemantics (model.restrict Λ) …`. That field presumed a finite-region ontic realization of each stage. Under #1504's Proposition U (reviewed, at `c66625e8`), that is impossible for any native exact model satisfying preparation–setting independence, item (xiv). Proposition U is a paper result, labelled (I).
- On a site-factorized Ω with finite-range dynamics, an exact qubit needs readout cones that lie in no single finite region.
- So `cone` must be unbounded over the procedures interpreting any one stage. That is a consequence the design expects, not a field it imposes.

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
2. **O2-b, stage compatibility (operational).** For `Λ ⊆ Λ'`, the stage theories agree under
   `inclObs`. This
   follows from `ContextStable` and `LabelInvariant` after the region reindexing
   `Conf Λ' Q ≃ Conf Λ Q × Conf (Λ' \ Λ) Q`, which is a design obligation with no kernel lemma
   located. The kernel's `stage_inclObs` (QuasilocalAlgebra.lean:700) is the algebra-level version.
3. **O2-c, S-∞, spectator inertness of the remainder (operational form).**
   - For `Λ ⊆ Λ'`, every protocol π on stage Λ, and any two preparations `p` and `p'` on stage `Λ'`
     whose restrictions to Λ agree (`RegionTower.restrict h p.ρ = restrict h p'.ρ`,
     RegionTower.lean:128), the native laws agree:
     `law p (inclProt h π) = law p' (inclProt h π)`.
   - So the law of a Λ-protocol depends on the preparation of the complement only through its
     restriction to Λ. The statement is about the prepared state of the complement, which is what
     makes it well-posed. A superseded wording asked for independence "after marginalization over
     the complement"; that is vacuous, since nothing can depend on the complement once it has been
     marginalized out.
   - This is the import of D-O2 and its hardest step.
   - **Relation to Theorem 24, which covers only part of this.** Theorem 24(iii) (GR.md:138) is exact
     invariance for a deep sector that *no dynamics couples*. In `CoherentTower`, the same `dyn`
     couples the remainder to Λ, and readout cones leave Λ. So S-∞ is not an instance of Theorem 24(iii)
     and is strictly stronger. The Theorem 24 thread bears on the decoupled case only.
   - **Relation to #1477.** The any-cardinality extension of Theorem 24, rows D362–D373, is part of
     #1477's frozen plan (P* `55544cc3`). That plan has not yet been executed. The rows are marked as
     needing scientific review. **O2-c waits**, and this record designs only its statement.
4. **O2-d, assembly.** Apply `inclusion_of_source` (§4.4) to the operational semantics `opSem` at
   stage `site A`, with `genTheory_qm_of_quantumArchitecture` supplying `hqm`. Then O2-a transports
   the result to A, and O2-c removes the dependence on the complement's preparation. No step
   restricts the ontic model to a finite region.

### 5.4 Scope checks (POSITIVE, cited)

- `q3_countermodel` (InstrumentAvailability.lean:335) shows that finite-support availability does not
  entail infinite-support coherent operations. `J_exact(A)` needs only finite-support operations, on
  `site A` and finitely many ancilla sites. So that countermodel does not obstruct D-O2.
- The quasilocal completion (`QuasilocalSystem`, QuasilocalCharacterization.lean:168) is not needed
  for D-O2's law equality, which lives on finite *stages*. The stages are operational carriers; they
  are not ontic regions (AW-U2). If it is used, it supplies uniqueness given
  the stages (`canon_unique`, `systemEquiv`), *not* an equivalence with "OI_Q". §A.34 applies, and
  D-O2 asserts no iff.
- **Directions.** `single_model_inclusion` is one-directional. No converse is designed.
- **Expected axioms.** The standard three.
- **What it would establish.** Answer (c)3's form of I, conditional on `QuantumArchitecture 𝓘` (O1),
  the operational `opSem`, the law bridge (O3) and S-∞. Its readout cones are unbounded, as #1504's
  Proposition U requires.
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
- **Docstrings in #1477's plan.** No design edits a docstring named in #1477's frozen, not yet executed
  plan (P* `55544cc3`): D282 is in
  FrozenSourcing.lean, D285 in RouteB.lean and D286 in SubstratumSource.lean. New modules import
  these files and leave them unchanged.
- **Gate.** Each new module carries `#print axioms` lines for the release gate.

### 6.2 (N)/(I) summary and the earliest assumed links

| Design | Label | Imports, and where the Lean statement makes them explicit |
|---|---|---|
| D-O1 | (I) | Kinematics: the type of `NativeSource.branch`. Phases: the `DerivedOI` conjunct, plug point A only. Implementation generation: inside `ReversibleImplementationLocality` for A and the `ImplementationLocality` field for B (AW-LEAN-1). System-level availability: the `sysAvail` field. O3 fields: a parameter of `toTheory`. |
| D-O3 | (I) | Uniform attach, readout existence and locality, feed-forward with retained records, discard: fields of `O3Fields`. Trace law: `LawBridge.trace_rule`. |
| D-I (§4.1–4.2) | (I) | The comparator `qLaw`, complex QM by definition. E: a predicate parameter. Unsourced clauses: named hypotheses of the inclusion theorem. |
| D-I.4b | (I) | Unbounded qubit nonnegative rank (Main:568 [55]): a hypothesis, since Mathlib has none. Isolation, the π-independence of U's law: the hypothesis `Isolation M`. |
| D-W | (I) | The comparator's matrices, used as data inside the stepwise simulator. That is the point of the countercontrol. The conclusion is conditional on `SchemaAdmissible` including clauses (a) and (b). |
| §4.4 | (I) | Kinematics, `LawBridge` and `O3Fields` as hypotheses. `hqm` is the O1 output. |
| D-O2 | (I) | `QuantumArchitecture 𝓘`, a structure field carrying O1. Operational `opSem`, a field. S-∞ in operational form, the field `spectator`. The readout cone `cone` is a field that is not bounded. O2-a alone is a statement about the comparator, with no native content. |

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

- **POSITIVE, pending review, and conditional on the stepwise restatement and on `SchemaAdmissible`
  (a) and (b): D-W.**
  - Only EP:75, EP:47, EP:92 and EP:102 can exclude the witness, and only through a nontrivial E.
  - A finite-information condition alone does not exclude it.
- **BORDERLINE / ELABORATING: D-I.2.** I-2's intensional part is not a predicate on the concrete map,
  but it is statable as naturality over an abstract label signature. The choice of that signature is
  E-content.
- **NEW: AW-LEAN-1.** `ImplementationGenerated` is a coincidence demand on the whole native
  repertoire at positive levels, and it binds plug points A and B alike.
- **ELABORATING: D-I.4b, corrected.** Its factorizing hypothesis is isolation, as in #1504's
  Proposition U.
- **CONFIRMING: D-O2 uses operational stage semantics with unbounded readout cones**, consistent with
  #1504's Proposition U and AW-U2.
- **ELABORATING: the phase and addressability trade-off between plug points A and B.**
- **ELABORATING, a reading for review: O3's ready-state obligation reduces to records.**
- **CONFIRMING: q3_countermodel and the quasilocal uniqueness** do not obstruct D-O2.

None of these findings is a theorem. Each is a design-level claim awaiting independent review.
