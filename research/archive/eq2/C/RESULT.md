# EQ2-C — the quantum building blocks: the qubit's dimension on the gate route, and which K∞ assumptions can be derived

Design only. Nothing is adopted, frozen or governed. Base: certified main `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`,
read-only at `scratchpad/eq/base/`. No Lean was built (no toolchain): every Lean statement is **UNBUILT**.
"Kernel" means a landed identifier at the base, cited `file:line`; all 198 such citations here were checked
mechanically at their lines (`c1_cite.py`). Mathlib availability was checked only against a local source tree whose
`lean-toolchain` reads v4.33.0, matching the base pin (`lakefile.toml`: `rev = "v4.33.0"`); nothing was compiled.
Literature is unverified unless stated: arxiv.org is egress-blocked. Running record: `NOTES.md` (productivity test
fixed first; nodes N0–N8).

Module abbreviations (files `verification/lean-mathlib/OIBridge/<Module>.lean`): SC StageCompletion,
CA CompletionAction, KF KInfFoundations, OG OrbitGeneration, ON OrbitNormalization, TB TransitiveBody,
IIP InvariantInnerProduct, ES EffectSpace, DO DenseOrbit, K1B K1Bridge, CD CompositeDimension, NGB NativeGateBall,
RSB RelcSelectBlock, RSP RelcSelectParity, RC5 RelcSelectC5, OC OddChar, PN ParityNot, K2G K2Guard, ST SharpTests,
IL ImplementationLocality, SS SubstratumSource, SCl StructuralClosure, MR MinimalRepertoire, LRS LieRankSource,
RS ReachabilitySeam, AC AncillaClosure, CL CoherentLift, MC MonoidalCompletion, SI SubstratumInterface,
MRv MicroscopicReversibility, LOS LevelOneSeam, TC TypedCompletion, CGOP CarrierGeneralOIPlus,
CI CompositeInterface, OA OperationalAssembly.

## 1. Finding

On the gate route the d = 3 statement composes from landed theorems plus a handful of cheap adapters. Its hypotheses
reduce to fifteen independently required assumptions:
- an OI stage tower with SC∞;
- FiniteRank;
- a sharp stage seed;
- prefix-closed protocol effects with inverse-closed action menus, which supply the K∞-Act data and, through label
  duals, K∞-V4;
- two level-uniform principles in place of K∞-Trans:
  - **Spec2**: every state is a mixture of a perfectly distinguishable pair of pure states;
  - **SS**: the reversible maps act transitively, or densely, on ordered such pairs;
- the locally tomographic two-token carrier with a common type chart;
- the gate data, with 2 ≤ d:
  - a NOT, the frame and two-sided positivity;
  - the corner identity **CI** and the tangent relation **TR** (together exactly relC);
  - type covariance.

The new theorem is BP-S (written, kernel-cheap because the centroid lemmas are landed): Spec2 + SS give boundary
purity (BP) and boundary transitivity. Both premises hold in finite-dimensional complex QM at every level, whereas BP
fails at the qutrit. Each premise is load-bearing, exactly:
- the regular pentagon is strongly self-dual, has capacity two and SS, and has neither Spec2 nor BP;
- the bidisk and the Stiefel orbitope have Spec2, connected groups transitive on their pure states and a swap for
  every frame, and have neither SS nor BP;
- the qutrit has Spec and SS with frames of three, and no BP.

So BP at capacity two follows from more basic, level-uniform principles. The self-duality avenue fails (the pentagon),
and the singleton-face and sharp-update avenues only relocate BP.

FiniteRank remains an independent premise:
- FiniteRank ⇔ UFR ∧ (N), where UFR is uniform finite resolution and (N) is uniform norming (written; Riesz both ways;
  no Kakutani step). Each clause is independent: the ellipsoid tower has UFR without (N), the ℓ² tower (N) without UFR;
- an exact OI-shaped renewal tower shows that the protocol-tower structure supplies neither clause;
- whether the gate premises force FiniteRank is open at two named walls.

Reversible operations:
- the operation data and V4 have theorem routes;
- the richness K∞-Trans needs, SS, does not follow from continuous transitive reversibility with frame swaps (the
  bidisk and the Stiefel orbitope).

C2 results:
- C7b is Lean-ready as a signed permutation on the landed `nK 3`;
- relC ⇔ CI ∧ TR is confirmed on all four truth patterns;
- type covariance is refined to the CtrlGate form, so no relT is needed;
- EQ-D T1/T4 are refined: the a = b clauses, a general-carrier block lemma, and a D that needs no relabelling.

Assumption-watch: a selector that takes CI plus *balance* assumes its conclusion modulo the block bound. The
foundational second half is TR, which alone carries the control's NOT.

## 2. Target theorems (UNBUILT)

Layers follow INTEGRATION-DESIGN v2 §2: the gate route is layer (II-1), chart existence for one token, carried to
d = 3; C2(b) belongs to (II-4).

### 2.1 G3 — the d = 3 statement on the gate route (layer II-1 with K1; forward)

```lean
namespace OIBridge.GateRoute
open StageCompletion CompletionAction OrbitGeneration OrbitNormalization TransitiveBody DenseOrbit
open EffectSpace K1Bridge CompositeDimension RelcSelect

/-- S13: the relative two-NOT control gate (no `CtrlGateOf` exists at the base). -/
structure TwoNotCtrlGateOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ)
    (NA NB : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where
  frame  : ∀ a b : Fin 2, T (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail
  relC   : ∀ ω, actC NA (T (actC NA ω)) = actT NB (T ω)

/-- type covariance (EQ-E T2's hypothesis; the K∞-Copy obligation in type form) -/
def TypeCovariant (z : Fin d → ℝ) (NA NB : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : Prop :=
  ∃ g : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ), g z = z ∧ (∀ x, x ∈ eball d ↔ g x ∈ eball d) ∧ ∀ x, NB (g x) = g (NA x)

/-- the two tokens' gate data, read in a ball chart `A` of their common type -/
def GateDataIn {D : DirectedStages} (C : CompletionChart D) (avail : Set ((Fin C.d → ℝ) →ᵃ[ℝ] ℝ))
    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) : Prop :=
  ∃ z NA NB T, IsNot (eball C.d) z NA ∧ TwoNotCtrlGateOf (eball C.d) (effTr A '' avail) z NA NB T
    ∧ TypeCovariant z NA NB

theorem three_of_gateRoute {D : DirectedStages} (C : CompletionChart D)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))} (hG : PreservesBody (chartBody C) G)
    (hT : DenseBoundaryOrbit (chartBody C) G)                    -- from Spec2 + FrameDense (§2.2)
    {r : (Fin C.d → ℝ) →ᵃ[ℝ] ℝ} (hP1 : SharpSeed (chartBody C) r)
    {avail : Set ((Fin C.d → ℝ) →ᵃ[ℝ] ℝ)} (hE : ∀ e ∈ avail, IsEffectOn (chartBody C) e)
    (hV4 : SeedOrbitAvailable G r avail) (h2 : 2 ≤ C.d)
    (hgate : ∀ A, A '' chartBody C = eball C.d → GateDataIn C avail A) : C.d = 3
```

