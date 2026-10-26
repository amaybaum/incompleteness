# NP-AVG-1 Stage 0 Layer 2: the planted-set CI timing calibration (proposal, for review; r5)

**Status: a proposal. Nothing here is placed under `.github/`, pushed to a trigger branch or
dispatched.** The owner, amaybaum, 2026-10-26, authorized conditionally "a separate, planted-set-only
CI timing calibration, provided it cannot access v8 and its exact workflow and resource limits are
reviewed before dispatch. This is not authorization to dispatch the existing full experimental
workflow." The owner also ruled: "Require at least 20 independent timing calibrations on the
relevant CI runner class." Its compute time counts in the campaign's 24-hour ceiling ("Include
calibration, count pass, primary run, mutant campaign, retries, and execution overhead").

**r5 applies LAYER2-R4-REVIEW §6:** CI-1 to CI-4 (required before dispatch), CI-5 to CI-7
(recommended), the isolation basis and the trigger note. A short pre-dispatch re-check of the exact
branch commit (tree, pins, live-main triggers) remains, before the owner authorizes the push.

## 1. What runs, and why it cannot reach v8

| file | where it runs | role |
| --- | --- | --- |
| `np-avg-1-stage0-planted-calibration.yml` | CI | `guard`, then `calibrate` (20 matrix jobs), then `aggregate` |
| `calib_ci.py` | CI | one calibration: `l2calib.py`'s procedure on planted quantity sets (sizes 8–40, 12 sets per size, fixed seed, ball(4) displaced to (40, 0, 0)) |
| `calib_aggregate.py` | CI | requires at least 20 calibrations from one commit (VOID otherwise); a v8-free summary, per CPU model |
| `postrun.py` | locally, after the run | the identity check against the owner-named SHA, u_cal by the preregistered rule, the per-job fixed overhead |

**Where isolation rests.** `calib_ci.py` imports no Layer-2 or engine module. It reads `s0geom.py`,
`s0ref.py` and `l2refcheck.py` as text, checks their SHA-256 against `../code/LAYER2-MANIFEST.json`
(and `l2calib.py`'s), and executes only a whitelist of 19 definitions, with an exact-set check.
`Setup`, `V8`, `Context`, `record_at`, `num_records`, `record_samples`, `ref_context` and the grants
are never defined. The extracted `closure` has no guard of its own. **Isolation therefore rests on
this reviewed, pinned script, which builds only planted sets from constants, and not on the engine's
v8 lock.** The fail-closed checks are backstops:
- before timing: no forbidden name in the extracted namespaces (`FORBIDDEN` now also names `V8_KEY`,
  `V8_REF` and `NO_V8`), and no engine or Layer-2 module imported;
- after timing: a scan of the interpreter's objects for any `Setup`, `Context` or grant, or any object
  carrying (dim, n, port) = (3, 6, (0, 0, −3)). It catches objects, not raw tuples.

The only file read beyond the six above is `/proc/cpuinfo`, for the CPU model (CI-4). The review's
audit hook found the six opens and no project import (LAYER2-R4-REVIEW §6).

**Local evidence** (`design/ci_local_check.py`, step `ci_calibration_local_check`):
- the extracted closure equals `s0geom.closure` on every planted set (0 mismatches; this check alone
  imports the real engine, and it never runs in CI);
- a planted v8-keyed object makes the script exit 2 with VOID and no file; an ordinary run passes;
- each calibration records its CPU model, wall-clock start and end, and run identity;
- the aggregator refuses 19 calibrations, accepts 20, and refuses 20 from two commits;
- `postrun.py` on a synthetic launch (20 calibrations, a run record and job records) holds with a
  u_cal, and is VOID when the authorized SHA differs;
- the workflow: one push trigger on the dedicated branch only, `contents: read`, concurrency, 20
  calibrations at `max-parallel: 4`, a timeout on every job, no self-pin, the three file pins equal to
  the files' SHA-256, every action pinned to a commit SHA, and `aggregate` under `always()` and the
  guard's success.

## 2. The trigger

GitHub runs a `workflow_dispatch` workflow only if the file is on the default branch. Three mechanics
were considered; B is proposed.

| option | how it runs | for | against |
| --- | --- | --- | --- |
| A. `workflow_dispatch` on `main` | the workflow, the CI scripts and the code files they read land on `main`; the owner dispatches it | an explicit, logged dispatch | lands Layer-2 WIP code on `main` before Layer 2 is frozen (§A.28) |
| **B. `push` to a dedicated branch** | `ci-calibration/np-avg-1-stage0`, carrying only this workflow under `.github/workflows/` and the files it reads; pushing it starts it | nothing lands on `main`; the branch's content is what is reviewed | the push is the launch (§A.43 item 4): it needs the owner's authorization naming the branch head SHA; every later push is another launch |
| C. `pull_request` | a PR from the branch | review UI | a synthetic merge, re-run on every push. Rejected |

**Conditions of B (re-checked at launch against live `main`).**
- **Exactly one commit on the live `main` head.** It adds only
  `.github/workflows/np-avg-1-stage0-planted-calibration.yml`, `stage0/layer2/ci/` and the files the
  scripts read (`code/s0geom.py`, `s0ref.py`, `l2refcheck.py`, `l2calib.py`, `LAYER2-MANIFEST.json`),
  all under the NP-AVG-1 planning directory. **No pull request** is opened from the branch.
- **Other workflows on that push** (LAYER2-R4-REVIEW §6):
  - `verify.yml` (push to `main`; `pull_request`) and `hidden-sector-replay.yml` (`main` only) do not
    fire.
  - `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` have push triggers on **any
    branch**, filtered only by path. For a new branch GitHub diffs against the parent of the earliest
    pushed commit, so one commit on `main`'s head that adds only the paths above matches neither
    filter. A push of more than 1,000 commits, or a diff timeout, runs path-filtered workflows
    unconditionally. They stay quiet only if the branch is exactly that one commit; the review's
    `origin/main` was from 2026-10-24, so this is re-checked at launch.
- **Identity (CI-1).** The workflow pins no hash of itself: a file cannot contain its own SHA-256, so
  r4's self-pin could never pass. The three file pins live in the pushed commit, so they detect
  drift, not substitution. The binding is the owner's authorization naming the exact head SHA, checked
  after the run by `postrun.py`: the run's `head_sha` (from the host's run record), and every
  calibration's `GITHUB_SHA` and `GITHUB_RUN_ID`, must equal the authorized SHA and the run, or the
  result is VOID. The check's output is retained with the result.

