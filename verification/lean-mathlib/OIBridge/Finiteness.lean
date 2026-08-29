/-
  OIBridge/Finiteness.lean — [Main] Lemma 1, as a conditional with its physical premise exposed.

      **Lemma 1** (Finiteness). The observer has finitely many distinguishable internal states, so
      the visible configuration space C_V is finite, with a discreteness scale ε providing a finite
      minimal cell volume. Any observer bounded by a finite-area surface can couple to only finitely
      many modes across that boundary; independent support comes from holographic entropy bounds.

  THIS IS THE ONE LEMMA WHOSE JUSTIFICATION IS PHYSICS, and the formalization is shaped around
  saying so rather than around hiding it. Lean is not asked to prove holography, and it is not asked
  to conjure `Finite C_V` out of a bare real number "finite area". What is proved is the
  IMPLICATION, with the physical input carried as a named, honest premise:

      FINITELY MANY BOUNDARY MODES, each with finitely many distinguishable settings, and the
      observer's internal state determined by those settings
          ⟹  C_V is finite, with an explicit cardinality bound.

  The premise is the instance arguments `[Finite Mode]` and `[∀ m, Finite (Setting m)]` together
  with the injection `read`. `[Finite Mode]` is exactly where the finite-area boundary and the
  holographic entropy bound enter, and NOTHING in this file argues for it. A reader who rejects the
  holographic input rejects that instance and keeps every theorem below intact and unusable, which
  is the correct behaviour for an imported premise.

  WHY THE PREMISE IS NOT A REAL NUMBER. Encoding "finite area" as some `A : ℝ` and deriving
  `Finite C_V` from it would need a bridge that does not exist in Lean and cannot: it is the
  physical content of the holographic bound. The premise is therefore stated at the level where it
  is actually a mathematical hypothesis — a finite index set of modes — and `modes_must_be_finite`
  proves that this is not a free choice of formulation: finitely many settings per mode, WITHOUT
  finitely many modes, does not give a finite configuration space.

  THE DISCRETENESS SCALE gets the same treatment. `card_cells_le` says a bounded region with a
  POSITIVE minimal cell volume carries finitely many cells, with the bound `V / ε`; and
  `cells_need_positive_floor` shows that bounded volume alone gives no bound at all, so the
  positivity of the discreteness scale is what is doing the work.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Pi
import Mathlib.SetTheory.Cardinal.Finite
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp

namespace OIBridge

namespace Finiteness

open Finset

set_option linter.unusedSectionVars false

/-! ### The boundary premise, and the finiteness it delivers

`Mode` is the set of modes the observer couples to across its boundary, `Setting m` the
distinguishable settings of mode `m`, and `read` says the observer's internal state is determined by
what crosses the boundary. `[Finite Mode]` is the imported physical premise. -/

/-- **Lemma 1's finiteness conclusion, from the boundary premise.** If the observer couples to
finitely many modes, each with finitely many distinguishable settings, and its internal state is
determined by those settings, then the visible configuration space is finite.

The premise is not argued for here — it is the finite-area/holographic input, imported. -/
theorem finite_of_boundary_modes {CV : Type*} {Mode : Type*} {Setting : Mode → Type*}
    [Finite Mode] [∀ m, Finite (Setting m)]
    (read : CV → ∀ m, Setting m) (hread : Function.Injective read) : Finite CV :=
  Finite.of_injective read hread

/-- The cardinality bound the same premise delivers: at most the product of the per-mode counts.
This is the quantitative form the holographic reading wants — the observer's state count is bounded
by what its boundary can carry. -/
theorem card_le_prod_boundary {CV : Type*} {Mode : Type*} {Setting : Mode → Type*}
    [Fintype Mode] [DecidableEq Mode] [∀ m, Fintype (Setting m)]
    (read : CV → ∀ m, Setting m) (hread : Function.Injective read) :
    Nat.card CV ≤ ∏ m, Fintype.card (Setting m) := by
  have h := Nat.card_le_card_of_injective read hread
  rwa [Nat.card_eq_fintype_card (α := ∀ m, Setting m), Fintype.card_pi] at h

/-- With a uniform bound `d` on the settings of each of `N` modes, the bound is `d ^ N` — the shape
the holographic entropy bound is usually quoted in. -/
theorem card_le_pow {CV : Type*} {Setting : Fin N → Type*} [∀ m, Fintype (Setting m)]
    (d : ℕ) (hd : ∀ m, Fintype.card (Setting m) ≤ d)
    (read : CV → ∀ m, Setting m) (hread : Function.Injective read) :
    Nat.card CV ≤ d ^ N := by
  refine (card_le_prod_boundary read hread).trans ?_
  calc ∏ m, Fintype.card (Setting m) ≤ ∏ _m : Fin N, d :=
        Finset.prod_le_prod' fun m _ => hd m
    _ = d ^ N := by simp

