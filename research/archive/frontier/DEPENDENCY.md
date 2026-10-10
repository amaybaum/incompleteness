# FRONTIER — the end-to-end dependency DAG for OI ↔ finite-dimensional complex QM

Read-only research thread. Base `b7af4852b79fa3bfa90e9b5c2eca3aca6890395a` (CC-2 landing), checkout
`scratchpad/wt-frontier`. Every kernel citation below was verified by `grep`/`sed` against
`verification/lean-mathlib/OIBridge/*.lean` at that commit; line numbers are at the base.

**Provenance check.** `git diff --stat 0f2687b7 HEAD -- verification/lean-mathlib` is empty, so the Lean
tree at the base is byte-identical to the tree the SELECT / DRIVE / OPACT / OI-STAGE notes cite
(`0f2687b7`); relative to Wave 2's base `f7f5c3b0` it adds exactly `StageCompletion.lean`,
`InvariantInnerProduct.lean`, `CompletionAction.lean` and their import lines. Every `file:line` in the
scratchpad notes therefore resolves at the base, and each one used here was re-read.

Classification key (one per edge): **SEALED** (theorem at the base, statement quoted), **ADAPTER** (mathematics
proved, interfaces do not compose literally), **LEMMA** (substantive but plausibly follows from existing
conditions; written or cited proof exists off-repo or is standard), **UNKNOWN** (unresolved),
**INDEPENDENT/PREMISE** (a sealed or exact countermodel shows non-entailment from the proposed antecedents).
"off-repo exact" = a replayed exact computation in the scratchpad (not evidence of a theorem; cited as pointer).

Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, NGB `NativeGateBall`,
SC `StageCompletion`, CA `CompletionAction`, IIP `InvariantInnerProduct`, GC `GeneralCarrier`, OA
`OperationalAssembly`, IL `ImplementationLocality`, TC `TypedCompletion`, DC `DiscreteCompletion`.

***

## 0. Identifiers the scratchpad notes rely on that do NOT exist at the base

Checked with case-insensitive `grep -rniE` over all 199 modules:

| name (as used in the notes) | status at base | consequence |
|---|---|---|
| `EnergyObservable`, `genAlg`, `Obs`, "dynamical correspondence" (Thread R, SELECT EO) | **absent** | EO has no kernel statement; every EO edge below is at best LEMMA/UNKNOWN |
| `DriveCore` (Thread N I2) | **absent** | the "no-continuity" drive is unformalized; `ElementaryDrivability` (KF:264) carries `flow_continuous` |
| `OperationalDrive`, `EffClose` (Thread O D-1), `BodyOperationalTheory`, `SeqClosed`, `DriveAvailable` (Thread P) | **absent** | no field-neutral notion of an *available* transformation exists; V4′ is a bare proposition on a set `avail` |
| `LIMCLOSE`/`LimClose` (DRIVE §0, SELECT §5) | **absent**; the only closure predicate is `DC.ClosureAvail` (DC:63), ℂ-typed, header "deliberately not adopted" | LIMCLOSE-C is a bare premise with no vocabulary |
| `elementaryDrivability_of_substratum` | **absent** (as the notes also record) | no sourcing route for the drive exists in the kernel |
| `ell_ellipsoid`, `ell_closure`, `rotWords`, `kR_exact_words`, `NormalizedInvariance` (Thread N) | **absent** | the ellipsoid step is not kernel |
| `dim3_of_transitive_energyObservable` (Thread R) | **absent** | DIM3 ⇐ {TRANS, EO} is written only |
| any `DirectedStages` instance built from an OI construction | **absent**: the only instances are the controls `badD` (SC:342), `bitTower` (SC:393), `midD` (CA:404) | N2 below has no kernel object |
| any `ElementaryDrivability` instance other than `ball3Drive` (KF:449) | **absent** | the B⁴/Hamel/Sp(1) countermodels are off-repo exact only |
| a field-neutral local-tomography or composite-of-bodies predicate | **absent** (only `InstrumentDilation.local_tomography_physical`, a theorem on `Matrix (A × B) (A × B) ℂ`) | Task 3's LT premise has no kernel home outside the quantum tensor product |
| Cartan closed-subgroup theorem / compact Lie rank-1 classification | not in Mathlib at the pinned tag (not re-checked here beyond the Thread N table) | Route Γ (ORD∞ ⇒ flow) and Thread R step 8 are citation-level |

