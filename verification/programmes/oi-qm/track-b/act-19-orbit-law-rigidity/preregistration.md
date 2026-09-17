# Track B act 19 — the rigidity of the cross-time laws act 18 opened: CONTROL PLANE

Owner-called. This file is the whole of act 19's control plane and is merged **alone**, before any
execution object exists. It takes up the question act 18 leaves standing at the top of its `L`-axis:
**act 18 showed that a genuine cross-time law plus one initial orbit can propagate (`L-PROP`), so how
rigid is the class of such laws?** It is **not** an attempt to derive or to recognise quantum
evolution, which is a later round and is an explicit non-doing here. It is **not** the threading
question, which act 13 localized and acts 14, 15 and 16 pursued carrier by carrier. It classifies
what act 18 opened, against a ladder of conditions frozen before any census is run.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–778**, quoted verbatim at this base —
the numbered item's opening sentence, ending part-way through line 778:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes
>    ownership of changing existing seal state — takes a pin commit `P`, and `P`
>    is mandatory.**

This freeze **creates new seal state**. The execution writes a new Lean module with its own guard
clause in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-OLR`**, and that
clause carries the archive-mode constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_OLR_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_OLR_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_OLR_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_OLR_SEALED_HEAD` to `E` and `_OLR_MERGE` to `L`, moving the `R7-OLR` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_OLR_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

### The lifecycle derivation, and why it comes out SEALING

**The lifecycle is derived from what the round owns, not from what recent Track B rounds happened to
take.** The rule the owner set is: act 19 is sealing **if and only if** its execution creates a new
formal object whose chronology matters to the result. The derivation, run against this freeze's own
scope:

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the shared structural theorem, the six ladder conditions as named `Prop`s, the census
   verdicts, the discriminating test and the headline. None of these exists at the base.
2. **Their chronology is load-bearing, and more so here than in any recent round of this
   programme.** The round's whole claim is that the condition ladder was fixed **before** the census
   of survivors was run. A ladder assembled after it was known which laws survive would be worth
   nothing: it would be reporting a search that had already seen its own answer, and the headline —
   rigid, family, or wide — would be a choice rather than a finding. **The ordering obligation frozen
   below is itself a chronology claim**, and an ancestry guard rooted at this control plane's merge
   commit is the mechanism that makes it enforceable rather than aspirational.
3. **A new module with new named results is new seal state** under `§A.37`'s definition, and a new
   `R7-*` ancestry/archive guard is new pin state.

**Therefore act 19 is SEALING, and it owns no other seal state.** The derivation is recorded here so
that a later reader sees the reason and not a habit.

**The counterfactual is recorded too, because the rule has a negative branch.** Were act 19 directed
to be purely classificatory over existing formal results — adding no Lean module, no named result and
no guard clause — it would own no seal state, it would take `L` alone under `§A.37` item 2, and it
would **not** acquire a pin merely because acts 13 through 18 each had one. In that shape the
ordering obligation would lose its mechanical enforcement and would rest on the result note's own
testimony, which is weaker; the freeze says so rather than presenting the non-sealing shape as
equivalent. **That branch is not this round's shape**, and the choice between them is recorded as an
open decision for owner settlement below.

### The tag, the stem, the module and the round directory are free at this base

At **`2ef6f1c7718bcd4739a550fe1c6413550490b3fe`**, the certified `main` this freeze is written
against:

- `git grep -- 'R7-OLR'` returns nothing anywhere in the tree, and the tag is absent from the
  seventy-eight `R7-*` tags `verification/lean/edge_rigidity_probe.py` currently carries.
- `git grep -- 'OLR'` returns nothing anywhere in the tree — **the bare three-letter form does not
  occur in prose, in Lean, in Python or in any manuscript**, so a bare-stem search for it is
  unambiguous.
- No constant whose name contains the stem `_OLR` exists in `verification/lean/edge_rigidity_probe.py`.
  The fifty-three seal constants that file carries use the stems `_A12P_`, `_A6D_`, `_A6I_`, `_A6P_`,
  `_ABR_`, `_CLG_`, `_CTI_`, `_HYA_`, `_HYB_`, `_HYE_`, `_PC4_`, `_PC4S_`, `_PQT_`, `_RBR_`, `_RNC_`,
  `_SGT_`, `_TCF_`, `_TRJ_`, `_TSG_`, `_WTS_` and `_XTS_`, and no substring search for `OLR` or
  `_OLR` can reach any of them.
- **The alternatives were checked before `OLR` was chosen**, and the check is recorded so that the
  choice is not re-litigated: the stems in use by the two most recent rounds are `_TRJ_` (act 17) and
  `_XTS_` (act 18) and both are excluded on that ground alone. Among the candidate stems for this
  round's subject, `LWR`, `ORL`, `LRG` and `OLR` all return nothing at this base; `RIG`, `LAW` and
  `ROT` were rejected without a search because their bare forms are common English substrings —
  *rigidity*, *rigid*, *law*, *laws*, *rotation* — and a bare-stem freedom check for any of them
  would be ambiguous in exactly the way act 18 recorded for `ICS` and `CTS`. **`OLR` was chosen
  because its bare form collides with nothing in the tree**, which is the property the freedom check
  needs.

**The round directory and the module name are free at this base too.**
`git ls-tree -r 2ef6f1c --name-only` lists 628 paths and contains no path matching `act-19` and no
path matching `OrbitLawRigidity`; `git grep -- 'act-19'` and `git grep -- 'OrbitLawRigidity'` both
return nothing anywhere in the tree. The round directory is
`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/` and the module is
`verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean`.

**One nearby name is recorded so that it is not mistaken for a collision.** The tree already carries
`verification/lean-mathlib/OIBridge/EdgeRigidity.lean` and
`verification/lean-mathlib/OIBridge/OperationalRigidity.lean`, and the guard file is itself named
`edge_rigidity_probe.py`. Those are different modules about different objects in different
programmes, and none of them contains the string `OrbitLawRigidity` or the stem `_OLR`. **A shared
English word is not a collision**, and the freedom check above is by exact string and not by theme.

### What this round does NOT own, named exhaustively

It alters **no existing seal constant**. In particular `_XTS_BASE`, `_XTS_SEALED_HEAD` and
`_XTS_MERGE` — act 18's seal — and `_TRJ_BASE`, `_TRJ_SEALED_HEAD` and `_TRJ_MERGE` — act 17's — and
`_RNC_BASE`, `_RNC_SEALED_HEAD` and `_RNC_MERGE` — act 16's — and `_TCF_BASE`, `_TCF_SEALED_HEAD` and
`_TCF_MERGE` — act 15's — and `_PQT_BASE`, `_PQT_SEALED_HEAD` and `_PQT_MERGE` — act 14's — and
`_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE` — act 13's — and `_A12P_*`, `_SGT_*`, `_TSG_BASE`
and `_CLG_BASE` are **read and never written**. An archive seal belongs to the round that set it:
touching the guard file that carries those constants does not make this round their owner, and the
execution's diff against `edge_rigidity_probe.py` **adds** the `R7-OLR` clause and changes nothing
else in the file.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`2ef6f1c7718bcd4739a550fe1c6413550490b3fe`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

### The obligation, and the part of it act 18 has now opened

`verification/ROADMAP.md`, **line 63**, the `P0` row's obligation cell and its status opening:

> | **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED: act 11's `GL2` proved the visible family does not fix the relative evolution;

and, from the same line, the sentence that makes the row two-part and names this round's part first:

> so what remains is **two-part**: what selects or constrains the Gram/orbit trajectory **across time**, and what determines the cross-time threading within those orbits, which act 11's `GL2` shows is not fixed even by the full Gram trajectory

and, from the same line, the clause act 18 appended, which is the baseline this round starts from:

> On the structural-law axis, which asks whether a constraint writable from the anchor and the visible family alone is proper and propagates, one named generator law, written at orbit level so that it descends, has a solution set at one exhibited configuration that is nonempty, non-singleton modulo the round's cross-time equivalence and proper, and two of its solutions agreeing at the initial time have the same trajectory.

### The act 17 baseline this round does not touch

`verification/ROADMAP.md`, **lines 560–565**, beginning part-way through line 560 — the bullet opens
at line 556, and the span quoted here is the part that governs this round:

> **there is no additional universal cross-time constraint on coherent Gram trajectories
> beyond pointwise realizability** — the present notion of coherence contributes no coupling between
> times at all, and **any such law must enter as additional structure**. The narrowing act 12's rank
> bound effects is **pointwise** and is labelled pointwise. This is a statement about coherence as
> the programme defines it, indexed by the naturals and pointwise in time, and **not** a statement
> that no cross-time structure could be added to the programme.

### The two-axis reporting precedent

`verification/ROADMAP.md`, **lines 585–587**:

> **The two findings are on two axes and are not merged into one ordering.** "The present notion of
> coherence imposes no cross-time coupling" is not above or below "these four proposed selectors all
> fail at one admissible configuration": they answer different questions.

Act 19 has **one** axis and one headline, and it inherits the discipline that produced that sentence
rather than the shape: a verdict is of the exact proposition frozen for it, the label is chosen
before the search, and no outcome is allowed to choose its own wording.

### The act 18 result this round consumes

`verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md`,
**line 13**:

> **The headline is the ORDERED PAIR of two co-equal axis outcomes:** **(`D-MID`, `L-PROP`)**. The

and, from the same note, **lines 145–146**, beginning part-way through line 145 — the sentence
`xs1_splice` opens at that line's start, and the span quoted here is the kernel statement this
round's shared theorem is bounded against:

> `xs1_pointwise_not_propagates` is the consequence:
> `PointwiseLaw Law → ¬ PropagatesFrom a₀ Γ Law`, at every configuration.

and **lines 446–448**, the descent route act 18 took and this round consumes:

> **The descent obligation is DISCHARGED, by the first of the two routes the freeze permits.** The
> candidate is **written directly as an orbit-level transition** `[G_{t+1}] = Φ([G_t])`, with `Φ` the
> identity on per-slice orbit classes, rather than as a representative-level `V_t` that would then

### The interpretation boundary the whole of `P0` sits inside

`verification/ROADMAP.md`, **lines 52–57**:

> Accordingly, a failure of uniqueness at `P0` is not by itself a failure of quantum emergence. It
> determines the ontology of that emergence: either the residual lift freedom is physically redundant,
> additional structure selects one quantum history, or observational incompleteness determines only an
> equivalence class of quantum histories. Only an empirically distinguishable residual not removed by
> the physically appropriate equivalence relation would license a claim of physics beyond standard
> quantum mechanics.

### The lifecycle rule that fixes this round's base

`AGENTS.md`, **lines 697–700**:

> The control plane's **merge commit is the mandated execution base**. The
> execution branches from exactly that commit and from nothing else, and its
> first act is to verify that the preregistration at that base has the blob the
> freeze names, before any target is executed.

