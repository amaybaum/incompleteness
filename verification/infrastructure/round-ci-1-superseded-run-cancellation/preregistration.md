# Infrastructure round CI-1 — superseded pull-request runs are cancelled: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The changed
workflow and the result note are execution objects, created only after the certified merge of this
file.

> **A push to a pull request's head cancels the run it supersedes; a run on `main` is never
> cancelled.** Nothing else about continuous integration changes.

## The commit vocabulary this freeze uses, fixed first

`CI-1` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `f557b1ccbdf9e441b33f5f70fa163823fc2ca10a`, the drafting snapshot: the certified head of
  `main` after `V3-6`'s landing (push run 36040631789, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

## What `CI-1` is, and what it is not

`CI-1` adds one top-level `concurrency` block to `.github/workflows/verify.yml`. Its effect is that
a new push to a pull request's head cancels the workflow run still in progress on the head it
replaces, and that no other run is ever cancelled. Every round's intermediate stage commits are
pushed without waiting for their runs, and only the exact-head run on `E` or `L` is evidence; the
superseded runs occupy runners and delay the run that counts.

It is not:

1. **A change to any job.** No job, step, trigger, path filter, runner, cache or required check
   changes. The file's parsed content outside the new key is unchanged.
2. **Evidence reuse.** No run is skipped because an earlier run saw the same tree; every head still
   receives its own run unless a later push to the same pull request supersedes it.
3. **A change to authority.** `V1` and `V2` stay authoritative, V3 stays shadow-only, and no
   verifier, gate step, guard clause or seal state is written.

## Measurements at `D` that shape the round

### `F1` — name freedom and the workflow at `D`

`CI-1`, `ci-1`, `round-ci-1`, `CI1-` and `superseded-run` occur nowhere in the tree at `D`.
`.github/workflows/verify.yml` has blob `d14d19389f452b39820206d449146ac424b7706c` at `D` and
carries no `concurrency` key. Its triggers are `pull_request` (every branch), `push` to `main`, and
`workflow_dispatch`, and its six jobs are `Lean kernel check`, `Mathlib bridge`, `Numerical
probes`, `Control-plane base check`, `Certificate verifier` and `V3 shadow verifier`.

### `F2` — what reads the workflow

At `D` two guard clauses and two tools read the workflow's text, each for the presence of a string
the change does not touch: the guard's `R7-MIN` (`repertoire_lie`) and `R7-CV1` (the `Certificate
verifier` job in shadow mode and never authoritative), `tools/ci_gate_presence_test.py` (the release
gate invoked in a `run:` command), and `tools/coverage_check.py`. No live check pins the workflow's
blob. The blob appears in earlier rounds' preregistrations only as a drafting-time measurement or
as a frozen blob of a merged control plane, which the base check treats as historical.

### `F3` — the change, measured at `D` in scratch

The frozen block below, inserted between the `on:` mapping and `jobs:` of the workflow at `D`,
gives a file whose YAML parse equals the parse at `D` plus one key, `concurrency`, and whose blob
is `e097d367149f3bbe3716d320d6e36f624dee7787`.

## The change, FROZEN as text

The execution inserts the following lines, byte for byte, into `.github/workflows/verify.yml`
immediately before the line `jobs:`, after the blank line that ends the `on:` mapping, and changes
nothing else in the file:

```yaml
# Superseded pull-request runs are cancelled, and no other run is. Every pull_request run of one
# pull request shares one group, so a push to its head cancels the run still in progress on the
# head it replaces. Every other run -- a push to main, a workflow_dispatch -- is alone in a group
# named by its own run id and is never cancelled, so the push run that certifies a commit on main
# always completes.
concurrency:
  group: ${{ github.workflow }}-${{ github.event_name == 'pull_request' && format('pr-{0}', github.event.pull_request.number) || format('run-{0}', github.run_id) }}
  cancel-in-progress: ${{ github.event_name == 'pull_request' }}

