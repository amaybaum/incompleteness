# Verifier round V3-7 — V3 publication rehearsal on a protected sandbox: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. The sandbox
branch, the pilot round's commits and pull requests, and the result note are execution objects,
created only after the certified merge of this file.

> **The V3 lifecycle is run once, for real, on the host, against a target branch protected as
> `main` is, and never against `main`.** A pilot round goes from `F` through `E`, a reconciliation
> and a receipt commit; its target is then moved, its stale receipt commit is refused, it
> reconciles again, and its final receipt commit is published by a non-force update. The shadow
> verifier is then asked whether the round holds and whether the target's tip is its publication.

## The commit vocabulary this freeze uses, fixed first

`V3-7` is run under `AGENTS.md` §A.37 as it stands at `D`: this control plane, then one execution
pull request that carries its landing.

- `D` = `f557b1ccbdf9e441b33f5f70fa163823fc2ca10a`, the drafting snapshot: the certified head of
  `main` after `V3-6`'s landing (push run 36040631789, all six jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  object id until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before the
  merge.
- `E` — the sealed execution commit of this round: the last commit of the execution branch that
  branches from `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The pilot round's objects carry a `ᴾ` mark wherever they could be confused with this round's:
`Dᴾ`, `Fᴾ`, `Eᴾ`, `R₁ᴾ`, `Q₁ᴾ`, `R₂ᴾ`, `Q₂ᴾ`, in `verification/infrastructure/v3/architecture.md`'s
sense. `T₀` is the sandbox target's first tip and `T₂` the tip after it is moved.

## What `V3-7` is, and what it is not

`V3-7` is a **rehearsal round**. It creates a sandbox target branch, `v3-sandbox/main`, protected
by rulesets equivalent to `main`'s, and runs on it one V3 round, pilot `PILOT-SB1`, through every
state of the lifecycle and one publication retry. What it lands on `main` is its result note and
nothing else.

It is not:

1. **A publication to `main`.** No commit of the pilot, and no V3 receipt, reaches `main`. The first
   V3 publication to `main` is a later, separately preregistered transition pilot.
2. **A promotion.** V3 stays shadow-only; `V1` and `V2` stay authoritative; no gate, check, guard,
   verifier or workflow is written.
3. **A specification or implementation round.** `architecture.md` and `tools/v3_verifier.py` are
   not written. The pilot is judged by the tool as it stands at `B`.
4. **A host-configuration round.** The rulesets are the owner's; this round reads them, requires
   them, and records them.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-7`, `v3-7`, `round-v3-7`, `V37-`, `PILOT-SB1`, `v3-sandbox`, `v3/pilots` and
`publication-rehearsal` occur nowhere in the tree at `D`. Neither `verification/receipts/` nor
`verification/v3-seals/` exists at `D`.

### `F2` — `main`'s protection at `D`

At drafting time one active ruleset, `guardrail` (id 21725642), targets the default branch. It
forbids deletion and non-fast-forward updates, requires the checks `Lean kernel check`, `Mathlib
bridge` and `Numerical probes` in strict mode, and requires every change to arrive by a pull
request merged by merge, squash or rebase. Its only bypass is the repository admin role, in
`pull_request` mode. Under it a non-force update of `main` to a receipt commit — `S10`'s
publication — is refused for every actor, because the pull-request rule admits no direct push;
and every admitted merge method makes `main` reach the round through a commit other than `Q`,
which `S10` says is not a publication. The owner has directed the host change below, which lifts
the pull-request rule for direct pushes by the admin role alone and keeps every other rule without
bypass.

### `F3` — the pilot, rehearsed at `D` without the host

The pilot's frozen files, the reconciliations and receipts built by the scratch builder, and a
local stand-in for the sandbox advance were committed as local objects on `D` and never pushed.
The shadow tool at `D` then gave `VERDICT  HOLDS` for `--verify-round Q₂ᴾ` and for
`--verify-round Q₁ᴾ`; `HOLDS` for `--publication Q₂ᴾ Q₂ᴾ`; `FAILS s10:not-q-itself` for
`--publication T₂ Q₂ᴾ` and for `--publication Q₂ᴾ Q₁ᴾ`; and `FAILS` for `--publication` of a host
merge of `Q₂ᴾ` into `T₂`. `T₂` is not an ancestor of `Q₁ᴾ`, and it is an ancestor of `Q₂ᴾ`.

