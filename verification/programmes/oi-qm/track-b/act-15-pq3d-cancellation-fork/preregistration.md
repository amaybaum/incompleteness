# Track B act 15 — the `PQ3` (d) cancellation fork: CONTROL PLANE

Owner-called. This file is the whole of act 15's control plane and is merged **alone**, before any
execution object exists. It takes up the single question act 14 left open: the cancellation fork
`PQ3` (d), asked on act 14's relative-candidate carrier `𝒪₂`.

**Blob identity is authoritative.** The execution guard pins this file by content.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** Under `§A.37` a sealing round is one whose preregistration
prospectively owns seal state — it creates new seal and pin state, or explicitly takes ownership of
changing existing seal state. This freeze creates new seal state: the execution writes a new Lean
module with its own guard clause in `verification/lean/edge_rigidity_probe.py` under the reserved
tag **`R7-TCF`**, and that clause carries two archive-mode seal constants which this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_TCF_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_TCF_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_TCF_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_TCF_SEALED_HEAD` to `E` and `_TCF_MERGE` to `L`, moving the `R7-TCF` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_TCF_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

**What this round does NOT own.** It alters **no existing seal constant**. `_CTI_SEALED_HEAD`,
`_CTI_MERGE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE` — act 13's and act 14's seals — are read and never
written. An archive seal belongs to the round that set it: touching the guard file that carries
those constants does not make this round their owner, and the execution's diff against
`edge_rigidity_probe.py` **adds** the `R7-TCF` clause and changes nothing else in the file.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `b41d22812f8c099a7435cee0d3bb869c3f45474c`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/preregistration.md` | `1b16008470bb1e2456c57aad58421a5941a55e0c` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md` | `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md` | `f614b666ad9098f866969c4c524e47f504e5d71c` |
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
| `verification/ROADMAP.md` | `4f9af3d3e8a2d5d66ff063c94a388d2c7c04f218` | **read** as the pinned statement of the `P0` row and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `dc30d365a06cb3a118d3bdb100c18b9b8c0d799e` | the `R7-TCF` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `179d57a9245b117f0db76fc9dec5362dc7a8fe2b` | one import line added after act 14's module |
| `verification/lean-mathlib/OIBridge/CancellationFork.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one file this round both reads and writes, and it is listed here
rather than above for exactly that reason: the verbatim clause governs the read-only table without
qualification, and the `ROADMAP`'s treatment is stated in its own row. If its blob differs at the
base, the execution records the discrepancy and does not repair the freeze.

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**Why it matters here.** Four sibling control planes are opening concurrently and several will merge
into `main` before this round's execution begins, so this round's mandated base — the merge commit
of this control-plane pull request — will carry results this freeze does not consume.

## Source scoping, carried from act 14

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists

Act 14 answered the threading question relative to four frozen carriers of observables and adopted
none. Its one undecided target is the cancellation fork `PQ3` (d), and act 14 named that fork's
obstruction precisely rather than leaving it as a gap. This round takes up that fork and nothing
else.

### `PQ3` (d), as act 14's freeze states the question

Quoted verbatim from `act-14-threading-observability/preregistration.md`, lines 409–412:

> **(d) Fork — can a nontrivial left part and a nontrivial strong-right part cancel on `𝒪₂`? NOT
> predicted.** The question: is there a coherent lift `U`, a constant `W ∈ 𝒢_L` and a strong family
> `K` such that `𝒪₂(W U_· K_·) = 𝒪₂(U)` while `𝒪₂(W U_·) ≠ 𝒪₂(U)` and `𝒪₂(U_· K_·) ≠ 𝒪₂(U)` — a
> pair separated by neither composite half yet identified as a whole.

and the two labels, from the same file, lines 416–417:

> | **`PQ3-d⁺`** | such a triple exists — the pair can be redundancy relative to `𝒪₂` while neither part is | an exhibited triple with all three conjuncts proved |
> | **`PQ3-d⁻`** | no such triple exists — relative to `𝒪₂` the pair is redundancy only when both parts are | a universal theorem over `≈_T` |

### What act 14 settled, and what it left open

**Settled, and consumed here unmodified.** `PQ0` (a)–(d); `PQ1` (a)–(c) and `PQ1` (d) in both
halves; `PQ2` (a)–(c); `PQ3` (a)–(c); `PQ4`. In particular `PQ3` (b) settles the analogous question
on the anchored-channel carrier `𝒪₁`: `pq3b_pair_factors_through_left` and
`pq3b_no_cancellation_on_anchoredChannel` prove that relative to `𝒪₁` the pair is redundancy for a
given lift **iff** its left part is, so on `𝒪₁` there is no case of "the pair separates although
neither part does". **That is a statement about `𝒪₁` and travels to no other carrier**, `𝒪₂`
included; act 14's own status rule 5 says so, and this freeze carries it.

**Left open.** `PQ3` (d) alone, recorded UNDECIDED with the obstruction named.

### The obstruction, quoted verbatim from act 14's result

From `act-14-threading-observability/result.md`, lines 320–328:

> **The obstruction, named.** The pair's relative object is `W (U_t K_t K_sᴴ U_sᴴ) Wᴴ`, the left
> part's alone is `W (U_t U_sᴴ) Wᴴ` and the strong-right part's alone is `U_t K_t K_sᴴ U_sᴴ`.
> `PQ3-d⁺` would need an exhibited triple in which the `𝒢_L`-conjugation undoes, in the anchored
> readback and at **every** time pair, exactly what the strong threading does — with all three
> conjuncts proved; `PQ3-d⁻` would need a **universal** theorem over `≈_T` saying no such
> cancellation exists. The tree contains neither ingredient: act 13's `CL1` and act 11's `GL2` are
> both **existential** statements about how the two parts move the relative candidate, and **no
> universal theorem about how a `𝒢_L`-conjugation acts on the readback of a general relative object
> exists anywhere in the merged record**. Neither side was attempted in this round.

**That last clause is the whole reason this freeze is shaped the way it is.** The branch this
programme refers to as `PQ3-d⁻` requires a universal theorem quantified over the threading
equivalence `≈_T`, and act 14 recorded that no such theorem is in the merged record. This freeze
does not take that recording on trust: `CF0` below makes the absence a target of this round, settled
by a named and bounded search, with the survey behind the freeze's prediction recorded as the
prediction's reason and not as a finding.

