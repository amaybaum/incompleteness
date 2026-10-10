/-! ### §C′ — drivability holds on the ball and fails on the bit -/

/-- The Euclidean unit ball of `ℝ³`, cut out by its quadratic form. -/
def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}

theorem mem_ball3 (v : Fin 3 → ℝ) : v ∈ ball3 ↔ v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1 := Iff.rfl

theorem vec3_ext {v w : Fin 3 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2) :
    v = w := by
  funext i
  fin_cases i
  exacts [h0, h1, h2]

/-- The ball is convex. -/
theorem ball3_convex : Convex ℝ ball3 := by
  intro x hx y hy a b ha hb hab
  rw [mem_ball3] at hx hy ⊢
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  obtain rfl : b = 1 - a := by linarith
  nlinarith [mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 0 - y 0)),
    mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 1 - y 1)),
    mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 2 - y 2)),
    mul_le_mul_of_nonneg_left hx ha, mul_le_mul_of_nonneg_left hy hb]

/-- The ball is compact. -/
theorem ball3_isCompact : IsCompact ball3 := by
  have hcl : IsClosed ball3 :=
    isClosed_le (f := fun v : Fin 3 → ℝ => v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) (g := fun _ => (1 : ℝ))
      (by fun_prop) continuous_const
  have hsub : ball3 ⊆ Metric.closedBall (0 : Fin 3 → ℝ) 1 := by
    intro v hv
    rw [mem_ball3] at hv
    rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
    intro i
    have h1 : v i ^ 2 ≤ ∑ j, v j ^ 2 :=
      Finset.single_le_sum (f := fun j => v j ^ 2) (fun j _ => sq_nonneg (v j))
        (Finset.mem_univ i)
    simp only [Fin.sum_univ_three] at h1
    rw [Real.norm_eq_abs, abs_le]
    constructor <;> nlinarith
  exact Metric.isCompact_of_isClosed_isBounded hcl (Metric.isBounded_closedBall.subset hsub)

/-- The rotation of `ℝ³` by the angle `t` about the third axis. -/
noncomputable def rotFun (t : ℝ) (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]

theorem rotFun_apply (t : ℝ) (v : Fin 3 → ℝ) :
    rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧
      rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2 :=
  ⟨rfl, rfl, rfl⟩

theorem rotFun_zero (v : Fin 3 → ℝ) : rotFun 0 v = v := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply 0 v
  apply vec3_ext
  · rw [a0, Real.cos_zero, Real.sin_zero]; ring
  · rw [a1, Real.cos_zero, Real.sin_zero]; ring
  · exact a2

theorem rotFun_add (s t : ℝ) (v : Fin 3 → ℝ) : rotFun s (rotFun t v) = rotFun (s + t) v := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply s (rotFun t v)
  obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
  obtain ⟨c0, c1, c2⟩ := rotFun_apply (s + t) v
  apply vec3_ext
  · rw [a0, b0, b1, c0, Real.cos_add, Real.sin_add]; ring
  · rw [a1, b0, b1, c1, Real.cos_add, Real.sin_add]; ring
  · rw [a2, b2, c2]

/-- A rotation preserves the ball. -/
theorem rotFun_mem_ball3 (t : ℝ) {v : Fin 3 → ℝ} (hv : v ∈ ball3) : rotFun t v ∈ ball3 := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply t v
  rw [mem_ball3, a0, a1, a2]
  have key : (Real.cos t * v 0 - Real.sin t * v 1) ^ 2 +
      (Real.sin t * v 0 + Real.cos t * v 1) ^ 2 + v 2 ^ 2 = v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 := by
    linear_combination (v 0 ^ 2 + v 1 ^ 2) * Real.sin_sq_add_cos_sq t
  rw [key]
  exact hv

/-- The rotation by `t`, as a linear map. -/
noncomputable def rotLin (t : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun := rotFun t
  map_add' v w := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (v + w)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    obtain ⟨c0, c1, c2⟩ := rotFun_apply t w
    apply vec3_ext <;> simp only [Pi.add_apply, a0, a1, a2, b0, b1, b2, c0, c1, c2] <;> ring
  map_smul' r v := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (r • v)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    apply vec3_ext <;>
      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, b0, b1, b2] <;> ring

/-- The rotation by `t`, as a linear equivalence with inverse the rotation by `-t`. -/
noncomputable def rotEquiv (t : ℝ) : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) :=
  { rotLin t with
    invFun := rotFun (-t)
    left_inv := fun v => by
      show rotFun (-t) (rotFun t v) = v
      rw [rotFun_add, neg_add_cancel, rotFun_zero]
    right_inv := fun v => by
      show rotFun t (rotFun (-t) v) = v
      rw [rotFun_add, add_neg_cancel, rotFun_zero] }

