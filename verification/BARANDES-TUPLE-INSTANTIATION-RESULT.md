# Track B act 6 — tuple instantiation and the Source-A branch test: result

Frozen preregistration: commit `85a8fdffef31bc0afc76faecd4e4a3f5d3fa8550`, blob
`2a2216b7791e93303598dafb0d035db18ad9d88a`, merged to `main` by PR #570.

Executed from `main` at `ef441c3a97cdfb7c4343852516ffbe10635f2ce5`, the merge of that freeze.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. Layer 1 reads **Source C v2** and Layer 2 reads **Source A**, each on its
own coordinates, and the two are never mixed. Source A coordinates are read off act 5's
**authoritative surface**, the PDF of arXiv:2302.10778v3.

All the mathematics is in `verification/lean-mathlib/OIBridge/BarandesTuple.lean`.

## Outcome — a pair, not one label

**`(TI1, UB2)`.**

**`TI1` — tuple instantiation proved.** The OI visible class instantiates Source C v2's ten-axiom
stochastic-process tuple, under the frozen declarations, with every axiom kernel-proved as its own
named result.

**`UB2` — the direct branch refuted.** A lawful OI family is **exhibited** that is not directly
unistochastic in Source A's orientation, so `DirectBranch` is false.

**The two labels are independent and are reported as a pair.** Layer 1 mentions unistochasticity
nowhere and is conditioned on no Layer-2 outcome; Layer 2 uses no component of the tuple. Neither
label is evidence for the other, and collapsing them into one headline would assert a connection
neither layer proves.

## Layer 1 — the tuple instantiation

### The interface is Source C v2's process, typed rather than summarized

`BarandesTuple` carries the tuple `(C, T, T₀, Γ, p, 𝒜)` of **eq (24), p. 8**, with all ten axioms as
fields. The conditioning-time argument is **kept in `Γ`'s type**: instantiating it at a singleton
`T₀` is a declaration, whereas erasing it would give a weaker tuple than the source defines, and
`TI1` would then have been proved against the wrong object.

| Axiom | Source C v2 | What it says | Status |
| --- | --- | --- | --- |
| **X1a** | §3, p. 8 | `C` finite | proved — the `Fintype` instance on `V` |
| **X1b** | p. 8 | `T` contains an initial time `0` | proved — `init := 0` |
| **X1c** | p. 8 | `T₀ ⊂ T` contains the initial time | proved — `Cond := (· = 0)`, `init_cond` |
| **X2** | (25) p. 8, (27) p. 9 | `Γ` takes values in `[0,1]` | `transpose_nonneg`, `transpose_le_one` |
| **X3** | (28) p. 9 | `∑ᵢ Γᵢⱼ = 1`, over the **first** index | `transpose_isColStochastic` |
| **X4** | (29) p. 9 | `Γᵢⱼ(t₀ ← t₀) = δᵢⱼ` | `transpose_zero` |
| **X5** | (30)–(31) p. 9 | `p` takes values in `[0,1]` | `tupleP_nonneg`, `tupleP_le_one` |
| **X6** | (32) p. 10 | `∑ⱼ pⱼ(0) = 1` | `tupleP_zero` with the hypothesis on `p0` |
| **X7** | (33) p. 10 | `pᵢ(t) = ∑ⱼ Γᵢⱼ(t ← 0) pⱼ(0)` | holds **by construction** of `tupleP` |
| **X8** | (34) p. 10 | `∑ᵢ pᵢ(t) = 1` at every `t` | `tupleP_sum`, **derived** from X3 and X6 |
| **X9** | (35) p. 10 | divisibility over conditioning times | `singletonDivisible_of_pper` |
| **X10** | (40)–(41) and text, p. 12 | `𝒜` a commutative algebra of maps `C × T → ℝ` | `alg := ⊤`, taken maximal |

Each axiom is a **separately named result**; the instantiation `barandesTupleOfPPer` only assembles
them. There is no aggregate satisfaction claim.

### The declarations, and what is parameterized

