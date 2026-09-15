# Reconstruction — Lemma 24.1C, the spanning-class decision: is the class `WT3` landed on the class the manuscripts' own route assumes? CONTROL PLANE

Owner-called. This file is the whole of the round's control plane and is merged **alone**, before
any execution object exists. It takes up one of the two live continuations of the `P1` row and
scopes the other out in terms.

**Blob identity is authoritative.** The execution guard pins this file by **path and content**, so
the directory name and the file name below are load-bearing and are settled before this merges.

---

## 0. The fork, taken explicitly

The `P1` row leaves two continuations live. This round is **one of them and not the other**, and
the choice is recorded here with its reason rather than left to the execution.

| continuation | what it asks | this round |
| --- | --- | --- |
| **24.1B — framework data** | does what Theorem 24's observables-preserving hypothesis fixes include every block-word trace `ST5` quantifies over? | **SCOPED OUT.** Frozen elsewhere; see §0.2 |
| **the spanning-class decision** | is `BlockSpanning` — the class on which `WT3_spanning_iff` lands — the same class as `HiddenCommutantTrivial`, the hypothesis the manuscripts' own route assumes, a strict strengthening of it, or neither? | **THIS ROUND** |

### 0.1 Why this round is the spanning-class decision

24.1A landed a biconditional on the class `BlockSpanning`, and named the class by a **definition of
its own** — `wordSpan U = ⊤` — rather than by the predicate the manuscripts' route runs on. The
merged result says so in terms, at `lemma-24-1a-word-trace-sufficiency/result.md:148–149`:

> `BlockSpanning U` is `wordSpan U = ⊤` (budget slot 4, fired), spanning and never
> `HiddenCommutantTrivial`.

That sentence records which predicate was **chosen as the definition**. It does not record, and no
merged artifact on this record records, **how the two classes stand to each other**. Until that is
settled, the reach of 24.1A's positive result is not known: a biconditional on a class nobody has
placed is a theorem whose scope is open. Placing it is a bounded question about finite matrices,
and it is the question this round asks.

It is also the question that orders the rest of the row. If the two classes coincide, then
`ST3`'s refuted reading and `WT3`'s established biconditional run on **one** class, and the
outstanding question about the obligation is the one 24.1B asks. If the spanning class is a strict
strengthening, then `WT3` reaches a class narrower than the route's own hypothesis, and `WT2` in
general is the outstanding question. **This round does not decide which of those the programme
should pursue.** It establishes the fact the ordering turns on, and records what further evidence
each branch would need.

### 0.2 Why 24.1B is scoped out, and how

24.1B is not a continuation this round may take, because **24.1B's freeze already exists, is
merged, and is immutable.** At this freeze's base the file
`verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md` is present at
blob `f614b666ad9098f866969c4c524e47f504e5d71c`, and there is **no** `result.md` beside it on a
bounded search of that directory at the base. 24.1B's control plane is merged and its execution has
not landed.

Under `§A.37` that settles it without argument:

> Amendment happens before the merge and only then: once merged the preregistration is
> **immutable**, and an execution that diverges from it **records the discrepancy** rather than
> repairing the freeze.
> — `AGENTS.md:688–691`

So 24.1B's targets, objects, predictions, gates and post-round sentences are fixed by that file and
by no other. This round cannot add to them, cannot restate them, and cannot pre-empt them. The one
thing it may do with 24.1B is **read its freeze as a pinned object**, which is what the start-state
table below does.

**Concretely scoped out of this round, and named so the execution can check itself:**

- 24.1B's four frozen objects — `H_obs`, `O_set`, `Φ-family`, `interleave` — are **not redefined,
  not restated, and not consulted**. No target of this round mentions them and no determination
  rests on one.
- **The manuscripts are not read as evidence.** `papers/` and `book/` appear nowhere in this
  round's start-state table, are consumed by no target, and are written by nothing. What Theorem
  24's hypothesis fixes is 24.1B's whole content and is untouched here.
- 24.1B's targets `WD0`–`WD4`, its partition-quantifier subtargets `WD1-q` and `WD2-q`, and its
  gate on `WD3-no` are **not executed, not anticipated, and not answered**.
- No sentence of this round's result may begin "the framework supplies" or "the framework does not
  supply".

**If 24.1B's result note appears at this round's mandated base**, because 24.1B's execution lands
first, the anti-contamination invariant in §3.2 governs: it is not consumed. This round's
determinations are the same whichever of the two executes first, and that independence is a
property the execution checks and reports.

### 0.3 The failure mode this round is built against

A round that straddled both would read 24.1B's manuscript question **and** the spanning-class
matrix question, and would then be free to move either answer to fit the other — a freeze whose
scope is settled after the outcome is known is not a freeze. It is named as hazard H2 in §9 and is
checked for in the final report.

---

## 1. The round's shape, declared in `§A.37`'s terms

**This is a SEALING round.** Under `§A.37` a sealing round is one

> whose preregistration prospectively owns seal state: either it creates new seal and pin state, or
> it explicitly takes ownership of changing existing seal state
> — `AGENTS.md:775–777`

This freeze **creates new seal state**. The execution writes one new Lean module,
`verification/lean-mathlib/OIBridge/SpanningClassReach.lean`, with its own guard clause in
`verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-SCD`**, and that clause
carries three archive-mode constants which this round owns:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_SCD_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_SCD_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_SCD_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

