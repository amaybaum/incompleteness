# Infrastructure round CI-RECEIPTS-1 — receipt-backed reuse of unchanged A42 exclusion evidence: PREREGISTRATION

**Status: drafting.** This file is the round's control plane. It is drafted on its pull request from `D` and is final
only at the commit `F` the owner designates; no commit after `F` changes it (§A.39). Sections marked *to be frozen*
are completed before `F` from the design runs recorded below; until then they state the rule they will carry and
leave the frozen values open.

```v3-round
round CI-RECEIPTS-1
kind non-sealing
record-directory verification/infrastructure/round-ci-receipts-1/
```

```v3-governed-paths
record AM verification/infrastructure/round-ci-receipts-1/
record AM verification/receipts/CI-RECEIPTS-1.json
execution A tools/ci_receipts.py
execution M .github/workflows/verify.yml
```

The record directory holds three files: this preregistration, the round's frozen controls `controls.py`, and the
result note. The receipt path is `verification/receipts/CI-RECEIPTS-1.json`. The two execution paths are the receipt
tool and the workflow. The paths are the same under every outcome. **No probe, no probe input, no Lean module, no
manuscript, no built artifact, `AGENTS.md`, `verification/ROADMAP.md` and no record of another round change under any
outcome.**

## The commit vocabulary

- `D` — `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`, the head of `main` after `CI-PERF-1` landed (main-push run
  36896981080, every job green; the A42 exclusion matrix skipped on push, as the aggregate requires).
- `F` — the commit the owner designates as this file's freeze. `delta(D, F)` is this file alone.
- `E` — the execution head the owner designates.
- `Λ`, `Q` — the reconciliation and the receipt commit, as §A.39 defines them.

## What the round is

The A42 exclusion matrix (`probes_a42_exclusion`, fifteen shards, about six CPU-hours) runs only on
`workflow_dispatch`, which is how every exact-head attestation is taken. Rounds whose execution commits change
nothing the A42 exclusion probe reads still recompute the whole matrix at every intermediate dispatch. This round adds
one mechanism: at an intermediate execution commit that a round's preregistration names in advance, a dispatch may
present the run id of an earlier successful exact-head run, and each A42 exclusion shard is then validated against
that run's receipt instead of recomputed, **if and only if** the shard's content-addressed manifest at the current
commit equals the manifest the receipt records and every identity check below holds. Otherwise the shard is
recomputed.

### Boundaries, frozen

1. **`F` and `E` are always full exact-head replays.** An `F` or `E` attestation run is a `workflow_dispatch` on
   exactly that commit with no reuse input; its aggregate must report every A42 exclusion shard as computed. A run
   that reports any shard as receipt-validated is not a `check-run` attestation for `F` or `E`, whatever its
   conclusion. `Q`'s run is also a full replay.
2. **Reuse only at explicitly identified intermediate execution commits.** A round may use reuse only at execution
   commits strictly between its `F` and its `E` that its own preregistration names in advance (by stage), and only
   with a source run on an ancestor commit of the same round. Pull-request and push runs never run the A42 exclusion
   shards, and the reuse input is a `workflow_dispatch` input only. A dispatch on a disposable branch may exercise the
   mechanism as design evidence; its result is never a round's evidence.
3. **No partial reuse.** The unit of reuse is the whole A42 exclusion family. One decision is taken once per run:
   either every one of the fifteen shards is receipt-validated against the same source run, or every shard is
   recomputed. A shard is never partly reused, and a run never mixes computed and receipt-validated A42 exclusion
   shards.
4. **Any mismatch forces recomputation.** A manifest difference in any category, a missing or unreadable receipt, a
   failed identity check, an unavailable source commit or an API error each force the full recomputation. Reuse
   is never the fallback of an error.
5. **First target: A42 exclusion only.** No other job reads or writes receipts. Generalization to other shards is a
   later round.
6. **Push and pull-request semantics are unchanged.** On `push` and `pull_request` the A42 exclusion matrix and the
   new receipt-decision job are skipped exactly as the matrix is at `D`, and the aggregate requires exactly that. A
   skipped job, a skipped matrix, or a run whose event is not `workflow_dispatch` is never a receipt source.