**So a second UNDECIDED is a live outcome of this round, preregistered as such and not as a
fallback.** A round that must either exhibit a triple or supply a universal theorem the record does
not contain can honestly end with neither. The status rule below writes that outcome's post-round
sentence out in full, and the prediction table rates the fork's resolution at no better than
**low**.

## The act 13 `CT3` (d) anti-conflation clause, FROZEN VERBATIM

Act 13's fork `CT3` (d) is structurally similar to `PQ3` (d) and must not be conflated with it in
either direction. The clause below is **THE CLAUSE**, and it is carried as a block quote **at every
mention of `CT3` (d)** in this file and in every artifact of this round.

**How each carriage is written, and why.** Each carriage opens with one line naming where it is
being carried, and then states the clause word for word. The naming line is there so that the
carriages read as distinguishable copies of one clause rather than as one paragraph pasted repeatedly
— which is a defect the repository's duplicate check exists to catch — and it changes nothing about
the clause it introduces.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed propagation
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name `CT3` (d) among the labels this round does not touch.

**THE CLAUSE:**

> `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
> cross-Gram separates every strong-right threading — a question about one datum's separating power.
> `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right gauge can
> cancel on the relative-candidate carrier — a question about cancellation between two parts of one
> relation. **Neither instantiates, constrains, nor supplies evidence for the other, and no
> implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this
> round returns, and no outcome of this round moves it in either direction.

Act 13's `CT3` (d) therefore appears in **analysis only**. **No target of this round is carried by
`CT3` (d)**, no target cites it as evidence, and no determination changes sign or strength because
of it. Writing a `PQ3` (d) outcome as if it bore on `CT3` (d), or an ingredient of `CT3` (d) as if
it bore on `PQ3` (d), is a **defect of this round** and is checked for in the final report.

For the reader's convenience, `CT3` (d)'s own recorded route to a label, quoted verbatim from
`act-13-cross-time-invariants/result.md`, lines 212–218 — and governed by the clause above:

> **(d) The fork — does level 3 separate every `GL2`-type pair? UNDECIDED.** Neither `CT3-d⁺` nor
> `CT3-d⁻` was reached, and neither is claimed. The route to the label: by `CT2` (a) a
> strong-right-related pair with equal `Ξ` at every `t, s` is constant-left related, `U' = C U` with
> `U_tᴴ C U_t` strong for every `t`; `CT3-d⁺` would need a universal theorem that every such `C`
> conjugates every relative object without moving its anchored readback, and `CT3-d⁻` would need an
> exhibited pair satisfying the strong-right and `Ξ`-equality conjuncts with distinct candidates.

> **THE CLAUSE, carried at this mention — the quotation of `CT3` (d)'s own route to a label.**
> `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
> cross-Gram separates every strong-right threading — a question about one datum's separating power.
> `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right gauge can
> cancel on the relative-candidate carrier — a question about cancellation between two parts of one
> relation. **Neither instantiates, constrains, nor supplies evidence for the other, and no
> implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever this
> round returns, and no outcome of this round moves it in either direction.

**One resemblance is recorded here so that it is not mistaken for a bridge.** Both forks have a
branch whose ingredient is "a universal theorem about a conjugation that does not move an anchored
readback". The two theorems quantify over different things — `CT3` (d)'s over constant-left elements
`C` forced by `Ξ`-equality on strong-right-related pairs, `PQ3` (d)'s over triples `(U, W, K)` with
`W ∈ 𝒢_L` and `K` a strong family — and **neither would establish the other**. Recording the
resemblance is not transferring it, and no target of this round is stated over `CT3` (d)'s objects.

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13 and 14

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `U : ℕ → U(V × A)` a lift, and the
following are consumed **unmodified**, at their own strengths, exactly as act 14 consumes them:
`readback`, `AdmissibleDilationAt`, `admissible_permMatrix`, `admissible_mul_of_fixes_anchor`,
`readback_isColStochastic`, `readback_relabel` (`R-3`), `one_admissible_at_every_anchor`,
`StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`, `GaugeRelated`, `strong_mem_weak`,
`strong_eq_one_of_ancilla_subsingleton`, `gaugeRelated_strong_iff_agree_on_anchor`,
`gl2_strong_gauge_moves_relative_candidate` (`GL2`), `gl3_constant_gauge_preserves_relative`
(`GL3`), `visible_marginal_eq_one_of_visible_subsingleton`, `LeftFibreGroup`, `FibreGram`,
`left_mul_submatrix`, `left_block_unitary`, `fibreGram_left_mul`, `left_preserves_admissible`,
`inFibreSwap_leftFibreGroup`, `CrossGram`, `FibreCrossGram`, `ConstLeftRelated`, `ConstRightRelated`,
`mul_strong_anchor_col`, `mul_strong_submatrix`, `ct2a_relative_conj`, `ct2a_crossGram_iff_constLeft`,
`ct2b_fibreCrossGram_iff`, `ct3g_fibreCrossGram_strong_right` (`CT3` (G)),
`ct4_constant_left_obstruction` (`CT4`), `cl1_constant_left_moves_relative_candidate` (`CL1`),
`AnchoredChannel`, `CrossFibreGram`, `ThreadingRelated` (`≈_T`), `UniformLeft`, and act 14's `PQ0`,
`PQ1`, `PQ2`, `PQ3` (a)–(c) and `PQ4` statements.

**The four carriers are act 14's**, frozen there with their presuppositions, and **none is adopted
as the physical one and none is asserted not to be**. This round asks its question on `𝒪₂`, the
relative-candidate carrier, because that is the carrier act 14's fork is asked on.

**The relative object** is `U_t U_sᴴ` and **the relative candidate** is `readback a₀` of its
entrywise modulus squared, exactly as acts 7, 11, 13 and 14 write them.

**The triple.** A **triple** is a datum `(U, W, K)` with `U` a coherent lift, `W` a constant matrix
with `LeftFibreGroup W`, and `K : ℕ → U(V × A)` a family with `StrongAnchorStabilizer a₀ (K t)` for
every `t`. Its **composite** is `U'_t := W · U_t · K_t`, which is `≈_T`-related to `U` by act 13's
`CT2` (b) as act 14 names that relation. A triple is **cancelling** iff all three of act 14's
conjuncts hold: `𝒪₂(U') = 𝒪₂(U)`, `𝒪₂(W U_·) ≠ 𝒪₂(U)` and `𝒪₂(U_· K_·) ≠ 𝒪₂(U)`.

