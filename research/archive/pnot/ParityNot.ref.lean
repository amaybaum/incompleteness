/-
  OIBridge/ParityNot.lean — round PARITY-NOT-1: DIM-1's parity count from the target and control
  relations alone, the NOT the relations force at `d = 3`, and forward positivity as a separate
  condition on the gate.

  `GateRel N G` is the target relation and the control relation of DIM-1's `NativeGate`, with
  neither the frame nor positivity.

  (A) Parity. With `IsNot (eball d) z N` and `GateRel N G`, the `+1` and `−1` eigenspaces of the
  homogenized NOT have equal dimension (`finrank_plus_eq_finrank_minus_rel`), so `d` is odd
  (`not_even_of_gateRel`). DIM-1's parity argument reads the two relations and nothing else.

  (B) The NOT at `d = 3`. With `IsNot (eball 3) z N` and `GateRel N G`, both eigenspaces have
  dimension two, the fixed space of `N` has dimension one (`tangentPlus_three`), `N` is the rotation
  by `π` about a unit axis, `N x = 2 (u · x) u − x` (`piRotation_three`), and `det N = 1`
  (`det_three`). The reflection `diag(1, 1, −1)` and `−id` are NOTs of `eball 3` with axis `z3` for
  which no gate satisfies the relations (`not_gateRel_refl3`, `not_gateRel_negId3`); both have
  determinant `−1`. DIM-1's `cnot` with `nflip` satisfies them (`gateRel_cnot`).

  (C) Positivity. The permutation gates `gJ3` (with `nflip` on `eball 3`) and `gJ5` (with
  `n5 = diag(1, 1, −1, −1, −1)` on `eball 5`) satisfy the frame and both relations. At each, the
  image of the product of the first axis with the corner pairs to `−1/10` with two sharp effects
  (`gJ3_value`, `gJ5_value`), so forward positivity fails (`not_posFwd_gJ3`, `not_posFwd_gJ5`). At
  `d = 5` the eigenspaces of `n5` are balanced (`finrank_plus_eq_finrank_minus_n5`).

  The statements concern the two relations, the frame and forward positivity of the gates named
  here. None of them selects a dimension, and none concerns a complex structure or the NOT of a
  physical theory.
-/
import OIBridge.EffectSpace

namespace OIBridge
namespace ParityNot

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace Finset

variable {d : ℕ}

/-! ### §A — parity from the two relations -/

/-- The target relation and the control relation of `NativeGate`, and nothing else. -/
structure GateRel (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where
  relT : ∀ ω, actT N (G (actT N ω)) = G ω
  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)

theorem gateRel_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ}
    {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) :
    GateRel N G :=
  ⟨hG.relT, hG.relC⟩

theorem opGate_comp_homMap_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G)
    (F : HVec d →ₗ[ℝ] HVec d) : opGate G (F ∘ₗ homMap N) = opGate G F ∘ₗ homMap N := by
  obtain ⟨ω, rfl⟩ : ∃ ω, F = toOp ω := ⟨fromOp F, (toOp_fromOp F).symm⟩
  have h : G (actT N ω) = actT N (G ω) := by
    rw [← hR.relT ω, actT_actT hN.invol]
  rw [← toOp_actT hN, opGate_toOp, opGate_toOp, h, toOp_actT hN]

theorem opGate_homMap_comp_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G)
    (F : HVec d →ₗ[ℝ] HVec d) :
    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N := by
  obtain ⟨ω, rfl⟩ : ∃ ω, F = toOp ω := ⟨fromOp F, (toOp_fromOp F).symm⟩
  have h : G (actC N ω) = actC N (actT N (G ω)) := by
    rw [← hR.relC ω, actC_actC hN.invol]
  rw [← toOp_actC, opGate_toOp, opGate_toOp, h, toOp_actC, toOp_actT hN]

theorem Lop_anti_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hR : GateRel N G) (f : OpSpace N) :
    Lop G hN.invol (Pop N f) = - Pop N (Lop G hN.invol f) := by
  apply LinearMap.ext; intro u
  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]
  have hcomp : Pop N f ∘ₗ projMinus hN.invol = homMap N ∘ₗ (f ∘ₗ projMinus hN.invol) := by
    apply LinearMap.ext; intro v
    simp only [LinearMap.comp_apply, Pop_apply]
  rw [hcomp, opGate_homMap_comp_rel hN hR, LinearMap.comp_apply, LinearMap.comp_apply,
    mem_minusSpace.mp u.2]
  simp only [map_neg]

