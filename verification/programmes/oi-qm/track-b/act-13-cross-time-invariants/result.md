# Track B act 13 — cross-time invariants of the relative evolution: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`5d8bee2c616d12c53234c54bfa7efae19dc1dcc1`, merged into `main` as
`d019718696fd12e4719b5ed5b7d8dfab45544a8c` (PR #602) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `d019718696fd12e4719b5ed5b7d8dfab45544a8c` (merge of PR #602) |
| This round's frozen control plane | `preregistration.md`, blob `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| Act 12's control plane | `../act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| Act 12's result (`LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`) | `../act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 12's module (`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`) | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's control plane | `../act-11-coherent-lift-gauge/preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 11's module (`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative`) | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| Act 10's control plane (the strengthened chronology mechanism) | `../act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| Act 7 layer 2's module (`readback`, `AdmissibleDilationAt`, `admissible_permMatrix`, `admissible_mul_of_fixes_anchor`) | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 7's governing preregistration (incl. `D3`) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| The live queue, `P0` row as act 12 left it | `verification/ROADMAP.md`, blob `5aa4235bf895b7c114feff406cc156d117bdb755` |
| This round's module | `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` |

**Every blob in the freeze's start-state table is present at the mandated base with the SHA the
freeze records; no discrepancy is recorded.** The freeze's first row names `main` at `aa4ac3a`
(PR #599) as the merged state at freeze time; the mandated base `d019718` is the merge of the
control-plane PR itself, exactly as the chronology control's clause 2 requires, and the two are
different objects by construction, not a discrepancy.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Outcome, in one line

**`CT1`, `CT2` (a) and (b) in both directions, `CT3` (G), (a), (b), (c) and `CT4` with `CL1` all
landed at evidence level 2, `CT2` (b) forward at kernel level — the frozen fallback was not used —
and the fork `CT3` (d) is UNDECIDED, as the freeze permits.** This is the freeze's **Case A** with
the fork clause adding nothing. Nothing moved from its predicted strength except `CT2` (b) forward,
which was predicted at medium and reached at full, through an infinite-family Gram-isometry lemma
stated for an arbitrary index type.

## The structural point, as frozen

**The two-sided action of act 12 does not act on relative evolutions.** `TwoSidedRelated` is
time-dependent on both sides; a time-dependent right factor changes relative objects (`GL2`) and a
time-dependent left factor changes them (`RO1`). The quotient in which the relative evolution lives
is the lift modulo a **constant right** unitary — any unitary, not a gauge class — and that is
`CT1`. Every "determines the relative evolution" below means "determines the lift modulo constant
right unitaries", and every "determines up to" names the exact quotient it means. Nothing in act
12's merged record is revised.

**Level 0 is read at two strengths, kept apart exactly as the freeze says.** The **raw** reading is
entrywise equality of the per-time fibre-Gram trajectory; the **phase-quotiented** reading is act
12's `GramPhaseEquiv` at every `t` and every `i`. The cross-time weak transformation law
`fibreCrossGram_mul_weak_apply` — `(Ξ_i^{(t,s)})_{jk} ↦ conj(c^t_j) (Ξ_i^{(t,s)})_{jk} c^s_k` —
shows that a weak right move with anchored phases moves the raw datum, so **raw level-0 equality is
not invariant under the whole weak-right action and does not itself compute act 12's per-slice
quotient**; what computes that quotient exactly is the phase-equivalence class of the level-0 datum
(`TG2`, both directions, consumed). Raw level-0 equality is the stronger, representative-level
equality: sufficient to place two slices in one two-sided orbit, not implied by membership in it.

## `CT1` — the exact quotient of the relative evolution

`ConstRightRelated`, `constRight_forced`, `ct1_forward`, `ct1_backward`,
`ct1_relative_iff_constRight`.

For unitary lifts, `(∀ t s, U'_t U'_sᴴ = U_t U_sᴴ) ⟺ U' ≈_R U`, both directions, with the directional
witnesses named separately:

- **forward, this round's** — `ct1_forward`: the one forced element `K = U_0ᴴ U'_0` is unitary and
  `U'_t = U_t K` for every `t`, by `U'_t = U'_t U'_0ᴴ U'_0 = U_t U_0ᴴ U'_0`;
- **backward, consumed** — `ct1_backward` is act 11's merged `gl3_constant_gauge_preserves_relative`
  applied and renamed, nothing more;
- the relating element is forced (`constRight_forced`), so membership is a computation.

**Bounded reading, as frozen:** the relative evolution is the lift modulo constant right unitaries,
and the threading question of `P0` is exactly the question of what pins a lift modulo constant right
unitaries. **`CT1` does not say what pins it.** The constant is not restricted to a gauge class,
and cannot be: `GI2`'s pair has identical relative objects with a constant relating element outside
`𝒢ʷ_{a₀}`.

## `CT2` — what each level of the column-Gram family determines

`CrossGram`, `FibreCrossGram`, `ConstLeftRelated`, `crossGram_apply`, `crossGram_self`,
`fibreCrossGram_apply`, `fibreCrossGram_apply_dotProduct`, `fibreCrossGram_diag`,
`sum_fibreCrossGram`, `crossGram_two_sided`, `crossGram_left_mul`, `crossGram_mul_right`,
`mul_strong_anchor_col`, `mul_strong_submatrix`, `fibreCrossGram_mul_weak_apply`, `constLeft_forced`,
`ct2a_forward`, `ct2a_backward`, `ct2a_crossGram_iff_constLeft`, `ct2a_relative_conj`,
`ct2b_backward`, `exists_unitary_of_inner_eq`, `ct2b_forward`, `ct2b_fibreCrossGram_iff`.

**The family, as frozen.** `CrossGram U t s = U_tᴴ U_s` is level 3, anchor-free, with identity
`(t,t)` slice (`crossGram_self`). `FibreCrossGram a₀ U i t s = X_i(U_t)ᴴ X_i(U_s)` is level 2,
carrying the anchor, with `(t,t)` slice act 12's `FibreGram a₀ (U t) i` **definitionally**
(`fibreCrossGram_diag` is `rfl`), so level 0 is the diagonal of level 2. Level 1 is the fibre sum of
level 2 and the anchored block of level 3 (`sum_fibreCrossGram`), a submatrix expression and not a
definition. The two-sided transformation law `Ξ ↦ K_tᴴ (U_tᴴ L_tᴴ L_s U_s) K_s` is
`crossGram_two_sided`; a time-dependent left factor survives as `L_tᴴ L_s`.

**(a) Level 3, both directions at level 2.** `ct2a_crossGram_iff_constLeft`: for unitary lifts,
`(∀ t s, Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U)) ⟺ U' ≈_L U`. Forward (`ct2a_forward`) by the forced element
`W = U'_0 U_0ᴴ`: from `U'_tᴴ U'_0 = U_tᴴ U_0`, conjugate-transpose and multiply on the left by
`U'_0`. Backward (`ct2a_backward`, the first transformation law `crossGram_left_mul`):
`(W U_t)ᴴ (W U_s) = U_tᴴ U_s`. **Consequence, stated exactly** (`ct2a_relative_conj`): the column
cross-Gram determines the lift up to one constant left unitary, hence the relative evolution up to
**conjugation by one constant unitary**, `U'_t U'_sᴴ = W (U_t U_sᴴ) Wᴴ`. That quotient is finer than
act 12's two-sided one and is **not** the identity on relative candidates — `CT4` is the
certificate. "Determines the lift up to `≈_L`" and "determines the relative candidate" are different
claims, and only the first is made.

**(b) Level 2, both directions at level 2.** `ct2b_fibreCrossGram_iff`: for unitary lifts,
`(∀ i t s, Ξ_i^{(t,s)}(U') = Ξ_i^{(t,s)}(U)) ⟺ ∃ W, LeftFibreGroup W ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U'`.

- **Backward** (`ct2b_backward`), the second transformation law: the anchored fibre columns of
  `W U_t K_t` are `W_i` times those of `U_t` (`mul_strong_submatrix`, act 12's
  `left_mul_submatrix`), and `W_iᴴ W_i = 1` (act 12's `left_block_unitary`).
- **Forward** (`ct2b_forward`), **reached at kernel level; the frozen fallback is NOT used.** The
  load-bearing step is `exists_unitary_of_inner_eq`: act 12's Gram-isometry lemma freed from its
  finite index set — two families of vectors in `ℂ^A` indexed by **any** type `ι`, with the same
  pairwise inner products, are related by one unitary on `ℂ^A`. The map `∑ cₚ xₚ ↦ ∑ cₚ yₚ` is
  well defined on the span and isometric there, because every inner product of finite linear
  combinations is a finite sum of the agreeing pairwise inner products; the span is a subspace of
  the finite-dimensional `ℂ^A`, and Mathlib's `LinearIsometry.extend` extends the isometry. Nothing
  assumes the family is finite, spanning or independent, so no finite-spanning-subfamily reduction
  was needed. For each fibre `i` the `ℕ × V`-indexed families `{P_i U_t e_{(j,a₀)}}` and
  `{P_i U'_t e_{(j,a₀)}}` have the same inner products, exactly the level-2 hypothesis
  (`fibreCrossGram_apply_dotProduct`); the fibre unitaries `W_i` assemble into `W ∈ 𝒢_L` with
  `U'_t e_{(j,a₀)} = W U_t e_{(j,a₀)}` for every `t` and `j`; and act 11's
  `gaugeRelated_strong_iff_agree_on_anchor` absorbs the off-anchor freedom into a time-dependent
  strong element. **The forward direction rides on that one lemma and act 11's orbit theorem**,
  exactly as frozen.

**Consequence, stated exactly:** the fibre cross-Gram trajectory determines the lift up to a
**constant** in-fibre left move and a **time-dependent strong** right gauge — its residual is exactly
`GL2`'s mechanism together with one constant `𝒢_L` conjugation, and nothing else. With `CT1`:
relative to the level-2 data, the threading freedom of `P0` is exactly a strong-right family `K_t`
modulo a constant, together with one constant in-fibre frame.

**The phase-quotiented corollary was not attempted.** The strict form landed, but no cross-time
phase-equivalence predicate was introduced (budget slot 5 unused), so the corollary replacing
"strong" by "weak" is not stated; the cross-time weak transformation law it would rest on,
`fibreCrossGram_mul_weak_apply`, is proved and serves the level-0 reading above.

**(c) The ladder sentence, asserted at full strength, since (a), (b) and `CT4` all landed:**

> **Level 0 modulo anchored phases classifies the per-slice two-sided orbit of act 12 at every time,
> so it determines the lift up to act 12's time-dependent two-sided action, with raw level-0
> equality a stronger representative-level equality; level 2 up to a constant in-fibre left move
> and a time-dependent strong right gauge; level 3 up to a constant left unitary. No level
> determines the relative candidate.**

The first clause is act 12's `TG2` applied slice by slice (`twoSidedRelated_iff`) and is consumed,
not re-proved; the last clause is `CT4`.

## `CT3` — separation and blindness on the merged witnesses

`ct3g_fibreCrossGram_strong_right`, `ct3g_fibreGram_strong_right`,
`ct3g_anchored_block_strong_right`, `strong_anchored_row`, `strong_pair_anchored_col`,
`ct3a_gl2_pair_separated_by_crossGram`, `ct3b_hadamard_trajectory_control`,
`ct3c_constant_lift_variant`.

**(G) Universal blindness of levels 0–2 to strong-right threading, at level 2.**
`ct3g_fibreCrossGram_strong_right`: for every lift `U`, every family `K` of strong elements and every
`i, t, s`, `Ξ_i^{(t,s)}(U·K) = Ξ_i^{(t,s)}(U)`; hence level 0 (`ct3g_fibreGram_strong_right`) and
level 1 (`ct3g_anchored_block_strong_right`) agree as well. This is the second transformation law
as a theorem: no function of the anchored-column data at any resolution separates any
strong-right-related pair, so **the least separating column-Gram datum for `GL2`-type pairs lies
outside the anchored block.**

**(a) `GL2`'s pair is separated by level 3, at an off-anchor row, at level 2.**
`ct3a_gl2_pair_separated_by_crossGram` re-exhibits act 11's pair with its matrices pinned by
equations in the statement — `U_0 = U_B`, `U_t = 𝟙` for `t ≥ 1`, `U'_0 = U_B P(ρ)`, `U'_t = 𝟙` for
`t ≥ 1`, `ρ = swap((0,1),(1,1))` — as two coherent lifts of one family related by a time-dependent
element of the **strong** class, and proves as conjuncts of the one theorem: every fibre
cross-Gram datum agrees (by (G)); **the certified entry is `((0,1),(1,1))` of `Ξ^{(0,1)}`, with
values `0` for `U` and `1` for `U'`**, the entry the freeze expected, computed under act 7's
convention through `mul_permMatrix_apply` and `permMatrix_mul_apply` and not read off; and the
relative candidates differ at `(0,1)`, `1/2` against `0`. The other separating entry the freeze
records, `((0,1),(1,0))` with values `−s` and `0`, was not certified and is not claimed. Together
with (G): **`GL2`'s pair shares every per-time Gram matrix, every level-1 and every level-2 datum,
and is separated by one off-anchor entry of `Ξ`.**

**(b) The Hadamard pair is the trajectory-type control, not a threading witness, at level 2.**
`ct3b_hadamard_trajectory_control` consumes act 12's `hadamard_lifts_not_twoSided` pair —
`U_t = H(1)`, `U'_0 = H(1)`, `U'_t = H(i)` for `t ≥ 1`, pinned by the same equations — and
`hadamard_slices_not_twoSided`: the two coherent lifts of one visible family have per-time Gram data
already **inequivalent** at `t = 1` (`¬ GramPhaseEquiv (FibreGram 0 (U 1)) (FibreGram 0 (U' 1))`,
consumed), so **the pair is not one sharing every per-time Gram matrix and is not presented as
one**. Its role is the control on the other part of `P0`: `Ξ^{(t,s)}(U) = 𝟙` for every `t, s`,
while `Ξ^{(0,1)}(U') = H(1)ᴴ H(i) ≠ 𝟙` — separated at the smallest level, because the difference is
a difference of Gram trajectory, not of threading. The certificate is the identity
`H(1)ᴴ H(i) = 𝟙 ⟹ H(i) = H(1)`, refuted at the entry `(1,1)`. That at `|A| = 1` every column is
anchored and the three levels coincide is the freeze's remark, not a theorem of this module.

**(c) The anchored columns of `Ξ` do not separate every `GL2`-type pair, at level 2.**
`ct3c_constant_lift_variant`: the constant-lift variant `U_t = U_B` for every `t`,
`U'_0 = U_B P(ρ)`, `U'_t = U_B` for `t ≥ 1`, pinned by equations — two coherent lifts of the
constant family `Bᵀ`, strong-right related and time-dependent exactly as in `GL2` — with, as
conjuncts of the one theorem: **every anchored column of `Ξ^{(t,s)}(U')` equal to the
corresponding column of `Ξ^{(t,s)}(U)` at every `t, s`** (`Ξ(U) = 𝟙` since the lift is constant,
`Ξ(U') = K_tᴴ K_s` whose anchored columns are the standard basis vectors by
`strong_pair_anchored_col`), so every level-2 datum and every off-anchor-row × anchored-column entry
agree; **the certified off-anchor × off-anchor entry `((0,1),(0,1))` of `Ξ^{(0,1)}`, values `1`
for `U` and `0` for `U'`**; and the relative candidates at `(0,1)`, **`0` against `1/4`** — the
value the freeze checked by hand, confirmed in the kernel: `U'_1 U'_0ᴴ = U_B P(ρ)ᴴ U_Bᴴ` carries
`e_{(1,0)}` to `½ e_{(0,1)} + ½ e_{(1,0)} − s e_{(1,1)}`. **So the least column-Gram datum separating
all `GL2`-type pairs is not the anchored-column block of `Ξ`; whether it is `Ξ` itself is the fork
(d).**

**(d) The fork — does level 3 separate every `GL2`-type pair? UNDECIDED.** Neither `CT3-d⁺` nor
`CT3-d⁻` was reached, and neither is claimed. The route to the label: by `CT2` (a) a
strong-right-related pair with equal `Ξ` at every `t, s` is constant-left related, `U' = C U` with
`U_tᴴ C U_t` strong for every `t`; `CT3-d⁺` would need a universal theorem that every such `C`
conjugates every relative object without moving its anchored readback, and `CT3-d⁻` would need an
exhibited pair satisfying the strong-right and `Ξ`-equality conjuncts with distinct candidates.
Neither was attempted in this round, and the constraint `U_tᴴ C U_t ∈ 𝒢ˢ_{a₀}` for all `t` is what
any witness must satisfy. `CT4`'s pair is not a candidate: its relating element is a constant left
`W ∈ 𝒢_L`, and the forced right element `U_tᴴ W U_t` is not strong at `t = 0`. **The fork clause
therefore adds nothing to the post-round sentence.**

## `CT4` with `CL1` — insufficiency of the whole family, by the constant-left obstruction

`ct4_constant_left_obstruction`, `cl1_constant_left_moves_relative_candidate`.

**`CT4`, at level 2.** On `V = Fin 2`, `A = Fin 2`, `a₀ = 0`, with the constant identity law, the
lifts `U_0 = 𝟙`, `U_t = X = P(swap((0,1),(1,1)))` for `t ≥ 1` and `U'_t = W U_t` with the
**constant** `W = P(swap((0,0),(0,1))) ∈ 𝒢_L`, pinned by equations, satisfy as conjuncts of the one
theorem:

- `|A| ≥ 2`, as the first conjunct, in the form act 12's `|V| ≥ 2` conjuncts take;
- both are coherent lifts of the identity family — `𝟙` by act 10's `one_admissible_at_every_anchor`,
  `X` by act 7's `admissible_permMatrix` since `X` fixes both anchored columns, `W U_t` by act 12's
  `left_preserves_admissible`;
- `U' ≈_L U` by the constant `W`, with `LeftFibreGroup W` (act 12's `inFibreSwap_leftFibreGroup`);
- **`Ξ^{(t,s)}(U') = Ξ^{(t,s)}(U)` for all `t, s`** (`ct2a_backward`), hence equal level-2, level-1
  and per-time Gram data (`ct2b_backward` with `K ≡ 𝟙`, both stated as conjuncts);
- **the relative candidates differ at the entry `(0,0)`: `1` against `0`.** `U_1 U_0ᴴ = X` fixes the
  anchored column `e_{(0,0)}`; `U'_1 U'_0ᴴ = W X Wᴴ` carries it to `e_{(1,1)}`, in the other visible
  fibre. The entries are integers, computed in the kernel.

**`CL1`, the mechanism, at level 2** (`cl1_constant_left_moves_relative_candidate`, a corollary of
`CT4`): a **constant** left `𝒢_L` move can change the relative candidate. This is the left
counterpart of `GL3` failing: `GL3` says a constant right gauge preserves every relative object; no
analogue holds on the left, even for the invisible group, because the readback of `W R Wᴴ` sees
`Wᴴ` on the input side. **`CL1` is existential and says nothing about every constant left move.**
`GI2`'s pair, a constant left move with identical relative objects, is not a counterexample to `CL1`
and `CL1` is not a revision of `GI2`: `GI2`'s lifts are constant in time, so `W R Wᴴ = W Wᴴ = 𝟙 = R`
there.

**Bounded reading of `CT4`, as frozen:** no member of the frozen family, up to and including the
full column cross-Gram, determines the relative candidate; any datum that does must fail to be
constant-left invariant, hence must depend on the dilation's rows, not only its columns. That is a
statement about the **shape** of a sufficient datum, not the naming of one; the row-Gram data
`U_t U_sᴴ` are the relative objects themselves and are not offered as an answer.

**`|A| = 1` is out of `CT4`'s reach, and the scoping is part of the statement.** There `𝒢_L` is the
diagonal phases, conjugation by which preserves every entrywise modulus, so the relative candidate
is invariant under constant `𝒢_L` moves and `CT4`'s obstruction is absent. `CT4` needs `|A| ≥ 2`;
the witness has `|A| = 2`, and the `|A| ≥ 2` conjunct carries the scoping.

## The frozen post-round sentence for `P0` — Case A, the fork clause adding nothing

The `P0` row stays **OPEN**. The sentence appended to it, verbatim from the freeze:

> `P0` remains open and two-part, and the threading part is localized exactly: the fibre cross-Gram
> trajectory determines the lift up to one constant in-fibre left move and one time-dependent strong
> right gauge, and no column-Gram datum — up to and including the full two-time column Gram —
> determines the relative candidate, by a constant-left obstruction. The residual threading freedom
> relative to this datum is exactly a strong-right family modulo a constant together with one
> constant in-fibre frame; nothing in act 13 selects either, and no connection, gauge fixing or
> selection principle is asserted or excluded.

**No case closes `P0`.** A characterization of what the frozen family determines is not a selection
of anything, and the row's label does not change.

## What these outcomes do NOT license

- **No selection principle is named**, endorsed or excluded. The round determines what the frozen
  data compute; it does not say what fixes them.
- **No connection and no gauge-fixing mechanism is asserted**, in either direction. "The threading
  freedom is exactly a strong-right family modulo a constant together with a constant in-fibre
  frame" is a statement about a quotient, not about a rule that picks a representative.
- **`P0` is not closed by a characterization.** It remains OPEN and two-part in every case above;
  what moves is the precision of the second part.
- **Nothing here says OI and QM are inequivalent.** Two lifts differing is not two theories
  differing; the finite observable-law correspondence is untouched.
- **The cross-Gram data are coordinates on the lift space, not physical quantities**, exactly as
  act 12 said of the per-time Gram data.
- **Nothing is imported from the substratum Lemma 24.1 round.** Its block-word traces, its
  `ST` labels and its "multi-time information" remark are objects of a different programme on a
  different carrier; this round neither consumes nor compares them, and a resemblance of vocabulary
  is not a bridge.
- **Nothing about Track I.**
- **`D3`, `D5`, the direct-branch statement, and every merged label** are consumed unmodified.
  The direct-branch statement is exactly act 7's: `D4a` positive on the direct branch; `T1`
  **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
  fraction of OI lies in the direct sector.**

## The relation to acts 11 and 12, as frozen — consumed, none revised

- Act 11's `GL2` **stands as stated** and is consumed as the threading witness; `CT3` (a) and (c)
  add the cross-Gram entries that separate it and its constant-lift variant, and revise nothing.
- Act 11's `GL3` is consumed as the backward direction of `CT1`; `CL1` is its left counterpart
  failing, and does not touch `GL3`.
- Act 11's `GI2` is **not revised** by `CL1`: its constant lifts have `W R Wᴴ = R` for the trivial
  reason, and act 12's reading of it as a left in-fibre move with identical Gram data stands.
- Act 12's `TG2` is consumed as the **phase-quotiented** reading of level 0 of the ladder: it
  classifies the per-slice two-sided orbit by the phase-equivalence class of the per-time
  fibre-Gram datum, not by its raw value, which the weak-right action moves by `Dᴴ G D`. `CT2` (b)
  is the cross-time extension of the raw reading and rides on the same orbit theorem. Act 12's
  `TG3` is consumed as the trajectory-type control; the Hadamard pair is not presented as sharing
  per-time Gram data, because `TG3` proves it does not.
- Act 12's `RO1` is consumed as the time-dependent left move; `CL1` is the constant one.
- **No manuscript is edited by this round.** Whether to propagate the ladder is a separate owner
  call.

## The chronology control

**`R7-CTI` certifies the strong property**, reusing act 10's mechanism by name through act 12's and
the Lemma 24.1 round's copies, with the archive-mode scaffolding of PR #599 carried and its pins
**unset at execution**:

- the preregistration blob is pinned **by content** to `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = d019718696fd12e4719b5ed5b7d8dfab45544a8c` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it;
- **archive mode** (`_CTI_SEALED_HEAD`, `_CTI_MERGE`) is present and **unset**: after the merge, one
  pin-only change records the sealed execution head and its merge commit, and the guard re-runs the
  same strong check against that object per clause 7.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The claim is scoped to the repository record.

## Definition budget: **FOUR of the frozen six slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `CrossGram` | **fired** |
| 2 | `FibreCrossGram` | **fired** |
| 3 | `ConstRightRelated` | **fired** |
| 4 | `ConstLeftRelated` | **fired** |
| 5 (conditional) | a cross-time phase equivalence on fibre cross-Gram data | **unused** — the phase-quotiented corollary of `CT2` (b) was not attempted |
| 6 (conditional) | a relative-object or relative-candidate abbreviation | **unused** — `CT3` (d) is UNDECIDED and `CT4` is stated with the relative objects written out as `U t * (U s)ᴴ`, as act 11 writes them |

**No seventh definition was introduced**, and no lift, gauge element, witness, carrier, cross-Gram
value or pair is a top-level definition — each is a bound variable pinned by an equation in the
statement that needs it, as acts 10, 11 and 12 did. Act 7's, act 11's and act 12's definitions are
reused, not redefined. The level-1 anchored block is a submatrix expression of slot 1 and a fibre
sum of slot 2, not a definition.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Thirty-five named results, **no unproved declaration, no
added axiom, no kernel-bypassing decision procedure**, every one printing only
`[propext, Classical.choice, Quot.sound]`:

| Result | Axioms |
| --- | --- |
| `crossGram_apply` | `[propext, Classical.choice, Quot.sound]` |
| `crossGram_self` | `[propext, Classical.choice, Quot.sound]` |
| `fibreCrossGram_apply` | `[propext, Classical.choice, Quot.sound]` |
| `fibreCrossGram_apply_dotProduct` | `[propext, Classical.choice, Quot.sound]` |
| `fibreCrossGram_diag` | `[propext, Classical.choice, Quot.sound]` |
| `sum_fibreCrossGram` | `[propext, Classical.choice, Quot.sound]` |
| `crossGram_two_sided` | `[propext, Classical.choice, Quot.sound]` |
| `crossGram_left_mul` | `[propext, Classical.choice, Quot.sound]` |
| `crossGram_mul_right` | `[propext, Classical.choice, Quot.sound]` |
| `mul_strong_anchor_col` | `[propext, Classical.choice, Quot.sound]` |
| `mul_strong_submatrix` | `[propext, Classical.choice, Quot.sound]` |
| `fibreCrossGram_mul_weak_apply` | `[propext, Classical.choice, Quot.sound]` |
| `ct3g_fibreCrossGram_strong_right` | `[propext, Classical.choice, Quot.sound]` |
| `ct3g_fibreGram_strong_right` | `[propext, Classical.choice, Quot.sound]` |
| `ct3g_anchored_block_strong_right` | `[propext, Classical.choice, Quot.sound]` |
| `constRight_forced` | `[propext, Classical.choice, Quot.sound]` |
| `constLeft_forced` | `[propext, Classical.choice, Quot.sound]` |
| `ct1_forward` | `[propext, Classical.choice, Quot.sound]` |
| `ct1_backward` | `[propext, Classical.choice, Quot.sound]` |
| `ct1_relative_iff_constRight` | `[propext, Classical.choice, Quot.sound]` |
| `ct2a_forward` | `[propext, Classical.choice, Quot.sound]` |
| `ct2a_backward` | `[propext, Classical.choice, Quot.sound]` |
| `ct2a_crossGram_iff_constLeft` | `[propext, Classical.choice, Quot.sound]` |
| `ct2a_relative_conj` | `[propext, Classical.choice, Quot.sound]` |
| `ct2b_backward` | `[propext, Classical.choice, Quot.sound]` |
| `exists_unitary_of_inner_eq` | `[propext, Classical.choice, Quot.sound]` |
| `ct2b_forward` | `[propext, Classical.choice, Quot.sound]` |
| `ct2b_fibreCrossGram_iff` | `[propext, Classical.choice, Quot.sound]` |
| `strong_anchored_row` | `[propext, Classical.choice, Quot.sound]` |
| `strong_pair_anchored_col` | `[propext, Classical.choice, Quot.sound]` |
| `ct3a_gl2_pair_separated_by_crossGram` | `[propext, Classical.choice, Quot.sound]` |
| `ct3b_hadamard_trajectory_control` | `[propext, Classical.choice, Quot.sound]` |
| `ct3c_constant_lift_variant` | `[propext, Classical.choice, Quot.sound]` |
| `ct4_constant_left_obstruction` | `[propext, Classical.choice, Quot.sound]` |
| `cl1_constant_left_moves_relative_candidate` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It revises no merged result.** Act 12's `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1` and
  `SH1-C2`; act 11's `GL1s`, `GL1w`, `GL2`, `GL3` and `GI2`; act 10's `AB0-A`/`AB0-B` and
  `one_admissible_at_every_anchor`; act 9's `RB3`/`RB1-A`/`RB1-B`; act 8's `CE1`; act 7's `DC1`,
  `DC2a`, `D4a`, `D4b` and `admissible_mul_of_fixes_anchor` — all cited and consumed unmodified.
- **Act 7 layer 2's `D5` chronological-ordering control stands NOT CERTIFIED.** Nothing here repairs
  it retroactively, and nothing here depends on it. Act 7's `D3` existence/regularity audit remains
  separately open and unused.
- **It names, endorses and excludes no selection principle**, asserts and denies no connection or
  gauge fixing, proposes no sufficient cross-time datum, adopts no datum outside the frozen
  column-Gram family, and introduces no regularity, homogeneity, generated evolution or source-level
  coherence. `CoherentLift` stays `ℕ`-indexed.
- **It does not name a smallest sufficient datum.** `CT3` bounds what separates the merged
  witnesses; `CT4` says no member of the family is sufficient; the shape remark is a consequence of
  `CT4`, not a proposal.
- **It compares Source A with neither Source B nor Source C**, on any axis.
- **It touches no manuscript.** Whether to propagate the ladder is a separate owner call.
- **It says nothing about Track I**, and nothing here is evidence for anything there.
