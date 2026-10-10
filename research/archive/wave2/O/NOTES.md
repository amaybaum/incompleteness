# Thread O (DRIVE): working notes

Read-only against L = `f7f5c3b0c621cc3e4b57e3709d11d9d580c81149`, in the worktree `wave2/wt-O-drive`, which was
left clean (`git status` is empty). Paths are under `verification/lean-mathlib/OIBridge/`. No Lean or lake was run.
The exact checks are in `o_drive.py`, which prints `OK -- 52 checks, 0 failed`. A replay is byte-identical
(`rerun.out`). sha256 of the script is `61e5f4f2…cd148`, and of its output `8f5d6281…3406a`.

## Productivity test (fixed before the walk)

A finding counts as a gem only if both of the following hold:
- it is strictly stronger than the restatement "DRIVE is open and needs an extension of the substratum";
- it constrains a premise or the shape of the extension, or it exposes a hidden assumption in the current framing
  of DRIVE.

Anything weaker is recorded and not propagated.

## Depth-first branch log

Each node lists its question, how it was checked, and the verdict.

**N1. Which landed objects carry a continuous one-parameter flow?**
Checked by grep plus a read of every hit (inventory in RESULT §1).
Verdict: only the KF and OrbitNormalization objects are field-neutral, and they are definitions or controls on a
stipulated `ball3`. Every operational flow is typed over ℂ.
- N1a. Does `ElementaryDrivability` carry any availability content? Checked against KF:264–276: there is no
  `avail` field. Verdict: **no.** It is a property of the body alone. `ball3_drivable` (KF:490) holds with no
  operational input.
  Consequence (F2): on any route that fixes the Bloch body, the drive is free. The operational content enters
  OG-1 only through V4′.
- N1b. Does OG-1 consume `ElementaryDrivability` directly? Checked by reading OG:348–430 and OG:715.
  Verdict: **no.** It consumes a set G under `PreservesBody` and `BoundaryTransitive`. The drive enters only
  through `preservesBody_drive` (OG:161) and `preservesBody_driveWords` (ON:107).
- N1c. Does the substratum's own phase structure carry a continuous flow? Checked: `substratumClass` (SC:180) is
  `IsMonomial`, so it contains every diagonal unitary (`phaseOperator_supplied` SC:333, `diagonal_avail` LA:754).
  Verdict: **yes, under the round-62 interface reading.** The flow t ↦ diag(1, e^{it}) is available in
  `substratumTheory` and acts as Rz(t) on the Bloch ball (exact B1).
  - It satisfies D1–D8, with N = Z.
  - It fails D9 inside the substratum operations (exact B5), which is the group-level `substratum_residual`.
  - Under the stated-access reading it is absent: `permTheory_not_substratumAvail` (SubstratumInterfaceAudit:695).
    The interface audit records that the manuscripts call diagonal-unitary conjugation gauge
    (programmes/substratum/interface-audit.md:66–72).

**N2. What is the weakest resource that is not the conclusion in disguise?**
- N2a. Is a resource stated on Ω∞ (a continuous group of body automorphisms plus an off-axis J) anything more
  than fields D1–D9? Checked field by field. Verdict: **no**, it is definitional. A non-trivial statement needs
  operations upstream of the body (OPACT), and OPACT is absent from KF (KF header lines 6–9).
- N2b. Can OPACT be built stage by stage? Checked with `isEmpty_drivability_of_finite_orbits` (ON:124) and the
  fact that a polytope has finitely many automorphisms (written). Verdict: **no.** A continuous flow cannot
  preserve any finite stage. OPACT has to be defined on the completion, by effect transport, which needs SC∞
  and invariance of the effect set E∞.
