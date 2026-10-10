# MINIMAL HYPOTHESES — three bundles

Base `b7af4852`. "Sufficient on paper" means: with the written/cited lemmas of FRONTIER.md accepted, the chain
to exact finite-dimensional complex operational QM (up to the antiunitary orientation) closes; every arrow is
either SEALED or has a written proof or a standard citation. Nothing in Bundle A is a kernel theorem end to end.

***

## Bundle A — currently sufficient on paper (single system → composite → full QM)

**A0 Scope commitments (not physical premises).**
- A0.1 A finite reversible substratum with an observer interface packaged as `D : DirectedStages` (F1; the only
  kernel instances are controls).
- A0.2 `SCInf D` (SC:78) — table consistency of forward maps.
- A0.3 `FiniteRank (body D)` (SC:299) — the open obligation of Main.md:542; false for every finite substratum
  with a non-polytope target (OI-STAGE NG1) and unknown for the lattice completion.
- A0.4 `BinaryVisible D` (SC:244) — the binary-visible part of ELEM; a sharp stage pair with values 1 and 0 (gives
  P1 through `sharpSeed_completion`, SC:224).

**A1 Operation data (OPACT-1 vocabulary).**
- A1.1 A set of `OpDatum D` with `AffineRespect` (CA:58), closed under inverse data (`Undoes`, CA:325), so that
  `inducedEquiv` (CA:333) with `preservesBody_inducedEquiv` (CA:352) gives a group `G ⊆ Aut(chartBody C)`.
- A1.2 LIMCLOSE-C: `G` closed under pointwise limits on stage preparations (F11).

**A2 Selector on the completed body.**
- A2.1 TRANS-x: `BoundaryTransitive (chartBody C) G` (OG:79).
- A2.2 EO: energy observability for `G` on `chartBody C` (F8 definition).
- A2.3 (ORD∞ and the drive are derivable from A2.1 by F7(b)/F5, except on the segment; keep the clause "the body
  is not a point or a segment", `not_drivable_singleton` KF:564 / `not_drivable_Icc` KF:529 mark the excluded
  cases.)

**A3 Effect availability.**
- A3.1 SEED-AVAIL: the P1 seed is available.
- A3.2 SEQ: an available effect read after an available operation is available.
- A3.3 TRANS±: the members of `G` (including the limit members under A1.2) are available operations.
  (A3.1–A3.3 ⇒ V4′, Thread P P-4; V4′ + P1 + A2.1 ⇒ `directionalFamily ⊆ avail`, `ballEffect_mem_avail` OG:369.)
- A3.4 Mixing closure of available effects (F12), to reach the full self-dual cone NB-1 and the Bloch adapter use.

**A4 Composite layer (NB-1 / K2).**
- A4.1 Two-system composite existence with LT (F13).
- A4.2 Identical-copy covariance / common `N` (F15).
- A4.3 A reversible nonlocal `G` with the native CNOT corner action, both NOT relations, and two-sided
  product positivity (F14).
- A4.4 K2: the composite body is the quantum tensor product and composition is functorial (F17; OPEN).

**A5 Operational completion at every composite level (matrix-level, after the Bloch adapter F18).**
- A5.1 `ImplementationLocality` (IL:370) and `EmbeddedObservation` (EmbeddedObservation:123), or equivalently
  well-formedness + observational independence + observer recursion (`OIPlus`, CarrierGeneralOIPlus:185).
- A5.2 `PhaseFreeRichness` at every level `A × Fin n` (MR:423) — the (iv)-type resource; in GR's smallest form,
  one executable layer flow of a moved involution within `DerivedOI` (`derivedOI_qm_iff_layerFlowExecutable'`,
  DerivedQ3:222), which presupposes the phase intervention (`PhasesAvailable` ∈ `DerivedOI`).
  Then `oiPlusMin_iff_qm` (MR:569) / `carrier_general_oiPlus` give exact finite endomorphic operational QM on
  every carrier, and `typed_determined_iff` (TC:850) the typed (rectangular) theory.

**A6 Orientation.** One oriented premise (passivity of a non-maximally-mixed stationary state, GR.md:206–210,
`counting_passive`) to remove the transpose branch left by `operational_orientation_noGo`
(OrientationSelection:139); otherwise the conclusion is QM/ℤ₂^anti.

**Count.** Physical premises in A (excluding scope A0 and adapters): A1.2, A2.1, A2.2, A3.1–A3.4, A4.1–A4.4,
A5.1, A5.2, A6 — fifteen named items, several of which are known to be mutually independent (Bundle C).

***

## Bundle B — likely reducible by bridge lemmas (with the lemma that would remove each)

