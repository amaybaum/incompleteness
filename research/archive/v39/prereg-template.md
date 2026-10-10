# Verifier round V3-9 — V3 made operable for provisional pilots: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The receipt
builder, the new `AGENTS.md` section, the narrowed specification preamble and the result note are
execution objects, created only after the certified merge of this file.

> **A permanent receipt builder, and one rule that lets an owner-authorized pilot run the native V3
> lifecycle.** `tools/v3_receipt.py` derives a receipt's repository facts from exact object ids;
> `AGENTS.md` gains `§A.39`, the provisional native lifecycle; the specification's preamble says V3
> is operative for such pilots and no other round. `§A.37`, `V1` and `V2` are unchanged.

## The commit vocabulary this freeze uses, fixed first

`V3-9` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `311f06ea174501587478024a09140297b56e089a`, the drafting snapshot: the certified head of
  `main` after `V3-8`'s landing (push run 36064453524, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Rᵢ`, `Λ`, `LB` and `Q` keep the meanings
`verification/infrastructure/v3/architecture.md` gives them. In this file they name objects of V3
rounds in general or of the synthetic rounds the conformance vectors build, never an object of this
round.

## What `V3-9` is, and what it is not

`V3-9` is an **operationalization round**, the first of four that finish the V3 programme: `V3-9`
makes V3 operable, `V3-10` runs one real provisional pilot, `V3-11` cuts authority over, and `V3-12`
retires the old stack. Only `V3-9` is frozen here; the others are named so that the scope of this
one is legible, and nothing in this file binds them. `V3-9` adds:

1. **A receipt builder**, `tools/v3_receipt.py`. Given the exact object ids of a round's commits and
   the attestation records the host holds, it derives every repository fact the receipt carries,
   with `tools/v3_verifier.py`'s own functions, and prints the receipt. It is a builder, not a
   verifier: whether a receipt commit holds remains `tools/v3_verifier.py --verify-round`'s
   question.
2. **`§A.39` in `AGENTS.md`**: a round the owner authorizes as a provisional V3 pilot runs the
   native lifecycle — one pull request from `D`, `F` designated, linear execution to a designated
   `E`, reconciliation if needed, the receipt commit `Q` built with the builder, `--verify-round Q`
   holding before the pull request lands through ordinary review and merge. `F`'s and `E`'s
   `check-run` attestations are dispatched runs on exactly those commits, and a pilot that halts
   after `F` closes through `S12`'s halted receipt.
3. **One preamble sentence** of the specification, which says V3 is operative only for such pilots.

It is not:

1. **A promotion.** No release-gate step, workflow job or required check is added or changed, no
   verdict of `tools/v3_verifier.py` gates anything, and `V1` and `V2` stay authoritative for every
   round, pilots included.
2. **A pilot.** No receipt is written: neither `verification/receipts/` nor
   `verification/v3-seals/` is created.