**Route.**
1. `chartBody_eq_eball_of_dense` (DO:209) gives A.
2. Transport along A. `hypotheses_tr` (ON:295) and `isEffectOn_tr` (ON:217) do this; for the dense form of
   transitivity the new adapter `denseBoundaryOrbit_tr` is needed.
3. Cone equality: `maxConeOf_avail_eq_of_dense` (DO:243).
4. `ctrlGate_of_cone_eq`, which is new and mirrors K1B:73.
5. `ctrlGate_of_typeCovariant` (§2.6).
6. `dim_of_ctrlGate` (RSB:739) with h2, or `three_of_ctrlGate` (RSB:753) with an entangling clause.

**Upstream.**
- C comes from FiniteRank: `exists_completionChart` CA:154.
- The seed on the chart: `sharpSeed_completion` SC:224, then `hypotheses_restrict` ON:529.
- G: the induced equivalences of the operation data, `preservesBody_inducedEquiv` CA:352, assembled by the new
  `inducedGroup`.
- With `avail` the restricted and transported stage effects, hE is kernel: SC:193, ON:423, ON:217.
- The dense forms are forced by EQ-E's seam S4.

### 2.2 BP-S — boundary purity and transitivity from Spec2 + SS (layer II-1; forward; QM converse)

```lean
namespace OIBridge.FramePurity
/-- frames: ordered pairs of distinct extreme points, swap-closed (for operational frames, perfect distinguishability
by `fullEffects` — not by a countable `avail`, NOTES N8) -/
structure FrameSystem (Ω : Set (Fin d → ℝ)) where
  F : (Fin d → ℝ) → (Fin d → ℝ) → Prop
  extreme : ∀ x y, F x y → x ∈ Ω.extremePoints ℝ ∧ y ∈ Ω.extremePoints ℝ
  ne : ∀ x y, F x y → x ≠ y
  swap : ∀ x y, F x y → F y x
def Spec2 (Ω) (Fr : FrameSystem Ω) : Prop :=
  ∀ w ∈ Ω, ∃ x y, Fr.F x y ∧ ∃ p : ℝ, 0 ≤ p ∧ p ≤ 1 ∧ w = p • x + (1 - p) • y
def FrameTransitive (Fr : FrameSystem Ω) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) : Prop :=
  ∀ x y x' y', Fr.F x y → Fr.F x' y' → ∃ g ∈ G, g x = x' ∧ g y = y'
def FrameDense (Fr : FrameSystem Ω) (G) : Prop :=
  ∀ x y x' y', Fr.F x y → Fr.F x' y' → (x', y') ∈ closure ((fun g => (g x, g y)) '' G)
theorem frame_midpoint_eq_centroid (hc : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty)
    (hG : PreservesBody Ω G) (hS : Spec2 Ω Fr) (hD : FrameDense Fr G) {x y} (h : Fr.F x y) :
    (1 / 2 : ℝ) • (x + y) = centroid Ω
theorem extreme_of_isBoundaryState_of_spec2 (…same…) {w} (hw : IsBoundaryState Ω w) : w ∈ Ω.extremePoints ℝ  -- BP
theorem denseBoundaryOrbit_of_spec2 (…same…) : DenseBoundaryOrbit Ω G
theorem boundaryTransitive_of_spec2 (…; hT : FrameTransitive Fr G) : BoundaryTransitive Ω G
-- converse (QM, capacity two), from landed facts: antipodal frames of ball3 and ON:667
theorem spec2_ball3 : Spec2 ball3 antipodalFrames
theorem frameTransitive_ball3Drive : FrameTransitive antipodalFrames driveWords3
-- countercontrol: the bidisk (rational coordinates): Spec2 holds, FrameTransitive fails for EVERY G with PreservesBody
theorem not_frameTransitive_bidisk (G) (hG : PreservesBody bidisk G) : ¬ FrameTransitive bidiskFrames G
```

**Written proof** (every step re-read against the kernel definitions; NOTES N1.3).
1. The centroid c is fixed by every member of G (TB:356).
2. c ∈ Ω (TB:388). By Spec2, c = p x + (1 − p) y for a frame (x, y).
3. Frames are swap-closed, so a sequence g_n ∈ G carries (x, y) to (y, x); in the exact case a single g does.
4. Then c = p y + (1 − p) x, so p = 1/2.
5. Carrying (x, y) to any frame (x′, y′) shows that every frame has midpoint c. So Ω is a union of segments
   [x, 2c − x] and is centrally symmetric about c.
6. c is interior: it is the midpoint of an interior point and its reflection.
7. A boundary state w = c + t(x − c) must have |t| = 1. Otherwise w lies on [c, x) or [c, 2c − x), which is interior
   (Mathlib `Convex.openSegment_interior_self_subset_interior`, local tree Convex/Topology.lean:148), and interior
   points are not boundary states (KF:601).
8. So every boundary state is a frame member, hence extreme: BP. Extreme points are boundary states (TB:284), so every
   extreme point is a frame member, and FrameDense (or FrameTransitive) gives DenseBoundaryOrbit (or
   BoundaryTransitive).

The proof uses no group structure on G and no effects beyond the definition of frames.

### 2.3 FR-R — FiniteRank as uniform finite resolution plus norming (layer II-1; both directions)

```lean
def stageDist (D : DirectedStages) (i : D.ι) (x y : CSpace D) : ℝ := ⨆ e : (D.stage i).E, |x ⟨i, e⟩ - y ⟨i, e⟩|
def UFR (D) : Prop := ∀ ε > 0, ∃ i, ∀ x ∈ body D, ∀ y ∈ body D, ‖x - y‖ ≤ stageDist D i x y + ε
def UniformNorming (D) : Prop := ∃ κ > 0, ∀ v ∈ vectorSpan ℝ (body D), ‖v‖ ≤ κ → v ∈ body D -ᵥ body D
theorem finiteRank_of_ufr_norming (hSC : SCInf D) (hu : UFR D) (hn : UniformNorming D) : FiniteRank (body D)  -- Riesz
theorem ufr_norming_of_finiteRank (hSC : SCInf D) (hne : (body D).Nonempty) (h : FiniteRank (body D)) :
    UFR D ∧ UniformNorming D                                         -- Heine–Borel, relative interior, Dini
theorem isCompact_body_iff_ufr (hSC : SCInf D) : IsCompact (body D) ↔ UFR D  -- Dini one way, total boundedness other
```

