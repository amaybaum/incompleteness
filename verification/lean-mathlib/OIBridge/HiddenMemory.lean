/-
  OIBridge/HiddenMemory.lean — [Main]'s unavoidable-hidden-predictive-memory theorem.

  b448 rank 1 of the coverage backlog, and the sharpest statement in [Main] §3.4: it is UNIVERSAL
  over realizations, where the equivalence chain is existential. The equivalence says some finite
  reversible realization exists, which Markov processes satisfy too; this says that EVERY faithful
  deterministic completion of a process that remembers its past must carry that memory in the
  hidden sector. The two are deliberately separate results and neither is a lemma of the other.

  THE THEOREM, all three clauses, as the manuscript states them:

      Let S be a visible process and R ANY faithful deterministic realization of it — a bijection
      φ on C_V × C_H with a hidden prior reproducing S. Write f_x(h) = π_V(φ(x,h)), and for a
      visible history p ending in x write μ_p for the hidden posterior. Then

      (a) PUSHFORWARD IDENTITY.    P(X_{t+1} | p, x) = (f_x)_# μ_p exactly.
      (b) DISTINGUISHABILITY FLOOR. ‖P(·|p,x) - P(·|p',x)‖_TV ≤ ‖μ_p - μ_{p'}‖_TV.
      (c) CAPACITY FLOOR.           M_t := I(X_<t; X_{t+1} | X_t) ≤ I(X_<t; H_t | X_t)
                                                                 ≤ log₂ |C_H|.

  ALL THREE ARE PROVED. Clause (c) is the reason `OIBridge/FiniteEntropy.lean` exists: Mathlib
  carries no Shannon entropy, no mutual information and no data-processing inequality, and proving
  only `M_t ≤ log₂|C_H|` — the easy half of the easy inequality — would be a different theorem
  wearing this one's name.

  WHAT IS AN ASSUMPTION AND WHAT IS PROVED. The realization is the assumption: a bijection, and a
  law for (X_<t, X_t, H_t) that it induces. Everything after that is deduction. In particular the
  next visible value is not posited to be a function of (X_t, H_t) — it is DEFINED as the visible
  component of φ, which is what makes the Markov chain X_<t → H_t → X_{t+1} given X_t hold rather
  than be assumed, and that chain is the whole content of clause (c)'s first inequality.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FiniteEntropy
import Mathlib.Analysis.SpecialFunctions.Log.Base

namespace OIBridge

namespace HiddenMemory

open Finset Real OIBridge.FiniteEntropy

set_option linter.unusedSectionVars false

variable {Hist V H : Type*} [Fintype Hist] [Fintype V] [Fintype H]
variable [DecidableEq Hist] [DecidableEq V] [DecidableEq H]

/-- A faithful deterministic realization at time `t`: the bijection `φ` on `C_V × C_H`, together
with the law it induces on `(X_<t, X_t, H_t)`.

The bijection is the manuscript's `φ` and the law is what "faithful … reproducing `S`" supplies.
Nothing else is assumed — in particular the next visible value is DEFINED below from `φ` rather
than posited to be a function of the pair. -/
structure Realization (Hist V H : Type*) [Fintype Hist] [Fintype V] [Fintype H] where
  step : V × H ≃ V × H
  w : Hist × V × H → ℝ
  nonneg : ∀ s, 0 ≤ w s
  total : ∑ s, w s = 1

variable (R : Realization Hist V H)

/-- `f_x(h) = π_V(φ(x, h))`: the next visible state. -/
def nextVis (x : V) (h : H) : V := (R.step (x, h)).1

/-- `P(X_<t = p, X_t = x)`, the weight of a history with its endpoint. -/
noncomputable def histProb (p : Hist) (x : V) : ℝ := ∑ h, R.w (p, x, h)

/-- `μ_p`: the hidden posterior `P(H_t = · | X_<t = p, X_t = x)`. -/
noncomputable def post (p : Hist) (x : V) : H → ℝ :=
  fun h => R.w (p, x, h) / histProb R p x