**The mandated base, stated as this round's own commitment.** The execution branches from the merge
commit of **this** control-plane pull request and from **nothing else** — not from `main` at any
later point, not from a sibling lane's head, and not from a rebase of either. **Its first act is to
verify that the preregistration at that base carries the blob this freeze names**, before any target
is executed, and to record the verification in the result note. If the blob differs, the execution
records the discrepancy and does not repair the freeze.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `2ef6f1c7718bcd4739a550fe1c6413550490b3fe`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/preregistration.md` | `fd3fa1359188966cae006deba4944a14aab5f3dd` |
| `verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md` | `14a2cd8c54946bf0078329402e6f853107b31d9d` |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md` | `3b5570102aa6aacb09788059989a70d8cdd5b70f` |
| `verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/result.md` | `a252b885c6f7f5f31d3ac101070e7f6ee1ebf5d6` |
| `verification/programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation/result.md` | `b13d684cb7454ff414a34ed9b6dca39065c3470f` |
| `verification/programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork/result.md` | `fe8df06ffefac22ce87668ecf026f4c9ebc5c13f` |
| `verification/programmes/oi-qm/track-b/act-14-threading-observability/result.md` | `d4815d56b1cea2ed42540a7d6262c3c4201ac9b7` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/preregistration.md` | `5d8bee2c616d12c53234c54bfa7efae19dc1dcc1` |
| `verification/programmes/oi-qm/track-b/act-13-cross-time-invariants/result.md` | `2c38dbf1c79a0aa3eb654a40d6cb527e99349b4a` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md` | `5850238f290f0424ff677ff6d5cc2c039b1f58c2` |
| `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/result.md` | `467d8be147b6ebd91f2eed12404566af74ac779f` |
| `verification/programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md` | `7b24353ad626de6f930e41242334cb09945ae303` |
| `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/result.md` | `ec9a6e0d8a7019805aca069abc39f90d632b6a2b` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/preregistration.md` | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| `verification/programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md` | `0e2c067a90ef9b8e3a4596299ff594bb6ba6807a` |
| `verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean` | `cb14c43b0becfe1a379ae3615d5553723ede9163` |
| `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` | `afc22cfc93b244c80e1c55a273dcfda1ddebb121` |
| `verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean` | `47eb21e22845f0319926227c80d0d7f2f033880b` |
| `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` | `4bba2040c33424fafbc6d31c0d63b86dff33691a` |
| `verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` | `8d17177799327d648bbbd001cf237e1ac37bd3fc` |
| `verification/lean-mathlib/OIBridge/ReanchoredChannelScope.lean` | `16f08f712cbbb0a0f752ac8d7e072b1d5e52d761` |
| `verification/lean-mathlib/OIBridge/CancellationFork.lean` | `2cdfdf7742694391f16a73eebe37e1c0dcad6674` |
| `verification/lean-mathlib/OIBridge/ThreadingObservability.lean` | `91508205b33d9419fbffec5ad44035fad35de5f1` |
| `verification/lean-mathlib/OIBridge/DilationChoice.lean` | `7e3a8222cedf530f3c109662e7174d72b6358063` |
| `verification/lean-mathlib/OIBridge/AnchorRobustness.lean` | `b74202bc160918b32ca1b333da532a141ea8015d` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

### The files this round writes

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` | **read** as the pinned statement of the `P0` row, of act 17's baseline and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `5cdd759534c9668c7f447b35a95ff888c973408a` | the `R7-OLR` clause **added**; **no existing seal constant altered** |
| `verification/lean-mathlib/OIBridge.lean` | `81814f25d9ea17aee2e15237af5bbfbe8dd92cfa` | one import line added after act 18's module |
| `verification/lean-manuscript-census.json` | `86bda14f2f88335dfa4fd3fdb10f693ab134537e` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/result.md` | — | created by the execution |

`verification/ROADMAP.md` is the one prose file this round both reads and writes, and it is listed
here rather than above for exactly that reason: the verbatim clause governs the read-only table
without qualification, and the `ROADMAP`'s treatment is stated in its own row. A difference in that
one blob at the base is recorded in the result note as a discrepancy, and the freeze is not repaired.

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

**Why this matters here, concretely.** Sibling lanes are drafting and executing in parallel with this
freeze, and some will merge into `main` before this round's execution begins. This freeze is written
against `2ef6f1c` alone and consumes nothing from any of them. No lane's unlanded output is read,
cited, compared or waited for.

## Source scoping, carried from acts 13 through 18

Source identities per act 1's frozen table: **A** = arXiv:2302.10778v3, **B** = arXiv:2507.21192v1,
**C** = arXiv:2309.03085v2. **Only Source A is adjudicated.** **Track I is not touched**, in either
direction; neither branch is evidence for the other.

## Why this round exists, and what act 18 left in front of it

Act 18's `L`-axis reached its top line. A law writable from `(a₀, Γ)` before any lift exists, stated
at orbit level so that it descends, with a solution set that is nonempty, non-singleton modulo the
round's cross-time equivalence and proper, was shown to propagate: two of its solutions agreeing at
time `0` have the same trajectory, and the initial orbit does work. **That answers an existence
question and opens a uniqueness question**, and the uniqueness question is this round's whole
subject. `L-PROP` says *a* law propagates. It says nothing whatever about *how many* such laws there
are, and act 18's own verdict language says so in terms: a `Y-PROPAGATES` is a statement about the
exact law that freeze named and about nothing in its neighbourhood.

**So the record now carries one inhabitant and no census.** Act 18 exhibited the identity transition
as an `L-PROP` law and stopped there, correctly, because its freeze had closed its candidate list at
four members and its scope at bounded existence. The question this round asks is the next one and is
frozen by the owner: **given that a genuine cross-time law plus one initial orbit can propagate, how
rigid is the class of such laws?**

### What act 19 inherits, and consumes without re-proving

These are consumed at merged strength. **None is re-proved, strengthened, redefined or enlarged**,
and a merged statement is not enlarged by being consumed.

1. **Act 17's `TJ1`, both directions.** The Gram trajectories of coherent lifts of a visible family
   are **exactly** the pointwise realizable assignments, so the admissible set is the **product over
   time** of the per-slice realizable sets. Every cross-time law enters the programme as additional
   structure.
2. **Act 17's `TJ3`.** Class-level selection impossibility, quantified `∃ C ∀ S`: one admissible
   configuration defeats every member of act 17's frozen four-member selector class. It is
   impossibility within that class at one configuration and is not a universal statement about
   structures.
3. **Act 18's headline, the ordered pair `(D-MID, L-PROP)`.** This round consumes the `L-PROP`
   element. The `D-MID` element is about readback data and is **not** this round's subject; no
   statement of this round bears on it in either direction.
4. **Act 18's `XS1`.** A pointwise law's solution set factors as the product over time of its
   per-time solution sets, so any uniqueness it yields is slice-by-slice and never propagation;
   `xs1_pointwise_not_propagates` carries the consequence, `PointwiseLaw Law → ¬ PropagatesFrom a₀ Γ
   Law`. **This is not the statement that no pointwise constraint yields cross-time determination**,
   which is false: a pointwise condition with a unique solution at every time determines the
   trajectory slice by slice, and what fails is propagation.
5. **Act 18's `LC3` and its descent discharge.** `L-PROP` was reached via `LC3`, the generator law,
   with the descent obligation discharged at orbit level rather than by a gauge-naturality proof on
   representatives. This round consumes the discharged candidate as the first member of its census
   list and does not rebuild it.
6. **Act 18's propagation definition, frozen with TWO clauses:** (i) uniqueness from the initial
   orbit, and (ii) the initial orbit contributes. Both clauses travel into this round unchanged, and
   the two non-propagation mechanisms — residual histories after the initial orbit is fixed, and an
   initial orbit that contributes nothing — stay apart and named.
7. **Act 12's `GramPhaseEquiv`**, the per-slice equivalence on fibre-Gram tuples, and **act 17's
   `GramTrajEquiv`** (`≈_O`), the trajectory lift of it. **Act 12 supplies the slice equivalence and
   act 17 supplies the trajectory lift**, and the attribution is kept exact wherever either is named.
   Both are consumed and **neither is redefined**.

### What the merged record supplies about rigidity, and what it does not

This table is a reading of the merged record, stated so that the gap this round works in is visible
and so that no target of this round has to discover it. Each cell cites the merged label that fills
it.

| question about the law class | what the merged record says | label |
| --- | --- | --- |
| whether a cross-time law can propagate at all | **yes**, one named law does | act 18's `L-PROP`, via `LC3` |
| whether a pointwise law can propagate | **no**, as a theorem | act 18's `XS1`, `xs1_pointwise_not_propagates` |
| what the admissible trajectory set is | exactly the product over time of the per-slice realizable sets | act 17's `TJ1`, both directions |
| what the per-slice orbit classes are | act 12's classification, with the rank bound inside `RealizableGram` | act 12's `SH1`, `TG2` |
| whether a law's transition descends to orbit classes | for `LC3`, **yes**, discharged at orbit level | act 18's `LC3` descent |
| **how many** laws propagate | **nothing on the record** | — |
| whether two laws can share an initial orbit and diverge | **nothing on the record** | — |
| whether structural conditions narrow the class | **nothing on the record** | — |

**The last three rows are this round's subject.** The merged record exhibits one law and is silent on
the class. Whether that silence is a gap or is the answer is what the round's first target asks of
the record and what its later targets ask of the kernel.

## The question, FROZEN

> **Given that a genuine cross-time law plus one initial orbit can propagate (`L-PROP`), how rigid is
> the class of such laws?**

**The round does NOT try to derive Schrödinger evolution.** It classifies what act 18 opened.
Deriving or recognising quantum evolution is a **later round** and is an explicit non-doing here,
named in the non-doings section and again in the forbidden sentences. No statement of this round
says, implies or approaches the claim that a surviving law is, resembles, approximates or points
toward quantum evolution, and no condition of the ladder below is stated with quantum evolution as
its standard of correctness.

## The strength of the ask, FROZEN

**The ask is a BOUNDED RIGIDITY CENSUS over a ladder of conditions frozen before the census, and the
owner has settled it as such.** The round asks whether the laws satisfying every frozen condition
coincide up to the already-recognized equivalence, or form a characterizable family, or form a class
too wide for a characterization this round can reach. It does **not** undertake to find the weakest
condition set that yields rigidity, to search for further conditions, to adopt any surviving law, or
to show that any of them obtains.

**Why a bounded census and not the stronger asks, recorded as a reason.** A "weakest sufficient
condition set" ask would require a lattice argument over an unbounded space of conditions, which is
the same unbounded shape act 18 named as a non-doing on its own axis and which this round's
definition budget does not fund. A "classification of all propagating laws" ask without a frozen
ladder would quantify over a space nothing on the record bounds. **A closed ladder frozen first and a
closed list of named laws frozen with it is what the round can honestly attempt**, and it is what the
three headline outcomes are calibrated to.

**The ask does not narrow what may be reported.** All three headline outcomes are **preregistered as
reachable, each at the full evidence bar frozen for it**. A result outside the frozen scope is
recorded as an observation and not executed. **The scope is fixed here, before the census.**

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13, 17 and 18

Throughout, `V` and `A` are finite types, `a₀ : A` the anchor, `Γ : ℕ → Matrix V V ℝ` a **visible
family**, `U : ℕ → U(V × A)` a lift, and the following are consumed **unmodified**, at their own
strengths: `readback`, `AdmissibleDilationAt`, `readback_relabel` (`R-3`),
`one_admissible_at_every_anchor`, `StrongAnchorStabilizer`, `WeakAnchorStabilizer`, `CoherentLift`,
`GaugeRelated`, `strong_mem_weak`, `gl2_strong_gauge_moves_relative_candidate` (`GL2`),
`LeftFibreGroup`, `TwoSidedRelated`, `FibreGram`, `GramPhaseEquiv`, `RealizableGram`,
`fibreGram_apply`, `fibreGram_diag`, `fibreGram_diag_of_admissible`, `fibreGram_posSemidef`,
`fibreGram_rank_le`, `sum_fibreGram`, `fibreGram_left_mul`, `fibreGram_mul_weak_apply`,
`left_preserves_admissible`, `gramPhaseEquiv_of_twoSided`, `twoSided_slice_iff`,
`twoSidedRelated_iff` (`TG2`, lifted), `gramPhaseEquiv_cross_invariant`, `hadamard_cross_ratio`,
`hadamard_slices_not_twoSided`, `hadamard_lifts_not_twoSided` (`TG3`), `sh1_necessity`,
`sh1_sufficiency`, `sh1_shape` (`SH1`), `sh1_c2_unique_orbit` (`SH1-C2`), `FibreCrossGram`,
`fibreCrossGram_apply`, `fibreCrossGram_diag`, `sum_fibreCrossGram`, `crossGram_two_sided`,
`ct2a_crossGram_iff_constLeft` (`CT2` (a)), `ct2b_fibreCrossGram_iff` (`CT2` (b)),
`ct3g_fibreGram_strong_right` and `ct3g_fibreCrossGram_strong_right` (`CT3` (G)); act 17's
`GramTrajEquiv`, `gramTrajEquiv_refl`, `gramTrajEquiv_symm`, `gramTrajEquiv_trans`,
`gramTrajEquiv_of_threading`, `tj1_necessity`, `tj1_sufficiency`, `tj1_trajectory_set`,
`tj1_no_universal_cross_time_constraint`, `hadamard_constant_lifts`, `SelectsAt` and
`tj3_imp_class_level_selection_impossibility`; and act 18's `PointwiseLaw`, `DeterminesTraj`,
`ProperAt`, `PropagatesFrom`, `xs1_pointwise_factors`, `xs1_splice`, `xs1_pointwise_not_propagates`,
`lc0_pointwise_law`, `lc3_generator_law`, `prod_mem_unitaryGroup`, `prod_admissible` and
`xs5_l_axis_prop`.

**Act 7's boundary is carried at every use of the visible family**, exactly as acts 11 through 18
carry it: act 7's `D4b` came back **negative** — Source A supplies no general map carrying the
relative candidate on the dilated carrier back to `V` — and the readback is the repository's own,
frozen by act 7's readback amendment. Every statement in this round about what is visible is a
statement under that convention, said at each use rather than once in a footnote.

### The orbit state space and the transition family

**Three objects, named once and used everywhere.**

- **`Ω(Γ, t)`, the admissible orbit state space at time `t`.** The set of `GramPhaseEquiv`-classes of
  fibre-Gram tuples `G : V → Matrix V V ℂ` satisfying `RealizableGram A (Γ t) G`. Act 12's `SH1`
  characterizes membership and carries the `|A|` rank bound inside `RealizableGram`; act 17's `TJ1`
  is what makes `Ω(Γ, ·)`'s product over time the admissible trajectory set. Classes are written
  `[G]`, and `Ω(Γ, t)` is written `Ω_t` where `Γ` is fixed by context.
- **A transition family `Φ`.** A family `Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)`, written at
  representative level and required to **descend**: `GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ
  t G')` at every `t`. The descent conjunct is part of the object and is not commentary on it, for
  the reason act 18 recorded for `LC3`: a representative-level transition that does not descend
  "selects" by fixing an unphysical frame, and what it determines is the frame and not the orbit.
- **The law a transition family generates.** `Law_Φ 𝔾 ≡ ∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`.
  This is a **law datum** in act 18's frozen sense: it is written from `(a₀, Γ, ℕ)` alone, it is
  constructed before any lift exists and it consults no lift at any point.

**One reading of "written from `(a₀, Γ)` alone" is load-bearing and is stated so that it cannot
drift.** A law datum is **chosen** before any lift exists and consults **no lift**; it need **not**
be a canonical function of `Γ`. Act 18's own `LC1` takes a prescribed matrix family and its `LC2`
takes a named pseudometric and a named bound, and neither is canonical in `Γ`. **The property that
does the work is lift-blindness, not canonicity**, and this round reads act 18's definition exactly
as act 18 wrote it and neither narrows nor widens it.

### The frozen quotient list — every equivalence a rigidity verdict may use

**Every equivalence any verdict of this round is taken modulo is one of these three, each established
before act 19 and each traceable to the round that established it.** The list is closed at this
freeze.

1. **Act 12's `GramPhaseEquiv`** — the per-slice equivalence on fibre-Gram tuples,
   `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` **line 102**, whose orbits act 12's `TG2`
   identifies with the orbits of the defined two-sided action. **Act 12 supplies it.**
2. **Act 17's `GramTrajEquiv`, written `≈_O`** — the trajectory lift of (1),
   `verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean` **line 121**: two trajectories
   are the same iff `GramPhaseEquiv (𝔾 t) (𝔾' t)` at every `t`, the phase family chosen independently
   at each time. **Act 17 supplies the lift**, built on act 12's slice equivalence.
3. **`≈_L`, the law equivalence, which is NOT a new relation.** `Law ≈_L Law'` iff the two laws have
   the same solution set among pointwise realizable trajectories:
   `∀ 𝔾, (∀ t, RealizableGram A (Γ t) (𝔾 t)) → (Law 𝔾 ↔ Law' 𝔾)`. It is **set equality of solution
   sets** and identifies no objects that (1) and (2) do not already identify: both laws being
   `≈_O`-invariant by the descent conjunct they carry, the two sets compared are already
   `≈_O`-saturated. **`≈_L` introduces no new identification and is defined from (1), (2) and
   equality alone.**

**No other equivalence may be used to reach `L-RIGID`.** An equivalence introduced, widened,
coarsened or re-chosen during execution — on trajectories, on classes, on transition families or on
laws — **cannot be used to reach `L-RIGID`**, and this round adopts neither raw Gram equality, nor
the uniform-phase relation, nor act 13's level-2 or level-3 relations, nor any conjugacy or
similarity relation on transition families.

**If the execution finds a plurality of survivors that would collapse only under some equivalence
outside this list, the outcome is `L-FAMILY` or `L-WIDE` and not `L-RIGID`.** The candidate new
equivalence is **recorded as an observation for a later round with its own freeze**, and is never
applied to this round's verdict.

## The condition ladder `L0`–`L5`, FROZEN BEFORE ANY CENSUS

**Six conditions, frozen here, in this wording, before any census of surviving laws is run.** Each is
stated as a predicate of a transition family `Φ` at a configuration `(a₀, Γ)`, with the law it
generates carrying act 18's `ProperAt` and `PropagatesFrom` as a standing hypothesis — **a candidate
that is not an `L-PROP` law in act 18's frozen sense is not on this round's ladder at all**, and its
exclusion is a consequence of act 18's definitions and not a condition of this round.

### `L0` — a well-defined total evolution on the admissible orbit state space

> **`L0`.** For **every** `ω ∈ Ω_0` there is a pointwise realizable solution `𝔾` of `Law_Φ` with
> `[𝔾 0] = ω`; and by act 18's propagation clause (i) that solution is unique modulo `≈_O`. So `Φ`
> induces a **total function** `E_t : Ω_0 → Ω_t` at every `t`, with `E_0 = id`.

**Why totality is the content, and why it is not already given.** Act 18's `Y-PROPAGATES` supplies
**uniqueness** from the initial orbit (clause (i)) and **non-degeneracy** (clause (ii)). It does
**not** supply that every admissible initial orbit extends to a solution at all. A law whose
solutions exist only through a named subset of `Ω_0` satisfies both of act 18's clauses while failing
to be an evolution of the state space: it is an evolution of part of it. `L0` is that gap and
nothing else, and the countercontrol table names the law that exhibits the gap.

### `L1` — preservation of pointwise admissibility

> **`L1`.** The transition carries admissible classes to admissible classes as a **relation on the
> whole per-slice orbit space**, and not merely along its own solutions: for every `G` with
> `RealizableGram A (Γ t) G`, the tuple `Φ t G` satisfies `RealizableGram A (Γ (t+1)) (Φ t G)`.

**Stated for the relation and not for its restriction to solutions, deliberately.** Restricted to
solutions the condition is close to vacuous, because a solution is pointwise realizable by
definition. Stated for the whole orbit space it is a real demand on `Φ` and it is the demand the
condition is meant to make: an evolution that must be truncated to stay admissible is not an
evolution of the admissible orbit space. **The freeze predicts this rung is implied on the class the
shared theorem produces and says so in advance**, with the implication to be **proved** rather than
asserted; see the rung-status labels below.

### `L2` — time-homogeneity and compositionality

> **`L2`.** There is a single `Φ̂` with `Φ t = Φ̂` at every `t`, so one law iterates consistently; and
> the induced evolution composes, `E_{t+s} = E_s ∘ E_t` with `E_t = Φ̂^t` on classes.

**Two conjuncts, and the second does not follow from the first for free.** Independence of `t` gives
`E_t = Φ̂^t` by induction only once the descent conjunct has made `Φ̂` a function on classes;
composition is then immediate. The freeze keeps them as two conjuncts so that a candidate failing
either is reported against the conjunct it fails.

### `L3` — reversibility, stated as two conjuncts

> **`L3i` — injectivity.** `Φ̂` is injective on classes: `GramPhaseEquiv (Φ̂ G) (Φ̂ G') →
> GramPhaseEquiv G G'`, for `G`, `G'` admissible at the configuration.
> **`L3s` — surjectivity.** Every admissible class is in the image: for every `G'` admissible there is
> an admissible `G` with `GramPhaseEquiv (Φ̂ G) G'`.

**"Where appropriate" is made precise here rather than left to the execution.** On a finite set
injectivity and surjectivity coincide, and it would be convenient to state `L3` as one conjunct.
**`Ω_t` need not be finite**: it is a quotient of a set cut out by `RealizableGram` over a complex
matrix space, and nothing merged says it is finite at any configuration where the round works. So
the two conjuncts are **stated and reported apart**, and a verdict that reaches one is not reported
as reaching the other. Where a candidate's `Ω_t` **is** shown finite in the kernel at the frozen
configuration, the execution may derive one conjunct from the other and **records that it did so and
at which configuration**; it may not assume finiteness.