`C = V`, `T = ℕ`, `T₀ = {0}`, `Γ_B(t ← 0) = (Γ t)ᵀ` in act 2's frozen orientation, `𝒜` the maximal
algebra of maps `V × ℕ → ℝ`, and `p` **constructed** from a parameterized `p0`.

**`p0` is parameterized, never supplied.** The theorem takes an arbitrary `p0` with `∀ j, 0 ≤ p0 j`
and `∑ j, p0 j = 1` as hypotheses. Act 1's **Q8** established that our datum does not carry `p`, and
nothing here claims otherwise.

**`p` at later times is constructed, not declared.** Source C **eq (33), p. 10** *fixes* `p` at every
target time from `p(0)` and `Γ`; only `p(0)` is free, by **eq (32), p. 10**. So `tupleP` builds the
whole time-dependent distribution, X7 holds by construction, and **X8 is derived from X3 and X6** —
which is how Source C itself derives eq (34), from (28) and (32). This is the correction the freeze
recorded: an earlier six-component shorthand treated `p` as a free normalized vector at every time,
and a `TI1` proved against that would have been proved against a weaker tuple than the source
defines.

### The class, not one realization

The target is `PPer` — Arc B's exact OI visible class, `C_OI(V) = PPer(V)` — so the instantiation
holds for every member, which is strictly stronger than instantiating at one realization.
`rootedRealization_instantiates` is the corollary, through the merged `rootedMap_mem_PPer`. It is a
**theorem** rather than a definition, which is what keeps the module at the frozen budget of seven
top-level definitions.

### The `T₀ = {0}` vacuity, in two parts

**X9 is a required axiom, not an optional one.** Source C writes that `Γ` "will be assumed to
satisfy" eq (35). But the equation quantifies `t₀` and `t′` over **conditioning times only**, never
over general target times. That is why it coexists with act 1's **`BD3`** and with the source's own
p. 11 remark that the process "is therefore indivisible for generic target times".

**Part one — it is discharged here**, at `T₀ = {0}`, by trivialization
(`singletonDivisible_of_pper`), as one of the ten axioms.

**Part two — discharging it bears on `PDivisible` in neither direction**, and this is proved
separately rather than asserted. `singletonDivisible_independent_of_pdivisible` exhibits **two**
`PPer` families that both satisfy the singleton condition, one `PDivisible` and one not. So no
reading of `TI1` licenses the inference that the OI family is divisible, and `BD3` is untouched.

## Layer 2 — the Source-A branch test

### A branch test, not a candidate selection

Layer 2 asks one question: is every OI visible family, transposed into Source A's orientation,
**directly unistochastic**? It selects no unitary lift, adopts no candidate rule, and adjudicates
nothing act 5 left open.

### The three ingredients

**`IsUnistochastic` is defined from scratch** — existence of a complex unitary whose entrywise
norm-squares are the matrix, **Source A eq (30), p. 11**. It is deliberately **not** routed through
`QfbData`, `QStar`, `born`, `overlap_row_sum` or `overlap_col_sum`. Defining it through any of those
would build into the predicate the very representation shortcut Arc D's **`RD1`** disqualifies.

**No representation shortcut is taken anywhere in the layer.** No theorem here discharges the branch
test from the existence of any representation. The merged `overlap_row_sum` and `overlap_col_sum` are
about the coherent-lift transport matrix on the shell, `QfbData.born` lives on the basis carrier, and
**no merged theorem identifies either with `(Γ t)ᵀ`**.

**The structural lemma** — `unistochastic_isRowStochastic_and_isColStochastic` — is Source A's own
**p. 11** observation that every unistochastic transition matrix is doubly stochastic, **proved here
rather than cited**. It is what makes the branch decidable by a stochasticity check instead of by
reasoning about all unitaries. `IsColStochastic` and the transpose lemmas are act 2's and are
consumed, not re-proved.