```

**Semantics.** For a `pull_request` run the group is the workflow's name and the pull request's
number, and `cancel-in-progress` is true, so a new run in that group cancels the run in progress or
pending in it. For every other event — `push` to `main` and `workflow_dispatch` — the group is the
workflow's name and the run's own id, which no other run shares, and `cancel-in-progress` is false,
so the run is neither cancelled nor held behind another.

## The controls, FROZEN

- **`C1` — the text.** At stage 1 the workflow's blob is `e097d367`, `git diff B` of the file adds
  exactly the frozen lines and removes none, and the file's YAML parse equals its parse at `B` plus
  the one key `concurrency`, whose value is the frozen group and `cancel-in-progress` expressions.
- **`C2` — the readers.** At stage 1 `tools/ci_gate_presence_test.py` passes, and the strings the
  guard's `R7-MIN` and `R7-CV1` read from the workflow are present exactly as at `B`.
- **`C3` — a superseded pull-request run is cancelled.** The execution pull request is opened on
  stage 1, and `E` is pushed to it while the stage-1 run is in progress. The pull-request run on
  stage 1 then concludes `cancelled`, and the pull-request run on `E` runs to completion.
- **`C4` — other runs are never cancelled.** While the stage-1 pull-request run is in progress, two
  `workflow_dispatch` runs are started on the execution branch at stage 1, one after the other. Both
  run to completion with no job `cancelled`, although each overlaps the other, the stage-1
  pull-request run and the push of `E`.
- **`C5` — the push to `main`.** After the landing merges, the push run on the landed `main` runs
  to completion with all six jobs green. This is the landed-state certification; it is recorded
  after the round and is not a target.

`C3` and `C4` are observations of runs that `E`'s own push triggers or overlaps, so they are
recorded in the `E` certification record on the execution pull request rather than in the result
note, as the exact-head run on `E` is.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `CI1-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and the frozen blob hold at `B` | `BASE-BROKEN` |
| `CI1-1` | `CONCURRENCY-INSTALLED` — stage 1 changes only the workflow, by the frozen lines; `C1` and `C2` hold | `CONCURRENCY-WRONG` |
| `CI1-2` | `SUPERSEDED-RUN-CANCELLED` — `C3` holds | `SUPERSEDED-RUN-KEPT` |
| `CI1-3` | `OTHER-RUNS-KEPT` — `C4` holds | `OTHER-RUN-CANCELLED` — fails the round |
| `CI1-4` | `AUTHORITY-UNCHANGED` — the exact-head run on `E` is green on all six jobs, with the guard at 105 PASS and 0 FAIL and `D`'s verdict map, the release gate at 19 of 19 with `V2` authoritative OK, and the shadow job's self-test, 133-vector corpus and 126 projection cells | `AUTHORITY-DISTURBED` — fails the round |
| `CI1-5` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `CI1-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `CI1-1` | `CONCURRENCY-INSTALLED`; workflow blob `e097d367` | strong | measured at `D` (`F3`) |
| `CI1-2` | `SUPERSEDED-RUN-CANCELLED` | strong | the documented semantics of `concurrency` with `cancel-in-progress` |
| `CI1-3` | `OTHER-RUNS-KEPT` | strong | each non-pull-request run is alone in its group |
| `CI1-4` | `AUTHORITY-UNCHANGED` | strong | no job, gate, guard or verifier changes (`F2`) |
| `CI1-5` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `CI1-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `CI1-1` | one: the frozen lines in the workflow | `C1`, `C2`; push; open the execution pull request; start the two dispatch runs |
| 2 | `CI1-2` to `CI1-5` | one: the result note; its commit is `E`, pushed while the stage-1 pull-request run is in progress | `C3` and `C4` from the runs, then the exact-head run on `E` |

## The mutation budget

- **Modified:** `.github/workflows/verify.yml` (the frozen lines, inserted).
- **Added:** `verification/infrastructure/round-ci-1-superseded-run-cancellation/result.md`.
- **Never written:** every other file, and in particular every job of the workflow, `tools/`,
  `AGENTS.md`, the guard and everything under `verification/lean/` and
  `verification/lean-mathlib/`, `verification/seals/`, `verification/certificates/`,
  `verification/infrastructure/v3/`, any other round's directory, `papers/` and `book/`. No
  `verification/receipts/` or `verification/v3-seals/` directory is created.

