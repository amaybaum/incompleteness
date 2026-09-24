# Verifier round V3-3 — V3 specification resolution: the gaps K1–K4 and G5–G7: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The amended
specification, the conformance vectors, the propagated status sentence and the result note are
execution objects, created only after the certified merge of this file.

> **The specification is settled on its merits, and the shadow is then measured against it.** A
> settlement is never chosen because the shadow already implements it, and never rejected because
> the shadow does not.

Everything below is subordinate to that sentence. Where a settlement below agrees with the reading
`V3-2` gave the shadow, it is because the alternatives were weighed and that reading was the better
one; where it departs, the departure is recorded with the vectors that show it, and the shadow is
left unchanged.

## The commit vocabulary this freeze uses, fixed first

`V3-3` is run under `AGENTS.md` §A.37 as it stands at `D`: two pull requests, this control plane
and then one execution pull request that carries its landing. The single-pull-request arrangement
`V3-2` ran under by owner direction was an exception for that round and is not used here.

- `D` = `347113a234ef5eea6986b663ea0971687591b33b`, the drafting snapshot: the certified head of
  `main` after `V3-2`'s landing (push run 35960220324, all six jobs green), designated by the owner
  as this round's `D`. Every measurement in this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before
  the merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Rᵢ`, `Λ`, `LB` and `Q` keep the meanings
`verification/infrastructure/v3/architecture.md` gives them. They name objects of the synthetic V3
rounds the conformance vectors build, never an object of this round.

## What `V3-3` is, and what it is not

`V3-3` is a **specification round**. It settles, normatively and in the text of
`verification/infrastructure/v3/architecture.md`, the seven places `V3-2` found the specification
silent or ambiguous: `K1` to `K4`, which `V3-2`'s preregistration froze as provisional readings
binding only the shadow, and `G5` to `G7`, which `V3-2`'s result recorded. It adds conformance
vectors only where a vector is needed to separate a settlement from a reading it rejects, and it
corrects the one status sentence the settlements make stale.

It is not:

1. **An implementation round.** `tools/v3_verifier.py` is not written. Where a settlement departs
   from the shadow's reading, the vectors that show the departure are placed where the shadow's
   runs do not execute them (reading `R2`), and a later implementation round owns the change.
2. **A promotion.** No act of `V3-2`'s promotion boundary is performed. No V3 verdict gates
   anything, and the continuous-integration authority of every job is unchanged.
3. **A migration.** No historical round, `PRA` included, is translated, classified or touched, and
   no `V1` or `V2` state is created, changed or removed.
4. **A bootstrap round.** How the first V3-governed round is certified and published (`V3-2`'s
   promotion prerequisites, `V3-1`'s hazard `H1`) is not addressed.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-3`, `v3-3`, `round-v3-3`, `V33-`, `specification-resolution` and `conformance-pending` occur
nowhere in the tree at `D`. Neither `verification/infrastructure/v3/conformance-pending/` nor
`verification/receipts/` exists at `D`.

### `F2` — the objects the round reads and writes, at `D`

| path | blob at `D` |
|---|---|
| `verification/infrastructure/v3/architecture.md` | `6c80e584021f973c529625b1da89469e7b136dfe` |
| `tools/v3_verifier.py` | `2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974` |
| `verification/README.md` | `052dfa270479c12470173ee90f340c4f805dac37` |

`verification/infrastructure/v3/conformance/` holds 84 vectors at `D`, the set `V3-2` landed. The
shadow runs them as an exact set: every top-level `*.json` file of the directory, each named for
its `id`; it does not descend into subdirectories.

### `F3` — the candidate vectors, measured at `D` in scratch

Every vector the tables below freeze was built at `D` in scratch by a throwaway generator that
reuses `V3-2`'s recipe helpers, which regenerate `V3-2`'s 84 landed vectors byte-identically. No
expected verdict was taken from any implementation's output.

- **On the unchanged shadow** (blob `2c34d4d7`): the ten corpus additions ran as expected (exit 0);
  each of the eleven pending vectors ran **not** as expected (exit 1), each with the shadow verdict
  the pending table records.
- **On a settlement patch** — a scratch copy of the shadow changed only where the settlements depart
  from its readings, SHA-256
  `481cf746fa74ba94bb7238f016921f5a98a7d415416c679745f3eb4545ab0bd3`, never tracked: all ten corpus
  additions, all eleven pending vectors, and 83 of the 84 landed vectors ran as expected. The one
  exception is `g6-admit-record-class-by-broader-entry`, the landed vector that encodes the reading
  `G6` rejects.
- **Own rule.** With each pending vector's own rule taken out of the settlement patch, that vector
  alone ran not as expected: each pending vector is decided by its own settlement and by nothing
  else.
- **Rejected alternatives.** For each rejected alternative in the tables below, a scratch copy
  implementing it turned its distinguishing vector from as expected to not as expected: seventeen
  alternatives on the unchanged shadow, and `G6`'s literal-only alternative on the settlement
  patch.
- A superseded receipt whose `seal` field is not an object makes the unchanged shadow raise an
  uncaught exception rather than return a verdict; the settlement patch, which does not read
  superseded receipts, returns `HOLDS`. No vector carries this case, because an uncaught exception
  ends a corpus run.

### `F4` — what the pending vectors expose in the shadow's readings

Three of the shadow's readings admit rounds that the settlements reject, and two of those admit
states that defeat a stated guarantee of the specification:

- **A halted round publishes seal state.** Under `V3-2`'s `G6` reading a path is a record path when
  a `record` entry governs it. A halted sealing round whose execution writes its declared seal
  record path keeps that file through `W` and publishes it through the halted landing; a halted
  round with no execution commits can do the same through the commit that takes `W`'s place. The
  shadow returns `HOLDS` on both. `S4` forbids `seal` in every halted receipt, and `S12` states
  that a halted execution's effects do not survive in the published tree.
- **A broad `record` entry exempts arbitrary paths from `W`.** A block declaring
  `record AM verification/` passes the shadow's `G6` check. `S12`'s withdrawal invariant then does
  not cover any path under `verification/`, and the halted landing admits changes to them.
- **A superseded receipt authorizes its own commit.** Under `V3-2`'s `K4` reading, the paths a
  superseded receipt commit may change are read from that commit's own receipt, which nothing
  validates. A superseded receipt that names a path as a seal record lets its commit change that
  path; the shadow returns `HOLDS` both for an ordinary path and for the round's own
  preregistration, restored by the next reconciliation.

### `F5` — tooling at `D`

Python 3.11 and git 2.43 in the drafting environment; the workflow pins Python 3.11. The
repository's object format is `sha1`. `tools/control_plane_lint.py` and
`tools/control_plane_base_check.py` read this file's preconditions block; the base check evaluates
a block-bearing artifact only when it is added or changed relative to the evaluated commit's first
parent.

## The settlements, FROZEN

Each item states: the ambiguity; `V3-2`'s provisional reading; the alternatives considered; the
settlement, whose exact normative text is frozen in the next section; why it is chosen; the vectors
that separate it from each alternative; and whether the shadow at `D` conforms, as measured.

### One principle behind four of the settlements

