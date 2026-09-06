# The Q3 round — phase-free richness from the closure and one executable layer flow

Owner-called, written from `main` at `f80688e`, the merge of the phase-source propagation.
Preregistered here and committed alone before any proof is attempted. The kernel object is the
lift audit's preregistered Q3 (`LIFT-AUDIT.md`), left open by that pass, by the flow-endpoint pass
and by the phase-source pass, and stated with `PhasesAvailable` as an explicit extra hypothesis:
the phase-source audit established that the stated substratum and observer access do not derive
it, so `DerivedOI` is `SourcedOI` with a stipulated conjunct, and the arrow below is a conditional
question with that conjunct named.

## The frozen question

For a finite carrier `S`, a theory `T : FiniteOperationalTheory S`, and an involution
`σ : Equiv.Perm S` with a moved configuration:

> **Q3.** `DerivedOI T ∧ LayerFlowExecutable T σ ⟹? PhaseFreeRichness T`

with `DerivedOI` the consequence closure of `RouteB` (reversible implementation locality, embedded
observation, the exchanges, the phases and the read-write operators at every level),
`LayerFlowExecutable T σ` the executability at every level and time of the gate flow of the layer
involution with the ancilla a spectator (`LiftAudit`), and `PhaseFreeRichness` the second
primitive-source principle (`MinimalRepertoire`): at every level with two or more states some pair
is continuously driven and every exchange is available.

**The hypotheses on the involution, fixed.** `σ` is an involution (`∀ x, σ (σ x) = x`) and moves a
configuration (`∃ x, σ x ≠ x`), the hypotheses of the lift audit's Q3′. Both are necessary for the
question to be one: the gate flow of the identity is the identity at every time, so
`LayerFlowExecutable T 1` holds in every theory, in particular in the substratum theory, which
satisfies `DerivedOI` and fails phase-free richness (`routeB_target`). The identity case is the
countercontrol C2 below, proved and not merely noted.

## Three distinctions, frozen

**(D1) The phase hypothesis is used materially.** The flow-endpoint pass refuted the same arrow
from `SourcedOI` (`flow_endpoint_refuted`): a ones-fixing theory executes every layer flow and
drives no pair. Any positive proof of Q3 therefore consumes `PhasesAvailable` at an identified
step, and the round records that step; a proof that does not consume it would contradict the
flow-endpoint theorem and is inadmissible.

**(D2) Sufficiency of the quarter phase as a sourced access is not sufficiency for the
repertoire.** The phase-source pass and its propagation established that the quarter-phase
intervention, when stipulated, sources `PhasesAvailable`; they do not establish that
`PhasesAvailable` together with one executable layer flow supplies the continuous transition
repertoire. That is what this round has to prove or refute, and nothing from those passes is
cited as if it settled it.

**(D3) The target is phase-free richness.** Neither the failure of the all-ones invariant nor the
availability of some non-monomial unitary is the target. The target is `PhaseFreeRichness T` as
literally defined: at every level with two or more states, one pair with its full transition flow
`flow (transition a b) t` for every real `t`, and every exchange.

## The attack, fixed in advance

**The constructive branch.** Combine the quarter phases with the gate flow of the involution to
isolate one transition flow at every level. The lift audit's isolation identity
(`gateFlow_isolation`) multiplies the gate flow by its sign-conjugate and removes the scalar the
cancellation leaves with a diagonal phase `e^{−iπt}` on the moved configurations; that phase is a
continuous diagonal the substratum's availability supplies and the quarter phases do not, which is
why the lift audit proved Q3′ and left Q3 open. The mechanism fixed here replaces the continuous
phase by time reversal, which `LayerFlowExecutable` supplies for free since it quantifies over
every real time:

> **The sign-flip identity, to be proved.** For an involution `τ`, a moved configuration `a` with
> `b = τ a`, and `D` the diagonal with `−1` at `b` and `1` elsewhere,
>
> `gateFlow τ t · (D · gateFlow τ (−t) · D) = flow (transition a b) (π t)`.
>
> On the chosen pair the sign conjugation reverses the rotation of the time-reversed flow and
> leaves its scalar, so the two rotations add and the scalars cancel; on every other moved pair
> the sign acts trivially and the flow meets its own inverse; on the fixed configurations
> nothing moves. No continuous phase enters.

`D` is the square of the quarter phase on `b` (`phaseGate b * phaseGate b`), available at every
level under `PhasesAvailable` through the composition of available one-outcome operations. This is
the step at which the phase hypothesis is consumed (D1): the sign flip on one configuration of the
chosen pair. Every factor of the identity is then available under the hypotheses, so the
transition flow on the pair `(x, 0), (σ x, 0)` at level `n` is available at every real angle, and
the exchanges are a conjunct of `DerivedOI`. The mechanism is fixed with its algebra so that the
proof cannot drift: in the orbit calculus of the lift audit (`orb`, `orb_mul`, `gateFlow_eq_orb`,
`diagonal_mul_orb_mul_diagonal`, `flow_transition_eq_orb`), with `e₁ = e^{iπt}` and
`e₂ = e^{−iπt}`, the diagonal coefficient of the product is `(1 + e₁)(1 + e₂)/4 + (e₁ − 1)(e₂ − 1)/4 = 1`
on a non-chosen moved configuration and `(1 + e₁)(1 + e₂)/4 − (e₁ − 1)(e₂ − 1)/4 = cos πt` on the
chosen pair; the antidiagonal coefficient is `0` off the chosen pair and `−(e₁ − e₂)/2 = −i sin πt`
on it.

**The negative branch.** If the sign-flip identity fails for some involution, or if the isolated
matrix is not the transition flow, the round does not patch the mechanism: it builds the
countertheory, a theory satisfying `DerivedOI` and executing the layer flow of an involution with
a moved configuration while failing phase-free richness, and refutes Q3
(`derivedQ3_refuted`). The candidate would be the theory generated by the smallest architecture
containing the monomial class and the gate flows of `σ` at every level, with the obstruction to
be identified by an invariant that the quarter phases and the gate flow preserve and the transition
flow does not. This branch is preregistered so that a negative result is a decision and not a
failure to prove; the expected branch, from the algebra above, is the constructive one.

**The endpoint, conditional on the constructive branch.** Under `DerivedOI T` alone, for an
involution with a moved configuration, `ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ`
(`derivedOI_qm_iff_layerFlowExecutable'`), from `derivedOI_qm_iff_phaseFree` and Q3 one way and
`layerFlowExecutable_of_control` the other: the lift audit's preregistered Q4, at its own
hypothesis, with the baseline `DerivedOI ∧ SubstratumAvail` of Q4′ replaced by `DerivedOI`. The
swap-layer instances follow on `Conf Λ (V × V)`.

## The countercontrols, fixed in advance

**C1, the phase hypothesis is necessary.** `flow_endpoint_refuted` (the flow-endpoint pass):
`SourcedOI` with the executable swap flow does not give phase-free richness. Cited, not re-proved;
the theorem of this round is stated with `PhasesAvailable` and `ExchangesAvailable` as its
hypotheses, so the citation shows the first cannot be dropped.

**C2, the moved-configuration hypothesis is necessary.** The gate flow of the identity is the
identity at every time (`gateFlow_one_eq_one`), so `LayerFlowExecutable T 1` holds in the
substratum theory on the two-state carrier (`substratumTheory_layerFlowExecutable_one`), which
satisfies `DerivedOI` and fails phase-free richness: a theory with `DerivedOI`,
`LayerFlowExecutable T 1` and `¬ PhaseFreeRichness T` exists (`derivedOI_layerFlowExecutable_one_not_phaseFree`).