## The result note

`result.md` records: each target's outcome against its prediction, `CI1-2` to `CI1-4` as
established by the runs the `E` certification record identifies; the chronology from `B` to `E`;
the stage-1 workflow blob; the outputs of `C1` and `C2`; the run ids of the stage-1 pull-request run
and the two dispatch runs as started; and every discrepancy.

## What no outcome of this round licenses

1. Skipping, reusing or trusting any run's result for a head other than the one it ran on.
2. Any change to a required check, a job, or the evidence an `E`, `L` or `B` certification needs.
3. Any change to `V1`, `V2` or V3 authority.

## Hazards

- **`H1` — a certification run superseded.** Under the change, a push to a pull request cancels
  the run on the head it replaces. The run on `E` is therefore the certification of record only if
  nothing is pushed to the pull request before it completes; §A.37 already builds `L` only after
  `E` is designated on its completed run, and the same order holds from `L` to its merge.
- **`H2` — the dispatch fallback.** §A.37's `workflow_dispatch` certification of an exact head is a
  non-pull-request run and is never cancelled by the change (`C4`).
- **`H3` — one author.** The change, the controls and their reading have one author; the owner's
  review of the `E` record is the check on the observations.

## Files

### Files this round reads AND writes

`.github/workflows/verify.yml` (the frozen lines).

### Files this round reads and MUST NOT write

Everything else, in particular `tools/ci_gate_presence_test.py`, `tools/coverage_check.py`, the
guard and `AGENTS.md`.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blob it fixes the workflow the lines are inserted into.

```control-plane-preconditions
d: f557b1ccbdf9e441b33f5f70fa163823fc2ca10a
frozen-blob: .github/workflows/verify.yml d14d19389f452b39820206d449146ac424b7706c
# row 1: name freedom, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'CI-1' -e 'ci-1' -e 'round-ci-1' -e 'CI1-' -e 'superseded-run' $D", "expect": "empty"}
# row 2: provenance, D to B
{"id": "db2-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db2-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-ci-1-superseded-run-cancellation/preregistration.md'", "expect": "empty"}
{"id": "db2-github-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- .github/", "expect": "exit0"}
# row 3: no execution object at B
{"id": "b3-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-ci-1-superseded-run-cancellation | grep -v -x -F 'verification/infrastructure/round-ci-1-superseded-run-cancellation/preregistration.md'", "expect": "empty"}
# row 4: this control plane at its path
{"id": "b4-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-ci-1-superseded-run-cancellation/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`. Full continuous integration passes on `L`
before it merges, and the push run on `main` is green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. A stop outcome halts the
round; the halt is recorded in a result note with the outcomes reached, and nothing else of the
execution lands. `CI-1` carries no guard clause, manifest record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — text frozen exactly.** The change is one block, so the freeze fixes its bytes rather
  than a site and a predicted replacement; any other text is a stop for `CI1-1`.
- **`R2` — one group per pull request, keyed by its number.** The number is fixed for the pull
  request's life, whatever its head branch is called. The declined option, keying by head ref,
  would let two pull requests from one branch name cancel each other.
- **`R3` — every other run alone in its own group.** GitHub's `concurrency` is set per workflow and
  cannot be switched off per event; a group named by the run's own id is the form in which a run
  shares its group with nothing and is therefore neither cancelled nor queued. The declined option,
  one shared group for `main` without cancellation, would queue each push run behind the previous
  one.
- **`R4` — the workflow level.** The block governs the whole run, so a superseded run's six jobs
  are cancelled together. The declined option, per-job blocks, repeats the rule six times for no
  difference in effect.
- **`R5` — observations in the `E` record.** `C3` and `C4` concern runs that exist only once `E`
  is pushed, so they are read from the runs and recorded where the exact-head run is.
