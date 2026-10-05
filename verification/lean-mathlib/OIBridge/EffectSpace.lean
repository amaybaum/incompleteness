/-
  OIBridge/EffectSpace.lean — round EFF-1: the effect set and the product-test cone of the coordinate
  Euclidean ball `eball d`, for every `d ≥ 1`, in the field-neutral vocabulary of `KInfFoundations`,
  `OrbitGeneration` and `CompositeDimension`.

  Two separate questions, each with its own theorems and hypotheses.

  (Q-CONE) Which test functionals determine the maximal product cone `maxCone (eball d)` of round
  DIM-1. The sharp directional effects `sharpEff b`, `b` a unit vector, determine it: the cone of
  joint vectors nonnegative on every product of two sharp effects is `maxCone (eball d)`, one
  theorem per inclusion (`maxCone_subset_maxConeOf_sharp`, `maxConeOf_sharp_subset_maxCone`), for
  `0 < d`. Under OG-1's named hypotheses on `eball d` — a body-preserving family `G`, a sharp seed,
  boundary transitivity and seed-orbit availability — every sharp effect is available
  (`sharpFamily_subset_avail`), with no mixing closure and no unit premise, so the available family
  determines the same cone once every available functional is an effect (`maxConeOf_avail_eq`).
  This is a statement about which test functionals determine the dual product cone; it does not
  assert that every affine effect is available.

  (Q-SET) Operational availability of the full affine effect set. Every effect on `eball d` is
  `r ↦ a + v · r` with `√(v · v) ≤ min a (1 − a)`, and conversely (`effect_eq_affine`,
  `isEffectOn_of_affine`); every effect is a sub-convex combination of the unit with one sharp
  effect, and conversely (`fullEffects_subset_unitSpan`, `unitSpan_subset_fullEffects`). Under
  OG-1's named hypotheses with the unit available and the named mixing closure `MixingClosed`, every
  effect is available (`fullEffects_subset_avail`). Without the mixing closure the full set does not
  follow: the sharp family with the unit satisfies OG-1's four hypotheses under the full
  automorphism family, contains the unit, consists of effects, and is neither mixing closed nor the
  full effect set (`not_fullEffects_of_orbit`), for every `0 < d`.

  Controls: at `d = 0` the sharp family is empty and does not determine the cone
  (`maxConeOf_sharpFamily_zero_ne`); at `d = 3` the effects of one axis with the unit determine a
  strictly larger cone (`maxConeOf_axis_ne`), so directional coverage is load-bearing for the cone;
  a countable family is never boundary transitive on `eball 3` (`not_boundaryTransitive_of_countable`).

  The named hypotheses (the seed, the orbit, transitivity, seed-orbit availability, the unit and the
  mixing closure) are premises; nothing here sources them from any construction. No limit closure,
  no drive, no one-parameter motion, no complex structure and no matrix representation is used or
  claimed.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositeDimension
import OIBridge.CompositeInterface
import Mathlib.Analysis.Real.Cardinality

namespace OIBridge
namespace EffectSpace

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface

variable {d : ℕ}

/-! ### §A — sharp directional effects of `eball d` -/

/-- The homogenized coefficients of the sharp directional effect along `b`. -/
noncomputable def sharpVec (b : Fin d → ℝ) : HVec d := Matrix.vecCons (1 / 2) fun j => b j / 2

theorem sharpVec_zero (b : Fin d → ℝ) : sharpVec b 0 = 1 / 2 := rfl

theorem sharpVec_succ (b : Fin d → ℝ) (j : Fin d) : sharpVec b j.succ = b j / 2 :=
  Matrix.cons_val_succ _ _ _

/-- The sharp directional effect along `b`: `x ↦ 1/2 + (b · x)/2`. -/
noncomputable def sharpEff (b : Fin d → ℝ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := affOf (sharpVec b)

theorem sharpEff_apply (b x : Fin d → ℝ) : sharpEff b x = 1 / 2 + ∑ j, b j / 2 * x j := by
  rw [sharpEff, affOf_apply, sharpVec_zero]
  simp only [sharpVec_succ]

/-- The sharp directional family of `eball d`: the sharp effects along unit vectors. -/
def sharpFamily (d : ℕ) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ b : Fin d → ℝ, ∑ j, b j ^ 2 = 1 ∧ e = sharpEff b}

theorem sum_neg_sq (b : Fin d → ℝ) : ∑ j, (-b) j ^ 2 = ∑ j, b j ^ 2 :=
  Finset.sum_congr rfl fun j _ => by rw [Pi.neg_apply, neg_sq]

