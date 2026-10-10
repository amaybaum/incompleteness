# Thread M — running notes (read-only; certified main 6d0abf6b)

Worktree `wt/` detached at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a (removed at the end). Python: sympy exact only,
`PYTHONDONTWRITEBYTECODE=1`. No Lean run, no repo edit.

## Inputs read
COMMON-LIMITS, M/CHARTER, PROTOCOL, SUMMARY; I, J, K, L RESULT.md (+ charters), L/OrbitGeneration.lean (§A–§F read in
full); background F/LEDGER.md, G/REPORT.md, H/RESULT.md with their charter dispositions.
Owner directions received mid-thread (both applied):
1. Keep G-AUT (body side: g, g⁻¹ map Ω into Ω) and V4′ (effect side: r∘g⁻¹ ∈ avail) as separate rows, checked
   separately in the quantum model. L's orbit equality uses P1 + K∞-R + G-AUT only; V4′ only adds availability.
2. Report SOURCED / OPEN / CIRCULAR for each of the four ingredients and each of the three traps
   (normalization, dimension 3, G-AUT/drive sourcing).

## Re-verified in the tree (6d0abf6b)
- NGB: `lorentz_of_effects` :105 (p a parameter, `1 ≤ p`); only kernel consumer `blocks_vanish` :149 (call at :164,
  hypothesis `2 ≤ p`) → `p_le_one` :176 → `nb1_kernel_core` :255. NGB and KF are leaf modules: imported only by
  `OIBridge.lean:245–246`; no other `.lean` mentions `ElementaryDrivability`, `KInfFoundations`, `NativeGateBall`.
- NB-1 prereg (theorem section): S4 runs the Lorentz test on `E₊ = ℝu ⊕ V₊`, `p = dim V₊`; S1, S2 and the S4 value
  identity are written proofs (exact d ≤ 7 / d = 5, 7). Hypotheses F, P±, Rt, Rc; full self-dual cones; LT composite;
  one common N. d = 3 positive control has p = q = 1 (S3 vacuous).
- KF: `FiniteStage` :63 (no stage maps anywhere; only KF uses it), `IsEffectOn` :116, `IsBoundaryState` :130,
  `SupportingEffectComplete` :135, `SingletonFaces` :139, `fullEffects` :149, `PerfectlyDistinguishable` :154,
  `isBoundaryState_of_certain_proper` :227, `ElementaryDrivability` :264 (fields :266–276), `CopyNatural` :284,
  `ball3` :311, `ball3Drive` :449, `ball3_drivable` :490, `not_drivable_Icc` :529, `not_drivable_singleton` :564,
  `card_le_two_of_centrallySymmetric` :632, Lemma B :770, `qubit_certain_face` :995, `KInf1` :1013,
  `ballEffect` :1026, `supportingEffectComplete_ball3` :1053, `kInf1_ball3_full` :1076, `not_kInf1_ball3_unit` :1089.
- SS: `DrivesElementary` :77, `QuantumArchitecture` :86, `genTheory_qm_of_quantumArchitecture` :136,
  `fullClass_quantumArchitecture` :151, `qm_generated_by_quantumArchitecture` :161.
- SC: `substratumClass` :180, `phaseOperator_supplied` :333, `substratumClass_not_drivesElementary` :370,
  `substratum_residual` :383, `substratum_plus_control_qm` :414 (the boxed GR §3.3 endpoint; census family 6 anchors
  Main.md `substratum_plus_control_qm`), `qm_generated_by_substratum_extension` :423.
- LiftAudit: `gateFlow` :47, `LayerFlowExecutable` :112, `layerFlowExecutable_of_control` :117,
  `substratumTheory_not_layerFlowExecutable` :200, **`derivedOI_qm_iff_layerFlowExecutable` :812** (matrix-level
  equivalence: under DerivedOI + SubstratumAvail, exact QM ⟺ one layer flow executable at every time).
