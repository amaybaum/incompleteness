# Track B act 4 — the dilation mapping obligation: result

Frozen preregistration: commit `38bbf616314d1f689ac446b4081d407045fd707b`, blob
`3323fc6fc3bbe579dcf34452b147ca12c78e830d`, merged to `main` by PR #566.

Executed from `main` at `e3e36fe7388def725310475d012ad8e1da7d0bb6`, the merge of that freeze.

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source C is adjudicated**, per the freeze. Equation and page
numbers below are Source C's throughout.

## Outcome

**`MP4` — unresolved at the frozen interface.**

Every hypothesis of Source C's construction is satisfied by our source-side datum under the
permitted `T₀` and `p` declarations, so `MP3` is not reached. But M2a has no determinate answer:
**Source C's construction defines no map from its outputs to a visible intermediate candidate**, and
M2a asks what *the construction* fixes. With no such map in the construction, the question the freeze
poses has no answer at the interface the freeze fixed, and `MP4` is the label for that.

**Answering the question as posed, at the scope the evidence supports:** Source C's construction, as
stated, does **not** itself produce a visible intermediate candidate at all — so it does not select
one. Whether a candidate-extraction rule attached to its outputs would be canonical is **open**, and
this round does not attach one.

**Why not `MP2`.** `MP2` says the construction *maps* and consumes a datum our side does not
determine. That presupposes the construction yields a candidate, which it does not. Classifying this
as `MP2` would require importing a post-processing step the freeze does not authorize and then
attributing its behaviour to the construction — which is precisely what the freeze's own rule
against forming the relative operator on the source's behalf forbids.

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
repaired rule, a hypothesis satisfiable under a permitted declaration is **satisfied**, and an
undetermined datum is never `MP3`'s business.

**A separate observation about `p`, which matters for the candidate.** `p` enters the construction
only at the density matrix (84) and at the dilated standalone distribution (109). The
transition-bearing layer — the dictionary (81), the Kraus decomposition (90), the dilated dictionary
(103) and (105) — **does not consume `p` at all**. So `p` is undetermined on our side *and*
irrelevant to the candidate question. This extends act 1's Q8 observation, which was scoped to §5.1,
to the layer that would induce a candidate.

**No hypothesis is incompatible. `MP3` is not reached**, and not by non-verification: each
hypothesis above is positively satisfied against the source's own statement of it.

## M2a — determinacy: **unresolved**

Two findings. The first is determinate and is the round's main positive content; the second is a
countercontrol and is carefully **not** a determination about the construction.

### The construction produces nothing indexed from an intermediate time

Every object the construction builds is indexed `(t ← 0)`: the potential matrix `Θ(t ← 0)` (73), the
dictionary (81), the density matrix (83), the Kraus operators (87)–(91), the channel (92)–(93), the
dilated unitary `Ũ(t ← 0)` (96), the dilated dictionary (103), and the unistochastic relation (105).

The dilated process makes this explicit: its conditioning-time set is declared to be **the singleton
`{0}`** (§5.8, p. 27). So the construction's own output tuple contains **no** propagator from an
intermediate time, and therefore no visible intermediate candidate.

This is a determinate finding about Source C, and it is not a defect of the construction, which
proves a theorem about representation rather than about division. **But it is what makes M2a
unresolved**: the frozen M2a asks whether *the construction* fixes a candidate uniquely, or up to a
named parameter, and a construction that fixes no candidate at all answers neither. Nothing in the
freeze authorizes attaching an extraction rule and reading the answer off that instead.

### Countercontrol: one natural post-processing would remain choice-dependent

The only evident route from the construction's outputs to an intermediate is the relative operator
`Θ(t ← 0) Θ(t′ ← 0)⁻¹`, or its dilated counterpart. **Source C does not form it, and this round does
not adopt it.** What follows is therefore a countercontrol on *that candidate rule*, recorded so the
open question is not mistaken for an easy one — **not** a determination of what Source C selects.

`Θ` is non-unique, and the source says so in terms: eq (72), p. 20 writes
`Γ_ij(t ← 0) = |Θ_ij(t ← 0)|²`, with the text stating that "this formula is an **identity**, not a
postulate. Any non-negative real number can be written **non-uniquely** as the modulus-square of a
complex number." Eq (73) calls `Θ(t ← 0)` a "**non-unique** 'potential matrix'". It is introduced per
target time — "For each fixed target time `t`, the complex numbers `Θ_ij(t ← 0)` collectively form
their own `N × N` matrix" (§5.1, p. 20) — and nothing in (72), (74) or (75) relates `Θ` across times.

Right-multiplying `Θ(t ← 0)` by any diagonal unitary `D_t` preserves every constraint the
construction imposes: `|Θ_ij d_{t,j}|² = |Θ_ij|²` leaves (72) and (74) untouched, and taking
`D_0 = 𝟙` leaves (75) untouched. So `Θ` and `Θ·D` are both admissible for the *same* `Γ`.

A two-configuration instance. Write `H` for the real Hadamard matrix `(1/√2)[[1, 1], [1, −1]]`, and
take `Θ(t′ ← 0) = Θ(t ← 0) = H`, admissible since `|H_ij|² = 1/2` for every entry. The relative
operator is then

