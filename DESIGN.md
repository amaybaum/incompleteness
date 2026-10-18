# Cited CI runs: batch extraction of Mathlib bridge output (design, not for merge)

This branch is a design for owner review. Nothing here has been pushed or launched. One push of this branch, at
the commit the owner approves, is the launch.

## 1. The run set, as measured on 2026-10-17

The source is `tranche3.remaining` in `manifest.json` on `wip/ci-evidence-retention-20261017` at `6266ae65`: 366
runs. Of those, the 223 runs whose citing claims rest on Mathlib bridge output (the session's `remaining-class.tsv`)
are pinned in `batchx/runs.json`, sha256 `5436c5b6…`. For each run the file records:
- the run id;
- the attempt-1 bridge job id;
- the head, event and creation time;
- the run's and the bridge job's conclusions, as the runs and jobs APIs gave them in the 2026-10-17 inventory;
- the expiry: creation plus 90 days, the manifest's rule (the repository's own retention setting was not readable);
- the shard.

Every field was cross-checked across the four sources (inventory, jobs list, classification, manifest) when the
file was built.

| | |
|---|---|
| expiry | 2026-12-21 (one run) to 2027-01-13; 123 runs expire 2026-12-22 to 12-28; 148 in December |
| event | 204 `workflow_dispatch`, 10 `push`, 9 `pull_request` |
| bridge job | 128 success, 94 failure, 1 cancelled |
| head commit | 59 on main, 66 on a branch only, 98 referenced by no ref on the host |

**The log lengths were not as stated in the brief.** The brief puts these logs at 7,900 to 8,100 lines. Five were
sampled with the job-log tool, and their `original_length` values were 7,863, 16,993, 36,379, 38,387 and 38,608. A
cold build prints every module's warnings and reports. The extraction downloads whole logs in CI, so the length
does not matter there. It does set the size of a result (section 4).

**Many red bridge jobs are red at the gate, not the build.** For example, run 35714047608's build completed and its
gate failed at `certificate-verifier`. The extraction records a red run as red. It never treats a run's failure as
an extraction failure.

## 2. Output channel (question 1)

What this session can read is a job log served by the job-log tool, at most 5,000 lines. The tool reports
`original_length`, so the session can tell whether a log was served whole. `gh api` refuses job-log downloads. The
Route B precedent downloaded and validated its artifact inside CI, not in the session.

| Option | What the session reads and verifies | API calls | Launches | §A.42 |
|---|---|---|---|---|
| **A. One workflow, a matrix of 32 shard jobs of at most 7 runs, each log under 5,000 lines** | 32 shard logs plus the self-test log, each served whole (checked against `original_length`). `collect.py` recovers each block, checks its SHA256 line, the shard's run set and the global run set, and writes the files. | about 3 per run: 669, plus one uncounted `/rate_limit` per shard | **1** | Results only; no raw log leaves the runner. |
| B. One job per run | 223 logs of about 300 to 550 lines. Under the tool's size threshold they arrive inline, so roughly 100,000 lines enter the context, and 223 reads are needed. | the same 669 | 1 | Same as A. |
| C. Several sequential runs, each a push | the same as A | the same | about 5 (at 4,500 lines each) | Same as A. |
| D. Upload an artifact of results | Nothing directly: by the Route B precedent the zip is read in CI, which needs a second validating workflow whose output must come back through a log anyway. The artifact also stays publicly downloadable for its retention period. | the same, plus artifact calls | **2** | Results only, but it is a write, which the template forbids. |

**Recommendation: A.** It is one push, so one authorization. Every result is read in full by the session, with the
digest of the bytes it was served. One shard's failure leaves the other shards intact. B multiplies session reads by
seven for no gain in isolation, because A already isolates each run (section 4). C costs a push per batch. D costs a
second launch and breaks the template's no-writes property.

## 3. Batching and bounds (question 2)

- **Shards:** 7 runs each, earliest expiry first, 32 shards. Shards 1 to 18 hold every run expiring by 2026-12-28.
  `max-parallel: 4`, `fail-fast: false`. GitHub starts matrix jobs in the order listed, so the earliest-expiring
  shards run first.