/-- The rotation by `t`, as an affine automorphism of `ℝ³`. -/
noncomputable def rot3 (t : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := (rotEquiv t).toAffineEquiv

theorem rot3_apply (t : ℝ) (v : Fin 3 → ℝ) : rot3 t v = rotFun t v := rfl

/-- The cyclic permutation of the coordinates, `(x, y, z) ↦ (z, x, y)`. -/
noncomputable def cycEquiv : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) where
  toFun v := ![v 2, v 0, v 1]
  invFun v := ![v 1, v 2, v 0]
  map_add' v w := by apply vec3_ext <;> rfl
  map_smul' r v := by apply vec3_ext <;> rfl
  left_inv v := by apply vec3_ext <;> rfl
  right_inv v := by apply vec3_ext <;> rfl

/-- The cyclic permutation, as an affine automorphism of `ℝ³`. -/
noncomputable def cyc3 : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cycEquiv.toAffineEquiv

theorem cyc3_apply (v : Fin 3 → ℝ) : cyc3 v 0 = v 2 ∧ cyc3 v 1 = v 0 ∧ cyc3 v 2 = v 1 :=
  ⟨rfl, rfl, rfl⟩

theorem cyc3_symm_apply (v : Fin 3 → ℝ) :
    cyc3.symm v 0 = v 1 ∧ cyc3.symm v 1 = v 2 ∧ cyc3.symm v 2 = v 0 :=
  ⟨rfl, rfl, rfl⟩

theorem cyc3_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3 v ∈ ball3 := by
  obtain ⟨c0, c1, c2⟩ := cyc3_apply v
  rw [mem_ball3, c0, c1, c2]
  rw [mem_ball3] at hv
  linarith

theorem cyc3_symm_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3.symm v ∈ ball3 := by
  obtain ⟨c0, c1, c2⟩ := cyc3_symm_apply v
  rw [mem_ball3, c0, c1, c2]
  rw [mem_ball3] at hv
  linarith

/-- **Positive control for drivability.** The ball is drivable: the rotations about the third
axis form the flow, the half-turn is the NOT, and the cyclic permutation of the axes carries the
flow off itself on the ball. -/
noncomputable def ball3Drive : ElementaryDrivability ball3 where
  flow := rot3
  flow_zero := AffineEquiv.ext fun v => by rw [rot3_apply, rotFun_zero, AffineEquiv.refl_apply]
  flow_add s t := AffineEquiv.ext fun v => by
    simp only [AffineEquiv.trans_apply, rot3_apply, rotFun_add]
  flow_continuous := by
    refine continuous_pi fun i => ?_
    fin_cases i
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => q.2 2
      fun_prop
  flow_preserves t _ hv := rotFun_mem_ball3 t hv
  t₀ := Real.pi
  N_involutive x _ := by
    simp only [rot3_apply]
    obtain ⟨a0, a1, a2⟩ := rotFun_apply Real.pi (rotFun Real.pi x)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply Real.pi x
    apply vec3_ext
    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a2, b2]
  N_moves := ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => by
    have h0 : rot3 Real.pi ![1, 0, 0] 0 = (![1, 0, 0] : Fin 3 → ℝ) 0 := congrFun h 0
    change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0
    rw [Real.cos_pi, Real.sin_pi] at h0
    norm_num at h0⟩
  J := cyc3
  J_preserves _ hv := cyc3_mem_ball3 hv
  J_symm_preserves _ hv := cyc3_symm_mem_ball3 hv
  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1],
    by show (0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2 ≤ 1; norm_num, fun h => by
      have h2 : cyc3 (rot3 Real.pi (cyc3.symm ![0, 0, 1])) 2 = rot3 s ![0, 0, 1] 2 :=
        congrFun h 2
      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2
      rw [Real.sin_pi, Real.cos_pi] at h2
      norm_num at h2⟩⟩

/-- The ball is drivable. -/
theorem ball3_drivable : Nonempty (ElementaryDrivability ball3) := ⟨ball3Drive⟩

/-- An affine automorphism of the line is `x ↦ g 0 + g.linear 1 * x`. -/
theorem affineEquiv_real_apply (g : ℝ ≃ᵃ[ℝ] ℝ) (x : ℝ) : g x = g 0 + g.linear 1 * x := by
  have h := g.map_vadd 0 x
  simp only [vadd_eq_add, add_zero] at h
  have hl : g.linear x = g.linear 1 * x := by
    have := map_smul g.linear x (1 : ℝ)
    simp only [smul_eq_mul, mul_one] at this
    rw [this, mul_comm]
  rw [h, hl, add_comm]

/-- Two mutually inverse affine maps of the line that both preserve `[-1, 1]` are `±` the
identity. -/
theorem bit_aux {a b c d : ℝ} (h1 : -1 ≤ a + b * 1 ∧ a + b * 1 ≤ 1)
    (h2 : -1 ≤ a + b * -1 ∧ a + b * -1 ≤ 1) (h3 : -1 ≤ c + d * 1 ∧ c + d * 1 ≤ 1)
    (h4 : -1 ≤ c + d * -1 ∧ c + d * -1 ≤ 1) (h5 : a + b * (c + d * 0) = 0)
    (h6 : a + b * (c + d * 1) = 1) : a = 0 ∧ b * b = 1 := by
  obtain ⟨h1l, h1u⟩ := h1
  obtain ⟨h2l, h2u⟩ := h2
  obtain ⟨h3l, h3u⟩ := h3
  obtain ⟨h4l, h4u⟩ := h4
  have hbd : b * d = 1 := by linear_combination h6 - h5
  have hab : a ^ 2 + b ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (a + b)) (by linarith : (0 : ℝ) ≤ 1 + (a + b)),
      mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (a - b)) (by linarith : (0 : ℝ) ≤ 1 + (a - b))]
  have hcd : c ^ 2 + d ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (c + d)) (by linarith : (0 : ℝ) ≤ 1 + (c + d)),
      mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (c - d)) (by linarith : (0 : ℝ) ≤ 1 + (c - d))]
  have hbd2 : b ^ 2 * d ^ 2 = 1 := by rw [← mul_pow, hbd]; norm_num
  have hb : 1 ≤ b ^ 2 := by
    nlinarith [mul_nonneg (sq_nonneg b) (by nlinarith [sq_nonneg c] : (0 : ℝ) ≤ 1 - d ^ 2)]
  have ha2 : a ^ 2 ≤ 0 := by linarith
  have ha : a = 0 := (pow_eq_zero_iff two_ne_zero).mp (le_antisymm ha2 (sq_nonneg a))
  exact ⟨ha, by nlinarith [sq_nonneg a]⟩

