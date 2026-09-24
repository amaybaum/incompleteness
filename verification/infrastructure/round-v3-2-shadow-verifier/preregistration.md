# Verifier round V3-2 — the V3 shadow verifier: scope, comparison, failure semantics and the promotion boundary: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. No shadow
verifier, conformance vector, census, workflow job or result exists at the time it is written; each
is an execution object and is created only after the certified merge of this file.

> **Presence is not authority.** The V3 shadow verifier runs, reports and is compared. It decides
> nothing. `V1` and `V2` remain the only mechanisms whose verdicts can accept or reject a build, a
> pull request or a round.

Everything below is subordinate to that sentence. `V3-2` must not produce a state in which a V3
verdict changes whether anything is accepted. A later reading that the certification semantics
changed merely because the shadow code is in the tree is excluded here, before the code exists.

## The commit vocabulary this freeze uses, fixed first

`V3-2` is run under `AGENTS.md` §A.37 as it stands at `D`: two pull requests, this control plane and
then one execution pull request that carries its landing. V3 is not operative, and this round does
not make it operative.

- `D` — the drafting snapshot: `9c480626ba0b3d6242bb99783356afefaf4f4bcf`, the certified head of
  `main` after `V3-1`'s landing (push run 35929458646, all five jobs green). Every measurement in
  this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  SHA until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before
  the merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge: first parent current green `main`, second parent exactly `E`.

The letters `F`, `W`, `Λ`, `LB` and `Q` keep the meanings `verification/infrastructure/v3/architecture.md`
gives them. They name objects of the synthetic V3 rounds the conformance corpus builds, and never
an object of this round.

**Protocol numbering.** Protocol 1 is the guard (`V1`), protocol 2 the round certificate (`V2`,
installed by `CV-1`), protocol 3 the architecture `V3-1` specified (`V3`). `V3-2` is the second round
of the V3 sequence. The sequence `V3-1` named — shadow implementation, migration census,
authoritative cutover, retirement of `V1` and `V2` — is kept: this round is the first of those, and
it constrains the later ones only through the promotion boundary below.

## What `V3-2` is, and what it is not

`V3-2` is a **shadow implementation round**. It delivers one standard-library verifier that
implements the V3 specification, a conformance corpus that exercises it, a comparison census against
`V2` on the questions both can answer, a non-gating workflow job that runs it, and a result note.

It is not:

1. **A promotion.** No V3 verdict gates anything, at any point of this round or after it, until a
   later round that states prospectively that it promotes (the promotion boundary, below).
2. **A migration.** No historical round is translated into a V3 receipt, no V3 status is assigned
   to any historical round, and no `V1` or `V2` state (guard clause, certificate, attestation row,
   live policy, relocation, conformance vector, seal record) is created, changed or removed. The
   comparison census reads `V2`'s rows as data; it makes no claim about any historical round's
   validity under any protocol.
3. **A specification round.** `verification/infrastructure/v3/architecture.md` is read and never
   written. A gap or inconsistency the implementation finds in it is recorded (`V32-7`), and the
   shadow carries a named reading; the specification is not amended here.
4. **A retirement.** `CV-2`'s unfinished retirement of `V1` stays as it is.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-2`, `v3-2`, `round-v3-2`, `V32-`, `v3_verifier`, `V3 shadow`, `v3-shadow`,
`verification/infrastructure/v3/conformance`, `projection census` and `v3-projection` occur nowhere
in the tree at `D`. The bare token `V32` occurs in one text file, as a matrix name in
`verification/lean/bohr_frequency_probe.py`, and inside compiled PDF files; neither is this round's.
`verification/receipts/` does not exist at `D`, and neither does `tools/v3_verifier.py`.

### `F2` — the `V2` data the comparison can read at `D`

`verification/certificates/attestations/` holds **36** rows at `D`: **30** of kind `landed`, each with
`base`, `sealed_head`, `tree` and `landing`; and **6** of kind `base-only` (`ABR`, `CLG`, `RBR`, `SI1`,
`SI2`, `TSG`), each with `base` alone. Sixteen certificates are content-only and have no row; they
carry no topology and are outside the comparison.

