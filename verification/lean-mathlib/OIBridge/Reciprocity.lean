/-
  OIBridge/Reciprocity.lean — [SM] Theorem 19 (reciprocity of visible transition counts).

      N_ij = N_{θj, θi}   for all visible i, j, and at every time scale n,

  for a substratum bijection `φ` on `V × H` that is T-invariant, `φ⁻¹ = 𝒯 ∘ φ ∘ 𝒯`, with respect to
  a time reversal that PRESERVES THE PARTITION — `𝒯 = θ × θ_H` acting componentwise — and with the
  counting-measure hidden prior, which is why the statement is about counts and the probability form
  `T_ij = T_{θj,θi}` is division by `|H|`.

  THE SIDE CONDITION IS THE POINT. Detailed balance `N_ij = N_ji` is the θ = id reading and holds
  only when the visible states carry no T-odd data. The manuscript keeps that distinction and so
  does this file: `detailed_balance` is a separate specialization, and the companion probe carries a
  T-invariant substratum with θ a transposition whose visible dynamics is a deterministic 3-cycle —
  `N_02 = |H|` against `N_20 = 0` — so the symmetric form genuinely fails off θ = id while the
  `(θj, θi)` form holds. [GR §3.2]'s precision note is that countercontrol.

  INVOLUTIVITY IS EXPLICIT HERE AND IMPLICIT IN THE MANUSCRIPT. The printed proof passes from
  `φ⁻¹ = 𝒯φ𝒯` to `φ = 𝒯φ⁻¹𝒯` and later cancels `𝒯𝒯`; both steps need `𝒯² = id`, which "the induced
  action of T" supplies physically — classical time reversal squares to the identity — but which no
  clause of the printed statement states. It is not removable: on `ℤ₄` with θ a rotation by one and
  φ the same rotation, `φ⁻¹ = 𝒯φ𝒯` holds and the conclusion is false. The hypotheses `hθV`, `hθH`
  below carry it, and the probe carries that countercontrol.

  `V` is not assumed finite: only the hidden sector is counted over.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Rat.Defs

namespace OIBridge

namespace Reciprocity

set_option autoImplicit false

variable {V H : Type*} [DecidableEq V] [Fintype H]

/-- The partition-preserving time reversal: `θ` on the visible sector, `θ_H` on the hidden. That
`𝒯` has this product form IS the manuscript's "partition preserved by time reversal". -/
def Tm (θ : V → V) (θH : H → H) : V × H → V × H := fun p => (θ p.1, θH p.2)

omit [DecidableEq V] [Fintype H] in
@[simp] theorem Tm_apply (θ : V → V) (θH : H → H) (p : V × H) :
    Tm θ θH p = (θ p.1, θH p.2) := rfl

/-- **The visible transition count** `N_ij`: the number of hidden states carrying `i` to `j`. With
the counting-measure prior, `T_ij = N_ij / |H|`. -/
def N (φ : Equiv.Perm (V × H)) (i j : V) : ℕ :=
  (Finset.univ.filter fun h : H => (φ (i, h)).1 = j).card

variable (φ : Equiv.Perm (V × H)) (θ : V → V) (θH : H → H)

omit [DecidableEq V] [Fintype H] in
/-- `𝒯` is an involution when its two components are. -/
theorem Tm_involutive (hθV : ∀ v, θ (θ v) = v) (hθH : ∀ h, θH (θH h) = h) (p : V × H) :
    Tm θ θH (Tm θ θH p) = p := by
  simp [Tm, hθV, hθH]

omit [DecidableEq V] [Fintype H] in
/-- **The key identity**: T-invariance read forwards. Where `φ` carries `(i, h)` to `(j, h')`, it
carries `(θj, θ_H h')` to `(θi, θ_H h)`. This is the printed proof's displayed computation, and
both involutivity hypotheses are consumed making it. -/
theorem key (hθV : ∀ v, θ (θ v) = v) (hθH : ∀ h, θH (θH h) = h)
    (hT : ∀ p, φ.symm p = Tm θ θH (φ (Tm θ θH p))) (i : V) (h : H) :
    φ (θ (φ (i, h)).1, θH (φ (i, h)).2) = (θ i, θH h) := by
  have h1 := hT (φ (i, h))
  rw [Equiv.symm_apply_apply] at h1
  have h2 := congrArg (Tm θ θH) h1
  rw [Tm_involutive θ θH hθV hθH] at h2
  exact h2.symm.trans rfl

