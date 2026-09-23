# The phase-source audit — does the stated substratum and observer access derive the phases?

`OIBridge/PhaseSource.lean` (the pass), `OIBridge/SubstratumInterface.lean` (the round-62
interface: `bijectiveOperator`, `phaseOperator`, `IsMonomial`), `OIBridge/StructuralClosure.lean`
(`substratumClass`, `phaseOperator_supplied`), `OIBridge/RouteB.lean` (`PhasesAvailable`,
`DerivedOI`, `substratumTheory_derivedOI`), `OIBridge/SubstratumInterfaceAudit.lean` (the
`Substratum` structure, `permClass`, `SourcedOI`, `derivedOI_iff_sourcedOI_phases`,
`bijectionLevel_not_phasesAvailable`), `OIBridge/ReadWriteControl.lean` (`ReadWriteFamily`,
`readWriteOperator`), `OIBridge/LiftAudit.lean` (`gateFlow`, `LayerFlowExecutable`),
`OIBridge/InstrumentRealization.lean` (`OnesFixing`, `instAvail_unitary_fixes_ones`, `onesClass`),
`OIBridge/FlowEndpoint.lean` (`onesTheory`, `phaseGate_mulVec_ones`);
`SUBSTRATUM-SOURCE-AUDIT.md`, `SUBSTRATUM-INTERFACE-AUDIT.md`, `FLOW-ENDPOINT-AUDIT.md`; guard
`R7-PHASE` in `verification/lean/edge_rigidity_probe.py`.

**Status: pass complete. Negative for the stated access: every operation the manuscripts state is ones-fixing and the kernel's `PhasesAvailable` on the substratum side rests on the round-62 phase intervention alone; underdetermined for the phrase "the phase structure", with the necessary condition and the tested sufficient access named under the scope amendment recorded below.** Written from `main` at commit `b1c0677`, the merge
of the flow-endpoint round. The sections below fix the question, the distinctions, the census of
every purported source of the phase structure in the corpus and the kernel, the criteria that
decide the outcome, the tests with their admissible outcomes and the countercontrol, before any
kernel work; the outcome section is added afterwards and records where a proved statement differs
from the preregistered one. Nothing here is a manuscript claim.

## The question

The flow-endpoint round decided `SourcedOI ∧ LayerFlowExecutable ⇏ PhaseFreeRichness`. The
stronger arrow, `DerivedOI ∧ LayerFlowExecutable ⟹? PhaseFreeRichness`, is the lift audit's
preregistered Q3 and stays open. The difference between the two hypotheses is one conjunct,
`PhasesAvailable` (`derivedOI_iff_sourcedOI_phases`): the quarter phase on every state at every
level. Before that arrow is attacked, the round asks where the conjunct comes from:

> Does the stated substratum and observer access derive `PhasesAvailable`, rather than assume it?

The question is narrow. It is not whether a diagonal complex representation exists
mathematically, nor whether phases can be reconstructed from transition data, nor whether the
emergent description carries a gauge group with `U(1)` factors. It is whether the machinery the
manuscripts actually state, the substratum `(S, φ)` and the operations an embedded observer
performs on it, supplies an executable relative-phase intervention at every level that
`PhasesAvailable` requires, under the migrated semantics in which availability is instrument
realization by an admissible class.

## Four distinctions, frozen at the outset

**(D1) Gauge is not an intervention.** A transformation of the substratum that preserves the
emergent physics, an element of the substratum gauge group `𝒢_sub` of `[Substratum §4]`, is a
statement about which descriptions are equivalent. An executable intervention is an admissible
operator the observer can select. The first does not supply the second.

**(D2) A representation fact is not availability.** That a phase is determined by continuous-time
transition data (`[Main §3.1]`, the phase-locking lemma), that a diagonal rephasing of the reconstructed
Hamiltonian moves no modulus (`[GR §3.3]`, the residual family), that every finite stochastic law
has a fixed-basis unitary/Born representation: each is a fact about representations of data
already available, and none is the availability of a phase rotation as an operation.