***

## 1. The DAG, node by node

Nodes N0–N13 follow the target chain *finite OI → finite representation → selected geometry → 3-ball + effects →
composite → full QM*. Each edge row: antecedents → conclusion, identifiers, file:line, literal type fit, class.

### N0 — Finite OI / observer premises

| edge | identifiers | file:line | types line up | class |
|---|---|---|---|---|
| boundary modes finite + finite settings ⇒ `C_V` finite (Lemma 1) | `Finiteness.lean` (conditional, physical premise `[Finite Mode]` exposed) | header lines 1–30 | yes | SEALED as implication; premise PHYSICAL |
| sealed C1–C4 core realized in a theory | `RealizesSealedOICore` | OIRealization:234 | — | definition (OI core) |
| bare OI ⇏ QM | `oi_alone_not_qm : ∃ T, RealizesSealedOICore T ∧ ¬ ExactAllFiniteEndomorphicQuantumOps T` | GC:160 | yes | SEALED (countermodel `diagTheory`) |
| full composite control ⇒ sealed core | `realizesSealedOICore_of_control` | OIRealization:252 | yes | SEALED |

### N1 — Finite representation (the fixed-basis bridge; input, not re-proved)

| edge | identifiers (statement) | file:line | class |
|---|---|---|---|
| S ⇔ D ⇔ Q_fb at every finite horizon | `finite_horizon_equivalence (P) : (Stochastic P ↔ RevRealizable P) ∧ (RevRealizable P ↔ QfbRealizable P) ∧ (QfbRealizable P ↔ Stochastic P)` | Equivalence:459 | SEALED |
| `QfbReal` carries unitary + fixed basis only (no generator clause) | `structure QfbReal`, `QfbReal.IsLaw` | Equivalence:190–218 | SEALED (scope) |
| dilation `W` isometry, marginal, extends to unitary | `dilation_isometry`, `dilation_marginal`, `dilation_extends` | EquivalenceChain:292/322/335 | SEALED |
| OI class = PPer, PPer ⊆ Q*, Q* ⊄ PPer | `qStar_of_pper`, `qStar_inclusion_iff_nonempty`, `qStar_not_subset_pper` | QuantumRepresentationT3:202/209, T2:169 | SEALED |
| CPTP + classical agreement ⇔ correlation-matrix family; reversible ⇔ rank-one phase | `cptpExtension_iff_correlationMatrix`, `reversibleExtension_iff_rankOne` | CoherentExtension:533/595 | SEALED |
| classical comb blind to the correlation matrix | `classicalComb_blind_to_correlation` | CoherentExtension:821 | SEALED |
| **N1 ⇏ N5 (representation sources no control)** | `substratum_residual` (StructuralClosure:383), `readWriteSourced_not_qm` (ReadWriteControl:174), `obs_not_layerFlowExecutable` (ExecSource:129), `substratumTheory_not_layerFlowExecutable` (LiftAudit:200), `onesFixing_not_phasesAvailable` (PhaseSource:52) | — | **INDEPENDENT** (matrix level: the stated substratum/observer theories realize the core and execute no layer flow) |

### N2 — An OI construction as a field-neutral stage system (`DirectedStages`)

| edge | identifiers | class |
|---|---|---|
| OI protocol tower PT/CT ⇒ `DirectedStages` with SC∞ | none (OI-STAGE note: laws `rfl`, SC∞ by `RegionTower.iterate_dependsOnlyOn_ball` RT:283, `card_fibre` RT:398 — these two exist; the packaging does not) | LEMMA (cheap; unlanded) |
| finite substratum ⇒ completed body is a polytope ⇒ no infinite-order automorphism | OI-STAGE NG1 (written + exact); kernel analogue `isEmpty_drivability_of_finite_orbits` (ON:124) gives "finite orbits ⇒ no drive" | LEMMA (NG1 written) + SEALED (ON:124) |
| Level 3A: linear rule, OBS-R, I₃ ⇒ exposed sector 4-dim, seven reachable points, hull = octahedron, action group Sym({0,1}²) | off-repo exact (RESULT-3A, LEMMA-3A) | off-repo exact; **no kernel object** |
| infinite-lattice CT has `FiniteRank` | none; Main.md:542 names it as an obligation; OI-STAGE exact ranks 1,1,1 (linear) and 1,4,6 growing (nonlinear) | UNKNOWN (open premise) |

