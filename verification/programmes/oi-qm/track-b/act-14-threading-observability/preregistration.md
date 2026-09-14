# Track B act 14 — is the residual threading freedom redundancy or physical: CONTROL PLANE

Owner-called. This file is the whole of act 14's control plane and is merged **alone**, before any
execution object exists. It is an **adjudication round**: it freezes what *observable* means here,
on explicitly named carriers, and determines for each carrier whether the residual threading freedom
act 13 localized survives the quotient by that carrier. The round asks a question about
observability; it does **not** assert that any carrier is the physical one, and it neither names,
endorses nor excludes any rule that would pick a representative.

**Blob identity is authoritative.** The execution guard pins this file by content.

## Start state

| | |
| --- | --- |
| Merged `main` | `7f130c37939896cdbf6ecfcaaf359f6da8edd7e4` (PR #620) |
| Act 13's control plane | `../act-13-cross-time-invariants/preregistration.md`, blob `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| Act 13's result (`CT1`, `CT2`, `CT3`, `CT4`, `CL1`) | `../act-13-cross-time-invariants/result.md`, blob `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| Act 13's module (`CrossGram`, `FibreCrossGram`, `ConstRightRelated`, `ConstLeftRelated`, `ct2b_fibreCrossGram_iff`, `ct3g_fibreCrossGram_strong_right`, `mul_strong_anchor_col`, `mul_strong_submatrix`, `ct4_constant_left_obstruction`, `cl1_constant_left_moves_relative_candidate`) | `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, blob `47eb21e22845f0319926227c80d0d7f2f033880b` |
| Act 12's control plane | `../act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| Act 12's result (`LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`) | `../act-12-two-sided-gauge/result.md`, blob `467d8be147b6ebd91f2eed12404566af74ac779f` |
| Act 12's module (`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `left_mul_submatrix`, `left_block_unitary`, `fibreGram_left_mul`, `left_preserves_admissible`, `inFibreSwap_leftFibreGroup`) | `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`, blob `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| Act 11's control plane | `../act-11-coherent-lift-gauge/preregistration.md`, blob `0f6d37fafd857d9e54d5dbff6d062cc360ea08e5` |
| Act 11's result (`GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`) | `../act-11-coherent-lift-gauge/result.md`, blob `7b24353ad626de6f930e41242334cb09945ae303` |
| Act 11's module (`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `gaugeRelated_strong_iff_agree_on_anchor`, `weak_preserves_admissible`, `gl2_strong_gauge_moves_relative_candidate`, `gl3_constant_gauge_preserves_relative`) | `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean`, blob `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| Act 10's module (`one_admissible_at_every_anchor`) | `verification/lean-mathlib/OIBridge/AnchorRobustness.lean`, blob `b74202bc160918b32ca1b333da532a141ea8015d` |
| Act 10's control plane (the strengthened chronology mechanism) | `../act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| Act 7 layer 2's module (`readback`, `readback_relabel`, `AdmissibleDilationAt`, `admissible_permMatrix`, `admissible_mul_of_fixes_anchor`) | `verification/lean-mathlib/OIBridge/DilationChoice.lean`, blob `7e3a8222cedf530f3c109662e7174d72b6358063` |
| Act 7's governing preregistration (incl. `D3`, `D4b`, the readback amendment) | `../act-07-dilation-choice/preregistration.md`, blob `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| The live queue, `P0` row as act 13 left it, and the programme interpretation boundary | `verification/ROADMAP.md`, blob `8f3f9b7758bffc86ba4b2888761770fb1881a180` |
| The chronology guard | `verification/lean/edge_rigidity_probe.py`, blob `c7e9827c6eb2be9ac7cb660f964d5b610eb3411c` — consumed as context and not modified by this PR |

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists

Act 13 localized the threading part of `P0` sharply and did not select it. `CT2` (b) proves, in both
directions, that the fibre cross-Gram trajectory determines a lift up to **one constant in-fibre left
move together with one time-dependent strong right gauge**, and `CT4` with `CL1` proves that no
member of the frozen column-Gram family — up to and including the full two-time column Gram —
determines the relative candidate. So the surviving freedom is exactly named, and nothing in the
merged record says what it means.

The `ROADMAP`'s programme interpretation boundary states the fork this leaves: *"either the residual
lift freedom is physically redundant, additional structure selects one quantum history, or
observational incompleteness determines only an equivalence class of quantum histories"*, with the
further condition that *"only an empirically distinguishable residual not removed by the physically
appropriate equivalence relation would license a claim of physics beyond standard quantum
mechanics"*. That sentence contains the round's whole difficulty in four words: **the physically
appropriate equivalence relation**. Until that relation is written down as an object, "the freedom
is gauge" and "the freedom is physical" are not statements with truth values.

So this round's central work is definitional, and it is deliberately done **before** any target is
stated: it freezes what a carrier of observables is, freezes four of them by construction from
objects already in the tree, records what each presupposes, and **adopts none**. Only then does it
ask the three questions the owner set — whether the constant in-fibre left move survives the
quotient, whether the time-dependent strong right gauge does, and whether the two together do.

**The answer is predicted to be carrier-dependent, and that is the round's substantive content, not
an evasion.** The two parts of the residual freedom transform differently: one changes no anchored
column at any time, the other changes every anchored column by one constant in-fibre unitary. A
round that returned a single verdict for "the freedom" would have concealed that.

## The structural point, FROZEN BEFORE ANYTHING ELSE

**The residual freedom act 13 localized is not one object; it is a pair of parts with different
transformation behaviour, and this file never quantifies over "the freedom" without saying which
part.**

Write the relation act 13's `CT2` (b) delivers as

```
U' ≈_T U   ⟺   ∃ W, LeftFibreGroup W ∧ GaugeRelated (StrongAnchorStabilizer a₀) (fun t => W * U t) U'
```

so that `U' ≈_T U` means `U'_t = W · U_t · K_t` with `W ∈ 𝒢_L` **constant** and `K_t` **strong** and
time-dependent. The two parts act as follows, and both laws are frozen here as derivations, not as
targets:

- **the strong right factor changes no anchored column, at any time.** `K_t e_{(j,a₀)} = e_{(j,a₀)}`
  by definition of the strong class, so `(U_t K_t) e_{(j,a₀)} = U_t e_{(j,a₀)}`. This is act 11's
  `gaugeRelated_strong_iff_agree_on_anchor` in its forward direction and act 13's
  `mul_strong_anchor_col` and `mul_strong_submatrix`, all merged. **Every** datum that is a function
  of the anchored columns at a single time is therefore identical for `U` and `U K`, whatever that
  datum is — not only the Gram data act 13's `CT3` (G) covered.
- **the constant left factor changes every anchored column by one constant in-fibre unitary.**
  `(W U_t) e_{(j,a₀)} = W (U_t e_{(j,a₀)})`, and `W = ⊕_i W_i` is block diagonal across the visible
  fibres, so on each fibre block the anchored columns are carried by the single unitary `W_i`
  (act 12's `left_mul_submatrix`, `left_block_unitary`). It preserves every fibre-Gram matrix
  (`fibreGram_left_mul`) and therefore every visible law, and it does **not** in general preserve the
  products of anchored column blocks taken across two *different* fibres.

**So the question "is the residual freedom redundancy or physical" splits at the outset**, and the
split is along the axis of which data a carrier reads: data built from the anchored columns at one
time, and data built from the relative objects `U_t U_sᴴ`, into which — by act 7's own mechanism note
— the adjoint carries the off-anchor columns that the anchored data never reads.

**Nothing in acts 11, 12 or 13 is revised by any of this.** `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`,
`TG3`, `SH1`, `CT1`–`CT4` and `CL1` are consumed as the statements they are.

## The objects, FROZEN

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `P_i` the orthogonal projection onto
the visible fibre `i`, `E_{jk}` the `V × V` matrix unit with a single `1` at `(j,k)`, and `readback`,
`AdmissibleDilationAt`, `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`,
`GaugeRelated`, `LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`CrossGram`, `FibreCrossGram`, `ConstRightRelated` and `ConstLeftRelated` are acts 7, 11, 12 and 13's,
**unmodified**. Lifts are `ℕ`-indexed families of unitaries `U : ℕ → U(V × A)`; the relative object is
`U_t U_sᴴ` and the relative candidate is `readback a₀` of its entrywise modulus squared, exactly as
acts 7, 11 and 13 write them. For a single matrix `M` and a fibre `i`, `X_i(M)` is act 12's fibre
block `M.submatrix (fun a => (i, a)) (fun j => (j, a₀))`, so that `FibreGram a₀ M i = X_i(M)ᴴ X_i(M)`.

**The anchored column family.** `C(M) := M.submatrix id (fun j => (j, a₀))`, the `(V × A) × V` matrix
whose `j`-th column is `M e_{(j,a₀)}`. It is a submatrix expression, not a definition. Its fibre
blocks are the `X_i(M)`.

**The cross-fibre Gram.** For a matrix `M` and fibres `i, i'`, the `V × V` matrix

```
Y_{i i'}(M) := X_i(M)ᴴ · X_{i'}(M),      (Y_{i i'})_{jk} = ⟨P_i M e_{(j,a₀)}, P_{i'} M e_{(k,a₀)}⟩ ,
```

whose diagonal `i' = i` is act 12's `FibreGram a₀ M i` definitionally. It carries the anchor. Act 12
froze the `i' = i` case; the off-diagonal case is this round's, and it is the object that separates
the two parts of the residual freedom.

**The anchored channel.** For a matrix `M` and a `V × V` matrix `ρ`,

```
𝔇_{a₀}(M)(ρ)_{i i'} := ∑_a ∑_{j,k} M_{(i,a),(j,a₀)} · ρ_{jk} · conj( M_{(i',a),(k,a₀)} )
                     =  ∑_{j,k} ρ_{jk} · (Y_{i' i}(M))_{kj} .
```

In words: embed `ρ` on the visible carrier at the anchored ancilla configuration, apply `M`, and sum
over the output ancilla index. It is a function of the anchored columns of `M` alone, and it is
built from the same two ingredients act 7's readback is built from — the anchor held on the input
side, the ancilla summed on the output side — with the modulus square replaced by the outer product,
so that the visible law is recovered as its diagonal action (`PQ0` (a) and (b)).

**Uniform relabellings.** `W ∈ 𝒢_L` is **uniform** iff all of its fibre blocks are equal, that is iff
`W = 1_V ⊗ W₀` for a single `W₀ ∈ U(A)` — the same ancilla relabelling in every visible fibre. A
global phase is the case `W₀ = c · 1_A` and needs no separate clause. Act 7's
`readback_relabel` (`R-3`) records that relabelling the ancilla along a bijection that carries the
anchor leaves the readback unchanged; the uniform elements of `𝒢_L` are the constant in-fibre moves
that do that relabelling identically across fibres. **`R-3` is consumed as the statement it is**: it
is about the readback, and it is not by itself a statement about the carriers frozen below.

## The physical quotient, FROZEN — the round's central definitional work

### What a carrier is, and what "redundancy" and "physical" mean relative to one

A **carrier of observables** `𝒪` is a map from coherent lifts to values, together with a recorded
reason for regarding its values as observations rather than as coordinates on the lift space. The
**quotient by `𝒪`** is the equivalence

```
U ≈_𝒪 U'   ⟺   𝒪(U) = 𝒪(U') .
```

A freedom — here, a subrelation of `≈_T` — is **redundancy relative to `𝒪`** iff every pair it
relates is `≈_𝒪`-equivalent, and **physical relative to `𝒪`** iff some pair it relates is not.

**Three constraints on the vocabulary, binding every sentence of the execution.**

1. **No sentence says "redundancy" or "physical" without naming the carrier.** There is no object in
   this file called *the* physical quotient; there are four frozen carriers and the quotients they
   induce.
2. **"Invisible" is acts 11 and 12's word and keeps acts 11 and 12's meaning** — preserving the
   visible marginal of every admissible dilation. It is **not** a synonym for "redundancy relative to
   a carrier", and the execution does not use it as one.
3. **A carrier is frozen with what it presupposes.** Each of the four below is stated with the
   physical assumption that makes its values observations, and that assumption is carried wherever
   the carrier's verdict is reported.

### The four carriers, FROZEN

They are organized on two axes — the **time structure** (one anchored preparation, or a
re-anchored preparation at a second time) and the **level** (probabilities only, or the full
anchored channel).

| | probabilities only | full anchored channel |
| --- | --- | --- |
| **one time** | `𝒪₀` — the visible carrier | `𝒪₁` — the anchored-channel carrier |
| **re-anchored two-time** | `𝒪₂` — the relative-candidate carrier | `𝒪₃` — the re-anchored-channel carrier |

**`𝒪₀`, the visible carrier.** `𝒪₀(U) := (t ↦ readback a₀ (U_t.map ‖·‖²)) = (t ↦ Γ_t)`, the visible
law at every time. *What it presupposes:* only that the observer's data is the stochastic family the
lift is admissible for — `AdmissibleDilationAt` is the statement that this datum equals `Γ_t`.
*Standing:* this is the datum the framework's own admissibility condition pins, and it is the one
carrier in this file whose observational status nothing in the tree disputes. *What adopting it
would cost:* by construction every coherent lift of one visible family is `≈_{𝒪₀}`-equivalent to
every other, so `𝒪₀` identifies act 12's `TG3` pair — proved to lie in **different** two-sided orbits
with different relative evolutions — and dissolves the whole of `P0`, not only its threading part.
**The round records that consequence and does not adopt the carrier.**

**`𝒪₁`, the anchored-channel carrier.** `𝒪₁(U) := (t ↦ 𝔇_{a₀}(U_t))`, the anchored channel at every
time. *What it presupposes:* that the reduced quantum description of the visible system, after one
preparation at the anchored ancilla configuration, is physical — including its off-diagonal entries
in the fixed visible basis, not only its diagonal. *Standing:* this is the standard notion of what is
physical about a dilation when the ancilla is not — what survives tracing the ancilla out — and it is
the carrier this file names at the level of states from one anchored preparation. **No claim is made
that it is the finest such carrier**, and none is needed: `PQ2` (b) bounds every carrier definable
from single-time anchored data at once, named or not. *What is not claimed for it:* that the established correspondence's fixed-basis representation makes an
off-diagonal entry an observation **at a single time**. The correspondence gives the visible law; the
coherences are the carrier's presupposition, and the file says so rather than assuming it.

**`𝒪₂`, the relative-candidate carrier.** `𝒪₂(U) := ((t,s) ↦ readback a₀ ((U_t U_sᴴ).map ‖·‖²))`, the
relative-candidate family — the datum acts 7, 11 and 13 use throughout. *What it presupposes:* that
the relative object may be read back through act 7's frozen map, hence that re-anchoring the ancilla
to `a₀` at the conditioning time `s` is a physical operation. *Standing, stated at act 7's own
strength:* act 7's `D4b` came back **negative** — Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V` — and the readback used is the repository's
own, frozen by act 7's readback amendment, with every label bounded accordingly. **A separation on
`𝒪₂` is therefore a separation relative to that convention**, and the execution says so at every use.

**`𝒪₃`, the re-anchored-channel carrier.** `𝒪₃(U) := ((t,s) ↦ 𝔇_{a₀}(U_t U_sᴴ))`. *What it
presupposes:* both of the previous two — re-anchoring at `s`, and the reduced state's coherences.
*Role:* it is the carrier on which "the pair is separated although neither part is" could in
principle live, and it is where the cancellation fork is asked.

### What is proved about how the carriers relate, and what is not

- `𝒪₀` is the **diagonal action** of `𝒪₁`, and `𝒪₂` is the diagonal action of `𝒪₃`: for every matrix
  `M`, `readback a₀ (M.map ‖·‖²) i j = (𝔇_{a₀}(M)(E_{jj}))_{i i}`. This is `PQ0` (a), and it is what
  ties both new carriers to merged objects rather than to an invented surrogate.
- **No other relation between the four is asserted.** In particular **the four are not a ladder
  ordered by resolution**: the one-time row and the re-anchored row are computed from different
  operations on the lift, and this round proves no implication between them in either direction. Act
  13's family was a ladder and said so; this file's carriers are not, and say so.

### What is deliberately not frozen as a carrier

- **Sequential-measurement statistics.** A carrier built from intermediate measurements would need a
  measurement model, which the tree does not contain; supplying one would introduce structure this
  round is forbidden to introduce (see *Non-doings*). It is named here so that its absence is a
  recorded choice and not an oversight, and the round makes no claim about what such a carrier would
  say.
- **Representative-level data.** The anchored column family `C(U_t)` itself, the cross-Gram family,
  the fibre-Gram trajectory: these are coordinates on the lift space, exactly as act 12 and act 13
  said of the Gram data, and none of them is offered as a carrier of observables.
- **Anything from another programme.** The substratum Lemma 24.1 round's channel family
  `Φ_t(ρ) = Tr_H[U^t (ρ ⊗ 𝟙/m) U^{-t}]` is on a different carrier with a uniform prior over the
  hidden index, not an anchored configuration, and belongs to a different programme. `𝔇_{a₀}` is
  defined natively here from act 7's anchor; nothing is consumed from, or compared with, that round.

## The frozen derivations, recorded as part of the freeze

These are recorded here so that no execution-specific artifact needs to precede this blob; they are
the analysis the round formalizes, not outcomes.

**The transformation laws.** For `W ∈ 𝒢_L` with fibre blocks `W_i`, and `K` strong:

```
C(W M)        = W · C(M),            X_i(W M) = W_i · X_i(M)
Y_{i i'}(W M) = X_i(M)ᴴ W_iᴴ W_{i'} X_{i'}(M)
Y_{i i}(W M)  = FibreGram a₀ M i                                  (act 12, fibreGram_left_mul)
C(M K)        = C(M),   hence   Y_{i i'}(M K) = Y_{i i'}(M),  𝔇_{a₀}(M K) = 𝔇_{a₀}(M)
```

The first two are act 12's `left_mul_submatrix` with the definition of `Y`; the third is act 12's
merged lemma; the fourth is act 11's `gaugeRelated_strong_iff_agree_on_anchor` forward direction and
act 13's `mul_strong_submatrix`, merged, plus the definition of `𝔇_{a₀}` as a function of `C`.
Together: **on `𝒪₁` the pair `(W, K_·)` acts exactly as `W` acts, with `K_·` contributing nothing**,
and **on `𝒪₀` neither acts**, the latter because the diagonal blocks are untouched.

**The uniform-relabelling computation.** If `W = 1_V ⊗ W₀` then `W_iᴴ W_{i'} = W₀ᴴ W₀ = 1` for every
pair `i, i'`, so `Y_{i i'}(W M) = Y_{i i'}(M)` and `𝔇_{a₀}(W M) = 𝔇_{a₀}(M)` for **every** `M`. The
block condition and uniformity are the same condition: `W_iᴴ W_{i'} = 1` for every pair says exactly
that all blocks are equal. Conversely, if `W_iᴴ W_{i'} ≠ 1` for some pair, the freeze expects a lift
on which `𝔇_{a₀}` moves; supplying one over general `V` and `A` is the step rated **medium** below.

**The `𝒪₁` separation witness, with its arithmetic.** On `V = Fin 2`, `A = Fin 2`, `a₀ = 0`, take the
constant identity law, the lift `U_t = 𝟙` for every `t`, and

```
W := P(swap((0,0),(0,1))) ∈ 𝒢_L ,     U'_t := W · U_t .
```

`𝟙` is admissible at every anchor (act 10's `one_admissible_at_every_anchor`), `W` lies in `𝒢_L`
(act 12's `inFibreSwap_leftFibreGroup`) and `W U_t` is admissible (act 12's
`left_preserves_admissible`), so both are coherent lifts of one visible family. Under act 7's
convention `P(σ)_{pq} = if q = σ p then 1 else 0`, the anchored columns are `C(𝟙) e_j = e_{(j,0)}`
and `C(W) e_0 = e_{(0,1)}`, `C(W) e_1 = e_{(1,0)}`. Take `ρ = ½ · J`, the `2 × 2` all-ones matrix
halved — the uniform visible superposition. Then

```
𝔇_{a₀}(𝟙)(ρ) = ρ ,          so   𝔇_{a₀}(𝟙)(ρ)_{0 1} = 1/2 ,
𝔇_{a₀}(W)(ρ)_{0 1} = 0 ,
```

the second because the two anchored columns of `W` sit at **different** ancilla indices, so no term
of `C(W) ρ C(W)ᴴ` contributes to the fibre-`0`-against-fibre-`1` sum over a common ancilla index.
Both channels have the same diagonal, `½` at each visible outcome, which is the identity law. **The
certificate is a difference of modulus, `1/2` against `0`, not of phase**, so it survives any
quotient of `𝒪₁` by a rephasing of the visible basis; the freeze chose the witness for that reason.
The same two entries can be certified on act 13's merged `CT4` pair at `t = 0`, whose `U_0 = 𝟙` and
`U'_0 = W` are these matrices; the execution may certify on either and records which. The owner-side
check is the permutation arithmetic; the execution computes rather than reads off, as act 11's
conjugation trap requires.

**The `𝒪₂` entries are merged and are not recomputed.** Act 11's `GL2` separates a strong-right
threading at the relative-candidate entry `(0,1)`, `1/2` against `0`; act 13's `CT4` with `CL1`
separates a constant left `𝒢_L` move at the entry `(0,0)`, `1` against `0`. Both are consumed.

**The both-parts-nontrivial `𝒪₂` witness.** Take act 13's `CT4` lift and `W`, and adjoin the strong
family `K_t := 1` for `t ∈ {0,1}` and `K_t := P(swap((0,1),(1,1)))` for `t ≥ 2`, which is strong
because it fixes `(0,0)` and `(1,0)`. Then `W ≠ 1`, `K` is not constant in `t`, and the relative
candidates of `U` and of `U'_t = W U_t K_t` at `(t,s) = (1,0)` are `CT4`'s, `1` against `0`. **This
witness is deliberately cheap and the freeze says so**: its strong family does no work at the
certified time pair. The substantive question about the pair is the cancellation fork, `PQ3` (d).

## Five targets, FROZEN

### `PQ0` — the carriers, and the bridge to the merged readback

**(a) The readback is the diagonal action of the anchored channel.** For every matrix `M` over the
carrier and all `i, j`:

```
readback a₀ (M.map (fun z => ‖z‖²)) i j  =  ( 𝔇_{a₀}(M) (E_{jj}) )_{i i} .
```

Hence `𝒪₀` is the diagonal action of `𝒪₁` and `𝒪₂` is the diagonal action of `𝒪₃`, the latter by
taking `M = U_t U_sᴴ`. **Bounded reading:** this says the two new carriers restrict to merged
objects; it does **not** say either new carrier is observable.

**(b) The anchored channel's diagonal is the visible law.** For an admissible `U_t`,
`(𝔇_{a₀}(U_t)(E_{jj}))_{ii} = Γ_t(i,j)`, and the diagonal of `Y_{i i}(U_t)` is act 12's
`fibreGram_diag_of_admissible`, consumed.

**(c) The transformation laws** of the previous section, as theorems: `C(M K) = C(M)` and
`𝔇_{a₀}(M K) = 𝔇_{a₀}(M)` for strong `K`; `Y_{i i'}(W M) = X_i(M)ᴴ W_iᴴ W_{i'} X_{i'}(M)` and
`Y_{i i}(W M) = FibreGram a₀ M i` for `W ∈ 𝒢_L`.

**(d) The anchored channel is trace-preserving on a unitary.** For unitary `M`,
`Tr 𝔇_{a₀}(M)(ρ) = Tr ρ` for every `ρ`, because `C(M)ᴴ C(M) = ∑_i Y_{i i}(M) = ∑_i FibreGram a₀ M i`
is the identity (act 12's `sum_fibreGram`, consumed). **Why this conjunct is in the round:** it is
what earns the word *channel* for `𝔇_{a₀}` rather than asserting it, and it applies to `𝒪₃` as well,
each relative object `U_t U_sᴴ` being unitary. **It is not a claim that the channel is observable**;
that remains `𝒪₁`'s and `𝒪₃`'s recorded presupposition. Complete positivity is immediate from the
`C ρ Cᴴ` form and is stated only if it is free.

### `PQ1` — the constant in-fibre left move, carrier by carrier

**(a) Relative to `𝒪₀`: redundancy.** For every `W ∈ 𝒢_L` and every coherent lift `U`, `W · U` is a
coherent lift of the same family and `𝒪₀(W·U) = 𝒪₀(U)`. Consumed from act 12's
`left_preserves_admissible` and `fibreGram_left_mul`.

**(b) Relative to `𝒪₁`: physical.** There exist a visible family, two coherent lifts of it and a
constant `W ∈ 𝒢_L` with `U'_t = W U_t` for every `t`, such that
`|𝔇_{a₀}(U'_{t})(ρ)_{i i'}| ≠ |𝔇_{a₀}(U_{t})(ρ)_{i i'}|` at a named time, a named input and a named
entry. The witness and its entries are frozen above. **Stated with the modulus** so that the
separation survives any rephasing of the visible basis.

**(c) Relative to `𝒪₂`: physical.** Consumed from act 13's `CT4` and `CL1`, at their own strength:
existential, `|A| ≥ 2`, with the `|A| = 1` scoping carried.

**(d) The `𝒪₁`-stabilizer of `𝒢_L` — which constant left moves are redundancy relative to `𝒪₁`.**

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`PQ1-d⁺`** | every uniform `W = 1_V ⊗ W₀` satisfies `𝔇_{a₀}(W M) = 𝔇_{a₀}(M)` for every `M` | the uniform-relabelling computation above |
| **`PQ1-d⁻`** | no other `W ∈ 𝒢_L` does — for every non-uniform `W` there is a coherent lift on which `𝒪₁` separates | a construction over general `V`, `A`, or an explicit reduction to one |

`PQ1-d⁺` is predicted positive at full. **`PQ1-d⁻` is predicted positive at medium**, and reporting
it at full when only `PQ1-d⁺` landed is the specific error its fallback exists to prevent.
**Reporting `PQ1-d⁻` UNDECIDED is an allowed outcome.**

### `PQ2` — the time-dependent strong right gauge, carrier by carrier

**(a) Relative to `𝒪₀`: redundancy.** Consumed from act 11's `weak_preserves_admissible` with
`strong_mem_weak`.

**(b) Relative to `𝒪₁`: redundancy, universally — and not only relative to `𝒪₁`.** For every lift `U`
and every family `K : ℕ → StrongAnchorStabilizer a₀`: `C(U_t K_t) = C(U_t)` for every `t`, hence
`𝔇_{a₀}(U_t K_t) = 𝔇_{a₀}(U_t)`, hence `Y_{i i'}(U_t K_t) = Y_{i i'}(U_t)` for every pair of fibres.
**The load-bearing conjunct is the first**: the anchored column family is *identical*, not merely
equal after some functional is applied, so **every** carrier definable from the single-time anchored
columns — at any level, including ones this round does not name — is blind to every strong-right
family. This covers act 13's `CT3` (G), which is stated for the Gram data, and more — the whole
anchored column family — and it **revises nothing**: `CT3` (G) stands as act 13 states it. It is the
reason no refinement of `𝒪₁` within single-time anchored data can separate this part.

**(c) Relative to `𝒪₂`: physical.** Consumed from act 11's `GL2`, at its own strength: existential,
one visible pair, one anchor, one time pair, under the frozen readback.

**The bounded reading of (b) with (c) together, which the execution states in these words:** the
strong-right part of the residual freedom is redundancy relative to every single-time anchored
carrier and is not redundancy relative to the relative-candidate carrier. Both are true; **neither is
the other**, and neither is "the strong-right part is gauge".

### `PQ3` — the two parts together

**(a) Relative to `𝒪₀`: redundancy.** The composite of (`PQ1` a) and (`PQ2` a).

**(b) Relative to `𝒪₁`: the pair's effect factors through the left part exactly.** For every lift
`U`, every constant `W ∈ 𝒢_L` and every strong family `K`,
`𝔇_{a₀}(W U_t K_t) = 𝔇_{a₀}(W U_t)` for every `t`. **Consequence, stated exactly:** relative to `𝒪₁`
the pair is redundancy for a given lift iff its left part is; the strong-right part can neither
create a separation nor cancel one. **So on `𝒪₁` there is no case of "the pair separates although
neither part does".**

**(c) Relative to `𝒪₂`: physical, with both parts nontrivial.** The witness frozen above:
`W ≠ 1`, `K` not constant in `t`, relative candidates differing at a named entry. **Recorded as the
cheap witness it is**, with its strong family doing no work at the certified time pair.

**(d) Fork — can a nontrivial left part and a nontrivial strong-right part cancel on `𝒪₂`? NOT
predicted.** The question: is there a coherent lift `U`, a constant `W ∈ 𝒢_L` and a strong family `K`
such that `𝒪₂(W U_· K_·) = 𝒪₂(U)` while `𝒪₂(W U_·) ≠ 𝒪₂(U)` and `𝒪₂(U_· K_·) ≠ 𝒪₂(U)` — a pair
separated by neither composite half yet identified as a whole.

| Label | Statement | Earned only by |
| --- | --- | --- |
| **`PQ3-d⁺`** | such a triple exists — the pair can be redundancy relative to `𝒪₂` while neither part is | an exhibited triple with all three conjuncts proved |
| **`PQ3-d⁻`** | no such triple exists — relative to `𝒪₂` the pair is redundancy only when both parts are | a universal theorem over `≈_T` |

The freeze predicts **neither side at any strength**. **Reporting the fork UNDECIDED is an allowed
outcome.** It is **not** act 13's `CT3` (d), which asked whether the full column cross-Gram separates
every strong-right threading; that fork is about a datum's separating power and this one is about
cancellation between two parts of one relation, and the execution does not conflate them.

### `PQ4` — the two reductions, and what a selector would have to select

Asserted at the strength jointly reached by `PQ1`, `PQ2` and `PQ3`, and **not** asserted beyond it.

**(a) The strong-right reduction, stated in the one direction it has.** The strong-right part changes
no anchored column at any time (`PQ2` b), so **a carrier separates it only if that carrier reads data
the single-time anchored columns do not determine** — which, in the case of `𝒪₂` and `𝒪₃`, is the
off-anchor columns that the adjoint carries into the anchored slot, act 7's own mechanism. **The
converse is not claimed:** reading such data is not shown sufficient to separate this part, and no
theorem here says it is. **Stated as the reduction it is:** whether the strong-right part is physical
turns on whether the dilation's off-anchor columns carry physical content, in the necessary direction
only. **This is not an answer to that question and the round does not answer it.**

**(b) The constant-left reduction, stated in the one direction it has.** The constant-left part
preserves every fibre-Gram matrix (`fibreGram_left_mul`, consumed) and moves the cross-fibre Gram
blocks `Y_{i i'}` with `i ≠ i'`, so **a carrier separates it only if that carrier reads relations
between the hidden fibres of distinct visible outcomes**; a carrier reading only within-fibre data
cannot. **The converse is not claimed.** With `PQ1` (d), what can be separated at all is confined to
the non-uniform part: a uniform relabelling of the ancilla is redundancy relative to `𝒪₁` for every
lift.

**(c) What a selector would have to select, and on what data.** **Stated conditionally, as a
description of a shape and never as a proposal.** If the physical carrier — whichever it turns out to
be — separates the residual freedom, then an additional selector would have to select, together:

- **one constant element of `𝒢_L` modulo the uniform relabellings** — equivalently one cross-fibre
  frame; and
- **one strong-right family `K_·` modulo a constant** — equivalently one threading of the off-anchor
  columns across time.

And it would have to do so on data that is **neither constant-left invariant nor strong-right
invariant**. By act 12's `fibreGram_left_mul` and act 13's `CT2` (a), `CT3` (G) and `CT4`, no
fibre-Gram datum and no column-Gram datum — up to and including the full two-time column Gram — has
both properties. **No such datum is named, proposed or excluded here**, and "a sufficient datum must
depend on the rows and on the off-anchor columns" is a consequence of the merged results, not a
candidate.

## The preregistered predictions, and their strengths

| target | prediction | strength | what would falsify it |
| --- | --- | --- | --- |
| `PQ0` (a) | positive | full | an index or convention slip; repaired, not reinterpreted |
| `PQ0` (b) | positive | full | consumed from act 12's `fibreGram_diag_of_admissible` |
| `PQ0` (c) | positive | full | consumed laws plus the definition of `𝔇_{a₀}` |
| `PQ0` (d) | positive | full | consumed from act 12's `sum_fibreGram` |
| `PQ1` (a) | positive — redundancy relative to `𝒪₀` | full | consumed from act 12 |
| `PQ1` (b) | positive — physical relative to `𝒪₁` | full | permutation arithmetic; the certified entries are `1/2` and `0` |
| `PQ1` (c) | positive — physical relative to `𝒪₂` | full | consumed from `CT4`, `CL1` |
| `PQ1` (d⁺) | positive | full | the uniform-relabelling computation |
| `PQ1` (d⁻) | positive | **medium** | the general construction over arbitrary `V`, `A` may exceed the round formally; see the fallback below |
| `PQ2` (a) | positive — redundancy relative to `𝒪₀` | full | consumed from act 11 |
| `PQ2` (b) | positive — redundancy relative to `𝒪₁`, and to every single-time anchored carrier | full | consumed from act 11's orbit theorem and act 13's `mul_strong_submatrix` |
| `PQ2` (c) | positive — physical relative to `𝒪₂` | full | consumed from `GL2` |
| `PQ3` (a) | positive — redundancy relative to `𝒪₀` | full | — |
| `PQ3` (b) | positive — the pair factors through the left part on `𝒪₁` | full | — |
| `PQ3` (c) | positive — physical relative to `𝒪₂`, both parts nontrivial | full | the strong element at `t ≥ 2` fails to be strong; then another off-anchor transposition is used, and the label does not move |
| `PQ3` (d) | **not predicted** | — | — |
| `PQ4` | asserted at the strength jointly reached by `PQ1`–`PQ3` | — | — |

**`PQ1` (d⁻) fallback, frozen now.** If the general construction is not reached, the execution
reports `PQ1` (d) as **`PQ1-d⁺` at evidence level 2 and `PQ1-d⁻` UNDECIDED with the obstruction
named**, and `PQ4` (b)'s clause is asserted as "at least the uniform relabellings are redundancy
relative to `𝒪₁`, and whether anything else is remains undecided" — never as an exact stabilizer.
No numerical fallback exists for a universal statement and none is offered. No other target has a
fallback: each is level 2, consumed, or UNDECIDED.

**UNDECIDED remains a permitted label for every target**, reported with the obstruction named.

## The two outcomes, and what each licenses

The round's question has two shapes of answer, and the file fixes what each buys **before** the
execution runs, so that the outcome cannot choose its own consequence.

**Outcome R — the freedom is redundancy relative to the carrier at issue.** If, relative to a named
carrier, every pair related by `≈_T` is identified, then relative to **that carrier** the threading
part of `P0` dissolves rather than needing a selector: there is nothing for a selector to select
that the carrier can see. **What this does not do, in every case:**

- **It does not close `P0`.** `P0` is two-part. Its other part — what selects or constrains the
  Gram/orbit trajectory across time — is untouched by every target in this round, and act 12's `TG3`
  pair, whose per-time Gram data are already proved inequivalent, is the standing witness that the
  trajectory part is not empty. **The row stays OPEN.**
- **It does not say the carrier is the physical one.** Redundancy relative to `𝒪₀` is
  redundancy relative to a carrier that identifies `TG3`'s pair too.
- **It does not transfer to another carrier.** Each verdict is reported with its carrier and does not
  travel.

**Outcome P — the freedom is physical relative to the carrier at issue.** If, relative to a named
carrier, some pair related by `≈_T` is separated, then relative to **that carrier** an additional
selector is genuinely required, and `PQ4` (c) states exactly what it would have to select and on what
shape of data. **What this does not do, in every case:**

- **It does not name, endorse or exclude any selection principle**, nor assert that a connection or a
  gauge fixing exists, suffices, or fails to suffice.
- **It does not say OI and QM are inequivalent.** Two lifts differing is not two theories differing,
  and the established finite observable-law correspondence is untouched. A separation relative to
  `𝒪₂` is, further, a separation relative to act 7's own readback convention, with `D4b` negative.
- **It does not close `P0` either.** A selector that is required is not a selector that is named.

**Mixed outcomes across carriers are permitted and are what the freeze predicts.** The predicted
result is `PQ2` (b) redundancy and `PQ1` (b) physical on the same carrier `𝒪₁`, with both physical on
`𝒪₂`; the execution reports the carriers separately and resolves no disagreement between them by
preferring one.

## The frozen post-round sentence for `P0`, per outcome case

The `P0` row stays **OPEN** in every case. The sentence the execution appends to it is fixed here so
that the outcome cannot choose its own wording.

**Case A — `PQ0`, `PQ1` (a)–(c), `PQ1` (d) in both halves, `PQ2`, `PQ3` (a)–(c) and `PQ4` land:**

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

**Case B — as A, but `PQ1-d⁻` UNDECIDED:** the clause "relative to the anchored-channel carrier
exactly for the uniform ancilla relabellings" is replaced by "relative to the anchored-channel
carrier at least for the uniform ancilla relabellings, whether for anything else being undecided",
and `PQ4` (b)'s exactness clause is not asserted.

**Case C — `PQ1` (b) UNDECIDED or negative:** the clause "it is separated by the anchored-channel
carrier on two coherent lifts …" is replaced by "whether the anchored-channel carrier separates it is
undecided", the `PQ3` (b) factorization is still asserted, and `PQ4` (b)'s reduction is asserted only
in the direction the merged results give.

**The fork `PQ3` (d)** changes one clause only: `PQ3-d⁺` adds "and relative to the
relative-candidate carrier the two parts can cancel, so the pair can be redundancy when neither part
is"; `PQ3-d⁻` adds "and relative to the relative-candidate carrier the two parts cannot cancel";
UNDECIDED adds nothing.

**No case closes `P0`.** An answer relative to a carrier is not a selection of anything, and the
row's label does not change.

## The status rule for the execution, FROZEN

Whatever the execution lands, the following binds the result note and every propagation of it.

1. **The execution may not close `P0`, and may not report either of its two parts closed.** The row
   stays OPEN in every case. A verdict about a carrier is not a selection, and the trajectory part is
   outside this round entirely.
2. **The execution may not name, adopt, endorse or exclude a selection principle**, and may not
   assert or deny that a connection or a gauge fixing exists or suffices, in either direction. **No
   sentence may begin "the selection principle is", "the connection is", or "the gauge fixing is".**
   `PQ4` (c) describes the shape of what a selector would have to select; it proposes nothing.
3. **The execution may not report the residual freedom gauge or physical beyond what it proves, and
   never without naming the carrier.** Every verdict is written as *redundancy relative to `𝒪ₓ`* or
   *physical relative to `𝒪ₓ`*, with the carrier's recorded presupposition carried with it. The
   unqualified sentences "the threading freedom is gauge" and "the threading freedom is physical" may
   not be written anywhere in the round's artifacts, in any paraphrase, including in a summary,
   abstract, table cell or propagation line.
4. **No carrier is adopted as the physical one.** The execution may not report that `𝒪₀`, `𝒪₁`, `𝒪₂`
   or `𝒪₃` is the physically appropriate equivalence relation, nor that any of them is not; it
   reports what each computes and what each presupposes.
5. **Where the question is undecided it is recorded UNDECIDED, with the obstruction named**, and no
   other carrier's verdict is enlarged to cover it. In particular a redundancy verdict on one carrier
   is never reported as evidence of redundancy on another, and a separation on one is never reported
   as a separation on another.
6. **Every `𝒪₂` and `𝒪₃` verdict carries act 7's boundary.** `D4b` came back negative and the
   readback is the repository's own, frozen by act 7's readback amendment. A separation on those
   carriers is a separation under that convention, and the note says so at every use rather than once
   in a footnote.
7. **The execution edits no manuscript.** Whether to propagate anything from this round is a separate
   owner call. It also introduces no measurement model, no regularity, homogeneity, generated
   evolution or source-level coherence condition, and does not change `CoherentLift`'s `ℕ`-indexing.
8. **No merged label is revised.** `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
   `SH1`, `SH1-C1`, `SH1-C2`, `CT1`, `CT2`, `CT3`, `CT4` and `CL1` are cited and consumed at their
   own strengths, and act 7 layer 2's `D5` control stands **NOT CERTIFIED**.
9. **The `ROADMAP` propagation carries the frozen post-round sentence for the case reached,
   verbatim**, and nothing stronger.

## What none of these outcomes licenses

- **No selection principle is named**, endorsed or excluded. The round determines what each frozen
  carrier computes; it does not say what fixes a representative.
- **No carrier is asserted to be the physical one**, and none is asserted not to be. The round
  freezes four and adopts none.
- **`P0` is not closed by an answer relative to a carrier.** It remains OPEN and two-part in every
  case; what moves is the precision of the threading part, and only relative to named carriers.
- **Nothing here says OI and QM are inequivalent.** Two lifts differing is not two theories
  differing; the established finite observable-law correspondence is untouched.
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

## The relation to acts 11, 12 and 13, frozen to prevent two labels for one question

- Act 11's `GL2` **stands as stated** and is consumed as the `𝒪₂` separation of the strong-right
  part; `PQ2` (c) cites it and adds nothing to it.
- Act 11's `GL3` is consumed through act 13's `CT1`; nothing here touches either.
- Act 11's `GI2` is **not revised**: its constant lifts have identical relative objects, and act 12's
  reading of it as a left in-fibre move with identical Gram data stands. `PQ1` (b) is not a `GI2`
  statement — `GI2` is about membership in the weak class, this is about a carrier of observables.
- Act 12's `LG1` is consumed as the invisibility and separate maximality of `𝒢_L`; **joint maximality
  of the two-sided action is neither asserted nor excluded here either**, and `𝒢_L × 𝒢ʷ_{a₀}` is
  named as act 12 names it.
- Act 12's `TG2` and `SH1` are consumed as per-slice classifications; `TG3` is consumed as the
  standing witness that `P0`'s trajectory part is not empty, and the freeze does not present its pair
  as sharing per-time Gram data, because `TG3` proves it does not.
- Act 13's `CT2` (b) is the source of `≈_T`, consumed in both directions; `PQ2` (b) extends `CT3`
  (G)'s reach from the Gram data to the whole anchored column family, which **adds to** `CT3` (G)
  and revises nothing; `CT4` and `CL1` are consumed as the `𝒪₂` separation of the constant-left part,
  and `PQ1` (b) adds one channel entry on the same pair.
- Act 13's fork `CT3` (d) stands UNDECIDED and is **not** this round's `PQ3` (d); the two forks ask
  different questions and the execution keeps them apart.
- **No manuscript is edited by this round.**

## Immutable inputs

Cited and consumed **unmodified**, each at its proved strength:

- act 7 layer 2's `readback` (**the repository's own map**, frozen by the readback amendment, with
  `D4b` negative on Source A supplying one), `readback_relabel` (`R-3`, a statement about the
  readback), `AdmissibleDilationAt`, `admissible_permMatrix`, `admissible_mul_of_fixes_anchor`,
  `permMatrix_apply_eq` and `mul_permMatrix_apply`;
- act 10's `one_admissible_at_every_anchor` (**universal**, every anchor);
- act 11's `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`,
  `strong_mem_weak`, `conjTranspose_mul_mem_unitaryGroup`, `weak_preserves_admissible`
  (**universal**), `gaugeRelated_strong_iff_agree_on_anchor` (**both directions**),
  `permMatrix_mul_apply`, `gl3_constant_gauge_preserves_relative` (**universal**), and
  `gl2_strong_gauge_moves_relative_candidate` (**existential**, one visible pair, one anchor, one
  time pair, under the frozen readback);
- act 12's `LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
  `left_mul_submatrix`, `left_block_unitary`, `fibreGram_left_mul` (**universal**),
  `left_preserves_admissible` (**universal**), `fibreGram_diag_of_admissible`, `sum_fibreGram`,
  `one_leftFibreGroup`,
  `inFibreSwap_leftFibreGroup`, `twoSidedRelated_iff` (**per slice**),
  `hadamard_slices_not_twoSided` and `hadamard_lifts_not_twoSided` (**existential**, `|A| = 1`,
  `|V| = 4`), with `LG1` (2)'s maximality read as **maximality among uniform left actions considered
  alone** and joint maximality neither asserted nor excluded;
- act 13's `CrossGram`, `FibreCrossGram`, `ConstRightRelated`, `ConstLeftRelated`,
  `mul_strong_anchor_col`, `mul_strong_submatrix`, `ct2b_fibreCrossGram_iff` (**both directions**),
  `ct2a_crossGram_iff_constLeft` (**both directions**), `ct3g_fibreCrossGram_strong_right`
  (**universal**), `ct4_constant_left_obstruction` and `cl1_constant_left_moves_relative_candidate`
  (**existential**, `|A| ≥ 2`, with the `|A| = 1` scoping part of the statement), and `CT3` (d)
  standing **UNDECIDED**;
- acts 1–13's labels; act 7 layer 2's `D5` control, which stands **NOT CERTIFIED**.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.**

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, with the archive rule of PR #599

The execution's guard tag is **`R7-PQT`**, reserved here and created by the execution PR.

1. **This preregistration blob is merged into `main` before any execution-specific act 14 object
   enters the repository tree** — any Lean definition or proof about anchored channels, cross-fibre
   Grams, the threading relation or the frozen witnesses, any search, any probe guard, any result
   artifact. **The single permitted exception is the analysis recorded inside this control-plane blob
   itself**, merged *as* the freeze — including the transformation laws, the carriers, the frozen
   witnesses and their entry values, which are recorded here so that no execution-specific artifact
   needs to precede it.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR.**
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails closed**,
   with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and `H`
   the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a
   descendant of `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for `B`,
   for `H`, and for every enumerated commit alike.
7. **Archive mode, adopted 2026-09-13 (PR #599).** After the execution PR merges, neither `HEAD` on
   `main` nor the head of a later pull request is the execution head — both reach sibling rounds
   merged before or after, and a sibling branched before this freeze is exactly the side history
   clause 5 refuses. The predicate is a property of the object that was reviewed, so after the merge
   the guard **re-runs the same strong check against the sealed execution head pinned by SHA,
   together with the merge commit that carried it**: the pinned merge commit's second parent must be
   the sealed head; the sealed head must pass clause 5 against `B` exactly as in its own PR run; and
   **both the sealed head and the merge commit must be reachable from the current target** — the real
   `pull_request.head.sha` in PR CI, `HEAD` otherwise — each **fail-closed**. Nothing about `B` or the
   blob pin changes. The switch to archive mode is a pin-only change to the guard, recording the two
   SHAs and nothing else.

**The claim is scoped to the repository record.**

## Definition budget

The execution introduces **at most six** top-level definitions, and these are the six:

1. **`AnchoredChannel`** (`𝔇_{a₀}(M)(ρ)`), the carrier of `𝒪₁` and `𝒪₃`, defined from the anchor and
   the carrier and from nothing outside this round's tree. *Needed.*
2. **`CrossFibreGram`** (`Y_{i i'}(M) = X_i(M)ᴴ X_{i'}(M)`), whose `i' = i` diagonal is act 12's
   `FibreGram` definitionally. *Needed.*
3. **`ThreadingRelated`** (`≈_T`), act 13's `CT2` (b) right-hand side named, so that every target is
   stated over one object. *Needed.*
4. **A uniformity predicate on `𝒢_L`** (`W = 1_V ⊗ W₀`), *if* `PQ1` (d) is attempted; unused
   otherwise. *Conditional.*
5. **A per-carrier observational-equality predicate**, *if* the four carriers cannot be kept apart in
   the statements without one; unused otherwise. *Conditional.*
6. **A relative-object or relative-candidate abbreviation**, *if* `PQ3` (c) or (d) cannot be stated
   readably without one; unused otherwise. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No lift, gauge element, witness,
carrier matrix, channel value or pair is a top-level definition** — each is a bound variable pinned by
an equation in the statement that needs it, as acts 10, 11, 12 and 13 did. The anchored column family
`C(M)` is a submatrix expression, not a definition. Acts 7's, 11's, 12's and 13's definitions are
**reused, not redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, no `sorry`, no `axiom`, no `native_decide` — for every
target, with the single preregistered exception of `PQ1` (d⁻) under its frozen fallback, which is
UNDECIDED-with-obstruction and not a lower evidence level.

## Named hazards

1. **Writing "the freedom is gauge" or "the freedom is physical".** There is no carrier-free verdict
   in this round. Every such sentence is a status-rule violation, in any paraphrase, in any summary
   line or table cell.
2. **Treating `𝒪₂` as an established observable.** Act 7's `D4b` is negative and the readback is the
   repository's own convention; a separation relative to `𝒪₂` is a separation under that convention
   and is reported with it.
3. **Treating `𝒪₀` as the physical carrier and concluding that `P0`'s threading part dissolves.**
   Adopting `𝒪₀` dissolves the whole of `P0`, including act 12's `TG3` separation, and the round
   adopts no carrier. Reporting the dissolution without its price is the specific error.
4. **Presenting the anchored channel as the sufficient datum act 13 declined to name.** It is blind
   to every strong-right family (`PQ2` b) and `GL2` moves the relative candidate by one, so it does
   not determine the relative candidate. It is a carrier of observables, not a proposed datum.
5. **Reading `PQ1` (b) as a decoherence claim.** It exhibits two coherent lifts of one visible family
   whose visible reduced states differ in one coherence. It says nothing about which lift is
   realized, nothing about any mechanism, and nothing about decoherence theory.
6. **Sliding "invisible" into "redundant" into "gauge" into "unphysical".** Four words, one slide.
   "Invisible" keeps acts 11 and 12's meaning; "redundancy relative to `𝒪ₓ`" is this file's predicate
   and is always carrier-indexed; "gauge" and "unphysical" are not used as verdicts at all.
7. **Reading `PQ2` (b) as "the strong-right part is gauge".** It is redundancy relative to every
   single-time anchored carrier and is not redundancy relative to `𝒪₂`. Both hold; neither is the
   other, and their conjunction is not a third, stronger sentence.
8. **Treating the four carriers as a ladder ordered by resolution.** Only two refinements are proved
   — `𝒪₀` the diagonal action of `𝒪₁`, `𝒪₂` the diagonal action of `𝒪₃` — and no implication between
   the one-time and re-anchored rows is asserted in either direction.
9. **Reading `PQ3` (c) as the substantive pair result.** Its strong family does no work at the
   certified time pair; the substantive question about the pair is the cancellation fork `PQ3` (d),
   which is not predicted.
10. **Conflating `PQ3` (d) with act 13's `CT3` (d).** `CT3` (d) asks whether the full column
    cross-Gram separates every strong-right threading; `PQ3` (d) asks whether two parts of `≈_T` can
    cancel on `𝒪₂`. Neither answers the other, and act 13's fork stays UNDECIDED regardless.
11. **Reporting `PQ1` (d⁻) at full when only `PQ1-d⁺` landed.** The exact stabilizer and the
    inclusion are different claims; the fallback wording is frozen and is not optional.
12. **Promoting `PQ4` from a reduction to a proposal.** "Whether the strong-right part is physical
    reduces to whether the off-anchor columns carry physical content" is a reduction of one open
    question to another. It answers neither, and it names no datum and no principle.
13. **Introducing a measurement model to build a sequential-measurement carrier.** The tree contains
    none; supplying one is introducing structure, which the round is forbidden to do. Its absence is
    recorded, and no claim is made about what such a carrier would say.
14. **Importing the substratum Lemma 24.1 round's channel vocabulary.** Its family averages over the
    hidden index with a uniform prior on a different carrier in a different programme; `𝔇_{a₀}` holds
    the ancilla at act 7's anchor. Nothing is consumed or compared, and the shared word "channel" is
    not a bridge.
15. **The conjugation trap, again.** Under act 7's convention `P(g) P(h) = P(h·g)` and
    `(P(σ) M)_{pq} = M_{σ p, q}`; forced elements, anchored columns and separating entries are
    computed, never read off a constructor.
16. **Forgetting the anchor.** `𝔇_{a₀}` and `Y_{i i'}` both carry `a₀`; the relative object `U_t U_sᴴ`
    does not. State which, in every statement.
17. **Reading act 7's `R-3` as a carrier-level invariance.** `readback_relabel` is a statement about
    the readback under a relabelling that carries the anchor. `PQ1` (d⁺) is a separate computation
    about `𝔇_{a₀}`, and neither is evidence for the other.
18. **Treating act 13's `CT4` pair as revised.** It is consumed unmodified; `PQ1` (b) may certify two
    channel entries on the same pair at `t = 0`, which adds a statement and revises none.
19. **Reporting a redundancy verdict on one carrier as evidence about another.** Verdicts do not
    travel, in either direction, and an UNDECIDED on one carrier is not covered by a verdict on
    another.
20. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See clauses 5 and 7.

## Non-doings

The round does not: adopt a carrier as the physical one; name, endorse or exclude a selection
principle; assert or deny that a connection or gauge fixing exists or suffices; propose a datum
sufficient for the relative candidate; introduce a measurement model, regularity, homogeneity,
generated evolution or source-level coherence; change `CoherentLift`'s `ℕ`-indexing; revise `GL1s`,
`GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1` or
any merged label; answer act 13's fork `CT3` (d); change `D3`, `D4b`, `D5`, the direct-branch
statement or the readback convention; consume or compare anything from the substratum Lemma 24.1
round; compare Source A with B or C; edit any manuscript; close `P0` or either of its parts; or say
anything about Track I.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.**
- **Then exactly one execution PR**, based on the merge commit of this one, carrying the Lean, the
  result note, the probe guard `R7-PQT` (pinning this blob, certifying clause 5's ancestry, and
  carrying the clause-7 archive mode with its pins unset), the `ROADMAP` propagation, and the census
  entry. **No manuscript changes.**
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **After the merge, one pin-only change** records the sealed execution head and its merge commit in
  the guard, switching it to archive mode per clause 7.

## Allowed final report

1. **The four carriers**, each with its definition, its recorded presupposition and its standing, and
   the statement that none is adopted;
2. **`PQ0`** — the bridge to act 7's readback, the diagonal statements, the transformation laws, and
   the trace-preservation conjunct that earns the word *channel*;
3. **`PQ1`** — the constant in-fibre left move on each carrier, with `PQ1` (b)'s named time, input and
   entry and its modulus form; `PQ1` (d) as `PQ1-d⁺` with `PQ1-d⁻` at level 2 or UNDECIDED with the
   obstruction, under the frozen fallback;
4. **`PQ2`** — the strong right gauge on each carrier, with (b) stated as the anchored-column
   identity it rests on and its reach over every single-time anchored carrier named;
5. **`PQ3`** — (a), (b) with the factorization stated exactly, (c) with its cheapness recorded, and
   (d) as `PQ3-d⁺`, `PQ3-d⁻` or UNDECIDED with the route to the label;
6. **`PQ4`** — the two reductions and the conditional shape of a selector, at the strength jointly
   reached, with nothing named;
7. the frozen `P0` sentence for the case reached, verbatim, and the row's label unchanged;
8. what the outcomes do **not** license, in this file's wording, and the status rule as honoured;
9. the relation to acts 11, 12 and 13 as frozen — `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`,
   `SH1`, `CT1`–`CT4` and `CL1` consumed and none revised, `CT3` (d) still UNDECIDED;
10. the definition count against the six-slot budget, with conditional slots marked fired or unused;
11. the chronology certification, naming the property certified and the archive-mode pins as unset at
    execution;
12. the axiom table with one line per named result.