**(D3) A global phase is not the resource.** A scalar of modulus one acts trivially on every
conjugation channel. The resource `PhasesAvailable` names is the relative phase, `phaseGate a`, a
diagonal unitary that is not a scalar and whose conjugation is not the identity; equivalently, a
diagonal unitary that moves the all-ones vector off its ray.

**(D4) Availability is instrument realization.** A phase counts as derived only if its
conjugation is available in the theory the stated access generates, under `InstAvail`: an
admissible isometric step, a register readout, coarse-graining, feed-forward, a uniform ancilla
discard, and nothing else. A phase manufactured by recombining branches, by choosing a
representation, or by a global gauge is not derived.

## The census of purported sources, taken before the pass

Every place in the corpus and the kernel where the phase structure enters or is said to enter,
with its classification under the distinctions. The classification is the preregistration's
reading; the tests decide it.

| source | where | what it says | classification |
|---|---|---|---|
| P1, the phase intervention | `SubstratumInterface.phaseOperator`, `phase_monomial`; `StructuralClosure.substratumClass`, `phaseOperator_supplied`; `RouteB.substratumTheory_derivedOI` | the round-62 interface records "bijective and phase interventions" as the substratum's two intervention kinds, the phase intervention's operator a diagonal `phaseOperator d`; the monomial class `substratumClass` contains every such operator, and the kernel's `PhasesAvailable` on the substratum side is proved from `phase_monomial` | a stipulation of the kernel: an intervention kind added at the interface, derived from nothing in `(S, φ)` |
| P2, the substratum-source sentence | `[GR §3.3]`, substratum-source form: "The concrete OI substratum — finite states, bijective microscopic dynamics (Axiom 2), and the phase structure — supplies the structural part in full"; "the reversal of a phase is its conjugate" | lists the phase structure among what the substratum supplies, citing the kernel's `phaseOperator_monomial` and `phaseOperator_conjTranspose` | narrates P1 |
| P3, the substratum gauge group | `[Substratum §4]`, Theorem 24: relabelling, alphabet change, deep-sector enlargement, graph isomorphism; the subsumed families: time reversal, hidden-sector reparametrization, "visible-sector emergent global phase (`U → e^{iθ}U`): at the substratum level `S` is a finite set with no complex structure; the emergent phase is trivially the identity on `(S, φ)`" | the manuscripts' own statement that the substratum carries no complex structure and that the emergent phase is a description-level identity | (D1), (D3): gauge, and global |
| P4, the internal-index and amplitude-scale gauge | `[Substratum §3.1]` A5 (amplitude-scale gauge invariance), A6 (invariance under spatially varying internal-index transformations); `[Substratum §3.3]`(d), the emergent gauge group `U(3) × U(2) × U(1)` as the unitary group of a block algebra | symmetries of the dynamics and of the emergent description | (D1): gauge of the description, no operation named |
| P5, the reconstruction gauge | `[GR §3.3]`: "diagonal rephasing moves no modulus, the energy origin is a global phase"; `[Main §3.1]`, the phase-locking lemma: phases determined by continuous-time data up to "physically irrelevant basis rephasing" | facts about the reconstructed representation of transition data | (D2), (D3): representation, and global |
| P6, the fixed-basis representation | `[Main §3.4]`, `S ⟺ D ⟺ Q_fb`; `[book ch. 1]`, "the Born rule in the fixed-basis representation is part of the representation dictionary" | a representation of every finite stochastic law | (D2): representation |
| P7, the observer's stated access | `[Main §1.2]`, an observation `(S, φ, V)`, the observer registers changes; C1–C4; `[GR §3.3]`, "finite bijective read-write dynamics"; kernel: `readVisible`/`localLuders`, `ReadWriteFamily`, `readWriteOperator`, the sourced class `permClass` (`permClass_le_of_exchanges`), the observer theory `obsTheory` | readout of the visible sector and bijective couplings; every operator supplied is a permutation matrix; the class they generate carries no phase (`bijectionLevel_not_phasesAvailable`) | executable, and ones-fixing |
| P8, the continuous-time extension and the layer flows | `[Main §2.3]`, `T_ij(t)` continuous; CT2 (`CONTINUOUS-TIME-AUDIT.md`); `LayerFlowExecutable`, a hypothesis throughout | the gate flow of a layer involution, `1 + (e^{iπt} − 1)(1 − P)/2`, carries complex entries; under executability it is an available unitary at every level | executable under the hypothesis, and ones-fixing (`gateFlow_mulVec_ones`); the ones-fixing theory with every gate flow has no phase (`onesTheory_not_phasesAvailable`) |
| P9, the observer architecture's own operations | the constructors of `InstAvail`: readout of a register, coarse-graining, feed-forward, uniform ancilla attach and discard; the hidden sector of C3 | the operations every embedded observer performs, with no admissible step beyond the class | executable; they preserve the ones-fixing invariant (`instAvail_unitary_fixes_ones`) |

