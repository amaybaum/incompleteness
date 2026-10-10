/-
  DRAFT — UNBUILT (EQ4-F proof development, design only; not adopted, not for any branch as is).

  The statement layer of the Pauli-free core of the IE₁-first route (DEPGRAPH §4.1, G1–G15):
  KT(4) gives IE₁ for every pair, the orientation parity and the cross relation, with no Pauli
  dictionary, no PSD cone and no complex numbers. Statements carry their exact pre-check ids
  (`precheck_ie1first` M1–M11, `precheck_core` N1–N9). Proofs are written out only where short;
  every other proof is an explicit `sorry` placeholder of this design file, never a certified result.
  No Lean toolchain was available; nothing here has been elaborated.
-/
import OIBridge.FourCopyPackage
import OIBridge.FourCopyParity

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations OrbitNormalization

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-- The transpose of a local map (its adjoint for the Euclidean pairing of one ball). -/
def trn (A : E3) : E3 := Matrix.toLin' (LinearMap.toMatrix' A)ᵀ

/-! ### G3 — the table calculus of local maps -/

/-- G3a [X N6]. -/
theorem ipW_actC (M : E3) (E X : W 3) : ipW E (actC M X) = ipW (actC (trn M) E) X := by
  sorry

/-- G3b [X N6]. -/
theorem ipW_actT (M : E3) (E X : W 3) : ipW E (actT M X) = ipW (actT (trn M) E) X := by
  sorry

/-- G3c: `homMap` is functorial. -/
theorem actC_comp (M N : E3) (ω : W 3) : actC M (actC N ω) = actC (M ∘ₗ N) ω := by
  sorry

theorem actT_comp (M N : E3) (ω : W 3) : actT M (actT N ω) = actT (M ∘ₗ N) ω := by
  sorry

/-- G3d: the two token actions commute. -/
theorem actC_actT_comm (M N : E3) (ω : W 3) : actC M (actT N ω) = actT N (actC M ω) := by
  funext μ ν
  -- both sides are `Σ κ λ, H(M) μ κ * ω κ λ * H(N) ν λ`
  sorry

theorem trn_comp_self {A : E3} (hA : IsOrth3 A) : trn A ∘ₗ A = LinearMap.id := by
  sorry

theorem comp_trn_self {A : E3} (hA : IsOrth3 A) : A ∘ₗ trn A = LinearMap.id := by
  sorry

/-! ### G1, G2 — the Bell-link map Θ -/

/-- `R = A · reflY · Bᵀ`. -/
def chartOf (A B : E3) : E3 := A ∘ₗ reflY ∘ₗ trn B

/-- G1 [X M5]: `Θ = actC R02 ∘ actT R13`; no orthogonality is needed. -/
theorem Theta_eq (A02 B02 A13 B13 : E3) (g : W 3) :
    Theta A02 B02 A13 B13 g = actC (chartOf A02 B02) (actT (chartOf A13 B13) g) := by
  sorry

/-- The inverse of Θ for orthogonal locals. -/
def ThetaInv (A02 B02 A13 B13 : E3) (g : W 3) : W 3 :=
  actC (trn (chartOf A02 B02)) (actT (trn (chartOf A13 B13)) g)

/-- G2 [X M8, N9]. -/
theorem Theta_ipW {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02) (h3 : IsOrth3 A13)
    (h4 : IsOrth3 B13) (E X : W 3) :
    ipW (Theta A02 B02 A13 B13 E) (Theta A02 B02 A13 B13 X) = ipW E X := by
  sorry

theorem ThetaInv_Theta {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02)
    (h3 : IsOrth3 A13) (h4 : IsOrth3 B13) (g : W 3) :
    ThetaInv A02 B02 A13 B13 (Theta A02 B02 A13 B13 g) = g := by
  sorry

theorem Theta_ThetaInv {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02)
    (h3 : IsOrth3 A13) (h4 : IsOrth3 B13) (g : W 3) :
    Theta A02 B02 A13 B13 (ThetaInv A02 B02 A13 B13 g) = g := by
  sorry

/-! ### G4 — Bell data in the cone and in its dual -/