**`PQ3-d⁺` is the existence of a cancelling triple; `PQ3-d⁻` is the universal statement that none
exists.** This file does not restate act 14's fork in different words anywhere else; the definition
just given is the fork, and every target below is stated over it.

**Act 7's boundary is carried at every use of `𝒪₂`**, exactly as act 14 carries it: act 7's `D4b`
came back **negative** — Source A supplies no general map carrying the relative candidate on the
dilated carrier back to `V` — and the readback is the repository's own, frozen by act 7's readback
amendment. Every `𝒪₂` statement in this round is a statement under that convention, said at each
use rather than once in a footnote.

## The evidence rule, FROZEN

`CF0` is settled by **locating and quoting**, not by proving a theorem. Its evidence rule is frozen
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
is true.

**The bounded search for `CF0` is fixed now**, so that its boundary cannot be chosen after its
result is known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/` and under
  `verification/lean/`; every `preregistration.md` and `result.md` under
  `verification/programmes/oi-qm/`; and `verification/ROADMAP.md`.
- **The search terms**: `ThreadingRelated`, `LeftFibreGroup`, `readback`, `RelativeCandidate`,
  `CrossGram`, `conj`, `cancel`, and the merged label names `GL2`, `GL3`, `CT2`, `CT3`, `CT4`,
  `CL1`, `PQ3`.
- **The question asked of each hit**: does this declaration state, for **every** lift, **every**
  `W ∈ 𝒢_L` and **every** strong family, a conclusion about `readback a₀` of the modulus square of
  `W (U_t K_t K_sᴴ U_sᴴ) Wᴴ` — or a statement from which such a conclusion follows by consuming
  merged results alone, with the consumption exhibited?
- **The recorded answer per hit** is one of: *supplies it* (quoted, with coordinate); *does not
  supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

The execution records the search in the result note in full. **A search that finds the theorem is a
finding, and a search that does not is equally a finding** — the second being that the record is
silent on the point, which is what `CF0` asks.

## The targets, FROZEN

Six targets, `CF0` through `CF5`. Each names what settles it and what evidence counts.

### `CF0` — is the universal ingredient `PQ3-d⁻` needs present in the merged record?

**The question.** Does the merged record contain a universal theorem, quantified over the threading
equivalence `≈_T` — equivalently over triples `(U, W, K)` as defined above — about how a constant
`𝒢_L` conjugation acts on the anchored readback of a general relative object?

**What settles it.** The bounded search frozen above, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule if the theorem is found — a verbatim
quotation with a coordinate, plus the derivation of the fork's `PQ3-d⁻` branch from it if that
derivation is immediate. Rule 3 if it is not — the recorded statement that the passage sought does
not exist on the named and bounded search, with the per-term record.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `CF0`**, and no outcome of `CF0` is a
theorem of this round.

**What `CF0` is not.** It is not a claim that the theorem is false, not a claim that it is
unprovable, and not a claim about what a future round could prove. It is a statement about the
merged record at this freeze's base.

### `CF1` — the cancellation equation in normal form

**The statement.** For every lift `U`, every `W` with `LeftFibreGroup W`, every family `K` with
`StrongAnchorStabilizer a₀ (K t)` for all `t`, and all `t, s`, with `U'_t = W U_t K_t`:

```
U'_t (U'_s)ᴴ  =  W · ( U_t K_t K_sᴴ U_sᴴ ) · Wᴴ
```

and hence `𝒪₂(U')(t,s) = readback a₀ ( | W (U_t K_t K_sᴴ U_sᴴ) Wᴴ |² )`.

**What settles it.** A Lean theorem at evidence level 2, universally quantified, proved from the
unitarity of `W` — which `LeftFibreGroup` carries as its first conjunct — and nothing else. Act 13's
merged `ct2a_relative_conj` is the `K ≡ 1` case and is consumed, not re-proved.

**Bounded reading, frozen.** This is an identity of matrices. **It says nothing about the value of
the readback**, nothing about whether the two sides' readbacks agree, and nothing about the fork. It
is the object over which `CF2`, `CF3`, `CF4` and `CF5` are stated, so that every later statement is
about one written-down thing.

### `CF2` — time-dependence of the strong family is necessary in any cancelling triple

**The statement.** For every triple `(U, W, K)` in which `K` is constant in `t` — that is, `K_t = K₀`
for every `t` — the third conjunct fails: `𝒪₂(U_· K_·) = 𝒪₂(U)`. Hence **no cancelling triple has a
strong family constant in time.**

**What settles it.** A Lean theorem at evidence level 2, consuming act 11's merged **universal**
`gl3_constant_gauge_preserves_relative`, which gives `(U_t K₀)(U_s K₀)ᴴ = U_t U_sᴴ` for every unitary
`K₀` and all `t, s`. The readbacks are then equal because the matrices are.

**Bounded reading, frozen.** `GL3` **stands as act 11 states it** and is consumed, not extended.
`CF2` says time-dependence is **necessary** for the strong part to move the relative candidate; it
does **not** say time-dependence is sufficient, and act 11's own note says so in terms — "Neither
statement says … that *every* time-dependent gauge moves *every* relative candidate". This round
adds no converse.

### `CF3` — the cardinality scoping of any cancelling triple

Two conjuncts, predicted separately and reported separately.

**(a) `|A| ≥ 2` is necessary.** When `A` is a subsingleton, every strong element is the identity, by
act 11's merged `strong_eq_one_of_ancilla_subsingleton`; so `K` is constant in `t`, and `CF2`
applies. Hence **no cancelling triple exists with a single ancilla configuration.**

**(b) `|V| ≥ 2` is necessary.** When `V` is a subsingleton, the relative candidate of every lift is
the constant `1` at its single entry — the readback of a column-stochastic matrix on a one-element
visible index set, by act 7's merged `readback_isColStochastic` with act 11's merged
`visible_marginal_eq_one_of_visible_subsingleton` — so the second conjunct fails for every `W`.
Hence **no cancelling triple exists with a single visible outcome.**

