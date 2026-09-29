# A45 — full-equivalence closure (disposable research, L41-based)

Base: L41 = `fa6ddf77703a8ce7f9eaf573ef48355194d72541`. Branch `claude/a45-full-equivalence-closure-research`. Not a
native round: no `F`, no receipt, no pull request, no claim about any landed verdict. Sections 0–2 are written before any
result of this thread and are not edited afterwards; results go in later sections, deviations are recorded there.

## 0. Goal and dependencies

**Goal.** Determine whether all admissible static realizations identified by the current Track-B geometry induce the
same operational object, or exhibit the first certified operational obstruction.

**Dependencies, fixed at the outset.**

- **A44 (operational bridge) is the primary dependency.** Closure needs either a certified map from static realizations
  to the operational object, or a theorem that the operational construction factors through a quotient already known to
  identify the realizations.
- **A43 (family generalization) is potentially helpful, not blocking.** It bears on the shape of the full static quotient
  and on whether Diţă status is intrinsic under all isometries of the normalized set; an abstract invariance argument can
  bypass a complete classification.
- **A42 (support minimality) is non-blocking unless it reveals a new equivalence invariant.** The least support of a
  non-Diţă straight line does not bear on whether operational data collapse the static distinctions.
- **A41 is the foundation**: its corrected semantics (partition structure, alignment, factorization class, partition
  orbit) are the static vocabulary here. Pre-L41 threads (A42–A44) are sources of candidates and algorithms, not evidence.

## 1. What the corpus already fixes (read at L41; K = kernel, P = prose)

- **The open target is definitional.** `ROADMAP.md` (programme interpretation boundary) states the fork: the residual
  lift freedom is physically redundant, or additional structure selects one quantum history, or observational
  incompleteness determines only an equivalence class of quantum histories; a physics-beyond-QM claim needs a residual
  "not removed by the physically appropriate equivalence relation". Act 14's preregistration (P) records that until that
  relation "is written down as an object, 'the freedom is gauge' and 'the freedom is physical' are not statements with
  truth values"; act 14 freezes four carriers `𝒪₀`–`𝒪₃` and adopts none.
- **The Q_fb operational datum depends on visible data only, by definition** (K, `QuantumRepresentation.lean`):
  `QfbData.born b b' := ‖U b' b‖²`, and `bornPow`, `jointMass`, `rooted` and `QStar` are built from `born`, `init`
  and `read` alone. No congruence lemma is stated.
