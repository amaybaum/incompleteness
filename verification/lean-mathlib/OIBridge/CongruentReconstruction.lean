/-
  OIBridge/CongruentReconstruction.lean — the congruent-case assembly, and the conditional
  two-branch theorem with the Piccard classification as its only unproved premise.

  THE DIRECT ALGEBRA, NOT A HIDDEN DEPENDENCY. Given spectra aligned by a mode permutation τ
  (translation: E'_{τa} = E_a + E₀) and equality of every coefficient line, the route is four
  short steps, none of which needs angles, logarithms, 2π-quotients, or genericity:

    1. `modulus_rigid` — the diagonal coefficient lines give |r_{ia}||r_{ib}| = 1 for all a ≠ b
       of the ratio r_{ia} = W_{i,τa}/V_{ia}; for m ≥ 3 that forces every |r_{ia}| = 1. This is
       the ONE place the dimension enters, and it is why m = 2 needs separate treatment.
    2. `line_forcing` (from HomometricKill, dimension-independent) — each off-diagonal line
       gives W_{i,τa} conj(W_{i,τo}) = λ_a · V_{ia} conj(V_{io}) with λ_a unimodular.
    3. `phase_coboundary` — the ratio splits: W_{i,τa} = d_i β_a V_{ia} with d, β unimodular.
       This is the phase-coboundary theorem in its multiplicative form; no unitarity is needed.
    4. `reconstruction_translation` — the β's cancel in H' = W diag(E') W†, the E₀ term needs
       only V's unitarity, and H' = D H D† + E₀·1 falls out entrywise.

  The REFLECTION branch (`reconstruction_reflection`) is the translation branch applied to the
  entrywise-conjugated source model (V̄, −E): conjugating a coefficient line swaps its pair
  orientation, so the reflected matching C_W^{τa,τb} = C_V^{ba} is exactly the translated
  matching for V̄ — no duplicated proof.

  THE CONDITIONAL WRAPPER `twoBranch_of_PiccardClassification` isolates the one external input:
  its classification premise offers three alternatives — translation-congruent, reflection-
  congruent, or the six-mode exceptional match (stated via equivalences Fin 6 ≃ Fin m, which
  force m = 6 with no dependent casts) — and the third is REFUTED by `homometricSix_unrealizable`,
  leaving the two Hamiltonian branches. Everything internal is kernel-proved; the premise is what
  the Piccard/Bekir–Golomb turnpike classification (plus the frequency-matching layer of
  BohrFrequency and the μ-orbit bridge of probe M10) will eventually supply.

  DIMENSIONS 0, 1, 2. The main theorems hypothesize 3 ≤ m, and the printed Claim carries no
  lower-dimensional exclusion, so the small cases are dispatched explicitly:
  `reconstruction_dim_zero` and `reconstruction_dim_one` close m = 0, 1 outright (the latter
  needs W's unitarity and no coefficient data at all). m = 2 closes by the TWO-LEVEL DICHOTOMY:
  the diagonal coefficient line q(1−q) = p(1−p) factors as (q−p)(1−p−q) = 0, so each row's
  moduli match or swap, unitarity's column sums make the choice global
  (`dim_two_moduli_dichotomy`), and the swap IS the reflection branch — diag(E₁,E₀) =
  (E₀+E₁)·1 − diag(E₀,E₁) — giving `unitary2_line_dichotomy` (W∘τ = DVB or W∘τ∘swap = DV̄B)
  and `reconstruction_dim_two`. The hyperbola that blocks `modulus_rigid` at m = 2 is not a
  third alternative; it is exactly the swap.

  THE SPECTRAL WRAPPER `twoBranch_of_spectral_classification` goes one step further than the
  coefficient-level wrapper: its classification premise mentions ONLY spectra (translated,
  negated-translated, or realizing the exceptional gap correspondence μ), and every coefficient
  hypothesis is derived from equal transition probabilities via
  `BohrFrequency.coefficient_line_extraction` under the Golomb (all-gaps-distinct) hypotheses.
  Piccard classifies gap correspondences; quantum coefficient equality is a theorem, not an input.
-/
import OIBridge.HomometricKill
import OIBridge.EdgeRigidity
import OIBridge.FrequencyMatching
import Mathlib.Tactic.FieldSimp
import Mathlib.LinearAlgebra.FiniteDimensional.Basic

namespace OIBridge
namespace CongruentReconstruction

open Complex Matrix HomometricSix

local notation "conj'" => (starRingEnd ℂ)

variable {m : ℕ}

/-- A coefficient line's diagonal is the product of the two moduli. -/
lemma line_diag (z w : ℂ) :
    (z * conj' w) * conj' (z * conj' w) = ((normSq z * normSq w : ℝ) : ℂ) := by
  rw [map_mul, Complex.conj_conj]
  push_cast
  rw [← Complex.mul_conj, ← Complex.mul_conj]
  ring

/-- MODULUS RIGIDITY. If all pairwise products of a nonnegative vector are 1 and there are at
least three coordinates, every coordinate is 1. The m ≥ 3 hypothesis is sharp: at m = 2 the
hyperbola ρ₀ρ₁ = 1 survives. -/
lemma modulus_rigid (hm : 3 ≤ m) (ρ : Fin m → ℝ) (hnn : ∀ a, 0 ≤ ρ a)
    (hprod : ∀ a b, a ≠ b → ρ a * ρ b = 1) : ∀ a, ρ a = 1 := by
  have hpos : ∀ a, 0 < ρ a := by
    intro a
    obtain ⟨b, hb⟩ := exists_fresh ({a} : Finset (Fin m))
      (by rw [Finset.card_singleton]; omega)
    have hba : b ≠ a := by simpa using hb
    have h1 := hprod a b (Ne.symm hba)
    rcases (hnn a).lt_or_eq with h | h
    · exact h
    · exfalso
      rw [← h, zero_mul] at h1
      exact zero_ne_one h1
  have hall : ∀ a b : Fin m, ρ a = ρ b := by
    intro a b
    by_cases hab : a = b
    · rw [hab]
    · obtain ⟨c, hc⟩ := exists_fresh ({a, b} : Finset (Fin m))
        (lt_of_le_of_lt (Finset.card_insert_le _ _)
          (by rw [Finset.card_singleton]; omega))
      have hca : a ≠ c := fun h => hc (h ▸ Finset.mem_insert_self _ _)
      have hcb : b ≠ c := fun h =>
        hc (h ▸ Finset.mem_insert_of_mem (Finset.mem_singleton_self _))
      have h3 : ρ a * ρ c = ρ b * ρ c := by
        rw [hprod a c hca, hprod b c hcb]
      exact mul_right_cancel₀ (ne_of_gt (hpos c)) h3
  intro a
  obtain ⟨b, hb⟩ := exists_fresh ({a} : Finset (Fin m))
    (by rw [Finset.card_singleton]; omega)
  have hab : a ≠ b := fun h => hb (h ▸ Finset.mem_singleton_self a)
  have h1 := hprod a b hab
  rw [← hall a b] at h1
  have hfac : (ρ a - 1) * (ρ a + 1) = 0 := by linear_combination h1
  rcases mul_eq_zero.mp hfac with h | h
  · linarith
  · exfalso
    have := hpos a
    linarith

/-- MODULI MATCH from the diagonal coefficient lines, for m ≥ 3 — the only step of the whole
congruent assembly that needs the dimension. -/
theorem moduli_match (hm : 3 ≤ m) (V W : Matrix (Fin m) (Fin m) ℂ)
    (τ : Equiv.Perm (Fin m)) (hVnz : ∀ i a, V i a ≠ 0)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    ∀ i a, normSq (W i (τ a)) = normSq (V i a) := by
  intro i a
  have hprod : ∀ x y : Fin m, x ≠ y →
      (normSq (W i (τ x)) / normSq (V i x)) * (normSq (W i (τ y)) / normSq (V i y)) = 1 := by
    intro x y hxy
    have hcd := hC x y hxy i i
    rw [line_diag, line_diag] at hcd
    have hreal : normSq (W i (τ x)) * normSq (W i (τ y))
        = normSq (V i x) * normSq (V i y) := by exact_mod_cast hcd
    have hx : normSq (V i x) ≠ 0 := ne_of_gt (normSq_pos.mpr (hVnz i x))
    have hy : normSq (V i y) ≠ 0 := ne_of_gt (normSq_pos.mpr (hVnz i y))
    field_simp
    linarith [hreal]
  have hone := modulus_rigid hm (fun x => normSq (W i (τ x)) / normSq (V i x))
    (fun x => div_nonneg (normSq_nonneg _) (normSq_nonneg _)) hprod a
  have hVa : normSq (V i a) ≠ 0 := ne_of_gt (normSq_pos.mpr (hVnz i a))
  field_simp at hone
  exact hone

/-- THE PHASE-COBOUNDARY THEOREM, moduli-hypothesis core: needs only a nonempty mode set. The
dimension enters this file solely through `moduli_match`; every dimension where the moduli can
be matched (m ≥ 3 generically, m = 2 by the two-level dichotomy) inherits the splitting. -/
theorem phase_coboundary_of_moduli (hm0 : 0 < m) (V W : Matrix (Fin m) (Fin m) ℂ)
    (τ : Equiv.Perm (Fin m)) (hVnz : ∀ i a, V i a ≠ 0)
    (hmod : ∀ i a, normSq (W i (τ a)) = normSq (V i a))
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    ∃ d β : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧ (∀ a, β a * conj' (β a) = 1)
      ∧ ∀ i a, W i (τ a) = d i * β a * V i a := by
  set o : Fin m := ⟨0, hm0⟩ with ho
  have hWnz : ∀ i a, W i (τ a) ≠ 0 := by
    intro i a
    intro hzero
    apply hVnz i a
    have := hmod i a
    rw [hzero, map_zero] at this
    exact normSq_eq_zero.mp this.symm
  -- step 2: unimodular line scalars against the reference column o
  have hlam : ∀ a : Fin m, a ≠ o → ∃ lam : ℂ, lam * conj' lam = 1
      ∧ ∀ i, W i (τ a) * conj' (W i (τ o)) = lam * (V i a * conj' (V i o)) := by
    intro a ha
    exact line_forcing (fun i => V i a * conj' (V i o))
      (fun i => W i (τ a) * conj' (W i (τ o))) o
      (mul_ne_zero (hVnz o a) (by simpa using hVnz o o))
      (fun i j => hC a o ha i j)
  choose lam hlamu hlamr using hlam
  -- step 3: the splitting
  refine ⟨fun i => W i (τ o) * conj' (V i o) / ((normSq (V i o) : ℝ) : ℂ),
    fun a => if ha : a = o then 1 else lam a ha, ?_, ?_, ?_⟩
  · intro i
    have hV0 : ((normSq (V i o) : ℝ) : ℂ) ≠ 0 := by
      exact_mod_cast ne_of_gt (normSq_pos.mpr (hVnz i o))
    rw [map_div₀, map_mul, Complex.conj_conj]
    have hcr : conj' ((normSq (V i o) : ℝ) : ℂ) = ((normSq (V i o) : ℝ) : ℂ) :=
      Complex.conj_ofReal _
    rw [hcr]
    rw [div_mul_div_comm, div_eq_one_iff_eq (mul_ne_zero hV0 hV0)]
    have h1 : W i (τ o) * conj' (W i (τ o)) = ((normSq (W i (τ o)) : ℝ) : ℂ) :=
      Complex.mul_conj _
    have h2 : V i o * conj' (V i o) = ((normSq (V i o) : ℝ) : ℂ) := Complex.mul_conj _
    calc W i (τ o) * conj' (V i o) * (conj' (W i (τ o)) * V i o)
        = (W i (τ o) * conj' (W i (τ o))) * (V i o * conj' (V i o)) := by ring
      _ = ((normSq (W i (τ o)) : ℝ) : ℂ) * ((normSq (V i o) : ℝ) : ℂ) := by rw [h1, h2]
      _ = ((normSq (V i o) : ℝ) : ℂ) * ((normSq (V i o) : ℝ) : ℂ) := by rw [hmod i o]
  · intro a
    dsimp only
    by_cases ha : a = o
    · rw [dif_pos ha]
      norm_num
    · rw [dif_neg ha]
      exact hlamu a ha
  · intro i a
    dsimp only
    by_cases ha : a = o
    · rw [ha, dif_pos rfl, mul_one]
      have hV0 : ((normSq (V i o) : ℝ) : ℂ) ≠ 0 := by
        exact_mod_cast ne_of_gt (normSq_pos.mpr (hVnz i o))
      rw [div_mul_eq_mul_div, eq_div_iff hV0]
      have h2 : V i o * conj' (V i o) = ((normSq (V i o) : ℝ) : ℂ) := Complex.mul_conj _
      calc W i (τ o) * ((normSq (V i o) : ℝ) : ℂ) = W i (τ o) * (V i o * conj' (V i o)) := by
            rw [h2]
        _ = W i (τ o) * conj' (V i o) * V i o := by ring
    · rw [dif_neg ha]
      have hr := hlamr a ha i
      have hV0 : ((normSq (V i o) : ℝ) : ℂ) ≠ 0 := by
        exact_mod_cast ne_of_gt (normSq_pos.mpr (hVnz i o))
      have hW0c : conj' (W i (τ o)) ≠ 0 := by simpa using hWnz i o
      rw [div_mul_eq_mul_div, div_mul_eq_mul_div, eq_div_iff hV0]
      -- W_{iτa} · normSq(V_io) = (W_{iτo} conj(V_io) · λ_a · V_ia) — verify by multiplying hr
      apply mul_right_cancel₀ hW0c
      have h1 : W i (τ o) * conj' (W i (τ o)) = ((normSq (W i (τ o)) : ℝ) : ℂ) :=
        Complex.mul_conj _
      calc W i (τ a) * ((normSq (V i o) : ℝ) : ℂ) * conj' (W i (τ o))
          = (W i (τ a) * conj' (W i (τ o))) * ((normSq (V i o) : ℝ) : ℂ) := by ring
        _ = lam a ha * (V i a * conj' (V i o)) * ((normSq (V i o) : ℝ) : ℂ) := by rw [hr]
        _ = lam a ha * (V i a * conj' (V i o)) * ((normSq (W i (τ o)) : ℝ) : ℂ) := by
              rw [hmod i o]
        _ = lam a ha * (V i a * conj' (V i o)) * (W i (τ o) * conj' (W i (τ o))) := by
              rw [h1]
        _ = W i (τ o) * conj' (V i o) * lam a ha * V i a * conj' (W i (τ o)) := by ring

/-- The phase-coboundary theorem at m ≥ 3: moduli match by rigidity, then split. -/
theorem phase_coboundary (hm : 3 ≤ m) (V W : Matrix (Fin m) (Fin m) ℂ)
    (τ : Equiv.Perm (Fin m)) (hVnz : ∀ i a, V i a ≠ 0)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    ∃ d β : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧ (∀ a, β a * conj' (β a) = 1)
      ∧ ∀ i a, W i (τ a) = d i * β a * V i a :=
  phase_coboundary_of_moduli (by omega) V W τ hVnz (moduli_match hm V W τ hVnz hC) hC

/-- Entry form of a spectral sandwich. -/
lemma spectral_apply (M : Matrix (Fin m) (Fin m) ℂ) (f : Fin m → ℂ) (i j : Fin m) :
    (M * Matrix.diagonal f * Mᴴ) i j = ∑ c, M i c * f c * conj' (M j c) := by
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply, Complex.star_def]

/-- Row orthonormality in sum form. -/
lemma row_sums (V : Matrix (Fin m) (Fin m) ℂ) (hV : V * Vᴴ = 1) (i j : Fin m) :
    (∑ a, V i a * conj' (V j a)) = if i = j then 1 else 0 := by
  have h := congrFun (congrFun hV i) j
  rw [Matrix.mul_apply] at h
  simp only [Matrix.conjTranspose_apply, Complex.star_def] at h
  rw [h, Matrix.one_apply]

/-- BRANCH ONE, moduli-hypothesis core. Aligned spectra plus coefficient-line equality give
`H' = D H D† + E₀·1` with `D` a unimodular diagonal. Only V's unitarity is used. -/
theorem reconstruction_translation_of_moduli (hm0 : 0 < m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (τ : Equiv.Perm (Fin m))
    (E E' : Fin m → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (hmod : ∀ i a, normSq (W i (τ a)) = normSq (V i a))
    (halign : ∀ a, E' (τ a) = E a + E₀)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1 := by
  obtain ⟨d, β, hd, hβ, hcob⟩ := phase_coboundary_of_moduli hm0 V W τ hVnz hmod hC
  refine ⟨d, hd, ?_⟩
  ext i j
  have hterm : ∀ a : Fin m, W i (τ a) * ((E' (τ a) : ℝ) : ℂ) * conj' (W j (τ a))
      = (d i * conj' (d j)) * (V i a * ((E a : ℝ) : ℂ) * conj' (V j a))
        + ((E₀ : ℝ) : ℂ) * ((d i * conj' (d j)) * (V i a * conj' (V j a))) := by
    intro a
    rw [hcob i a, hcob j a]
    have hE : ((E' (τ a) : ℝ) : ℂ) = ((E a : ℝ) : ℂ) + ((E₀ : ℝ) : ℂ) := by
      rw [halign a]
      push_cast
      ring
    rw [hE]
    simp only [map_mul]
    linear_combination (d i * conj' (d j) * (V i a * conj' (V j a))
      * (((E a : ℝ) : ℂ) + ((E₀ : ℝ) : ℂ))) * hβ a
  have hδ := row_sums V hV i j
  calc (W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ) i j
      = ∑ c, W i c * ((E' c : ℝ) : ℂ) * conj' (W j c) := spectral_apply W _ i j
    _ = ∑ a, W i (τ a) * ((E' (τ a) : ℝ) : ℂ) * conj' (W j (τ a)) :=
        (Equiv.sum_comp τ (fun c => W i c * ((E' c : ℝ) : ℂ) * conj' (W j c))).symm
    _ = ∑ a, ((d i * conj' (d j)) * (V i a * ((E a : ℝ) : ℂ) * conj' (V j a))
          + ((E₀ : ℝ) : ℂ) * ((d i * conj' (d j)) * (V i a * conj' (V j a)))) :=
        Finset.sum_congr rfl (fun a _ => hterm a)
    _ = (d i * conj' (d j)) * (∑ a, V i a * ((E a : ℝ) : ℂ) * conj' (V j a))
          + ((E₀ : ℝ) : ℂ) * ((d i * conj' (d j)) * (∑ a, V i a * conj' (V j a))) := by
        rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum]
    _ = (Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
          * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1) i j := by
        rw [hδ]
        rw [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply]
        rw [Matrix.diagonal_conjTranspose]
        rw [Matrix.mul_diagonal, Matrix.diagonal_mul]
        rw [spectral_apply V _ i j]
        rw [Pi.star_apply, Complex.star_def]
        by_cases hij : i = j
        · rw [if_pos hij, hij]
          simp only [smul_eq_mul]
          push_cast
          linear_combination ((E₀ : ℝ) : ℂ) * hd j
        · rw [if_neg hij]
          simp only [smul_eq_mul]
          push_cast
          ring

/-- BRANCH ONE at m ≥ 3. -/
theorem reconstruction_translation (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (τ : Equiv.Perm (Fin m))
    (E E' : Fin m → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (halign : ∀ a, E' (τ a) = E a + E₀)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1 :=
  reconstruction_translation_of_moduli (by omega) V W τ E E' E₀ hV hVnz
    (moduli_match hm V W τ hVnz hC) halign hC

/-- Entrywise conjugation of a matrix. -/
noncomputable def conjM (M : Matrix (Fin m) (Fin m) ℂ) : Matrix (Fin m) (Fin m) ℂ :=
  M.map (starRingEnd ℂ)

lemma conjM_apply (M : Matrix (Fin m) (Fin m) ℂ) (i j : Fin m) :
    conjM M i j = conj' (M i j) := rfl

lemma conjM_unitary {M : Matrix (Fin m) (Fin m) ℂ} (hM : M * Mᴴ = 1) :
    conjM M * (conjM M)ᴴ = 1 := by
  ext i j
  have h := congrFun (congrFun hM i) j
  rw [Matrix.mul_apply] at h ⊢
  simp only [Matrix.conjTranspose_apply, Complex.star_def] at h
  simp only [Matrix.conjTranspose_apply, Complex.star_def, conjM_apply, Complex.conj_conj]
  have hsum : (∑ c, conj' (M i c) * M j c) = conj' (∑ c, M i c * conj' (M j c)) := by
    rw [map_sum]
    exact Finset.sum_congr rfl (fun c _ => by rw [map_mul, Complex.conj_conj])
  rw [hsum, h, Matrix.one_apply]
  by_cases hij : i = j
  · rw [if_pos hij, map_one]
  · rw [if_neg hij, map_zero]

/-- BRANCH TWO, moduli-hypothesis core, by conjugation of branch one. Reflected spectra plus
coefficient-line equality with the pair orientation swapped give `H' = −(D H̄ D†) + E₀·1`. -/
theorem reconstruction_reflection_of_moduli (hm0 : 0 < m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (τ : Equiv.Perm (Fin m))
    (E E' : Fin m → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (hmod : ∀ i a, normSq (W i (τ a)) = normSq (V i a))
    (halign : ∀ a, E' (τ a) = -E a + E₀)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i b * conj' (V i a)) * conj' (V j b * conj' (V j a))) :
    ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d
              * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
              * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1 := by
  -- apply branch one to the conjugated source model (V̄, −E)
  obtain ⟨d, hd, hmain⟩ := reconstruction_translation_of_moduli hm0 (conjM V) W τ
    (fun a => -E a) E' E₀ (conjM_unitary hV)
    (fun i a => by simpa [conjM_apply] using hVnz i a)
    (fun i a => by rw [conjM_apply, Complex.normSq_conj]; exact hmod i a)
    (fun a => by rw [halign a])
    (by
      intro a b hab i j
      have hswap := hC a b hab i j
      rw [hswap]
      simp only [conjM_apply, map_mul, Complex.conj_conj]
      ring)
  refine ⟨d, hd, ?_⟩
  rw [hmain]
  congr 1
  -- diagonal d * (V̄ diag(−E) V̄ᴴ) * ... = −(diagonal d * conjM(V diag E Vᴴ) * ...)
  have hcore : conjM V * Matrix.diagonal (fun a => ((-E a : ℝ) : ℂ)) * (conjM V)ᴴ
      = -(conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)) := by
    ext i j
    rw [spectral_apply]
    rw [Matrix.neg_apply, conjM_apply]
    rw [spectral_apply]
    rw [map_sum, ← Finset.sum_neg_distrib]
    refine Finset.sum_congr rfl (fun c _ => ?_)
    simp only [conjM_apply, map_mul, Complex.conj_conj, Complex.conj_ofReal]
    push_cast
    ring
  rw [hcore]
  rw [Matrix.mul_neg, Matrix.neg_mul]

/-- BRANCH TWO at m ≥ 3. The moduli still match directly: the swapped-orientation lines have the
same diagonal products. -/
theorem reconstruction_reflection (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (τ : Equiv.Perm (Fin m))
    (E E' : Fin m → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (halign : ∀ a, E' (τ a) = -E a + E₀)
    (hC : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i b * conj' (V i a)) * conj' (V j b * conj' (V j a))) :
    ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d
              * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
              * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1 := by
  have hCconj : ∀ a b : Fin m, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (conjM V i a * conj' (conjM V i b)) * conj' (conjM V j a * conj' (conjM V j b)) := by
    intro a b hab i j
    rw [hC a b hab i j]
    simp only [conjM_apply, map_mul, Complex.conj_conj]
    ring
  have hmod : ∀ i a, normSq (W i (τ a)) = normSq (V i a) := by
    intro i a
    have := moduli_match hm (conjM V) W τ
      (fun i a => by simpa [conjM_apply] using hVnz i a) hCconj i a
    rwa [conjM_apply, Complex.normSq_conj] at this
  exact reconstruction_reflection_of_moduli (by omega) V W τ E E' E₀ hV hVnz hmod halign hC

/-- Dimension 0: vacuous. -/
theorem reconstruction_dim_zero (V W : Matrix (Fin 0) (Fin 0) ℂ) (E E' : Fin 0 → ℝ) (E₀ : ℝ) :
    W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
      = Matrix.diagonal (fun _ => (1 : ℂ))
          * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
          * (Matrix.diagonal (fun _ => (1 : ℂ)))ᴴ + (E₀ : ℂ) • 1 := by
  ext i j
  exact i.elim0

/-- Dimension 1: no coefficient data is needed at all — both unitarity conditions pin the single
entry, and the branch is the identity phase. -/
theorem reconstruction_dim_one (V W : Matrix (Fin 1) (Fin 1) ℂ) (E E' : Fin 1 → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1) (halign : E' 0 = E 0 + E₀) :
    W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
      = Matrix.diagonal (fun _ => (1 : ℂ))
          * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
          * (Matrix.diagonal (fun _ => (1 : ℂ)))ᴴ + (E₀ : ℂ) • 1 := by
  have hWu : W 0 0 * conj' (W 0 0) = 1 := by
    have hrow := row_sums W hW 0 0
    rw [if_pos rfl, Fin.sum_univ_one] at hrow
    exact hrow
  have hVu : V 0 0 * conj' (V 0 0) = 1 := by
    have hrow := row_sums V hV 0 0
    rw [if_pos rfl, Fin.sum_univ_one] at hrow
    exact hrow
  ext i j
  have hi : i = 0 := Subsingleton.elim i 0
  have hj : j = 0 := Subsingleton.elim j 0
  rw [hi, hj]
  rw [Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, if_pos rfl]
  rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul]
  rw [spectral_apply W _ 0 0, spectral_apply V _ 0 0]
  rw [Fin.sum_univ_one, Fin.sum_univ_one]
  rw [Pi.star_apply, Complex.star_def]
  have hE : ((E' 0 : ℝ) : ℂ) = ((E 0 : ℝ) : ℂ) + ((E₀ : ℝ) : ℂ) := by
    rw [halign]
    push_cast
    ring
  rw [hE]
  simp only [smul_eq_mul, map_one]
  linear_combination (((E 0 : ℝ) : ℂ) + ((E₀ : ℝ) : ℂ)) * hWu - ((E 0 : ℝ) : ℂ) * hVu

/-! ### Dimension two: the dichotomy that closes the last small case -/

/-- Row sums of a unitary in `normSq` form, reindexed along a permutation. -/
lemma normSq_row_sum {k : ℕ} (M : Matrix (Fin k) (Fin k) ℂ) (hM : M * Mᴴ = 1)
    (τ : Equiv.Perm (Fin k)) (i : Fin k) :
    (∑ a, normSq (M i (τ a))) = 1 := by
  have h := row_sums M hM i i
  rw [if_pos rfl] at h
  have hre : (∑ a, M i (τ a) * conj' (M i (τ a))) = 1 := by
    rw [Equiv.sum_comp τ (fun c => M i c * conj' (M i c))]
    exact h
  have hcast : (∑ a, ((normSq (M i (τ a)) : ℝ) : ℂ)) = 1 := by
    rw [← hre]
    exact Finset.sum_congr rfl fun a _ => (Complex.mul_conj _).symm
  exact_mod_cast hcast

/-- Column sums of a unitary in `normSq` form. -/
lemma normSq_col_sum {k : ℕ} (M : Matrix (Fin k) (Fin k) ℂ) (hM : M * Mᴴ = 1) (c : Fin k) :
    (∑ i, normSq (M i c)) = 1 := by
  have hM' := mul_eq_one_comm.mp hM
  have h := congrFun (congrFun hM' c) c
  rw [Matrix.mul_apply] at h
  simp only [Matrix.conjTranspose_apply, Complex.star_def] at h
  rw [Matrix.one_apply, if_pos rfl] at h
  have hre : (∑ i, M i c * conj' (M i c)) = 1 := by
    rw [← h]
    exact Finset.sum_congr rfl fun i _ => mul_comm _ _
  have hcast : (∑ i, ((normSq (M i c) : ℝ) : ℂ)) = 1 := by
    rw [← hre]
    exact Finset.sum_congr rfl fun i _ => (Complex.mul_conj _).symm
  exact_mod_cast hcast

/-- THE TWO-LEVEL MODULUS DICHOTOMY. At m = 2 the diagonal coefficient line factors as
`(q − p)(1 − p − q) = 0`, so each row's moduli either match or swap; unitarity's column sums
force the choice to be global. The apparent hyperbola of `modulus_rigid` is not a third branch —
it is exactly the swap. -/
theorem dim_two_moduli_dichotomy (V W : Matrix (Fin 2) (Fin 2) ℂ) (τ : Equiv.Perm (Fin 2))
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hC : ∀ a b : Fin 2, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    (∀ i a, normSq (W i (τ a)) = normSq (V i a))
    ∨ (∀ i a, normSq (W i (τ (Equiv.swap 0 1 a))) = normSq (V i a)) := by
  have hVrow : ∀ i : Fin 2, normSq (V i 0) + normSq (V i 1) = 1 := by
    intro i
    have := normSq_row_sum V hV (Equiv.refl _) i
    rwa [Fin.sum_univ_two] at this
  have hWrow : ∀ i : Fin 2, normSq (W i (τ 0)) + normSq (W i (τ 1)) = 1 := by
    intro i
    have := normSq_row_sum W hW τ i
    rwa [Fin.sum_univ_two] at this
  have hVcol : normSq (V 0 0) + normSq (V 1 0) = 1 := by
    have := normSq_col_sum V hV 0
    rwa [Fin.sum_univ_two] at this
  have hWcol : normSq (W 0 (τ 0)) + normSq (W 1 (τ 0)) = 1 := by
    have := normSq_col_sum W hW (τ 0)
    rwa [Fin.sum_univ_two] at this
  have hdich : ∀ i : Fin 2,
      normSq (W i (τ 0)) = normSq (V i 0) ∨ normSq (W i (τ 0)) = 1 - normSq (V i 0) := by
    intro i
    have hcd := hC 0 1 (by decide) i i
    rw [line_diag, line_diag] at hcd
    have hreal : normSq (W i (τ 0)) * normSq (W i (τ 1))
        = normSq (V i 0) * normSq (V i 1) := by exact_mod_cast hcd
    have h1 : normSq (W i (τ 1)) = 1 - normSq (W i (τ 0)) := by linarith [hWrow i]
    have h2 : normSq (V i 1) = 1 - normSq (V i 0) := by linarith [hVrow i]
    rw [h1, h2] at hreal
    have hfac : (normSq (W i (τ 0)) - normSq (V i 0))
        * (1 - normSq (V i 0) - normSq (W i (τ 0))) = 0 := by
      linear_combination hreal
    rcases mul_eq_zero.mp hfac with h | h
    · left; linarith
    · right; linarith
  -- reduce mixed rows to the pure cases through the column sums
  have hsame : (normSq (W 0 (τ 0)) = normSq (V 0 0) ∧ normSq (W 1 (τ 0)) = normSq (V 1 0))
      ∨ (normSq (W 0 (τ 0)) = 1 - normSq (V 0 0)
          ∧ normSq (W 1 (τ 0)) = 1 - normSq (V 1 0)) := by
    rcases hdich 0 with h0 | h0 <;> rcases hdich 1 with h1 | h1
    · exact Or.inl ⟨h0, h1⟩
    · -- mixed forces the half-half degeneracy, which lands in BOTH cases
      exact Or.inl ⟨h0, by linarith [hWcol, hVcol]⟩
    · exact Or.inl ⟨by linarith [hWcol, hVcol], h1⟩
    · exact Or.inr ⟨h0, h1⟩
  have hswap : ∀ a : Fin 2, τ (Equiv.swap 0 1 a) = τ (Equiv.swap 0 1 a) := fun _ => rfl
  rcases hsame with ⟨h0, h1⟩ | ⟨h0, h1⟩
  · left
    intro i a
    fin_cases i <;> fin_cases a
    · exact h0
    · show normSq (W 0 (τ 1)) = normSq (V 0 1)
      have := hWrow 0; have := hVrow 0; linarith
    · exact h1
    · show normSq (W 1 (τ 1)) = normSq (V 1 1)
      have := hWrow 1; have := hVrow 1; linarith
  · right
    intro i a
    fin_cases i <;> fin_cases a
    · show normSq (W 0 (τ (Equiv.swap 0 1 0))) = normSq (V 0 0)
      rw [Equiv.swap_apply_left]
      have := hWrow 0; linarith
    · show normSq (W 0 (τ (Equiv.swap 0 1 1))) = normSq (V 0 1)
      rw [Equiv.swap_apply_right]
      have := hVrow 0; linarith
    · show normSq (W 1 (τ (Equiv.swap 0 1 0))) = normSq (V 1 0)
      rw [Equiv.swap_apply_left]
      have := hWrow 1; linarith
    · show normSq (W 1 (τ (Equiv.swap 0 1 1))) = normSq (V 1 1)
      rw [Equiv.swap_apply_right]
      have := hVrow 1; linarith

/-- THE TWO-LEVEL LINE DICHOTOMY: `W∘τ = D V B` or `W∘τ∘swap = D V̄ B` with `D`, `B` diagonal
unimodular. The swap branch carries entrywise conjugation — it is the reflection branch in
matrix form, exactly as the two-branch Claim demands. -/
theorem unitary2_line_dichotomy (V W : Matrix (Fin 2) (Fin 2) ℂ) (τ : Equiv.Perm (Fin 2))
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (hC : ∀ a b : Fin 2, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    (∃ d β : Fin 2 → ℂ, (∀ i, d i * conj' (d i) = 1) ∧ (∀ a, β a * conj' (β a) = 1)
      ∧ ∀ i a, W i (τ a) = d i * β a * V i a)
    ∨ (∃ d β : Fin 2 → ℂ, (∀ i, d i * conj' (d i) = 1) ∧ (∀ a, β a * conj' (β a) = 1)
      ∧ ∀ i a, W i (τ (Equiv.swap 0 1 a)) = d i * β a * conj' (V i a)) := by
  rcases dim_two_moduli_dichotomy V W τ hV hW hC with hmod | hmod
  · exact Or.inl (phase_coboundary_of_moduli (by omega) V W τ hVnz hmod hC)
  · right
    set τ' : Equiv.Perm (Fin 2) := (Equiv.swap 0 1).trans τ with hτ'
    have hτ'app : ∀ a, τ' a = τ (Equiv.swap 0 1 a) := fun a => rfl
    have hC' : ∀ a b : Fin 2, a ≠ b → ∀ i j,
        (W i (τ' a) * conj' (W i (τ' b))) * conj' (W j (τ' a) * conj' (W j (τ' b)))
          = (conjM V i a * conj' (conjM V i b)) * conj' (conjM V j a * conj' (conjM V j b)) := by
      intro a b hab i j
      rw [hτ'app a, hτ'app b]
      have hσ : Equiv.swap 0 1 a ≠ Equiv.swap 0 1 b := fun h => hab ((Equiv.swap 0 1).injective h)
      have hval := hC (Equiv.swap 0 1 a) (Equiv.swap 0 1 b) hσ i j
      rw [hval]
      have hσa : Equiv.swap 0 1 a = b := by
        fin_cases a <;> fin_cases b <;> first | (exact absurd rfl hab) | rfl
      have hσb : Equiv.swap 0 1 b = a := by
        fin_cases a <;> fin_cases b <;> first | (exact absurd rfl hab) | rfl
      rw [hσa, hσb]
      simp only [conjM_apply, map_mul, Complex.conj_conj]
      ring
    have hmod' : ∀ i a, normSq (W i (τ' a)) = normSq (conjM V i a) := by
      intro i a
      rw [hτ'app a, conjM_apply, Complex.normSq_conj]
      exact hmod i a
    obtain ⟨d, β, hd, hβ, hcob⟩ := phase_coboundary_of_moduli (by omega) (conjM V) W τ'
      (fun i a => by simpa [conjM_apply] using hVnz i a) hmod' hC'
    exact ⟨d, β, hd, hβ, fun i a => hcob i a⟩

/-- DIMENSION TWO CLOSES: translation-aligned data at m = 2 yields one of the two printed
branches — the second with the shifted origin `E⋆ = E₀ + E₀' + E₀''`. The hyperbola that blocks
`modulus_rigid` is precisely the reflection branch, not a third alternative. -/
theorem reconstruction_dim_two (V W : Matrix (Fin 2) (Fin 2) ℂ) (τ : Equiv.Perm (Fin 2))
    (E E' : Fin 2 → ℝ) (E₀ : ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1) (hVnz : ∀ i a, V i a ≠ 0)
    (halign : ∀ a, E' (τ a) = E a + E₀)
    (hC : ∀ a b : Fin 2, a ≠ b → ∀ i j,
      (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
        = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b))) :
    (∃ d : Fin 2 → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ Estar : ℝ, ∃ d : Fin 2 → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (Estar : ℂ) • 1) := by
  rcases dim_two_moduli_dichotomy V W τ hV hW hC with hmod | hmod
  · exact Or.inl (reconstruction_translation_of_moduli (by omega) V W τ E E' E₀
      hV hVnz hmod halign hC)
  · right
    refine ⟨E 0 + E 1 + E₀, ?_⟩
    set τ' : Equiv.Perm (Fin 2) := (Equiv.swap 0 1).trans τ with hτ'
    have hτ'app : ∀ a, τ' a = τ (Equiv.swap 0 1 a) := fun a => rfl
    have halign' : ∀ a, E' (τ' a) = -E a + (E 0 + E 1 + E₀) := by
      intro a
      fin_cases a
      · show E' (τ' 0) = -E 0 + (E 0 + E 1 + E₀)
        rw [hτ'app 0, Equiv.swap_apply_left, halign 1]
        ring
      · show E' (τ' 1) = -E 1 + (E 0 + E 1 + E₀)
        rw [hτ'app 1, Equiv.swap_apply_right, halign 0]
        ring
    have hmod' : ∀ i a, normSq (W i (τ' a)) = normSq (V i a) := by
      intro i a
      rw [hτ'app a]
      exact hmod i a
    have hC' : ∀ a b : Fin 2, a ≠ b → ∀ i j,
        (W i (τ' a) * conj' (W i (τ' b))) * conj' (W j (τ' a) * conj' (W j (τ' b)))
          = (V i b * conj' (V i a)) * conj' (V j b * conj' (V j a)) := by
      intro a b hab i j
      rw [hτ'app a, hτ'app b]
      have hσ : Equiv.swap 0 1 a ≠ Equiv.swap 0 1 b := fun h => hab ((Equiv.swap 0 1).injective h)
      have hval := hC (Equiv.swap 0 1 a) (Equiv.swap 0 1 b) hσ i j
      rw [hval]
      have hσa : Equiv.swap 0 1 a = b := by
        fin_cases a <;> fin_cases b <;> first | (exact absurd rfl hab) | rfl
      have hσb : Equiv.swap 0 1 b = a := by
        fin_cases a <;> fin_cases b <;> first | (exact absurd rfl hab) | rfl
      rw [hσa, hσb]
    exact reconstruction_reflection_of_moduli (by omega) V W τ' E E' (E 0 + E 1 + E₀)
      hV hVnz hmod' halign' hC'

/-- The exceptional six-mode coefficient match, stated through equivalences `Fin 6 ≃ Fin m` so
that it forces `m = 6` with no dependent casts: relabelings of rows, source modes, and target
modes realize the standard homometric correspondence `mu` at the coefficient level. When the
Piccard classification is consumed, its exceptional six-mark family must be verified (from the
primary formula) to induce exactly this μ-orbit — the finite bridge probe M10 anticipates. -/
def ExceptionalMatch (V W : Matrix (Fin m) (Fin m) ℂ) : Prop :=
  ∃ eR eS eT : Fin 6 ≃ Fin m, ∀ a b : Fin 6, a < b → ∀ i j : Fin 6,
    (W (eR i) (eT (mu a b).1) * conj' (W (eR i) (eT (mu a b).2)))
      * conj' (W (eR j) (eT (mu a b).1) * conj' (W (eR j) (eT (mu a b).2)))
    = (V (eR i) (eS a) * conj' (V (eR i) (eS b)))
      * conj' (V (eR j) (eS a) * conj' (V (eR j) (eS b)))

/-- The exceptional alternative is impossible: transport along the equivalences lands exactly in
the hypotheses of `homometricSix_unrealizable`. -/
theorem exceptional_impossible (V W : Matrix (Fin m) (Fin m) ℂ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hex : ExceptionalMatch V W) : False := by
  obtain ⟨eR, eS, eT, hmatch⟩ := hex
  have transport : ∀ (M : Matrix (Fin m) (Fin m) ℂ) (e : Fin 6 ≃ Fin m), M * Mᴴ = 1 →
      (Matrix.of fun i a => M (eR i) (e a)) * (Matrix.of fun i a => M (eR i) (e a))ᴴ = 1 := by
    intro M e hM
    ext i j
    rw [Matrix.mul_apply]
    simp only [Matrix.conjTranspose_apply, Complex.star_def, Matrix.of_apply]
    have hrow := row_sums M hM (eR i) (eR j)
    calc (∑ a : Fin 6, M (eR i) (e a) * conj' (M (eR j) (e a)))
        = ∑ c : Fin m, M (eR i) c * conj' (M (eR j) c) :=
          Equiv.sum_comp e (fun c => M (eR i) c * conj' (M (eR j) c))
      _ = if eR i = eR j then 1 else 0 := hrow
      _ = (1 : Matrix (Fin 6) (Fin 6) ℂ) i j := by
          rw [Matrix.one_apply]
          by_cases hij : i = j
          · rw [if_pos hij, if_pos (by rw [hij])]
          · rw [if_neg hij, if_neg (fun h => hij (eR.injective h))]
  exact homometricSix_unrealizable
    (Matrix.of fun i a => V (eR i) (eS a)) (Matrix.of fun i c => W (eR i) (eT c))
    (transport V eS hV) (transport W eT hW)
    (fun i a => hVnz _ _) (fun i c => hWnz _ _)
    (fun a b hab i j => hmatch a b hab i j)

/-- THE CONDITIONAL TWO-BRANCH THEOREM. Everything internal is kernel-proved; the classification
premise — translation-congruent, reflection-congruent, or the exceptional six-mode match — is
what the Piccard/Bekir–Golomb turnpike classification supplies. The exceptional alternative is
refuted by `homometricSix_unrealizable`, leaving exactly the two Hamiltonian branches. -/
theorem twoBranch_of_PiccardClassification (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hclass :
      (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, (∀ a, E' (τ a) = E a + E₀)
        ∧ ∀ a b : Fin m, a ≠ b → ∀ i j,
          (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
            = (V i a * conj' (V i b)) * conj' (V j a * conj' (V j b)))
      ∨ (∃ τ : Equiv.Perm (Fin m), ∃ E₀ : ℝ, (∀ a, E' (τ a) = -E a + E₀)
        ∧ ∀ a b : Fin m, a ≠ b → ∀ i j,
          (W i (τ a) * conj' (W i (τ b))) * conj' (W j (τ a) * conj' (W j (τ b)))
            = (V i b * conj' (V i a)) * conj' (V j b * conj' (V j a)))
      ∨ ExceptionalMatch V W) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) := by
  rcases hclass with ⟨τ, E₀, halign, hC⟩ | ⟨τ, E₀, halign, hC⟩ | hex
  · left
    obtain ⟨d, hd, hmain⟩ := reconstruction_translation hm V W τ E E' E₀ hV hVnz halign hC
    exact ⟨E₀, d, hd, hmain⟩
  · right
    obtain ⟨d, hd, hmain⟩ := reconstruction_reflection hm V W τ E E' E₀ hV hVnz halign hC
    exact ⟨E₀, d, hd, hmain⟩
  · exact (exceptional_impossible V W hV hW hVnz hWnz hex).elim

/-- **THE SPECTRAL TWO-BRANCH THEOREM.** The classification premise now speaks ONLY about
spectra: the target energies are a translate of the source energies, their negation-translate,
or (both spectra being six-mode) they realize the exceptional gap correspondence `mu`. Every
coefficient hypothesis of `twoBranch_of_PiccardClassification` is manufactured from equal
transition probabilities by `BohrFrequency.coefficient_line_extraction` — one spectral identity
per line, using only that both gap structures are Golomb (all gaps distinct). This is the
theorem in the form the Piccard/Bekir–Golomb turnpike classification can actually feed:
Piccard classifies gap correspondences; quantum coefficient equality is derived, not assumed. -/
theorem twoBranch_of_spectral_classification (hm : 3 ≤ m)
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
          E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS b) - E (eS a))) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) := by
  apply twoBranch_of_PiccardClassification hm V W E E' hV hW hVnz hWnz
  rcases hclass with ⟨τ, E₀, halign⟩ | ⟨τ, E₀, halign⟩ | ⟨eS, eT, hspec⟩
  · refine Or.inl ⟨τ, E₀, halign, fun a b hab i j => ?_⟩
    have hmatch : E' (τ b) - E' (τ a) = E b - E a := by
      rw [halign a, halign b]; ring
    have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
      (a := a) (b := b) (c := τ a) (d := τ b) hab
      (fun h => hab (τ.injective h)) hmatch i j
    simp only [Complex.star_def] at hline
    simp only [map_mul, Complex.conj_conj]
    linear_combination hline
  · refine Or.inr (Or.inl ⟨τ, E₀, halign, fun a b hab i j => ?_⟩)
    have hmatch : E' (τ b) - E' (τ a) = E a - E b := by
      rw [halign a, halign b]; ring
    have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
      (a := b) (b := a) (c := τ a) (d := τ b) (Ne.symm hab)
      (fun h => hab (τ.injective h)) hmatch i j
    simp only [Complex.star_def] at hline
    simp only [map_mul, Complex.conj_conj]
    linear_combination hline
  · refine Or.inr (Or.inr ⟨eS, eS, eT, fun a b hab i j => ?_⟩)
    have hmatch := hspec a b hab
    have hline := BohrFrequency.coefficient_line_extraction V W E E' hgapV hgapW hU
      (a := eS a) (b := eS b) (c := eT (mu a b).1) (d := eT (mu a b).2)
      (fun h => hab.ne (eS.injective h))
      (fun h => (mu_gap a b hab).1.ne (eT.injective h)) hmatch (eS i) (eS j)
    simp only [Complex.star_def] at hline
    simp only [map_mul, Complex.conj_conj]
    linear_combination hline

#print axioms modulus_rigid
#print axioms moduli_match
#print axioms phase_coboundary_of_moduli
#print axioms phase_coboundary
#print axioms reconstruction_translation_of_moduli
#print axioms reconstruction_translation
#print axioms reconstruction_reflection_of_moduli
#print axioms reconstruction_reflection
#print axioms reconstruction_dim_zero
#print axioms reconstruction_dim_one
#print axioms dim_two_moduli_dichotomy
#print axioms unitary2_line_dichotomy
#print axioms reconstruction_dim_two
#print axioms exceptional_impossible
#print axioms twoBranch_of_PiccardClassification
#print axioms twoBranch_of_spectral_classification

end CongruentReconstruction
end OIBridge
