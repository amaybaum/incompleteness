import OIBridge.ThreadingObservability

/-!
# Act 15 — the `PQ3` (d) cancellation fork on the relative-candidate carrier

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md`, blob
`6428e0acab070ccfd2a84d13c6f55616526206ba`, from `main` at
`e4501bfff4e80533a5440c67d032f1ad401bdbe1` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## What this round is

Act 14 answered the threading question relative to four frozen carriers of observables and adopted
none. Its one undecided target is the **cancellation fork `PQ3` (d)**, asked on the
relative-candidate carrier `𝒪₂`: is there a coherent lift `U`, a constant `W ∈ 𝒢_L` and a strong
family `K` with `𝒪₂(W U_· K_·) = 𝒪₂(U)` while `𝒪₂(W U_·) ≠ 𝒪₂(U)` and `𝒪₂(U_· K_·) ≠ 𝒪₂(U)` — a
pair separated by neither composite half yet identified as a whole. This module takes up that fork
and nothing else.

**Every verdict here is relative to `𝒪₂`**, and act 7's boundary is carried at every use: act 7's
`D4b` came back **negative**, so Source A supplies no general map carrying the relative candidate on
the dilated carrier back to `V`, and the readback is the repository's own convention frozen by act
7's readback amendment. A separation relative to `𝒪₂` is a separation under that convention.

## The three per-triple predicates, in the freeze's letters

For a **triple** `(U, W, K)` — `U` a coherent lift, `W` constant with `LeftFibreGroup W`, `K` a
family with `StrongAnchorStabilizer a₀ (K t)` at every `t` — with composite `U'_t = W · U_t · K_t`:

```
C(U, W, K)  :  𝒪₂(U')      = 𝒪₂(U)
L(U, W, K)  :  𝒪₂(W U_·)   = 𝒪₂(U)
R(U, W, K)  :  𝒪₂(U_· K_·) = 𝒪₂(U)
```

each an equality of the whole two-time family, at every time pair. A triple is **cancelling** iff
`C ∧ ¬L ∧ ¬R`, which is act 14's question written in these letters.

## The seam the freeze holds open, and which branch of it this module reaches

Act 14's `PQ3-d⁻` row carries **two statements that are not logically equivalent**, and the freeze
records them apart:

* **`N`** — no cancelling triple exists: for every triple, `C → (L ∨ R)`. This is the exact negation
  of `PQ3-d⁺`.
* **`S`** — for every triple, `C → (L ∧ R)`. `S` implies `N` by propositional logic alone; `N` does
  not imply `S`, so `S` is strictly the stronger.

**This module reaches neither `N` nor `S`. It refutes both**, by exhibiting a cancelling triple:
`cf5_cancelling_triple_exists` is `PQ3-d⁺`, and `cf5_not_no_cancelling_on_relativeCandidate` records
that `N` fails on this carrier, from which `S` fails a fortiori since `S` implies `N`. **Act 14 is
not edited by this**: its row stands exactly as act 14 wrote it, and the difference between its two
clauses is recorded as a discrepancy of reading in this round's result note, not repaired here.

## What is proved

* `cf1_composite_normal_form` — the composite's relative object is the constant left element's
  conjugation of `U_t K_t K_sᴴ U_sᴴ`, universally, with the readback consequence. **An identity of
  matrices**: it says nothing about the value of any readback and nothing about the fork.
* `cf2_constant_strong_family_redundant` — no cancelling triple has a strong family constant in
  time, through act 11's merged **universal** `gl3_constant_gauge_preserves_relative`.
* `cf3_cardinality_scoping` — `|A| ≥ 2` and `|V| ≥ 2` are necessary, each a conjunct of one theorem.
* `cf4_nontriviality_conjuncts` — in any cancelling triple the strong family moves the relative
  object itself at some time pair, and the constant left element moves the anchored readback of some
  relative object, so `W ≠ 1`.
* `cf5_cancelling_triple_exists` — **the fork, answered positively**: a cancelling triple on
  `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`, with all three conjuncts proved and the two
  inequalities certified at named time pairs and named entries.
* `cf5_not_no_cancelling_on_relativeCandidate` — the consequence for `N`.

## What none of this licenses

