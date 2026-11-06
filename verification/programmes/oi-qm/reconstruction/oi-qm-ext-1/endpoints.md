# OI ↔ finite operational QM: endpoint and hypothesis ledger

**Standing.** Paper-only Gate A specification for #1169, authorized by #1031 comment 6685633671. Definitions, source inventory and proposed bridge obligations; no new equivalence theorem or physical mechanism is established. Source snapshot: `8dd8bc6f0992c48b70b36020c29f5020c139144b`. The candidate physical extension is to be proposed separately at Gate B. This specification is submitted for independent review.

## 1. Existing conditional result to use

For a nonempty finite carrier A and a theory T of type `FiniteOperationalTheory A`, the corpus already supplies:

```text
ExactAllFiniteEndomorphicQuantumOps T ↔ PhysicalCompletionConditions T
```

The two directions have different witnesses:

| Direction | Source witness |
|---|---|
| Five completion conditions imply exact finite endomorphic operations | `OIBridge.GeneralCarrier.exactAll_of_physical_general`, GeneralCarrier.lean:93 |
| Exact finite endomorphic operations imply the five conditions | `OIBridge.PhysicalCharacterization.physical_of_exactAll`, PhysicalCharacterization.lean:301 |
| Assembled characterization | `OIBridge.GeneralCarrier.exactAll_iff_physical_general`, GeneralCarrier.lean:100 |

Paths in this table are under `verification/lean-mathlib/OIBridge/`. These are existing formal statements on main, not new results of this unit. This unit reads their statements and explicit dependencies; it does not claim a fresh Lean build or new end-to-end kernel certification.

The five conditions are composite operational validity, inert spectators, full composite unitary control, iterated ancilla closure, and system-to-level-one consistency. Their conjunction is defined in PhysicalCharacterization.lean:295.

The ambient structure is already complex-linear: its operations are linear maps on complex matrix spaces, including the system–ancilla spaces. OperationalAssembly.lean:594 also supplies availability, coarse-graining, outcome-dependent sequential composition, available preparations, uniformly mixed ancilla attachment, spectator-independent basis readout, and attach–run–discard closure. A native physical interpretation of these fields is an obligation; their occurrence as structure fields is not a derivation from bare OI.

The distinction also preserves results already derived inside the interface: `OperationalAssembly.readout_is_localLuders` derives the readout form from its stated linear and spectator-independence hypotheses. The existence and physical realization of those interface data remain different obligations.

The same boundary is stated in Main §3.4: complex matrix kinematics is given in this characterization, and its operational derivation is open. The kernel characterization concerns available operation families inside that representation. It is not by itself a construction of physically realizable native OI models matching all quantum experimental histories.

## 2. Endpoints and common protocols

For every nonempty finite carrier A, fix the primary comparison interface `J_exact(A)` as follows. Its system objects are A and `B_n = A × Fin n` for every integer `n > 0`; level one is identified with A by the canonical one-state-ancilla bijection. Joining an m-state helper to `B_n` uses the fixed reindexing `(A × Fin n) × Fin m ≃ A × Fin (n*m)`. These are the positive composite levels of the existing endomorphic characterization.

The interface contains:

1. Every density preparation `ρ` on each object: every positive semidefinite complex matrix of trace one, with the full complex parameter domain, including all pure and mixed states.
2. Every finite-outcome endomorphic quantum instrument on each object: every finite family of completely positive complex-linear branch maps whose sum preserves trace. Its branches are trace-nonincreasing on positive inputs. All such families and their full complex parameter domains are included, rather than a selected gate or measurement menu.
3. Every finite sequential/adaptive protocol built from these primitives. Each protocol is a finite tree, with a next instrument chosen as a function of the retained past. The family contains trees of every finite depth and every finite branching size; there is no fixed maximum horizon.
4. The classical record operations needed for those trees: append each outcome to an allocated finite record, retain it, read it repeatedly without changing that record, condition later choices on it, and relabel or coarse-grain outcomes. The resource contract must supply compatible finite record/controller resources for every such protocol.
5. Independent attachment of a helper in any density state on `Fin m` with `m > 0`, operations on the resulting positive composite levels, untouched spectators, and discarding a selected helper with the fixed join/reindexing maps. There is no fixed upper bound on the positive ancilla level. Genuinely dimension-changing maps beyond these specified preparations, joins, discards and reindexings are outside this primary endpoint unless a separate typed implementation/transport obligation is added.

The quantum class `Q_exact(A)` supplies this entire interface with the standard sequential instrument/trace law. The common labels identify preparation and intervention requests; they do not postulate that a native procedure realizes a requested density matrix or instrument. Constructing the native procedure and its fixed label interpretation is part of the correspondence obligation. Neither quantum preparation availability, a finite menu, nor a horizon can be narrowed later while retaining the name `J_exact(A)`. A smaller independently justified target must be enumerated and named as a restricted target.

