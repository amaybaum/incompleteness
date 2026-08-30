/-
  OIBridge/BohrFrequency.lean — [GR] Theorem (Bohr-frequency completeness).

      The transition probabilities determine the Bohr-frequency set {E_a − E_b}.

  THIS FILE REPLACES A WITHDRAWN THEOREM. The statement that stood here in the manuscript — that
  matching transition probabilities force `H' = DHD†` — is false on three counts, each carried as a
  kernel identity or a probe countercontrol: the energy origin (`shift_normSq` below: `H + E₀`
  preserves every `|U_ij(t)|²`), the antiunitary reflection (`reflect_normSq`: `−H̄` conjugates
  `U(t)` entrywise), and, under the printed eigenvalue-only hypothesis, the C₄ ring of
  [SM Proposition 20], whose degenerate gaps let `H̄` through (probe). What survives, and what the
  §3.3 dimensional argument actually needs, is frequency completeness: the probabilities pin the
  full set of energy gaps, and no dimensionless data of this kind can pin the scale ℏ.

  THE ANALYTIC STEP IS DEDEKIND. "Distinct characters `t ↦ e^{iωt}` are linearly independent" is
  `linearIndependent_monoidHom` applied to `Multiplicative ℝ → ℂ`, with the injectivity of
  `ω ↦ chr ω` supplied by evaluating at `t = π/(ω₁−ω₂)`, where the two characters differ by
  `e^{iπ} = −1`. Nothing here samples, truncates, or approximates: the equality of the probability
  families is used at every real time.

  DEGENERATE GAPS ARE ALLOWED HERE. The return-probability coefficients `|V_ia|²|V_ib|²` are
  positive, so grouping by frequency value merges them without cancellation — which is exactly why
  frequency completeness is robust where Hamiltonian reconstruction is not. The reconstruction
  claim, with its distinct-gap hypothesis and two-branch conclusion, is stated in the manuscript
  as an open claim; its invisible branches are certified here, its classification is not.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.LinearAlgebra.LinearIndependent.Basic
import Mathlib.Data.Complex.BigOperators
import Mathlib.Data.Matrix.Basic

namespace OIBridge

namespace BohrFrequency

set_option autoImplicit false

open Complex Finset

/-! ### Dedekind for the characters of `(ℝ, +)` -/

/-- The character `t ↦ e^{iωt}`, as a monoid homomorphism `Multiplicative ℝ →* ℂ`. -/
noncomputable def chr (ω : ℝ) : Multiplicative ℝ →* ℂ where
  toFun t := Complex.exp (Complex.I * ω * (t.toAdd : ℂ))
  map_one' := by simp
  map_mul' x y := by
    show Complex.exp (Complex.I * ω * ((x.toAdd + y.toAdd : ℝ) : ℂ)) = _
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring

@[simp] theorem chr_apply (ω t : ℝ) :
    chr ω (Multiplicative.ofAdd t) = Complex.exp (Complex.I * ω * t) := rfl

/-- **Distinct frequencies give distinct characters**, by evaluation at `t = π/(ω₁ − ω₂)`. -/
theorem chr_injective : Function.Injective chr := by
  intro ω₁ ω₂ h
  by_contra hne
  have hd : (ω₁ - ω₂ : ℝ) ≠ 0 := sub_ne_zero.2 hne
  set t : ℝ := Real.pi / (ω₁ - ω₂) with ht
  have h1 := congrArg (fun f : Multiplicative ℝ →* ℂ => f (Multiplicative.ofAdd t)) h
  simp only [chr_apply] at h1
  have h2 : Complex.exp (Complex.I * ω₁ * t - Complex.I * ω₂ * t) = 1 := by
    rw [Complex.exp_sub, h1, div_self (Complex.exp_ne_zero _)]
  have h3 : Complex.I * ω₁ * t - Complex.I * ω₂ * t = Real.pi * Complex.I := by
    have harg : ((ω₁ - ω₂) * t : ℝ) = Real.pi := by
      rw [ht]
      field_simp
    calc Complex.I * ω₁ * t - Complex.I * ω₂ * t
        = (((ω₁ - ω₂) * t : ℝ) : ℂ) * Complex.I := by push_cast; ring
      _ = Real.pi * Complex.I := by rw [harg]
  rw [h3, Complex.exp_pi_mul_I] at h2
  norm_num at h2

