import OIBridge.CausalReadback

/-!
  OIBridge/TransposeBridge.lean — targets of `BARANDES-TRANSPOSE-BRIDGE-PREREGISTRATION.md`.

  Frozen preregistration: commit `951c84604156a92522cc7df26927a14dd435f1ca`, blob
  `4cb6b71832c033f61ac6052c0d2ba11763150d62`, merged to `main` by PR #561.

  Track B act 2, and step 5 of the Amendment 2 sequence.  This module carries the four frozen
  targets: **T1**, the predicate duality in both directions; **T2**, the single-pair factorization
  bridge; **T3**, the family-level restatement with its negation corollary; and **T4**, the
  endpoint lemma.

  WHAT THIS ROUND IS FOR.  Act 1 (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560)
  answered its Q4 with a **prose** transposition, which sits at level 3 of its own frozen evidence
  hierarchy — the hierarchy that rates a Lean equivalence above it at level 2.  This module is the
  upgrade, and it is therefore a **check** on act 1 rather than bookkeeping: had any direction here
  failed, the outcome would have been `RT3` and act 1's Q4 would have taken an appended correction.

  WHAT IT IS NOT.  Nothing here relates `PIndivisibleWithin` to any external predicate.  Act 1
  settled the definition axis at `BD3` — Barandes's *indivisible stochastic process* is a tuple
  class containing Markov chains, not a failure predicate — and that verdict is neither reopened
  nor re-derived.  `PDivisibleCol` is **this programme's own** `PDivisible` written in the opposite
  orientation, and the theorems below say that the two orientations are the same predicate under
  transposition.  That is a fact about matrices.  It is not a correspondence claim, and it sources
  nothing.

  WHAT IS NOT CLOSED HERE.  `PDivisible` bounds its time pairs by a horizon `K`.  The external
  equation act 1 compared against has no such bound, and T4 does not remove the difference: it
  proves only that the *other* recorded difference — that `PDivisible` admits `s = 0` where the
  external range is strict — costs nothing when the family trivializes at the root.  The horizon
  gap is a genuine difference of quantifier domain and is reported as one.

  `IsColStochastic`, `PDivisibleCol` and `PIndivisibleColWithin` are introduced here because no
  column-stochastic predicate exists elsewhere in `OIBridge/`.  They are stated in exactly the form
  the freeze fixes, and control 4 of that freeze forbids reshaping them to fit a proof.
-/

namespace OIBridge
namespace TransposeBridge

open Matrix CausalReadback

section Abstract

variable {V : Type*} [Fintype V]

/-! ### T1 — the predicate duality -/

/-- **COLUMN-STOCHASTIC**: nonnegative entries, every *column* summing to one.

The dual of the merged `IsRowStochastic`, and the orientation the external literature writes its
transition matrices in. -/
def IsColStochastic (M : Matrix V V ℝ) : Prop :=
  (∀ i j, 0 ≤ M i j) ∧ ∀ j, ∑ i, M i j = 1

/-- **T1** — a matrix is row-stochastic exactly when its transpose is column-stochastic.

Stated as an equivalence rather than an implication: a one-way version would leave the bridge
one-way exactly where act 1 claimed the two orientations carry the same content. -/
theorem isRowStochastic_iff_transpose_isColStochastic (M : Matrix V V ℝ) :
    IsRowStochastic M ↔ IsColStochastic Mᵀ := by
  constructor
  · rintro ⟨hnn, hsum⟩
    exact ⟨fun i j => hnn j i, hsum⟩
  · rintro ⟨hnn, hsum⟩
    exact ⟨fun i j => hnn j i, hsum⟩

/-- **T1, dual direction** — a matrix is column-stochastic exactly when its transpose is
row-stochastic.

Both directions are proved because the family-level bridge below consumes one of each: the forward
leg transposes a row-stochastic propagator, the backward leg transposes a column-stochastic one. -/
theorem isColStochastic_iff_transpose_isRowStochastic (M : Matrix V V ℝ) :
    IsColStochastic M ↔ IsRowStochastic Mᵀ := by
  constructor
  · rintro ⟨hnn, hsum⟩
    exact ⟨fun i j => hnn j i, hsum⟩
  · rintro ⟨hnn, hsum⟩
    exact ⟨fun i j => hnn j i, hsum⟩

