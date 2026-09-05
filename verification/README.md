# Verification suite

Machine-checked certificates for the finite and algebraic core of the OI papers, in three
layers:

- **`lean/`** — six self-contained **Lean 4 proof files** (zero dependencies: no Mathlib, no
  lake project) for the lattice, gauge-counting and staggered-fermion statements of `papers/SM.md`
  and `papers/GR.md`, with **numerical probes** (Python 3) that instantiate every hypothesis and
  conclusion on the concrete operators, exactly in integer or rational arithmetic wherever the
  statements are integer identities.
- **`lean-mathlib/`** — `OIBridge`, the Mathlib-based formal verification programme: 115 modules and,
  at this commit, 2,421 named results, each printing its axiom dependencies (`propext`, `Classical.choice`,
  `Quot.sound` and nothing else; no `sorry`, no `axiom`, no `native_decide`). It carries the
  reconstruction theorems of `papers/GR.md` §3.3 and the OI → finite-QM completion classification,
  and it is the project's main theorem-verification layer.
- **`coverage/LEDGER.json`** — the proof-coverage ledger: every canonical manuscript statement,
  the kernel theorem or probe that certifies it, its level (K3 exact / K2 / K1 / P probe / GAP),
  and the recorded delta between manuscript and formal statement. `tools/coverage_check.py`
  enforces it; `tools/release_gate.py` runs that check with the others.

The two kernel verdicts are always reported separately: the zero-import files and the Mathlib
project have their own toolchains and their own CI jobs, so a breakage in either can never be
mistaken for a verdict on the other.

## The flagship result

`OIBridge/GeneralCarrier.lean`, `main_result` — for every nonempty finite observable system:

    exact finite operational quantum mechanics
      ⟺  valid probabilities
        ∧ trivial-ancilla consistency
        ∧ inert spectators
        ∧ full reversible control
        ∧ iterated composition

Exactness means the available outcome families on the system and on every ancilla level are
exactly the normalized finite Kraus instruments (`exactAll_iff_physical_general`). Both directions
are kernel-internal with no external premise. Two of the five conditions are well-formedness
requirements and three are substantive selection principles (`exactAll_iff_substantive`); each
condition is independent of the other four and of the observation process, exhibited by a qubit
theory realizing the sealed OI core that satisfies the other four and fails that one
(`RankGapTheory.five_way_minimality`, witnesses `everywhereAvailable`, `countermodel`,
`diagTheory`, `gapTheory`, `systemLoose`). Bare finite OI therefore does not select quantum
mechanics (`oi_alone_not_qm`); the theorem classifies the OI-compatible completions and does not
derive quantum mechanics from observation (`oi_compatible_classification`). The manuscript
statement is `papers/GR.md` §3.3, *Theorem (operational-completion characterization)*.

The three substantive principles are independent axes, not merely pairwise independent: every
one of the eight patterns of holding and failing is realized by a well-formed theory carrying
the sealed OI core (`SubstantiveCensus.substantive_census`), so no Boolean relation among them
holds on that class (`no_boolean_relation`), and QM is the single no-failure cell
(`qm_is_the_top_cell`). The census, with the exact operations of each cell and the observable
deviation each permits, is `CENSUS-oi-compatible-theories.md`.

The hierarchy is layered rather than redefined (`CompletedOI.lean`): `OICore` is the original
principle, unchanged; `CompletedOI` is the core plus the five conditions, equivalent to finite
operational QM and, since full control realizes the core, to the five conditions alone. The
three substantive principles are compressed to principles with independent observational
meaning: observational independence (an operation acts as itself when an untouched system is
adjoined), reversible richness (available reversible transformations can be undone, and a
drift with finitely many controls generates `su(D)` at every level), and observer recursion (a
composite observable system is itself an admissible observable system). `OIPlus`, the core with
well-formedness and these three, is equivalent to finite operational QM (`oiPlus_iff_qm`), and
each of the three is independent of the core, well-formedness and the other two
(`oiPlus_independence`). None of the three follows from bare OI. The equivalence holds on every
nonempty finite carrier (`CarrierGeneralOIPlus.carrier_general_oiPlus`): there the sealed qubit
core has no counterpart, OI⁺ is well-formedness plus the three principles, and on the qubit
that definition is provably the one with the core conjunct (`oiPlus_qubit_iff`). Observer recursion
is itself derived (`EmbeddedObservation.observerRecursion_of_embeddedObservation`) from embedded
observation: one family of finite operational theories on all finite carriers, regrouping-invariant
(the level-`m` families of the observer at `S` are the system families of the observer at
`S × Fin m`), relabelling-invariant, with the given theory as its ambient member. The same principle
yields the level-one seam of well-formedness, so composite operational validity, observational
independence, reversible richness and embedded observation are equivalent to finite operational QM
on every nonempty finite carrier (`carrier_general_oiPlusEmbedded`); the rank-gap theory shows that
the core, well-formedness and the other two principles do not supply embedded observation
(`embeddedObservation_independent`). The converse from observer recursion to embedded observation is
not claimed outside that equivalence. Observational independence is not forced by validity,
reversible richness and embedded observation (`ImplementationLocality.redundancy_fails`: the round-34
countermodel carries all three through the 2-positive family on every carrier); it is derived
(`observationalIndependence_of_implementationLocality`) from implementation locality, a class of
admissible operators at every carrier that generates availability, is stable under adjoining
uncoupled degrees of freedom, and is label-invariant. The countermodel is generated by no class at
all (`countermodel_not_implementationGenerated`), so its failure is implementability. Implementation
locality, reversible richness and embedded observation are equivalent to finite operational QM on
every nonempty finite carrier (`carrier_general_oiPlusLocal`). Reversible richness splits into inverse
accessibility and Lie-rank richness (`MicroscopicReversibility.reversibleRichness_iff`); the inverse
clause is derived from a dagger-stable implementation class through the rank-one ray lemma
(`inverseAccessibility_of_generated_daggerStable`), so reversible implementation locality, Lie-rank
richness and embedded observation are equivalent to finite operational QM on every nonempty finite
carrier (`carrier_general_oiPlusMicro`). Lie-rank richness gives full control unconditionally
(`PositiveReachability.control_of_lieRank`), and on a well-formed theory full control yields inverse
accessibility (`PositiveReachability.inverseAccessibility_of_lieRank`), so dagger stability is not
needed as a hypothesis of the characterization. The Lie-rank clause is derived from elementary
transition richness (`LieRankSource.lieRank_of_elementary`): one continuously driven transition, one
quarter phase and the state exchanges generate `su(D)` at every level, and full control supplies
them (`elementary_of_control`), so reversible implementation locality, elementary transition
richness and embedded observation are equivalent to finite operational QM on every nonempty finite
carrier (`carrier_general_oiPlusElem`). The diagonal architecture shows the clause is not forced by
the other two (`lieRank_not_redundant`). Every principle in the package is now stated at the level
of implementations or the observer architecture, none Lie-algebraic.

## Contents (`lean/`)

- `OI_Gauge_Certificates.lean` — telescoping/plaquette triviality for arbitrary abelian
  alphabets; central-sign collapse for every odd q; the kernel-checked cubic counting
  layer (24 / 72 / 288 / 144) behind the local-gauge closure argument of `papers/SM.md`;
  and the character layer above it — the five irreducible characters of O given as
  functions on the group elements rather than as a trusted class table, their
  orthonormality, and the multiplicities of V₆, End(V₆) and the broken restriction.
- `OI_Regulator_Symmetry.lean` — the regulator-symmetry certificates: the character sums
  of the induced action on quadratic forms, over the 384-element hypercubic group and the
  96-element native group, for both the metric sector Sym²(ℝ⁴) and the field-strength
  sector Sym²(Λ²ℝ⁴), together with the invariance of the named basis forms and the
  countercontrol showing the electric form is not hypercubic-invariant.
- `OI_Structural_Core.lean` — Theorem 1a of `papers/SM.md` at operator level (exact
  projected evolution and kernel equivariance), the Susskind factorization's cancellation
  mechanism, Theorem 3's chirality algebra, and the quadratic boost-Ward identity.
- `OI_Staggered_Relations.lean` — the staggered generator relations (phase involutions,
  commuting shifts, and the axis-order sign pattern) imply pairwise anticommutation and
  the squares, and hence the factorization for **any number of axes** — by structural
  induction over a list of pairwise-anticommuting summands, with the three- and four-axis
  statements as corollaries. Axes are indexed by natural numbers, so one structure serves
  every dimension.
- `OI_Structural_Chain.lean` — the detailed-balance lemma stated without the exponential
  (edgewise balance plus connectivity forces proportionality, in a commutative monoid, with
  no division and no spectral argument), and the cubic quadratic invariant: the character of
  the induced action on Sym²(ℝ³) sums to 48 over the signed permutation group and 24 over its
  rotations, with δ exhibited invariant and a direction-singling form shown not to be.
- `OI_Time_Reversal.lean` — Theorem 17 of `papers/SM.md`: time-reversal invariance of the
  discrete wave equation, stated over an arbitrary additive commutative group of field values
  with the spatial stencil abstract, so both the displayed nearest-neighbour form and the
  d-dimensional reading are instances.
