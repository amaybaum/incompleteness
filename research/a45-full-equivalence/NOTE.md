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

***

## 5. Q2 — what any justified relation must satisfy (framework)

Q2 does not choose the physically correct relation. It fixes necessary criteria, places the candidate relations
against them, and derives the consequences conditionally. The six tests are the owner's, stated before any Q2
computation; the exact probe `q2_probe.py` (output `q2_probe.json`) ran before this section was written.

**Tests.** (T1) *sourcing* — every datum the relation uses is produced by a landed map from the operational theory or
from a Track-B realization, and no relation distinguishes objects by a coordinate the theory never exposes;
(T2) *representation independence* — transformations already treated as representational redundancy are identified;
(T3) *operational extensionality* — agreement on every adopted experiment and intervention forces equivalence unless an
explicit additional principle is named; (T4) *composition/intervention stability* — equivalence survives every licensed
composite and intervention; (T5) *non-circularity* — a lift-sensitive carrier is not made physical by the distinctions
under investigation; (T6) *minimality* — prefer the coarsest relation preserving all adopted structure.

**The licensed interventions.** The corpus's stated access is `permClass`, i.e. `IsScaledPartialPerm`
(`OperationalSourcing.lean:160`), and relative-phase control carries the settled *Additional* verdict, stable against
the whole Arc C layer (`PROGRAMME.md` §3.12). Every licensed intervention is therefore monomial.

**Candidate relations** on admissible static realizations `H` (flat unitaries at the product configuration, trivial
ancilla), ordered from coarsest to finest:

- `R₀` visible: `H ~ H'` iff equal visible slice (and hence equal Born moduli). On Track-B realizations of one slice,
  everything is identified.
- `R_cls` class-level: equal two-sided class (`GramPhaseEquiv`; `featureVec`; Diţă status and A41's classes are functions
  of it).
- `R_rd` right-diagonal: `H' = H D`, `D` diagonal unitary.
- `R_ph` global phase: `H' = c H`. At the trivial ancilla this is exactly the relation of `𝒪₁` (A44's I5: `𝒪₁(pad H)`
  determines `H` up to one phase).

`R₀ ⊋ R_cls ⊋ R_rd ⊋ R_ph` (each strictly finer; probe pairs and the definitions).

## 6. Q2 — results

**P1 (monomial interventions preserve `R₀`).** If every row of `M` and every column of `N` has at most one nonzero
entry, then `|M H N|²` is a function of `|H|²`: each entry of `M H N` is a single product `m·h·n`. So `R₀` is stable
under the whole stated access. **P** (one line) and **X** (S1: permutation×diagonal and scaled partial permutations,
slices equal on all five realizations).

**P2 (the dividing line for a left intervention `K`).** If every row of `K` has at most one nonzero entry, `R₀` is
`K`-stable (P1). If some row `i` of `K` has two nonzero entries, then for every flat `H` there is a diagonal unitary `D`
with `|K D H|² ≠ |K H|²`. *Proof.* Fix a column `j`; `(K D H)_{ij} = Σ_c k_{ic} d_c H_{cj}` has at least two nonzero terms
since every `H_{cj} ≠ 0`. Write it as `α d_a + β` with `α = k_{ia} H_{aj} ≠ 0`; choose the other `d_c` so that `β ≠ 0`
(one nonzero term, or generic phases when there are several); then `|α d_a + β|²` is non-constant on the unit circle. ∎
**P**, and **X** (S2: `K = F4(i) ⊗ I₄` and `K = SIGᴴ` separate all ten pairs, including the two-sided-equivalent pair
`SIG` / `D₁ SIG D₂` and the Diţă / non-Diţă pair). The right-hand analogue holds with columns and right diagonals.

