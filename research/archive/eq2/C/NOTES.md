# EQ2-C — running notes (design only; nothing adopted, frozen or governed)

Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, read-only at `scratchpad/eq/base/`.
Writes: only `scratchpad/eq2/C/`. No Lean/lake (no toolchain). No git writes. `eq2/A`, `eq2/B` not read.

## Productivity test (fixed 2026-10-08, before any node was walked)

The thread is a **gem** iff, for at least one of the three C3 targets (boundary purity BP at capacity two,
FiniteRank, the reversible operations), it produces a fact strictly stronger than the obvious restatement
("X needs a premise") AND either
 (a) derives the target from premises that hold in finite-dimensional complex QM **at every level** (not only at the
     elementary scope), each premise shown load-bearing by an exact countermodel, or
 (b) proves the target independent of a named candidate source by the smallest exact countermodel, or
 (c) exposes a hidden assumption on the gate route (C1) that the ledger of an earlier thread missed.
A relabelling of the target (a premise equivalent to it on every body considered) is recorded as a non-gem.
C1/C2 are deliverables, not gems: they are judged complete when every hypothesis of the d = 3 gate statement is named
and classified, and each C2 item is refined against the kernel text it names.

Propagation bar: better-than-coherence. A favourable branch gets a countercontrol and maximum skepticism.

## Mathlib source used for availability checks

`scratchpad/ml-v433-src/m/` — a Mathlib source tree whose `lean-toolchain` reads `leanprover/lean4:v4.33.0`, matching the
base pin (`verification/lean-mathlib/lakefile.toml`: `rev = "v4.33.0"`; there is no `lake-manifest.json` at the base).
Provenance: left by an earlier session, not re-fetched here. Availability claims checked against it are labelled
"local v4.33 tree"; they are not kernel checks (nothing was compiled).

## Node log

### N0 — kernel reading at the base (every line below was opened and read)

Abbreviations: SC StageCompletion, CA CompletionAction, KF KInfFoundations, OG OrbitGeneration, ON OrbitNormalization,
TB TransitiveBody, IIP InvariantInnerProduct, ES EffectSpace, DO DenseOrbit, K1B K1Bridge, CD CompositeDimension,
RSB RelcSelectBlock, RSP RelcSelectParity, RC5 RelcSelectC5, OC OddChar, PN ParityNot, K2G K2Guard, ST SharpTests,
IL ImplementationLocality, SS SubstratumSource, SCl StructuralClosure, MR MinimalRepertoire, LRS LieRankSource,
RS ReachabilitySeam, AC AncillaClosure, CL CoherentLift, MC MonoidalCompletion, SI SubstratumInterface,
MRv MicroscopicReversibility, LOS LevelOneSeam.

