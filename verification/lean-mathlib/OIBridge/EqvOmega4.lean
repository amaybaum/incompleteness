/-
  OIBridge/EqvOmega4.lean — design module of the research thread `research/equivalence` (node E8,
  draft S4). Not adopted, not certified, not a round: boundary transitivity (K∞-Trans) is not implied
  by the other single-system seams, on a disposable branch.

  Ω₄ = {(x, s) ∈ ℝ³ × ℝ : ‖x‖⁴ + s⁴ ≤ 1}, written on `Fin 4 → ℝ` with `s` the last coordinate
  (`omega4`). It is compact, convex and has interior; it is centrally symmetric about `0`; it is
  strictly convex, hence relatively strictly convex (`relStrictConvex_of_strictConvex`), hence has
  singleton faces for every effect family; it carries the sharp seed `v ↦ (1 + v 3)/2` and an
  elementary drive: the rotations of the first two coordinates as the flow, the half-turn as the NOT,
  the cyclic permutation of the first three coordinates as `J` (`omega4Drive`).

  Ω₄ is not an affine image of the Euclidean ball (`not_affine_eball_omega4`): in the plane of the
  first and last axes, no quadric contains the eight states `(±1, 0)`, `(0, ±1)`, `(±5/6, ±5/6)` and
  excludes the eight points `(±1, ±1/2)`, `(±1/2, ±1)`. By TRB-1's `exists_affine_image_eq_eball` and
  KTRANS-DENSE-1's `exists_affine_image_eq_eball_of_dense`, no body-preserving family on Ω₄ is
  boundary transitive or has a dense boundary orbit (`not_boundaryTransitive_omega4`,
  `not_denseBoundaryOrbit_omega4`; together `kinfTrans_separation`).

  Supporting-effect completeness of the full effects on Ω₄ is not proved here. Nothing here says which
  bodies OI supplies.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DenseOrbit

namespace OIBridge
namespace EqvOmega4

open Set KInfFoundations OrbitGeneration TransitiveBody DenseOrbit

noncomputable section

/-! ### §A — the body -/

/-- Ω₄: the ℓ⁴-sum of the Euclidean 3-ball and the segment. -/
def omega4 : Set (Fin 4 → ℝ) := {v | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1}

