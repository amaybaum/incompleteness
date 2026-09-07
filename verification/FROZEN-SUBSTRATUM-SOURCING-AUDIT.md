# The frozen substratum nonclassical-resource sourcing audit — does the stated architecture source any resource sufficient for the phases and dense control?

Owner-called from `main` at `8f277f5`, the merge of the dense-instrument bridge audit. Preregistered
here and committed alone before any proof is attempted.

The dense-instrument bridge audit closed the last mathematical gap on the density side: the
consequence closure with dense unitary control approximates every finite endomorphic Kraus
instrument (`krausDense_of_denseControl`), and the canonical fixed-gate theory is dense finite
quantum mechanics at every angle with `α/π` irrational. That theorem is downstream of this round
and is not part of its premise. What it leaves is a sourcing question, and the substratum interface
audit already showed that the question is larger than one gate: the sourced theory and the observer
theory both fail `DerivedOI`, and they fail it at the phases
(`bijectionLevel_not_phasesAvailable`, `permTheory_not_derivedOI`, `obs_not_derivedOI`). A round
that asked whether the architecture supplies a mixing gate *given* `DerivedOI` would assume its way
past the harder half. This round therefore sits below `DerivedOI` and asks the sourcing question for
both obligations at once.

## The question

> Does the presently stated substratum and observer architecture source any operational resource
> from which both the missing phase structure and dense unitary control follow?

Stated against the kernel's predicates, with the already-sourced part of the closure carried
separately:

> frozen sourced architecture ⟹ `PhasesAvailable T ∧ DenseUnitaryControl T`,

where `SourcedOI T` — the conjuncts of `DerivedOI` other than the phases — is the part the
architecture is already known to reach, and `derivedOI_iff_sourcedOI_phases` is the decomposition
the round works in.

No particular resource is the search target. `FixedGateSourced α`, `mixImage α`, `PairFlow`,
`PairFlowSourced` and every other named gate or flow are admissible *consequences* if some already
sourced structure is proved to imply them; none is preregistered as the required physical datum, and
the round does not go looking for a gate.

## The architecture, frozen exactly as it stands

Nothing in the following is changed, enriched or replaced during the round.

**The substrate.** `Substratum` with its sites `ι`, alphabet `V`, second-order rule `R`,
configuration space `Conf := ι → V × V` and dynamics `φ`. The axiom predicates `A1` (finiteness),
`A2` (determinism, automatic for the structure), `A3 D` (bounded coupling degree), `A4Exact` and
`A4 G` (center independence, exact and up to gauge), `A5` (linearity), and `A3Family`. **A6 remains
a gap with no predicate**, exactly as the substratum interface audit recorded it, and this round
does not define one. The manuscripts' wave rule `waveSubstratum d L q α` with its proved
`waveSubstratum_A1`, `_A2`, `_A3`, `_A4Exact`, `_A5`.

**The interface.** The sourced class `permClass`, the contractively scaled partial permutations,
with `permClass_arch`, `permClass_contextStable`, `permClass_labelInvariant`,
`permClass_daggerStable`, `permClass_unitaryRaySaturated`, `permClass_permMatrix`,
`permClass_readWrite`, `permClass_le_substratum`, and the characterization
`permClass_le_of_exchanges` that no architecture containing the exchanges is smaller. The sourced
theory `permTheory A := genTheory permClass permClass_arch A`, the observer theory
`obsTheory 𝒮 := permTheory 𝒮.Conf`, and the sourcing theorems that put the substrate's own
operations into availability: `obs_dynamics_avail`, `obs_dynamics_inv_avail`, `obs_shear_avail`,
`permTheory_avail_conj`.

**The shape predicates and the existing negatives.** `IsMonomial`, `bijectiveOperator`,
`phaseOperator`, `MonomialSource`, `monomialSource_not_control`, `monomialSource_not_qm`;
`BijectionLevel`, `bijectionLevel_configurationLevel`, `permClass_bijectionLevel`;
`PreservesNonneg`, `preservesNonneg_conj_of_scaled`, `preservesNonneg_sum`,
`preservesNonneg_of_realized`, `diagonal_nonneg_of_preservesNonneg`,
`phaseGate_not_preservesNonneg`, `sign_not_preservesNonneg`; and the universal negatives
`bijectionLevel_not_phasesAvailable`, `permTheory_not_phasesAvailable`, `permTheory_not_derivedOI`,
`obs_not_phasesAvailable`, `obs_not_derivedOI`.

**The rule-independence result.** `obsTheory_rule_independent`: two substrata on the same sites and
alphabet have the same observer theory, whatever their rules. Configuration-level sourcing consumes
nothing of A3 through A6. This is the sharpest constraint the round inherits and the census of
layer 1 must confront it directly rather than around it.

