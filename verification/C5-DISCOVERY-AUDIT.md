# The C5 discovery audit — is there a realization-level condition that sources the coherent resource?

Owner-called, written from `main` at `0df6a8a`, the merge of the sourcing propagation round.
Preregistered here and committed alone before any proof is attempted. Two sourcing audits and
their propagation leave the finite-QM completion in this state: within the closure, exact finite
endomorphic operational quantum mechanics is equivalent to phase-free richness
(`derivedOI_qm_iff_phaseFree`) and, with the phase intervention granted, to the executability of
one layer flow of an involution with a moved configuration (`derivedOI_qm_iff_layerFlowExecutable'`);
the stated substratum dynamics with the observer's access supplies neither the phase
(`permTheory_not_phasesAvailable_onesFixing`) nor the flow (`obs_not_layerFlowExecutable`), and the
observer-level lift, in every formulation that lands, derives neither
(`coherentLiftClass_eq_substratumClass`). The manuscripts' realization conditions C1–C4, coupling,
persistence, capacity and history readback, are diagnostics of a visible–hidden realization; the
finite completion quantifies over none of them. This round asks whether a fifth condition of that
same logical type exists. Nothing is named "C5" in it; every candidate is a "C5 candidate" until
outcome A supplies one.

## The question

> Does there exist a realization-level condition, of the same logical type as C1–C4, on the
> visible–hidden partition, such that together with the existing realization structure it sources
> the coherent operational resource that distinguishes the quantum completion from the known
> non-quantum OI realizations?

In the kernel, the coherent resource is two obligations on a finite operational theory `T`, tested
separately:

> **O1, the relative-phase resource.** `PhasesAvailable T`: at every level, the quarter phase on
> every state is an available operation.
>
> **O2, the continuous coherent transition resource.** `LayerFlowExecutable T σ` for one involution
> `σ` with a moved configuration: its gate flow available at every level and every real time.

With the closure, O1 and O2 together give phase-free richness and quantum mechanics
(`phaseFree_of_phases_layerFlowExecutable`, `qm_of_derivedOI_layerFlowExecutable`); quantum mechanics
gives both (`derivedOI_layerFlowExecutable_of_qm`). A candidate that survives must establish O1 and
O2 as two independent positive obligations, and only then may the existing kernel compose them.
A candidate is never defined by its output.

## Three admissible outcomes, frozen

- **A, single condition.** One independently checkable partition-level condition survives the
  kill battery and provably sources both O1 and O2 through an explicitly stated map from partition
  data to admissible implementation structure.
- **B, two-condition obstruction.** No single tested realization property does both jobs; the
  phase and the continuous coherent flow separate at realization level as they do operationally.
- **C, underdetermined.** The corpus does not state a sourcing map rich enough to decide either
  candidate without introducing new physical structure.

## The necessary tests every candidate must pass, frozen

1. **Level.** It is a property of the visible–hidden realization or partition, not merely of the
   update `(S, φ)`: a property of the update alone reaches the observer through the stipulated
   sourcing, lands in a configuration-level class, and fails phase-free richness
   (`configurationLevel_not_phaseFree`).
2. **Non-monomiality through the map.** Through its sourcing map it makes the generated
   implementation class non-configuration-level, supplying a non-monomial admissible operator
   somewhere (`exists_nonMonomial_of_layerFlowExecutable`, the necessary condition).
3. **The substratum-theory countermodel.** It excludes the theory with the phase and no flow
   (`substratumTheory_derivedOI`, `substratumTheory_not_layerFlowExecutable`).
4. **The ones-fixing countermodel.** It excludes the theory with every flow and no phase
   (`onesTheory_layerFlowExecutable`, `onesTheory_not_phasesAvailable`, `onesTheory_not_qm`).
5. **The remaining witnesses.** It excludes the permutation theory (`permTheory`, configuration-level)
   and the five witnesses of `five_way_minimality`, each realizing the sealed OI core and failing
   one condition of the finite completion.
6. **Not the read-write family.** It does not merely reproduce the continuously parameterized
   read-write family, permutation-valued at every parameter (`readWriteOperator_eq_perm`).
7. **Vocabulary.** Its definition mentions none of: quantum mechanics, `PhaseFreeRichness`,
   `PhasesAvailable`, `LayerFlowExecutable`, non-monomiality, availability. Those are tests and
   consequences.
