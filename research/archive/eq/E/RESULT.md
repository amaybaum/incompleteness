# EQ-E — RESULT: the converse direction and global consistency (EQUIV-CLOSE)

Research only; nothing here is adopted, frozen or governed. Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`
at `scratchpad/eq/base/` (read-only). Every `file:line` below is at the base, under
`verification/lean-mathlib/OIBridge/` unless another path is given. Scripts and outputs are in `scratchpad/eq/E/`:
`common.py`, `s1_stage_act.py`, `s3_scope_qutrit.py`, `s4_not_pairs.py`, `s5_pauli_adapter.py`, `s6_gate_class.py`,
`s7_k2_composite.py`, `s8_one_model.py`, `qe2_graph.py`, each with its `.out`. `run_all.py` replays all eight and compares
each output byte for byte: `run_all: OK`, 111 checks, 0 failed. All arithmetic is sympy-exact: rationals, Gaussian
rationals and symbolic trigonometric identities, with no floating point. Three first-run failures came from my test
harness, not the mathematics: a mis-specified expected gate in s4, and Python ints in s1 and s7. Each is recorded in
`NOTES.md`, and the run-1 outputs are kept. No Lean was run. All Lean text below is UNBUILT.

## 1. Finding

Under one explicit identification ι_Q of OI's stages, horizons, bodies, operations, copies and carriers with
finite-dimensional complex quantum theory (QM), every premise of the current forward route holds in QM at the
elementary (qubit) scope. One two-qubit model, M_Q, carries all of them at once, so no two landed premises are
incompatible as stated. The converse is therefore a theorem route at the elementary scope, with these witnesses:
- **Kernel-witnessed:** K1, endomorphic K3, and the ball-side K∞ premises.
- **Exact or written:** K∞-Stage, K∞-Act, K2 and the identification itself.
- **No kernel witness:** typed K3. The only `TypedOperationalTheory` in the kernel is the non-quantum control `typedDiag`
  (TypedCompletion:916).

The substance of QE1 is the list of readings and identifications under which QM does **not** satisfy a premise, each
with an exact witness:
- **(i) Scope.** K∞-Trans and K∞-Geom fail on the qutrit for every family G. The formalized K∞-Stage predicates hold on
  the qutrit too, so they do not mark out the elementary scope. "Capacity two" does, and holds exactly at n = 2 in QM.
- **(ii) Stage towers.** K∞-Act holds only on a stage tower whose effects are informationally complete (IC). A
  fixed-basis observer's horizon tower completes to the classical bit.
- **(iii) K∞-Copy.** The quantum CNOT's NOT relations do not force the two copies' NOTs to agree. (Ad_Y, Ad_X)
  satisfies both relations, and the solutions form a circle. K∞-Copy therefore holds in QM only in its existential form.
  Its candidate weakening, type covariance, holds in QM and fails on both recorded non-quantum survivors.
- **(iv) The native gate.** DIM-1's NOT relations hold only on the family CNOT·diag(1,1,u,ū)·(I⊗Z)^k (one parameter, two
  branches). The quantum gates whose conjugation acts as the classical CNOT on the corner states (the "CNOT-frame" gates)
  form a three-parameter class, and the relations fail with every linear NOT for gates such as (S⊗I)·CNOT.
- **(v) Countable towers.** Exact K∞-Trans together with K∞-V4 forces an uncountable available-effect family. The
  available effects therefore cannot be the stage effects of a countably indexed tower. The dense form, witnessed by
  QM's rational rotations, is the consistent choice; the kernel's own dense witness uses reflections, which QM excludes.

QE2 finds the kernel route disconnected:
- The K∞ block (`sharpSeed_completion`, `chartBody_eq_eball`, `hypotheses_tr`, `preservesBody_inducedEquiv`) has no
  consumer outside its own module.
- `ElementaryDrivability` and `CopyNatural` are read by no theorem on the path to d = 3.
- The landed control drive's NOT is Ad_Z, not DIM-1's Ad_X.

QE4's incompatibilities all involve a premise read outside M_Q's choices. The sharpest: cnot and its one-copy-reflected
conjugate T″ = (I⊗reflY)·cnot·(I⊗reflY) both satisfy every K1 premise with the same z and N, yet admit no common K2Guard
candidate cone.

## 2. Evidence level

**Table A: QE1, premise by premise.** "QM?" is the verdict under ι_Q. ι_Q is fixed in `NOTES.md` §N1.1 and summarized
here:
- elementary system ↔ ℂ²;
- body ↔ Bloch ball, via Pauli expectation coordinates (the kernel's `hom`);
- G ↔ PU(2) acting by conjugation, which is SO(3) on the ball;
- available effects ↔ all 0 ≤ E ≤ I;
- copies ↔ ℂ²⊗ℂ²;
- W 3 ↔ the coefficient matrix ω_{μν} = tr(ρ σ_μ⊗σ_ν);
- stage ↔ (horizon, instrument menu) with Born tables;
- K3 carriers ↔ `Matrix S S ℂ` with the full implementation class.

| premise (kernel object) | QM? | scope in QM | identification it needs | evidence |
|---|---|---|---|---|
| K∞-Stage: `SCInf` StageCompletion:78, `BinaryVisible` SC:244, `FiniteRank` SC:299 | yes | every n, including the qutrit (rank 8), so it does **not** delimit the elementary scope | stages = (horizon, menu); forward maps = inclusions or marginals | exact, s1 |
| elementary scope (no predicate exists) | proposal: capacity two | exactly n = 2 | perfect distinguishability with the available effects | kernel Lemma D `card_le_two_of_centrallySymmetric` KInfFoundations:632; exact, s1 (qutrit capacity 3) |
| horizons | SCInf as marginal consistency, horizons 1→2→3 | — | fixed-basis tower gives rank 1 (d = 1); a 3-context menu gives rank 3 | exact, s1 |
| K∞-Act: `OpDatum` CompletionAction:46, `AffineRespect` CA:58, inverse datum | yes on IC towers; **StateRespect fails** on a Z-only tower (Hadamard) | every n | IC stage effects on the system | exact, s1 |
| K∞-Drive: `ElementaryDrivability` KF:264 | yes | n ≥ 2: qubit kernel `ball3Drive` KF:449; qutrit exact. Not elementary-scoped | — | kernel and exact, s3 |
| K∞-Trans: `BoundaryTransitive` OrbitGeneration:79, dense form `DenseBoundaryOrbit` DenseOrbit:53 | n = 2: yes, with SO(3) words, `boundaryTransitive_ball3Drive` OrbitNormalization:667 and `eball_three` TransitiveBody:671. n ≥ 3: **no, for every G** | elementary | G orientation-preserving | kernel; exact s3: diag(½,½,0) is a boundary state that is not extreme, so `not_boundaryTransitive_of_nonextreme_boundary` TB:301 applies |
| K∞-Seed: `SharpSeed` OG:65 | yes | every n | rank-one projector; stage source `sharpSeed_completion` SC:224 | exact, s1 |
| K∞-V4: `SeedOrbitAvailable` OG:74 | yes | every n | exact form: available = all effects; dense form: available = rational stage effects | written; exact s8 |
| effect soundness `EffectsOn` EffectSpace:567; 0 < d | yes (d = 3) | — | 0 ≤ E ≤ I ↔ \|v\| ≤ min(a, 1−a) | exact s5 (characteristic polynomial) |
| K∞-Copy: the single N in `IsNot` CompositeDimension:210 and `NativeGate` CD:218; `CopyNatural` KF:284 | ∃ a common N: yes (Ad_X). "The NOTs compatible with the gate agree": **no** | — | canonical ℂ²≅ℂ² | exact s4: the solutions are N_B = Ad_X, N_A ∈ {π-rotations about horizontal axes} |
| type covariance (ROADMAP candidate weakening) | yes: N_A = R_z(φ) N_B R_z(φ)⁻¹, with R_z(φ) a unitary | — | g = Ad diag(1, e^{iφ}) | exact s4 (symbolic); foils C2N (d = 5) and d = 7 fail it |
| K∞-Geom: `SingletonFaces` KF:139, `RelStrictConvex` KF:144 | n = 2: yes (`singletonFaces_closedBall` KF:658). n ≥ 3: no | elementary (already recorded) | — | kernel; exact s3 |
| K1: `IsNot`, `NativeGate`/`NativeGateOf` K1Bridge:49, `EntanglingOf` K1B:64, `2 ≤ d` (`HasTwoSharpTests` SharpTests:41) | yes, for (z3, Ad_X, CNOT, Φ⁺) | two qubits | kernel `cnot` = transfer matrix of the quantum CNOT; `nflip` = Ad_X; `phiW` = Φ⁺ | kernel `isNot_nflip` CD:838, `nativeGate_cnot` CD:1160, `entangling_cnot` CD:1380, `hasTwoSharpTests_of_two_le` ST:137; exact s5 |
| scope of the NOT relations among CNOT-frame gates | **only** CNOT·diag(1,1,u,ū)·(I⊗Z)^k. Witness (S⊗I)·CNOT: frame, positivity and entangling all hold, and **no** NOT pair exists | — | the native gate must be an aligned representative | exact s6 (64-gate grid plus a symbolic all-phase solve, via `piRotation_three` ParityNot:161) |
| K2: local tomography (encoded by `W d` CD:97), composite cone, local actions | yes: Pauli products have rank 16; the quantum cone is a `CandidateCone` (K2Guard:95) invariant under cnot and local rotations | — | local group without reflections | exact s7; foil: real QM fails local tomography |
| Kₙ (no predicate) | yes | every n; each ℂⁿ is a face of (ℂ²)^{⊗k} | — | written |
| K3: `QuantumArchitecture` SubstratumSource:86, `OIPlus` CarrierGeneralOIPlus:185, `ShadowQuantum` TypedCompletion:291 | yes | every carrier | `fullClass` | kernel `fullClass_quantumArchitecture` SS:151, `qm_generated_by_quantumArchitecture` SS:161, `oiPlus_of_qm` CGOP:198, `fullQuantum_exactAll` IsometryExtension:231. Typed: written only |
| sealed OI core | yes, on the qubit carrier | `FiniteOperationalTheory (Fin 2)` | — | kernel `qm_implies_oiCore` CompletedOI:549 |
| OI with a fixed finite substratum (A1) | exactly: no. To every finite accuracy: yes | holds for completions, not for a fixed stage | — | kernel F2 `classical_exposed_ncard_le` KF:947 and `FiniteStage.exposed_le_card` KF:868; papers/Main.md §3.4 (already recorded) |

**Table B: other claims.**

| claim | evidence level |
|---|---|
| the kernel `cnot` (CD:741–786) is the Pauli transfer matrix of the quantum CNOT (control = first factor); `nflip` = Ad_X; `phiW` = CNOT(\|+⟩\|0⟩); `prodState`, `sharpEff` and `prodEffVal` are Born values; `reflY` is the transpose | exact, s5 (22 checks; two countercontrols fail as required) |
| K2Guard's obstruction (`no_candidateCone_cnot_reflY` K2G:143) is the non-positivity of the partial transpose: the chain value −½ is reproduced through ι_Q | exact, s7 |
| the landed control drive's NOT `rot3 π` is Ad_Z, which fixes z3; a drive about the first axis aligns with DIM-1's NOT (R_x(π) = `nflip`, with J = `cyc3` off axis) | exact, s3 |
| the kernel route is disconnected (Section 5.2) | grep extraction, `qe2_graph.out` |
| no `TypedOperationalTheory` instance exists except `typedDiag` TC:916 | grep at the base |
| COMP-1's `Carrier d d` (CompositeInterface:579) is definitionally DIM-1's `W d`, and `pState` CI:633 = `prodState` CD:161 | reading of the definitions |
| the NOT-conjugacy reduction: two-NOT relations with frame-conjugate NOTs give a common-NOT native gate | written proof (Section 4, T2); exact on the QM instance, s4 |

**Literature bearing on the question.** All entries are unverified: no source was fetched, and no theorem numbers were
checked.
- Masanes–Müller–Augusiak–Pérez-García, *PNAS* 110 (2013) 16373: d = 3 for locally tomographic balls with a continuous
  reversible interaction. This is DIM-1's nearest relative.
- Masanes–Müller, *NJP* 13 (2011) 063001.
- de la Torre–Masanes–Short–Müller, *PRL* 109 (2012) 090403.
- Barnum–Müller–Ududec, *NJP* 16 (2014) 123029.
- Peres, *PRL* 77 (1996) 1413, and the Horodeckis (1996): positivity of the partial transpose, the content of K2Guard.
- Hardy–Wootters, *Found. Phys.* 42 (2012) 454: real QM fails local tomography.

## 3. Countermodels and controls

Every decision rule was written into the script header before the script was run.

**K1 identification (s5).**
- Positive control: the kernel table equals the quantum CNOT.
- Countercontrols, both failing as required: the CNOT with control and target exchanged, and the kernel table with one
  sign flipped.

**K∞-Copy (s4).**
- Control: the common N, Ad_X.
- Countercontrols: the z-reflection and −id both fail relC.
- Witness of non-agreement: (Ad_Y, Ad_X), with N_A ≠ N_B.
- Foils for type covariance: NB-1's C2N pair at d = 5 (homogenized +1 multiplicities 3 vs 2) and the K∞ d = 7 pair (4 vs
  2). Neither pair is conjugate, so type covariance excludes both.
- Reduction instance: T̃ = (I⊗R_z(π/2)⁻¹)·cnot·(I⊗R_z(π/2)) is the quantum gate \|0⟩⟨0\|⊗I − \|1⟩⟨1\|⊗Y, with common NOT
  Ad_Y. The gate \|0⟩⟨0\|⊗I + \|1⟩⟨1\|⊗Y is kept as a countercontrol; it differs by Z⊗I.

**Native-gate scope (s6).**
- Control: D = I admits Ad_X.
- Over the 64 Clifford-phase gates CNOT·D: 8 admit a common NOT (Ad_X or Ad_Y), 56 admit no NOT pair at all over every
  linear map of ℝ³, and none admits a two-NOT pair only.
- The irrational-phase member u = (3+4i)/5 has common NOT [[−7/25, 24/25, 0], [24/25, 7/25, 0], [0, 0, −1]].
- The symbolic all-phase solve returns exactly the four sign branches of CNOT·diag(1, λ, μw, μλ/w).

**K∞-Stage and K∞-Act (s1).**
- Qubit tower: 30 rational Bloch vectors in three nested stages.
- Qutrit tower: 9 IC projectors; it passes all three formalized predicates. This is the scope countercontrol.
- Non-IC Z-only tower: StateRespect fails for a unitary.
- Fixed-basis horizon tower: rank 1.
- The transpose passes AffineRespect, so K∞-Act alone admits antiunitary maps.

**Scope (s3).**
- Qutrit: a non-extreme boundary state, and SingletonFaces fails.
- Qutrit ElementaryDrivability: the flow law U(s)U(t) = U(s+t) holds symbolically, there is an involution at π, and J is
  off axis.
- Qubit controls: the kernel's drive, and the aligned drive.
- Product of two rational reflections: a rational rotation (det +1) mapping z3 to (2/3, 1/3, 2/3).

**K2 (s7).**
- Foil: real QM's I/4 and (I + Y⊗Y)/4 agree on every product of real local effects.
- Partial transpose of Φ⁺: eigenvalue −½.
- With `nflip` in place of `reflY`, the chain value is 0.

**One model and charts (s8).**
- Global transpose maps cnot to cnot.
- T″ satisfies the frame and both relations, yet T″(\|+⟩\|0⟩) = PT(Φ⁺).
- T″(cnot(prodState xplus z3)) pairs −½ with sharp(−e₁)⊗sharp(−e₃), so it lies outside maxCone.
- The qutrit's certain effect diag(1,1,0) restricts to the unit of the qubit face.

**Determinism.** `run_all.py` replays all eight scripts exactly.

## 4. Proposed next theorems

### 4.1 The two-way statement (QE3), two directions witnessed separately (§A.34)

**Data.**
- An *elementary datum*: a directed stage system `D`, a completion chart `C` with `C.d = d`, a set `G` of affine
  automorphisms of the chart, an available family `avail`, and a seed `r`.
- A *two-copy datum* (z, N_A, N_B, T) with `T : W d ≃ₗ[ℝ] W d`.

**Forward (F).** The route, with each premise labelled.

- **F1, chart → ball.** `SCInf D`, `FiniteRank (body D)`, `PreservesBody (chartBody C) G`, and
  `BoundaryTransitive (chartBody C) G` (or `DenseBoundaryOrbit`) give an affine `A` with `A '' chartBody C = eball d`.
  The transported data `(conjTr A '' G, effTr A r, effTr A '' avail)` then satisfy the four OG-1 hypotheses on `eball d`.
  - Status: kernel pieces exist (`chartBody_eq_eball` TB:651 or DO:209, `hypotheses_tr` OrbitNormalization:295,
    `hypotheses_restrict` ON:529, `sharpSeed_completion` SC:224).
  - Missing: the composition. That is adapter T5.
- **F2, ball + gate → d = 3.** `EffectsOn (eball d) avail`, the four OG-1 hypotheses, `IsNot (eball d) z N_A`, a
  two-NOT native gate, **type covariance** (N_B = g N_A g⁻¹ with g a linear ball automorphism fixing z), and `2 ≤ d`
  (⟺ `HasTwoSharpTests (eball d)`, ST:155) together give d = 3.
  - Status: kernel `three_of_nativeGate_of_two_le` K2Guard:234 (relative form K2G:253, dense form DO:317), through T2.
- **F3, the composite is the quantum one.** OPEN (K2). There is no statement in the kernel.
- **F4, every finite carrier.** OPEN (Kₙ). No predicate exists.
- **F5, operations.** Kernel: `genTheory_qm_of_quantumArchitecture` SS:136, `typed_determined_iff` TC:850,
  `oiPlus_iff_qm` CGOP:207.

Premise labels:
- *Independently assumed:* SCInf, FiniteRank, BinaryVisible (not consumed on the d = 3 path), K∞-Trans in its exact or
  dense form, K∞-V4, EffectsOn, IsNot, the native-gate clauses (relT is not needed: `dim_of_ctrlGate` RelcSelectBlock:739),
  type covariance, `2 ≤ d`, and QuantumArchitecture.
- *Proved from earlier premises:* K∞-Seed from SCInf plus a sharp stage pair (SC:224), up to the restriction seam.
- *Not consumed:* K∞-Act (only a source of `PreservesBody`), K∞-Drive (no consumer), and K∞-Geom (not on the d = 3 path).
- *Missing:* the elementary-scope predicate (proposal T4), K2, Kₙ, and the adapters T5 and T7.

**Converse (C).** For the finite-dimensional complex quantum theory on ℂⁿ, with every instrument available, read
through ι_Q:
- **C1.** K∞-Stage and K∞-Act hold for every n on IC towers (exact).
- **C2.** At capacity two (n = 2): K∞-Trans in both forms, K∞-Seed, K∞-V4, EffectsOn, K∞-Geom, K∞-Drive and
  `HasTwoSharpTests` hold (kernel and exact).
- **C3.** On two qubits: `IsNot`, `NativeGate`/`NativeGateOf` (with common NOT, hence type covariance) and
  `EntanglingOf` hold (kernel and exact). This is T1.
- **C4.** The K2 premises hold (exact and written).
- **C5.** Kₙ holds trivially.
- **C6.** K3 holds: kernel at the endomorphic level, written at the typed level (T3).
- **C7.** The sealed OI core holds on `Fin 2` (kernel). OI holds as completions of stage towers, not as a fixed finite
  substratum.

Readings that QM **violates**, and which the statement therefore excludes:
- K∞-Copy as agreement of all gate-compatible NOTs;
- "every CNOT-frame gate satisfies the relations";
- K∞-Trans or K∞-Geom imposed at capacity at least 3, or on the scope `BinaryVisible ∧ SCInf ∧ FiniteRank`;
- exact K∞-Trans with available effects equal to the stage effects of a countable tower;
- K∞-Act on non-IC towers;
- "every gate meeting the native-gate hypotheses is available" (I1 in Section 6).

**How this differs from `oiPlus_iff_qm`.** `oiPlus_iff_qm` (CGOP:207) is one fully proved biconditional on a
`FiniteOperationalTheory A` over `Matrix A A ℂ`. Both of its sides presuppose complex matrix kinematics.

In the proposal:
1. The directions are separate, each with its own witnesses.
2. F starts from field-neutral data: stage towers, convex bodies, affine effects, and a real bilinear two-copy carrier.
   It reaches complex kinematics only through the named open links F3 and F4, so F is conditional on two missing
   theorems.
3. C concerns QM models under the explicit ι_Q, and claims each elementary-scoped premise only at capacity two.
4. `oiPlus_iff_qm` appears only as the last segment, F5 and C6.

### 4.2 Candidate theorems

**T1. `k1_quantum_witness`.** Converse; Lean, UNBUILT. Composable from landed lemmas.
```lean
theorem k1_quantum_witness :
    EffectsOn (eball 3) (fullEffects (eball 3)) ∧ PreservesBody (eball 3) driveWords3 ∧
    SharpSeed (eball 3) (sharpEff z3) ∧ BoundaryTransitive (eball 3) driveWords3 ∧
    SeedOrbitAvailable driveWords3 (sharpEff z3) (fullEffects (eball 3)) ∧
    IsNot (eball 3) z3 nflip ∧ NativeGateOf (eball 3) (fullEffects (eball 3)) z3 nflip cnot ∧
    EntanglingOf (eball 3) (fullEffects (eball 3)) cnot ∧ HasTwoSharpTests (eball 3) ∧
    ∀ g ∈ driveWords3, LinearMap.det g.linear = 1