**P3 (what coherent interventions generate).** If `|K H|² = |K H'|²` for every unitary `K`, then `H' = H D`: taking `K`
with first row `x̄` shows `|⟨x, h_j⟩| = |⟨x, h'_j⟩|` for every unit `x`, so each column `h'_j` lies on the ray of `h_j`.
The converse is immediate. So all left coherent interventions generate exactly `R_rd`, and interventions on both sides
generate `R_ph`. **P**, **X** (S3: right-diagonal moves invisible under `K`, left-diagonal moves separated).

**P4 (the class-level relations are never the stable relation).** `R_cls` — and with it Diţă status, A41's
factorization classes and partition orbits, and `featureVec` — is not the coarsest relation stable under either regime.
Under monomial access it is strictly finer than the stable `R₀` (T6, T3). Under any access containing a row-non-monomial
`K` it is not stable (P2 with `H' = D H` two-sided-equivalent to `H`). **P** from P1–P3; **X** (S2).

### The six tests, per relation

| test | `R₀` visible | `R_cls` class-level | `R_rd` / `R_ph` (coherent completion `R_T`) |
| --- | --- | --- | --- |
| T1 sourcing | passes: `𝒪₀` via `a35_shared_gram_realizable`; `Γ` licensed | sourced from the realization (`FibreGram`, `featureVec`), exposed by no adopted operational object — fails the second clause | needs the realization composed with a non-monomial intervention; no landed map makes a static realization a composable operation — **missing bridge** |
| T2 representation independence | passes for every candidate redundancy (invariant under everything preserving the slice) | passes for global phase and the two-sided gauge | separates left- (and right-) diagonal moves: passes only if those are not redundancy — **undecided** in the corpus (act 14 uses no gauge verdict) |
| T3 extensionality | passes: the adopted experiments are visible (F1) | fails without a named additional principle | passes only as an explicit extension (it adds experiments) |
| T4 stability, stated access | passes (P1) | passes (finer relations are trivially stable) | passes |
| T4 stability, with a row-non-monomial intervention | **fails** (P2) | **fails** (P2, P4) | `R_rd` passes for left interventions, `R_ph` for both (P3) |
| T5 non-circularity | passes (the framework's own admissibility condition) | fails: its objects were introduced to classify the lift geometry under test | independent motivation exists (standard coherent control; `𝒪₁`'s presupposition is the reduced density operator), as an additional principle |
| T6 minimality | passes: coarsest relation preserving the adopted structure | fails | fails under current adoption; passes relative to an adopted completion |

### Conditional theorems

- **Q2-A (visible factorization).** If a relation `R` factors through the visible data (slice, Born moduli, `init`,
  `read`), all admissible static realizations of one visible slice are `R`-equivalent, and remain so after any
  intervention in the stated access. **P** (definitions + P1), **X** (S1, S4).
- **Q2-B (lift retention).** If `R` refines any certified lift separator (`FibreGram`, the Gram class and invariants,
  `featureVec`, Diţă status, `𝒪₁`), full Track-B equivalence fails, with exhibited pairs (Q1 probe; A44). **X**, **K**.
- **Q2-C (intervention dichotomy).** For a licensed left intervention `K`: `R₀` is `K`-stable iff every row of `K` has at
  most one nonzero entry (on flat realizations). **P** (P1, P2), **X**.
- **Q2-D (no class-level stable relation).** No relation between `R₀` and `R_rd` that retains the two-sided class is the
  coarsest relation stable under an access containing a row-non-monomial intervention; and under monomial access `R₀`
  is. **P** (P1–P4).

### What follows, and its scope

