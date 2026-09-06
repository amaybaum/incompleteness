# The instrument-migration audit — provenance-aware realization as the implementation semantics

`OIBridge/ImplementationLocality.lean` (`Realized`, `ImplementationGenerated`,
`ImplementationLocality`, the derivations, `implementationLocality_of_qm`, the countermodel
diagnosis, `OIPlusLocal`), `OIBridge/LieRankSource.lean` (the `realized_*` closure lemmas,
`Architecture`, `IsGenInstrument`, `genTheory`, the diagonal class, `OIPlusElem`),
`OIBridge/MicroscopicReversibility.lean` (`ReversibleImplementationLocality`, inverse accessibility
from dagger stability, `OIPlusMicro`), `OIBridge/PositiveReachability.lean` (unitary control from
Lie-rank richness without inverses, `OIPlusPos`), `OIBridge/InstrumentRealization.lean`
(`InstAvail`, the instrument forms, `PhaseSaturated`, the countercontrol), and the eight modules
that consume the generated theory (`SubstratumSource`, `StructuralClosure`, `SubstratumInterfaceAudit`,
`RouteB`, `ManuscriptAxioms`, `LiftAudit`, `MinimalRepertoire`, `ScalarClosure`);
`INSTRUMENT-REALIZATION-AUDIT.md` (the survival record this migration executes); guard `R7-MIG`
and the guards `R7-INST`, `R7-SUB`, `R7-SCAL`, `R7-MAX`, `R7-LIFT` in
`verification/lean/edge_rigidity_probe.py`.

**Status: pass complete.** The sections through the non-doings fix the decision, the census of
what changes, the module plan and the tests with their admissible outcomes before any edit, at
commit `45e6063`; the outcome section records what the migration did. Nothing here is a
manuscript claim.

## The decision it implements

The instrument-realization audit defined `InstAvail`, proved it sound for the branch-wise notion
and strictly finer than it, and re-established the implementation-locality stack for it under
parallel instrument names with one added hypothesis. The owner's decision at its review, quoted:

> After #518 merges, I recommend a separate preregistered migration round to make
> provenance-aware realization the canonical implementation semantics. In that migration I would
> rename `PhaseSaturated` to `UnitaryRaySaturated` (or similar), because it is really a statement
> that a nonzero scalar multiple of a unitary can be promoted back to the unitary, not the same
> thing as the project's phase resource. I would keep that condition local to inverse
> accessibility rather than adding it to the equivalence package.

So this round replaces the branch-wise semantics in place: `ImplementationGenerated` is
instrument generation, `genTheory` is the instrument theory, every theorem of the stack keeps
its name and its statement except where the survival record says it needs a hypothesis, the
parallel `Inst` names disappear, and the saturation condition is renamed and confined to the
derivation of inverse accessibility from dagger stability.

## The census of what changes, taken before the edit

**The definitions that change in place.**

- `ImplementationGenerated T 𝓘`, in `ImplementationLocality`: from
  `T.availExt N O F ↔ (∀ a, Realized 𝓘 (A × Fin N) (F a)) ∧ ∀ X, Σₐ tr((F a) X) = tr X` to
  `T.availExt N O F ↔ InstAvail 𝓘 (A × Fin N) O F`. The trace clause is a theorem of the
  predicate (`instAvail_trace`).
- `genTheory 𝓘 arch S`, in `LieRankSource`: from the branch-wise fields (`IsGenInstrument`) to
  the instrument fields of `instTheory`. Its name is kept; the branch-wise theory is kept under
  the name `branchTheory` in the comparison module, with `IsGenInstrument` as its predicate.
- `PhaseSaturated` is renamed `UnitaryRaySaturated`, stated next to inverse accessibility.

**The definitions that do not change.** `Realized` (the branch-wise notion, kept for the
comparison theorems and the scalar-hull regression), `ImplementationClass`, `ContextStable`,
`LabelInvariant`, `DaggerStable`, `Architecture` (its fields; it moves upstream), every package
(`ImplementationLocality`, `ReversibleImplementationLocality`, `OIPlusLocal`, `OIPlusMicro`,
`OIPlusElem`, `OIPlusPos`, `OIPlusMin`, `DerivedOI`, `SourcedOI`), and every class
(`fullClass`, `diagClass`, `substratumClass`, `permClass`, `onesClass`).

