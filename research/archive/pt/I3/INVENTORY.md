# I3 — premise inventory: operational foundations and composite reconstruction (stage 6, step 1)

Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only). Governing text `pt/PROTOCOL-STAGE6.md`
(`b277b7c1…`). Paths: kernel modules under `pt/base/verification/lean-mathlib/OIBridge/` (file:line given as
`Module.lean:n`); round notes under `pt/base/verification/programmes/oi-qm/reconstruction/`; `ROADMAP.md` is
`pt/base/verification/ROADMAP.md`; design modules [D] under `pt/inputs/fourcopy/`.

**Record format** (uniform, one block per item, ids `I3.<n>`, never renumbered): `kind` · `level` · `status`; then
`statement` (exact quote: Lean header to `:=`/`where` and docstring, or the manuscript/roadmap sentence); `provenance`;
`depends_on`; `yields`; `bridge`; `bearing`; `flag`. Exact Lean text is reproduced from `kdecls.out`, `kcensus.out`,
`kcensus2.out` (outputs of the scripts in this directory) and from direct reads of the files at the lines given.
Status words are taken from the record that fixes them and never upgraded. "Unsourced" means: the record that fixes the
status says no OI construction supplies it. Two statuses outside the L vocabulary are needed and are marked as such:
`[D]` (design module, kernel-checked in the design run `ff9c3a35`, not certified, not at L) and `PT-record` (a status
fixed by an audited PT stage record, not by the corpus at L).

Abbreviations of the round notes: DIM-1 = `round-dim-1-dimension-selector/result.md`, and likewise EFF-1, K1-BRIDGE-1,
K1-SHARP-TESTS-1, K2-GUARD-1, KTRANS-DENSE-1, NB-1, ODD-CHAR-1, PARITY-NOT-1, RELC-SELECT-1, KINF-1, KINF-2, OG-1,
TRB-1, CMP-1, IIP-1, OPACT-1, ORD-1, COMP-1, KT4-PREM-1.

**Facts used in every `bridge` field** (exact, `kimports.out`): no module of the kernel outside the 22 K-programme
modules imports any of them, directly or transitively; the only non-K module a K module imports is
`CoherentExtension` (by `KInfFoundations`, for the matrix-level `qubit_certain_face`). In the whole kernel, `actT`/`actC`
occur only in `CompositeDimension`, `K1Bridge`, `K2Guard`, `ParityNot` and the four `RelcSelect*` modules, and their
written map argument is always one of: a variable `N`, `nflip`, `neg1`, `nC5`, `n5`, `reflY` (grep of every
occurrence, NOTES 17:21Z). Where `N` is universally quantified with no hypothesis on it, the statement is an algebraic
identity of the carrier maps (`actT_tens`, `actC_tens`, CompositeDimension.lean:1923, :1930; `toOp_actC`, :451;
`actT_prodState`, K2Guard.lean:173: a one-copy linear map carries product states to product states; I3.185); every
statement that constrains pair vectors or a pair cone under `actC`/`actT` concerns an involution of one copy: the NOT of a
hypothesis (`NativeGate`, `GateRel`, `CtrlGate`, `NativeGateOf`, `not_even_of_relC`) or an instance (`nflip`, `neg1`,
`n5`, `nC5`, and through `GateRel` instances `nK k`, `refl3`, `negId3`), or the reflection `reflY`. No kernel declaration
applies `actC`/`actT` to a member of an `ElementaryDrivability` flow, to its `J`, to `cyc3`, to a one-parameter family,
or to a rotation other than the half-turn NOTs (`nflip`, and the NOT variable when it is a π-rotation, I3.24).

***

## §A — the pair carrier `W d` and the native gate (DIM-1, `CompositeDimension.lean`)

### I3.1 `W d`
- kind: definition-as-hypothesis · level: P · status: assumed — the premise the carrier encodes (local tomography);
  ROADMAP.md:997 "the product form of the composite tests, which `W d` encodes (K2)"; K2 OPEN (ROADMAP.md:1001)
- statement (CompositeDimension.lean:95–97): "/-- The joint bilinear carrier of two copies: a real function of a control
  index and a target index. Local tomography is the premise this carrier encodes. -/ abbrev W (d : ℕ) := Fin (d + 1) →
  Fin (d + 1) → ℝ"
- provenance: DIM-1 ("On the bilinear carrier `W d`, which encodes local tomography …"; "Local tomography (the carrier
  `W d`) … named premises of the selectors")
- depends_on: — · yields: every statement of §A–§D and the [D] modules (all pair cones `K ⊆ W 3`)
- bridge: n/a (level P). The adapter "from COMP-1's `Composite` to the carrier `W d`" is open (DIM-1 "What stays open");
  the coordinate model of `CompositeInterface` §E is the same function space, "confined to the instances"
- bearing: direct constraint on `K` (fixes the carrier of every pair cone; LT built in) · flag: —

### I3.2 `prodState`
- kind: definition-as-hypothesis · level: P · status: proved [K] (definition); the clause "products in `K`" is a
  hypothesis wherever used (H1, I3.147; `CandidateCone`, I3.43; `hadm` (a), I3.130)
- statement (CompositeDimension.lean:160–161): "/-- The product state of two copies. -/ def prodState (x y : Fin d → ℝ)
  : W d := fun μ ν => hom x μ * hom y ν"
- provenance: DIM-1 §A · depends_on: `hom` (CompositeDimension.lean:100) · yields: I3.3–I3.9, H1
- bridge: n/a · bearing: direct constraint on `K` through H1 · flag: —

### I3.3 `maxCone`
- kind: definition-as-hypothesis · level: P · status: proved [K] (definition); it encodes the full affine effect set of
  each copy (DIM-1 "the full affine effect set enters K1 there", K1-BRIDGE-1 preregistration; replaced by an available
  family in I3.49, I3.51)
- statement (CompositeDimension.lean:185–187): "/-- The maximal cone of two copies of `Ω`: nonnegative on every product
  of effects on `Ω`. -/ def maxCone (Ω : Set (Fin d → ℝ)) : Set (W d) := {ω | ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f
  → 0 ≤ prodEffVal e f ω}"
- provenance: DIM-1 §A · depends_on: `IsEffectOn` (I3.58), `prodEffVal` (CompositeDimension.lean:182)
- yields: `NativeGate.posFwd/posInv`, `jointStates`, `CandidateCone` (upper bound `K ⊆ maxCone`), `hadm` (b)
- bridge: n/a · bearing: direct constraint on `K` (upper bound in every admissible family) · flag: —

### I3.4 `jointStates`
- kind: definition-as-hypothesis · level: P · status: proved [K] (definition)
- statement (CompositeDimension.lean:189–191): "/-- The joint states: the normalized vectors of the maximal cone. -/
  def jointStates (Ω : Set (Fin d → ℝ)) : Set (W d) := {ω | ω ∈ maxCone Ω ∧ ω 0 0 = 1}"
- provenance: DIM-1 §A · depends_on: I3.3 · yields: `Entangling` (I3.10)
- bridge: n/a · bearing: direct (the entangling clause is read on it) · flag: —

### I3.5 `IsProduct`
- kind: definition-as-hypothesis · level: P · status: proved [K] (definition)
- statement (CompositeDimension.lean:193–195): "/-- A joint vector is a product state of `Ω`. -/ def IsProduct (Ω : Set
  (Fin d → ℝ)) (ω : W d) : Prop := ∃ x ∈ Ω, ∃ y ∈ Ω, ω = prodState x y"
- provenance: DIM-1 §A · depends_on: I3.2 · yields: `Entangling`, `EntanglingOf`, `dim1_core` (`cnot1` control)
- bridge: n/a · bearing: direct (part of the entangling clause) · flag: —

### I3.6 `actT`
- kind: definition-as-hypothesis (carrier map) · level: P · status: proved [K] (definition)
- statement (CompositeDimension.lean:197–198): "/-- `N` acting on the target index. -/ def actT (N : (Fin d → ℝ) →ₗ[ℝ]
  (Fin d → ℝ)) (ω : W d) : W d := fun μ => homMap N (ω μ)"
- provenance: DIM-1 §A ("the two actions of `N`")
- depends_on: `homMap` (CompositeDimension.lean:112) · yields: `NativeGate.relT/relC`, `GateRel`, `CtrlGate`,
  `NativeGateOf`, `no_candidateCone_cnot_reflY`, [D] `NClass`, `IE1`, `IE1Drive`
- bridge: this is the only kernel map from a one-copy linear map to the pair carrier. Its arguments in kernel
  statements at L: a variable `N` (in identities valid for every linear map, I3.185, or as the NOT of a hypothesis),
  `nflip`, `neg1`, `nC5`, `n5`, `reflY`. On product states the idle extension of any one-copy map is a product
  (`actT_prodState`, I3.185); on non-product vectors no statement at L concerns a flow member, `J`/`cyc3`, or a rotation of
  order > 2; idle-extended local rotations acting on a pair cone appear only in the [D] predicates `IE1`
  (FourCopyCore.lean:156) and `IE1Drive` (FourCopyPackage.lean:279)
- bearing: direct constraint on `K` or on (b_min): (b_min) in every stage-5 form is a statement "`actC g` or `actT g`
  preserves `K`" for one-token `g`; the map exists at L, the invariance statement for `g` ≠ NOT/`reflY` does not
- flag: the invariance of `K` under `actT g` for a rotation `g` is (b) / IE1-type: do not assume

### I3.7 `actC`
- kind: definition-as-hypothesis (carrier map) · level: P · status: proved [K] (definition)
- statement (CompositeDimension.lean:200–202): "/-- `N` acting on the control index. -/ def actC (N : (Fin d → ℝ) →ₗ[ℝ]
  (Fin d → ℝ)) (ω : W d) : W d := fun μ ν => homMap N (fun κ => ω κ ν) μ"
- provenance: DIM-1 §A · depends_on: `homMap` · yields: `NativeGate.relC`, `GateRel.relC`, `CtrlGate.relC`,
  `NativeGateOf.relC`, `not_even_of_relC`, `actC_tens`, `toOp_actC` (I3.185), [D] `NClass`, `IE1`, `IE1Drive`
- bridge: as I3.6 (the control-index map; its kernel arguments at L: a variable `N`, `nflip`, `neg1`, `nC5`, `n5`)
- bearing: direct constraint on `K` or on (b_min) (as I3.6, control token)
- flag: the invariance of `K` under `actC g` for a rotation `g` is (b) / IE1-type: do not assume

### I3.8 `IsNot`
- kind: hypothesis-structure · level: O · status: assumed (hypothesis of every selector: `dim_of_nativeGate`,
  `three_of_nativeGate`, `dim_of_nativeGateOf`, `dim_of_ctrlGate`, …; ROADMAP.md:995 "`IsNot` … all unsourced");
  instances proved [K]: `isNot_nflip` (CompositeDimension.lean:838), `isNot_neg1`, `isNot_n5`, `isNot_nK`
- statement (CompositeDimension.lean:209–215): "/-- The NOT of one copy: a linear involution preserving the body and
  inverting the corner axis. -/ structure IsNot (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d →
  ℝ)) : Prop where unit : ∑ j, z j ^ 2 = 1 · invol : ∀ x, N (N x) = x · preserves : ∀ x ∈ Ω, N x ∈ Ω · flips : N z = -z"
- provenance: DIM-1 §B (frozen hypotheses)
- depends_on: — · yields: I3.12–I3.20, §B, §C selectors; at `d = 3` with `GateRel`, `N` is a π-rotation (I3.24)
- bridge: O→P only through the hypotheses `NativeGate.relT/relC` (I3.9), which state how `actT N`, `actC N` interact
  with the gate; no theorem states that `K` is invariant under `actT N` or `actC N`
- bearing: constrains the single-token structure the pair inherits (the common NOT of both copies; K∞-Copy, I3.173)
- flag: —

### I3.9 `NativeGate`
- kind: hypothesis-structure · level: P · status: assumed (hypothesis of `dim_of_nativeGate`, `three_of_nativeGate`,
  `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`, `blockData_of_nativeGate`; ROADMAP.md:984–986 K1
  CONDITIONAL); instance proved [K]: `nativeGate_cnot` (I3.13)
- statement (CompositeDimension.lean:217–225): "/-- The native-gate hypotheses on two identical copies of `Ω`, with one
  `N` in both relations. -/ structure NativeGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d →
  ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where frame : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState
  (corner z a) (corner z (a + b)) · posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω · posInv : ∀ x ∈ Ω, ∀ y ∈
  Ω, G.symm (prodState x y) ∈ maxCone Ω · relT : ∀ ω, actT N (G (actT N ω)) = G ω · relC : ∀ ω, actC N (G (actC N ω))
  = actT N (G ω)"
- provenance: DIM-1 §B; fields read separately by PARITY-NOT-1 (`GateRel` = relT ∧ relC), RELC-SELECT-1 (`CtrlGate` =
  without relT), ODD-CHAR-1 (frame + `GateRel`)
- depends_on: I3.2, I3.3, I3.6, I3.7, `corner` · yields: I3.12–I3.19; `ctrlGate_of_nativeGate` (I3.32),
  `gateRel_of_nativeGate` (ParityNot.lean:46)
- bridge: n/a (level P). Note: positivity is on product inputs only (`posFwd/posInv`); it is not `hgate` (`cnot K ⊆ K`)
  for a pair cone `K` (H2, I3.148), which no kernel statement at L asserts of any cone
- bearing: direct constraint on the gate; constrains `K` only through H2 (PT-record) · flag: —

### I3.10 `Entangling`
- kind: hypothesis-structure (def … : Prop) · level: P · status: assumed (hypothesis of `three_of_nativeGate` alone,
  DIM-1); instance proved [K]: `entangling_cnot` (I3.14); its use is weakened to `2 ≤ d` (I3.45)
