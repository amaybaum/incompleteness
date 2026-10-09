/-
  OIBridge/FourCopyHeadline.lean — design (EQ4-F), not adopted: the Pauli-free headline
  KT(4; 01|23, 02|13) → IE₁ ∧ parity. The proofs here are assemblies: they add no `sorry` of
  their own, and `#print axioms` reports, through the exposed sub-lemmas of `FourCopyIE1.lean`,
  exactly which open obligations each result still rests on.

  * G13 (`ie1_all`): IE₁ for every pair, from the cross relation, the rotation links and the
    invariance lemmas at targets `01` and `02`.
  * G14 (`parity_all`): the orientation parity, from IE₁ and Lemma P with memberships.
  * G15 (`kt4_general_ie1`): the cross relation, IE₁ and the parity from the four-copy interface.
    Inverse-gate preservation is not a hypothesis: the recurrence lemma (R) derives it from
    orthogonality (O15), closedness and forward preservation.
  * `kt4_forward_ie1`: the same from `KT4Core` through Lemma B1; `kt4_forward_ie1_kt4` and
    `kt4_forward_ie1_lt` read it for `KT4` and `KT4LT`.

  The hypotheses are N-CLASS gates (`hcls`), admissible (`hadm`) and closed (`hcl`) pair cones,
  forward gate preservation (`hgate`) and the four-copy data. No complex number, Pauli matrix or
  PSD cone enters any statement or proof of this file or of the files it imports.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyIE1
import OIBridge.FourCopyBridge
import OIBridge.FourCopyLocal
import OIBridge.FourCopyBipolar

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-- **G13.** IE₁ for every pair cone. -/
theorem ie1_all (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hprod : ∀ p, ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K p)
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hbi : ∀ p, dualW (dualW (K p)) = K p)
    (hbs : ∀ p, bellOf (A p) (B p) ∈ K p) (hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p))
    (h : FCC K) : ∀ p, IE1 (K p) := by
  have hoA : ∀ p, IsOrth3 (A p) := fun p => (hcls p).1
  have hoB : ∀ p, IsOrth3 (B p) := fun p => (hcls p).2.1
  have hL : ∀ p a b, actC (A p ∘ₗ rotWord a b) (actT (B p) phiW) ∈ K p ∧
      actC (A p) (actT (B p ∘ₗ rotWord' a b) phiW) ∈ K p := fun p a b =>
    link_mem (hcls p) (hprod p) (hgate p) a b
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

/-- **G14.** The orientation parity of the four-cycle. -/
theorem parity_all (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p)
    (hie : ∀ p, IE1 (K p)) (h : FCC K) : EvenCycle (fun p => orient (A p) (B p)) :=
  kt4_parity_of_witnesses
    (parity_witnesses (hcls .p01) (hadm .p01).1.2 (hadm .p01).1.1 (hgate .p01) (hinv .p01)
      (hie .p01)).1
    (parity_witnesses (hcls .p23) (hadm .p23).1.2 (hadm .p23).1.1 (hgate .p23) (hinv .p23)
      (hie .p23)).1
    (parity_witnesses (hcls .p02) (hadm .p02).1.2 (hadm .p02).1.1 (hgate .p02) (hinv .p02)
      (hie .p02)).2.1
    (parity_witnesses (hcls .p13) (hadm .p13).1.2 (hadm .p13).1.1 (hgate .p13) (hinv .p13)
      (hie .p13)).2.2 h

/-- **G15. Theorem C′ (Pauli-free).** From the four-copy interface: the cross relation at target
`01`, IE₁ for every pair and the orientation parity. No inverse-gate hypothesis. -/
theorem kt4_general_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hcl : ∀ p, IsClosed (K p)) (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p) (h : FCC K) :
    K .p01 = Theta (A .p02) (B .p02) (A .p13) (B .p13) '' dualW (K .p23) ∧
      (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hinv : ∀ p, ∀ ω ∈ K p, (N p).symm ω ∈ K p := fun p =>
    inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)
  have hbi : ∀ p, dualW (dualW (K p)) = K p := fun p => bidual_of_adm (hadm p) (hcl p)
  have hbs : ∀ p, bellOf (A p) (B p) ∈ K p := fun p => bell_mem (hcls p) (hadm p).1.1 (hgate p)
  have hbe : ∀ p, bellOf (A p) (B p) ∈ dualW (K p) := fun p =>
    bell_mem_dual (hcls p) (hadm p).1.2 (hinv p)
  have hie := ie1_all K N A B A' B' hcls (fun p => (hadm p).1.1) hgate hbi hbs hbe h
  refine ⟨cross_rel (FourCopyCoherent.target01 h) (hbi .p01) (hcls .p02).1 (hcls .p02).2.1
    (hcls .p13).1 (hcls .p13).2.1 (hbs .p02) (hbs .p13) (hbe .p02) (hbe .p13), hie, ?_⟩
  exact parity_all K N A B A' B' hcls hadm hgate hinv hie h

/-- **Theorem A′ (headline, Pauli-free).** The core of KT(4), admissible closed pair cones and
N-CLASS gates preserving them give IE₁ for every pair and even orientation parity. -/
theorem kt4_forward_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
    (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
    (hcl : ∀ p, IsClosed (K p)) (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) := by
  have hF : FCC K := fourCopyCoherent_of_kt4Core (hadm .p01).1.2 (hadm .p23).1.2
    (hadm .p02).1.2 (hadm .p13).1.2 (hadm .p01).2.2 (hadm .p23).2.2 (hadm .p02).2.2
    (hadm .p13).2.2 H
  obtain ⟨-, hIE, hpar⟩ := kt4_general_ie1 K N A B A' B' hcls hadm hcl hgate hF
  exact ⟨hIE, hpar⟩

/-- Theorem A′ for `KT4`. -/
theorem kt4_forward_ie1_kt4 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4 (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) :=
  kt4_forward_ie1 K N A B A' B' hcls hadm hcl hgate H.toCore

/-- Theorem A′ for `KT4LT`. -/
theorem kt4_forward_ie1_lt (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3)
    (A B A' B' : Pr → E3) (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p))
    (hadm : ∀ p, PairAdm (K p)) (hcl : ∀ p, IsClosed (K p))
    (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
    {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]
    (H : KT4LT (K .p01) (K .p23) (K .p02) (K .p13) V) :
    (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p)) :=
  kt4_forward_ie1 K N A B A' B' hcls hadm hcl hgate H.toCore

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.ie1_all
#print axioms OIBridge.FourCopy.parity_all
#print axioms OIBridge.FourCopy.kt4_general_ie1
#print axioms OIBridge.FourCopy.kt4_forward_ie1
#print axioms OIBridge.FourCopy.kt4_forward_ie1_kt4
#print axioms OIBridge.FourCopy.kt4_forward_ie1_lt