### `F4` — the tooling

At `D`, `tools/v3_verifier.py` has blob `21ea40977655d4a36c6e387b496ec5e353e9196b` and
`architecture.md` blob `12cff3f2c9b2cb7803ed1572c98bccba7590c707`. The workflow's `pull_request`
trigger covers every base branch, so the pilot's pull requests into `v3-sandbox/main` receive the
six jobs on each head; its `push` trigger covers `main` only.

## The host state the round requires, FROZEN

Before stage 1, and read again at the closing checks, the host's rules as the public rules endpoint
reports them for `main` and for `v3-sandbox/main` are exactly:

| ruleset | target | rules | bypass |
|---|---|---|---|
| `A` | the default branch | `deletion`; `non_fast_forward`; `required_status_checks`, strict, `do_not_enforce_on_create` false, the three checks | none |
| `B` | the default branch | `pull_request` with `guardrail`'s parameters | repository admin role, `always` |
| `A′` | `refs/heads/v3-sandbox/**` | as `A` | none |
| `B′` | `refs/heads/v3-sandbox/**` | as `B` | as `B` |

`guardrail` is disabled or deleted, and no other active ruleset applies to either branch. These
are host facts: the executor reads and records them, and no predicate reads them (`G8`). A host
state that differs is a stop outcome for `V37-0`.

## The pilot, FROZEN

The pilot round's id is `PILOT-SB1`. Its files are these, byte for byte.

`verification/infrastructure/v3/pilots/round-pilot-sb1/preregistration.md` (blob
`a97cf25aaf7d0e65fd80d0f15e7d81c69ad4873f`), the pilot's only control-plane file:

````text
{{PILOT_PREREG}}````

`verification/infrastructure/v3/pilots/PILOT-SB1-execution.md` (blob
`31461911b8623f5d55b92fb400765b6b6ec900ed`), the pilot's execution object:

````text
{{PILOT_EXEC}}````

`verification/infrastructure/v3/pilots/round-pilot-sb1/result.md` (blob
`3d0f9d7ae16392eebd78e2650cbf6f4ba3f7e0c3`), the pilot's result note, a record path:

````text
{{PILOT_RESULT}}````

`verification/infrastructure/v3/pilots/SANDBOX-ADVANCE.md` (blob
`0addb414e8c2e9f556c6ca884e81b34bbc928c5e`), the content of the pull request that moves the target:

````text
{{SANDBOX_ADVANCE}}````

The pilot's receipt, `verification/receipts/PILOT-SB1.json`, is built from the repository by a
scratch builder with the tool's own `S4`, `S7` and `S8` functions: complete, non-sealing, `d` =
`Dᴾ`, `candidates` empty, `resolved_paths` empty, and four attestations — the owner's designation
of `Fᴾ` and of `Eᴾ`, each recorded as the URL of the owner's comment on the pilot pull request, and
the exact-head workflow run on each, recorded as the run's URL. The builder refuses a receipt the
tool's `validate_receipt` rejects.

## The sequence, FROZEN

Every host operation below is authorized by this freeze and performed in this order, on the
sandbox only. The two owner designations are the owner's acts. No operation writes `main`.

