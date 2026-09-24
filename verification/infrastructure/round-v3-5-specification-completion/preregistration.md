# Verifier round V3-5 — V3 specification completion: the gaps G8–G12: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The amended
specification, the conformance vectors, the README paragraph and the result note are execution
objects, created only after the certified merge of this file.

> **The specification is settled on its merits, and the shadow is then measured against it.** A
> settlement is never chosen because the shadow already implements it, and never rejected because
> the shadow does not.

Where a settlement below agrees with what the shadow does at `D`, the alternatives were weighed and
that behaviour was the better one; where it departs, the departure is recorded with the vectors
that show it, and the shadow is left unchanged.

## The commit vocabulary this freeze uses, fixed first

`V3-5` is run under `AGENTS.md` §A.37 as it stands at `D`: two pull requests, this control plane
and then one execution pull request that carries its landing.

- `D` = `f639af0abf67fb252f048e631e6237f84a25df24`, the drafting snapshot: the certified head of
  `main` after `V3-4`'s landing (push run 35995216658, all six jobs green), designated by the owner
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

## What `V3-5` is, and what it is not

`V3-5` is a **specification round**. It settles, normatively and in the text of
`verification/infrastructure/v3/architecture.md`, the five places `V3-3` recorded as gaps and left
unsettled: `G8` to `G12`. With them the specification has no recorded gap. It adds conformance
vectors that separate each settlement from the alternatives it rejects, places the vectors the
shadow does not meet where the shadow's runs do not execute them, and brings the one paragraph of
`verification/README.md` that describes the shadow's relation to the specification up to date.

It is not:

1. **An implementation round.** `tools/v3_verifier.py` is not written. The settlements of `G10` and
   `G12` depart from what the shadow does; their vectors are placed in
   `verification/infrastructure/v3/conformance-pending/`, and a later implementation round owns the
   change.
2. **A promotion.** No act of `V3-2`'s promotion boundary is performed. No V3 verdict gates
   anything, and the continuous-integration authority of every job is unchanged.
3. **A migration.** No historical round is translated, classified or touched, no `V1` or `V2` state
   is created, changed or removed, and no file under `verification/seals/` is written. `G12` gives
   V3 seal records their own namespace, `verification/v3-seals/`, and leaves
   `verification/seals/` to protocol 2; how the facts in protocol 2's records map into V3 receipts
   is the migration census's question.