/-! ### The countercontrol: which half of the premise carries the conclusion

Finitely many settings per mode is not enough. It is the finiteness of the MODE SET — the
finite-area boundary — that delivers the conclusion, and this theorem is what stops the premise from
being weakened to the harmless half. -/

/-- **Finitely many settings per mode does not suffice.** There is an observer whose every boundary
mode has just two settings, whose internal state is faithfully read at the boundary, and whose
configuration space is nonetheless infinite — because the modes are infinite in number.

So `[Finite Mode]` in the theorems above is load-bearing, and it is precisely the clause the
finite-area surface and the holographic bound are invoked for. -/
theorem modes_must_be_finite :
    ∃ (CV : Type) (Mode : Type) (Setting : Mode → Type) (read : CV → ∀ m, Setting m),
      (∀ m, Finite (Setting m)) ∧ Function.Injective read ∧ Infinite CV := by
  classical
  refine ⟨ℕ → Bool, ℕ, fun _ => Bool, id, fun _ => inferInstance, Function.injective_id, ?_⟩
  exact Infinite.of_injective (fun n : ℕ => fun k : ℕ => decide (k = n)) (by
    intro a b hab
    have := congrFun hab a
    simpa using this.symm)

/-! ### The discreteness scale

"A finite minimal cell volume" is the second half of Lemma 1, and it is a counting statement: a
bounded region cannot hold more cells than its volume divided by the smallest one. -/

/-- **A positive minimal cell volume makes a bounded region carry finitely many cells**, at most
`V / ε` of them. This is the discreteness-scale clause of Lemma 1. -/
theorem card_cells_le {ι : Type*} (cells : Finset ι) (vol : ι → ℝ) (ε V : ℝ) (hε : 0 < ε)
    (hlb : ∀ i ∈ cells, ε ≤ vol i) (htot : ∑ i ∈ cells, vol i ≤ V) :
    (cells.card : ℝ) ≤ V / ε := by
  have hsum : (cells.card : ℝ) * ε ≤ ∑ i ∈ cells, vol i := by
    calc (cells.card : ℝ) * ε = ∑ _i ∈ cells, ε := by
          rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ ∑ i ∈ cells, vol i := Finset.sum_le_sum hlb
  rw [le_div_iff₀ hε]
  linarith [hsum, htot]

/-- **Without a positive floor there is no bound at all.** For every `N`, a region of volume `V`
admits `N` cells of positive volume. So the discreteness scale's POSITIVITY is what makes the cell
count finite; bounded volume on its own says nothing. -/
theorem cells_need_positive_floor (V : ℝ) (hV : 0 < V) (N : ℕ) (hN : 0 < N) :
    ∃ vol : Fin N → ℝ, (∀ i, 0 < vol i) ∧ ∑ i, vol i ≤ V := by
  have hNr : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hN
  refine ⟨fun _ => V / (N : ℝ), fun _ => div_pos hV hNr, ?_⟩
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  rw [mul_div_cancel₀ _ (ne_of_gt hNr)]

/-! ### The lemma

Both clauses in one conditional statement, with the imported premise in the hypotheses where a
reader can see and refuse it. -/

/-- **Lemma 1 (Finiteness), [Main] §1.2, as a conditional.**

Given the boundary premise — finitely many modes, finitely many settings each, and an observer whose
internal state is determined by them — the visible configuration space is finite with an explicit
cardinality bound; and given a positive discreteness scale, a bounded region carries at most `V / ε`
cells. The finite-area/holographic input is the `[Fintype Mode]` instance and the positivity of `ε`,
and neither is argued for here. -/
theorem finiteness {CV : Type*} {Mode : Type*} {Setting : Mode → Type*}
    [Fintype Mode] [DecidableEq Mode] [∀ m, Fintype (Setting m)]
    (read : CV → ∀ m, Setting m) (hread : Function.Injective read)
    {ι : Type*} (cells : Finset ι) (vol : ι → ℝ) (ε V : ℝ) (hε : 0 < ε)
    (hlb : ∀ i ∈ cells, ε ≤ vol i) (htot : ∑ i ∈ cells, vol i ≤ V) :
    Finite CV ∧ Nat.card CV ≤ ∏ m, Fintype.card (Setting m) ∧ (cells.card : ℝ) ≤ V / ε :=
  ⟨finite_of_boundary_modes read hread,
   card_le_prod_boundary read hread,
   card_cells_le cells vol ε V hε hlb htot⟩

/-! ### What these proofs rest on -/

#print axioms finite_of_boundary_modes
#print axioms card_le_prod_boundary
#print axioms card_le_pow
#print axioms modes_must_be_finite
#print axioms card_cells_le
#print axioms cells_need_positive_floor
#print axioms finiteness

end Finiteness

end OIBridge