**The theorems whose proofs consume the old shape**, by the destructuring `⟨hreal, htr⟩` or
`hav.1 ()` of an available family, each to be re-proved through soundness
(`realized_of_instAvail`, `instAvail_trace`) or monotonicity (`instAvail_mono`):
`parallel_of_implementationLocal`, `krausSoundExt_of_implementationGenerated`,
`generated_of_qm`, `countermodel_not_implementationGenerated` (`ImplementationLocality`);
`inverseAccessibility_of_generated_daggerStable` (`MicroscopicReversibility`);
`diagGen_not_control` (`LieRankSource`); `genTheory_avail_conj` (`SubstratumSource`);
`configurationLevel_availExt_le`, `configurationLevel_falsifierUnavailable`
(`ManuscriptAxioms`); `configurationLevel_not_layerFlowExecutable` (`LiftAudit`);
`substratumTheory_falsifierUnavailable` (`RouteB`); `bijectionLevel_not_phasesAvailable`,
`bijectionLevel_diagonal_only_scalar`, `permTheory_no_sign`,
`permTheory_availExt_le_substratum` (`SubstratumInterfaceAudit`); `genTheory_availExt_eq`,
`permTheory_hull_availExt_iff` (`ScalarClosure`); every field of `genTheory` and
`genFamily_relabelling` (`LieRankSource`).

**The theorem whose proof consumed free recombination.** `inverseAccessibility_of_generated_daggerStable`
re-summed the adjoint branches. Its consumers: `inverseAccessibility_of_reversibleImplementationLocality`,
which `oiPlusLocal_of_oiPlusMicro` (`MicroscopicReversibility`) and `lieRank_not_redundant`
(`LieRankSource`) consume. The first is the seam: `OIPlusMicro → OIPlusLocal` needs the inverse
clause of reversible richness, and the survival record says it needs saturation if it is taken
from dagger stability. The kernel has a second source of the inverse clause that consumes no
dagger stability: `control_of_lieRank` (`PositiveReachability`, round fifty-four), Lie-rank
richness alone gives full composite unitary control, and `reversibleRichness_of_control` then
supplies inverse accessibility on a well-formed theory. It is stated downstream of
`LieRankSource` only because the module that holds it also holds the `OIPlusPos` package; its
core, Sections A–G, consumes nothing from `LieRankSource`.

**The surfaces that pin the old semantics.** Guards: `R7-INST` (the parallel instrument names,
the unchanged branch-wise definitions), `R7-SUB` (`permTheory` as `genTheory permClass`, the
no-phase theorem's statement), `R7-SCAL` (`genTheory_availExt_eq`, the README sentence naming
`IsGenInstrument`), `R7-MAX` (the configuration-level statements), the per-module name registry
(`MicroscopicReversibility`, `LieRankSource`, `PositiveReachability`, `SubstratumSource`,
`InstrumentRealization`). Notes: `SUBSTRATUM-INTERFACE-AUDIT.md`, `SCALAR-CLOSURE-AUDIT.md`,
`INSTRUMENT-REALIZATION-AUDIT.md`, each frozen and each to receive a migration section. README:
the three paragraphs of those rounds. Census: the three families. Manuscripts: GR §3.3 states
implementation locality as generation "by finite families of admissible implementation operators
with aggregate probability normalization" and that "the normalization half of operational
validity is explicit in implementation generation"; under the new primitive the normalization is
a theorem of the primitive, not a clause of the generation. No manuscript sentence is edited in
this round; the requalification is recorded below as an owner decision for a propagation round.

## The module plan, fixed in advance

1. `PositiveReachability` keeps its Sections A–G with the import of `LieRankSource` removed;
   its Section H, the theory-level package `OIPlusPos` and its equivalences, moves verbatim to a
   new module `OIBridge/PositivePackage.lean` in the same namespace, so that every name is
   unchanged. `control_of_lieRank` and `inverseAccessibility_of_lieRank` are stated in
   `MicroscopicReversibility`, which imports the core.