The quantum trace rule is the comparator's definition, not a native OI measurement postulate. Exactness for `J_exact(A)` has no preassigned finite menu, horizon bound or ancilla cutoff. Restricted finite-menu/horizon approximation remains the separate target of §3.

An extended native OI model must carry its underlying OI data plus an explicit interpretation of J's labels by allowed physical procedures. Defining arbitrary probability tables with the desired quantum values is not a physical realization. Nor is `RealizesSealedOICore` identified here with the whole class of physically realizable native OI models.

For a model X, let p_X(h | π, p) denote the joint probability of finite outcome history h in protocol π. The native record law must be separately specified; it cannot inherit the quantum trace rule merely by notation. Conditional probabilities are compared only where their conditioning history has positive probability.

The primary proposed model-level target is:

```text
For each nonempty finite A and a fixed, independently specified extension E:

For every M in M(E, J_exact(A)),
  there exists one T in Q_exact(A) such that
  p_M(h | π, p) = p_T(h | π, p)
  for every preparation p, protocol π and history h in J_exact(A).

For every T in Q_exact(A),
  there exists one M in M(E, J_exact(A)) such that
  p_T(h | π, p) = p_M(h | π, p)
  for every preparation p, protocol π and history h in J_exact(A).
```

The witnesses and label interpretations must work coherently for the complete `J_exact(A)` family. They cannot be chosen anew per outcome, setting or experiment. Preservation of sequential composition, conditioning and the declared composite structure is part of the correspondence.

These are proposed obligations, not proved statements. The first kernel table in §1 discharges the two directions of an internal algebraic characterization only; it does not discharge either whole-model realization statement above.

### 2.1 Candidate native model data and admissibility

A candidate is specified by data `(Ω, Φ, Λ, μ, ι, R, τ, E)`. Here Ω is the declared world-configuration space, Φ its common autonomous reversible dynamics, and Λ a preparation-seed space. The declared extension principles E constrain these objects and their physical interpretation. The choices of measurable structure, finite or infinite resources, and any coherent carrier are part of E, not consequences of writing this tuple. Bare OI hypotheses are traced to Main §1.2; this schema does not identify the formal predicate `RealizesSealedOICore` with physical admissibility.

For each preparation p, `μ_p` is a probability law on Λ. A program-loading map `ι(p, π, λ)` prepares the system, controller, ready records and other declared physical subsystems for protocol π. It must be built from the candidate's stated admissible preparation procedures. The uncontrolled seed law is fixed for the preparation and cannot be chosen to fit future settings or a desired output history. Independence of this seed law alone is insufficient: the loaded physical state must also satisfy the following conditions.

Let `ν_(p,π) = (ι(p,π,·))_* μ_p`. The model must identify the controlled setting/program variables and a physical restriction map U onto the joint uncontrolled preparation, environment, controller-noise and ready-record variables relevant to the later outcomes. Every such uncontrolled component is included; U cannot be empty or discard an inconvenient hidden correlation. No global product decomposition of Ω is inferred.

For a fixed preparation and shared experimental past, changing a future setting/program may load only the specified controller fields. The restriction of `ν_(p,π)` to U must be unchanged until the declared setting interaction. The loading operation preserves the preparation it claims to hold fixed, the ready-state specification, and already established public records; those records are unchanged on admissible configurations. The controller/program fields that differ must be physically isolated from U and the retained records until their declared interaction.

For a fresh randomized setting S, require joint conditional independence on the actual loaded physical law:

```text
Law(U, S | p, retained past)
  = Law(U | p, retained past) × Law(S | p, retained past).
```

This is a requirement on the loaded state and setting mechanism, not a consequence of using an identical or uniform `μ_p`. A later declared controller–system coupling may change the state and outcome law as a function of the chosen setting.

**Causal-prefix compatibility.** Protocols with the same realized prefix must induce the same joint uncontrolled-state and history law before they diverge, with the preparation, earlier settings, recorded outcomes and spent resources held fixed. Only isolated fields encoding unused future program choices may differ. A given operation label denotes the same physical procedure whenever selected, with dependence restricted to its declared inputs and retained past; unused future choices cannot alter its incoming state or response law through loading. Subsequent choices may depend on the retained past as the adaptive protocol specifies. A proposed E must physically establish these isolation, loading, independence and prefix properties; this definition does not source them.

The record maps R and declared observation/termination rules τ extract a history `H_M(λ, π)` from the same Φ and the loaded physical program. Settings must act through specified controller–system couplings. Recorded outcomes, feed-forward and repeated record reads must be realizable by that dynamics; arbitrary lookup tables supplied only with quantum outcome probabilities do not count as physical source evidence. If a candidate uses a product factorization of Ω or a particular causal/locality structure, it must state that hypothesis rather than infer it from the schema.

