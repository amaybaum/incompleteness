# Track B act 4 — the dilation mapping obligation: result

Frozen preregistration: commit `38bbf616314d1f689ac446b4081d407045fd707b`, blob
`3323fc6fc3bbe579dcf34452b147ca12c78e830d`, merged to `main` by PR #566.

Executed from `main` at `e3e36fe7388def725310475d012ad8e1da7d0bb6`, the merge of that freeze.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source C is adjudicated**, per the freeze. Equation and page
numbers below are Source C's throughout.

## Outcome

**`MP2` — the construction maps, and consumes data our side does not determine.**

Every hypothesis of Source C's construction is satisfied by our source-side datum under the
permitted `T₀` and `p` declarations. The construction runs. What it does **not** do is fix a visible
intermediate candidate from the transition data alone: the candidate is determinate only given
choices that `Γ` leaves open, and the round names them.

**Answering the question as posed:** Source C's construction does **not** itself select a visible
intermediate candidate from the stochastic datum we already have. The selection depends on extra
information our datum does not determine.

## M1 — the construction's hypotheses, one at a time

The source-side datum is the merged `RootedRealization V H` read as a tuple, per act 1's Q8:
`Γ_ij(t ← 0) := (rootedMap R t)ᵀ`, with `T₀` and `p` declared alongside. Q8's ledger is inherited,
not re-derived.

| # | Hypothesis | Source C | Status |
|---|---|---|---|
| H1 | input is an indivisible stochastic process `(C, T, T₀, Γ, p, A)`, `C` finite of size `N` | §5.1, p. 20 | **satisfied** |
| H2 | one conditioning time singled out, taken to be `0` | §5.1, p. 20 | **satisfied** (declaration `T₀ = {0}`) |
| H3 | non-negativity (45): `Γ_ij(t ← 0) ≥ 0` | §5.1, p. 20 | **satisfied** |
| H4 | normalization (28), becoming the summation condition (74) | §5.1, p. 20 | **satisfied** |
| H5 | trivialization (46), giving `Θ(0 ← 0) ≡ 𝟙` at (75) | §5.1, p. 20 | **satisfied** |
| H6 | a standalone distribution `p`, forming `ρ(0) = diag(p₁(0), …, p_N(0))` at (84) | §5.4, p. 22 | **satisfied** (declaration; see below) |
| H7 | an algebra `A` of random variables | §5.4, pp. 22–23, eqs (85)–(86) | **satisfied** |

**H1.** `C := V`, a `Fintype`. Membership in the class is by tuple satisfaction; act 1's `BD3`
settled that the class contains Markov chains and that failure of divisibility is not among the
theorem's hypotheses, so nothing further is required of our process. Cited from act 1, not
re-derived. For `V` empty the input is degenerate and `N = 0`; every statement below assumes the
nonempty carrier, as act 3's C2 also required.

**H3.** `rootedMap_isRowStochastic` gives non-negative entries, which transpose unchanged.

**H4.** The same merged theorem gives row sums one, which after transposition is Source C's
column normalization (28), and hence (74).

**H5.** `rootedMap_zero` (merged in act 2) gives `rootedMap R 0 = 𝟙`, which transposes to `𝟙`.

**H6, and why it is *satisfied* rather than *incompatible*.** Our datum does not determine `p` —
Q8 established that, since our prior lives on the hidden carrier `H` and Source C's `p(·,0)` is a
distribution on `C`. But Source C eq (32), p. 10 makes `p(0)` freely adjustable subject only to
normalization, so **any** normalized declaration satisfies the hypothesis. Under the freeze's
repaired rule, a hypothesis satisfiable under a permitted declaration is **satisfied**, and the
undetermined datum is `MP2`'s business, not `MP3`'s.

**A separate observation about `p`, which matters for the candidate.** `p` enters the construction
only at the density matrix (84) and at the dilated standalone distribution (109). The
transition-bearing layer — the dictionary (81), the Kraus decomposition (90), the dilated dictionary
(103) and (105) — **does not consume `p` at all**. So `p` is undetermined on our side *and*
irrelevant to the candidate question. This extends act 1's Q8 observation, which was scoped to §5.1,
to the layer that would induce a candidate.