2. `ImplementationLocality` receives, upstream of `ImplementationGenerated`: `readProj`,
   `InstAvail` and its constructors verbatim, `instAvail_mono`, `instAvail_trace`, the
   one-outcome composition lemmas, `Architecture`, the `realized_*` closure lemmas and
   `conjChannel_smul`, `realized_of_instAvail`, `cp_of_instAvail`, the relabelling and spectator
   closures (`instAvail_transport`, `instAvail_spectator`, `instAvail_withSpectator` with their
   matrix lemmas), and `genTheory` with its family and its embedded observation. Its Sections D–F
   are re-proved for the new definition with unchanged statements.
3. `MicroscopicReversibility`: `UnitaryRaySaturated`; `inverseAccessibility_of_generated_daggerStable`
   with the two added hypotheses; `inverseAccessibility_of_reversibleImplementationLocality` with
   the per-class hypothesis; `oiPlusLocal_of_oiPlusMicro` through `inverseAccessibility_of_lieRank`;
   `fullClass_unitaryRaySaturated`.
4. `LieRankSource`: the moved sections removed; `diagClass_unitaryRaySaturated`;
   `lieRank_not_redundant` through the saturated derivation for the diagonal class.
5. The eight consuming modules: proofs repaired through soundness and monotonicity, statements
   unchanged; `substratumClass_unitaryRaySaturated` in `StructuralClosure`,
   `permClass_unitaryRaySaturated` in `SubstratumInterfaceAudit`; `genTheory_availExt_eq` restated
   as `↔ InstAvail 𝓘 (A × Fin n) O F`; `permTheory_hull_availExt_iff` re-proved.
6. `InstrumentRealization`: the moved sections removed; the parallel `Inst` definitions and
   theorems removed, each replaced by the canonical name it duplicated; `IsGenInstrument` and
   `branchTheory` defined here as the comparison objects, with `genTheory_le_branchTheory`;
   the countercontrol and the ones-fixing class unchanged.

## The tests, each with its admissible outcomes

**M1. The semantics.** `ImplementationGenerated` and `genTheory` carry the instrument semantics
in place, pinned verbatim; `branchTheory` carries the branch-wise one. Admissible outcomes: the
two definitions as fixed above, or a definition that could not be placed upstream of its
consumers, recorded with the consumer.

**M2. Statements.** Every theorem consuming `ImplementationGenerated`, `ImplementationLocality`,
`ReversibleImplementationLocality` or `genTheory` keeps its name and its statement, except the
two fixed in advance: `inverseAccessibility_of_generated_daggerStable` gains
`(arch : Architecture 𝓘)` and `(hs : UnitaryRaySaturated 𝓘)`, and
`inverseAccessibility_of_reversibleImplementationLocality` gains the per-class form of the same;
and `genTheory_availExt_eq`, whose right-hand side is the new predicate. Admissible outcomes: the
list above exactly, or a further theorem that needed a hypothesis, named with the reason.

**M3. The compressed sets.** `oiPlusMicro_iff_qm`, `oiPlusElem_iff_qm`, `oiPlusPos_iff_qm`,
`oiPlusMin_iff_qm`, `oiPlusLocal_iff_qm` and their carrier-general forms keep their statements,
the inverse clause of reversible richness taken from Lie-rank control on a well-formed theory.
Admissible outcomes: unchanged statements, or a package that needs the saturation condition,
named; in that case the condition is not added to the package silently but recorded as the
outcome of this test.

**M4. Saturation, local.** `UnitaryRaySaturated` is defined once, next to inverse accessibility,
holds for the four classes of the kernel, and occurs in no package definition and in no
equivalence with quantum mechanics. Admissible outcomes: absence from every package, guarded, or
the package in which it had to appear, named, which is the outcome of M3.

**M5. One name per result.** The parallel instrument names of the previous round are removed:
`InstrumentGenerated`, `InstrumentLocality`, `ReversibleInstrumentLocality`, `OIPlusInst`,
`OIPlusMinInst`, `DerivedOIInst`, `SourcedOIInst`, `RouteBTargetInst`, `SubstratumAvailInst`, the
`*Inst` theories and theorems, each to the canonical name it duplicated, listed in the outcome.
The countercontrol `flow_realized_not_instrumentRealized`, the ones-fixing class and the protocol
invariant are unchanged. Admissible outcomes: the list, or a parallel name that has no canonical
counterpart, kept and recorded.