The census finds one entry that supplies a phase to the kernel, P1, and it is a stipulation. Every
executable route the manuscripts state, P7–P9, supplies ones-fixing operators and preserves the
ones-fixing invariant. The remaining entries are gauge, representation, or global phase. Whether
that reading is right is what the tests decide; whether a manuscript sentence names an access the
census has not formalized is the third outcome.

## The criteria, fixed in advance

The outcome is one of three, decided by the criteria below and nothing else.

**Positive.** Some operation the manuscripts state the observer performs, formalized as an
admissible operator or a protocol of admissible operators under `InstAvail`, has an available
conjugation equal to the quarter phase up to a global scalar, at every level with two or more
states. Then `PhasesAvailable` is derived, `DerivedOI` is a sourced baseline, and the lift audit's
Q3 from `DerivedOI` is the next theorem round.

**Negative.** Every operation the manuscripts state, formalized, lies in a class whose admissible
isometries fix the all-ones ray, and every remaining mention of the phase structure classifies as
gauge (D1), representation (D2) or global phase (D3). Then the stated architecture does not source
the phases: the kernel's `PhasesAvailable` on the substratum side rests on P1 alone, sourcing stops
at `SourcedOI`, and an executable relative-phase intervention is an additional physical assumption
on the route to quantum mechanics.

**Underdetermined.** Some manuscript sentence names an access to the substratum that the census
has not formalized and whose executable content the manuscripts do not specify, so that neither
the positive nor the negative criterion is met for it. Then the round names the missing access
exactly, as an operator condition, in place of the phrase "phase structure".

The three are not exclusive across sentences: the stated access can be negative while one
sentence is underdetermined. The outcome records the verdict per entry and the headline that
follows from the entries together.

## The tests, each with its admissible outcomes

**T1. The invariant, general.** `onesFixing_not_phasesAvailable`: for every architecture whose
admissible isometries fix the all-ones ray (`OnesFixing`), the generated theory has no quarter
phase at any level with two or more states, on every finite carrier with at least two states. The
mechanism is the instrument-realization audit's: an available unitary conjugation is
instrument-realized, its unitary fixes the ray (`instAvail_unitary_fixes_ones`), and the quarter
phase moves it (`phaseGate_mulVec_ones`). Admissible outcomes: the theorem, or a ones-fixing
architecture with an available quarter phase, which would refute the invariant.

**T2. The stated access is ones-fixing.** `permClass_onesFixing : OnesFixing permClass`: every
isometry in the sourced class is a unit scalar times a permutation matrix, and it fixes the ray.
With T1 this gives a second proof of `permTheory_not_phasesAvailable`, by the same invariant that
decides the flow endpoint, so that the two negatives are one mechanism. The kernel's bijective
interventions, read-write operators and relabellings are permutation matrices
(`permMatrix_mulVec_ones`, `readWriteOperator_mulVec_ones`) and the layer gate flows fix the ray
(`gateFlow_mulVec_ones`): every executable operator of P7 and P8 is ones-fixing. Admissible
outcomes: the theorems, or an executable operator of the stated access that moves the ray, named,
which is the positive outcome.