-- from eball_three ▸ (preservesBody_driveWords3 ON:674, boundaryTransitive_ball3Drive ON:667), sharpEff_sharpSeed
-- ES:118, isEffectOn_seedTransport OG:94, isNot_nflip, maxConeOf_fullEffects ES:415 ▸ nativeGate_cnot,
-- jointStatesOf_eq K1B:88 ▸ entangling_cnot, hasTwoSharpTests_of_two_le ST:137; det of rot3 t and cyc3 is 1.
```
The last conjunct makes the witness compatible with K2Guard. The landed d = 1 analogue,
`two_le_load_bearing_relative` ST:185, uses `fullAut`, which contains reflections.

**T2. `nativeGate_of_typeCovariant` (the NOT-conjugacy reduction).** Forward; Lean, UNBUILT; written proof below.
```lean
-- TwoNotGate Ω z NA NB G: frame, posFwd, posInv (maxCone Ω), relT with NB, relC: actC NA (G (actC NA ω)) = actT NB (G ω)
theorem nativeGate_of_typeCovariant {g : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ)} (hgz : g z = z)
    (hgΩ : ∀ x, x ∈ eball d ↔ g x ∈ eball d) (hconj : ∀ x, NB (g x) = g (NA x))
    (hG : TwoNotGate (eball d) z NA NB G) :
    NativeGate (eball d) z NA (((actTEquiv g).trans G).trans (actTEquiv g).symm)