- **Size of a shard log:**
  - A worst-case result is 522 lines: a cold build printing all 222 modules, a 25-step gate and 37 jobs (measured on
    a fixture of that shape).
  - Seven of those, with banner, CROSSCHECK, RESULT, verdict and end-of-output lines, come to 3,672 lines (measured on a seven-run
    fixture shard of that shape).
  - `assemble.py` prints at most `LINE_BUDGET = 4200` lines, after every CHECK and RESULT line is counted.
  - The runner adds about 270 lines: 218 for set-up and two checkouts, about 16 for the host step, 9 for the assemble
    step's header and 26 after the verdict. These were measured on the #829 extractor's own log: 4,036 lines, of which
    the assembler printed 3,399.
  - A worst-case shard log is therefore 3,941 lines (measured with those runner lines around the fixture's output,
    and read whole by `collect.py`), and the budget bounds any shard log at 4,469.
    `collect.py` refuses any log of 5,000 lines or more, and any log not served whole.
  - A block that would pass the budget is withheld. Its run becomes UNVERIFIED with the reason named, and its earlier
    blocks still print.
- **Timeouts:**
  - selftest job 20 min;
  - shard job 25 min;
  - every step has its own `timeout-minutes` (checkouts 5, host read 12, assemble 8, self-tests 15);
  - per HTTP request, a 60 s read timeout;
  - per log, a 240 s overall deadline and a 64 MiB cap.
  - Expected wall time is about 8 waves of 3 to 5 minutes.
- **Rate limit:** a `GITHUB_TOKEN` is limited to 1,000 requests per hour per repository.
  - The batch needs about 669 counted calls: per run, the attempt-1 run record, one page of jobs and the logs
    endpoint. The storage fetch is not an API call.
  - Each shard reads `/rate_limit` (uncounted) once, then tracks `X-RateLimit-Remaining` on every answer.
  - Below `RESERVE = 150` it sends nothing more. Each unread item is recorded with stage `rate-limit-reserve`, and
    its run is UNVERIFIED and named.
  - Other workflows running in the same hour share the budget, so launch at a quiet time.

## 4. Fail-closed rules and the run set (question 3)

The per-run verdict concerns the record, not the run: a red build or gate yields HOLDS when the log says so
consistently.

| Condition | Verdict | Printed reason |
|---|---|---|
| log missing; HTTP 404 or 410 on the logs endpoint (expired or deleted) | UNVERIFIED | `log not available (HTTP 410): expired or deleted` |
| any read not made: storage error, cap, deadline, reserve | UNVERIFIED | the stage, the exception type and the HTTP status; never the link |
| log bytes, digest or line count differ from the download record | UNVERIFIED | `does not match its download record` |
| log truncated: runner header not on line 1, or no orphan cleanup in its last 12 lines | UNVERIFIED | `log: complete` |
| unknown format: no single job-name line, no single checkout line, a step that ran without exactly one section, no merge line in a PR log | UNVERIFIED (not FAILS: review note N3 is fixed and mutation-tested) | `format: …` |
| head mismatch: the checked-out commit is not the run's head, or a PR's synthetic merge is of another head | FAILS | `head: …` |
| run record at another head, event, attempt or workflow; attempt-1 run conclusion not the pinned one; bridge job id or name not the pinned one; bridge conclusion not the pinned one | FAILS | `run: …`, `jobs: …` |
| job or step `skipped`, or any conclusion other than success, failure or cancelled | UNVERIFIED | conclusion named |
| Build step success with no build line, or failure with one; Release gate step success without a PASS verdict, or failure with one; a skipped step with a section | FAILS | `build: …`, `gate: …`, `log: …` |
| Build step failed with no `error:` line or error annotation; gate step failed with no verdict line | UNVERIFIED | `cause is located`, `printed a verdict` |
| gate verdict PASS with a FAIL step, or failed with none; a step name repeated | FAILS | `gate: …` |
| job success with a failed step, or failure with none | FAILS | `job: …` |
| an unclosed axiom list | UNVERIFIED | the section's reading is unreliable |
| credential, signed-URL, IP or e-mail shape in the result | FAILS | `output: credential …` |
| block past the line budget | UNVERIFIED | `output budget` |
| malformed run, jobs or fetch record | UNVERIFIED | `malformed record: …` |
| two or more gate blocks in one gate section (the extractor would keep the last) | UNVERIFIED | `gate: at most one gate block` |
| a read the host step never completed: the step was stopped by its timeout. The fetch record is written before the first read and after every read, so completed reads survive | UNVERIFIED | `not read: the host step stopped before it completed` |