- `*_probe.py` — twenty-nine probe files, all run by CI. `gauge_certificates`, `structural_core`,
  `staggered_relations`, `structural_chain`, `representation_bridge` and `time_reversal` are the
  companions of the proof files above: every integer the Lean files submit to `decide` is
  recomputed by an independent construction. The rest instantiate the `OIBridge` theorems on
  explicit finite data — `bohr_frequency_probe.py` carries the F-series (F1–F81, one per
  round of the reconstruction and completion programme, each reading the kernel file it
  certifies back for its claim discipline) and `edge_rigidity_probe.py` carries the R7 lint,
  which requires every listed kernel result to be a `theorem` with a `#print axioms` line and
  guards the claim boundaries round by round.
- `VERIFYING.md` — how to run everything; `ROADMAP.md` — the original plan for the zero-import
  layer.

## Contents (`lean-mathlib/`)

One lake project, pinned to `leanprover/lean4:v4.33.0` and mathlib4 `v4.33.0`.
`OIBridge.lean` imports every module, so `lake build` checks all of them; `OIBridge/` holds the
modules, in the order the development grew:

- **Representation bridge and counting** (`Averaging`, `CombRealization`, `LinkDecomposition`,
  `QuarterTurn`, `TasteBranching`, `GaugeDimension`, `CubicIsotropy`): the averaging identity
  and the equivariant-map dimension formula derived from Mathlib, the transport of the cubic
  counting layer onto a `Representation` (`dim Hom_G(V₆, V₆) = 3`), and the SM-side lattice
  statements that need Mathlib's linear algebra.
- **The equivalence chain and memory** (`EquivalenceChain`, `FiniteEntropy`, `HiddenMemory`,
  `Equivalence`, `C3Necessity`, `CanonicalMeasure`, `Finiteness`, `FactorUniqueness`,
  `IdempotentTrace`, `Irreducibility`, `KrausUniqueness`, `StinespringUniqueness`,
  `Separability`, `WeylTwirl`, `WeylLift`, `BoundaryRank`, `Reciprocity`): the finite-horizon
  equivalence of `papers/Main.md` §3.4, the memory and necessity theorems, and the
  Weyl-twirl separability results.
- **Hamiltonian reconstruction** (`BohrFrequency`, `FrequencyMatching`, `PiccardBridge`,
  `EdgeRigidity`, `HomometricSix`, `HomometricKill`, `CongruentReconstruction`,
  `TurnpikeScopeTransfer`, `AntiunitaryInvariance`, `ThermalOrientation`, `ShellAssignment`):
  Bohr-frequency completeness and the two-branch D-gauge theorem of `papers/GR.md` §3.3, the
  homometric exception killed, the operational antiunitary invariance, and the thermodynamic
  orientation selector.
- **Coherent completions** (`CoherentLift`, `TwoByTwoNoGo`, `AccessibleAlgebra`,
  `OperationalRigidity`, `JordanClassification`, `OrientationSelection`, `OrientationClosure`,
  `CycleFibreHull`, `DynamicsGlue`, `DomainGlue`, `ObservabilityQuotient`, `PassiveQuotient`,
  `ControlledQuotient`, `CoherentExtension`, `ProjectiveAction`, `ControlLie`): existence
  obstructions for visible-local coherent lifts, the coherent-completion classification
  (unitary gauge or one global antiunitary reversal), the orientation no-go, the observability
  quotients, and the control Lie algebra.
- **Instruments, dilation and assembly** (`InstrumentDilation`, `Purification`,
  `BranchSelector`, `IndependenceCensus`, `MonoidalCompletion`, `OperationalAssembly`,
  `StinespringAssembly`, `KrausSoundness`, `CompositeSoundness`, `HiddenCoherence`,
  `AncillaInterference`, `PartialTranspose`, `FactorExchange`, `DimensionalObstruction`,
  `DimensionalCountermodel`, `BoundaryAudit`): the finite operational theory structure, the
  Stinespring circuit assembly giving every finite Kraus instrument from composite unitary
  control, Kraus soundness, the positive-but-not-completely-positive countermodel, and the
  first boundary audit (PSD factorization discharged internally).
- **The completion classification** (`ReferenceExtension`, `ReferenceSufficiency`,
  `SpectatorBridge`, `AncillaClosure`, `ClosureObstruction`, `CompositionalIndependence`,
  `OIRealization`, `OperationalValidity`, `LevelOneSeam`, `PhysicalCharacterization`,
  `DiagonalTheory`, `RankGapTheory`, `IsometryExtension`, `GeneralCarrier`,
  `UhlmannUniqueness`, `ReachabilitySeam`, `OrbitReachability`, `SubstantiveCensus`,
  `CompletedOI`, `CarrierGeneralOIPlus`, `EmbeddedObservation`, `ImplementationLocality`, `MicroscopicReversibility`, `LieRankSource`, `SubstratumSource`, `SubstratumInterface`, `ReadWriteControl`, `StructuralClosure`, `TypedCompletion`, `RegionLimit`, `RegionTower`, `QuasilocalAlgebra`, `QuasilocalCharacterization`, `InstrumentCompletion`, `InstrumentAvailability`): the five completion conditions defined one by one with the countermodel
  that separates each, the sealed OI core realized with its actual visible readout, the
  characterization theorem with its necessity direction, the five-way minimality audit, the
  discharge of finite isometry extension, the removal of the qubit restriction, the discharge
  of finite right-unitary uniqueness, the compact-Lie reachability seam reduced to one local
  lemma and that lemma proved, the eight-cell census of the three substantive principles, and
  the layered hierarchy with the three principles compressed to observational independence,
  reversible richness and observer recursion, and that hierarchy carried to every nonempty
  finite carrier.

`verification/MILESTONE-finite-quantum-instruments.md` records an earlier checkpoint of this
programme as a status artifact.

## The external boundary

Each `OIBridge` theorem states its own hypotheses; the standard finite-dimensional facts the
development once cited rather than proved are tracked as an explicit ledger, updated in place
with provenance preserved (`BoundaryAudit.lean`, `IsometryExtension.lean`,
`UhlmannUniqueness.lean`, `ReachabilitySeam.lean`, `OrbitReachability.lean`):