theorem mem_eball_of_sphere {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : b ∈ eball d := by
  rw [mem_eball, hb]

theorem neg_mem_eball {x : Fin d → ℝ} (hx : x ∈ eball d) : -x ∈ eball d := by
  rw [mem_eball, sum_neg_sq]
  exact hx

theorem zero_mem_eball : (0 : Fin d → ℝ) ∈ eball d := by
  rw [mem_eball]
  simp

theorem lor_sharpVec {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : Lor (sharpVec b) := by
  refine ⟨by rw [sharpVec_zero]; norm_num, ?_⟩
  have h : ∑ j : Fin d, sharpVec b j.succ ^ 2 = (∑ j, b j ^ 2) / 4 := by
    rw [Finset.sum_div]
    exact Finset.sum_congr rfl fun j _ => by rw [sharpVec_succ]; ring
  rw [h, hb, sharpVec_zero]
  norm_num

theorem sharpEff_isEffectOn {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :
    IsEffectOn (eball d) (sharpEff b) :=
  isEffectOn_affOf (lor_sharpVec hb) (le_of_eq (sharpVec_zero b))

theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b b = 1 := by
  rw [sharpEff_apply]
  have h : ∑ j, b j / 2 * b j = (∑ j, b j ^ 2) / 2 := by
    rw [Finset.sum_div]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [h, hb]
  norm_num

theorem sharpEff_neg_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b (-b) = 0 := by
  rw [sharpEff_apply]
  have h : ∑ j, b j / 2 * (-b) j = -((∑ j, b j ^ 2) / 2) := by
    rw [Finset.sum_div, ← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun j _ => by rw [Pi.neg_apply]; ring
  rw [h, hb]
  norm_num

/-- Every sharp directional effect is a sharp seed of `eball d`. -/
theorem sharpEff_sharpSeed {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :
    SharpSeed (eball d) (sharpEff b) :=
  ⟨sharpEff_isEffectOn hb, ⟨b, mem_eball_of_sphere hb, sharpEff_self hb⟩,
    ⟨-b, neg_mem_eball (mem_eball_of_sphere hb), sharpEff_neg_self hb⟩⟩

/-- A unit vector is a boundary state of `eball d`. -/
theorem isBoundaryState_eball_of_sphere {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) :
    IsBoundaryState (eball d) b :=
  sharpSeed_certain_isBoundaryState (sharpEff_sharpSeed hb) (mem_eball_of_sphere hb)
    (sharpEff_self hb)

/-- A boundary state of `eball d` is a unit vector. -/
theorem sphere_of_isBoundaryState_eball {x : Fin d → ℝ} (h : IsBoundaryState (eball d) x) :
    ∑ j, x j ^ 2 = 1 := by
  obtain ⟨hx, y, hy, hout⟩ := h
  rw [mem_eball] at hx hy
  by_contra hne
  have hlt := lt_of_le_of_ne hx hne
  set t := (1 - ∑ j, x j ^ 2) / 9 with ht
  have htp : 0 < t := by rw [ht]; linarith
  have ht1 : t ≤ 1 := by
    have : 0 ≤ ∑ j, x j ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
    rw [ht]; linarith
  apply hout t htp
  rw [mem_eball]
  have hexp : ∑ j, (x + t • (x - y)) j ^ 2 =
      ∑ j, x j ^ 2 + t * ∑ j, 2 * (x j * (x j - y j)) + t ^ 2 * ∑ j, (x j - y j) ^ 2 := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by
      simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
      ring
  have hb1 : ∑ j, 2 * (x j * (x j - y j)) ≤ 5 := by
    have hp : ∀ j, 2 * (x j * (x j - y j)) ≤ 3 * x j ^ 2 + 2 * y j ^ 2 := fun j => by
      nlinarith [sq_nonneg (x j - y j), sq_nonneg (x j + y j), sq_nonneg (x j)]
    calc ∑ j, 2 * (x j * (x j - y j)) ≤ ∑ j, (3 * x j ^ 2 + 2 * y j ^ 2) :=
          Finset.sum_le_sum fun j _ => hp j
      _ = 3 * ∑ j, x j ^ 2 + 2 * ∑ j, y j ^ 2 := by
          rw [Finset.sum_add_distrib, Finset.mul_sum, Finset.mul_sum]
      _ ≤ 5 := by linarith
  have hb2 : ∑ j, (x j - y j) ^ 2 ≤ 4 := by
    have hp : ∀ j, (x j - y j) ^ 2 ≤ 2 * x j ^ 2 + 2 * y j ^ 2 := fun j => by
      nlinarith [sq_nonneg (x j + y j)]
    calc ∑ j, (x j - y j) ^ 2 ≤ ∑ j, (2 * x j ^ 2 + 2 * y j ^ 2) :=
          Finset.sum_le_sum fun j _ => hp j
      _ = 2 * ∑ j, x j ^ 2 + 2 * ∑ j, y j ^ 2 := by
          rw [Finset.sum_add_distrib, Finset.mul_sum, Finset.mul_sum]
      _ ≤ 4 := by linarith
  rw [hexp]
  have h2 : t ^ 2 * ∑ j, (x j - y j) ^ 2 ≤ t * 4 := by
    have h0 : 0 ≤ ∑ j, (x j - y j) ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
    nlinarith
  have h1 : t * ∑ j, 2 * (x j * (x j - y j)) ≤ t * 5 := mul_le_mul_of_nonneg_left hb1 htp.le
  have h9 : t * 9 = 1 - ∑ j, x j ^ 2 := by rw [ht]; ring
  linarith

/-- An affine functional in homogenized coordinates. -/
theorem ehom_apply (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :
    e x = ehom e 0 + ∑ j, ehom e j.succ * x j := by
  rw [ehom_dot e x, Fin.sum_univ_succ, hom_zero, mul_one]
  simp only [hom_succ]

/-- **Sharpness forces the directional normalization.** An effect on `eball d` certain at `u` and
zero at `w` is the sharp effect along `u`, and `u` is a unit vector. -/
theorem sharp_eq_of_certain {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) r)
    {u w : Fin d → ℝ} (hu : u ∈ eball d) (hw : w ∈ eball d) (h1 : r u = 1) (h0 : r w = 0) :
    ∑ j, u j ^ 2 = 1 ∧ r = sharpEff u := by
  have hL := lor_ehom he
  have hb := (lor_pair_bound hL hu).2
  have hm := (he (-w) (neg_mem_eball hw)).2
  rw [ehom_apply] at h1 h0 hm
  have hneg : ∑ j, ehom r j.succ * (-w) j = -∑ j, ehom r j.succ * w j := by
    rw [← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun j _ => by rw [Pi.neg_apply]; ring
  rw [hneg] at hm
  have hc : ehom r 0 = 1 / 2 := by linarith
  have hau : ∑ j, ehom r j.succ * u j = 1 / 2 := by linarith
  have ha2 : ∑ j : Fin d, ehom r j.succ ^ 2 ≤ 1 / 4 := by
    have := hL.2
    rw [hc] at this
    linarith
  rw [mem_eball] at hu
  have hexp : ∑ j, (u j - 2 * ehom r j.succ) ^ 2 =
      ∑ j, u j ^ 2 - 4 * ∑ j, ehom r j.succ * u j + 4 * ∑ j, ehom r j.succ ^ 2 := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  have hle : ∑ j, (u j - 2 * ehom r j.succ) ^ 2 ≤ 0 := by rw [hexp]; linarith
  have hz : ∀ j, u j = 2 * ehom r j.succ := by
    intro j
    have hzero := (Finset.sum_eq_zero_iff_of_nonneg
      (fun j _ => sq_nonneg (u j - 2 * ehom r j.succ))).1
      (le_antisymm hle (Finset.sum_nonneg fun j _ => sq_nonneg _)) j (Finset.mem_univ j)
    have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hzero
    linarith
  have hu2 : ∑ j, u j ^ 2 = 4 * ∑ j, ehom r j.succ ^ 2 := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by rw [hz j]; ring
  have hau2 : ∑ j, ehom r j.succ * u j = 2 * ∑ j, ehom r j.succ ^ 2 := by
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun j _ => by rw [hz j]; ring
  refine ⟨by linarith, ?_⟩
  refine AffineMap.ext fun x => ?_
  rw [ehom_apply r x, sharpEff_apply, hc]
  congr 1
  exact Finset.sum_congr rfl fun j _ => by rw [hz j]; ring

/-! ### §B — the full automorphism family of `eball d` and its reflections -/

/-- The full automorphism family of `eball d`: every affine automorphism that, with its inverse,
maps the ball into itself. -/
def fullAut (d : ℕ) : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)) :=
  {g | ∀ x ∈ eball d, g x ∈ eball d ∧ g.symm x ∈ eball d}

theorem preservesBody_fullAut : PreservesBody (eball d) (fullAut d) := fun _ hg => hg

/-- The reflection in the hyperplane orthogonal to `m`. -/
noncomputable def reflLin (m : Fin d → ℝ) : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ) where
  toFun x := x - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) • m
  map_add' x y := by
    have h : ∑ j, (x + y) j * m j = ∑ j, x j * m j + ∑ j, y j * m j := by
      rw [← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun j _ => by rw [Pi.add_apply]; ring
    funext i
    simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul, h]
    ring
  map_smul' c x := by
    have h : ∑ j, (c • x) j * m j = c * ∑ j, x j * m j := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ => by rw [Pi.smul_apply, smul_eq_mul]; ring
    funext i
    simp only [Pi.smul_apply, Pi.sub_apply, smul_eq_mul, RingHom.id_apply, h]
    ring

theorem reflLin_apply (m x : Fin d → ℝ) :
    reflLin m x = x - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) • m := rfl

theorem reflLin_dot {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :
    ∑ j, reflLin m x j * m j = -∑ j, x j * m j := by
  have h : ∑ j, reflLin m x j * m j =
      ∑ j, x j * m j - (2 * (∑ j, x j * m j) / ∑ j, m j ^ 2) * ∑ j, m j ^ 2 := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun j _ => by
      rw [reflLin_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
      ring
  rw [h, div_mul_cancel₀ _ hm]
  ring

theorem reflLin_reflLin {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :
    reflLin m (reflLin m x) = x := by
  have hd := reflLin_dot hm x
  funext i
  rw [reflLin_apply, hd]
  simp only [reflLin_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem reflLin_sq {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :
    ∑ j, reflLin m x j ^ 2 = ∑ j, x j ^ 2 := by
  set k := 2 * (∑ j, x j * m j) / ∑ j, m j ^ 2 with hk
  have h : ∑ j, reflLin m x j ^ 2 =
      ∑ j, x j ^ 2 - 2 * k * ∑ j, x j * m j + k ^ 2 * ∑ j, m j ^ 2 := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by
      rw [reflLin_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
      ring
  rw [h]
  have hkq : k * ∑ j, m j ^ 2 = 2 * ∑ j, x j * m j := by
    rw [hk, div_mul_cancel₀ _ hm]
  have : k ^ 2 * ∑ j, m j ^ 2 = k * (2 * ∑ j, x j * m j) := by
    rw [← hkq]; ring
  rw [this]
  ring

/-- The reflection as an affine automorphism. -/
noncomputable def reflAff {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) :
    (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) :=
  (LinearEquiv.ofInvolutive (reflLin m) (reflLin_reflLin hm)).toAffineEquiv

theorem reflAff_apply {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :
    reflAff hm x = reflLin m x := rfl

theorem reflAff_symm_apply {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) (x : Fin d → ℝ) :
    (reflAff hm).symm x = reflLin m x := by
  have h := (reflAff hm).symm_apply_apply (reflLin m x)
  rw [reflAff_apply, reflLin_reflLin hm] at h
  exact h.symm

theorem reflAff_mem_fullAut {m : Fin d → ℝ} (hm : ∑ j, m j ^ 2 ≠ 0) : reflAff hm ∈ fullAut d := by
  intro x hx
  rw [mem_eball] at hx
  refine ⟨?_, ?_⟩
  · rw [reflAff_apply, mem_eball, reflLin_sq hm]; exact hx
  · rw [reflAff_symm_apply, mem_eball, reflLin_sq hm]; exact hx

theorem refl_mem_fullAut : AffineEquiv.refl ℝ (Fin d → ℝ) ∈ fullAut d := fun x hx =>
  ⟨hx, hx⟩

/-- The reflection exchanging two distinct unit vectors. -/
theorem reflLin_swap {u v : Fin d → ℝ} (hu : ∑ j, u j ^ 2 = 1) (hv : ∑ j, v j ^ 2 = 1)
    (hm : ∑ j, (u - v) j ^ 2 ≠ 0) : reflLin (u - v) u = v := by
  have hq : ∑ j, (u - v) j ^ 2 = 2 * ∑ j, u j * (u - v) j := by
    have h1 : ∑ j, (u - v) j ^ 2 = ∑ j, u j ^ 2 - 2 * ∑ j, u j * v j + ∑ j, v j ^ 2 := by
      rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
      exact Finset.sum_congr rfl fun j _ => by rw [Pi.sub_apply]; ring
    have h2 : ∑ j, u j * (u - v) j = ∑ j, u j ^ 2 - ∑ j, u j * v j := by
      rw [← Finset.sum_sub_distrib]
      exact Finset.sum_congr rfl fun j _ => by rw [Pi.sub_apply]; ring
    rw [h1, h2, hu, hv]
    ring
  have hk : 2 * (∑ j, u j * (u - v) j) / ∑ j, (u - v) j ^ 2 = 1 := by
    rw [hq] at hm ⊢
    exact div_self hm
  rw [reflLin_apply, hk, one_smul]
  abel

/-- The full automorphism family is boundary transitive on `eball d`. -/
theorem boundaryTransitive_fullAut : BoundaryTransitive (eball d) (fullAut d) := by
  intro u v hu hv
  have hu1 := sphere_of_isBoundaryState_eball hu
  have hv1 := sphere_of_isBoundaryState_eball hv
  by_cases huv : u = v
  · exact ⟨AffineEquiv.refl ℝ (Fin d → ℝ), refl_mem_fullAut, by rw [huv]; rfl⟩
  · have hm : ∑ j, (u - v) j ^ 2 ≠ 0 := by
      intro h0
      apply huv
      funext j
      have hj := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg ((u - v) j))).1 h0 j
        (Finset.mem_univ j)
      have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hj
      rw [Pi.sub_apply] at this
      linarith
    exact ⟨reflAff hm, reflAff_mem_fullAut hm, by rw [reflAff_apply]; exact reflLin_swap hu1 hv1 hm⟩

/-! ### §C — generation of the sharp family from OG-1's named hypotheses -/

section Generation

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- Every transport of a sharp seed along a body-preserving map is a sharp directional effect. -/
theorem seedTransport_mem_sharpFamily (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) {g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hg : g ∈ G) :
    seedTransport r g ∈ sharpFamily d := by
  obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := hP1
  have ht : IsEffectOn (eball d) (seedTransport r g) :=
    isEffectOn_seedTransport he fun x hx => (hG g hg x hx).2
  obtain ⟨hs, heq⟩ := sharp_eq_of_certain ht (hG g hg u hu).1 (hG g hg w hw).1
    (by rw [seedTransport_apply_apply, h1]) (by rw [seedTransport_apply_apply, h0])
  exact ⟨g u, hs, heq⟩

/-- **Generation of the sharp family.** Under OG-1's four named hypotheses on `eball d`, every sharp
directional effect is available. No mixing closure and no unit premise is used. -/
theorem sharpFamily_subset_avail (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) :
    sharpFamily d ⊆ avail := by
  rintro e ⟨b, hb, rfl⟩
  obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := hP1
  have hbu : IsBoundaryState (eball d) u :=
    sharpSeed_certain_isBoundaryState ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ hu h1
  obtain ⟨g, hg, hgu⟩ := hK u b hbu (isBoundaryState_eball_of_sphere hb)
  have ht : IsEffectOn (eball d) (seedTransport r g) :=
    isEffectOn_seedTransport he fun x hx => (hG g hg x hx).2
  have ht1 : seedTransport r g b = 1 := by rw [← hgu, seedTransport_apply_apply, h1]
  have ht0 : seedTransport r g (g w) = 0 := by rw [seedTransport_apply_apply, h0]
  obtain ⟨-, heq⟩ := sharp_eq_of_certain ht (mem_eball_of_sphere hb) (hG g hg w hw).1 ht1 ht0
  rw [← heq]
  exact hV4 g hg

theorem seedOrbit_subset_sharpFamily (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) : seedOrbit G r ⊆ sharpFamily d := by
  rintro f ⟨g, hg, rfl⟩
  exact seedTransport_mem_sharpFamily hG hP1 hg

theorem sharpFamily_subset_seedOrbit (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G) :
    sharpFamily d ⊆ seedOrbit G r :=
  sharpFamily_subset_avail hG hP1 hK (seedOrbitAvailable_self G r)

/-- The seed orbit is the sharp family, one theorem per inclusion. -/
theorem seedOrbit_eq_sharpFamily (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) : seedOrbit G r = sharpFamily d :=
  Set.Subset.antisymm (seedOrbit_subset_sharpFamily hG hP1)
    (sharpFamily_subset_seedOrbit hG hP1 hK)

end Generation

/-! ### §D — Q-CONE: the sharp family determines the product-test cone -/

/-- The cone of joint vectors nonnegative on every product of two members of `A`. -/
def maxConeOf (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set (W d) :=
  {ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}

/-- DIM-1's maximal cone is the cone of the full effect family. -/
theorem maxConeOf_fullEffects (Ω : Set (Fin d → ℝ)) : maxConeOf (fullEffects Ω) = maxCone Ω := by
  ext ω
  show (∀ e ∈ fullEffects Ω, ∀ f ∈ fullEffects Ω, 0 ≤ prodEffVal e f ω) ↔
    ∀ e f, IsEffectOn Ω e → IsEffectOn Ω f → 0 ≤ prodEffVal e f ω
  exact ⟨fun h e f he hf => h e he f hf, fun h e he f hf => h e f he hf⟩

theorem maxConeOf_anti {A B : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (h : A ⊆ B) :
    maxConeOf B ⊆ maxConeOf A := by
  intro ω hω
  show ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω
  intro e he f hf
  exact hω e (h he) f (h hf)

/-- The unit vector along the first axis. -/
noncomputable def axisVec (hd : 0 < d) : Fin d → ℝ := Pi.single (⟨0, hd⟩ : Fin d) 1

theorem axisVec_sq (hd : 0 < d) : ∑ j, axisVec hd j ^ 2 = 1 := by
  rw [Finset.sum_eq_single (⟨0, hd⟩ : Fin d)]
  · simp [axisVec]
  · intro j _ hj
    simp [axisVec, Pi.single_apply, hj]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- The homogenized unit is the sum of two opposite sharp vectors. -/
theorem hom_zero_eq_sharp (b : Fin d → ℝ) : hom (0 : Fin d → ℝ) = sharpVec b + sharpVec (-b) := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i
  · rw [hom_zero, Pi.add_apply, sharpVec_zero, sharpVec_zero]
    norm_num
  · rw [hom_succ, Pi.add_apply, sharpVec_succ, sharpVec_succ, Pi.neg_apply, Pi.zero_apply]
    ring

/-- A cone vector is a nonnegative combination of the homogenized unit and one sharp vector. -/
theorem lor_decomp (hd : 0 < d) {v : HVec d} (hv : Lor v) :
    ∃ α β : ℝ, ∃ b : Fin d → ℝ, 0 ≤ α ∧ 0 ≤ β ∧ ∑ j, b j ^ 2 = 1 ∧
      v = α • hom (0 : Fin d → ℝ) + β • sharpVec b := by
  obtain ⟨h0, hs⟩ := hv
  obtain ⟨t, ht⟩ : ∃ t : ℝ, t = ∑ j : Fin d, v j.succ ^ 2 := ⟨_, rfl⟩
  rw [← ht] at hs
  have ht0 : 0 ≤ t := ht ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  rcases eq_or_lt_of_le ht0 with hz | hpos
  · have hzj : ∀ j : Fin d, v j.succ = 0 := by
      intro j
      have hj := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (v (Fin.succ j)))).1
        (by rw [← ht, ← hz]) j (Finset.mem_univ j)
      exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hj
    refine ⟨v 0, 0, axisVec hd, h0, le_refl 0, axisVec_sq hd, ?_⟩
    funext i
    refine Fin.cases ?_ (fun j => ?_) i
    · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_zero, sharpVec_zero]
      ring
    · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_succ, sharpVec_succ, hzj j,
        Pi.zero_apply]
      ring
  · set s := Real.sqrt t with hsdef
    have hs0 : 0 < s := Real.sqrt_pos.2 hpos
    have hss : s ^ 2 = t := Real.sq_sqrt ht0
    have hsv : s ≤ v 0 := by
      have h := Real.sqrt_le_sqrt hs
      rwa [Real.sqrt_sq h0] at h
    refine ⟨v 0 - s, 2 * s, fun j => v j.succ / s, by linarith, by linarith, ?_, ?_⟩
    · have h : ∑ j : Fin d, (v j.succ / s) ^ 2 = (∑ j : Fin d, v j.succ ^ 2) / s ^ 2 := by
        rw [Finset.sum_div]
        exact Finset.sum_congr rfl fun j _ => by rw [div_pow]
      rw [h, ← ht, hss, div_self (ne_of_gt hpos)]
    · funext i
      refine Fin.cases ?_ (fun j => ?_) i
      · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_zero, sharpVec_zero]
        ring
      · simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_succ, sharpVec_succ,
          Pi.zero_apply]
        field_simp

/-- A linear functional nonnegative on every sharp vector is nonnegative on the cone. -/
theorem nonneg_of_sharp (hd : 0 < d) (L : HVec d →ₗ[ℝ] ℝ)
    (h : ∀ b : Fin d → ℝ, ∑ j, b j ^ 2 = 1 → 0 ≤ L (sharpVec b)) {v : HVec d} (hv : Lor v) :
    0 ≤ L v := by
  obtain ⟨α, β, b, hα, hβ, hb, rfl⟩ := lor_decomp hd hv
  have hu : L (hom (0 : Fin d → ℝ)) =
      L (sharpVec (axisVec hd)) + L (sharpVec (-axisVec hd)) := by
    rw [hom_zero_eq_sharp (axisVec hd), map_add]
  have h1 := h _ (axisVec_sq hd)
  have h2 := h (-axisVec hd) (by rw [sum_neg_sq]; exact axisVec_sq hd)
  have h3 := h b hb
  rw [map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul, hu]
  have : 0 ≤ L (sharpVec (axisVec hd)) + L (sharpVec (-axisVec hd)) := add_nonneg h1 h2
  positivity

/-- The pairing as a linear functional of the right (target) effect. -/
def pvRight (a : HVec d) (ω : W d) : HVec d →ₗ[ℝ] ℝ where
  toFun b := pairVal a b ω
  map_add' b b' := pairVal_add_right a b b' ω
  map_smul' c b := pairVal_smul_right c a b ω

theorem pvRight_apply (a b : HVec d) (ω : W d) : pvRight a ω b = pairVal a b ω := rfl

theorem prodEffVal_sharp (x y : Fin d → ℝ) (ω : W d) :
    prodEffVal (sharpEff x) (sharpEff y) ω = pairVal (sharpVec x) (sharpVec y) ω := by
  rw [prodEffVal, sharpEff, sharpEff, ehom_affOf, ehom_affOf]

/-- **Q-CONE, one inclusion.** The full effect cone lies in the sharp-test cone. -/
theorem maxCone_subset_maxConeOf_sharp : maxCone (eball d) ⊆ maxConeOf (sharpFamily d) := by
  intro ω hω
  show ∀ e ∈ sharpFamily d, ∀ f ∈ sharpFamily d, 0 ≤ prodEffVal e f ω
  rintro e ⟨b, hb, rfl⟩ f ⟨c, hc, rfl⟩
  exact hω _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- **Q-CONE, the other inclusion.** For `0 < d`, a joint vector nonnegative on every product of
two sharp effects is nonnegative on every product of two effects. -/
theorem maxConeOf_sharp_subset_maxCone (hd : 0 < d) :
    maxConeOf (sharpFamily d) ⊆ maxCone (eball d) := by
  intro ω hω
  show ∀ e f, IsEffectOn (eball d) e → IsEffectOn (eball d) f → 0 ≤ prodEffVal e f ω
  intro e f he hf
  have key : ∀ x y : Fin d → ℝ, ∑ j, x j ^ 2 = 1 → ∑ j, y j ^ 2 = 1 →
      0 ≤ pairVal (sharpVec x) (sharpVec y) ω := by
    intro x y hx hy
    have h := hω (sharpEff x) ⟨x, hx, rfl⟩ (sharpEff y) ⟨y, hy, rfl⟩
    rwa [prodEffVal_sharp] at h
  have step : ∀ y : Fin d → ℝ, ∑ j, y j ^ 2 = 1 → 0 ≤ pairVal (ehom e) (sharpVec y) ω := by
    intro y hy
    have h := nonneg_of_sharp hd (pvLeft (sharpVec y) ω)
      (fun x hx => by rw [pvLeft_apply]; exact key x y hx hy) (lor_ehom he)
    rwa [pvLeft_apply] at h
  have h := nonneg_of_sharp hd (pvRight (ehom e) ω)
    (fun y hy => by rw [pvRight_apply]; exact step y hy) (lor_ehom hf)
  rw [pvRight_apply] at h
  rw [prodEffVal]
  exact h

/-- **Q-CONE.** For `0 < d` the sharp family determines DIM-1's maximal cone. -/
theorem maxConeOf_sharpFamily (hd : 0 < d) : maxConeOf (sharpFamily d) = maxCone (eball d) :=
  Set.Subset.antisymm (maxConeOf_sharp_subset_maxCone hd) maxCone_subset_maxConeOf_sharp

section ConeGeneration

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- **Q-CONE from OG-1's named hypotheses.** For `0 < d`, the four hypotheses make the sharp family
available, and the sharp family determines DIM-1's maximal cone. No mixing closure and no unit
premise is used. -/
theorem cone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) :
    sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d) :=
  ⟨sharpFamily_subset_avail hG hP1 hK hV4, maxConeOf_sharpFamily hd⟩

