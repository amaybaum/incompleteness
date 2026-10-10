/-! ### §G — hypothesis K∞-1, as a statement, and its controls -/

/-- **Hypothesis K∞-1**, stated and not proved: a compact convex body admitting an elementary
drive has supporting-effect completeness relative to the available effects. This is the
field-neutral Naimark step. Compactness enters because an open body has no boundary state
(`supportingEffectComplete_of_isOpen`). The module proves K∞-1 for no physical family; it is an
open target. -/
def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →
    SupportingEffectComplete Ω avail

/-- What K∞-1 buys when it holds: with singleton faces, a compact convex drivable body is
relatively strictly convex. -/
theorem relStrictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hcomp : IsCompact Ω) (hconv : Convex ℝ Ω) (hK : KInf1 Ω avail)
    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :
    RelStrictConvex Ω :=
  relStrictConvex_of_supporting_singleton hconv (hK hcomp hconv hD) hSF

/-- The effect `v ↦ (1 + u · v)/2` on `ℝ³`. -/
noncomputable def ballEffect (u : Fin 3 → ℝ) : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 3 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (u 0 • LinearMap.proj 0 + u 1 • LinearMap.proj 1 + u 2 • LinearMap.proj 2 :
      (Fin 3 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem ballEffect_apply (u v : Fin 3 → ℝ) :
    ballEffect u v = 1 / 2 + (u 0 * v 0 + u 1 * v 1 + u 2 * v 2) / 2 := by
  simp [ballEffect] <;> ring

/-- A step from a state of the ball off its sphere, by a sixteenth of the gap, stays in it. -/
theorem ball3_extend {x0 x1 x2 y0 y1 y2 ε : ℝ} (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 ≤ 1)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 ≤ 1) (hε : 0 < ε)
    (hε' : 16 * ε = 1 - (x0 ^ 2 + x1 ^ 2 + x2 ^ 2)) :
    (x0 + ε * (x0 - y0)) ^ 2 + (x1 + ε * (x1 - y1)) ^ 2 + (x2 + ε * (x2 - y2)) ^ 2 ≤ 1 := by
  have hT : (x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2 ≤ 4 := by
    nlinarith [sq_nonneg (x0 + y0), sq_nonneg (x1 + y1), sq_nonneg (x2 + y2)]
  have hS : x0 * (x0 - y0) + x1 * (x1 - y1) + x2 * (x2 - y2) ≤ 2 := by
    nlinarith [sq_nonneg (x0 + y0), sq_nonneg (x1 + y1), sq_nonneg (x2 + y2)]
  have hε1 : ε ≤ 1 / 16 := by nlinarith [sq_nonneg x0, sq_nonneg x1, sq_nonneg x2]
  have h1 := mul_le_mul_of_nonneg_left hS hε.le
  have h2 := mul_le_mul_of_nonneg_left hT (mul_nonneg hε.le hε.le)
  have h3 := mul_le_mul_of_nonneg_left hε1 hε.le
  nlinarith [h1, h2, h3]

/-- **Positive control for (SEC) on a drivable body.** The ball has supporting-effect
completeness with its full effects: a boundary state lies on the unit sphere, and the effect
`v ↦ (1 + x · v)/2` is a proper effect certain there. -/
theorem supportingEffectComplete_ball3 : SupportingEffectComplete ball3 (fullEffects ball3) := by
  rintro x ⟨hx, y, hy, hout⟩
  rw [mem_ball3] at hx hy
  have hsph : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 = 1 := by
    by_contra hne
    have hlt := lt_of_le_of_ne hx hne
    apply hout ((1 - (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2)) / 16) (by linarith)
    rw [mem_ball3]
    simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
    exact ball3_extend hx hy (by linarith) (by ring)
  have heff : IsEffectOn ball3 (ballEffect x) := by
    intro v hv
    rw [mem_ball3] at hv
    rw [ballEffect_apply]
    constructor <;> nlinarith [sq_nonneg (x 0 - v 0), sq_nonneg (x 1 - v 1),
      sq_nonneg (x 2 - v 2), sq_nonneg (x 0 + v 0), sq_nonneg (x 1 + v 1), sq_nonneg (x 2 + v 2)]
  refine ⟨ballEffect x, heff, heff, ⟨0, ?_, ?_⟩, ?_⟩
  · rw [mem_ball3]; norm_num
  · rw [ballEffect_apply]; norm_num
  · rw [ballEffect_apply]; linear_combination hsph / 2

/-- **K∞-1 holds non-vacuously** for the ball with its full effects: the ball is compact, convex
and drivable, and has supporting-effect completeness. -/
theorem kInf1_ball3_full : KInf1 ball3 (fullEffects ball3) :=
  fun _ _ _ => supportingEffectComplete_ball3

/-- The state `(1, 0, 0)` of the ball is a boundary state. -/
theorem isBoundaryState_ball3 : IsBoundaryState ball3 ![1, 0, 0] := by
  refine ⟨by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, ![-1, 0, 0],
    by show (-1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun ε hε h => ?_⟩
  change (1 + ε * (1 - -1)) ^ 2 + (0 + ε * (0 - 0)) ^ 2 + (0 + ε * (0 - 0)) ^ 2 ≤ 1 at h
  nlinarith

/-- **K∞-1 fails** for the ball with the unit effect alone: the ball is compact, convex and
drivable, and its boundary state `(1, 0, 0)` is certain for no proper available effect. So K∞-1
is a proposition about the effect family, not a consequence of the body. -/
theorem not_kInf1_ball3_unit : ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} := by
  intro hK
  obtain ⟨e, he, -, hp, -⟩ := hK ball3_isCompact ball3_convex ball3_drivable _ isBoundaryState_ball3
  rw [Set.mem_singleton_iff] at he
  subst he
  exact not_isProperOn_const_one _ hp

