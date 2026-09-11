import OIBridge.RootedClassification
import OIBridge.RootedClassificationAllTime
import OIBridge.TransposeBridge

/-!
  OIBridge/BarandesTuple.lean — targets of `BARANDES-TUPLE-INSTANTIATION-PREREGISTRATION.md`.

  Frozen preregistration: commit `85a8fdffef31bc0afc76faecd4e4a3f5d3fa8550`, blob
  `2a2216b7791e93303598dafb0d035db18ad9d88a`, merged to `main` by PR #570.

  Track B act 6, and the first Track B round since act 2 to write Lean.  The module carries **two
  logically independent layers**, and the round reports a PAIR of outcomes rather than one label.

  LAYER 1 — TUPLE INSTANTIATION.  `BarandesTuple` is the external stochastic-process interface
  typed from Source C v2 §3 directly: the tuple `(C, T, T₀, Γ, p, 𝒜)` of eq (24) p. 8, with the ten
  axioms X1a–X10 of eqs (25)–(35) and (40)–(41).  `barandesTupleOfPPer` proves that the OI visible
  class instantiates it, under the frozen declarations `C = V`, `T = ℕ`, `T₀ = {0}`,
  `Γ_B(t ← 0) = (Γ t)ᵀ`, `p` CONSTRUCTED from a parameterized `p0`, and `𝒜` the maximal algebra of
  maps `V × ℕ → ℝ`.  Every axiom is proved as its own named result first; the instantiation only
  assembles them.

  WHY THE CLASS AND NOT THE REALIZATION.  Arc B's `C_OI(V) = PPer(V)` makes `PPer` the exact OI
  visible class, so proving instantiation there is stronger than proving it for one realization;
  `rootedRealization_instantiates` is the corollary, through the merged `rootedMap_mem_PPer`.

  WHY `p` IS CONSTRUCTED AND NOT DECLARED.  Source C eq (33) p. 10 FIXES `p` at every later time
  from `p(0)` and `Γ`.  Only `p(0)` is freely adjustable (eq (32)).  So `tupleP` builds the whole
  time-dependent distribution from an arbitrary normalized `p0`, X7 holds by construction, and X8
  is DERIVED from X3 and X6 — which is how Source C itself derives eq (34), from (28) and (32).
  Act 1's Q8 established our datum does not carry `p`; that is unchanged.  What changed is that a
  free normalized vector at every time would not have satisfied the component.

  THE T₀ = {0} VACUITY, IN TWO PARTS.  X9 (eq (35) p. 10) is a REQUIRED axiom — Source C writes
  that `Γ` "will be assumed to satisfy" it — but quantified only over conditioning times
  `t₀, t′ ∈ T₀`, which is why it coexists with act 1's `BD3` and with the source's own p. 11 remark
  that the process "is therefore indivisible for generic target times".  So it is DISCHARGED here
  at `T₀ = {0}` by trivialization (`singletonDivisible_of_pper`), as one of the ten axioms.  And
  `singletonDivisible_independent_of_pdivisible` states, separately, that discharging it bears on
  our all-time `PDivisible` in NEITHER direction: two `PPer` families both satisfy the singleton
  condition, one `PDivisible` and one not.

  LAYER 2 — THE SOURCE-A BRANCH TEST.  `IsUnistochastic` is Source A (30) p. 11, defined FROM
  SCRATCH: existence of a complex unitary whose entrywise norm-squares are the matrix.  It is
  deliberately NOT defined through `QfbData`, `QStar`, `born` or `overlap` — defining it that way
  would build into the predicate the very shortcut Arc D's `RD1` disqualifies.  For the same
  reason no theorem here discharges the branch test from the existence of any representation:
  `overlap_row_sum`/`overlap_col_sum` are about the coherent-lift transport matrix on the shell and
  `QfbData.born` lives on the basis carrier, and no merged theorem identifies either with `(Γ t)ᵀ`.

  `unistochastic_isRowStochastic_and_isColStochastic` is Source A's own p. 11 observation, proved
  here rather than cited, and it is what makes the branch decidable by a stochasticity check rather
  than by reasoning about all unitaries.

  WHAT LAYER 2 DOES NOT SETTLE.  Direct unistochasticity and DILATABILITY are different
  propositions, and nothing here relates them in either direction.  A visible matrix that is not
  unistochastic may still embed in a larger unitary construction by Source A §3.4 p. 10; that is
  act 5's unadjudicated dilated branch and is not adjudicated here.  Conversely the existence of a
  dilation would not show the original matrix unistochastic.  **No result here says the external
  correspondence fails.**

  NOR IS `UB2` A CLASSIFICATION.  `OffDirectBranch` is EXISTENTIAL: it exhibits one lawful member off
  the direct branch, refuting the universal `DirectBranch`.  It does not say every OI family is off
  that branch, and directly unistochastic members may still use the direct branch.  What follows is a
  statement about the FULL-CLASS route — a correspondence covering all of `PPer` cannot stay entirely
  on the direct branch — and nothing stronger.
