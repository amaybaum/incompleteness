/-
  FourCopyIE1.lean — EQ4-F design candidate: the formalization package KT(4; 01|23, 02|13) → IE₁.

  UNBUILT. There is no local Lean toolchain; this file has never been elaborated or compiled. Every `sorry`
  marks an open obligation, and the proofs written out are unchecked. Nothing here is adopted, frozen or
  governed. Companion document: FORMAL.md (statements, hypothesis ledger, proof skeleton, Mathlib inventory).

  Base: certified main bcbc516f (read-only snapshot). Base names used, with the line of the declaration, read at
  the base (paths under verification/lean-mathlib/OIBridge/):
    CompositeDimension   HVec 93, W 97, hom 100, homMap 112, prodState 161, pairVal 164, prodEffVal 182,
                         maxCone 186, actT 198, actC 201, IsNot 210, NativeGate 218, actT_actT 471,
                         actC_actC 476, sum_univ_four' 731, cnot 775, cnot_apply 788, cnot_symm_apply 790,
                         z3 793, nflip 797, actT_apply 828, actC_apply 831, isNot_nflip 838,
                         cnot_prodState_mem_maxCone 1152, nativeGate_cnot 1160, xplus 1213, phiW 1220,
                         cnot_prodState_xplus_z3 1222, xplus_mem 1227, z3_mem 1229, tens 1450,
                         lor_eq_zero_of_head 1576, actT_tens 1923, actC_tens 1930
    CompositeInterface   coord 85, BoundedAffine 139, exists_effect_rescale 148, ProductData 210 (prodEff 216,
                         prodEff_apply 217), PreComposite 223 (convex 226, prod_mem 227, prodEff_effect 228,
                         prodEff_unit 230), Composite 243 (lt 245), condA_mem 431, JointReversible 445,
                         subset_maxBody 467
    KInfFoundations      IsEffectOn 116
    OrbitGeneration      seedTransport 49, PreservesBody 69, isEffectOn_seedTransport 94
    OrbitNormalization   words 53, driveWords3 571, rot3_mem_driveWords3 574, cyc3_mem_driveWords3 577,
                         rotX 581, euler_apply_pole 589, exists_euler_angles 614, exists_word_pole 658
    K2Guard              reflY 46, reflY_mem_eball 67, reflY_reflY 73, det_reflY 78, CandidateCone 95,
                         idW 101, actT_reflY_phiW 106, actT_prodState 173
    RelcSelectBlock      CtrlGate 45 (namespace RelcSelect), ctrlGate_of_nativeGate 53, dim_of_ctrlGate 739
    EffectSpace          sharpVec 57, sharpEff 65, sharpEff_isEffectOn 97, prodEffVal_sharp 514
    TransitiveBody       eball 518
    MonoidalCompletion   tensorOf 193
    OperationalRigidity  psd_trace_mul_nonneg 917
  Introduced here (absent at the base; collision check in NOTES): the table product, the Euclidean pairing and
  dual cone, the twin gate, the four-copy carrier and every statement below. `pauli1`, `pauliW`, `Q3`, `twin`
  follow the EQ2-A design and `NClass` follows EQ2-B's `ctrlGate_classification`; both designs are UNBUILT.
  `Adm` (ClosureObstruction:78) and `IsRot` (QuarterTurn:233) exist at the base with other meanings, hence
  `PairAdm` and `IsRot3`.

  Layers.
    Part A  cheap: finite real linear algebra on `W 3` (`fin_cases`, `simp`, Finset sums); no ℂ, no topology.
    Part B  the bridge from a COMP-1 four-copy composite: the new carrier vocabulary. Moderate.
    Part C  heavy: Pauli dictionary over ℂ, link filters, density and closure, spectral theorem, bipolar,
            Euler generation, IE₁ of Q3 and of the twin.
    Part D  the package: Theorems A–D and the corollary.
    Part E  a remark kept apart from the package: the converse under uniform composition.
  Evidence ids in comments:
    - EQ3 probes p1–p6 (scratchpad/eq3/P);
    - the audit audit_eq3_n1 (K*, O*, I*, L*, G*, P*, F*, Q);
    - this thread's f1_package_identities (K*, R*, W*, C*, B*, G*) and f2_parity_witnesses (K, X1–X3).
  Step tags as in FORMAL.md:
    - (s) state-level;
    - (2) an operation of a standalone two-token composite.
  No (o) step occurs.

  Elaboration hazards (the reason a design check is recommended in FORMAL.md §8):
    - `*` on `W 3` is the pointwise `Pi` product, so the table product is written out as `tabMul`;
    - `Fin (3 + 1)` versus `Fin 4` in rewriting, hence `sum_univ_four'`;
    - images of `LinearEquiv` coercions in `''`;
    - `Bool.xor` for parity;
    - `open scoped ComplexOrder` for `Matrix.PosSemidef` over ℂ.
-/
import OIBridge.K2Guard
import OIBridge.RelcSelectBlock
import OIBridge.OrbitNormalization
import OIBridge.MonoidalCompletion
import OIBridge.OperationalRigidity
import Mathlib.Analysis.Matrix.Spectrum
import Mathlib.Analysis.Matrix.PosDef
import Mathlib.Analysis.Convex.Cone.Dual
import Mathlib.Analysis.Complex.Polynomial.Basic

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard RelcSelect CompositeInterface EffectSpace KInfFoundations
open TransitiveBody OrbitGeneration OrbitNormalization
open scoped ComplexOrder

noncomputable section

/-! ## Part A — cheap layer -/

/-! ### A.1 Table calculus on `W 3` -/

/-- The table product, row = first token. On `W 3 = Fin 4 → Fin 4 → ℝ` the operator `*` is the pointwise
product of the `Pi` instance, not the matrix product, so the product is written out. -/
def tabMul (A B : W 3) : W 3 := fun μ ν => ∑ κ, A μ κ * B κ ν

