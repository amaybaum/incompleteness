/-
  RelcSelectSqueeze.lean — design module for round RELC-SELECT-1.
  UNBUILT: written without a Lean toolchain against the landed sources at L = e2426ba4. Every
  declaration is intended to compile as written; nothing here has been checked by the kernel.

  The squeezed gate at `d = 5`. With the landed NOT `n5` and axis `z5` on `eball 5`, the gate
  `gSq = G_ε ∘ (I ⊗ K_λ)` (`ε = 1/10`, `λ = 1/2`) is a linear equivalence of `W 5` with the frame,
  the target and the control relation and forward positivity on product states, and without inverse
  positivity (`gSq_sep`). Its inverse has the frame, both relations and inverse positivity, and not
  forward positivity (`gSqInv_sep`). Neither is a `NativeGate` (`not_nativeGate_gSq`,
  `not_nativeGate_gSqInv`).

  §A  Transfer of the frame and the two relations from `G` to `G.symm`, for every `d`, `N`, `G`
      with `IsNot` (`frame_symm`, `relT_symm`, `relC_symm_of_relT`, `gateRel_symm`).
  §B  The gate as a weighted involutive index permutation: entry `(m, n)` of `gSq ω` is
      `sqW m n * ω (sqPc m n) (sqPt m n)`; the inverse has weights `sqWi`.
  §C  Frame and relations.
  §D  Forward positivity. The pairing of two cone vectors with the image of a product state is
      the decomposition `pairVal_gSq_prodState`; its nonnegativity is `gSq_core`, assembled from
      five real-variable lemmas (`rsq_cs4`, `rsq_ab`, `rsq_s`, `rsq_key`, `rsq_assemble`).
  §E  Inverse positivity fails: an exact value `−1/2` with two sharp effects (`gSq_symm_value`).
  §F  Packaged statements.
-/
import OIBridge.OddChar

namespace OIBridge
namespace RelcSelect

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot

variable {d : ℕ}

/-! ### §A — the frame and the relations transfer to the inverse -/

theorem add_add_fin2 : ∀ a b : Fin 2, a + (a + b) = b := by decide

/-- The frame of `G` gives the frame of `G.symm`. -/
theorem frame_symm {z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d}
    (hF : ∀ a b : Fin 2,
      G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) :
    ∀ a b : Fin 2,
      G.symm (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)) := by
  intro a b
  have h := hF a (a + b)
  rw [add_add_fin2] at h
  rw [← h, G.symm_apply_apply]

/-- The target relation of `G` gives the target relation of `G.symm`. -/
theorem relT_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω) :
    ∀ ω, actT N (G.symm (actT N ω)) = G.symm ω := by
  have hc : ∀ ω, G (actT N ω) = actT N (G ω) := fun ω => by
    have h := hT (actT N ω)
    rw [actT_actT hN.invol] at h
    exact h.symm
  intro ω
  apply G.injective
  rw [hc, G.apply_symm_apply, G.apply_symm_apply, actT_actT hN.invol]

