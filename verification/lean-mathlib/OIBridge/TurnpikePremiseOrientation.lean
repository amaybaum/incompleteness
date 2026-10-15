import OIBridge.TurnpikeScopeTransfer
import OIBridge.PiccardBridge

/-!
# The orientation of the formal integer-classification premise (round BG-2)

`ScopeTransfer.BGIntegerClassification` fixes, in its exceptional branch, the orientation in which
the forced correspondence `mu` realizes the gaps: target gaps equal source gaps `F (eS b) - F (eS a)`.
This module shows that this proposition, as written, fails at six marks.

* The integer rulers `r1 = (0,1,4,10,12,17)` and `r2refl = 17 - r2 ∘ rev = (0,4,6,9,16,17)` satisfy
  every hypothesis of the proposition (`hyps_r1_r2refl`).
* No pair of relabelings realizes `mu` in the fixed orientation (`not_muForm_r1_r2refl`). Eight gap
  identities force three linear relations on the source labels; a kernel decision over the 720
  source permutations leaves three difference patterns (`source_difference_cases`), and a kernel
  decision over the 216 target triples shows that `r2refl` realizes none of them
  (`reflected_difference_obstruction`).
* Hence `not_BGIntegerClassification`.
* Controls: the printed pair `(r1, r2)` realizes `mu` in the fixed orientation (`muForm_r1_r2`), and
  the instance realizes it reversed (`revMuForm_r1_r2refl`).

Scope: one formal statement at one instance. Nothing here concerns the published classification of
Bekir and Golomb, the exceptional family in general, or the two-branch conclusion of GR;
`spectral_classification_of_BG` and `twoBranch_of_BGClassification` remain implications whose
hypothesis `hBG` is refutable. The finite reductions use `decide +kernel`, never `native_decide`.
-/

namespace OIBridge.PremiseOrientation

open ScopeTransfer HomometricSix

set_option maxRecDepth 100000
set_option maxHeartbeats 0

def r2refl : Fin 6 → ℤ := fun i => 17 - r2 i.rev

theorem hyps_r1_r2refl : StrictMono r1 ∧ StrictMono r2refl
    ∧ (∀ a b c d : Fin 6, a < b → c < d → r1 b - r1 a = r1 d - r1 c → a = c ∧ b = d)
    ∧ (∀ a b c d : Fin 6, a < b → c < d → r2refl b - r2refl a = r2refl d - r2refl c → a = c ∧ b = d)
    ∧ Finset.image (fun p : AscPair 6 => r1 p.1.2 - r1 p.1.1) Finset.univ
        = Finset.image (fun p : AscPair 6 => r2refl p.1.2 - r2refl p.1.1) Finset.univ
    ∧ (¬ ∃ c : ℤ, ∀ i, r2refl i = r1 i + c) ∧ (¬ ∃ c : ℤ, ∀ i, r2refl i = c - r1 i.rev) := by
  refine ⟨by decide +kernel, by decide +kernel, golomb_r1, by decide +kernel,
    by decide +kernel, ?_, ?_⟩
  · rintro ⟨c, hc⟩
    have h0 := hc 0
    have h1 := hc 1
    norm_num [r2refl, r1, r2, Fin.rev] at h0 h1
    omega
  · rintro ⟨c, hc⟩
    have h0 := hc 0
    have h1 := hc 1
    norm_num [r2refl, r1, r2, Fin.rev] at h0 h1
    omega

theorem source_difference_cases : ∀ e : Equiv.Perm (Fin 6),
    r1 (e 5) + 2 * r1 (e 0) = r1 (e 1) + r1 (e 2) + r1 (e 4) →
    2 * r1 (e 1) + r1 (e 3) = 2 * r1 (e 0) + r1 (e 4) →
    r1 (e 1) + 2 * r1 (e 3) = r1 (e 0) + r1 (e 2) + r1 (e 5) →
    (r1 (e 1) - r1 (e 0) = 1 ∧ r1 (e 5) - r1 (e 0) = 17)
    ∨ (r1 (e 1) - r1 (e 0) = -6 ∧ r1 (e 5) - r1 (e 0) = -9)
    ∨ (r1 (e 1) - r1 (e 0) = 5 ∧ r1 (e 5) - r1 (e 0) = -8) := by
  decide +kernel