3. **A change to `§A.37`, to the specification's rules, or to the verifier.** `§A.37` stays the
   default and governs `V3-9` itself; the settlements `S1`–`S13`, `K1`–`K4` and `G5`–`G12`, the
   corpus and `tools/v3_verifier.py` are unchanged.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-9`, `v3-9`, `round-v3-9`, `V39-`, `v3_receipt` and `operationalization` occur nowhere in the
tree at `D`. Neither `tools/v3_receipt.py`, `verification/receipts/` nor `verification/v3-seals/`
exists at `D`.

### `F2` — the section number

`AGENTS.md` at `D` ends with `§A.37`, and neither `§A.38` nor `§A.39` occurs in it. `§A.38` is
already assigned, though never landed: `GH-1`'s frozen preregistration and its halt record name its
ref-hygiene rule `§A.38`. `§A.39` occurs at `D` only in `V3-1`'s preregistration, whose reading
`R2` declines to write "a prospective `§A.39`" and leaves the operative V3 rule to a later round.
This round's section is therefore `§A.39`, and `§A.38` stays `GH-1`'s.

### `F3` — the objects the round reads or writes, at `D`

| path | blob at `D` |
|---|---|
| `AGENTS.md` | `a9687b39c69973d35a2ff81c257687071fd35eca` |
| `verification/infrastructure/v3/architecture.md` | `db36dbd1ee4f779eff13525ffd3dc11d9041ab36` |
| `tools/v3_verifier.py` | `ccfbe813790e4855f408462449327f32e59d545b` |

`verification/infrastructure/v3/conformance/` holds 135 vectors at `D`. Of them, 29 are repository
vectors that commit a receipt and verify its receipt commit as holding, before any host-state step:
24 complete non-sealing, 2 complete sealing, 2 halted with execution commits and 1 halted without,
7 of the 29 with more than one reconciliation.

### `F4` — what a pilot needs from the present machinery

Measured at `D` with a scratch preregistration that carries no `control-plane-preconditions` block:
`tools/control_plane_lint.py` passes, `tools/control_plane_base_check.py --mode M` evaluates
0 rows with no failure, and `tools/artifact_placement_check.py` passes. `V2`'s live policy,
`verification/certificates/live-policy.json` (blob `78a5c1457ca222c65cb146cdcc9b3081b6e6909b`),
carries `"count": 0`, and the certificate verifier checks the certificate records that exist rather
than requiring one per round. A pilot therefore needs neither a precondition block nor a `V2`
certificate, and `V3-9` changes none of that machinery.

The guard reads `AGENTS.md` at the head in three places: `R7-MSP` for two phrases of `§A.35`, and
`SI2-7` and `SI3-6` for phrases of `§A.37` and the absence of two superseded sentences. Appending a
section after `§A.37` that carries none of those sentences changes none of the three.

### `F5` — the execution, simulated at `D`

The execution was simulated at `D` in a scratch worktree, each stage applied and committed with its
files, every tool run being the committed tool at that commit, run from the worktree. The results
are the predictions below:

| measurement | stage 1 | stage 2 |
|---|---|---|
| `tools/v3_receipt.py` blob | `{{BLOB:builder}}` | the same |
| `AGENTS.md` blob | `a9687b39` | `{{BLOB:agents}}` |
| `architecture.md` blob | `db36dbd1` | `{{BLOB:arch}}` |
| `tools/v3_verifier.py` blob | `ccfbe813` | the same |
| verifier corpus, exact and as expected | 135 | 135 |

At stage 1, `tools/v3_receipt.py --self-test` printed:

```text
{{SELFTEST}}```

## The builder, FROZEN by semantics

At stage 1 the execution adds `tools/v3_receipt.py` and changes nothing else. The file below is the
drafting-time implementation, with SHA-256
`{{SHA:builder}}`.
It is a prediction, as is its blob. A file whose text differs is recorded as a divergence, with its
diff, and the owner reviews every divergence for consistency with the semantics below before `E` is
designated; a divergence the owner finds inconsistent is a stop outcome for `V39-1`.

**Semantics.**

1. **Inputs.** The status (`complete` or `halted`); the exact object ids of `D`, `F`, `E` (complete
   only), `W` (halted with execution commits only) and the round's reconciliations in order; the
   resolved paths; each candidate's commit and what was measured on it; for a complete sealing
   round, the bytes of the seal record the receipt commit will carry; and the attestation records as
   (kind, subject, record). Every commit argument is refused unless it is a full-length lowercase
   hexadecimal object id, before any repository read.
2. **Derived, never supplied:** `round` and `kind` from the declaration at `F`; `object_format`; the
   control-plane blobs and the governed-path digest at `F`; `tree_e` and `S8`'s digest of
   `delta(F, E)`; each candidate's tree; the landing's base (the last reconciliation's first
   parent), object (the last reconciliation) and `S8`'s digest of `delta(LB, Λ)`; the seal record's
   path and blob; each attestation's commit; and `absent` with its reason codes. Each derivation
   calls `tools/v3_verifier.py`'s own function for it.
3. **Refusals.** The builder refuses — prints a reason and writes no receipt — when the control
   plane at `F` is not valid, when the status and the supplied commits disagree, when the last
   reconciliation is not a two-parent merge, when an attestation names a subject the status has no
   commit for, or when the result would not satisfy `S4` standalone.
4. **Not read:** no ref, branch, host state, clock or network. The builder does not decide whether
   `F` or `E` was designated, whether a check passed, or whether the round holds.
5. **Output.** The receipt as one JSON object, indent 1, UTF-8, with a trailing newline, to
   standard output or `--out <file>`.
6. **`--self-test`.** For every conformance vector whose receipt commit holds, it replays the vector
   up to that commit, reads the committed receipt's supplied data, rebuilds the receipt, and
   requires the rebuilt receipt to equal the committed one, the same inputs to come back from its
   command line, and a receipt commit carrying the rebuilt receipt to hold. On each of those it
   commits thirteen corrupted receipts, one per field class — `d`; `f`; a control-plane blob; the
   governed-path digest; `tree_e`; the execution delta digest; the landing's base, delta digest and
   reconciliations; the seal blob; an attestation's commit; the missing `F` designation; the schema
   version — each applied where the receipt has the field, and requires every one to fail. It
   requires each of the five shapes, complete non-sealing, complete sealing, halted with and
   without execution commits, and more than one reconciliation, to occur at least once. Exit 0
   only if all of this holds.

```text
{{BUILDER}}```

## The rule and the preamble, FROZEN as text

At stage 2 the execution appends the text below to `AGENTS.md` as it stands at `B`, byte for byte
after its last byte, and changes nothing else in the file:

```text
{{A39}}```

In the same commit the sentence below, which occurs exactly once in
`verification/infrastructure/v3/architecture.md` at `B`, is replaced by the second, and nothing else
in the file changes.

The sentence at `B`:

```text
{{PRE_OLD}}```

The sentence at `E`:

```text
{{PRE_NEW}}```

## The controls, FROZEN

- **`C1` — the builder's self-test.** At stage 1, `tools/v3_receipt.py --self-test` exits 0 and its
  last line is `v3_receipt: self-test OK`, with the counts `F5` records.
- **`C2` — own rule.** At stage 1, each of six scratch copies of the builder with one derivation
  wrong runs its self-test to exit 1, ending `v3_receipt: self-test FAILED`, with at least one
  `FAIL` line: the execution delta taken from `D` instead of `F`; the landing base taken from the
  second parent; the control-plane blobs in reverse order; no `withdrawal` reason when there are no
  execution commits; the seal blob hashed without git's object header; every attestation's commit
  taken from `F`.
- **`C3` — the command line.** At stage 1, `--status complete --d HEAD --f HEAD` prints
  `v3_receipt: refused (input:not-an-object-id)` and exits 2, and no argument prints the usage line
  and exits 2.
- **`C4` — the verifier untouched.** At every stage's commit, `tools/v3_verifier.py` has its `D`
  blob, `--corpus` reports `CORPUS  135 vector(s), exact and as expected`, and `--self-test`
  passes.
- **`C5` — the texts.** At stage 2, `AGENTS.md` is its `B` bytes followed by the frozen text
  exactly, carrying one `## §A.39 ` heading and no `§A.38`; `architecture.md` differs from its `B`
  bytes by the frozen sentence alone and no longer contains `is not operative`.