/-! ### T2 — the single-pair factorization bridge -/

/-- **T2** — act 1's transposition, at one time pair.

The propagator moves from the **right** of a row-stochastic action to the **left** of a
column-stochastic one, and the stochasticity requirement travels with it onto the same factor.  The
orientation hazard the act 1 freeze named — that row-stochastic-on-the-right and
column-stochastic-on-the-left might not be the same content — is discharged here rather than
assumed. -/
theorem factor_transpose_iff (A B Λ : Matrix V V ℝ) :
    (A = B * Λ ∧ IsRowStochastic Λ) ↔ (Aᵀ = Λᵀ * Bᵀ ∧ IsColStochastic Λᵀ) := by
  constructor
  · rintro ⟨hA, hΛ⟩
    refine ⟨?_, (isRowStochastic_iff_transpose_isColStochastic Λ).1 hΛ⟩
    rw [hA, Matrix.transpose_mul]
  · rintro ⟨hA, hΛ⟩
    refine ⟨?_, (isRowStochastic_iff_transpose_isColStochastic Λ).2 hΛ⟩
    have h := congrArg Matrix.transpose hA
    simpa only [Matrix.transpose_transpose, Matrix.transpose_mul] using h

/-! ### T3 — the family-level restatement -/

/-- **P-DIVISIBILITY WITHIN A HORIZON, IN THE OPPOSITE ORIENTATION**.

