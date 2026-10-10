/-
  B1_UNBUILT.lean — thread B (PAIR-ACT), research only.

  UNBUILT. No Lean toolchain was available: nothing in this file has been compiled or kernel-checked. It is written
  against the design modules exported from ff9c3a358c57ce938978f15f2915d2145ae7b4a5 (`inputs/fourcopy/FourCopy*.lean`)
  and the landed modules they import. Each `_cons` declaration is a copy of a design declaration in which only the
  lines that consumed `hgate` or `hinv` are changed; `b1_steps.py` checks those diffs exactly against the design text.

  * `CONS`: the clause the design proof of `kt4_forward_ie1` consumes — the link family, the Bell state and the Bell
    effect. `kt4_forward_ie1_cons`: the headline with `CONS` in place of `hgate`; no Lemma R.
  * `OQ1` (gate images of product states in the cone, Bell table in the dual cone) and `SECT` (gate images of product
    states in the cone, inverse gate from the cone into the maximal cone): `cons_of_oq1`, `oq1_of_sect`.
  * `PREC` (gate preservation after a local orthogonal pre-correction): `kt4_forward_ie1_prec` is one application of
    `kt4_forward_ie1` to the corrected gates, which have the same post-locals.
  * `cons_of_hgate`, `prec_of_hgate`: hgate implies each weakening (the first under hcl, through Lemma R).
-/
import OIBridge.FourCopyHeadline

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### §A — the consumed clause -/

/-- The clause the design proof consumes from `hgate` and `hinv`. -/
structure CONS (K : Set (W 3)) (A B : E3) : Prop where
  link : ∀ a b : ℝ, actC (A ∘ₗ rotWord a b) (actT B phiW) ∈ K
  bs : bellOf A B ∈ K
  bd : bellOf A B ∈ dualW K

