# Track B act 5 — Source A's candidate selection: result

Frozen preregistration: commit `4fe593986f113fa431e12f7a061eb927ae849e95`, blob
`d4180a572297f31932aea2de41dff7d1e1fcb789`, merged to `main` by PR #568.

Executed from `main` at `7c77a8e45d49bf2d2b8bbdbeb007fd978a063920`, the merge of that freeze.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated**, per the freeze. Every coordinate below
is read off the **authoritative surface**: the PDF of arXiv:2302.10778v3, which self-identifies by
its p. 1 stamp `arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`.

## Outcome

**`SA2` — selection conditional on a named extra datum.**

Reached by the route: **A1 *identified*, A2 affirmative, A3 complete, A4 not invariant (exhibited),
A5 *determinate given a named parameter*, A6 a named third rule.** All six questions are reached
and answered; none is *not reached*.

Source A **does** form a visible intermediate candidate as part of its own development —
`Γ_ik(t ← t′) ≡ |U_ik(t ← t′)|²` at eq (42), p. 14 — and it is load-bearing across four subsections.
But evaluating it consumes, over and above the base stochastic datum, a **choice of unitary lift**
`U(s ← 0)` of that datum, constrained only by `Γ_ij(s ← 0) = |U_ij(s ← 0)|²` at (30). Two lifts are
exhibited below that agree with the base datum **at every time** and induce the **identity** and the
**swap** as the visible intermediate candidate.

**The datum `SA2` names is that choice of unitary lift** — A3's Layer 2, a parameter the construction
consumes in addition to A3's Layer-1 base stochastic datum, and not fixed by it. Per the freeze, this
means a freedom internal to Source A's construction; it is **not** a datum missing from our side, and
nothing here says anything about what our `RootedRealization` supplies.

**Scope.** `SA2` is established on the **direct unistochastic branch** that eq (39) assumes. The
non-unistochastic case, where §3.4's dilation is invoked first, is not adjudicated here.

### The structural fact underneath

Source A contains **two** relative-time objects, and the audit turns on the difference between them.

| | Definition | Computed from | Stochastic? | Fixed by the visible data? |
|---|---|---|---|---|
| eq (37), p. 13 | `Γ̃(t ← t′) ≡ Γ(t ← 0) Γ⁻¹(t′ ← 0)` | `Γ` alone | **no** — "not generically stochastic" | **yes**, but only where `Γ(t′ ← 0)` is invertible — a condition (37) states and the witness below does not meet |
| eq (42), p. 14 | `Γ_ik(t ← t′) ≡ \|U_ik(t ← t′)\|²` | `U` | **yes** — "manifestly unistochastic" | **no** |

The object computable from the visible data alone is not a candidate; the object that is a candidate
is not computable from the visible data alone. That dichotomy is the round's finding, and it is
Source A's own structure, not an artefact of how this round reads it.

## A1 — identification of the object: **identified**

**The object is `Γ_ik(t ← t′) ≡ |U_ik(t ← t′)|²`, eq (42), §3.5 "Interference", p. 14.** Type: a
**visible (stochastic) matrix** — Source A calls it "manifestly unistochastic" — indexed from an
intermediate time `t′` to a later time `t`, for any two times with `t > t′ > 0`.

It is built from the **relative time-evolution operator** at eq (39), p. 13:

> "suppose that `Γ(t ← 0)` is unistochastic, with unitary time-evolution operator `U(t ← 0)`. Then,
> for any two times `t` and `t′`, one can define a relative time-evolution operator
> `U(t ← t′) ≡ U(t ← 0) U†(t′ ← 0)`"

with the composition law `U(t ← 0) = U(t ← t′) U(t′ ← 0)` at eq (40), p. 14.

**Why eq (42) and not eq (37).** Source A first tries the object built from the visible data alone:
`Γ̃(t ← t′) ≡ Γ(t ← 0) Γ⁻¹(t′ ← 0)` at eq (37), p. 13, giving `Γ(t ← 0) = Γ̃(t ← t′) Γ(t′ ← 0)` at
(38), which "resembles the divisibility condition". Source A then rules it out, p. 13: "the inverse
of a stochastic matrix can only be stochastic if both matrices are permutation matrices and,
therefore, do not involve nontrivial probabilities. Hence, the matrix `Γ̃(t ← t′)` defined above is
**not generically stochastic**, so one does not obtain a genuine form of divisibility." A matrix that
is not stochastic is not a visible intermediate candidate, so (37) is not the A1 object.