The two directions have separate witnesses (§A.34):
- (⇐) Riesz, `FiniteDimensional.of_isCompact_closedBall₀` (local tree Analysis/Normed/Module/FiniteDimension.lean:475).
  The κ-ball of the span is closed inside the compact body − body.
- (⇒) a closed bounded subset of a finite-dimensional affine subspace is compact, Dini gives UFR (local tree
  Topology/UniformSpace/Dini.lean:95, `Monotone.tendstoUniformlyOn_of_forall_tendsto`; the stage distances increase
  along the directed index by SC∞), and a finite-dimensional convex body has a relative interior point, which gives (N).

### 2.4 C2(a) — C7b at d = 7 (layer II-1, separation; `c2a_c7b.py` 17/17)

The NOT is already landed: `OddChar.nK 3` = diag(1,1,1,−1,−1,−1,−1) (OC:56), with axis `zK 3` = e₇ (OC:59), IsNot
`isNot_nK 3` (OC:102) and balance `finrank_plus_eq_finrank_minus_nK 3` (OC:176). Only the gate is new; it follows
gC5 (RC5:89–393).

```lean
def sgnC7b (μ ν : Fin 8) : ℝ :=
  if ((μ = 1 ∨ μ = 3 ∨ μ = 5) ∧ (ν = 3 ∨ ν = 5 ∨ ν = 7)) ∨ ((μ = 2 ∨ μ = 4 ∨ μ = 6) ∧ (ν = 2 ∨ ν = 4 ∨ ν = 6))
  then -1 else 1
def pcC7b : Fin 8 → Fin 8 → Fin 8   -- μ = 0: ν ≤ 1 ↦ 0, else 7;  μ = 7: ν ≤ 1 ↦ 7, else 0;
                                    -- μ ∈ 1..6: ν ≤ 1 ↦ μ, else J μ  (J: 1↔2, 3↔4, 5↔6)   (full table: c2a_c7b.out)
def ptC7b : Fin 8 → Fin 8 → Fin 8   -- μ ∈ {0,7}: ν;  μ ∈ 1..6: 0 ↦ 1, 1 ↦ 0, else K ν  (K: 2↔3, 4↔5, 6↔7)
def gC7bFun (ω : W 7) : W 7 := fun μ ν => sgnC7b μ ν * ω (pcC7b μ ν) (ptC7b μ ν)
def gC7b : W 7 ≃ₗ[ℝ] W 7                          -- self-inverse, as gC5 (RC5:134)
theorem gC7b_frame (a b : Fin 2) : gC7b (prodState (corner (zK 3) a) (corner (zK 3) b))
    = prodState (corner (zK 3) a) (corner (zK 3) (a + b))
theorem gC7b_relT (ω) : actT (nK 3) (gC7b (actT (nK 3) ω)) = gC7b ω
theorem gC7b_relC_lhs : actC (nK 3) (gC7b (actC (nK 3) (OddChar.entW 0 2))) 7 2 = -1   -- rhs: = 1
theorem gC7b_not_relC : ¬ ∀ ω, actC (nK 3) (gC7b (actC (nK 3) ω)) = actT (nK 3) (gC7b ω)
theorem gC7b_not_cornerId :                                                   -- CI fails at Y = e₂
    ¬ ∀ Y, gC7b (tens (hom (-(zK 3))) Y) = tens (hom (-(zK 3))) (homMap (nK 3) (Mfwd (zK 3) gC7b Y))
theorem prodEffVal_gC7b_prodState (e f) (x y : Fin 7 → ℝ) : prodEffVal e f (gC7b (prodState x y)) =
    (ehom e 0 + x 6 * ehom e 7) * (ehom f 0 + ehom f 1 * y 0)
  + (ehom e 7 + x 6 * ehom e 0) * (ehom f 2 * y 1 + ehom f 3 * y 2 + ehom f 4 * y 3 + ehom f 5 * y 4
                                   + ehom f 6 * y 5 + ehom f 7 * y 6)
  + (ehom e 1 * x 0 + ehom e 2 * x 1 + ehom e 3 * x 2 + ehom e 4 * x 3 + ehom e 5 * x 4 + ehom e 6 * x 5)
      * (ehom f 0 * y 0 + ehom f 1)
  + (ehom e 2 * x 0 - ehom e 1 * x 1 + ehom e 4 * x 2 - ehom e 3 * x 3 + ehom e 6 * x 4 - ehom e 5 * x 5)
      * (ehom f 3 * y 1 - ehom f 2 * y 2 + ehom f 5 * y 3 - ehom f 4 * y 4 + ehom f 7 * y 5 - ehom f 6 * y 6)
theorem gC7b_posFwd : ∀ x ∈ eball 7, ∀ y ∈ eball 7, gC7b (prodState x y) ∈ maxCone (eball 7)
theorem gC7b_posInv : ∀ x ∈ eball 7, ∀ y ∈ eball 7, gC7b.symm (prodState x y) ∈ maxCone (eball 7)
theorem balanced_relT_not_dimension_selecting : ¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N) (G : W d ≃ₗ[ℝ] W d),
    IsNot (eball d) z N → Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) →
    (∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) →
    (∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) →
    (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) →
    (∀ ω, actT N (G (actT N ω)) = G ω) → d = 1 ∨ d = 3
```

**Positivity, Lean-level.** The value identity has been checked symbolically (T4.1). From it, 8-variable versions of
`selC5_target` (RC5:242) and `selC5_core` (RC5:303) follow, with Bessel inequalities for J on six tangent coordinates
and for K on six target coordinates. BAL's identities I1–I6 are the exact algebra (T4.2), and the bound is tight at the
witness (value 0; the 2J variant gives −1).

**Type caution.** `nK 3 : (Fin (2*3+1) → ℝ) →ₗ …` lives at `d = 2*3+1`. Either state the module at that `d`, or
transport by `(2*3+1 : ℕ) = 7`.

### 2.5 C2(b) — EQ-D T1 and T4, refined (layer II-4, the repertoire half; `c2b_drive_lift.py` 9/9)

```lean
theorem drivesElementary_of_qubit {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (hphase : 𝓘 (Fin 2) (phaseGate (0 : Fin 2)))
    (hflow₀ : ∀ t : ℝ, 𝓘 (Fin 2) (flow (transition (0 : Fin 2) 0) t))   -- needed for the a = b clauses
    (hflow₁ : ∀ t : ℝ, 𝓘 (Fin 2) (flow (transition (0 : Fin 2) 1) t)) :
    DrivesElementary 𝓘
def cardSplitClass : ImplementationClass := fun S _ _ K => (∃ j : ℕ, Fintype.card S = 2 ^ j) ∨ IsMonomial K
theorem cardSplit_independence : Architecture cardSplitClass ∧ LabelInvariant cardSplitClass ∧
    DaggerStable cardSplitClass ∧ ¬ ContextStable cardSplitClass ∧ ¬ DrivesElementary cardSplitClass
theorem cardSplit_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (genTheory cardSplitClass cardSplit_arch (Fin 2))
```