4. **A bootstrap round.** How the first V3-governed round is certified and published is not
   addressed.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-5`, `v3-5`, `round-v3-5`, `V35-`, `specification-completion`, `v3-owned-refs` and `v3-seals`
occur nowhere in the tree at `D`. None of `verification/infrastructure/v3/conformance-pending/`,
`verification/receipts/` and `verification/v3-seals/` exists at `D`; the first was removed by
`V3-4`.

### `F2` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `verification/infrastructure/v3/architecture.md` | `3326bf309d6392e4e5d69a9e7ab6d812dba035af` |
| `tools/v3_verifier.py` | `883122c4070408ee3957d969e095324b62e21a87` |
| `verification/README.md` | `690f841ec02dbafbed972667a426cf41fc4ca741` |

`verification/infrastructure/v3/conformance/` holds 105 vectors at `D`. The shadow runs them as an
exact set: every top-level `*.json` file of the directory, each named for its `id`.

### `F3` — the corpus is regenerable, and `G12` changes nine of its vectors

A throwaway generator that reuses the recipe helpers of `V3-2`, `V3-3` and `V3-4` regenerates the
105 vectors at `D` byte for byte. Run again with one change — each sealing round's seal record at
`verification/v3-seals/<round>.json` rather than at `verification/seals/` under the round id with
its hyphen removed, and the example receipts and set G2 read from `architecture.md` as the frozen
edits leave it — it changes
exactly nine vectors and no others (`G12`, below). Under the settlement patch, the nine at `D`
behave as follows: four run not as expected (`k4-admit-sealing-superseded-receipt-commit`,
`mc7-counter-seal-record-missing-from-q`, `mc7-pass-sealing` and `s4-canonical-ex-2`, each failing
`s4:seal`); three still run as expected but only beside a failure of their seal entry
(`g6-reject-halted-landing-publishes-unnamed-seal-record`,
`g6-reject-halted-record-commit-writes-unnamed-seal-record` and
`k1-reject-receipt-kind-disagrees-with-declaration`); and two are copies of the specification's own
examples, which the frozen edits change (`s4-seal-in-non-sealing`, which carries example `EX-2`'s
`seal` field, and `s7-g2-nested`, which is set G2).

### `F4` — the candidate vectors, measured at `D` in scratch

Every vector the tables below freeze was built at `D` in scratch. No expected verdict was taken
from any implementation's output.

- **On the unchanged shadow** (blob `883122c4`): the 116 vectors of the corpus at `E` — the 105 with
  the nine modified, and the eleven additions — ran as expected; each of the seventeen pending
  vectors ran **not** as expected, each returning `HOLDS`.
- **On a settlement patch** — a scratch copy of the shadow changed only where the `G10` and `G12`
  settlements depart from it, never tracked, with SHA-256
  `b63e12d86036e643c3ac250cb8ad0e443fb43e6448ed558baaa06082be40c534`:
  all 116 corpus vectors and all seventeen pending vectors ran as expected.
- **Own rule.** The patch is five rules. With each taken out, exactly the pending vectors it owns
  ran not as expected, and every other pending vector ran as expected.
- **Rejected alternatives.** For each of the twelve rejected alternatives the tables below name
  with a vector, a scratch copy implementing it turned each of its distinguishing vectors from as
  expected to not as expected.

### `F5` — what the pending vectors expose in the shadow's behaviour

- **A line a reader takes for a declaration is ignored.** A tilde fence, a fence of four
  backticks, an indented fence, an opener with further text or a CR, each carrying governed-path
  entries or a round declaration, renders as a declaration and changes nothing the shadow reads.
- **A sealing round's seal entry may name any single file.** The shadow admits a seal entry at a
  path unrelated to the round, in protocol 2's `verification/seals/`, at another round's receipt
  path, or with `M`, and a sealing round with no seal entry at all.
- **A round may change another round's durable state.** An `execution` entry covering
  `verification/receipts/`, `verification/seals/` or `verification/v3-seals/` lets the execution
  add or change another round's receipt or seal record, or protocol 2's seal state, and the shadow
  returns `HOLDS`.
- **A receipt commit may modify an existing file.** A sealing round whose seal record path is
  already occupied publishes its "seal record" by modifying that file, and the shadow returns
  `HOLDS`.

### `F6` — tooling at `D`

Python 3.11 and git 2.43 in the drafting environment; the workflow pins Python 3.11. The
repository's object format is `sha1`. `tools/control_plane_lint.py` and
`tools/control_plane_base_check.py` read this file's preconditions block.

## The settlements, FROZEN

Each item states: the gap as `V3-3` recorded it; the alternatives considered; the settlement, whose
exact normative text is frozen in the next section; why it is chosen; the vectors that separate it
from each alternative; and whether the shadow at `D` conforms, as measured.

### Item `G8` — mutable state and predicates

- **Gap.** `S1` admits a mutable ref or host state into a predicate when the control plane
  "declares, prospectively and by name, that the round owns it", and gives no form of that
  declaration; the shadow implements no such predicate.
- **Alternatives.** (a) A declaration form — a `v3-owned-refs` block, say — and predicates over the
  named refs inside the execution window. (b) No mutable ref or host state is ever a predicate
  input: host facts are attestations or the executor's evidence, and publication inspects the live
  tip of `main` as an operation only. (c) (b), with a control plane that claims ownership of a ref
  invalid.
- **Settlement.** (b). Frozen text: edits `N3`, `N4`, `N5`.
- **Why.** `S1` and `S6` decide a round from commits alone, each assertion reconstructed at its
  named subject. A predicate over a ref inside the execution window reads a state that no commit
  records, so no verifier can re-derive it afterwards, and `S1` already says no historical verdict
  depends on it. Under (a) it is an executor's measurement given a predicate's name, and the
  declaration is syntax with no verifiable consequence. The one case `V3-1`'s census attributes to
  the clause, `GH-1`'s check of the ref deletion it declared it owned (mechanism `M7`), is a host
  observation of that kind: a fact about `GH-1` for the migration census, not a mechanism for V3.
  (c) makes a round invalid for words that no predicate reads.
- **Vectors.** (c): `g8-admit-ownership-declaration-inert` (new). No vector separates (a) from (b),
  since under both no historical verdict reads the ref; (a) is rejected by the argument above. The
  landed `mc1-pass-ref-churn`, `mc1-counter-branch-tip-refused` and `input-refuses-*` remain.
- **Shadow at `D`.** Conforms.

### Item `G9` — the control plane before `F`

- **Gap.** `S2` calls the amendments before `F` append-only, while `T1`'s predicate admits any
  change to a control-plane file before `F`.
- **Alternatives.** (a) Append-only: the preregistration is created once and never changed, and
  amendments are only added. (b) `T1`'s reading: before `F` any control-plane file of the round may
  be added, modified or deleted, and the freeze is `F`. (c) The preregistration may be revised;
  amendments are only added.
- **Settlement.** (b). Frozen text: edits `N6`, `N7`, `N13`, `N20`.
- **Why.** Every commit before `F` has one parent and stays in `F`'s history, so the drafting
  record is kept under every alternative; append-only adds no record the history lacks. What it
  adds is irreversibility before the freeze. Under (a) a declaration error in the preregistration
  cannot be corrected before `F`, because `K2` admits the declarations only there, and the round
  must be abandoned; under (c) an amendment withdrawn in review stays in the control plane at `F`
  and in the receipt. Nothing about the outcome exists before `F`, so revising the draft cannot fit
  a result to it. `V3-3` and `V3-4` each revised their preregistration in place before the freeze.
- **Vectors.** (a): `g9-admit-preregistration-revised-before-f` (new). (c):
  `g9-admit-amendment-revised-before-f` and `g9-admit-amendment-deleted-before-f` (new). The landed
  `mc8-pass-amendments-before-f` remains.
- **Shadow at `D`.** Conforms.

### Item `G10` — recognizing the declaration blocks

- **Gap.** `K1`, `K2` and `S7` speak of fenced blocks with an info string and do not say which lines
  open and close one. CommonMark admits tilde fences, fences of more than three backticks,
  indentation, info strings followed by further words, and nesting.
- **The shadow at `D`.** A block opens at a line that is exactly three backticks and the info
  string and closes at the next line of exactly three backticks; enclosing fences are ignored; an
  opener with no closer makes the control plane invalid; every other fence shape is ignored.
- **Alternatives.** (a) The shadow's behaviour. (b) CommonMark block structure: a declaration is a
  fenced block a CommonMark renderer produces, and a block nested in another fence is content.
  (c) Exact lines, with every near miss making the control plane invalid. (d) Exact lines, with the
  other fence shapes also read as declarations.
- **Settlement.** (c), with the lexical definitions of opener, closer, block, not closed and near
  miss frozen in edit `N13`. Frozen text: edits `N13`, `N20`.
- **Why.** A grammar the verifier reads differently from a renderer lets the reviewed text and the
  enforced text differ. (b) removes that only by importing a Markdown parser, and with it the
  parser's version, into the protocol. (a) and (d) keep the grammar small but differ from a
  renderer silently: under (a) a tilde fence of entries renders as a declaration and is ignored;
  under (d) the grammar grows to every fence shape. (c) keeps the shadow's grammar and makes every
  line a reader could take for a declaration, and which the verifier does not read as one, a
  failure. The two readings can then differ only where an exact opener lies inside another
  construct, which the raw text shows (hazard `H3`).
- **Vectors.** (b): `g10-admit-blocks-inside-other-fence` and
  `g10-reject-quoted-example-block-counts` (new). (d):
  `g10-reject-tilde-fence-as-only-governed-block` (new). (a): the six pending `g10-reject-*`
  vectors. `g10-reject-unclosed-opener` (new) states `K2`'s unclosed rule in `G10`'s terms; every
  alternative rejects it.
- **Shadow at `D`.** Does not conform: it ignores near misses.

### Item `G11` — the round's objects after `E`

- **Gap.** `S3` says later objects only append, and nothing says whether an unpublished
  reconciliation or receipt commit may be replaced before publication, or what "every
  reconciliation" in `K3` and "every receipt commit" in `K4` range over.
- **Alternatives.** (a) Append-only: every reconciliation and receipt commit the round ever builds
  is an object of the round, and a defective one is fatal. (b) The round's objects after `E` are
  those of the chain its final `Q` reaches; any other is not an object of the round.
- **Settlement.** (b). Frozen text: edits `N2`, `N3`, `N8`, `N9`, `N10`, `N16`, `N17`, `N18`, `N21`.
- **Why.** Under `S1` a verifier decides a round from `Q` and the commits its receipt names. An
  abandoned reconciliation that `Q` does not reach is not among them, and to find it a verifier
  would have to read refs, a reflog or the host's record of the pull request, which `S1` forbids.
  (a) therefore cannot be checked with the protocol's own inputs; it is a host discipline, and two
  rounds with the same repository facts could satisfy it and break it. `V3-3`'s hazard `H2`
  recorded its cost: one defective commit appended after `E` was fatal to the round. Under (b) the
  round's validity is a property of what `Q` reaches, which is what the receipt records and what
  publication makes reachable from `main`; an abandoned attempt never reaches `main`. `F..E` stays
  immutable: `E` is pinned by the receipt and by the certification attestations.
- **Vectors.** (a): `g11-admit-abandoned-attempt-off-chain` and
  `g11-admit-rebuild-from-e-after-failed-publication` (new).
  `g11-reject-receipt-lists-abandoned-reconciliation` (new): the reconciliations the receipt lists
  are the chain `Q` reaches, and an abandoned one cannot be listed. The landed `mc2-pass-base-drift`
  and `k4-admit-superseded-receipt-commit` remain.
- **Shadow at `D`.** Conforms.

### Item `G12` — the seal record

- **Gap.** `G6` admits in a sealing round one `record` entry at any single file outside the record
  directory, another round's receipt path included; nothing says where seal records lie, how many
  a round has, or what they hold.
- **Alternatives.** (a) `V3-3`'s text: any single file outside the record directory. (b) A seal
  directory per round, `verification/v3-seals/<round>/`, holding any files. (c) No seal record: a
  sealing round publishes its receipt only. (d) The fixed seal record, and further seal records
  within the record directory. (e) The fixed path, with the content validated as a `V2` manifest
  record. (f) The fixed path, with the round free to modify a file already there. (g) Exactly one
  seal record per sealing round, at `verification/v3-seals/<round>.json`, declared `record A`, its
  content opaque to V3; no V3 round changes another round's receipt or seal record, or any file
  under `verification/seals/`. (h) (g) with the seal record in protocol 2's namespace, at
  `verification/seals/<round>.json`.
- **Settlement.** (g). Frozen text: edits `N3`, `N11`, `N12`, `N14`, `N15`, `N18`, `N19`, `N20`,
  `N21`, `N22`, `N23`, `N24`, `N25`.
- **Why.** Under (a) a sealing round may declare, and publish as its own seal state, another round's
  receipt or seal record. A path fixed by the round id makes the seal record the round's own by
  construction and gives the migration census one place to look. `record A` makes the file the
  round's creation: a round cannot take over a file already at its path, because that change is a
  modification, which is unauthorized. The namespace is V3's own because `verification/seals/`
  already belongs to protocol 2: `AGENTS.md` §A.37 has every sealing round write its manifest record
  there, and `V2`'s manifest integrity rule reads every record the directory holds. Under (h) a V3
  seal record would enter the directory `V2` governs, a V3 round id could collide with a `V2` stem,
  and the migration census would have to tell two schemas apart in one directory. With (g) the two
  protocols' seal state never shares a directory, protocol 2's records stay what they are — legacy
  state whose facts the migration census maps into V3 receipts, not V3 seal records to be renamed or
  reinterpreted — and no V3 round can change them. (b) and (d) give a round many seal files, which
  no consumer needs and which widen what a receipt pins. (c) drops what a seal record gives that the
  receipt does not: a durable file at a fixed path that a consumer reads without parsing receipts.
  (e) duplicates receipt fields and binds V3 to the schema of a protocol that is to be retired. (f)
  lets a round rewrite state it did not create. The rule on other rounds' receipts and seal records
  states for every entry what the seal entry states for itself: no declaration reaches another
  round's durable state.
- **Vectors.** (a): the eleven pending `g12-reject-*` vectors. (b), (c) and (e): the modified
  `mc7-pass-sealing`. (d): `g12-reject-receipt-names-second-seal-record`. (f):
  `g12-reject-seal-record-path-already-present`. (h): `g12-reject-seal-entry-in-legacy-namespace`.
  Nine landed vectors are modified to the fixed path (`F3`).
- **Shadow at `D`.** Does not conform: it admits any single-file seal entry outside the record
  directory, one in `verification/seals/` included, a seal entry with `M`, a sealing round without
  one, any number of seal records, a modification at the seal record path, and changes to other
  rounds' receipts and seal records and to `verification/seals/`.

### Summary

| item | settlement | shadow at `D` conforms | new corpus vectors | modified | pending vectors |
|---|---|---|---|---|---|
| `G8` | (b) | yes | 1 | — | — |
| `G9` | (b) | yes | 3 | — | — |
| `G10` | (c) | no | 4 | — | 6 |
| `G11` | (b) | yes | 3 | — | — |
| `G12` | (g) | no | — | 9 | 11 |

The departures of `G10` and `G12` make one later implementation round necessary: seventeen pending
vectors fail on the shadow at `D`, and the settlement patch shows they can be met without breaking
any other vector.

## The normative text, FROZEN

The execution changes `verification/infrastructure/v3/architecture.md` by the twenty-five edits
below, applied in order to its blob at `B`, which the preconditions require to be its blob at `D`.
For a **replace**, the first block occurs exactly once in the file and is replaced by the second.
For an **insert**, the first block occurs exactly once and the second is inserted after it,
separated from it by one blank line. Every block ends with a newline. The file at `E` is
byte-identical to the result, and nothing else in it changes.

#### `N1` — replace, the provenance sentence

The located block:

```text
seven gaps round `V3-2` recorded, `K1` to `K4` and `G5` to `G7`, and each settlement is normative
text under its identifier. The specification is not operative: until a later round activates it,
every round is governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by
it.
```

Its replacement:

```text
seven gaps round `V3-2` recorded, `K1` to `K4` and `G5` to `G7`. Round `V3-5`, under the frozen
preregistration
`verification/infrastructure/round-v3-5-specification-completion/preregistration.md`, settled the
five gaps round `V3-3` recorded, `G8` to `G12`. Each settlement is normative text under its
identifier. The specification is not operative: until a later round activates it, every round is
governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by it.
```

#### `N2` — replace, the reconciliations in the objects table (`G11`)

The located block:

```text
| `R₁ … Rₖ` | the reconciliation commits, merges whose first parent is the tip of `main` when each is built |
```

Its replacement:

```text
| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parent is the tip of `main` when each is built |
```

#### `N3` — replace, the traceability table

The located block:

```text
| `G7` | no commit after `F` changes the control plane | `G7`, under `S2`; lifecycle transitions T3, T5, T6 and T7 |
```

Its replacement:

```text
| `G7` | no commit after `F` changes the control plane | `G7`, under `S2`; lifecycle transitions T3, T5, T6 and T7 |
| `G8` | mutable state is never a predicate input | `G8`, under `S1`; every predicate of the lifecycle |
| `G9` | before `F` the control plane is a draft | `G9`, under `S2`; lifecycle transition T1 |
| `G10` | declaration blocks are recognized by exact lines | `G10`, under `S7`; lifecycle transition T1 |
| `G11` | the round's later objects are those its final receipt commit reaches | `G11`, under `S3`; lifecycle transitions T6 and T7 |
| `G12` | the seal record | `G12`, under `S7`; lifecycle transitions T1, T3, T6 and T7 |
```

#### `N4` — replace, host state in `S1` (`G8`)

The located block:

```text
A mutable ref or host state **may** enter a predicate only when the round's control plane at `F`
declares, prospectively and by name, that the round owns it. Such a predicate is evaluated only
inside the round's execution window, between the designation of `F` and publication; no historical
verdict on the round depends on it afterwards.
```

Its replacement:

```text
A mutable ref or host state **must not** enter a V3 predicate, whatever the round's control plane
declares (`G8`).
```

#### `N5` — insert, `G8`

The anchor:

```text
Locating a commit is not a predicate. A verifier **may** be handed `E` or `Q` by any means — an
argument, a ref, a search of history — but whether the round holds is decided from the commits
alone. The one operation that reads the live tip of `main` is publication (`S10`), which either
succeeds atomically or leaves `main` untouched; it is never an input to the round's validity.
```

The inserted block:

```text
### `G8` — mutable state is never a predicate input