The native history law is

```text
p_M(h | π, p) = μ_p({ λ : H_M(λ, π) = h }).
```

All terms must be well-defined in the declared measurable model. The initial law, program-loading rules, world dynamics, record interpretation and resource policy are fixed for the model. A physical preparation rule may legitimately depend on its preparation label; it cannot be replaced by a new fitted hidden law for each subsequent experiment.

The class `M(E, J)` consists of candidates satisfying the declared E and realizing every protocol in J through these data. E and admission to this class must be specified independently of equality to the quantum comparator's probabilities. Matching those probabilities is the theorem obligation, never the admission test. Construction and nonemptiness of a physically meaningful candidate class are obligations for the subsequent construction unit; Gate A supplies the interface contract and claims neither. A soundness statement over an empty class cannot establish the research objective.

The protocol family J is declared before comparing laws. A native model lacking a target preparation, setting, instrument, record operation or composite procedure has an availability gap; the correspondence cannot hide it by restricting to the intersection of available experiments. Both directions must preserve the typed preparation/intervention labels, sequential and outcome-dependent composition, and the declared spectator/composite operations. Equality means operational equivalence under these tests, not a bijection between ontic configurations and density matrices.

Record storage, controller size, preparation cost, observation times and the physical supply of ancillas are included in the resource policy. An arbitrary number of finite protocol steps or ancillas requires a compatible resource family or a declared completion. Enlarging resources separately for each experiment is not one fixed model unless the common construction and compatibility maps are stated and proved. These are explicit obligations, not established properties of an unspecified extension.

### 2.2 Quantum histories and the two directions

For a quantum protocol with initial density operator `ρ_p` and the instrument branches selected along history h, its law is the trace of the sequentially composed unnormalized branch applied to `ρ_p`. Its preparation and instrument availability are exactly `J_exact(A)`: every density preparation, normalized finite-outcome CP instrument and positive ancilla level, with all finite adaptive protocol trees. General changes of system type, if included beyond endomorphic operations, require an explicit implementation/transport argument; they are not silently supplied by the endomorphic characterization.

The model-level target above is therefore indexed by the preparation as well as the protocol. In both directions, the same witness and label interpretation must cover all p, π and h in the declared target. The native law in §2.1 and the comparator trace law remain independently defined until a reconstruction proves that they agree.

## 3. Exactness and finite resources

Main §3.4 and its conclusion distinguish exact finite-observable representations, bounded finite-menu/horizon approximation, and the complete continuum operational theory at all precisions.

Gate A must keep two claims separate:

- **Primary target:** exact correspondence for the full `J_exact(A)` family at each nonempty finite A. The extended-native class and its resource/parameter domains must be stated before asserting this target.
- **Separate approximation target:** for declared dimension, finite menu, finite horizon and ε > 0, one realization covers the entire declared experiment family to a stated error. An approximation theorem does not establish the primary target.

No single fixed finite classical carrier is silently used as an exact realization of all continuum qubit preparations/effects at all precisions. Any completion, carrier enlargement or additional coherent resource is entered as an explicit extra condition. Failure of the primary target does not authorize retrospectively replacing it with the approximation target.

## 4. Physical categories and hypothesis ledger

### 4.1 Crosswalk to the existing theorem

The five candidate categories describe physical research tasks. They have a many-to-many relation to the existing theorem's premises and ambient structure:

| Candidate category | Existing formal requirement or result to reuse | Physical obligation for an extension |
|---|---|---|
| Coh-1 | Given complex matrix/linear interface and composite carriers in `FiniteOperationalTheory` | Specify the actual carrier and phase-sensitive distinctions, and justify its matrix representation; no coherence follows merely from a classical probability law |
| Dyn-1 | `HasCompositeUnitaryControl`; exact-operation sufficiency once all completion conditions hold | Source the allowed control dynamics at every claimed composite level; a single non-monomial gate or interference example does not supply all finite unitary control |
| Prep-1 | `prepAvail`, mixed-ancilla attachment and the pure-seed derivations in `OperationalAssembly` | Realize the required preparation and reset procedures, ready-state resources and setting-independent seed laws; preserve the hypotheses of the existing preparation derivations |
| Meas-1 | The given readout existence/locality data, `readout_is_localLuders`, and `CompositeOperationalValidity` | Source a physical instrument and stable accessible records, and derive its native probability law where claimed; the comparator trace rule alone supplies no native readout mechanism |
| Comp-1 | `InertSpectatorCompositionality`, `IteratedAncillaClosure`, `SystemToLevelOne`, and the interface's composition/discard rules | Establish the actual subsystem joins, spectator behavior, repeatable record access and compatible controller/ancilla use within one physical model |