### `L4` — compatibility with the gauge/orbit quotient, in two parts

> **`L4d` — descent.** `Φ` respects act 12's `GramPhaseEquiv` in its argument:
> `GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')`.
> **`L4n` — representative-level gauge-naturality.** `Φ` lifts to representatives naturally under act
> 12's two-sided moves: for the constant and time-dependent in-fibre left moves of `LeftFibreGroup`
> and the strong and weak right gauges at `a₀`, the transition commutes with the merged
> transformation laws on `FibreGram` — act 12's `fibreGram_left_mul` and `fibreGram_mul_weak_apply`
> are the two laws it must commute with.

**`L4d` is the shared theorem's own hypothesis, and the freeze says so before the census.** The
theorem below assumes quotient-well-definedness, so `L4d` cannot be a further restriction on the
action class that theorem produces: **its honest rung status is `L4d-HYP`**, and the result note
reports it as a hypothesis and not as a discharged rung. Saying this **now**, before any survivor is
known, is what keeps it from being an excuse later.

**`L4n` is a genuine strengthening and is tested as one.** Descent says the transition is a function
on classes. Naturality says it comes from a move on representatives that the invisible gauge cannot
see. The second does not follow from the first, and act 18 named the alternative route explicitly:
its `LC3` discharged descent **by writing the candidate at orbit level**, precisely so that a
representative-level naturality proof would not be needed. **This round tests whether the
representative-level property is a restriction**, and records the result either way.

### `L5` — composition of independent systems, and the test it had to pass

> **`L5`.** At a **product configuration** — carriers `V = V₁ × V₂`, ancilla `A = A₁ × A₂`, anchor
> `a₀ = (a₀₁, a₀₂)`, and the visible family `Γ ((i₁,i₂), (j₁,j₂)) = Γ₁ (i₁, j₁) · Γ₂ (i₂, j₂)` — the
> transition **factorizes on product classes**: there are transition families `Φ₁` on `Ω(Γ₁, ·)` and
> `Φ₂` on `Ω(Γ₂, ·)` with `Φ̂ (G₁ ⊠ G₂) ≈ (Φ̂₁ G₁) ⊠ (Φ̂₂ G₂)` for every pair of admissible `G₁`, `G₂`,
> the equivalence being act 12's `GramPhaseEquiv` and `⊠` the product embedding on fibre-Gram tuples
> induced by the Kronecker product of admissible dilations.

**Nothing in that statement mentions unitary evolution, a generator, a one-parameter group,
continuity, a Hamiltonian or Schrödinger's equation.** Every object in it is the repository's own:
the Kronecker product of matrices, act 12's `FibreGram`, act 12's `GramPhaseEquiv` and act 12's
`RealizableGram`. The product visible family is the **pointwise product** of two visible families,
which is what the anchored readback of a Kronecker product of admissible dilations computes to, by
the same index-wise argument act 18's `prod_mem_unitaryGroup` and `prod_admissible` already carry for
the carrier–ancilla product.

#### The `L5` test, performed at drafting time and recorded here

**`L5` was admitted to the ladder only after passing the test the owner set**, which has two parts:
the condition must be **definable without referring to Schrödinger or unitary evolution as the
standard**, and both a **satisfying** and a **violating** candidate must be exhibitable on the same
terms. The test was run before this freeze was written, and both parts came out positive. **This is
the freeze's analysis and not a finding**: whether the two candidates behave as stated is for the
execution to prove or to refute, and the ladder's wording does not move either way.

- **Part (a), definability — PASSED.** The statement above is written entirely in the programme's own
  vocabulary. No standard of correctness external to the repository appears in it, and no condition
  of the ladder is stated as "agrees with quantum evolution" in any paraphrase.
- **Part (b), a satisfying candidate — PASSED, twice.** `ΦI`, the identity transition on classes —
  act 18's own `LC3` — satisfies `L5` with `Φ̂₁ = Φ̂₂ = id`, and it is manifestly not quantum evolution
  in any sense, which is what makes it the freeze's certificate that **`L5` does not presuppose the
  answer**. `ΦPP`, the transition induced by a **product permutation** `σ₁ × σ₂` of `V₁ × V₂`,
  satisfies it with `Φ̂₁ = Φ_{σ₁}` and `Φ̂₂ = Φ_{σ₂}`.
- **Part (b), a violating candidate — PASSED.** `ΦCTRL`, the **controlled relabelling**: on product
  classes, apply the carrier permutation `σ` to the second factor exactly when the first factor's
  class equals a named class `ω̄₁`, and leave the second factor alone otherwise; on classes that are
  not product classes, act as the identity. Its refutation of `L5` is finite and does not quantify
  over the whole orbit space: if `Φ̂ = Φ̂₁ ⊠ Φ̂₂` then `Φ̂₂` is a function of its own argument alone,
  and the two product classes `ω̄₁ ⊠ ω₂` and `ω₁' ⊠ ω₂` with `ω₁' ≠ ω̄₁` force `Φ̂₂ ω₂` to equal both
  `Φ_σ ω₂` and `ω₂`, which are inequivalent classes. **Two named instances close it.**

**So `L5` stays in the ladder, in the wording frozen above.** It was not weakened to survive the
test, and the no-post-hoc rule was not weakened to accommodate it. **Had either part failed, `L5`
would have been removed from the ladder and the round run on `L0`–`L4`**, which the owner records as
already constituting a meaningful rigidity experiment; the freeze states that branch so the reader
sees that the test had a real negative outcome available to it.

**One honest cost is recorded rather than hidden.** `L5` needs the product embedding `⊠` to be
well-defined on classes and to land in the realizable set — the Kronecker product of two admissible
dilations is admissible for the product family, its fibre-Gram tuple is the Kronecker product of the
factors' tuples, positive semidefiniteness is preserved and the rank bound multiplies to `|A₁|·|A₂|`.
That is construction work in the execution and it is named as such. **If the execution cannot
discharge it, `L5` is reported UNDECIDED and is NOT silently dropped**: the headline is then computed
over the conditions the kernel actually discharges, the headline label names that set explicitly, and
the round additionally records that the headline over the full ladder is undecided. **That fallback
is frozen here, before the census**, so that it is reporting and not repair.

### Each rung is tested as a genuine restriction, and the verdict labels say so

**A condition that every survivor satisfies for free is decoration, and the freeze refuses to report
decoration as a rung.** For each of `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4n` and `L5` the execution
reports exactly one of these three labels, and the label is earned and never assumed.

| label | what it says | earned only by |
| --- | --- | --- |
| `Li-RESTRICTS` | the rung is a genuine restriction on the class the shared theorem produces | an **exhibited** law satisfying every earlier rung and failing this one, at evidence level 2, with the failing conjunct and the separating class named |
| `Li-FREE` | the rung is **not** a restriction: every law satisfying the earlier rungs satisfies it | a **universal** kernel proof at evidence level 2 of the implication, over the configuration named |
| `Li-UNDECIDED` | neither was reached | the recorded statement that neither was reached, with the obstruction named — which rung, which conjunct, which step, and what would settle it |

**`L4d` carries the fourth label `L4d-HYP`**, and only `L4d`: it is the shared theorem's own
hypothesis, so neither `L4d-RESTRICTS` nor `L4d-FREE` is a meaningful verdict about it and neither is
claimed. **A `Li-FREE` is a finding and not a shortfall**: it says the rung was stated, tested, and
found to be implied, which is exactly the information "this ladder has six rungs and one of them does
nothing" carries.

**Neither label enlarges or shrinks the ladder.** A rung reported `Li-FREE` **stays in the ladder**
and stays in the conjunction the headline quantifies over. The ladder is not edited by its own
verdicts.

## The ordering obligation — the mechanical teeth of the no-post-hoc rule

**The rule.** If reversibility plus composition plus quotient naturality still leaves many laws, the
round records `L-FAMILY` or `L-WIDE`. It does **not** add "one more physically reasonable condition"
after seeing the survivors. **The candidate condition set `L0`–`L5` is frozen before any census of
surviving laws is run, and cannot be edited after the first discriminating search or proof attempt
has exposed which laws survive.**

**The obligation, in its exact frozen wording, which binds the execution:**

> **The ordering obligation.** The condition ladder `L0`–`L5` is fixed by this control-plane blob and
> by nothing else. The execution states each rung in its Lean module in the wording this file freezes
> for it, **before** it attempts any discriminating result; and from the moment the first
> discriminating result enters the execution branch, **no commit of that branch alters the statement
> of any rung, adds a rung, removes a rung, or changes the conjunction the headline quantifies
> over.** The first discriminating result is whichever of these enters the branch earliest: the first
> proof of the shared structural theorem, the first exhibited survivor of the ladder, the first
> exhibited failure of a rung, or the first witness or refutation of the discriminating test. **An
> execution that cannot demonstrate this ordering has not honoured it**, and the round is reported
> with the ordering obligation named as undischarged.

### What the execution must record to demonstrate it honoured the ordering

**Five records, each checkable by an auditor from the branch alone.** The result note carries all
five, and a missing record is a defect of the round and not a formality.

1. **The ladder table.** A table with one row per rung — `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d`,
   `L4n`, `L5` — giving for each the Lean declaration that states it and the section of this file
   that freezes it. **A condition stated in the module that this file does not freeze is a defect of
   the round**, and so is a rung of this file with no declaration.
2. **The ladder commit.** The SHA of the commit on the execution branch at which every rung's Lean
   statement is present, together with the statement that **no discriminating result is present at
   that commit**: no proof of the shared theorem, no census, no survivor, no rung failure, no
   discriminating witness. An auditor checks with `git show` and `git diff` against the mandated
   base.
3. **The discrimination commit.** The SHA of the commit at which the first discriminating result
   entered the branch, named as such, with which result it was.
4. **The immutability span.** The statement, with the command that checks it, that between the
   discrimination commit and the certified head `E` **no diff touches any rung's statement**:
   `git diff <discrimination commit> <E> -- verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean`
   restricted to the declarations named in record 1 is empty. The result note prints the command and
   its result.
5. **The quotient record.** The statement that the only equivalences used in any verdict are the
   three on this freeze's frozen quotient list, with the declaration or lemma that uses each, and the
   statement that **no equivalence was introduced or widened during execution**. Where the execution
   noticed a candidate new equivalence it is recorded as an observation, named as not applied, and
   assigned to a later round.

**And, where the round reaches `L-FAMILY` or `L-WIDE`, the result note carries this sentence and the
round adds no condition:**

> The surviving class is what the frozen conditions leave. **No condition was added after the
> survivors were known, and no equivalence was widened after the survivors were known.** The ladder
> stands as this round's control plane froze it, and a condition that would narrow the survivors
> belongs to a later round with its own freeze.

### The two rescue routes are closed together

**Once discrimination begins, neither a new condition nor a new equivalence may be introduced to
convert a plurality into rigidity.** The symmetry is the point and is stated so that it is visible:
**adding a condition narrows the survivors; widening the quotient merges them.** Both turn
`L-FAMILY` or `L-WIDE` into `L-RIGID` after the fact, both are the same manoeuvre in different
clothes, and both are forbidden by the same rule and for the same reason.

- **The condition route** is closed by the ordering obligation above and by its five records.
- **The equivalence route** is closed by the frozen quotient list, which names the three equivalences
  any verdict may use and forbids every other.

**What a surviving plurality yields is `L-FAMILY` or `L-WIDE`, and those are preregistered outcomes
at full evidence bar.** Neither is a failure, neither is a fallback, and neither is a reason to reach
for a rescue.

## The shared structural theorem, which RUNS FIRST — `OL1`

**This target runs before the census and before the discriminating test**, and both depend on its
outcome in a way this freeze fixes in advance. It is assumption-light and structural, and it is what
turns "a law that propagates" into "an action on a state space", which is the object the ladder's
rungs are conditions on.

> **`OL1` (a), the general form.** Any `L-PROP` law that is quotient-well-defined (`L4d`) and
> compositional (`L2`) **descends to a composition of maps on the admissible orbit spaces**: there
> are functions `Φ̄_t : Ω_t → Ω_{t+1}`, well defined on `GramPhaseEquiv`-classes, such that a
> pointwise realizable trajectory `𝔾` solves the law iff `[𝔾 (t+1)] = Φ̄_t [𝔾 t]` at every `t`; and
> the evolution from the initial orbit is the composite `E_t = Φ̄_{t-1} ∘ ⋯ ∘ Φ̄_0`, a function of the
> initial class alone.

> **`OL1` (b), the homogeneous form.** At a **time-homogeneous** visible family — `Γ t = Γ₀` at every
> `t`, so that `Ω_t = Ω_0 =: Ω` at every `t` — and with `L2`, the family is constant, `Φ̄_t = Φ̄`, and
> `E_t = Φ̄^t`. **So the law is a monoid action of `(ℕ, +)` on `Ω`**, that is, a semigroup action
> together with `E_0 = id`.

**Why the theorem is split in two, stated as the reason it is.** "Descends to an action/semigroup on
the admissible orbit space" is exactly right at a time-homogeneous configuration and is **not
literally stateable** at a general one: when `Ω_t` varies with `t` there is no single set for a
monoid to act on, and what one has is a composable family of maps between different sets — a
composition and not an action. **Writing (b) as though it held generally would overstate the
theorem**, and writing only (a) would lose the statement the round actually wants. Both are frozen,
both are reported, and the result note says which configurations each was proved at.

**What `OL1` is NOT.** It is **not** a statement that such a law exists — act 18 supplies that, and
this round consumes it. It is **not** a statement that the action is faithful, transitive, free,
continuous or by any kind of symmetry. It is **not** a statement about laws that fail `L2` or `L4d`,
about which it says nothing in either direction. And it is **not** a bridge to any representation
theory: no statement of this round realizes `Φ̄` as a group element, a unitary, an operator or a
generator, and the non-doings forbid it in terms.

**The `TJ1` dependence is named at the step and not in a footnote.** Reading the solution set as a
composition of maps on per-time state spaces requires the ambient admissible set to be the **product
over time** of those spaces, which is act 17's `TJ1` and is not a general fact about trajectory sets.
The execution cites `TJ1` at exactly that step, as act 18's `XS1` did at its own.

**The `OL1` dependency, frozen in both directions.**

> **If `OL1` lands**, the ladder's rungs are conditions on the induced maps `Φ̄`, the census is run
> over transition families, and the discriminating test compares two induced evolutions from one
> initial class. **If `OL1` does not land**, the ladder's rungs are stated of the representative-level
> transition family `Φ` with its descent conjunct, the census runs unchanged against that object, and
> the round records the shared theorem as UNDECIDED with the obstruction named. **Nothing about the
> ladder, the candidate list, the discriminating test or the headline labels changes in either
> case** — only the object the rungs are read of, and the result note says which it was.

## The three headline outcomes

**Three settling outcomes, exhaustive of what the round can settle**, plus the UNDECIDED label every
round of this programme carries. They are mutually exclusive by the obligations below and no two can
be claimed together.

| line | outcome | statement |
| --- | --- | --- |
| rigid | **`L-RIGID`** | all laws satisfying the frozen conditions coincide up to the already-recognized equivalence |
| family | **`L-FAMILY`** | the surviving class is nontrivial and **structurally characterizable**: exhibited **and** characterized |
| wide | **`L-WIDE`** | the conditions fail to narrow the class enough for such a characterization to be reached |
| otherwise | **`L-UNDECIDED`** | none of the above was reached, with the obstruction named specifically |

**`L-UNDECIDED` is recorded as a live preregistered outcome and not as a failure**, exactly as every
round from act 10 onward records it. The owner's framing names three outcomes as exhaustive; the
freeze reads that as exhaustive **of the settling outcomes**, and says so here rather than letting an
execution discover it, because a round that cannot reach a settling outcome must have a label for
what it did reach.

### `L-RIGID`, and the quotient it is taken modulo

> **`L-RIGID`, stated symbolically.** `∀ Γ a₀ Φ Φ'`, both satisfying the frozen ladder at the
> configuration, `∀ 𝔾 𝔾'` pointwise realizable with `Law_Φ 𝔾` and `Law_{Φ'} 𝔾'` and
> `GramPhaseEquiv (𝔾 0) (𝔾' 0)`: `GramTrajEquiv 𝔾 𝔾'`.