**M6. The surfaces.** The guards are updated to pin the migrated text and reject the old
definitions; the three frozen notes receive a migration section each; the README paragraphs are
corrected in place; the census families are corrected; no manuscript is edited, and the GR §3.3
sentences on the normalization clause are recorded as an owner decision for a propagation round.
Admissible outcome: all of the above, guarded by `R7-MIG`.

**M7. The checks.** Full kernel build; every result printing only `propext`, `Classical.choice`,
`Quot.sound`; the release gate; the probe; the census. Admissible outcome: all green.

## What the round does not do

Edit a manuscript. Delete `Realized`, `IsGenInstrument` or the scalar-hull regression, which
stay as the branch-wise comparison. Change `Architecture.smul` or any class. Define the least
class `flowClass`. Assert or refute the flow endpoint. Propagate Route B. Refresh the transfer
bundle.

## The outcome

Preregistration commit `45e6063`. The migration was made as fixed in advance. The kernel builds
and every result prints only `propext`, `Classical.choice`, `Quot.sound`: 121 modules and 2,699
named results at this commit, each result counted once, the parallel names of the previous round
gone.

| test | outcome | kernel |
|---|---|---|
| M1 | the semantics: `ImplementationGenerated T 𝓘` is `T.availExt N O F ↔ InstAvail 𝓘 (A × Fin N) O F` and `genTheory 𝓘 arch S` carries the instrument fields, both in `ImplementationLocality`, with `InstAvail` and its five constructors, `Architecture`, the branch-wise closure lemmas, soundness and the relabelling and spectator closures placed upstream of them in that module; `IsGenInstrument` and `branchTheory` carry the branch-wise notion in `InstrumentRealization`, and the generated theory lies inside the branch-wise theory at every level | `InstAvail`, `ImplementationGenerated`, `genTheory`, `realized_of_instAvail`, `instAvail_withSpectator`, `IsGenInstrument`, `branchTheory`, `genTheory_le_branchTheory` |
| M2 | statements: every theorem consuming the migrated definitions keeps its name and its statement, except the three fixed in advance: `inverseAccessibility_of_generated_daggerStable` gains `(arch : Architecture 𝓘)` and `(hs : UnitaryRaySaturated 𝓘)`; `inverseAccessibility_of_reversibleImplementationLocality` gains the per-class hypothesis `∀ 𝓘, ImplementationGenerated T 𝓘 → Architecture 𝓘 ∧ UnitaryRaySaturated 𝓘`; `genTheory_availExt_eq` has `InstAvail 𝓘 (A × Fin n) O F` on its right. No further theorem needed a hypothesis. `control_of_lieRank`, `inverseAccessibility_of_lieRank` and `genTheory_reversibleImplementationLocality` are stated in `MicroscopicReversibility` with unchanged statements | the three, and `lieRank_not_redundant`, whose proof takes the inverse clause of the diagonal theory from the saturated derivation with `diagClass_unitaryRaySaturated` |
| M3 | the compressed sets: `oiPlusLocal_iff_qm`, `oiPlusMicro_iff_qm`, `oiPlusElem_iff_qm`, `oiPlusPos_iff_qm`, `oiPlusMin_iff_qm` and their carrier-general forms keep their statements; `oiPlusLocal_of_oiPlusMicro` takes the inverse clause from `inverseAccessibility_of_lieRank` on the well-formed theory, so no package consumes the saturation condition | `oiPlusLocal_of_oiPlusMicro`, `carrier_general_oiPlusLocal`, `carrier_general_oiPlusMicro`, `carrier_general_oiPlusElem`, `carrier_general_oiPlusPos`, `carrier_general_oiPlusMin` |
| M4 | saturation, local: `UnitaryRaySaturated` is defined once, in `MicroscopicReversibility` beside inverse accessibility, holds for the four classes of the kernel, and occurs in no package definition and in no equivalence with quantum mechanics, guarded | `UnitaryRaySaturated`, `fullClass_unitaryRaySaturated`, `diagClass_unitaryRaySaturated`, `substratumClass_unitaryRaySaturated`, `permClass_unitaryRaySaturated` |
| M5 | one name per result: the parallel names are removed, each to the canonical name it duplicated, per the list below; two parallel results have no counterpart and are dropped, recorded below; the countercontrol, the ones-fixing class and the protocol invariant are unchanged | `InstrumentRealization`, 69 named results |
| M6 | the surfaces: `R7-MIG` pins the migrated definitions and rejects the parallel names and the branch-wise generation clause; `R7-INST`, `R7-SUB`, `R7-SCAL`, `R7-INV` and the per-module registry pin the migrated text; the four frozen notes carry a migration section each; the README paragraphs are corrected in place; the census family is corrected; no manuscript is edited, and the GR §3.3 sentences on the normalization clause are recorded below as an owner decision for a propagation round | `verification/lean/edge_rigidity_probe.py` |
| M7 | the checks: full build, axiom check, release gate, probe, census, all green | the release gate |