**The run-set rule:**
- **Per shard.** The shard's expected runs are the entries of the pinned `runs.json` with that shard number. The
  verdict line `EXTRACT SHARD K/32 HOLDS` requires exactly those runs, each once, each with an explicit HOLDS; any
  FAILS makes it FAILS, and anything else UNVERIFIED. The banner `BATCH SHARD K/32 RUNSET <sha256 of the sorted
  ids> RUNS n` names the set.
- **Global, in the session.** `collect.py` requires:
  - every served log to be whole and under 5,000 lines;
  - an answer to belong to the shard the job index gives its job id. Identity comes from trusted collection
    metadata (the tool's job id and the extraction run's jobs list, every job at the launched 40-hex commit, on
    the launch branch, of this workflow), never from the log's own text. The log can only add shards to those a job
    is involved with, and every place it names one counts: every RUNSET line, the assembler banner, the end-of-output
    marker, the verdict line, and the `runs.json` shard of every RESULT line and block. A damaged, missing or
    reordered banner therefore cannot hide a mislabelled copy;
  - the job rule, decided after every file is read, so neither file order nor shard numbering can change it:
    - a job involved with two or more shards voids every one of them;
    - a job whose answers differ, or with an answer whose banner is missing or malformed, voids its shard
      (UNVERIFIED, none of its runs usable);
    - an answer of a job outside the run fails and voids the shard its banner names;
    - byte-identical copies are taken once;
  - each banner and RESULT set to match `runs.json`, and the assembler banner to name the pinned assembler,
    host-reader and extractor blobs, the extractor's commit and `runs.json`'s digest;
  - a block exactly for each HOLDS run, matching its SHA256 line, canonical, naming that run's job and head, and
    naming in `source` the same pinned blobs and digest;
  - exactly one start marker (the assembler banner) and exactly one end-of-output marker, in that order, the end
    marker naming that shard and the pinned assembler; every RESULT line and block between them; and no
    `CHECK all ...` line between them, which is the assembler's own report that it stopped or that its run set is
    wrong;
  - exactly one verdict line in the whole log: the line just before the end-of-output marker, and the one the
    RESULT lines imply. A verdict-shaped line outside the pair, or an assembler that never printed its end marker,
    refuses the shard;
  - the runs collected to be exactly the 223, each once.

  `collected.json` records, in separate fields:
  - `launched_commit`: the full 40-hex `--head`, which the job index required of every job;
  - `collector`: the commit the collector was run from, the committed blob of `batchx/collect.py`, the git blob and
    sha256 of the bytes actually executed, whether they match the committed blob, and the values it pins;
  - each shard's job id and the extraction run.

  It prints one `RUN` line per run with its expiry and verdict, and ends `COLLECT HOLDS` only when all 223 are
  usable.

**One bad run cannot hide in a batch HOLDS**, because the shard and the batch hold only on explicit per-run HOLDS.
**One bad run does not block the others either.** A run is usable when its RESULT line is HOLDS and its shard passed
every check, whatever the other runs' verdicts. This is a change from #829, where a block was accepted only under a
final `EXTRACT HOLDS` (open question 2).

## 5. What a result records, and classification (question 4)

Every result is `ci/<run>/results.json`, `kind: "cited-bridge"`, `form: "derived"`. It names its commit (the run's
head), run, job, recipe and source digest, and is recorded identically for every run, whatever its class:

- **`run`, `checkout`, `jobs`, `bridge_steps`:**
  - identity and attempt-1 conclusions;
  - every job as `name: conclusion` (claims such as "all eight jobs green");
  - every bridge step;
  - for a PR run, the synthetic merge's base and head. The merge commit's own id is under `observed`.
