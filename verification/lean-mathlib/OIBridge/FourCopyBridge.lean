/-
  OIBridge/FourCopyBridge.lean — design (EQ4-F), not adopted: Lemma R and Lemma B1 of the
  four-copy package. Every proof in this file is complete.

  * O1, O3: the four-copy contraction read on targets `01` and `02` (`fourVal_eq_01`,
    `fourVal_eq_02`); Lemma R at target `02` (`FourCopyCoherent.target02`).
  * B1a (O20 restated): every entry of a maximal-cone table is bounded by its unit entry
    (`abs_le_00_of_maxCone`); O20 as stated (`abs_le_one_of_maxCone`).
  * O21: a dual-cone table is a positive multiple of an effect of the normalized pair body
    (`exists_effect_of_dualW`).
  * B1 over `KT4Core` (`fourCopyCoherent_of_kt4Core`). Its hypotheses are the maximal-cone bound
    and nonnegative scaling of each pair cone, and the fields of `KT4Core`; `KT4.toCore` derives
    those fields from `KT4`, reading `prod_mem`, `prodEff_effect` (lower bound), `prodEff_apply`,
    `one_body` and `tok`. O22 (`fourCopyCoherent_of_kt4`) is the corollary for `KT4`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyCore

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody CompositeInterface

noncomputable section

variable {K01 K23 K02 K13 : Set (W 3)}

/-! ### §A — Lemma R (O1, O3) -/