`tools/certificate_verifier.py` decides each landed row by `derive_landed` and each base-only row by
`derive_base_only`, and prints one `ROW` line per row with its codes. Its visibility targets are the
reachable history of `HEAD` on a push and, on a pull request, the event payload's
`pull_request.head.sha` with the live `refs/remotes/origin/<base ref>`, recovered over the network
when absent (`V3-1`'s `F2`, mechanisms `M1`, `M2` and `M3`).

### `F3` — the comparison measured at `D`, in scratch

Each of the 30 landed rows was evaluated at `D` by a throwaway script, commit-locally, on five
predicates: `tree(sealed_head)` equals the recorded tree; the landing has exactly two parents and
the second is `sealed_head`; every commit of `rev-list sealed_head ^base` descends from `base` (the
strengthened ancestry `V2` asks); `rev-list sealed_head ^base` is linear from `base`; and `base` lies
on the first-parent chain of the landing's first parent. **All 30 rows hold all five.**

`V2` was run in shadow mode in a scratch clone of `D` whose `origin` points at a path that does not
exist, so that no recovery can fetch, under four states of the surrounding repository and host
context:

| | state | `V2` result at `D` |
|---|---|---|
| `P0` | push mode, `HEAD` detached at `D` | 36 rows, all PASS |
| `P1` | as `P0` after every ref under `refs/heads/` and `refs/remotes/` is deleted and a `dev` and a `junk` branch are created | 36 rows, all PASS |
| `P2` | pull-request event, `head.sha` = `D`, base ref `main`, no `refs/remotes/origin/main` | fail-closed before any row: `visibility:base-ref-unresolvable` |
| `P3` | pull-request event, `head.sha` = `X` and `refs/remotes/origin/main` = `X`, where `X` = `e0be0ab6dca7b6661a008a9f5e1f3a29ea736003`, the first parent of `CGR`'s landing | 30 rows PASS; `CGR`, `CV1`, `GR1`, `GR2`, `NLV` and `PFR` FAIL with `landing:zero-candidates` |

The same repository objects give different `V2` verdicts under `P2` and `P3` because the verdict
depends on host context. The comparison below is built to separate that dependence from a defect.

### `F4` — known gaps in the specification at `D`

Reading `architecture.md` against the task of implementing it, four places leave a verifier without
a mechanical answer. They are listed here so that the shadow's reading of each is fixed before any
code exists, rather than chosen by the implementation to fit its results.

| | gap | where |
|---|---|---|
| `K1` | the round id, `kind` and the record directory have subject `F`, but no declaration form at `F` is given | `S4` field table; "The round's record directory" |
| `K2` | "exactly one fenced block" with info string `v3-governed-paths` is required of "the control plane", which may be several files (the preregistration and its amendments); which file, or whether across all of them, is not said | `S7` Declaration |
| `K3` | `S9` requires `D` on `LB`'s first-parent chain; nothing is required of the first parent of a reconciliation other than the last | `S9` |
| `K4` | the receipt commits between reconciliations (a superseded `Q` after a failed publication) have no stated delta rule of their own | `S10`; lifecycle T6 |

### `F5` — tooling and the workflow at `D`

Python 3.11 and git 2.43 in the drafting environment; the workflow's jobs pin Python 3.11 and install
only `numpy` and `scipy`. The repository's object format is `sha1`. The workflow has **no path
filters** and five jobs: `Lean kernel check`, `Mathlib bridge`, `Numerical probes`,
`Control-plane base check` and `Certificate verifier`. Its header says that three verification jobs
are required status checks on `main`, and its comment on the `Certificate verifier` job says that
job is not one of them. The required-check set itself is host state and is not read here. `tools/release_gate.py` runs nineteen steps, among them `V2` in authoritative
mode; the guard's `R7-CV1` reads the live workflow text only to require that the `Certificate
verifier` job runs `V2` in shadow mode and never authoritatively.

## The shadow's provisional readings of `F4`, FROZEN

These readings bind the shadow and nothing else. They are not amendments to the specification and
confer no status on it. Each is reported by the shadow at every run and in the result note, and the
promotion boundary requires that a specification round settle each one, adopting or replacing it,
before promotion.

- **`K1` reading.** The preregistration at `F` carries exactly one fenced block with info string
  `v3-round`, of three lines `round <id>`, `kind <sealing|non-sealing>` and
  `record-directory <path>/`, each exactly once, in any order. The round id matches
  `[A-Z0-9]+(-[A-Z0-9]+)*`; the record directory is a path that `S7` would accept and ends in `/`.
  The receipt's `round` and `kind` must equal the block's.
- **`K2` reading.** Over all control-plane files at `F` taken together, there is exactly one
  `v3-governed-paths` block and exactly one `v3-round` block. An amendment that repeats either makes
  the control plane invalid.
- **`K3` reading.** For every reconciliation `Rᵢ`, `D` lies on the first-parent chain of `Rᵢ`'s first
  parent; and for `i > 1`, `Rᵢ₋₁`'s first parent lies on the first-parent chain of `Rᵢ`'s first
  parent.
- **`K4` reading.** Every receipt commit, superseded or final, is a single-parent child of the
  reconciliation before it, and its delta from that reconciliation is exactly the receipt path plus,
  for a sealing receipt, the seal records it names (`S10`'s rule for `Q`, applied to each).

## The execution objects, FROZEN as a specification

- **`tools/v3_verifier.py`** — the shadow verifier. Standard library only. It implements, as
  `architecture.md` states them, with the `F4` readings above:
  - `S7`: parsing, validation, canonical bytes, digest, and authorization of a delta record;
  - `S8`: parsing `git diff-tree -r --raw --no-renames --no-abbrev -z`, validation, canonical bytes
    and digest;
  - `S4`: validation of a receipt, standalone (schema, presence rules, reason codes, attestation
    minimums) and against the repository (every recorded subject exists and its recorded tree,
    blob, delta and ancestry agree);
  - the lifecycle predicates T1, T3, T5, T6 and T7, evaluated from a receipt commit `Q` and the
    commits its receipt names; and the publication question of `S10` (whether a given commit is `Q`
    itself);
  - the **projection**: for a named subject commit and each `V2` attestation row read from that
    commit, the comparison axes below, computed commit-locally.

  It has exactly these entry points: `--self-test`; `--corpus [DIR]`; `--verify-round <Q>`;
  `--publication <T> <Q>`; `--project <subject>`; and `--mode shadow --subject <commit>`, which runs
  the corpus and the projection and reports. **It has no authoritative mode**, and no argument or
  environment variable changes its exit status on a verdict about a round or a row. Every commit
  argument must be a full-length lowercase hexadecimal object id; a ref name, `HEAD` or an
  abbreviated id is refused before any repository read. Locating a commit is the caller's business
  (`S1`).
- **`verification/infrastructure/v3/conformance/`** — the conformance corpus: one JSON file per
  vector, each with an `id`, the settlements it exercises, a recipe (a byte input, a synthetic
  repository built in a temporary directory from a restricted command vocabulary, or named commits
  of this repository), the entry point it calls, and its expected verdict with, for a failure, the
  reason-code family it must fail with (`s4:`, `s7:`, `s8:`, `s3:`, `s9:`, `s10:`, `s12:`, `t1:`,
  `input:`). The minimum coverage is frozen below.
- **`verification/infrastructure/round-v3-2-shadow-verifier/census.json`** — the comparison census
  and the perturbation control, machine-readable (the evidence, below).
- **`.github/workflows/verify.yml`** — one added job, `V3 shadow verifier`, and nothing else changed:
  checkout with `fetch-depth: 0`, Python 3.11, then `--self-test`, `--corpus`, and
  `--mode shadow --subject "$(git rev-parse HEAD)"`. The job is not a required check, is not invoked
  by `tools/release_gate.py`, and no other job depends on it.
- **`verification/README.md`** — one added paragraph, next to the existing `V2` paragraph, stating
  that `tools/v3_verifier.py` is the V3 shadow verifier installed by `V3-2`, that it gates nothing,
  that `V1` and `V2` remain authoritative, and where its corpus and this round's record are. No
  other line changes.
- **`verification/infrastructure/round-v3-2-shadow-verifier/result.md`** — the result note.

### The conformance corpus, minimum coverage, FROZEN

The expected values in rows 1 to 4 are taken from `architecture.md` and not from the shadow's own
output. They were computed at `V3-1` by a model the shadow does not share code with, so a shadow that
reproduces them is controlled by something other than itself.

| | settlement | vectors | expected |
|---|---|---|---|
| 1 | `S7` | G1 in both orders; G2 | one digest for G1, `e8bbfdef7908f026af80b86520349aa377d6963d98a995799aaf83d36251e946`; G2 `9781ab0207e9d09d8f5f6f5bee3acd117f6743b568f25f619987ef6fae79489d`; the four rows of G2's governance table |
| 2 | `S7` | the fourteen invalid blocks of the rejection table, and a valid block whose `record` class omits the round's record directory or receipt path | each FAILS in family `s7:` |
| 3 | `S8` | the three deltas between commits of this repository in the worked-example table; the scratch delta with LF and `é` in a path, under `core.quotePath` true and false | the four digests of the worked examples; one set of canonical bytes for both settings |
| 4 | `S4` | the four canonical example receipts, standalone | each HOLDS under its column |
| 5 | `S4` | a required field missing; a forbidden field present; an `A` field absent without a reason; an `A` field present with a reason; an unknown reason code; `execution_delta_digest` without `e`; a duplicate key; a key outside the field table; an object id of the wrong width | each FAILS in family `s4:` |
| 6 | lifecycle | a synthetic round for every cell of `V3-1`'s frozen `MC1`–`MC8` table, the passing case and each countercase | each passing case HOLDS; each countercase FAILS in the family of the settlement it breaks |
| 7 | `F4` | for each of `K1` to `K4`, one round the reading admits and one it rejects | as the reading says |
| 8 | input | a `ref` name, `HEAD` and an abbreviated id passed as a commit argument | each refused in family `input:` before any repository read |

Two countercases of that table describe a reading the shadow does not implement, and row 6 realizes
them as follows. `MC1`'s (a predicate given a branch tip as input) is the row-8 refusal together with
the static check of `V32-2`. `MC5`'s (an assertion evaluated on the live tree) becomes two vectors: a
completed synthetic round verified from `Q`, then verified again after later commits and
working-tree changes alter every file it records, with byte-identical output; and a receipt whose
recorded control-plane blob disagrees with the one at `F`, which FAILS in family `s4:`. The corpus
is executed as an exact set: a vector file the run does not execute, or an executed id with no file,
is a corpus failure.

## The comparison with `V2`, FROZEN

### Axes

The projection compares the shadow and `V2` only on questions both answer. It reads the rows from
the named subject commit, never from the working tree.

| axis | rows | `V2`'s question (codes) | the shadow's question, commit-local | same predicate? |
|---|---|---|---|---|
| `X0` | base-only | `base` exists and is an ancestor of a visibility target (`base:unreachable`) | `base` exists and is an ancestor of the subject | yes, with the target fixed to the subject |
| `X1` | landed | `tree(sealed_head)` equals `tree` (`topology:tree-mismatch`) | the same | yes |
| `X2` | landed | every commit of `rev-list sealed_head ^base` descends from `base` (`topology:ancestry`) | the same | yes |
| `X3` | landed | exactly one non-first parent of `landing` passes `X2`'s check, and it is `sealed_head` (`sealed-head:*`) | `landing` has exactly two parents and the second is `sealed_head` (`S9`'s shape) | **no**: `V2` admits a landing with more than two parents if one candidate passes |
| `X4` | landed | `landing` is the unique merge, in the visibility targets, whose non-first parent is `sealed_head` (`landing:*`) | `landing` exists and its second parent is `sealed_head` | **no**: uniqueness over live history is outside `S1` |

`V2`'s codes on any other question — certificate schema, evidence, policies, dependencies,
relocations, `row:certificate-mismatch` — are **not compared**: V3 has no counterpart to the
certificate data model, and the census says so rather than scoring them.

The shadow also reports, for each landed row, three **V3-only** facts: whether
`rev-list sealed_head ^base` is linear from `base` (`S3`'s form); whether `base` lies on the
first-parent chain of the landing's first parent (`S9`'s form); and the digest of
`delta(base, sealed_head)` (`S8`). They are information. They are never compared, and a row that
fails one is not thereby a divergence or an invalid round.

### Adjudication classes

Every (row, axis, perturbation) cell of the census is assigned exactly one class, by these rules
applied in order:

1. **`AGREE`** — the two verdicts are the same.
2. **`INPUT`** — they differ, and `V2`'s verdict on the same row and axis under `P0` equals the
   shadow's. The difference comes from an input `S1` excludes (the event payload, a remote-tracking
   ref, a recovery). It is not a defect of either implementation.
3. **`PREDICATE`** — they differ, rule 2 does not apply, and the axis is marked **no** above, and the
   difference is exactly the one named there (a landing with more than two parents for `X3`; a
   second merge carrying `sealed_head` as a non-first parent, or a landing absent from the visibility
   targets, for `X4`). The difference is by specification. It is not a defect.
4. **`IMPLEMENTATION`** — any other difference: the same question on the same inputs answered
   differently, or a shadow verdict of `UNDECIDABLE` where `V2` decided. It is a defect in at least
   one implementation.

The classes are assigned by the census code from the verdicts, not by the executor. An
`IMPLEMENTATION` cell is recorded with both verdicts and a minimal reproduction. **This round does
not decide which implementation is wrong, and changes neither to remove the difference**. `V2` is
never changed here in any case, and the shadow is changed only under the discipline in "The order
is part of the contract". Adjudication belongs to the owner.

### The perturbation control

The census runs the shadow and `V2` in a scratch clone of the subject whose `origin` URL points at a
path that does not exist, under `P0`, `P1`, `P2` and `P3` exactly as `F3` defines them, with `D`
replaced by the subject. The shadow is given the same explicit arguments in all four. Its report
excludes the scratch path and the time, and it must be **byte-identical across all four**. `V2`'s
`ROW` lines in each state are recorded and classified.

## Failure semantics, FROZEN

**The shadow's verdicts.** Every object the shadow evaluates — a vector, a receipt, a lifecycle
predicate, a projection cell — ends in exactly one of `HOLDS`, `FAILS` with one or more reason codes,
or `UNDECIDABLE` with one reason code (an object the repository does not contain, or a shallow
repository). `UNDECIDABLE` is never promoted to `HOLDS`, and never fixed by fetching: the shadow
performs no network operation of any kind.

**Exit status.**

| entry point | exit 0 | exit non-zero |
|---|---|---|
| `--self-test` | every internal fixture as expected | any fixture not as expected |
| `--corpus` | every vector gives its expected verdict and the set is exact | any vector not as expected, or the set not exact |
| `--verify-round`, `--publication`, `--project` | the question was evaluated, whatever the verdict; the verdict is printed | the arguments were refused, or the tool could not run |
| `--mode shadow` | always, the verdicts and any defects printed | never on a verdict; only if the interpreter itself cannot start the tool |

A non-zero `--self-test` or `--corpus` is a defect of the shadow, and the job goes red. A verdict
about a round or a row never changes any exit status. Neither a red shadow job nor a `FAILS`
verdict blocks anything, because the job is not required and nothing that is required reads it.

**Failures of the round.** A stop outcome of any target halts the round (status rule, below).
`AUTHORITY-LEAKED` on `V32-8` is not a discrepancy to record: it means the round did what it promised
not to do, and it fails the round.

## The evidence to record, FROZEN

`census.json` records, and the result note summarizes:

- the subject, the shadow's blob and `V2`'s blob at the subject, and the Python and git versions;
- for every row: its kind, each axis's shadow verdict and `V2` verdict under each of `P0`–`P3`,
  each cell's class, and for landed rows the three V3-only facts;
- the SHA-256 of the shadow's report under each of `P0`–`P3`, which must be one value;
- `V2`'s top-level result under each state;
- the counts per class.

The result note also records:

- the corpus as executed: every vector id with expected and obtained verdict, and the SHA-256 of the
  corpus directory's files in path order;
- the mutation controls (`V32-4`): each mutated check, the countercase it was run against, and the
  outcome;
- the static input-admission scan (`V32-2`) with every token searched and its count;
- every specification gap found beyond `K1`–`K4`, with the reading the shadow takes (`V32-7`);
- the non-authority battery at `E` (`V32-8`);
- every change to the shadow after its first commit, with the vector that justified it.

## The promotion boundary, FROZEN

**Promotion** is any change after which a V3 verdict can alter whether a build, a pull request or a
round is accepted. Exactly these acts are promotion:

1. invoking `tools/v3_verifier.py`, or any code derived from it, from `tools/release_gate.py`, from
   any step of a required check, or from any job a required check depends on;
2. a guard clause, a `V2` certificate, live-policy clause or conformance vector, or any other
   verifier's verdict depending on a V3 verdict;
3. adding the `V3 shadow verifier` job, or any job running V3 code, to the repository's required
   status checks, or otherwise changing the host's rules so that a V3 verdict can block a merge;
4. text in `AGENTS.md` that makes any V3 settlement operative, or an amendment of §A.37 that refers
   to V3 as governing;
5. creating `verification/receipts/`, or any V3 receipt anywhere in the tree;
6. running any round under V3's lifecycle (`F`, `W`, reconciliations, `Q`, fast-forward
   publication) as its governing protocol;
7. adding an authoritative mode to the shadow, or any argument or variable that makes a verdict
   change an exit status.

`V3-2` does none of them. **Only a round whose preregistration states prospectively that it
promotes may do any of them**, just as §A.37 makes a round sealing only by its prospective ownership
of seal state. The diff does not decide this. A round that performs one of these acts without that
statement has promoted without authority, whatever its diff looks like.

**What a promotion round must be able to cite from this round.** The following are necessary and
not sufficient:

- `V3-2` COMPLETE;
- `V32-3` `CONFORMANCE-EXACT` and `V32-4` `CONTROLS-FIRE`;
- `V32-5` with no `IMPLEMENTATION` cell;
- `V32-6` `PERTURBATION-INVARIANT`;
- `V32-7` `SPEC-SUFFICIENT`, or a specification round landed after `V3-2` that settles every gap it
  recorded, `K1`–`K4` included;
- `V32-8` `SHADOW-ONLY`.

**What this round does not settle, which a promotion round must.** How the first V3-governed round
is certified, given that no V3 round exists to certify it. Whether the host permits the non-force
update of `main` that `S10` requires, and for which actor (`V3-1`'s hazard `H1`). The migration
census of historical rounds. The retirement of `V1` and `V2`. The shadow's green record on the host
after this round lands is a host attestation. On its own it is not evidence of anything a promotion
round may cite.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V32-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` |
| `V32-1` | `IMPLEMENTED` — `tools/v3_verifier.py` exists, imports only the standard library, has exactly the entry points above and no authoritative mode, refuses non-object-id commit arguments, and names no round stem of the `V2` corpus in its logic | `IMPLEMENTATION-INCOMPLETE` |
| `V32-2` | `COMMIT-LOCAL` — a static scan of the shadow's source finds no match for any of the patterns `GITHUB_`, `refs/remotes`, `refs/pull`, `\borigin\b`, `\bfetch\b`, `ls-remote`, `for-each-ref`, `symbolic-ref`, `show-ref`, and `^\s*(import\|from)\s+(urllib\|http\|socket\|time\|datetime)\b`; the source reads the process environment in exactly one place, for `PATH`, and every git subprocess receives an explicit environment built from that value and fixed literals; and the report of `--mode shadow` is byte-identical under `P0`–`P3` and with a hostile environment (`GITHUB_EVENT_NAME`, `GITHUB_EVENT_PATH`, `GITHUB_SHA`, `GITHUB_REF`, `GIT_DIR` and `GIT_CONFIG_GLOBAL` set to misleading values) | `INPUT-LEAK` |
| `V32-3` | `CONFORMANCE-EXACT` — the corpus meets the minimum coverage, every vector gives its expected verdict in its expected family, and the set is exact | `CONFORMANCE-FAILED` |
| `V32-4` | `CONTROLS-FIRE` — in scratch, on a copy of the shadow and never in the tracked file, each of these checks is disabled in turn: `S3` linearity, `S7` authorization, `S9` conditions 1, 2 and 3, the `K3` first-parent rule, the `S12` withdrawal invariant, `S10`'s `delta(Λ, Q)` rule, and `S4`'s presence rules; with each disabled, its countercase vectors then pass | `CONTROL-VOID` — a mutated copy still rejects its countercase; the vector's verdict is void and the target stops |
| `V32-5` | `CENSUS-AGREES` — every `P0` cell `AGREE`, and every cell of `P1`–`P3` `AGREE` or `INPUT`; or `CENSUS-CLASSIFIED` — no `IMPLEMENTATION` cell in any state, and at least one `PREDICATE` cell | `CENSUS-IMPLEMENTATION-DIVERGENT` — any `IMPLEMENTATION` cell in any state |
| `V32-6` | `PERTURBATION-INVARIANT` — one SHA-256 for the shadow's report under `P0`–`P3`; `V2`'s verdicts recorded and classified | `PERTURBATION-SENSITIVE` |
| `V32-7` | `SPEC-SUFFICIENT` — no gap beyond `K1`–`K4`; or `SPEC-GAPS-RECORDED` — each further gap recorded with the shadow's reading and at least one vector exercising that reading | `SPEC-CONTRADICTORY` — two settlements the shadow cannot satisfy together on some vector; recorded, and the specification is not repaired here |
| `V32-8` | `SHADOW-ONLY` — `tools/release_gate.py`, `tools/certificate_verifier.py`, the guard, `AGENTS.md` and `architecture.md` have their `B` blobs at `E`; the workflow's diff `B`..`E` only adds lines, all inside the one new job; the guard at `E` gives `ALL CHECKS PASS` with 105 PASS and 0 FAIL and `D`'s verdict map; `V2` is authoritative OK at `E`; the release gate passes 19 of 19 steps at `E`; no promotion act of the list above is present | `AUTHORITY-LEAKED` — fails the round |
| `V32-9` | `SCOPE-HELD` — `git diff --name-status B E` is exactly the mutation budget below | `SCOPE-EXCEEDED` |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V32-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V32-1` | `IMPLEMENTED` | strong | the entry points are fixed here |
| `V32-2` | `COMMIT-LOCAL` | strong | the refusal of non-object-id arguments and the absence of network code make it structural |
| `V32-3` | `CONFORMANCE-EXACT` | moderate | the corpus is large, and rows 6 and 7 build synthetic rounds whose every cell `V3-1`'s model decided, but the shadow is new code |
| `V32-4` | `CONTROLS-FIRE` | moderate | nine mutations, each needing a countercase that reaches exactly one check |
| `V32-5` | `CENSUS-AGREES` | strong | rests on `F3`: all 30 landed rows hold `X1`–`X4`'s commit-local forms at `D`, and `V2` passes all 36 rows under `P0`. A measurement, not a forecast |
| `V32-6` | `PERTURBATION-INVARIANT`; `V2` as `F3` measured, so every `P2` cell `INPUT` and the six `P3` `landing:zero-candidates` cells `INPUT` | strong | the shadow reads no input the perturbations change; `V2`'s side rests on `F3` |
| `V32-7` | `SPEC-GAPS-RECORDED` | weak | `F4` found four gaps on reading alone; implementation usually finds more, but none is known |
| `V32-8` | `SHADOW-ONLY` | strong | the budget writes no gating file |
| `V32-9` | `SCOPE-HELD` | strong | the budget is fixed here |

**Status rule.** The round is COMPLETE iff every target reaches a passing outcome. It is HALTED at the
first stop outcome, and the targets not reached are recorded as such. `CENSUS-AGREES` and
`CENSUS-CLASSIFIED` are agreement findings, not proofs of correctness: two implementations can share
an error. The result note says so in those words.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V32-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V32-1`, `V32-2` | one: `tools/v3_verifier.py` with its self-test | self-test; the static scan; argument refusal |
| 2 | `V32-3`, `V32-4`, `V32-7` | one: the conformance corpus | the corpus exact; the mutation controls in scratch; gaps recorded |
| 3 | `V32-5`, `V32-6` | one: `census.json` | the census and the perturbation control |
| 4 | — | one: the workflow job and the README paragraph | the workflow diff is additive and inside the new job |
| 5 | `V32-8`, `V32-9` | one: the result note; its commit is `E` | the closing checks at `E`, then the exact-head pull request |

**Changes to the shadow after stage 1.** Any change to `tools/v3_verifier.py` after its stage-1
commit must, in the same commit, add a conformance vector that fails on the previous blob of the
tool and passes on the new one, with an expected verdict derived from `architecture.md` or from an
`F4` reading, and never from `V2`'s output or from the census. A change made after the census commit
voids the census, which is recomputed in full and recommitted; both are recorded in the result note.
A change whose only effect is to move a census cell towards `V2`'s verdict, without such a vector, is
forbidden.

## The mutation budget

- **Added:** `tools/v3_verifier.py`; the files of `verification/infrastructure/v3/conformance/`;
  `verification/infrastructure/round-v3-2-shadow-verifier/census.json` and `result.md`.
- **Modified:** `.github/workflows/verify.yml` (the one added job); `verification/README.md` (the one
  added paragraph).
- **Deleted:** nothing.
- **Never written:** `verification/infrastructure/v3/architecture.md`, `AGENTS.md`,
  `tools/release_gate.py`, `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
  `tools/control_plane_lint.py`, every other file under `tools/`, the guard and everything under
  `verification/lean/` and `verification/lean-mathlib/`, `verification/seals/`,
  `verification/certificates/`, `verification/programmes/`, `verification/audits/`, any other round's
  directory, `papers/` and `book/`. No `verification/receipts/` directory is created.

## What no outcome of this round licenses

1. Any sentence that V3 is operative, or that the shadow is, or should now be treated as,
   authoritative.
2. Any claim about the validity of a historical round under any protocol, from the census or from
   the V3-only facts.
3. Any change to `V1` or `V2` state.
4. Reading `CENSUS-AGREES` as a proof that either implementation is correct.
5. Re-opening `GH-1`, `CV-2` or `V3-1`.

## Hazards

- **`H1` — a shared misreading.** The shadow and `V3-1`'s model have the same author, so they could
  share a misreading of the specification. The expected values of corpus rows 1 to 4 come from
  `architecture.md`, and the mutation controls show that each named check can fire. Neither excludes
  an error both readings share. The model's code is not an input to the shadow, and no code of it
  is copied.
- **`H2` — authority outside the repository.** The host's required-check set is not in the tree. A
  host-side change could make the shadow job blocking with no commit at all. The promotion boundary
  names that change as promotion (act 3) and reserves it to a promotion round. The repository cannot
  enforce this; the owner's discipline does.
- **`H3` — history in the shadow job.** The repository vectors of corpus row 3 and the projection need
  full history. The job checks out with `fetch-depth: 0`, which is the host's action and not the
  tool's. Without it the shadow reports `UNDECIDABLE` and fetches nothing.
- **`H4` — `V2`'s recovery.** `V2` fetches when its base ref is absent. In the census the scratch
  clone's `origin` points at a path that does not exist, so recovery fails offline and `V2` fails
  closed, as `F3` measured under `P2`.
- **`H5` — a small census.** Thirty landed rows that all agree are weak evidence of agreement in
  general. Most of this round's evidential weight lies in the corpus, the mutation controls and the
  perturbation control. The census is the one place the two implementations meet on real history.
- **`H6` — provisional readings mistaken for specification.** `K1`–`K4`'s readings bind only the
  shadow. The shadow prints them at every run, and the promotion boundary requires them to be
  settled by a specification round.

## Files

### Files this round reads AND writes

`.github/workflows/verify.yml` (one added job); `verification/README.md` (one added paragraph).

### Files this round reads and MUST NOT write

`verification/infrastructure/v3/architecture.md`, `tools/certificate_verifier.py`,
`tools/release_gate.py`, the guard, `AGENTS.md`, and every file under
`verification/certificates/attestations/`.

## Preconditions

```control-plane-preconditions
d: 9c480626ba0b3d6242bb99783356afefaf4f4bcf
frozen-blob: verification/infrastructure/v3/architecture.md 6c80e584021f973c529625b1da89469e7b136dfe
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: .github/workflows/verify.yml 3ed93ea20bb42f986850d008d5a5edc93a4b7e34
frozen-blob: tools/release_gate.py ca851befa24028655ecbbee85e53482bc186eb82
frozen-blob: tools/certificate_verifier.py a475408874b850f34c31eca5e1cb4ab549601f38
frozen-blob: verification/lean/edge_rigidity_probe.py 2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f
frozen-blob: verification/README.md cda16e5d1464615ba51986f869e2f065c19bc920
# row 1: name freedom and absences, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-2' -e 'v3-2' -e 'round-v3-2' -e 'V32-' $D", "expect": "empty"}
{"id": "d1-tool-free", "scope": "D", "check": "git grep -l -F -e 'v3_verifier' -e 'V3 shadow' -e 'v3-shadow' -e 'verification/infrastructure/v3/conformance' $D", "expect": "empty"}
{"id": "d1-no-tool", "scope": "D", "check": "git ls-tree --name-only $D tools/v3_verifier.py", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
# row 2: the V2 rows the comparison reads, at D
{"id": "d2-rows-36", "scope": "D", "check": "test $(git ls-tree --name-only $D verification/certificates/attestations/ | wc -l) -eq 36", "expect": "exit0"}
{"id": "d2-base-only-6", "scope": "D", "check": "test $(for f in $(git ls-tree --name-only $D verification/certificates/attestations/); do git show $D:$f; done | grep -c -F '\"kind\": \"base-only\"') -eq 6", "expect": "exit0"}
# row 3: provenance, D to B: D an ancestor, and nothing but this file between them
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-2-shadow-verifier/preregistration.md'", "expect": "empty"}
# row 4: no execution object at B; files are read directly, never through git grep
{"id": "b4-no-tool", "scope": "B", "check": "git ls-tree --name-only $REF tools/v3_verifier.py", "expect": "empty"}
{"id": "b4-no-corpus", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/v3/conformance", "expect": "empty"}
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-2-shadow-verifier | grep -v -x -F 'verification/infrastructure/round-v3-2-shadow-verifier/preregistration.md'", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
{"id": "b4-rows-36", "scope": "B", "check": "test $(git ls-tree --name-only $REF verification/certificates/attestations/ | wc -l) -eq 36", "expect": "exit0"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-2-shadow-verifier/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37: `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main` and its second parent is exactly `E`. Conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; there is no rebase, amend or force-push. Each commit-bearing
stage commits before its checkpoint. A stop outcome halts the round. The halt is recorded in a result
note with the outcomes reached, and nothing else of the execution lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B`
descends from `B`, is a single-parent commit, and that the branch absorbed no later `main`. The
check is recorded in the result and followed by exact-head review. `V3-2` carries no guard clause,
manifest record or round certificate (reading `R1`).

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — no guard clause, no `V2` certificate.** `V3-2` adds no `V1` clause and writes no `V2`
  certificate or attestation, as `GH-1` and `V3-1` did not. A standing guard clause asserting non-authority
  would be an assertion about later trees, the `M5` form `V3-1` excluded. It would also block the
  promotion round it is meant to separate from, unless that round amended it. Non-authority is
  therefore checked at `E` and at `L` by this round's closing battery, and it holds afterwards by
  the promotion boundary: a later act of promotion is a promotion round by definition. The declined
  option is an `R7-V32` clause pinning the release gate's text.
- **`R2` — `V2` alone as comparator.** The census compares the shadow with `V2`. `V1` enters only
  through `V32-8`'s check that its verdict map is unchanged. `V1`'s per-round clauses are archived
  code over historical subjects, and `CV-1`'s census compared them with `V2` at `CV-1`'s own subject.
  This round makes no `V1`-to-V3 agreement claim, directly or by transitivity. The declined option
  runs the guard's per-round clauses beside the projection.
- **`R3` — a CI job, not a gate step.** The shadow runs in its own non-required job and nowhere in the
  release gate. A step in the gate would be promotion act 1. The declined option runs the shadow
  inside the gate with its exit status ignored, which leaves one edit between shadow and authority.
- **`R4` — the provisional readings live here.** `K1`–`K4` are settled for the shadow in this
  freeze, not by the implementation and not by amending `architecture.md`. A shadow that chose its
  own readings could choose them to fit its results, and a specification amended by an
  implementation round would no longer be the thing the shadow tests. The declined options are an
  implementation-chosen reading and a `V3-1` amendment.
- **`R5` — the conformance corpus beside the specification.** The corpus lives at
  `verification/infrastructure/v3/conformance/`, next to `architecture.md`, and not in the round's
  directory. It is the specification's executable companion and outlives this round, as `V3-1`'s
  `R6` placed the specification. The round's directory holds only its preregistration, census and
  result, per §A.36.