**From the density side, carried but not used as a premise.** `DenseUnitaryControl`, `KrausDense`,
`DenseFiniteQM`, `ChanWithin`, `conj_within`, `krausDense_of_denseControl`,
`denseFiniteQM_of_denseControl`, `fixedGateTheory_denseFiniteQM`. The bridge theorem is a
consequence of dense control, never a source of it.

## The four layers, frozen

**Layer 1, the exact source census.** Enumerate what the present architecture actually places into
operational availability, and separate that from what it merely represents mathematically. Every
item is classified as *sourced* — a theorem putting it into `availExt` — or *represented* — an
object the kernel can write down with no availability theorem behind it. The items to classify at
minimum: the substrate's own update and its inverse, the shear layer, the configuration bijections
generally, the read-write operators, the exchanges, the phase operator `phaseOperator` and the
quarter phase `phaseGate`, the wave rule's own action, and any coherent or wave object for which an
operational-carrier map genuinely exists rather than being posited. The census records for each
whether the sourcing theorem exists, and where it does not, that it does not. Continuous paths and
one-parameter families count as represented, not sourced, unless an availability theorem is exhibited.

**Layer 2, the phase ceiling.** The existing negatives are reused, not re-proved at witness level.
The round states the strongest source class the architecture currently justifies, and the exact
reason that class cannot supply the phase resource. The expected form: the sourced class is
bijection-level (`permClass_bijectionLevel`) and is the least architecture containing the exchanges
(`permClass_le_of_exchanges`), every operation realized by a bijection-level class preserves
nonnegative entries (`preservesNonneg_of_realized`), and the quarter phase does not
(`phaseGate_not_preservesNonneg`), so no bijection-level class supplies the phases
(`bijectionLevel_not_phasesAvailable`). What the layer must add is the *scope* statement: whether
anything the census of layer 1 found sourced escapes the bijection level. If nothing does, the
phase ceiling is the architecture's ceiling and not merely one class's.

**Layer 3, the dense-control ceiling.** Asked independently of layer 2, and answered by a structural
invariant rather than by testing a particular gate. The preregistered candidate invariant is
`PreservesNonneg`, with the expected route:

> every operation sourced by the frozen architecture preserves nonnegative entries; a theory with
> `DenseUnitaryControl` has, for every unitary `U` and every `ε > 0`, an available `V` with
> `conjChannel V` within `2 ε` of `conjChannel U` in `ChanWithin` (`conj_within`); entries are
> bounded by the operator norm, so `conjChannel U` is an entrywise limit of nonnegative-preserving
> maps and preserves nonnegative entries itself, for **every** unitary `U`; and the pair rotation
> `StateMixingCoupling.rot θ` at a suitable angle does not preserve them. Hence no
> bijection-level-sourced theory has `DenseUnitaryControl`.

If that route closes, the desired negative form is reached: every sourced operation lies in a
characterized class, and that class does not give dense control. If `PreservesNonneg` turns out not
to be the right invariant, monomiality (`MonomialSource`, `monomialSource_not_control`), diagonal
preservation, an all-ones-ray invariant or projective discreteness may be used instead; the
requirement is that the invariant be a property of the *class* and the no-go universal over it, not
a statement about one gate.

**Layer 4, the combined sourcing verdict.** Only after layers 2 and 3 are audited separately: is
there one already-sourced resource that supplies both obligations? A single resource could in
principle furnish the phases and dense control together, and nothing in this round preregisters that
two independent physical additions are necessary. What is established today is only that both
obligations need sourcing. If both ceilings hold, the verdict states that the resource is
independent of the presently stated architecture, for both obligations, and names what an extension
would have to add.

## The prediction, recorded before proof

Outcome 3 is expected. The reasons are already in the kernel and are stated here so that a
surprise is visible as one: the sourced class is bijection-level and is the least architecture
containing the exchanges; every bijection-level class fails the phases universally; and
`obsTheory_rule_independent` says the observer theory does not see the rule at all, so A3 through
A6 — including whatever the wave structure contributes — are invisible to the present sourcing map.
A positive outcome would require the census of layer 1 to find some sourced operation outside the
bijection level, which would contradict `permClass_bijectionLevel` unless the sourcing map itself is
richer than the audit recorded. That is the one place a genuine surprise could live, and layer 1 is
designed to look there.

The prediction is not a result. If the census finds such an operation, the round follows it.

## Admissible outcomes, frozen

Exactly three.

1. **Positive.** An operation or structure already present in the frozen architecture is shown to
   land in the operational interface and to be sufficient, with no new axiom, to source the phase
   structure and dense unitary control. The theorem exhibits the operation, its sourcing, and the
   two implications.
2. **Split or partial.** The frozen architecture supplies one obligation and not the other, or
   supplies a weaker nonclassical resource insufficient for the combined endpoint. The exact
   remaining physical condition is named as a statement, not as a gesture.