**T3. The distinctions, in the kernel.** (D3) `phaseGate_not_scalar`: on a carrier with two or more
states, `phaseGate a` is not a scalar multiple of the identity; `conjChannel_phaseGate_ne_id`: its
conjugation is not the identity; a unit scalar acts trivially on every conjugation channel
(`ReachabilitySeam.conjChannel_smul`). (D2) `diagonal_conj_phaseGate`: every diagonal unitary `D`
has `D * phaseGate a * Dᴴ = phaseGate a`, so a rephasing of the representation neither creates nor
removes the resource. Admissible outcomes: the theorems.

**T4. The stipulation, isolated.** `phaseGate_moves_ones` and `substratumClass_not_onesFixing`: the
kernel's phase intervention is admissible in `substratumClass` (`phase_monomial`), unitary, and
moves the all-ones ray; so the monomial class is not ones-fixing, and P1 is the one intervention
kind of the kernel's substratum interface that is not. Together with T2 this locates
`PhasesAvailable` on the substratum side in P1 and nowhere else in the kernel. Admissible
outcomes: the theorems, or a second non-ones-fixing intervention kind in the interface, named.

**T5. The manuscript census, per entry.** Each entry P1–P9 is decided by the criteria: positive,
negative, or underdetermined, with the sentence quoted. The expected verdicts are those of the
census table: P1 negative as a stipulation, P3–P6 negative under (D1)–(D3), P7–P9 negative by T1
and T2, and P2 the candidate for underdetermined, since "the phase structure" is not given
executable content by any manuscript sentence and is stated to be absent at the substratum level
by P3. Admissible outcomes: the verdicts as expected; or a positive entry, which decides the round
positively; or a different entry underdetermined, with the missing access named.

**T6. The countercontrol.** Three checks that a phase is not manufactured. Branch recombination:
availability is `InstAvail`, which has no sum constructor (`INSTRUMENT-MIGRATION-AUDIT.md`), and the
invariant of T1 is a theorem of that predicate. Representation choice: T3 (D2). Global gauge: T3
(D3). And the positive control: adjoining the quarter phase as an admissible operator does source
it, `substratumTheory_derivedOI`; so the criteria detect a phase when one is stipulated, and the
negative verdicts are not an artifact of the criteria. Admissible outcome: all four.

**T7. The surfaces and the checks.** Guard `R7-PHASE` pins the theorems of T1–T4, the absence of
any new intervention kind or class in the module, this note's order, census, criteria and
non-claims; `SUBSTRATUM-SOURCE-AUDIT.md` receives a fifth entry recording the verdict on its
"gauge/phase structure" escape route; `SUBSTRATUM-INTERFACE-AUDIT.md` receives a section
recording that the location of the phases it reported is decided; the README carries the
paragraph and the counts; the census carries the family as kernel-only with no anchor. Full
build; every result printing only `propext`, `Classical.choice`, `Quot.sound`; the release gate;
the probe; the census. No manuscript is edited: what the audit earns for `[GR §3.3]` is recorded
for the propagation round that follows, together with the two normalization sentences and the
five file attributions already listed. Admissible outcome: all green.

## What the outcomes mean, fixed in advance

**If the verdict is negative for the stated access.** Current OI sourcing stops at `SourcedOI`.
`DerivedOI` is `SourcedOI` with a stipulated conjunct, and the arrow the lift audit's Q3 asks about
has a hypothesis the substratum does not supply. The next theorem round is then a decision: attack
Q3 from `DerivedOI` as a conditional result whose extra hypothesis is named as an assumption, or
attack the sourcing of a relative-phase intervention as a physical principle. That decision is the
owner's and is not taken here.