- **Every admissible static realization has the same visible slice.** At the product configuration every flat unitary
  `H` gives an admissible dilation `pad H` of `Γ₀ ⊗ Γ₀ = J/16` (K, `a35_shared_gram_realizable`), and every act-9
  admissible readback returns that slice (K, `rb3_of_admissible`; A44's I4).
- **The lift-level classes are separated by a frozen carrier.** `twoSided_slice_iff` (K, `TwoSidedGauge.lean:826`)
  identifies the two-sided relation with `GramPhaseEquiv`; A44 (pre-L41) found `𝒪₁` (`AnchoredChannel`) and the Gram
  class detect Diţă status on act 39's family only by completeness (they resolve the whole two-sided class), and every
  coarser named invariant blind.
- **No certified static→operational functor.** No kernel theorem builds `QfbData`, a rooted realization, a Q\* family or
  a `FiniteOperationalTheory` from a Track-B `H`, `pad H`, admissible dilation or coherent lift (A44's Finding N;
  confirmed at L41 by inventory). The operational uniqueness theorems (`quasilocal_characterization`,
  `sameData_unitary_or_transpose`) take operational data or quasilocal systems as input, not Track-B realizations.

## 2. The three questions, with decision rules fixed in advance

**Q1 — the target relation.** Write down, for each certified operational object `𝒪` defined in the corpus, (a) its
input type, (b) whether a certified map sends an admissible static realization into that input type, (c) the relation
`~_𝒪` it induces on static realizations. Classify each as:
- *visible*: `𝒪` is a function of the visible data (slice, Born weights, `init`, `read`);
- *lift-level*: `𝒪` is defined on the realization or its dilation and depends on more than the visible data;
- *not applicable*: its input type receives no certified map from a static realization.
The target of Q2/Q3 is stated per class, never as one unqualified "operational equivalence". The strongest statement the
thread could need is the relation of the strongest *applicable* `𝒪` the corpus certifies as operational; if the corpus
certifies none as the physical observable (act 14), that absence is the Q1 finding.

**Q2 — factorization.** For a class of `𝒪`, `FACTORS` iff there is a proof (kernel, written, or exact over the whole
domain) that `𝒪 ∘ (realization ↦ input)` is constant on a quotient that identifies every admissible static
realization of the Track-B geometry (all flat unitaries at the product configuration, and the families through SIG
studied by acts 34–41). Any map into `𝒪`'s input type that the corpus does not certify is named and every verdict is
conditional on it (assumption-watch **AW-static**, carried from A44).

**Q3 — obstruction.** For a class where Q2 does not close, `OBSTRUCTION` iff two admissible static realizations,
statically distinct in A41's semantics (different Diţă status, factorization class or two-sided class), are exhibited
with exactly different values of an applicable, certified `𝒪`. `COLLISION` evidence (equal values across a static
distinction) supports equivalence for that `𝒪` only. Non-constancy is not separation of the relevant classes; one
exhibited pair decides, never a proof of existence alone.

**Interpretation, fixed in advance.** An obstruction for a lift-level carrier is a statement about that carrier, not a
physical distinction, unless the corpus certifies the carrier as observable. A factorization for visible carriers is a
statement that those carriers cannot see the static geometry, not that the geometry is unphysical.

**Controls.** Every Q2/Q3 verdict is void unless: a visible carrier (`𝒪₀`) comes out FACTORS on the full domain; a
carrier known to resolve the two-sided class (`FibreGram`) comes out OBSTRUCTION with an exhibited pair; a toy carrier
that varies but is not class-determined (a single matrix entry) is not mistaken for either; A41's census classifier
reproduces its landed values on any point it is applied to.

**Working hypothesis (to be tested, not assumed).** Because every admissible static realization shares its visible
slice, every *visible* `𝒪` factors trivially; the full-equivalence question then reduces exactly to act 14's open
choice of relation among the *lift-level* carriers, where A44 found separation by completeness. If so, A44's missing
static→multi-time map is load-bearing only for the *not-applicable* carriers, and the shortest closure route is a
certified argument that the physically appropriate relation is visible-level — or else a certified reason it is not.

***

Everything below was written after the Q1 inventory and probe ran.

## 3. Q1 — the classification

**Method.** Two read-only sweeps of L41 (the Track-B carriers of acts 7–41, and the operational-theory objects), every
row tied to a definition and to the corpus's own status sentence; the adoption quotes the conclusion rests on were
re-read verbatim at L41. The exact probe `q1_probe.py` (output `q1_probe.json`) evaluates every carrier applicable to a
single dilation on five admissible realizations sharing the visible slice `J/16`: `SIG`, a two-sided gauge transform of
`SIG`, a relabelling of `SIG`, the Diţă face point `H3(1, v₂, v₃)` and the non-Diţă point `SIG ∘ v^{E40}` (A42).
**Controls (all green):** `𝒪₀` equal on all five; `featureVec` and `𝒪₁` each lift-dependent with an exhibited pair
(neither is labelled visible because the slice is fixed); raw `FibreGram` lift-dependent; a single matrix entry
representative-level, not class-level.

**Classes (as refined by the owner).** *V-sourced*: visible-determined and instantiated from a Track-B static
realization by a landed theorem. *V-bridge*: visible-determined (its value is a function of the visible law / Born
moduli / `init` / `read`), but no landed map from a Track-B realization into its input. *Lift*: depends on the lift
beyond the visible data (single-time). *Multi*: defined on `ℕ`-indexed lifts or time pairs. *Theory*: defined on
implementation classes, theories, operator algebras or operational data. Status: **Est** established/adopted; **Lic**
licensed input datum; **Pres** recorded presupposition; **Test** named object of test / "coordinate on the lift space";
**Decl** explicitly declined or disqualified; **Add** explicit additional condition. Consequence: **auto** (equal on
all realizations of one visible datum); **relation** (requires the relation choice); **bridge** (would agree if
instantiated; the constructor is missing); **n/a** (no static instance, and not visible-determined).

| object (repo name) | input domain | Track-B static instance (landed map) | dependence | two-sided / A41 invariance | status | consequence |
| --- | --- | --- | --- | --- | --- | --- |
| `𝒪₀` visible slice `readback a₀ (‖U‖²)` (`DilationChoice.lean:86`) | one dilation | yes: `a35_shared_gram_realizable` (`DitaHull.lean:140`) | V-sourced | constant on all flat unitaries (probe; A44 I4) | undisputed, not adopted (act 14 prereg:191-196); Γ is the licensed datum (act 17 prereg:507) | **auto** |
| act-9 admissible readback `R.map` (`ReadbackRobustness.lean:95,120`) | real matrix over any ancilla | yes, by specialisation of `rb3_of_admissible` (`:199`) | V-sourced | equals `𝒪₀` on `‖unitary‖²` | extension of `𝒪₀`'s rule, not a new observable (act 7 readback amendment:135) | **auto** |
| `IsUnistochastic` of the slice (`BarandesTuple.lean:430`) | real matrix | applicable to `𝒪₀`'s value; no theorem states it | V-sourced (predicate on `𝒪₀`) | constant | branch test, no adoption (act 6 result:108-112) | **auto** |
| `S ⇔ D ⇔ Q_fb`, `finite_horizon_equivalence` (`Equivalence.lean:459`) | a trajectory law | none from a realization; takes the law itself | V-bridge (law) | function of the law | **Est** (`ROADMAP.md:38-42`) | **auto** for lifts of one law (the law is shared by admissibility); no realization→law constructor beyond `𝒪₀` |
| `QfbData.born/bornPow/jointMass/rooted`, `QStar` (`QuantumRepresentation.lean:60-165`) | `(U, init, read)`; `Γ` | none | V-bridge (moduli, `init`, `read`) | equal on all five under the named embedding `U := H/4` (probe) | **Est** as representation, "nothing more" (PROGRAMME:204) | **bridge** |
| `RootedRealization`, `rootedMap`, `PPer`, `C4e/C4r`, `PDivisible` (`CausalReadback.lean`, `RootedClassification.lean`) | bijection + prior; `Γ : ℕ → Matrix` | none | V-bridge (family) / hidden prior | function of `Γ` (and the prior) | `C_OI = PPer` kernel-closed; priors can change the rooted family (PROGRAMME:100-102) | **bridge** |
| `BarandesTuple` (`BarandesTuple.lean:100`) | `Γ` with `PPer`, parameter `p0` | none | V-bridge | function of `Γ`, `p0` | no candidate-selection adopted (PROGRAMME:628) | **bridge** |
| `candidateOf` (`CandidateSelection.lean:60`) | `QfbData` + fibre weight | none | moduli + hidden fibre weight | `admissible_nonUnique` (`:435`) | candidate-selection principle "required… none adopted" (PROGRAMME:258) | **bridge** (and not unique) |
| `FibreGram` (`TwoSidedGauge.lean:95`) | one dilation | yes: step `hG` of `a35_shared_gram_realizable` | Lift, representative-level | moved by the right gauge (`fibreGram_mul_weak_apply`); probe pair R0/R1 | **Test**: "coordinate on the lift space, not a physical quantity" (act 12 prereg:254-255) | **relation** |
| `GramPhaseEquiv` class, cross invariant (`TwoSidedGauge.lean:102,870`) | Gram tuples | yes (`a30_s_strictify`, act 35) | Lift, class-level | two-sided invariant (`twoSided_slice_iff`) | **Test** | **relation** |
| `mixedTriple`, `featureVec`, `dist_featureVec`, product normalized set, act 35 cross coordinates, hull / stratum membership (`OrbitGeometrySelector.lean:79`, `OrbitGeometryRigidity.lean:99,126`, `DitaHull.lean`) | Gram tuples | yes (`a35_control_witness`, `DitaHull.lean:732`; A38/A39) | Lift, class-level | two-sided invariant (`mixedTriple_gauge`, `geo2_twoSided_trivial`); separates Diţă from non-Diţă (probe R3/R4) | **Test**: "named object of test" (act 24 prereg:10-11); "anything but mathematics" (act 35 prereg:11) | **relation** |
| Diţă status, factorization class, partition orbit (A36–A41) | a matrix | yes (A41 census) | Lift, class-level (relaxed status invariant under `D₁ · _ · D₂`) | A41 semantics | mathematics; no isometry or factorization adopted (act 37 prereg:1531) | **relation** |
| `𝒪₁` `AnchoredChannel`, `CrossFibreGram` (`ThreadingObservability.lean:144,158`) | one dilation | not on a flat `H` by a theorem (constant lifts at `Fin 2 × Fin 2` only); computable on `pad H` | Lift, representative-level | moved by non-uniform left and by the right gauge (probe R0/R1; `pq1d_minus`) | **Pres**: "recorded presupposition, not a finding" (`:141-142`) | **relation** |
| `𝒪₂` `RelativeCandidate`, `𝒪₃` `ReanchoredChannel`, relative evolution `U_tU_sᴴ`, `CrossGram`, `FibreCrossGram` | `ℕ`-lift, time pair | none for a single slice; a constant lift gives `U_tU_sᴴ = 1` | Multi | constant-right invariant (`gl3`, `ct1`), moved by time-dependent gauges (`gl2`, `cl1`) | **Pres** / "not adopted… not asserted not to be" (`CancellationFork.lean:121`, `ReanchoredChannelScope.lean:117`); "coordinates on the lift space" (`CrossTimeInvariants.lean:75`) | **n/a** (static) / **relation** (lifts) |
| `CoherentLift`, `GaugeRelated`, `TwoSidedRelated`, `ThreadingRelated`, `GramTrajEquiv`, `SelectsAt`, `PointwiseLaw`, `DeterminesTraj`, `ProperAt`, `PropagatesFrom` | lifts, trajectories, laws | constant lifts of Hadamard pads only | Multi (relations and predicates on lifts) | — | relations, or named objects of test (act 17 prereg:386-388; act 18 prereg:1308-1310) | **n/a** |
| `MovesVisibleCandidate`, `VisibleInvariance`, `PreservesDivergence`, `JointlyReproducingAnchor` | pairs of slices / dilations | none | Lift (pairs) | `VisibleInvariance` refuted (`dc4_refuted_*`) | properties of the convention, not observables | **n/a** |
| `ImplementationClass`, `InstAvail`, `genTheory`, `FiniteOperationalTheory`, `HasCompositeUnitaryControl`, `DenseUnitaryControl`, `IsGenInstrument`, `PhasesAvailable`, `NonnegBounded` | implementation classes, theories | none (`fixedGateTheory` takes an angle, not a Track-B object) | Theory, relative-phase sensitive (`conjChannel K`) | — | **Add**: "operational completion principles remain explicit additional conditions" (`ROADMAP.md:45-46`); not an OI ⇔ QM theorem (milestone audit:16-18) | **n/a** (missing bridge; phase-sensitive) |
| `RepUnitary`, `repAugmented`, `padData`'s `U` (`OperationalSourcing.lean`) | the `U` of a representation | none | Theory / representation, full phases | `repAugmented_allUnitaries` | **Decl**: disqualified (`:930-934`) | **n/a** |
| `QuasilocalSystem`, `OISystem`, `quasilocal_characterization` | C\*-algebra with stages, substratum `Φ` | none | Theory | unique given the stages and `Φ` (`systemEquiv_dyn`) | characterizes; selects no Hilbert representation (PROGRAMME:90) | **n/a** |
| `sameData_unitary_or_transpose`, `OrientationSelection` | operational pairing data | none | Theory (probabilities) | determines up to unitary **or antiunitary** equivalence | theorem; orientation not data-definable (`OrientationSelection.lean:28,43`) | **n/a** |
| `OIPlusMin`, `TypedOperationalTheory`, IndependenceCensus completions, `DerivedOI` (Route B) | theories | none | Theory | `oi_core_underdetermines_completion` (non-uniqueness) | **Add** / census results | **n/a** |

## 4. Q1 — findings

**F1 (the owner's boxed statement, in a stronger form).** Every operational datum the corpus establishes or licenses —
the finite observable-law correspondence `S ⇔ D ⇔ Q_fb` / `QStar` (**Est**) and the visible family `Γ` (**Lic**) — is
visible-determined: its value is a function of the Born moduli, `init`, `read`, or of `Γ` itself. So "adopted ⇒
visible-determined" holds outright; the disjunct "or lacks a certified map" is needed only for objects that are
*not* adopted. Evidence: definitions (K), the adoption sentences quoted above (P, verbatim at L41), and the probe (X).

**F2 (the adopted layer is automatic on Track-B realizations).** The adopted layer takes the visible law as its input,
and every admissible static realization of the Track-B geometry is an admissible dilation of the same slice
(`a35_shared_gram_realizable`), with every admissible readback returning it (`rb3_of_admissible`). On it, equivalence is
immediate: case 1 (V-sourced) for `𝒪₀` and the readbacks; for the representation-level objects (`QfbData`, rooted
families) the value would agree if instantiated (probe, named embedding), but no Track-B→`QfbData` constructor is landed
— case 2 (V-bridge). The missing constructor is a representation bridge, not a source of distinctions: whatever `U`
it chose, `born` sees only moduli.

**F3 (every lift-sensitive separator is unadopted).** Every carrier that separates static realizations sharing the
visible slice — `FibreGram`, the Gram class and its invariants, `featureVec`, the normalized-set geometry, Diţă status
and A41's classes, `𝒪₁` — is recorded as a coordinate on the lift space, a named object of test, mathematics, or a
recorded presupposition, and act 14 forbids reporting any of `𝒪₀`–`𝒪₃` as, or as not, the physically appropriate
relation (prereg:588-590). The multi-time carriers (`𝒪₂`, `𝒪₃`, the relative evolution) have no single-slice instance.

**F4 (the only other channel is theory-level, and it is an explicit additional condition).** The corpus's
relative-phase-sensitive operational objects are theory-level: implementation availability through `conjChannel K`,
composite and dense unitary control, `PhasesAvailable`. These are where lift-level (phase) content could become
operational. They are explicit additional conditions (`ROADMAP.md:45-46`), not established; `repAugmented` is
disqualified; and no landed map sends a Track-B realization into an implementation class or theory. Any route by which
Diţă status or the two-sided class became operationally meaningful must pass either through adopting a lift-level
carrier (act 14's open choice) or through a theory-level completion principle together with a static→theory bridge
that the corpus does not contain.

**F5 (the reduction is already recorded, and not decided).** Act 14 states, and declines to act on, the consequence of
adopting the visible carrier: "every coherent lift of one visible family is `≈_{𝒪₀}`-equivalent to every other … and
dissolves the whole of `P0`" (prereg:191-196). A45's Q1 adds the completeness of the inventory behind that sentence:
nothing adopted escapes it, and the only non-visible operational content is the unadopted lift carriers and the
additional theory-level completion principles.

**The reduced question.** With F1–F5, full equivalence over Track-B static realizations reduces to:

> Which lift-level distinctions — carried by the unadopted lift carriers, or made operational by a theory-level
> completion principle through a static→theory bridge — are part of the intended operational theory?

Under the visible relation the answer to the full-equivalence question is yes, automatically (F2). Under any relation
that includes a lift-level carrier it is no, with exhibited separations (probe; A44). The bottleneck is act 14's
unresolved relation, and on the theory side the status of the completion principles — not A42's or A43's geometry.

**Q1 verdict.** The owner's boxed statement holds, in the stronger form F1. Scope: the corpus at L41, the objects
inventoried in §3 (every carrier, readback, law, representation and theory object the two sweeps found), static
realizations at the product configuration. Evidence: K (definitions and theorems cited), P (status sentences, verbatim),
X (the probe). Not established: that no future carrier could be adopted that escapes the dichotomy — that is the
content of the open relation choice, not a gap in the inventory.