theorem Lop_eq_zero_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hR : GateRel N G) (f : OpSpace N)
    (hf : Lop G hN.invol f = 0) : f = 0 := by
  set F : HVec d →ₗ[ℝ] HVec d := f ∘ₗ projMinus hN.invol with hF
  have hminus : ∀ u ∈ minusSpace N, opGate G F u = 0 := by
    intro u hu
    have := LinearMap.congr_fun hf ⟨u, hu⟩
    rwa [Lop_apply, LinearMap.zero_apply] at this
  have hFN : F ∘ₗ homMap N = -F := by
    apply LinearMap.ext; intro v
    simp only [hF, LinearMap.comp_apply, LinearMap.neg_apply, projMinus_homMap, map_neg]
  have hplus : ∀ v ∈ plusSpace N, opGate G F v = 0 := by
    intro v hv
    have h1 := LinearMap.congr_fun (opGate_comp_homMap_rel hN hR F) v
    rw [hFN, map_neg, LinearMap.neg_apply, LinearMap.comp_apply, mem_plusSpace.mp hv] at h1
    have h2 : (2 : ℝ) • opGate G F v = 0 := by
      rw [two_smul]
      nth_rewrite 1 [← h1]
      exact neg_add_cancel _
    exact (smul_eq_zero.mp h2).resolve_left two_ne_zero
  have hall : opGate G F = 0 := by
    apply LinearMap.ext; intro v
    have hdecomp : v = (1 / 2 : ℝ) • (v + homMap N v) + (1 / 2 : ℝ) • (v - homMap N v) := by
      module
    have hp : (1 / 2 : ℝ) • (v + homMap N v) ∈ plusSpace N := by
      rw [mem_plusSpace, map_smul, map_add, homMap_homMap hN.invol, add_comm (homMap N v) v]
    have hm : (1 / 2 : ℝ) • (v - homMap N v) ∈ minusSpace N := (projMinus hN.invol v).2
    rw [LinearMap.zero_apply, hdecomp, map_add, hplus _ hp, hminus _ hm, add_zero]
  have hGF : G (fromOp F) = 0 := by
    apply toOp_injective
    rw [← opGate_toOp, toOp_fromOp, hall, ← toOpLin_apply, map_zero]
  have hF0 : F = 0 := by
    have h0 : fromOp F = 0 := G.injective (by rw [hGF, map_zero])
    rw [← toOp_fromOp F, h0, ← toOpLin_apply, map_zero]
  apply LinearMap.ext; intro u
  have := LinearMap.congr_fun hF0 u
  rw [hF, LinearMap.comp_apply, LinearMap.zero_apply] at this
  rw [LinearMap.zero_apply, ← this]
  congr 1
  exact Subtype.ext (projMinus_of_mem hN.invol u.2).symm

theorem Lop_injective_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :
    Function.Injective (Lop G hN.invol) :=
  LinearMap.ker_eq_bot.mp (LinearMap.ker_eq_bot'.mpr fun f hf => Lop_eq_zero_rel hN hR f hf)

/-- **Parity from the two relations.** The `+1` and `−1` eigenspaces of the homogenized NOT have
the same dimension; the frame and positivity are not read. -/
theorem finrank_plus_eq_finrank_minus_rel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by
  have hpar := NativeGateBall.parity (Pop N) (Lop G hN.invol) (Lop_injective_rel hN hR)
    (Lop_anti_rel hN hR)
  rw [finrank_ker_Pop_sub, finrank_ker_Pop_add] at hpar
  exact Nat.eq_of_mul_eq_mul_left (one_le_finrank_minusSpace hN) hpar

/-- No even dimension carries the two relations. -/
theorem not_even_of_gateRel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d :=
  not_even_of_balanced (finrank_plus_add_finrank_minus hN.invol)
    (finrank_plus_eq_finrank_minus_rel hN hR)

/-! ### §B — the NOT at `d = 3` -/

/-- At `d = 3` the two eigenspaces of the homogenized NOT both have dimension two. -/
theorem finrank_plus_minus_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :
    Module.finrank ℝ (plusSpace N) = 2 ∧ Module.finrank ℝ (minusSpace N) = 2 := by
  have h1 := finrank_plus_add_finrank_minus hN.invol
  have h2 := finrank_plus_eq_finrank_minus_rel hN hR
  omega

/-- At `d = 3` the fixed space of the NOT has dimension one. -/
theorem tangentPlus_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) : tangentPlus N = 1 := by
  have h := (finrank_plus_minus_three hN hR).1
  unfold tangentPlus
  omega