No control-plane declaration makes a mutable ref or host state an input to a predicate. The
specification defines no form for such a declaration, and a control plane that names a ref, a
branch or a host setting changes no predicate by doing so. Host facts enter a round in two ways
only. An owner's designation and a check run's conclusion are attestations (`S5`), recorded and
never read by a predicate. Anything else the executor observes on the host — the state of a branch,
a deletion it performs, a setting it changes — is the executor's evidence, recorded in the round's
result note and read by no predicate. Publication (`S10`) inspects the live tip of `main` as an
operation, and the outcome of that operation is not an input to the round's validity.
```

#### `N6` — replace, the drafting commits in `S2` (`G9`)

The located block:

```text
A V3 round is one pull request. It begins from `D` with control-plane-only commits: the
preregistration and, before `F` exists, append-only amendments. Each of these commits has exactly
one parent and changes only control-plane files of the round's record directory.

`F` is the exact commit the owner approves and designates. Before `F` is designated, amendments are
appended; after it, no commit **may** change a control-plane file. Execution begins only after the
required checks have passed on exactly `F` and the owner has designated `F`.
```

Its replacement:

```text
A V3 round is one pull request. It begins from `D` with control-plane-only commits, which create
the preregistration and may add amendments. Each of these commits has exactly one parent and
changes only control-plane files of the round's record directory.

`F` is the exact commit the owner approves and designates. Before `F` is designated, the control
plane is a draft, which a commit may revise (`G9`); after it, no commit **may** change a
control-plane file. Execution begins only after the required checks have passed on exactly `F` and
the owner has designated `F`.
```

#### `N7` — insert, `G9`

The anchor:

```text
`F`, and not a merge commit on `main`, is the execution's ancestry anchor. `delta(D, F)` touches only
control-plane files of the round's record directory.
```

The inserted block:

```text
### `G9` — before `F` the control plane is a draft

