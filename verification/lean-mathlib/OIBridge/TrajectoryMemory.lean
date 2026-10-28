/-
# Actual trajectory laws for hidden predictive memory

Research candidate: initial laws are pushed through the actual iterates of one
finite permutation. No independent history/present/hidden joint law is assumed.
The inherited entropy inequalities and the genuine supremum over natural time /
horizon pairs are separate from physical readout or memory-retention mechanisms.
-/
import OIBridge.C3Necessity

namespace OIBridge.TrajectoryMemory
open Finset OIBridge.FiniteEntropy OIBridge.HiddenMemory

variable {V H : Type*} [Fintype V] [Fintype H]
variable [DecidableEq V] [DecidableEq H]

/-- Actual observed prefix, present and hidden state from one initial sample. -/
def past (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : Fin t → V :=
  fun j => (step^[j.val] q).1

def now (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : V :=
  (step^[t] q).1

def hidden (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : H :=
  (step^[t] q).2

def next (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : V :=
  (step (step^[t] q)).1

def future (step : V × H ≃ V × H) (t L : ℕ) (q : V × H) : Fin L → V :=
  fun j => (step^[j.val + 1] (step^[t] q)).1

def slice (step : V × H ≃ V × H) (t : ℕ) (q : V × H) : (Fin t → V) × V × H :=
  (past step t q, step^[t] q)

/-- The joint law is constructed from the initial law, not supplied independently. -/
noncomputable def realization (step : V × H ≃ V × H) (μ : FiniteEntropy.Dist (V × H)) (t : ℕ) :
    Realization (Fin t → V) V H where
  step := step
  w := marg μ.p (slice step t)
  nonneg := marg_nonneg μ.nonneg _
  total := by rw [sum_marg]; exact μ.total

/-- Conditional mutual information commutes with pushforward of its sample law. -/
theorem cmi_marg {σ τ A B C : Type*}
    [Fintype σ] [Fintype τ] [Fintype A] [Fintype B] [Fintype C]
    [DecidableEq σ] [DecidableEq τ] [DecidableEq A] [DecidableEq B] [DecidableEq C]
    (w : σ → ℝ) (e : σ → τ) (a : τ → A) (b : τ → B) (c : τ → C) :
    cmi (marg w e) a b c = cmi w (a ∘ e) (b ∘ e) (c ∘ e) := by
  simp only [cmi, marg_marg]
  rfl

theorem cmiBits_marg {σ τ A B C : Type*}
    [Fintype σ] [Fintype τ] [Fintype A] [Fintype B] [Fintype C]
    [DecidableEq σ] [DecidableEq τ] [DecidableEq A] [DecidableEq B] [DecidableEq C]
    (w : σ → ℝ) (e : σ → τ) (a : τ → A) (b : τ → B) (c : τ → C) :
    cmiBits (marg w e) a b c = cmiBits w (a ∘ e) (b ∘ e) (c ∘ e) := by
  simp only [cmiBits, cmi_marg]

/-- The constructed realization reproduces the actual next-step joint law. -/
theorem next_joint_law (step : V × H ≃ V × H) (μ : FiniteEntropy.Dist (V × H)) (t : ℕ) :
    marg (realization step μ t).w
      (fun s => (varHist s, varNow s, varNext (realization step μ t) s)) =
    marg μ.p (fun q => (past step t q, now step t q, next step t q)) := by
  change marg (marg μ.p (slice step t)) _ = _
  rw [marg_marg]
  rfl

/-- The constructed realization reproduces the actual future-block joint law. -/
theorem future_joint_law (step : V × H ≃ V × H) (μ : FiniteEntropy.Dist (V × H)) (t L : ℕ) :
    marg (realization step μ t).w
      (fun s => (varHist s, varNow s, C3.varFuture (realization step μ t) L s)) =
    marg μ.p (fun q => (past step t q, now step t q, future step t L q)) := by
  change marg (marg μ.p (slice step t)) _ = _
  rw [marg_marg]
  rfl

/-- The time-indexing of the future block agrees with the original orbit. -/
theorem future_at (step : V × H ≃ V × H) (t L : ℕ) (q : V × H) (j : Fin L) :
    future step t L q j = now step (t + (j.val + 1)) q := by
  unfold future now
  rw [Nat.add_comm t (j.val + 1)]
  exact congrArg Prod.fst
    (Function.iterate_add_apply (step : V × H → V × H) (j.val + 1) t q).symm

/-- Time-trajectory interpretation of the one-step hidden-memory inequality. -/
theorem trajectory_memory [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) (t : ℕ) :
    cmiBits μ.p (past step t) (now step t) (next step t) ≤
      cmiBits μ.p (past step t) (now step t) (hidden step t) ∧
    cmiBits μ.p (past step t) (now step t) (hidden step t) ≤
      Real.logb 2 (Fintype.card H) := by
  have h := capacity_floor (realization step μ t)
  change cmiBits (marg μ.p (slice step t)) varHist varNow
      (varNext (realization step μ t)) ≤
      cmiBits (marg μ.p (slice step t)) varHist varNow varHid ∧
    cmiBits (marg μ.p (slice step t)) varHist varNow varHid ≤ _ at h
  simp only [cmiBits_marg] at h
  exact h

/-- Time-trajectory interpretation of C3 at every finite future horizon. -/
theorem trajectory_c3 [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) (t L : ℕ) :
    cmiBits μ.p (past step t) (now step t) (future step t L) ≤
      Real.logb 2 (Fintype.card H) := by
  have h := C3.c3_necessity (realization step μ t) L
  change cmiBits (marg μ.p (slice step t)) varHist varNow
      (C3.varFuture (realization step μ t) L) ≤ _ at h
  rw [cmiBits_marg] at h
  exact h

/-- Genuine supremum over all natural times and finite future horizons. -/
noncomputable def trajectoryIstar (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) : ℝ :=
  sSup (Set.range fun i : ℕ × ℕ =>
    cmiBits μ.p (past step i.1) (now step i.1) (future step i.1 i.2))

theorem trajectoryIstar_le [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) : trajectoryIstar step μ ≤ Real.logb 2 (Fintype.card H) := by
  apply csSup_le
  · exact ⟨_, ⟨(0, 0), rfl⟩⟩
  · rintro _ ⟨⟨t, L⟩, rfl⟩
    exact trajectory_c3 step μ t L

/-- The per-process hidden-alphabet bound for that actual trajectory supremum. -/
theorem trajectory_capacity [Nonempty H] (step : V × H ≃ V × H)
    (μ : FiniteEntropy.Dist (V × H)) :
    (2 : ℝ) ^ trajectoryIstar step μ ≤ (Fintype.card H : ℝ) := by
  have hc : (0 : ℝ) < (Fintype.card H : ℝ) := by
    exact_mod_cast Fintype.card_pos_iff.2 ‹Nonempty H›
  have hpow : (2 : ℝ) ^ trajectoryIstar step μ ≤
      (2 : ℝ) ^ Real.logb 2 (Fintype.card H) :=
    (Real.rpow_le_rpow_left_iff (by norm_num : (1 : ℝ) < 2)).2
      (trajectoryIstar_le step μ)
  rwa [Real.rpow_logb (by norm_num) (by norm_num) hc] at hpow

#print axioms next_joint_law
#print axioms future_joint_law
#print axioms future_at
#print axioms trajectory_memory
#print axioms trajectory_c3
#print axioms trajectoryIstar_le
#print axioms trajectory_capacity
end OIBridge.TrajectoryMemory