- **Discharged internally:** PSD square-root / factorization (`psdFactorization_discharged`);
  finite isometry extension for every finite carrier (`finiteIsometryExtensionSF_discharged`,
  from Mathlib's orthonormal-basis extension theorem); finite right-unitary uniqueness,
  `A Aᴴ = B Bᴴ ⟹ B = A U` with `U` unitary on a common environment (`rightUnitary_of_gram`);
  compact Lie integration / reachability (`OrbitReachability.localReachabilityOfLieRank`) —
  if the dynamical control Lie algebra contains `su(D)`, the subgroup generated by the
  passive flows, the controls and the phases is a neighbourhood of the identity in the
  unitary group. The proof is specialized to the compact matrix-group setting: the orbit
  directions `Ad(r)(−iH)` and the phase direction span a real subspace closed under the
  bracket by one derivative, a finite family of them spans it, the product of their
  one-parameter groups paired with a Hermitian complement has surjective strict derivative
  at `0`, and the inverse-function theorem with local injectivity of `exp` finishes. Around
  it: local reachability gives exact reachability by the open-subgroup theorem and the
  connectedness of the matrix unitary group (`exact_of_local`), exact reachability gives
  every unitary conjugation channel (`universalReachability_of_exact`), and the
  round-nineteen criterion `𝔏 ⊇ su(D) ⟹ universal unitary reachability` holds with no
  external premise (`universalReachability_of_lieRank_unconditional`).
- **Remaining:** none.

Formal external-boundary ledger: empty. OI/QM classification and finite compact-matrix
reachability routes kernel-internal within their stated hypotheses. The primitive-source
audit (`PRIMITIVE-SOURCE-AUDIT.md`) carries the classification one level below the five
operational conditions: observer recursion and the level-one seam derive from embedded
observation, observational independence and the positivity half of validity from
implementation locality, the inverse clause of reversible richness from dagger-stable
implementations, and the Lie-rank clause from elementary transition richness. The strongest
carrier-general statement is therefore that implementation locality, elementary transition
richness, and embedded observation are together equivalent to exact finite endomorphic
operational quantum mechanics on every nonempty finite carrier
(`PositiveReachability.carrier_general_oiPlusPos`), with every principle stated at the level of
implementations or the observer architecture and no dagger clause: the compact-group argument for
the inverse clause is carried out in `INVERSE-CLAUSE-AUDIT.md`, the dagger-stable package
(`LieRankSource.carrier_general_oiPlusElem`) characterizes the same class
(`oiPlusPos_iff_oiPlusElem`), and the repertoire is cut to one continuously driven pair and the
exchanges, with no quarter phase (`MINIMAL-REPERTOIRE-AUDIT.md`,
`MinimalRepertoire.carrier_general_oiPlusMin`). A separate substratum-source audit
(`SUBSTRATUM-SOURCE-AUDIT.md`) opens the next question — whether the concrete OI physics supplies
that structure — and its first entry collapses the three primitive-source principles onto one
object: a theory generated by a context-, label-, and dagger-stable, elementary-driving
implementation architecture is exactly finite operational QM
(`SubstratumSource.genTheory_qm_of_quantumArchitecture`), with elementary drivability the decisive
property the abstract stabilities do not entail (`diagGen_not_quantumArchitectureGenerated`). Its
second entry fixes the interface between substratum interventions and implementation operators and
proves a baseline no-go: the observable operators of bijective and phase interventions are monomial,
and a theory whose available conjugations are all monomial has no control and is not QM, because a
genuine two-state rotation is not monomial (`SubstratumInterface.monomialSource_not_qm`,
`rot_not_monomial`) — finite bijective dynamics alone does not supply the decisive operator. Its third entry audits the
decisive escape route, read-write coupling, and returns the no-go for the current axioms: a
read-write family (a selectable local coupling, bijective at every parameter value) induces only
permutation operators, so a read-write-sourced theory is a monomial source and is not QM
(`ReadWriteControl.readWriteSourced_not_qm`); a strict interpolation toward the swap is not a
bijection (`offDiagonal_interp_not_monomial`), so the tunable coupling produces no off-diagonal
generator, and the memory-swap countercontrol shows bidirectional read-write is not off-diagonal
controllability (`readWriteControl_independent`). Under the current axioms a continuously tunable
off-diagonal coupling is an irreducible empirical addition; no control law is introduced to force
it. Its fourth entry closes the structural audit: the class the substratum supplies — the monomials
of the second entry, nothing added — is an architecture, context-stable, label-invariant and
dagger-stable (`StructuralClosure.substratumClass_structurallyClosed`, through the elementwise form
`monomial_iff_submonomial`), so for the substratum the quantum-architecture question is exactly
elementary drivability (`quantumArchitecture_iff_drives_of_closed`); the substratum class does not
drive the elementary transitions and its generated theory is not QM (`substratum_residual`), while
any structurally closed extension that does drive them generates finite operational QM on every
nonempty carrier (`substratum_plus_control_qm`) and QM is generated by such an extension
(`qm_generated_by_substratum_extension`): current OI substratum plus continuous off-diagonal
controllability is finite operational QM, the controllability being a hypothesis on the extension
and not a property of the current substratum. The
canonical OI⁺ statements are frozen and this audit does not modify them. The substratum-source form of
the conclusion is propagated to the manuscripts (GR §3.3, with cross-references in Main §3.4, the
Explainer, and book chapters 1 and 19) under its scope guards: not bare OI ⇒ QM, the controllability
resource not derived from A1–A6, finite and endomorphic, nonempty finite carriers, the control
resource an empirical extension of the current substratum, and no claim that the elementary control
repertoire is minimal. The programme is publication-frozen at the substratum-source state, and the
OI→QM derivation programme is closed at this commit: OI alone admits many theories; the concrete OI
substratum supplies all of the structural requirements for quantum mechanics but not continuous
state-mixing controllability; quantum mechanics is obtained exactly when that one remaining physical
resource is added. The compact-semigroup redundancy of the inverse clause is proved
(`INVERSE-CLAUSE-AUDIT.md`), and the control repertoire is cut to one continuously driven pair
and the exchanges (`MINIMAL-REPERTOIRE-AUDIT.md`): the one physical resource beyond the substratum
is a single continuously driven transition.

**Level II (OI_Q): the typed completion.** A new thread, with bare OI and the frozen Level I
statements untouched, asks whether "endomorphic" in the Level I conclusion is a physical limitation or
an artifact of the typing, as a redundancy test rather than by postulate (`TypedCompletion.lean`,
`TYPED-COMPLETION-AUDIT.md`). A typed finite operational theory (`TypedOperationalTheory`) has an
availability predicate on outcome families of maps between any two finite carriers, with the closure
rules of the endomorphic structure at their carrier-general type and no dilation clause; its
endomorphic shadow is a `FiniteOperationalTheory` on every carrier and is automatically an
embedded-observation family (`shadow_embeddedObservation`). Under the shadow hypothesis — exact finite
endomorphic QM on every nonempty carrier, what Level I supplies — a family between nonempty carriers is
typed-available exactly when it is a typed Kraus instrument (`typed_determined`,
`typed_determined_of_oiPlusElem`), by register wrapping and compression for soundness and by a
uniform ancilla, a relabelling and register operators for completeness; the converse holds by
restriction to one carrier, so the shadow is quantum exactly when the typed theory is the finite
typed quantum theory (`typed_determined_iff`). The interface carries no
quantum content: the typed diagonal theory satisfies every rule and its shadow is not QM
(`typed_interface_not_quantum`). For this interface the fork closes with full redundancy: no fresh
chosen-state preparation and no coherence condition beyond the typed closure rules is needed, so
"endomorphic" is a typing artifact. The typed form is propagated to the manuscripts (GR §3.3, with
cross-references in Main §3.4, the Explainer, and book chapters 1 and 19) with the interface
qualification stated beside it, and Level II is frozen at this commit: within the natural
carrier-general extension of the operational rules already used at Level I, the remaining qualifier
is finite-dimensional rather than endomorphic.

**Level III (OI_Q): the quasilocal-completion audit.** Opened as an audit, not a postulate
(`RegionLimit.lean`, `QUASILOCAL-COMPLETION-AUDIT.md`): no continuity, completeness or Hilbert-space
axiom is added, and every claimed necessity comes with a countermodel. The corpus holds the lattice
fundamental at fixed spacing, so there is no spatial continuum limit to recover: the directed system
the substratum supplies is the family of finite regions, a larger region adjoining a factor `S × R`,
and its limit is the infinite-region (quasilocal) lattice theory. Its restriction maps are the Level II discard
(`restrict_eq_discardR`) with the observable inclusion as dual (`trace_inclObs_mul`); the reference
family and every pure product family are consistent under restriction; their overlap on `n` adjoined
`q`-state sites decays as `q^{-n}` (`overlap_uniform_pure`, `overlap_eventually_small`), the finite
shadow of the fact that the physical representation is selected only by a choice of reference family;
and continuous time is not determined by the discrete dynamics — two Hermitian generators whose flows
agree at every integer time and differ at `t = 1/2` (`continuous_extension_not_unique`). Of the
pre-registered outcomes, the region system is redundant with the frozen interface; whether a
distinguished representation is a theory-level input or merely a state selection within one
quasilocal theory is open; a continuous-time law is an input only if the target is continuous-time
Hamiltonian QM rather than discrete-time quasilocal QM; and no continuum-structure gap arises
because no continuum structure is claimed. The second entry (`RegionTower.lean`) formalizes the actual
region tower — regions as finite sets of sites — and proves that inclusion of observables and
restriction of states are functorial along chains of regions and dual under the trace pairing, the
transitivity of restriction being derived from that of inclusion (`inclObs_trans`, `restrict_trans`,
`trace_inclObs_mul_restrict`); proves the causal cone for an update with a coupling graph
(`iterate_dependsOnlyOn_ball`, `readout_unaffected_outside_ball`), so discrete-time dynamics is
compatible across regions by locality alone; and settles the state-selection question at the level
of laws: consistent families are closed under mixing, the reference family is consistent, and the
uniform state is the unique normalized state invariant under the substratum's own bijective and phase
interventions (`consistent_mix`, `uniform_family_consistent`, `invariant_normalized_eq_uniform`), so a
sector selector would be a state-level input of the initial-condition kind rather than an axiom of
the theory. The third entry (`QuasilocalAlgebra.lean`) constructs the infinite-region object itself:
the local algebra as the algebra of equivalence classes of finite-region observables (`emb_eq_iff`),
realized as a ring on the free vector space over global configurations, which carries no inner
product, norm or state; the inclusions as star homomorphisms that are injective and hence isometric
for the operator norm (`norm_inclObs`); the C*-norm on the local algebra and its abstract norm
completion, a C*-algebra (`instCStarAlgebraQuasilocal`) that is literally the closure of the union of
the finite stages (`closure_iUnion_stage`); every consistent family of density matrices as a unital
positive state of the completion, by unique continuous extension (`quasiState_unique`,
`quasiState_nonneg`); and every reversible finite-range dynamics as an isometric star automorphism
of the completion, with the transport of a local observable localized on an explicit finite region
(`heis_emb`, `heisQ_mul`, `norm_heisQ`, `heis_iterate_emb`). No representation is chosen, no
continuity or continuous-time law is added, and no Hilbert-space representation is constructed; the
quasilocal algebra is identified with the discrete-time quasilocal target by definition. The fourth
entry (`QuasilocalCharacterization.lean`) removes that tautology: the target class is defined
independently of the construction — a C*-algebra with compatible injective unital star embeddings of
the finite matrix stages, observables of disjoint regions commuting (`emb_comm_of_disjoint`, a
finite-stage theorem), and the stages dense (`QuasilocalSystem`) — the OI completion is a member
(`oiSystem`), and it is the unique member up to a canonical star isomorphism compatible with the
stages, obtained from the universal property of the local algebra and of the completion
(`localHom_unique`, `canonEquiv`, `canonHom_surjective`, `canon_unique`, `systemEquiv_unique`);
states and the OI-induced dynamics transport along it (`systemState_isState`, `canon_dyn`,
`systemEquiv_dyn`). The dynamics target is decided by a countermodel rather than chosen: a
locality-preserving phase automorphism of the quasilocal algebra is induced by no reversible
finite-range substratum dynamics (`phase_localityPreserving`, `phaseQ_ne_heisQ`), so the Level III
equivalence is stated for the OI-induced discrete automorphism and not for general
locality-preserving dynamics. Uniqueness is among systems with these local stages; no
Hilbert-space representation is constructed. Level III is frozen at that entry and propagated to
GR §3.3 with cross-references in Main §3.4, the Explainer, and book chapters 1 and 19: the
canonical infinite-region completion of OI_Q is, up to a canonical star-isomorphism, the unique
quasilocal fixed-lattice C\*-system carrying the substratum's local stages and OI-induced discrete
dynamics — the uniqueness theorem the kernel proves rather than a biconditional. It carries the
eight scope guards listed in `QUASILOCAL-COMPLETION-AUDIT.md`: the quantum completion condition
retained, the lattice fundamental, the uniqueness relative to these local stages, the dynamics
restriction proved rather than adopted, no representation or sector selected, continuous time
optional and separately shown undetermined, the Level I and Level II statements kept as their own,
and the completion covering the algebra, states and OI-induced dynamics rather than all
infinite-dimensional instruments or all locality-preserving dynamics.

**Post-Level III: the instrument audit.** Level III completed the algebra, the state space and one
discrete dynamics; it did not complete the operational availability relation of Level II, and that
seam is the subject of an audit rather than a new level (`InstrumentCompletion.lean`,
`INSTRUMENT-COMPLETION-AUDIT.md`). The first entry fixes the Heisenberg convention, defines three
nested candidate classes without adopting one — finite-support, stage-compatible, and all
completely positive instruments on the completion — and decides the first pre-registered question
in both directions: a finite-support quasilocal instrument is exactly a finite-region Kraus
instrument with the Level II normalization (`qInstrument_of_kraus`, `kraus_of_finiteSupport`,
`finiteSupport_iff_kraus`), acting on larger regions by the inert spectator extension
(`qBranch_stage_inclObs`) and fixing the observables of disjoint regions
(`qTotal_stage_of_disjoint`). Finite-support instrument totals do not exhaust the stage-compatible
quasilocal maps: the all-sites phase family is compatible with the inclusions, gives an isometric
unital star-endomorphism of the completion — invertibility is not proved and is not needed — and is
the total map of no finite-support instrument (`phaseAllWt_compat`, `phaseAll_not_finiteSupport`).
It is not itself packaged as an instrument: class 2 is not formalized in this entry. Not decided, and not claimed either way: whether a general
compatible family extends, whether such families are operationally available under OI_Q, whether
the Kraus class exhausts the completely positive instruments, and whether an operational-completion
principle is required. The abstract completely positive class is not formalized in this entry. The second entry decides
Q3 negatively (`InstrumentAvailability.lean`). A countermodel declares an operation available
exactly when it is a finite-support instrument; it is a predicate on the frozen Level III objects,
which are unchanged (`states_untouched`, `dynamics_untouched`), contains every finite-region endomorphic
Kraus instrument the Level II theory supplies inside this fixed-carrier interface and no more
(`availFS_of_kraus`, `kraus_of_availFS`), and is closed under the identity, composition, outcome
relabelling, outcome coarse-graining and the frozen OI-induced dynamics (`availFS_id`,
`availFS_comp`, `availFS_relabel`, `qBranchJ_coarse`, `availFS_dyn`) — yet the all-sites phase map
is the total map of no available operation at any finite outcome index (`phaseAll_not_availFS`).
The current frozen structure together with finite-support quasilocal availability therefore does
not entail the availability of genuinely infinite-support coherent operations, within this
fixed-algebra interface (`q3_countermodel`), and Q5 sharpens: an extension requiring them needs
some additional principle, an addition rather than a consequence, with "operational completion" a
proposed name rather than a uniquely forced one. This is independence from the frozen structure,
not impossibility: nothing says OI forbids such operations. Level II's typed attachment and discard
change the carrier, are not expressible by this predicate, and stay separately frozen. The third entry
is a corpus census rather than a Lean development: the live corpus was searched for the vocabulary
in which an operation of unbounded support would appear, with the countercheck being whether the
existing argument already justifies finite support rather than whether a finite rewriting is
available. The load-bearing operational theorems carry finiteness in their own hypotheses (finite
accessible horizon, finite carriers, finite circuits); the causal cone bounds the rest; GR's
classical horizon temperature and its classical passivity layer are derived from a finite total
system and an explicitly finite bath, with no thermodynamic limit, and what the horizon thermal
claim contributes to the calibration is reduced to finite-system detailed balance under an explicit
finite-observer error budget; and the remaining claims that invoke an infinite background —
stationary distributions, the KMS state itself, horizon mode counts, gravity as the macroscopic
behaviour of the coupling structure — invoke *states* and *counts*, which the countermodel keeps in
full, rather than operations. No live claim requires an infinite-support intervention, and no item
is left unclassified: SM's cycle ergodicity and large-`L` stationary distribution concern the
substratum's own dynamics, where what stays open is the analytical derivation of the Lyapunov
coefficient rather than any operational availability. Q2 and Q4 therefore stand as
optional mathematical extensions outside the core programme, in the position continuous time
occupies relative to Level III. That finding is a survey of the corpus at this commit, not a
theorem, and is to be re-run if a claim performing an unbounded operation is added.

`REPRESENTATION-SECTOR-AUDIT.md` runs the same evidence-first method on the neighbouring seam.
Level III's theorem is that the laws select no Hilbert-space representation and no superselection
sector; the audit asks the narrower question of whether any current prediction requires an
independent representation or sector choice beyond its state data. It does not. The criterion is
stated carefully: a state on a C\*-algebra already determines a GNS representation and sector
information can ride on classes of states, so inequivalence alone establishes nothing — a burden
exists only where a claim needs a choice the algebra and its state do not already make. GR's
thermal conditions are state conditions and the corpus says so in its own headings; the
discriminating data is a ratio of detector transition rates, fixed once the state is, so the
α-vacua, whose standard treatment is representation-level, impose no extra postulate. That data is
not claimed finitely checkable — the slope invoked is a derivative and a bounded frequency window
is not a finite observable set. Substratum Lemma 24.1's GNS/Stinespring step
runs on a finite cyclic subspace; SM's chiral symmetry breaking is diagnosed by finite-volume
scaling; its θ-vacuum passage narrows a parameter and is recorded open on H-top and H-det;
Structure's Fock space and von Neumann algebra are Step 1 of a comparison recipe whose remaining
steps the corpus lists as open, with no prediction resting on the pair. Where a selection burden
does exist it is state-side and already named: GR records ℏ and the `1/4` as conditional on
H-state, with an additional state principle logically necessary because the realization theorem
admits vacuum-like and excited laws over the same partition. Two items are recorded as ambiguous
rather than resolved — the algebraic status of H-state's "vacuum class", and whether GR's
conditions transport from the emergent theory's states to states on the quasilocal algebra, a map
the corpus does not construct. That transport is a seam between the GR/H-state layer and the
Level III lattice state space rather than a reopening of the OI→QM programme, and is backlogged
rather than made a required round. Representation construction therefore stands as optional
mathematics outside the core programme, on the same survey-not-theorem footing.

`CONTINUOUS-TIME-AUDIT.md` opens the dynamics thread. Level III froze a discrete dynamics and
recorded continuous time as additional structure on the strength of a non-uniqueness countermodel;
that countermodel says nothing about existence, which is what this thread asks. The first entry
answers it. Reversibility forces the previous-slice coefficient to `-1` in SM's general
second-order form, so the phase-space map on the per-site pair is `(p, c)` to `(c, F(c) - p)`, and
`OIBridge/SecondOrderCircuit.lean` proves for an arbitrary site type and arbitrary neighbourhood
function that this factors as a **depth-two circuit**: a shear layer and an on-site swap layer,
each an involution, each a product of commuting single-site gates. The gates commute because a
shear gate writes only its own site's previous component and reads only current components, which
no gate writes — so the factorization is insensitive to linearity, alphabet, dimension, and
state-dependence of the coupling. An involution gives a projection and hence an exact
one-parameter unitary, polynomial rather than a functional calculus, reaching the gate at time one;
the gates are supplied as elements of the quasilocal algebra of the infinite lattice, with each
generator bounded and lying in a single finite region's stage. Two layers of such gates, driven
over `[0,1]` and `[1,2]`, reach their composite exactly. Existence and per-gate locality are
settled affirmatively. Two things the first entry leaves outside its scope: the drive theorem
quantifies over a finite list of gates rather than constructing the all-sites layer as an
automorphism of the quasilocal algebra, and the local-Hamiltonian statement needs a finite-range
hypothesis on the neighbourhood function that the factorization itself does not. A **single
time-independent** generator is not obtained and is not claimed,
the drive being piecewise constant across the two layers, and uniqueness stays decided negatively
by the frozen countermodel. Continuous time remains additional structure rather than part of the
core: the entry shows the structure is available, not that OI supplies it.

The second entry supplies the all-sites layers. `OIBridge/SecondOrderLayer.lean` builds the shear
layer by stabilization — only the finitely many gates whose regions meet a finite region `Λ` can
move an observable of `Λ`, so conjugating by that finite product agrees with conjugating by any
larger one — and `OIBridge/SwapLayer.lean` does the same for the swap layer, where a gate occupies
a single site and the stabilization hypothesis is plain inclusion. Each layer is a strongly
continuous one-parameter group of `*`-automorphisms of the quasilocal algebra: group law, inverse,
isometry, and strong continuity in the time parameter. `OIBridge/SecondOrderDrive.lean` composes
them. The order is settled by theorem rather than convention: `permOp` is covariant while
`heis` sandwiches its argument between a covariant and a contravariant factor, so a configuration
map that shears first and swaps second has a Heisenberg action that applies the **swap** flow first
and the shear second (`heis_of_comp`, `heisQ_of_comp`). The composite is claimed to be exactly a
norm-continuous path of `*`-automorphisms through the identity — start at the identity, every point
an isometric automorphism, continuous in the parameter — and **not** a one-parameter group: the two
layers do not commute, so no group law for the composite follows, and none is asserted. The
update itself is packaged as a `ReversibleDynamics` (`ruleDynamics`), with the coupling data
supplied in all four directions and reversibility taken from the factorization rather than assumed,
and `heisQ_ruleDynamics` applies the order theorem to it. Both layer endpoints are then identified. A dynamics
supported in one finite region has a permutation operator that *is* a local operator — the embedded
permutation matrix of that region's permutation — so its Heisenberg action is conjugation by one
stage's element; and two dynamics that give a region the same restricted configuration and the same
off-region agreement relation act the same on that region's observables. For the swap layer those
two facts suffice, once the finite product of on-site gates over a region is collapsed into the
single permutation matrix of the swap of the whole region. For the shear layer the region-supported
replacement shears at every site of `affected R Λ` rather than only of `Λ`, since a gate whose
neighbourhood meets `Λ` does not commute with `Λ`'s observables; the collapse of the gate product
is the same argument, and the off-region agreement matches because a site outside the affected set
has a gate region disjoint from `Λ`. So `swapQ_one_eq_heisQ`, `layerQ_one_eq_heisQ` and
`driveQ_one_eq_heisQ` identify the two flows and their composite at time one with the frozen
Heisenberg actions: the path starts at the identity and **ends at the update**. What stays
unclaimed is the group law for the composite, and any generator. The finite-range hypothesis
the first entry anticipated is load-bearing here and is carried as a field of the `Rule` structure
rather than as an ambient assumption.

The third entry opens CT3, restated in the form the infinite lattice permits. An extensive
Hamiltonian is not an element of the quasilocal algebra, so the target is not `H` with
`e^{iH} = U` but **one time-independent finite-range interaction whose automorphism group `τ_t`
satisfies `τ_1 = heisQ(Φ_OI)`**. CT2 already settles part of it: each layer *separately* is
autonomously generated, so CT3 asks whether the composite of two autonomously generated local
flows is itself autonomously generated locally — the Floquet-versus-static question.
`verification/lean/static_generator_probe.py` runs the cheapest necessary test before any
logarithm. An autonomous flow makes its generator a conserved quantity of one discrete step, so on
a finite periodic lattice `P† H P = H` for `H = Σ_x h_x` of width `w`; the census dimension is the
nullity of that system minus the closed-form redundancy of the parametrization, with ranks exact
over `GF(p)` in the direction an obstruction needs. Because `P` is a permutation matrix the
centralizer splits into a diagonal part (conserved classical densities) and an off-diagonal part,
and a diagonal `H` exponentiates to a diagonal unitary — so an autonomous local generator needs
off-diagonal weight. Because `rank_p ≤ rank_ℚ` the modular census is an upper bound only, which cannot
establish that the centralizer exceeds the scalars, so the dimension is bracketed from both sides:
kernel vectors are rationally reconstructed and verified against every equation exactly over `ℤ`.
For the corpus rule that gives 1, 7 and 25 at `w = 1, 2, 3` as upper bounds with certified lower
bounds 1, 7 and 14 — exact over `ℚ` at `w ≤ 2`, bracketed `14 ≤ dim ≤ 25` at `w = 3` — splitting
(modularly) as 1+0, 3+4 and 5+20 and stable in `L`, with an explicit integer `H` of nonzero
off-diagonal weight verified over `ℤ` at `w = 2` and `w = 3`. **The centralizer test therefore does
not obstruct**: candidates survive and the exponential
condition has to be tested. Controls make that readable — two rules whose leap is on-site, which
provably do admit a static generator, give dimensions 37 and 505, so the method detects generators
where they must exist, while a one-sided coupled control gives 1. The census is run at `w ≤ 3` and
is not a statement about all finite ranges; nothing claims a static generator exists, and a
negative CT3 would not obstruct continuous-time evolution in the ordinary time-dependent sense.

The fourth entry settles one branch of CT3 and is careful about what that does not mean. If
`e^{iH} = U` with `H` Hermitian then `H` is quantized on each eigenspace of `P`, which splits the
problem: `H` a function of `P` (linear), or `H` acting inside degenerate eigenspaces (nonlinear).
`verification/lean/spectral_logarithm_probe.py` settles the first. Since `P^r` sends a
configuration's basis vector to `σ^r` of it, a function of `P` has matrix entries only on pairs
`(σ^r b, b)`; for a full-period `b` the entry at `σ^r b` is exactly `c_r`, so exhibiting one such
`b` whose displacement escapes every width-`w` window forces `c_r = 0`. That certificate costs
`O(m·N·L)` rather than `O(L·q^{4w})`, so it reaches **every** width below the system size rather
than stopping at `w = 3`: `S_w = ℝ·I` at every `w ≤ L−1`, by witness and by an independent exact
rational solve. The spectral logarithm branch is dead. **It closes nothing**, and the control is
what shows it: the on-site rules, which provably do have static local generators, return the same
answer, because for them the generator is a sum while `P` is a product and so is not a function of
`P` at all. Six of R1's seven width-2 dimensions act inside degenerate eigenspaces and remain the
open case: a six-parameter family of local Hermitian `H` modulo scalars, each required to have on
every `P`-eigenspace a spectrum inside the corresponding `2π`-lattice coset. Those are dimensions
of `H` and not of `K` — writing `H = H₀ + 2πK` is spectral bookkeeping, and `H₀` is a spectral
function of `P` and so nonlocal by this very round — and six is a fixed-volume count, since a
stable dimension does not show the solution directions are compatible across volumes.

The fifth entry builds the artifact R2-B consumes and then obstructs width 2 with it.
`verification/lean/centralizer_basis_probe.py` constructs an exact integer basis of the width-2
local centralizer, each element verified against every defining equation over `ℤ`, complete against
the R1 census with the identity in its span. `P^m = I` forces every eigenvalue of `H` into the
single lattice `−θ + (2π/m)ℤ` with the `ω^r` block at residue `n ≡ −r (mod m)`; summed over a block
that is linear in the coefficients and computable from `Π_r = (1/m)Σ_k ω^{−rk}P^k` without
diagonalizing. The Hermitian search space splits into a real-symmetric sector, where
`T_{m−r} = +T_r`, and `i`×(real-antisymmetric), where `T_{m−r} = −T_r`; at width 2 the second has
identically zero block traces, which is computed rather than assumed and is what confines the
result to that width. Then `d_{m−r} = d_r` makes `k = e_{m−r} − e_r` annihilate every column, and
the block condition collapses to `(m−2r)d_r/m ∈ ℤ` with no free parameters — failing as `204/5` at
`L = 5` and `1340/3` at `L = 6`. **Width-2 R2-B is obstructed at both volumes**, by exact integer
certificate. The on-site controls, which do have static local generators, are not obstructed, since
their `m = 2` admits no conjugate pair. Rank was the wrong diagnostic: a low-rank trace map makes
the condition harder to satisfy, not easier. Width `≥ 3`, and the transport to infinite volume,
remain open — the periodization bridge is now load-bearing.

The sixth entry closes the arithmetic that test rests on, for `q = 2`.
`verification/lean/wave_period_probe.py`, with the proofs in
`CT3-R2B-Q2-PERIOD-AND-CYCLES.md`, works from the traveling-wave factorization
`x² + (S+S⁻¹)x + 1 = (x+S)(x+S⁻¹)` in its d'Alembert form: every `𝔽₂` solution on `ℤ²` is
`f(n−t) + g(n+t)`, with a two-dimensional representation kernel spanned by the constant and the
parity function. Imposing both periodicities gives `dim_{𝔽₂} ker(F_L^k − I) = 2gcd(k,L) −
1_{L,k odd}`, hence `m_L = L` for even `L` and `2L` for odd `L`, and by Möbius inversion the exact
cycle spectrum — `C_ℓ = M(ℓ)` for even `L`, `C_e = M(e)/2` and `C_{2e} = M(e)/4` for odd `L`, with
`M` the aperiodic-necklace count on four letters — so `D_s` and the first-moment test are decided at
every `L` without enumerating `4^L` states. Silence at `L = 2^a` is a theorem, from
`v₂(C_{2^i}) = 2^i − i ≥ j − 1`. The converse fails: at an odd prime `L = p > 3` both admissible
tests reduce to `p² | 4^{p−1} − 1`, the Wieferich condition base 2, so **`L = 1093` and `L = 3511`
are silent and are not powers of two**. This round also corrects the corpus: the period formula of
`SM` Appendix A / book Appendix B.3.1 read `L` at `q = 2`, where the value is `2L`, and the uniform
`ord(F mod q) = qL` holds at every prime (the appendix's Jordan-Chevalley theorem is consistent
with this but gives only that the factor orders divide `L` and `q`);
`rank(N) = 2` likewise holds only for even `L`. Width `≥ 3`, infinite volume and `q = 3` stay open.

`OI-CORE-FORWARD-REDUNDANCY.md` freezes one reading of the finite equivalence, because the theorem
admits a stronger paraphrase than the formalization supports. Three statements, and only these
three. **Containment**: `qm_implies_oiCore` — every theory in the characterized quantum class
realizes the sealed OI core, by the route `QM → full composite unitary control →
RealizesSealedOICore`. **Redundancy**: `completedOI_iff_physical` — the OI conjunct is implied by
the five physical conditions, so it does no work in the forward derivation; what selects quantum
mechanics is coherent controllability. **No ontological necessity**: `OICore` is an existential
realizability condition about a particular four-state gadget, so a containment theorem about it is
not an explanatory one, and nothing shows a hidden sub-quantum level is required — with density
matrices as states, informationally complete measurements exist, so the universally quantified form
of observational incompleteness is false at the quantum-state level. `oiCore_forward_redundancy`
collects the three. The core keeps its positive role: it defines what counts as an OI realization,
which is what gives `oi_alone_not_qm` content. `tools/claims_check.py` guards the paraphrase with
an `OI_CLAIMS` class carrying its own marker list.

`C1C4-MINIMALITY-AUDIT.md` is the corpus audit of C1 coupling, C4 readback, hidden predictive
memory, raw versus minimal carrier, the observability quotient and passive minimality, read against
the frozen results. One defect: Chapter 18's summary of the framework's logical chain read
"recurrence guarantees that **any partition** of `S` will exhibit returns of information from hidden
to visible", dropping C1, where `[Main]` §2.3 and Chapter 1 §1.7 both carry finiteness **and** C1.
`verification/lean/partition_coupling_probe.py` certifies the countermodel exactly: the uncoupled
product system `φ(v,h) = (v+1, h+1)` on `ℤ/3 × ℤ/4` recurs at `φ¹² = id`, yet every two-time visible
matrix is a permutation independent of the hidden prior, the family is divisible at every
intermediate step, and total variation is constant — recurrence without any restoration. The control
is the corpus's own coin-and-die system, where C1 holds, the one-step matrix is `[[2/3,1/3],[1/3,2/3]]`,
and total variation contracts `1 → 1/3` and returns in full at `t = 2`; so the measurement is not
blind. Both parallel book sources now name C1 in the chain, and the `R7-AUDA` guard holds them
there. The other five axes came back clean and are recorded as such, with one status fact: no ledger
entry attaches to `PassiveQuotient.lean` or `ObservabilityQuotient.lean`, so the minimal-carrier
machinery is kernel-proved infrastructure that currently underwrites no manuscript statement.

`CONCRETE-CUT-AUDIT.md` is Audit B, the concrete-cut audit of the physical papers, with its census
under `audit-census.json`. Finding B1: `[GR]` §2.2, headed *Verification of the conditions*, verified
C1, C2 and C3 at the cosmological horizon and had no C4 entry, while §8.4 listed "the C1–C4
conditions" among the `ħ` derivation's dependencies, the book's Chapter 7 said §7.2 "verifies that
the cosmological horizon satisfies the framework's four conditions" and inferred C4 from the
bidirectionality of the boundary coupling, and `[Main]` §1.3 deferred the read-write cycle to the
companion work as "a property to be independently demonstrated there". Each paper treated the other
as the place readback across the horizon is established, and neither established it; bidirectional
coupling is a strengthened C1 and persistence is C2, and `[Main]` §3.4 derives C1 and C3 *from* C4,
so verifying those two cannot supply it. The repair manufactures no proof: `[GR]` §2.2 carries a
fourth entry recording C4 as a named realization condition at the cosmological cut, **not presently
discharged**, with what remains stated; both book sources carry the same status; and C4 is not added
as a hypothesis of the `ħ` derivation, which is carried by H-slope with the horizon and frame
conditions. The SM lattice cut is the honest model — Theorem 22 has C1 structural, the C3 floor by data
processing, and C2 and C4 as explicit hypotheses with the discharging lemmas named unproved — and the
audit found three residues around it: Layer 0 listing C1–C4 as inputs to a gauge chain that consumes
none of them, §2.1's inventory omitting C4 and saying C2 holds for any system with the right partition
geometry, Chapter 1's C4 definition calling the horizon read-write cycle automatic, and — in the
paragraph after it and again in the Introduction — three conditions listed as what sustains the
memory-bearing sector and all four declared satisfied by enormous margins. All repaired in every
parallel source, to a two-row status that must not be collapsed: at the cosmological cut C1 verified
structurally, C2 and C3 verified with enormous margins, C4 open; at the lattice cut C1 structural,
C3 a capacity floor for the realized process, C2 and C4 hypotheses.
The `R7-AUDB` guard holds all of it.

`CONCRETE-CUT-FREEZE.md` is the corrected interpretation the two audits earned, stated once in the
form the guards enforce. It copies the canonical two-row table verbatim from `CONCRETE-CUT-AUDIT.md`
and freezes five readings with the locations that carry each: the recurrence chain names C1; C4 is
the primitive and is discharged at neither physical cut; C1–C4 are diagnostics of a realization,
not hypotheses of the `ħ` calibration or of Layer 0; the OI core is forward-redundant; and the
minimal-carrier machinery underwrites no manuscript statement. OI-N opens from it; CT3 stays paused
behind OI-N.

`OI-N-EXPLORATORY.md` opens the exploratory necessity thread from the frozen status, and
`OIBridge/PassiveObservation.lean` closes its two easy ends. A **passive instrument** is a finite
family of completely positive maps whose nonselective channel is the identity; **OI-N1**
(`passive_branch_scalar`, `no_complete_passive_observation`) proves every branch is a scalar
multiple of the identity — the identity's Choi matrix is rank one (`choiMatrix_id`), the branches'
Choi matrices are positive semidefinite and sum to it, and a positive semidefinite summand of a
rank-one matrix is a multiple of it (`psd_summand_of_rankOne`, from
`PosSemidef.dotProduct_mulVec_zero_iff` and an elementary double-orthogonal-complement step) — so
the outcome law is the same for every state and no passive instrument separates states when the
algebra has two of them. **OI-N2** is the commutative control: the pinching instrument is completely
positive, is the identity on diagonal matrices, and separates diagonal states — while on the full
algebra its nonselective channel is dephasing and it is not passive (`pinching_not_passive`) — so
the contrast identifies noncommutativity as the candidate obstruction, whose exact finite-dimensional
boundary is N3. Ten named results, each printing only `propext`, `Classical.choice`, `Quot.sound`.

`OIBridge/CentralObservation.lean` is **OI-N3**, and it closes that boundary as a classification.
The finite-dimensional C*-algebra `⊕_i M_{d_i}` is taken in block-diagonal matrix form, for a
labelling `blk : S → I` of basis states by blocks; a passive instrument on it is a finite family of
completely positive maps on the ambient algebra whose nonselective channel fixes every
block-diagonal matrix; intrinsic instruments on the algebra admit the corresponding ambient
extension by the block conditional expectation; that transport is not formalized here, and the
kernel statements are for `IsBlockPassiveInstrument` as defined. The central theorem,
`central_classification`: every such instrument induces a
classical stochastic observation of the center — `tr (F_a ρ) = ∑_i c_{a,i} · tr (P_i ρ P_i)` on
every block-diagonal `ρ`, with `c_{a,i} ≥ 0` from complete positivity and `∑_a c_{a,i} = 1` from
passivity on every nonempty block; nothing inside a block is read. The two steps beyond the single
block are proved, not assumed: **block preservation** (`branch_preserves_block`) — passivity on the
block projector `P_i` forces every Kraus operator of every branch to vanish between distinct blocks
(`exists_kraus` from the kernel's `psdFactorization_discharged` and `kraus_of_choi_factor`;
`kraus_block_vanish` reads the diagonal of `K P_i K†`), so no branch moves probability between
blocks — and **blockwise scalars** (`branch_scalar_on_block`) — the restriction of a branch to the
fibre of block `i` has Choi matrix a principal submatrix of the original
(`choiMatrix_restrictMap`), the restricted family is a passive instrument on the fibre
(`restricted_passive`), and N1 makes each branch a scalar there. The control `blockPinch`,
`X ↦ P_i X P_i`, is passive on the algebra and reads the block weights. The boundary: a block with
two basis states carries two pure states every passive instrument confuses
(`no_complete_passive_of_block`); with singleton blocks the control separates states
(`blockPinch_separates`); so complete passive observation of `⊕_i M_{d_i}` is possible iff each block
contains at most one basis state, the labelling injective and every nonempty `d_i = 1`
(`complete_passive_iff_injective`), iff the algebra is commutative
(`injective_iff_commutative`, `complete_passive_iff_commutative`). Thirteen named results, each
printing only `propext`, `Classical.choice`, `Quot.sound`. Scope: the block-diagonal form is the
object; the Wedderburn–Artin identification of an abstract finite-dimensional C*-algebra with it is
not formalized.

`OIBridge/PassiveIndependence.lean` is **OI-N4**: passive incompleteness is theory-insensitive,
and carries no discriminatory information about the OI core. `PassivelyIncomplete T`
says no family a theory `T` makes available on the system is both passive and state-separating;
by N1 it holds for every theory on a carrier with two or more states
(`passivelyIncomplete_of_card`, `passivelyIncomplete_qubit`) — it is carrier-intrinsic and does
not vary with `T`. The OI core does vary: `diagTheory` realizes it, and `labelTheory` — the
diagonal theory with ancilla-label preservation (`KeepsLabels`) in place of diagonal preservation
on composite operations — does not, because the OI control `τ` flips the ancilla's second bit
(`tau_moves_label`, `label_not_oiCore`). So `OICore T → PassivelyIncomplete T` holds for every
`T` with the hypothesis idle (`oiCore_to_passive_vacuous` is N1 alone), and
`PassivelyIncomplete T → OICore T` fails (`passivelyIncomplete_without_oiCore`,
`passive_not_implies_oiCore`); `passive_nondiscriminating` is the diagram, one vacuous
implication and one failing converse, the two notions orthogonal — one fixed by the observable
algebra, the other by the theory's hidden-memory and control structure. What varies is the sector:
the pinching instrument is a Kraus family preserving diagonals (`pinching_isKrausFamily`,
`pinching_preservesDiag`), so both theories are passively complete on their commutative sector and
passively incomplete on the full algebra (`sector_diagram`) — passive (in)completeness tracks the
observable algebra, the N3 boundary, and is the same on both sides of the OI-core line. Fourteen
named results, each printing only `propext`, `Classical.choice`, `Quot.sound`. Scope: `labelTheory`
is a witness against `OICore` and no completion condition is claimed for it; the cell
`OICore ∧ ¬ PassivelyCompleteOnDiagonal` is neither inhabited nor shown empty.

`OIBridge/InternalObserver.lean` is **OI-N5**, the internal observer: a passive self-record can only
be read, never written. On a carrier with a record map `blk : S → O` — for a system-plus-register
carrier the visible value `rec b` of the register, `recBlk` — an instrument **records** when branch
`o` sends every block-diagonal input into record block `o`, and an **internal observer** is a
recording instrument that is passive on the record-block algebra. **N5.0**
(`no_full_passive_self_record`): passivity on the full joint algebra with a two-valued record is
impossible — N1 makes every branch a scalar, and a scalar confined to one record block on another
block's projector is zero. **N5.1**, rigidity (`branch_kills_other_block`,
`branch_fixes_own_block`, `internal_branch_eq_blockPart`, `internal_outcome_law`): block
preservation from N3 and the record condition together force branch `o` to annihilate every other
record block and fix its own, so on every block-diagonal state `F_o ρ = P_o ρ P_o` and
`p(o | ρ) = tr (P_o ρ P_o)`. **N5.2**, the boundary (`internal_complete_iff`,
`no_complete_internal_observer`): complete passive internal observation iff each record block
contains at most one carrier state, equivalently iff the record map is injective, so every nonempty
record block is one-dimensional; hence a separate register never observes a system with two or
more states completely
and passively, whatever function of the register the record is. Controls: the singleton record
partition, where the block-label instrument is a complete passive internal observer
(`classical_control`); and the recorder "measure `A`, write the register" (`recordInstr`), completely
positive, recording, and genuinely record-creating (`recordInstr_writes`), whose nonselective
channel dephases the system and resets the register, so it is not passive on the record-block
algebra (`recordInstr_not_passive`, `recordInstr_not_internal`). Acquiring a new record changes the
joint system. Fourteen named results, each printing only `propext`, `Classical.choice`,
`Quot.sound`. Scope: the record semantics is the one `Records` fixes; nothing about consciousness,
self-modelling or an observer's ontology, and nothing about `OICore`. With N5 the thread's five
items are closed; the thread stays exploratory in status, and `R7-OIN` guards all four modules.
`OI-N-FREEZE.md` states the endpoint once — noncommutativity forbids complete passive
observation; passive incompleteness does not diagnose `OICore`; a passive internal observer can
only read an existing record; creating a genuinely new internal record requires changing the
joint system — each line the name of a kernel theorem, with what is frozen, how it is enforced and
what it does not claim. Extending the thread needs a new charter. Not
claimed: that quantum mechanics requires OI or a hidden ontology — `qm_implies_oiCore` is
containment, the necessity reading is not a theorem of this thread, and N4 shows passive
incompleteness in a theory with no OI core at all; "passive" here is not the passive quotient of
`PassiveQuotient.lean`.

