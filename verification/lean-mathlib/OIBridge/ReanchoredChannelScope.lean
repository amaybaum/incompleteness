import OIBridge.CancellationFork

/-!
# Act 16 — the cancellation question on the re-anchored-channel carrier `𝒪₃`

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/preregistration.md`,
blob `48099a3b334e8d01f31af706e8738cd49cfca774`, from the merge commit of that control plane,
`d05399020d05d4a7b6f662d2e069062452e7d6b4`, which the freeze fixes as this round's mandated base.

## What this round is

Act 14 froze four carriers of observables and adopted none. Act 15 answered the cancellation fork on
the relative-candidate carrier `𝒪₂` positively. The re-anchored-channel carrier
`𝒪₃(U) = ((t,s) ↦ 𝔇_{a₀}(U_t U_sᴴ))` is the one frozen carrier on which the merged record says
nothing about the pair, and this module asks the cancellation question there and nothing else.

**Every verdict here names its carrier**, and act 7's boundary is carried at every use of `𝒪₂` and
`𝒪₃`: act 7's `D4b` came back **negative**, so Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V`, and the readback is the repository's own
convention frozen by act 7's readback amendment.

## The six per-triple predicates, in the freeze's letters

For a **triple** `(U, W, K)` — `U` a coherent lift, `W` constant with `LeftFibreGroup W`, `K` a
family with `StrongAnchorStabilizer a₀ (K t)` at every `t` — with composite `U'_t = W · U_t · K_t`:

```
C₂ : 𝒪₂(U') = 𝒪₂(U)      L₂ : 𝒪₂(W U_·) = 𝒪₂(U)      R₂ : 𝒪₂(U_· K_·) = 𝒪₂(U)
C₃ : 𝒪₃(U') = 𝒪₃(U)      L₃ : 𝒪₃(W U_·) = 𝒪₃(U)      R₃ : 𝒪₃(U_· K_·) = 𝒪₃(U)
```

each an equality of the whole two-time family, at every time pair. A triple is **`𝒪₃`-cancelling**
iff `C₃ ∧ ¬L₃ ∧ ¬R₃`, which is this round's fork.

## What is proved

* `rn1_reanchored_refines_relative` and `rn1_reanchored_refines_relative_family` — **`RN1`**:
  `𝒪₃`-equality implies `𝒪₂`-equality, universally, through act 14's merged
  `pq0a_readback_is_diagonal_action` at `M = U_t U_sᴴ` and injectivity of the real-to-complex
  coercion. **This is a refinement within the re-anchored row and nothing more.** Its converse is
  **refused** and is used nowhere below; no implication between the one-time row and the re-anchored
  row is asserted in either direction; no strictness is claimed.
* `rn2_nontriviality_transfer` — **`RN2` (a) and (b)**: the two contrapositives of `RN1`, as
  conjuncts of one theorem.
* `rn2c_act15_triple_nontrivial_on_reanchored` — **`RN2` (c)**: act 15's exhibited triple satisfies
  `¬L₃ ∧ ¬R₃`, with `cf5_cancelling_triple_exists` consumed at its own **existential** strength.
* `rn3a_act15_triple_cancels_on_reanchoredChannel` — **`RN3` (a)**, reaching **`RN3-a⁺`**: the
  triple act 15 exhibits — its objects pinned here by the equations act 15's own construction uses —
  satisfies `C₃` at **every** time pair.
* `rn3_plus_cancelling_triple_on_reanchoredChannel` — **`RN3` (b) line 1, `RN3⁺`**: an
  `𝒪₃`-cancelling triple, with all three conjuncts in the kernel, the lift's coherence discharged
  from merged results, and the two inequalities certified at named time pairs and named entries.
* `rn3_not_no_cancelling_on_reanchoredChannel` — the consequence for `N₃`, and through it for `S₃`.
* `rn4_redundancy_does_not_factor_on_relativeCandidate` — **`RN4`**: the non-factorization
  consequence **on `𝒪₂` and on nothing else**.

## What none of this licenses

**No verdict travels between carriers, in any direction.** Act 14's `PQ3` (b) is about `𝒪₁` and is
not evidence about `𝒪₃`, although `𝒪₁` and `𝒪₃` share `𝔇_{a₀}` as their value map — a shared
construction is not a shared verdict, and act 14 records that no implication between the one-time row
and the re-anchored row is proved in either direction. Act 15's `PQ3-d⁺` is about `𝒪₂` and is not
evidence about `𝒪₃`; what travels from `𝒪₂` to `𝒪₃` is exactly the two contrapositives `RN1`
licenses and nothing else. No outcome here is evidence about `𝒪₀`, `𝒪₁` or `𝒪₂`, and `RN4` is a
statement about `𝒪₂` alone.

