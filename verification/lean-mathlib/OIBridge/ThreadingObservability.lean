import OIBridge.CrossTimeInvariants

/-!
# Act 14 — is the residual threading freedom redundancy or physical

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-14-threading-observability/preregistration.md`, blob
`1b16008470bb1e2456c57aad58421a5941a55e0c`, from `main` at
`bc76a88dbe300a35715d5ce8196002f31aa62493` — the merge commit of that control plane, which the
freeze fixes as this round's mandated base.

## What this round is

An **adjudication round**. Act 13's `CT2` (b) localized the residual threading freedom of `P0`
exactly: the fibre cross-Gram trajectory determines a lift up to **one constant in-fibre left move
together with one time-dependent strong right gauge**. This module asks what that freedom means by
freezing four **carriers of observables**, computing what each carrier does to each part of the
freedom, and **adopting none of them**.

**Every verdict here is relative to a named carrier.** "Redundancy relative to `𝒪ₓ`" and "physical
relative to `𝒪ₓ`" are the only two predicates used; there is no carrier-free verdict in this
module, in any paraphrase.

## The structural point, frozen before anything else

**The residual freedom is not one object; it is a pair of parts with different transformation
behaviour**, and nothing here quantifies over "the freedom" without saying which part:

* the **strong right factor changes no anchored column, at any time** — `pq2b_anchored_column_identity`
  proves the anchored column family is *identical*, so **every** carrier definable from single-time
  anchored data is blind to it (`pq2b_every_single_time_anchored_carrier`);
* the **constant left factor changes every anchored column by one constant in-fibre unitary** — it
  preserves every fibre-Gram matrix (`pq0c_crossFibreGram_left_mul_diag`, act 12's
  `fibreGram_left_mul` consumed) and moves the off-diagonal cross-fibre blocks
  (`pq0c_crossFibreGram_left_mul`).

## The four carriers

| | probabilities only | full anchored channel |
| --- | --- | --- |
| **one time** | `𝒪₀`, the visible carrier — `readback a₀ (‖U_t ·‖²)` | `𝒪₁`, the anchored-channel carrier — `AnchoredChannel a₀ (U t)` |
| **re-anchored two-time** | `𝒪₂`, the relative-candidate carrier — `readback a₀ (‖U_t U_sᴴ ·‖²)` | `𝒪₃`, the re-anchored-channel carrier — `AnchoredChannel a₀ (U t * (U s)ᴴ)` |

`𝒪₀` is the diagonal action of `𝒪₁` and `𝒪₂` the diagonal action of `𝒪₃`
(`pq0a_readback_is_diagonal_action`, the latter by taking the matrix argument to be `U_t U_sᴴ`).
**No other relation between the four is asserted: they are not a ladder ordered by resolution.**

**Each carrier is used with its recorded presupposition.** `𝒪₁` and `𝒪₃` presuppose that the
reduced description's off-diagonal entries in the fixed visible basis are observations; `𝒪₂` and
`𝒪₃` presuppose that re-anchoring the ancilla at the conditioning time is a physical operation, and
act 7's `D4b` came back **negative**, the readback being the repository's own convention frozen by
act 7's readback amendment. **A separation relative to `𝒪₂` or `𝒪₃` is a separation under that
convention.** Nothing here adopts any carrier as the physical one, and nothing here says any of them
is not.

## The four budget slots

* `AnchoredChannel` — `𝔇_{a₀}(M)(ρ)_{i i'} = ∑_a (C(M) ρ C(M)ᴴ)_{(i,a),(i',a)}` for the anchored
  column family `C(M) = M.submatrix id (·, a₀)`; the carrier of `𝒪₁` and `𝒪₃`.
* `CrossFibreGram` — `Y_{i i'}(M) = X_i(M)ᴴ X_{i'}(M)`, whose `i' = i` diagonal is act 12's
  `FibreGram` definitionally (`crossFibreGram_diag`).
* `ThreadingRelated` — act 13's `CT2` (b) right-hand side named, so every target is stated over one
  object (`threadingRelated_iff_fibreCrossGram` is `ct2b_fibreCrossGram_iff` renamed).
* `UniformLeft` — `W = 1_V ⊗ W₀`, the uniformity predicate `PQ1` (d) needs.

The two remaining conditional slots are unused: no per-carrier observational-equality predicate and
no relative-object abbreviation is introduced, the relative objects being written out as
`U t * (U s)ᴴ` exactly as acts 11 and 13 write them.

## The targets

* **`PQ0`** — the carriers and the bridge to the merged readback:
  `pq0a_readback_is_diagonal_action`, `pq0b_anchoredChannel_diagonal_is_visible`, the
  transformation laws `pq0c_*`, and `pq0d_anchoredChannel_trace_preserving`, which earns the word
  *channel* for `𝔇_{a₀}` rather than asserting it.
* **`PQ1`** — the constant in-fibre left move: redundancy relative to `𝒪₀`
  (`pq1a_constant_left_redundant_visible`); physical relative to `𝒪₁`
  (`pq1b_constant_left_physical_anchoredChannel`, a difference of **modulus**, `1/2` against `0`);
  physical relative to `𝒪₂` (`pq1c_constant_left_physical_relative_candidate`, act 13's `CT4` and
  `CL1` consumed); and the `𝒪₁`-stabilizer, `pq1d_plus_uniform_left_redundant_anchoredChannel`
  together with `pq1d_minus_nonuniform_left_physical_anchoredChannel`.
* **`PQ2`** — the time-dependent strong right gauge: redundancy relative to `𝒪₀`
  (`pq2a_strong_right_redundant_visible`); redundancy relative to `𝒪₁` **and to every carrier
  definable from single-time anchored data** (`pq2b_anchored_column_identity`,
  `pq2b_every_single_time_anchored_carrier`, `pq2b_strong_right_redundant_anchoredChannel`);
  physical relative to `𝒪₂` (`pq2c_strong_right_physical_relative_candidate`, act 11's `GL2`
  consumed).
* **`PQ3`** — the two parts together: `pq3a_pair_redundant_visible`;
  `pq3b_pair_factors_through_left` with `pq3b_no_cancellation_on_anchoredChannel`, so relative to
  `𝒪₁` the pair is redundancy exactly when its left part is; and
  `pq3c_pair_physical_relative_candidate`, **a deliberately cheap witness whose strong family does
  no work at the certified time pair**.
* **`PQ4`** — the two reductions in the one direction each has:
  `pq2b_every_single_time_anchored_carrier` for the strong-right part and
  `pq4b_within_fibre_carrier_blind_to_constant_left` for the constant-left part. **The converses
  are not claimed**, and no datum and no selection principle is named.

## What none of this licenses

No carrier is adopted as the physical one, and none is asserted not to be. No selection principle is
named, endorsed or excluded, and nothing here asserts or denies that a connection or a gauge fixing
exists or suffices. `P0` is not closed, and neither of its two parts is: a verdict about a carrier is
not a selection, and the trajectory part is outside this round entirely. Nothing here says OI and QM
are inequivalent. `pq1b_constant_left_physical_anchoredChannel` is **not** a decoherence claim: it
exhibits two coherent lifts of one visible family whose visible reduced states differ in one
coherence, and says nothing about which lift is realized and nothing about any mechanism. The
anchored channel is **not** offered as a datum sufficient for the relative candidate — it is blind
to every strong-right family and `GL2` moves the candidate by one. The cross-fibre Gram and the
anchored channel are constructions on the lift space, and their status as observations is each
carrier's recorded presupposition. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
`SH1`, `CT1`–`CT4` and `CL1` are consumed and none is revised; act 13's fork `CT3` (d) stands
UNDECIDED and is not this round's `PQ3` (d). Nothing is imported from the substratum Lemma 24.1
round, and nothing here is about Track I.
-/

namespace OIBridge
namespace ThreadingObservability

open Finset Matrix CausalReadback RootedClassification TransposeBridge BarandesTupleRound
  ContinuousExtension DilationChoice ReadbackRobustness AnchorRobustness CoherentLiftGauge
  TwoSidedGauge CrossTimeInvariants

open scoped ComplexOrder

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budget slots -/