`CF2`, `CF3` and `CF4` are **necessary conditions on a witness**; their conjunction is not a further,
stronger statement and in particular is not a non-existence theorem. `GL3` is consumed as act 11
states it and **no converse is claimed**: time-dependence is necessary for the strong part to move
the relative candidate, and is not shown sufficient. `GL2`, `CT4` and `CL1` are consumed at their own
**existential** strengths and none is enlarged. `cf5_cancelling_triple_exists` is a statement about
`𝒪₂` and **travels to no other carrier**: act 14's `PQ3` (b) settles the analogous question
negatively on the anchored-channel carrier `𝒪₁`, the two do not conflict, and no implication between
the carriers is proved in either direction. **No carrier is adopted as the physical one**, and none
is asserted not to be; `P0` is not closed and neither of its two parts is. Nothing here names,
endorses or excludes a selection principle, and nothing here asserts or denies that a connection or
gauge fixing exists or suffices. Nothing here says OI and QM are inequivalent: two lifts differing is
not two theories differing. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`,
`CT1`–`CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(c) and `PQ4` are consumed and none is revised.
Nothing is imported from the substratum Lemma 24.1 rounds, and nothing here is about Track I.

**THE CLAUSE, carried at this mention — the module docstring's statement of what is not licensed.**
`CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
cross-Gram separates every strong-right threading — a question about one datum's separating power.
`PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right gauge can
cancel on the relative-candidate carrier — a question about cancellation between two parts of one
relation. **Neither instantiates, constrains, nor supplies evidence for the other, and no
implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this round
returns, and no outcome of this round moves it in either direction.
-/

namespace OIBridge
namespace CancellationFork

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness AnchorRobustness CoherentLiftGauge
  TwoSidedGauge CrossTimeInvariants ThreadingObservability

open scoped ComplexOrder

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budget slot -/

