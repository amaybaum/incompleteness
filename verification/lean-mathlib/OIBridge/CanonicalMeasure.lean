/-
  OIBridge/CanonicalMeasure.lean — [Main] Lemma 3, the determinism/reversibility/selected-measure
  lemma, in the shape its own status remarks require.

      **Lemma 3** (Determinism, reversibility, and the selected measure). φ is a function with a
      unique successor for every state (determinism) and, as the reversible representative of §1.2,
      a bijection. On each accessible orbit the invariant measure is unique (uniform on the cycle);
      globally, the counting measure is selected among invariant measures as the maximal-entropy
      one — A SELECTION PRINCIPLE, NOT UNIQUENESS FROM INVARIANCE ALONE.

  WHAT IS ASSUMED AND WHAT IS PROVED — the whole difficulty of this lemma, because it deliberately
  combines clauses of different epistemic status.

  * REVERSIBILITY IS NOT DERIVED HERE, and must not be. The manuscript's own status remark calls
    the bijective substratum "a representation choice — the minimal recurrent bijective
    representative of the hidden dynamics", recovered by a two-pronged argument one prong of which
    is EMPIRICAL (the observed unitarity of quantum dynamics). A Lean derivation of it from first
    principles would be proving something the manuscript explicitly declines to claim. So `φ` here
    is a `Equiv.Perm S`, taken as given, exactly as the manuscript takes it.
  * WHAT IS PROVED FROM FINITENESS is the structural half of the same remark: on a finite set,
    injectivity implies surjectivity (`injective_imp_bijective`). That is the second prong's
    mathematical content and it is a theorem.
  * DETERMINISM — "a unique successor for every state" — is what it means for `φ` to be a function
    at all, and carries no separate obligation.

  THE SELECTION, IN FOUR CLAUSES. `orbit_invariant_unique` (an invariant law supported on an orbit
  is the uniform law on it), `counting_invariant` (the counting measure is invariant under every
  permutation), `counting_maximal_entropy` (it maximizes entropy among invariant laws), and
  `invariance_does_not_select` — the guard. That last one is a THEOREM, not a comment: two disjoint
  nonempty invariant sets carry two distinct invariant probability laws, so invariance alone never
  selects. A later refactor cannot quietly turn the selection principle back into a uniqueness
  claim without this theorem contradicting it.

  THE LEMMA'S FORMAL OBLIGATION IS ENTIRELY FINITE, and the manuscript now says so in its own
  typography. The continuum analogue — Liouville measure is invariant but not in general the unique
  absolutely continuous invariant measure — is an illustration in a setting the framework's finite
  scope does not use, and it is carried in its own remark following the lemma rather than inside
  the italicized statement. It is deliberately not formalized. Its role is discharged here by
  `invariance_does_not_select`, which proves non-uniqueness where the framework actually lives, on
  the finite state space, and is therefore the load-bearing statement rather than the analogy.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FiniteEntropy

namespace OIBridge

namespace CanonicalMeasure

open Finset Real OIBridge.FiniteEntropy

set_option linter.unusedSectionVars false

variable {S : Type*} [Fintype S] [DecidableEq S]

/-! ### Determinism and reversibility

The bijection is taken as given, per the manuscript's status remark. What finiteness contributes is
the structural prong: an injective self-map of a finite type is already a bijection. -/

/-- **On a finite set, injectivity implies surjectivity.** The structural prong of Lemma 3's
two-pronged argument; the other prong is empirical and has no Lean content. -/
theorem injective_imp_bijective (f : S → S) (hf : Function.Injective f) : Function.Bijective f :=
  Finite.injective_iff_bijective.1 hf

/-! ### Invariant probability laws -/

/-- A probability law on the finite state space. -/
def IsProb (p : S → ℝ) : Prop := (∀ s, 0 ≤ p s) ∧ ∑ s, p s = 1

/-- Invariance, in the measure-theoretic form: the pushforward of `p` along `φ` is `p` again. It is
stated this way rather than as `p ∘ φ = p` so that the definition does not presuppose the
bijection; `invariant_iff` shows the two agree once `φ` is one. -/
def Invariant (φ : Equiv.Perm S) (p : S → ℝ) : Prop := marg p φ = p

