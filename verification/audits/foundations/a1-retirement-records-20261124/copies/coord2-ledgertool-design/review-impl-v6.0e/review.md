# Independent review: implementation of design v6.0e at 67bae482

Reviewer: independent non-author reviewer of the v6.0e implementation, 2026-11-24. Review only; nothing in the tool
worktree was modified and nothing was committed, pushed or dispatched. One REST GET was made
(`repos/amaybaum/incompleteness`, to confirm the pinned `repository_id`).

Object reviewed: commit **67bae482b5842ede9e8430da841bd78563b0f97d**, tree 1689ac2e9a222a40ccc28302654e15d210ec4e6b,
branch `tools/ledger-coverage-20261123`, 8 single-parent commits on 443e871f (verified: `git log --format=%P`, 8 commits,
one parent each). Every run used a copy of that exact tree, materialized from the object store through a temporary
index file under this review's scratch directory; the runners' `--repo` pointed at the shared store read-only, and every
revision was passed as the full id `67bae482…` after the coordinator's notice that the worktree's HEAD would move.

## Verdict

**REJECT** for the exact commit, on one blocking finding (B-1, a one-line fix plus control cases). Everything else
conforms to v6.0e or is an escalated discrepancy for owner decision; the nits below are not blocking. After the B-1 fix
and its control cases, and with the owner's decisions on D-1 and D-2, I expect ACCEPT-WITH-NITS.

## Inputs (verified by sha256 before use)

| Input | sha256 | |
|---|---|---|
| DESIGN-v6.0e.md | 4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131 | match |
| INVENTORY-v6.0e.md | ce3abd51df3ce12b9ee05accf4eb235869c4745556a73ca7c850db771a2720f0 | match |
| impl-v6.0e/EXACT-DELTA.md | 900a03763e0dc6688f65474aa3ab82ba9ebe42319ae17828fd5d0ecdd63bf960 | match |
| impl-v6.0e/MANIFEST.sha256 | e65ee36deacd654849dc0a4d080ae0347d5881ed48942d43912de2f9c87e2e98 | match (see I-1) |
| staged A1 configuration | 5af8f07e5bf5073e5126ab3a03792f34600ae6c0354f7b8453bd6d7d221f9c6d | match at start; overwritten 14:17:39, restored 15:05:03 (I-1); reconstructed byte-exactly |
| coord2-q10/DISPOSITION.md | 7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89 | match |
| impl-stage1-s1/CORRECTION-Q10.md | 44fb8665e7f1ab3663ed0a742e713208c6688fd458e5056abbfbe24c49830c86 | match |

## Blocking finding

### B-1. The `uses:` line rule accepts `./` local actions and local reusable workflows when they carry a 40-hex suffix

**Against:** design v6.0e sec. 6.3 point 5 (R-a): "`^\s*(- )?uses: <owner>/<repo>[/<path>]@<40 lowercase hex>\s*$`,
with literal `<owner>` and `<repo>` names; **this refuses `./` (a local action or a reusable workflow of the same
repository)**". The rule is enforced at the tool (`cli.execution_identity`) and at the consumer
(`checker.accept_with_host`); both call `checker.uses_line_problems`.

**Evidence.** `engine/checker.py` line 40: `_uses = re.compile(r'^\s*(- )?uses: [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(/[^@\s]+)?@[0-9a-f]{40}\s*$')`.
The owner component admits `.` and `..`, so `./…@<hex>` and `../…@<hex>` match. Reproduction
(`probe/line_rule_impl.py` on `probe/wf/`, output `probe/line_rule_impl_b1.out`):

| Workflow blob | Implemented rule |
|---|---|
| the pinned workflow with `- uses: ./.github/actions/x@0123…4567` in place of the upload step (`b1a`) | PASS (no problem reported) |
| a job `uses: ./.github/workflows/w.yml@0123…4567` (`b1b`) | PASS |
| a step `- uses: ../x/y@0123…4567` (`b1c`) | PASS |

