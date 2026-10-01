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
   with a source run on a commit of the same round. Reuse at a design run, a pull-request run or a push run does not
   exist: those events never run the A42 exclusion shards, and the reuse input is a `workflow_dispatch` input only.
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
| `closure` | path and blob of every tracked file in the probe's transitive import and tool closure: every module the probe and its tools import from the repository, the receipt tool itself, and every repository source a tool executes or reads as code |
| `data` | path and blob of every tracked non-code file the shard reads (for example `verification/lean/a42/Rle13_39.txt` and the JSON and measurement files the landed probes replay) |
| `pins` | the dependency pins of the shard job, exactly as its install step states them |
| `environment` | the resolved interpreter (`sys.version`, implementation, machine, system), the runner image family (`ImageOS`), and the sorted `name==version` list of every installed distribution |
| `workflow` | the exact text of the workflow fragments that decide and run the shard: the receipt-decision job and the A42 exclusion job |

**Closure completeness is measured, not assumed.** Every computing shard runs the probe under an audit hook installed
in the interpreter and in every child interpreter it starts. The hook records each file the run opens. A computing
shard fails if any opened file tracked at the commit is outside the manifest's `closure` and `data` sets; no receipt
is emitted for it. Files the run creates are outputs, not inputs, and are not required in the manifest.

*To be frozen:* the declared roots of the closure and the data list, measured from the opened-file sets of a full
design run, and the exact categories into which each measured file falls.

## The receipt

A computing shard that exits 0 and passes the closure audit emits one receipt, uploaded as an artifact of its own run
named for the shard. It records:

- the source run id, run attempt, job name and job id, the event, and the commit (`head_sha`);
- the shard id, the full manifest and its digest;
- the probe's result identity: its final summary line and the SHA-256 of its complete output;
- supporting metadata: start and end times and the runner image version (recorded, not part of the manifest).

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

Because the receipt tool and the workflow fragments are in the manifest, check 5 and check 6 together establish that
the source run executed the same receipt code and the same job definition as the current run.

## The aggregate

The aggregate job distinguishes the two successes. On `workflow_dispatch` it reports the A42 exclusion family as
`computed` or as `receipt-validated from run <R>`, and requires the matrix result to be success in both; on every
other event it requires the matrix and the decision job to be skipped.

## Controls

*To be frozen,* each with the decision rule stated before it runs:

- **Mutation controls**, one per category, each a single change that must turn a valid receipt into a mismatch naming
  that category: the probe source; an imported helper under `verification/lean/a42/`; a data file; a dependency pin;
  the Python version or the workflow fragment.
- **Positive control:** an edit to a tracked file outside the manifest leaves the manifest digest unchanged and the
  receipt validates.
- **Stale and forged receipts:** a receipt with the correct manifest presented under a wrong run identity (a
  different run id, a run whose shard job was skipped, a push or pull-request run, a different commit) fails; a
  receipt with the correct result and a wrong manifest fails.
- **Skipped matrix:** a run in which the A42 exclusion matrix was skipped is rejected as a source.
- **Closure audit:** a run that opens a tracked file outside the manifest fails and emits no receipt.

Offline controls run in the receipt tool's self-test and in `controls.py`; the live controls run against real runs of
this round's execution, at the intermediate commits frozen below.

## Execution

*To be frozen:* the stages, the intermediate commit at which the live reuse control runs and the run that is its
source, the tool blob, the workflow edit and the controls blob.

## Outcomes

*To be frozen:* the outcome labels and the mechanical rule that selects among them.
