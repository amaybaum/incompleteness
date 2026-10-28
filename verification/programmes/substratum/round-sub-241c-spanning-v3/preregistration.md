# Substratum Lemma 24.1C, the spanning-class decision, as native round `SUB-241C-SPAN`: PREREGISTRATION

**Status: candidate control plane of a native V3 sealing round; `F` is not designated.** It is drafted
on one pull request from `D` under `AGENTS.md` §A.39, from the planning issue #986, and the owner
approved the round on 2026-10-28. The round takes up a legacy freeze that was merged and never
executed, and adopts that freeze's targets as frozen. Nothing is executed here. Only the owner
designates `F`; an instruction to proceed is not a designation.

## The declarations

```v3-round
round SUB-241C-SPAN
kind sealing
record-directory verification/programmes/substratum/round-sub-241c-spanning-v3/
```

```v3-governed-paths
record AM verification/programmes/substratum/round-sub-241c-spanning-v3/
record AM verification/receipts/SUB-241C-SPAN.json
record A verification/v3-seals/SUB-241C-SPAN.json
execution A verification/lean-mathlib/OIBridge/SpanningClassReach.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M verification/ROADMAP.md
execution M verification/README.md
```

The record directory holds this preregistration, the round's frozen controls `controls.py`, which
the first execution commit adds at the blob frozen below, and the result note `result.md`. The
receipt is `verification/receipts/SUB-241C-SPAN.json`. The seal record
`verification/v3-seals/SUB-241C-SPAN.json` is the specification's `G12` record: it is governed
`record A` and is written by the receipt commit `Q` alone, never by the execution. Every other path
the round changes is an `execution` path:

| path | class and ops | what the execution does to it |
| --- | --- | --- |
| `verification/lean-mathlib/OIBridge/SpanningClassReach.lean` | `execution A` | creates it: the round's one Lean module |
| `verification/lean-mathlib/OIBridge.lean` | `execution M` | inserts `import OIBridge.SpanningClassReach` directly after `import OIBridge.WordTraceSufficiency` |
| `verification/lean-manuscript-census.json` | `execution M` | appends one `kernel-only` family, last, with no manuscript anchor, in every decided outcome |
| `verification/ROADMAP.md` | `execution M` | inserts one paragraph in the P1 section on Lemma 24.1, directly after the 24.1A paragraph; no row, status cell or label changes |
| `verification/README.md` | `execution M` | inserts one ledger paragraph directly before `## Seal infrastructure round SI-1 — the shadow validator and the equivalence census` |

The module is `A` only because it does not exist at `F`; the other four exist at `D` and are
modified only. No other path is governed. In particular the legacy freeze's directory,
`verification/seals/`, `verification/infrastructure/legacy-records.json`,
`verification/lean/edge_rigidity_probe.py`, `papers/` and `book/` are not governed and do not change
under any outcome.

## The objects

The symbols are the specification's (`verification/infrastructure/v3/architecture.md`, Objects).