/-- Every member of the family is an effect on `Ω`. -/
def EffectsOn (Ω : Set (Fin d → ℝ)) (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ A, IsEffectOn Ω e

/-- The available family determines DIM-1's maximal cone once every available functional is an
effect. -/
theorem maxConeOf_avail_eq (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :
    maxConeOf avail = maxCone (eball d) := by
  refine Set.Subset.antisymm ?_ ?_
  · exact (maxConeOf_anti (sharpFamily_subset_avail hG hP1 hK hV4)).trans
      (maxConeOf_sharp_subset_maxCone hd)
  · rw [← maxConeOf_fullEffects]
    exact maxConeOf_anti fun e he => hE e he

end ConeGeneration

/-! ### §E — Q-SET: the full effect set -/

/-- The sub-convex span of the unit with one member of `S`. -/
def unitSpan (S : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ f ∈ S, ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ α + β ≤ 1 ∧ e = α • unitEff d + β • f}

/-- The mixing closure, a named premise: closure under sub-convex binary combinations. -/
def MixingClosed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A

theorem mix_apply (e f : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (α β : ℝ) (x : Fin d → ℝ) :
    (α • e + β • f) x = α * e x + β * f x := by
  simp only [AffineMap.coe_add, AffineMap.coe_smul, Pi.add_apply, Pi.smul_apply, smul_eq_mul]

/-- **The upper bound.** Every effect on `eball d` is `r ↦ a + v · r` with
`√(v · v) ≤ min a (1 − a)`. -/
theorem effect_eq_affine {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball d) e) :
    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧
      ∀ x, e x = a + ∑ j, v j * x j := by
  refine ⟨ehom e 0, fun j => ehom e j.succ, ?_, ehom_apply e⟩
  have hL := lor_ehom he
  obtain ⟨t, ht⟩ : ∃ t : ℝ, t = ∑ j : Fin d, ehom e j.succ ^ 2 := ⟨_, rfl⟩
  have ht0 : 0 ≤ t := ht ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  rw [← ht]
  have hlow : Real.sqrt t ≤ ehom e 0 := by
    have h := Real.sqrt_le_sqrt (ht ▸ hL.2)
    rwa [Real.sqrt_sq hL.1] at h
  refine le_min hlow ?_
  rcases eq_or_lt_of_le ht0 with hz | hpos
  · rw [← hz, Real.sqrt_zero]
    have h := (he 0 zero_mem_eball).2
    rw [ehom_apply] at h
    simp only [Pi.zero_apply, mul_zero, Finset.sum_const_zero, add_zero] at h
    linarith
  · set s := Real.sqrt t with hsdef
    have hs0 : 0 < s := Real.sqrt_pos.2 hpos
    have hss : s ^ 2 = t := Real.sq_sqrt ht0
    have hx : (fun j : Fin d => ehom e j.succ / s) ∈ eball d := by
      rw [mem_eball]
      have h : ∑ j : Fin d, (ehom e j.succ / s) ^ 2 = t / s ^ 2 := by
        rw [ht, Finset.sum_div]
        exact Finset.sum_congr rfl fun j _ => by rw [div_pow]
      rw [h, hss, div_self (ne_of_gt hpos)]
    have h := (he _ hx).2
    rw [ehom_apply] at h
    have hsum : ∑ j : Fin d, ehom e j.succ * (ehom e j.succ / s) = s := by
      have h2 : ∑ j : Fin d, ehom e j.succ * (ehom e j.succ / s) = t / s := by
        rw [ht, Finset.sum_div]
        exact Finset.sum_congr rfl fun j _ => by ring
      rw [h2, ← hss]
      field_simp
    rw [hsum] at h
    linarith

/-- **The upper bound, converse.** Every functional `r ↦ a + v · r` with
`√(v · v) ≤ min a (1 − a)` is an effect on `eball d`. -/
theorem isEffectOn_of_affine {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {a : ℝ} {v : Fin d → ℝ}
    (hv : Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a)) (he : ∀ x, e x = a + ∑ j, v j * x j) :
    IsEffectOn (eball d) e := by
  intro x hx
  have ht0 : 0 ≤ ∑ j, v j ^ 2 := Finset.sum_nonneg fun j _ => sq_nonneg _
  have hlor : Lor (Matrix.vecCons (Real.sqrt (∑ j, v j ^ 2)) v) := by
    refine ⟨Real.sqrt_nonneg _, ?_⟩
    simp only [Matrix.cons_val_succ, Matrix.cons_val_zero]
    rw [Real.sq_sqrt ht0]
  have hb := lor_pair_bound hlor hx
  simp only [Matrix.cons_val_succ, Matrix.cons_val_zero] at hb
  have h1 := le_trans hv (min_le_left _ _)
  have h2 := le_trans hv (min_le_right _ _)
  rw [he x]
  constructor <;> linarith [hb.1, hb.2]

/-- **The decomposition.** For `0 < d`, every effect on `eball d` is a sub-convex combination of
the unit with one sharp directional effect. -/
theorem fullEffects_subset_unitSpan (hd : 0 < d) :
    fullEffects (eball d) ⊆ unitSpan (sharpFamily d) := by
  intro e he
  have hL : Lor (ehom e) := lor_ehom he
  obtain ⟨a, v, hv, hev⟩ := effect_eq_affine he
  obtain ⟨t, ht⟩ : ∃ t : ℝ, t = ∑ j, v j ^ 2 := ⟨_, rfl⟩
  have ht0 : 0 ≤ t := ht ▸ Finset.sum_nonneg fun j _ => sq_nonneg _
  rw [← ht] at hv
  have h1 := le_trans hv (min_le_left _ _)
  have h2 := le_trans hv (min_le_right _ _)
  have hs0 := Real.sqrt_nonneg t
  rcases eq_or_lt_of_le ht0 with hz | hpos
  · have hvj : ∀ j, v j = 0 := by
      intro j
      have hj := (Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (v j))).1
        (by rw [← ht, ← hz]) j (Finset.mem_univ j)
      exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hj
    refine ⟨sharpEff (axisVec hd), ⟨axisVec hd, axisVec_sq hd, rfl⟩, a, 0, by linarith, le_refl 0,
      by linarith, ?_⟩
    refine AffineMap.ext fun x => ?_
    rw [mix_apply, hev x, unitEff_apply]
    simp only [hvj, zero_mul, Finset.sum_const_zero, add_zero]
    ring
  · set s := Real.sqrt t with hsdef
    have hsp : 0 < s := Real.sqrt_pos.2 hpos
    have hss : s ^ 2 = t := Real.sq_sqrt ht0
    refine ⟨sharpEff (fun j => v j / s), ⟨fun j => v j / s, ?_, rfl⟩, a - s, 2 * s, by linarith,
      by linarith, by linarith, ?_⟩
    · have h : ∑ j, (v j / s) ^ 2 = t / s ^ 2 := by
        rw [ht, Finset.sum_div]
        exact Finset.sum_congr rfl fun j _ => by rw [div_pow]
      rw [h, hss, div_self (ne_of_gt hpos)]
    · refine AffineMap.ext fun x => ?_
      rw [mix_apply, hev x, unitEff_apply, sharpEff_apply, mul_add, Finset.mul_sum]
      have h : ∑ j, 2 * s * (v j / s / 2 * x j) = ∑ j, v j * x j :=
        Finset.sum_congr rfl fun j _ => by field_simp
      rw [h]
      ring

/-- **The decomposition, converse.** Every sub-convex combination of the unit with one sharp
directional effect is an effect on `eball d`. -/
theorem unitSpan_subset_fullEffects : unitSpan (sharpFamily d) ⊆ fullEffects (eball d) := by
  rintro e ⟨f, ⟨b, hb, rfl⟩, α, β, hα, hβ, hαβ, rfl⟩ x hx
  have hf := sharpEff_isEffectOn hb x hx
  rw [mix_apply, unitEff_apply]
  constructor <;> nlinarith [hf.1, hf.2]

/-- For `0 < d` the full effect set of `eball d` is the sub-convex span of the unit with the sharp
family. -/
theorem fullEffects_eq_unitSpan (hd : 0 < d) :
    fullEffects (eball d) = unitSpan (sharpFamily d) :=
  Set.Subset.antisymm (fullEffects_subset_unitSpan hd) unitSpan_subset_fullEffects

section SetGeneration

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- **Q-SET, conditional on the mixing closure.** For `0 < d`, OG-1's four named hypotheses with the
unit available and the named mixing closure make every effect on `eball d` available. -/
theorem fullEffects_subset_avail (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail) :
    fullEffects (eball d) ⊆ avail := by
  intro e he
  obtain ⟨f, hf, α, β, hα, hβ, hαβ, rfl⟩ := fullEffects_subset_unitSpan hd he
  exact hM _ hU f (sharpFamily_subset_avail hG hP1 hK hV4 hf) α β hα hβ hαβ

/-- With every available functional an effect, the available family is the full effect set. -/
theorem avail_eq_fullEffects (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail)
    (hE : EffectsOn (eball d) avail) : avail = fullEffects (eball d) :=
  Set.Subset.antisymm (fun e he => hE e he) (fullEffects_subset_avail hd hG hP1 hK hV4 hU hM)

end SetGeneration

/-- The sharp family with the unit. -/
def sharpUnitFamily (d : ℕ) : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ) := insert (unitEff d) (sharpFamily d)

