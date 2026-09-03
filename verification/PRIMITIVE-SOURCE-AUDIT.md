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
| Composite operational validity | `CompositeOperationalValidity` | Operational semantics: available families map states to states and preserve probability in aggregate | Positivity derived from implementation locality (`validity_of_implementationLocality`); the normalization half is the trace clause of implementation generation, stated there rather than derived |
| System-to-level-one seam | `SystemToLevelOne` | Relabelling of the carrier along `A ≃ A × Fin 1` | Derived from embedded observation (`systemToLevelOne_of_embeddedObservation`) |
| Observational independence | `ObservationalIndependence` = inert-spectator compositionality | Implementation locality: a context-stable, label-invariant class of admissible operators generating availability | Derived (`observationalIndependence_of_implementationLocality`); not derivable from the core, validity, reversible richness and embedded observation (`redundancy_fails`) |
| Reversible richness, inverse clause | `InverseAccessibility` (first conjunct of `ReversibleRichness`, `reversibleRichness_iff`) | Dagger-stable implementations: the adjoint of an admissible operator is admissible | Derived (`inverseAccessibility_of_generated_daggerStable`); whether it is already forced by implementation locality, embedded observation and Lie-rank richness is open in both directions |
| Reversible richness, Lie-rank clause | `LieRankRichness` (second conjunct of `ReversibleRichness`) | Elementary transition richness: driven state transitions, exchanges, one quarter phase | Derived (`lieRank_of_elementary`); not forced by reversible implementation locality and embedded observation (`lieRank_not_redundant`) |
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

## The second entry: observational independence

**The redundancy test.** Round fifty-six strengthened observer recursion to embedded
observation, so the first question is whether validity, reversible richness and embedded
observation already force observational independence. They do not (`redundancy_fails`).
The round-34 countermodel (`countermodel`: Kraus families on the qubit, 2-positive
trace-preserving instruments on every composite) carries the OI core, validity and
reversible richness, and it carries embedded observation: the 2-positive-instrument theory
on every finite carrier (`twoPosTheory`, `twoPosFamily`) is a regrouping- and
relabelling-invariant family whose qubit member is the countermodel, definitionally on the
composites and by `twoPositive_qubit_cp` on the system. It has no observational
independence. The four-part package does not compress to three.

**Form without existence.** Round thirty-seven's `isSpectatorExtension_iff` fixes the form
of any spectator extension as `withSpectator`. `form_fixed_existence_fails` records that for
the countermodel's available two-qubit reduction map the qutrit extension is so fixed and
not available. The missing physics is existence.

**The primitive, below availability.** An implementation class (`ImplementationClass`)
assigns to every finite carrier the admissible single operators; an operation is realized
by the class when it is a finite sum of conjugations by admissible operators (`Realized`).
Implementation generation (`ImplementationGenerated`): at every positive level a family is
available exactly when each branch is realized and the aggregate trace is preserved.
Context stability (`ContextStable`): `𝓘 S K → 𝓘 (R × S) (1_R ⊗ K)`. Label invariance
(`LabelInvariant`): admissibility is transported along carrier bijections. Neither
stability nor invariance mentions availability or the spectator extension; the lint checks
the statements for that vocabulary.

**The derivation.** The extension of a conjugation is the conjugation by the reindexed
`1 ⊗ K` (`withSpectator_conjChannel`, the local form), so realization is preserved
(`realized_withSpectator`) and the aggregate trace is preserved; hence
`observationalIndependence_of_implementationLocality`. Realized operations are completely
positive, so validity is derived too (`validity_of_implementationLocality`).

**Necessity and diagnosis.** Exact finite operational QM is generated by the full class
(`implementationLocality_of_qm`). The countermodel is generated by no class at all, because
its reduction map is not completely positive (`countermodel_not_implementationGenerated`):
its failure is implementability, not context stability.

**The compressed set.** `OIPlusLocal` is implementation locality, reversible richness and
embedded observation, and `carrier_general_oiPlusLocal` proves it equivalent to exact
finite endomorphic operational QM on every nonempty finite carrier.

## The third entry: the inverse clause of reversible richness

**The split.** `InverseAccessibility` says every available conjugation channel has its
adjoint channel available; `LieRankRichness` is the drift/control certificate at every
level; `reversibleRichness_iff` records that reversible richness is their conjunction. The
kernel consumes the inverse clause at exactly one place, the adjoint-closure hypothesis of
the round-50 reachability theorem (`control_of_lieRank_inverse`).

