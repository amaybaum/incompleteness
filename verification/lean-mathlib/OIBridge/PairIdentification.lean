/-
  OIBridge/PairIdentification.lean — pair identification from frequency data under a
  triangle-genericity condition, and the sign-aware form of the classification premise.

  PART 1: TRIANGLE GENERICITY. Equal transition probabilities give equal gap sets
  (`ScopeTransfer.gaps_eq_of_equal_probabilities`), but a gap set alone need not fix the
  spectrum up to congruence: non-congruent rulers with distinct differences and equal difference
  sets exist (`HomometricSix.r1`, `HomometricSix.r2`). The condition `TriangleGeneric` (the
  manuscripts' (G4)) excludes them. It says that an additive relation
  `(E_b − E_a) + (E_d − E_c) = E_f − E_e` among the gaps of three pairwise distinct mode pairs
  holds only as a triangle identity: `b = c, e = a, f = d` or `d = a, e = c, f = b`. The triangle
  identities are exactly the three-term relations of this shape that hold for every spectrum, so
  (G4) excludes only relations that are not forced; it says nothing about relations with four or
  more terms, which include forced ones such as `ω_kl + ω_mn = ω_kn − ω_lm`. Each excluded
  relation is a nonzero linear equation on the spectrum, so the condition fails only on finitely
  many hyperplanes; it is a hypothesis on the spectrum, not a consequence of anything here.

  THE ARGUMENT, no ruler classification. Fix two modes `o ≠ a₀` and the target pair `(p, q)`
  whose directed gap is `E_{a₀} − E_o`. For any further mode `y`, the gaps of `(o, a₀)`,
  `(a₀, y)` and `(o, y)` satisfy a triangle identity; their target pairs therefore satisfy the
  same additive relation and, by (G4), form a triangle, so the target pair of `(o, y)` starts at
  `p` or ends at `q` (`star_step`). Applying the same step to two further modes shows that the
  choice is the same for every `y` (`congruent_of_triangleGeneric`): either every target pair of
  `(o, y)` starts at `p`, and `E'` contains the translate `E + E₀`, or every one ends at `q`, and
  `E'` contains the reflected translate `−E + E₀`. Equal dimensions make the containment a
  relabelling (`perm_of_cover`). The theorem needs (G4) for the target spectrum only and distinct
  gaps for the source spectrum only, and holds from dimension two.

  `twoBranch_of_congruence` turns a translation- or reflection-congruence into the two Hamiltonian
  branches through `reconstruction_translation` and `reconstruction_reflection`: translation
  matches the pair `(a, b)` with `(τ a, τ b)` and gives `D H D† + E₀`; reflection matches it with
  `(τ b, τ a)`, which conjugates its coefficient line, and gives `−D H̄ D† + E₀`. With
  `gaps_eq_of_equal_probabilities` this yields `twoBranch_of_triangleGeneric` ((G4) for the second
  Hamiltonian) and `twoBranch_of_triangleGeneric_source` ((G4) for the first): the two branches
  follow from equal transition probabilities with no classification premise and without the
  six-mode obstruction, for every mode count `m ≥ 3`.

  PART 2: THE SIGN-AWARE PREMISE. `twoBranch_of_signed_spectral_classification` admits, in its
  classification premise, the exceptional correspondence μ in either global orientation. The
  reversed orientation reduces to the positive one by conjugation: reversing every source pair
  conjugates the source coefficient lines, so the reversed match for `V` is the positive match
  for the entrywise conjugate `V̄`, and `exceptional_impossible` applied to `(V̄, W)` excludes it.
  `BGSignedClassification` is the sign-aware integer premise (μ or its global reversal, one
  orientation for the whole pair); `twoBranch_of_BGSignedClassification` derives the two
  branches from it through `real_to_integer_surrogate`. The instance refuting the unsigned premise
  satisfies the signed conclusion (`signedForm_r1_r2refl`). Whether `BGSignedClassification` is
  true is not decided here.
  These consumers restate, in the gated library, the conditional consumers compiled as design
  evidence in `verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.TurnpikePremiseOrientation

namespace OIBridge
namespace PairIdentification

open Complex Matrix HomometricSix BohrFrequency CongruentReconstruction ScopeTransfer

local notation "conj'" => (starRingEnd ℂ)

variable {m : ℕ}

/-! ### Part 1: triangle genericity -/

/-- **(G4), triangle genericity.** An additive relation among the directed gaps of three pairwise
distinct mode pairs is a triangle identity. -/
def TriangleGeneric (E : Fin m → ℝ) : Prop :=
  ∀ a b c d e f : Fin m, a ≠ b → c ≠ d → e ≠ f →
    ¬(a = c ∧ b = d) → ¬(a = d ∧ b = c) → ¬(a = e ∧ b = f) → ¬(a = f ∧ b = e) →
    ¬(c = e ∧ d = f) → ¬(c = f ∧ d = e) →
    E b - E a + (E d - E c) = E f - E e →
    (b = c ∧ e = a ∧ f = d) ∨ (d = a ∧ e = c ∧ f = b)

/-- Distinct gaps make the spectrum injective. -/
lemma injective_of_gaps {E : Fin m → ℝ}
    (hgap : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d) :
    Function.Injective E := by
  intro a b hab
  by_contra hne
  have h := hgap a b b a hne (Ne.symm hne) (by linarith)
  exact hne h.1

/-- Equal gap sets and an injective source give every source gap a target pair. -/
lemma cover_of_gap_sets {E E' : Fin m → ℝ} (hinj : Function.Injective E)
    (hsets : Finset.image (fun q : Fin m × Fin m => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin m × Fin m => E' q.2 - E' q.1) Finset.univ) :
    ∀ a b : Fin m, a ≠ b → ∃ c d : Fin m, c ≠ d ∧ E' d - E' c = E b - E a := by
  intro a b hab
  have hmem : E b - E a ∈ Finset.image (fun q : Fin m × Fin m => E' q.2 - E' q.1) Finset.univ := by
    rw [← hsets]
    exact Finset.mem_image.mpr ⟨(a, b), Finset.mem_univ _, rfl⟩
  obtain ⟨q, _, hq⟩ := Finset.mem_image.mp hmem
  refine ⟨q.1, q.2, fun h => ?_, hq⟩
  have hq' : E' q.2 - E' q.1 = E b - E a := hq
  rw [h, sub_self] at hq'
  exact hab (hinj (by linarith))

/-- **The triangle step.** If the target pair of `(o, x)` is `(p, q)`, then the target pair of
`(o, y)` starts at `p` or ends at `q`. -/
theorem star_step {E E' : Fin m → ℝ}
    (hgap : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E')
    (hcover : ∀ a b : Fin m, a ≠ b → ∃ c d : Fin m, c ≠ d ∧ E' d - E' c = E b - E a)
    {o x y : Fin m} (hox : o ≠ x) (hoy : o ≠ y) (hxy : x ≠ y)
    {p q u v : Fin m} (hpq : p ≠ q) (huv : u ≠ v)
    (h1 : E' q - E' p = E x - E o) (h2 : E' v - E' u = E y - E o) :
    u = p ∨ v = q := by
  obtain ⟨r, s, hrs, h3⟩ := hcover x y hxy
  have hrel : E' q - E' p + (E' s - E' r) = E' v - E' u := by linarith
  have d1 : ¬(p = r ∧ q = s) := by
    rintro ⟨hpr, hqs⟩
    rw [hpr, hqs] at h1
    exact hox (hgap o x x y hox hxy (by linarith)).1
  have d2 : ¬(p = s ∧ q = r) := by
    rintro ⟨hps, hqr⟩
    rw [hps, hqr] at h1
    exact hoy (hgap o x y x hox (Ne.symm hxy) (by linarith)).1
  have d3 : ¬(p = u ∧ q = v) := by
    rintro ⟨hpu, hqv⟩
    rw [hpu, hqv] at h1
    exact hxy (hgap o x o y hox hoy (by linarith)).2
  have d4 : ¬(p = v ∧ q = u) := by
    rintro ⟨hpv, hqu⟩
    rw [hpv, hqu] at h1
    exact hoy (hgap o x y o hox (Ne.symm hoy) (by linarith)).1
  have d5 : ¬(r = u ∧ s = v) := by
    rintro ⟨hru, hsv⟩
    rw [hru, hsv] at h3
    exact hox (hgap x y o y hxy hoy (by linarith)).1.symm
  have d6 : ¬(r = v ∧ s = u) := by
    rintro ⟨hrv, hsu⟩
    rw [hrv, hsu] at h3
    exact hxy (hgap x y y o hxy (Ne.symm hoy) (by linarith)).1
  rcases hG4 p q r s u v hpq hrs huv d1 d2 d3 d4 d5 d6 hrel with
    ⟨_, hup, _⟩ | ⟨_, _, hvq⟩
  · exact Or.inl hup
  · exact Or.inr hvq

/-- **Spectral congruence from triangle genericity.** Distinct source gaps, (G4) for the target,
and a target pair for every source gap force the target to contain a translate of the source or
of its reflection. -/
theorem congruent_of_triangleGeneric (hm : 2 ≤ m) {E E' : Fin m → ℝ}
    (hgap : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E')
    (hcover : ∀ a b : Fin m, a ≠ b → ∃ c d : Fin m, c ≠ d ∧ E' d - E' c = E b - E a) :
    (∃ E₀ : ℝ, ∀ a, ∃ c, E' c = E a + E₀) ∨ (∃ E₀ : ℝ, ∀ a, ∃ c, E' c = -E a + E₀) := by
  obtain ⟨o, a₀, hoa⟩ : ∃ o a₀ : Fin m, o ≠ a₀ :=
    ⟨⟨0, by omega⟩, ⟨1, by omega⟩, fun h => by simp [Fin.ext_iff] at h⟩
  obtain ⟨p, q, hpq, hpq_eq⟩ := hcover o a₀ hoa
  by_cases hA : ∃ b, o ≠ b ∧ ∀ v, E' v - E' p ≠ E b - E o
  · by_cases hB : ∃ c, o ≠ c ∧ ∀ u, E' q - E' u ≠ E c - E o
    · exfalso
      obtain ⟨b, hob, hbA⟩ := hA
      obtain ⟨c, hoc, hcB⟩ := hB
      obtain ⟨ub, vb, hubvb, hb⟩ := hcover o b hob
      obtain ⟨uc, vc, hucvc, hc⟩ := hcover o c hoc
      have hab : a₀ ≠ b := fun h => hbA q (by rw [← h]; exact hpq_eq)
      have hac : a₀ ≠ c := fun h => hcB p (by rw [← h]; exact hpq_eq)
      have hvb : vb = q := by
        rcases star_step hgap hG4 hcover hoa hob hab hpq hubvb hpq_eq hb with h | h
        · exact (hbA vb (by rw [← h]; exact hb)).elim
        · exact h
      have huc : uc = p := by
        rcases star_step hgap hG4 hcover hoa hoc hac hpq hucvc hpq_eq hc with h | h
        · exact h
        · exact (hcB uc (by rw [← h]; exact hc)).elim
      have hbc : b ≠ c := fun h => hcB ub (by rw [← h, ← hvb]; exact hb)
      rcases star_step hgap hG4 hcover hob hoc hbc hubvb hucvc hb hc with h | h
      · exact hbA vb (by rw [← huc, h]; exact hb)
      · exact hcB uc (by rw [← hvb, ← h]; exact hc)
    · right
      refine ⟨E' q + E o, fun a => ?_⟩
      by_cases hoa' : o = a
      · exact ⟨q, by subst hoa'; ring⟩
      · have hex : ∃ u, E' q - E' u = E a - E o := by
          by_contra hne
          exact hB ⟨a, hoa', fun u hu => hne ⟨u, hu⟩⟩
        obtain ⟨u, hu⟩ := hex
        exact ⟨u, by linarith⟩
  · left
    refine ⟨E' p - E o, fun a => ?_⟩
    by_cases hoa' : o = a
    · exact ⟨p, by subst hoa'; ring⟩
    · have hex : ∃ v, E' v - E' p = E a - E o := by
        by_contra hne
        exact hA ⟨a, hoa', fun v hv => hne ⟨v, hv⟩⟩
      obtain ⟨v, hv⟩ := hex
      exact ⟨v, by linarith⟩

/-- A containment of an injective image in a spectrum on the same mode set is a relabelling. -/
lemma perm_of_cover (E' F : Fin m → ℝ) (hF : Function.Injective F)
    (h : ∀ a, ∃ c, E' c = F a) : ∃ τ : Equiv.Perm (Fin m), ∀ a, E' (τ a) = F a := by
  choose g hg using h
  have ginj : Function.Injective g := by
    intro a b hab
    apply hF
    rw [← hg a, ← hg b, hab]
  exact ⟨Equiv.ofBijective g (Finite.injective_iff_bijective.mp ginj),
    fun a => show E' (g a) = F a from hg a⟩

/-- **The spectral classification under (G4).** Real spectra on the same mode set, with
distinct source gaps, (G4) for the target and equal gap sets, are translation- or
reflection-congruent. -/
theorem spectral_classification_of_triangleGeneric (hm : 2 ≤ m) (E E' : Fin m → ℝ)
    (hgap : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E')
    (hsets : Finset.image (fun q : Fin m × Fin m => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin m × Fin m => E' q.2 - E' q.1) Finset.univ) :
    (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
    ∨ (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀) := by
  have hinj := injective_of_gaps hgap
  rcases congruent_of_triangleGeneric hm hgap hG4 (cover_of_gap_sets hinj hsets) with
    ⟨E₀, h⟩ | ⟨E₀, h⟩
  · obtain ⟨τ, hτ⟩ := perm_of_cover E' (fun a => E a + E₀)
      (fun a b hab => hinj (by simpa using hab)) h
    exact Or.inl ⟨τ, E₀, hτ⟩
  · obtain ⟨τ, hτ⟩ := perm_of_cover E' (fun a => -E a + E₀)
      (fun a b hab => hinj (by simpa using hab)) h
    exact Or.inr ⟨τ, E₀, hτ⟩

/-- **The spectral classification under (G4) for the source.** The roles of the two spectra
are symmetric: (G4) for the source and distinct target gaps give the same conclusion. -/
theorem spectral_classification_of_triangleGeneric_source (hm : 2 ≤ m) (E E' : Fin m → ℝ)
    (hgap' : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E)
    (hsets : Finset.image (fun q : Fin m × Fin m => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin m × Fin m => E' q.2 - E' q.1) Finset.univ) :
    (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
    ∨ (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀) := by
  rcases spectral_classification_of_triangleGeneric hm E' E hgap' hG4 hsets.symm with
    ⟨τ, E₀, h⟩ | ⟨τ, E₀, h⟩
  · refine Or.inl ⟨τ.symm, -E₀, fun a => ?_⟩
    have h' := h (τ.symm a)
    rw [Equiv.apply_symm_apply] at h'
    linarith
  · refine Or.inr ⟨τ.symm, E₀, fun a => ?_⟩
    have h' := h (τ.symm a)
    rw [Equiv.apply_symm_apply] at h'
    linarith

/-- **Phase locking along a congruence.** Equal transition probabilities, distinct gaps on both
sides and a translation- or reflection-congruence of the spectra give the two Hamiltonian
branches. Translation matches the pair `(a, b)` with `(τ a, τ b)` and yields `D H D† + E₀`;
reflection matches it with `(τ b, τ a)`, which conjugates its coefficient line, and yields
`−D H̄ D† + E₀`. Only the congruent reconstruction and the single-gap coefficient extraction are
used. -/
theorem twoBranch_of_congruence (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ,
      BohrFrequency.Umat V E t i j * star (BohrFrequency.Umat V E t i j)
        = BohrFrequency.Umat W E' t i j * star (BohrFrequency.Umat W E' t i j))
    (hcong : (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
      ∨ (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) := by
  rcases hcong with ⟨τ, E₀, halign⟩ | ⟨τ, E₀, halign⟩
  · left
    obtain ⟨d, hd, hmain⟩ := reconstruction_translation hm V W τ E E' E₀ hV hVnz halign
      (fun a b hab i j => by
        have hmatch : E' (τ b) - E' (τ a) = E b - E a := by
          rw [halign a, halign b]; ring
        have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
          (a := a) (b := b) (c := τ a) (d := τ b) hab
          (fun h => hab (τ.injective h)) hmatch i j
        simp only [Complex.star_def] at hline
        simp only [map_mul, Complex.conj_conj]
        linear_combination hline)
    exact ⟨E₀, d, hd, hmain⟩
  · right
    obtain ⟨d, hd, hmain⟩ := reconstruction_reflection hm V W τ E E' E₀ hV hVnz halign
      (fun a b hab i j => by
        have hmatch : E' (τ b) - E' (τ a) = E a - E b := by
          rw [halign a, halign b]; ring
        have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
          (a := b) (b := a) (c := τ a) (d := τ b) (Ne.symm hab)
          (fun h => hab (τ.injective h)) hmatch i j
        simp only [Complex.star_def] at hline
        simp only [map_mul, Complex.conj_conj]
        linear_combination hline)
    exact ⟨E₀, d, hd, hmain⟩

/-- **THE TWO-BRANCH THEOREM UNDER (G4).** Equal transition probabilities for all times, with
unitary eigenbases, non-vanishing overlaps and distinct gaps for both Hamiltonians and (G4) for
the second, give `H' = D H D† + E₀` or `H' = −D H̄ D† + E₀`. No classification premise; any
mode count `m ≥ 3`. -/
theorem twoBranch_of_triangleGeneric (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E')
    (hU : ∀ i j : Fin m, ∀ t : ℝ,
      BohrFrequency.Umat V E t i j * star (BohrFrequency.Umat V E t i j)
        = BohrFrequency.Umat W E' t i j * star (BohrFrequency.Umat W E' t i j)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) :=
  twoBranch_of_congruence hm V W E E' hV hVnz hgapV hgapW hU
    (spectral_classification_of_triangleGeneric (by omega) E E' hgapV hG4
      (gaps_eq_of_equal_probabilities (by omega) V W E E' hVnz hWnz hU))

/-- **THE TWO-BRANCH THEOREM UNDER (G4) FOR THE FIRST HAMILTONIAN.** As
`twoBranch_of_triangleGeneric`, with (G4) assumed for `H` instead of `H'`. -/
theorem twoBranch_of_triangleGeneric_source (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hG4 : TriangleGeneric E)
    (hU : ∀ i j : Fin m, ∀ t : ℝ,
      BohrFrequency.Umat V E t i j * star (BohrFrequency.Umat V E t i j)
        = BohrFrequency.Umat W E' t i j * star (BohrFrequency.Umat W E' t i j)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) :=
  twoBranch_of_congruence hm V W E E' hV hVnz hgapV hgapW hU
    (spectral_classification_of_triangleGeneric_source (by omega) E E' hgapW hG4
      (gaps_eq_of_equal_probabilities (by omega) V W E E' hVnz hWnz hU))

/-! ### Part 2: the sign-aware classification premise -/

/-- **The two branches from the sign-aware spectral premise.** The premise admits the
exceptional correspondence μ in either global orientation; the reversed orientation is the
positive one for the conjugated source eigenbasis, which `exceptional_impossible` excludes. -/
theorem twoBranch_of_signed_spectral_classification (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ,
      BohrFrequency.Umat V E t i j * star (BohrFrequency.Umat V E t i j)
        = BohrFrequency.Umat W E' t i j * star (BohrFrequency.Umat W E' t i j))
    (hclass :
      (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
      ∨ (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀)
      ∨ (∃ eS eT : Fin 6 ≃ Fin m, ∀ a b : Fin 6, a < b →
          E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS b) - E (eS a))
      ∨ (∃ eS eT : Fin 6 ≃ Fin m, ∀ a b : Fin 6, a < b →
          E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS a) - E (eS b))) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) := by
  rcases hclass with h | h | h | ⟨eS, eT, hspec⟩
  · exact twoBranch_of_spectral_classification hm V W E E' hV hW hVnz hWnz hgapV hgapW hU
      (Or.inl h)
  · exact twoBranch_of_spectral_classification hm V W E E' hV hW hVnz hWnz hgapV hgapW hU
      (Or.inr (Or.inl h))
  · exact twoBranch_of_spectral_classification hm V W E E' hV hW hVnz hWnz hgapV hgapW hU
      (Or.inr (Or.inr h))
  · exfalso
    refine exceptional_impossible (conjM V) W (conjM_unitary hV) hW
      (fun i a => by simpa [conjM_apply] using hVnz i a) hWnz
      ⟨eS, eS, eT, fun a b hab i j => ?_⟩
    have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
      (a := eS b) (b := eS a) (c := eT (mu a b).1) (d := eT (mu a b).2)
      (fun h => hab.ne' (eS.injective h))
      (fun h => (mu_gap a b hab).1.ne (eT.injective h)) (hspec a b hab) (eS i) (eS j)
    simp only [Complex.star_def] at hline
    simp only [conjM_apply, map_mul, Complex.conj_conj]
    linear_combination hline

/-- **The sign-aware integer premise.** Any two strictly increasing integer rulers with distinct
internal differences and equal difference sets that are neither translates nor reflections of one
another have six marks and realize μ or its global reversal through explicit relabelings, one
orientation for the whole pair. -/
def BGSignedClassification : Prop :=
  ∀ (n : ℕ) (F F' : Fin n → ℤ),
    StrictMono F → StrictMono F' →
    (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d) →
    (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d) →
    (Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ) →
    (¬ ∃ c : ℤ, ∀ i, F' i = F i + c) →
    (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) →
    ∃ eS eT : Fin 6 ≃ Fin n,
      (∀ a b : Fin 6, a < b → F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS b) - F (eS a))
      ∨ (∀ a b : Fin 6, a < b → F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS a) - F (eS b))

/-- The instance refuting the unsigned premise satisfies the sign-aware conclusion. -/
theorem signedForm_r1_r2refl : ∃ eS eT : Fin 6 ≃ Fin 6,
    (∀ a b : Fin 6, a < b →
      PremiseOrientation.r2refl (eT (mu a b).2) - PremiseOrientation.r2refl (eT (mu a b).1)
        = r1 (eS b) - r1 (eS a))
    ∨ (∀ a b : Fin 6, a < b →
      PremiseOrientation.r2refl (eT (mu a b).2) - PremiseOrientation.r2refl (eT (mu a b).1)
        = r1 (eS a) - r1 (eS b)) := by
  obtain ⟨eS, eT, h⟩ := PremiseOrientation.revMuForm_r1_r2refl
  exact ⟨eS, eT, Or.inr h⟩

/-- **The real spectral classification from the sign-aware premise**, through the real-to-integer
reduction; the surrogate's directed gap identities transport either orientation back. -/
theorem spectral_classification_of_signedBG (hBG : BGSignedClassification)
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
  rcases real_to_integer_surrogate E E' hgapE hgapE' hsets with htr | hrf |
    ⟨σ, σ', F, F', hFm, hF'm, hFg, hF'g, hFsets, hFnottr, hFnorf, transfer_gap⟩
  · exact Or.inl htr
  · exact Or.inr (Or.inl hrf)
  obtain ⟨eS, eT, hint | hint⟩ := hBG n F F' hFm hF'm hFg hF'g hFsets hFnottr hFnorf
  · refine Or.inr (Or.inr (Or.inl ⟨eS.trans σ, eT.trans σ', fun a b hab => ?_⟩))
    exact transfer_gap (eS a) (eS b) (eT (mu a b).1) (eT (mu a b).2)
      (fun h => hab.ne (eS.injective h)) (hint a b hab)
  · refine Or.inr (Or.inr (Or.inr ⟨eS.trans σ, eT.trans σ', fun a b hab => ?_⟩))
    exact transfer_gap (eS b) (eS a) (eT (mu a b).1) (eT (mu a b).2)
      (fun h => hab.ne' (eS.injective h)) (hint a b hab)

/-- **The two-branch theorem from the sign-aware integer premise.** Every step other than
`BGSignedClassification` is kernel-proved. -/
theorem twoBranch_of_BGSignedClassification (hBG : BGSignedClassification) (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ,
      BohrFrequency.Umat V E t i j * star (BohrFrequency.Umat V E t i j)
        = BohrFrequency.Umat W E' t i j * star (BohrFrequency.Umat W E' t i j)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) :=
  twoBranch_of_signed_spectral_classification hm V W E E' hV hW hVnz hWnz hgapV hgapW hU
    (spectral_classification_of_signedBG hBG E E' hgapV hgapW
      (gaps_eq_of_equal_probabilities (by omega) V W E E' hVnz hWnz hU))

#print axioms injective_of_gaps
#print axioms cover_of_gap_sets
#print axioms star_step
#print axioms congruent_of_triangleGeneric
#print axioms perm_of_cover
#print axioms spectral_classification_of_triangleGeneric
#print axioms spectral_classification_of_triangleGeneric_source
#print axioms twoBranch_of_congruence
#print axioms twoBranch_of_triangleGeneric
#print axioms twoBranch_of_triangleGeneric_source
#print axioms twoBranch_of_signed_spectral_classification
#print axioms signedForm_r1_r2refl
#print axioms spectral_classification_of_signedBG
#print axioms twoBranch_of_BGSignedClassification

end PairIdentification
end OIBridge