set_option maxHeartbeats 4000000 in
/-- O1: the contraction read on target `01`. -/
theorem fourVal_eq_01 (X Y E F : W 3) :
    fourVal X Y E F = ipW X (tabMul (tabMul E Y) (tabT F)) := by
  simp only [fourVal, ipW, tabMul, tabT, sum_univ_four']
  ring

set_option maxHeartbeats 4000000 in
/-- O3: the contraction read on target `02`. -/
theorem fourVal_eq_02 (X Y E F : W 3) :
    fourVal X Y E F = ipW E (tabMul (tabMul X F) (tabT Y)) := by
  simp only [fourVal, ipW, tabMul, tabT, sum_univ_four']
  ring

/-- Lemma R, target `02`: the `01` and `23` tables act as links. -/
theorem FourCopyCoherent.target02 (h : FourCopyCoherent K01 K23 K02 K13) :
    PairLinked K02 K13 K01 K23 where
  upper X hX Y hY E hE F hF := by
    have h1 := h.famII X hX Y hY E hE F hF
    rwa [← fourVal_eq_01, fourVal_eq_02] at h1
  lower L hL L' hL' e he f hf := by
    have h1 := h.famI L hL L' hL' e he f hf
    rwa [← fourVal_eq_01, fourVal_eq_02] at h1

/-! ### §B — B1a: entries of a maximal-cone table -/

/-- The corner vectors `e₀ + s eμ` are in the homogenized cone of the ball for `s² ≤ 1`. -/
theorem lor_bvec_zero_add {d : ℕ} (μ : Fin (d + 1)) {s : ℝ} (hs : s ^ 2 ≤ 1) :
    Lor (bvec (0 : Fin (d + 1)) + s • bvec μ) := by
  rcases Fin.eq_zero_or_eq_succ μ with h | ⟨j, rfl⟩
  · subst h
    have h1 : Lor ((1 + s) • hom (0 : Fin d → ℝ)) := lor_smul lor_hom_zero (by nlinarith)
    rw [← bvec_zero_eq, add_smul, one_smul] at h1
    exact h1
  · rw [bvec_zero_eq]
    exact lor_hom_zero_add_smul_bvec j hs

/-- The pairing of two basis vectors reads one entry. -/
theorem pairVal_bvec_bvec {d : ℕ} (μ ν : Fin (d + 1)) (ω : W d) :
    pairVal (bvec μ) (bvec ν) ω = ω μ ν := by
  rw [pairVal_bvec]
  simp only [bvec_apply, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_ite_eq]
  simp

/-- The pairing of two corner vectors. -/
theorem pairVal_corner {d : ℕ} (μ ν : Fin (d + 1)) (s t : ℝ) (ω : W d) :
    pairVal (bvec 0 + s • bvec μ) (bvec 0 + t • bvec ν) ω =
      ω 0 0 + t * ω 0 ν + s * ω μ 0 + s * t * ω μ ν := by
  simp only [pairVal_add_left, pairVal_add_right, pairVal_smul_left, pairVal_smul_right,
    pairVal_bvec_bvec]
  ring

/-- **B1a.** On DIM-1's maximal cone every entry is bounded by the unit entry. -/
theorem abs_le_00_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (μ ν : Fin (3 + 1)) :
    |ω μ ν| ≤ ω 0 0 := by
  have key : ∀ s t : ℝ, s ^ 2 ≤ 1 → t ^ 2 ≤ 1 →
      0 ≤ ω 0 0 + t * ω 0 ν + s * ω μ 0 + s * t * ω μ ν := by
    intro s t hs ht
    rw [← pairVal_corner μ ν s t ω]
    exact pairVal_nonneg_of_maxCone hω (lor_bvec_zero_add μ hs) (lor_bvec_zero_add ν ht)
  have h1 := key 1 1 (by norm_num) (by norm_num)
  have h2 := key (-1) (-1) (by norm_num) (by norm_num)
  have h3 := key 1 (-1) (by norm_num) (by norm_num)
  have h4 := key (-1) 1 (by norm_num) (by norm_num)
  rw [abs_le]
  constructor <;> linarith

theorem nonneg_00_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) : 0 ≤ ω 0 0 :=
  (abs_nonneg _).trans (abs_le_00_of_maxCone hω 0 0)

/-- A maximal-cone table with vanishing unit entry vanishes. -/
theorem eq_zero_of_maxCone_00 {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (h : ω 0 0 = 0) :
    ω = 0 := by
  funext μ ν
  have hb := abs_le_00_of_maxCone hω μ ν
  rw [h] at hb
  exact abs_nonpos_iff.1 hb

/-- O20: the normalized slice of the maximal cone is bounded. -/
theorem abs_le_one_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (h00 : ω 0 0 = 1)
    (μ ν : Fin 4) : |ω μ ν| ≤ 1 := by
  have h := abs_le_00_of_maxCone hω μ ν
  rwa [h00] at h

/-! ### §C — the flat chart -/

theorem tabCoord_flatW (μ ν : Fin (3 + 1)) (ω : W 3) : tabCoord μ ν (flatW ω) = ω μ ν := by
  simp only [tabCoord, coord_apply, flatW, Equiv.symm_apply_apply]

theorem tabEff_flatW (E ω : W 3) : tabEff E (flatW ω) = ipW E ω := by
  unfold tabEff ipW
  rw [affine_sum_apply]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [affine_sum_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, tabCoord_flatW]

/-- The expansion of a bilinear product effect on two table functionals. -/
theorem bilin_tabEff {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (D : ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin 16 → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ))
    (E F : W 3) (ω : V) :
    D (tabEff E) (tabEff F) ω =
      ∑ a, ∑ c, ∑ b, ∑ d, E a c * F b d * D (tabCoord a c) (tabCoord b d) ω := by
  simp only [tabEff, map_sum, LinearMap.map_smul, LinearMap.sum_apply, LinearMap.smul_apply,
    affine_sum_apply, AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun c _ =>
    Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun d _ => ?_
  ring

/-! ### §D — O21: dual-cone tables are effects up to a positive scale -/

/-- **O21.** Every dual-cone table of a cone inside the maximal cone is a positive multiple of an
`IsEffectOn` effect of the normalized pair body: scale `1 / (1 + Σ |E μ ν|)`. -/
theorem exists_effect_of_dualW {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3)) {E : W 3}
    (hE : E ∈ dualW K) : ∃ c : ℝ, 0 < c ∧ IsEffectOn (pairBody K) (c • tabEff E) := by
  obtain ⟨M, hMdef⟩ : ∃ M : ℝ, M = ∑ μ, ∑ ν, |E μ ν| := ⟨_, rfl⟩
  have hM : 0 ≤ M := by
    rw [hMdef]
    exact Finset.sum_nonneg fun _ _ => Finset.sum_nonneg fun _ _ => abs_nonneg _
  have hpos : 0 < M + 1 := by linarith
  have hc : 0 < 1 / (M + 1) := one_div_pos.mpr hpos
  refine ⟨1 / (M + 1), hc, ?_⟩
  rintro _ ⟨ω, ⟨hωK, h00⟩, rfl⟩
  rw [AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, tabEff_flatW]
  have hnn : 0 ≤ ipW E ω := mem_dualW.1 hE ω hωK
  have hle : ipW E ω ≤ M := by
    rw [hMdef]
    unfold ipW
    refine Finset.sum_le_sum fun μ _ => Finset.sum_le_sum fun ν _ => ?_
    have hb := abs_le_one_of_maxCone (hK hωK) h00 μ ν
    calc E μ ν * ω μ ν ≤ |E μ ν * ω μ ν| := le_abs_self _
      _ = |E μ ν| * |ω μ ν| := abs_mul _ _
      _ ≤ |E μ ν| * 1 := mul_le_mul_of_nonneg_left hb (abs_nonneg _)
      _ = |E μ ν| := mul_one _
  refine ⟨mul_nonneg hc.le hnn, ?_⟩
  calc 1 / (M + 1) * ipW E ω ≤ 1 / (M + 1) * (M + 1) :=
        mul_le_mul_of_nonneg_left (by linarith) hc.le
    _ = 1 := one_div_mul_cancel (ne_of_gt hpos)

/-! ### §E — scalar bookkeeping -/

/-- A positive rescaling of a cone table into the normalized pair body. -/
theorem flatW_mem_pairBody {K : Set (W 3)} (hK : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    {X : W 3} (hX : X ∈ K) (hp : 0 < X 0 0) : flatW ((X 0 0)⁻¹ • X) ∈ pairBody K :=
  ⟨(X 0 0)⁻¹ • X, ⟨hK _ (inv_nonneg.2 hp.le) X hX, by
    simp only [Pi.smul_apply, smul_eq_mul]
    exact inv_mul_cancel₀ hp.ne'⟩, rfl⟩

theorem fourVal_smul (a b : ℝ) (X Y E F : W 3) :
    fourVal (a • X) (b • Y) E F = a * b * fourVal X Y E F := by
  simp only [fourVal, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => ?_
  ring

theorem fourVal_smul_eff (a b : ℝ) (X Y E F : W 3) :
    fourVal X Y (a • E) (b • F) = a * b * fourVal X Y E F := by
  simp only [fourVal, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => ?_
  ring

theorem fourVal_zero_left (Y E F : W 3) : fourVal 0 Y E F = 0 := by simp [fourVal]

theorem fourVal_zero_right (X E F : W 3) : fourVal X 0 E F = 0 := by simp [fourVal]

theorem fourVal_zero_eff_left (X Y F : W 3) : fourVal X Y 0 F = 0 := by simp [fourVal]

theorem fourVal_zero_eff_right (X Y E : W 3) : fourVal X Y E 0 = 0 := by simp [fourVal]

/-! ### §F — the consumed core -/

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- `KT4` gives the core: the products of one grouping lie in the common body, on which the
product effects of the other grouping are effects; token coherence holds on the body. -/
def KT4.toCore (H : KT4 K01 K23 K02 K13 V) : KT4Core K01 K23 K02 K13 V where
  stA := H.PA.prodState
  stB := H.PB.prodState
  effA := H.PA.prodEff
  effB := H.PB.prodEff
  effA_apply := H.PA.prodEff_apply
  effB_apply := H.PB.prodEff_apply
  posBA e f he hf x hx y hy :=
    (H.PB.prodEff_effect e f he hf _ (by rw [← H.one_body]; exact H.PA.prod_mem x hx y hy)).1
  posAB e f he hf x hx y hy :=
    (H.PA.prodEff_effect e f he hf _ (by rw [H.one_body]; exact H.PB.prod_mem x hx y hy)).1
  tokA a b c d x hx y hy := H.tok a b c d _ (H.PA.prod_mem x hx y hy)
  tokB a b c d x hx y hy :=
    H.tok a b c d _ (by rw [H.one_body]; exact H.PB.prod_mem x hx y hy)

/-- The form with local tomography gives the core by forgetting `lt`. -/
def KT4LT.toCore (H : KT4LT K01 K23 K02 K13 V) : KT4Core K01 K23 K02 K13 V :=
  H.toKT4.toCore

/-! ### §G — Lemma B1 -/

/-- Family I's value: a product effect of the `02|13` grouping, built from tables, on a product
state of the `01|23` grouping, is the four-copy contraction (token coherence of `01|23` states). -/
theorem core_valI (H : KT4Core K01 K23 K02 K13 V) {x y : W 3}
    (hx : flatW x ∈ pairBody K01) (hy : flatW y ∈ pairBody K23) (E F : W 3) :
    H.effB (tabEff E) (tabEff F) (H.stA (flatW x) (flatW y)) = fourVal x y E F := by
  rw [bilin_tabEff]
  unfold fourVal
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun c _ =>
    Finset.sum_congr rfl fun d _ => ?_
  rw [← H.tokA a b c d _ hx _ hy, H.effA_apply, tabCoord_flatW, tabCoord_flatW]
  ring

/-- Family II's value (token coherence of `02|13` states). -/
theorem core_valII (H : KT4Core K01 K23 K02 K13 V) {l l' : W 3}
    (hl : flatW l ∈ pairBody K02) (hl' : flatW l' ∈ pairBody K13) (e f : W 3) :
    H.effA (tabEff e) (tabEff f) (H.stB (flatW l) (flatW l')) = fourVal e f l l' := by
  rw [bilin_tabEff]
  unfold fourVal
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun d _ => ?_
  rw [H.tokB a b c d _ hl _ hl', H.effB_apply, tabCoord_flatW, tabCoord_flatW]
  ring

/-- **Lemma B1 over the consumed core.** The maximal-cone bound and nonnegative scaling of each
pair cone, with the fields of `KT4Core`, give the four-copy interface. -/
theorem fourCopyCoherent_of_kt4Core
    (m01 : K01 ⊆ maxCone (eball 3)) (m23 : K23 ⊆ maxCone (eball 3))
    (m02 : K02 ⊆ maxCone (eball 3)) (m13 : K13 ⊆ maxCone (eball 3))
    (s01 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K01, c • ω ∈ K01)
    (s23 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K23, c • ω ∈ K23)
    (s02 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K02, c • ω ∈ K02)
    (s13 : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K13, c • ω ∈ K13)
    (H : KT4Core K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 where
  famI X hX Y hY E hE F hF := by
    rw [← fourVal_eq_01]
    by_cases hX0 : X 0 0 = 0
    · simp only [eq_zero_of_maxCone_00 (m01 hX) hX0, fourVal_zero_left, le_refl]
    by_cases hY0 : Y 0 0 = 0
    · simp only [eq_zero_of_maxCone_00 (m23 hY) hY0, fourVal_zero_right, le_refl]
    have hXp : 0 < X 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (m01 hX)) (Ne.symm hX0)
    have hYp : 0 < Y 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (m23 hY)) (Ne.symm hY0)
    obtain ⟨cE, hcE, heE⟩ := exists_effect_of_dualW m02 hE
    obtain ⟨cF, hcF, heF⟩ := exists_effect_of_dualW m13 hF
    have hx := flatW_mem_pairBody s01 hX hXp
    have hy := flatW_mem_pairBody s23 hY hYp
    have h0 := H.posBA _ _ heE heF _ hx _ hy
    have h1 : H.effB (cE • tabEff E) (cF • tabEff F)
        (H.stA (flatW ((X 0 0)⁻¹ • X)) (flatW ((Y 0 0)⁻¹ • Y))) =
          cE * cF * ((X 0 0)⁻¹ * (Y 0 0)⁻¹) * fourVal X Y E F := by
      simp only [LinearMap.map_smul, LinearMap.smul_apply, AffineMap.coe_smul, Pi.smul_apply,
        smul_eq_mul]
      rw [core_valI H hx hy, fourVal_smul]
      ring
    rw [h1] at h0
    exact (mul_nonneg_iff_of_pos_left
      (mul_pos (mul_pos hcE hcF) (mul_pos (inv_pos.2 hXp) (inv_pos.2 hYp)))).1 h0
  famII L hL L' hL' e he f hf := by
    rw [← fourVal_eq_01]
    by_cases hL0 : L 0 0 = 0
    · simp only [eq_zero_of_maxCone_00 (m02 hL) hL0, fourVal_zero_eff_left, le_refl]
    by_cases hL0' : L' 0 0 = 0
    · simp only [eq_zero_of_maxCone_00 (m13 hL') hL0', fourVal_zero_eff_right, le_refl]
    have hLp : 0 < L 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (m02 hL)) (Ne.symm hL0)
    have hLp' : 0 < L' 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (m13 hL')) (Ne.symm hL0')
    obtain ⟨ce, hce, hee⟩ := exists_effect_of_dualW m01 he
    obtain ⟨cf, hcf, hef⟩ := exists_effect_of_dualW m23 hf
    have hl := flatW_mem_pairBody s02 hL hLp
    have hl' := flatW_mem_pairBody s13 hL' hLp'
    have h0 := H.posAB _ _ hee hef _ hl _ hl'
    have h1 : H.effA (ce • tabEff e) (cf • tabEff f)
        (H.stB (flatW ((L 0 0)⁻¹ • L)) (flatW ((L' 0 0)⁻¹ • L'))) =
          ce * cf * ((L 0 0)⁻¹ * (L' 0 0)⁻¹) * fourVal e f L L' := by
      simp only [LinearMap.map_smul, LinearMap.smul_apply, AffineMap.coe_smul, Pi.smul_apply,
        smul_eq_mul]
      rw [core_valII H hl hl', fourVal_smul_eff]
      ring
    rw [h1] at h0
    exact (mul_nonneg_iff_of_pos_left
      (mul_pos (mul_pos hce hcf) (mul_pos (inv_pos.2 hLp) (inv_pos.2 hLp')))).1 h0

/-- **O22 (Lemma B1) for `KT4`.** Admissible pair cones and KT(4) give the four-copy interface. -/
theorem fourCopyCoherent_of_kt4 (a01 : PairAdm K01) (a23 : PairAdm K23) (a02 : PairAdm K02)
    (a13 : PairAdm K13) (H : KT4 K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 :=
  fourCopyCoherent_of_kt4Core a01.1.2 a23.1.2 a02.1.2 a13.1.2 a01.2.2 a23.2.2 a02.2.2 a13.2.2
    H.toCore

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.fourVal_eq_01
#print axioms OIBridge.FourCopy.fourVal_eq_02
#print axioms OIBridge.FourCopy.FourCopyCoherent.target02
#print axioms OIBridge.FourCopy.abs_le_00_of_maxCone
#print axioms OIBridge.FourCopy.eq_zero_of_maxCone_00
#print axioms OIBridge.FourCopy.abs_le_one_of_maxCone
#print axioms OIBridge.FourCopy.tabEff_flatW
#print axioms OIBridge.FourCopy.bilin_tabEff
#print axioms OIBridge.FourCopy.exists_effect_of_dualW
#print axioms OIBridge.FourCopy.KT4.toCore
#print axioms OIBridge.FourCopy.core_valI
#print axioms OIBridge.FourCopy.core_valII
#print axioms OIBridge.FourCopy.fourCopyCoherent_of_kt4Core
#print axioms OIBridge.FourCopy.fourCopyCoherent_of_kt4