**Eq (37) is moreover only conditionally defined.** Source A states the hypothesis at p. 13 —
"suppose that at some time `t′`, the transition matrix `Γ(t′ ← 0)` **has a matrix inverse**
`Γ⁻¹(t′ ← 0)`" — so (37) is available only where `Γ(t′ ← 0)` is invertible. The witness used at A4
below does **not** meet that condition: its `Γ(t′ ← 0) = [[1/2, 1/2], [1/2, 1/2]]` is singular. This
does not weaken the dichotomy — (37) is already disqualified as a candidate on Source A's own
stochasticity grounds, which is the disqualification that matters — but the qualifier belongs on the
table, and the note does not claim (37) is available everywhere.

**The other three located sites are instances of the same construction, not rivals.** S2 §3.7 p. 17
eq (46) forms a composite-system relative time-evolution operator and factorizes it; S3 §3.9 p. 21
eqs (65)–(66) form a relative transition matrix `Γ^AB(t ← t″)` and factorize it; S4 §4.2 pp. 23–25
eqs (73)–(77) form a hybrid relative transition matrix, with (77) written as
`… = Σ |U_{d d(α′)}(t ← t′)|² |Ψ̃_{α′}(t′)|²` — the same `|U(t ← t′)|²` readout in a measurement
setting. A1 therefore identifies **one object with three further instances**, which is one of the
outcomes the freeze's four-site table explicitly allowed.

## A2 — construction or post-processing: **part of the construction**

Affirmative, and the burden the freeze places on the affirmative is met by the source's own use of
the object rather than by its appearance on a page.

- **Defined by the source**, at (39) and (42), in the source's own voice ("one can define").
- **Relied on for the source's headline result about interference.** Eq (43), p. 14, computes
  `Γ_ij(t ← 0) − [Γ(t ← t′)Γ(t′ ← 0)]_ij = Σ_{k≠l} U_ik(t←t′) Ψ_k(t′) conj(U_il(t←t′)) conj(Ψ_l(t′))`,
  of which Source A says, p. 14: "the right-hand side of (43) gives **the general mathematical
  formula for quantum interference**, despite the absence of manifestly quantum-theoretic
  assumptions."
- **Carried forward into three further developments** — S2's division events and the Markov
  approximation, S3's entanglement factorization, S4's measurement process, where (77) is what
  "implies that the time `t′` is a division event".

Defined, carried forward, and relied upon. **This round invents nothing on Source A's behalf**: the
relative operator and its modulus-square readout are both written down by Source A.

## A3 — provenance of the inputs: complete

Every input is listed, **in two layers that the audit must not run together**. The distinction is
the whole of A3's significance, and it is what makes A5's answer sayable without circularity.

### Layer 1 — the base stochastic datum

| Datum | Citation |
|---|---|
| the transition-matrix family `Γ(s ← 0)` over the times in play, in particular at `s = t′` and `s = t` | §3.1–§3.2; the object the whole construction is about |
| **presupposition:** each such `Γ(s ← 0)` is **unistochastic** | eq (39)'s own preamble, p. 13 |

Source A defines unistochastic at §3.4, pp. 10–11 — `Θ(t ← 0) = U(t ← 0)` at (28), and
`Γ_ij(t ← 0) = |U_ij(t ← 0)|²` at (30), p. 11, with p. 11 stating it in words: "a unistochastic
matrix is a square matrix whose individual entries are the modulus-squares of the corresponding
entries of a unitary matrix." §3.4, p. 10 argues the presupposition is "without any real loss of
generality", because a non-unitary `Θ(t ← 0)` can first be dilated to a unitary one — a step whose
consequences for this round are scoped under F4 below.

### Layer 2 — the extra construction parameter