**The landing shape is therefore `E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only
commit that sets `_SCD_SEALED_HEAD` to `E` and `_SCD_MERGE` to `L`, moving the `R7-SCD` clause from
execution mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the
landing, because `git rev-list HEAD ^_SCD_BASE` at `L` reaches the sibling rounds merged into main
since this freeze, which do not descend from the base.

### 1.1 Every seal constant this round does NOT own

The two sibling seals in the `P1` lane are **read and never written**:

| constant | value at this base | owner |
| --- | --- | --- |
| `_SGT_BASE` | `c46e1606d4cafe2720afd69dc06c667eb0f1acff` | the Lemma 24.1 semigroup-transfer round, guard `R7-SGT` |
| `_SGT_SEALED_HEAD` | `57103e9ddf430c538094fed48358c4d1b050ce4d` | as above |
| `_SGT_MERGE` | `11a8a59d22793a10182f853fe3c05edf5415d724` | as above |
| `_WTS_BASE` | `baadea2638019b335d96c892590491a6fb420936` | the Lemma 24.1A round, guard `R7-WTS` |
| `_WTS_SEALED_HEAD` | `c31fe45d28d6aa37782902f67aba404ef721a59e` | as above |
| `_WTS_MERGE` | `6a6f206f830f5b44e1b19a6912b823d545207126` | as above |

Both clauses stand in **archive mode** at this base, with their pins set. `§A.37` states the rule
this round obeys:

> **An archive seal belongs to the round that set it, and stays immutable afterwards.** A later
> round does not re-pin it, and does not acquire a pin commit merely by touching the guard file
> that carries it. An existing seal constant changes only in a round whose own preregistration says
> in advance that it changes it — and such a round is *sealing*, because it has taken ownership of
> that state prospectively rather than as a side effect of its diff.
> — `AGENTS.md:793–799`

This freeze says in advance that it changes **none** of them. The execution's diff against
`edge_rigidity_probe.py` **adds** the `R7-SCD` clause and changes nothing else in the file. The
same holds of every other seal constant in that file — `_CTI_*`, `_PQT_*`, `_TCF_*`, `_A6P_*`,
`_A6D_*`, `_A6I_*`, `_A12P_*`, `_HYA_*`, `_HYB_*`, `_PC4_*`, `_PC4S_*` — none of which this round
reads as evidence or writes at all.

24.1B reserves **no** guard tag and sets **no** seal constant, by its own declaration at
`lemma-24-1b-framework-data/preregistration.md:8–11`:

> **Unguarded round.** No new guard file is added by this round, and no existing guard is modified.
> The definition budget is zero and no Lean module is written, so no kernel object exists for an
> ancestry guard to order and no guard tag is reserved.

So there is no 24.1B seal for this round to collide with, in either direction.

---

## 2. Locating controls — the governing passages at the base, quoted with coordinates

Each is quoted here as it stands at this freeze's base and is re-verified by the execution against
the blob pinned in §3.1. These are the passages the round is answerable to.

### 2.1 The `P1` row, `verification/ROADMAP.md:64`, status cell

> **OPEN** — the semigroup-transfer route is refuted on the tested readings (`ST2`–`ST4`); the
> obligation itself is untouched; 24.1A: block-word trace equality is necessary and sufficient for
> hidden conjugation on the spanning class (`WT3_spanning_iff`), sufficiency on general pairs
> UNDECIDED at the unitary-implementation step, 24.1B named and not begun

**Two clauses of that cell are the whole of this round's warrant.** "the semigroup-transfer route
is refuted on the tested readings" and "the obligation itself is untouched" are **different
statements**, and the row states them side by side precisely so they are not read as one.

### 2.2 The `P1` section on the Lemma 24.1 round, `verification/ROADMAP.md:516–522`

> **The label stays OPEN**: a negative on the lemma's route is not an impossibility theorem for the
> obligation, Lemma 24.1 is not called false without qualification, `ST5`'s hypothesis is a
> candidate strengthened hypothesis and not a certified repair, and the four generators are not
> called incomplete — the round says nothing about (ii)/(iv). What the row now needs is stronger
> multi-time information or a different proof route. No manuscript edit; the propagation is a
> separate owner call.

### 2.3 The `P1` section on 24.1A, `verification/ROADMAP.md:533–544`

> The frozen sentence for that outcome: *On every finite carrier `V × H`, for pairs of dilation
> data whose visible blocks each span all of `M_m(ℂ)`, equality of all block-word traces is
> necessary and sufficient for hidden conjugation; on general pairs necessity holds and sufficiency
> is reached at the strength of `WT1` — the trace-preserving `*`-isomorphism of the word spans at
> level 2, its unitary implementation UNDECIDED. Whether the reconstruction framework supplies that
> data is round 24.1B and is OPEN. The P1 row stays OPEN.* The obstruction to `WT2` is the spatial
> structure theory of `*`-subalgebras of `M_m(ℂ)` — the decomposition adapted to the simple
> summands and the unitary equivalence of equal-multiplicity representations — carried by neither
> Mathlib at the pin nor the corpus. **The label stays OPEN**: Lemma 24.1 is not repaired, the four
> generators are neither called complete nor called incomplete, the manuscripts' route is not
> restored, and 24.1B is named and not begun. No manuscript edit.

### 2.4 24.1A's three boundaries, `lemma-24-1a-word-trace-sufficiency/result.md:62–74`

> ### Three boundaries, stated once and kept everywhere below
>
> 1. **Lemma 24.1 is not repaired.** A theorem about an invariant on finite matrices is not
>    completeness of `𝒢_sub`; whether the reconstruction framework supplies the block-word trace
>    data is round 24.1B, which is named here and not begun.
> 2. **The four gauge generators are neither called complete nor called incomplete.** Nothing here
>    is about generators (ii)/(iv), which have no meaning on a finite carrier, and nothing here
>    exhausts `𝒢_sub`.
> 3. **The manuscripts' route is not restored.** The semigroup-transfer route stays refuted on the
>    tested readings (`ST2`–`ST4`); a sufficiency theorem for a stronger hypothesis does not revive
>    the route from the weaker one. **No negative is reported**: no pair with equal word traces and
>    no hidden conjugation was found or sought, and none would be labelled without an append-only
>    amendment.

### 2.5 The route-versus-obligation clause, `lemma-24-1-semigroup-transfer/result.md:229–232`

> **This round does not prove that stronger data are necessary for completeness itself**:
> `ST2`–`ST4` show what the present route needs, not what every possible completeness proof needs.

### 2.6 `WT2`'s named obstruction, `lemma-24-1a-word-trace-sufficiency/result.md:174–190`

> **UNDECIDED, and the obstruction is named among the freeze's (a)–(f).** `WT1` supplies the input
> the general route needs — a trace-preserving `*`-isomorphism `φ : 𝒲(U) → 𝒲(U')` of unital
> `*`-subalgebras of `M_m(ℂ)` — and there the round stops. **The obstruction is (b) together with
> (e)** […] Mathlib at the pin carries Wedderburn–Artin in abstract form and Schur's lemma and
> carries none of (a)–(f); the corpus carries none; and none was built here

### 2.7 24.1B's charter, `lemma-24-1a-word-trace-sufficiency/preregistration.md:399–408`

> ## Round 24.1B, named and not begun
>
> 24.1B asks whether the reconstruction framework's data — what Theorem 24's
> "observables-preserving" hypothesis actually fixes — determine every block-word trace.
> `ST3`/`ST4` show the uniform-prior channel family alone does not; the interleaved balanced words
> are multi-time visible correlation data, and whether the framework's notion of observables
> includes them is a question about the manuscripts' definitions, not about matrices. This file
> names 24.1B, records that it is OPEN, and freezes nothing about it: no target, no prediction, no
> reading of the manuscripts. It cannot begin before 24.1A's execution has merged, and it needs its
> own control plane.

**That control plane exists and is merged.** See §0.2.

### 2.8 The two predicates, as the merged kernel defines them

From `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean:98–102`:

> /-- **Slot 2.** The operative cyclicity predicate: every hidden operator commuting with `U` is a
> scalar. -/
> def HiddenCommutantTrivial (U : Matrix (V × H) (V × H) ℂ) : Prop :=
>   ∀ Y : Matrix H H ℂ, ((1 : Matrix V V ℂ) ⊗ₖ Y) * U = U * ((1 : Matrix V V ℂ) ⊗ₖ Y) →
>     ∃ c : ℂ, Y = c • (1 : Matrix H H ℂ)

From `verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean:93–103`:

> /-- **Slot 2.** The word span `𝒲(U) = span_ℂ { wordEval U w : w }`, a subspace of `M_m(ℂ)`. -/
> @[reducible] def wordSpan (U : Matrix (V × H) (V × H) ℂ) : Submodule ℂ (Matrix H H ℂ) :=
>   Submodule.span ℂ (Set.range (wordEval U))
> […]
> /-- **Slot 4 (conditional, fired).** The spanning hypothesis: `𝒲(U) = M_m(ℂ)`. -/
> def BlockSpanning (U : Matrix (V × H) (V × H) ℂ) : Prop :=
>   wordSpan U = ⊤

**These two definitions are consumed exactly as merged.** Neither is restated under a new name,
neither is generalized, and neither is edited.

---

## 3. Start state

### 3.1 The start-state blob table

Pinned **by blob** at this freeze's base, `main` at
`b78eac870ba3ee9ef9e98659ac933bf97dc62226`. Blob identity is authoritative: the commit locates the
tree, the blob is what is compared. A file that moved is the same file; a file that was rewritten
is not.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md` | `b8168df9ed1acff21eb89e84487b43470124f845` |
| `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md` | `b5822febb2626af48c29f6198fd6d74637ef9896` |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/preregistration.md` | `98cfcfdc0e74ffe0186c502517a842bfeb25d351` |
| `verification/programmes/substratum/lemma-24-1a-word-trace-sufficiency/result.md` | `124a02c9d2b17c0cf280f15a00ab269f68e33a24` |
| `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md` | `f614b666ad9098f866969c4c524e47f504e5d71c` |
| `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean` | `5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8` |
| `verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean` | `ea8e96921f8c4bce9b26f7c99a1719d5f9e05520` |
| `verification/lean-mathlib/lean-toolchain` | `025e59548e48cf71f2744154e2890beefe30a258` |
| `verification/lean-mathlib/lakefile.toml` | `5935a5aed3ed1bf4c5a7224049464d18ed4a8600` |
| `verification/audits/foundations/act12-scope-propagation-audit.md` | `1d471eddde3bc0df8b7dbf26ddf642c4af6783b5` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/preregistration.md` | `6428e0acab070ccfd2a84d13c6f55616526206ba` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**`papers/` and `book/` are deliberately absent from this table.** They are 24.1B's evidence base
and are not this round's; see §0.2. The execution reads no manuscript file, and a manuscript
quotation appearing in the result note is a defect of the round.

### 3.2 The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**The `§A.37` justification.** The control plane's merge commit is the mandated execution base:

> The control plane's **merge commit is the mandated execution base**. The execution branches from
> exactly that commit and from nothing else, and its first act is to verify that the
> preregistration at that base has the blob the freeze names, before any target is executed.
> — `AGENTS.md:693–697`

That base is cut **after** this freeze is written, so it carries whatever sibling rounds merged in
between — and the same section makes what those siblings bring non-negotiable in the other
direction:

> Amendment happens before the merge and only then: once merged the preregistration is
> **immutable**, and an execution that diverges from it **records the discrepancy** rather than
> repairing the freeze. A freeze that can be edited after the outcome is known is not a freeze.
> — `AGENTS.md:688–692`

So presence at the base and licence to consume are two different things. The base is where the
execution *stands*; the freeze is what the execution *consumes*. Reading a sibling result because
it happens to be on disk would let the round's evidence base be chosen after its question was
known, which is exactly the editing-after-the-outcome that the immutability clause forbids.

**Why it bites specifically here.** Several sibling lanes are drafting and executing in parallel,
and **24.1B's own execution may land before this round's base is cut.** If
`lemma-24-1b-framework-data/result.md` is present at the mandated base, it is **not read, not
cited, not consumed and not answered**, and the execution records its presence as a start-state
note. This round's determinations do not depend on which of the two executes first, and the
execution states that in the result note in terms.

### 3.3 The files this round writes, pinned separately

Named separately, because the verbatim clause in §3.1 governs the read-only table without
qualification and does not apply to these. Each is pinned by blob at this base all the same, so
that a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads.

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | **read** as the pinned statement of the `P1` row and its section, and **written** only by appending the frozen post-round sentence for the case reached; **the row's label unchanged** |
| `verification/README.md` | `d25eb2d44d0aa324c095930f40174296fd0f2279` | one ledger paragraph appended |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the `R7-SCD` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `0bff51eb9cc3c22859da2ac0efc622910e77d7b4` | one import line added after `WordTraceSufficiency` |
| `verification/lean-manuscript-census.json` | `3e968e6c970301be5ba0b9631b234c957a6222d1` | **read**, and written only if the round's module earns a census entry; the execution states which |
| `verification/lean-mathlib/OIBridge/SpanningClassReach.lean` | — | created by the execution |
| `verification/programmes/substratum/lemma-24-1c-spanning-class-decision/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one file this round both reads and writes, and it is listed here
rather than above for exactly that reason. If its blob differs at the base, the execution records
the discrepancy and does not repair the freeze.

### 3.4 Immutable inputs

Consumed as merged and unrevised: `ST0`–`ST5` from the Lemma 24.1 semigroup-transfer round; `WT0`,
`WT1`, `WT2-gen`, `WT3` on the spanning class and `WT4` from 24.1A, with `WT2` UNDECIDED. The `P1`
row's label is read and not moved. **`WT2` is not reopened**: no piece of its (a)–(f) obstruction is
built, attempted, or scoped here, and a `WT2` proof appearing in the execution is a defect of the
round.

---

## 4. The evidence rule, FROZEN

Every determination in this round is carried by exactly one of:

1. a **kernel theorem** in this round's module, compiled at the pin, with its `#print axioms` line
   — evidence level 2; or
2. a **verbatim quotation** from a pinned blob, with its file and line coordinate; or
3. an explicit, recorded statement that **the passage or the Mathlib declaration sought does not
   exist**, on a **named and bounded** search — the search stated by what was searched, with what
   query, over what tree, so a reader can repeat it.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the classes
must coincide, because otherwise `WT3` would be idle", or "Mathlib must have this, because the
result is standard", is **not evidence** and may appear only in a clearly labelled analysis
paragraph that says it is not evidence and that no target rests on it.

**Silence is a finding.** Where the record does not settle a question, the finding is that it does
not settle it — reported as silence, with the search that established the silence named. Silence is
never reported as a negative answer and never reported as a positive one.

**Strength is recorded per determination**, as `full`, `high`, `medium` or `UNDECIDED`. A
determination carried by a passage that names a thing without displaying it is at most `medium`.

---

## 5. The targets, FROZEN

### `SC0` — locating controls, cheap and certain

Verify that each passage quoted in §2 stands at the mandated base, byte-identical, in the blob
pinned for it in §3.1 or §3.3, and record its coordinate as found. Record any coordinate drift as a
discrepancy without repairing the freeze.

**Falsifier.** Any of the §2 passages absent from its pinned blob at the base.

### `SC1` — exactly which readings `ST2`–`ST4` refuted, and exactly which they did not

Report, **each by its own verbatim quotation with a coordinate**, and **separately, never merged**:

1. **`ST2`** — the reading refuted, its carrier, and the absorption recorded with it.
2. **`ST3`** — the reading refuted, its carrier, and the four conjuncts the theorem carries.
3. **`ST4`** — the reading refuted, its carrier, and the **frozen deep-sector model** the theorem
   is stated inside.

Then report, by quotation, **what the three do not reach**: what `ST4`'s enlargement model leaves
outside it, what the round records about generators (ii)/(iv), and the round's own statement of
what a negative on the route does and does not license.

**This target exists so that nobody re-reads the refutation as broader than it is.** The permitted
form of every sentence in this target is "reading R, on carrier C, under model M, is refuted"; the
forbidden form is "the transfer is refuted", unqualified.

**Falsifier.** Any of the three readings not recoverable as a quoted statement with its carrier and
its model.

### `SC2` — what `ST5` and 24.1A established, and at exactly what scope

Report, by quotation with coordinates:

1. `ST5`'s **necessity** result and its scope — every word, balanced or not, on every carrier.
2. `ST5`'s **sufficiency** status as the Lemma 24.1 round left it, and the obstruction named there.
3. `WT1`'s statement and what it reaches on general pairs.
4. `WT2-gen` and `WT3`'s statements and the class they are stated on, with the class named by its
   merged definition and not paraphrased.
5. `WT2`'s UNDECIDED status and its named obstruction, quoted.
6. 24.1A's frozen post-round sentence, quoted whole.

**Falsifier.** Any of the six not recoverable verbatim from the pinned blobs.

### `SC3` — the route and the obligation, held apart on the record

Determine, **by quotation only**, what the merged record permits and forbids being said about the
**obligation** given that the **route** is refuted on the readings `SC1` enumerates. Report:

1. the permitted sentence, quoted, from each of the two merged results;
2. the forbidden sentences, quoted as lists, from each;
3. whether any passage anywhere in the pinned blobs asserts that the obligation itself is refuted,
   false, established or repaired — and if none is found, **record that on a named bounded search**
   over the pinned blobs, with the search stated.

**This is the target that owns the round's central hazard.** The route and the obligation are
different statements; a result note that treats a refutation of the first as bearing on the second
has committed the defect this target exists to prevent.

**Falsifier.** A passage found asserting anything about the obligation's truth. If one is found,
`SC3` reports it verbatim and the round records a discrepancy against the `P1` row's status cell.

### `SC4` — the reach of the spanning class, in the kernel

The round's substance. Four sub-determinations, each with its own outcome and its own strength;
each may land independently and one landing UNDECIDED does not stop the others.

**`SC4(a)` — `BlockSpanning U → HiddenCommutantTrivial U`.** For every finite `V`, `H` and every
`U : Matrix (V × H) (V × H) ℂ`: if `wordSpan U = ⊤` then every hidden `Y` commuting with `U` is a
scalar. The merged module already carries the closure facts this needs — `one_mem_wordSpan`,
`visibleBlock_mem_wordSpan`, `mul_mem_wordSpan`, `conjTranspose_mem_wordSpan`
(`WordTraceSufficiency.lean:139–181`) — so `wordSpan U` is a unital `*`-closed subalgebra, and the
step from "commutes with every element of `M_H(ℂ)`" to "is a scalar" is the centre of a matrix
algebra.

**`SC4(b)` — the converse, `HiddenCommutantTrivial U → BlockSpanning U`.** **NOT predicted.** This
is the direction that carries the double-commutant content: `wordSpan U` is a unital `*`-subalgebra
of `M_H(ℂ)` whose commutant is the scalars, and the conclusion `wordSpan U = ⊤` is the double
commutant theorem in exactly the spatial finite-dimensional form 24.1A recorded as absent. The
execution:

- attempts the direction;
- **and, whatever the attempt yields, performs and records a named bounded search** of Mathlib at
  the pin and of the corpus for a double-commutant or bicommutant statement for unital `*`-closed
  subalgebras of `Matrix n n ℂ`, reporting the search terms, the trees searched, and what was
  found or that nothing was found.

Both an established implication and a recorded absence are permitted outcomes. Neither may be
inferred from the other.

**`SC4(c)` — where Pair C sits.** Decide `BlockSpanning` for the `ST3`/`ST4` carrier `φ̂_C` on
`ℤ₂ × ℤ₃`, pinned by the same equations `ST3_pairC` pins it by, by direct computation and not by
`SC4(b)`. `ST3` establishes `HiddenCommutantTrivial` for it (`pairC_hct`,
`SemigroupTransfer.lean:677`), so this sub-determination settles one instance of `SC4(b)`
independently of the general question.

**`SC4(d)` — the class is a restriction, and is inhabited non-degenerately.** Exhibit, on a carrier
with at least two visible and at least two hidden elements, one `U` with `BlockSpanning U` and one
`U` with `¬ BlockSpanning U`.

The `ST2` carrier `φ̂_A` is a candidate for the second. The Lemma 24.1 result records at
`lemma-24-1-semigroup-transfer/result.md:141–142`:

> Both hidden commutants of Pair A contain `X`, so neither is GNS-cyclic, and Pair A separates
> the two cyclicities exactly as the freeze said it would.

**That passage is prose in a result note and is not, on a bounded search of the merged module's
axiom table, carried by a kernel theorem.** So the contrapositive route is available only if the
execution first proves `¬ HiddenCommutantTrivial φ̂_A` in the kernel, by exhibiting `X` as a
non-scalar element of the hidden commutant; `¬ BlockSpanning φ̂_A` then follows from `SC4(a)`. **If
that route is taken the execution says so and names both steps.** A quoted prose statement may not
stand in for either step, and a derived fact is not presented as a computed one.

**Falsifier for `SC4` as a whole.** `SC4(a)` refuted by a counterexample. That outcome would mean
the two predicates are not ordered at all, which the round reports as found and does not soften.

### `SC5` — the decision, assembled

Exactly one of the following, at the strength jointly reached by `SC4(a)`–`SC4(d)`:

- **`SC5-coincide`** — the spanning class and the GNS-cyclic class are the same class.
  **Requires `SC4(a)` and `SC4(b)` both positive at evidence level 2.** Nothing less writes it: a
  positive `SC4(c)` on one carrier is one instance and is not the general statement.
- **`SC5-strict`** — the spanning class is a strict strengthening of the GNS-cyclic class.
  **Requires `SC4(a)` positive at evidence level 2 and `SC4(b)` refuted by an exhibited `U` with
  `HiddenCommutantTrivial U` and `¬ BlockSpanning U`**, both conjuncts proved.
- **`SC5-UNDECIDED`** — the permitted fallback, with the obstruction named. **This is a live
  preregistered outcome and is not a failure of the round.** It is what the round reports if
  `SC4(b)` is neither established nor refuted, and the round's other targets still land.

**The gate on `SC5-coincide` and `SC5-strict`, FROZEN:**

> Neither `SC5-coincide` nor `SC5-strict` may be written on the strength of `SC4(c)` alone.
> `SC4(c)` decides one carrier. The general relation between the two predicates is `SC4(b)`'s
> question, and where `SC4(b)` is neither established nor refuted the outcome is `SC5-UNDECIDED`
> with the obstruction named, whatever `SC4(c)` found.

**Why this gate exists.** A single carrier on which the two predicates agree is consistent with
their coinciding everywhere and equally consistent with their diverging elsewhere. Letting one
instance write the general sentence would let the round reach its most consequential conclusion on
the cheapest available evidence. The gate makes the decision rule match the target's wording rather
than the easier question underneath it. **The gate binds the decision rule, not the prediction.**

### `SC6` — the ordering census: what evidence would settle which continuation comes next

A **census, not an action.** List, with coordinates, every place in the pinned blobs that states a
dependency between 24.1B's question and the spanning class — every passage that says one is needed
for the other, or that one is open pending the other. Then record, without acting on it and without
recommending it, the evidence each continuation would need:

- **for 24.1B** — as 24.1B's own merged freeze specifies it, cited by coordinate and **not
  restated**;
- **for a `WT2` continuation** — the (a)–(f) obstruction as 24.1A's result names it, cited by
  coordinate and not restated;
- **for a spanning-class continuation beyond this round** — whatever `SC4(b)` leaves open, stated
  as the open question it is.

**No continuation is recommended, chosen, scheduled or begun.** The census exists so that a later
owner call has its surface enumerated. A sentence of the form "the programme should next" is a
defect of this round.

---

## 6. The preregistered predictions, with signs, strengths and reasons

Recorded before execution so the outcome can be compared against them.

| target | prediction | sign | strength expected | reason |
| --- | --- | --- | --- | --- |
| `SC0` | the passages stand as quoted | positive | full | each was located and quoted while drafting this freeze, against the named blobs |
| `SC1` | the three readings are separately recoverable with carrier and model | positive | full | the merged result states each under its own heading with its carrier inline |
| `SC2` | all six items recoverable verbatim | positive | full | 24.1A's result states each under its own heading and quotes its own frozen sentence |
| `SC3` | permitted and forbidden lists recoverable; **no passage found asserting anything about the obligation's truth** | positive, with the third part expected to find nothing | high | both merged results carry explicit forbidden-sentence lists; the bounded search is over a small pinned set |
| `SC4(a)` | `BlockSpanning U → HiddenCommutantTrivial U` | positive | high | the merged module already carries unitality, multiplicative closure and adjoint closure of `wordSpan`, so the remaining content is the centre of `Matrix H H ℂ`; **high and not full, because the formal cost of the centre step at the pin is not known to this freeze** |
| `SC4(b)` | **NOT predicted — the round's genuine fork** | none | — | the direction is the spatial double-commutant statement, which 24.1A recorded as absent from Mathlib at the pin and from the corpus. This freeze does not predict that it is unavailable, because it did not search; the named bounded search is the target |
| `SC4(c)` | `BlockSpanning φ̂_C` decidable by direct computation | positive | medium | the carrier is `3 × 3` and finite, so the computation exists; **medium, because the formal cost of exhibiting nine spanning word values is not known to this freeze** |
| `SC4(d)` | both witnesses exhibited | positive | medium | the `¬ BlockSpanning` witness is expected to come from `ST2`'s Pair A through `SC4(a)`; the `BlockSpanning` witness is expected from `SC4(c)` if that lands, and otherwise needs its own carrier |
| `SC5` | **`SC5-UNDECIDED` is the single most likely outcome, and it is a full preregistered outcome of the round** | — | medium | it follows directly if `SC4(b)` lands neither way, which the gate then forces regardless of `SC4(c)`. `SC5-coincide` is the outcome if the double-commutant step proves reachable; `SC5-strict` if a separating witness exists. **This freeze leans to no one of the three** |
| `SC6` | census assembled | positive | high | a census over pinned blobs |

**Three predictions are deliberately held below full, and one is not made at all.** `SC4(b)` is the
round's substance, and a freeze that predicted it would be claiming the answer it is chartered to
find. `SC5` is held at medium on its most likely outcome and at no sign on the other two.

**No prediction licenses its own conclusion.** A target that lands against prediction is reported
against prediction, and the prediction is not amended. If any target lands above its predicted
strength, the result note records the promotion and its reason.

---

## 7. The post-round sentences, frozen now, one per outcome

Exactly one of the three is written, verbatim, in the result note and nowhere else.

**If `SC5-coincide`:**

> On every finite carrier `V × H`, the spanning hypothesis `BlockSpanning U` and the cyclicity
> predicate `HiddenCommutantTrivial U` are the same condition, both directions at evidence level 2.
> Lemma 24.1A's biconditional `WT3_spanning_iff` therefore holds on exactly the class the
> semigroup-transfer route's own GNS-cyclic reading assumes, and the class on which `ST3` refuted
> that reading and the class on which `WT3` established the biconditional are one class. This is a
> statement about two predicates on finite matrices. **It does not repair Lemma 24.1, does not
> restore the manuscripts' route, does not say the four generators are complete or incomplete, and
> says nothing about whether the reconstruction framework supplies the block-word trace data, which
> is round 24.1B's question and is untouched here.** The `P1` obligation remains OPEN and the row's
> label does not move.

**If `SC5-strict`:**

> On every finite carrier `V × H`, `BlockSpanning U` implies `HiddenCommutantTrivial U` at evidence
> level 2, and the converse fails on the carrier exhibited in the result note. The spanning
> hypothesis is therefore strictly stronger than the cyclicity predicate, and Lemma 24.1A's
> biconditional `WT3_spanning_iff` holds on a class strictly narrower than the one the
> semigroup-transfer route's own GNS-cyclic reading assumes. This is a statement about two
> predicates on finite matrices. **It does not repair Lemma 24.1, does not restore the manuscripts'
> route, does not say the four generators are complete or incomplete, does not say that `WT3` is
> idle, and says nothing about whether the reconstruction framework supplies the block-word trace
> data, which is round 24.1B's question and is untouched here.** The `P1` obligation remains OPEN
> and the row's label does not move.

**If `SC5-UNDECIDED`:**

> `BlockSpanning U` implies `HiddenCommutantTrivial U` at the strength recorded for `SC4(a)`.
> Whether the converse holds is UNDECIDED, with the obstruction named in the result note, and the
> relation between the class Lemma 24.1A's biconditional lands on and the class the
> semigroup-transfer route's GNS-cyclic reading assumes is therefore settled in one direction and
> open in the other. What the record does and does not settle is stated in the result note and is
> not extrapolated. **Nothing here repairs Lemma 24.1, restores the manuscripts' route, or says the
> four generators are complete or incomplete, and nothing here bears on whether the reconstruction
> framework supplies the block-word trace data, which is round 24.1B's question and is untouched.**
> The `P1` obligation remains OPEN and the row's label does not move.

**If the obstruction at `SC5-UNDECIDED` is the double-commutant statement**, the result note names
it in these terms and no others: `wordSpan U` is a unital `*`-closed subalgebra of `Matrix H H ℂ`;
`HiddenCommutantTrivial U` says its commutant is the scalars; the conclusion `wordSpan U = ⊤` is
the double commutant theorem in spatial finite-dimensional form; and the named bounded search found
it at the stated place or found nothing at the stated places. **That is a statement about what the
record and the library carry, not a claim that the converse does or does not hold.** Naming it is a
finding; resolving it would be a later round with its own control plane.

---

## 8. What none of these outcomes licenses

- **Nothing about the truth of Lemma 24.1 or of Theorem 24.** The forbidden sentences are "Lemma
  24.1 is repaired", "Lemma 24.1 is false", "Theorem 24 is false", "Theorem 24 is repaired",
  "completeness holds", "completeness fails", "the generators are complete", "the generators are
  incomplete", and "the manuscripts' route is restored".
- **Nothing that promotes or demotes any merged target.** `ST0`–`ST5` and `WT0`–`WT4` are consumed
  as merged and none is revised, re-derived, extended or weakened. In particular no outcome here
  makes `WT3` wrong, idle or absent from the record.
- **`WT2` is not reopened.** Its (a)–(f) obstruction stays recorded as UNDECIDED. No piece of it is
  built, attempted or scoped here. `SC4(b)` is a different statement — the double commutant for the
  commutant-trivial case — and if establishing it would establish `WT2`, the execution **records
  that and stops**, because reaching `WT2` through a side door is outside this freeze.
- **Nothing about 24.1B's question**, in either direction. See §0.2.
- **Nothing about the physical substratum.** Whether the wave rule on the cubic lattice satisfies
  `BlockSpanning`, or what its word traces are, is not asked, and 24.1A's exclusion of it at
  `result.md:242–243` stands.
- **Nothing about approximate deep sectors, time reversal, or enlargement.** `ST4`'s enlargement
  lemma is not consumed; this round is on a fixed carrier.
- **Nothing about Track B, `P0`, act 14's carriers, act 15's fork, or the fibre-Gram
  classification**, in either direction. The substratum programme and the OI→QM programme share the
  repository and nothing else; act 15's preregistration is pinned in §3.1 as the **house-form
  model** for this document and for no other purpose, and no target cites it as evidence.
- **Nothing about Bell or H-Bell**, nothing about A6, nothing about hydrodynamics.
- **No manuscript is edited, and no manuscript is read.** Whether and how to propagate any finding
  is an owner call in a separate round.
- **No selection principle is named**, and no sentence beginning "the selection principle is" is
  written.
- **No continuation is recommended.** `SC6` enumerates; it does not choose.

---

## 9. Named hazards

1. **H1 — conflating the refuted route with the untouched obligation.** The central hazard of the
   whole `P1` lane. The route is refuted on three enumerated readings; the obligation is untouched.
   These are different statements and a result note that slides from one to the other has failed.
   `SC1` and `SC3` exist for this hazard, the `P1` row's own wording is quoted at §2.1 as the
   standard, and the final report states for each sentence about the obligation which quotation
   carries it.
2. **H2 — fork-straddling.** A round that answered both 24.1B's manuscript question and the
   spanning-class matrix question could move either answer to fit the other. §0.2 scopes 24.1B out
   by name, object and evidence base; the manuscripts are absent from the start-state table; and
   the final report states explicitly that no manuscript was read and no 24.1B object was consulted.
3. **H3 — reading the refutation as broader than it is.** `ST2`, `ST3` and `ST4` refute three named
   readings on named carriers under a named deep-sector model. "The transfer is refuted",
   unqualified, is forbidden; `SC1` requires reading, carrier and model together in every sentence.
4. **H4 — reading `SC5-strict` as a defect verdict on 24.1A.** A strictly stronger hypothesis is
   not an idle theorem. The post-round sentence for that outcome is written to make the distinction
   unavoidable and the forbidden sentences are listed.
5. **H5 — reading `SC5-coincide` as a repair.** If the two classes coincide, `WT3` lands on the
   route's own class — and that still says nothing about whether the framework supplies the
   word-trace data, which is 24.1B's question. The post-round sentence carries the exclusion inside
   itself.
6. **H6 — reaching `WT2` through a side door.** `SC4(b)`'s double-commutant step is adjacent to
   `WT2`'s (b)+(e) obstruction. If the execution finds itself building the spatial structure
   theory, it has left this round. The non-licence in §8 says to record and stop.
7. **H7 — generalizing from one carrier.** `SC4(c)` decides one `3 × 3` instance. The gate in
   `SC5` exists for this hazard and is checked for in the final report.
8. **H8 — reconstructive inference presented as a finding.** Forbidden by §4. The final report
   states, per determination, which kernel theorem or which quotation carries it.
9. **H9 — treating silence as denial.** A bounded search that finds no double-commutant statement
   in Mathlib at the pin establishes that the search found nothing, not that the statement is
   unprovable. `SC4(b)` requires the search be named and bounded and its result be reported as what
   it is.
10. **H10 — writing a seal this round does not own.** `_SGT_*` and `_WTS_*` belong to the rounds
    that set them and are read and never written. §1.1 lists them; the execution's diff against
    `edge_rigidity_probe.py` adds the `R7-SCD` clause and changes nothing else.
11. **H11 — consuming a sibling result present at the base.** Governed by the anti-contamination
    invariant at §3.2, with 24.1B's own pending execution as the concrete case.
12. **H12 — moving the `P1` label.** The row's label stays **OPEN** on every outcome. The
    execution appends the frozen post-round sentence for the case reached and changes no status
    cell.

---

## 10. Definition budget

**Two slots, both conditional, and neither expected to fire.** The round's frozen statements in
`SC4(a)`–`SC4(d)` use only the merged definitions `BlockSpanning`, `wordSpan`, `wordEval`,
`visibleBlock` and `HiddenCommutantTrivial`, consumed exactly as merged. The budget exists so that
an unbudgeted definition appearing in the execution is visible as an overrun.

| slot | name | what it would be | fires only if |
| --- | --- | --- | --- |
| 1 | `hiddenCommutant` | the commutant of the visible blocks as a `Submodule ℂ (Matrix H H ℂ)`, so that `SC4` can be stated as a relation between two subspaces | stating `SC4(a)`/`SC4(b)` as implications between the two merged predicates proves unworkable at the pin, which this freeze does not expect |
| 2 | a named witness datum for `SC4(d)` | one `U` on a carrier with `|V| ≥ 2`, `|H| ≥ 2`, written as a definition rather than inlined | neither Pair A nor Pair C serves as the witness `SC4(d)` needs |

**If a slot fires, the execution says which and why.** If a precise formal subclaim worth separating
is uncovered, the execution **names it and does not build it**, and it becomes a candidate for a
later round with its own control plane.

**Evidence level.** `SC4` is at evidence level 2 throughout, with an axiom table and a
`#print axioms` line for every theorem. `SC0`–`SC3` and `SC6` are type P, carried by quotation and
by recorded silence, and the result note says so in terms rather than leaving the mixture to be
inferred.

---

## 11. The chronology control

1. This preregistration is merged **alone**, before any execution object exists. Once merged it is
   **immutable**; an execution that diverges records the discrepancy rather than repairing it.
2. The **mandated execution base** is the merge commit of this control plane's pull request. The
   execution branches from exactly that commit and from nothing else, and its first act is to
   verify that this file at that base has the blob the guard names, **at the path the guard names**,
   before any target is executed.
3. **Before certification the execution never absorbs later main.** No merge from main, no rebase,
   no amend, no force-push. The branch will show as behind, and often as conflicted, for as long as
   it sits at its sealed head; that is the protocol working.
4. The round is **sealing**. Its landing under `§A.37` is `E` → `L` → `P`: the landing merge `L`
   with current green main as first parent and exactly `E` as second, then the mandatory pin commit
   `P` setting `_SCD_SEALED_HEAD` to `E` and `_SCD_MERGE` to `L`. Conflicts are resolved in `L`,
   never in `E`; the sealed commit stays byte-identical.
5. The certification of record is the run whose `head_sha` is `E`, identified by that SHA and not
   by which run happens to be latest on the branch.
6. Full continuous integration must pass again on `P` before the pull request merges, and the
   resulting main build must be green before the next round's landing is constructed.
7. A red badge on the pull request sitting at `E` that comes solely from an archive clause which
   entered main after the base is not by itself a research failure; `workflow_dispatch` on the
   branch is the fallback for that case and is not the routine.

---

## 12. Execution discipline

The execution produces **the result note, the one Lean module, the `R7-SCD` guard clause, the one
import line, and the `ROADMAP` and `README` pointers the round's own section needs** — and nothing
else. One pull request from the mandated base carrying the execution; after certification the same
pull request carries `L` and then `P`.

---

## 13. Allowed final report

Every target with its outcome, evidence type, strength and the kernel theorem or quotation carrying
it; the three readings of `SC1` reported separately with carrier and model; `SC3`'s permitted and
forbidden lists quoted; `SC4`'s axiom table; the named bounded searches with their terms and trees;
the `SC6` census; the discrepancy section; the single frozen post-round sentence; an explicit
statement that no manuscript was read and no 24.1B object was consulted; and an explicit statement
of whether 24.1B's result note was present at the base and was not consumed. Nothing else.

---

## 14. Points at which this freeze chose a reading, recorded rather than resolved

1. **The round is the spanning-class decision and not 24.1B.** The alternative was to take 24.1B
   as this round's content. It is set aside because 24.1B's freeze is merged and immutable, not
   because 24.1B is the less interesting question. §0.2 records the ground.
2. **"The spanning-class decision" is read here as the relation between `BlockSpanning` and
   `HiddenCommutantTrivial`.** A different reading would take it as the question whether the
   manuscripts' substratum lies in the spanning class. That reading needs a `Substratum` packaging
   of the manuscripts' rule as dilation data, which no round has built; this freeze records the
   alternative reading, does not adopt it, and leaves it to `SC6`'s census.
3. **The round is sealing.** An alternative would write it unguarded, as 24.1B is written, and
   carry the immutability in the blob pins alone. This freeze does not, because the round produces
   kernel objects and every kernel object in this programme is ordered by a guard.
4. **`SC4(b)` is left unpredicted rather than predicted at low strength.** Recording no sign is
   more honest than recording a weak one, and the round's value does not depend on which way it
   falls.
5. **`SC4(c)` is kept as its own sub-determination rather than folded into `SC4(b)`.** One carrier
   settled is worth recording even where the general question is not, and the gate in `SC5` stops
   it from being read as more.

---

## 15. Decisions the owner settles before this freezes

Listed because the execution guard pins this file by **path and blob**, so each of these is fixed
before the merge and cannot move afterwards.

1. **The round's letter and directory name.** This file is drafted at
   `verification/programmes/substratum/lemma-24-1c-spanning-class-decision/preregistration.md` and
   calls the round **24.1C**. The letter `B` is taken: `lemma-24-1b-framework-data/` holds a merged
   control plane at blob `f614b666ad9098f866969c4c524e47f504e5d71c` and carries no result note at
   this base. If the owner wants a different letter or a different directory, it changes here.
2. **The guard tag and its constants.** Drafted as `R7-SCD` with `_SCD_BASE`,
   `_SCD_SEALED_HEAD`, `_SCD_MERGE`.
3. **The module name.** Drafted as `verification/lean-mathlib/OIBridge/SpanningClassReach.lean`.
4. **Whether the round is sealing at all.** §14.3 records the alternative.
5. **Whether `SC4(c)` and `SC4(d)` stay in scope**, or the round narrows to `SC4(a)` and `SC4(b)`
   alone.
6. **Whether `SC6` stays in scope**, or the ordering census is deferred to an owner call outside
   any round.
7. **Whether the census file `verification/lean-manuscript-census.json` is written**, listed in
   §3.3 as conditional.
8. **The execution's ordering against 24.1B's pending execution.** This freeze is written so the
   two are independent in both directions, and §3.2 governs whichever lands first. If the owner
   wants them ordered, the order is fixed here and the freeze says so.