```
*Proof.* Write T̃ = actT g⁻¹ ∘ G ∘ actT g.
- relT: NA·g⁻¹ = g⁻¹·NB, so T̃ meets relT with NA.
- relC: actC and actT commute, and g⁻¹·NB·g = NA, so T̃ meets relC with NA.
- Frame: g fixes ±z, so g fixes each corner and the frame of G passes to T̃.
- Positivity: g and g⁻¹ preserve the ball, so `actT g` and `actT g⁻¹` preserve maxCone and carry product states to
  product states.

Corollary: `IsNot (eball d) z NA`, together with these hypotheses, gives d = 1 ∨ d = 3 by `dim_of_nativeGate` CD:2723. QM
satisfies the hypotheses (s4). The NB-1 and K∞ survivors violate type covariance (s4).

**T3. `typedKraus_theory`.** Converse; Lean, UNBUILT. Define a `TypedOperationalTheory` whose `availT` is
`IsTypedKrausInstrument` (TC:448), verify the closure rules (id, coarse, bind, relabel, attach, discard, readout), and
prove its `ShadowQuantum` through `typed_determined_iff`. This would be the missing typed-level converse witness. Its
written proof is standard.

**T4. Capacity-two scope.** Converse and scope; written plus exact.
- Definition: `Capacity2 Ω avail` means some pair of states is perfectly distinguishable by available effects (KF
  `PerfectlyDistinguishable`) and no triple is.
- Claim: in QM, Capacity2 holds ⟺ n = 2 (written; exact s1 for n = 3).
- Claim: under ι_Q, K∞-Trans and K∞-Geom hold on every capacity-two QM system.
- Foils: the square gbit is capacity two (Lemma D) and fails K∞-Trans (TRB-1 §G). The classical bit fails `2 ≤ d`
  (ST:197).

**T5. `chart_to_eball_hypotheses`.** Forward adapter; Lean, UNBUILT. Compose `chartBody_eq_eball`, `hypotheses_tr`,
`isEffectOn_tr` (ON:217) and `sharpSeed_restrict` / `hypotheses_restrict` into one statement, so that K∞-Stage's seed
and the chart family reach the hypotheses of `dim_of_nativeGateOf`.

**T6. `cnotFrame_relations_iff`.** Converse scope; exact layer, certified symbolically in s6. A quantum gate U whose
conjugation acts as the classical CNOT on the z-corners admits a linear N with `IsNot` and both relations iff
U ∝ CNOT·diag(1,1,u,ū)·(I⊗Z)^k with |u| = 1 and k ∈ {0,1}. N is then the π-rotation about the horizontal axis at angle
arg(±u). Companion statement, `twoNot_cnot_circle` (exact, s4): for the quantum CNOT, the pairs satisfying relT(N_B) and
relC(N_A, N_B) are exactly N_B = Ad_X with N_A = [[c, s, 0], [s, −c, 0], [0, 0, −1]], c² + s² = 1.

**T7. `pauli_adapter`.** Kₙ at n = 2; Lean, UNBUILT. ω ↦ Σ ω_{μν} σ_μ⊗σ_ν / 4 is a linear isomorphism from `W 3` onto
the Hermitian elements of `Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ`. It carries `prodState`, `prodEffVal`, `cnot` and
`nflip` to the tensor product of states, the Born pairing, Ad_CNOT and Ad_X (exact s5). It also carries
`jointStates (eball 3)` onto a set strictly larger than the PSD set, which is why K2 remains needed.

## 5. Dependencies

### 5.1 QE2: dependency graph

`qe2_graph.out` gives the location, header and consumers of every declaration.

```
K∞-Stage   SCInf SC:78, FiniteRank SC:299, BinaryVisible SC:244 ─► sharpSeed_completion SC:224   [no consumer]
           FiniteRank ─► exists_chart_of_finiteRank SC:304 ─► CompletionChart CA:144 ─► chartBody CA:166
