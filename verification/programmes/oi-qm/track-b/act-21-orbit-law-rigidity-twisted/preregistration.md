# Track B act 21 — the rigidity of the cross-time laws act 18 opened, re-frozen at act 20's certified naturality: CONTROL PLANE

Owner-called. This file is the whole of act 21's control plane and is merged **alone**, before any
execution object exists. It re-freezes **act 19's experiment** — the bounded rigidity census over a
ladder of conditions frozen before any census is run — with **one** mathematical change: the
naturality rung `L4n`, which act 19's closure found underspecified and which act 20 classified, is
restated as act 20's certified `N-TWIST` notion, exactly at that strength. Everything else in the
experiment — the question, the ask, the objects, the quotient list, `L0`, `L1`, `L2`, `L3i`, `L3s`,
`L4d`, `L5`, the shared theorem, the headlines, the discriminating test, the seven candidates, the
witness supply, the countercontrols, the status rule, the predictions and the `P0` sentences — is
act 19's, carried by line range from act 19's pinned blob under the provenance rule below. The
lifecycle, the chronology and the guard are this round's own, under the manifest protocol `SI-3`
left in force, and the contamination attestation act 20 built is carried with the span act 20's
result said it should have.

It is **not** a continuation of act 19's execution, **not** a re-run of act 19 with one rung edited
in flight, and **not** an adjudication of anything act 19's closure lists as uncertified. It is
**not** an attempt to derive or to recognise quantum evolution, which stays an explicit non-doing.

**Blob identity is authoritative.** The execution guard pins this file by content, by path and by
blob together, so the path below is load-bearing and does not move after this merges.

## The round's shape, declared first, in `§A.37`'s terms — under the manifest protocol

**This is a SEALING round.** `AGENTS.md` `§A.37`, **lines 775–780**, quoted verbatim at this base —
the numbered item's opening, ending part-way through line 780:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes
>    ownership of changing existing seal state — takes a pin commit `P`, and `P`
>    is mandatory.** `P` writes the round's own **manifest record** —
>    `sealed_head` = `E` and `merge` = `L`, under `verification/seals/` — and not
>    a legacy constant; see *Sealing through the manifest* at the end of this

This freeze **creates new seal state**, and it creates it in the representation `SI-3` left in force:
**data under `verification/seals/`, no constant in the guard file.** The round's seal state is carried
in two places at two times, and nowhere else:

| object | where it lives | state during execution | state from `P` |
| --- | --- | --- | --- |
| the mandated execution base | the **prospective declaration** in `verification/lean/edge_rigidity_probe.py`, `_MANIFEST_PROSPECTIVE = {'OLT': B}`, with `B` the merge commit of this pull request | **declared**, and the validator classifies `OLT` as `EXECUTION` against it | **removed** by `P`; a stem both declared and recorded is a failure |
| the declared integrity baseline | `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLT',)}`, in the same file | the seals tree at `B` — twenty-five records — plus the one addition this freeze authorizes, by stem | unchanged; `OLT.json` is the authorized addition, validated by content |
| the round's manifest record | `verification/seals/OLT.json` | **absent** | **written by `P`**: `{"round": "OLT", "kind": "sealed", "base": B, "sealed_head": E, "merge": L}`; the validator classifies `OLT` as `ARCHIVED` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
writes `OLT.json` and removes the `OLT` entry from the prospective declaration, and touches nothing
else. Without `P` the round sits at `LANDED-PENDING-PIN`, permitted at `L` itself, and every head
descending from that unpinned landing fails as *seal pending*.

**No legacy seal constant is written, at any commit of the round.** Nothing matching
`_OLT_(BASE|SEALED_HEAD|MERGE)` exists at any commit, `SI-3`'s standing contract — zero legacy
assignment statements in the guard file — holds at every head, and every read of any round's seal
state goes through the manifest accessor. The execution's guard clause certifies chronology through
one keyed call, `_si2_authority('OLT', tag='R7-OLT')`, and never through a per-round constant.

### The lifecycle derivation, and why it comes out SEALING

**The lifecycle is derived from what the round owns, not from what act 19 declared.** The rule the
owner set for act 19 is carried: a round is sealing **if and only if** its execution creates a new
formal object whose chronology matters to the result. Run against this freeze's own scope:

1. **The execution creates new formal objects.** A new Lean module carrying this round's own named
   results — the shared structural theorem, the ladder's rungs as named `Prop`s, the census
   verdicts, the discriminating test and the headline. None of these exists at the base; act 19's
   module never reached `main`, and act 20's module is about naturality and carries no rung.
2. **Their chronology is load-bearing.** The round's whole claim is that the condition ladder was
   fixed **before** the census of survivors was run — and act 19 is the round that showed what it
   costs when that ordering is not enforceable: its closure is a chronology adjudication. The
   ordering obligation below is itself a chronology claim, and a validator-certified ancestry rooted
   at this control plane's merge commit is the mechanism that makes it enforceable.
3. **A new module with new named results is new seal state** under `§A.37`'s definition, and under
   the manifest protocol that seal state is a new `sealed` record, which only a sealing round's `P`
   may write.

**Therefore act 21 is SEALING, and it owns no other seal state.** The counterfactual act 19 recorded
— a purely classificatory round over existing formal results, taking `L` alone — is not this
round's shape, because the owner has directed that act 21 re-prove every fact it uses in its own
module.

### The tag, the stem, the module and the round directory are free at this base

At **`63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`**, the certified `main` this freeze is written
against — the landing merge of `SI-3`, certified by main-push run 35412319426:

- `git grep -- 'R7-OLT'` returns nothing anywhere in the tree, and the tag is absent from the
  **eighty-four** `R7-*` tags `verification/lean/edge_rigidity_probe.py` carries at this base.
- `git grep -- 'OLT'` returns nothing anywhere in the tree — **the bare three-letter form does not
  occur in prose, in Lean, in Python, in JSON or in any manuscript** — so a bare-stem search for it
  is unambiguous, and `git grep -- '_OLT'` returns nothing.
- No record `verification/seals/OLT.json` exists; the twenty-five records at this base use the stems
  `A12P`, `A6D`, `A6I`, `A6P`, `ABR`, `CLG`, `CTI`, `HYA`, `HYB`, `HYE`, `PC4`, `PC4S`, `PQT`, `RBR`,
  `RNC`, `RNT`, `SGT`, `SI1`, `SI2`, `SI3`, `TCF`, `TRJ`, `TSG`, `WTS` and `XTS`, and no substring
  search for `OLT` reaches any of them.
- **The alternatives were checked before `OLT` was chosen**, and the check is recorded so that the
  choice is not re-litigated. `OLR`, act 19's reserved stem, is **not** reused: act 19's closure
  records that `R7-OLR` and `_OLR_` remain free names outside act 19's directory, and reusing them
  would make this round look like act 19's execution resumed, which it is not — a fresh round takes
  a fresh stem so that no search for act 19's objects can find act 21's. `OLT` — orbit-law rigidity,
  twisted — names what changed. `RNT` is act 20's and is excluded on that ground alone.

**The round directory and the module name are free at this base too.**
`git grep -- 'act-21'` returns two hits, both in `verification/infrastructure/`, both stating that a
seal-infrastructure round is **not** act 21 — `SI-1`'s precondition that act 21 had not begun, and
`SI-3`'s non-licence clause — and neither names a path; `git grep -- 'OrbitLawRigidityTwisted'`
returns nothing. The round directory is
`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/` and the module is
`verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`. The prose mentions of "act 21" at
this base — in act 20's control plane and result, in the guard's `R7-RNT` clause, in the census
entry for act 20's module, in act 20's Lean module and in the `SI` rounds' documents — all say the
same thing: that act 21 is the round in which the naturality choice is made, and that nothing before
it adopts a part of its ladder. None is a collision, and none is a commitment about this freeze
beyond that.

**Two nearby names are recorded so that they are not mistaken for collisions.** Act 19's directory
`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/` exists at this base and holds
exactly two files, its control plane and its closure; no `OrbitLawRigidity.lean` exists anywhere in
the tree. **A shared English phrase is not a collision**, and the freedom check above is by exact
string and not by theme.

### What this round does NOT own, named exhaustively

It alters **no existing manifest record**. The twenty-five records under `verification/seals/` at
this base — the seals tree `1abe1c988b1cb0a5fd119bbae8bd7108933334a4` — are **read and never
written**; the declared baseline holds them against mutation, removal and unauthorized addition on
every run, and the one addition it authorizes is `OLT`. It writes **no legacy constant**. It does not
re-pin, re-derive or re-declare any other round's seal: `SI3.json`, `RNT.json` and the rest belong to
the rounds that set them. Inside the guard file the execution **adds** the `R7-OLT` clause, **sets**
the two stem-free declarations named above, and **edits four contracts in three closed rounds'
guards at exactly the places the supersession table names** — and changes nothing else in the file.
An archive seal belongs to the round that set it: touching the guard file that carries a closed
round's clause does not make this round its owner, and the supersession table is the whole of what
this round is authorized to touch there.

## Provenance — this freeze re-freezes act 19's experiment, and says exactly how

**The rule, set by the owner.** Act 21 adopts act 19's mathematical ladder unchanged except for
replacing the contaminated `L4n` by the certified `N-TWIST` predicate from act 20, keeping `L0`,
`L1`, `L2`, `L3i`, `L3s`, `L4d` and `L5` at the same mathematical strength, inheriting the
already-owner-settled choices — `L5` stays; the `L3` finiteness route remains permitted with its
required reporting — and keeping act 19's candidate set, quotient list, per-rung restriction tests,
headline semantics, discriminating test and status rule. **Only mechanical changes required by the
new round — names, current merged references, the manifest lifecycle, the chronology controls — are
allowed**, and the provenance is explicit so that an auditor can diff this file against act 19's
blob and account for every difference.