Stage → body: `DirectedStages` SC:63, `SCInf` SC:78, `sharpSeed_completion` SC:224, `BinaryVisible` SC:244,
`FiniteRank` SC:299 (= `FiniteDimensional ℝ (affineSpan ℝ Ω).direction`), `exists_chart_of_finiteRank` SC:304,
`OpDatum` CA:46, `AffineRespect` CA:58, `CompletionChart` CA:144, `exists_completionChart` CA:154, `chartBody` CA:166,
`Undoes` CA:325, `inducedEquiv` CA:333, `preservesBody_inducedEquiv` CA:352 (one datum, singleton set).
Body → ball: `PreservesBody` OG:69, `BoundaryTransitive` OG:79, `SharpSeed` OG:65, `SeedOrbitAvailable` OG:74,
`IsBodyGroup` TB:223, `isBoundaryState_of_extreme` TB:284, `extreme_of_isBoundaryState_of_transitive` TB:290,
`not_boundaryTransitive_of_nonextreme_boundary` TB:301, `centroid_fixed_of_preservesBody` TB:356 (via
`invariant_inner_product` IIP:336, `centroid_fixed` IIP:152), `centroid_mem` TB:388, `centroid_mem_interior` TB:427
(needs BoundaryTransitive), `exists_affine_image_eq_eball` TB:602, `chartBody_eq_eball` TB:651, `eball_three` TB:671,
`DenseBoundaryOrbit` DO:53, `chartBody_eq_eball_of_dense` DO:209. KF: `IsBoundaryState` KF:130 (intrinsic),
`PerfectlyDistinguishable` KF:154, `CentrallySymmetric` KF:160, `card_le_two_of_centrallySymmetric` KF:632,
`not_isBoundaryState_of_mem_interior` KF:601, `CopyNatural` KF:284, `ElementaryDrivability` KF:264.
Effects: `EffectsOn` ES:567, `maxConeOf_avail_eq` ES:572, `maxConeOf_avail_eq_of_dense` DO:243. Transport:
`effTr` ON:159, `conjTr` ON:177, `isEffectOn_tr` ON:217, `hypotheses_tr` ON:295, `sharpSeed_restrict` ON:427,
`hypotheses_restrict` ON:529.
Gate: `W` CD:97, `homMap` CD:112, `actT` CD:198, `actC` CD:201, `IsNot` CD:210, `NativeGate` CD:218 (relT and relC),
`Entangling` CD:229, `opGate_homMap_comp` CD:503, `finrank_plus_eq_finrank_minus` CD:682 (via `NativeGateBall.parity`
on the operator space: an injective `Lop` anticommuting with `Pop`), `corner_form` CD:1805, `Mfwd` CD:1878,
`gate_actC` CD:1945, `gate_corner_neg` CD:1965, `dim_of_nativeGate` CD:2723, `three_of_nativeGate` CD:2748.
`CtrlGate` RSB:45 (frame, posFwd, posInv, relC; no relT), `ctrlGate_of_nativeGate` RSB:53, `gate_actC_ctrl` RSB:92
(relC read at :95), `gate_corner_neg_ctrl` RSB:99 (its only consumer, :103), `gt_corner_neg_ctrl` RSB:113,
`blockData_of_ctrlGate` RSB:716, `not_entangling_one_ctrl` RSB:725, `dim_of_ctrlGate` RSB:739 (parity read at :746
through `finrank_plus_eq_finrank_minus_relC hN hG.relC`), `three_of_ctrlGate` RSB:753.
`finrank_plus_eq_finrank_minus_relC` RSP:329 takes the FULL relC (`hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)`).
Relative forms: `NativeGateOf` K1B:49 (with relT), `EntanglingOf` K1B:64, `nativeGate_of_avail` K1B:108,
`dim_of_nativeGateOf` K1B:128, `three_of_nativeGateOf` K1B:138; dense DO:284/299/307/317. No `CtrlGateOf` exists
(grep at base: no hit). `three_of_nativeGate_of_two_le` K2G:234, `three_of_nativeGateOf_of_two_le` K2G:253.
`HasTwoSharpTests` ST:41, `hasTwoSharpTests_iff` ST:155, `two_le_load_bearing_relative` ST:185.
d = 7 vocabulary already landed: `OddChar.nK k` OC:56 (signs + on homogeneous 0..k, − on k+1..2k+1), `zK k` OC:59,
`isNot_nK` OC:102, `finrank_plus_eq_finrank_minus_nK` OC:176, `entW` OC:238, `diagSign` PN:292,
`homMap_diagSign` PN:299. At k = 3: `nK 3` = diag(1,1,1,−1,−1,−1,−1) = BAL's N7b, `zK 3` = e₇ = BAL's z7.
K3 side: `ImplementationClass` IL:244, `InstAvail` IL:268, `ContextStable` IL:359 (adjoins `1_R` on the FIRST
factor: `tensorOf (1 : Matrix R R ℂ) K`), `LabelInvariant` IL:364, `Architecture` IL:506 (one, mul, smul, proj,
block), `genTheory` IL:852, `DrivesElementary` SS:77 (three clauses: flows of `transition a b` for ALL a b incl.
a = b; swaps `permMatrix (Equiv.swap a b)`; `phaseGate a`), `QuantumArchitecture` SS:86, `substratumClass` SCl:180,
`StructurallyClosed` SCl:183, `quantumArchitecture_iff_drives_of_closed` SCl:364, `ExtendsSubstratum` SCl:401,
`transition` LRS:199 (`single a b 1 + single b a 1`), `phaseGate` LRS:209 (`diagonal (if a = p then I else 1)`),
`flow` RS:95 (`NormedSpace.exp ((-(t:ℂ) * I) • H)`), `ancBlock` AC:457 (`of fun s t => K (s, f) (t, e)`, ancilla
SECOND), `ancBlock_tensorOf_one` MR:488 (stated only for carriers `A × Fin n`), `permMatrix` CL:92, `tensorOf` MC:193,
`IsMonomial` SI:75, `DaggerStable` MRv:216, `ExactAllFiniteEndomorphicQuantumOps` LOS:186.
Mathlib (local v4.33 tree): `Matrix.exp_blockDiagonal`, `Matrix.exp_units_conj`, `Matrix.exp_add_of_commute`,
`Matrix.exp_diagonal` present in `Mathlib/Analysis/Normed/Algebra/MatrixExponential.lean`.

