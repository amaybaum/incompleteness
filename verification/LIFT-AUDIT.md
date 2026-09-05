# The lift audit — do the substratum's own layer flows give the observer an executable continuous mixing family?

`OIBridge/LiftAudit.lean` (the pass), `OIBridge/SecondOrderCircuit.lean`, `SecondOrderLayer.lean`,
`SwapLayer.lean`, `SecondOrderDrive.lean` (CT2: the depth-two factorization, the gate unitaries
`unit g t`, the layer flows, the drive path), `OIBridge/RouteB.lean` and `ManuscriptAxioms.lean`
(the witness and the configuration-level sourcing bound), `OIBridge/MinimalRepertoire.lean`
(`PhaseFreeRichness`, `OIPlusMin`); `CONTINUOUS-TIME-AUDIT.md`, `MANUSCRIPT-AXIOM-AUDIT.md`;
guard `R7-LIFT` in `verification/lean/edge_rigidity_probe.py`.

**Status: pass complete. Q1 positive; Q2 negative for the substratum theory and for every
configuration-level class, executability consistent under control; the preregistered Q3, from
`DerivedOI` and executability, is open, not established by this pass; a strengthened Q3′ is
positive under the substratum's availability and executability; the preregistered Q4 is not
established as stated, and a strengthened Q4′ is proved: relative to the baseline `DerivedOI`
with the substratum's availability, exact quantum mechanics is exactly the executability of one
layer flow.** The preregistration sections were written before any proof was attempted (commit
`0d299c7`); this status line and the outcome section are the only later edits, and the outcome
section records where the proved hypothesis is stronger than the preregistered one. Nothing here is a manuscript claim.

## Why this audit, and what it may not assume

The manuscript-axiom pass proved that any implementation class all of whose operators are
monomial generates a theory inside the Route B witness, which lacks phase-free richness
(`configurationLevel_not_phaseFree`). So the one conjunct of `OIPlusMin` the substratum does not
supply, phase-free richness, requires some non-configuration-level sourcing: some way in which an
embedded observer comes to execute a continuous one-parameter mixing family, not merely a
non-monomial gate. The manuscripts' specifically named candidate is the observer-level lift
`φ → L_obs` (`[SM §4.1]`, recorded there as not proved), and the corpus's one **derived**
continuous object is CT2: the substratum update factors as two layers of commuting local
involutions, each gate `g` is reached at time one by the exact one-parameter unitary group
`unit g t = 1 + (e^{iπt} − 1)·(1 − g)/2` (`SecondOrderCircuit.unit`, `unit_mul_unit`, `unit_one`),
and the layers and their composite act on the quasilocal algebra as continuous paths of
automorphisms (`layerQ`, `swapQ`, `driveQ_isContinuousPath`).

Three things are excluded in advance, and the guard rejects them.

1. **Executability is not inferred from the path.** "There exists a strongly continuous
   automorphism path" is mathematics. `T.availExt n Unit (fun _ => conjChannel U)` is operational
   availability. Time-one executability plus a mathematical interpolation does not give
   intermediate-time executability, and no step below may read the second off the first.
2. **The CT2 flows are candidates, not operations.** The map from a finite-region CT2 unitary into
   an operationally available channel is itself under audit. Nothing in the kernel places
   `unit g t` in any theory's availability, and this audit does not begin by placing it there.
3. **The target is the literal interface.** A positive result must meet `PhaseFreeRichness` as
   written: at every level `n` with at least two states, a pair `a ≠ b` with
   `conjChannel (flow (transition a b) t)` available for every real `t`, `flow` the matrix
   exponential of `ReachabilitySeam`. One executable non-monomial gate is not a result.

Each arrow of

> continuous mathematical path ⇒ executable continuous path ⇒ `PhaseFreeRichness`

is proved or refuted on its own, and no arrow is inferred from its neighbour.

## The objects

Fix a finite region `Λ` of the lattice and the alphabet pair `V × V` of the second-order form,
`V` a nontrivial finite additive group, so that a configuration is `Conf Λ (V × V)`. The theory
in which executability is asked is a `FiniteOperationalTheory` on the carrier
`S := Conf Λ (V × V)`, with levels `S × Fin n`; the identification of the theory's carrier with
the region's configuration space is a modelling choice made here, not derived, and every
statement below is relative to it. The layer involutions on the region are the kernel's own:

- the swap layer, `regionSwap V Λ : S ≃ S`, `(p, c) ↦ (c, p)` at every site
  (`regionSwap_involutive`), which moves every configuration with `p ≠ c` at some site;