`K3`, `K4`, `G5` and `G7` each ask whether a rule stated for one commit binds the other commits of
the same role. They are settled by one principle: **every commit the round appends satisfies the
rule of its role, whether or not it ends up certified or published; and the round's durable state is
its final receipt alone** (`S4`). A superseded reconciliation or receipt commit, and an execution
commit of a halted round, are objects the round owns and its receipt reaches; a verifier that
admitted them unchecked would certify objects the specification's own definitions exclude. The
content of a superseded receipt, by contrast, is not the round's state and is not read.

### `K1` — the round declaration

- **Ambiguity.** `S4` gives the receipt's `round` and `kind` the subject `F`, and the record
  directory is "one repository directory the control plane names", but no form of declaration at
  `F` is given.
- **`V3-2`'s reading.** One `v3-round` block in the preregistration at `F`, three lines `round`,
  `kind`, `record-directory`, each exactly once, in any order; the receipt must agree with it.
- **Alternatives.** (a) `V3-2`'s reading. (b) The declaration as extra lines of the
  `v3-governed-paths` block. (c) The round id and kind derived from paths — the record directory's
  name, the presence of seal entries. (d) No declaration: the receipt's `round` and `kind` taken as
  given.
- **Settlement.** (a), stated with two precisions: the record directory is the directory holding
  the preregistration that carries the block, and neither the round id nor the kind is derived from
  a path. Where the block lies is `K2`'s. Frozen text: edits `A2`, `A3`, `A13`, `A16`.
- **Why.** (b) gives the governed-path block a second grammar and either changes `S7`'s canonical
  bytes, and with them its worked examples, or excludes lines from them. (c) makes the id depend on
  a naming convention the repository's round directories do not follow (`round-v3-2-shadow-verifier`
  for `V3-2`), and makes the kind, a prospective ownership of seal state, an inference from other
  declarations. (d) contradicts `S4`'s subject `F`: a value re-derived from nothing is asserted, not
  re-derived.
- **Vectors.** (b): `k1-reject-declaration-inside-governed-block` (new). (c):
  `k1-admit-record-directory-name-free` (new). (d):
  `k1-reject-receipt-kind-disagrees-with-declaration` (new). The landed
  `k1-admit-round-block-any-order` and `k1-reject-round-block-incomplete` remain.
- **Shadow at `D`.** Conforms on every vector, except that it admits a `v3-round` block that lies in
  an amendment rather than in the preregistration, which `K2` settles. One further departure was
  found by reading only: the shadow derives the record directory from `delta(D, F)` with a pattern
  that misreads an amendment whose file name is `preregistration.md`. No vector carries it.

### `K2` — where the declarations lie

- **Ambiguity.** `S7` requires "exactly one fenced block" of "the control plane", which may be
  several files.
- **`V3-2`'s reading.** Exactly one `v3-governed-paths` block and one `v3-round` block across all
  control-plane files at `F`, wherever they lie.
- **Alternatives.** (a) `V3-2`'s reading. (b) Both blocks in the preregistration, none in any
  amendment. (c) Several blocks, the last in path order superseding the others. (d) Several
  blocks, their entries united.
- **Settlement.** (b). Frozen text: edits `A7`, `A13`.
- **Why.** Under (a) a block may leave the preregistration for an amendment, which gives the scope
  of a round no fixed place and contradicts `V3-2`'s own `K1` reading ("the preregistration at `F`
  carries" the `v3-round` block). (a) and (b) give the same power to change a declaration before
  `F`: under both, an amendment cannot add a second block, so a declaration is changed where it
  lies. (c) makes the set in force depend on file-name order and hides it across files. (d) makes a
  round's scope the union of text in several files, with conflict rules `S7` does not have. The
  settlement relies on `T1` admitting a revision of the preregistration before `F`, which its
  predicate does (gap `G9`).
- **Vectors.** (a): `k2-reject-governed-block-only-in-amendment` and
  `k2-reject-round-block-only-in-amendment` (pending). (c): the landed
  `k2-reject-amendment-repeats-governed-block`. (d): `k2-reject-amendment-adds-governed-entries`
  (new). The landed `k2-admit-blocks-only-in-preregistration` remains.
- **Shadow at `D`.** Does not conform: it admits either block when it lies only in an amendment.

### `K3` — the first parent of every reconciliation

- **Ambiguity.** `S9` requires `D` on `LB`'s first-parent chain and says nothing of the first
  parents of earlier reconciliations.
- **`V3-2`'s reading.** For every `Rᵢ`, `D` on the first-parent chain of `Rᵢ`'s first parent, and
  for `i > 1`, `Rᵢ₋₁`'s first parent on the first-parent chain of `Rᵢ`'s first parent.
- **Alternatives.** (a) `V3-2`'s reading. (b) Only the last reconciliation constrained. (c) `D` on
  each first parent's chain, in no order. (d) Every first parent on `LB`'s chain, in no order.
  (e) (a) with strictly advancing first parents.
- **Settlement.** (a), non-strict: two consecutive reconciliations may share a first parent.
  Frozen text: edits `A9`, `A15`.
- **Why.** `S9` defines each reconciliation's first parent as the tip of `main` when it is built,
  and `main`'s first-parent chain only extends. The commit-local content of that definition is
  exactly (a): the first parents lie, in order, on one first-parent chain beginning after `D`. It
  also keeps `S10`'s claim true that a publication attempted after `main` has moved past `LB` fails:
  with (a), and with `S3`, `G5` and `K4` keeping every other commit of the round linear, every
  commit `Q` reaches is a commit of the round or an ancestor of `LB`. Under (b), (c) or (d) a
  reconciliation built on a stale `main` is admitted; under (b) and (c) a later reconciliation built
  on an older `main` than an earlier one is admitted at the end, and a `Q` can then descend from a
  newer `main` than its `LB`, so that a non-force update succeeds and `main`'s first-parent chain
  loses its own earlier tip. (e) rejects a reconciliation built when `main` has not moved, which
  `S9`'s definition permits. The cost of (a) is recorded as hazard `H2`.
- **Vectors.** (b) and (c): the landed `k3-reject-first-parent-regressed`. (d):
  `k3-reject-intermediate-regression` (new). (e): `k3-admit-reconciliation-on-unmoved-base` (new).
  The landed `k3-admit-two-reconciliations` remains.
- **Shadow at `D`.** Conforms.

### `K4` — every receipt commit

- **Ambiguity.** The receipt commits between reconciliations, superseded after a failed
  publication, have no delta rule of their own.
- **`V3-2`'s reading.** Every receipt commit is a single-parent child of its reconciliation, and its
  delta is exactly the receipt path plus, for a sealing receipt, the seal records it names.
- **Alternatives.** (a) `V3-2`'s reading: the seal records a superseded receipt names itself.
  (b) No rule for superseded receipt commits. (c) A single parent only. (d) (a) with the superseded
  receipt also required to be a valid receipt. (e) The receipt path only. (f) `S10`'s rule for `Q`,
  with the seal records the round's final receipt names.
- **Settlement.** (f). The content of a superseded receipt is not read. Frozen text: edits `A10`,
  `A15`, `A16`.