- **`expected.outcome`:** `gate-verdict`, `build-failed`, `not-built`, `cancelled` or `gate-not-run`.
- **`expected.build_success`, `build_errors`, `failed_targets`, `error_annotations`:** the build's `error:` lines,
  with runner paths removed, and the targets Lake names (claims such as "fails with exactly one source error at
  `ProductStratum.lean:37:61`").
- **`expected.gate`:** the steps, statuses, summaries and verdict, when the gate printed one. These carry claims
  such as "`lean-axioms` at 5251 named results" and "red only at `lean-manuscript`".
- **`expected.markers`:** the four failure markers over the Build and Release gate sections.
- **`expected.axiom_reports`:** for each module with reports in the log, one line: count, axiom sets, and the
  sha256 of its canonical report lines (claims such as "199 of 199 theorems within `propext`, `Classical.choice`
  and `Quot.sound`"). Also `expected.outside_permitted`, every report outside the three, in full.
- **`expected.modules`:** empty, since no receipt governs these runs.
- **`gaps`:** what the result does not carry, named per run:
  - no governed module set;
  - the module set printed depends on the build cache;
  - per-declaration lists are carried as digests;
  - the gate's step list is not checked against `tools/release_gate.py` at the head;
  - the job ended before a gate verdict;
  - every report line the pinned extractor does not parse, as `module:line`.
- **`observed`, `source`, `reproduce`:** log lines and sections, the module count and the synthetic merge; the
  extractor, assembler and host-reader blobs and the log's bytes, lines and sha256; the recipe. The recipe builds
  cold at the head (or rebuilds the PR merge from its base and head), runs the gate, extracts, and compares.

**Classes, as this design defines them.** No definition of "class (a)" was found in the session's files, so these
are proposals for the owner (open question 3):
- **class (a):** the citing claim rests only on what the result carries in full: job and step conclusions, build
  success or its errors, the gate's lines and verdict, the markers, and per-module report counts and axiom sets;
- **not yet classified:** every other run, until its citing lines have been matched field by field.

The extraction is claim-agnostic, so both get the same result. Classification happens in the archive's claims
table. A claim that needs a per-declaration report, or a module the log did not print, is recorded there as not
retained, with the result's named gap. A later, targeted launch can then carry full report lists for the named
modules only.

## 6. Extractor version (question 5)

The pinned extractor is `extract_result.py` from main `b96662e6`, blob `05c41bce`. It is checked at the checkout's
HEAD and tree and by the bytes' blob id before it runs, and its interface (`extract`, `strip`, `MARKERS`, `TS` and the
report fields) is probed. The design does not assume the separate repair lands.

- **Under `05c41bce`:**
  - A report whose declaration name is primed does not match the blob's `REPORT` pattern.
  - An independent loose detector finds every line containing `depends on axioms: [` or `does not depend on any
    axioms` in the Build section.
  - Each such line the extractor did not parse is named in `gaps` as `module:line`. It is never dropped silently
    (mutant 06), and it does not make the run fail.
  - Direct `lean` output does not occur in the bridge job, which runs `lake build`; if it did, the same detector
    would name it.
- **Under a repaired blob:**
  - The self-test checks the invariant on both sides: a primed report is either parsed or named as a gap, never both
    and never neither.
  - It also simulates a repaired `REPORT` pattern in-process and shows that the report is then parsed and the gap
    empties.
  - Repinning is a deliberate change: `MAIN_COMMIT` and `EXTRACT_RESULT_BLOB` in `assemble.py`, plus the two
    checkout refs in the workflow. It needs review like any other change.
  - A blob with another interface is refused before it runs, so every run would read UNVERIFIED rather than be
    misread.

## 7. Self-tests and controls (question 6)

All run in the `selftest` job with no token, before any shard reads anything. All pass locally under
`python3 -I`.

| Suite | Cases | What it covers |
|---|---|---|
| `host.py --self-test` | 51 | 28 allow-list cases (6 allowed, 22 refused shapes); runs-file pin; a clean shard against local servers; the token only as Bearer to the API, never to storage; no leak of link, path, query or token; HTTP 410/404 recorded; rate-limit reserve stops JSON and log reads mid-shard; second redirect; non-https link; JSON redirect refused; no-redirect log; cap; short body; deadline; no token; job-count mismatch |
| `assemble.py --self-test` | 75 | clean shard (green dispatch, green PR, red build), variant invariance, canonical/SHA256, no run-varying content; red gate, cancelled, not-built recorded and held; each fail-closed rule above as a mutation case with its expected verdict and reason; primed name under the pinned blob and under a simulated repair; malformed records; the run-set rule (missing, extra, duplicate, none) and the verdict table; line budget; CROSSCHECK never decisive; blob pin; interface pin; scan; host.py's digest pin |
| `collect.py --self-test` | 85 | whole shards in any order; byte-identical output; a tail or a wrong `original_length` refused; missing and duplicate shard; RUNSET mismatch; missing or extra RESULT; tampered block; a block for a non-holding run; a block naming another head; a verdict line at odds with the RESULT lines; one UNVERIFIED or FAILS run among holders |
| `controls.py` | 71 | the plan and pins, with 16 negative controls. The pins are cross-validated: collect.py's pins of the assemble.py and host.py blobs against the files' blobs; collect.py's `EXTRACT_RESULT_BLOB` and `MAIN_COMMIT` against assemble.py's; and the workflow's two `extract_result.py` checkout refs against `MAIN_COMMIT` (each must be caught); end to end: assemble.py's real output, served whole with a real-shaped runner trailer, is collected byte-identical, a red shard's output is read with its FAILS run named, and a tail is refused; the unmutated copy passes; **50 code mutants across the three scripts, all killed**, including the third review's own M1, M1b, M2, M3, M3b, M4 and M6. Each mutant for a review fix must fail every one of its named regression tests, matched by exact name; a table lists every test each one fails. The `[RP]` tests vary the real order of the answers and the name each is paired with, and pin each scenario's exit code and usable-run count |

CROSSCHECK lines compare each downloaded log with a session observation in `batchx/crosscheck.json`, sha256-pinned.
The observation is `original_length` plus the sha256 of the last 40 served lines, recorded for five jobs that
exercise the main shapes (red gate, red build, cancelled, green PR, latest green). The lines are printed for
diagnosis and never decide a verdict. Every other run prints `not observed in session`.

## 8. Exact launch behaviour

Pushing `tmp/ci-batch-extract-design-20261017` at the reviewed commit starts this one workflow and nothing else. The
tree holds no other workflow.

1. **`selftest`** checks out this branch and main's `extract_result.py` at `b96662e6` (sparse,
   `persist-credentials: false`). It runs the four suites with no token, and fails the workflow before any read if
   any case fails.