## 3. Pins and versions (CI-2)

| item | pinned to | how it was resolved |
| --- | --- | --- |
| `calib_ci.py` | `PIN_CALIB_CI`, its SHA-256 | from the file in this tree |
| `calib_aggregate.py` | `PIN_CALIB_AGGREGATE` | the same |
| `LAYER2-MANIFEST.json` | `PIN_MANIFEST` (it pins the four code files the scripts read) | the same |
| `actions/checkout` | `3d3c42e5aac5ba805825da76410c181273ba90b1` (v7.0.1) | `git ls-remote` on 2026-10-26 (lightweight tags; the SHA is the commit) |
| `actions/setup-python` | `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0` (v7.1.0) | the same |
| `actions/upload-artifact` | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` (v7.0.2) | the same |
| `actions/download-artifact` | `9000827ccba6bdab643e8b6fd33ac0654aef8333` (v8.0.2; `merge-multiple` exists from v4.1) | the same |
| Python | 3.13.16 | listed for `linux` 24.04 x64 in `actions/python-versions`' `versions-manifest.json` as read on 2026-10-26 |

**What is not confirmed offline.** Whether these action majors run unchanged on the hosted
`ubuntu-24.04` image on the launch day, and whether the artifacts of upload-artifact v7 are read by
download-artifact v8 as expected, cannot be confirmed without running Actions. setup-python reads the
versions manifest at run time, so 3.13.16's availability is confirmed only as of the read. A failure of
any of these fails the job (safe, but it spends a launch). The pre-dispatch re-check confirms each
against the live sources. Any change to the code files changes `PIN_MANIFEST`, and the pins are
refilled from the exact branch tree at that re-check.

## 4. u_cal: the preregistered statistic (CI-3)

Fixed here, before any CI data, and implemented in `postrun.py`:
1. **The quantity.** For each calibration i, K_i = the v8 estimate's known terms with that
   calibration's tables (`l2plan.estimate` on the v8 dry run's context-size histogram, without the C7
   inputs or the survivor cap: the dry run's standing computation, no enumeration). This is the
   v8-weighted aggregate, not the unweighted sum of the tables (which `calib_aggregate.py` reports for
   information).
2. **The spread.** s = the sample standard deviation of log K_i over all n calibrations.
3. **An upper confidence bound, not a point estimate.** s_U = s · √((n − 1) / χ²_{0.05, n−1}), the
   one-sided 95 % upper confidence bound on the standard deviation, with χ²'s lower 5 % quantile by the
   Wilson–Hilferty approximation. (The review's simulation puts the n = 20 point estimate's 5–95 % range
   at ±6–9 %; the bound takes that error into u_cal rather than leaving it to u_model.)
4. **u_cal = exp(2.3263 · √2 · s_U)**, the 99th percentile of the ratio of two independent lognormal
   draws at that bound, rounded up to three decimals.
5. **Reported for information only:** the point estimate exp(2.3263 · √2 · s) and the empirical 99th
   percentile of the ordered-pair ratios.

**Mixed runner hardware.** All calibrations are pooled, whatever their CPU model: the run would draw
its jobs from the same hosted fleet, so the pooled spread is the relevant one. The per-model counts and
medians are reported beside it. Fewer than 20 calibrations in all, or any identity failure, is VOID.

**What the statistic is, and is not.** The ratio of two single calibrations is conservative for the
campaign total, whose many jobs average runner noise, and about right for a single job's timeout. It is
not fitted: it is fixed before the data, and it can only be larger than the point estimate.

**At n = 20,** s_U ≈ 1.37 s. For s = 0.06 that gives u_cal ≈ 1.31; for s = 0.09, ≈ 1.50 (illustration,
not data).

## 5. Measurements the run adds (CI-4 to CI-6)

- **CI-4, the CPU model**, from `/proc/cpuinfo`, in every calibration and per model in the aggregate.
- **CI-5, the per-job fixed overhead.** Each calibration records its script's wall-clock start and end
  (UTC). `postrun.py` reads the host's job records and reports, per calibration job, the job duration
  minus the script time (median, 90th percentile, maximum), and the guard and aggregate jobs'
  durations. This measures `budget.campaign.per_job_fixed_overhead_seconds`, which the campaign total
  needs (r4 carried it as a judgement inside the reserve; it is a cost).
- **CI-6, temporal independence.** All 20 jobs of one launch run within minutes of each other, so
  time-of-day variation is not sampled. **Proposed: two launches at least six hours apart,** each a
  separate push authorized by the owner, each of 20 calibrations; `postrun.py` pools them (n = 40). The
  alternative is one launch, with the time-of-day variation stated as part of u_model's judgement. The
  owner chooses; the second launch's compute time counts in the campaign ledger.
- **CI-7.** `aggregate` runs under `always()` and the guard's success, so when calibration jobs fail it
  prints VOID with the number found instead of being skipped. It never runs after a failed guard.

## 6. Resource limits (for review)

| limit | value |
| --- | --- |
| runner class | `ubuntu-24.04`, GitHub-hosted: the class the enumeration's jobs would use |
| calibrations | 20 per launch (matrix `index` 1–20), each an independent job on its own runner |
| parallelism | `max-parallel: 4` |
| concurrency | one group, `cancel-in-progress: false` |
| timeouts | `guard` 5 min; each `calibrate` job 15 min; `aggregate` 5 min |
| worst-case runner time | 5 + 20 × 15 + 5 = 310 runner-minutes per launch |
| expected runner time | about 20 × 2–4 min per launch (one calibration takes about 11 s locally, plus setup); 40–80 runner-minutes. It is charged to the campaign ledger as measured |
| permissions | `contents: read`; no secrets; `persist-credentials: false` |
| retention | artifacts for 30 days; retained under §A.42 by an evidence-retention PR before the κ decision lands, with `postrun.py`'s output and the host's run and job records |
| v8 access | none in CI. `postrun.py`, run locally, computes the v8 dry run's known terms (combinatorics and the cost formula; no enumeration, no context, no closure) |

## 7. What the result is used for

u_cal from §4 enters κ = u_cal × u_model, rounded up to one decimal (the owner's method), before any
v8 count. The calibration's tables also replace the local calibration in the v8 dry run. The per-job
fixed overhead fills the campaign ledger's execution-overhead term.

## 8. Review checklist

1. The scripts import nothing v8-capable; the forbidden-name list and the tripwire are backstops to the
   whitelist, and isolation rests on the pinned script.
2. The extracted definitions equal the engine's (local equivalence, 0 mismatches), and the hash checks
   bind them to the manifest.
3. The workflow's trigger, permissions, concurrency, matrix, timeouts, pins and action SHAs.
4. u_cal's rule (§4) is fixed before the data, and `postrun.py` implements it.
5. The branch at launch: exactly one commit on the live `main` head, only the files of §2, no path of
   another push-triggered workflow, no PR.
6. The owner's authorization of each push, naming the branch head SHA; `postrun.py` holds on the run.