The commits of `rev-list F ^D` may add, modify and delete the round's control-plane files: the
preregistration may be rewritten, and an amendment revised or removed. Nothing before `F` is
append-only. The constraints on those commits are T1's: each has exactly one parent, `D` is an
ancestor of `F`, and each changes only control-plane files of the round's record directory. The
declarations in force are those `K2` reads at `F`, and no predicate reads the content of a
control-plane file at a commit before `F`. Every earlier state stays in `F`'s history.
```

#### `N8` — replace, `G7` over the round's objects (`G11`)

The located block:

```text
The rule that no commit after `F` changes a control-plane file binds every commit of the round after
`F`: each execution commit, `W` or the commit that takes its place (`S12`), each reconciliation, and
each receipt commit, superseded or final. At each of them the round's control-plane files are
exactly those at `F`, each with its state at `F`: none is changed, removed or added. A control-plane
file listed in `landing.resolved_paths` is no exception.
```

Its replacement:

```text
The rule that no commit after `F` changes a control-plane file binds every commit of the round after
`F`: each execution commit, `W` or the commit that takes its place (`S12`), and each reconciliation
and receipt commit of the round (`G11`), superseded or final. At each of them the round's
control-plane files are exactly those at `F`, each with its state at `F`: none is changed, removed
or added. A control-plane file listed in `landing.resolved_paths` is no exception.
```

#### `N9` — replace, the last sentence of `S3` (`G11`)

The located block:

```text
the owner designates `E`. Nothing after certification rewrites `F..E`; later objects only append.
```

Its replacement:

```text
the owner designates `E`. Nothing after certification rewrites `F..E`, and every later object of
the round descends from `E` (`G11`).
```

#### `N10` — insert, `G11`

The anchor:

```text
`delta(F, E)` **must** be authorized under `S7`, and no commit of `F..E` changes a control-plane
file.
```

The inserted block:

```text
### `G11` — the round's later objects are those its final receipt commit reaches

The reconciliations and receipt commits of the round are exactly those of one chain, which `Q`
fixes. `Λ`, `Q`'s parent, is the last reconciliation. Each reconciliation's second parent is either
a receipt commit, whose parent is the reconciliation before it in the chain, or, for `R₁`, `E`, `W`
or the commit in `W`'s place (`S12`). `landing.reconciliations` lists the chain's reconciliations,
in order, and nothing else. A reconciliation or receipt commit that `Q` does not reach through that
chain is not an object of the round, whether or not it exists in the repository or was once the
head of the pull request, and no predicate reads it.

Before publication a round may therefore abandon a reconciliation or receipt commit and build again
from `E`, from `W` or the commit in its place, or from a receipt commit it keeps. `F`, `E` and the
commits of `F..E` are never replaced. The result note may record abandoned objects as provenance;
they are not predicate inputs.
```

#### `N11` — replace, the `seal` row of the field table (`G12`)

The located block:

```text
| `seal` | object `{"records"}`: `records` an array of `{"path", "blob"}`, the seal records `Q` publishes, sorted by path bytes, non-empty | `Q` | `R` if `kind` is `"sealing"`, `—` otherwise | `—` | `—` |
```

Its replacement:

```text
| `seal` | object `{"records"}`: `records` an array of exactly one `{"path", "blob"}`, the round's seal record path and the object id of its file at `Q` (`G12`) | `Q` | `R` if `kind` is `"sealing"`, `—` otherwise | `—` | `—` |
```

#### `N12` — replace, authorization in `S7` (`G12`)

The located block:

```text
that entry's `<ops>`, with the status `T` counting as `M`. A path no entry governs is unauthorized;
this includes every path the text block cannot express.
```

Its replacement:

```text
that entry's `<ops>`, with the status `T` counting as `M`. A path no entry governs is unauthorized;
this includes every path the text block cannot express. A change `G12` excludes is unauthorized,
whichever entry governs it.
```

#### `N13` — replace, `K2`, and add `G10`

The located block:

```text
At `F`, the preregistration carries exactly one `v3-governed-paths` block and exactly one
`v3-round` block (`K1`), which are the declarations in force, and no amendment carries a fenced
block with either info string. A fenced block with either info string that is not closed, in any
control-plane file at `F`, makes the control plane invalid. This fixes where the declarations lie at
`F`, and nothing about how control-plane files may change before it.
```

Its replacement:

```text
At `F`, the preregistration carries exactly one `v3-governed-paths` block and exactly one
`v3-round` block (`K1`), which are the declarations in force, and no amendment carries a block with
either info string. Blocks are recognized as `G10` states. An opener that is not closed, or a near
miss, in any control-plane file at `F`, makes the control plane invalid. This fixes where the
declarations lie at `F`; how control-plane files may change before it is `G9`'s.

### `G10` — declaration blocks are recognized by exact lines

The declaration blocks are recognized in the bytes of each control-plane file, line by line and
without Markdown semantics. A line is the bytes between two LF bytes (0x0A), or between the start
or the end of the file and an LF; every other byte, a CR (0x0D) included, belongs to the line. With
`I` either reserved info string, `v3-round` or `v3-governed-paths`:

1. An **opener** for `I` is a line that is exactly three backticks (0x60) followed by `I`.
2. A **closer** is a line that is exactly three backticks.
3. A block for `I` begins at an opener for `I`. Its body is the lines after the opener up to, and
   not including, the first closer after it, where the block ends. An opener after which no closer
   occurs is **not closed**.
4. A **near miss** for `I` is a line that is not an opener and that consists of, in order: zero or
   more spaces (0x20) and TABs (0x09); a run of three or more backticks, or of three or more
   tildes (0x7E); zero or more spaces and TABs; `I`; and then either nothing, or a space, a TAB or
   a CR followed by any bytes.

Nesting has no meaning. An opener is an opener wherever it lies, inside another fenced block, an
HTML comment or any other Markdown construct, and every line of the file, the lines of a block's
body included, is examined for a near miss. A tilde fence, a fence of four or more backticks, an
indented fence and an opener followed by further text are near misses, never declarations. A line
whose info string only begins with `I`, such as `v3-roundtrip`, is neither an opener nor a near
miss. A fenced block with any other info string is not a declaration and is not read.
```

#### `N14` — replace, the record class for seal records (`G12`)

The located block:

```text
3. every other `record` entry's `<path>` lies within `R` or, in a sealing round only, is a single
   file outside `R`, not a directory prefix, declaring a seal record path.
```

Its replacement:

```text
3. every other `record` entry's `<path>` lies within `R`, except one: the block of a sealing round
   has the entry `record A S`, where `S` is the round's seal record path (`G12`).
```

#### `N15` — insert, `G12`

The anchor:

```text
(`S4`), so the record paths of a halted round are `P` and the paths within `R`. `S12`'s record
commit and halted landing admit record paths in this sense and no others.
```

The inserted block:

```text
### `G12` — the seal record

A sealing round has exactly one seal record, at its **seal record path**
`verification/v3-seals/<round>.json`, where `<round>` is its round id (`K1`). Its block at `F`
carries `record A` of that path (`G6`), so the round may add the file and may never modify or
delete it: if a file already lies at the path, the round's change to it is not an addition, and is
unauthorized. The receipt of a complete sealing round names exactly that path and the object id of
its file at `Q` (`S4`); a non-sealing receipt and a halted receipt name none.

V3 assigns the seal record no field and no format. Its protocol meaning is exactly this: the
durable blob the round owns at its fixed seal record path, whose object id the final receipt pins.
The `.json` extension is conventional. No V3 predicate parses the file or derives any validity from
its content; a consumer of a round's seal record may impose its own format on it, and the V3
verifier does not.