/-- `P(X_{t+1} = · | X_<t = p, X_t = x)`, computed from the joint law rather than posited. -/
noncomputable def nextLaw (p : Hist) (x : V) : V → ℝ :=
  fun v => (∑ h ∈ univ.filter (fun h => nextVis R x h = v), R.w (p, x, h)) / histProb R p x

/-! ### Clause (a): the pushforward identity -/

/-- **(a) Pushforward identity.** `P(X_{t+1} | p, x) = (f_x)_# μ_p`, exactly.

Determinism makes `X_{t+1}` a function of `(X_t, H_t)`, so conditioning on `p` and pushing `μ_p`
through `f_x` IS the conditional law — the manuscript's proof, and the reason the identity is an
equality rather than an approximation. -/
theorem pushforward_identity (p : Hist) (x : V) :
    nextLaw R p x = marg (post R p x) (nextVis R x) := by
  funext v
  simp only [nextLaw, marg, post, div_eq_mul_inv]
  rw [Finset.sum_mul]

/-! ### Clause (b): the distinguishability floor -/

/-- Total variation distance between two finite distributions. -/
noncomputable def tv {α : Type*} [Fintype α] (μ ν : α → ℝ) : ℝ :=
  (1 / 2) * ∑ a, |μ a - ν a|

/-- **Total variation is monotone under a deterministic channel.** Pushing two distributions
through the same map cannot separate them further. -/
theorem tv_marg_le {α β : Type*} [Fintype α] [Fintype β] [DecidableEq α] [DecidableEq β]
    (μ ν : α → ℝ) (e : α → β) : tv (marg μ e) (marg ν e) ≤ tv μ ν := by
  classical
  have hterm : ∀ b : β, |marg μ e b - marg ν e b|
      ≤ ∑ a ∈ univ.filter (fun a => e a = b), |μ a - ν a| := by
    intro b
    rw [marg, marg, ← Finset.sum_sub_distrib]
    exact Finset.abs_sum_le_sum_abs _ _
  have hsum : ∑ b, |marg μ e b - marg ν e b| ≤ ∑ a, |μ a - ν a| := by
    refine (Finset.sum_le_sum fun b _ => hterm b).trans ?_
    exact le_of_eq (Finset.sum_fiberwise_of_maps_to (fun a _ => Finset.mem_univ (e a)) _)
  simp only [tv]
  linarith

