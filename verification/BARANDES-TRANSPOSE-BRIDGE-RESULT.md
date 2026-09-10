# Track B act 2 — the Lean transpose bridge: result

Executed against the preregistration frozen at blob
`4cb6b71832c033f61ac6052c0d2ba11763150d62`
(`verification/BARANDES-TRANSPOSE-BRIDGE-PREREGISTRATION.md`, merged by PR #561).

Base: `main` at `1a5e1a1bc1d906fa9dad1226206c4c018c2ccdf3`, which carries that blob. Every commit of
this round descends from that merge, so the control-plane ordering is checkable from the history.

Kernel module: `verification/lean-mathlib/OIBridge/TransposeBridge.lean`.

## Headline outcome

**RT1 — the bridge is kernel-closed.** All four frozen targets are proved against the definitions
exactly as frozen. Seven named results, each printing only `[propext, Classical.choice, Quot.sound]`.

The recorded prediction was **RT1, at high confidence**, and it **held**. Nothing was reshaped to
make a proof close; `RT3` was never reached for.

## 1. The four targets

### T1 — the predicate duality: **proved, both directions**

`IsColStochastic` is defined in the frozen form. Two results carry the target:

- `isRowStochastic_iff_transpose_isColStochastic` — `IsRowStochastic M ↔ IsColStochastic Mᵀ`
- `isColStochastic_iff_transpose_isRowStochastic` — `IsColStochastic M ↔ IsRowStochastic Mᵀ`

Both directions were required by the freeze, and both are load-bearing rather than decorative: T3's
forward leg consumes the first (it transposes a row-stochastic propagator) and its backward leg
consumes the second (it transposes a column-stochastic one). A one-way T1 would have left T3
provable in one direction only, which is exactly the failure the freeze anticipated.

The proofs are transposition of the index pair in each conjunct. `Mᵀ i j` is `M j i` definitionally,
so the nonnegativity clauses exchange by argument swap and the row-sum and column-sum clauses are
alpha-equivalent.

### T2 — the single-pair factorization bridge: **proved**

- `factor_transpose_iff` — `(A = B * Λ ∧ IsRowStochastic Λ) ↔ (Aᵀ = Λᵀ * Bᵀ ∧ IsColStochastic Λᵀ)`

This is act 1's transposition at one time pair. The forward direction rewrites by the equation and
applies `Matrix.transpose_mul`; the backward direction transposes the hypothesis and simplifies
under `Matrix.transpose_transpose` and `Matrix.transpose_mul`.

The orientation hazard the act 1 freeze named — that row-stochastic-acting-on-the-right and
column-stochastic-acting-on-the-left "are the same content under transpose; that they are the same
*here* is a claim to check, not to assume" — is discharged by this result rather than assumed. The
stochasticity requirement travels onto the same factor: it is the newly introduced intermediate that
must be stochastic on both sides, not the given earlier-time map.

### T3 — the family-level restatement: **proved, with its negation corollary**

`PDivisibleCol` and `PIndivisibleColWithin` are defined in the frozen form, unchanged.

- `pDivisible_iff_pDivisibleCol_transpose` — `PDivisible K Γ ↔ PDivisibleCol K (fun t => (Γ t)ᵀ)`
- `pIndivisibleWithin_iff_pIndivisibleColWithin_transpose` —
  `PIndivisibleWithin K Γ ↔ PIndivisibleColWithin K (fun t => (Γ t)ᵀ)`

The forward leg instantiates the witness at `Λᵀ`, the backward leg at `Mᵀ`. The corollary is
`not_congr` of the equivalence and is stated separately because `PIndivisibleWithin` is the
predicate the corpus actually reasons with.

This is where the transposition stops being a statement about one factorization instance and becomes
a statement about the **predicate**: the two orientations are the same predicate on transposed
families, at every horizon and every family.

### T4 — the endpoint marker: **proved**

- `root_factor_of_trivial` —
  `Γ 0 = 1 → IsRowStochastic (Γ t) → ∃ Λ, IsRowStochastic Λ ∧ Γ t = Γ 0 * Λ`

The witness is `Γ t` itself, and the equation closes by `Matrix.one_mul`. This converts act 1's
"the extra case is vacuous rather than stronger" from an assertion into a lemma.

**One result was added beyond the frozen four targets, and is reported as an addition rather than
folded into T4:**

- `rootedMap_zero` — `rootedMap R 0 = 1`, for any `RootedRealization V H`

The frozen T4 takes `Γ 0 = 1` as a **hypothesis**, and the preregistration says in prose that
`rootedMap R 0 = 1` supplies it. Leaving that in prose would have left the endpoint result
conditional on an unproved side claim about the programme's own realization layer, so it is proved:
the zeroth iterate of the update is the identity, the diagonal entry sums the prior to one by
`prior_sum`, and the off-diagonal entries vanish. Together with the merged
`rootedMap_isRowStochastic`, both hypotheses of `root_factor_of_trivial` now hold for **every**
family this programme produces, not only for families assumed to trivialize.

This addition does not widen the round: it adds no new target, decides nothing the freeze left open,
and its statement is about `rootedMap` alone.

## 2. Axiom status

Every named result carries a `#print axioms` line, and every line prints exactly
`[propext, Classical.choice, Quot.sound]`:

| # | result |
|---|---|
| 1 | `isRowStochastic_iff_transpose_isColStochastic` |
| 2 | `isColStochastic_iff_transpose_isRowStochastic` |
| 3 | `factor_transpose_iff` |
| 4 | `pDivisible_iff_pDivisibleCol_transpose` |
| 5 | `pIndivisibleWithin_iff_pIndivisibleColWithin_transpose` |
| 6 | `root_factor_of_trivial` |
| 7 | `rootedMap_zero` |

**Seven named results.** No `sorry`, no custom `axiom`, no `native_decide`. The module builds clean
with no warnings of its own.

Mathematical status and kernel status are reported separately, as always: the mathematical content
is a transposition identity, and the kernel status is that all seven results are axiom-clean.

## 3. Outcome label and prediction

**`RT1`.** All four targets proved, axiom-clean.

The freeze recorded **`RT1` at high confidence**, on the ground that `Matrix.transpose_mul` gives the
product reversal, transposition is involutive, and row and column sums exchange over a `Fintype` — so
no step would need anything act 1's prose omitted. That is what happened: the three Mathlib facts
named in the prediction are the three the proofs use, and no additional hypothesis was required.

The prediction **held**. It is recorded as held rather than as vindication: a confident prediction
that comes true is weaker evidence than one that survives a genuine chance of failure, and the
reason `RT3` was live here is that act 1's Q4 had never been machine-checked.

**No prediction was recorded** on whether the horizon difference could be removed, and none was
attempted. See §5.

## 4. Effect on act 1

**The kernel confirms act 1's Q4 transposition. No correction is appended to act 1.**

Act 1's Q4 stated, in prose, that after transposing the column-stochastic left action to the
row-stochastic right action, the external factorization equation is the body of `PDivisible` exactly,
with `s := t′` and `Λ := Γ̃(t ← t′)ᵀ`, and that "a matrix is column-stochastic exactly when its
transpose is row-stochastic, so the stochasticity requirement transports without residue".

Both halves of that claim are now theorems: the stochasticity transport is T1, and the factorization
transport is T2, with T3 lifting it to the predicate.

**Under act 1's own frozen evidence hierarchy this is a level change.** That hierarchy rates
"a transposed predicate defined in Lean and proved equivalent to `PDivisible` under the stated
transposition" at level 2, above "prose determination" at level 3, and named step 5 of the Amendment
2 sequence as where the upgrade belonged. Act 1's Q4 accordingly stands at **level 2 on its
this-side half**.

The **other-side half is untouched and stays at level 1**: what the external text's equation *says*
was established from primary-source locations in act 1, and nothing in this round bears on it. The
upgrade is to the transposition step, not to the reading of the source.

## 5. What the horizon difference remains

`PDivisible` bounds its time pairs by a horizon `K`. The external equation act 1 compared against
carries no such bound; its intermediate times range over `t > t′ > t₀` without a horizon.

**This is a difference of quantifier domain, and it is reported as a difference, not a defect.** T4
does not remove it and did not attempt to. What T4 settles is the *other* recorded difference — that
`PDivisible` admits `s = 0` where the external range is strict — and it settles it as costing
nothing, since at `s = 0` the condition is discharged by the map itself whenever the family
trivializes at the root, which `rootedMap_zero` now proves it does.

So of the two differences act 1 recorded against the external equation, one is proved vacuous and one
stands. Any later round that wants the horizon gap closed must say what it would mean to close it;
this round takes no position on that.

## 6. What a later Track B round can begin from

Stated, not executed.

1. **A `BarandesTuple` instantiation lemma.** Act 1's Q8 found that the merged rooted-realization
   datum supplies four of the six tuple components outright and leaves `T₀` and `p` to be declared.
   A structure carrying `(C, T, T₀, Γ, p, A)` with the normalization and trivialization conditions,
   plus an instance built from `RootedRealization`, would make "our processes instantiate the tuple"
   checkable rather than argued. `rootedMap_zero` supplies the trivialization condition for that
   instance. What such a round may **not** do is derive any indivisibility relation: act 1's `BD3`
   means none is available.
2. **The question `BD3` leaves open.** Since the class predicate and `PIndivisibleWithin` are
   predicates of different kinds, the useful question is what `PIndivisibleWithin` adds on top of
   class membership. Act 1 located the answer in the external framework — the interference term of
   arXiv:2302.10778v3 §3.5 eq (43) — and whether the OI processes of §2.3 make that term nonzero, at
   what horizon, is well posed and untouched here.
3. **The horizon question of §5**, if a later round decides it is worth posing precisely.

## 7. What this round does not claim

Explicitly, as the freeze requires:

- **Nothing here is a claim about any Barandes predicate.** `PDivisibleCol` is this programme's own
  `PDivisible` written in the opposite orientation. The theorems say the two orientations are the
  same predicate under transposition. They say nothing about what any external text's predicate is,
  and act 1's `BD3` and `BR3` are neither reopened, softened, nor re-derived.
- **Nothing here is a sourcing claim.** A transposition identity is a fact about matrices. It does
  not describe OI as sourcing any resource, and Arc D round 1's boundary stands intact.
- **No primary source was consulted.** The round needed none, and act 1's determinations are cited
  rather than re-litigated.
- **No manuscript, book, bibliography or publication edit occurs.** The Explainer surface act 1
  flagged remains on the backlog, untouched.
- **Track separation is observed both ways.** Nothing here is evidence for a Track I result, and no
  Track I result was used here.
- **No fifth condition is named or adopted**, no deferred Arc D resource is adjudicated, and no
  merged Arc B, C or D result is reopened, restated or re-proved.