**What settles each.** A Lean theorem at evidence level 2, stated as a conjunct of one theorem in
the form act 12's, act 13's and act 14's cardinality conjuncts take.

**Bounded reading, frozen.** `CF3` bounds where a `PQ3-d⁺` witness could live. **It is not evidence
that one exists**, and its two conjuncts are not evidence for each other.

### `CF4` — the two non-triviality conjuncts, reduced to statements about the relative objects

**(a)** The third conjunct — `𝒪₂(U_· K_·) ≠ 𝒪₂(U)` — implies that there are times `t, s` with
`U_t K_t K_sᴴ U_sᴴ ≠ U_t U_sᴴ`. So any cancelling triple's strong family moves the relative **object**
and not only its readback, at some time pair. Act 11's `GL2` is the merged **existential** statement
that such a family exists on one exhibited lift; **`CF4` (a) does not enlarge `GL2`** and `GL2`
stands as stated.

**(b)** The second conjunct — `𝒪₂(W U_·) ≠ 𝒪₂(U)` — implies, through act 13's merged
`ct2a_relative_conj`, that there are times `t, s` with
`readback a₀ (|W (U_t U_sᴴ) Wᴴ|²) ≠ readback a₀ (|U_t U_sᴴ|²)`; in particular `W ≠ 1`. Act 13's `CT4`
with `CL1` is the merged **existential** statement that such a `W` exists on one exhibited lift;
**`CF4` (b) does not enlarge `CT4` or `CL1`** and both stand as stated.

**What settles each.** A Lean theorem at evidence level 2, each the contrapositive of an equality of
matrices, stated as conjuncts of one theorem.

**Bounded reading, frozen.** `CF4` is a pair of necessary conditions on a hypothetical witness.
**Neither is evidence that a witness exists, and neither is a step toward one.** Together with `CF2`
and `CF3` they are the constraints any `PQ3-d⁺` witness must satisfy, written down so that a later
round has them stated rather than reconstructed. **Their conjunction is not a further, stronger
statement**, and in particular it is not a non-existence theorem.

### `CF5` — THE FORK: `PQ3-d⁺`, `PQ3-d⁻`, or UNDECIDED for the second time

**The question is act 14's, restated over `CF1`'s normal form and over nothing else.** Is there a
triple `(U, W, K)` that is cancelling?

| label | statement | earned only by |
| --- | --- | --- |
| **`PQ3-d⁺`** | a cancelling triple exists — relative to `𝒪₂` the pair can be redundancy while neither part is | an exhibited triple with **all three** conjuncts proved in the kernel, at evidence level 2, with the lift's coherence discharged from merged results and the two inequalities certified at named time pairs and named entries |
| **`PQ3-d⁻`** | no cancelling triple exists — relative to `𝒪₂` the pair is redundancy only when both parts are | a **universal** theorem over `≈_T`, at evidence level 2, quantified over every lift, every `W ∈ 𝒢_L` and every strong family, with no cardinality hypothesis beyond those `CF3` establishes as necessary |
| **UNDECIDED** | neither branch was reached | the recorded statement that neither was reached, with the obstruction named and with `CF0`'s finding recorded alongside it |

**A second UNDECIDED is a preregistered outcome of this round, not a fallback.** The freeze rates it
the single most likely outcome and says so in the prediction table, with its reason. Its post-round
sentence is written out in full in the status rule below, before the round runs.

**What `CF5` may not do.** It may not report a branch at a strength the kernel does not carry; it
may not report `PQ3-d⁻` on the strength of `CF2`, `CF3` and `CF4` together, which are necessary
conditions and not a universal theorem; and it may not report `PQ3-d⁺` on the strength of an
unexhibited construction. **Reporting `PQ3-d⁻` because a witness was sought and not found is the
specific error this target's status rule exists to prevent.**

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `CF0` | **negative** — the record is silent; the universal ingredient is not there | **high** | A pre-freeze survey of the file set named in the evidence rule found the universal readback statements to be act 7's `readback_isColStochastic`, `readback_relabel` (`R-3`, a relabelling of the ancilla **type** along a bijection carrying the anchor), `readback_of_admissible` and `readback_permMatrix_apply`, none of which concerns a `𝒢_L` conjugation of a general relative object; act 13's `ct2a_relative_conj` gives the conjugation **identity** and stops there; act 11's `GL3` is about a constant right factor; and every `𝒪₂` separation in the record — `GL2`, `CT4`, `CL1`, `PQ1` (c), `PQ2` (c), `PQ3` (c) — is existential on an exhibited lift. The survey is the freeze's **reason**, not a finding: `CF0`'s finding is whatever the execution's own bounded search records. |
| `CF1` | positive | **high** | Algebra from the unitarity of `W`, which `LeftFibreGroup` carries; act 13's merged `ct2a_relative_conj` is the `K ≡ 1` case and its proof is three rewrites. |
| `CF2` | positive | **high** | Act 11's merged `gl3_constant_gauge_preserves_relative` is universal over unitary right factors and gives the matrix equality directly; equal matrices have equal readbacks. |
| `CF3` (a) | positive | **high** | Act 11's merged `strong_eq_one_of_ancilla_subsingleton` collapses the strong class to the identity at `|A| = 1`, reducing (a) to `CF2`. |
| `CF3` (b) | positive | **medium** | The conclusion follows from column-stochasticity of the readback on a one-element visible index set, but the exact merged route — act 7's `readback_isColStochastic` applied to the modulus square of a unitary relative object, or act 11's `visible_marginal_eq_one_of_visible_subsingleton` — is not frozen here, and supplying the column-stochasticity of the modulus square may cost a lemma. **Reporting `CF3` (b) UNDECIDED with the obstruction named is an allowed outcome**, and it does not move `CF3` (a). |
| `CF4` (a) | positive | **high** | The contrapositive of an equality of matrices; if the relative objects agree at every time pair their readbacks do. |
| `CF4` (b) | positive | **high** | Act 13's merged `ct2a_relative_conj` rewrites the left part's relative object as the conjugation; the rest is the contrapositive. |
| `CF5` | **UNDECIDED** — the fork is recorded undecided for the second time | **medium** | `PQ3-d⁻` needs the universal theorem `CF0` predicts is absent, and constructing one is a research step no merged result reduces to a computation. `PQ3-d⁺` needs a triple in which a `𝒢_L` conjugation undoes, in the anchored readback and at **every** time pair, exactly what a strong threading does; the freeze names no candidate and knows of none. |
| `CF5` → `PQ3-d⁺` | not predicted | **low** | If a witness is found the freeze expects it to come from a permutation triple on small `V` and `A`, where the readback is a sum of zeros and ones; the freeze names no such triple and does not rate the search better than low. |
| `CF5` → `PQ3-d⁻` | not predicted | **low** | Rated low for the reason `CF0` records: the ingredient is absent from the merged record, and the round's definition budget does not fund building a general theory of how `𝒢_L` conjugation acts on anchored readbacks. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named.