/-- The target-side form of a link from its control-side form: the rewriting step of `link_mem`. -/
theorem link_target_of_ctrl {K : Set (W 3)} {A B : E3} {a b : ℝ}
    (h1 : actC (A ∘ₗ rotWord a b) (actT B phiW) ∈ K) :
    actC A (actT (B ∘ₗ rotWord' a b) phiW) ∈ K := by
  rw [← actT_comp, ← actC_rotWord_phiW, ← actC_actT_comm, actC_comp]
  exact h1

/-! ### §B — the design proof with `CONS` in place of `hgate` -/

/-- **G13, CONS form.** -/
theorem ie1_all_cons (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hcons : ∀ p, CONS (K p) (A p) (B p)) (hbi : ∀ p, dualW (dualW (K p)) = K p)
    (hbs : ∀ p, bellOf (A p) (B p) ∈ K p) (hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p))
    (h : FCC K) : ∀ p, IE1 (K p) := by
  have hoA : ∀ p, IsOrth3 (A p) := fun p => (hcls p).1
  have hoB : ∀ p, IsOrth3 (B p) := fun p => (hcls p).2.1
  have hL : ∀ p a b, actC (A p ∘ₗ rotWord a b) (actT (B p) phiW) ∈ K p ∧
      actC (A p) (actT (B p ∘ₗ rotWord' a b) phiW) ∈ K p := fun p a b =>
    ⟨(hcons p).link a b, link_target_of_ctrl ((hcons p).link a b)⟩
  have step : ∀ T T' La Lb : Pr, PairLinked (K T) (K T') (K La) (K Lb) →
      IE1 (K T) ∧ IE1 (K T') := by
    intro T T' La Lb hPL
    have hKΘ := cross_rel hPL (hbi T) (hoA La) (hoB La) (hoA Lb) (hoB Lb) (hbs La) (hbs Lb)
      (hbe La) (hbe Lb)
    have hC : ∀ R, IsRot3 R → ∀ X ∈ K T, actC R X ∈ K T :=
      rot_of_words (P := fun R => ∀ X ∈ K T, actC R X ∈ K T)
        (fun M M' hM hM' X hX => by rw [← actC_comp]; exact hM _ (hM' X hX)) (hoA La)
        (fun a b => inv_left_ctrl hPL (hbi T) (hoA La) hKΘ (hL La a b).1 (hbs Lb))
    have hT : ∀ R, IsRot3 R → ∀ X ∈ K T, actT R X ∈ K T :=
      rot_of_words (P := fun R => ∀ X ∈ K T, actT R X ∈ K T)
        (fun M M' hM hM' X hX => by rw [← actT_comp]; exact hM _ (hM' X hX)) (hoA Lb)
        (fun a b => inv_right_ctrl hPL (hbi T) (hoA Lb) hKΘ (hbs La) (hL Lb a b).1)
    have hC' : ∀ R, IsRot3 R → ∀ f ∈ dualW (K T'), actC R f ∈ dualW (K T') :=
      rot_of_words' (P := fun R => ∀ f ∈ dualW (K T'), actC R f ∈ dualW (K T'))
        (fun M M' hM hM' f hf => by rw [← actC_comp]; exact hM _ (hM' f hf)) (hoB La)
        (fun a b => inv_left_partner hPL (hbi T) (hoA La) (hoB La) (hoA Lb) (hoB Lb) hKΘ
          (hL La a b).2 (hbs Lb))
    have hT' : ∀ R, IsRot3 R → ∀ f ∈ dualW (K T'), actT R f ∈ dualW (K T') :=
      rot_of_words' (P := fun R => ∀ f ∈ dualW (K T'), actT R f ∈ dualW (K T'))
        (fun M M' hM hM' f hf => by rw [← actT_comp]; exact hM _ (hM' f hf)) (hoB Lb)
        (fun a b => inv_right_partner hPL (hbi T) (hoA La) (hoB La) (hoA Lb) (hoB Lb) hKΘ
          (hbs La) (hL Lb a b).2)
    refine ⟨fun R hR => ⟨image_eq_of_rot (act := actC) actC_comp actC_id hC R hR,
      image_eq_of_rot (act := actT) actT_comp actT_id hT R hR⟩, ?_⟩
    exact ie1_of_dualW (hbi T') fun R hR =>
      ⟨image_eq_of_rot (act := actC) actC_comp actC_id hC' R hR,
        image_eq_of_rot (act := actT) actT_comp actT_id hT' R hR⟩
  have h01 := step .p01 .p23 .p02 .p13 (FourCopyCoherent.target01 h)
  have h02 := step .p02 .p13 .p01 .p23 (FourCopyCoherent.target02 h)
  intro p
  cases p
  · exact h01.1
  · exact h01.2
  · exact h02.1
  · exact h02.2

/-- **G14b, CONS form.** The Bell state and the Bell effect are hypotheses instead of being produced from `hgate`
and `hinv` by `bell_mem` and `bell_mem_dual`. -/
theorem parity_witnesses_cons {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : K ⊆ maxCone (eball 3))
    (hbs0 : bellOf A B ∈ K) (hbe0 : bellOf A B ∈ dualW K) (hie : IE1 K) :
    gateOf (orient A B) (prodState xplus z3) ∈ K ∧
      gateOf (orient A B) (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K ∧
      gateOf (orient A B) (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K := by
  have hA : IsOrth3 A := hcls.1
  have hB : IsOrth3 B := hcls.2.1
  have hC : IsOrth3 (chartOf A B) := isOrth3_chartOf hA hB
  have hbs : bellOf A B ∈ K := hbs0
  have hbe : bellOf A B ∈ dualW K := hbe0
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

/-- **G14, CONS form.** -/
theorem parity_all_cons (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hbs : ∀ p, bellOf (A p) (B p) ∈ K p) (hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p))
    (hie : ∀ p, IE1 (K p)) (h : FCC K) : EvenCycle (fun p => orient (A p) (B p)) :=
  kt4_parity_of_witnesses
    (parity_witnesses_cons (hcls .p01) (hadm .p01).1.2 (hbs .p01) (hbe .p01)
      (hie .p01)).1
    (parity_witnesses_cons (hcls .p23) (hadm .p23).1.2 (hbs .p23) (hbe .p23)
      (hie .p23)).1
    (parity_witnesses_cons (hcls .p02) (hadm .p02).1.2 (hbs .p02) (hbe .p02)
      (hie .p02)).2.1
    (parity_witnesses_cons (hcls .p13) (hadm .p13).1.2 (hbs .p13) (hbe .p13)
      (hie .p13)).2.2 h

/-- **G15, CONS form.** No Lemma R: the inverse gate is not read. -/
theorem kt4_general_ie1_cons (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hcl : ∀ p, IsClosed (K p)) (hcons : ∀ p, CONS (K p) (A p) (B p)) (h : FCC K) :
    K .p01 = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hbi : ∀ p, dualW (dualW (K p)) = K p := fun p => bidual_of_adm (hadm p) (hcl p)
  have hbs : ∀ p, bellOf (A p) (B p) ∈ K p := fun p => (hcons p).bs
  have hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p) := fun p => (hcons p).bd
  have hie := ie1_all_cons K N A B A' B' hcls hcons hbi hbs hbe h
  refine ⟨cross_rel (FourCopyCoherent.target01 h) (hbi .p01) (hcls .p02).1 (hcls .p02).2.1
    (hcls .p13).1 (hcls .p13).2.1 (hbs .p02) (hbs .p13) (hbe .p02) (hbe .p13), hie, ?_⟩
  exact parity_all_cons K N A B A' B' hcls hadm hbs hbe hie h

/-- **Theorem A′, CONS form.** -/
theorem kt4_forward_ie1_cons (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hcl : ∀ p, IsClosed (K p)) (hcons : ∀ p, CONS (K p) (A p) (B p))
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hF : FCC K := fourCopyCoherent_of_kt4Core (hadm .p01).1.2 (hadm .p23).1.2
    (hadm .p02).1.2 (hadm .p13).1.2 (hadm .p01).2.2 (hadm .p23).2.2 (hadm .p02).2.2
    (hadm .p13).2.2 H
  obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1_cons K N A B A' B' hcls hadm hcl hcons hF
  exact ⟨hIE, hpar⟩

/-! ### §C — OQ1 and SECT give CONS; hgate gives CONS -/

/-- Open question 1's clause: gate images of product states lie in the cone; the Bell table lies in its dual. -/
def OQ1 (K : Set (W 3)) (N : W 3 ≃ₗ[ℝ] W 3) (A B : E3) : Prop :=
  (∀ x ∈ eball 3, ∀ y ∈ eball 3, N (prodState x y) ∈ K) ∧ bellOf A B ∈ dualW K

/-- `OQ1` gives `CONS`: the proofs of `link_mem` and `bell_mem` with `hgate _ (hprod …)` replaced by the product
clause of `OQ1`. -/
theorem cons_of_oq1 {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (h : OQ1 K N A B) : CONS K A B where
  link a b := by
    have hmem := h.1 _ (orth_mem_eball (isOrth3_trn hcls.2.2.1) (rot3_xplus_mem a)) _
      (orth_mem_eball (isOrth3_trn hcls.2.2.2.1) (rotX_z3_mem b))
    rw [hcls.apply_prodState, cnot_prodState_rot, ← actC_actT_comm, actC_comp] at hmem
    exact hmem
  bs := by
    obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state
    rw [← hxy]
    exact h.1 x hx y hy
  bd := h.2

/-- The separable sector: gate images of product states lie in the cone, and the inverse gate maps the cone into the
maximal cone (equivalently, by orthogonality, gate images of product effects are dual-cone tables). -/
def SECT (K : Set (W 3)) (N : W 3 ≃ₗ[ℝ] W 3) : Prop :=
  (∀ x ∈ eball 3, ∀ y ∈ eball 3, N (prodState x y) ∈ K) ∧ ∀ ω ∈ K, N.symm ω ∈ maxCone (eball 3)

/-- The gate image of a product of sharp effects is a dual-cone table when the inverse gate maps the cone into the
maximal cone: `sharp_mem_dualW` read through the gate. -/
theorem gate_sharp_mem_dualW_of_inv_pos {N : W 3 ≃ₗ[ℝ] W 3} (hNo : ∀ E X, ipW (N E) (N X) = ipW E X)
    {K : Set (W 3)} (hpos : ∀ ω ∈ K, N.symm ω ∈ maxCone (eball 3)) {b c : Fin 3 → ℝ}
    (hb : ∑ j, b j ^ 2 = 1) (hc : ∑ j, c j ^ 2 = 1) :
    N (tens (sharpVec b) (sharpVec c)) ∈ dualW K := by
  refine mem_dualW.2 fun X hX => ?_
  have h1 : ipW (N (tens (sharpVec b) (sharpVec c))) X =
      ipW (tens (sharpVec b) (sharpVec c)) (N.symm X) := by
    rw [← hNo (tens (sharpVec b) (sharpVec c)) (N.symm X), N.apply_symm_apply]
  rw [h1, ipW_tens, ← prodEffVal_sharp]
  exact hpos X hX _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- `SECT` gives `OQ1`: the proof of `bell_mem_dual` with `dualW_of_inv … hinv (sharp_mem_dualW …)` replaced by
`gate_sharp_mem_dualW_of_inv_pos`. -/
theorem oq1_of_sect {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (h : SECT K N) : OQ1 K N A B := by
  refine ⟨h.1, ?_⟩
  obtain ⟨b, c, hb, hc, hbc⟩ := hcls.bell_effect
  have hm := gate_sharp_mem_dualW_of_inv_pos hcls.ipW_map h.2 hb hc
  rw [hbc] at hm
  refine mem_dualW.2 fun X hX => ?_
  have h1 := mem_dualW.1 hm X hX
  rw [ipW_smul_left] at h1
  exact (mul_nonneg_iff_of_pos_left (by norm_num)).1 h1

/-- `hgate` gives `CONS` under `hcls`, `hadm`, `hcl`: `link_mem`, `bell_mem`, and `bell_mem_dual` after Lemma R. -/
theorem cons_of_hgate {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hadm : PairAdm K) (hcl : IsClosed K) (hgate : ∀ ω ∈ K, N ω ∈ K) :
    CONS K A B where
  link a b := (link_mem hcls hadm.1.1 hgate a b).1
  bs := bell_mem hcls hadm.1.1 hgate
  bd := bell_mem_dual hcls hadm.1.2 (inv_mem_of_orth hcls.ipW_map hcl hgate)

/-! ### §D — PREC: hgate after a local orthogonal pre-correction -/

/-- The local map `actC C ∘ actT D` of orthogonal `C`, `D` as a linear equivalence. -/
def locEquiv (C D : E3) (hC : IsOrth3 C) (hD : IsOrth3 D) : W 3 ≃ₗ[ℝ] W 3 where
  toFun ω := actC C (actT D ω)
  invFun ω := actC (trn C) (actT (trn D) ω)
  map_add' ω₁ ω₂ := by
    funext μ ν
    simp only [actC_apply, actT_apply, Pi.add_apply, map_add]
  map_smul' c ω := by
    funext μ ν
    simp only [actC_apply, actT_apply, Pi.smul_apply, map_smul, smul_eq_mul, RingHom.id_apply]
  left_inv ω := by
    show actC (trn C) (actT (trn D) (actC C (actT D ω))) = ω
    rw [← actC_actT_comm C (trn D), actC_comp, actT_comp, trn_comp_self hC, trn_comp_self hD,
      actC_id, actT_id]
  right_inv ω := by
    show actC C (actT D (actC (trn C) (actT (trn D) ω))) = ω
    rw [← actC_actT_comm (trn C) D, actC_comp, actT_comp, comp_trn_self hC, comp_trn_self hD,
      actC_id, actT_id]

/-- A corrected gate keeps the N-CLASS form, with the same post-locals. -/
theorem nclass_comp_loc {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' C D : E3} (hcls : NClass N A B A' B')
    (hC : IsOrth3 C) (hD : IsOrth3 D) :
    NClass ((locEquiv C D hC hD).trans N) A B (A' ∘ₗ C) (B' ∘ₗ D) := by
  obtain ⟨hA, hB, hA', hB', hN⟩ := hcls
  refine ⟨hA, hB, isOrth3_comp hA' hC, isOrth3_comp hB' hD, fun ω => ?_⟩
  have e : actC A' (actT B' (actC C (actT D ω))) = actC (A' ∘ₗ C) (actT (B' ∘ₗ D) ω) := by
    rw [← actC_actT_comm C B', actT_comp, actC_comp]
  show N (actC C (actT D ω)) = _
  rw [hN, e]

/-- **PREC.** Some corrected gate, with the same post-locals, preserves the cone. -/
def PREC (K : Set (W 3)) (N : W 3 ≃ₗ[ℝ] W 3) : Prop :=
  ∃ C D : E3, ∃ hC : IsOrth3 C, ∃ hD : IsOrth3 D, ∀ ω ∈ K, ((locEquiv C D hC hD).trans N) ω ∈ K

/-- **Theorem A′ with PREC in place of hgate.** `kt4_forward_ie1` applied to the corrected gates; the conclusion
reads only the post-locals, which the correction does not change. -/
theorem kt4_forward_ie1_prec (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hcl : ∀ p, IsClosed (K p)) (hprec : ∀ p, PREC (K p) (N p))
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  simp only [PREC] at hprec
  choose C D hC hD hG using hprec
  exact kt4_forward_ie1 K (fun p => (locEquiv (C p) (D p) (hC p) (hD p)).trans (N p)) A B
    (fun p => A' p ∘ₗ C p) (fun p => B' p ∘ₗ D p)
    (fun p => nclass_comp_loc (hcls p) (hC p) (hD p)) hadm hcl hG H

theorem isOrth3_id : IsOrth3 (LinearMap.id : E3) := by
  unfold IsOrth3
  rw [LinearMap.toMatrix'_id]
  exact Submonoid.one_mem _

/-- `hgate` gives `PREC` (no correction). -/
theorem prec_of_hgate {N : W 3 ≃ₗ[ℝ] W 3} {K : Set (W 3)} (hgate : ∀ ω ∈ K, N ω ∈ K) : PREC K N :=
  ⟨LinearMap.id, LinearMap.id, isOrth3_id, isOrth3_id, fun ω hω => by
    show N (actC LinearMap.id (actT LinearMap.id ω)) ∈ K
    rw [actT_id, actC_id]
    exact hgate ω hω⟩

end

end FourCopy
end OIBridge