/-- The target and the control relation of `G` give the control relation of `G.symm`. -/
theorem relC_symm_of_relT {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :
    ∀ ω, actC N (G.symm (actC N ω)) = actT N (G.symm ω) := by
  have hc : ∀ ω, G (actT N ω) = actT N (G ω) := fun ω => by
    have h := hT (actT N ω)
    rw [actT_actT hN.invol] at h
    exact h.symm
  have hc' : ∀ ω, G (actC N ω) = actC N (actT N (G ω)) := fun ω => by
    have h := congrArg (actC N) (hC ω)
    rwa [actC_actC hN.invol] at h
  intro ω
  have key : G.symm (actC N ω) = actC N (actT N (G.symm ω)) := by
    apply G.injective
    rw [G.apply_symm_apply, hc', hc, G.apply_symm_apply, actT_actT hN.invol]
  rw [key, actC_actC hN.invol]

theorem gateRel_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hR : GateRel N G) : GateRel N G.symm :=
  ⟨relT_symm hN hR.relT, relC_symm_of_relT hN hR.relT hR.relC⟩

/-! ### §B — the squeezed gate at `d = 5` -/

/-- The classical control indices: `0` (the unit) and `5` (the corner axis). -/
def sqCls : Fin 6 → Bool
  | 0 => true | 1 => false | 2 => false | 3 => false | 4 => false | 5 => true

/-- The target relabelling of the tangent rows: `0 ↔ 1`, `3 ↔ 5`. It preserves `odd5`. -/
def sqSig : Fin 6 → Fin 6
  | 0 => 1 | 1 => 0 | 2 => 2 | 3 => 5 | 4 => 4 | 5 => 3

/-- The control index read at `(m, n)`: `perm5 m` on the target-odd columns. -/
def sqPc (m n : Fin 6) : Fin 6 := if odd5 n then perm5 m else m

/-- The target index read at `(m, n)`: `n` on the classical rows, `sqSig n` on the tangent rows. -/
def sqPt (m n : Fin 6) : Fin 6 := if sqCls m then n else sqSig n

/-- The row weight `ε = 1/10` of the tangent rows. -/
noncomputable def sqR (m : Fin 6) : ℝ := if sqCls m then 1 else 1 / 10

/-- The squeeze `K_λ`, `λ = 1/2`, on the tangent target indices. -/
noncomputable def sqK (n : Fin 6) : ℝ := if sqCls n then 1 else 1 / 2

noncomputable def sqW (m n : Fin 6) : ℝ := sqR m * sqK (sqPt m n)

noncomputable def sqWi (m n : Fin 6) : ℝ := (if sqCls m then 1 else 10) * (if sqCls n then 1 else 2)

/-- The squeezed gate as a function. -/
noncomputable def gSqFun (ω : W 5) : W 5 := fun m n => sqW m n * ω (sqPc m n) (sqPt m n)

/-- Its inverse as a function. -/
noncomputable def gSqInvFun (ω : W 5) : W 5 := fun m n => sqWi m n * ω (sqPc m n) (sqPt m n)

theorem gSqFun_apply (ω : W 5) (m n : Fin 6) :
    gSqFun ω m n = sqW m n * ω (sqPc m n) (sqPt m n) := rfl

theorem gSqInvFun_apply (ω : W 5) (m n : Fin 6) :
    gSqInvFun ω m n = sqWi m n * ω (sqPc m n) (sqPt m n) := rfl

theorem sqPc_sqPc : ∀ m n : Fin 6, sqPc (sqPc m n) (sqPt m n) = m := by decide

theorem sqPt_sqPt : ∀ m n : Fin 6, sqPt (sqPc m n) (sqPt m n) = n := by decide

theorem sqCls_sqPc : ∀ m n : Fin 6, sqCls (sqPc m n) = sqCls m := by decide

theorem odd5_sqPt : ∀ m n : Fin 6, odd5 (sqPt m n) = odd5 n := by decide

theorem odd5_sqPc : ∀ m n : Fin 6, odd5 (sqPc m n) = (if odd5 n then !odd5 m else odd5 m) := by
  decide

theorem sqWi_sqW (m n : Fin 6) : sqWi m n * sqW (sqPc m n) (sqPt m n) = 1 := by
  have h1 := sqCls_sqPc m n
  have h2 := sqPt_sqPt m n
  simp only [sqW, sqWi, sqR, sqK, h1, h2]
  split_ifs <;> norm_num

theorem sqW_sqWi (m n : Fin 6) : sqW m n * sqWi (sqPc m n) (sqPt m n) = 1 := by
  have h1 := sqCls_sqPc m n
  simp only [sqW, sqWi, sqR, sqK, h1]
  split_ifs <;> norm_num

theorem gSqInvFun_gSqFun (ω : W 5) : gSqInvFun (gSqFun ω) = ω := by
  funext m n
  rw [gSqInvFun_apply, gSqFun_apply, sqPc_sqPc, sqPt_sqPt, ← mul_assoc, sqWi_sqW, one_mul]

theorem gSqFun_gSqInvFun (ω : W 5) : gSqFun (gSqInvFun ω) = ω := by
  funext m n
  rw [gSqFun_apply, gSqInvFun_apply, sqPc_sqPc, sqPt_sqPt, ← mul_assoc, sqW_sqWi, one_mul]

/-- **The squeezed gate** `G_ε ∘ (I ⊗ K_λ)` at `d = 5`, `ε = 1/10`, `λ = 1/2`. -/
noncomputable def gSq : W 5 ≃ₗ[ℝ] W 5 where
  toFun := gSqFun
  invFun := gSqInvFun
  map_add' ω₁ ω₂ := by
    funext m n
    simp only [gSqFun_apply, Pi.add_apply, mul_add]
  map_smul' c ω := by
    funext m n
    simp only [gSqFun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring
  left_inv := gSqInvFun_gSqFun
  right_inv := gSqFun_gSqInvFun

theorem gSq_apply (ω : W 5) : gSq ω = gSqFun ω := rfl

theorem gSq_symm_apply (ω : W 5) : gSq.symm ω = gSqInvFun ω := rfl

/-! ### §C — the frame and the relations -/

theorem gSq_frame (a b : Fin 2) :
    gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [gSq_apply, gSqFun_apply, sqW, sqR, sqK, sqPc, sqPt, sqSig, perm5,
      prodState_apply, corner_zero, corner_one, z5]

/-- The signs of the homogenized `n5`. -/
noncomputable def sqSg (μ : Fin 6) : ℝ := if odd5 μ then -1 else 1

theorem homMap_n5_sqSg (v : HVec 5) (μ : Fin (5 + 1)) : homMap n5 v μ = sqSg μ * v μ :=
  homMap_n5_sign v μ

theorem sqSg_sq (μ : Fin 6) : sqSg μ * sqSg μ = 1 := by
  unfold sqSg
  split_ifs <;> norm_num

theorem sqSg_sqPt (m n : Fin 6) : sqSg (sqPt m n) = sqSg n := by
  simp only [sqSg, odd5_sqPt]

theorem sqSg_sqPc (m n : Fin 6) : sqSg (sqPc m n) = sqSg m * sqSg n := by
  simp only [sqSg, odd5_sqPc]
  cases odd5 m <;> cases odd5 n <;> norm_num

theorem gSq_relT : ∀ ω, actT n5 (gSq (actT n5 ω)) = gSq ω := by
  intro ω
  funext m n
  simp only [actT_apply, homMap_n5_sqSg, gSq_apply, gSqFun_apply]
  linear_combination (sqSg n * sqW m n * ω (sqPc m n) (sqPt m n)) * sqSg_sqPt m n
    + (sqW m n * ω (sqPc m n) (sqPt m n)) * sqSg_sq n

theorem gSq_relC : ∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω) := by
  intro ω
  funext m n
  simp only [actC_apply, actT_apply, homMap_n5_sqSg, gSq_apply, gSqFun_apply]
  linear_combination (sqSg m * sqW m n * ω (sqPc m n) (sqPt m n)) * sqSg_sqPc m n
    + (sqSg n * sqW m n * ω (sqPc m n) (sqPt m n)) * sqSg_sq m

theorem gateRel_gSq : GateRel n5 gSq := ⟨gSq_relT, gSq_relC⟩

/-! ### §D — forward positivity -/

/-- Cauchy–Schwarz in four variables. -/
theorem rsq_cs4 (p1 p2 p3 p4 q1 q2 q3 q4 : ℝ) :
    (p1 * q1 + p2 * q2 + p3 * q3 + p4 * q4) ^ 2
      ≤ (p1 ^ 2 + p2 ^ 2 + p3 ^ 2 + p4 ^ 2) * (q1 ^ 2 + q2 ^ 2 + q3 ^ 2 + q4 ^ 2) := by
  linarith [sq_nonneg (p1 * q2 - p2 * q1), sq_nonneg (p1 * q3 - p3 * q1),
    sq_nonneg (p1 * q4 - p4 * q1), sq_nonneg (p2 * q3 - p3 * q2),
    sq_nonneg (p2 * q4 - p4 * q2), sq_nonneg (p3 * q4 - p4 * q3)]

/-- The lower bound on the two target pairings. With `f` the head of a cone vector, `t` the norm
of its tangent part, `s` the norm of the tangent part of a ball point and `u` the product of the
two axis coordinates, `A, B ≥ f ± u − ts/2` give `A, B ≥ 0` and `AB ≥ (t² + f²s²)/8`. -/
theorem rsq_ab (f t s u A B : ℝ) (hf : 0 ≤ f) (ht : 0 ≤ t) (hs : 0 ≤ s) (htf : t ≤ f)
    (hs1 : s ≤ 1) (hu : u ^ 2 ≤ (f ^ 2 - t ^ 2) * (1 - s ^ 2))
    (hA : f + u - t * s / 2 ≤ A) (hB : f - u - t * s / 2 ≤ B) :
    0 ≤ A ∧ 0 ≤ B ∧ (t ^ 2 + f ^ 2 * s ^ 2) / 8 ≤ A * B := by
  have hts : 0 ≤ t * s := mul_nonneg ht hs
  have hts1 : t * s ≤ t * 1 := mul_le_mul_of_nonneg_left hs1 ht
  have hfts : 0 ≤ f - t * s := by linarith
  have hu2 : u ^ 2 ≤ (f - t * s) ^ 2 := by linarith [sq_nonneg (f * s - t)]
  have hu' := abs_le_of_sq_le_sq' hu2 hfts
  have hL1 : 0 ≤ f + u - t * s / 2 := by linarith [hu'.1]
  have hL2 : 0 ≤ f - u - t * s / 2 := by linarith [hu'.2]
  have hA0 : 0 ≤ A := le_trans hL1 hA
  have hB0 : 0 ≤ B := le_trans hL2 hB
  have hprod : (f + u - t * s / 2) * (f - u - t * s / 2) ≤ A * B := mul_le_mul hA hB hL2 hA0
  have hs2 : 0 ≤ 1 - s ^ 2 := by nlinarith [mul_nonneg hs (sub_nonneg.mpr hs1)]
  have ht2 : 0 ≤ f ^ 2 - t ^ 2 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr htf) (add_nonneg hf ht)]
  have h2 : 0 ≤ t ^ 2 * (1 - s ^ 2) := mul_nonneg (sq_nonneg t) hs2
  have h3 : 0 ≤ s ^ 2 * (f ^ 2 - t ^ 2) := mul_nonneg (sq_nonneg s) ht2
  refine ⟨hA0, hB0, ?_⟩
  linarith [sq_nonneg (t - f * s)]

/-- The upper bound on the two tangent-row target sums `S_e`, `S_o`. -/
theorem rsq_s (f b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 : ℝ)
    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ f ^ 2)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :
    (b1 + (f * y0 + b2 * y1) / 2) ^ 2 + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) ^ 2
      ≤ 2 * (b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2) + f ^ 2 * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2) := by
  have hy4 : 0 ≤ 1 - y4 ^ 2 := by
    linarith [sq_nonneg y0, sq_nonneg y1, sq_nonneg y2, sq_nonneg y3]
  have hfb2 : 0 ≤ f ^ 2 - b2 ^ 2 := by
    linarith [sq_nonneg b1, sq_nonneg b3, sq_nonneg b4, sq_nonneg b5]
  have hfb54 : 0 ≤ f ^ 2 - b5 ^ 2 - b4 ^ 2 := by
    linarith [sq_nonneg b1, sq_nonneg b2, sq_nonneg b3]
  have h01 : 0 ≤ y0 ^ 2 + y1 ^ 2 := by positivity
  have h23 : 0 ≤ y2 ^ 2 + y3 ^ 2 := by positivity
  linarith [sq_nonneg (b1 - (f * y0 + b2 * y1) / 2), sq_nonneg (b3 * y4 - (b5 * y2 + b4 * y3) / 2),
    sq_nonneg (f * y1 - b2 * y0), sq_nonneg (b5 * y3 - b4 * y2),
    mul_nonneg (sq_nonneg b3) hy4, mul_nonneg hfb2 h01, mul_nonneg hfb54 h23,
    mul_nonneg (sq_nonneg f) h23, sq_nonneg b2, sq_nonneg b4]