**The two `CF5` rows rating `PQ3-d⁺` and `PQ3-d⁻` at low are the freeze's whole position on the
fork's resolution.** No sentence of this file predicts the fork's resolution at medium or high.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached.
The wording is fixed before the round runs so that no outcome can choose its own wording.

### `CF0`

- **Outcome `CF0`-silent** — the bounded search records that the passage sought does not exist:
  > On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
  > `verification/lean/`, every `preregistration.md` and `result.md` under
  > `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
  > the merged record contains no universal theorem, quantified over the threading equivalence,
  > about how a constant `𝒢_L` conjugation acts on the anchored readback of a general relative
  > object. **The finding is that the record is silent on the point.** It is not a finding that such
  > a theorem is false, not a finding that it is unprovable, and not a bound on what a later round
  > could prove. Act 14's recording of the same absence is confirmed on this round's own search and
  > is not enlarged.
- **Outcome `CF0`-found** — the search locates the theorem:
  > The merged record contains the universal ingredient, quoted verbatim above with its coordinate.
  > **Act 14's recorded absence is recorded as a discrepancy against this round's search and act
  > 14's result note is not edited**: a merged result note is a statement about its own round and
  > stays as it stands. Whether the located theorem yields `PQ3-d⁻` is `CF5`'s question and is not
  > settled by locating the theorem.

### `CF1`

- **Outcome `CF1`-positive:**
  > The composite's relative object is the constant left element's conjugation of
  > `U_t K_t K_sᴴ U_sᴴ`, universally, at evidence level 2. This is an identity of matrices; it says
  > nothing about the value of any readback and nothing about the fork.
- **Outcome `CF1`-UNDECIDED:**
  > The normal form was not reached in the kernel, and every later target that is stated over it is
  > reported UNDECIDED with this recorded as the obstruction.

### `CF2`

- **Outcome `CF2`-positive:**
  > No cancelling triple has a strong family constant in time, at evidence level 2, through act 11's
  > merged `GL3` consumed as the universal statement it is. **This is a necessary condition on a
  > hypothetical witness and is not evidence that one exists.** `GL3` is not extended and no
  > converse is claimed: time-dependence is necessary for the strong part to move the relative
  > candidate, and is not shown sufficient.
- **Outcome `CF2`-UNDECIDED:**
  > Whether a cancelling triple's strong family must be time-dependent is undecided in this round,
  > with the obstruction named; act 11's `GL3` stands as stated and nothing is claimed from it here.

### `CF3`

- **Outcome `CF3`-both:**
  > No cancelling triple exists with a single ancilla configuration or with a single visible
  > outcome, at evidence level 2: `|A| ≥ 2` and `|V| ≥ 2` are necessary, each as a conjunct of one
  > theorem. **These bound where a witness could live and are not evidence that one exists.**
- **Outcome `CF3`-(a)-only:**
  > `|A| ≥ 2` is necessary for a cancelling triple, at evidence level 2. Whether `|V| ≥ 2` is
  > necessary is undecided in this round, with the obstruction named, and `CF3` (a) does not cover
  > it.
- **Outcome `CF3`-UNDECIDED:**
  > Neither cardinality scoping was reached, with the obstruction named.

### `CF4`

- **Outcome `CF4`-both:**
  > In any cancelling triple the strong family moves the relative object itself at some time pair,
  > and the constant left element moves the anchored readback of some relative object, so `W ≠ 1`;
  > both at evidence level 2. Act 11's `GL2` and act 13's `CT4` with `CL1` are the merged
  > existential statements that each is possible on one exhibited lift; **neither is enlarged, and
  > neither of these necessary conditions is evidence that a cancelling triple exists.**
- **Outcome `CF4`-partial or UNDECIDED:**
  > The conjunct reached is reported at evidence level 2 and the other is reported UNDECIDED with
  > the obstruction named; neither covers the other.

### `CF5` — the fork, with the second UNDECIDED written out in full

- **Outcome `PQ3-d⁺`:**
  > A cancelling triple is exhibited: relative to the relative-candidate carrier, and under act 7's
  > readback convention with `D4b` negative, the pair of a constant in-fibre left move and a
  > time-dependent strong right gauge can be redundancy while neither part is. The triple's three
  > conjuncts are proved in the kernel at evidence level 2, with the lift's coherence discharged
  > from merged results and the two inequalities certified at named time pairs and named entries.
  > **This is a statement about `𝒪₂` and travels to no other carrier**; act 14's `PQ3` (b) settles
  > the analogous question negatively on `𝒪₁` and the two do not conflict, `𝒪₁` and `𝒪₂` being computed
  > from different operations on the lift with no implication proved between them in either
  > direction. **No carrier is adopted as the physical one**, `P0` stays OPEN and two-part, and
  > nothing here names, endorses or excludes a selection principle.
- **Outcome `PQ3-d⁻`:**
  > No cancelling triple exists: relative to the relative-candidate carrier, and under act 7's
  > readback convention with `D4b` negative, the pair is redundancy only when both parts are. The
  > statement is universal over the threading equivalence at evidence level 2, with the universal
  > ingredient supplied by this round and recorded as this round's own result. **This is a statement
  > about `𝒪₂` and travels to no other carrier.** **No carrier is adopted as the physical one**,
  > `P0` stays OPEN and two-part, and nothing here names, endorses or excludes a selection
  > principle.
- **Outcome `CF5`-UNDECIDED — the SECOND UNDECIDED, its post-round sentence frozen in full:**
  > **The cancellation fork `PQ3` (d) is recorded UNDECIDED for the second time.** Neither
  > `PQ3-d⁺` nor `PQ3-d⁻` was reached in this round, and **neither is claimed**. `PQ3-d⁺` would need
  > an exhibited triple in which the constant left element's conjugation undoes, in the anchored
  > readback and at every time pair, exactly what the strong threading does, with all three
  > conjuncts proved; this round exhibits no such triple and names no candidate. `PQ3-d⁻` would need
  > a universal theorem over the threading equivalence saying no such cancellation exists; on the
  > named and bounded search this round records, that theorem is absent from the merged record, and
  > this round does not supply it. **What this round adds is the shape of any resolution and not a
  > resolution**: the composite's relative object is the constant left element's conjugation of
  > `U_t K_t K_sᴴ U_sᴴ`; a cancelling triple's strong family cannot be constant in time; none exists
  > with a single ancilla configuration or with a single visible outcome; and in any such triple the
  > strong family moves the relative object itself while the constant left element moves the
  > anchored readback of some relative object. **A second UNDECIDED is a statement about this round
  > and about the record, and not about the question.** It is **not** a finding that the fork is
  > unresolvable, **not** a finding that it is hard, **not** a bound on what a later round can do,
  > and **not** a finding against any settled result of act 14: `PQ0`, `PQ1` (a)–(d), `PQ2`, `PQ3`
  > (a)–(c) and `PQ4` stand exactly as act 14 states them, and `PQ3` (b)'s settlement of the
  > analogous question on the anchored-channel carrier is untouched and does not travel to `𝒪₂`. Act 13's
  > `CT3` (d) stays UNDECIDED and is untouched. **No carrier is adopted as the physical one**, `P0`
  > stays OPEN and two-part, and nothing here names, endorses or excludes a selection principle.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The sentence the execution
appends to it is fixed here.

**Case A — `CF0` silent, `CF1`, `CF2`, `CF3` (a) and (b), `CF4` (a) and (b) land, and `CF5` is
UNDECIDED.** This is the case the freeze predicts.

> `P0` remains open and two-part, and act 14's answer relative to each frozen carrier of observables
> stands exactly as act 14 states it. The cancellation fork `PQ3` (d) — whether a constant in-fibre
> left move and a time-dependent strong right gauge can cancel on the relative-candidate carrier, so
> that the pair is redundancy relative to that carrier while neither part is — is recorded UNDECIDED
> for the second time, and neither `PQ3-d⁺` nor `PQ3-d⁻` is claimed. What this round adds is the
> shape of any resolution and not a resolution: the composite's relative object is the constant left
> element's conjugation of `U_t K_t K_sᴴ U_sᴴ`; a cancelling triple's strong family cannot be
> constant in time; none exists with a single ancilla configuration or with a single visible
> outcome; and in any such triple the strong family moves the relative object itself while the
> constant left element moves the anchored readback of some relative object, so the constant left
> element is not the identity. On the named and bounded search this round records, the universal
> theorem over the threading equivalence that `PQ3-d⁻` would need is absent from the merged record,
> and this round does not supply it. A second UNDECIDED is a statement about this round and about
> the record, not about the question: the fork is not reported unresolvable, no bound on its
> difficulty is asserted, and nothing in act 14's settled results is weakened. Act 13's `CT3` (d)
> stays UNDECIDED and is untouched; neither fork answers the other. **No carrier is adopted as the
> physical one**, `P0`'s other part — what selects or constrains the Gram/orbit trajectory across
> time — is untouched, and nothing here names, endorses or excludes a selection principle.

**Case B — as A, but `CF5` reaches `PQ3-d⁺`:** the clause "is recorded UNDECIDED for the second
time, and neither `PQ3-d⁺` nor `PQ3-d⁻` is claimed" is replaced by "is answered `PQ3-d⁺`: relative
to the relative-candidate carrier, under act 7's readback convention with `D4b` negative, the two
parts can cancel, so the pair can be redundancy relative to that carrier while neither part is"; the
sentence beginning "On the named and bounded search" and the sentence beginning "A second UNDECIDED"
are omitted; every other clause stands.

**Case C — as A, but `CF5` reaches `PQ3-d⁻`:** the clause "is recorded UNDECIDED for the second
time, and neither `PQ3-d⁺` nor `PQ3-d⁻` is claimed" is replaced by "is answered `PQ3-d⁻`: relative
to the relative-candidate carrier, under act 7's readback convention with `D4b` negative, the two
parts cannot cancel, so the pair is redundancy relative to that carrier only when both parts are";
the sentence beginning "On the named and bounded search" is replaced by "the universal theorem over
the threading equivalence that `PQ3-d⁻` needs is supplied by this round and is recorded as this
round's own result"; the sentence beginning "A second UNDECIDED" is omitted; every other clause
stands.

**Case D — `CF1` UNDECIDED:** every clause of Case A's "what this round adds" list that is stated
over the normal form is omitted, the clauses that land are reported at their own strengths, and
`CF5` is UNDECIDED.

**No case closes `P0`**, and no case reports either of its two parts closed.

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The fork is unresolvable."** An UNDECIDED here is **not** a finding that the fork is
   unresolvable, not a finding that it is undecidable, and not a finding that it is hard. It is the
   recorded fact that neither branch was reached in this round.
2. **"Act 14 was wrong", or any sentence that treats an UNDECIDED here as evidence against act 14.**
   An UNDECIDED here is **not** a finding against act 14's settled results. `PQ0`, `PQ1` (a)–(d),
   `PQ2`, `PQ3` (a)–(c) and `PQ4` stand exactly as act 14 states them.
3. **"No cancelling triple exists", asserted on the strength of `CF2`, `CF3` and `CF4`.** Those are
   necessary conditions on a witness. A conjunction of necessary conditions is not a universal
   non-existence theorem, and their conjunction is not a further, stronger sentence.
4. **"A witness was sought and not found, so there is none."** Absence of a witness in this round is
   not a negative result, and no search is presented as exhaustive over triples.
5. **"The record's silence shows the theorem is false."** `CF0`'s finding, if silent, is that the
   record is silent. Silence is not a truth value.
6. **Any sentence that carries an outcome of this round to act 13's `CT3` (d), or an ingredient of
   `CT3` (d) to this round.** The anti-conflation clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
   > cross-Gram separates every strong-right threading — a question about one datum's separating
   > power. `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right
   > gauge can cancel on the relative-candidate carrier — a question about cancellation between two
   > parts of one relation. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.