K∞-Act     OpDatum+AffineRespect+Undoes ─► preservesBody_inducedEquiv CA:352                       [no consumer]
K∞-Trans   PreservesBody+BoundaryTransitive on chartBody ─► chartBody_eq_eball TB:651 (dense DO:209) [no consumer]
           exists_affine_image_eq_eball TB:602 (compact, convex, interior, PreservesBody, BoundaryTransitive, 0<d)
transport  hypotheses_tr ON:295, hypotheses_restrict ON:529, isEffectOn_tr ON:217                   [no consumer on route]
seed orbit seedOrbit_ball3_eq OG:348 (PreservesBody, SharpSeed, BoundaryTransitive on ball3), eball_three TB:671
EFF-1      sharpFamily_subset_avail ES:374 ─► maxConeOf_avail_eq ES:572 (0<d, PreservesBody, SharpSeed,
           BoundaryTransitive, SeedOrbitAvailable, EffectsOn) ─► K1Bridge nativeGate_of_avail K1B:108
K1         dim_of_nativeGateOf K1B:128, three_of_nativeGateOf K1B:138 ─► dim_of_nativeGate CD:2723 (IsNot, NativeGate),
           three_of_nativeGate CD:2748 (+Entangling); dense DO:299/307; 2≤d form K2G:253 (← HasTwoSharpTests ST:155,
           no composition); CtrlGate form dim_of_ctrlGate RSB:739, three_of_ctrlGate RSB:753 [no consumer]
