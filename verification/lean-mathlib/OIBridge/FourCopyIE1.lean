/-
  OIBridge/FourCopyIE1.lean — design (EQ4-F), not adopted: the sub-lemmas of the Pauli-free route
  KT(4) → IE₁ ∧ parity, with the helper lemmas they read. No complex number, Pauli matrix or PSD
  cone is used, and no proof in this file uses `sorry`.

  * Rotation facts: orthogonal maps of determinant `1` are rotations, rotations compose, the
    generators `rot3 t` and `rotX t` are rotations, the transpose keeps the determinant, and the
    chart `A · reflY · Bᵀ` has determinant `-(det A · det B)`.
  * G5, G6: the cross relations `K = Θ '' K'*` and `K' = Θ⁻¹ '' K*` for a target in the form of
    Lemma R (`PairLinked`), from Bell tables in the link cones and in their duals.
  * G7: rotation links. `cnot` commutes with rotations about the third axis on the control token
    and about the first axis on the target token; on a product of rotated pure states it gives a
    rotated Bell table (G7(ii)), which reads the same on either token (G7(iii)); the gate images
    of products supply these tables in every pair cone (`link_mem`).
  * G9: invariance of a target cone (control side) and of its partner's dual (target side) under
    the conjugated rotation words carried by the links.
  * G10: the conjugated words generate the rotations (Euler, O39).
  * G11: inclusion under every rotation gives image equality.
  * G12: IE₁ passes to the dual cone; for a cone equal to its bidual it passes back.
  * G14: Lemma P with its four memberships as hypotheses (`kt4_parity_of_witnesses`), and the
    witnesses (`parity_witnesses`): a rotation carries the Bell table of the post-locals to the
    Bell table of the pair's orientation bit, `idW` or `phiW`; the rotation by `π` about the
    second axis (`rotYpi`) carries the image of `(xplus, z3)` to the image of `(-xplus, -z3)`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyCore
import OIBridge.FourCopyLocal
import OIBridge.FourCopyEuler
import OIBridge.FourCopyTables

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody OrbitNormalization

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### Rotation facts -/

theorem isOrth3_of_isRot3 {R : E3} (hR : IsRot3 R) : IsOrth3 R := by
  unfold IsRot3 at hR
  unfold IsOrth3
  exact (Matrix.mem_specialOrthogonalGroup_iff.1 hR).1