## The manifest

A shard's manifest is a canonical JSON object; its digest is the SHA-256 of its canonical serialization (sorted keys,
no insignificant whitespace, UTF-8). It has six categories, and a difference in any one of them is a mismatch.

| category | content |
|---|---|
| `probe` | the blob of `verification/lean/dita_support_minimality_probe.py` and the shard id (`--part` value) |
| `closure` | path and blob of every tracked `.py` file under `verification/lean/a42/`, of the receipt tool `tools/ci_receipts.py`, and of the three landed sources a tool executes: `verification/lean/dita_arc_exclusivity_probe.py`, `verification/lean/dita_index_map_probe.py`, `verification/lean/dita_index_map_independent.py` |
| `data` | path and blob of every other tracked file under `verification/lean/a42/` (at `D`, `Rle13_39.txt`) and of `verification/programmes/oi-qm/track-b/act-41-index-map-semantics/measurements.json` |
| `pins` | the dependency pins of the shard job, exactly as its install step states them |
| `environment` | the resolved interpreter (`sys.version`, implementation, machine, system), the runner image family (`ImageOS`), and the sorted `name==version` list of every installed distribution |
| `workflow` | the workflow's header (every non-comment line before `jobs:`, which carries the triggers and the reuse input) and the exact text of the two jobs that decide and run the shard: `a42_receipts` and `probes_a42_exclusion` |

A tracked path the manifest names but the commit lacks enters with a null blob, so deleting a file is a mismatch.
A directory entry is evaluated at the commit, so adding a file under `verification/lean/a42/` is a mismatch.

**Closure completeness is measured, not assumed.** Every computing shard runs the probe under an audit hook installed
in the interpreter and in every child interpreter it starts. The hook records each file the run opens. A computing
shard fails if any opened file tracked at the commit is outside the manifest's `closure` and `data` sets; no receipt
is emitted for it. Files the run creates are outputs, not inputs, and are not required in the manifest.

**The lists were measured.** Design run 36900831018 ran all fifteen shards with the closure set to the directory and
the tool alone. Every shard's probe printed its OK summary; fourteen failed the audit and `r5` passed it. The files
the audit named outside the manifest were exactly `verification/lean/dita_arc_exclusivity_probe.py` (read and executed
by `a42/lib42.py`; thirteen shards), and, in `paths` alone, `verification/lean/dita_index_map_probe.py`,
`verification/lean/dita_index_map_independent.py` and the act-41 `measurements.json`. These are the four explicit
entries above. The audit stays in force at every computing shard, so a later change that makes a shard read a new
tracked file fails that shard rather than leaving the file out of the manifest.

## The receipt

A computing shard that exits 0 and passes the closure audit emits one receipt, uploaded as an artifact of its own run
named for the shard. It records:

- the repository, the source run id, run attempt, job name, event and commit (`head_sha`); the job's numeric id is
  read from the API at validation and printed with the validated result;
- the shard id, the full manifest and its digest;
- the probe's result identity: its final summary line and the SHA-256 of its complete output;
- supporting metadata: start and end times, the runner image version, and the tracked files the run opened
  (recorded, not part of the manifest).

A receipt is never produced by a receipt-validated shard; a receipt's source run is always a run that computed.

## Validation

A shard is receipt-validated against a source run `R` exactly when all of the following hold; the first that fails
names the reason, and the decision is recomputation:

1. `R` is a run of this workflow file in this repository, its event is `workflow_dispatch`, it is completed and its
   conclusion is success.
2. The job named `Numerical probes / A42 exclusion (<shard>)` in `R`'s attempt exists exactly once and concluded
   success; a skipped, cancelled or failed job is not a source.
3. `R` carries exactly one receipt artifact for the shard; the receipt's run id, attempt, job, event, commit and shard
   equal what the API reports for `R` and that job.
