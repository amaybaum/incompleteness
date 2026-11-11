# Q-C2-1: separate design-run readiness and authorization packet

**NOT AUTHORIZED / NOT YET READY.** This is a reviewable request specification, not a run instruction. The
current owner decision authorizes implementation, non-scientific checks, ordinary PR CI and independent review
only. #1218 remains draft. Exact implementation head/review/CI identities are recorded in append-only #1218
comments; no scientific result or execution approval follows from a green implementation PR.

## Proposed bounded unit

After the outstanding gates below are resolved, request **one design PR run and its required local A3 fixture
preflight** on an immutable source tree derived from the reviewed implementation. Record its exact source/tree
identities and the approved D before approval. The current research-draft SOURCE_BASE is unset; a D-bound source
has a distinct blob. No tree containing the actual workflow splice is published under the implementation unit.

| Resource | Proposed fixed boundary |
| --- | --- |
| Initial S_max | 100000 visited (d-1)-subsets per facet enumeration, solver and verifier independently; already owner-approved for the implementation |
| Local preflight | One A3 fixture command on the exact proposed design source with Python 3.11, within 3600 seconds; then the structural fixture-mode marker; preserve output and exit status |
| Hosted design | One disposable-branch pull_request run with its base branch held at D; job A timeout-minutes 60; job B skipped; no decisive input or dispatch |
| Stress | Exactly the frozen SF-1/20261108, SF-1/1, SF-1/2 and SF-2 counterparts; ST-BP over-maximum exception; frozen fixtures/completions/C-SYM only; no diagnostic benchmark |
| Algorithmic budgets | Design measures them without per-fragment budgets, as specified. General caps are the copied (16,16,100000,200); ST-BP uses its own S_max and SF-2 is uncapped. Final general/B-P triples and B-P caps are computed by the frozen mechanical rule, never selected from decisive data |
| Timeout acceptance | Exact sigma*(W_max^BP + 1203*W_max + 2*W_fix + W_stress) + t_810 <= 1200; sigma derives from the design's integer step times and work records; either hosted job has its own 60-minute limit |
| Repetition | No automatic retry, re-run, second source, extra seed, increased budget or scientific repair run. A red design can return for a separate owner decision under the existing pre-F S_max rule |

The proposal excludes confirmation/gate-test/decisive dispatches, F/E/freeze designation, frozen-splice publication
before authorization, merge, new physical premises and any #866 producer investigation. Those retain separate
decisions. Q-C2-2 stays inactive. #1210's frozen designs and #1216 Backlog are unchanged.

## Required evidence and pre-push conditions

1. Full implementation review of a pinned complete source checkpoint, blocker dispositions, and exact-head green
   ordinary CI. Paper acceptance at f634f8e3 alone does not certify the scripts. Frozen fixture-bearing tests are
   source-defined but remain unexecuted until the separate local A3/design authorization.
2. Resolve and record D, its main activity entry and T0; pin every primary input, including RCH/DSN's required
   landed source paths/blobs. A missing/unset pin fails DS. Do not substitute an authored commit date for T0.
3. Bind SOURCE_BASE to that approved D before the authorized local fixture preflight. Retain a focused source diff
   against the reviewed implementation. Confirm the unchanged four-key refusal, exact imports, no-set/C-INDEP/
   C-IFACE guards and byte-exact inert splice. Record all future design/confirmation/gate/round branches before F.
4. Complete A3 locally before the first checker-bearing recorded-branch push. Preserve its fixture JSON, status,
   Python version and elapsed time; fixture-mode-check must exit zero. Do not cancel job A on recorded branches.
5. Inventory every repository dispatch since repository creation and every other event from the verified T0,
   covering all refs and every attempt with all jobs pages. Split saturated created-time windows, preserve counts,
   read every head tree and each recorded branch's activity, and never turn Forbidden/missing data into empty data.
   The later S1/verdict/final captures still repeat their own required host-time checks.

## Retention and stopping