`COMPLETION-ASSUMPTION-AUDIT.md` reconciles the completion-assumption reduction charter
(`EQUIVALENCE-STRENGTHENING-ROADMAP-2026-09-05.md`) with the kernel. The charter asks that each of
the five completion assumptions end as DERIVED or INDEPENDENT with a kernel witness; the note
records that every row is settled by the primitive-source and substratum-source audits — the seam
from embedded observation, closure from observer recursion, inert spectators and validity from
implementation locality, control from elementary transition richness through Lie-rank richness
with no dagger clause (`lieRank_of_elementary`, `control_of_lieRank`) — each with its independence
countercontrol, and that the charter's "current
exact package" is the round-41 five-condition statement while the most compressed package
currently recorded is
`OIPlusElem` (`carrier_general_oiPlusElem`). The one witness the charter asks for that the kernel
did not carry is supplied by `OIBridge/LevelOneRecursion.lean`: the loose theory has observer
recursion (`systemLoose_observerRecursion`) and no level-one seam, so the seam is independent of
observer recursion (`levelOne_independent_of_recursion`, `levelOne_row`) — three named results,
each printing only `propext`, `Classical.choice`, `Quot.sound`. The residual items are listed as
open and none is settled by that note: the minimal elementary repertoire, context stability given
generation, and the empirical addition of continuous off-diagonal controllability; the inverse
clause is settled by the next entry. Guard `R7-CAA`.