Refinements found by reading the kernel text:
- **(r1)** `DrivesElementary` (SS:77) quantifies over every a, b, including a = b. There `transition a a = 2 E_aa`
  (LRS:199), so flow (transition a a) t is a diagonal phase. This is the relabelled `flow (transition 0 0) t`,
  which is why hflow₀ is a hypothesis (D3).
- **(r2)** For a = b, `permMatrix (Equiv.swap a a) = 1` follows by `Equiv.swap_self` and `permMatrix_one'` (LRS:228),
  and `Architecture.one` then gives the clause.
- **(r3)** `ancBlock_tensorOf_one` (MR:488) is stated only for carriers `A × Fin n`. T1 needs a general-carrier copy:
  ancilla second (AC:457), `1_R` first (IL:359).
- **(r4)** D = `tensorOf 1 ((phaseGate 0)^2)` needs no relabelling (EQ-D used reindex τ). It commutes with the
  relabelled pair term and anticommutes with every other term (D1: all 40 ordered pairs in Fin 2..5).
- **(r5)** Swaps for a ≠ b: `phaseGate a * phaseGate b * flow (transition a b) (π/2) = permMatrix (swap a b)` (D4).
- **(r6)** The exp algebra is in the local v4.33 tree, in Analysis/Normed/Algebra/MatrixExponential.lean:
  `Matrix.exp_blockDiagonal` (:87, for `tensorOf U 1`), `Matrix.exp_units_conj` (:156, for reindex and for D) and
  `Matrix.exp_add_of_commute` (:130). Alternatively, a closed-form lemma `flow_transition_apply` (moderate) replaces
  them; it rests on T² = E_aa + E_bb and T³ = T (D0).
- **T4.** Architecture, LabelInvariant and DaggerStable reuse SCl:231/275/289, plus the arithmetic lemma
  c·m = 2^j, m ≥ 1 ⇒ c = 2^i (K1). The witnesses are exact (K2). `cardSplit_not_qm` is EQ-D's argument through
  `realized_of_instAvail` (IL:530) and `preservesDiag_conj_of_monomial` (SI:126): every carrier in an `InstAvail`
  derivation at level 3 has 6m elements, never a power of 2.

### 2.6 C2(c) — EQ-E T2 for the gate route's CtrlGate (layer II-1/K1; forward; `c2c_typecov.py` 7/7)

```lean
noncomputable def actTEquiv (g : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ)) : W d ≃ₗ[ℝ] W d     -- inverse actT g.symm
theorem actT_comp (A B) (ω : W d) : actT A (actT B ω) = actT (A ∘ₗ B) ω          -- CD:471 is involution-only
theorem actC_actT_comm (N M) (ω : W d) : actC N (actT M ω) = actT M (actC N ω)
theorem maxCone_actT {A} (hA : ∀ x ∈ eball d, A x ∈ eball d) {ω} (h : ω ∈ maxCone (eball d)) :
    actT A ω ∈ maxCone (eball d)
theorem ctrlGate_of_typeCovariant {g : (Fin d → ℝ) ≃ₗ[ℝ] (Fin d → ℝ)} (hgz : g z = z)
    (hgΩ : ∀ x, x ∈ eball d ↔ g x ∈ eball d) (hconj : ∀ x, NB (g x) = g (NA x))
    (hG : TwoNotCtrlGate (eball d) z NA NB G) :          -- frame, P±, relC(NA, NB); NO relT
    CtrlGate (eball d) z NA ((actTEquiv g).trans (G.trans (actTEquiv g).symm))
```

**Proof.** Write T̃ = actT g⁻¹ ∘ G ∘ actT g.
- relC: actC and actT commute (TC.7), and actT g⁻¹ ∘ actT N_B = actT (N_A g⁻¹).
- Frame: g fixes ±z.
- Positivity: `actT_prodState` (K2G:173) and `maxCone_actT`.

QM instance: the kernel cnot with (N_A, nflip) and g a rotation about z (TC.1–3). The hypothesis g z = z is sufficient
but not necessary: a rotation about x moves z, commutes with nflip and keeps the frame (TC.5 control). Type covariance
is load-bearing: gC5 with NB-1's C2N pair satisfies every two-NOT clause, and no g exists, since the traces are −1 and
−3 (TC.6).

### 2.7 C2(d) — relC ⇔ CI ∧ TR (layer II-1; forward; `c2d_relc_split.py` 9/9)

```lean
def CornerId (z) (N) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  ∀ Y : HVec d, G (tens (hom (-z)) Y) = tens (hom (-z)) (homMap N (Mfwd z G Y))
def TangentRel (z) (N) (G : W d ≃ₗ[ℝ] W d) : Prop :=
  ∀ c : Fin d → ℝ, (∑ j, c j * z j) = 0 → ∀ Y, actC N (G (actC N (tens (lift c) Y))) = actT N (G (tens (lift c) Y))
theorem relC_iff_corner_and_tangent (hN : IsNot (eball d) z N)
    (hframe : ∀ b : Fin 2, G (prodState z (corner z b)) = prodState z (corner z b))
    (hpos : ∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) :
    (∀ ω, actC N (G (actC N ω)) = actT N (G ω)) ↔ CornerId z N G ∧ TangentRel z N G
theorem blockData_of_cornerGate (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hframe…) (hP± …) (hCI : CornerId z N G) :
    BlockData (tangentPlus N)        -- RSB §B–§D restated: RSB reads relC only at :95, used only at :103
```

**Proof of the equivalence.**
- Control decomposition: HVec = span(hom z, hom(−z)) ⊕ lift(z^⊥), using `hom_eq_add_lift` CD:1646 and
  `hom_add_hom_neg` CD:1735. homMap N preserves both summands (S.1).
- On the classical sector, relC is CI: use `corner_form` CD:1805 at z and `actC_tens` / `actT_tens` CD:1930/1923.
- On the tangent sector, relC is TR by definition.

Four exact instances realize all four truth patterns (S.2): cnot (T,T), gC5 (T,F), C7b (F,F), cnot′ (F,T).

Caution (NOTES N7): `dim_of_cornerGate_balanced` (CI plus balance) is a separation device, not a foundation. Given CI's
block bound p ≤ 1, balance is equivalent to the conclusion through `dim_of_bounds` (NGB:248).

## 3. Hypotheses ledger