**No hypothesis is incompatible. `MP3` is not reached**, and not by non-verification: each
hypothesis above is positively satisfied against the source's own statement of it.

## M2a — determinacy: **determinate given named parameters**

Two findings, and the second is the one that decides the round.

### The construction produces nothing indexed from an intermediate time

Every object the construction builds is indexed `(t ← 0)`: the potential matrix `Θ(t ← 0)` (73), the
dictionary (81), the density matrix (83), the Kraus operators (87)–(91), the channel (92)–(93), the
dilated unitary `Ũ(t ← 0)` (96), the dilated dictionary (103), and the unistochastic relation (105).

The dilated process makes this explicit: its conditioning-time set is declared to be **the singleton
`{0}`** (§5.8, p. 27). So the construction's own output tuple contains **no** propagator from an
intermediate time, and therefore contains no visible intermediate candidate.

This is not a defect of the construction — it proves a theorem about representation, not about
division — but it is decisive for our question. The candidate act 3 is about is not among the
construction's outputs, and the only route to one from those outputs is the relative operator
`Θ(t ← 0) Θ(t′ ← 0)⁻¹`, or its dilated counterpart. **Source C does not take that step**, and this
round does not take it on the source's behalf.

### Along that route, the candidate depends on a choice `Γ` does not fix

`Θ` is non-unique, and the source says so in terms: eq (72), p. 20 writes
`Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²`, with the text stating that "this formula is an **identity**, not a
postulate. Any non-negative real number can be written **non-uniquely** as the modulus-square of a
complex number." Eq (73) calls `Θ(t ← 0)` a "**non-unique** 'potential matrix'". The matrix is
introduced per target time — "For each fixed target time `t`, the complex numbers `Θ_ij(t ← 0)`
collectively form their own `N × N` matrix" (§5.1, p. 20) — and nothing in (72), (74) or (75)
relates `Θ` at different times.

**That freedom is not inert at the candidate level**, and establishing this is what separates `MP1`
from `MP2` rather than leaving unitary non-uniqueness to stand in for candidate non-uniqueness.
Right-multiplying `Θ(t ← 0)` by any diagonal unitary `D_t` preserves every constraint the
construction imposes: `|Θ_ij d_{t,j}|² = |Θ_ij|²` leaves (72) and (74) untouched, and taking
`D_0 = 𝟙` leaves (75) untouched. So `Θ` and `Θ·D` are both admissible for the *same* `Γ`.

A two-configuration instance, computed on the source's own equations. Write `H` for the real
Hadamard matrix `(1/√2)[[1, 1], [1, −1]]`, and take `Θ(t′ ← 0) = Θ(t ← 0) = H`, which is admissible
since `|H_ij|² = 1/2` for every entry. The relative operator is then

- with `D_t = 𝟙`: `H H† = 𝟙`, whose modulus-squares are the **identity** matrix;
- with `D_t = diag(1, −1)`: `H D_t H† = [[0, 1], [1, 0]]`, whose modulus-squares are the **swap**.

Identity and swap are different visible propagators, from the same `Γ` and the same admissible
construction. The choice is therefore load-bearing for the candidate, not only for the operator.

**Evidence level.** This is a worked example on the source's stated equations — act 1's hierarchy
puts it at level 3, not level 2. It is not kernel-checked, and no Lean was written in this round.

### The named parameters

1. **The per-target-time phase freedom in `Θ`** — everything about `Θ(t ← 0)` beyond `|Θ_ij|²`,
   which is all that `Γ` fixes. Eq (72), (73), §5.1 p. 20.
2. **The Stinespring completion.** §5.7, p. 24 and footnote 13, p. 25: the partial isometry is
   extended to a unitary by adding columns that "**can always be chosen** so that they are mutually
   orthogonal with each other and with the previous `N²` columns", and the dilated dimension `Ñ` is
   only bounded, `N ≤ Ñ ≤ N³` (94), with `1 ≤ N′ ≤ N²` (99). Neither the completion nor the
   dimension is determined by `Γ`.