theorem reflected_difference_obstruction : ∀ i j k : Fin 6,
    ¬ ((r2refl j - r2refl i = 1 ∧ r2refl k - r2refl i = 17)
      ∨ (r2refl j - r2refl i = -6 ∧ r2refl k - r2refl i = -9)
      ∨ (r2refl j - r2refl i = 5 ∧ r2refl k - r2refl i = -8)) := by
  decide +kernel

theorem not_muForm_r1_r2refl : ¬ ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2refl (eT (mu a b).2) - r2refl (eT (mu a b).1) = r1 (eS b) - r1 (eS a) := by
  rintro ⟨eS, eT, h⟩
  have h01 := h 0 1 (by decide)
  have h02 := h 0 2 (by decide)
  have h03 := h 0 3 (by decide)
  have h04 := h 0 4 (by decide)
  have h05 := h 0 5 (by decide)
  have h12 := h 1 2 (by decide)
  have h24 := h 2 4 (by decide)
  have h35 := h 3 5 (by decide)
  simp only [mu] at h01 h02 h03 h04 h05 h12 h24 h35
  have hR1 : r1 (eS 5) + 2 * r1 (eS 0)
      = r1 (eS 1) + r1 (eS 2) + r1 (eS 4) := by linarith
  have hR2 : 2 * r1 (eS 1) + r1 (eS 3)
      = 2 * r1 (eS 0) + r1 (eS 4) := by linarith
  have hR3 : r1 (eS 1) + 2 * r1 (eS 3)
      = r1 (eS 0) + r1 (eS 2) + r1 (eS 5) := by linarith
  apply reflected_difference_obstruction (eT 0) (eT 1) (eT 5)
  rcases source_difference_cases eS hR1 hR2 hR3 with hcase | hcase | hcase
  · exact Or.inl ⟨by linarith [hcase.1], by linarith [hcase.2]⟩
  · exact Or.inr (Or.inl ⟨by linarith [hcase.1], by linarith [hcase.2]⟩)
  · exact Or.inr (Or.inr ⟨by linarith [hcase.1], by linarith [hcase.2]⟩)

theorem not_BGIntegerClassification : ¬ BGIntegerClassification := by
  intro hBG
  obtain ⟨hmono, hmono', hgap, hgap', hsets, htr, hrf⟩ := hyps_r1_r2refl
  exact not_muForm_r1_r2refl (hBG 6 r1 r2refl hmono hmono' hgap hgap' hsets htr hrf)

theorem muForm_r1_r2 : ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2 (eT (mu a b).2) - r2 (eT (mu a b).1) = r1 (eS b) - r1 (eS a) :=
  ⟨Equiv.refl _, Equiv.refl _, fun a b hab => (mu_gap a b hab).2⟩

theorem revMuForm_r1_r2refl : ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
    r2refl (eT (mu a b).2) - r2refl (eT (mu a b).1) = r1 (eS a) - r1 (eS b) := by
  refine ⟨Equiv.refl _, Fin.revPerm, fun a b hab => ?_⟩
  change (17 - r2 (mu a b).2.rev.rev) - (17 - r2 (mu a b).1.rev.rev)
    = r1 a - r1 b
  rw [Fin.rev_rev, Fin.rev_rev]
  linarith [(mu_gap a b hab).2]

#print axioms hyps_r1_r2refl
#print axioms source_difference_cases
#print axioms reflected_difference_obstruction
#print axioms not_muForm_r1_r2refl
#print axioms not_BGIntegerClassification
#print axioms muForm_r1_r2
#print axioms revMuForm_r1_r2refl

end OIBridge.PremiseOrientation