- **`D`** = `0d917665d32287e5d0ce649012175f2c7bf75b09`, the head of `main` when drafting began (the
  merge of #959). The drafting brief records its verify run 40535620231 as green; that run is
  provenance and is not an attestation of this round. Every measurement in this file was taken at
  `D`.
- **`F`**: the commit carrying this file that the owner designates. `delta(D, F)` is this file and
  any amendment under `amendments/`.
- **`E`**: the certified execution head, linear from `F`, which the owner designates.
- **`Λ`**: the last reconciliation, first parent a later base on whose first-parent chain `D` lies,
  second parent `E` (or a superseded receipt commit); built with `--no-ff` if that base is `D`.
- **`Q`**: the final receipt commit, a single-parent child of `Λ` that adds exactly the receipt and
  the seal record.
- **`W`**: the withdrawal commit of the specification's `S12`, if the round halts.

There is no pin commit (`S11`).

***

## Provenance: the legacy freeze

- **The freeze.**
  `verification/programmes/substratum/lemma-24-1c-spanning-class-decision/preregistration.md`, blob
  `b6f383741e84a1c53a599de349922f4d525e1349`, drafted against `b78eac870ba3ee9ef9e98659ac933bf97dc62226`
  and merged by PR #643 as `e21a42c6303f19356cfca6402c76e842143155d1`, the legacy freeze's mandated
  execution base. The blob is the same at the merge and at `D`.
- **Never executed.** At `D` the legacy directory holds that one file and no result note; no file
  `SpanningClassReach.lean` exists; neither the guard tag `R7-SCD` nor any `_SCD_*` constant occurs
  outside the legacy freeze.
- **Closed.** `verification/infrastructure/legacy-records.json` closes the directory (line 78) and
  pins the file at the same blob (line 350), and the release gate's `legacy-records` step keeps it.
  `verification/infrastructure/round-v3-12-retirement-census/preregistration.md:223–229` lists it among
  the five legacy directories that hold a merged control plane and no execution.
- **The rule this round follows.** `AGENTS.md:822–823` at `D`: "A question one of those rounds left
  open, or froze and never executed, is taken up by a new native round, which cites the old freeze as
  provenance and leaves the old record as it stands." The legacy directory stays byte-for-byte as it
  stands; this round's record is its own directory.

## What this round adopts

**Adopted completely, as frozen, by citation and verbatim quotation:** the targets `SC0`–`SC6`;
`SC4(a)`–`SC4(d)` at evidence level 2 with the axiom table; the `SC5` decision rule and its gate. With
them, and equally frozen: the evidence rule (§4), the definition budget (§10), the predictions (§6),
the three post-round sentences (§7), the non-licences (§8), among them the forbidden sentence
"Lemma 24.1 is false", the hazards (§9), the scoping-out of 24.1B (§0.2), the anti-contamination
invariant (§3.2), the immutable inputs (§3.4), the allowed final report (§13), the freeze's own
recorded readings (§14) and its one record-level discrepancy (§15.1).

Nothing quoted below is reinterpreted, restated in other words, weakened or strengthened. Where a
quoted passage names an object of the legacy lifecycle, the native object it reads as is fixed by the
vocabulary table that follows the quotations; that table changes no target, rule, prediction or
sentence.

**Not adopted as operative, and cited as provenance only:** §1 and §1.1 (the guard tag, the `_SCD_*`
constants and the landing `E` → `L` → `P`), §11 (the chronology control) and §12's lifecycle sentence.
The specification's lifecycle replaces them (owner decision 3). §2's passages are adopted as
`SC0`'s objects through the passage table below, and §3.1's start-state table is re-taken at `D`
(owner decision 7).

Each quotation below is the freeze's text at the cited lines of blob `b6f38374`, every line prefixed
by `> `. `controls.py freeze <F>` compares each one with the blob, line for line.

### §0.2, 24.1B scoped out

Legacy lines 66–82 (blob `b6f38374`), verbatim:

> **Concretely scoped out of this round, and named so the execution can check itself:**
>
> - 24.1B's four frozen objects — `H_obs`, `O_set`, `Φ-family`, `interleave` — are **not redefined,
>   not restated, and not consulted**. No target of this round mentions them and no determination
>   rests on one.
> - **The manuscripts are not read as evidence.** `papers/` and `book/` appear nowhere in this
>   round's start-state table, are consumed by no target, and are written by nothing. What Theorem
>   24's hypothesis fixes is 24.1B's whole content and is untouched here.
> - 24.1B's targets `WD0`–`WD4`, its partition-quantifier subtargets `WD1-q` and `WD2-q`, and its
>   gate on `WD3-no` are **not executed, not anticipated, and not answered**.
> - No sentence of this round's result may begin "the framework supplies" or "the framework does not
>   supply".
>
> **If 24.1B's result note appears at this round's mandated base**, because 24.1B's execution lands
> first, the anti-contamination invariant in §3.2 governs: it is not consumed. This round's
> determinations are the same whichever of the two executes first, and that independence is a
> property the execution checks and reports.

### §3.2, the anti-contamination invariant

Legacy lines 297–301 (blob `b6f38374`), verbatim:

> ### 3.2 The anti-contamination invariant, verbatim
>
> > A start-state discrepancy does not license the execution to consume the newer sibling result
> > merely because it happens to be present at its mandated base. The round consumes only what its
> > freeze says it consumes.

### §3.3, the files the round writes, as frozen

The blobs in this table are the legacy drafting snapshot's; the start state is re-taken at `D` below.

Legacy lines 331–349 (blob `b6f38374`), verbatim:

> ### 3.3 The files this round writes, pinned separately
>
> Named separately, because the verbatim clause in §3.1 governs the read-only table without
> qualification and does not apply to these. Each is pinned by blob at this base all the same, so
> that a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads.
>
> | path | blob at this base | what the round does to it |
> | --- | --- | --- |
> | `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | **read** as the pinned statement of the `P1` row and its section, and **written** only by appending the frozen post-round sentence for the case reached; **the row's label unchanged** |
> | `verification/README.md` | `d25eb2d44d0aa324c095930f40174296fd0f2279` | one ledger paragraph appended |
> | `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the `R7-SCD` clause **added**; **no existing seal constant altered** |
> | `verification/lean-mathlib/OIBridge.lean` | `0bff51eb9cc3c22859da2ac0efc622910e77d7b4` | one import line added after `WordTraceSufficiency` |
> | `verification/lean-manuscript-census.json` | `3e968e6c970301be5ba0b9631b234c957a6222d1` | **written**: one new **kernel-only** family entry for this round's module, carrying no manuscript anchor. Every `OIBridge` module carries one of the registry dispositions, and this module is a publication-facing kernel result this round deliberately does not propagate to a manuscript, which is what kernel-only names. The entry is written **in every outcome, `SC5-UNDECIDED` included** — the module exists and carries the round's certified kernel findings whatever `SC5` returns |
> | `verification/lean-mathlib/OIBridge/SpanningClassReach.lean` | — | created by the execution |
> | `verification/programmes/substratum/lemma-24-1c-spanning-class-decision/result.md` | — | created by the execution |
>
> `verification/ROADMAP.md` is the one file this round both reads and writes, and it is listed here
> rather than above for exactly that reason. If its blob differs at the base, the execution records
> the discrepancy and does not repair the freeze.

### §3.4, the immutable inputs

Legacy lines 351–357 (blob `b6f38374`), verbatim:

> ### 3.4 Immutable inputs
>
> Consumed as merged and unrevised: `ST0`–`ST5` from the Lemma 24.1 semigroup-transfer round; `WT0`,
> `WT1`, `WT2-gen`, `WT3` on the spanning class and `WT4` from 24.1A, with `WT2` UNDECIDED. The `P1`
> row's label is read and not moved. **`WT2` is not reopened**: no piece of its (a)–(f) obstruction is
> built, attempted, or scoped here, and a `WT2` proof appearing in the execution is a defect of the
> round.

### §4, the evidence rule

Legacy lines 361–382 (blob `b6f38374`), verbatim:

> ## 4. The evidence rule, FROZEN
>
> Every determination in this round is carried by exactly one of:
>
> 1. a **kernel theorem** in this round's module, compiled at the pin, with its `#print axioms` line
>    — evidence level 2; or
> 2. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
> 3. an explicit, recorded statement that **the passage or the Mathlib declaration sought does not
>    exist**, on a **named and bounded** search — the search stated by what was searched, with what
>    query, over what tree, so a reader can repeat it.
>
> **Reconstructive inference is forbidden as a finding.** A determination of the form "the classes
> must coincide, because otherwise `WT3` would be idle", or "Mathlib must have this, because the
> result is standard", is **not evidence** and may appear only in a clearly labelled analysis
> paragraph that says it is not evidence and that no target rests on it.
>
> **Silence is a finding.** Where the record does not settle a question, the finding is that it does
> not settle it — reported as silence, with the search that established the silence named. Silence is
> never reported as a negative answer and never reported as a positive one.
>
> **Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`. A
> determination carried by a passage that names a thing without displaying it is at most `medium`.

### §5, the targets `SC0`–`SC6`

Legacy lines 386–545 (blob `b6f38374`), verbatim:

> ## 5. The targets, FROZEN
>
> ### `SC0` — locating controls, cheap and certain
>
> Verify that each passage quoted in §2 stands at the mandated base, byte-identical, in the blob
> pinned for it in §3.1 or §3.3, and record its coordinate as found. Record any coordinate drift as a
> discrepancy without repairing the freeze.
>
> **Falsifier.** Any of the §2 passages absent from its pinned blob at the base.
>
> ### `SC1` — exactly which readings `ST2`–`ST4` refuted, and exactly which they did not
>
> Report, **each by its own verbatim quotation with a coordinate**, and **separately, never merged**:
>
> 1. **`ST2`** — the reading refuted, its carrier, and the absorption recorded with it.
> 2. **`ST3`** — the reading refuted, its carrier, and the four conjuncts the theorem carries.
> 3. **`ST4`** — the reading refuted, its carrier, and the **frozen deep-sector model** the theorem
>    is stated inside.
>
> Then report, by quotation, **what the three do not reach**: what `ST4`'s enlargement model leaves
> outside it, what the round records about generators (ii)/(iv), and the round's own statement of
> what a negative on the route does and does not license.
>
> **This target exists so that nobody re-reads the refutation as broader than it is.** The permitted
> form of every sentence in this target is "reading R, on carrier C, under model M, is refuted"; the
> forbidden form is "the transfer is refuted", unqualified.
>
> **Falsifier.** Any of the three readings not recoverable as a quoted statement with its carrier and
> its model.
>
> ### `SC2` — what `ST5` and 24.1A established, and at exactly what scope
>
> Report, by quotation with coordinates:
>
> 1. `ST5`'s **necessity** result and its scope — every word, balanced or not, on every carrier.
> 2. `ST5`'s **sufficiency** status as the Lemma 24.1 round left it, and the obstruction named there.
> 3. `WT1`'s statement and what it reaches on general pairs.
> 4. `WT2-gen` and `WT3`'s statements and the class they are stated on, with the class named by its
>    merged definition and not paraphrased.
> 5. `WT2`'s UNDECIDED status and its named obstruction, quoted.
> 6. 24.1A's frozen post-round sentence, quoted whole.
>
> **Falsifier.** Any of the six not recoverable verbatim from the pinned blobs.
>
> ### `SC3` — the route and the obligation, held apart on the record
>
> Determine, **by quotation only**, what the merged record permits and forbids being said about the
> **obligation** given that the **route** is refuted on the readings `SC1` enumerates. Report:
>
> 1. the permitted sentence, quoted, from each of the two merged results;
> 2. the forbidden sentences, quoted as lists, from each;
> 3. whether any passage anywhere in the pinned blobs asserts that the obligation itself is refuted,
>    false, established or repaired — and if none is found, **record that on a named bounded search**
>    over the pinned blobs, with the search stated.
>
> **This is the target that owns the round's central hazard.** The route and the obligation are
> different statements; a result note that treats a refutation of the first as bearing on the second
> has committed the defect this target exists to prevent.
>
> **Falsifier.** A passage found asserting anything about the obligation's truth. If one is found,
> `SC3` reports it verbatim and the round records a discrepancy against the `P1` row's status cell.
>
> ### `SC4` — the reach of the spanning class, in the kernel
>
> The round's substance. Four sub-determinations, each with its own outcome and its own strength;
> each may land independently and one landing UNDECIDED does not stop the others.
>
> **`SC4(a)` — `BlockSpanning U → HiddenCommutantTrivial U`.** For every finite `V`, `H` and every
> `U : Matrix (V × H) (V × H) ℂ`: if `wordSpan U = ⊤` then every hidden `Y` commuting with `U` is a
> scalar. The merged module already carries the closure facts this needs — `one_mem_wordSpan`,
> `visibleBlock_mem_wordSpan`, `mul_mem_wordSpan`, `conjTranspose_mem_wordSpan`
> (`WordTraceSufficiency.lean:139–181`) — so `wordSpan U` is a unital `*`-closed subalgebra, and the
> step from "commutes with every element of `M_H(ℂ)`" to "is a scalar" is the centre of a matrix
> algebra.
>
> **`SC4(b)` — the converse, `HiddenCommutantTrivial U → BlockSpanning U`.** **NOT predicted.** This
> is the direction that carries the double-commutant content: `wordSpan U` is a unital `*`-subalgebra
> of `M_H(ℂ)` whose commutant is the scalars, and the conclusion `wordSpan U = ⊤` is the double
> commutant theorem in exactly the spatial finite-dimensional form 24.1A recorded as absent. The
> execution:
>
> - attempts the direction;
> - **and, whatever the attempt yields, performs and records a named bounded search** of Mathlib at
>   the pin and of the corpus for a double-commutant or bicommutant statement for unital `*`-closed
>   subalgebras of `Matrix n n ℂ`, reporting the search terms, the trees searched, and what was
>   found or that nothing was found.
>
> Both an established implication and a recorded absence are permitted outcomes. Neither may be
> inferred from the other.
>
> **`SC4(c)` — where Pair C sits.** Decide `BlockSpanning` for the `ST3`/`ST4` carrier `φ̂_C` on
> `ℤ₂ × ℤ₃`, pinned by the same equations `ST3_pairC` pins it by, by direct computation and not by
> `SC4(b)`. `ST3` establishes `HiddenCommutantTrivial` for it (`pairC_hct`,
> `SemigroupTransfer.lean:677`), so this sub-determination settles one instance of `SC4(b)`
> independently of the general question.
>
> **`SC4(d)` — the class is a restriction, and is inhabited non-degenerately.** Exhibit, on a carrier
> with at least two visible and at least two hidden elements, one `U` with `BlockSpanning U` and one
> `U` with `¬ BlockSpanning U`.
>
> The `ST2` carrier `φ̂_A` is a candidate for the second. The Lemma 24.1 result records at
> `lemma-24-1-semigroup-transfer/result.md:141–142`:
>
> > Both hidden commutants of Pair A contain `X`, so neither is GNS-cyclic, and Pair A separates
> > the two cyclicities exactly as the freeze said it would.
>
> **That passage is prose in a result note and is not, on a bounded search of the merged module's
> axiom table, carried by a kernel theorem.** So the contrapositive route is available only if the
> execution first proves `¬ HiddenCommutantTrivial φ̂_A` in the kernel, by exhibiting `X` as a
> non-scalar element of the hidden commutant; `¬ BlockSpanning φ̂_A` then follows from `SC4(a)`. **If
> that route is taken the execution says so and names both steps.** A quoted prose statement may not
> stand in for either step, and a derived fact is not presented as a computed one.
>
> **Falsifier for `SC4` as a whole.** `SC4(a)` refuted by a counterexample. That outcome would mean
> the two predicates are not ordered at all, which the round reports as found and does not soften.
>
> ### `SC5` — the decision, assembled
>
> Exactly one of the following, at the strength jointly reached by `SC4(a)`–`SC4(d)`:
>
> - **`SC5-coincide`** — the spanning class and the GNS-cyclic class are the same class.
>   **Requires `SC4(a)` and `SC4(b)` both positive at evidence level 2.** Nothing less writes it: a
>   positive `SC4(c)` on one carrier is one instance and is not the general statement.
> - **`SC5-strict`** — the spanning class is a strict strengthening of the GNS-cyclic class.
>   **Requires `SC4(a)` positive at evidence level 2 and `SC4(b)` refuted by an exhibited `U` with
>   `HiddenCommutantTrivial U` and `¬ BlockSpanning U`**, both conjuncts proved.
> - **`SC5-UNDECIDED`** — the permitted fallback, with the obstruction named. **This is a live
>   preregistered outcome and is not a failure of the round.** It is what the round reports if
>   `SC4(b)` is neither established nor refuted, and the round's other targets still land.
>
> **The gate on `SC5-coincide` and `SC5-strict`, FROZEN:**
>
> > Neither `SC5-coincide` nor `SC5-strict` may be written on the strength of `SC4(c)` alone.
> > `SC4(c)` decides one carrier. The general relation between the two predicates is `SC4(b)`'s
> > question, and where `SC4(b)` is neither established nor refuted the outcome is `SC5-UNDECIDED`
> > with the obstruction named, whatever `SC4(c)` found.
>
> **Why this gate exists.** A single carrier on which the two predicates agree is consistent with
> their coinciding everywhere and equally consistent with their diverging elsewhere. Letting one
> instance write the general sentence would let the round reach its most consequential conclusion on
> the cheapest available evidence. The gate makes the decision rule match the target's wording rather
> than the easier question underneath it. **The gate binds the decision rule, not the prediction.**
>
> ### `SC6` — the ordering census: what evidence would settle which continuation comes next
>
> A **census, not an action.** List, with coordinates, every place in the pinned blobs that states a
> dependency between 24.1B's question and the spanning class — every passage that says one is needed
> for the other, or that one is open pending the other. Then record, without acting on it and without
> recommending it, the evidence each continuation would need:
>
> - **for 24.1B** — as 24.1B's own merged freeze specifies it, cited by coordinate and **not
>   restated**;
> - **for a `WT2` continuation** — the (a)–(f) obstruction as 24.1A's result names it, cited by
>   coordinate and not restated;
> - **for a spanning-class continuation beyond this round** — whatever `SC4(b)` leaves open, stated
>   as the open question it is.
>
> **No continuation is recommended, chosen, scheduled or begun.** The census exists so that a later
> owner call has its surface enumerated. A sentence of the form "the programme should next" is a
> defect of this round.

### §6, the predictions

Legacy lines 549–572 (blob `b6f38374`), verbatim:

> ## 6. The preregistered predictions, with signs, strengths and reasons
>
> Recorded before execution so the outcome can be compared against them.
>
> | target | prediction | sign | strength expected | reason |
> | --- | --- | --- | --- | --- |
> | `SC0` | the passages stand as quoted | positive | full | each was located and quoted while drafting this freeze, against the named blobs |
> | `SC1` | the three readings are separately recoverable with carrier and model | positive | full | the merged result states each under its own heading with its carrier inline |
> | `SC2` | all six items recoverable verbatim | positive | full | 24.1A's result states each under its own heading and quotes its own frozen sentence |
> | `SC3` | permitted and forbidden lists recoverable; **no passage found asserting anything about the obligation's truth** | positive, with the third part expected to find nothing | high | both merged results carry explicit forbidden-sentence lists; the bounded search is over a small pinned set |
> | `SC4(a)` | `BlockSpanning U → HiddenCommutantTrivial U` | positive | high | the merged module already carries unitality, multiplicative closure and adjoint closure of `wordSpan`, so the remaining content is the centre of `Matrix H H ℂ`; **high and not full, because the formal cost of the centre step at the pin is not known to this freeze** |
> | `SC4(b)` | **NOT predicted — the round's genuine fork** | none | — | the direction is the spatial double-commutant statement, which 24.1A recorded as absent from Mathlib at the pin and from the corpus. This freeze does not predict that it is unavailable, because it did not search; the named bounded search is the target |
> | `SC4(c)` | `BlockSpanning φ̂_C` decidable by direct computation | positive | medium | the carrier is `3 × 3` and finite, so the computation exists; **medium, because the formal cost of exhibiting nine spanning word values is not known to this freeze** |
> | `SC4(d)` | both witnesses exhibited | positive | medium | the `¬ BlockSpanning` witness is expected to come from `ST2`'s Pair A through `SC4(a)`; the `BlockSpanning` witness is expected from `SC4(c)` if that lands, and otherwise needs its own carrier |
> | `SC5` | **`SC5-UNDECIDED` is the single most likely outcome, and it is a full preregistered outcome of the round** | — | medium | it follows directly if `SC4(b)` lands neither way, which the gate then forces regardless of `SC4(c)`. `SC5-coincide` is the outcome if the double-commutant step proves reachable; `SC5-strict` if a separating witness exists. **This freeze leans to no one of the three** |
> | `SC6` | census assembled | positive | high | a census over pinned blobs |
>
> **Three predictions are deliberately held below full, and one is not made at all.** `SC4(b)` is the
> round's substance, and a freeze that predicted it would be claiming the answer it is chartered to
> find. `SC5` is held at medium on its most likely outcome and at no sign on the other two.
>
> **No prediction licenses its own conclusion.** A target that lands against prediction is reported
> against prediction, and the prediction is not amended. If any target lands above its predicted
> strength, the result note records the promotion and its reason.

### §7, the post-round sentences

Legacy lines 576–624 (blob `b6f38374`), verbatim:

> ## 7. The post-round sentences, frozen now, one per outcome
>
> Exactly one of the three is written, verbatim, in the result note and nowhere else.
>
> **If `SC5-coincide`:**
>
> > On every finite carrier `V × H`, the spanning hypothesis `BlockSpanning U` and the cyclicity
> > predicate `HiddenCommutantTrivial U` are the same condition, both directions at evidence level 2.
> > Lemma 24.1A's biconditional `WT3_spanning_iff` therefore holds on exactly the class the
> > semigroup-transfer route's own GNS-cyclic reading assumes, and the class on which `ST3` refuted
> > that reading and the class on which `WT3` established the biconditional are one class. This is a
> > statement about two predicates on finite matrices. **It does not repair Lemma 24.1, does not
> > restore the manuscripts' route, does not say the four generators are complete or incomplete, and
> > says nothing about whether the reconstruction framework supplies the block-word trace data, which
> > is round 24.1B's question and is untouched here.** The `P1` obligation remains OPEN and the row's
> > label does not move.
>
> **If `SC5-strict`:**
>
> > On every finite carrier `V × H`, `BlockSpanning U` implies `HiddenCommutantTrivial U` at evidence
> > level 2, and the converse fails on the carrier exhibited in the result note. The spanning
> > hypothesis is therefore strictly stronger than the cyclicity predicate, and Lemma 24.1A's
> > biconditional `WT3_spanning_iff` holds on a class strictly narrower than the one the
> > semigroup-transfer route's own GNS-cyclic reading assumes. This is a statement about two
> > predicates on finite matrices. **It does not repair Lemma 24.1, does not restore the manuscripts'
> > route, does not say the four generators are complete or incomplete, does not say that `WT3` is
> > idle, and says nothing about whether the reconstruction framework supplies the block-word trace
> > data, which is round 24.1B's question and is untouched here.** The `P1` obligation remains OPEN
> > and the row's label does not move.
>
> **If `SC5-UNDECIDED`:**
>
> > `BlockSpanning U` implies `HiddenCommutantTrivial U` at the strength recorded for `SC4(a)`.
> > Whether the converse holds is UNDECIDED, with the obstruction named in the result note, and the
> > relation between the class Lemma 24.1A's biconditional lands on and the class the
> > semigroup-transfer route's GNS-cyclic reading assumes is therefore settled in one direction and
> > open in the other. What the record does and does not settle is stated in the result note and is
> > not extrapolated. **Nothing here repairs Lemma 24.1, restores the manuscripts' route, or says the
> > four generators are complete or incomplete, and nothing here bears on whether the reconstruction
> > framework supplies the block-word trace data, which is round 24.1B's question and is untouched.**
> > The `P1` obligation remains OPEN and the row's label does not move.
>
> **If the obstruction at `SC5-UNDECIDED` is the double-commutant statement**, the result note names
> it in these terms and no others: `wordSpan U` is a unital `*`-closed subalgebra of `Matrix H H ℂ`;
> `HiddenCommutantTrivial U` says its commutant is the scalars; the conclusion `wordSpan U = ⊤` is
> the double commutant theorem in spatial finite-dimensional form; and the named bounded search found
> it at the stated place or found nothing at the stated places. **That is a statement about what the
> record and the library carry, not a claim that the converse does or does not hold.** Naming it is a
> finding; resolving it would be a later round with its own control plane.

### §8, the non-licences

Legacy lines 628–656 (blob `b6f38374`), verbatim:

> ## 8. What none of these outcomes licenses
>
> - **Nothing about the truth of Lemma 24.1 or of Theorem 24.** The forbidden sentences are "Lemma
>   24.1 is repaired", "Lemma 24.1 is false", "Theorem 24 is false", "Theorem 24 is repaired",
>   "completeness holds", "completeness fails", "the generators are complete", "the generators are
>   incomplete", and "the manuscripts' route is restored".
> - **Nothing that promotes or demotes any merged target.** `ST0`–`ST5` and `WT0`–`WT4` are consumed
>   as merged and none is revised, re-derived, extended or weakened. In particular no outcome here
>   makes `WT3` wrong, idle or absent from the record.
> - **`WT2` is not reopened.** Its (a)–(f) obstruction stays recorded as UNDECIDED. No piece of it is
>   built, attempted or scoped here. `SC4(b)` is a different statement — the double commutant for the
>   commutant-trivial case — and if establishing it would establish `WT2`, the execution **records
>   that and stops**, because reaching `WT2` through a side door is outside this freeze.
> - **Nothing about 24.1B's question**, in either direction. See §0.2.
> - **Nothing about the physical substratum.** Whether the wave rule on the cubic lattice satisfies
>   `BlockSpanning`, or what its word traces are, is not asked, and 24.1A's exclusion of it at
>   `result.md:242–243` stands.
> - **Nothing about approximate deep sectors, time reversal, or enlargement.** `ST4`'s enlargement
>   lemma is not consumed; this round is on a fixed carrier.
> - **Nothing about Track B, `P0`, act 14's carriers, act 15's fork, or the fibre-Gram
>   classification**, in either direction. The substratum programme and the OI→QM programme share the
>   repository and nothing else; act 15's preregistration is pinned in §3.1 as the **house-form
>   model** for this document and for no other purpose, and no target cites it as evidence.
> - **Nothing about Bell or H-Bell**, nothing about A6, nothing about hydrodynamics.
> - **No manuscript is edited, and no manuscript is read.** Whether and how to propagate any finding
>   is an owner call in a separate round.
> - **No selection principle is named**, and no sentence beginning "the selection principle is" is
>   written.
> - **No continuation is recommended.** `SC6` enumerates; it does not choose.

### §9, the hazards

Legacy lines 660–700 (blob `b6f38374`), verbatim:

> ## 9. Named hazards
>
> 1. **H1 — conflating the refuted route with the untouched obligation.** The central hazard of the
>    whole `P1` lane. The route is refuted on three enumerated readings; the obligation is untouched.
>    These are different statements and a result note that slides from one to the other has failed.
>    `SC1` and `SC3` exist for this hazard, the `P1` row's own wording is quoted at §2.1 as the
>    standard, and the final report states for each sentence about the obligation which quotation
>    carries it.
> 2. **H2 — fork-straddling.** A round that answered both 24.1B's manuscript question and the
>    spanning-class matrix question could move either answer to fit the other. §0.2 scopes 24.1B out
>    by name, object and evidence base; the manuscripts are absent from the start-state table; and
>    the final report states explicitly that no manuscript was read and no 24.1B object was consulted.
> 3. **H3 — reading the refutation as broader than it is.** `ST2`, `ST3` and `ST4` refute three named
>    readings on named carriers under a named deep-sector model. "The transfer is refuted",
>    unqualified, is forbidden; `SC1` requires reading, carrier and model together in every sentence.
> 4. **H4 — reading `SC5-strict` as a defect verdict on 24.1A.** A strictly stronger hypothesis is
>    not an idle theorem. The post-round sentence for that outcome is written to make the distinction
>    unavoidable and the forbidden sentences are listed.
> 5. **H5 — reading `SC5-coincide` as a repair.** If the two classes coincide, `WT3` lands on the
>    route's own class — and that still says nothing about whether the framework supplies the
>    word-trace data, which is 24.1B's question. The post-round sentence carries the exclusion inside
>    itself.
> 6. **H6 — reaching `WT2` through a side door.** `SC4(b)`'s double-commutant step is adjacent to
>    `WT2`'s (b)+(e) obstruction. If the execution finds itself building the spatial structure
>    theory, it has left this round. The non-licence in §8 says to record and stop.
> 7. **H7 — generalizing from one carrier.** `SC4(c)` decides one `3 × 3` instance. The gate in
>    `SC5` exists for this hazard and is checked for in the final report.
> 8. **H8 — reconstructive inference presented as a finding.** Forbidden by §4. The final report
>    states, per determination, which kernel theorem or which quotation carries it.
> 9. **H9 — treating silence as denial.** A bounded search that finds no double-commutant statement
>    in Mathlib at the pin establishes that the search found nothing, not that the statement is
>    unprovable. `SC4(b)` requires the search be named and bounded and its result be reported as what
>    it is.
> 10. **H10 — writing a seal this round does not own.** `_SGT_*` and `_WTS_*` belong to the rounds
>     that set them and are read and never written. §1.1 lists them; the execution's diff against
>     `edge_rigidity_probe.py` adds the `R7-SCD` clause and changes nothing else.
> 11. **H11 — consuming a sibling result present at the base.** Governed by the anti-contamination
>     invariant at §3.2, with 24.1B's own pending execution as the concrete case.
> 12. **H12 — moving the `P1` label.** The row's label stays **OPEN** on every outcome. The
>     execution appends the frozen post-round sentence for the case reached and changes no status
>     cell.

### §10, the definition budget

Legacy lines 704–723 (blob `b6f38374`), verbatim:

> ## 10. Definition budget
>
> **Two slots, both conditional, and neither expected to fire.** The round's frozen statements in
> `SC4(a)`–`SC4(d)` use only the merged definitions `BlockSpanning`, `wordSpan`, `wordEval`,
> `visibleBlock` and `HiddenCommutantTrivial`, consumed exactly as merged. The budget exists so that
> an unbudgeted definition appearing in the execution is visible as an overrun.
>
> | slot | name | what it would be | fires only if |
> | --- | --- | --- | --- |
> | 1 | `hiddenCommutant` | the commutant of the visible blocks as a `Submodule ℂ (Matrix H H ℂ)`, so that `SC4` can be stated as a relation between two subspaces | stating `SC4(a)`/`SC4(b)` as implications between the two merged predicates proves unworkable at the pin, which this freeze does not expect |
> | 2 | a named witness datum for `SC4(d)` | one `U` on a carrier with `|V| ≥ 2`, `|H| ≥ 2`, written as a definition rather than inlined | neither Pair A nor Pair C serves as the witness `SC4(d)` needs |
>
> **If a slot fires, the execution says which and why.** If a precise formal subclaim worth separating
> is uncovered, the execution **names it and does not build it**, and it becomes a candidate for a
> later round with its own control plane.
>
> **Evidence level.** `SC4` is at evidence level 2 throughout, with an axiom table and a
> `#print axioms` line for every theorem. `SC0`–`SC3` and `SC6` are type P, carried by quotation and
> by recorded silence, and the result note says so in terms rather than leaving the mixture to be
> inferred.

### §12, the execution's produce-list

Its first sentence is adopted as the list of what the execution produces, with "the `R7-SCD` guard
clause" read as `controls.py` (owner decision 3); its lifecycle sentence is replaced.

Legacy lines 752–757 (blob `b6f38374`), verbatim:

> ## 12. Execution discipline
>
> The execution produces **the result note, the one Lean module, the `R7-SCD` guard clause, the one
> import line, the one kernel-only entry in `verification/lean-manuscript-census.json`, and the
> `ROADMAP` and `README` pointers the round's own section needs** — and nothing else. One pull request from the mandated base carrying the execution; after certification the same
> pull request carries `L` and then `P`.

### §13, the allowed final report

Legacy lines 761–768 (blob `b6f38374`), verbatim:

> ## 13. Allowed final report
>
> Every target with its outcome, evidence type, strength and the kernel theorem or quotation carrying
> it; the three readings of `SC1` reported separately with carrier and model; `SC3`'s permitted and
> forbidden lists quoted; `SC4`'s axiom table; the named bounded searches with their terms and trees;
> the `SC6` census; the discrepancy section; the single frozen post-round sentence; an explicit
> statement that no manuscript was read and no 24.1B object was consulted; and an explicit statement
> of whether 24.1B's result note was present at the base and was not consumed. Nothing else.

### §14, the freeze's recorded readings

Legacy lines 772–790 (blob `b6f38374`), verbatim:

> ## 14. Points at which this freeze chose a reading, recorded rather than resolved
>
> 1. **The round is the spanning-class decision and not 24.1B.** The alternative was to take 24.1B
>    as this round's content. It is set aside because 24.1B's freeze is merged and immutable, not
>    because 24.1B is the less interesting question. §0.2 records the ground.
> 2. **"The spanning-class decision" is read here as the relation between `BlockSpanning` and
>    `HiddenCommutantTrivial`.** A different reading would take it as the question whether the
>    manuscripts' substratum lies in the spanning class. That reading needs a `Substratum` packaging
>    of the manuscripts' rule as dilation data, which no round has built; this freeze records the
>    alternative reading, does not adopt it, and leaves it to `SC6`'s census.
> 3. **The round is sealing.** An alternative would write it unguarded, as 24.1B is written, and
>    carry the immutability in the blob pins alone. This freeze does not, because the round produces
>    kernel objects and every kernel object in this programme is ordered by a guard.
> 4. **`SC4(b)` is left unpredicted rather than predicted at low strength.** Recording no sign is
>    more honest than recording a weak one, and the round's value does not depend on which way it
>    falls.
> 5. **`SC4(c)` is kept as its own sub-determination rather than folded into `SC4(b)`.** One carrier
>    settled is worth recording even where the general question is not, and the gate in `SC5` stops
>    it from being read as more.

### §15.1, the record-level discrepancy

Legacy lines 828–840 (blob `b6f38374`), verbatim:

> ### 15.1 One record-level discrepancy, recorded and NOT repaired by this round
>
> `verification/ROADMAP.md` states, in the `P1` row and again in the body, that **24.1B is "named and
> not begun"**, while `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md`
> exists at the base with blob `f614b666ad9098f866969c4c524e47f504e5d71c`. Whether a merged control
> plane counts as a round having "begun" is a reading, and this freeze takes neither side of it: what
> is recorded is that the two statements sit together on the record, so a reader of the `P1` row is not
> left to discover the freeze's existence for themselves.
>
> **This round does not repair it.** 24.1C writes nothing to `verification/ROADMAP.md`, the
> `ROADMAP` sits in the read-only start-state table, and correcting another round's row is not this
> round's to do. The execution carries this record forward into its result note unchanged and adds
> nothing to it.

***

## How the legacy text reads in this native round

| legacy term | reads here as |
| --- | --- |
| "this freeze's base", the §3.1 table at `b78eac87` | the start state re-taken at `D` (below); a pin that moved is recorded as drift, and the freeze is not repaired |
| "the mandated base", "the base", "the mandated execution base" (§2, §3.2, `SC0`, §13) | `F`. `delta(D, F)` touches only this record directory, so `F`'s tree is `D`'s everywhere else, and `SC0` is measured at `F` |
| "the execution guard", "the guard", "`R7-SCD`" | `controls.py`, frozen below; no guard clause is written |
| `_SCD_BASE` | the receipt's `f`, with `d` |
| `_SCD_SEALED_HEAD` | the receipt's `e`, with `tree_e` |
| `_SCD_MERGE` | the receipt's `landing.object`, `Λ`, whose first parent is `landing.base` |
| the pin commit `P` | none (`S11`): the seal record that `Q` adds, whose object id the receipt's `seal.records[0].blob` pins |
| "merged **alone**, before any execution object exists" | `delta(D, F)` is control-plane only and `F` is designated before the first execution commit (`S2`, T1, T2) |
| "the certification of record is the run whose `head_sha` is `E`" | `E`'s `check-run` attestation in the receipt |
| "Full continuous integration must pass again on `P` before the pull request merges" | the pull request's checks on `Q` before it lands: host operation, outside the verdict (`S10`) |
| "24.1B's result note ... present at the mandated base" | a 24.1B result present at `F`: the legacy path `lemma-24-1b-framework-data/result.md`, or a receipt `verification/receipts/SUB-241B-OBS.json` |
| `§A.37` as the governing text | the `§A.37` record; `§A.39` governs this round |
| "the `R7-SCD` clause **added**" to `edge_rigidity_probe.py` | no change to `edge_rigidity_probe.py` |

***

## The owner decisions of 2026-10-28, encoded

1. **Identity and paths.** Round `SUB-241C-SPAN`, `kind sealing`, record directory
   `verification/programmes/substratum/round-sub-241c-spanning-v3/`, receipt
   `verification/receipts/SUB-241C-SPAN.json`, seal record `verification/v3-seals/SUB-241C-SPAN.json`:
   the two declaration blocks above. Each path, and `verification/v3-seals/` itself, is absent at
   `D`, and each name the round introduces is free at `D` outside the legacy freeze (start state,
   below). This is the first use of `verification/v3-seals/`; the lifecycle rehearsal below shows
   the verifier and the release gate admitting it.
2. **Provenance.** The legacy execution base `e21a42c6303f19356cfca6402c76e842143155d1`, the frozen blob
   `b6f383741e84a1c53a599de349922f4d525e1349` and the legacy path are cited above, and the targets
   and their rules are adopted by verbatim quotation.
3. **`R7-SCD`.** Its content checks are `controls.py`'s (the mapping table below). No ancestry
   guard, no `_SCD_*` constant, no guard clause in `edge_rigidity_probe.py` and no pin commit is
   written. The legacy seal roles map to receipt fields as the vocabulary table states, and the seal
   record carries the mapping with its values.
4. **`ROADMAP.md`.** The round's own paragraph, required by §3.3 and §12, is allowed. §15.1 is read
   as prohibiting the correction of the 24.1B status discrepancy, and not the round's own paragraph.
   Both readings are recorded under X2.
5. **Execution paths.** The module `execution A`; `OIBridge.lean`, the census, `ROADMAP.md` and
   `README.md` `execution M`; the result note and `controls.py` inside the record directory, under
   its `record AM` entry. The census entry is written in every decided outcome.
6. **Independence.** No premise from `SUB-241B-OBS` or any 24.1B result; §3.2's refusal is adopted
   verbatim (Independence, below).
7. **Checkpoints and start state.** Every invariant this file asserts names its checkpoint
   (Invariants and their checkpoints, below). The start state is re-taken at `D` and its drift from
   `b78eac87` and `e21a42c6` recorded (Start state, below).

***

## Discrepancies and readings, recorded and not repaired

- **X1. Start-state drift.** Of the seventeen pins of §3.1 and §3.3, six moved between the legacy
  drafting snapshot `b78eac87` and the legacy base `e21a42c6`: `AGENTS.md`, `ROADMAP.md`,
  `README.md`, `edge_rigidity_probe.py`, `OIBridge.lean` and the census. Each of the six differs
  again at `D`; the other eleven are identical at all three commits. The freeze is not repaired; the
  start state is re-taken below.
- **X2. `ROADMAP.md`: §15.1 against §3.3 and §12.** §3.3 says the round writes `ROADMAP.md` "only by
  appending the frozen post-round sentence for the case reached", and §12 lists "the `ROADMAP` and
  `README` pointers the round's own section needs". §15.1 says "24.1C writes nothing to
  `verification/ROADMAP.md`, the `ROADMAP` sits in the read-only start-state table". *Reading A,
  adopted by owner decision 4:* §15.1 prohibits correcting the pre-existing 24.1B status
  discrepancy, which is another round's row, and does not prohibit the round's own paragraph; the
  paragraph is written and the discrepancy is left as it stands. *Reading B, recorded and not
  adopted:* §15.1 prohibits any write to `ROADMAP.md`, so §3.3's append and §12's pointer would be
  void. `controls.py` holds Reading A and its boundary: `ROADMAP.md` at `E` is `D`'s with the one
  frozen paragraph inserted and no other byte changed, so the 24.1B wording at `ROADMAP.md:64` and
  `:706` cannot change.
- **X3. §7's "nowhere else" against §3.3's appended sentence.** §7 says the frozen sentence "is
  written, verbatim, in the result note and nowhere else"; §3.3 appends "the frozen post-round
  sentence for the case reached" to `ROADMAP.md`. *Reading, adopted:* §3.3 is the specific provision
  for `ROADMAP.md`, so the sentence is written in the result note and in the `ROADMAP.md` paragraph,
  and nowhere else; the README paragraph, the census note and the module carry the outcome vector and
  not the sentence. `controls.py` checks each of the four.
- **X4. The `AGENTS.md` passages the legacy freeze quotes.** §0.2, §1, §1.1 and §3.2 quote
  `AGENTS.md:688–697`, `:775–777` and `:793–799` of blob `c51e4fb7`. None of those passages stands in
  `AGENTS.md` at `D` (blob `ca0d37ad`); they stand in the §A.37 record text,
  `AGENTS.md` at `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`, which `AGENTS.md:765–766` at `D` names.
  §3.2's invariant is adopted as the freeze's own text and does not rest on the `AGENTS.md` passage.
- **X5. The legacy seal state of §1.1.** The `_SGT_*` and `_WTS_*` constants no longer exist in the
  guard at `D`. The same six values stand as the legacy seal records `verification/seals/SGT.json`
  (blob `2ff4f68b`) and `verification/seals/WTS.json` (blob `27104c27`), kept by the release gate's
  `legacy-records` step. This round reads both and writes neither; `controls.py` checks their blobs
  and values against §1.1's table.
- **X6. `SC0`'s coordinates.** Every §2 passage stands at `D`, verbatim up to line wrapping. The two
  in `ROADMAP.md` other than the row moved: §2.2 from 516–522 to 679–685, and §2.3 from 533–544 to
  696–707. The passage table below records each.
- **X7. 24.1B's status on the record.** At `D`, `ROADMAP.md:64` and `:706` say 24.1B is "named and not
  begun", while 24.1B's control plane is merged (blob `f614b666`) and closed by `legacy-records` as
  never executed. Per §15.1 and owner decision 4 this round does not correct it.
- **X8. The `SC5` rule writes no sentence for five cells.** §5 says `SC5` is "exactly one" of three
  outcomes and §7 freezes one sentence for each. With `SC4(a)` refuted, no sentence is true: the
  `SC5-UNDECIDED` sentence opens by asserting `SC4(a)` "at the strength recorded". With `SC4(a)`
  UNDECIDED and `SC4(b)` decided either way, the `SC5-UNDECIDED` sentence says the converse is
  UNDECIDED, which is false, and the other two need `SC4(a)` positive. **The rule this file adds, and
  which is not the legacy freeze's:** in those five cells the round writes no post-round sentence,
  records the labels it reached in the result note with the statement frozen below, and halts under
  the specification's `S12`. A refuted `SC4(a)` is §5's falsifier for `SC4`, and is reported in the
  result note "as found". This rule is flagged for the owner's review at `F`.
- **X9. The kernel statement pins.** The legacy freeze states `SC4` in prose and names the Lean form
  only in its headings ("`BlockSpanning U → HiddenCommutantTrivial U`" and its converse). A native
  freeze must fix the statements its controls compare before `F`. The statements frozen below
  transcribe §5's text over the merged definitions, consumed as merged (§2.8): `SC4(a)` and `SC4(b)`
  as the two implications under the merged modules' section variables, which is "for every finite
  `V`, `H`"; `SC4(c)` at `φ̂_C` pinned by the equation `U = Equiv.Perm.permMatrix ℂ φC` with `φC` the
  merged local notation, as `ST3_pairC` pins it; the refutations as exhibited witnesses with both
  conjuncts. That is a reading of prose, recorded as one. Whether each frozen text elaborates at the
  pin is owed as design evidence before `F` (Pre-`F` evidence, below).
- **X10. `SC4(d)`, "on a carrier".** §5 asks for "one `U` with `BlockSpanning U` and one `U` with
  `¬ BlockSpanning U`" "on a carrier with at least two visible and at least two hidden elements". §6's
  prediction expects the first from Pair C, on `ℤ₂ × ℤ₃`, and the second from Pair A, on `ℤ₂ × ℤ₂`.
  *Reading, adopted:* each witness lies on its own carrier meeting the size bound. The freeze's
  non-degeneracy condition is the size bound and nothing more, and no other is added; the result note
  names each witness.
- **X11. "One ledger paragraph appended" to `README.md`.** At the legacy base the round ledger was the
  run of paragraphs that ended the file. At `D` it ends before `## Seal infrastructure round SI-1 —
  the shadow validator and the equivalence census`. *Reading, adopted:* the paragraph is inserted
  there, at the end of the ledger.
- **X12. §10's slot 2 has no name.** §10 names slot 1 (`hiddenCommutant`) and describes slot 2 as "a
  named witness datum for `SC4(d)`". `controls.py` admits at most one definition besides
  `hiddenCommutant`: a matrix on a carrier `Fin a × Fin b` with `a, b ≥ 2`, which an `SC4(d)` witness
  theorem uses.

***

## Start state at `D`

§3.1's twelve read-only pins and §3.3's five written files, with their blobs at the legacy drafting
snapshot, at the legacy base and at `D`. `controls.py start-state <D>` prints this table and fails
on any difference.

| path | blob at `b78eac87` | blob at `e21a42c6` | blob at `D` |
| --- | --- | --- | --- |
| `AGENTS.md` | `c51e4fb7` | `3e3f0045` | `ca0d37ad` |
| `verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md` | `b8168df9` | `b8168df9` | `b8168df9` |
| `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md` | `b5822feb` | `b5822feb` | `b5822feb` |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md` | `98cfcfdc` | `98cfcfdc` | `98cfcfdc` |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md` | `124a02c9` | `124a02c9` | `124a02c9` |
| `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md` | `f614b666` | `f614b666` | `f614b666` |
| `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean` | `5ee55b5c` | `5ee55b5c` | `5ee55b5c` |
| `verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean` | `ea8e9692` | `ea8e9692` | `ea8e9692` |
| `verification/lean-mathlib/lean-toolchain` | `025e5954` | `025e5954` | `025e5954` |
| `verification/lean-mathlib/lakefile.toml` | `5935a5ae` | `5935a5ae` | `5935a5ae` |
| `verification/audits/foundations/act12-scope-propagation-audit.md` | `1d471edd` | `1d471edd` | `1d471edd` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md` | `6428e0ac` | `6428e0ac` | `6428e0ac` |
| `verification/ROADMAP.md` | `5ee35552` | `4eb3a650` | `69bedfe9` |
| `verification/README.md` | `d25eb2d4` | `9983b078` | `d3e89853` |
| `verification/lean/edge_rigidity_probe.py` | `6e334e83` | `75890ec6` | `36dfadab` |
| `verification/lean-mathlib/OIBridge.lean` | `0bff51eb` | `81814f25` | `179344d8` |
| `verification/lean-manuscript-census.json` | `3e968e6c` | `86bda14f` | `89a44bbc` |

Also read at `D`, and never written:

| path | blob at `D` |
| --- | --- |
| `verification/programmes/substratum/lemma-24-1c-spanning-class-decision/preregistration.md` | `b6f383741e84a1c53a599de349922f4d525e1349` |
| `verification/seals/SGT.json` | `2ff4f68bd5e4283cb67ca53b20b745a998486252` |
| `verification/seals/WTS.json` | `27104c27c5cade441bc6749cf8c862a2da8b5610` |
| `verification/infrastructure/legacy-records.json` | `9e48bd31797e1673f03807e699a10ae4a0b960c7` |

The Mathlib pin is `rev = "v4.33.0"` in `lakefile.toml` (blob `5935a5ae`, unchanged since the legacy
drafting snapshot), with toolchain `leanprover/lean4:v4.33.0`. "Mathlib at the pin" in §5 is that tag.

**Free at `D`.** None of `SpanningClassReach`, `SUB-241C`, `round-sub-241c`, `v3-seals/SUB-241C`,
`SC4a_`, `SC4b_`, `SC4c_` or `SC4d_` occurs in the tree outside the legacy freeze, and none of the
record directory, the receipt, the seal record, the module or `verification/v3-seals/` exists.

**24.1B at `D`.** Neither `verification/programmes/substratum/lemma-24-1b-framework-data/result.md`
nor `verification/receipts/SUB-241B-OBS.json` exists. The first lies in a closed namespace and cannot
be added.

## `SC0`'s passages

Each §2 passage, located by its normalized text (blockquote markers removed, whitespace collapsed,
split at `[…]`), with its line range at `D` and in the blob the legacy freeze pinned.

| passage | file | lines at `D` | lines in the pinned blob |
| --- | --- | --- | --- |
| §2.1 | `verification/ROADMAP.md` | 64–64 | 64–64 |
| §2.2 | `verification/ROADMAP.md` | 679–685 | 516–522 |
| §2.3 | `verification/ROADMAP.md` | 696–707 | 533–544 |
| §2.4 | `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md` | 62–74 | 62–74 |
| §2.5 | `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md` | 229–231 | 229–231 |
| §2.6 | `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md` | 174–177; 182–183 | 174–177; 182–183 |
| §2.7 | `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md` | 399–408 | 399–408 |
| §2.8a | `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean` | 98–102 | 98–102 |
| §2.8b | `verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean` | 93–95; 101–103 | 93–95; 101–103 |

***

## Independence

No target of this round rests on a premise from `SUB-241B-OBS` or from any 24.1B result, in either
direction. What makes that measurable:

- **The evidence base is fixed before any sibling can enter it.** `F`'s tree is `D`'s outside this
  record directory, the execution is linear from `F`, and later history enters only by reconciliation
  after `E` (`S3`, `S9`). Every label, the result note and the surfaces are fixed at `E`.
- **No 24.1B result was present at `D`**, and so none at `F`: `controls.py` measures both paths named
  in the vocabulary table, and the result note carries the measured sentence.
- **The module** imports `OIBridge.WordTraceSufficiency` and Mathlib only, and contains none of the
  24.1B objects `H_obs`, `O_set`, `interleave` (§0.2), nor `familyAt` or `enlarge`.
- **The result note** quotes only the blobs of the start-state table and the legacy freeze, cites no
  path under `papers/` or `book/`, and carries the sentence "No manuscript file was read and no 24.1B
  object was consulted."

***

## The kernel statement pins, FROZEN

The module `verification/lean-mathlib/OIBridge/SpanningClassReach.lean` begins with the import
`import OIBridge.WordTraceSufficiency`, followed only by `import Mathlib.…` lines. Before its first
declaration it carries each of these exactly once:

```lean
namespace OIBridge
namespace SpanningClassReach
set_option autoImplicit false
open Matrix SemigroupTransfer WordTraceSufficiency
variable {V H : Type} [Fintype V] [DecidableEq V] [Fintype H] [DecidableEq H]
```

It ends with `end SpanningClassReach` and `end OIBridge`. The `variable` line is the merged modules'
and is the module's only one; there is no `include`, `omit`, `open … in`, `universe`,
`set_option autoImplicit` other than `false`, `axiom`, `instance`, `structure`, `class`,
`inductive`, `opaque`, `example`, `macro`, `syntax`, `notation` or `elab`. A `local notation` is
admitted only for the merged witness permutations, verbatim:

```lean
local notation "φA" => (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)))
local notation "φA'" => (Equiv.swap ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)))
local notation "φC" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) * Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)))
local notation "φC'" => (Equiv.swap ((0 : Fin 2), (2 : Fin 3)) ((1 : Fin 2), (0 : Fin 3)) * Equiv.swap ((1 : Fin 2), (1 : Fin 3)) ((1 : Fin 2), (2 : Fin 3)) * Equiv.swap ((0 : Fin 2), (0 : Fin 3)) ((0 : Fin 2), (1 : Fin 3)))
```

The labels, each a `theorem` whose statement up to `:=` is exactly the frozen text, whitespace
collapsed. `Fin a × Fin b` stands for numerals `a` and `b`: at least 1 for the two refutations, at
least 2 for `SC4(d)`.

```lean
theorem SC4a_spanning_imp_hct (U : Matrix (V × H) (V × H) ℂ) (hU : BlockSpanning U) : HiddenCommutantTrivial U :=
theorem SC4a_counterexample : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, BlockSpanning U ∧ ¬ HiddenCommutantTrivial U :=
theorem SC4b_hct_imp_spanning (U : Matrix (V × H) (V × H) ℂ) (hU : HiddenCommutantTrivial U) : BlockSpanning U :=
theorem SC4b_separating : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, HiddenCommutantTrivial U ∧ ¬ BlockSpanning U :=
theorem SC4c_pairC_spanning : ∃ U : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ, U = Equiv.Perm.permMatrix ℂ φC ∧ BlockSpanning U :=
theorem SC4c_pairC_not_spanning : ∃ U : Matrix (Fin 2 × Fin 3) (Fin 2 × Fin 3) ℂ, U = Equiv.Perm.permMatrix ℂ φC ∧ ¬ BlockSpanning U :=
theorem SC4d_spanning_witness : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, BlockSpanning U :=
theorem SC4d_nonspanning_witness : ∃ U : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ, ¬ BlockSpanning U :=
```

| target | positive label | negative label | UNDECIDED |
| --- | --- | --- | --- |
| `SC4(a)` | `SC4a_spanning_imp_hct` | `SC4a_counterexample`, §5's falsifier | neither |
| `SC4(b)` | `SC4b_hct_imp_spanning` | `SC4b_separating`, the exhibited `U` of `SC5-strict` | neither |
| `SC4(c)` | `SC4c_pairC_spanning` | `SC4c_pairC_not_spanning` | neither |
| `SC4(d)` | both `SC4d_spanning_witness` and `SC4d_nonspanning_witness` | none | otherwise |

A target carrying both labels fails. Any other theorem whose name begins `SC0`–`SC6` fails. Every
`theorem` and `lemma` has one `#print axioms OIBridge.SpanningClassReach.<name>` line and no other
declaration has one. The module contains none of `sorry`, `admit`, `native_decide`,
`Lean.ofReduceBool`, `implemented_by`, `extern`, `unsafe`, `HiddenConjugate`, `WordTracesEqual`,
`transferMap`, any identifier beginning `WT2`, `familyAt`, `enlarge`, `H_obs`, `O_set` or
`interleave`: `WT2` is not reopened, `ST4`'s enlargement is not consumed, and no 24.1B object is
read.