/-- **The key lemma** (squared form): for a cone vector `b` and a ball point `y`, the two target
pairings `A`, `B` are nonnegative and `2 ε² (S_e² + S_o²) ≤ A B` at `ε = 1/10`. -/
theorem rsq_key (b0 b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 : ℝ) (hb0 : 0 ≤ b0)
    (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ b0 ^ 2)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :
    0 ≤ b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2
      ∧ 0 ≤ b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2
      ∧ ((b1 + (b0 * y0 + b2 * y1) / 2) ^ 2 + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) ^ 2) / 50
        ≤ (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2)
          * (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2) := by
  obtain ⟨t, ht0, ht2⟩ : ∃ t : ℝ, 0 ≤ t ∧ t ^ 2 = b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 :=
    ⟨Real.sqrt _, Real.sqrt_nonneg _, Real.sq_sqrt (by positivity)⟩
  obtain ⟨s, hs0, hs2⟩ : ∃ s : ℝ, 0 ≤ s ∧ s ^ 2 = y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 :=
    ⟨Real.sqrt _, Real.sqrt_nonneg _, Real.sq_sqrt (by positivity)⟩
  have htf : t ≤ b0 :=
    (abs_le_of_sq_le_sq' (by linarith [sq_nonneg b5] : t ^ 2 ≤ b0 ^ 2) hb0).2
  have hs1 : s ≤ 1 :=
    (abs_le_of_sq_le_sq' (by linarith [sq_nonneg y4] : s ^ 2 ≤ 1 ^ 2) zero_le_one).2
  have hu : (b5 * y4) ^ 2 ≤ (b0 ^ 2 - t ^ 2) * (1 - s ^ 2) := by
    rw [mul_pow]
    exact mul_le_mul (by linarith) (by linarith) (sq_nonneg _) (by linarith [sq_nonneg b5])
  have hts : 0 ≤ t * s := mul_nonneg ht0 hs0
  have hts2 : (t * s) ^ 2
      = (b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2) * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2) := by
    rw [mul_pow, ht2, hs2]
  have hr1 : (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) ^ 2 ≤ (t * s) ^ 2 := by
    rw [hts2]
    exact rsq_cs4 b1 b2 b3 b4 y0 y1 y2 y3
  have hr2 : (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) ^ 2 ≤ (t * s) ^ 2 := by
    rw [hts2]
    linarith [rsq_cs4 b1 b2 b3 b4 y0 y1 (-y2) (-y3)]
  have hr1' := abs_le_of_sq_le_sq' hr1 hts
  have hr2' := abs_le_of_sq_le_sq' hr2 hts
  obtain ⟨hA0, hB0, hAB⟩ := rsq_ab b0 t s (b5 * y4)
    (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2)
    (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2)
    hb0 ht0 hs0 htf hs1 hu (by linarith [hr1'.1]) (by linarith [hr2'.1])
  refine ⟨hA0, hB0, ?_⟩
  have hS := rsq_s b0 b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 hb hy
  have hfs : b0 ^ 2 * s ^ 2 = b0 ^ 2 * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2) := by rw [hs2]
  have hF : 0 ≤ b0 ^ 2 * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2) := by positivity
  have hT : 0 ≤ b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 := by positivity
  linarith