/-- **The NOT at `d = 3` is a rotation by `π`.** There is a unit axis `u` with
`N x = 2 (u · x) u − x`. -/
theorem piRotation_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :
    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x := by
  have ht : Module.finrank ℝ (tangentSpace N) = 1 := by
    rw [finrank_tangentSpace]
    exact tangentPlus_three hN hR
  have hne : tangentSpace N ≠ ⊥ := fun h0 => by
    have := Submodule.finrank_eq_zero.mpr h0
    omega
  obtain ⟨v, hvS, hv0⟩ := (Submodule.ne_bot_iff _).mp hne
  have hv' : (⟨v, hvS⟩ : tangentSpace N) ≠ 0 := fun h => hv0 (congrArg Subtype.val h)
  have hspan := (finrank_eq_one_iff_of_nonzero' (⟨v, hvS⟩ : tangentSpace N) hv').1 ht
  obtain ⟨hfix, hv00⟩ := mem_tangentSpace.mp hvS
  obtain ⟨w, hw⟩ : ∃ w : Fin 3 → ℝ, Matrix.vecTail v = w := ⟨_, rfl⟩
  have hNw : N w = w := by
    have := congrArg Matrix.vecTail hfix
    rw [vecTail_homMap, hw] at this
    exact this
  have hw0 : w ≠ 0 := by
    intro h0
    apply hv0
    funext i
    refine Fin.cases ?_ (fun j => ?_) i
    · exact hv00
    · exact congrFun (hw.trans h0) j
  obtain ⟨s, hs_def⟩ : ∃ s : ℝ, ∑ j, w j ^ 2 = s := ⟨_, rfl⟩
  have hs : 0 < s := by
    rw [← hs_def]
    rcases (Finset.sum_nonneg fun j _ => sq_nonneg (w j) : (0 : ℝ) ≤ ∑ j, w j ^ 2).lt_or_eq
      with h | h
    · exact h
    · exfalso
      apply hw0
      funext j
      exact (pow_eq_zero_iff two_ne_zero).mp
        ((Finset.sum_eq_zero_iff_of_nonneg (fun j _ => sq_nonneg (w j))).1 h.symm j
          (Finset.mem_univ _))
  have hr : Real.sqrt s * Real.sqrt s = s := Real.mul_self_sqrt hs.le
  have hdot : ∀ x : Fin 3 → ℝ, ∑ j, (N x) j * w j = ∑ j, x j * w j := fun x => by
    rw [dot_apply hN x w, hNw]
  have hkey : ∀ x : Fin 3 → ℝ, ∃ c : ℝ, x + N x = c • w := by
    intro x
    have hmem : (Matrix.vecCons 0 (x + N x) : HVec 3) ∈ tangentSpace N := by
      rw [mem_tangentSpace]
      refine ⟨?_, rfl⟩
      funext i
      refine Fin.cases ?_ (fun j => ?_) i
      · rfl
      · rw [homMap_succ, Matrix.tail_cons, map_add, hN.invol]
        simp [add_comm]
    obtain ⟨c, hc⟩ := hspan ⟨_, hmem⟩
    have h1 : c • v = Matrix.vecCons 0 (x + N x) := congrArg Subtype.val hc
    have h2 := congrArg Matrix.vecTail h1
    rw [vecTail_smul, Matrix.tail_cons, hw] at h2
    exact ⟨c, h2.symm⟩
  refine ⟨(Real.sqrt s)⁻¹ • w, ?_, ?_⟩
  · simp only [Pi.smul_apply, smul_eq_mul, mul_pow]
    rw [← Finset.mul_sum, hs_def, inv_pow, sq, hr]
    exact inv_mul_cancel₀ hs.ne'
  · intro x
    obtain ⟨c, hc⟩ := hkey x
    have hcs : c * s = 2 * ∑ j, x j * w j := by
      have e1 : ∑ j, (x + N x) j * w j = ∑ j, (c • w) j * w j := by rw [hc]
      have e2 : ∑ j, (x + N x) j * w j = 2 * ∑ j, x j * w j := by
        simp only [Pi.add_apply, add_mul, Finset.sum_add_distrib, hdot x]
        ring
      have e3 : ∑ j, (c • w) j * w j = c * s := by
        rw [← hs_def, Finset.mul_sum]
        exact Finset.sum_congr rfl fun j _ => by simp only [Pi.smul_apply, smul_eq_mul]; ring
      linarith
    have hNx : N x = c • w - x := by
      rw [← hc]
      abel
    rw [hNx]
    congr 1
    rw [smul_smul]
    congr 1
    simp only [Pi.smul_apply, smul_eq_mul]
    have hsum : ∑ j, (Real.sqrt s)⁻¹ * w j * x j = (Real.sqrt s)⁻¹ * ∑ j, x j * w j := by
      rw [Finset.mul_sum]
      exact Finset.sum_congr rfl fun j _ => by ring
    rw [hsum]
    have hinv : (Real.sqrt s)⁻¹ * (Real.sqrt s)⁻¹ = s⁻¹ := by rw [← mul_inv, hr]
    have hc' : c = 2 * (∑ j, x j * w j) * s⁻¹ := (eq_mul_inv_iff_mul_eq₀ hs.ne').mpr hcs
    rw [hc', ← hinv]
    ring

/-- A rotation by `π` about a unit axis of the three-dimensional space has determinant one. -/
theorem det_eq_one_of_piRotation {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {u : Fin 3 → ℝ}
    (hu : ∑ j, u j ^ 2 = 1) (hN : ∀ x, N x = (2 * ∑ j, u j * x j) • u - x) :
    LinearMap.det N = 1 := by
  have hu3 : u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2 = 1 := by
    rw [Fin.sum_univ_three] at hu
    exact hu
  have hent : ∀ i j : Fin 3, LinearMap.toMatrix' N i j =
      2 * u j * u i - (if i = j then 1 else 0) := fun i j => by
    rw [LinearMap.toMatrix'_apply, hN]
    simp [Pi.single_apply]
  have hd : ∀ i : Fin 3, LinearMap.toMatrix' N i i = 2 * u i * u i - 1 := fun i => by
    rw [hent, if_pos rfl]
  have ho : ∀ i j : Fin 3, i ≠ j → LinearMap.toMatrix' N i j = 2 * u j * u i := fun i j h => by
    rw [hent, if_neg h, sub_zero]
  rw [← LinearMap.det_toMatrix', Matrix.det_fin_three, hd 0, hd 1, hd 2,
    ho 0 1 (by decide), ho 0 2 (by decide), ho 1 0 (by decide), ho 1 2 (by decide),
    ho 2 0 (by decide), ho 2 1 (by decide)]
  linear_combination 2 * hu3

/-- **The NOT at `d = 3` has determinant one.** -/
theorem det_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)} {G : W 3 ≃ₗ[ℝ] W 3}
    (hN : IsNot (eball 3) z N) (hR : GateRel N G) : LinearMap.det N = 1 := by
  obtain ⟨u, hu, hform⟩ := piRotation_three hN hR
  exact det_eq_one_of_piRotation hu hform

theorem tangentPlus_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :
    tangentPlus N = 1 :=
  tangentPlus_three hN (gateRel_of_nativeGate hG)

theorem piRotation_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :
    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x :=
  piRotation_three hN (gateRel_of_nativeGate hG)

theorem det_of_nativeGate_three {z : Fin 3 → ℝ} {N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)}
    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hG : NativeGate (eball 3) z N G) :
    LinearMap.det N = 1 :=
  det_three hN (gateRel_of_nativeGate hG)