The same function reports nothing for these lines, so the tool would not refuse (no `CONFIG_UNREVIEWED`) and the
consumer would not refuse on the line rule. On the runner, a step `uses:` value beginning with `./` is a path in the
checkout (to my reading of the Actions runner, the `@…` becomes part of the directory name, `.github/actions/x@…`);
that would execute a file outside `tool.files`, which point 5 excludes. The GitHub-side consequence is not verified here
(it needs CI); the deviation from the adopted design's stated refusal is demonstrated without it. The v6.0d delta
review's REJECT (B-1) was on exactly this property ("refuses every form the text says it refuses"); the v6.0e design
review's probe used the same character class and did not include a `./…@<hex>` case, so the gap passed both. The
controls EI7 and TR28-consumer pass because the design's EI7 list names `./.github/actions/x` without a suffix.

The pinned workflow at this commit contains no such line (`probe/workflow_yaml_check.out`: line rule clean), so no run
is affected today; the finding is that the check does not deliver the refusal the design specifies for it.

**Smallest fix.** Restrict the owner component to GitHub's owner-name syntax, e.g.
`[A-Za-z0-9](?:-?[A-Za-z0-9])*` (letters, digits, single inner hyphens; no `.`), leaving the rest of the rule as is,
and add three cases to EI7 (tool half and consumer half): `./.github/actions/x@<40 hex>`,
`./.github/workflows/w.yml@<40 hex>`, `../x/y@<40 hex>`. Checked (`probe/line_rule_fix_check.py`, output
`probe/line_rule_fix_check.out`): with that owner pattern, c01, c02 and the pinned workflow pass; r01-r27 and the three
B-1 cases are refused; 0 unexpected. No design change is needed: the design's prose already requires the refusal.

## Test reproduction

All runs from the archived copy of 67bae482, staged configuration 5af8f07e (reconstructed copy for the later runs, see
I-1, I-2), `--main 9deb6956…`. Outputs in `logs/`.