/-- **A vanishing finite combination of distinct characters has vanishing coefficients.**
Dedekind's linear independence of characters, specialized. -/
theorem coeffs_eq_zero {s : Finset ℝ} {c : ℝ → ℂ}
    (h : ∀ t : ℝ, ∑ ω ∈ s, c ω * Complex.exp (Complex.I * ω * t) = 0) :
    ∀ ω ∈ s, c ω = 0 := by
  have hli : LinearIndependent ℂ (fun ω : ℝ => ((chr ω : Multiplicative ℝ →* ℂ) :
      Multiplicative ℝ → ℂ)) :=
    (linearIndependent_monoidHom (Multiplicative ℝ) ℂ).comp chr chr_injective
  have hsum : (∑ ω ∈ s, c ω • ((chr ω : Multiplicative ℝ →* ℂ) : Multiplicative ℝ → ℂ)) = 0 := by
    funext t
    have := h t.toAdd
    simpa [Finset.sum_apply, chr, smul_eq_mul] using this
  exact linearIndependent_iff'.1 hli s c hsum

/-! ### The return probability and its frequency support -/

variable {m : ℕ}

/-- The gap set `{E_b − E_a}`. -/
noncomputable def gaps (E : Fin m → ℝ) : Finset ℝ :=
  Finset.image (fun q : Fin m × Fin m => E q.2 - E q.1) Finset.univ

/-- The total (real, positive) coefficient a frequency value carries in the return probability:
degenerate gaps merge their contributions, and merging positives cannot cancel. -/
noncomputable def ampR (E p : Fin m → ℝ) (ω : ℝ) : ℝ :=
  ∑ q ∈ Finset.univ.filter (fun q : Fin m × Fin m => E q.2 - E q.1 = ω), p q.1 * p q.2

/-- **The return probability** `|U_ii(t)|²` in spectral form: `p a = |V_ia|²`. -/
noncomputable def retProb (E p : Fin m → ℝ) (t : ℝ) : ℂ :=
  ∑ q : Fin m × Fin m, ((p q.1 * p q.2 : ℝ) : ℂ) *
    Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * t)

