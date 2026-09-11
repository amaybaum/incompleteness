# Track B act 7 — the dilation-choice round: result

Frozen preregistration: commit `06ea197f02e736dbeb4247c0ecd0f57f9b381a73`, blob
`810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19`, merged to `main` by PR #572.

Executed from `main` at `ba571a589a6942ba9a93679997ee92c9f717448a`, the merge of that freeze.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** Every coordinate below is read off the
**authoritative surface**: the PDF of arXiv:2302.10778v3, verified by its p. 1 stamp
`arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`, title *The Stochastic-Quantum Correspondence*, dated
June 30, 2025.

## Outcome

**`DC2a` — §3.4's input contract is not met by the off-direct witness.**

Reached by the route the stop table fixes: **D1 answered, D2 FAILS on an inherited hypothesis,
layer 2 not reached.**

**The failed hypothesis, named:** Source A's **time-domain and continuity contract**, inherited from
§2.1 and §2, against our `ℕ`-indexed discrete off-direct witness.

- **p. 3, §2.1:** "the set of target times `t` will usually be assumed to be **isomorphic to the real
  line ℝ**, up to a choice of measurement units … the target time `t` is treated here as a
  **real-valued variable**".
- **p. 4, after (5):** "On physical grounds, `Γ(t ← t₀)` will be assumed to satisfy the **continuity
  condition** that in the limit `t → t₀`, it approaches its value `Γ(t₀ ← t₀)`, which will be taken
  to be the `N × N` identity matrix `𝟙`".

Act 6's `UB2` witness is literally `Γ : ℕ → Matrix (Fin 2) (Fin 2) ℝ`. On `ℕ` with `t₀ = 0` the limit
`t → t₀` carries no content, and the target-time set is not isomorphic to `ℝ`. The witness therefore
does not instantiate the contract Source A states.

**This is a stop, not a refutation of anything.** `DC2a` says the round's own off-direct witness is
outside the input contract of the construction under test. It says nothing about whether the dilation
moves the visible candidate, and nothing about Source A's adequacy.

## The layer-1 record

### D1 — what object is dilated: **Θ(t ← 0)**, by enlarging the configuration space

§3.4, p. 10: "if `Θ(t ← 0)` is not **already** a unitary matrix, then one can **turn it into** a
unitary matrix by enlarging or **dilating** the original `N`-element configuration space `C` to one
containing at most `N³` configurations. One can then formally regard the original indivisible
stochastic process as a **subsystem** of this dilated stochastic process."

The dilated object is the **time-evolution operator**, not the visible transition family. `Θ` is
itself already a non-unique choice upstream of the dilation — (12) p. 6 defines it by
`Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²`, and p. 7 records that it "is guaranteed to exist, although it is not
unique".

### D2 — the input contract, in Source A's orientation, including what it inherits: **FAILS**

**Orientation, first.** Source A's normalization (3) p. 4 is `∑_{i=1}^{N} Γ_ij(t ← t₀) = 1` — over the
**first** index — and p. 4 names the object "a **(column) stochastic matrix**". This is the external
column-stochastic orientation the freeze requires the contract be tested in. Act 6's
`transpose_nonneg` and `transpose_isColStochastic` give exactly non-negativity and first-index
normalization for `(Γ t)ᵀ`, so the **orientation half of the contract is met** by the transposed
object, with act 2's `RT1` as the licence for the move.

**Hypotheses §3.4 states locally**, each met by our witness at each `t`:

| Hypothesis | Coordinate | Our witness |
| --- | --- | --- |
| `C` finite, `N` configurations | p. 3 | `Fin 2` ✓ |
| Non-negativity of `Γ` entries | (2) p. 4 | `transpose_nonneg` ✓ |
| Normalization over the first index | (3) p. 4 | `transpose_isColStochastic` ✓ |
| `Θ` exists with the summation condition | (12) p. 6, (13) p. 7 | follows ✓ |
| Kraus operators and the Kraus identity | (25), (26) p. 10 | follows ✓ |

**Hypotheses inherited from §2, and the failure:**

| Hypothesis | Coordinate | Our witness |
| --- | --- | --- |
| `Γ(t₀ ← t₀) = 𝟙` | p. 4 | `Γ 0 = 1` ✓ |
| Target times isomorphic to `ℝ`; `t` real-valued | p. 3 | **`ℕ`-indexed — FAILS** |
| Continuity: `Γ(t ← t₀) → 𝟙` as `t → t₀` | p. 4 | **no content on `ℕ` — FAILS** |

