import OIBridge.FiniteEntropy
import Mathlib.Analysis.SpecialFunctions.BinaryEntropy
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Pi
import Mathlib.GroupTheory.Perm.Basic

/-!
# PREP-REGRESS-1: conservation, the transfer identity and the held-predictability budget

Kernel statements of three results of the research record
`verification/programmes/oi-qm/reconstruction/prep-regress-1-20261119/RESULT.md`, §4, node 2.
Everything is finite and sum-based; laws are functions `p : S → ℝ` with `0 ≤ p` and `Σ p = 1`,
and the uniform law is `u = 1/|S|`. Information is in nats; dividing by `log 2` gives the
record's bits, and the budget is also stated in bits.

* **2.1, conservation** (`relEnt_evolve`, `relEnt_evolve_unif`). For a bijection `φ` of a finite
  set and any `φ`-invariant `μ`, `D(p_t‖μ) = D(p₀‖μ)` for every `t ∈ ℤ`, where
  `p_t = (φ^t)_* p₀`. For `μ = u`, `D(p‖u) = log|S| − H(p)` (`relEnt_unif`).
* **2.3, exact transfer identity** (`transfer_identity`, `transfer_identity_evolve`). On
  `S = H × Rest`, `D(p‖u) = K(H) + D(p_Rest‖u_Rest)` with `K(H) = log|H| − H(H|Rest)` and
  `H(H|Rest) = −Σ p(h,r) log (p(h,r)/p_Rest(r))`; hence
  `K_t(H) + D(p_{Rest,t}‖u_Rest) = D(p₀‖u)` for every `t`.
* **2.5, multi-record bound** (`held_predictability_budget`, `held_predictability_budget_bits`,
  `held_predictability_budget_bits_uniform`, `multi_record_bound`). On `S = A × B`, with
  predictors `f : A → {0,1}^N` read from the block `A` and targets `g : B → {0,1}^N` read from the
  disjoint block `B`, with `g` jointly balanced (`g_* u_B` uniform on `{0,1}^N`), and with
  `ε_k = P_p(f_k(A) ≠ g_k(B))` evaluated for one law `p` (one time `T`):
  `D(p‖u) ≥ Σ_k (1 − h₂(ε_k))` in bits, and `≥ N (1 − h₂(ε̄))` when every `ε_k ≤ ε̄ ≤ 1/2`.
  With `p = p_T` and conservation, the left side is `D(p₀‖u)`.

The hypotheses of 2.5 enter as follows. Disjointness of predictors and targets is the product
structure: `f` reads only the `A` factor and `g` only the `B` factor of one state. Joint
balancedness is the hypothesis `hbal` on the pushforward `marg (unif B) g`. Retention at one time
is the single law `p` at which every `ε_k` is evaluated. A third block that is neither predictor
nor target is absorbed into `A`.

The proof of 2.5 here does not pass through Fano's inequality or a separate data-processing
lemma. It applies Gibbs' inequality (`FiniteEntropy.sum_mul_log_le`) once, against the comparison
law `q(a,b) = 2^N / (|A||B|) · Π_k w_k(f_k a, g_k b)`, where `w_k` is the binary symmetric channel
with crossover `ε_k`. Joint balancedness makes `q` a probability law (`comparison_bound`), and
`E_p log Π_k w_k = −Σ_k h(ε_k)` (`sum_mul_log_bscProd`). The resulting inequality is the record's
displayed bound `D(p₀‖u) ≥ N − Σ_k h₂(ε_k)`.

Not formalized here: the per-cycle `(N+1)` form, the local and infinite-volume form 2.6, the
fresh-cell monotonicity 2.7, the readiness ceiling 2.4, and the necessity countercontrols of 2.5
(C15a, C15b).
-/

open scoped BigOperators

namespace OIBridge
namespace PrepRegressBudget

open FiniteEntropy

noncomputable section

set_option autoImplicit false
set_option linter.unusedSectionVars false

/-- The uniform law `u` on a finite type: `u(a) = 1/|α|`. -/
def unif (α : Type*) [Fintype α] (_a : α) : ℝ := (Fintype.card α : ℝ)⁻¹

/-! ### Relative entropy and conservation (record 2.1) -/

section Conservation

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- Relative entropy `D(p‖μ) = Σ_s p(s) log (p(s)/μ(s))`, in nats. -/
def relEnt (p μ : S → ℝ) : ℝ := ∑ s, p s * Real.log (p s / μ s)