### N3 — Completion interface (CMP-1)

| edge | statement | file:line | class |
|---|---|---|---|
| SC∞ ⇒ sharp stage pair is a sharp seed on the completion | `sharpSeed_completion (hSC : SCInf D) (h1 : p e x1 = 1) (h0 : p e x0 = 0) : SharpSeed (body D) (coord D ⟨i, e⟩)` | SC:224 | SEALED (conditional on SC∞) |
| every stage effect is an effect on the body (no premise) | `stageEffects_isEffectOn`, `coord_unit_eq_one` | SC:193/204 | SEALED |
| BinaryVisible ⇒ visible test on body; + SC∞ ⇒ perfectly distinguishable pair | `visible_test_completion`, `perfectlyDistinguishable_visible` | SC:260/274 | SEALED (conditional) |
| FiniteRank + nonempty ⇒ affine chart of the span | `exists_chart_of_finiteRank` | SC:304 | SEALED |
| SC∞, FiniteRank, BinaryVisible sourced from OI | none | UNKNOWN (named premises; CMP-1 result §"What stays open") |

### N4 — Operations on the completed body (OPACT-1)

| edge | statement | file:line | class |
|---|---|---|---|
| AffineRespect datum ⇒ unique affine map of the chart; preserves `chartBody`; composes | `existsUnique_induced`, `induced_mem`, `induced_after` | CA:258/300/319 | SEALED |
| datum with inverse datum ⇒ affine equivalence with `PreservesBody (chartBody C) {inducedEquiv …}` | `preservesBody_inducedEquiv` | CA:352 | SEALED |
| stage effects pulled back are effects on the chart body | `isEffectOn_pullback` | CA:364 | SEALED |
| StateRespect ⇏ AffineRespect | `midOp_stateRespect`, `midOp_not_affineRespect` | CA:434/461 | SEALED (countermodel) |
| a source of AffineRespect operation data in an OI construction | none (OI-STAGE: label-map duals need PREFIX-CLOSURE; written) | UNKNOWN / LEMMA |
| `PreservesBody` ⇔ `g '' Ω = Ω` (IIP's hypothesis form) | trivial; chart form `image_bodyR_eq` | IIP:428 | ADAPTER (two lines) |

### N5 — Drive / infinite-order operation on the completed body

| edge | identifiers | class |
|---|---|---|
| ORD∞ (one infinite-order reversible AffineRespect datum) + FiniteRank + compact chart body ⇒ continuous circle of automorphisms (D1–D8) | DRIVE Route Γ: Cartan closed-subgroup theorem + torus structure (citation); not in Mathlib | LEMMA (standard math; kernel-hard) |
| + J non-normalizing (OFF-Γ′) ⇒ `ElementaryDrivability (chartBody C)` | DRIVE §2.3 (written) | LEMMA |
| ORD∞ alone ⇏ off-axis J | kernel `not_boundaryTransitive_flow` (OG:620) shows the flow alone is not transitive; `obligations_independent` (C5Discovery:59) matrix OFF/flow independence | INDEPENDENT (D9 is a separate premise) |
| chart body compact with nonempty interior (needed by IIP) | `isCompact_bodyR`, `interior_bodyR_nonempty` (IIP:402/375) need `[FiniteDimensional ℝ V]`; `CSpace D = lp … ∞` is not finite-dimensional | **ADAPTER** (new lemma: `chartBody C` is closed by `isClosedEmbedding_chart` CA:189 and bounded in `Fin d → ℝ`; interior from `affineSpan_gen` CA:218 + `Convex.interior_nonempty_iff_affineSpan_eq_top`) |
| stage-preserving operation has finite order on a finite-rank body | DRIVE F-D3 (written) | LEMMA (cheap) |
| drive availability as *operations* | no vocabulary (see §0) | UNKNOWN |

### N6 — Invariant inner product (IIP-1)

| edge | statement | file:line | class |
|---|---|---|---|
| compact body with interior in `Fin n → ℝ`: every `g '' Ω = Ω` fixes centroid and preserves `invMatrix Ω` (sym. pos. def.) | `invariant_inner_product` | IIP:§D (used at IIP:469) | SEALED |
| through a chart of the affine span, for every restriction `g'` of a body automorphism | `invariant_inner_product_span [FiniteDimensional ℝ V] …` | IIP:455 | SEALED, but **does not apply to `CSpace D`** (see N5 ADAPTER); the `Fin n` form applies to `chartBody` once compactness/interior are supplied |

### N7 — Selection of the geometry (SELECT §4 hypotheses: ORD∞, TRANS, EO, V4′)

| edge | identifiers | class |
|---|---|---|
| `BoundaryTransitive Ω G` (OG:79, exact finite words over *all* `IsBoundaryState`) + `PreservesBody Ω G` ⇒ every boundary state is extreme (affine automorphisms preserve extreme points) | none in kernel; two-line argument (this note) | LEMMA (cheap) — **this is where the SELECT ordering breaks: see RESULT §"predicate divergences"** |
| exact TRANS + IIP (centroid-fixing, invariant quadratic form) + compact convex + interior ⇒ Ω is the Q-ball (every boundary state on one Q-sphere; Lemma B form) | `eq_closedBall_of_frontier_subset_sphere` (KF:770) gives the Euclidean-norm instance; the Q-form/chart instance is unlanded | ADAPTER + LEMMA (Thread R step 2; K∞ design §7 Lemma B) — **no DIM3, no drive needed** |
| DIM3 + IIP-N + `ElementaryDrivability` ⇒ ellipsoid (`ell_ellipsoid`) | Thread N (written + exact) | LEMMA |
| DIM3 + IIP-N + `ElementaryDrivability` (with `flow_continuous`) ⇒ `BoundaryTransitive Ω (words (range D.flow ∪ {D.J}))` | Thread N KR-exact-words (written; Euler-angle route partially kernel: `exists_euler_angles` ON:614, `euler_apply_pole` ON:589 for the control drive) | LEMMA; `flow_continuous` load-bearing (Hamel model off-repo) |
| TRANS ⇏ DIM3 | `boundaryTransitive_ball4 : BoundaryTransitive ball4 isom4`, `finrank_E4 : Module.finrank ℝ E4 = 4` | ON:735/744 | **INDEPENDENT (SEALED)** |
| {TRANS, EO} ⇔ DIM3 given DRIVE + compact + FR | Thread R §3 (written; step 8 cites compact rank-1 classification) | LEMMA (citation-level) |
| EO ⇐ {ORD∞/DRIVE, TRANS, V4′, FR, compact}? | Thread R countermodel B⁴ with the Sp(1) drive: DRIVE and TRANS hold exactly, no intertwiner (off-repo exact `r_checks.py` B1, E); kernel has only `boundaryTransitive_ball4` for `isom4`, no `ElementaryDrivability ball4` | **INDEPENDENT (off-repo exact; kernel partial)** |
| TRANS ⇐ ORD∞ (+ FR)? | `not_boundaryTransitive_flow` (OG:620): the infinite-order rotation flow of `ball3Drive` is not boundary transitive | **INDEPENDENT (SEALED)** |
| ORD∞ ⇐ exact TRANS (dim ≥ 2)? | uncountable boundary ⇒ `G` uncountable ⇒ not torsion (Schur/Jordan or: closure is a positive-dimensional compact Lie group); written here | LEMMA (new; see FRONTIER F7) |
| EO sourced from any OI/observer theorem | none; only corpus shadow is the ℂ gate flow `SecondOrderCircuit.unit g t = exp(iπt·proj g)` (SOC:356) and `LiftAudit.gateFlow` (LA:47) | UNKNOWN (unsourced) |

### N8 — From the 3-ball to the directional effects and the Lorentz cone (OG-1 / NB-1 bridge)

| edge | statement | file:line | class |
|---|---|---|---|
| `T '' Ω = ball3` + PreservesBody + SharpSeed + BoundaryTransitive ⇒ seed orbit = directional family read through `T` | `seedOrbit_eq_of_normalization` | ON:307 | SEALED (conditional) |
| same ⇒ Lorentz-cone test for transported seeds | `lorentz_of_normalization` | ON:340 | SEALED |
| on `ball3`: PreservesBody + P1 + K∞-R ⇒ `seedOrbit G r = directionalFamily` | `seedOrbit_ball3_eq` | OG:348 | SEALED |
| + V4′ ⇒ every `ballEffect b`, `∑ b j ^ 2 = 1`, is available | `ballEffect_mem_avail` | OG:369 | SEALED |
| directional family ⇒ Lorentz cone | `lorentz_of_effects (p) (hp : 1 ≤ p) … : 0 ≤ x0 ∧ ∑ v j ^ 2 ≤ x0 ^ 2` | NGB:105 | SEALED |
| P1 + K∞-R + V4′ + PreservesBody ⇒ (SEC) on any body; `KInf1 ball3 avail` | `supportingEffectComplete_of_sharp_transitive`, `kInf1_ball3_of_orbit` | OG:192/389 | SEALED |
| hypotheses move along charts and coordinate changes | `hypotheses_tr`, `hypotheses_restrict` | ON:295/529 | SEALED |
| (SF) on a ball for any family | `singletonFaces_closedBall` | KF:658 | SEALED |
| (SEC) + (SF) ⇒ relative strict convexity, and converse | `relStrictConvex_of_supporting_singleton`, `singletonFaces_of_relStrictConvex` | KF:575/590 | SEALED |
| V4′ ⇐ SEED-AVAIL ∧ SEQ ∧ TRANS± | Thread P P-4 (written); needs a record `(eff, trans)` absent from the kernel | LEMMA (trivial) on an UNKNOWN vocabulary |
| V4′ on the words ⇔ ∃ generator-closed subfamily containing `r` | Thread P P-2 (written) — the circularity certificate | LEMMA |
| V4′ with countable available group fails for the continuum family | Thread P E8 (off-repo exact; rational orbit); kernel shadow `fixedGateTheory_not_qm` (DC:1948) with `fixedGateTheory_denseUnitaryControl` (DC:1942) | INDEPENDENT (matrix level SEALED; field-neutral off-repo) |
| sharp seed from SC∞ (P1 source) | `sharpSeed_completion` (SC:224) | SEALED (conditional on SC∞ and a stage pair with values 1 and 0) |

### N9 — LIMCLOSE-C (limit closure of availability)

| edge | identifiers | class |
|---|---|---|
| available operations closed under pointwise limits on stage preparations ⇒ flow members (closure of ⟨g⟩) are available | definitional once stated; no vocabulary | UNKNOWN (premise) |
| limit closure follows from the completion (SC∞/FiniteRank/OPACT)? | CMP-1 closes *states* only (`body D := closure (convexHull …)`, SC:141); OPACT-1 has no closure | no edge |
| dense availability ⇏ exact availability | `fixedGateTheory_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory α)` (DC:1948) with `fixedGateTheory_denseUnitaryControl` (DC:1942), `fixedGateTheory_krausSoundExt` (DC:1938) | **INDEPENDENT (SEALED, matrix level)** |

### N10 — Composite / G-layer (NB-1, K2)

| edge | identifiers | class |
|---|---|---|
| two LT d-balls, full self-dual cones, common `N`, invertible `G` with CNOT corners, `(I⊗N)G(I⊗N)=G`, `(N⊗I)G(N⊗I)=(I⊗N)G`, `G`, `G⁻¹` product-state positive ⇒ `d ∈ {1,3}` | kernel core `nb1_kernel_core` (NGB:255) = `p_le_one` ∧ `parity` ∧ `dim_of_bounds`; S1, S2, S4 value identity written for all `d`, exact for `d ≤ 7` | SEALED (core) + LEMMA (written general-`d`) |
| common `N` (copy naturality) deletable? | C2N two-NOT countermodel `d = 5` (NB-1 probe, exact); `d = 7` two-NOT with both NOTs continuously interpolable (K∞ §6, exact) | **INDEPENDENT (exact; not kernel)** |
| control-NOT relation deletable? | C5 J/K map `d = 5` (exact) | INDEPENDENT (exact) |
| `G⁻¹` positivity deletable? | NB-1 result: open | UNKNOWN |
| existence of a nonlocal reversible `G` from single-system ball geometry | no theorem; `ball3Drive`, `fullAut3` are single-system | **PREMISE (anti-circularity: nothing single-system supplies it)** |
| LT (field-neutral) | no predicate; `local_tomography_physical` (InstrumentDilation:440) assumes `Matrix (A × B) (A × B) ℂ` | PREMISE; the kernel theorem is a reverse-direction witness only |
| composite existence / functoriality / readout / discard (field-neutral) | absent | PREMISE |
| K2 (composition theorem, antiunitary and CP bridge) | ROADMAP K2 **OPEN**; no governed round | UNKNOWN |

### N11 — Matrix-level operational completion (the sealed classification, consumed as input)

| edge | statement | file:line | class |
|---|---|---|---|
| exact finite endomorphic QM on system and every composite ⇔ five conditions | `exactAll_iff_physical_general`, `general_characterization`, `main_result` | GC:100/107/188 | SEALED |
| the five conditions | `PhysicalCompletionConditions T := CompositeOperationalValidity T ∧ InertSpectatorCompositionality T ∧ HasCompositeUnitaryControl T ∧ IteratedAncillaClosure T ∧ SystemToLevelOne T` | PhysicalCharacterization:295 | definition |
| each of the five independent of the other four and of the OI core | `five_way_minimality` (RankGapTheory:702), as conjunct (iii) of `main_result` | SEALED |
| OI⁺ ⇔ QM on every nonempty finite carrier | `carrier_general_oiPlus`, `oiPlus_iff_qm` | CarrierGeneralOIPlus:213/207 | SEALED |
| primitive-source forms | `oiPlusMin_iff_qm` (MinimalRepertoire:569), `oiPlusPos_iff_qm` (PositivePackage:55); `OIPlusMin := ImplementationLocality ∧ PhaseFreeRichness ∧ EmbeddedObservation` (MR:544) | SEALED |
| phase-free richness ⇒ control needs `IteratedAncillaClosure` on carriers with ≤ 2 states | `control_of_phaseFree (hclos : IteratedAncillaClosure T) (h : PhaseFreeRichness T)`, via `descend` (MR:512) and `not_hControl_two` (MR:362) | MR:529 | SEALED (closure load-bearing at small carriers) |
| typed (rectangular) determination | `typed_determined_iff : 𝒯.ShadowQuantum ↔ ∀ S S' … availT S S' (Fin m) F ↔ IsTypedKrausInstrument F` | TC:850 | SEALED |
| substratum + continuous off-diagonal controllability ⇔ QM | `substratum_extension_quantum_iff_drives`, `substratum_plus_control_qm` | StructuralClosure:408/414 | SEALED |
| within `DerivedOI`: QM ⇔ one executable layer flow of a moved involution | `derivedOI_qm_iff_layerFlowExecutable' (hd : DerivedOI T) (hσ) (hx : σ x ≠ x) : ExactAll… ↔ LayerFlowExecutable T σ` | DerivedQ3:222 | SEALED |
| composite soundness is not forced by control + system exactness | `exactControl_not_implies_krausSoundExt` | DimensionalCountermodel:648 | SEALED (INDEPENDENT witness) |
| control ⇏ inert spectators | `control_not_implies_parallelReferenceExtension` | ReferenceExtension:507 | SEALED |
| inert spectators and iterated closure independent, both deletable | `independence_matrix`, `inert_not_deletable`, `closure_not_deletable`, `conditional_classification` | CompositionalIndependence:214/252/261/277 | SEALED |
| availability ⇏ H_comp | `availability_not_implies_hComp` | MonoidalCompletion:770 | SEALED |

### N12 — From the selected 3-ball (+ composites) to N11's hypotheses

| edge | identifiers | class |
|---|---|---|
| 3-ball with directional effects ≅ `Matrix (Fin 2) (Fin 2) ℂ` density matrices and effects (Bloch parametrization) | none in kernel (`qubit_certain_face` KF:995 is a fragment on the matrix side) | ADAPTER (standard; needs a Bloch-map theorem) |
| drive words `SO(3)` ≅ unitary conjugations `SU(2)/U(1)` | none | ADAPTER (double cover; standard) |
| single-system drive + composite ⇒ composite-level drives (`PhaseFreeRichness` at every `A × Fin n`) | none; `five_way_minimality` shows `HasCompositeUnitaryControl` independent of the other four + core | **PREMISE / UNKNOWN** (the largest gap in the chain) |
| `ImplementationLocality`, `EmbeddedObservation` from the field-neutral layer | none | PREMISE |
| Kraus soundness as a restriction | `KrausSound` (KrausSoundness:128); from validity + inert + control: `krausSoundExt_of_validity_inert` (OperationalValidity:124) | SEALED given the five conditions |

### N13 — Identification and orientation

| edge | statement | file:line | class |
|---|---|---|---|
| two completions with identical complete pairing data are unitary- or transpose-conjugate | `sameData_unitary_or_transpose … : ∃ Φ W, (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ((∀ X, Φ X = W * X * Wᴴ) ∨ (∀ X, Φ X = W * Xᵀ * Wᴴ))` (hypotheses: Hermitian spanning menus with unit, separating PSD state families generating the PSD cone) | JordanClassification:1109 | SEALED — **assumes matrix kinematics** |
| no selector factoring through pairing data picks the orientation | `operational_orientation_noGo (G σ S) : S (fun i k => trace ((G i)ᵀ * (σ k)ᵀ)) = S (fun i k => trace (G i * σ k))` | OrientationSelection:139 | SEALED (residual ℤ₂^anti is genuine) |
| circuit statistics invariant under global transposition | `circuit_invariance` | AntiunitaryInvariance:71 | SEALED |
| the relative evolution between two times is not fixed by the visible family | ROADMAP P0 (Track B acts 11–15, `GL2`, `CT2`–`CT4`) | OPEN (not re-verified here) |

***

## 2. Reverse direction (QM ⇒ premises) — kernel witnesses

| premise | QM witness | file:line | class |
|---|---|---|---|
| drive on the ball | `ball3Drive`, `ball3_drivable : Nonempty (ElementaryDrivability ball3)` | KF:449/490 | SEALED |
| exact TRANS for the drive's words | `boundaryTransitive_ball3Drive : BoundaryTransitive ball3 driveWords3` | ON:667 | SEALED |
| P1, V4′ jointly satisfiable | `seedOrbit_fullAut3`, `seedOrbitAvailable_self` | OG:561/144 | SEALED |
| (SEC), (SF), K∞-1 on the ball with full effects | `supportingEffectComplete_ball3`, `singletonFaces_closedBall`, `kInf1_ball3_full` | KF:1053/658/1076 | SEALED |
| QM satisfies the five conditions / OI⁺ / layer flow | `physical_of_exactAll`, `oiPlus_of_qm`, `derivedOI_layerFlowExecutable_of_qm`, `layerFlowExecutable_of_control` | PhysicalCharacterization:301, CarrierGeneralOIPlus:198, DerivedQ3:229, LiftAudit:117 | SEALED |
| QM's LT, purification, pure seed, Lüders selector | `local_tomography_physical`, `purification_of_factorization`, `uniform_readout_feedforward_seed`, `luders_selector_cp` | InstrumentDilation:440, Purification:165/115/128 | SEALED |
| EO for the qubit (hat map `so(3) ≅ ℝ³`) | off-repo exact (Thread R H1) | UNRESOLVED (kernel) |
| ORD∞, OFF-Γ′ for the qubit | off-repo exact (DRIVE G1–G2) | UNRESOLVED (kernel; elementary) |
| a QM `DirectedStages` with SC∞, FiniteRank, BinaryVisible and AffineRespect phase/Clifford data | DRIVE §1.2–1.4 matrix instance (written+exact; forces body = Bloch ball) | UNRESOLVED (kernel); the only kernel tower with SC∞ is the classical `bitTower` |
| LIMCLOSE-C in QM | standard (compact unitary group); no kernel statement | UNRESOLVED (kernel) |
| copy naturality in QM | trivial (one `N`) | written |
| NB-1 hypotheses for two qubits | probe control C3 (exact) | exact, not kernel |