**§5's side conditions, measured.** `SC4(c)` "by direct computation and not by `SC4(b)`": no theorem
or definition the `SC4(c)` label's proof reaches inside the module is an `SC4(b)` label. `SC4(d)`'s
Pair A route: when the non-spanning witness's proof reaches `SC4a_spanning_imp_hct`, the result note
says that it "is derived through `SC4(a)`" and names both steps; when it does not, the note does not
say so.

**The definition budget, §10.** At most two definitions. Slot 1, if it fires, is
`def hiddenCommutant (U : Matrix (V × H) (V × H) ℂ) : Submodule ℂ (Matrix H H ℂ) :=` (optionally
`noncomputable` or attributed). Slot 2, if it fires, is one
`def <name> : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ :=` with `a, b ≥ 2`, reached by an `SC4(d)`
witness theorem. The labels keep their frozen form whichever slot fires.

## The decision, computed from the labels

`SC5` is §5's rule, applied to the labels at `E`:

| `SC4(a)` | `SC4(b)` | `SC5` |
| --- | --- | --- |
| positive | positive | `SC5-coincide` |
| positive | refuted | `SC5-strict` |
| positive | UNDECIDED | `SC5-UNDECIDED` |
| UNDECIDED | UNDECIDED | `SC5-UNDECIDED` |
| refuted | any | no frozen sentence: the round halts (X8) |
| UNDECIDED | positive or refuted | no frozen sentence: the round halts (X8) |

