/-
  OIBridge/EffectSpace.lean — round EFF-1: effect completion on the ball, in the field-neutral
  vocabulary of `KInfFoundations` and `OrbitGeneration`.

  Two logically separate targets, each its own theorem with its own hypotheses.

  (A) Generation. With an explicitly named sub-convex mixing closure on a family of affine
      functionals (`MixingClosed`), the directional family `directionalFamily` of OG-1 together
      with the unit effect generates the sub-convex span `unitSpan directionalFamily`
      (`generation_of_mixingClosed`). Chained through OG-1's `seedOrbit_ball3_eq`, the same span
      is available from a sharp seed under a body-preserving boundary-transitive family whose seed
      orbit is available, once the unit is available and the available family is mixing closed
      (`unitSpan_subset_avail`); with target (B) this is `fullEffects_subset_avail`, and with the
      premise that every available functional is an effect it is `avail_eq_fullEffects`. The
      mixing closure is a named premise of the generation theorem and is derived nowhere here.

  (B) Upper bound. Independently of (A), with no premise beyond `IsEffectOn ball3`, every effect
      on `ball3` is affine of the form `e r = a + v · r` with `0 ≤ a ≤ 1` and
      `√(v · v) ≤ min a (1 − a)` (`effect_eq_affine`), and lies in `unitSpan directionalFamily`
      (`fullEffects_subset_unitSpan`); conversely every member of that span is an effect on the
      ball (`unitSpan_subset_fullEffects`). The equality `fullEffects_eq_unitSpan` cites both
      directions.

  Also here: the unbiased family `unbiasedFamily = {(1 + b · r)/2 : b · b ≤ 1}`, which is the
  convex hull of the directional family (two inclusions), the slice of effects with the value
  `1/2` at the centre (two theorems), and a proper subset of the effect space (it misses the unit
  and OG-1's `unsharpSeed`). Controls: the full effect family satisfies every premise of (A); the
  sub-convex span of the directional family satisfies them and is not the conclusion restated; the
  family `{unit, 0} ∪ directionalFamily` fails `MixingClosed`; the effects reading the third
  coordinate alone (the classical bit on an axis of the ball) satisfy the unit, mixing, effect,
  sharp-seed and transitivity premises and fail seed-orbit availability; the identity alone
  satisfies seed-orbit availability for the span of one directional effect and is not boundary
  transitive; the universal family fails the effect premise; a countable family is never boundary
  transitive on `ball3`.

  The mixing closure is a named premise of the generation theorem; the upper bound is proved
  independently of it; no limit closure, no drive, no one-parameter motion, no complex structure
  and no matrix representation is used or claimed. Nothing here sources the seed, the orbit, the
  availability, the unit or the mixing closure from any construction.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.TransitiveBody
import Mathlib.Analysis.Real.Cardinality

namespace OIBridge
namespace EffectSpace

open Set KInfFoundations OrbitGeneration

/-! ### §A — vocabulary -/

section Vocabulary

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- The unit effect. -/
noncomputable def unitEffect : V →ᵃ[ℝ] ℝ := AffineMap.const ℝ V (1 : ℝ)

theorem unitEffect_apply (x : V) : unitEffect x = 1 := rfl

/-- A combination of two affine functionals, evaluated. -/
theorem mix_apply (e f : V →ᵃ[ℝ] ℝ) (α β : ℝ) (x : V) :
    (α • e + β • f) x = α * e x + β * f x := by
  simp only [AffineMap.coe_add, AffineMap.coe_smul, Pi.add_apply, Pi.smul_apply, smul_eq_mul]

/-- The sub-convex span of the unit with one member of `S`: `α • 1 + β • f`, `f ∈ S`,
`α, β ≥ 0`, `α + β ≤ 1`. -/
def unitSpan (S : Set (V →ᵃ[ℝ] ℝ)) : Set (V →ᵃ[ℝ] ℝ) :=
  {e | ∃ f ∈ S, ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ α + β ≤ 1 ∧ e = α • unitEffect + β • f}

/-- The mixing closure, a named premise: the family is closed under sub-convex binary
combinations `α • e + β • f`, `α, β ≥ 0`, `α + β ≤ 1`. -/
def MixingClosed (A : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A

/-- Convex closure: the family is closed under convex binary combinations. -/
def ConvexClosed (A : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ A, ∀ f ∈ A, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β = 1 → α • e + β • f ∈ A

/-- Every member of the family is an effect on `Ω`. -/
def EffectsOn (Ω : Set V) (A : Set (V →ᵃ[ℝ] ℝ)) : Prop := ∀ e ∈ A, IsEffectOn Ω e

theorem effectsOn_iff_subset {Ω : Set V} {A : Set (V →ᵃ[ℝ] ℝ)} :
    EffectsOn Ω A ↔ A ⊆ fullEffects Ω := Iff.rfl

theorem unitEffect_mem_fullEffects (Ω : Set V) : unitEffect ∈ fullEffects Ω := by
  intro x _
  rw [unitEffect_apply]
  norm_num

/-- The full effect family of any body is mixing closed. -/
theorem mixingClosed_fullEffects (Ω : Set V) : MixingClosed (fullEffects Ω) := by
  intro e he f hf α β hα hβ hαβ x hx
  have h1 : IsEffectOn Ω e := he
  have h2 : IsEffectOn Ω f := hf
  have h1x := h1 x hx
  have h2x := h2 x hx
  rw [mix_apply]
  constructor <;> nlinarith [h1x.1, h1x.2, h2x.1, h2x.2]

/-- Target (A), abstract form: a family containing `S` and the unit and closed under mixing
contains the sub-convex span of the unit with `S`. -/
theorem unitSpan_subset_of_mixingClosed {S A : Set (V →ᵃ[ℝ] ℝ)} (hS : S ⊆ A)
    (hU : unitEffect ∈ A) (hM : MixingClosed A) : unitSpan S ⊆ A := by
  rintro e ⟨f, hf, α, β, hα, hβ, hαβ, rfl⟩
  exact hM unitEffect hU f (hS hf) α β hα hβ hαβ

theorem seedTransport_refl (r : V →ᵃ[ℝ] ℝ) : seedTransport r (AffineEquiv.refl ℝ V) = r := by
  ext x
  rw [seedTransport_apply, AffineEquiv.symm_refl, AffineEquiv.refl_apply]

end Vocabulary

/-! ### §B — the geometry of the ball's effects (target (B), premise-free) -/

section Ball

theorem ex_sphere :
    (![1, 0, 0] : Fin 3 → ℝ) 0 ^ 2 + (![1, 0, 0] : Fin 3 → ℝ) 1 ^ 2 +
      (![1, 0, 0] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
  show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 = 1
  norm_num

theorem nez_sphere :
    (![0, 0, -1] : Fin 3 → ℝ) 0 ^ 2 + (![0, 0, -1] : Fin 3 → ℝ) 1 ^ 2 +
      (![0, 0, -1] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
  show (0 : ℝ) ^ 2 + 0 ^ 2 + (-1) ^ 2 = 1
  norm_num

/-- The coefficient bounds in coordinates: an affine functional `c + a · v` with values in
`[0, 1]` on the ball has `0 ≤ c ≤ 1`, `a · a ≤ c²` and `a · a ≤ (1 − c)²`. -/
theorem coeff_bounds {c a0 a1 a2 : ℝ}
    (h : ∀ v : Fin 3 → ℝ, v ∈ ball3 →
      0 ≤ c + v 0 * a0 + v 1 * a1 + v 2 * a2 ∧ c + v 0 * a0 + v 1 * a1 + v 2 * a2 ≤ 1) :
    0 ≤ c ∧ c ≤ 1 ∧ a0 ^ 2 + a1 ^ 2 + a2 ^ 2 ≤ c ^ 2 ∧
      a0 ^ 2 + a1 ^ 2 + a2 ^ 2 ≤ (1 - c) ^ 2 := by
  have h0 : (0 : Fin 3 → ℝ) ∈ ball3 := by
    rw [mem_ball3]
    norm_num
  have hc := h 0 h0
  simp only [Pi.zero_apply, zero_mul, add_zero] at hc
  obtain ⟨hc0, hc1⟩ := hc
  obtain ⟨A, hA⟩ : ∃ A : ℝ, A = a0 ^ 2 + a1 ^ 2 + a2 ^ 2 := ⟨_, rfl⟩
  have hA0 : 0 ≤ A := by rw [hA]; positivity
  rcases eq_or_lt_of_le hA0 with hz | hpos
  · rw [← hA, ← hz]
    exact ⟨hc0, hc1, sq_nonneg c, sq_nonneg (1 - c)⟩
  · set s := Real.sqrt A with hs
    have hs0 : 0 < s := Real.sqrt_pos.2 hpos
    have hs2 : s ^ 2 = A := Real.sq_sqrt hA0
    obtain ⟨k, hk⟩ : ∃ k : ℝ, s * k = 1 := ⟨_, mul_inv_cancel₀ hs0.ne'⟩
    have hk2 : s ^ 2 * k ^ 2 = 1 := by rw [← mul_pow, hk, one_pow]
    have hp : (![a0 * k, a1 * k, a2 * k] : Fin 3 → ℝ) ∈ ball3 := by
      show (a0 * k) ^ 2 + (a1 * k) ^ 2 + (a2 * k) ^ 2 ≤ 1
      have e1 : (a0 * k) ^ 2 + (a1 * k) ^ 2 + (a2 * k) ^ 2 = s ^ 2 * k ^ 2 := by
        rw [hs2, hA]; ring
      rw [e1, hk2]
    have hn : (![-(a0 * k), -(a1 * k), -(a2 * k)] : Fin 3 → ℝ) ∈ ball3 := by
      show (-(a0 * k)) ^ 2 + (-(a1 * k)) ^ 2 + (-(a2 * k)) ^ 2 ≤ 1
      have e1 : (-(a0 * k)) ^ 2 + (-(a1 * k)) ^ 2 + (-(a2 * k)) ^ 2 = s ^ 2 * k ^ 2 := by
        rw [hs2, hA]; ring
      rw [e1, hk2]
    have hdot : a0 * k * a0 + a1 * k * a1 + a2 * k * a2 = s := by
      have e2 : a0 * k * a0 + a1 * k * a1 + a2 * k * a2 = s ^ 2 * k := by rw [hs2, hA]; ring
      rw [e2]
      linear_combination s * hk
    have F1 : c + a0 * k * a0 + a1 * k * a1 + a2 * k * a2 ≤ 1 := (h _ hp).2
    have F2 : 0 ≤ c + -(a0 * k) * a0 + -(a1 * k) * a1 + -(a2 * k) * a2 := (h _ hn).1
    have hcs1 : c + s ≤ 1 := by linarith
    have hcs0 : s ≤ c := by linarith
    refine ⟨hc0, hc1, ?_, ?_⟩
    · rw [← hA, ← hs2]
      nlinarith [mul_nonneg (sub_nonneg.2 hcs0) (add_nonneg hs0.le hc0)]
    · rw [← hA, ← hs2]
      nlinarith [mul_nonneg (sub_nonneg.2 (by linarith : s ≤ 1 - c))
        (add_nonneg hs0.le (by linarith : (0 : ℝ) ≤ 1 - c))]

/-- An effect on the ball, in coordinates, with its coefficient bounds. -/
theorem effect_decomp {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 e) :
    ∃ c a0 a1 a2 : ℝ, 0 ≤ c ∧ c ≤ 1 ∧ a0 ^ 2 + a1 ^ 2 + a2 ^ 2 ≤ c ^ 2 ∧
      a0 ^ 2 + a1 ^ 2 + a2 ^ 2 ≤ (1 - c) ^ 2 ∧
      ∀ v : Fin 3 → ℝ, e v = c + v 0 * a0 + v 1 * a1 + v 2 * a2 := by
  obtain ⟨c, a0, a1, a2, hr⟩ : ∃ c a0 a1 a2 : ℝ, ∀ v : Fin 3 → ℝ,
      e v = c + v 0 * a0 + v 1 * a1 + v 2 * a2 := ⟨_, _, _, _, affine3_apply e⟩
  have h : ∀ v : Fin 3 → ℝ, v ∈ ball3 →
      0 ≤ c + v 0 * a0 + v 1 * a1 + v 2 * a2 ∧ c + v 0 * a0 + v 1 * a1 + v 2 * a2 ≤ 1 := by
    intro v hv
    rw [← hr v]
    exact he v hv
  obtain ⟨h0, h1, h2, h3⟩ := coeff_bounds h
  exact ⟨c, a0, a1, a2, h0, h1, h2, h3, hr⟩

/-- **Target (B), the upper bound.** Every effect on the ball is `r ↦ a + v · r` with
`0 ≤ a ≤ 1` and `√(v · v) ≤ min a (1 − a)`. -/
theorem effect_eq_affine {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 e) :
    ∃ (a : ℝ) (v : Fin 3 → ℝ), 0 ≤ a ∧ a ≤ 1 ∧
      Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧ ∀ r : Fin 3 → ℝ, e r = a + ∑ j, v j * r j := by
  obtain ⟨c, a0, a1, a2, h0, h1, h2, h3, hr⟩ := effect_decomp he
  refine ⟨c, ![a0, a1, a2], h0, h1, ?_, fun r => ?_⟩
  · rw [Fin.sum_univ_three]
    show Real.sqrt (a0 ^ 2 + a1 ^ 2 + a2 ^ 2) ≤ min c (1 - c)
    refine le_min ?_ ?_
    · calc Real.sqrt (a0 ^ 2 + a1 ^ 2 + a2 ^ 2) ≤ Real.sqrt (c ^ 2) := Real.sqrt_le_sqrt h2
        _ = c := Real.sqrt_sq h0
    · calc Real.sqrt (a0 ^ 2 + a1 ^ 2 + a2 ^ 2) ≤ Real.sqrt ((1 - c) ^ 2) :=
            Real.sqrt_le_sqrt h3
        _ = 1 - c := Real.sqrt_sq (by linarith)
  · rw [Fin.sum_univ_three, hr r]
    show c + r 0 * a0 + r 1 * a1 + r 2 * a2 = c + (a0 * r 0 + a1 * r 1 + a2 * r 2)
    ring

/-- **Target (B), span form.** Every effect on the ball is a sub-convex combination of the unit
with one directional effect. -/
theorem fullEffects_subset_unitSpan : fullEffects ball3 ⊆ unitSpan directionalFamily := by
  intro e he
  have he' : IsEffectOn ball3 e := he
  obtain ⟨c, a0, a1, a2, h0, h1, h2, h3, hr⟩ := effect_decomp he'
  obtain ⟨A, hA⟩ : ∃ A : ℝ, A = a0 ^ 2 + a1 ^ 2 + a2 ^ 2 := ⟨_, rfl⟩
  have hA0 : 0 ≤ A := by rw [hA]; positivity
  rcases eq_or_lt_of_le hA0 with hz | hpos
  · have q0 := sq_nonneg a0
    have q1 := sq_nonneg a1
    have q2 := sq_nonneg a2
    have z0 : a0 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    have z1 : a1 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    have z2 : a2 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    refine ⟨ballEffect ![0, 0, 1], ⟨_, ez_sphere, rfl⟩, c, 0, h0, le_rfl, by linarith, ?_⟩
    apply AffineMap.ext
    intro v
    rw [mix_apply, unitEffect_apply, hr v, z0, z1, z2]
    ring
  · set s := Real.sqrt A with hs
    have hs0 : 0 < s := Real.sqrt_pos.2 hpos
    have hs2 : s ^ 2 = A := Real.sq_sqrt hA0
    obtain ⟨k, hk⟩ : ∃ k : ℝ, s * k = 1 := ⟨_, mul_inv_cancel₀ hs0.ne'⟩
    have hk2 : s ^ 2 * k ^ 2 = 1 := by rw [← mul_pow, hk, one_pow]
    have hb : (![a0 * k, a1 * k, a2 * k] : Fin 3 → ℝ) 0 ^ 2 +
        (![a0 * k, a1 * k, a2 * k] : Fin 3 → ℝ) 1 ^ 2 +
        (![a0 * k, a1 * k, a2 * k] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
      show (a0 * k) ^ 2 + (a1 * k) ^ 2 + (a2 * k) ^ 2 = 1
      have e1 : (a0 * k) ^ 2 + (a1 * k) ^ 2 + (a2 * k) ^ 2 = s ^ 2 * k ^ 2 := by
        rw [hs2, hA]; ring
      rw [e1, hk2]
    have hsc : s ≤ c := by nlinarith
    have hsc' : s ≤ 1 - c := by nlinarith
    refine ⟨ballEffect ![a0 * k, a1 * k, a2 * k], ⟨_, hb, rfl⟩, c - s, 2 * s, by linarith,
      by linarith, by linarith, ?_⟩
    apply AffineMap.ext
    intro v
    rw [mix_apply, unitEffect_apply, ballEffect_apply, hr v]
    show c + v 0 * a0 + v 1 * a1 + v 2 * a2 =
      (c - s) * 1 + 2 * s * (1 / 2 + (a0 * k * v 0 + a1 * k * v 1 + a2 * k * v 2) / 2)
    linear_combination (-(a0 * v 0 + a1 * v 1 + a2 * v 2)) * hk

/-- The converse: every sub-convex combination of the unit with a directional effect is an
effect on the ball. -/
theorem unitSpan_subset_fullEffects : unitSpan directionalFamily ⊆ fullEffects ball3 := by
  rintro e ⟨f, ⟨b, hb, rfl⟩, α, β, hα, hβ, hαβ, rfl⟩
  intro v hv
  rw [mix_apply, unitEffect_apply]
  have hf := ballEffect_isEffectOn hb v hv
  constructor <;> nlinarith [hf.1, hf.2]

/-- The effect space of the ball, both directions cited. -/
theorem fullEffects_eq_unitSpan : fullEffects ball3 = unitSpan directionalFamily :=
  Set.Subset.antisymm fullEffects_subset_unitSpan unitSpan_subset_fullEffects

/-! #### The unbiased family -/

/-- The unbiased family `{(1 + b · v)/2 : b · b ≤ 1}`. -/
def unbiasedFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ b : Fin 3 → ℝ, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 ≤ 1 ∧ e = ballEffect b}

theorem unbiasedFamily_convexClosed : ConvexClosed unbiasedFamily := by
  rintro e ⟨b, hb, rfl⟩ f ⟨b', hb', rfl⟩ α β hα hβ hαβ
  have hm : α • b + β • b' ∈ ball3 :=
    ball3_convex ((mem_ball3 b).mpr hb) ((mem_ball3 b').mpr hb') hα hβ hαβ
  refine ⟨α • b + β • b', (mem_ball3 _).mp hm, ?_⟩
  apply AffineMap.ext
  intro v
  rw [mix_apply]
  simp only [ballEffect_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  linear_combination (1 / 2 : ℝ) * hαβ

theorem unbiasedFamily_convex : Convex ℝ unbiasedFamily := by
  intro e he f hf α β hα hβ hαβ
  exact unbiasedFamily_convexClosed e he f hf α β hα hβ hαβ

/-- The convex hull of the directional family lies in the unbiased family. -/
theorem convexHull_directional_subset_unbiased :
    convexHull ℝ directionalFamily ⊆ unbiasedFamily := by
  refine convexHull_min ?_ unbiasedFamily_convex
  intro e he
  obtain ⟨b, hb, h⟩ := he
  exact ⟨b, hb.le, h⟩

/-- The unbiased family lies in the convex hull of the directional family: each member is a
two-point combination of antipodal directional effects. -/
theorem unbiasedFamily_subset_convexHull : unbiasedFamily ⊆ convexHull ℝ directionalFamily := by
  rintro e ⟨b, hb, rfl⟩
  obtain ⟨B, hB⟩ : ∃ B : ℝ, B = b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 := ⟨_, rfl⟩
  have hB0 : 0 ≤ B := by rw [hB]; positivity
  rcases eq_or_lt_of_le hB0 with hz | hpos
  · have q0 := sq_nonneg (b 0)
    have q1 := sq_nonneg (b 1)
    have q2 := sq_nonneg (b 2)
    have z0 : b 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    have z1 : b 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    have z2 : b 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
    have hez : ballEffect ![0, 0, 1] ∈ convexHull ℝ directionalFamily :=
      subset_convexHull ℝ _ ⟨_, ez_sphere, rfl⟩
    have hnez : ballEffect ![0, 0, -1] ∈ convexHull ℝ directionalFamily :=
      subset_convexHull ℝ _ ⟨_, nez_sphere, rfl⟩
    have heq : ballEffect b =
        (1 / 2 : ℝ) • ballEffect ![0, 0, 1] + (1 / 2 : ℝ) • ballEffect ![0, 0, -1] := by
      apply AffineMap.ext
      intro v
      rw [mix_apply, ballEffect_apply, ballEffect_apply, ballEffect_apply, z0, z1, z2]
      show (1 : ℝ) / 2 + (0 * v 0 + 0 * v 1 + 0 * v 2) / 2 =
        1 / 2 * (1 / 2 + (0 * v 0 + 0 * v 1 + 1 * v 2) / 2) +
          1 / 2 * (1 / 2 + (0 * v 0 + 0 * v 1 + -1 * v 2) / 2)
      ring
    rw [heq]
    exact convex_convexHull ℝ _ hez hnez (by norm_num) (by norm_num) (by norm_num)
  · set s := Real.sqrt B with hs
    have hs0 : 0 < s := Real.sqrt_pos.2 hpos
    have hs2 : s ^ 2 = B := Real.sq_sqrt hB0
    have hs1 : s ≤ 1 := by nlinarith
    obtain ⟨k, hk⟩ : ∃ k : ℝ, s * k = 1 := ⟨_, mul_inv_cancel₀ hs0.ne'⟩
    have hk2 : s ^ 2 * k ^ 2 = 1 := by rw [← mul_pow, hk, one_pow]
    have hu : (![b 0 * k, b 1 * k, b 2 * k] : Fin 3 → ℝ) 0 ^ 2 +
        (![b 0 * k, b 1 * k, b 2 * k] : Fin 3 → ℝ) 1 ^ 2 +
        (![b 0 * k, b 1 * k, b 2 * k] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
      show (b 0 * k) ^ 2 + (b 1 * k) ^ 2 + (b 2 * k) ^ 2 = 1
      have e1 : (b 0 * k) ^ 2 + (b 1 * k) ^ 2 + (b 2 * k) ^ 2 = s ^ 2 * k ^ 2 := by
        rw [hs2, hB]; ring
      rw [e1, hk2]
    have hnu : (![-(b 0 * k), -(b 1 * k), -(b 2 * k)] : Fin 3 → ℝ) 0 ^ 2 +
        (![-(b 0 * k), -(b 1 * k), -(b 2 * k)] : Fin 3 → ℝ) 1 ^ 2 +
        (![-(b 0 * k), -(b 1 * k), -(b 2 * k)] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
      show (-(b 0 * k)) ^ 2 + (-(b 1 * k)) ^ 2 + (-(b 2 * k)) ^ 2 = 1
      have e1 : (-(b 0 * k)) ^ 2 + (-(b 1 * k)) ^ 2 + (-(b 2 * k)) ^ 2 = s ^ 2 * k ^ 2 := by
        rw [hs2, hB]; ring
      rw [e1, hk2]
    have hu' : ballEffect ![b 0 * k, b 1 * k, b 2 * k] ∈ convexHull ℝ directionalFamily :=
      subset_convexHull ℝ _ ⟨_, hu, rfl⟩
    have hnu' : ballEffect ![-(b 0 * k), -(b 1 * k), -(b 2 * k)] ∈
        convexHull ℝ directionalFamily :=
      subset_convexHull ℝ _ ⟨_, hnu, rfl⟩
    have heq : ballEffect b = ((1 + s) / 2) • ballEffect ![b 0 * k, b 1 * k, b 2 * k] +
        ((1 - s) / 2) • ballEffect ![-(b 0 * k), -(b 1 * k), -(b 2 * k)] := by
      apply AffineMap.ext
      intro v
      rw [mix_apply, ballEffect_apply, ballEffect_apply, ballEffect_apply]
      show (1 : ℝ) / 2 + (b 0 * v 0 + b 1 * v 1 + b 2 * v 2) / 2 =
        (1 + s) / 2 * (1 / 2 + (b 0 * k * v 0 + b 1 * k * v 1 + b 2 * k * v 2) / 2) +
          (1 - s) / 2 * (1 / 2 + (-(b 0 * k) * v 0 + -(b 1 * k) * v 1 + -(b 2 * k) * v 2) / 2)
      linear_combination (-(b 0 * v 0 + b 1 * v 1 + b 2 * v 2) / 2) * hk
    rw [heq]
    exact convex_convexHull ℝ _ hu' hnu' (by linarith) (by linarith) (by ring)

/-- A member of the unbiased family is an effect on the ball with the value `1/2` at the
centre. -/
theorem unbiased_isEffectOn_half {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (h : e ∈ unbiasedFamily) :
    IsEffectOn ball3 e ∧ e 0 = 1 / 2 := by
  obtain ⟨b, hb, rfl⟩ := h
  refine ⟨fun v hv => ?_, ?_⟩
  · rw [mem_ball3] at hv
    rw [ballEffect_apply]
    constructor <;> nlinarith [sq_nonneg (b 0 - v 0), sq_nonneg (b 1 - v 1),
      sq_nonneg (b 2 - v 2), sq_nonneg (b 0 + v 0), sq_nonneg (b 1 + v 1), sq_nonneg (b 2 + v 2)]
  · rw [ballEffect_apply]
    simp

/-- An effect on the ball with the value `1/2` at the centre is in the unbiased family. -/
theorem mem_unbiased_of_half {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 e)
    (h0 : e 0 = 1 / 2) : e ∈ unbiasedFamily := by
  obtain ⟨c, a0, a1, a2, -, -, h2, -, hr⟩ := effect_decomp he
  have hc : c = 1 / 2 := by
    have h := hr 0
    simp only [Pi.zero_apply, zero_mul, add_zero] at h
    rw [h0] at h
    exact h.symm
  rw [hc] at h2
  refine ⟨![2 * a0, 2 * a1, 2 * a2], ?_, ?_⟩
  · show (2 * a0) ^ 2 + (2 * a1) ^ 2 + (2 * a2) ^ 2 ≤ 1
    nlinarith [h2]
  · apply AffineMap.ext
    intro v
    rw [hr v, ballEffect_apply, hc]
    show 1 / 2 + v 0 * a0 + v 1 * a1 + v 2 * a2 =
      1 / 2 + (2 * a0 * v 0 + 2 * a1 * v 1 + 2 * a2 * v 2) / 2
    ring

/-- The unit is not in the unbiased family. -/
theorem unitEffect_not_unbiased : unitEffect ∉ unbiasedFamily := by
  rintro ⟨b, -, h⟩
  have h1 : unitEffect (0 : Fin 3 → ℝ) = ballEffect b 0 := by rw [h]
  rw [unitEffect_apply, ballEffect_apply] at h1
  norm_num at h1

/-- OG-1's unsharp seed `3/4 + z/4` is not in the unbiased family. -/
theorem unsharpSeed_not_unbiased : unsharpSeed ∉ unbiasedFamily := by
  rintro ⟨b, -, h⟩
  have h1 : unsharpSeed 0 = ballEffect b 0 := by rw [h]
  rw [unsharpSeed_apply, ballEffect_apply] at h1
  norm_num at h1

/-- The unsharp seed is an effect on the ball (OG-1's `unsharpSeed_isEffectOn`). -/
theorem unsharpSeed_mem_fullEffects : unsharpSeed ∈ fullEffects ball3 := unsharpSeed_isEffectOn

end Ball

/-! ### §C — generation (target (A)) -/

section Generation

variable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}

/-- **Target (A).** A family containing the directional family and the unit and closed under
mixing contains the sub-convex span of the unit with the directional family. The mixing closure
is a hypothesis. -/
theorem generation_of_mixingClosed {A : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hD : directionalFamily ⊆ A) (hU : unitEffect ∈ A) (hM : MixingClosed A) :
    unitSpan directionalFamily ⊆ A :=
  unitSpan_subset_of_mixingClosed hD hU hM

/-- OG-1's generation half in subset form: the directional family is available. -/
theorem directionalFamily_subset_avail (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail) :
    directionalFamily ⊆ avail := by
  rw [← seedOrbit_ball3_eq hG hP1 hK]
  exact seedOrbit_subset hV4

/-- **Target (A), chained through OG-1.** Under `PreservesBody`, P1, K∞-R, V4′, the unit
available and the mixing closure, the sub-convex span of the unit with the directional family is
available. -/
theorem unitSpan_subset_avail (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hU : unitEffect ∈ avail) (hM : MixingClosed avail) : unitSpan directionalFamily ⊆ avail :=
  generation_of_mixingClosed (directionalFamily_subset_avail hG hP1 hK hV4) hU hM

/-- Targets (A) and (B) together: every effect on the ball is available. -/
theorem fullEffects_subset_avail (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hU : unitEffect ∈ avail) (hM : MixingClosed avail) : fullEffects ball3 ⊆ avail :=
  fullEffects_subset_unitSpan.trans (unitSpan_subset_avail hG hP1 hK hV4 hU hM)

/-- With the premise that every available functional is an effect on the ball, the available
family is exactly the effect space of the ball. -/
theorem avail_eq_fullEffects (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hU : unitEffect ∈ avail) (hM : MixingClosed avail) (hE : EffectsOn ball3 avail) :
    avail = fullEffects ball3 :=
  Set.Subset.antisymm (fun e he => hE e he) (fullEffects_subset_avail hG hP1 hK hV4 hU hM)

end Generation

/-! ### §D — controls -/

section Controls

/-- Positive control: the full effect family of the ball satisfies every premise of the
generation theorem, with all automorphisms of the ball and the seed `(1 + z)/2`. -/
theorem avail_fullEffects_control :
    SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) (fullEffects ball3) ∧
      unitEffect ∈ fullEffects ball3 ∧ MixingClosed (fullEffects ball3) ∧
      EffectsOn ball3 (fullEffects ball3) :=
  ⟨fun g hg => isEffectOn_seedTransport (ballEffect_isEffectOn ez_sphere)
      (fun z hz => (preservesBody_fullAut3 g hg z hz).2),
    unitEffect_mem_fullEffects ball3, mixingClosed_fullEffects ball3, fun _ he => he⟩

/-- The span itself satisfies the unit and mixing premises, so the premises are not the
conclusion restated: the content is the upper bound. -/
theorem unitEffect_mem_unitSpan : unitEffect ∈ unitSpan directionalFamily :=
  ⟨ballEffect ![0, 0, 1], ⟨_, ez_sphere, rfl⟩, 1, 0, zero_le_one, le_rfl, by norm_num,
    by apply AffineMap.ext; intro v; rw [mix_apply]; ring⟩

theorem mixingClosed_unitSpan_directional : MixingClosed (unitSpan directionalFamily) := by
  rw [← fullEffects_eq_unitSpan]
  exact mixingClosed_fullEffects ball3

/-- Negative control: the family of the unit, the zero effect and the directional effects is
not mixing closed; the half-half mixture of the unit with `(1 + z)/2` is the unsharp seed. -/
theorem not_mixingClosed_discrete :
    ¬ MixingClosed ({unitEffect, 0} ∪ directionalFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) := by
  intro hM
  have hU : unitEffect ∈ ({unitEffect, 0} ∪ directionalFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) :=
    Set.mem_union_left _ (Set.mem_insert _ _)
  have hZ : ballEffect ![0, 0, 1] ∈
      ({unitEffect, 0} ∪ directionalFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) :=
    Set.mem_union_right _ ⟨_, ez_sphere, rfl⟩
  have h := hM _ hU _ hZ (1 / 2) (1 / 2) (by norm_num) (by norm_num) (by norm_num)
  have heq : (1 / 2 : ℝ) • unitEffect + (1 / 2 : ℝ) • ballEffect ![0, 0, 1] = unsharpSeed := by
    apply AffineMap.ext
    intro v
    rw [mix_apply, unitEffect_apply, ballEffect_apply, unsharpSeed_apply]
    show (1 : ℝ) / 2 * 1 + 1 / 2 * (1 / 2 + (0 * v 0 + 0 * v 1 + 1 * v 2) / 2) = 3 / 4 + v 2 / 4
    ring
  rw [heq, Set.mem_union, Set.mem_insert_iff, Set.mem_singleton_iff] at h
  rcases h with (h | h) | ⟨b, hb, h⟩
  · obtain ⟨y, -, hy⟩ := unsharpSeed_isProperOn
    rw [h, unitEffect_apply] at hy
    exact lt_irrefl _ hy
  · have h1 : unsharpSeed ![0, 0, 1] = (0 : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) ![0, 0, 1] := by rw [h]
    rw [unsharpSeed_certain, AffineMap.coe_zero, Pi.zero_apply] at h1
    exact one_ne_zero h1
  · have hS : SharpSeed ball3 unsharpSeed := by
      rw [h]
      exact ballEffect_sharp hb
    exact not_sharpSeed_unsharp hS

/-- The effects reading the third coordinate alone, `v ↦ c + a · v 2` with `|a| ≤ c` and
`|a| ≤ 1 − c`: the effect space of the classical bit on an axis of the ball. -/
def bitFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ c a : ℝ, |a| ≤ c ∧ |a| ≤ 1 - c ∧ ∀ v, e v = c + a * v 2}

theorem unitEffect_mem_bitFamily : unitEffect ∈ bitFamily :=
  ⟨1, 0, by norm_num, by norm_num, fun v => by rw [unitEffect_apply]; ring⟩

theorem ballEffect_ez_mem_bitFamily : ballEffect ![0, 0, 1] ∈ bitFamily :=
  ⟨1 / 2, 1 / 2, abs_le.mpr ⟨by norm_num, by norm_num⟩, abs_le.mpr ⟨by norm_num, by norm_num⟩,
    fun v => by
      rw [ballEffect_apply]
      show (1 : ℝ) / 2 + (0 * v 0 + 0 * v 1 + 1 * v 2) / 2 = 1 / 2 + 1 / 2 * v 2
      ring⟩

theorem bitFamily_mixingClosed : MixingClosed bitFamily := by
  rintro e ⟨c1, a1, h1, h1', he⟩ f ⟨c2, a2, h2, h2', hf⟩ α β hα hβ hαβ
  obtain ⟨l1, u1⟩ := abs_le.mp h1
  obtain ⟨l1', u1'⟩ := abs_le.mp h1'
  obtain ⟨l2, u2⟩ := abs_le.mp h2
  obtain ⟨l2', u2'⟩ := abs_le.mp h2'
  refine ⟨α * c1 + β * c2, α * a1 + β * a2, abs_le.mpr ⟨?_, ?_⟩, abs_le.mpr ⟨?_, ?_⟩,
    fun v => ?_⟩
  · nlinarith
  · nlinarith
  · nlinarith
  · nlinarith
  · rw [mix_apply, he v, hf v]
    ring

theorem bitFamily_effectsOn : EffectsOn ball3 bitFamily := by
  rintro e ⟨c, a, h, h', he⟩ v hv
  rw [mem_ball3] at hv
  rw [he v]
  obtain ⟨l, u⟩ := abs_le.mp h
  obtain ⟨l', u'⟩ := abs_le.mp h'
  have hv2 : v 2 ^ 2 ≤ 1 := by nlinarith [sq_nonneg (v 0), sq_nonneg (v 1)]
  have hvl : -1 ≤ v 2 := by nlinarith
  have hvu : v 2 ≤ 1 := by nlinarith
  constructor
  · nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ c + a) (by linarith : (0 : ℝ) ≤ 1 + v 2),
      mul_nonneg (by linarith : (0 : ℝ) ≤ c - a) (by linarith : (0 : ℝ) ≤ 1 - v 2)]
  · nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - c - a) (by linarith : (0 : ℝ) ≤ 1 + v 2),
      mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - c + a) (by linarith : (0 : ℝ) ≤ 1 - v 2)]

theorem ballEffect_ex_not_mem_bitFamily : ballEffect ![1, 0, 0] ∉ bitFamily := by
  rintro ⟨c, a, -, -, he⟩
  have h1 := he ![1, 0, 0]
  have h2 := he (-![1, 0, 0])
  rw [ballEffect_self ex_sphere] at h1
  rw [ballEffect_neg_self ex_sphere] at h2
  change (1 : ℝ) = c + a * 0 at h1
  change (0 : ℝ) = c + a * -0 at h2
  norm_num at h1 h2
  linarith

/-- Negative control: the bit family satisfies the unit, mixing, effect, sharp-seed and
transitivity premises and fails seed-orbit availability. -/
theorem not_seedOrbitAvailable_bitFamily :
    ¬ SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) bitFamily := by
  intro hV4
  have hmem : ballEffect ![1, 0, 0] ∈ seedOrbit fullAut3 (ballEffect ![0, 0, 1]) := by
    rw [seedOrbit_fullAut3]
    exact ⟨_, ex_sphere, rfl⟩
  exact ballEffect_ex_not_mem_bitFamily (seedOrbit_subset hV4 hmem)

/-- Negative control: the identity alone is not boundary transitive. -/
theorem not_boundaryTransitive_refl :
    ¬ BoundaryTransitive ball3 {AffineEquiv.refl ℝ (Fin 3 → ℝ)} := by
  intro hK
  obtain ⟨g, hg, hgx⟩ := hK ![1, 0, 0] ![0, 0, 1] (isBoundaryState_ball3_of_sphere ex_sphere)
    (isBoundaryState_ball3_of_sphere ez_sphere)
  rw [Set.mem_singleton_iff] at hg
  subst hg
  rw [AffineEquiv.refl_apply] at hgx
  have h0 := congrFun hgx 0
  change (1 : ℝ) = 0 at h0
  exact one_ne_zero h0

/-- Under the identity alone the seed orbit of `(1 + z)/2` is available in the span of that one
effect. -/
theorem seedOrbitAvailable_refl :
    SeedOrbitAvailable {AffineEquiv.refl ℝ (Fin 3 → ℝ)} (ballEffect ![0, 0, 1])
      (unitSpan {ballEffect ![0, 0, 1]}) := by
  intro g hg
  rw [Set.mem_singleton_iff] at hg
  subst hg
  rw [seedTransport_refl]
  exact ⟨_, Set.mem_singleton _, 0, 1, le_rfl, zero_le_one, by norm_num,
    by apply AffineMap.ext; intro v; rw [mix_apply]; ring⟩

theorem ballEffect_ex_not_mem_unitSpan_ez :
    ballEffect ![1, 0, 0] ∉ unitSpan {ballEffect ![0, 0, 1]} := by
  rintro ⟨f, hf, α, β, -, -, -, h⟩
  rw [Set.mem_singleton_iff] at hf
  subst hf
  have h1 : ballEffect ![1, 0, 0] ![1, 0, 0] =
      (α • unitEffect + β • ballEffect ![0, 0, 1] : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) ![1, 0, 0] := by
    rw [← h]
  have h2 : ballEffect ![1, 0, 0] (-![1, 0, 0]) =
      (α • unitEffect + β • ballEffect ![0, 0, 1] : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (-![1, 0, 0]) := by
    rw [← h]
  rw [ballEffect_self ex_sphere, mix_apply, unitEffect_apply, ballEffect_apply] at h1
  rw [ballEffect_neg_self ex_sphere, mix_apply, unitEffect_apply, ballEffect_apply] at h2
  change (1 : ℝ) = α * 1 + β * (1 / 2 + (0 * 1 + 0 * 0 + 1 * 0) / 2) at h1
  change (0 : ℝ) = α * 1 + β * (1 / 2 + (0 * -1 + 0 * -0 + 1 * -0) / 2) at h2
  norm_num at h1 h2
  linarith

/-- Negative control: the universal family fails the effect premise. -/
theorem not_effectsOn_univ : ¬ EffectsOn ball3 (Set.univ : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) := by
  intro hE
  have h0 : (0 : Fin 3 → ℝ) ∈ ball3 := by
    rw [mem_ball3]
    norm_num
  have h := (hE ((2 : ℝ) • unitEffect) (Set.mem_univ _) 0 h0).2
  simp only [AffineMap.coe_smul, Pi.smul_apply, unitEffect_apply, smul_eq_mul, mul_one] at h
  norm_num at h

/-- Countercontrol: a countable family is never boundary transitive on `ball3`, since the
boundary states are the unit sphere, which is uncountable. Exact transitivity therefore needs an
uncountable repertoire; no limit closure is adopted here. -/
theorem not_boundaryTransitive_of_countable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    (hG : G.Countable) : ¬ BoundaryTransitive ball3 G := by
  intro hK
  have hsph : {b : Fin 3 → ℝ | b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1}.Countable := by
    refine Set.Countable.mono ?_ (hG.image fun g => g ![0, 0, 1])
    intro b hb
    obtain ⟨g, hg, hgb⟩ := hK ![0, 0, 1] b (isBoundaryState_ball3_of_sphere ez_sphere)
      (isBoundaryState_ball3_of_sphere hb)
    exact ⟨g, hg, hgb⟩
  have hmaps : Set.MapsTo (fun t : ℝ => (![t, Real.sqrt (1 - t ^ 2), 0] : Fin 3 → ℝ))
      (Set.Icc (-1 : ℝ) 1) {b : Fin 3 → ℝ | b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1} := by
    intro t ht
    obtain ⟨h1, h2⟩ := ht
    have hnn : 0 ≤ 1 - t ^ 2 := by nlinarith
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

end Controls

/-! ### The verdict -/

/-- The two targets with their controls, together: the upper bound in both forms, the two
inclusions, the abstract and the chained generation theorems, the unsharp-seed gap, and the
mixing, availability, transitivity and countability controls. -/
theorem eff1_core :
    fullEffects ball3 ⊆ unitSpan directionalFamily ∧
    unitSpan directionalFamily ⊆ fullEffects ball3 ∧
    (∀ e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn ball3 e →
      ∃ (a : ℝ) (v : Fin 3 → ℝ), 0 ≤ a ∧ a ≤ 1 ∧ Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧
        ∀ r : Fin 3 → ℝ, e r = a + ∑ j, v j * r j) ∧
    (∀ A : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ), directionalFamily ⊆ A → unitEffect ∈ A →
      MixingClosed A → unitSpan directionalFamily ⊆ A) ∧
    (∀ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ)
      (avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)),
      PreservesBody ball3 G → SharpSeed ball3 r → BoundaryTransitive ball3 G →
      SeedOrbitAvailable G r avail → unitEffect ∈ avail → MixingClosed avail →
      EffectsOn ball3 avail → avail = fullEffects ball3) ∧
    unsharpSeed ∈ fullEffects ball3 ∧ unsharpSeed ∉ unbiasedFamily ∧
    ¬ MixingClosed ({unitEffect, 0} ∪ directionalFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) ∧
    ¬ SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) bitFamily ∧
    ¬ BoundaryTransitive ball3 {AffineEquiv.refl ℝ (Fin 3 → ℝ)} ∧
    (∀ G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)), G.Countable → ¬ BoundaryTransitive ball3 G) := by
  refine ⟨fullEffects_subset_unitSpan, unitSpan_subset_fullEffects,
    fun e he => effect_eq_affine he, fun A hD hU hM => generation_of_mixingClosed hD hU hM,
    fun G r avail hG hP1 hK hV4 hU hM hE => avail_eq_fullEffects hG hP1 hK hV4 hU hM hE,
    unsharpSeed_mem_fullEffects, unsharpSeed_not_unbiased, not_mixingClosed_discrete,
    not_seedOrbitAvailable_bitFamily, not_boundaryTransitive_refl,
    fun G hG => not_boundaryTransitive_of_countable hG⟩