**What was considered, and why it does not narrow the contract.** Two observations cut the other way
and are recorded rather than suppressed: §3.4's Stinespring step is applied at a fixed `t` and does
not itself invoke continuity, which is consumed downstream at (33) p. 12 where the source explicitly
adds "differentiable function of the time `t`"; and the source exhibits discrete-time instances of
its own, at footnote 11 p. 12 and at (57)–(58) p. 19, which give a discrete-time Markov chain over
integer `n`. **Neither licenses narrowing D2 to §3.4's own sentences.** The freeze states that the
list "is **not** limited to hypotheses §3.4 restates locally" and that "scoping D2 to §3.4's own
sentences would be the way to miss a genuine `DC2a`" — a clause written before the source was read,
against exactly this move. A contract narrowed after reading the source is not the contract that was
frozen.

### D3 — the freedoms, inventoried

| Freedom | Coordinate | Status |
| --- | --- | --- |
| `Θ` not unique | p. 7 | **examined** |
| Choice of number system for `Θ` (reals, complex, quaternions, "a more general algebra") | p. 7 | **examined** — act 5's `F2`, still not exhibited |
| Time-dependent phase gauge `Θ_ij ↦ exp(θ_ij(t))Θ_ij` | footnote 6, p. 7 | **examined** — act 5's `F1` |
| Kraus decompositions "(non-unique)" | p. 10 | **recorded, not examined** |
| Ancilla size: `N′ ≤ N²`, `N̄ ≤ N³` — bounded, not fixed | §3.4 p. 10 | **recorded, not examined** |
| Initial ancilla configuration `j′` — "for **at least some** choices" | §3.4 p. 10 | **recorded, not examined** |
| The dilated `Ũ(t ← 0)` itself — Stinespring gives **existence** only | §3.4 p. 10 | **recorded, not examined** |

**Cross-time coherence: the source provides none, and the asymmetry is citable.** §3.4's assertion is
**per-`t`**: the Stinespring theorem "implies the **existence** of an `Ñ × Ñ` unitary time-evolution
operator `Θ̃(t ← 0) = Ũ(t ← 0)` whose corresponding … transition matrix `Γ̃(t ← 0)` yields the
original … `Γ(t ← 0)` by marginalization" (p. 10). Existence is asserted at each `t` separately. The
source does **not** fix, prove, or assume a coherently chosen time-indexed family `{Ũ(t ← 0)}_t`, and
states no regularity for one.

The contrast with the undilated case is sharp and is the point: where the source needs regularity of
a unitary family it says so explicitly — (33) p. 12 assumes `U(t ← 0)` is "a differentiable function
of the time `t`" — and it imposes no analogue on `Ũ`. Meanwhile the relative operator (39) p. 13
consumes **two** times. So a coherent dilated family is presupposed by any relative construction on
the dilated carrier and is supplied nowhere.

This freedom is **recorded as open** and is unaffected by the `DC2a` stop: it is a property of the
source's text, not of our witness.

### D4a, D4b — **not reached** as outcome-bearing tests

The stop table routes `DC2a` to "layer 2 **not reached**", and D4's answers are outcome-bearing only
for the branch between `DC2b` and the readback path. They are recorded **not reached — the source
layer stopped the round**, never *unresolved*.

**A counterfactual source reading is recorded, and it is NOT outcome-bearing.** Conditional on D2
being repaired by a source-admissible witness, the reading is **D4a positive / D4b negative**:

- **D4a positive.** §3.4 p. 10 says the original process "may be regarded as a subsystem of this
  dilated stochastic process" and constructs `Ũ(t ← 0)`; (28) p. 11 then says that "without any real
  loss of generality … one can focus on the case in which the time-evolution operator is unitary",
  dropping the tildes; and §3.5 p. 13 defines the relative operator
  `U(t ← t′) ≡ U(t ← 0)U†(t′ ← 0)` for **any** unistochastic process with unitary `U(t ← 0)`. The
  dilated process is such a process.
- **D4b negative.** §3.4 supplies marginalization back to the original carrier **only for the rooted
  object**, `Γ̃(t ← 0) → Γ(t ← 0)` at fixed initial ancilla configuration `j′` (p. 10). It supplies
  **no** general map carrying the relative candidate `|Ũ(t ← t′)|²` back to `V`. §3.7 does not repair
  this generically: it does form a relative operator on a composite carrier (46) p. 17 and does
  marginalize back to the subject carrier (50) p. 18, landing on
  `Γ^S_{ii′}(t ← t′) ≡ |U^S_{ii′}(t ← t′)|²` at (52) p. 18 — but only under the idealized correlation
  condition (45) p. 17 and the tensor-factorization condition (46) p. 17, neither of which the source
  states of a generic Stinespring dilation. Importing them would be constructing on the source's
  behalf, which act 4 declined and this round declines likewise.

