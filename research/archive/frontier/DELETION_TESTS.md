# DELETION TESTS — "all other candidate assumptions ⟹ H ?"

Base `b7af4852`. For each questionable final assumption `H`: the test, the best proof route, the best
countermodel route, what would settle it, and the present verdict with its evidence type (kernel / exact
off-repo / written). Ordered by the mission's priority: SELECT composition, LIMCLOSE-C, EO, G/composite
provenance, local tomography, remaining primitives.

The candidate single-system bundle is SELECT §4: {ORD∞, TRANS, EO, V4′} on the completed body of a finite-rank
stage tower, with SC∞ and the OPACT data in force. TRANS is read in **two** ways throughout, because the SELECT
note and the kernel differ on it (RESULT §"predicate divergences"):
- TRANS-v: transitivity on the extreme points (what `select/checks.log` tested on the octahedron);
- TRANS-x: `OrbitGeneration.BoundaryTransitive Ω G` (OG:79), i.e. for **every** pair of `IsBoundaryState`s.

***

## 1. The SELECT composition itself

**H = "ORD∞ ∧ TRANS ∧ EO ∧ V4′ (on the completed body) ⟹ Ω is a 3-ball with the directional effects available".**

- *Is it an adapter, a lemma, or missing a premise?* All three, in layers:
  - **Missing premises (not derivable):** (i) `FiniteRank`, compactness and nonempty relative interior of the
    completed body — compactness is an ADAPTER (FRONTIER F3), finite rank is UNKNOWN (F2); (ii) the OFF clause
    `J_off_axis` if the drive is to be reached from ORD∞ (F6) — but see below, under TRANS-x it is not needed;
    (iii) the availability vocabulary and SEQ/TRANS± behind V4′ (F9–F11).
  - **Substantive lemmas:** F5 (Cartan), F7 (TRANS-x ⇒ purity/ORD∞/ellipsoid), F8 (TRANS+EO ⇒ DIM3, citation
    step 8), Thread N's ellipsoid/KR-exact-words.
  - **Adapters:** chart-body compactness (F3), `PreservesBody ⇔ g '' Ω = Ω`, LDL normalization to `ball3` so that
    `seedOrbit_eq_of_normalization` (ON:307) and `lorentz_of_normalization` (ON:340) fire.
  - **Sealed tail:** once `T '' Ω = ball3`, `SharpSeed`, `BoundaryTransitive`, `PreservesBody`,
    `SeedOrbitAvailable` are in hand, OG-1 closes to the Lorentz cone with no further premise.
- *Verdict:* **not an adapter.** The state-space half (a) of SELECT §4 is a composition of written lemmas with one
  citation-level step (compact Lie structure, used twice: F5 and F8) and one missing adapter (F3); the effect
  half (b) is sealed modulo V4′'s own premises. Nothing in it is proved as a theorem at the base.
- *Settling result:* kernelize F7(c) and the LDL normalization; then the only unsealed single-system content is
  EO ⇒ DIM3 (F8) and the sourcing of TRANS-x, EO, V4′.

## 2. LIMCLOSE-C

**H = "available operations on the completed body are closed under pointwise limits on stage preparations".**

- *Exact fact the final proof uses:* only that the flow members `S(t) ∈ closure⟨g⟩` are **available** operations,
  so that TRANS± (F10) holds for every real `t` and V4′ then yields the whole continuum `directionalFamily`.
  Without it the available group is at most countable (words in finitely many stage operations), the seed orbit
  is countable, and `seedOrbit G r = directionalFamily` (OG:348) cannot hold for the available `G` — Thread P E8
  (exact): the words of `{rot3(arccos 3/5), cyc3}` have a rational orbit.
- *Does it follow from sealed completion machinery?* No. CMP-1 closes states (`body D := closure (convexHull …)`,
  SC:141) and nothing else; OPACT-1 induces maps from data and has no limit clause; `isEffectOn_pullback` (CA:364)
  shows pulled-back stage effects are effects, not that they are available.
- *Best proof route:* none; the only route is to **define** the available group as a closed subgroup of
  `Aut(chartBody)` (adopting the field-neutral D3), which relocates the premise into a definition.
- *Best countermodel route (SEALED, matrix level):* `fixedGateTheory α` — `fixedGateTheory_derivedOI` (DC:1929),
  `fixedGateTheory_fixedGateSourced` (DC:1933), `fixedGateTheory_denseUnitaryControl` (DC:1942),
  `fixedGateTheory_krausSoundExt`, and `fixedGateTheory_not_qm` (DC:1948): dense, countable availability with every
  other structural clause, and not QM.
- *Verdict:* **INDEPENDENT** (matrix-level kernel witness; field-neutral analogue exact off-repo). Weakest
  theorem target: the premise as stated, or the closed-subgroup definition.

## 3. EO (energy observability / dynamical correspondence)

**H = "ORD∞ ∧ TRANS ∧ V4′ ∧ FiniteRank ∧ compact (∧ SEC ∧ SF) ⟹ EO".**