/-- G4a: products of sharp effects are dual-cone tables of every candidate cone (the proof of
`gate_sharp_mem_dualW` without the gate). -/
theorem sharp_mem_dualW {K : Set (W 3)} (hK : CandidateCone K) {b c : Fin 3 → ℝ}
    (hb : ∑ j, b j ^ 2 = 1) (hc : ∑ j, c j ^ 2 = 1) : tens (sharpVec b) (sharpVec c) ∈ dualW K := by
  refine mem_dualW.2 fun X hX => ?_
  rw [ipW_tens, ← prodEffVal_sharp]
  exact hK.2 hX _ _ (sharpEff_isEffectOn hb) (sharpEff_isEffectOn hc)

/-- G4b [X M9]: the Bell state lies in the cone (gate on a product state of the ball). -/
theorem bell_mem {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : CandidateCone K) (hgate : ∀ ω ∈ K, N ω ∈ K) : bellOf A B ∈ K := by
  obtain ⟨x, hx, y, hy, hxy⟩ := hcls.bell_state
  rw [← hxy]
  exact hgate _ (hK.1 x hx y hy)

/-- G4c [X M9]: the Bell table is a dual-cone table (dual action of the inverse gate). -/
theorem bell_mem_dual {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : CandidateCone K) (hinv : ∀ ω ∈ K, N.symm ω ∈ K) :
    bellOf A B ∈ dualW K := by
  obtain ⟨b, c, hb, hc, hbc⟩ := hcls.bell_effect
  have h := dualW_of_inv (hcls.ipW_map) hinv (sharp_mem_dualW hK hb hc)
  rw [hbc] at h
  -- `(1/4) • bellOf A B ∈ dualW K` gives `bellOf A B ∈ dualW K` (dual cones are cones)
  refine mem_dualW.2 fun X hX => ?_
  have := mem_dualW.1 h X hX
  -- ITER: `ipW ((1/4) • E) X = (1/4) * ipW E X`.
  simp only [ipW, Pi.smul_apply, smul_eq_mul] at this ⊢
  rw [← Finset.mul_sum] at this
  sorry

/-! ### G5, G6 — the cross relations -/