- **Why.** (a) lets an unvalidated object define what its own commit may change (`F4`): the measured
  cases are an arbitrary path and the round's own preregistration. (f) takes the permitted paths
  from the final receipt, which is the round's durable state and is validated, and it reads no
  superseded content, so an unreadable superseded receipt neither fails the round nor stops the
  verifier. (b) and (c) let a superseded receipt commit carry any change into the next
  reconciliation. (d) makes the content of an unpublished receipt part of the round's validity,
  which `S4` gives to the final receipt alone. (e) forbids the seal records that every attempt of a
  sealing round must carry. Since `S9`'s condition 2 exempts only the receipt path, a later
  reconciliation of a sealing round restores each seal record to its state at `E` before the next
  receipt commit adds it again, as `k4-admit-sealing-superseded-receipt-commit` does.
- **Vectors.** (a): `k4-admit-superseded-receipt-unreadable`,
  `k4-reject-superseded-receipt-authorizes-own-extra-path` and
  `g7-reject-superseded-receipt-commit-changes-preregistration` (pending). (b) and (c): the landed
  `k4-reject-superseded-receipt-commit-changes-more`. (d):
  `k4-admit-superseded-receipt-not-a-valid-receipt` (new). (e):
  `k4-admit-sealing-superseded-receipt-commit` (new). The landed
  `k4-admit-superseded-receipt-commit` remains.
- **Shadow at `D`.** Does not conform: it reads each superseded receipt, fails when one is not JSON,
  takes the permitted seal records from it, and raises an uncaught exception when its `seal` field
  is not an object (`F3`).

### `G5` — the halted execution

- **Ambiguity.** `T5` requires `W` to be a single-parent child of "the last" execution commit;
  `S3`'s linearity is stated for `F..E` alone, and a halted round has no `E`.
- **`V3-2`'s reading.** Every execution commit, certified or not, is linear from `F` and changes no
  control-plane file.
- **Alternatives.** (a) `V3-2`'s reading. (b) No constraint on a halted execution's topology.
  (c) (a) with `delta(F, last)` also required to be authorized under `S7`.
- **Settlement.** (a), with the explicit statement that a halted execution's delta is not required
  to be authorized. Frozen text: edits `A12`, `A14`.
- **Why.** An executor does not know, when it commits, whether the round will halt; a rule that
  bound the execution only if it were later certified could be escaped by halting. A candidate that
  absorbed later `main` would carry measurements of a tree the round did not make. Without
  linearity, "the last" execution commit is not defined. (c) would make unpublishable exactly the
  rounds that halt because their execution went outside its governed paths — the outcome every
  preregistered `SCOPE-EXCEEDED` target provides for; what of a halted execution reaches the
  published tree is fixed by the withdrawal invariant and the halted landing, not by `S7`.
- **Vectors.** (b): the landed `g5-reject-halted-execution-not-linear`. (c):
  `g5-admit-halted-execution-with-unauthorized-change` (new). The landed
  `mc6-pass-halted-with-withdrawal` remains.
- **Shadow at `D`.** Conforms.

### `G6` — the record class

- **Ambiguity.** `S7`: the `record` class "must contain" the record directory and the receipt path,
  while the same bullet defines record paths as the round's own record and execution paths as
  "everything else the round may change".
- **`V3-2`'s reading.** "Contain" means governed, by the longest-match rule, by a `record` entry.
- **Alternatives.** (a) `V3-2`'s reading. (b) Literal `record` entries for the record directory and
  the receipt path, other entries unconstrained. (c) The `record` class exactly the round's own
  record, and record paths as `S7` defines them rather than as the declared class labels them.
- **Settlement.** (c): at `F`, literal `record` entries for the record directory `R` and the receipt
  path `P`, no `execution` entry within `R`, and no other `record` entry outside `R` except, in a
  sealing round, a single file declaring a seal record path; and a record path is a path within
  `R`, `P`, or a seal record the round's final receipt names. `S12`'s record commit and halted
  landing admit record paths in that sense only. Frozen text: edits `A6`, `A7`, `A8`, `A11`, `A13`,
  `A14`, `A15`.