**Earned only by** a universal kernel proof at evidence level 2 over the configuration named, quotient
taken over the equivalences on the **frozen quotient list** and over no other. A proof that reaches
uniqueness only after adopting an equivalence outside that list **does not earn `L-RIGID`**, and what
it earns is `L-FAMILY` or `L-WIDE` with the candidate equivalence recorded as an observation.

### The `L-FAMILY` / `L-WIDE` boundary is the characterization theorem

**The two outcomes blur after the fact unless the boundary is fixed before it, so the boundary is
fixed here and it is a single object: the characterization theorem.**

> **`L-FAMILY` is earned only by a BOTH-DIRECTIONS characterization**, at evidence level 2, naming a
> parameter set `P` written from `(a₀, Γ)` and the merged record's own objects alone, and a family
> `p ↦ Φ_p`, such that: **(i)** every `Φ_p` satisfies the frozen ladder at the configuration; and
> **(ii)** every transition family satisfying the frozen ladder at the configuration generates a law
> `≈_L` to `Law_{Φ_p}` for some `p ∈ P`. Together with at least two `p`, `p'` whose laws are **not**
> `≈_L`, with the separating class and invariant named.

> **`L-WIDE` is earned by** at least two `≈_L`-inequivalent survivors exhibited at evidence level 2,
> **and no such characterization reached**, with the obstruction to direction (ii) named
> specifically — which step, over what the universal quantifier ranges, and what would settle it.

**Direction (ii) is the one that cannot be skipped, and the freeze says so in terms.** **Two exhibited
survivors earn `L-WIDE`, never `L-FAMILY`.** Pointing at two examples and calling the residue a
family is precisely the report this boundary exists to prevent: a shapeless residue is what `L-WIDE`
names, and naming it `L-FAMILY` would claim a classification the round did not do.

**And the boundary cuts the other way too.** A round that proves both directions and then reports
`L-WIDE` because the parameter set is large is **defective**: **`L-WIDE` is the absence of a
characterization, not the presence of a big one.** A large but characterized class is `L-FAMILY`, and
the result note says how large it is inside that verdict.

**A restatement is not a characterization.** A parameter set `P` whose membership condition is the
frozen ladder itself, or any paraphrase of it — "`P` is the set of transition families satisfying
`L0`–`L5`" and its variants — does **not** earn `L-FAMILY`. `P` must be written from `(a₀, Γ)` and
the merged record's own objects, and its membership must be checkable without consulting the ladder.
**The result note states in terms why its `P` is not a restatement**, and a `P` that is one is
reported as `L-WIDE` with the obstruction named.

## The decisive countercontrol — the same-initial-orbit pair at its FIRST divergence

**This is the discriminating test, and it is frozen with its quantifiers written symbolically.**

> **`SIOP`, the same-initial-orbit pair, exhibited at its FIRST divergence.**
>
> `∃ Γ a₀ Φ Φ' 𝔾 𝔾' t*,`
> `  LadderConds a₀ Γ Φ  ∧  LadderConds a₀ Γ Φ'  ∧  ¬ (Law_Φ ≈_L Law_{Φ'})`
> `  ∧ (∀ t, RealizableGram A (Γ t) (𝔾 t))  ∧  (∀ t, RealizableGram A (Γ t) (𝔾' t))`
> `  ∧ Law_Φ 𝔾  ∧  Law_{Φ'} 𝔾'`
> `  ∧ 1 ≤ t*`
> `  ∧ (∀ s, s < t* → GramPhaseEquiv (𝔾 s) (𝔾' s))`
> `  ∧ ¬ GramPhaseEquiv (𝔾 t*) (𝔾' t*)`

**The earlier-agreement conjunct is what makes `t*` the FIRST divergence, and it is part of the
witness and not commentary on it.** A difference at a later time caused merely by feeding
already-different states forward is **not primitive non-uniqueness** — it is the same divergence
propagated, and reporting it as the discriminating witness would overstate what was found.

**A clean first-divergence formulation IS available here, and the reason is worth stating.** `ℕ`
carries successor and order, and it is well-ordered; so a pair of trajectories that differ at all has
a **least** time at which they differ, and `∀ s < t*` is the statement that `t*` is it. **Nothing
beyond successor and order is used** — no continuity, no limit, no metric on the index — so the
formulation costs nothing the index type does not already have. The freeze therefore does **not** fall
back to "differ at some time", and a result note that reports a witness at `t* ≥ 2` **without** the
earlier-agreement conjunct has reported a propagated divergence as a primitive one, which is a defect
of this round.

**The strongest case is `t* = 1`, and the freeze names it.** At `t* = 1` the earlier-agreement
conjunct reduces to agreement at time `0`, which is the same-initial-orbit hypothesis itself: the two
laws are handed the same initial orbit and disagree at the very next step. That is primitive
non-uniqueness in the plainest available sense, and the countercontrol table names a predicted
witness at exactly `t* = 1`.

**What each answer means, frozen.**

- **`SIOP-YES`** — such a pair exists and is exhibited. **Rigidity is cleanly falsified**, and the
  headline is `L-FAMILY` or `L-WIDE` according to whether the characterization of the surviving class
  is reached.
- **`SIOP-NO`** — no such pair can exist, by theorem: the negation of the displayed statement is
  proved universally at the configuration named. **That is the meaningful `L-RIGID` result**, and it
  is what earns the rigid line.
- **`SIOP-UNDECIDED`** — neither was reached, with the obstruction named specifically. **Searching and
  not finding earns nothing**: the absence of an exhibited pair is **not** `SIOP-NO`.

**`SIOP-NO` and `L-RIGID` are the same statement read two ways**, and the freeze records the
equivalence so that neither is claimed without the other: the displayed `L-RIGID` statement is the
negation of `SIOP`'s trajectory conjuncts under the ladder hypothesis, with the first-divergence
conjunct dropped because a first divergence exists whenever any divergence does. The execution proves
one and reports both, naming which it proved.

## The frozen candidate law list

**Seven named transition families. The list is closed at this freeze.** Each is stated in the
programme's vocabulary, with its provenance named and its role on the ladder fixed. A candidate
discovered during execution is **recorded as an observation and not executed**, and belongs to a
later round with its own freeze.

**The frozen configuration for the single-carrier candidates** is act 12's: `V = Fin 4`, `A = Fin 1`,
`a₀ = 0`, `Γ ≡ ¼`, with act 12's frozen Hadamard family
`H(z) = ½ · [[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]`. **The frozen product configuration** is
`V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0,0)`, `Γ ≡ 1/16` — the pointwise product of two
copies of `Γ ≡ ¼`, constant and therefore invariant under every permutation of the product carrier.

### `ΦI` — the identity transition

> **Statement.** `Φ̂ G = G`. The law it generates is `∀ t, GramPhaseEquiv (𝔾 (t+1)) (𝔾 t)` — the
> trajectory's orbit class is constant in time.

**Where it comes from.** It is **act 18's `LC3`**, the generator law that carried act 18's `L-PROP`,
with its descent obligation discharged at orbit level by that round. It is consumed here as a merged
instance and is **not rebuilt**. **Its role: the baseline survivor**, predicted to satisfy every rung.

### `ΦP` — the carrier-relabelling transition

> **Statement.** For a permutation `σ` of `V` under which `Γ` is invariant — `Γ t (σ i) (σ j) = Γ t i
> j` at every `t` — `Φ̂ G i = (G (σ i)) ∘ σ`, the simultaneous relabelling of the fibre index and of
> both matrix indices by `σ`.

**Where it comes from, and why it is a law datum.** `σ` is chosen before any lift exists and consults
no lift, which is what act 18's definition of a law datum requires; it is not required to be a
canonical function of `Γ`, and act 18's `LC1` and `LC2` already take data in that sense. At the frozen
configuration `Γ ≡ ¼` is constant, so **every** permutation of `V` leaves it invariant. **Its role:
the second survivor**, and with `ΦI` the predicted `SIOP` witness.

**The separating computation the freeze names in advance.** Act 18 already exhibited, for its `LC2`
clause (i) failure, that the class of `H(1)` and the class of `H(1)` **with its last two columns
interchanged** are `∼_D`-inequivalent, certified through act 12's merged `∼_D`-invariant read at the
fibre pair `(0,2)`, where the values are `1/16` and `−1/16`. **That is a merged, already-exhibited
separation** and it is the one the countercontrol table uses. This is written here as the freeze's
**reason**, and it is **analysis, not a finding**.

### `ΦX` — the restricted-initial transition

> **Statement.** `Law 𝔾 ≡ (∀ t, GramPhaseEquiv (𝔾 (t+1)) (𝔾 t)) ∧ (GramPhaseEquiv (𝔾 0) (G(H(1))) ∨
> GramPhaseEquiv (𝔾 0) (G(H(i))))` — the identity transition, admitted only through two named initial
> classes.

**Where it comes from.** It is act 18's `LC0` law datum — the two-class pointwise condition — conjoined
with a genuinely cross-time constancy requirement. **It is not pointwise**, so act 18's `XS1` says
nothing about it in either direction, and the freeze says so rather than leaving it to be rediscovered.
**Its role: the `L0` countercontrol.** It is an `L-PROP` law — nonempty, non-singleton modulo `≈_O`,
proper against the constant trajectory at `[G(H(−1))]`, uniqueness from the initial orbit, and the
initial orbit contributing at `t = 1` — while an admissible initial class outside the two named admits
no solution at all, so `L0`'s totality fails.

### `ΦC` — the constant transition

> **Statement.** For a named admissible class `ω₀`, `Φ̂ G = G₀` where `G₀` is a named representative of
> `ω₀`, at every `G`.

**Where it comes from.** It is the crudest evolution that is still an evolution: every state is sent
to one state. **Its role: the `L3i` countercontrol.** It is total, admissibility-preserving,
time-homogeneous and descending — the image being a single class, descent is immediate — while it is
injective on classes only if `Ω` has one class, which act 12's merged inequivalences refute at the
frozen configuration.

### `ΦT` — the time-inhomogeneous alternation

> **Statement.** `Φ t = ΦI` when `t` is even and `Φ t = ΦP` when `t` is odd, with `σ` the column
> transposition the `ΦP` entry names.

**Where it comes from.** It is the least contrived failure of one law iterating consistently: two
perfectly good transitions, applied in alternation. **Its role: the `L2` countercontrol.** It is
total, admissibility-preserving, reversible and descending at every `t`, while no single `Φ̂` equals
`Φ t` at every `t`, which act 18's already-exhibited class separation certifies.

### `ΦPP` — the product permutation transition

> **Statement.** At the frozen product configuration, `Φ̂ = Φ_{σ₁ × σ₂}` for permutations `σ₁` of `V₁`
> and `σ₂` of `V₂`, acting as `ΦP` does with the product permutation.

**Where it comes from.** It is the `L5` satisfying candidate that is **not** the identity, so that
`L5`'s satisfaction is witnessed by something with content. **Its role: the `L5` satisfying
candidate**, with `Φ̂₁ = Φ_{σ₁}` and `Φ̂₂ = Φ_{σ₂}` as the factorization.

### `ΦCTRL` — the controlled relabelling

> **Statement.** At the frozen product configuration, with `ω̄₁` a named class in `Ω(Γ₁)` and `σ` a
> permutation of `V₂`: on a product class `ω₁ ⊠ ω₂`, `Φ̂ (ω₁ ⊠ ω₂) = ω₁ ⊠ (Φ_σ ω₂)` if `ω₁ = ω̄₁`, and
> `ω₁ ⊠ ω₂` otherwise; on a class with no product representative, `Φ̂` is the identity.

**Where it comes from, and why it is a law datum and not a dynamical assumption.** It is written from
the product configuration's own data — a named class and a named permutation — and consults no lift.
It is the leanest statement of "what happens to the second system depends on the first", which is what
`L5` is about, and **it names no interaction, no Hamiltonian, no coupling constant and no evolution
operator**. **Its role: the `L5` violating candidate**, refuted against `L5` by the two-instance
argument recorded in the `L5` test above.

**Well-definedness on classes is an obligation of this candidate and not an assumption.** "Has a
product representative" must be shown `GramPhaseEquiv`-invariant, which it is by construction — the
property is stated of the class — and the execution discharges it explicitly. Where it cannot,
`ΦCTRL` is reported UNDECIDED with the obstruction named, and `L5`'s rung status falls to
`L5-UNDECIDED` rather than to `L5-FREE`: **the absence of an exhibited violator is not a proof that
none exists.**

## The witness supply, FROZEN

**Every witness of this round is drawn from this supply, and the configuration for each obligation is
named in the countercontrol table below, in advance.** A configuration chosen after an outcome is
known is a preregistration failure in miniature, and an alternative witness found during execution is
**recorded as an observation and never substituted**.

1. **Act 12's Hadamard objects** at `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼`, with the frozen
   family `H(z)` and the merged admissibility and inequivalence of `H(1)`, `H(i)` and `H(−1)`. Act
   17's `hadamard_constant_lifts` supplies the constant coherent lifts, and act 12's merged
   `∼_D`-invariant `G^{(0)}_{10} · G^{(1)}_{01}` takes the value `z/16` on `H(z)`.
2. **Act 18's fourth admissible dilation** — `H(1)` with its last two columns interchanged — whose
   class act 18 exhibited as `∼_D`-inequivalent to that of `H(1)`, certified through the same merged
   invariant read at the fibre pair `(0,2)`, values `1/16` and `−1/16`.
3. **Act 12's `sh1_sufficiency` and act 17's `tj1_sufficiency`**, which realize any pointwise
   realizable tuple and any pointwise realizable assignment by an admissible dilation and by a
   coherent lift respectively, at any finite `|A|` satisfying the rank bound. This is what discharges
   the admissibility side of every trajectory this round names by its per-slice classes.
4. **Act 18's `prod_mem_unitaryGroup` and `prod_admissible`**, the index-wise product statements,
   consumed as the merged starting point for the product configuration's admissibility.
5. **The moves of acts 11, 12 and 13**: the constant and time-dependent in-fibre left moves of
   `LeftFibreGroup`, and the strong and weak right gauges at `a₀`, with their merged transformation
   laws on `FibreGram` — which is what `L4n` is stated against.

**The one-`|A|`-value caveat, carried from act 18 and recorded again.** Act 12's `|A| = 1` is the
strongest case for the per-slice statements and is not degenerate there. **It is not automatically the
right case for a cross-time statement**, and act 18 recorded the concrete instance where it collapsed
one. Where a countercontrol of this round needs `|A| ≥ 2` the table says so.

## The countercontrols, one per rung and one per candidate

**A negative result is reportable because its shape was fixed before the search.** For each rung and
each candidate the freeze states here what a negative answer looks like concretely and what evidence
earns it.

**Evidence that earns any countercontrol**: a Lean theorem at evidence level 2 whose statement pins
the objects by equations, discharges admissibility from merged results, and certifies the separating
quantity at a named index through a named invariant. **Searching and not finding earns nothing.**

