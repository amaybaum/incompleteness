/-
  OIBridge/OddChar.lean — design (round ODD-CHAR-1, not for landing): the dimensions that carry
  a NOT, the frame and the two gate relations are exactly the odd ones, and at every odd dimension
  at least three an explicit gate with the frame and the relations fails forward positivity.

  (A) The family. For `k : ℕ` and `d = 2k+1`, the homogeneous indices `0, …, k` have sign `+1` and
  `k+1, …, 2k+1` sign `−1` (`oddK`); the reversal `Fin.rev` exchanges the two classes
  (`oddK_rev`). `nK k` is the diagonal NOT with those signs, a NOT of `eball (2k+1)` with axis the
  last coordinate (`isNot_nK`), and `gRev k` is PARITY-NOT-1's sign-free permutation gate for the
  reversal. It satisfies `NativeGate`'s frame (`gRev_frame`) and both relations (`gateRel_gRev`).

  (B) The characterization. Some `z`, `N`, `G` with `IsNot (eball d) z N`, the frame and
  `GateRel N G` exist exactly when `d` is odd (`exists_frame_gateRel_iff_odd`): one direction is
  PARITY-NOT-1's `not_even_of_gateRel`; the other is DIM-1's `cnot1` at `d = 1` and `gRev k` at
  `d = 2k+1`, `k ≥ 1`.

  (C) Positivity. For `k ≥ 1` the image under `gRev k` of the product of the first axis with the
  corner pairs to `−1/10` with the sharp effects of `wK k` and the corner (`gRev_value`), so
  forward positivity fails (`not_posFwd_gRev`).

  Nothing here concerns which gates are positive, the frame-free or relation-free cases, a complex
  structure, or the NOT of a physical theory.
-/
import OIBridge.ParityNot

namespace OIBridge
namespace OddChar

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot

variable {d : ℕ}

/-! ### §A — the family -/

/-- The sign class of a homogeneous index at `d = 2k+1`: the upper half is odd. -/
def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))