**The direct-branch proposition, in the exact external orientation**, and its genuine complement:

    DirectBranch     ≡  ∀ Γ, PPer Γ → ∀ t, IsUnistochastic ((Γ t)ᵀ)
    OffDirectBranch  ≡  ∃ Γ, PPer Γ ∧ ∃ t, ¬ IsUnistochastic ((Γ t)ᵀ)

Both are stated over `PPer`, so the test is about the class rather than about one realization.

### The witness, and which half of the structural lemma refutes it

On `Fin 2`: the family with `Γ 0 = 1`, period `2`, and at odd times the row-stochastic

    A  =  [[1, 0], [1, 0]]

`PPer` membership is proved, not assumed: `Γ 0 = 1`, row stochasticity at every time, and
periodicity at `M = 2`. Its transpose is

    Aᵀ  =  [[1, 1], [0, 0]]

whose **columns** each sum to `1` — so `Aᵀ` **is** column-stochastic — and whose **rows** sum to `2`
and `0`.

**The refutation therefore runs through the ROW half of the structural lemma applied to `Aᵀ`, and
not the column half.** Transposing a row-stochastic matrix makes it column-stochastic, so the failure
that survives transposition into Source A's orientation is the row one. The orientation is stated
this way because the opposite reading was written into an earlier draft of the freeze and corrected
under review; `collapsed_slice_not_unistochastic` is the single computation both statements of `UB2`
run through, and it computes a **row** sum.

`offDirectBranch` is the exhibited witness, and `not_directBranch` records the universal statement's
failure separately rather than leaving it implicit.

### The witness is lawful at the realization layer too

`offDirectBranch_realization` is declared an **addition** beyond the two outcome-bearing theorems,
not folded into them. It takes the freeze's own named route through the merged
`pper_has_responseRealization` to upgrade the same witness to a `RootedRealization`, so the witness
cannot be read as an abstract matrix family with no OI realization behind it. Non-negativity and
normalization of the prior are carried by `RootedRealization`'s own `prior_nonneg` and `prior_sum`
fields, so lawfulness is a consequence of the merged structure rather than an added hypothesis.

## The control this round exists to protect: direct unistochasticity ≠ dilatability

These are **different propositions**, and nothing here relates them in either direction.

- **`UB2` does not say Source A is inapplicable to OI.** Source A **§3.4, p. 10** dilates a
  non-unitary `Θ(t ← 0)` to a unitary one on a larger carrier, so a visible matrix that is not
  unistochastic may still embed there. `UB2` places the OI class on **act 5's unadjudicated dilated
  branch**.
- **Conversely**, the existence of a dilation would not show the original matrix unistochastic, and
  no result here infers one from the other.
- **Whether the dilation choice moves the induced candidate is not adjudicated here.** It is the next
  load-bearing obligation and belongs to a later round with its own freeze.

**No result in this round says the external correspondence fails.**

## What was not proved

**`TI2` and `TI3` are not reached, and `TI1` is why.** `TI2` requires an **exhibited** lawful
counterexample to a **named** axiom, against the fully typed interface under the frozen
declarations; every axiom is instead proved. `TI3` is the unresolved label and nothing is
unresolved at Layer 1.

**`UB1` is refuted, not merely unproved.** The distinction matters and the freeze fixed it in
advance: failure to prove `UB1` would have been `UB3`, and `UB2` is earned only by the exhibited
witness. It was exhibited.

**`UB3` is not reached.** Nothing at Layer 2 is left unsettled by this round's own question.

## What this licenses, and what it does not

**Licensed.** The OI visible class satisfies the external tuple's stated axioms at the frozen
declarations. The instantiation obligation act 3 named as a separate task — "the eventual task is to
show our representation instantiates his construction" — is discharged **at Layer 1's scope**: the
tuple of Source C v2 §3, at `T₀ = {0}`, with `p` parameterized at time zero.

**Licensed.** The OI class sits off Source A's direct unistochastic branch, so any route from OI to
Source A's construction runs through the **dilation**, and the dilation's choice structure is the
next thing that must be settled.