`RN1` is **not** an equivalence: the converse — concluding `C₃` from `C₂` — is used nowhere, and
`RN3` (a) is decided by computing the channel, never by transporting `C₂`. **`𝒪₃` is not claimed to
be strictly finer than `𝒪₂`**: one implication is proved and no strictness is asserted. `GL2`, `GL3`,
`CT4`, `CL1` and `PQ3-d⁺` are consumed at their own strengths and none is enlarged from existential
to universal. **No carrier is adopted as the physical one**, and none is asserted not to be; the
observational status of `𝒪₂` and `𝒪₃` is each carrier's recorded presupposition, not a finding.
`P0` is not closed and neither of its two parts is; in particular **what selects or constrains the
Gram/orbit trajectory across time is untouched here in either direction**. Nothing names, endorses or
excludes a selection principle, and nothing asserts or denies that a connection or gauge fixing
exists or suffices. Nothing here says OI and QM are inequivalent: two lifts differing is not two
theories differing. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`,
`CT1`–`CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(d), `PQ4` and `CF0`–`CF5` are consumed and none
is revised; act 14's `PQ4` (c) is not corrected and act 14's description of `𝒪₃`'s role is not
repaired. Nothing is imported from the substratum Lemma 24.1 rounds, and nothing here is about
Track I.

