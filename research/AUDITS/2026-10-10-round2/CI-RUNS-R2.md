# CI runs cited by the round-2 threads — verified through the GitHub API

Same reading as `../2026-10-10-round1/CI-RUNS.md`: on a research branch the release gate is red by construction
(`claims`, `duplicate` scan `research/archive/` when the branch carries it; `lean-manuscript` refuses a design module
without a census disposition); the meaningful signals are the Mathlib bridge *Build* step, the module's
`#print axioms` lines and the `lean-axioms` step. Every run below is a `workflow_dispatch` on a disposable dev branch.
Design evidence only; nothing certified.

| run | branch @ head | created (UTC) | Mathlib bridge job: Build step | module declarations on standard axioms | `lean-axioms` | gate red on | run conclusion |
|---|---|---|---|---|---|---|---|
| 38090594001 (job 114326045727) | `dev-origin/passive` @ `aef5d4463a604601dc5cbe2da89fa02a8b67bdbc` | 22:13:16Z | success (3645 jobs) | `OriginPassive`: 11 | OK, 5882 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (2 problems) | failure (gate) |
| 38091462366 (job 114328589839) | `dev-origin/passive` @ `c2484cca3107085e360c461167095262dba45444` | 22:27:03Z | success (3645 jobs) | `OriginPassive`: 13 (adds `finiteOrderOn_chartBody_of_binary`, `not_infiniteOrderOn_chartBody_of_binary`) | OK, 5884, no sorry | `claims`, `duplicate`, `lean-manuscript` (2 problems) | failure (gate) |
| 38090784384 (job 114326594532) | `dev-bridge/b11-lemma` @ `00d43da401c0587337901c0b7a21b1f682c493f6` | 22:16:12Z | **failure** (a reserved token `𝒫` in `BridgeLemma`; corrected in the next commit) | — | — | gate skipped | cancelled (the thread cancelled the leftover probe shards) |
| 38092042844 (job 114330283929) | `dev-bridge/b11-lemma` @ `f1c5f0fb3cf8b3c2b37d860c118dad84ee65d218` | 22:36:12Z | success (3644 jobs; `Built OIBridge.BridgeLemma`, warnings only) | `BridgeLemma`: 14/14 | PASS, 5874 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (1 problem) | cancelled (leftover probe shards cancelled after the bridge job completed; the Lean kernel check and 21 shards succeeded) |
| 38093576860 (job 114334767486) | `dev-bridge/b11-lemma` @ `bbbefb72c67c220caece6a3dc43b506fc4197e22` | 23:01:42Z | **failure** (`BridgeDictionary.dict_tens`: termwise `ring` after the sums were reordered; `dict_tens`, `dict_prodState` print `sorryAx`; `monomial_extension_admissible` standard; `BridgeLemma` rebuilt 14/14 standard) | partial, as stated | — | gate skipped | cancelled (leftover probe shards) |
| 38090116254 (job 114324651733) | `dev-equivalence/kn-desc` @ `05b5756c858dd033e9cb77cb91ed34359e7e1ff1` | 22:05:43Z | success | `EqvKnDesc`: 12 | OK, no sorry | `lean-manuscript` only (the branch is cut from L: no `research/archive/`) | failure (gate) |
| 38090924005 (job 114327010280) | `dev-equivalence/omega4` @ `195dfbeeca73fea4a7f7b529f8b7375a38e73869` | 22:18:26Z | **failure** (`EqvOmega4.lean:157:16`, `:215:16`) | the eight declarations built before the failure, as the thread records | — | gate skipped | failure (build) |
| 38091534622 (job 114328799399) | `dev-equivalence/split-l3` @ `8c92343e3a7d21b41a97090271285e0bff591eef` | 22:28:13Z | success (3646 jobs) | `StageSeed` 3, `CopyCovariance` 12, `EqvLevel3` 4 | OK, 5879, no sorry | `lean-manuscript` only (3 problems) | failure (gate) |

Job conclusions, head SHAs, events and timestamps were read from `GET …/actions/runs/{id}` and `…/jobs`; the step
readings (Build, prints, `lean-axioms`) from the Mathlib bridge job logs. The three bridge runs show `cancelled` as the
run conclusion because the thread cancelled the still-running numerical-probe shards after reading its bridge job; the
cancelled shards do not bear on the design modules, but round 3 instructs the threads not to cancel jobs.
