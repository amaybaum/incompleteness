# LEDGER — the remaining OI–QM equivalence obligations (node E1, updated by every later node)

**Base.** L = `9f9f8257` (the thread checkpoint `4dc0321c` adds `research/archive/` only). Every `file:line` is at L,
paths under `verification/lean-mathlib/OIBridge/` unless stated; ROADMAP lines are `verification/ROADMAP.md` at L.
Research only: nothing here changes a status at L, proposes manuscript text, or is a round.

**Labels** (charter): CERTIFIED [K at L, file:line] — a kernel theorem at L, quoted where a status depends on it;
CONDITIONAL (named items at their status); CONJECTURE; FAILED (kept with evidence); OPEN. **Evidence**: [K] kernel at L;
[D] design module (kernel-checked on a disposable branch, not certified); [W] written argument; [X] exact computation in
this thread (script, output, replay under `experiments/`); [A] audited off-repo record in `research/archive/` (cited as
data, not re-certified unless re-run); [U] unsourced.

**Scope of "obligation".** One row per item that separates the certified finite characterization
(`oiPlus_iff_qm`, CarrierGeneralOIPlus.lean:207; `typed_determined_iff`, TypedCompletion.lean:850;
`genTheory_qm_of_quantumArchitecture`, SubstratumSource.lean:136 — all over complex matrix carriers given in their
types) from an OI–QM equivalence with the quantum kinematics in the conclusion (Part A, the K row), from its
continuum/Bell extensions (Part B), and the queue rows on other tracks that the equivalence statement inherits as
scope conditions (Part C). Part D lists the queue rows that are not equivalence obligations, with the reason.

## Summary (counts by status at L; this thread changes no status)

| status at L | rows | ids |
| --- | --- | --- |
| OPEN | 18 | Kinf-Stage, Kinf-Act, Kinf-Drive, Kinf-Trans, Kinf-Seed, Kinf-V4, Kinf-Copy, Kinf-Geom, K2 (6 clauses), lambda (a research premise, not a ROADMAP row), Kn, H-inf, L3-conv, H-Bell, P0, L24.1, C4, SOI |
| OPEN, with a reduction recorded by this thread | (in the 18) | Kinf-Seed (→ Kinf-Stage + a sharp stage test, [D]); Kinf-Copy (→ type covariance, [D]+[X]); Kn (→ drivability on qubit-power carriers + the K3 closure clauses, [W]+[X]) |
| OPEN, separated by a countermodel recorded by this thread | (in the 18) | Kinf-Trans (not implied by every other single-system seam together: Ω₄, [W]+[X]) |
| OPEN, relocated (no source, a sharper form) | (in the 18) | Kinf-V4 (→ sequential closure of available tests, [W]); lambda (→ multi-token LT + FCC, [W] + record) |
| CONDITIONAL | 3 | K1-res (the selector, on its unsourced premises), K3, A6 |
| EXTERNAL | 1 | BG |
| not an equivalence obligation | 4 | H-link, H-state/frame/slope, G3 map, P3 GR→L3 states |

Rows in Parts A–C: 22 (18 OPEN, 3 CONDITIONAL, 1 EXTERNAL). K2's six clauses are counted as one row; their per-clause
status after stages 3–6 is in NOTES-E4.md. Round readiness (NOTES-E7): ready now — Kinf-Seed (S1), Kinf-Copy (S2), Kn
(S3), Kinf-Trans separation (S4), L3-conv (S5); statement and controls ready, proof heavy — K2 schema (S6); not ready —
the rest.

## Part A — the finite route to complex matrix kinematics (ROADMAP row K, :68, :971–1102)

The route, as the ROADMAP orders it (:1081–1093): K∞-Stage → K∞-Act → {K∞-Drive, K∞-Trans, K∞-Seed, K∞-V4} → ball
(TRB-1) and sharp family (OG-1) → effect cone (EFF-1) → K2 → {K∞-Copy, native gate} → `d = 3` (DIM-1) → Kₙ → K3.