/-- The constant effect one half. -/
noncomputable def halfEff (d : ℕ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := (1 / 2 : ℝ) • unitEff d

theorem halfEff_apply (x : Fin d → ℝ) : halfEff d x = 1 / 2 := by
  rw [halfEff, AffineMap.coe_smul, Pi.smul_apply, unitEff_apply, smul_eq_mul, mul_one]

theorem halfEff_mem_fullEffects : halfEff d ∈ fullEffects (eball d) := by
  intro x _
  rw [halfEff_apply]
  norm_num

theorem halfEff_not_mem_sharpUnitFamily : halfEff d ∉ sharpUnitFamily d := by
  rintro (h | ⟨b, hb, h⟩)
  · have := congrArg (fun e : (Fin d → ℝ) →ᵃ[ℝ] ℝ => e 0) h
    simp only [halfEff_apply, unitEff_apply] at this
    norm_num at this
  · have := congrArg (fun e : (Fin d → ℝ) →ᵃ[ℝ] ℝ => e b) h
    simp only [halfEff_apply, sharpEff_self hb] at this
    norm_num at this

/-- **Q-SET without the mixing closure.** For every `0 < d`, the sharp family with the unit
satisfies OG-1's four named hypotheses under the full automorphism family, contains the unit and
consists of effects, and it is neither mixing closed nor the full effect set: the four hypotheses
with the unit do not imply that every effect is available. -/
theorem not_fullEffects_of_orbit (hd : 0 < d) :
    PreservesBody (eball d) (fullAut d) ∧ SharpSeed (eball d) (sharpEff (axisVec hd)) ∧
      BoundaryTransitive (eball d) (fullAut d) ∧
      SeedOrbitAvailable (fullAut d) (sharpEff (axisVec hd)) (sharpUnitFamily d) ∧
      unitEff d ∈ sharpUnitFamily d ∧ EffectsOn (eball d) (sharpUnitFamily d) ∧
      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d := by
  have hP1 := sharpEff_sharpSeed (axisVec_sq hd)
  refine ⟨preservesBody_fullAut, hP1, boundaryTransitive_fullAut, ?_, Set.mem_insert _ _, ?_, ?_,
    ?_⟩
  · intro g hg
    exact Set.mem_insert_of_mem _ (seedTransport_mem_sharpFamily preservesBody_fullAut hP1 hg)
  · rintro e (rfl | ⟨b, hb, rfl⟩)
    · exact isEffectOn_unitEff _
    · exact sharpEff_isEffectOn hb
  · intro hM
    apply halfEff_not_mem_sharpUnitFamily (d := d)
    have h := hM _ (Set.mem_insert _ _) _ (Set.mem_insert _ _) (1 / 2) 0 (by norm_num) le_rfl
      (by norm_num)
    rwa [zero_smul, add_zero] at h
  · intro h
    exact halfEff_not_mem_sharpUnitFamily (h halfEff_mem_fullEffects)

/-! ### §F — controls -/

/-- At `d = 0` the sharp family is empty and its cone is not DIM-1's maximal cone. -/
theorem maxConeOf_sharpFamily_zero_ne : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) := by
  intro h
  have hempty : sharpFamily 0 = ∅ := by
    ext e
    simp only [sharpFamily, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_exists,
      not_and]
    intro b hb
    simp at hb
  have hω : (fun _ _ => -1 : W 0) ∈ maxConeOf (sharpFamily 0) := by
    rw [hempty]
    show ∀ e ∈ (∅ : Set ((Fin 0 → ℝ) →ᵃ[ℝ] ℝ)), ∀ f ∈ (∅ : Set ((Fin 0 → ℝ) →ᵃ[ℝ] ℝ)),
      0 ≤ prodEffVal e f (fun _ _ => -1 : W 0)
    intro e he
    exact absurd he (Set.notMem_empty e)
  rw [h] at hω
  have hneg := hω (unitEff 0) (unitEff 0) (isEffectOn_unitEff _) (isEffectOn_unitEff _)
  have hval : prodEffVal (unitEff 0) (unitEff 0) (fun _ _ => -1 : W 0) = -1 := by
    rw [prodEffVal, pairVal, Fin.sum_univ_succ, Fin.sum_univ_succ]
    simp only [Fin.sum_univ_zero, add_zero, ehom_zero_eq, unitEff_apply]
    norm_num
  rw [hval] at hneg
  norm_num at hneg