No round changes another round's receipt or seal state. A change is unauthorized, whichever entry
governs it, when it is to a path under `verification/receipts/` other than the round's receipt
path, to a path under `verification/v3-seals/` other than its seal record path, or to any path
under `verification/seals/`, which holds the seal state of protocol 2 and is no V3 round's.
```

#### `N16` — replace, `K3` over the round's reconciliations (`G11`)

The located block:

```text
The requirement that `D` lie on `LB`'s first-parent chain binds every reconciliation, not only the
last. `D` lies on the first-parent chain of `R₁`'s first parent, and for each `i > 1` the first
parent of `Rᵢ₋₁` lies on the first-parent chain of `Rᵢ`'s first parent. The first parents of the
reconciliations therefore lie, in order, on one first-parent chain, which is `LB`'s. Two consecutive
reconciliations may have the same first parent, when `main` has not moved between them. A round in
which one reconciliation's first parent lies behind an earlier one's is invalid, even when a later
reconciliation's first parent lies ahead of both.
```

Its replacement:

```text
The requirement that `D` lie on `LB`'s first-parent chain binds every reconciliation of the round
(`G11`), not only the last. `D` lies on the first-parent chain of `R₁`'s first parent, and for each
`i > 1` the first parent of `Rᵢ₋₁` lies on the first-parent chain of `Rᵢ`'s first parent. The first
parents of the reconciliations therefore lie, in order, on one first-parent chain, which is `LB`'s.
Two consecutive reconciliations may have the same first parent, when `main` has not moved between
them. A round in which one reconciliation's first parent lies behind an earlier one's is invalid,
even when a later reconciliation's first parent lies ahead of both.
```

#### `N17` — replace, the retry after a failed publication (`G11`)

The located block:

```text
and `main` is untouched. The round then:

1. appends a further reconciliation, whose first parent is the new tip of `main` and whose second
   parent is `Q`;
2. appends a new final receipt commit on it, whose receipt names the new `LB` and `Λ` and lists every
   reconciliation;
3. reruns the required checks on the new `Q`;
4. retries publication.

`F`, `E` and every earlier commit stay as they are. A superseded receipt commit remains in the
history as the second parent of the next reconciliation.
```

Its replacement:

```text
and `main` is untouched. The round then:

1. builds a further reconciliation, whose first parent is the new tip of `main` and whose second
   parent is either `Q`, which then remains in the round as a superseded receipt commit, or an
   object from which the round builds again (`G11`);
2. builds a new final receipt commit on it, whose receipt names the new `LB` and `Λ` and lists
   every reconciliation of the chain the new `Q` reaches;
3. reruns the required checks on the new `Q`;
4. retries publication.

`F`, `E` and the commits of `F..E` stay as they are.
```

#### `N18` — replace, `K4` over the round's receipt commits (`G11`, `G12`)

The located block:

```text
`S10`'s rule for `Q` binds every receipt commit of the round, superseded or final. Each receipt
commit `Qᵢ` is a single-parent child of the reconciliation `Rᵢ` before it, and `delta(Rᵢ, Qᵢ)` is
exactly the receipt path plus the seal records that the round's final receipt names. The content of
a superseded receipt is not read: the final receipt is the round's durable state (`S4`), and it
alone fixes which seal records any receipt commit carries.
```

Its replacement:

```text
`S10`'s rule for `Q` binds every receipt commit of the round (`G11`), superseded or final. Each
receipt commit `Qᵢ` is a single-parent child of the reconciliation `Rᵢ` before it, and
`delta(Rᵢ, Qᵢ)` is exactly the receipt path plus the seal record that the round's final receipt
names, each change authorized (`G12`). The content of a superseded receipt is not read: the final
receipt is the round's durable state (`S4`), and it alone fixes which seal record any receipt
commit carries.
```

#### `N19` — replace, `S11` (`G12`)

The located block:

```text
Sealing and non-sealing rounds use the same lifecycle, commits and receipt position. A sealing
receipt carries `seal`, and `Q` publishes the seal state it owns; a non-sealing receipt carries no
`seal`, and `Q` publishes none. The V3 lifecycle has no separate pin commit.
```

Its replacement:

```text
Sealing and non-sealing rounds use the same lifecycle, commits and receipt position. A sealing
receipt carries `seal`, and `Q` publishes the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` publishes none. The V3 lifecycle has no
separate pin commit.
```

#### `N20` — replace, lifecycle transition T1

The located block:

```text
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files; the round declaration and the governed-path block at `F` are valid and lie in the preregistration (`K1`, `S7`, `K2`); the record class is the round's own record (`G6`) | `D`, `F`, the commits between them, their trees |
```

Its replacement:

```text
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files, which it may add, modify or delete (`G9`); the round declaration and the governed-path block at `F` are valid, recognized by exact lines with no near miss (`G10`), and lie in the preregistration (`K1`, `S7`, `K2`); the record class is the round's own record, with a sealing round's seal record path (`G6`, `G12`) | `D`, `F`, the commits between them, their trees |
```

#### `N21` — replace, lifecycle transition T6

The located block:

```text
| T6: → `RECONCILED` | `S9`: each reconciliation's parents as specified, and its first parent as `K3` requires; each superseded receipt commit as `K4` requires; no control-plane file changes at any of them (`G7`); the landing authorized (`S9`, or `S12` with `G6`'s record paths) | `D`, `E` or `W`, each reconciliation and receipt commit, `LB`, `Λ`, their trees, the block at `F`, the seal records the final receipt names |
```

Its replacement:

```text
| T6: → `RECONCILED` | `S9`: each reconciliation of the chain `Q` reaches (`G11`) with its parents as specified, and its first parent as `K3` requires; each superseded receipt commit of that chain as `K4` requires; no control-plane file changes at any of them (`G7`); the landing authorized (`S9`, or `S12` with `G6`'s record paths) | `D`, `E` or `W`, each reconciliation and receipt commit of that chain, `LB`, `Λ`, their trees, the block at `F`, the seal record the final receipt names |
```

#### `N22` — replace, lifecycle transition T7

The located block:

```text
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal records (`K4`); no control-plane file changed at `Q` (`G7`); the receipt at `Q` valid under `S4` and consistent with every subject it records, its `round` and `kind` those of the declaration at `F` (`K1`) | `Q`, `Λ`, the receipt at `Q`, every commit it names |
```

Its replacement:

```text
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal record, each change authorized (`K4`, `G12`); no control-plane file changed at `Q` (`G7`); the receipt at `Q` valid under `S4` and consistent with every subject it records, its `round` and `kind` those of the declaration at `F` (`K1`), and its seal record the round's own (`G12`) | `Q`, `Λ`, the receipt at `Q`, every commit it names |
```

#### `N23` — replace, the seal record of set G2 (`G12`)

The located block:

```text
record A verification/seals/EX2.json
```

Its replacement:

```text
record A verification/v3-seals/EX-2.json
```

#### `N24` — replace, the digest of set G2 (`G12`)

The located block:

```text
Digest of G2: `9781ab0207e9d09d8f5f6f5bee3acd117f6743b568f25f619987ef6fae79489d`. Under G2, a change to a path is governed as follows:
```

Its replacement:

```text
Digest of G2: `0053d9c8bb76392786d52bd9f0da71dcd44455e51833bde01ec15b1ab2942d85`. Under G2, a change to a path is governed as follows:
```

#### `N25` — replace, the seal record of the sealing example receipt (`G12`)

The located block:

```text
      {"path": "verification/seals/EX2.json", "blob": "5555555555555555555555555555555555555555"}
```

Its replacement:

```text
      {"path": "verification/v3-seals/EX-2.json", "blob": "5555555555555555555555555555555555555555"}
```

## The README paragraph, FROZEN

The execution replaces, in `verification/README.md`, the paragraph on the shadow verifier. The
located block occurs exactly once at `B`; the file at `E` is its blob at `B` with that one
replacement.

