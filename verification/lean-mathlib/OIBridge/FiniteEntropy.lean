/-
  OIBridge/FiniteEntropy.lean — the finite Shannon layer, built because Mathlib has none.

  b448 rank 1 is [Main]'s unavoidable-hidden-predictive-memory theorem, whose clause (c) is a
  CONDITIONAL MUTUAL INFORMATION statement:

      M_t := I(X_<t ; X_{t+1} | X_t)  ≤  I(X_<t ; H_t | X_t)  ≤  log₂ |C_H|.

  Mathlib carries `Real.negMulLog` and the binary entropy function and nothing else: no Shannon
  entropy of a finite distribution, no mutual information, no conditional mutual information, no
  data-processing inequality. Proving a weaker statement — `M_t ≤ log₂ |C_H|` alone, say — would be
  a different theorem wearing the same name, so the layer is built here instead.

  WHAT IS BUILT, and it is deliberately the minimum the theorem needs. Everything is finite,
  real-valued and sum-based; no measure theory enters.

    * `entropy p = Σ negMulLog (p a)` for a distribution on a finite type;
    * relative entropy and its NONNEGATIVITY, which is the single analytic input — everything
      after it is algebra with finite sums;
    * joint entropy, conditional entropy, mutual information, conditional mutual information,
      all as sums over product types;
    * `entropy_le_log_card`, and the data-processing inequality in the form the theorem uses.

  THE ONE ANALYTIC STEP is `log x ≤ x - 1`. Gibbs' inequality follows in three lines and carries
  everything else: nonnegativity of conditional mutual information, and the uniform bound
  `H(p) ≤ log n` (which is Gibbs against the uniform distribution). No convexity, no Jensen, no
  integration.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.SpecialFunctions.Log.NegMulLog
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Prod

namespace OIBridge

namespace FiniteEntropy

open Finset Real

variable {α β γ : Type*} [Fintype α] [Fintype β] [Fintype γ]
variable [DecidableEq α] [DecidableEq β] [DecidableEq γ]

/- Several lemmas below are stated with the section's three type variables in scope but use only
one or two of them. The alternative is to split the section three ways for no gain in content, so
the linter is silenced here rather than the statements contorted -- the same choice, and for the
same reason, as `OIBridge.lean` makes for `Module.Finite`. -/
set_option linter.unusedSectionVars false

/-- A distribution on a finite type: nonnegative and summing to one. -/
structure Dist (α : Type*) [Fintype α] where
  p : α → ℝ
  nonneg : ∀ a, 0 ≤ p a
  total : ∑ a, p a = 1

attribute [simp] Dist.total

/-- Shannon entropy in NATS. The manuscript states clause (c) in bits; converting is division by
`log 2` and is done at the point of use, so no base is baked into the layer. -/
noncomputable def entropy (p : α → ℝ) : ℝ := ∑ a, Real.negMulLog (p a)

/-! ### The one analytic input

`log x ≤ x - 1`, and Gibbs' inequality from it. Everything after this section is algebra. -/

/-- **Gibbs' inequality.** For distributions `p` and `q` with `q` absolutely continuous over `p`,

    Σ p a · log (p a) ≥ Σ p a · log (q a),

i.e. no distribution scores better against `p` than `p` itself. The proof is `log t ≤ t - 1`
applied at `t = q a / p a`, summed. -/
theorem sum_mul_log_le (p q : α → ℝ) (hp : ∀ a, 0 ≤ p a) (hq : ∀ a, 0 ≤ q a)
    (hsum : ∑ a, q a ≤ ∑ a, p a) (hac : ∀ a, 0 < p a → 0 < q a) :
    ∑ a, p a * Real.log (q a) ≤ ∑ a, p a * Real.log (p a) := by
  have key : ∀ a ∈ (univ : Finset α),
      p a * Real.log (q a) - p a * Real.log (p a) ≤ q a - p a := by
    intro a _
    rcases eq_or_lt_of_le (hp a) with h0 | hpos
    · -- `p a = 0` contributes nothing on the left and `q a ≥ 0` on the right
      simp [← h0, hq a]
    · have hqa : 0 < q a := hac a hpos
      have hlog : Real.log (q a / p a) ≤ q a / p a - 1 :=
        Real.log_le_sub_one_of_pos (div_pos hqa hpos)
      have hexp : Real.log (q a / p a) = Real.log (q a) - Real.log (p a) :=
        Real.log_div (ne_of_gt hqa) (ne_of_gt hpos)
      have := mul_le_mul_of_nonneg_left hlog (le_of_lt hpos)
      rw [hexp, mul_sub] at this
      calc p a * Real.log (q a) - p a * Real.log (p a)
          ≤ p a * (q a / p a - 1) := this
        _ = q a - p a := by field_simp
  have hle := Finset.sum_le_sum key
  rw [Finset.sum_sub_distrib, Finset.sum_sub_distrib] at hle
  linarith

