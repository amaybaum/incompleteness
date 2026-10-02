/-
  OIBridge/InvariantInnerProduct.lean — round IIP-1: a common fixed point and an invariant inner
  product for the affine automorphisms of a convex body, on the translation space of its affine
  span.

  Nothing here is a hypothesis about OI, and no group, compactness of a group or Haar measure is
  used. The fixed point is the centroid of the body and the inner product comes from the body's
  second moment, both taken with respect to Lebesgue measure on coordinates `Fin n → ℝ`. Every
  affine automorphism `g` of the coordinate space with `g '' Ω = Ω` preserves both: the change of
  variables along `g` forces `|det g| = 1`, so integrals over `Ω` are invariant under `g`.

  Proved here.
    §A  change of variables along an affine automorphism preserving `Ω`: `|det| = 1` and the
        set integral over `Ω` is invariant (`abs_det_eq_one`, `setIntegral_comp_eq`);
    §B  the centroid is fixed by every such automorphism (`centroid_fixed`);
    §C  the second-moment form `moment Ω u v` is symmetric, positive definite when `Ω` has
        nonempty interior (`moment_pos`), and invariant under the transpose of the linear part
        (`moment_transpose_invariant`); its matrix `momentMatrix Ω` satisfies `A S Aᵀ = S`
        (`momentMatrix_conj`);
    §D  the inverse `invMatrix Ω = (momentMatrix Ω)⁻¹` is symmetric, positive definite and
        invariant under the linear part itself (`invariant_inner_product`);
    §E  on the translation space of a body's affine span, through an affine chart as in
        `OrbitNormalization` §D: the restricted body is compact with nonempty interior, and the
        restriction of every affine automorphism of the body fixes the restricted centroid and
        preserves the restricted inner product (`invariant_inner_product_span`);
    §F  control: without interior the second moment can vanish identically — on the origin in
        dimension at least one (`momentMatrix_origin`, `not_pos_moment_origin`).

  No ellipsoid, no transitivity and no dimension is claimed.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.OrbitNormalization
import Mathlib.MeasureTheory.Function.Jacobian
import Mathlib.Analysis.Calculus.FDeriv.Linear
import Mathlib.Analysis.Calculus.FDeriv.Add
import Mathlib.MeasureTheory.Measure.Lebesgue.EqHaar
import Mathlib.Analysis.Normed.Affine.AddTorsorBases
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv

namespace OIBridge
namespace InvariantInnerProduct

open MeasureTheory Set Matrix KInfFoundations OrbitGeneration OrbitNormalization

variable {n : ℕ}

/-! ### §A — change of variables along an affine automorphism -/