**THE CLAUSE, carried at this mention — the module docstring's statement of what is not licensed.**
`CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
separates **every** strong-right threading — a question about one datum's separating power. This
round asks whether a constant in-fibre left move and a time-dependent strong right gauge can cancel
on the re-anchored-channel carrier, so that the pair is redundancy relative to that carrier while
neither part is — a question about cancellation between two parts of one relation, on one named
carrier. **Neither instantiates, constrains, nor supplies evidence for the other, and no implication
transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this round returns, and
no outcome of this round moves it in either direction.
-/

namespace OIBridge
namespace ReanchoredChannelScope

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness AnchorRobustness CoherentLiftGauge
  TwoSidedGauge CrossTimeInvariants ThreadingObservability CancellationFork

open scoped ComplexOrder

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budget slot -/

/-- **THE RE-ANCHORED CHANNEL AT ONE TIME PAIR** (act 16's budget slot 1) — the `𝒪₃` value:
`𝒪₃(U)(t,s) = 𝔇_{a₀}(U_t U_sᴴ)`, act 14's anchored channel applied to the **relative object**
`U_t U_sᴴ` rather than to the per-time lift.

Act 14 defines `AnchoredChannel` and applies it to `U_t`; this round needs the value at a time
**pair**, because every target below states an equality or an inequality of `𝒪₃` values over **all**
time pairs, which act 14 never had to write.

**Act 7's boundary is carried at every use**: `D4b` is negative, and the readback is the
repository's own convention. **`𝒪₃` is not adopted as the physical carrier here, and is not asserted
not to be.** -/
def ReanchoredChannel (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ) :
    Matrix V V ℂ → Matrix V V ℂ :=
  AnchoredChannel a₀ (U t * (U s)ᴴ)

/-- The re-anchored channel in the trace form act 14's `anchoredChannel_eq_trace` supplies: it is a
function of the cross-fibre Gram of the relative object. -/
theorem reanchoredChannel_eq_trace (a₀ : A) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ)
    (ρ : Matrix V V ℂ) (i i' : V) :
    ReanchoredChannel a₀ U t s ρ i i'
      = Matrix.trace (ρ * CrossFibreGram a₀ (U t * (U s)ᴴ) i' i) :=
  anchoredChannel_eq_trace a₀ (U t * (U s)ᴴ) ρ i i'

/-- Equal cross-fibre Grams at every pair of fibres give the same anchored channel. The bridge every
`𝒪₃` computation below goes through, so that no channel value is ever read off a constructor. -/
theorem anchoredChannel_congr_crossFibreGram {a₀ : A} {M N : Matrix (V × A) (V × A) ℂ}
    (h : ∀ i i' : V, CrossFibreGram a₀ M i i' = CrossFibreGram a₀ N i i') :
    AnchoredChannel a₀ M = AnchoredChannel a₀ N := by
  funext ρ
  ext i i'
  rw [anchoredChannel_eq_trace, anchoredChannel_eq_trace, h i' i]

/-! ### Section B — `RN1`: the refinement, within the re-anchored row and in one direction only -/

/-- **`RN1` — `𝒪₃`-EQUALITY IMPLIES `𝒪₂`-EQUALITY, AT ONE TIME PAIR.** If the two lifts' re-anchored
channels agree at `(t, s)`, their relative candidates agree at `(t, s)`.

The whole content is act 14's merged `pq0a_readback_is_diagonal_action` read at `M = U_t U_sᴴ`,
which makes the `𝒪₂` value at `(t, s)` a function of the `𝒪₃` value at `(t, s)`, together with
injectivity of the real-to-complex coercion.

**Bounded reading, as the freeze fixes it.** This is a refinement **within the re-anchored row**.
It says **nothing** about `𝒪₀` and `𝒪₁` and asserts **no** implication between the one-time row and
the re-anchored row in either direction — act 14's record that no such implication is proved stands
untouched. **The converse is refused**: `𝒪₂`-equality does not give `𝒪₃`-equality, nothing here says
it does, and no later statement in this module uses a converse. It is **not** a statement that either
carrier is observable and it adopts neither. **No strictness is claimed**: this round does not prove
that the implication fails to reverse and does not assert that it does. -/
theorem rn1_reanchored_refines_relative (a₀ : A) (U U' : ℕ → Matrix (V × A) (V × A) ℂ) (t s : ℕ)
    (h : ReanchoredChannel a₀ U' t s = ReanchoredChannel a₀ U t s) :
    RelativeCandidate a₀ U' t s = RelativeCandidate a₀ U t s := by
  ext i j
  have hρ := congrFun h
    (Matrix.of fun p q : V => if p = j then (if q = j then (1 : ℂ) else 0) else 0)
  have hij := congrFun (congrFun hρ i) i
  have key : ((RelativeCandidate a₀ U' t s i j : ℝ) : ℂ)
      = ((RelativeCandidate a₀ U t s i j : ℝ) : ℂ) := by
    show ((readback a₀ (Matrix.of fun p q => ‖(U' t * (U' s)ᴴ) p q‖ ^ 2) i j : ℝ) : ℂ)
      = ((readback a₀ (Matrix.of fun p q => ‖(U t * (U s)ᴴ) p q‖ ^ 2) i j : ℝ) : ℂ)
    rw [pq0a_readback_is_diagonal_action, pq0a_readback_is_diagonal_action]
    exact hij
  exact_mod_cast key

/-- **`RN1`, THE WHOLE-FAMILY FORM** — `𝒪₃(U') = 𝒪₃(U)` implies `𝒪₂(U') = 𝒪₂(U)`, both read at
**every** time pair. The form every later target consumes.

**Bounded reading:** as at `rn1_reanchored_refines_relative`. The converse is refused; no
implication between the one-time row and the re-anchored row is asserted; no strictness is claimed;
neither carrier is adopted. -/
theorem rn1_reanchored_refines_relative_family (a₀ : A) (U U' : ℕ → Matrix (V × A) (V × A) ℂ)
    (h : ∀ t s, ReanchoredChannel a₀ U' t s = ReanchoredChannel a₀ U t s) :
    ∀ t s, RelativeCandidate a₀ U' t s = RelativeCandidate a₀ U t s :=
  fun t s => rn1_reanchored_refines_relative a₀ U U' t s (h t s)

/-! ### Section C — `RN2`: the two non-triviality conjuncts on `𝒪₃`, by contraposition -/

/-- **`RN2` (a) AND (b) — THE TWO CONTRAPOSITIVES, AS CONJUNCTS OF ONE THEOREM.**

**(a)** If the constant left part alone moves `𝒪₂`, it moves `𝒪₃`: `¬L₂ → ¬L₃`.

**(b)** If the strong-right part alone moves `𝒪₂`, it moves `𝒪₃`: `¬R₂ → ¬R₃`.

Each is `RN1`'s whole-family form contraposed, at the pair `(U, W U_·)` and at the pair
`(U, U_· K_·)` respectively.

**Bounded reading, as the freeze fixes it.** These supply **two** of the three conjuncts of the `𝒪₃`
fork and **not** the third. Neither is evidence that `C₃` holds on any triple — that is `RN3` and is
settled there. Neither is evidence that an `𝒪₃`-cancelling triple exists: a triple satisfying two of
three conjuncts is not a witness. **Act 15's `PQ3-d⁺` is not carried from `𝒪₂` to `𝒪₃` by this**;
what travels is exactly the two contrapositives `RN1` licenses. `GL2`, `CT4` and `CL1` are **not**
enlarged from existential to universal by anything here. -/
theorem rn2_nontriviality_transfer {a₀ : A} {U K : ℕ → Matrix (V × A) (V × A) ℂ}
    (W : Matrix (V × A) (V × A) ℂ) :
    ((¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s)
        → ¬ ∀ t s, ReanchoredChannel a₀ (fun t => W * U t) t s = ReanchoredChannel a₀ U t s)
      ∧ ((¬ ∀ t s, RelativeCandidate a₀ (fun t => U t * K t) t s = RelativeCandidate a₀ U t s)
        → ¬ ∀ t s, ReanchoredChannel a₀ (fun t => U t * K t) t s
              = ReanchoredChannel a₀ U t s) :=
  ⟨fun hL2 hL3 => hL2 (rn1_reanchored_refines_relative_family a₀ U (fun t => W * U t) hL3),
   fun hR2 hR3 => hR2 (rn1_reanchored_refines_relative_family a₀ U (fun t => U t * K t) hR3)⟩

/-- **`RN2` (c) — ACT 15's EXHIBITED TRIPLE SATISFIES `¬L₃ ∧ ¬R₃`.**

Act 15's merged `cf5_cancelling_triple_exists` is consumed at its own **existential** strength: its
statement carries the two `𝒪₂` inequalities as explicit conjuncts, and (a) and (b) are applied to
them. The triple's `𝒪₂` content — `C₂` included — is act 15's and is restated here unchanged.

**Bounded reading, as the freeze fixes it.** This supplies two of the three conjuncts of the `𝒪₃`
fork and **not** the third. It is **not** evidence that `C₃` holds on this triple or on any triple,
and it is **not** evidence that an `𝒪₃`-cancelling triple exists. **Act 15's `PQ3-d⁺` is a verdict
on `𝒪₂` and stands exactly as act 15 states it**; it is not weakened, qualified, revised or
enlarged, and it is not carried to `𝒪₃`. -/
theorem rn2c_act15_triple_nontrivial_on_reanchored :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
      (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
      CoherentLift (0 : Fin 3) Γ U
        ∧ LeftFibreGroup W
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t))
        ∧ ThreadingRelated (0 : Fin 3) U (fun t => W * U t * K t)
        ∧ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
        ∧ (¬ ∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t) t s
              = ReanchoredChannel (0 : Fin 3) U t s)
        ∧ (¬ ∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => U t * K t) t s
              = ReanchoredChannel (0 : Fin 3) U t s) := by
  obtain ⟨Γ, U, K, W, hcoh, hW, -, hK, -, -, hthread, hC2, -, -, hnL2, -, -, hnR2⟩ :=
    cf5_cancelling_triple_exists
  exact ⟨Γ, U, K, W, hcoh, hW, hK, hthread, hC2,
    (rn2_nontriviality_transfer (a₀ := (0 : Fin 3)) (U := U) (K := K) W).1 hnL2,
    (rn2_nontriviality_transfer (a₀ := (0 : Fin 3)) (U := U) (K := K) W).2 hnR2⟩

/-! ### Section D — the `𝒪₃` value of a permutation dilation, computed and never read off -/

/-- The relative object of a permutation family is one permutation matrix. Act 15's computation,
isolated so that both the `𝒪₂` and the `𝒪₃` statements below run through the same identity.

**Act 7's convention is used and never read off a constructor** (the round's named conjugation
trap): `σ.permMatrix ℂ` carries `1` at `(p, q)` exactly when `σ p = q`, mathlib's `permMatrix_mul`
composes in the order `(σ * τ).permMatrix = τ.permMatrix * σ.permMatrix`, and
`conjTranspose_permMatrix` sends `(σ.permMatrix)ᴴ` to `(σ⁻¹).permMatrix`. -/
theorem relativeObject_permMatrix {ϖ : ℕ → Equiv.Perm (V × A)}
    {U : ℕ → Matrix (V × A) (V × A) ℂ} (hU : ∀ t, U t = (ϖ t).permMatrix ℂ) (t s : ℕ) :
    U t * (U s)ᴴ = ((ϖ s)⁻¹ * ϖ t).permMatrix ℂ := by
  rw [hU t, hU s, Matrix.conjTranspose_permMatrix, Matrix.permMatrix_mul]

/-- **THE CROSS-FIBRE GRAM OF A PERMUTATION MATRIX, IN CLOSED FORM** — the number of ancilla
configurations `a` at which the permutation sends both `(i, a)` and `(i', a)` into the anchored
column set, landing on `(j, a₀)` and `(k, a₀)` respectively.

Unlike the readback, this does **not** collapse to a single fibre test: the off-diagonal pairs
`i ≠ i'` are live, and they are exactly what `𝒪₃` reads and `𝒪₂` does not. Every `𝒪₃` value below is
computed through this lemma. -/
theorem crossFibreGram_permMatrix (a₀ : A) (σ : Equiv.Perm (V × A)) (i i' j k : V) :
    CrossFibreGram a₀ (σ.permMatrix ℂ) i i' j k
      = ∑ a : A, (if ((j, a₀) : V × A) = σ (i, a) then (1 : ℂ) else 0)
          * (if ((k, a₀) : V × A) = σ (i', a) then (1 : ℂ) else 0) := by
  rw [crossFibreGram_apply]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [permMatrix_apply_eq, permMatrix_apply_eq]
  split_ifs <;> simp

/-! ### Section E — `RN3` (a): the decision about act 15's exhibited triple on `𝒪₃` -/

/-- **`RN3` (a), REACHING `RN3-a⁺` — ACT 15's EXHIBITED TRIPLE SATISFIES `C₃` AT EVERY TIME PAIR.**

The objects are **pinned by the equations in the statement**, which are act 15's own: `W` the
in-fibre swap `P(swap((0,0),(0,1)))`; `U` the identity at time `0` and `P(swap((0,0),(1,1)))`
afterwards; `K` the identity at time `0` and
`P(swap((0,1),(1,2)) · swap((0,2),(1,1)))` afterwards, on `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`.
No lift, gauge element, witness, matrix, triple, entry value or pair is a top-level definition here.

**The computation, and why it is not an accident of the readback.** At `(0,0)` and at any pair of
equal-behaviour times both relative objects are the identity. At `(1,0)` the composite's relative
object is `w⁻¹ k u w` and the lift's is `u`; their anchored columns are **different** — the
preimages of the anchored column set are `(1,2)` and `(1,0)` for the composite against `(1,1)` and
`(1,0)` for the lift — yet every cross-fibre Gram entry agrees, both being supported on the fibre
pair `(1,1)` with the value `1` at `(0,0)` and at `(1,1)`. The pair `(0,1)` is the inverse of
`(1,0)` and agrees for the same reason. Since the anchored channel is a function of the cross-fibre
Gram (`anchoredChannel_eq_trace`), the two channels coincide as functions of the input state.

**Bounded reading, as the freeze fixes it.** `C₃` is computed here; it is **not** transported from
`C₂`. Using `RN1`'s converse — concluding `C₃` from `C₂` — would make this true by fiat and is the
error this target exists to decide; no step of this proof does it. **This is a statement about `𝒪₃`
and travels to no other carrier**, and it carries act 7's boundary — `D4b` negative, the readback
the repository's own. **Act 15's `PQ3-d⁺` on `𝒪₂` stands exactly as act 15 states it** and is not
weakened, qualified, revised or enlarged by this. -/
theorem rn3a_act15_triple_cancels_on_reanchoredChannel
    {w u k : Equiv.Perm (Fin 2 × Fin 3)}
    (hw : w = Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)))
    (hu : u = Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((1 : Fin 2), (1 : Fin 3)))
    (hk : k = Equiv.swap ((0 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3))
              * Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (1 : Fin 3)))
    {πU πK : ℕ → Equiv.Perm (Fin 2 × Fin 3)}
    (hπU : ∀ t, πU t = if t = 0 then 1 else u) (hπK : ∀ t, πK t = if t = 0 then 1 else k)
    {U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ}
    {W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ}
    (hU : ∀ t, U t = (πU t).permMatrix ℂ) (hK : ∀ t, K t = (πK t).permMatrix ℂ)
    (hW : W = w.permMatrix ℂ) :
    ∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t * K t) t s
        = ReanchoredChannel (0 : Fin 3) U t s := by
  have hpair : ∀ t, (πU t = 1 ∧ πK t = 1) ∨ (πU t = u ∧ πK t = k) := by
    intro t
    rw [hπU t, hπK t]
    by_cases ht : t = 0 <;> simp [ht]
  have hcomp : ∀ t, W * U t * K t = (πK t * (πU t * w)).permMatrix ℂ := by
    intro t
    rw [hW, hU t, hK t, Matrix.permMatrix_mul, Matrix.permMatrix_mul]
  intro t s
  show AnchoredChannel (0 : Fin 3) ((fun t => W * U t * K t) t * ((fun t => W * U t * K t) s)ᴴ)
      = AnchoredChannel (0 : Fin 3) (U t * (U s)ᴴ)
  rw [relativeObject_permMatrix (U := fun t => W * U t * K t) hcomp t s,
    relativeObject_permMatrix (U := U) hU t s]
  refine anchoredChannel_congr_crossFibreGram fun i i' => ?_
  ext j c
  rw [crossFibreGram_permMatrix, crossFibreGram_permMatrix]
  simp only [Fin.sum_univ_three]
  rcases hpair t with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> rcases hpair s with ⟨h3, h4⟩ | ⟨h3, h4⟩ <;>
    rw [h1, h2, h3, h4] <;> fin_cases i <;> fin_cases i' <;> fin_cases j <;> fin_cases c <;>
      simp +decide [hw, hu, hk]

