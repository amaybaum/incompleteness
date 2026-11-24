# Focused independent review of design v6.0c of the ledger coverage tool

Reviewer: independent, non-author. This was a review only. Nothing was written in the repository or
in the tool worktree, and there was no commit, push, GitHub write, GraphQL call or CI run. No host
read was made. Every file this review wrote is under `review-v6.0c/`, and the throwaway probe trees
were made under the session workspace (`rv60c<tmp>/`). The permission system refused no operation.

## Objects verified

| Object | sha256 / id | Result |
|---|---|---|
| `DESIGN-v6.0c.md` | dd72ee5b9f1ed3718b5f1584bf88b957dbb481b0c9ac9dca3d6ff784389aa594 | match |
| `INVENTORY-v6.0c.md` | 86cbe962381a3a25fdaba9387cbf37922fa51d0e892ed075bff2cb76a4eb914c | match |
| `CHANGES-v6.0c.md` | c7d24bc8b1f3b690ac798b308f792716371eaa548af16e48a4712aa139fcf4d2 | match |
| `CHANGES-v6.0c-from-v6.0b.diff` | 4920ce8c2fc4159e16e27ec3cc0bdba5126d7569e4a8fd991ea28c41e4194e79 | match. Regenerated with `diff -u DESIGN-v6.0b.md DESIGN-v6.0c.md`, including the header lines: byte-identical (same sha256) |
| `CHANGES-v6.0c-from-v5.5.9.diff` | 2e37208f49116ebd9f77c70ba105e9aed63183c99e1986c66023cdc09275be26 | match. Regenerated: the body after the two header lines is byte-identical (191a1e9c… on both sides) |
| `DESIGN-v6.0b.md` | f87dd8bee2c0a9d20beaf462351245f4735eaf056ad0485616fe391dacceb452 | match |
| `review-v6.0b/review.md` | 0c41ec5aa395e7971665b156275fbffdb3fee05a283459d11a4bcf0b4a3445aa | match |
| `DESIGN-v5.5.9.md` | cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 | match |
| `coord2-impl-wt` | HEAD 443e871f225a414f69bef3f1e3cab45cb30d6594 | match; clean before and after the probes |
| `AGENTS.md` at 9deb6956 (`origin/main`) | blob sha256 43a28e2653843e8a8ba87e38778cacd6815b71ee54d7977af945303d1783ce27 | read with `git show` |

## Verdict: ACCEPT-WITH-NITS

O-1 (b) is implemented as specified. The pre-run pin check is a fixed inline step,
`python3 -I -S -B -c`, in the pinned workflow. It reads `tool.files` from `F` with `git cat-file`,
walks the entry point and the package with `os.lstat`, and requires the exact path set, regular
files only, and a sha256 equal to each pin. A failure ends the job before the entry point runs.

I simulated that program on probe trees. It refused every tree in which a file under the checked
paths differs from the pins: P4, P7, P9, P10, a changed byte, a missing file, an extra file, a FIFO
and a device node. In each of those trees no planted code ran. On the clean tree the program passes
and the entry point runs.

No planted file outside the checked paths executed: the CX-3 tree, stdlib-named modules,
`sitecustomize`, `usercustomize` and `.pth` files, at the checkout root or in `tools/`.

The nits are applied correctly. The 14 hunks map to O-1, the nits or the owner's bullets, and
nothing else changed. No authorization machinery returns.

There are no blocking findings. One open item, O-4, is put to the owner. Under it, the program's
reference values come from the `F` the run is given. It is not an acceptance route, but it bears on
the owner's sentence "An unverified file must not execute" (see below).

## The key question

*"Could an incorrect scientific result pass under the revised design when it would have been
rejected under v5.5.9 for technical reasons?"*

**No.** I found no such case. v6.0c is stricter than v6.0b in every case below and does not move
acceptance relative to v5.5.9.