**If one entry is underdetermined.** The round names the missing access as an operator condition:
an admissible operator, selectable by the observer at every level, that moves the all-ones ray, of
which the quarter phase is the canonical instance. The phrase "phase structure" in `[GR §3.3]` is
then requalified in the propagation round to that condition, as an assumption, and not
silently.

**If the verdict is positive.** `DerivedOI` is a sourced baseline, the substratum-source sentence
stands, and the lift audit's Q3 is the next round with no extra assumption.

**What no outcome establishes.** Whether relative phase is the unique or the minimal resource on
the route to quantum mechanics; the flow-endpoint audit records that it is an obstruction
identified and not more. Whether `DerivedOI ∧ LayerFlowExecutable` gives `PhaseFreeRichness`: the
lift audit's Q3, untouched. Whether a richer substratum ontology than `(S, φ)` with the stated
access, one the manuscripts explicitly do not claim completeness against (`[Substratum §4]`, the
scope of the completeness claim), would source a phase. Whether the observer-level lift is
derivable. Route A in either direction. Bare OI.

## What the round does not do

Define a new intervention kind, a new class, or a new theory. Change `PhasesAvailable`,
`DerivedOI`, `SourcedOI`, `substratumClass` or any package. Edit a manuscript. Decide the lift
audit's Q3. Attack the sourcing of a relative-phase principle. Propagate Route B. Refresh the
transfer bundle.

## Scope amendment, recorded after the preregistration

The preregistration above (commit `2cc1cbc`) is frozen and unchanged. One reading in it is
requalified before the outcome is recorded, at the owner's direction at review, quoted:

> The outcome/guard repeatedly names the missing access as "an admissible operator, selectable at
> every level, that moves the all-ones ray." The kernel proves this as an obstruction/necessary
> condition: a ones-fixing architecture cannot source `PhasesAvailable`, and the quarter phase
> moves the ray. It does not prove that an arbitrary non-ones-fixing operator is sufficient to
> source the quarter-phase family. A transition or other coherent unitary can move the ray without
> thereby furnishing `PhasesAvailable`. Moving the all-ones ray is a necessary condition for
> escaping this countermodel invariant; the canonical sufficient access tested here is the
> quarter-phase intervention itself (or, more generally, some explicitly proved repertoire that
> synthesizes `PhasesAvailable`). Do not describe the ray-moving condition alone as *the* missing
> access sufficient to source the conjunct.

So the sentences of the criteria and of the meanings section that say the round "names the
missing access" as an operator that moves the all-ones ray are read as follows. What T1 and T4
prove is a necessary condition: any access that sources `PhasesAvailable` must supply an
admissible operator that moves the all-ones ray, since a ones-fixing class supplies none. What
they do not prove is sufficiency: a transition flow at a quarter turn moves the ray and is
admissible in `onesClass`'s branch-wise closure, and the flow-endpoint audit's witness shows that
moving the ray by such an operator does not by itself furnish a quarter phase. The sufficient
access this round tests is the quarter-phase intervention itself, `phaseOperator`, whose
adjunction sources the conjunct (`substratumTheory_derivedOI`, the positive control of T6); any
other sufficient access is a repertoire explicitly proved to synthesize `PhasesAvailable`, and
none is proved here. The outcome below and every outcome-facing surface state the condition in
that form; no theorem changes.

## The outcome

Preregistration commit `2cc1cbc`, scope amendment above. The kernel module is `OIBridge/PhaseSource.lean`, ten named
results, each printing only `propext`, `Classical.choice`, `Quot.sound`. Every test reached the
outcome expected in advance; no proved statement differs from the preregistered one.

