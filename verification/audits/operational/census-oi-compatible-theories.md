# The census of OI-compatible operational theories

Round fifty-two. The operational-completion characterization (`GeneralCarrier.main_result`,
`papers/GR.md` §3.3) says that a well-formed finite operational theory is exactly finite
operational quantum mechanics if and only if it satisfies three substantive selection
principles:

- **I** — inert spectators (`InertSpectatorCompositionality`): every available composite
  operation extends to an available operation on a larger composite that acts as the identity
  on an untouched spectator;
- **C** — sufficient reversible control (`HasCompositeUnitaryControl`): every unitary
  conjugation on every finite ancilla extension is available;
- **K** — iterated composition (`IteratedAncillaClosure`): attaching a uniform ancilla, running
  an available operation on the enlarged composite, and forgetting the ancilla yields an
  available operation on the smaller composite.

Well-formedness (valid probabilities and trivial-ancilla consistency) is assumed throughout;
so is realization of the sealed OI core. This document records, for each of the eight patterns
of holding and failing, whether the class is nonempty, which theory realizes it, its exact
allowed operations, its closure under composition, the observable deviation from quantum
mechanics it permits, and which candidate principle would rule it out. Every line carries its
kernel status: **proved** (a named result in `OIBridge/SubstantiveCensus.lean` or an earlier
module), **read off the definition** (a fact about the witness visible from its construction,
not separately stated as a theorem), or **not formalized** (physical interpretation).

## The lattice

    proved (substantive_census): all eight cells are nonempty.
    proved (no_boolean_relation): no Boolean relation among I, C, K holds on the class.
    proved (qm_is_the_top_cell): the no-failure cell is exactly finite operational QM.

```
                              ┌─────────────────────────────┐
                              │  ∅  · finite operational QM │
                              │  every normalized Kraus     │
                              │  instrument, every level    │
                              └──────────┬──────────────────┘
                 ┌───────────────────────┼───────────────────────┐
     ┌───────────┴───────────┐ ┌─────────┴───────────┐ ┌─────────┴───────────┐
     │ {I} countermodel      │ │ {C} diagTheory      │ │ {K} gapTheory       │
     │ 2-positive composites │ │ diagonal-preserving │ │ rank-gap composites │
     └───────────┬───────────┘ └─────────┬───────────┘ └─────────┬───────────┘
        ┌────────┴──────────┬────────────┴───────────┬───────────┴────────┐
 ┌──────┴──────────────┐ ┌──┴──────────────────┐ ┌───┴─────────────────┐  │
 │ {I,C}               │ │ {I,K}               │ │ {C,K}               │  │
 │ diagTwoPosTheory    │ │ cappedTheory        │ │ diagGapTheory       │  │
 └──────┬──────────────┘ └──┬──────────────────┘ └───┬─────────────────┘  │
        └──────────────────┬┴────────────────────────┘                    │
                ┌──────────┴──────────────┐                               │
                │ {I,C,K} cappedDiagTheory│◄──────────────────────────────┘
                └─────────────────────────┘
```

Each edge is inclusion of failure sets, not inclusion of theories: the witnesses were chosen
for the shortest proofs, and the census claims existence in each cell, nothing about
representatives. QM is the unique cell in which nothing fails.

## The construction behind the four new cells

Proved. `classTheory C` cuts a `FiniteOperationalTheory` out of a per-level class `C.P` of
composite maps that are 2-positive and closed under composition, finite sums and the Lüders
readout, together with a system class and a preparation class. Each of the five conditions
reduces to one closure property of the class (`classTheory_validity`,
`classTheory_systemToLevelOne`, `classTheory_realizes`, `classTheory_inert`,
`classTheory_control`, `classTheory_closure`), and each failure reduces to one witness outside
the class (`classTheory_not_inert`, `classTheory_not_control`, `classTheory_not_closure`).