/-- **The uniform bound.** Entropy is at most the log of the alphabet size. Gibbs against the
uniform distribution; no separate convexity argument is needed. -/
theorem entropy_le_log_card (p : α → ℝ) (hp : ∀ a, 0 ≤ p a) (htot : ∑ a, p a = 1)
    [Nonempty α] : entropy p ≤ Real.log (Fintype.card α) := by
  have hcard : (0 : ℝ) < Fintype.card α := by
    exact_mod_cast Fintype.card_pos
  set u : α → ℝ := fun _ => (Fintype.card α : ℝ)⁻¹ with hu
  have hun : ∀ a, 0 ≤ u a := fun a => le_of_lt (inv_pos.2 hcard)
  have husum : ∑ a, u a = 1 := by
    rw [hu, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    exact mul_inv_cancel₀ (ne_of_gt hcard)
  have hgibbs := sum_mul_log_le p u hp hun (by rw [husum, htot]) (fun a _ => inv_pos.2 hcard)
  have hlogu : ∀ a, Real.log (u a) = -Real.log (Fintype.card α) := by
    intro a; rw [hu]; simp [Real.log_inv]
  have hleft : ∑ a, p a * Real.log (u a) = -Real.log (Fintype.card α) := by
    have hterm : ∀ a : α, p a * Real.log (u a) = p a * (-Real.log (Fintype.card α)) :=
      fun a => by rw [hlogu a]
    rw [Finset.sum_congr rfl fun a _ => hterm a, ← Finset.sum_mul, htot, one_mul]
  have hent : entropy p = -∑ a, p a * Real.log (p a) := by
    unfold entropy
    rw [← Finset.sum_neg_distrib]
    exact Finset.sum_congr rfl fun a _ => by simp [Real.negMulLog]
  rw [hent]
  rw [hleft] at hgibbs
  linarith

/-! ### Marginals as pushforwards

Every derived distribution below is a pushforward of ONE underlying joint law along a map. That
keeps `H(A,B)`, `H(B)` and the rest from being separate definitions with separate lemmas, and it
makes the "`D` is a function of `(B,C)`" step a statement about injectivity rather than about
information. -/

/-- The pushforward of `w` along `e`: the law of `e` under `w`. -/
noncomputable def marg (w : α → ℝ) (e : α → β) : β → ℝ :=
  fun b => ∑ a ∈ univ.filter (fun a => e a = b), w a

theorem marg_nonneg {w : α → ℝ} (hw : ∀ a, 0 ≤ w a) (e : α → β) : ∀ b, 0 ≤ marg w e b :=
  fun _ => Finset.sum_nonneg fun a _ => hw a

theorem sum_marg (w : α → ℝ) (e : α → β) : ∑ b, marg w e b = ∑ a, w a := by
  classical
  exact Finset.sum_fiberwise_of_maps_to (fun a _ => Finset.mem_univ (e a)) w

/-- Pushing forward twice is pushing forward along the composite. -/
theorem marg_marg (w : α → ℝ) (e : α → β) (f : β → γ) :
    marg (marg w e) f = marg w (f ∘ e) := by
  classical
  funext c
  simp only [marg, Function.comp_apply]
  rw [← Finset.sum_fiberwise_of_maps_to
      (s := univ.filter fun a => f (e a) = c) (t := univ.filter fun b => f b = c)
      (g := e) (fun a ha => by simp_all) w]
  refine Finset.sum_congr rfl fun b hb => Finset.sum_congr ?_ fun _ _ => rfl
  have hfb : f b = c := by simpa using hb
  ext a
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  exact ⟨fun h => ⟨by rw [h]; exact hfb, h⟩, fun h => h.2⟩

/-- **Entropy is a relabelling invariant.** Pushing forward along an injective map changes nothing:
the fibers are singletons, and `negMulLog 0 = 0` kills the rest. This is the lemma that makes "`D`
is a function of `(B, C)`" cost no information. -/
theorem entropy_marg_of_injective {w : α → ℝ} {e : α → β} (he : Function.Injective e) :
    entropy (marg w e) = entropy w := by
  classical
  have hval : ∀ a : α, marg w e (e a) = w a := by
    intro a
    have hfib : univ.filter (fun x => e x = e a) = {a} := by
      ext x; simp [he.eq_iff]
    simp [marg, hfib]
  have hsplit : entropy (marg w e)
      = ∑ b ∈ univ.image e, Real.negMulLog (marg w e b) := by
    refine (Finset.sum_subset (Finset.subset_univ _) ?_).symm
    intro b _ hb
    have hz : marg w e b = 0 := by
      refine Finset.sum_eq_zero fun a ha => ?_
      exact absurd (Finset.mem_image.2 ⟨a, Finset.mem_univ a, (Finset.mem_filter.1 ha).2⟩) hb
    simp [hz, Real.negMulLog]
  rw [hsplit, Finset.sum_image (fun x _ y _ h => he h)]
  exact Finset.sum_congr rfl fun a _ => by rw [hval a]

/-! ### Conditional mutual information

`I(A; C | B)` on a joint law over `α × β × γ`, written in the entropy form so that every identity
below is finite-sum algebra. -/

@[reducible] noncomputable def mAB (w : α × β × γ → ℝ) : α × β → ℝ :=
  marg w (fun s => (s.1, s.2.1))
@[reducible] noncomputable def mCB (w : α × β × γ → ℝ) : γ × β → ℝ :=
  marg w (fun s => (s.2.2, s.2.1))
@[reducible] noncomputable def mB (w : α × β × γ → ℝ) : β → ℝ := marg w (fun s => s.2.1)

/-- `I(A; C | B) = H(A,B) + H(C,B) - H(A,B,C) - H(B)`. -/
noncomputable def cmi3 (w : α × β × γ → ℝ) : ℝ :=
  entropy (mAB w) + entropy (mCB w) - entropy w - entropy (mB w)

/-- Grouping a weighted sum by the fibers of a map: `Σ_a w(a) g(e a) = Σ_b (marg w e)(b) g(b)`.
This one identity replaces the three ad-hoc regroupings the conditional-mutual-information
computation would otherwise need, one per marginal. -/
theorem sum_mul_comp (w : α → ℝ) (e : α → β) (g : β → ℝ) :
    ∑ a, w a * g (e a) = ∑ b, marg w e b * g b := by
  classical
  rw [← Finset.sum_fiberwise_of_maps_to (fun a _ => Finset.mem_univ (e a))
        (fun a => w a * g (e a))]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [marg, Finset.sum_mul]
  refine Finset.sum_congr rfl fun a ha => ?_
  rw [(Finset.mem_filter.1 ha).2]

theorem sum_mul_log_eq_neg_entropy (p : α → ℝ) :
    ∑ a, p a * Real.log (p a) = -entropy p := by
  rw [entropy, ← Finset.sum_neg_distrib]
  exact Finset.sum_congr rfl fun a _ => by simp [Real.negMulLog]

theorem mAB_apply (w : α × β × γ → ℝ) (a : α) (b : β) : mAB w (a, b) = ∑ c, w (a, b, c) := by
  classical
  have hfil : univ.filter (fun s : α × β × γ => (s.1, s.2.1) = (a, b))
      = ({a} : Finset α) ×ˢ (({b} : Finset β) ×ˢ (univ : Finset γ)) := by
    ext s; simp [Finset.mem_filter, Prod.ext_iff, eq_comm]
  rw [mAB, marg, hfil, Finset.sum_product, Finset.sum_singleton, Finset.sum_product,
    Finset.sum_singleton]

theorem mCB_apply (w : α × β × γ → ℝ) (c : γ) (b : β) : mCB w (c, b) = ∑ a, w (a, b, c) := by
  classical
  have hfil : univ.filter (fun s : α × β × γ => (s.2.2, s.2.1) = (c, b))
      = (univ : Finset α) ×ˢ (({b} : Finset β) ×ˢ ({c} : Finset γ)) := by
    ext s; simp [Finset.mem_filter, Prod.ext_iff, eq_comm, and_comm]
  rw [mCB, marg, hfil, Finset.sum_product]
  exact Finset.sum_congr rfl fun a _ => by
    rw [Finset.sum_product, Finset.sum_singleton, Finset.sum_singleton]

theorem mB_apply (w : α × β × γ → ℝ) (b : β) : mB w b = ∑ a, ∑ c, w (a, b, c) := by
  classical
  have hfil : univ.filter (fun s : α × β × γ => s.2.1 = b)
      = (univ : Finset α) ×ˢ (({b} : Finset β) ×ˢ (univ : Finset γ)) := by
    ext s
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_product,
      Finset.mem_singleton]
    tauto
  rw [mB, marg, hfil, Finset.sum_product]
  exact Finset.sum_congr rfl fun a _ => by
    rw [Finset.sum_product, Finset.sum_singleton]

