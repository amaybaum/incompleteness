/-
  OIBridge/FourCopyIE1.lean — design (EQ4-F), not adopted: the exposed sub-lemmas of the
  Pauli-free route KT(4) → IE₁ ∧ parity (DEPGRAPH §4.1). This file holds every `sorry` of that
  route: each open sub-lemma below is one placeholder, and the assembly in
  `FourCopyHeadline.lean` composes them without further `sorry`. No complex number, Pauli matrix
  or PSD cone is used.

  Proved here: G5, G9a–G9d, G10, G10′, G11, G12, G12′ and G14a, with the rotation facts they
  read. Open, one placeholder each: G6 (`cross_rel_symm`, read by the classification only), G7
  (`link_mem`) and its two table identities G7(ii) and G7(iii), and G14b (`parity_witnesses`).

  * G5, G6: the cross relations `K = Θ '' K'*` and `K' = Θ⁻¹ '' K*` for a target in the form of
    Lemma R (`PairLinked`), from Bell tables in the link cones and in their duals.
  * G7: rotation links: `cnot` on a product of rotated pure states is a rotated Bell table, read
    on either token; the gate images of products supply them in every pair cone.
  * G9: invariance of a target cone (control side) and of its partner's dual (target side) under
    the conjugated rotation words carried by the links.
  * G10: the conjugated words generate the rotations (Euler, O39).
  * G11: inclusion under every rotation gives image equality.
  * G12: IE₁ passes to the dual cone; for a cone equal to its bidual it passes back.
  * G14: Lemma P with its four memberships as hypotheses (`kt4_parity_of_witnesses`, complete),
    and the reduction of the witnesses to memberships under IE₁ (`parity_witnesses`).

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
  sorry

/-! ### G7 — rotation links -/

/-- **G7(ii).** `cnot` on a product of rotated pure states is a rotated Bell table. -/
theorem cnot_prodState_rot (a b : ℝ) :
    cnot (prodState (rot3 a xplus) (rotX b z3)) = actC (rotWord a b) phiW := by
  sorry

/-- **G7(iii).** The same table read on the target token. -/
theorem actC_rotWord_phiW (a b : ℝ) : actC (rotWord a b) phiW = actT (rotWord' a b) phiW := by
  sorry

/-- **G7.** The links of a pair: gate images of products of the ball, in control-side and
target-side form. -/
theorem link_mem {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hprod : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hgate : ∀ ω ∈ K, N ω ∈ K) (a b : ℝ) :
    actC (A ∘ₗ rotWord a b) (actT B phiW) ∈ K ∧
      actC A (actT (B ∘ₗ rotWord' a b) phiW) ∈ K := by
  sorry

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

/-- **G14b.** Under IE₁ the post-locals of an N-CLASS gate reduce to the reflection charts
`{I, reflY}`, and Lemma P's witnesses become memberships carrying the pair's orientation bit. -/
theorem parity_witnesses {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3))
    (hprod : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hgate : ∀ ω ∈ K, N ω ∈ K) (hinv : ∀ ω ∈ K, N.symm ω ∈ K) (hie : IE1 K) :
    gateOf (orient A B) (prodState xplus z3) ∈ K ∧
      gateOf (orient A B) (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K ∧
      gateOf (orient A B) (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K := by
  sorry

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
#print axioms OIBridge.FourCopy.cross_rel
#print axioms OIBridge.FourCopy.cross_rel_symm
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
#print axioms OIBridge.FourCopy.parity_witnesses