/-- The matrix of the linear part of an affine automorphism of the coordinate space. -/
noncomputable def linMatrix (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=
  LinearMap.toMatrix' g.toAffineMap.linear

theorem mulVec_apply_eq (M : Matrix (Fin n) (Fin n) ℝ) (v : Fin n → ℝ) (i : Fin n) :
    (M *ᵥ v) i = ∑ k, M i k * v k := rfl

theorem affine_apply_eq (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (x : Fin n → ℝ) :
    g x = linMatrix g *ᵥ x + g 0 := by
  have h := g.toAffineMap.linearMap_vsub x 0
  rw [vsub_eq_sub, vsub_eq_sub, sub_zero, AffineEquiv.coe_toAffineMap] at h
  rw [linMatrix, LinearMap.toMatrix'_mulVec, h]
  abel

theorem affine_sub_eq (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (x y : Fin n → ℝ) :
    g x - g y = linMatrix g *ᵥ (x - y) := by
  rw [affine_apply_eq g x, affine_apply_eq g y, mulVec_sub]
  abel

theorem hasFDerivWithinAt_affine (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (s : Set (Fin n → ℝ))
    (x : Fin n → ℝ) :
    HasFDerivWithinAt (g : (Fin n → ℝ) → (Fin n → ℝ))
      (LinearMap.toContinuousLinearMap g.toAffineMap.linear) s x := by
  have hfun : (g : (Fin n → ℝ) → (Fin n → ℝ)) =
      fun y => LinearMap.toContinuousLinearMap g.toAffineMap.linear y + g 0 := by
    funext y
    have h := g.toAffineMap.linearMap_vsub y 0
    rw [vsub_eq_sub, vsub_eq_sub, sub_zero, AffineEquiv.coe_toAffineMap] at h
    rw [LinearMap.coe_toContinuousLinearMap', h]
    abel
  rw [hfun]
  exact ((LinearMap.toContinuousLinearMap g.toAffineMap.linear).hasFDerivAt.add_const
    (g 0)).hasFDerivWithinAt

/-- Change of variables along an affine automorphism preserving `Ω`. -/
theorem setIntegral_comp {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)
    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) (h : (Fin n → ℝ) → ℝ) :
    ∫ x in Ω, h x = |LinearMap.det g.toAffineMap.linear| * ∫ x in Ω, h (g x) := by
  have key := integral_image_eq_integral_abs_det_fderiv_smul volume hm
    (fun x _ => hasFDerivWithinAt_affine g Ω x) (fun x _ y _ hxy => g.injective hxy) h
  rw [hg] at key
  rw [key]
  simp only [smul_eq_mul]
  rw [integral_const_mul]
  rfl

/-- An affine automorphism preserving a body of positive finite volume has `|det| = 1`. -/
theorem abs_det_eq_one {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω) (hpos : 0 < volume.real Ω)
    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :
    |LinearMap.det g.toAffineMap.linear| = 1 := by
  have h := setIntegral_comp hm g hg (fun _ => (1 : ℝ))
  simp only [setIntegral_const, smul_eq_mul, mul_one] at h
  exact (mul_right_cancel₀ hpos.ne' ((one_mul _).trans h)).symm

/-- Integrals over `Ω` are invariant under an affine automorphism preserving `Ω`. -/
theorem setIntegral_comp_eq {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)
    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω)
    (h : (Fin n → ℝ) → ℝ) :
    ∫ x in Ω, h (g x) = ∫ x in Ω, h x := by
  rw [setIntegral_comp hm g hg h, abs_det_eq_one hm hpos g hg, one_mul]

theorem det_linMatrix_ne_zero {Ω : Set (Fin n → ℝ)} (hm : MeasurableSet Ω)
    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :
    (linMatrix g).det ≠ 0 := by
  intro h0
  have h1 := abs_det_eq_one hm hpos g hg
  rw [linMatrix, LinearMap.det_toMatrix'] at h0
  rw [h0, abs_zero] at h1
  exact zero_ne_one h1

/-! ### §B — the centroid -/

/-- The centroid of `Ω` with respect to Lebesgue measure. -/
noncomputable def centroid (Ω : Set (Fin n → ℝ)) : Fin n → ℝ :=
  fun i => (volume.real Ω)⁻¹ * ∫ x in Ω, x i

theorem integrableOn_coord {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (i : Fin n) :
    IntegrableOn (fun x : Fin n → ℝ => x i) Ω :=
  (continuous_apply i).continuousOn.integrableOn_compact hc

theorem setIntegral_mulVec_coord {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)
    (M : Matrix (Fin n) (Fin n) ℝ) (b : Fin n → ℝ) (i : Fin n) :
    ∫ x in Ω, (M *ᵥ x + b) i = (∑ k, M i k * ∫ x in Ω, x k) + volume.real Ω * b i := by
  have hsum : ∀ x : Fin n → ℝ, (M *ᵥ x + b) i = (∑ k, M i k * x k) + b i := by
    intro x
    rw [Pi.add_apply, mulVec_apply_eq]
  have hcs : IntegrableOn (fun x : Fin n → ℝ => ∑ k, M i k * x k) Ω :=
    (continuous_finsetSum _ fun k _ =>
      continuous_const.mul (continuous_apply k)).continuousOn.integrableOn_compact hc
  have hcb : IntegrableOn (fun _ : Fin n → ℝ => b i) Ω :=
    continuous_const.continuousOn.integrableOn_compact hc
  simp_rw [hsum]
  rw [integral_add hcs hcb,
    integral_finsetSum _ fun k _ => (integrableOn_coord hc k).const_mul (M i k),
    setIntegral_const, smul_eq_mul]
  congr 1
  exact Finset.sum_congr rfl fun k _ => integral_const_mul _ _

/-- **The centroid is fixed** by every affine automorphism preserving a compact body of positive
volume. -/
theorem centroid_fixed {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hpos : 0 < volume.real Ω)
    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :
    g (centroid Ω) = centroid Ω := by
  have hm := hc.measurableSet
  funext i
  have hint : ∫ x in Ω, x i = (∑ k, linMatrix g i k * ∫ x in Ω, x k) + volume.real Ω * g 0 i := by
    have h1 : ∫ x in Ω, g x i = ∫ x in Ω, x i := setIntegral_comp_eq hm hpos g hg (fun x => x i)
    have h2 : (fun x => g x i) = fun x => (linMatrix g *ᵥ x + g 0) i :=
      funext fun x => by rw [affine_apply_eq g x]
    rw [← h1, h2]
    exact setIntegral_mulVec_coord hc (linMatrix g) (g 0) i
  have hv : (volume.real Ω)⁻¹ * (volume.real Ω * g 0 i) = g 0 i := by
    rw [← mul_assoc, inv_mul_cancel₀ hpos.ne', one_mul]
  rw [affine_apply_eq g (centroid Ω), Pi.add_apply, mulVec_apply_eq]
  simp only [centroid]
  rw [hint, mul_add, Finset.mul_sum, hv]
  congr 1
  refine Finset.sum_congr rfl fun k _ => ?_
  ring

/-! ### §C — the second moment -/

/-- The second-moment form of `Ω` about its centroid. -/
noncomputable def moment (Ω : Set (Fin n → ℝ)) (u v : Fin n → ℝ) : ℝ :=
  ∫ x in Ω, ((x - centroid Ω) ⬝ᵥ u) * ((x - centroid Ω) ⬝ᵥ v)

/-- The matrix of the second-moment form. -/
noncomputable def momentMatrix (Ω : Set (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=
  fun i j => moment Ω (Pi.single i 1) (Pi.single j 1)

theorem moment_symm (Ω : Set (Fin n → ℝ)) (u v : Fin n → ℝ) : moment Ω u v = moment Ω v u := by
  unfold moment
  simp_rw [mul_comm]

theorem continuous_dot_sub (c u : Fin n → ℝ) :
    Continuous fun x : Fin n → ℝ => (x - c) ⬝ᵥ u := by
  simp only [dotProduct]
  exact continuous_finsetSum _ fun i _ =>
    ((continuous_apply i).sub continuous_const).mul continuous_const

theorem integrableOn_moment {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (c u v : Fin n → ℝ) :
    IntegrableOn (fun x : Fin n → ℝ => ((x - c) ⬝ᵥ u) * ((x - c) ⬝ᵥ v)) Ω :=
  ((continuous_dot_sub c u).mul (continuous_dot_sub c v)).continuousOn.integrableOn_compact hc

theorem dot_eq_sum_single (w u : Fin n → ℝ) : w ⬝ᵥ u = ∑ i, u i * (w ⬝ᵥ Pi.single i 1) := by
  simp only [dotProduct_single, mul_one]
  rw [dotProduct]
  exact Finset.sum_congr rfl fun i _ => mul_comm _ _

/-- The form is given by its matrix. -/
theorem moment_eq_dotProduct {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (u v : Fin n → ℝ) :
    moment Ω u v = u ⬝ᵥ (momentMatrix Ω *ᵥ v) := by
  have hexp : ∀ x : Fin n → ℝ, ((x - centroid Ω) ⬝ᵥ u) * ((x - centroid Ω) ⬝ᵥ v) =
      ∑ i, ∑ j, u i * v j * (((x - centroid Ω) ⬝ᵥ Pi.single i 1) *
        ((x - centroid Ω) ⬝ᵥ Pi.single j 1)) := by
    intro x
    rw [dot_eq_sum_single (x - centroid Ω) u, dot_eq_sum_single (x - centroid Ω) v,
      Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
    ring
  unfold moment
  simp_rw [hexp]
  rw [integral_finsetSum _ fun i _ =>
    integrable_finsetSum _ fun j _ => (integrableOn_moment hc _ _ _).const_mul _]
  rw [dot_mulVec_eq_sum_sum, Finset.sum_comm]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [integral_finsetSum _ fun j _ => (integrableOn_moment hc _ _ _).const_mul _]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [integral_const_mul]
  simp only [momentMatrix, moment]
  ring

theorem momentMatrix_transpose {Ω : Set (Fin n → ℝ)} : (momentMatrix Ω)ᵀ = momentMatrix Ω := by
  ext i j
  rw [transpose_apply]
  exact moment_symm Ω _ _

/-- **Positivity.** On a compact body with nonempty interior, the second moment is positive
definite. -/
theorem moment_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    {u : Fin n → ℝ} (hu : u ≠ 0) : 0 < moment Ω u u := by
  set c := centroid Ω
  set f : (Fin n → ℝ) → ℝ := fun x => ((x - c) ⬝ᵥ u) * ((x - c) ⬝ᵥ u) with hf
  have hfc : Continuous f := (continuous_dot_sub c u).mul (continuous_dot_sub c u)
  have hnn : ∀ x, 0 ≤ f x := fun x => mul_self_nonneg _
  -- a point of the interior where the linear form is nonzero
  obtain ⟨p, hp⟩ := hi
  obtain ⟨k, hk⟩ : ∃ k, u k ≠ 0 := by
    by_contra h
    push Not at h
    exact hu (funext h)
  have hq : ∃ q ∈ interior Ω, f q ≠ 0 := by
    by_cases h0 : (p - c) ⬝ᵥ u = 0
    · obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp isOpen_interior p hp
      refine ⟨p + (ε / 2) • Pi.single k 1, hball ?_, ?_⟩
      · rw [Metric.mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul,
          Real.norm_of_nonneg (by positivity)]
        have : ‖(Pi.single k 1 : Fin n → ℝ)‖ = 1 := by
          rw [Pi.norm_single, norm_one]
        rw [this, mul_one]
        linarith
      · have hlin : (p + (ε / 2) • Pi.single k 1 - c) ⬝ᵥ u = (ε / 2) * u k := by
          rw [add_sub_right_comm, add_dotProduct, h0, zero_add, smul_dotProduct,
            single_dotProduct, one_mul, smul_eq_mul]
        simp only [hf, hlin]
        exact mul_ne_zero (mul_ne_zero (by positivity) hk) (mul_ne_zero (by positivity) hk)
    · exact ⟨p, hp, mul_ne_zero h0 h0⟩
  obtain ⟨q, hqi, hq0⟩ := hq
  have hint : IntegrableOn f Ω := hfc.continuousOn.integrableOn_compact hc
  have hpos_set : 0 < volume (Function.support f ∩ Ω) := by
    have hU : IsOpen (Function.support f ∩ interior Ω) :=
      hfc.isOpen_support.inter isOpen_interior
    have hne : (Function.support f ∩ interior Ω).Nonempty := ⟨q, hq0, hqi⟩
    exact (hU.measure_pos volume hne).trans_le
      (measure_mono (inter_subset_inter_right _ interior_subset))
  have := (setIntegral_pos_iff_support_of_nonneg_ae (ae_of_all _ hnn) hint).mpr hpos_set
  exact this

/-- The moment matrix of a compact body with nonempty interior is invertible. -/
theorem momentMatrix_det_ne_zero {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) : (momentMatrix Ω).det ≠ 0 := by
  intro h0
  obtain ⟨v, hv, hSv⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr h0
  have hp := moment_pos hc hi hv
  rw [moment_eq_dotProduct hc, hSv, dotProduct_zero] at hp
  exact lt_irrefl _ hp

theorem dot_mulVec_transpose (A : Matrix (Fin n) (Fin n) ℝ) (x y : Fin n → ℝ) :
    (A *ᵥ x) ⬝ᵥ y = x ⬝ᵥ (Aᵀ *ᵥ y) := by
  rw [dotProduct_mulVec, vecMul_transpose]

/-- **Invariance of the moment** under the transpose of the linear part. -/
theorem moment_transpose_invariant {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)
    (hpos : 0 < volume.real Ω) (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω)
    (u v : Fin n → ℝ) :
    moment Ω ((linMatrix g)ᵀ *ᵥ u) ((linMatrix g)ᵀ *ᵥ v) = moment Ω u v := by
  have hm := hc.measurableSet
  have hcen := centroid_fixed hc hpos g hg
  have hpt : ∀ x w, (x - centroid Ω) ⬝ᵥ ((linMatrix g)ᵀ *ᵥ w) = (g x - centroid Ω) ⬝ᵥ w := by
    intro x w
    rw [← dot_mulVec_transpose, ← affine_sub_eq, hcen]
  unfold moment
  simp_rw [hpt]
  exact setIntegral_comp_eq hm hpos g hg
    (fun y => ((y - centroid Ω) ⬝ᵥ u) * ((y - centroid Ω) ⬝ᵥ v))

/-- In matrix form: `A S Aᵀ = S`. -/
theorem momentMatrix_conj {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hpos : 0 < volume.real Ω)
    (g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ)) (hg : g '' Ω = Ω) :
    linMatrix g * momentMatrix Ω * (linMatrix g)ᵀ = momentMatrix Ω := by
  ext i j
  have h := moment_transpose_invariant hc hpos g hg (Pi.single i 1) (Pi.single j 1)
  rw [moment_eq_dotProduct hc, moment_eq_dotProduct hc, dot_mulVec_transpose,
    transpose_transpose, Matrix.mulVec_mulVec, Matrix.mulVec_mulVec] at h
  simpa [single_dotProduct, Matrix.mulVec_single] using h

/-! ### §D — the invariant inner product -/

/-- The inverse of the moment matrix: the matrix of the invariant inner product. -/
noncomputable def invMatrix (Ω : Set (Fin n → ℝ)) : Matrix (Fin n) (Fin n) ℝ :=
  (momentMatrix Ω)⁻¹

theorem invMatrix_transpose (Ω : Set (Fin n → ℝ)) : (invMatrix Ω)ᵀ = invMatrix Ω := by
  rw [invMatrix, transpose_nonsing_inv, momentMatrix_transpose]

theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)
    {u : Fin n → ℝ} (hu : u ≠ 0) : 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u) := by
  have hdet : IsUnit (momentMatrix Ω).det := isUnit_iff_ne_zero.mpr (momentMatrix_det_ne_zero hc hi)
  set w := invMatrix Ω *ᵥ u with hw
  have hu' : u = momentMatrix Ω *ᵥ w := by
    rw [hw, invMatrix, Matrix.mulVec_mulVec, mul_nonsing_inv _ hdet, Matrix.one_mulVec]
  have hw0 : w ≠ 0 := by
    intro h0
    rw [h0, Matrix.mulVec_zero] at hu'
    exact hu hu'
  have hp := moment_pos hc hi hw0
  rw [moment_eq_dotProduct hc] at hp
  rw [hu', dotProduct_comm]
  exact hp

/-- **The invariant inner product.** On a compact body with nonempty interior, `invMatrix Ω` is
symmetric and positive definite, and every affine automorphism preserving the body fixes its
centroid and preserves the inner product `⟨u, v⟩ = u ⬝ᵥ (invMatrix Ω *ᵥ v)` through its linear
part. -/
theorem invariant_inner_product {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) :
    (invMatrix Ω)ᵀ = invMatrix Ω ∧ (∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)) ∧
      ∀ g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ), g '' Ω = Ω →
        g (centroid Ω) = centroid Ω ∧
          ∀ u v, (linMatrix g *ᵥ u) ⬝ᵥ (invMatrix Ω *ᵥ (linMatrix g *ᵥ v)) =
            u ⬝ᵥ (invMatrix Ω *ᵥ v) := by
  have hpos : 0 < volume.real Ω := by
    obtain ⟨p, hp⟩ := hi
    have h1 : 0 < volume (interior Ω) := isOpen_interior.measure_pos volume ⟨p, hp⟩
    have h2 : 0 < volume Ω := h1.trans_le (measure_mono interior_subset)
    exact ENNReal.toReal_pos h2.ne' hc.measure_lt_top.ne
  refine ⟨invMatrix_transpose Ω, fun u hu => invMatrix_pos hc hi hu, fun g hg => ?_⟩
  refine ⟨centroid_fixed hc hpos g hg, fun u v => ?_⟩
  have hS : IsUnit (momentMatrix Ω).det := isUnit_iff_ne_zero.mpr (momentMatrix_det_ne_zero hc hi)
  have hA : IsUnit (linMatrix g).det :=
    isUnit_iff_ne_zero.mpr (det_linMatrix_ne_zero hc.measurableSet hpos g hg)
  have hAt : IsUnit (linMatrix g)ᵀ.det := isUnit_det_transpose _ hA
  -- `Aᵀ S⁻¹ A = S⁻¹` from `A S Aᵀ = S`
  have hconj := momentMatrix_conj hc hpos g hg
  have hinv : (linMatrix g)ᵀ * invMatrix Ω * linMatrix g = invMatrix Ω := by
    have e1 : invMatrix Ω = ((linMatrix g)ᵀ)⁻¹ * invMatrix Ω * (linMatrix g)⁻¹ := by
      conv_lhs => rw [invMatrix, ← hconj]
      rw [Matrix.mul_inv_rev, Matrix.mul_inv_rev, invMatrix, Matrix.mul_assoc]
    calc (linMatrix g)ᵀ * invMatrix Ω * linMatrix g
        = (linMatrix g)ᵀ * (((linMatrix g)ᵀ)⁻¹ * invMatrix Ω * (linMatrix g)⁻¹) * linMatrix g := by
          rw [← e1]
      _ = invMatrix Ω := by
          rw [Matrix.mul_assoc ((linMatrix g)ᵀ)⁻¹, ← Matrix.mul_assoc (linMatrix g)ᵀ,
            mul_nonsing_inv _ hAt, Matrix.one_mul, Matrix.mul_assoc,
            nonsing_inv_mul _ hA, Matrix.mul_one]
  rw [dot_mulVec_transpose, Matrix.mulVec_mulVec, Matrix.mulVec_mulVec, hinv]

/-! ### §E — on the translation space of the affine span -/

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- The restriction of a convex body to an injective affine chart whose range is the body's affine
span has nonempty interior. -/
theorem interior_bodyR_nonempty [FiniteDimensional ℝ V] {d : ℕ}
    {L : (Fin d → ℝ) →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V}
    (hconv : Convex ℝ Ω)
    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :
    (interior (bodyR L p0 Ω)).Nonempty := by
  have hcv : Convex ℝ (bodyR L p0 Ω) := hconv.affine_preimage (chart L p0)
  rw [hcv.interior_nonempty_iff_affineSpan_eq_top]
  have hsub : Ω ⊆ Set.range (chart L p0) := fun x hx =>
    (hspan x).mp (subset_affineSpan ℝ Ω hx)
  have himg : chart L p0 '' bodyR L p0 Ω = Ω := by
    ext x
    constructor
    · rintro ⟨w, hw, rfl⟩
      exact hw
    · intro hx
      obtain ⟨w, rfl⟩ := hsub hx
      exact ⟨w, hx, rfl⟩
  have hinj := chart_injective hL p0
  rw [eq_top_iff]
  intro w _
  have hw : chart L p0 w ∈ affineSpan ℝ Ω := (hspan _).mpr ⟨w, rfl⟩
  rw [← himg, ← AffineSubspace.map_span] at hw
  obtain ⟨w', hw', hww'⟩ := hw
  rw [← hinj hww']
  exact hw'

/-- The restricted body of a compact body is compact. -/
theorem isCompact_bodyR [FiniteDimensional ℝ V] {d : ℕ} {L : (Fin d → ℝ) →ₗ[ℝ] V}
    (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V} (hcomp : IsCompact Ω)
    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :
    IsCompact (bodyR L p0 Ω) := by
  obtain ⟨Lg, hLg⟩ := exists_chart_leftInverse hL
  have hsub : Ω ⊆ Set.range (chart L p0) := fun x hx =>
    (hspan x).mp (subset_affineSpan ℝ Ω hx)
  have hEq : bodyR L p0 Ω = chartRetract Lg p0 '' Ω := by
    ext w
    constructor
    · intro hw
      exact ⟨chart L p0 w, hw, chartRetract_chart hLg p0 w⟩
    · rintro ⟨x, hx, rfl⟩
      obtain ⟨w, rfl⟩ := hsub hx
      show chart L p0 (chartRetract Lg p0 (chart L p0 w)) ∈ Ω
      rw [chartRetract_chart hLg p0 w]
      exact hx
  rw [hEq]
  have hfun : (chartRetract Lg p0 : V → Fin d → ℝ) = fun x => Lg x + -(Lg p0) :=
    funext (chartRetract_apply Lg p0)
  have hcont : Continuous (chartRetract Lg p0 : V → Fin d → ℝ) := by
    rw [hfun]
    exact (Lg.continuous_of_finiteDimensional).add continuous_const
  exact hcomp.image hcont

/-- A restriction `g'` of an automorphism `g` of the body maps the restricted body onto itself. -/
theorem image_bodyR_eq {d : ℕ} {L : (Fin d → ℝ) →ₗ[ℝ] V} {p0 : V} {Ω : Set V}
    {g : V ≃ᵃ[ℝ] V} (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω)
    {g' : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hgg : ∀ w, chart L p0 (g' w) = g (chart L p0 w)) :
    g' '' bodyR L p0 Ω = bodyR L p0 Ω := by
  have hsymm : ∀ w, chart L p0 (g'.symm w) = g.symm (chart L p0 w) := by
    intro w
    have := hgg (g'.symm w)
    rw [AffineEquiv.apply_symm_apply] at this
    rw [this, AffineEquiv.symm_apply_apply]
  ext w
  constructor
  · rintro ⟨w', hw', rfl⟩
    show chart L p0 (g' w') ∈ Ω
    rw [hgg]
    exact (hg _ hw').1
  · intro hw
    refine ⟨g'.symm w, ?_, AffineEquiv.apply_symm_apply g' w⟩
    show chart L p0 (g'.symm w) ∈ Ω
    rw [hsymm]
    exact (hg _ hw).2

/-- **The invariant inner product on the translation space of the affine span.** For a compact
convex body `Ω` in a finite-dimensional space and an injective affine chart `w ↦ L w + p0` of its
affine span, the restricted body has nonempty interior, `invMatrix` of the restricted body is
symmetric and positive definite, and for every affine automorphism `g` of the body and every
restriction `g'` of `g` to the chart, `g'` fixes the restricted centroid and its linear part
preserves the inner product. -/
theorem invariant_inner_product_span [FiniteDimensional ℝ V] {d : ℕ}
    {L : (Fin d → ℝ) →ₗ[ℝ] V} (hL : LinearMap.ker L = ⊥) {p0 : V} {Ω : Set V}
    (hconv : Convex ℝ Ω) (hcomp : IsCompact Ω)
    (hspan : ∀ x, x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)) :
    IsCompact (bodyR L p0 Ω) ∧ (interior (bodyR L p0 Ω)).Nonempty ∧
      (invMatrix (bodyR L p0 Ω))ᵀ = invMatrix (bodyR L p0 Ω) ∧
      (∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ u)) ∧
      ∀ g : V ≃ᵃ[ℝ] V, (∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) →
        ∀ g' : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ), (∀ w, chart L p0 (g' w) = g (chart L p0 w)) →
          g' (centroid (bodyR L p0 Ω)) = centroid (bodyR L p0 Ω) ∧
            ∀ u v, (linMatrix g' *ᵥ u) ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ (linMatrix g' *ᵥ v)) =
              u ⬝ᵥ (invMatrix (bodyR L p0 Ω) *ᵥ v) := by
  have hc := isCompact_bodyR hL hcomp hspan
  have hi := interior_bodyR_nonempty hL hconv hspan
  obtain ⟨h1, h2, h3⟩ := invariant_inner_product hc hi
  exact ⟨hc, hi, h1, h2, fun g hg g' hgg => h3 g' (image_bodyR_eq hg hgg)⟩

/-! ### §F — control: interior is needed -/

/-- In dimension at least one the origin is a null set. -/
theorem volume_origin (hn : 0 < n) : volume ({0} : Set (Fin n → ℝ)) = 0 := by
  haveI : Nonempty (Fin n) := ⟨⟨0, hn⟩⟩
  have h := Measure.addHaar_submodule volume (⊥ : Submodule ℝ (Fin n → ℝ)) bot_ne_top
  rwa [Submodule.bot_coe] at h

/-- The second moment of a single point vanishes. -/
theorem momentMatrix_origin (hn : 0 < n) : momentMatrix ({0} : Set (Fin n → ℝ)) = 0 := by
  ext i j
  show moment {0} (Pi.single i 1) (Pi.single j 1) = 0
  unfold moment
  exact setIntegral_measure_zero _ (volume_origin hn)

/-- Without interior the second moment is not positive definite: on a point in dimension at least
one, it vanishes on a nonzero vector. -/
theorem not_pos_moment_origin (hn : 0 < n) :
    ∃ u : Fin n → ℝ, u ≠ 0 ∧ moment ({0} : Set (Fin n → ℝ)) u u = 0 := by
  refine ⟨Pi.single ⟨0, hn⟩ 1, ?_, ?_⟩
  · intro h
    have := congrFun h ⟨0, hn⟩
    simp at this
  · unfold moment
    exact setIntegral_measure_zero _ (volume_origin hn)

/-! ### §G — the verdict -/

/-- **Round IIP-1.** The common fixed point and the invariant inner product of the affine
automorphisms of a compact convex body, on the translation space of its affine span, and the
control that interior is needed. -/
theorem iip1_core :
    (∀ (Ω : Set (Fin n → ℝ)), IsCompact Ω → (interior Ω).Nonempty →
      ∀ g : (Fin n → ℝ) ≃ᵃ[ℝ] (Fin n → ℝ), g '' Ω = Ω →
        g (centroid Ω) = centroid Ω ∧
          ∀ u v, (linMatrix g *ᵥ u) ⬝ᵥ (invMatrix Ω *ᵥ (linMatrix g *ᵥ v)) =
            u ⬝ᵥ (invMatrix Ω *ᵥ v)) ∧
    (∀ (Ω : Set (Fin n → ℝ)), IsCompact Ω → (interior Ω).Nonempty →
      (invMatrix Ω)ᵀ = invMatrix Ω ∧ ∀ u, u ≠ 0 → 0 < u ⬝ᵥ (invMatrix Ω *ᵥ u)) ∧
    (0 < n → ∃ u : Fin n → ℝ, u ≠ 0 ∧ moment ({0} : Set (Fin n → ℝ)) u u = 0) :=
  ⟨fun _ hc hi g hg => (invariant_inner_product hc hi).2.2 g hg,
    fun _ hc hi => ⟨(invariant_inner_product hc hi).1, (invariant_inner_product hc hi).2.1⟩,
    fun hn => not_pos_moment_origin hn⟩

end InvariantInnerProduct
end OIBridge

#print axioms OIBridge.InvariantInnerProduct.affine_apply_eq
#print axioms OIBridge.InvariantInnerProduct.setIntegral_comp
#print axioms OIBridge.InvariantInnerProduct.abs_det_eq_one
#print axioms OIBridge.InvariantInnerProduct.setIntegral_comp_eq
#print axioms OIBridge.InvariantInnerProduct.centroid_fixed
#print axioms OIBridge.InvariantInnerProduct.moment_eq_dotProduct
#print axioms OIBridge.InvariantInnerProduct.moment_pos
#print axioms OIBridge.InvariantInnerProduct.momentMatrix_det_ne_zero
#print axioms OIBridge.InvariantInnerProduct.moment_transpose_invariant
#print axioms OIBridge.InvariantInnerProduct.momentMatrix_conj
#print axioms OIBridge.InvariantInnerProduct.invMatrix_pos
#print axioms OIBridge.InvariantInnerProduct.invariant_inner_product
#print axioms OIBridge.InvariantInnerProduct.interior_bodyR_nonempty
#print axioms OIBridge.InvariantInnerProduct.isCompact_bodyR
#print axioms OIBridge.InvariantInnerProduct.image_bodyR_eq
#print axioms OIBridge.InvariantInnerProduct.invariant_inner_product_span
#print axioms OIBridge.InvariantInnerProduct.volume_origin
#print axioms OIBridge.InvariantInnerProduct.momentMatrix_origin
#print axioms OIBridge.InvariantInnerProduct.not_pos_moment_origin
#print axioms OIBridge.InvariantInnerProduct.iip1_core