| rung or target | the countercontrol this freeze names | configuration |
| --- | --- | --- |
| `L0` | `ΦX`: an admissible initial class outside the two it names — the class of `H(−1)`, pointwise realizable by act 12's merged `sh1_necessity` — admits no solution, so totality fails while act 18's two propagation clauses hold | supply 1 and 3, `\|A\| = 1` |
| `L1` | **none named, and the freeze predicts `L1-FREE`**: on the class the shared theorem produces, every value of the induced evolution is the class of a pointwise realizable trajectory's slice, so admissibility is inherited. The freeze names no violating candidate and rates the rung accordingly | any |
| `L2` | `ΦT`: no single `Φ̂` equals `Φ t` at every `t`, certified at `t = 0` against `t = 1` through act 18's exhibited class separation | supply 1 and 2, `\|A\| = 1` |
| `L3i` | `ΦC`: two `∼_D`-inequivalent admissible classes — those of `H(1)` and `H(i)`, by act 12's merged `hadamard_slices_not_twoSided` — have the same image, so injectivity on classes fails | supply 1, `\|A\| = 1` |
| `L3s` | `ΦC`: the image is the single class `ω₀`, and the class of `H(i)` is admissible and outside it, so surjectivity fails | supply 1, `\|A\| = 1` |
| `L4d` | **not a rung with a countercontrol**: it is the shared theorem's hypothesis and is reported `L4d-HYP` | — |
| `L4n` | **named and expected hard**: a transition descending to classes with no gauge-natural representative-level lift. The freeze names no construction and rates it accordingly; **UNDECIDED with the obstruction named is an allowed outcome and is not a shortfall** | supply 5 |
| `L5` | `ΦCTRL`: the two product classes `ω̄₁ ⊠ ω₂` and `ω₁' ⊠ ω₂` force a putative second factor `Φ̂₂` to equal both `Φ_σ` and the identity on `ω₂`, which are `∼_D`-inequivalent by act 12's merged inequivalence | supply 1, 3 and 4, product configuration |
| `OL1` (a) | discharged by reading act 18's `PropagatesFrom` clause (i) as the well-definedness of `Φ̄_t` on classes, with `TJ1` cited where the ambient set must be a product | any |
| `OL1` (b) | discharged at a time-homogeneous `Γ`; at a non-homogeneous `Γ` the monoid statement is **not attempted** and the freeze says so in advance | frozen configuration |
| `SIOP` | `ΦI` against `ΦP` with `σ` the column transposition of supply 2, from the initial class of `H(1)`: at `t* = 1` the `ΦI`-solution is at `[G(H(1))]` and the `ΦP`-solution at the class of supply 2's dilation, `∼_D`-inequivalent through the merged invariant at the fibre pair `(0,2)`, values `1/16` and `−1/16`; the earlier-agreement conjunct is agreement at time `0`, which is the hypothesis | supply 1, 2 and 3, `\|A\| = 1` |
| `L-FAMILY` direction (ii) | **named and expected hard**: the universal statement that every ladder-satisfying transition family is `≈_L` to a named `Φ_p`. The freeze names no construction and rates it accordingly; `L-WIDE` with the obstruction named is an allowed outcome and is **not** a shortfall | frozen configuration |

**One witness family, several consequences — reported as one witness and its consequences.** Act 12's
Hadamard objects and act 18's fourth dilation carry most of the table. The execution reports that as
**one merged witness family and the consequences this round draws from it**, and never as several
independent findings.

**The countercontrols consume merged witnesses; they do not enlarge them.** Act 12's `TG3` is
existential about its own exhibited dilations, act 12's `SH1` is the per-slice characterization at its
own strength, act 17's `TJ1` is the product characterization it is, and act 18's `L-PROP` is a verdict
about `LC3`. None is enlarged, restated or revised by anything here.

## The evidence rule, FROZEN

`OL0` is settled by **locating and quoting**, not by proving a theorem. Its evidence rule is frozen
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

**Searching and not finding is never a settling outcome.** This binds the Lean targets as well as
`OL0`. No line of the headline is earned by the absence of a witness: `L-RIGID` requires a universal
proof and is **not** earned by failing to find a `SIOP` pair, and a rung is **not** reported
`Li-FREE` because no violating candidate was found.

