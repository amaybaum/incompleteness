# Thread K — running notes (read-only, certified main 6d0abf6b)

Worktree: threads/K/wt at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a. Abbreviations: KF = KInfFoundations.lean,
SS = SubstratumSource.lean, SC = StructuralClosure.lean, SI = SubstratumInterface.lean, LA = LiftAudit.lean,
LRS = LieRankSource.lean, OR = OrbitReachability.lean, RS = ReachabilitySeam.lean, SOC = SecondOrderCircuit.lean,
SOD = SecondOrderDrive.lean. All under verification/lean-mathlib/OIBridge/.

## Identifiers re-verified at 6d0abf6b
- `ElementaryDrivability` KF:264 (fields D1–D9 KF:266–276); `ball3` KF:311; `rotFun` KF:351; `rot3` KF:411;
  `cycEquiv` KF:416, `cyc3` KF:425; `ball3Drive` KF:449 (flow rot3, t0 = π, J = cyc3, off-axis at t = π, x = e_z);
  `ball3_drivable` KF:490; `not_drivable_Icc` KF:529; `not_drivable_singleton` KF:564.
- Lemma B `eq_closedBall_of_frontier_subset_sphere` KF:770 (frontier in V topology, 0 ∈ interior).
- No other landed `ElementaryDrivability` instance or consumer outside KF (grep over *.lean): KF is a leaf.
- `DrivesElementary` SS:77; `QuantumArchitecture` SS:86; `fullClass_drivesElementary` SS:147.
- `IsMonomial` SI:75; `bijectiveOperator` SI:80; `phaseOperator` SI:83 (arbitrary d : S → ℂ).
- `substratumClass` SC:180; `bijectiveOperator_supplied` SC:330; `phaseOperator_supplied` SC:333;
  `substratumClass_not_drivesElementary` SC:370; `substratum_residual` SC:383.
- `transition` LRS:199; `phaseGate` LRS:209; `transition_hermitian` LRS:211; `perm_conj_transition` LRS:245;
  `phase_conj_transition` LRS:258; `bracket_XY` LRS:268; `ctrl` LRS:290; `ctrl_unitary` LRS:293;
  `hControl_star` LRS:352 : `HControl (transition i₀ j₁) (ctrl i₀)`.
- `flow` RS:95 (e^{-itH}); `generators` RS:130; `reachable` RS:136 (Subgroup.closure = abstract generated
  subgroup, not topological closure); `ExactReachability` RS:189.
- `exactReachability_of_hcontrol` OR:625 (hH Hermitian, hU unitary, HControl ⇒ ExactReachability).
- `HControl` MonoidalCompletion:349.
- `unit` SOC:356 = 1 + (e^{iπt} − 1)·(1 − g)/2; `permMat` SOC:710; `gateFlow` LA:47 = unit (permMat σ) t;
  `gateFlow_group` LA:75; `gateFlow_zero` LA:80; `gateFlow_one` LA:84; `gateFlow_half_entries` LA:138
  (entries (1+i)/2, (1−i)/2 in one column at t = 1/2 ⇒ not monomial).
- SOD header: the swap and shear layer flows are strongly continuous one-parameter groups of *-automorphisms
  of the quasilocal algebra; their composite is a continuous path, explicitly *not* a group.
- SI header: "It does not decide whether the continuous-time extension, the read-write coupling, or the
  gauge/phase structure supplies a non-monomial generator".

## Working log
1. Sub-question 1 on ball3Drive: cyc3 Rz(t) cyc3⁻¹ = Rx(t) (cyc3 e_z = e_x). Rz, Rx full circles ⇒ zxz Euler
   words give all of SO(3) as an abstract group (no closure). cyc3 has det +1, so G = SO(3) exactly.
   Transitivity word: Rz(φ+π/2) Rx(θ) e_z = (sinθ cosφ, sinθ sinφ, cosθ).
2. Every drive on ball3 (not just ball3Drive): affine bijections of the ball onto itself are O(3); continuous
   nontrivial one-parameter group ⇒ full circle about an axis a; off-axis ⇔ J a ∉ {±a}; two full circles with
   distinct axes generate SO(3) (cap argument, written). Continuity is load-bearing here: Hamel-basis flow
   t ↦ Rz(φ(t)), φ additive with φ(ℝ) = ℚπ, passes D1, D2, D4–D9 and fails only D3; generated group countable.
3. Abstract bodies: bidisk, cone over B³, B⁴ with SO(3)⊕1 drive — three countermodels with different strengths.
4. Dimension-3 classification: compact convex drivable body of affine dimension 3 is an ellipsoid (written).
5. Sourcing: substratum (monomial) group on the qubit Bloch ball keeps the z-axis up to sign ⇒ orbit of a pole is
   two points. The CT2 gate flow (LA:47) on Fin 2 is Rx(πt) on the Bloch ball; with the substratum's quarter phase
   as J it is off-axis, and with substratum phases it generates SO(3). The only non-substratum member is the gate
   flow at non-integer times (LA:138 at t = 1/2). ℂ is imported; no real one-parameter group of linear maps on
   ℝ^S passes through an odd permutation (det = square ≥ 0), continuity-free.
6. k_groups.py final: `OK -- 47 checks, 13 written notes`, sha256 a4820ca370c67da656f86de681fc1b35d2f8efa1a8de638dfe915a95afe908de.
   Pressure test of the favourable dimension-3 branch: each step (centroid fixed, compact closure orthogonal, flow image
   a full circle by D3, D9 ⇒ Ja ≠ ±a via J R_a(θ) J⁻¹ = R_{Ja}(det J·θ), cap argument, SO(3)-invariant convex ⇒ ball)
   rechecked; no premise beyond compactness, convexity, dimension 3 and the drive fields. Route caution recorded:
   NB-1's d ∈ {1,3} presupposes balls.
7. RESULT.md written. Worktree removed at the end.