/-! ### §C — controls for the NOT at `d = 3` -/

/-- A diagonal map of one copy. -/
def diagSign (c : Fin d → ℝ) : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ) where
  toFun x := fun i => c i * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' a x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem diagSign_apply (c x : Fin d → ℝ) (i : Fin d) : diagSign c x i = c i * x i := rfl

theorem homMap_diagSign (c : Fin d → ℝ) (v : HVec d) (μ : Fin (d + 1)) :
    homMap (diagSign c) v μ = Matrix.vecCons 1 c μ * v μ := by
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp
  · rw [homMap_succ, Matrix.cons_val_succ]
    rfl

/-- The reflection inverting the third coordinate. -/
def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![1, 1, -1]

/-- The NOT inverting every coordinate. -/
def negId3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![-1, -1, -1]

theorem negId3_eq : negId3 = -LinearMap.id := by
  refine LinearMap.ext fun x => funext fun i => ?_
  fin_cases i <;> simp [negId3, diagSign_apply]

theorem isNot_refl3 : IsNot (eball 3) z3 refl3 where
  unit := isNot_nflip.unit
  invol x := by funext i; fin_cases i <;> simp [refl3, diagSign_apply]
  preserves x hx := by
    rw [mem_eball, Fin.sum_univ_three] at hx ⊢
    simpa [refl3, diagSign_apply, neg_sq] using hx
  flips := by funext i; fin_cases i <;> simp [refl3, diagSign_apply]

theorem isNot_negId3 : IsNot (eball 3) z3 negId3 where
  unit := isNot_nflip.unit
  invol x := by funext i; fin_cases i <;> simp [negId3, diagSign_apply]
  preserves x hx := by
    rw [mem_eball, Fin.sum_univ_three] at hx ⊢
    simpa [negId3, diagSign_apply, neg_sq] using hx
  flips := by funext i; fin_cases i <;> simp [negId3, diagSign_apply]

theorem minusSpace_refl3_le :
    minusSpace refl3 ≤ Submodule.span ℝ {(Pi.single 3 1 : HVec 3)} := by
  intro v hv
  rw [mem_minusSpace] at hv
  rw [Submodule.mem_span_singleton]
  refine ⟨v 3, ?_⟩
  have e0 : homMap refl3 v 0 = 1 * v 0 := homMap_diagSign _ _ _
  have e1 : homMap refl3 v 1 = 1 * v 1 := homMap_diagSign _ _ _
  have e2 : homMap refl3 v 2 = 1 * v 2 := homMap_diagSign _ _ _
  have h0 := congrFun hv 0
  have h1 := congrFun hv 1
  have h2 := congrFun hv 2
  rw [e0, Pi.neg_apply] at h0
  rw [e1, Pi.neg_apply] at h1
  rw [e2, Pi.neg_apply] at h2
  have z0 : v 0 = 0 := by linarith
  have z1 : v 1 = 0 := by linarith
  have z2 : v 2 = 0 := by linarith
  funext i
  fin_cases i <;> simp <;> linarith