**The module plan, as executed.** `PositiveReachability` keeps Sections A–G, nineteen results,
with no import of `LieRankSource`; `PositivePackage` holds `OIPlusPos` and its three equivalences
in the namespace `PositiveReachability`, so every name is unchanged; `MicroscopicReversibility`
imports the positive-reachability core and states `control_of_lieRank` and
`inverseAccessibility_of_lieRank` beside the split of reversible richness.
`ImplementationLocality` holds, in order, the primitive (`readProj`, `InstAvail`,
`conjChannel_trace_iff`, `instAvail_mono`, `instAvail_trace`, `ImplementationGenerated`,
`ContextStable`, `LabelInvariant`, `ImplementationLocality`, `fullClass`), the branch-wise
closure (`cp_of_realized`, `conjChannel_smul`, the `realized_*` lemmas), the architecture
(`Architecture`, `fullClass_arch`, `realized_of_instAvail`, `cp_of_instAvail`, the one-outcome
composition lemmas), the relabelling and spectator closures with their matrix lemmas, the
generated theory (`genTheory`, `genFamily`, `genTheory_embeddedObservation`,
`genTheory_availExt_iff`, `genTheory_fullClass_control`, `genTheory_mono`, `genTheory_generated`,
`genTheory_implementationLocality`), the derivation, necessity with
`instAvail_fullClass_of_krausFamily`, the diagnosis and the compressed set: 81 named results.
`LieRankSource` keeps the diagonal architecture, the elementary transitions and `OIPlusElem`.
`SubstratumSource` proves `genTheory_avail_conj` as one step. The eight consuming modules are
repaired through `realized_of_instAvail` and `instAvail_mono` with unchanged statements.

**The names, each to its canonical counterpart.** `InstrumentGenerated` to
`ImplementationGenerated`; `InstrumentLocality` to `ImplementationLocality`;
`ReversibleInstrumentLocality` to `ReversibleImplementationLocality`;
`instrumentLocality_of_reversible` to `implementationLocality_of_reversible`; `instTheory`,
`instFamily` and the `instTheory_*`, `instFamily_*` results to `genTheory`, `genFamily` and the
`genTheory_*`, `genFamily_*` results, `instTheory_le_genTheory` to `genTheory_le_branchTheory`;
`parallel_of_instrumentLocal`, `observationalIndependence_of_instrumentLocality`,
`krausSoundExt_of_instrumentGenerated`, `validity_of_instrumentLocality`,
`instrumentGenerated_of_qm`, `instrumentLocality_of_qm`, `reversibleInstrumentLocality_of_qm`,
`countermodel_not_instrumentGenerated`, `countermodel_not_instrumentLocality`,
`instrumentLocality_independent` to the results of the same name with `implementation` for
`instrument` and `generated_of_qm` for `instrumentGenerated_of_qm`; `OIPlusInst` and its four
results to `OIPlusLocal` and its; `OIPlusMinInst`, `qm_of_oiPlusMinInst`, `oiPlusMinInst_of_qm`,
`oiPlusMinInst_iff_qm`, `carrier_general_oiPlusMinInst` to `OIPlusMin`, `qm_of_oiPlusMin`,
`oiPlusMin_of_qm`, `oiPlusMin_iff_qm`, `carrier_general_oiPlusMin`; `PhaseSaturated` to
`UnitaryRaySaturated` and the four `*_phaseSaturated` instances to `*_unitaryRaySaturated`;
`inverseAccessibility_of_instrumentGenerated` to `inverseAccessibility_of_generated_daggerStable`
and `inverseAccessibility_of_reversibleInstrumentLocality` to
`inverseAccessibility_of_reversibleImplementationLocality`; `DerivedOIInst`, `SourcedOIInst` and
their five results to `DerivedOI`, `SourcedOI` and theirs; `substratumInstTheory` and
`permInstTheory` with their results to `substratumTheory` and `permTheory` with theirs
(`_derivedOI`, `_sourcedOI`, `_not_phasesAvailable`, `_not_derivedOI`, `_availExt_le_substratum`,
`_falsifierUnavailable`, `_not_phaseFree`, `_relabel`, `_realizesSealedOICore`,
`_not_substratumAvail`), `bijectionLevel_not_phasesAvailable_inst` to
`bijectionLevel_not_phasesAvailable`, `configurationLevel_instAvailExt_le` to
`configurationLevel_availExt_le`; `SubstratumAvailInst` and `substratumAvailInst_phasesAvailable`
to `SubstratumAvail` and `substratumAvail_phasesAvailable`; `RouteBTargetInst` and
`routeB_target_inst` to `RouteBTarget` and `routeB_target`. The primitive's own results keep their
names in `ImplementationLocality`: `InstAvail`, `readProj`, `conjChannel_trace_iff`,
`instAvail_mono`, `instAvail_trace`, `realized_of_instAvail`, `cp_of_instAvail`,
`instAvail_comp_one`, `instAvail_one_comp`, `instAvail_id`, the transport and spectator lemmas,
`instAvail_transport`, `instAvail_spectator`, `instAvail_withSpectator`,
`instAvail_fullClass_of_krausFamily`; `conjChannel_zero'` and
`exists_scaled_mem_of_instAvail_unitary` move to `MicroscopicReversibility`.