theorem sum_mAB (w : α × β × γ → ℝ) (b : β) : ∑ a, mAB w (a, b) = mB w b := by
  rw [mB_apply]; exact Finset.sum_congr rfl fun a _ => mAB_apply w a b

theorem sum_mCB (w : α × β × γ → ℝ) (b : β) : ∑ c, mCB w (c, b) = mB w b := by
  rw [mB_apply, Finset.sum_comm]
  exact Finset.sum_congr rfl fun c _ => mCB_apply w c b

/-- **Conditional mutual information is nonnegative.** Gibbs' inequality against the
conditionally-independent law `q(a,b,c) = p(a,b) p(c,b) / p(b)`. This is the only place the
analytic input is used a second time, and everything downstream is algebra. -/
theorem cmi3_nonneg (w : α × β × γ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1) :
    0 ≤ cmi3 w := by
  classical
  have hABn : ∀ x : α × β, 0 ≤ mAB w x := fun x => marg_nonneg hw _ x
  have hCBn : ∀ x : γ × β, 0 ≤ mCB w x := fun x => marg_nonneg hw _ x
  have hBn : ∀ b : β, 0 ≤ mB w b := fun b => marg_nonneg hw _ b
  set q : α × β × γ → ℝ :=
    fun s => if mB w s.2.1 = 0 then 0
             else mAB w (s.1, s.2.1) * mCB w (s.2.2, s.2.1) / mB w s.2.1 with hq
  have hqn : ∀ s, 0 ≤ q s := by
    intro s
    by_cases h : mB w s.2.1 = 0
    · simp [hq, h]
    · simp only [hq, if_neg h]
      exact div_nonneg (mul_nonneg (hABn _) (hCBn _)) (hBn _)
  have hqsum : ∑ s, q s = 1 := by
    have hinner : ∀ (a : α) (b : β),
        ∑ c, q (a, b, c) = if mB w b = 0 then (0 : ℝ) else mAB w (a, b) := by
      intro a b
      by_cases h : mB w b = 0
      · simp [hq, h]
      · simp only [hq, if_neg h, div_eq_mul_inv, mul_assoc]
        rw [← Finset.mul_sum, ← Finset.sum_mul, sum_mCB, mul_inv_cancel₀ h, mul_one]
    have houter : ∀ b : β,
        ∑ a, (if mB w b = 0 then (0 : ℝ) else mAB w (a, b)) = mB w b := by
      intro b
      by_cases h : mB w b = 0
      · simp [h]
      · simp only [if_neg h]
        exact sum_mAB w b
    simp only [Fintype.sum_prod_type]
    rw [Finset.sum_comm]
    have hb : ∀ b : β, ∑ a, ∑ c, q (a, b, c) = mB w b := by
      intro b
      rw [Finset.sum_congr rfl fun a _ => hinner a b]
      exact houter b
    rw [Finset.sum_congr rfl fun b _ => hb b, sum_marg]
    exact htot
  have hac : ∀ s, 0 < w s → 0 < q s := by
    intro s hs
    have hAB : 0 < mAB w (s.1, s.2.1) := by
      rw [mAB_apply]
      exact Finset.sum_pos' (fun c _ => hw _) ⟨s.2.2, Finset.mem_univ _, by simpa using hs⟩
    have hCB : 0 < mCB w (s.2.2, s.2.1) := by
      rw [mCB_apply]
      refine Finset.sum_pos' (fun a _ => hw _) ⟨s.1, Finset.mem_univ _, ?_⟩
      simpa using hs
    have hB : 0 < mB w s.2.1 := by
      rw [mB_apply]
      refine Finset.sum_pos' (fun a _ => Finset.sum_nonneg fun c _ => hw _)
        ⟨s.1, Finset.mem_univ _, ?_⟩
      refine Finset.sum_pos' (fun c _ => hw _) ⟨s.2.2, Finset.mem_univ _, ?_⟩
      simpa using hs
    simp only [hq, if_neg (ne_of_gt hB)]
    positivity
  have hgibbs := sum_mul_log_le w q hw hqn (by rw [hqsum, htot]) hac
  -- expand the left-hand side
  have hlog : ∀ s : α × β × γ, w s * Real.log (q s)
      = w s * Real.log (mAB w (s.1, s.2.1)) + w s * Real.log (mCB w (s.2.2, s.2.1))
        - w s * Real.log (mB w s.2.1) := by
    intro s
    rcases eq_or_lt_of_le (hw s) with h0 | hpos
    · simp [← h0]
    · have hB : 0 < mB w s.2.1 := by
        rw [mB_apply]
        refine Finset.sum_pos' (fun a _ => Finset.sum_nonneg fun c _ => hw _)
          ⟨s.1, Finset.mem_univ _, ?_⟩
        exact Finset.sum_pos' (fun c _ => hw _) ⟨s.2.2, Finset.mem_univ _, by simpa using hpos⟩
      have hAB : 0 < mAB w (s.1, s.2.1) := by
        rw [mAB_apply]
        exact Finset.sum_pos' (fun c _ => hw _) ⟨s.2.2, Finset.mem_univ _, by simpa using hpos⟩
      have hCB : 0 < mCB w (s.2.2, s.2.1) := by
        rw [mCB_apply]
        exact Finset.sum_pos' (fun a _ => hw _) ⟨s.1, Finset.mem_univ _, by simpa using hpos⟩
      simp only [hq, if_neg (ne_of_gt hB)]
      rw [Real.log_div (by positivity) (ne_of_gt hB), Real.log_mul (ne_of_gt hAB) (ne_of_gt hCB)]
      ring
  rw [Finset.sum_congr rfl fun s _ => hlog s] at hgibbs
  rw [Finset.sum_sub_distrib, Finset.sum_add_distrib] at hgibbs
  -- and identify each piece with a marginal entropy
  have hA : ∑ s : α × β × γ, w s * Real.log (mAB w (s.1, s.2.1)) = -entropy (mAB w) := by
    rw [sum_mul_comp w (fun s => (s.1, s.2.1)) (fun x => Real.log (mAB w x)),
      sum_mul_log_eq_neg_entropy]
  have hC : ∑ s : α × β × γ, w s * Real.log (mCB w (s.2.2, s.2.1)) = -entropy (mCB w) := by
    rw [sum_mul_comp w (fun s => (s.2.2, s.2.1)) (fun x => Real.log (mCB w x)),
      sum_mul_log_eq_neg_entropy]
  have hBm : ∑ s : α × β × γ, w s * Real.log (mB w s.2.1) = -entropy (mB w) := by
    rw [sum_mul_comp w (fun s => s.2.1) (fun x => Real.log (mB w x)),
      sum_mul_log_eq_neg_entropy]
  rw [hA, hC, hBm, sum_mul_log_eq_neg_entropy] at hgibbs
  rw [cmi3]
  linarith