- the shear layer, `shearPerm R S A` for a rule `R` (`shearOnRegion_involutive`).

For an involution `g` of `S` the finite-region gate unitary at time `t` is `unit (permMat g) t`,
and at level `n` the layer acts on `S × Fin n` as `g × id`, the ancilla a spectator, so the
candidate at level `n` is `unit (permMat (g × id)) t`. The swap layer is attacked first; the shear
layer follows only if the swap layer settles a question in a way that leaves it open.

## The three questions, in order, each with its own outcomes

**Q1. Finite-region realization.** Does the layer flow give a well-defined family of finite-region
channel candidates with the exact group and continuity properties? Concretely, for an involution
`g` of `S` and every `n` and `t`: `unit (permMat (g × id)) t` is a unitary matrix; the family is a
one-parameter group in `t` with value `1` at `t = 0` and `permMat (g × id)` at `t = 1`; its
conjugation `conjChannel (unit (permMat (g × id)) t)` is trace-preserving, so it has the shape of
a one-outcome channel; and the finite-region unitary is the region's stage image of the
quasilocal gate unitary of CT2. Admissible outcomes: the theorems (`gateFlow_unitary`,
`gateFlow_group`, `gateFlow_zero`, `gateFlow_one`, `gateFlow_trace`, `gateFlow_stage`), or a
kernel theorem that one of them fails. Most of Q1 is assembly of `SecondOrderCircuit`; it is kept
as a question so that Q2 and Q3 have a fixed object to refer to, and so that "candidate" is a
proved property and not a word.

**Q2. Derived executability.** Can availability of every intermediate time be proved from the
existing substratum and observer architecture, with no new availability axiom? The existing
architecture is the theory the substratum's interventions generate, `substratumTheory S`
(monomial generation, `StructuralClosure.substratumClass`), and the statement is the predicate

> `LayerFlowExecutable T g := ∀ n t, T.availExt n Unit (fun _ => conjChannel (unit (permMat (g × id_n)) t))`.

Admissible outcomes, for the swap layer `g = regionSwap V Λ` on a nonempty region with
nontrivial `V`: a kernel theorem `substratumTheory_layerFlowExecutable` proving the predicate
for `substratumTheory S`, or a kernel theorem `substratumTheory_not_layerFlowExecutable` proving
its negation. A derivation counts only if it is a proof of availability in `substratumTheory S`
as defined; adding an availability axiom, enlarging the class, or reading availability off the
CT2 path is not a derivation. Consistency is recorded alongside whichever outcome holds:
`layerFlowExecutable_of_control`, the predicate holds in every theory with composite unitary
control, so it is satisfiable and is not contradicted by quantum mechanics.

**Q3. Richness bridge.** If the layer flow is executable, does it supply the continuous
transition flows at every level that `PhaseFreeRichness` requires? The hypothesis is
`LayerFlowExecutable T g`, taken as a hypothesis whether Q2 derived it or not, together with what
the substratum already supplies through `DerivedOI T` (the exchanges, the phases, the closure).
The conjecture, fixed here with its mechanism so that the proof cannot drift: on a moved pair
`{x, g x}` the gate unitary is `e^{iπt/2}` times the transition flow `flow (transition x (g x)) (πt/2)`,
on every other moved pair the same, and on fixed points the identity; conjugating the gate flow
by a diagonal sign that flips one element of every moved pair except the chosen one reverses the
rotation on those pairs, so the product of the gate flow with its sign-conjugate is the transition
flow at angle `πt` on the chosen pair, a scalar phase on the other moved configurations and the
identity on the fixed points; a diagonal unitary, monomial hence available, removes the phase.
Since `πt` ranges over the reals, every value of the transition flow on the pair `(x, k), (g x, k)`
at level `n` is available. Admissible outcomes: `phaseFree_of_layerFlowExecutable` (from
`DerivedOI T`, an involution with a moved point, and the hypothesis), or a kernel theorem that
the hypothesis together with `DerivedOI` does not give phase-free richness
(`layerFlowExecutable_not_phaseFree_countermodel`). The technical core, preregistered as the
risk, is the identification of the isolated rotation with `flow (transition a b) s`, the matrix
exponential; the kernel has no closed form for that exponential, and one has to be proved
(`flow_transition_closedForm`), through the idempotent decomposition of the transition generator
and `NormedSpace.exp_add_of_commute`, or through the uniqueness of the solution of the defining
linear equation. If the closed form cannot be established, Q3 is reported open at that step, not
closed either way.