`INVERSE-CLAUSE-AUDIT.md` and `OIBridge/PositiveReachability.lean` remove dagger stability from
the exact characterization. The question, preregistered as a fork (direct redundancy, inverse
derivation only, independence) and attacked in that order, is whether Lie-rank richness alone
gives full composite unitary control with no inverse of a control available; Outcome A holds.
The **positive reachable monoid** `posReach H U` is the submonoid of the unitary group generated
by the flows, the controls and the phases, every element of which is available by composition
alone (`avail_of_mem_posReach`). The positive powers of a unitary recur in the compact unit ball
(`exists_pow_tendsto_one`), so `m^{p_k-1} → m†` along a subsequence (`exists_pow_pred_tendsto_star`)
— the only form in which an adjoint is used; the real span of the positive orbit directions is
closed and `Ad`-invariant, hence `Ad(m†)`-invariant by limit (`adStar_mem_posSpan`), hence
preserved by `e^{t Ad(m)(-iH)} = m e^{-itH} m†` (`exp_posDir_conj_mem_posSpan`), so the
round-fifty derivative step makes it a Lie subalgebra containing the control Lie algebra
(`bracket_mem_posSpan`, `controlLie_le_posLie`) and every skew-Hermitian matrix when `𝔏 ⊇ su(D)`
(`skew_mem_posSpan`). Greedy nested prefixes of positive words with spanning directions exist by
induction on the codimension (`map_adEquiv_posSpan₀`, `exists_nested_spanning`); the word
`A_1 e^{-it_1H} ⋯ A_n e^{-it_nH}` is a positive word (`wordMap_mem_posReach`) with strict
derivative `h ↦ (Σ_j h_j Ad(A_1⋯A_j)(-iH)) · B` (`wordMap_hasStrictFDerivAt`); with a phase and a
Hermitian complement the round-fifty `Ψ` has surjective derivative (`psiW_hasStrictFDerivAt`,
`psiDerivW_surjective`), so the inverse-function theorem makes `posReach` a neighbourhood of `B`
(`posReach_mem_nhds_totalProd`); a submonoid that is a neighbourhood of one of its elements is a
neighbourhood of `1` by recurrence (`nhds_one_of_nhds_mem`); and a submonoid containing the
phases that is a neighbourhood of `1` is everything, since a symmetric neighbourhood generates a
clopen subgroup of the connected unitary group and the subgroup it generates is the submonoid it
generates (`eq_top_of_nhds_one`, `posReach_eq_top`). `universalReachability_of_lieRank_positive`
is the round-fifty conclusion with the `hstar` hypothesis deleted. At the theory level,
`control_of_lieRank` gives `LieRankRichness T → HasCompositeUnitaryControl T`,
`inverseAccessibility_of_lieRank` derives the inverse clause on a well-formed theory, and
`OIPlusPos` — implementation locality, elementary transition richness, embedded observation, with
no dagger stability — is equivalent to exact finite endomorphic operational QM on every nonempty
finite carrier (`oiPlusPos_iff_qm`, `oiPlusPos_iff_oiPlusElem`, `carrier_general_oiPlusPos`).
Twenty-four named results, each printing only `propext`, `Classical.choice`, `Quot.sound`. Not
claimed: that `HControl` is necessary for positive reachability; the minimal elementary
repertoire; the converse from inverse accessibility to dagger stability; anything about
non-compact groups. Guard `R7-INV`.

