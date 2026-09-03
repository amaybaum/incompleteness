# The primitive-source audit of quantum-complete OI

Quantum-complete OI (OI⁺) is equivalent to exact finite endomorphic operational quantum
mechanics on every nonempty finite carrier (`CarrierGeneralOIPlus.carrier_general_oiPlus`).
Its ingredients are the OI core, well-formedness, and three principles: observational
independence, reversible richness, observer recursion. This document records, ingredient by
ingredient, whether the kernel shows it to be constitutive (part of what it means to observe
and to assign probabilities), derived from something more primitive, or open, and where a
proposed derivation fails, which countermodel fails it. Every "derived" or "not derivable"
entry names the kernel result; every "open" entry names the candidate source and no more.

## The table

| Ingredient | Kernel form | Candidate deeper source | Status at this commit |
|---|---|---|---|
| Composite operational validity | `CompositeOperationalValidity` | Operational semantics: available families map states to states and preserve probability in aggregate | Constitutive, treated as admissibility; no source proposed |
| System-to-level-one seam | `SystemToLevelOne` | Relabelling of the carrier along `A ≃ A × Fin 1` | Derived from embedded observation (`systemToLevelOne_of_embeddedObservation`) |
| Observational independence | `ObservationalIndependence` = inert-spectator compositionality | Locality of the coupling together with intervention modularity | Open; not derivable from the core, well-formedness, reversible richness and observer recursion (`independence_independent`) |
| Reversible richness, inverse clause | first conjunct of `ReversibleRichness` | Reversible dynamics with accessible controls | Open; not derivable from the core, well-formedness, observational independence and observer recursion (`richness_independent`, which refutes the whole conjunction) |
| Reversible richness, Lie-rank clause | second conjunct of `ReversibleRichness` | Symmetry and control architecture | Open; likely independent of the dynamical axioms, and not claimed to follow from them |
| Observer recursion | `ObserverRecursion` | Embedded observation: one regrouping- and relabelling-invariant family of theories on all finite carriers | Derived (`observerRecursion_of_embeddedObservation`); not derivable from the core, well-formedness and the other two principles (`recursion_independent`, `embeddedObservation_independent`) |

## The derived entries in detail

**Embedded observation.** `EmbeddedObservation.lean` defines a family of finite operational
theories on every finite carrier (`TheoryFamily`) with three properties. Regrouping
invariance (`RegroupingInvariant`): the positive-level families of the observer at `S` are
the system families of the observer at `S × Fin m`. Relabelling invariance
(`RelabellingInvariant`): availability is transported along every bijection of carriers.
Ambience (`IsAmbientMember`): the given theory is the family's member at its own carrier, on
the system and at every positive level. `EmbeddedObservation T` is the existence of such a
family. Nothing in it mentions a discard, a closure rule or a shifted theory.

**What the derivation consumes.** From the embedded theories the proof uses only what every
finite operational theory carries by its structure: the identity, the uniform preparation
with its discard rule, and the native readout, whose form is forced
(`readout_is_localLuders`). Iterated ancilla closure is the embedded observer's discard rule
read through the three invariances along `shiftIdx` and its inverse
(`closure_of_embedded`). The identity and the relative readout at every level follow the same
route (`id_of_embedded`, `read_of_embedded`). Observer recursion then follows through the
round-53 construction (`observerRecursion_of_closure`). The level-one seam is relabelling
along `A ≃ A × Fin 1` (`systemToLevelOne_of_embedded`).

**Necessity.** Exact finite operational QM satisfies the principle
(`embeddedObservation_of_qm`): the family is the CP-instrument theory on every carrier
(`cpTheory`, `cpFamily`), for which regrouping invariance is definitional and relabelling
invariance is transport of complete positivity.

**The countercontrol.** The rank-gap theory (`RankGapTheory.gapTheory`) carries the sealed
core, well-formedness, observational independence and reversible richness and has no
iterated ancilla closure, hence no embedded-observation family
(`embeddedObservation_independent`, `core_not_embeddedObservation`). So bare OI does not
supply the principle, and neither do the other principles.

**The compressed set.** With the seam derived, `OIPlusEmbedded` is composite operational
validity, observational independence, reversible richness and embedded observation, and
`carrier_general_oiPlusEmbedded` proves it equivalent to exact finite endomorphic operational
QM on every nonempty finite carrier; `oiPlusEmbedded_iff_oiPlus` identifies it with
carrier-general OI⁺.

## What is not claimed

- The converse from observer recursion to embedded observation is not proved outside the
  OI⁺ context, where both are equivalent to QM.
- The independence of observational independence and of reversible richness from embedded
  observation is not re-established; the round-53 witnesses establish it relative to observer
  recursion.
- No source is proposed for composite operational validity.
- Nothing here bears on the sources of observational independence or of either clause of
  reversible richness. Those are the remaining entries of the table, and for each failed
  implication an explicit countermodel is the required deliverable.