4. The receipt's manifest serializes to the receipt's digest.
5. The receipt's repository-derived categories (`probe`, `closure`, `data`, `pins`, `workflow`) equal those computed
   from `R`'s commit itself, fetched from the repository; the receipt is not trusted for them.
6. The receipt's manifest equals the manifest computed at the current commit in the current job, category by
   category.
7. `R`'s commit is the current commit or an ancestor of it.

Because the receipt tool and the workflow fragments are in the manifest, check 5 and check 6 together establish that
the source run executed the same receipt code and the same job definition as the current run.

## The aggregate

The aggregate job distinguishes the two successes. On `workflow_dispatch` it reports the A42 exclusion family as
`computed` or as `receipt-validated from run <R>`, and requires the matrix result to be success in both; on every
other event it requires the matrix and the decision job to be skipped.

## Controls

Three layers, each with its decision rule fixed here. None of them is a substitute for another.

**The receipt tool's self-test** (`python3 tools/ci_receipts.py --self-test`) runs in the decision job of every
dispatch, before the decision. It builds a synthetic repository, computes a shard under the audit hook, and requires,
each as its own named check:

- the receipt is written and records run, commit, digest and result; a run that opens an unlisted tracked file fails
  and writes no receipt (closure audit);
- the positive control: an edit outside the manifest leaves the digest unchanged and the receipt holds, and `decide`
  returns reuse;
- one mutation per category, each a mismatch naming exactly its category at check 6: probe source (`probe`); imported
  helper, new helper, receipt tool (`closure`); data file under the closure directory, data file on the explicit list
  (`data`); dependency pin (`pins, workflow`); python-version in the job and the decision job (`workflow`); resolved
  Python version, resolved dependency version (`environment`);
- stale and forged receipts: the receipt of one run presented under another (check 3), a push run and a pull-request
  run (check 1), a dispatch run whose matrix was skipped (check 1), a successful run whose shard job was skipped (check
  2), a missing receipt (check 3), a receipt naming another commit (check 3), a receipt-validated record presented as a
  source (check 3), an edited manifest with a stale digest (check 4), an edited manifest with a consistent digest
  (check 5), a receipt claiming the current manifest from an older commit (check 5), a source off the current line
  (check 7);
- no partial reuse: one shard without a receipt makes `decide` return compute for the family; no input returns
  compute; a malformed run id is rejected.

**`controls.py`** runs on the real repository at a named commit `C`, every mutation in a scratch clone:

| id | control | holds when |
|---|---|---|
| K1 | determinism | the manifest at `C` is reproducible; the fifteen shard manifests differ only in the shard id; probe, closure and data blobs are all present |
| K2 | positive | an edit to `papers/Main.md` and to the aggregate job changes no shard manifest |
| K3 | mutations | probe source → `probe`; `a42/lib42.py`, a new file under `a42/`, `dita_arc_exclusivity_probe.py`, the tool → `closure`; `a42/Rle13_39.txt`, `measurements.json` → `data`; the shard job's numpy pin → `pins, workflow`; the shard job's python-version, the decision job, the header's input default → `workflow`; resolved Python and dependency versions → `environment`; a mutation that does not apply is a failure |
| K4 | lists | every closure and data path is tracked at `C`; the workflow matrix is the tool's fifteen shards |
| K5 | semantics | both A42 jobs are dispatch-only; the matrix needs the decision job and refuses any mode but `compute` and `reuse`; the reuse input is optional and defaults to empty; the aggregate requires both jobs, success on dispatch and skipped otherwise, and prints the two successes distinctly |
| K6 | live identity | with run and job identities read from the live API and the receipt served locally: the honest receipt rebuilt at the source commit holds at `C`; correct manifest with the wrong run id fails at check 3; correct manifest from the push run at `D` (36896981080) fails at check 1; from the failed design run 36900831018 fails at check 1; correct result with an edited manifest fails at check 4 (stale digest) and check 5 (consistent digest); a receipt naming another commit fails at check 3; no receipt fails at check 3 |
| K7 | tool | the receipt tool's self-test passes |