- statement (CompositeDimension.lean:227–231): "/-- The entangling clause: some pure product input has an image that is
  an extreme joint state and is not a product state. -/ def Entangling (Ω : Set (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) :
  Prop := ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ, G (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧ ¬
  IsProduct Ω (G (prodState x y))"
- provenance: DIM-1 §B · depends_on: I3.4, I3.5 · yields: I3.17, I3.19, `two_le_of_entangling` (I3.46)
- bridge: n/a · bearing: direct (on the gate's images in `maxCone`) · flag: —

### I3.11 `cnot`, `sgn`, `pc`, `pt`, `z3`, `nflip`, `xplus`, `phiW` (the `d = 3` witness data)
- kind: definition-as-hypothesis (witness data; no hypothesis role of its own) · level: P (`cnot`, `phiW`), O (`z3`, `nflip`,
  `xplus`) · status: proved [K] (definitions)
- statement: "def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1" (:741); `pc`, `pt`
  (:744, :751, explicit tables); "def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)" (:758);
  "/-- The `d = 3` gate as a linear equivalence of the joint carrier. -/ def cnot : W 3 ≃ₗ[ℝ] W 3 where" (:775, inverse
  `cnotFun`); "def z3 : Fin 3 → ℝ := ![0, 0, 1]" (:793); "/-- The common NOT of the `d = 3` witness: the reflection
  fixing the first coordinate and inverting the other two. -/ def nflip : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where toFun x :=
  fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i" (:795–798); "def xplus : Fin 3 → ℝ := ![1, 0, 0]" (:1213); "/-- The
  entangled image: the diagonal joint vector with entries `1, 1, −1, 1`. -/ def phiW : W 3 := fun μ ν => if μ = ν then
  (if μ = 2 then -1 else 1) else 0" (:1219–1220)
- provenance: DIM-1 §K, §N · depends_on: — · yields: I3.12–I3.14; every PT stage's `cnot` (H2) and `phiW`
- bridge: n/a · bearing: direct (the native gate `cnot` of H2) · flag: —

### I3.12 `isNot_nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`
- kind: theorem · level: P (O for `isNot_nflip`) · status: proved [K] (DIM-1 ledger row "`d = 3` witness": proved)
- statement: "theorem isNot_nflip : IsNot (eball 3) z3 nflip where" (:838); "theorem cnot_frame (a b : Fin 2) : cnot
  (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b))" (:848–849); "theorem
  cnot_relT (ω : W 3) : actT nflip (cnot (actT nflip ω)) = cnot ω" (:854); "theorem cnot_relC (ω : W 3) : actC nflip
  (cnot (actC nflip ω)) = actT nflip (cnot ω)" (:860)
- provenance: DIM-1 §K · depends_on: — (exact evaluation) · yields: I3.13
- bridge: n/a · bearing: direct (the NOT's pair action enters only through these two relations) · flag: —

### I3.13 `nativeGate_cnot`
- kind: theorem · level: P · status: proved [K]
- statement (CompositeDimension.lean:1159–1160): "/-- The `d = 3` gate satisfies every native-gate hypothesis. -/
  theorem nativeGate_cnot : NativeGate (eball 3) z3 nflip cnot where"
- provenance: DIM-1 §M (two-sided positivity on every product state by `cnot_core`, :1067; `cnot_prodState_mem_maxCone`,
  :1152) · depends_on: I3.12, `cnot_prodEffVal_nonneg` (:1140) · yields: I3.19; KT4-PREM-1 source map row `hcls`
- bridge: n/a · bearing: direct (the certified native gate on product inputs) · flag: —

### I3.14 `entangling_cnot`
- kind: theorem · level: P · status: proved [K]
- statement (CompositeDimension.lean:1378–1380): "/-- The `d = 3` gate is entangling: the pure product input `(xplus,
  z3)` has an extreme joint image that is not a product state. -/ theorem entangling_cnot : Entangling (eball 3) cnot"
- provenance: DIM-1 §N (`cnot_prodState_xplus_z3 : cnot (prodState xplus z3) = phiW`, :1222)
- depends_on: `phiW_mem_jointStates`, `phiW_not_product`, `lor_ray`, `phiW_eq_of_segment` · yields: I3.19
- bridge: n/a · bearing: direct (`phiW` is an extreme ray of `maxCone (eball 3)`'s slice) · flag: —

### I3.15 parity: `finrank_plus_eq_finrank_minus`, `not_even_of_nativeGate`
- kind: theorem · level: P · status: proved [K]
- statement: "/-- **Parity (S5) from the frozen hypotheses.** The `+1` and `−1` eigenspaces of the homogenized common NOT
  on the control space have the same dimension. -/ theorem finrank_plus_eq_finrank_minus {z : Fin d → ℝ} {N : (Fin d →
  ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
  Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)" (:680–684); "/-- No even dimension carries a native
  gate. -/ theorem not_even_of_nativeGate … (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : ¬ Even d"
  (:692–695)
- provenance: DIM-1 §I–§J · depends_on: I3.8, I3.9; `NativeGateBall.parity` (I3.125)
- yields: I3.18; reread from relations alone by I3.22 and I3.30 · bridge: n/a · bearing: direct (dimension) · flag: —

### I3.16 `blockData_of_nativeGate` (with `BlockData`)
- kind: theorem (with its theorem-internal auxiliary `BlockData`, CompositeDimension.lean:712) · level: P · status:
  proved [K]
- statement (CompositeDimension.lean:2700–2705): "/-- **The block reduction (S1, S2, S4).** Two identical copies of the
  Euclidean ball of dimension at least two with a native gate carry the block data of the `+1` eigenspace's tangent
  dimension. -/ theorem blockData_of_nativeGate … (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N
  G) : BlockData (tangentPlus N)"; `BlockData` docstring (:707–711): "… For `2 ≤ d` the data is derived from the frozen
  hypotheses in §Q (`blockData_of_nativeGate`); it is the hypothesis of `NativeGateBall.p_le_one`."
- provenance: DIM-1 ("is no premise of any selector") · depends_on: I3.8, I3.9 · yields: I3.18 via `p_le_one`
- bridge: n/a · bearing: direct · flag: —

### I3.17 `not_entangling_one`
- kind: theorem · level: P · status: proved [K]
- statement (CompositeDimension.lean:1434–1438): "/-- No gate of two intervals is entangling: the frame carries every
  pure product input to a product state. -/ theorem not_entangling_one {z : Fin 1 → ℝ} {N : (Fin 1 → ℝ) →ₗ[ℝ] (Fin 1 →
  ℝ)} {G : W 1 ≃ₗ[ℝ] W 1} (hN : IsNot (eball 1) z N) (hG : NativeGate (eball 1) z N G) : ¬ Entangling (eball 1) G"
- provenance: DIM-1 §O · depends_on: I3.8, I3.9 · yields: I3.19 · bridge: n/a · bearing: direct · flag: —

### I3.18 `dim_of_nativeGate` (the selector)
- kind: theorem · level: P · status: proved [K]; its premises are unsourced (ROADMAP.md:984–1000, K1 CONDITIONAL)
- statement (CompositeDimension.lean:2721–2725): "/-- **The selector.** Two identical copies of the Euclidean ball with a
  native gate have dimension one or three. -/ theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d →
  ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d = 1 ∨ d = 3"
- provenance: DIM-1 outcome `DIM-1-SELECTOR-PROVED` · depends_on: I3.8, I3.9 (and the carrier I3.1)
- yields: I3.19, I3.37, I3.45, K1 (I3.164) · bridge: n/a · bearing: constrains the single-token structure the pair
  inherits (fixes the ball dimension `d` of each token) · flag: —

### I3.19 `three_of_nativeGate`
- kind: theorem · level: P · status: proved [K]; premises unsourced (ROADMAP.md:984–1000)
- statement (CompositeDimension.lean:2746–2750): "/-- **The selector under the entangling clause.** Two identical copies
  of the Euclidean ball with an entangling native gate have dimension three. -/ theorem three_of_nativeGate {z : Fin d →
  ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N
  G) (hE : Entangling (eball d) G) : d = 3"
- provenance: DIM-1 · depends_on: I3.8, I3.9, I3.10 · yields: I3.21, K1 (I3.164)
- bridge: n/a · bearing: constrains the single-token structure the pair inherits (`d = 3`) · flag: —

### I3.20 DIM-1 controls: `nativeGate_cnot1`, `not_entangling_cnot1`, `no_gate_four`
- kind: theorem · level: P · status: proved [K]
- statement: "theorem nativeGate_cnot1 : NativeGate (eball 1) z1 neg1 cnot1 where" (CompositeDimension.lean:2861);
  "theorem not_entangling_cnot1 : ¬ Entangling (eball 1) cnot1" (:2869); "/-- `eball 4` carries no native gate. -/
  theorem no_gate_four : ¬ ∃ (z : Fin 4 → ℝ) (N : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ)) (G : W 4 ≃ₗ[ℝ] W 4), IsNot (eball 4)
  z N ∧ NativeGate (eball 4) z N G" (:2887–2889)
- provenance: DIM-1 §P · depends_on: — · yields: I3.21; the `d = 1` countermodel of I3.41
- bridge: n/a · bearing: direct (load-bearing tests of the entangling clause) · flag: —

### I3.21 `dim1_core` (DIM-1 verdict)
- kind: theorem · level: P · status: proved [K]
- statement (CompositeDimension.lean:2895–2909, first lines): "/-- The kernel layer's verdict: the parity exclusion, the
  selector, the selector under the entangling clause, the `d = 3` witness, the classical controls and the `eball 4`
  exclusion. -/ theorem dim1_core : (∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W
  d), IsNot (eball d) z N → NativeGate (eball d) z N G → ¬ Even d) ∧ … ∧ (IsNot (eball 3) z3 nflip ∧ NativeGate (eball
  3) z3 nflip cnot ∧ Entangling (eball 3) cnot) ∧ …" (full text: `kdecls.out`)
- provenance: DIM-1 ledger row "verdict: proved" · depends_on: I3.13–I3.20 · yields: K1 (I3.164)
- bridge: n/a · bearing: constrains the single-token structure the pair inherits (`d`; as I3.18–I3.19) · flag: —

## §B — the gate hypotheses taken apart (PARITY-NOT-1, ODD-CHAR-1, RELC-SELECT-1)

### I3.22 `not_even_of_gateRel` (with `finrank_plus_eq_finrank_minus_rel`)
- kind: theorem · level: P · status: proved [K] (PARITY-NOT-1 `PARITY-FROM-RELATIONS-PROVED`)
- statement (ParityNot.lean:137–138): "theorem not_even_of_gateRel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
  {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d"
- provenance: PARITY-NOT-1 Q-REL · depends_on: I3.8, I3.23 · yields: I3.27
- bridge: n/a · bearing: direct (the two NOT relations alone exclude even `d`) · flag: —

### I3.23 `GateRel`
- kind: hypothesis-structure · level: P · status: assumed (hypothesis of I3.22, I3.24, I3.25, I3.27); instances proved
  [K]: `gateRel_cnot`, `gateRel_gJ3`, `gateRel_gJ5`, `gateRel_gRev`
- statement (ParityNot.lean:41–44): "/-- The target relation and the control relation of `NativeGate`, and nothing else.
  -/ structure GateRel (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where relT : ∀ ω, actT N (G (actT
  N ω)) = G ω · relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)"
- provenance: PARITY-NOT-1 · depends_on: I3.6, I3.7 · yields: I3.22, I3.24–I3.28, I3.33
- bridge: n/a · bearing: direct (relations between the NOT's pair action and the gate; no invariance of `K`) · flag: —

### I3.24 `piRotation_three` (with `tangentPlus_three`, `det_three`)
- kind: theorem · level: O (conclusion about the NOT) from P hypotheses · status: proved [K]
- statement (ParityNot.lean:161–163): "theorem piRotation_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G :
  W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) : ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑
  j, u j * x j) • u - x"
- provenance: PARITY-NOT-1 Q-NOT ("`N` is the rotation by `π` about `u` … `det N = 1`")
- depends_on: I3.8, I3.23 · yields: I3.25 (determinant −1 NOTs excluded)
- bridge: a P→O transfer: the pair relations fix the single-token NOT as a π-rotation · bearing: constrains the
  single-token structure the pair inherits · flag: —

### I3.25 `not_gateRel_refl3`, `not_gateRel_negId3`
- kind: theorem · level: P · status: proved [K]
- statement (ParityNot.lean:389): "theorem not_gateRel_refl3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel refl3 G" (and
  `not_gateRel_negId3`; both NOTs have determinant −1)
- provenance: PARITY-NOT-1 Q-NOT · depends_on: I3.24 · yields: — · bridge: n/a
- bearing: direct (orientation-reversing NOTs carry no gate) · flag: —

### I3.26 `not_posFwd_gJ3`, `not_posFwd_gJ5`
- kind: theorem · level: P · status: proved [K] (PARITY-NOT-1 `POSITIVITY-SEPARATION-PROVED`)
- statement (ParityNot.lean:547–548): "theorem not_posFwd_gJ3 : ¬ ∀ x ∈ eball 3, ∀ y ∈ eball 3, gJ3 (prodState x y) ∈
  maxCone (eball 3)"; (:704–705) the same for `gJ5` on `eball 5`
- provenance: PARITY-NOT-1 Q-SEP · depends_on: — (exact rational witness −1/10) · yields: —
- bridge: n/a · bearing: direct (frame + relations do not supply forward positivity) · flag: —

### I3.27 `exists_frame_gateRel_iff_odd`
- kind: theorem · level: P · status: proved [K] (ODD-CHAR-1 `ODD-CHARACTERIZATION-PROVED`; directions by
  `not_even_of_gateRel` and the explicit families `cnot1`, `gRev k`)
- statement (OddChar.lean:184–189): "theorem exists_frame_gateRel_iff_odd (d : ℕ) : (∃ (z : Fin d → ℝ) (N : (Fin d → ℝ)
  →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N ∧ (∀ a b : Fin 2, G (prodState (corner z a) (corner z b))
  = prodState (corner z a) (corner z (a + b))) ∧ GateRel N G) ↔ Odd d"
- provenance: ODD-CHAR-1 · depends_on: I3.8, I3.22, I3.23 · yields: I3.28
- bridge: n/a · bearing: direct (positivity is what excludes odd `d ≥ 5`) · flag: —

### I3.28 `not_posFwd_gRev`
- kind: theorem · level: P · status: proved [K]
- statement (OddChar.lean:287–289): "theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) : ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈
  eball (2 * k + 1), gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1))"
- provenance: ODD-CHAR-1 Q-POS ("Whether either clause is needed without the other is open" for this family)
- depends_on: — · yields: — · bridge: n/a · bearing: direct · flag: —

### I3.29 `CtrlGate`
- kind: hypothesis-structure · level: P · status: assumed (hypothesis of I3.31); `ctrlGate_of_nativeGate` (I3.32)
- statement (RelcSelectBlock.lean:44–51): "/-- `NativeGate` without the target relation `relT`. -/ structure CtrlGate (Ω :
  Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where frame : … ·
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω · posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone
  Ω · relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)"
- provenance: RELC-SELECT-1; KT4-PREM-1 source map row `hcls` ("`CtrlGate`, `dim_of_ctrlGate`, `three_of_ctrlGate`")
- depends_on: I3.3, I3.6, I3.7 · yields: I3.31 · bridge: n/a · bearing: direct (gate) · flag: —

### I3.30 `not_even_of_relC`
- kind: theorem · level: P · status: proved [K] (RELC-SELECT-1 `RELC-PARITY-PROVED`)
- statement (RelcSelectParity.lean:354–356): "theorem not_even_of_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d →
  ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d"
- provenance: RELC-SELECT-1 Q-PAR · depends_on: I3.8, relC · yields: I3.31 · bridge: n/a · bearing: direct · flag: —

### I3.31 `dim_of_ctrlGate`, `three_of_ctrlGate`
- kind: theorem · level: P · status: proved [K] (`CTRL-SELECTOR-PROVED`)
- statement (RelcSelectBlock.lean:739–741): "theorem dim_of_ctrlGate … (hN : IsNot (eball d) z N) (hG : CtrlGate (eball
  d) z N G) : d = 1 ∨ d = 3"; (:753–755) "theorem three_of_ctrlGate … (hG : CtrlGate (eball d) z N G) (hE : Entangling
  (eball d) G) : d = 3"
- provenance: RELC-SELECT-1 Q-SEL · depends_on: I3.8, I3.29, I3.10 · yields: KT4-PREM-1 row `hcls` (supplied fact)
- bridge: n/a · bearing: constrains the single-token structure the pair inherits (`d`) · flag: —

### I3.32 `ctrlGate_of_nativeGate`
- kind: lemma-folded (edge `NativeGate → CtrlGate`) · level: P · status: proved [K]
- statement (RelcSelectBlock.lean:53–55): "theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin
  d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) : CtrlGate Ω z N G"
- provenance: RELC-SELECT-1 §A · depends_on: I3.9 · yields: I3.31 · bridge: n/a · bearing: direct (an edge between two gate hypotheses) · flag: —

### I3.33 `gSq_sep`, `gSqInv_sep`
- kind: theorem · level: P · status: proved [K] (`POSITIVITY-SEPARATION-PROVED`)
- statement (RelcSelectSqueeze.lean:465–470): "theorem gSq_sep : IsNot (eball 5) z5 n5 ∧ (∀ a b : Fin 2, gSq (prodState
  (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧ GateRel n5 gSq ∧ (∀ x ∈ eball 5, ∀ y ∈
  eball 5, gSq (prodState x y) ∈ maxCone (eball 5)) ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈
  maxCone (eball 5))"; `gSqInv_sep` (:476) the mirror statement for `gSq.symm`
- provenance: RELC-SELECT-1 Q-POS · depends_on: — · yields: — · bridge: n/a
- bearing: direct (each positivity clause is load-bearing at `d = 5`) · flag: —

### I3.34 `relT_not_dimension_selecting`
- kind: theorem · level: P · status: proved [K] (`RELT-NOT-DIMENSION-SELECTING-PROVED`)
- statement (RelcSelectC5.lean:393–400): "theorem relT_not_dimension_selecting : ¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d →
  ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N → (∀ a b : Fin 2, G (prodState (corner z a) (corner z
  b)) = prodState (corner z a) (corner z (a + b))) → (∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball
  d)) → (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) → (∀ ω, actT N (G (actT N ω)) = G
  ω) → d = 1 ∨ d = 3"
- provenance: RELC-SELECT-1 Q-REL (`nC5`, `gC5` "not proposed as a NOT or a gate of a physical theory")
- depends_on: — · yields: — · bridge: n/a · bearing: direct (the control relation is load-bearing) · flag: —

## §C — K1 relative to available tests, sharp tests, the K2 guard (K1-BRIDGE-1, K1-SHARP-TESTS-1, K2-GUARD-1)

### I3.35 `NativeGateOf`
- kind: hypothesis-structure · level: P · status: assumed (hypothesis of I3.37, I3.38, I3.47; ROADMAP.md:995–996 "the
  relative native-gate and entangling hypotheses are, all unsourced"); instance proved [K]: `nativeGateOf_cnot1`
- statement (K1Bridge.lean:46–56): "/-- DIM-1's native-gate hypotheses relative to a family `avail` of available test
  functionals: the frame, the two NOT relations and, in place of `maxCone Ω`, two-sided positivity on the cone of the
  products of the family. -/ structure NativeGateOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin
  d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where frame : … · posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T
  (prodState x y) ∈ maxConeOf avail · posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail · relT : ∀ ω,
  actT N (T (actT N ω)) = T ω · relC : ∀ ω, actC N (T (actC N ω)) = actT N (T ω)"
- provenance: K1-BRIDGE-1 `K1-EFFECT-AVAILABILITY-DISCHARGED` · depends_on: I3.49, I3.6, I3.7
- yields: I3.37, I3.38, I3.41, I3.47 · bridge: n/a · bearing: direct (gate, on the available-test cone) · flag: —

### I3.36 `EntanglingOf`
- kind: hypothesis-structure (def … : Prop) · level: P · status: assumed (hypothesis of I3.38)
- statement (K1Bridge.lean:62–66): "/-- DIM-1's entangling clause relative to the family: some pure product input has an
  image that is an extreme joint state of the family's cone and is not a product state. -/ def EntanglingOf (Ω : Set
  (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop := ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈
  Ω.extremePoints ℝ, T (prodState x y) ∈ (jointStatesOf avail).extremePoints ℝ ∧ ¬ IsProduct Ω (T (prodState x y))"
- provenance: K1-BRIDGE-1 · depends_on: I3.49, I3.5 · yields: I3.38 · bridge: n/a · bearing: direct · flag: —

### I3.37 `dim_of_nativeGateOf`
- kind: theorem · level: P (hypotheses at O and P) · status: proved [K]; premises unsourced (ROADMAP.md:995–996)
- statement (K1Bridge.lean:128–132): "theorem dim_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail) (hG :
  PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 :
  SeedOrbitAvailable G r avail) {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot
  (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3"
- provenance: K1-BRIDGE-1 · depends_on: I3.48, I3.74, I3.73, I3.76, I3.75, I3.8, I3.35; through I3.51 and I3.18
- yields: K1 (I3.164) · bridge: this theorem is itself the O→P composition: single-ball hypotheses (K∞-Trans, K∞-Seed,
  K∞-V4, body preservation) reach the pair statement only through `maxConeOf_avail_eq` (I3.51)
- bearing: constrains the single-token structure the pair inherits (`d`) · flag: —

### I3.38 `three_of_nativeGateOf`
- kind: theorem · level: P · status: proved [K]; premises unsourced
- statement (K1Bridge.lean:138–143): as I3.37 with "(hEnt : EntanglingOf (eball d) avail T) : d = 3"
- provenance: K1-BRIDGE-1 · depends_on: as I3.37 and I3.36 · yields: K1 (I3.164) · bridge: as I3.37
- bearing: constrains the single-token structure the pair inherits (`d`; as I3.37) · flag: —

### I3.39 `HasTwoSharpTests`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (the reading of the selector premise `2 ≤ d`;
  K1-SHARP-TESTS-1: "This round does not show that OI provides two sharp binary tests")
- statement (SharpTests.lean:39–43): "/-- Two sharp binary tests of `Ω`, separated on `Ω` from each other and from each
  other's complement. -/ def HasTwoSharpTests (Ω : Set V) : Prop := ∃ e f : V →ᵃ[ℝ] ℝ, SharpSeed Ω e ∧ SharpSeed Ω f ∧
  (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)"
- provenance: K1-SHARP-TESTS-1 · depends_on: I3.73 · yields: I3.40 · bridge: to the pair selectors only through the
  equivalence I3.40 with `2 ≤ d` and the K2-GUARD-1 selectors I3.45, I3.47 · bearing: constrains the single-token
  structure the pair inherits · flag: —

### I3.40 `hasTwoSharpTests_iff`
- kind: theorem · level: O · status: proved [K] (`K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED`)
- statement (SharpTests.lean:155): "theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d"
- provenance: K1-SHARP-TESTS-1 Q-CLASSIFIED (each direction by its own argument) · depends_on: I3.39
- yields: with I3.45/I3.47, a reading of `2 ≤ d` · bridge: as I3.39 · bearing: constrains the single-token structure the pair inherits (as I3.39) · flag: —

### I3.41 `two_le_not_implied`
- kind: theorem · level: P · status: proved [K] (`K1-TWO-LE-NOT-IMPLIED`)
- statement (SharpTests.lean:197–203): "theorem two_le_not_implied : ¬ (∀ (d : ℕ) (avail …) (G …) (r …) (z …) (N …) (T :
  W d ≃ₗ[ℝ] W d), EffectsOn (eball d) avail → PreservesBody (eball d) G → SharpSeed (eball d) r → BoundaryTransitive
  (eball d) G → SeedOrbitAvailable G r avail → IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → 2 ≤ d)"
- provenance: K1-SHARP-TESTS-1 Q-NOT-IMPLIED (`d = 1` countermodel) · depends_on: — · yields: —
- bridge: n/a · bearing: direct (`2 ≤ d` is an independent premise of the selector) · flag: —

### I3.42 `prodState_mem_maxCone`
- kind: theorem · level: P (from O data) · status: proved [K]
- statement (K2Guard.lean:165–166): "theorem prodState_mem_maxCone {Ω : Set (Fin d → ℝ)} {x y : Fin d → ℝ} (hx : x ∈ Ω)
  (hy : y ∈ Ω) : prodState x y ∈ maxCone Ω"
- provenance: K2-GUARD-1; KT4-PREM-1 source map row `hadm` ("what `D` supplies") · depends_on: I3.2, I3.3
- yields: `productSet`, `cnotOrbit` candidate cones (K2Guard.lean:179, :182); H1 is consistent with `K ⊆ maxCone`
- bridge: an O→P statement: effects of one copy make products nonnegative on every product test · bearing: direct
  (products lie in the upper bound of every admissible `K`; it does not put products in a given `K`) · flag: —

### I3.43 `CandidateCone`
- kind: hypothesis-structure (def … : Prop) · level: P · status: assumed (hypothesis of I3.44; it is `hadm` (a)–(b),
  i.e. [D] `PairAdm` minus convexity, I3.130)
- statement (K2Guard.lean:93–96): "/-- The candidate-cone family of two copies of `eball 3`: the sets of joint vectors
  containing every product state of the ball and contained in DIM-1's maximal cone. -/ def CandidateCone (K : Set (W 3))
  : Prop := (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)"
- provenance: K2-GUARD-1 Q-ORIENTATION · depends_on: I3.2, I3.3 · yields: I3.44; [D] `PairAdm`
- bridge: n/a · bearing: direct constraint on `K` (H1 plus the `maxCone` bound) · flag: —

### I3.44 `no_candidateCone_cnot_reflY`
- kind: theorem · level: P · status: proved [K] (`K2-ORIENTATION-OBSTRUCTION-PROVED`)
- statement (K2Guard.lean:143–144): "theorem no_candidateCone_cnot_reflY {K : Set (W 3)} (hK : CandidateCone K) (hC : ∀
  ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False"; `reflY` (K2Guard.lean:46) is `diag(1, −1, 1)` on the
  second copy
- provenance: K2-GUARD-1 ("a composite route that admits `cnot` and chooses its cone from this candidate family cannot
  also admit `reflY` on one copy as a reversible symmetry"; control: with `nflip` the chain value is `0`)
- depends_on: I3.43, `chain_eq`, `chain_value` (K2Guard.lean:116, :134) · yields: KT4-PREM-1 Q2 ("for `reflY` it fails
  on every `cnot`-invariant candidate cone"); the twin is not `cnot`-invariant (`cnot idW = chainW`, :110)
- bridge: n/a · bearing: direct constraint on `K` and on local actions on the pair: the only kernel theorem at L in which
  `K` is required invariant under a one-copy map other than the gate, and the answer is a no-go for that map
- flag: — (it concerns a determinant −1 reflection, not a rotation)

### I3.45 `three_of_nativeGate_of_two_le`
- kind: theorem · level: P · status: proved [K] (`K1-ENTANGLING-WEAKENED`)
- statement (K2Guard.lean:234–236): "theorem three_of_nativeGate_of_two_le {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d
  → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d = 3"
- provenance: K2-GUARD-1 Q-ENTANGLING · depends_on: I3.8, I3.9, I3.18 · yields: K1 path "`NativeGateOf` with `2 ≤ d`
  gives `d = 3`; where `2 ≤ d` comes from remains open" · bridge: n/a · bearing: constrains the single-token structure the pair inherits (`d`; as I3.18) · flag: —

### I3.46 `two_le_of_entangling`
- kind: lemma-folded (edge `Entangling → 2 ≤ d` under I3.8, I3.9) · level: P · status: proved [K]; "no converse is
  stated" (K2-GUARD-1)
- statement (K2Guard.lean:240–242): "theorem two_le_of_entangling … (hN : IsNot (eball d) z N) (hG : NativeGate (eball
  d) z N G) (hE : Entangling (eball d) G) : 2 ≤ d" · provenance: K2-GUARD-1 · depends_on: I3.10, I3.17
- yields: I3.45 · bridge: n/a · bearing: direct (an edge between gate hypotheses and `2 ≤ d`) · flag: —

### I3.47 `three_of_nativeGateOf_of_two_le`
- kind: theorem · level: P · status: proved [K]
- statement (K2Guard.lean:253–257): "theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d) (hE : EffectsOn (eball d)
  avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 :
  SeedOrbitAvailable G r avail) {z …} {N …} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d)
  avail z N T) : d = 3"
- provenance: K2-GUARD-1 · depends_on: as I3.37 plus `2 ≤ d` · yields: K1 (I3.164) · bridge: through I3.51
- bearing: constrains the single-token structure the pair inherits (`d`; as I3.37) · flag: —

## §D — the effect set and the product-test cone (EFF-1, KTRANS-DENSE-1)

### I3.48 `EffectsOn`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed ("effect soundness", hypothesis of I3.37,
  I3.38, I3.47, I3.51; ROADMAP.md:995 "effect soundness … unsourced")
- statement (EffectSpace.lean:566–568): "/-- Every member of the family is an effect on `Ω`. -/ def EffectsOn (Ω : Set
  (Fin d → ℝ)) (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := ∀ e ∈ A, IsEffectOn Ω e"
- provenance: EFF-1 · depends_on: I3.58 · yields: I3.51 · bridge: through I3.51 to `maxCone`
- bearing: constrains the composite only through `maxConeOf_avail_eq` (I3.51) · flag: —

### I3.49 `maxConeOf`
- kind: definition-as-hypothesis · level: P · status: proved [K] (definition)
- statement (EffectSpace.lean:410–412): "/-- The cone of joint vectors nonnegative on every product of two members of `A`.
  -/ def maxConeOf (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set (W d) := {ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}"
- provenance: EFF-1 §D · depends_on: `prodEffVal` · yields: I3.35, I3.36, I3.51 · bridge: n/a
- bearing: direct (the product-test cone of the available tests) · flag: —

### I3.50 `MixingClosed`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open — EFF-1: "The unit and `MixingClosed`
  are an unsourced OPEN premise, and DIM-1's effect premise is not discharged" (K1-BRIDGE-1 later removes the full
  effect set from K1's premises: I3.37)
- statement (EffectSpace.lean:590–592): "/-- The mixing closure, a named premise: closure under sub-convex binary
  combinations. -/ def MixingClosed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := ∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β
  → α + β ≤ 1 → α • e + β • f ∈ A"
- provenance: EFF-1 Q-SET · depends_on: — · yields: I3.52 · bridge: none at L to the pair (Q-SET is single-ball)
- bearing: constrains the single-token structure (which effects are available) · flag: —

### I3.51 `maxConeOf_avail_eq` (with `sharpFamily_subset_avail`, `maxConeOf_sharpFamily`)
- kind: theorem · level: P (hypotheses at O) · status: proved [K] (EFF-1 `CONE-DERIVED`, "DERIVED is relative to those
  four hypotheses, which the round does not source; it is not a derivation from OI")
- statement (EffectSpace.lean:570–575): "/-- The available family determines DIM-1's maximal cone once every available
  functional is an effect. -/ theorem maxConeOf_avail_eq (hd : 0 < d) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed
  (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d)
  avail) : maxConeOf avail = maxCone (eball d)"; "theorem sharpFamily_subset_avail (hG : PreservesBody (eball d) G) (hP1
  : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) : sharpFamily d ⊆
  avail" (:374–376)
- provenance: EFF-1 · depends_on: I3.74, I3.73, I3.76, I3.75, I3.48 · yields: I3.37, I3.38, I3.47
- bridge: **the O→P bridge theorem of the K programme at L**: it carries single-ball hypotheses (K∞-Trans, K∞-Seed,
  K∞-V4, body preservation, effect soundness) to the pair-level product-test cone `maxCone (eball d)`. It transfers
  effect availability, not operations: nothing in it acts on `W d` with a one-copy map
- bearing: constrains the composite only through this theorem (fixes the cone in the gate's positivity clauses; it does
  not constrain `K` beyond `K ⊆ maxCone`) · flag: —

### I3.52 `fullEffects_subset_avail`
- kind: theorem · level: O · status: proved [K] (EFF-1 `CONDITIONAL-FULL-EFFECTS`)
- statement (EffectSpace.lean:718–721): "theorem fullEffects_subset_avail (hd : 0 < d) (hG : PreservesBody (eball d) G)
  (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff
  d ∈ avail) (hM : MixingClosed avail) : fullEffects (eball d) ⊆ avail"
- provenance: EFF-1 Q-SET · depends_on: I3.74, I3.73, I3.76, I3.75, I3.50 · yields: — · bridge: none at L (single
  ball) · bearing: constrains the single-token structure · flag: —

### I3.53 `not_fullEffects_of_orbit`
- kind: theorem · level: O · status: proved [K]
- statement (EffectSpace.lean:762–767): "theorem not_fullEffects_of_orbit (hd : 0 < d) : PreservesBody (eball d) (fullAut
  d) ∧ SharpSeed (eball d) (sharpEff (axisVec hd)) ∧ BoundaryTransitive (eball d) (fullAut d) ∧ SeedOrbitAvailable
  (fullAut d) (sharpEff (axisVec hd)) (sharpUnitFamily d) ∧ unitEff d ∈ sharpUnitFamily d ∧ EffectsOn (eball d)
  (sharpUnitFamily d) ∧ ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d"
- provenance: EFF-1 Q-SET · depends_on: — · yields: — · bridge: n/a · bearing: constrains the single-token structure
  (the mixing closure is load-bearing for the full effect set) · flag: —

### I3.54 `DenseBoundaryOrbit`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (hypothesis of the dense variants; "Nothing here
  sources a dense boundary orbit or any other hypothesis", DenseOrbit.lean header)
- statement (DenseOrbit.lean:52–55): "/-- Every boundary state lies in the closure of the orbit of every boundary state.
  -/ def DenseBoundaryOrbit {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) :
  Prop := ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) '' G)"
- provenance: KTRANS-DENSE-1 · depends_on: I3.60 · yields: I3.56 · bridge: through `maxConeOf_avail_eq_of_dense` (I3.56)
- bearing: constrains the composite only through I3.56 · flag: —

### I3.55 `denseBoundaryOrbit_of_boundaryTransitive`
- kind: lemma-folded (edge K∞-Trans → dense orbit) · level: O · status: proved [K]; the converse fails
  (`not_boundaryTransitive_ratRefl`, KTRANS-DENSE-1 `KTRANS-DENSE-STRICTLY-WEAKER`)
- statement (DenseOrbit.lean:57–58): "theorem denseBoundaryOrbit_of_boundaryTransitive … (hT : BoundaryTransitive Ω G) :
  DenseBoundaryOrbit Ω G" · provenance: KTRANS-DENSE-1 · depends_on: I3.76 · yields: I3.56
- bridge: n/a · bearing: constrains the composite only through I3.56 (an edge K∞-Trans → dense orbit) · flag: —

### I3.56 `maxConeOf_avail_eq_of_dense` (with the dense ball and selector variants)
- kind: theorem · level: P (hypotheses at O) · status: proved [K] (`KTRANS-DENSE-CONE-PROVED`, `-BALL-PROVED`)
- statement (DenseOrbit.lean:243–246): "theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) (hG : PreservesBody (eball d) G)
  (hP1 : SharpSeed (eball d) r) (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail) (hE :
  EffectsOn (eball d) avail) : maxConeOf avail = maxCone (eball d)"; dense selectors `dim_of_nativeGateOf_dense`,
  `three_of_nativeGateOf_dense`, `three_of_nativeGateOf_of_two_le_dense`; ball `exists_affine_image_eq_eball_of_dense`
- provenance: KTRANS-DENSE-1 · depends_on: I3.54, I3.73–I3.75, I3.48 · yields: K1 path with K∞-Trans weakened
- bridge: O→P, as I3.51 with the weaker transitivity · bearing: constrains the composite only through this theorem
- flag: —

## §E — K∞: the field-neutral single-system premises (KINF-2, OG-1, TRB-1, IIP-1, CMP-1, OPACT-1, ORD-1)

### I3.57 `FiniteStage`
- kind: definition-as-hypothesis (data structure) · level: O · status: proved [K] (definition); instances at L only the
  controls (`badD`, `bitTower`, `midD`; KT4-PREM-1 Q2) — no instance built from an OI construction
- statement (KInfFoundations.lean:61–72): "/-- A finite observer stage: finitely many preparations `P`, finitely many
  effects `E`, a probability table `p e x ∈ [0, 1]`, and a unit effect certain on every preparation. -/ structure
  FiniteStage where P : Type · E : Type · [fP : Fintype P] · [fE : Fintype E] · p : E → P → ℝ · unit : E · nonneg : ∀ e
  x, 0 ≤ p e x · le_one : ∀ e x, p e x ≤ 1 · unit_eq : ∀ x, p unit x = 1"
- provenance: KINF-2 §A · depends_on: — · yields: I3.92 · bridge: none at L (no pair-level stage system; "no
  declaration builds a directed system from two systems", KT4-PREM-1 Q2) · bearing: constrains the single-token
  structure (the K∞ route upstream of the ball, ROADMAP.md:1084); no pair-level stage system at L · flag: —

### I3.58 `IsEffectOn`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (KInfFoundations.lean:115–117): "/-- An affine functional is an effect on `Ω` when it takes values in `[0,
  1]` on `Ω`. -/ def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop := ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1"
- provenance: KINF-2 · depends_on: — · yields: I3.3, I3.48, I3.73, `PreComposite.prodEff_effect`
- bridge: enters the pair through `maxCone` (I3.3) · bearing: constrains the composite only through `maxCone` (I3.3) · flag: —

### I3.59 `IsProperOn`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (KInfFoundations.lean:123–126): "/-- An effect is proper on `Ω` when some state gives it a value below one.
  The unit effect, and every effect identically one on `Ω`, is not proper. Properness is tested on `Ω`, not on `V`. -/
  def IsProperOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop := ∃ y ∈ Ω, e y < 1"
- provenance: KINF-2 (correction of KINF-1) · depends_on: — · yields: I3.61, I3.62 · bridge: none at L · bearing: none
  at L · flag: —

### I3.60 `IsBoundaryState`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (KInfFoundations.lean:128–131): "/-- A boundary state of `Ω`, read in `Ω` alone: some state `y` is such that
  no extension of the segment from `y` through `x` beyond `x` stays in `Ω`. -/ def IsBoundaryState (Ω : Set V) (x : V)
  : Prop := x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω"
- provenance: KINF-2 · depends_on: — · yields: I3.61, I3.76, I3.54 · bridge: through I3.76 → I3.51
- bearing: constrains the composite only through I3.51 · flag: —

### I3.61 `SupportingEffectComplete` (SEC)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (K∞-1 / SEC is "an open target", KInf1
  docstring; derived on `ball3` under OG-1's hypotheses, `supportingEffectComplete_ball3_of_orbit`)
- statement (KInfFoundations.lean:133–136): "/-- Supporting-effect completeness (SEC) relative to a family `avail` of
  available functionals: every boundary state of `Ω` is certain for some proper available effect. -/ def
  SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := ∀ x, IsBoundaryState Ω x → ∃ e ∈ avail,
  IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1"
- provenance: KINF-2 §B′ · depends_on: I3.58–I3.60 · yields: I3.71, I3.72 · bridge: none at L · bearing: none at L
  (single-system geometry; ROADMAP K∞-Geom, I3.174) · flag: —

### I3.62 `SingletonFaces` (SF)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open (K∞-Geom, ROADMAP.md:1031–1033; "The
  singleton-face principle, relative strict convexity (`RelStrictConvex`) and the ball they yield hold for the qubit and
  fail for complex quantum systems of level three or more", ROADMAP.md:1045–1047)
- statement (KInfFoundations.lean:138–140): "/-- Singleton faces (SF): every proper available effect is certain on at
  most one state. -/ def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := ∀ e ∈ avail, IsEffectOn Ω e →
  IsProperOn Ω e → (certainFace Ω e).Subsingleton"
- provenance: KINF-2 · depends_on: I3.58, I3.59 · yields: I3.72 (Lemma C) · bridge: none at L · bearing: none at L
- flag: —

### I3.63 `RelStrictConvex`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition); equivalent to SF given SEC (I3.72)
- statement (KInfFoundations.lean:142–146): "/-- Relative strict convexity: every point strictly between two distinct
  states is a state and is not a boundary state. -/ def RelStrictConvex (Ω : Set V) : Prop := ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y
  → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 → a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)"
- provenance: KINF-2 §D · depends_on: I3.60 · yields: I3.72 · bridge: none at L · bearing: none at L · flag: —

### I3.64 `PerfectlyDistinguishable`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (KInfFoundations.lean:152–157): "/-- A finite family of states is perfectly distinguishable by a family of
  effects when the effects are effects on `Ω`, sum to the unit on `Ω`, and each is certain on its own state. -/ def
  PerfectlyDistinguishable (Ω : Set V) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ) : Prop := (∀ i, x i ∈ Ω) ∧
  (∀ i, IsEffectOn Ω (e i)) ∧ (∀ y ∈ Ω, ∑ i, e i y = 1) ∧ (∀ i, e i (x i) = 1)"
- provenance: KINF-2 · depends_on: I3.58 · yields: I3.72 (Lemma D), `SharpReadout` (I3.119),
  `sharpSeed_of_perfectlyDistinguishable` · bridge: none at L · bearing: none at L · flag: —

### I3.65 `CentrallySymmetric`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition; hypothesis of Lemma D in I3.72)
- statement (KInfFoundations.lean:159–161): "/-- Central symmetry of `Ω` about `c`: the reflection `x ↦ c + (c − x)`
  preserves `Ω`. -/ def CentrallySymmetric (Ω : Set V) (c : V) : Prop := ∀ x ∈ Ω, c + (c - x) ∈ Ω"
- provenance: KINF-2 · depends_on: — · yields: I3.72 · bridge: none at L · bearing: none at L · flag: —

### I3.66 `ElementaryDrivability` (K∞-Drive)
- kind: hypothesis-structure (data structure with Prop fields) · level: O · status: assumed / open — ROADMAP.md:1017
  "**K∞-Drive** — field-neutral drivability, `ElementaryDrivability`", K∞ OPEN, "All are unsourced" (ROADMAP.md:1009);
  KINF-2 "named here as definitions, discharged by no OI construction"; instance proved [K] for the control `ball3`
  (I3.67)
- statement (KInfFoundations.lean:260–276): "/-- Elementary drivability of a body `Ω`, stated without a field: a
  continuous one-parameter group of affine automorphisms of `V` preserving `Ω`, on which a distinguished involution of `Ω`
  (the NOT) lies, together with an automorphism `J` of `Ω` whose conjugate of some flow member agrees on `Ω` with no flow
  member. -/ structure ElementaryDrivability (Ω : Set V) where flow : ℝ → V ≃ᵃ[ℝ] V · flow_zero : flow 0 =
  AffineEquiv.refl ℝ V · flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s) · flow_continuous : Continuous fun q
  : ℝ × V => flow q.1 q.2 · flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω · t₀ : ℝ · N_involutive : ∀ x ∈ Ω, flow t₀
  (flow t₀ x) = x · N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x · J : V ≃ᵃ[ℝ] V · J_preserves : ∀ x ∈ Ω, J x ∈ Ω ·
  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω · J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x"; its NOT
  (:278–280): "def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V := D.flow D.t₀"
- provenance: KINF-2 §C (corrected vocabulary; KINF-1 halted, ROADMAP.md:1071) · depends_on: —
- yields: I3.78 (`preservesBody_drive`), I3.83 (`boundaryTransitive_ball3Drive` for the control), I3.84, `KInf1` (I3.71,
  as antecedent); it does **not** yield `BoundaryTransitive` on a general body ("no theorem derives transitivity from
  `ElementaryDrivability` on a general body", ROADMAP.md:1020–1022; I3.81)
- bridge: **none at L.** What exists at L: (i) the carrier maps `actC N`, `actT N` (I3.6–I3.7); statements that
  constrain pair vectors under them concern only involutions — `N` the linear NOT of `IsNot` inside the relations
  `relT`/`relC` of `NativeGate`/`GateRel`/`CtrlGate`/`NativeGateOf`, the instances `nflip`, `neg1`, `nC5`, `n5`, and
  `reflY` — while the identities valid for every one-copy linear map (I3.185) send products to products and say nothing
  about non-product vectors; (ii) `ElementaryDrivability` is read only
  in `OrbitGeneration` and `OrbitNormalization`, single-body statements (`kimports.out`; grep); (iii) `eball_three :
  eball 3 = ball3` (TransitiveBody.lean:671) identifies the two balls as sets. What is not at L: any statement with
  `actC`/`actT` of a flow member, of `J`, or of `cyc3`; any theorem relating `D.N` (an affine equivalence `V ≃ᵃ[ℝ] V`)
  to an `IsNot` NOT (a linear map of `Fin d → ℝ`) or to `nflip`; any pair-level invariance under the drive. The only
  pair-level lift of the drive words anywhere is the design predicate `IE1Drive` (FourCopyPackage.lean:279, [D],
  I3.142), whose link to IE1 (`ie1Drive_of_ie1`) is a `sorry`. By the definitions (not a kernel theorem): `ball3Drive`'s
  NOT `rot3 π` fixes the third coordinate, so it does not invert `z3`; DIM-1's `nflip` fixes the first coordinate and
  inverts `z3`. The "native drive through the NOT, on the NOT axis" of stages 4–5 is a PT construction, not a kernel
  object at L
- bearing: none at L as a constraint on `K`; it is the single-token datum (flow and `J`) that the (b_DJ) form of
  (b_min) idle-extends (PROTOCOL-STAGE5.md:22–25) · flag: — (the object itself); its pair-level extension is (b)
  (do not assume)

### I3.67 `ball3Drive`, `ball3_drivable` (with `ball3`, `rot3`, `cyc3`)
- kind: theorem (positive control) · level: O · status: proved [K]
- statement (KInfFoundations.lean:446–449): "/-- **Positive control for drivability.** The ball is drivable: the
  rotations about the third axis form the flow, the half-turn is the NOT, and the cyclic permutation of the axes carries
  the flow off itself on the ball. -/ noncomputable def ball3Drive : ElementaryDrivability ball3 where flow := rot3 · … ·
  t₀ := Real.pi · … · J := cyc3"; "/-- The ball is drivable. -/ theorem ball3_drivable : Nonempty (ElementaryDrivability
  ball3)" (:489–490); "noncomputable def cyc3 : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cycEquiv.toAffineEquiv" (:425,
  `cyc3 v = (v 2, v 0, v 1)`, :427)
- provenance: KINF-2 §C′ · depends_on: — · yields: I3.83, I3.72 · bridge: none at L (as I3.66)
- bearing: none at L on `K`; it fixes the single-token `J` (`cyc3`) named in (b_DJ) (PROTOCOL-STAGE5.md:23) · flag: —

### I3.68 `not_drivable_Icc`, `not_drivable_singleton`
- kind: theorem (negative controls) · level: O · status: proved [K]
- statement (KInfFoundations.lean:529): "theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1))";
  (:564) "theorem not_drivable_singleton (x : V) : IsEmpty (ElementaryDrivability ({x} : Set V))"
- provenance: KINF-2 §C′ · depends_on: — · yields: I3.72 · bridge: none at L · bearing: none at L · flag: —

### I3.69 `CopyNatural` (K∞-Copy)
- kind: hypothesis-structure (def … : Prop) · level: O (two copies, compared by an identification; no pair carrier) ·
  status: assumed / open — ROADMAP.md:1027–1030 (K∞-Copy, unsourced); KINF-2 "copy naturality: named here as
  definitions, discharged by no OI construction"; NB-1 "Whether OI supplies one common NOT on identical copies
  (identical-copy covariance): not derived, not supplied here"
- statement (KInfFoundations.lean:282–285): "/-- Copy naturality: under the identification `e` of copy `A` with copy
  `B`, the NOT of `B` is the conjugate of the NOT of `A`. -/ def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :
  Prop := N_B = (e.symm.trans N_A).trans e"
- provenance: KINF-2 §C · depends_on: — · yields: `copyNatural_refl_iff`, `copyNatural_iff_apply` (:288, :294); in DIM-1
  the common `N` of both copies is built into `NativeGate` ("with one `N` in both relations"), not derived from
  `CopyNatural` · bridge: none at L (no theorem reads `CopyNatural` into `NativeGate`; DIM-1/RELC-SELECT-1 controls:
  different NOTs on the two copies admit `d = 5`, ROADMAP.md:999–1000) · bearing: constrains the single-token structure
  the pair inherits (would supply the common NOT) · flag: —

### I3.70 `ClassicallyExposed`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition; appears in the conclusion of Theorem F2,
  `classical_exposed_ncard_le`, KInfFoundations.lean:947)
- statement (KInfFoundations.lean:892–895): "/-- A point of a body in the simplex exposed by a response effect: the
  response effect with vector `c ∈ [0, 1]^N` is certain exactly there. -/ def ClassicallyExposed (Ω : Set (Fin N → ℝ))
  (x : Fin N → ℝ) : Prop := ∃ c : Fin N → ℝ, (∀ i, 0 ≤ c i ∧ c i ≤ 1) ∧ {p ∈ Ω | ∑ i, c i * p i = 1} = {x}"
- provenance: KINF-2 §E′ · depends_on: — · yields: I3.72 · bridge: none at L · bearing: none at L · flag: —

### I3.71 `KInf1` (hypothesis K∞-1)
- kind: hypothesis-structure (def … : Prop) · level: O · status: open — docstring "stated and not proved … The module
  proves K∞-1 for no physical family; it is an open target"; holds for `ball3` with full effects (`kInf1_ball3_full`),
  fails with the unit alone (`not_kInf1_ball3_unit`); derived on `ball3` under OG-1's hypotheses (`kInf1_ball3_of_orbit`,
  OrbitGeneration.lean:389)
- statement (KInfFoundations.lean:1008–1015): "/-- **Hypothesis K∞-1**, stated and not proved: a compact convex body
  admitting an elementary drive has supporting-effect completeness relative to the available effects. This is the
  field-neutral Naimark step. … -/ def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := IsCompact Ω → Convex ℝ Ω →
  Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail"
- provenance: KINF-2 §G · depends_on: I3.66, I3.61 · yields: `relStrictConvex_of_kInf1` (:1019) · bridge: none at L
- bearing: none at L · flag: —

### I3.72 `kinf2_kernel_core` (KINF-2 verdict)
- kind: theorem · level: O · status: proved [K] (KINF-2 `KINF-2-FOUNDATIONS-PROVED`)
- statement (KInfFoundations.lean:1098–1124, first lines): "/-- The round's verdict: Lemma C and its converse, the
  inertness of non-proper effects, the semantic controls for (SEC), (SF), drivability and K∞-1, Lemma D, Lemma B, the
  finite-preparation bound and Theorem F2, together. -/ theorem kinf2_kernel_core : (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ]
  ℝ)), Convex ℝ Ω → SupportingEffectComplete Ω avail → SingletonFaces Ω avail → RelStrictConvex Ω) ∧ (∀ (Ω : Set V)
  (avail …), RelStrictConvex Ω → SingletonFaces Ω avail) ∧ … ∧ Nonempty (ElementaryDrivability ball3) ∧ IsEmpty
  (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) ∧ KInf1 ball3 (fullEffects ball3) ∧ ¬ KInf1 ball3 {AffineMap.const ℝ (Fin
  3 → ℝ) (1 : ℝ)} ∧ …" (full text `kdecls.out`)
- provenance: KINF-2 · depends_on: I3.58–I3.71 · yields: K∞ vocabulary of OG-1, CMP-1, TRB-1 · bridge: none at L
- bearing: none at L (single body) · flag: —

### I3.73 `SharpSeed` (K∞-Seed, P1)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open — ROADMAP.md:1023–1024 (K∞-Seed,
  unsourced; "on the completion it follows from SC∞ and a stage effect with values one and zero at two stage
  preparations", I3.97)
- statement (OrbitGeneration.lean:63–66): "/-- **P1, the sharp seed**: an effect on `Ω` with the value one at a state and
  the value zero at a state. -/ def SharpSeed (Ω : Set V) (r : V →ᵃ[ℝ] ℝ) : Prop := IsEffectOn Ω r ∧ (∃ x ∈ Ω, r x = 1)
  ∧ (∃ y ∈ Ω, r y = 0)"
- provenance: OG-1 · depends_on: I3.58 · yields: I3.79, I3.51, I3.37, I3.39 · bridge: through I3.51
- bearing: constrains the composite only through `maxConeOf_avail_eq` (I3.51) · flag: —

### I3.74 `PreservesBody`
- kind: hypothesis-structure (def … : Prop) · level: O (also the joint reversible action of COMP-1, I3.118) · status:
  assumed (OG-1: "the premise on `G` that the statements below need and that none of the three names"; EFF-1 "body
  preservation … which the round does not source")
- statement (OrbitGeneration.lean:68–70): "/-- Every member of `G` is an automorphism of `Ω`: it and its inverse map `Ω`
  into `Ω`. -/ def PreservesBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω"
- provenance: OG-1 · depends_on: — · yields: I3.79, I3.51, I3.88, I3.89, I3.118 · bridge: through I3.51 (for a family on
  one ball); as `JointReversible` (I3.118) it is stated on a composite body, but no kernel statement at L instantiates
  it with idle-extended one-copy maps · bearing: constrains the composite only through I3.51 · flag: —

### I3.75 `SeedOrbitAvailable` (K∞-V4, V4′)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open — ROADMAP.md:1025–1026 ("Body
  preservation of a transport does not supply it"), unsourced
- statement (OrbitGeneration.lean:72–75): "/-- **V4′, seed-orbit availability**: every transport of the seed along a
  member of `G` is available. -/ def SeedOrbitAvailable (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) (avail : Set (V →ᵃ[ℝ] ℝ))
  : Prop := ∀ g ∈ G, seedTransport r g ∈ avail"
- provenance: OG-1 · depends_on: `seedTransport` (OrbitGeneration.lean:49) · yields: I3.51, I3.52, I3.37
- bridge: through I3.51 · bearing: constrains the composite only through I3.51 · flag: —

### I3.76 `BoundaryTransitive` (K∞-Trans; "K∞-R" in OG-1's record)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open — ROADMAP.md:1018–1022 ("K∞-Drive does
  not give it"), unsourced; instances proved [K]: `boundaryTransitive_fullAut3` (I3.80), `boundaryTransitive_ball3Drive`
  (I3.83), `boundaryTransitive_ball4` (I3.85)
- statement (OrbitGeneration.lean:78–80): "/-- **K∞-R, boundary transitivity**: a member of `G` carries any boundary
  state to any other. -/ def BoundaryTransitive (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ x y, IsBoundaryState Ω x →
  IsBoundaryState Ω y → ∃ g ∈ G, g x = y"
- provenance: OG-1; label note ROADMAP.md:1035–1038 · depends_on: I3.60 · yields: I3.79, I3.88–I3.90 (the ball), I3.51
  (the cone), I3.55 · bridge: to the pair cone only through I3.51 (effects, not operations). PT stage 4 (Y O, audited):
  "the literal pair transfer of `BoundaryTransitive` fails for `Q3` itself" (INTEGRATION-NOTE-STAGE4.md:85–86), so it is
  not lifted verbatim · bearing: constrains the single-token structure the pair inherits (the ball of each token) and
  the composite only through I3.51 · flag: —

### I3.77 `CoversBoundaryFrom` (COVER)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (hypothesis of `supportingEffectComplete_of_cover`,
  OrbitGeneration.lean:174; follows from I3.76 by `coversBoundaryFrom_of_transitive`, :187)
- statement (OrbitGeneration.lean:82–84): "/-- COVER: every boundary state is the image of `x₀` under a member of `G`. -/
  def CoversBoundaryFrom (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) (x₀ : V) : Prop := ∀ y, IsBoundaryState Ω y → ∃ g ∈ G, g x₀ =
  y" · provenance: OG-1 §C · depends_on: I3.60 · yields: I3.82 · bridge: none at L · bearing: none at L · flag: —

### I3.78 `preservesBody_drive`
- kind: theorem · level: O · status: proved [K]
- statement (OrbitGeneration.lean:160–162): "/-- The flow members and `J` of an elementary drive are automorphisms of `Ω`.
  -/ theorem preservesBody_drive {Ω : Set V} (D : ElementaryDrivability Ω) : PreservesBody Ω (Set.range D.flow ∪
  {D.J})" · provenance: OG-1 §B′ · depends_on: I3.66 · yields: `preservesBody_driveWords` (OrbitNormalization.lean:107)
- bridge: none at L (single body; the composite form would need `JointReversible` of idle-extended maps, not stated)
- bearing: constrains the single-token structure only · flag: —

### I3.79 `seedOrbit_ball3_eq` (the reduced orbit-generation theorem)
- kind: theorem · level: O · status: proved [K] (OG-1)
- statement (OrbitGeneration.lean:345–350): "/-- **The reduced orbit-generation theorem.** Under `PreservesBody`, P1 and
  K∞-R, the transports of the seed are exactly the directional effects `(1 + b · x)/2`, `|b|² = 1`. -/ theorem
  seedOrbit_ball3_eq {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (hG : PreservesBody ball3 G)
  (hP1 : SharpSeed ball3 r) (hK : BoundaryTransitive ball3 G) : seedOrbit G r = directionalFamily"
- provenance: OG-1 §E · depends_on: I3.74, I3.73, I3.76 · yields: I3.82, I3.81; the `d`-general form is EFF-1's I3.51
- bridge: none at L directly (EFF-1's I3.51 is the bridge) · bearing: constrains the single-token structure · flag: —

### I3.80 `boundaryTransitive_fullAut3`
- kind: theorem (positive control) · level: O · status: proved [K]
- statement (OrbitGeneration.lean:535–537): "/-- **Positive control for K∞-R.** The affine automorphisms of the ball act
  transitively on its boundary. -/ theorem boundaryTransitive_fullAut3 : BoundaryTransitive ball3 fullAut3"; "def
  fullAut3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := {g | ∀ x ∈ ball3, g x ∈ ball3 ∧ g.symm x ∈ ball3}" (:521–522)
- provenance: OG-1 §G; cited by PT stage 4 as the body symmetry of node S4 ("availability unsourced: K∞-Act, K∞-Drive,
  K∞-Trans OPEN", Y/RESULT.md:236) · depends_on: — · yields: I3.82
- bridge: none at L — a symmetry of the single body; no statement at L makes `fullAut3` act on `W 3` or preserve a pair
  cone (that would be (b_S4)) · bearing: constrains the single-token structure only · flag: its pair-level action is
  (b) (do not assume)

### I3.81 `not_boundaryTransitive_flow`
- kind: theorem (negative control) · level: O · status: proved [K]
- statement (OrbitGeneration.lean:618–620): "/-- K∞-R is not implied by P1 and `PreservesBody`: the flow of `ball3Drive`
  satisfies both with the seed `(1 + z)/2`, and is not boundary transitive. -/ theorem not_boundaryTransitive_flow : ¬
  BoundaryTransitive ball3 (Set.range rot3)"
- provenance: OG-1 §G; ROADMAP.md:1020–1022 · depends_on: I3.79 · yields: the K∞-Trans/K∞-Drive separation
- bridge: n/a (O) · bearing: none at L on `K` · flag: —

### I3.82 `orbit_generation_core` (OG-1 verdict)
- kind: theorem · level: O · status: proved [K] (`OG-1-INFRASTRUCTURE-PROVED` with `og1_infrastructure_core`,
  OrbitNormalization.lean:753)
- statement (OrbitGeneration.lean:715–736, first conjuncts): "theorem orbit_generation_core : (∀ (Ω : Set V) (G : Set (V
  ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) (avail : Set (V →ᵃ[ℝ] ℝ)) (x₀ : V), PreservesBody Ω G → IsEffectOn Ω r → IsProperOn Ω r →
  r x₀ = 1 → CoversBoundaryFrom Ω G x₀ → SeedOrbitAvailable G r avail → SupportingEffectComplete Ω avail) ∧ (∀ (G :
  Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ), PreservesBody ball3 G → SharpSeed ball3 r →
  BoundaryTransitive ball3 G → seedOrbit G r = directionalFamily) ∧ … ∧ ¬ BoundaryTransitive ball3 (Set.range rot3) ∧ …"
  (full text `kdecls.out`)
- provenance: OG-1 · depends_on: I3.73–I3.77 · yields: EFF-1, K1-BRIDGE-1 · bridge: through I3.51 · bearing: constrains the single-token structure (as I3.79)
- flag: —

### I3.83 `boundaryTransitive_ball3Drive` (with `driveWords3`)
- kind: theorem · level: O · status: proved [K]
- statement (OrbitNormalization.lean:665–667): "/-- **`ball3Drive` is boundary-transitive.** The words of the landed
  control drive carry any boundary state of `ball3` to any other. -/ theorem boundaryTransitive_ball3Drive :
  BoundaryTransitive ball3 driveWords3"; (:569–572) "/-- The words of the landed control drive: rotations about the
  third axis and the cyclic permutation of the axes. -/ def driveWords3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := words
  (Set.range ball3Drive.flow ∪ {ball3Drive.J})"
- provenance: OG-1 §E · depends_on: I3.67 · yields: [D] `IE1Drive` quantifies over `driveWords3` (I3.142)
- bridge: none at L (the words act on one ball; their pair-level lift exists only as [D] `IE1Drive`) · bearing:
  constrains the single-token structure; it shows the flow with `J` is boundary transitive on the control ball, while
  the flow alone is not (I3.81) · flag: its pair-level action is (b_DJ)-type (do not assume)

### I3.84 `isEmpty_drivability_of_finite_orbits`
- kind: theorem · level: O · status: proved [K]
- statement (OrbitNormalization.lean:124–127): "theorem isEmpty_drivability_of_finite_orbits {Ω : Set V} (hfin : ∀ x ∈
  Ω, {y | ∃ g : V ≃ᵃ[ℝ] V, (∀ z ∈ Ω, g z ∈ Ω ∧ g.symm z ∈ Ω) ∧ g x = y}.Finite) : IsEmpty (ElementaryDrivability Ω)"
- provenance: OG-1 §B · depends_on: I3.66 · yields: — · bridge: none at L · bearing: none at L · flag: —

### I3.85 `boundaryTransitive_ball4`
- kind: theorem (countercontrol: transitivity does not fix dimension three) · level: O · status: proved [K]
- statement (OrbitNormalization.lean:735): "theorem boundaryTransitive_ball4 : BoundaryTransitive ball4 isom4"
- provenance: OG-1 §F · depends_on: — · yields: — · bridge: n/a · bearing: none at L · flag: —

### I3.86 `IsBodyGroup` (TRANS, group clause)
- kind: hypothesis-structure · level: O · status: assumed (component of `TransBody`; instance on `ball3`: TRB-1 §G)
- statement (TransitiveBody.lean:221–227): "/-- **TRANS, the group clause.** `G` contains the identity, is closed under
  composition and inversion, and every member maps `Ω` into `Ω`. -/ structure IsBodyGroup (Ω : Set V) (G : Set (V ≃ᵃ[ℝ]
  V)) : Prop where one_mem : AffineEquiv.refl ℝ V ∈ G · mul_mem : ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G · inv_mem : ∀ g ∈ G,
  g.symm ∈ G · preserves : ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω"
- provenance: TRB-1 §C · depends_on: — · yields: I3.87 · bridge: none at L · bearing: none at L · flag: —

### I3.87 `TransBody` (TRANS)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (TRB-1: "a source of a body-preserving
  boundary-transitive family … in an OI construction" stays open)
- statement (TransitiveBody.lean:234–235): "/-- **TRANS.** A body group acting transitively on every boundary state of
  `Ω`. -/ def TransBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := IsBodyGroup Ω G ∧ BoundaryTransitive Ω G"
- provenance: TRB-1 · depends_on: I3.86, I3.76 · yields: TRB-1 corollaries · bridge: none at L · bearing: constrains
  the single-token structure the pair inherits (the ball) · flag: —

### I3.88 `eq_qBall_of_boundaryTransitive`
- kind: theorem · level: O · status: proved [K] (`TRB-1-BALL-PROVED`)
- statement (TransitiveBody.lean:457–460): "theorem eq_qBall_of_boundaryTransitive (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc
  : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG :
  PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R"
- provenance: TRB-1 §E · depends_on: I3.74, I3.76, I3.91 · yields: I3.89 · bridge: none at L · bearing: constrains the
  single-token structure the pair inherits (every token body is a ball: the factors of `W d`) · flag: —

### I3.89 `exists_affine_image_eq_eball`
- kind: theorem · level: O · status: proved [K]
- statement (TransitiveBody.lean:602–605): "theorem exists_affine_image_eq_eball (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc :
  IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG :
  PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ A : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), A '' Ω = eball d"
- provenance: TRB-1 §F; ROADMAP.md:1018–1019 · depends_on: I3.88 · yields: the `eball d` of DIM-1/EFF-1 (by
  normalization; no kernel theorem composes TRB-1 with DIM-1) · bridge: none at L as a theorem; DIM-1 takes `eball d`
  as given · bearing: constrains the single-token structure the pair inherits · flag: —

### I3.90 `extreme_of_isBoundaryState_of_transitive` (boundary purity)
- kind: theorem · level: O · status: proved [K]
- statement (TransitiveBody.lean:290–293): "theorem extreme_of_isBoundaryState_of_transitive [Nontrivial V] {Ω : Set V}
  (hc : IsCompact Ω) (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty) {G : Set (V ≃ᵃ[ℝ] V)} (hG : PreservesBody Ω G)
  (hT : BoundaryTransitive Ω G) {x : V} (hx : IsBoundaryState Ω x) : x ∈ Ω.extremePoints ℝ"
- provenance: TRB-1 §D · depends_on: I3.74, I3.76 · yields: — · bridge: none at L · bearing: none at L · flag: —

### I3.91 `invariant_inner_product` (with `centroid_fixed`)
- kind: theorem (premise-free) · level: O · status: proved [K] (`IIP-1-INVARIANT-INNER-PRODUCT-PROVED`)
- statement (InvariantInnerProduct.lean:336–342): "theorem invariant_inner_product {Ω : Set (Fin n → ℝ)} (hc :
  IsCompact Ω) (hi : (interior Ω).Nonempty) : (invMatrix Ω)ᵀ = invMatrix Ω ∧ (∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)) ∧
  ∀ g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ), g '' Ω = Ω → g (centroid Ω) = centroid Ω ∧ ∀ u v, (linMatrix g *ᵥ u) ⬝ᵥ (invMatrix
  Ω *ᵥ (linMatrix g *ᵥ v)) = u ⬝ᵥ (invMatrix Ω *ᵥ v)"
- provenance: IIP-1 ("Nothing here is a hypothesis about OI") · depends_on: — · yields: I3.88 · bridge: none at L
- bearing: none at L · flag: —

### I3.92 `DirectedStages` (with `StageMap`)
- kind: definition-as-hypothesis (data structure) · level: O · status: proved [K] (definition); only control instances
  at L (`badD`, `bitTower`, `midD`; KT4-PREM-1 Q2: "no declaration builds a directed system from two systems")
- statement (StageCompletion.lean:62–74): "/-- A directed system of finite stages with functorial forward maps. -/
  structure DirectedStages where ι : Type · [pre : Preorder ι] · [ne : Nonempty ι] · directed : ∀ i j : ι, ∃ k, i ≤ k ∧
  j ≤ k · stage : ι → FiniteStage · map : ∀ {i j : ι}, i ≤ j → StageMap (stage i) (stage j) · comp_E : … · comp_P : …";
  `StageMap` (:52–56) "/-- A map of finite stages: effects and preparations carried forward, unit to unit. -/"
- provenance: CMP-1 §A · depends_on: I3.57 · yields: I3.94–I3.105 · bridge: none at L (the stage-level product of two
  `DirectedStages` is outside COMP-1, open: COMP-1 header, KT4-PREM-1 open question 3) · bearing: constrains the
  single-token structure (K∞-Stage) · flag: —

### I3.93 `StageMap.Consistent`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition; the component of SC∞)
- statement (StageCompletion.lean:58–60): "/-- Table consistency of a stage map. -/ def StageMap.Consistent {S T :
  FiniteStage} (f : StageMap S T) : Prop := ∀ e x, T.p (f.onE e) (f.onP x) = S.p e x"
- provenance: CMP-1 · depends_on: I3.92 · yields: I3.94 · bridge: none at L · bearing: none at L · flag: —

### I3.94 `SCInf` (SC∞, K∞-Stage)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open — ROADMAP.md:1010–1013 (K∞-Stage
  "`SCInf`, `BinaryVisible` and `FiniteRank`", unsourced); CMP-1 "Nothing here derives SC∞ … from an OI construction"
- statement (StageCompletion.lean:77–79): "/-- **SC∞, stage consistency**: every forward map carries the probability
  table. -/ def SCInf (D : DirectedStages) : Prop := ∀ (i j : D.ι) (h : i ≤ j), (D.map h).Consistent"
- provenance: CMP-1 · depends_on: I3.92, I3.93 · yields: I3.97, `val_eq_at` · bridge: none at L · bearing: constrains
  the single-token structure (the completion upstream of the ball) · flag: —

### I3.95 `BinaryVisible` (ELEM-bin)
- kind: hypothesis-structure (data structure with Prop fields) · level: O · status: assumed / open (K∞-Stage; "the
  binary-visible part of the elementary-system scope — necessary, not sufficient"; ROADMAP.md:1012–1013 "A predicate
  for the full elementary-visible scope is not yet formalized")
- statement (StageCompletion.lean:240–249): "/-- **ELEM-bin, the binary-visible condition**: every stage carries a binary
  visible test, and the forward maps carry the visible outcomes to the visible outcomes. It is the binary-visible part of
  the elementary-system scope — necessary, not sufficient; it says nothing about reading the body on the visible factor
  alone. -/ structure BinaryVisible where v0 : ∀ i, (D.stage i).E · v1 : ∀ i, (D.stage i).E · test : ∀ i x, (D.stage
  i).p (v0 i) x + (D.stage i).p (v1 i) x = 1 · carried0 : … · carried1 : …"
- provenance: CMP-1 · depends_on: I3.92 · yields: `visible_test_completion`, `perfectlyDistinguishable_visible`
- bridge: none at L · bearing: constrains the single-token structure · flag: —

### I3.96 `FiniteRank` (K∞-Stage)
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open (ROADMAP.md:1010–1012: "Finite rank gives
  the completion chart that TRB-1 normalizes"; unsourced). PT stage 1 (A, audited): FiniteRank of an OI-native pair
  completion is the non-restating source of `hcl` (INTEGRATION-REVIEW.md:80, U2)
- statement (StageCompletion.lean:298–300): "/-- **Finite rank**: the affine span of the body is finite-dimensional. -/
  def FiniteRank (Ω : Set V) : Prop := FiniteDimensional ℝ (affineSpan ℝ Ω).direction"
- provenance: CMP-1 · depends_on: — · yields: I3.98, I3.103 · bridge: none at L (no pair completion at L) · bearing:
  constrains the single-token structure; for a pair system it would bear on closedness (`hcl`, I3.131) only through a
  pair completion that L does not define · flag: —

### I3.97 `sharpSeed_completion`
- kind: theorem · level: O · status: proved [K]
- statement (StageCompletion.lean:222–226): "/-- **The sharp seed survives the completion under SC∞.** A stage effect
  certain at one stage preparation and zero at another is a sharp seed on the completion body. -/ theorem
  sharpSeed_completion (hSC : SCInf D) {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P} (h1 : (D.stage i).p e x1 =
  1) (h0 : (D.stage i).p e x0 = 0) : SharpSeed (body D) (coord D ⟨i, e⟩)"
- provenance: CMP-1 §C; ROADMAP.md:1023–1024 · depends_on: I3.94 · yields: I3.73 on the completion · bridge: none at L
- bearing: constrains the single-token structure · flag: —

### I3.98 `exists_chart_of_finiteRank`
- kind: theorem · level: O · status: proved [K]
- statement (StageCompletion.lean:304–306): "theorem exists_chart_of_finiteRank {Ω : Set V} (hne : Ω.Nonempty) (hfr :
  FiniteRank Ω) : ∃ (d : ℕ) (L : (Fin d → ℝ) →ₗ[ℝ] V) (p0 : V), LinearMap.ker L = ⊥ ∧ ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈
  Set.range (chart L p0)" · provenance: CMP-1 §E · depends_on: I3.96 · yields: I3.103, TRB-1 §A
- bridge: none at L · bearing: constrains the single-token structure · flag: —

### I3.99 `OpDatum` (K∞-Act)
- kind: hypothesis-structure (data structure with a Prop field) · level: O · status: assumed / open — ROADMAP.md:1014–1016
  (K∞-Act "reversible operation data on the completed body: an `OpDatum` with `AffineRespect` and an inverse datum",
  unsourced); OPACT-1 "Nothing here supplies an operation datum"
- statement (CompletionAction.lean:44–48): "/-- A completion-valued operation datum: the completed state each stage
  preparation is carried to. -/ structure OpDatum (D : DirectedStages) where τ : Prep D → CSpace D · mem_body : ∀ x, τ
  x ∈ body D"
- provenance: OPACT-1 · depends_on: I3.92 · yields: I3.100–I3.105, I3.110 · bridge: none at L. KT4-PREM-1 Q2: P-ACT2
  (the gate as an `OpDatum` of a pair system, I3.146) "states gate preservation on preparations; it does not derive it"
- bearing: constrains the single-token structure; at the pair level only through P-ACT2 (not at L) · flag: —

### I3.100 `StateRespect`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (weaker than I3.101: `midOp_stateRespect`,
  `midOp_not_affineRespect`, CompletionAction §E)
- statement (CompletionAction.lean:52–54): "/-- **StateRespect**: preparations with the same preparation vector have the
  same image. -/ def StateRespect (T : OpDatum D) : Prop := ∀ x y, prepVec D x = prepVec D y → T.τ x = T.τ y"
- provenance: OPACT-1 §A · depends_on: I3.99 · yields: — · bridge: none at L · bearing: none at L · flag: —

### I3.101 `AffineRespect`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (K∞-Act; hypothesis of I3.105, I3.111)
- statement (CompletionAction.lean:56–60): "/-- **AffineRespect**: every finite affine relation among preparation
  vectors holds among the images. -/ def AffineRespect (T : OpDatum D) : Prop := ∀ (s : Finset (Prep D)) (c : Prep D →
  ℝ), ∑ x ∈ s, c x = 0 → ∑ x ∈ s, c x • prepVec D x = 0 → ∑ x ∈ s, c x • T.τ x = 0"
- provenance: OPACT-1 · depends_on: I3.99 · yields: I3.105 · bridge: none at L · bearing: constrains the single-token
  structure · flag: —

### I3.102 `Undoes`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (the inverse-datum hypotheses `hST`, `hTS` of
  I3.105; "inverse availability" open, OPACT-1)
- statement (CompletionAction.lean:324–326): "/-- `S` undoes `T`: `S` after `T` returns every stage preparation. -/ def
  Undoes (S T : OpDatum D) (hS : AffineRespect S) : Prop := ∀ x, (after C S T hS).τ x = prepVec D x"
- provenance: OPACT-1 §D · depends_on: I3.99, I3.101, I3.103 · yields: I3.105 · bridge: none at L · bearing: none at L
- flag: —

### I3.103 `CompletionChart`
- kind: definition-as-hypothesis (data structure) · level: O · status: proved [K] (definition; "which a nonempty body of
  `FiniteRank` admits", OPACT-1 header)
- statement (CompletionAction.lean:142–151): "/-- The chart data of a completed body: an injective affine chart of its
  affine span, with a left inverse of the chart's linear part. -/ structure CompletionChart (D : DirectedStages) where d
  : ℕ · L : (Fin d → ℝ) →ₗ[ℝ] CSpace D · p0 : CSpace D · Lg : CSpace D →ₗ[ℝ] (Fin d → ℝ) · hL : LinearMap.ker L = ⊥ ·
  hLg : ∀ w, Lg (L w) = w · hspan : ∀ v, v ∈ affineSpan ℝ (body D) ↔ v ∈ Set.range (chart L p0)"
- provenance: OPACT-1 §C · depends_on: I3.92, I3.98 · yields: I3.105, I3.111, TRB-1 §A · bridge: none at L · bearing:
  none at L · flag: —

### I3.104 `body_isClosed`
- kind: theorem · level: O · status: proved [K]
- statement (CompletionAction.lean:202): "theorem body_isClosed : IsClosed (body D) := isClosed_closure"; `body`
  (StageCompletion.lean:140–142): "/-- **The completion body**: the closed convex hull of the preparation vectors. -/ def
  body : Set (CSpace D) := closure (convexHull ℝ (Set.range (prepVec D)))"
- provenance: OPACT-1; KT4-PREM-1 source map row `hcl` ("`body_isClosed`, for one system")
- depends_on: I3.92 · yields: P-STAGE2 → `hcl` (I3.145, I3.131) · bridge: none at L (one directed system; the pair
  completion with chart onto `W 3` is P-STAGE2, not at L) · bearing: constrains the composite only through P-STAGE2,
  which L does not state · flag: —

### I3.105 `preservesBody_inducedEquiv`
- kind: theorem · level: O · status: proved [K]
- statement (CompletionAction.lean:352–354): "theorem preservesBody_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S)
  (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) : PreservesBody (chartBody C) {inducedEquiv C
  hS hT hST hTS}" · provenance: OPACT-1 §D; ROADMAP.md:1014–1016; KT4-PREM-1 row `hgate` ("for one system")
- depends_on: I3.99, I3.101, I3.102, I3.103 · yields: P-ACT2 → `hgate` (I3.146, I3.132) · bridge: none at L (P-ACT2
  "restates gate preservation") · bearing: constrains the composite only through P-ACT2, not at L · flag: —

### I3.106 `InfiniteOrderOn`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (CompositionOrder.lean:49–52): "/-- Infinite order on `Ω`: every positive power moves some state of `Ω`.
  Iteration is of the underlying function. -/ def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∀ m : ℕ, 1 ≤ m
  → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x" · provenance: ORD-1 · depends_on: — · yields: I3.108 · bridge: none at L · bearing: none
  at L · flag: —

### I3.107 `FiniteOrderOn`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (CompositionOrder.lean:54–56): "/-- Finite order on `Ω`: some positive power fixes every state of `Ω`. -/
  def FiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x"
- provenance: ORD-1 · depends_on: — · yields: I3.111 · bridge: none at L · bearing: none at L · flag: —

### I3.108 `OrdInf` (ORD∞)
- kind: hypothesis-structure (def … : Prop) · level: O · status: open (ORD-1: "Whether a composition-closed
  boundary-transitive family in dimension ≥ 2 has a member of infinite order" stays open; "TRANS ⇒ ORD∞ is not stated")
- statement (CompositionOrder.lean:58–60): "/-- **ORD∞**: some member of `G` has infinite order on `Ω`. A predicate on a
  set of affine automorphisms; nothing about closure. -/ def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈
  G, InfiniteOrderOn Ω g" · provenance: ORD-1 · depends_on: I3.106 · yields: I3.112 · bridge: none at L · bearing:
  none at L · flag: —

### I3.109 `MulClosed`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition; hypothesis of I3.112)
- statement (CompositionOrder.lean:62–63): "/-- Composition closure of a set of affine automorphisms. -/ def MulClosed (G
  : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G" · provenance: ORD-1 · depends_on: — · yields: I3.112
- bridge: none at L · bearing: none at L · flag: —

### I3.110 `StagePreserving`
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed (hypothesis of I3.111; ORD-1 "a source … of
  stage preservation in an OI construction" open)
- statement (CompositionOrder.lean:232–235): "/-- **Stage preservation**: each preparation of stage `i` is carried to a
  preparation vector of the same stage `i`. -/ def StagePreserving (T : OpDatum D) : Prop := ∀ (i : D.ι) (x : (D.stage
  i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩" · provenance: ORD-1 · depends_on: I3.99 · yields: I3.111
- bridge: none at L · bearing: none at L · flag: —

### I3.111 `finiteOrderOn_of_stagePreserving`
- kind: theorem · level: O · status: proved [K] (`ORD-1-COMPOSITION-ORDER-PROVED`)
- statement (CompositionOrder.lean:348–351): "theorem finiteOrderOn_of_stagePreserving {S T : OpDatum D} (hS :
  AffineRespect S) (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (hsp : StagePreserving T) :
  FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)"
- provenance: ORD-1 §D · depends_on: I3.99–I3.103, I3.110 · yields: `ord1_core` (:456); research record DRIVE-RESULT
  (pt/inputs/ledgers, not at L) reads it as "the generator must cross stages" · bridge: none at L · bearing: constrains
  the single-token structure (a stage-preserving operation cannot generate a drive) · flag: —

### I3.112 `not_ordInf_of_finite_of_mulClosed`
- kind: theorem · level: O · status: proved [K]
- statement (CompositionOrder.lean:109–110): "theorem not_ordInf_of_finite_of_mulClosed {Ω : Set V} {G : Set (V ≃ᵃ[ℝ]
  V)} (hG : G.Finite) (hcl : MulClosed G) : ¬ OrdInf Ω G" · provenance: ORD-1 §E · depends_on: I3.108, I3.109
- yields: `ord1_core` · bridge: none at L · bearing: none at L · flag: —

## §F — the composite interface (COMP-1, `CompositeInterface.lean`)

### I3.113 `ProductData`
- kind: definition-as-hypothesis (data structure with Prop fields) · level: P · status: proved [K] (definition; the
  coordinate model `Fin (dA+1) → Fin (dB+1) → ℝ` is an instance, CompositeInterface §E)
- statement (CompositeInterface.lean:207–217): "/-- Product-state and product-effect data on a real carrier `V`: a
  bi-affine product-state map and a bilinear product-effect pairing with the evaluation law `prodEff e f (prodState x y) =
  e x * f y`. -/ structure ProductData (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where prodState
  : … · prodState_combo_left : … · prodState_combo_right : … · prodEff : ((Fin dA → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin dB → ℝ)
  →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ) · prodEff_apply : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ)
  →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ) (y : Fin dB → ℝ), prodEff e f (prodState x y) = e x * f y"
- provenance: COMP-1 §B · depends_on: — · yields: I3.114 · bridge: n/a (P; "The coordinate model of §E … is confined
  to the instances and enters no statement about the interface") · bearing: direct (product structure of a composite)
- flag: —

### I3.114 `PreComposite`
- kind: hypothesis-structure (data structure with Prop fields) · level: P · status: assumed (the eight interface fields;
  KT4-PREM-1 row `hadm`: "the pair system as a pre-composite in the coordinate model `W 3`, which presupposes the open
  composite obligation K2"; PT stage 1 D, T3: `hadm ⟺` product-test cone of a COMP-1 pre-composite of two balls)
- statement (CompositeInterface.lean:220–230): "/-- A pre-composite: product data together with a convex body `Ω` of the
  carrier that contains the product states, on which every product of effects is an effect and the unit pairing is one.
  These are the eight fields of the interface other than local tomography. -/ structure PreComposite (ΩA : Set (Fin dA
  → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] extends ProductData dA dB V where Ω
  : Set V · convex : Convex ℝ Ω · prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω · prodEff_effect : … IsEffectOn ΩA
  e → IsEffectOn ΩB f → IsEffectOn Ω (prodEff e f) · prodEff_unit : ∀ ω ∈ Ω, prodEff (unitEff dA) (unitEff dB) ω = 1"
- provenance: COMP-1 · depends_on: I3.113, I3.58 · yields: I3.115–I3.122; [D] `KT4`, `TokenCoherent`
- bridge: n/a · bearing: direct (a composite body: products inside, product effects valid) · flag: —

### I3.115 `LocallyTomographic`
- kind: hypothesis-structure (def … : Prop) · level: P · status: assumed / open (K2: "local tomography, which DIM-1's
  carrier `W d` encodes as a premise", ROADMAP.md:1003; independent of the other fields, I3.121)
- statement (CompositeInterface.lean:232–238): "/-- Local tomography of a pre-composite: two states of the body that agree
  on every product of effects are equal. Stated as a predicate so that it can be asserted of a structure as a field and
  refuted of another as a control. -/ def LocallyTomographic … (P : PreComposite ΩA ΩB V) : Prop := ∀ ω ∈ P.Ω, ∀ ω' ∈
  P.Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ), IsEffectOn ΩA e → IsEffectOn ΩB f → P.prodEff e f ω =
  P.prodEff e f ω') → ω = ω'"
- provenance: COMP-1 · depends_on: I3.114 · yields: I3.116, I3.121 · bridge: n/a · bearing: direct (built into `W d`,
  I3.1) · flag: —

### I3.116 `Composite`
- kind: hypothesis-structure (data structure with Prop fields) · level: P · status: assumed (`lt` "is a premise of the
  structure; it is not derived from the other eight fields anywhere in this module")
- statement (CompositeInterface.lean:240–246): "/-- **The weak composite interface.** A pre-composite with local
  tomography as a field. … -/ structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V :
  Type) [NormedAddCommGroup V] [NormedSpace ℝ V] extends PreComposite ΩA ΩB V where lt : ∀ ω ∈ Ω, ∀ ω' ∈ Ω, (∀ (e :
  (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ), IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω')
  → ω = ω'"
- provenance: COMP-1 · depends_on: I3.114, I3.115 · yields: `ball3MinComposite`, `ball3MaxComposite` (:807, :811), [D]
  `KT4LT` · bridge: none at L to `W d` ("an adapter from COMP-1's `Composite` to the carrier `W d`" open, DIM-1)
- bearing: direct · flag: —

### I3.117 `BoundedAffine`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition; holds for compact bodies,
  `boundedAffine_of_isCompact`, CompositeInterface.lean:142)
- statement (CompositeInterface.lean:138–140): "/-- Every affine functional is bounded in absolute value on `Ω`. -/ def
  BoundedAffine (Ω : Set (Fin d → ℝ)) : Prop := ∀ e : (Fin d → ℝ) →ᵃ[ℝ] ℝ, ∃ B : ℝ, ∀ x ∈ Ω, |e x| ≤ B"
- provenance: COMP-1 §E (LT is a theorem of the coordinate model through `prodEff_eq_of_eff_eq`, which "needs only that
  affine functionals are bounded on the factor bodies") · depends_on: — · yields: LT in the coordinate model
- bridge: n/a · bearing: none at L on `K` · flag: —

### I3.118 `JointReversible`
- kind: hypothesis-structure (abbrev … : Prop) · level: P · status: assumed (a predicate; no OI source; KT4-PREM-1 / PT
  stage 1 B: `JointReversible`/`PreservesBody` of the pair slice restates `hgate`)
- statement (CompositeInterface.lean:444–445): "/-- Joint reversible action: a family of affine automorphisms of the
  carrier preserving the body. -/ abbrev JointReversible (G : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω G"
- provenance: COMP-1 (L10: `jointReversible_words`) · depends_on: I3.74, I3.114 · yields: L10
- bridge: n/a. It is the kernel's form of "a family of maps preserving a composite body"; instantiated at L with no
  idle-extended one-copy family · bearing: direct constraint on `K` if instantiated; (b_min) has the form
  `JointReversible` of an idle-extended one-token family — no such instance at L · flag: an instance with idle-extended
  rotations is (b) (do not assume)

### I3.119 `SharpReadout`
- kind: definition-as-hypothesis (data structure with Prop fields) · level: O (register) · status: proved [K]
  (definition; hypothesis-data of L5)
- statement (CompositeInterface.lean:391–397): "/-- A sharp register readout: a perfectly distinguishable pair of register
  states and effects whose two effects sum to the unit functional. -/ structure SharpReadout (ΩB : Set (Fin dB → ℝ))
  where y : Fin 2 → (Fin dB → ℝ) · f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ · pd : PerfectlyDistinguishable ΩB y f · sum_eq :
  f 0 + f 1 = unitEff dB" · provenance: COMP-1 · depends_on: I3.64 · yields: L5–L7 · bridge: n/a · bearing: none at L
- flag: —

### I3.120 `condA_prodState` (L9, no signalling on products)
- kind: theorem · level: P · status: proved [K]
- statement (CompositeInterface.lean:331–333): "/-- **L9.** No signalling on products: the conditional state of a product
  is its first factor. -/ theorem condA_prodState (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {y : Fin dB → ℝ} (hy : f y ≠ 0) (x : Fin
  dA → ℝ) : D.condA f (D.prodState x y) = x"
- provenance: COMP-1 §C · depends_on: I3.113 · yields: `comp1_core` · bridge: n/a · bearing: direct but only on
  products (PT stage 5 candidate θ: steering/no-signalling, `maxCone`) · flag: —

### I3.121 `not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre` (with `paddedBall3`)
- kind: theorem (independence control) · level: P · status: proved [K]
- statement (CompositeInterface.lean:885–896): "theorem not_locallyTomographic_paddedPre (hne : P.Ω.Nonempty) : ¬
  LocallyTomographic (paddedPre P)"; "theorem no_composite_over_paddedPre (hne : P.Ω.Nonempty) : ¬ ∃ C : Composite ΩA ΩB
  (V × ℝ), C.toPreComposite = paddedPre P"; `paddedBall3` (:908–910) "/-- The padding control on the ball pair. -/"
- provenance: COMP-1 §G ("the field `lt` is therefore independent of the other fields and is never derived from them");
  PT stage 1/2: LT INDEPENDENT (`paddedBall3`) · depends_on: I3.114 · yields: LT independence
- bridge: n/a · bearing: direct (LT is not implied by the pre-composite fields) · flag: —

### I3.122 `comp1_core` (COMP-1 verdict)
- kind: theorem · level: P · status: proved [K] (`COMP-1-INTERFACE-PROVED`)
- statement (CompositeInterface.lean:922–926, first conjunct): "/-- Round COMP-1, together: the laws L1–L11 for every
  composite, the three instances, and the padding control. -/ theorem comp1_core : (∀ (dA dB : ℕ) (V : Type)
  [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V) (x : Fin dA → ℝ) (y : Fin dB → ℝ), D.margA
  (D.prodState x y) = x) ∧ …" · provenance: COMP-1 · depends_on: I3.113–I3.121 · yields: COMP-1 instances, KT4-PREM-1
  Q2 (`K_cl` slice is a `Composite` with non-closed body that `cnot` preserves) · bridge: n/a
- bearing: direct (interface laws hold for every composite; none selects a cone) · flag: —

## §G — NB-1 and the effect cone of the ball (`NativeGateBall.lean`; DIM-1 §L)

### I3.123 `Lor`
- kind: definition-as-hypothesis (theorem-internal auxiliary: "`Lor` occurs in no hypothesis", DIM-1) · level: O · status: proved
  [K] (definition)
- statement (CompositeDimension.lean:867–869): "/-- The cone of homogenized vectors whose unit coordinate dominates the
  norm of the rest: the homogenized coefficients of the effects of the ball, up to scale. -/ def Lor (v : HVec d) : Prop
  := 0 ≤ v 0 ∧ ∑ j : Fin d, v j.succ ^ 2 ≤ v 0 ^ 2" · provenance: DIM-1 §L · depends_on: — · yields: I3.124
- bridge: n/a · bearing: none at L on its own · flag: —

### I3.124 the effect cone of the ball: `lor_ehom`, `isEffectOn_affOf`, `lor_toOp_of_maxCone`
- kind: theorem · level: O (`lor_ehom`, `isEffectOn_affOf`), P (`lor_toOp_of_maxCone`) · status: proved [K]
- statement: "theorem lor_ehom {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) : Lor (ehom e)"
  (CompositeDimension.lean:930); "theorem isEffectOn_affOf {v : HVec d} (hv : Lor v) (hv0 : v 0 ≤ 1 / 2) : IsEffectOn
  (eball d) (affOf v)" (:916–917); "theorem lor_toOp_of_maxCone {ω : W d} (hω : ω ∈ maxCone (eball d)) {f : HVec d} (hf
  : Lor f) : Lor (toOp ω f)" (:1049–1050)
- provenance: DIM-1 ("the cone geometry is a theorem about `maxCone`") · depends_on: I3.123, I3.3 · yields: I3.13
  positivity, the block reduction · bridge: `lor_toOp_of_maxCone` is an O→P statement: a `maxCone` vector, read as an
  operator, carries the single-ball effect cone (Lorentz, self-dual) into itself · bearing: constrains the single-token
  structure the pair inherits (the token's effect cone is the Lorentz cone; this is the single-system self-duality that
  has no pair-level counterpart at L, cf. H3, I3.149) · flag: —

### I3.125 `NativeGateBall.parity`
- kind: theorem (premise-free linear algebra) · level: P (general vector space; used in the pair selectors) · status: proved [K]
  (`NB-1-CORE-PROVED`)
- statement (NativeGateBall.lean:192–197): "/-- **S5.** An injective linear map anticommuting with `P` maps the `+1`
  eigenspace of `P` injectively into the `−1` eigenspace and back, so the two have equal dimension. -/ theorem parity {V
  : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V] (P L : V →ₗ[ℝ] V) (hL : Function.Injective L) (hanti :
  ∀ v, L (P v) = - P (L v)) : Module.finrank ℝ (LinearMap.ker (P - LinearMap.id)) = Module.finrank ℝ (LinearMap.ker (P +
  LinearMap.id))" · provenance: NB-1 §D · depends_on: — · yields: I3.15 · bridge: n/a · bearing: constrains the single-token structure the pair inherits (the dimension count of the selectors) · flag: —

### I3.126 `p_le_one`, `dim_of_bounds`
- kind: theorem · level: P (matrix/arithmetic; used in the pair selectors) · status: proved [K]
- statement (NativeGateBall.lean:174–183): "/-- **S4, conclusion.** If some entry of the E₊ block is nonzero (as
  invertibility requires), then `p ≤ 1`. -/ theorem p_le_one (p m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p
  → Fin p → Matrix (Fin m) (Fin m) ℝ) (hB : ∀ r s, B r s = - B s r) (hpos : …) (hne : ∃ r k l, A r k l ≠ 0) : p ≤ 1";
  (:248–249) "theorem dim_of_bounds (p q d : ℕ) (hp : p ≤ 1) (hpq : p = q) (hd : p + q + 1 = d) : d = 1 ∨ d = 3"
- provenance: NB-1 §C, §F · depends_on: — · yields: I3.18 (through I3.16) · bridge: n/a · bearing: constrains the single-token structure the pair inherits (the dimension count of the selectors) · flag: —

### I3.127 `lorentz_of_effects`
- kind: theorem · level: O · status: proved [K]
- statement (NativeGateBall.lean:104–107): "/-- If every unit effect direction `b` keeps `x₀ + b·v ≥ 0`, then `x₀ ≥ 0`
  and `|v|² ≤ x₀²`. -/ theorem lorentz_of_effects (p : ℕ) (hp : 1 ≤ p) (x0 : ℝ) (v : Fin p → ℝ) (h : ∀ b : Fin p → ℝ,
  (∑ j, b j ^ 2) = 1 → 0 ≤ x0 + ∑ j, b j * v j) : 0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2"
- provenance: NB-1 §B; OG-1 §F ("the family is exactly the hypothesis of `NativeGateBall.lorentz_of_effects` at `p =
  3`") · depends_on: — · yields: `lorentz_of_seedOrbit`, `lorentz_of_available` (OrbitGeneration.lean:406, :422)
- bridge: none at L · bearing: constrains the single-token structure (single-ball self-duality test) · flag: —

### I3.128 `nb1_kernel_core` (NB-1 verdict)
- kind: theorem · level: P (premise-free; used in the pair selectors) · status: proved [K]; NB-1: "That theorem [the finite native-gate ball no-go] is not a kernel
  theorem: its proof is layered, and this module certifies one layer of it" (the `d`-general layer was completed in
  DIM-1 §Q)
- statement (NativeGateBall.lean:255–268): "theorem nb1_kernel_core : (∀ (p m : ℕ) (A …) (B …), (∀ r s, B r s = - B s r)
  → … → (∃ r k l, A r k l ≠ 0) → p ≤ 1) ∧ (∀ (V : Type) … (P L : V →ₗ[ℝ] V), Function.Injective L → (∀ v, L (P v) = - P
  (L v)) → Module.finrank ℝ (LinearMap.ker (P - LinearMap.id)) = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id))) ∧
  (∀ p q d : ℕ, p ≤ 1 → p = q → p + q + 1 = d → d = 1 ∨ d = 3)"
- provenance: NB-1 · depends_on: — · yields: DIM-1 · bridge: n/a · bearing: constrains the single-token structure the pair inherits (the dimension count of the selectors) · flag: —

## §H — the KT4 premise audit (KT4-PREM-1, landed) and the four-copy design modules [D] (`pt/inputs/fourcopy/`)

Status of the five premises of the audited theorem (KT4-PREM-1 result.md:17–21, :174–182, :196–201): "**Premises with
an independent source on `D`.** None of the five hypotheses"; each "needs an additional premise". The landed round
checks models by exact computation (probe and independent check), not in the kernel ("no countermodel is
kernel-checked", result.md:238). The design modules are not at L.

### I3.129 `hcls` — N-CLASS gates (`NClass`)
- kind: hypothesis-structure (def … : Prop, [D]) · level: P · status: not at L — [D] FourCopyCore.lean:130–134; as a
  premise: assumed, "a classification of control gates at `d = 3` as N-CLASS, which `D` does not contain; its inputs
  `IsNot`, `CtrlGate` and the entangling clause are open premises of ROADMAP row K1" (KT4-PREM-1 result.md:178);
  cannot be dropped (`M_refl`), not necessary (`M_id`); PT stage 1 (D, audited): CONDITIONAL on K1's gate premises (T1)
- statement (FourCopyCore.lean:130–134): "/-- **N-CLASS**: the gate is `cnot` between orthogonal local maps, post-locals
  `(A, B)` and pre-locals `(A', B')`. -/ def NClass (N : W 3 ≃ₗ[ℝ] W 3) (A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) :
  Prop := IsOrth3 A ∧ IsOrth3 B ∧ IsOrth3 A' ∧ IsOrth3 B' ∧ ∀ ω, N ω = actC A (actT B (cnot (actC A' (actT B' ω))))"
- provenance: design module; KT4-PREM-1 Q3 · depends_on: I3.6, I3.7, I3.11, `IsOrth3` (FourCopyCore.lean:118–120)
- yields: I3.139 · bridge: n/a (P) · bearing: direct (the gate of each pair cone; local maps are the chart, not an action
  on `K`) · flag: —

### I3.130 `hadm` — pair admissibility (`PairAdm`, with `IsConvexCone`)
- kind: hypothesis-structure (def … : Prop, [D]) · level: P · status: not at L — [D] FourCopyDefs.lean:42–43; as a
  premise: assumed; KT4-PREM-1: "the pair system as a pre-composite in the coordinate model `W 3`, which presupposes the
  open composite obligation K2" (result.md:179); cannot be dropped (`M_class`), not necessary (`M_mix`); PT stage 1:
  (a), (b), (c) each INDEPENDENT of L (INTEGRATION-REVIEW.md:98–100)
- statement (FourCopyDefs.lean:38–43): "/-- A convex cone of tables. -/ def IsConvexCone (K : Set (W 3)) : Prop := (∀ ω ∈
  K, ∀ ω' ∈ K, ω + ω' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K"; "/-- Admissibility of one pair cone: a candidate cone
  of K2-GUARD-1 that is a convex cone. -/ def PairAdm (K : Set (W 3)) : Prop := CandidateCone K ∧ IsConvexCone K"
- provenance: design module; KT4-PREM-1 Q3 · depends_on: I3.43 · yields: I3.139, I3.140 · bridge: n/a · bearing:
  direct constraint on `K` · flag: —

### I3.131 `hcl` — closedness of each pair cone
- kind: hypothesis-structure (hypothesis `∀ p, IsClosed (K p)` of I3.139) · level: P · status: assumed; KT4-PREM-1:
  "P-STAGE2" needed (result.md:181), cannot be dropped (`M_cl`), necessity needs `hgate` (`M_int`); PT stage 1:
  INDEPENDENT (`M_cl` via `D_cl`); "the closedness content is **finite rank of the pair completion**" (A, audited)
- statement (FourCopyHeadline.lean:122): "(hcl : ∀ p, IsClosed (K p))"
- provenance: KT4-PREM-1 Q1-CL, Q2 · depends_on: — · yields: I3.139 · bridge: from one system only through
  `body_isClosed` (I3.104) via P-STAGE2 (I3.145), not at L · bearing: direct constraint on `K` · flag: —

### I3.132 `hgate` — gate preservation (H2 of stage 3 is this clause for `cnot`)
- kind: hypothesis-structure (hypothesis `∀ p, ∀ ω ∈ K p, N p ω ∈ K p` of I3.139) · level: P · status: assumed;
  KT4-PREM-1: "P-ACT2, which restates gate preservation" (result.md:182); cannot be dropped (`M_D`), not necessary
  (`M_max`); PT stage 1 (B, audited): INDEPENDENT, every source found restates it
- statement (FourCopyHeadline.lean:122): "(hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)"
- provenance: KT4-PREM-1 Q1-MAX, Q2 · depends_on: — · yields: I3.139 · bridge: from one system only through
  `preservesBody_inducedEquiv` (I3.105) via P-ACT2 (I3.146), not at L · bearing: direct constraint on `K` · flag: —

### I3.133 `H` — the four-copy core (`KT4Core`, with `KT4`, `KT4LT`)
- kind: hypothesis-structure (data structure, [D]) · level: P (four tokens) · status: not at L — [D]
  FourCopyCore.lean:70–115; as a premise: assumed; KT4-PREM-1: "no statement with three or more tokens"; "under `hadm`,
  `H ⟺ FCC`" (Lemma B1 one way [D], explicit carrier the other) (result.md:180, :119–126)
- statement (FourCopyCore.lean:94–99): "/-- **The core of KT(4) that Lemma B1 reads.** Product states of each grouping in
  one carrier, bilinear product effects with their evaluation laws, positivity of each grouping's product effects on the
  other grouping's product states, and token coherence on the product states of each grouping. Each field is a
  consequence of the corresponding `KT4` fields (`KT4.toCore`); no body, convexity, normalization, combination law or
  local tomography is a field. -/ structure KT4Core (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V]
  [NormedSpace ℝ V] where stA … stB … effA … effB … effA_apply … effB_apply … posBA … posAB … tokA … tokB …"; `KT4`
  (:70–78) "Two COMP-1 pre-composites of the normalized pair bodies, one per grouping, with one body and the four-token
  coherence clause. Local tomography of the four-copy composite is not a field."
- provenance: design module · depends_on: I3.114, I3.134 · yields: I3.139, I3.140 · bridge: n/a · bearing: direct
  (four-token constraint on the four pair cones) · flag: —

### I3.134 token clauses `tokA`, `tokB` (`TokenCoherent`)
- kind: hypothesis-structure (def … : Prop, [D]) · level: P (four tokens) · status: not at L — [D]; as a premise:
  assumed; cannot be dropped (`M_tok`: FCC fails at `−1/8` for `(Q3, Q3, Q3, twin)`), not necessary for given data
  (`M_tokC`); PT stage 1 (C, audited): CONDITIONAL on N2 (`TokProdState`) (INTEGRATION-REVIEW.md:105)
- statement (FourCopyCore.lean:61–69): "/-- **The four-token coherence clause.** On the common body, the product of the
  coordinate effects `(a, b)` on pair `01` and `(c, d)` on pair `23` equals the product of the coordinate effects `(a, c)`
  on pair `02` and `(b, d)` on pair `13`. -/ def TokenCoherent … (PA : PreComposite Ω01 Ω23 V) (PB : PreComposite Ω02
  Ω13 V) : Prop := ∀ a b c d : Fin 4, ∀ ω ∈ PA.Ω, PA.prodEff (tabCoord a b) (tabCoord c d) ω = PB.prodEff (tabCoord a c)
  (tabCoord b d) ω" · provenance: design module; KT4-PREM-1 Q1-MAP · depends_on: I3.114 · yields: I3.133
- bridge: n/a · bearing: direct (four-token) · flag: —

### I3.135 FCC — the cone-level four-copy interface (`FourCopyCoherent`, `FCC`)
- kind: hypothesis-structure (structure … : Prop, [D]) · level: P (four tokens) · status: not at L — [D]; PT stage 1:
  CONDITIONAL on N0 ∧ N1 ∧ N2 (regrouping invariance, equal strength); stage 2: CONDITIONAL on SDC (I3.157); INDEPENDENT
  of L (`M_tok`, uniform `K_gen`, uniform `K_gen*`); stage 3: "uniform pair self-duality … ⇒ FCC … refuted exactly"
- statement (FourCopyDefs.lean:53–60): "/-- The cone-level four-copy interface. `famI`: products of states across `01|23`
  against products of effects across `02|13`; `famII`: products of states across `02|13` against products of effects
  across `01|23`. The effect factors range over the full Euclidean dual cones. -/ structure FourCopyCoherent (K01 K23
  K02 K13 : Set (W 3)) : Prop where famI : ∀ X ∈ K01, ∀ Y ∈ K23, ∀ E ∈ dualW K02, ∀ F ∈ dualW K13, 0 ≤ ipW X (tabMul
  (tabMul E Y) (tabT F)) · famII : ∀ L ∈ K02, ∀ L' ∈ K13, ∀ e ∈ dualW K01, ∀ f ∈ dualW K23, 0 ≤ ipW e (tabMul (tabMul L
  f) (tabT L'))"; `FCC` (FourCopyCore.lean:176–177) "abbrev FCC (K : Pr → Set (W 3)) : Prop := FourCopyCoherent (K .p01)
  (K .p23) (K .p02) (K .p13)"
- provenance: design module · depends_on: I3.143 · yields: I3.139 (through I3.140) · bridge: n/a · bearing: direct
  (four-token constraint; "OVL4 is a four-token principle that no pair cone decides", stage 3) · flag: —

### I3.136 `PairLinked` (Lemma R's interface form)
- kind: hypothesis-structure (structure … : Prop, [D]; theorem-internal auxiliary of Lemma R) · level: P · status: not
  at L — [D] · statement (FourCopyCore.lean:32–37): "/-- The two families read from one target pair `K`, with partner
  `K'` and link pairs `La`, `Lb`. -/ structure PairLinked (K K' La Lb : Set (W 3)) : Prop where upper : … · lower : …"
- provenance: design module (`FourCopyCoherent.target01`) · depends_on: I3.143 · yields: Lemma R · bridge: n/a
- bearing: direct (internal to the four-copy route) · flag: —

### I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`)
- kind: definition-as-hypothesis ([D]) · level: P · status: not at L — [D] FourCopyCore.lean:155–157; conclusion of
  I3.139 (CONDITIONAL on the five premises, [D]); PT stage 1–3: INDEPENDENT of L; fails on every exotic cone of stage 3
- statement (FourCopyCore.lean:155–157): "/-- **IE₁** for one pair cone: invariance under every local rotation of either
  token. -/ def IE1 (K : Set (W 3)) : Prop := ∀ R, IsRot3 R → actC R '' K = K ∧ actT R '' K = K"; "def IsRot3 (R : (Fin
  3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop := LinearMap.toMatrix' R ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ" (:122–124)
- provenance: design module · depends_on: I3.6, I3.7 · yields: I3.139 conclusion · bridge: n/a · bearing: direct
  constraint on `K` (it contains (b_S4) for both tokens; stage 4 S5) · flag: **do not assume** (IE1)

### I3.138 `EvenCycle` (with `EvenCycle4`)
- kind: definition-as-hypothesis ([D]) · level: P (four tokens) · status: not at L — [D]; conclusion of I3.139
- statement (FourCopyDefs.lean:95–98): "/-- The twist parity of the four-cycle `0–1–3–2–0`, pairs in the order `01, 23,
  02, 13`: the number of twisted pairs is even. -/ def EvenCycle4 (τ01 τ23 τ02 τ13 : Bool) : Prop := (τ01.toNat +
  τ23.toNat + τ02.toNat + τ13.toNat) % 2 = 0"; `EvenCycle` (FourCopyCore.lean:179–180)
- provenance: design module · depends_on: — · yields: — · bridge: n/a · bearing: direct (orientation parity) · flag: —

### I3.139 `kt4_forward_ie1` (Theorem A′, the audited theorem)
- kind: theorem ([D]) · level: P (four tokens) · status: not at L — [D] "kernel-checked in a design run, not certified"
  (KT4-PREM-1 result.md:188, :241)
- statement (FourCopyHeadline.lean:118–125): "/-- **Theorem A′ (headline, Pauli-free).** The core of KT(4), admissible
  closed pair cones and N-CLASS gates preserving them give IE₁ for every pair and even orientation parity. -/ theorem
  kt4_forward_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B
  p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p)) (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) {V :
  Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) : (∀ p, IE1 (K p))
  ∧ EvenCycle (fun p => orient (A p) (B p))"
- provenance: design module; KT4-PREM-1 · depends_on: I3.129–I3.133 · yields: IE1 (I3.137) at every pair (the
  conclusion; it is the only route at L or [D] whose conclusion contains (b_S4)) · bridge: n/a · bearing: direct
  constraint on `K` (conditional on four-token data) · flag: conclusion is IE1 (do not assume)

### I3.140 `fourCopyCoherent_of_kt4Core` (Lemma B1)
- kind: theorem ([D]) · level: P · status: not at L — [D]
- statement (FourCopyBridge.lean:267–276): "/-- **Lemma B1 over the consumed core.** The maximal-cone bound and
  nonnegative scaling of each pair cone, with the fields of `KT4Core`, give the four-copy interface. -/ theorem
  fourCopyCoherent_of_kt4Core (m01 : K01 ⊆ maxCone (eball 3)) … (s01 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K01, c • ω ∈ K01) … (H :
  KT4Core K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13"
- provenance: design module · depends_on: I3.133, I3.3 · yields: I3.139, `H ⟺ FCC` (one direction) · bridge: n/a
- bearing: direct · flag: —

### I3.141 `KT4Cone`
- kind: hypothesis-structure (structure … : Prop, [D] preflight) · level: P (four tokens) · status: not at L — [D] in
  FourCopyPackage.lean, a preflight whose theorems are `sorry` ("Every `sorry` here is an open proof obligation")
- statement (FourCopyPackage.lean:82–87): "/-- Cone-level KT(4; 01|23, 02|13). -/ structure KT4Cone (K01 K23 K02 K13 : Set
  (W 3)) (K4 : Set W4) : Prop where prodA_mem : ∀ X ∈ K01, ∀ Y ∈ K23, prodA X Y ∈ K4 · prodB_mem : ∀ L ∈ K02, ∀ L' ∈
  K13, prodB L L' ∈ K4 · effA_nonneg : ∀ e ∈ dualW K01, ∀ f ∈ dualW K23, ∀ Ω ∈ K4, 0 ≤ effA e f Ω · effB_nonneg : ∀ E ∈
  dualW K02, ∀ F ∈ dualW K13, ∀ Ω ∈ K4, 0 ≤ effB E F Ω" · provenance: design preflight (EQ4-F) · depends_on: I3.143
- yields: preflight package (Theorems B–D, `sorry`) · bridge: n/a · bearing: direct (four-token) · flag: —

### I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the drive words, anywhere)
- kind: definition-as-hypothesis and theorem ([D] preflight) · level: P · status: not at L — [D]; `ie1Drive_of_ie1` is
  "Open." with proof `sorry` (FourCopyPackage.lean:291–293)
- statement (FourCopyPackage.lean:278–281): "/-- IE₁ in the drive form: invariance under the local lifts of the landed
  drive words. -/ def IE1Drive (K : Set (W 3)) : Prop := ∀ g ∈ driveWords3, actC (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3
  → ℝ)) '' K = K ∧ actT (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K"; "/-- The drive words are rotations, so
  IE₁ gives the drive form. Open. -/ theorem ie1Drive_of_ie1 {K : Set (W 3)} (h : IE1 K) : IE1Drive K"
- provenance: design preflight; ledger EQ2-SYNTHESIS.md:75 defines IE₁ as "two-copy composite invariant under the
  lifts of `driveWords3`" (research record) · depends_on: I3.83 (`driveWords3`), I3.6, I3.7 · yields: —
- bridge: it is the design-level statement of the O→P lift of `ball3Drive`'s words (flow about the third axis and
  `cyc3`) on both tokens; not at L, and the words are those of the control drive, not of an OI drive
- bearing: direct constraint on `K` (it contains a (b_DJ)-type invariance on both tokens) · flag: **do not assume**
  (IE1 in drive form; (b))

### I3.143 `ipW`, `dualW` (the Euclidean pairing and dual cone of tables)
- kind: definition-as-hypothesis ([D]) · level: P · status: not at L — [D] (FourCopyDefs.lean:30–34); at L no kernel
  declaration defines a dual cone of `W 3` (grep: `dualW`/`ipW` absent from the kernel)
- statement (FourCopyDefs.lean:30–34): "/-- The Euclidean pairing of an effect table with a state table. -/ def ipW (E X :
  W 3) : ℝ := ∑ μ, ∑ ν, E μ ν * X μ ν"; "/-- The Euclidean dual cone: the tables nonnegative on `K`. -/ def dualW (K :
  Set (W 3)) : Set (W 3) := {E | ∀ X ∈ K, 0 ≤ ipW E X}"
- provenance: design module · depends_on: I3.1 · yields: I3.135, I3.141, H3 (I3.149) · bridge: n/a · bearing: direct
  (the pairing in which H3 is stated) · flag: —

### I3.144 `Q3`, `twin`, `pauliW`, `twistQ3`
- kind: definition-as-hypothesis ([D] preflight; comparison objects) · level: P · status: not at L — [D] in the `sorry` preflight
  FourCopyPackage.lean:174–190; in the kernel at L `Q3` occurs only as a question label in DerivedQ3/FlowEndpoint (name
  collision, I4's scope), and the twin enters only as `actT reflY` with `cnot idW = chainW` (K2Guard.lean:110)
- statement (FourCopyPackage.lean:180, :183): "/-- The quantum pair cone. -/ def Q3 : Set (W 3) :=
  {ω | (pauliW ω).PosSemidef}"; "/-- The twin cone `actT reflY '' Q3`. -/ def twin : Set (W 3) := actT reflY '' Q3"
- provenance: design preflight · depends_on: `pauliW` (:175–177) · yields: comparison object of stages 3–5
- bridge: the matrix-level PSD self-duality cited for `Q3 = dualW Q3` (PROTOCOL-STAGE3.md:66: JordanClassification.lean:84
  `psd_iff_trace_nonneg`; OperationalRigidity.lean:917) is at level M (thread I4); no kernel map from `Matrix (Fin 2 ×
  Fin 2) (Fin 2 × Fin 2) ℂ` to `W 3` exists at L (`pauliW` is [D]) · bearing: direct (comparison object only)
- flag: **do not assume** (`Q3`/PSD/pure-state reachability)

### I3.145 P-STAGE2 (named premise of KT4-PREM-1)
- kind: hypothesis-structure (named premise, prose) · level: P · status: assumed (named premise of the landed KT4-PREM-1 record; a premise `D` does not state) — "a pair-level route
  therefore needs two premises that `D` does not state" (KT4-PREM-1 result.md:162)
- statement (KT4-PREM-1 result.md:164–166): "**P-STAGE2** — the pair system as a directed system whose completion has a
  chart onto `W 3` with chart body the normalized slice of `K_p`. It gives `hcl` through `body_isClosed`. It presupposes
  the pair's local tomography, which `W 3` encodes, and so the open composite obligation K2."
- provenance: KT4-PREM-1 Q2 · depends_on: I3.92, I3.104, I3.1 · yields: I3.131 · bridge: it is itself the missing O→P
  bridge for closedness (stage completion of one system → pair cone) · bearing: direct constraint on `K` if granted
- flag: — (PT stage 1: "assuming either for the premise it delivers is a restatement", PROTOCOL.md:57–61)

### I3.146 P-ACT2 (named premise of KT4-PREM-1)
- kind: hypothesis-structure (named premise, prose) · level: P · status: assumed (named premise of the landed KT4-PREM-1 record; a premise `D` does not state) (KT4-PREM-1 result.md:162)
- statement (KT4-PREM-1 result.md:167–172): "**P-ACT2** — the gate `N_p` as an operation datum on that system with an
  inverse datum, inducing `N_p` on the chart. It gives `hgate` through `preservesBody_inducedEquiv`. An operation datum
  carries each preparation into the completed body (`OpDatum.mem_body`), so P-ACT2 states gate preservation on
  preparations; it does not derive it. Idle extension does not supply P-ACT2's datum: for local rotations, idle extension
  of one-copy data to the pair cone is IE1 itself, and for `reflY` it fails on every `cnot`-invariant candidate cone
  (`no_candidateCone_cnot_reflY`)."
- provenance: KT4-PREM-1 Q2 · depends_on: I3.99, I3.105, I3.145 · yields: I3.132 · bridge: it is the missing O→P bridge
  for operations; its idle-extension form for rotations is IE1 · bearing: direct constraint on `K` if granted
- flag: the idle-extension reading is IE1 (do not assume)

## §I — the pair premises as the PT stage records fix them (H1–H3, the (b) forms, the stage-1/2 principles)

### I3.147 H1 — products in `K`
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: assumed (hypothesis of Q-SD, Q-EX, Q-EX-BRIDGE);
  "the certified product datum; hadm (a)" (PROTOCOL-STAGE3.md:45); relative to L: INDEPENDENT (`M_class`;
  INTEGRATION-REVIEW.md:98); at L only `prodState_mem_maxCone` (I3.42), which puts products in `maxCone`, not in `K`
- statement (PROTOCOL-STAGE3.md:45): "**(H1)** `prodState x y ∈ K` for all `x, y ∈ eball 3` (the certified product
  datum; hadm (a));"
- provenance: PT stage 3 protocol · depends_on: I3.2 · yields: Q-SD, Q-EX · bridge: n/a · bearing: direct constraint on
  `K` · flag: —

### I3.148 H2 — `cnot`-invariance (level (i)); `G16`-invariance (level (ii))
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: assumed; "the certified native gate; hgate —
  hinv follows, `cnot` being an involution" (PROTOCOL-STAGE3.md:46); relative to L: `hgate` INDEPENDENT (`M_max`,
  `M_D13`; INTEGRATION-REVIEW.md:102); level (ii) = invariance under S2's even class (order 16) (PROTOCOL-STAGE3.md:51–52)
- statement (PROTOCOL-STAGE3.md:46): "**(H2)** `cnot ω ∈ K` for all `ω ∈ K` (the certified native gate; hgate — hinv
  follows, `cnot` being an involution);"
- provenance: PT stage 3 protocol · depends_on: I3.11, I3.13 · yields: Q-SD · bridge: n/a · bearing: direct · flag: —

### I3.149 H3 — trace self-duality `K = dualW K`
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: assumed, unsourced at L — the dual cone `dualW`
  exists only in a design module (I3.143); stage 3: H1–H3 do not force `K = Q3` (EXOTIC at levels (i) and (ii),
  INTEGRATION-NOTE-STAGE3.md:11–14); stage 4: "K = Q3" is "CONDITIONAL on the composite action (b) and on trace
  self-duality H3" (INTEGRATION-NOTE-STAGE4.md:18); stage 2: CSD2 ("every pair effect is a pair state") is a conjunct of
  SDC with observer-native source UNRESOLVED (INTEGRATION-ADDENDUM-STAGE2.md:45–51, :76)
- statement (PROTOCOL-STAGE3.md:47): "**(H3)** `K = dualW K` (self-duality for `ipW`)."
- provenance: PT stage 3 protocol · depends_on: I3.143 · yields: Q-SD, Q-EX, Q-EX-BRIDGE · bridge: none at L from the
  single-ball self-duality (the Lorentz effect cone, I3.124, I3.127) to the pair; no kernel theorem relates `maxCone` to
  its own dual · bearing: direct constraint on `K` · flag: —

### I3.150 (b_S4) — the full rotation group of one token acts on the pair preserving `K`
- kind: hypothesis-structure (PT-record; the target principle) · level: P · status: PT-record: open — "INDEPENDENT of
  H1–H3 plus the certified pair structure at L" (PROTOCOL-STAGE5.md:17–20; INTEGRATION-NOTE-STAGE4.md:20, :118–123);
  sufficient for `K = Q3` given H1–H3 (stage 4, [W + X], audited)
- statement (PROTOCOL-STAGE5.md:19): "**(b_S4)** the full rotation group of one token acts on the pair preserving `K`
  (`actC SO(3)` or `actT SO(3)`);"
- provenance: PT stages 4–5 · depends_on: I3.6/I3.7, I3.80 (the body symmetry, single token) · yields: `K = Q3` (stage
  4) · bridge: none at L (I3.66, I3.80) · bearing: direct (it is a (b_min) form) · flag: **do not assume** ((b))

### I3.151 (b_n) — one rotation subgroup of one token about an off-frame axis
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: open; stage 4 record S3[n]: "UNIQUE iff n is off
  the native frame's coordinate axes (level (ii))" (INTEGRATION-NOTE-STAGE4.md:40)
- statement (PROTOCOL-STAGE5.md:20): "**(b_n)** one rotation subgroup of one token about an axis `n` off the native
  frame's coordinate axes;"
- provenance: PT stages 4–5 · depends_on: as I3.150 · yields: `K = Q3` (stage 4) · bridge: none at L · bearing: direct
- flag: **do not assume** ((b))

### I3.152 (b_R1) — one order-3 rotation of one token about (5,1,1)
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: open; stage 4 record R1: "UNIQUE [W + X]; its
  only proper sub-extension (cnot alone) EXOTIC-X" (INTEGRATION-NOTE-STAGE4.md:42)
- statement (PROTOCOL-STAGE5.md:21): "**(b_R1)** one order-3 rotation of one token about (5,1,1);"
- provenance: PT stages 4–5 · depends_on: as I3.150 · yields: `K = Q3` · bridge: none at L · bearing: direct
- flag: **do not assume** ((b))

### I3.153 (b_DJ) — the native drive with the native `J` acting on one token
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: open; stage 4: "The drive the corpus attaches to
  the NOT (`nflip`, axis x; corner axis `z3`) lies exactly on the exceptional set: its idle extension does not force
  `Q3`. Idle extension of the drive together with its off-axis conjugate (`J_off_axis` of `ElementaryDrivability`,
  KInfFoundations.lean:264, 276) contains S4 and does." (INTEGRATION-NOTE-STAGE4.md:113–116)
- statement (PROTOCOL-STAGE5.md:22–25): "**(b_DJ)** the native drive (the flow through the NOT, on the NOT axis) together
  with the native `J` (`cyc3`, `KInfFoundations.lean:449`), both acting on one token of the pair preserving `K` — to be
  fixed exactly in the coordinator's pre-audit: the Lie closure of the flow and its `J`-conjugate, with `cnot`, is the
  full `su(2) ⊕ su(2)`."
- provenance: PT stage 5 · depends_on: I3.66, I3.67, I3.6/I3.7 · yields: `K = Q3` (stage 4/5 records) · bridge: none at L
  (I3.66: no kernel statement applies `actC`/`actT` to a flow member or to `cyc3`; the drive "through the NOT, on the NOT
  axis" is a PT construction; `ball3Drive`'s flow is about the third axis) · bearing: direct · flag: **do not assume**

### I3.154 IE2 — idle extension of the pair interaction groups
- kind: hypothesis-structure (PT-record / research record) · level: P (three or more tokens) · status: PT-record: open
  ("IE₂ open", INTEGRATION-REVIEW.md:187, :211); forbidden as a premise (PROTOCOL.md:82; PROTOCOL-STAGE3.md:133)
- statement (ledger EQ2-SYNTHESIS.md:76, research record): "**IE₂**: idle extension of the pair interaction groups, tree
  closure form"; ISP (:85) "native inert-spectator compositionality … one principle with IE₁ and IE₂ as instances"
- provenance: research ledgers (pt/inputs/ledgers), PT stage 1 · depends_on: — · yields: — · bridge: none at L
- bearing: direct constraint on multi-token composites (none at L) · flag: **do not assume** (IE2)

### I3.155 frame covariance (FC) of the native gate
- kind: hypothesis-structure (PT-record) · level: P · status: PT-record: flagged; "FC ⟺ IE1 given hgate, with exact
  words confirmed" (INTEGRATION-ADDENDUM-STAGE2.md:124); candidate μ "fails the disguise test by record"
  (PROTOCOL-STAGE5.md:95)
- statement (INTEGRATION-ADDENDUM-STAGE2.md:123–124): "**What reaches Q3 among the routes examined:** - local agency or
  frame covariance. Both are flagged; FC ⟺ IE1 given hgate, with exact words confirmed;"
- provenance: PT stage 2 (S2, audited) · depends_on: I3.148 · yields: IE1 (with hgate) · bridge: none at L
- bearing: direct · flag: **do not assume** (frame covariance)

### I3.156 INV2 — the native gate is an operational involution on the pair system
- kind: hypothesis-structure (PT-record, named principle) · level: P · status: PT-record: "INV2 and SDC are named
  principles, not results. Their observer-native sources are open." (INTEGRATION-ADDENDUM-STAGE2.md:290)
- statement (INTEGRATION-ADDENDUM-STAGE2.md:38): "Its finite rank and local tomography are CONDITIONAL on one principle,
  INV2: the native gate is an operational involution on the pair system."
- provenance: PT stage 2 (S2) · depends_on: — · yields: "INV2 ⇒ LT for data-generated systems" (:107); "INV2, or a
  finite operation group, ⇒ finite rank" (:108) · bridge: none at L (no pair system at L) · bearing: direct (LT and
  finite rank of a data-generated pair completion) · flag: —

### I3.157 SDC = P3 ∧ OVL4 ∧ CSD2 — self-duality under composition
- kind: hypothesis-structure (PT-record, named principle) · level: P (four tokens) · status: PT-record: FCC is
  CONDITIONAL on SDC; "Its observer-native source is **UNRESOLVED**" (INTEGRATION-ADDENDUM-STAGE2.md:45–51); stage 3:
  "The four-token route (S3's SDC: P3 ∧ OVL4 ∧ CSD2) is untouched" (INTEGRATION-NOTE-STAGE3.md:58–60)
- statement (INTEGRATION-ADDENDUM-STAGE2.md:73–76): "**Strongest result.** FCC is CONDITIONAL on SDC … - P3: both
  groupings' independent preparations are states of one four-token system. - OVL4: four-token states overlap
  nonnegatively for the composed pairing. - CSD2: every pair effect is a pair state."
- provenance: PT stage 2 (S3) · depends_on: I3.143 · yields: FCC (I3.135) · bridge: none at L · bearing: direct
  (four-token) · flag: —

### I3.158 N0 ∧ N1 ∧ N2 — regrouping invariance of a four-token composite (stage-1 principle S3)
- kind: hypothesis-structure (PT-record, named principle) · level: P (four tokens) · status: PT-record: "independently
  motivated equivalent. L has no structure with three or more tokens: UNRESOLVED whether the framework supplies it"
  (INTEGRATION-REVIEW.md:143)
- statement (INTEGRATION-REVIEW.md:143): "**S3 Four tokens** | the four tokens compose into one regrouping-invariant system
  (N0 ∧ N1 ∧ N2) | FCC ⟺ H |"
- provenance: PT stage 1 (C, audited) · depends_on: I3.114 · yields: FCC, token clauses · bridge: none at L
- bearing: direct (four-token) · flag: —

### I3.159 S2 Pair — a compact, gate-reversible COMP-1 pre-composite (stage-1 principle)
- kind: hypothesis-structure (PT-record, named principle) · level: P · status: PT-record: "restating sources only. The
  non-restating route would be an OI-native pair system (not defined at L) with FiniteRank (K∞-Stage) and reversible
  operation data (K∞-Act): UNRESOLVED" (INTEGRATION-REVIEW.md:142)
- statement (INTEGRATION-REVIEW.md:142): "**S2 Pair** | the normalized slice of `K_p` is the body of a **compact** COMP-1
  pre-composite of two balls on the table carrier, and the native gate **preserves** it in both directions | `hadm ∧
  hcl ∧ hgate` …"
- provenance: PT stage 1 integration · depends_on: I3.114, I3.13 · yields: `hadm ∧ hcl ∧ hgate` · bridge: none at L
- bearing: direct constraint on `K` · flag: —

### I3.160 H — pair-level homogeneity of `K`
- kind: hypothesis-structure (PT-record, candidate) · level: P · status: PT-record: "UNIQUE [W + X + K + L]; CONDITIONAL
  on H and on Koecher–Vinberg + Jordan–von Neumann–Wigner [L]; minimality UNRESOLVED" (INTEGRATION-NOTE-STAGE4.md:35); "H
  is not the pair analogue of TRB-1's premise and T is" (:85–86)
- statement (PROTOCOL-STAGE4.md:59): "**H** homogeneity of `K` (stage 3: only `Q3` among symmetric cones [W + L]; …"
- provenance: PT stages 3–4 · depends_on: — · yields: `K = Q3` (conditional) · bridge: none at L · bearing: direct
- flag: — (not a do-not-assume item by the stage-6 list; it is a structural candidate, recorded at its status)

### I3.161 T — pair-level reversible richness (transitivity on extreme rays)
- kind: hypothesis-structure (PT-record, candidate) · level: P · status: PT-record: "EXCLUDES-KNOWN (invariant c = 15 on
  defects, 9 on products); EXCLUDES-ALL UNRESOLVED" (INTEGRATION-NOTE-STAGE4.md:36)
- statement (PROTOCOL-STAGE4.md:62–63): "**T** pair-level reversible richness: the group of reversible pair
  transformations preserving `K` acts transitively on the normalized extreme rays of `K`."
- provenance: PT stage 4 · depends_on: — · yields: — · bridge: its single-system analogue is K∞-Trans (I3.76); no
  bridge at L · bearing: direct · flag: — (OI⁺ "reversible richness" is on the stage-6 do-not-assume list as an OI⁺
  completion condition; T is the PT stage-4 pair-cone node, recorded separately)

## §J — the ROADMAP obligations of the K row (`ROADMAP.md`, with `audits/foundations/kinf-seams-audit.md`)

Status source: `ROADMAP.md` at L; the seams audit (`pt/base/verification/audits/foundations/kinf-seams-audit.md:33–42`)
records each K∞ obligation with its kernel object and "sourced: no". Level O for K∞ items, P for K1/K2.

### I3.162 P1 — K: pre-quantum kinematics (the umbrella row)
- kind: obligation (ROADMAP) · level: O (the field-neutral programme; its parts span O, P and, for K3, M) · status: open (ROADMAP.md:68 "**OPEN** — K3 **CONDITIONAL** …;
  K1 **CONDITIONAL** …; K2 **OPEN** (read-only research, no governed round); K∞ **OPEN** — eight unsourced obligations …;
  Kₙ **OPEN** …")
- statement (ROADMAP.md:68, opening): "| **P1** | K — pre-quantum kinematics: from field-neutral operational premises to
  the complex matrix kinematics the finite characterization assumes | OI→QM / Reconstruction | **OPEN** — …"
- provenance: ROADMAP.md:68 · depends_on: I3.164–I3.179 · yields: "complex quantum kinematics in the conclusion rather
  than the premises" · bridge: n/a · bearing: none at L as a constraint (it is an obligation) · flag: —

### I3.163 K section framing
- kind: obligation (ROADMAP) · level: O (framing of the K row; spans O, P, M) · status: open
- statement (ROADMAP.md:973–976): "The finite operational characterization (`oiPlus_iff_qm`, `typed_determined_iff`) is
  stated over complex matrix carriers, so the quantum kinematics is in its premises. This row tracks the obligation to
  reach that kinematics from field-neutral operational premises, or to isolate the minimal premises from which it
  follows. It has five parts, each with its own status."
- provenance: ROADMAP.md:971–976 · depends_on: — · yields: I3.164–I3.179 · bridge: n/a · bearing: none at L · flag: —

### I3.164 K1 — the dimension
- kind: obligation (ROADMAP) · level: P · status: conditional (ROADMAP.md:984 "**K1 — the dimension. CONDITIONAL.**";
  "`0 < d`, effect soundness, the four K∞ hypotheses, `IsNot` and the relative native-gate and entangling hypotheses
  are, all unsourced", :995–996)
- statement (ROADMAP.md:984–987): "In the DIM-1 coordinate realization of two identical `d`-balls on the locally
  tomographic bilinear carrier `W d`, one common `IsNot` involution and a `NativeGate` satisfying its frame, two-sided
  positivity on `maxCone` and two NOT relations imply `d ∈ {1, 3}` (`dim_of_nativeGate`); adding `Entangling` implies
  `d = 3` (`three_of_nativeGate`)." (continues to :1000: "Dropping the control-NOT relation, or allowing different NOTs
  on the two copies, admits `d = 5` countermodels.")
- provenance: ROADMAP.md:984–1000 · depends_on: I3.18, I3.19, I3.37, I3.38, I3.8, I3.35, I3.36, I3.48, I3.73–I3.76
- yields: "`d = 3` (DIM-1)" in the finite route · bridge: n/a · bearing: constrains the single-token structure the pair
  inherits (`d = 3`) · flag: —

### I3.165 K2 — the composite
- kind: obligation (ROADMAP) · level: P · status: open (ROADMAP.md:1001 "**K2 — the composite. OPEN.**")
- statement (ROADMAP.md:1001–1006): "Read-only research has mapped a candidate `d = 3` composition route, but no governed
  round records the classification or the cone theorem. Its obligations include local tomography, which DIM-1's carrier
  `W d` encodes as a premise, the composite cone, local actions compatible with it, the formal composition theorem, the
  antiunitary and complete-positivity bridge, and the relation to the K3 machinery; all are open. K2 does not discharge
  H-Bell."
- provenance: ROADMAP.md:1001–1006 · depends_on: — · yields: K2 sub-obligations: LT (I3.1, I3.115), the composite cone
  (H1–H3 setting), "local actions compatible with it" (the field-neutral form of (b); PROTOCOL-STAGE5.md:67) · bridge:
  n/a · bearing: direct constraint on `K` (as an open obligation) · flag: its "local actions compatible with the
  composite cone" clause is (b) (do not assume)

### I3.166 K∞ — the field-neutral premises
- kind: obligation (ROADMAP) · level: O · status: open (ROADMAP.md:1007 "**K∞ — the field-neutral premises. OPEN.**"; "All
  are unsourced", :1009)
- statement (ROADMAP.md:1007–1009): "The obligations are seams of the present route to the elementary ball, each carried
  by a named kernel object; they are not claimed to be independent, and later theorems may discharge several together.
  All are unsourced."
- provenance: ROADMAP.md:1007–1009; seams audit §3 · depends_on: — · yields: I3.167–I3.174 · bridge: to the pair only
  through EFF-1's cone equality (I3.51) for Trans/Seed/V4; none for Stage, Act, Drive, Copy, Geom · bearing: constrains
  the single-token structure the pair inherits · flag: —

### I3.167 K∞-Stage
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:35 "no; CMP-1 states each as a named
  proposition and proves it for no OI construction")
- statement (ROADMAP.md:1010–1013): "**K∞-Stage** — stage consistency, the elementary scope and finite rank: `SCInf`,
  `BinaryVisible` and `FiniteRank`. Finite rank gives the completion chart that TRB-1 normalizes
  (`exists_completionChart`). A predicate for the full elementary-visible scope is not yet formalized."
- provenance: ROADMAP.md:1010–1013 · depends_on: I3.94, I3.95, I3.96 · yields: finite-dimensional completed body
- bridge: none at L (no pair completion; P-STAGE2, I3.145) · bearing: constrains the single-token structure · flag: —

### I3.168 K∞-Act
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:36 "no; OPACT-1 sources no operation")
- statement (ROADMAP.md:1014–1016): "**K∞-Act** — reversible operation data on the completed body: an `OpDatum` with
  `AffineRespect` and an inverse datum, which induce body-preserving affine equivalences (`preservesBody_inducedEquiv`)."
- provenance: ROADMAP.md:1014–1016 · depends_on: I3.99, I3.101, I3.102, I3.105 · yields: reversible affine actions on
  the body · bridge: none at L (P-ACT2, I3.146) · bearing: constrains the single-token structure; PT stage 4: "(a), 'an
  isolated token admits all rotations', is a body symmetry at L whose operational availability is itself unsourced
  (K∞-Act, K∞-Drive, K∞-Trans OPEN), and (a) does not give (b)" (INTEGRATION-NOTE-STAGE4.md:20) · flag: —

### I3.169 K∞-Drive
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:37 "no")
- statement (ROADMAP.md:1017): "**K∞-Drive** — field-neutral drivability, `ElementaryDrivability`."
- provenance: ROADMAP.md:1017; seams audit §1–§2 · depends_on: I3.66 · yields: `preservesBody_drive`,
  `preservesBody_driveWords` (body preservation only) · bridge: none at L (I3.66) · bearing: constrains the
  single-token structure only; the (b_DJ) form of (b_min) is its idle extension (not at L) · flag: —

### I3.170 K∞-Trans
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:38 "no; not implied by K∞-Drive (§2)")
- statement (ROADMAP.md:1018–1022): "**K∞-Trans** — all-boundary transitivity, `BoundaryTransitive`, which TRB-1 consumes
  for the ball (`exists_affine_image_eq_eball`) and OG-1 for the sharp family (`seedOrbit_ball3_eq`). K∞-Drive does not
  give it: a drive's flow preserves the ball and a sharp seed and is not boundary transitive
  (`not_boundaryTransitive_flow`), and no theorem derives transitivity from `ElementaryDrivability` on a general body."
- provenance: ROADMAP.md:1018–1022 · depends_on: I3.76 · yields: I3.88–I3.89, I3.79, I3.51 · bridge: through I3.51 to
  `maxCone` · bearing: constrains the composite only through I3.51 · flag: —

### I3.171 K∞-Seed
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:39 "no")
- statement (ROADMAP.md:1023–1024): "**K∞-Seed** — a sharp seed, `SharpSeed`; on the completion it follows from SC∞ and a
  stage effect with values one and zero at two stage preparations (`sharpSeed_completion`)."
- provenance: ROADMAP.md:1023–1024 · depends_on: I3.73, I3.97 · yields: I3.51, I3.79 · bridge: through I3.51
- bearing: constrains the composite only through I3.51 · flag: —

### I3.172 K∞-V4
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:40 "no; body preservation of a transport
  does not make the transported effect available")
- statement (ROADMAP.md:1025–1026): "**K∞-V4** — seed-orbit availability, `SeedOrbitAvailable` (V4′): every transport of
  the seed along the orbit is available. Body preservation of a transport does not supply it."
- provenance: ROADMAP.md:1025–1026 · depends_on: I3.75 · yields: I3.51 · bridge: through I3.51 · bearing: constrains the
  composite only through I3.51 · flag: —

### I3.173 K∞-Copy
- kind: obligation (ROADMAP) · level: O (two copies) · status: open, unsourced (seams audit:41 "the one `N` of DIM-1's
  `IsNot` and `NativeGate`, used on both copies … no")
- statement (ROADMAP.md:1027–1030): "**K∞-Copy** — identical-copy covariance, or copy naturality: identical copies' NOTs
  agree. An untested candidate weakening is that the frame-preserving conjugacy class of the native inversion is
  determined by system type rather than by token; if the planned exact probe confirms it, the obligation becomes type
  covariance of native inversion."
- provenance: ROADMAP.md:1027–1030 · depends_on: I3.69, I3.8 · yields: the common `N` of `NativeGate` · bridge: none at
  L as a theorem; DIM-1 builds the common NOT into `NativeGate` · bearing: constrains the single-token structure the pair
  inherits · flag: —

### I3.174 K∞-Geom
- kind: obligation (ROADMAP) · level: O · status: open, unsourced (seams audit:42 "no; elementary-scoped")
- statement (ROADMAP.md:1031–1033): "**K∞-Geom** — a sharp-update or singleton-face principle: the certain outcome of a
  proper sharp binary test identifies one state. A corrected statement, excluding the unit effect, is planned for a
  successor foundations round and is not frozen."
- provenance: ROADMAP.md:1031–1033 · depends_on: I3.62, I3.63 · yields: KINF-2 geometric route · bridge: none at L
- bearing: none at L on `K` · flag: —

### I3.175 the K∞-R label note
- kind: obligation (ROADMAP, bookkeeping) · level: O · status: open (no status change; records an ambiguity)
- statement (ROADMAP.md:1035–1038): "The label K∞-R is ambiguous in the landed records: `OrbitGeneration` and OG-1's
  record use it for `BoundaryTransitive`. The queue uses K∞-Drive and K∞-Trans. The obligations, their kernel objects
  and the negative result for the flow are recorded in [`audits/foundations/kinf-seams-audit.md`] …"
- provenance: ROADMAP.md:1035–1038; seams audit §1 · depends_on: I3.76, I3.66 · yields: — · bridge: n/a · bearing: none
  at L · flag: —

### I3.176 the geometric obligation is not committed to singleton faces
- kind: obligation (ROADMAP) · level: O · status: open ("No such alternative is presently sourced")
- statement (ROADMAP.md:1040–1043): "The geometric obligation is not committed uniquely to singleton faces: a successor
  foundations round may express the needed geometric input through corrected sharp-face structure or through a stronger
  independently sourced alternative such as self-duality. No such alternative is presently sourced."
- provenance: ROADMAP.md:1040–1043 · depends_on: I3.174 · yields: — · bridge: none at L (the self-duality named here is
  single-system; the pair-level H3, I3.149, is a different statement) · bearing: none at L · flag: —

### I3.177 the geometric branch is elementary-scoped
- kind: obligation (ROADMAP) · level: O · status: open (scope requirement; "requires a field-neutral predicate for an
  elementary system")
- statement (ROADMAP.md:1045–1051): "The geometric branch is scoped to an elementary system. The singleton-face principle,
  relative strict convexity (`RelStrictConvex`) and the ball they yield hold for the qubit and fail for complex quantum
  systems of level three or more: on the qutrit with every effect available, `P = diag(1, 1, 0)` is a proper effect
  certain on the two distinct states `|0⟩⟨0|` and `|1⟩⟨1|`, whose midpoint is a boundary state. They are therefore not
  requirements of finite quantum theory in general. The successor foundations work must formalize that scope, which
  requires a field-neutral predicate for an elementary system."
- provenance: ROADMAP.md:1045–1051 · depends_on: I3.62, I3.63 · yields: Kₙ separation (I3.179) · bridge: n/a
- bearing: none at L on `K` · flag: —

### I3.178 matrix-level drivability, the region limit, and continuous NOTs
- kind: obligation (ROADMAP) · level: O (with a matrix-level comparison, M) · status: open ("Whether a field-neutral analogue of that implication holds is
  open")
- statement (ROADMAP.md:1053–1057): "At the matrix level, drivability already yields sharp effects, through the K3 chain
  above, so sharp effects are not an independent premise there. Whether a field-neutral analogue of that implication
  holds is open. The region limit does not refine a fixed subsystem's effects: region inclusion is `X ↦ X ⊗ 1`
  (`inclObs`). Continuous interpolability of the NOT does not imply copy naturality: a `d = 7` two-NOT countermodel with
  both NOTs continuously interpolable survives."
- provenance: ROADMAP.md:1053–1057 · depends_on: I3.66, I3.73, I3.69 · yields: — · bridge: the matrix-level drivability
  (`DrivesElementary`, SubstratumSource.lean:77) is a different object, I4's scope; no kernel map to
  `ElementaryDrivability` (`kimports.out`) · bearing: none at L on `K` · flag: —

### I3.179 Kₙ — the elementary-to-arbitrary-carrier lift
- kind: obligation (ROADMAP) · level: O (a lift from the elementary O/P objects to the matrix carriers M) · status: open (ROADMAP.md:1058 "**Kₙ — elementary-to-arbitrary-carrier lift.
  OPEN.**"; classification in `audits/foundations/kn-elementary-carrier-census.md`, thread I4's scope)
- statement (ROADMAP.md:1058–1064): "DIM-1 reaches only the elementary `d = 3` ball, while the K3 interfaces quantify over
  every finite carrier: … Kₙ therefore lifts the operational architecture, not only the state and effect spaces. No
  current theorem supplies the lift. No theorem consumes the DIM-1 ball, and K2's candidate route composes elementary
  systems only."
- provenance: ROADMAP.md:1058–1069 · depends_on: I3.164, I3.165 · yields: — · bridge: none at L ("No theorem consumes the
  DIM-1 ball"; confirmed by `kimports.out`: no module outside the K cluster imports `CompositeDimension`) · bearing: none
  at L on the pair cone · flag: —

### I3.180 KINF-1 halted
- kind: obligation (ROADMAP, record) · level: O · status: refuted (by the KINF-1 halt record: the frozen vocabulary
  "mishandled the unit effect"; "no foundations vocabulary from that round is authoritative") — not a premise
- statement (ROADMAP.md:1071–1073): "**KINF-1** halted under `S12` before the Lean foundations module was introduced:
  owner review found that the frozen supporting-effect and singleton-face vocabulary mishandled the unit effect. Its
  execution was withdrawn, and no foundations vocabulary from that round is authoritative."
- provenance: ROADMAP.md:1071–1073; KINF-1 result ("none of the two frozen labels") · depends_on: — · yields: KINF-2
  vocabulary (I3.59–I3.62) · bridge: n/a · bearing: none at L · flag: —

### I3.181 the research direction (unproved)
- kind: obligation (ROADMAP) · level: O · status: open ("A research direction, unproved")
- statement (ROADMAP.md:1075–1079): "**A research direction, unproved.** K∞-Geom, K∞-Drive and K∞-Copy may be sourced by
  a theory of the physical observation interaction, in which sharp outcomes carry a sourced update rule, observational
  contexts admit continuous reversible transport, and the type of native inversion is invariant across identical system
  tokens. These are three separate candidates, not one principle; only the third has so far produced a candidate
  reduction of an existing premise."
- provenance: ROADMAP.md:1075–1079 · depends_on: I3.174, I3.169, I3.173 · yields: — · bridge: none at L · bearing: none
  at L · flag: —

### I3.182 the finite route
- kind: obligation (ROADMAP) · level: O (the route runs O → P → M) · status: open (the order of consumption; every arrow conditional on its
  unsourced inputs)
- statement (ROADMAP.md:1081–1093): "**The finite route.** The order in which the present route consumes these
  obligations: · K∞-Stage (stage consistency, elementary scope, finite rank) → finite-dimensional completed body · K∞-Act
  → reversible affine actions on the body · K∞-Drive, K∞-Trans, K∞-Seed, K∞-V4 → the elementary ball and its sharp family
  → the effect cone of the ball (EFF-1) · K2 (local tomography, the composite cone) · K∞-Copy, the native gate (frame,
  NOT relations, two-sided positivity, entangling) → d = 3 (DIM-1) · Kₙ (the operational architecture at every finite
  carrier) · K3 → finite operational quantum theory" (line breaks of the code block rendered as ·)
- provenance: ROADMAP.md:1081–1093; seams audit §4 (which lists K2 as "(local tomography, the composite cone, compatible
  local actions)", kinf-seams-audit.md:54) · depends_on: I3.164–I3.179 · yields: — · bridge: the route has no arrow from
  any K∞ item to the composite cone `K` other than through K2, which is open · bearing: none at L as a constraint
- flag: —

### I3.183 orthogonality to P0
- kind: obligation (ROADMAP) · level: O (row framing) · status: open
- statement (ROADMAP.md:1095–1096): "This row is orthogonal to `P0`: a complete operational reconstruction would not by
  itself select a unique quantum history."
- provenance: ROADMAP.md:1095–1096 · depends_on: — · yields: — · bridge: n/a · bearing: none at L · flag: —

## §K — manuscript statement of the reconstruction route (papers at L)

### I3.184 the operational-reconstruction route: reconstruction axioms as hypotheses of a continuum endpoint
- kind: manuscript-principle · level: X (manuscript statement about operational reconstructions; M-level theories) · status:
  conditional — the manuscript states the route as "a classification conditional on the five completion conditions, not
  an independent derivation" (Main.md:352)
- statement (Main.md:352, the sentences in I3's scope): "**Operational-reconstruction route: target conditions and the
  outstanding bridge.** The reconstruction theorems [Hardy …; Masanes and Müller …; Chiribella, D'Ariano and Perinotti
  …] derive quantum theory from operational axiom sets. … The purification, continuous-transitivity, and
  tomographic-locality axioms of the cited reconstructions are hypotheses of their continuum endpoint, which the
  classical-dimension obstruction places beyond any fixed finite carrier; they are not what the finite characterization
  uses."
- provenance: papers/Main.md:352 · depends_on: — · yields: — · bridge: none at L from these axioms to the K-programme
  objects; the field-neutral analogues at L are K∞-Trans (I3.76; continuous transitivity) and LT encoded by `W d` (I3.1;
  tomographic locality) · bearing: none at L as a constraint on `K` (the rest of the paragraph — the five completion
  conditions — is thread I2's manuscript scope and thread I4's kernel scope) · flag: the five completion conditions are
  OI⁺ conditions (do not assume; recorded by I2/I4)

## §L — records added after the first pass (ids continue; nothing renumbered)

### I3.185 carrier-map identities for every one-copy linear map: `actT_prodState`, `actT_tens`, `actC_tens`, `toOp_actC`
- kind: lemma-folded (edges of the carrier maps I3.6–I3.7) · level: P (from O data) · status: proved [K]
- statement: "/-- A local linear map of the second copy carries a product state to a product state. -/ theorem
  actT_prodState (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x y : Fin d → ℝ) : actT N (prodState x y) = prodState x (N y)"
  (K2Guard.lean:172–174); "theorem actT_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y : HVec d) : actT N (tens X Y) =
  tens X (homMap N Y)" (CompositeDimension.lean:1923–1924); "theorem actC_tens (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (X Y :
  HVec d) : actC N (tens X Y) = tens (homMap N X) Y" (:1930–1931); "/-- The control action in operator form: left
  composition with the homogenized NOT. -/ theorem toOp_actC (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) : toOp (actC
  N ω) = homMap N ∘ₗ toOp ω" (:450–452)
- provenance: K2-GUARD-1 (`reflY_mem_productSet`, K2Guard.lean:190); DIM-1 §F, §Q · depends_on: I3.6, I3.7, I3.2
- yields: `productSet` invariant under `actT reflY` (K2Guard.lean:190); with a body-preserving one-copy map, products of
  the ball go to products of the ball
- bridge: the only O→P statements at L about an arbitrary one-copy map acting on the pair carrier; they reach product
  (tensor) vectors only, and no statement at L concerns the image of a non-product vector under `actC g`/`actT g` for
  `g` not an involution (the PT stage-4 note records that `SEP` and `maxCone` satisfy (b) while `K_gen` and the exotic
  cones do not, INTEGRATION-NOTE-STAGE4.md:122–123; a PT record, not a kernel statement) · bearing: direct, on products
  only
- flag: —

### I3.186 `eball_three`
- kind: lemma-folded (edge identifying the K∞ ball with DIM-1's ball) · level: O · status: proved [K]
- statement (TransitiveBody.lean:669–670): "/-- At `d = 3` the coordinate Euclidean ball is `KInfFoundations.ball3`. -/
  theorem eball_three : eball 3 = ball3"
- provenance: TRB-1 corollaries · depends_on: — · yields: the K∞ objects on `ball3` (`ball3Drive`, `fullAut3`,
  `driveWords3`) and the DIM-1/EFF-1 objects on `eball 3` speak about the same set · bridge: an O-level identification of
  bodies, not a transfer to the pair carrier · bearing: constrains the single-token structure the pair inherits (the
  token body of `W 3` is the K∞ ball) · flag: —

### I3.187 the classification step of KT4-PREM-1: `hcls ∧ hadm ∧ hgate ∧ IE1 ⇒ K_p ∈ {Q3, twin}`
- kind: theorem (written argument in a landed round record) · level: P · status: conditional-on IE1, `hcls`, `hadm`,
  `hgate`; "a written argument and it is not yet kernel-checked" (KT4-PREM-1 result.md:142); finite steps exact (probe
  checks C1–C6); one standard Lie-theory input "not checked" (:140–141)
- statement (KT4-PREM-1 result.md:128–129): "**Q1-NEC: CLASSIFICATION-STEPS-VERIFIED.** The written classification: `hcls
  ∧ hadm ∧ hgate ∧ IE1` give `K_p ∈ {Q3, twin}` at every pair, hence `hcl`; `H` is not used."
- provenance: KT4-PREM-1 Q1-NEC; non-inference rule (:241–243: "the classification of a pair cone as Q3 or its twin
  holds relative to N-CLASS gates, admissible cones, gate preservation and IE1, none of which is sourced")
- depends_on: I3.129, I3.130, I3.132, I3.137 · yields: `hcl` relative to the others · bridge: n/a · bearing: direct
  constraint on `K` (conditional on IE1) · flag: uses IE1 (do not assume)