This mirrors the merged `PDivisible` clause for clause — same quantifier prefix, same horizon
bound, same conjunction order — and differs only where the transposition touches: `IsColStochastic`
in place of `IsRowStochastic`, and the propagator on the **left** of the earlier map rather than the
right. -/
def PDivisibleCol (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∀ s t : ℕ, s < t → t ≤ K →
    ∃ Λ : Matrix V V ℝ, IsColStochastic Λ ∧ Γ t = Λ * Γ s

/-- **P-INDIVISIBILITY IN THE OPPOSITE ORIENTATION**: the negation. -/
def PIndivisibleColWithin (K : ℕ) (Γ : ℕ → Matrix V V ℝ) : Prop := ¬ PDivisibleCol K Γ

/-- **T3** — the two orientations are the same predicate on transposed families.

This is where act 1's transposition stops being a statement about one factorization instance and
becomes a statement about the *predicate*.  Neither side is a claim about any external notion:
`PDivisibleCol` is `PDivisible` written the other way round, and this says so. -/
theorem pDivisible_iff_pDivisibleCol_transpose (K : ℕ) (Γ : ℕ → Matrix V V ℝ) :
    PDivisible K Γ ↔ PDivisibleCol K (fun t => (Γ t)ᵀ) := by
  constructor
  · intro h s t hst htK
    obtain ⟨Λ, hΛ, hEq⟩ := h s t hst htK
    refine ⟨Λᵀ, (isRowStochastic_iff_transpose_isColStochastic Λ).1 hΛ, ?_⟩
    show (Γ t)ᵀ = Λᵀ * (Γ s)ᵀ
    rw [hEq, Matrix.transpose_mul]
  · intro h s t hst htK
    obtain ⟨M, hM, hEq⟩ := h s t hst htK
    refine ⟨Mᵀ, (isColStochastic_iff_transpose_isRowStochastic M).1 hM, ?_⟩
    have hEq' : (Γ t)ᵀ = M * (Γ s)ᵀ := hEq
    have h2 := congrArg Matrix.transpose hEq'
    simpa only [Matrix.transpose_transpose, Matrix.transpose_mul] using h2

/-- **T3, negation corollary** — indivisibility transports with divisibility.

Immediate from the equivalence, and stated separately because `PIndivisibleWithin` is the predicate
the corpus actually reasons with. -/
theorem pIndivisibleWithin_iff_pIndivisibleColWithin_transpose
    (K : ℕ) (Γ : ℕ → Matrix V V ℝ) :
    PIndivisibleWithin K Γ ↔ PIndivisibleColWithin K (fun t => (Γ t)ᵀ) :=
  not_congr (pDivisible_iff_pDivisibleCol_transpose K Γ)

/-! ### T4 — the endpoint marker -/

open scoped Classical in
/-- **T4** — the `s = 0` instances of `PDivisible` cost nothing when the family trivializes at the
root.

Act 1 recorded two differences between `PDivisible` and the external factorization equation: the
horizon bound, and that `PDivisible` admits `s = 0` where the external range of intermediate times
is strict.  It asserted the second difference is vacuous rather than strengthening.  This is that
assertion as a lemma: the witness is the map itself, since `Γ 0` is the identity.

The statement is the frozen one **verbatim**, carrying no `DecidableEq V` hypothesis.  The identity
matrix notation needs decidable equality on `V` to elaborate, and that is supplied by a **scoped
classical instance** rather than by a binder, so the published theorem type has exactly the four
arguments the freeze fixed.  Adding an instance argument would have been a target change under
control 4, and is not made.

The horizon difference is untouched, and no attempt is made here to remove it. -/
theorem root_factor_of_trivial (Γ : ℕ → Matrix V V ℝ) (t : ℕ)
    (h0 : Γ 0 = 1) (ht : IsRowStochastic (Γ t)) :
    ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ Γ t = Γ 0 * Λ :=
  ⟨Γ t, ht, by rw [h0, Matrix.one_mul]⟩

omit [Fintype V] in
/-- **T4 at the merged realization layer** — a rooted realization supplies T4's hypotheses.

`rootedMap R 0` is the identity because the zeroth iterate of the update is, and the rooted maps are
row-stochastic by the merged `rootedMap_isRowStochastic`.  So the endpoint case is discharged for
every family this programme actually produces, not only for families assumed to trivialize. -/
theorem rootedMap_zero {H : Type*} [DecidableEq V] [Fintype H]
    (R : RootedRealization V H) : rootedMap R 0 = 1 := by
  ext a j
  show (∑ h : H, if ((⇑R.step)^[0] (a, h)).1 = j then R.prior h else 0) = _
  by_cases hj : a = j
  · subst hj
    simpa using R.prior_sum
  · simp [hj]

/-- **T4 discharged at a concrete rooted family** — the second addition, and the reason the first
one is worth having.

T4 is stated with the identity matrix elaborated under a **scoped classical** decidable-equality
instance, because the frozen signature carries no `DecidableEq V` binder and adding one would have
been a target change.  `rootedMap`, by contrast, carries the ambient instance.  The two identities
are propositionally equal but not syntactically so, which means "T4's hypotheses hold for every
family this programme produces" does not follow from `rootedMap_zero` by bare instantiation.

Rather than assert the composition, this proves it directly at the realization layer, so the claim
rests on a theorem instead of on an instance-compatibility argument left to the reader. -/
theorem rootedMap_root_factor {H : Type*} [DecidableEq V] [Fintype H]
    (R : RootedRealization V H) (t : ℕ) :
    ∃ Λ : Matrix V V ℝ, IsRowStochastic Λ ∧ rootedMap R t = rootedMap R 0 * Λ :=
  ⟨rootedMap R t, rootedMap_isRowStochastic R t, by rw [rootedMap_zero, Matrix.one_mul]⟩

end Abstract

end TransposeBridge
end OIBridge

#print axioms OIBridge.TransposeBridge.isRowStochastic_iff_transpose_isColStochastic
#print axioms OIBridge.TransposeBridge.isColStochastic_iff_transpose_isRowStochastic
#print axioms OIBridge.TransposeBridge.factor_transpose_iff
#print axioms OIBridge.TransposeBridge.pDivisible_iff_pDivisibleCol_transpose
#print axioms OIBridge.TransposeBridge.pIndivisibleWithin_iff_pIndivisibleColWithin_transpose
#print axioms OIBridge.TransposeBridge.root_factor_of_trivial
#print axioms OIBridge.TransposeBridge.rootedMap_zero
#print axioms OIBridge.TransposeBridge.rootedMap_root_factor
