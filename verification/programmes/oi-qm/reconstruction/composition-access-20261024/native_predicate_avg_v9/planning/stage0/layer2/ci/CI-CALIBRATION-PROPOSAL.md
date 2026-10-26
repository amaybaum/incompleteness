# NP-AVG-1 Stage 0 Layer 2: the planted-set CI timing calibration (proposal, for review)

**Status: a proposal. Nothing here is placed under `.github/`, pushed to a trigger branch or
dispatched.** The owner, amaybaum, 2026-10-26, authorized conditionally "a separate, planted-set-only
CI timing calibration, provided it cannot access v8 and its exact workflow and resource limits are
reviewed before dispatch. This is not authorization to dispatch the existing full experimental
workflow." The owner also ruled: "Require at least 20 independent timing calibrations on the
relevant CI runner class." This directory holds what the review needs: the workflow, the two
scripts, and this note. Placing the workflow and launching it are later steps, each after review
and with the owner's authorization (§A.43 item 4).

## 1. What runs, and why it cannot reach v8

| file | role |
| --- | --- |
| `np-avg-1-stage0-planted-calibration.yml` | the workflow: `guard`, then `calibrate` (20 matrix jobs), then `aggregate` |
| `calib_ci.py` | one calibration: `l2calib.py`'s procedure on planted quantity sets (sizes 8–40, 12 sets per size, fixed seed, ball(4) displaced to (40, 0, 0)) |
| `calib_aggregate.py` | requires at least 20 calibrations (VOID otherwise); computes the ratio statistic for u_cal on a v8-free aggregate |

**No v8-capable object can exist in the calibration process.**
- `calib_ci.py` imports no Layer-2 or engine module. It reads `s0geom.py`, `s0ref.py` and
  `l2refcheck.py` as text and checks their SHA-256 against `../code/LAYER2-MANIFEST.json`, as it
  does for `l2calib.py`. It then executes only the named geometry and closure definitions (`axes`,
  `vadd`, `l1`, `lball`, `Rule`, `FROZEN`, `Pair`, `_slices`, `in_cone`, `tip_labels`, `tips`,
  `closure`; `unit`, `shift`, `cells_within`, `RefGeometry`, `self_supporting`, `greatest`;
  `CachedGeo`). `Setup`, `V8`, `Context`, `record_at`, `num_records`, `record_samples`,
  `ref_context` and the grants are never defined.
- **Fail-closed checks.**
  - Before timing: no forbidden name in the extracted namespaces, and no engine or Layer-2 module
    imported.
  - After timing: a scan of the interpreter's objects for any `Setup`, `Context` or grant, or any
    object carrying (dim, n, port) = (3, 6, (0, 0, −3)).
  - On any hit the script prints VOID, writes no file and exits 2.
- `calib_aggregate.py` imports nothing from Layer 2 and reads no v8 configuration. Its statistic is
  on the sum of each calibration's four timing tables. The v8-weighted statistic (each calibration's
  v8 estimate, as `design/kappa_calibration.py` computes it, from combinatorics only) is computed
  afterwards, locally, from the retained artifact.

**Local evidence** (`design/ci_local_check.py`, step `ci_calibration_local_check`):
- the extracted closure equals `s0geom.closure` on every planted set (0 mismatches; this check alone
  imports the real engine, and it never runs in CI);
- a planted v8-keyed object makes the script exit 2 with VOID and no file;
- an ordinary run passes the tripwire;
- the aggregator refuses 19 calibrations and accepts 20;
- the workflow's triggers, permissions, concurrency, matrix and timeouts are as stated below.

## 2. The trigger, and the trade-offs

GitHub runs a `workflow_dispatch` workflow only if the file is on the default branch. Three
mechanics were considered.