theorem marg_perm (φ : Equiv.Perm S) (p : S → ℝ) (t : S) : marg p φ t = p (φ.symm t) := by
  classical
  have hfil : (univ.filter fun s => φ s = t) = {φ.symm t} := by
    ext s
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    exact ⟨fun h => by rw [← h, Equiv.symm_apply_apply], fun h => by rw [h, Equiv.apply_symm_apply]⟩
  rw [marg, hfil, Finset.sum_singleton]

/-- For a bijection, invariance is the pointwise identity the manuscript uses. -/
theorem invariant_iff (φ : Equiv.Perm S) (p : S → ℝ) : Invariant φ p ↔ ∀ s, p (φ s) = p s := by
  constructor
  · intro h s
    have hs := congrFun h (φ s)
    rw [marg_perm, Equiv.symm_apply_apply] at hs
    exact hs.symm
  · intro h
    funext t
    rw [marg_perm, ← h (φ.symm t), Equiv.apply_symm_apply]

/-- An invariant law is constant along every trajectory. -/
theorem invariant_pow (φ : Equiv.Perm S) (p : S → ℝ) (h : Invariant φ p) (n : ℕ) (s : S) :
    p ((φ ^ n) s) = p s := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [pow_succ', Equiv.Perm.mul_apply, (invariant_iff φ p).1 h, ih]

/-! ### The uniform law on a set, and the orbits -/

/-- The uniform (counting) law on a finite set of states. -/
noncomputable def unif (A : Finset S) : S → ℝ := fun s => if s ∈ A then ((A.card : ℝ))⁻¹ else 0

theorem unif_nonneg (A : Finset S) (s : S) : 0 ≤ unif A s := by
  unfold unif; split <;> positivity

theorem sum_unif (A : Finset S) (hA : A.Nonempty) : ∑ s, unif A s = 1 := by
  classical
  have hcard : (0 : ℝ) < (A.card : ℝ) := by exact_mod_cast Finset.card_pos.2 hA
  have h1 : ∑ s, unif A s = ∑ _s ∈ A, ((A.card : ℝ))⁻¹ := by
    simp [unif, Finset.sum_ite_mem, Finset.univ_inter]
  rw [h1, Finset.sum_const, nsmul_eq_mul]
  field_simp

theorem unif_isProb (A : Finset S) (hA : A.Nonempty) : IsProb (unif A) :=
  ⟨unif_nonneg A, sum_unif A hA⟩

/-- A `φ`-invariant set is mapped ONTO itself, not merely into itself — finiteness again. -/
theorem image_eq_of_mapsTo (φ : Equiv.Perm S) {A : Finset S} (hA : ∀ x ∈ A, φ x ∈ A) :
    A.image φ = A := by
  classical
  refine Finset.eq_of_subset_of_card_le (fun t ht => ?_) ?_
  · obtain ⟨x, hx, rfl⟩ := Finset.mem_image.1 ht
    exact hA x hx
  · rw [Finset.card_image_of_injective _ φ.injective]

theorem mem_iff_symm_mem (φ : Equiv.Perm S) {A : Finset S} (hA : ∀ x ∈ A, φ x ∈ A) (t : S) :
    φ.symm t ∈ A ↔ t ∈ A := by
  classical
  constructor
  · intro h
    have := hA _ h
    rwa [Equiv.apply_symm_apply] at this
  · intro h
    rw [← image_eq_of_mapsTo φ hA] at h
    obtain ⟨x, hx, hxt⟩ := Finset.mem_image.1 h
    rwa [← hxt, Equiv.symm_apply_apply]

/-- The uniform law on any invariant set is invariant. -/
theorem unif_invariant (φ : Equiv.Perm S) {A : Finset S} (hA : ∀ x ∈ A, φ x ∈ A) :
    Invariant φ (unif A) := by
  funext t
  rw [marg_perm, unif, unif]
  by_cases h : t ∈ A
  · rw [if_pos h, if_pos ((mem_iff_symm_mem φ hA t).2 h)]
  · rw [if_neg h, if_neg fun hc => h ((mem_iff_symm_mem φ hA t).1 hc)]

/-- The orbit of `s`: every state the trajectory through `s` reaches. -/
noncomputable def orbit (φ : Equiv.Perm S) (s : S) : Finset S := by
  classical exact {t | ∃ n : ℕ, (φ ^ n) s = t}.toFinset

theorem mem_orbit (φ : Equiv.Perm S) (s t : S) : t ∈ orbit φ s ↔ ∃ n : ℕ, (φ ^ n) s = t := by
  classical
  simp [orbit]

theorem self_mem_orbit (φ : Equiv.Perm S) (s : S) : s ∈ orbit φ s :=
  (mem_orbit φ s s).2 ⟨0, by simp⟩

theorem orbit_nonempty (φ : Equiv.Perm S) (s : S) : (orbit φ s).Nonempty :=
  ⟨s, self_mem_orbit φ s⟩

theorem orbit_mapsTo (φ : Equiv.Perm S) (s : S) : ∀ t ∈ orbit φ s, φ t ∈ orbit φ s := by
  intro t ht
  obtain ⟨n, hn⟩ := (mem_orbit φ s t).1 ht
  exact (mem_orbit φ s _).2 ⟨n + 1, by rw [pow_succ', Equiv.Perm.mul_apply, hn]⟩

/-! ### Clause: on each accessible orbit the invariant measure is unique, and uniform -/

/-- **On each accessible orbit the invariant measure is unique — uniform on the cycle.**

An invariant law is constant along trajectories, so it is constant on the orbit; a constant law on
a finite set summing to one is the uniform one. Nothing here is a choice: within one orbit the
measure IS determined. -/
theorem orbit_invariant_unique (φ : Equiv.Perm S) (s : S) (p : S → ℝ)
    (hinv : Invariant φ p) (hprob : IsProb p)
    (hsupp : ∀ t, t ∉ orbit φ s → p t = 0) :
    p = unif (orbit φ s) := by
  classical
  have hconst : ∀ t ∈ orbit φ s, p t = p s := by
    intro t ht
    obtain ⟨n, rfl⟩ := (mem_orbit φ s t).1 ht
    exact invariant_pow φ p hinv n s
  have hsum : ∑ t ∈ orbit φ s, p t = 1 := by
    rw [← hprob.2]
    exact Finset.sum_subset (Finset.subset_univ _) fun t _ ht => hsupp t ht
  have hcard : ((orbit φ s).card : ℝ) * p s = 1 := by
    rw [← hsum, Finset.sum_congr rfl hconst, Finset.sum_const, nsmul_eq_mul]
  have hcpos : (0 : ℝ) < ((orbit φ s).card : ℝ) := by
    exact_mod_cast Finset.card_pos.2 (orbit_nonempty φ s)
  have hps : p s = ((orbit φ s).card : ℝ)⁻¹ := by
    field_simp at hcard ⊢
    linarith [hcard]
  funext t
  by_cases ht : t ∈ orbit φ s
  · rw [hconst t ht, hps, unif, if_pos ht]
  · rw [hsupp t ht, unif, if_neg ht]

/-! ### Clause: the counting measure is invariant and maximizes entropy -/

/-- **The counting measure is invariant** under every permutation of the state space. -/
theorem counting_invariant (φ : Equiv.Perm S) : Invariant φ (unif (univ : Finset S)) :=
  unif_invariant φ fun _ _ => Finset.mem_univ _

theorem counting_isProb [Nonempty S] : IsProb (unif (univ : Finset S)) :=
  unif_isProb _ Finset.univ_nonempty

theorem entropy_counting [Nonempty S] :
    entropy (unif (univ : Finset S)) = Real.log (Fintype.card S) := by
  have hcard : (0 : ℝ) < (Fintype.card S : ℝ) := by
    exact_mod_cast Fintype.card_pos_iff.2 ‹Nonempty S›
  have hval : ∀ s : S, unif (univ : Finset S) s = ((Fintype.card S : ℝ))⁻¹ := by
    intro s; simp [unif, Finset.card_univ]
  simp only [entropy, hval, Real.negMulLog, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  rw [Real.log_inv]
  field_simp

/-- **The counting measure maximizes entropy among invariant laws.**

Recorded rather than glossed: the bound does not USE invariance — `entropy_le_log_card` holds for
every probability law — so the counting measure is the maximum over a strictly larger set than the
manuscript's clause claims. Stating the clause in the manuscript's form keeps the correspondence
exact; the strengthening is noted here and nowhere relied upon. -/
theorem counting_maximal_entropy [Nonempty S] (φ : Equiv.Perm S) (p : S → ℝ)
    (hprob : IsProb p) (_hinv : Invariant φ p) :
    entropy p ≤ entropy (unif (univ : Finset S)) := by
  rw [entropy_counting]
  exact entropy_le_log_card p hprob.1 hprob.2

/-! ### The guard: invariance alone does not select

The manuscript is explicit that this is a SELECTION principle. Here is the theorem that keeps it
one — and it is the finite counterpart of the manuscript's continuum parenthetical, proved where
the framework actually lives. -/

/-- **Invariance alone does not select a measure.** Two disjoint nonempty invariant sets carry two
distinct invariant probability laws. Any permutation with at least two cycles has them, so
uniqueness from invariance is false in the finite setting too — not only in the continuum. -/
theorem invariance_does_not_select (φ : Equiv.Perm S) {A B : Finset S}
    (hA : A.Nonempty) (hB : B.Nonempty) (hAm : ∀ x ∈ A, φ x ∈ A) (hBm : ∀ x ∈ B, φ x ∈ B)
    (hdisj : Disjoint A B) :
    ∃ p q : S → ℝ, Invariant φ p ∧ Invariant φ q ∧ IsProb p ∧ IsProb q ∧ p ≠ q := by
  classical
  refine ⟨unif A, unif B, unif_invariant φ hAm, unif_invariant φ hBm,
    unif_isProb A hA, unif_isProb B hB, ?_⟩
  obtain ⟨a, ha⟩ := hA
  have hbA : a ∉ B := Finset.disjoint_left.1 hdisj ha
  intro hEq
  have h1 : unif A a = ((A.card : ℝ))⁻¹ := by rw [unif, if_pos ha]
  have h2 : unif B a = 0 := by rw [unif, if_neg hbA]
  have hcard : (0 : ℝ) < (A.card : ℝ) := by exact_mod_cast Finset.card_pos.2 ⟨a, ha⟩
  rw [hEq, h2] at h1
  exact absurd h1.symm (by positivity)

/-- A permutation with two cycles exists, so `invariance_does_not_select` is not vacuous: the
double transposition on four states carries the uniform law on each of its two cycles. -/
theorem two_cycle_witness :
    ∃ (φ : Equiv.Perm (Fin 4)) (A B : Finset (Fin 4)), A.Nonempty ∧ B.Nonempty ∧
      (∀ x ∈ A, φ x ∈ A) ∧ (∀ x ∈ B, φ x ∈ B) ∧ Disjoint A B ∧ φ ≠ 1 := by
  refine ⟨Equiv.swap 0 1 * Equiv.swap 2 3, {0, 1}, {2, 3}, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> decide

/-! ### The lemma

The clauses in one statement, in the manuscript's order and with its scope. -/

/-- **Lemma 3 (determinism, reversibility, and the selected measure), [Main] §1.2.**

Given the reversible representative — a permutation of the finite state space, taken as given
because the manuscript takes it as given — the invariant law on each accessible orbit is unique
and uniform; the counting measure is invariant; it maximizes entropy among invariant laws; and
invariance ALONE does not select, so the third clause is a selection principle and not a
uniqueness claim. -/
theorem determinism_reversibility_selected_measure [Nonempty S] (φ : Equiv.Perm S) :
    (∀ s : S, ∀ p : S → ℝ, Invariant φ p → IsProb p → (∀ t, t ∉ orbit φ s → p t = 0) →
        p = unif (orbit φ s)) ∧
      Invariant φ (unif (univ : Finset S)) ∧
      (∀ p : S → ℝ, IsProb p → Invariant φ p →
        entropy p ≤ entropy (unif (univ : Finset S))) ∧
      (∀ A B : Finset S, A.Nonempty → B.Nonempty → (∀ x ∈ A, φ x ∈ A) → (∀ x ∈ B, φ x ∈ B) →
        Disjoint A B →
        ∃ p q : S → ℝ, Invariant φ p ∧ Invariant φ q ∧ IsProb p ∧ IsProb q ∧ p ≠ q) :=
  ⟨fun s p hinv hprob hsupp => orbit_invariant_unique φ s p hinv hprob hsupp,
   counting_invariant φ,
   fun p hprob hinv => counting_maximal_entropy φ p hprob hinv,
   fun _ _ hA hB hAm hBm hd => invariance_does_not_select φ hA hB hAm hBm hd⟩

/-! ### What these proofs rest on -/

#print axioms injective_imp_bijective
#print axioms invariant_iff
#print axioms orbit_invariant_unique
#print axioms counting_invariant
#print axioms entropy_counting
#print axioms counting_maximal_entropy
#print axioms invariance_does_not_select
#print axioms two_cycle_witness
#print axioms determinism_reversibility_selected_measure

end CanonicalMeasure

end OIBridge