| step | operation | observation required |
|---|---|---|
| `h0` | read the rules for `main` and `v3-sandbox/main` | the frozen host state |
| `h1` | create `v3-sandbox/main` at `B` by a non-force push; `T₀` = `B` = `Dᴾ` | the branch exists at `B` |
| `h2` | push `Fᴾ`, a single-parent child of `B` adding the pilot preregistration, to `v3-pilot/sb1`, and open the pilot pull request into `v3-sandbox/main` | the exact-head run on `Fᴾ`: six jobs green |
| `h3` | the owner designates `Fᴾ` in a comment on the pilot pull request | the comment |
| `h4` | push `Eᴾ`, a single-parent child of `Fᴾ` adding the execution object and the pilot's result note | the exact-head run on `Eᴾ`: six jobs green |
| `h5` | the owner designates `Eᴾ` | the comment |
| `h6` | push `R₁ᴾ` (parents `T₀`, `Eᴾ`) and `Q₁ᴾ` (its single-parent child adding the receipt) | the exact-head run on `Q₁ᴾ`: six jobs green; `--verify-round Q₁ᴾ` HOLDS |
| `h7` | open, from `T₀`, a pull request adding the advance file into `v3-sandbox/main`, and merge it by a merge commit once its run is green; `T₂` is that merge | the target's tip is `T₂` |
| `h8` | non-force push of `Q₁ᴾ` to `v3-sandbox/main` | refused; the tip is still `T₂` |
| `h9` | force push of `Q₁ᴾ` to `v3-sandbox/main` | refused by the host; the tip is still `T₂` |
| `h10` | push `R₂ᴾ` (parents `T₂`, `Q₁ᴾ`) and `Q₂ᴾ` (its single-parent child with the rebuilt receipt, naming `T₂`, `R₂ᴾ` and the reconciliations `R₁ᴾ`, `R₂ᴾ`) to `v3-pilot/sb1` | the exact-head run on `Q₂ᴾ`: six jobs green; `--verify-round Q₂ᴾ` HOLDS |
| `h11` | non-force push of `Q₂ᴾ` to `v3-sandbox/main` | accepted; the tip is `Q₂ᴾ` |
| `h12` | read the target and the pilot pull request | the tip is `Q₂ᴾ`; no commit on the target has `Q₂ᴾ` as a parent |

## The controls, FROZEN

- **`C1` — the pilot's objects.** `Fᴾ`, `Eᴾ`, `R₁ᴾ`, `Q₁ᴾ`, `R₂ᴾ` and `Q₂ᴾ` have the parents the
  sequence gives them; the pilot files have the frozen blobs at `Eᴾ`; `delta(Dᴾ, Fᴾ)` is the pilot
  preregistration alone; `delta(Fᴾ, Eᴾ)` is the execution object and the result note;
  `delta(R₁ᴾ, Q₁ᴾ)` and `delta(R₂ᴾ, Q₂ᴾ)` are the receipt path alone.
- **`C2` — the verifier.** From a checkout holding the objects, the tool at `B` gives
  `VERDICT  HOLDS` for `--verify-round Q₂ᴾ` and for `--verify-round Q₁ᴾ`; `HOLDS` for
  `--publication <tip> Q₂ᴾ`, with the tip read from the host at `h12`; and `FAILS
  s10:not-q-itself` for `--publication T₂ Q₂ᴾ` and for `--publication <tip> Q₁ᴾ`.
- **`C3` — the refusals.** At `h8` and `h9` the host refuses the update, and the tip read after each
  is `T₂`.
- **`C4` — the publication.** At `h11` the host accepts a non-force update from `T₂` to `Q₂ᴾ`; at
  `h12` the tip is `Q₂ᴾ`.
- **`C5` — the checks on exactly each subject.** The exact-head runs on `Fᴾ`, `Eᴾ`, `Q₁ᴾ` and
  `Q₂ᴾ` are green on all six jobs, and on `Q₂ᴾ` the guard gives 105 PASS and 0 FAIL, the release
  gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and 133-vector corpus.