theorem plusSpace_negId3_le :
    plusSpace negId3 ≤ Submodule.span ℝ {(Pi.single 0 1 : HVec 3)} := by
  intro v hv
  rw [mem_plusSpace] at hv
  rw [Submodule.mem_span_singleton]
  refine ⟨v 0, ?_⟩
  have e1 : homMap negId3 v 1 = -1 * v 1 := homMap_diagSign _ _ _
  have e2 : homMap negId3 v 2 = -1 * v 2 := homMap_diagSign _ _ _
  have e3 : homMap negId3 v 3 = -1 * v 3 := homMap_diagSign _ _ _
  have h1 := congrFun hv 1
  have h2 := congrFun hv 2
  have h3 := congrFun hv 3
  rw [e1] at h1
  rw [e2] at h2
  rw [e3] at h3
  have z1 : v 1 = 0 := by linarith
  have z2 : v 2 = 0 := by linarith
  have z3 : v 3 = 0 := by linarith
  funext i
  fin_cases i <;> simp <;> linarith

theorem finrank_minusSpace_refl3_le : Module.finrank ℝ (minusSpace refl3) ≤ 1 := by
  have hne : (Pi.single 3 1 : HVec 3) ≠ 0 := by
    intro h
    have := congrFun h 3
    simp at this
  exact (Submodule.finrank_mono minusSpace_refl3_le).trans (finrank_span_singleton hne).le

theorem finrank_plusSpace_negId3_le : Module.finrank ℝ (plusSpace negId3) ≤ 1 := by
  have hne : (Pi.single 0 1 : HVec 3) ≠ 0 := by
    intro h
    have := congrFun h 0
    simp at this
  exact (Submodule.finrank_mono plusSpace_negId3_le).trans (finrank_span_singleton hne).le

/-- The reflection `diag(1, 1, −1)` carries no pair of relations. -/
theorem not_gateRel_refl3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel refl3 G := fun hR => by
  have h := (finrank_plus_minus_three isNot_refl3 hR).2
  have hle := finrank_minusSpace_refl3_le
  omega

/-- The NOT `−id` carries no pair of relations. -/
theorem not_gateRel_negId3 (G : W 3 ≃ₗ[ℝ] W 3) : ¬ GateRel negId3 G := fun hR => by
  have h := (finrank_plus_minus_three isNot_negId3 hR).1
  have hle := finrank_plusSpace_negId3_le
  omega

theorem det_refl3 : LinearMap.det refl3 = -1 := by
  have h : refl3 = Matrix.toLin' (Matrix.diagonal (![1, 1, -1] : Fin 3 → ℝ)) := by
    refine LinearMap.ext fun x => funext fun i => ?_
    rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal]
    rfl
  rw [h, LinearMap.det_toLin', Matrix.det_diagonal, Fin.prod_univ_three]
  simp

theorem det_negId3 : LinearMap.det negId3 = -1 := by
  have h : negId3 = Matrix.toLin' (Matrix.diagonal (![-1, -1, -1] : Fin 3 → ℝ)) := by
    refine LinearMap.ext fun x => funext fun i => ?_
    rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal]
    rfl
  rw [h, LinearMap.det_toLin', Matrix.det_diagonal, Fin.prod_univ_three]
  show (-1 : ℝ) * -1 * -1 = -1
  norm_num

/-- DIM-1's `cnot` with `nflip` carries the two relations. -/
theorem gateRel_cnot : GateRel nflip cnot := ⟨cnot_relT, cnot_relC⟩

theorem tangentPlus_nflip : tangentPlus nflip = 1 := tangentPlus_three isNot_nflip gateRel_cnot

theorem det_nflip_rel : LinearMap.det nflip = 1 := det_three isNot_nflip gateRel_cnot

/-! ### §D — the sign-free permutation gates -/

/-- The permutation gate: identity on the target-even columns, the control-index involution `p`
on the target-odd columns. -/
def sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1)) (ω : W d) : W d :=
  fun μ ν => if odd ν then ω (p μ) ν else ω μ ν

theorem sgate_sgate (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))
    (hp : ∀ μ, p (p μ) = μ) (ω : W d) : sgate odd p (sgate odd p ω) = ω := by
  funext μ ν
  simp only [sgate]
  split_ifs <;> simp [hp]

