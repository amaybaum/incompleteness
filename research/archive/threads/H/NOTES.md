# Thread H running notes (minimal field-neutral vocabulary for Naimark transport)

Certified main 6d0abf6b; worktree threads/H/wt (detached, read-only). KF = KInfFoundations.lean, OA =
OperationalAssembly.lean, NGB = NativeGateBall.lean. Line numbers at 6d0abf6b.

## 0. Read
- CHARTER.md (+ appended review protocol: typed formula e_x(s) = r(D(U(A(s, ρ_R)))), outcome classes O-*).
- F/LEDGER.md, G/REPORT.md, G/NOTES.md.
- KF full: §A FiniteStage KF:63; §B effects KF:116-150; PerfectlyDistinguishable KF:154 (field-neutral!);
  §C ElementaryDrivability KF:264, CopyNatural KF:284; §E' simplex/response KF:889-947; KInf1 KF:1013;
  ballEffect KF:1026.
- NGB:1-140. NB-1 composite rule in the module header: "two locally tomographic d-ball systems with their full
  self-dual effect cones ... G, G⁻¹ both sending product states into the MAXIMAL tensor cone". lorentz_of_effects
  NGB:105 quantifies over every unit b (full self-dual effects consumed as hypothesis).
- OA:594-800: FiniteOperationalTheory (matrix carriers A × Fin n, prepAvail_uniform, readout + readout_local,
  prepAvail_discard via discardWith/ptraceAnc). circuit_available OA:757.

## 1. Inventory (verified at 6d0abf6b)
- Field-neutral modules (no Matrix/ℂ): Averaging, BackgroundIndependence, C3Necessity, CanonicalMeasure,
  CombRealization, ControlledQuotient, EdgeRigidity, FactorUniqueness, FiniteEntropy, Finiteness, GaugeDimension,
  HiddenMemory, HomometricSix, HydroSourceAudit, IdempotentTrace, Irreducibility, LevelOneRecursion,
  PiccardBridge, Reciprocity, TasteBranching (+ KF, PassiveQuotient, Equivalence mostly). None has a composite of
  CONVEX BODIES. Affine/convex vocabulary only in KF, OrbitGeometryRigidity, PassiveQuotient, StochasticInterface.
- ONTIC (classical, field-neutral) Naimark ingredients are all landed: RevReal Eq:157 (V × Hid, step : Equiv,
  init law, product NOT required), RevReal.traj Eq:176 (readout at time k = visible factor of step^k: pullback of
  the readout along the dynamics), RevReal.law Eq:180 = marg FE:130 (discard), hiddenExt PQ:498 (controlled
  permutation on S × A), quotMeasure_branch PQ:410 (conditioning on a visible value).
- Matrix: tensorOf MC:193, conjChannel MC:360, localLuders OA:191, ptraceAnc OA:453, uniformAttach OA:492,
  pureAttach OA:500, discardWith OA:515, FiniteOperationalTheory OA:594 (availExt :599, prepAvail :626,
  prepAvail_uniform :630, readout :640, readout_avail :642, readout_local :643, prepAvail_discard :649),
  readout_is_localLuders OA:658, HasCompositeUnitaryControl OA:665, circuit_available OA:757,
  control_of_lieRank MicroscopicReversibility:114, TypedCompletion attachUniform :113 / discardR :129.
- Papers: substratum composes by products of configuration sets (Main.md:358 S = ∏ S_i; C_V × C_H).
  Main.md:540 SIC remark: sharp effect value 1/2 + √3/2 > 1 at an ontic vertex. Main.md:628: graph locality
  "does not alone establish ... local tomography, or one common tensor-product instrument category".
  Main.md:542: local tomography/composite completeness are reconstruction routes "only after their hypotheses are
  actually established". ROADMAP K2 composite OPEN; K1 uses product-to-max positivity only.

## 2. Key reasoning
- On the ball, "certain at x and zero somewhere" forces (1+x·r)/2 (β = 1/2). So sharpness = a PD pair (KF:154).
- Classical register: Ω ⊗ Δ_n is canonical (simplex factor: min = max); A, D, r definable with no choice
  (r = barycentric coordinate, not an effect-space quantifier). But Aut(L ⊕ L) is block-permuting (connected
  extreme-ray components), so the transported readout is constant. Vacuous.
- Non-classical register: rule not canonical. SWAP preserves min/QM/max, relocates the register's seed; CNOT/ZZ
  preserve QM only; CNOT-Naimark = seed ∘ g. The register adds nothing to the SHARP family.
- So composite is eliminable for the target; reduced formula e = r_vis ∘ g⁻¹ is typable in KF (affine map ∘
  AffineEquiv). Missing: the rule putting e ∘ g into avail (avail is an unconstrained parameter, F). The native
  seed = visible readout (ontic, landed; body image via P1). Ontic pullback along DYNAMICS is native (Eq:176) but
  substratum dynamics fixes the axis (substratum_residual SC:383); off-axis maps = K∞-R (out of scope).
- Outcome: O-FUNCT. First untypable arrow in the full formula: A.
- Pressure test of the favourable reduction: scope = rank-one sharp effects on the ball. In QM d ≥ 4, rank-2
  projectors need coarse-graining closure as well; unsharp (POVM) effects are where a register is genuinely
  needed. Neither is consumed by lorentz_of_effects.
- Disk (rebit): the construction itself works (SO(2) transitive, self-dual) and is excluded only at the drive
  antecedent (F: B6). Square: excluded at the drive antecedent (B5); with the finite Aut instead, a point seed
  fails COVER (3/4 at edge midpoints), an edge seed gives the gbit's own edge effects (SF fails, KF:726).

## 3. Script
- h_controls.py → `OK -- 62 checks, 12 written notes`; replay identical (rerun.out);
  sha256 85d9a11820d7ded43df04aea8678af12d1b5385dbb75d964ce01d0ddaa559605.
