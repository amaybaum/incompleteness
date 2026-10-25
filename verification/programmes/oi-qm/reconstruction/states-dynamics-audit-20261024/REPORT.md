# States and dynamics: exactness and sourcing audit

Research draft, 24 October 2026. Consistency axis only. No premise adoption,
manuscript status change, native-round designation, or equivalence claim.

## Result of the first source audit

The native-Y construction does not remove the existing A1 cardinality
obstruction. It produces one more finite native apparatus for one calibrated
menu. Under the same countable realization map and finite-protocol notion of
availability, adding such apparatuses still leaves only countably many
available conjugation rays. This is a conditional implication, not a no-go
theorem for observational incompleteness or for every classical model.

The maintained A1 theorem has a stronger premise than the shorthand
"countably many unitary gates": `countable_not_pairFlowSourced` assumes a
countable set D of matrices such that **every** available level-one single-
outcome conjugation `conjChannel V` has V proportional to an element of D.
Its `hmem` quantifier includes nonunitary V. A proposed realization argument
must establish that premise, not just count its displayed unitary examples.

This audit reads the source declarations on main; it does not rerun Lean or
claim a new kernel theorem. The programme's earlier written argument and
its review already identify this correction. The useful application here is
to classify the current native-Y work and the next reset by the same premise.

## Assumption boundary

| Premise or conclusion | Status in this audit | Consequence |
| --- | --- | --- |
| Every protocol has a finite description over a countable primitive/context set | Explicit hypothesis of the countability application | Descriptions form a countable set, even with no common length bound |
| Every available conjugation is determined by one such implementation/context | Required sourcing hypothesis | The image has countably many rays; representation choices cannot silently add operations |
| Countable-ray hypothesis implies no sourced pair flow | Existing Lean theorem inspected on main | Exact operational QM is excluded through the kernel's necessary pair-flow direction |
| Arbitrary real priors, arbitrary real observer dials, infinite descriptions, or closure points are automatically countable | Not asserted | Each requires its own sourcing and availability analysis |
| Finite native Y readout and any finite native reset preserve the two preceding hypotheses | Conditional written argument | They can advance a bounded instrument construction without supplying an A1 continuum |
| Countability excludes arbitrary-precision approximation | False | The existing fixed-gate theory is a direct countercontrol |
| A source for all states, preparations, phases and operations is established by clean Y | Not established | These remain separate proof obligations |

The fixed-gate countercontrol on main has dense unitary control at an angle
whose ratio to pi is irrational, while `fixedGateTheory_not_qm` excludes
exact QM for every fixed angle. It is a theory-level witness that countability
alone does not refute A2. Its non-native gate resource is supplied; it is not
a native OI construction.

## Four different endpoints

1. **A bounded calibrated menu:** exact equality for named preparations and
   finite protocols. This is the present native-instrument target.
2. **A2 approximation:** for each target and positive error, an actually
   available finite implementation approximates it. A complete claim needs
   a stated metric, uniformity domain, resource dependence, and composition
   control. The kernel's `DenseFiniteQM` is `KrausSoundExt` together with
   outcome-wise `KrausDense`; gate density alone is not its full definition.
3. **Almost-sure termination:** a distribution over finite run lengths with
   probability-one eventual termination. This is not a finite worst-case
   protocol and is not automatically admitted by present availability.
4. **A1 exact availability:** each target instrument itself belongs to the
   available theory. A convergent sequence does not establish this membership
   without an additional rule; a closure rule changes the target theory.

The distinction is standard in quantum compilation: Dawson and Nielsen's
Solovay-Kitaev review concerns approximation by finite gate sequences. Hardy's
reconstruction instead includes continuous reversible transformations as an
axiom. Neither supplies those transformations from the native lattice.

## Candidate correspondence: obligations rather than an assumed map

| Object | Required correspondence | Present boundary |
| --- | --- | --- |
| Preparation | An initial native preparation induces a specified operational state; mixtures and the whole allowed preparation set are accounted for | Twelve-state/eight-preparation calibration is supplied in #885; full quantum state set not derived here |
| State | Identify preparations indistinguishable under every permitted continuation, then give a sound and sufficiently rich map to density operators | Equality on a finite menu need not survive enlarged access; no global map supplied |
| Operation | Native evolution and controls induce the claimed operation on those equivalence classes | Local truth tables do not prove a well-defined operation on every class |
| Instrument | Each outcome map gives both its probability and the updated state, including failure outcomes | #910's clean readout does not yet supply its Y reset |
| Composition | The correspondence respects sequential/parallel composition and adaptive controls | Owned by the composition track; essential to upgrading local witnesses |
| Full equivalence | Both soundness (no extra operational laws) and completeness (every target law available) | Neither follows from calibrated examples or from necessary conditions alone |