/-- The pushforward of a law along a bijection: `(τ_* p)(s) = p(τ⁻¹ s)`. -/
def push (τ : Equiv.Perm S) (p : S → ℝ) (s : S) : ℝ := p (τ⁻¹ s)

/-- The law at time `t` of the dynamics `φ` started from `p`: `p_t = (φ^t)_* p`, `t ∈ ℤ`. -/
def evolve (φ : Equiv.Perm S) (t : ℤ) (p : S → ℝ) : S → ℝ := push (φ ^ t) p

/-- A law sums to one only on a nonempty type; this supplies a point of positive weight. -/
theorem exists_of_total {p : S → ℝ} (htot : ∑ s, p s = 1) : ∃ s, p s ≠ 0 := by
  have hne : ∑ s, p s ≠ 0 := by rw [htot]; exact one_ne_zero
  obtain ⟨s, -, hs⟩ := Finset.exists_ne_zero_of_sum_ne_zero hne
  exact ⟨s, hs⟩

/-- `D(p‖u) = log|S| − H(p)` for every law `p`. -/
theorem relEnt_unif (p : S → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1) :
    relEnt p (unif S) = Real.log (Fintype.card S) - entropy p := by
  obtain ⟨s₀, -⟩ := exists_of_total htot
  have hcard : 0 < (Fintype.card S : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨s₀⟩
  have key : ∀ s, p s * Real.log (p s / unif S s)
      = p s * Real.log (p s) + p s * Real.log (Fintype.card S) := by
    intro s
    rcases eq_or_lt_of_le (hp s) with h0 | hpos
    · rw [← h0]; simp
    · rw [unif, div_inv_eq_mul, Real.log_mul hpos.ne' hcard.ne', mul_add]
  unfold relEnt
  rw [Finset.sum_congr rfl (fun s _ => key s), Finset.sum_add_distrib, ← Finset.sum_mul, htot,
    one_mul, sum_mul_log_eq_neg_entropy p]
  ring

/-- Pushforward along a bijection preserves positivity. -/
theorem evolve_nonneg (φ : Equiv.Perm S) (t : ℤ) {p : S → ℝ} (hp : ∀ s, 0 ≤ p s) :
    ∀ s, 0 ≤ evolve φ t p s :=
  fun s => hp ((φ ^ t)⁻¹ s)

/-- Pushforward along a bijection preserves total mass. -/
theorem sum_evolve (φ : Equiv.Perm S) (t : ℤ) (p : S → ℝ) :
    ∑ s, evolve φ t p s = ∑ s, p s :=
  Equiv.sum_comp ((φ ^ t)⁻¹) p

/-- Relative entropy to a `τ`-invariant reference is unchanged by pushing forward along `τ`. -/
theorem relEnt_push (p μ : S → ℝ) (τ : Equiv.Perm S) (hμ : ∀ s, μ (τ s) = μ s) :
    relEnt (push τ p) μ = relEnt p μ := by
  simp only [relEnt, push]
  have h : ∀ s, p (τ⁻¹ s) * Real.log (p (τ⁻¹ s) / μ s)
      = p (τ⁻¹ s) * Real.log (p (τ⁻¹ s) / μ (τ⁻¹ s)) := by
    intro s
    have hs : μ (τ (τ⁻¹ s)) = μ (τ⁻¹ s) := hμ (τ⁻¹ s)
    rw [Equiv.Perm.apply_inv_self] at hs
    rw [hs]
  rw [Finset.sum_congr rfl (fun s _ => h s)]
  exact Equiv.sum_comp (τ⁻¹) (fun x => p x * Real.log (p x / μ x))

/-- A reference invariant under `φ` is invariant under every integer power of `φ`. -/
theorem invariant_zpow (μ : S → ℝ) (φ : Equiv.Perm S) (hμ : ∀ s, μ (φ s) = μ s) (t : ℤ) :
    ∀ s, μ ((φ ^ t) s) = μ s := by
  induction t with
  | zero => intro s; simp
  | succ i ih =>
    intro s
    rw [zpow_add_one, Equiv.Perm.mul_apply, ih, hμ]
  | pred i ih =>
    intro s
    rw [zpow_sub_one, Equiv.Perm.mul_apply, ih]
    have hs : μ (φ (φ⁻¹ s)) = μ (φ⁻¹ s) := hμ (φ⁻¹ s)
    rw [Equiv.Perm.apply_inv_self] at hs
    exact hs.symm

/-- **Record 2.1, conservation.** For a bijection `φ` of a finite set and a `φ`-invariant
reference `μ`, `D(p_t‖μ) = D(p₀‖μ)` for every `t ∈ ℤ`. -/
theorem relEnt_evolve (φ : Equiv.Perm S) (μ p : S → ℝ) (hμ : ∀ s, μ (φ s) = μ s) (t : ℤ) :
    relEnt (evolve φ t p) μ = relEnt p μ :=
  relEnt_push p μ (φ ^ t) (invariant_zpow μ φ hμ t)

/-- **Record 2.1 for `μ = u`.** `D(p_t‖u) = D(p₀‖u)` for every bijection and every `t ∈ ℤ`. -/
theorem relEnt_evolve_unif (φ : Equiv.Perm S) (p : S → ℝ) (t : ℤ) :
    relEnt (evolve φ t p) (unif S) = relEnt p (unif S) :=
  relEnt_evolve φ (unif S) p (fun _ => rfl) t

end Conservation

/-! ### The exact transfer identity (record 2.3) -/

section Transfer

variable {H R : Type*} [Fintype H] [Fintype R] [DecidableEq H] [DecidableEq R]

/-- The law of the rest block: `p_Rest(r) = Σ_h p(h, r)`. -/
def restLaw (p : H × R → ℝ) (r : R) : ℝ := ∑ h, p (h, r)

/-- Conditional entropy `H(H | Rest) = −Σ_{h,r} p(h,r) log (p(h,r) / p_Rest(r))`, in nats. -/
def condEnt (p : H × R → ℝ) : ℝ := -∑ s, p s * Real.log (p s / restLaw p s.2)

/-- Held content of the block `H`: `K(H) = log|H| − H(H | Rest)`, in nats. -/
def heldContent (p : H × R → ℝ) : ℝ := Real.log (Fintype.card H) - condEnt p

theorem sum_restLaw (p : H × R → ℝ) : ∑ r, restLaw p r = ∑ s, p s := by
  simp only [restLaw]
  rw [Fintype.sum_prod_type]
  exact Finset.sum_comm

/-- The chain rule `H(H | Rest) = H(H, Rest) − H(Rest)`. -/
theorem condEnt_eq (p : H × R → ℝ) (hp : ∀ s, 0 ≤ p s) :
    condEnt p = entropy p - entropy (restLaw p) := by
  have hle : ∀ s : H × R, p s ≤ restLaw p s.2 := by
    rintro ⟨h, r⟩
    exact Finset.single_le_sum (f := fun h' => p (h', r)) (fun h' _ => hp (h', r))
      (Finset.mem_univ h)
  have key : ∀ s : H × R, p s * Real.log (p s / restLaw p s.2)
      = p s * Real.log (p s) - p s * Real.log (restLaw p s.2) := by
    intro s
    rcases eq_or_lt_of_le (hp s) with h0 | hpos
    · rw [← h0]; simp
    · have hr : 0 < restLaw p s.2 := lt_of_lt_of_le hpos (hle s)
      rw [Real.log_div hpos.ne' hr.ne', mul_sub]
  have hsplit : ∑ s : H × R, p s * Real.log (restLaw p s.2)
      = ∑ r, restLaw p r * Real.log (restLaw p r) := by
    rw [Fintype.sum_prod_type, Finset.sum_comm]
    refine Finset.sum_congr rfl fun r _ => ?_
    simp only [restLaw, Finset.sum_mul]
  unfold condEnt
  rw [Finset.sum_congr rfl (fun s _ => key s), Finset.sum_sub_distrib, hsplit,
    sum_mul_log_eq_neg_entropy p, sum_mul_log_eq_neg_entropy (restLaw p)]
  ring