### N1 — C3 target BP (boundary purity at capacity two). Depth-first, one avenue at a time.

Avenue choice (decisive branch): of the three suggested sources, "singleton face / sharp update" and "self-duality"
were tested first as cheap side branches, then the decomposition-plus-symmetry avenue was walked to the end.

- N1.1 singleton face (SF). With supporting-effect completeness, SF ⇔ relative strict convexity (KF:575 one way,
  KF:590 the other). SF restricted to atomic (fine-grained) sharp effects is level-uniform in QM, but at capacity two
  every proper sharp effect is atomic, so on an elementary body it is SF again. A "sharp update" clause
  (non-disturbance on certain states + state-independent output) is equivalent to SF once measure-and-prepare
  instruments exist. Verdict: RELOCATION, not a source (non-gem). No script needed beyond the kernel lemmas.
- N1.2 self-duality. COUNTEREXAMPLE: the regular pentagon is strongly self-dual (exact M = diag(α, Q), D5-invariant,
  K* = MK), capacity two, satisfies SS (D5 is simply transitive on the 10 ordered frames) and ELEM2, and fails BP.
  So self-duality + SS + capacity two ⇏ BP. Self-duality + homogeneity (Koecher–Vinberg; literature, unverified)
  would give a Lorentz cone at rank two; homogeneity is a strong dynamical premise (filters) — not pursued.
- N1.3 decomposition + symmetry (decisive). Spec2 (every state lies on the segment of a frame = an ordered pair of
  perfectly distinguishable pure states) + SS (G transitive on ordered frames) ⇒ every frame's midpoint is the
  centroid c (TB:356 fixes c; Spec2 at c plus the swap forces p = 1/2), Ω = ⋃[x, 2c − x] is centrally symmetric,
  c is interior, a boundary state c + t(x − c) needs |t| = 1 (points of [c, x) are interior), so boundary states are
  frame members, hence extreme: BP. SS then gives transitivity on extreme points, so BoundaryTransitive (OG:79).
  Dense form: SS replaced by "the G-orbit of an ordered frame is dense in the frames" gives BP and
  DenseBoundaryOrbit (DO:53) by the same limits. Exact probe `c3_bp.py` 40/40.
  Pressure test of the favourable branch: (i) every step re-read against KF:130 (intrinsic boundary state), KF:601,
  TB:284/356/388; the proof uses no group structure of G (only the transitivity property) and no effects beyond
  defining frames; (ii) frames defined through `PerfectlyDistinguishable` (KF:154) with an effect pair are
  automatically swap-closed; (iii) countermodels exist for each premise dropped (pentagon: no Spec2; bidisk,
  Stiefel: no SS; qutrit: frames are triples; Carathéodory: capacity ≥ 3) — none satisfies both premises with pairs;
  (iv) the per-body disguise check: on one finite-dimensional capacity-two body with full effects,
  Spec2 ∧ SS ⇔ ball ⇔ BoundaryTransitive. The content is therefore the level-uniformity: Spec and SS hold in QM at
  every level (maximal frames = orthonormal bases), BP does not (qutrit). That meets productivity clause (a).
  NEW relative to EQ-A: EQ-A's ELEM2 + GEOM2 gives relative strict convexity only and its GEOM2 is a face statement;
  here neither premise mentions faces, and the pair also yields the transitivity half of K∞-Trans.