| Step | Writer | This review | Agreement |
|---|---|---|---|
| 1 self-test | exit 0, all PASS | exit 0, 86/86 passed | yes |
| 2 staged purity lint | PASS, 0 findings | PASS, 0 findings | yes |
| 3 synthetic | 36 PASS | 36 PASS (repo = the worktree at 67bae482, clean, before HEAD moved); with my non-git tree as repo, M10 fails as expected (it needs a git worktree) | yes |
| 4 conformance | 74 PASS, 2 NOT RUN (TR5, G-A1) | 74 PASS, 2 NOT RUN; every id and status identical to the writer's file | yes |
| 5 A1 conformance | 47 PASS | 47 PASS (twice: `HEAD` while HEAD was 67bae482, and the full id) | yes |
| 6 A1 controls, non-sweep groups | 89 PASS + RT-T NOT RUN | 89 PASS + RT-T NOT RUN; ids and statuses identical (group times within 5 % of the writer's) | yes |
| 6 A1 controls, sweeps SW1/SW2 | PASS, 4182 s | see "Sweeps" below | |
| 7 release gate | failing rows as S1 (environment-bound) | not re-run (needs the worktree's files; environment-bound rows only) | not checked |

Totals: 86 + 36 + 74 + 47 + 91 = **334 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 0 FAIL**, matching `logs/controls-table.md`
of the writer (with SW1/SW2 counted from the sweeps run below).

**Sweeps.** Re-run independently (`--only sweeps`, separate process, 14:15:36-15:24 UTC): SW1 PASS (697 sites, 401 s), SW2 PASS (584 sites, 3,710 s), no site failing either predicate, group time 4,117 s (writer 4,182 s), with two other processes running on the host. `logs/a1-controls-sweeps.json`.

**Writer's sweeps log.** `impl-v6.0e/logs/full/`: `head.txt` 67bae482, `status.txt` empty (clean),
`staged-config.sha256` 5af8f07e, exits 0,0,0,0,0,2,1,1 as reported, `a1-controls.json` 91 PASS + RT-T NOT RUN with
SW1 697 sites and SW2 584 sites, no site failing either predicate. These files are listed in the writer's manifest and
match it.

### Regression probes of earlier reviews (against the implemented pre-run program and line rule)

| Probe | Run | Result |
|---|---|---|
| v6.0d pre-run probes (EI8, EI13-EI15, R-d, P4/P7/P9/P10, CX-3 branch and main, refs/heads/main-x, trailing newline, unset `GITHUB_REF`, inner-parent symlink) | `probe/run_probes_impl.sh`: the v6.0d harness with the program extracted from the implemented workflow by the R-e rule and the 67bae482 tool | every refusal case fails before the entry point with no marker; EI8 and CX-3-on-main pass with no marker; the single marker is the EI15 countercontrol's (intended: shows the ref test is what refuses). `probe/run_probes_impl.out` |
| YAML reading of the workflow | `probe/workflow_yaml_check.py` (PyYAML) | the `run:` value GitHub would read, shell-split, ends in exactly the program the R-e extraction yields (equal); argv prefix `python3 -I -S -B -c`; workflow sha256 6ea5ee7f… equals the staged `tool.workflow.blob_sha256` |
| CX-3 (`tools/hashlib.py` beside the pinned files) | `probe/cx3_impl.out` | the shadow module is never loaded, exit 0 (at 443e871f the same probe printed `CX3-SHADOW-LOADED`) |
| `uses:` rule on v6.0d `wf/r01-r27`, `c01`, `c02` | `probe/line_rule_impl_v60d_wf.out` | r01-r27 refused, c01/c02 pass, 0 unexpected |
| `uses:` rule on `./…@<hex>` forms | `probe/line_rule_impl_b1.out` | accepted: B-1 |
| O-4 cases (v6.0c) | EI15 above | refused |

### New controls (GV1-GV7, EI1-EI15)

`controls.json` carries GV1-GV7 and EI1-EI15 with `case`, `expect.text` and `by` equal, character for character, to the
design's sec. 10.4 rows (22/22 checked). Read against the code, each control tests what its row states, with these
remarks: GV4's commit case corrupts the segment's first commit, not the HP merge (D-6); GV4 records that `cat-file -p`
refuses a corrupted tree (D-5, confirmed with git 2.43 here); EI6's predicate admits the interpreter's whole isolated
`sys.path` outside the checkout (D-7); EI5 does not isolate the "cannot be read" clause (N-1); EI7 lists only the forms
the design names (B-1); EI10 ran (a C compiler is present) and passed with a live countercontrol.

## Conformance to v6.0e (task 1)

- **Removed machinery.** `engine/authority.py` and `adapters/rest_fixture.py` deleted; no `graphql`, comment,
  thread, deletion-event, file-history, freeze-ledger, authority, `OwnerTimeline`, `auth_schema`, `forbidden`,
  `retirement.owner`, `--plan`, `--round` or `--config-sha256` remains in the engine or entry point (grep). Remaining
  `owner` strings are the ledger's carried column (`row`, `code`, `owner`), scientific data. `oi-owner-authorization/1`
  occurs only in negative controls (CONFIG_INVALID for the retired record kind). `RestHost` reads only
  `/repositories/{id}/actions/runs/{id}`, `…/runs?head_sha=`, `…/runs/{id}/jobs`, `…/runs/{id}/artifacts`.
- **Verified reader** (`engine/gitobj.py`): full ids only; `--no-replace-objects` with `GIT_NO_REPLACE_OBJECTS`,
  `GIT_NO_LAZY_FETCH`, no transport; id recomputed from type, length and content; parents, tree and entries with modes
  parsed from verified bytes; `read` refuses non-regular entries; ancestry and first-parent walks from parsed parents.
- **Admission from F** (`cli.freeze_admission`, `config.read_pin_table`): configuration read only from `F`'s tree;
  `PREREG.md` beside it; last `### N.N Record pins` subsection; header and separator skipped; malformed or duplicate
  rows refuse; configuration and a review record naming its blob must be listed. Run on P's real `PREREG.md`
  (4c79be64): it selects §31.31 and returns the six pins of that subsection.
- **Execution identity** (`cli.execution_identity`, `RestHost._run`): point 1 (run record by run id in the job's
  repository; repository and head repository ids equal `repository_id`; event push or workflow_dispatch; incomplete
  record refuses), point 2 (exact `tool.files` set at `T`, regular files, sha256 pins; workflow path and blob pin;
  checkout compared byte for byte with `T`), point 5 (line rule at tool and consumer; pre-run program in the workflow
  text, run as `python3 -I -S -B -c`), point 6 (`head_branch == main` at the tool; `T` on `M`'s first-parent chain at
  the consumer). `repository_id` 1156244443 equals the repository's REST id.
- **Consumer predicate** (`checker.accept`, `accept_with_host`): `/5`, chain only, no harness marker, recomputed
  PASS, adapter, configuration, `F`, pin table, tool blobs and workflow pins, host run record, `T` = head_sha, `T`'s
  tree from the consumer's store, line rule, first-parent chain, evaluated commits, artifact digest of the exact bytes.
  Any exception is non-acceptance.
- **`/5` schema and `class_meaning`**: the schema requires `class_meaning` as a const equal to the sec. 5 table; the
  entry point's INTERNAL result carries the same table; `outcome.annotate` quotes the meaning in every item and state.
  The schema does not make `config.admission` required (N-2).
- **Entry point**: only `os` and `sys` precede the isolation check; refusal is plain text, exit 65 (R-3); the package is
  loaded by location; nothing inserted into `sys.path`.
- **Class record**: 53 pins, each `{path, git_blob, blob_sha256}` equal to `git ls-tree -r 67bae482` of
  `tools/ledger_coverage.py`, `tools/ledger_coverage/` and the audit directory less the record itself; every blob's
  sha256 recomputed; all modes 100644. The staged configuration's `tool.files` equal the 43 tool files of the commit.
- **Purity**: `interface_names = {'PREREG.md'}` exempts only that exact literal (D-3, probe below).

## Mutation (task 3)

The final survivors were read against the code. Run 2 (1c6dcd09) is code-identical to 67bae482 for the engine and
entry point; ad0d83bf changed two runners (re-tested in run 3), 67bae482 only the class record.

| Mutant | Writer's claim | Assessment |
|---|---|---|
| V05 (Overlay ancestry shortcut disabled) | equivalent | agreed: the base walk returns the same answer; only cost differs |
| I06 (`mode not in regular_modes` check at T removed) | redundant | agreed: `repo.read(T, p)` raises on any non-regular entry and the same refusal (CONFIG_UNREVIEWED) follows; only the message differs |
| C08 (consumer: exact set to subset) | equivalent | agreed: an extra file at `T` raises `KeyError` on `pins_f[p]`, caught as non-acceptance |
| C16 (`repo.resolve(M)` removed from `resolve_main`) | equivalent: an unreadable `M` cannot equal `L`'s first parent, which is read | **not equivalent at the function**: `landing_first_parent` is a caller-supplied id, and reading `L` verifies `L`, not its parent; with `M` equal to that id and absent from the store, the original refuses and the mutant returns `M`. Redundant at system level only, because the consumer's first-parent walk from `M` then fails. EI5's "cannot read" case uses an id that also differs from `L`'s first parent, so it does not isolate the clause (N-1) |
| H03 (failed host read returns `[]` instead of `None`) | equivalent | agreed: both callers (`deleg_host_run`, `deleg_preserve_check`) treat an empty list as missing evidence |
| P01 | survives the harness, killed by Z9h | agreed (`mut/run3/P01-a1-z9.json`) |

Important code paths without a killing control: the `./…@<hex>` forms of the line rule (B-1), and the readability
clause of `resolve_main` (N-1). The mutation runs were not re-run; I relied on the writer's `mut/` results, which name
their source commits.

## Discrepancies D-1 to D-12 (task 4)

| # | Classification | Smallest correction or decision | Guarantee impact |
|---|---|---|---|
| D-1 workflow placement | ambiguity in the adopted design (inventory 3d "written with the implementation" against sec. 12.3 "only under `tools/` and its audit directory"; GitHub reads only `.github/workflows/`) | owner decision; see below. Recommended: land the workflow with the tool at `.github/workflows/ledger-coverage.yml` under a one-path exception, as one file (moved, not copied) | none if done as below; until a copy exists at the pinned path no real run is possible (TR5, EI14 dispatch) |
| D-2 per-check arguments | ambiguity in the adopted design; the implemented `$OPERATION` is the less safe of the readings | fixed, explicitly defined arguments per plan check; see below | not exploitable for a misstated `F`, configuration, `T` or evaluated commit; weakens argument fidelity (recorded command can differ from the intended one, `--repo` dropped from `invocation`) |
| D-3 `PREREG.md` allowlist | ambiguity in the adopted design (sec. 6.3 fixes the literal; sec. 16.1 lists three categories) | accept the fourth category of exactly one value | none: exempts only the exact string `PREREG.md`; `"see PREREG.md"`, `"PREREG"` and the identifier `PREREG` are still flagged by `register-caps` (probe) |
| D-4 `controls.json` has no TR/LN/WB | ambiguity (inventory error) | correct the statement in the implementation record; no code change | none (confirmed): at 443e871f the file held only V, S, RT, A, L, G, SW, X, N ids; TR/LN/WB expectations live in the runners as before; GV/EI rows are verbatim |
| D-5 `cat-file -p` | necessary technical correction (design premise false for trees: confirmed, git 2.43 refuses a corrupted tree with "hash mismatch", prints a corrupted blob) | keep: assert the bytes the store serves to a non-verifying reader, record `-p` | none: the control's point (git itself does not protect the reader) is tested more directly |
| D-6 GV4 class for a corrupted commit | ambiguity (design names the unresolvable-object class; the retained `hp_chain_check` reads the HP merge first and reports `CONFIG_INCONSISTENT`) | accept; add the corrupted-merge case to GV4 with "ERROR 65, no PASS" | none: `hp_chain_check` reads through the verified reader; ERROR 65 either way |
| D-7 EI6 "standard library" | ambiguity in the adopted design (the design's own command `python3 -I -B` runs `site` and the image's `.pth` hooks, which are not standard library) | accept the predicate (interpreter's isolated `sys.path`, nothing inside the checkout); alternatively the owner may choose `-S` on the entry point, which the stdlib-only tool permits, to make the narrower reading hold | none for the guarantee point 5 protects (no checkout file outside `tool.files` executes); the runner image is in the residual trust |
| D-8 in-place re-pin | necessary technical correction (the record is an unlanded draft; `supersedes: null` stays correct) | accept; earlier versions remain in the branch history (443e871f and earlier commits) | none: pins equal `ls-tree` (verified, 53) |
| D-9 TR45 op-C | necessary (environment): needs native delegated runs at `X` and `C` | keep NOT RUN until CI (with G-A1) | none, provided TR45 is reported as `TR45-opB` only, as it is |
| D-10 changes beyond "retain" | necessary technical correction (`/5` and `class_meaning` cannot be produced without them) | accept; correct inventory 3a's "retain" to "modify" in the record; fix the dangling "D-18" in IMPLEMENTATION-INVENTORY (N-3) | none |
| D-11 O-3 without control | necessary technical correction (implements O-3) | accept; add a local control: it is cheap (N-4) | none (strengthens). Verified locally: `probe/o3_filter_probe.py`, a global smudge filter does not run in `Native.clone`; the countercontrol with the global configuration in force runs it |
| D-12 runtime | not a discrepancy with the design; no correction needed for correctness (see Runtime) | none now; the owner's separately authorized cache fix is out of this review's scope | none |

### D-1 in detail (owner's preliminary recommendation: land with the tool under a narrow exception)

Consistent with v6.0e's other rules, with three conditions:

- **Pins.** `tool.workflow.path` is already `.github/workflows/ledger-coverage.yml` and its blob pin is the text's
  sha256 (6ea5ee7f…). Point 2 reads the workflow at that path in `T` = the run's `head_sha`; a copy only in the audit
  directory can never satisfy it. Landing it with the tool makes `T`'s tree hold the tool and the pinned workflow
  together.
- **Pre-run check and point 6.** The step refuses unless `GITHUB_REF` is `refs/heads/main`; the tool refuses unless
  `head_branch` is `main`; the consumer walks `T` on `M`'s first-parent chain. All three require the workflow on
  `main`, whichever landing brings it.
- **R14 and the landing classes.** R14 ("touches no ledgered path") holds: the A1 ledger names 44 files, none under
  `.github/` or `tools/`. But the class record `tool-landing` lists the prefixes `tools/ledger_coverage/` and the audit
  directory only, so a landed `.github/workflows/ledger-coverage.yml` would be an unclassified side change at RT-L2/R19
  unless the record lists it. Add it as one exact path with its blob pin (not a `.github/workflows/` prefix).
- **One copy.** Move the file rather than keep two byte-identical copies (the EI controls' `WORKFLOW` constant then
  names the moved path); otherwise add a control that the two are byte-identical.
- **Launch.** The workflow is `workflow_dispatch`-only, so landing it starts nothing (sec. A.43 item 4).

Exception wording needed (design sec. 12.3, recorded as an owner decision or a design amendment): "The tool's landing
may add paths only under `tools/`, its audit directory, and the one file `.github/workflows/ledger-coverage.yml`, the
workflow that `tool.workflow` pins. It touches no ledgered path (control R14)."

Coupling with D-2: if the workflow's run lines are fixed per plan check (below), they must equal the amended plan's
sec. 11 commands, which do not exist yet. Either the arms are written per operation now (generic, quoted role inputs)
and land with the tool, or the per-check workflow lands with the plan amendment; a later change of the workflow is a new
blob, re-pinned by the configuration frozen at `F`, so landing now does not lock it.

### D-2 in detail (owner's preliminary recommendation: fixed, explicitly defined arguments)

Current line: `python3 -I -B tools/ledger_coverage.py $OPERATION --freeze "$F" --config "$F:$CFG" --out "$RUNNER_TEMP/out"`.

- **Not a shell injection.** Results of parameter expansion are not re-parsed as shell syntax: `;`, `|`, `$(…)`,
  redirections and quotes inside the input are literal words.
- **Argument-parsing risks that remain** (and that `set -f` would not remove): word splitting (no argument can contain
  whitespace); pathname expansion of `*`, `?`, `[` against checkout files; an injected `--` turns the fixed trailing
  options into positionals (USAGE); an injected `--repo DIR` is accepted by every operation and is **dropped from the
  recorded `invocation`** (`cli.invocation` removes `--repo` and `--out`), so the recorded command would not say which
  store was read. The fixed `--freeze`, `--config` and `--out` come last and win (argparse last-wins), and the verified
  reader binds every object to its id, so no input can misstate `F`, the configuration, `T` or the evaluated commits
  that the consumer compares; the risk is fidelity of the arguments, and the dispatcher's free choice of flags such as
  `--profile`, `--scope`, `--rules`, `--classify`, `--segment`, `--hp`, `--final` that select what is checked.
- **Who sets inputs.** `workflow_dispatch` inputs are set by repository writers, who can also choose which check to
  dispatch; fixed arguments remove the free-form part, not that choice.

A fixed-argument design within the sec. 6.3 point 5 checklist (inputs only via `env:`, no `${{ inputs.* }}` in `run:`,
no `if:` after the pre-run check, exact run lines):

```yaml
on:
  workflow_dispatch:
    inputs:
      freeze: {required: true, type: string}
      config: {required: true, type: string}
      check:  {required: true, type: choice, options: [item1, item2, …]}   # the amended plan's sec. 11 check ids
      x:      {required: true, type: string}   # one input per role commit the checks need (X, H, C, L, M …)
…
      - name: ledger coverage
        env: {F: "${{ inputs.freeze }}", CFG: "${{ inputs.config }}", CHECK: "${{ inputs.check }}", X: "${{ inputs.x }}", …}
        run: |
          case "$CHECK" in
            item7) exec python3 -I -B tools/ledger_coverage.py terms --check item7 --final --commit "$X" --freeze "$F" --config "$F:$CFG" --out "$RUNNER_TEMP/out" ;;
            …    ) exec python3 -I -B tools/ledger_coverage.py … ;;   # one arm per check, each the plan's exact command, every expansion quoted
            *) exit 64 ;;
          esac
```

Each arm is reviewable text pinned by the workflow blob; role ids are refused by the tool unless full 40-hex ids
(`gitobj.full_id`) and compared by the consumer with the landing record. No arm passes `--repo`. A note for the
owner: the consumer predicate does not compare the result's `invocation` with the plan's command for the check; with
fixed arms that comparison is unnecessary, with `$OPERATION` it would be needed.

## Runtime (task 5, D-12)

- **Cause confirmed.** A profile of the A1 `coverage` group alone (`logs/prof.out`, cProfile, 35.0 s): `GitRepo.paths`
  46,940 calls, 10.6 s tottime (second to profile matching, 15.8 s); `blob_id` 46,281 calls, 11.2 s cumulative; object
  hashing (`object_id`) 1,028 calls, 0.03 s; `_batch` reads that reach `git cat-file` are bounded by the number of
  distinct objects. Objects are verified once and cached; the dict rebuild is the cost, as the writer states.
- **CI fit.** The A1 step is single-threaded (one core used, not four); 4,647 s (writer) is about 78 min against the
  GitHub-hosted default of 360 minutes, which applies because the workflow sets no `timeout-minutes`; peak 1.2 GB
  against 16 GB. A hosted runner core may be slower than this container's; a factor of 4 would still fit. The CI
  double run of sec. 16.7 is two jobs or two steps; as two steps in one job it would be about 160 min, still within the
  limit. No fix is needed for correctness now; the owner has separately authorized a cache, which is outside this
  review.

## ESC-6 (task 6)

The README's section "References to content not on `main` (sec. A.42 item 8)" classifies each reference in its own
row, with where it is, what reads it and its classification. Each row agrees with the accepted disposition (R1-R6,
sec. 3.1-3.4, sec. 4): the per-rule `recorded_at` of W1/W2 is a gap (ESC-1); the top-level `recorded_at` of w1-w2,
dr-deny and resid is provenance (ESC-5 administrative for dr-deny and resid); register-infinity's two P fields are
provenance and the parameters' stated equality to P's checker a gap (ESC-2); repo-scope's `source.commit` not read,
its claim's support a gap (ESC-3); gr58's tree not read, the classified line only at T1′, a gap (ESC-4); the control
and runner references are provenance; 86d79863 is a computed id. The README's new statement that none of these
references is read by the tool's own admission or execution identity is correct for v6.0e (`freeze_admission` reads
only the configuration, `PREREG.md` and the files its table lists; `execution_identity` reads `T`'s tool files and
workflow). The writer's review of `CORRECTION-Q10.md` is accurate: N-6 (the note's "incorrect for register-infinity,
repo-scope" should be "incorrect for the support of their claims": disposition sec. 3.1 line 102 finds the blanket
label accurate for the record-field reads of R4 and R5) and N-7 (the "v5.5.10 implementation" schedule is stale: v5.5.10
and v5.5.10a were not adopted; the correction is made by the v6.0e implementation) both check against the texts. ESC-6
closes on this independent review of the README correction and of the writer's note review.

## Governance (task 7)

- Added lines of `git diff 443e871f 67bae482` (3,156) and the eight commit messages: no "workspace", local path,
  e-mail address other than the attribution trailers, model id outside the trailers, `closes/fixes/resolves #N`, or
  comment form; the `oi-` strings are schema ids, two of them retired ids used only in negative controls.
- Commit identity `Claude <<commit-identity-email>>` (author and committer); every commit ends with the session's
  `Co-Authored-By` and `Claude-Session` trailers.
- Changed paths: only `tools/ledger_coverage.py`, `tools/ledger_coverage/…` and
  `verification/audits/foundations/ledger-coverage-tool-20261123/…` (`git diff --name-status`).
- Class record pins equal `git ls-tree -r` of the landing paths (53, plus the record itself).

## NOT RUN list (task 8)

The writer's list is complete and each item is justified; every item needing real GitHub stays explicitly
unvalidated until the CI stage:

| Item | Needs | Status |
|---|---|---|
| TR5 (positive control in repository 1156244443) | a run of the pinned workflow on GitHub; also D-1 (the workflow is not at its pinned path) | unvalidated |
| G-A1 (native A1 classes at `X`/`C`, host-run classes) | full clones per tree and host records in CI | unvalidated |
| RT-T | reviewed records (none exist) | unvalidated |
| TR45 op-C part | native delegated runs (G-A1) | unvalidated |
| Y8 as one CI job over two configurations | CI | unvalidated |
| EI14 real branch dispatch | a real `workflow_dispatch` on a branch (simulated by `GITHUB_REF`) | unvalidated |
| O-3 filter effect | none: verified locally by this review (`probe/o3_filter_probe.out`); a control should be added (N-4) | locally validated, no control |
| every real-host REST read (`RestHost`: numeric `/repositories/{id}` paths, `head_repository` presence on dispatch runs, artifact `digest` field, pagination totals) | GitHub | unvalidated |
| CI double run (sec. 16.7) | CI | unvalidated |
| the workflow on GitHub itself (YAML accepted, `persist-credentials: false` fetch of `F` by id, artifact upload) | GitHub; part of TR5 | unvalidated (added here) |
| release-gate environment rows | Lean toolchain, full clone | unvalidated (unchanged from S1) |

## Nits, open items and integrity notes (not blocking)

- **N-1.** EI5's "an id the verified reader cannot read" case (`'1'*40`) also differs from `L`'s first parent, so the
  readability clause of `resolve_main` has no isolating control (mutant C16 survives). Add the case "`M` equal to the
  given first parent and absent from the store".
- **N-2.** The `/5` schema does not require `config.admission` (as `/4` did not); design sec. 5 says the schema makes it
  required. Acceptance is unaffected (`accept` requires mode `chain`). Make it conditionally required for results that
  reach admission, or record the reading.
- **N-3.** `IMPLEMENTATION-INVENTORY.md` cites "discrepancy D-18" for `engine/outcome.py`; the record has D-10.
- **N-4.** D-11's O-3 effect can be controlled locally (the probe above, about a second).
- **N-5.** GV4: add the corrupted HP-merge case (D-6).
- **I-1 (provenance of the implementation record).** At 14:17:39 UTC the staged configuration inside `impl-v6.0e/`
  was overwritten in place by the cache fix's generator (eb778ed5…, pinning that fix's commits), so for a period
  `impl-v6.0e/MANIFEST.sha256` (e65ee36d) did not verify (`sha256sum -c`: the staged configuration FAILED). Per the
  coordinator it was restored at 15:05:03; re-checked at the end of this review: the file hashes 5af8f07e…9c6d again
  and every entry of the manifest verifies. The cache fix's configuration now lies in `staging-c59b562c/`. The 67bae482
  evidence was never affected: the writer's logs name 5af8f07e, and this review reconstructed that file byte for byte
  from the overwritten one and the 67bae482 blobs (`staged/retirement-config-5af8f07e.json`, sha256 verified) before the
  restoration. Recommendation: a generator for a later commit writes only to its own record directory.