/-- **Negative control for drivability.** The classical bit `[-1, 1]` is not drivable: the flow
member at half the NOT's parameter is `±` the identity on the line, so the NOT, its square, is
the identity and moves nothing. -/
theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) := by
  refine ⟨fun D => ?_⟩
  obtain ⟨x, -, hmove⟩ := D.N_moves
  have hinv : ∀ y, D.flow (D.t₀ / 2) (D.flow (-(D.t₀ / 2)) y) = y := by
    intro y
    have h1 := congrArg (fun f : ℝ ≃ᵃ[ℝ] ℝ => f y) (D.flow_add (D.t₀ / 2) (-(D.t₀ / 2)))
    simp only [AffineEquiv.trans_apply, add_neg_cancel, D.flow_zero,
      AffineEquiv.refl_apply] at h1
    exact h1.symm
  have hsq : D.flow D.t₀ x = D.flow (D.t₀ / 2) (D.flow (D.t₀ / 2) x) := by
    have h1 := congrArg (fun f : ℝ ≃ᵃ[ℝ] ℝ => f x) (D.flow_add (D.t₀ / 2) (D.t₀ / 2))
    simp only [AffineEquiv.trans_apply, add_halves] at h1
    exact h1
  have hp : (1 : ℝ) ∈ Set.Icc (-1 : ℝ) 1 := ⟨by norm_num, le_rfl⟩
  have hm : (-1 : ℝ) ∈ Set.Icc (-1 : ℝ) 1 := ⟨le_rfl, by norm_num⟩
  have hh := affineEquiv_real_apply (D.flow (D.t₀ / 2))
  have hk := affineEquiv_real_apply (D.flow (-(D.t₀ / 2)))
  have e1 := D.flow_preserves (D.t₀ / 2) 1 hp
  have e2 := D.flow_preserves (D.t₀ / 2) (-1) hm
  have e3 := D.flow_preserves (-(D.t₀ / 2)) 1 hp
  have e4 := D.flow_preserves (-(D.t₀ / 2)) (-1) hm
  have i0 := hinv 0
  have i1 := hinv 1
  rw [hh 1, Set.mem_Icc] at e1
  rw [hh (-1), Set.mem_Icc] at e2
  rw [hk 1, Set.mem_Icc] at e3
  rw [hk (-1), Set.mem_Icc] at e4
  rw [hk 0, hh] at i0
  rw [hk 1, hh] at i1
  obtain ⟨ha, hb⟩ := bit_aux e1 e2 e3 e4 i0 i1
  apply hmove
  rw [hsq, hh (D.flow (D.t₀ / 2) x), hh x, ha]
  linear_combination x * hb

/-- A one-point body is not drivable: nothing on it can move. -/
theorem not_drivable_singleton (x : V) : IsEmpty (ElementaryDrivability ({x} : Set V)) := by
  refine ⟨fun D => ?_⟩
  obtain ⟨y, hy, hmove⟩ := D.N_moves
  rw [Set.mem_singleton_iff] at hy
  subst hy
  exact hmove (D.flow_preserves D.t₀ y (Set.mem_singleton y))