-/

namespace OIBridge
namespace BarandesTupleRound

open Finset Matrix CausalReadback RootedClassification TransposeBridge

universe u v

/-! ### Layer 1 — the external tuple interface, typed from Source C v2 §3 -/

/-- **THE EXTERNAL STOCHASTIC-PROCESS TUPLE** `(C, T, T₀, Γ, p, 𝒜)`, Source C v2 eq (24), p. 8.

The ten frozen axioms, each a field:

* **X1a** `C` finite — the `Fintype` instance;
* **X1b** `init : T`, the initial time `0` that `T` is assumed to contain (p. 8);
* **X1c** `Cond`, the conditioning times `T₀ ⊂ T`, with `init_cond : Cond init` — `T₀` is "assumed
  to include the initial time 0" (p. 8);
* **X2** `Γ : C² × T × T₀ → [0,1]`, eq (25) p. 8 and eq (27) p. 9, as `Γ_nonneg` and `Γ_le_one`;
* **X3** normalization `∑ i, Γ i j t t₀ = 1`, eq (28) p. 9 — the sum is over the FIRST index;
* **X4** trivialization `Γ i j t₀ t₀ = δ_ij`, eq (29) p. 9;
* **X5** `p : C × T → [0,1]`, eqs (30)–(31) p. 9;
* **X6** initial normalization `∑ j, p j 0 = 1`, eq (32) p. 10;
* **X7** marginalization `p i t = ∑ j, Γ i j t 0 * p j 0`, eq (33) p. 10;
* **X8** all-time normalization `∑ i, p i t = 1`, eq (34) p. 10;
* **X9** divisibility over conditioning times, eq (35) p. 10 — `t₀` and `t′` both range over `T₀`
  only, never over general target times;
* **X10** `𝒜` a commutative algebra whose ELEMENTS are the maps `C × T → ℝ`, taken maximal
  (eqs (40)–(41) and the text, p. 12).  The component is the algebra, not one random variable, and
  it lives over `C × T` rather than over `C` alone.

