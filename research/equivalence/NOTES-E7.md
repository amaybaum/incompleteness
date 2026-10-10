# NOTES-E7 — round readiness, and preregistration skeletons

**Nothing here is a control plane, a preregistration or a round.** These are research drafts in this thread's own
directory. A governed round under AGENTS.md §A.39 would need its own `v3-round` and `v3-governed-paths` blocks, a
registry family (§A.35), frozen controls and owner designation of `F`; none is created or proposed for creation here.

**Readiness criterion.** A round is *ready* when (i) a theorem statement exists in landed vocabulary (or with a definition
budget of named, small new definitions), (ii) its outcome can be predicted with a sign, a strength and a reason, and (iii)
each hypothesis has a control that is exact or kernel-checkable. *Ready* says nothing about whether the round would move a
ROADMAP status: most ready rounds below would not, and each skeleton says so.

## 1. Readiness per obligation

| obligation (LEDGER id) | ready now? | why / what is missing | skeleton |
| --- | --- | --- | --- |
| Kinf-Seed | **yes** | statement and proof exist ([D] green, run 38083519826); controls in the kernel | S1 |
| Kinf-Copy | **yes** | statement and proof exist ([D]); controls exact ([X]) and partly kernel (`gC5`, `nC5` RelcSelectC5) | S2 |
| Kn | **yes** | statement (Kₙ-DESC) with a complete written proof and exact instances; kernel cost moderate (an `Equiv` extension, the closed form of `flow (transition · ·)`) | S3 |
| Kinf-Trans | **yes** (separation) | statement exists; proof written + exact; kernel cost moderate-high (strict convexity of an ℓ⁴-sum, the ellipse-section step) | S4 |
| L3-conv | **yes** (assembly) | per-region converse relative to the matrix stages; cost unchecked (one interface definition) | S5 |
| K2 (schema, pair level) | statement and controls **yes**; proof **heavy** | stage-4 Y2 is written with exact ingredients; a kernel proof needs a real-PSD `Q3` and a spectral step; a round should admit an UNDECIDED outcome | S6 |
| Kinf-Stage | partly | the protocol tower PT (`protocolTower_scInf` by `rfl`, `FiniteRank` on finite Ω, SA P-F [A]) is a ready definition round; the scope predicate needs an owner choice (ElemScope) | — (SA P-F is already drafted [A]) |
| Kinf-Act | partly | `affineRespect_of_labelDual` (SA P-A [A]) is a ready cheap round; sourcing the consumed family is not | — |
| Kinf-Drive, Kinf-V4, Kinf-Geom | no | no source to state; V4's relocation to operational closure is one line (NOTES-E2) and not worth a round alone | — |
| K1-res | no | `two_le_not_implied` and `hasTwoSharpTests_iff` [K] exhaust what can be proved without a source | — |
| lambda | no (for sourcing); certification of the design theorem possible | `kt4_forward_ie1` re-derived at L [D]; a certifying round would certify a conditional with five unsourced hypotheses (KT4-PREM-1) | — |
| H-inf | no | downstream of K; the scope-correct statement (NOTES-E6 §2) is wording, not a theorem | — |
| H-Bell | owner call | HB-1 is a frozen, never-executed §A.37 control plane; a new native round would cite it | — |
| P0, L24.1, A6, C4, SOI, BG | outside this thread | each has its own programme; L24.1's WT2 waits on spatial structure theory absent from Mathlib at the pin | — |

## 2. Skeletons

### S1 — EQV-SEED: the seed of the ball from a sharp stage test

- **Question.** Is K∞-Seed implied by SC∞, a completion chart, a stage effect with the values 1 and 0 at two stage
  preparations, and the chart body's identification with `eball`?
- **Statement.** `sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage_dense`
  as in `lean/EqvSeams.lean` §A (quoted in NOTES-E2 §1).
- **Predicted outcome.** PROVED; strength very high (the module built green at `f5367a7a`, run 38083519826).
- **Controls.** SC∞ load-bearing: `badD`, `not_scInf_bad` (StageCompletion.lean:342, :350) — a stage value that does
  not transfer; the zero value load-bearing: `not_sharpSeed_unsharp` (OrbitGeneration.lean:652); positive:
  `bitTower_scInf` (StageCompletion.lean:401) with its seed (:435).
- **What no outcome licenses.** That OI supplies a sharp stage test, a chart or the ball identification.
- **ROADMAP effect if proved.** K∞-Seed's sentence (:1023–1024) could name the stage-level sharp test as the remaining
  content (proposal HP-1); no status changes.

### S2 — EQV-COPY: type covariance of native inversion suffices

- **Question.** Does DIM-1's selector hold when the two copies' NOTs are conjugate by a corner-fixing body automorphism
  instead of equal?
- **Statement.** `nativeGate2_conj`, `nativeGate_of_conj`, `dim_of_nativeGate2_conj`,
  `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg` (`lean/EqvSeams.lean` §B–§D).
- **Predicted outcome.** PROVED; strength very high (built green).
- **Controls.** Positive: `swapped_nativeGate2` with `swapped_not_ne` (`lean/EqvSeamsControl.lean`); the hypothesis
  "the conjugator preserves the ball" load-bearing for the transfer: a shear fixing `z` (exact, value `−1/2`,
  `e2_copy_conj` S1); the conjugacy hypothesis load-bearing: the d = 5 J/K data — at L as `gC5` with `nC5`
  (RelcSelectC5.lean) for the one-NOT form; a kernel statement of its two-NOT clauses with unequal splits would be new.
- **Hazard.** The control instance's gate also has a one-NOT reading with the target NOT (`e2_copy_conj` C6): the round
  must not claim that type covariance admits gates that copy naturality excludes.