/-- A closed convex cone, nonempty (the bipolar's hypotheses). -/
structure ClosedCone (K : Set (W 3)) : Prop where
  cone : IsConvexCone K
  closed : IsClosed K
  nonempty : K.Nonempty

theorem ClosedCone.bidual {K : Set (W 3)} (hK : ClosedCone K) : dualW (dualW K) = K := by
  rw [dualW_dualW hK.cone hK.nonempty, hK.closed.closure_eq]

/-- G5 [X M5, M8; K incl_I, incl_II]: a target cone is the Θ-image of its partner's dual. Stated for
`PairLinked`, so that Lemma R's relabellings serve every target. -/
theorem cross_rel {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb) (hK : ClosedCone K)
    {Aa Ba Ab Bb : E3} (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba) (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb)
    (sa : bellOf Aa Ba ∈ La) (sb : bellOf Ab Bb ∈ Lb)
    (ea : bellOf Aa Ba ∈ dualW La) (eb : bellOf Ab Bb ∈ dualW Lb) :
    K = Theta Aa Ba Ab Bb '' dualW K' := by
  apply Set.Subset.antisymm
  · -- (II): `X = Θ (Θ⁻¹ X)` and `Θ⁻¹ X ∈ K'*`
    intro X hX
    refine ⟨ThetaInv Aa Ba Ab Bb X, mem_dualW.2 fun Y hY => ?_, Theta_ThetaInv h1 h2 h3 h4 X⟩
    have hu := h.upper X hX Y hY _ ea _ eb
    -- `ipW (Θ⁻¹ X) Y = ipW X (Θ Y)` by G2
    sorry
  · -- (I) and the bipolar
    rintro _ ⟨f, hf, rfl⟩
    rw [← hK.bidual]
    refine mem_dualW.2 fun e he => ?_
    rw [ipW_comm]
    exact h.lower _ sa _ sb e he f hf

/-- G6: the partner cone is the Θ⁻¹-image of the target's dual. -/
theorem cross_rel_symm {K K' La Lb : Set (W 3)} (h : PairLinked K K' La Lb) (hK : ClosedCone K)
    (hK' : ClosedCone K') {Aa Ba Ab Bb : E3} (h1 : IsOrth3 Aa) (h2 : IsOrth3 Ba)
    (h3 : IsOrth3 Ab) (h4 : IsOrth3 Bb) (sa : bellOf Aa Ba ∈ La) (sb : bellOf Ab Bb ∈ Lb)
    (ea : bellOf Aa Ba ∈ dualW La) (eb : bellOf Ab Bb ∈ dualW Lb) :
    K' = ThetaInv Aa Ba Ab Bb '' dualW K := by
  sorry

/-! ### G7, G8 — link families and rotated links -/

/-- G7a [X M10]: N-CLASS gates on product states, pre-locals absorbed. -/
theorem nclass_prodState {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    (x y : Fin 3 → ℝ) :
    N (prodState (trn A' x) (trn B' y)) = actC A (actT B (cnot (prodState x y))) := by
  sorry

/-- G7b [X N4]: maximally entangled rotation links. -/
theorem cnot_prodState_rot (a b : ℝ) :
    cnot (prodState (rot3 a xplus) (rotX b z3)) =
      actC (((rot3 a).linear : E3) ∘ₗ ((rotX b).linear : E3)) phiW := by
  sorry

/-- G7c [X N5]: the same tables, read on the target side. -/
theorem actT_rot_phiW (a b : ℝ) :
    actT (((rotX b).linear : E3) ∘ₗ ((rot3 a).linear : E3)) phiW =
      actC (((rot3 a).linear : E3) ∘ₗ ((rotX b).linear : E3)) phiW := by
  sorry

/-- G8a [X M6]: a rotated left link, control side. -/
theorem rotlink_left_control {A02 B02 A13 B13 : E3} (hA : IsOrth3 A02) (R : E3) (g : W 3) :
    tabMul (tabMul (actC A02 (actT B02 (actC R phiW))) g) (tabT (bellOf A13 B13)) =
      actC (A02 ∘ₗ R ∘ₗ trn A02) (Theta A02 B02 A13 B13 g) := by
  sorry

/-- G8b [X M7]: a rotated left link, target side. -/
theorem rotlink_left_target {A02 B02 A13 B13 : E3} (hB : IsOrth3 B02) (R : E3) (g : W 3) :
    tabMul (tabMul (actC A02 (actT B02 (actT R phiW))) g) (tabT (bellOf A13 B13)) =
      Theta A02 B02 A13 B13 (actC (B02 ∘ₗ trn R ∘ₗ trn B02) g) := by
  sorry

/-- G8c [X N1]: a rotated right link, control side. -/
theorem rotlink_right_control {A02 B02 A13 B13 : E3} (hA : IsOrth3 A13) (R : E3) (g : W 3) :
    tabMul (tabMul (bellOf A02 B02) g) (tabT (actC A13 (actT B13 (actC R phiW)))) =
      actT (A13 ∘ₗ R ∘ₗ trn A13) (Theta A02 B02 A13 B13 g) := by
  sorry

/-- G8d [X N2]: a rotated right link, target side. -/
theorem rotlink_right_target {A02 B02 A13 B13 : E3} (hB : IsOrth3 B13) (R : E3) (g : W 3) :
    tabMul (tabMul (bellOf A02 B02) g) (tabT (actC A13 (actT B13 (actT R phiW)))) =
      Theta A02 B02 A13 B13 (actT (B13 ∘ₗ trn R ∘ₗ trn B13) g) := by
  sorry

/-! ### G9–G12 — from rotated links to IE₁ -/

/-- G9 (generic form): a map that sends `Θ '' D` into the bidual of `K = Θ '' D` preserves `K`. -/
theorem invariant_of_bidual {K D : Set (W 3)} (hK : ClosedCone K) {Θ' Φ : W 3 → W 3}
    (hKD : K = Θ' '' D) (hΦ : ∀ f ∈ D, Φ (Θ' f) ∈ dualW (dualW K)) : ∀ X ∈ K, Φ X ∈ K := by
  intro X hX
  rw [hKD] at hX
  obtain ⟨f, hf, rfl⟩ := hX
  rw [← hK.bidual]
  exact hΦ f hf

/-- G9 (partner form): if `Θ (Ψ f) ∈ K = Θ '' D` for all `f ∈ D`, with Θ injective, then `Ψ '' D ⊆ D`. -/
theorem invariant_partner {K D : Set (W 3)} {Θ' Ψ : W 3 → W 3} (hinj : Function.Injective Θ')
    (hKD : K = Θ' '' D) (hΨ : ∀ f ∈ D, Θ' (Ψ f) ∈ K) : ∀ f ∈ D, Ψ f ∈ D := by
  intro f hf
  have h := hΨ f hf
  rw [hKD] at h
  obtain ⟨g, hg, hgf⟩ := h
  rw [← hinj hgf]
  exact hg

/-- G10: the conjugated z- and x-rotations generate SO(3) (Euler, O39). -/
theorem so3_of_generators {P : E3 → Prop} (hmul : ∀ M N, P M → P N → P (M ∘ₗ N)) {A : E3}
    (hA : IsOrth3 A) (hz : ∀ a, P (A ∘ₗ ((rot3 a).linear : E3) ∘ₗ trn A))
    (hx : ∀ b, P (A ∘ₗ ((rotX b).linear : E3) ∘ₗ trn A)) : ∀ R, IsRot3 R → P R := by
  -- `trn A ∘ R ∘ A` is a rotation; Euler gives `rot3 ψ * rotX θ * rot3 φ`; conjugate back.
  sorry

/-- G11: inclusion under every rotation gives image equality. -/
theorem image_eq_of_forall_rot {K : Set (W 3)} (act : E3 → W 3 → W 3)
    (hcomp : ∀ M N ω, act M (act N ω) = act (M ∘ₗ N) ω) (hid : ∀ ω, act LinearMap.id ω = ω)
    (h : ∀ R, IsRot3 R → ∀ ω ∈ K, act R ω ∈ K) : ∀ R, IsRot3 R → act R '' K = K := by
  sorry

/-- G12: IE₁ passes to the dual cone and back (closed convex cones). -/
theorem ie1_dualW {K : Set (W 3)} (h : IE1 K) : IE1 (dualW K) := by
  sorry

theorem ie1_of_ie1_dualW {K : Set (W 3)} (hK : ClosedCone K) (h : IE1 (dualW K)) : IE1 K := by
  sorry

/-! ### G13–G15 — the Pauli-free theorem -/

/-- G13: IE₁ for every pair cone. -/
theorem ie1_of_four_copy (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    (h : FCC K) : ∀ p, IE1 (K p) := by
  sorry

/-- G14a: Lemma P with memberships as hypotheses (the computation of `kt4_parity_aligned`). -/
theorem kt4_parity_of_witnesses {K01 K23 K02 K13 : Set (W 3)} {τ01 τ23 τ02 τ13 : Bool}
    (hX : gateOf τ01 (prodState xplus z3) ∈ K01) (hY : gateOf τ23 (prodState xplus z3) ∈ K23)
    (hE : gateOf τ02 (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K02)
    (hF : gateOf τ13 (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K13)
    (h : FourCopyCoherent K01 K23 K02 K13) : EvenCycle4 τ01 τ23 τ02 τ13 := by
  have hv := h.famI _ hX _ hY _ hE _ hF
  simp only [gateOf_sharp, gateOf_prodState_xplus_z3, gateOf_prodState_neg, ipW_dg_smul] at hv
  revert hv
  cases τ01 <;> cases τ23 <;> cases τ02 <;> cases τ13 <;> norm_num [sgnB, EvenCycle4, Bool.toNat]

/-- G14b [X N8]: witness reduction under IE₁. -/
theorem parity_witnesses_of_ie1 {N : W 3 ≃ₗ[ℝ] W 3} {A B A' B' : E3} (hcls : NClass N A B A' B')
    {K : Set (W 3)} (hK : PairAdm K) (hcl : IsClosed K) (hgate : ∀ ω ∈ K, N ω ∈ K)
    (hinv : ∀ ω ∈ K, N.symm ω ∈ K) (hie : IE1 K) :
    gateOf (orient A B) (prodState xplus z3) ∈ K ∧
      gateOf (orient A B) (tens (sharpVec xplus) (sharpVec z3)) ∈ dualW K ∧
      gateOf (orient A B) (tens (sharpVec (-xplus)) (sharpVec (-z3))) ∈ dualW K := by
  sorry

/-- G15: **Theorem C′ (Pauli-free).** -/
theorem kt4_general_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    (h : FCC K) :
    K .p01 = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  sorry

/-- **Theorem A′ (headline, Pauli-free).** KT(4) gives IE₁ for every pair and even orientation parity. -/
theorem kt4_forward_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4 (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hF : FCC K := fourCopyCoherent_of_kt4 (hadm .p01) (hadm .p23) (hadm .p02) (hadm .p13) H
  obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1 K N A B A' B' hcls hadm hcl hgate hinv hF
  exact ⟨hIE, hpar⟩

end

end FourCopy
end OIBridge