/-! ### Section F — `RN3` (b): the fork on `𝒪₃`, reaching line 1 -/

/-- **`RN3` (b), LINE 1 — `RN3⁺`: AN `𝒪₃`-CANCELLING TRIPLE EXISTS.**

Relative to the re-anchored-channel carrier `𝒪₃`, and under act 7's readback convention with `D4b`
negative, the pair of a constant in-fibre left move and a time-dependent strong right gauge **can be
redundancy while neither part is**.

**The triple** is the one act 15 exhibits, on `V = Fin 2`, `A = Fin 3`, anchor `a₀ = 0`, with two
effective times, its objects pinned by the equations act 15's own construction uses.

**The three conjuncts, and how each is earned.**

* `C₃` at every time pair is `rn3a_act15_triple_cancels_on_reanchoredChannel` — **`RN3-a⁺`**,
  computed in the kernel from the cross-fibre Gram of each relative object.
* `¬L₃` and `¬R₃` are `RN2` (a) and (b) — the two contrapositives of `RN1` — applied to the
  triple's own `𝒪₂` separations, which are act 15's certified ones: `𝒪₂(W U_·)` is `1` where
  `𝒪₂(U)` is `0` at the time pair `(1, 0)` and the entry `(0, 0)`, and `𝒪₂(U_· K_·)` is `1` where
  `𝒪₂(U)` is `0` at the time pair `(0, 1)` and the entry `(0, 0)`.