- **ROADMAP effect if proved.** The candidate at :1027–1030 is confirmed; K∞-Copy could be restated as type covariance of
  native inversion (equivalently equal ±1 eigenspace dimensions for `IsNot` NOTs, a [W] equivalence the round could
  prove as well).

### S3 — EQV-KN-DESC: drivability descends from qubit-power carriers

- **Question.** In an implementation class with `Architecture`, `ContextStable` and `LabelInvariant`, does drivability
  at the carriers `Fin (2^k)` give `DrivesElementary` at every finite carrier?
- **Statement.** `compress_mem`, `drivesElementary_of_pow`, `quantumArchitecture_iff_pow` (NOTES-E3 §3), the iff with one
  witness per direction (§A.34).
- **Predicted outcome.** PROVED; strength high (complete written proof, exact instances `e3_compress` 7/7); the risk is
  kernel engineering (an `Equiv` extending a prescribed injection; a closed form of `flow (transition a b) t`).
- **Controls.** `ContextStable` load-bearing: the class "full at sizes `2^k`, unit-disk diagonal elsewhere" (closure
  clauses written; failures exact, `e3_compress` K2); `block` and `LabelInvariant` load-bearing: the generated classes of
  NOTES-E3 §2 (written; to be made exact by the round); invariance of the coordinate subspace load-bearing for the
  generators: the non-unitary compression `e3_compress` K1; positive: `fullClass` (`fullClass_arch`,
  ImplementationLocality.lean:518).
- **What no outcome licenses.** That K2 or OI supplies drivability on qubit registers, or the closure clauses.
- **ROADMAP effect if proved.** Kₙ's sentence (:1058–1069) could say that, inside the K3 interfaces, the carrier-general
  quantifier reduces to qubit-power carriers given the architecture's closure clauses (proposal HP-1).

### S4 — EQV-TRANS-SEP: transitivity is independent of the other single-system seams

- **Question.** Is there a compact convex body with interior carrying ElementaryDrivability, a sharp seed, relative
  strict convexity, supporting-effect completeness for its full effects and central symmetry, on which no set of affine
  automorphisms is boundary transitive or has a dense boundary orbit?
- **Statement.** `∃ Ω : Set (Fin 4 → ℝ), IsCompact Ω ∧ Convex ℝ Ω ∧ (interior Ω).Nonempty ∧
  Nonempty (ElementaryDrivability Ω) ∧ (∃ r, SharpSeed Ω r) ∧ RelStrictConvex Ω ∧
  SupportingEffectComplete Ω (fullEffects Ω) ∧ CentrallySymmetric Ω 0 ∧
  ∀ G, PreservesBody Ω G → ¬ BoundaryTransitive Ω G ∧ ¬ DenseBoundaryOrbit Ω G`, witness Ω₄.
- **Predicted outcome.** PROVED; strength medium-high (written proof complete, exact checks `e2_drive_trans` 10/10);
  kernel risk in strict convexity of the ℓ⁴-sum and in the step "an affine image of a ball has ellipse sections"
  (contrapositive of `exists_affine_image_eq_eball` TransitiveBody.lean:602 and `…_of_dense` DenseOrbit.lean:174).
- **Controls.** Positive: `eball 4` (all clauses and transitive); strict convexity load-bearing for Geom:
  `B³ × [−1, 1]` (drivable, not strictly convex); the non-ellipse step non-vacuous: the 4-ball's section system is
  consistent (`e2_drive_trans` C1).
- **What no outcome licenses.** Anything about which bodies OI supplies, or about chart dimension 3 (where a drive
  forces the ellipsoid, NOTES-E2 R3, [W] + [L]).

### S5 — EQV-L3-CONV: the per-region converse of Level III

- **Question.** Does every member of `QuasilocalSystem` with finite-support availability satisfy OI⁺ at every finite
  region?
- **Statement (needs one definition).** `regionTheory S Λ : FiniteOperationalTheory (Conf Λ Q)` built from the
  finite-support instruments of `S` on region Λ; then `∀ Λ, OIPlus (regionTheory S Λ)` from `finiteSupport_iff_kraus`
  (InstrumentCompletion.lean:195) and `oiPlus_of_qm` (CarrierGeneralOIPlus.lean:198).
- **Predicted outcome.** PROVED; strength medium (the interface definition's cost is unchecked).
- **Controls.** `q3_countermodel` (InstrumentAvailability.lean:335) bounds the scope to finite support.
- **What no outcome licenses.** A derivation of the matrix-algebra stages — they are in `QuasilocalSystem`'s definition;
  the result is an iff between two descriptions that both carry the quantum kinematics (NOTES-E6 §3).

### S6 — EQV-K2-SCHEMA: the pair cone under A_miss

- **Question.** Do products, `cnot`-invariance, self-duality and invariance under ball3Drive's flow and its
  `cyc3`-conjugate on one token force the pair cone to be `Q3`?
- **Statement.** `pairCone_eq_Q3_of_drive` (NOTES-E4 §3), with `Q3 := {ω | certW ω ⪰ 0}` (a new definition, ℂ-free).
- **Predicted outcome.** PROVED, strength medium; a kernel proof needs a spectral argument; the round should freeze an
  UNDECIDED label for a proof not reached, and never certify the conclusion from the exact instances.
- **Controls.** Positive `Q3`; K(Z_F) (no A_miss); `PT_B(Q3)` (no `cnot`-invariance, failing at `idW` by K2Guard.lean:106,
  110, 134); `B3` (no self-duality).
- **What no outcome licenses.** A source for H2, H3 or A_miss; anything beyond two tokens; a discharge of H-Bell.
