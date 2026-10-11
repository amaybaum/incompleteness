# CI runs cited by the round-3 threads — verified through the GitHub API (live; rows added as each thread is audited)

Same reading as the round-1 and round-2 records: on a research branch the release gate is red by construction
(`lean-manuscript` refuses a design module without a census disposition; `claims` and `duplicate` also fail when the
branch carries `research/archive/`); the meaningful signals are the Mathlib bridge *Build* step, the module's
`#print axioms` lines and the `lean-axioms` step. Every run below is a `workflow_dispatch` on a disposable dev branch.
Design evidence only; nothing certified. Round-3 rule: no job or run cancelled by a thread.

| run | branch @ head | created (UTC) | Mathlib bridge job: Build step | module declarations on standard axioms | `lean-axioms` | gate red on | run conclusion / cancellations |
|---|---|---|---|---|---|---|---|
| 38098314988 (job 114348781009) | `dev-origin/exclusive` @ `39fd0e670a8a44a663a9090f4a27cf2f27e8fe15` | 2026-10-11T00:24:25Z | **failure** (three errors in `reach_mergeInto`: a `Decidable` instance naming the unrewritten term after `simp`) | `OriginExclusive`: 27 standard, 3 `sorryAx` (`reach_mergeInto`, `reach_collectAt`, `reach_pointMass`) | — | gate skipped | failure (build); 32 jobs success, none cancelled |
| 38099172719 (job 114351335821) | `dev-origin/exclusive` @ `5df964af0b3dac6c0d1c69d7078be14217b57e23` | 2026-10-11T00:39:31Z | success (3644 jobs; `Built OIBridge.OriginExclusive`, linter warnings only) | `OriginExclusive`: 33/33 | OK, 5893 named results, no sorry | `lean-manuscript` only (1 problem; the branch is cut from L) | failure (gate); 32 jobs success, none cancelled |
| 38096511360 (job 114343410536) | `dev-equivalence/omega4` @ `95beab2b48ab9a07dac820e1df7d0850828f5bec` | 2026-10-10T23:52:27Z | success (3644 jobs; `Built OIBridge.EqvOmega4 (14s)`, deprecation warnings only) | `EqvOmega4`: 15/15 | OK, 5875 named results, no sorry | `lean-manuscript` only (1 problem; cut from L: `claims`, `duplicate` PASS) | failure (gate); 32 jobs success, none cancelled |
| 38099025197 (job 114350890660) | `dev-equivalence/k2-schema` @ `472835c58ed8bbd10b402eb6aa47900428482d6a` | 2026-10-11T00:36:52Z | **failure** (`✖ [3642/3644] Building OIBridge.EqvK2Schema`; four errors: 105:87 `dict_tens`, 122:67 `dict_smul`, 167:64 `trace_dict_mul` unsolved goals after `ring`, 235:2 `dict_coordOf` `ring failed`) | `EqvK2Schema`: 10 standard, 12 `sorryAx` (`dict_tens`, `dict_prodState`, `dict_sum`, `trace_dict_mul`, `ipW_eq_trace`, `dict_coordOf`, `dictEquiv`, `posSemidef_dict_of_pure`, `subset_Q3_of_pure_dual`, `Q3_subset_of_pure`, `Q3_selfDual`, `pairCone_eq_Q3_of_drive`) | — | gate skipped | failure (build); 32 jobs success, none cancelled |
| 38101580750 (job 114358419270) | `dev-equivalence/k2-schema` @ `aabc649ea936479bdfec4818b0dbae8f8fda85d9` | 2026-10-11T01:21:50Z | success (3644 jobs; `Built OIBridge.EqvK2Schema (6.5s)`, unused-simp-argument warnings only) | `EqvK2Schema`: 22/22 | OK, 5882 named results, no sorry | `lean-manuscript` only (1 problem; cut from L) | failure (gate); 32 jobs success, none cancelled |
| 38099134414 (job 114351216052) | `dev-bridge/r3-dict` @ `3d554e7e0330ad8d2141b645479e9ef23be0f58b` | 2026-10-11T00:38:50Z | success (3644 jobs; `Built OIBridge.BridgeDictionary (23s)`, warnings only) | `BridgeDictionary`: 20/20 | OK, 5880 named results, no sorry | `claims` (7), `duplicate` (104), `lean-manuscript` (1) — the branch is cut from `research/bridge`, which carries `research/archive/` | failure (gate); 32 jobs success, none cancelled |
| 38101591388 (job 114358450003) | `dev-bridge/r3-reach` @ `747bcf94374e6dd1363a12f4f3b453b5618d04ef` | 2026-10-11T01:22:01Z | success (3646 jobs; `Built OIBridge.BridgeReach (1.7s)`, warnings only; the job waited in the queue until 01:33:55Z) | `BridgeReach`: 21/21 | OK, 5881 named results, no sorry | `claims` (7), `duplicate` (104), `lean-manuscript` (1) — as above | failure (gate); 32 jobs success, none cancelled |

The print-axioms lines were counted by the coordinator's `joblog_extract.py` over the saved job logs (the declaration
names listed per module in the audit notes); the gate tables were read line by line. The equivalence and origin dev
branches are cut from L (their gate tables show `claims` and `duplicate` PASS); the bridge dev branches are cut from
`research/bridge` and fail those two steps by construction, as the thread records.

Job conclusions, head SHAs, events and timestamps were read from `GET …/actions/runs/{id}` and `…/jobs`; the step
readings (Build, prints, `lean-axioms`, the gate table) from the Mathlib bridge job logs.