/-- The assembly: AM–GM on the two classical terms, Cauchy–Schwarz on the tangent term, the key
lemma, and `P ≥ 0 ∧ E² ≤ P² ⇒ P + E ≥ 0`. -/
theorem rsq_assemble (α p q A B Se So Ce Co Tc Ta : ℝ) (h1 : 0 ≤ 1 + α) (h2 : 0 ≤ 1 - α)
    (hp : 0 ≤ p) (hq : 0 ≤ q) (hA : 0 ≤ A) (hB : 0 ≤ B) (hTc0 : 0 ≤ Tc) (hTa0 : 0 ≤ Ta)
    (hTc : Tc ≤ 1 - α ^ 2) (hTa : Ta ≤ p * q) (hCe : Ce ^ 2 ≤ Tc * Ta) (hCo : Co ^ 2 ≤ Tc * Ta)
    (hkey : (Se ^ 2 + So ^ 2) / 50 ≤ A * B) :
    0 ≤ (1 + α) / 2 * (p * A) + (1 - α) / 2 * (q * B) + (Se * Ce + So * Co) / 10 := by
  have hP1 : 0 ≤ (1 + α) / 2 * (p * A) := mul_nonneg (by linarith) (mul_nonneg hp hA)
  have hP2 : 0 ≤ (1 - α) / 2 * (q * B) := mul_nonneg (by linarith) (mul_nonneg hq hB)
  have hα : 0 ≤ 1 - α ^ 2 := le_trans hTc0 hTc
  have hTT : Tc * Ta ≤ (1 - α ^ 2) * (p * q) := mul_le_mul hTc hTa hTa0 hα
  have hAB0 : 0 ≤ A * B := mul_nonneg hA hB
  have h4 : Tc * Ta * (A * B) ≤ (1 - α ^ 2) * (p * q) * (A * B) :=
    mul_le_mul_of_nonneg_right hTT hAB0
  have hAM : (1 - α ^ 2) * (p * q) * (A * B)
      ≤ ((1 + α) / 2 * (p * A) + (1 - α) / 2 * (q * B)) ^ 2 := by
    linarith [sq_nonneg ((1 + α) / 2 * (p * A) - (1 - α) / 2 * (q * B))]
  have hCS : (Se * Ce + So * Co) ^ 2 ≤ (Se ^ 2 + So ^ 2) * (Ce ^ 2 + Co ^ 2) := by
    linarith [sq_nonneg (Se * Co - So * Ce)]
  have hS0 : 0 ≤ Se ^ 2 + So ^ 2 := by positivity
  have h5 : (Se ^ 2 + So ^ 2) * (Ce ^ 2 + Co ^ 2) ≤ (Se ^ 2 + So ^ 2) * (2 * (Tc * Ta)) :=
    mul_le_mul_of_nonneg_left (by linarith) hS0
  have h6 : (Se ^ 2 + So ^ 2) / 50 * (Tc * Ta) ≤ A * B * (Tc * Ta) :=
    mul_le_mul_of_nonneg_right hkey (mul_nonneg hTc0 hTa0)
  have hE : ((Se * Ce + So * Co) / 10) ^ 2
      ≤ ((1 + α) / 2 * (p * A) + (1 - α) / 2 * (q * B)) ^ 2 := by
    linarith
  have hlow := (abs_le_of_sq_le_sq' hE (add_nonneg hP1 hP2)).1
  linarith

/-- The core inequality in coordinates: `a`, `b` cone vectors, `x`, `y` ball points. -/
theorem gSq_core (a0 a1 a2 a3 a4 a5 b0 b1 b2 b3 b4 b5 x0 x1 x2 x3 x4 y0 y1 y2 y3 y4 : ℝ)
    (ha0 : 0 ≤ a0) (ha : a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2 + a5 ^ 2 ≤ a0 ^ 2)
    (hb0 : 0 ≤ b0) (hb : b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2 + b5 ^ 2 ≤ b0 ^ 2)
    (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 ≤ 1)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :
    0 ≤ (1 + x4) / 2 * ((a0 + a5) * (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2))
      + (1 - x4) / 2 * ((a0 - a5) * (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2))
      + ((b1 + (b0 * y0 + b2 * y1) / 2) * (x0 * a1 + x1 * a2 + x2 * a3 + x3 * a4)
        + (b3 * y4 + (b5 * y2 + b4 * y3) / 2) * (x0 * a3 + x1 * a4 + x2 * a1 + x3 * a2)) / 10 := by
  obtain ⟨hA, hB, hkey⟩ := rsq_key b0 b1 b2 b3 b4 b5 y0 y1 y2 y3 y4 hb0 hb hy
  have hx4 := abs_le_of_sq_le_sq'
    (by linarith [sq_nonneg x0, sq_nonneg x1, sq_nonneg x2, sq_nonneg x3] : x4 ^ 2 ≤ 1 ^ 2)
    zero_le_one
  have ha5 := abs_le_of_sq_le_sq'
    (by linarith [sq_nonneg a1, sq_nonneg a2, sq_nonneg a3, sq_nonneg a4] : a5 ^ 2 ≤ a0 ^ 2) ha0
  have hCe := rsq_cs4 x0 x1 x2 x3 a1 a2 a3 a4
  have hCo : (x0 * a3 + x1 * a4 + x2 * a1 + x3 * a2) ^ 2
      ≤ (x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2) * (a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2) := by
    linarith [rsq_cs4 x0 x1 x2 x3 a3 a4 a1 a2]
  have h := rsq_assemble x4 (a0 + a5) (a0 - a5)
    (b0 + b5 * y4 + (b1 * y0 + b2 * y1 + b3 * y2 + b4 * y3) / 2)
    (b0 - b5 * y4 + (b1 * y0 + b2 * y1 - b3 * y2 - b4 * y3) / 2)
    (b1 + (b0 * y0 + b2 * y1) / 2) (b3 * y4 + (b5 * y2 + b4 * y3) / 2)
    (x0 * a1 + x1 * a2 + x2 * a3 + x3 * a4) (x0 * a3 + x1 * a4 + x2 * a1 + x3 * a2)
    (x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2) (a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2)
    (by linarith [hx4.1]) (by linarith [hx4.2]) (by linarith [ha5.1]) (by linarith [ha5.2])
    hA hB (by positivity) (by positivity) (by linarith) (by linarith) hCe hCo hkey
  exact h

/-- The pairing of two vectors with the image of a product state: the decomposition identity. -/
theorem pairVal_gSq_prodState (a b : HVec 5) (x y : Fin 5 → ℝ) :
    pairVal a b (gSq (prodState x y))
      = (1 + x 4) / 2
          * ((a 0 + a 5) * (b 0 + b 5 * y 4 + (b 1 * y 0 + b 2 * y 1 + b 3 * y 2 + b 4 * y 3) / 2))
        + (1 - x 4) / 2
          * ((a 0 - a 5) * (b 0 - b 5 * y 4 + (b 1 * y 0 + b 2 * y 1 - b 3 * y 2 - b 4 * y 3) / 2))
        + ((b 1 + (b 0 * y 0 + b 2 * y 1) / 2) * (x 0 * a 1 + x 1 * a 2 + x 2 * a 3 + x 3 * a 4)
          + (b 3 * y 4 + (b 5 * y 2 + b 4 * y 3) / 2)
            * (x 0 * a 3 + x 1 * a 4 + x 2 * a 1 + x 3 * a 2)) / 10 := by
  -- Primary: evaluate the 36 entries on the left only, so that simp never rewrites the
  -- right-hand side (e.g. by cancelling common summands); then `ring`. Fallback: DIM-1's
  -- `prodEffVal_cnot_prodState` pattern.
  conv_lhs =>
    simp only [pairVal, gSq_apply, gSqFun_apply, prodState_apply, sum_univ_six']
    simp +decide [sqW, sqR, sqK, sqPc, sqPt, sqCls, sqSig, perm5, odd5]
  ring

theorem lor_five {v : HVec 5} (hv : Lor v) :
    0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2 + v 5 ^ 2 ≤ v 0 ^ 2 := by
  obtain ⟨h0, h⟩ := hv
  rw [Fin.sum_univ_five] at h
  exact ⟨h0, h⟩

theorem gSq_pairVal_nonneg {a b : HVec 5} (ha : Lor a) (hb : Lor b) {x y : Fin 5 → ℝ}
    (hx : x ∈ eball 5) (hy : y ∈ eball 5) : 0 ≤ pairVal a b (gSq (prodState x y)) := by
  obtain ⟨ha0, ha'⟩ := lor_five ha
  obtain ⟨hb0, hb'⟩ := lor_five hb
  rw [mem_eball, Fin.sum_univ_five] at hx hy
  rw [pairVal_gSq_prodState]
  exact gSq_core (a 0) (a 1) (a 2) (a 3) (a 4) (a 5) (b 0) (b 1) (b 2) (b 3) (b 4) (b 5)
    (x 0) (x 1) (x 2) (x 3) (x 4) (y 0) (y 1) (y 2) (y 3) (y 4) ha0 ha' hb0 hb' hx hy

/-- **Forward positivity** of the squeezed gate on product states of the ball. -/
theorem gSq_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5) := by
  intro x hx y hy
  show ∀ e f, IsEffectOn (eball 5) e → IsEffectOn (eball 5) f →
    0 ≤ prodEffVal e f (gSq (prodState x y))
  intro e f he hf
  exact gSq_pairVal_nonneg (lor_ehom he) (lor_ehom hf) hx hy

/-! ### §E — inverse positivity fails -/

theorem x5_unit : ∑ j, x5 j ^ 2 = 1 := by
  rw [Fin.sum_univ_five]
  simp [x5]

theorem negx5_unit : ∑ j, (-x5) j ^ 2 = 1 := by
  rw [sum_neg_sq]
  exact x5_unit

theorem sharpVec_negx5 : sharpVec (-x5) = fun μ : Fin (5 + 1) =>
    if μ = 0 then 1 / 2 else if μ = 1 then -1 / 2 else 0 := by
  funext i
  fin_cases i
  · rfl
  · show -x5 0 / 2 = -1 / 2
    simp [x5]
  · show -x5 1 / 2 = 0
    simp [x5]
  · show -x5 2 / 2 = 0
    simp [x5]
  · show -x5 3 / 2 = 0
    simp [x5]
  · show -x5 4 / 2 = 0
    simp [x5]

/-- The image under the inverse of the product of the corner with the first axis pairs to `−1/2`
with the sharp effects of the corner and of the negated first axis. -/
theorem gSq_symm_value :
    prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2 := by
  rw [prodEffVal_sharp, sharpVec_z5, sharpVec_negx5]
  simp +decide [pairVal, sum_univ_six', gSq_symm_apply, gSqInvFun_apply, sqWi, sqPc, sqPt, sqCls,
    sqSig, perm5, odd5, prodState_apply, x5, z5]
  norm_num

theorem gSq_symm_not_mem_maxCone : gSq.symm (prodState z5 x5) ∉ maxCone (eball 5) := fun h => by
  have hv := h _ _ (sharpEff_isEffectOn z5_unit) (sharpEff_isEffectOn negx5_unit)
  rw [gSq_symm_value] at hv
  norm_num at hv

/-- **Inverse positivity fails.** -/
theorem gSq_not_posInv :
    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5) :=
  fun h => gSq_symm_not_mem_maxCone (h _ z5_mem _ x5_mem)