The one new device is the **level cap**. A class that is strictly smaller at low levels than
at high levels breaks iterated composition without touching control: a high-level map's
ancilla discard lands outside the low-level class. A class admitting 2-positive maps that are
not completely positive above the cap breaks inert spectators there. The two analytic inputs
are the normalized reduction map `redMap = (2·tr(X)·I − X)/(2d − 1)` on a `d`-level carrier —
trace preserving and 2-positive for every `d` (`redMap_trace`, `redMap_twoPositive`), not
3-positive on any carrier with three levels (`amplRef_redMap_ent3_not_posSemidef`, witness value
`−3/(2d − 1)`), whose uniform-ancilla discard from level six to level three is
`(4·tr(X)·I − X)/23` (`discard_redMap`), not completely positive (`traceShift_not_cp`, Choi form
`a·d − d²`) — and the round-44 gap channel tensored with an untouched ancilla
(`spectatorLast`), which is completely positive and diagonal-preserving at level six and
discards to itself (`discardWith_uniform_spectatorLast`), a map that is not gap-admissible at
level three (`gapChannel_not_gap`).

## The eight cells

### ∅ — finite operational quantum mechanics

- **Nonempty:** proved (`cell_none`, from `main_result`).
- **Realized by:** the exact theory of the completion classification.
- **Allowed operations:** on the system and on every ancilla level, exactly the normalized
  finite Kraus instruments (proved: `exactAll_iff_physical_general`).
- **Closure:** sequential composition, coarse-graining, spectator extension and ancilla
  discard all hold (proved, as the five conditions).
- **Deviation from QM:** none.
- **Ruled out by:** nothing; this is the reference cell.

### {I} — inert spectators fail

- **Nonempty:** proved (`cell_I`).
- **Realized by:** the round-34 dimensional countermodel (`countermodel`).
- **Allowed operations:** on the system, exactly the Kraus instruments (proved:
  `countermodel_exact`); on every composite, the 2-positive trace-preserving instruments (read
  off the definition). The two-qubit reduction map `(2·tr(X)·I − X)/7` is available and has no
  Kraus form (proved: `countermodel_reduction2_available`, `reduction2_not_cp`).
- **Closure:** sequential composition and ancilla discard hold (proved:
  `countermodel_iteratedAncillaClosure`); parallel composition with an untouched spectator
  fails — the available two-qubit map has no available extension by a qutrit spectator
  (proved: `countermodel_not_qutritReferenceExtension`).
- **Deviation from QM:** an operation on a pair that is positive on every state of the pair
  produces negative statistics once the pair is entangled with a third system that the
  operation does not touch. The signature is spectator dependence: the outcome distribution of
  a local procedure depends on whether a distant, untouched reference is correlated with the
  pair (not formalized; the negative witness `−3/7` is proved).
- **Ruled out by:** a locality or causal-independence principle — the statistics of a
  procedure must not depend on correlations with a system it does not act on. This is the
  content of I itself, restated; the census shows it is not implied by C, K, well-formedness or
  the OI core (proved: the cell is nonempty), so it must be adopted as a principle if it is to
  hold (not formalized as a derivation).

### {C} — reversible control fails

- **Nonempty:** proved (`cell_C`).
- **Realized by:** the diagonal theory (`diagTheory`).
- **Allowed operations:** the normalized Kraus instruments whose every branch preserves
  computational-basis diagonal states, at every level (read off the definition). The 3-4-5
  rotation is unitary and unavailable (proved: `rot_not_preservesDiag`).
- **Closure:** all four closure rules hold (proved: `diag_validity`, `diag_inert`,
  `diag_iteratedAncillaClosure`, `diag_systemToLevelOne`); the class is closed under
  composition because diagonal preservation is.
- **Deviation from QM:** no operation creates coherence from a basis state, so no
  interference from basis preparations; the accessible unitaries are the monomial ones. The
  signature is the absence of interference fringes in any experiment prepared and read in the
  computational basis (not formalized beyond the rotation witness).
- **Ruled out by:** a reachability principle — the Lie-rank criterion of round fifty
  (`universalReachability_of_lieRank_unconditional`) derives full control from a drift and
  controls generating `su(D)`, so any physical principle supplying such a generating set rules
  the cell out (proved as an implication; the physical premise is not formalized).

### {K} — iterated composition fails

- **Nonempty:** proved (`cell_K`).
- **Realized by:** the rank-gap theory (`gapTheory`).
- **Allowed operations:** all Kraus instruments on the system; on a level-`N` composite, the
  instruments whose Kraus operators are each invertible or factor through at most `N` levels
  (read off the definition). The level-three gap channel with a rank-four Kraus operator is
  unavailable (proved: `gapChannel_not_gap`).
- **Closure:** sequential composition, spectator extension and full control hold (proved:
  `gap_inert`, `gap_control`); ancilla discard fails — the gap channel's unitary dilation is
  available one level up, and discarding the ancilla would produce it (proved:
  `gap_not_iteratedAncillaClosure`).