* The **two inequalities are additionally certified on `𝒪₃` itself**, at named time pairs and named
  entries: at the time pair `(1, 0)`, on the input state `E_{00}` and at the output entry `(0, 0)`,
  `𝒪₃(W U_·)` is `1` while `𝒪₃(U)` is `0`; at the time pair `(0, 1)`, on the same input state and
  the same output entry, `𝒪₃(U_· K_·)` is `1` while `𝒪₃(U)` is `0`.
* The lift's coherence, and the composite's, are discharged from merged results — act 7's
  `admissible_mul_of_fixes_anchor` and act 12's `left_preserves_admissible`.

`C₂` is recorded as a conjunct and is obtained **from `C₃` through `RN1`**, in the one direction
`RN1` runs; the converse is not used here or anywhere below.

**Bounded reading, as the freeze fixes it.** **This is a statement about `𝒪₃` and travels to no
other carrier.** Act 14's `PQ3` (b) settles the analogous question negatively on the
anchored-channel carrier `𝒪₁` and the two do not conflict — `𝒪₁` applies `𝔇_{a₀}` to `U_t` and `𝒪₃`
applies it to `U_t U_sᴴ`, and act 14 records that no implication between the one-time row and the
re-anchored row is proved in either direction. Act 15's `PQ3-d⁺` on `𝒪₂` is a separate verdict on a
separate carrier and stands exactly as act 15 states it. **No carrier is adopted as the physical
one**, `P0` stays OPEN and two-part, and nothing here names, endorses or excludes a selection
principle. -/
theorem rn3_plus_cancelling_triple_on_reanchoredChannel :
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
        ∧ (∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t * K t) t s
              = ReanchoredChannel (0 : Fin 3) U t s)
        ∧ ReanchoredChannel (0 : Fin 3) (fun t => W * U t) 1 0
              (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)
              0 0 = 1
        ∧ ReanchoredChannel (0 : Fin 3) U 1 0
              (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)
              0 0 = 0
        ∧ (¬ ∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t) t s
              = ReanchoredChannel (0 : Fin 3) U t s)
        ∧ ReanchoredChannel (0 : Fin 3) (fun t => U t * K t) 0 1
              (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)
              0 0 = 1
        ∧ ReanchoredChannel (0 : Fin 3) U 0 1
              (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)
              0 0 = 0
        ∧ (¬ ∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => U t * K t) t s
              = ReanchoredChannel (0 : Fin 3) U t s)
        ∧ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
        ∧ (¬ ∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t) t s
              = RelativeCandidate (0 : Fin 3) U t s)
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
  have hcohU : ∀ t, AdmissibleDilationAt
      (readback (0 : Fin 3) (Matrix.of fun p q => ‖(πU t).permMatrix ℂ p q‖ ^ 2))
      (0 : Fin 3) ((πU t).permMatrix ℂ) := fun t => ⟨permMatrix_mem_unitaryGroup _, fun _ _ => rfl⟩
  -- `C₃` — the composite is redundant relative to `𝒪₃`, at EVERY time pair (`RN3-a⁺`)
  have hC3 : ∀ t s, ReanchoredChannel (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) t s
        = ReanchoredChannel (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) t s :=
    rn3a_act15_triple_cancels_on_reanchoredChannel hw hu hk (fun t => by rw [hπU])
      (fun t => by rw [hπK]) (fun _ => rfl) (fun _ => rfl) (W := w.permMatrix ℂ) rfl
  -- the two `𝒪₂` separations, act 15's own, certified at named time pairs and named entries
  have hL1 : RelativeCandidate (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) 1 0 0 0 = 1 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) (π := fun t => πU t * w)
      (fun t => (Matrix.permMatrix_mul _ _).symm), hπU0, hπU1]
    simp +decide [hw, hu]
  have hU10 : RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 1 0 0 0 = 0 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ) (π := πU) (fun _ => rfl), hπU0, hπU1]
    simp +decide [hu]
  have hR1 : RelativeCandidate (0 : Fin 3)
      (fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) 0 1 0 0 = 1 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) (π := fun t => πK t * πU t)
      (fun t => (Matrix.permMatrix_mul _ _).symm), hπU0, hπU1, hπK0, hπK1]
    simp +decide [hu, hk]
  have hU01 : RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 0 1 0 0 = 0 := by
    rw [relativeCandidate_of_permMatrix (0 : Fin 3)
      (U := fun t => (πU t).permMatrix ℂ) (π := πU) (fun _ => rfl), hπU0, hπU1]
    simp +decide [hu]
  have hnL2 : ¬ ∀ t s, RelativeCandidate (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) t s
        = RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) t s := by
    intro hcon
    have h := congrFun (congrFun (hcon 1 0) 0) 0
    rw [hL1, hU10] at h
    norm_num at h
  have hnR2 : ¬ ∀ t s, RelativeCandidate (0 : Fin 3)
      (fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) t s
        = RelativeCandidate (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) t s := by
    intro hcon
    have h := congrFun (congrFun (hcon 0 1) 0) 0
    rw [hR1, hU01] at h
    norm_num at h
  -- the named `𝒪₃` entry certificates, computed through the cross-fibre Gram
  have hchan : ∀ (ϖ : ℕ → Equiv.Perm (Fin 2 × Fin 3))
      (M : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ), (∀ t, M t = (ϖ t).permMatrix ℂ) →
      ∀ t s, ReanchoredChannel (0 : Fin 3) M t s
          (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0) 0 0
        = CrossFibreGram (0 : Fin 3) (((ϖ s)⁻¹ * ϖ t).permMatrix ℂ) 0 0 0 0 := by
    intro ϖ M hM t s
    have hobj : ReanchoredChannel (0 : Fin 3) M t s
        = AnchoredChannel (0 : Fin 3) (((ϖ s)⁻¹ * ϖ t).permMatrix ℂ) := by
      show AnchoredChannel (0 : Fin 3) (M t * (M s)ᴴ) = _
      rw [relativeObject_permMatrix hM t s]
    rw [hobj]
    exact anchoredChannel_unit (0 : Fin 3) _ 0 0 0 0
  have hL3e : ReanchoredChannel (0 : Fin 3)
      (fun t => w.permMatrix ℂ * (πU t).permMatrix ℂ) 1 0
        (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0) 0 0
      = 1 := by
    rw [hchan (fun t => πU t * w) _ (fun t => (Matrix.permMatrix_mul _ _).symm) 1 0,
      crossFibreGram_permMatrix, hπU0, hπU1]
    simp +decide [hw, hu, Fin.sum_univ_three]
  have hU3e : ReanchoredChannel (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 1 0
        (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0) 0 0
      = 0 := by
    rw [hchan πU _ (fun _ => rfl) 1 0, crossFibreGram_permMatrix, hπU0, hπU1]
    simp +decide [hu, Fin.sum_univ_three]
  have hR3e : ReanchoredChannel (0 : Fin 3)
      (fun t => (πU t).permMatrix ℂ * (πK t).permMatrix ℂ) 0 1
        (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0) 0 0
      = 1 := by
    rw [hchan (fun t => πK t * πU t) _ (fun t => (Matrix.permMatrix_mul _ _).symm) 0 1,
      crossFibreGram_permMatrix, hπU0, hπU1, hπK0, hπK1]
    simp +decide [hu, hk, Fin.sum_univ_three]
  have hU3e' : ReanchoredChannel (0 : Fin 3) (fun t => (πU t).permMatrix ℂ) 0 1
        (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0) 0 0
      = 0 := by
    rw [hchan πU _ (fun _ => rfl) 0 1, crossFibreGram_permMatrix, hπU0, hπU1]
    simp +decide [hu, Fin.sum_univ_three]
  refine ⟨fun t => readback (0 : Fin 3) (Matrix.of fun p q => ‖(πU t).permMatrix ℂ p q‖ ^ 2),
    fun t => (πU t).permMatrix ℂ, fun t => (πK t).permMatrix ℂ, w.permMatrix ℂ,
    hcohU, hWleft, ?_, hKstrong, ?_, ?_, ?_, hC3, hL3e, hU3e,
    ?_, hR3e, hU3e', ?_,
    rn1_reanchored_refines_relative_family (0 : Fin 3) _ _ hC3, hnL2, hnR2⟩
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
  · -- so the constant left part alone is NOT redundant relative to `𝒪₃`
    intro hcon
    have h := congrFun (congrFun (congrFun (hcon 1 0)
      (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)) 0) 0
    rw [hL3e, hU3e] at h
    norm_num at h
  · -- so the strong-right part alone is NOT redundant relative to `𝒪₃`
    intro hcon
    have h := congrFun (congrFun (congrFun (hcon 0 1)
      (Matrix.of fun p q : Fin 2 => if p = 0 then (if q = 0 then (1 : ℂ) else 0) else 0)) 0) 0
    rw [hR3e, hU3e'] at h
    norm_num at h

/-- **THE CONSEQUENCE FOR `N₃`, AND THROUGH IT FOR `S₃`.**

The freeze holds the two universal propositions on `𝒪₃` apart: `N₃` — no `𝒪₃`-cancelling triple
exists, `C₃ → (L₃ ∨ R₃)` at every triple — and `S₃`, the strictly stronger `C₃ → (L₃ ∧ R₃)`. **`N₃`
fails on the re-anchored-channel carrier**, because `rn3_plus_cancelling_triple_on_reanchoredChannel`
exhibits a triple at which `C₃` holds and neither disjunct does.

**`S₃` implies `N₃` by propositional logic alone**, so the failure of `N₃` carries the failure of
`S₃` with it. **That direction is reported as following, not as separately proved.**

**This is a statement about `𝒪₃` and travels to no other carrier.** Act 14's `PQ3` (b) on `𝒪₁` is
untouched by it in either direction, and act 15's `PQ3-d⁺` on `𝒪₂` stands exactly as act 15 states
it. **No carrier is adopted as the physical one.** -/
theorem rn3_not_no_cancelling_on_reanchoredChannel :
    ¬ (∀ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
        (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
        (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
        CoherentLift (0 : Fin 3) Γ U → LeftFibreGroup W →
        (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t)) →
        (∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t * K t) t s
            = ReanchoredChannel (0 : Fin 3) U t s) →
        ((∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => W * U t) t s
              = ReanchoredChannel (0 : Fin 3) U t s)
          ∨ (∀ t s, ReanchoredChannel (0 : Fin 3) (fun t => U t * K t) t s
              = ReanchoredChannel (0 : Fin 3) U t s))) := by
  intro hN
  obtain ⟨Γ, U, K, W, hcoh, hW, -, hK, -, -, -, hC3, -, -, hnL3, -, -, hnR3, -, -, -⟩ :=
    rn3_plus_cancelling_triple_on_reanchoredChannel
  rcases hN Γ U K W hcoh hW hK hC3 with h | h
  · exact hnL3 h
  · exact hnR3 h

/-! ### Section G — `RN4`: non-factorization on `𝒪₂`, and on nothing else -/

/-- **`RN4` — RELATIVE TO `𝒪₂`, THE REDUNDANCY SUBRELATION OF `≈_T` DOES NOT FACTOR AS THE PRODUCT
OF THE TWO PARTS' REDUNDANCY SUBRELATIONS.**

Two conjuncts. The first is act 15's exhibition, consumed at its own **existential** strength: there
is a triple with `C₂ ∧ ¬L₂ ∧ ¬R₂`. The second is the consequence: the universal statement that a
composite redundant relative to `𝒪₂` has both halves redundant relative to `𝒪₂` is **false**, so
knowing each part's `𝒪₂`-redundancy class does not determine the composite's — both parts are
`𝒪₂`-separating while the composite is `𝒪₂`-redundant. **No new witness is constructed.**

**Bounded reading, as the freeze fixes it.** **This is a statement about `𝒪₂` and travels to no
other carrier**: it says nothing about `𝒪₀`, `𝒪₁` or `𝒪₃`, and it is **not** evidence about `RN3`.
It carries act 7's boundary — `D4b` negative, the readback the repository's own. **It does not say a
selector is required**, on any carrier, and it names, endorses and excludes no selection principle,
no connection and no gauge fixing, in either direction. **It does not correct act 14's `PQ4` (c)**:
that statement's word is "together", which is the conjunctive reading, and the conjunctive reading is
untouched here; what is refuted is the factoring reading, on `𝒪₂`, and the two readings are recorded
apart in this round's result note. **It is not a claim about which choices a physical selector would
face**, because no carrier is adopted as the physical one. **It adds nothing to act 15**: the
existential content is act 15's, and this states the consequence act 15's exhibition carries for the
factoring reading and nothing further. -/
theorem rn4_redundancy_does_not_factor_on_relativeCandidate :
    (∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
        (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
        (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
        CoherentLift (0 : Fin 3) Γ U ∧ LeftFibreGroup W
          ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t))
          ∧ ThreadingRelated (0 : Fin 3) U (fun t => W * U t * K t)
          ∧ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
                = RelativeCandidate (0 : Fin 3) U t s)
          ∧ (¬ ∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t) t s
                = RelativeCandidate (0 : Fin 3) U t s)
          ∧ (¬ ∀ t s, RelativeCandidate (0 : Fin 3) (fun t => U t * K t) t s
                = RelativeCandidate (0 : Fin 3) U t s))
      ∧ ¬ (∀ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
            (U K : ℕ → Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ)
            (W : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ),
            CoherentLift (0 : Fin 3) Γ U → LeftFibreGroup W →
            (∀ t, StrongAnchorStabilizer (0 : Fin 3) (K t)) →
            (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t * K t) t s
                = RelativeCandidate (0 : Fin 3) U t s) →
            ((∀ t s, RelativeCandidate (0 : Fin 3) (fun t => W * U t) t s
                  = RelativeCandidate (0 : Fin 3) U t s)
              ∧ (∀ t s, RelativeCandidate (0 : Fin 3) (fun t => U t * K t) t s
                  = RelativeCandidate (0 : Fin 3) U t s))) := by
  obtain ⟨Γ, U, K, W, hcoh, hW, -, hK, -, -, hthread, hC2, -, -, hnL2, -, -, hnR2⟩ :=
    cf5_cancelling_triple_exists
  exact ⟨⟨Γ, U, K, W, hcoh, hW, hK, hthread, hC2, hnL2, hnR2⟩,
    fun hS => hnL2 (hS Γ U K W hcoh hW hK hC2).1⟩

