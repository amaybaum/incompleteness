# EQ-E running notes — converse direction and global consistency (EQUIV-CLOSE)

Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58` at `scratchpad/eq/base/` (read-only).
All writes in `scratchpad/eq/E/`. No Lean, no git writes, exact arithmetic for every claim.

## 0. Productivity test (fixed before any computation, §A.31)

The thread is a **gem** iff it yields a fact strictly stronger than the obvious restatement
("quantum theory satisfies the quantum axioms") AND it either constrains the two-way statement or
exposes a hidden assumption. Concretely, at least one of:

- **G1 (NEW, converse failure).** A premise consumed by the forward route (K∞-*, K1, K2, Kₙ, K3) that
  *fails* in finite-dimensional complex quantum theory in the scope in which the route states it,
  or holds only under an identification of OI stages/horizons with quantum systems that the route
  does not fix — with an exact quantum witness — and that is **not already recorded** in the corpus
  (ROADMAP P1-K, kinf-seams-audit, kn census) or in the listed prior ledgers. Re-finding the qutrit
  singleton-face failure is explicitly *not* a gem (already recorded).
- **G2 (NEW, seam).** An interface seam in the kernel dependency graph where one statement's
  conclusion is not literally the next one's hypothesis, which the corpus does not already name
  (e.g. a carrier mismatch, a quantifier mismatch, a scope mismatch), with the exact file:line pair.
- **G3 (NEW, incompatibility).** Two landed premises that cannot hold together in one model, with an
  exact witness (or, failing that, a documented search with its exact scope).
- **G4 (POSITIVE).** An explicit identification under which every premise of the forward route holds
  in complex QT, each checked exactly — this validates the converse in the elementary scope and is
  stronger than the restatement because it fixes the identification and scope of every premise.

**Non-gem (record only):** relabelling the existing conditional `oiPlus_iff_qm`; listing premises
without testing them; float-only evidence; re-deriving a recorded failure.

**Decision rule (pre-registered, rule not numbers):** a premise is classified
- HOLDS(scope, identification) iff an exact check over the stated scope succeeds and a non-quantum
  foil (classical bit / real / gbit / polygon) is checked to fail or pass as the premise predicts
  (countercontrol);
- FAILS iff an exact quantum witness violates the premise as stated in the kernel (not as paraphrased);
- MIS-SCOPED iff it holds for the elementary qubit identification but fails at another identification
  the route also needs (e.g. Kₙ / K3 carriers), witness exact;
- UNTESTABLE-AS-STATED iff the kernel object has no quantum instance without an extra identification
  choice, named.

Depth-first: QE1 first (decisive), one premise at a time, each node closed with a verdict.

## 1. Branch log

### N1 — QE1 premise inventory (read at base, file:line under `verification/lean-mathlib/OIBridge/`)

| premise | kernel object (definition) | consumed by (route theorem) |
|---|---|---|
| K∞-Stage | `SCInf` StageCompletion:78, `BinaryVisible` SC:244, `FiniteRank` SC:299; `FiniteStage` KInfFoundations:63; elementary scope: no predicate | `sharpSeed_completion` SC:224; `exists_chart_of_finiteRank` SC:304; TRB-1 `chartBody_eq_eball` TransitiveBody:651 (via `CompletionChart`) |
| K∞-Act | `OpDatum` CompletionAction:46, `AffineRespect` CA:58, `Undoes`/`inducedEquiv` | `preservesBody_inducedEquiv` CA:352; consumed further only by ORD-1 (CompositionOrder); NOT read by TRB-1/EFF-1/K1 (they take any `G`) |
| K∞-Drive | `ElementaryDrivability` KInfFoundations:264 | `preservesBody_drive` OG:161, `preservesBody_driveWords` ON:107, `isEmpty_drivability_of_finite_orbits` ON:124; NOT read by any theorem on the route to d = 3 |
| K∞-Trans | `BoundaryTransitive` OG:79 (dense form `DenseBoundaryOrbit` DenseOrbit:53) | `exists_affine_image_eq_eball` TB:602, `chartBody_eq_eball` TB:651, `seedOrbit_ball3_eq` OG:348, `maxConeOf_avail_eq` EffectSpace:572, K1Bridge selectors |
| K∞-Seed | `SharpSeed` OG:71 | `seedOrbit_ball3_eq`, `maxConeOf_avail_eq`, K1Bridge; source `sharpSeed_completion` SC:224 |
| K∞-V4 | `SeedOrbitAvailable` OG:79-ish (OG:83) | `ballEffect_mem_avail`, `maxConeOf_avail_eq`, K1Bridge |
| K∞-Copy | the single `N` in `IsNot`/`NativeGate` (CompositeDimension:210,218); `CopyNatural` KF:284 | `dim_of_nativeGate` CD:2723, `three_of_nativeGate` CD:2748 (and relative/dense/ctrl forms) |
| K∞-Geom | `SingletonFaces` KF:139, `RelStrictConvex` KF:144 | `relStrictConvex_of_supporting_singleton` KF:575 (not on the d = 3 path) |
| K1 | `IsNot` CD:210, `NativeGate` CD:218, `Entangling` CD:229, `NativeGateOf`/`EntanglingOf` K1Bridge:49/64, `EffectsOn` EffectSpace:567, `0 < d`, `2 ≤ d` (`HasTwoSharpTests` SharpTests:41), `CtrlGate` (RelcSelectBlock) | `dim_of_nativeGateOf` K1B:128, `three_of_nativeGateOf` K1B:138, `dim_of_ctrlGate` RSB:739, `three_of_ctrlGate` RSB:753 |
| K2 | carrier `W d` CD:97 (LT encoded); `Composite`/`LocallyTomographic` CompositeInterface:235/243; `CandidateCone` K2Guard:95 | DIM-1 reads `W d` only; no theorem reads `Composite` on the route |
| Kₙ | no predicate | — |
| K3 | `QuantumArchitecture` SubstratumSource:86 (`Architecture`, `ContextStable`, `LabelInvariant`, `DaggerStable`, `DrivesElementary` SS:77); `ShadowQuantum` TypedCompletion:291; `OIPlus` CarrierGeneralOIPlus:185 | `genTheory_qm_of_quantumArchitecture` SS:136, `typed_determined_iff` TC:850, `oiPlus_iff_qm` CGOP:207 |

Converse kernel witnesses already landed: `fullClass_quantumArchitecture` SS:151, `qm_generated_by_quantumArchitecture` SS:161,
`oiPlus_of_qm` CGOP:196-ish, `isNot_nflip` CD:838, `nativeGate_cnot`, `entangling_cnot`, `ball3Drive` KF:449,
`boundaryTransitive_ball3Drive` ON:667, `boundaryTransitive_fullAut` EffectSpace:337, `singletonFaces_closedBall` KF:658,
`eball_three` TB:671.

### Node plan (depth-first; QE1 first)
- N1.1 identification ι_Q (written) → N1.2 K∞-Stage (s1) → N1.3 K∞-Act (s2) → N1.4/1.5/1.8 Drive, Trans, Geom at qubit vs
  qutrit (s3) → N1.7 K∞-Copy: NOT pairs of the quantum cnot (s4) → N1.9 K1 Pauli adapter and gate class (s5, s6) →
  N1.10 K2 (s7) → N1.11 Kₙ/K3 (kernel citations).
- N2 QE2 graph and seams; N3 QE3 statement; N4 QE4 one-model check (s8) and incompatibility search.

### N1.1 — the identification ι_Q (written; fixed before the computations below)
- elementary system ↔ a qubit ℂ²; body ↔ Bloch ball via ρ(x) = (I + x·σ)/2 (Pauli expectation coordinates,
  kernel `hom`); effects ↔ 0 ≤ E ≤ I via E = Σ_μ a_μ σ_μ ↦ affine functional a₀ + a·x;
- available reversible operations G ↔ PU(2) acting by conjugation (= SO(3) on the ball); available effects avail ↔
  all effects; seed ↔ a rank-one projector;
- two identical copies ↔ ℂ²⊗ℂ² with the canonical identification; joint carrier W 3 ↔ the 4×4 matrix
  ω_{μν} = tr(ρ σ_μ⊗σ_ν) (control index μ, target ν);
- stage tower ↔ an increasing family of finite sets of density matrices and of effects with Born tables, forward
  maps = inclusions; horizon ↔ the stage index;
- K3/Kₙ carriers ↔ Matrix S S ℂ for every finite S, ancilla extensions S × Fin n, the full implementation class.

### N1.9a — s5 (Pauli adapter): VERDICT CONFIRMED (22/22, both countercontrols fail as required)
kernel `cnot` = Pauli transfer matrix of the quantum CNOT (control = first factor); `nflip` = Ad_X; `z3` = |0⟩,
`xplus` = |+⟩; `phiW` = Φ⁺ = CNOT(|+⟩|0⟩); `prodState`, `sharpEff`, `prodEffVal` are the Born values; eball 3 = Bloch
ball (charpoly), EFF-1's effect description = 0 ≤ E ≤ I (charpoly). The transpose acts as `reflY` = diag(1,−1,1):
K2Guard's one-copy reflection is the partial transpose. Note: the kernel's control drive `ball3Drive` has NOT
`rot3 π` = Ad_Z (flips x-basis states, fixes z3), not DIM-1's Ad_X.

### N1.7 — s4 (K∞-Copy against QM): VERDICT
- relT with the quantum CNOT forces N_B = Ad_X (unique even before the involution condition).
- relC (two-NOT form) with N_B = Ad_X: N_A ranges over all π-rotations about horizontal axes, [[c,s,0],[s,−c,0],[0,0,−1]],
  c²+s² = 1 — a circle, not a point.
- WITNESS: (N_A, N_B) = (Ad_Y, Ad_X) meets both relations of the quantum CNOT with N_A ≠ N_B. So the universal
  reading of K∞-Copy ("every NOT pair compatible with the native gate agrees") FAILS in QM; the kernel's existential
  reading (∃ one N for both relations) HOLDS (N = Ad_X).
- Type covariance ("the pair is conjugate by a frame-preserving automorphism") HOLDS in QM: N_A = R_z(φ) N_B R_z(φ)⁻¹
  (symbolic identity), R_z(φ) = Ad diag(1, e^{iφ}) a quantum operation fixing z3. It FAILS on both recorded foils
  (NB-1 C2N d = 5: plus-multiplicities 3 vs 2; K∞ §6 d = 7: 4 vs 2).
- Reduction instance: T̃ = (I⊗g⁻¹) cnot (I⊗g), g = R_z(π/2), meets frame + both relations with common NOT Ad_Y; T̃ is the
  quantum gate (I⊗S†)CNOT(I⊗S) = |0⟩⟨0|⊗I − |1⟩⟨1|⊗Y.
- Run 1 had one FAIL: I had mis-specified the expected gate as |0⟩⟨0|⊗I + |1⟩⟨1|⊗Y (s4_not_pairs.run1.out). Corrected
  expected value computed from the conjugation itself; the wrong gate is kept as a countercontrol (it differs by Z⊗I).
- Classification: K∞-Copy converse = HOLDS (existential); universal reading = INCOMPATIBLE WITH QM (exact witness);
  candidate weakening (type covariance) = HOLDS in QM and excludes both foils. Productivity: NEW (G1-type: a reading of a
  route premise that QM violates, with exact witness; not in ROADMAP/NB-1/DIM-1 records — DIM-1 lists "different NOTs on
  the two copies" as open, NB-1's C3 control checks only one NOT).

### N1.9b — s6 (native-gate relations inside QM's CNOT-frame class): VERDICT
- Frame class (written): Ad_U has DIM-1's `frame` iff U = CNOT·D, D diagonal unitary; all such U are two-sided positive
  and entangling.
- Grid of 64 Clifford-phase D (d00 = 1, d_ab ∈ {±1, ±i}): 8 admit a common NOT (Ad_X or Ad_Y), 56 admit NO NOT pair at
  all (common or two-NOT, over all linear maps of ℝ³), none admits a two-NOT pair only.
- GENERAL (symbolic, using PARITY-NOT-1's kernel theorem `piRotation_three` ParityNot:161 to reduce N to a π-rotation
  about a horizontal axis): CNOT·D has a common NOT iff D ∝ diag(1,1,u,ū)·(I⊗Z)^k, |u| = 1, k ∈ {0,1}; the NOT is then the
  π-rotation about the axis at angle arg(±u) — the orbit of (cnot, Ad_X) under the frame symmetries R_z(φ)⊗R_z(φ) and the
  target phase I⊗Z. Exact irrational-phase member checked (u = (3+4i)/5, N = [[-7/25,24/25,0],[24/25,7/25,0],[0,0,-1]]).
- WITNESS: (S⊗I)CNOT = CNOT·diag(1,1,i,i): frame ✓, positive ✓, entangling ✓ (reduced state I/2), NO linear N satisfies
  IsNot + relT + relC, and no two-NOT pair exists either.
- A manual expectation of mine (antiunitary control NOT for this gate) was wrong: I had applied T∘Ad_U∘T = Ad_Ū to a
  partial transpose; the exact solver is authoritative.
- Classification: DIM-1's native-gate relations hold in QM existentially (cnot), on a one-parameter (×2) family of the
  three-parameter frame class, and FAIL for a generic CNOT-frame entangling quantum gate. So "the native gate" cannot be
  identified with an arbitrary physically given CNOT-frame entangling gate; the relations are an alignment condition QM
  satisfies by choice of representative. Productivity: NEW (QM-side scope of a route premise; DIM-1 lists gate
  uniqueness as open and NB-1's C3 control checks CNOT only).

### N1.2 / N1.3 — s1 (K∞-Stage, K∞-Act under ι_Q): VERDICT
- Qubit tower (30 rational Bloch vectors, three nested stages, effects: unit, (I±Z)/2, (I±v·σ)/2): FiniteStage axioms,
  SCInf, BinaryVisible, FiniteRank (chart dimension 3, prepVec injective) exact; the sharp-seed source hypothesis of
  `sharpSeed_completion` holds. K∞-Stage HOLDS for the qubit.
- Qutrit tower (9 rational pure states, IC projectors): SCInf, BinaryVisible, FiniteRank (rank 8) exact. So the
  formalized K∞-Stage predicates hold for the qutrit too and do NOT delimit the elementary scope; capacity two does
  (qutrit capacity 3 exact; qubit ≤ 2 by the kernel's Lemma D `card_le_two_of_centrallySymmetric` KF:632).
- K∞-Act: unitary conjugations (rational z-rotation, Hadamard) are AffineRespect data with inverse data on the IC tower
  (26 affine relations checked exactly). COUNTERCONTROL: on a Z-only (non-IC) tower |+⟩ and |+i⟩ share a preparation
  vector while their Hadamard images do not — StateRespect fails for a unitary. So K∞-Act holds in QM under ι_Q only
  with an informationally complete stage tower (identification requirement IC). Also: the transpose (det −1) is
  AffineRespect data too — K∞-Act does not exclude antiunitary maps.
- Run 1 had one FAIL from my test harness (Python ints made 1/2 a float in the sharp-seed check); fixed by passing
  exact Rationals, and a Rational-type assertion added on every table entry (s1_stage_act.run1.out kept).
- Classification: K∞-Stage CONFIRMED in QM (all n); scope NOT delimited by its formalized part (ELABORATING: corpus says
  the scope predicate is unformalized; new: an explicit QM witness that BinaryVisible ∧ SCInf ∧ FiniteRank admit the
  qutrit, and capacity-two as a converse-valid scope). K∞-Act CONFIRMED in QM with the IC requirement (NEW, modest:
  an identification premise the converse needs; OI's observer cut is explicitly not complete, so the elementary
  system's stage tower must be IC even though the global cut is not).

### N1.4 / N1.5 / N1.8 — s3 (Drive, Trans, Geom beyond the qubit): VERDICT (14/14)
- K∞-Trans: qubit ✓ (kernel `boundaryTransitive_ball3Drive` ON:667, `boundaryTransitive_fullAut` EffectSpace:337); qutrit ✗
  for EVERY G: diag(1/2,1/2,0) is a boundary state (x + ε(x−y) has eigenvalue −ε) and not extreme, so the landed
  `not_boundaryTransitive_of_nonextreme_boundary` (TransitiveBody:301) applies; the dense form fails too (DenseOrbit:125
  would make the body a Q-ball). ELEMENTARY-SCOPED. The ROADMAP's K∞-Trans bullet carries no scope note (only the
  geometric branch K∞-Geom is scoped there). CONFIRMING (thread-R ledger knew "TRANS, which the qutrit violates");
  corpus propagation gap.
- K∞-Geom: qutrit ✗ (recorded; re-verified). ELEMENTARY-SCOPED (recorded).
- K∞-Drive: the qutrit carries an ElementaryDrivability (flow Ad exp(−itH), H = |0⟩⟨1|+|1⟩⟨0|; involution at t₀ = π;
  J = Ad of the permutation (1 2), off axis) — exact. NOT elementary-scoped; consumed by no route theorem (N2).
- Seam: the landed control drive `ball3Drive` has NOT `rot3 π` = Ad_Z, which fixes z3; DIM-1's NOT is Ad_X. A drive
  about the first axis aligns them (R_x(π) = nflip, J = cyc3 off axis) — so alignment is realizable in QM, but no
  premise or theorem ties K∞-Drive's NOT to IsNot's N.
- Dense K∞-Trans in QM: the countable rational ROTATION group (det +1, rational unitary conjugations) has dense boundary
  orbits; the kernel's dense witness `ratRefl` (DenseOrbit:342) consists of reflections (antiunitary), the choice
  K2Guard excludes alongside cnot.

### N1.10 — s7 (K2 against QM): VERDICT (11/11 after a harness fix)
- Complex two-qubit LT: 16 Pauli products R-independent in Herm(4) ✓. FOIL real QM: I/4 and (I + Y⊗Y)/4 (real symmetric
  states) agree on every product of real local effects — LT fails (exact).
- Quantum cone: contains products, lies in maxCone (written), preserved by CNOT and local Clifford rotations (unitary,
  orthogonal transfer matrices) — a K2Guard `CandidateCone` invariant under cnot and the local rotations.
- K2Guard's chain reproduced through ι_Q: actT reflY is the partial transpose (Φ⁺ ↦ eigenvalue −1/2); cnot·actT reflY·cnot
  (prodState xplus z3) = chainW with pairing −1/2; with nflip the value is 0. So K2Guard's obstruction is the
  non-positivity of the partial transpose, and QM satisfies K2's local-action premise because its local group is SO(3).
- Harness bug in run 1 (Python ints made b/2 a float inside `sharpVec`); fixed in common.py by sympifying inputs; all
  scripts re-run green (s7_k2_composite.run1.out kept). No decimal number appears in any current output.

### N1.2b — horizons (s1, 20/20)
- A fixed-basis observer's horizon tower (Z readout with Lüders update after each step of a fixed rational unitary)
  satisfies SCInf as marginal consistency (horizons 1→2→3, exact) but completes to a SEGMENT: every horizon effect is
  c_s·U†P_bU, affine rank 1 — the qubit read this way is the classical bit (d = 1).
- With a three-context instrument menu before the readout the rank is 3 (the Bloch ball).
- So ι_Q must identify OI's stages with (horizon, instrument menu) pairs whose effects are IC on the elementary system;
  K∞-V4 + K∞-Trans are what force rotated readouts into the available family. Without contexts the route lands on d = 1
  (where `two_le_not_implied` already shows the remaining hypotheses hold).

### N2 — QE2 graph (qe2_graph.py → qe2_graph.out, every declaration located at the base) — seams
Consumers outside their own module (from the extraction): `sharpSeed_completion`, `chartBody_eq_eball`,
`hypotheses_tr`, `preservesBody_inducedEquiv`, `exists_completionChart`, `SCInf`, `BinaryVisible`, `CopyNatural`,
`SingletonFaces`, `RelStrictConvex`, `HasTwoSharpTests`, `hasTwoSharpTests_iff`, `three_of_nativeGateOf_of_two_le`,
`DenseBoundaryOrbit`, `dim_of_nativeGateOf_dense`, `CtrlGate`, `dim_of_ctrlGate`, `ShadowQuantum`: NONE.
The only composed chains: EFF-1 `maxConeOf_avail_eq` → K1B `nativeGate_of_avail` → DIM-1 `dim_of_nativeGate`; and the
K3 chain inside the complex modules. No TypedOperationalTheory instance exists except the control `typedDiag`
(TC:916): the typed converse has no kernel witness; the endomorphic converse does (`genTheory fullClass`,
`fullClass_quantumArchitecture` SS:151, `fullQuantum_exactAll` IsometryExtension:231 on Fin 2).

### N4 — QE4: s8 one model M_Q (13/13)
- Seed = corners; NOT complements the seed; drive NOT (R_x(π)) = DIM-1 NOT = Ad_X ∈ G; G ⊆ SO(3); COMP-1 coordinate carrier
  `Carrier d d` is definitionally `W d` and `pState` = `prodState`; normalisation; global transpose fixes cnot (CNOT real);
  qubit face of the qutrit inherits SF (diag(1,1,0) restricts to the unit), effects and G; dense form with countable
  rational stage effects and rational rotations.
- INCOMPATIBILITY outside M_Q: T'' = (I⊗reflY)cnot(I⊗reflY) satisfies frame + relT + relC with z3, nflip (and positivity,
  entangling — written, local ball automorphisms), maps |+⟩|0⟩ to PT(Φ⁺) (eigenvalue −1/2), and {cnot, T''} admit no
  common candidate cone (T''(cnot(prod)) pairs −1/2). Corollary of K2Guard's chain. So "every gate meeting the native-gate
  hypotheses is available" is incompatible with a K2Guard composite; the native-gate premise must stay existential.

### Maximum-skepticism passes on the favourable branches (§A.31)
- Converse POSITIVE: each premise re-checked in its kernel form, not a paraphrase (definitions read at the base);
  finite-tower checks extended to the completion by the written affine-injectivity argument; universal parts cited to
  kernel theorems. Foils: real QM (LT), classical bit (two_le_not_implied ST:197), square gbit (capacity 2 by Lemma D, not
  boundary transitive by TRB-1 §G), C2N and d = 7 (type covariance).
- Type covariance favourable: the reduction is checked symbolically on the QM instance and is a 5-line written proof
  (actT/actC commute; g fixes ±z; local ball automorphisms preserve maxCone). It is prior-ledger material (K-INF §16.1);
  the NEW part is the QM classification (circle) and the foil check.
- "No incompatible pair": the search covered every hypothesis of the route's kernel theorems (qe2_graph list); one model
  satisfies all of them; scope variations each produce an exhibited incompatibility (I1–I6 in RESULT).

### Fixed point
Passes 1–4 over the premise list after s8 (identifications vs each other; horizons vs K∞-Seed; embeddings vs SF; charts
vs the composite cone; orientation gauge) produced no further NEW item. Stop.

### Close
RESULT.md written (six sections). run_all: OK (8 scripts, 111 checks, outputs replay byte-exact). Base manifest
`sha256sum -c` clean; nothing written outside scratchpad/eq/E; no __pycache__.