**Q4, conditional, only if Q3 closes positively.** The endpoint theorem: under `DerivedOI T` on
the region carrier, `ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T g`
(`derivedOI_qm_iff_layerFlowExecutable`), from `derivedOI_qm_iff_phaseFree` one way and
`layerFlowExecutable_of_control` the other. This names the extra principle exactly, if Q2 is
negative: the executability of the substratum's own layer flows at intermediate times.

## What the outcomes mean, fixed in advance

- Q1, Q2, Q3 all positive: Route A reaches `PhaseFreeRichness` from the substratum's existing
  availability, and under `DerivedOI` quantum mechanics follows by `derivedOI_qm_iff_phaseFree`.
- Q1 positive, Q2 negative, Q3 positive: the exact extra sourcing principle is isolated as
  `LayerFlowExecutable`, and Q4 gives the conditional equivalence; the manuscripts' statement
  that the continuous interpolation is chosen rather than derived is confirmed at the operational
  level, with the choice named.
- Q1 positive, Q2 positive, Q3 negative: CT2 is executable but the wrong continuous resource, and
  Route A must seek another non-configuration-level sourcing.
- Q1 negative: the candidate is not well formed, and the audit stops there.

None of these is a manuscript claim. The manuscripts already state that a continuous
one-parameter interpolation of the finite permutation is additional structure; the audit tests
whether that structure, read as the substratum's own layer flows, is what an embedded observer
lacks, and whether granting it is exactly what quantum mechanics needs.

## What the audit does not do

Construct the observer-level lift `φ → L_obs` of `[SM §4.1]`; the CT2 layer flows are tested as
the first candidate for a derived non-configuration-level sourcing, and a negative Q2 does not
say the lift cannot be derived by another route. Identify the theory's carrier with the manuscript
substratum by anything other than the stated modelling choice. Assert anything about A1–A6.
Narrate anything in a manuscript. Refresh the transfer bundle.

## The outcome

Preregistration commit `0d299c7`. Every question closed in the preregistered order under its
preregistered name; the object is a single layer involution on a region, never the composite
drive; no availability was read off the CT2 path; no non-monomial gate was counted as a result.

| question | outcome | kernel |
|---|---|---|
| Q1, finite-region realization | **positive** | `gateFlow_unitary`, `gateFlow_group`, `gateFlow_zero`, `gateFlow_one`, `gateFlow_trace`, `gateFlow_stage` |
| Q2, derived executability | **negative** for `substratumTheory S`, and for the theory of every configuration-level class: at `t = 1/2` the gate flow of an involution with a moved configuration does not preserve the diagonal (`gateFlow_half_not_preservesDiag`), so it is realized by no monomial family (`configurationLevel_not_layerFlowExecutable`, `substratumTheory_not_layerFlowExecutable`); consistent: it holds in every theory with composite unitary control (`layerFlowExecutable_of_control`) | as named |
| Q3, richness bridge, as preregistered (`DerivedOI T` and `LayerFlowExecutable T σ` give `PhaseFreeRichness T`) | **open**: not established by this pass, neither the theorem nor a countermodel at that hypothesis | none |
| Q3′, the strengthened bridge (`SubstratumAvail T` and `LayerFlowExecutable T σ`, for an involution with a moved configuration) | **positive**: `PhaseFreeRichness T` as literally stated (`phaseFree_of_layerFlowExecutable`) | with `exp_smul_idempotent`, `flow_transition_closedForm`, the orbit calculus (`orb_mul`, `gateFlow_eq_orb`, `flow_transition_eq_orb`, `diagonal_mul_orb_mul_diagonal`), `signFun_mul`, `gateFlow_isolation` |
| Q4, the endpoint, as preregistered (under `DerivedOI T` alone) | **not established as stated** | none |
| Q4′, the strengthened endpoint | under `DerivedOI T ∧ SubstratumAvail T`, `ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ` (`derivedOI_qm_iff_layerFlowExecutable`) | |
| the swap layer | `regionSwap_moves`; `substratumTheory_not_layerFlowExecutable_swap`, `phaseFree_of_layerFlowExecutable_swap`, `derivedOI_qm_iff_layerFlowExecutable_swap` on `Conf Λ (V × V)`, `Λ` nonempty, `V` nontrivial | |