A control whose observation cannot be made — a run that does not exist, an endpoint that does not
answer — is void, and its target stops.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V37-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B`; the host state is the frozen one (`h0`) | `BASE-BROKEN` |
| `V37-1` | `PILOT-FROZEN` — `h1` to `h3`, with `C5` on `Fᴾ` | `PILOT-NOT-FROZEN` |
| `V37-2` | `PILOT-CERTIFIED` — `h4` and `h5`, with `C5` on `Eᴾ` | `PILOT-NOT-CERTIFIED` |
| `V37-3` | `FIRST-RECEIPT` — `h6`, with `C5` on `Q₁ᴾ` and `--verify-round Q₁ᴾ` HOLDS | `FIRST-RECEIPT-FAILS` |
| `V37-4` | `STALE-REFUSED` — `h7` to `h9`, with `C3` | `STALE-ACCEPTED` — fails the round |
| `V37-5` | `RETRY-PUBLISHED` — `h10` to `h12`, with `C4` and `C5` on `Q₂ᴾ` | `RETRY-FAILS` |
| `V37-6` | `ROUND-VERIFIED` — `C1` and `C2` | `ROUND-NOT-VERIFIED` |
| `V37-7` | `MAIN-UNTOUCHED` — no pilot commit is reachable from `main` at `E`; `main`'s rules are the frozen ones at the closing read; the exact-head run on `E` gives the guard 105 PASS and 0 FAIL with `D`'s verdict map, the release gate 19 of 19 with `V2` authoritative OK, and the shadow job its self-test and 133-vector corpus | `MAIN-DISTURBED` — fails the round |
| `V37-8` | `SCOPE-HELD` — `git diff --no-renames --name-status B E` is exactly the mutation budget | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V37-0` | `BASE-HOLDS` | moderate | the rows are strong; the host state depends on the owner's change being made as frozen |
| `V37-1` | `PILOT-FROZEN` | strong | `F3`; the pilot's files are inert to every job |
| `V37-2` | `PILOT-CERTIFIED` | strong | as `V37-1` |
| `V37-3` | `FIRST-RECEIPT` | strong | `F3` |
| `V37-4` | `STALE-REFUSED` | strong | a non-force update that is not a fast-forward is refused by git and by `A′`'s `non_fast_forward` rule, which has no bypass |
| `V37-5` | `RETRY-PUBLISHED` | moderate | `F3` for the objects; the host's acceptance of a direct push by the admin role under `B′`'s bypass, with `A′`'s checks satisfied by the pull-request runs on exactly `Q₂ᴾ`, is the thing this round exists to observe |
| `V37-6` | `ROUND-VERIFIED` | strong | `F3` |
| `V37-7` | `MAIN-UNTOUCHED` | strong | no step writes `main` |
| `V37-8` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome. It is HALTED at
the first stop outcome, and the targets not reached are recorded as such. A halt after `h1` leaves
`v3-sandbox/main` and the pilot's pull requests as they stand; nothing on `main` changes.

## The order is part of the contract

| stage | targets | commit on the execution branch | checkpoint |
|---|---|---|---|
| 0 | `V37-0` | none | branch from `B`; blob check; rows at `B`; `h0` |
| 1 | `V37-1` to `V37-6` | none | `h1` to `h12` in order, each observation recorded as made |
| 2 | `V37-7`, `V37-8` | one: the result note; its commit is `E` | `C1`, `C2`, the closing host read, scope, then the exact-head run on `E` |

## The mutation budget

- **Added:** `verification/infrastructure/round-v3-7-publication-rehearsal/result.md`.
- **Nothing else** is modified, added or deleted on the execution branch. The pilot's files, its
  receipt and the advance file exist only in the pilot's and the sandbox's commits, which are not
  merged into `main`.
- **Never written, on `main` or by this round's execution branch:** `.github/`, `tools/`,
  `AGENTS.md`, the guard, `verification/infrastructure/v3/`, `verification/seals/`,
  `verification/certificates/`, any other round's directory, `papers/` and `book/`; no
  `verification/receipts/` or `verification/v3-seals/` directory is created on `main`.

## The result note

`result.md` records: each target's outcome against its prediction; the host state read at `h0` and
at the close; every object id of the sequence (`T₀`, `Fᴾ`, `Eᴾ`, `R₁ᴾ`, `Q₁ᴾ`, `T₂`, `R₂ᴾ`, `Q₂ᴾ`),
with the pull requests, the owner's designation comments and the exact-head runs; the host's
response to each of `h8`, `h9` and `h11` as the push reported it; the outputs of `C1` and `C2`,
with the SHA-256 of each scratch script, none of which is landed; and every discrepancy. The
exact-head run on `E` is identified by the `E` certification record, since the note is part of `E`.

## What no outcome of this round licenses

1. Any publication to `main`, or any claim that `main`'s protection admits one, beyond the host
   state read here.
2. Any sentence that V3 is operative, or any wiring of it into a gate or required check.
3. Treating the pilot's receipt, or anything on `v3-sandbox/main`, as state of `main`.
4. Any change to `V1` or `V2` state, to `architecture.md`, or to another round's records.

## Hazards

- **`H1` — the host is part of the experiment.** The rulesets are owner-set host state. If they are
  not as frozen, the round stops at `V37-0` rather than rehearse against a different host.
- **`H2` — the admin bypass is the owner's authority.** The executor pushes through the owner's
  credentials, which carry `B′`'s bypass. This freeze authorizes the sandbox pushes of the sequence
  and no other direct push; every direct push to `main` remains an owner-directed operation.