**How this file was produced.** Every section listed as *carried* below was taken **by line range
from act 19's preregistration blob `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`** at `B`, with the
substitutions in the next table applied and nothing else changed; every section listed as *new* was
written for this round. The two mandatory verbatim clauses — the start-state discrepancy clause and
the anti-contamination invariant — are among the carried lines.

| act 19 lines | section | status |
| --- | --- | --- |
| 289–293 | Source scoping | carried; "acts 13 through 18" → "acts 13 through 20" |
| 295–366 | Why this round exists; what it inherits; what the merged record supplies | carried; act 20 added as an inheritance item and a table row; consumed-declaration list extended |
| 368–399 | The question; the strength of the ask | carried verbatim |
| 401–487 | The objects; the orbit state space; the frozen quotient list | carried; act 20's declarations appended to the consumed list; "before act 19" → "before act 21" |
| 489–548 | The ladder's preamble, `L0`, `L1`, `L2`, `L3i`, `L3s` | carried verbatim |
| 550–553, 559–564 | `L4`'s heading and `L4d`, with `L4d-HYP` | carried verbatim |
| 554–558, 566–571 | act 19's `L4n` and its paragraph | **replaced** — the one mathematical change |
| 573–651 | `L5`, the `L5` test, the rung labels | carried verbatim |
| 653–723 | The ordering obligation and its five records | carried; the module path in record 4; the attestation set and the anti-expansion rule appended as new subsections |
| 725–991 | `OL1`, the headlines, `SIOP`, the seven candidates | carried; one paragraph on act 20's merged `RelabelTransition`/`RelabelLift` added under `ΦP` |
| 993–1055 | The witness supply and the countercontrols | carried; supply 5's last clause reworded to act 20's notion; supply 6 (act 20's lift) added; the `L4n` row restated |
| 1057–1187 | The evidence rule and the six targets | carried; one paragraph naming act 19's and act 20's files in the `OL0` file set added |
| 1189–1224 | The predictions | carried; the `L4n` row's reason restated; the `OL3` row's reason extended by one sentence |
| 1226–1455 | The status rule and the `P0` sentences | carried; "Act 19 asks" → "Act 21 asks"; "acts 11 through 18 stand" → "acts 11 through 20 stand" |
| 1457–1572 | Naming is not endorsing; THE CLAUSE; what no outcome licenses | carried; "Act 19 classifies" → "Act 21 classifies" in THE CLAUSE; "Acts 11 through 18" → "Acts 11 through 20"; items 25–27 appended |
| 1574–1671 | Named hazards | carried; hazards 28 and 30 restated for the manifest; 32–34 appended |
| 1673–1727 | Non-doings; out of scope; what the round changes about `P0`; the direct-branch statement | carried; "act 19" → "act 21" (three); the seal-constant non-doing restated; act 19/act 20 boundary non-doings added; `RNT1`–`RNT6` added to the merged-label list; "acts 12, 17 or 18" → "acts 12, 17, 18 or 20" |
| 1729–1785 | Definition budget; evidence level | carried; the `L4n` inline sentence restated; act 20's definitions added to the reused list |
| 1787–1875 | Act 19's chronology control and preconditions | **replaced** by this round's, under the manifest protocol |
| 1877–1902 | Execution discipline | carried; the guard-clause bullet and the landing bullet restated for the manifest; an attestation bullet added |
| 1904–1949 | Allowed final report | carried; items 1, 2, 14 and 16 restated; item 19 added |
| 1951–2057 | Owner settlements and open decisions | **replaced**: act 19's twelve calls carried, its three open decisions recorded as settled, this round's settlements added |
| 1–287 | Title, shape, freedom checks, locating controls, start state | **replaced** by this round's |

**The substitution list is the generator's own record and is reproduced in full at the end of
this file**, so that "mechanical" is checkable rather than asserted.

**One consequence of the rule is stated so that it is not mistaken for an oversight.** The carried
predictions are act 19's predictions, including the predicted `SIOP` witness from the initial class
of `H(1)`. Act 19's closure, at its lines 98–106, records that act 19's **uncertified** execution
substituted another member of the frozen witness supply for that class, having found in its own
kernel that the predicted class cannot diverge under the simultaneous relabelling, and rules that
the substitution was a legitimate outcome of an existential target and not an ordering failure.
That record is a statement about an uncertified execution and is **not evidence here**; the
prediction is carried as the owner directed, the target is existential over the initial class and
the trajectories exactly as act 19 froze it, and an execution that witnesses `SIOP` at another member
of the frozen supply reports, as act 19's closure says, that the predicted witness failed and the
existential target was witnessed differently. **No configuration outside the frozen supply may be
substituted**, and that rule is act 19's too.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`**. Every quotation below is
verbatim from a blob pinned in the start-state table, with its file and line coordinate.

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

### The manifest protocol, in the three passages this round executes under

`AGENTS.md`, **lines 879–889**, from the subsection *Sealing through the manifest, from `SI-2`'s
landing* that opens at line 871:

> **The seal record is data, not code.** A round's seal state lives in one JSON
> record per round under `verification/seals/`, `<STEM>.json`, validated by the
> generic validator `SI-2` made authoritative: the discriminated union `SI-1`
> built, `kind: "sealed"` carrying `base`, `sealed_head` and `merge`, or
> `kind: "base-only"` carrying `base` alone and forbidding the other two, a
> forbidden field being a failure even as null. The guard's clause for a round
> is a call to that validator keyed on the round's record, and nothing else
> gates. Manifest integrity is data-driven: against the record set fixed at a
> round's start, a record mutated, removed or added is reported as such, and a
> round's only permitted change to the set is the addition its own
> preregistration authorizes.

`AGENTS.md`, **lines 941–952**, from the subsection *The representation retired, from `SI-3`'s
landing* that opens at line 936 and governs rounds begun after `SI-3`'s landing merge — which this
round is:

> **The legacy representation is retired.** From `SI-3`'s landing the guard
> file carries **no legacy seal constant** — no module-level `_<STEM>_BASE`,
> `_<STEM>_SEALED_HEAD` or `_<STEM>_MERGE` — **no shadow** of a manifest
> verdict, and **no per-round seal-integrity comparison**. `SI-3` removed them
> against `SI-2`'s frozen inventory plus `SI-2`'s own base constant: sixty-two
> statements over sixty names, twenty-three shadows, five comparators. A round
> that writes any of them again fails the standing contract `SI-3`'s guard
> keeps — **zero legacy assignment statements in the file** — and has
> recreated the representation that was retired. Every read of a round's seal
> state goes through the **manifest accessor**, one function that returns a
> named field of one round's record and fails closed where the record or the
> field is missing.

`AGENTS.md`, **lines 954–962**, how a sealing round carries its base while it executes:

> **How a sealing round carries its base while it executes.** It writes no
> constant. It declares its mandated execution base, by stem, in the
> **prospective declaration** — a stem-free mapping outside the validator's
> marker-bounded regions, handed to the validator as its prospective input —
> and the validator classifies the round `EXECUTION` against that base through
> act 10's strengthened check, and `LANDED-PENDING-PIN` at its landing merge.
> **`P` removes the entry when it writes the record**, so that from `P` on the
> round is classified from its record alone; a stem that is both declared and
> recorded is a failure.

`AGENTS.md`, **lines 964–970**, how manifest integrity is declared:

> **How manifest integrity is declared.** The data-driven rule holds the
> manifest against a **declared baseline**: the seals tree at the current
> round's mandated execution base, read from git, plus the additions the
> current round's preregistration authorizes, by stem. An authorized addition
> is admitted by stem here and validated by content by the validator; anything
> else added, and anything mutated or removed, is reported as such and fails.
> Each round declares its own baseline; no round's guard hard-codes another's.

`AGENTS.md`, **lines 972–978**, the closed-round rule, which is the authority for the supersession
table below:

> **A closed round's contracts are read over the records it manifested.** A
> landed round's manifest-cardinality and integrity contracts — its record
> count, its authorized-addition set, its census and its probes — are evaluated
> over the records that round manifested, and a later round's authorized
> additions are outside that historical scope. This is the rule `SI-2`'s
> Amendment 1 applied to `SI-1` and `SI-3` applied to both `SI-1` and `SI-2`;
> stated here once, it needs no per-round amendment again.

### The obligation, and the part of it act 18 opened

`verification/ROADMAP.md`, **line 63**, the `P0` row's obligation cell and its status opening —
the row is at the same blob as at act 19's freeze, `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da`, act
19 having appended nothing to it and act 20 having been frozen to append nothing:

> | **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED: act 11's `GL2` proved the visible family does not fix the relative evolution;

and, from the same line, the sentence that makes the row two-part and names this round's part first:

> so what remains is **two-part**: what selects or constrains the Gram/orbit trajectory **across time**, and what determines the cross-time threading within those orbits, which act 11's `GL2` shows is not fixed even by the full Gram trajectory

and, from the same line, the clause act 18 appended, which is the baseline this round starts from:

> On the structural-law axis, which asks whether a constraint writable from the anchor and the visible family alone is proper and propagates, one named generator law, written at orbit level so that it descends, has a solution set at one exhibited configuration that is nonempty, non-singleton modulo the round's cross-time equivalence and proper, and two of its solutions agreeing at the initial time have the same trajectory.

### The act 17 baseline, the two-axis precedent and the interpretation boundary

`verification/ROADMAP.md`, **lines 560–565**, beginning part-way through line 560:

> **there is no additional universal cross-time constraint on coherent Gram trajectories
> beyond pointwise realizability** — the present notion of coherence contributes no coupling between
> times at all, and **any such law must enter as additional structure**. The narrowing act 12's rank
> bound effects is **pointwise** and is labelled pointwise. This is a statement about coherence as
> the programme defines it, indexed by the naturals and pointwise in time, and **not** a statement
> that no cross-time structure could be added to the programme.

`verification/ROADMAP.md`, **lines 585–587**:

> **The two findings are on two axes and are not merged into one ordering.** "The present notion of
> coherence imposes no cross-time coupling" is not above or below "these four proposed selectors all
> fail at one admissible configuration": they answer different questions.

`verification/ROADMAP.md`, **lines 52–57**:

> Accordingly, a failure of uniqueness at `P0` is not by itself a failure of quantum emergence. It
> determines the ontology of that emergence: either the residual lift freedom is physically redundant,
> additional structure selects one quantum history, or observational incompleteness determines only an
> equivalence class of quantum histories. Only an empirically distinguishable residual not removed by
> the physically appropriate equivalence relation would license a claim of physics beyond standard
> quantum mechanics.

### The act 18 result this round consumes

`verification/programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure/result.md`,
**line 13**:

> **The headline is the ORDERED PAIR of two co-equal axis outcomes:** **(`D-MID`, `L-PROP`)**. The

and **lines 145–146**, beginning part-way through line 145:

> `xs1_pointwise_not_propagates` is the consequence:
> `PointwiseLaw Law → ¬ PropagatesFrom a₀ Γ Law`, at every configuration.

and **lines 446–448**:

> **The descent obligation is DISCHARGED, by the first of the two routes the freeze permits.** The
> candidate is **written directly as an orbit-level transition** `[G_{t+1}] = Φ([G_t])`, with `Φ` the
> identity on per-slice orbit classes, rather than as a representative-level `V_t` that would then

### Act 19's closure — what stands, what is uncertified, and what a successor may use

`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/closure.md`, **lines 3–6**:

> **Act 19 terminates without a rigidity headline.** Its control plane was frozen and merged and
> remains valid; an execution was run against it and is not certified. This note exists so the
> repository carries a durable account of why there is a control plane in this directory and no
> result note beside it.

**lines 82–83**, the adjudication:

> Either ground alone closes the round. Together they settle it: **`ae983580` is act 19's
> uncontaminated ladder boundary, and `52b64009` is a post-ladder, candidate-informed weakening.**

**lines 108–110**, the rule that binds this round:

> **The lower-level proofs on the execution branch remain available as research material.** They are
> not evidence for any later round, and no later round may cite them as settled. Anything a successor
> wants from them it proves again under its own freeze.

**lines 129–137**, the question the closure left to a later round:

> The third is what `52b64009` states, and it should not be called commutation. The scientifically
> interesting question — which act 19 could not settle, because settling it during execution is exactly
> what the ordering obligation forbids — is whether the freeze intended the first or the second.
>
> **That question belongs to a later round with its own freeze**, and this closure neither answers it
> nor prejudges it. The observation to carry forward is that a condition asking one object to respect
> another's symmetry is not fully stated until the respecting is pinned to a particular map, and that
> the difference between the three rows above is the difference between a rigidity verdict that means
> something and one that does not.

**This round answers that question by owner settlement — the second row — and the answer is recorded
in the settlements section, not argued here.** The closure's register is kept throughout: the
distinction is between a statement being **refuted** and a statement being **uncertified by that
round**, and nothing in this file says act 19's mathematics is false.

### Act 20's classification, the input the naturality choice was made against

`verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md`, **lines
537–544**:

> **Outcome reached: `CLASS-TWISTED-NOT-STRICT`.** The composition rule the freeze fixes requires
> `LAW-EXACT` with `ALPHA-NONTRIVIAL` **and** `STRICT-NO`, and all three inputs landed at the full
> evidence bar frozen for each.
>
> > The lift this round built is **twisted-natural and not strictly natural**: an exact intertwining
> > law holds with exhibited maps on both sides, at least one of those maps is not the identity at an
> > exhibited gauge element, and an exhibited pair witnesses the failure of strict equivariance —
> > each at evidence level 2 and each earned separately.

**lines 562–564**, the separation status:

> **The separation status is carried beside the classification and not folded into it**:
> `SEP-STRICT` on the left side and `SEP-STRICT` on the right side, each at the configuration its own
> witness pins.

**lines 205–207**, the finding about the attestation instrument that this round acts on:

> **Act 21's freeze should set the attestation span to end at its own
> definition-commit analogue**, and that is recorded as a finding of this round about the instrument
> rather than about the mathematics.

and, from act 20's control plane,
`verification/programmes/oi-qm/track-b/act-20-representative-naturality/preregistration.md`,
**lines 497–504**:

> **Act 21 is a fresh rigidity round with its own freeze, written only after act 20 is merged, pinned
> and reviewed.** It is not a continuation of act 19's execution, not a re-run of act 19 with one rung
> edited, and not a resumption of anything. Nothing in act 20 — no label, no theorem, no
> recommendation, no observation — is a commitment about act 21's ladder, its quotient list, its
> candidate list or its headline. **Whatever act 21 imposes as its naturality condition, it imposes in
> its own control plane, with its own reasons, and it may impose a condition act 20 classified as
> failing, as holding, or as undecided.** Act 20's merged result is an input to that decision and is
> not the decision.

**Act 20 classified and chose nothing; the choice is made here, by the owner.** Act 20's `RNT6`
sentence — "that choice is the owner's and it is made in act 21's preregistration" — is honoured by
this file being where it is made.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `d2c949f09f630f238e964308bbde9a9d8bec6279` |
| `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md` | `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057` |
| `verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/closure.md` | `3d37529cb89a4d2bb60281f14f15645e3beaeb4c` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/preregistration.md` | `131783f48ac492fdfdc46072aee3f39278973622` |
| `verification/programmes/oi-qm/track-b/act-20-representative-naturality/result.md` | `6f2d2c6a70eda2806e41b88b3b9fe5d4292f46db` |
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
| `verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean` | `4c1137f35600320b9273c857ec62271341b05cd0` |
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
| `verification/seals/RNT.json` | `546965414aa47fa9b9554448e9c5d13d52f81109` |
| `verification/seals/SI3.json` | `7c447c3fff08e47abee5bb653dd705919b550813` |
| `verification/seals/` (tree) | `1abe1c988b1cb0a5fd119bbae8bd7108933334a4` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

### The files this round writes

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` | **read** as the pinned statement of the `P0` row, of act 17's baseline and of the programme interpretation boundary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label unchanged |
| `verification/lean/edge_rigidity_probe.py` | `8b999f7a86d95dbc6a2871c0fe4be3f0bbcd64c9` | the `R7-OLT` clause **added**; `_MANIFEST_PROSPECTIVE` and `_MANIFEST_BASELINE` **set** as the shape section states, the former emptied by `P`; the supersession table's **four edits** in `R7-SI1`, `R7-SI2` and `R7-SI3`; **nothing else**; no legacy constant written |
| `verification/lean-mathlib/OIBridge.lean` | `69de4a29ea7744f0de85cfd099fb7f6d01d7fea5` | one import line added after act 20's module, line 209 |
| `verification/lean-manuscript-census.json` | `a256f914854c157277060519ab630af47c395897` | one census entry added for this round's module |
| `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` | — | created by the execution |
| `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/result.md` | — | created by the execution |
| `verification/seals/OLT.json` | — | created by **`P`**, and by nothing before `P` |

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

**Why this matters here, concretely.** This freeze is written against `63d8ca0` alone and consumes
nothing from any lane that lands after it. No lane's unlanded output is read, cited, compared or
waited for. **And the same clause reaches backward**: the branch `claude/act-19-execution` is
present in the repository and is consumed by nothing — it is not in the start-state table, it is not
a blob at `B`, and act 19's closure forbids citing it.

## Source scoping, carried from acts 13 through 20

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

### What act 21 inherits, and consumes without re-proving

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
8. **Act 20's three notions, its lift and its classification, at merged strength.** `StrictNatural`,
   `TwistedNatural` and `OrbitNatural` are act 20's frozen `Prop`s; `RelabelTransition σ` is act 19's
   `ΦP` statement carried into Lean; `RelabelLift σ` is one lift of it with `rnt2_lifting_property`
   and `rnt2_admissible`; `rnt3_law_exact` is `TwistedNatural a₀ (RelabelInducedLeft σ)
   (RelabelInducedRight σ) (RelabelLift σ)` at arbitrary `V`, `A` and anchor; `rnt4b_not_strictNatural`
   and the two `rnt5_*_separation` theorems are the negatives. **This round consumes the notion as its
   `L4n` and the lift as its starting point for `ΦP`'s `L4n` obligation**; it does not re-prove, restate
   or enlarge any of them, and act 20's `RNT6` — a classification of one lift, choosing nothing — is
   read as exactly that.

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
| whether the carrier relabelling's transition has a representative-level lift intertwining with the gauge classes up to fixed induced maps | **yes**, for the one lift act 20 built, on both sides, the maps exhibited and not the identity, the lift not strictly natural | act 20's `RNT3`, `rnt3_law_exact`; `RNT4`; `RNT6` `CLASS-TWISTED-NOT-STRICT` |
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

## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13, 17, 18 and 20

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
`xs5_l_axis_prop`; and act 20's `StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition`,
`RelabelLift`, `RelabelInducedLeft`, `RelabelInducedRight`, `rnt1_strict_imp_twisted`,
`rnt1_twisted_imp_orbit`, `rnt2_lifting_property`, `rnt2_admissible`, `rnt3_left_closure`,
`rnt3_left_law`, `rnt3_right_closure`, `rnt3_right_law`, `rnt3_law_exact`, `rnt3_orbit`,
`rnt4a_left_nontrivial`, `rnt4a_right_nontrivial`, `rnt4b_not_strictNatural`, `rnt5_left_separation`
and `rnt5_right_separation`.

**Act 7's boundary is carried at every use of the visible family**, exactly as acts 11 through 20
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
before act 21 and each traceable to the round that established it.** The list is closed at this
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
> **`L4n` — representative-level gauge-naturality, at act 20's certified strength.** At every `t`,
> `Φ t` admits a representative-level lift that is **twisted-natural** in act 20's frozen sense
> `N-TWIST`: there are a map `Ψ_t` on dilations and maps `αL_t`, `αR_t` on dilations, all three
> **fixed before the quantifier over inputs**, such that
> **(i) lifting** — `FibreGram a₀ (Ψ_t U) = Φ t (FibreGram a₀ U)` for every `U` admissible for
> `Γ t` at `a₀`;
> **(ii) admissibility** — `Ψ_t U` is admissible for `Γ (t+1)` at `a₀` for every `U` admissible for
> `Γ t` at `a₀`; and
> **(iii) twisted equivariance** — `TwistedNatural a₀ αL_t αR_t Ψ_t`, act 20's declaration consumed
> unrestated, whose four conjuncts are `LeftFibreGroup L → LeftFibreGroup (αL_t L)`,
> `WeakAnchorStabilizer a₀ K → WeakAnchorStabilizer a₀ (αR_t K)`,
> `LeftFibreGroup L → Ψ_t (L * U) = αL_t L * Ψ_t U` and
> `WeakAnchorStabilizer a₀ K → Ψ_t (U * K) = Ψ_t U * αR_t K`, each quantified over all `L`, `U`
> and `K`.

**`L4d` is the shared theorem's own hypothesis, and the freeze says so before the census.** The
theorem below assumes quotient-well-definedness, so `L4d` cannot be a further restriction on the
action class that theorem produces: **its honest rung status is `L4d-HYP`**, and the result note
reports it as a hypothesis and not as a discharged rung. Saying this **now**, before any survivor is
known, is what keeps it from being an excuse later.

**`L4n` is the one rung this freeze restates, and it is restated at act 20's certified strength and
at no other.** Act 19's wording asked that the transition "commute with the merged transformation
laws"; act 19's closure found that phrase underspecified between three notions — strict
equivariance, twisted equivariance for one fixed map, and orbit preservation — and act 20 formalized
the three, built the carrier relabelling's representative-level lift, and certified that lift
**twisted-natural and not strictly natural** (`CLASS-TWISTED-NOT-STRICT`), with the per-input
existential **strictly weaker** than the fixed-map form on both sides (`SEP-STRICT (L)`,
`SEP-STRICT (R)`). **The owner chose the second row**, and the choice is recorded in the settlements
and not argued for here: `L4n` is `TwistedNatural` itself, with the two lifting obligations act 20's
`RNT2` fixed for a lift, stated across one time step.

**Three things about the statement are fixed here so that they cannot drift.** First, the
**quantifier order** is `∃ Ψ_t αL_t αR_t, ∀ L U K` and never `∀ L U K, ∃`: the maps are fixed before
the inputs, which is the whole difference between `N-TWIST` and `N-ORBIT`, and is exactly what act
19's execution lost at `52b64009`. Second, **no constraint is placed on the induced maps beyond act
20's two closure conjuncts.** `αL_t` and `αR_t` are not required to be the identity, to be
homomorphisms, to be induced by any map of the carrier, or to stand in any relation to `Φ`; a
candidate-specific constraint on them would be a different rung, and this freeze does not write one.
Third, **(i) and (ii) are act 20's `RNT2` obligations and nothing more**, stated of an arbitrary lift
across one time step; at the frozen configuration `Γ` is constant, so (ii) is act 20's
`rnt2_admissible` shape exactly, at a visible slice invariant under every permutation of the
carrier.

**`L4n` is tested as a genuine restriction, exactly as act 19 tested it.** Descent says the
transition is a function on classes. `L4n` says it comes from a move on representatives that
intertwines with the invisible gauge up to fixed induced maps on each class. The second does not
follow from the first, and act 18 named the alternative route explicitly: its `LC3` discharged
descent **by writing the candidate at orbit level**, precisely so that a representative-level
naturality proof would not be needed. **This round tests whether the representative-level property,
at act 20's strength, is a restriction**, and records the result either way.

**Analysis, recorded here as the freeze's reading and not as a finding.** With the induced maps
unconstrained, the identity lies in both gauge classes — act 12's `one_leftFibreGroup` on the left,
and on the right the identity satisfies act 11's weak-stabilizer definition at every anchor, a
one-line check the execution carries out if it uses this route — and a lift that **ignores its
input**, `Ψ_t U = U₀` for one fixed admissible `U₀`, satisfies the conjuncts of (iii) with
`αL_t ≡ 1` and `αR_t ≡ 1`: both intertwining equations read `U₀ = 1 * U₀`. So the constant transition
`ΦC`, whose value is one class, is expected to satisfy `L4n` through such a lift, with `U₀` supplied
by act 12's `sh1_sufficiency`; it fails `L3i` and `L3s` and is not a survivor, so nothing about the
headline turns on this. What the observation says is that the intertwining conjuncts of `N-TWIST`
bind a lift only **through the lifting obligation (i)**, which ties `Ψ_t` to `Φ t`; whatever content
`L4n` has on the class the shared theorem produces is carried by (i) and (iii) jointly. The freeze
records this so that a `L4n-FREE`, if reached, is read as a fact about the notion at act 20's
strength and not as a surprise, and it **adds no conjunct**: the owner's direction is that `L4n` is
act 20's notion itself, and a freeze that tightened the maps after writing this paragraph would be
doing at drafting time what the ordering obligation forbids at execution time.

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
   `git diff <discrimination commit> <E> -- verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`
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

### The attestation set — act 20's three questions, scoped from the mandated base to the LADDER commit

**Act 19's ordering obligation was honoured in every respect an audit of the branch can check, and
the round still closed uncertified**, because what contaminated it arrived by pen-and-paper
reasoning that no commit records. Act 20 answered that with a third attestation question, and
recorded as a finding about the instrument that its own frozen span — base to discrimination commit
— ended too late, after the interval in which the answer matters. **This freeze carries the three
questions and ends the span where act 20's result says it should end: at the ladder commit, record
2.** From the ladder commit on, discriminating work is what the round is supposed to be doing.

**The result note answers all three, in this wording, for the span from the mandated base `B` to
the ladder commit:**

> **Q1 — INTENTIONAL.** Did the execution attempt or run any proof, search, decision procedure or
> numerical experiment intended to reveal which of the frozen candidate laws satisfies or fails any
> rung, whether any rung is implied by the earlier rungs, or whether a same-initial-orbit pair
> exists?
>
> **Q2 — INCIDENTAL.** Did any compiler response, elaboration result, typeclass resolution, accepted
> or rejected term, or build output reveal any of that unintentionally?
>
> **Q3 — UNAIDED REASONING.** Did the execution **reason its way** to any information bearing on
> which laws survive, on which rungs restrict, or on the discriminating pair, **without running
> anything**?

**A PARTIAL fact counts for all three.** Learning that one candidate satisfies or fails one conjunct
of one rung, or that one rung is implied by the earlier rungs on one input, is already
discriminating. **A question is answered YES if any such partial fact was acquired**, however
incidentally, however small, and whether or not it was acted on. There is no threshold below which
a fact about the census does not count.

**What the freeze itself places in front of the execution is not a YES, and is listed rather than
left implicit.** This file carries act 19's predictions and countercontrol table, the `L5` test,
the reason column of the prediction table, the analysis paragraph under `L4n`, and — through the
start-state table — act 20's merged theorems, including `rnt3_law_exact`, which states that the
carrier relabelling's lift is twisted-natural, and act 19's closure, which records what an
uncertified execution found. Reading those is reading the freeze. **The result note lists which
freeze-supplied facts were in front of it**, as act 20's note did at its §4, so that the owner can
weigh them rather than discover them; the three questions are about what the execution acquired
**beyond** the freeze and the pinned blobs.

**How a YES is handled, frozen before it can be needed.** A YES is **disclosed**, with what was
learned, when it was learned relative to the ladder commit, and whether any rung statement changed
afterwards. It is not concealed and it is not argued away. **A disclosure does not cure a
contamination** — act 19's closure is explicit that its disclosure established the contamination
rather than curing it — and equally a YES does not by itself void the round: what it does is put
the adjudication in front of the owner with the facts stated. **A YES followed by a change to any
rung's statement before the ladder commit is act 19's failure exactly**, and a round in that
position is reported with the ordering obligation named as undischarged. **Concealment is the defect
this set exists to prevent**, and an execution that answers all three NO is making a substantive
claim that the rest of the record must be consistent with.

**The ladder commit's boundary is stronger here than act 20's definition commit's was, and the
freeze says so rather than claiming more than that.** Act 19's ladder can be stated without
determining which laws survive it, whereas act 20's definitions could not be stated without
determining the induced map. The attestation runs all the same, because the ladder commit checks
that no rung was *restated* after the fact and cannot check that no survivor was *known* before it.

**The three answers are reported as measurements and not as intentions**, in the result note's own
words, beside the five records.

### The anti-expansion rule, FROZEN

**If execution discovers an eighth candidate law, a further equivalence under which survivors would
collapse, a further rung, a further configuration, or a strengthening of a merged theorem that would
bear on the headline, it is recorded as an observation for a later round with its own freeze and is
not executed here.** The candidate list is closed at seven, the quotient list at three, the ladder at
`L0`–`L5`, and the configurations at those the countercontrol table names. This rule restates, in one
place, the closure the candidate list, the quotient list and the ordering obligation each carry for
their own object, so that an execution cannot expand one by reading the others narrowly. An
observation so recorded carries no label, earns no line of the headline, and is not evidence for any
verdict of this round.

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

**Act 20 carried this statement into Lean and it is consumed at merged strength.** `RelabelTransition
σ` is act 19's `ΦP` statement, `RelabelTransition σ G i j k = G (σ i) (σ j) (σ k)`, and `RelabelLift
σ` is one representative-level lift of it, with `rnt2_lifting_property`, `rnt2_admissible` and
`rnt3_law_exact` merged. **This round reuses those declarations and does not restate `ΦP`**; what
it proves about `ΦP` — its `L-PROP` conjuncts and its rungs — it proves under its own freeze.

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
   laws on `FibreGram` — the classes act 20's `TwistedNatural` is stated against, and so what `L4n`
   consumes.
6. **Act 20's lift and its exact law**: `RelabelLift σ`, `RelabelInducedLeft σ` and
   `RelabelInducedRight σ`, with `rnt2_lifting_property`, `rnt2_admissible` and `rnt3_law_exact`
   merged at arbitrary `V`, `A` and anchor — the starting point for `ΦP`'s `L4n` obligation at the
   frozen configuration, and for `ΦPP`'s at the product configuration.

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
| `L4n` | **named and expected hard**: a transition descending to classes with no twisted-natural representative-level lift satisfying the lifting obligation. The freeze names no construction and rates it accordingly; the constant-lift analysis under `L4n` says where such a construction would have to bite; **UNDECIDED with the obstruction named is an allowed outcome and is not a shortfall** | supply 5 and 6 |
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

**Four more members of the file set at `B` are named in advance for the same reason.** Act 19's
control plane, act 20's control plane and act 20's result are `preregistration.md` and `result.md`
files under `verification/programmes/oi-qm/`, and act 20's module is a `*.lean` file under
`verification/lean-mathlib/`; act 19's closure is neither and is outside the set. Their hits are
asked the question like any other hit, and the freeze records its reading in advance — act 19's
control plane is a specification and not a decision, and act 20's result says in terms that it
classifies one lift against three notions and decides nothing about any ladder — while the
finding is whatever the execution's own search records.

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
| `L4n` | not predicted | **low** | Both predicted survivors have twisted-natural lifts at act 20's strength — the identity, with `αL = αR = id`, which is act 20's `RNT1` (a) shape; and the carrier relabelling, by act 20's merged `rnt3_law_exact` with `rnt2_lifting_property` and `rnt2_admissible` — so neither witnesses a restriction; the freeze names no transition descending to classes without such a lift; and the analysis under `L4n` records that the intertwining conjuncts alone are satisfied by a constant lift, so any restriction would have to come through the lifting obligation. **UNDECIDED with the obstruction named is an allowed outcome and is the freeze's expectation.** |
| `L5` | **`L5-RESTRICTS`**, via `ΦCTRL` | **medium** | The two-instance refutation is finite and does not quantify over the orbit space. The medium rating is for the product-embedding construction the rung needs — that the Kronecker product of admissible dilations is admissible for the product family and that its fibre-Gram tuple is the Kronecker product of the factors' — which act 18's `prod_admissible` starts but does not finish. **`L5-UNDECIDED` is an allowed outcome and is not a shortfall.** |
| `OL3`, the census | **`ΦI` and `ΦP` survive every rung at the frozen configuration; `ΦX`, `ΦC` and `ΦT` each fail the rung they are named for; `ΦPP` satisfies `L5` and `ΦCTRL` fails it** | **medium** | Each is the countercontrol table's own entry. The medium rating is for the `L-PROP` conjuncts of `ΦP`, which the freeze reads as following from `σ² = id` and act 12's merged inequivalences but which no merged result states. `ΦP`'s `L4n` is predicted discharged by act 20's merged lift and exact law at the frozen configuration, where `Γ ≡ ¼` is invariant under every `σ`, and `ΦI`'s by the identity lift with identity induced maps. |
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

> `P0` remains open and two-part, and the answers of acts 11 through 20 stand exactly as those rounds
> state them. Act 18's structural-law axis reached its top line: a law writable from the anchor and
> the visible family before any lift exists, stated at orbit level so that it descends, together with
> one initial orbit, propagates uniquely. Act 21 asks how rigid the class of such laws is, against a
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

Acts 11 through 20 each carry the non-doing "names, endorses or excludes no selection principle".
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
> Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
   > Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
25. **Any adjudication of act 19's uncertified execution, in either direction.** No sentence of this
    round says that anything act 19's closure lists as uncertified is refuted or is established, and
    nothing from `claude/act-19-execution` is cited, imported, adapted or counted. Everything this
    round uses it proves under its own freeze, which is what act 19's closure requires at its lines
    108–110.
26. **"Act 20 chose `N-TWIST`", "act 20 recommends the twisted form", or any sentence that reads act
    20's classification as a choice.** Act 20 classified and chose nothing; the choice of `N-TWIST`
    is the owner's, made in this freeze, and no artifact of this round attributes it elsewhere or
    rates the three notions against one another.
27. **"`L4n` is act 19's `L4n`", or any report of the rung as unchanged from act 19.** The rung is
    restated at act 20's strength and the restatement is this freeze's one mathematical change; the
    result note says so where it reports the rung.
## Named hazards

1. **A post-hoc rescue condition.** **This is the strongest hazard in the round.** The specific failure
   guarded against is an execution that finds a plurality, adds "one more physically reasonable
   condition", and reports `L-RIGID`. The ordering obligation and its five records exist for it.
   > **THE CLAUSE, carried at this mention — the hazard list.**
   > Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
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
    treating `L` as the end of it: at `L` the validator classifies `OLT` as `LANDED-PENDING-PIN`,
    permitted, and every head descending from that unpinned landing fails as *seal pending* until
    `P` writes `verification/seals/OLT.json` and removes the prospective entry.
29. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
30. **A stem both declared and recorded, or a legacy constant written.** The specific failure guarded
    against is a `P` that writes the record and leaves the prospective entry in place — which the
    validator fails — or an execution that writes `_OLT_BASE`, `_OLT_SEALED_HEAD` or `_OLT_MERGE`,
    which recreates the representation `SI-3` retired and fails its standing zero-statement contract.
31. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.
32. **Contamination that no commit records.** Act 19's failure: candidate-specific information
    acquired by unaided reasoning before the ladder was fixed, and a rung rewritten in its light. The
    attestation set's third question and the partial-fact rule exist for it, and the span ends at the
    ladder commit.
33. **Consuming act 19's execution branch.** Its proofs are research material and nothing else; a
    successor that wants any of them proves them again under its own freeze, and this round cites
    nothing from it.
34. **A supersession outside the table.** The execution edits `R7-SI1`, `R7-SI2` and `R7-SI3` at
    exactly the four places the supersession table names, and nowhere else; a failure elsewhere in
    those guards is a result requiring adjudication and not a repair.
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
strengthen acts 12, 17, 18 or 20**; revise `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`,
`TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`, `AB1`, `AB2`, `CT1`, `CT2`, `CT3`, `CT4`, `CL1`, `PQ0`–`PQ4`,
`CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3`, `XS0`–`XS5`, `RNT1`–`RNT6` or any merged label; answer act 13's fork `CT3` (d)
or move it in either direction; redefine act 12's `GramPhaseEquiv` or act 17's `GramTrajEquiv`; test a
law outside the frozen list; realize the transition as an operator, unitary, generator or group
element; change `CoherentLift`'s `ℕ`-indexing or introduce continuity, smoothness or a generated
evolution; introduce a further carrier or revise any of act 14's four; resolve, reopen or narrow act
10's anchor-axis reclassification; report a bounded verdict as a general impossibility; change `D3`,
`D4b`, `D5`, the direct-branch statement or the readback convention; alter any existing manifest record, or
write a legacy seal constant; adjudicate act 19's uncertified execution in either direction, or cite
anything from `claude/act-19-execution`; choose among act 20's three notions on any ground other
than the owner settlement this freeze records, or rate them against one another; consume or compare anything from the substratum Lemma 24.1 rounds; compare Source A with B
or C; edit any manuscript; close `P0` or either of its parts; or say anything about Track I.

### Deriving or recognising quantum evolution is EXPLICITLY OUT OF SCOPE

**"Show that these conditions single out Schrödinger evolution" is not asked, not bounded and not
attempted.** It is the natural stretch target of this round and it is unbounded here: it needs a
notion of quantum evolution on the orbit space that the record does not carry, a bridge from a
transition on `GramPhaseEquiv`-classes to an operator on a Hilbert space that acts 12 through 20 do
not build, and an evidence bar this freeze could not honestly fix. It is named here as a non-doing
**so that it cannot creep in mid-execution**: an execution that finds a rigid or narrow class and
begins asking whether the survivor looks like unitary evolution has left this round's scope, and what
it finds is **recorded as an observation and not executed**. A later round that wants the recognition
question must freeze it first.

**And the round refuses the weaker version too.** "The surviving class resembles", "is consistent
with", "is what one would expect from", or "is a step toward" quantum evolution are forbidden
sentences, for the same reason: this round has no standard against which resemblance could be
measured, and a round without a standard may not report a comparison.

### What act 21 does and does not change about `P0`

**`P0` stays OPEN and two-part in every case, and its label does not change.** What act 21 can change
is the **bounding** of its trajectory part, and only that: act 18 established that a cross-time law
plus one initial orbit can propagate, and act 21 asks how many such laws there are once structural
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
and `L4n` inline as `∀ t, ∃ Ψ αL αR, (lifting) ∧ (admissibility) ∧ TwistedNatural a₀ αL αR Ψ`,
consuming act 20's `TwistedNatural` unrestated. **`L4d` consumes no slot**, being the
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
variable pinned by an equation in the statement that needs it, as acts 10 through 20 did. Acts 7's,
10's, 11's, 12's, 13's, 17's, 18's and 20's definitions are **reused, not redefined**; in particular
`FibreGram`, `GramPhaseEquiv`, `RealizableGram`, `CoherentLift`, `FibreCrossGram`, `TwoSidedRelated`,
`GramTrajEquiv`, `SelectsAt`, `PointwiseLaw`, `DeterminesTraj`, `ProperAt`, `PropagatesFrom`,
`StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition`, `RelabelLift`,
`RelabelInducedLeft` and `RelabelInducedRight` are
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
## The chronology control — act 10's STRENGTHENED mechanism, through the manifest and never a constant

The execution's guard tag is **`R7-OLT`**, reserved here and created by the execution pull request.
The round's stem is **`OLT`**; its seal state is the prospective declaration during execution and
the record `verification/seals/OLT.json` from `P`, as the shape section states, and **no constant**.

1. **This preregistration blob is merged into `main` before any execution-specific act 21 object
   enters the repository tree** — any Lean definition or proof about a transition family, about a
   ladder condition, about the descent of a propagating law or about the rigidity of the class; any
   search artifact; any probe clause; any result artifact; any manifest record or declaration for
   `OLT`. **The single permitted exception is the analysis recorded inside this control-plane blob
   itself**, merged *as* the freeze, including the frozen evidence rule, the `L5` test carried from
   act 19, the table of what the merged record supplies, the analysis under `L4n`, and the
   pre-freeze reading recorded as the reason for `OL0`'s prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, `B`. The execution's first commit sets `_MANIFEST_PROSPECTIVE = {'OLT': B}` and
   `_MANIFEST_BASELINE = {'base': B, 'authorized': ('OLT',)}`, both outside the validator's
   marker-bounded regions, and nothing else about the round is read by the generic region.
3. **The execution guard pins this file's blob by content at this exact path, with a one-byte drift
   control** — the pinned blob compared, a one-byte mutation of the file refused — **fail-closed**.
4. **The ancestry question is asked of the real execution head through the validator's prospective
   path** — the round's clause is one keyed call, `_si2_authority('OLT', tag='R7-OLT')`, and its
   verdict is the validator's for the record or declaration keyed `OLT` and nothing else — with
   `pull_request.head.sha` from the Actions event payload as the target in pull-request continuous
   integration, `HEAD` otherwise, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` the declared base and `H` the real
   execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant
   of `B`**, fail-closed — act 10's strengthened form, which is what the validator's `EXECUTION`
   classification certifies.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for
   `B`, for `H`, and for every enumerated commit alike.
7. **Archive mode is the record.** At `L` the validator classifies `OLT` as `LANDED-PENDING-PIN`,
   which is permitted at `L` itself and fails every descendant as *seal pending*. `P` writes
   `verification/seals/OLT.json` with `base` = `B`, `sealed_head` = `E` and `merge` = `L`, and removes
   the `OLT` entry from the prospective declaration; from `P` on the validator classifies `OLT` as
   `ARCHIVED`, re-derives `L` from `E` over the union of the event's visibility targets, requires the
   derived landing to equal the pinned one and the pinned merge's second parent to equal `E`, and
   requires both to be reachable from the target — each **fail-closed**. `P` is a pin-only change
   recording the record and removing the declaration, and nothing else.
8. **Existing manifest records are read with the integrity rule and never written.** The declared
   baseline holds the twenty-five records at `B` against mutation, removal and any addition other
   than `OLT`, on every run, through the data-driven rule; and `R7-OLT` reads `RNT.json` and
   `SI3.json` through the manifest accessor as the preconditions below require. An archive seal
   belongs to the round that set it.
9. **This round's own state is never a permanently fixed execution-mode value, because there is no
   value to fix.** `R7-OLT` reads no `_OLT_BASE`, `_OLT_SEALED_HEAD` or `_OLT_MERGE`; nothing matching
   `_OLT_(BASE|SEALED_HEAD|MERGE)` exists at any commit of the round; and the validator's three
   classifications are what the round passes through, exactly as `SI-3`'s were exercised in vivo. The
   negative cases that a declared-and-recorded stem fails, that a descendant of an unpinned landing
   fails, and that a pin whose second parent is not `E` fails are the validator's own and are
   re-run on every head.
10. **The standing contract holds at every head.** `SI-3`'s zero-legacy-statement contract, its
    tokenizer census of genuine identifier reads and its region-boundary checks are not this round's
    to modify, and every head of the round passes them unchanged.
11. **The ordering obligation's records 2–4 are checked mechanically by `R7-OLT`**, from the result
    note's commit table and from git, each with a mutation control: (a) the ladder commit and the
    discrimination commit are on the first-parent chain from `B` to `E`, in that order; (b) at the
    ladder commit the module states every rung declaration record 1 names and contains **no**
    `theorem`, `lemma`, `example` or `instance`; (c) the discrimination commit is the first commit on
    that chain at which the module contains one; (d) between the discrimination commit and `E` the
    text of every declaration record 1 names is byte-identical, by extraction of each declaration
    from the module at both commits. A fabricated SHA off the chain, a theorem present at the ladder
    commit, and a rung whose text differs between the two commits each **fail** the control, and the
    three are exercised as negatives on synthetic text before the commit.
12. **Content contracts hold the result note to this freeze's distinctions**, each mutation-tested
    against the exact failure it exists to catch: the round's shape as sealing under the manifest
    with `E` → `L` → `P`; the five records present with their SHAs; the three attestation answers
    present as a table for the span `B` → ladder commit; the freeze-supplied-facts list present;
    the sentence that no condition was added and no equivalence was widened after the survivors were
    known, where `L-FAMILY` or `L-WIDE` is reached; the headline label carrying its condition set;
    `L4n` reported as act 20's `TwistedNatural` itself and as this freeze's one change; the act 19
    boundary sentence that nothing from `claude/act-19-execution` is cited; THE CLAUSE carried
    verbatim at every mention with its count; and the frozen `P0` sentence for the case reached
    present in `verification/ROADMAP.md` verbatim.

### The contracts this round supersedes, named in advance

**Under `§A.37`'s closed-round rule this section is the authorization.** Three closed rounds' guards
carry contracts that read the current head or the current manifest rather than the records and
commits those rounds manifested, and each fails on any act 21 head for a reason that has nothing to
do with act 21's result. **The failures were measured, not inferred**: at drafting time a throwaway
simulation of an act 21 execution head — one Lean file added, the two declarations set — and of its
landing and pin — `OLT.json` written, the declaration emptied — was run against the guard at `B`,
and exactly `R7-SI1`, `R7-SI2` and `R7-SI3` went red in both states, for exactly the conjuncts
below; with the four dispositions applied, both states ran green, with the validator classifying
`OLT` as `EXECUTION` at the simulated head and `ARCHIVED` at the simulated pin. Each entry names the
frozen contract, why an act 21 head fails it, and what stands in its place. **Nothing outside this
table is touched in `R7-SI1`, `R7-SI2` or `R7-SI3`**, and a failure outside it is a result requiring
adjudication.

| guard | contract | why an act 21 head fails it | disposition |
| --- | --- | --- | --- |
| `R7-SI1` | `N12`, `_si1_no_forbidden_paths`: the round wrote no manuscript, no book file and no Lean, read as `git diff <SI1 base> HEAD` | the diff to any act 21 head contains `OrbitLawRigidityTwisted.lean` | **read over the round's own execution**: `git diff <SI1 base> d75427aece402e1629d56d1ca96fbc8d3c8101e8`, `SI-1`'s execution head `E`, the second parent of its landing merge `66eea646fcbf242df89b168bcce3336ff1b77802` on `main`'s first-parent spine; the contract's meaning — what `SI-1` wrote — is unchanged |
| `R7-SI2` | the same contract, `_si2_diff`, read as `git diff <SI2 base> HEAD` | the same file | **read over the round's own execution**: `git diff <SI2 base> df2fab5770085d7e83543c50c00ffc6a3c2a37d0`, `SI-2`'s execution head `E`, the second parent of its landing merge `d89fff8abb20e2c63a33949b79947650bf47df6a` |
| `R7-SI3` | the same contract, `_si3_diff`, read as `git diff <SI3 base> HEAD` | the same file | **read over the round's own execution once recorded**: the second endpoint is `SI3.json`'s `sealed_head` through the manifest accessor where the `SI3` record exists, and `HEAD` only while `SI3` is itself declared — which it no longer is |
| `R7-SI3` | `SI3-1`'s pinned-mode conjunct: `len(recs) == 25 and sealed == 19 and base_only == 6`, `recs['SI3'].base == _MANIFEST_BASELINE['base']`, `_MANIFEST_PROSPECTIVE == {}` | `OLT.json` is a twenty-sixth record from `P`; the declared baseline is act 21's from the execution's first commit; the prospective declaration carries `OLT` until `P` | **read over the records `SI-3` manifested**: the counts over `_SI3_MANIFESTED`, the twenty-five stems `SI-3` manifested, which must all be present; `SI3`'s base compared to its own mandated base `b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5` as a literal; and only the `SI3` key of the prospective declaration tested, which is what the clause's own `declared`/`recorded` guard already reads. `SI-3`'s executing-mode branch is not touched |

What this table does **not** do: it does not edit any frozen document, does not change what `SI-1`,
`SI-2` or `SI-3` recorded as their outcomes, does not touch any negative case or tag map, and does
not reopen anything adjudicated. **The four dispositions are the same rule applied four times** —
`AGENTS.md` lines 972–978 — and they are the rule's first application to a Track B round, which is
recorded so that the next round does not have to rediscover it: a closed round's head-relative
contract is a contract about *that round's* commits, and the closed-round rule is how it is read.

### What must have merged before the execution begins, checkable mechanically

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md \| git hash-object --stdin` equals the blob the `R7-OLT` clause pins |
| 2 | Act 20's execution is merged **and sealed**, in the manifest | `git show B:verification/seals/RNT.json` is `{"round": "RNT", "kind": "sealed", "base": "84f27b50198ee31c224e31284905ff6c284ea9db", "sealed_head": "0f8b4e06a1cc31ab0c01f2edb5011f1efe545e1b", "merge": "6a6d62e97518600bf2de51cf1d39146d1adbdff9"}`, and the guard at `B` classifies `RNT` as `ARCHIVED` |
| 3 | `SI-3`'s execution is merged **and sealed**, and the manifest protocol is in force | `git show B:verification/seals/SI3.json` carries `kind: "sealed"`, `base` `b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5`, `sealed_head` `6677846a1f9c3c28e8d4095386879b662ee719be` and `merge` `2399b471ff5784b2aa2d08050129eaeca351286c`; `git show B:verification/lean/edge_rigidity_probe.py` carries `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE = {'base': 'b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5', 'authorized': ('SI2', 'SI3')}` |
| 4 | The seals tree at `B` is the pinned one and carries no `OLT` | `git rev-parse B:verification/seals` is `1abe1c988b1cb0a5fd119bbae8bd7108933334a4`; it holds twenty-five records, nineteen `sealed` and six `base-only`, and no `OLT.json` |
| 5 | The guard at `B` is green and carries no legacy constant | the guard file at `B` prints eighty-four `R7-*` tags, all `PASS`, on main-push run 35412319426; `_SI2_LEGACY_RE` finds zero assignment statements in it |
| 6 | The guard tag and its stem are still free | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-OLT` and no occurrence of `_OLT`; `git grep -- 'OLT' B` returns nothing |
| 7 | The modules this round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/RepresentativeNaturality.lean`, `…/IntermediateCrossTimeStructure.lean`, `…/GramTrajectorySelection.lean`, `…/CrossTimeInvariants.lean`, `…/TwoSidedGauge.lean` and `…/CoherentLiftGauge.lean` all succeed, and `OIBridge.lean` at `B` imports `OIBridge.RepresentativeNaturality` at line 209 |
| 8 | No act 21 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean` |
| 9 | Act 19 is closed and its formal state never reached `main` | `git ls-tree B --name-only verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/` lists exactly `closure.md` and `preregistration.md`, at blobs `3d37529cb89a4d2bb60281f14f15645e3beaeb4c` and `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`; no `OrbitLawRigidity.lean` exists in the tree; `git show B:verification/lean/edge_rigidity_probe.py` contains no `R7-OLR` and no `_OLR` |
| 10 | `B`'s provenance | `B` is `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`; its first parent is `b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5` and its second parent is `bae13c9eec30f63e4b0e6644811e6d124ee08a30`, `SI-3`'s `P`. Read as a provenance fact about `B` — that this freeze was written against the certified post-`SI-3` `main` — and not as a requirement that live `main` remain there |
| 11 | The passages the locating controls quote are at their coordinates | `AGENTS.md` at `B` is blob `d2c949f09f630f238e964308bbde9a9d8bec6279` and carries the quoted text at lines 697–700, 775–780, 879–889, 941–952, 954–962, 964–970 and 972–978; `verification/ROADMAP.md` at `B` is blob `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` |

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
- **The attestation set is answered for the span `B` → ladder commit**, all three questions, with the
  partial-fact rule applied and the freeze-supplied facts that were in front of the execution listed.
- **Then exactly one execution pull request**, based on that merge commit, carrying the Lean module,
  the result note, the `R7-OLT` guard clause, the prospective declaration and the declared baseline
  set as the chronology control states, the supersession table's four edits and nothing else in the
  three guards it names, the `ROADMAP` propagation and the census entry. **No manuscript changes.**
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no rebase,
  no amend, no force-push. A red badge caused solely by an archive clause that entered `main` after
  the base is not a research failure; the certification of record is the run whose `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. `P` writes `verification/seals/OLT.json` with its three fields, removes the `OLT` entry
  from the prospective declaration, and touches nothing else. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.
## Allowed final report

1. **The round's shape**, restated: sealing under the manifest protocol, `E` → `L` → `P`, with the
   prospective declaration and the declared baseline as set at execution, the record `P` writes named
   field by field, no existing manifest record altered, no legacy constant written, and the base-blob
   verification recorded;
2. **the ordering obligation's five records, in full** — the ladder table, the ladder commit SHA, the
   discrimination commit SHA, the immutability span with the command and its result, and the quotient
   record — **and the statement that no condition was added and no equivalence was widened after the
   survivors were known** — and the attestation set's three answers for the span from `B` to the
   ladder commit, as measurements, with the freeze-supplied facts that were in front of the execution
   listed;
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
14. the relation to acts 10, 11, 12, 13, 14, 15, 16, 17, 18 and 20 — every merged label consumed,
    none revised — with act 12's classification, act 17's `TJ1` and `TJ3`, act 18's `XS1` and `L-PROP`
    and act 20's `RNT1`–`RNT6` consumed at merged strength, and the act 19 boundary honoured as act
    20's result honoured it at its §14: act 19's freeze and closure read and not edited, nothing from
    its execution branch cited, and nothing it lists as uncertified reported as refuted;
15. the definition count against the eight-slot budget, with the conditional slot marked fired or
    unused;
16. the chronology certification, naming the property certified, the eleven preconditions checked at
    `B`, the validator's classification of `OLT` at `E` (`EXECUTION`), at `L` (`LANDED-PENDING-PIN`)
    and at `P` (`ARCHIVED`) as read from the continuous-integration logs of the exact heads, the
    supersession table's four edits reported as measurements with their negative controls, and
    `SI-3`'s standing zero-legacy-statement contract reported as holding at every head;
17. the axiom table with one line per named result;
18. the discrepancies, if any, recorded and not repaired;
19. **the provenance as honoured**: the statement that the rungs `L0`, `L1`, `L2`, `L3i`, `L3s`, `L4d`
    and `L5` were stated in the module in act 19's wording as this file carries it, that `L4n` was
    stated as act 20's `TwistedNatural` with the two lifting obligations and no added conjunct, and
    that the candidate list, the quotient list and the discriminating test are act 19's unchanged.
## Owner settlements before immutability

Recorded before this freeze merges and becomes immutable under `§A.37`. **Every item below is a call
already made**, written here so the record shows it was settled rather than left open; the body of
this freeze is written to them throughout. **This freeze carries no open decision.**

### Act 19's twelve settlements, inherited

These are act 19's items 1 through 12, carried in act 19's wording with the round's name changed
where the item names the round; each remains a call made.

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
5. **`L-RIGID` is modulo equivalences already recognized before act 21**, and the frozen quotient list
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
    untouched. Act 21 is orbit/trajectory-law rigidity only.
12. **Acts 12, 17 and 18 are consumed at merged strength**: not re-proved, not strengthened, not
    redefined. Act 12 supplies the slice equivalence and act 17 the trajectory lift, and the
    attribution is exact wherever either is named.

### Act 19's three open decisions, settled

Act 19 recorded three decisions as open at its freeze. The owner settled them, and this freeze is
written to the settlements:

13. **SEALING**, under the manifest protocol: the tag `R7-OLT`, the stem `OLT`, the landing
    `E` → `L` → `P` with `P` mandatory, the prospective declaration during execution and the record
    from `P`. The reason is the derivation in the shape section: the execution creates a new formal
    object whose chronology matters to the result.
14. **`L5` is retained**, in act 19's wording, with the `L5` test as act 19 recorded it, the product
    configuration, `ΦPP` and `ΦCTRL`, definition slot 5 conditional on nothing further, and the
    product-embedding cost named as construction work with `L5-UNDECIDED` an allowed outcome.
15. **The `L3` finiteness route is permitted with its required reporting**: where the execution
    proves `Ω_t` finite in the kernel at the named configuration it may derive one of `L3i`, `L3s`
    from the other, and it records that it did so and at which configuration; it may not assume
    finiteness.

### Act 21's own settlements

16. **The naturality rung is `N-TWIST`, exactly at act 20's certified strength.** `L4n` is act 20's
    `TwistedNatural` itself, together with the two lifting obligations act 20's `RNT2` fixed for a
    lift, stated across one time step; **no new candidate-specific constraint on the induced maps is
    added**, and the analysis under `L4n` about what unconstrained maps admit is recorded and acted
    on by nothing. Act 20's `CLASS-TWISTED-NOT-STRICT` and its two `SEP-STRICT` verdicts are the input
    the choice was made against; the choice is the owner's and is made here. **Act 20 is consumed at
    merged strength**, as item 12 consumes acts 12, 17 and 18: not re-proved, not strengthened, not
    redefined.
17. **The ladder's provenance is act 19's experiment re-frozen, not rebuilt.** `L0`, `L1`, `L2`,
    `L3i`, `L3s`, `L4d` and `L5` are carried at the same mathematical strength, `L4n` alone is
    replaced, and only the mechanical changes the provenance table enumerates are made — names,
    current merged references, the manifest lifecycle, the chronology controls. **Act 21 re-proves
    every fact it uses; act 19's execution remains research material only.**
18. **The attestation span ends at the ladder commit.** All three questions are kept, the
    partial-fact rule applies, and the span is from the mandated base through the ladder commit —
    act 20's finding about its own instrument, applied.
19. **The census and the candidates are act 19's, unchanged.** The seven transition families `ΦI`,
    `ΦP`, `ΦX`, `ΦC`, `ΦT`, `ΦPP` and `ΦCTRL`; the three-member quotient list; the per-rung
    restriction tests and their three labels with `L4d-HYP`; the `L-RIGID` / `L-FAMILY` / `L-WIDE`
    / `L-UNDECIDED` semantics; and `SIOP` with its first-divergence conjunct, all reused unchanged.
20. **The anti-expansion rule is frozen**: an eighth candidate, a collapsing equivalence, a further
    rung, a further configuration or a strengthening of a merged theorem discovered during execution
    is recorded as an observation for a later round and is not executed.
21. **Act 19's predictions are carried unchanged**, including the predicted `SIOP` witness, with
    `ΦP` now predicted to discharge `L4n` through act 20's merged lift and exact law; the closure's
    record about act 19's uncertified execution and the predicted witness is noted in the provenance
    section and is not evidence here.
22. **The four supersessions in `R7-SI1`, `R7-SI2` and `R7-SI3` are authorized as the table names
    them**, under the closed-round rule, measured in simulation at drafting time, and nothing else in
    those guards is touched.

**One check was performed at drafting time and its outcome is recorded here as a settlement rather
than as a correction in flight.** The two mandatory verbatim clauses of this file — the start-state
discrepancy clause and the anti-contamination invariant — were **extracted by reading bytes** from
act 19's preregistration blob `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`, as every carried range was, and
each reproduced here without retyping: the discrepancy clause is plain prose there and here, the
anti-contamination invariant is a block quote there and here, and each appears in this file exactly
once.

## Appendix — the substitution list, in full

Every difference between this file's carried ranges and act 19's blob is one of the following, each
applied the number of times stated and nowhere else. Insertions of whole paragraphs, items or rows
are listed by their anchor sentence.

| block (act 19 lines) | replaced | by | times |
| --- | --- | --- | --- |
| 289-366 | ## Source scoping, carried from acts 13 through 18 | ## Source scoping, carried from acts 13 through 20 | 1 |
| 289-366 | ### What act 19 inherits, and consumes without re-proving | ### What act 21 inherits, and consumes without re-proving | 1 |
| 289-366 |    Both are consumed and **neither is redefined**. ⏎  |    Both are consumed and **neither is redefined**. ⏎ 8. **Act 20's three notions, its lift and its classification, at merged strength.** … | 1 |
| 289-366 | \| whether a law's transition descends to orbit classes \| for `LC3`, **yes**, discharged at orbit level \| act 18's `LC3` descent \| ⏎  | \| whether a law's transition descends to orbit classes \| for `LC3`, **yes**, discharged at orbit level \| act 18's `LC3` descent \| ⏎ \… | 1 |
| 368-487 | ## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13, 17 and 18 | ## The objects, FROZEN — all consumed from acts 7, 10, 11, 12, 13, 17, 18 and 20 | 1 |
| 368-487 | `xs5_l_axis_prop`. ⏎  | `xs5_l_axis_prop`; and act 20's `StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition`, ⏎ `RelabelLift`, `RelabelInducedL… | 1 |
| 368-487 | exactly as acts 11 through 18 ⏎ carry it | exactly as acts 11 through 20 ⏎ carry it | 1 |
| 368-487 | before act 19 and each traceable | before act 21 and each traceable | 1 |
| 653-723 | verification/lean-mathlib/OIBridge/OrbitLawRigidity.lean | verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean | 1 |
| 725-991 | the second survivor**, and with `ΦI` the predicted `SIOP` witness. ⏎  | the second survivor**, and with `ΦI` the predicted `SIOP` witness. ⏎  ⏎ **Act 20 carried this statement into Lean and it is consumed at m… | 1 |
| 993-1055 |    laws on `FibreGram` — which is what `L4n` is stated against. ⏎  |    laws on `FibreGram` — the classes act 20's `TwistedNatural` is stated against, and so what `L4n` ⏎    consumes. ⏎ 6. **Act 20's lift a… | 1 |
| 993-1055 | \| `L4n` \| **named and expected hard**: a transition descending to classes with no gauge-natural representative-level lift. The freeze n… | \| `L4n` \| **named and expected hard**: a transition descending to classes with no twisted-natural representative-level lift satisfying … | 1 |
| 1057-1187 | is fixed here and is not moved during execution, exactly as act 18 recorded for its own. ⏎  | is fixed here and is not moved during execution, exactly as act 18 recorded for its own. ⏎  ⏎ **Four more members of the file set at `B` … | 1 |
| 1189-1224 | \| `L4n` \| not predicted \| **low** \| Both predicted survivors have obvious representative-level lifts — the identity, and the column p… | \| `L4n` \| not predicted \| **low** \| Both predicted survivors have twisted-natural lifts at act 20's strength — the identity, with `αL… | 1 |
| 1189-1224 | but which no merged result states. \| | but which no merged result states. `ΦP`'s `L4n` is predicted discharged by act 20's merged lift and exact law at the frozen configuration… | 1 |
| 1226-1455 | Act 19 asks how rigid the class of such laws is | Act 21 asks how rigid the class of such laws is | 1 |
| 1226-1455 | the answers of acts 11 through 18 stand exactly as those rounds | the answers of acts 11 through 20 stand exactly as those rounds | 1 |
| 1457-1572 | Acts 11 through 18 each carry the non-doing | Acts 11 through 20 each carry the non-doing | 1 |
| 1457-1572 | Act 19 classifies the cross-time laws a frozen ladder | Act 21 classifies the cross-time laws a frozen ladder | 2 |
| 1574-1671 | Act 19 classifies the cross-time laws a frozen ladder | Act 21 classifies the cross-time laws a frozen ladder | 1 |
| 1574-1671 | 28. **A landing without `P`.** This is a sealing round. The specific failure guarded against is ⏎     treating `L` as the end of it: in e… | 28. **A landing without `P`.** This is a sealing round. The specific failure guarded against is ⏎     treating `L` as the end of it: at `… | 1 |
| 1574-1671 | 30. **A chronology guard that fixes this round's own pins at `None` for all time.** See the chronology ⏎     control's clause 9, which ex… | 30. **A stem both declared and recorded, or a legacy constant written.** The specific failure guarded ⏎     against is a `P` that writes … | 1 |
| 1673-1727 | act 19 | act 21 | 3 |
| 1673-1727 | **re-prove or ⏎ strengthen acts 12, 17 or 18**; | **re-prove or ⏎ strengthen acts 12, 17, 18 or 20**; | 1 |
| 1673-1727 | `TJ0`–`TJ3`, `XS0`–`XS5` or any merged label | `TJ0`–`TJ3`, `XS0`–`XS5`, `RNT1`–`RNT6` or any merged label | 1 |
| 1673-1727 | that acts 12 through 18 do ⏎ not build | that acts 12 through 20 do ⏎ not build | 1 |
| 1673-1727 | alter any existing archive seal ⏎ constant; | alter any existing manifest record, or ⏎ write a legacy seal constant; adjudicate act 19's uncertified execution in either direction, or … | 1 |
| 1729-1785 | **`L2` and `L4n` consume no slot**: `L2` is stated inline as `∃ Φ̂, ∀ t, Φ t = Φ̂` inside `LadderConds`, ⏎ and `L4n` inline against act 1… | **`L2` and `L4n` consume no slot**: `L2` is stated inline as `∃ Φ̂, ∀ t, Φ t = Φ̂` inside `LadderConds`, ⏎ and `L4n` inline as `∀ t, ∃ Ψ … | 1 |
| 1729-1785 | as acts 10 through 18 did. Acts 7's, ⏎ 10's, 11's, 12's, 13's, 17's and 18's definitions | as acts 10 through 20 did. Acts 7's, ⏎ 10's, 11's, 12's, 13's, 17's, 18's and 20's definitions | 1 |
| 1729-1785 | `ProperAt` and `PropagatesFrom` are ⏎ consumed and none is restated. | `ProperAt`, `PropagatesFrom`, ⏎ `StrictNatural`, `TwistedNatural`, `OrbitNatural`, `RelabelTransition`, `RelabelLift`, ⏎ `RelabelInducedL… | 1 |
| 1877-1902 | - **The ladder commit comes second**, before any discriminating result, and its SHA is recorded. The ⏎   ordering obligation's five recor… | - **The ladder commit comes second**, before any discriminating result, and its SHA is recorded. The ⏎   ordering obligation's five recor… | 1 |
| 1877-1902 |   the result note, the `R7-OLR` guard clause with `_OLR_SEALED_HEAD` and `_OLR_MERGE` present and ⏎   unset, the `ROADMAP` propagation an… |   the result note, the `R7-OLT` guard clause, the prospective declaration and the declared baseline ⏎   set as the chronology control sta… | 1 |
| 1877-1902 | - **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P` ⏎   mandatory. | - **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P` ⏎   mandatory. `P` writes `verification/seal… | 1 |
| 1904-1949 | 1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled named ⏎    and no existing seal constant … | 1. **The round's shape**, restated: sealing under the manifest protocol, `E` → `L` → `P`, with the ⏎    prospective declaration and the d… | 1 |
| 1904-1949 |    record — **and the statement that no condition was added and no equivalence was widened after the ⏎    survivors were known**; |    record — **and the statement that no condition was added and no equivalence was widened after the ⏎    survivors were known** — and th… | 1 |
| 1904-1949 | 14. the relation to acts 10, 11, 12, 13, 14, 15, 16, 17 and 18 — every merged label consumed, none ⏎     revised — with act 12's classifi… | 14. the relation to acts 10, 11, 12, 13, 14, 15, 16, 17, 18 and 20 — every merged label consumed, ⏎     none revised — with act 12's clas… | 1 |
| 1904-1949 | 16. the chronology certification, naming the property certified, the nine preconditions checked at ⏎     `B`, the archive-mode pins as un… | 16. the chronology certification, naming the property certified, the eleven preconditions checked at ⏎     `B`, the validator's classific… | 1 |
| 1904-1949 | 18. the discrepancies, if any, recorded and not repaired. ⏎  | 18. the discrepancies, if any, recorded and not repaired; ⏎ 19. **the provenance as honoured**: the statement that the rungs `L0`, `L1`, … | 1 |
| 1958-1994 | **`L-RIGID` is modulo equivalences already recognized before act 19** | **`L-RIGID` is modulo equivalences already recognized before act 21** | 1 |
| 1958-1994 | 11. **Threading stays OUT**, act 16's cancellation cell stays untouched, and act 18's `D`-axis is ⏎     untouched. Act 19 is orbit/trajec… | 11. **Threading stays OUT**, act 16's cancellation cell stays untouched, and act 18's `D`-axis is ⏎     untouched. Act 21 is orbit/trajec… | 1 |

Appended blocks — the attestation set, the anti-expansion rule, the paragraph under `ΦP`, witness
supply 6, the `OL0` file-set paragraph, forbidden sentences 25–27, hazards 32–34 and report item 19
— are additions after the last line of their carried range and replace nothing. The `L4n` block
quote and its paragraph, the chronology control, the preconditions, and the sections listed as
*replaced* in the provenance table are this round's text.