- Harness corrections before the first run (recorded, not hidden): two vacuous `True` checks (BD.3, Q3.4) and one
  tautological comparison (Q3.3) were replaced by real checks; placeholder code in H.5 was removed; ST.4's first
  instance had an irrational square root (it would have failed, not passed) and now reuses the BD search; the C2 trig
  identity is reduced modulo s² + c² − 1 instead of `simplify`. The first recorded run is `c3_bp.run1.out` (40/40).

### N2 — C3 target FiniteRank. Avenue: uniform finite resolution through the protocol towers.

- N2.1 UFR (for every ε a stage whose effects fix every effect value to within ε, uniformly over states) ⇔
  compactness of the body in the operational (ℓ^∞) metric: Dini (local v4.33: `Monotone.tendstoLocallyUniformly_of_
  forall_tendsto`, Topology/UniformSpace/Dini.lean) one way, total boundedness through the finite-dimensional stage
  images the other. Written.
- N2.2 UFR alone does not give FiniteRank: EQ-A's compact ellipsoid tower (exact there; (N)-failure re-derived here,
  EL.1). The missing clause is uniform norming (N): body − body contains an operational ball of its span. Theorem
  FR-R (written): FiniteRank ⇔ UFR ∧ (N). (⇐) Riesz (local v4.33: `FiniteDimensional.of_isCompact_closedBall₀`,
  Analysis/Normed/Module/FiniteDimension.lean:475); (⇒) closed bounded sets of a finite-dimensional affine subspace
  are compact, and a finite-dimensional convex body has a relative interior point. Separations: ℓ² tower ((N), ¬UFR),
  ellipsoid tower (UFR, ¬(N)). Relative to EQ-A's Theorem R: ELABORATING — the same Riesz endpoint with the
  norming clause made explicit and no Kakutani step (EQ-A derives (N) from V4 + dense orbit + RSC with Kakutani).
- N2.3 Do the protocol towers supply UFR? Exact countermodel to the structural claim: the passive protocol tower of
  the shift on the stationary renewal process with gap law 4/(k(k+1)(k+2)) (an invariant measure, a bijective
  dynamics, a binary readout, SC∞ by one global law) has nonsingular Hankel blocks of every size n ≤ 12 and
  age states 16^k pairwise ≥ 15/38 apart (written: ≥ 1/2 − 33/289 for all k). So the tower structure gives neither
  UFR nor FiniteRank. Scope: it is OI-shaped, not a lattice rule with the uniform product measure. NEW (modest).
- N2.4 For the corpus's own lattice rules UFR is OPEN (the rank thread's wall: an unbounded lower bound for the
  nonlinear rule). Already decisive for the gate route: rank ≥ 154 at horizon 8 means that even if FiniteRank held
  there, the body would have dimension ≥ 153, which no gate-route ball admits (d ∈ {1, 3}).
- N2.5 Favourable avenue tested with maximum skepticism: "the gate premises force FiniteRank" (a dimension-free
  selector). Blocked at two named walls: (i) the parity half is a dimension count (RSP:329 compares
  (d+1)P with P² + Q² on operator spaces); with P = 2 and Q infinite both sides are the same infinite dimension, so no
  contradiction arises — a dimension-free selector needs a new argument for TR's role; (ii) before any gate, the
  infinite-dimensional body would have to be identified as a Hilbert ball, which is Mazur's rotation problem in
  general (open; literature from memory, unverified). Verdict for the avenue: OPEN with these walls.

### N3 — C3 target: the reversible operations (K∞-Act data / OPACT, K∞-Trans).