Status vocabulary:
- **kernel**: a landed identifier.
- **exact**: a script in this directory.
- **written**: a proof given here or in a cited ledger.
- **unsourced**: no source in OI or the kernel.
- **literature**: an external result, unverified.

### 3.1 The gate route (primary; owner D2)

| # | hypothesis | kernel object | status | QM? | independence evidence |
|---|---|---|---|---|---|
| H1 | an OI stage tower D | `DirectedStages` SC:63 | unsourced: the only instances at the base are controls (SC:342, SC:393, CA:404); oistage's PT/CT are written candidates | yes (IC towers, EQ-E s1) | it is the setting |
| H2 | SC∞ | `SCInf` SC:78 | unsourced; PT by `rfl`, CT from RT:283/398 (oistage, written) | yes | `badD` SC:342 (kernel) |
| H3 | FiniteRank | SC:299 → `exists_completionChart` CA:154 | unsourced. **INDEPENDENT** of the single-system package (EQ-A ℓ² tower; replayed) and of the protocol-tower structure (renewal tower, exact here); FiniteRank ⇔ UFR ∧ (N) (written here) | yes | ℓ² tower: (N) without UFR. Ellipsoid tower: UFR without (N). Renewal tower: neither |
| H4 | a sharp stage seed (values 1 and 0 at two stage preparations) | `sharpSeed_completion` SC:224 | unsourced stage data; the completion step is kernel | yes | SIC tower: no available sharp seed (EQ-A; replayed) |
| H5 | operation data: `OpDatum`, `AffineRespect`, inverse data (`Undoes`) | CA:46/58/325 → `preservesBody_inducedEquiv` CA:352 per datum | **THEOREM ROUTE** from prefix-closed protocol effects and inverse-closed action menus (oistage F-S1; replayed). These two are the premises | yes on IC towers; StateRespect fails on non-IC towers (EQ-E s1) | `midOp_not_affineRespect` CA:461 (kernel); observation-only effects with the hidden-bit swap (oistage A3) |
| H6 | the body group G of the induced maps, PreservesBody | OG:69 | derived from H5; seam S2: there is no set-level object, so the new adapter `inducedGroup` is needed | yes | — |
| H7 | K∞-Trans, dense form | `DenseBoundaryOrbit` DO:53 | **derived** from H7a + H7b by BP-S (written; kernel-cheap) | yes at capacity two; no at three or more (qutrit, TB:301) | for K∞-Trans itself: flow (OG:620), square (TB:772), octahedron (TB:862) |
| H7a | Spec2, frames read through `fullEffects` | new | written premise | yes at every level (spectral decomposition) | regular pentagon: SS, capacity two, strongly self-dual, ELEM2; no Spec2 (exact) |
| H7b | SS in the dense form (`FrameDense`) | new | written premise | yes at every level (unitaries on orthonormal bases; rational rotations at capacity two) | bidisk and Stiefel orbitope: SS fails for EVERY body-preserving group, by the centroid (exact) |
| H8 | `avail` ⊆ effects | `EffectsOn` ES:567 | **discharged** for avail = restricted, transported stage effects: SC:193, ON:423, ON:217 (kernel) | yes | — |
| H9 | K∞-V4 | `SeedOrbitAvailable` OG:74 | **THEOREM ROUTE** from label-dual inverses (EQ-A T5, written), which H5 supplies for action words. Countable towers force the dense form (EQ-E S4) | yes (dense) | SIC+axis tower (EQ-A; replayed) |
| H10 | 2 ≤ d | `hasTwoSharpTests_iff` ST:155 | unsourced | yes | d = 1: `two_le_load_bearing_relative` ST:185 (kernel) |
| H11 | the locally tomographic two-token carrier W d with a common type chart | `W` CD:97 | unsourced: K2 (local tomography) plus the kinematic half of K∞-Copy | yes (EQ-E s7) | real QM fails local tomography (EQ-E s7); `no_composite_over_paddedPre` (COMP-1) |
| H12 | the NOT, `IsNot (eball d) z N_A` | CD:210 | unsourced (the gate's specification) | yes (`isNot_nflip` CD:838) | — |
| H13 | the frame | field of `CtrlGate` RSB:45 | unsourced (specification) | yes, for aligned representatives only (EQ-E T6) | — |
| H14 | two-sided positivity on the available cone | `NativeGateOf` K1B:49 pattern | unsourced | yes | `gRev k` (OC): frame and both relations, but posFwd fails |
| H15a | the corner identity CI (target NOT only) | consequence of relC at RSB:99 | unsourced | yes | **C7b**: every other clause and balance hold, CI fails (exact) |
| H15b | the tangent relation TR (carries the control NOT) | the rest of relC, read at RSB:746 → RSP:329 | unsourced | yes | **gC5**: CI holds, TR fails (kernel RC5:179; exact split here) |
| H16 | type covariance | the token form `CopyNatural` KF:284 is unconsumed | unsourced | yes (EQ-E s4; TC.1–2) | gC5 with NB-1's C2N pair (TC.6; traces −1 vs −3) |
| H17 | entangling clause (an alternative to H10) | `EntanglingOf` K1B:64 | unsourced | yes (CD:1380) | `not_entangling_cnot1` CD:2869 |

**Independently required on the gate route:**
- the setting: H1, H2;
- H3, H4;
- H5's two closure premises (prefix-closed protocol effects; inverse-closed action menus);
- H7a, H7b;
- H10 or H17;
- H11;
- the specification: H12, H13;
- H14, H15a, H15b, H16.

**Derived:**
- H6 from H5;
- H7 from H7a and H7b;
- H8 is kernel;
- H9 from H5.

**Not consumed:**
- K∞-Drive (`ElementaryDrivability` KF:264; EQ-E S5);
- `BinaryVisible` SC:244;
- the token form of K∞-Copy (KF:284), replaced by H16;
- relT (the CtrlGate route; RSB:45 has no relT);
- K∞-Geom, `SingletonFaces` and `RelStrictConvex`, which enter only through BP, now supplied by H7a/H7b.

**Global consistency.** EQ-E's two-qubit model M_Q satisfies every landed premise at once, and Spec2 and SS hold
there too, so the list is jointly satisfiable.

### 3.2 Seams S1–S12 (EQ-E §5.2) and new seams, with the adapters

| seam | content | class | adapter or verdict here |
|---|---|---|---|
| S1 | the seed is concluded on `body D`; the selectors read `eball d` | adapter | `ballChart_hypotheses` (EQ-E T5): SC:224 → ON:529 → ON:295 / ON:217. Moderate (bookkeeping) |
| S2 | no set of induced maps | gap → adapter | `inducedGroup` with `preservesBody_inducedGroup` from CA:352. Cheap. Richness stays a premise (H7b) |
| S3 | ∃A; the K1 data are not restated through A | adapter | `ballChart_hypotheses` plus `denseBoundaryOrbit_tr` (ON:295 transports only BoundaryTransitive). Cheap |
| S4 | `stageEffects` versus avail: exact Trans + V4 is impossible on a countable tower | substantive | resolved by the dense route: H7b dense, DO:209/243/299. The frames of H7a are read through `fullEffects` (NOTES N8) |
| S5 | `ElementaryDrivability` is dead on the route | gap | stays off the route (§3.1); continuity is not needed on the gate route |
| S6 | `CopyNatural` is unconsumed | gap → design | `ctrlGate_of_typeCovariant` (§2.6) links H16 to RSB:739 |
| S7 | `HasTwoSharpTests` is composed with no selector | adapter | `three_of_ctrlGate_of_two_le`, a CtrlGate copy of K2G:234, with ST:155. Cheap |
| S8 | W d versus COMP-1's composite over a general V | adapter (coordinate model) / substantive (K2) | unchanged (H11) |
| S9 | real `W 3` versus K3's complex matrices | substantive (Kₙ) | off the d = 3 path (EQ-E T7 is the n = 2 piece) |
| S10 | `ball3` versus `eball d` | closed | TB:671 |
| S11 | `genTheory` versus typed theories | gap | off the d = 3 path |
| S12 | no quantum typed instance | gap | off the d = 3 path (EQ-E T3) |
| **S13** (new) | no relative CtrlGate (`CtrlGateOf`) | adapter | `TwoNotCtrlGateOf` plus `ctrlGate_of_cone_eq` (mirrors K1B:73–138). Cheap |
| **S14** (new) | actT composition: CD:471 covers only involutions; there is no `actTEquiv` and no actC/actT commutation lemma | adapter | §2.6 helpers. Cheap |
| **S15** (new) | no frame vocabulary for K∞-Trans | new premise vocabulary | `FrameSystem`, `Spec2`, `FrameDense` (§2.2) |
| **S16** (new) | the gate's corners must be a frame of the body when the gate is given in chart coordinates | adapter | stated in ball coordinates (`GateDataIn`, ∀A); an O(d)-transport lemma makes "some A" and "every A" equivalent. Moderate |
| **S17** (new, marker) | the BAL B4 selector's "balance" | — | not a foundation (NOTES N7): the second half must be TR |

### 3.3 The continuous route, a separate ledger (owner D2: it never substitutes for §3.1)

| # | hypothesis | status | QM? | independence evidence |
|---|---|---|---|---|
| CR1 | the stage → body → ball chain: H1–H6, and K∞-Trans in a connected form (a closed connected group containing local SO(d) on each token) | as in §3.1; the connected form is stronger than H7 | yes | — |
| CR2 | the locally tomographic carrier (= H11) | unsourced | yes | real QM |
| CR3 | a closed connected group of normalization-preserving reversible maps of an admissible joint cone (products ⊆ K ⊆ maxCone) containing local SO(d)×SO(d) (IE₁) | unsourced (EQ-C IE₁ wall) | yes | K_heis (EQ-C): CX without local SO(3)² |
| CR4 | a non-local element, or a continuous non-product two-sided-positive flow | unsourced | yes | **J/K flow** at d = 5 and 7 (EQ-B, exact): CR4 holds and no d is selected; the local words W5 and W7 violate CR3 |
| CR5 | Krumm–Müller 2019, Theorem 1: for d ≠ 3 the global group is local | literature, unverified | — | — |
| CR6 | FiniteRank (= H3) | as in §3.1 | yes | as H3 |

Not used by the continuous route: H10 (continuity already excludes the segment), H12–H16 (NOT, frame, gate
positivity, CI, TR, type covariance), and H8/H9 when positivity is stated on maxCone. It needs Lie theory (Yamabe,
the closed-subgroup theorem), absent from Mathlib to our knowledge (unverified), and one unverified literature
theorem.

### 3.4 C4 — what each assumption does on the gate route, and whether the continuous route uses it

| assumption | role on the gate route | continuous route |
|---|---|---|
| H1–H4 | the completed body, its chart, the seed | same chain (CR1) |
| H5 (closure premises) | operation data, hence G (H6) and V4 (H9) | uses data too; continuity is free from one infinite-order datum on a finite-rank body (drive F-D2, Cartan; literature) |
| H7a Spec2 + H7b SS | the ball: TRB-1 (DO:209) and the cone (DO:243) | the ball, plus a stronger connected local SO(d) (CR1/CR3) |
| H8, H9 | identify the available cone with maxCone (EFF-1) | only if positivity is stated relative to avail; EQ-B/EQ-C use maxCone |
| H3 FiniteRank | chart dimension d | yes (CR6) |
| H10 / H17 | excludes the bit, d = 1 | no: continuity excludes d = 1 |
| H11 | the carrier W d | yes (CR2) |
| H12, H13, H14 | the gate's specification and positivity | no (positivity of the group instead) |
| H15a CI | block bound p_N ≤ 1 (RSB:716) | no |
| H15b TR | parity p_N = q_N (RSP:329) | no |
| H16 | reduces two NOTs to one (§2.6) | no (automatic at d = 3 with SO(3): EQ-B) |
| CR3, CR4, CR5 | — | the continuous route's own selection mechanism |

## 4. Missing lemmas

**Kernel (new):**
- Cheap:
  - BP-S block. Context: TB:356, TB:388, KF:601, KF:160; Mathlib Convex/Topology.lean:148.
  - `denseBoundaryOrbit_tr` (ON:295 covers only BoundaryTransitive).
  - `inducedGroup` (CA:333/352).
  - `TwoNotCtrlGateOf`, `ctrlGate_of_cone_eq`, `three_of_ctrlGate_of_two_le` (K1B:49–138, K2G:234 patterns).
  - `actTEquiv`, `actT_comp`, `actC_actT_comm`, `maxCone_actT` (CD:198/201, CD:471, K2G:173).
  - `ctrlGate_of_typeCovariant`.
  - `relC_iff_corner_and_tangent` (CD:1639/1646/1735/1805, RSB:60/99).
  - `ancBlock_tensorOf_one'` for a general carrier (MR:488).
  - `cardSplitClass` with its four clauses (SCl:231/275/289).
- Moderate:
  - `blockData_of_cornerGate` (RSB:60–716 restated).
  - `gC7b` and its positivity (selC7 lemmas after RC5:212–369).
  - `drivesElementary_of_qubit` (exp algebra or `flow_transition_apply`).
  - `ballChart_hypotheses` (SC:224, ON:529, ON:295, DO:209).
  - FR-R (SC:128 `CSpace`, SC:141 `body`, SC:299).
  - `three_of_gateRoute` (composition).
- Not needed on the gate route: Lie theory; Kakutani.

**Mathlib** (present in the local v4.33 tree; not compiled):
- `FiniteDimensional.of_isCompact_closedBall₀` (Analysis/Normed/Module/FiniteDimension.lean:475);
- `Monotone.tendstoUniformlyOn_of_forall_tendsto` (Topology/UniformSpace/Dini.lean:95);
- `Convex.openSegment_interior_self_subset_interior` (Analysis/Convex/Topology.lean:148);
- `IsCompact.extremePoints_nonempty` (Analysis/Convex/KreinMilman.lean:64);
- in Analysis/Normed/Algebra/MatrixExponential.lean: `Matrix.exp_diagonal` (:84), `Matrix.exp_blockDiagonal` (:87),
  `Matrix.exp_add_of_commute` (:130), `Matrix.exp_units_conj` (:156).
- Unverified, and continuous route only: Cartan, Yamabe.

**Exact certificates (here):**
- C7b tables, value identity, I1–I6 (`c2a`);
- the drive-lift identities and the cardSplit witnesses (`c2b`);
- type covariance (`c2c`);
- the relC split (`c2d`);
- BP-S controls and foils, including the pentagon over ℚ(√5) (`c3_bp`);
- the renewal tower (`c3_fr`);
- SS independence (`c3_ops`).

A kernel version of the pentagon needs ℚ(√5) arithmetic. It is optional, because the bidisk suffices for SS
independence; only Spec2's independence uses the pentagon.

## 5. Formalization strategy

Suggestions only. Any proposal returns for the owner's separate review.

| round | content | cost | controls / countercontrols a governed round would need |
|---|---|---|---|
| R-A | DriveLift: §2.5 T1 + T4 (owner order 1) | cheap–moderate | `c2b` D0–D6 as frozen probe; countercontrols: cardSplit fails ContextStable (K2), σ = id gives 1 (D5), wrong angle/pair rejected (D6) |
| R-B | BalancedC7: §2.4 (owner order 2) | moderate | `c2a` as frozen probe; controls: table rule reproduces landed gC5 (T0.1); countercontrols: 2J variant negative (T4.3), single sign flips break G²/relT (T5.1) |
| R-C | RelcSplit + CtrlGateBridge: §2.6, §2.7 (first theorem only), S13, S14, S7 | cheap | `c2c`, `c2d`; countercontrols: gC5 + C2N not type covariant (trace), rotation about y breaks the frame, cnot′ (TR ∧ ¬CI) |
| R-D | FramePurity: §2.2 with converse on ball3 via ON:667 | cheap | `c3_bp`; kernel countercontrol: bidisk (rational; SS fails by TB:356); optional ℚ(√5) pentagon for Spec2 |
| R-E | `blockData_of_cornerGate` and the CI + balance selector | moderate | only as a separation statement (NOTES N7) |
| R-F | GateRouteThree: §2.1 with S1–S3, S16 adapters | moderate | QM witness (EQ-E T1 `k1_quantum_witness` + `c2c` instance) to show the hypotheses are jointly satisfiable |
| R-G | FiniteRankResolution: §2.3 | moderate | `c3_fr` and EQ-A's towers as frozen probes (both directions witnessed separately) |

**Order.**
1. R-A, then R-B, as the owner set it.
2. R-C and R-D, which are cheap. They remove K∞-Trans and the relT/two-NOT mismatch from the route.
3. R-F, the composition.
4. R-G.
5. R-E only if a CI-based statement is wanted.

EQ-E T3 (`typedKraus_theory`) and Theorem A′ (the owner's items 3–4) are outside this thread.

## 6. Research questions

| question | classification | evidence |
|---|---|---|
| **BP at capacity two**, avenue: decomposition + symmetry | **THEOREM ROUTE**: Spec2 + SS ⇒ BP and boundary transitivity (dense form too). Both premises are level-uniform in QM; BP is not | written proof §2.2 (re-read step by step against the kernel); `c3_bp.py` 40/40 |
| — Spec2 alone, SS alone | **INDEPENDENT PREMISES** | pentagon (SS without Spec2), bidisk and Stiefel (Spec2 without SS); `c3_bp.py` P5, BD, ST |
| — the capacity-two scope | load-bearing | qutrit: Spec and SS with triples; BP fails (Q3) |
| — avenue: self-duality | **COUNTEREXAMPLE**: self-dual + SS + capacity two ⇏ BP | pentagon strongly self-dual, M = diag(α, Q) exact (P5.12–15). Self-dual + homogeneous (Koecher–Vinberg) is literature, unverified, and needs filters |
| — avenue: singleton faces / sharp update | relocation (non-gem): equivalent to BP at capacity two | KF:575, KF:590; NOTES N1.1 |
| **FiniteRank**, avenue: uniform finite resolution through protocol towers | **INDEPENDENT PREMISE** of the protocol-tower structure; **THEOREM ROUTE** to the operational form FiniteRank ⇔ UFR ∧ (N) (written) | renewal tower: unbounded Hankel rank (12/12 minors) and age states pairwise ≥ 15/38 apart (`c3_fr.py`). Separations: ellipsoid (EL.1), ℓ² (L2.1; EQ-A replayed) |
| — UFR for OI's lattice rules | **OPEN** | wall: an unbounded rank lower bound for the nonlinear rule (rank thread). Ranks ≥ 154 already rule those bodies out as gate-route balls |
| — gate premises ⇒ FiniteRank | **OPEN** | two walls: (i) the parity count (RSP:329) has no infinite-dimensional content (P = 2, Q = ∞); (ii) the infinite-dimensional ball identification (Mazur's rotation problem; literature, unverified) |
| **Reversible operations**: K∞-Act data | **THEOREM ROUTE** from prefix-closed effects + inverse-closed menus | oistage F-S1, replayed byte-identically; wall: no OI-built `DirectedStages` in the kernel |
| — V4 | **THEOREM ROUTE** (label-dual inverses); dense form forced on countable towers | EQ-A T5 (qa2 replayed); EQ-E S4 |
| — K∞-Trans | **THEOREM ROUTE** from Spec2 + SS | as above |
| — SS itself | **INDEPENDENT PREMISE**: not implied by a connected group transitive on pure states with a swap for every frame, Spec2, capacity two and full effects | bidisk (abelian), Stiefel (non-abelian); `c3_ops.py` 10/10 |
| — continuity | not consumed on the gate route; free from one infinite-order datum (written + citation, drive F-D2) | EQ-E S5; OPACT countable no-go (replayed) |

**Converse test in QM and the named foils:**

| | QM qubit | QM level ≥ 3 | qutrit | Carathéodory | square gbit | pentagon | hexagon | bidisk | Stiefel | ℓ² tower | ellipsoid tower |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Spec2 / Spec | ✓ | ✓ (frames of n) | ✓ (triples) | — (cap ≥ 3) | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |
| SS | ✓ | ✓ | ✓ | n/a | ✗ (H.1 + centroid) | ✓ | ✗ (H.4) | ✗ | ✗ | ✓ | ✗ with stage effects |
| BP | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| capacity two | ✓ | ✗ | ✗ | ✗ (exact triple) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| UFR ∧ (N) | ✓ | ✓ | ✓ | ✓ (finite dim) | ✓ | ✓ | ✓ | ✓ | ✓ | (N) only | UFR only |

**Literature.** The search summary for Barnum–Müller–Ududec, *NJP* 16 (2014) 123029 (arXiv:1403.4147), reports the
three single-system postulates — classical decomposability, strong symmetry, no higher-order interference — and that
their non-classical solutions include ball state spaces of every dimension. That is consistent with BP-S. The paper's
formal definitions, and whether it derives the rank-two ball from the first two postulates alone, were not read:
arxiv.org is egress-blocked, so this is unverified. Sources (search results only):
[arXiv:1403.4147](https://www.arxiv.org/pdf/1403.4147), [DOI](https://doi.org/10.1088/1367-2630/16/12/123029),
[Müller's slides](https://mpmueller.net/wp-content/uploads/2024/05/sydney2014slides.pdf).

**§A.31 classification of this pass.**
- **NEW:** Theorem BP-S with its foil table; the CtrlGate form of type covariance with its "sufficient, not necessary"
  observation; the renewal tower; marker N7.
- **ELABORATING:** FR-R (EQ-A Theorem R made Kakutani-free with (N) explicit); the C2(b) refinements.
- **CONFIRMING:** relC ⇔ CI ∧ TR (EQ-B T1, BAL B4); C7b (BAL B1).

Productivity test: met, by clause (a) for BP and clause (c) for N7.

**Fixed point:** not reached. Next passes:
- whether OI's record-writing observation supplies Spec2, through non-disturbing sharp tests with pure posteriors;
- a dimension-free substitute for the parity count.

Consistency axis only; bands unchanged.

## 7. Evidence and probe log

All scripts run as `python3 -I -B` from `scratchpad/eq2/C/`. `run_all.py` runs each twice, requires byte-identical
outputs and exit code 0, replays the prior scripts read-only, and writes `replay.log`. Result: `run_all: OK`.
Hashes are the first 16 hex digits of sha256, from `replay.log`.

| script | sha256 (script) | output | sha256 (output) | checks | verdict |
|---|---|---|---|---|---|
| `c1_cite.py` (arg: the base OIBridge dir) | 749b301bae6d606b | `c1_cite.out` | 2c42f42d570ea83d | 2/2 | CITATIONS-VERIFIED (198) |
| `c2a_c7b.py` | 38feae750ecd2640 | `c2a_c7b.out` | 9f4bef34a60b0449 | 17/17 | C7B-LEAN-READY |
| `c2b_drive_lift.py` | ce432f08879442dc | `c2b_drive_lift.out` | ec7c5b647a67a603 | 9/9 | DRIVE-LIFT-REFINED |
| `c2c_typecov.py` | ca06a8387d13b07c | `c2c_typecov.out` | 75179f1c04c3e7aa | 7/7 | TYPECOV-CTRL |
| `c2d_relc_split.py` | 5b9a16d62e32dfaa | `c2d_relc_split.out` | 475754e5a63b5d43 | 9/9 | RELC-SPLIT |
| `c3_bp.py` | 0519b3ea823b420c | `c3_bp.out` | a72a9d6e57e1669e | 40/40 | BP-SPEC-SS |
| `c3_fr.py` | cf640e6d3d93c260 | `c3_fr.out` | 8e6ff30567c2a2b7 | 8/8 | FR-UFR-N |
| `c3_ops.py` | 1ed76dca3da11cc2 | `c3_ops.out` | a43dc81c5843ca7e | 10/10 | SS-INDEPENDENT |
| prior `oistage/oistage_checks.py` | 38bacf2bf4d7d883 | `replay_prior_out/` | f466ff1f9fd2b26f | 20/20 | identical to `oistage/out.txt` |
| prior `eq/A/qa2_towers.py` | 667e9f8dae949490 | `replay_prior_out/` | 514c898930df0772 | 18 | identical to recorded |
| prior `eq/A/qa3_l2tower.py` | 0d26d2a5aca81ae0 | `replay_prior_out/` | 4264ae70f92a9937 | 14 | identical to recorded |
| prior `opact/opact_checks.py` | a49d8e3562771563 | `replay_prior_out/` | 7317b15412a2447e | 26 | identical to `opact/out.txt` |

**Helpers:**
- `c_common.py`: exact ℚ(√5) arithmetic and the check recorder.
- `replay_prior.py`: read-only runner for prior scripts.
- `vendor_bal/{relt_common,relt_lsig,bal_gates}.py`: verbatim copies of BAL's helpers, sha256 identical to
  `scratchpad/bal/` (02cb7ddb…, 884343c4…, 9c70c3fc…).

**Run history** (kept, not hidden; NOTES N1, N3, N4, N5, N6):
- `c3_bp` (40/40 at run 1). Before run 1: two vacuous `True` checks and one tautology were replaced by real checks, and
  ST.4's irrational instance was fixed.
- `c3_ops`. Run 1 (9/10, kept): the test vector was not orthogonal to n, a harness error; fixed in run 2 (10/10).
- `c2c_typecov`. Run 1 (6/7, kept): the countercontrol rotation commuted with nflip, a harness error that also exposed
  "g z = z is sufficient, not necessary". In run 2 the static verdict string overclaimed "must fix z"; corrected in
  run 3 (7/7).
- `c2a_c7b`: the citation label RC5:111–131 was corrected to RC5:89/94/104 (the computation was unchanged).
- `c2b_drive_lift`: run 2 added the mutation self-test D6.
- `c1_cite`: the citation list was extended from 182 entries (`c1_cite.run1.out`) to 198 before the final replay.
- `replay_prior_out/{oistage_checks,opact_checks,qa2_towers,qa3_l2tower}.{out,err}` (unprefixed) are the first manual
  replay of the prior scripts, made before `run_all.py` existed. Their bytes are identical to the `prior_*.out` files,
  and their stderr is empty.

**Isolation.**
- No file was written outside `scratchpad/eq2/C/`.
- The prior scripts were run read-only under `-B`. The one bytecode cache found, `opact/__pycache__`, is dated
  2026-10-02, before this session.
- `eq/base` was not modified, and `eq2/A` and `eq2/B` were not read.