/-- The effects of one axis of `eball 3` with the unit. -/
def axisFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=
  {unitEff 3, sharpEff ![0, 0, 1], sharpEff ![0, 0, -1]}

/-- A joint vector outside DIM-1's cone. -/
noncomputable def outVec : W 3 := tens ![1, 2, 0, 0] ![1, 2, 0, 0]

theorem ehom_unitEff (d : ℕ) : ehom (unitEff d) = hom (0 : Fin d → ℝ) := by
  have h : unitEff d = affOf (hom (0 : Fin d → ℝ)) := by
    refine AffineMap.ext fun x => ?_
    rw [unitEff_apply, affOf_apply, hom_zero]
    simp
  rw [h, ehom_affOf]

/-- **Directional coverage is load-bearing for the cone.** At `d = 3` the effects of one axis with
the unit determine a strictly larger cone than DIM-1's maximal cone. -/
theorem maxConeOf_axis_ne : maxConeOf axisFamily ≠ maxCone (eball 3) := by
  have hin : outVec ∈ maxConeOf axisFamily := by
    have hval : ∀ e ∈ axisFamily, ∑ μ, ehom e μ * (![1, 2, 0, 0] : HVec 3) μ = 1 ∨
        ∑ μ, ehom e μ * (![1, 2, 0, 0] : HVec 3) μ = 1 / 2 := by
      rintro e (rfl | rfl | rfl)
      · left
        rw [ehom_unitEff]
        norm_num [Fin.sum_univ_succ, hom]
      · right
        rw [sharpEff, ehom_affOf]
        norm_num [Fin.sum_univ_succ, sharpVec]
      · right
        rw [sharpEff, ehom_affOf]
        norm_num [Fin.sum_univ_succ, sharpVec]
    show ∀ e ∈ axisFamily, ∀ f ∈ axisFamily, 0 ≤ prodEffVal e f outVec
    intro e he f hf
    rw [prodEffVal, outVec, pairVal_tens]
    have hf' : ∑ ν, (![1, 2, 0, 0] : HVec 3) ν * ehom f ν =
        ∑ ν, ehom f ν * (![1, 2, 0, 0] : HVec 3) ν :=
      Finset.sum_congr rfl fun ν _ => mul_comm _ _
    rw [hf']
    rcases hval e he with h1 | h1 <;> rcases hval f hf with h2 | h2 <;> rw [h1, h2] <;> norm_num
  intro h
  rw [h] at hin
  have hneg := hin (sharpEff ![-1, 0, 0]) (sharpEff ![1, 0, 0])
    (sharpEff_isEffectOn (by simp [Fin.sum_univ_succ]))
    (sharpEff_isEffectOn (by simp [Fin.sum_univ_succ]))
  rw [prodEffVal_sharp, outVec, pairVal_tens] at hneg
  norm_num [Fin.sum_univ_succ, sharpVec] at hneg

/-- A countable family is never boundary transitive on `eball 3`: its boundary states are the unit
sphere, which is uncountable. -/
theorem not_boundaryTransitive_of_countable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    (hG : G.Countable) : ¬ BoundaryTransitive (eball 3) G := by
  intro hK
  have hz : ∑ j, (![0, 0, 1] : Fin 3 → ℝ) j ^ 2 = 1 := by simp [Fin.sum_univ_succ]
  have hsph : {b : Fin 3 → ℝ | ∑ j, b j ^ 2 = 1}.Countable := by
    refine Set.Countable.mono ?_ (hG.image fun g => g ![0, 0, 1])
    intro b hb
    obtain ⟨g, hg, hgb⟩ := hK ![0, 0, 1] b (isBoundaryState_eball_of_sphere hz)
      (isBoundaryState_eball_of_sphere hb)
    exact ⟨g, hg, hgb⟩
  have hmaps : Set.MapsTo (fun t : ℝ => (![t, Real.sqrt (1 - t ^ 2), 0] : Fin 3 → ℝ))
      (Set.Icc (-1 : ℝ) 1) {b : Fin 3 → ℝ | ∑ j, b j ^ 2 = 1} := by
    intro t ht
    obtain ⟨h1, h2⟩ := ht
    have hnn : 0 ≤ 1 - t ^ 2 := by nlinarith
    show ∑ j, (![t, Real.sqrt (1 - t ^ 2), 0] : Fin 3 → ℝ) j ^ 2 = 1
    rw [Fin.sum_univ_three]
    show t ^ 2 + Real.sqrt (1 - t ^ 2) ^ 2 + (0 : ℝ) ^ 2 = 1
    rw [Real.sq_sqrt hnn]
    ring
  have hinj : Set.InjOn (fun t : ℝ => (![t, Real.sqrt (1 - t ^ 2), 0] : Fin 3 → ℝ))
      (Set.Icc (-1 : ℝ) 1) := by
    intro s _ t _ hst
    exact congrFun hst 0
  have hc : (Set.Icc (-1 : ℝ) 1).Countable := hmaps.countable_of_injOn hinj hsph
  have h : Cardinal.mk (Set.Icc (-1 : ℝ) 1) ≤ Cardinal.aleph0 :=
    Cardinal.le_aleph0_iff_set_countable.mpr hc
  have hI : Cardinal.mk (Set.Icc (-1 : ℝ) 1) = Cardinal.continuum :=
    Cardinal.mk_Icc_real (by norm_num)
  rw [hI] at h
  exact absurd h (not_le.mpr Cardinal.aleph0_lt_continuum)

/-! ### The verdict -/

/-- The two questions with their controls, together. Q-CONE: for every `0 < d`, the sharp family
determines DIM-1's maximal cone, and OG-1's four named hypotheses make it available. Q-SET: the
upper bound in both directions; the decomposition in both directions; the full set from the four
hypotheses with the unit and the mixing closure; and the four hypotheses with the unit without the
full set. Controls: `d = 0`, one axis at `d = 3`, a countable family. -/
theorem eff1_core :
    (∀ d : ℕ, 0 < d → maxConeOf (sharpFamily d) = maxCone (eball d)) ∧
    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), 0 < d → PreservesBody (eball d) G →
        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →
        sharpFamily d ⊆ avail ∧ maxConeOf (sharpFamily d) = maxCone (eball d)) ∧
    (∀ (d : ℕ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ), IsEffectOn (eball d) e →
        ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧
          ∀ x, e x = a + ∑ j, v j * x j) ∧
    (∀ d : ℕ, 0 < d → fullEffects (eball d) = unitSpan (sharpFamily d)) ∧
    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), 0 < d → PreservesBody (eball d) G →
        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →
        unitEff d ∈ avail → MixingClosed avail → fullEffects (eball d) ⊆ avail) ∧
    (∀ d : ℕ, 0 < d → ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧
        SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧
        unitEff d ∈ avail ∧ EffectsOn (eball d) avail ∧ ¬ MixingClosed avail ∧
        ¬ fullEffects (eball d) ⊆ avail) ∧
    maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) ∧
    maxConeOf axisFamily ≠ maxCone (eball 3) ∧
    (∀ G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)), G.Countable → ¬ BoundaryTransitive (eball 3) G) :=
  ⟨fun _ hd => maxConeOf_sharpFamily hd,
    fun _ _ _ _ hd hG hP1 hK hV4 => cone_of_orbit hd hG hP1 hK hV4,
    fun _ _ he => effect_eq_affine he,
    fun _ hd => fullEffects_eq_unitSpan hd,
    fun _ _ _ _ hd hG hP1 hK hV4 hU hM => fullEffects_subset_avail hd hG hP1 hK hV4 hU hM,
    fun _ hd => ⟨fullAut _, sharpEff (axisVec hd), sharpUnitFamily _, not_fullEffects_of_orbit hd⟩,
    maxConeOf_sharpFamily_zero_ne,
    maxConeOf_axis_ne,
    fun _ hG => not_boundaryTransitive_of_countable hG⟩