8. **The map, stated.** If it survives, the round states explicitly the map from partition data to
   admissible implementation structure that its sourcing uses; a geometric structure is not an
   intervention until that map is written down, and the round records whether the corpus supplies
   the map or the round does.

A candidate that fails any of 1–7 is dead; one that passes 1–7 and lacks 8 is underdetermined.

## The two candidate families, frozen

**Candidate 1, tunable coupling.** The corpus's version is a negative control already decided: the
read-write family has a continuous parameter and a permutation matrix at every value, so the class
it generates is bijection-level, executes no layer flow (`bijectionLevel_not_layerFlowExecutable`)
and, being ones-fixing, has no quarter phase (`permClass_onesFixing`). The corpus's other
continuous object, the continuous-time visible transition matrix `T(t)` of `[Main §2.2]` that
"departs from the permutation class", is a stochastic matrix on visible states, whose Kraus form
has monomial operators and preserves diagonal states (`stochasticChannel_kraus_monomial`,
`stochasticChannel_preservesDiag`). The only live version is a coupling whose intermediate values
are not bijection-valued on configurations, and the round asks whether any physical condition the
corpus states forces such a sourcing map. It does not postulate one.

**Candidate 2, symplectic partition structure.** The substratum's per-site state is a pair
`V × V`, the current and the previous value, and the one-step map is the leapfrog
`leapEquiv R.F`, the shear layer `(a, b) ↦ (F(b) − a, b)`, which replaces the previous value by the
update minus it, composed with the swap layer `(a, b) ↦ (b, a)`; for a symmetric coupling this is a canonical transformation of the discrete
phase space. That fact alone is update-level and inert by test 1. The partition-induced version is
the live one: a polarization of the per-site phase space into a position half, which the observer
reads, and a momentum half, with the observer's state space the amplitudes over positions, and the
sourcing map the Weil representation of the substratum's canonical layers on that space. Under
this map, a shear with a quadratic generating form goes to a diagonal phase in the positions,
carrying the coupling's neighbour terms as relative phases, and the swap goes to the finite Fourier
transform, which is not monomial. The round tests this map on the two-valued alphabet, where the
shear image is the quarter phase and the swap image is the Hadamard matrix, and asks three things
in order: whether the sourced class passes test 2, whether it supplies O1, and whether it supplies
O2. The expected obstruction for O2 is finiteness: over a finite alphabet the symplectic group and
its Weil image are finite, and a finite group of operators contains no continuous one-parameter
family; the round states this and records what the kernel proves of it.

**What the candidates are not allowed to become.** Neither candidate is adopted by being named. A
candidate whose "sourcing map" is the reading of a representation as an availability fails test 8
and is recorded as a representation, as the lift-source audit recorded the coherent completion.

## The tests, each with its admissible outcomes

**T0. The obligations and their independence.** Kernel: O1 and O2 together with the closure give
quantum mechanics, and quantum mechanics gives both (cited); O1 without O2 and O2 without O1 are
each consistent, the substratum theory and the ones-fixing theory being the witnesses
(`obligations_independent`, packaged from the cited results). Admissible outcome: the theorem.

**T1. The kill battery, packaged.** Kernel: one predicate `KillBattery T` listing the theories a
candidate's sourced theory must differ from, with the reason each is not quantum
(`killBattery_substratum`, `killBattery_ones`, `killBattery_perm`); and the statement that any
theory satisfying O1 and O2 within the closure lies outside the battery
(`obligations_outside_battery`). Admissible outcome: the theorems.

**T2. Candidate 1, the negative control.** Kernel: the theory generated by any bijection-level
class fails both obligations (`bijectionLevel_fails_obligations`, from
`bijectionLevel_not_layerFlowExecutable` and the ones-fixing phase obstruction); the corpus's
continuous-time visible law is a classical map (cited). The live version: the round records that
the corpus states no physical condition forcing a non-bijection-valued coupling, or names one.
Admissible outcome: the theorem and the record, or a named condition, which then enters T4.

**T3. Candidate 2, the update-level fact is inert.** Kernel: any class the canonical structure of
the update reaches through the stipulated sourcing is configuration-level and fails O1 and O2
(`updateLevel_symplectic_inert`, a corollary of `configurationLevel_not_phaseFree` and
`configurationLevel_not_layerFlowExecutable`). The symplecticity of the leapfrog map itself is
stated as a mathematical fact and not proved in this round. Admissible outcome: the corollary.