- **Deviation from QM:** a composite cannot be reused as a system. An operation that is
  realizable by acting on the composite with one more ancilla and then discarding it is not
  itself available; the signature is a channel whose Stinespring implementation succeeds while
  its direct implementation is forbidden, i.e. the resource count of an operation depends on
  whether an ancilla is bookkept as part of the system (not formalized).
- **Ruled out by:** a subsystem-universality or observer-nesting principle — a composite that
  an observer can treat as a system must be a system for the theory. The census shows K is not
  implied by I, C, well-formedness or the OI core (proved: the cell is nonempty).

### {I, C} — inert spectators and control fail

- **Nonempty:** proved (`cell_IC`).
- **Realized by:** the diagonal two-positive theory (`diagTwoPosTheory`): 2-positive,
  diagonal-preserving instruments on every composite.
- **Allowed operations:** read off the definition; the two-qubit reduction map is available
  (it preserves diagonals: `reduction2_preservesDiag`) and the rotation is not.
- **Closure:** ancilla discard holds (proved: `diagTwoPos_closure`); spectator extension fails
  at the reduction map (proved: `diagTwoPos_not_inert`).
- **Deviation from QM:** both signatures above at once: spectator dependence and no basis
  interference.
- **Ruled out by:** either principle above.

### {I, K} — inert spectators and iterated composition fail

- **Nonempty:** proved (`cell_IK`).
- **Realized by:** the capped two-positive theory (`cappedTheory`): 2-positive instruments on
  every composite, completely positive on levels one to three.
- **Allowed operations:** read off the definition; every unitary at every level (proved:
  `capped_control`); the level-six reduction map, 2-positive and not completely positive, is
  available above the cap.
- **Closure:** sequential composition holds; spectator extension fails at the level-six
  reduction map (proved: `capped_not_inert`); ancilla discard fails because the level-six
  reduction map discards to `(4·tr(X)·I − X)/23` on level three, which is not completely
  positive and so lies below the cap (proved: `capped_not_closure`).
- **Deviation from QM:** spectator dependence appears only on large composites, and an
  operation available on a system with two ancillas cannot be reduced to the system with one:
  the theory's positivity requirements depend on how many ancillas are bookkept. The signature
  is a size threshold in the admissible operations (not formalized).
- **Ruled out by:** a locality principle, or a subsystem-universality principle, each on its
  own.

### {C, K} — control and iterated composition fail

- **Nonempty:** proved (`cell_CK`).
- **Realized by:** the diagonal rank-gap theory (`diagGapTheory`): completely positive,
  diagonal-preserving instruments, gap-admissible on levels one to three.
- **Allowed operations:** read off the definition; the gap channel tensored with an untouched
  ancilla is available at level six and the gap channel is not available at level three.
- **Closure:** spectator extension holds (proved: `diagGap_inert`); the rotation is
  unavailable (proved: `diagGap_not_control`); the untouched-ancilla extension of the gap
  channel discards to the gap channel, which is below the cap (proved: `diagGap_not_closure`).
- **Deviation from QM:** no basis interference, and a composite cannot be reused as a system.
- **Ruled out by:** a reachability principle or a subsystem-universality principle, each on
  its own.

### {I, C, K} — all three fail

- **Nonempty:** proved (`cell_ICK`).
- **Realized by:** the capped diagonal two-positive theory (`cappedDiagTheory`).
- **Allowed operations:** the diagonal-preserving members of the capped two-positive theory
  (read off the definition).
- **Closure:** sequential composition and coarse-graining only.
- **Deviation from QM:** all three signatures.
- **Ruled out by:** any one of the three candidate principles.

## Completed OI and OI⁺ (round fifty-three)

The hierarchy is layered, not redefined (`OIBridge/CompletedOI.lean`):

- **`OICore`** is `RealizesSealedOICore`, the original principle, unchanged (proved: every
  earlier result and countermodel keeps its meaning by definition).
- **`CompletedOI`** is the core plus the five completion conditions. It is exactly finite
  operational QM (proved: `completedOI_iff_qm`), and since full composite control realizes the
  core, it is exactly the five conditions (proved: `completedOI_iff_physical`). Bare OI is not
  completed OI (proved: `oiCore_not_completedOI`).