**Where the proved hypothesis is stronger than the preregistered one.** Q3 was preregistered
with the hypothesis `DerivedOI T`. The mechanism needs two diagonal unitaries at every level, the
sign of the non-chosen orbits (entries `±1`) and the phase `e^{−iπt}` on the moved
configurations; the substratum's phase structure supplies every diagonal unitary
(`monomial_diagonal`, `substratumTheory_avail_conj`), but `DerivedOI`'s quarter phases generate
only fourth roots of unity. The hypothesis proved is therefore `SubstratumAvail T`, that `T`
carries the substratum theory's availability (`substratumTheory_substratumAvail`), and the
theorems are Q3′ and Q4′, not Q3 and Q4. The preregistered Q3 is left **open** at its
hypothesis: this pass proves neither `PhaseFreeRichness` from `DerivedOI` and executability nor a
countermodel to it, and closing it either way would be a new result. The pass does not show that
`SubstratumAvail` follows from `DerivedOI`, nor that it is the minimal extra baseline: the proof
visibly uses arbitrary diagonal-unitary availability, which is stronger than the quarter phases
`DerivedOI` abstracts. Q3′ uses no embedded observation and no dagger stability; Q4′ adds
`DerivedOI T` for `derivedOI_qm_iff_phaseFree`. The mechanism itself is the preregistered one:
on a moved pair the gate flow is `e^{iπt/2}` times the transition flow at `πt/2`; conjugation by
the sign reverses the rotation on every non-chosen orbit; the product of the gate flow with its
sign-conjugate is the transition flow at `πt` on the chosen pair, the scalar `e^{iπt}` on the other
moved configurations and the identity on the fixed ones; the phase diagonal removes the scalar
(`gateFlow_isolation`). The preregistered technical risk, the closed form of the matrix
exponential, closed through the two orthogonal idempotents `(Π ± X)/2` and `NormedSpace.exp` of
a scaled idempotent.

**What the outcome establishes.** Q1 positive; Q2 negative for configuration-level generation,
with consistency under control; Q3 open at the preregistered hypothesis and Q3′ positive; Q4′
proved. None of the three preregistered total outcomes is reached as stated, because the
preregistered Q3 is neither closed positively nor refuted; what is reached is the strengthened
form of the second: `LayerFlowExecutable`, the executability at intermediate times of one layer
of the substratum's own update on the region carrier with the ancilla a spectator, is not derived
from configuration-level generation, is consistent with quantum mechanics, and is necessary and
sufficient for exact finite operational quantum mechanics **relative to the baseline
`DerivedOI ∧ SubstratumAvail`**. Relative to that baseline it is the extra sourcing principle;
whether a smaller baseline would do, in particular whether `DerivedOI` alone suffices for Q3, is
open. The manuscripts' statement that a continuous interpolation of the finite permutation is
additional structure is confirmed at the operational level relative to that baseline, with the
structure named as an availability principle rather than as a choice of generator, and the
frontier of Route A is one arrow:

> substratum and observer architecture ⟶ `LayerFlowExecutable` (derived, not stipulated),
> relative to the baseline `DerivedOI ∧ SubstratumAvail`

**What the outcome does not establish.** The preregistered Q3: `PhaseFreeRichness` from
`DerivedOI` and executability, open. That `SubstratumAvail` follows from `DerivedOI`, or that
the baseline `DerivedOI ∧ SubstratumAvail` is minimal. That the lift `φ → L_obs` is derivable,
or that it is not: Q2 says the present architecture, configuration-level generation, does not
make the layer flow executable, and says nothing about a different reading of the observer
architecture. That `LayerFlowExecutable` is the only principle that would do: relative to the
baseline it is necessary and sufficient for quantum mechanics, and a different principle could be
sufficient as well. That the identification of the theory's carrier with a region's
configuration space is anything but the stated modelling choice. That anything here reaches a
manuscript.

**Fifty-six named results**, each printing only `propext`, `Classical.choice`, `Quot.sound`.

## What this note does not claim

That executability of the layer flow is derived from the substratum: it is the extra principle
relative to the baseline, and Q2 shows the substratum's configuration-level generation does not
supply it. That the preregistered Q3 or Q4 holds as stated; the theorems are Q3′ and Q4′ under
the stronger baseline. That `SubstratumAvail` follows from `DerivedOI`, or that the baseline is
minimal. That the observer-level lift is derivable, or that it is not. That Route A is closed in either
direction. That the drive is derived from bare OI, or that quantum mechanics rests on
observation incompleteness. That the carrier identification is derived. That anything here is a
manuscript claim.