**T4. Candidate 2, the polarization map on the two-valued alphabet.** Kernel, on the site carrier
`Fin 2` and its levels: the polarization map is defined explicitly as a function from the two
layers to matrices (`weilImage`), the shear to the quarter phase `phaseGate` and the swap to the
Hadamard matrix `hadamard`; the Hadamard matrix is not monomial (`hadamard_not_monomial`) and does
not preserve diagonal states (`hadamard_not_preservesDiag`); the class generated by the
substratum's monomials together with the two images is not configuration-level
(`polarizedClass_not_configurationLevel`), so test 2 passes; the quarter phase is in the class at
every level on every state, so O1 holds for the polarized theory (`polarizedTheory_phasesAvailable`),
where the level-wise phases are obtained from the site phase by the exchanges. Admissible outcome:
the theorems; or a failure of O1 at some level, named with the reason.

**T5. Candidate 2, the flow.** Whether the polarized theory satisfies O2. Admissible outcomes, in
order of strength: (a) a kernel theorem that the polarized theory executes no layer flow of an
involution with a moved configuration (`polarizedTheory_not_layerFlowExecutable`), through an
invariant of the finite class, the entries of every generated operator lying in a finite set the
flow leaves at some time; (b) the finiteness obstruction stated as a mathematical fact, the Weil
image of a finite symplectic group being a finite group and a finite group containing no
one-parameter family of distinct operators, with the missing kernel step named exactly; (c) the
theorem that the polarized theory does execute a layer flow, which would send candidate 2 to
outcome A pending test 8.

**T6. Test 8 for candidate 2.** The round records whether the corpus supplies the polarization
map: whether any manuscript states that the observer's state space is the amplitudes over one
half of the per-site phase space and that the layers act on it by the Weil representation. The
expected record is that it does not: the corpus's carrier is the full configuration space, its
sourcing the stipulated bijective and phase interventions. Admissible outcome: the record, either
way.

**T7. The verdict.** From T0–T6, exactly one of A, B, C, stated with its reason; if B, the two
sides separated, phase from the discrete symplectic polarization and flow from a continuous
parameter, each with the countermodel that shows the other side missing; if C, the map the
corpus does not supply named.

**T8. The surfaces and the checks.** Module `OIBridge/C5Discovery.lean`, defining the battery
predicate, the polarization map and the polarized class and nothing named "C5"; guard `R7-C5D`
pinning the theorems, this note's order, outcomes, tests, candidates and non-claims, and
rejecting any adoption of a C5 in the note or the kernel; README paragraph and counts; the census
carries the family as kernel-only with no anchor. Full build; every result printing only
`propext`, `Classical.choice`, `Quot.sound`; the release gate; the probe; the census. No manuscript
is edited. Admissible outcome: all green.

## What the outcomes mean, fixed in advance

**If B.** The two resources separate at realization level: a discrete symplectic polarization of
the coupling sources the relative phase and a non-monomial operator, and a continuous parameter
sources motion between endpoints, and no single tested realization property does both. The
frontier is then stated as two realization-level properties rather than two operational
assumptions, which is progress in the manuscripts' own terms, and the next question is whether a
continuous canonical structure, a realization the corpus does not state, would join them.

**If C.** The corpus has the structure to state the candidates and not the map; the round records
the map each would need, and no C5 candidate is adopted.

**If A.** A C5 candidate is recorded with its map, its passage of the battery and its two
obligations; adoption as a condition, its naming, and its propagation are separate owner
decisions in a later round.

**What no outcome establishes.** That a C5 exists or does not exist beyond the two candidate
families tested. Minimality or uniqueness of anything. Anything about a manuscript. That the
polarization map is physically available to the observer: the round states the map and tests
its consequences; availability of its images is not derived from the stated access.

## What the round does not do

Adopt or name a C5. Place a gate flow, a phase or a non-monomial operator in a class by hand
except as the explicitly stated image of the polarization map under test. Read availability off
a representation. Change `LayerFlowExecutable`, `PhasesAvailable`, `obsTheory`, `substratumTheory`
or any definition. Attempt the phase by a route other than the two candidates. Edit a manuscript.
Refresh the transfer bundle.