2. **`extract`, 32 matrix jobs, 4 at a time.** Each one:
   - checks out the same two trees;
   - runs `host.py` with `GH_TOKEN`, which reads only its shard's attempt-1 run records, job lists and bridge-job
     logs from the pinned endpoints;
   - then runs `assemble.py` with no token, even if the read failed.
3. **What a shard prints:**
   - the banner and RUNSET line;
   - a CROSSCHECK line per run;
   - every failed or unverified check;
   - one RESULT line per run;
   - each holding run's block and SHA256 line;
   - `EXTRACT SHARD K/32 HOLDS|FAILS|UNVERIFIED`, with exit 0, 1 or 2;
   - the end-of-output marker `BATCH END shard K/32: assembler <blob prefix>`, its last line, also on its
     exception path.
4. **What is written:** nothing. No artifact, cache, commit, ref, tag, release, step summary or output, and no
   self-retrigger.

**After the run, in the session:**
1. Read the selftest log and each shard's log with the job-log tool (`tail_lines` 5000).
2. Save the extraction run's jobs list from the JSON endpoint
   `repos/amaybaum/incompleteness/actions/runs/<run>/jobs?per_page=100`. Then run `python3 -I batchx/collect.py
   --runs batchx/runs.json --run-jobs <jobs list> --head <launched commit> --served <each saved answer> --out <dir>`.
3. Commit only blocks that `collect.py` marks usable, in the archive's own tranche change. That change is reviewed
   separately; this branch is never merged.

**One launch covers all 223 runs.** A run left UNVERIFIED (budget, reserve, transient read failure) needs a second
launch with a `runs.json` restricted to those runs: a new commit, a new review and a new authorization. Launching by
about 2026-11-30 leaves three weeks for that before the first expiry on 2026-12-21.

## 9. Open questions for the owner

1. **Archive acceptance.** The archive's checker does not yet accept `cited-bridge`:
   - R4 requires `build_success: true` for a bridge result;
   - R11 fails a `bridge` result of an unattested run at a commit on main;
   - `compare_result.py` reads neither `axiom_reports` nor `build_errors`.

   The tranche that lands these results needs a rule and a comparator for the new kind. Should that be designed now
   or after extraction?
