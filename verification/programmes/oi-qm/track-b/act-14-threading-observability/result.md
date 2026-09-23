# Track B act 14 — is the residual threading freedom redundancy or physical: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`1b16008470bb1e2456c57aad58421a5941a55e0c`, merged into `main` as
`bc76a88dbe300a35715d5ce8196002f31aa62493` (PR #621) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `bc76a88dbe300a35715d5ce8196002f31aa62493` (merge of PR #621) |
| This round's frozen control plane | `preregistration.md`, blob `1b16008470bb1e2456c57aad58421a5941a55e0c` |
| Act 13's control plane | `../act-13-cross-time-invariants/preregistration.md`, blob `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| Act 13's result (`CT1`, `CT2`, `CT3`, `CT4`, `CL1`) | `../act-13-cross-time-invariants/result.md`, blob `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| Act 13's module | `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, blob `47eb21e22845f0319926227c80d0d7f2f033880b` |
| Act 12's control plane | `../act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| Act 12's result (`LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`) | `../act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 12's module | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's control plane | `../act-11-coherent-lift-gauge/preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 11's module | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| Act 10's control plane (the strengthened chronology mechanism) | `../act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| Act 7 layer 2's module | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 7's governing preregistration (incl. `D3`, `D4b`, the readback amendment) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| The live queue, `P0` row as act 13 left it | `verification/ROADMAP.md`, blob `8f3f9b7758bffc86ba4b2888761770fb1881a180` |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `c7e9827c6eb2be9ac7cb660f964d5b610eb3411c` |
| This round's module | `verification/lean-mathlib/OIBridge/ThreadingObservability.lean` |

**Every blob in the freeze's start-state table is present at the mandated base with the SHA the
freeze records.** The freeze's first row names `main` at `7f130c3` (PR #620) as the merged state at
freeze time; the mandated base `bc76a88` is the merge of the control-plane PR itself, exactly as the
chronology control's clause 2 requires, and the two are different objects by construction, not a
discrepancy.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Outcome, in one line

**`PQ0` (a)–(d), `PQ1` (a)–(c), `PQ1` (d) in both halves — `PQ1-d⁻` reached at evidence level 2, so
the frozen fallback was not used — `PQ2` (a)–(c), `PQ3` (a)–(c) and `PQ4` all landed at evidence
level 2, and the fork `PQ3` (d) is UNDECIDED, as the freeze permits.** This is the freeze's
**Case A** with the fork clause adding nothing. Nothing moved from its predicted strength except
`PQ1-d⁻`, which was predicted at medium and reached at full, through a permutation lift over
arbitrary finite `V` and `A`.

**The verdict is carrier-dependent, and that is the round's substantive content.** The two parts of
the residual freedom behave differently on the same carrier, and the same part behaves differently on
different carriers. **No carrier is adopted as the physical one, and none is asserted not to be.**

## The structural point, as frozen

**The residual freedom act 13 localized is not one object; it is a pair of parts with different
transformation behaviour, and no sentence of this note quantifies over "the freedom" without saying
which part.** Act 13's `CT2` (b) delivers

```
U' ≈_T U   ⟺   ∃ W, LeftFibreGroup W ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U'
```

— `U'_t = W · U_t · K_t` with `W ∈ 𝒢_L` **constant** and `K_t` **strong** and time-dependent — and
the two parts act as follows, both proved here as derivations rather than asserted:

- **the strong right factor changes no anchored column, at any time.** `pq2b_anchored_column_identity`
  proves `C(U_t K_t) = C(U_t)`, the anchored column family **identical** and not merely equal after
  some functional is applied.
- **the constant left factor changes every anchored column by one constant in-fibre unitary.**
  `pq0c_crossFibreGram_left_mul` gives `Y_{i i'}(W M) = X_i(M)ᴴ W_iᴴ W_{i'} X_{i'}(M)`, and
  `pq0c_crossFibreGram_left_mul_diag` gives `Y_{i i}(W M) = FibreGram a₀ M i`: the diagonal is fixed,
  the off-diagonal cross-fibre blocks are not.

**So the question "is the residual threading freedom redundancy or physical" splits at the outset**,
and the split is along the axis of which data a carrier reads. **Nothing in acts 11, 12 or 13 is
revised by any of this**: `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`–`CT4` and
`CL1` are consumed as the statements they are.

## The four carriers, and the fact that none is adopted

A **carrier of observables** `𝒪` is a map from coherent lifts to values, together with a recorded
reason for regarding its values as observations rather than as coordinates on the lift space; the
quotient by `𝒪` is `U ≈_𝒪 U' ⟺ 𝒪(U) = 𝒪(U')`; a subrelation of `≈_T` is **redundancy relative to
`𝒪`** iff every pair it relates is `≈_𝒪`-equivalent and **physical relative to `𝒪`** iff some pair it
relates is not. **These are the only two predicates used below, and each is always carrier-indexed.**
"Invisible" keeps acts 11 and 12's meaning — preserving the visible marginal of every admissible
dilation — and is not used as a synonym for either.

| | probabilities only | full anchored channel |
| --- | --- | --- |
| **one time** | `𝒪₀` — the visible carrier | `𝒪₁` — the anchored-channel carrier |
| **re-anchored two-time** | `𝒪₂` — the relative-candidate carrier | `𝒪₃` — the re-anchored-channel carrier |

**`𝒪₀`, the visible carrier.** `𝒪₀(U) = (t ↦ readback a₀ (U_t.map ‖·‖²))`. *Presupposes:* only that
the observer's data is the stochastic family the lift is admissible for. *Standing:* the datum the
framework's own admissibility condition pins, and the one carrier here whose observational status
nothing in the tree disputes. *What adopting it would cost:* by construction every coherent lift of
one visible family is `≈_{𝒪₀}`-equivalent to every other, so `𝒪₀` identifies act 12's `TG3` pair —
proved to lie in **different** two-sided orbits with different relative evolutions — and dissolves
the whole of `P0`, not only its threading part. **The round records that consequence and does not
adopt the carrier.**

**`𝒪₁`, the anchored-channel carrier.** `𝒪₁(U) = (t ↦ 𝔇_{a₀}(U_t))`, this round's
`AnchoredChannel`. *Presupposes:* that the reduced quantum description of the visible system after
one preparation at the anchored ancilla configuration is physical, **including its off-diagonal
entries in the fixed visible basis, not only its diagonal**. *Standing:* the standard notion of what
is physical about a dilation when the ancilla is not — what survives tracing the ancilla out.
**No claim is made that it is the finest such carrier**, and none is needed:
`pq2b_every_single_time_anchored_carrier` bounds every carrier definable from single-time anchored
data at once, named or not. *What is not claimed for it:* that the established correspondence's
fixed-basis representation makes an off-diagonal entry an observation **at a single time**. The
correspondence gives the visible law; the coherences are the carrier's presupposition, and this note
says so rather than assuming it.

**`𝒪₂`, the relative-candidate carrier.** `𝒪₂(U) = ((t,s) ↦ readback a₀ ((U_t U_sᴴ).map ‖·‖²))`.
*Presupposes:* that the relative object may be read back through act 7's frozen map, hence that
re-anchoring the ancilla to `a₀` at the conditioning time `s` is a physical operation. *Standing,
at act 7's own strength:* act 7's `D4b` came back **negative** — Source A supplies no general map
carrying the relative candidate on the dilated carrier back to `V` — and the readback used is the
repository's own, frozen by act 7's readback amendment. **Every `𝒪₂` verdict below is a verdict
under that convention, and this note says so at each use.**

**`𝒪₃`, the re-anchored-channel carrier.** `𝒪₃(U) = ((t,s) ↦ 𝔇_{a₀}(U_t U_sᴴ))`. *Presupposes:* both
of the previous two. *Role:* the carrier on which "the pair is separated although neither part is"
could in principle live, and where the cancellation fork is asked.

**None of the four is adopted as the physical one, and none is asserted not to be.** Each verdict is
reported with its carrier and with that carrier's presupposition, and **no verdict travels**: a
redundancy verdict on one carrier is never reported as evidence of redundancy on another, and a
separation on one is never reported as a separation on another.

**The four are not a ladder ordered by resolution.** Only two refinements are proved — `𝒪₀` is the
diagonal action of `𝒪₁` and `𝒪₂` is the diagonal action of `𝒪₃` (`PQ0` a) — and **no implication
between the one-time row and the re-anchored row is asserted in either direction.**

**Deliberately not frozen as a carrier, and recorded as choices rather than oversights:**
sequential-measurement statistics, which would need a measurement model the tree does not contain
and which the round is forbidden to supply — **no claim is made about what such a carrier would
say**; and representative-level data — the anchored column family, the cross-Gram family, the
fibre-Gram trajectory — which are coordinates on the lift space, exactly as act 12 and act 13 said of
the Gram data.

## `PQ0` — the carriers, and the bridge to the merged readback

`AnchoredChannel`, `CrossFibreGram`, `crossFibreGram_apply`, `crossFibreGram_diag`,
`anchoredChannel_apply`, `anchoredChannel_block`, `anchoredChannel_eq_trace`, `trace_unit_mul`,
`anchoredChannel_unit`, `anchoredCol_gram`, `anchoredCol_isometry`,
`pq0a_readback_is_diagonal_action`, `pq0b_anchoredChannel_diagonal_is_visible`,
`pq0c_anchoredCol_mul_strong`, `pq0c_anchoredChannel_mul_strong`, `pq0c_crossFibreGram_mul_strong`,
`pq0c_crossFibreGram_left_mul`, `pq0c_crossFibreGram_left_mul_diag`,
`pq0d_anchoredChannel_trace_preserving`.

**The objects.** `AnchoredChannel a₀ M ρ i i' = ∑_a (C(M) ρ C(M)ᴴ)_{(i,a),(i',a)}` for the anchored
column family `C(M) = M.submatrix id (·, a₀)`, which is a submatrix **expression** and not a
definition; `CrossFibreGram a₀ M i i' = X_i(M)ᴴ X_{i'}(M)`, whose `i' = i` diagonal is act 12's
`FibreGram a₀ M i` **definitionally** (`crossFibreGram_diag` is `rfl`). The closed form
`𝔇_{a₀}(M)(ρ)_{i i'} = Tr(ρ · Y_{i' i}(M))` (`anchoredChannel_eq_trace`) is the identity every later
statement about the anchored channel is proved through, so **the anchored channel is a function of
the cross-fibre Gram and of nothing else**.

**(a) The readback is the diagonal action of the anchored channel, at level 2.**
`pq0a_readback_is_diagonal_action`: for every matrix over the carrier and all `i, j`,
`readback a₀ (M.map ‖·‖²) i j = (𝔇_{a₀}(M)(E_{jj}))_{i i}`. Hence `𝒪₀` is the diagonal action of
`𝒪₁`, and `𝒪₂` is the diagonal action of `𝒪₃` by taking `M = U_t U_sᴴ`. **Bounded reading:** this
says the two new carriers restrict to merged objects; **it does not say either new carrier is
observable.**

**(b) The anchored channel's diagonal is the visible law, at level 2.**
`pq0b_anchoredChannel_diagonal_is_visible`: for an admissible `U_t`,
`(𝔇_{a₀}(U_t)(E_{jj}))_{ii} = Γ_t(i,j)`, through act 12's merged `fibreGram_diag_of_admissible`,
consumed.

**(c) The transformation laws, as theorems, at level 2.** `C(M K) = C(M)` and
`𝔇_{a₀}(M K) = 𝔇_{a₀}(M)` for strong `K`; `Y_{i i'}(M K) = Y_{i i'}(M)` for **every** pair of
fibres, which **adds to** act 13's `CT3` (G) and revises nothing;
`Y_{i i'}(W M) = X_i(M)ᴴ W_iᴴ W_{i'} X_{i'}(M)` and `Y_{i i}(W M) = FibreGram a₀ M i` for `W ∈ 𝒢_L`,
the latter act 12's merged `fibreGram_left_mul` consumed.

**(d) The anchored channel is trace-preserving on a unitary, at level 2.**
`pq0d_anchoredChannel_trace_preserving`: `Tr 𝔇_{a₀}(M)(ρ) = Tr ρ` for every `ρ`, because
`C(M)ᴴ C(M) = ∑_i Y_{i i}(M) = ∑_i FibreGram a₀ M i` is the identity (`anchoredCol_gram` with act
12's merged `sum_fibreGram`, consumed). **This is what earns the word *channel* for `𝔇_{a₀}` rather
than asserting it**, and it applies to `𝒪₃` as well, each relative object `U_t U_sᴴ` being unitary.
**It is not a claim that the channel is observable**; that remains `𝒪₁`'s and `𝒪₃`'s recorded
presupposition. **Complete positivity was not free and is not stated**, as the freeze's conditional
allows; the `C ρ Cᴴ` form is in the kernel as `anchoredChannel_block` and nothing is claimed beyond
it.

## `PQ1` — the constant in-fibre left move, carrier by carrier

**(a) Relative to `𝒪₀`: redundancy, at level 2.** `pq1a_constant_left_redundant_visible`: for every
`W ∈ 𝒢_L` and every coherent lift, `W · U` is a coherent lift of the same visible family and
`𝒪₀(W·U) = 𝒪₀(U)`. Consumed from act 12's merged `left_preserves_admissible`, whose mechanism is
`fibreGram_left_mul`.

**(b) Relative to `𝒪₁`: physical, at level 2.** `pq1b_constant_left_physical_anchoredChannel`, all
conjuncts of one theorem, on `V = Fin 2`, `A = Fin 2`, `a₀ = 0`, with the matrices pinned by
equations in the statement:

- `|A| ≥ 2`, as the first conjunct, in the form act 12's and act 13's `|V| ≥ 2` and `|A| ≥ 2`
  conjuncts take;
- the constant identity law `Γ_t = 𝟙` and the constant identity lift `U_t = 𝟙`, coherent by act 10's
  merged `one_admissible_at_every_anchor`; the constant in-fibre swap
  `W = P(swap((0,0),(0,1))) ∈ 𝒢_L` by act 12's merged `inFibreSwap_leftFibreGroup`; and
  `U'_t = W U_t` coherent for the **same** family by act 12's merged `left_preserves_admissible`;
- `U' ≈_T U`, with the strong family trivial;
- **the named input is `ρ = ½ · J`, the uniform visible superposition; the named time is `t = 0`; the
  named entry is the coherence `(0,1)`; and the certified values are `1/2` for `U` against `0` for
  `U'`** — and the separation is stated **with the modulus**, `‖𝔇_{a₀}(U'_0)(ρ)_{01}‖ ≠
  ‖𝔇_{a₀}(U_0)(ρ)_{01}‖`, so it survives any quotient of `𝒪₁` by a rephasing of the visible basis;
- **both diagonals agree at every visible outcome**, `½` at each, which is the identity law, and the
  two visible readbacks are equal at every time.

The certified matrices `𝟙` and `W` are act 13's merged `CT4` pair at `t = 0`; **`CT4` is consumed
unmodified and this adds two channel entries on the same pair.** The permutation arithmetic is
computed under act 7's convention `P(σ)_{pq} = if q = σ p then 1 else 0`, not read off a constructor.

**`|A| ≥ 2` is part of the statement.** At `|A| = 1` the in-fibre group is the diagonal phases, and
conjugation by them multiplies each cross-fibre Gram block by a unit scalar, so the modulus form of
the separation is absent there; the witness has `|A| = 2` and the conjunct carries the scoping.

**This is not a decoherence claim.** It exhibits two coherent lifts of one visible family whose
visible reduced states differ in one coherence. **It says nothing about which lift the framework
realizes, nothing about any mechanism, and nothing about decoherence theory.**

**(c) Relative to `𝒪₂`: physical, at level 2, consumed.**
`pq1c_constant_left_physical_relative_candidate` restates act 13's merged `CT4` and `CL1` over
`ThreadingRelated` at their own strength: existential, `|A| ≥ 2`, with the `|A| = 1` scoping carried
as the first conjunct, relative candidates `1` against `0` at the entry `(0,0)`. **`CT4` and `CL1`
are not revised.** **Act 7's boundary is carried**: `D4b` is negative and the readback is the
repository's own convention, so this is a separation relative to `𝒪₂` **under that convention**.

**(d) The `𝒪₁`-stabilizer of `𝒢_L` — which constant left moves are redundancy relative to `𝒪₁`.**
`UniformLeft`, `uniformLeft_block`, `pq1d_plus_uniform_left_redundant_anchoredChannel`,
`nonuniform_left_block_witness`, `crossFibreGram_mul_permMatrix`,
`pq1d_minus_nonuniform_left_physical_anchoredChannel`.

- **`PQ1-d⁺`, at level 2.** Every uniform `W = 1_V ⊗ W₀` satisfies `𝔇_{a₀}(W M) = 𝔇_{a₀}(M)` for
  **every** matrix `M` and every input, because `W_iᴴ W_{i'} = W₀ᴴ W₀ = 1` for every pair of fibres.
  A global phase is the case `W₀ = c · 1_A` and needs no separate clause. `uniformLeft_block` proves
  that for `W ∈ 𝒢_L` uniformity **is** the block condition `W_iᴴ W_{i'} = 1` for every pair.
- **`PQ1-d⁻`, at level 2 — the frozen fallback is NOT used.** For **every** non-uniform `W ∈ 𝒢_L`,
  over arbitrary finite `V` and `A`, there is a coherent lift on which `𝒪₁` separates `U` from
  `W · U`. The construction: non-uniformity gives two **distinct** fibres `i ≠ i'` and ancilla
  indices `a, b` with `(W_iᴴ W_{i'})_{ab} ≠ δ_{ab}` (distinctness is forced, since at `i = i'` the
  block condition is act 12's merged `left_block_unitary`); one permutation `σ` of the dilated
  carrier sends `(i,a)` to `(i,a₀)` and `(i',b)` to `(i',a₀)`, which exists because both pairs are
  distinct; the **constant permutation lift** `U_t = P(σ)` is admissible for the visible family act
  7's merged `admissible_permMatrix` computes from it, and `W · U` is admissible by act 12's merged
  `left_preserves_admissible`. At the matrix unit `E_{i' i}` the anchored channel reads the single
  entry `Y_{i i'}(·)_{i i'}`, which is `δ_{ab}` for `U` and `(W_iᴴ W_{i'})_{ab}` for `W · U`.

**Consequence, stated exactly:** among constant in-fibre left moves, redundancy relative to `𝒪₁`
holds **exactly** for the uniform ancilla relabellings. **This is a statement about `𝒪₁` and about no
other carrier.** Act 7's `readback_relabel` (`R-3`) is a statement about the readback and is not
consumed here; `PQ1` (d⁺) is a separate computation about `𝔇_{a₀}`, and **neither is evidence for
the other**.

## `PQ2` — the time-dependent strong right gauge, carrier by carrier

`pq2a_strong_right_redundant_visible`, `pq2b_anchored_column_identity`,
`pq2b_every_single_time_anchored_carrier`, `pq2b_strong_right_redundant_anchoredChannel`,
`pq2b_strong_right_crossFibreGram`, `pq2c_strong_right_physical_relative_candidate`.

**(a) Relative to `𝒪₀`: redundancy, at level 2.** Consumed from act 11's merged
`weak_preserves_admissible` with `strong_mem_weak`.

**(b) Relative to `𝒪₁`: redundancy, universally — and not only relative to `𝒪₁`, at level 2.**
**The load-bearing conjunct is `pq2b_anchored_column_identity`:** `C(U_t K_t) = C(U_t)` at every
time, for every lift and every family of strong elements — the anchored column family is
**identical**, not merely equal after some functional is applied. Hence
`𝔇_{a₀}(U_t K_t) = 𝔇_{a₀}(U_t)` and `Y_{i i'}(U_t K_t) = Y_{i i'}(U_t)` for every pair of fibres,
and hence, by `pq2b_every_single_time_anchored_carrier`, **every** carrier definable from the
single-time anchored columns — at any level, including carriers this round does not name — is blind
to every strong-right family. **This covers act 13's merged `CT3` (G), which is stated for the Gram
data, and more — the whole anchored column family — and it revises nothing:** `CT3` (G) stands as act
13 states it. It is the reason no refinement of `𝒪₁` within single-time anchored data can separate
this part.

**(c) Relative to `𝒪₂`: physical, at level 2, consumed.** Act 11's merged `GL2` restated over
`ThreadingRelated`, at its own strength: existential, one visible pair, one anchor, one time pair,
under the frozen readback. **`GL2` stands as stated and nothing is added to it.** **Act 7's boundary
is carried**, as for every `𝒪₂` verdict.

**The bounded reading of (b) with (c) together, in the freeze's words:** the strong-right part of the
residual freedom is redundancy relative to every single-time anchored carrier and is not redundancy
relative to the relative-candidate carrier. **Both are true; neither is the other**, and their
conjunction is not a third, stronger sentence.

## `PQ3` — the two parts together

`pq3a_pair_redundant_visible`, `pq3b_pair_factors_through_left`,
`pq3b_no_cancellation_on_anchoredChannel`, `pq3c_pair_physical_relative_candidate`.

**(a) Relative to `𝒪₀`: redundancy, at level 2.** The composite of (`PQ1` a) and (`PQ2` a).

**(b) Relative to `𝒪₁`: the pair's effect factors through the left part exactly, at level 2.**
`pq3b_pair_factors_through_left`: `𝔇_{a₀}(W U_t K_t) = 𝔇_{a₀}(W U_t)` for every lift, every constant
`W ∈ 𝒢_L` and every strong family. **Consequence, stated exactly**
(`pq3b_no_cancellation_on_anchoredChannel`, an iff): relative to `𝒪₁` the pair is redundancy for a
given lift **iff** its left part is; the strong-right part can neither create a separation nor cancel
one. **So on `𝒪₁` there is no case of "the pair separates although neither part does".**

**(c) Relative to `𝒪₂`: physical, with both parts nontrivial, at level 2.**
`pq3c_pair_physical_relative_candidate`, all conjuncts of one theorem: act 13's merged `CT4` lift
and its constant `W ∈ 𝒢_L` with `W ≠ 𝟙`, adjoined to the strong family `K_t = 𝟙` for `t ∈ {0,1}` and
`K_t = P(swap((0,1),(1,1)))` for `t ≥ 2`, which is strong because it fixes both anchored columns; the
composite `U'_t = W U_t K_t` is coherent for the same family by act 7's merged
`admissible_mul_of_fixes_anchor`; `K` is not constant in `t`; and the relative candidates at
`(t,s) = (1,0)` are `CT4`'s, `1` against `0` at the entry `(0,0)`.

**This witness is deliberately cheap and is recorded as such: its strong family does no work at the
certified time pair.** The substantive question about the pair is the cancellation fork (d).
**Act 7's boundary is carried.**

**(d) The fork — can a nontrivial left part and a nontrivial strong-right part cancel on `𝒪₂`?
UNDECIDED.** Neither `PQ3-d⁺` nor `PQ3-d⁻` was reached, and **neither is claimed**; the freeze
predicted neither side at any strength, and this note does not strengthen it.

**The obstruction, named.** The pair's relative object is `W (U_t K_t K_sᴴ U_sᴴ) Wᴴ`, the left part's
alone is `W (U_t U_sᴴ) Wᴴ` and the strong-right part's alone is `U_t K_t K_sᴴ U_sᴴ`. `PQ3-d⁺` would
need an exhibited triple in which the `𝒢_L`-conjugation undoes, in the anchored readback and at
**every** time pair, exactly what the strong threading does — with all three conjuncts proved;
`PQ3-d⁻` would need a **universal** theorem over `≈_T` saying no such cancellation exists. The tree
contains neither ingredient: act 13's `CL1` and act 11's `GL2` are both **existential** statements
about how the two parts move the relative candidate, and **no universal theorem about how a
`𝒢_L`-conjugation acts on the readback of a general relative object exists anywhere in the merged
record**. Neither side was attempted in this round.

**The fork is not act 13's `CT3` (d)**, which asks whether the full column cross-Gram separates every
strong-right threading. That fork is about a datum's separating power and this one is about
cancellation between two parts of one relation; **neither answers the other, and act 13's fork stays
UNDECIDED regardless.** **The fork clause therefore adds nothing to the post-round sentence.**

## `PQ4` — the two reductions, and what a selector would have to select

Asserted at the strength jointly reached by `PQ1`, `PQ2` and `PQ3`, and **not** asserted beyond it.
`pq2b_every_single_time_anchored_carrier` and `pq4b_within_fibre_carrier_blind_to_constant_left` are
the two kernel statements; neither has a converse here.

**(a) The strong-right reduction, stated in the one direction it has.** The strong-right part changes
no anchored column at any time (`PQ2` b), so **a carrier separates it only if that carrier reads data
the single-time anchored columns do not determine** — which, in the case of `𝒪₂` and `𝒪₃`, is the
off-anchor columns that the adjoint carries into the anchored slot, act 7's own mechanism.
`pq2b_every_single_time_anchored_carrier` states this for an arbitrary function of the anchored
column family, so it bounds unnamed carriers too. **The converse is not claimed:** reading such data
is not shown sufficient to separate this part, and no theorem here says it is. **Stated as the
reduction it is:** whether the strong-right part is physical turns on whether the dilation's
off-anchor columns carry physical content, in the necessary direction only. **This is not an answer
to that question and the round does not answer it.**

**(b) The constant-left reduction, stated in the one direction it has.** The constant-left part
preserves every fibre-Gram matrix (`pq0c_crossFibreGram_left_mul_diag`, act 12's merged
`fibreGram_left_mul` consumed) and moves the cross-fibre Gram blocks `Y_{i i'}` with `i ≠ i'`, so
**a carrier separates it only if that carrier reads relations between the hidden fibres of distinct
visible outcomes**; `pq4b_within_fibre_carrier_blind_to_constant_left` states this for an arbitrary
function of the within-fibre data. **The converse is not claimed.** With `PQ1` (d), what can be
separated at all is confined to the non-uniform part: **a uniform relabelling of the ancilla is
redundancy relative to `𝒪₁` for every lift, and among constant in-fibre moves the exact `𝒪₁`
stabilizer is the uniform relabellings.**

**(c) What a selector would have to select, and on what data. Stated conditionally, as a description
of a shape, and never as a proposal.** If the physical carrier — whichever it turns out to be —
separates the residual freedom, then an additional selector would have to select, together:

- **one constant element of `𝒢_L` modulo the uniform relabellings** — equivalently one cross-fibre
  frame; and
- **one strong-right family `K_·` modulo a constant** — equivalently one threading of the off-anchor
  columns across time.

And it would have to do so on data that is **neither constant-left invariant nor strong-right
invariant**. By act 12's merged `fibreGram_left_mul` and act 13's merged `CT2` (a), `CT3` (G) and
`CT4`, no fibre-Gram datum and no column-Gram datum — up to and including the full two-time column
Gram — has both properties. **No such datum is named, proposed or excluded here**, and "a sufficient
datum must depend on the rows and on the off-anchor columns" is a consequence of the merged results,
not a candidate.

## The frozen post-round sentence for `P0` — Case A, the fork clause adding nothing

The `P0` row stays **OPEN**. The sentence appended to it, verbatim from the freeze:

> `P0` remains open and two-part, and the threading part is answered relative to each frozen carrier
> of observables and to none other. The time-dependent strong right gauge changes no anchored column
> at any time, so it is redundancy relative to the visible carrier, relative to the anchored-channel
> carrier and relative to every carrier definable from single-time anchored data; it is not
> redundancy relative to the relative-candidate carrier, where act 11's `GL2` separates it under act
> 7's readback convention. The constant in-fibre left move is redundancy relative to the visible
> carrier and, among constant in-fibre moves, relative to the anchored-channel carrier exactly for
> the uniform ancilla relabellings; it is separated by the anchored-channel carrier on two coherent
> lifts of one visible family whose visible reduced states differ in modulus at one coherence, and by
> the relative-candidate carrier, where act 13's `CL1` separates it. Relative to the anchored-channel
> carrier the two parts together act exactly as the left part alone. **No carrier is adopted as the
> physical one**, so whether an additional selector is required turns on a decision this round does
> not take; if one is required it must select one constant in-fibre frame modulo the uniform
> relabellings together with one strong-right family modulo a constant, on data that is neither
> constant-left invariant nor strong-right invariant — which no fibre-Gram or column-Gram datum is.
> Nothing here names, endorses or excludes a selection principle, and `P0`'s other part — what
> selects or constrains the Gram/orbit trajectory across time — is untouched.

**No case closes `P0`.** An answer relative to a carrier is not a selection of anything, and the
row's label does not change. **Neither of `P0`'s two parts is reported closed.**

## What these outcomes do NOT license

- **No selection principle is named**, endorsed or excluded. The round determines what each frozen
  carrier computes; it does not say what fixes a representative, and it asserts and denies no
  connection and no gauge fixing, in either direction.
- **No carrier is asserted to be the physical one**, and none is asserted not to be. The round
  freezes four and adopts none.
- **`P0` is not closed by an answer relative to a carrier.** It remains OPEN and two-part; what moves
  is the precision of the threading part, and only relative to named carriers.
- **Nothing here says OI and QM are inequivalent.** Two lifts differing is not two theories
  differing; the established finite observable-law correspondence is untouched. A separation relative
  to `𝒪₂` or `𝒪₃` is, further, a separation relative to act 7's own readback convention, with `D4b`
  negative.
- **Nothing here is a claim about decoherence.** `PQ1` (b) says two coherent lifts of one visible
  family differ in the visible reduced state's coherence. It says nothing about which lift the
  framework realizes, nothing about any mechanism, and nothing about decoherence theory.
- **The anchored channel is not offered as a datum sufficient for the relative candidate.** It is
  blind to every strong-right family by `PQ2` (b), and act 11's `GL2` moves the relative candidate by
  one; so it does not determine the relative candidate and is not the datum act 13's `CT4` declined
  to name.
- **The cross-fibre Gram and the anchored channel are constructions on the lift space**, and their
  status as observations is each carrier's recorded presupposition, not a finding of this round —
  exactly as act 12 and act 13 said of the Gram data.
- **Nothing is imported from the substratum Lemma 24.1 round.** Its channel family, its block-word
  traces and its `ST` labels are objects of a different programme on a different carrier with a
  uniform prior; this round neither consumes nor compares them, and a resemblance of vocabulary is
  not a bridge.
- **Nothing about Track I.**
- **`D3`, `D4b`, `D5`, the direct-branch statement, and every merged label** are consumed unmodified.
  The direct-branch statement is exactly act 7's: `D4a` positive on the direct branch; `T1`
  **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
  fraction of OI lies in the direct sector.**

## The status rule, as honoured

1. `P0` is not closed and neither of its two parts is reported closed; the row stays OPEN.
2. No selection principle is named, adopted, endorsed or excluded; no sentence of this note begins
   "the selection principle is", "the connection is" or "the gauge fixing is". `PQ4` (c) describes
   the shape of what a selector would have to select and proposes nothing.
3. Every verdict is written as *redundancy relative to `𝒪ₓ`* or *physical relative to `𝒪ₓ`*, with the
   carrier's recorded presupposition carried with it. **The unqualified sentences "the threading
   freedom is gauge" and "the threading freedom is physical" appear nowhere in this round's
   artifacts, in any paraphrase, including in summary lines and table cells.**
4. No carrier is adopted as the physical one, and none is asserted not to be.
5. The one undecided question, `PQ3` (d), is recorded UNDECIDED with the obstruction named, and no
   other carrier's verdict is enlarged to cover it. **No verdict travels between carriers.**
6. Every `𝒪₂` and `𝒪₃` verdict carries act 7's boundary, stated at each use rather than once in a
   footnote.
7. **No manuscript is edited by this round.** No measurement model, regularity, homogeneity,
   generated evolution or source-level coherence condition is introduced, and `CoherentLift` stays
   `ℕ`-indexed.
8. No merged label is revised. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
   `SH1`, `SH1-C1`, `SH1-C2`, `CT1`, `CT2`, `CT3`, `CT4` and `CL1` are cited and consumed at their
   own strengths, and act 7 layer 2's `D5` control stands **NOT CERTIFIED**.
9. The `ROADMAP` propagation carries the frozen post-round sentence for Case A verbatim, and nothing
   stronger.

## The relation to acts 11, 12 and 13, as frozen — consumed, none revised

- Act 11's `GL2` **stands as stated** and is consumed as the `𝒪₂` separation of the strong-right
  part; `PQ2` (c) cites it and adds nothing to it.
- Act 11's `GL3` is consumed through act 13's `CT1`; nothing here touches either.
- Act 11's `GI2` is **not revised**: its constant lifts have identical relative objects, and act 12's
  reading of it as a left in-fibre move with identical Gram data stands. **`PQ1` (b) is not a `GI2`
  statement** — `GI2` is about membership in the weak class, `PQ1` (b) is about a carrier of
  observables.
- Act 12's `LG1` is consumed as the invisibility and separate maximality of `𝒢_L`; **joint maximality
  of the two-sided action is neither asserted nor excluded here either**, and `𝒢_L × 𝒢ʷ_{a₀}` is
  named as act 12 names it.
- Act 12's `TG2` and `SH1` are consumed as per-slice classifications; `TG3` is consumed as the
  standing witness that `P0`'s trajectory part is not empty, and this note does not present its pair
  as sharing per-time Gram data, because `TG3` proves it does not.
- Act 13's `CT2` (b) is the source of `≈_T`, consumed in both directions as
  `threadingRelated_iff_fibreCrossGram`; `PQ2` (b) extends `CT3` (G)'s reach from the Gram data to
  the whole anchored column family, which **adds to** `CT3` (G) and revises nothing; `CT4` and `CL1`
  are consumed as the `𝒪₂` separation of the constant-left part, and `PQ1` (b) adds two channel
  entries on the same pair.
- Act 13's fork `CT3` (d) stands UNDECIDED and is **not** this round's `PQ3` (d); the two forks ask
  different questions and this note keeps them apart.
- **No manuscript is edited by this round.**

## Discrepancies

**One item is recorded; it is not a divergence from anything the freeze fixes.**

- **The freeze reserves the guard tag `R7-PQT` but does not name the module path.** The execution
  places the round's Lean at `verification/lean-mathlib/OIBridge/ThreadingObservability.lean`,
  following the round-directory naming convention of acts 11, 12 and 13, and imports it from
  `OIBridge.lean` immediately after act 13's module. Nothing in the freeze is contradicted.

**No other discrepancy.** Every blob in the freeze's start-state table is present at the mandated
base with the SHA the freeze records. Every target landed at its predicted strength or above, and the
one target the freeze left unpredicted is reported UNDECIDED with its obstruction named. **The frozen
`PQ1` (d⁻) fallback was available and was not used**, because the general construction was reached.
**Complete positivity of the anchored channel was not free and is not stated**, exactly as the
freeze's conditional allows.

## The chronology control

**`R7-PQT` certifies the strong property**, reusing act 10's mechanism by name through acts 12's and
13's copies, with the archive-mode scaffolding of PR #599 carried and its pins **unset at
execution**:

- the preregistration blob is pinned **by content** to `1b16008470bb1e2456c57aad58421a5941a55e0c`;
- the real execution head `H` is resolved from `pull_request.head.sha` in a PR run — **never** the
  synthetic merge commit — failing closed with no fallback;
- `B = bc76a88dbe300a35715d5ce8196002f31aa62493` must be an ancestor of `H`; **and**
- **every commit in `git rev-list H ^B` must be a descendant of `B`**, which excludes pre-freeze side
  history rather than merely certifying the final head;
- history recovery is performed by the guard itself for `B`, for `H` **and for every enumerated
  commit**, and a failed recovery **fails** the check rather than skipping it;
- **archive mode** (`_PQT_SEALED_HEAD`, `_PQT_MERGE`) is present and **unset**: after the merge, one
  pin-only change records the sealed execution head and its merge commit, and the guard re-runs the
  same strong check against that object per clause 7.

**The property certified is: no commit reachable from the execution head lies outside `B`'s
descendants.** The claim is scoped to the repository record.

## Definition budget: **FOUR of the frozen six slots fire**

| Slot | Definition | Status |
| --- | --- | --- |
| 1 | `AnchoredChannel` | **fired** |
| 2 | `CrossFibreGram` | **fired** |
| 3 | `ThreadingRelated` | **fired** |
| 4 (conditional) | a uniformity predicate on `𝒢_L` — `UniformLeft` | **fired** — `PQ1` (d) was attempted and both halves landed |
| 5 (conditional) | a per-carrier observational-equality predicate | **unused** — the four carriers are kept apart in the statements without one, each target naming its carrier's object directly |
| 6 (conditional) | a relative-object or relative-candidate abbreviation | **unused** — the relative objects are written out as `U t * (U s)ᴴ`, as acts 11 and 13 write them |

**No seventh definition was introduced**, and **no lift, gauge element, witness, carrier matrix,
channel value or pair is a top-level definition** — each is a bound variable pinned by an equation in
the statement that needs it, as acts 10, 11, 12 and 13 did. The anchored column family `C(M)` is a
submatrix expression, not a definition, and the matrix units `E_{jk}` at which the carriers are
evaluated are expressions too. Acts 7's, 11's, 12's and 13's definitions are **reused, not
redefined**.

## Evidence level and axiom report

**Evidence level 2** — kernel-checked. Thirty-nine named results, **no unproved declaration, no added
axiom, no kernel-bypassing decision procedure**, every one printing only
`[propext, Classical.choice, Quot.sound]`:

| Result | Axioms |
| --- | --- |
| `crossFibreGram_apply` | `[propext, Classical.choice, Quot.sound]` |
| `crossFibreGram_diag` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredChannel_apply` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredChannel_block` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredChannel_eq_trace` | `[propext, Classical.choice, Quot.sound]` |
| `trace_unit_mul` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredChannel_unit` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredCol_gram` | `[propext, Classical.choice, Quot.sound]` |
| `anchoredCol_isometry` | `[propext, Classical.choice, Quot.sound]` |
| `pq0a_readback_is_diagonal_action` | `[propext, Classical.choice, Quot.sound]` |
| `pq0b_anchoredChannel_diagonal_is_visible` | `[propext, Classical.choice, Quot.sound]` |
| `pq0c_anchoredCol_mul_strong` | `[propext, Classical.choice, Quot.sound]` |
| `pq0c_anchoredChannel_mul_strong` | `[propext, Classical.choice, Quot.sound]` |
| `pq0c_crossFibreGram_mul_strong` | `[propext, Classical.choice, Quot.sound]` |
| `pq0c_crossFibreGram_left_mul` | `[propext, Classical.choice, Quot.sound]` |
| `pq0c_crossFibreGram_left_mul_diag` | `[propext, Classical.choice, Quot.sound]` |
| `pq0d_anchoredChannel_trace_preserving` | `[propext, Classical.choice, Quot.sound]` |
| `threadingRelated_iff_fibreCrossGram` | `[propext, Classical.choice, Quot.sound]` |
| `threadingRelated_of_constLeft` | `[propext, Classical.choice, Quot.sound]` |
| `threadingRelated_of_strongRight` | `[propext, Classical.choice, Quot.sound]` |
| `pq1a_constant_left_redundant_visible` | `[propext, Classical.choice, Quot.sound]` |
| `pq1b_constant_left_physical_anchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `pq1c_constant_left_physical_relative_candidate` | `[propext, Classical.choice, Quot.sound]` |
| `uniformLeft_block` | `[propext, Classical.choice, Quot.sound]` |
| `pq1d_plus_uniform_left_redundant_anchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `nonuniform_left_block_witness` | `[propext, Classical.choice, Quot.sound]` |
| `crossFibreGram_mul_permMatrix` | `[propext, Classical.choice, Quot.sound]` |
| `pq1d_minus_nonuniform_left_physical_anchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `pq2a_strong_right_redundant_visible` | `[propext, Classical.choice, Quot.sound]` |
| `pq2b_anchored_column_identity` | `[propext, Classical.choice, Quot.sound]` |
| `pq2b_every_single_time_anchored_carrier` | `[propext, Classical.choice, Quot.sound]` |
| `pq2b_strong_right_redundant_anchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `pq2b_strong_right_crossFibreGram` | `[propext, Classical.choice, Quot.sound]` |
| `pq2c_strong_right_physical_relative_candidate` | `[propext, Classical.choice, Quot.sound]` |
| `pq3a_pair_redundant_visible` | `[propext, Classical.choice, Quot.sound]` |
| `pq3b_pair_factors_through_left` | `[propext, Classical.choice, Quot.sound]` |
| `pq3b_no_cancellation_on_anchoredChannel` | `[propext, Classical.choice, Quot.sound]` |
| `pq3c_pair_physical_relative_candidate` | `[propext, Classical.choice, Quot.sound]` |
| `pq4b_within_fibre_carrier_blind_to_constant_left` | `[propext, Classical.choice, Quot.sound]` |

## What this round does not do

- **It revises no merged result.** Act 13's `CT1`, `CT2`, `CT3`, `CT4` and `CL1`; act 12's `LG1`,
  `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1` and `SH1-C2`; act 11's `GL1s`, `GL1w`, `GL2`, `GL3` and `GI2`;
  act 10's `AB0-A`/`AB0-B` and `one_admissible_at_every_anchor`; act 9's `RB3`/`RB1-A`/`RB1-B`; act
  8's `CE1`; act 7's `DC1`, `DC2a`, `D4a`, `D4b` and `admissible_mul_of_fixes_anchor` — all cited and
  consumed unmodified.
- **Act 7 layer 2's `D5` chronological-ordering control stands NOT CERTIFIED.** Nothing here repairs
  it retroactively, and nothing here depends on it. Act 7's `D3` existence/regularity audit remains
  separately open and unused.
- **It adopts no carrier**, names, endorses and excludes no selection principle, asserts and denies
  no connection or gauge fixing, proposes no datum sufficient for the relative candidate, introduces
  no measurement model, and introduces no regularity, homogeneity, generated evolution or
  source-level coherence. `CoherentLift` stays `ℕ`-indexed.
- **It does not answer act 13's fork `CT3` (d)**, and does not conflate it with `PQ3` (d).
- **It does not name a smallest sufficient datum.** `PQ4` (c) describes the shape a sufficient datum
  would have to have; that is a consequence of the merged results, not a proposal.
- **It compares Source A with neither Source B nor Source C**, on any axis.
- **It touches no manuscript.** Whether to propagate anything from this round is a separate owner
  call.
- **It says nothing about Track I**, and nothing here is evidence for anything there.