A control whose scratch copy fails for a reason other than the rule it tests is void, and its target
stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V39-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V39-1` | `BUILDER-INSTALLED` — stage 1 adds `tools/v3_receipt.py` and nothing else; `C1`–`C4` hold | `BUILDER-WRONG` |
| `V39-2` | `PILOT-RULE-INSTALLED` — stage 2 changes `AGENTS.md` and `architecture.md` as frozen and nothing else; `C4`, `C5` hold | `RULE-WRONG` |
| `V39-3` | `AUTHORITY-UNCHANGED` — `.github/workflows/verify.yml`, `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `tools/v3_verifier.py` and the corpus have their `B` blobs at `E`; neither `verification/receipts/` nor `verification/v3-seals/` exists; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and the 135-vector corpus | `AUTHORITY-CHANGED` — fails the round |
| `V39-4` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V39-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V39-1` | `BUILDER-INSTALLED`; builder blob `{{BLOB:builder}}` | strong | measured at `D` (`F5`) |
| `V39-2` | `PILOT-RULE-INSTALLED`; `AGENTS.md` blob `{{BLOB:agents}}`, `architecture.md` blob `{{BLOB:arch}}` | strong | measured at `D` (`F5`) |
| `V39-3` | `AUTHORITY-UNCHANGED` | strong | no job, gate, guard, verifier or corpus file is written, and the guard's reads of `AGENTS.md` are untouched (`F4`) |
| `V39-4` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V39-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V39-1` | one: `tools/v3_receipt.py` | `C1`–`C4` |
| 2 | `V39-2` | one: `AGENTS.md` and `architecture.md` | `C4`, `C5` |
| 3 | `V39-3`, `V39-4` | one: the result note; its commit is `E` | the closing checks, then the exact-head run |