The conditioning argument is kept in `Γ`'s type deliberately.  Instantiating it at a singleton `T₀`
is a declaration; erasing it would give a weaker tuple than Source C defines. -/
structure BarandesTuple (C : Type u) (T : Type v) [Fintype C] [DecidableEq C] where
  /-- X1b — the initial time, which `T` is assumed to contain. -/
  init : T
  /-- X1c — the conditioning times `T₀ ⊂ T`. -/
  Cond : T → Prop
  /-- X1c — `T₀` contains the initial time. -/
  init_cond : Cond init
  /-- X2 — the transition map, carrying its conditioning-time argument. -/
  Γ : C → C → T → Subtype Cond → ℝ
  /-- X2 — entries are non-negative. -/
  Γ_nonneg : ∀ i j t t₀, 0 ≤ Γ i j t t₀
  /-- X2 — entries are at most one. -/
  Γ_le_one : ∀ i j t t₀, Γ i j t t₀ ≤ 1
  /-- X3 — normalization, summing over the first index. -/
  Γ_sum : ∀ j t t₀, ∑ i, Γ i j t t₀ = 1
  /-- X4 — trivialization at a conditioning time. -/
  Γ_triv : ∀ i j (t₀ : Subtype Cond), Γ i j t₀.1 t₀ = if i = j then 1 else 0
  /-- X5 — the standalone distribution. -/
  p : C → T → ℝ
  /-- X5 — non-negative. -/
  p_nonneg : ∀ i t, 0 ≤ p i t
  /-- X5 — at most one. -/
  p_le_one : ∀ i t, p i t ≤ 1
  /-- X6 — normalized at the initial time. -/
  p_init_sum : ∑ j, p j init = 1
  /-- X7 — the marginalization law, which fixes `p` at every later time. -/
  p_marg : ∀ i t, p i t = ∑ j, Γ i j t ⟨init, init_cond⟩ * p j init
  /-- X8 — normalized at every target time. -/
  p_sum : ∀ t, ∑ i, p i t = 1
  /-- X9 — divisibility, over conditioning times only. -/
  Γ_div : ∀ i j t (t₀ t' : Subtype Cond), Γ i j t t₀ = ∑ k, Γ i k t t' * Γ k j t'.1 t₀
  /-- X10 — the algebra of random variables, over `C × T`. -/
  alg : Subalgebra ℝ (C × T → ℝ)
  /-- X10 — taken maximal. -/
  alg_maximal : alg = ⊤

variable {V : Type} [Fintype V] [DecidableEq V]

/-! #### The declared components, and the axioms one at a time -/

/-- **THE CONSTRUCTED STANDALONE DISTRIBUTION.**  Source C eq (33), p. 10 fixes `p` at every target
time from `p(0)` and `Γ`, so only `p(0)` is free.  This builds the whole time-dependent `p` from an
arbitrary normalized `p0` in the frozen transposed orientation, `Γ_B(t ← 0) = (Γ t)ᵀ`.

`p0` is PARAMETERIZED, never supplied: act 1's Q8 established our datum does not carry it, and
nothing below claims otherwise. -/
noncomputable def tupleP (Γ : ℕ → Matrix V V ℝ) (p0 : V → ℝ) : V → ℕ → ℝ :=
  fun i t => ∑ j, (Γ t)ᵀ i j * p0 j

/-- **X2, lower half** — the transposed family has non-negative entries. -/
theorem transpose_nonneg {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (i j : V) (t : ℕ) :
    0 ≤ (Γ t)ᵀ i j :=
  (hΓ.2.1 t).1 j i

/-- **X2, upper half** — entries are at most one: each is one term of a sum of non-negatives that
equals one. -/
theorem transpose_le_one {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (i j : V) (t : ℕ) :
    (Γ t)ᵀ i j ≤ 1 := by
  have hsum : ∑ k, Γ t j k = 1 := (hΓ.2.1 t).2 j
  have hmem : i ∈ (univ : Finset V) := mem_univ i
  have := Finset.single_le_sum (f := fun k => Γ t j k)
    (fun k _ => (hΓ.2.1 t).1 j k) hmem
  rw [hsum] at this
  exact this

/-- **X3** — normalization in the external orientation: the transposed family is column-stochastic,
which is Source C eq (28)'s sum over the FIRST index.

Act 2's `isRowStochastic_iff_transpose_isColStochastic` is consumed, not re-proved. -/
theorem transpose_isColStochastic {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (t : ℕ) :
    IsColStochastic (Γ t)ᵀ :=
  (isRowStochastic_iff_transpose_isColStochastic (Γ t)).1 (hΓ.2.1 t)

/-- **X4** — trivialization at the conditioning time `0`.  Act 2's `rootedMap_zero` reaches this
class through `PPer`'s own root-identity clause. -/
theorem transpose_zero {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (i j : V) :
    (Γ 0)ᵀ i j = if i = j then 1 else 0 := by
  rw [Matrix.transpose_apply, hΓ.1, Matrix.one_apply]
  by_cases h : i = j
  · simp [h]
  · simp [h, Ne.symm h]

/-- **The constructed `p` returns `p0` at the initial time**, by trivialization — so `p0` really is
the tuple's `p(0)` and X6 is about the parameterized vector. -/
theorem tupleP_zero {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (p0 : V → ℝ) (i : V) :
    tupleP Γ p0 i 0 = p0 i := by
  unfold tupleP
  rw [Finset.sum_congr rfl fun j _ => by rw [transpose_zero hΓ i j]]
  simp

/-- **X5, lower half** — the constructed `p` is non-negative. -/
theorem tupleP_nonneg {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) {p0 : V → ℝ}
    (hp0 : ∀ j, 0 ≤ p0 j) (i : V) (t : ℕ) : 0 ≤ tupleP Γ p0 i t :=
  Finset.sum_nonneg fun j _ => mul_nonneg (transpose_nonneg hΓ i j t) (hp0 j)

/-- **X8** — normalization at every target time, DERIVED from X3 and X6 rather than assumed.  This
is Source C's own derivation of eq (34) from eqs (28) and (32). -/
theorem tupleP_sum {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) {p0 : V → ℝ}
    (hp0sum : ∑ j, p0 j = 1) (t : ℕ) : ∑ i, tupleP Γ p0 i t = 1 := by
  unfold tupleP
  rw [Finset.sum_comm]
  have : ∀ j : V, ∑ i, (Γ t)ᵀ i j * p0 j = p0 j := by
    intro j
    rw [← Finset.sum_mul, (transpose_isColStochastic hΓ t).2 j, one_mul]
  rw [Finset.sum_congr rfl fun j _ => this j]
  exact hp0sum

/-- **X5, upper half** — the constructed `p` is at most one: one term of a sum of non-negatives
that equals one, by X8. -/
theorem tupleP_le_one {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) {p0 : V → ℝ}
    (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) (i : V) (t : ℕ) :
    tupleP Γ p0 i t ≤ 1 := by
  have hsum := tupleP_sum hΓ hp0sum t
  have := Finset.single_le_sum (f := fun k => tupleP Γ p0 k t)
    (fun k _ => tupleP_nonneg hΓ hp0 k t) (mem_univ i)
  rw [hsum] at this
  exact this

/-! #### X9 at `T₀ = {0}`, and what it does not say -/

/-- **THE DIVISIBILITY CONDITION AT A SINGLETON CONDITIONING SET.**  Source C eq (35), p. 10,
specialized to `T₀ = {0}`: both `t₀` and `t′` are forced to `0`, so the condition reads as the one
equation below.

This is the tuple's X9 under the frozen declaration, and NOT our all-time `PDivisible`, which
quantifies over every intermediate target time. -/
def SingletonT0Divisible (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∀ i j t, (Γ t)ᵀ i j = ∑ k, (Γ t)ᵀ i k * (Γ 0)ᵀ k j

/-- **X9 IS DISCHARGED** at `T₀ = {0}`, by trivialization.  One of the ten axioms the instantiation
requires — not skipped. -/
theorem singletonDivisible_of_pper {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) :
    SingletonT0Divisible Γ := by
  intro i j t
  rw [Finset.sum_congr rfl fun k _ => by rw [transpose_zero hΓ k j]]
  simp

/-- **THE TWO-CONFIGURATION WITNESS FAMILY**, built inside a proof rather than as a top-level
definition, per the freeze's witness discipline, and shared by the two results that need it:
layer 1's independence theorem and layer 2's refutation.

`Γ 0 = 1`, period `2`, and at odd times the row-stochastic collapsing slice
`A = ![![1,0],![1,0]]` — every root sent to configuration `0`. -/
theorem collapsing_witness :
    ∃ Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ,
      PPer Γ ∧ Γ 1 = Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0) ∧ Γ 2 = 1 := by
  classical
  have hone : IsRowStochastic (1 : Matrix (Fin 2) (Fin 2) ℝ) := by
    constructor
    · intro i j; rw [Matrix.one_apply]; split <;> norm_num
    · intro i; simp [Matrix.one_apply, Finset.sum_ite_eq]
  have hA : IsRowStochastic
      (Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0) : Matrix (Fin 2) (Fin 2) ℝ) := by
    constructor
    · intro i j
      show (0 : ℝ) ≤ if j = 0 then (1 : ℝ) else 0
      split <;> norm_num
    · intro i
      show (∑ j, if j = 0 then (1 : ℝ) else 0) = 1
      simp
  refine ⟨fun t => if t % 2 = 0 then 1 else Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0),
    ⟨?_, ?_, 2, by norm_num, ?_⟩, ?_, ?_⟩
  · simp
  · intro t
    by_cases h : t % 2 = 0
    · simpa [h] using hone
    · simpa [h] using hA
  · intro t; simp [Nat.add_mod_right]
  · norm_num
  · simp

/-- **DISCHARGING X9 SAYS NOTHING ABOUT ALL-TIME `PDivisible`, IN EITHER DIRECTION.**

Two `PPer` families are exhibited.  Both satisfy `SingletonT0Divisible` — every `PPer` family does,
by the previous theorem — and one is `PDivisible` at its horizon while the other is not.  So the
singleton condition neither establishes divisibility nor refutes it, and no outcome of layer 1 is
evidence about `PDivisible`.

This is stated because the vacuity is easy to mistake for a finding, and in both directions at
once.  Source C's own p. 11 remark, that the process "is therefore indivisible for generic target
times", is the source-side counterpart; it is cited, not extended. -/
theorem singletonDivisible_independent_of_pdivisible :
    (∃ (W : Type) (_ : Fintype W) (_ : DecidableEq W) (Γ : ℕ → Matrix W W ℝ),
        PPer Γ ∧ SingletonT0Divisible Γ ∧ PDivisible 2 Γ) ∧
    (∃ (W : Type) (_ : Fintype W) (_ : DecidableEq W) (Γ : ℕ → Matrix W W ℝ),
        PPer Γ ∧ SingletonT0Divisible Γ ∧ ¬ PDivisible 2 Γ) := by
  constructor
  · -- the constant identity family: `PPer`, and divisible with `Λ = 1`
    refine ⟨Fin 2, inferInstance, inferInstance, fun _ => (1 : Matrix (Fin 2) (Fin 2) ℝ), ?_, ?_, ?_⟩
    · refine ⟨rfl, fun t => ⟨fun i j => ?_, fun i => ?_⟩, 1, one_pos, fun t => rfl⟩
      · by_cases h : i = j <;> simp [Matrix.one_apply, h]
      · simp [Matrix.one_apply]
    · exact singletonDivisible_of_pper ⟨rfl, fun t => ⟨fun i j => by
        by_cases h : i = j <;> simp [Matrix.one_apply, h], fun i => by
        simp [Matrix.one_apply]⟩, 1, one_pos, fun t => rfl⟩
    · intro s t _ _
      exact ⟨1, ⟨fun i j => by by_cases h : i = j <;> simp [Matrix.one_apply, h],
        fun i => by simp [Matrix.one_apply]⟩, by simp⟩
  · -- the collapsing family: `PPer`, and NOT divisible at `s = 1, t = 2`
    obtain ⟨Γ, hpper, h1, h2⟩ := collapsing_witness
    refine ⟨Fin 2, inferInstance, inferInstance, Γ, hpper,
      singletonDivisible_of_pper hpper, ?_⟩
    intro hdiv
    obtain ⟨Λ, _, hfac⟩ := hdiv 1 2 (by norm_num) (by norm_num)
    rw [h2, h1] at hfac
    have e00 := congrFun (congrFun hfac 0) 0
    have e10 := congrFun (congrFun hfac 1) 0
    simp [Matrix.mul_apply] at e00 e10
    linarith

/-- **X6** — Source C eq (32), p. 10.  The constructed `p` is normalized at the initial time.

Its own named result rather than an assembly inside the instantiation: X6 is one of the ten axioms,
and the freeze requires each to be proved separately.  The content is that `tupleP` agrees with `p0`
at time zero, so the hypothesis on `p0` transfers. -/
theorem tupleP_init_sum {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) {p0 : V → ℝ}
    (hp0sum : ∑ j, p0 j = 1) : ∑ j, tupleP Γ p0 j 0 = 1 := by
  rw [Finset.sum_congr rfl fun j _ => tupleP_zero hΓ p0 j]
  exact hp0sum

/-- **X7** — Source C eq (33), p. 10, the marginalization law.

The equation that FIXES `p` at every target time from `p(0)` and `Γ`, stated here about the
construction's OWN time-zero values rather than about `p0` directly: that is the shape the tuple's
field has, and `tupleP_zero` is what identifies the two. -/
theorem tupleP_marg {Γ : ℕ → Matrix V V ℝ} (hΓ : PPer Γ) (p0 : V → ℝ) (i : V) (t : ℕ) :
    tupleP Γ p0 i t = ∑ j, (Γ t)ᵀ i j * tupleP Γ p0 j 0 := by
  rw [Finset.sum_congr rfl fun j _ => by rw [tupleP_zero hΓ p0 j]]
  rfl

/-! #### The instantiation -/

/-- **LAYER 1's TARGET — the OI visible class instantiates the external tuple.**

`PPer Γ` together with a normalized `p0` yields a `BarandesTuple` over `C = V`, `T = ℕ`,
`T₀ = {0}`, with `Γ_B(t ← 0) = (Γ t)ᵀ`, `p` constructed by `tupleP`, and `𝒜 = ⊤` the maximal
algebra of maps `V × ℕ → ℝ`.

Every one of the ten axioms is supplied by its own named result — X2 through X9 above, and
X1a, X1b, X1c and X10 immediately below, which are statements about this construction and so
cannot precede it.  This definition assembles them and proves nothing on its own. -/
noncomputable def barandesTupleOfPPer (Γ : ℕ → Matrix V V ℝ) (hΓ : PPer Γ)
    (p0 : V → ℝ) (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) :
    BarandesTuple V ℕ where
  init := 0
  Cond := fun t => t = 0
  init_cond := rfl
  Γ := fun i j t _ => (Γ t)ᵀ i j
  Γ_nonneg := fun i j t _ => transpose_nonneg hΓ i j t
  Γ_le_one := fun i j t _ => transpose_le_one hΓ i j t
  Γ_sum := fun j t _ => (transpose_isColStochastic hΓ t).2 j
  Γ_triv := fun i j t₀ => by
    have h : t₀.1 = 0 := t₀.2
    rw [h]; exact transpose_zero hΓ i j
  p := tupleP Γ p0
  p_nonneg := fun i t => tupleP_nonneg hΓ hp0 i t
  p_le_one := fun i t => tupleP_le_one hΓ hp0 hp0sum i t
  p_init_sum := tupleP_init_sum hΓ hp0sum
  p_marg := fun i t => tupleP_marg hΓ p0 i t
  p_sum := fun t => tupleP_sum hΓ hp0sum t
  Γ_div := fun i j t t₀ t' => by
    have h' : t'.1 = 0 := t'.2
    rw [h']
    exact singletonDivisible_of_pper hΓ i j t
  alg := ⊤
  alg_maximal := rfl

/-! #### The four declaration-level axioms, each as its own named result

X1a–X1c and X10 are carried by the DECLARATIONS rather than by a computation, which is exactly why
they are stated here rather than left implicit in the assembly above: the freeze requires each of
X1a–X10 to be proved as its own named result, and a component supplied by `rfl` is still a component
that has to be checked against what the source asks for. -/

omit [DecidableEq V] in
/-- **X1a** — Source C v2 §3, p. 8: the configuration space `C` is FINITE.

The declaration is `C := V`, and `V` carries `Fintype` throughout this module. -/
theorem decl_carrier_finite : Set.Finite (Set.univ : Set V) := Set.finite_univ

/-- **X1b** — Source C v2 p. 8: the time set `T` is "assumed to contain" an initial time `0`.

The declaration is `T := ℕ`, and the tuple's initial time is `0` in it. -/
theorem decl_init_eq_zero (Γ : ℕ → Matrix V V ℝ) (hΓ : PPer Γ) (p0 : V → ℝ)
    (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) :
    (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).init = 0 := rfl

/-- **X1c** — Source C v2 p. 8: the conditioning times `T₀ ⊂ T` are "assumed to include the initial
time 0".

BOTH halves are stated, and the first is the one that would otherwise go unrecorded: `T₀` is the
singleton `{0}` exactly, not merely some subset containing `0`.  That is the declaration every later
`T₀`-quantified axiom is discharged at, so pinning it here is what keeps X9's discharge honest. -/
theorem decl_T0_singleton_containing_init (Γ : ℕ → Matrix V V ℝ) (hΓ : PPer Γ) (p0 : V → ℝ)
    (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) :
    (∀ t : ℕ, (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).Cond t ↔ t = 0)
      ∧ (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).Cond
          (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).init :=
  ⟨fun _ => Iff.rfl, rfl⟩

/-- **X10** — Source C v2 eqs (40)–(41) and the text, p. 12: `𝒜` is an algebra whose elements are
the maps `C × T → ℝ`, taken maximal.

The second conjunct is the operative half: EVERY such map is a member, which is what taking the
algebra maximal amounts to.  Stating only `alg = ⊤` would record the declaration without recording
what it gives, and the component the source describes is the algebra rather than any one random
variable. -/
theorem decl_alg_maximal (Γ : ℕ → Matrix V V ℝ) (hΓ : PPer Γ) (p0 : V → ℝ)
    (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) :
    (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).alg = ⊤
      ∧ ∀ f : V × ℕ → ℝ, f ∈ (barandesTupleOfPPer Γ hΓ p0 hp0 hp0sum).alg :=
  ⟨rfl, fun _ => Algebra.mem_top⟩

/-- **THE REALIZATION-LAYER COROLLARY.**  A merged `RootedRealization` instantiates the tuple,
through the merged `rootedMap_mem_PPer`.  Recorded as a corollary because the theorem above is
about the whole visible class, which Arc B identifies with `PPer`. -/
theorem rootedRealization_instantiates {H : Type} [Fintype H]
    (R : RootedRealization V H) (p0 : V → ℝ) (hp0 : ∀ j, 0 ≤ p0 j) (hp0sum : ∑ j, p0 j = 1) :
    ∃ B : BarandesTuple V ℕ, B.Γ = fun i j t _ => (rootedMap R t)ᵀ i j :=
  ⟨barandesTupleOfPPer (rootedMap R) (rootedMap_mem_PPer R) p0 hp0 hp0sum, rfl⟩

/-! ### Layer 2 — the Source-A branch test -/

/-- **UNISTOCHASTIC**, Source A eq (30) p. 11 and the definition in words on the same page: a matrix
whose entries are the modulus-squares of the corresponding entries of a unitary matrix.

Defined FROM SCRATCH.  It is deliberately not phrased through `QfbData`, `QStar`, `QfbData.born` or
the `overlap` construction: routing it through any of those would build into the predicate the
representation shortcut that Arc D's `RD1` disqualifies, and the branch test would then be decided
by the encoding rather than by the matrix under test. -/
def IsUnistochastic (M : Matrix V V ℝ) : Prop :=
  ∃ U : Matrix V V ℂ, U ∈ Matrix.unitaryGroup V ℂ ∧ ∀ i j, M i j = ‖U i j‖ ^ 2

/-- **THE STRUCTURAL LEMMA** — a unistochastic matrix is stochastic in BOTH directions.

Source A's own observation at p. 11, that "every unistochastic transition matrix is doubly
stochastic", proved here rather than cited.  This is what makes the branch test decidable by a
stochasticity check on the matrix itself instead of by reasoning about all unitaries. -/
theorem unistochastic_isRowStochastic_and_isColStochastic {M : Matrix V V ℝ}
    (h : IsUnistochastic M) : IsRowStochastic M ∧ IsColStochastic M := by
  obtain ⟨U, hU, hM⟩ := h
  have hnn : ∀ i j, 0 ≤ M i j := by
    intro i j; rw [hM i j]; positivity
  have hrow : ∀ i, ∑ j, M i j = 1 := by
    intro i
    have h1 := Matrix.mem_unitaryGroup_iff.1 hU
    have hii := congrFun (congrFun h1 i) i
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at hii
    have hterm : ∀ r : V, U i r * (star U) r i = ((‖U i r‖ ^ 2 : ℝ) : ℂ) := by
      intro r
      rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, RCLike.star_def,
        Complex.mul_conj]
      norm_cast
      exact Complex.normSq_eq_norm_sq _
    rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hii
    have : ∑ r, ‖U i r‖ ^ 2 = 1 := by exact_mod_cast hii
    rw [Finset.sum_congr rfl fun j _ => hM i j]
    exact this
  have hcol : ∀ j, ∑ i, M i j = 1 := by
    intro j
    have h1 := Matrix.mem_unitaryGroup_iff'.1 hU
    have hjj := congrFun (congrFun h1 j) j
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at hjj
    have hterm : ∀ r : V, (star U) j r * U r j = ((‖U r j‖ ^ 2 : ℝ) : ℂ) := by
      intro r
      rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm, RCLike.star_def,
        Complex.mul_conj]
      norm_cast
      exact Complex.normSq_eq_norm_sq _
    rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hjj
    have : ∑ r, ‖U r j‖ ^ 2 = 1 := by exact_mod_cast hjj
    rw [Finset.sum_congr rfl fun i _ => hM i j]
    exact this
  exact ⟨⟨hnn, hrow⟩, ⟨hnn, hcol⟩⟩

/-- **THE DIRECT BRANCH** — Source A eq (39) p. 13 presupposes that the visible transition matrix is
unistochastic, in the external transposed orientation.  This is the universal statement for the OI
visible class. -/
def DirectBranch : Prop :=
  ∀ (W : Type) (_ : Fintype W) (_ : DecidableEq W) (Γ : ℕ → Matrix W W ℝ),
    PPer Γ → ∀ t, IsUnistochastic (Γ t)ᵀ

/-- **THE GENUINE COMPLEMENT** — an EXHIBITED lawful OI family off the direct branch.

Not the absence of a proof of `DirectBranch`: a witness is required.  Failure to prove the universal
statement would be `UB3`, not this. -/
def OffDirectBranch : Prop :=
  ∃ (W : Type) (_ : Fintype W) (_ : DecidableEq W) (Γ : ℕ → Matrix W W ℝ),
    PPer Γ ∧ ∃ t, ¬ IsUnistochastic (Γ t)ᵀ

/-- **THE SLICE THAT FAILS**, extracted so the `PPer`-level and realization-level statements of
`UB2` run through ONE computation rather than two.  The matrix is `A = ![![1,0],![1,0]]`, whose
transpose `Aᵀ = ![![1,1],![0,0]]` has COLUMNS each summing to one — so `Aᵀ` IS column-stochastic —
and ROWS summing to `2` and `0`.  The refutation therefore runs through the ROW half of
`unistochastic_isRowStochastic_and_isColStochastic` applied to `Aᵀ`, not the column half:
transposing a row-stochastic matrix makes it column-stochastic, so the failure that survives
transposition into Source A's orientation is the row one. -/
theorem collapsed_slice_not_unistochastic {W : Matrix (Fin 2) (Fin 2) ℝ}
    (hW : W = Matrix.of (fun _ j => if j = 0 then (1 : ℝ) else 0)) : ¬ IsUnistochastic Wᵀ := by
  intro huni
  -- the ROW half is the one that fails on the transpose
  have hrowstoch := (unistochastic_isRowStochastic_and_isColStochastic huni).1
  have hbad : ∑ j, (Wᵀ) 1 j = 0 := by
    rw [hW]
    simp [Matrix.transpose_apply]
  rw [hrowstoch.2 1] at hbad
  norm_num at hbad

/-- **LAYER 2's VERDICT — the OI visible class is NOT contained in Source A's direct unistochastic
branch.**

The witness is on `Fin 2`: the `PPer` family with `Γ 0 = 1`, period `2`, and the row-stochastic
slice `A = ![![1,0],![1,0]]` at odd times.  Its transpose is `Aᵀ = ![![1,1],![0,0]]`, whose COLUMNS
each sum to one — so `Aᵀ` IS column-stochastic — and whose ROWS sum to `2` and `0`.  The refutation
therefore runs through the ROW half of `unistochastic_isRowStochastic_and_isColStochastic` applied
to `Aᵀ`, not the column half: transposing a row-stochastic matrix makes it column-stochastic, so the
failure that survives transposition into Source A's orientation is the row one.

**WHAT THIS DOES NOT SAY.**  It does not say Source A is inapplicable to OI.  Source A §3.4 p. 10
dilates a non-unitary `Θ(t ← 0)` to a unitary one on a larger carrier, so a visible matrix that is
not unistochastic may still embed there.  Nor does it classify the class: the statement is
EXISTENTIAL, so it puts the FULL-CLASS route onto act 5's **unadjudicated dilated branch** — a
correspondence covering all of `PPer` must handle that branch for the members exhibited here — while
directly unistochastic members may still use the direct one.  Whether the dilation choice moves the
induced candidate is not adjudicated here and belongs to a later round with its own freeze. -/
theorem offDirectBranch : OffDirectBranch := by
  classical
  obtain ⟨Γ, hpper, h1, _⟩ := collapsing_witness
  exact ⟨Fin 2, inferInstance, inferInstance, Γ, hpper, 1,
    collapsed_slice_not_unistochastic h1⟩

/-- **`DirectBranch` FAILS**, immediately from the exhibited witness.  Recorded separately so the
universal statement's status is named rather than left implicit. -/
theorem not_directBranch : ¬ DirectBranch := by
  intro h
  obtain ⟨W, hW, hDW, Γ, hpper, t, hnot⟩ := offDirectBranch
  exact hnot (h W hW hDW Γ hpper t)

/-- **THE `UB2` WITNESS IS LAWFUL AT THE REALIZATION LAYER TOO**, and not only as a `PPer` family.

Declared as an ADDITION beyond the two outcome-bearing theorems above rather than folded into them.
The freeze requires a `UB2` witness to be lawful and names this as the route where the realization
layer is wanted, through the merged `pper_has_responseRealization`; that route is taken here so the
witness cannot be read as an abstract matrix family with no OI realization behind it.  Lawfulness of
the prior is carried by `RootedRealization`'s own `prior_nonneg` and `prior_sum` fields, so it is a
consequence of the merged structure rather than an added hypothesis. -/
theorem offDirectBranch_realization :
    ∃ (M : ℕ) (_ : 0 < M) (R : RootedRealization (Fin 2) (ResponseHidden (Fin 2) M)) (t : ℕ),
      ¬ IsUnistochastic (rootedMap R t)ᵀ := by
  classical
  obtain ⟨Γ, hpper, h1, _⟩ := collapsing_witness
  obtain ⟨M, hM, R, hR⟩ := pper_has_responseRealization hpper
  exact ⟨M, hM, R, 1, collapsed_slice_not_unistochastic (by rw [hR]; exact h1)⟩


/-! ### What these proofs rest on

Printed at build time so the kernel's own answer, not a claim in a comment, is what the log carries.
`sorryAx` in any of these lines would mean a hole. -/

#print axioms OIBridge.BarandesTupleRound.transpose_nonneg
#print axioms OIBridge.BarandesTupleRound.transpose_le_one
#print axioms OIBridge.BarandesTupleRound.transpose_isColStochastic
#print axioms OIBridge.BarandesTupleRound.transpose_zero
#print axioms OIBridge.BarandesTupleRound.tupleP_zero
#print axioms OIBridge.BarandesTupleRound.tupleP_nonneg
#print axioms OIBridge.BarandesTupleRound.tupleP_sum
#print axioms OIBridge.BarandesTupleRound.tupleP_le_one
#print axioms OIBridge.BarandesTupleRound.tupleP_init_sum
#print axioms OIBridge.BarandesTupleRound.tupleP_marg
#print axioms OIBridge.BarandesTupleRound.singletonDivisible_of_pper
#print axioms OIBridge.BarandesTupleRound.collapsing_witness
#print axioms OIBridge.BarandesTupleRound.singletonDivisible_independent_of_pdivisible
#print axioms OIBridge.BarandesTupleRound.barandesTupleOfPPer
#print axioms OIBridge.BarandesTupleRound.decl_carrier_finite
#print axioms OIBridge.BarandesTupleRound.decl_init_eq_zero
#print axioms OIBridge.BarandesTupleRound.decl_T0_singleton_containing_init
#print axioms OIBridge.BarandesTupleRound.decl_alg_maximal
#print axioms OIBridge.BarandesTupleRound.rootedRealization_instantiates
#print axioms OIBridge.BarandesTupleRound.unistochastic_isRowStochastic_and_isColStochastic
#print axioms OIBridge.BarandesTupleRound.collapsed_slice_not_unistochastic
#print axioms OIBridge.BarandesTupleRound.offDirectBranch
#print axioms OIBridge.BarandesTupleRound.not_directBranch
#print axioms OIBridge.BarandesTupleRound.offDirectBranch_realization

end BarandesTupleRound
end OIBridge