- **Why.** `S7`'s own definition is exclusive: a `record` entry covering paths that are not the
  round's own record contradicts it. The class exists so that `W` can undo the execution without
  erasing the record (`V3-1`'s reading `R4`); under (a) and (b) a declaration can move any path out
  of `W`'s reach and into the halted landing, and a halted sealing round can publish seal state
  (`F4`). An `execution` entry within `R` makes every halted outcome invalid, since `W` would have
  to remove the result note that `S12` requires it to keep. Seal record entries are admitted at `F`
  because a sealing round cannot know then whether it will halt; the definition of record paths,
  which counts only the seal records the final receipt names, keeps a halted round from publishing
  them. The location of seal records is left open (gap `G12`).
- **Vectors.** (a): `g6-reject-record-class-by-broader-entry`,
  `g6-reject-record-entry-outside-own-record`, `g6-reject-execution-entry-within-record-directory`,
  `g6-reject-record-file-entry-in-non-sealing-round`,
  `g6-reject-halted-landing-publishes-unnamed-seal-record` and
  `g6-reject-halted-record-commit-writes-unnamed-seal-record` (pending). (b):
  `g6-reject-record-entry-outside-own-record` and
  `g6-reject-execution-entry-within-record-directory`. The landed
  `g6-reject-receipt-shadowed-by-execution-entry` remains; the landed
  `g6-admit-record-class-by-broader-entry`, which asserts reading (a), is removed from the corpus,
  and `g6-reject-record-class-by-broader-entry` carries the same block with the settled verdict.
- **Shadow at `D`.** Does not conform: it checks coverage by longest match only, and classes paths
  in the halted landing and the record commit by the declared class.

### `G7` — no commit after `F` changes the control plane

- **Ambiguity.** `S2` forbids a change to a control-plane file after `F`, while `S9` admits in a
  reconciliation any governed path listed in `landing.resolved_paths`, a control-plane file under a
  `record` entry included.
- **`V3-2`'s reading.** `S2` binds every commit of the round after `F`, reconciliations and receipt
  commits included.
- **Alternatives.** (a) `V3-2`'s reading, with "change" meaning that the control-plane files and
  their states differ from those at `F`. (b) Only the files present at `F` frozen: a control-plane
  file may be added after `F`. (c) `S9` prevails: a listed control-plane file may change in a
  reconciliation.
- **Settlement.** (a): at every commit of the round after `F`, the control-plane files are exactly
  those at `F`, each with its state at `F`. Frozen text: edits `A5`, `A14`, `A15`, `A16`.
- **Why.** A freeze that can be amended after it is frozen is not a freeze, and the receipt's
  `control_plane_blobs` records the state at `F`; a published record directory carrying a different
  preregistration or an added amendment would contradict the receipt that publishes it. `main` has
  no legitimate reason to touch a record directory that did not exist at `D`, so (c) buys nothing
  but the ability to rewrite the freeze.
- **Vectors.** (b): `g7-reject-reconciliation-adds-amendment` (new). (c): the landed
  `g7-reject-reconciliation-changes-preregistration`. Through `K4`'s mechanism:
  `g7-reject-superseded-receipt-commit-changes-preregistration` (pending).
- **Shadow at `D`.** Conforms at execution commits, `W`, the commit in its place, every
  reconciliation and the final `Q`. It does not check a superseded receipt commit's control-plane
  files, which `K4`'s reading then lets change: the pending vector above.

### Summary

| item | settlement | same as `V3-2`'s reading | shadow at `D` conforms | new corpus vectors | pending vectors |
|---|---|---|---|---|---|
| `K1` | (a), with precisions | yes | yes, but for `K2`'s location | 3 | — |
| `K2` | (b) | no | no | 1 | 2 |
| `K3` | (a), non-strict | yes | yes | 2 | — |
| `K4` | (f) | no | no | 2 | 2 |
| `G5` | (a), authorization not required | yes | yes | 1 | — |
| `G6` | (c) | no | no | — | 6 |
| `G7` | (a) | yes | yes, but through `K4` | 1 | 1 |

The departures make a later implementation round necessary: eleven pending vectors fail on the
shadow at `D`, and the settlement patch shows they can be met without breaking any other vector.

## The normative text, FROZEN

The execution changes `verification/infrastructure/v3/architecture.md` by the sixteen edits below,
applied in order to its blob at `B`, which the preconditions require to be its blob at `D`. For a
**replace**, the first block occurs exactly once in the file and is replaced by the second. For an
**insert**, the first block occurs exactly once and the second is inserted after it, separated from
it by one blank line. Every block ends with a newline. The file at `E` is byte-identical to the
result, and nothing else in it changes.

#### `A1` — replace, the provenance sentence

The located block:

```text
This document specifies protocol 3 of the repository's round verification. Protocol 1 is the guard
(`V1`) and protocol 2 the round certificate (`V2`). This specification was produced by round `V3-1`
under the frozen preregistration
`verification/infrastructure/round-v3-1-architecture/preregistration.md`, whose settlements `S1` to
`S13` it states as normative text. It is not operative: until a later round activates it, every
round is governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by it.
```

Its replacement:

```text
This document specifies protocol 3 of the repository's round verification. Protocol 1 is the guard
(`V1`) and protocol 2 the round certificate (`V2`). This specification was produced by round `V3-1`
under the frozen preregistration
`verification/infrastructure/round-v3-1-architecture/preregistration.md`, whose settlements `S1` to
`S13` it states as normative text. Round `V3-3`, under the frozen preregistration
`verification/infrastructure/round-v3-3-specification-resolution/preregistration.md`, settled the
seven gaps round `V3-2` recorded, `K1` to `K4` and `G5` to `G7`, and each settlement is normative
text under its identifier. The specification is not operative: until a later round activates it,
every round is governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by
it.
```

#### `A2` — replace, the record directory (`K1`)

The located block:

```text
**The round's record directory** is one repository directory the control plane names. It holds the
round's **control-plane files**, `preregistration.md` and the files under `amendments/`, and its
result note `result.md`. **The receipt path** is `verification/receipts/<round id>.json`, where the
round id matches `[A-Z0-9]+(-[A-Z0-9]+)*`.
```

Its replacement:

```text
**The round's record directory** is one repository directory the round declaration names (`K1`).
It holds the round's **control-plane files**, `preregistration.md` and the files under
`amendments/`, and its result note `result.md`. **The receipt path** is
`verification/receipts/<round id>.json`, where the round id matches `[A-Z0-9]+(-[A-Z0-9]+)*`.
```

#### `A3` — insert, `K1`

The anchor:

```text
**A path's state at a commit** is either the pair (mode, object id) of the path's entry in that
commit's tree, or its absence from that tree.
```

The inserted block:

```text
### `K1` — the round declaration

The preregistration declares the round in one fenced block with info string `v3-round`; `K2` fixes
where the block lies. Each line of the block that is not blank and does not start with `#` is
`<key> <value>`, the two separated by one space. `<key>` is `round`, `kind` or `record-directory`,
and each of the three appears exactly once, in any order:

- `round` is the round id, matching `[A-Z0-9]+(-[A-Z0-9]+)*`;
- `kind` is `sealing` or `non-sealing`;
- `record-directory` is a path `S7` accepts, ending in `/`: the directory that holds the
  preregistration carrying the block.

A block that breaks any of these rules is invalid, and so is a control plane without one. The
receipt's `round` and `kind`, whose subject is `F`, are re-derived from the declaration at `F` and
must equal it. The declaration names the round's record directory, whose control-plane files are
the only paths `delta(D, F)` may touch (`S2`), and it fixes the receipt path,
`verification/receipts/<round>.json`. Neither the round id nor the kind is derived from a path.
```

#### `A4` — replace, the traceability table

The located block:

```text
| `S13` | no migration | `S13` |
```

Its replacement:

```text
| `S13` | no migration | `S13` |
| `K1` | the round declaration | `K1`, under the objects; lifecycle transitions T1 and T7 |
| `K2` | the declarations lie in the preregistration | `K2`, under `S7`; lifecycle transition T1 |
| `K3` | the first parent of every reconciliation | `K3`, under `S9`; lifecycle transition T6 |
| `K4` | every receipt commit | `K4`, under `S10`; lifecycle transitions T6 and T7 |
| `G5` | the halted execution is linear | `G5`, under `S12`; lifecycle transition T5 |
| `G6` | the record class is the round's own record | `G6`, under `S7`; lifecycle transitions T1, T5 and T6 |
| `G7` | no commit after `F` changes the control plane | `G7`, under `S2`; lifecycle transitions T3, T5, T6 and T7 |
```

#### `A5` — insert, `G7`

The anchor:

```text
`F`, and not a merge commit on `main`, is the execution's ancestry anchor. `delta(D, F)` touches only
control-plane files of the round's record directory.
```

The inserted block:

```text
### `G7` — no commit after `F` changes the control plane

The rule that no commit after `F` changes a control-plane file binds every commit of the round after
`F`: each execution commit, `W` or the commit that takes its place (`S12`), each reconciliation, and
each receipt commit, superseded or final. At each of them the round's control-plane files are
exactly those at `F`, each with its state at `F`: none is changed, removed or added. A control-plane
file listed in `landing.resolved_paths` is no exception.
```

#### `A6` — replace, the record class in `S7` (`G6`)

The located block:

```text
- `<class>` is `execution` or `record`. **Record paths** carry the round's own record: its record
  directory, its receipt path and, for a sealing round, the seal records its receipt names.
  **Execution paths** are everything else the round may change. The `record` class **must** contain
  the round's record directory and its receipt path.
```

Its replacement:

```text
- `<class>` is `execution` or `record`. **Record paths** carry the round's own record: its record
  directory, its receipt path and, for a sealing round, the seal records its receipt names.
  **Execution paths** are everything else the round may change. The `record` class is exactly the
  round's own record (`G6`).
```

#### `A7` — insert, `K2` and `G6`

The anchor:

```text
The set in force is the set at `F`, re-derived from `F` by the verifier; no later policy redefines
it.
```

The inserted block:

```text
### `K2` — the declarations lie in the preregistration

The preregistration carries exactly one `v3-governed-paths` block and exactly one `v3-round` block
(`K1`), and these are the declarations in force at `F`. No amendment carries a fenced block with
either info string. A fenced block with either info string that is not closed, in any control-plane
file, makes the control plane invalid.

### `G6` — the record class is the round's own record

With `R` the record directory and `P` the receipt path that the round declaration fixes (`K1`), the
block at `F` is valid for the round only if:

1. it has a `record` entry whose `<path>` is `R` and a `record` entry whose `<path>` is `P`;
2. no `execution` entry's `<path>` lies within `R`, that is, equals `R` or begins with it;
3. every other `record` entry's `<path>` lies within `R` or, in a sealing round only, is a single
   file outside `R`, not a directory prefix, declaring a seal record path.

These conditions are checked against the round, at `F`. A **record path** of the round is a path
that lies within `R`, the path `P`, or a seal record that the round's final receipt names; a path is
not a record path merely because a `record` entry governs it. A halted receipt names no seal record
(`S4`), so the record paths of a halted round are `P` and the paths within `R`. `S12`'s record
commit and halted landing admit record paths in this sense and no others.
```

#### `A8` — replace, the record-class rule among the worked examples (`G6`)

The located block:

```text
A valid block whose `record` class omits the round's record directory or its receipt path is also
invalid; that rule is checked against the round, at `F`.
```

Its replacement:

```text
A valid block that breaks one of `G6`'s three conditions for its round is also invalid; those
conditions are checked against the round, at `F`.
```

#### `A9` — insert, `K3`

The anchor:

```text
For a halted round `S12` replaces conditions 2 and 3. No branch name and no live ref enters these
conditions.
```

The inserted block:

```text
### `K3` — the first parent of every reconciliation

The requirement that `D` lie on `LB`'s first-parent chain binds every reconciliation, not only the
last. `D` lies on the first-parent chain of `R₁`'s first parent, and for each `i > 1` the first
parent of `Rᵢ₋₁` lies on the first-parent chain of `Rᵢ`'s first parent. The first parents of the
reconciliations therefore lie, in order, on one first-parent chain, which is `LB`'s. Two consecutive
reconciliations may have the same first parent, when `main` has not moved between them. A round in
which one reconciliation's first parent lies behind an earlier one's is invalid, even when a later
reconciliation's first parent lies ahead of both.
```

#### `A10` — insert, `K4`

The anchor:

```text
A `main` that reaches the round's commits through any commit other than `Q` itself — a merge
created on the host, a squash or a rebase — is not a publication of the round.
```

The inserted block:

```text
### `K4` — every receipt commit

`S10`'s rule for `Q` binds every receipt commit of the round, superseded or final. Each receipt
commit `Qᵢ` is a single-parent child of the reconciliation `Rᵢ` before it, and `delta(Rᵢ, Qᵢ)` is
exactly the receipt path plus the seal records that the round's final receipt names. The content of
a superseded receipt is not read: the final receipt is the round's durable state (`S4`), and it
alone fixes which seal records any receipt commit carries.
```

#### `A11` — replace, record paths in `S12` (`G6`)

The located block:

```text
complete round. When no execution commits exist, the round appends to `F` a single-parent commit
that changes only `record` paths and carries the result note, and that commit takes the place of
`W`.
The halted landing is authorized when every path of `delta(LB, Λ)` is a `record` path and its change
is authorized.
```

Its replacement:

```text
complete round. When no execution commits exist, the round appends to `F` a single-parent commit
that changes only record paths (`G6`) and carries the result note, and that commit takes the place
of `W`.
The halted landing is authorized when every path of `delta(LB, Λ)` is a record path (`G6`) and its
change is authorized.
```

#### `A12` — insert, `G5`

The anchor:

```text
- **The receipt names them only as `candidates`**, never as `E`.
```

The inserted block:

```text
### `G5` — the halted execution

The execution commits of a halted round are the commits of `rev-list W ^F` other than `W`. `S3`'s
form binds each of them as it binds the commits of `F..E`: each has exactly one parent, which is `F`
or another of them, so that none absorbs later `main`; and, by `G7`, none changes a control-plane
file. Their delta from `F` is not required to be authorized under `S7`: a halt may follow a change
outside the governed paths, and what of the halted execution reaches the published tree is decided
by the withdrawal invariant and the halted landing.
```

#### `A13` — replace, lifecycle transition T1

The located block:

```text
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files; the governed-path block at `F` is valid (`S7`) | `D`, `F`, the commits between them, their trees |
```

Its replacement:

```text
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files; the round declaration and the governed-path block at `F` are valid and lie in the preregistration (`K1`, `S7`, `K2`); the record class is the round's own record (`G6`) | `D`, `F`, the commits between them, their trees |
```

#### `A14` — replace, lifecycle transition T5

The located block:

```text
| T5: → `HALTED` | when execution commits exist: `W` is a single-parent child of the last, listed in `candidates`, and satisfies the withdrawal invariant; the result note is present at `W` (`S12`) | `F`, `W`, the commits between them, their trees, the block at `F` |
```

Its replacement:

```text
| T5: → `HALTED` | when execution commits exist: they are linear from `F` (`G5`); `W` is a single-parent child of the last, listed in `candidates`, and satisfies the withdrawal invariant; the result note is present at `W` (`S12`); when none exist, the commit that takes `W`'s place changes only record paths (`G6`); no control-plane file changes after `F` (`G7`) | `F`, `W` or the commit in its place, the commits between them, their trees, the block at `F` |
```

#### `A15` — replace, lifecycle transition T6

The located block:

```text
| T6: → `RECONCILED` | `S9`: each reconciliation's parents as specified; `D` on `LB`'s first-parent chain; the landing authorized (`S9` or `S12`) | `D`, `E` or `W`, each reconciliation and receipt commit, `LB`, `Λ`, their trees, the block at `F` |
```

Its replacement:

```text
| T6: → `RECONCILED` | `S9`: each reconciliation's parents as specified, and its first parent as `K3` requires; each superseded receipt commit as `K4` requires; no control-plane file changes at any of them (`G7`); the landing authorized (`S9`, or `S12` with `G6`'s record paths) | `D`, `E` or `W`, each reconciliation and receipt commit, `LB`, `Λ`, their trees, the block at `F`, the seal records the final receipt names |
```

#### `A16` — replace, lifecycle transition T7

The located block:

```text
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal records; the receipt at `Q` valid under `S4` and consistent with every subject it records | `Q`, `Λ`, the receipt at `Q`, every commit it names |
```

Its replacement:

```text
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal records (`K4`); no control-plane file changed at `Q` (`G7`); the receipt at `Q` valid under `S4` and consistent with every subject it records, its `round` and `kind` those of the declaration at `F` (`K1`) | `Q`, `Λ`, the receipt at `Q`, every commit it names |
```

## The status correction, FROZEN as text

`verification/README.md`'s paragraph on the V3 shadow verifier says that the shadow implements the
specification with the provisional readings; after this round the specification settles them, in
places differently. At `E`, the paragraph below, which occurs exactly once in the file at `B`, is
replaced by the second, and nothing else in the file changes.

The paragraph at `B`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the protocol-3 specification
(`infrastructure/v3/architecture.md`) with the provisional readings `V3-2`'s preregistration froze,
and it gates nothing: it has no authoritative mode, no verdict it prints changes an exit status,
the release gate does not invoke it, and its workflow job, `V3 shadow verifier`, is not a required
check. `V1` and `V2` remain authoritative. Its conformance corpus is
`infrastructure/v3/conformance/`, executed as an exact set; its comparison with `V2` over the
attestation rows is `V3-2`'s `census.json`.
```