2. **Per-run use.** Should a holding run's block be usable when its shard or the batch is not HOLDS (this design),
   or only under a batch HOLDS (the #829 rule)?
3. **"Class (a)".** Is the meaning in section 5 the intended one? If the owner's classification differs, the result
   content may still suffice, since it is claim-agnostic; only the gap naming would change.
4. **Extractor.** Keep `05c41bce` for this launch (recommended; gaps named), or wait for the repair and repin?
5. **Pull-request checkout line.** Nine runs depend on the line `HEAD is now at <abbrev> Merge <head> into
   <base>`. No full PR bridge log was available to confirm it; the tool serves only tails. If the format differs,
   those runs read UNVERIFIED, not wrong.
6. **Timing and rate.** Launch when no other heavy workflow runs in the same hour? `max-parallel` 4 and the reserve
   of 150 are proposals.
7. **CROSSCHECK coverage.** Five jobs are observed. Extending to all 223 costs about 3k tokens per job at 40 lines.
8. **Off-main heads.** 98 heads are referenced by no ref on the host, and 66 only by a branch. Reproducing those
   results needs the objects retained, as §A.42 item 7 and `check_objects.py` provide. Is that tracked separately?
9. **Branch name.** The trigger names this branch. Launching under another name changes the trigger and the guards,
   which means another review.

## 10. The runs the first launch covers

All 223 runs of `batchx/runs.json`, by shard, earliest expiry first. In the table, s, f and c are the bridge job's
pinned conclusion (success, failure, cancelled), and PR marks a `pull_request` run.

| shard | expires | runs (bridge job conclusion: s success, f failure, c cancelled) |
|---|---|---|
| 1 | 2026-12-21 to 2026-12-25 | 35714047608 (f, PR), 36125130929 (s), 36149801375 (s), 36168400287 (s), 36201832097 (s), 36222012214 (s), 36222335508 (f) |
| 2 | 2026-12-25 | 36235746157 (s), 36235747207 (f), 36241719499 (s), 36243196377 (s), 36243198088 (f), 36244571105 (s), 36244774129 (s) |
| 3 | 2026-12-25 | 36244775311 (s), 36247320536 (f), 36247897586 (f), 36248241812 (s), 36257341185 (f), 36257659584 (s), 36258147032 (f) |
| 4 | 2026-12-25 | 36258396274 (s), 36260031181 (f), 36260347617 (f), 36260577722 (f), 36261156494 (f), 36262031899 (f), 36263052349 (f) |
| 5 | 2026-12-25 | 36263793447 (f), 36264819945 (f), 36265488073 (f), 36266295674 (f), 36266554482 (f), 36267279783 (f), 36268604860 (f) |
| 6 | 2026-12-25 | 36269594164 (f), 36270236955 (f), 36270907147 (f), 36271548391 (f), 36272252074 (f), 36273233977 (f), 36273967096 (f) |
| 7 | 2026-12-25 to 2026-12-26 | 36274601997 (s), 36275377264 (s), 36292921173 (s), 36296861494 (f), 36297196513 (s), 36297226027 (f), 36299395269 (f) |
| 8 | 2026-12-26 | 36299880442 (f), 36300473449 (f), 36303549800 (s), 36308085118 (s), 36308759834 (f), 36309156707 (s), 36310787113 (f) |
| 9 | 2026-12-26 | 36312854482 (s), 36313140818 (s), 36318313840 (s), 36330185755 (f), 36330499550 (s), 36331117696 (f), 36331629574 (s) |
| 10 | 2026-12-26 | 36331881958 (s), 36337348555 (f), 36337705347 (s), 36338026254 (f), 36338078890 (s), 36338320980 (f), 36338368274 (s) |
| 11 | 2026-12-27 | 36373806246 (s), 36377310857 (s), 36377702851 (f), 36378121576 (s), 36378520807 (f), 36379680840 (f), 36379736607 (f) |
| 12 | 2026-12-27 | 36379784064 (s), 36394779889 (s), 36394783617 (f), 36396014114 (f), 36397409142 (s), 36398762851 (f), 36400614526 (f) |
| 13 | 2026-12-27 | 36400756752 (f), 36401680413 (f), 36402777894 (s), 36412115126 (s), 36413005685 (s), 36413016990 (s), 36414030731 (f) |
| 14 | 2026-12-27 | 36416531599 (f), 36417464997 (f), 36418280236 (s), 36430858292 (f), 36431692617 (f), 36439639584 (f), 36440020816 (f) |
| 15 | 2026-12-27 | 36441143645 (f), 36442265583 (f), 36443771320 (f), 36445577768 (f), 36447516037 (f), 36448890710 (f), 36450535104 (f) |
| 16 | 2026-12-27 | 36451750208 (s), 36452360434 (f), 36453414586 (s), 36470083819 (s), 36474528405 (f), 36476760295 (f), 36478152302 (s) |
| 17 | 2026-12-28 | 36542154102 (s), 36573013258 (s), 36596287670 (f), 36598896118 (f), 36599732472 (f), 36609040917 (f), 36612901341 (s) |
| 18 | 2026-12-28 to 2026-12-29 | 36619165282 (f), 36619224682 (f, PR), 36619408800 (s), 36629048484 (s), 36635614122 (s), 36708282201 (f), 36708644229 (f) |
| 19 | 2026-12-29 | 36709510536 (c), 36709850033 (s), 36710673482 (s), 36740471750 (s), 36743809499 (s), 36766630415 (f), 36767218862 (s) |
| 20 | 2026-12-29 to 2026-12-30 | 36767922023 (s), 36777659398 (s), 36832326177 (f), 36832691716 (f), 36834204549 (s), 36834982921 (s), 36835228403 (s) |
| 21 | 2026-12-30 to 2026-12-31 | 36855272075 (s), 36857990743 (s), 36980774530 (s), 36987452281 (s), 36987454767 (s), 37011853989 (f), 37013353037 (s) |
| 22 | 2026-12-31 to 2027-01-02 | 37024002953 (s), 37140734308 (f), 37143464345 (f), 37220522515 (f), 37221543291 (f), 37221769686 (s), 37223131863 (s) |
| 23 | 2027-01-02 to 2027-01-03 | 37226093756 (f), 37226256441 (s), 37226273423 (s), 37232152756 (s), 37235405513 (s), 37236372977 (s), 37261154814 (s) |
| 24 | 2027-01-03 | 37262395333 (s), 37271337107 (s), 37271632718 (s), 37274703967 (s), 37278262616 (s), 37285358151 (s), 37287001071 (s) |
| 25 | 2027-01-03 to 2027-01-04 | 37299337191 (s), 37334884651 (s), 37340470069 (s), 37360536874 (f), 37361193865 (s), 37413453969 (s), 37415025699 (s) |
| 26 | 2027-01-04 | 37418155161 (s), 37434227020 (s), 37434770553 (s), 37437438347 (s), 37446110629 (s), 37467680750 (s), 37468315829 (f) |
| 27 | 2027-01-04 | 37471469288 (s), 37473592066 (s), 37479897974 (s), 37492945459 (f), 37494787556 (s), 37498896443 (s), 37501311098 (s) |
| 28 | 2027-01-04 to 2027-01-05 | 37509405217 (s), 37553717564 (s), 37555310752 (s), 37569163013 (s), 37575788187 (s), 37594392508 (f), 37595568691 (s) |
| 29 | 2027-01-05 | 37608886234 (s), 37619679678 (s), 37643178804 (s), 37646141082 (s), 37648623767 (s), 37659104049 (s), 37693331995 (f) |
| 30 | 2027-01-05 to 2027-01-07 | 37693929094 (s), 37695369269 (s), 37718803221 (s), 37721579646 (s), 37732488729 (s), 37948419430 (f), 37958712227 (f) |
| 31 | 2027-01-07 to 2027-01-10 | 37972004827 (s), 37979649705 (s), 38162504147 (f, PR), 38205087980 (f, PR), 38205760341 (f, PR), 38208044012 (s, PR), 38227812539 (s, PR) |
| 32 | 2027-01-10 to 2027-01-13 | 38250344438 (s, PR), 38250404107 (s, PR), 38733789118 (s), 38752296936 (s), 38782670851 (s), 38808914622 (s) |