/-- **(b) Distinguishability floor.** For two histories sharing an endpoint, the observed gap in
next-step laws is at most the gap between the hidden posteriors. A deterministic map is a channel,
and total variation is monotone under channels. -/
theorem distinguishability_floor (p p' : Hist) (x : V) :
    tv (nextLaw R p x) (nextLaw R p' x) ≤ tv (post R p x) (post R p' x) := by
  rw [pushforward_identity, pushforward_identity]
  exact tv_marg_le _ _ _

/-! ### Clause (c): the capacity floor -/

/-- `X_<t`, as a random variable on the sample space. -/
def varHist : Hist × V × H → Hist := fun s => s.1
/-- `X_t`. -/
def varNow : Hist × V × H → V := fun s => s.2.1
/-- `H_t`. -/
def varHid : Hist × V × H → H := fun s => s.2.2
/-- `X_{t+1}`, which is DEFINED from `φ` and is therefore a function of `(X_t, H_t)` rather than
assumed to be one. That is what makes the Markov chain of clause (c) hold. -/
def varNext : Hist × V × H → V := fun s => nextVis R (varNow s) (varHid s)

/-- Conditional mutual information in BITS, which is the unit clause (c) is stated in. -/
noncomputable def cmiBits {σ α β γ : Type*} [Fintype σ] [DecidableEq σ] [Fintype α]
    [DecidableEq α] [Fintype β] [DecidableEq β] [Fintype γ] [DecidableEq γ]
    (w : σ → ℝ) (a : σ → α) (b : σ → β) (c : σ → γ) : ℝ :=
  cmi w a b c / Real.log 2

/-- `M_t := I(X_<t ; X_{t+1} | X_t)`, in bits. -/
noncomputable def memory : ℝ := cmiBits R.w (varHist) (varNow) (varNext R)

/-- **The capacity bound, in the general form the manuscript's theorems instantiate.**

ANY quantity read off the pair `(X_t, H_t)` — the next visible value, the whole visible future,
anything at all — carries at most the predictive information the hidden state carries, which is at
most `log₂|C_H|`. Determinism is the entire hypothesis, and it enters exactly once: it is what makes
the readout a FUNCTION of the pair, hence `X_<t → H_t → · | X_t` a Markov chain rather than an
assumed one.

`capacity_floor` below is the one-step instance and `C3.c3_necessity` the whole-future instance, so
the two manuscript theorems share this proof rather than duplicating it. -/
theorem capacity_floor_of_fun [Nonempty H] {D : Type*} [Fintype D] [DecidableEq D]
    (d : V × H → D) :
    cmiBits R.w (varHist) (varNow) (fun s => d (varNow s, varHid s))
        ≤ cmiBits R.w (varHist) (varNow) (varHid) ∧
      cmiBits R.w (varHist) (varNow) (varHid) ≤ Real.logb 2 (Fintype.card H) := by
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  constructor
  · -- data processing: the readout is a deterministic function of `(X_t, H_t)`
    have := cmi_le_of_deterministic R.w R.nonneg R.total (varHist) (varNow) (varHid) d
    simp only [cmiBits]
    exact (div_le_div_iff_of_pos_right hlog2).mpr this
  · have := cmi_le_log_card R.w R.nonneg R.total (varHist) (varNow) (varHid)
    rw [cmiBits, Real.logb, div_le_div_iff_of_pos_right hlog2]
    exact this

/-- **(c) Capacity floor.** `M_t ≤ I(X_<t ; H_t | X_t) ≤ log₂ |C_H|`.

`X_<t → H_t → X_{t+1}` is a Markov chain given `X_t` by the same functional dependence that gives
clause (a); data processing gives the first inequality and `I ≤ H(H_t) ≤ log₂|C_H|` the second. It
is the one-step instance of `capacity_floor_of_fun`. -/
theorem capacity_floor [Nonempty H] :
    memory R ≤ cmiBits R.w (varHist) (varNow) (varHid) ∧
      cmiBits R.w (varHist) (varNow) (varHid) ≤ Real.logb 2 (Fintype.card H) :=
  capacity_floor_of_fun R (fun q : V × H => nextVis R q.1 q.2)

/-! ### The theorem

The three clauses, in one statement whose type mirrors the manuscript's. -/

/-- **Theorem (unavoidable hidden predictive memory), [Main] §3.4.**

For ANY faithful deterministic realization: the next-step conditional law is exactly the
pushforward of the hidden posterior; the observed distinguishability of two histories is bounded by
the distinguishability of their posteriors; and the visible predictive information is bounded by
the hidden predictive information, which is bounded by the log of the hidden alphabet. -/
theorem unavoidable_hidden_predictive_memory [Nonempty H] :
    (∀ p : Hist, ∀ x : V, nextLaw R p x = marg (post R p x) (nextVis R x)) ∧
    (∀ p p' : Hist, ∀ x : V,
      tv (nextLaw R p x) (nextLaw R p' x) ≤ tv (post R p x) (post R p' x)) ∧
    (memory R ≤ cmiBits R.w (varHist) (varNow) (varHid) ∧
      cmiBits R.w (varHist) (varNow) (varHid) ≤ Real.logb 2 (Fintype.card H)) :=
  ⟨fun p x => pushforward_identity R p x,
   fun p p' x => distinguishability_floor R p p' x,
   capacity_floor R⟩

/-! ### What these proofs rest on -/

#print axioms pushforward_identity
#print axioms tv_marg_le
#print axioms distinguishability_floor
#print axioms capacity_floor_of_fun
#print axioms capacity_floor
#print axioms unavoidable_hidden_predictive_memory

end HiddenMemory

end OIBridge
