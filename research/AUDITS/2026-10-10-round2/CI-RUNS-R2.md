# CI runs cited by the round-2 threads — verified through the GitHub API

Same reading as `../2026-10-10-round1/CI-RUNS.md`: on a research branch the release gate is red by construction
(`claims`, `duplicate` scan `research/archive/`; `lean-manuscript` refuses a design module without a census disposition);
the meaningful signals are the Mathlib bridge *Build* step, the module's `#print axioms` lines and the `lean-axioms` step.

| run | branch @ head | event | created (UTC) | Build step | module declarations on standard axioms | `lean-axioms` | gate red on |
|---|---|---|---|---|---|---|---|
| 38090594001 (job 114326045727) | `dev-origin/passive` @ `aef5d4463a604601dc5cbe2da89fa02a8b67bdbc` | `workflow_dispatch` | 2026-10-10T22:13:16Z | success (3645 jobs) | `OriginPassive`: 11 (the thread's log; the coordinator read the gate lines) | OK, 5882 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (2 problems) |
| 38091462366 (job 114328589839) | `dev-origin/passive` @ `c2484cca3107085e360c461167095262dba45444` | `workflow_dispatch` | 2026-10-10T22:27:03Z | success (3645 jobs) | `OriginPassive`: 13 (adds Section D: `finiteOrderOn_chartBody_of_binary`, `not_infiniteOrderOn_chartBody_of_binary`) | OK, 5884 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (2 problems) |

At the time of the audit the two runs' probe shards were still completing; the Mathlib bridge jobs had completed with
the step results above (read from `GET …/actions/runs/{id}/jobs` and the job logs). Design evidence only.
