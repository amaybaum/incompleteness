/-
  OIBridge/FrequencyMatching.lean — probabilities to coefficient lines.

  The one general Fourier theorem the reconstruction needs, replacing per-branch lemmas: the
  COMPLEX amplitude a frequency carries in a transition probability,

      A_ij(ω) = Σ_{E_b − E_a = ω} V_ia V̄_ja V̄_ib V_jb,

  is determined by the probability function. `normSq_expansion` (BohrFrequency) already writes
  |U_ij(t)|² as the Fourier sum of these amplitudes over the gap set, and `coeffs_eq_zero` is
  Dedekind's independence of distinct characters — so equality of |U_ij(t)|² for all t matches
  the amplitudes frequency by frequency (`coefficients_by_frequency_determined`), over the union
  of the two gap sets and trivially off it.

  With all gaps distinct each nonzero fiber is a singleton, so a single spectral identity
  E'_d − E'_c = E_b − E_a extracts one full coefficient line (`coefficient_line_extraction`).
  That one corollary supplies the coefficient hypotheses of every branch of the reconstruction —
  translation, reflection, and the six-mode exceptional match — keeping the Piccard premise
  purely spectral: the classification speaks about spectra, and this file converts spectra plus
  equal probabilities into quantum coefficient equality.

  The two models are allowed different mode counts m, m′; equality of dimensions is never used.
-/
import OIBridge.BohrFrequency

namespace OIBridge
namespace BohrFrequency

open Complex Finset