`MINIMAL-REPERTOIRE-AUDIT.md`, `OIBridge/MinimalRepertoire.lean` and
`verification/lean/repertoire_lie_probe.py` cut the elementary repertoire to one continuously
driven pair and the exchanges. The question — how much of "every pair driven, every exchange, a
quarter phase on every state" is needed — was preregistered as a fork after one exact
computation fixed the hypothesis: the drives on the edges of a bipartite graph generate inside a
conjugate of `so(D)` with no diagonal direction, a theorem for every colouring and so for every
even cycle, while the tested odd cycles `3, 5, 7` generate `su(D)` (the probe, exact over `ℚ`:
odd cycles `8, 24, 48`, even cycles `6, 15, 28`, paths `3, 6, 10, 15`, complete graphs
`8, 15, 24`), so one drive with one cyclic permutation is not a uniform finite-carrier repertoire;
generation for the complete graph is the theorem, and no general non-bipartite theorem is proved.
The primitive is therefore **phase-free richness**:
at every level with two or more states, some pair is continuously driven and every exchange of
two distinct states is available. Outcome A holds. On three or more states one driven transition
and the permutations generate `su(D)` with no phase — two drives sharing a state bracket to the
imaginary transition on the third pair, which the quarter phase used to supply (`bracket_XX`,
`hControl_perm`, through the round-59 decomposition isolated as `hControl_of_XYZ`). The
**bipartite obstruction** is a theorem: for any colouring, the drives on bichromatic pairs and
the colour-compatible permutations generate inside the colour-phase conjugate of the real
antisymmetric matrices (`colourAlg`, `controlLie_le_colourAlg`), so no population difference is
reached (`diag_zero_of_mem_controlLie`, `popDiff_notMem_controlLie`,
`not_hControl_of_colourCompatible`); the qubit with its drive and every permutation of its two
states (`not_hControl_two`) and the even cycle with one drive (`not_hControl_evenCycle`) are its
instances, so the single-cycle candidate has an even-carrier countercontrol, and one adjacent
exchange added to the cycle gives every permutation. At the levels with two or
fewer states, control **descends** from level `3n`: `U ⊗ 1` is available there
(`control_at_level`, through `universalReachability_of_lieRank_positive`, no inverse and no
phase), iterated ancilla closure — derived from embedded observation — returns its
uniform-attach-then-discard to level `n`, and the discard of `conj (U ⊗ 1)` is `conj U`
(`tensorOf_one_isometry`, `discard_tensorOf_one`, `descend`); classical coarse-graining plays no
part. Hence `control_of_phaseFree`, and `OIPlusMin` — implementation locality, phase-free
richness, embedded observation — is equivalent to exact finite endomorphic operational QM on
every nonempty finite carrier (`oiPlusMin_iff_qm`, `oiPlusMin_iff_oiPlusPos`,
`carrier_general_oiPlusMin`). The discrete part of the repertoire is two elements: one full
cycle and one adjacent exchange generate every permutation, inverses being positive powers
(`perm_avail_of_cycle_swap`, `phaseFree_of_cyclic`). Twenty-three named results, each printing
only `propext`, `Classical.choice`, `Quot.sound`. Not claimed: that one driven transition is
minimal in any stronger sense; that the driven pair can be replaced by a discrete resource; that
the OI substratum supplies it. Guard `R7-MIN`.