/-! ### Conditional mutual information of random variables, and data processing

Everything above is stated for a joint law on a product type. Here it is lifted to random
variables on one underlying finite sample space, which is the form the memory theorem needs, and
the data-processing inequality is proved in the shape it uses: the third variable is replaced by a
DETERMINISTIC FUNCTION of the second and third. -/

variable {σ δ : Type*} [Fintype σ] [DecidableEq σ] [Fintype δ] [DecidableEq δ]

/-- `I(A; C | B)` for random variables `a`, `b`, `c` on a finite sample space carrying law `w`. -/
noncomputable def cmi (w : σ → ℝ) (a : σ → α) (b : σ → β) (c : σ → γ) : ℝ :=
  cmi3 (marg w (fun s => (a s, b s, c s)))

/-- Entropy is unchanged by an injective recoding of an already-derived variable. This is the
workhorse of the data-processing proof: adjoining a function of what you already have, reordering
coordinates, and swapping a pair are all instances. -/
theorem entropy_marg_recode (w : σ → ℝ) {τ ρ : Type*} [Fintype τ] [DecidableEq τ]
    [Fintype ρ] [DecidableEq ρ] (e : σ → τ) (k : τ → ρ) (hk : Function.Injective k) :
    entropy (marg w (fun s => k (e s))) = entropy (marg w e) := by
  have h : (fun s => k (e s)) = k ∘ e := rfl
  rw [h, ← marg_marg w e k]
  exact entropy_marg_of_injective hk