## M2b — containment: **no**

Our source-side datum determines `Γ`, and `Γ` determines `|Θ_ij(t ← 0)|²` and nothing more. Neither
named parameter is determined by the datum or by the permitted `T₀` and `p` declarations:

- the phase freedom is invisible to `Γ` by construction, since `Γ` is the modulus-square;
- the Stinespring completion is a choice made downstream of `Γ`, on the source's own account of it.

So a datum the construction consumes — in the sense of consuming a *choice* in order to yield a
determinate intermediate — is **not** determined by our side.

## M3 — not reached

M3 is conditional on M2 yielding a determinate candidate. It does not: the candidate is determinate
only relative to parameters our datum leaves open, which is `MP2`. **No candidate is identified in
our vocabulary**, and in particular nothing here says the induced candidate is `initWeight`'s,
`uniformWeight`'s, or a third.

Whether some admissible choice of the named parameters reproduces `initWeight`'s candidate, or
`uniformWeight`'s, is a well-posed question and is recorded as **open**. It is not asked here,
because asking it would mean selecting among the parameters, which is the candidate-selection
principle this round is forbidden to adopt.

## M4 — what act 3's `CU1a` retains, and what changes at programme level

**`CU1a` is preserved exactly and is not revised.** It states that the merged OI → `QfbData` bridge
does not select the candidate at this interface, and it is a theorem about **our** bridge. Nothing
in this round bears on it: act 4 audits an external construction and touches no this-side object.

**What changes is the programme-level reading**, and only this much. Before act 4 it was open
whether the missing selection was already supplied by the external correspondence. Against **Source
C's construction**, it is not: that construction does not produce an intermediate candidate at all,
and the route from its outputs to one turns on parameters `Γ` does not fix.

**What this does not license.** Not that the external framework requires an additional physical
principle — that claim is forbidden by act 3's frozen licence and this round does not earn it.
Not that the selection is unavailable: **Source A's earlier construction is out of scope by the
freeze** and forms relative operators in its own development, so it may yet supply what Source C's
does not. Not anything about the backward obligation, which was not attempted.

## Direction, stated per the freeze

Every claim above establishes the **forward** obligation only: our source-side datum → Source C's
construction → what that construction determines. **No claim here establishes the backward
obligation** — that the Hilbert space and unitary the construction produces coincide with the
`QfbData` our side already carries. That was not attempted and is not assumed.

## Prediction, and whether it held

The freeze recorded **no prediction** on `MP1` versus `MP2` versus `MP4`, having withdrawn an
earlier lean that rested on a footnote in the wrong paper. Nothing to score.

It recorded **`MP3` unlikely**, on Q8's ledger rather than on any reading of the construction. That
**held**: every hypothesis is satisfied, and the two Q8 identified as undetermined turned out to be
declarable exactly as Q8 suggested.

It recorded **`MP4` materially live**. That did **not** obtain: the construction's own text settles
both M2a and M2b without ambiguity, and the non-uniqueness is stated by the source rather than
inferred.

## What remains open

- **Source A's construction**, out of scope here. Whether it supplies a selection Source C's does
  not, and whether the two agree, is the natural next question on this route.
- Whether any admissible choice of the named parameters reproduces either named rule's candidate.
- The **backward obligation**, untouched.
- Whether a selection principle *should* be adopted on our side — deliberately not asked.

## Controls

Source C only; Source A not adjudicated. No Lean written. No this-side definition introduced. No
candidate-selection principle adopted or proposed. No backward identification assumed. Act 1's
`BD3`, `BR3` and Q8 cited, not extended; `RT1` and `CU1a` neither reopened nor revised. No
manuscript edit. No sourcing inference: determining what an external construction fixes says nothing
about OI physics. Equation and page numbers are Source C's throughout, never mixed with Source A's.

**This is an audit determination, not a theorem.** It sits at act 1's evidence levels 1 and 3, never
at level 2.