## Exact finite-resource diagnostic

The written derivation and pre-computation rule are in `PROBE-SPEC.md`.
With finitely many fair bits and deterministic dynamics, unconditional events
are dyadic and nonzero herald-conditioned events are rational. Here the
uniform bank must contain **all** randomness used, conditional on the fixed
input and earlier history. The bound is not on only the newly introduced bits
when a correlated reservoir also participates.

For post-Y weights 5:3:2 with independent fair z, the six successful cell
probabilities are (5,5,3,3,2,2)/20. A uniform deterministic sampler therefore
needs a positive success atom count divisible by 20. Always-success sampling
from a finite fair-bit bank is excluded. At the illustrative success rate
5/16, six fair bits suffice and fewer do not: assign the six counts
5,5,3,3,2,2 among 64 seed atoms and declare the other 44 failures. This rate
is a resource benchmark, not a claim about the actual downstream reset.

Keeping the seed and XORing its label into a blank three-bit register extends
this abstract sampler to an involution on 512 states. Both y values produce
the prescribed decoded carrier law. The three blank bits are additional
readiness resources. This exhibits an abstract reversible sampler, not a
native lattice implementation, and does not source either its seed bank or
its decoder.

For the irrational target p=(2+sqrt(2))/4, an event n/M on M successful
uniform atoms has error strictly greater than 1/(8M^2), by its nonzero integer
polynomial residual and factorization through 8p^2-8p+1=0. This produces a
finite-budget separation, but not an A2 error floor: dyadic brackets of width
2^-b contain p for arbitrarily large b. A two-state identity model with p
already placed in its prior is an exact countercontrol, demonstrating why
finite state count alone does not establish the rational-probability premise.

The checker verifies integer feasibility for bit counts 0 through 16, the
entire 512-state involution, both carrier laws, 2,144 exact rational comparisons
for the error bound, and 16 dyadic brackets. It rejects a wrong 5:2:3 law and
a fixed-z law whose (a,b) marginal is nevertheless correct. The general
counting/error statements rest on the written proof, not on those bounded
enumerations. No claim of full instrument approximation follows from a
Bernoulli approximation example.

Replay with Python 3's standard library:

```sh
python3 checks.py
python3 -O checks.py
```

Both outputs are byte-identical to `result.json`, whose structured verdict is
`PASS`. `checks.py --output path.json` writes the same data directly. Any
failed condition raises an exception and exits nonzero before a pass result
is written. `SHA256SUMS` covers the four deliverable source/result files.

## Consequence for the parallel programme

The next native-reset attempt should account for its complete conditional
random bank and implement its acceptance law, rather than require an
always-success deterministic sampler that this resource class cannot supply.
The composition track must verify that earlier records do not spoil the
uniform conditional bank. These are necessary checks on a candidate; the
abstract sampler does not demonstrate that a native candidate exists.

On the broader state/dynamics track, the outstanding step remains sourcing
an operation/state correspondence that actually changes a load-bearing A1
premise, or establishing a stated A2 endpoint under permitted resources.
Neither the six-bit benchmark nor the native clean-Y readout does that.

## Sources and scope of reading

- Main snapshot `de6fe29324ade8a0826c18f7829786086dd590da`:
  `verification/lean-mathlib/OIBridge/PairFlowEquivalence.lean`,
  `countable_not_pairFlowSourced`, `derivedOI_pairFlowSourced_of_qm`;
  `SubstratumInterfaceAudit.lean`, `sourcedOI_of_qm`,
  `sourcedOI_qm_iff_phaseFree`; `DiscreteCompletion.lean`,
  `DenseFiniteQM`, `KrausDense`, `fixedGateTheory_denseUnitaryControl`,
  `fixedGateTheory_not_qm`.
- Programme snapshot `2d555f17c23bea31d32b3f5eb4c49d245b413a76`, prefix
  `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`:
  `INTEGRATION.md`, `PLAN.md`, `oa-node1/NODE.md` (final review controls the
  interpretation), and `mc-node5/NODE.md`. These are off-main WIP provenance;
  their evidence must land no later than a dependent enduring claim.
- Native-Y checkpoint `5f6786d6f02605f8e8821a536b678495e19015da`,
  `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/CURRENT-HANDOFF.md`.
- C. M. Dawson and M. A. Nielsen, *The Solovay-Kitaev algorithm*,
  <https://arxiv.org/abs/quant-ph/0505030> (primary-source abstract checked).
- L. Hardy, *Quantum Theory From Five Reasonable Axioms*,
  <https://arxiv.org/abs/quant-ph/0101012> (primary-source abstract checked).

No new absence claim about the full manuscript corpus is made. Historical
reports are interpreted through their applied review corrections. The
classification above confirms and applies the existing obstruction; it does
not claim novelty for the counting argument or for the density distinction.