| option | how it runs | for | against |
| --- | --- | --- | --- |
| **A. `workflow_dispatch` on `main`** | the workflow, the CI scripts and the five code files they read land on `main` by a reviewed pull request; the owner dispatches it | an explicit, logged dispatch by the owner; the file is reviewed where it lives | lands Layer-2 WIP code on `main` before Layer 2 is frozen (§A.28's burden on permanent content); the landing PR runs `verify.yml`; a later edit to the code changes what a dispatch runs, unless the guard's pins are updated by another reviewed PR |
| **B. `push` to a dedicated branch (proposed)** | a branch `ci-calibration/np-avg-1-stage0`, cut from `main`, carrying only this workflow under `.github/workflows/` and the files it reads; pushing that branch starts it | nothing lands on `main`; the branch's content is exactly what is reviewed; the guard pins every file by SHA-256 and the exact ref | the push is the launch (§A.43 item 4): it needs the owner's explicit authorization, recorded on the guiding PR, naming the branch head SHA; every later push to that branch is another launch, so the branch must be pushed once and then left |
| C. `pull_request` | a PR from the branch | review UI | runs on a synthetic merge, and again on every push to the PR; it is not a single, designated launch. Rejected |

**Why B is proposed.** It runs the reviewed files and only them, keeps WIP code off `main`, and
makes the single push the owner's designated launch.

**Its conditions:**
- **Base.** The branch is cut from `main` and adds only `.github/workflows/np-avg-1-stage0-planted-calibration.yml`,
  `stage0/layer2/ci/` and the files the scripts read (`code/s0geom.py`, `s0ref.py`,
  `l2refcheck.py`, `l2calib.py`, `LAYER2-MANIFEST.json`), all under the NP-AVG-1 planning
  directory. It is not cut from the research branch, whose history differs from `main`.
- **Other workflows on that push.**
  - `verify.yml` and `hidden-sector-replay.yml` run on pushes to `main` only.
  - `bg2-orientation-design.yml` and `bridge-compatibility-research.yml` have path-filtered push
    triggers with no branch filter. Their paths (`bekir-golomb-orientation-design/**`,
    `bridge-compatibility-audit/**`, `physical-state-operation-compatibility/**`,
    `OIBridge/BridgeFiniteProtocol.lean` and their own workflow files) are not touched by a branch
    cut as above.
  - This must be re-checked at the launch against the exact branch diff. A branch that touched those
    paths would start them, which is why option B fixes the base.
- **No pull request** is opened from the branch.
- **Pins.** The pinned SHA-256 values in the workflow's `env` are filled in at review, from the exact
  files on the branch. The guard fails if any differs, or if the ref is not the dedicated branch.
- **Action versions** are pinned to commit SHAs at review.

## 3. Resource limits (for review)

| limit | value |
| --- | --- |
| runner class | `ubuntu-24.04`, GitHub-hosted: the class the enumeration's jobs would use. The calibration is of that class, so the enumeration workflow must name the same one |
| calibrations | 20 (matrix `index` 1–20), each an independent job on its own runner; the owner's minimum |
| parallelism | `max-parallel: 4` |
| concurrency | one group, `cancel-in-progress: false`: a second push queues instead of cancelling |
| timeouts | `guard` 5 min; each `calibrate` job 15 min; `aggregate` 5 min |
| worst-case runner time | 5 + 20 × 15 + 5 = 310 runner-minutes, if every job hits its timeout |
| expected runner time | about 20 × 2–4 min, with one calibration taking about 11 s locally plus setup; roughly 40–80 runner-minutes in all |
| permissions | `contents: read`; no secrets; `persist-credentials: false` |
| retention | artifacts for 30 days, then retained under §A.42 by an evidence-retention PR if a claim depends on them (the κ decision would) |
| v8 access | none: no engine or Layer-2 module is imported, no v8 configuration is read, and a tripwire fails closed |

## 4. What the result is used for

`calib_aggregate.py`'s statistic over 20 or more runner-class calibrations is the candidate for
u_cal: the 99th percentile of the ratio between two independent calibrations (`KAPPA-PROPOSAL.md`).
The owner fixes κ = u_cal × u_model from it, before any v8 count (owner ruling on sequencing). The
calibration's tables also replace the local calibration in the dry run of the enumeration, if the
owner later authorizes one.

## 5. Review checklist

1. The scripts import nothing v8-capable; the forbidden-name list and the tripwire cover every
   v8-capable name in `s0geom.py` and `s0ref.py`.
2. The extracted definitions equal the engine's (local equivalence, 0 mismatches), and the hash
   checks bind them to the manifest.
3. The workflow's trigger, permissions, concurrency, matrix, timeouts and pins.
4. The branch diff at launch: only the files listed in §2, and no path of another push-triggered
   workflow.
5. The owner's authorization of the push, naming the branch head SHA.