The pre-existing five-way independence theorem concerns its specified qubit completion class with formal OI-core realization. It is not an independence theorem for Coh-1 through Comp-1, for the native model data in §2.1, or for a future physically restricted E. Those questions require their own stated class and evidence.

### 4.2 Initial numbered ledger

“Open” below means an obligation of this proposed bridge, not a new universal claim that the whole corpus lacks a result. Each native-sourcing assessment must search the relevant corpus and trace actual support before deciding derived, posited, independent or unsourced.

| ID | Clause | Current role / status | Required source or check |
|---|---|---|---|
| 1 | Complex matrix state/operation kinematics | Mathematical representation already assumed by `FiniteOperationalTheory`; native justification not established by that definition | OperationalAssembly:594; native construction or an explicit added posit |
| 2 | The structure's availability, preparation, basis-readout and composition fields | Given formal interface; native realization open for this bridge | Interpret every field by a physically sourced procedure, including the preparation/readout clauses |
| 3 | CompositeOperationalValidity | One of the existing five completion conditions, additional to the raw structure | OperationalValidity:88; native statistics and their matrix representation must justify its full quantified scope |
| 4 | InertSpectatorCompositionality | Existing completion condition | Independent-system attachment must preserve the interpreted operation |
| 5 | HasCompositeUnitaryControl | Existing completion condition; all required finite composite unitaries, not one chosen non-monomial gate | OperationalAssembly:665; a sourced control construction or explicit posit with that scope |
| 6 | IteratedAncillaClosure | Existing completion condition | Iterated attach–operate–discard realization at the declared levels |
| 7 | SystemToLevelOne | Existing completion condition / representation consistency | Native system and trivial-ancilla interpretations must agree |
| 8 | Preparation, ready states and setting independence | Physical interface obligations; no native supply inferred from a quantum comparator | Source ledger for the relevant #866/#914 obligations |
| 9 | Native record/readout law, including Born probabilities where claimed | Separate physical obligation; the trace rule is initially the comparator's rule | Preserve the #1143 F-4 distinction; derive the native law or label it as an added assumption |
| 10 | Coherent carrier, record persistence and genuine system–setting coupling | Candidate physical obligations corresponding to Coh-1/Dyn-1/Meas-1/Comp-1 | Audit the actual native operations and relevant retained records; a classical record match alone is not a coherence witness |
| 11 | A consistent whole-process realization and reverse model coverage | New bridge obligations; neither is supplied merely by equality of available matrix-operation sets | Construct both witness maps and check all histories/compositions in scope |
| 12 | Exactness, parameter domain and resource/completion policy | Scope conditions requiring declaration | Respect the boundary in §3; no concealed precision or carrier enlargement |

The issue's Coh-1, Dyn-1, Prep-1, Meas-1 and Comp-1 are candidate requirement groups. They are not identified one-to-one with the five kernel conditions. In particular, a single E-nm transformation is not silently identified with full composite unitary control.

RankGapTheory.lean:702 supplies five-way independence witnesses in the formal completion class with `RealizesSealedOICore`. It does not classify physical admissibility of every native model class this project might propose. S8-A's scoped planning assessment and the #1033 transfers likewise do not prove either realization map in §2.

If an extension directly posits Hilbert kinematics, all needed unitary control or the native Born law, the resulting theorem must disclose those imports and its limited explanatory content. “The native model reproduces all QM” is not an admissible premise.

## 5. First unit and review boundary

The proposed paper-only Gate A unit produces:

1. A precise endpoint/interface specification, the candidate native model contract of §2.1, and both whole-model obligations stated separately.
2. A source-linked ledger and category crosswalk refining §4, separating native results, mathematical representation, imported quantum facts and added physical assumptions.
3. A map from the existing internal characterization to the remaining native bridge obligations, preserving the theorem's nonempty-carrier, endomorphic-operation and given-kinematics scope.
4. An independent review of definitions, directionality, noncircularity, resource scope and every source/status assertion.

Completion of this unit adopts no new physical premise and proves no full OI ↔ QM equivalence. Any later sufficient-extension construction, conditional proof, necessity/minimality investigation, simulation, Lean change, manuscript change, freeze, dispatch or merge retains its separate authorization.

The existing kernel theorem is a component to reuse with its actual scope. The work still needed is to specify and establish the native realization and sourcing bridge under explicitly declared conditions.

The research acceptance criterion after the later authorized gates is a new, noncircular physical reconstruction with a common operational realization and an assumption-source/minimality audit, or a precise identification of irreducible missing physical inputs within a stated class. Gate A is complete only when independent review accepts the endpoint, noncircular admission contract, source map and explicit remaining obligations. It does not itself establish that later physical acceptance criterion.