`SC4(c)` enters no cell, which is §5's gate. The outcome vector is generated from the labels,
never written by hand: `Outcome: ` followed by one entry per target and the `SC5` token, joined by
` · `, ending with a full stop. The entries are:

| target | positive | negative | UNDECIDED |
| --- | --- | --- | --- |
| `SC4(a)` | `` `SC4(a)` established `` | `` `SC4(a)` refuted `` | `` `SC4(a)` UNDECIDED `` |
| `SC4(b)` | `` `SC4(b)` established `` | `` `SC4(b)` refuted `` | `` `SC4(b)` UNDECIDED `` |
| `SC4(c)` | `` `SC4(c)` `φ̂_C` spanning `` | `` `SC4(c)` `φ̂_C` not spanning `` | `` `SC4(c)` UNDECIDED `` |
| `SC4(d)` | `` `SC4(d)` both witnesses exhibited `` | — | `` `SC4(d)` UNDECIDED `` |

and the `SC5` token in backticks, or `no frozen `SC5` outcome` in a halting cell.

In a halting cell the result note carries the vector and the statement "No frozen post-round sentence
applies to this outcome; the round halts under the specification's `S12`." and none of the three
sentences; the execution paths are withdrawn by `W`.

## The surfaces, FROZEN

Each template is filled by replacing `{VECTOR}` with the outcome vector and `{SENTENCE}` with the
frozen sentence for the `SC5` outcome reached. `controls.py` compares each inserted paragraph with
its template after collapsing whitespace, so line wrapping is free and nothing else is.