Stage commits are pushed without waiting for continuous integration on them; the certification of
record is the exact-head run on `E`.

## The mutation budget

- **Added:** `tools/v3_receipt.py`;
  `verification/infrastructure/round-v3-9-operationalization/result.md`.
- **Modified:** `AGENTS.md` (the appended `§A.39`); `verification/infrastructure/v3/architecture.md`
  (the one frozen sentence).
- **Never written:** every other file under `tools/`, `.github/`, the guard and everything under
  `verification/lean/` and `verification/lean-mathlib/`,
  `verification/infrastructure/v3/conformance/`, `verification/seals/`,
  `verification/certificates/`, `verification/programmes/`, `verification/audits/`,
  `verification/ROADMAP.md`, `verification/README.md`, any other round's directory, `papers/` and
  `book/`. Neither `verification/receipts/` nor `verification/v3-seals/` is
  created.

## The result note

`result.md` records: each target's outcome against its prediction; the chronology from `B` to `E`;
each stage's blobs against their predictions, with the diff of every divergence; the outputs of `C1`
to `C5`, with the SHA-256 of each scratch script, none of which is landed; and every discrepancy.
The exact-head run on `E` is identified by the `E` certification record, since the note is part of
`E`.

## What no outcome of this round licenses

1. Any sentence that V3 is the default protocol, or that a V3 receipt is an authoritative record.
2. Any wiring of `tools/v3_receipt.py` or `tools/v3_verifier.py` into a gate or required check.
3. Any change to `V1` or `V2` state, to `§A.37`, or to another round's records.
4. Running a pilot: `§A.39` admits one only when the owner authorizes it in that round's own
   preregistration.

## Hazards

- **`H1` — one author.** The builder, the rule text and the controls have one author; the owner's
  review of the freeze and of the `E` record is the check on a shared misreading.
- **`H2` — shared functions.** The builder derives each digest with the verifier's own function, so
  a defect in that function would pass the self-test's reproduction. The digest functions are held
  independently by the corpus's literal-digest vectors (`s8-landed-*`, `s4-canonical-ex-*`), which
  this round does not touch.
- **`H3` — the guard reads `AGENTS.md`.** `F4` measured which phrases it reads; the exact-head run
  on `E` is the check that appending `§A.39` disturbs none.

## Files

### Files this round reads AND writes

`AGENTS.md` (the appended section); `verification/infrastructure/v3/architecture.md` (the one
sentence); `tools/v3_receipt.py` (new).

### Files this round reads and MUST NOT write

`tools/v3_verifier.py` and `verification/infrastructure/v3/conformance/`, which the builder and its
self-test read; `.github/workflows/verify.yml`, `tools/release_gate.py`,
`tools/certificate_verifier.py`, `tools/control_plane_base_check.py`, `tools/control_plane_lint.py`,
the guard, and the other `V3` round directories.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the objects the edits are applied to.