theorem oddK_rev (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : oddK k (Fin.rev μ) = !oddK k μ := by
  have h1 := μ.isLt
  have h2 : ((Fin.rev μ : Fin (2 * k + 1 + 1)) : ℕ) = 2 * k + 1 - μ := by rw [Fin.val_rev]; omega
  unfold oddK
  rw [h2]
  by_cases h : k < (μ : ℕ)
  · have h' : ¬ k < 2 * k + 1 - (μ : ℕ) := by omega
    rw [decide_eq_true h, decide_eq_false h']
    rfl
  · have h' : k < 2 * k + 1 - (μ : ℕ) := by omega
    rw [decide_eq_false h, decide_eq_true h']
    rfl

/-- The signs of the NOT on the `2k+1` coordinates. -/
def cK (k : ℕ) (j : Fin (2 * k + 1)) : ℝ := if oddK k j.succ then -1 else 1

/-- The NOT of `eball (2k+1)` with the signs of `oddK`. -/
def nK (k : ℕ) : (Fin (2 * k + 1) → ℝ) →ₗ[ℝ] (Fin (2 * k + 1) → ℝ) := diagSign (cK k)

/-- The corner axis: the last coordinate. -/
def zK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 2 * k then 1 else 0

/-- The reversal gate of two copies of `eball (2k+1)`. -/
def gRev (k : ℕ) : W (2 * k + 1) ≃ₗ[ℝ] W (2 * k + 1) := sgateEquiv (oddK k) Fin.rev Fin.rev_rev

theorem gRev_apply (k : ℕ) (ω : W (2 * k + 1)) : gRev k ω = sgate (oddK k) Fin.rev ω := rfl

theorem cK_sq (k : ℕ) (j : Fin (2 * k + 1)) : cK k j ^ 2 = 1 := by
  unfold cK
  split_ifs <;> norm_num

theorem homMap_nK_sign (k : ℕ) (v : HVec (2 * k + 1)) (μ : Fin (2 * k + 1 + 1)) :
    homMap (nK k) v μ = (if oddK k μ then -1 else 1) * v μ := by
  show homMap (diagSign (cK k)) v μ = _
  rw [homMap_diagSign]
  congr 1
  refine Fin.cases ?_ (fun j => ?_) μ
  · have h0 : oddK k 0 = false := by
      unfold oddK
      simp
    rw [h0]
    rfl
  · rw [Matrix.cons_val_succ]
    rfl

/-- A sum over `Fin n` of an indicator of one value of the index. -/
theorem sum_val_ite (n m : ℕ) (hm : m < n) (c : ℝ) :
    ∑ j : Fin n, (if (j : ℕ) = m then c else 0) = c := by
  rw [Finset.sum_eq_single ⟨m, hm⟩]
  · simp
  · intro b _ hb
    have : (b : ℕ) ≠ m := fun h => hb (Fin.ext h)
    simp [this]
  · intro h
    exact absurd (Finset.mem_univ _) h

theorem sum_zK_sq (k : ℕ) : ∑ j, zK k j ^ 2 = 1 := by
  have h : ∀ j : Fin (2 * k + 1), zK k j ^ 2 = if (j : ℕ) = 2 * k then 1 else 0 := fun j => by
    simp only [zK]
    split_ifs <;> norm_num
  rw [Finset.sum_congr rfl fun j _ => h j]
  exact sum_val_ite (2 * k + 1) (2 * k) (by omega) 1

theorem isNot_nK (k : ℕ) : IsNot (eball (2 * k + 1)) (zK k) (nK k) where
  unit := sum_zK_sq k
  invol x := by
    funext i
    show cK k i * (cK k i * x i) = x i
    rw [← mul_assoc, ← sq, cK_sq, one_mul]
  preserves x hx := by
    rw [mem_eball] at hx ⊢
    have h : ∀ j, (nK k x j) ^ 2 = x j ^ 2 := fun j => by
      show (cK k j * x j) ^ 2 = x j ^ 2
      rw [mul_pow, cK_sq, one_mul]
    rw [Finset.sum_congr rfl fun j _ => h j]
    exact hx
  flips := by
    funext i
    show cK k i * zK k i = -zK k i
    by_cases h : (i : ℕ) = 2 * k
    · have ho : oddK k i.succ = true := by
        unfold oddK
        rw [Fin.val_succ, h]
        exact decide_eq_true (show k < 2 * k + 1 by omega)
      simp [cK, zK, h, ho]
    · simp [zK, h]

/-- The homogeneous vector of a multiple of the corner axis. -/
theorem hom_smul_zK (k : ℕ) (c : ℝ) (μ : Fin (2 * k + 1 + 1)) :
    hom (c • zK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 2 * k + 1 then c else 0 := by
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp
  · rw [hom_succ, Fin.val_succ]
    simp only [Pi.smul_apply, smul_eq_mul, zK]
    split_ifs <;> first | (exfalso; omega) | (norm_num; done)

theorem hom_zK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) :
    hom (zK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 2 * k + 1 then 1 else 0 := by
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp
  · rw [hom_succ, Fin.val_succ]
    simp only [zK]
    split_ifs <;> first | (exfalso; omega) | (norm_num; done)

theorem gRev_frame_aux (k : ℕ) {s t : ℝ} (hs : s = 1 ∨ s = -1) {x y w : Fin (2 * k + 1) → ℝ}
    (hx : x = s • zK k) (hy : y = t • zK k) (hw : w = (s * t) • zK k) :
    gRev k (prodState x y) = prodState x w := by
  subst hx hy hw
  rcases hs with rfl | rfl
  all_goals
    funext μ ν
    have hμ := μ.isLt
    have hν := ν.isLt
    have hr : ((Fin.rev μ : Fin (2 * k + 1 + 1)) : ℕ) = 2 * k + 1 - μ := by
      rw [Fin.val_rev]; omega
    simp only [gRev_apply, sgate, prodState_apply, hom_smul_zK, hr, oddK, decide_eq_true_eq]
    split_ifs <;> first | (exfalso; omega) | (norm_num; done) | ring

/-- **The frame.** `gRev k` acts as the controlled NOT on the corners. -/
theorem gRev_frame (k : ℕ) (a b : Fin 2) :
    gRev k (prodState (corner (zK k) a) (corner (zK k) b)) =
      prodState (corner (zK k) a) (corner (zK k) (a + b)) := by
  fin_cases a <;> fin_cases b
  · exact gRev_frame_aux k (Or.inl rfl) (one_smul ℝ (zK k)).symm (one_smul ℝ (zK k)).symm
      (by rw [one_mul, one_smul]; rfl)
  · exact gRev_frame_aux k (Or.inl rfl) (one_smul ℝ (zK k)).symm (neg_one_smul ℝ (zK k)).symm
      (by rw [one_mul, neg_one_smul]; rfl)
  · exact gRev_frame_aux k (Or.inr rfl) (neg_one_smul ℝ (zK k)).symm (one_smul ℝ (zK k)).symm
      (by rw [mul_one, neg_one_smul]; rfl)
  · exact gRev_frame_aux k (Or.inr rfl) (neg_one_smul ℝ (zK k)).symm (neg_one_smul ℝ (zK k)).symm
      (by rw [neg_one_mul, neg_neg, one_smul]; rfl)

/-- **The relations.** `gRev k` satisfies the target and the control relation with `nK k`. -/
theorem gateRel_gRev (k : ℕ) : GateRel (nK k) (gRev k) :=
  ⟨fun ω => by simp only [gRev_apply]; exact sgate_relT (homMap_nK_sign k) ω,
   fun ω => by simp only [gRev_apply]; exact sgate_relC (homMap_nK_sign k) (oddK_rev k) ω⟩

theorem finrank_plus_eq_finrank_minus_nK (k : ℕ) :
    Module.finrank ℝ (plusSpace (nK k)) = Module.finrank ℝ (minusSpace (nK k)) :=
  finrank_plus_eq_finrank_minus_rel (isNot_nK k) (gateRel_gRev k)

/-! ### §B — the characterization -/

/-- **The odd dimensions.** A NOT, the frame and the two relations exist on `eball d` exactly when
`d` is odd. -/
theorem exists_frame_gateRel_iff_odd (d : ℕ) :
    (∃ (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
      IsNot (eball d) z N ∧
        (∀ a b : Fin 2,
          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧
        GateRel N G) ↔ Odd d := by
  constructor
  · rintro ⟨z, N, G, hN, -, hR⟩
    exact Nat.not_even_iff_odd.mp (not_even_of_gateRel hN hR)
  · rintro ⟨k, hk⟩
    rcases Nat.eq_zero_or_pos k with h0 | _
    · subst h0
      have hd : d = 1 := by omega
      subst hd
      exact ⟨z1, neg1, cnot1, isNot_neg1, cnot1_frame, gateRel_of_nativeGate nativeGate_cnot1⟩
    · subst hk
      exact ⟨zK k, nK k, gRev k, isNot_nK k, gRev_frame k, gateRel_gRev k⟩

/-! ### §C — positivity fails at every odd dimension at least three -/

/-- The first axis of `eball (2k+1)`. -/
def xK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i => if (i : ℕ) = 0 then 1 else 0

/-- The direction of the first sharp effect of the witness: `−(3/5 e_{2k−1} + 4/5 e_{2k})`. -/
noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i =>
  if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0

theorem hom_xK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) :
    hom (xK k) μ = if (μ : ℕ) = 0 then 1 else if (μ : ℕ) = 1 then 1 else 0 := by
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp
  · rw [hom_succ, Fin.val_succ]
    simp only [xK]
    split_ifs <;> first | (exfalso; omega) | (norm_num; done)

theorem sum_xK_sq (k : ℕ) : ∑ j, xK k j ^ 2 = 1 := by
  have h : ∀ j : Fin (2 * k + 1), xK k j ^ 2 = if (j : ℕ) = 0 then 1 else 0 := fun j => by
    simp only [xK]
    split_ifs <;> norm_num
  rw [Finset.sum_congr rfl fun j _ => h j]
  exact sum_val_ite (2 * k + 1) 0 (by omega) 1

theorem sum_wK_sq (k : ℕ) (hk : 1 ≤ k) : ∑ j, wK k j ^ 2 = 1 := by
  have h : ∀ j : Fin (2 * k + 1), wK k j ^ 2 =
      (if (j : ℕ) = 2 * k - 1 then 9 / 25 else 0) + (if (j : ℕ) = 2 * k then 16 / 25 else 0) :=
    fun j => by
      simp only [wK]
      split_ifs <;> first | (exfalso; omega) | (norm_num; done)
  rw [Finset.sum_congr rfl fun j _ => h j, Finset.sum_add_distrib,
    sum_val_ite (2 * k + 1) (2 * k - 1) (by omega) (9 / 25),
    sum_val_ite (2 * k + 1) (2 * k) (by omega) (16 / 25)]
  norm_num

/-- The joint vector with a single unit entry. -/
def entW (p q : Fin (d + 1)) : W d := fun μ ν => if μ = p then (if ν = q then 1 else 0) else 0

theorem pairVal_entW (a b : HVec d) (p q : Fin (d + 1)) : pairVal a b (entW p q) = a p * b q := by
  simp only [pairVal, entW]
  rw [Finset.sum_eq_single p]
  · rw [Finset.sum_eq_single q]
    · simp
    · intro c _ hc
      simp [hc]
    · intro h
      exact absurd (Finset.mem_univ q) h
  · intro c _ hc
    apply Finset.sum_eq_zero
    intro ν _
    simp [hc]
  · intro h
    exact absurd (Finset.mem_univ p) h

/-- The image of the product of the first axis with the corner pairs to `−1/10` with the sharp
effects of `wK k` and the corner. -/
theorem gRev_value (k : ℕ) (hk : 1 ≤ k) :
    prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = -1 / 10 := by
  have h0 : 0 < 2 * k + 1 := by omega
  have h1 : 2 * k - 1 < 2 * k + 1 := by omega
  have h2 : 2 * k < 2 * k + 1 := by omega
  have hω : gRev k (prodState (xK k) (zK k)) =
      entW 0 0 + entW (Fin.succ ⟨0, h0⟩) 0 + entW (Fin.succ ⟨2 * k - 1, h1⟩) (Fin.succ ⟨2 * k, h2⟩)
        + entW (Fin.succ ⟨2 * k, h2⟩) (Fin.succ ⟨2 * k, h2⟩) := by
    funext μ ν
    have hμ := μ.isLt
    have hν := ν.isLt
    have hr : ((Fin.rev μ : Fin (2 * k + 1 + 1)) : ℕ) = 2 * k + 1 - μ := by
      rw [Fin.val_rev]; omega
    simp only [gRev_apply, sgate, prodState_apply, hom_xK, hom_zK, hr, oddK, decide_eq_true_eq,
      entW, Pi.add_apply, Fin.ext_iff, Fin.val_succ, Fin.val_zero, Fin.val_mk, zero_add]
    split_ifs <;> first | (exfalso; omega) | (norm_num; done)
  rw [prodEffVal_sharp, hω, pairVal_add_omega, pairVal_add_omega, pairVal_add_omega, pairVal_entW,
    pairVal_entW, pairVal_entW, pairVal_entW]
  simp only [sharpVec_zero, sharpVec_succ, wK, zK, Fin.val_mk]
  split_ifs <;> first | (exfalso; omega) | (norm_num; done)

theorem gRev_not_mem_maxCone (k : ℕ) (hk : 1 ≤ k) :
    gRev k (prodState (xK k) (zK k)) ∉ maxCone (eball (2 * k + 1)) := fun h => by
  have hv := h _ _ (sharpEff_isEffectOn (sum_wK_sq k hk)) (sharpEff_isEffectOn (sum_zK_sq k))
  rw [gRev_value k hk] at hv
  norm_num at hv

/-- **At every odd dimension at least three, the frame and the relations hold and forward
positivity fails.** -/
theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :
    ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈ eball (2 * k + 1),
      gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1)) :=
  fun h => gRev_not_mem_maxCone k hk
    (h _ (mem_eball_of_sphere (sum_xK_sq k)) _ (mem_eball_of_sphere (sum_zK_sq k)))

theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :
    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k) :=
  fun hG => not_posFwd_gRev k hk hG.posFwd

end OddChar
end OIBridge

#print axioms OIBridge.OddChar.oddK_rev
#print axioms OIBridge.OddChar.isNot_nK
#print axioms OIBridge.OddChar.gRev_frame
#print axioms OIBridge.OddChar.gateRel_gRev
#print axioms OIBridge.OddChar.finrank_plus_eq_finrank_minus_nK
#print axioms OIBridge.OddChar.exists_frame_gateRel_iff_odd
#print axioms OIBridge.OddChar.sum_wK_sq
#print axioms OIBridge.OddChar.pairVal_entW
#print axioms OIBridge.OddChar.gRev_value
#print axioms OIBridge.OddChar.gRev_not_mem_maxCone
#print axioms OIBridge.OddChar.not_posFwd_gRev
#print axioms OIBridge.OddChar.not_nativeGate_gRev