- with `D_t = 𝟙`: `H H† = 𝟙`, whose modulus-squares are the **identity** matrix;
- with `D_t = diag(1, −1)`: `H D_t H† = [[0, 1], [1, 0]]`, whose modulus-squares are the **swap**.

Identity and swap are different visible propagators, from the same `Γ` and the same admissible
construction data.

**Exactly what this shows, and what it does not.** It shows that *if* the relative-operator rule were
adopted as the candidate extraction, the resulting candidate would depend on a choice `Γ` does not
fix. It does **not** show what Source C's construction selects, because Source C selects nothing
here; and it does not by itself establish that every admissible extraction rule is choice-dependent.

**Evidence level.** A worked example on the source's stated equations — act 1's hierarchy puts it at
level 3, not level 2. Not kernel-checked, and no Lean was written in this round.

### The freedoms the construction leaves, and their status

- **The per-target-time phase freedom in `Θ`**, beyond `|Θ_ij|²`, which is all that `Γ` fixes —
  eq (72), (73), §5.1 p. 20. **Exhibited above as candidate-load-bearing for the relative-operator
  rule**, and for that rule only.
- **The Stinespring completion.** §5.7, p. 24 and footnote 13, p. 25: the partial isometry is
  extended to a unitary by adding columns that "**can always be chosen** so that they are mutually
  orthogonal with each other and with the previous `N²` columns", and the dilated dimension `Ñ` is
  only bounded, `N ≤ Ñ ≤ N³` (94), with `1 ≤ N′ ≤ N²` (99). This is **downstream representation
  non-uniqueness**, and this round does **not** exhibit two admissible completions changing any
  visible candidate. It is therefore recorded as representation freedom and is **not** named as a
  candidate-selection datum — the same distinction between representation freedom and candidate
  freedom that the phase example had to earn.

## M2b — containment: **not reached**

M2b is conditional on M2a's answer — the freeze asks whether every datum the construction consumes,
*including any parameter M2a names*, is determined by our datum. M2a is unresolved, so there is no
consumed-datum list to test and M2b is **not reached**.

Recorded separately, because it is true and will matter if an extraction rule is ever authorized:
`Γ` determines `|Θ_ij(t ← 0)|²` and nothing more, so the phase freedom is invisible to `Γ` by
construction and is not determined by our datum or by the permitted `T₀` and `p` declarations. That
is a fact about our side, not an answer to M2b.

## M3 — not reached

M3 is conditional on M2 yielding a determinate candidate. M2a is unresolved, so M3 is not reached,
and the two are consistent: there is no candidate to name because the construction fixes none.

**No candidate is identified in our vocabulary**, and in particular nothing here says the induced
candidate is `initWeight`'s, `uniformWeight`'s, or a third.

Whether, under some authorized extraction rule, an admissible choice reproduces either named rule's
candidate is a well-posed question and is recorded as **open**. It is not asked here, because asking
it would require both adopting an extraction rule the freeze does not authorize and then selecting
among its parameters — two things this round is forbidden to do.

## M4 — what act 3's `CU1a` retains, and what changes at programme level

**`CU1a` is preserved exactly and is not revised.** It states that the merged OI → `QfbData` bridge
does not select the candidate at this interface, and it is a theorem about **our** bridge. Nothing
in this round bears on it: act 4 audits an external construction and touches no this-side object.

**What changes is the programme-level reading**, and less than an `MP1` or `MP2` would have changed.
Before act 4 it was open whether the missing selection was supplied by the external correspondence.
What is now determinate is narrower: **Source C's construction, as stated, produces no intermediate
propagator**, so it does not supply a selection — not because it supplies an ambiguous one, but
because it produces no candidate at that layer at all.

**What this does not license.** Not that the external framework requires an additional physical
principle — forbidden by act 3's frozen licence, and not earned. Not that the selection is
unavailable: **Source A's earlier construction is out of scope by the freeze** and forms relative
operators in its own development, so it may yet supply what Source C's does not. Not that every
extraction rule attachable to Source C's outputs is choice-dependent — only the relative-operator
rule was examined, and only as a countercontrol. Not anything about the backward obligation, which
was not attempted.

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

It recorded **`MP4` materially live**. That **held**, and is the outcome. What made it live was not
an unclear source — Source C is entirely clear about what it builds — but the gap between what the
construction produces and what the frozen M2a asks about. The freeze was right to keep `MP4`
reachable.

## What remains open

- **Source A's construction**, out of scope here. It forms relative operators in its own
  development, so it is the natural next question on this route, and the sharpest one.
- **Whether any candidate-extraction rule attached to Source C's outputs is canonical.** Settling
  this needs an append-only frozen amendment that admits and defines the extraction, since reading
  an answer off an unauthorized post-processing is exactly what this round declined to do. The
  countercontrol above says only that the relative-operator rule would not be choice-free.
- Whether the Stinespring completion freedom is candidate-load-bearing. Not exhibited here, and
  recorded as representation freedom rather than as a selection datum.
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