1. **The strongest outcome the owner asked for holds, relative to the Q1 inventory.** Any relation finer than visible
   equivalence on Track-B static realizations requires at least one unadopted assumption: *either* a lift carrier is
   declared observable (failing T1's second clause, T3, T5 and T6 under current adoption), *or* a completion principle
   licenses a row-non-monomial intervention (currently *Additional*) **together with** a bridge that makes a static
   realization a composable operation (not in the corpus). The adopted layer is visible (F1) and the stated access is
   monomial, so by Q2-C no adopted intervention can refine `R₀`.
2. **Closure, in the wording the constructor's absence requires.** *Conditional on instantiating the established
   visible operational correspondence for a Track-B realization, its result — and its result after any intervention in
   the stated access — is independent of the static realization within one visible slice.* The instantiation is a
   small bridge: `ι(H) := QfbData` with `U := H/4` (or `pad H`), any `init`, `read`; `IsLaw` holds for a unitary `U`,
   and `rooted (ι H)` is a function of `|H|`, `init`, `read`. Kernel-feasible: a congruence lemma for `born` plus the
   flatness `|H_{ij}| = 1/4`.
3. **Failure of equivalence occurs only in explicitly stronger extensions**, and P3–P4 fix what those extensions
   distinguish: a coherent-completion extension does not land on the static geometry the Track-B rounds studied. It
   lands on `R_rd` or `R_ph`, which separate even two-sided-equivalent realizations; the Diţă / A41 distinctions are
   neither needed (monomial access) nor stable (coherent access).
4. **Scope.** Static realizations at the product configuration with trivial ancilla (assumption-watch **AW-|A|=1**:
   at `|A| > 1` the left group is `∏ U(A)` and P2–P3 need restating); the corpus at L41; "licensed" means the stated
   access. Nothing here adopts a relation, a carrier or a principle.

**Q3, as it now stands.** A small run: act 14's four carriers on selected A41 pairs (two-sided-equivalent,
Diţă / non-Diţă, relabelled), each through the six tests. Expected, from Q1–Q2: `𝒪₀` applicable and identical;
`𝒪₁` applicable (computable on `pad H`), separating at `R_ph`, presuppositional; `𝒪₂`, `𝒪₃` not applicable to a single
slice (no certified static instantiation), and trivial on the constant lift (`U_t U_sᴴ = 1`).

## 7. The bridge lemma (kernel)

`TrackBQfbBridge.lean` (this directory). It was built as `verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean` on the
disposable branch `claude/a45-bridge-dev` @ `68cf4596` (never landed), in run 36596287670, Mathlib bridge job 109501934929.
That run is design evidence, not an attestation. Build OK; `lean-axioms` OK with 5270 named results (5251 at L41, plus
19) and no `sorry`; every theorem of the module depends on `[propext, Classical.choice, Quot.sound]` only. The gate's
only red step is `lean-manuscript`, because the new module has no census disposition; that is expected on a dev branch.
The first build (run 36595682134, `fa26d6a3`) failed on two rewrites of `born` across the dependent field `Bas`. The
repair states those two steps on the visible carrier; no statement changed.

| owner item | theorem | statement |
| --- | --- | --- |
| 1 unitary construction | `UH_unitary` | `IsFlatHadamard H` (unimodular entries, `H Hᴴ = 16`) ⇒ `U_H := H/4 ∈ U(16)`; `UH_norm`: `‖U_H i j‖ = 1/4` |
| 2 Born identification | `UH_born_eq_slice`, `UH_admissible` | `born(U_H) b b' = 1/16 = (Γ₀ ⊗ Γ₀)`; `pad U_H` is an admissible dilation of `Γ₀ ⊗ Γ₀` (via `a35_shared_pad_unitary`) |
| 3 constructor | `realData`, `realData_isLaw`, `realData_positiveRootMass`, `realData_qstar` | `QfbData` with `U`, and `hadData`'s `init` (uniform) and `read` (`id`); no new field. Unitary `U` ⇒ lawful, positive root mass, a member of `Q*` |
| 4 visible congruence | `slice_of_admissible`, `visible_congr` | two trivial-ancilla admissible dilations of one slice `G` ⇒ equal `born`, equal `rooted` for all `t a j` |
| 5 licensed-intervention congruence | `normSq_mul_mul_congr`, `bridge`, `flat_bridge` | `M, N ∈ permClass` ⇒ `‖(M U N) i j‖² = ‖(M U' N) i j‖²` and equal `rooted` of `realData (M U N)` |