K3         DrivesElementary SS:77 ─► genTheory_elementary ─► lieRank_of_elementary LieRankSource:476 ─►
           control_of_lieRank MicroscopicReversibility:114 ─► fullInstruments_of_control StinespringAssembly:197
           (+FiniteIsometryExtensionSF, discharged IsometryExtension:116); genTheory_qm_of_quantumArchitecture SS:136
           (QuantumArchitecture) via qm_of_oiPlusElem LieRankSource:535; typed_determined_iff TC:850 (ShadowQuantum);
           oiPlus_iff_qm CGOP:207 (OIPlus)
```

### 5.2 Seams: where one statement's conclusion is not literally another's hypothesis

Each seam is classified: adapter (mathematics in hand), gap (no statement), or substantive (open mathematics).

| # | seam | class |
|---|---|---|
| S1 | `sharpSeed_completion` concludes on `body D` ⊆ ℓ^∞ (`CSpace D`). The selectors read `SharpSeed (eball d) r` on `Fin d → ℝ`. The restriction to the chart and the transport by A exist (`sharpSeed_restrict`, `hypotheses_tr`) but are not composed. | adapter (T5) |
| S2 | `preservesBody_inducedEquiv` concerns one operation datum. K∞-Trans needs the **set** G of all induced maps, and no kernel object defines that set. TRB-1, EFF-1 and K1 accept any G, so K∞-Act is not read by the route. | gap |
| S3 | `chartBody_eq_eball` gives ∃A. The K1 hypotheses are not restated through A in any theorem. EffectsOn transport (`isEffectOn_tr`) is outside `hypotheses_tr`. | adapter (T5) |
| S4 | CMP-1's effect interface is `stageEffects D` (SC:176). K1 reads an arbitrary `avail`, with no relation between them. With exact K∞-Trans and K∞-V4, `avail ⊇ sharpFamily d` (uncountable for d ≥ 2), so `avail = stageEffects` is impossible on a countably indexed tower. The dense form removes the conflict. | substantive (needs an effect-closure premise or the dense form) |
| S5 | `ElementaryDrivability` is consumed only by `preservesBody_drive` OG:161, `preservesBody_driveWords` ON:107 and `isEmpty_drivability_of_finite_orbits` ON:124, none on the path to d = 3. Its NOT is not linked to `IsNot`'s N. The landed `ball3Drive` NOT is Ad_Z, not DIM-1's Ad_X. | gap (K∞-Drive is a dead premise on the route) |
| S6 | `CopyNatural` KF:284 has no consumer. DIM-1 encodes K∞-Copy as one shared N. | gap (T2 is the missing link) |
| S7 | `HasTwoSharpTests` is classified on `eball d` only (ST:155) and is composed with no selector. | adapter |
| S8 | DIM-1's carrier `W d` versus COMP-1's `Composite` over an arbitrary V. DIM-1's result lists this adapter as open. On the coordinate model `Carrier d d` = `W d` definitionally. | adapter (coordinate model) / substantive (general V, K2) |
| S9 | Real `W 3` versus K3's `Matrix (A × Fin n) ℂ`. The two module families share no import (KN census §1). | substantive (Kₙ); T7 is the n = 2 piece |
| S10 | OG-1 is stated on `ball3`, EFF-1 and K1 on `eball d`. | closed by `eball_three` TB:671 |
| S11 | `genTheory_qm_of_quantumArchitecture` concludes for `genTheory 𝓘 A`, a `FiniteOperationalTheory`. `typed_determined_iff` concerns a `TypedOperationalTheory` 𝒯. No theorem builds a typed theory from an architecture. | gap |
| S12 | The typed converse: no QM `TypedOperationalTheory` instance exists, only `typedDiag` TC:916. | gap (T3) |

### 5.3 Other EQ threads

None of the results above depends on another thread. The balanced-NOT question (relT, frame and two-sided positivity at
equal eigenspaces) was not touched; s6 works at d = 3 inside QM only. If another thread treats copy naturality, T2 and
the s4 classification are the overlap.

### 5.4 Unsourced premises

These remain unsourced from OI:
- SCInf, FiniteRank, BinaryVisible, and the elementary scope;
- K∞-Act data and the IC tower;
- K∞-Trans (exact or dense), K∞-V4, EffectsOn;
- IsNot, the native gate, and type covariance or a common N;
- `2 ≤ d` or entangling;
- local tomography, the composite cone, K2, Kₙ;
- QuantumArchitecture, or OIPlus / ShadowQuantum.

The converse adds nothing here. It shows each premise is satisfiable by QM under ι_Q.

## 6. Classification

- **QE1, the converse, premise by premise: THEOREM ROUTE at the elementary scope.** Every premise holds in QM under ι_Q.
  - Kernel witnesses: K1, endomorphic K3, the OI core on `Fin 2`, the ball-side K∞ premises.
  - Exact or written: K∞-Stage, K∞-Act, K2.
  - Written only: typed K3 (T3).

  **COUNTEREXAMPLE** for the following readings, each with an exact quantum witness:
  - K∞-Trans and K∞-Geom beyond capacity two (qutrit; Geom already recorded);
  - the formalized K∞-Stage as the elementary scope (the qutrit passes);
  - K∞-Act on non-IC towers (Hadamard on a Z-only tower);
  - universal K∞-Copy ((Ad_Y, Ad_X));
  - the NOT relations for every CNOT-frame gate ((S⊗I)·CNOT);
  - exact K∞-Trans with K∞-V4 and countable stage effects (cardinality, written).

  NEW findings: the K∞-Copy circle, the native-gate family T6, and the IC/horizon identification. CONFIRMING findings:
  the K∞-Trans scope (the thread-R ledger knew it; the ROADMAP bullet lacks the note) and the finite-substratum limit.
- **QE2, the dependency graph: OPEN, with named walls.** S1, S3, S7 and S10 are adapters (S10 closed). S2, S5, S6, S11
  and S12 are gaps. S4, S8 (general V) and S9 are substantive. NEW: no kernel theorem consumes the K∞ block, K∞-Drive,
  `CopyNatural`, `HasTwoSharpTests` or `ShadowQuantum`, and the typed converse has no instance.
- **QE3, the two-way theorem.** The converse is a THEOREM ROUTE: kernel and exact, with T1 and T3 to build. The forward
  direction is OPEN at the walls K2 (F3) and Kₙ (F4), with adapter T5 and reduction T2 to build. It differs from
  `oiPlus_iff_qm` as stated in Section 4.1.
- **QE4, global compatibility.** **No incompatible pair among the landed premises as stated:** the single model M_Q
  satisfies all of them at once. The search covered every hypothesis of every route theorem listed in `qe2_graph.out`,
  across horizons, charts, the orientation gauge, composites, ancillas and the qubit-face embedding (s1, s3, s7, s8).

  **COUNTEREXAMPLES** for strengthened readings, each with a witness:
  - **(I1)** cnot and T″ = (I⊗reflY)·cnot·(I⊗reflY) both satisfy every K1 premise with z3 and `nflip`, and admit no common
    `CandidateCone` (−½, s8; a corollary of K2Guard's chain). So "every native gate is available" is inconsistent with a
    K2Guard composite.
  - **(I2)** A G containing reflections (`fullAut` in the EFF-1 and SharpTests controls; `ratRefl` in the dense witness),
    together with cnot and a candidate cone. Landed: K2Guard:143.
  - **(I3)** Exact K∞-Trans with K∞-V4 and `avail = stageEffects` of a countable tower (written).
  - **(I4)** A fixed finite classical realization of the effects, together with K∞-Seed, K∞-Trans, K∞-V4 and d ≥ 2.
    Landed: F2, KF:947.
  - **(I5)** The universal K∞-Copy and native-gate readings, against QM (s4, s6).
  - **(I6)** `BinaryVisible ∧ SCInf ∧ FiniteRank` taken as the scope of K∞-Trans and K∞-Geom, against the qutrit (s1, s3).

  None of these involves the choices M_Q makes: an existential gate, an orientation-preserving G, all-effects or dense
  availability, IC towers, and capacity-two scope.
