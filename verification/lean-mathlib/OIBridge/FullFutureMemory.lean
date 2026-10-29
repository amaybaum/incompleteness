/-
# The entire visible future as an exact finite-image random variable

The codomain below is the image of the actual infinite sequence map on the finite
state space, not a fixed finite prefix or a freely chosen predictive surrogate.
Conditional information uses ordinary discrete Shannon entropy on this finite
image. No infinite-product measure or limit theorem is invoked or certified.
-/
import OIBridge.TrajectoryMemory
import Mathlib.Data.Fintype.OfMap

namespace OIBridge.FullFutureMemory
open OIBridge.FiniteEntropy OIBridge.HiddenMemory

variable {V H : Type*} [Fintype V] [Fintype H]
variable [DecidableEq V] [DecidableEq H]

/-- The complete visible sequence strictly after the state supplied as input. -/
def trace (step : V × H ≃ V × H) (q : V × H) : ℕ → V :=
  fun j => (step^[j + 1] q).1

/-- Actual whole-future sequences, with equal sequences identified exactly. -/
def FutureTrace (step : V × H ≃ V × H) := Set.range (trace step)

def encodeFuture (step : V × H ≃ V × H) (q : V × H) : FutureTrace step :=
  ⟨trace step q, q, rfl⟩

theorem encodeFuture_surjective (step : V × H ≃ V × H) :
    Function.Surjective (encodeFuture step) := by
  rintro ⟨f, ⟨q, rfl⟩⟩
  exact ⟨q, rfl⟩

/-- Finiteness comes from the finite source, despite the sequence-valued ambient type. -/
instance finiteFutureTrace (step : V × H ≃ V × H) : Finite (FutureTrace step) := by
  classical
  letI : Fintype (FutureTrace step) :=
    Fintype.ofSurjective (encodeFuture step) (encodeFuture_surjective step)
  infer_instance

noncomputable def futureTraceFintype (step : V × H ≃ V × H) :
    Fintype (FutureTrace step) := Fintype.ofFinite _

noncomputable def futureTraceDecidableEq (step : V × H ≃ V × H) :
    DecidableEq (FutureTrace step) := Classical.decEq _

attribute [local instance] futureTraceFintype futureTraceDecidableEq

/-- The code identifies exactly equal entire futures; it retains every future coordinate. -/
theorem encodeFuture_eq_iff (step : V × H ≃ V × H) (q q' : V × H) :
    encodeFuture step q = encodeFuture step q' ↔
      ∀ j : ℕ, (step^[j + 1] q).1 = (step^[j + 1] q').1 := by
  constructor
  · intro h j
    exact congrArg (fun f : FutureTrace step => f.val j) h
  · intro h
    apply Subtype.ext
    funext j
    exact h j

def futureRV (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : FutureTrace step :=
  encodeFuture step (step^[t] q)

/-- Decoding any coordinate gives the original orbit's actual future observation. -/
theorem futureRV_apply (step : V × H ≃ V × H) (t j : ℕ) (q : V × H) :
    (futureRV step t q).val j = TrajectoryMemory.now step (t + (j + 1)) q := by
  change (step^[j + 1] (step^[t] q)).1 = (step^[t + (j + 1)] q).1
  rw [Nat.add_comm t (j + 1)]
  exact congrArg Prod.fst
    (Function.iterate_add_apply (step : V × H → V × H) (j + 1) t q).symm

theorem finite_block_is_truncation (step : V × H ≃ V × H) (t L : ℕ) (q : V × H) :
    (fun j : Fin L => (futureRV step t q).val j.val) =
      TrajectoryMemory.future step t L q := rfl

/-- The actual whole future obeys the same hidden-information bound, with no horizon parameter. -/
theorem full_future_via_hidden [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) (t : ℕ) :
    cmiBits μ.p (TrajectoryMemory.past step t) (TrajectoryMemory.now step t)
        (futureRV step t) ≤
      cmiBits μ.p (TrajectoryMemory.past step t) (TrajectoryMemory.now step t)
        (TrajectoryMemory.hidden step t) ∧
    cmiBits μ.p (TrajectoryMemory.past step t) (TrajectoryMemory.now step t)
        (TrajectoryMemory.hidden step t) ≤ Real.logb 2 (Fintype.card H) := by
  have h := capacity_floor_of_fun (TrajectoryMemory.realization step μ t) (encodeFuture step)
  change cmiBits (marg μ.p (TrajectoryMemory.slice step t)) varHist varNow
      (fun s => encodeFuture step (varNow s, varHid s)) ≤
      cmiBits (marg μ.p (TrajectoryMemory.slice step t)) varHist varNow varHid ∧
    cmiBits (marg μ.p (TrajectoryMemory.slice step t)) varHist varNow varHid ≤ _ at h
  simp only [TrajectoryMemory.cmiBits_marg] at h
  exact h

theorem full_future_c3 [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) (t : ℕ) :
    cmiBits μ.p (TrajectoryMemory.past step t) (TrajectoryMemory.now step t)
      (futureRV step t) ≤ Real.logb 2 (Fintype.card H) :=
  (full_future_via_hidden step μ t).1.trans (full_future_via_hidden step μ t).2

/-- Genuine supremum over all natural times of the whole-trace conditional information. -/
noncomputable def fullFutureIstar (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) : ℝ :=
  sSup (Set.range fun t : ℕ =>
    cmiBits μ.p (TrajectoryMemory.past step t) (TrajectoryMemory.now step t) (futureRV step t))

theorem fullFutureIstar_le [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) : fullFutureIstar step μ ≤
      Real.logb 2 (Fintype.card H) := by
  apply csSup_le
  · exact ⟨_, ⟨0, rfl⟩⟩
  · rintro _ ⟨t, rfl⟩
    exact full_future_c3 step μ t

theorem full_future_capacity [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) :
    (2 : ℝ) ^ fullFutureIstar step μ ≤ (Fintype.card H : ℝ) := by
  have hc : (0 : ℝ) < (Fintype.card H : ℝ) := by
    exact_mod_cast Fintype.card_pos_iff.2 ‹Nonempty H›
  have hpow : (2 : ℝ) ^ fullFutureIstar step μ ≤
      (2 : ℝ) ^ Real.logb 2 (Fintype.card H) :=
    (Real.rpow_le_rpow_left_iff (by norm_num : (1 : ℝ) < 2)).2
      (fullFutureIstar_le step μ)
  rwa [Real.rpow_logb (by norm_num) (by norm_num) hc] at hpow

#print axioms encodeFuture_surjective
#print axioms encodeFuture_eq_iff
#print axioms futureRV_apply
#print axioms finite_block_is_truncation
#print axioms full_future_via_hidden
#print axioms full_future_c3
#print axioms fullFutureIstar_le
#print axioms full_future_capacity
end OIBridge.FullFutureMemory