**`ROADMAP.md`.** Inserted as its own paragraph directly after the 24.1A paragraph of the P1 section
on Lemma 24.1, which ends "and 24.1B is named and not begun. No manuscript edit.", and before "This
is the row to watch":

```text
**Executed, 24.1C** — `programmes/substratum/round-sub-241c-spanning-v3/`, the native sealing round
`SUB-241C-SPAN` (receipt `receipts/SUB-241C-SPAN.json`, seal record `v3-seals/SUB-241C-SPAN.json`;
`OIBridge/SpanningClassReach.lean`), taking up the legacy freeze
`programmes/substratum/lemma-24-1c-spanning-class-decision/` (preregistration blob
`b6f383741e84a1c53a599de349922f4d525e1349`, merged by PR #643 as `e21a42c`, never executed).
{VECTOR} The frozen sentence for that outcome: {SENTENCE}
```

**`README.md`.** Inserted as its own paragraph directly before the line
`## Seal infrastructure round SI-1 — the shadow validator and the equivalence census`:

```text
The reconstruction programme's Lemma 24.1C round, the spanning-class decision, is the native sealing
round `SUB-241C-SPAN` (`programmes/substratum/round-sub-241c-spanning-v3/`, receipt
`receipts/SUB-241C-SPAN.json`, seal record `v3-seals/SUB-241C-SPAN.json`). It takes up the legacy
freeze `programmes/substratum/lemma-24-1c-spanning-class-decision/` (preregistration blob
`b6f383741e84a1c53a599de349922f4d525e1349`, merged by PR #643 as `e21a42c`, never executed).
`OIBridge/SpanningClassReach.lean` places `BlockSpanning`, the class on which `WT3_spanning_iff`
lands, against `HiddenCommutantTrivial`. {VECTOR} The frozen sentence for that outcome is stated in
the result note and in the P1 section of `ROADMAP.md`. The P1 label stays OPEN, no manuscript is
read or edited, and no 24.1B object is consulted. The round adds no guard clause: its content checks
are the frozen `controls.py` in its record directory, and its lifecycle is its receipt.
```