| Parameter | Citation |
|---|---|
| a **choice of unitary lift** `U(s ← 0)` of the base datum — any unitary with `\|U_ij(s ← 0)\|² = Γ_ij(s ← 0)`, per (30) | eq (39) takes such a `U` as given: "suppose that `Γ(t ← 0)` is unistochastic, **with unitary time-evolution operator** `U(t ← 0)`" |

Evaluating (39) and (42) consumes the lift at the two times in play, `U(t ← 0)` and `U(t′ ← 0)`:
(39) composes exactly those two, and (42) takes entrywise modulus-squares. Nothing else enters.

### Why the two layers are different

Eq (30) determines `Γ` from `U`; it does not determine `U` from `Γ`. **The lift is therefore an
input the construction consumes over and above the base stochastic datum**, and A4 asks whether that
under-determination reaches the candidate. It is this **Layer-2 parameter**, not the Layer-1 datum,
that A5 names — so the `SA2` datum is a choice not fixed by the base stochastic datum, rather than a
restatement of the data A3 listed.

**Not asked here, per the freeze:** whether our merged `RootedRealization` supplies either layer.
That is the containment question deliberately deferred to the tuple-instantiation step, and it is
recorded open below.

## A4 — invariance under the source's own freedoms: **not invariant**

Four freedoms Source A permits on these inputs, enumerated.

### F1 — the freedom in the unitary lift. **Examined. The object is NOT invariant.**

**The admissibility ground is definitional, and does not rest on footnote 6.** Source A's own
statement of the construction is what licenses the two choices below:

- p. 11, defining the presupposition: "a unistochastic matrix is a square matrix whose individual
  entries are the modulus-squares of the corresponding entries of a unitary matrix", with (30)
  `Γ_ij(t ← 0) = |U_ij(t ← 0)|²`;
- eq (39)'s preamble, p. 13: "suppose that `Γ(t ← 0)` is unistochastic, **with unitary
  time-evolution operator** `U(t ← 0)`."

So (39)'s only condition on the lift is (30). **Any** unitary whose entrywise modulus-squares are
`Γ(s ← 0)` is an admissible `U(s ← 0)` for that base datum, by Source A's own statement — and
diagonal unitary factors leave entrywise moduli untouched, so `U(s ← 0)` and `U(s ← 0)D(s)` are both
admissible lifts of the **same** base datum, for any diagonal unitary `D(s)`.

