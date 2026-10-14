import OIBridge.TurnpikeScopeTransfer
import OIBridge.PiccardBridge

/-!
# Sign-aware integer classification and its conditional consumers

The exceptional correspondence has one global orientation, chosen before the
pair quantifiers. The sign-aware integer classification is an explicit
hypothesis; this module does not prove the published classification or its
translation into that hypothesis. Both orientations transfer to real spectra.
The reversed exceptional branch is excluded by conjugating the source
coefficient data and applying the existing six-mode obstruction.
-/

namespace OIBridge.ScopeTransferSigned

open HomometricSix ScopeTransfer

/-- Integer classification with a single orientation for the exceptional pair.
The two universal clauses are alternatives for the whole pair, not for each gap. -/
def BGIntegerClassificationSigned : Prop :=
  ∀ (n : ℕ) (F F' : Fin n → ℤ),
    StrictMono F → StrictMono F' →
    (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d) →
    (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d) →
    (Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ) →
    (¬ ∃ c : ℤ, ∀ i, F' i = F i + c) →
    (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) →
    ∃ eS eT : Fin 6 ≃ Fin n,
      (∀ a b : Fin 6, a < b →
        F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS b) - F (eS a))
      ∨ (∀ a b : Fin 6, a < b →
        F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS a) - F (eS b))