`ROUTE-B-AUDIT.md` and `OIBridge/RouteB.lean` open Route B — whether the continuously driven
transition is independent of everything the kernel derives from the substratum — and stop at its
specification, milestone B0. `DerivedOI` is the conjunction of the theory-level predicates the
kernel proves both for a theory generated by the substratum class and for exact quantum mechanics:
reversible implementation locality, embedded observation, and the availability at every level of
the exchanges, the phases and the read-write operators; `DerivedOICore` adds the sealed OI core on
the two-state carrier. The falsifier is the rotation `rot`, whose availability phase-free richness
forces through the closure embedded observation supplies (`falsifier_available_of_phaseFree`), so
a theory with embedded observation in which `rot` is unavailable fails phase-free richness
(`not_phaseFree_of_falsifier_unavailable`). Quantum mechanics satisfies the closure
(`derivedOI_of_qm`, `derivedOICore_of_qm`), so the closure is consistent. The target,
`RouteBTarget`, a two-state theory satisfying `DerivedOICore` with `rot` unavailable, is stated and
not proved; a witness would separate the closure from phase-free richness (`target_separates`) and
would not be quantum mechanics (`target_not_qm`). The substratum theory, generated by the
monomial class, satisfies the closure on every carrier (`substratumTheory_derivedOI`) and lacks
the falsifier on the two-state carrier (`substratumTheory_falsifierUnavailable`, the stronger
statement than the absence of full control), so `target_of_substratum_core` reduces the target to
one hypothesis and B1 is one question: whether that theory realizes the sealed OI core. Nineteen
named results, each printing only `propext`, `Classical.choice`, `Quot.sound`. Not claimed: that a
countertheory exists, that the substratum theory realizes the core, or that `DerivedOI` exhausts
what bare OI entails beyond what the kernel derives at this commit. Guard `R7-RB0`.