/-- **RECIPROCITY OF THE VISIBLE TRANSITION COUNTS.** The two counting sets are carried onto one
another by `h ↦ θ_H (π_H φ(i, h))` and its mirror, which the proof exhibits as the `card_bij`
data. -/
theorem count_reciprocity (hθV : ∀ v, θ (θ v) = v) (hθH : ∀ h, θH (θH h) = h)
    (hT : ∀ p, φ.symm p = Tm θ θH (φ (Tm θ θH p))) (i j : V) :
    N φ i j = N φ (θ j) (θ i) := by
  refine Finset.card_bij (fun h _ => θH (φ (i, h)).2) ?_ ?_ ?_
  · intro h hh
    have hj : (φ (i, h)).1 = j := (Finset.mem_filter.1 hh).2
    have hk := key φ θ θH hθV hθH hT i h
    rw [hj] at hk
    exact Finset.mem_filter.2 ⟨Finset.mem_univ _, by rw [hk]⟩
  · intro h₁ hh₁ h₂ hh₂ heq
    have hθinj : Function.Injective θH := Function.LeftInverse.injective hθH
    have h2 : (φ (i, h₁)).2 = (φ (i, h₂)).2 := hθinj heq
    have h1 : (φ (i, h₁)).1 = (φ (i, h₂)).1 := by
      rw [(Finset.mem_filter.1 hh₁).2, (Finset.mem_filter.1 hh₂).2]
    have hfull : φ (i, h₁) = φ (i, h₂) := Prod.ext h1 h2
    have := φ.injective hfull
    exact (Prod.ext_iff.1 this).2
  · intro h'' hh''
    have hmem : (φ (θ j, h'')).1 = θ i := (Finset.mem_filter.1 hh'').2
    have hk := key φ θ θH hθV hθH hT (θ j) h''
    rw [hmem, hθV i, hθV j] at hk
    refine ⟨θH (φ (θ j, h'')).2, ?_, ?_⟩
    · exact Finset.mem_filter.2 ⟨Finset.mem_univ _, by rw [hk]⟩
    · rw [hk]
      exact hθH h''

omit [DecidableEq V] [Fintype H] in
/-- **T-invariance propagates to every power**: `(φⁿ)⁻¹ = 𝒯 φⁿ 𝒯`. -/
theorem hT_pow (hθV : ∀ v, θ (θ v) = v) (hθH : ∀ h, θH (θH h) = h)
    (hT : ∀ p, φ.symm p = Tm θ θH (φ (Tm θ θH p))) :
    ∀ (n : ℕ) (p : V × H), (φ ^ n).symm p = Tm θ θH ((φ ^ n) (Tm θ θH p)) := by
  intro n
  induction n with
  | zero =>
    intro p
    rw [pow_zero]
    exact (Tm_involutive θ θH hθV hθH p).symm
  | succ n ih =>
    intro p
    have step : (φ ^ (n + 1)).symm p = φ.symm ((φ ^ n).symm p) := by
      rw [pow_succ]
      rfl
    rw [step, ih p, hT, Tm_involutive θ θH hθV hθH]
    congr 1
    rw [pow_succ']
    rfl

/-- **[SM] THEOREM 19.** Reciprocity at every time scale, in the count form the counting-measure
prior makes exact, together with the probability form `T_ij(n) = T_{θj,θi}(n)` — the same equality
divided by `|H|`. -/
theorem theorem_19 (hθV : ∀ v, θ (θ v) = v) (hθH : ∀ h, θH (θH h) = h)
    (hT : ∀ p, φ.symm p = Tm θ θH (φ (Tm θ θH p))) :
    (∀ (n : ℕ) (i j : V), N (φ ^ n) i j = N (φ ^ n) (θ j) (θ i)) ∧
    (∀ (n : ℕ) (i j : V),
      (N (φ ^ n) i j : ℚ) / (Fintype.card H : ℚ)
        = (N (φ ^ n) (θ j) (θ i) : ℚ) / (Fintype.card H : ℚ)) := by
  have hmain : ∀ (n : ℕ) (i j : V), N (φ ^ n) i j = N (φ ^ n) (θ j) (θ i) := fun n i j =>
    count_reciprocity (φ ^ n) θ θH hθV hθH (hT_pow φ θ θH hθV hθH hT n) i j
  exact ⟨hmain, fun n i j => by rw [hmain n i j]⟩

/-- **The detailed-balance reading**: with no T-odd visible data — `θ = id` — reciprocity is the
symmetric `N_ij = N_ji`, at every time scale. The companion probe's countercontrol shows this
reading is FALSE off `θ = id`, which is the side condition [GR §3.2] insists on. -/
theorem detailed_balance (hθH : ∀ h, θH (θH h) = h)
    (hT : ∀ p, φ.symm p = Tm id θH (φ (Tm id θH p))) (n : ℕ) (i j : V) :
    N (φ ^ n) i j = N (φ ^ n) j i :=
  (theorem_19 φ id θH (fun _ => rfl) hθH hT).1 n i j

/-! ### What these proofs rest on -/

#print axioms Tm_involutive
#print axioms key
#print axioms count_reciprocity
#print axioms hT_pow
#print axioms theorem_19
#print axioms detailed_balance

end Reciprocity

end OIBridge