7. **"The threading freedom is gauge" or "the threading freedom is physical."** Act 14's status rule
   3 binds this round too: there is no carrier-free verdict, and every verdict names its carrier.
8. **"Carrier `𝒪ₓ` is the physical one", or "carrier `𝒪ₓ` is not the physical one."** No carrier is
   adopted and none is asserted not to be.
9. **"`P0` is closed", or "`P0`'s threading part is closed."** The row stays OPEN and two-part in
   every case.
10. **"The selection principle is …", "the connection is …", "the gauge fixing is …"** — no sentence
    of this round may begin that way, and none may assert or deny that a connection or gauge fixing
    exists or suffices, in either direction.
11. **"OI and QM are inequivalent."** Two lifts differing is not two theories differing, and the
    established finite observable-law correspondence is untouched. Every `𝒪₂` statement is further a
    statement under act 7's own readback convention, with `D4b` negative.
12. **Any transfer of a verdict between carriers.** A settlement on `𝒪₁` is not a settlement on
    `𝒪₂`, in either direction, and an UNDECIDED on one carrier is not covered by a verdict on
    another.
13. **Any sentence about Track I**, or about Source B or Source C, on any axis.
14. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **Conflating `PQ3` (d) with act 13's `CT3` (d).** **This is the strongest hazard in the round.**
   The two forks are structurally similar — both left UNDECIDED by their own rounds, both turning on
   a constant left element interacting with a strong right family, both with a branch whose
   ingredient is a universal theorem about a conjugation that does not move an anchored readback —
   and the similarity is exactly what makes the error easy. The specific failure guarded against is
   an artifact of this round reporting a `PQ3` (d) outcome as bearing on `CT3` (d), or citing
   `CT3` (d)'s ingredients as evidence for `PQ3` (d). The anti-conflation clause is carried verbatim
   at every mention:
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > `CT3` (d) is act 13's fork and `PQ3` (d) is act 14's. `CT3` (d) asks whether the full column
   > cross-Gram separates every strong-right threading — a question about one datum's separating
   > power. `PQ3` (d) asks whether a constant in-fibre left move and a time-dependent strong right
   > gauge can cancel on the relative-candidate carrier — a question about cancellation between two
   > parts of one relation. **Neither instantiates, constrains, nor supplies evidence for the other,
   > and no implication transfers in either direction.** Act 13's `CT3` (d) stays UNDECIDED whatever
   > this round returns, and no outcome of this round moves it in either direction.