**`OIBridge.lean`.** `import OIBridge.SpanningClassReach` inserted on the line after
`import OIBridge.WordTraceSufficiency`, and no other change.

**The census.** `verification/lean-manuscript-census.json` is `D`'s with one family appended last,
every other key and family unchanged:

- `name`: "the spanning-class decision: BlockSpanning against HiddenCommutantTrivial (round SUB-241C-SPAN, substratum Lemma 24.1C)"
- `modules`: `["SpanningClassReach"]`; `status`: `"kernel-only"`; `manuscript`: `[]`
- `note`: "Substratum Lemma 24.1C, the native sealing round SUB-241C-SPAN under AGENTS.md §A.39, taking up the legacy freeze programmes/substratum/lemma-24-1c-spanning-class-decision/preregistration.md (blob b6f383741e84a1c53a599de349922f4d525e1349, merged by PR #643, never executed). {VECTOR} Kernel-only: no manuscript anchor, and no manuscript is read or edited; the P1 label stays OPEN. Record: verification/programmes/substratum/round-sub-241c-spanning-v3/."

The registry contract of §A.35 is met: the family is new, `kernel-only` and names no anchor, and no
theorem in an existing module is strengthened.

## The result note, FROZEN requirements

`result.md` in the record directory. Beyond §13, `controls.py check` requires:

- each of the headings `## Outcome`, `## SC0`, `## SC1`, `## SC2`, `## SC3`, `## SC4(a)`, `## SC4(b)`, `## SC4(b) bounded search`, `## SC4(c)`, `## SC4(d)`, `## SC5`, `## SC6`, `## Axiom table`, `## Definition budget`, `## Discrepancies`, `## Independence`, exactly once, as a line;
- the outcome vector exactly once, and exactly one line beginning `Outcome: `;
- the frozen sentence for the `SC5` outcome exactly once, as a blockquote, and neither other
  sentence; or, in a halting cell, the halting statement above;
- "No manuscript file was read and no 24.1B object was consulted."
- the measured 24.1B sentence, one of "No 24.1B result note was present at `F`, and none was
  consumed." and "A 24.1B result note was present at `F` and was not read, cited or consumed.";
- "`SC0`–`SC3` and `SC6` are type P, carried by quotation and by recorded silence; `SC4` is at
  evidence level 2.";
- one of "Slot 1 (`hiddenCommutant`): fired." and "Slot 1 (`hiddenCommutant`): unused.", and one of
  "Slot 2 (a named witness datum for `SC4(d)`): fired." and "Slot 2 (a named witness datum for
  `SC4(d)`): unused.", each matching the module;
- under `## SC0`, one row `| §<id> | `<path>` | <lines at F> |` per passage, equal to the
  coordinates `controls.py` measures at `F`;
- under `## SC4(b) bounded search`, lines beginning `Search terms:`, `Trees searched:` and
  `Result:`, recording the search §5 requires whatever the attempt yields;
- under `## SC5`, on `SC5-UNDECIDED`, a line beginning `Obstruction:`; if it names the double
  commutant statement, it carries §7's terms: "`wordSpan U` is a unital `*`-closed subalgebra of
  `Matrix H H ℂ`", "`HiddenCommutantTrivial U` says its commutant is the scalars", "the conclusion
  `wordSpan U = ⊤` is the double commutant theorem in spatial finite-dimensional form" and "the named
  bounded search found";
- under `## Axiom table`, one row `` | `<name>` | `[<axioms>]` | `` per theorem of the module, name
  for name, each list within `propext`, `Classical.choice` and `Quot.sound`;
- every quotation cited as `` `<path>:<a>–<b>`, blob `<sha>`: ``, followed by a blank line and a
  blockquote, equal line for line to lines `a`–`b` of that blob, and the blob one of the start-state
  table's blobs at `D` or the legacy freeze's;
- no path under `papers/` or `book/`.

**Forbidden phrases**, checked in the result note and in each inserted paragraph, outside
blockquotes, backtick spans and quotation marks, case-insensitively: "lemma 24.1 is repaired",
"lemma 24.1 is false", "theorem 24 is false", "theorem 24 is repaired", "completeness holds",
"completeness fails", "the generators are complete", "the generators are incomplete", "the
manuscripts' route is restored", "the transfer is refuted", "the programme should next", "the
selection principle is"; and, at the start of a sentence, "the framework supplies" and "the framework
does not supply". They are §8's, §0.2's, §5's `SC1` and `SC6`, and §8's selection-principle sentence.

***

## `R7-SCD`, carried by `controls.py`

`R7-SCD` was never written: the legacy freeze reserved the tag (§1, and §15 item 2) and left its clause to the
execution. What it was to check is read from the freeze and from the shape of its merged siblings
`R7-SGT` and `R7-WTS`. Each content check maps to `controls.py`; each chronology check is replaced by
the specification.

| `R7-SCD`'s check | `controls.py` | code on failure |
| --- | --- | --- |
| the preregistration "by path and content" (§11 item 2, §15) | `freeze`: the legacy blob at its path, unchanged at every checked commit; this file's blob unchanged from `F` | `start:legacy-freeze`, `legacy:freeze-changed`, `check:preregistration-changed` |
| the start-state blobs (§3.1, §3.3) | `start-state`: every pin at `D` with its drift; `check`: the read-only pins unchanged | `start:blob:<path>`, `read-only:written:<path>` |
| the pinned passages (§2, `SC0`) | `start-state`: each passage and its coordinates at `D` and in the pinned blob; `check`: the result note's `SC0` rows equal the coordinates at `F` | `start:coordinate:<id>`, `sc0:passage-absent:<id>`, `note:sc0-row` |
| the kernel statements, in terms | the frozen header and label texts; one label per target | `module:label-statement:<name>`, `module:header:<item>`, `module:both-labels:<t>`, `module:stray-label:<name>` |
| no unproved declaration, no kernel bypass | the forbidden identifiers | `module:forbidden-token:<t>` |
| the definition budget (§10) | at most the two slots, in their forms; the note's slot lines match | `module:budget`, `note:budget-line` |
| the axiom table (§10, evidence level 2) | a print per theorem; the note's table name for name, within the three axioms; `axioms` mode against the build log at `E` | `module:prints`, `note:axiom-table`, `axioms:table-differs-from-log` |
| the frozen sentence, and only it (§7) | the one sentence for the `SC5` outcome, in the note and the `ROADMAP.md` paragraph only | `note:sentence`, `note:other-sentence`, `roadmap:sentence`, `sentence-outside-note-and-roadmap` |
| the `SC5` gate (§5) | `SC5` computed from `SC4(a)` and `SC4(b)` only; the vector generated | `note:vector` |
| `SC4(c)` not by `SC4(b)`; Pair A route stated | the dependency closure inside the module | `module:sc4c-through-sc4b`, `note:pair-a-route` |
| the non-licences (§8, §0.2, §5) | the forbidden phrases | `note:forbidden:<phrase>`, `<surface>:forbidden:<phrase>` |
| no `WT2`, no enlargement, no 24.1B object (§3.4, §8, §0.2) | the forbidden identifiers; the import set | `module:forbidden-token:<t>`, `module:import` |
| no manuscript read (§0.2, §3.1, H2) | no `papers/` or `book/` path in the note; the note's statement | `note:manuscript-path`, `note:no-manuscript` |
| 24.1B's result present or not, never consumed (§3.2, §13) | measured at `F`; the note's sentence matches | `note:24.1b-presence` |
| the bounded search recorded (`SC4(b)`) | the three lines | `note:bounded-search` |
| the obstruction in §7's terms | the four terms | `note:obstruction`, `note:obstruction-terms` |
| the quotations verbatim (§4 item 2) | each cited quotation against its blob | `note:quote` |
| the `P1` label does not move (§8, H12) | `ROADMAP.md` at `E` is `D`'s with the one paragraph inserted | `roadmap:insertion` |
| the README pointer | `README.md` at `E` is `D`'s with the one paragraph inserted | `readme:insertion` |
| the census entry, `kernel-only`, every outcome (§15 item 7) | `D`'s registry with the frozen family appended | `census:entry` |
| the one import line | `OIBridge.lean` at `E` is `D`'s with the line inserted | `bridge:import` |
| the sibling seals read, never written (§1.1, H10) | the two legacy seal records' blobs and values | `seals:legacy-seal-state` |
| only `R7-SCD` added to the guard file | the guard file unchanged | `guard:changed` |
| the execution's produce-list (§12) | the paths of `delta(D, E)` are exactly the frozen eight | `paths:extra`, `paths:missing` |
| ancestry: base an ancestor of the head, every commit of `H ^B` a descendant | **not carried.** `S3` (linear from `F`) and T1–T7 of `tools/v3_verifier.py --verify-round Q` | — |
| archive mode: `_SCD_SEALED_HEAD`, `_SCD_MERGE` set by `P` | **not carried.** The receipt's `e` and `landing.object`, and the seal record `Q` adds | — |

