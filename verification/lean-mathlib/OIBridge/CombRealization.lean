/-
  OIBridge/CombRealization.lean — b446, the saturated-class lemma, kernel-checked.

  This file is the pilot for the verification standard the corpus is moving to: where a round
  produces a short structural theorem, LEAN PROVES THE REASON and Python keeps the exhaustive
  census. `comb_realization_probes.py` (CR3, CR4) enumerates every bijection at n = 8 and n = 9
  and confirms the lemma's forced steps hold in 100% of cases; what is proved here is the
  universal implication those enumerations sample. The two layers are independent and neither
  substitutes for the other: PROBED IS NOT FORMALLY PROVED, and a census over n <= 9 is evidence
  where this file is certification.

  THE STATEMENT, in the language of `papers/oi_lattice_code/foundations/comb_realization_probes.py`.
  A finite-state machine realizing a comb has a state set `S`, a readout `π : S → Bool`, and for
  each action a one-step map `g = φ ∘ I_a` which reversibility makes a bijection. A readout class
  is SATURATED when every one of its states carries positive prior weight. Two facts about the
  b76B comb at horizon 2, both read off a SINGLE REPEATED action sequence `(a,a)`:

    * outcome `(b, ¬b)` has probability zero in sector `b` — so for a supported state `s` with
      `π s = b`, if `π (g s) = b` then `π (g (g s)) = b`;
    * outcome `(b, b)` has probability 1/4 in the OTHER sector — so some supported `t` has
      `π t ≠ b`, `π (g t) = b` and `π (g (g t)) = b`.

  Those two together are contradictory when the class `{π = b}` is saturated. The proof is three
  lines of mathematics: the first fact propagates forward along the orbit of `t`, so every
  positive iterate of `t` lies in the class; but `g` is an injective self-map of a finite type, so
  the orbit of `t` returns to `t`, which does not lie in the class.

  NOTHING ABOUT THE COMB'S NUMBERS ENTERS THE PROOF. The hypotheses are the two support facts and
  nothing else, so the theorem holds for every bijective realization of any comb presenting them.
  FINITENESS IS ESSENTIAL AND NOT DECORATION: on `ℤ` with `g` the successor map and `π n = (1 ≤ n)`
  both hypotheses hold and there is no contradiction.

  WHAT IS ASSUMED AND WHAT IS PROVED. The hypotheses `closed` and the witness `t` are the comb's
  own support pattern, established numerically in the probe; everything after that is deduction.
  `Function.Injective g` is exactly reversibility of the one-step map — NOT readout preservation,
  NOT involutivity of the instruments, NOT that a common `φ` factors through both. That is why the
  b446 lower bound pins the whole 2×2 instrument lattice at once.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.Fintype.Pigeonhole
import Mathlib.Data.Finset.Card

namespace OIBridge

namespace CombRealization

variable {S : Type*}

/-- The forward orbit of `t` under `g`. Defined by structural recursion rather than through
`Function.iterate` so that the step equation holds by `rfl` and the induction below needs no
iterate lemmas at all. -/
def orbit (g : S → S) (t : S) : ℕ → S
  | 0 => t
  | n + 1 => g (orbit g t n)

@[simp] theorem orbit_zero (g : S → S) (t : S) : orbit g t 0 = t := rfl

@[simp] theorem orbit_succ (g : S → S) (t : S) (n : ℕ) :
    orbit g t (n + 1) = g (orbit g t n) := rfl