- N3.1 Which reversible-operation premises the gate route consumes (kernel reading, N0): PreservesBody of the body
  group (OG:69; per datum from CA:352), BoundaryTransitive or DenseBoundaryOrbit (OG:79, DO:53), SeedOrbitAvailable
  (OG:74), the NOT (CD:210), the gate (RSB:45) and type covariance. ElementaryDrivability (KF:264) is not consumed
  (EQ-E S5). Continuity is therefore not needed on the gate route.
- N3.2 Data (K∞-Act): THEOREM ROUTE from prefix-closed protocol effects and inverse-closed action menus (oistage
  F-S1; replayed). V4: THEOREM ROUTE from label-dual inverses (EQ-A T5; replayed). Exact transitivity with V4 and a
  countable tower are incompatible (EQ-E (v)); the dense form is the consistent one.
- N3.3 Richness: Theorem BP-S makes SS the precise premise (with Spec2) for K∞-Trans. Decisive test: is SS implied by
  a connected group transitive on the pure states, a swap for every frame, Spec2, capacity two and full effects?
  No — bidisk (SO(2)², abelian) and Stiefel orbitope (SO(3), non-abelian) satisfy all of these and fail SS
  (`c3_ops.py` 10/10, with `c3_bp.py` BD/ST). SS: INDEPENDENT PREMISE, QM-true at every level.
- N3.4 Harness error, recorded: `c3_ops` run 1 (kept as `c3_ops.run1.py`/`.run1.out`, 9/10) used m = (1/3,−2/3,2/3)
  as a unit vector orthogonal to n = (2/3,1/3,2/3); m·n = 4/9. Fixed to (1/3,2/3,−2/3) and the check now asserts
  m·n = 0 and |m| = 1 itself. Same decision rule; run 2 10/10.

### N4 — C2(a) C7b as a Lean-ready signed-permutation gate

- `c2a_c7b.py` 17/17. The table rule reproduces the landed gC5 tables exactly (sgnC5 RC5:89, pcC5 RC5:94, ptC5
  RC5:104) and BAL's C7b. The NOT is already landed: `OddChar.nK 3` = diag(1,1,1,−1,−1,−1,−1) with axis `zK 3` = e₇,
  `isNot_nK` OC:102, balance `finrank_plus_eq_finrank_minus_nK` OC:176. Only the gate is new.
- Label error, recorded: run 1 of `c2a_c7b.py` cited the gC5 tables as "RC5:111-131"; the declarations are at
  RC5:89/94/104. Only the label text changed (the computation is unchanged); the recorded replay uses the corrected
  label.

### N5 — C2(c) type covariance over CtrlGate; C2(d) relC ⇔ CI ∧ TR

