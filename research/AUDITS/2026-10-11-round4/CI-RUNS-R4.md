# CI runs cited by the round-4 threads — verified through the GitHub API (live; rows added as each thread is audited)

Same reading as rounds 1–3: on a research branch the release gate is red by construction (`lean-manuscript` refuses a
design module without a census disposition); the meaningful signals are the Mathlib bridge *Build* step, the module's
`#print axioms` lines and the `lean-axioms` step. Every run below is a `workflow_dispatch` on a disposable dev branch
cut from L. Design evidence only; nothing certified. Round-4 rule: no job or run cancelled by a thread.

| run | branch @ head | created (UTC) | Mathlib bridge job: Build step | module declarations on standard axioms | `lean-axioms` | gate red on | run conclusion / cancellations |
|---|---|---|---|---|---|---|---|
| 38108620996 (job 114379324788) | `dev-origin/token-order` @ `35d326a32ea8c1efbde1bff43fef579325c4f50d` | 2026-10-11T03:30:46Z | success (3644 jobs; `Built OIBridge.OriginTokenOrder`, linter warnings only) | `OriginTokenOrder`: 45/45 (two print lines wrapped in the log, joined and counted) | OK, 5905 named results, no sorry | `lean-manuscript` only (1 problem); `claims`, `duplicate`, `legacy-records` 303, `v3-receipts` 43 PASS | failure (gate); 32 jobs success, 1 failure, none cancelled |
| 38111982910 (job 114389268268) | `dev-origin/angle` @ `9dd6a1733bcd…` | 2026-10-11T04:33:51Z | **failure** (one error: `OriginAngle.lean:181:25` rewrite direction of `blockOf_mul` in `blockOf_gen2_mem`) | `OriginAngle`: 52 prints — 46 standard, `oddPair_odd` on `[propext, Quot.sound]`, 5 `sorryAx` (`blockOf_gen2_mem`, `levelOneClause_of_gen2Dense`, `angleWeakened_of_rational`, `angleSuffices_iff`, `o12_core`) | — | gate skipped | failure (build); 32 jobs success, 1 failure, none cancelled (completed after the thread's close) |
| 38112242400 (job 114390032425) | `dev-origin/angle` @ `f0cd92729dc7b1199ef0dd969b610b48512ad937` | 2026-10-11T04:38:50Z | success (3644 jobs; `Built OIBridge.OriginAngle`, linter warnings only; the job waited in the queue until 04:47:02Z) | `OriginAngle`: 52/52 (51 on `[propext, Classical.choice, Quot.sound]`, `oddPair_odd` on `[propext, Quot.sound]`; one print line wrapped, joined) | OK, 5912 named results, no sorry | `lean-manuscript` only (1 problem); `claims`, `duplicate`, `legacy-records` 303, `v3-receipts` 43 PASS | in progress at audit time (29 success, 1 failure — the bridge job through the gate — two A42 shards pending); none cancelled |

The print-axioms lines were counted by the coordinator over the saved job logs (the GitHub job-log tool, the tail of
5000 and 3000 lines; the built-in `gh` client refuses the log redirect), with wrapped lines joined before counting;
the gate tables were read line by line. Job conclusions, head SHAs, events and timestamps were read from
`GET …/actions/runs/{id}` and `…/jobs`.