theorem cmi_eq (w : σ → ℝ) (a : σ → α) (b : σ → β) (c : σ → γ) :
    cmi w a b c = entropy (marg w (fun s => (a s, b s))) + entropy (marg w (fun s => (c s, b s)))
      - entropy (marg w (fun s => (a s, b s, c s))) - entropy (marg w b) := by
  unfold cmi cmi3 mAB mCB mB
  rw [marg_marg, marg_marg, marg_marg]
  rfl

theorem cmi_nonneg (w : σ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1)
    (a : σ → α) (b : σ → β) (c : σ → γ) : 0 ≤ cmi w a b c :=
  cmi3_nonneg _ (marg_nonneg hw _) (by rw [sum_marg]; exact htot)

/-- **Data processing for a deterministic post-processing.** If `d` is a function of `(b, c)` then
`I(A; d | B) ≤ I(A; C | B)`.

The proof is the classical one and it is exact rather than approximate: the difference of the two
conditional mutual informations IS `I(A; C | B, d)`, which is nonnegative. Adjoining `d` to a
variable that already determines it costs no entropy, which is what turns the difference into a
conditional mutual information rather than merely bounding it. -/
theorem cmi_le_of_deterministic (w : σ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1)
    (a : σ → α) (b : σ → β) (c : σ → γ) (g : β × γ → δ) :
    cmi w a b (fun s => g (b s, c s)) ≤ cmi w a b c := by
  set d : σ → δ := fun s => g (b s, c s) with hd
  set bd : σ → β × δ := fun s => (b s, d s) with hbd
  -- adjoining `d` to `(c, b)` costs nothing
  have h1 : entropy (marg w (fun s => (c s, bd s))) = entropy (marg w (fun s => (c s, b s))) := by
    refine entropy_marg_recode w (fun s => (c s, b s)) (fun p => (p.1, p.2, g (p.2, p.1))) ?_
    intro p p' hpp
    simp only [Prod.mk.injEq] at hpp
    exact Prod.ext hpp.1 hpp.2.1
  -- and adjoining it to `(a, b, c)` costs nothing either, reordering included
  have h2 : entropy (marg w (fun s => (a s, bd s, c s)))
      = entropy (marg w (fun s => (a s, b s, c s))) := by
    refine entropy_marg_recode w (fun s => (a s, b s, c s))
      (fun t => (t.1, (t.2.1, g (t.2.1, t.2.2)), t.2.2)) ?_
    intro t t' htt
    simp only [Prod.mk.injEq] at htt
    exact Prod.ext htt.1 (Prod.ext htt.2.1.1 htt.2.2)
  -- and `H(B, d) = H(d, B)`
  have h3 : entropy (marg w bd) = entropy (marg w (fun s => (d s, b s))) := by
    have hsw := entropy_marg_recode w (fun s => (d s, b s))
      (Prod.swap : δ × β → β × δ) Prod.swap_injective
    simpa [hbd] using hsw
  have hkey : cmi w a bd c = cmi w a b c - cmi w a b d := by
    rw [cmi_eq, cmi_eq, cmi_eq, h1, h2, h3]
    ring
  have := cmi_nonneg w hw htot a bd c
  linarith [hkey ▸ this]