The located block:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It is the V3 shadow implementation of the
currently settled protocol-3 rules (`infrastructure/v3/architecture.md`), including the
settlements of `K1`–`K4` and `G5`–`G7` that round `V3-3` fixed
(`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`). The gaps `G8`–`G12` that `V3-3`
recorded remain unsettled, and the shadow implements no settlement of them. It gates nothing: it
has no authoritative mode, no verdict it prints changes an exit status, the release gate does not
invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1` and `V2`
remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

Its replacement:

```text
`tools/v3_verifier.py` is the V3 shadow verifier, installed by round `V3-2`
(`infrastructure/round-v3-2-shadow-verifier/`). It implements the protocol-3 rules of
`infrastructure/v3/architecture.md` with two exceptions. It implements the settlements of
`K1`–`K4` and `G5`–`G7` that round `V3-3` fixed
(`infrastructure/round-v3-3-specification-resolution/`) and round `V3-4` implemented
(`infrastructure/round-v3-4-implementation-conformance/`), and it meets the settlements of `G8`,
`G9` and `G11` that round `V3-5` fixed (`infrastructure/round-v3-5-specification-completion/`).
It does not implement `V3-5`'s settlements of `G10` and `G12`; the vectors that separate them from
its behaviour are in `infrastructure/v3/conformance-pending/`, which it does not run. It gates
nothing: it has no authoritative mode, no verdict it prints changes an exit status, the release
gate does not invoke it, and its workflow job, `V3 shadow verifier`, is not a required check. `V1`
and `V2` remain authoritative. Its conformance corpus is `infrastructure/v3/conformance/`, executed
as an exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
```

## The conformance vectors, FROZEN

Every vector has the format of `V3-2`'s corpus (`id`, `settlements`, `kind`, recipe, expected
verdict and family), is built only from that format's existing recipe vocabulary, and is named for
its `id`. The recipes below use `V3-2`'s synthetic rounds: `D` holding `README.md`,
`tools/ex/keep.txt` and `verification/README.md`; a preregistration at `F` with the standard
declaration and the governed paths `record AM` of the record directory and of the receipt path,
`execution AMD tools/ex/` and `execution M verification/README.md` (plus, for a sealing round,
`record A verification/v3-seals/<round>.json`); two execution commits; `R1` with first parent `D`;
`Q` carrying the receipt. Only the differences are stated.

### Modified in `verification/infrastructure/v3/conformance/`

Each keeps its `id`, `settlements`, recipe and expected verdict; the only change is that each seal
record path is the round's fixed one, `verification/v3-seals/<round>.json`, and that the two copies
of the specification's examples follow the frozen edits.

| id | change |
|---|---|
| `g6-reject-halted-landing-publishes-unnamed-seal-record` | `seals/EX3.json` → `v3-seals/EX-3.json` |
| `g6-reject-halted-record-commit-writes-unnamed-seal-record` | `seals/EX4.json` → `v3-seals/EX-4.json` |
| `k1-reject-receipt-kind-disagrees-with-declaration` | the declared seal entry `seals/EX2.json` → `v3-seals/EX-2.json` |
| `k4-admit-sealing-superseded-receipt-commit` | `seals/EX2.json` → `v3-seals/EX-2.json` |
| `mc7-counter-seal-record-missing-from-q` | `seals/EX2.json` → `v3-seals/EX-2.json` |
| `mc7-pass-sealing` | `seals/EX2.json` → `v3-seals/EX-2.json` |
| `s4-canonical-ex-2` | the example receipt as edit `N25` leaves it |
| `s4-seal-in-non-sealing` | the `seal` field of example `EX-2` as edit `N25` leaves it |
| `s7-g2-nested` | set G2 and its digest as edits `N23` and `N24` leave them |

### Added to `verification/infrastructure/v3/conformance/`

| id | settlements | recipe | expected | excludes |
|---|---|---|---|---|
| `g8-admit-ownership-declaration-inert` | `G8`, `S1` | the preregistration also carries a `v3-owned-refs` block naming `refs/heads/main` and `refs/heads/dev`; the round is verified, `main` and `dev` are moved, `dev` is deleted, and it is verified again with the same output | HOLDS | `G8` (c) |
| `g9-admit-preregistration-revised-before-f` | `G9`, `S2` | a first control-plane commit `PR` carries a draft of the preregistration; `F` rewrites it | HOLDS | `G9` (a) |
| `g9-admit-amendment-revised-before-f` | `G9`, `S2` | `PR` adds the preregistration and an amendment; `F` rewrites the amendment | HOLDS | `G9` (c) |
| `g9-admit-amendment-deleted-before-f` | `G9`, `S2` | `PR` adds the preregistration and an amendment; `F` deletes the amendment | HOLDS | `G9` (c) |
| `g10-reject-unclosed-opener` | `G10`, `K2` | the preregistration ends with an opener for `v3-round` and no closer | FAILS `t1:` | — |
| `g10-admit-blocks-inside-other-fence` | `G10`, `K2` | both declaration blocks lie inside a fence of four backticks with info string `text` | HOLDS | `G10` (b) |
| `g10-reject-quoted-example-block-counts` | `G10`, `K2` | the preregistration also quotes, inside a fence of four backticks, an exact `v3-governed-paths` block | FAILS `t1:` | `G10` (b) |
| `g10-reject-tilde-fence-as-only-governed-block` | `G10`, `K2` | the governed paths are declared only in a tilde fence | FAILS `t1:` | `G10` (d) |
| `g11-admit-abandoned-attempt-off-chain` | `G11`, `S9`, `S10` | `R1a` (first parent `D`) and `Q1a`, which also adds `tools/ex/smuggled.txt`, are abandoned; `R1` (first parent `M2`, a child of `D`, second parent `E`) and `Q` form the chain | HOLDS | `G11` (a) |
| `g11-admit-rebuild-from-e-after-failed-publication` | `G11`, `S10` | `R1` and a valid `Q1` are abandoned after `main` moves to `M2`; `R2` (first parent `M2`, second parent `E`) and `Q` form the chain | HOLDS | `G11` (a) |
| `g11-reject-receipt-lists-abandoned-reconciliation` | `G11`, `S9`, `S4` | as the first `G11` vector, with the receipt listing `R1a` and `R1` | FAILS `s10:` | — |

### Added to `verification/infrastructure/v3/conformance-pending/`

The shadow does not run this directory. Each vector below states the settled verdict; the shadow at
`D` returns `HOLDS` on every one.

| id | settlements | recipe | expected |
|---|---|---|---|
| `g10-reject-tilde-fence` | `G10`, `K2` | the standard preregistration also carries a tilde fence with info string `v3-governed-paths` and the entry `execution AMD other/` | FAILS `t1:` |
| `g10-reject-longer-backtick-fence` | `G10`, `K2` | the same block in a fence of four backticks | FAILS `t1:` |
| `g10-reject-indented-opener` | `G10`, `K2` | an opener for `v3-round` indented by three spaces, with a round line and an indented closer | FAILS `t1:` |
| `g10-reject-opener-with-trailing-text` | `G10`, `K2` | an opener for `v3-governed-paths` followed by ` extra`, with an entry and a closer | FAILS `t1:` |
| `g10-reject-opener-with-cr` | `G10`, `K2` | an opener for `v3-governed-paths`, its entry and its closer, each line ending in CR LF | FAILS `t1:` |
| `g10-reject-near-miss-in-amendment` | `G10`, `K2` | an amendment before `F` carrying a tilde fence with info string `v3-round` | FAILS `t1:` |
| `g12-reject-seal-entry-not-at-fixed-path` | `G12`, `G6`, `S7` | halted sealing `EX-4` without execution commits, whose block declares `record A verification/v3-seals/EX4.json` | FAILS `t1:` |
| `g12-reject-seal-entry-in-legacy-namespace` | `G12`, `G6`, `S7` | as above, declaring `record A verification/seals/EX-4.json` | FAILS `t1:` |
| `g12-reject-seal-entry-not-add-only` | `G12`, `G6`, `S7` | as above, declaring `record AM verification/v3-seals/EX-4.json` | FAILS `t1:` |
| `g12-reject-seal-entry-names-another-rounds-receipt` | `G12`, `G6`, `S7` | as above, declaring `record A verification/receipts/EX-9.json` | FAILS `t1:` |
| `g12-reject-sealing-round-without-seal-entry` | `G12`, `G6`, `S7` | as above, with no seal entry | FAILS `t1:` |
| `g12-reject-receipt-seal-path-not-fixed` | `G12`, `S4` | example receipt `EX-2` with its seal record at `verification/seals/EX-2.json` | FAILS `s4:` |
| `g12-reject-receipt-names-second-seal-record` | `G12`, `S4`, `S11` | complete sealing `EX-2` whose `Q` adds and whose receipt names the fixed seal record and `seal-extra.json` in the record directory | FAILS `s4:` |
| `g12-reject-seal-record-path-already-present` | `G12`, `S10`, `K4` | complete sealing `EX-2` with a file at `verification/v3-seals/EX-2.json` at `D`, which `Q` modifies | FAILS `s10:` |
| `g12-reject-execution-changes-another-rounds-receipt` | `G12`, `S7`, `S3` | the block also declares `execution AMD verification/receipts/`; the execution adds `verification/receipts/EX-9.json` | FAILS `s3:` |
| `g12-reject-execution-changes-legacy-seal-namespace` | `G12`, `S7`, `S3` | the block also declares `execution AMD verification/seals/`; the execution adds `verification/seals/OTHER.json` | FAILS `s3:` |
| `g12-reject-execution-changes-another-rounds-seal-record` | `G12`, `S7`, `S3` | the block also declares `execution AMD verification/v3-seals/`; the execution adds `verification/v3-seals/EX-9.json` | FAILS `s3:` |

The drafting-time digests, SHA-256 of each set's files concatenated in path order, are:

- the nine modified vectors: `2a0cc7d8a883c6b1d806721c1fd531ff71f3f937e087c831630f72de1aaf6303`;
- the eleven corpus additions: `b0f3db227e5c02370aa83c3f2a7fd5a77d563f6494f145d9fdaa93a62e65c3c6`;
- the seventeen pending vectors: `8d2209b69b5f516d4d1a6ce12d633ece91e18cc4a91fd25dfb3f7ed90a994069`.

They are predictions, not pins: a vector that differs
from its drafting-time bytes while matching its frozen row is recorded as a discrepancy.

## The controls, FROZEN

Each control runs at the execution's stage-2 checkpoint and again at `E`.

- **`C1` — the corpus on the unchanged shadow.** `tools/v3_verifier.py --corpus` at `E` runs the 116
  vectors of `conformance/` as an exact set, every one as expected, exit 0.
- **`C2` — the pending set on the unchanged shadow.** `tools/v3_verifier.py --corpus` on
  `conformance-pending/` runs its seventeen vectors, and every one of them runs **not** as expected,
  returning `HOLDS`.
- **`C3` — satisfiability.** A scratch copy of the shadow, changed only where the `G10` and `G12`
  settlements depart from it and never tracked, runs `conformance/` and `conformance-pending/` at
  `E`, every vector as expected. Its SHA-256 is recorded; its code enters no tracked file.
- **`C4` — own rule.** The settlement patch is five rules, each owning the pending vectors in this
  table. For each rule, the patch with that rule taken out runs the vectors it owns not as expected
  and every other pending vector as expected.

  | rule | owned pending vectors |
  |---|---|
  | near misses (`G10`) | the six `g10-reject-*` pending vectors |
  | the seal entry at `F` (`G12`) | `g12-reject-seal-entry-*`, `g12-reject-sealing-round-*` |
  | the receipt names the fixed seal record alone (`G12`) | `g12-reject-receipt-*` |
  | each receipt commit's changes authorized (`G12`) | `g12-reject-seal-record-path-*` |
  | no change to another round's receipt or seal state (`G12`) | `g12-reject-execution-*` |

- **`C5` — rejected alternatives.** For each rejected alternative the settlement tables name with a
  distinguishing vector, other than the shadow's own behaviour, which `C2` exercises, a scratch
  copy implementing it runs each of its distinguishing vectors not as expected, while the copy it
  was made from runs them as expected. The copies are of the unchanged shadow for `G8` (c), `G9`
  (a) and (c), `G10` (b) and `G11` (a), and of the settlement patch for `G10` (d) and `G12` (b),
  (c), (d), (e), (f) and (h). There are twelve.
- **`C6` — the normative text.** Applying the frozen edits to `architecture.md`'s blob at `B`
  yields its blob at `E` exactly.
- **`C7` — the README paragraph.** Applying the frozen replacement to `verification/README.md`'s
  blob at `B` yields its blob at `E` exactly.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its
target stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V35-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V35-1` | `SPECIFICATION-SETTLED` — `C6` holds | `SPECIFICATION-DIVERGED` |
| `V35-2` | `STATUS-CURRENT` — `C7` holds | `STATUS-DIVERGED` |
| `V35-3` | `CORPUS-CONFORMING` — `conformance/` at `E` is `conformance/` at `B` with the nine vectors modified and the eleven added, each matching its frozen row; `C1` holds | `CORPUS-FAILED` |
| `V35-4` | `DEPARTURES-DEMONSTRATED` — `conformance-pending/` at `E` holds exactly the seventeen pending vectors, each matching its frozen row; `C2` holds | `PENDING-VACUOUS` — a pending vector the unchanged shadow already meets |
| `V35-5` | `SETTLEMENTS-SATISFIABLE` — `C3` and `C4` hold | `SPEC-CONTRADICTORY` — no patch meets the corpus and the pending set together; or `CONTROL-VOID` |
| `V35-6` | `ALTERNATIVES-EXCLUDED` — `C5` holds for every alternative the settlement tables name with a vector | `CONTROL-VOID` |
| `V35-7` | `SHADOW-UNCHANGED` — `tools/v3_verifier.py`, `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard and `AGENTS.md` have their `B` blobs at `E`; the guard at `E` gives 105 PASS and 0 FAIL with `D`'s verdict map; `V2` is authoritative OK; the release gate passes 19 of 19; the shadow's self-test passes; no act of `V3-2`'s promotion boundary is present | `AUTHORITY-LEAKED` — fails the round |
| `V35-8` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

The repository-wide conditions of `V35-7` — the guard, `V2`, the release gate — are read from the
exact-head continuous-integration run on `E`, not run locally.

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V35-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V35-1` | `SPECIFICATION-SETTLED`; `architecture.md`'s blob at `E` `12cff3f2c9b2cb7803ed1572c98bccba7590c707` | strong | the edits are frozen, each located block occurs once at `D`, and applying them to the blob at `D` gives that blob |
| `V35-2` | `STATUS-CURRENT`; `verification/README.md`'s blob at `E` `50c390168966980c4ebf590a78c4269089af68c2` | strong | the same, for the one replacement |
| `V35-3` | `CORPUS-CONFORMING`; the digests `2a0cc7d8` (modified) and `b0f3db22` (added) | strong | measured at `D` (`F4`) |
| `V35-4` | `DEPARTURES-DEMONSTRATED`; the pending digest `8d2209b6` | strong | measured at `D` (`F4`) |
| `V35-5` | `SETTLEMENTS-SATISFIABLE` | strong | measured at `D` with the patch `b63e12d8` |
| `V35-6` | `ALTERNATIVES-EXCLUDED` | strong | measured at `D`: twelve alternatives, each excluded |
| `V35-7` | `SHADOW-UNCHANGED` | strong | the budget writes no tool, workflow or gate |
| `V35-8` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such. `SETTLEMENTS-SATISFIABLE`
and `ALTERNATIVES-EXCLUDED` are consistency findings about the settlements and their vectors, made
with code by the author of the settlements; they are not evidence that the settlements are right.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V35-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V35-1`, `V35-2` | one: `architecture.md` and `verification/README.md` | `C6`, `C7` |
| 2 | `V35-3` to `V35-6` | one: the nine modified and eleven added corpus vectors, and `conformance-pending/` | `C1` to `C5` |
| 3 | `V35-7`, `V35-8` | one: the result note; its commit is `E` | the closing checks at `E`, then the exact-head pull request |

A stage-2 finding that a frozen vector does not decide what its row says is a stop outcome for the
target it bears on. It is recorded, and neither the vector nor the settlement is repaired in this
round.

## The mutation budget

- **Modified:** `verification/infrastructure/v3/architecture.md` (the twenty-five frozen edits);
  `verification/README.md` (the one frozen replacement); the nine vectors of
  `verification/infrastructure/v3/conformance/` listed above.
- **Added:** the eleven vectors of `verification/infrastructure/v3/conformance/` above; the
  seventeen vectors of `verification/infrastructure/v3/conformance-pending/`;
  `verification/infrastructure/round-v3-5-specification-completion/result.md`.
- **Deleted:** nothing.
- **Never written:** `tools/v3_verifier.py` and every other file under `tools/`, `.github/`,
  `AGENTS.md`, the guard and everything under `verification/lean/` and `verification/lean-mathlib/`,
  `verification/seals/`, `verification/certificates/`, `verification/programmes/`,
  `verification/audits/`, `verification/ROADMAP.md`, any other round's directory, `papers/` and
  `book/`. Neither `verification/receipts/` nor `verification/v3-seals/` is created.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
the outputs of `C1` to `C7`, with the SHA-256 of the settlement patch and of each scratch script,
none of which is landed; the vectors' digests against the predictions; for each of the five items,
its settlement and whether the shadow conforms, as measured at `E`; and every discrepancy.

## What no outcome of this round licenses

1. Any sentence that V3 is operative, or that the shadow implements `G10` or `G12`.
2. Any change to `tools/v3_verifier.py` in this round, or any claim that the pending vectors are
   met.
3. Any claim about the validity of a historical round under any protocol, or about how the facts
   in protocol 2's records under `verification/seals/` map into V3 receipts.
4. Any change to `V1` or `V2` state, or to any required check.
5. Reading `SETTLEMENTS-SATISFIABLE` or `ALTERNATIVES-EXCLUDED` as proof that the settlements are
   correct.
6. Editing `V3-3`'s or `V3-4`'s records, or re-opening `V3-1` to `V3-4`.

## Hazards

- **`H1` — one author.** The shadow, the settlements, the vectors and the scratch patches have one
  author. The controls establish consistency: that the settlements can be met together with every
  other vector, and that each vector separates what it is said to separate. A misreading shared by
  all of them is not excluded; the owner's review of the settlements is the check on it.
- **`H2` — `G11` narrows what a verifier sees of a round's history.** Abandoned attempts are
  invisible to every predicate by design. What was abandoned, and why, is recorded only where an
  executor records it, in the result note as provenance.
- **`H3` — `G10` reads openers without Markdown structure.** An exact opener inside an HTML comment
  or another fence counts as a declaration although a renderer hides it or shows it as code. The
  raw text shows it, and review reads the raw text; `g10-reject-quoted-example-block-counts` fixes
  the consequence for a quoted example. A V3 control plane cannot quote a declaration block
  verbatim.
- **`H4` — `G12` and protocol 2's seal state.** `verification/seals/` holds `V2` manifest records,
  and under `G12` no V3 round may change them. A V3 round that must also satisfy protocol 2 while
  protocol 2 is authoritative — writing its `V2` manifest record there under §A.37 — cannot do so
  as a V3 round; the rounds that run under both protocols are the migration round's question, as
  is how protocol 2's recorded facts enter V3 receipts.
- **`H5` — pending vectors are not run by continuous integration.** Their failure on the shadow is
  this round's measurement. The implementation round that meets them moves them into the corpus.
- **`H6` — frozen blobs.** If `main` moves before `B` and changes a file this freeze pins, the
  preconditions fail at `M` and the freeze is redrafted from a new `D`.

## Files

### Files this round reads AND writes

`verification/infrastructure/v3/architecture.md` (the frozen edits); `verification/README.md` (the
frozen replacement); `verification/infrastructure/v3/conformance/` (nine modified, eleven added);
`verification/infrastructure/v3/conformance-pending/` (created, seventeen added).

### Files this round reads and MUST NOT write

`tools/v3_verifier.py`, `tools/certificate_verifier.py`, `tools/release_gate.py`,
`tools/control_plane_base_check.py`, `tools/control_plane_lint.py`, `.github/workflows/verify.yml`,
the guard, `AGENTS.md`, `verification/seals/`, and the round directories of `V3-1` to `V3-4`; and
`verification/v3-seals/`, which is not created.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to. The `B`-scoped rows assert that no
execution object exists at `B`, reading the tree directly.

```control-plane-preconditions
d: f639af0abf67fb252f048e631e6237f84a25df24
frozen-blob: verification/infrastructure/v3/architecture.md 3326bf309d6392e4e5d69a9e7ab6d812dba035af
frozen-blob: tools/v3_verifier.py 883122c4070408ee3957d969e095324b62e21a87
frozen-blob: verification/README.md 690f841ec02dbafbed972667a426cf41fc4ca741
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-5' -e 'v3-5' -e 'round-v3-5' -e 'V35-' -e 'specification-completion' -e 'v3-owned-refs' -e 'v3-seals' $D", "expect": "empty"}
{"id": "d1-no-pending-dir", "scope": "D", "check": "git ls-tree -d --name-only $D verification/infrastructure/v3/conformance-pending", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
{"id": "d1-v3-seals-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/v3-seals", "expect": "empty"}
# row 2: the corpus at D
{"id": "d2-corpus-105", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 105", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-5-specification-completion/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-5-specification-completion | grep -v -x -F 'verification/infrastructure/round-v3-5-specification-completion/preregistration.md'", "expect": "empty"}
{"id": "b4-no-pending-dir", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/infrastructure/v3/conformance-pending", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
{"id": "b4-no-v3-seals", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/v3-seals", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-5-specification-completion/preregistration.md", "expect": "exit0"}
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
commits before its checkpoint, and a stage's commit is pushed without waiting for continuous
integration on it: the certification of record is the exact-head run on `E`. A stop outcome halts
the round; the halt is recorded in a result note with the outcomes reached, and nothing else of the
execution lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B` has
one parent, that the oldest has `B` as its parent, and that the branch absorbed no later `main`,
recorded in the result and followed by exact-head review. `V3-5` carries no guard clause, manifest
record or round certificate (reading `R5`).

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — settlements inside the sections they settle.** As in `V3-3`, each settlement is a
  subsection of the section whose gap it closes, with a traceability row and the lifecycle
  predicates updated.
- **`R2` — departures in `conformance-pending/`.** `V3-4` removed the directory when it moved
  `V3-3`'s pending vectors into the corpus; this round creates it again for the `G10` and `G12`
  vectors, with the same role. The declined options are the ones `V3-3`'s `R2` declined.
- **`R3` — nine landed vectors modified in place.** Each keeps its identifier, its settlements, its
  recipe and its expected verdict; only the seal record path, which is incidental to what each
  vector tests, moves to the fixed path `G12` requires, and the two copies of the specification's
  examples follow the examples. The declined option retires the nine identifiers and adds nine
  replacements, which would retire identifiers whose claims are unchanged.
- **`R4` — the README paragraph.** At `D` the paragraph says `G8`–`G12` remain unsettled and that
  the shadow implements the currently settled rules; both become false when this round lands. The
  frozen replacement states what is then true — which settlements the shadow implements or meets,
  and which it does not — in the same landing (`AGENTS.md` §A.25). The declined option, `V3-3`'s,
  leaves the paragraph to the implementation round and ships a false status line in between.
- **`R5` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-4`.
- **`R6` — the tool's printed rule list.** The shadow prints `K1`–`K4` as its settled rules. The
  list names the rules it implements, and it stays true; the implementation round adds to it.
- **`R7` — vectors frozen by their rows.** Each vector is frozen by its identifier, settlements,
  recipe and expected verdict; the drafting-time bytes are a prediction.