- LevelOneSeam: `ExactAllFiniteEndomorphicQuantumOps` :186. OA: `availExt_bind` :617 (structure field),
  `readout_avail` :642, `readout_is_localLuders` :658, `circuit_available` :757. RT: `inclObs` :123,
  `trace_inclObs_mul_restrict` :190, `Consistent` :319, `consistent_mix` :341. RL: `inclObs` :102.
- ROADMAP P1 row :68 and K section :971–1032: final target "complex quantum kinematics in the conclusion rather than
  the premises"; K1 CONDITIONAL, K2 OPEN, K3 CONDITIONAL, K∞ OPEN. :997–999 still says the corrected singleton-face
  statement "is not frozen" although KINF-2 froze `SingletonFaces` (KF:139) — stale, as F said (flag only).
- Main.md :352 (route: classification conditional on five completion conditions; finite predictive rank of the
  completion not proved), :540 (SIC), :542 (completion must retain finite predictive dimension), :212/:628 (causal
  separation does not establish local tomography).
- Census: family 86 (NGB) and 87 (KF) both `kernel-only`, `manuscript: []`.

## Corrections / sharpenings of the inputs
- L: "the RHS is exactly what lorentz_of_effects consumes" is true for L's own new bridge `lorentz_of_seedOrbit`
  (p = 3, a single-ball self-duality statement). The corpus's only consumer is `blocks_vanish` at p = dim V₊ ≥ 2 on
  composite data, fed by `hpos`, which comes from P± through the written S4 value identity. In the d = 3 route the
  NB-1 consumption is at p = 1 and is not invoked.
- Coordinator remark that `preservesBody_drive` covers only `ball3Drive`: the draft (L:161) states it for any
  `D : ElementaryDrivability Ω`, but only for the generator set `range D.flow ∪ {D.J}`; closure under words is a
  written one-line induction, not drafted. Its premise is the drive itself, so G-AUT is sourced exactly as far as the
  drive is.
- K's named target `elementaryDrivability_of_substratum`: read with "substratum" = the current substratum class,
  its matrix shadow is refuted in the kernel (`substratum_residual`, `substratumTheory_not_layerFlowExecutable`).
  The drive can only come from an extension: the non-integer-time gate flow = `LayerFlowExecutable`. Field-neutral
  DRIVE is the shadow of the same residual that already closes the matrix-level equivalence (LiftAudit:812).
- J: DIM3 implies finite predictive rank (affine dim 3 ⇒ rank 4), so FR is not a separate open item in route A.
  The ambient ℓ^∞(E∞) is infinite-dimensional: restriction to aff Ω∞ is a needed typing step (written, cheap).
- New scope row ELEM: in QM the forward premises hold only for the capacity-two body read on the visible factor.
  Unscoped, K∞-R, DIM3 and the singleton-face principle are false in QM (qutrit; dilated block readout P₀⊗1).

## Exact layer
`m_checks.py` → `OK -- 50 checks, 0 failed, 8 written notes`; replay identical (`rerun.out`).
sha256 m_checks.py 599b6ced…bdcd2, m_checks.out 46c452e4…71fe. Two first-draft checks were vacuous (`1 < 2`, a table
restricted to itself); they were turned into written notes and two non-vacuity controls were added (N8d, Q2b-control).

## Pressure tests of favourable links (§A.31)
- K dim-3 ellipsoid: re-derived (Aut compact, centroid fixed, averaged inner product, flow = full circle by D3 + D9,
  J a ≠ ±a, two circles ⇒ SO(3) by the no-2-dim-subalgebra argument). Holds; written only (K-T4 costly).
- Normalization: free as a coordinate choice provided states, effects, drive, and (for NB-1) both copies and G are
  all pushed through T; the consumer itself is coordinate-bound (N8a/N8d). Cross-copy alignment is NOT free: it is
  copy covariance (N10).
- Reverse model: drive on ambient ℓ^∞(E∞) in QM exists via R ⊕ id on a closed complement of the 4-dim span; the
  coordinate-permutation extension would fail D3 (not norm-continuous). Written; no fatal.
- No forward premise of the scoped chain fails in the qubit model.