| test | outcome | kernel |
|---|---|---|
| T1 | the invariant, general: for every architecture whose admissible isometries fix the all-ones ray, the generated theory has no quarter phase at any level with two or more states, on every carrier with at least two states, by the instrument-realization audit's invariant and `phaseGate_mulVec_ones` | `onesFixing_not_phasesAvailable` |
| T2 | the stated access is ones-fixing: an isometry among the scaled partial permutations has one nonzero entry, the common scalar, in every row, so the sourced class is ones-fixing; its theory has no quarter phase by T1, the same mechanism that decides the flow endpoint; the bijective interventions, the read-write operators and the layer gate flows fix the all-ones vector | `permClass_onesFixing`, `permTheory_not_phasesAvailable_onesFixing`, `bijectiveOperator_mulVec_ones`, `readWriteOperator_mulVec_ones`, `gateFlow_mulVec_ones` |
| T3 | the distinctions: the quarter phase is not a scalar and its conjugation is not the identity, multiplying the coherence from its state to any other by `i`; every diagonal unitary fixes it under conjugation; a unit scalar acts trivially on every conjugation channel | `phaseGate_not_scalar`, `conjChannel_phaseGate_ne_id`, `diagonal_conj_phaseGate`, `ReachabilitySeam.conjChannel_smul` |
| T4 | the stipulation, isolated: the quarter phase moves the all-ones ray, and the monomial class of the round-62 interface, which admits it as a phase intervention, is not ones-fixing; it is the one intervention kind of the interface that is not, and the one the kernel's `PhasesAvailable` on the substratum side rests on | `phaseGate_moves_ones`, `substratumClass_not_onesFixing` |
| T5 | the census, per entry: the verdicts below, as expected; no entry positive; P2 underdetermined, with the necessary condition and the tested sufficient access named, under the scope amendment | the table below |
| T6 | the countercontrol: no sum constructor in `InstAvail`, the invariant a theorem of that predicate; the representation and the global-gauge checks of T3; and the positive control, that adjoining the quarter phase as an admissible operator does source it | `INSTRUMENT-MIGRATION-AUDIT.md`, T3, `substratumTheory_derivedOI` |
| T7 | the surfaces and the checks: `R7-PHASE`; the sections in `SUBSTRATUM-SOURCE-AUDIT.md` and `SUBSTRATUM-INTERFACE-AUDIT.md`; the README and the census; full build, axiom check, release gate, probe, census, all green; no manuscript edited | `verification/lean/edge_rigidity_probe.py` |

**The verdicts, per entry.**

| entry | verdict | reason |
|---|---|---|
| P1, the phase intervention | negative, a stipulation | `phaseOperator` is an intervention kind declared at the round-62 interface; nothing in `(S, φ)` or in the stated access produces it, and it is the one kind of the interface that moves the all-ones ray (T4) |
| P2, the substratum-source sentence | **underdetermined** | "the phase structure" narrates P1 and names no operation the observer performs; no manuscript sentence gives it executable content, and `[Substratum §4]` states that the substratum carries no complex structure |
| P3, the substratum gauge group | negative | gauge (D1); the emergent global phase is the identity on `(S, φ)` and global (D3) |
| P4, the internal-index and amplitude-scale gauge | negative | gauge of the description (D1); no operation named |
| P5, the reconstruction gauge | negative | representation (D2), and the energy origin a global phase (D3); the reconstructed diagonal rephasing fixes the quarter phase under conjugation (T3), so it neither creates nor removes the resource |
| P6, the fixed-basis representation | negative | representation (D2) |
| P7, the observer's stated access | negative | every operator supplied is a permutation matrix, ones-fixing (T2); the class they generate has no quarter phase (T1, T2) |
| P8, the continuous-time extension and the layer flows | negative | under the hypothesis `LayerFlowExecutable`, the gate flows are ones-fixing, and the ones-fixing theory with every gate flow has no quarter phase (`onesTheory_not_phasesAvailable`, T1) |
| P9, the observer architecture's own operations | negative | the constructors of `InstAvail` preserve the ones-fixing invariant (`instAvail_unitary_fixes_ones`) |

