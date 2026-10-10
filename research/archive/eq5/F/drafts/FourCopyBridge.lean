/-
  DRAFT — UNBUILT (EQ4-F proof development, design only; not adopted, not for any branch as is).

  Proofs for the bridge layer of the four-copy package, written against the statement layer at
  `f0d37906` (`FourCopyPackage.lean`) and the COMP-1 interface at the certified base
  (`CompositeInterface.lean`). No Lean toolchain was available: nothing here has been elaborated, and
  the points most likely to need iteration are marked `-- ITER:`.

  Contents:
  * B1a `abs_le_00_of_maxCone` (the restated O20) and its corollaries `nonneg_00_of_maxCone`,
    `eq_zero_of_maxCone_00`, and O20 as stated;
  * B1d `tabCoord_flatW`;
  * O21 `exists_effect_of_dualW`;
  * O1 `fourVal_eq_01`;
  * SC7 `KT4Core`, `KT4.toCore`, `KT4LT.toCore`;
  * B1 `fourCopyCoherent_of_kt4Core`, and O22 `fourCopyCoherent_of_kt4` as its corollary.

  Hypotheses read by B1: `PairAdm` (the maximal-cone half of `CandidateCone` and the cone half of
  `IsConvexCone`) and the `KT4Core` fields. Not read: `PreComposite.convex`, `prodEff_unit`,
  `prodState_combo_left/right`, `Composite.lt`, closedness, gates.
-/
import OIBridge.FourCopyPackage

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations CompositeInterface

noncomputable section

variable {K01 K23 K02 K13 : Set (W 3)}

/-! ### B1a — the entries of a maximal-cone table are bounded by its unit entry -/

