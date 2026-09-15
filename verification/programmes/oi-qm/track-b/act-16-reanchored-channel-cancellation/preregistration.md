# Track B act 16 — the cancellation question on the re-anchored-channel carrier: CONTROL PLANE

Owner-called. This file is the whole of act 16's control plane and is merged **alone**, before any
execution object exists. It takes up the question act 15's `PQ3-d⁺` leaves in front of `P0`'s
threading part: the pair question on act 14's fourth frozen carrier, the re-anchored-channel carrier
`𝒪₃`, which is the one frozen carrier on which nothing about the pair is settled.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–778**, quoted verbatim at this base —
the numbered item's opening sentence, ending part-way through line 778:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes ownership of
>    changing existing seal state — takes a pin commit `P`, and `P` is mandatory.**

This freeze **creates new seal state**. The execution writes a new Lean module with its own guard
clause in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-RNC`**, and that
clause carries the archive-mode constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_RNC_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_RNC_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_RNC_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_RNC_SEALED_HEAD` to `E` and `_RNC_MERGE` to `L`, moving the `R7-RNC` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_RNC_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

**What this round does NOT own, named exhaustively.** It alters **no existing seal constant**. In
particular `_TCF_BASE`, `_TCF_SEALED_HEAD` and `_TCF_MERGE` — act 15's seal — and `_PQT_BASE`,
`_PQT_SEALED_HEAD` and `_PQT_MERGE` — act 14's — and `_CTI_BASE`, `_CTI_SEALED_HEAD` and
`_CTI_MERGE` — act 13's — and `_A12P_*`, `_SGT_*`, `_TSG_BASE` and `_CLG_BASE` are **read and never
written**. An archive seal belongs to the round that set it: touching the guard file that carries
those constants does not make this round their owner, and the execution's diff against
`edge_rigidity_probe.py` **adds** the `R7-RNC` clause and changes nothing else in the file.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`b78eac870ba3ee9ef9e98659ac933bf97dc62226`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

### The obligation itself

`verification/ROADMAP.md`, **line 63**, the `P0` row's obligation cell and its status opening:

> | **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED: act 11's `GL2` proved the visible family does not fix the relative evolution;

and, from the same line, the clause act 15 added:

> act 15 took up act 14's one undecided target and answered it **`PQ3-d⁺`** — a cancelling triple is exhibited at evidence level 2, so relative to the relative-candidate carrier, under act 7's readback convention with `D4b` negative, the two parts **can** cancel and the pair can be redundancy relative to that carrier while neither part is, which refutes the proposition that no cancelling triple exists and with it the strictly stronger proposition that a redundant composite forces both halves to be redundant, while act 14's row is left exactly as act 14 wrote it; the answer is relative to `𝒪₂` and travels to no other carrier, act 14's `PQ3` (b) on the anchored-channel carrier being untouched, and no carrier is adopted as the physical one

### The interpretation boundary the whole of `P0` sits inside

`verification/ROADMAP.md`, **lines 52–57**:

> Accordingly, a failure of uniqueness at `P0` is not by itself a failure of quantum emergence. It
> determines the ontology of that emergence: either the residual lift freedom is physically redundant,
> additional structure selects one quantum history, or observational incompleteness determines only an
> equivalence class of quantum histories. Only an empirically distinguishable residual not removed by
> the physically appropriate equivalence relation would license a claim of physics beyond standard
> quantum mechanics.

### What act 11 left open about the shape, and what act 12 made two-part

`verification/ROADMAP.md`, **lines 164–169**, beginning part-way through line 164 — the paragraph
opens at line 162, and the span quoted here is the part that governs this round, the `ROADMAP`'s
statement that act 11 leaves the shape of the determining structure unconstrained:

> Act 11 does **not** constrain that structure's shape. `GI2` does not do it: its
> witness lies outside the weak class yet has *identical* relative objects, so it separates the lift
> space from the gauge class without separating the relative evolutions. **The shape question stays
> open**, and what would bear on it is a same-visible pair that is **both** outside the weak class
> **and** different in relative evolution. Act 11 supplies none and shows neither that one exists nor
> that one cannot.

`verification/ROADMAP.md`, **lines 229–235**:

> **What this changes about `P0`.** The quotient by the defined two-sided action is classified
> exactly, and `P0` remains **two-part**: what selects or constrains the Gram/orbit trajectory across
> time, and what determines the cross-time representative — the threading — within those selected
> orbits. **Act 11's `GL2` shows the second is not fixed even by the full Gram trajectory**: a
> time-dependent strong right gauge fixes every anchored column, hence every fibre-Gram matrix at
> every time, yet changes the relative evolution. No connection, gauge-fixing mechanism, or selection
> principle is asserted. Both parts are the next frontier, and neither is act 12's.

### The carrier discipline this round inherits

`verification/ROADMAP.md`, **lines 440–446**, ending part-way through line 446, the statement of what act 15 does not license:

> **What act 15 does NOT license.** No carrier is adopted as the physical one and none is asserted not
> to be; `P0` stays **OPEN** and two-part and neither part is closed; no selection principle is named,
> endorsed or excluded and no connection or gauge fixing is asserted or denied; nothing says OI and QM
> are inequivalent. **The answer is relative to `𝒪₂` and travels to no other carrier**: act 14's
> `PQ3` (b) settles the analogous question negatively on the anchored-channel carrier `𝒪₁`, the two do
> not conflict, and no implication between the carriers is proved in either direction.

`verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md`, **lines 127–134**:

> **None of the four is adopted as the physical one, and none is asserted not to be.** Each verdict is
> reported with its carrier and with that carrier's presupposition, and **no verdict travels**: a
> redundancy verdict on one carrier is never reported as evidence of redundancy on another, and a
> separation on one is never reported as a separation on another.
>
> **The four are not a ladder ordered by resolution.** Only two refinements are proved — `𝒪₀` is the
> diagonal action of `𝒪₁` and `𝒪₂` is the diagonal action of `𝒪₃` (`PQ0` a) — and **no implication
> between the one-time row and the re-anchored row is asserted in either direction.**

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 697–700**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md` | `6428e0acab070ccfd2a84d13c6f55616526206ba` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` | `fe8df06ffefac22ce87668ecf026f4c9ebc5c13f` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/preregistration.md` | `1b16008470bb1e2456c57aad58421a5941a55e0c` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md` | `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md` | `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| `verification/lean-mathlib/OIBridge/CancellationFork.lean` | `2cdfdf7742694391f16a73eebe37e1c0dcad6674` |
| `verification/lean-mathlib/OIBridge/ThreadingObservability.lean` | `91508205b33d9419fbffec5ad44035fad35de5f1` |
| `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` | `47eb21e22845f0319926227c80d0d7f2f033880b` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/lean-mathlib/OIBridge/AnchorRobustness.lean` | `b74202bc160918b32ca1b333da532a141ea8015d` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | **read** as the pinned statement of the `P0` row and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the `R7-RNC` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `0bff51eb9cc3c22859da2ac0efc622910e77d7b4` | one import line added after act 15's module |
| `verification/lean-manuscript-census.json` | `3e968e6c970301be5ba0b9631b234c957a6222d1` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/ReanchoredChannelScope.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one prose file this round both reads and writes, and it is listed
here rather than above for exactly that reason: the verbatim clause governs the read-only table
without qualification, and the `ROADMAP`'s treatment is stated in its own row. If its blob differs
at the base, the execution records the discrepancy and does not repair the freeze.

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**The `§A.37` justification, stated beneath it.** `AGENTS.md` lines 697–700, quoted above, fix the
execution's base as the merge commit of *this* control-plane pull request: the execution branches
from exactly that commit and from nothing else. So the base is fixed the moment this file merges,
and whatever sibling lanes have landed in `main` by then is a fact about the base's tree and not a
fact about this round's inputs. **Sibling results present at the base are not inputs.** The
start-state table above is the complete list of what this round consumes, and a file that is present
at the base and absent from that table is read by nothing in this round.

**Why this matters here, concretely.** Several sibling lanes are drafting and executing in parallel
with this freeze, and some will merge into `main` before this round's execution begins. This freeze
is written against `b78eac87` alone and consumes nothing from any of them.

## Source scoping, carried from acts 14 and 15

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and the scoping decision it takes rather than defers

Act 15 answered act 14's cancellation fork `PQ3` (d) positively, on the relative-candidate carrier
`𝒪₂` and on that carrier alone. The verdict is quoted above from the `ROADMAP` and again from act
15's own result note below. **This freeze takes the scoping decision that outcome leaves**, and takes
it here rather than deferring it to the execution.

### What the pair question's answer is, carrier by carrier, at this base

This table is a reading of the merged record, stated so that the gap this round takes up is visible
and so that no target of this round has to discover it. Each cell cites the merged label that fills
it; the empty cell is the round's subject.

| carrier | act 14's name | what the merged record says about **the pair** `(W, K)` | label |
| --- | --- | --- | --- |
| `𝒪₀` | the visible carrier | the pair is redundancy, universally | `PQ3` (a) |
| `𝒪₁` | the anchored-channel carrier | the pair's effect factors through the left part exactly, so the pair is redundancy for a given lift **iff** its left part is — there is no cancellation there | `PQ3` (b) |
| `𝒪₂` | the relative-candidate carrier | the pair is physical with both parts nontrivial (`PQ3` c), **and** a cancelling triple exists — `PQ3-d⁺` | `PQ3` (c), act 15's `CF5` |
| `𝒪₃` | the re-anchored-channel carrier | **nothing** | — |

**That empty cell is this round's subject, and naming it is this freeze's scoping decision.** The
round asks the cancellation question on `𝒪₃` and asks nothing else about any carrier's status.

### `𝒪₃`, quoted from act 14 with its coordinate

`verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md`, **lines 123–125**:

> **`𝒪₃`, the re-anchored-channel carrier.** `𝒪₃(U) = ((t,s) ↦ 𝔇_{a₀}(U_t U_sᴴ))`. *Presupposes:* both
> of the previous two. *Role:* the carrier on which "the pair is separated although neither part is"
> could in principle live, and where the cancellation fork is asked.

### The `𝒪₃` role seam, RECORDED AND NOT REPAIRED

**Act 14's own text says two things about where its fork is asked, and they are not the same
thing.** The passage just quoted names `𝒪₃` as the carrier "where the cancellation fork is asked".
Act 14's fork as stated, and as act 15 answered it, is asked on `𝒪₂`. From
`act-14-threading-observability/preregistration.md`, **lines 409–412**:

> **(d) Fork — can a nontrivial left part and a nontrivial strong-right part cancel on `𝒪₂`? NOT
> predicted.** The question: is there a coherent lift `U`, a constant `W ∈ 𝒢_L` and a strong family
> `K` such that `𝒪₂(W U_· K_·) = 𝒪₂(U)` while `𝒪₂(W U_·) ≠ 𝒪₂(U)` and `𝒪₂(U_· K_·) ≠ 𝒪₂(U)` — a
> pair separated by neither composite half yet identified as a whole.

**This is recorded as a seam in the merged record and is not repaired, not corrected, not
reinterpreted and not normalized.** Act 14's merged text stands exactly as act 14 wrote it, and act
15's `PQ3-d⁺` answers the fork as `PQ3` (d) literally states it — on `𝒪₂`. Nothing in this round
edits either. **What this round does instead** is ask the question of `𝒪₃` explicitly, under its own
labels, so that the `𝒪₃` question is settled or recorded undecided under a name of this round's own
rather than under act 14's label. **No target of this round is carried by this seam, no prediction
changes sign or strength because of it, and this round asserts nothing about what act 14 "meant".**
The execution records the seam in its result note's discrepancies section and does nothing else with
it.

### What act 15 established, and what it did not