| id | obligation | statement at L (kernel object) | status at L | blocking premise / missing theorem | unlocks | depends on | candidate discharging theorem | round readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Kinf-Stage** | stage consistency, elementary scope, finite rank | `SCInf` StageCompletion.lean:78 (`∀ i j (h : i ≤ j), (D.map h).Consistent`); `BinaryVisible` :244; `FiniteRank` :299 (`FiniteDimensional ℝ (affineSpan ℝ Ω).direction`); no predicate for the elementary scope | OPEN (ROADMAP :1010–1013) | no `DirectedStages` built from any OI object (only controls `badD`, `bitTower`, `midD` [K], SA-LEDGER §1.1 [A]); FiniteRank not forced on infinite carriers (Hilbert-matrix countermodel [A], SA P3); `BinaryVisible` vacuous as stated (zero/unit pair) [A] | the chart (`exists_completionChart` CompletionAction.lean:154), hence every chart consumer (TRB-1, OG-1, EFF-1) | origin thread (a source regime: SA's E1 invasive observation / E2 irreversible step) | the protocol tower PT (SA-LEDGER P-F, [A], unlanded): `protocolTower_scInf` by `rfl`, `FiniteRank` on finite carriers; the scope premise ElemScope (P-D) | a round could freeze PT's definition and `protocolTower_scInf`/`FiniteRank` on finite Ω now (E7); the scope predicate needs an owner choice |
| **Kinf-Act** | reversible operation data on the completed body | `OpDatum` CompletionAction.lean:46; `AffineRespect` :58; `Undoes` :325; `preservesBody_inducedEquiv` :352 | OPEN (:1014–1016) | existence form discharged by the identity datum (`idDatum`, CompositionOrder.lean:228 [K]) — content is relative to the family consumed downstream (SA §2.3 [A]); a stage-preserving datum has finite order (`finiteOrderOn_of_stagePreserving` CompositionOrder.lean:348 [K]), so a drive's generator must cross stages; label duals give `AffineRespect` (SA P-A [A]) | body automorphisms for Kinf-Drive / Kinf-Trans / Kinf-V4 | Kinf-Stage | `affineRespect_of_labelDual` (SA P-A) | P-A is a cheap kernel round (E7); sourcing the consumed family is not |
| **Kinf-Drive** | field-neutral drivability | `ElementaryDrivability` KInfFoundations.lean:264 (continuous flow of body automorphisms, NOT on the flow, `J` off the flow's axis) | OPEN (:1017) | no OI source; on a finite-rank body, drive ⇔ one infinite-order reversible AffineRespect datum + a non-normalizing `J` (OPS-Γ, Cartan citation, [A] drive/RESULT §2.3); matrix route circular (F-D1 [A]) | with Kinf-Trans: the ball's dynamics; K∞-1 at matrix level | Kinf-Act, Kinf-Stage | OPS-Γ ⇒ `ElementaryDrivability` (needs Cartan; not in Mathlib to the record's knowledge) | not ready (no source) |
| **Kinf-Trans** | boundary transitivity of a body-preserving family | `BoundaryTransitive` OrbitGeneration.lean:79 (`∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y`) | OPEN (:1018–1022) | CERTIFIED [K OrbitGeneration.lean:620] `not_boundaryTransitive_flow : ¬ BoundaryTransitive ball3 (Set.range rot3)`; weakened for its eleven pairing-table consumers to `DenseBoundaryOrbit` (DenseOrbit.lean:53; `maxConeOf_avail_eq_of_dense` :243; strictly weaker, `not_boundaryTransitive_ratRefl` :398) [K]; E2: on Ω₄ = {‖x‖⁴ + s⁴ ≤ 1} ⊂ ℝ⁴ ElementaryDrivability, a sharp seed, seed-orbit availability (`G = Aut`, full effects), relative strict convexity (singleton faces for every family), K∞-1 for the full effects and capacity ≤ 2 hold and no body-preserving family is boundary transitive or has a dense boundary orbit — CONJECTURE [W]+[X] (`e2_drive_trans` 10/10) with the [K] contrapositive of TransitiveBody.lean:602 / DenseOrbit.lean:174; in chart dimension 3 a drive forces the ellipsoid (CONJECTURE [W]+[L], NOTES-E2 R3) | TRB-1's ball (`exists_affine_image_eq_eball` TransitiveBody.lean:602), EFF-1's cone | Kinf-Act, Kinf-Drive (not implied by it) | — (a source of transitivity, or of a dense boundary orbit, from OI) | the separation is ready (NOTES-E7 S4); a source is not |
| **Kinf-Seed** | a sharp seed | `SharpSeed` OrbitGeneration.lean:65 (effect on Ω with a value 1 and a value 0) | OPEN (:1023–1024) | on the completion it follows from SC∞ and a stage effect with values 1, 0 (`sharpSeed_completion` StageCompletion.lean:224 [K]); E2: discharged from Kinf-Stage (SC∞ + chart), a sharp stage test (a stage effect with values 1 and 0 at two stage preparations) and the ball identification — `EqvSeams.sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage(_dense)`, CONJECTURE [D] (dev `f5367a7a`, run 38083519826 green; copy in `lean/`) | K1's `hP1` | Kinf-Stage (SC∞ + a chart), Kinf-Trans or its dense form (the identification) | `exists_sharpSeed_eball_of_stage(_dense)` [D] | ready: NOTES-E7 S1 |
| **Kinf-V4** | seed-orbit availability | `SeedOrbitAvailable` OrbitGeneration.lean:74 (`∀ g ∈ G, seedTransport r g ∈ avail`) | OPEN (:1025–1026) | body preservation of a transport does not make the effect available; a countable family suffices for the cone (`countable_seedOrbit_cone` DenseOrbit.lean:403 [K]); E2: V4 follows from seed availability and the closure of the available tests under transport by members of `G` (`seedTransport r g = r ∘ g⁻¹` OrbitGeneration.lean:49) — a relocation onto sequential closure, CONJECTURE [W] | EFF-1's cone equality | Kinf-Trans (same `G`), Kinf-Act | — | not ready |
| **Kinf-Copy** | identical copies' NOTs agree | DIM-1's `NativeGate` uses one `N` in `relT` and `relC` (CompositeDimension.lean:218); `CopyNatural` KInfFoundations.lean:284 | OPEN (:1027–1030) | J/K two-NOT countermodels at d = 5, 7 [A] (thread B, k-infinity §6); E2: replaceable by type covariance of native inversion (the target NOT conjugate to the control NOT by a body automorphism fixing or reversing the corner axis; for `IsNot` NOTs ⇔ equal ±1 eigenspace dimensions [W]) — `EqvSeams.dim_of_nativeGate2_conj`, CONJECTURE [D] (run 38083519826); the d = 5, 7 J/K countermodels violate it (`e2_copy_conj` 13/13, run 1 kept) [X]; not shown to admit any gate copy naturality excludes | DIM-1 / K1 selector without literal equality of NOTs | K2 (identification of the two factor charts) | type covariance of native inversion ⇒ `d ∈ {1,3}` [D] | ready: NOTES-E7 S2 |
| **Kinf-Geom** | sharp-update / singleton-face principle, elementary-scoped | `SingletonFaces` KInfFoundations.lean:139; `RelStrictConvex` :144; Lemma C `relStrictConvex_of_supporting_singleton` :575 and converse `singletonFaces_of_relStrictConvex` :590 [K] | OPEN (:1031–1051) | not sourced; false for complex QM at level ≥ 3 (qutrit `diag(1,1,0)` [K-audit `kn-elementary-carrier-census.md` §4]); independent of dynamics/capacity (torus, Stiefel [A]); a field-neutral "elementary system" predicate is missing | strict convexity; with Kinf-Trans the ball | Kinf-Stage (scope) | — (corrected sharp-face or self-duality route, owner-scoped) | not ready |
| **K1-res** | the selector's remaining premises | `dim_of_nativeGateOf` K1Bridge.lean:128 and `three_of_nativeGateOf_of_two_le` K2Guard.lean:253 [K]: `(hd : 2 ≤ d) (hE : EffectsOn (eball d) avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) … (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3`; `2 ≤ d ↔ HasTwoSharpTests (eball d)` (`hasTwoSharpTests_iff` SharpTests.lean:155 [K]); `two_le_not_implied` :197 [K] | CONDITIONAL as a selector (:984–1000); its premises OPEN | `0 < d`/`2 ≤ d`, effect soundness, `IsNot`, `NativeGateOf` (frame, both positivity clauses, `relC`; `relT` not needed for the selector: `dim_of_ctrlGate` RelcSelectBlock.lean:739 [K]) — all unsourced | `d = 3` | Kinf-* (via the cone), K2 (the carrier `W d` encodes LT) | — | not ready (premises unsourced) |
| **K2** | the composite: (a) LT / product-test structure, (b) the composite cone, (c) local actions compatible with it, (d) the composition theorem, (e) antiunitary/CP bridge, (f) relation to K3 | `PreComposite` CompositeInterface.lean:223, `Composite` :243 (`LocallyTomographic` :235); bounds `minBody_subset` :461, `subset_maxBody` :467 [K]; `CandidateCone` K2Guard.lean:95 and `no_candidateCone_cnot_reflY` :143 [K] | OPEN (:1001–1006) | per clause (NOTES-E4 §2): (b) cone — settled negatively at the pair level (H1–H3 do not force `Q3`: K(E0), K(Z_F) [A]); (c) local actions — is the composite action (b) itself, INDEPENDENT of every item at L (stage 6 [A]); (e) reversible part settled by `no_candidateCone_cnot_reflY` [K]; remaining: (a) LT as a source (K1 consumes PTQ only, k2d D3 [A]), (d) beyond two tokens (IE₂/KT∞), (e) three-copy part, (f) a k-token dictionary and a map between (b) and `ContextStable` | the pair cone `Q3` (conditional), IE₁, generation | Kinf-Act/Drive (availability of the flow and `J`), Kₙ, bridge thread (an H→P or M→P map), countermodels thread (exotic cones) | E4 schema `pairCone_eq_Q3_of_drive`: H1 + H2 + H3 + A_miss ⇒ `K = Q3`, CONDITIONAL on H2, H3, A_miss (proof: stage-4 Y2 [A], [W]+[X]; controls K(Z_F), twin, B3) | NOTES-E7 S6: statement and controls ready, proof heavy (spectral step); A_miss stays unsourced |
| **lambda** | four-copy coherence with `tok` (KT(4)) | none at L: no structure with three or more tokens (kernel reading at L; L's Lean tree = `bcbc516f`'s); `kt4_forward_ie1` is a design-run theorem over a kernel identical to L's (FourCopyHeadline at `ff9c3a35`, run 37948419430 [D]; re-derived over L's kernel on `dev-equivalence/kt4-at-l` at `288f80ec`, run 38084161796: build green, `kt4_forward_ie1` axioms standard [D]); KT4-PREM-1 certified the dependency assessment (receipt at L) | not a ROADMAP row; [U] | E5: `tok` holds by construction on the multi-index table carrier (multi-token LT, a carrier premise) and `H ⟺ FCC` under `hadm` [K-record], so the substantive residue is FCC (positivity across groupings); `hcl` cannot be dropped (`M_cl`), `hgate` not necessary (`M_max`) and cannot be dropped (`M_D`) [K-record] | IE₁ ⇒ (b_S4) ⇒ `Q3` | K2, Kinf-Act at pair level (P-STAGE2, P-ACT2), multi-token LT | a composition principle for four copies giving FCC (KT4-PREM-1 open question 2) | certification of the design theorem needs a registry family (§A.35); it would certify a conditional with five unsourced hypotheses |
| **Kn** | elementary → every finite carrier with its repertoire | `ImplementationClass` ImplementationLocality.lean:244 (a predicate at every finite carrier); `DrivesElementary` SubstratumSource.lean:77 (at every carrier); `QuantumArchitecture` :86 | OPEN (:1058–1069) | no theorem consumes the DIM-1 ball (no import edge, census [K-audit]); E3: inside any `Architecture` with `ContextStable` and `LabelInvariant`, admissible operators compress to every coordinate subspace (W-DESC), so drivability at the carriers `Fin (2^k)` gives `DrivesElementary` at every carrier — CONJECTURE [W]+[X] (`e3_compress` 7/7); the census's missing subspace principle is, at the K3 interface, `ContextStable + LabelInvariant + block`; what remains is drivability on qubit registers through a k-token dictionary, and the closure clauses (ContextStable = the spectator clause β of (b)) | K3 at every carrier | K2 (k tokens), (b) | Kₙ-DESC: `compress_mem`, `drivesElementary_of_pow`, `quantumArchitecture_iff_pow` (NOTES-E3 §3) | ready: NOTES-E7 S3 (pure matrix statement) |
| **K3** | the operations | `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean:136 [K]: `QuantumArchitecture 𝓘 → ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 hq.arch A)`; `typed_determined_iff` TypedCompletion.lean:850 [K]; `oiPlus_iff_qm` CarrierGeneralOIPlus.lean:207 [K] | CONDITIONAL on reaching complex matrix kinematics (:978–983) | `substratum_residual` StructuralClosure.lean:383 [K]: the substratum class has Architecture, ContextStable, LabelInvariant, DaggerStable and `¬ DrivesElementary` | finite operational QM | Kn, K2, K1 | — (it is a theorem; its hypothesis is the kinematics) | — |

## Part B — beyond finite carriers, and Bell

| id | obligation | statement at L | status | blocking premise / missing theorem | unlocks | depends on | candidate | readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **H-inf** | finite → continuum / infinite-dimensional completion of the whole characterization | `RegionLimit`, `CoherentContinuumSource`, quasilocal audits; `continuous_extension_not_unique` RegionLimit.lean:296 [K] | OPEN (:70, :936–951) | no theorem lifts composites + dynamics/selection beyond finite carriers; the quasilocal stages are complex matrix algebras by construction, so every infinite-system statement is downstream of K; infinite-support instruments are a separate unprioritized question (:945–947; HINF-REVIEW [A]) | a scope-correct OI→QM statement beyond finite carriers | K (finite, native), P0 | the scope-correct statement of NOTES-E6 §2 (finite carriers + the lattice completion only) | not a round target until K moves (E7) |
| **L3-conv** | the converse direction of Level III | `canon_unique` QuasilocalCharacterization.lean:359; `systemEquiv_dyn` :497 [K] — a uniqueness theorem among systems with the substratum's matrix-algebra stages, not a biconditional (AGENTS §A.34; HINF-REVIEW point 4 [A]) | OPEN (part of H-inf) | no theorem derives the OI_Q conditions from membership in `QuasilocalSystem`, whose definition contains the matrix-algebra stages; per region the converse is assembly of `finiteSupport_iff_kraus` (InstrumentCompletion.lean:195) and `oiPlus_of_qm` (CarrierGeneralOIPlus.lean:198) through an interface definition not in the kernel | the iff, scope-correctly (relative to the matrix stages) | H-inf; K | per-region converse (NOTES-E6 §3) | ready: NOTES-E7 S5 (derives nothing about the kinematics) |
| **H-Bell** | composite and Bell closure in the substratum/gravity sense | no kernel object; HB-1 control plane merged (§A.37 era) and never executed | OPEN (:67, :953–969) | preparation-indexed graphs must preserve no-signalling **and** satisfy an Ollivier–Ricci stability condition; the hop metric of the degree-6 cubic graph is exactly ℓ¹ (fails before any Bell edge) | Bell-inclusive completion | K2 does not discharge it (:1006); the operational Bell content belongs to K2 (pair cone), not to H-Bell (NOTES-E6 §1) | a new native round on HB-1's frozen question (§A.37) | owner call (HB-1 frozen, never executed) |

## Part C — queue rows the equivalence statement inherits as scope conditions

| id | obligation | statement at L | status | blocking item | unlocks | depends on | candidate | readiness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **P0** | what selects the relative quantum evolution OI leaves free (two-part: cross-time Gram trajectory; threading) | `CoherentLift` CoherentLiftGauge.lean:124; `gl2_strong_gauge_moves_relative_candidate` :537; `ct4_constant_left_obstruction` CrossTimeInvariants.lean:965 [K]; acts 11–45 | OPEN, localized (:63) | no carrier and no law adopted; class-level selection impossibility only within frozen classes | uniqueness of the quantum history (orthogonal to K, :1095–1096) | — | — (Track B's own programme) | Track B's own rounds |
| **L24.1** | Lemma 24.1, semigroup transfer (𝒢_sub completeness) | `ST3_pairC` SemigroupTransfer.lean:749; `trace_wordEval_hiddenConjugate` :468; `WT1_transfer` WordTraceSufficiency.lean:420; `WT3_spanning_iff` :624 [K] | OPEN (:64, :665–720) | `WT2` unitary implementation on general pairs (structure theory of *-subalgebras of `M_m(ℂ)`); 24.1B not begun | unconditional 𝒢_sub completeness | — | WT2 | substratum programme |
| **A6** | background independence / local gauge covariance | `A6Cov` BackgroundIndependence.lean:131; `a6cov_all` :161; `pk2a_bridge` A6Instantiation.lean:257; `cx3b_complex_not_A1` :512 [K] | CONDITIONAL (:65) on the identification of the physical substratum with the packaged carrier | that identification | the A1–A6 package | — | — | owner decision (:818–819) |
| **C4** | physical C4 discharge at the cosmological and lattice cuts | `RoutedReadback` PhysicalC4Discharge.lean:68; `LatticeCutReadback` :633; `core_routedReadbackAtStorage_two` PhysicalC4StorageReadback.lean:342 [K] | OPEN, exact per cut (:66) | cosmological: the finite realization datum; lattice: [SM] Theorem 22's readback genericity lemma | the physical realization | — | — | physical-realization programme |
| **SOI** | stochastic observer interface `(Obs, μ)` | `ensemble_underdetermined` StochasticInterface.lean:118; `waveSubstratum_stochastic_interface_gap` :191 [K] | OPEN (:69) | independently motivated structure selecting `Obs`, `μ`, or invariance of consuming claims | a sourced physical stochastic law | — | — | foundations programme |
| **BG** | Bekir–Golomb integer classification | `BGIntegerClassification` TurnpikeScopeTransfer.lean:542 (cited premise of `spectral_classification_of_BG` :563) | EXTERNAL (:71) | formalizing the 2007 classification | the last reconstruction premise of the turnpike transfer | — | — | independent formalization job |

## Part D — queue rows that are not equivalence obligations

H-link (:72, the physical `K = 6` carrier), H-state/H-frame/H-slope (:73, the `ℏ` and `1/4` calibration), the
covariant matter→boundary coupling G3 (:74) and GR states → Level-III states (:75) are Standard-Model and gravity
bridges downstream of the OI→QM question; none appears among the hypotheses of the three finite characterization
theorems or of the K-route theorems, and none is consumed by H-∞ or H-Bell as the ROADMAP states them. They are listed
so that the inventory is complete, and carry no row here.

## Cross-thread dependencies (stated as interfaces; the other threads' branches were not read)

- **bridge**: any proved map from the hidden-history (H), matrix (M) or general (G) levels to the pair carrier `W 3`
  (P) would bear on K2(c) = (b) and on Kₙ (the field-neutral → `ImplementationClass` map); stage 6's NO-MEET [A]
  records that no such map exists at L.
- **origin**: a source regime for Kinf-Stage/Act/Drive (SA's E1/E2 escapes) or for (b) would discharge rows marked
  "no source".
- **countermodels**: exotic pair cones (K(Z_F), EXOTIC-E seeds) are what keep K2(b)/(c) OPEN; an embedded-observer
  realization of K(Z_F), or an obstruction to one, is open at L in either direction (stage 6 §6 [A]).

## Round-2 notes (dated; statuses at L unchanged — this thread changes no status)

Each note is dated, names its evidence, and supersedes nothing in the tables above, which stay as written in round 1.

- **2026-10-10 (round 2) — Kinf-Act, Kinf-Drive.** Received HO-2 v1 (inbox; bridge B3): an off-axis
  `ElementaryDrivability` is never the closure of directed stage-preserving finite operations, so a drive's generator
  must cross stages — CONDITIONAL on Jordan's theorem and the finite subgroups of SO(3) [L]. Consistent with, and sharper
  than, `finiteOrderOn_of_stagePreserving` (CompositionOrder.lean:348 [K]). Status OPEN.
- **2026-10-10 (round 2) — Kinf-Seed.** The three seed theorems compile as the standalone predicted module `StageSeed`
  over L ([D] run 38091534622, R-E8.4); preregistration draft S1 (KINF-SEED-1) written. Status OPEN.
- **2026-10-10 (round 2) — Kinf-Copy.** The type-covariance reduction compiles as the standalone predicted module
  `CopyCovariance` over L ([D] run 38091534622, R-E8.4); draft S2 (KINF-COPY-1) written. Status OPEN.
- **2026-10-10 (round 2) — Kinf-Trans.** The decisive step of the separation, Ω₄ is no affine image of `eball 4`, is
  kernel-checked in a design run together with Ω₄'s compactness, convexity, symmetry, seed and drive ([D] run
  38090924005, R-E8.3); strict convexity and the separation theorems did not build in that run (two failed terms; the
  proof-only repair is unmeasured), so the separation stays at R-E2.5's [W]+[X]. Draft S4 (KTRANS-SEP-1) written, marked
  not ready to freeze. Status OPEN.
- **2026-10-10 (round 2) — Kn.** Kₙ-DESC is kernel-checked in a design run ([D] run 38090116254, R-E8.2): within the K3
  architecture drivability descends from the carriers `Fin (2^k)`, and `QuantumArchitecture` is equivalent to its closure
  clauses with qubit-power drivability, one witness per direction. Draft S3 (KN-DESC-1) written. What remains is
  unchanged: drivability on qubit registers and the closure clauses (`ContextStable` the matrix form of (b)'s spectator
  clause). Status OPEN.
- **2026-10-10 (round 2) — K2.** The pair-level schema `pairCone_eq_Q3_of_drive` has a complete written proof with every
  identity checked exactly (NOTES-E10; R-E10.1–R-E10.4): A_miss enters at one lemma (reachability of every pure state from the
  products by words in `cnot` and one token's unitaries); the cone step needs no spectral theorem (PSD definition and
  Gram decomposition); the finite clause `⟨R_z(π/2), cyc3⟩` fails at reachability on an exact witness (EXOTIC-E by claim
  D [A]); two exact rotations `R_z(θ₀)` (`cos θ₀ = 3/5`) and `cyc3` suffice given H3's closedness. Status OPEN; the schema
  is CONDITIONAL on H2, H3, A_miss.
- **2026-10-10 (round 2) — L3-conv.** NOTES-E9: the converse read relative to the target class (C-REG) holds by transfer
  along the stage map ([D] `kraus_iff_of_member`); the naive dynamical converse (C-DYN) is false ([D]
  `not_naiveConverseDyn`, from [K] :769/:792; exact stage witnesses, including a real sign automorphism); the naive
  kinematic converse (C-KIN) is false (classical lattice, non-uniform sites [X]; [D] `not_comm_of_system`); the converse
  holds at one finite level under H-FAC, H-UNIF, H-GEN and H-DYN ([W]+[L]+[X]), H-FAC being the site-level quantum
  kinematics. Status OPEN as an obligation in its strong reading, which is now refuted as stated; the scope-correct
  Level III statement of NOTES-E6 §3 stands.

## Round-3 notes (dated; statuses at L unchanged — this thread changes no status)

Each note is dated, names its evidence, and supersedes nothing above.

- **2026-10-11 (round 3) — Kinf-Trans.** Draft S4's checkpoint `C0` is met: the repaired `EqvOmega4` builds over L with all
  fifteen prints standard ([D] run 38096511360, R-E12.1), so the separation — on Ω₄ every other single-system seam in its
  kernel form holds and no body-preserving family is boundary transitive or has a dense boundary orbit — is kernel-checked
  in a design run (upgrading R-E2.5's [W]+[X]). Received HO-15 v1 (CONDITIONAL): Aut(Ω₄) = O(3) × ℤ₂ with orbits the level
  sets of `s⁴`; the facial invariant `c*` is constant on every `C¹` body, so it cannot source K∞-Trans (assumption-watch
  marker). Received HO-9 v1 item 3 (CONDITIONAL; its stage-crossing clause CERTIFIED, CompositionOrder.lean:378): no
  passive finite-rank tower carries an infinite-order datum, hence no drive and no transitive family of that origin.
  Status OPEN.
- **2026-10-11 (round 3) — Kinf-Trans, self-duality (E13).** Self-duality of the state cone is not a source of K∞-Trans in
  chart dimension 4: Ω⋆ (strongly self-dual, every seam but central symmetry; R-E13.1) and Ω_cs (self-dual, every seam
  including central symmetry; R-E13.3) are drivable, strictly convex, with sharp seeds, and admit no boundary-transitive
  or dense-orbit family (CONJECTURE [W]+[X], the non-transitivity through TransitiveBody.lean:602 and DenseOrbit.lean:174).
  What does force the ellipsoid is central symmetry with a self-dualizing inner product invariant under the central
  symmetry (R-E13.2, [W]); a centrally symmetric self-dual non-ellipsoid carries a filter. HO-15's assumption-watch
  marker, sharpened accordingly. In chart dimension 3 the question is empty (R-E2.6). Status OPEN.
- **2026-10-11 (round 3) — L3-conv, infinite volume (E14).** NOTES-E9's H-DYN is a top-stage condition; read at every
  finite stage of an infinite lattice it forces site permutations and excludes OI's own interacting dynamics (R-E14.1,
  exact at `N = 3, 4`). In the transport form (stage matrix units to `{0,1}`-matrices) with locality preservation of the
  automorphism and its inverse, it yields a global `ReversibleDynamics` and a Target A system (R-E14.2, written proof).
  Like H-DYN it restates (O3) on the stages. Status OPEN.
- **2026-10-11 (round 3) — K2.** The pair-level schema is kernel-checked in a design run (R-E11.1–R-E11.3, [D] run
  38101580750): the dictionary `W 3 ≃ Herm(ℂ² ⊗ ℂ²)` as a real-linear equivalence with its product law and pairing,
  LOWER and UPPER, and `pairCone_eq_Q3_of_drive` with L4 isolated as the hypothesis `ReachPure`. Received HO-10 v1
  (a compact pair group containing `cnot` with abelian identity component cannot meet such a reachability hypothesis:
  item 1 CONJECTURE, item 2 CONDITIONAL on claim (D)) and HO-12 v1 (the dictionary's (D1)–(D2); the clause (T) a named
  premise, FAILED as a bridge; the A_miss split), each at its label. Status OPEN; the schema stays CONDITIONAL on H2,
  H3, A_miss and `ReachPure`, none sourced.