- **`OIPlus`** is the core, well-formedness, and three principles with independent
  observational meaning, one per substantive condition:
  - *observational independence* — an available operation on a composite acts as itself when
    an untouched system is adjoined. Equivalent to inert spectators (proved); it is what makes
    independent observations jointly performable (proved: `parallel_of_observationalIndependence`).
    The compression is nil beyond the equivalence: this principle is the condition.
  - *reversible richness* — every available reversible transformation can be undone, and at
    every level a passive drift with finitely many controls generates `su(D)`. It gives full
    composite control by the round-fifty reachability theorem (proved:
    `control_of_reversibleRichness`); every well-formed fully controllable theory is reversibly
    rich, with the rank-one matrix unit as drift and all unitaries as controls (proved:
    `reversibleRichness_of_control`). This is a finite certificate about a generating set, not
    the postulate that every unitary is available.
  - *observer recursion* — a composite observable system is itself an admissible observable
    system at every level. It gives iterated composition through the shifted theory's own
    discard rule (proved: `closure_of_observerRecursion`); iterated composition with the
    identity and the relative readout at every level gives the shifted theory (proved:
    `observerRecursion_of_closure`).

Then `OIPlus ⟺ finite operational QM` on the qubit carrier (proved: `oiPlus_iff_qm`), and each
of the three principles fails on a theory with the core, well-formedness and the other two
(proved: `oiPlus_independence`, from the cells {I}, {C}, {K} above). On every nonempty finite
carrier the same equivalence holds for OI⁺ without the core conjunct, which is a qubit statement
and is redundant there (proved: `CarrierGeneralOIPlus.carrier_general_oiPlus`, `oiPlus_qubit_iff`). Not claimed: that any of
the three follows from bare OI (the census proves the opposite); that these are the only
natural principles; that well-formedness is derivable.

## Embedded observation (round fifty-six)