theorem isRot3_trn {R : E3} (hR : IsRot3 R) : IsRot3 (trn R) := by
  unfold IsRot3 at hR ⊢
  rw [toMatrix'_trn]
  obtain ⟨hO, hdet⟩ := Matrix.mem_specialOrthogonalGroup_iff.1 hR
  rw [Matrix.mem_specialOrthogonalGroup_iff, Matrix.mem_orthogonalGroup_iff,
    Matrix.transpose_transpose, Matrix.det_transpose]
  exact ⟨(Matrix.mem_orthogonalGroup_iff' _ _).1 hO, hdet⟩

/-- The conjugate of a rotation by an orthogonal map is a rotation. -/
theorem isRot3_conj {A R : E3} (hA : IsOrth3 A) (hR : IsRot3 R) :
    IsRot3 (trn A ∘ₗ R ∘ₗ A) := by
  unfold IsRot3 at hR ⊢
  unfold IsOrth3 at hA
  rw [LinearMap.toMatrix'_comp, LinearMap.toMatrix'_comp, toMatrix'_trn]
  obtain ⟨hRO, hRdet⟩ := Matrix.mem_specialOrthogonalGroup_iff.1 hR
  have hAtA := (Matrix.mem_orthogonalGroup_iff' _ _).1 hA
  have hd : (LinearMap.toMatrix' A).det * (LinearMap.toMatrix' A).det = 1 := by
    have h := congrArg Matrix.det hAtA
    rwa [Matrix.det_mul, Matrix.det_transpose, Matrix.det_one] at h
  rw [Matrix.mem_specialOrthogonalGroup_iff]
  refine ⟨Submonoid.mul_mem _ ?_ (Submonoid.mul_mem _ hRO hA), ?_⟩
  · rw [Matrix.mem_orthogonalGroup_iff, Matrix.transpose_transpose]
    exact hAtA
  · rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose, hRdet]
    linear_combination hd

theorem rotX_zero_apply (v : Fin 3 → ℝ) : ((rotX 0).linear : E3) v = v := by
  rw [rotX_linear_apply, rotFun_zero, LinearEquiv.apply_symm_apply]

theorem trn_rot3 (t : ℝ) : trn ((rot3 t).linear : E3) = ((rot3 (-t)).linear : E3) := by
  apply LinearMap.toMatrix'.injective
  rw [toMatrix'_trn, toMatrix'_rot3, toMatrix'_rot3]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Rz]

theorem trn_rotX (t : ℝ) : trn ((rotX t).linear : E3) = ((rotX (-t)).linear : E3) := by
  apply LinearMap.toMatrix'.injective
  rw [toMatrix'_trn, toMatrix'_rotX, toMatrix'_rotX]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Rx]

/-- The transpose of a reversed word is a word. -/
theorem trn_rotWord' (a b : ℝ) : trn (rotWord' a b) = rotWord (-a) (-b) := by
  rw [rotWord', rotWord, trn_comp, trn_rot3, trn_rotX]

/-- An orthogonal map of determinant `1` is a rotation. -/
theorem isRot3_of_det {R : E3} (hO : IsOrth3 R) (hd : LinearMap.det R = 1) : IsRot3 R := by
  unfold IsRot3
  unfold IsOrth3 at hO
  rw [Matrix.mem_specialOrthogonalGroup_iff]
  exact ⟨hO, by rw [LinearMap.det_toMatrix']; exact hd⟩

theorem isRot3_comp {R S : E3} (hR : IsRot3 R) (hS : IsRot3 S) : IsRot3 (R ∘ₗ S) := by
  unfold IsRot3 at *
  rw [LinearMap.toMatrix'_comp]
  exact Submonoid.mul_mem _ hR hS

theorem isRot3_rot3 (t : ℝ) : IsRot3 ((rot3 t).linear : E3) := by
  unfold IsRot3
  rw [toMatrix'_rot3]
  exact Rz_mem t

theorem isRot3_rotX (t : ℝ) : IsRot3 ((rotX t).linear : E3) := by
  unfold IsRot3
  rw [toMatrix'_rotX]
  exact Rx_mem t

theorem det_trn (A : E3) : LinearMap.det (trn A) = LinearMap.det A := by
  first
  | rw [trn, LinearMap.det_toLin', Matrix.det_transpose, LinearMap.det_toMatrix']
  | rw [← LinearMap.det_toMatrix', ← LinearMap.det_toMatrix', toMatrix'_trn, Matrix.det_transpose]

/-- The chart of a Bell table has determinant `-(det A · det B)`. -/
theorem det_chartOf (A B : E3) :
    LinearMap.det (chartOf A B) = -(LinearMap.det A * LinearMap.det B) := by
  rw [chartOf, LinearMap.det_comp, LinearMap.det_comp, det_reflY, det_trn]
  ring

theorem det_mul_self_of_orth {A : E3} (hA : IsOrth3 A) :
    LinearMap.det A * LinearMap.det A = 1 := by
  unfold IsOrth3 at hA
  have h := congrArg Matrix.det ((Matrix.mem_orthogonalGroup_iff' _ _).1 hA)
  rw [Matrix.det_mul, Matrix.det_transpose, Matrix.det_one, LinearMap.det_toMatrix'] at h
  exact h

theorem rot3_eq_linear (t : ℝ) (v : Fin 3 → ℝ) : rot3 t v = ((rot3 t).linear : E3) v := by
  rw [rot3_apply, rot3_linear_apply]

theorem rotX_eq_linear (t : ℝ) (v : Fin 3 → ℝ) : rotX t v = ((rotX t).linear : E3) v := by
  first
  | (rw [rotX_linear_apply, rotX, OrbitNormalization.mul_apply', OrbitNormalization.mul_apply',
      OrbitNormalization.inv_apply', rot3_apply] <;> rfl)
  | rfl

theorem rot3_xplus_mem (t : ℝ) : rot3 t xplus ∈ eball 3 := by
  rw [rot3_eq_linear]
  exact orth_mem_eball (isOrth3_of_isRot3 (isRot3_rot3 t)) xplus_mem

theorem rotX_z3_mem (t : ℝ) : rotX t z3 ∈ eball 3 := by
  rw [rotX_eq_linear]
  exact orth_mem_eball (isOrth3_of_isRot3 (isRot3_rotX t)) z3_mem

/-! ### G5, G6 — the cross relations -/

/-- **G5.** A target cone is the Θ-image of its partner's dual, for Bell tables of orthogonal
locals in the link cones and in their duals. Inclusion (I) and the bipolar give `⊇`; inclusion
(II) and the orthogonality of Θ give `⊆`. -/
theorem cross_rel {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) {Aa Ba Ab Bb : E3} (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba)
    (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb) (sa : bellOf Aa Ba ∈ La) (sb : bellOf Ab Bb ∈ Lb)
    (ea : bellOf Aa Ba ∈ dualW La) (eb : bellOf Ab Bb ∈ dualW Lb) :
    K = Theta Aa Ba Ab Bb '' dualW K' := by
  apply Set.Subset.antisymm
  · intro X hX
    refine ⟨ThetaInv Aa Ba Ab Bb X, mem_dualW.2 fun Y hY => ?_, Theta_ThetaInv h1 h2 h3 h4 X⟩
    have h5 := Theta_ipW h1 h2 h3 h4 (ThetaInv Aa Ba Ab Bb X) Y
    rw [Theta_ThetaInv h1 h2 h3 h4] at h5
    rw [← h5]
    exact h.upper X hX Y hY _ ea _ eb
  · rintro _ ⟨f, hf, rfl⟩
    rw [← hbi]
    refine mem_dualW.2 fun e he => ?_
    rw [ipW_comm]
    exact h.lower _ sa _ sb e he f hf

/-- **G6.** The partner cone is the Θ⁻¹-image of the target's dual. Read by the classification
(the squeeze), not by `kt4_general_ie1`. -/
theorem cross_rel_symm {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) (hbi' : dualW (dualW K') = K') {Aa Ba Ab Bb : E3}
    (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba) (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb)
    (sa : bellOf Aa Ba ∈ La) (sb : bellOf Ab Bb ∈ Lb)
    (ea : bellOf Aa Ba ∈ dualW La) (eb : bellOf Ab Bb ∈ dualW Lb) :
    K' = ThetaInv Aa Ba Ab Bb '' dualW K := by
  have hKΘ := cross_rel h hbi h1 h2 h3 h4 sa sb ea eb
  apply Set.Subset.antisymm
  · intro Y hY
    refine ⟨Theta Aa Ba Ab Bb Y, mem_dualW.2 fun X hX => ?_, ThetaInv_Theta h1 h2 h3 h4 Y⟩
    rw [hKΘ] at hX
    obtain ⟨f, hf, rfl⟩ := hX
    rw [Theta_ipW h1 h2 h3 h4, ipW_comm Y f]
    exact mem_dualW.1 hf Y hY
  · rintro _ ⟨E, hE, rfl⟩
    rw [← hbi']
    refine mem_dualW.2 fun f hf => ?_
    have hfK : Theta Aa Ba Ab Bb f ∈ K := by
      rw [hKΘ]
      exact ⟨f, hf, rfl⟩
    have h5 := Theta_ipW h1 h2 h3 h4 f (ThetaInv Aa Ba Ab Bb E)
    rw [Theta_ThetaInv h1 h2 h3 h4] at h5
    rw [ipW_comm (ThetaInv Aa Ba Ab Bb E) f, ← h5, ipW_comm (Theta Aa Ba Ab Bb f) E]
    exact mem_dualW.1 hE _ hfK

/-! ### G7 — rotation links -/

theorem homMap_rot3_one (t : ℝ) (v : HVec 3) :
    homMap ((rot3 t).linear : E3) v 1 = Real.cos t * v 1 - Real.sin t * v 2 := by
  first
  | rfl
  | exact (homMap_succ ((rot3 t).linear : E3) v 0).trans (rotFun_apply t (Matrix.vecTail v)).1

theorem homMap_rot3_two (t : ℝ) (v : HVec 3) :
    homMap ((rot3 t).linear : E3) v 2 = Real.sin t * v 1 + Real.cos t * v 2 := by
  first
  | rfl
  | exact (homMap_succ ((rot3 t).linear : E3) v 1).trans (rotFun_apply t (Matrix.vecTail v)).2.1

theorem homMap_rot3_three (t : ℝ) (v : HVec 3) : homMap ((rot3 t).linear : E3) v 3 = v 3 := by
  first
  | rfl
  | exact (homMap_succ ((rot3 t).linear : E3) v 2).trans (rotFun_apply t (Matrix.vecTail v)).2.2

theorem homMap_rotX_one (t : ℝ) (v : HVec 3) : homMap ((rotX t).linear : E3) v 1 = v 1 := by
  first
  | rfl
  | exact (homMap_succ ((rotX t).linear : E3) v 0).trans
      (rotFun_apply t (cycEquiv.symm (Matrix.vecTail v))).2.2

theorem homMap_rotX_two (t : ℝ) (v : HVec 3) :
    homMap ((rotX t).linear : E3) v 2 = Real.cos t * v 2 - Real.sin t * v 3 := by
  first
  | rfl
  | exact (homMap_succ ((rotX t).linear : E3) v 1).trans
      (rotFun_apply t (cycEquiv.symm (Matrix.vecTail v))).1

theorem homMap_rotX_three (t : ℝ) (v : HVec 3) :
    homMap ((rotX t).linear : E3) v 3 = Real.sin t * v 2 + Real.cos t * v 3 := by
  first
  | rfl
  | exact (homMap_succ ((rotX t).linear : E3) v 2).trans
      (rotFun_apply t (cycEquiv.symm (Matrix.vecTail v))).2.1

set_option maxHeartbeats 1000000 in
/-- `cnot` commutes with a rotation about the third axis on the control token. -/
theorem cnot_actC_rot3 (t : ℝ) (ω : W 3) :
    cnot (actC ((rot3 t).linear : E3) ω) = actC ((rot3 t).linear : E3) (cnot ω) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actC_apply, cnot_apply, cnotFun_apply, sgn, pc, pt, homMap_rot3_one,
      homMap_rot3_two, homMap_rot3_three] <;> ring

set_option maxHeartbeats 1000000 in
/-- `cnot` commutes with a rotation about the first axis on the target token. -/
theorem cnot_actT_rotX (t : ℝ) (ω : W 3) :
    cnot (actT ((rotX t).linear : E3) ω) = actT ((rotX t).linear : E3) (cnot ω) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actT_apply, cnot_apply, cnotFun_apply, sgn, pc, pt, homMap_rotX_one,
      homMap_rotX_two, homMap_rotX_three] <;> ring

/-- A rotation about the third axis reads the same on either token of `phiW`. -/
theorem actT_rot3_phiW (t : ℝ) :
    actT ((rot3 t).linear : E3) phiW = actC ((rot3 t).linear : E3) phiW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actT_apply, actC_apply, phiW, homMap_rot3_one, homMap_rot3_two,
      homMap_rot3_three]

/-- A rotation about the first axis reads the same on either token of `phiW`. -/
theorem actT_rotX_phiW (t : ℝ) :
    actT ((rotX t).linear : E3) phiW = actC ((rotX t).linear : E3) phiW := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actT_apply, actC_apply, phiW, homMap_rotX_one, homMap_rotX_two,
      homMap_rotX_three]

/-- **G7(ii).** `cnot` on a product of rotated pure states is a rotated Bell table. -/
theorem cnot_prodState_rot (a b : ℝ) :
    cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rotWord a b) phiW := by
  rw [rot3_eq_linear, rotX_eq_linear, ← actC_prodState, ← actT_prodState, cnot_actC_rot3,
    cnot_actT_rotX, cnot_prodState_xplus_z3, actT_rotX_phiW, actC_comp, rotWord]

/-- **G7(iii).** The same table read on the target token. -/
theorem actC_rotWord_phiW (a b : ℝ) : actC (rotWord a b) phiW = actT (rotWord' a b) phiW := by
  rw [rotWord', ← actT_comp, actT_rot3_phiW, ← actC_actT_comm, actT_rotX_phiW, actC_comp,
    rotWord]

/-- **G7.** The links of a pair: gate images of products of the ball, in control-side and
target-side form. -/
theorem link_mem {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hprod : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hgate : ∀ ω ∈ K, N ω ∈ K) (a b : ℝ) :
    actC (A ∘ₗ rotWord a b) (actT B phiW) ∈ K ∧
      actC A (actT (B ∘ₗ rotWord' a b) phiW) ∈ K := by
  have h1 : actC (A ∘ₗ rotWord a b) (actT B phiW) ∈ K := by
    have hmem := hgate _ (hprod _ (orth_mem_eball (isOrth3_trn hcls.2.2.1) (rot3_xplus_mem a)) _
      (orth_mem_eball (isOrth3_trn hcls.2.2.2.1) (rotX_z3_mem b)))
    rw [hcls.apply_prodState, cnot_prodState_rot, ← actC_actT_comm, actC_comp] at hmem
    exact hmem
  refine ⟨h1, ?_⟩
  rw [← actT_comp, ← actC_rotWord_phiW, ← actC_actT_comm, actC_comp]
  exact h1

/-! ### G9 — invariance carried by the links -/

/-- **G9a.** A control-side link on the left: the target cone is invariant under the conjugated
map `Aa · M · Aaᵀ` on its first token. -/
theorem inv_left_ctrl {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) {Aa Ba Ab Bb : E3} (hA : IsOrth3 Aa)
    (hKΘ : K = Theta Aa Ba Ab Bb '' dualW K') {M : E3}
    (hL : actC (Aa ∘ₗ M) (actT Ba phiW) ∈ La) (hb : bellOf Ab Bb ∈ Lb) :
    ∀ X ∈ K, actC (Aa ∘ₗ M ∘ₗ trn Aa) X ∈ K := by
  intro X hX
  rw [hKΘ] at hX
  obtain ⟨f, hf, rfl⟩ := hX
  rw [← hbi]
  refine mem_dualW.2 fun e he => ?_
  rw [ipW_comm, ← link_left_ctrl hA]
  exact h.lower _ hL _ hb e he f hf

/-- **G9b.** A control-side link on the right: invariance on the second token. -/
theorem inv_right_ctrl {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) {Aa Ba Ab Bb : E3} (hA : IsOrth3 Ab)
    (hKΘ : K = Theta Aa Ba Ab Bb '' dualW K') {M : E3}
    (ha : bellOf Aa Ba ∈ La) (hL : actC (Ab ∘ₗ M) (actT Bb phiW) ∈ Lb) :
    ∀ X ∈ K, actT (Ab ∘ₗ M ∘ₗ trn Ab) X ∈ K := by
  intro X hX
  rw [hKΘ] at hX
  obtain ⟨f, hf, rfl⟩ := hX
  rw [← hbi]
  refine mem_dualW.2 fun e he => ?_
  rw [ipW_comm, ← link_right_ctrl Aa Ba hA]
  exact h.lower _ ha _ hL e he f hf

/-- **G9c.** A target-side link on the left: the partner's dual is invariant under the
conjugated map `Ba · Mᵀ · Baᵀ` on its first token. -/
theorem inv_left_partner {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) {Aa Ba Ab Bb : E3} (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba)
    (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb) (hKΘ : K = Theta Aa Ba Ab Bb '' dualW K') {M : E3}
    (hL : actC Aa (actT (Ba ∘ₗ M) phiW) ∈ La) (hb : bellOf Ab Bb ∈ Lb) :
    ∀ f ∈ dualW K', actC (Ba ∘ₗ trn M ∘ₗ trn Ba) f ∈ dualW K' := by
  intro f hf
  have hmem : Theta Aa Ba Ab Bb (actC (Ba ∘ₗ trn M ∘ₗ trn Ba) f) ∈ K := by
    rw [← hbi]
    refine mem_dualW.2 fun e he => ?_
    rw [ipW_comm, ← link_left_target Aa h2]
    exact h.lower _ hL _ hb e he f hf
  rw [hKΘ] at hmem
  obtain ⟨g, hg, hgeq⟩ := hmem
  have hinj := congrArg (ThetaInv Aa Ba Ab Bb) hgeq
  rw [ThetaInv_Theta h1 h2 h3 h4, ThetaInv_Theta h1 h2 h3 h4] at hinj
  rw [← hinj]
  exact hg

/-- **G9d.** A target-side link on the right: invariance of the partner's dual on its second
token. -/
theorem inv_right_partner {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb)
    (hbi : dualW (dualW K) = K) {Aa Ba Ab Bb : E3} (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba)
    (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb) (hKΘ : K = Theta Aa Ba Ab Bb '' dualW K') {M : E3}
    (ha : bellOf Aa Ba ∈ La) (hL : actC Ab (actT (Bb ∘ₗ M) phiW) ∈ Lb) :
    ∀ f ∈ dualW K', actT (Bb ∘ₗ trn M ∘ₗ trn Bb) f ∈ dualW K' := by
  intro f hf
  have hmem : Theta Aa Ba Ab Bb (actT (Bb ∘ₗ trn M ∘ₗ trn Bb) f) ∈ K := by
    rw [← hbi]
    refine mem_dualW.2 fun e he => ?_
    rw [ipW_comm, ← link_right_target Aa Ba Ab h4]
    exact h.lower _ ha _ hL e he f hf
  rw [hKΘ] at hmem
  obtain ⟨g, hg, hgeq⟩ := hmem
  have hinj := congrArg (ThetaInv Aa Ba Ab Bb) hgeq
  rw [ThetaInv_Theta h1 h2 h3 h4, ThetaInv_Theta h1 h2 h3 h4] at hinj
  rw [← hinj]
  exact hg

/-! ### G10, G11, G12 — from the words to IE₁ -/

/-- **G10.** A property of one-copy maps closed under composition that holds for every word
`A · (rot3 a · rotX b) · Aᵀ` (A orthogonal) holds for every rotation. -/
theorem rot_of_words {P : E3 → Prop} (hmul : ∀ M N, P M → P N → P (M ∘ₗ N)) {A : E3}
    (hA : IsOrth3 A) (hgen : ∀ a b : ℝ, P (A ∘ₗ rotWord a b ∘ₗ trn A)) :
    ∀ R, IsRot3 R → P R := by
  intro R hR
  obtain ⟨ψ, θ, φ, hE⟩ := so3_euler (isRot3_conj hA hR)
  have key : R = (A ∘ₗ rotWord ψ θ ∘ₗ trn A) ∘ₗ (A ∘ₗ rotWord φ 0 ∘ₗ trn A) := by
    refine LinearMap.ext fun x => ?_
    have h1 := congrArg (fun F : E3 => A (F (trn A x))) hE
    simp only [LinearMap.comp_apply, apply_trn_apply hA] at h1
    simp only [LinearMap.comp_apply, rotWord, trn_apply_apply hA, rotX_zero_apply]
    exact h1
  rw [key]
  exact hmul _ _ (hgen ψ θ) (hgen φ 0)

/-- **G10′.** The same for the transposed reversed words `A · (rotX b · rot3 a)ᵀ · Aᵀ`. -/
theorem rot_of_words' {P : E3 → Prop} (hmul : ∀ M N, P M → P N → P (M ∘ₗ N)) {A : E3}
    (hA : IsOrth3 A) (hgen : ∀ a b : ℝ, P (A ∘ₗ trn (rotWord' a b) ∘ₗ trn A)) :
    ∀ R, IsRot3 R → P R :=
  rot_of_words hmul hA fun a b => by
    have h := hgen (-a) (-b)
    rwa [trn_rotWord', neg_neg, neg_neg] at h

/-- **G11.** Inclusion under every rotation gives image equality. -/
theorem image_eq_of_rot {K : Set (W 3)} {act : E3 → W 3 → W 3}
    (hcomp : ∀ M N ω, act M (act N ω) = act (M ∘ₗ N) ω) (hid : ∀ ω, act LinearMap.id ω = ω)
    (h : ∀ R, IsRot3 R → ∀ ω ∈ K, act R ω ∈ K) : ∀ R, IsRot3 R → act R '' K = K := by
  intro R hR
  apply Set.Subset.antisymm
  · rintro _ ⟨ω, hω, rfl⟩
    exact h R hR ω hω
  · intro ω hω
    refine ⟨act (trn R) ω, h (trn R) (isRot3_trn hR) ω hω, ?_⟩
    rw [hcomp, comp_trn_self (isOrth3_of_isRot3 hR), hid]

/-- **G12.** IE₁ passes to the dual cone. -/
theorem ie1_dualW {K : Set (W 3)} (h : IE1 K) : IE1 (dualW K) := by
  have hC : ∀ R, IsRot3 R → ∀ E ∈ dualW K, actC R E ∈ dualW K := by
    intro R hR E hE
    refine mem_dualW.2 fun X hX => ?_
    have hX' : actC (trn R) X ∈ K := by
      rw [← (h (trn R) (isRot3_trn hR)).1]
      exact ⟨X, hX, rfl⟩
    have h1 := mem_dualW.1 hE _ hX'
    rwa [ipW_actC, trn_trn] at h1
  have hT : ∀ R, IsRot3 R → ∀ E ∈ dualW K, actT R E ∈ dualW K := by
    intro R hR E hE
    refine mem_dualW.2 fun X hX => ?_
    have hX' : actT (trn R) X ∈ K := by
      rw [← (h (trn R) (isRot3_trn hR)).2]
      exact ⟨X, hX, rfl⟩
    have h1 := mem_dualW.1 hE _ hX'
    rwa [ipW_actT, trn_trn] at h1
  exact fun R hR => ⟨image_eq_of_rot (act := actC) actC_comp actC_id hC R hR,
    image_eq_of_rot (act := actT) actT_comp actT_id hT R hR⟩

/-- **G12′.** IE₁ of the dual of a cone equal to its bidual gives IE₁ of the cone. -/
theorem ie1_of_dualW {K : Set (W 3)} (hbi : dualW (dualW K) = K) (h : IE1 (dualW K)) :
    IE1 K := by
  rw [← hbi]
  exact ie1_dualW h

/-! ### G14 — the orientation parity -/

set_option maxHeartbeats 1000000 in
/-- **G14a. Lemma P with memberships as hypotheses.** The computation of `kt4_parity_aligned`:
the states `gateOf τ (prodState xplus z3)` on pairs `01`, `23` and the gate images of the sharp
products `(xplus, z3)` on pair `02` and `(-xplus, -z3)` on pair `13`, as members of the cones
and duals, force even parity of the twist bits. -/
theorem kt4_parity_of_witnesses {K01 K23 K02 K13 : Set (W 3)} {τ01 τ23 τ02 τ13 : Bool}
    (hX : gateOf τ01 (prodState xplus z3) ∈ K01) (hY : gateOf τ23 (prodState xplus z3) ∈ K23)
    (hE : gateOf τ02 (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K02)
    (hF : gateOf τ13 (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K13)
    (h : FourCopyCoherent K01 K23 K02 K13) : EvenCycle4 τ01 τ23 τ02 τ13 := by
  have hv := h.famI _ hX _ hY _ hE _ hF
  simp only [gateOf_sharp, gateOf_prodState_xplus_z3, gateOf_prodState_neg, ipW_dg_smul] at hv
  revert hv
  cases τ01 <;> cases τ23 <;> cases τ02 <;> cases τ13 <;> norm_num [sgnB, EvenCycle4, Bool.toNat]

theorem tabMul_idW (X : W 3) : tabMul X idW = X := by
  rw [idW_eq_dg]
  funext μ ν
  fin_cases ν <;> simp [tabMul, dg, sum_univ_four']

theorem actC_reflY_idW : actC reflY idW = phiW := by
  rw [← tabMul_phiW_left, tabMul_idW]

/-- The Bell table of the post-locals is the identity table in the chart `A · reflY · Bᵀ`. -/
theorem bellOf_eq_actC (A B : E3) : bellOf A B = actC (chartOf A B) idW := by
  have h : tabMul (bellOf A B) idW = actC (chartOf A B) idW := by
    rw [bellOf, tabMul_actC_left, tabMul_actT_left, tabMul_phiW_left, actC_comp, actC_comp,
      LinearMap.comp_assoc, chartOf]
  rw [← h, tabMul_idW]

/-- The rotation by `π` about the second axis, `diag(-1, 1, -1)`. -/
def rotYpi : E3 where
  toFun x := fun i => (![-1, 1, -1] : Fin 3 → ℝ) i * x i
  map_add' x y := by funext i; simp only [Pi.add_apply, mul_add]
  map_smul' c x := by funext i; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; ring

theorem rotYpi_apply (x : Fin 3 → ℝ) (i : Fin 3) :
    rotYpi x i = (![-1, 1, -1] : Fin 3 → ℝ) i * x i := rfl

theorem homMap_rotYpi_one (v : HVec 3) : homMap rotYpi v 1 = -v 1 := by
  show -1 * v 1 = -v 1; ring

theorem homMap_rotYpi_two (v : HVec 3) : homMap rotYpi v 2 = v 2 := by
  show 1 * v 2 = v 2; ring

theorem homMap_rotYpi_three (v : HVec 3) : homMap rotYpi v 3 = -v 3 := by
  show -1 * v 3 = -v 3; ring

theorem rotYpi_eq_toLin' :
    rotYpi = Matrix.toLin' (Matrix.diagonal (![-1, 1, -1] : Fin 3 → ℝ)) := by
  refine LinearMap.ext fun x => funext fun i => ?_
  rw [Matrix.toLin'_apply, Matrix.mulVec_diagonal, rotYpi_apply]

theorem isRot3_rotYpi : IsRot3 rotYpi := by
  have hO : IsOrth3 rotYpi := by
    unfold IsOrth3
    rw [rotYpi_eq_toLin', LinearMap.toMatrix'_toLin', Matrix.mem_orthogonalGroup_iff,
      Matrix.diagonal_transpose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
    congr 1
    funext i
    fin_cases i <;> norm_num
  refine isRot3_of_det hO ?_
  rw [rotYpi_eq_toLin', LinearMap.det_toLin', Matrix.det_diagonal, Fin.prod_univ_three]
  simp

theorem actC_rotYpi_dg (p q r s : ℝ) : actC rotYpi (dg p q r s) = dg p (-q) r (-s) := by
  funext μ ν
  fin_cases μ <;> fin_cases ν <;>
    simp +decide [actC_apply, dg, homMap_rotYpi_one, homMap_rotYpi_two, homMap_rotYpi_three]

/-- `rotYpi` on the control token carries the gate image of `(xplus, z3)` to the gate image of
`(-xplus, -z3)`. -/
theorem gateOf_neg_eq (τ : Bool) :
    gateOf τ (prodState (-xplus) (-z3)) = actC rotYpi (gateOf τ (prodState xplus z3)) := by
  rw [gateOf_prodState_neg, gateOf_prodState_xplus_z3, actC_rotYpi_dg]

theorem smul_mem_dualW {K : Set (W 3)} {c : ℝ} (hc : 0 ≤ c) {E : W 3} (hE : E ∈ dualW K) :
    c • E ∈ dualW K :=
  mem_dualW.2 fun X hX => by
    rw [ipW_smul_left]
    exact mul_nonneg hc (mem_dualW.1 hE X hX)

theorem actC_mem_of_ie1 {K : Set (W 3)} (h : IE1 K) {R : E3} (hR : IsRot3 R) {X : W 3}
    (hX : X ∈ K) : actC R X ∈ K := by
  rw [← (h R hR).1]
  exact ⟨X, hX, rfl⟩

/-- **G14b.** Under IE₁ a rotation carries the Bell table of the post-locals of an N-CLASS gate to
the Bell table of the pair's orientation bit, and Lemma P's witnesses become memberships of the
cone and, by G12, of its dual. -/
theorem parity_witnesses {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3))
    (hprod : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hgate : ∀ ω ∈ K, N ω ∈ K) (hinv : ∀ ω ∈ K, N.symm ω ∈ K) (hie : IE1 K) :
    gateOf (orient A B) (prodState xplus z3) ∈ K ∧
      gateOf (orient A B) (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K ∧
      gateOf (orient A B) (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K := by
  have hA : IsOrth3 A := hcls.1
  have hB : IsOrth3 B := hcls.2.1
  have hC : IsOrth3 (chartOf A B) := isOrth3_chartOf hA hB
  have hbs : bellOf A B ∈ K := bell_mem hcls hprod hgate
  have hbe : bellOf A B ∈ dualW K := bell_mem_dual hcls hK hinv
  obtain ⟨R, hR, hRH⟩ : ∃ R : E3, IsRot3 R ∧
      actC R (bellOf A B) = gateOf (orient A B) (prodState xplus z3) := by
    by_cases hD : LinearMap.det A * LinearMap.det B = -1
    · have ho : orient A B = true := decide_eq_true hD
      rw [ho, gateOf_true, cnotTw_prodState_xplus_z3, bellOf_eq_actC]
      refine ⟨trn (chartOf A B), isRot3_trn (isRot3_of_det hC ?_), ?_⟩
      · linarith [det_chartOf A B]
      · rw [actC_comp, trn_comp_self hC, actC_id]
    · have ho : orient A B = false := decide_eq_false hD
      have hsq : (LinearMap.det A * LinearMap.det B - 1) *
          (LinearMap.det A * LinearMap.det B + 1) = 0 := by
        linear_combination (LinearMap.det B * LinearMap.det B) * det_mul_self_of_orth hA +
          det_mul_self_of_orth hB
      have hD1 : LinearMap.det A * LinearMap.det B = 1 := by
        rcases mul_eq_zero.1 hsq with h | h
        · linarith
        · exact (hD (by linarith)).elim
      rw [ho, gateOf_false, cnot_prodState_xplus_z3, bellOf_eq_actC]
      refine ⟨reflY ∘ₗ trn (chartOf A B),
        isRot3_of_det (isOrth3_comp isOrth3_reflY (isOrth3_trn hC)) ?_, ?_⟩
      · rw [LinearMap.det_comp, det_reflY, det_trn, det_chartOf, hD1]
        norm_num
      · rw [actC_comp, LinearMap.comp_assoc, trn_comp_self hC, LinearMap.comp_id,
          actC_reflY_idW]
  have hRd : ∀ S : E3, IsRot3 S → actC S (bellOf A B) ∈ dualW K := fun S hS =>
    actC_mem_of_ie1 (ie1_dualW hie) hS hbe
  refine ⟨?_, ?_, ?_⟩
  · rw [← hRH]
    exact actC_mem_of_ie1 hie hR hbs
  · rw [gateOf_sharp, ← hRH]
    exact smul_mem_dualW (by norm_num) (hRd R hR)
  · rw [gateOf_sharp, gateOf_neg_eq, ← hRH, actC_comp]
    exact smul_mem_dualW (by norm_num) (hRd _ (isRot3_comp isRot3_rotYpi hR))

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.isOrth3_of_isRot3
#print axioms OIBridge.FourCopy.isRot3_trn
#print axioms OIBridge.FourCopy.isRot3_conj
#print axioms OIBridge.FourCopy.rotX_zero_apply
#print axioms OIBridge.FourCopy.trn_rot3
#print axioms OIBridge.FourCopy.trn_rotX
#print axioms OIBridge.FourCopy.trn_rotWord'
#print axioms OIBridge.FourCopy.isRot3_of_det
#print axioms OIBridge.FourCopy.isRot3_comp
#print axioms OIBridge.FourCopy.isRot3_rot3
#print axioms OIBridge.FourCopy.isRot3_rotX
#print axioms OIBridge.FourCopy.det_trn
#print axioms OIBridge.FourCopy.det_chartOf
#print axioms OIBridge.FourCopy.det_mul_self_of_orth
#print axioms OIBridge.FourCopy.rot3_eq_linear
#print axioms OIBridge.FourCopy.rotX_eq_linear
#print axioms OIBridge.FourCopy.rot3_xplus_mem
#print axioms OIBridge.FourCopy.rotX_z3_mem
#print axioms OIBridge.FourCopy.cross_rel
#print axioms OIBridge.FourCopy.cross_rel_symm
#print axioms OIBridge.FourCopy.homMap_rot3_one
#print axioms OIBridge.FourCopy.homMap_rot3_two
#print axioms OIBridge.FourCopy.homMap_rot3_three
#print axioms OIBridge.FourCopy.homMap_rotX_one
#print axioms OIBridge.FourCopy.homMap_rotX_two
#print axioms OIBridge.FourCopy.homMap_rotX_three
#print axioms OIBridge.FourCopy.cnot_actC_rot3
#print axioms OIBridge.FourCopy.cnot_actT_rotX
#print axioms OIBridge.FourCopy.actT_rot3_phiW
#print axioms OIBridge.FourCopy.actT_rotX_phiW
#print axioms OIBridge.FourCopy.cnot_prodState_rot
#print axioms OIBridge.FourCopy.actC_rotWord_phiW
#print axioms OIBridge.FourCopy.link_mem
#print axioms OIBridge.FourCopy.inv_left_ctrl
#print axioms OIBridge.FourCopy.inv_right_ctrl
#print axioms OIBridge.FourCopy.inv_left_partner
#print axioms OIBridge.FourCopy.inv_right_partner
#print axioms OIBridge.FourCopy.rot_of_words
#print axioms OIBridge.FourCopy.rot_of_words'
#print axioms OIBridge.FourCopy.image_eq_of_rot
#print axioms OIBridge.FourCopy.ie1_dualW
#print axioms OIBridge.FourCopy.ie1_of_dualW
#print axioms OIBridge.FourCopy.kt4_parity_of_witnesses
#print axioms OIBridge.FourCopy.tabMul_idW
#print axioms OIBridge.FourCopy.actC_reflY_idW
#print axioms OIBridge.FourCopy.bellOf_eq_actC
#print axioms OIBridge.FourCopy.rotYpi
#print axioms OIBridge.FourCopy.rotYpi_apply
#print axioms OIBridge.FourCopy.homMap_rotYpi_one
#print axioms OIBridge.FourCopy.homMap_rotYpi_two
#print axioms OIBridge.FourCopy.homMap_rotYpi_three
#print axioms OIBridge.FourCopy.rotYpi_eq_toLin'
#print axioms OIBridge.FourCopy.isRot3_rotYpi
#print axioms OIBridge.FourCopy.actC_rotYpi_dg
#print axioms OIBridge.FourCopy.gateOf_neg_eq
#print axioms OIBridge.FourCopy.smul_mem_dualW
#print axioms OIBridge.FourCopy.actC_mem_of_ie1
#print axioms OIBridge.FourCopy.parity_witnesses