**Established, and consumed here at its own strength.** `CF0` (the record's silence on the universal
ingredient, a statement about the record at act 15's base and not a truth value); `CF1` the normal
form; `CF2` time-dependence necessary; `CF3` (a) and (b) the cardinality scopings; `CF4` (a) and (b)
the non-triviality conjuncts; and `CF5` at line 1 — `PQ3-d⁺`, an exhibited cancelling triple. From
`act-15-pq3d-cancellation-fork/result.md`, **lines 76–78**:

> **The answer is relative to `𝒪₂`, under act 7's readback convention with `D4b` negative, and it
> travels to no other carrier.** No carrier is adopted as the physical one, `P0` stays **OPEN** and
> two-part, and nothing here names, endorses or excludes a selection principle.

**Not established, and open at this base.** Whether the pair can cancel on `𝒪₃`; whether act 15's
own exhibited triple cancels on `𝒪₃`; and what relation, if any, holds between `𝒪₂`-redundancy and
`𝒪₃`-redundancy for the pair. The first two are `RN3`. The third is `RN1` in the one direction this
round claims it, and is refused in the other.

## The carrier rule, FROZEN — no verdict travels, and no target generalizes

**Every verdict in this round names its carrier, and no verdict is reported on a carrier other than
the one its proof is about.** This is act 14's status rules 3, 4 and 5 binding this round, and act
15's "travels to no other carrier" binding it too. The rule has four consequences this freeze states
in advance so that the execution cannot discover them after an outcome:

1. **`PQ3-d⁺` is about `𝒪₂`.** It is **not** evidence that a cancelling triple relative to `𝒪₃`
   exists, **not** evidence that none does, and **not** evidence about `𝒪₀` or `𝒪₁`. No target of
   this round may cite it as bearing on `𝒪₃`'s fork beyond what `RN2` proves — which is two of the
   three conjuncts and not the third.
2. **`PQ3` (b) is about `𝒪₁`.** It settles the composite-versus-left question on the
   anchored-channel carrier, and it is **not** evidence about `𝒪₃`, in either direction, even though
   `𝒪₁` and `𝒪₃` share the anchored channel `𝔇_{a₀}` as their value map. **A shared construction is
   not a shared verdict**: `𝒪₁` applies `𝔇_{a₀}` to `U_t`, `𝒪₃` applies it to `U_t U_sᴴ`, and act 14
   records that no implication between the one-time row and the re-anchored row is proved in either
   direction.
3. **The one refinement this round does claim is stated within the re-anchored row and nowhere
   else.** `RN1` proves `𝒪₃`-equality implies `𝒪₂`-equality. It says nothing about `𝒪₀` and `𝒪₁`,
   and its converse is refused.
4. **No carrier is adopted as the physical one, and none is asserted not to be.** `𝒪₂` and `𝒪₃`
   verdicts carry act 7's boundary — `D4b` negative, the readback the repository's own — at every
   use rather than once in a footnote.

## The act 13 `CT3` (d) anti-conflation clause, FROZEN VERBATIM

Act 13's fork `CT3` (d) is structurally similar to the question this round asks and must not be
conflated with it in either direction. The clause below is **THE CLAUSE**, and it is carried as a
block quote **at every prose mention of `CT3` (d)** in this file and in every artifact of this round.

**How each carriage is written, and why.** Each carriage opens with one line naming where it is
being carried, and then states the clause word for word. The naming line is there so that the
carriages read as distinguishable copies of one clause rather than as one paragraph pasted
repeatedly — which is a defect the repository's duplicate check exists to catch — and it changes
nothing about the clause it introduces. Act 15's freeze established this pattern and this round
follows it.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed propagation
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name `CT3` (d) among the labels this round does not touch.

**THE CLAUSE:**

> `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
> separates **every** strong-right threading — a question about one datum's separating power. This
> round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
> cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that carrier
> while neither part is — a question about cancellation between two parts of one relation, on one
> named carrier. **Neither instantiates, constrains, nor supplies evidence for the other, and no
> implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this round
> returns, and no outcome of this round moves it in either direction.

Act 13's `CT3` (d) therefore appears in **analysis only**. **No target of this round is carried by
`CT3` (d)**, no target cites it as evidence, and no determination changes sign or strength because
of it. Writing an outcome of this round as if it bore on `CT3` (d), or an ingredient of `CT3` (d) as
if it bore on this round's question, is a **defect of this round** and is checked for in the final
report.

For the reader's convenience, `CT3` (d)'s own recorded route to a label, quoted verbatim from
`act-13-cross-time-invariants/result.md`, lines 212–218 — and governed by the clause above:

> **(d) The fork — does level 3 separate every `GL2`-type pair? UNDECIDED.** Neither `CT3-d⁺` nor
> `CT3-d⁻` was reached, and neither is claimed. The route to the label: by `CT2` (a) a
> strong-right-related pair with equal `Ξ` at every `t, s` is constant-left related, `U' = C U` with
> `U_tᴴ C U_t` strong for every `t`; `CT3-d⁺` would need a universal theorem that every such `C`
> conjugates every relative object without moving its anchored readback, and `CT3-d⁻` would need an
> exhibited pair satisfying the strong-right and `Ξ`-equality conjuncts with distinct candidates.

> **THE CLAUSE, carried at this mention — the quotation of `CT3` (d)'s own route to a label.**
> `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
> separates **every** strong-right threading — a question about one datum's separating power. This
> round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
> cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that carrier
> while neither part is — a question about cancellation between two parts of one relation, on one
> named carrier. **Neither instantiates, constrains, nor supplies evidence for the other, and no
> implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this round
> returns, and no outcome of this round moves it in either direction.

**One resemblance is recorded here so that it is not mistaken for a bridge, in this round's own
terms.** `CT3` (d)'s `CT3-d⁺` branch and this round's `RN3` (b) lines 2 and 3 each want a universal
theorem about a conjugation that does not move an anchored datum — and this round's anchored datum is
the anchored **channel** rather than the anchored readback, which puts the two statements further
apart rather than closer. The two theorems quantify over different
things — `CT3` (d)'s over constant-left elements `C` forced by `Ξ`-equality on strong-right-related
pairs, this round's over triples `(U, W, K)` with `W ∈ 𝒢_L` and `K` a strong family — and **neither
would establish the other**. Recording the resemblance is not transferring it, and no target of this
round is stated over `CT3` (d)'s objects.

## The `PQ4` (c) reading, RECORDED AND FROZEN APART

Act 14's `PQ4` (c) describes what a selector would have to select. From
`act-14-threading-observability/result.md`, **lines 362–369**:

> **(c) What a selector would have to select, and on what data. Stated conditionally, as a description
> of a shape, and never as a proposal.** If the physical carrier — whichever it turns out to be —
> separates the residual freedom, then an additional selector would have to select, together:
>
> - **one constant element of `𝒢_L` modulo the uniform relabellings** — equivalently one cross-fibre
>   frame; and
> - **one strong-right family `K_·` modulo a constant** — equivalently one threading of the off-anchor
>   columns across time.

**Two readings of "together" are available, and they are not equivalent.** On the **conjunctive**
reading, a selector must supply both choices — which says nothing about whether the two may be made
independently. On the **factoring** reading, a selector's job decomposes into two separate choices,
one per part, so that fixing each part's class fixes the composite's. **`PQ3-d⁺` bears on the second
reading and on `𝒪₂` only**, and `RN4` states exactly what it bears on and nothing further.

**This section repairs nothing.** Act 14's merged text stands exactly as act 14 wrote it; nothing
here edits it, reinterprets it or normalizes it, and no sentence of this round says what act 14
"meant". `PQ4` (c)'s word is "together", which is the conjunctive reading, and **the conjunctive
reading is untouched by anything in this round**. What `RN4` refutes is the factoring reading, on
`𝒪₂`, and it says so in those words. The execution records the two readings in its discrepancies
section and nowhere else.

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13, 14 and 15

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `U : ℕ → U(V × A)` a lift, and the
following are consumed **unmodified**, at their own strengths: `readback`,
`AdmissibleDilationAt`, `admissible_mul_of_fixes_anchor`, `readback_isColStochastic`,
`readback_relabel` (`R-3`), `readback_permMatrix_apply`, `one_admissible_at_every_anchor`,
`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `strong_mem_weak`,
`strong_eq_one_of_ancilla_subsingleton`, `gl2_strong_gauge_moves_relative_candidate` (`GL2`),
`gl3_constant_gauge_preserves_relative` (`GL3`),
`visible_marginal_eq_one_of_visible_subsingleton`, `LeftFibreGroup`, `FibreGram`,
`left_preserves_admissible`, `fibreGram_left_mul`, `sum_fibreGram`, `CrossGram`, `FibreCrossGram`,
`ct2a_relative_conj`, `ct3g_fibreCrossGram_strong_right` (`CT3` (G)),
`ct4_constant_left_obstruction` (`CT4`), `cl1_constant_left_moves_relative_candidate` (`CL1`),
`AnchoredChannel`, `anchoredChannel_apply`, `anchoredChannel_block`, `anchoredChannel_eq_trace`,
`anchoredChannel_unit`, `CrossFibreGram`, `crossFibreGram_diag`, `ThreadingRelated` (`≈_T`),
`UniformLeft`, act 14's `PQ0` (a)–(d) — in particular `pq0a_readback_is_diagonal_action` —
`PQ1` (a)–(d), `PQ2` (a)–(c), `PQ3` (a)–(c) and `PQ4` statements, and act 15's `RelativeCandidate`,
`relativeCandidate_apply`, `relativeCandidate_congr`, `cf1_composite_normal_form`,
`cf2_constant_strong_family_redundant`, `cf3_cardinality_scoping`, `cf4_nontriviality_conjuncts`,
`relativeCandidate_of_permMatrix`, `cf5_cancelling_triple_exists` and
`cf5_not_no_cancelling_on_relativeCandidate`.

**The four carriers are act 14's**, frozen there with their presuppositions, and **none is adopted
as the physical one and none is asserted not to be**. This round asks its question on `𝒪₃` because
that is the one frozen carrier on which the merged record says nothing about the pair.

**The relative object** is `U_t U_sᴴ`, exactly as acts 7, 11, 13, 14 and 15 write it. **`𝒪₂`'s value
at one time pair** is act 15's `RelativeCandidate a₀ U t s`. **`𝒪₃`'s value at one time pair** is
`AnchoredChannel a₀ (U_t U_sᴴ)`, act 14's channel applied to the relative object.

**The triple.** A **triple** is a datum `(U, W, K)` with `U` a coherent lift, `W` a constant matrix
with `LeftFibreGroup W`, and `K : ℕ → U(V × A)` a family with `StrongAnchorStabilizer a₀ (K t)` for
every `t`. Its **composite** is `U'_t := W · U_t · K_t`, which is `≈_T`-related to `U` by act 13's
`CT2` (b) as act 14 names that relation.

**The six per-triple predicates, FROZEN.** For a triple `(U, W, K)` with composite `U'`:

```
C₂(U, W, K)  :  𝒪₂(U')      = 𝒪₂(U)      — the composite is redundant relative to 𝒪₂ on this triple
L₂(U, W, K)  :  𝒪₂(W U_·)   = 𝒪₂(U)      — the left part alone is redundant relative to 𝒪₂ on it
R₂(U, W, K)  :  𝒪₂(U_· K_·) = 𝒪₂(U)      — the strong-right part alone is redundant relative to 𝒪₂ on it
C₃(U, W, K)  :  𝒪₃(U')      = 𝒪₃(U)      — the composite is redundant relative to 𝒪₃ on this triple
L₃(U, W, K)  :  𝒪₃(W U_·)   = 𝒪₃(U)      — the left part alone is redundant relative to 𝒪₃ on it
R₃(U, W, K)  :  𝒪₃(U_· K_·) = 𝒪₃(U)      — the strong-right part alone is redundant relative to 𝒪₃ on it
```

Each is an equality of the whole two-time family, at every time pair, and each is carrier-indexed,
with act 7's boundary carried. A triple is **`𝒪₂`-cancelling** iff `C₂ ∧ ¬L₂ ∧ ¬R₂` — which is act
14's fork, and act 15's `PQ3-d⁺` exhibits one. A triple is **`𝒪₃`-cancelling** iff
`C₃ ∧ ¬L₃ ∧ ¬R₃` — which is this round's `RN3`.

**The two universal propositions on `𝒪₃`, FROZEN SEPARATELY**, in the shape act 15's freeze fixed for
`𝒪₂` and for the same reason:

> **`N₃` — no `𝒪₃`-cancelling triple exists.** For every triple, `C₃ → (L₃ ∨ R₃)`. **`N₃` is the
> exact negation of the existence of an `𝒪₃`-cancelling triple.**

> **`S₃` — the composite is `𝒪₃`-redundant only when both halves are.** For every triple,
> `C₃ → (L₃ ∧ R₃)`.

**`S₃` implies `N₃`, by propositional logic alone; `N₃` does not imply `S₃`.** As schemas,
`C₃ → (L₃ ∨ R₃)` does not entail `C₃ → (L₃ ∧ R₃)`: a triple with `C₃ ∧ L₃ ∧ ¬R₃`, or one with
`C₃ ∧ ¬L₃ ∧ R₃`, satisfies `N₃` and refutes `S₃`. **So `S₃` is strictly the stronger**, and a proof
of `N₃` is not a proof of `S₃`. The two are kept apart at every use in this round, and `RN3`'s
hierarchy has a line for each.

**Act 7's boundary is carried at every use of `𝒪₂` and `𝒪₃`**, exactly as acts 14 and 15 carry it:
act 7's `D4b` came back **negative** — Source A supplies no general map carrying the relative
candidate on the dilated carrier back to `V` — and the readback is the repository's own, frozen by
act 7's readback amendment. Every `𝒪₂` and `𝒪₃` statement in this round is a statement under that
convention, said at each use rather than once in a footnote.

## The evidence rule, FROZEN

`RN0` is settled by **locating and quoting**, not by proving a theorem. Its evidence rule is frozen
here and binds the execution:

1. Evidence is a **verbatim quotation** from a pinned blob, with its file path and line coordinate;
   or
2. a **verbatim quotation** from a merged result note or preregistration, with its coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist** on the record
   searched, with the search **named and bounded** — the file set enumerated, the search terms
   listed, and the result recorded for each term.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the record must
contain X, because otherwise Y would not have been written" may appear only in a clearly labelled
analysis paragraph that states it is not evidence and that no target rests on it. **Where the record
is silent, the finding is that it is silent** — not that the thing sought is false, and not that it
is true. **Silence is a finding.**

**The bounded search for `RN0` is fixed now**, so that its boundary cannot be chosen after its
result is known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/` and under
  `verification/lean/`; every `preregistration.md` and `result.md` under
  `verification/programmes/oi-qm/`; and `verification/ROADMAP.md`. The set is taken from
  `git ls-tree -r --name-only B`, so untracked package trees are outside it by construction.
- **The search terms**: `AnchoredChannel`, `ReanchoredChannel`, `CrossFibreGram`, `ThreadingRelated`,
  `LeftFibreGroup`, `StrongAnchorStabilizer`, `cancel`, `redundan`, and the merged label names
  `PQ0`, `PQ2`, `PQ3`, `PQ4`, `CF1`, `CF5`, `CT2`, `CT3`.
- **The question asked of each hit**: does this declaration decide, for some triple or for every
  triple `(U, W, K)`, any one of `C₃`, `L₃` or `R₃` — that is, does it state a conclusion about
  `AnchoredChannel a₀` applied to a **relative object** `U_t U_sᴴ` or to its composite counterpart,
  at every time pair — or a statement from which such a conclusion follows by consuming merged
  results alone, with the consumption exhibited?
- **The recorded answer per hit** is one of: *supplies it* (quoted, with coordinate); *does not
  supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

The execution records the search in the result note in full. **A search that finds a decision is a
finding, and a search that does not is equally a finding** — the second being that the record is
silent on the point, which is what `RN0` asks.

## The targets, FROZEN

Five targets, `RN0` through `RN4`. Each names what settles it and what evidence counts.

### `RN0` — does the merged record decide the pair question on `𝒪₃`, in either direction?

**The question.** At this freeze's base, does the merged record contain any statement — universal or
existential — deciding `C₃`, `L₃` or `R₃` for any triple or for all triples?

**What settles it.** The bounded search frozen above, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule if a decision is found — a verbatim
quotation with a coordinate, plus a statement of exactly which of `C₃`, `L₃` and `R₃` it decides and
for which triples. Rule 3 if none is found — the recorded statement that the passage sought does not
exist on the named and bounded search, with the per-term record.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `RN0`**, and no outcome of `RN0` is a theorem
of this round.

**What `RN0` is not.** It is not a claim that any statement it fails to find is false, not a claim
that one is unprovable, and not a claim about what a later round could prove. It is a statement about
the merged record at this freeze's base. **Nor is it a licence to treat `RN1`'s or `RN2`'s
conclusions as retro-evidence about it**: what `RN1` and `RN2` prove is this round's own, and what
`RN0` records is what was in the record before this round wrote anything.

### `RN1` — the refinement, stated within the re-anchored row and in one direction only

**The statement.** For every anchor `a₀`, every pair of lifts `U`, `U'` over the same finite carrier,
and all times `t, s`: if `AnchoredChannel a₀ (U'_t U'_sᴴ) = AnchoredChannel a₀ (U_t U_sᴴ)` then
`RelativeCandidate a₀ U' t s = RelativeCandidate a₀ U t s`. Hence `𝒪₃(U') = 𝒪₃(U)` implies
`𝒪₂(U') = 𝒪₂(U)`.

**What settles it.** A Lean theorem at evidence level 2, universally quantified, consuming act 14's
merged `pq0a_readback_is_diagonal_action` at `M = U_t U_sᴴ` and the injectivity of the real-to-complex
coercion, and nothing else.

**Bounded reading, frozen.** This is a refinement **within the re-anchored row**.

- **It says nothing about `𝒪₀` and `𝒪₁`**, and asserts **no** implication between the one-time row
  and the re-anchored row, in either direction. Act 14's record that no such implication is proved
  stands untouched, and this round does not add one.
- **The converse is refused.** `𝒪₂`-equality does not give `𝒪₃`-equality, nothing here says it does,
  and no later target of this round uses a converse.
- **It is not a statement that either carrier is observable**, and it adopts neither. Each carrier's
  observational status remains its own recorded presupposition.
- **It is not a statement that `𝒪₃` is "finer" in any sense beyond the implication written.** No
  strictness is claimed: this round does not prove that the implication fails to reverse, and does
  not assert that it does.

### `RN2` — the two non-triviality conjuncts on `𝒪₃`, by contraposition

Three parts, predicted separately and reported separately.

**(a)** For every triple, `¬L₂ → ¬L₃`: if the left part alone moves `𝒪₂`, it moves `𝒪₃`.

**(b)** For every triple, `¬R₂ → ¬R₃`: if the strong-right part alone moves `𝒪₂`, it moves `𝒪₃`.

**(c)** Instantiated at act 15's exhibited triple: that triple satisfies `¬L₃ ∧ ¬R₃`.

**What settles each.** (a) and (b) are Lean theorems at evidence level 2, each the contrapositive of
`RN1` applied to the pair `(U, W U_·)` and to the pair `(U, U_· K_·)` respectively, stated as
conjuncts of one theorem. (c) is a Lean theorem at evidence level 2, consuming act 15's merged
`cf5_cancelling_triple_exists` at its own **existential** strength — its statement carries
`¬ ∀ t s, RelativeCandidate a₀ (fun t => W * U t) t s = RelativeCandidate a₀ U t s` and the
corresponding strong-right conjunct explicitly — and applying (a) and (b) to it.

**Bounded reading, frozen.** `RN2` supplies **two** of the three conjuncts of the `𝒪₃` fork and
**not** the third.

- **It is not evidence that `C₃` holds on act 15's triple, or on any triple.** Whether `C₃` holds is
  `RN3` and is settled there or recorded undecided there.
- **It is not evidence that an `𝒪₃`-cancelling triple exists.** A triple satisfying two of three
  conjuncts is not a witness.
- **It does not carry `PQ3-d⁺` from `𝒪₂` to `𝒪₃`.** Act 15's result is consumed at its own
  existential strength and is not enlarged; what travels is exactly the two contrapositives `RN1`
  licenses, and nothing else.
- **`GL2`, `CT4` and `CL1` are not enlarged** from existential to universal by anything here.

### `RN3` — THE FORK ON `𝒪₃`

Two parts. **(a)** is a decision about act 15's exhibited triple. **(b)** is the fork over all
triples, under a strict four-outcome hierarchy.

#### `RN3` (a) — does act 15's exhibited triple cancel on `𝒪₃`?

**The question.** For act 15's triple — `V = Fin 2`, `A = Fin 3`, `a₀ = 0`, the `W`, `U` and `K`
that `cf5_cancelling_triple_exists` exhibits — does `C₃` hold: is
`AnchoredChannel a₀ (W U_t K_t K_sᴴ U_sᴴ Wᴴ) = AnchoredChannel a₀ (U_t U_sᴴ)` at **every** time pair?

**The three outcomes, exhaustive:**

| label | statement | earned only by |
| --- | --- | --- |
| **`RN3-a⁺`** | that triple satisfies `C₃`, hence with `RN2` (c) it is `𝒪₃`-cancelling | a kernel proof of `∀ t s` equality at evidence level 2, the objects pinned by equations in the statement |
| **`RN3-a⁻`** | that triple does not satisfy `C₃` | a kernel proof at evidence level 2 of an inequality at a **named** time pair and a **named** entry, with both entry values proved |
| **UNDECIDED** | neither was reached | the recorded statement that neither was reached, with the obstruction named |

**What `RN3-a⁻` does NOT establish.** It settles **one triple**. It is **not** `N₃`, **not** evidence
for `N₃`, **not** evidence that no `𝒪₃`-cancelling triple exists, and **not** a bound on what a later
round could exhibit. Reporting it as anything more is the specific defect this sub-target's status
rule exists to prevent.

**What `RN3-a⁻` would additionally record, and at what strength.** It would record that `𝒪₃`
separates a pair which `𝒪₂` identifies — an existential separation statement about that one triple,
on `𝒪₃`, carrying act 7's boundary. That is a statement about `𝒪₃` and travels to no other carrier;
in particular it is not a statement that `𝒪₃` is strictly finer than `𝒪₂` in general, which this
round does not claim.

#### `RN3` (b) — the fork over all triples

**The question.** Is there an `𝒪₃`-cancelling triple — a triple with `C₃ ∧ ¬L₃ ∧ ¬R₃`? And if not,
which of `N₃` and `S₃` is proved?

**`RN3` (b) is attempted in this round.** The owner's scope decision is recorded here: the round
attempts the fork on `𝒪₃` rather than stopping at `RN0`–`RN2`, and UNDECIDED below is priced
accordingly rather than standing in for the attempt.

**The hierarchy is strict and exhaustive, and the outcome reached is the highest line the kernel
actually carries** — never a higher one:

| # | outcome | statement | earned only by |
| --- | --- | --- | --- |
| 1 | **`RN3⁺`** | an `𝒪₃`-cancelling triple exists — relative to `𝒪₃` the pair can be redundancy while neither part is | an exhibited triple with **all three** conjuncts proved in the kernel, at evidence level 2, with the lift's coherence discharged from merged results and the two inequalities certified at named time pairs and named entries. `RN3-a⁺` together with `RN2` (c) earns this line and no other |
| 2 | **`RN3-S`** | **`S₃`** — for every triple, `C₃ → (L₃ ∧ R₃)` | a **universal** proof of `S₃` at evidence level 2, quantified over every lift, every `W ∈ 𝒢_L` and every strong family. `N₃` follows from it by the implication frozen above and is reported as following, not as separately proved |
| 3 | **`RN3-N`** | **`N₃` and not `S₃`** — for every triple, `C₃ → (L₃ ∨ R₃)`, with `S₃` not proved | a **universal** proof of `N₃` at evidence level 2, under the same quantification, **without** a proof of `S₃`. The outcome's frozen sentence says in terms that the literal cancellation question on `𝒪₃` is answered negatively and that the stronger reading is **NOT** claimed |
| 4 | **UNDECIDED** | none of the above was reached | the recorded statement that none was reached, with the obstruction named and with `RN0`'s finding and `RN3` (a)'s outcome recorded alongside it |

**Line 3 exists because `S₃` is strictly stronger than `N₃`**, for the reason frozen in the objects
section: `S₃ → N₃` by propositional logic, and `N₃ → S₃` fails as a schema and is not settled over
the actual triples by anything in the merged record. **Line 3 is what prevents spending a hard
universal proof and then reporting something strictly stronger than what was proved.**

**UNDECIDED is a preregistered outcome of this round, not a fallback.** The freeze rates it the most
likely outcome of `RN3` (b) and says so in the prediction table, with its reason. Its post-round
sentence is written out in full in the status rule below, before the round runs.

**What `RN3` (b) may not do.**

- It may not report an outcome at a strength the kernel does not carry.
- It may not report line 2 on the strength of a proof of `N₃`. **A proof of `N₃` is line 3**, and the
  gap between them is the difference between `L₃ ∨ R₃` and `L₃ ∧ R₃`.
- It may not report line 2 or line 3 on the strength of `RN3-a⁻`, which settles one triple.
- It may not report line 2 or line 3 on the strength of act 14's `PQ3` (b), which is about `𝒪₁`.
- It may not report line 1 on the strength of an unexhibited construction, or on the strength of
  act 15's `PQ3-d⁺`, which is about `𝒪₂`.
- **Reporting a settling outcome because a witness was sought and not found is the specific error
  this target's status rule exists to prevent.**

### `RN4` — what `PQ3-d⁺` does to the factoring reading of `PQ4` (c), on `𝒪₂` and on nothing else

**The statement.** There is a triple `(U, W, K)` with `C₂ ∧ ¬L₂ ∧ ¬R₂`. Hence, relative to `𝒪₂`, the
redundancy subrelation of `≈_T` is **not** the product of the two parts' redundancy subrelations:
knowing each part's `𝒪₂`-redundancy class does not determine the composite's, because both parts are
`𝒪₂`-separating while the composite is `𝒪₂`-redundant.

**What settles it.** A Lean theorem at evidence level 2, consuming act 15's merged
`cf5_cancelling_triple_exists` at its own existential strength and restating the non-factorization
consequence over this round's frozen predicates `C₂`, `L₂`, `R₂`. No new witness is constructed.

**Bounded reading, frozen.**

- **This is a statement about `𝒪₂` and travels to no other carrier.** It says nothing about `𝒪₀`,
  `𝒪₁` or `𝒪₃`, and it is **not** evidence about `RN3`.
- **It does not say a selector is required.** It names, endorses and excludes no selection principle,
  no connection and no gauge fixing, in either direction.
- **It does not correct act 14's `PQ4` (c).** `PQ4` (c)'s word is "together", which is the
  conjunctive reading, and the conjunctive reading is untouched. What is refuted is the factoring
  reading, on `𝒪₂`, and the two readings are recorded apart in the section above and in the
  execution's discrepancies section.
- **It is not a claim about which choices a physical selector would face**, because no carrier is
  adopted as the physical one.
- **It adds nothing to act 15.** The existential content is act 15's; `RN4` states the consequence
  act 15's exhibition carries for `PQ4` (c)'s factoring reading and nothing further.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `RN0` | **negative** — the record is silent; no statement decides `C₃`, `L₃` or `R₃` for any triple | **high** | A pre-freeze survey of the file set named in the evidence rule found every merged statement about the pair to be indexed to `𝒪₀` (`PQ3` a), `𝒪₁` (`PQ3` b) or `𝒪₂` (`PQ3` c, act 15's `CF1`–`CF5`); act 14's `pq2b_anchored_column_identity` is about the per-time lift's anchored columns and the relative object is not of the form `M K`; `PQ0` (a) and (d) mention `𝒪₃` but decide nothing about the pair on it. The survey is the freeze's **reason**, not a finding: `RN0`'s finding is whatever the execution's own bounded search records. |
| `RN1` | positive | **high** | Act 14's merged `pq0a_readback_is_diagonal_action` states `((readback a₀ (|M|²) i j : ℝ) : ℂ) = AnchoredChannel a₀ M E_{jj} i i` for every matrix `M`; at `M = U_t U_sᴴ` it makes `𝒪₂`'s value a function of `𝒪₃`'s, and equal functions have equal images. The one step beyond rewriting is injectivity of the real-to-complex coercion. |
| `RN2` (a) | positive | **high** | The contrapositive of `RN1` applied to the pair `(U, W U_·)`. |
| `RN2` (b) | positive | **high** | The contrapositive of `RN1` applied to the pair `(U, U_· K_·)`. |
| `RN2` (c) | positive | **medium** | Act 15's `cf5_cancelling_triple_exists` states the two `𝒪₂` inequalities as explicit conjuncts of one existential, so (c) is an `obtain` followed by two applications of (a) and (b); the medium rating is for the bookkeeping of carrying an eleven-conjunct existential through, not for any doubt about the route. **Reporting `RN2` (c) UNDECIDED with the obstruction named is an allowed outcome**, and it does not move (a) or (b). |
| `RN3` (a) — that it resolves at all | **resolves** | **high** | It is a decision about named permutation matrices over `Fin 2 × Fin 3` with two effective times, in the shape acts 11–15 used throughout: the anchored columns of each relative object reduce to a single permutation and the channel's entries are read off act 14's merged `anchoredChannel_unit` and `crossFibreGram_diag`. Decidability over finite index types is kernel-checked with `decide`. |
| `RN3` (a) — its sign | **negative** (`RN3-a⁻`) | **low** | Act 15 built its triple to cancel on `𝒪₂` and nothing in that construction constrained it on `𝒪₃`. `𝒪₃` reads the anchored channel of the relative object, which act 14's `PQ0` records as a function of that object's cross-fibre Gram, while `𝒪₂` reads the diagonal entries of that Gram's diagonal blocks — act 14's `PQ0` (a) with `crossFibreGram_diag`. A datum tuned to the second is not expected to satisfy the first by accident. **The rating is low and not lower**, because on two visible outcomes what `𝒪₃` adds beyond `𝒪₂` is thin, and the freeze names no computation and does not rate either sign better than low. **This paragraph is the prediction's recorded reason and is not a finding**; whatever the kernel returns is `RN3` (a)'s outcome. |
| `RN3` (b) | **UNDECIDED** | **medium** | Conditional on `RN3` (a) coming back negative, which the freeze rates at low; if (a) is positive, line 1 follows at once through `RN2` (c) and this row is falsified. Absent that route, lines 2 and 3 each need a universal theorem about how a `𝒢_L` conjugation acts on the anchored **channel** of a general relative object, which `RN0` predicts is absent from the record and which this round's definition budget does not fund building. |
| `RN3` (b) → line 1, `RN3⁺` | not predicted | **low** | Its whole predicted route is through `RN3` (a), which the freeze rates negative at low. The freeze names no second candidate triple and does not rate a search for one better than low. |
| `RN3` (b) → line 2, `RN3-S` (`S₃`) | not predicted | **low** | `S₃` is strictly the stronger of the two universals and is stronger in a direction nothing in the merged record reaches: it constrains triples in which one half is `𝒪₃`-redundant on its own, which no merged statement touches. Rated at or below line 3's strength for that reason, and never above it. |
| `RN3` (b) → line 3, `RN3-N` (`N₃` and not `S₃`) | not predicted | **low** | Rated low for the reason `RN0` records, and **rated at or above line 2**, because `S₃` implies `N₃` and so any route to line 2 is also a route to line 3, while the converse fails; a freeze that rated the stronger proposition higher than the weaker one would be incoherent. |
| `RN4` | positive | **high** | The existential content is act 15's merged `cf5_cancelling_triple_exists`, whose conjuncts are exactly `C₂`, `¬L₂` and `¬R₂` for one exhibited triple; non-factorization is the existential read off it, and the proof is an `obtain` and a repackaging. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named.

**The four `RN3` rows rating lines 1, 2 and 3 at low, and `RN3` (a)'s sign at low, are the freeze's
whole position on the fork's resolution.** No sentence of this file predicts the `𝒪₃` fork's
resolution at medium or high on any of the three settling lines.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
The wording is fixed before the round runs so that no outcome can choose its own wording. **UNDECIDED
is a live preregistered outcome for every target and is not a failure**; where it is reached the
frozen sentence below is the report, with the obstruction named.

### The outcomes of `RN0`

- **Outcome `RN0`-silent** — the bounded search records that the passage sought does not exist:
  > On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
  > `verification/lean/`, every `preregistration.md` and `result.md` under
  > `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
  > the merged record decides none of `C₃`, `L₃` and `R₃`, for any triple or for all triples: it
  > contains no statement about the anchored channel of a relative object under a constant in-fibre
  > left move together with a time-dependent strong right gauge. **The finding is that the record is
  > silent on the point.** It is not a finding that any such statement is false, not a finding that
  > one is unprovable, and not a bound on what a later round could prove.
- **Outcome `RN0`-found** — the search locates a deciding statement:
  > The merged record decides at least one of `C₃`, `L₃` and `R₃`, quoted verbatim above with its
  > coordinate, and the record says exactly which predicate it decides and for which triples.
  > Whether that statement settles the `𝒪₃` fork is `RN3`'s question and is not settled by locating
  > it. No merged artifact is edited, and no earlier round's recording is enlarged or corrected.

### The outcomes of `RN1`

- **Outcome `RN1`-positive:**
  > `𝒪₃`-equality implies `𝒪₂`-equality, universally, at evidence level 2, through act 14's merged
  > `PQ0` (a) consumed. **This is a refinement within the re-anchored row and nothing more**: it
  > asserts no implication between the one-time row and the re-anchored row in either direction, its
  > converse is refused and not claimed, it asserts no strictness, and it says nothing about which
  > carrier is observable. **No carrier is adopted as the physical one.**
- **Outcome `RN1`-UNDECIDED:**
  > The refinement was not reached in the kernel, with the obstruction named, and every later target
  > stated over it — `RN2` and hence `RN3` (a)'s route through `RN2` (c) — is reported UNDECIDED with
  > this recorded as the obstruction. Act 14's `PQ0` (a) stands as act 14 states it and nothing is
  > claimed from it here.

### The outcomes of `RN2`

- **Outcome `RN2`-all-three:**
  > For every triple, a left part that moves `𝒪₂` moves `𝒪₃`, and a strong-right part that moves
  > `𝒪₂` moves `𝒪₃`; and act 15's exhibited triple therefore satisfies `¬L₃` and `¬R₃`. All three at
  > evidence level 2. **These supply two of the three conjuncts of the `𝒪₃` fork and not the third.**
  > Nothing here is evidence that `C₃` holds on that triple or on any triple, nothing here is
  > evidence that an `𝒪₃`-cancelling triple exists, and **act 15's `PQ3-d⁺` is consumed at its own
  > existential strength and is not carried from `𝒪₂` to `𝒪₃`.**
- **Outcome `RN2`-(a)-and-(b)-only:**
  > The two universal contrapositives hold at evidence level 2. Whether act 15's exhibited triple
  > satisfies `¬L₃` and `¬R₃` is undecided in this round, with the obstruction named, and (a) and (b)
  > do not cover it.
- **Outcome `RN2`-UNDECIDED:**
  > Neither contrapositive was reached, with the obstruction named.

### The outcomes of `RN3` (a)

- **Outcome `RN3-a⁺`:**
  > Act 15's exhibited triple satisfies `C₃` at every time pair, at evidence level 2. With `RN2` (c)
  > it is therefore `𝒪₃`-cancelling, and `RN3` (b) reaches line 1 through it and through no other
  > route. **This is a statement about `𝒪₃` and travels to no other carrier**, and it carries act 7's
  > boundary — `D4b` negative, the readback the repository's own.
- **Outcome `RN3-a⁻`:**
  > Act 15's exhibited triple does not satisfy `C₃`: the two sides differ at a named time pair and a
  > named entry, both entry values proved, at evidence level 2. So relative to `𝒪₃` that triple's
  > composite is separated, and `𝒪₃` separates a pair which `𝒪₂` identifies. **This settles one
  > triple and nothing more.** It is **not** `N₃`, **not** evidence for `N₃`, **not** a statement
  > that no `𝒪₃`-cancelling triple exists, and **not** a bound on what a later round could exhibit.
  > It is **not** a statement that `𝒪₃` is strictly finer than `𝒪₂` in general, which this round
  > does not claim. **This is a statement about `𝒪₃` and travels to no other carrier**, and it
  > carries act 7's boundary. **Act 15's `PQ3-d⁺` on `𝒪₂` stands exactly as act 15 states it and is
  > not weakened, qualified or revised by this**: the two are verdicts on different carriers and
  > neither is evidence about the other.
- **Outcome `RN3` (a)-UNDECIDED:**
  > Whether act 15's exhibited triple satisfies `C₃` is undecided in this round, with the obstruction
  > named. Neither `RN3-a⁺` nor `RN3-a⁻` is claimed, and no sentence of this round treats the
  > absence of a decision as a decision.

### The outcomes of `RN3` (b) — four outcomes, each with its sentence frozen in full

- **Outcome line 1, `RN3⁺`:**
  > An `𝒪₃`-cancelling triple is exhibited: relative to the re-anchored-channel carrier, and under
  > act 7's readback convention with `D4b` negative, the pair of a constant in-fibre left move and a
  > time-dependent strong right gauge can be redundancy while neither part is. The triple's three
  > conjuncts are proved in the kernel at evidence level 2, with the lift's coherence discharged from
  > merged results and the two inequalities certified at named time pairs and named entries. **This
  > is a statement about `𝒪₃` and travels to no other carrier**; act 14's `PQ3` (b) settles the
  > analogous question negatively on `𝒪₁` and the two do not conflict, `𝒪₁` and `𝒪₃` being computed
  > from different operations on the lift with no implication proved between them in either
  > direction, and act 15's `PQ3-d⁺` on `𝒪₂` is a separate verdict on a separate carrier. **No
  > carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and nothing here names,
  > endorses or excludes a selection principle.
- **Outcome line 2, `RN3-S` — `S₃` proved:**
  > Relative to the re-anchored-channel carrier, and under act 7's readback convention with `D4b`
  > negative, **`S₃` holds: for every triple, if the composite is redundant relative to `𝒪₃` then
  > both halves are redundant relative to `𝒪₃` individually.** The statement is universal over the
  > threading equivalence at evidence level 2, with the universal ingredient supplied by this round
  > and recorded as this round's own result. **`N₃` follows from `S₃` by propositional logic and is
  > reported as following, not as separately proved**, so no `𝒪₃`-cancelling triple exists either.
  > **This is a statement about `𝒪₃` and travels to no other carrier**, and in particular it is not
  > a statement about `𝒪₂`, where act 15's `PQ3-d⁺` stands exactly as act 15 states it and is not
  > weakened, qualified or revised. **No carrier is adopted as the physical one**, `P0` stays OPEN
  > and two-part, and nothing here names, endorses or excludes a selection principle.
- **Outcome line 3, `RN3-N` — `N₃` proved, `S₃` NOT claimed:**
  > Relative to the re-anchored-channel carrier, and under act 7's readback convention with `D4b`
  > negative, **`N₃` holds: no `𝒪₃`-cancelling triple exists — for every triple, if the composite is
  > redundant relative to `𝒪₃` then at least one of its two halves is redundant relative to `𝒪₃`
  > individually.** The statement is universal over the threading equivalence at evidence level 2.
  > **The literal cancellation question on `𝒪₃` is thereby answered negatively: on that carrier the
  > two parts cannot cancel.** **The stronger reading — that relative to `𝒪₃` the pair is redundancy
  > only when both parts are, the proposition this round calls `S₃` — is NOT claimed, is not proved,
  > and does not follow from what is proved here.** `S₃` implies `N₃` and `N₃` does not imply `S₃`;
  > what this round establishes is the weaker of the two, and whether `S₃` also holds is **UNDECIDED**
  > and is recorded as such, with the separating shape — a triple satisfying `C₃ ∧ L₃ ∧ ¬R₃`, or one
  > satisfying `C₃ ∧ ¬L₃ ∧ R₃` — named and neither exhibited nor excluded. **This is a statement
  > about `𝒪₃` and travels to no other carrier**, and in particular it is not a statement about
  > `𝒪₂`, where act 15's `PQ3-d⁺` stands exactly as act 15 states it and is not weakened, qualified
  > or revised. **No carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and
  > nothing here names, endorses or excludes a selection principle.
- **Outcome line 4, `RN3` (b)-UNDECIDED — its post-round sentence frozen in full:**
  > **The cancellation question on the re-anchored-channel carrier is recorded UNDECIDED.** None of
  > the three settling outcomes was reached in this round, and **none is claimed**: no
  > `𝒪₃`-cancelling triple is exhibited, `N₃` is not proved, and `S₃` is not proved. Line 1 would
  > need an exhibited triple with all three conjuncts proved; `N₃` and `S₃` would each need a
  > universal theorem over the threading equivalence about how a constant `𝒢_L` conjugation acts on
  > the anchored channel of a general relative object, and on the named and bounded search this round
  > records, the record is silent on that ingredient. **What this round adds on this carrier is two
  > of the three conjuncts and a refinement, and not a resolution**: `𝒪₃`-equality implies
  > `𝒪₂`-equality, so a part that moves `𝒪₂` moves `𝒪₃`, and act 15's exhibited triple therefore
  > satisfies the two non-triviality conjuncts on `𝒪₃`; whether its composite is `𝒪₃`-redundant is
  > reported at `RN3` (a) and is the whole of what separates this round from line 1. **An UNDECIDED
  > is a statement about this round and about the record, and not about the question.** It is **not**
  > a finding that the question is unresolvable, **not** a finding that it is hard, **not** a bound on
  > what a later round can do, and **not** a finding against any settled result of act 14 or act 15:
  > `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(c), `PQ4` and act 15's `PQ3-d⁺` stand exactly as those rounds
  > state them. Act 13's `CT3` (d) stays UNDECIDED and is untouched. **No carrier is adopted as the
  > physical one**, `P0` stays OPEN and two-part, and nothing here names, endorses or excludes a
  > selection principle.

### The outcomes of `RN4`

- **Outcome `RN4`-positive:**
  > Relative to the relative-candidate carrier, the redundancy subrelation of the threading
  > equivalence does not factor as the product of the two parts' redundancy subrelations: there is a
  > triple whose composite is redundant relative to `𝒪₂` while neither half is, at evidence level 2,
  > consuming act 15's exhibition at its own existential strength. **This is a statement about `𝒪₂`
  > and travels to no other carrier**, and it carries act 7's boundary. It does **not** say a
  > selector is required, and it names, endorses and excludes no selection principle, connection or
  > gauge fixing. **Act 14's `PQ4` (c) is not corrected**: its word is "together", the conjunctive
  > reading, which is untouched; what is refuted is the factoring reading, and the two readings are
  > recorded apart in the discrepancies section and nowhere else.
- **Outcome `RN4`-UNDECIDED:**
  > The non-factorization consequence was not reached in the kernel, with the obstruction named; act
  > 15's `PQ3-d⁺` stands as act 15 states it and nothing is claimed from it here.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The sentence the execution
appends to it is fixed here.

**Case A — `RN0` silent, `RN1` and `RN2` land, `RN3` (a) reaches `RN3-a⁻`, `RN3` (b) is UNDECIDED,
and `RN4` lands.** This is the case the freeze predicts.

> `P0` remains open and two-part, and acts 14's and 15's answers relative to each frozen carrier of
> observables stand exactly as those rounds state them. The cancellation question is now asked of the
> one frozen carrier on which the merged record said nothing about the pair — the re-anchored-channel
> carrier — and on that carrier it is recorded UNDECIDED: no cancelling triple relative to it is
> exhibited, and neither the proposition that none exists nor the strictly stronger proposition that
> a redundant composite forces both halves to be redundant is claimed. What this round adds on that
> carrier is a refinement and two of the three conjuncts, and not a resolution: equality of the
> re-anchored channel at every time pair implies equality of the relative candidate at every time
> pair, so a part that moves the relative candidate moves the re-anchored channel, and act 15's
> exhibited triple therefore satisfies both non-triviality conjuncts on the re-anchored-channel
> carrier while its composite is separated there at a named time pair and a named entry — which
> settles that one triple and is not a statement that no cancelling triple relative to that carrier
> exists. On the named and bounded search this round records, the merged record decides none of the
> three conditions on that carrier for any triple. Relative to the relative-candidate carrier, act
> 15's `PQ3-d⁺` further gives that the redundancy subrelation of the threading equivalence does not
> factor as the product of the two parts' redundancy subrelations; act 14's `PQ4` (c) is not edited,
> its conjunctive wording being untouched. Act 13's `CT3` (d) stays UNDECIDED and is untouched;
> neither question answers the other. **No carrier is adopted as the physical one**, `P0`'s other
> part — what selects or constrains the Gram/orbit trajectory across time — is untouched, and nothing
> here names, endorses or excludes a selection principle.

**Three clauses of Case A vary with the outcome, and they vary independently.** Naming them here,
and fixing each clause's substitutions against the target that governs it, is what lets the execution
compose the sentence it actually earned rather than carry a clause that reads against its own
outcome.

- **The fork clause**, governed by `RN3` (b), is Case A's
  > "and on that carrier it is recorded UNDECIDED: no cancelling triple relative to it is exhibited,
  > and neither the proposition that none exists nor the strictly stronger proposition that a
  > redundant composite forces both halves to be redundant is claimed"
- **The resolution phrase**, governed by `RN3` (b), is the words "and not a resolution" inside the
  sentence beginning "What this round adds on that carrier".
- **The transfer clause**, governed by `RN3` (a), is that sentence's final sub-clause, Case A's
  > "while its composite is separated there at a named time pair and a named entry — which settles
  > that one triple and is not a statement that no cancelling triple relative to that carrier exists"

**The fork clause and the resolution phrase, per `RN3` (b) outcome.**

| `RN3` (b) | fork clause | resolution phrase |
| --- | --- | --- |
| UNDECIDED (**Case A**) | as written above | as written above |
| line 1, `RN3⁺` (**Case B**) | "and on that carrier it is answered positively: relative to the re-anchored-channel carrier, under act 7's readback convention with `D4b` negative, the two parts can cancel, so the pair can be redundancy relative to that carrier while neither part is" | "together with the resolution" |
| line 2, `RN3-S` (**Case C**) | "and on that carrier it is answered in the stronger of its two readings: relative to the re-anchored-channel carrier, under act 7's readback convention with `D4b` negative, a redundant composite forces both halves to be redundant individually, so in particular the two parts cannot cancel there" | "together with the resolution" |
| line 3, `RN3-N` (**Case D**) | "and on that carrier it is answered negatively in its literal form: relative to the re-anchored-channel carrier, under act 7's readback convention with `D4b` negative, no cancelling triple relative to that carrier exists, so the two parts cannot cancel there — while the strictly stronger reading, that a redundant composite forces both halves to be redundant individually, is **not** claimed and remains undecided" | "together with the resolution" |

**The transfer clause, per `RN3` (a) outcome.**

| `RN3` (a) | transfer clause |
| --- | --- |
| `RN3-a⁻` (**Case A**) | as written above |
| `RN3-a⁺` | "while its composite is redundant there at every time pair" |
| UNDECIDED | "while whether its composite is redundant there is undecided in this round, with the obstruction named" |

**Case E — `RN2` (c) UNDECIDED:** the transfer clause and the clause before it, both of which are
stated about act 15's exhibited triple, are omitted together; the fork clause and the resolution
phrase stand at whatever `RN3` (b) reaches; every other clause stands.

**Case F — `RN1` UNDECIDED:** every clause of Case A's "What this round adds" sentence that is stated
over the refinement is omitted, the targets that land are reported at their own strengths, and `RN2`
and `RN3` are UNDECIDED, with the fork clause as in Case A.

**Case G — `RN4` UNDECIDED:** Case A's sentence beginning "Relative to the relative-candidate
carrier" is omitted; every other clause stands at whatever the other targets reach.

**The execution composes the sentence from these substitutions and reports no other wording.** **No
composition closes `P0`**, and none reports either of its two parts closed.

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The question on `𝒪₃` is unresolvable."** An UNDECIDED here is **not** a finding that the
   question is unresolvable, not a finding that it is undecidable, and not a finding that it is hard.
   It is the recorded fact that none of the three settling outcomes was reached in this round.
2. **Any transfer of a verdict between carriers, in any direction.** The cases that matter here are
   named: act 14's `PQ3` (b) is about `𝒪₁` and is not evidence about `𝒪₃`, although both use the
   anchored channel; act 15's `PQ3-d⁺` is about `𝒪₂` and is not evidence about `𝒪₃`, although `RN1`
   relates the two carriers' equalities in one direction; and no outcome of this round on `𝒪₃` is
   evidence about `𝒪₀`, `𝒪₁` or `𝒪₂`. **A shared construction is not a shared verdict.**
3. **"Act 15 was wrong", or any sentence that treats `RN3-a⁻` as evidence against act 15.** Act 15's
   `PQ3-d⁺` is a verdict on `𝒪₂`; a separation of the same triple on `𝒪₃` is a verdict on `𝒪₃`. The
   two are consistent by construction — `RN1` runs from `𝒪₃`-equality to `𝒪₂`-equality and not back —
   and neither weakens, qualifies or revises the other.
4. **"`𝒪₃` is strictly finer than `𝒪₂`."** `RN1` proves one implication. This round proves no
   strictness and asserts none, and `RN3-a⁻`, if reached, is an existential separation on one triple
   and not a general strictness theorem.
5. **"No cancelling triple relative to `𝒪₃` exists", asserted on the strength of `RN3-a⁻`.** That
   settles one triple. One triple is not a universal non-existence theorem.
6. **"A witness was sought and not found, so there is none."** Absence of a witness in this round is
   not a negative result, and no search is presented as exhaustive over triples.
7. **ANY SENTENCE OF `S₃`'s FORM, ON THE STRENGTH OF LINE 3.** Line 3 licenses no sentence of `S₃`'s
   form, in any paraphrase. The forbidden sentences include, and are not limited to: "relative to
   `𝒪₃` the pair is redundancy only when both parts are"; "a redundant composite forces both halves
   to be redundant"; "if the composite is `𝒪₃`-redundant then the left part is"; "if the composite is
   `𝒪₃`-redundant then the strong-right part is". What line 3 proves is `C₃ → (L₃ ∨ R₃)`; `S₃` is
   `C₃ → (L₃ ∧ R₃)`; **the disjunction is not the conjunction**.
8. **"The record's silence shows the statement sought is false."** `RN0`'s finding, if silent, is
   that the record is silent. **Silence is a finding, and it is not a truth value.**
9. **Any sentence that carries an outcome of this round to act 13's `CT3` (d), or an ingredient of
   `CT3` (d) to this round.** The anti-conflation clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
   > separates **every** strong-right threading — a question about one datum's separating power. This
   > round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
   > cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that
   > carrier while neither part is — a question about cancellation between two parts of one relation,
   > on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.
10. **"The threading freedom is gauge" or "the threading freedom is physical."** Act 14's status rule
    3 binds this round too: there is no carrier-free verdict, and every verdict names its carrier.
11. **"Carrier `𝒪ₓ` is the physical one", or "carrier `𝒪ₓ` is not the physical one."** No carrier is
    adopted and none is asserted not to be.
12. **"`P0` is closed", or "`P0`'s threading part is closed."** The row stays OPEN and two-part in
    every case, and `P0`'s other part — what selects or constrains the Gram/orbit trajectory across
    time — is untouched by this round.
13. **"The selection principle is …", "the connection is …", "the gauge fixing is …"** — no sentence
    of this round may begin that way, and none may assert or deny that a connection or gauge fixing
    exists or suffices, in either direction. **`RN4` in particular does not say a selector is
    required**, on any carrier.
14. **"Act 14's `PQ4` (c) is corrected", or any sentence that repairs, reinterprets, normalizes or
    supersedes it.** Its two readings are **recorded** and act 14's merged text stands as written.
15. **"Act 14 asked its fork on `𝒪₃`", or any sentence that settles act 14's role-description seam by
    choosing a reading.** The seam is **recorded** and act 14's merged text stands as written; act
    15 answered act 14's fork as `PQ3` (d) literally states it, on `𝒪₂`, and this round asks its own
    question on `𝒪₃` under its own labels.
16. **"OI and QM are inequivalent."** Two lifts differing is not two theories differing, and the
    established finite observable-law correspondence is untouched. Every `𝒪₂` and `𝒪₃` statement is
    further a statement under act 7's own readback convention, with `D4b` negative.
17. **Any sentence about Track I**, or about Source B or Source C, on any axis.
18. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **Letting a target generalize across carriers.** **This is the strongest hazard in the round**,
   because the round's whole subject is a second carrier and because `𝒪₁` and `𝒪₃` share the
   anchored channel while `𝒪₂` and `𝒪₃` share the relative object. The specific failures guarded
   against are three, each named: reporting act 15's `PQ3-d⁺` as bearing on `𝒪₃` beyond the two
   contrapositives `RN2` proves; reporting act 14's `PQ3` (b) — the `𝒪₁` non-cancellation — as
   bearing on `𝒪₃` because both carriers are built from `𝔇_{a₀}`; and reporting an `𝒪₃` outcome as
   bearing on `𝒪₂`, in either direction. **Every verdict names its carrier**, and the carrier rule
   above is checked clause by clause in the final report.
2. **Conflating this round's question with act 13's `CT3` (d).** The two are structurally similar —
   both turn on a constant left element interacting with a strong right family, and each has a
   branch whose ingredient is a universal theorem about a conjugation that does not move an anchored
   datum. The specific failure guarded against is an artifact of this round reporting an outcome as
   bearing on `CT3` (d), or citing `CT3` (d)'s ingredients as evidence here. The anti-conflation
   clause is carried verbatim at every mention:
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > `CT3` (d) is act 13's fork and it belongs to act 13. It asks whether the full column cross-Gram
   > separates **every** strong-right threading — a question about one datum's separating power. This
   > round asks whether a constant in-fibre left move and a time-dependent strong right gauge can
   > cancel on the re-anchored-channel carrier, so that the pair is redundancy relative to that
   > carrier while neither part is — a question about cancellation between two parts of one relation,
   > on one named carrier. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.
3. **Reading `RN1` as an equivalence.** `RN1` runs from `𝒪₃`-equality to `𝒪₂`-equality. The specific
   failure guarded against is using the converse anywhere — for instance concluding `C₃` from `C₂`,
   which would make act 15's triple `𝒪₃`-cancelling by fiat and would be exactly the error `RN3` (a)
   exists to decide.
4. **Reading `RN1` as an implication between the one-time row and the re-anchored row.** Act 14
   records that no such implication is proved. The specific failure guarded against is a sentence of
   the form "so the carriers form a ladder", or a statement relating `𝒪₁` to `𝒪₂` or `𝒪₃` on the
   strength of `RN1`.
5. **Treating `RN2` as two thirds of a witness.** `RN2` supplies `¬L₃` and `¬R₃` for act 15's triple.
   The specific failure guarded against is "so only `C₃` remains, and it plainly holds" — which is
   exactly the reconstructive inference the evidence rule forbids as a finding.
6. **Reporting `RN3-a⁻` as `N₃`.** One triple is not a universal theorem. The specific failure
   guarded against is a result note that decides one triple negatively and then writes "so the two
   parts cannot cancel on `𝒪₃`".
7. **Reporting `RN3-a⁻` as evidence against act 15.** The specific failure guarded against is a
   sentence weakening, qualifying or revising `PQ3-d⁺` because the same triple is separated on a
   different carrier. `PQ3-d⁺` is a verdict on `𝒪₂` and stands exactly as act 15 states it.
8. **Reporting line 2 on the strength of a proof of `N₃`.** The gap is `L₃ ∨ R₃` against
   `L₃ ∧ R₃`. Line 3 and its frozen sentence exist to make the weaker report the natural one.
9. **Reporting a settling outcome because a witness was sought and not found.** Absence of a witness
   is neither `N₃` nor `S₃`.
10. **A reader supplying the missing universal theorem from background knowledge the record does not
    contain.** The specific failure guarded against is a step of the form "of course a unitary
    conjugation does not change a partial trace" — plausible-sounding, absent from the record, and
    licensed by nothing in it. The anchored channel is a partial trace of `C(M) ρ C(M)ᴴ` over the
    ancilla index at the **anchored input column**, and a general `𝒢_L` conjugation of the relative
    object does not act on `C(M)` by a similarity. Every step of every proof in this round is
    discharged from a merged result cited by name or from an argument written out in the kernel.
11. **The conjugation trap.** Under act 7's convention `P(g) P(h) = P(h·g)` and
    `(P(σ) M)_{pq} = M_{σ p, q}`. Anchored columns, conjugates, channel entries and separating
    entries are computed in the kernel, never read off a constructor. The specific failure guarded
    against is an inverted permutation making a hoped-for cancellation, or a hoped-for separation,
    look real.
12. **Forgetting the anchor.** `AnchoredChannel a₀`, `readback a₀` and the strong class all carry
    `a₀`; the relative object `U_t U_sᴴ` does not. The specific failure guarded against is a
    statement that silently changes which configuration is anchored — which act 7's `R-3` explicitly
    does **not** license, being a statement about names and not about which configuration is
    anchored.
13. **Treating `𝒪₂` or `𝒪₃` as an established observable.** Act 7's `D4b` is negative and the
    readback is the repository's own convention. Every `𝒪₂` and `𝒪₃` statement in this round is a
    statement under that convention and is reported with it at each use.
14. **Adopting a carrier.** The specific failure guarded against is a sentence of the form "since the
    physical carrier is `𝒪₃`". No carrier is adopted and none is asserted not to be.
15. **Reading `RN4` as a claim that a selector is required.** `RN4` says the `𝒪₂` redundancy
    subrelation does not factor. The specific failure guarded against is "so an additional selector
    must select the two jointly", which names a requirement this round does not establish and which
    turns on a carrier decision this round does not take.
16. **Repairing act 14's `PQ4` (c) or its `𝒪₃` role description.** Both are **recorded** as readings
    and neither is repaired. The specific failure guarded against is a sentence saying what act 14
    "meant", or an artifact of this round editing act 14.
17. **Enlarging `PQ3-d⁺`, `GL2`, `CT4` or `CL1` from existential to universal.** Each is an
    existential statement about one exhibited lift or triple. The specific failure guarded against is
    citing one of them as though it quantified over lifts or over triples.
18. **Touching `P0`'s other part.** What selects or constrains the Gram/orbit trajectory across time
    is not this round's subject. The specific failure guarded against is a sentence of this round
    bearing on it in either direction.
19. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs; the specific failure guarded against is an execution that
    reads a lane that merged between this freeze and its base.
20. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier in a different programme. Nothing is consumed or compared, and a shared word is not a
    bridge.
21. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_RNC_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
22. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
23. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: adopt a carrier as the physical one; name, endorse or exclude a selection
principle; assert or deny that a connection or gauge fixing exists or suffices; propose a datum
sufficient for the relative candidate; introduce a measurement model, regularity, homogeneity,
generated evolution or source-level coherence condition; change `CoherentLift`'s `ℕ`-indexing;
introduce a further carrier or revise any of act 14's four; revise `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`,
`LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3`
(a)–(d), `PQ4`, `CF0`, `CF1`, `CF2`, `CF3`, `CF4`, `CF5` or any merged label; answer act 13's fork
`CT3` (d) or move it in either direction; **repair, correct, reinterpret, normalize or supersede act
14's `PQ4` (c) or act 14's description of `𝒪₃`'s role, both of which are recorded as carrying
readings and are left exactly as act 14 wrote them**; weaken, qualify or revise act 15's `PQ3-d⁺`;
report a proof of `N₃` in `S₃`'s words, or `S₃` on the strength of `N₃`; touch `P0`'s other part —
what selects or constrains the Gram/orbit trajectory across time; change `D3`, `D4b`, `D5`, the
direct-branch statement or the readback convention; alter any existing archive seal constant; consume
or compare anything from the substratum Lemma 24.1 rounds; compare Source A with B or C; edit any
manuscript; close `P0` or either of its parts; or say anything about Track I.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most two** top-level Lean definitions, and these are the two:

1. **`ReanchoredChannel`** — `ReanchoredChannel a₀ U t s := AnchoredChannel a₀ (U t * (U s)ᴴ)`, the
   `𝒪₃` value at one time pair. Act 14 defines `AnchoredChannel` and applies it to the per-time lift;
   this round needs the value at a time **pair**, because every target states an equality or an
   inequality of `𝒪₃` values over **all** time pairs, which act 14 never had to write. *Needed.*
2. **An `𝒪₃`-cancelling-triple predicate** — the three conjuncts `C₃ ∧ ¬L₃ ∧ ¬R₃` as one `Prop` over
   `(U, W, K)` — *if* `RN2` and `RN3` cannot be stated readably with the conjuncts written inline;
   unused otherwise. *Conditional.*

**A third definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. **No lift, gauge element, witness, matrix, triple, entry value or pair is a
top-level definition** — each is a bound variable pinned by an equation in the statement that needs
it, as acts 10, 11, 12, 13, 14 and 15 did. Acts 7's, 10's, 11's, 12's, 13's, 14's and 15's
definitions are **reused, not redefined**; in particular `AnchoredChannel` and `RelativeCandidate`
are consumed and neither is restated.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `RN1`, `RN2`, `RN4`, `RN3` (a) whichever label it
reaches, and, if any of lines 1, 2 or 3 of its hierarchy is reached, `RN3` (b). `decide` over finite
index types is kernel-checked and permitted; `native_decide` is not, and neither is `sorry`.

**`RN0` is type P and carries no evidence level.** It is settled by the frozen evidence rule —
verbatim quotation with a coordinate, or the recorded statement that the passage sought does not
exist on the named and bounded search — and by nothing else. **Reconstructive inference is forbidden
as a finding**, and where the record is silent the finding is that it is silent.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-RNC`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_RNC_SEALED_HEAD`** and **`_RNC_MERGE`**, with
the base held in **`_RNC_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 16 object
   enters the repository tree** — any Lean definition or proof about the re-anchored channel of a
   relative object, about `𝒪₃`-cancelling triples or about the refinement; any search artifact; any
   probe clause; any result artifact. **The single permitted exception is the analysis recorded
   inside this control-plane blob itself**, merged *as* the freeze, including the frozen evidence
   rule, the carrier table of what is settled where, and the pre-freeze survey recorded as the reason
   for `RN0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_RNC_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content at this exact path, and the
   execution ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _RNC_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of
   `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_RNC_SEALED_HEAD` and `_RNC_MERGE` are present and **unset** at execution.
   After `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the
   same strong check against the sealed object: the pinned merge's second parent must equal the
   sealed head; the sealed head must pass clause 5 against `B` exactly as in its own run; and both
   must be reachable from the current target — the real `pull_request.head.sha` in pull-request
   continuous integration, `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change
   recording the two SHAs and nothing else.
8. **Existing seal constants are read with mutation controls and never written.** The guard clause
   checks `_TCF_SEALED_HEAD`, `_TCF_MERGE`, `_PQT_SEALED_HEAD`, `_PQT_MERGE`, `_CTI_SEALED_HEAD` and
   `_CTI_MERGE` equal to the values acts 15, 14 and 13 set, because an archive seal belongs to the
   round that set it.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/preregistration.md \| git hash-object --stdin` equals the blob the `R7-RNC` clause pins |
| 2 | Act 15's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, both non-`None` |
| 3 | Act 15's module and result are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/CancellationFork.lean` and `git cat-file -e B:verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` both succeed |
| 4 | Act 14's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` |
| 5 | Act 13's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` |
| 6 | No act 16 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/ReanchoredChannelScope.lean` |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are **not** inputs: the anti-contamination invariant governs, and the
round consumes only what this freeze's start-state table names.

**The claim is scoped to the repository record.**

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative**, and the path this file sits at is pinned with it, so the directory and filename do
  not move after this merges.
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This pull request carries this file alone.**
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  Lean module, the result note, the `R7-RNC` guard clause with `_RNC_SEALED_HEAD` and `_RNC_MERGE`
  present and unset, the `ROADMAP` propagation and the census entry. **No manuscript changes.**
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no
  rebase, no amend, no force-push. A red badge caused solely by an archive clause that entered
  `main` after the base is not a research failure; the certification of record is the run whose
  `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled
   named and no existing seal constant altered;
2. **`RN0`** — the bounded search, recorded in full, with the per-term result and the finding stated
   as a finding about the record;
3. **`RN1`** — the refinement, with its bounded reading and its refused converse;
4. **`RN2`** — the two contrapositives and the instantiation at act 15's triple, each reported
   separately, with act 15's exhibition consumed at its own existential strength;
5. **`RN3` (a)** — the decision about act 15's triple on `𝒪₃`, in the status rule's frozen wording,
   with the named time pair and named entry where it is negative, and with what it does not
   establish said in terms;
6. **`RN3` (b)** — the outcome as the highest line of the four-line hierarchy the kernel actually
   carries: `RN3⁺`, `RN3-S` with `S₃` written out, `RN3-N` with `N₃` written out and `S₃` explicitly
   not claimed, or UNDECIDED — in the status rule's frozen wording for the outcome reached, with the
   obstruction named in the UNDECIDED case;
7. **`RN4`** — the non-factorization consequence on `𝒪₂`, with act 14's `PQ4` (c) unedited and its
   two readings recorded apart;
8. **the carrier rule as honoured**, clause by clause: every verdict named its carrier, no verdict
   travelled, and the three named failure modes of hazard 1 did not occur;
9. the frozen `P0` sentence for the case reached, verbatim, and the row's label unchanged;
10. what no outcome licenses, in this file's wording, and the status rule as honoured;
11. the relation to acts 11, 12, 13, 14 and 15 — every merged label consumed, none revised — and act
    13's `CT3` (d) still UNDECIDED, with the anti-conflation clause carried verbatim at each
    mention;
12. the definition count against the two-slot budget, with the conditional slot marked fired or
    unused;
13. the chronology certification, naming the property certified, the preconditions checked at `B`,
    and the archive-mode pins as unset at execution;
14. the axiom table with one line per named result;
15. the discrepancies, if any, recorded and not repaired — act 14's `PQ4` (c) readings and act 14's
    `𝒪₃` role description among them.