/-- Adding a variable never decreases entropy: `H(Y) ≤ H(X, Y)`. An instance of nonnegative
conditional mutual information, since `I(X; X | Y) = H(X, Y) - H(Y)`. -/
theorem entropy_le_entropy_pair (w : σ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1)
    (x : σ → α) (y : σ → β) :
    entropy (marg w y) ≤ entropy (marg w (fun s => (x s, y s))) := by
  have hrec : entropy (marg w (fun s => (x s, y s, x s)))
      = entropy (marg w (fun s => (x s, y s))) := by
    refine entropy_marg_recode w (fun s => (x s, y s)) (fun p => (p.1, p.2, p.1)) ?_
    intro p p' hpp
    simp only [Prod.mk.injEq] at hpp
    exact Prod.ext hpp.1 hpp.2.1
  have h := cmi_nonneg w hw htot x y x
  rw [cmi_eq, hrec] at h
  linarith

/-- Subadditivity: `H(X, Y) ≤ H(X) + H(Y)`. Nonnegative mutual information, obtained by
conditioning on the trivial variable. -/
theorem entropy_pair_le_add (w : σ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1)
    (x : σ → α) (y : σ → β) :
    entropy (marg w (fun s => (x s, y s))) ≤ entropy (marg w x) + entropy (marg w y) := by
  have hx : entropy (marg w (fun s => (x s, (() : Unit)))) = entropy (marg w x) := by
    refine entropy_marg_recode w x (fun a => (a, (() : Unit))) ?_
    intro a a' h; simpa using congrArg Prod.fst h
  have hy : entropy (marg w (fun s => (y s, (() : Unit)))) = entropy (marg w y) := by
    refine entropy_marg_recode w y (fun b => (b, (() : Unit))) ?_
    intro b b' h; simpa using congrArg Prod.fst h
  have hxy : entropy (marg w (fun s => (x s, (() : Unit), y s)))
      = entropy (marg w (fun s => (x s, y s))) := by
    refine entropy_marg_recode w (fun s => (x s, y s)) (fun p => (p.1, (() : Unit), p.2)) ?_
    intro p p' hpp
    simp only [Prod.mk.injEq] at hpp
    exact Prod.ext hpp.1 hpp.2.2
  have hunit : entropy (marg w (fun _ : σ => (() : Unit))) = 0 := by
    have : marg w (fun _ : σ => (() : Unit)) = fun _ => (1 : ℝ) := by
      funext u
      simpa [marg] using htot
    rw [this, entropy]
    simp [Real.negMulLog]
  have h := cmi_nonneg w hw htot x (fun _ : σ => (() : Unit)) y
  rw [cmi_eq, hx, hy, hxy, hunit] at h
  linarith