| premise | reduces to / removed by | lemma | evidence that the reduction is sound |
|---|---|---|---|
| ORD∞ (SELECT 1) | A2.1 TRANS-x | F7(b): uncountable boundary ⇒ `G` has an infinite-order element | Schur–Jordan or closed-subgroup theorem; written here |
| the drive `ElementaryDrivability` (D1–D9) as a separate premise | A2.1 + A1.2 + compactness | F5 (Route Γ, Cartan) for D1–D8; the OFF clause D9 becomes unnecessary once TRANS-x is assumed (the ellipsoid comes from F7(c), transitivity is assumed) | DRIVE §2.3 written; Thread R step 1 |
| DIM3 as a premise | A2.1 + A2.2 | F8 (Thread R §3; step 8 cites compact rank-1 classification) | exact independence audit of every hypothesis (r_checks.py) |
| the ellipsoid / `T '' Ω = ball3` normalization | A2.1 + IIP-1 + F3 | F7(c) + LDL normalization; feeds `seedOrbit_eq_of_normalization` (ON:307) | Lemma B kernel instance `eq_closedBall_of_frontier_subset_sphere` (KF:770) |
| (SEC), `KInf1` on the body | A3 + A2.1 + P1 | `supportingEffectComplete_of_sharp_transitive` (OG:192), `kInf1_ball3_of_orbit` (OG:389) | SEALED |
| (SF) | the ball | `singletonFaces_closedBall` (KF:658) | SEALED |
| P1 (sharp seed) | A0.2 + A0.4 | `sharpSeed_completion` (SC:224) | SEALED |
| chart-body compactness | A0.3 + closedness of `body D` | F3 adapter | `isClosedEmbedding_chart` (CA:189), `body_isClosed` (CA:202) |
| full effect cone | A3.1–A3.4 | F12 (elementary convex geometry) | standard |
| Kraus soundness | A5.1 + A5.2 | `krausSoundExt_of_validity_inert` (OperationalValidity:124) | SEALED |
| `HasCompositeUnitaryControl` | A5.2 + iterated ancilla closure (from A5.1) | `control_of_phaseFree` (MR:529) | SEALED |
| typed QM | endomorphic QM on every carrier | `typed_determined_iff` (TC:850) | SEALED |
| the OI-core conjunct | A5 | `completedOI_iff_physical` (CompletedOI:110), `realizesSealedOICore_of_control` | SEALED |
| copy naturality (A4.2) | "type covariance of native inversion" (frame-preserving conjugacy class fixed by system type) | NOT-conjugacy reduction (K∞ §16 item 1) — untested | candidate only |

***

## Bundle C — currently evidenced independent (only with actual independence evidence)

| premise | independent of | witness | evidence type | location |
|---|---|---|---|---|
| EO (A2.2) | DRIVE, TRANS-x, V4′, FR, compactness, (SEC), (SF), capacity 2 | `B⁴` with the `Sp(1)` drive (also `B⁴` with `isom4`, `B⁵` quaternionic bit, `B⁷`) | exact off-repo; kernel partial (`boundaryTransitive_ball4`, `finrank_E4`) | Thread R §4.1, §6; ON:735/744 |
| TRANS-x (A2.1) | ORD∞ / a continuous flow | the rotation flow of `ball3Drive` alone | **kernel** | `not_boundaryTransitive_flow` OG:620 |
| TRANS-x | drive + V4′ + full effects (dim 4) | `B⁴`, `R(t) ⊕ I₂`, block swap | exact off-repo | Thread N X8 |
| DIM3 | TRANS-x | `ball4`, `isom4` | **kernel** | ON:735/744 |
| OFF (`J_off_axis`) | the flow and the phases (matrix level) | `substratumTheory`/`onesTheory`: phase without flow, flow without phase | **kernel** | `obligations_independent` C5Discovery:59 |
| LIMCLOSE-C (A1.2) | every other structural clause (matrix level) | `fixedGateTheory α` | **kernel** | DC:1929–1948 |
| V4′ (A3) | drive existence | drive present, flow not available (CM2) | exact off-repo | Thread P §4 |
| SEED, SEQ, TRANS± | each other | CM0, CM1, CM2, CM2′ | exact off-repo | Thread P §4 |
| common `N` (A4.2) | the other NB-1 hypotheses | two-NOT J/K maps, `d = 5` and `d = 7` | exact off-repo (NB-1 probe, K∞ §6) | NB-1 result; K-INF-DESIGN §6 |
| control-NOT relation | the other NB-1 hypotheses | C5 J/K map, `d = 5` | exact (NB-1 probe) | NB-1 result |
| composite soundness / inert spectators / iterated closure (A5.1 parts) | exact system QM + full composite control | round-34 countermodel; `admissibleTheory` | **kernel** | `exactControl_not_implies_krausSoundExt`, `independence_matrix`, `inert_not_deletable`, `closure_not_deletable` |
| each of the five completion conditions | the other four + OI core | `everywhereAvailable`, `countermodel`, `diagTheory`, `gapTheory`, `systemLoose` | **kernel** | `five_way_minimality` (via `main_result` GC:188) |
| the three OI⁺ principles | each other | qubit witnesses | **kernel** | `oiPlus_independence` CarrierGeneralOIPlus:230 |
| the drive / layer flow (A5.2) | the stated substratum and observer access | `substratumTheory`, `obsTheory` | **kernel** | `substratumTheory_not_layerFlowExecutable` LA:200, `obs_not_layerFlowExecutable` ExecSource:129, `substratum_residual` StructuralClosure:383 |
| the phase intervention | finite bijective read-write dynamics | ones-fixing classes | **kernel** | `onesFixing_not_phasesAvailable` PhaseSource:52 |
| orientation (A6) | all unoriented operational data | transposition | **kernel** | `operational_orientation_noGo` OrientationSelection:139, `circuit_invariance` AntiunitaryInvariance:71 |
| the OI core as a selector | — | `diagTheory` realizes the core and is not QM | **kernel** | `oi_alone_not_qm` GC:160 |

**Not in Bundle C despite being premises** (no independence witness in the corpus): composite existence (A4.1),
LT (A4.1), nonlocal `G` existence (A4.3), `G⁻¹` positivity, K2 (A4.4), `FiniteRank` (A0.3), `SCInf` (A0.2),
`AffineRespect` data (A1.1), SEQ/TRANS± sourcing. These are PREMISE/UNKNOWN, not INDEPENDENT — "no theorem
found" is not treated as independence.