/-- **THE ANCHORED CHANNEL `𝔇_{a₀}`** (act 14's budget slot 1) — embed `ρ` on the visible carrier at
the anchored ancilla configuration, apply `M`, and sum over the **output** ancilla index:

`𝔇_{a₀}(M)(ρ)_{i i'} = ∑_a ∑_{j,k} M_{(i,a),(j,a₀)} ρ_{jk} conj(M_{(i',a),(k,a₀)})`.

It is a function of the **anchored columns** `C(M) = M.submatrix id (·, a₀)` alone, and it is built
from the two ingredients act 7's `readback` is built from — the anchor held on the input side, the
ancilla summed on the output side — with the modulus square replaced by the outer product, so that
the visible law is recovered as its diagonal action (`pq0a_readback_is_diagonal_action`,
`pq0b_anchoredChannel_diagonal_is_visible`). **Carries the anchor.**

**It is the carrier of `𝒪₁` and `𝒪₃`, not a proposed datum**: `pq2b_strong_right_redundant_anchoredChannel`
shows it blind to every strong-right family, and act 11's `GL2` moves the relative candidate by one,
so it does not determine the relative candidate. Its status as a carrier of observations is a
recorded presupposition, not a finding. -/
def AnchoredChannel (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ) :
    Matrix V V ℂ :=
  Matrix.of fun i i' => ∑ a : A,
    (M.submatrix id (fun j : V => (j, a₀)) * ρ
      * (M.submatrix id (fun j : V => (j, a₀)))ᴴ) (i, a) (i', a)

/-- **THE CROSS-FIBRE GRAM `Y_{i i'}`** (slot 2) — `X_i(M)ᴴ · X_{i'}(M)` for act 12's fibre block
`X_i(M) = M.submatrix (i,·) (·,a₀)`, entrywise `⟨P_i M e_{(j,a₀)}, P_{i'} M e_{(k,a₀)}⟩`. **Carries
the anchor.** Its `i' = i` diagonal is act 12's `FibreGram a₀ M i` definitionally
(`crossFibreGram_diag`); act 12 froze that case, and the off-diagonal case is this round's. It is the
object that separates the two parts of the residual freedom: the strong-right part leaves it
invariant (`pq2b_strong_right_crossFibreGram`) and the constant-left part moves its off-diagonal
blocks while fixing its diagonal (`pq0c_crossFibreGram_left_mul`,
`pq0c_crossFibreGram_left_mul_diag`). -/
def CrossFibreGram (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i i' : V) : Matrix V V ℂ :=
  (M.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
    * M.submatrix (fun a : A => (i', a)) (fun j : V => (j, a₀))

/-- **THE THREADING RELATION `≈_T`** (slot 3) — act 13's `CT2` (b) right-hand side named, so that
every target of this round is stated over one object: `U' ≈_T U` iff `U'_t = W · U_t · K_t` with
`W ∈ 𝒢_L` **constant** and `K_t` **strong** and time-dependent.

`threadingRelated_iff_fibreCrossGram` is act 13's merged `ct2b_fibreCrossGram_iff` renamed, in both
directions: `≈_T` is exactly the residual of the fibre cross-Gram trajectory. **The two parts are
kept apart throughout** — `threadingRelated_of_constLeft` and `threadingRelated_of_strongRight` are
the two subrelations, and no statement of this module quantifies over `≈_T` without naming which
part it means. -/
def ThreadingRelated (a₀ : A) (U U' : ℕ → Matrix (V × A) (V × A) ℂ) : Prop :=
  ∃ W : Matrix (V × A) (V × A) ℂ, LeftFibreGroup W
    ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U'

/-- **UNIFORMITY OF A CONSTANT IN-FIBRE LEFT MOVE** (slot 4, conditional — fired) — `W = 1_V ⊗ W₀`
for a single `W₀ ∈ U(A)`: the **same** ancilla relabelling in every visible fibre. A global phase is
the case `W₀ = c · 1_A` and needs no separate clause.

For `W ∈ 𝒢_L`, uniformity is exactly the block condition `W_iᴴ W_{i'} = 1` for every pair of fibres
(`uniformLeft_block`), which is what the `𝒪₁` computation consumes. **Act 7's `readback_relabel`
(`R-3`) is a statement about the readback and is not consumed here**: `PQ1` (d⁺) is a separate
computation about `𝔇_{a₀}`, and neither is evidence for the other. -/
def UniformLeft (W : Matrix (V × A) (V × A) ℂ) : Prop :=
  ∃ W₀ : Matrix A A ℂ, W₀ ∈ Matrix.unitaryGroup A ℂ
    ∧ ∀ p q : V × A, W p q = if p.1 = q.1 then W₀ p.2 q.2 else 0

/-! ### Section B — the carriers as objects: entries, the diagonal, and the trace form -/

/-- The cross-fibre Gram entrywise, as the inner product of two anchored columns projected into two
(possibly different) visible fibres. -/
theorem crossFibreGram_apply (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i i' j k : V) :
    CrossFibreGram a₀ M i i' j k
      = ∑ a : A, star (M (i, a) (j, a₀)) * M (i', a) (k, a₀) := by
  simp [CrossFibreGram, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.submatrix_apply]

/-- **ACT 12's FIBRE GRAM IS THE DIAGONAL OF THE CROSS-FIBRE GRAM, DEFINITIONALLY.** -/
theorem crossFibreGram_diag (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i : V) :
    CrossFibreGram a₀ M i i = FibreGram a₀ M i := rfl

/-- The anchored channel entrywise, in the form the freeze displays it. -/
theorem anchoredChannel_apply (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ)
    (i i' : V) :
    AnchoredChannel a₀ M ρ i i'
      = ∑ a : A, ∑ k : V, ∑ j : V,
          M (i, a) (j, a₀) * ρ j k * star (M (i', a) (k, a₀)) := by
  simp only [AnchoredChannel, Matrix.of_apply, Matrix.mul_apply, Matrix.conjTranspose_apply,
    Matrix.submatrix_apply, id_eq, Finset.sum_mul]

/-- The `(i, i')` block of `C(M) ρ C(M)ᴴ` is `X_i(M) ρ X_{i'}(M)ᴴ`: the anchored column family
restricted to two fibres. -/
theorem anchoredChannel_block (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ)
    (i i' : V) (a b : A) :
    (M.submatrix id (fun j : V => (j, a₀)) * ρ * (M.submatrix id (fun j : V => (j, a₀)))ᴴ)
        (i, a) (i', b)
      = (M.submatrix (fun c : A => (i, c)) (fun j : V => (j, a₀)) * ρ
          * (M.submatrix (fun c : A => (i', c)) (fun j : V => (j, a₀)))ᴴ) a b := rfl

/-- **THE ANCHORED CHANNEL IS A FUNCTION OF THE CROSS-FIBRE GRAM**, in the freeze's closed form
`𝔇_{a₀}(M)(ρ)_{i i'} = ∑_{j,k} ρ_{jk} (Y_{i' i}(M))_{k j} = Tr(ρ · Y_{i' i}(M))`. Every statement
about `𝔇_{a₀}` below is proved through this identity rather than by re-expanding the sums. -/
theorem anchoredChannel_eq_trace (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ)
    (i i' : V) :
    AnchoredChannel a₀ M ρ i i' = Matrix.trace (ρ * CrossFibreGram a₀ M i' i) := by
  have h1 : AnchoredChannel a₀ M ρ i i'
      = Matrix.trace (M.submatrix (fun c : A => (i, c)) (fun j : V => (j, a₀)) * ρ
          * (M.submatrix (fun c : A => (i', c)) (fun j : V => (j, a₀)))ᴴ) := by
    show (∑ a : A, _) = _
    exact Finset.sum_congr rfl fun a _ => anchoredChannel_block a₀ M ρ i i' a a
  rw [h1, Matrix.trace_mul_comm, ← Matrix.mul_assoc]
  exact Matrix.trace_mul_comm _ _

/-- `Tr(E_{r c} · G) = G_{c r}` for the matrix unit `E_{r c}`. The matrix units are **expressions**,
not definitions: they are the inputs at which the carriers are evaluated. -/
theorem trace_unit_mul (r c : V) (G : Matrix V V ℂ) :
    Matrix.trace
        ((Matrix.of fun p q : V => if p = r then (if q = c then (1 : ℂ) else 0) else 0) * G)
      = G c r := by
  rw [Matrix.trace]
  simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.of_apply]
  rw [Finset.sum_eq_single r
    (fun p _ hp => Finset.sum_eq_zero fun q _ => by rw [if_neg hp, zero_mul])
    (fun h => absurd (Finset.mem_univ _) h)]
  rw [Finset.sum_eq_single c (fun q _ hq => by rw [if_pos rfl, if_neg hq, zero_mul])
    (fun h => absurd (Finset.mem_univ _) h)]
  rw [if_pos rfl, if_pos rfl, one_mul]

/-- The anchored channel at a matrix unit reads off one cross-fibre Gram entry. -/
theorem anchoredChannel_unit (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (r c i i' : V) :
    AnchoredChannel a₀ M
        (Matrix.of fun p q : V => if p = r then (if q = c then (1 : ℂ) else 0) else 0) i i'
      = CrossFibreGram a₀ M i' i c r := by
  rw [anchoredChannel_eq_trace, trace_unit_mul]

/-- `C(M)ᴴ C(M) = ∑_i Y_{i i}(M) = ∑_i FibreGram a₀ M i`: the anchored column family's Gram matrix
is the fibre sum of the cross-fibre Gram's diagonal. -/
theorem anchoredCol_gram (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) :
    (M.submatrix id (fun j : V => (j, a₀)))ᴴ * M.submatrix id (fun j : V => (j, a₀))
      = ∑ i : V, FibreGram a₀ M i := by
  ext j k
  simp only [Matrix.sum_apply, Matrix.mul_apply, Matrix.conjTranspose_apply,
    Matrix.submatrix_apply, id_eq]
  rw [Fintype.sum_prod_type]
  exact Finset.sum_congr rfl fun i _ => by rw [fibreGram_apply]

/-- **THE ANCHORED COLUMNS OF A UNITARY ARE ORTHONORMAL** — `C(M)ᴴ C(M) = 1`, by act 12's merged
`sum_fibreGram`. This is what makes `𝔇_{a₀}` trace-preserving. -/
theorem anchoredCol_isometry {a₀ : A} {M : Matrix (V × A) (V × A) ℂ}
    (hM : M ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (M.submatrix id (fun j : V => (j, a₀)))ᴴ * M.submatrix id (fun j : V => (j, a₀)) = 1 := by
  rw [anchoredCol_gram, sum_fibreGram hM]

/-! ### Section C — `PQ0`: the bridge to the merged readback, the laws, and trace preservation -/

/-- **`PQ0` (a) — THE READBACK IS THE DIAGONAL ACTION OF THE ANCHORED CHANNEL.** For every matrix
over the carrier and all `i, j`,
`readback a₀ (M.map ‖·‖²) i j = (𝔇_{a₀}(M)(E_{jj}))_{i i}`.

Hence `𝒪₀` is the diagonal action of `𝒪₁`, and `𝒪₂` is the diagonal action of `𝒪₃` by taking
`M = U_t U_sᴴ`.

**Bounded reading:** this says the two new carriers restrict to merged objects; it does **not** say
either new carrier is observable, and it asserts no other relation between the four carriers — in
particular no implication between the one-time row and the re-anchored row, in either direction. -/
theorem pq0a_readback_is_diagonal_action (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i j : V) :
    ((readback a₀ (Matrix.of fun p q => ‖M p q‖ ^ 2) i j : ℝ) : ℂ)
      = AnchoredChannel a₀ M
          (Matrix.of fun p q : V => if p = j then (if q = j then (1 : ℂ) else 0) else 0) i i := by
  rw [anchoredChannel_unit, crossFibreGram_diag, fibreGram_diag]
  rfl

/-- **`PQ0` (b) — THE ANCHORED CHANNEL'S DIAGONAL IS THE VISIBLE LAW.** For an admissible dilation,
`(𝔇_{a₀}(M)(E_{jj}))_{ii} = Γ_{ij}`, by act 12's merged `fibreGram_diag_of_admissible`. -/
theorem pq0b_anchoredChannel_diagonal_is_visible {Γ : Matrix V V ℝ} {a₀ : A}
    {M : Matrix (V × A) (V × A) ℂ} (h : AdmissibleDilationAt Γ a₀ M) (i j : V) :
    AnchoredChannel a₀ M
        (Matrix.of fun p q : V => if p = j then (if q = j then (1 : ℂ) else 0) else 0) i i
      = (Γ i j : ℂ) := by
  rw [anchoredChannel_unit, crossFibreGram_diag]
  exact fibreGram_diag_of_admissible h i j

/-- **`PQ0` (c), THE STRONG-RIGHT LAW ON THE ANCHORED COLUMN FAMILY** — `C(M K) = C(M)`. Act 11's
`gaugeRelated_strong_iff_agree_on_anchor` forward direction and act 13's `mul_strong_anchor_col`,
both merged, in the form the whole of `PQ2` (b) rests on. -/
theorem pq0c_anchoredCol_mul_strong {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (M : Matrix (V × A) (V × A) ℂ) :
    (M * K).submatrix id (fun j : V => (j, a₀)) = M.submatrix id (fun j : V => (j, a₀)) := by
  ext p j
  simp only [Matrix.submatrix_apply, id_eq]
  exact mul_strong_anchor_col hK M p j

/-- **`PQ0` (c), THE STRONG-RIGHT LAW ON THE ANCHORED CHANNEL** — `𝔇_{a₀}(M K) = 𝔇_{a₀}(M)` for
every input `ρ`, because `𝔇_{a₀}` is a function of `C` and `C` is unchanged. -/
theorem pq0c_anchoredChannel_mul_strong {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ) :
    AnchoredChannel a₀ (M * K) ρ = AnchoredChannel a₀ M ρ := by
  unfold AnchoredChannel
  rw [pq0c_anchoredCol_mul_strong hK]

/-- **`PQ0` (c), THE STRONG-RIGHT LAW ON THE CROSS-FIBRE GRAM** — `Y_{i i'}(M K) = Y_{i i'}(M)` for
**every** pair of fibres, the off-diagonal pairs included. This **adds to** act 13's `CT3` (G),
which is stated for the fibre cross-Gram, and revises nothing. -/
theorem pq0c_crossFibreGram_mul_strong {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (M : Matrix (V × A) (V × A) ℂ) (i i' : V) :
    CrossFibreGram a₀ (M * K) i i' = CrossFibreGram a₀ M i i' := by
  unfold CrossFibreGram
  rw [mul_strong_submatrix hK, mul_strong_submatrix hK]

/-- **`PQ0` (c), THE CONSTANT-LEFT LAW ON THE CROSS-FIBRE GRAM** —
`Y_{i i'}(W M) = X_i(M)ᴴ W_iᴴ W_{i'} X_{i'}(M)` for `W ∈ 𝒢_L`, by act 12's merged
`left_mul_submatrix`. **The block factor `W_iᴴ W_{i'}` is what survives on the off-diagonal pairs**
and what `PQ1` (d) is about. -/
theorem pq0c_crossFibreGram_left_mul {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i i' : V) :
    CrossFibreGram a₀ (W * M) i i'
      = (M.submatrix (fun a : A => (i, a)) (fun j : V => (j, a₀)))ᴴ
          * ((W.submatrix (fun a : A => (i, a)) (fun a : A => (i, a)))ᴴ
              * W.submatrix (fun a : A => (i', a)) (fun a : A => (i', a)))
          * M.submatrix (fun a : A => (i', a)) (fun j : V => (j, a₀)) := by
  unfold CrossFibreGram
  rw [left_mul_submatrix hW, left_mul_submatrix hW, Matrix.conjTranspose_mul]
  simp only [Matrix.mul_assoc]

/-- **`PQ0` (c), THE CONSTANT-LEFT LAW ON THE DIAGONAL** — `Y_{i i}(W M) = FibreGram a₀ M i`: the
constant-left part preserves **every** fibre-Gram matrix, act 12's merged `fibreGram_left_mul`
consumed. -/
theorem pq0c_crossFibreGram_left_mul_diag {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) (i : V) :
    CrossFibreGram a₀ (W * M) i i = FibreGram a₀ M i :=
  fibreGram_left_mul hW a₀ M i

/-- **`PQ0` (d) — THE ANCHORED CHANNEL IS TRACE-PRESERVING ON A UNITARY.** `Tr 𝔇_{a₀}(M)(ρ) = Tr ρ`
for every `ρ`, because `∑_i Y_{i i}(M) = C(M)ᴴ C(M) = 1` (act 12's `sum_fibreGram`, consumed).

**Why this is in the round:** it is what earns the word *channel* for `𝔇_{a₀}` rather than asserting
it, and it applies to `𝒪₃` as well, each relative object `U_t U_sᴴ` being unitary. **It is not a
claim that the channel is observable**; that remains `𝒪₁`'s and `𝒪₃`'s recorded presupposition. -/
theorem pq0d_anchoredChannel_trace_preserving {a₀ : A} {M : Matrix (V × A) (V × A) ℂ}
    (hM : M ∈ Matrix.unitaryGroup (V × A) ℂ) (ρ : Matrix V V ℂ) :
    Matrix.trace (AnchoredChannel a₀ M ρ) = Matrix.trace ρ := by
  have h : Matrix.trace (AnchoredChannel a₀ M ρ)
      = ∑ i : V, Matrix.trace (ρ * FibreGram a₀ M i) := by
    rw [Matrix.trace]
    exact Finset.sum_congr rfl fun i _ => anchoredChannel_eq_trace a₀ M ρ i i
  rw [h, ← Matrix.trace_sum, ← Finset.mul_sum, sum_fibreGram hM, Matrix.mul_one]

/-! ### Section D — the threading relation, and its two parts kept apart -/

/-- **`≈_T` IS EXACTLY THE RESIDUAL OF THE FIBRE CROSS-GRAM TRAJECTORY** — act 13's merged
`ct2b_fibreCrossGram_iff` renamed, in both directions, so that every target of this round is stated
over one object. Act 13's statement is consumed unmodified. -/
theorem threadingRelated_iff_fibreCrossGram {a₀ : A} {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : ∀ t, U t ∈ Matrix.unitaryGroup (V × A) ℂ)
    (hU' : ∀ t, U' t ∈ Matrix.unitaryGroup (V × A) ℂ) :
    (∀ i t s, FibreCrossGram a₀ U' i t s = FibreCrossGram a₀ U i t s) ↔ ThreadingRelated a₀ U U' :=
  ct2b_fibreCrossGram_iff hU hU'

/-- **THE CONSTANT-LEFT SUBRELATION** — one part of `≈_T`, with the strong family trivial. -/
theorem threadingRelated_of_constLeft {a₀ : A} {W : Matrix (V × A) (V × A) ℂ}
    (hW : LeftFibreGroup W) (U : ℕ → Matrix (V × A) (V × A) ℂ) :
    ThreadingRelated a₀ U (fun t => W * U t) :=
  ⟨W, hW, fun _ => 1, fun _ => ⟨one_mem _, fun p j => Matrix.one_apply⟩,
    fun t => (Matrix.mul_one _).symm⟩

/-- **THE STRONG-RIGHT SUBRELATION** — the other part of `≈_T`, with the constant left move
trivial. -/
theorem threadingRelated_of_strongRight {a₀ : A} {K : ℕ → Matrix (V × A) (V × A) ℂ}
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (U : ℕ → Matrix (V × A) (V × A) ℂ) :
    ThreadingRelated a₀ U (fun t => U t * K t) :=
  ⟨1, one_leftFibreGroup, K, hK, fun t => by
    show U t * K t = 1 * U t * K t
    rw [Matrix.one_mul]⟩

/-! ### Section E — `PQ1`: the constant in-fibre left move, carrier by carrier -/

/-- **`PQ1` (a) — THE CONSTANT IN-FIBRE LEFT MOVE IS REDUNDANCY RELATIVE TO `𝒪₀`.** For every
`W ∈ 𝒢_L` and every coherent lift, `W · U` is a coherent lift of the same visible family and the
visible carrier's value is unchanged. Consumed from act 12's `left_preserves_admissible`, whose
mechanism is `fibreGram_left_mul`. -/
theorem pq1a_constant_left_redundant_visible {Γ : ℕ → Matrix V V ℝ} {a₀ : A}
    {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    {U : ℕ → Matrix (V × A) (V × A) ℂ} (hU : CoherentLift a₀ Γ U) :
    CoherentLift a₀ Γ (fun t => W * U t)
      ∧ ∀ t, readback a₀ (Matrix.of fun p q => ‖(W * U t) p q‖ ^ 2)
              = readback a₀ (Matrix.of fun p q => ‖U t p q‖ ^ 2) := by
  refine ⟨fun t => left_preserves_admissible hW (hU t), fun t => ?_⟩
  rw [readback_of_admissible (left_preserves_admissible hW (hU t)), readback_of_admissible (hU t)]

/-- **`PQ1` (b) — THE CONSTANT IN-FIBRE LEFT MOVE IS PHYSICAL RELATIVE TO `𝒪₁`.** On `V = Fin 2`,
`A = Fin 2`, `a₀ = 0`, with the constant identity law and the constant identity lift `U_t = 𝟙`, the
constant in-fibre swap `W = P(swap((0,0),(0,1))) ∈ 𝒢_L` gives a second coherent lift `U'_t = W U_t`
of the **same** visible family, and at the uniform visible superposition `ρ = ½ · J` the two
anchored channels differ at the coherence `(0,1)`: `1/2` for `U`, `0` for `U'`, while **both
diagonals agree**, which is the identity law.

**The certificate is a difference of modulus, not of phase**, so it survives any quotient of `𝒪₁` by
a rephasing of the visible basis. The certified matrices `𝟙` and `W` are act 13's merged `CT4` pair
at `t = 0`; `CT4` is consumed unmodified and this adds two channel entries on the same pair.

**`|A| ≥ 2` is part of the statement**, as its first conjunct: at `|A| = 1` the in-fibre group is the
diagonal phases, conjugation by which multiplies each cross-fibre Gram block by a unit scalar, and
the modulus form of the separation is absent.

**This is not a decoherence claim** (act 14's hazard 5): it says two coherent lifts of one visible
family have visible reduced states differing in one coherence, and says nothing about which lift the
framework realizes, nothing about any mechanism, and nothing about decoherence theory. **The
permutation convention is act 7's**, and every entry is computed, not read off. -/
theorem pq1b_constant_left_physical_anchoredChannel :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U U' : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (W : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) (ρ : Matrix (Fin 2) (Fin 2) ℂ),
      (∀ a : Fin 2, ∃ a' : Fin 2, a' ≠ a)
        ∧ (∀ t, Γ t = 1)
        ∧ (∀ t, U t = 1)
        ∧ W = (Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
            : Equiv.Perm (Fin 2 × Fin 2)).permMatrix ℂ
        ∧ (∀ t, U' t = W * U t)
        ∧ LeftFibreGroup W
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ThreadingRelated (0 : Fin 2) U U'
        ∧ ρ = Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))
        ∧ AnchoredChannel (0 : Fin 2) (U 0) ρ 0 1 = 1 / 2
        ∧ AnchoredChannel (0 : Fin 2) (U' 0) ρ 0 1 = 0
        ∧ ‖AnchoredChannel (0 : Fin 2) (U' 0) ρ 0 1‖
            ≠ ‖AnchoredChannel (0 : Fin 2) (U 0) ρ 0 1‖
        ∧ (∀ i : Fin 2, AnchoredChannel (0 : Fin 2) (U' 0) ρ i i
            = AnchoredChannel (0 : Fin 2) (U 0) ρ i i)
        ∧ (∀ t, readback (0 : Fin 2) (Matrix.of fun p q => ‖U' t p q‖ ^ 2)
            = readback (0 : Fin 2) (Matrix.of fun p q => ‖U t p q‖ ^ 2)) := by
  classical
  obtain ⟨τ, hτ⟩ : ∃ τ : Equiv.Perm (Fin 2 × Fin 2),
      τ = Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hτleft : LeftFibreGroup (τ.permMatrix ℂ) := by
    rw [hτ]; exact inFibreSwap_leftFibreGroup
  have hcohU : CoherentLift (0 : Fin 2) (fun _ => (1 : Matrix (Fin 2) (Fin 2) ℝ))
      (fun _ => (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)) :=
    fun _ => one_admissible_at_every_anchor _
  refine ⟨fun _ => 1, fun _ => 1, fun _ => τ.permMatrix ℂ * 1, τ.permMatrix ℂ,
    Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ)),
    ?_, fun _ => rfl, fun _ => rfl, by rw [hτ], fun _ => rfl, hτleft, hcohU,
    fun t => left_preserves_admissible hτleft (hcohU t),
    ⟨τ.permMatrix ℂ, hτleft, fun _ => 1, fun _ => ⟨one_mem _, fun p j => Matrix.one_apply⟩,
      fun _ => (Matrix.mul_one _).symm⟩,
    rfl, ?_, ?_, ?_, ?_, ?_⟩
  · intro a
    fin_cases a
    · exact ⟨1, by decide⟩
    · exact ⟨0, by decide⟩
  · show AnchoredChannel (0 : Fin 2) (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) 0 1 = 1 / 2
    rw [anchoredChannel_apply]
    simp +decide [Fin.sum_univ_two, Matrix.one_apply, Prod.ext_iff]
  · show AnchoredChannel (0 : Fin 2) (τ.permMatrix ℂ * 1)
      (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) 0 1 = 0
    rw [Matrix.mul_one, anchoredChannel_apply]
    simp +decide [hτ, Fin.sum_univ_two, Equiv.swap_apply_def]
  · show ‖AnchoredChannel (0 : Fin 2) (τ.permMatrix ℂ * 1)
        (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) 0 1‖
      ≠ ‖AnchoredChannel (0 : Fin 2) (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) 0 1‖
    rw [Matrix.mul_one, anchoredChannel_apply, anchoredChannel_apply]
    simp +decide [hτ, Fin.sum_univ_two, Matrix.one_apply, Prod.ext_iff, permMatrix_apply_eq,
      Equiv.swap_apply_def]
  · intro i
    show AnchoredChannel (0 : Fin 2) (τ.permMatrix ℂ * 1)
        (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) i i
      = AnchoredChannel (0 : Fin 2) (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
        (Matrix.of (fun _ _ : Fin 2 => (1 / 2 : ℂ))) i i
    rw [Matrix.mul_one, anchoredChannel_apply, anchoredChannel_apply]
    fin_cases i <;>
      simp +decide [hτ, Fin.sum_univ_two, Matrix.one_apply, Prod.ext_iff, permMatrix_apply_eq,
        Equiv.swap_apply_def]
  · intro t
    have h1 : AdmissibleDilationAt (1 : Matrix (Fin 2) (Fin 2) ℝ) (0 : Fin 2)
        (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) := one_admissible_at_every_anchor _
    have h2 : AdmissibleDilationAt (1 : Matrix (Fin 2) (Fin 2) ℝ) (0 : Fin 2)
        (τ.permMatrix ℂ * (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)) :=
      left_preserves_admissible hτleft h1
    show readback (0 : Fin 2) (Matrix.of fun p q =>
          ‖(τ.permMatrix ℂ * (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)) p q‖ ^ 2)
      = readback (0 : Fin 2) (Matrix.of fun p q =>
          ‖(1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) p q‖ ^ 2)
    rw [readback_of_admissible h2, readback_of_admissible h1]

/-- **`PQ1` (c) — THE CONSTANT IN-FIBRE LEFT MOVE IS PHYSICAL RELATIVE TO `𝒪₂`.** Consumed from act
13's merged `CT4` and `CL1` at their own strength: existential, `|A| ≥ 2`, with the `|A| = 1` scoping
carried as the first conjunct. **`CT4` is not revised**; this restates it over `ThreadingRelated`.

**Act 7's boundary is carried**: `D4b` came back negative and the readback is the repository's own
convention, frozen by act 7's readback amendment, so this is a separation relative to `𝒪₂` **under
that convention**. -/
theorem pq1c_constant_left_physical_relative_candidate :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U U' : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (W : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      (∀ a : Fin 2, ∃ a' : Fin 2, a' ≠ a)
        ∧ LeftFibreGroup W
        ∧ (∀ t, U' t = W * U t)
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ThreadingRelated (0 : Fin 2) U U'
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2) 0 0 = 1
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) 0 0 = 0 := by
  obtain ⟨Γ, U, U', W, htwo, -, -, -, -, hfac, hW, hcoh, hcoh', -, -, -, h1, h0⟩ :=
    ct4_constant_left_obstruction
  have hU'eq : U' = fun t => W * U t := funext hfac
  refine ⟨Γ, U, U', W, htwo, hW, hfac, hcoh, hcoh', ?_, h1, h0⟩
  rw [hU'eq]
  exact threadingRelated_of_constLeft hW U

/-- **UNIFORMITY IS THE BLOCK CONDITION.** For `W ∈ 𝒢_L`, `W = 1_V ⊗ W₀` holds exactly when
`W_iᴴ W_{i'} = 1` for every pair of fibres — which says exactly that all the blocks are equal. This
is the form `PQ1` (d) consumes on both sides. -/
theorem uniformLeft_block {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W) :
    UniformLeft W ↔ ∀ i i' : V,
      (W.submatrix (fun a : A => (i, a)) (fun a : A => (i, a)))ᴴ
        * W.submatrix (fun a : A => (i', a)) (fun a : A => (i', a)) = 1 := by
  constructor
  · rintro ⟨W₀, hW₀, hEq⟩ i i'
    have hb : ∀ j : V, W.submatrix (fun a : A => (j, a)) (fun a : A => (j, a)) = W₀ := by
      intro j
      ext a b
      rw [Matrix.submatrix_apply, hEq]
      simp
    rw [hb, hb]
    have h := Matrix.mem_unitaryGroup_iff'.1 hW₀
    rwa [Matrix.star_eq_conjTranspose] at h
  · intro hall
    rcases isEmpty_or_nonempty V with hV | hV
    · exact ⟨1, one_mem _, fun p q => (hV.false p.1).elim⟩
    · obtain ⟨i₀⟩ := hV
      have hblk : ∀ j : V, W.submatrix (fun a : A => (j, a)) (fun a : A => (j, a))
          = W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a)) := by
        intro j
        have hmem : W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a))
            ∈ Matrix.unitaryGroup A ℂ := by
          rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
          exact left_block_unitary hW i₀
        have h2 : W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a))
            * (W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a)))ᴴ = 1 := by
          have h := Matrix.mem_unitaryGroup_iff.1 hmem
          rwa [Matrix.star_eq_conjTranspose] at h
        calc W.submatrix (fun a : A => (j, a)) (fun a : A => (j, a))
            = (W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a))
                * (W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a)))ᴴ)
              * W.submatrix (fun a : A => (j, a)) (fun a : A => (j, a)) := by
                rw [h2, Matrix.one_mul]
          _ = W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a))
              * ((W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a)))ᴴ
                * W.submatrix (fun a : A => (j, a)) (fun a : A => (j, a))) :=
                Matrix.mul_assoc _ _ _
          _ = _ := by rw [hall i₀ j, Matrix.mul_one]
      refine ⟨W.submatrix (fun a : A => (i₀, a)) (fun a : A => (i₀, a)), ?_, ?_⟩
      · rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
        exact left_block_unitary hW i₀
      · rintro ⟨i, a⟩ ⟨j, b⟩
        by_cases hij : i = j
        · subst hij
          rw [if_pos rfl]
          have := congrFun (congrFun (hblk i) a) b
          simpa only [Matrix.submatrix_apply] using this
        · rw [if_neg hij]
          exact hW.2 (i, a) (j, b) hij

/-- **`PQ1` (d⁺) — EVERY UNIFORM ANCILLA RELABELLING IS REDUNDANCY RELATIVE TO `𝒪₁`, FOR EVERY
MATRIX.** If `W = 1_V ⊗ W₀` then `W_iᴴ W_{i'} = W₀ᴴ W₀ = 1` for every pair, so every cross-fibre Gram
block and hence every anchored-channel value is unchanged. A global phase is the case
`W₀ = c · 1_A`. -/
theorem pq1d_plus_uniform_left_redundant_anchoredChannel {a₀ : A}
    {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W) (hUni : UniformLeft W)
    (M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ) :
    AnchoredChannel a₀ (W * M) ρ = AnchoredChannel a₀ M ρ := by
  have hblk := (uniformLeft_block hW).1 hUni
  ext i i'
  rw [anchoredChannel_eq_trace, anchoredChannel_eq_trace,
    pq0c_crossFibreGram_left_mul hW, hblk, Matrix.mul_one]
  rfl

/-- A non-uniform `W ∈ 𝒢_L` has two **distinct** fibres whose block condition fails at a named pair
of ancilla indices. The distinctness is forced: at `i = i'` the block condition is act 12's
`left_block_unitary`. -/
theorem nonuniform_left_block_witness {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    (hnu : ¬ UniformLeft W) :
    ∃ (i i' : V) (a b : A), i ≠ i' ∧
      ((W.submatrix (fun c : A => (i, c)) (fun c : A => (i, c)))ᴴ
        * W.submatrix (fun c : A => (i', c)) (fun c : A => (i', c))) a b
        ≠ (1 : Matrix A A ℂ) a b := by
  rw [uniformLeft_block hW] at hnu
  push_neg at hnu
  obtain ⟨i, i', hne⟩ := hnu
  have hii' : i ≠ i' := by
    rintro rfl
    exact hne (left_block_unitary hW i)
  refine ⟨i, i', ?_⟩
  by_contra hc
  push_neg at hc
  exact hne (by ext a b; exact hc a b hii')

/-- Under a permutation dilation the cross-fibre Gram reads the columns the permutation sends to the
anchored slot. Act 7's convention is used throughout and the index is computed, never read off. -/
theorem crossFibreGram_mul_permMatrix (a₀ : A) (σ : Equiv.Perm (V × A))
    (M : Matrix (V × A) (V × A) ℂ) (i i' j k : V) :
    CrossFibreGram a₀ (M * σ.permMatrix ℂ) i i' j k
      = ∑ c : A, star (M (i, c) (σ.symm (j, a₀))) * M (i', c) (σ.symm (k, a₀)) := by
  rw [crossFibreGram_apply]
  exact Finset.sum_congr rfl fun c _ => by
    rw [mul_permMatrix_apply, mul_permMatrix_apply]

/-- **`PQ1` (d⁻) — NO OTHER CONSTANT IN-FIBRE LEFT MOVE IS REDUNDANCY RELATIVE TO `𝒪₁`.** For
**every** non-uniform `W ∈ 𝒢_L`, over arbitrary finite `V` and `A`, there is a coherent lift on which
the anchored-channel carrier separates `U` from `W · U`.

The construction: `W` non-uniform gives two distinct fibres `i ≠ i'` and ancilla indices `a, b` with
`(W_iᴴ W_{i'})_{ab} ≠ δ_{ab}` (`nonuniform_left_block_witness`). One permutation `σ` of the dilated
carrier sends `(i,a)` to `(i,a₀)` and `(i',b)` to `(i',a₀)` — it exists because both pairs are
distinct — and the constant permutation lift `U_t = P(σ)` is admissible for the visible family act
7's `admissible_permMatrix` computes from it, while `W · U` is admissible by act 12's
`left_preserves_admissible`. At the matrix unit `E_{i' i}` the anchored channel reads the entry
`Y_{i i'}(·)_{i i'}`, which is `δ_{ab}` for `U` and `(W_iᴴ W_{i'})_{ab}` for `W · U`.

**With `PQ1` (d⁺): among constant in-fibre left moves, redundancy relative to `𝒪₁` holds exactly for
the uniform ancilla relabellings.** No claim is made about any other carrier. -/
theorem pq1d_minus_nonuniform_left_physical_anchoredChannel {a₀ : A}
    {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W) (hnu : ¬ UniformLeft W) :
    ∃ (Γ : ℕ → Matrix V V ℝ) (U : ℕ → Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ) (m n : V),
      CoherentLift a₀ Γ U ∧ CoherentLift a₀ Γ (fun t => W * U t)
        ∧ ∀ t, AnchoredChannel a₀ (W * U t) ρ m n ≠ AnchoredChannel a₀ (U t) ρ m n := by
  classical
  obtain ⟨i, i', a, b, hii', hab⟩ := nonuniform_left_block_witness hW hnu
  obtain ⟨τ₁, hτ₁⟩ : ∃ τ₁ : Equiv.Perm (V × A),
      τ₁ = Equiv.swap ((i, a) : V × A) ((i, a₀) : V × A) := ⟨_, rfl⟩
  obtain ⟨z, hz⟩ : ∃ z : V × A, z = τ₁ ((i', b) : V × A) := ⟨_, rfl⟩
  obtain ⟨σ, hσ⟩ : ∃ σ : Equiv.Perm (V × A),
      σ = τ₁.trans (Equiv.swap z ((i', a₀) : V × A)) := ⟨_, rfl⟩
  have hx : ((i, a) : V × A) ≠ ((i', b) : V × A) := fun h => hii' (congrArg Prod.fst h)
  have hy : ((i, a₀) : V × A) ≠ ((i', a₀) : V × A) := fun h => hii' (congrArg Prod.fst h)
  have hτ₁x : τ₁ ((i, a) : V × A) = ((i, a₀) : V × A) := by
    rw [hτ₁]; exact Equiv.swap_apply_left _ _
  have hzne : z ≠ ((i, a₀) : V × A) := by
    intro hcon
    apply hx
    have : τ₁ ((i', b) : V × A) = τ₁ ((i, a) : V × A) := by rw [← hz, hcon, hτ₁x]
    exact (τ₁.injective this).symm
  have hσ1 : σ ((i, a) : V × A) = ((i, a₀) : V × A) := by
    rw [hσ]
    show (Equiv.swap z ((i', a₀) : V × A)) (τ₁ ((i, a) : V × A)) = _
    rw [hτ₁x]
    exact Equiv.swap_apply_of_ne_of_ne (Ne.symm hzne) hy
  have hσ2 : σ ((i', b) : V × A) = ((i', a₀) : V × A) := by
    rw [hσ]
    show (Equiv.swap z ((i', a₀) : V × A)) (τ₁ ((i', b) : V × A)) = _
    rw [← hz]
    exact Equiv.swap_apply_left _ _
  have hsym1 : σ.symm ((i, a₀) : V × A) = ((i, a) : V × A) :=
    (Equiv.symm_apply_eq σ).2 hσ1.symm
  have hsym2 : σ.symm ((i', a₀) : V × A) = ((i', b) : V × A) :=
    (Equiv.symm_apply_eq σ).2 hσ2.symm
  have hadm : AdmissibleDilationAt
      (Matrix.of fun p q : V => if (σ.symm (q, a₀)).1 = p then (1 : ℝ) else 0) a₀
      (σ.permMatrix ℂ) := admissible_permMatrix a₀ σ fun _ _ => rfl
  refine ⟨fun _ => Matrix.of fun p q : V => if (σ.symm (q, a₀)).1 = p then (1 : ℝ) else 0,
    fun _ => σ.permMatrix ℂ,
    Matrix.of fun p q : V => if p = i' then (if q = i then (1 : ℂ) else 0) else 0,
    i', i, fun _ => hadm, fun t => left_preserves_admissible hW hadm, fun t => ?_⟩
  have hleft : CrossFibreGram a₀ (W * σ.permMatrix ℂ) i i' i i'
      = ((W.submatrix (fun c : A => (i, c)) (fun c : A => (i, c)))ᴴ
          * W.submatrix (fun c : A => (i', c)) (fun c : A => (i', c))) a b := by
    rw [crossFibreGram_mul_permMatrix, hsym1, hsym2, Matrix.mul_apply]
    exact Finset.sum_congr rfl fun c _ => by
      simp only [Matrix.conjTranspose_apply, Matrix.submatrix_apply]
  have hright : CrossFibreGram a₀ (σ.permMatrix ℂ) i i' i i' = (1 : Matrix A A ℂ) a b := by
    have hrw : (σ.permMatrix ℂ) = (1 : Matrix (V × A) (V × A) ℂ) * σ.permMatrix ℂ :=
      (Matrix.one_mul _).symm
    rw [hrw, crossFibreGram_mul_permMatrix, hsym1, hsym2]
    rw [Finset.sum_eq_single a
      (fun c _ hc => by
        rw [Matrix.one_apply_ne (fun hcon => hc (Prod.ext_iff.1 hcon).2), star_zero, zero_mul])
      (fun h => absurd (Finset.mem_univ _) h)]
    rw [Matrix.one_apply_eq, star_one, one_mul]
    by_cases hb2 : a = b
    · subst hb2
      rw [Matrix.one_apply_eq, Matrix.one_apply_eq]
    · rw [Matrix.one_apply_ne (fun hcon => hb2 (Prod.ext_iff.1 hcon).2),
        Matrix.one_apply_ne hb2]
  show AnchoredChannel a₀ (W * σ.permMatrix ℂ) _ i' i
    ≠ AnchoredChannel a₀ (σ.permMatrix ℂ) _ i' i
  rw [anchoredChannel_unit, anchoredChannel_unit, hleft, hright]
  exact hab

/-! ### Section F — `PQ2`: the time-dependent strong right gauge, carrier by carrier -/

/-- **`PQ2` (a) — THE STRONG RIGHT GAUGE IS REDUNDANCY RELATIVE TO `𝒪₀`.** Consumed from act 11's
merged `weak_preserves_admissible` with `strong_mem_weak`. -/
theorem pq2a_strong_right_redundant_visible {Γ : ℕ → Matrix V V ℝ} {a₀ : A}
    {U K : ℕ → Matrix (V × A) (V × A) ℂ} (hU : CoherentLift a₀ Γ U)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) :
    CoherentLift a₀ Γ (fun t => U t * K t)
      ∧ ∀ t, readback a₀ (Matrix.of fun p q => ‖(U t * K t) p q‖ ^ 2)
              = readback a₀ (Matrix.of fun p q => ‖U t p q‖ ^ 2) := by
  refine ⟨fun t => weak_preserves_admissible (hU t) (strong_mem_weak (hK t)), fun t => ?_⟩
  rw [readback_of_admissible (weak_preserves_admissible (hU t) (strong_mem_weak (hK t))),
    readback_of_admissible (hU t)]

/-- **`PQ2` (b), THE LOAD-BEARING CONJUNCT — THE ANCHORED COLUMN FAMILY IS IDENTICAL.**
`C(U_t K_t) = C(U_t)` at every time, for every lift and every family of strong elements. Not "equal
after some functional is applied": the object itself. -/
theorem pq2b_anchored_column_identity {a₀ : A} {K : ℕ → Matrix (V × A) (V × A) ℂ}
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t : ℕ) :
    (U t * K t).submatrix id (fun j : V => (j, a₀))
      = (U t).submatrix id (fun j : V => (j, a₀)) :=
  pq0c_anchoredCol_mul_strong (hK t) (U t)

/-- **`PQ2` (b) — EVERY CARRIER DEFINABLE FROM THE SINGLE-TIME ANCHORED COLUMNS IS BLIND TO EVERY
STRONG-RIGHT FAMILY**, at any level, including carriers this round does not name. This is the reason
no refinement of `𝒪₁` within single-time anchored data can separate this part of the freedom, and it
is the one direction `PQ4` (a) has.

**It covers act 13's merged `CT3` (G), which is stated for the Gram data, and more — the whole
anchored column family — and it revises nothing:** `CT3` (G) stands as act 13 states it. -/
theorem pq2b_every_single_time_anchored_carrier {β : Type} (𝒪 : Matrix (V × A) V ℂ → β) {a₀ : A}
    {K : ℕ → Matrix (V × A) (V × A) ℂ} (hK : ∀ t, StrongAnchorStabilizer a₀ (K t))
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (t : ℕ) :
    𝒪 ((U t * K t).submatrix id (fun j : V => (j, a₀)))
      = 𝒪 ((U t).submatrix id (fun j : V => (j, a₀))) := by
  rw [pq2b_anchored_column_identity hK U t]

/-- **`PQ2` (b) ON `𝒪₁` — THE STRONG RIGHT GAUGE IS REDUNDANCY RELATIVE TO THE ANCHORED-CHANNEL
CARRIER**, for every lift, every strong family, every time and every input. -/
theorem pq2b_strong_right_redundant_anchoredChannel {a₀ : A}
    {K : ℕ → Matrix (V × A) (V × A) ℂ} (hK : ∀ t, StrongAnchorStabilizer a₀ (K t))
    (U : ℕ → Matrix (V × A) (V × A) ℂ) (t : ℕ) (ρ : Matrix V V ℂ) :
    AnchoredChannel a₀ (U t * K t) ρ = AnchoredChannel a₀ (U t) ρ :=
  pq0c_anchoredChannel_mul_strong (hK t) (U t) ρ

/-- **`PQ2` (b) ON THE CROSS-FIBRE GRAM** — every pair of fibres, the off-diagonal pairs included. -/
theorem pq2b_strong_right_crossFibreGram {a₀ : A} {K : ℕ → Matrix (V × A) (V × A) ℂ}
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) (U : ℕ → Matrix (V × A) (V × A) ℂ) (t : ℕ)
    (i i' : V) :
    CrossFibreGram a₀ (U t * K t) i i' = CrossFibreGram a₀ (U t) i i' :=
  pq0c_crossFibreGram_mul_strong (hK t) (U t) i i'

/-- **`PQ2` (c) — THE STRONG RIGHT GAUGE IS PHYSICAL RELATIVE TO `𝒪₂`.** Consumed from act 11's
merged `GL2` at its own strength: existential, one visible pair, one anchor, one time pair, under
the frozen readback. **`GL2` stands as stated and nothing is added to it** except its restatement
over `ThreadingRelated`.

**Act 7's boundary is carried**: `D4b` came back negative and the readback is the repository's own
convention, so this is a separation relative to `𝒪₂` **under that convention**.

**With `PQ2` (b): the strong-right part is redundancy relative to every single-time anchored carrier
and is not redundancy relative to the relative-candidate carrier. Both are true; neither is the
other**, and their conjunction is not a third, stronger sentence. -/
theorem pq2c_strong_right_physical_relative_candidate :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ) (U U' K : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 2) (K t))
        ∧ (∀ t, U' t = U t * K t)
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ ThreadingRelated (0 : Fin 2) U U'
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2)
            ≠ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) := by
  obtain ⟨Γ, U, U', K, hcoh, hcoh', hK, hfac, hne, hsep⟩ :=
    gl2_strong_gauge_moves_relative_candidate
  refine ⟨Γ, U, U', K, hcoh, hcoh', hK, hfac, hne, ?_, hsep⟩
  have hU'eq : U' = fun t => U t * K t := funext hfac
  rw [hU'eq]
  exact threadingRelated_of_strongRight hK U

/-! ### Section G — `PQ3`: the two parts together -/

/-- **`PQ3` (a) — THE PAIR IS REDUNDANCY RELATIVE TO `𝒪₀`.** The composite of `PQ1` (a) and
`PQ2` (a). -/
theorem pq3a_pair_redundant_visible {Γ : ℕ → Matrix V V ℝ} {a₀ : A}
    {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    {U K : ℕ → Matrix (V × A) (V × A) ℂ} (hU : CoherentLift a₀ Γ U)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) :
    CoherentLift a₀ Γ (fun t => W * U t * K t)
      ∧ ∀ t, readback a₀ (Matrix.of fun p q => ‖(W * U t * K t) p q‖ ^ 2)
              = readback a₀ (Matrix.of fun p q => ‖U t p q‖ ^ 2) := by
  have hL : CoherentLift a₀ Γ (fun t => W * U t) :=
    (pq1a_constant_left_redundant_visible hW hU).1
  refine ⟨fun t => weak_preserves_admissible (hL t) (strong_mem_weak (hK t)), fun t => ?_⟩
  rw [readback_of_admissible (weak_preserves_admissible (hL t) (strong_mem_weak (hK t))),
    readback_of_admissible (hU t)]

/-- **`PQ3` (b) — RELATIVE TO `𝒪₁` THE PAIR ACTS EXACTLY AS ITS LEFT PART.**
`𝔇_{a₀}(W U_t K_t) = 𝔇_{a₀}(W U_t)` for every lift, every constant `W` and every strong family. -/
theorem pq3b_pair_factors_through_left {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (W M : Matrix (V × A) (V × A) ℂ) (ρ : Matrix V V ℂ) :
    AnchoredChannel a₀ (W * M * K) ρ = AnchoredChannel a₀ (W * M) ρ :=
  pq0c_anchoredChannel_mul_strong hK (W * M) ρ

/-- **`PQ3` (b), THE CONSEQUENCE STATED EXACTLY** — relative to `𝒪₁` the pair is redundancy for a
given lift **iff** its left part is; the strong-right part can neither create a separation nor cancel
one. **So on `𝒪₁` there is no case of "the pair separates although neither part does".** -/
theorem pq3b_no_cancellation_on_anchoredChannel {a₀ : A} {K : Matrix (V × A) (V × A) ℂ}
    (hK : StrongAnchorStabilizer a₀ K) (W M : Matrix (V × A) (V × A) ℂ) :
    (∀ ρ : Matrix V V ℂ, AnchoredChannel a₀ (W * M * K) ρ = AnchoredChannel a₀ M ρ)
      ↔ ∀ ρ : Matrix V V ℂ, AnchoredChannel a₀ (W * M) ρ = AnchoredChannel a₀ M ρ := by
  constructor
  · intro h ρ
    rw [← pq3b_pair_factors_through_left hK W M ρ]
    exact h ρ
  · intro h ρ
    rw [pq3b_pair_factors_through_left hK W M ρ]
    exact h ρ

/-- **`PQ3` (c) — THE PAIR IS PHYSICAL RELATIVE TO `𝒪₂`, WITH BOTH PARTS NONTRIVIAL.** Act 13's
merged `CT4` lift and its constant `W ∈ 𝒢_L`, with the strong family `K_t = 𝟙` for `t ∈ {0,1}` and
`K_t = P(swap((0,1),(1,1)))` for `t ≥ 2`, which is strong because it fixes both anchored columns. So
`W ≠ 𝟙`, `K` is not constant in `t`, and the relative candidates at `(t,s) = (1,0)` are `CT4`'s, `1`
against `0`.

**This witness is deliberately cheap and is recorded as such: its strong family does no work at the
certified time pair.** The substantive question about the pair is the cancellation fork `PQ3` (d),
which this round leaves UNDECIDED, and which is **not** act 13's fork `CT3` (d).

**Act 7's boundary is carried**, as for every `𝒪₂` verdict. -/
theorem pq3c_pair_physical_relative_candidate :
    ∃ (Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ)
      (U U' K : ℕ → Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
      (W : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ),
      LeftFibreGroup W
        ∧ W ≠ 1
        ∧ (∀ t, StrongAnchorStabilizer (0 : Fin 2) (K t))
        ∧ (∃ t s : ℕ, K t ≠ K s)
        ∧ (∀ t, U' t = W * U t * K t)
        ∧ CoherentLift (0 : Fin 2) Γ U ∧ CoherentLift (0 : Fin 2) Γ U'
        ∧ ThreadingRelated (0 : Fin 2) U U'
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U 1 * (U 0)ᴴ) p q‖ ^ 2) 0 0 = 1
        ∧ readback (0 : Fin 2) (Matrix.of fun p q => ‖(U' 1 * (U' 0)ᴴ) p q‖ ^ 2) 0 0 = 0 := by
  classical
  obtain ⟨Γ, U, Uc, W, -, -, -, -, hWdef, hfac, hW, hcoh, hcoh', -, -, -, h1, h0⟩ :=
    ct4_constant_left_obstruction
  obtain ⟨ρ, hρ⟩ : ∃ ρ : Equiv.Perm (Fin 2 × Fin 2),
      ρ = Equiv.swap ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) := ⟨_, rfl⟩
  have hfix : ∀ p j, (ρ.permMatrix ℂ) p (j, (0 : Fin 2))
      = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro p j
    obtain ⟨x, y⟩ := p
    fin_cases x <;> fin_cases y <;> fin_cases j <;> simp +decide [hρ]
  have hKfix : ∀ t (p : Fin 2 × Fin 2) (j : Fin 2),
      (if t ≤ 1 then (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) else ρ.permMatrix ℂ)
        p (j, (0 : Fin 2)) = if p = (j, (0 : Fin 2)) then 1 else 0 := by
    intro t p j
    by_cases ht : t ≤ 1
    · rw [if_pos ht, Matrix.one_apply]
    · rw [if_neg ht]; exact hfix p j
  have hKunit : ∀ t,
      (if t ≤ 1 then (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) else ρ.permMatrix ℂ)
        ∈ Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ := by
    intro t
    by_cases ht : t ≤ 1
    · rw [if_pos ht]; exact one_mem _
    · rw [if_neg ht]; exact permMatrix_mem_unitaryGroup ρ
  have hK : ∀ t, StrongAnchorStabilizer (0 : Fin 2)
      (if t ≤ 1 then (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ) else ρ.permMatrix ℂ) :=
    fun t => ⟨hKunit t, hKfix t⟩
  have hUc : ∀ t, W * U t = Uc t := fun t => (hfac t).symm
  refine ⟨Γ, U,
    fun t => W * U t * (if t ≤ 1 then 1 else ρ.permMatrix ℂ),
    fun t => if t ≤ 1 then 1 else ρ.permMatrix ℂ, W, hW, ?_, hK, ?_, fun _ => rfl, hcoh, ?_,
    ⟨W, hW, fun t => if t ≤ 1 then 1 else ρ.permMatrix ℂ, hK, fun _ => rfl⟩, h1, ?_⟩
  · rw [hWdef]
    intro hcon
    have h00 := congrFun (congrFun hcon ((0 : Fin 2), (0 : Fin 2))) ((0 : Fin 2), (0 : Fin 2))
    rw [permMatrix_apply_eq, Matrix.one_apply] at h00
    simp +decide at h00
  · refine ⟨0, 2, ?_⟩
    simp only [if_pos (by norm_num : (0 : ℕ) ≤ 1), if_neg (by norm_num : ¬ (2 : ℕ) ≤ 1)]
    intro hcon
    have h01 := congrFun (congrFun hcon ((0 : Fin 2), (1 : Fin 2))) ((1 : Fin 2), (1 : Fin 2))
    rw [Matrix.one_apply, permMatrix_apply_eq] at h01
    simp +decide [hρ] at h01
  · intro t
    show AdmissibleDilationAt (Γ t) 0 (W * U t * (if t ≤ 1 then 1 else ρ.permMatrix ℂ))
    rw [hUc t]
    exact admissible_mul_of_fixes_anchor (hcoh' t) (hKunit t) (hKfix t)
  · have e1 : W * U 1 * (if (1 : ℕ) ≤ 1 then 1 else ρ.permMatrix ℂ) = Uc 1 := by
      rw [if_pos (le_refl 1), Matrix.mul_one, hUc]
    have e0 : W * U 0 * (if (0 : ℕ) ≤ 1 then 1 else ρ.permMatrix ℂ) = Uc 0 := by
      rw [if_pos (by norm_num : (0 : ℕ) ≤ 1), Matrix.mul_one, hUc]
    show readback (0 : Fin 2) (Matrix.of fun p q =>
        ‖((W * U 1 * (if (1 : ℕ) ≤ 1 then 1 else ρ.permMatrix ℂ))
          * (W * U 0 * (if (0 : ℕ) ≤ 1 then 1 else ρ.permMatrix ℂ))ᴴ) p q‖ ^ 2) 0 0 = 0
    rw [e1, e0]
    exact h0

/-! ### Section H — `PQ4`: the constant-left reduction, in the one direction it has -/

/-- **`PQ4` (b) — A CARRIER READING ONLY WITHIN-FIBRE DATA CANNOT SEPARATE THE CONSTANT-LEFT PART.**
The constant-left part preserves every fibre-Gram matrix (act 12's merged `fibreGram_left_mul`), so
**a carrier separates it only if that carrier reads relations between the hidden fibres of distinct
visible outcomes**.

**The converse is not claimed:** reading such data is not shown sufficient to separate this part, and
no theorem here says it is. This is a reduction of one open question to another; it names no datum
and no principle. -/
theorem pq4b_within_fibre_carrier_blind_to_constant_left {β : Type}
    (𝒪 : (V → Matrix V V ℂ) → β) {W : Matrix (V × A) (V × A) ℂ} (hW : LeftFibreGroup W)
    (a₀ : A) (M : Matrix (V × A) (V × A) ℂ) :
    𝒪 (fun i => CrossFibreGram a₀ (W * M) i i) = 𝒪 (fun i => CrossFibreGram a₀ M i i) := by
  have h : (fun i => CrossFibreGram a₀ (W * M) i i) = fun i => CrossFibreGram a₀ M i i :=
    funext fun i => pq0c_crossFibreGram_left_mul_diag hW a₀ M i
  rw [h]

end ThreadingObservability
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.ThreadingObservability.crossFibreGram_apply
#print axioms OIBridge.ThreadingObservability.crossFibreGram_diag
#print axioms OIBridge.ThreadingObservability.anchoredChannel_apply
#print axioms OIBridge.ThreadingObservability.anchoredChannel_block
#print axioms OIBridge.ThreadingObservability.anchoredChannel_eq_trace
#print axioms OIBridge.ThreadingObservability.trace_unit_mul
#print axioms OIBridge.ThreadingObservability.anchoredChannel_unit
#print axioms OIBridge.ThreadingObservability.anchoredCol_gram
#print axioms OIBridge.ThreadingObservability.anchoredCol_isometry
#print axioms OIBridge.ThreadingObservability.pq0a_readback_is_diagonal_action
#print axioms OIBridge.ThreadingObservability.pq0b_anchoredChannel_diagonal_is_visible
#print axioms OIBridge.ThreadingObservability.pq0c_anchoredCol_mul_strong
#print axioms OIBridge.ThreadingObservability.pq0c_anchoredChannel_mul_strong
#print axioms OIBridge.ThreadingObservability.pq0c_crossFibreGram_mul_strong
#print axioms OIBridge.ThreadingObservability.pq0c_crossFibreGram_left_mul
#print axioms OIBridge.ThreadingObservability.pq0c_crossFibreGram_left_mul_diag
#print axioms OIBridge.ThreadingObservability.pq0d_anchoredChannel_trace_preserving
#print axioms OIBridge.ThreadingObservability.threadingRelated_iff_fibreCrossGram
#print axioms OIBridge.ThreadingObservability.threadingRelated_of_constLeft
#print axioms OIBridge.ThreadingObservability.threadingRelated_of_strongRight
#print axioms OIBridge.ThreadingObservability.pq1a_constant_left_redundant_visible
#print axioms OIBridge.ThreadingObservability.pq1b_constant_left_physical_anchoredChannel
#print axioms OIBridge.ThreadingObservability.pq1c_constant_left_physical_relative_candidate
#print axioms OIBridge.ThreadingObservability.uniformLeft_block
#print axioms OIBridge.ThreadingObservability.pq1d_plus_uniform_left_redundant_anchoredChannel
#print axioms OIBridge.ThreadingObservability.nonuniform_left_block_witness
#print axioms OIBridge.ThreadingObservability.crossFibreGram_mul_permMatrix
#print axioms OIBridge.ThreadingObservability.pq1d_minus_nonuniform_left_physical_anchoredChannel
#print axioms OIBridge.ThreadingObservability.pq2a_strong_right_redundant_visible
#print axioms OIBridge.ThreadingObservability.pq2b_anchored_column_identity
#print axioms OIBridge.ThreadingObservability.pq2b_every_single_time_anchored_carrier
#print axioms OIBridge.ThreadingObservability.pq2b_strong_right_redundant_anchoredChannel
#print axioms OIBridge.ThreadingObservability.pq2b_strong_right_crossFibreGram
#print axioms OIBridge.ThreadingObservability.pq2c_strong_right_physical_relative_candidate
#print axioms OIBridge.ThreadingObservability.pq3a_pair_redundant_visible
#print axioms OIBridge.ThreadingObservability.pq3b_pair_factors_through_left
#print axioms OIBridge.ThreadingObservability.pq3b_no_cancellation_on_anchoredChannel
#print axioms OIBridge.ThreadingObservability.pq3c_pair_physical_relative_candidate
#print axioms OIBridge.ThreadingObservability.pq4b_within_fibre_carrier_blind_to_constant_left