3. **No-go.** Every resource actually sourced by the frozen architecture stays inside a rigorously
   characterized class that cannot supply one or both obligations. The conclusion recorded is then
   that the quantum-enabling nonclassical resource is an independent empirical datum relative to the
   presently stated OI architecture — a scientific result, not a failed round.

No outcome names or adopts C5, none says that OI supplies the phases or any gate, none claims that
the architecture is thereby refuted, and none claims that exactly two independent additions are
needed.

## The circularity guard, the round's most important constraint

> No new axiom, carrier map, coupling, phase intervention, polarization map, continuous control,
> admissible operator, or enrichment of the implementation class may be added to the frozen
> substratum and then reported as sourced by OI.

If a positive proof requires such an addition, the addition is recorded as a **candidate empirical
extension**, with the exact consequence it would buy, and the sourcing verdict for the frozen
architecture remains negative. A6 may be discussed as the gap it is; it may not be filled with a
new physical operation and the result counted as something the architecture already had.

Two distinctions are kept explicit in every statement of the round:

- `PhasesAvailable` is not `DenseUnitaryControl`. Neither implies the other here, and the round
  proves nothing that conflates them.
- A resource sufficient for dense quantum mechanics is not a resource sourced by the substratum.
  Sufficiency is the density side, already settled; sourcing is this round's question, and the two
  are never run together in one sentence.

## Tests, frozen

**T1. The census.** Layer 1 as stated, with every item classified sourced or represented and the
sourcing theorem named where it exists. Admissible outcome: the census, with the classification
exhaustive over the items listed.

**T2. The scope of the sourced class.** Whether everything the census finds sourced is
bijection-level, stated as a theorem or as the exact item that escapes. Admissible outcome: either.

**T3. The phase ceiling.** Layer 2, with the strongest justified source class named and the reason
stated at class level. Admissible outcome: the theorem; or the item that escapes it.

**T4. The dense-control ceiling.** Layer 3, with the invariant proved to hold of the sourced class
and the no-go proved universal over it. Admissible outcome: the theorem; or the exact step at which
the invariant fails to separate.

**T5. The rule's operational content.** What, if anything, A3 through A5 and the wave rule
contribute to availability, read against `obsTheory_rule_independent`. Admissible outcome: the
statement, including the statement that they contribute nothing under the present sourcing.

**T6. The combined verdict.** Layer 4, with the two obligations audited separately first, and the
possibility of a single resource for both left open rather than excluded.

**T7. The surfaces and the checks.** Module `OIBridge/FrozenSourcing.lean`; nothing named C5; no
existing definition changed, enriched or restated; no new axiom on the substratum; guard `R7-FSS`
pinning the census, the ceilings, the verdict, this note's order, prediction, outcomes, tests and
non-doings, rejecting any C5 naming, any claim that OI supplies the phases or a gate, any claim
that a new operation added during the round was sourced, any conflation of the two obligations, and
any manuscript edit; README paragraph and counts; the census carries the family as kernel-only; the
substratum interface audit and the dense-instrument bridge audit may each receive one append-only
cross-reference section after their frozen text. Full build; every result printing only `propext`,
`Classical.choice`, `Quot.sound`; the release gate; the probe; the Bohr probe; the census; the
voice check. No manuscript is edited. Admissible outcome: all green.

**T8. The verdict statement.** Exactly one of the three outcomes, with the census status, the phase
ceiling, the dense-control ceiling and the combined verdict each stated separately.

## What this round does not do

- Name or adopt C5, or call any resource, gate or extension C5.
- Add any axiom, operation, carrier map, coupling or class enrichment to the frozen substratum, or
  report anything added as sourced.
- Define a predicate for A6, adopt either reading of it, or fill the gap.
- Preregister `FixedGateSourced α`, `mixImage α`, `PairFlow`, `PairFlowSourced` or any particular
  gate as the required datum, or search for a gate rather than for what the architecture sources.
- Claim that the phases and dense control require two independent physical additions.
- Claim that a negative outcome refutes the OI architecture, or that it establishes the resource
  cannot be sourced by any architecture; the scope is the presently stated one.
- Conflate `PhasesAvailable` with `DenseUnitaryControl`, or sufficiency for dense quantum mechanics
  with sourcing by the substratum.
- Use the dense-instrument bridge theorem as a premise of any sourcing statement; it is downstream.
- Retract or weaken `qm_iff_derivedOI_pairFlowSourced`, `fixedGateTheory_not_qm`,
  `fixedGateTheory_denseFiniteQM`, or any existing result.
- Edit a manuscript.

The point of the round is to determine whether the nonclassical resource that the density side now
shows to be sufficient is latent in the OI architecture as stated, or is an independent empirical
datum relative to it.

Status: preregistered; no proof attempted.