| Case | v5.5.9 | v6.0c | Evidence |
|---|---|---|---|
| CX-1: engine module changed at `T'` | refused (pins in `A`) | the pre-run check fails before any tool code runs (sha256 differs); at the tool, TR28; at the consumer, refused from its own store | probe "EI13 one byte changed" |
| CX-2: a changed workflow writes a forged result | refused (TR15, TR50) | refused at the consumer by TR15 and TR50 against `tool.workflow`. The run is not of the pinned workflow, so the pre-run check does not apply to it | design text; unchanged |
| CX-3: unpinned `tools/hashlib.py` on a branch `T'` | refused (TR29) | the pre-run check passes and the file never executes. ERROR at the tool (`head_branch`); non-acceptance at the consumer (TR29) | probe "EI14": no marker |
| CX-4: a `./` local action or reusable workflow; a script in `T` | refused off `main` (TR29); on `main`, review only | EI7 at the tool and the consumer; the workflow checklist; TR29 | design text |
| P4: an unchecked-hash `.pyc` | executed in the run, then refused | the pre-run check fails on the extra path; never executed | probe EI9. Countercontrol: without the pre-run check, the marker is written |
| P7: an extension module `util.so` | executed, then refused | the pre-run check fails; never executed | probe EI10 |
| P9: a symlinked pinned module | executed, then refused | the pre-run check fails (non-regular entry); never executed | probe EI11 |
| P10: a symlinked entry point | executed, then refused | the pre-run check fails; `evil.py` never runs | probe EI12 |
| A branch `T` with pins equal | refused (TR29) | ERROR at the tool (`head_branch`) and non-acceptance at the consumer (TR29) | design text |

## Blocking findings

None.

## Open item for the owner

### O-4. The pre-run check's reference is the `F` the run is given (demonstrated; not an acceptance route)

**Case.** A `workflow_dispatch` run of the byte-identical pinned workflow on a branch `T'` that
carries changed tool code. The dispatcher supplies `F'`, a commit whose configuration pins that
code. Any commit the fetch can reach by id qualifies. The design does not require `F` to be a full
40-hex id in the step, so `HEAD` would also be read.

**Result.** The pre-run check passes and the changed module runs. Probe "O-4": the marker is
written. With the plan's `F` the same tree fails (countercontrol).

**Why it is not blocking:**

- **No acceptance.** EI3 refuses at the consumer, because `F'` differs from the landing record's
  `F`. TR29 also refuses, because `T'` is off `main`. The tool's own `head_branch` ERROR comes
  only after the changed code has run.
- **Equal privilege.** The case needs write access, which can already push a different workflow
  to a branch and run any code in CI.
- **Not demonstrably a v5.5.9 regression.** v5.5.9's workflow clause ("verify the tool blobs
  against `engine_pins` before executing") does not say where the workflow read `A`. The tool read
  `A` from `main`, but the workflow could have read the copy in the checkout, which a branch
  controls.

**Bearing on the owner's sentence.** Read strictly, "An unverified file must not execute" means the
files must be verified against the plan's pins. Under that reading, the gap is that the pre-run
check verifies against a run input instead.

**Smallest fix, if the owner wants it: one or two lines in the inline program.**

- Refuse unless the environment value `GITHUB_REF` is `refs/heads/main`. The runner sets it for the
  run, and the checklist already forbids `GITHUB_ENV` writes.
- Refuse unless `F` matches `^[0-9a-f]{40}$`.

**What the fix gives:**

- In every run of the pinned workflow, only code merged on `main` can execute.
- The tool-level branch check now precedes all tool code, not just its evaluation.
- It removes F-18's ambiguity. `head_branch` is also the tag name for a run on a tag named `main`
  (inferred, not checked on the host); `GITHUB_REF` tells a branch from a tag.
- No new host read and no new trust root.

It is optional under this review's stopping rule.

## Nits (non-blocking)

- **R-a. The `uses:` rule's detection method is unstated, and EI7 does not test the forms N-b
  names.** The text says that quoted keys, flow mappings, block scalars and aliases refuse. EI7
  tests only `./`, tag and branch forms.
  - A double-quoted key written with an escape, `"\x75ses": ./x`, contains no literal `uses`. A
    standard YAML parser (PyYAML here) reads it as `uses`, so a line detector misses it.
  - Fix: add to EI7 a quoted key, a flow mapping, an alias and an escaped key. Add to the checklist
    "no quoted or escaped mapping keys, flow mappings, anchors or aliases anywhere in the blob",
    since the content review is the backstop for those.
  - This is not a weakening: v5.5.9 had no mechanical `uses:` check.
  - I did not verify whether GitHub's parser accepts escaped keys.
- **R-b. Checklist additions.** Each is one line and keeps the step's "failure ends the job"
  meaning:
  - no `continue-on-error`, and no `if:` on the steps after the pre-run check;
  - no reusable workflow. The `[/<path>]` form admits one, and its own steps are not under the
    checklist.