- N2c. Matrix regime: is the gate-flow continuum irreducible? Checked with the exact identity
  gateFlow(levelPerm swap n, t) = M_n D_t M_n⁷ for M_n = mixImage n (π/4) (exact I0, I1 at n = 1, 2, 3) and with
  the Hadamard image (I2). Verdict: **no.**
  - Under `SubstratumAvail`, one fixed Clifford gate gives `LayerFlowExecutable`.
  - For any fixed non-monomial gate, the phase generator together with that gate spans su(2) (exact I4, I5); the
    monomial controls give rank 1 (I6).
  - **F1, NEW.** Favourable branch, so it was pressure-tested (N2c-i to N2c-iii).
  - N2c-i. Does it contradict `polarizedTheoryC_not_qm` (PolarizationClosure:620) or `fixedGateTheory_not_qm`
    (DC:1948)? Checked: both theories are countable up to scalar, so neither has `SubstratumAvail`. With F1, the
    kernel then forces `¬ SubstratumAvail` for both. This is consistent, and it gives two controls.
  - N2c-ii. Is `SubstratumAvail` sourced? Checked: no. It is a round-62 interface stipulation, which the
    observer-sourced theory fails (SubstratumInterfaceAudit:695). F1 relocates the continuum; it does not source it.
  - N2c-iii. Does F1 bear on the field-neutral body? Checked: no. Its body is the ℂ density-matrix body.
- N2d. Is the off-axis clause independent of the flow? Checked with B3–B6, D1–D5 and C5–C7.
  Verdict: **yes.** For monomial J, D9 against the gate flow holds iff the relative phase is non-real.
  - The ones-fixing theory has the whole gate flow (FlowEndpoint:87) and no off-axis element (exact D3).
  - The rebit has the pair flow and no off-axis element.
  - Kernel counterpart: `obligations_independent` (C5Discovery:59). **F3, ELABORATING.**

**N3. Dense versus exact availability.**
- N3a. Fixed-gate theory: a continuous t ↦ flow t x into a countable set is constant (written). A finitely
  generated linear group has no nontrivial divisible subgroup, so no additive hom ℝ → G exists at all
  (Malcev residual finiteness; citation).
  Kernel: `mixTheoryR_not_layerFlowExecutable` (SMC:673) and `countable_not_pairFlowSourced` (PFE:218).
- N3b. With limit closure (D3) and one infinite-order gate on a compact body, the closed group contains a
  continuous circle whose half-turn moves a state. This is written; it uses Cartan's closed-subgroup theorem and
  the torus structure (citation).
- **F4, ELABORATING.** It is the field-neutral form of DiscreteCompletion.

**N4. Typing.**
- N4a. Is the natural induced action on ℓ^∞(E∞) jointly continuous? Checked with exact E1: rational rotations
  R_n → id displace the indicator of one effect by 1 in sup norm. Verdict: **no.**
  - The drive has to be typed on the finite-dimensional chart (ON §D), or extended by R ⊕ id on a complement.
  - **F5, ELABORATING.** It sharpens M's remark about a coordinate-permutation extension.

**N5. Circularity.**
- N5a. Does any drive premise fix dimension 3? Checked: the B⁴ drive satisfies every field (exact F1–F3), and
  `boundaryTransitive_ball4` is kernel (ON:735). Verdict: **no.** CONFIRMING.
- N5b. Is any premise a substratum-only drive (the refuted route)? Checked: the continuum premise is always
  either an extension (GATEFLOW, FIXGATE + D3) or the interface phase stipulation (PHASEFLOW). The off-axis
  premise is always a non-monomial operation or a non-real phase. Verdict: **no.**
- N5c. Does the update path give a group? Checked: `driveQ` is a path (SecondOrderDrive:225, header). A toy
  composite of two involution flows is not a group (exact H1). Verdict: **no.** BORDERLINE.

**Fixed point.** The passes N3, N4 and N5 produced no NEW finding after F1 and F2. There were three consecutive
passes without a NEW finding, so the walk stopped.

## Identifiers checked at L (file:line)

KF:
- `ElementaryDrivability` :264; `ball3Drive` :449; `ball3_drivable` :490; `not_drivable_Icc` :529.

OG:
- `preservesBody_drive` :161; `seedOrbit_ball3_eq` :348; `ballEffect_mem_avail` :369; `lorentz_of_available` :422;
  `orbit_generation_core` :715.

ON:
- `preservesBody_driveWords` :107; `isEmpty_drivability_of_finite_orbits` :124; `seedOrbit_eq_of_normalization` :307;
  `hypotheses_restrict` :529; `driveWords3` :571; `boundaryTransitive_ball3Drive` :667; `boundaryTransitive_ball4` :735.