/-- **Record 2.3, exact transfer identity.** For every law `p` on `H × Rest`,
`D(p‖u) = K(H) + D(p_Rest‖u_Rest)`. -/
theorem transfer_identity (p : H × R → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1) :
    relEnt p (unif (H × R)) = heldContent p + relEnt (restLaw p) (unif R) := by
  obtain ⟨s₀, -⟩ := exists_of_total htot
  have hH : 0 < (Fintype.card H : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨s₀.1⟩
  have hR : 0 < (Fintype.card R : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨s₀.2⟩
  have hRn : ∀ r, 0 ≤ restLaw p r := fun r => Finset.sum_nonneg fun h _ => hp (h, r)
  have hRt : ∑ r, restLaw p r = 1 := (sum_restLaw p).trans htot
  rw [relEnt_unif p hp htot, relEnt_unif (restLaw p) hRn hRt, heldContent, condEnt_eq p hp,
    Fintype.card_prod, Nat.cast_mul, Real.log_mul hH.ne' hR.ne']
  ring

/-- **Record 2.3 along the dynamics.** For a bijection `φ` of `H × Rest` and every `t ∈ ℤ`,
`K_t(H) + D(p_{Rest,t}‖u_Rest) = D(p₀‖u)`. -/
theorem transfer_identity_evolve (φ : Equiv.Perm (H × R)) (p₀ : H × R → ℝ)
    (hp₀ : ∀ s, 0 ≤ p₀ s) (htot₀ : ∑ s, p₀ s = 1) (t : ℤ) :
    heldContent (evolve φ t p₀) + relEnt (restLaw (evolve φ t p₀)) (unif R)
      = relEnt p₀ (unif (H × R)) := by
  rw [← transfer_identity (evolve φ t p₀) (evolve_nonneg φ t hp₀)
    ((sum_evolve φ t p₀).trans htot₀), relEnt_evolve_unif]

/-- A rise of held content in `H` equals the fall of the rest's relative entropy:
`K_{t₁}(H) − K_{t₀}(H) = D(p_{Rest,t₀}‖u) − D(p_{Rest,t₁}‖u)`. -/
theorem heldContent_change (φ : Equiv.Perm (H × R)) (p₀ : H × R → ℝ)
    (hp₀ : ∀ s, 0 ≤ p₀ s) (htot₀ : ∑ s, p₀ s = 1) (t₀ t₁ : ℤ) :
    heldContent (evolve φ t₁ p₀) - heldContent (evolve φ t₀ p₀)
      = relEnt (restLaw (evolve φ t₀ p₀)) (unif R)
        - relEnt (restLaw (evolve φ t₁ p₀)) (unif R) := by
  have h₀ := transfer_identity_evolve φ p₀ hp₀ htot₀ t₀
  have h₁ := transfer_identity_evolve φ p₀ hp₀ htot₀ t₁
  linarith

end Transfer

/-! ### The held-predictability budget (record 2.5) -/

section Budget

variable {A B X Y : Type*} [Fintype A] [Fintype B] [Fintype X] [Fintype Y]
  [DecidableEq A] [DecidableEq B] [DecidableEq X] [DecidableEq Y]

/-- **Comparison bound.** Let `g` be balanced (`g_* u_B = u_Y`) and let `ρ(x, ·)` be a law on
`Y` for every `x`, positive wherever `p` is. Then
`log|Y| + E_p log ρ(f(A), g(B)) ≤ D(p‖u)`. This is Gibbs' inequality against the law
`q(a,b) = |Y| / (|A||B|) · ρ(f a, g b)`, which balancedness makes a probability law. -/
theorem comparison_bound (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → X) (g : B → Y) (hbal : ∀ y, marg (unif B) g y = unif Y y)
    (ρ : X → Y → ℝ) (hρ0 : ∀ x y, 0 ≤ ρ x y) (hρ1 : ∀ x, ∑ y, ρ x y = 1)
    (hsupp : ∀ s, 0 < p s → 0 < ρ (f s.1) (g s.2)) :
    Real.log (Fintype.card Y) + ∑ s, p s * Real.log (ρ (f s.1) (g s.2))
      ≤ relEnt p (unif (A × B)) := by
  obtain ⟨s₀, -⟩ := exists_of_total htot
  have hA : 0 < (Fintype.card A : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨s₀.1⟩
  have hB : 0 < (Fintype.card B : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨s₀.2⟩
  have hY : 0 < (Fintype.card Y : ℝ) := by exact_mod_cast Fintype.card_pos_iff.mpr ⟨g s₀.2⟩
  have hAB : (Fintype.card (A × B) : ℝ) = Fintype.card A * Fintype.card B := by
    rw [Fintype.card_prod, Nat.cast_mul]
  -- the sum over a block of targets, by balancedness
  have hfib : ∀ a, ∑ b, ρ (f a) (g b) = (Fintype.card B : ℝ) / Fintype.card Y := by
    intro a
    have h := sum_mul_comp (unif B) g (ρ (f a))
    simp only [hbal] at h
    simp only [unif] at h
    rw [← Finset.mul_sum, ← Finset.mul_sum, hρ1, mul_one] at h
    calc ∑ b, ρ (f a) (g b)
        = (Fintype.card B : ℝ) * ((Fintype.card B : ℝ)⁻¹ * ∑ b, ρ (f a) (g b)) := by
          rw [← mul_assoc, mul_inv_cancel₀ hB.ne', one_mul]
      _ = (Fintype.card B : ℝ) / Fintype.card Y := by rw [h, div_eq_mul_inv]
  obtain ⟨c, hc⟩ : ∃ c : ℝ, c = (Fintype.card Y : ℝ) / Fintype.card (A × B) := ⟨_, rfl⟩
  have hcpos : 0 < c := by rw [hc, hAB]; exact div_pos hY (mul_pos hA hB)
  have hqsum : ∑ s : A × B, c * ρ (f s.1) (g s.2) = 1 := by
    rw [← Finset.mul_sum, Fintype.sum_prod_type]
    simp only [hfib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    rw [hc, hAB]
    have hYne : (Fintype.card Y : ℝ) ≠ 0 := hY.ne'
    have hABne : (Fintype.card A : ℝ) * Fintype.card B ≠ 0 := (mul_pos hA hB).ne'
    calc _ = ((Fintype.card Y : ℝ) * (Fintype.card Y : ℝ)⁻¹)
          * (((Fintype.card A : ℝ) * Fintype.card B)
            * ((Fintype.card A : ℝ) * Fintype.card B)⁻¹) := by ring
      _ = 1 := by rw [mul_inv_cancel₀ hYne, mul_inv_cancel₀ hABne, one_mul]
  have hgibbs : ∑ s, p s * Real.log (c * ρ (f s.1) (g s.2)) ≤ ∑ s, p s * Real.log (p s) :=
    sum_mul_log_le p (fun s => c * ρ (f s.1) (g s.2)) hp
      (fun s => mul_nonneg hcpos.le (hρ0 _ _)) (le_of_eq (hqsum.trans htot.symm))
      (fun s hs => mul_pos hcpos (hsupp s hs))
  have hlog : ∀ s : A × B, p s * Real.log (c * ρ (f s.1) (g s.2))
      = p s * Real.log c + p s * Real.log (ρ (f s.1) (g s.2)) := by
    intro s
    rcases eq_or_lt_of_le (hp s) with h0 | hpos
    · rw [← h0]; simp
    · rw [Real.log_mul hcpos.ne' (hsupp s hpos).ne', mul_add]
  rw [Finset.sum_congr rfl (fun s _ => hlog s), Finset.sum_add_distrib, ← Finset.sum_mul, htot,
    one_mul] at hgibbs
  have hlogc : Real.log c = Real.log (Fintype.card Y) - Real.log (Fintype.card (A × B)) := by
    rw [hc]
    exact Real.log_div hY.ne' (by rw [hAB]; exact (mul_pos hA hB).ne')
  rw [hlogc] at hgibbs
  have hent := sum_mul_log_eq_neg_entropy p
  rw [relEnt_unif p hp htot]
  linarith

variable {N : ℕ}

/-- Binary symmetric channel weight with crossover `e`: `1 − e` if the bits agree, `e` if not. -/
def bsc (e : ℝ) (b c : Bool) : ℝ := if b = c then 1 - e else e

/-- Product of `N` binary symmetric channels with crossovers `ε k`. -/
def bscProd (ε : Fin N → ℝ) (x y : Fin N → Bool) : ℝ := ∏ k, bsc (ε k) (x k) (y k)

/-- The error rate of record `k`: `ε_k = P_p(f_k(A) ≠ g_k(B))`. -/
def mismatch (p : A × B → ℝ) (f : A → Fin N → Bool) (g : B → Fin N → Bool) (k : Fin N) : ℝ :=
  ∑ s, if f s.1 k = g s.2 k then 0 else p s

theorem mismatchTerm_nonneg (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (f : A → Fin N → Bool)
    (g : B → Fin N → Bool) (k : Fin N) (s : A × B) :
    0 ≤ (if f s.1 k = g s.2 k then (0 : ℝ) else p s) := by
  split_ifs
  · exact le_rfl
  · exact hp s

theorem matchTerm_nonneg (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (f : A → Fin N → Bool)
    (g : B → Fin N → Bool) (k : Fin N) (s : A × B) :
    0 ≤ (if f s.1 k = g s.2 k then p s else (0 : ℝ)) := by
  split_ifs
  · exact hp s
  · exact le_rfl

/-- The agreement mass of record `k` is `1 − ε_k`. -/
theorem match_add_mismatch (p : A × B → ℝ) (htot : ∑ s, p s = 1) (f : A → Fin N → Bool)
    (g : B → Fin N → Bool) (k : Fin N) :
    (∑ s, if f s.1 k = g s.2 k then p s else 0) = 1 - mismatch p f g k := by
  rw [mismatch, ← htot, eq_sub_iff_add_eq, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun s _ => ?_
  split_ifs <;> simp

theorem mismatch_nonneg (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (f : A → Fin N → Bool)
    (g : B → Fin N → Bool) (k : Fin N) : 0 ≤ mismatch p f g k :=
  Finset.sum_nonneg fun s _ => mismatchTerm_nonneg p hp f g k s

theorem mismatch_le_one (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool) (k : Fin N) : mismatch p f g k ≤ 1 := by
  have h := match_add_mismatch p htot f g k
  have h0 : 0 ≤ ∑ s, (if f s.1 k = g s.2 k then p s else 0) :=
    Finset.sum_nonneg fun s _ => matchTerm_nonneg p hp f g k s
  linarith

theorem le_mismatch (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (f : A → Fin N → Bool)
    (g : B → Fin N → Bool) (k : Fin N) {s : A × B} (hs : f s.1 k ≠ g s.2 k) :
    p s ≤ mismatch p f g k := by
  have h := Finset.single_le_sum
    (f := fun s' : A × B => if f s'.1 k = g s'.2 k then (0 : ℝ) else p s')
    (fun s' _ => mismatchTerm_nonneg p hp f g k s') (Finset.mem_univ s)
  simp only [if_neg hs] at h
  exact h

theorem le_one_sub_mismatch (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool) (k : Fin N) {s : A × B}
    (hs : f s.1 k = g s.2 k) : p s ≤ 1 - mismatch p f g k := by
  rw [← match_add_mismatch p htot f g k]
  have h := Finset.single_le_sum
    (f := fun s' : A × B => if f s'.1 k = g s'.2 k then p s' else (0 : ℝ))
    (fun s' _ => matchTerm_nonneg p hp f g k s') (Finset.mem_univ s)
  simp only [if_pos hs] at h
  exact h

theorem bsc_nonneg {e : ℝ} (h0 : 0 ≤ e) (h1 : e ≤ 1) (b c : Bool) : 0 ≤ bsc e b c := by
  unfold bsc
  split_ifs
  · linarith
  · exact h0

theorem bsc_sum (e : ℝ) (b : Bool) : ∑ c, bsc e b c = 1 := by
  cases b <;> simp [bsc, Fintype.sum_bool] <;> ring

theorem bscProd_sum (ε : Fin N → ℝ) (x : Fin N → Bool) : ∑ y, bscProd ε x y = 1 := by
  unfold bscProd
  rw [← Fintype.prod_sum]
  simp [bsc_sum]

theorem bscProd_nonneg {ε : Fin N → ℝ} (h0 : ∀ k, 0 ≤ ε k) (h1 : ∀ k, ε k ≤ 1)
    (x y : Fin N → Bool) : 0 ≤ bscProd ε x y :=
  Finset.prod_nonneg fun k _ => bsc_nonneg (h0 k) (h1 k) (x k) (y k)

/-- Every channel factor is positive at a point of positive weight. -/
theorem bsc_pos (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool) {s : A × B} (hs : 0 < p s) (k : Fin N) :
    0 < bsc (mismatch p f g k) (f s.1 k) (g s.2 k) := by
  unfold bsc
  split_ifs with h
  · exact lt_of_lt_of_le hs (le_one_sub_mismatch p hp htot f g k h)
  · exact lt_of_lt_of_le hs (le_mismatch p hp f g k h)

theorem bscProd_pos (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool) {s : A × B} (hs : 0 < p s) :
    0 < bscProd (mismatch p f g) (f s.1) (g s.2) :=
  Finset.prod_pos fun k _ => bsc_pos p hp htot f g hs k

/-- `E_p log Π_k w_k(f_k, g_k) = Σ_k (ε_k log ε_k + (1 − ε_k) log (1 − ε_k))`. -/
theorem sum_mul_log_bscProd (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool) :
    ∑ s, p s * Real.log (bscProd (mismatch p f g) (f s.1) (g s.2))
      = ∑ k, (mismatch p f g k * Real.log (mismatch p f g k)
          + (1 - mismatch p f g k) * Real.log (1 - mismatch p f g k)) := by
  have hterm : ∀ s : A × B, p s * Real.log (bscProd (mismatch p f g) (f s.1) (g s.2))
      = ∑ k, p s * Real.log (bsc (mismatch p f g k) (f s.1 k) (g s.2 k)) := by
    intro s
    rcases eq_or_lt_of_le (hp s) with h0 | hpos
    · rw [← h0]; simp
    · rw [bscProd, Real.log_prod (s := Finset.univ)
          (f := fun k => bsc (mismatch p f g k) (f s.1 k) (g s.2 k))
          (fun k _ => (bsc_pos p hp htot f g hpos k).ne'), Finset.mul_sum]
  rw [Finset.sum_congr rfl (fun s _ => hterm s), Finset.sum_comm]
  refine Finset.sum_congr rfl fun k _ => ?_
  have hsplit : ∀ s : A × B, p s * Real.log (bsc (mismatch p f g k) (f s.1 k) (g s.2 k))
      = (if f s.1 k = g s.2 k then p s else 0) * Real.log (1 - mismatch p f g k)
        + (if f s.1 k = g s.2 k then 0 else p s) * Real.log (mismatch p f g k) := by
    intro s
    unfold bsc
    split_ifs <;> ring
  rw [Finset.sum_congr rfl (fun s _ => hsplit s), Finset.sum_add_distrib, ← Finset.sum_mul,
    ← Finset.sum_mul, match_add_mismatch p htot f g k]
  unfold mismatch
  ring

/-- `ε log ε + (1 − ε) log (1 − ε) = −h(ε)`, with `h` Mathlib's binary entropy in nats. -/
theorem neg_binEntropy (e : ℝ) :
    e * Real.log e + (1 - e) * Real.log (1 - e) = -Real.binEntropy e := by
  rw [Real.binEntropy_eq_negMulLog_add_negMulLog_one_sub]
  simp only [Real.negMulLog]
  ring

/-- **Record 2.5, multi-record bound (nats).** On `S = A × B`, with predictors `f` read from `A`,
jointly balanced targets `g` read from the disjoint block `B`, and the error rates
`ε_k = P_p(f_k(A) ≠ g_k(B))` of one law `p`: `D(p‖u) ≥ N log 2 − Σ_k h(ε_k)`. -/
theorem held_predictability_budget (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s) (htot : ∑ s, p s = 1)
    (f : A → Fin N → Bool) (g : B → Fin N → Bool)
    (hbal : ∀ y, marg (unif B) g y = unif (Fin N → Bool) y) :
    (N : ℝ) * Real.log 2 - ∑ k, Real.binEntropy (mismatch p f g k)
      ≤ relEnt p (unif (A × B)) := by
  have h := comparison_bound p hp htot f g hbal (bscProd (mismatch p f g))
    (fun x y => bscProd_nonneg (mismatch_nonneg p hp f g) (mismatch_le_one p hp htot f g) x y)
    (fun x => bscProd_sum (mismatch p f g) x) (fun s hs => bscProd_pos p hp htot f g hs)
  rw [sum_mul_log_bscProd p hp htot f g] at h
  have hcard : Real.log (Fintype.card (Fin N → Bool)) = (N : ℝ) * Real.log 2 := by
    simp [Fintype.card_fun, Real.log_pow]
  rw [hcard, Finset.sum_congr rfl (fun k _ => neg_binEntropy (mismatch p f g k)),
    Finset.sum_neg_distrib] at h
  linarith

/-- **Record 2.5, multi-record bound (bits).** Under the hypotheses of
`held_predictability_budget`, `D(p‖u)/log 2 ≥ Σ_k (1 − h₂(ε_k))` with
`h₂ = h / log 2` the binary entropy in bits. -/
theorem held_predictability_budget_bits (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s)
    (htot : ∑ s, p s = 1) (f : A → Fin N → Bool) (g : B → Fin N → Bool)
    (hbal : ∀ y, marg (unif B) g y = unif (Fin N → Bool) y) :
    ∑ k, (1 - Real.binEntropy (mismatch p f g k) / Real.log 2)
      ≤ relEnt p (unif (A × B)) / Real.log 2 := by
  have h := held_predictability_budget p hp htot f g hbal
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  rw [le_div_iff₀ hl, Finset.sum_mul]
  have hterm : ∀ k : Fin N, (1 - Real.binEntropy (mismatch p f g k) / Real.log 2) * Real.log 2
      = Real.log 2 - Real.binEntropy (mismatch p f g k) := by
    intro k
    rw [sub_mul, one_mul, div_mul_cancel₀ _ hl.ne']
  rw [Finset.sum_congr rfl (fun k _ => hterm k), Finset.sum_sub_distrib, Finset.sum_const,
    Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  linarith

/-- **Record 2.5, uniform form (bits).** If every `ε_k ≤ ε̄ ≤ 1/2`, then
`D(p‖u)/log 2 ≥ N (1 − h₂(ε̄))`. -/
theorem held_predictability_budget_bits_uniform (p : A × B → ℝ) (hp : ∀ s, 0 ≤ p s)
    (htot : ∑ s, p s = 1) (f : A → Fin N → Bool) (g : B → Fin N → Bool)
    (hbal : ∀ y, marg (unif B) g y = unif (Fin N → Bool) y)
    (e : ℝ) (he : e ≤ 2⁻¹) (hk : ∀ k, mismatch p f g k ≤ e) :
    (N : ℝ) * (1 - Real.binEntropy e / Real.log 2) ≤ relEnt p (unif (A × B)) / Real.log 2 := by
  have h := held_predictability_budget_bits p hp htot f g hbal
  have hl : 0 < Real.log 2 := Real.log_pos (by norm_num)
  have hmono : ∀ k, Real.binEntropy (mismatch p f g k) ≤ Real.binEntropy e := by
    intro k
    have h0 := mismatch_nonneg p hp f g k
    exact Real.binEntropy_strictMonoOn.monotoneOn ⟨h0, (hk k).trans he⟩
      ⟨h0.trans (hk k), he⟩ (hk k)
  have hconst : ∑ _k : Fin N, (1 - Real.binEntropy e / Real.log 2)
      = (N : ℝ) * (1 - Real.binEntropy e / Real.log 2) := by
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  have hsum : (N : ℝ) * (1 - Real.binEntropy e / Real.log 2)
      ≤ ∑ k, (1 - Real.binEntropy (mismatch p f g k) / Real.log 2) := by
    rw [← hconst]
    refine Finset.sum_le_sum fun k _ => ?_
    have h1 : Real.binEntropy (mismatch p f g k) * (Real.log 2)⁻¹
        ≤ Real.binEntropy e * (Real.log 2)⁻¹ :=
      mul_le_mul_of_nonneg_right (hmono k) (inv_nonneg.mpr hl.le)
    rw [div_eq_mul_inv, div_eq_mul_inv]
    linarith
  exact hsum.trans h

/-- **Record 2.5 with conservation.** For a bijection `φ` of `A × B`, an initial law `p₀` and
one time `T`, with the error rates evaluated on `p_T = (φ^T)_* p₀`:
`D(p₀‖u)/log 2 ≥ Σ_k (1 − h₂(ε_k))`. -/
theorem multi_record_bound (φ : Equiv.Perm (A × B)) (p₀ : A × B → ℝ) (hp₀ : ∀ s, 0 ≤ p₀ s)
    (htot₀ : ∑ s, p₀ s = 1) (T : ℤ) (f : A → Fin N → Bool) (g : B → Fin N → Bool)
    (hbal : ∀ y, marg (unif B) g y = unif (Fin N → Bool) y) :
    ∑ k, (1 - Real.binEntropy (mismatch (evolve φ T p₀) f g k) / Real.log 2)
      ≤ relEnt p₀ (unif (A × B)) / Real.log 2 := by
  rw [← relEnt_evolve_unif φ p₀ T]
  exact held_predictability_budget_bits (evolve φ T p₀) (evolve_nonneg φ T hp₀)
    ((sum_evolve φ T p₀).trans htot₀) f g hbal

end Budget

end

#print axioms relEnt_unif
#print axioms relEnt_evolve
#print axioms relEnt_evolve_unif
#print axioms condEnt_eq
#print axioms transfer_identity
#print axioms transfer_identity_evolve
#print axioms heldContent_change
#print axioms comparison_bound
#print axioms sum_mul_log_bscProd
#print axioms held_predictability_budget
#print axioms held_predictability_budget_bits
#print axioms held_predictability_budget_bits_uniform
#print axioms multi_record_bound

end PrepRegressBudget
end OIBridge
