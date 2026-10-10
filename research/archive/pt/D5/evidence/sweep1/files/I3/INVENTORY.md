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
map argument is always one of: the NOT variable `N` of a hypothesis (`NativeGate`, `GateRel`, `CtrlGate`,
`NativeGateOf`, `not_even_of_relC`), `nflip`, `neg1`, `nC5`, `n5`, `reflY` (grep, NOTES 16:55Z). No kernel declaration
applies `actC`/`actT` to a member of an `ElementaryDrivability` flow, to its `J`, to `cyc3`, or to any rotation.

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
  statements at L: `N` (the NOT of a hypothesis), `nflip`, `neg1`, `nC5`, `n5`, `reflY`. Not applied at L to any flow
  member, `J`/`cyc3`, or rotation; idle-extended local rotations appear only in the [D] predicates `IE1`
  (FourCopyCore.lean:156) and `IE1Drive` (FourCopyPackage.lean:279)
- bearing: direct constraint on `K` or on (b_min): (b_min) in every stage-5 form is a statement "`actC g` or `actT g`
  preserves `K`" for one-token `g`; the map exists at L, the invariance statement for `g` ≠ NOT/`reflY` does not
- flag: the invariance of `K` under `actT g` for a rotation `g` is (b) / IE1-type: do not assume

### I3.7 `actC`
- kind: definition-as-hypothesis (carrier map) · level: P · status: proved [K] (definition)
- statement (CompositeDimension.lean:200–202): "/-- `N` acting on the control index. -/ def actC (N : (Fin d → ℝ) →ₗ[ℝ]
  (Fin d → ℝ)) (ω : W d) : W d := fun μ ν => homMap N (fun κ => ω κ ν) μ"
- provenance, depends_on, yields, bridge, bearing, flag: as I3.6 (control index)

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
- kind: definition (witness data; no hypothesis role of its own) · level: P (`cnot`, `phiW`), O (`z3`, `nflip`,
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
- bridge: n/a · bearing: as I3.18–I3.19 · flag: —

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
- provenance: RELC-SELECT-1 §A · depends_on: I3.9 · yields: I3.31 · bridge: n/a · bearing: — · flag: —

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
- bearing: as I3.37 · flag: —

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
- yields: with I3.45/I3.47, a reading of `2 ≤ d` · bridge: as I3.39 · bearing: as I3.39 · flag: —

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
  gives `d = 3`; where `2 ≤ d` comes from remains open" · bridge: n/a · bearing: as I3.18 · flag: —

### I3.46 `two_le_of_entangling`
- kind: lemma-folded (edge `Entangling → 2 ≤ d` under I3.8, I3.9) · level: P · status: proved [K]; "no converse is
  stated" (K2-GUARD-1)
- statement (K2Guard.lean:240–242): "theorem two_le_of_entangling … (hN : IsNot (eball d) z N) (hG : NativeGate (eball
  d) z N G) (hE : Entangling (eball d) G) : 2 ≤ d" · provenance: K2-GUARD-1 · depends_on: I3.10, I3.17
- yields: I3.45 · bridge: n/a · bearing: — · flag: —

### I3.47 `three_of_nativeGateOf_of_two_le`
- kind: theorem · level: P · status: proved [K]
- statement (K2Guard.lean:253–257): "theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d) (hE : EffectsOn (eball d)
  avail) (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) (hV4 :
  SeedOrbitAvailable G r avail) {z …} {N …} {T : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d)
  avail z N T) : d = 3"
- provenance: K2-GUARD-1 · depends_on: as I3.37 plus `2 ≤ d` · yields: K1 (I3.164) · bridge: through I3.51
- bearing: as I3.37 · flag: —

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
- bridge: n/a · bearing: — · flag: —

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
  structure the pair inherits only through the K∞ route (ROADMAP.md:1084) · flag: —

### I3.58 `IsEffectOn`
- kind: definition-as-hypothesis · level: O · status: proved [K] (definition)
- statement (KInfFoundations.lean:115–117): "/-- An affine functional is an effect on `Ω` when it takes values in `[0,
  1]` on `Ω`. -/ def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop := ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1"
- provenance: KINF-2 · depends_on: — · yields: I3.3, I3.48, I3.73, `PreComposite.prodEff_effect`
- bridge: enters the pair through `maxCone` (I3.3) · bearing: constrains the composite through `maxCone` · flag: —

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
- kind: hypothesis-structure (def … : Prop) · level: O · status: assumed / open (K∞-Geom, ROADMAP.md:1031–1033; "the
  singleton-face principle … fail[s] for complex quantum systems of level three or more", ROADMAP.md:1046–1049)
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