end EffectSpace
end OIBridge

#print axioms OIBridge.EffectSpace.unitEffect_apply
#print axioms OIBridge.EffectSpace.mix_apply
#print axioms OIBridge.EffectSpace.effectsOn_iff_subset
#print axioms OIBridge.EffectSpace.unitEffect_mem_fullEffects
#print axioms OIBridge.EffectSpace.mixingClosed_fullEffects
#print axioms OIBridge.EffectSpace.unitSpan_subset_of_mixingClosed
#print axioms OIBridge.EffectSpace.seedTransport_refl
#print axioms OIBridge.EffectSpace.ex_sphere
#print axioms OIBridge.EffectSpace.nez_sphere
#print axioms OIBridge.EffectSpace.coeff_bounds
#print axioms OIBridge.EffectSpace.effect_decomp
#print axioms OIBridge.EffectSpace.effect_eq_affine
#print axioms OIBridge.EffectSpace.fullEffects_subset_unitSpan
#print axioms OIBridge.EffectSpace.unitSpan_subset_fullEffects
#print axioms OIBridge.EffectSpace.fullEffects_eq_unitSpan
#print axioms OIBridge.EffectSpace.unbiasedFamily_convexClosed
#print axioms OIBridge.EffectSpace.unbiasedFamily_convex
#print axioms OIBridge.EffectSpace.convexHull_directional_subset_unbiased
#print axioms OIBridge.EffectSpace.unbiasedFamily_subset_convexHull
#print axioms OIBridge.EffectSpace.unbiased_isEffectOn_half
#print axioms OIBridge.EffectSpace.mem_unbiased_of_half
#print axioms OIBridge.EffectSpace.unitEffect_not_unbiased
#print axioms OIBridge.EffectSpace.unsharpSeed_not_unbiased
#print axioms OIBridge.EffectSpace.unsharpSeed_mem_fullEffects
#print axioms OIBridge.EffectSpace.generation_of_mixingClosed
#print axioms OIBridge.EffectSpace.directionalFamily_subset_avail
#print axioms OIBridge.EffectSpace.unitSpan_subset_avail
#print axioms OIBridge.EffectSpace.fullEffects_subset_avail
#print axioms OIBridge.EffectSpace.avail_eq_fullEffects
#print axioms OIBridge.EffectSpace.avail_fullEffects_control
#print axioms OIBridge.EffectSpace.unitEffect_mem_unitSpan
#print axioms OIBridge.EffectSpace.mixingClosed_unitSpan_directional
#print axioms OIBridge.EffectSpace.not_mixingClosed_discrete
#print axioms OIBridge.EffectSpace.unitEffect_mem_bitFamily
#print axioms OIBridge.EffectSpace.ballEffect_ez_mem_bitFamily
#print axioms OIBridge.EffectSpace.bitFamily_mixingClosed
#print axioms OIBridge.EffectSpace.bitFamily_effectsOn
#print axioms OIBridge.EffectSpace.ballEffect_ex_not_mem_bitFamily
#print axioms OIBridge.EffectSpace.not_seedOrbitAvailable_bitFamily
#print axioms OIBridge.EffectSpace.not_boundaryTransitive_refl
#print axioms OIBridge.EffectSpace.seedOrbitAvailable_refl
#print axioms OIBridge.EffectSpace.ballEffect_ex_not_mem_unitSpan_ez
#print axioms OIBridge.EffectSpace.not_effectsOn_univ
#print axioms OIBridge.EffectSpace.not_boundaryTransitive_of_countable
#print axioms OIBridge.EffectSpace.eff1_core