- **R-c. Wording.**
  - Point 5 calls the pre-run check "the first step after the checkout", but the checklist puts the
    fetch of `F` before it. Say "after the checkout and the fetch of `F`".
  - Point 1 lists the run-record fields it reads without `head_branch`, which point 6 says "point 1
    already reads". The field is in the same REST response, so no read is added; list it in
    point 1.
  - Inventory table 6 row P8 still says the workflow "runs only the entry point and fixed `git`
    commands"; its last sentence then adds the pre-run check.
  - Sec. 15 item 10 still says "the owner's requirement 5", which belongs to the earlier decision.
- **R-d. Parent components.** The step does not use `lstat` on `tools` itself. A tree whose `tools`
  is a symlink, to `real/` or to an absolute path outside the checkout, passes the step.
  - Probe: only pinned bytes run, so nothing unverified executes.
  - At the tool, point 2 refuses such a `T` (its tree lacks the pinned paths, TR28), and the
    consumer refuses it too.
  - Optional: one line requiring `tools` to be a real directory.
- **R-e. EI8-EI13 runner.** Inventory table 3b assigns them to `conformance_controls.py`, which
  takes "the pre-run check's program from the workflow text". The workflow does not exist yet
  (table 3d), and the rule for extracting the program from the blob is not stated.
  - Fix: one sentence fixing it, for example the single `run:` line of the step named `pre-run pin
    check`.
  - EI9 must build its `.pyc` for the running interpreter's cache tag.
  - As assigned, the controls are runnable once the workflow exists; my probe runs the same cases
    on materialized git trees.

## O-1 (b): does the step verify every file that can execute, in every run of the pinned workflow?

**Yes, relative to the `F` it is given** (O-4 qualifies the reference). Evidence by case
(`probe/run_probes.out`, Python 3.13.18, git 2.43.0):

| Probe | Result |
|---|---|
| EI8 clean tree | pre-run OK, 45 files; entry point runs (exit 64 for `--help`) |
| EI9 (P4), EI10 (P7), EI11 (P9), EI12 (P10) | pre-run FAIL; entry point not run; no marker |
| EI13: one byte changed, missing file, extra `.py`, FIFO, char device, unknown `F`, configuration absent, no `tool.files` | pre-run FAIL in each case; no marker |
| F-19: run without inputs | pre-run FAIL ("F and configuration path required") |
| case-variant `engine/Util.py`; NFD-named extra file | pre-run FAIL (extra path) |
| hard link to an outside file: same content / other content | OK (pinned bytes) / FAIL (sha256) |
| symlinked parent `tools`, to `real/` or to an absolute outside path | OK, and only pinned bytes run (R-d) |
| empty extra directory | OK; it holds no code (git cannot record it) |
| EI14 (CX-3 plus `tools/{hashlib,re,subprocess,json,stat,os}.py`) | OK; entry point runs; no marker |
| F-16: stdlib-named modules, `sitecustomize`, `usercustomize`, `encodings.py`, `.pth`, `tools/importlib/` at the root and in `tools/` | OK; entry point runs; no marker |
| `sys.path` of `-I -S -B -c` in the checkout | stdlib zip, stdlib, lib-dynload only (no `''`) |
| `sys.path` of `-I -B` | adds the image's site-packages only; no checkout entry |
| N-g: entry point without `-I` (separately `-B -S`, `os` not preloaded) with `tools/json.py` and `tools/os.py` | exit 65 `ERROR isolation`; no marker (`os` is a frozen module) |
| O-4: changed module with a caller-chosen `F'` | OK; marker written. Countercontrol with the plan's `F`: FAIL |

**F-16 against "An unverified file must not execute".** An unchecked file outside the checked paths
is present but cannot execute:

- Neither interpreter invocation puts any checkout path on `sys.path`. Isolated mode omits the
  script directory and `''`; `-S` or the image's own site paths cover the rest.
- The entry point loads only its package, by location.
- `.pth` files are read only from site directories, and `sitecustomize` and `usercustomize` only
  from `sys.path`.
- The `git` commands read `.git/config`, which checkout writes and the tree cannot supply.
  `cat-file blob` applies no attribute filters.
- The delegated checker runs (N-h) are outside the rule and unchanged from v5.5.9.

F-16 is acceptable. Widening the scan to all of `tools/` would refuse the repository's other tools
and add nothing.

**TOCTOU.** Steps run sequentially in one job. The checklist fixes the run lines between the check
and the entry point to none, and checkout leaves no process behind, so no writer exists between the
two. The residual is host-runner trust, already stated as F-15.