The paragraph at `E`:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the protocol-3 specification
(`infrastructure/v3/architecture.md`) as `V3-2` read it, with the provisional readings `V3-2`'s
preregistration froze. Round `V3-3` (`infrastructure/round-v3-3-specification-resolution/`)
settled those readings, and the three further gaps `V3-2` found, in the specification; the vectors
on which the settled specification and the shadow differ are in
`infrastructure/v3/conformance-pending/`, which the shadow does not run. The shadow gates nothing:
it has no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2` remain
authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an exact
set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

## The conformance vectors, FROZEN

Every vector has the format `V3-2`'s corpus uses (`id`, `settlements`, `kind`, recipe, expected
verdict and family), is built only from that format's existing recipe vocabulary, and is named for
its `id`. The recipes below use `V3-2`'s synthetic rounds: `D` holding `README.md`,
`tools/ex/keep.txt` and `verification/README.md`; a preregistration at `F` with the standard
declaration and the governed paths `record AM` of the record directory and of the receipt path,
`execution AMD tools/ex/` and `execution M verification/README.md` (plus `record A` of the seal
record for a sealing round); two execution commits; `R1` with first parent `D`; `Q` carrying the
receipt. Only the differences are stated.

### Added to `verification/infrastructure/v3/conformance/`

| id | settlements | recipe | expected | excludes |
|---|---|---|---|---|
| `k1-reject-declaration-inside-governed-block` | `K1`, `S7` | the preregistration has no `v3-round` block; its `v3-governed-paths` block begins with the three declaration lines; the receipt's digest is that of the governed entries alone | FAILS `t1:` | `K1` (b) |
| `k1-admit-record-directory-name-free` | `K1` | round `EX-1` whose record directory is `verification/infrastructure/round-alpha/`, declared so and governed so | HOLDS | `K1` (c) |
| `k1-reject-receipt-kind-disagrees-with-declaration` | `K1`, `S4` | round `EX-2` declared sealing, with its seal record entry; a complete receipt of kind `non-sealing` without `seal` | FAILS `s4:` | `K1` (d) |
| `k2-reject-amendment-adds-governed-entries` | `K2` | the standard preregistration; an amendment before `F` carrying a second `v3-governed-paths` block with the one entry `execution M README.md`; the receipt's digest is that of the union | FAILS `t1:` | `K2` (d) |
| `k3-reject-intermediate-regression` | `K3`, `S9` | three reconciliations with first parents `M2` (a child of `D`), `D` and `M3` (a child of `M2`), each followed by a well-formed receipt commit | FAILS `s9:` | `K3` (d) |
| `k3-admit-reconciliation-on-unmoved-base` | `K3`, `S9` | two reconciliations, both with first parent `D` | HOLDS | `K3` (e) |
| `k4-admit-sealing-superseded-receipt-commit` | `K4`, `S10`, `S11` | sealing `EX-2`; `Q` adds the receipt and the seal record; `R2` (first parent `M2`) restores the seal record to its state at `E`; `Q2` adds it again | HOLDS | `K4` (e) |
| `k4-admit-superseded-receipt-not-a-valid-receipt` | `K4` | two reconciliations; the superseded receipt path carries a JSON object that is not a valid receipt | HOLDS | `K4` (d) |
| `g5-admit-halted-execution-with-unauthorized-change` | `G5`, `S12` | halted `EX-3`; the execution commit adds `tools/ex/a.txt` and the ungoverned `other/unauthorized.txt`; `W` removes both and adds the result note | HOLDS | `G5` (c) |
| `g7-reject-reconciliation-adds-amendment` | `G7`, `S2`, `S9` | `R1` adds `amendments/amendment-late.md` to the record directory and lists it in `resolved_paths` | FAILS `s9:` | `G7` (b) |

### Removed from `verification/infrastructure/v3/conformance/`

`g6-admit-record-class-by-broader-entry`, which asserts `HOLDS` for `record AM verification/` with
`execution AMD tools/ex/`: `G6` rejects it. Its identifier is retired, and the same block with the
settled verdict is the pending `g6-reject-record-class-by-broader-entry`.

### Added to `verification/infrastructure/v3/conformance-pending/`

The shadow does not run this directory. Each vector below states the settled verdict; the last
column is the unchanged shadow's verdict, measured at `D`.

| id | settlements | recipe | expected | shadow at `D` |
|---|---|---|---|---|
| `k2-reject-governed-block-only-in-amendment` | `K2` | the preregistration carries only the `v3-round` block; an amendment before `F` carries the `v3-governed-paths` block | FAILS `t1:` | HOLDS |
| `k2-reject-round-block-only-in-amendment` | `K2`, `K1` | the preregistration carries only the `v3-governed-paths` block; an amendment before `F` carries the `v3-round` block | FAILS `t1:` | HOLDS |
| `k4-admit-superseded-receipt-unreadable` | `K4` | two reconciliations; the superseded receipt path carries text that is not JSON | HOLDS | FAILS `s10:` |
| `k4-reject-superseded-receipt-authorizes-own-extra-path` | `K4`, `S10` | non-sealing, two reconciliations; the superseded receipt names `tools/ex/smuggled.txt` as a seal record and its commit adds that file; `R2` removes it | FAILS `s10:` | HOLDS |
| `g6-reject-record-class-by-broader-entry` | `S7`, `G6` | the block `record AM verification/`, `execution AMD tools/ex/`, for round `EX-1` | FAILS `s7:` | HOLDS |
| `g6-reject-record-entry-outside-own-record` | `S7`, `G6` | the standard block for `EX-1` plus `record AM verification/seals/` | FAILS `s7:` | HOLDS |
| `g6-reject-execution-entry-within-record-directory` | `S7`, `G6` | the standard block for `EX-1` plus `execution AM` of the record directory's `notes/` | FAILS `s7:` | HOLDS |
| `g6-reject-record-file-entry-in-non-sealing-round` | `S7`, `G6`, `K1` | a complete non-sealing round whose block adds `record A verification/seals/EX1.json` | FAILS `t1:` | HOLDS |
| `g6-reject-halted-landing-publishes-unnamed-seal-record` | `S12`, `S11`, `G6` | halted sealing `EX-3`; the execution commit adds its declared seal record path, which `W` keeps and `R1` publishes | FAILS `s12:` | HOLDS |
| `g6-reject-halted-record-commit-writes-unnamed-seal-record` | `S12`, `S11`, `G6` | halted sealing `EX-4` without execution commits; the commit in `W`'s place adds the result note and its declared seal record path; `R1` removes the seal record | FAILS `s12:` | HOLDS |
| `g7-reject-superseded-receipt-commit-changes-preregistration` | `G7`, `K4`, `S2` | non-sealing, two reconciliations; the superseded receipt names the preregistration as a seal record and its commit changes the preregistration; `R2` restores it | FAILS `s10:` | HOLDS |

The drafting-time digests, SHA-256 of each directory's added files concatenated in path order, are
`187c8301b1fb32b19089d14a8ad3c96462d841bf619fe24081a2d752a635d15b` for the ten corpus additions and
`605f9328fa4751fb766362a743e043883249784c4899fe088038f01baa5d96bc` for the eleven pending vectors.
They are predictions (below), not pins: a vector that differs from its drafting-time bytes while
matching its frozen row is recorded as a discrepancy.

## The controls, FROZEN

Each control runs at the execution's stage-2 checkpoint and again at `E`.

- **`C1` — the corpus on the unchanged shadow.** `tools/v3_verifier.py --corpus` at `E` runs the 93
  vectors of `conformance/` as an exact set, every one as expected, exit 0.
- **`C2` — the pending set on the unchanged shadow.** `tools/v3_verifier.py --corpus` on
  `conformance-pending/` runs its eleven vectors, and every one of them runs **not** as expected,
  with the shadow verdict the pending table records.
- **`C3` — satisfiability.** A scratch copy of the shadow, changed only where the settlements depart
  from its readings and never tracked, runs `conformance/` and `conformance-pending/` at `E`, every
  vector as expected. Its SHA-256 is recorded; its code enters no tracked file.
- **`C4` — own rule.** For each pending vector, the settlement patch with that vector's own rule
  taken out runs that vector not as expected, and every pending vector not decided by the same rule
  as expected.
- **`C5` — rejected alternatives.** For each rejected alternative the settlement tables name with a
  distinguishing vector, other than `V3-2`'s own readings, which the unchanged shadow implements and
  `C2` exercises, a scratch copy implementing the alternative — of the unchanged shadow, or of the
  settlement patch for `G6` (b) — runs that vector not as expected, while the copy it was made from
  runs it as expected. There are eighteen.
- **`C6` — the normative text.** Applying the frozen edits to `architecture.md`'s blob at `B`
  yields its blob at `E` exactly.
- **`C7` — the status correction.** Substituting the frozen paragraph in `verification/README.md`'s
  blob at `B` yields its blob at `E` exactly.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its
target stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V33-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V33-1` | `SPECIFICATION-SETTLED` — `C6` holds | `SPECIFICATION-DIVERGED` |
| `V33-2` | `CORPUS-CONFORMING` — `conformance/` at `E` is `conformance/` at `B` less the removed vector, plus the ten added vectors, each matching its frozen row; `C1` holds | `CORPUS-FAILED` |
| `V33-3` | `DEPARTURES-DEMONSTRATED` — `conformance-pending/` at `E` holds exactly the eleven pending vectors, each matching its frozen row; `C2` holds | `PENDING-VACUOUS` — a pending vector the unchanged shadow already meets |
| `V33-4` | `SETTLEMENTS-SATISFIABLE` — `C3` and `C4` hold | `SPEC-CONTRADICTORY` — no patch meets the corpus and the pending set together; or `CONTROL-VOID` |
| `V33-5` | `ALTERNATIVES-EXCLUDED` — `C5` holds for every alternative the settlement tables name with a vector | `CONTROL-VOID` |
| `V33-6` | `PROPAGATED` — `C7` holds; and at `E`, of the files under `verification/` outside the round directories and the two vector directories, the phrase "provisional reading" occurs only in `verification/README.md`, and there only in the paragraph `C7` fixes | `STALE-SURFACE` |
| `V33-7` | `SHADOW-UNCHANGED` — `tools/v3_verifier.py`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard and `AGENTS.md` have their `B` blobs at `E`; the guard at `E` gives 105 PASS and 0 FAIL with `D`'s verdict map; `V2` is authoritative OK; the release gate passes 19 of 19; the shadow's self-test passes; no act of `V3-2`'s promotion boundary is present | `AUTHORITY-LEAKED` — fails the round |
| `V33-8` | `SCOPE-HELD` — `git diff --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V33-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V33-1` | `SPECIFICATION-SETTLED`; `architecture.md`'s blob at `E` `841bb5d51c5b554555a19cf28b526c9ea7a1dd16` | strong | the edits are frozen, each located block occurs once at `D`, and applying them to the blob at `D` gives that blob |
| `V33-2` | `CORPUS-CONFORMING`; the additions' digest `187c8301b1fb32b19089d14a8ad3c96462d841bf619fe24081a2d752a635d15b` | strong | measured at `D` (`F3`) |
| `V33-3` | `DEPARTURES-DEMONSTRATED`; the pending digest `605f9328fa4751fb766362a743e043883249784c4899fe088038f01baa5d96bc` | strong | measured at `D` (`F3`) |
| `V33-4` | `SETTLEMENTS-SATISFIABLE` | strong | measured at `D` with the patch `481cf746` |
| `V33-5` | `ALTERNATIVES-EXCLUDED` | strong | measured at `D`: eighteen alternatives, each excluded |
| `V33-6` | `PROPAGATED`; `verification/README.md`'s blob at `E` `9500e26c39574ad75ffbc8e6f034d8e05d563eb9` | strong | at `D` the phrase occurs, outside round directories and vectors, only in that README paragraph and in the shadow's own source, which is not a status surface (hazard `H3`) |
| `V33-7` | `SHADOW-UNCHANGED` | strong | the budget writes no tool, workflow or gate |
| `V33-8` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such. `SETTLEMENTS-SATISFIABLE`
and `ALTERNATIVES-EXCLUDED` are consistency findings about the settlements and their vectors, made
with code by the author of the settlements; they are not evidence that the settlements are right.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V33-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V33-1` | one: `architecture.md` | `C6` |
| 2 | `V33-2`, `V33-3`, `V33-4`, `V33-5` | one: the corpus additions and removal, and `conformance-pending/` | `C1` to `C5` |
| 3 | `V33-6` | one: the README paragraph | `C7`, the surface check |
| 4 | `V33-7`, `V33-8` | one: the result note; its commit is `E` | the closing checks at `E`, then the exact-head pull request |

A stage-2 finding that a frozen vector does not decide what its row says is a stop outcome for the
target it bears on. It is recorded, and neither the vector nor the settlement is repaired in this
round.

## The mutation budget

- **Modified:** `verification/infrastructure/v3/architecture.md` (the sixteen frozen edits);
  `verification/README.md` (the one frozen paragraph).
- **Added:** the ten vectors of `verification/infrastructure/v3/conformance/` above; the eleven
  vectors of `verification/infrastructure/v3/conformance-pending/`;
  `verification/infrastructure/round-v3-3-specification-resolution/result.md`.
- **Deleted:**
  `verification/infrastructure/v3/conformance/g6-admit-record-class-by-broader-entry.json`.
- **Never written:** `tools/v3_verifier.py` and every other file under `tools/`, `.github/`,
  `AGENTS.md`, the guard and everything under `verification/lean/` and `verification/lean-mathlib/`,
  `verification/seals/`, `verification/certificates/`, `verification/programmes/`,
  `verification/audits/`, `verification/ROADMAP.md`, any other round's directory, `papers/` and
  `book/`. No `verification/receipts/` directory is created.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
the outputs of `C1` to `C7`, with the SHA-256 of the settlement patch and of each scratch script,
none of which is landed; the vectors' digests against the predictions; for each of the seven items,
its settlement and whether the shadow conforms, as measured at `E`; the gaps recorded below, as
recorded; and every discrepancy.

## What no outcome of this round licenses

1. Any sentence that V3 is operative, or that the shadow implements the settled specification.
2. Any change to `tools/v3_verifier.py` in this round, or any claim that the pending vectors are
   met.
3. Any claim about the validity of a historical round under any protocol.
4. Any change to `V1` or `V2` state, or to any required check.
5. Treating `G8` to `G12` as settled.
6. Reading `SETTLEMENTS-SATISFIABLE` or `ALTERNATIVES-EXCLUDED` as proof that the settlements are
   correct.
7. Editing `V3-2`'s records, or re-opening `V3-1` or `V3-2`.

## Gaps found while drafting, recorded and not settled

Drafting the settlements exposed five further places where `architecture.md` leaves a verifier or an
executor a choice. They lie outside the seven items this round was asked to settle, and are
recorded here, numbered after `V3-2`'s, for a later specification round.

| gap | where | the choice left open |
|---|---|---|
| `G8` | `S1` | a mutable ref or host state may enter a predicate when the control plane "declares, prospectively and by name, that the round owns it", but no form of that declaration is given; the shadow implements no such predicate |
| `G9` | `S2`, `T1` | `S2` calls the amendments before `F` append-only, while `T1`'s predicate admits any change to a control-plane file before `F`: revising the preregistration, changing or deleting an amendment |
| `G10` | `S7`, `K1`, `K2` | which lines open and close a fenced block: the shadow recognizes only a line that is exactly three backticks and the info string, closed by a line of exactly three backticks, and ignores enclosing fences; CommonMark also admits tilde fences, longer fences, indentation and nesting |
| `G11` | `S3`, `S10` | whether an unpublished object after `E` — a reconciliation or a receipt commit — may be replaced before publication, or only appended to ("later objects only append") |
| `G12` | `S11`, `G6` | where seal records lie and what they hold: `G6` admits a seal record entry at any single file outside the record directory, another round's receipt path included |

## Hazards

- **`H1` — one author.** The shadow, `V3-2`'s readings, the settlements, the vectors and the scratch
  patches have one author. The controls establish consistency: that the settlements can be met
  together with every other vector, and that each vector separates what it is said to separate. A
  misreading shared by all of them is not excluded; the owner's review of the settlements is the
  check on it.
- **`H2` — strictness per commit.** `K3`, `K4`, `G5` and `G7` make a defective commit appended
  after `E` fatal to the round unless such a commit may be replaced before publication, which is
  `G11`. The settlements accept that cost rather than certify an object the specification's
  definitions exclude.
- **`H3` — the shadow's printed readings.** The shadow prints `K1`–`K4` at every run as provisional
  readings awaiting a specification round. After this round that text is stale, and it stays so
  until an implementation round changes the tool; the report is not a status artifact, and the
  README paragraph states the position.
- **`H4` — pending vectors are not run by continuous integration.** Their failure on the shadow is
  this round's measurement. An implementation round that meets a pending vector moves it into the
  corpus with the change that meets it.
- **`H5` — frozen blobs.** If `main` moves before `B` and changes a file this freeze pins, the
  preconditions fail at `M` and the freeze is redrafted from a new `D`.

## Files

### Files this round reads AND writes

`verification/infrastructure/v3/architecture.md` (the frozen edits); `verification/README.md` (the
one frozen paragraph); `verification/infrastructure/v3/conformance/` (ten added, one removed);
`verification/infrastructure/v3/conformance-pending/` (created, eleven added).

### Files this round reads and MUST NOT write

`tools/v3_verifier.py`, `tools/certificate_verifier.py`, `tools/release_gate.py`,
`tools/control_plane_base_check.py`, `tools/control_plane_lint.py`, `.github/workflows/verify.yml`,
the guard, `AGENTS.md`, and `V3-2`'s round directory.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to. The `B`-scoped rows assert that no
execution object exists at `B`, reading the tree directly.

```control-plane-preconditions
d: 347113a234ef5eea6986b663ea0971687591b33b
frozen-blob: verification/infrastructure/v3/architecture.md 6c80e584021f973c529625b1da89469e7b136dfe
frozen-blob: tools/v3_verifier.py 2c34d4d7f1adadc4bdecbad94ff8eadb7b30f974
frozen-blob: verification/README.md 052dfa270479c12470173ee90f340c4f805dac37
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-3' -e 'v3-3' -e 'round-v3-3' -e 'V33-' -e 'specification-resolution' $D", "expect": "empty"}
{"id": "d1-pending-free", "scope": "D", "check": "git grep -l -F -e 'conformance-pending' $D", "expect": "empty"}
{"id": "d1-no-pending-dir", "scope": "D", "check": "git ls-tree -d --name-only $D verification/infrastructure/v3/conformance-pending", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
# row 2: the corpus at D
{"id": "d2-corpus-84", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 84", "expect": "exit0"}
{"id": "d2-removed-vector-present", "scope": "D", "check": "git cat-file -e $D:verification/infrastructure/v3/conformance/g6-admit-record-class-by-broader-entry.json", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-3-specification-resolution/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-3-specification-resolution | grep -v -x -F 'verification/infrastructure/round-v3-3-specification-resolution/preregistration.md'", "expect": "empty"}
{"id": "b4-no-pending-dir", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/infrastructure/v3/conformance-pending", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-3-specification-resolution/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. Each commit-bearing stage
commits before its checkpoint. A stop outcome halts the round; the halt is recorded in a result note
with the outcomes reached, and nothing else of the execution lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B` has
one parent, that the oldest has `B` as its parent, and that the branch absorbed no later `main`,
recorded in the result and followed by exact-head review. `V3-3` carries no guard clause, manifest
record or round certificate (reading `R5`).

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — settlements inside the sections they settle.** Each settlement is a subsection of the
  section whose ambiguity it resolves, with a traceability row and the lifecycle predicates updated,
  so that a reader of `S7` or `S9` meets the rule where it applies. The declined option appends the
  seven settlements as a separate section.
- **`R2` — departures in a sibling directory.** The vectors on which a settlement departs from the
  shadow are landed in `verification/infrastructure/v3/conformance-pending/`, which the shadow's
  runs do not execute; the corpus stays exactly the set the shadow runs, and meets. The
  implementation round that changes the shadow finds the vectors that justify each change already
  frozen here, not chosen by itself. The declined options are: adding them to the corpus, which
  turns the shadow job red on every build; not landing them, which leaves the settlements without
  executable form; and a subdirectory of the corpus, which blurs what the corpus's exact set is.
- **`R3` — the shadow unchanged.** The owner's direction keeps `tools/v3_verifier.py` unchanged
  unless the settled specification demonstrably requires an implementation round. The eleven
  pending vectors, failing on the shadow and met by the settlement patch, are that demonstration.
  This round does not make the change.
- **`R4` — the status correction.** `verification/README.md`'s paragraph is corrected here because
  §A.25 requires a status change to reach every surface that states it, and this is the one surface
  at `D` that does. The declined option leaves the paragraph for the implementation round.
- **`R5` — no guard clause, certificate or attestation**, as for `V3-1` and `V3-2`.
- **`R6` — §A.37's two pull requests.** `V3-2`'s single-pull-request arrangement was an exception
  for that round and is not precedent; nothing in this round turns on it.
- **`R7` — vectors frozen by their rows.** Each vector is frozen by its identifier, settlements,
  recipe and expected verdict; the drafting-time bytes are a prediction. The declined option pins
  each file's digest, which would turn a byte of formatting into a stop.
- **`R8` — `G8` to `G12` recorded, not settled.** They were found while drafting and lie outside
  the seven items the round was asked to settle.