**The bounded search for `OL0` is fixed now**, so that its boundary cannot be chosen after its result
is known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/` and under
  `verification/lean/`; every `preregistration.md` and `result.md` under
  `verification/programmes/oi-qm/`; and `verification/ROADMAP.md`. The set is taken from
  `git ls-tree -r --name-only B`, so untracked package trees are outside it by construction.
- **The search terms**: `PropagatesFrom`, `PointwiseLaw`, `GramTrajEquiv`, `GramPhaseEquiv`,
  `RealizableGram`, `CoherentLift`, `rigid`, `unique`, `semigroup`, `monoid`, `action`, `homogene`,
  `reversib`, `invert`, `composit`, `factoriz`, `classif`, and the merged label names `TJ1`, `TJ3`,
  `XS1`, `LC3`, `CT2`, `SH1`, `TG2`, `TG3`, `GL2`, `L-PROP`.
- **The question asked of each hit**: does this declaration decide, for the class of cross-time laws
  that propagate in act 18's frozen sense, whether two such laws satisfying any structural conditions
  must agree — or does it decide, for any such law, whether it is unique, whether it composes, whether
  it is reversible, or whether it factorizes over independent systems?
- **The recorded answer per hit** is one of: *supplies it* (quoted, with coordinate); *does not
  supply it, and why* (quoted, with coordinate); or *not relevant to the question*.

The execution records the search in the result note in full. **A search that finds a decision is a
finding, and a search that does not is equally a finding** — the second being that the record is
silent on the point, which is what `OL0` asks.

**One property of the file set is recorded in advance rather than repaired later.** This round's own
control plane is inside the set by construction, being a `preregistration.md` under
`verification/programmes/oi-qm/` at `B`. **Its hits are recorded as not relevant to the question**:
the freeze is this round's own specification and is not a decision of the merged record. The boundary
is fixed here and is not moved during execution, exactly as act 18 recorded for its own.

## The targets, FROZEN

Six targets, `OL0` through `OL5`. Each names what settles it and what evidence counts.

### `OL0` — does the merged record decide the rigidity question, in either direction?

**The question.** At this freeze's base, does the merged record contain any statement — universal or
existential — deciding whether two cross-time laws propagating in act 18's frozen sense must agree,
or deciding, for any such law, whether it is unique, total, reversible, compositional or factorizing?

**What settles it.** The bounded search frozen above, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule if a decision is found. Rule 3 if none is
found — the recorded statement that the passage sought does not exist on the named and bounded
search, with the per-term record.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `OL0`**, and no outcome of `OL0` is a theorem
of this round. **Nor is it a licence to treat this round's own theorems as retro-evidence about it.**

### `OL1` — the shared structural theorem, which runs first

**The statement.** As frozen above, in its two parts (a) and (b), with `TJ1` cited at the step where
the ambient admissible set has to be a product.

**What settles it.** A Lean theorem at evidence level 2 for each part, consuming act 17's merged
`tj1_sufficiency` and `tj1_trajectory_set`, act 12's `SH1`, and act 18's `PropagatesFrom` at their own
strengths.

**Bounded reading, frozen.**

- **Part (b) is stated at time-homogeneous configurations only**, and the freeze says so before the
  proof rather than after: at a general `Γ` there is no single set for a monoid to act on.
- **It is a descent statement and not an existence statement.** That an `L-PROP` law exists is act
  18's and is consumed.
- **It says nothing about faithfulness, transitivity, freeness or any symmetry property** of the
  induced action, and no artifact of this round claims one.
- **It builds no bridge to representation theory.** `Φ̄` is a function on classes and is realized as
  no operator, unitary, generator or group element anywhere in this round.

### `OL2` — the per-rung status of the ladder

Eight parts, predicted and reported separately: `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d`, `L4n`, `L5`.
Each carries one of the labels `Li-RESTRICTS`, `Li-FREE` or `Li-UNDECIDED`, except `L4d` which carries
`L4d-HYP`.

**What no `OL2` verdict establishes.** A verdict on one rung is not a verdict on another. An
`Li-RESTRICTS` is **not** an endorsement of the rung: it says the rung has content, and says nothing
about whether it is the right condition to impose. An `Li-FREE` is **not** a criticism of the rung and
**not** a licence to drop it — the rung stays in the ladder and stays in the conjunction the headline
quantifies over.

### `OL3` — the census of the frozen candidate list against the ladder

Seven parts, one per named transition family, each reported with which rungs it satisfies at the
configuration this freeze names for it, each at evidence level 2 or UNDECIDED with the obstruction
named.

**The census is over this freeze's closed list and is not a census of all laws.** A survivor of the
census is a survivor **on this list**; the universal direction over all ladder-satisfying families is
the `L-FAMILY` characterization's direction (ii) and belongs to `OL5`.

### `OL4` — the discriminating test

**The statement.** `SIOP`, as frozen above with its earlier-agreement conjunct, reported as
`SIOP-YES`, `SIOP-NO` or `SIOP-UNDECIDED`.

**What settles it.** For `SIOP-YES`, an exhibited pair at evidence level 2 with `t*` named and the
earlier-agreement conjunct proved. For `SIOP-NO`, a universal kernel proof of the negation at the
configuration named. For `SIOP-UNDECIDED`, the recorded statement with the obstruction named.

### `OL5` — the headline

**The statement.** One of `L-RIGID`, `L-FAMILY`, `L-WIDE` or `L-UNDECIDED`, earned as the obligations
above require, over the conditions the kernel actually discharged, with that set named in the label.

**The label carries its condition set explicitly.** Where every rung was discharged the headline reads
`L-FAMILY (L0–L5)` or its analogue; where `L5` was reported UNDECIDED it reads `L-WIDE (L0–L4)`, with
the additional record that the headline over the full ladder is undecided. **This is fixed here,
before the census, so that it is reporting and not repair.**

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `OL0` | **negative** — the record is silent on the rigidity of the propagating class | **high** | A pre-freeze reading of the file set named in the evidence rule found act 18's `L-PROP` to be a verdict about `LC3` and about nothing in its neighbourhood, act 18's `XS1` to be a no-go bounded to pointwise laws, and acts 12, 13 and 17 to be about the per-slice classification, the threading residual and the ambient trajectory set. Nothing states how many laws propagate. The reading is the freeze's **reason**, not a finding: `OL0`'s finding is whatever the execution's own bounded search records. |
| `OL1` (a) | positive | **high** | Act 18's `PropagatesFrom` clause (i) is exactly the well-definedness of `Φ̄_t` on classes, and the splice-free direction needs only act 17's merged `tj1_trajectory_set` to make the ambient set a product. No new construction is required. |
| `OL1` (b) | positive at a time-homogeneous `Γ` | **high** | Independence of `t` plus descent gives `E_t = Φ̂^t` by induction. The frozen configuration is time-homogeneous by construction, `Γ ≡ ¼` at every `t`. |
| `L0` | **`L0-RESTRICTS`**, via `ΦX` | **medium** | The three-part `L-PROP` check for `ΦX` runs through act 12's Hadamard family and act 17's `tj1_sufficiency`, and totality fails at the class of `H(−1)`. The medium rating is for the kernel bookkeeping of the `L-PROP` conjuncts, not for the argument. |
| `L1` | **`L1-FREE`** | **medium** | Every value of the induced evolution is a slice of a pointwise realizable solution, so admissibility is inherited; the medium rating is for stating the implication for the relation on the whole orbit space rather than only along solutions, which is the strictly stronger reading `L1` is frozen at. **UNDECIDED with the obstruction named is an allowed outcome.** |
| `L2` | **`L2-RESTRICTS`**, via `ΦT` | **high** | The separation is act 18's own exhibited class inequivalence, read at `t = 0` against `t = 1`. |
| `L3i` | **`L3i-RESTRICTS`**, via `ΦC` | **high** | Two merged-inequivalent classes with one image. The inequivalence is act 12's `hadamard_slices_not_twoSided`, merged. |
| `L3s` | **`L3s-RESTRICTS`**, via `ΦC` | **high** | The image is one class and a second admissible class exists, by the same merged inequivalence. |
| `L4d` | **`L4d-HYP`** | — | It is the shared theorem's hypothesis and no rung verdict is meaningful for it. Reported as a hypothesis, not as a discharged rung. |
| `L4n` | not predicted | **low** | Both predicted survivors have obvious representative-level lifts — the identity, and the column permutation — so neither witnesses a restriction; and the freeze names no transition descending to classes without a gauge-natural lift. **UNDECIDED with the obstruction named is an allowed outcome and is the freeze's expectation.** |
| `L5` | **`L5-RESTRICTS`**, via `ΦCTRL` | **medium** | The two-instance refutation is finite and does not quantify over the orbit space. The medium rating is for the product-embedding construction the rung needs — that the Kronecker product of admissible dilations is admissible for the product family and that its fibre-Gram tuple is the Kronecker product of the factors' — which act 18's `prod_admissible` starts but does not finish. **`L5-UNDECIDED` is an allowed outcome and is not a shortfall.** |
| `OL3`, the census | **`ΦI` and `ΦP` survive every rung at the frozen configuration; `ΦX`, `ΦC` and `ΦT` each fail the rung they are named for; `ΦPP` satisfies `L5` and `ΦCTRL` fails it** | **medium** | Each is the countercontrol table's own entry. The medium rating is for the `L-PROP` conjuncts of `ΦP`, which the freeze reads as following from `σ² = id` and act 12's merged inequivalences but which no merged result states. |
| `OL4`, the discriminating test | **`SIOP-YES`**, at `t* = 1`, via `ΦI` against `ΦP` | **medium** | Both are predicted survivors; they are handed the same initial class, that of `H(1)`; and at `t = 1` they sit at classes act 18 already exhibited as `∼_D`-inequivalent. The medium rating is for `ΦP`'s ladder conjuncts, not for the separation, which is merged. |
| `OL5`, the headline | **`L-WIDE (L0–L5)`** | **medium** | Conditional on `SIOP-YES`, which rules out `L-RIGID`, and on direction (ii) of the characterization **not** being reached: the universal quantifier there ranges over every transition family satisfying the ladder, and neither the freeze nor the merged record supplies a handle on that class. **`L-FAMILY` is preregistered as reachable** — at the product configuration the ladder with `L5` plausibly cuts the survivors down to the product permutations, which would be a genuine characterization — and that branch is rated **not predicted, at low-to-medium**. `L-RIGID` is preregistered as reachable and is rated **low**, for the reason the `SIOP` prediction gives. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named specifically.

**What this table's shape says, stated plainly.** The freeze predicts, at medium, that the class of
propagating cross-time laws is **not rigid** — that two laws satisfying every condition on the frozen
ladder can be handed the same initial orbit and disagree at the very next step — and that the
surviving class is **too wide for this round to characterize**. **That is the freeze's substantive
position**, and it is an uncomfortable one to preregister: it predicts that the round's own ladder,
assembled in good faith from the conditions one would think to impose, does not pin the law. The round
is worth running because that position is testable, because `L-RIGID` and `L-FAMILY` are both
preregistered as reachable at full evidence bar, because `OL1` is a theorem whichever way the headline
falls, and because the per-rung verdicts say which conditions have content and which are decoration —
information the record does not currently carry at all.

**And the freeze rates its own position at medium and not higher**, because `ΦP`'s ladder conjuncts
are not merged and because the product-configuration construction `L5` needs is real work that could
fail.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached. The
wording is fixed before the round runs so that no outcome can choose its own wording. **UNDECIDED is
a live preregistered outcome for every target and is not a failure**; where it is reached the frozen
sentence below is the report, with the obstruction named.

### The outcomes of `OL0`

- **Outcome `OL0`-silent** — the bounded search records that the passage sought does not exist:
  > On the search this freeze bounds — every `*.lean` file under `verification/lean-mathlib/` and
  > `verification/lean/`, every `preregistration.md` and `result.md` under
  > `verification/programmes/oi-qm/`, and `verification/ROADMAP.md`, against the frozen term list —
  > the merged record decides nothing about how many cross-time laws propagate in act 18's frozen
  > sense, and nothing about whether such a law is unique, total, reversible, compositional or
  > factorizing over independent systems. **The finding is that the record is silent on the point.**
  > It is not a finding that any such statement is false, not a finding that one is unprovable, and
  > not a bound on what a later round could prove.
- **Outcome `OL0`-found** — the search locates a deciding statement:
  > The merged record decides at least one of the questions this round asks, quoted verbatim above
  > with its coordinate, and the record says exactly which question it decides and for which objects.
  > Whether that statement settles the headline is the headline's own question and is not settled by
  > locating it. No merged artifact is edited, and no earlier round's recording is enlarged or
  > corrected.

### The outcomes of `OL1`

- **Outcome `OL1`-landed:**
  > An `L-PROP` law that is quotient-well-defined and compositional descends to a composition of maps
  > on the admissible orbit spaces, at evidence level 2, the ambient admissible set being a product by
  > act 17's merged `TJ1`; and at a time-homogeneous visible family the family of maps is constant, so
  > the law is a **monoid action of `(ℕ, +)`** on the admissible orbit space. **This is a descent
  > statement and not an existence statement**: that such a law exists is act 18's `L-PROP` and is
  > consumed here. It says nothing about faithfulness, transitivity, freeness or any symmetry property
  > of the induced action, it realizes the transition as no operator, unitary, generator or group
  > element, and the monoid form is stated at time-homogeneous configurations only, because at a
  > general visible family there is no single state space for a monoid to act on.
- **Outcome `OL1`-UNDECIDED:**
  > The descent was not reached in the kernel, with the obstruction named. **The ladder's rungs are
  > therefore read of the representative-level transition family with its descent conjunct**, the
  > census and the discriminating test run unchanged against that object, and act 18's `PropagatesFrom`
  > and act 17's `TJ1` stand as those rounds state them with nothing claimed from them here.

### The outcomes of `OL2`, per rung

- **Outcome `Li-RESTRICTS`**, for a named rung `Li`:
  > An exhibited transition family satisfies every earlier rung of this freeze's ladder and fails
  > `Li`, at evidence level 2, with the failing conjunct and the separating class named. **So `Li` is
  > a genuine restriction on the class the shared theorem produces and is not decoration.** This is a
  > statement about the exact condition frozen under the label `Li`, at the configuration named, and
  > it does **not** endorse the condition, does **not** say the programme requires it, and does
  > **not** say it is the right condition to impose.
- **Outcome `Li-FREE`**, for a named rung `Li`:
  > Every transition family satisfying the earlier rungs of this freeze's ladder satisfies `Li`,
  > proved universally at evidence level 2 at the configuration named. **So `Li` is not a restriction
  > on that class**, and the information it adds to the ladder is none. **The rung stays in the
  > ladder** and stays in the conjunction the headline quantifies over: this is a finding about the
  > condition and not a licence to drop it, and no artifact of this round reports the ladder as having
  > fewer rungs than this freeze names.
- **Outcome `L4d-HYP`:**
  > `L4d` is the hypothesis of this round's shared structural theorem and is reported as a hypothesis
  > and not as a discharged rung. Neither `L4d-RESTRICTS` nor `L4d-FREE` is a meaningful verdict about
  > it and neither is claimed. The freeze said so before the census, and this report is that statement
  > honoured.
- **Outcome `Li`-UNDECIDED**, for a named rung `Li`:
  > The status of `Li` is undecided in this round, with the obstruction named specifically — the rung,
  > the conjunct, the step at which the proof stopped, and what would settle it. Neither label is
  > claimed, and no sentence of this round treats the absence of a decision as a decision. In
  > particular the absence of a violating candidate is **not** reported as the rung being free, and
  > the absence of an implication proof is **not** reported as the rung having content.

### The outcomes of `OL3`, per candidate

- **Outcome `Φ`-SURVIVES**, for a named transition family `Φ`:
  > The transition family named `Φ` in this round's frozen list satisfies every rung of the ladder
  > this freeze fixes, at the configuration this freeze names for it, at evidence level 2, with each
  > rung's conjunct discharged separately. **This is a statement about the exact family frozen under
  > that label**, and it does **not** endorse it, does **not** say it obtains, and does **not** adopt
  > it as the physical law of evolution.
- **Outcome `Φ`-FAILS**, for a named transition family `Φ` and a named rung:
  > The transition family named `Φ` fails the rung named, at the configuration this freeze names, at
  > evidence level 2, with the failing conjunct and the separating class named. **This settles that
  > family against that rung and nothing in its neighbourhood**, and it is not a statement that
  > families of its shape fail in general.
- **Outcome `Φ`-UNDECIDED**, for a named transition family `Φ` and a named rung:
  > Whether `Φ` satisfies the rung named is undecided in this round, with the obstruction named
  > specifically — the family, the rung, the step and what would settle it. Neither label is claimed.

### The outcomes of `OL4`

- **Outcome `SIOP-YES`:**
  > Two transition families satisfying every condition on this freeze's frozen ladder, whose laws are
  > **not** equivalent under this round's frozen law equivalence, are handed the **same initial orbit
  > class** and their solutions **first diverge** at an exhibited time — the agreement at every
  > earlier time being part of the witness, so that what is exhibited is primitive non-uniqueness and
  > not a divergence propagated from an earlier one — at evidence level 2, with the separating class
  > and invariant named. **So rigidity is cleanly falsified at the configuration named.** This settles
  > the exact ladder this freeze fixes and is **not** a statement that no condition set yields
  > rigidity, **not** a statement about conditions this round does not test, and **not** a licence to
  > add one.
- **Outcome `SIOP-NO`:**
  > No two transition families satisfying every condition on this freeze's frozen ladder, handed the
  > same initial orbit class, have inequivalent trajectories: proved universally at the configuration
  > named, at evidence level 2, the quotient taken over act 12's per-slice equivalence and act 17's
  > trajectory lift of it and over no other relation. **That is the meaningful rigidity result**, and
  > it is bounded to the ladder this freeze fixes and to the configuration named.
- **Outcome `SIOP-UNDECIDED`:**
  > The discriminating test is undecided in this round, with the obstruction named specifically. **The
  > absence of an exhibited pair is not a proof that none exists**, and no sentence of this round
  > treats a failed search as rigidity.

### The outcomes of `OL5` — the headline, each sentence frozen in full

- **Outcome `L-RIGID`:**
  > **All laws satisfying the frozen conditions coincide up to the already-recognized equivalence.**
  > Every transition family satisfying this freeze's ladder, handed the same initial orbit class,
  > yields the same trajectory under act 17's `GramTrajEquiv`, proved universally at evidence level 2
  > at the configuration named. **The quotient is act 12's per-slice equivalence and act 17's
  > trajectory lift of it, both established before this round**, and no equivalence introduced or
  > widened during execution enters the verdict. **This is a statement about the exact ladder this
  > freeze fixes**, at the configuration named: it does **not** say the surviving law obtains, does
  > **not** adopt it, does **not** derive, recognise or approach quantum evolution, and does **not**
  > close `P0` or either of its parts. `P0` stays **OPEN** and two-part, its threading part is
  > untouched, and no carrier is adopted as the physical one.
- **Outcome `L-FAMILY`:**
  > **At least two inequivalent laws survive the frozen conditions, and the surviving class is
  > structurally characterized.** A parameter set written from the anchor and the visible family and
  > the merged record's own objects is exhibited, together with a both-directions theorem at evidence
  > level 2: every member of the family satisfies the ladder, and every transition family satisfying
  > the ladder generates a law equivalent to some member. At least two members are inequivalent under
  > this round's frozen law equivalence, with the separating class and invariant named. **The
  > parameter set is not a restatement of the ladder**, and the report says in terms why. **No
  > condition was added after the survivors were known, and no equivalence was widened after the
  > survivors were known.** This settles the exact ladder this freeze fixes, at the configuration
  > named; it does not adopt any member, does not say one obtains, and does not derive, recognise or
  > approach quantum evolution. `P0` stays **OPEN** and two-part.
- **Outcome `L-WIDE`:**
  > **At least two inequivalent laws survive the frozen conditions, and the conditions do not narrow
  > the class enough for a characterization this round could reach.** The survivors are exhibited at
  > evidence level 2 and their inequivalence is certified through a named invariant; the
  > both-directions characterization is **not** reached, and the obstruction to its universal
  > direction is named specifically — which step, over what the quantifier ranges, and what would
  > settle it. **This is the absence of a characterization and not the presence of a big one.** **No
  > condition was added after the survivors were known, and no equivalence was widened after the
  > survivors were known**; a plurality that would collapse only under an equivalence outside this
  > freeze's frozen quotient list **is a plurality**, and any such candidate equivalence is recorded
  > as an observation for a later round and is not applied here. This settles the exact ladder this
  > freeze fixes, at the configuration named, and is not a statement that no condition set yields
  > rigidity. `P0` stays **OPEN** and two-part.
- **Outcome `L-UNDECIDED`:**
  > **The headline is recorded UNDECIDED.** Neither rigidity, nor a characterized family, nor an
  > exhibited plurality was reached, and none is claimed. The obstruction is named specifically — the
  > target, the rung, the candidate, the step and what would settle it. **An UNDECIDED is a statement
  > about this round and about the record, and not about the question.** It is not a finding that the
  > question is unresolvable, not a finding that it is hard, and not a bound on what a later round can
  > do.

## The frozen post-round sentence for the `P0` row, per case

The `P0` row stays **OPEN** in every case and its label does not change. The sentence the execution
appends to it is composed from the clauses fixed here, and from no other wording.

**Case A — `OL0` silent, `OL1` lands, `SIOP-YES`, and the headline reaches `L-WIDE`.** This is the
case the freeze predicts.

> `P0` remains open and two-part, and the answers of acts 11 through 18 stand exactly as those rounds
> state them. Act 18's structural-law axis reached its top line: a law writable from the anchor and
> the visible family before any lift exists, stated at orbit level so that it descends, together with
> one initial orbit, propagates uniquely. Act 19 asks how rigid the class of such laws is, against a
> ladder of conditions frozen before any census of survivors was run and against a closed list of
> named laws frozen with it. On the structural question that runs first, such a law descends to a
> composition of maps on the admissible orbit spaces, and at a time-homogeneous visible family to a
> monoid action of the naturals on that space — a descent statement and not an existence statement,
> realizing the transition as no operator, no generator and no group element. Against that action
> class the frozen conditions were tested one by one as genuine restrictions rather than as
> decoration, and the record says for each whether it has content or is implied. The discriminating
> test is a same-initial-orbit pair exhibited at its first divergence, the agreement at every earlier
> time being part of the witness so that what is shown is primitive non-uniqueness rather than a
> divergence propagated forward; such a pair exists, so rigidity is cleanly falsified for this
> ladder at the configuration named, and at least two inequivalent laws survive every condition. The
> surviving class is not characterized: the conditions do not narrow it enough for a classification
> this round could reach, the obstruction to the universal direction is named, and the absence of a
> characterization is what the verdict records rather than the presence of a big one. No condition
> was added after the survivors were known and no equivalence was widened after the survivors were
> known; the quotient is act 12's per-slice equivalence and act 17's trajectory lift of it, both
> established before this round. The condition ladder is closed and is not exhaustive, each verdict
> is of the exact frozen proposition and of nothing in its neighbourhood, and deriving or recognising
> quantum evolution is out of scope by this round's own freeze. `P0`'s threading part is untouched,
> act 16's cancellation cell is untouched in either direction, **no carrier is adopted as the physical
> one**, **no surviving law is adopted as the physical one**, and nothing here names, endorses or
> excludes a selection principle.

**Three clauses of Case A vary with the outcome, and they vary independently.** Naming them here, and
fixing each clause's substitutions against the target that governs it, is what lets the execution
compose the sentence it actually earned rather than carry a clause that reads against its own
outcome.

- **The structural clause**, governed by `OL1`, is Case A's sentence beginning "On the structural
  question that runs first".
- **The discrimination clause**, governed by `OL4`, is Case A's sentence beginning "The discriminating
  test is a same-initial-orbit pair".
- **The headline clause**, governed by `OL5`, is Case A's sentence beginning "The surviving class is
  not characterized" together with the sentence beginning "No condition was added".

**The structural clause, per `OL1` outcome.**

| `OL1` | structural clause |
| --- | --- |
| landed (**Case A**) | as written above |
| UNDECIDED | "On the structural question that runs first, the descent of such a law to a composition of maps on the admissible orbit spaces was not reached, with the obstruction named, so the conditions were read of the representative-level transition family with its descent conjunct and the census ran unchanged against that object." |

**The discrimination clause, per `OL4` outcome.**

| `OL4` | discrimination clause |
| --- | --- |
| `SIOP-YES` (**Case A**) | as written above |
| `SIOP-NO` | "The discriminating test is a same-initial-orbit pair, and no such pair can exist under this ladder: two laws satisfying every frozen condition and handed the same initial orbit class have the same trajectory under the round's cross-time equivalence, proved universally at the configuration named." |
| `SIOP-UNDECIDED` | "The discriminating test is a same-initial-orbit pair exhibited at its first divergence, and it is recorded undecided with the obstruction named; the absence of an exhibited pair is not a proof that none exists, and nothing here treats a failed search as rigidity." |

**The headline clause, per `OL5` outcome.**

| `OL5` | headline clause |
| --- | --- |
| `L-WIDE` (**Case A**) | as written above |
| `L-RIGID` | "All laws satisfying the frozen conditions coincide up to the equivalence act 12 and act 17 established before this round, proved universally at the configuration named, which is a statement about the exact ladder this freeze fixes and is neither an adoption of the surviving law nor a derivation, recognition or approach to quantum evolution. No condition was added after the survivors were known and no equivalence was widened after the survivors were known." |
| `L-FAMILY` | "The surviving class is structurally characterized: a parameter set written from the anchor and the visible family and the merged record's own objects is exhibited together with a both-directions theorem, every member satisfying the ladder and every ladder-satisfying family generating an equivalent law, with at least two members inequivalent and the parameter set shown not to be a restatement of the ladder. No condition was added after the survivors were known and no equivalence was widened after the survivors were known." |
| `L-UNDECIDED` | "The headline is recorded undecided with the obstruction named, neither rigidity, nor a characterized family, nor an exhibited plurality having been reached, which is a statement about this round and about the record and not about the question. No condition was added after the survivors were known and no equivalence was widened after the survivors were known." |

**The execution composes the sentence from these substitutions and reports no other wording.** **No
composition closes `P0`**, and none reports either of its two parts closed.

## Naming a law is not endorsing it, FROZEN

Acts 11 through 18 each carry the non-doing "names, endorses or excludes no selection principle".
**This round names candidate laws and candidate conditions, and it must, because it cannot test what
it cannot name.** The reconciliation is frozen here so that it cannot be improvised afterwards.

1. **Naming is for testing.** Each law and each condition is named as an **object of test** and for no
   other purpose. Naming it is not proposing it, not adopting it, not asserting that it is the right
   shape, and not asserting that the programme needs a cross-time law at all.
2. **The round still endorses none.** No outcome of this round endorses any law or any condition, and
   no sentence of any artifact of this round says that a cross-time law is required, on any carrier or
   carrier-free.
3. **Exclusion is only ever of the precise stated form.** Where a law fails a rung, what fails is the
   **exact proposition frozen under that label**, on the exact configuration frozen for it, and
   nothing in its neighbourhood. A failure of `ΦC` at `L3i` is not a refutation of irreversible
   evolutions in general, and the result note says so at each such failure.
4. **The lists are closed at this freeze.** The execution tests these seven laws and these six
   conditions and no others.

### The non-adoption clause, FROZEN VERBATIM

**This is THE CLAUSE, and it is carried as a block quote at every place in this file and in every
artifact of this round where a law's survival could be read as its adoption.** Each carriage opens
with one line naming where it is being carried, contiguous with the body, so that the carriages read
as distinguishable copies of one clause rather than as one paragraph pasted repeatedly — which is a
defect the repository's duplicate check exists to catch — and the naming line changes nothing about
the clause it introduces. Acts 15, 16, 17 and 18 established this pattern and this round follows it.

**Two kinds of mention do not admit an inserted block quote and are governed by this section
instead**, which an auditor checks by reading them against THE CLAUSE: the byte-fixed post-round
sentences of the status rule and of the `P0` row, which carry the clause's substance in their own
frozen wording and cannot admit a quotation inside a quotation; and the bare list entries that do
nothing but name a law among the laws this round tests.

> **THE CLAUSE, carried at this mention — the section that states it.**
> Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"This is Schrödinger evolution", "this is unitary evolution", "the conditions single out quantum
   dynamics", or any statement that a surviving law is, resembles, approximates or points toward
   quantum evolution.** Deriving or recognising quantum evolution is a **later round** and is an
   explicit non-doing of this one. **A round that is not trying to reach a destination may not report
   progress toward it.**
2. **"The surviving law is the physical one", or "this is the law of nature."** The non-adoption
   clause governs:
   > **THE CLAUSE, carried at this mention — the list of what no outcome licenses.**
   > Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
3. **"One more physically reasonable condition would settle it", or any condition added after the
   survivors are known.** The ordering obligation forbids it and its five records are how an auditor
   checks.
4. **"Under the right equivalence the survivors coincide", or any equivalence outside the frozen
   quotient list used in a verdict.** A plurality that collapses only under a new equivalence **is a
   plurality**.
5. **"Two examples make a family."** `L-FAMILY` requires the both-directions characterization; two
   exhibited survivors earn `L-WIDE`.
6. **"The class is too big to classify, so `L-WIDE`", said after both directions were proved.**
   `L-WIDE` is the absence of a characterization, not the presence of a big one.
7. **"The pair differs at some time", reported as the discriminating witness without the
   earlier-agreement conjunct.** That is a propagated divergence reported as a primitive one.
8. **"`L-RIGID` was not reached, so the class is wide."** A failed search earns UNDECIDED, and the
   absence of a `SIOP` pair is not rigidity either.
9. **"The ladder has five rungs", or any report of the ladder with a rung dropped because it was found
   free.** A rung reported `Li-FREE` stays in the ladder.
10. **"The action is a group", "the action is faithful", "the action is transitive", or any symmetry
    property of the induced action.** `OL1` says none of these.
11. **"`XS1` rules out cross-time laws", or "act 18 showed the law is unique."** `XS1` is bounded to
    pointwise laws in act 18's sense, and `L-PROP` is a verdict about `LC3` and about nothing in its
    neighbourhood.
12. **Any statement about the threading, the cross-time representative, the relative evolution or the
    relative candidate.** These are invisible to `≈_O` by construction. **A round that cannot see a
    distinction may not report one**, in either direction.
13. **Any statement about act 16's cancellation cell**, in either direction, and any reading of act
    16's `RN3⁺` or act 15's `PQ3-d⁺` as bearing on the rigidity of cross-time laws.
14. **Any statement about act 14's four carriers**, or any adoption of a carrier, or any assertion
    that a carrier is not the physical one. This round defines no carrier and reads none.
15. **Any statement about act 18's `D`-axis**, its readback data or its `D-MID` outcome. This round
    consumes the `L`-axis element of act 18's headline pair and says nothing about the other.
16. **"Act 10's anchor axis is resolved", or "reopened", or "narrowed."**
17. **"`P0` is closed", or "`P0`'s trajectory part is closed."** The row stays OPEN and two-part in
    every case.
18. **"Act 12's classification is strengthened", "act 17's `TJ1` is enlarged", or "act 18's `L-PROP`
    is extended."** All are consumed at merged strength. **A merged statement is not enlarged by being
    consumed.**
19. **"The evolution is continuous", "smooth", "generated", "one-parameter", or any statement resting
    on structure the index type does not carry.** `CoherentLift` is `ℕ`-indexed and this round does
    not change that.
20. **"OI and QM are inequivalent."** Two laws differing is not two theories differing, and the
    established finite observable-law correspondence is untouched. Every visibility statement here is
    further a statement under act 7's own readback convention, with `D4b` negative.
21. **"The condition list is exhaustive", or "these are the physically reasonable conditions."** Six
    conditions are frozen for testing. A condition outside them is neither imposed nor refuted by
    anything here.
22. **"The law list is exhaustive."** Seven transition families are frozen for testing, and a law
    outside them is neither refuted nor endorsed here.
23. **Any sentence about Track I**, or about Source B or Source C, on any axis.
24. **Any import from the substratum Lemma 24.1 rounds.** A shared word is not a bridge.

## Named hazards

1. **A post-hoc rescue condition.** **This is the strongest hazard in the round.** The specific failure
   guarded against is an execution that finds a plurality, adds "one more physically reasonable
   condition", and reports `L-RIGID`. The ordering obligation and its five records exist for it.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
   > none. A law that survives every condition this freeze names is a law that survives **those**
   > conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
   > nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
   > physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
   > the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
   > to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
   > **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
   > one, and nothing here derives, recognises or approaches quantum evolution.**
2. **A post-hoc rescue equivalence.** The specific failure guarded against is the same manoeuvre in
   different clothes: an execution that finds a plurality, declares a new equivalence under which the
   survivors collapse, and reports `L-RIGID`. The frozen quotient list is what closes it, and the two
   routes are named together so that closing one does not leave the other open.
3. **A divergence reported at the wrong time.** The specific failure guarded against is a `SIOP`
   witness at `t* ≥ 2` without the earlier-agreement conjunct, which is a divergence propagated
   forward reported as primitive non-uniqueness.
4. **`L-FAMILY` claimed from two examples.** The specific failure guarded against is a result note
   that exhibits two survivors, calls the residue a family, and never attempts the universal
   direction.
5. **`L-WIDE` claimed after a characterization was proved.** The reverse failure, guarded against for
   the same reason: `L-WIDE` is the absence of a characterization.
6. **A characterization that restates the ladder.** The specific failure guarded against is a
   parameter set defined as "the families satisfying `L0`–`L5`", which proves both directions
   trivially and characterizes nothing.
7. **Decoration reported as a rung.** The specific failure guarded against is a ladder whose rungs are
   all satisfied for free by every member of the class, reported as though each had narrowed it. The
   `Li-RESTRICTS` / `Li-FREE` labels are what make the difference visible.
8. **A rung dropped because it was found free.** The opposite failure: `Li-FREE` is a finding about
   the condition, not a licence to shorten the ladder or to renumber it.
9. **Deriving quantum evolution by accident.** The specific failure guarded against is a sentence of
   the form "and this is just unitary evolution", or a condition stated with quantum dynamics as its
   standard of correctness. `L5` was tested against exactly that and the test is recorded.
10. **`L5` smuggling the answer in.** The specific failure guarded against is a composition condition
    stated in terms of tensor-product Hamiltonians, generator additivity or a one-parameter group.
    `L5` as frozen mentions none of these, and the identity transition satisfies it, which is the
    freeze's certificate that it does not presuppose the answer.
11. **A generator law that does not descend.** Carried from act 18: a representative-level transition
    that does not descend "selects" by fixing an unphysical frame. The descent conjunct is part of the
    transition-family object here and not a commentary on it.
12. **Reading `OL1` as an existence statement.** It is a descent statement; that an `L-PROP` law
    exists is act 18's and is consumed.
13. **Stating the monoid form at a non-homogeneous configuration.** There is no single state space for
    a monoid to act on there, and `OL1` (b) is frozen at time-homogeneous configurations only.
14. **Realizing the transition as an operator.** The specific failure guarded against is a step that
    represents `Φ̄` as a unitary, a matrix acting on a state space, a generator or a group element, on
    the way to anything. No such step is licensed.
15. **Treating an undischarged rung as discharged because no counterexample was found.** The specific
    failure guarded against is reporting `Li-FREE` from a search.
16. **Enlarging a bounded verdict.** The specific failure guarded against is a sentence of the form
    "so no condition set yields rigidity" or "so all cross-time laws agree". Each verdict is bounded to
    the frozen ladder, the frozen list and the named configuration.
17. **Seeing the threading.** The specific failure guarded against is a statement of this round
    distinguishing two lifts that `≈_O` identifies — for instance reporting that act 11's `GL2` pair
    has two trajectories. It has one, for this round, and the round says nothing about the difference.
18. **Reading raw Gram equality or act 13's relation as this round's relation.** The frozen quotient
    list names the three equivalences and forbids every other.
19. **Touching act 16's cancellation cell or the threading question.** Neither is asked here, in either
    direction, and no outcome of this round bears on either.
20. **Reading an outcome of this round as bearing on act 18's `D`-axis.** The two axes of act 18
    answer different questions and this round consumes one of them; a verdict here is not evidence
    about readback data in either direction.
21. **Importing time structure the index type does not have.** `ℕ` carries successor and order and
    nothing else. The first-divergence conjunct uses exactly that and nothing more, and no candidate,
    proof or sentence may rest on continuity, differentiability or a limit.
22. **Choosing a configuration after an outcome is known.** The countercontrol table names the
    configuration for every rung and every candidate in advance, and an alternative found during
    execution is recorded as an observation and never substituted.
23. **Treating the `|A| = 1` case as automatically the right one for a cross-time statement.** Carried
    from act 18, which recorded the concrete instance where it collapsed a cross-time distinction.
24. **A reader supplying a missing theorem from background knowledge the record does not contain.**
    The specific failure guarded against is a step of the form "of course the evolution is unitary" or
    "of course reversibility forces a group" — plausible-sounding, absent from the record, and
    licensed by nothing in it.
25. **Forgetting the anchor, and forgetting the rank bound.** `FibreGram a₀` and `RealizableGram` both
    carry data a cross-time statement can silently drop: the anchor, and the `|A|` rank bound that
    makes `SH1` sufficiency true.
26. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs.
27. **Importing the substratum Lemma 24.1 rounds' vocabulary.** Those rounds work on a different
    carrier in a different programme. Nothing is consumed or compared, and a shared word is not a
    bridge.
28. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_OLR_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
29. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
30. **A chronology guard that fixes this round's own pins at `None` for all time.** See the chronology
    control's clause 9, which exists because an earlier round wrote exactly such a clause and its whole
    execution object had to be rebuilt.
31. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: **derive, recognise, approach or claim progress toward quantum evolution**, in any
paraphrase; adopt any surviving law as the physical one; adopt a carrier as the physical one or define
a carrier of its own; endorse any condition or any law; assert or deny that a cross-time law is
required or suffices; **edit `L0`–`L5` after the first discriminating result**, add a rung, remove a
rung or renumber the ladder; **introduce or widen an equivalence during execution**, or use one
outside the frozen quotient list in any verdict; **ask the threading question or the cross-time
representative question, in either direction**; touch act 16's cancellation cell, in either direction;
state anything about the relative object, the relative candidate, the anchored channel or the
re-anchored channel; state anything about act 18's `D`-axis or its readback data; **re-prove or
strengthen acts 12, 17 or 18**; revise `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`,
`TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`, `AB1`, `AB2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`–`PQ4`,
`CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3`, `XS0`–`XS5` or any merged label; answer act 13's fork `CT3` (d)
or move it in either direction; redefine act 12's `GramPhaseEquiv` or act 17's `GramTrajEquiv`; test a
law outside the frozen list; realize the transition as an operator, unitary, generator or group
element; change `CoherentLift`'s `ℕ`-indexing or introduce continuity, smoothness or a generated
evolution; introduce a further carrier or revise any of act 14's four; resolve, reopen or narrow act
10's anchor-axis reclassification; report a bounded verdict as a general impossibility; change `D3`,
`D4b`, `D5`, the direct-branch statement or the readback convention; alter any existing archive seal
constant; consume or compare anything from the substratum Lemma 24.1 rounds; compare Source A with B
or C; edit any manuscript; close `P0` or either of its parts; or say anything about Track I.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

**"Show that these conditions single out Schrödinger evolution" is not asked, not bounded and not
attempted.** It is the natural stretch target of this round and it is unbounded here: it needs a
notion of quantum evolution on the orbit space that the record does not carry, a bridge from a
transition on `GramPhaseEquiv`-classes to an operator on a Hilbert space that acts 12 through 18 do
not build, and an evidence bar this freeze could not honestly fix. It is named here as a non-doing
**so that it cannot creep in mid-execution**: an execution that finds a rigid or narrow class and
begins asking whether the survivor looks like unitary evolution has left this round's scope, and what
it finds is **recorded as an observation and not executed**. A later round that wants the recognition
question must freeze it first.

**And the round refuses the weaker version too.** "The surviving class resembles", "is consistent
with", "is what one would expect from", or "is a step toward" quantum evolution are forbidden
sentences, for the same reason: this round has no standard against which resemblance could be
measured, and a round without a standard may not report a comparison.

### What act 19 does and does not change about `P0`

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 19 can change
is the **bounding** of its trajectory part, and only that: act 18 established that a cross-time law
plus one initial orbit can propagate, and act 19 asks how many such laws there are once structural
conditions are imposed. **No outcome of this round closes `P0`, no outcome closes either of its parts,
and no outcome makes either part closable.** `P0`'s threading part is untouched in either direction.
And even `L-RIGID` would be a statement about **one frozen ladder at one named configuration** and not
a statement that the programme has found the structure `P0` asks for: what `P0` asks is what
**determines** the relative quantum evolution, and showing that a named ladder leaves one law is not
showing that the ladder is the right ladder or that the law obtains.

**The direct-branch statement is frozen exactly, and no more:** `D4a` positive on the direct branch;
`T1` **necessary, not sufficient**; `n = 3` properness at **evidence level 3**; **no claim about what
fraction of OI lies in the direct sector.** Act 7 layer 2's `D5` control stands **NOT CERTIFIED**.

## Definition budget

The execution introduces **at most eight** top-level Lean definitions, and these are the eight:

1. **`TransitionLaw`** — the law a transition family generates, carrying the `L4d` descent conjunct:
   `TransitionLaw Φ Law := (∀ t G G', GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) ∧ ∀ 𝔾,
   Law 𝔾 ↔ ∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`. Every rung and every candidate is stated over
   it. *Needed.*
2. **`EvolvesTotally`** — `L0`, the totality of the induced evolution on `Ω_0`. *Needed.*
3. **`PreservesAdmissible`** — `L1`, stated for the relation on the whole per-slice orbit space.
   *Needed.*
4. **`Reversible`** — `L3`, carrying `L3i` and `L3s` as two conjuncts so that each is reported apart.
   *Needed.*
5. **`FactorizesOnProduct`** — `L5`, at the frozen product configuration. *Conditional*: it fires only
   if `L5` is retained by the owner settlement below, and it is unused otherwise.
6. **`LadderConds`** — the conjunction `L0 ∧ L1 ∧ L2 ∧ L3 ∧ L4 ∧ L5` as one `Prop`. **This is the
   single declaration the ordering obligation pins**, and the ladder cannot be made checkable without
   it. *Needed.*
7. **`LawEquiv`** — `≈_L`, equality of solution sets among pointwise realizable trajectories. All
   three headline outcomes are stated over it. *Needed.*
8. **`SameInitialOrbitPair`** — the discriminating test as one `Prop`, carrying the earlier-agreement
   conjunct. *Needed.*

**`L2` and `L4n` consume no slot**: `L2` is stated inline as `∃ Φ̂, ∀ t, Φ t = Φ̂` inside `LadderConds`,
and `L4n` inline against act 12's merged transformation laws. **`L4d` consumes no slot**, being the
first conjunct of `TransitionLaw`.

**Why this budget is larger than act 18's five, recorded as a reason and not as an expansion.** The
ladder has six rungs and the ordering obligation requires each to be a **named declaration** whose
statement an auditor can diff across two commits. A ladder stated inline in the theorems that use it
cannot be checked that way, and the obligation would become aspirational — which is exactly what the
owner's mechanical-teeth requirement forbids. **The extra slots buy the checkability of the no-post-hoc
rule**, and the freeze says so rather than letting the count drift.

**A further definition beyond these eight requires its own append-only amendment**, separately frozen
and merged before the work it affects. **No lift, gauge element, witness, matrix, visible family, Gram
tuple, entry value, permutation, class or configuration is a top-level definition** — each is a bound
variable pinned by an equation in the statement that needs it, as acts 10 through 18 did. Acts 7's,
10's, 11's, 12's, 13's, 17's and 18's definitions are **reused, not redefined**; in particular
`FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `CoherentLift`, `FibreCrossGram`, `TwoSidedRelated`,
`GramTrajEquiv`, `SelectsAt`, `PointwiseLaw`, `DeterminesTraj`, `ProperAt` and `PropagatesFrom` are
consumed and none is restated.

## Evidence level

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `OL1`, for each part of `OL2`, `OL3` and `OL4` whichever
label it reaches, and for `OL5` whichever line it reaches other than UNDECIDED. `decide` over finite
index types is kernel-checked and permitted; `native_decide` is not, and neither is `sorry`.
`Classical.choice` is expected wherever act 17's `tj1_sufficiency` is applied, which assembles a lift
from a per-time choice, and its appearance there is not a defect.

**`OL0` is type P and carries no evidence level.** It is settled by the frozen evidence rule —
verbatim quotation with a coordinate, or the recorded statement that the passage sought does not exist
on the named and bounded search — and by nothing else. **Reconstructive inference is forbidden as a
finding**, and where the record is silent the finding is that it is silent.

## The chronology control — act 10's STRENGTHENED mechanism, with the archive rule of PR #599

The execution's guard tag is **`R7-OLR`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_OLR_SEALED_HEAD`** and **`_OLR_MERGE`**, with the
base held in **`_OLR_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific act 19 object
   enters the repository tree** — any Lean definition or proof about a transition family, about a
   ladder condition, about the descent of a propagating law or about the rigidity of the class; any
   search artifact; any probe clause; any result artifact. **The single permitted exception is the
   analysis recorded inside this control-plane blob itself**, merged *as* the freeze, including the
   frozen evidence rule, the `L5` test, the table of what the merged record supplies, and the
   pre-freeze reading recorded as the reason for `OL0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_OLR_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content at this exact path, and the
   execution ancestry, **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails closed**,
   with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _OLR_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of `B`**,
   fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for `B`,
   for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_OLR_SEALED_HEAD` and `_OLR_MERGE` are present and **unset** at execution. After
   `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the same strong
   check against the sealed object: the pinned merge's second parent must equal the sealed head; the
   sealed head must pass clause 5 against `B` exactly as in its own run; and both must be reachable
   from the current target — the real `pull_request.head.sha` in pull-request continuous integration,
   `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change recording the two SHAs and
   nothing else.
8. **Existing seal constants are read with mutation controls and never written.** The guard clause
   checks `_XTS_BASE`, `_XTS_SEALED_HEAD`, `_XTS_MERGE`, `_TRJ_BASE`, `_TRJ_SEALED_HEAD`, `_TRJ_MERGE`,
   `_RNC_BASE`, `_RNC_SEALED_HEAD`, `_RNC_MERGE`, `_TCF_BASE`, `_TCF_SEALED_HEAD`, `_TCF_MERGE`,
   `_PQT_BASE`, `_PQT_SEALED_HEAD`, `_PQT_MERGE`, `_CTI_BASE`, `_CTI_SEALED_HEAD` and `_CTI_MERGE`
   equal to the values acts 18, 17, 16, 15, 14 and 13 set, because an archive seal belongs to the
   round that set it.
9. **This round's own triple is never a permanently fixed execution-mode value.** `R7-OLR` must not
   assert `(_OLR_BASE, _OLR_SEALED_HEAD, _OLR_MERGE)` equal to `(_OLR_BASE, None, None)` as a standing
   invariant. Either the round's own triple is **excluded** from the prior-seal integrity clause of
   item 8 — which names other rounds' seals and is the shape this freeze intends, following the
   `_tcf_prior_seals`, `_rnc_prior_seals`, `_trj_prior_seals` and `_xts_prior_seals` precedent of
   **zero executable references to the round's own constants**, with docstring prose explaining the
   exclusion being entirely sufficient — or it is checked **mode-aware**, the expectation being
   `(_OLR_BASE, None, None)` while `_OLR_SEALED_HEAD` is unset and
   `(_OLR_BASE, _OLR_SEALED_HEAD, _OLR_MERGE)` once `P` has set them, and read from the module
   constants rather than from the argument, so that a fabricated tuple cannot define its own
   expectation. A clause that fixes this round's own pins at `None` for all time contradicts item 7,
   under which `P` must set them: the guard would then pass at no commit once the round lands, and the
   round's mandatory lifecycle could not complete. **This item exists because an earlier round wrote
   exactly such a clause and its whole execution object had to be rebuilt**, and it is written so that
   the executing agent cannot reintroduce that failure: **the exclusion route is the one this freeze
   intends**, and the mode-aware route is permitted only in the exact form stated here, with the
   expectation read from the module constants and **never** from the argument. Prior rounds' seals stay
   read-only invariants exactly as item 8 states; this item constrains only how the round treats its
   **own** pins.

**The executing agent is directed to the exclusion route, in terms.** The `R7-OLR` prior-seal
integrity function names acts 13's, 14's, 15's, 16's, 17's and 18's triples and **says nothing whatever
about `_OLR_BASE`, `_OLR_SEALED_HEAD` or `_OLR_MERGE`**: zero executable references to this round's own
constants, with the exclusion explained in the function's docstring. **And the exclusion is verified
empirically before the commit, in three configurations**, the third being the one an earlier round
failed: unmutated, expecting `True`; every single-field fabrication of each prior-seal constant one at
a time, expecting `False` each time; and **this round's own pins set to plausible values with the prior
seals unmutated, expecting `True`**. The three results are reported as measurements and not as
intentions.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md \| git hash-object --stdin` equals the blob the `R7-OLR` clause pins |
| 2 | Act 18's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_XTS_SEALED_HEAD = '730a518c173460d7bed525da10a95ee6bd32c7de'` and `_XTS_MERGE = '0b893d75cca344faeb9a9e434b5b8537f8b45dac'`, both non-`None` |
| 3 | Act 17's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TRJ_SEALED_HEAD = '94d41561114b2aee5939dcfa976ce98b8f141093'` and `_TRJ_MERGE = 'e8b12a433ebc0e5047504d2c95664a85ca65d1e8'`, both non-`None` |
| 4 | Act 16's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_RNC_SEALED_HEAD = '31db7c1082b012c00c43f3fda35ce44c5653e123'` and `_RNC_MERGE = 'eb70bbb9b2b3311095945ec3ce2418962f3b741a'`, both non-`None` |
| 5 | Act 15's execution is merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_TCF_SEALED_HEAD = 'c622461495c6b2db4e09c8084f404bd5ca2c5192'` and `_TCF_MERGE = '9e0cc3834538b7bdcb742fcaa046194cfa9526fb'`, both non-`None` |
| 6 | Act 14's and act 13's executions are merged **and sealed** | `git show B:verification/lean/edge_rigidity_probe.py` contains `_PQT_SEALED_HEAD = '5008a47bf7e67edc502120f9269c4a4661ef7342'`, `_PQT_MERGE = 'c50dd22457bfd4812761cb56e7ca1a559af33c5e'`, `_CTI_SEALED_HEAD = '9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7'` and `_CTI_MERGE = '292848b3c908d33ac432a5360effe0c259e3ce16'`, all four non-`None` |
| 7 | The modules this round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/IntermediateCrossTimeStructure.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/CrossTimeInvariants.lean`, `git cat-file -e B:verification/lean-mathlib/OIBridge/TwoSidedGauge.lean` and `git cat-file -e B:verification/lean-mathlib/OIBridge/CoherentLiftGauge.lean` all succeed |
| 8 | No act 19 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean` |
| 9 | The guard tag and its stem are still free | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-OLR` and no occurrence of `_OLR` |

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
- **The execution branches from the merge commit of this control-plane pull request and from nothing
  else**, and **its first act is to verify that the preregistration at that base carries the blob this
  freeze names**, before any target is executed. The verification is recorded in the result note.
- **The ladder commit comes second**, before any discriminating result, and its SHA is recorded. The
  ordering obligation's five records are assembled as the execution proceeds and not reconstructed at
  the end.
- **Then exactly one execution pull request**, based on that merge commit, carrying the Lean module,
  the result note, the `R7-OLR` guard clause with `_OLR_SEALED_HEAD` and `_OLR_MERGE` present and
  unset, the `ROADMAP` propagation and the census entry. **No manuscript changes.**
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no rebase,
  no amend, no force-push. A red badge caused solely by an archive clause that entered `main` after
  the base is not a research failure; the certification of record is the run whose `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled named
   and no existing seal constant altered, and the base-blob verification recorded;
2. **the ordering obligation's five records, in full** — the ladder table, the ladder commit SHA, the
   discrimination commit SHA, the immutability span with the command and its result, and the quotient
   record — **and the statement that no condition was added and no equivalence was widened after the
   survivors were known**;
3. **`OL0`** — the bounded search, recorded in full, with the per-term result and the finding stated
   as a finding about the record;
4. **`OL1`** — the shared structural theorem in both its parts or its obstruction, with the `TJ1`
   dependence named at the step, with part (b) reported at time-homogeneous configurations only, and
   with the bounded reading carried;
5. **`OL2`** — the eight rung statuses, each with its frozen label and sentence, `L4d` reported as a
   hypothesis, every `Li-FREE` reported as a finding about the condition and **not** as a licence to
   shorten the ladder;
6. **`OL3`** — the seven-candidate census, each reported separately with its frozen label, each verdict
   stated of the exact frozen family at the exact frozen configuration;
7. **`OL4`** — the discriminating test, with `t*` named, the **earlier-agreement conjunct proved**, and
   the witness reported as primitive non-uniqueness or the universal negation reported as rigidity;
8. **`OL5`** — the headline in the status rule's frozen wording, with the condition set named in the
   label, with the `L-FAMILY` characterization's both directions reported separately where it is
   claimed and its parameter set shown not to be a restatement, and with the obstruction named
   specifically in each UNDECIDED case;
9. **the `L5` test as it stood at execution** — whether the condition was still definable in the
   programme's vocabulary, whether the satisfying and the violating candidates behaved as the freeze
   predicted, and the record of the product-embedding construction;
10. **the scope boundary as honoured**: the confirmation that no statement of the round distinguishes
    two lifts `≈_O` identifies, that **nothing derives, recognises or approaches quantum evolution**,
    that act 16's cancellation cell and the threading question are untouched in either direction, that
    act 18's `D`-axis is untouched, and that act 10's anchor-axis reclassification is untouched;
11. **the non-adoption clause carried verbatim at each mention**, with the count of carriages, and the
    confirmation that no law is adopted, endorsed or given physical status by surviving;
12. the frozen `P0` sentence for the case reached, composed from the frozen clauses, verbatim, and the
    row's label unchanged;
13. what no outcome licenses, in this file's wording, and the status rule as honoured;
14. the relation to acts 10, 11, 12, 13, 14, 15, 16, 17 and 18 — every merged label consumed, none
    revised — with act 12's classification, act 17's `TJ1` and `TJ3` and act 18's `XS1` and `L-PROP`
    consumed at merged strength;
15. the definition count against the eight-slot budget, with the conditional slot marked fired or
    unused;
16. the chronology certification, naming the property certified, the nine preconditions checked at
    `B`, the archive-mode pins as unset at execution, and clause 9 reported as honoured by exclusion
    with the three empirical configurations reported as measurements;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired.

## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Items 1 through 12 are calls
already made**, written here so the record shows they were settled rather than left open. The body of
this freeze is written to them throughout. **The open decisions follow them in their own section and
are not calls already made.**

1. **The scientific scope is FROZEN as written and is not renegotiated.** No rung is added to the
   ladder, the ladder is not widened, and the candidate list is closed. An execution that wants more
   freezes its own round.
2. **The round does NOT try to derive Schrödinger evolution.** It classifies what act 18 opened.
   Deriving or recognising quantum evolution is a later round and is an explicit non-doing, carried in
   the non-doings, in the forbidden sentences and in the hazard list alike.
3. **The condition ladder is frozen BEFORE any census**, and the ordering obligation's five records are
   what an auditor checks. The obligation is written as a checkable ordering on the execution and not
   as an aspiration.
4. **NO POST-HOC CONDITIONS, and NO POST-HOC EQUIVALENCES.** The two rescue routes are closed together
   and the symmetry is stated where both are named: adding a condition narrows the survivors, widening
   the quotient merges them, and both convert a plurality into rigidity after the fact.
5. **`L-RIGID` is modulo equivalences already recognized before act 19**, and the frozen quotient list
   names the three that may be used: act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv`, and the law
   equivalence derived from them, which introduces no new identification. An equivalence introduced or
   widened during execution cannot reach `L-RIGID`.
6. **The `L-FAMILY` / `L-WIDE` boundary is the both-directions characterization theorem**, and neither
   the "two examples make a family" failure nor the "too big to classify" failure is permitted. A
   parameter set that restates the ladder characterizes nothing.
7. **The discriminating test is exhibited at its FIRST divergence**, with the earlier-agreement
   conjunct part of the witness. A clean formulation is available because `ℕ` is well-ordered, and no
   fallback to "differ at some time" is used.
8. **Each rung is tested as a genuine restriction**, with `Li-RESTRICTS`, `Li-FREE` and `Li-UNDECIDED`
   as the exhaustive labels, and `L4d` reported as the shared theorem's hypothesis. A rung found free
   stays in the ladder.
9. **`L5` passed the owner's test and stays in the ladder**, in a wording that mentions no unitary
   evolution, no generator, no one-parameter group and no Schrödinger equation, with a satisfying
   candidate and a violating candidate both exhibited on the same terms. It was not weakened to
   survive, and the no-post-hoc rule was not weakened to accommodate it.
10. **The shared theorem runs FIRST**, and is split into a general composition form and a
    time-homogeneous monoid-action form, because the monoid statement is not literally stateable at a
    general visible family.
11. **Threading stays OUT**, act 16's cancellation cell stays untouched, and act 18's `D`-axis is
    untouched. Act 19 is orbit/trajectory-law rigidity only.
12. **Acts 12, 17 and 18 are consumed at merged strength**: not re-proved, not strengthened, not
    redefined. Act 12 supplies the slice equivalence and act 17 the trajectory lift, and the
    attribution is exact wherever either is named.

### Open decisions, recorded for owner settlement before this freeze merges

**These are NOT calls already made.** Each is recorded with its options, this freeze's recommendation
and the reason, in the act 16, 17 and 18 pattern of recording a settlement rather than leaving one
implicit. **The freeze does not merge until each is settled**, and the body above is written to the
recommended option throughout so that settling it the other way is a bounded edit and not a rewrite.

**Open decision 1 — SEALING or NON-SEALING.**

- **Option A, recommended: SEALING**, under the guard tag `R7-OLR`, landing `E` → `L` → `P` with `P`
  mandatory, with chronology clause 9 honoured by excluding this round's own triple from the
  prior-seal integrity clause. **The reason is derived and not defaulted**: act 19's execution creates
  a new Lean module with new named results, and the round's whole claim is a claim about **when** the
  ladder was fixed relative to the census — so the round creates a new formal object whose chronology
  matters to the result, which is exactly the owner's sealing criterion. The `R7-OLR` ancestry guard
  is what makes the ordering obligation enforceable rather than self-reported.
- **Option B: NON-SEALING**, taking `L` alone under `§A.37` item 2. This is correct **only if** the
  owner directs that act 19 add no Lean module, no named result and no guard clause — a purely
  classificatory round over existing formal results. **The cost is recorded honestly**: in that shape
  the ladder has no kernel statement to diff, the ordering obligation's records 1 through 4 lose their
  mechanical check, and the no-post-hoc rule rests on the result note's own testimony. **The freeze
  recommends against Option B** for that reason and not because recent rounds have been sealing.
- **What changes if Option B is settled**: the round's shape section, the chronology control, the
  preconditions table, the definition budget, the evidence level and the execution discipline are
  rewritten; the scientific content, the ladder, the quotient list, the candidate list, the
  discriminating test and the status rule are unchanged.

**Open decision 2 — `L5`'s retention, its wording, and the product-embedding cost.**

- **Option A, recommended: retain `L5` in the wording frozen above.** It passed the owner's two-part
  test at drafting time: it is definable without reference to Schrödinger or unitary evolution, and
  both a satisfying candidate (`ΦI`, and `ΦPP` with content) and a violating candidate (`ΦCTRL`) are
  exhibitable on the same terms. Its non-presupposition certificate is that the identity transition
  satisfies it, so `L5` cannot by itself have selected a quantum answer.
- **Option B: drop `L5` and run the round on `L0`–`L4`.** The owner records that `L0`–`L4` already
  constitute a meaningful rigidity experiment. **The reason this option is live** is cost, not
  principle: `L5` needs the product embedding on fibre-Gram tuples — Kronecker product of admissible
  dilations, admissibility for the pointwise-product visible family, positive semidefiniteness and the
  multiplied rank bound — and act 18's `prod_admissible` starts that construction without finishing
  it. If the owner judges that cost too large for this round, dropping `L5` **before** the freeze
  merges is clean; dropping it afterwards is forbidden by the ordering obligation.
- **What changes if Option B is settled**: `L5`'s section, the `L5` test section, the `ΦPP` and
  `ΦCTRL` entries of the candidate list, the `L5` rows of the countercontrol and prediction tables,
  definition slot 5 and the frozen product configuration are removed; the headline labels then read
  `(L0–L4)` throughout. Nothing else moves.

**Open decision 3 — whether the `L3` finiteness route is permitted.** `L3i` and `L3s` are frozen as
two conjuncts because `Ω_t` is not known to be finite. **Recommended: permit the execution to derive
one conjunct from the other where it proves `Ω_t` finite in the kernel at the named configuration, and
require it to record that it did so and where.** The alternative is to forbid the route entirely and
require both conjuncts proved directly at every configuration, which is cleaner and more expensive.
The freeze recommends the permissive form with the recording requirement, because the recording makes
the route visible and the prohibition would buy nothing the recording does not.

**One check was performed at drafting time and its outcome is recorded here as a settlement rather
than as a correction in flight.** The two mandatory verbatim clauses of this file — the start-state
discrepancy clause and the anti-contamination invariant — were **extracted by reading bytes** from act
18's preregistration blob `fd3fa1359188966cae006deba4944a14aab5f3dd`, each bounded by its own
paragraph, and each reproduced here without retyping. The discrepancy clause is **plain prose** in act
18's file and is plain prose here; the anti-contamination invariant is a **block quote** in act 18's
file and is a block quote here. Each appears in this file **exactly once**, and each is byte-identical
to act 18's after stripping block-quote markers and normalizing whitespace.