**Two parallel results dropped.** `isGenInstrument_of_instrumentGenerated`, which is
`isGenInstrument_of_instAvail` applied to the generation clause, and `oiPlusMinInst_iff_oiPlusMin`,
an identity after the migration. Neither has a canonical counterpart because neither says
anything the canonical names do not.

**The scalar-hull regression, re-proved.** `permTheory_hull_availExt_iff` keeps its statement.
Its proof is two new lemmas: an isometry in the scalar hull of the sourced class lies in the
sourced class, its common entry having modulus at most one by the row norm
(`permClass_of_scalarHull_isometry`), and the readout projectors lie in it, so instrument
realization by the hull is instrument realization by the class (`instAvail_scalarHull_permClass`);
the converse is `instAvail_mono`. The branch-wise regression `realized_scalarHull_iff` is
unchanged, as fixed in advance; `ScalarClosure` has 12 named results.

**Where the saturation condition is consumed.** In `inverseAccessibility_of_generated_daggerStable`
and its per-class corollary, and, for the diagonal class, in `lieRank_not_redundant`. Nowhere
else. Whether inverse accessibility fails for some dagger-stable architecture that is not
unitary-ray saturated is open, as it was in the survival record.

**The GR §3.3 sentences.** GR §3.3 states implementation locality as generation "by finite
families of admissible implementation operators with aggregate probability normalization" and
that "the normalization half of operational validity is explicit in implementation generation".
Under the migrated semantics the normalization is a theorem of the primitive
(`instAvail_trace`), not a clause of the generation, and the families are the outcomes of one
protocol. Whether those two sentences are to be requalified is an owner decision for a propagation
round; no manuscript is edited here, and the census family stays verification-only.

**What the outcome establishes.** The kernel's implementation semantics is provenance-aware
realization: availability in an implementation-generated theory is instrument realization by the
class, with no sum constructor, and every publication-facing consequence of implementation
locality holds with an unchanged statement. The saturation condition is confined to the
derivation of inverse accessibility from dagger stability, which no equivalence with quantum
mechanics consumes.

**What the outcome does not establish.** Anything about the flow endpoint, which is neither
asserted nor refuted; that is the round to be re-preregistered on the migrated semantics. That
inverse accessibility holds for every dagger-stable architecture without saturation. That any
manuscript sentence is changed.

## What this note does not claim

That the flow endpoint is settled in either direction. That the least class `flowClass` is
defined. That inverse accessibility holds without the saturation condition for every dagger-stable
class. That the GR §3.3 sentences on the normalization clause have been requalified. That
anything here reaches a manuscript.