**The redundancy test, honestly.** Whether implementation locality, embedded observation
and Lie-rank richness already force inverse accessibility is not settled in either
direction. Without the clause the available unitaries at a level form a semigroup
containing the flows in both time directions and the controls; a subsemigroup of a compact
group with nonempty interior is a group, and the flows plausibly give that interior, so the
clause may be redundant. Neither that proof, which needs closure groups and interior of
reachable sets, nor a countermodel is built.

**The primitive, below availability.** A dagger-stable class (`DaggerStable`):
`𝓘 S K → 𝓘 S Kᴴ`. Reversible implementation locality is implementation locality with a
dagger-stable class.

**The derivation.** An available conjugation channel `conj V` is realized by admissible
operators and trace preserving, so `V` is an isometry. The Choi matrix of `conj V` is the
dyad of the vectorized `V`, so the dyads of the realizing operators sum to a rank-one dyad
and each lies on the ray of `V` (`dyad_sum_span_single`, `kraus_of_conj_unitary`); the
squared moduli sum to one; the adjoint family realizes `conj Vᴴ`, which is trace preserving
and hence available (`inverseAccessibility_of_generated_daggerStable`).

**Necessity and the compressed set.** Exact QM is generated by the full class, which is
dagger-stable. `OIPlusMicro` is reversible implementation locality, Lie-rank richness and
embedded observation, and `carrier_general_oiPlusMicro` proves it equivalent to exact
finite endomorphic operational QM on every nonempty finite carrier. The Lie-rank clause is
the one substantive selector whose source is not audited.

## The fourth entry: the Lie-rank clause of reversible richness

**The redundancy test.** An implementation class closed under the operations a theory
performs on implementations — identity, product, scalar, ancilla projector, ancilla block
(`Architecture`) — generates a finite operational theory on every carrier (`genTheory`), and
a context-stable, label-invariant, dagger-stable such class gives a theory carrying
reversible implementation locality and embedded observation
(`genTheory_reversibleImplementationLocality`, `genTheory_embeddedObservation`). The diagonal
class is such an architecture; its generated theory on the qubit has no composite unitary
control (`diagGen_not_control`), so the Lie-rank clause is not forced by the other two
principles (`lieRank_not_redundant`).

**The primitive, in elementary implementations.** `ElementaryTransitionRichness`: at every
level, every real transition `E_ab + E_ba` is continuously drivable, every exchange is
available, and a quarter phase on every state is available. Nothing in it mentions a Lie
algebra or reachability.

**The derivation.** With drift `X_{i₀j₁}` and controls the words (a permutation, optionally
the quarter phase on `i₀`), conjugation relabels the transition (`perm_conj_transition`) and
the phase turns it into its imaginary partner (`phase_conj_transition`); a permutation
reaches every ordered pair (`exists_perm_pair`); the bracket
`[−iX_pq, −iY_pq] = 2i(E_pp − E_qq)` supplies the diagonal directions (`bracket_XY`); every
traceless skew-Hermitian is a real combination (`pair_decomp`), so `su(D)` lies in the
control Lie algebra (`hControl_star`) and Lie-rank richness follows
(`lieRank_of_elementary`), the control words all available (`avail_ctrl`).

**Necessity and the compressed set.** Full control supplies every elementary transition
(`elementary_of_control`). `OIPlusElem` is reversible implementation locality, elementary
transition richness and embedded observation, and `carrier_general_oiPlusElem` proves it
equivalent to exact finite endomorphic operational QM on every nonempty finite carrier.
Every principle in it is now stated at the level of implementations or the observer
architecture.

## What is not claimed

- The converse from observer recursion to embedded observation is not proved outside the
  OI⁺ context, where both are equivalent to QM.
- The independence of observational independence and of reversible richness from embedded
  observation is not re-established; the round-53 witnesses establish it relative to observer
  recursion.
- Whether context stability is redundant given implementation generation is not settled:
  no theory generated by a class that is not closed under `1 ⊗ ·` and failing observational
  independence is built.
- The converse from observational independence to implementation locality is not claimed
  outside the OI⁺ context.
- The normalization half of validity is not derived; it is the trace clause of
  implementation generation.
- The redundancy of inverse accessibility given implementation locality, embedded observation
  and Lie-rank richness is open in both directions.
- The converse from inverse accessibility to dagger stability is not claimed.
- The minimal elementary repertoire is not settled: whether the quarter phase is dispensable
  on three or more states, or one driven pair and one exchange orbit suffice.
- The converse from Lie-rank richness to elementary transition richness is not claimed.