/-- **THE RELATIVE CANDIDATE AT ONE TIME PAIR** (act 15's budget slot 1) — the `𝒪₂` value:
`𝒪₂(U)(t,s) = readback a₀ (|U_t U_sᴴ|²)`, act 7's frozen readback of the entrywise modulus square
of the relative object `U_t U_sᴴ`.

This is act 14's conditional slot 6, which act 14 left **unused**. This round needs it because every
target states an equality or an inequality of `𝒪₂` values over **all** time pairs, which acts 11, 13
and 14 never had to write.

**Act 7's boundary is carried at every use**: `D4b` is negative, and the readback is the
repository's own convention. **`𝒪₂` is not adopted as the physical carrier here, and is not asserted
not to be.** -/
noncomputable def RelativeCandidate (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    Matrix V V ℝ :=
  readback a₀ (Matrix.of fun p q => ‖(U t * (U s)ᴴ) p q‖ ^ 2)

omit [DecidableEq V] [DecidableEq A] in
theorem relativeCandidate_apply (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) (i j : V) :
    RelativeCandidate a₀ U t s i j = ∑ a : A, ‖(U t * (U s)ᴴ) (i, a) (j, a₀)‖ ^ 2 := rfl

omit [DecidableEq V] [DecidableEq A] in
/-- Equal relative objects at a time pair give equal `𝒪₂` values there. The one-line bridge from a
matrix identity to a readback identity, used wherever a target is settled by an identity of
matrices. **It has no converse here**: nothing below reads an equality of readbacks as an equality
of relative objects. -/
theorem relativeCandidate_congr {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ} {t s : ℕ}
    (h : U' t * (U' s)ᴴ = U t * (U s)ᴴ) :
    RelativeCandidate a₀ U' t s = RelativeCandidate a₀ U t s := by
  unfold RelativeCandidate
  rw [h]

/-! ### Section B — `CF1`: the cancellation equation in normal form -/

/-- **`CF1` — THE COMPOSITE'S RELATIVE OBJECT IS THE CONSTANT LEFT ELEMENT'S CONJUGATION OF
`U_t K_t K_sᴴ U_sᴴ`**, universally, with the readback consequence.

**Bounded reading, as the freeze fixes it.** This is an **identity of matrices**. It says nothing
about the value of the readback, nothing about whether the two sides' readbacks agree, and nothing
about the fork. It is the object over which `CF2`, `CF3`, `CF4` and `CF5` are stated, so that every
later statement is about one written-down thing. Reading it as "so the readbacks agree" does not
follow and is the fork's whole content.

Act 13's merged `ct2a_relative_conj` is the `K ≡ 1` case and is consumed there, not re-proved here.

**The hypotheses are the freeze's and are not load-bearing**: the proof is associativity together
with the conjugate transpose of a product, so the identity holds for arbitrary matrices. They are
carried so that the statement is the one the freeze names, and the reader is told here rather than
left to infer that neither `LeftFibreGroup W` nor strength of `K` enters the proof. -/
theorem cf1_composite_normal_form (a₀ : A) {W : Matrix (V × A) (V × A) ℂ}
    (_hW : LeftFibreGroup W) {U K : ℕ → Matrix (V × A) (V × A) ℂ}
    (_hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (t s : ℕ) :
    (W * U t * K t) * (W * U s * K s)ᴴ
        = W * (U t * K t * (K s)ᴴ * (U s)ᴴ) * Wᴴ
      ∧ RelativeCandidate a₀ (fun t => W * U t * K t) t s
        = readback a₀ (Matrix.of fun p q =>
            ‖(W * (U t * K t * (K s)ᴴ * (U s)ᴴ) * Wᴴ) p q‖ ^ 2) := by
  have key : (W * U t * K t) * (W * U s * K s)ᴴ
      = W * (U t * K t * (K s)ᴴ * (U s)ᴴ) * Wᴴ := by
    rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]
  refine ⟨key, ?_⟩
  unfold RelativeCandidate
  rw [key]

/-! ### Section C — `CF2`: time-dependence of the strong family is necessary -/

/-- **`CF2` — NO CANCELLING TRIPLE HAS A STRONG FAMILY CONSTANT IN TIME.** If `K_t = K_0` at every
`t`, the third conjunct `𝒪₂(U_· K_·) = 𝒪₂(U)` holds, so `C ∧ ¬L ∧ ¬R` cannot.

Act 11's merged **universal** `gl3_constant_gauge_preserves_relative` gives
`(U_t K_0)(U_s K_0)ᴴ = U_t U_sᴴ` for every unitary `K_0` and all `t, s`; the readbacks are then equal
because the matrices are.

**Bounded reading, as the freeze fixes it.** `GL3` **stands as act 11 states it** and is consumed,
not extended. `CF2` says time-dependence is **necessary** for the strong part to move the relative
candidate; it does **not** say time-dependence is sufficient, and act 11's own note refuses that in
terms — neither statement says that *every* time-dependent gauge moves *every* relative candidate.
**This is a necessary condition on a hypothetical witness and is not evidence that one exists.** -/
theorem cf2_constant_strong_family_redundant {a₀ : A} {U K : ℕ → Matrix (V × A) (V × A) ℂ}
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (hconst : ∀ t, K t = K 0)
    (W : Matrix (V × A) (V × A) ℂ) :
    (∀ t s, RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s)
      ∧ ¬ ((∀ t s, RelativeCandidate a₀ (fun t => W * U t * K t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s,
                RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s)) := by
  have hR : ∀ t s, RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s := by
    intro t s
    refine relativeCandidate_congr ?_
    show (U t * K t) * (U s * K s)ᴴ = U t * (U s)ᴴ
    rw [hconst t, hconst s]
    exact gl3_constant_gauge_preserves_relative (hK 0).1 U t s
  exact ⟨hR, fun h => h.2.2 hR⟩

/-! ### Section D — `CF3`: the cardinality scoping of any cancelling triple -/

/-- At `|V| = 1` the relative candidate of every unitary family is the constant `1`: the readback of
a column-stochastic matrix on a one-element visible index set, through act 11's merged
`visible_marginal_eq_one_of_visible_subsingleton` applied to the relative object, which is admissible
for its own readback by act 7's definition of admissibility. -/
theorem relativeCandidate_eq_one_of_visible_subsingleton [Subsingleton V] {a₀ : A}
    {U : ℕ → Matrix (V × A) (V × A) ℂ} (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (t s : ℕ) (i j : V) : RelativeCandidate a₀ U t s i j = 1 := by
  have hunit : (U t * (U s)ᴴ) ∈ Matrix.unitaryGroup (V × A) ℂ :=
    mul_conjTranspose_mem_unitaryGroup (hU t) (hU s)
  exact visible_marginal_eq_one_of_visible_subsingleton
    (G := RelativeCandidate a₀ U t s) ⟨hunit, fun _ _ => rfl⟩ i j

/-- **`CF3` — THE CARDINALITY SCOPING OF ANY CANCELLING TRIPLE**, two conjuncts of one theorem.

**(a) `|A| ≥ 2` is necessary.** When `A` is a subsingleton every strong element is the identity, by
act 11's merged `strong_eq_one_of_ancilla_subsingleton`; so `K` is constant in `t` and `CF2` applies.
**No cancelling triple exists with a single ancilla configuration.**

**(b) `|V| ≥ 2` is necessary.** When `V` is a subsingleton the relative candidate of every lift is
the constant `1` at its single entry, so the second conjunct fails for every `W`. **No cancelling
triple exists with a single visible outcome.**

**Bounded reading, as the freeze fixes it.** `CF3` bounds where a `PQ3-d⁺` witness could live. **It
is not evidence that one exists**, and its two conjuncts are not evidence for each other. -/
theorem cf3_cardinality_scoping {a₀ : A} {U K : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (W : Matrix (V × A) (V × A) ℂ)
    (hW : W ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (Subsingleton A →
        ¬ ((∀ t s,
              RelativeCandidate a₀ (fun t => W * U t * K t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s,
                RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s)))
      ∧ (Subsingleton V →
        ¬ ((∀ t s,
              RelativeCandidate a₀ (fun t => W * U t * K t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s)
            ∧ (¬ ∀ t s,
                RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s))) := by
  constructor
  · intro hA
    have hconst : ∀ t, K t = K 0 := by
      intro t
      rw [strong_eq_one_of_ancilla_subsingleton (hK t),
        strong_eq_one_of_ancilla_subsingleton (hK 0)]
    exact (cf2_constant_strong_family_redundant hK hconst W).2
  · intro hV
    have hWU : ∀ t, (W * U t) ∈ Matrix.unitaryGroup (V × A) ℂ := fun t => mul_mem hW (hU t)
    have hL : ∀ t s,
        RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s := by
      intro t s
      ext i j
      rw [relativeCandidate_eq_one_of_visible_subsingleton hWU t s i j,
        relativeCandidate_eq_one_of_visible_subsingleton hU t s i j]
    exact fun h => h.2.1 hL

/-! ### Section E — `CF4`: the two non-triviality conjuncts -/

/-- **`CF4` — THE TWO NON-TRIVIALITY CONJUNCTS, REDUCED TO STATEMENTS ABOUT THE RELATIVE OBJECTS.**

**(a)** The third conjunct implies that there are times `t, s` with
`U_t K_t K_sᴴ U_sᴴ ≠ U_t U_sᴴ`: any cancelling triple's strong family moves the relative **object**
and not only its readback, at some time pair.

**(b)** The second conjunct implies, through act 13's merged `ct2a_relative_conj`, that there are
times `t, s` with `readback a₀ (|W (U_t U_sᴴ) Wᴴ|²) ≠ readback a₀ (|U_t U_sᴴ|²)`; in particular
`W ≠ 1`.

**Bounded reading, as the freeze fixes it.** Act 11's `GL2` is the merged **existential** statement
that such a strong family exists on one exhibited lift, and act 13's `CT4` with `CL1` the merged
**existential** statement that such a `W` does; **neither is enlarged here**, and neither is cited as
though it quantified over lifts. `CF4` is a pair of **necessary conditions on a hypothetical
witness**. Neither is evidence that a witness exists, and neither is a step toward one. Together with
`CF2` and `CF3` they are the constraints any `PQ3-d⁺` witness must satisfy, written down so that they
are stated rather than reconstructed. **Their conjunction is not a further, stronger statement**, and
in particular it is not a non-existence theorem. -/
theorem cf4_nontriviality_conjuncts {a₀ : A} {U K : ℕ → Matrix (V × A) (V × A) ℂ}
    (W : Matrix (V × A) (V × A) ℂ) :
    ((¬ ∀ t s, RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s)
        → ∃ t s : ℕ, U t * K t * (K s)ᴴ * (U s)ᴴ ≠ U t * (U s)ᴴ)
      ∧ ((¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s)
        → (∃ t s : ℕ,
              readback a₀ (Matrix.of fun p q => ‖(W * (U t * (U s)ᴴ) * Wᴴ) p q‖ ^ 2)
                ≠ readback a₀ (Matrix.of fun p q => ‖(U t * (U s)ᴴ) p q‖ ^ 2))
            ∧ W ≠ 1) := by
  have hconj : ∀ t s : ℕ, RelativeCandidate a₀ (fun t => W * U t) t s
      = readback a₀ (Matrix.of fun p q => ‖(W * (U t * (U s)ᴴ) * Wᴴ) p q‖ ^ 2) := by
    intro t s
    unfold RelativeCandidate
    rw [ct2a_relative_conj (U := U) (U' := fun t => W * U t) (fun _ => rfl) t s]
  constructor
  · intro hR
    by_contra hcon
    push_neg at hcon
    exact hR fun t s => relativeCandidate_congr (by
      show (U t * K t) * (U s * K s)ᴴ = U t * (U s)ᴴ
      simp only [Matrix.conjTranspose_mul, ← Matrix.mul_assoc]
      exact hcon t s)
  · intro hL
    refine ⟨?_, ?_⟩
    · by_contra hcon
      push_neg at hcon
      exact hL fun t s => by rw [hconj t s, hcon t s]; rfl
    · intro hone
      refine hL fun t s => ?_
      rw [hconj t s, hone, Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]
      rfl

/-! ### Section F — `CF5`: the fork, answered by an exhibited cancelling triple -/

/-- The `𝒪₂` value of a pair of permutation dilations, in closed form: the relative object is one
permutation matrix, and act 7's merged `readback_permMatrix_apply` reads its anchored column off.

**Act 7's convention is used and never read off a constructor** (the round's named conjugation
trap): `σ.permMatrix ℂ` carries `1` at `(p, q)` exactly when `σ p = q`, mathlib's
`permMatrix_mul` composes in the order `(σ * τ).permMatrix = τ.permMatrix * σ.permMatrix`, and
`conjTranspose_permMatrix` sends `(σ.permMatrix)ᴴ` to `(σ⁻¹).permMatrix`. Every index below is
computed through this lemma. -/
theorem relativeCandidate_of_permMatrix (a₀ : A) {U : ℕ → Matrix (V × A) (V × A) ℂ}
    {π : ℕ → Equiv.Perm (V × A)} (hU : ∀ t, U t = (π t).permMatrix ℂ) (t s : ℕ) (i j : V) :
    RelativeCandidate a₀ U t s i j
      = if (((π t)⁻¹ * π s) (j, a₀)).1 = i then (1 : ℝ) else 0 := by
  have hprod : U t * (U s)ᴴ = ((π s)⁻¹ * π t).permMatrix ℂ := by
    rw [hU t, hU s, Matrix.conjTranspose_permMatrix, Matrix.permMatrix_mul]
  unfold RelativeCandidate
  rw [hprod, readback_permMatrix_apply, ← Equiv.Perm.inv_def, _root_.mul_inv_rev, inv_inv]

/-- **`CF5` — `PQ3-d⁺`: A CANCELLING TRIPLE EXISTS.**

Relative to the relative-candidate carrier `𝒪₂`, and under act 7's readback convention with `D4b`
negative, the pair of a constant in-fibre left move and a time-dependent strong right gauge **can be
redundancy while neither part is**.

**The triple**, on `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`, with two effective times:

* `W = P(swap((0,0),(0,1)))` — an in-fibre swap inside the visible fibre `0`, which moves the
  anchored basis vector of that fibre; `LeftFibreGroup W` holds because its support lies in one
  fibre.
* `U_0 = 𝟙`, `U_t = P(swap((0,0),(1,1)))` for `t ≠ 0` — a coherent lift of its own readback family.
* `K_0 = 𝟙`, `K_t = P(swap((0,1),(1,2)) · swap((0,2),(1,1)))` for `t ≠ 0` — strong, because its
  support misses both anchored columns `(0,0)` and `(1,0)`.

**The three conjuncts.** `C` holds at **every** time pair: at `(0,0)` and at equal nonzero times both
relative objects are `𝟙`, and at `(1,0)` and `(0,1)` the conjugation by `W` undoes in the anchored
readback exactly what the strong threading does, the anchored columns landing in the visible fibre
`1` on both sides. `¬L` is certified at the time pair `(1,0)` and the entry `(0,0)`, where
`𝒪₂(W U_·)` is `1` and `𝒪₂(U)` is `0`. `¬R` is certified at the time pair `(0,1)` and the entry
`(0,0)`, where `𝒪₂(U_· K_·)` is `1` and `𝒪₂(U)` is `0`.

**The two halves do different work at different time pairs, and that is the content of the
cancellation**: neither half is redundant on its own, and the composite is.

**Bounded reading.** **This is a statement about `𝒪₂` and travels to no other carrier.** Act 14's
`PQ3` (b) settles the analogous question negatively on the anchored-channel carrier `𝒪₁` — the pair
is redundancy for a given lift there **iff** its left part is — and the two do not conflict, `𝒪₁` and
`𝒪₂` being computed from different operations on the lift with no implication proved between them in
either direction. **No carrier is adopted as the physical one**, `P0` stays open and two-part, and
nothing here names, endorses or excludes a selection principle.

**THE CLAUSE, carried at this mention — the statement of the fork's positive answer.**
`CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
cross-Gram separates every strong-right threading — a question about one datum's separating power.
`PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right gauge can
cancel on the relative-candidate carrier — a question about cancellation between two parts of one
relation. **Neither instantiates, constrains, nor supplies evidence for the other, and no
implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this round
returns, and no outcome of this round moves it in either direction. -/
theorem cf5_cancelling_triple_exists :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
      (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
      CoherentLift (0 : Fin 3) Γ U
        ∧ LeftFibreGroup W
        ∧ W ≠ 1
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t))
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ CoherentLift (0 : Fin 3) Γ (fun t => W * U t * K t)
        ∧ ThreadingRelated (0 : Fin 3) U (fun t => W * U t * K t)
        ∧ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
        ∧ RelativeCandidate (0 : Fin 3) (fun t => W * U t) 1 0 0 0 = 1
        ∧ RelativeCandidate (0 : Fin 3) U 1 0 0 0 = 0
        ∧ (¬ ∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
        ∧ RelativeCandidate (0 : Fin 3) (fun t => U t * K t) 0 1 0 0 = 1
        ∧ RelativeCandidate (0 : Fin 3) U 0 1 0 0 = 0
        ∧ (¬ ∀ t s, RelativeCandidate (0 : Fin 3) (fun t => U t * K t) t s
              = RelativeCandidate (0 : Fin 3) U t s) := by
  classical
  obtain ⟨w, hw⟩ : ∃ w : Equiv.Perm (Fin 2 × Fin 3),
      w = Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)) := ⟨_, rfl⟩
  obtain ⟨u, hu⟩ : ∃ u : Equiv.Perm (Fin 2 × Fin 3),
      u = Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((1 : Fin 2), (1 : Fin 3)) := ⟨_, rfl⟩
  obtain ⟨k, hk⟩ : ∃ k : Equiv.Perm (Fin 2 × Fin 3),
      k = Equiv.swap ((0 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3))
        * Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (1 : Fin 3)) := ⟨_, rfl⟩
  obtain ⟨πU, hπU⟩ : ∃ πU : ℕ → Equiv.Perm (Fin 2 × Fin 3),
      πU = fun t => if t = 0 then 1 else u := ⟨_, rfl⟩
  obtain ⟨πK, hπK⟩ : ∃ πK : ℕ → Equiv.Perm (Fin 2 × Fin 3),
      πK = fun t => if t = 0 then 1 else k := ⟨_, rfl⟩
  -- the two effective times, read off once
  have hpair : ∀ t, (πU t = 1 ∧ πK t = 1) ∨ (πU t = u ∧ πK t = k) := by
    intro t; rw [hπU, hπK]; by_cases ht : t = 0 <;> simp [ht]
  have hπU0 : πU 0 = 1 := by rw [hπU]; simp
  have hπK0 : πK 0 = 1 := by rw [hπK]; simp
  have hπU1 : πU 1 = u := by rw [hπU]; norm_num
  have hπK1 : πK 1 = k := by rw [hπK]; norm_num
  -- the constant left element lies in `𝒢_L`: its support is inside one visible fibre
  have hWleft : LeftFibreGroup (w.permMatrix ℂ) := by
    refine ⟨permMatrix_mem_unitaryGroup _, fun p q hpq => ?_⟩
    obtain ⟨x, y⟩ := p
    obtain ⟨c, d⟩ := q
    rw [permMatrix_apply_eq]
    fin_cases x <;> fin_cases y <;> fin_cases c <;> fin_cases d <;>
      simp +decide [hw] at hpq ⊢
  -- the strong family fixes both anchored columns at every time
  have hKfix : ∀ t (p : Fin 2 × Fin 3) (j : Fin 2),
      (πK t).permMatrix ℂ p (j, (0 : Fin 3)) = if p = (j, (0 : Fin 3)) then 1 else 0 := by
    intro t p j
    rcases hpair t with ⟨-, h2⟩ | ⟨-, h2⟩
    · rw [h2, Matrix.permMatrix_one, Matrix.one_apply]
    · rw [h2, permMatrix_apply_eq]
      obtain ⟨x, y⟩ := p
      fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hk]
  have hKstrong : ∀ t, StrongAnchorStabilizer (0 : Fin 3) ((πK t).permMatrix ℂ) :=
    fun t => ⟨permMatrix_mem_unitaryGroup _, hKfix t⟩
  -- the four families, each as a single permutation matrix
  have hWU : ∀ t, w.permMatrix ℂ * (πU t).permMatrix ℂ = (πU t * w).permMatrix ℂ :=
    fun t => (Matrix.permMatrix_mul _ _).symm
  have hUK : ∀ t, (πU t).permMatrix ℂ * (πK t).permMatrix ℂ = (πK t * πU t).permMatrix ℂ :=
    fun t => (Matrix.permMatrix_mul _ _).symm
  have hWUK : ∀ t, w.permMatrix ℂ * (πU t).permMatrix ℂ * (πK t).permMatrix ℂ
      = (πK t * (πU t * w)).permMatrix ℂ := by
    intro t; rw [hWU t, ← Matrix.permMatrix_mul]
  -- the lift is coherent for its own readback family
  have hcohU : ∀ t, AdmissibleDilationAt
      (readback (0 : Fin 3) (Matrix.of fun p q => ‖(πU t).permMatrix ℂ p q‖ ^ 2))
      (0 : Fin 3) ((πU t).permMatrix ℂ) := fun t => ⟨permMatrix_mem_unitaryGroup _, fun _ _ => rfl⟩
  -- `C` — the composite is redundant relative to `𝒪₂`, at EVERY time pair
  have hC : ∀ t s, RelativeCandidate (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) t s
        = RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) t s := by
    intro t s
    ext i j
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
        (U := fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ * (πK t).permMatrix ℂ)
        (π := fun t => πK t * (πU t * w)) hWUK,
      relativeCandidate_of_permMatrix (0 : Fin 3)
        (U := fun t => (πU t).permMatrix ℂ) (π := πU) (fun _ => rfl)]
    rcases hpair t with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases hpair s with ⟨h3, h4⟩ | ⟨h3, h4⟩ <;>
      rw [h1, h2, h3, h4] <;> fin_cases i <;> fin_cases j <;> simp +decide [hw, hu, hk]
  -- the two certified separations
  have hL1 : RelativeCandidate (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) 1 0 0 0 = 1 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) (π := fun t => πU t * w) hWU,
      hπU0, hπU1]
    simp +decide [hw, hu]
  have hU10 : RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 1 0 0 0 = 0 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ) (π := πU) (fun _ => rfl), hπU0, hπU1]
    simp +decide [hu]
  have hR1 : RelativeCandidate (0 : Fin 3)
      (fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) 0 1 0 0 = 1 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ)
      (π := fun t => πK t * πU t) hUK, hπU0, hπU1, hπK0, hπK1]
    simp +decide [hu, hk]
  have hU01 : RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 0 1 0 0 = 0 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ) (π := πU) (fun _ => rfl), hπU0, hπU1]
    simp +decide [hu]
  refine ⟨fun t => readback (0 : Fin 3) (Matrix.of fun p q => ‖(πU t).permMatrix ℂ p q‖ ^ 2),
    fun t => (πU t).permMatrix ℂ, fun t => (πK t).permMatrix ℂ, w.permMatrix ℂ,
    hcohU, hWleft, ?_, hKstrong, ?_, ?_, ?_, hC, hL1, hU10, ?_, hR1, hU01, ?_⟩
  · -- the constant left element is not the identity
    intro hcon
    have h00 := congrFun (congrFun hcon ((0 : Fin 2), (0 : Fin 3))) ((0 : Fin 2), (0 : Fin 3))
    rw [permMatrix_apply_eq, Matrix.one_apply] at h00
    simp +decide [hw] at h00
  · -- the strong family is not constant in time
    refine ⟨0, 1, fun hcon => ?_⟩
    simp only [hπK0, hπK1, Matrix.permMatrix_one] at hcon
    have h := congrFun (congrFun hcon ((0 : Fin 2), (1 : Fin 3))) ((1 : Fin 2), (2 : Fin 3))
    rw [Matrix.one_apply, permMatrix_apply_eq] at h
    simp +decide [hk] at h
  · -- the composite is a coherent lift of the same visible family
    intro t
    show AdmissibleDilationAt _ (0 : Fin 3)
      (w.permMatrix ℂ * (πU t).permMatrix ℂ * (πK t).permMatrix ℂ)
    rw [Matrix.mul_assoc]
    exact left_preserves_admissible hWleft
      (admissible_mul_of_fixes_anchor (hcohU t) (permMatrix_mem_unitaryGroup _) (hKfix t))
  · -- the composite is threading-related to the lift
    exact ⟨w.permMatrix ℂ, hWleft, fun t => (πK t).permMatrix ℂ, hKstrong, fun _ => rfl⟩
  · -- so the constant left part alone is NOT redundant relative to `𝒪₂`
    intro hcon
    have h := congrFun (congrFun (hcon 1 0) 0) 0
    rw [hL1, hU10] at h
    norm_num at h
  · -- so the strong-right part alone is NOT redundant relative to `𝒪₂`
    intro hcon
    have h := congrFun (congrFun (hcon 0 1) 0) 0
    rw [hR1, hU01] at h
    norm_num at h