- **I-2 (which staged configuration this review's runs read).** Path: the A1 runs started at 14:15:36 UTC
  (A1 controls non-sweep, A1 controls sweeps, A1 conformance re-run) were given
  `impl-v6.0e/staging/.../retirement-config.json`, the path that was overwritten at 14:17:39 and, per the coordinator,
  restored at 15:05:03. The runners read that file exactly once, in the `A1` constructor (`a1_controls.py` lines 88-90,
  `a1_conformance.py` line 579 through the same class), into an in-memory stand-in for `F`; nothing re-reads it. Every
  run result these processes wrote records configuration blob 5af8f07e (A1 controls: 103 runs; A1 conformance: 21 runs,
  plus one run of a deliberately altered configuration variant, 4702e3a3, present identically in the writer's run). The
  sweeps write no run files, but they load the configuration through `config.load`, which verifies every record pin; with
  the overwritten file that load fails with `SOURCE_CHANGED` on the class record (observed in I-3), so the SW1/SW2 PASS
  could not have been produced from it. No doubt remains, and no re-run was needed. The earlier runs (self-test, purity,
  synthetic, conformance, the first A1 conformance) finished before 14:17:39; the purity lint read the file at about
  14:0x and passed with 0 findings. All later runs used the private copy `staged/retirement-config-5af8f07e.json`
  (sha256 verified).
- **I-3.** My first profiling run read the overwritten configuration and failed with `SOURCE_CHANGED` (class record
  pin); it was discarded and re-run on the reconstructed file. No other run of this review used the changed file (its
  results record configuration 5af8f07e).

## Files of this review

`review.md`; `probe/` (line-rule probes and outputs, B-1 workflows, fix check, pre-run regression harness and output,
YAML check, CX-3 output, O-3 probe and output); `logs/` (this review's runner outputs and result files);
`staged/retirement-config-5af8f07e.json` (the reconstructed staged configuration); `MANIFEST.sha256`.