- `c2d_relc_split.py` 9/9 (run 1). Own implementation (not EQ-B's code). Four instances realize all four
  (CI, TR) patterns: cnot (T,T), gC5 (T,F), C7b (F,F), cnot′ = cnot with the −z slice acting by
  homMap(diag(−1,1,−1)) (F,T). On each, relC = CI ∧ TR and relC on span(hom z, hom(−z)) ⊗ H = CI. With the kernel
  reading (relC read at RSB:95 only for CI, RSB:103; full relC at RSB:746 → RSP:329) this confirms EQ-B T1 and
  BAL B4's split.
- `c2c_typecov.py`: run 1 (kept: `.run1.py`, `.run1.out`, 6/7) FAILED TC.5: the countercontrol rotation was about x,
  which moves z but commutes with nflip, so the frame survived. Harness error in the choice of countercontrol, and a
  real observation: "g z = z" is sufficient, not necessary, for the frame of actT g⁻¹ ∘ G ∘ actT g (what the frame
  needs is that g⁻¹ N_B M₀ g and g⁻¹ M₀ g act correctly on ±z). Run 2 uses a rotation about y (moves z, does not
  commute with nflip: frame breaks) and keeps the x-rotation as a control. Run 2's static verdict string still said
  "the conjugating map must fix z" — an overclaim against TC.5's own control; corrected in run 3 (7/7). The
  recorded replay is of the corrected script.

### N6 — C2(b) EQ-D T1 / T4 refined against the K3 modules

- `c2b_drive_lift.py` 9/9 (run 2; run 1 was 8/8 without the D6 mutation self-test, added because the run took under a
  second and a comparator that always answers "equal" would have passed D1–D4; D5 and D6 show it rejects).
- Refinements found by reading the kernel text: (r1) `DrivesElementary` (SS:77) quantifies over all a, b including
  a = b, where `transition a a = 2 E_aa`; the a = b flows are the relabelled `flow (transition 0 0) t` (D3) — this is
  why hflow₀ is a hypothesis. (r2) `permMatrix (Equiv.swap a a) = 1` via `Equiv.swap_self` and `permMatrix_one'`
  (LRS:228) and `Architecture.one`. (r3) `ancBlock_tensorOf_one` (MR:488) is stated only for carriers `A × Fin n`;
  T1 needs it for an arbitrary carrier (cheap copy). (r4) D = `tensorOf 1 ((phaseGate 0)^2)` needs no relabelling:
  it commutes with the relabelled pair term and anticommutes with every other (r,0)–(r,1) term (D1 at all 40 ordered
  pairs in Fin 2..5; EQ-D used reindex τ). (r5) the exp algebra is available in the local v4.33 tree
  (`Matrix.exp_blockDiagonal` for `tensorOf U 1`, `Matrix.exp_units_conj` for reindex and for D,
  `Matrix.exp_add_of_commute`), or a closed-form lemma `flow_transition_apply` (moderate) replaces it.
- T4: the Architecture/LabelInvariant/DaggerStable halves reuse the landed monomial-class lemmas
  (`substratumClass_arch` SCl:231, `_labelInvariant` SCl:275, `_daggerStable` SCl:289) plus the arithmetic lemma
  (K1: c·m = 2^j, m ≥ 1 ⇒ c = 2^i). The block clause is where the arithmetic is used.

### N7 — assumption-watch marker (NEW-borderline, productivity clause (c)): "balance" is the selector's conclusion in disguise

The selector's last step is `NativeGateBall.dim_of_bounds (p q d) (hp : p ≤ 1) (hpq : p = q) (hd : p + q + 1 = d)`
(NGB:248, `omega`). The block reduction supplies p ≤ 1 (RSB:716 → `p_le_one_of_blockData` CD:722) and reads relC only
through the corner identity CI (RSB:95 → :103). Balance (finrank plusSpace = finrank minusSpace) is exactly hpq. So,
with CI (hence p ≤ 1) in hand, balance ⇔ [d ∈ {1,3} and (d = 3 → p = 1)]: a selector that takes CI and balance as its
two premises (BAL's restated B4 selector, listed by BAL as a candidate freeze) assumes its conclusion modulo the block
bound. It is a correct SEPARATION device (it shows each half of relC is needed: C7b, gC5) but not a foundation. In the
foundational form the second premise must be TR (a gate relation that mentions no dimension), from which balance is
DERIVED by the operator-space count (RSP:329). Cross-propagation: any proposal that "relC = CI + parity" should state
the second half as TR, not as balance. A further consequence: CI alone involves only the TARGET's NOT (the control
enters through hom(−z) = homMap N (hom z)), so the two-NOT / type-covariance question (K∞-Copy) is carried entirely by
TR — the half that cannot be replaced by a kinematic property without assuming the conclusion.

### N8 — design caution for Spec2 / SS on the gate route (found while assembling the C1 ledger)

With `avail` = the stage effects of a countably indexed tower (the only consistent choice with V4, EQ-E S4), only
countably many antipodal pairs of the ball are perfectly distinguishable BY AVAILABLE EFFECTS, so Spec2 read with
avail-frames fails (the available diameters are a null set). Spec2 and SS must read frames through `fullEffects` of the
chart body (or the pointwise closure of `avail`), and SS must be the DENSE form (the group is countable). Theorem BP-S
does not use distinguishability at all (only that frames are pairs of distinct extreme points, swap-closed and
G-invariant), so this changes the operational reading, not the proof. Kernel-side converse: on `ball3` the landed
`boundaryTransitive_ball3Drive` (ON:667) gives SS for antipodal frames exactly (affine automorphisms of the ball fix
its centre, so g(−x) = −g x).
