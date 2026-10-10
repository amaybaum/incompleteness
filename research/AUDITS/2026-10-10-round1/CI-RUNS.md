# CI runs cited by the round-1 threads — verified 2026-10-10 through the GitHub API

The research branches trigger no workflow on push; these runs were dispatched by the threads (`workflow_dispatch`) on
their disposable development branches. On a research branch the release gate is red **by construction**: the `claims`
and `duplicate` steps scan `research/archive/` (present at every thread's base), and `lean-manuscript` refuses a design
module without a census disposition. The meaningful signals for a design run are the Mathlib bridge *Build* step, the
`#print axioms` lines of the module, and the `lean-axioms` gate step. The table records exactly those.

| run | branch @ head | event | created (UTC) | Build step | module declarations on standard axioms | `lean-axioms` | gate red on |
|---|---|---|---|---|---|---|---|
| 38083519826 (job 114305141530) | `dev-equivalence/kinf-seams` @ `f5367a7a532c145ee5dade4799fb97a292d6eb4c` | `workflow_dispatch` | 2026-10-10T20:22:54Z | success (3645 jobs) | `EqvSeams`: 12; `EqvSeamsControl`: 3 | OK, 5875 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (2 problems) |
| 38084161796 (job 114307027913) | `dev-equivalence/kt4-at-l` @ `288f80ecbeb612cbcdb8f5ced8289eadebce7ee5` | `workflow_dispatch` | 2026-10-10T20:32:38Z | success (3654 jobs) | `FourCopyHeadline`: `ie1_all`, `parity_all`, `kt4_general_ie1`, `kt4_forward_ie1`, `kt4_forward_ie1_kt4`, `kt4_forward_ie1_lt` (+ `FourCopyIE1`) | OK, 6015 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (10 problems) |
| 38084486326 (job 114308015615) | `dev-origin/envelope` @ `c3f7fbb21f32587ef3f00d156d58a3743d28ed53` | `workflow_dispatch` | 2026-10-10T20:37:45Z | success (3644 jobs) | `OriginEnvelope`: 12 (`dephase_apply`, `dephase_sum`, `conj_dephase_of_submonomial`, `instAvail_substratum_dephase`, `instAvail_permClass_dephase`, `one_add_I_ne_zero`, `one_sub_I_ne_zero`, `gateFlow_half_not_monomial`, `swap01_invol`, `levelSwap_moves`, `onesClass_mixer_available`, `onesFixing_class_carries_mixer`) | OK, 5871 named results, no sorry | `claims`, `duplicate`, `lean-manuscript` (1 problem) |

Every other job of each run (Lean kernel check, all Numerical probes shards) succeeded. The overall run conclusion is
`failure` because of the gate step, as expected on a research branch. The step-level record was read from
`GET /repos/amaybaum/incompleteness/actions/runs/{id}/jobs` and the job logs from the API on 2026-10-10 (log excerpts:
`Build completed successfully (N jobs)`; the gate table lines quoted above).

These runs are **design evidence**: they certify nothing at L. A result they support is CONJECTURE / [D] until a
governed §A.39 round carries it to `main`.