variable {n : Type*} {m m' : ℕ}

/-- The complex amplitude carried by frequency `ω` in `|U_ij(t)|²`: the fiber sum of the
coefficient tensor `C^{ab}_{ij} = V_ia V̄_ja V̄_ib V_jb` over pairs with `E_b − E_a = ω`. -/
noncomputable def ampC (V : n → Fin m → ℂ) (E : Fin m → ℝ) (i j : n) (ω : ℝ) : ℂ :=
  ∑ q ∈ Finset.univ.filter (fun q : Fin m × Fin m => E q.2 - E q.1 = ω),
    V i q.1 * star (V j q.1) * star (V i q.2) * V j q.2

/-- Off the gap set the amplitude vanishes: the fiber is empty. -/
theorem ampC_eq_zero (V : n → Fin m → ℂ) {E : Fin m → ℝ} (i j : n) {ω : ℝ}
    (hω : ω ∉ gaps E) : ampC V E i j ω = 0 := by
  rw [ampC]
  refine Finset.sum_eq_zero fun q hq => ?_
  exfalso
  apply hω
  rw [← (Finset.mem_filter.mp hq).2]
  exact Finset.mem_image_of_mem _ (Finset.mem_univ q)

/-- The transition probability, regrouped by frequency value: `|U_ij(t)|²` is the Fourier sum of
the complex amplitudes over the gap set. -/
theorem normSq_eq_sum_gaps (V : n → Fin m → ℂ) (E : Fin m → ℝ) (t : ℝ) (i j : n) :
    Umat V E t i j * star (Umat V E t i j)
      = ∑ ω ∈ gaps E, ampC V E i j ω * Complex.exp (Complex.I * ω * t) := by
  rw [normSq_expansion, ← Finset.sum_fiberwise_of_maps_to
    (g := fun q : Fin m × Fin m => E q.2 - E q.1)
    (fun q _ => Finset.mem_image_of_mem _ (Finset.mem_univ q))]
  refine Finset.sum_congr rfl fun ω _ => ?_
  rw [ampC, Finset.sum_mul]
  refine Finset.sum_congr rfl fun q hq => ?_
  have hval : E q.2 - E q.1 = ω := (Finset.mem_filter.mp hq).2
  rw [hval]

/-- **COEFFICIENTS BY FREQUENCY ARE DETERMINED.** Equality of the transition probabilities for
all times forces equality of every complex frequency amplitude — Dedekind's independence applied
to the union of the two gap sets, with both amplitudes vanishing off their own sets. -/
theorem coefficients_by_frequency_determined
    (V : n → Fin m → ℂ) (W : n → Fin m' → ℂ) (E : Fin m → ℝ) (E' : Fin m' → ℝ)
    (hU : ∀ i j : n, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j)) :
    ∀ i j : n, ∀ ω : ℝ, ampC V E i j ω = ampC W E' i j ω := by
  intro i j ω
  set s : Finset ℝ := gaps E ∪ gaps E' with hs
  have hzero : ∀ x ∈ s, ampC V E i j x - ampC W E' i j x = 0 := by
    apply coeffs_eq_zero
    intro t
    have hVs : (∑ x ∈ s, ampC V E i j x * Complex.exp (Complex.I * x * t))
        = ∑ x ∈ gaps E, ampC V E i j x * Complex.exp (Complex.I * x * t) := by
      refine (Finset.sum_subset Finset.subset_union_left fun x _ hx => ?_).symm
      rw [ampC_eq_zero V i j hx, zero_mul]
    have hWs : (∑ x ∈ s, ampC W E' i j x * Complex.exp (Complex.I * x * t))
        = ∑ x ∈ gaps E', ampC W E' i j x * Complex.exp (Complex.I * x * t) := by
      refine (Finset.sum_subset Finset.subset_union_right fun x _ hx => ?_).symm
      rw [ampC_eq_zero W i j hx, zero_mul]
    calc (∑ x ∈ s, (ampC V E i j x - ampC W E' i j x) * Complex.exp (Complex.I * x * t))
        = (∑ x ∈ s, ampC V E i j x * Complex.exp (Complex.I * x * t))
          - ∑ x ∈ s, ampC W E' i j x * Complex.exp (Complex.I * x * t) := by
          rw [← Finset.sum_sub_distrib]
          exact Finset.sum_congr rfl fun x _ => by ring
      _ = Umat V E t i j * star (Umat V E t i j)
          - Umat W E' t i j * star (Umat W E' t i j) := by
          rw [hVs, hWs, ← normSq_eq_sum_gaps, ← normSq_eq_sum_gaps]
      _ = 0 := by rw [hU i j t, sub_self]
  by_cases hmem : ω ∈ s
  · have := hzero ω hmem
    linear_combination this
  · have hV0 : ampC V E i j ω = 0 :=
      ampC_eq_zero V i j (fun h => hmem (Finset.mem_union_left _ h))
    have hW0 : ampC W E' i j ω = 0 :=
      ampC_eq_zero W i j (fun h => hmem (Finset.mem_union_right _ h))
    rw [hV0, hW0]

/-- Distinct gaps make each nonzero fiber a singleton. -/
theorem fiber_singleton {E : Fin m → ℝ}
    (hgap : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    {a b : Fin m} (hab : a ≠ b) :
    Finset.univ.filter (fun q : Fin m × Fin m => E q.2 - E q.1 = E b - E a)
      = {(a, b)} := by
  have hω : E b - E a ≠ 0 := by
    intro h0
    have := hgap a b b a hab (Ne.symm hab) (by linarith)
    exact hab this.1
  apply Finset.eq_singleton_iff_unique_mem.mpr
  constructor
  · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, rfl⟩
  · intro q hq
    have hval : E q.2 - E q.1 = E b - E a := (Finset.mem_filter.mp hq).2
    have hne : q.1 ≠ q.2 := by
      intro h
      rw [h, sub_self] at hval
      exact hω hval.symm
    obtain ⟨h1, h2⟩ := hgap q.1 q.2 a b hne hab hval
    exact Prod.ext h1 h2

/-- **SINGLE-GAP COEFFICIENT EXTRACTION.** Under distinct gaps on both sides, one spectral
identity `E'_d − E'_c = E_b − E_a` extracts the full coefficient line: this is the sole
converter from probability data to the coefficient hypotheses of every reconstruction branch. -/
theorem coefficient_line_extraction
    (V : n → Fin m → ℂ) (W : n → Fin m' → ℂ) (E : Fin m → ℝ) (E' : Fin m' → ℝ)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m', a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : n, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j))
    {a b : Fin m} {c d : Fin m'} (hab : a ≠ b) (hcd : c ≠ d)
    (hmatch : E' d - E' c = E b - E a) :
    ∀ i j : n, W i c * star (W j c) * star (W i d) * W j d
      = V i a * star (V j a) * star (V i b) * V j b := by
  intro i j
  have hdet := coefficients_by_frequency_determined V W E E' hU i j (E b - E a)
  rw [ampC, ampC, fiber_singleton hgapV hab] at hdet
  have hfW : Finset.univ.filter
      (fun q : Fin m' × Fin m' => E' q.2 - E' q.1 = E b - E a) = {(c, d)} := by
    rw [← hmatch]
    exact fiber_singleton hgapW hcd
  rw [hfW] at hdet
  rw [Finset.sum_singleton, Finset.sum_singleton] at hdet
  exact hdet.symm

#print axioms ampC_eq_zero
#print axioms normSq_eq_sum_gaps
#print axioms coefficients_by_frequency_determined
#print axioms fiber_singleton
#print axioms coefficient_line_extraction

end BohrFrequency
end OIBridge
