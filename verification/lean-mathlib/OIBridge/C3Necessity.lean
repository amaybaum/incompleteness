/-
  OIBridge/C3Necessity.lean — [Main]'s C3-necessity theorem and its per-process capacity corollary.

      **Theorem (C3 necessity).** Let m = |C_H|. The non-Markovian mutual information satisfies

          I(X_<t ; X_>t | X_t) ≤ log₂ m.

      **Corollary (per-process capacity bound).** Any deterministic-bijection realization of a
      process whose conditional past–future information reaches I* = sup_t I(X_<t ; X_>t | X_t)
      requires m ≥ 2^{I*}.

  A COROLLARY OF THE HIDDEN-MEMORY LAYER, NOT A SECOND PROOF. `HiddenMemory.capacity_floor_of_fun`
  bounds the conditional information of ANY quantity read off `(X_t, H_t)` by `log₂|C_H|`, with
  determinism entering exactly once — it is what makes the readout a function of the pair, hence
  `X_<t → H_t → · | X_t` a Markov chain. The memory theorem instantiates it at the next visible
  value; C3 instantiates it at the WHOLE VISIBLE FUTURE. Lean checks the dependency, so there is no
  duplicated data-processing argument to drift out of agreement.

  WHAT `X_>t` IS HERE. The future is not posited to be a function of `(X_t, H_t)` — it is DEFINED
  by iterating the bijection from that pair, which is the manuscript's "the total system is
  deterministic: X_>t is a function of (X_t, H_t)". Every horizon `L` is covered, and the bound is
  the same for all of them, which is what lets `I*` range over horizons as well as times.

  WHAT `I*` IS. The manuscript's `I*` is a supremum over accessible times. Formally it is the
  maximum over a finite nonempty family of accessible slices — each a realization of the SAME
  hidden alphabet, each with its own visible history alphabet, law and horizon. The common hidden
  alphabet is what makes `m ≥ 2^{I*}` a statement about one physical hidden sector rather than a
  family of unrelated ones; it is an assumption of the corollary and is written into its signature.

  WHAT IS NOT PROVED HERE, because the manuscript denies it. The corollary's sustained-backflow
  reading — `m ≳ 2^{K I_0}` for backflow at rate `I_0` over `K` events — holds only "under the
  additional hypothesis that the per-event contributions accumulate without hidden-state reuse or
  compression", and the manuscript says in the same breath that this independence hypothesis is not
  a consequence of P-indivisibility. Nothing here proves it, and the probe exhibits a realization
  where it fails. Likewise `m ≥ n` is NOT claimed: a two-hidden-state, three-visible-state bijection
  with full distinguishability revival is exactly the manuscript's counterexample to reading C3 as a
  bound set by the visible count.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.HiddenMemory

namespace OIBridge

namespace C3

open Finset Real OIBridge.FiniteEntropy OIBridge.HiddenMemory

set_option linter.unusedSectionVars false

variable {Hist V H : Type*} [Fintype Hist] [Fintype V] [Fintype H]
variable [DecidableEq Hist] [DecidableEq V] [DecidableEq H]

/-! ### The visible future

`X_>t` at horizon `L`, DEFINED by iterating the bijection from `(X_t, H_t)` rather than assumed to
be a function of it. That definition is the manuscript's "the total system is deterministic". -/

/-- The visible future of a state pair, `L` steps of it. -/
def futureOf (R : Realization Hist V H) (L : ℕ) : V × H → (Fin L → V) :=
  fun q j => (R.step^[(j : ℕ) + 1] q).1

/-- `X_>t` as a random variable on the sample space: the visible future read off `(X_t, H_t)`. -/
def varFuture (R : Realization Hist V H) (L : ℕ) : Hist × V × H → (Fin L → V) :=
  fun s => futureOf R L (varNow s, varHid s)

/-- The first entry of the visible future is the next visible value, so C3's readout extends the
memory theorem's rather than replacing it. -/
theorem varFuture_zero (R : Realization Hist V H) {L : ℕ} (hL : 0 < L) (s : Hist × V × H) :
    varFuture R L s ⟨0, hL⟩ = varNext R s := by
  simp [varFuture, futureOf, varNext, nextVis, varNow, varHid]

/-! ### The theorem -/

/-- **Theorem (C3 necessity), [Main] §3.3.** `I(X_<t ; X_>t | X_t) ≤ log₂ m`, at every horizon.