theorem mem_omega4 (v : Fin 4 → ℝ) :
    v ∈ omega4 ↔ (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 ≤ 1 := Iff.rfl

theorem vec4_ext {v w : Fin 4 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2)
    (h3 : v 3 = w 3) : v = w := by
  funext i
  fin_cases i
  exacts [h0, h1, h2, h3]

theorem omega4_isCompact : IsCompact omega4 := by
  have hcl : IsClosed omega4 :=
    isClosed_le (f := fun v : Fin 4 → ℝ => (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4)
      (g := fun _ => (1 : ℝ)) (by fun_prop) continuous_const
  have hsub : omega4 ⊆ Metric.closedBall (0 : Fin 4 → ℝ) 2 := by
    intro v hv
    rw [mem_omega4] at hv
    rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg (by norm_num : (0 : ℝ) ≤ 2)]
    intro i
    have hq : 0 ≤ v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 := by positivity
    have h3 : 0 ≤ v 3 ^ 2 := sq_nonneg _
    have hqle : v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1 := by nlinarith [sq_nonneg (v 3 ^ 2)]
    have h3le : v 3 ^ 2 ≤ 1 := by nlinarith [sq_nonneg (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2)]
    have h1 : v i ^ 2 ≤ ∑ j, v j ^ 2 :=
      Finset.single_le_sum (f := fun j => v j ^ 2) (fun j _ => sq_nonneg (v j))
        (Finset.mem_univ i)
    simp only [Fin.sum_univ_four] at h1
    rw [Real.norm_eq_abs, abs_le]
    constructor <;> nlinarith
  exact Metric.isCompact_of_isClosed_isBounded hcl (Metric.isBounded_closedBall.subset hsub)

/-- The convexity inequality on reals, with `b = 1 - a`. -/
theorem conv_core (a x0 x1 x2 s y0 y1 y2 t : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ 1 - a)
    (hx : (x0 ^ 2 + x1 ^ 2 + x2 ^ 2) ^ 2 + s ^ 4 ≤ 1)
    (hy : (y0 ^ 2 + y1 ^ 2 + y2 ^ 2) ^ 2 + t ^ 4 ≤ 1) :
    ((a * x0 + (1 - a) * y0) ^ 2 + (a * x1 + (1 - a) * y1) ^ 2 + (a * x2 + (1 - a) * y2) ^ 2) ^ 2
      + (a * s + (1 - a) * t) ^ 4 ≤ 1 := by
  have hab : 0 ≤ a * (1 - a) := mul_nonneg ha hb
  have e1 : (a * x0 + (1 - a) * y0) ^ 2 + (a * x1 + (1 - a) * y1) ^ 2 + (a * x2 + (1 - a) * y2) ^ 2
      = a * (x0 ^ 2 + x1 ^ 2 + x2 ^ 2) + (1 - a) * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2)
        - a * (1 - a) * ((x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2) := by ring
  have e2 : (a * s + (1 - a) * t) ^ 4
      = (a * s ^ 2 + (1 - a) * t ^ 2 - a * (1 - a) * (s - t) ^ 2) ^ 2 := by ring
  have hz : 0 ≤ a * (x0 ^ 2 + x1 ^ 2 + x2 ^ 2) + (1 - a) * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2)
      - a * (1 - a) * ((x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2) := by
    rw [← e1]; positivity
  have hw : 0 ≤ a * s ^ 2 + (1 - a) * t ^ 2 - a * (1 - a) * (s - t) ^ 2 := by
    have e3 : (a * s + (1 - a) * t) ^ 2 = a * s ^ 2 + (1 - a) * t ^ 2 - a * (1 - a) * (s - t) ^ 2 := by
      ring
    rw [← e3]; positivity
  have hD : 0 ≤ (x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2 := by positivity
  have hE : 0 ≤ (s - t) ^ 2 := sq_nonneg _
  have hxx : (x0 ^ 2 + x1 ^ 2 + x2 ^ 2) ^ 2 + (s ^ 2) ^ 2 ≤ 1 := by
    have e : (s ^ 2) ^ 2 = s ^ 4 := by ring
    rw [e]; exact hx
  have hyy : (y0 ^ 2 + y1 ^ 2 + y2 ^ 2) ^ 2 + (t ^ 2) ^ 2 ≤ 1 := by
    have e : (t ^ 2) ^ 2 = t ^ 4 := by ring
    rw [e]; exact hy
  rw [e1, e2]
  set X := x0 ^ 2 + x1 ^ 2 + x2 ^ 2
  set Y := y0 ^ 2 + y1 ^ 2 + y2 ^ 2
  set D := (x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2
  set S := s ^ 2
  set T := t ^ 2
  set E := (s - t) ^ 2
  have h5 : 0 ≤ (a * X + (1 - a) * Y - a * (1 - a) * D) * (a * (1 - a) * D) :=
    mul_nonneg hz (mul_nonneg hab hD)
  have h6 : 0 ≤ (a * S + (1 - a) * T - a * (1 - a) * E) * (a * (1 - a) * E) :=
    mul_nonneg hw (mul_nonneg hab hE)
  have h3 : 0 ≤ a * (1 - a) * (X - Y) ^ 2 := mul_nonneg hab (sq_nonneg _)
  have h4 : 0 ≤ a * (1 - a) * (S - T) ^ 2 := mul_nonneg hab (sq_nonneg _)
  have h1 : a * (X ^ 2 + S ^ 2) ≤ a * 1 := mul_le_mul_of_nonneg_left hxx ha
  have h2 : (1 - a) * (Y ^ 2 + T ^ 2) ≤ (1 - a) * 1 := mul_le_mul_of_nonneg_left hyy hb
  have h7 : 0 ≤ (a * (1 - a) * D) ^ 2 + (a * (1 - a) * E) ^ 2 := by positivity
  linarith [h1, h2, h3, h4, h5, h6, h7]

theorem omega4_convex : Convex ℝ omega4 := by
  intro x hx y hy a b ha hb hab
  obtain rfl : b = 1 - a := by linarith
  have hx' : (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 + x 3 ^ 4 ≤ 1 := hx
  have hy' : (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2) ^ 2 + y 3 ^ 4 ≤ 1 := hy
  rw [mem_omega4]
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  exact conv_core a (x 0) (x 1) (x 2) (x 3) (y 0) (y 1) (y 2) (y 3) ha hb hx' hy'

/-- The strict inequality behind strict convexity, on abstract reals. -/
theorem abstract_strict (a X Y S T D E : ℝ) (ha : 0 < a) (hb : 0 < 1 - a)
    (hz : 0 ≤ a * X + (1 - a) * Y - a * (1 - a) * D)
    (hw : 0 ≤ a * S + (1 - a) * T - a * (1 - a) * E)
    (hD : 0 ≤ D) (hE : 0 ≤ E) (hDE : 0 < D + E)
    (hx : X ^ 2 + S ^ 2 ≤ 1) (hy : Y ^ 2 + T ^ 2 ≤ 1) :
    (a * X + (1 - a) * Y - a * (1 - a) * D) ^ 2 + (a * S + (1 - a) * T - a * (1 - a) * E) ^ 2
      < 1 := by
  have hab : 0 < a * (1 - a) := mul_pos ha hb
  have h5 : 0 ≤ (a * X + (1 - a) * Y - a * (1 - a) * D) * (a * (1 - a) * D) :=
    mul_nonneg hz (mul_nonneg hab.le hD)
  have h6 : 0 ≤ (a * S + (1 - a) * T - a * (1 - a) * E) * (a * (1 - a) * E) :=
    mul_nonneg hw (mul_nonneg hab.le hE)
  have h3 : 0 ≤ a * (1 - a) * (X - Y) ^ 2 := mul_nonneg hab.le (sq_nonneg _)
  have h4 : 0 ≤ a * (1 - a) * (S - T) ^ 2 := mul_nonneg hab.le (sq_nonneg _)
  have h1 : a * (X ^ 2 + S ^ 2) ≤ a * 1 := mul_le_mul_of_nonneg_left hx ha.le
  have h2 : (1 - a) * (Y ^ 2 + T ^ 2) ≤ (1 - a) * 1 := mul_le_mul_of_nonneg_left hy hb.le
  have hDE2 : 0 < D ^ 2 + E ^ 2 := by
    rcases lt_or_eq_of_le hD with hD' | hD'
    · have := pow_pos hD' 2
      nlinarith [sq_nonneg E]
    · have hE' : 0 < E := by linarith
      have := pow_pos hE' 2
      nlinarith [sq_nonneg D]
  have h7 : 0 < (a * (1 - a)) ^ 2 * (D ^ 2 + E ^ 2) := mul_pos (pow_pos hab 2) hDE2
  linarith [h1, h2, h3, h4, h5, h6, h7]

/-- **Ω₄ is strictly convex.** -/
theorem omega4_strictConvex : StrictConvex ℝ omega4 := by
  intro x hx y hy hxy a b ha hb hab
  obtain rfl : b = 1 - a := by linarith
  have hopen : IsOpen {v : Fin 4 → ℝ | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 < 1} :=
    isOpen_lt (by fun_prop) continuous_const
  have hsub : {v : Fin 4 → ℝ | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 < 1} ⊆ omega4 :=
    fun v hv => le_of_lt hv
  refine interior_maximal hsub hopen ?_
  have hx' : (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 + x 3 ^ 4 ≤ 1 := hx
  have hy' : (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2) ^ 2 + y 3 ^ 4 ≤ 1 := hy
  have hDE : 0 < ((x 0 - y 0) ^ 2 + (x 1 - y 1) ^ 2 + (x 2 - y 2) ^ 2) + (x 3 - y 3) ^ 2 := by
    by_contra hle
    push_neg at hle
    apply hxy
    have s0 := sq_nonneg (x 0 - y 0)
    have s1 := sq_nonneg (x 1 - y 1)
    have s2 := sq_nonneg (x 2 - y 2)
    have s3 := sq_nonneg (x 3 - y 3)
    apply vec4_ext
    · exact le_antisymm (by nlinarith) (by nlinarith)
    · exact le_antisymm (by nlinarith) (by nlinarith)
    · exact le_antisymm (by nlinarith) (by nlinarith)
    · exact le_antisymm (by nlinarith) (by nlinarith)
  have e1 : (a * x 0 + (1 - a) * y 0) ^ 2 + (a * x 1 + (1 - a) * y 1) ^ 2
      + (a * x 2 + (1 - a) * y 2) ^ 2
      = a * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) + (1 - a) * (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2)
        - a * (1 - a) * ((x 0 - y 0) ^ 2 + (x 1 - y 1) ^ 2 + (x 2 - y 2) ^ 2) := by ring
  have e3 : (a * x 3 + (1 - a) * y 3) ^ 2
      = a * x 3 ^ 2 + (1 - a) * y 3 ^ 2 - a * (1 - a) * (x 3 - y 3) ^ 2 := by ring
  have e2 : (a * x 3 + (1 - a) * y 3) ^ 4
      = (a * x 3 ^ 2 + (1 - a) * y 3 ^ 2 - a * (1 - a) * (x 3 - y 3) ^ 2) ^ 2 := by ring
  have hz : 0 ≤ a * (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) + (1 - a) * (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2)
      - a * (1 - a) * ((x 0 - y 0) ^ 2 + (x 1 - y 1) ^ 2 + (x 2 - y 2) ^ 2) := by
    rw [← e1]; positivity
  have hw : 0 ≤ a * x 3 ^ 2 + (1 - a) * y 3 ^ 2 - a * (1 - a) * (x 3 - y 3) ^ 2 := by
    rw [← e3]; positivity
  have hD : 0 ≤ (x 0 - y 0) ^ 2 + (x 1 - y 1) ^ 2 + (x 2 - y 2) ^ 2 := by positivity
  have hxx : (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 + (x 3 ^ 2) ^ 2 ≤ 1 := by
    have e : (x 3 ^ 2) ^ 2 = x 3 ^ 4 := by ring
    rw [e]; exact hx'
  have hyy : (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2) ^ 2 + (y 3 ^ 2) ^ 2 ≤ 1 := by
    have e : (y 3 ^ 2) ^ 2 = y 3 ^ 4 := by ring
    rw [e]; exact hy'
  have key := abstract_strict a (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2)
    (x 3 ^ 2) (y 3 ^ 2) ((x 0 - y 0) ^ 2 + (x 1 - y 1) ^ 2 + (x 2 - y 2) ^ 2) ((x 3 - y 3) ^ 2)
    ha hb hz hw hD (sq_nonneg _) hDE hxx hyy
  show ((a • x + (1 - a) • y) 0 ^ 2 + (a • x + (1 - a) • y) 1 ^ 2
      + (a • x + (1 - a) • y) 2 ^ 2) ^ 2 + (a • x + (1 - a) • y) 3 ^ 4 < 1
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  rw [e1, e2]
  exact key

theorem relStrictConvex_omega4 : RelStrictConvex omega4 :=
  relStrictConvex_of_strictConvex omega4_strictConvex

theorem singletonFaces_omega4 (avail : Set ((Fin 4 → ℝ) →ᵃ[ℝ] ℝ)) :
    SingletonFaces omega4 avail :=
  singletonFaces_of_relStrictConvex avail relStrictConvex_omega4

theorem omega4_interior_nonempty : (interior omega4).Nonempty := by
  refine ⟨0, ?_⟩
  have hopen : IsOpen {v : Fin 4 → ℝ | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 < 1} :=
    isOpen_lt (by fun_prop) continuous_const
  have hsub : {v : Fin 4 → ℝ | (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 < 1} ⊆ omega4 :=
    fun v hv => le_of_lt hv
  refine interior_maximal hsub hopen ?_
  show ((0 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (0 : ℝ) ^ 4 < 1
  norm_num

theorem omega4_centrallySymmetric : CentrallySymmetric omega4 0 := by
  intro x hx
  have hx' : (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 + x 3 ^ 4 ≤ 1 := hx
  rw [mem_omega4]
  simp only [Pi.add_apply, Pi.sub_apply, Pi.zero_apply, Pi.neg_apply, zero_add, zero_sub]
  have e : ((-x 0) ^ 2 + (-x 1) ^ 2 + (-x 2) ^ 2) ^ 2 + (-x 3) ^ 4
      = (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 + x 3 ^ 4 := by ring
  rw [e]
  exact hx'

/-! ### §B — the seed -/

/-- The effect `v ↦ (1 + v 3)/2`. -/
noncomputable def seed4 : (Fin 4 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 4 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (LinearMap.proj 3 : (Fin 4 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem seed4_apply (v : Fin 4 → ℝ) : seed4 v = 1 / 2 + v 3 / 2 := by
  simp [seed4] <;> ring

theorem sharpSeed_omega4 : SharpSeed omega4 seed4 := by
  refine ⟨fun x hx => ?_, ⟨![0, 0, 0, 1], ?_, ?_⟩, ⟨![0, 0, 0, -1], ?_, ?_⟩⟩
  · rw [mem_omega4] at hx
    rw [seed4_apply]
    have hq : 0 ≤ (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2) ^ 2 := sq_nonneg _
    have h4 : x 3 ^ 4 ≤ 1 := by linarith
    have h2 : x 3 ^ 2 ≤ 1 := by nlinarith [sq_nonneg (x 3 ^ 2)]
    constructor <;> nlinarith
  · show ((0 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (1 : ℝ) ^ 4 ≤ 1
    norm_num
  · rw [seed4_apply]
    show (1 : ℝ) / 2 + 1 / 2 = 1
    norm_num
  · show ((0 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-1 : ℝ) ^ 4 ≤ 1
    norm_num
  · rw [seed4_apply]
    show (1 : ℝ) / 2 + (-1) / 2 = 0
    norm_num

/-! ### §C — the drive -/

/-- The rotation of the first two coordinates by the angle `t`. -/
noncomputable def rotFun4 (t : ℝ) (v : Fin 4 → ℝ) : Fin 4 → ℝ :=
  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2, v 3]

theorem rotFun4_apply (t : ℝ) (v : Fin 4 → ℝ) :
    rotFun4 t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧
      rotFun4 t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun4 t v 2 = v 2 ∧
        rotFun4 t v 3 = v 3 :=
  ⟨rfl, rfl, rfl, rfl⟩

theorem rotFun4_zero (v : Fin 4 → ℝ) : rotFun4 0 v = v := by
  obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply 0 v
  apply vec4_ext
  · rw [a0, Real.cos_zero, Real.sin_zero]; ring
  · rw [a1, Real.cos_zero, Real.sin_zero]; ring
  · exact a2
  · exact a3

theorem rotFun4_add (s t : ℝ) (v : Fin 4 → ℝ) : rotFun4 s (rotFun4 t v) = rotFun4 (s + t) v := by
  obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply s (rotFun4 t v)
  obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply t v
  obtain ⟨c0, c1, c2, c3⟩ := rotFun4_apply (s + t) v
  apply vec4_ext
  · rw [a0, b0, b1, c0, Real.cos_add, Real.sin_add]; ring
  · rw [a1, b0, b1, c1, Real.cos_add, Real.sin_add]; ring
  · rw [a2, b2, c2]
  · rw [a3, b3, c3]

theorem rotFun4_mem_omega4 (t : ℝ) {v : Fin 4 → ℝ} (hv : v ∈ omega4) : rotFun4 t v ∈ omega4 := by
  obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply t v
  rw [mem_omega4, a0, a1, a2, a3]
  have key : (Real.cos t * v 0 - Real.sin t * v 1) ^ 2 + (Real.sin t * v 0 + Real.cos t * v 1) ^ 2
      = v 0 ^ 2 + v 1 ^ 2 := by
    linear_combination (v 0 ^ 2 + v 1 ^ 2) * Real.sin_sq_add_cos_sq t
  rw [key]
  exact hv

noncomputable def rotLin4 (t : ℝ) : (Fin 4 → ℝ) →ₗ[ℝ] (Fin 4 → ℝ) where
  toFun := rotFun4 t
  map_add' v w := by
    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply t (v + w)
    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply t v
    obtain ⟨c0, c1, c2, c3⟩ := rotFun4_apply t w
    apply vec4_ext <;>
      simp only [Pi.add_apply, a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3] <;> ring
  map_smul' r v := by
    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply t (r • v)
    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply t v
    apply vec4_ext <;>
      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, a3, b0, b1, b2, b3] <;>
      ring

noncomputable def rotEquiv4 (t : ℝ) : (Fin 4 → ℝ) ≃ₗ[ℝ] (Fin 4 → ℝ) :=
  { rotLin4 t with
    invFun := rotFun4 (-t)
    left_inv := fun v => by
      show rotFun4 (-t) (rotFun4 t v) = v
      rw [rotFun4_add, neg_add_cancel, rotFun4_zero]
    right_inv := fun v => by
      show rotFun4 t (rotFun4 (-t) v) = v
      rw [rotFun4_add, add_neg_cancel, rotFun4_zero] }

noncomputable def rot4 (t : ℝ) : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ) := (rotEquiv4 t).toAffineEquiv

theorem rot4_apply (t : ℝ) (v : Fin 4 → ℝ) : rot4 t v = rotFun4 t v := rfl

/-- The cyclic permutation of the first three coordinates, `(x, y, z, s) ↦ (z, x, y, s)`. -/
noncomputable def cycEquiv4 : (Fin 4 → ℝ) ≃ₗ[ℝ] (Fin 4 → ℝ) where
  toFun v := ![v 2, v 0, v 1, v 3]
  invFun v := ![v 1, v 2, v 0, v 3]
  map_add' v w := by apply vec4_ext <;> rfl
  map_smul' r v := by apply vec4_ext <;> rfl
  left_inv v := by apply vec4_ext <;> rfl
  right_inv v := by apply vec4_ext <;> rfl

noncomputable def cyc4 : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ) := cycEquiv4.toAffineEquiv

theorem cyc4_apply (v : Fin 4 → ℝ) :
    cyc4 v 0 = v 2 ∧ cyc4 v 1 = v 0 ∧ cyc4 v 2 = v 1 ∧ cyc4 v 3 = v 3 :=
  ⟨rfl, rfl, rfl, rfl⟩

theorem cyc4_symm_apply (v : Fin 4 → ℝ) :
    cyc4.symm v 0 = v 1 ∧ cyc4.symm v 1 = v 2 ∧ cyc4.symm v 2 = v 0 ∧ cyc4.symm v 3 = v 3 :=
  ⟨rfl, rfl, rfl, rfl⟩

theorem cyc4_mem_omega4 {v : Fin 4 → ℝ} (hv : v ∈ omega4) : cyc4 v ∈ omega4 := by
  obtain ⟨c0, c1, c2, c3⟩ := cyc4_apply v
  rw [mem_omega4, c0, c1, c2, c3]
  rw [mem_omega4] at hv
  have e : (v 2 ^ 2 + v 0 ^ 2 + v 1 ^ 2) ^ 2 + v 3 ^ 4
      = (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 := by ring
  rw [e]
  exact hv

theorem cyc4_symm_mem_omega4 {v : Fin 4 → ℝ} (hv : v ∈ omega4) : cyc4.symm v ∈ omega4 := by
  obtain ⟨c0, c1, c2, c3⟩ := cyc4_symm_apply v
  rw [mem_omega4, c0, c1, c2, c3]
  rw [mem_omega4] at hv
  have e : (v 1 ^ 2 + v 2 ^ 2 + v 0 ^ 2) ^ 2 + v 3 ^ 4
      = (v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) ^ 2 + v 3 ^ 4 := by ring
  rw [e]
  exact hv

/-- **Ω₄ is drivable.** -/
noncomputable def omega4Drive : ElementaryDrivability omega4 where
  flow := rot4
  flow_zero := AffineEquiv.ext fun v => by rw [rot4_apply, rotFun4_zero, AffineEquiv.refl_apply]
  flow_add s t := AffineEquiv.ext fun v => by
    simp only [AffineEquiv.trans_apply, rot4_apply, rotFun4_add]
  flow_continuous := by
    refine continuous_pi fun i => ?_
    fin_cases i
    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => q.2 2
      fun_prop
    · show Continuous fun q : ℝ × (Fin 4 → ℝ) => q.2 3
      fun_prop
  flow_preserves t _ hv := rotFun4_mem_omega4 t hv
  t₀ := Real.pi
  N_involutive x _ := by
    simp only [rot4_apply]
    obtain ⟨a0, a1, a2, a3⟩ := rotFun4_apply Real.pi (rotFun4 Real.pi x)
    obtain ⟨b0, b1, b2, b3⟩ := rotFun4_apply Real.pi x
    apply vec4_ext
    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a2, b2]
    · rw [a3, b3]
  N_moves := ⟨![1, 0, 0, 0], by show ((1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num,
    fun h => by
      have h0 : rot4 Real.pi ![1, 0, 0, 0] 0 = (![1, 0, 0, 0] : Fin 4 → ℝ) 0 := congrFun h 0
      change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0
      rw [Real.cos_pi, Real.sin_pi] at h0
      norm_num at h0⟩
  J := cyc4
  J_preserves _ hv := cyc4_mem_omega4 hv
  J_symm_preserves _ hv := cyc4_symm_mem_omega4 hv
  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1, 0],
    by show ((0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num, fun h => by
      have h2 : cyc4 (rot4 Real.pi (cyc4.symm ![0, 0, 1, 0])) 2 = rot4 s ![0, 0, 1, 0] 2 :=
        congrFun h 2
      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2
      rw [Real.sin_pi, Real.cos_pi] at h2
      norm_num at h2⟩⟩

theorem omega4_drivable : Nonempty (ElementaryDrivability omega4) := ⟨omega4Drive⟩

/-! ### §D — Ω₄ is no affine image of the ball -/

/-- **Ω₄ is not an ellipsoid.** In the plane of the first and last axes, no quadric contains the
eight states `(±1, 0)`, `(0, ±1)`, `(±5/6, ±5/6)` and excludes the eight points `(±1, ±1/2)`,
`(±1/2, ±1)`; the affine image of a ball cut by that plane would be such a quadric. -/
theorem not_affine_eball_omega4 :
    ¬ ∃ A : (Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ), A '' omega4 = eball 4 := by
  rintro ⟨A, hA⟩
  have hin : ∀ x, x ∈ omega4 → ∑ j, (A x j) ^ 2 ≤ 1 := by
    intro x hx
    have hx' : A x ∈ A '' omega4 := Set.mem_image_of_mem A hx
    rw [hA] at hx'
    exact hx'
  have hout : ∀ x, x ∉ omega4 → 1 < ∑ j, (A x j) ^ 2 := by
    intro x hx
    by_contra hle
    have hle' : ∑ j, (A x j) ^ 2 ≤ 1 := not_lt.mp hle
    have hmem : A x ∈ A '' omega4 := by
      rw [hA]
      exact hle'
    obtain ⟨y, hy, hyx⟩ := hmem
    have hxy : y = x := A.injective hyx
    rw [hxy] at hy
    exact hx hy
  have hdec : ∀ x : Fin 4 → ℝ, A x = A.linear x + A 0 := by
    intro x
    have h := A.map_vadd 0 x
    simp only [vadd_eq_add, add_zero] at h
    exact h
  have hv : ∀ u s : ℝ, (![u, 0, 0, s] : Fin 4 → ℝ) = u • ![1, 0, 0, 0] + s • ![0, 0, 0, 1] := by
    intro u s
    apply vec4_ext <;> simp
  obtain ⟨a, ha⟩ : ∃ a : Fin 4 → ℝ, a = A.linear ![1, 0, 0, 0] := ⟨_, rfl⟩
  obtain ⟨c, hc⟩ : ∃ c : Fin 4 → ℝ, c = A.linear ![0, 0, 0, 1] := ⟨_, rfl⟩
  obtain ⟨p, hp⟩ : ∃ p : Fin 4 → ℝ, p = A 0 := ⟨_, rfl⟩
  have hcoord : ∀ (u s : ℝ) (j : Fin 4), A ![u, 0, 0, s] j = u * a j + s * c j + p j := by
    intro u s j
    rw [hdec ![u, 0, 0, s], hv u s, map_add, map_smul, map_smul, ha, hc, hp]
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  obtain ⟨α, hα⟩ : ∃ α : ℝ, α = a 0 ^ 2 + a 1 ^ 2 + a 2 ^ 2 + a 3 ^ 2 := ⟨_, rfl⟩
  obtain ⟨β, hβ⟩ : ∃ β : ℝ, β = c 0 ^ 2 + c 1 ^ 2 + c 2 ^ 2 + c 3 ^ 2 := ⟨_, rfl⟩
  obtain ⟨γ, hγ⟩ : ∃ γ : ℝ, γ = a 0 * c 0 + a 1 * c 1 + a 2 * c 2 + a 3 * c 3 := ⟨_, rfl⟩
  obtain ⟨b₀, hb₀⟩ : ∃ b : ℝ, b = a 0 * p 0 + a 1 * p 1 + a 2 * p 2 + a 3 * p 3 := ⟨_, rfl⟩
  obtain ⟨b₃, hb₃⟩ : ∃ b : ℝ, b = c 0 * p 0 + c 1 * p 1 + c 2 * p 2 + c 3 * p 3 := ⟨_, rfl⟩
  obtain ⟨P, hP⟩ : ∃ P : ℝ, P = p 0 ^ 2 + p 1 ^ 2 + p 2 ^ 2 + p 3 ^ 2 := ⟨_, rfl⟩
  have hsum : ∀ u s : ℝ, ∑ j, (A ![u, 0, 0, s] j) ^ 2
      = u ^ 2 * α + s ^ 2 * β + 2 * u * s * γ + 2 * u * b₀ + 2 * s * b₃ + P := by
    intro u s
    simp only [hcoord, Fin.sum_univ_four, hα, hβ, hγ, hb₀, hb₃, hP]
    ring
  have i1 := hin ![1, 0, 0, 0] (by show ((1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num)
  have i2 := hin ![-1, 0, 0, 0]
    (by show ((-1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (0 : ℝ) ^ 4 ≤ 1; norm_num)
  have i3 := hin ![0, 0, 0, 1] (by show ((0 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (1 : ℝ) ^ 4 ≤ 1; norm_num)
  have i4 := hin ![0, 0, 0, -1]
    (by show ((0 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-1 : ℝ) ^ 4 ≤ 1; norm_num)
  have i5 := hin ![5 / 6, 0, 0, 5 / 6]
    (by show (((5 : ℝ) / 6) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + ((5 : ℝ) / 6) ^ 4 ≤ 1; norm_num)
  have i6 := hin ![5 / 6, 0, 0, -(5 / 6)]
    (by show (((5 : ℝ) / 6) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-((5 : ℝ) / 6)) ^ 4 ≤ 1; norm_num)
  have i7 := hin ![-(5 / 6), 0, 0, 5 / 6]
    (by show ((-((5 : ℝ) / 6)) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + ((5 : ℝ) / 6) ^ 4 ≤ 1; norm_num)
  have i8 := hin ![-(5 / 6), 0, 0, -(5 / 6)]
    (by show ((-((5 : ℝ) / 6)) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-((5 : ℝ) / 6)) ^ 4 ≤ 1; norm_num)
  have o1 := hout ![1, 0, 0, 1 / 2]
    (by show ¬ (((1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + ((1 : ℝ) / 2) ^ 4 ≤ 1); norm_num)
  have o2 := hout ![1, 0, 0, -(1 / 2)]
    (by show ¬ (((1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-((1 : ℝ) / 2)) ^ 4 ≤ 1); norm_num)
  have o3 := hout ![-1, 0, 0, 1 / 2]
    (by show ¬ (((-1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + ((1 : ℝ) / 2) ^ 4 ≤ 1); norm_num)
  have o4 := hout ![-1, 0, 0, -(1 / 2)]
    (by show ¬ (((-1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-((1 : ℝ) / 2)) ^ 4 ≤ 1); norm_num)
  have o5 := hout ![1 / 2, 0, 0, 1]
    (by show ¬ ((((1 : ℝ) / 2) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (1 : ℝ) ^ 4 ≤ 1); norm_num)
  have o6 := hout ![1 / 2, 0, 0, -1]
    (by show ¬ ((((1 : ℝ) / 2) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-1 : ℝ) ^ 4 ≤ 1); norm_num)
  have o7 := hout ![-(1 / 2), 0, 0, 1]
    (by show ¬ (((-((1 : ℝ) / 2)) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (1 : ℝ) ^ 4 ≤ 1); norm_num)
  have o8 := hout ![-(1 / 2), 0, 0, -1]
    (by show ¬ (((-((1 : ℝ) / 2)) ^ 2 + 0 ^ 2 + 0 ^ 2) ^ 2 + (-1 : ℝ) ^ 4 ≤ 1); norm_num)
  rw [hsum] at i1 i2 i3 i4 i5 i6 i7 i8 o1 o2 o3 o4 o5 o6 o7 o8
  linarith

/-! ### §E — the separation -/

theorem not_boundaryTransitive_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}
    (hG : PreservesBody omega4 G) : ¬ BoundaryTransitive omega4 G := fun hT =>
  not_affine_eball_omega4 (exists_affine_image_eq_eball (by norm_num) omega4_isCompact
    omega4_convex omega4_interior_nonempty hG hT)

theorem not_denseBoundaryOrbit_omega4 {G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ))}
    (hG : PreservesBody omega4 G) : ¬ DenseBoundaryOrbit omega4 G := fun hT =>
  not_affine_eball_omega4 (exists_affine_image_eq_eball_of_dense (by norm_num) omega4_isCompact
    omega4_convex omega4_interior_nonempty hG hT)

/-- **The separation of K∞-Trans.** Ω₄ is a compact convex body with interior that is drivable,
carries a sharp seed, is relatively strictly convex and centrally symmetric, and on which no
body-preserving family is boundary transitive or has a dense boundary orbit. -/
theorem kinfTrans_separation :
    IsCompact omega4 ∧ Convex ℝ omega4 ∧ (interior omega4).Nonempty
      ∧ Nonempty (ElementaryDrivability omega4) ∧ SharpSeed omega4 seed4
      ∧ RelStrictConvex omega4 ∧ CentrallySymmetric omega4 0
      ∧ ∀ G : Set ((Fin 4 → ℝ) ≃ᵃ[ℝ] (Fin 4 → ℝ)), PreservesBody omega4 G →
          ¬ BoundaryTransitive omega4 G ∧ ¬ DenseBoundaryOrbit omega4 G :=
  ⟨omega4_isCompact, omega4_convex, omega4_interior_nonempty, omega4_drivable, sharpSeed_omega4,
    relStrictConvex_omega4, omega4_centrallySymmetric,
    fun _ hG => ⟨not_boundaryTransitive_omega4 hG, not_denseBoundaryOrbit_omega4 hG⟩⟩

end

end EqvOmega4
end OIBridge

#print axioms OIBridge.EqvOmega4.omega4_isCompact
#print axioms OIBridge.EqvOmega4.conv_core
#print axioms OIBridge.EqvOmega4.omega4_convex
#print axioms OIBridge.EqvOmega4.abstract_strict
#print axioms OIBridge.EqvOmega4.omega4_strictConvex
#print axioms OIBridge.EqvOmega4.relStrictConvex_omega4
#print axioms OIBridge.EqvOmega4.singletonFaces_omega4
#print axioms OIBridge.EqvOmega4.omega4_interior_nonempty
#print axioms OIBridge.EqvOmega4.omega4_centrallySymmetric
#print axioms OIBridge.EqvOmega4.sharpSeed_omega4
#print axioms OIBridge.EqvOmega4.omega4_drivable
#print axioms OIBridge.EqvOmega4.not_affine_eball_omega4
#print axioms OIBridge.EqvOmega4.not_boundaryTransitive_omega4
#print axioms OIBridge.EqvOmega4.not_denseBoundaryOrbit_omega4
#print axioms OIBridge.EqvOmega4.kinfTrans_separation
