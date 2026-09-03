# Verification suite

Machine-checked certificates for the finite and algebraic core of the OI papers, in three
layers:

- **`lean/`** — six self-contained **Lean 4 proof files** (zero dependencies: no Mathlib, no
  lake project) for the lattice, gauge-counting and staggered-fermion statements of `papers/SM.md`
  and `papers/GR.md`, with **numerical probes** (Python 3) that instantiate every hypothesis and
  conclusion on the concrete operators, exactly in integer or rational arithmetic wherever the
  statements are integer identities.
- **`lean-mathlib/`** — `OIBridge`, the Mathlib-based formal verification programme: 90 modules and,
  at this commit, 1,650 named results, each printing its axiom dependencies (`propext`, `Classical.choice`,
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
carrier (`carrier_general_oiPlusMicro`). Whether the inverse clause is already forced by the other
principles is not settled in either direction. The Lie-rank clause is derived from elementary
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
  explicit finite data — `bohr_frequency_probe.py` carries the F-series (F1–F70, one per
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
  `CompletedOI`, `CarrierGeneralOIPlus`, `EmbeddedObservation`, `ImplementationLocality`, `MicroscopicReversibility`, `LieRankSource`): the five completion conditions defined one by one with the countermodel
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
reachability routes kernel-internal within their stated hypotheses. The programme is
publication-frozen at this state.

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