**C3, the diagonal used is a fourth root of unity.** The diagonal of the identity is the square of
one quarter phase (`phaseGate_mul_self`), with entries `±1`; the module cites neither `phaseFun`
nor `SubstratumAvail`, and the guard checks it.

**C4, consistency.** Quantum mechanics satisfies both hypotheses (`derivedOI_of_qm`,
`layerFlowExecutable_of_control`) and the conclusion; the endpoint theorem is not vacuous.

## The tests, fixed in advance

**T1. The sign-flip identity.** `gateFlow_isolation_flip`, as displayed, for every involution,
moved configuration and real time. Admissible outcome: the theorem, or the negative branch.

**T2. The diagonal from the quarter phases.** `phaseGate_mul_self`: the square of the quarter phase
on `b` is the diagonal with `−1` at `b`; its conjugation is available at every level under
`PhasesAvailable` (`flip_avail`). Admissible outcome: both.

**T3. Q3.** `phaseFree_of_phases_layerFlowExecutable`: from `PhasesAvailable T`,
`ExchangesAvailable T`, an involution with a moved configuration and `LayerFlowExecutable T σ`,
`PhaseFreeRichness T`; and `phaseFree_of_derivedOI_layerFlowExecutable` from `DerivedOI T`.
Admissible outcome: the theorems, or `derivedQ3_refuted`.

**T4. The endpoint.** `derivedOI_qm_iff_layerFlowExecutable'` under `DerivedOI T` alone, and
`qm_of_derivedOI_layerFlowExecutable`; the swap-layer instances. Admissible outcome: the theorems,
conditional on T3 positive.

**T5. The countercontrols.** C1 cited; C2, C3, C4 proved as named. Admissible outcome: all.

**T6. The lift audit's record.** The theorems of this round are stated at the lift audit's
preregistered hypothesis and not at the strengthened one; `LIFT-AUDIT.md` and
`PHASE-SOURCE-AUDIT.md` receive a section each recording the decision, placed after their frozen
text. Admissible outcome: both.

**T7. The surfaces and the checks.** Module `OIBridge/DerivedQ3.lean`, no new intervention kind,
class or theory; guard `R7-Q3`; README paragraph and counts; census family kernel-only with no
anchor; full build; every result printing only `propext`, `Classical.choice`, `Quot.sound`; the
release gate; the probe; the census. No manuscript is edited: whether the result earns a manuscript
sentence is an owner decision for a propagation round. Admissible outcome: all green.

## What the outcomes mean, fixed in advance

**If Q3 is positive.** Under the closure with the phases stipulated, the executability of one layer
flow of an involution with a moved configuration is necessary and sufficient for exact finite
endomorphic operational quantum mechanics, with the baseline `DerivedOI` and no substratum
availability beyond it. The frontier of Route A is then the two named assumptions, the phase
intervention and the executability, both explicit; `SubstratumAvail` is not needed for the
endpoint, and Q4′ is superseded by Q4 at the preregistered hypothesis.

**If Q3 is refuted.** Even explicit relative phase together with continuous layer dynamics stays
below quantum mechanics, and the classification sharpens: a third resource, to be named by the
invariant the countertheory preserves, separates `DerivedOI ∧ LayerFlowExecutable` from phase-free
richness.

**What no outcome establishes.** That `PhasesAvailable` is derivable from the stated substratum
(the phase-source pass: it is not). That relative phase or the layer flow is the unique or the
minimal resource. That the observer-level lift is derivable. Route A in either direction. Bare OI.
Anything about a manuscript.

## What the round does not do

Edit a manuscript. Change `DerivedOI`, `LayerFlowExecutable`, `PhaseFreeRichness` or any
definition. Source a relative-phase intervention from the substratum, or claim to. Define the least
class carrying the layer flows. Reopen the phase-source census. Narrate Route B. Refresh the
transfer bundle.

Status: preregistered; the outcome follows in its own section.
