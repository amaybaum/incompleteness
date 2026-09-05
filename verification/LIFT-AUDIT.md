# The lift audit — do the substratum's own layer flows give the observer an executable continuous mixing family?

`OIBridge/LiftAudit.lean` (the pass), `OIBridge/SecondOrderCircuit.lean`, `SecondOrderLayer.lean`,
`SwapLayer.lean`, `SecondOrderDrive.lean` (CT2: the depth-two factorization, the gate unitaries
`unit g t`, the layer flows, the drive path), `OIBridge/RouteB.lean` and `ManuscriptAxioms.lean`
(the witness and the configuration-level sourcing bound), `OIBridge/MinimalRepertoire.lean`
(`PhaseFreeRichness`, `OIPlusMin`); `CONTINUOUS-TIME-AUDIT.md`, `MANUSCRIPT-AXIOM-AUDIT.md`;
guard `R7-LIFT` in `verification/lean/edge_rigidity_probe.py`.

**Status: preregistered; no question tested yet.** This section is written before any proof is
attempted (the preregistration commit is named in the outcome section) and is edited afterwards
only to append the outcome section and to record, marked as such, any scope repair made at
review. Nothing here is a manuscript claim.

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