`LEAN-MANUSCRIPT-CENSUS.md`, `tools/lean_manuscript_census.py` and
`verification/lean-manuscript-census.json` synchronize the manuscripts with the whole kernel rather
than with the latest round. The check, run by the release gate as `lean-manuscript`, resolves every
kernel identifier and path cited in a manuscript against `OIBridge`, refuses a paragraph that cites
a superseded theorem without its successor, requires every module to carry one of five registry
dispositions — current, consistent-uncited, scope-consistent, kernel-only, verification-only —
requires every family under the first three to name at least one manuscript anchor, and requires
every anchor to be present in the manuscript it names. The check is complete relative to the
maintained registry and cannot infer that a theorem inside an existing module has become stronger;
the registry contract of `AGENTS.md` §A.35, pinned by `R7-MSP`, requires every publication-facing
strengthening to update the registry in the same commit. The census
found three stale citations, all at the seam the inverse-clause result moved: the strongest
characterization named reversible implementation locality and the dagger-stable package in GR §3.3,
Main §3.4, the Explainer and both book chapters with their mirrors; the OI⁺ reversible-richness
certificate cited the reachability theorem with the inverse clause; and the typed form cited the
package-level corollary from the dagger-stable package, for which
`OIBridge/TypedPositive.lean` supplies `typed_determined_of_oiPlusPos`, one result printing only
`propext`, `Classical.choice`, `Quot.sound`. All three are repaired; the five-condition
characterization and the OI⁺ layered form are stated as such beside the strongest statement; the
substratum endpoint is unchanged; OI-N is narrated in one paragraph of Main §3.4 and one of the
Explainer, outside the assumptions and arrows of the characterization, with the N4 anti-conflation
in the same paragraph (theory-insensitive, no evidence of a hidden ontology, no statement that QM
rests on OI); guard `R7-OINN`. The SM counting layer and the Main §3.4 equivalence chain carry
kernel pointers at the proof or list paragraphs that follow their principal statements, the
statement lines and the coverage ledger untouched (`theorem_7`, `finrank_intertwiners`,
`ohInvariant_iff`, `theorem_8`, `theorem_16`, `theorem_19`; `finite_horizon_equivalence`,
`S_imp_D`, `permMatrix_mem_unitaryGroup`, `isDiag_Phi`, `c3_necessity`,
`unavoidable_hidden_predictive_memory`, `entanglementBreaking_twirl`), both families current, pointers only and no restatement; guard
`R7-PTR`. CT2 is narrated in GR §3.3's continuous-time paragraph, Main §2.3 and the
quasilocal summaries: the depth-two factorization, the two layer groups, and the norm-continuous
path of local `*`-automorphisms from the identity to the update's Heisenberg action
(`driveQ_isContinuousPath`, `driveQ_one_eq_heisQ`), stated as a path, with no one-parameter-group
law for the composite established, no generator exhibited and CT3 open; guard `R7-CTN`. The minimal repertoire is propagated
under §A.35: GR §3.3
states phase-free richness as the second primitive-source principle with the elementary repertoire
as its stronger form and `OIPlusMin` boxed, Main §3.4, the Explainer and the book chapters carry the
summary, the registry records the supersessions of `carrier_general_oiPlusPos`, `oiPlusPos_iff_qm`,
`hControl_star` and `typed_determined_of_oiPlusPos` by their phase-free successors, and
`OIBridge/TypedPositive.lean` supplies `typed_determined_of_oiPlusMin`, one result printing only
`propext`, `Classical.choice`, `Quot.sound`. The cycle claim in the manuscripts is stated at its
evidence, the even-carrier countercontrol cited and no minimality of the driven transition asserted.
Guard `R7-MSP` pins the propagated statements in sources and generated forms and the presence of
the census in the gate.

`audit-census.json` and `verification/lean/audit_census_probe.py` make the negative findings of an
audit reproducible: every vocabulary searched, its pattern, the files and counts it hits, its
disposition and the reason, re-run on every CI pass and failing on drift. The manifest carries its
own operating rule — re-read and re-decide on drift, update `expect` in the same commit as the text
change, never widen a pattern to make a mismatch disappear — and the probe checks the rule is still
there.

Not claimed anywhere in the tree: that OI derives quantum mechanics; that any completion
condition follows from OI; the unequal-environment form of purifier uniqueness; the general
orbit theorem, the closed-subgroup theorem, or anything about non-compact groups; that the
Lie-rank condition is necessary for exact reachability.

## Running the checks

    # zero-import layer
    cd verification/lean
    for f in OI_*.lean; do lean "$f"; done
    python3 edge_rigidity_probe.py      # R-series, including the R7 lint of OIBridge
    python3 bohr_frequency_probe.py     # F-series

    # Mathlib programme
    cd verification/lean-mathlib
    lake exe cache get && lake build    # every module; #print axioms lines in the log

    # release gate, from the repository root
    python3 tools/release_gate.py       # toolchain, staleness, voice, claims, mirror,
                                        # citation, architecture, coverage, lean-axioms, ...

`.github/workflows/verify.yml` runs the zero-import kernel check, the Mathlib build, and the
probes as three independent jobs on every change under `verification/`.