The whole visible future is a function of `(X_t, H_t)`, so conditioning on `X_t` makes
`X_<t → H_t → X_>t` a Markov chain; data processing and `I ≤ log₂|C_H|` finish it. Both steps are
`HiddenMemory.capacity_floor_of_fun`, instantiated at the future readout. -/
theorem c3_necessity [Nonempty H] (R : Realization Hist V H) (L : ℕ) :
    cmiBits R.w (varHist) (varNow) (varFuture R L) ≤ Real.logb 2 (Fintype.card H) := by
  obtain ⟨h1, h2⟩ := capacity_floor_of_fun R (futureOf R L)
  exact le_trans h1 h2

/-- The intermediate quantity is named because the manuscript's chain passes through it: the
predictive information the observer can see is bounded by the information the hidden state holds,
before the alphabet bound is applied at all. -/
theorem c3_necessity_via_hidden [Nonempty H] (R : Realization Hist V H) (L : ℕ) :
    cmiBits R.w (varHist) (varNow) (varFuture R L)
        ≤ cmiBits R.w (varHist) (varNow) (varHid) ∧
      cmiBits R.w (varHist) (varNow) (varHid) ≤ Real.logb 2 (Fintype.card H) :=
  capacity_floor_of_fun R (futureOf R L)

/-! ### `I*` and the per-process capacity bound

`I*` is the manuscript's supremum over accessible times, taken here as a maximum over a finite
nonempty family of slices sharing a hidden alphabet. Sharing the alphabet is the whole point: the
corollary is a statement about the size of ONE hidden sector. -/

/-- `I* = sup_t I(X_<t ; X_>t | X_t)`, over a finite nonempty family of accessible slices and their
horizons. Each slice carries its own visible-history alphabet, law and horizon; all of them share
the hidden alphabet `H`. -/
noncomputable def Istar {ι : Type*} {F : Finset ι} (hF : F.Nonempty)
    (R : ι → Realization Hist V H) (L : ι → ℕ) : ℝ :=
  F.sup' hF fun i => cmiBits (R i).w (varHist) (varNow) (varFuture (R i) (L i))

theorem Istar_le_log_card [Nonempty H] {ι : Type*} {F : Finset ι} (hF : F.Nonempty)
    (R : ι → Realization Hist V H) (L : ι → ℕ) :
    Istar hF R L ≤ Real.logb 2 (Fintype.card H) :=
  Finset.sup'_le hF _ fun i _ => c3_necessity (R i) (L i)

/-- **Corollary (per-process capacity bound), [Main] §3.3.** `m ≥ 2^{I*}`.

The hidden sector must be at least as large as the backflow it carries. Note what this is NOT: it
is not `m ≥ n`, and it is not a bound growing with the number of coupling events — the manuscript
is explicit that the latter needs an independence hypothesis P-indivisibility does not supply. -/
theorem card_hidden_ge_two_pow_Istar [Nonempty H] {ι : Type*} {F : Finset ι} (hF : F.Nonempty)
    (R : ι → Realization Hist V H) (L : ι → ℕ) :
    (2 : ℝ) ^ (Istar hF R L) ≤ (Fintype.card H : ℝ) := by
  have hcard : (0 : ℝ) < (Fintype.card H : ℝ) := by
    exact_mod_cast Fintype.card_pos_iff.2 ‹Nonempty H›
  have hb : (1 : ℝ) < 2 := by norm_num
  have hstep : (2 : ℝ) ^ (Istar hF R L) ≤ (2 : ℝ) ^ (Real.logb 2 (Fintype.card H)) :=
    (Real.rpow_le_rpow_left_iff hb).2 (Istar_le_log_card hF R L)
  rwa [Real.rpow_logb (by norm_num) (by norm_num) hcard] at hstep

/-- **The C3 clause as the manuscript states it**, theorem and corollary together: the observable
past–future information at every accessible slice is bounded by `log₂ m`, and therefore the hidden
alphabet is at least `2^{I*}`. -/
theorem c3_necessity_and_capacity [Nonempty H] {ι : Type*} {F : Finset ι} (hF : F.Nonempty)
    (R : ι → Realization Hist V H) (L : ι → ℕ) :
    (∀ i ∈ F, cmiBits (R i).w (varHist) (varNow) (varFuture (R i) (L i))
        ≤ Real.logb 2 (Fintype.card H)) ∧
      (2 : ℝ) ^ (Istar hF R L) ≤ (Fintype.card H : ℝ) :=
  ⟨fun i _ => c3_necessity (R i) (L i), card_hidden_ge_two_pow_Istar hF R L⟩

/-! ### What these proofs rest on -/

#print axioms varFuture_zero
#print axioms c3_necessity
#print axioms c3_necessity_via_hidden
#print axioms Istar_le_log_card
#print axioms card_hidden_ge_two_pow_Istar
#print axioms c3_necessity_and_capacity

end C3

end OIBridge