**This reading settles nothing in this round.** It is recorded so the next round starts from a known
position rather than re-deriving it, and it would route to the **readback-amendment path**, not to
`DC2b`, if and only if D2 is first repaired.

### D5a, D5b — **not reached**

Act 3's padding theorem bears only on layer 2's witness comparison, which is not reached. Recorded
**not reached — the source layer stopped the round**. No determination of the shape condition or the
quantity-identification condition is made or relied on anywhere in this round.

### D6 — the source acknowledges the freedoms

p. 7 ("guaranteed to exist, although it is not unique"); footnote 6 p. 7, the time-dependent phase
gauge, which "alter[s] the structure of the resulting Hilbert-space representation … including the
dynamics, in such a way that all empirical results remain unchanged"; end of §3.2 p. 9, that the
objects "are not uniquely defined by `C` or by `Γ(t ← 0)`"; p. 10, Kraus decompositions as
"(non-unique) generalizations". **Corroboration only** — no admissibility judgement in this round
rests on any of these, per the freeze.

## What is not reached

`T1` (the visible screen), `T2` (admissibility), `T3` (the readback), `T4` (both witnesses), witness
B's construction, and **all Lean** are **not reached**. No module is written, no definition is
introduced, no census entry is added. `DC1`, `DC3` and `DC4` are **not reached**, and none of them is
*unresolved*: the layer-1 stop is a different status and the two are never interchanged.

## What this licenses, and what it does not

**Licensed.** Source A's dilation, as stated, runs on a time-domain contract our frozen off-direct
witness does not meet. The obligation act 6 identified — that a full-class route must handle the
dilated branch — is therefore **not yet testable on the witness we have**.

**Not licensed.** Nothing here says the dilation is inapplicable to OI, that the correspondence
fails, that the dilation does or does not move the visible candidate, or that Source A requires an
additional principle. Nothing here revises `BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1` or `UB2`;
acts 1 through 6 are not reopened. Nothing here is a sourcing claim, in either track direction, and
no candidate-selection principle is adopted or proposed. No manuscript is edited.

## Prediction, and whether it held

**It did not hold, and the miss is informative.** The freeze predicted `DC2b` at roughly one in three
and otherwise expected layer 1 to pass, with the prior "tilted toward `DC1`". It attached no
probability to `DC2a` at all, carrying it only in the grid and the stop table. The actual stop is
`DC2a`, and the reason it was reached is the clause the review process added late: D2's extension to
**inherited** prerequisites, together with the sentence that "scoping D2 to §3.4's own sentences
would be the way to miss a genuine `DC2a`". Without that clause this round would have passed layer 1
on §3.4's local sentences alone and run a divergence test against a witness outside the source's
stated contract — reporting a `DC2b` or a `DC1`/`DC3` that the contract did not support.

## What remains open, and the next obligation

**The next obligation is specific and replaces the dilation round rather than cancelling it:**

> **Construct a continuous, Source-A-admissible, off-direct OI/`PPer` witness — or prove that no such
> witness exists under the OI constraints.**

If such a witness exists, act 7 reopens at exactly **D4a positive / D4b negative**, which triggers the
readback-amendment path, at reduced strength, per the frozen stop table.

**A hazard on that route, recorded from the source.** Footnote 11, p. 12 gives Source A's own
discrete-to-continuous interpolation: with `δt` the discrete time step and `Σ` a permutation matrix,
`Γ_ij(n δt + t ← n δt) ≡ |(Σ^{t/δt})_ij|²` "defines a **unistochastic** matrix that analytically
interpolates the original discrete, deterministic process to a smooth, unistochastic process". That
interpolation lands **on** the direct branch, which is the wrong side for an off-direct witness. So
the obvious route to continuizing our witness may be exactly the route that destroys the property the
witness exists to have. This is recorded as a signpost, not as a proof that the construction is
impossible.

**Also open, and untouched by the stop:** whether the OI visible class has a continuous-time
formulation at all — Arc B's `C_OI(V) = PPer(V)` is defined over `ℕ` with a periodicity condition,
and extending it is a question for Track I rather than a corollary of anything here. And D3's
cross-time coherence gap stands on its own as a property of Source A's text.

## Evidence level

Act 1's **level 3 — a reading of the accepted text**, throughout. No theorem is proved in this round
and none is claimed. The `DC2a` determination is an audit determination about a stated contract, not
a mathematical result about dilations.