**Footnote 6, p. 7 corroborates rather than carries this.** Source A states the non-uniqueness at
§3.1, p. 7, on eq (12) `Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²` (which p. 6 calls "not a postulate—it is a
mathematical identity"):

> "The `N × N` matrix `Θ(t ← 0)` introduced here is guaranteed to exist, although it is **not
> unique**, so one can view it as metaphorically akin to a 'potential' for `Γ(t ← 0)`"

and names the resulting freedom in footnote 6, p. 7:

> "This nonuniqueness implies a previously unrecognized form of **gauge invariance** for all quantum
> systems, in which one changes the individual entries `Θ_ij(t ← 0)` by **arbitrary, time-dependent
> phase factors**: `Θ_ij(t ← 0) ↦ exp(θ_ij(t)) Θ_ij(t ← 0)`. These gauge transformations then alter
> the structure of the resulting Hilbert-space representation ahead, **including the dynamics**, in
> such a way that all empirical results remain unchanged."

with §3.2, p. 9 adding that `Θ(t ← 0)`, `ρ(t)`, `Ψ(t)` and `A(t)` "do not naturally have direct
physical meanings, in part because **they are not uniquely defined by `C` or by `Γ(t ← 0)`**."
Right-multiplication by a diagonal unitary is the case `θ_ij(t) = β_j(t)` of footnote 6's per-entry
phases and preserves unitarity, so the transformation used below is inside that freedom too. **But
the counterexample does not depend on that reading**, and deliberately does not rest on it:
footnote 6's separate sentence about empirical results could otherwise be read as restricting which
transformations count as gauge, making the citation circular. The definitional ground above is free
of that.

**The counterexample, at the level of the whole stochastic family.**

Let `Γ(s ← 0)` be any base datum admitting a lift `U(s ← 0)` with
`U(t′ ← 0) = U(t ← 0) = H`, where `H = (1/√2)[[1, 1], [1, −1]]` is the real Hadamard — admissible
since `|H_ij|² = 1/2` for every entry, giving

    Γ(t ← 0)  =  Γ(t′ ← 0)  =  [[1/2, 1/2], [1/2, 1/2]]

Such a lift exists: `U(2)` is path-connected, so a family running from `U(0 ← 0) = 𝟙` through `H` at
`t′` and again at `t` can be chosen, and it fixes the base datum it realizes.

Now take **any diagonal-unitary-valued function of time** `D(s)` with

    D(0) = D(t′) = 𝟙 ,        D(t) = diag(1, −1)

— for instance `D(s) = diag(1, exp(iπ f(s)))` with `f` smooth, `f(0) = f(t′) = 0`, `f(t) = 1`, so
`D` may be taken **smooth**, and the construction never relies on a discontinuity — and set

    U′(s ← 0)  ≡  U(s ← 0) D(s) .

Then `U′` is a lift of the **same base datum at every time**:
`|U′_ij(s ← 0)|² = |U_ij(s ← 0)|² = Γ_ij(s ← 0)` for **every** `s`, since `D(s)` is diagonal unitary;
and `U′(0 ← 0) = 𝟙` is preserved. The two lifts are indistinguishable in the entire visible family.

Their relative readouts at `(t, t′)` are not:

- **from `U`:** `U(t ← t′) = H H† = [[1, 0], [0, 1]]`, so

      Γ(t ← t′)  =  [[1, 0], [0, 1]]     — the identity

- **from `U′`:** `U′(t ← t′) = H·diag(1, −1)·H† = [[0, 1], [1, 0]]`, so

      Γ(t ← t′)  =  [[0, 1], [1, 0]]     — the swap

**What this establishes, and why the family-level form is the one the burden needs.** Both lifts are
admissible by (30)/(39); they agree with the base stochastic datum **at every time**, not merely at
the two endpoints in play; and they induce different visible intermediate candidates. So the choice
of lift is not fixed by the base stochastic datum, and the candidate moves with it.

**This is a visible counterexample, not an operator-level one**, as the freeze requires: the two
matrices displayed are the candidates themselves, after the modulus-square readout, not the
operators behind them.

### F2 — the choice of number system for `Θ`. **Not examined.**

§3.1, p. 7: the entries "could be taken to be the real square roots of the corresponding quantities
`Γ_ij(t ← 0)`, but they could also include complex numbers, quaternions, or even the elements of a
more general algebra", with Source A choosing "only the complex numbers at most". This round does not
examine whether a different algebra changes the candidate.

### F3 — unitary representatives outside the `E U D` orbit. **Not examined.**

Eq (30), p. 11 admits **any** `U′` with `|U′_ij|² = Γ_ij(t ← 0)`, a set generally larger than
`{E U D}`. Not separately examined, and the direction matters: enlarging the admissible set can only
add candidate values, never remove the two already exhibited.

### F4 — the Stinespring dilation freedom. **Not examined.**

§3.4, p. 10: an ancillary configuration space `C′` "of some size `N′ ≤ N²`", dilated size `Ñ ≤ N³`,
with the marginalization holding "for at least some choices of the ancilla's configuration `j′` at
the initial time 0". This round does not exhibit two admissible dilations changing any visible
candidate, so — following act 4's discipline exactly — it is recorded as **representation freedom**
and is **not** named as a candidate-selection datum.

### The branch this round settles, and why no unexamined freedom bears on A5 within it

**`SA2` is established on the direct unistochastic branch**, and the note claims it there and not
beyond. Eq (39) assumes a unistochastic `Γ(t ← 0)` outright, so the branch is exactly the one the
construction addresses without a prior dilation, and the family-level counterexample refutes
canonical selection **within it**: two lifts admissible by (30)/(39), agreeing with the base datum at
every time, inducing different candidates.

On that branch the `SA4` boundary is clean. The freeze routes to `SA4` if A4 leaves unexamined a
permitted freedom **that bears on A5**, whose three answers are *unique*, *determinate given a named
parameter*, and *unresolved*. F1 is examined and **rules out *unique* by exhibition**; fixing the
lift fixes the candidate outright, which rules out *unresolved*. F2 and F3 are freedoms in choosing
the lift, so they can only enlarge the set of reachable candidates — neither restores uniqueness nor
un-determines the object once the lift is fixed. So A5's answer is pinned, and `SA4` is not
triggered.

**F4 is scoped, not dismissed.** It is **not** claimed globally irrelevant to A5. On the
unistochastic branch F4 is never invoked, because no dilation is needed for (39) to apply — which is
why it does not bear on the answer *here*. For a **non-unistochastic** visible process, §3.4, p. 10
has Source A dilate first, and the dilation choice may then become load-bearing for the induced
relative candidate. **That case is not adjudicated by this round**, and whether the generic process
even needs the dilation is part of the containment question the freeze defers to the
tuple-instantiation / formal-mapping step.

What remains open on the settled branch is the **completeness of the parameter list**: the parameter
named at A5 is F1's, and a later round needing the full list must examine F2 and F3 — and, on the
dilated branch, F4.

## A5 — uniqueness after the visible readout: **determinate given a named parameter**

Not unique: the counterexample above gives two admissible values from lifts that agree with the base
stochastic datum **at every time**.

Determinate once the parameter is fixed: given the lift at the two times in play, eq (39) and eq (42)
determine `Γ(t ← t′)` outright, with no further choice.

**The named parameter is A3's Layer 2 — the choice of unitary lift** `U(s ← 0)` satisfying (30),
evaluated at `t` and `t′`. It is not A3's Layer 1: the base stochastic datum is held fixed across
both choices, which is exactly what the family-level counterexample establishes. What the candidate
depends on is the *relative* part of the lift between the two times — the counterexample's readout
depends on `D(t) D(t′)†` alone.

This is what makes `SA2`'s datum sayable without circularity: **the parameter is a choice the
construction consumes in addition to the base datum, not a restatement of that datum**.

**An observation recorded at its own scope, not adjudicated.** Since `Γ(t ← t′)` moves under F1,
eq (43)'s discrepancy `Γ(t ← 0) − Γ(t ← t′)Γ(t′ ← 0)` moves with it, its two other terms being
gauge-invariant. Source A separately reads that discrepancy empirically, §3.6, p. 15: "relative phase
factors in state vectors have clear empirical signatures", and "there will generically be a
quantitative discrepancy between the system's actual behavior—as predicted theoretically or measured
empirically—and predictions made for the system based on a heuristic-approximate divisible or
Markovian approximation." **This round does not adjudicate how those two readings sit together.**
Nothing here says Source A is mistaken, that interference lacks empirical content, or that the
discrepancy is unmeasurable — an operational specification of the divisible approximation might fix
the representatives by means this round has not examined. It is recorded as **open** below, and it is
the sharpest open question the round produces.

## A6 — identification in our vocabulary: **a named third rule**

Not `initWeight`'s and not `uniformWeight`'s, and the reason is structural rather than a matter of
computing and comparing: those two are `FibreWeight`s, consumed by `candidateOf` together with
`bornPow` over a **hidden carrier**. Source A's rule consumes no fibre structure and no hidden
carrier, and our two rules consume no unitary representative. The constructions do not have the same
inputs, so neither of our frozen rules can be the one Source A's development produces.

**The third rule, stated explicitly enough for a later act to define it, and deliberately not defined
here** — as `SA2` requires, a **parameterized family** rather than a single rule:

> Given visible `Γ(t ← 0)` and `Γ(t′ ← 0)`, both unistochastic, and given as parameter a choice of
> unitary representatives `U(t ← 0)`, `U(t′ ← 0)` with `|U(t ← 0)_ij|² = Γ_ij(t ← 0)` and
> `|U(t′ ← 0)_ij|² = Γ_ij(t′ ← 0)`, the candidate is the entrywise modulus-square of
> `U(t ← 0) U†(t′ ← 0)`.

The family is indexed by the representatives; the counterexample shows the index is not redundant.

**No candidate-selection principle is adopted or proposed.** Naming the family is A6's frozen job;
selecting a member of it is not, and this round selects none. No Lean definition is written.

## What act 3's `CU1a` retains, and the programme-level reading

**`CU1a` is preserved exactly and is not revised.** It states that the merged OI → `QfbData` bridge
does not select the candidate at this interface; it is a theorem about **our** bridge, and act 5
audits an external construction and touches no this-side object.

**Act 4's `MP4` is unrevised**, Source C is not re-adjudicated, and **no amendment authorizing a
candidate-extraction rule has been made** — here or as a consequence of anything found here.

**What changes at programme level, at the scope the evidence supports.** Before act 5 it was open
whether Source A's relative-time machinery defines a visible intermediate candidate. It does, and it
is load-bearing. What is now also determinate is that the candidate it defines is **not fixed by the
visible transition data**: it depends on a choice Source A itself names as gauge. So the missing
selection is located rather than supplied — `SA2` is the most valuable answer short of `SA1`
precisely because it names the datum instead of leaving it as "something is missing".

**What this does not license.** Not that the external framework requires an additional physical
principle — forbidden by act 3's frozen licence, and not earned. Not that the selection is
unavailable: an operational or dynamical specification could fix the representatives, and this round
did not look. Not any claim that Source A's treatment is better than, equivalent to, agrees with, or
supersedes Source C's — **all four are outside this round's scope by the freeze**, and whether the
two agree is recorded open. Not a theorem-level claim about Source A: this is an audit of a
construction, and the theorem's own statement would have to say so.

## Direction, stated per the freeze

Every claim above is about **Source A's construction on Source A's own data**.

**No claim here establishes the forward obligation**, which would require our source-side datum to be
mapped onto Source A's inputs — precisely the containment question the freeze defers. **No claim here
establishes the backward obligation** either; it was not attempted and is not assumed.

## Evidence level

An **audit determination, not a theorem** — act 1's evidence levels 1 and 3, never at level 2. The
counterexample at A4 is a worked example on the source's stated equations: level 3, not
kernel-checked. **No Lean module is written in this round**, and no this-side definition is
introduced.

## Prediction, and whether it held

The freeze recorded **no prediction** on `SA1` versus `SA2` versus `SA4`. Nothing to score there.

It recorded **`SA3` unlikely**, on the location check and that alone, with the live path to `SA3`
named: every one of the four sites could still have failed A2 by being expository rather than
load-bearing. That **held** — and the reason it held is not the reason the location check suggested.
The object is load-bearing not because it appears at four sites but because eq (43) depends on it,
and (43) is Source A's interference formula.

## What remains open

- **Whether the gauge-dependence of `Γ(t ← t′)` is reconcilable with §3.6's empirical reading of the
  discrepancy at (43).** The sharpest question this round produces. Settling it needs the operational
  content of "a heuristic-approximate divisible approximation" pinned down well enough to say whether
  it fixes the representatives — which this round did not examine and the freeze did not ask for.
- **Whether our merged `RootedRealization` supplies Source A's inputs** — that is, whether our
  visible data is unistochastic at all, and whether our datum determines a unitary lift.
  Deliberately deferred by the freeze to the tuple-instantiation / formal-mapping step, which is
  second on the frontier. **If our visible data is not unistochastic**, §3.4's dilation is invoked
  before (39) applies, and F4 stops being an unexamined side freedom and becomes load-bearing for
  the induced candidate — so that step decides which branch this route is even on.
- **The non-unistochastic branch**, on which `SA2` is not claimed: whether the dilation choice moves
  the induced relative candidate there. Not adjudicated by this round.
- **The completeness of A5's parameter list** on the settled branch, F2 and F3 being unexamined;
  required before any claim that the named parameter is the *only* one.
- **Whether Source A and Source C agree** on any induced candidate. Out of scope by the freeze and
  untouched.
- **Whether any member of A6's family is canonical**, and on what grounds. Answering it would be
  adopting a candidate-selection principle, which no round has been authorized to do.

## Explicitly

- This is an **audit determination, not a theorem**, and no Lean was written.
- **No theorem-level claim about Source A is made.**
- **Act 4's `MP4` is unrevised and no extraction rule has been authorized.**
- **Nothing here claims OI forces quantum structure.**
- **Nothing here is a sourcing claim** — determining what an external construction fixes sources
  nothing about OI physics, and track separation holds both ways.
- **No candidate-selection principle has been adopted**, and A6's family is named, not selected from.