LA:
- `gateFlow` :47; `LayerFlowExecutable` :112; `layerFlowExecutable_of_control` :117;
  `substratumTheory_not_layerFlowExecutable` :200; `SubstratumAvail` :745; `substratumTheory_substratumAvail` :750;
  `diagonal_avail` :754; `avail_conj_mul` :770; `derivedOI_qm_iff_layerFlowExecutable` :812.

SS:
- `DrivesElementary` :77; `QuantumArchitecture` :86; `genTheory_qm_of_quantumArchitecture` :136;
  `fullClass_drivesElementary` :147.

SC:
- `substratumClass` :180; `phaseOperator_supplied` :333; `substratumClass_not_drivesElementary` :370;
  `substratum_residual` :383; `ExtendsSubstratum` :401; `substratum_plus_control_qm` :414.

DC:
- `FixedGateSourced` :34; `DenseUnitaryControl` :45; `ClosureAvail` :63; `dense_angles` :518;
  `fixedGateTheory` :1926; `fixedGateTheory_derivedOI` :1929; `fixedGateTheory_fixedGateSourced` :1933;
  `fixedGateTheory_denseUnitaryControl` :1942; `fixedGateTheory_not_qm` :1948.

SMC:
- `rot` :45; `mixImage` :50; `MixR` :56; `MixC` :72; `mixImage_unitary` :152; `mixTheory_qm` :511;
  `mixR_countable_upToScalar` :662; `mixTheoryR_not_layerFlowExecutable` :673.

RPF / PFE:
- `PairFlow` RPF:41; `PairFlowSourced` PFE:48; `qm_iff_derivedOI_pairFlowSourced` PFE:199;
  `countable_not_pairFlowSourced` PFE:218.

SecondOrderCircuit:
- `unit` :356; `flow` :432; `drive` :635.

SwapLayer:
- `swapU` :95; `swapQ` :372; `continuous_swapQ_time` :446; `swapQ_add_time` :494.

SecondOrderLayer:
- `layerQ` :675; `layerQ_add_time` :966.

SecondOrderDrive:
- `driveQ` :135; `driveQ_isContinuousPath` :225; `driveQ_one_eq_heisQ` :829.

ReachabilitySeam / OrbitReachability:
- `flow` RS:95; `exactReachability_of_hcontrol` OR:625.

ReadWriteControl:
- `ReadWriteFamily` :86 (`couple` :87); `readWriteSourced_not_qm` :174.

FlowEndpoint:
- `onesTheory_layerFlowExecutable` :87; `onesTheory_not_phasesAvailable` :177.

C5Discovery:
- `obligations_independent` :59; `gateFlow_half_eq_hsh` :287.

PolarizationClosure:
- `polarizedTheoryC_derivedOI` :606; `polarizedTheoryC_not_qm` :620.

PhaseSource:
- `permTheory_not_phasesAvailable_onesFixing` :104; `substratumClass_not_onesFixing` :196.

SubstratumInterfaceAudit:
- `permClass` :236; `permTheory_not_substratumAvail` :695.

RouteB:
- `PhasesAvailable` :128; `DerivedOI` :141; `substratumTheory` :279; `substratumTheory_derivedOI` :290.

OA:
- `HasCompositeUnitaryControl` :665; `circuit_available` :757.

CoherentContinuumSource:
- `gateFlow_not_monomial` :74; `substratumClass_not_countablyCovered` :235.

DerivedQ3:
- `derivedOI_layerFlowExecutable_one_not_phaseFree` :294.

## Background re-verified (threads G, K, M)

- K §3: the ℂ assembly (gate flow, quarter phase as J, swap as N) is a transitive drive. Re-checked exactly
  (A5, B6, G1–G3).
  - Correction: K calls the non-integer gate times "the one unsourced ingredient". That holds under the interface
    reading with the gate flow as the continuum. Under the same reading one fixed Clifford gate suffices (F1).
  - Under the stated-access reading the quarter phase is unsourced as well (PhaseSource:104), so there are two
    ingredients.
- M row K2a (DRIVE = field-neutral `LayerFlowExecutable`): confirmed as the matrix shadow. F1 shows that, relative
  to `SubstratumAvail`, the shadow reduces to `FixedGateSourced (π/4)`.
- G result 5 (monomial unitaries keep the z-axis up to sign): confirmed (B5).