def sgateEquiv (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))
    (hp : ∀ μ, p (p μ) = μ) : W d ≃ₗ[ℝ] W d where
  toFun := sgate odd p
  invFun := sgate odd p
  map_add' ω ω' := by
    funext μ ν
    simp only [sgate, Pi.add_apply]
    split_ifs <;> rfl
  map_smul' c ω := by
    funext μ ν
    simp only [sgate, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    split_ifs <;> rfl
  left_inv := sgate_sgate odd p hp
  right_inv := sgate_sgate odd p hp

theorem sgateEquiv_apply (odd : Fin (d + 1) → Bool) (p : Fin (d + 1) → Fin (d + 1))
    (hp : ∀ μ, p (p μ) = μ) (ω : W d) : sgateEquiv odd p hp ω = sgate odd p ω := rfl

/-- The target relation for a permutation gate and a NOT acting by the signs of `odd`. -/
theorem sgate_relT {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool}
    {p : Fin (d + 1) → Fin (d + 1)}
    (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ) (ω : W d) :
    actT N (sgate odd p (actT N ω)) = sgate odd p ω := by
  funext μ ν
  simp only [actT_apply, hN, sgate]
  split_ifs <;> ring

/-- The control relation for a permutation gate whose involution exchanges the two signs. -/
theorem sgate_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {odd : Fin (d + 1) → Bool}
    {p : Fin (d + 1) → Fin (d + 1)}
    (hN : ∀ (v : HVec d) μ, homMap N v μ = (if odd μ then -1 else 1) * v μ)
    (hodd : ∀ μ, odd (p μ) = !odd μ) (ω : W d) :
    actC N (sgate odd p (actC N ω)) = actT N (sgate odd p ω) := by
  funext μ ν
  simp only [actC_apply, actT_apply, hN, sgate, hodd]
  cases odd μ <;> cases odd ν <;> simp

/-! ### §E — `d = 3`: the gate `gJ3` -/

def odd3 : Fin 4 → Bool
  | 0 => false | 1 => false | 2 => true | 3 => true

def perm3 : Fin 4 → Fin 4
  | 0 => 3 | 1 => 2 | 2 => 1 | 3 => 0

theorem perm3_perm3 : ∀ μ, perm3 (perm3 μ) = μ := by decide

theorem odd3_perm3 : ∀ μ, odd3 (perm3 μ) = !odd3 μ := by decide

/-- The sign-free permutation gate of two copies of `eball 3`. -/
def gJ3 : W 3 ≃ₗ[ℝ] W 3 := sgateEquiv odd3 perm3 perm3_perm3

theorem gJ3_apply (ω : W 3) : gJ3 ω = sgate odd3 perm3 ω := rfl

theorem homMap_nflip_sign (v : HVec 3) (μ : Fin (3 + 1)) :
    homMap nflip v μ = (if odd3 μ then -1 else 1) * v μ := by
  fin_cases μ <;> simp [odd3]

theorem gJ3_frame (a b : Fin 2) :
    gJ3 (prodState (corner z3 a) (corner z3 b)) = prodState (corner z3 a) (corner z3 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [gJ3_apply, sgate, perm3, prodState_apply, corner_zero, corner_one]

theorem gateRel_gJ3 : GateRel nflip gJ3 :=
  ⟨fun ω => by simp only [gJ3_apply]; exact sgate_relT homMap_nflip_sign ω,
   fun ω => by simp only [gJ3_apply]; exact sgate_relC homMap_nflip_sign odd3_perm3 ω⟩

/-- The direction of the first sharp effect of the witness, `−(3/5 e₂ + 4/5 e₃)`. -/
noncomputable def w3 : Fin 3 → ℝ := ![0, -3 / 5, -4 / 5]

theorem w3_unit : ∑ j, w3 j ^ 2 = 1 := by
  rw [Fin.sum_univ_three]
  show (0 : ℝ) ^ 2 + (-3 / 5) ^ 2 + (-4 / 5) ^ 2 = 1
  norm_num

theorem sharpVec_w3 : sharpVec w3 = ![1 / 2, 0, -3 / 10, -2 / 5] := by
  funext i
  fin_cases i
  · rfl
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (-3 / 5 : ℝ) / 2 = -3 / 10
    norm_num
  · show (-4 / 5 : ℝ) / 2 = -2 / 5
    norm_num

theorem sharpVec_z3 : sharpVec z3 = ![1 / 2, 0, 0, 1 / 2] := by
  funext i
  fin_cases i
  · rfl
  · show z3 0 / 2 = 0
    norm_num
  · show z3 1 / 2 = 0
    norm_num
  · show z3 2 / 2 = 1 / 2
    norm_num

/-- The image of the pure product `(e₁, z3)` pairs to `−1/10` with two sharp effects. -/
theorem gJ3_value :
    prodEffVal (sharpEff w3) (sharpEff z3) (gJ3 (prodState xplus z3)) = -1 / 10 := by
  rw [prodEffVal_sharp, sharpVec_w3, sharpVec_z3]
  simp +decide [pairVal, sum_univ_four', gJ3_apply, sgate, odd3, perm3, prodState_apply, xplus]
  norm_num

theorem gJ3_not_mem_maxCone : gJ3 (prodState xplus z3) ∉ maxCone (eball 3) := fun h => by
  have hv := h _ _ (sharpEff_isEffectOn w3_unit) (sharpEff_isEffectOn isNot_nflip.unit)
  rw [gJ3_value] at hv
  norm_num at hv

/-- **At `d = 3` the frame and the relations hold and forward positivity fails.** -/
theorem not_posFwd_gJ3 :
    ¬ ∀ x ∈ eball 3, ∀ y ∈ eball 3, gJ3 (prodState x y) ∈ maxCone (eball 3) :=
  fun h => gJ3_not_mem_maxCone (h _ xplus_mem _ z3_mem)

theorem not_nativeGate_gJ3 : ¬ NativeGate (eball 3) z3 nflip gJ3 :=
  fun hG => not_posFwd_gJ3 hG.posFwd

/-! ### §F — `d = 5`: the NOT `n5` and the gate `gJ5` -/

def odd5 : Fin 6 → Bool
  | 0 => false | 1 => false | 2 => false | 3 => true | 4 => true | 5 => true

def perm5 : Fin 6 → Fin 6
  | 0 => 5 | 1 => 3 | 2 => 4 | 3 => 1 | 4 => 2 | 5 => 0

theorem perm5_perm5 : ∀ μ, perm5 (perm5 μ) = μ := by decide

theorem odd5_perm5 : ∀ μ, odd5 (perm5 μ) = !odd5 μ := by decide

/-- The signs of `n5` on the five coordinates. -/
def c5 (j : Fin 5) : ℝ := if odd5 j.succ then -1 else 1

/-- The NOT of `eball 5` fixing the first two coordinates and inverting the other three. -/
def n5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign c5

/-- The corner axis of `eball 5`. -/
def z5 : Fin 5 → ℝ := fun i => if i = 4 then 1 else 0

/-- The first axis of `eball 5`. -/
def x5 : Fin 5 → ℝ := fun i => if i = 0 then 1 else 0

theorem c5_sq (j : Fin 5) : c5 j ^ 2 = 1 := by
  unfold c5
  split_ifs <;> norm_num

theorem homMap_n5_sign (v : HVec 5) (μ : Fin (5 + 1)) :
    homMap n5 v μ = (if odd5 μ then -1 else 1) * v μ := by
  show homMap (diagSign c5) v μ = _
  rw [homMap_diagSign]
  congr 1
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp [odd5]
  · rw [Matrix.cons_val_succ]
    rfl

theorem isNot_n5 : IsNot (eball 5) z5 n5 where
  unit := by
    rw [Fin.sum_univ_five]
    simp [z5]
  invol x := by
    funext i
    show c5 i * (c5 i * x i) = x i
    rw [← mul_assoc, ← sq, c5_sq, one_mul]
  preserves x hx := by
    rw [mem_eball] at hx ⊢
    have h : ∀ j, (n5 x j) ^ 2 = x j ^ 2 := fun j => by
      show (c5 j * x j) ^ 2 = x j ^ 2
      rw [mul_pow, c5_sq, one_mul]
    rw [Finset.sum_congr rfl fun j _ => h j]
    exact hx
  flips := by
    funext i
    show c5 i * z5 i = -z5 i
    fin_cases i <;> simp +decide [c5, z5]

theorem x5_mem : x5 ∈ eball 5 := by
  rw [mem_eball, Fin.sum_univ_five]
  simp [x5]

theorem z5_mem : z5 ∈ eball 5 := by
  rw [mem_eball, Fin.sum_univ_five]
  simp [z5]

/-- The sign-free permutation gate of two copies of `eball 5`. -/
def gJ5 : W 5 ≃ₗ[ℝ] W 5 := sgateEquiv odd5 perm5 perm5_perm5

theorem gJ5_apply (ω : W 5) : gJ5 ω = sgate odd5 perm5 ω := rfl

@[simp] theorem hom5_one (x : Fin 5 → ℝ) : hom x (1 : Fin (5 + 1)) = x 0 := rfl
@[simp] theorem hom5_two (x : Fin 5 → ℝ) : hom x (2 : Fin (5 + 1)) = x 1 := rfl
@[simp] theorem hom5_three (x : Fin 5 → ℝ) : hom x (3 : Fin (5 + 1)) = x 2 := rfl
@[simp] theorem hom5_four (x : Fin 5 → ℝ) : hom x (4 : Fin (5 + 1)) = x 3 := rfl
@[simp] theorem hom5_five (x : Fin 5 → ℝ) : hom x (5 : Fin (5 + 1)) = x 4 := rfl

theorem gJ5_frame (a b : Fin 2) :
    gJ5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [gJ5_apply, sgate, perm5, prodState_apply, corner_zero, corner_one, z5]

theorem gateRel_gJ5 : GateRel n5 gJ5 :=
  ⟨fun ω => by simp only [gJ5_apply]; exact sgate_relT homMap_n5_sign ω,
   fun ω => by simp only [gJ5_apply]; exact sgate_relC homMap_n5_sign odd5_perm5 ω⟩

/-- **Parity holds at `d = 5`**: with `n5` and `gJ5` the eigenspaces are balanced. -/
theorem finrank_plus_eq_finrank_minus_n5 :
    Module.finrank ℝ (plusSpace n5) = Module.finrank ℝ (minusSpace n5) :=
  finrank_plus_eq_finrank_minus_rel isNot_n5 gateRel_gJ5

/-- The direction of the first sharp effect of the witness, `−(3/5 e₃ + 4/5 e₅)`. -/
noncomputable def w5 : Fin 5 → ℝ := fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0

theorem w5_unit : ∑ j, w5 j ^ 2 = 1 := by
  rw [Fin.sum_univ_five]
  show (0 : ℝ) ^ 2 + 0 ^ 2 + (-3 / 5) ^ 2 + 0 ^ 2 + (-4 / 5) ^ 2 = 1
  norm_num

theorem z5_unit : ∑ j, z5 j ^ 2 = 1 := isNot_n5.unit

theorem sharpVec_w5 : sharpVec w5 = fun μ : Fin (5 + 1) =>
    if μ = 0 then 1 / 2 else if μ = 3 then -3 / 10 else if μ = 5 then -2 / 5 else 0 := by
  funext i
  fin_cases i
  · rfl
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (-3 / 5 : ℝ) / 2 = -3 / 10
    norm_num
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (-4 / 5 : ℝ) / 2 = -2 / 5
    norm_num

theorem sharpVec_z5 : sharpVec z5 = fun μ : Fin (5 + 1) =>
    if μ = 0 then 1 / 2 else if μ = 5 then 1 / 2 else 0 := by
  funext i
  fin_cases i
  · rfl
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (0 : ℝ) / 2 = 0
    norm_num
  · show (1 : ℝ) / 2 = 1 / 2
    rfl

theorem sum_univ_six' (f : Fin (5 + 1) → ℝ) :
    ∑ i, f i = f 0 + f 1 + f 2 + f 3 + f 4 + f 5 :=
  Fin.sum_univ_six f

/-- The image of the pure product `(e₁, z5)` pairs to `−1/10` with two sharp effects. -/
theorem gJ5_value :
    prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1 / 10 := by
  rw [prodEffVal_sharp, sharpVec_w5, sharpVec_z5]
  simp +decide [pairVal, sum_univ_six', gJ5_apply, sgate, odd5, perm5, prodState_apply, x5, z5]
  norm_num

theorem gJ5_not_mem_maxCone : gJ5 (prodState x5 z5) ∉ maxCone (eball 5) := fun h => by
  have hv := h _ _ (sharpEff_isEffectOn w5_unit) (sharpEff_isEffectOn z5_unit)
  rw [gJ5_value] at hv
  norm_num at hv

/-- **At `d = 5` the frame and the relations hold and forward positivity fails.** -/
theorem not_posFwd_gJ5 :
    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5) :=
  fun h => gJ5_not_mem_maxCone (h _ x5_mem _ z5_mem)

theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5 :=
  fun hG => not_posFwd_gJ5 hG.posFwd

end ParityNot
end OIBridge

#print axioms OIBridge.ParityNot.finrank_plus_eq_finrank_minus_rel
#print axioms OIBridge.ParityNot.not_even_of_gateRel
#print axioms OIBridge.ParityNot.finrank_plus_minus_three
#print axioms OIBridge.ParityNot.tangentPlus_three
#print axioms OIBridge.ParityNot.piRotation_three
#print axioms OIBridge.ParityNot.det_three
#print axioms OIBridge.ParityNot.piRotation_of_nativeGate_three
#print axioms OIBridge.ParityNot.det_of_nativeGate_three
#print axioms OIBridge.ParityNot.not_gateRel_refl3
#print axioms OIBridge.ParityNot.not_gateRel_negId3
#print axioms OIBridge.ParityNot.det_refl3
#print axioms OIBridge.ParityNot.det_negId3
#print axioms OIBridge.ParityNot.gateRel_cnot
#print axioms OIBridge.ParityNot.det_nflip_rel
#print axioms OIBridge.ParityNot.gJ3_frame
#print axioms OIBridge.ParityNot.gateRel_gJ3
#print axioms OIBridge.ParityNot.gJ3_value
#print axioms OIBridge.ParityNot.not_posFwd_gJ3
#print axioms OIBridge.ParityNot.isNot_n5
#print axioms OIBridge.ParityNot.gJ5_frame
#print axioms OIBridge.ParityNot.gateRel_gJ5
#print axioms OIBridge.ParityNot.finrank_plus_eq_finrank_minus_n5
#print axioms OIBridge.ParityNot.gJ5_value
#print axioms OIBridge.ParityNot.not_posFwd_gJ5