## The seal record and the receipt

The seal record is the round's one `G12` record. V3 reads no field of it; its format is this round's
own, and `controls.py seal-record <F> <E> <Λ>` renders it, byte for byte, as indented JSON with these
fields: `schema` `"sub-241c-span-seal"`, `version` `1`, `round`; `legacy`, naming the freeze, its blob,
its merge `e21a42c6…` and the reserved tag `R7-SCD`; `roles`, the three rows below with their values;
`pins`, the blobs of the preregistration at `F` and of `controls.py`, the module and the result note
at `E`; and `outcome`, the vector.

| legacy role | receipt field | value |
| --- | --- | --- |
| `_SCD_BASE` | `f` | `F` |
| `_SCD_SEALED_HEAD` | `e` | `E` |
| `_SCD_MERGE` | `landing.object` | `Λ` |

`controls.py receipt <Q>` re-renders it from the receipt at `Q` and requires the file at `Q`, the
rendering and the receipt's `seal.records[0].blob` to agree, `Q`'s one parent to be `Λ`, and the
record directory at `Q` to equal `E`'s.

**Building again after a receipt commit.** If the chosen base advances after a receipt commit is
built, the round builds again as the specification's `G11` admits: either a new reconciliation from
`E`, or one whose second parent is the receipt commit kept, which then removes the seal record so
that the new receipt commit can add it again under `record A`. The conformance vector
`k4-admit-sealing-superseded-receipt-commit` is the second form. A seal record is never modified in
place.

***

## `controls.py`, FROZEN

`verification/programmes/substratum/round-sub-241c-spanning-v3/controls.py`, written before `F` and
added by the first execution commit with exactly this blob:

Frozen blob of `controls.py`: `bcdf66701b3383602477cd855674451db7f5102a`.

It imports nothing from the repository and changes nothing. It reads git objects by full object id
through `git cat-file`, `git ls-tree`, `git diff-tree` and `git rev-list --parents` with a fixed
environment, and reads no ref, network, clock or working-tree file. It fails closed: anything
unexpected prints `FAIL` with a code and exits 1. Its entry points:

- `--self-test`, hermetic: synthetic executions over all 54 outcome rows (`SC4(a)`, `SC4(b)` and
  `SC4(c)` in three states, `SC4(d)` in two), each under several budget and route options, must hold;
  then the mutation controls, each of which must fail with its named code;
- `start-state <D>`: the start state, the passages, the frozen sentences against the legacy blob,
  the free names and paths, and 24.1B's absence;
- `freeze <F>`: `delta(D, F)` touches only the control plane, and this file at `F` carries the two
  blocks, every frozen text and template, the start-state and passage rows, the controls blob line,
  and each legacy quotation verbatim, the quoted ranges being exactly the fifteen adopted;
- `check <C> --f <F> [--stage]`: everything above about the module, the labels and the vector,
  and, without `--stage`, the result note, the surfaces and the exact path set;
- `seal-record <F> <E> <Λ>` and `receipt <Q>`, as above;
- `axioms <C> <log>`: the note's axiom table against the build log's `#print axioms` reports.

Run at `D`, `--self-test` prints:

```text
controls: 252 synthetic executions over 54 outcome rows hold as frozen, 83 of 83 mutation controls fail as required
controls: self-test OK
```

***

## The execution

**Before any commit**, the executor writes the frozen `controls.py` from its blob and runs it:
`freeze F` and `start-state D` must print OK (`C1`). Then linear commits from `F`, each with one
parent:

1. **Stage 1.** Adds `controls.py` at its frozen blob; adds the module with the frozen header, the
   merged notations it needs and no label; inserts the import line. `check <S1> --f F --stage` OK.
2. **Stage 2.** `SC4(a)`: `SC4a_spanning_imp_hct` or `SC4a_counterexample`, or neither.
3. **Stage 3.** `SC4(c)` and `SC4(d)`, by direct computation.
4. **Stage 4.** `SC4(b)`: the attempt, and the named bounded search, whatever the attempt yields.
5. **Stage 5.** The census family, the `ROADMAP.md` paragraph and the `README.md` paragraph for the
   outcome reached (none in a halting cell).
6. **The result note** `result.md`, whose commit is `E` (or, in a halting cell, the last execution
   commit before `W`).

`tools/legacy_records_check.py` runs at each stage commit, beside `controls.py check --stage`.

Lean runs in CI only (`AGENTS.md` §A.40). Each stage is pushed so the pull request's run builds the
module; a stage whose build fails is followed by a fixing commit, never rewritten. Every label is
read from the module at `E`. `E` is attested by an exact-head `workflow_dispatch` run on `E`, which
the owner authorizes.

## Invariants and their checkpoints

| invariant | checkpoint |
| --- | --- |
| the start state is the one recorded here | `C0`: `controls.py start-state D` OK, at drafting and again at `C1` |
| execution begins from the frozen control plane | `C1`: `controls.py freeze F` OK before the first execution commit |
| the controls are the frozen ones | `C2`: `controls.py`'s blob at stage 1 and at `E` is the frozen blob (checked by `check`); `--self-test` OK at `E` |
| the module's header, labels, budget and forbidden identifiers are as frozen | `C3`: `check <S> --f F --stage` at each stage commit; `C4` at `E` |
| the result note, the vector, the sentence, the surfaces and the path set are as frozen | `C4`: `check E --f F` OK |
| every frozen statement elaborates as frozen | before `F`: the elaboration run owed below; at `E`: `C5`, since each label compiles under its frozen statement |
| every result is kernel-checked within the three axioms | `C5`: the exact-head run at `E`, with the `Mathlib bridge` build green and the release gate's `lean-axioms` step passing; `C6`: `controls.py axioms E <that job's log>` OK |
| the census stays complete | `C5`: the release gate's `lean-manuscript` step at `E` |
| the retained guard is unchanged in verdict | `C5`: the guard at `E` reports every check `PASS`, as at `D` |
| no premise from 24.1B or `SUB-241B-OBS` | `C0` (absent at `D`); `C4` (identifiers, imports, the note's sentences) |
| the legacy freeze, the legacy seal records and the legacy manifest are untouched | `C4`; `tools/legacy_records_check.py` at each stage commit and at `Q` (`C8`) |
| the seal record is the frozen mapping with its values | `C7`: `controls.py receipt Q` OK |
| the round holds | `C8`: `tools/v3_verifier.py --verify-round Q` prints `VERDICT  HOLDS`; `--receipts Q` holds on every receipt |

## Pre-`F` evidence

**Done, locally, at drafting.** `controls.py --self-test` and `start-state D` as printed above.
`freeze` on a scratch commit carrying this file. A lifecycle rehearsal in scratch objects that were
never pushed: for one decided outcome and for one halting cell, a `D → F → E → Λ → Q` chain (or
`F → E′ → W → Λ → Q`) whose execution carries `controls.py` at its frozen blob, a synthetic module
with the frozen statements (never compiled), the surfaces and a result note; the receipt built by
`tools/v3_receipt.py` with placeholder attestation records and the seal record rendered by
`controls.py`. The results are recorded on the pull request, not here.

**Owed before `F`.** First, `controls.py`'s source at the frozen blob, published on a branch linked
from the pull request, so that the blob exists in the repository for `C1` and reviewers read the
exact file this freeze pins; it cannot lie on the round's branch before `F`, since `delta(D, F)` may
touch only the preregistration and `amendments/` (T1). Second, an elaboration run of the frozen header and the eight label statements at the
pin: a disposable branch from `D` carrying a module with each frozen statement under `#check` (or
proved by `sorry` in a file never landed), dispatched once with the owner's authorization, the run
green with exactly eight elaborated statements, and a countercontrol with one statement deliberately
ill-typed, red at its own line. Until that run exists the X9 transcription is unchecked, and a frozen
statement that fails to elaborate after `F` is a freeze failure under the status rule.

## The status rule

The labels are the measurements, read from the module at `E`. If `C1` fails, no execution commit is
made, and the round halts under `S12` with the record-only child of `F`.

- **A proof-implementation failure with the frozen statement unchanged** is repaired by later linear
  commits before `E`, never by rewriting one.
- **A target that cannot be decided** is reported UNDECIDED; that is a measurement.
- **A freeze failure** halts the round under `S12`: a frozen statement that is ill-typed or cannot be
  stated under the frozen header; a halting cell of the decision table (X8); a start-state check that
  fails at `C1`. The result note names it, and a successor round re-freezes.
- **A round that cannot otherwise reach a green `E`** halts under `S12` and records why.

## Non-doings

This round does not edit the legacy freeze or any other closed record; does not write a guard
clause, a `_SCD_*` constant or a pin commit; does not read or edit a manuscript; does not read,
cite or consume `SUB-241B-OBS` or any 24.1B result; does not correct the 24.1B status wording; does
not reopen `WT2`; does not move the `P1` label; and recommends no continuation. Consistency axis
only: correctness bands unchanged.