Preserve the local fixture output, complete design run/attempt/job/step records and times, pull-request base/head
binding, artifact IDs/names/digests/expiry, original archives and extracted files. Keep artifact retention 90 days
and no repository run/log/artifact deletion until Q, **only after the still-pending owner retention commitment is recorded**. File SHA-256 pins hash
preserved bytes; API artifact digests hash archives. Confirmation's A7, not a file/archive digest comparison,
later binds the stress pin. The separate R8/R10 landing checks remain mandatory without an enduring claim about
unretained host content.

Stop before publishing a design tree if local fixture output is missing/non-fixture, a required guard/review/CI
check fails, a source/pin/D/T0/branch prerequisite is absent, inventory is incomplete, or the exact proposed source
diff is not covered by review. After an authorized design, a timeout or red outcome stops the unit. No F is
requested if the mechanical timeout test fails or no successful required confirmation/gate evidence exists.
Host-VOID retakes and checker outcomes retain C.6's distinction; a checker outcome is not an authorized retake.

## Known limits and currently open readiness evidence

- `D` is selected (`cac5d264`, #1169 c.6789676675) and is re-confirmed when the round PR is opened. The execution
  tree, T0, the host inventory, SOURCE_BASE and measured budgets/pins remain unset. RCH/DSN paths/blobs are still required, rather than waived or inferred from drafts.
- The connector's repository-runs endpoint is accessible (a probe found 633 dispatch records). This probe is not a
  complete inventory. One environment's connector rejected the branch-activity endpoint (HTTP 400 endpoint
  allowlist) and its gh fallback returned Forbidden. A read from the writer's environment on 2026-11-11 succeeded
  for the branch `research/arp2-qc21-prep-20261109` only: 30 events (1 `branch_creation`, 29 `push`), a continuous
  before/after chain to `64c0df59`, no `force_push` and no `branch_deletion`. That is branch-scoped evidence; it
  is not the repository-wide history and fixes no T0. No T0 or empty-activity finding is inferred. Any complete inventory assembled later must retain its exact capture scope and attempts evidence.
- Independent B1 REVISE at `2f3a8b83` identified three valid conditional items. The owner approved the exact B1
  C.7/host-checker rule on #1169 c.6784808669: A42 and ARP-1 keeper succeed on dispatch and skip on PR; the KTRANS
  marker is always skipped after the axiom-report step succeeds; every other required job and step succeeds. The
  author-side repair is unreviewed. No blanket skip permission or change to R2's fixture failure semantics.
- The timeout proxy omits P/REP-INV/C/diagnostic runtime **and C-SYM facet enumeration work** and can undercharge larger-rank facet visits. The frozen
  job timeout and incomplete-output stop remain real limits; no performance claim has been measured here.
- The source and selection physical mechanism remains NOT PASSED under #866. This conditional experiment cannot
  promote a simulator benchmark, mathematical factor or scoped witness into a physical OI-to-QM derivation.

No permission question is presented while these prerequisites are unresolved. The owner should approve a fully
identified, reviewed design source and a complete bounded evidence packet, with execution approval as the final
step.

### Execution base

`D` = `cac5d26441dd33e9348151487e4df7b547195481` by owner decision #1169 c.6789676675 (amaybaum,
2026-11-11T07:19:40Z), re-confirmed equal to `main`'s head when the round PR is opened; if `main` has moved, `D` is
then the current head of `main` by the same decision. `controls.py`'s `D_SHA` carries it. The decision fixes D only.
T0 activity evidence, RCH/DSN pins, the source-tree binding (`SOURCE_BASE`, still unset), the retention commitment and
measured budgets remain prerequisite decisions; no design run is authorized. The author-side B1–B5 fixes and N1–N11
dispositions require independent review and exact-head CI before the packet may be proposed for approval.

## B2 gated checker self-test: request prepared, not run

Prepared under the writer task "Request B2 gated run" selected in #1169 c.6789676675, which is "a request to prepare,
not an authorization to execute". **NOT AUTHORIZED.** Nothing below has been executed.

**Purpose.** The B2 repairs (M-SOLVER's SG-1-valid invalid-certificate case; M-BUDGET's out-of-scope B-P, in-budget
valid B-P and reported-only case with `k_fragment_controls` green) exist only as definitions in `t_mutations`. The
isolated harness cannot reach them. They run only inside the checker's own `--self-test` (preregistration A8).