/-- **The capacity bound.** `I(A; C | B) ≤ log |γ|`: what one variable can say about another,
however conditioned, is bounded by the log of the alphabet it is read from. -/
theorem cmi_le_log_card (w : σ → ℝ) (hw : ∀ s, 0 ≤ w s) (htot : ∑ s, w s = 1)
    (a : σ → α) (b : σ → β) (c : σ → γ) [Nonempty γ] :
    cmi w a b c ≤ Real.log (Fintype.card γ) := by
  have hgrow : entropy (marg w (fun s => (a s, b s)))
      ≤ entropy (marg w (fun s => (a s, b s, c s))) := by
    have h := entropy_le_entropy_pair w hw htot c (fun s => (a s, b s))
    have hrec : entropy (marg w (fun s => (c s, a s, b s)))
        = entropy (marg w (fun s => (a s, b s, c s))) := by
      refine entropy_marg_recode w (fun s => (a s, b s, c s))
        (fun t => (t.2.2, t.1, t.2.1)) ?_
      intro t t' htt
      simp only [Prod.mk.injEq] at htt
      exact Prod.ext htt.2.1 (Prod.ext htt.2.2 htt.1)
    rw [hrec] at h
    exact h
  have hsub := entropy_pair_le_add w hw htot c b
  have hbound : entropy (marg w c) ≤ Real.log (Fintype.card γ) :=
    entropy_le_log_card (marg w c) (marg_nonneg hw _) (by rw [sum_marg]; exact htot)
  rw [cmi_eq]
  linarith

/-! ### What these proofs rest on

Printed at build time so the kernel's own answer is what the log carries. -/

#print axioms sum_mul_log_le
#print axioms entropy_le_log_card
#print axioms cmi3_nonneg
#print axioms cmi_le_of_deterministic
#print axioms cmi_le_log_card

end FiniteEntropy

end OIBridge