**The target theorem, as proved** (`bridge`, general finite `V`; `flat_bridge` at `Fin 4 × Fin 4` for flat Hadamards):
if `pad U` and `pad U'` are admissible dilations of the same visible slice `G`, then for all `M, N ∈ permClass` the
instantiated data `realData (M U N)` and `realData (M U' N)` have equal Born weights and equal rooted families. Only
this direction is proved; nothing here asserts a converse.

**Scope, and what is not proved.**
- The realizations are trivial-ancilla (`Fin 1 × Fin 1`) dilations (AW-|A|=1 stands).
- "Licensed" means `permClass`, the stated access. A row-non-monomial intervention is outside the hypotheses, and Q2's
  P2 shows the conclusion fails there.
- `realData` is a constructor this thread supplies. It reuses the corpus datum and adds no field, but no landed theorem
  names it as the map from Track-B realizations to `Q_fb`; AW-static therefore persists as "the instantiation is
  `realData`". The congruence holds for any `init` and `read` shared by the two data: the proof uses only `born`.
- In the flat case the Born weights are constant, so `flat_bridge` is immediate once items 1–2 hold. The content that
  generalizes is `bridge`, for an arbitrary slice `G`.

## 8. Q3 — regression / countercontrol suite

`q3_suite.py` (output `q3_suite.json`); exact Gaussian-rational arithmetic, run locally after the bridge built (18 s).
Every expected cell was fixed in the script's `EXPECT` table before any carrier was evaluated. Realizations: Q1's R0–R4,
plus `R5 = i·SIG` (an `R_ph` pair with R0) and `R6 = SIG·D` (in `R_rd`, not in `R_ph`); 21 pairs. Off-slice
countercontrol `X = F4(1)/2 ⊗ I4`.

| cell | expected | measured |
| --- | --- | --- |
| `𝒪₀` equal on every pair | 21/21 | 21/21 |
| `𝒪₀` separates off-slice `X` | yes | yes |
| `𝒪₁` (`H E_kl Hᴴ` for all `k, l`) equal exactly on the `R_ph` pair (R0, R5) | 1/21 | 1/21, on (R0, R5) |
| `𝒪₂`, `𝒪₃` applicable to a single slice | no | no (by definition: both take a time pair) |
| constant lift: `U_t U_sᴴ = 1` on every realization | yes | yes |
| B1 `rooted` (bridge instantiation, `t ≤ 3`) equal on every pair | 21/21 | 21/21 |
| B2 `rooted` after three monomial `(M, N)`, perm×diag and scaled partial perm | 21/21 | 21/21 |
| B3 row-non-monomial `K = F4(i) ⊗ I4` separates some pair | yes | yes |
| all realizations flat unitary; `X` unitary, off slice | yes | yes |