2. **A reader supplying the missing universal theorem from background knowledge the record does not
   contain.** **This is the second strongest hazard, and it is a hazard for the execution as much as
   for a reader.** The specific failure guarded against is a step of the form "of course a unitary
   conjugation does not change a readback" or "this is the standard invariance of a trace" —
   plausible-sounding, absent from the record, and licensed by nothing in it. The anchored readback
   is not a trace: it sums modulus squares over the ancilla index at the anchored **input** column,
   and the record contains no statement that it is unchanged by conjugation by a general element of
   `𝒢_L` — which is exactly what `CF0` asks and exactly what `PQ3-d⁻` would need. Every step of
   every proof in this round is discharged from a merged result cited by name or from an argument
   written out in the kernel. Nothing is discharged from what "is well known".
3. **Reporting `PQ3-d⁻` because a witness was sought and not found.** Absence of a witness is not a
   universal theorem. The `CF5` status rule fixes the wording for UNDECIDED so that the two cannot
   be written as one.
4. **Reporting `PQ3-d⁻` on the strength of `CF2`, `CF3` and `CF4`.** Those bound where a witness can
   live. The specific failure guarded against is adding the three necessary conditions together and
   calling the sum an impossibility result.
5. **Reporting the second UNDECIDED as a finding about the fork rather than about this round.** The
   specific failure guarded against is the sentence "the fork is unresolvable", and every paraphrase
   of it, including "no progress is possible" and "the question is ill-posed".
6. **Treating an UNDECIDED here as evidence against act 14.** The specific failure guarded against
   is a sentence weakening `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(c) or `PQ4` because this round did not
   settle `PQ3` (d). Those labels are consumed at their own strengths and none is revised.
7. **Carrying act 14's `PQ3` (b) from `𝒪₁` to `𝒪₂`.** `PQ3` (b) proves the pair factors through the
   left part on the anchored-channel carrier, so no cancellation happens there. The specific failure
   guarded against is reporting that as an answer to the fork, or as evidence for `PQ3-d⁻`. Act 14's
   own freeze records that the one-time and re-anchored rows have **no** implication proved between
   them in either direction.
8. **Treating `𝒪₂` as an established observable.** Act 7's `D4b` is negative and the readback is the
   repository's own convention. Every `𝒪₂` statement in this round is a statement under that
   convention and is reported with it at each use.
9. **Adopting a carrier.** The specific failure guarded against is a sentence of the form "since the
   physical carrier is `𝒪₂`". No carrier is adopted and none is asserted not to be.
10. **Reading `CF1` as a statement about readbacks.** `CF1` is an identity of matrices. The specific
    failure guarded against is writing "so the readbacks agree", which does not follow and is the
    fork's whole content.
11. **Extending act 11's `GL3` into a converse.** `GL3` says a constant right factor moves no
    relative object. The specific failure guarded against is reporting `CF2` as "every
    time-dependent strong family moves the relative candidate", which act 11's own note refuses in
    terms.
12. **Enlarging `GL2`, `CT4` or `CL1` from existential to universal.** Each is an existential
    statement about one exhibited lift. The specific failure guarded against is citing one of them
    as though it quantified over lifts, which is exactly the gap `PQ3-d⁻` needs filled.
13. **Treating `CF3`'s cardinality conjuncts as evidence that a witness exists.** They bound where
    one could live. The specific failure guarded against is "so a witness must have `|V| ≥ 2` and
    `|A| ≥ 2`, and here is one on `Fin 2`" with the second clause unproved.
14. **The conjugation trap, again.** Under act 7's convention `P(g) P(h) = P(h·g)` and
    `(P(σ) M)_{pq} = M_{σ p, q}`. Forced elements, anchored columns, conjugates and separating
    entries are computed in the kernel, never read off a constructor. The specific failure guarded
    against is an inverted permutation making a hoped-for cancellation look real.
15. **Forgetting the anchor.** `readback a₀` and the strong class both carry `a₀`; the relative
    object `U_t U_sᴴ` does not. The specific failure guarded against is a statement that silently
    changes which configuration is anchored — which act 7's `R-3` explicitly does **not** license,
    being a statement about names and not about which configuration is anchored.
16. **Reading act 7's `R-3` as invariance of the readback under a `𝒢_L` conjugation.** `R-3` is
    about relabelling the ancilla type along a bijection carrying the anchor. The specific failure
    guarded against is quoting `R-3` as the missing universal ingredient; it is not it, and `CF0`'s
    search records why for each hit.
17. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs; the specific failure guarded against is an execution that
    reads a lane that merged between this freeze and its base.
18. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier with a uniform prior in a different programme. Nothing is consumed or compared, and a
    shared word is not a bridge.
19. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_TCF_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
20. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
21. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: adopt a carrier as the physical one; name, endorse or exclude a selection
principle; assert or deny that a connection or gauge fixing exists or suffices; propose a datum
sufficient for the relative candidate; introduce a measurement model, regularity, homogeneity,
generated evolution or source-level coherence condition; change `CoherentLift`'s `ℕ`-indexing;
revise `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `CT1`, `CT2`, `CT3`,
`CT4`, `CL1`, `PQ0`, `PQ1`, `PQ2`, `PQ3` (a)–(c), `PQ4` or any merged label; answer act 13's fork
`CT3` (d) or move it in either direction; change `D3`, `D4b`, `D5`, the direct-branch statement or
the readback convention; alter any existing archive seal constant; consume or compare anything from
the substratum Lemma 24.1 rounds; compare Source A with B or C; edit any manuscript; close `P0` or
either of its parts; or say anything about Track I.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most two** top-level Lean definitions, and these are the two:

1. **`RelativeCandidate`** — `RelativeCandidate a₀ U t s := readback a₀ (|U_t U_sᴴ|²)`, the `𝒪₂`
   value at one time pair. This is act 14's conditional slot 6, which act 14 left **unused**;
   this round needs it because every target states an equality or an inequality of `𝒪₂` values over
   **all** time pairs, which acts 11, 13 and 14 never had to write. *Needed.*
2. **A cancelling-triple predicate** — the three conjuncts of act 14's fork as one `Prop` over
   `(U, W, K)` — *if* `CF2`, `CF3`, `CF4` and `CF5` cannot be stated readably with the conjuncts
   written inline; unused otherwise. *Conditional.*

**A third definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. **No lift, gauge element, witness, matrix, triple, entry value or pair is a
top-level definition** — each is a bound variable pinned by an equation in the statement that needs
it, as acts 10, 11, 12, 13 and 14 did. Acts 7's, 10's, 11's, 12's, 13's and 14's definitions are
**reused, not redefined**.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `CF1`, `CF2`, `CF3`, `CF4` and, if either branch is
reached, `CF5`.

**`CF0` is type P and carries no evidence level.** It is settled by the frozen evidence rule —
verbatim quotation with a coordinate, or the recorded statement that the passage sought does not
exist on the named and bounded search — and by nothing else. **Reconstructive inference is forbidden
as a finding**, and where the record is silent the finding is that it is silent.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-TCF`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_TCF_SEALED_HEAD`** and **`_TCF_MERGE`**, with
the base held in **`_TCF_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 15 object
   enters the repository tree** — any Lean definition or proof about cancelling triples, relative
   candidates or the normal form; any search artifact; any probe clause; any result artifact. **The
   single permitted exception is the analysis recorded inside this control-plane blob itself**,
   merged *as* the freeze, including the frozen evidence rule and the pre-freeze survey recorded as
   the reason for `CF0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_TCF_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _TCF_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of
   `B`**, fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_TCF_SEALED_HEAD` and `_TCF_MERGE` are present and **unset** at execution.
   After `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the
   same strong check against the sealed object: the pinned merge's second parent must equal the
   sealed head; the sealed head must pass clause 5 against `B` exactly as in its own run; and both
   must be reachable from the current target — the real `pull_request.head.sha` in pull-request
   continuous integration, `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change
   recording the two SHAs and nothing else.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md \| git hash-object --stdin` equals the blob the `R7-TCF` clause pins |
| 2 | Act 14's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'` and `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, both non-`None` |
| 3 | Act 14's module and result are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/ThreadingObservability.lean` and `git cat-file -e B:verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` both succeed |
| 4 | Act 13's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, both non-`None` |
| 5 | No act 15 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/CancellationFork.lean` |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are **not** inputs: the anti-contamination invariant governs, and the
round consumes only what this freeze's start-state table names.

**The claim is scoped to the repository record.**

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This pull request carries this file alone.**
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  Lean module, the result note, the `R7-TCF` guard clause with `_TCF_SEALED_HEAD` and `_TCF_MERGE`
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
2. **`CF0`** — the bounded search, recorded in full, with the per-term result and the finding stated
   as a finding about the record;
3. **`CF1`** — the normal form, with its bounded reading;
4. **`CF2`** — time-dependence of the strong family as a necessary condition, with `GL3` consumed
   and no converse claimed;
5. **`CF3`** — the two cardinality scopings, each reported separately;
6. **`CF4`** — the two non-triviality conjuncts, with `GL2`, `CT4` and `CL1` consumed at their own
   existential strengths;
7. **`CF5`** — `PQ3-d⁺`, `PQ3-d⁻` or UNDECIDED, in the status rule's frozen wording for the outcome
   reached, with the obstruction named in the UNDECIDED case;
8. the frozen `P0` sentence for the case reached, verbatim, and the row's label unchanged;
9. what no outcome licenses, in this file's wording, and the status rule as honoured;
10. the relation to acts 11, 12, 13 and 14 — every merged label consumed, none revised — and act
    13's `CT3` (d) still UNDECIDED, with the anti-conflation clause carried verbatim at each
    mention;
11. the definition count against the two-slot budget, with the conditional slot marked fired or
    unused;
12. the chronology certification, naming the property certified, the preconditions checked at `B`,
    and the archive-mode pins as unset at execution;
13. the axiom table with one line per named result;
14. the discrepancies, if any, recorded and not repaired.