end ReanchoredChannelScope
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.ReanchoredChannelScope.reanchoredChannel_eq_trace
#print axioms OIBridge.ReanchoredChannelScope.anchoredChannel_congr_crossFibreGram
#print axioms OIBridge.ReanchoredChannelScope.rn1_reanchored_refines_relative
#print axioms OIBridge.ReanchoredChannelScope.rn1_reanchored_refines_relative_family
#print axioms OIBridge.ReanchoredChannelScope.rn2_nontriviality_transfer
#print axioms OIBridge.ReanchoredChannelScope.rn2c_act15_triple_nontrivial_on_reanchored
#print axioms OIBridge.ReanchoredChannelScope.relativeObject_permMatrix
#print axioms OIBridge.ReanchoredChannelScope.crossFibreGram_permMatrix
#print axioms OIBridge.ReanchoredChannelScope.rn3a_act15_triple_cancels_on_reanchoredChannel
#print axioms OIBridge.ReanchoredChannelScope.rn3_plus_cancelling_triple_on_reanchoredChannel
#print axioms OIBridge.ReanchoredChannelScope.rn3_not_no_cancelling_on_reanchoredChannel
#print axioms OIBridge.ReanchoredChannelScope.rn4_redundancy_does_not_factor_on_relativeCandidate