**The headline.** For the stated access the verdict is negative: every operation the manuscripts
state the observer performs, formalized, lies in a class whose admissible isometries fix the
all-ones ray, and the operations of the observer architecture preserve that invariant; so the
stated substratum and observer access do not derive `PhasesAvailable`. The kernel's
`PhasesAvailable` on the substratum side rests on P1, a stipulation, and on nothing else. Current
OI sourcing stops at `SourcedOI`; `DerivedOI` is `SourcedOI` with a stipulated conjunct; and an
executable relative-phase intervention is an additional physical assumption on the route to
quantum mechanics, not a consequence of `(S, φ)` with the stated access.

**The missing access, under the scope amendment.** For P2 the verdict is underdetermined, and
the round states what the phrase "the phase structure" would have to supply, in two parts that
are not to be conflated. The necessary condition: any access sourcing the conjunct supplies an
admissible operator, selectable by the observer at every level, that moves the all-ones vector off
its ray, since T1 says a ones-fixing class supplies none. The sufficient access tested: the
quarter-phase intervention `phaseOperator` itself, whose adjunction sources the conjunct
(`substratumTheory_derivedOI`); more generally, a repertoire explicitly proved to synthesize
`PhasesAvailable`, of which none is proved here. Moving the ray is not by itself sufficient: the
quarter-turn transition flow moves it and furnishes no quarter phase (the flow-endpoint witness).
Whether the manuscripts' `[GR §3.3]` sentence is to be requalified to the quarter-phase
intervention stated as an assumption is recorded for the propagation round that follows; nothing
is changed here.

**What the outcome establishes.** Under the migrated semantics, no route the manuscripts state,
gauge, representation, global phase, readout, bijective write access, the layer flows under
executability, or the observer architecture's own attach, readout, feed-forward and discard,
yields a relative phase; the one route that does is a declared intervention kind. The two
negatives of the programme, the flow endpoint and the phase source, are one mechanism: the
all-ones ray. The decision that follows, whether to attack the lift audit's Q3 from `DerivedOI`
as a conditional result with its extra hypothesis named as an assumption, or to attack the
sourcing of a relative-phase intervention as a physical principle, is the owner's.

**What the outcome does not establish.** That an operator moving the all-ones ray suffices to
source `PhasesAvailable`: the condition is necessary, and the sufficient access tested is the
quarter-phase intervention itself. Whether relative phase is the unique or the minimal resource
on the route; the flow-endpoint audit records it as an obstruction identified and not more. Whether `DerivedOI ∧ LayerFlowExecutable` gives `PhaseFreeRichness`. Whether a richer
substratum ontology than `(S, φ)` with the stated access would source a phase; the manuscripts
claim no completeness against one, and none is examined. Whether the observer-level lift is
derivable. Route A in either direction. Bare OI. Any manuscript sentence.

## What this note does not claim

That moving the all-ones ray is sufficient to source `PhasesAvailable`, or that the ray-moving
condition alone is the missing access. That the manuscripts are wrong: they state that the substratum carries no complex structure, and
the round agrees with them. That `DerivedOI` is false of the physics, or that the phases cannot be
sourced by some access the manuscripts do not state. That the lift audit's Q3 from `DerivedOI` is
refuted or holds. That relative phase is the unique or minimal missing resource. That anything
here reaches a manuscript.

## The decision that followed, recorded after the round

The owner took the first option named under "If the verdict is negative for the stated access":
the lift audit's Q3 from `DerivedOI`, attacked as a conditional result with `PhasesAvailable`
named as an assumption. The Q3 round (`DERIVED-Q3-AUDIT.md`, preregistration commit `f206058`)
decides it in the constructive branch: under `DerivedOI`, the executability of one layer flow of an
involution with a moved configuration gives phase-free richness
(`phaseFree_of_derivedOI_layerFlowExecutable`), the phase hypothesis consumed at one step, the
sign flip on one configuration of the chosen pair, which is the square of the quarter phase
(`phaseGate_mul_self`). The second option, the sourcing of a relative-phase intervention as a
physical principle, is not taken up and stays open; nothing in this note changes.