/-- The integer-to-real transfer preserves the globally chosen orientation. -/
theorem spectral_classification_of_BGSigned (hBG : BGIntegerClassificationSigned)
    {n : ℕ} (E E' : Fin n → ℝ)
    (hgapE : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapE' : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hsets : Finset.image (fun q : Fin n × Fin n => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin n × Fin n => E' q.2 - E' q.1) Finset.univ) :
    (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
    ∨ (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀)
    ∨ (∃ eS eT : Fin 6 ≃ Fin n, ∀ a b : Fin 6, a < b →
        E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS b) - E (eS a))
    ∨ (∃ eS eT : Fin 6 ≃ Fin n, ∀ a b : Fin 6, a < b →
        E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS a) - E (eS b)) := by
  classical
  rcases Nat.eq_zero_or_pos n with hn0 | npos
  · subst hn0
    exact Or.inl ⟨1, 0, fun a => a.elim0⟩
  -- injectivity of both spectra
  have hEinj : Function.Injective E := by
    intro a b hab
    by_contra hne
    exact hne (hgapE a b b a hne (Ne.symm hne) (by rw [hab])).1
  have hE'inj : Function.Injective E' := by
    intro a b hab
    by_contra hne
    exact hne (hgapE' a b b a hne (Ne.symm hne) (by rw [hab])).1
  -- sort both spectra
  set σ : Equiv.Perm (Fin n) := Tuple.sort E with hσdef
  set σ' : Equiv.Perm (Fin n) := Tuple.sort E' with hσ'def
  have hmonoE : StrictMono (E ∘ σ) :=
    (Tuple.monotone_sort E).strictMono_of_injective (hEinj.comp σ.injective)
  have hmonoE' : StrictMono (E' ∘ σ') :=
    (Tuple.monotone_sort E').strictMono_of_injective (hE'inj.comp σ'.injective)
  -- the sorted signed distinct-gap hypotheses, and their ascending forms
  have hgapS : ∀ a b c d : Fin n, a ≠ b → c ≠ d →
      (E ∘ σ) b - (E ∘ σ) a = (E ∘ σ) d - (E ∘ σ) c → a = c ∧ b = d := by
    intro a b c d hab hcd h
    have := hgapE (σ a) (σ b) (σ c) (σ d)
      (fun h' => hab (σ.injective h')) (fun h' => hcd (σ.injective h')) h
    exact ⟨σ.injective this.1, σ.injective this.2⟩
  have hgapS' : ∀ a b c d : Fin n, a ≠ b → c ≠ d →
      (E' ∘ σ') b - (E' ∘ σ') a = (E' ∘ σ') d - (E' ∘ σ') c → a = c ∧ b = d := by
    intro a b c d hab hcd h
    have := hgapE' (σ' a) (σ' b) (σ' c) (σ' d)
      (fun h' => hab (σ'.injective h')) (fun h' => hcd (σ'.injective h')) h
    exact ⟨σ'.injective this.1, σ'.injective this.2⟩
  have hascS : ∀ a b c d : Fin n, a < b → c < d →
      (E ∘ σ) b - (E ∘ σ) a = (E ∘ σ) d - (E ∘ σ) c → a = c ∧ b = d :=
    fun a b c d hab hcd => hgapS a b c d (ne_of_lt hab) (ne_of_lt hcd)
  have hascS' : ∀ a b c d : Fin n, a < b → c < d →
      (E' ∘ σ') b - (E' ∘ σ') a = (E' ∘ σ') d - (E' ∘ σ') c → a = c ∧ b = d :=
    fun a b c d hab hcd => hgapS' a b c d (ne_of_lt hab) (ne_of_lt hcd)
  -- gap-set equality survives sorting
  have himg : ∀ (f : Fin n → ℝ) (τ : Equiv.Perm (Fin n)),
      Finset.image (fun q : Fin n × Fin n => f (τ q.2) - f (τ q.1)) Finset.univ
        = Finset.image (fun q : Fin n × Fin n => f q.2 - f q.1) Finset.univ := by
    intro f τ
    apply Finset.ext
    intro v
    simp only [Finset.mem_image, Finset.mem_univ, true_and]
    constructor
    · rintro ⟨q, rfl⟩
      exact ⟨(τ q.1, τ q.2), rfl⟩
    · rintro ⟨q, rfl⟩
      exact ⟨(τ.symm q.1, τ.symm q.2), by simp⟩
  -- the forced gap correspondence of the sorted pair
  have hforce : ∀ p : AscPair n, ∃ cd : Fin n × Fin n, cd.1 < cd.2
      ∧ (E' ∘ σ') cd.2 - (E' ∘ σ') cd.1 = (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1 := by
    intro p
    have hv : (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1
        ∈ Finset.image (fun q : Fin n × Fin n => (E' ∘ σ') q.2 - (E' ∘ σ') q.1)
            Finset.univ := by
      have h1 : (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1
          ∈ Finset.image (fun q : Fin n × Fin n => E q.2 - E q.1) Finset.univ :=
        Finset.mem_image_of_mem _ (Finset.mem_univ (σ p.1.1, σ p.1.2))
      rw [hsets] at h1
      rw [show (fun q : Fin n × Fin n => (E' ∘ σ') q.2 - (E' ∘ σ') q.1)
        = fun q : Fin n × Fin n => E' (σ' q.2) - E' (σ' q.1) from rfl, himg E' σ']
      exact h1
    obtain ⟨q, _, hq⟩ := Finset.mem_image.mp hv
    have hvpos : 0 < (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1 := sub_pos.mpr (hmonoE p.2)
    rcases lt_trichotomy q.1 q.2 with h | h | h
    · exact ⟨q, h, hq⟩
    · exfalso
      rw [h] at hq
      simp only [sub_self] at hq
      linarith [hq ▸ hvpos]
    · exfalso
      have := hmonoE' h
      linarith [hq]
  choose νf hν1 hν2 using hforce
  -- trichotomy: translate, reflect, or genuinely nontrivial
  by_cases htr : ∃ c : ℝ, ∀ i, (E' ∘ σ') i = (E ∘ σ) i + c
  · obtain ⟨c, hc⟩ := htr
    left
    refine ⟨σ.symm.trans σ', c, fun a => ?_⟩
    have h2 : E' (σ' (σ.symm a)) = E (σ (σ.symm a)) + c := hc (σ.symm a)
    rw [Equiv.apply_symm_apply] at h2
    exact h2
  by_cases hrf : ∃ c : ℝ, ∀ i, (E' ∘ σ') i = c - (E ∘ σ) i.rev
  · obtain ⟨c, hc⟩ := hrf
    right; left
    refine ⟨σ.symm.trans (Fin.revPerm.trans σ'), c, fun a => ?_⟩
    have h2 : E' (σ' ((σ.symm a).rev)) = c - E (σ ((σ.symm a).rev.rev)) := hc ((σ.symm a).rev)
    rw [Fin.rev_rev, Equiv.apply_symm_apply] at h2
    rw [show (σ.symm.trans (Fin.revPerm.trans σ')) a = σ' ((σ.symm a).rev) from rfl, h2]
    ring
  -- nontriviality witnesses
  push Not at htr hrf
  obtain ⟨i₀, hi₀⟩ := htr ((E' ∘ σ') ⟨0, npos⟩ - (E ∘ σ) ⟨0, npos⟩)
  obtain ⟨i₁, hi₁⟩ := hrf ((E' ∘ σ') ⟨0, npos⟩ + (E ∘ σ) (⟨0, npos⟩ : Fin n).rev)
  have hnt : (E' ∘ σ') i₀ - (E ∘ σ) i₀
      ≠ (E' ∘ σ') ⟨0, npos⟩ - (E ∘ σ) ⟨0, npos⟩ := fun h => hi₀ (by linarith)
  have hnr : (E' ∘ σ') i₁ + (E ∘ σ) i₁.rev
      ≠ (E' ∘ σ') ⟨0, npos⟩ + (E ∘ σ) (⟨0, npos⟩ : Fin n).rev := fun h => hi₁ (by linarith)
  -- the scope transfer
  obtain ⟨F, F', hFm, hF'm, hFg, hF'g, hFν, hFnt, hFnr⟩ :=
    integer_realization_of_real_realization νf (E ∘ σ) (E' ∘ σ')
      hmonoE hmonoE' hascS hascS' hν2 hnt hnr
  -- the premise inputs for the integer surrogate
  have hinjF : Function.Injective (fun p : AscPair n => F p.1.2 - F p.1.1) := by
    intro p p' h
    have := hFg p.1.1 p.1.2 p'.1.1 p'.1.2 p.2 p'.2 h
    exact Subtype.ext (Prod.ext this.1 this.2)
  have hinjF' : Function.Injective (fun p : AscPair n => F' p.1.2 - F' p.1.1) := by
    intro p p' h
    have := hF'g p.1.1 p.1.2 p'.1.1 p'.1.2 p.2 p'.2 h
    exact Subtype.ext (Prod.ext this.1 this.2)
  have hFsets : Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ := by
    apply Finset.eq_of_subset_of_card_le
    · intro v hv
      obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hv
      exact Finset.mem_image.mpr ⟨⟨νf p, hν1 p⟩, Finset.mem_univ _, hFν p⟩
    · rw [Finset.card_image_of_injective _ hinjF', Finset.card_image_of_injective _ hinjF]
  have hFnottr : ¬ ∃ c : ℤ, ∀ i, F' i = F i + c := by
    rintro ⟨c, hc⟩
    exact hFnt (by rw [hc i₀, hc ⟨0, npos⟩]; ring)
  have hFnorf : ¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev := by
    rintro ⟨c, hc⟩
    exact hFnr (by rw [hc i₁, hc ⟨0, npos⟩]; ring)
  obtain ⟨eS, eT, hint⟩ := hBG n F F' hFm hF'm hFg hF'g hFsets hFnottr hFnorf
  -- The surrogate's forced directed gaps transport in either orientation.
  have transfer_gap : ∀ a b c d : Fin n, a ≠ b →
      F' d - F' c = F b - F a →
      (E' ∘ σ') d - (E' ∘ σ') c = (E ∘ σ) b - (E ∘ σ) a := by
    intro a b c d hab hint'
    rcases lt_trichotomy (a) (b) with h | h | h
    · have hFp : F' (νf ⟨(a, b), h⟩).2 - F' (νf ⟨(a, b), h⟩).1
          = F (b) - F (a) := hFν ⟨(a, b), h⟩
      have hupos : (0 : ℤ) < F (b) - F (a) := sub_pos.mpr (hFm h)
      have ho : c < d := by
        rcases lt_trichotomy (c) (d) with h' | h' | h'
        · exact h'
        · exfalso
          rw [h'] at hint'
          simp only [sub_self] at hint'
          omega
        · exfalso
          have := hF'm h'
          omega
      have hpair := hF'g (c) (d)
        (νf ⟨(a, b), h⟩).1 (νf ⟨(a, b), h⟩).2 ho (hν1 ⟨(a, b), h⟩)
        (by rw [hint', hFp])
      have hEp : (E' ∘ σ') (νf ⟨(a, b), h⟩).2 - (E' ∘ σ') (νf ⟨(a, b), h⟩).1
          = (E ∘ σ) (b) - (E ∘ σ) (a) := hν2 ⟨(a, b), h⟩
      rw [hpair.1, hpair.2]
      exact hEp
    · exact (hab h).elim
    · have hFp : F' (νf ⟨(b, a), h⟩).2 - F' (νf ⟨(b, a), h⟩).1
          = F (a) - F (b) := hFν ⟨(b, a), h⟩
      have huneg : F (b) - F (a) < 0 := sub_neg.mpr (hFm h)
      have ho : d < c := by
        rcases lt_trichotomy (d) (c) with h' | h' | h'
        · exact h'
        · exfalso
          rw [h'] at hint'
          simp only [sub_self] at hint'
          omega
        · exfalso
          have := hF'm h'
          omega
      have hpair := hF'g (d) (c)
        (νf ⟨(b, a), h⟩).1 (νf ⟨(b, a), h⟩).2 ho (hν1 ⟨(b, a), h⟩)
        (by omega)
      have hEp : (E' ∘ σ') (νf ⟨(b, a), h⟩).2 - (E' ∘ σ') (νf ⟨(b, a), h⟩).1
          = (E ∘ σ) (a) - (E ∘ σ) (b) := hν2 ⟨(b, a), h⟩
      rw [hpair.1, hpair.2]
      linarith [hEp]
  rcases hint with hplus | hminus
  · right; right; left
    refine ⟨eS.trans σ, eT.trans σ', fun a b hab => ?_⟩
    exact transfer_gap (eS a) (eS b) (eT (mu a b).1) (eT (mu a b).2)
      (fun h => hab.ne (eS.injective h)) (hplus a b hab)
  · right; right; right
    refine ⟨eS.trans σ, eT.trans σ', fun a b hab => ?_⟩
    exact transfer_gap (eS b) (eS a) (eT (mu a b).1) (eT (mu a b).2)
      (fun h => hab.ne (eS.injective h.symm)) (hminus a b hab)

open Matrix CongruentReconstruction BohrFrequency
local notation "conj'" => (starRingEnd ℂ)

/-- The reversed exceptional gap branch is incompatible with the actual
unitarity, nonzero-overlap, distinct-gap and probability-equality hypotheses. -/
theorem reversed_exceptional_impossible {m : ℕ}
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j))
    (hrev : ∃ eS eT : Fin 6 ≃ Fin m, ∀ a b : Fin 6, a < b →
      E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS a) - E (eS b)) : False := by
  obtain ⟨eS, eT, hspec⟩ := hrev
  apply exceptional_impossible (conjM V) W (conjM_unitary hV) hW
    (fun i a => by simpa [conjM_apply] using hVnz i a) hWnz
  refine ⟨eS, eS, eT, fun a b hab i j => ?_⟩
  have hline := coefficient_line_extraction V W E E' hgapV hgapW hU
    (a := eS b) (b := eS a) (c := eT (mu a b).1) (d := eT (mu a b).2)
    (fun h => hab.ne (eS.injective h.symm))
    (fun h => (mu_gap a b hab).1.ne (eT.injective h)) (hspec a b hab) (eS i) (eS j)
  simp only [Complex.star_def] at hline
  simp only [conjM_apply, map_mul, Complex.conj_conj]
  linear_combination hline

/-- Conditional two-branch reconstruction from the sign-aware integer premise.
No unsigned classification hypothesis is consumed by this theorem. -/
theorem twoBranch_of_BGSignedClassification (hBG : BGIntegerClassificationSigned)
    {m : ℕ} (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) := by
  apply twoBranch_of_spectral_classification hm V W E E' hV hW hVnz hWnz hgapV hgapW hU
  rcases spectral_classification_of_BGSigned hBG E E' hgapV hgapW
    (gaps_eq_of_equal_probabilities (by omega) V W E E' hVnz hWnz hU)
      with htr | hrf | hplus | hminus
  · exact Or.inl htr
  · exact Or.inr (Or.inl hrf)
  · exact Or.inr (Or.inr hplus)
  · exact (reversed_exceptional_impossible V W E E'
      hV hW hVnz hWnz hgapV hgapW hU hminus).elim

#print axioms spectral_classification_of_BGSigned
#print axioms reversed_exceptional_impossible
#print axioms twoBranch_of_BGSignedClassification

end OIBridge.ScopeTransferSigned

