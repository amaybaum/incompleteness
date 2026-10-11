/-
  OIBridge/BridgeReachDim.lean — design module of the research thread `research/bridge`
  (round 4, node B16). Not certified. Built on a disposable dev branch only; not for merge.

  B7-1 beyond the finite case. The conclusion of `ReachUnitary` and of `ReachAnti` (BridgeReach,
  round 3) holds for every subgroup of `U(4)` that countably many C¹ curves of matrices cover: in
  particular for every countable subgroup and, through the written link of NOTES-B16 §2, for every
  closed subgroup whose identity component has dimension at most one. The argument is a dimension
  count: the pair vectors that some element carries to a product lie in countably many C¹ images
  of `ℝ × ℂ³` (real dimension 7) in `ℂ⁴` (real dimension 8), so their complement is dense
  (Mathlib's `ContDiff.dimH_range_le` and `dense_compl_of_dimH_lt_finrank`).

  Proved here:
    §A  the products are covered by two C¹ charts of `ℂ³` (`kron2_mem_chart`, `charts_contDiff`);
    §B  the dimension lemma: countably many C¹ maps `ℝ × ℂ³ → ℂ⁴` miss a common vector
        (`exists_not_mem_ranges`), from `finrank_dom = 7` and `finrank_pvec = 8`;
    §C  the avoidance theorem for countably many C¹ curves (`avoid_of_curves`) and its coset form
        (`avoidA_of_curves`); the group statements under a countable C¹ cover
        (`reachUnitary_of_curveCover`, `reachAnti_of_curveCover`), with no condition on the coset;
        the reduction of `ReachUnitary` and `ReachAnti` to the existence of covers
        (`reachUnitary_of_covers`, `reachAnti_of_covers`); the countable case
        (`curveCover_of_countable`, `reachUnitary_countable`);
    §D  controls: on the controlled-phase circle `diag(1, 1, 1, e^{it})` the vector `(1, 2, 3, 5)`
        avoids the products at every `t` (`cz_avoids`), an explicit witness for a one-dimensional
        family; the identity of `ℂ⁴`, a C¹ map from a space of dimension 8, misses nothing
        (`ctl_dim_eight`), so the dimension gap is load-bearing.

  Every statement concerns orbits of pair vectors under groups of conjugations; none concerns the
  operational availability of an operation. Nothing here proves B7-1 for identity components of
  dimension two or more.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BridgeReach
import Mathlib.Topology.MetricSpace.HausdorffDimension
import Mathlib.Analysis.Calculus.ContDiff.Operations
import Mathlib.LinearAlgebra.Complex.FiniteDimensional
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace OIBridge
namespace BridgeReachDim

open Matrix BridgeReach
open scoped ENNReal

/-! ### §A — two charts of the products -/

/-- The chart `(1, x₀) ⊗ (x₁, x₂)`. -/
def chart0 (x : Fin 3 → ℂ) : PVec :=
  fun ij => (if ij.1 = 0 then 1 else x 0) * (if ij.2 = 0 then x 1 else x 2)

/-- The chart `(0, 1) ⊗ (x₁, x₂)`. -/
def chart1 (x : Fin 3 → ℂ) : PVec :=
  fun ij => (if ij.1 = 0 then 0 else 1) * (if ij.2 = 0 then x 1 else x 2)

/-- The two charts, indexed by `Bool`. -/
def charts (b : Bool) : (Fin 3 → ℂ) → PVec := cond b chart1 chart0

/-- **EVERY PRODUCT LIES IN A CHART.** -/
theorem kron2_mem_chart (a b : Fin 2 → ℂ) :
    ∃ x : Fin 3 → ℂ, kron2 a b = chart0 x ∨ kron2 a b = chart1 x := by
  by_cases h : a 0 = 0
  · refine ⟨fun k => if k = 1 then a 1 * b 0 else a 1 * b 1, Or.inr ?_⟩
    funext ij
    obtain ⟨i, j⟩ := ij
    fin_cases i <;> fin_cases j <;> simp [kron2, chart1, h]
  · have h' : a 0 ≠ 0 := h
    have e1 : a 1 / a 0 * (a 0 * b 0) = a 1 * b 0 := by
      first
      | (field_simp; done)
      | (field_simp; ring)
      | (rw [div_mul_eq_mul_div, div_eq_iff h']; ring)
    have e2 : a 1 / a 0 * (a 0 * b 1) = a 1 * b 1 := by
      first
      | (field_simp; done)
      | (field_simp; ring)
      | (rw [div_mul_eq_mul_div, div_eq_iff h']; ring)
    refine ⟨fun k => if k = 0 then a 1 / a 0 else if k = 1 then a 0 * b 0 else a 0 * b 1,
      Or.inl ?_⟩
    funext ij
    obtain ⟨i, j⟩ := ij
    fin_cases i <;> fin_cases j <;> simp [kron2, chart0, h', e1, e2] <;>
      first
      | (field_simp; done)
      | (field_simp; ring)
      | ring

theorem sel_contDiff (p : Prop) [Decidable p] (f g : (Fin 3 → ℂ) → ℂ) (hf : ContDiff ℝ 1 f)
    (hg : ContDiff ℝ 1 g) : ContDiff ℝ 1 (fun x => if p then f x else g x) := by
  by_cases h : p
  · simp only [if_pos h]
    exact hf
  · simp only [if_neg h]
    exact hg

theorem coord_contDiff (k : Fin 3) : ContDiff ℝ 1 (fun x : Fin 3 → ℂ => x k) :=
  contDiff_apply ℝ ℂ k

theorem chart0_contDiff (ij : Fin 2 × Fin 2) : ContDiff ℝ 1 (fun x : Fin 3 → ℂ => chart0 x ij) :=
  (sel_contDiff (ij.1 = 0) (fun _ => 1) (fun x => x 0) contDiff_const (coord_contDiff 0)).mul
    (sel_contDiff (ij.2 = 0) (fun x => x 1) (fun x => x 2) (coord_contDiff 1) (coord_contDiff 2))

theorem chart1_contDiff (ij : Fin 2 × Fin 2) : ContDiff ℝ 1 (fun x : Fin 3 → ℂ => chart1 x ij) :=
  (sel_contDiff (ij.1 = 0) (fun _ => 0) (fun _ => 1) contDiff_const contDiff_const).mul
    (sel_contDiff (ij.2 = 0) (fun x => x 1) (fun x => x 2) (coord_contDiff 1) (coord_contDiff 2))

theorem charts_contDiff (b : Bool) (ij : Fin 2 × Fin 2) :
    ContDiff ℝ 1 (fun x : Fin 3 → ℂ => charts b x ij) := by
  cases b
  · exact chart0_contDiff ij
  · exact chart1_contDiff ij

/-! ### §B — the dimension lemma -/

theorem finrank_dom : Module.finrank ℝ (ℝ × (Fin 3 → ℂ)) = 7 := by
  first
  | (simp [Module.finrank_prod, Module.finrank_pi_fintype, Complex.finrank_real_complex]; done)
  | (rw [Module.finrank_prod, Module.finrank_self, Module.finrank_pi_fintype]
     simp [Complex.finrank_real_complex])

theorem finrank_pvec : Module.finrank ℝ PVec = 8 := by
  first
  | (simp [Module.finrank_pi_fintype, Complex.finrank_real_complex]; done)
  | (rw [Module.finrank_pi_fintype]
     simp [Complex.finrank_real_complex])

/-- **COUNTABLY MANY C¹ MAPS FROM `ℝ × ℂ³` MISS A COMMON PAIR VECTOR.** -/
theorem exists_not_mem_ranges {ι : Type} [Countable ι] (Φ : ι → (ℝ × (Fin 3 → ℂ)) → PVec)
    (hΦ : ∀ i, ContDiff ℝ 1 (Φ i)) : ∃ v : PVec, ∀ i, v ∉ Set.range (Φ i) := by
  have hle : dimH (⋃ i, Set.range (Φ i)) ≤ ((7 : ℕ) : ℝ≥0∞) := by
    rw [dimH_iUnion]
    refine iSup_le fun i => ?_
    have h := (hΦ i).dimH_range_le
    rwa [finrank_dom] at h
  have hdim : dimH (⋃ i, Set.range (Φ i)) < (Module.finrank ℝ PVec : ℝ≥0∞) := by
    rw [finrank_pvec]
    first
    | exact hle.trans_lt (Nat.cast_lt.mpr (by norm_num))
    | exact hle.trans_lt (by norm_num)
  obtain ⟨v, hv⟩ := (dense_compl_of_dimH_lt_finrank hdim).nonempty
  exact ⟨v, fun i hi => hv (Set.mem_iUnion.mpr ⟨i, hi⟩)⟩

/-! ### §C — the avoidance theorems -/

/-- The map `(t, x) ↦ γ(t) · chart(x)`, coordinatewise. -/
def badMap (γ : ℝ → M4) (ch : (Fin 3 → ℂ) → PVec) (p : ℝ × (Fin 3 → ℂ)) : PVec :=
  fun i => ∑ j, γ p.1 i j * ch p.2 j

theorem badMap_eq (γ : ℝ → M4) (ch : (Fin 3 → ℂ) → PVec) (t : ℝ) (x : Fin 3 → ℂ) :
    badMap γ ch (t, x) = γ t *ᵥ ch x := rfl

theorem badMap_contDiff {γ : ℝ → M4} (hγ : ∀ i j, ContDiff ℝ 1 fun t => γ t i j)
    {ch : (Fin 3 → ℂ) → PVec} (hch : ∀ j, ContDiff ℝ 1 fun x => ch x j) :
    ContDiff ℝ 1 (badMap γ ch) := by
  refine contDiff_pi.2 fun i => ?_
  show ContDiff ℝ 1 fun p : ℝ × (Fin 3 → ℂ) => ∑ j, γ p.1 i j * ch p.2 j
  exact ContDiff.sum fun j _ => ((hγ i j).comp contDiff_fst).mul ((hch j).comp contDiff_snd)

/-- The coset map `(t, x) ↦ conj(L · γ(t) · chart(x))`. -/
def badMapA (L : M4) (γ : ℝ → M4) (ch : (Fin 3 → ℂ) → PVec) (p : ℝ × (Fin 3 → ℂ)) : PVec :=
  conjV (L *ᵥ badMap γ ch p)

theorem badMapA_contDiff (L : M4) {γ : ℝ → M4} (hγ : ∀ i j, ContDiff ℝ 1 fun t => γ t i j)
    {ch : (Fin 3 → ℂ) → PVec} (hch : ∀ j, ContDiff ℝ 1 fun x => ch x j) :
    ContDiff ℝ 1 (badMapA L γ ch) := by
  have hB := contDiff_pi.1 (badMap_contDiff hγ hch)
  refine contDiff_pi.2 fun i => ?_
  have hS : ContDiff ℝ 1 (fun p : ℝ × (Fin 3 → ℂ) => ∑ l, L i l * badMap γ ch p l) :=
    ContDiff.sum fun l _ => contDiff_const.mul (hB l)
  first
  | exact Complex.conjCLE.contDiff.comp hS
  | (convert Complex.conjCLE.contDiff.comp hS using 1
     funext p
     simp [badMapA, conjV, Matrix.mulVec, dotProduct, Complex.conjCLE_apply, Function.comp])

/-- **AVOIDANCE FOR COUNTABLY MANY C¹ CURVES**: some pair vector is no `γ_k(t) · (a ⊗ b)`. -/
theorem avoid_of_curves (γ : ℕ → ℝ → M4) (hγ : ∀ k i j, ContDiff ℝ 1 fun t => γ k t i j) :
    ∃ v : PVec, ∀ (k : ℕ) (t : ℝ) (a b : Fin 2 → ℂ), v ≠ γ k t *ᵥ kron2 a b := by
  obtain ⟨v, hv⟩ := exists_not_mem_ranges (ι := ℕ × Bool)
    (fun kb => badMap (γ kb.1) (charts kb.2))
    (fun kb => badMap_contDiff (hγ kb.1) (charts_contDiff kb.2))
  refine ⟨v, fun k t a b hvab => ?_⟩
  obtain ⟨x, hx | hx⟩ := kron2_mem_chart a b
  · refine hv (k, false) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
    show γ k t *ᵥ chart0 x = v
    rw [← hx, ← hvab]
  · refine hv (k, true) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
    show γ k t *ᵥ chart1 x = v
    rw [← hx, ← hvab]

/-- **AVOIDANCE ON A COSET**: some pair vector is no `conj(L · γ_k(t) · (a ⊗ b))`, and no
`γ_k(t) · (a ⊗ b)`. -/
theorem avoidA_of_curves (L : M4) (γ : ℕ → ℝ → M4)
    (hγ : ∀ k i j, ContDiff ℝ 1 fun t => γ k t i j) :
    ∃ v : PVec, ∀ (k : ℕ) (t : ℝ) (a b : Fin 2 → ℂ),
      v ≠ γ k t *ᵥ kron2 a b ∧ v ≠ conjV (L *ᵥ (γ k t *ᵥ kron2 a b)) := by
  obtain ⟨v, hv⟩ := exists_not_mem_ranges (ι := (ℕ × Bool) ⊕ (ℕ × Bool))
    (Sum.elim (fun kb => badMap (γ kb.1) (charts kb.2))
      (fun kb => badMapA L (γ kb.1) (charts kb.2)))
    (fun i => by
      cases i with
      | inl kb => exact badMap_contDiff (hγ kb.1) (charts_contDiff kb.2)
      | inr kb => exact badMapA_contDiff L (hγ kb.1) (charts_contDiff kb.2))
  refine ⟨v, fun k t a b => ⟨fun hvab => ?_, fun hvab => ?_⟩⟩
  · obtain ⟨x, hx | hx⟩ := kron2_mem_chart a b
    · refine hv (Sum.inl (k, false)) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
      show γ k t *ᵥ chart0 x = v
      rw [← hx, ← hvab]
    · refine hv (Sum.inl (k, true)) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
      show γ k t *ᵥ chart1 x = v
      rw [← hx, ← hvab]
  · obtain ⟨x, hx | hx⟩ := kron2_mem_chart a b
    · refine hv (Sum.inr (k, false)) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
      show conjV (L *ᵥ (γ k t *ᵥ chart0 x)) = v
      rw [← hx, ← hvab]
    · refine hv (Sum.inr (k, true)) (Set.mem_range.mpr ⟨(t, x), ?_⟩)
      show conjV (L *ᵥ (γ k t *ᵥ chart1 x)) = v
      rw [← hx, ← hvab]

/-- **A COUNTABLE C¹ CURVE COVER** of a subgroup: countably many C¹ curves of matrices whose union
contains every element. -/
def CurveCover (H : Subgroup U4) : Prop :=
  ∃ γ : ℕ → ℝ → M4, (∀ k i j, ContDiff ℝ 1 fun t => γ k t i j) ∧
    ∀ h ∈ H, ∃ (k : ℕ) (t : ℝ), γ k t = (h : M4)

theorem inv_mul_val (h : U4) : ((h⁻¹ : U4) : M4) * (h : M4) = 1 :=
  congrArg Subtype.val (inv_mul_cancel h)

theorem kron2_zero : kron2 0 0 = 0 := by
  funext ij
  simp [kron2]

/-- **B7-1 UNDER A CURVE COVER, UNITARY GROUPS**: the conclusion of `ReachUnitary`. -/
theorem reachUnitary_of_curveCover (H : Subgroup U4) (hH : CurveCover H) :
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) := by
  obtain ⟨γ, hγ, hcov⟩ := hH
  obtain ⟨v, hv⟩ := avoid_of_curves γ hγ
  have key : ∀ h ∈ H, ∀ a b : Fin 2 → ℂ, (h : M4) *ᵥ v ≠ kron2 a b := by
    intro h hh a b hab
    obtain ⟨k, t, hkt⟩ := hcov h⁻¹ (H.inv_mem hh)
    apply hv k t a b
    rw [hkt, ← hab, Matrix.mulVec_mulVec, inv_mul_val, Matrix.one_mulVec]
  refine ⟨v, fun hv0 => key 1 H.one_mem 0 0 ?_, fun h hh a b => key h hh a b⟩
  rw [hv0, Matrix.mulVec_zero, kron2_zero]

/-- **B7-1 UNDER A CURVE COVER, WITH AN ANTIUNITARY COSET**: the conclusion of `ReachAnti`, with no
condition on the coset. -/
theorem reachAnti_of_curveCover (H : Subgroup U4) (K : U4) (hH : CurveCover H) :
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) ∧
      AvoidsProducts v (fun u => ((h : M4) * (K : M4)) *ᵥ conjV u) := by
  obtain ⟨γ, hγ, hcov⟩ := hH
  obtain ⟨v, hv⟩ := avoidA_of_curves (star (K : M4)) γ hγ
  have hK1 : star (K : M4) * (K : M4) = 1 := by
    first
    | exact unitary.star_mul_self_of_mem K.2
    | exact (Matrix.mem_unitaryGroup_iff'.mp K.2)
  have keyA : ∀ h ∈ H, ∀ a b : Fin 2 → ℂ, (h : M4) *ᵥ v ≠ kron2 a b := by
    intro h hh a b hab
    obtain ⟨k, t, hkt⟩ := hcov h⁻¹ (H.inv_mem hh)
    apply (hv k t a b).1
    rw [hkt, ← hab, Matrix.mulVec_mulVec, inv_mul_val, Matrix.one_mulVec]
  have keyB : ∀ h ∈ H, ∀ a b : Fin 2 → ℂ, ((h : M4) * (K : M4)) *ᵥ conjV v ≠ kron2 a b := by
    intro h hh a b hab
    obtain ⟨k, t, hkt⟩ := hcov h⁻¹ (H.inv_mem hh)
    apply (hv k t a b).2
    have hprod : star (K : M4) * ((h⁻¹ : U4) : M4) * ((h : M4) * (K : M4)) = 1 := by
      rw [Matrix.mul_assoc, ← Matrix.mul_assoc ((h⁻¹ : U4) : M4), inv_mul_val, Matrix.one_mul,
        hK1]
    have hc : conjV v = star (K : M4) *ᵥ (((h⁻¹ : U4) : M4) *ᵥ kron2 a b) := by
      calc conjV v = (star (K : M4) * ((h⁻¹ : U4) : M4) * ((h : M4) * (K : M4))) *ᵥ conjV v := by
            rw [hprod, Matrix.one_mulVec]
        _ = star (K : M4) *ᵥ (((h⁻¹ : U4) : M4) *ᵥ (((h : M4) * (K : M4)) *ᵥ conjV v)) := by
            simp only [Matrix.mulVec_mulVec, Matrix.mul_assoc]
        _ = star (K : M4) *ᵥ (((h⁻¹ : U4) : M4) *ᵥ kron2 a b) := by rw [hab]
    rw [hkt, ← hc, conjV_conjV]
  refine ⟨v, fun hv0 => keyA 1 H.one_mem 0 0 ?_,
    fun h hh => ⟨fun a b => keyA h hh a b, fun a b => keyB h hh a b⟩⟩
  rw [hv0, Matrix.mulVec_zero, kron2_zero]

/-- `ReachUnitary` follows from the existence of covers for its subgroups. -/
theorem reachUnitary_of_covers
    (hcov : ∀ H : Subgroup U4, IsClosed (H : Set U4) → IdCompComm H → CurveCover H) :
    ReachUnitary :=
  fun H hc hid => reachUnitary_of_curveCover H (hcov H hc hid)

/-- `ReachAnti` follows from the existence of covers for its subgroups. -/
theorem reachAnti_of_covers
    (hcov : ∀ H : Subgroup U4, IsClosed (H : Set U4) → IdCompComm H → CurveCover H) :
    ReachAnti :=
  fun H K hc hid _ _ => reachAnti_of_curveCover H K (hcov H hc hid)

/-- **A COUNTABLE SUBGROUP HAS A CURVE COVER**, by constant curves. -/
theorem curveCover_of_countable (H : Subgroup U4) (hc : (H : Set U4).Countable) :
    CurveCover H := by
  obtain ⟨f, hf⟩ := hc.exists_eq_range ⟨1, H.one_mem⟩
  refine ⟨fun k _ => ((f k : U4) : M4), fun k i j => contDiff_const, fun h hh => ?_⟩
  have hh' : h ∈ (H : Set U4) := hh
  rw [hf] at hh'
  obtain ⟨k, hk⟩ := hh'
  exact ⟨k, 0, congrArg Subtype.val hk⟩

/-- **B7-1 FOR COUNTABLE SUBGROUPS**, by the dimension count (the finite case of round 3 included). -/
theorem reachUnitary_countable (H : Subgroup U4) (hc : (H : Set U4).Countable) :
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) :=
  reachUnitary_of_curveCover H (curveCover_of_countable H hc)

/-! ### §D — controls -/

/-- `e^{it}`. -/
noncomputable def czE (t : ℝ) : ℂ := (Real.cos t : ℂ) + (Real.sin t : ℂ) * Complex.I

/-- The controlled phase `diag(1, 1, 1, e^{it})`. -/
noncomputable def czMat (t : ℝ) : M4 :=
  Matrix.diagonal fun ij => if ij = ((1 : Fin 2), (1 : Fin 2)) then czE t else 1

theorem czE_contDiff : ContDiff ℝ 1 czE := by
  have hc : ContDiff ℝ 1 (fun t : ℝ => (Real.cos t : ℂ)) :=
    Complex.ofRealCLM.contDiff.comp Real.contDiff_cos
  have hs : ContDiff ℝ 1 (fun t : ℝ => (Real.sin t : ℂ)) :=
    Complex.ofRealCLM.contDiff.comp Real.contDiff_sin
  exact hc.add (hs.mul contDiff_const)

/-- The controlled-phase circle is a C¹ curve. -/
theorem cz_entry_contDiff (i j : Fin 2 × Fin 2) : ContDiff ℝ 1 fun t => czMat t i j := by
  by_cases hij : i = j
  · subst hij
    by_cases h11 : i = ((1 : Fin 2), (1 : Fin 2))
    · simp only [czMat, Matrix.diagonal_apply_eq, if_pos h11]
      exact czE_contDiff
    · simp only [czMat, Matrix.diagonal_apply_eq, if_neg h11]
      exact contDiff_const
  · simp only [czMat, Matrix.diagonal_apply_ne _ hij]
    exact contDiff_const

theorem cz_prodDet (t : ℝ) : prodDet (czMat t *ᵥ ctlV) = 5 * czE t - 6 := by
  simp [prodDet, czMat, Matrix.mulVec_diagonal, ctlV] <;> ring

/-- **POSITIVE CONTROL**: the vector `(1, 2, 3, 5)` avoids the products on the whole controlled-phase
circle: `prodDet = 5 e^{it} − 6`, whose real part is at most `−1`. -/
theorem cz_avoids (t : ℝ) : AvoidsProducts ctlV (fun u => czMat t *ᵥ u) := by
  apply avoids_of_prodDet
  show prodDet (czMat t *ᵥ ctlV) ≠ 0
  rw [cz_prodDet]
  intro h
  have hre := congrArg Complex.re h
  simp [czE] at hre
  have hcos := Real.cos_le_one t
  linarith

/-- **COUNTERCONTROL**: the identity of `ℂ⁴` is a C¹ map from a space of real dimension 8 whose range
is everything, so no vector avoids it; the gap `7 < 8` is load-bearing. -/
theorem ctl_dim_eight :
    ContDiff ℝ 1 (fun v : PVec => v) ∧ ∀ v : PVec, v ∈ Set.range (fun v : PVec => v) :=
  ⟨contDiff_id, fun v => Set.mem_range.mpr ⟨v, rfl⟩⟩

#print axioms kron2_mem_chart
#print axioms sel_contDiff
#print axioms coord_contDiff
#print axioms chart0_contDiff
#print axioms chart1_contDiff
#print axioms charts_contDiff
#print axioms finrank_dom
#print axioms finrank_pvec
#print axioms exists_not_mem_ranges
#print axioms badMap_eq
#print axioms badMap_contDiff
#print axioms badMapA_contDiff
#print axioms avoid_of_curves
#print axioms avoidA_of_curves
#print axioms inv_mul_val
#print axioms kron2_zero
#print axioms reachUnitary_of_curveCover
#print axioms reachAnti_of_curveCover
#print axioms reachUnitary_of_covers
#print axioms reachAnti_of_covers
#print axioms curveCover_of_countable
#print axioms reachUnitary_countable
#print axioms czE_contDiff
#print axioms cz_entry_contDiff
#print axioms cz_prodDet
#print axioms cz_avoids
#print axioms ctl_dim_eight

end BridgeReachDim
end OIBridge