**Command (one attempt).** At the exact reviewed head named in the authorization, from an empty scratch directory
outside the repository, with `<wt>` the worktree root:

```
timeout --signal=KILL 3600 python3 -I -S -B <wt>/verification/programmes/oi-qm/reconstruction/drafts/arp2-qc21/scripts/qc21_check.py --self-test > selftest.out
echo $? > selftest.exit
```

Python 3.11 matches the workflow; the interpreter version is recorded either way. Stdlib only; the checker reads
and writes no file, makes no network or process call, and needs no environment variable.

**What it computes.** `self_test()` runs `t_misc`, `t_decide_paths`, `t_mutations`, `t_mguard_checker`, then the
whole fixture section, and checks the fixture-mode output. Concretely:
- the exact solver and its independent verifier (factorization, reductions, steps 2–4 of C.1 with exact simplex,
  facet enumeration, certificates) on the 13 frozen fixture fragments, each also re-decided at step 4 and by C-SYM,
  with no budget (`P_max`, `B_max`, `W_max` are unset) and the frozen caps; and the M-FACET, M-W, M-MODEL, M-SOLVER,
  M-FACTOR, M-RAY and M-BUDGET mutations on some of these fixtures;
- the CW-P classical-field and QM-P quantum paper models, ATTR-FIX and UPR-BC on synthetic records;
- C's fixture controls (C-STAB, C-R60, C-R60-ODD, C-35, C-S3, C-PLANT, C-CONSX, C-DET, C-STEP, REP-FRAME) and
  STAB-TRUE. These evaluate C's rule maps on 6-cell ring configurations, the native-rule detector and orbit
  statistics on supplied matrices and planted laws, up to horizon 12;
- `native_step`, the substratum's class-N update, on two supplied two-cell states;
- M-GUARD through `s_entry` in fixture mode, and the one counted refusal of `s_decisive`.

**OI-mechanism content, stated plainly.** It **does** execute OI-substratum rule code: `native_step`, C's rule maps
and the native-rule detector. It runs them only on supplied states, matrices and laws, which are fixture-mode inputs
under *Control modes*. It also runs the full exact LP/certificate pipeline on the fixtures. It builds **no** decisive
family: no construction-B simulation (`p_sim`), no P arm classes, no B fragment from OI data, no REP-INV and no C
orbit of an OI rule. All of these are reachable only through the four registered builders, which refuse at their
first statement; M-GUARD checks that refusal. Its fixture section is the same computation as the gated local A3
fixture command (`--event fixture`). Authorizing this self-test therefore authorizes that fixture computation's
content, though not A3 as a recorded preflight.

**Runtime and resources.** Not measured: no part of `--self-test` or A3 has been run. With no budgets, runtime is
bounded only by the caps (`CAP_FACET_SUBSETS = 100000`) and the 3600 s kill limit above. That limit is the same
local bound proposed for A3 and is not preregistered. It is one single-threaded process; memory is unmeasured, and the 3600 s limit bounds wall time only. The run
is executed under an address-space limit of the execution environment (`ulimit -v`, stated with the result);
exceeding it ends the process with a nonzero status, which is not a pass. The limit is an operational
safeguard and is not part of the frozen command.

**What decides (§A.44).** The exit status in `selftest.exit` decides:
- `0`: every check passed, the B2 cases included;
- `1`: at least one check failed;
- `137` (killed at the limit) or any other status: timeout or crash, which is not a pass.

`selftest.out` (one `PASS`/`FAIL <name>` line per check and a count) is a diagnostic and is retained with its
SHA-256 and the exit status. The pass/fail rule is fixed here; no expected counts are stated.

**Stopping.** On any status other than `0`, stop and report; there is no rerun without a new authorization. A pass
is implementation evidence for the self-test's checks at that head only. It is not a fixture record, a design,
stress or A3 record, a pin, or scientific evidence.

**Not authorized by this request.**
- `controls.py --self-test` (A9), `--stress`, `--event` in any form (local A3), and the isolated harness changes it
  might prompt;
- any design, confirmation, gate, S1 or decisive run, dispatch, workflow splice, round PR, F/E or merge;
- recording the output as round evidence or pinning anything from it.