/-- The return probability, regrouped by frequency value. -/
theorem retProb_eq_sum_gaps (E p : Fin m → ℝ) (t : ℝ) :
    retProb E p t = ∑ ω ∈ gaps E, ((ampR E p ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t) := by
  rw [retProb, ← Finset.sum_fiberwise_of_maps_to (g := fun q : Fin m × Fin m => E q.2 - E q.1)
    (fun q _ => Finset.mem_image_of_mem _ (Finset.mem_univ q))]
  refine Finset.sum_congr rfl fun ω _ => ?_
  rw [ampR]
  push_cast
  rw [Finset.sum_mul]
  refine Finset.sum_congr rfl fun q hq => ?_
  have hval : E q.2 - E q.1 = ω := by
    have := (Finset.mem_filter.1 hq).2
    simpa using this
  have hcast : ((E q.2 : ℂ) - (E q.1 : ℂ)) = (ω : ℂ) := by exact_mod_cast hval
  rw [hcast]

/-- **Every gap carries a strictly positive coefficient** when all overlaps are non-vanishing. -/
theorem ampR_pos {E p : Fin m → ℝ} (hp : ∀ a, 0 < p a) {ω : ℝ} (hω : ω ∈ gaps E) :
    0 < ampR E p ω := by
  obtain ⟨q, _, hq⟩ := Finset.mem_image.1 hω
  refine Finset.sum_pos (fun r _ => mul_pos (hp r.1) (hp r.2)) ?_
  exact ⟨q, Finset.mem_filter.2 ⟨Finset.mem_univ q, hq⟩⟩

/-- Off the gap set the coefficient vanishes: the fiber is empty. -/
theorem ampR_eq_zero {E p : Fin m → ℝ} {ω : ℝ} (hω : ω ∉ gaps E) : ampR E p ω = 0 := by
  rw [ampR]
  refine Finset.sum_eq_zero fun q hq => ?_
  exfalso
  refine hω ?_
  have hval : E q.2 - E q.1 = ω := by
    have := (Finset.mem_filter.1 hq).2
    simpa using this
  exact hval ▸ Finset.mem_image_of_mem _ (Finset.mem_univ q)

/-- **BOHR-FREQUENCY COMPLETENESS.** Two spectral models with positive overlaps and equal return
probabilities at every time have the same gap set. Degenerate gaps are allowed on both sides. -/
theorem gaps_determined {E p E' p' : Fin m → ℝ} (hp : ∀ a, 0 < p a) (hp' : ∀ a, 0 < p' a)
    (h : ∀ t : ℝ, retProb E p t = retProb E' p' t) : gaps E = gaps E' := by
  set s : Finset ℝ := gaps E ∪ gaps E' with hs
  set c : ℝ → ℂ := fun ω => ((ampR E p ω : ℝ) : ℂ) - ((ampR E' p' ω : ℝ) : ℂ) with hc
  have hzero : ∀ t : ℝ, ∑ ω ∈ s, c ω * Complex.exp (Complex.I * ω * t) = 0 := by
    intro t
    have hext : ∀ (F pp : Fin m → ℝ), (∀ ω ∈ s \ gaps F, ((ampR F pp ω : ℝ) : ℂ) = 0) := by
      intro F pp ω hω
      rw [ampR_eq_zero (Finset.mem_sdiff.1 hω).2]
      norm_num
    have h1 : (∑ ω ∈ s, ((ampR E p ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t))
        = retProb E p t := by
      rw [retProb_eq_sum_gaps]
      refine (Finset.sum_subset (Finset.subset_union_left) fun ω _ hω => ?_).symm
      rw [ampR_eq_zero hω]
      norm_num
    have h2 : (∑ ω ∈ s, ((ampR E' p' ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t))
        = retProb E' p' t := by
      rw [retProb_eq_sum_gaps]
      refine (Finset.sum_subset (Finset.subset_union_right) fun ω _ hω => ?_).symm
      rw [ampR_eq_zero hω]
      norm_num
    calc ∑ ω ∈ s, c ω * Complex.exp (Complex.I * ω * t)
        = (∑ ω ∈ s, ((ampR E p ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t))
          - ∑ ω ∈ s, ((ampR E' p' ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t) := by
          rw [← Finset.sum_sub_distrib]
          exact Finset.sum_congr rfl fun ω _ => by rw [hc]; ring
      _ = retProb E p t - retProb E' p' t := by rw [h1, h2]
      _ = 0 := by rw [h t, sub_self]
  have hmatch : ∀ ω ∈ s, ampR E p ω = ampR E' p' ω := by
    intro ω hω
    have := coeffs_eq_zero hzero ω hω
    rw [hc] at this
    exact_mod_cast sub_eq_zero.1 this
  refine Finset.ext fun ω => ⟨fun hω => ?_, fun hω => ?_⟩
  · have hpos := ampR_pos hp hω
    rw [hmatch ω (Finset.mem_union_left _ hω)] at hpos
    by_contra hc'
    rw [ampR_eq_zero hc'] at hpos
    exact lt_irrefl 0 hpos
  · have hpos := ampR_pos hp' hω
    rw [← hmatch ω (Finset.mem_union_right _ hω)] at hpos
    by_contra hc'
    rw [ampR_eq_zero hc'] at hpos
    exact lt_irrefl 0 hpos

/-! ### The full model, its expansion, and the two invisible impostors

These are the kernel half of the withdrawn theorem's post-mortem: any correct reconstruction
conclusion must carry the energy origin and the antiunitary reflection, because both are exactly
invisible to every `|U_ij(t)|²`. -/

variable {n : Type*}

/-- The propagator in spectral form: `U_ij(t) = Σ_a V_ia e^{−iE_a t} V̄_ja`. -/
noncomputable def Umat (V : n → Fin m → ℂ) (E : Fin m → ℝ) (t : ℝ) : n → n → ℂ :=
  fun i j => ∑ a, V i a * Complex.exp (-(Complex.I * (E a : ℂ) * t)) * star (V j a)

/-- Conjugating the phase factor reverses its frequency. -/
theorem star_phase (x s : ℝ) :
    star (Complex.exp (-(Complex.I * (x : ℂ) * (s : ℂ))))
      = Complex.exp (Complex.I * (x : ℂ) * (s : ℂ)) := by
  rw [← starRingEnd_apply, ← Complex.exp_conj, map_neg, map_mul, map_mul, Complex.conj_I,
    Complex.conj_ofReal, Complex.conj_ofReal]
  ring_nf

/-- **The expansion of `|U_ij(t)|²`**: a combination of the same gap frequencies, with the
coefficient tensor `C^{ab}_{ij} = V_ia V̄_ja V̄_ib V_jb`. At `i = j` the coefficients are the
positive `|V_ia|²|V_ib|²` of `retProb`. -/
theorem normSq_expansion (V : n → Fin m → ℂ) (E : Fin m → ℝ) (t : ℝ) (i j : n) :
    Umat V E t i j * star (Umat V E t i j)
      = ∑ q : Fin m × Fin m, (V i q.1 * star (V j q.1) * star (V i q.2) * V j q.2) *
          Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * t) := by
  rw [Umat, star_sum, Finset.sum_mul_sum, ← Finset.sum_product']
  show (∑ q : Fin m × Fin m, _) = _
  refine Finset.sum_congr rfl fun q _ => ?_
  simp only [star_mul', star_star]
  rw [star_phase (E q.2) t]
  have hprod : Complex.exp (-(Complex.I * (E q.1 : ℂ) * t)) * Complex.exp (Complex.I * (E q.2 : ℂ) * t)
      = Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * t) := by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring
  rw [← hprod]
  ring

/-- **IMPOSTOR ONE: the energy origin.** Shifting every eigenvalue multiplies `U(t)` by the global
phase `e^{−iE₀t}`, so every `|U_ij(t)|²` is untouched. -/
theorem shift_modsq (V : n → Fin m → ℂ) (E : Fin m → ℝ) (E₀ t : ℝ) (i j : n) :
    Umat V (fun a => E a + E₀) t i j * star (Umat V (fun a => E a + E₀) t i j)
      = Umat V E t i j * star (Umat V E t i j) := by
  have hfac : Umat V (fun a => E a + E₀) t i j
      = Complex.exp (-(Complex.I * (E₀ : ℂ) * t)) * Umat V E t i j := by
    rw [Umat, Umat, Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => ?_
    have hsplit : Complex.exp (-(Complex.I * ((E a + E₀ : ℝ) : ℂ) * t))
        = Complex.exp (-(Complex.I * (E₀ : ℂ) * t)) * Complex.exp (-(Complex.I * (E a : ℂ) * t)) := by
      rw [← Complex.exp_add]
      congr 1
      push_cast
      ring
    rw [hsplit]
    ring
  have hunit : star (Complex.exp (-(Complex.I * (E₀ : ℂ) * t)))
      * Complex.exp (-(Complex.I * (E₀ : ℂ) * t)) = 1 := by
    rw [star_phase E₀ t, ← Complex.exp_add]
    rw [show Complex.I * (E₀ : ℂ) * t + -(Complex.I * (E₀ : ℂ) * t) = 0 from by ring]
    exact Complex.exp_zero
  rw [hfac, star_mul']
  calc Complex.exp (-(Complex.I * (E₀ : ℂ) * t)) * Umat V E t i j *
        (star (Complex.exp (-(Complex.I * (E₀ : ℂ) * t))) * star (Umat V E t i j))
      = (star (Complex.exp (-(Complex.I * (E₀ : ℂ) * t)))
          * Complex.exp (-(Complex.I * (E₀ : ℂ) * t)))
        * (Umat V E t i j * star (Umat V E t i j)) := by ring
    _ = Umat V E t i j * star (Umat V E t i j) := by rw [hunit, one_mul]

/-- **IMPOSTOR TWO: the antiunitary reflection.** `V → V̄, E → −E` conjugates `U(t)` entrywise —
this is `H → −H̄` — so every `|U_ij(t)|²` is untouched, while the spectrum reflects. -/
theorem reflect_conj (V : n → Fin m → ℂ) (E : Fin m → ℝ) (t : ℝ) (i j : n) :
    Umat (fun i a => star (V i a)) (fun a => -E a) t i j = star (Umat V E t i j) := by
  rw [Umat, Umat, star_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  simp only [star_mul', star_star]
  rw [star_phase (E a) t]
  have hneg : Complex.exp (-(Complex.I * ((-E a : ℝ) : ℂ) * t))
      = Complex.exp (Complex.I * (E a : ℂ) * t) := by
    congr 1
    push_cast
    ring
  rw [hneg]

/-- And conjugation preserves every squared modulus. -/
theorem reflect_modsq (V : n → Fin m → ℂ) (E : Fin m → ℝ) (t : ℝ) (i j : n) :
    Umat (fun i a => star (V i a)) (fun a => -E a) t i j *
      star (Umat (fun i a => star (V i a)) (fun a => -E a) t i j)
      = Umat V E t i j * star (Umat V E t i j) := by
  rw [reflect_conj, star_star]
  ring

/-! ### The wrapper -/

/-- **[GR] THEOREM (Bohr-frequency completeness)**, all clauses. The return probability is a
positive combination over exactly the gap set; every `|U_ij(t)|²` expands over the same
frequencies; and equal return probabilities force equal gap sets. -/
theorem bohr_frequency_completeness {E p E' p' : Fin m → ℝ}
    (hp : ∀ a, 0 < p a) (hp' : ∀ a, 0 < p' a) :
    (∀ t, retProb E p t
        = ∑ ω ∈ gaps E, ((ampR E p ω : ℝ) : ℂ) * Complex.exp (Complex.I * ω * t)) ∧
    (∀ ω ∈ gaps E, 0 < ampR E p ω) ∧
    ((∀ t : ℝ, retProb E p t = retProb E' p' t) → gaps E = gaps E') :=
  ⟨fun t => retProb_eq_sum_gaps E p t, fun _ hω => ampR_pos hp hω,
   fun h => gaps_determined hp hp' h⟩

/-! ### What these proofs rest on -/

#print axioms chr_injective
#print axioms coeffs_eq_zero
#print axioms retProb_eq_sum_gaps
#print axioms ampR_pos
#print axioms gaps_determined
#print axioms normSq_expansion
#print axioms shift_modsq
#print axioms reflect_conj
#print axioms reflect_modsq
#print axioms bohr_frequency_completeness

end BohrFrequency

end OIBridge