/-- **THE CONSEQUENCE FOR `N`, AND THROUGH IT FOR `S`.**

The freeze holds act 14's `PQ3-d⁻` row apart into two propositions, `N` — no cancelling triple
exists, `C → (L ∨ R)` at every triple — and `S`, the strictly stronger `C → (L ∧ R)`. **`N` fails on
the relative-candidate carrier**, because `cf5_cancelling_triple_exists` exhibits a triple at which
`C` holds and neither disjunct does.

**`S` implies `N` by propositional logic alone**, so the failure of `N` carries the failure of `S`
with it. **That direction is reported as following, not as separately proved**, and it is recorded
here in the weaker direction the kernel actually establishes: what is proved is that `N` is false,
and `¬S` is its immediate consequence, not an independent result.

**Act 14 is not corrected by this.** Its row stands exactly as act 14 wrote it; the difference
between its two clauses is recorded as a discrepancy of reading in this round's result note, and is
not repaired, reinterpreted or normalized here. **This is a statement about `𝒪₂` and travels to no
other carrier**, act 14's `PQ3` (b) on `𝒪₁` being untouched by it in either direction. -/
theorem cf5_not_no_cancelling_on_relativeCandidate :
    ¬ (∀ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
        (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
        (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
        CoherentLift (0 : Fin 3) Γ U → LeftFibreGroup W →
        (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t)) →
        (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
            = RelativeCandidate (0 : Fin 3) U t s) →
        ((∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
          ∨ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => U t * K t) t s
              = RelativeCandidate (0 : Fin 3) U t s))) := by
  intro hN
  obtain ⟨Γ, U, K, W, hcoh, hW, -, hK, -, -, -, hC, -, -, hnL, -, -, hnR⟩ :=
    cf5_cancelling_triple_exists
  rcases hN Γ U K W hcoh hW hK hC with h | h
  · exact hnL h
  · exact hnR h

end CancellationFork
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.CancellationFork.relativeCandidate_apply
#print axioms OIBridge.CancellationFork.relativeCandidate_congr
#print axioms OIBridge.CancellationFork.cf1_composite_normal_form
#print axioms OIBridge.CancellationFork.cf2_constant_strong_family_redundant
#print axioms OIBridge.CancellationFork.relativeCandidate_eq_one_of_visible_subsingleton
#print axioms OIBridge.CancellationFork.cf3_cardinality_scoping
#print axioms OIBridge.CancellationFork.cf4_nontriviality_conjuncts
#print axioms OIBridge.CancellationFork.relativeCandidate_of_permMatrix
#print axioms OIBridge.CancellationFork.cf5_cancelling_triple_exists
#print axioms OIBridge.CancellationFork.cf5_not_no_cancelling_on_relativeCandidate