- *Exact formal content:* none at the base. Thread R's candidate: `genAlg Ω G` = Lie algebra of the closure of the
  linear parts of `G` on `dir Ω`; `Obs Ω` = `Module.Dual ℝ (dir Ω)`; `EnergyObservable := ∃ φ : genAlg →ₗ Obs,
  Injective φ ∧ φ ⁅X,Y⁆ = −(φ Y) ∘ X`. Its sole corpus shadow is the ℂ-typed gate flow
  `SecondOrderCircuit.unit g t = exp(iπt·proj g)` (SOC:356), whose generator is π times a sharp effect; that is a
  matrix fact, not a source.
- *Does any earlier OI/observer theorem produce it?* No. No kernel theorem mentions a generator-to-observable map;
  `DerivedOI` (RouteB:141) contains `PhasesAvailable`, `ExchangesAvailable`, `ReadWriteAvailable` — all
  monomial. (Names, comments and prose were not used as evidence; the grep is over declarations.)
- *Best proof route:* none known; EO is the single-system fingerprint of ℂ (Alfsen–Shultz; Barnum–Müller–Ududec),
  so a derivation would have to source complex structure.
- *Best countermodel route:* the 4-ball with the `Sp(1)` left-multiplication drive — DRIVE fields and exact TRANS
  hold, every injective equivariant `𝔤 → ℝ⁴` fails (Thread R B1, E; exact off-repo). Kernel already has the
  dimension-4 transitivity for `isom4` (`boundaryTransitive_ball4`, ON:735); it lacks an `ElementaryDrivability
  ball4`.
- *Verdict:* **INDEPENDENT** of all other single-system candidates (exact off-repo; kernel partial). Settling
  result: land `ball4` with the `Sp(1)` drive as a kernel `ElementaryDrivability` and the (defined) failure of EO
  — this upgrades the independence to kernel evidence and fixes EO's definition.

## 4. ORD∞

**H = "the other hypotheses ⟹ some available reversible operation of infinite order on the body".**

- Under TRANS-v (vertex transitivity): the Level 3A octahedron with `Sym({0,1}²)` satisfies TRANS-v, V4′ trivially
  (finite family), EO vacuously; ORD∞ fails (finite `G`). **INDEPENDENT** (exact, Level 3A + `select/checks.log`).
- Under TRANS-x (`BoundaryTransitive`): F7(b) — an uncountable boundary forces an uncountable `G`, which is not
  torsion. **LEMMA**: ORD∞ is derivable, except on the segment (`d = 1`), where TRANS-x holds with `G = {id,
  flip}` and `not_drivable_Icc` (KF:529) shows no drive. So under TRANS-x the whole content of ORD∞ is "the body is
  not the classical bit".
- The three notions are distinct: one infinite-order operation (ORD∞) ⇏ a continuous flow without compactness +
  finite rank + closure (Route Γ, F5); a continuous flow ⇏ transitivity (`not_boundaryTransitive_flow`, OG:620,
  SEALED); transitivity (TRANS-x) ⇒ ORD∞ (F7(b)). Full boundary transitivity is strictly the strongest.

## 5. TRANS

**H = "ORD∞ ∧ EO ∧ V4′ (∧ OFF, ∧ DIM3) ⟹ TRANS-x for the drive's own words".**

- *Which form the selector needs:* `seedOrbit_ball3_eq` (OG:348) and `seedOrbit_eq_of_normalization` (ON:307)
  consume exactly `BoundaryTransitive Ω G` — exact finite words, every boundary state. Closure-transitivity is
  not enough (Hamel model, Thread N §3, exact + written: `ELL-closure` holds, `BoundaryTransitive` fails because
  the word group is countable).
- *Proof route:* with DIM3 + IIP + `ElementaryDrivability` (continuity load-bearing) Thread N's KR-exact-words
  gives it (LEMMA, unlanded; kernel has only the control `boundaryTransitive_ball3Drive`, ON:667). Without DIM3:
  `B⁴` with `R(t) ⊕ I₂` and the block swap satisfies every drive field and is not transitive (Thread N X8;
  exact).
- *Do `ElementaryDrivability`, generated words, orbit generation imply it?* `preservesBody_driveWords` (ON:107)
  gives only `PreservesBody` of the words — body preservation, not transitivity. Orbit generation
  (`seedOrbit_ball3_eq`) **consumes** transitivity. No sealed hypothesis implies it.
- *Verdict:* TRANS-x is derivable from {DRIVE with continuity, DIM3, IIP} (LEMMA) and otherwise a PREMISE;
  as the SELECT bundle takes DIM3 from {TRANS, EO}, TRANS-x cannot be derived inside the bundle without
  circularity — it must be a premise there, and it is the strongest one (F7).

## 6. V4′ / effect richness

**H = "the state-space hypotheses ⟹ V4′".** Separated:

| assumption | implied by | kernel | verdict |
|---|---|---|---|
| one sharp seed (P1) | SC∞ + a stage pair with values 1, 0 | `sharpSeed_completion` (SC:224) | SEALED conditional |
| orbit availability of the seed (V4′) | SEED-AVAIL ∧ SEQ ∧ TRANS± | written (Thread P P-4); CM0/CM1/CM2/CM2′ exact countermodels show each load-bearing | LEMMA on missing vocabulary; premises unsourced |
| directional effects available | V4′ + P1 + K∞-R + PreservesBody | `ballEffect_mem_avail` (OG:369) | SEALED conditional |
| supporting-effect completeness (SEC) | same | `supportingEffectComplete_ball3_of_orbit` (OG:382) | SEALED conditional |
| singleton faces (SF) | the ball alone (any family) | `singletonFaces_closedBall` (KF:658) | SEALED |
| full effects | directional family + mixing closure | none (F12) | LEMMA + PREMISE |
| V4′ ⇐ drive existence alone | refuted: drive exists, flow not available (Thread P CM2, exact) | — | INDEPENDENT (exact) |

Matrix-level analogue (SEALED): `genTheory_qm_of_quantumArchitecture` (SubstratumSource:136) — drivability gives
every instrument including the sharp effects (K∞-1M); the field-neutral Naimark step `KInf1` (KF:1013) is a
definition proved for no physical family.

## 7. G / composite provenance

**H = "single-system 3-ball + composite existence + LT ⟹ ∃ reversible nonlocal `G` with the native relations".**

- *Proof route:* none; nothing in the single-system leg mentions a second system. Anti-circularity: `fullAut3`,
  `ball3Drive`, `boundaryTransitive_ball3Drive` are single-body objects.
- *Countermodel route (standard GPT, not in corpus):* two qubit balls composed with only local reversible
  operations (the "locally quantum, no entangling gate" theory). Satisfies every single-system clause and LT, has
  no `G`. Cheap exact probe; would settle independence.
- *Sealed evidence that stronger availability does not supply composite structure:*
  `exactControl_not_implies_krausSoundExt` (DimensionalCountermodel:648), `control_not_implies_parallelReferenceExtension`
  (ReferenceExtension:507), `independence_matrix` (CompositionalIndependence:214), `availability_not_implies_hComp`
  (MonoidalCompletion:770).
- *Verdict:* PREMISE; independence likely but the exact witness is not in the corpus.

**H = "common `N` on identical copies".** INDEPENDENT (NB-1 C2N `d = 5`; K∞ §6 `d = 7`, exact). Settling result: the
"type covariance of native inversion" reduction (ROADMAP K∞) as an exact probe.

**H = "`G⁻¹` positivity".** UNKNOWN (NB-1 open item). Settling result: search `d ≥ 5` for `G` injective with
`G(min) ⊆ max` and `G⁻¹` not positive meeting the other relations.

## 8. Local tomography

**H = "composite existence + single-system structure + availability ⟹ LT".**

- No field-neutral LT predicate exists. The kernel's `local_tomography_physical` (InstrumentDilation:440) has
  the quantum tensor product as its domain and is a reverse-direction witness only.
- Independence evidence in the corpus is indirect: `exactControl_not_implies_qutritReferenceExtension`
  (ReferenceExtension:513) shows exact system QM + full composite control does not give the spectator extension;
  the known GPT countermodels to LT (real QM, where product effects do not separate composite states) are standard
  and not in the corpus.
- *Verdict:* PREMISE; settle by adding the real-qubit composite as an exact probe (LT fails, everything
  single-system holds).

## 9. Remaining primitives (Naimark-style transport)

| primitive | matrix-level object | field-neutral | provenance | verdict |
|---|---|---|---|---|
| composite with a register | `availExt n` on `A × Fin n` (OA:594 structure field); typed `S × R` (TC:165) | absent | interface postulate | PREMISE |
| register attachment / preparation | `prepAvail_uniform` (field); pure seed derived from swap control `pureSeedPrep_available` (OA); typed `attach` | absent | field + control | PREMISE (uniform attach) + SEALED (pure seed from control) |
| sharp register readout | `readout`, `readout_avail`, `readout_local` (fields); form derived `readout_is_localLuders` (OA:658) | absent | existence postulated, form derived | PREMISE (existence) + SEALED (form) |
| reversible transport + discard | `prepAvail_discard` (field) + `circuit_available` (OA:757, needs `HasCompositeUnitaryControl`); `InstAvail.discard` (IL:285) | absent | field + control | PREMISE + SEALED |
| functoriality (bind/coarse) | `availExt_bind`, `availExt_coarse` fields; `InstAvail.bind/coarse` constructors | absent | postulated / definitional | PREMISE |

All five are ℂ-matrix-specific at the base; none is usable without the quantum structure to be derived. The
field-neutral programme's K∞-1 (`KInf1`) is the statement that the four primitives reproduce sharp effects from a
drive; it is proved for no physical family (`kInf1_ball3_full` is the ball-with-full-effects control;
`not_kInf1_ball3_unit` shows it depends on the family).