- **`H3` — sandbox objects persist only while referenced.** The pilot's commits are reachable from
  `v3-sandbox/main` and `v3-pilot/sb1`. The result note records every object id; the branches are
  kept until the transition pilot has run, so the evidence stays re-checkable.
- **`H4` — one author.** The builder, the pilot and the reading of the host's responses have one
  author; the owner's review of the `E` record is the check on them.

## Files

### Files this round reads AND writes

`verification/infrastructure/round-v3-7-publication-rehearsal/result.md` only, on `main`'s side.

### Files this round reads and MUST NOT write

`tools/v3_verifier.py`, `verification/infrastructure/v3/architecture.md`, the workflow, the guard,
`AGENTS.md`, and every other file.

## Preconditions

Row `db3-only-this-file` requires that nothing but this file lie between `D` and `B`; with the
frozen blobs it fixes the tool that judges the pilot.

```control-plane-preconditions
d: f557b1ccbdf9e441b33f5f70fa163823fc2ca10a
frozen-blob: tools/v3_verifier.py 21ea40977655d4a36c6e387b496ec5e353e9196b
frozen-blob: verification/infrastructure/v3/architecture.md 12cff3f2c9b2cb7803ed1572c98bccba7590c707
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-7' -e 'v3-7' -e 'round-v3-7' -e 'V37-' -e 'PILOT-SB1' -e 'v3-sandbox' -e 'v3/pilots' -e 'publication-rehearsal' $D", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
{"id": "d1-v3-seals-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/v3-seals", "expect": "empty"}
# row 2: provenance, D to B
{"id": "db2-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db2-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-7-publication-rehearsal/preregistration.md'", "expect": "empty"}
{"id": "db2-v3-unchanged", "scope": "D->B", "check": "git diff --quiet $D $REF -- verification/infrastructure/v3/ tools/v3_verifier.py .github/", "expect": "exit0"}
# row 3: no execution object at B
{"id": "b3-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-7-publication-rehearsal | grep -v -x -F 'verification/infrastructure/round-v3-7-publication-rehearsal/preregistration.md'", "expect": "empty"}
{"id": "b3-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
{"id": "b3-no-pilots", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/infrastructure/v3/pilots", "expect": "empty"}
# row 4: this control plane at its path
{"id": "b4-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-7-publication-rehearsal/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`. Full continuous integration passes on `L`
before it merges, and the push run on `main` is green before any later round's landing is built.
The sandbox branch, the pilot branch and the pilot's pull requests are not part of the landing.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`, then
`h0`. It never absorbs later `main` before `E`; no rebase, amend or force-push of the execution
branch. The pilot branch is pushed only by fast-forward. A stop outcome halts the round; the halt
is recorded in a result note with the outcomes reached, and nothing else of the execution lands.
`V3-7` carries no guard clause, manifest record or round certificate.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — sandbox only.** The pilot never reaches `main`: this round proves the mechanism, and a
  separate transition pilot uses it on `main`, so that `main` never moves outside this round's own
  `B` → `E` → `L` while it runs.
- **`R2` — the host state frozen and read, not written.** The rulesets are the owner's acts; the
  round requires them at `h0` and records them twice. The declined option, rehearsing on an
  unprotected branch, would prove the topology and not the protected-host path.
- **`R3` — the retry keeps `Q₁ᴾ`.** `R₂ᴾ`'s second parent is `Q₁ᴾ`, which remains in the round as a
  superseded receipt commit (`S10` 1, `K4`), so the retry exercises the superseded-receipt rule.
  The declined option rebuilds from `Eᴾ` and leaves `Q₁ᴾ` off the chain (`G11`), which the corpus
  already exercises.
- **`R4` — the force push attempted.** `h9` asks the host to refuse a forced update of the
  protected target, which is what distinguishes host protection from the client's own refusal at
  `h8`. It is attempted on the sandbox only.
- **`R5` — a non-sealing pilot.** The seal record adds no host mechanics; the corpus carries it.
- **`R6` — sandbox operations pre-authorized.** The owner's approval of this freeze directs the
  sandbox pushes and the advance merge of the sequence; the designations of `Fᴾ` and `Eᴾ` remain
  the owner's acts, as `S5` requires of a human attestation.
- **`R7` — six checks, not three.** The host requires three; the round requires all six green on
  each pilot subject, as the transition pilot will on `main`.