**Verdict: all cells match.** The `𝒪₂`/`𝒪₃` applicability cell is definitional, not measured. The constant-lift cell is
the only computed content for those carriers. `𝒪₁` separates the two-sided-equivalent pair (R0, R1), the
right-diagonal pair (R0, R6) and the Diţă / non-Diţă pair (R3, R4), and identifies only the global phase. It therefore
resolves `R_ph`, a relation finer than every class-level relation, and is not stable under the class structure.
Together with B3 (and Q2's S2, where `K` separates R0/R1), class-level distinctions define neither the stable relation
under monomial access (B1, B2: nothing is separated) nor under coherent access (everything down to `R_ph` is).

## 9. Kernel additions after Q3: converse, trajectory laws, the landed equivalence

Two more design-evidence builds on `claude/a45-bridge-dev`: `a77a7dfd` (run 36598896118, job 109510848797) and
`8863c9c9` (run 36599732472, job 109513725393). Each built with no `sorry`; `lean-axioms` reports 5274 and then 5277
named results. Every theorem of the module depends on `[propext, Classical.choice, Quot.sound]` only, and
`lean-manuscript` is again the only red gate step.

- **Converse at the realization level.** `realData_rooted_one`: with identity readout and uniform initial law,
  `rooted 1 a j = ‖U j a‖²`. Hence `slice_eq_of_rooted_eq` (equal rooted families ⇒ equal Born weights), and
  `rooted_eq_iff_slice_eq`: for trivial-ancilla admissible dilations of `G` and `G'`, the instantiated rooted families
  agree iff `G = G'`. The forward direction's witness is `slice_eq_of_rooted_eq` and the backward one's is
  `visible_congr` (§A.34). On these realizations the relation induced by the instantiated data is exactly `R₀`.
- **Trajectory laws.** `rootTraj_congr` and `bridge_traj`: the root-conditioned trajectory laws `rootTraj K a`, the
  objects `finite_horizon_equivalence` is stated for, agree at every horizon under the hypotheses of `bridge`.
- **Track-B → `Q_fb` → `S`.** `realData_traj_stochastic`: for unitary `U`, each `rootTraj K a` of `realData U` is
  `QfbRealizable` (the landed `qfbRealizable_rootTraj`) and `Stochastic` (the landed `Qfb_imp_S`). No new
  construction enters; the realization's laws enter the landed `S ↔ D ↔ Q_fb` equivalence
  (`finite_horizon_equivalence`, `Equivalence.lean:459`).

**What the converse settles, and what it does not.** Class-level injectivity (same `Q_fb` data ⇒ same Track-B class) is
false, not merely unproved. R3 (Diţă) and R4 (non-Diţă) are admissible flat realizations of one slice. So by
`rooted_eq_iff_slice_eq` they have equal instantiated data (Q3 B1 exhibits it exactly), while their A41 classes
differ. The representational equivalence `S ↔ D ↔ Q_fb` does not need that injectivity: it relates laws, and its
`S → D → Q_fb` direction builds its own datum (`D_imp_Qfb`'s permutation unitary), not a Track-B realization.

## 10. Ancilla probe

`q4_ancilla.py` (output `q4_ancilla.json`), exact rational arithmetic. Every verdict cell was fixed in `EXPECT` before
evaluation. Visible `V` has 4 values, the ancilla `{a₀, a₁}`, the slice `G = J/4`. The dilations have fixed
`(·, a₀)` columns (a real Hadamard `F` split across the ancilla at angles `φ_i`) and a completion `(·, a₁)` equal to
`W` applied to the orthonormal complement.

| cell | expected | measured |
| --- | --- | --- |
| all five dilations unitary and admissible for `G` | yes | yes |
| CARRIED (basis `V × A`, evolution `U`, `init (i, a₀) = 1/4`, `read = fst`): `t = 1` rooted family `= G` | yes | yes |
| CARRIED `t = 2` differs, D1 (`φ` varying, `W = 1`) vs D2 (`φ` varying, `W = Fᵀ/2`) | yes | yes: first row uniform `1/4` vs `(17187, 6371, 23271, 20771)/67600` |
| CARRIED `t = 2` equal, D3 vs D4 (`φ` constant) | yes | yes |
| REFRESHED (ancilla reset to `a₀` each step; kernel `G`) equal on all five | yes | yes (by construction: a control, not a finding) |

A descriptive check was added after the verdict cells: D1 and D2 share every `(·, a₀)` column and differ only in the
completion. The `t = 2` separation therefore depends on data that no quantity built from the `(·, a₀)` columns sees:
not the slice, and not the fibre Gram at `a₀`. The corpus's own ancilla construction, `padData` (a product `Q.U ⊗ W`),
is proved invisible to the rooted family (`OperationalSourcing.lean`, S1); the separation needs a non-product
dilation with the ancilla carried between steps.

## 11. Closure assessment

**Proved (kernel, design evidence; trivial-ancilla admissible realizations; `realData`).** Same visible slice ⇒ equal
Born weights, rooted families and trajectory laws, before and after any `permClass` interventions on either side
(`bridge`, `bridge_traj`). Conversely, equal rooted families ⇒ same slice (`rooted_eq_iff_slice_eq`). The laws are
`Q_fb`-realizable and stochastic via the landed `qfbRealizable_rootTraj` and `Qfb_imp_S`, and so enter the landed
`S ↔ D ↔ Q_fb`. On this domain the relation the adopted operational data induce on Track-B realizations is exactly
`R₀`.

**The two scope questions that remain.**

1. **Instantiation.** No landed theorem names a map from Track-B realizations to `Q_fb`, so `realData` is this
   thread's definition. It adds no field and takes `init`/`read` from `hadData`. What the congruence proofs use from
   it is the evolution `U` and the fact that the two data share `init` and `read`. A version quantified over arbitrary
   shared `init`/`read` is a mechanical generalization, not yet in the kernel. Closing this is a decision to freeze
   the definition "the `Q_fb` evolution of a trivial-ancilla realization is its unitary", not a theorem to find.
2. **Ancilla.** At `|A| > 1` the outcome depends on the semantics, as §10 shows. With the ancilla carried as hidden
   basis states, which is what `Q_fb`'s non-injective `read` allows, the `t ≥ 2` law is not slice-determined.
   Exhibited: equal slice, equal `(·, a₀)` columns, different `t = 2` law. With the ancilla refreshed each step, the
   law is `G^t` and visible. So either the theorem is stated for trivial-ancilla realizations, or a `|A| > 1`
   realization's `Q_fb` semantics is fixed as the refreshed one. The carried semantics is a multi-time structure (a
   coherent ancilla history), the territory of the unadopted `𝒪₂`/`𝒪₃`.

**Not needed, and false at class level.** A converse from `Q_fb` data to the Track-B class does not hold (§9). No
reconstruction programme follows from it.

**Two-layer result, as it now stands.**
- *Current theory* (adopted objects, stated access, trivial ancilla, `realData`): the relation Track-B realizations
  induce through the adopted operational data is `R₀`, and it is stable under every licensed intervention.
- *Extensions:* a coherent (row-non-monomial) intervention, a lift-level carrier declared observable, or a carried
  ancilla each refine it: to `R_rd`/`R_ph` (P3), to the carrier's own relation (Q1), or to completion-sensitive data
  (§10). Each needs an additional, currently unadopted principle. None lands on A41's class geometry (P4).

## 12. Scope for a freeze (owner decisions after §11; no `F` yet)

1. **Instantiation:** `realData` as built — trivial ancilla, uniform initial law, identity readout. The generalization
   to arbitrary shared `init`/`read` is not added before `F`; it would enlarge the claim surface without strengthening
   the conclusion, and can be a later corollary.
2. **Level of the claim:** trajectory laws — `bridge_traj`, `realData_traj_stochastic`, and the landed
   `finite_horizon_equivalence` (`S ↔ D ↔ Q_fb`). No separate reconstruction of `S` from Track-B is claimed or needed.
3. **No class reconstruction.** `rooted_eq_iff_slice_eq` identifies the induced relation with `R₀`; R3/R4 witness that
   A41's classes are not recovered. The collision states which quotient the equivalence lives on.
4. **Larger ancillas, a scope note only:** product padding (`padData`) is invisible (landed); a refreshed ancilla gives
   `G^t` (compatible; a possible later generalization); a carried ancilla is excluded by §10's exact counterexample and
   belongs to the unadopted higher-history semantics.

Landing the module would also require its census disposition in `verification/lean-manuscript-census.json`
(`lean-manuscript`, §A.35), which is the only red gate step on the dev builds.