**The step's own reliance.** The step relies on the runner's `python3` (from `PATH`, which the
checklist protects) and `git`. This is the same host-runner trust (F-15) that the entry point
relies on, and no file of the checkout is involved.

**Simplicity.** About 25 lines of standard library in the pinned workflow text. It adds no new
read, trust root or infrastructure. Not adding the entry-point package scan (F-17) is right: it
would be a second mechanism for the same property. Point 2's own checkout comparison is now
redundant inside workflow runs but still serves direct runs (EI1). Keeping it is harmless.

## Nits N-a to N-h

| Nit | Applied | Check |
|---|---|---|
| N-a counts | yes | Recounted with `diff -u`: v6.0c from v6.0b 14/39/100; from v5.5.9 45/596/518; v6.0b from v6.0a 30/86; v6.0b from v5.5.9 596/457; v6.0a from v6.0 106; v6.0a from v5.5.9 594; v6.0 from v5.5.9 577/312. All equal CHANGES and F-20 |
| N-b `uses:` rule and checklist | yes | The rule is fail-closed on lines. Gaps are R-a and R-b. Point 5 now names "the actions it names by commit id" |
| N-c tool-level ERROR | yes | `head_branch` from the same run record; TR29 first case restored to ERROR at the tool and non-acceptance at the consumer. The consumer's walk of `M` (sec. 5 predicate, point 6, TR29) is unchanged and binding. F-18 is correct. O-4 offers a stronger and earlier form |
| N-d sec. 5 wording | yes | "points 1-3, the `uses:` check of point 5, and point 6", matching point 4 and point 6 |
| N-e stale EI1-EI5; runners | yes | Inventory tables 1a, 2 (S13), 3b and 3c now say EI1-EI14. Runners named: subprocess runs for EI6 and EI8-EI14, workflow blobs for EI7 (R-e) |
| N-f G23a disposition | yes | G23a cites both v5.5.9 clauses and their v6.0c homes |
| N-g ordering | yes | Wrapper text, EI6 second case and inventory 3a: "only `sys` and `os` precede it". Probe confirmed |
| N-h delegated runs | yes | Point 5 excludes them, governed by sec. 7 as in v5.5.9 |

## New controls EI8-EI14

Each control tests what it claims, and my probe reproduces each expected outcome.

- **EI8** is the needed positive control.
- **EI13**'s "a directory entry that is neither a regular file nor a directory" is testable with a
  FIFO, which needs no root.
- **EI14**'s expectation matches the probe: the step passes and nothing executes. The tool and
  consumer refusals rest on TR29 as stated.

They are runnable as assigned once the workflow exists (R-e).

## Hunk map (v6.0b to v6.0c)

All 14 hunks were read in the regenerated diff. The `CHANGES-v6.0c.md` table is accurate.

| # | Content | Source | Verified |
|---|---|---|---|
| 1 | title; v6.0c status bullet quoting the review and the owner decision | owner decision | yes. Adoption is stated as procedural; the quotation is verbatim against the task brief |
| 2 | v6.0b bullet loses its authority sentence (moved to 1) | traceability | yes |
| 3 | identifiers EI8-EI14 | owner decision (nits) | yes |
| 4, 9 | `INVENTORY-v6.0c.md` pointer; EI1-EI14 | traceability, N-e | yes |
| 5 | 0.2 row for review v6.0b | traceability | yes |
| 6 | wrapper: isolation check precedes every non-preloaded import | N-g | yes |
| 7 | sec. 5 consumer wording | N-d | yes |
| 8 | point 5 (scope, N-h exclusion, pre-run check, import-path wording, N-g, N-b rule and checklist); point 6 `head_branch` | O-1 (b), Q-1, N-b, N-c, N-g, N-h; owner bullet "verify executable dependencies before the tool runs" | yes |
| 10 | TR29 first case | N-c | yes |
| 11 | EI1 scope, EI6 ordering, EI8-EI14 | O-1 (b), Q-1, N-g; owner bullet "retain the independent consumer checks" (EI1, EI14 name TR28, TR52, TR29) | yes |
| 12 | sec. 15 item 10: focused review | owner decision | yes (R-c on "requirement 5") |
| 13 | sec. 15 item 12: the pre-run check in the plan's workflow | plan item P8 | yes |
| 14 | S13 acceptance list EI1-EI14 | owner decision | yes |

Nothing else changed.

**Authorization.** The added lines that mention approval or the owner are the quoted decision, the
procedural adoption sentence and the review item. The pre-run check compares bytes with pins and
reads no comment, designation or approval. No added wording implies that a passing step or a PASS
means approval.