/-- The token exchange of a table (EQ2-A's `swapW`). -/
def tabT (A : W 3) : W 3 := fun μ ν => A ν μ

/-- The Euclidean pairing of an effect table with a state table. -/
def ipW (E X : W 3) : ℝ := ∑ μ, ∑ ν, E μ ν * X μ ν

/-- The Euclidean dual cone: the effect tables nonnegative on `K`. Up to positive scale these are the
`IsEffectOn` effects (KF:116) of the normalized body; the dictionary is `exists_effect_of_dualW` (Part B). -/
def dualW (K : Set (W 3)) : Set (W 3) := {E | ∀ X ∈ K, 0 ≤ ipW E X}

/-- A convex cone of tables (EQ2-B's `IsConvexCone`; the cone-level reading of COMP-1's `convex`, CI:226). -/
def IsConvexCone (K : Set (W 3)) : Prop :=
  (∀ ω ∈ K, ∀ ω' ∈ K, ω + ω' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K

/-- **H-adm** for one pair: the landed candidate-cone predicate (K2G:95) and convexity. -/
def PairAdm (K : Set (W 3)) : Prop := CandidateCone K ∧ IsConvexCone K

/-- Signs of the global transpose in the Pauli order `1, X, Y, Z`. -/
def sgnY : Fin 4 → ℝ := ![1, 1, -1, 1]

/-- The global transpose on tables (EQ2-A's `transposeW`). -/
def transposeW (ω : W 3) : W 3 := fun μ ν => sgnY μ * sgnY ν * ω μ ν

theorem ipW_comm (E X : W 3) : ipW E X = ipW X E := by
  unfold ipW
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => mul_comm _ _

/-- Product-effect tables pair as `pairVal` (CD:164). -/
theorem ipW_tens (a b : HVec 3) (ω : W 3) : ipW (tens a b) ω = pairVal a b ω := by
  unfold ipW tens pairVal
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring

theorem ipW_tabT (E X : W 3) : ipW (tabT E) (tabT X) = ipW E X := by
  unfold ipW tabT
  exact Finset.sum_comm

theorem tabT_tabT (A : W 3) : tabT (tabT A) = A := rfl

theorem mem_dualW_image_tabT {K : Set (W 3)} {E : W 3} : E ∈ dualW (tabT '' K) ↔ tabT E ∈ dualW K := by
  constructor
  · intro h X hX
    have := h (tabT X) ⟨X, hX, rfl⟩
    rwa [← ipW_tabT, tabT_tabT] at this
  · rintro h _ ⟨X, hX, rfl⟩
    have := h X hX
    rwa [← ipW_tabT, tabT_tabT] at this

theorem smul_mem_dualW {K : Set (W 3)} {E : W 3} {c : ℝ} (hc : 0 < c) :
    c • E ∈ dualW K ↔ E ∈ dualW K := by
  sorry -- ipW (c • E) X = c * ipW E X; positivity of c

theorem isClosed_dualW (K : Set (W 3)) : IsClosed (dualW K) := by
  sorry -- an intersection of closed half-spaces (`isClosed_biInter`); or Mathlib `PointedCone.isClosed_dual`
        -- (Analysis/Convex/Cone/Dual.lean:53) for the pairing `ipW`

/-- `Δ · f · Δᵀ = T f` with `Δ = phiW` (EQ3 p1 B4; audit I1). -/
theorem phiW_tabMul (f : W 3) : tabMul (tabMul phiW f) (tabT phiW) = transposeW f := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [tabMul, tabT, phiW, transposeW, sgnY, sum_univ_four']

/-- Twin Bell links induce no transpose: `idW · f · idWᵀ = f` (p1 E2; p2 P4). -/
theorem idW_tabMul (f : W 3) : tabMul (tabMul idW f) (tabT idW) = f := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [tabMul, tabT, idW, sum_univ_four']

theorem transposeW_transposeW (ω : W 3) : transposeW (transposeW ω) = ω := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [transposeW, sgnY]

theorem ipW_transposeW (E X : W 3) : ipW (transposeW E) X = ipW E (transposeW X) := by
  unfold ipW transposeW
  exact Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => by ring

/-! ### A.2 The interface predicate and its four readings -/

/-- The four-copy contraction (tokens 0, 1, 2, 3): `X` on (0,1), `Y` on (2,3), `E` on (0,2), `F` on (1,3). -/
def fourVal (X Y E F : W 3) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, X a b * Y c d * E a c * F b d

/-- **The interface predicate** (H-KT4 ∧ H-eff at the level of pair tables). `famI`: products of states across
01|23 against products of effects across 02|13. `famII`: products of states across 02|13 against products
of effects across 01|23. The dual cones are the full Euclidean duals (H-eff). -/
structure FourCopyCoherent (K01 K23 K02 K13 : Set (W 3)) : Prop where
  famI : ∀ X ∈ K01, ∀ Y ∈ K23, ∀ E ∈ dualW K02, ∀ F ∈ dualW K13,
    0 ≤ ipW X (tabMul (tabMul E Y) (tabT F))
  famII : ∀ L ∈ K02, ∀ L' ∈ K13, ∀ e ∈ dualW K01, ∀ f ∈ dualW K23,
    0 ≤ ipW e (tabMul (tabMul L f) (tabT L'))

/-- The families read from one target pair `K`, with partner `K'` and link pairs `La`, `Lb`. -/
structure PairLinked (K K' La Lb : Set (W 3)) : Prop where
  upper : ∀ X ∈ K, ∀ Y ∈ K', ∀ E ∈ dualW La, ∀ F ∈ dualW Lb,
    0 ≤ ipW X (tabMul (tabMul E Y) (tabT F))
  lower : ∀ L ∈ La, ∀ L' ∈ Lb, ∀ e ∈ dualW K, ∀ f ∈ dualW K',
    0 ≤ ipW e (tabMul (tabMul L f) (tabT L'))

theorem fourVal_eq_01 (X Y E F : W 3) : fourVal X Y E F = ipW X (tabMul (tabMul E Y) (tabT F)) := by
  sorry -- Finset.mul_sum, Finset.sum_comm, ring under the sums  [X f1 R1; p1 A1; audit O3]
theorem fourVal_eq_23 (X Y E F : W 3) : fourVal X Y E F = ipW Y (tabMul (tabMul (tabT E) X) F) := by
  sorry -- [X f1 R2]
theorem fourVal_eq_02 (X Y E F : W 3) : fourVal X Y E F = ipW E (tabMul (tabMul X F) (tabT Y)) := by
  sorry -- [X f1 R3]
theorem fourVal_eq_13 (X Y E F : W 3) : fourVal X Y E F = ipW F (tabMul (tabMul (tabT X) E) Y) := by
  sorry -- [X f1 R4]; countercontrol f1 R5: without the transposes the identity fails

variable {K01 K23 K02 K13 : Set (W 3)}

/-- Lemma R, target 01. -/
theorem FourCopyCoherent.target01 (h : FourCopyCoherent K01 K23 K02 K13) : PairLinked K01 K23 K02 K13 :=
  ⟨h.famI, h.famII⟩

/-- Lemma R, target 02: the 01 and 23 tables act as links. -/
theorem FourCopyCoherent.target02 (h : FourCopyCoherent K01 K23 K02 K13) : PairLinked K02 K13 K01 K23 where
  upper X hX Y hY E hE F hF := by
    have := h.famII X hX Y hY E hE F hF
    rwa [← fourVal_eq_01, fourVal_eq_02] at this
  lower L hL L' hL' e he f hf := by
    have := h.famI L hL L' hL' e he f hf
    rwa [← fourVal_eq_01, fourVal_eq_02] at this

/-- Lemma R, target 23: links read through the token exchange. -/
theorem FourCopyCoherent.target23 (h : FourCopyCoherent K01 K23 K02 K13) :
    PairLinked K23 K01 (tabT '' K02) (tabT '' K13) := by
  sorry -- fourVal_eq_01 and fourVal_eq_23 with mem_dualW_image_tabT  [X f1 R2]

/-- Lemma R, target 13. -/
theorem FourCopyCoherent.target13 (h : FourCopyCoherent K01 K23 K02 K13) :
    PairLinked K13 K02 (tabT '' K01) (tabT '' K23) := by
  sorry -- fourVal_eq_01 and fourVal_eq_13 with mem_dualW_image_tabT  [X f1 R4]

/-! ### A.3 The four-copy table carrier at the cone level (Lemma B2) -/

/-- The four-copy table carrier, tokens in the order 0, 1, 2, 3; local tomography is built in, as for `W d`
(CD:95–97). -/
abbrev W4 := Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ

/-- Product of pair tables across 01|23. -/
def prodA (X Y : W 3) : W4 := fun a b c d => X a b * Y c d
/-- Product of pair tables across 02|13. -/
def prodB (L L' : W 3) : W4 := fun a b c d => L a c * L' b d
/-- Product effect across 01|23. -/
def effA (e f : W 3) (Ω : W4) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, e a b * f c d * Ω a b c d
/-- Product effect across 02|13. -/
def effB (E F : W 3) (Ω : W4) : ℝ := ∑ a, ∑ b, ∑ c, ∑ d, E a c * F b d * Ω a b c d

/-- Cone-level KT(4; 01|23, 02|13): one four-copy cone carrying both groupings' products of states, on which both
groupings' products of effects with full dual-cone factors are nonnegative. -/
structure KT4Cone (K01 K23 K02 K13 : Set (W 3)) (K4 : Set W4) : Prop where
  prodA_mem : ∀ X ∈ K01, ∀ Y ∈ K23, prodA X Y ∈ K4
  prodB_mem : ∀ L ∈ K02, ∀ L' ∈ K13, prodB L L' ∈ K4
  effA_nonneg : ∀ e ∈ dualW K01, ∀ f ∈ dualW K23, ∀ Ω ∈ K4, 0 ≤ effA e f Ω
  effB_nonneg : ∀ E ∈ dualW K02, ∀ F ∈ dualW K13, ∀ Ω ∈ K4, 0 ≤ effB E F Ω

theorem effA_prodA (e f X Y : W 3) : effA e f (prodA X Y) = ipW e X * ipW f Y := by
  sorry -- [X f1 W1]
theorem effB_prodB (E F L L' : W 3) : effB E F (prodB L L') = ipW E L * ipW F L' := by
  sorry -- [X f1 W1]
theorem effB_prodA (E F X Y : W 3) : effB E F (prodA X Y) = fourVal X Y E F := by
  sorry -- [X f1 W2]
theorem effA_prodB (e f L L' : W 3) : effA e f (prodB L L') = fourVal e f L L' := by
  sorry -- [X f1 W2]
/-- Token coherence holds in the table model (f1 W3); reading one factor transposed breaks it (f1 W4). -/
theorem effA_tens_eq_effB (a b c d : HVec 3) (Ω : W4) :
    effA (tens a b) (tens c d) Ω = effB (tens a c) (tens b d) Ω := by
  sorry -- [X f1 W3]

/-- **Lemma B2, (⇐).** A cone-level four-copy body gives the interface. -/
theorem fourCopyCoherent_of_kt4Cone {K4 : Set W4} (h : KT4Cone K01 K23 K02 K13 K4) :
    FourCopyCoherent K01 K23 K02 K13 where
  famI X hX Y hY E hE F hF := by
    rw [← fourVal_eq_01, ← effB_prodA]
    exact h.effB_nonneg E hE F hF _ (h.prodA_mem X hX Y hY)
  famII L hL L' hL' e he f hf := by
    rw [← fourVal_eq_01, ← effA_prodB]
    exact h.effA_nonneg e he f hf _ (h.prodB_mem L hL L' hL')

/-- **Lemma B2, (⇒).** The interface is realized by an explicit cone-level four-copy body (faithfulness; not
used by the theorems). -/
theorem exists_kt4Cone_of_fourCopyCoherent (h : FourCopyCoherent K01 K23 K02 K13) :
    ∃ K4 : Set W4, KT4Cone K01 K23 K02 K13 K4 := by
  refine ⟨{Ω | (∀ e ∈ dualW K01, ∀ f ∈ dualW K23, 0 ≤ effA e f Ω) ∧
      (∀ E ∈ dualW K02, ∀ F ∈ dualW K13, 0 ≤ effB E F Ω)}, ?_, ?_, ?_, ?_⟩
  · intro X hX Y hY
    refine ⟨fun e he f hf => ?_, fun E hE F hF => ?_⟩
    · rw [effA_prodA]; exact mul_nonneg (he X hX) (hf Y hY)
    · rw [effB_prodA, fourVal_eq_01]; exact h.famI X hX Y hY E hE F hF
  · intro L hL L' hL'
    refine ⟨fun e he f hf => ?_, fun E hE F hF => ?_⟩
    · rw [effA_prodB, fourVal_eq_01]; exact h.famII L hL L' hL' e he f hf
    · rw [effB_prodB]; exact mul_nonneg (hE L hL) (hF L' hL')
  · exact fun e he f hf Ω hΩ => hΩ.1 e he f hf
  · exact fun E hE F hF Ω hΩ => hΩ.2 E hE F hF

/-! ### A.4 Aligned gates, Bell data, the inverse's dual action, N-CLASS -/

/-- `actT N` as a linear equivalence, for an involution `N` (actT_actT, CD:471). -/
def actTEquiv (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (hN : ∀ x, N (N x) = x) : W 3 ≃ₗ[ℝ] W 3 where
  toFun := actT N
  invFun := actT N
  map_add' := by sorry -- homMap is linear (CD:112)
  map_smul' := by sorry
  left_inv := actT_actT hN
  right_inv := actT_actT hN

/-- The twin-oriented gate `cnot' = R_B ∘ cnot ∘ R_B`, `R_B = actT reflY` (EQ3's `cnot'`). -/
def cnotTw : W 3 ≃ₗ[ℝ] W 3 :=
  ((actTEquiv reflY reflY_reflY).trans cnot).trans (actTEquiv reflY reflY_reflY)

theorem cnotTw_apply (ω : W 3) : cnotTw ω = actT reflY (cnot (actT reflY ω)) := rfl

/-- The aligned gate of orientation `τ`: `cnot` for `false`, `cnot'` for `true`. -/
def gateOf (τ : Bool) : W 3 ≃ₗ[ℝ] W 3 := if τ then cnotTw else cnot

/-- The aligned gates are involutions (CD:790; f1 C1); for them H-inv coincides with H-gate. -/
theorem gateOf_symm_apply (τ : Bool) (ω : W 3) : (gateOf τ).symm ω = gateOf τ ω := by
  sorry -- cases τ; cnot_symm_apply (CD:790); actT_actT (CD:471) with reflY_reflY (K2G:73)

/-- Euclidean self-adjointness of the aligned gates (audit K3; p1 B2; f1 C1). -/
theorem ipW_gateOf (τ : Bool) (E X : W 3) : ipW (gateOf τ E) X = ipW E (gateOf τ X) := by
  sorry -- cases τ; the 16 entries are a signed permutation: fin_cases and sum_univ_four'

/-- The twin Bell table (f1 C2). -/
theorem cnotTw_prodState_xplus_z3 : cnotTw (prodState xplus z3) = idW := by
  have hz : reflY z3 = z3 := by
    funext i
    fin_cases i <;> simp [z3]
  rw [cnotTw_apply, actT_prodState, hz, cnot_prodState_xplus_z3, actT_reflY_phiW]

/-- `cnot'` satisfies every native-gate hypothesis with `nflip` and `z3`. Witness for H-pairwise in the twin
orientation. -/
theorem nativeGate_cnotTw : NativeGate (eball 3) z3 nflip cnotTw := by
  sorry -- frame, relT, relC: fin_cases [X f1 C3]; posFwd and posInv: cnotTw (prodState x y)
        -- = actT reflY (cnot (prodState x (reflY y))) [X f1 C4], cnot_prodState_mem_maxCone (CD:1152),
        -- reflY_mem_eball (K2G:67), and actT reflY preserves maxCone (eball 3)  [W]

/-- A reflection chart at the first token also turns `cnot` into `cnot'` (f2 X1). -/
theorem actC_reflY_cnot_actC_reflY (ω : W 3) : actC reflY (cnot (actC reflY ω)) = cnotTw ω := by
  sorry -- funext; fin_cases on 16 entries  [X f2 X1; countercontrol with nflip]

/-- Sharp product-effect tables (ES:57): `sharpVec b ⊗ sharpVec c = ¼ prodState b c`. -/
theorem tens_sharpVec (b c : Fin 3 → ℝ) :
    tens (sharpVec b) (sharpVec c) = (1 / 4 : ℝ) • prodState b c := by
  sorry -- sharpVec b = (1/2) • hom b, entrywise

/-- **Gate-supplied effects (aligned), a (2) step.** The dual action of an aligned gate on a product of sharp
effects is an effect table of every candidate cone that the gate preserves. -/
theorem gate_sharp_mem_dualW {τ : Bool} {K : Set (W 3)} (hK : CandidateCone K)
    (hG : ∀ ω ∈ K, gateOf τ ω ∈ K) {b c : Fin 3 → ℝ} (hb : ∑ j, b j ^ 2 = 1) (hc : ∑ j, c j ^ 2 = 1) :
    gateOf τ (tens (sharpVec b) (sharpVec c)) ∈ dualW K := by
  intro X hX
  rw [ipW_gateOf, ipW_tens, ← prodEffVal_sharp]
  exact hK.2 (hG X hX) _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- **Dual action of the inverse gate, a (2) step** (audit §5a, G1, G3). For a gate orthogonal for `ipW`, if
its inverse preserves `K` (H-inv) then `N E` is an effect table of `K` whenever `E` is. The effect `e ∘ N⁻¹`
has table `(N⁻¹)ᵀ E = N E`. This is the only use of H-inv. -/
theorem dualW_of_inv {N : W 3 ≃ₗ[ℝ] W 3} (hNo : ∀ E X, ipW (N E) (N X) = ipW E X)
    {K : Set (W 3)} (hinv : ∀ ω ∈ K, N.symm ω ∈ K) {E : W 3} (hE : E ∈ dualW K) : N E ∈ dualW K := by
  intro X hX
  have h := hE (N.symm X) (hinv X hX)
  rwa [← hNo E (N.symm X), N.apply_symm_apply] at h

/-- Orthogonality of a one-copy linear map. -/
def IsOrth3 (A : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' A ∈ Matrix.orthogonalGroup (Fin 3) ℝ

/-- **H-NCLASS**: the native gate is `ℓ₁ ∘ cnot ∘ ℓ₂` with orthogonal local factors. `ℓ₁ = (A, B)` are the
post-locals and `ℓ₂ = (A', B')` the pre-locals (EQ2-B `ctrlGate_classification`, UNBUILT). -/
def NClass (N : W 3 ≃ₗ[ℝ] W 3) (A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  IsOrth3 A ∧ IsOrth3 B ∧ IsOrth3 A' ∧ IsOrth3 B' ∧
    ∀ ω, N ω = actC A (actT B (cnot (actC A' (actT B' ω))))

/-- N-CLASS gates are orthogonal for the Euclidean pairing, so `(N⁻¹)ᵀ = N` [X audit G1]. -/
theorem NClass.ipW_map {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    (h : NClass N A B A' B') (E X : W 3) : ipW (N E) (N X) = ipW E X := by
  sorry -- homMap of an orthogonal map is orthogonal; actC, actT are left/right multiplications; cnot is a
        -- signed permutation (audit K3)

/-- The post-local Bell table `H_R`, `R = A · reflY · Bᵀ` [X audit G2]. -/
def bellOf (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : W 3 := actC A (actT B phiW)

/-- Bell state, a (2) step: the gate applied to a product state of the standalone pair [X audit G2]. -/
theorem NClass.bell_state {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    (h : NClass N A B A' B') : ∃ x ∈ eball 3, ∃ y ∈ eball 3, N (prodState x y) = bellOf A B := by
  sorry -- x = A'⁻¹ xplus, y = B'⁻¹ z3; actT_prodState (K2G:173) and its actC analogue;
        -- cnot_prodState_xplus_z3 (CD:1222)

/-- Bell effect, a (2) step: the gate applied to a product of sharp effects, `¼ H_R`, the same identification
as the Bell state [X audit G3]. Through `N`'s own dual the identification differs [X audit G5, f1 G3]. -/
theorem NClass.bell_effect {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    (h : NClass N A B A' B') :
    ∃ b c : Fin 3 → ℝ, ∑ j, b j ^ 2 = 1 ∧ ∑ j, c j ^ 2 = 1 ∧
      N (tens (sharpVec b) (sharpVec c)) = (1 / 4 : ℝ) • bellOf A B := by
  sorry -- b = A'⁻¹ xplus, c = B'⁻¹ z3, tens_sharpVec, NClass.bell_state

/-- The Bell-link map in general charts: `Θ g = H_{R02} · g · H_{R13}ᵀ` [X audit G4; p2 U1]. -/
def Theta (A02 B02 A13 B13 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (g : W 3) : W 3 :=
  tabMul (tabMul (bellOf A02 B02) g) (tabT (bellOf A13 B13))

/-! ### A.5 The two inclusions, inequality form (no closedness) -/

/-- **Inclusion (I), inequality form.** Link states in `K02`, `K13` send `K23*` into `K01**`. Steps: links (2),
then products of states across 02|13 and of effects across 01|23 (s). -/
theorem incl_I (h : FourCopyCoherent K01 K23 K02 K13) {β02 β13 : W 3} (h02 : β02 ∈ K02)
    (h13 : β13 ∈ K13) {f : W 3} (hf : f ∈ dualW K23) :
    tabMul (tabMul β02 f) (tabT β13) ∈ dualW (dualW K01) := by
  intro e he
  rw [ipW_comm]
  exact h.famII β02 h02 β13 h13 e he f hf

/-- **Inclusion (II)** (no closedness). Link effects in `K02*`, `K13*` bound `K01` by the dual of the linked
image of `K23`. -/
theorem incl_II (h : FourCopyCoherent K01 K23 K02 K13) {ε02 ε13 : W 3} (h02 : ε02 ∈ dualW K02)
    (h13 : ε13 ∈ dualW K13) {X : W 3} (hX : X ∈ K01) :
    X ∈ dualW ((fun Y => tabMul (tabMul ε02 Y) (tabT ε13)) '' K23) := by
  rintro _ ⟨Y, hY, rfl⟩
  exact h.famI X hX Y hY ε02 h02 ε13 h13

/-- Aligned (I) with the `cnot` Bell link: `T(K23*) ⊆ K01**` [X p2 N1; audit I1]. -/
theorem incl_I_aligned (h : FourCopyCoherent K01 K23 K02 K13) (h02 : phiW ∈ K02) (h13 : phiW ∈ K13) :
    transposeW '' dualW K23 ⊆ dualW (dualW K01) := by
  rintro _ ⟨f, hf, rfl⟩
  rw [← phiW_tabMul]
  exact incl_I h h02 h13 hf

/-- Aligned (II): `K01 ⊆ T(K23*)` [X p2 N2; audit I2]. -/
theorem incl_II_aligned (h : FourCopyCoherent K01 K23 K02 K13) (h02 : phiW ∈ dualW K02)
    (h13 : phiW ∈ dualW K13) : K01 ⊆ transposeW '' dualW K23 := by
  intro X hX
  refine ⟨transposeW X, fun Y hY => ?_, transposeW_transposeW X⟩
  have := incl_II h h02 h13 hX (tabMul (tabMul phiW Y) (tabT phiW)) ⟨Y, hY, rfl⟩
  rwa [phiW_tabMul, ← ipW_transposeW] at this

/-! ### A.6 Lemma P — aligned parity (cheap: no closedness, no convexity, no ℂ) -/

/-- Twist parity of the 4-cycle 0–1–3–2–0, pairs in the order (01, 23, 02, 13). -/
def EvenCycle4 (τ01 τ23 τ02 τ13 : Bool) : Prop :=
  Bool.xor (Bool.xor τ01 τ13) (Bool.xor τ23 τ02) = false

/-- **Lemma P.** Witness at every odd pattern [X f2 X3; f1 B2]: `X = gateOf τ01 (prodState xplus z3)`,
`Y = gateOf τ23 (prodState xplus z3)`, `E = gateOf τ02 (tens (sharpVec xplus) (sharpVec z3))`,
`F = gateOf τ13 (tens (sharpVec (-xplus)) (sharpVec (-z3)))`. The family-(i) value is `-1/8`. -/
theorem kt4_parity_aligned {τ01 τ23 τ02 τ13 : Bool}
    (c01 : CandidateCone K01) (c23 : CandidateCone K23) (c02 : CandidateCone K02) (c13 : CandidateCone K13)
    (g01 : ∀ ω ∈ K01, gateOf τ01 ω ∈ K01) (g23 : ∀ ω ∈ K23, gateOf τ23 ω ∈ K23)
    (g02 : ∀ ω ∈ K02, gateOf τ02 ω ∈ K02) (g13 : ∀ ω ∈ K13, gateOf τ13 ω ∈ K13)
    (h : FourCopyCoherent K01 K23 K02 K13) : EvenCycle4 τ01 τ23 τ02 τ13 := by
  have hX := g01 _ (c01.1 xplus xplus_mem z3 z3_mem)                       -- (2)
  have hY := g23 _ (c23.1 xplus xplus_mem z3 z3_mem)                       -- (2)
  have hx1 : ∑ j, xplus j ^ 2 = 1 := by simp [xplus, Fin.sum_univ_three]
  have hz1 : ∑ j, z3 j ^ 2 = 1 := by simp [z3, Fin.sum_univ_three]
  have hx1' : ∑ j, (-xplus) j ^ 2 = 1 := by simp [xplus, Fin.sum_univ_three]
  have hz1' : ∑ j, (-z3) j ^ 2 = 1 := by simp [z3, Fin.sum_univ_three]
  have hE := gate_sharp_mem_dualW c02 g02 hx1 hz1                          -- (2)
  have hF := gate_sharp_mem_dualW c13 g13 hx1' hz1'                        -- (2)
  have hv := h.famI _ hX _ hY _ hE _ hF                                    -- (s)
  unfold EvenCycle4
  revert hv
  cases τ01 <;> cases τ23 <;> cases τ02 <;> cases τ13 <;> intro hv <;> sorry
  -- even patterns: `rfl`; odd patterns: evaluate `hv` to `0 ≤ -1/8` (entries are explicit: cnot_apply,
  -- cnotTw_apply, tens_sharpVec, sum_univ_four') and close with `norm_num`  [X f2 X3]

/-! ### A.7 Per-token reflection charts (D1; a re-description, not an operation) -/

/-- The per-token reflection chart on a pair. -/
def chartR (εi εj : Bool) (ω : W 3) : W 3 :=
  (if εi then actC reflY else id) ((if εj then actT reflY else id) ω)

/-- Coboundary patterns are untwisted by per-token reflection charts [X f2 X1–X2]. -/
theorem chartR_gateOf (εi εj : Bool) (ω : W 3) :
    chartR εi εj (gateOf (Bool.xor εi εj) (chartR εi εj ω)) = cnot ω := by
  sorry -- four cases: definition of cnotTw, actC_reflY_cnot_actC_reflY, and transposeW ∘ cnot = cnot ∘ transposeW
        -- (p1 B3) with actC reflY ∘ actT reflY = transposeW

/-- The interface predicate is transported by per-token reflection charts. The reflections are orthogonal
involutions, and each token's index is reflected in both tables that carry it. -/
theorem fourCopyCoherent_chart (ε : Fin 4 → Bool) (h : FourCopyCoherent K01 K23 K02 K13) :
    FourCopyCoherent (chartR (ε 0) (ε 1) '' K01) (chartR (ε 2) (ε 3) '' K23)
      (chartR (ε 0) (ε 2) '' K02) (chartR (ε 1) (ε 3) '' K13) := by
  sorry -- fourVal is invariant when each token's index carries the same diagonal sign in both tables

/-! ## Part B — the bridge from a COMP-1 four-copy composite (new carrier vocabulary; moderate) -/

/-- Flattening of pair tables into the chart `Fin 16 → ℝ`: COMP-1's factor bodies are chart sets (CI:223). -/
def flatW : W 3 ≃ₗ[ℝ] (Fin 16 → ℝ) := by
  sorry -- currying `Fin 4 × Fin 4 → ℝ` and `finProdFinEquiv`; LinearEquiv.funCongrLeft

/-- The normalized pair body of a cone in the flat chart: each group's full body. -/
def pairBody (K : Set (W 3)) : Set (Fin 16 → ℝ) := flatW '' {ω | ω ∈ K ∧ ω 0 0 = 1}

/-- The table-entry functional `ω ↦ ω μ ν` on the flat chart: COMP-1's `coord` (CI:85). -/
def tabCoord (μ ν : Fin 4) : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ := coord (finProdFinEquiv (μ, ν))

/-- **H-KT4.tok.** The four-token product effects built through either grouping agree on the body. -/
def TokenCoherent {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    {Ω01 Ω23 Ω02 Ω13 : Set (Fin 16 → ℝ)} (PA : PreComposite Ω01 Ω23 V) (PB : PreComposite Ω02 Ω13 V) :
    Prop :=
  ∀ a b c d : Fin 4, ∀ ω ∈ PA.Ω,
    PA.prodEff (tabCoord a b) (tabCoord c d) ω = PB.prodEff (tabCoord a c) (tabCoord b d) ω

/-- **H-KT4** in the form the forward derivation reads: two COMP-1 pre-composites with the full normalized pair
bodies as group bodies, one body, and token coherence. KT as stated in EQ3 takes `Composite` (with `lt`,
CI:245); `lt` is H-LT and is not read here. -/
structure KT4 (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  PA : PreComposite (pairBody K01) (pairBody K23) V
  PB : PreComposite (pairBody K02) (pairBody K13) V
  one_body : PA.Ω = PB.Ω
  tok : TokenCoherent PA PB

/-- The normalized slice of DIM-1's maximal cone is bounded. -/
theorem abs_le_one_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (h00 : ω 0 0 = 1) (μ ν : Fin 4) :
    |ω μ ν| ≤ 1 := by
  sorry -- pair with sharp effects along ±e_j and the unit (ES:97, ES:514)

/-- Dual-cone tables are positive multiples of `IsEffectOn` effects of the normalized body (the H-eff
dictionary). -/
theorem exists_effect_of_dualW {K : Set (W 3)} (hK : CandidateCone K) {E : W 3} (hE : E ∈ dualW K) :
    ∃ c : ℝ, 0 < c ∧ IsEffectOn (pairBody K) (c • ∑ μ, ∑ ν, E μ ν • tabCoord μ ν) := by
  sorry -- abs_le_one_of_maxCone bounds `ipW E` on the slice; rescale

/-- A functional vanishing on a factor body has vanishing product effects on the composite body. `g` and `-g`
are both effects there, so this uses H-eff twice; a general `f` is reached through `exists_effect_rescale`
(CI:148). -/
theorem prodEff_eq_zero_of_vanish {Ω₁ Ω₂ : Set (Fin 16 → ℝ)} {V : Type} [NormedAddCommGroup V]
    [NormedSpace ℝ V] (P : PreComposite Ω₁ Ω₂ V) (hb : BoundedAffine Ω₂) {g : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ}
    (hg : ∀ x ∈ Ω₁, g x = 0) (f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ) : ∀ ω ∈ P.Ω, P.prodEff g f ω = 0 := by
  sorry

/-- **Lemma B1 (H-KT4 ∧ H-eff ⇒ interface).** No `Composite.lt` field, no closedness and no gate is used. -/
theorem fourCopyCoherent_of_kt4 {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (a01 : PairAdm K01) (a23 : PairAdm K23) (a02 : PairAdm K02) (a13 : PairAdm K13)
    (H : KT4 K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 := by
  sorry
  -- (1) X ∈ K is `X 0 0 • (normalized X)`; `X 0 0 = 0` forces `X = 0` in maxCone (eball 3) (via toOp and
  --     lor_eq_zero_of_head, CD:1576);
  -- (2) exists_effect_of_dualW for the effect factors;
  -- (3) prodEff_eq_zero_of_vanish to pass from an effect to its table expansion;
  -- (4) bilinearity of `prodEff` (CI:216) and H.tok;
  -- (5) prodEff_apply (CI:217) on products. H.one_body gives PA.Ω ⊆ PB.Ω for famI and PB.Ω ⊆ PA.Ω for
  --     famII; the value is fourVal [X f1 W2; p1 A1–A3; audit O1–O3].

/-! ## Part C — heavy layer (statements; proofs open) -/

/-! ### C.1 Pauli dictionary (EQ2-A §A design names) -/

/-- Pauli matrices in the kernel coordinate order: 0 ↦ 1, 1 ↦ X, 2 ↦ Y, 3 ↦ Z. -/
def pauli1 : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- The Pauli presentation of a pair table (first index = first token; MonoidalCompletion.tensorOf, MC:193). -/
def pauliW (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  (1 / 4 : ℂ) • ∑ μ, ∑ ν, ((ω μ ν : ℝ) : ℂ) • MonoidalCompletion.tensorOf (pauli1 μ) (pauli1 ν)

/-- The quantum pair cone. -/
def Q3 : Set (W 3) := {ω | (pauliW ω).PosSemidef}
/-- The twin: `R_B Q3`. -/
def twin : Set (W 3) := actT reflY '' Q3
/-- The pair cone of orientation `τ`. -/
def twistQ3 (τ : Bool) : Set (W 3) := if τ then twin else Q3

theorem phiW_mem_Q3 : phiW ∈ Q3 := by sorry            -- [X f1 G0; EQ2-A a1 A1.8]
theorem phiW_not_mem_twin : phiW ∉ twin := by sorry    -- [X f1 G0]
theorem idW_mem_twin : idW ∈ twin := ⟨phiW, phiW_mem_Q3, actT_reflY_phiW⟩
theorem idW_not_mem_Q3 : idW ∉ Q3 := by sorry          -- singlet eigenvalue −1/2 [X f1 G0; audit K5]
theorem candidateCone_Q3 : CandidateCone Q3 := by sorry
  -- products: Matrix.PosSemidef.kronecker (Mathlib Analysis/Matrix/Order.lean:213); Q3 ⊆ maxCone: lor_ehom (CD:930)
  -- and psd_trace_mul_nonneg (OR:917)
theorem isConvexCone_Q3 : IsConvexCone Q3 := by sorry -- Matrix.PosSemidef.add, .smul (LinearAlgebra/Matrix/PosDef.lean:102, 107)
/-- Self-duality of `Q3` for the Euclidean pairing: `ipW E X = 4 tr(pauliW E · pauliW X)`. -/
theorem dualW_Q3 : dualW Q3 = Q3 := by sorry
  -- ⊇ psd_trace_mul_nonneg (OR:917); ⊆ Matrix.posSemidef_iff_dotProduct_mulVec (LinearAlgebra/Matrix/PosDef.lean:297)
  -- tested on pure tables
theorem dualW_twin : dualW twin = twin := by sorry     -- actT reflY is an orthogonal involution
theorem isClosed_Q3 : IsClosed Q3 := by
  rw [← dualW_Q3]; exact isClosed_dualW Q3
/-- The chart rule: an O(3) × O(3) chart maps `Q3` onto `Q3` or onto the twin according to the determinant
product. -/
theorem chart_rule {A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (hA : IsOrth3 A) (hB : IsOrth3 B) :
    (fun ω => actC A (actT B ω)) '' Q3 =
      twistQ3 (decide (LinearMap.det A * LinearMap.det B = -1)) := by sorry
  -- SO(3) part: ie1_Q3 (C.4); reflections: actC reflY ∘ actT reflY = transposeW and transposeW '' Q3 = Q3
  -- [X f1 G1 instances; W]
theorem bellOf_mem_twistQ3 {A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (hA : IsOrth3 A) (hB : IsOrth3 B) :
    bellOf A B ∈ twistQ3 (decide (LinearMap.det A * LinearMap.det B = -1)) := by sorry  -- [X f1 G1]

/-! ### C.2 Bipolar -/

/-- `K** = cl K` for a nonempty convex cone of tables. -/
theorem dualW_dualW {K : Set (W 3)} (hK : IsConvexCone K) (hne : K.Nonempty) :
    dualW (dualW K) = closure K := by
  sorry
  -- ⊇: isClosed_dualW and K ⊆ K**;
  -- ⊆: geometric_hahn_banach_closed_point (Mathlib Analysis/LocallyConvex/Separation.lean:231) applied to
  --    closure K (Convex.closure, Analysis/Convex/Topology.lean:198); the cone scaling forces the separating
  --    functional to be ≤ 0 on K; represent it by its table

/-! ### C.3 Link filters and the pure-state supply (aligned) -/

/-- The table of the pure state with coefficient matrix `C` (row = first token): `tr(Cᴴ σ_μ C σ_νᵀ)`. -/
def pureTab (C : Matrix (Fin 2) (Fin 2) ℂ) : W 3 :=
  fun μ ν => (Matrix.trace (Cᴴ * pauli1 μ * C * (pauli1 ν)ᵀ)).re

theorem pureTab_mem_Q3 (C : Matrix (Fin 2) (Fin 2) ℂ) : pureTab C ∈ Q3 := by sorry
  -- pauliW (pureTab C) = vecMulVec v (star v), v = vec C; Matrix.posSemidef_vecMulVec_self_star
  -- (LinearAlgebra/Matrix/PosDef.lean:412)

/-- The Bloch vector of a nonzero qubit vector. -/
def blochOf (a : Fin 2 → ℂ) : Fin 3 → ℝ :=
  fun j => (Matrix.trace (Matrix.vecMulVec a (star a) * pauli1 j.succ)).re /
    (Matrix.trace (Matrix.vecMulVec a (star a))).re

/-- The filtered conditional of a partner gate effect through Schmidt-diagonal links is a positive multiple of
a pure table with coefficient `diag(1,u) · conj(Circ b) · diag(1,u')` [X audit L4; p1 C2, D2–D3]. -/
theorem link_conditional (u u' : ℂ) (b : Fin 2 → ℂ) (hb : b ≠ 0) :
    ∃ c : ℝ, 0 < c ∧
      tabMul (tabMul (cnot (prodState (blochOf ![1, u]) z3))
          (cnot (tens (sharpVec xplus) (sharpVec (blochOf b)))))
        (tabT (cnot (prodState (blochOf ![1, u']) z3))) =
      c • pureTab (Matrix.diagonal ![1, u] * (Matrix.of ![![b 0, b 1], ![b 1, b 0]]).map star *
        Matrix.diagonal ![1, u']) := by sorry

/-- Coverage [X audit L3; p1 D1]: every coefficient matrix with four nonzero entries has the form above, with
`w` a square root of `pqr/s` (Mathlib IsAlgClosed.exists_eq_mul_self, FieldTheory/IsAlgClosed/Basic.lean:90). -/
theorem coverage {C : Matrix (Fin 2) (Fin 2) ℂ} (hC : ∀ i j, C i j ≠ 0) :
    ∃ (u u' : ℂ) (b : Fin 2 → ℂ) (s : ℂ), b ≠ 0 ∧ s ≠ 0 ∧
      C = s • (Matrix.diagonal ![1, u] * (Matrix.of ![![b 0, b 1], ![b 1, b 0]]).map star *
        Matrix.diagonal ![1, u']) := by sorry

/-- Density of generic coefficient matrices (Mathlib dense_pi, Topology/NhdsWithin.lean:421; dense_compl_singleton,
Topology/ClusterPt.lean:274). -/
theorem dense_generic : Dense {C : Matrix (Fin 2) (Fin 2) ℂ | ∀ i j, C i j ≠ 0} := by sorry

/-- A closed convex cone containing every generic pure table contains `Q3`. Pure tables of all coefficient
matrices by density and continuity (image_closure_subset_closure_image, Topology/Continuous.lean:211); then
`Q3` as the cone of pure tables by the spectral theorem (Matrix.IsHermitian.spectral_theorem,
Analysis/Matrix/Spectrum.lean:141; Matrix.PosSemidef.eigenvalues_nonneg, Analysis/Matrix/PosDef.lean:42). -/
theorem Q3_subset_of_generic {K : Set (W 3)} (hK : IsConvexCone K) (hcl : IsClosed K)
    (hpure : ∀ C : Matrix (Fin 2) (Fin 2) ℂ, (∀ i j, C i j ≠ 0) → pureTab C ∈ K) : Q3 ⊆ K := by sorry

/-! ### C.4 Rotations, Euler generation, IE₁ -/

/-- Rotations of one ball. -/
def IsRot3 (R : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  LinearMap.toMatrix' R ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ

/-- **IE₁** for one pair cone: invariance under every local rotation of either token. -/
def IE1 (K : Set (W 3)) : Prop := ∀ R, IsRot3 R → actC R '' K = K ∧ actT R '' K = K

/-- IE₁ in EQ2's form: invariance under the composite lifts of the landed drive words (ON:571). -/
def IE1Drive (K : Set (W 3)) : Prop :=
  ∀ g ∈ driveWords3, actC (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K ∧
    actT (g.linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) '' K = K

/-- Euler generation. The base gives pole transitivity (euler_apply_pole ON:589, exists_euler_angles ON:614,
exists_word_pole ON:658). The stabilizer of the pole in SO(3) is the rotations about the third axis (EQ2-B Lemma
DW, UNBUILT). Mathlib has no Euler-angle decomposition (FORMAL.md §7). -/
theorem so3_euler {R : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} (hR : IsRot3 R) :
    ∃ ψ θ φ : ℝ, R = ((rot3 ψ * rotX θ * rot3 φ).linear : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) := by sorry

theorem ie1_Q3 : IE1 Q3 := by sorry      -- spin lift of rot3 and rotX (explicit unitaries), so3_euler, pauliW
theorem ie1_twin : IE1 twin := by sorry  -- actT reflY normalizes the local rotation group
/-- The drive form needs only that the drive words are rotations (the easy direction of EQ2-B Lemma DW):
the generators rot3 t and cyc3 (ON:574, ON:577) have determinant 1 and preserve the norm. -/
theorem ie1Drive_of_ie1 {K : Set (W 3)} (h : IE1 K) : IE1Drive K := by sorry

/-! ## Part D — the package -/

/-- The four pairs of the instance: the groups of the groupings 01|23 and 02|13. -/
inductive Pr
  | p01 | p23 | p02 | p13
  deriving DecidableEq, Fintype

/-- The interface predicate for a family of pair cones. -/
abbrev FCC (K : Pr → Set (W 3)) : Prop := FourCopyCoherent (K .p01) (K .p23) (K .p02) (K .p13)

/-- Twist parity of the 4-cycle. -/
def EvenCycle (τ : Pr → Bool) : Prop := EvenCycle4 (τ .p01) (τ .p23) (τ .p02) (τ .p13)

/-- The orientation bit of a gate: the determinant sign of its post-locals. -/
def orient (A B : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Bool := decide (LinearMap.det A * LinearMap.det B = -1)

/-- **Theorem B (aligned form).** Gates exactly `cnot` or `cnot'`; no N-CLASS; H-inv coincides with H-gate. -/
theorem kt4_aligned (K : Pr → Set (W 3)) (τ : Pr → Bool)
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, gateOf (τ p) ω ∈ K p) (h : FCC K) :
    (∀ p, K p = twistQ3 (τ p)) ∧ (∀ p, IE1 (K p)) ∧ EvenCycle τ := by
  sorry
  -- parity: kt4_parity_aligned (Part A);
  -- charts: fourCopyCoherent_chart and chartR_gateOf reduce to all-`cnot`;
  -- lower bound: FourCopyCoherent.target01/23/02/13, link_conditional, coverage, dense_generic,
  --   Q3_subset_of_generic, dualW_dualW;
  -- upper bound: incl_II_aligned, dualW_Q3;
  -- squeeze: phiW_mem_Q3, idW_not_mem_Q3;
  -- IE₁: ie1_Q3, ie1_twin

/-- **Theorem C (general charts).** N-CLASS; inclusion (II) through the dual action of the inverse gate. -/
theorem kt4_general (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p) (h : FCC K) :
    K .p01 = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, K p = twistQ3 (orient (A p) (B p))) ∧ (∀ p, IE1 (K p)) ∧
      EvenCycle (fun p => orient (A p) (B p)) := by
  sorry
  -- Bell data: NClass.bell_state with hgate; NClass.bell_effect with dualW_of_inv, NClass.ipW_map and hinv;
  -- cross relation: incl_I, incl_II, dualW_dualW, hcl;
  -- IE₁ of the closures: rotation links [X audit G6, L5; p3 G3–G4] and so3_euler;
  -- then reduction to sign-twisted aligned data [X f1 G1] and the aligned argument;
  -- orientation: bellOf_mem_twistQ3; parity [X f1 G2–G3]

/-- **Theorem D (closure level; no closedness).** Stated here for general charts; the aligned case drops
`hcls` and `hinv`. -/
theorem kt4_closure (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p) (h : FCC K) :
    closure (K .p01) = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, closure (K p) = twistQ3 (orient (A p) (B p))) ∧ (∀ p, IE1 (closure (K p))) ∧
      EvenCycle (fun p => orient (A p) (B p)) ∧ (∀ p, interior (closure (K p)) ⊆ K p) := by
  sorry
  -- ⊇ of the first conjunct: incl_I and dualW_dualW; ⊆: incl_II and isClosed_dualW (Θ a linear isomorphism);
  -- the interior sandwich: K p contains the full-dimensional separable cone and
  -- Convex.combo_interior_closure_subset_interior (Mathlib Analysis/Convex/Topology.lean:88)

/-- **Theorem A (forward; headline).** From H-KT4 (with H-KT4.tok) and H-eff through Lemma B1, and H-pairwise,
H-adm, H-gate, H-inv, H-NCLASS, H-closed: every pair cone is Q3 or the twin in its token charts, IE₁ holds for
every pair, and the 4-cycle of twist bits is even. -/
theorem kt4_forward (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hpair : ∀ p, ∃ (z : Fin 3 → ℝ) (n : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)),
      IsNot (eball 3) z n ∧ CtrlGate (eball 3) z n (N p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (H : KT4 (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∃ τ : Pr → Bool, (∀ p, K p = twistQ3 (τ p)) ∧ EvenCycle τ) ∧ (∀ p, IE1 (K p)) := by
  have h : FCC K := fourCopyCoherent_of_kt4 (hadm .p01) (hadm .p23) (hadm .p02) (hadm .p13) H
  obtain ⟨-, hK, hIE, hpar⟩ := kt4_general K N A B A' B' hcls hadm hcl hgate hinv h
  exact ⟨⟨fun p => orient (A p) (B p), hK, hpar⟩, hIE⟩
  -- `hpair` (H-pairwise) is the sourcing premise of `hcls` through EQ2-B's classification; it is not read once
  -- N-CLASS is carried as a hypothesis.

/-- **Corollary (IE₁ in the drive form).** -/
theorem kt4_forward_drive (K : Pr → Set (W 3)) (hIE : ∀ p, IE1 (K p)) : ∀ p, IE1Drive (K p) :=
  fun p => ie1Drive_of_ie1 (hIE p)

/-! ## Part E — remark, kept apart: not part of the package's theorem -/

/-- Realization witness, uniform quantum configuration (audit Q, P2): `PSD₁₆` carries both groupings. -/
theorem fcc_uniform_Q3 : FourCopyCoherent Q3 Q3 Q3 Q3 := by sorry
/-- Realization witness, uniform twin configuration (audit P2: `PT_{0,3}(PSD₁₆)`). -/
theorem fcc_uniform_twin : FourCopyCoherent twin twin twin twin := by sorry
/-- IE₁ without parity does not give the instance: Q3 on 01, 23, 02 and the twin on 13 (audit P1; f2 X3,
value −1/8). -/
theorem not_fcc_odd : ¬ FourCopyCoherent Q3 Q3 Q3 twin := by sorry

end

end FourCopy
end OIBridge