/-! ### §F — the packaged statements -/

theorem not_nativeGate_gSq : ¬ NativeGate (eball 5) z5 n5 gSq :=
  fun hG => gSq_not_posInv hG.posInv

theorem not_nativeGate_gSqInv : ¬ NativeGate (eball 5) z5 n5 gSq.symm :=
  fun hG => gSq_not_posInv hG.posFwd

/-- **Forward positivity does not imply inverse positivity** under the NOT, the frame and the two
relations at `d = 5`. -/
theorem gSq_sep :
    IsNot (eball 5) z5 n5
      ∧ (∀ a b : Fin 2,
          gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)))
      ∧ GateRel n5 gSq
      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))
      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=
  ⟨isNot_n5, gSq_frame, gateRel_gSq, gSq_posFwd, gSq_not_posInv⟩

/-- **Inverse positivity does not imply forward positivity** under the NOT, the frame and the two
relations at `d = 5`: the inverse of the squeezed gate. -/
theorem gSqInv_sep :
    IsNot (eball 5) z5 n5
      ∧ (∀ a b : Fin 2,
          gSq.symm (prodState (corner z5 a) (corner z5 b))
            = prodState (corner z5 a) (corner z5 (a + b)))
      ∧ GateRel n5 gSq.symm
      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))
      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=
  ⟨isNot_n5, frame_symm gSq_frame, gateRel_symm isNot_n5 gateRel_gSq, gSq_posFwd, gSq_not_posInv⟩

end RelcSelect
end OIBridge

#print axioms OIBridge.RelcSelect.frame_symm
#print axioms OIBridge.RelcSelect.relT_symm
#print axioms OIBridge.RelcSelect.relC_symm_of_relT
#print axioms OIBridge.RelcSelect.gateRel_symm
#print axioms OIBridge.RelcSelect.gSq_frame
#print axioms OIBridge.RelcSelect.gateRel_gSq
#print axioms OIBridge.RelcSelect.pairVal_gSq_prodState
#print axioms OIBridge.RelcSelect.gSq_core
#print axioms OIBridge.RelcSelect.gSq_posFwd
#print axioms OIBridge.RelcSelect.gSq_symm_value
#print axioms OIBridge.RelcSelect.gSq_not_posInv
#print axioms OIBridge.RelcSelect.not_nativeGate_gSq
#print axioms OIBridge.RelcSelect.not_nativeGate_gSqInv
#print axioms OIBridge.RelcSelect.gSq_sep
#print axioms OIBridge.RelcSelect.gSqInv_sep