**Not licensed.** Nothing here says the correspondence fails, that Source A is inapplicable, or that
the OI family is `PDivisible` or `PIndivisible`. Nothing identifies any object here with any external
candidate rule. Nothing adopts or proposes a candidate-selection principle. Nothing claims OI forces
quantum structure. **Nothing here is a sourcing claim**, and the track separation of Amendment 2 holds
in both directions: no Track I conclusion is used as evidence here, and no result here is evidence for
Track I. **No fifth condition**, no deferred Arc D resource adjudicated, and §3.6 is not reopened.

**Unrevised.** Act 1's `BD3` and `BR3`, act 2's `RT1`, act 3's `CU1a`, act 4's `MP4` and act 5's
`SA2` are cited and left exactly as merged. Acts 4 and 5 are not reopened.

## Predictions, and whether they held

**`TI1` was predicted likely "but less trivially than the earlier draft assumed", with the live path
away from it an axiom the component-level ledger had not examined.** It held, and the freeze's
diagnosis was the right one: X2–X4 were what `PPer` already carries after transposition, X9 collapsed
at a singleton `T₀`, and the work was all in X5–X8 — the `p` law that the earlier shorthand had
treated as a declaration.

**`UB2` was predicted "materially likely", as the round's substantive prediction, on merged and
definitional ground: `PPer` requires row stochasticity and carries no column-sum condition, while
Source A states that every unistochastic matrix is doubly stochastic.** It held, and by exactly that
route.

**The prediction was recorded at that strength and no higher**, and `UB2` is reported as earned by
the exhibited witness rather than by the prediction.

## What remains open, and what would settle it

1. **The dilated branch.** `UB2` makes Source A's §3.4 dilation the load-bearing step for any
   OI-to-Source-A route. What would settle it: a round that types the dilation, determines whether
   the dilation choice moves the induced visible candidate, and reports at act 5's `A4`/`A5` burden —
   an exhibited visible-level witness, not an operator-level one.
2. **`T₀` beyond the singleton.** `TI1` runs at `T₀ = {0}`. Whether the OI class instantiates the
   tuple at a larger `T₀` is a different question, and act 1's `BD3` bears on it. What would settle
   it: a round that fixes a `T₀` and proves or refutes X9 there.
3. **`p0`'s provenance.** Q8 stands: our datum does not supply `p0`. Whether anything on our side
   selects it is untouched here.
4. **Act 5's gauge-versus-empirical tension**, left open there and not adjudicated here.

## Controls, discharged

- **Kernel discipline.** No `sorry`, `axiom` or `native_decide`. **Eighteen named results**, each
  with a `#print axioms` line printing only `[propext, Classical.choice, Quot.sound]`. The module is
  registered in `verification/lean-manuscript-census.json` and imported in `OIBridge.lean`.
- **Definition budget.** **Exactly seven** top-level definitions, matching the freeze:
  `BarandesTuple`, `tupleP`, `SingletonT0Divisible`, `barandesTupleOfPPer`, `IsUnistochastic`,
  `DirectBranch`, `OffDirectBranch`. Witnesses are built **inside the proofs that need them**, per
  act 3's lesson; `rootedRealization_instantiates` is a theorem for the same reason.
- **Merged results consumed, never re-proved:** `rootedMap_zero`, `rootedMap_mem_PPer`,
  `pper_has_responseRealization`, act 2's `RT1` bridge and `IsColStochastic`.
- **`A` is the full function algebra, taken canonically** — not derived, and not argued to be the
  smallest algebra that would serve.
- **Source coordinates** follow act 1's frozen table and act 5's authoritative surface, and are never
  mixed across sources.
- **No manuscript edit**, and no manuscript claim is affected by this round.

## Evidence level

Act 1's **level 2 — kernel-checked** — for every named result in both layers. Layer 1's *interface*
is a reading of Source C v2 at act 1's level 3, and it is that reading, not the kernel, that the
citation table above is accountable for; the guard pins the axiom list and its coordinates so a
reshaped interface fails rather than passes.