```control-plane-preconditions
d: 311f06ea174501587478024a09140297b56e089a
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: verification/infrastructure/v3/architecture.md db36dbd1ee4f779eff13525ffd3dc11d9041ab36
frozen-blob: tools/v3_verifier.py ccfbe813790e4855f408462449327f32e59d545b
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-9' -e 'v3-9' -e 'round-v3-9' -e 'V39-' -e 'v3_receipt' -e 'operationalization' $D", "expect": "empty"}
{"id": "d1-section-free", "scope": "D", "check": "git show $D:AGENTS.md | grep -F -e '§A.38' -e '§A.39'", "expect": "empty"}
{"id": "d1-builder-absent", "scope": "D", "check": "git ls-tree --name-only $D tools/v3_receipt.py", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts verification/v3-seals", "expect": "empty"}
# row 2: the vector inventory at D
{"id": "d2-corpus-135", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/infrastructure/v3/conformance/ | wc -l) -eq 135", "expect": "exit0"}
# row 3: provenance, D to B
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-9-operationalization/preregistration.md'", "expect": "empty"}
{"id": "db3-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py AGENTS.md", "expect": "exit0"}
# row 4: no execution object at B
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-9-operationalization | grep -v -x -F 'verification/infrastructure/round-v3-9-operationalization/preregistration.md'", "expect": "empty"}
{"id": "b4-builder-absent", "scope": "B", "check": "git ls-tree --name-only $REF tools/v3_receipt.py", "expect": "empty"}
{"id": "b4-agents-no-section", "scope": "B", "check": "git show $REF:AGENTS.md | grep -F -e '§A.39'", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts verification/v3-seals", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-9-operationalization/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. The execution pull request
may be opened after stage 1, held from merging. A stop outcome halts the round; the halt is recorded
in a result note with the outcomes reached, and nothing else of the execution lands. `V3-9` carries
no guard clause, manifest record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — a separate builder that reuses the verifier's functions.** The builder imports
  `tools/v3_verifier.py` for `S7`, `S8`, the control plane at `F` and `S4`'s standalone check,
  rather than restating them, so the two tools cannot drift apart on a digest; the verifier is not
  changed and does not import the builder. The declined options are a `--build-receipt` entry point
  in the verifier, which would put a builder inside the tool that judges its output, and an
  independent reimplementation, which would duplicate the specification's algorithms.
- **`R2` — the corpus is the builder's test data.** The self-test's evidence is that the builder
  reproduces the receipts the corpus's vectors commit and that the verifier rejects each corrupted
  field class; it adds no vector. The corpus is read, not written.
- **`R3` — `§A.39`, not `§A.38`** (`F2`). The owner's direction named a new `§A.38`; the number is
  already `GH-1`'s, and `V3-1` pointed at `§A.39` for this rule.
- **`R4` — `§A.37` unchanged.** `§A.39` is appended; nothing in `§A.37` is amended, and `§A.37`
  remains the default lifecycle and governs `V3-9`.
- **`R5` — the preamble alone.** Only the sentence that made the specification wholly inoperative
  changes; `S13` and every settlement stand.
- **`R6` — no continuous-integration step for the builder.** Its self-test runs in this round's
  controls and in the pilot that uses it; wiring it into a job is `V3-11`'s, with the rest of V3's
  gate wiring.
- **`R7` — no `V2` artifact for a pilot** (`F4`). A pilot's receipt is its protocol record; the
  guard and the release gate remain the safety net without a parallel certificate.
- **`R8` — no guard clause, certificate or attestation**, as for `V3-1` to `V3-8`.
- **`R9` — attestations name their subject.** A pull-request run tests a synthetic merge, so
  `§A.39` makes each `check-run` attestation a `workflow_dispatch` run whose `head_sha` is exactly
  `F` or `E`, taken while the branch is held there. This is host practice that keeps the
  attestation's description of its subject true; no verifier predicate reads it.
- **`R10` — the halt path.** `§A.39` closes a pilot that stops after `F` through `S12`: `W`, or
  the record commit when no execution commits exist, reconciliation, a halted receipt with `F`'s
  attestations alone, and `--verify-round Q` holding. The builder and the verifier already carry
  both halted shapes, so nothing but the rule's text is added for it.