/-- **B1a.** On DIM-1's maximal cone every entry is bounded by the unit entry. Witnesses: the
pairings against `(1, ±e_μ) ⊗ (1, ±e_ν)` (or the unit vector when the index is `0`). -/
theorem abs_le_00_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (μ ν : Fin 4) :
    |ω μ ν| ≤ ω 0 0 := by
  have key : ∀ s t : ℝ, s ^ 2 ≤ 1 → t ^ 2 ≤ 1 →
      0 ≤ pairVal (fun κ : Fin 4 => if κ = 0 then (1 : ℝ) else if κ = μ then s else 0)
        (fun κ : Fin 4 => if κ = 0 then (1 : ℝ) else if κ = ν then t else 0) ω := by
    intro s t hs ht
    -- ITER: the four Lorentz side conditions after `fin_cases`; `simp` should decide the `if`s.
    refine pairVal_nonneg_of_maxCone hω (lor_of_three ?_ ?_) (lor_of_three ?_ ?_) <;>
      fin_cases μ <;> fin_cases ν <;> simp <;> nlinarith
  have h1 := key 1 1 (by norm_num) (by norm_num)
  have h2 := key (-1) (-1) (by norm_num) (by norm_num)
  have h3 := key 1 (-1) (by norm_num) (by norm_num)
  have h4 := key (-1) 1 (by norm_num) (by norm_num)
  -- ITER: `pairVal` unfolds to a double sum over `Fin (3 + 1)`; `sum_univ_four'` expands it.
  fin_cases μ <;> fin_cases ν <;>
    simp only [pairVal, sum_univ_four'] at h1 h2 h3 h4 <;> norm_num at h1 h2 h3 h4 <;>
    exact abs_le.2 ⟨by linarith, by linarith⟩

theorem nonneg_00_of_maxCone {ω : W 3} (hω : ω ∈ maxCone (eball 3)) : 0 ≤ ω 0 0 :=
  (abs_nonneg _).trans (abs_le_00_of_maxCone hω 0 0)

/-- A maximal-cone table with vanishing unit entry vanishes. -/
theorem eq_zero_of_maxCone_00 {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (h : ω 0 0 = 0) : ω = 0 := by
  funext μ ν
  have hb := abs_le_00_of_maxCone hω μ ν
  rw [h] at hb
  exact abs_nonpos_iff.1 hb

/-- O20 as stated in the package, from B1a. -/
theorem abs_le_one_of_maxCone' {ω : W 3} (hω : ω ∈ maxCone (eball 3)) (h00 : ω 0 0 = 1)
    (μ ν : Fin 4) : |ω μ ν| ≤ 1 :=
  h00 ▸ abs_le_00_of_maxCone hω μ ν

/-! ### B1d — coordinates of the flat chart -/

theorem tabCoord_flatW (μ ν : Fin 4) (ω : W 3) : tabCoord μ ν (flatW ω) = ω μ ν := by
  -- ITER: `finProdFinEquiv.symm_apply_apply` at the index `finProdFinEquiv (μ, ν)`.
  simp [tabCoord, flatW, coord_apply]

theorem tableEff_apply (E ω : W 3) :
    (∑ μ, ∑ ν, E μ ν • tabCoord μ ν) (flatW ω) = ipW E ω := by
  rw [affine_sum_apply]
  refine Finset.sum_congr rfl fun μ _ => ?_
  rw [affine_sum_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, tabCoord_flatW]

/-! ### O21 — dual-cone tables are effects up to a positive scale -/

/-- **O21.** Every dual-cone table is a positive multiple of an `IsEffectOn` effect of the normalized
pair body: scale `1 / (1 + Σ |E μ ν|)`, using B1a on the normalized slice. -/
theorem exists_effect_of_dualW {K : Set (W 3)} (hK : CandidateCone K) {E : W 3}
    (hE : E ∈ dualW K) :
    ∃ c : ℝ, 0 < c ∧ IsEffectOn (pairBody K) (c • ∑ μ, ∑ ν, E μ ν • tabCoord μ ν) := by
  set M : ℝ := ∑ μ, ∑ ν, |E μ ν| with hMdef
  have hM : 0 ≤ M := Finset.sum_nonneg fun _ _ => Finset.sum_nonneg fun _ _ => abs_nonneg _
  refine ⟨1 / (M + 1), by positivity, ?_⟩
  rintro _ ⟨ω, ⟨hωK, h00⟩, rfl⟩
  rw [AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, tableEff_apply]
  have hnn : 0 ≤ ipW E ω := mem_dualW.1 hE ω hωK
  have hle : ipW E ω ≤ M := by
    refine Finset.sum_le_sum fun μ _ => Finset.sum_le_sum fun ν _ => ?_
    have hb := abs_le_one_of_maxCone' (hK.2 hωK) h00 μ ν
    calc E μ ν * ω μ ν ≤ |E μ ν * ω μ ν| := le_abs_self _
      _ = |E μ ν| * |ω μ ν| := abs_mul _ _
      _ ≤ |E μ ν| * 1 := mul_le_mul_of_nonneg_left hb (abs_nonneg _)
      _ = |E μ ν| := mul_one _
  refine ⟨mul_nonneg (by positivity) hnn, ?_⟩
  rw [div_mul_eq_mul_div, one_mul, div_le_one (by positivity)]
  linarith

/-! ### O1 — the four-copy contraction read on target `01` -/

theorem fourVal_eq_01 (X Y E F : W 3) :
    fourVal X Y E F = ipW X (tabMul (tabMul E Y) (tabT F)) := by
  simp only [fourVal, ipW, tabMul, tabT, Finset.mul_sum, Finset.sum_mul]
  -- LHS order `a b c d`; RHS order `μ ν λ κ` with `(μ, ν, κ, λ) = (a, b, c, d)`: swap the inner two.
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  rw [Finset.sum_comm]
  -- ITER: summand shape after `Finset.mul_sum`/`Finset.sum_mul`.
  exact Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun d _ => by ring

/-! ### SC7 — the consumed fields of KT(4) -/

/-- **KT(4), the consumed core.** Two product data on one carrier, one body, the product states of
each grouping in the body, the product effects of each grouping effects on the body, and the
four-token coherence clause. `KT4` and `KT4LT` give it by forgetting fields. -/
structure KT4Core (K01 K23 K02 K13 : Set (W 3)) (V : Type) [NormedAddCommGroup V]
    [NormedSpace ℝ V] where
  DA : ProductData 16 16 V
  DB : ProductData 16 16 V
  Ω : Set V
  memA : ∀ x ∈ pairBody K01, ∀ y ∈ pairBody K23, DA.prodState x y ∈ Ω
  memB : ∀ x ∈ pairBody K02, ∀ y ∈ pairBody K13, DB.prodState x y ∈ Ω
  effA : ∀ (e : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ),
    IsEffectOn (pairBody K01) e → IsEffectOn (pairBody K23) f → IsEffectOn Ω (DA.prodEff e f)
  effB : ∀ (e : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ),
    IsEffectOn (pairBody K02) e → IsEffectOn (pairBody K13) f → IsEffectOn Ω (DB.prodEff e f)
  tok : ∀ a b c d : Fin 4, ∀ ω ∈ Ω,
    DA.prodEff (tabCoord a b) (tabCoord c d) ω = DB.prodEff (tabCoord a c) (tabCoord b d) ω

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- The minimal form gives the core by forgetting `convex`, `prodEff_unit` and the combination laws. -/
def KT4.toCore (H : KT4 K01 K23 K02 K13 V) : KT4Core K01 K23 K02 K13 V where
  DA := H.PA.toProductData
  DB := H.PB.toProductData
  Ω := H.PA.Ω
  memA := H.PA.prod_mem
  memB x hx y hy := by rw [H.one_body]; exact H.PB.prod_mem x hx y hy
  effA := H.PA.prodEff_effect
  effB e f he hf := by rw [H.one_body]; exact H.PB.prodEff_effect e f he hf
  tok := H.tok

def KT4LT.toCore (H : KT4LT K01 K23 K02 K13 V) : KT4Core K01 K23 K02 K13 V :=
  H.toKT4.toCore

/-! ### B1 — the bridge -/

/-- Expansion of a product effect built from tables (bilinearity of `prodEff`, termwise evaluation). -/
theorem prodEff_tables (D : ProductData 16 16 V) (E F : W 3) (ω : V) :
    D.prodEff (∑ μ, ∑ ν, E μ ν • tabCoord μ ν) (∑ μ, ∑ ν, F μ ν • tabCoord μ ν) ω =
      ∑ a, ∑ c, ∑ b, ∑ d, E a c * F b d * D.prodEff (tabCoord a c) (tabCoord b d) ω := by
  -- ITER: the same rewriting chain as COMP-1's `prodEff_expand` (CI:290), twice.
  simp only [map_sum, map_smul, LinearMap.sum_apply, LinearMap.smul_apply, affine_sum_apply,
    AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun c _ =>
    Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun d _ => by ring

/-- Family I's value through token coherence: a product effect of the `02|13` grouping, built from
tables, on a product state of the `01|23` grouping, is the four-copy contraction. -/
theorem core_valI (H : KT4Core K01 K23 K02 K13 V) {x y : W 3} (E F : W 3)
    (hω : H.DA.prodState (flatW x) (flatW y) ∈ H.Ω) :
    H.DB.prodEff (∑ μ, ∑ ν, E μ ν • tabCoord μ ν) (∑ μ, ∑ ν, F μ ν • tabCoord μ ν)
      (H.DA.prodState (flatW x) (flatW y)) = fourVal x y E F := by
  rw [prodEff_tables]
  have hterm : ∀ a b c d : Fin 4,
      H.DB.prodEff (tabCoord a c) (tabCoord b d) (H.DA.prodState (flatW x) (flatW y)) =
        x a b * y c d := fun a b c d => by
    rw [← H.tok a b c d _ hω, H.DA.prodEff_apply, tabCoord_flatW, tabCoord_flatW]
  simp only [hterm, fourVal]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun b _ => Finset.sum_congr rfl fun c _ =>
    Finset.sum_congr rfl fun d _ => by ring

/-- Family II's value through token coherence (the clause read in the other direction). -/
theorem core_valII (H : KT4Core K01 K23 K02 K13 V) {l l' : W 3} (e f : W 3)
    (hω : H.DB.prodState (flatW l) (flatW l') ∈ H.Ω) :
    H.DA.prodEff (∑ μ, ∑ ν, e μ ν • tabCoord μ ν) (∑ μ, ∑ ν, f μ ν • tabCoord μ ν)
      (H.DB.prodState (flatW l) (flatW l')) = fourVal e f l l' := by
  rw [prodEff_tables]
  have hterm : ∀ a b c d : Fin 4,
      H.DA.prodEff (tabCoord a b) (tabCoord c d) (H.DB.prodState (flatW l) (flatW l')) =
        l a c * l' b d := fun a b c d => by
    rw [H.tok a b c d _ hω, H.DB.prodEff_apply, tabCoord_flatW, tabCoord_flatW]
  -- Positionally the expansion's term at `(i, j, k, l)` is `e i j * f k l * DA.prodEff (tabCoord i j)
  -- (tabCoord k l) ω`, and `fourVal e f l l'`'s term at `(i, j, k, l)` is `e i j * f k l * l i k *
  -- l' j l`; `hterm i j k l` closes it with no reordering of the sums.
  simp only [fourVal]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
    Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun d _ => ?_
  rw [hterm]
  ring

/-- A positive rescaling of a cone table into the normalized pair body. -/
theorem flatW_mem_pairBody {K : Set (W 3)} (hK : PairAdm K) {X : W 3} (hX : X ∈ K)
    (hp : 0 < X 0 0) : flatW ((X 0 0)⁻¹ • X) ∈ pairBody K :=
  ⟨(X 0 0)⁻¹ • X, ⟨hK.2.2 _ (inv_nonneg.2 hp.le) X hX, by
    simp [Pi.smul_apply, smul_eq_mul, inv_mul_cancel₀ hp.ne']⟩, rfl⟩

theorem fourVal_smul (a b : ℝ) (X Y E F : W 3) :
    fourVal (a • X) (b • Y) E F = a * b * fourVal X Y E F := by
  simp only [fourVal, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring

theorem fourVal_zero_left (Y E F : W 3) : fourVal 0 Y E F = 0 := by simp [fourVal]

theorem fourVal_zero_right (X E F : W 3) : fourVal X 0 E F = 0 := by simp [fourVal]

/-- The scalar bookkeeping of both families. -/
theorem nonneg_of_scaled {cE cF a b v : ℝ} (hcE : 0 < cE) (hcF : 0 < cF) (ha : 0 < a) (hb : 0 < b)
    (h : 0 ≤ cE * (cF * (a * b * v))) : 0 ≤ v := by
  have h1 := (mul_nonneg_iff_of_pos_left hcE).1 h
  have h2 := (mul_nonneg_iff_of_pos_left hcF).1 h1
  exact (mul_nonneg_iff_of_pos_left (mul_pos ha hb)).1 h2

/-- **Lemma B1 over the consumed core.** -/
theorem fourCopyCoherent_of_kt4Core (a01 : PairAdm K01) (a23 : PairAdm K23) (a02 : PairAdm K02)
    (a13 : PairAdm K13) (H : KT4Core K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 where
  famI X hX Y hY E hE F hF := by
    rw [← fourVal_eq_01]
    by_cases hX0 : X 0 0 = 0
    · rw [eq_zero_of_maxCone_00 (a01.1.2 hX) hX0, fourVal_zero_left]
    by_cases hY0 : Y 0 0 = 0
    · rw [eq_zero_of_maxCone_00 (a23.1.2 hY) hY0, fourVal_zero_right]
    have hXp : 0 < X 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (a01.1.2 hX)) (Ne.symm hX0)
    have hYp : 0 < Y 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (a23.1.2 hY)) (Ne.symm hY0)
    obtain ⟨cE, hcE, heE⟩ := exists_effect_of_dualW a02.1 hE
    obtain ⟨cF, hcF, heF⟩ := exists_effect_of_dualW a13.1 hF
    have hω := H.memA _ (flatW_mem_pairBody a01 hX hXp) _ (flatW_mem_pairBody a23 hY hYp)
    have h0 := (H.effB _ _ heE heF _ hω).1
    -- ITER: pull the two scalars out of `prodEff` (linear in each slot) and out of the evaluation.
    rw [map_smul, LinearMap.smul_apply, map_smul, AffineMap.coe_smul, Pi.smul_apply,
      AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, smul_eq_mul, core_valI H E F hω,
      fourVal_smul] at h0
    exact nonneg_of_scaled hcE hcF (inv_pos.2 hXp) (inv_pos.2 hYp) h0
  famII L hL L' hL' e he f hf := by
    rw [← fourVal_eq_01]
    by_cases hL0 : L 0 0 = 0
    · rw [eq_zero_of_maxCone_00 (a02.1.2 hL) hL0]
      simp [fourVal]
    by_cases hL0' : L' 0 0 = 0
    · rw [eq_zero_of_maxCone_00 (a13.1.2 hL') hL0']
      simp [fourVal]
    have hLp : 0 < L 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (a02.1.2 hL)) (Ne.symm hL0)
    have hLp' : 0 < L' 0 0 := lt_of_le_of_ne (nonneg_00_of_maxCone (a13.1.2 hL')) (Ne.symm hL0')
    obtain ⟨ce, hce, hee⟩ := exists_effect_of_dualW a01.1 he
    obtain ⟨cf, hcf, hef⟩ := exists_effect_of_dualW a23.1 hf
    have hω := H.memB _ (flatW_mem_pairBody a02 hL hLp) _ (flatW_mem_pairBody a13 hL' hLp')
    have h0 := (H.effA _ _ hee hef _ hω).1
    rw [map_smul, LinearMap.smul_apply, map_smul, AffineMap.coe_smul, Pi.smul_apply,
      AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, smul_eq_mul, core_valII H e f hω] at h0
    -- `fourVal e f l l'` with `l = L00⁻¹ • L`, `l' = L'00⁻¹ • L'`: the scalars sit in the effect
    -- slots of `fourVal`, which is linear there as well.
    have hs : fourVal e f ((L 0 0)⁻¹ • L) ((L' 0 0)⁻¹ • L') =
        (L 0 0)⁻¹ * (L' 0 0)⁻¹ * fourVal e f L L' := by
      simp only [fourVal, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
      exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring
    rw [hs] at h0
    exact nonneg_of_scaled hce hcf (inv_pos.2 hLp) (inv_pos.2 hLp') h0

/-- **O22 (Lemma B1), as stated in the package**: the minimal form through the core. -/
theorem fourCopyCoherent_of_kt4 (a01 : PairAdm K01) (a23 : PairAdm K23) (a02 : PairAdm K02)
    (a13 : PairAdm K13) (H : KT4 K01 K23 K02 K13 V) : FourCopyCoherent K01 K23 K02 K13 :=
  fourCopyCoherent_of_kt4Core a01 a23 a02 a13 H.toCore

end

end FourCopy
end OIBridge