The first entry of the primitive-source audit (`PRIMITIVE-SOURCE-AUDIT.md`) concerns the
recursion principle. `EmbeddedObservation.lean` replaces the per-level existence claim of
observer recursion by one uniform structure: a family of finite operational theories on
every finite carrier that is regrouping-invariant (the positive-level families of the
observer at `S` are the system families of the observer at `S × Fin m`),
relabelling-invariant (availability is transported along every carrier bijection), and has
the given theory as its ambient member. Nothing in the principle mentions a discard, a
closure rule or a shifted theory. From it the kernel derives iterated ancilla closure
(`closure_of_embedded`, the embedded observer's own discard rule), the identity and the
relative readout at every level, hence observer recursion
(`observerRecursion_of_embeddedObservation`), and the level-one seam of well-formedness
(`systemToLevelOne_of_embeddedObservation`). Exact finite operational QM satisfies the
principle with the CP-instrument theory on every carrier as the family
(`embeddedObservation_of_qm`). The cell {K} above is the countercontrol: the rank-gap theory
carries the core, well-formedness, observational independence and reversible richness and
has no such family (`embeddedObservation_independent`). The compressed set — composite
operational validity, observational independence, reversible richness, embedded observation
— is equivalent to exact finite endomorphic operational QM on every nonempty finite carrier
(`carrier_general_oiPlusEmbedded`). The converse from observer recursion to embedded
observation is not claimed outside that equivalence, and the independence of the other two
principles from embedded observation is not re-established; the round-53 witnesses establish
it relative to observer recursion.

## Implementation locality (round fifty-seven)

The second entry of the audit concerns observational independence, and it is worked in the
order the audit demands. First the redundancy test: the cell {I} above, the round-34
countermodel, carries the OI core, composite operational validity and reversible richness,
and `ImplementationLocality.lean` shows it also carries embedded observation, through the
2-positive-instrument theory on every finite carrier as the family (`twoPosFamily`,
`countermodel_embeddedObservation`). It has no observational independence, so validity,
reversible richness and embedded observation do not force it (`redundancy_fails`). Second
the separation of form from existence: every spectator extension of the available two-qubit
reduction map along the qutrit index is `withSpectator`, and that extension is not available
(`form_fixed_existence_fails`). Third the primitive, stated below availability: an
implementation class of admissible operators at every carrier that generates availability
(each branch a finite sum of conjugations by admissible operators, trace preserved in
aggregate), is stable under adjoining uncoupled degrees of freedom, and is label-invariant
(`ImplementationLocality`). From it observational independence is derived
(`observationalIndependence_of_implementationLocality`), through the local form of the
extension of a conjugation, and so is validity. Exact finite operational QM is generated by
the full class (`implementationLocality_of_qm`). The countermodel is generated by no class
at all, since its reduction map is not completely positive
(`countermodel_not_implementationGenerated`): its failure is implementability, not context
stability. The compressed set — implementation locality, reversible richness, embedded
observation — is equivalent to exact finite endomorphic operational QM on every nonempty
finite carrier (`carrier_general_oiPlusLocal`). Whether context stability is redundant given
implementation generation is not settled.

## Microscopic reversibility (round fifty-eight)

The third entry of the audit splits reversible richness into inverse accessibility (every
available conjugation channel has its adjoint channel available) and Lie-rank richness (the
drift/control certificate at every level), the conjunction being reversible richness by
definition (`MicroscopicReversibility.reversibleRichness_iff`). The inverse clause is
derived from a dagger-stable implementation class, one in which the adjoint of an
admissible operator is admissible: an available conjugation channel is realized by
admissible operators and trace preserving, its Choi matrix is the dyad of the vectorized
operator, so every realizing operator lies on the ray of the channel's operator
(`kraus_of_conj_unitary`), and the adjoint family realizes the adjoint channel
(`inverseAccessibility_of_generated_daggerStable`). Exact finite operational QM is generated
by the full class, which is dagger-stable. The compressed set — reversible implementation
locality, Lie-rank richness, embedded observation — is equivalent to exact finite
endomorphic operational QM on every nonempty finite carrier (`carrier_general_oiPlusMicro`).
Whether the inverse clause is already forced by implementation locality, embedded
observation and Lie-rank richness is not settled in either direction: the kernel consumes it
exactly at the adjoint-closure hypothesis of the round-50 reachability theorem, and neither
a proof through the semigroup structure of the available unitaries nor a countermodel is
built.

## Elementary transitions (round fifty-nine)

The fourth entry of the audit derives the Lie-rank clause. First the redundancy test:
implementation classes closed under the operations a theory performs on implementations
generate a finite operational theory on every carrier, and the diagonal class — operators
with no off-diagonal entry — is such an architecture. Its generated theory carries
reversible implementation locality and embedded observation and has no composite unitary
control, since every available conjugation preserves diagonal matrices and the round-42
rotation does not (`LieRankSource.diagGen_not_control`), so the clause is not forced
(`lieRank_not_redundant`). Then the primitive, stated in elementary implementations: at
every level every real transition `E_ab + E_ba` is continuously drivable, every exchange is
available, and a quarter phase on every state is available
(`ElementaryTransitionRichness`). From one driven transition, the exchanges and one quarter
phase the control Lie algebra is shown to contain `su(D)` — a permutation relabels the
transition, the phase turns it into its imaginary partner, and the bracket of the two gives
the population differences (`hControl_star`) — so Lie-rank richness follows
(`lieRank_of_elementary`). Full control supplies every elementary transition
(`elementary_of_control`). The compressed set — reversible implementation locality,
elementary transition richness, embedded observation — is equivalent to exact finite
endomorphic operational QM on every nonempty finite carrier (`carrier_general_oiPlusElem`),
and every principle in it is now stated at the level of implementations or the observer
architecture. The minimal elementary repertoire is not settled.

## What the census says and does not say

- The three principles are three independent axes on the class of well-formed OI-compatible
  theories (proved). Any derivation of one of them must therefore introduce a physical premise
  strictly stronger than the sealed OI core plus the other two principles; the census bounds
  what such a derivation can be, and does not supply one.
- The map "which principle fails ↔ which signature detects it" is: I ↔ spectator dependence of
  local statistics; C ↔ absence of coherence generation, restricted accessible unitaries;
  K ↔ a resource count that depends on ancilla bookkeeping. These are interpretations of
  proved kernel witnesses, not formalized predictions.
- Not claimed: that any cell is physically realized; that the witnesses are canonical
  representatives of their cells; that OI selects any cell; anything about the two
  well-formedness conditions failing together with substantive ones. The completion
  classification is unchanged.

Kernel: `verification/lean-mathlib/OIBridge/SubstantiveCensus.lean` (77 named results, axioms
`propext`, `Classical.choice`, `Quot.sound` only). Probe: `bohr_frequency_probe.py`, F64.