`python3 controls.py --self-test` runs K1–K5 and K7 at `HEAD`; `python3 controls.py check --commit C --source-run S`
runs all seven. It prints one `PASS` or `FAIL` line per check and `controls: OK -- <n> checks` only when none fails.
The countercontrol was run in drafting: a tool without `dita_arc_exclusivity_probe.py` in its closure and a workflow
without the aggregate's skipped requirement, the matrix's mode guard and the empty input default fail exactly K3
(executed source; workflow header, whose anchor is gone), and K5 (three checks), five of 24.

**The live run controls** are the exact-head runs of the execution below: the computing run at stage 1, the reuse run
at stage 2, and the full replay at `E`.

## Design evidence

Runs on the disposable branch `claude/ci-receipts-1-dev`; none is a round attestation.

| run | commit | what it showed |
|---|---|---|
| 36900689313 | `24bbc0cc` less one fix | decision job red: the self-test's synthetic repository committed bytecode the probe wrote; fixed by ignoring `__pycache__/` there |
| 36900831018 | `24bbc0cc` | the closure measurement above |
| DESIGN-SOURCE | `b6a39780` | DESIGN-SOURCE-RESULT |
| DESIGN-REUSE | DESIGN-REUSE-COMMIT | DESIGN-REUSE-RESULT |
| 36903494687 | `dc0a7fed` | DESIGN-NEG-RESULT |

## Execution

Every stage is a single-parent child of the one before. No stage changes this file.

| stage | parent | changes | blob after the stage |
|---|---|---|---|
| 1 | `F` | adds `verification/infrastructure/round-ci-receipts-1/controls.py`; adds `tools/ci_receipts.py`; edits `.github/workflows/verify.yml` by the edit `W1` below | controls `K-BLOB`, tool `T-BLOB`, workflow `W1-BLOB` |
| 2 | stage 1 | edits `.github/workflows/verify.yml` by the edit `W2` below (the aggregate job only) | workflow `W2-BLOB` |
| 3 = candidate `E` | stage 2 | adds the result note `result.md` | — |

**Stage 1 — the computing source run `S`.** The branch is held at stage 1 and the workflow dispatched with no input.
Acceptance: every job green; the decision job prints `mode compute`; all fifteen shards print their probe's OK summary
and `ci_receipts: receipt a42-receipt-<shard>`; the run carries exactly fifteen artifacts named
`a42-receipt-<shard>`.

**Stage 2 — the named intermediate reuse commit.** Stage 2 is the one commit of this round at which reuse is
permitted. Its change lies outside the manifest. The branch is held at stage 2 and the workflow dispatched with
`a42_reuse_run` set to `S`. Acceptance: every job green; the decision job prints `all 15 shards hold; mode reuse from
run S`; each shard prints `receipt-validated` with source run `S`; the aggregate prints `A42 exclusion: success,
receipt-validated from run S (15 shards; not an F, E or Q attestation)`; and `python3 controls.py check --commit
<stage 2> --source-run S` prints `controls: OK`.

**Candidate `E`.** Stage 3 adds the result note. The branch is held at `E` and the workflow dispatched with no input.
Acceptance: every job green; the decision job prints `mode compute`; all fifteen shards compute and emit receipts; the
aggregate prints `A42 exclusion: success, computed (15 shards)`; and `controls.py check --commit E --source-run S`
prints `controls: OK`. This run is `E`'s `check-run` attestation; `F`'s is a dispatch at `F`, where the workflow is
`D`'s and every A42 shard computes as at `D`.

## Outcomes

- **`CI-RECEIPTS-1-OPERATIVE`** — every acceptance above holds.
- **`CI-RECEIPTS-1-HALTED`** — any acceptance fails. The round halts under §A.39's halted-round rule; a fix is a new
  round.

The rule is mechanical: the label is `CI-RECEIPTS-1-OPERATIVE` exactly when the stage-1 run, the stage-2 reuse run,
both `controls.py check` runs and the `E` replay each print their stated acceptance lines with every job green, and
`CI-RECEIPTS-1-HALTED` otherwise.

## The workflow edits

W-EDITS