/-- Injectivity cancels a common tail of steps: two orbit points that agree after `n` further
steps already agreed. -/
theorem orbit_cancel {g : S → S} (hg : Function.Injective g) (t : S) :
    ∀ n i j : ℕ, orbit g t (i + n) = orbit g t (j + n) → orbit g t i = orbit g t j := by
  intro n
  induction n with
  | zero => intro i j h; simpa using h
  | succ k ih =>
      intro i j h
      -- `i + (k+1)` is definitionally `(i + k) + 1`, and `orbit` steps by `rfl`, so this is a
      -- retyping rather than a rewrite. `simp` here would unfold `orbit_succ` forever.
      have h' : g (orbit g t (i + k)) = g (orbit g t (j + k)) := h
      exact ih i j (hg h')

/-- An injective self-map of a finite type returns every point to itself: some POSITIVE number of
steps carries `t` back to `t`. This is the one place finiteness is used, and it is used exactly
once. -/
theorem exists_return [Finite S] {g : S → S} (hg : Function.Injective g) (t : S) :
    ∃ d : ℕ, 0 < d ∧ orbit g t d = t := by
  obtain ⟨i, j, hne, heq⟩ := Finite.exists_ne_map_eq_of_infinite (orbit g t)
  rcases Nat.lt_or_ge i j with hlt | hge
  · refine ⟨j - i, by omega, ?_⟩
    have h : orbit g t (0 + i) = orbit g t ((j - i) + i) := by
      simpa [Nat.sub_add_cancel (le_of_lt hlt)] using heq
    simpa using (orbit_cancel hg t i 0 (j - i) h).symm
  · have hlt : j < i := by omega
    refine ⟨i - j, by omega, ?_⟩
    have h : orbit g t (0 + j) = orbit g t ((i - j) + j) := by
      simpa [Nat.sub_add_cancel (le_of_lt hlt)] using heq.symm
    simpa using (orbit_cancel hg t j 0 (i - j) h).symm

/-- **The saturated-class lemma.**

If every state of the readout class `{π = b}` obeys the sector's own support constraint — reading
`b` one step out forces `b` two steps out — then no state OUTSIDE that class can read `b` at both
of its next two steps.

Read as a no-go: the comb requires such a state, so the class cannot be saturated.

The hypotheses name a single action; `g` is that action's one-step map and nothing here compares
two different actions. -/
theorem saturated_class_obstruction [Finite S] {g : S → S} (hg : Function.Injective g)
    (π : S → Bool) (b : Bool)
    (closed : ∀ s, π s = b → π (g s) = b → π (g (g s)) = b)
    (t : S) (ht : π t ≠ b) (h₁ : π (g t) = b) (h₂ : π (g (g t)) = b) :
    False := by
  -- Forward propagation: every POSITIVE iterate of `t` reads `b`.
  have key : ∀ n : ℕ, π (orbit g t (n + 1)) = b ∧ π (orbit g t (n + 2)) = b := by
    intro n
    induction n with
    | zero => exact ⟨h₁, h₂⟩
    | succ k ih => exact ⟨ih.2, closed _ ih.1 ih.2⟩
  -- Finiteness: the orbit returns, and it returns to a state that does NOT read `b`.
  obtain ⟨d, hd, hret⟩ := exists_return hg t
  obtain ⟨m, rfl⟩ : ∃ m : ℕ, d = m + 1 := ⟨d - 1, by omega⟩
  exact ht (hret ▸ (key m).1)

/- `hts` below is retained deliberately and the linter silenced rather than the hypothesis dropped.
The deduction never consumes it — the obstruction constrains the class `{π = b}`, and `t` lies
outside that class — but the comb's 1/4 outcome is realized by a SUPPORTED state, and a statement
that quietly allowed an unsupported witness would not be the fact the round proves. -/
set_option linter.unusedVariables false in
/-- **Workspace states are forced.** Under the same two support facts restricted to SUPPORTED
states, the readout class `{π = b}` must contain a state of prior weight zero.

This is the form the b446 round uses: a reversible realization of that comb cannot spend all of a
readout class on supported states. -/
theorem workspace_state_forced [Finite S] {g : S → S} (hg : Function.Injective g)
    (π : S → Bool) (b : Bool) (supp : S → Prop)
    (closed : ∀ s, supp s → π s = b → π (g s) = b → π (g (g s)) = b)
    (t : S) (hts : supp t) (ht : π t ≠ b) (h₁ : π (g t) = b) (h₂ : π (g (g t)) = b) :
    ∃ s, π s = b ∧ ¬ supp s := by
  by_contra hcon
  have hall : ∀ s, π s = b → supp s := by
    intro s hs
    by_contra hns
    exact hcon ⟨s, hs, hns⟩
  exact saturated_class_obstruction hg π b (fun s hs => closed s (hall s hs) hs) t ht h₁ h₂

/-- **A readout class carrying four supported states needs a fifth state.**

`A` is the supported part of the class — four states, because the comb's mixed action sequence
carries four equiprobable outcomes there. The forced workspace state is outside `A`, so the class
has at least five members. -/
theorem class_card_ge_five [Fintype S] [DecidableEq S] {g : S → S} (hg : Function.Injective g)
    (π : S → Bool) (b : Bool) (supp : S → Prop)
    (closed : ∀ s, supp s → π s = b → π (g s) = b → π (g (g s)) = b)
    (t : S) (hts : supp t) (ht : π t ≠ b) (h₁ : π (g t) = b) (h₂ : π (g (g t)) = b)
    (A : Finset S) (hA : 4 ≤ A.card) (hAcls : ∀ s ∈ A, π s = b) (hAsupp : ∀ s ∈ A, supp s) :
    5 ≤ (Finset.univ.filter fun s => π s = b).card := by
  obtain ⟨w, hw, hwns⟩ :=
    workspace_state_forced hg π b supp closed t hts ht h₁ h₂
  have hwA : w ∉ A := fun h => hwns (hAsupp w h)
  have hsub : insert w A ⊆ Finset.univ.filter fun s => π s = b := by
    intro x hx
    rcases Finset.mem_insert.mp hx with rfl | hx
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, hw⟩
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, hAcls x hx⟩
  have hcard : (insert w A).card = A.card + 1 := Finset.card_insert_of_notMem hwA
  have := Finset.card_le_card hsub
  omega

/-- **The b446 lower bound.** Both readout classes obey the sector constraint on supported states,
both carry four supported states, and each supplies the other's witness. Then the machine has at
least ten states.

The combined hypothesis `closed` says: for a supported state, reading its OWN value one step out
forces that value two steps out. That is exactly the pair of zero-probability outcomes `(0,1)` in
sector 0 and `(1,0)` in sector 1, both read off the repeated action sequence. The two witnesses
are the probability-1/4 outcomes `(1,1)` in sector 0 and `(0,0)` in sector 1. -/
theorem card_ge_ten [Fintype S] [DecidableEq S] {g : S → S} (hg : Function.Injective g)
    (π : S → Bool) (supp : S → Prop)
    (closed : ∀ s, supp s → π (g s) = π s → π (g (g s)) = π s)
    (t₀ : S) (ht₀s : supp t₀) (ht₀ : π t₀ = false)
    (h₀₁ : π (g t₀) = true) (h₀₂ : π (g (g t₀)) = true)
    (t₁ : S) (ht₁s : supp t₁) (ht₁ : π t₁ = true)
    (h₁₁ : π (g t₁) = false) (h₁₂ : π (g (g t₁)) = false)
    (A₀ : Finset S) (hA₀ : 4 ≤ A₀.card)
    (hA₀c : ∀ s ∈ A₀, π s = false) (hA₀s : ∀ s ∈ A₀, supp s)
    (A₁ : Finset S) (hA₁ : 4 ≤ A₁.card)
    (hA₁c : ∀ s ∈ A₁, π s = true) (hA₁s : ∀ s ∈ A₁, supp s) :
    10 ≤ Fintype.card S := by
  have closed' : ∀ (b : Bool) (s : S), supp s → π s = b → π (g s) = b → π (g (g s)) = b := by
    intro b s hs hsb hgb
    subst hsb
    exact closed s hs hgb
  -- the class `{π = false}` needs five states, witnessed by `t₁`
  have hfive₀ : 5 ≤ (Finset.univ.filter fun s => π s = false).card :=
    class_card_ge_five hg π false supp (closed' false) t₁ ht₁s (by simp [ht₁]) h₁₁ h₁₂
      A₀ hA₀ hA₀c hA₀s
  -- and the class `{π = true}` needs five, witnessed by `t₀`
  have hfive₁ : 5 ≤ (Finset.univ.filter fun s => π s = true).card :=
    class_card_ge_five hg π true supp (closed' true) t₀ ht₀s (by simp [ht₀]) h₀₁ h₀₂
      A₁ hA₁ hA₁c hA₁s
  -- and the two classes partition the state set
  have hsplit : (Finset.univ.filter fun s => π s = false).card
      + (Finset.univ.filter fun s => π s = true).card = Fintype.card S := by
    classical
    have hnot : (Finset.univ.filter fun s => ¬ (π s = false))
        = (Finset.univ.filter fun s => π s = true) := by
      apply Finset.filter_congr
      intro x _
      cases π x <;> simp
    rw [← hnot, Finset.card_filter_add_card_filter_not, Finset.card_univ]
  omega

/-! ### What these proofs rest on

Printed at build time so the kernel's own answer, not a claim in a comment, is what the log
carries. `sorryAx` appearing in any of these lines would mean a hole; only the three standard
axioms should be listed. -/

#print axioms saturated_class_obstruction
#print axioms workspace_state_forced
#print axioms class_card_ge_five
#print axioms card_ge_ten

end CombRealization

end OIBridge