## Row check

I keyed rows by their first cell (`rows/rows_cmp.py`, the prior reviewer's script, re-run).

**v6.0b to v6.0c** (`rows/rows-v60b-v60c.txt`):

- 501 rows retained, 4 modified (TR29, EI1, EI6, S13), 8 added (the 0.2 row and EI8-EI14), none
  removed. This equals CHANGES.

**v5.5.9 to v6.0c** (`rows/rows-v559-v60c.txt`):

- 439 retained, 34 modified, 71 removed, 40 added.
- Control ids: 28 modified and 58 removed, matching inventory table 2.
- The 58 removed ids are exactly the retired list: O4, TR4, TR6-TR12, TR16-TR27, TR31-TR44, TR47,
  TR49, TR53-TR70, LN9, LN11, LN12.
- The new control ids are GV1-GV7 and EI1-EI14.
- The inventory's table-row figures (422/40/65/29) use line-by-line keying and differ only by
  method, as in the prior review.

**Identifiers:**

- EI8-EI14 appear in no earlier design or v5.5.10/v5.5.10a file. Only the v6.0c work files carry
  them.
- TR29's first case keeps its v5.5.9 text, and its outcome returns to v5.5.9's ERROR / non-acceptance.
- EI1's and EI6's cases are unchanged in meaning: EI1 is scoped to direct runs, and EI6's timing is
  made precise.
- No id is reused with a changed meaning.

## Flag verdicts

| Flag | Verdict |
|---|---|
| F-16 | **Acceptable.** The file is present but cannot execute (probes EI14 and F-16); TR29 refuses at the tool and the consumer |
| F-17 | **Acceptable.** The pre-run check covers the same entries before any tool code runs |
| F-18 | **Acceptable as stated** (host-attested; the consumer's walk binds). Note the tag-name ambiguity (inferred); O-4's `GITHUB_REF` line would remove it |
| F-19 | **Correct.** Probe: no inputs, step fails. A `push` run cannot reach the entry point. `workflow_dispatch`-only is left to review (§A.43 item 4, §A.50 item 2) |
| F-20 | **Correct.** Every figure recounted (table above) |

## Guarantees against v5.5.9

The guarantees G1-G23a of inventory table 4 were checked for the rows v6.0c touches:

| Guarantee | Change in v6.0c |
|---|---|
| G2 (executed code equals pins) | strengthened: refused before execution in pinned-workflow runs |
| G23 (`T` on `main`) | the tool-level ERROR is restored |
| G23a | both v5.5.9 workflow clauses now have explicit homes |

No other row changed between v6.0b and v6.0c. The independent consumer checks (point 4, TR28,
TR51, TR52, TR29, EI3) are unchanged.

## Governance

AGENTS.md at 9deb6956:

- **§A.42.** Unchanged from v6.0b: `T` is on `main`. O-2 (the reachability of `F`) stays open.
- **§A.44.** The pre-run step's verdict is its exit status and the job's conclusion, which is
  structured evidence.
- **§A.43 item 4 and §A.50 item 2.** A dispatch that uses plan records is a trial needing owner
  approval each time. The step adds no launch.
- **§A.49.** The step writes nothing to GitHub.
- **§A.45.** No Issue or comment is read.
- **No AGENTS.md amendment is needed.**

## Verified vs inferred

**Verified:**

- all hashes, both regenerated diffs, and all line counts;
- the hunk map and both row comparisons;
- the identifier checks;
- the probes in `probe/run_probes.out`, simulating the described program and the v6.0c entry point
  on copies of 443e871f's tool files in throwaway git repositories;
- PyYAML's reading of escaped and quoted `uses` keys;
- AGENTS.md §A.42-§A.51 at 9deb6956.

**Inferred (not executed on a hosted runner):**

- GitHub's YAML handling of escaped keys;
- `head_branch` for tag refs;
- `GITHUB_REF` values and their non-overridability;
- that `actions/checkout` starts no lingering process;
- runner step sequencing.

## Files

- `review.md`
- `probe/`: `prerun.py` (simulated inline program), `entry_v60c.py` (simulated entry point),
  `run_probes.sh`, `run_probes.out`; `marker_mod.py`, `make_pyc.py` and `ext_util.c`, copied from
  the v6.0b review's probe
- `rows/`: `rows_cmp.py`, `rows-v60b-v60c.txt`, `rows-v559-v60c.txt`
- `MANIFEST.sha256`