end EffectSpace
end OIBridge

#print axioms OIBridge.EffectSpace.sharpEff_isEffectOn
#print axioms OIBridge.EffectSpace.sharpEff_sharpSeed
#print axioms OIBridge.EffectSpace.isBoundaryState_eball_of_sphere
#print axioms OIBridge.EffectSpace.sphere_of_isBoundaryState_eball
#print axioms OIBridge.EffectSpace.sharp_eq_of_certain
#print axioms OIBridge.EffectSpace.reflLin_swap
#print axioms OIBridge.EffectSpace.boundaryTransitive_fullAut
#print axioms OIBridge.EffectSpace.seedTransport_mem_sharpFamily
#print axioms OIBridge.EffectSpace.sharpFamily_subset_avail
#print axioms OIBridge.EffectSpace.seedOrbit_eq_sharpFamily
#print axioms OIBridge.EffectSpace.maxConeOf_fullEffects
#print axioms OIBridge.EffectSpace.lor_decomp
#print axioms OIBridge.EffectSpace.nonneg_of_sharp
#print axioms OIBridge.EffectSpace.maxCone_subset_maxConeOf_sharp
#print axioms OIBridge.EffectSpace.maxConeOf_sharp_subset_maxCone
#print axioms OIBridge.EffectSpace.maxConeOf_sharpFamily
#print axioms OIBridge.EffectSpace.cone_of_orbit
#print axioms OIBridge.EffectSpace.maxConeOf_avail_eq
#print axioms OIBridge.EffectSpace.effect_eq_affine
#print axioms OIBridge.EffectSpace.isEffectOn_of_affine
#print axioms OIBridge.EffectSpace.fullEffects_subset_unitSpan
#print axioms OIBridge.EffectSpace.unitSpan_subset_fullEffects
#print axioms OIBridge.EffectSpace.fullEffects_eq_unitSpan
#print axioms OIBridge.EffectSpace.fullEffects_subset_avail
#print axioms OIBridge.EffectSpace.avail_eq_fullEffects
#print axioms OIBridge.EffectSpace.not_fullEffects_of_orbit
#print axioms OIBridge.EffectSpace.maxConeOf_sharpFamily_zero_ne
#print axioms OIBridge.EffectSpace.maxConeOf_axis_ne
#print axioms OIBridge.EffectSpace.not_boundaryTransitive_of_countable
#print axioms OIBridge.EffectSpace.eff1_core
