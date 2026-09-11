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
But it is computed from the **unitary time-evolution operator** `U(t ← 0)`, not from the transition
matrix `Γ(t ← 0)`, and Source A states in its own terms that `U` is fixed by `Γ` only up to a gauge
freedom. Two admissible choices are exhibited below whose visible readouts are the **identity** and
the **swap** on the same `Γ(t ← 0)` and `Γ(t′ ← 0)`.

**The datum `SA2` names is the choice of unitary representatives** — a choice not fixed by the
Source A data A3 lists. Per the freeze, this means a freedom internal to Source A's construction; it
is **not** a datum missing from our side, and nothing here says anything about what our
`RootedRealization` supplies.

### The structural fact underneath

Source A contains **two** relative-time objects, and the audit turns on the difference between them.

| | Definition | Computed from | Stochastic? | Fixed by the visible data? |
|---|---|---|---|---|
| eq (37), p. 13 | `Γ̃(t ← t′) ≡ Γ(t ← 0) Γ⁻¹(t′ ← 0)` | `Γ` alone | **no** — "not generically stochastic" | **yes** |
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

The A1 object `Γ(t ← t′)` is computed from exactly:

| Input | Citation | Note |
|---|---|---|
| `U(t ← 0)` | eq (39), p. 13; introduced at eq (28), p. 11 | the unitary time-evolution operator at the later time |
| `U(t′ ← 0)` | eq (39), p. 13 | the same at the earlier time |

and nothing else: (39) composes exactly these two, and (42) takes entrywise modulus-squares.

**The presupposition on the input process**, stated at (39), p. 13: `Γ(t ← 0)` is **unistochastic**.
Source A defines this at §3.4, pp. 10–11 — `Θ(t ← 0) = U(t ← 0)` at (28) and
`Γ_ij(t ← 0) = |U_ij(t ← 0)|²` at (30), p. 11 — and argues at §3.4, p. 10 that this is "without any
real loss of generality" because a non-unitary `Θ(t ← 0)` can be dilated to a unitary one.

**The inputs are `U`, not `Γ`.** This is the whole of A3's significance and it is worth stating
plainly: eq (30) determines `Γ` from `U`, and does not determine `U` from `Γ`. What A4 asks is
whether that under-determination reaches the candidate.

**Not asked here, per the freeze:** whether our merged `RootedRealization` supplies these inputs.
That is the containment question deliberately deferred to the tuple-instantiation step, and it is
recorded open below.

## A4 — invariance under the source's own freedoms: **not invariant**

Four freedoms Source A permits on these inputs, enumerated.

### F1 — the gauge freedom in `Θ`. **Examined. The object is NOT invariant.**

Source A states the non-uniqueness itself, §3.1, p. 7, on eq (12) `Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²`
(which p. 6 calls "not a postulate—it is a mathematical identity"):

> "The `N × N` matrix `Θ(t ← 0)` introduced here is guaranteed to exist, although it is **not
> unique**, so one can view it as metaphorically akin to a 'potential' for `Γ(t ← 0)`"

and names the resulting freedom in **footnote 6, p. 7**:

> "This nonuniqueness implies a previously unrecognized form of **gauge invariance** for all quantum
> systems, in which one changes the individual entries `Θ_ij(t ← 0)` by **arbitrary, time-dependent
> phase factors**: `Θ_ij(t ← 0) ↦ exp(θ_ij(t)) Θ_ij(t ← 0)`. These gauge transformations then alter
> the structure of the resulting Hilbert-space representation ahead, **including the dynamics**, in
> such a way that all empirical results remain unchanged."

And §3.2, p. 9, on `Θ(t ← 0)`, `ρ(t)`, `Ψ(t)` and `A(t)`: they "do not naturally have direct physical
meanings, in part because **they are not uniquely defined by `C` or by `Γ(t ← 0)`**."

In the unistochastic case `Θ = U` the transformation must preserve unitarity. The unitarity-preserving
subgroup of footnote 6's per-entry phases is `U ↦ E U D` with `E`, `D` diagonal unitaries — the case
`θ_ij(t) = α_i(t) + β_j(t)` — and it leaves `Γ(t ← 0) = |U(t ← 0)|²` unchanged, since diagonal
unitary factors do not change entrywise moduli. So `U` and `E U D` are both admissible
representatives of the **same** visible `Γ(t ← 0)`, under the freedom Source A itself names.

**The exhibited counterexample, at the visible level, as two concrete matrices.**

Take `N = 2`, `H = (1/√2)[[1, 1], [1, −1]]` (real Hadamard), and the same at both times:
`U(t ← 0) = U(t′ ← 0) = H`. This is admissible since `|H_ij|² = 1/2` for every entry, so

    Γ(t ← 0) = Γ(t′ ← 0) = [[1/2, 1/2], [1/2, 1/2]]

a legitimate unistochastic matrix. Now apply F1 at the later time only, taking `D_t` diagonal unitary
and `D_{t′} = 𝟙`; write `D = D_t D_{t′}†`. Then `U(t ← t′) = H D H†`, and the `E` factors drop out
under the modulus-square at (42), so the readout depends only on `D`:

- **`D = 𝟙`:** `H H† = [[1, 0], [0, 1]]`, so

      Γ(t ← t′)  =  [[1, 0], [0, 1]]     — the identity

- **`D = diag(1, −1)`:** `H D H† = [[0, 1], [1, 0]]`, so

      Γ(t ← t′)  =  [[0, 1], [1, 0]]     — the swap

Both choices are admissible under F1. Both leave `Γ(t ← 0)` and `Γ(t′ ← 0)` **exactly** as above.
The visible intermediate candidates are the identity and the swap — different stochastic matrices.

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

### Why no unexamined freedom bears on A5's answer

The freeze routes to `SA4` if A4 leaves unexamined a permitted freedom **that bears on A5**. A5's
three admissible answers are *unique*, *determinate given a named parameter*, and *unresolved*. F1 is
examined and **rules out *unique* by exhibition**; and fixing the representatives fixes the candidate
outright, which rules out *unresolved*. So A5's answer is pinned by F1 alone. F2, F3 and F4 could
each only enlarge the set of reachable candidates — they cannot restore uniqueness and cannot
un-determine the object once the representatives are fixed. **None of them bears on which of the
three answers A5 takes**, so `SA4` is not triggered.

What they *can* affect is the **completeness of the parameter list**, and that is recorded open
rather than claimed settled: the parameter named at A5 is F1's, and a later round needing the full
parameter list — particularly in the dilated case, where F4 is actually invoked — must examine F2–F4.

## A5 — uniqueness after the visible readout: **determinate given a named parameter**

Not unique: the counterexample above gives two admissible values on the same visible data.

Determinate once the parameter is fixed: given `U(t ← 0)` and `U(t′ ← 0)`, eq (39) and eq (42)
determine `Γ(t ← t′)` outright, with no further choice.

**The named parameter: the choice of unitary representatives** `U(t ← 0)` and `U(t′ ← 0)` of the
visible `Γ(t ← 0)` and `Γ(t′ ← 0)` — equivalently, the gauge choice footnote 6, p. 7 names. What the
candidate depends on is the *relative* gauge between the two times: the counterexample's readout
depends on `D = D_t D_{t′}†` alone.

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
  visible data is unistochastic at all, and whether our datum determines a unitary representative.
  Deliberately deferred by the freeze to the tuple-instantiation / formal-mapping step, which is
  second on the frontier.
- **The completeness of A5's parameter list**, F2–F4 being unexamined; required before any claim that
  the named parameter is the *only* one.
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
