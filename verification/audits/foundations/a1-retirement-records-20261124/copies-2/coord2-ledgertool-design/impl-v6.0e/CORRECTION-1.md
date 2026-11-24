# Correction 1 of the v6.0e implementation

Writer's record, 2026-11-24. This work was local only. There was no push, pull request, GitHub write, CI or dispatch.
The shared object store was only read.

**Authority.** Owner `amaybaum`, 2026-11-24, relayed by the coordinating session. Decision 2 authorizes "the
consolidated implementation correction": B-1, D-1, D-2, D-6, D-7, D-11, D-4/D-10, the nits N-1 to N-5, the caching
notes, the re-pin, the regenerated configuration and the full suite. It requires "one bounded correction commit" and a
focused independent review of that commit against five criteria. Decision 3 approves the closure of ESC-6. No further
design revisions or optimizations are authorized.

## Commit

**3184c7f9075948d8474197eee03ba5b94ba85db5**:
- tree d34231827c150484ba13be7885a072e56310b72d;
- single parent c59b562c168dc24706f51b791ec526dd897c909d;
- author and committer `Claude <<commit-identity-email>>`, signed;
- message ends with the two required trailer lines;
- branch `tools/ledger-coverage-20261123`.

This is exactly one commit, and it includes the class-record re-pin. The re-pin needs no separate commit for two
reasons. The class record pins every landed path except itself. The configuration is not landed. So the generator
was run on the working tree before the commit, and the record entered the same commit.

After the commit, the class record's 53 pins equal `git ls-tree -r HEAD` of the landing paths less the record itself
(53 = 53, every blob equal). The pins are:
- the entry point;
- 42 files under `tools/ledger_coverage/`;
- 9 files in the audit directory;
- `.github/workflows/ledger-coverage.yml`.

The old audit-directory workflow pin is gone.

| File at 3184c7f9 | git blob | sha256 |
|---|---|---|
| `.github/workflows/ledger-coverage.yml` | f17911941279d36a5b4f84c9f706cb17738322c2 | 4206b6b4d08ff43c3a0764dbb9f6aa803be2d9d9e871ff5eeefd975d92abbbe4 |
| `tools/ledger_coverage.py` | 90e96d21fed97f2af9c2c70fa831ae6e13aed390 | a1644e76bfb41f45d0bb95c57770c4701d30d65ec89557cff4b4115c806571f1 |
| `tools/ledger_coverage/engine/checker.py` | d218ec09e6107a0c002cae3e9cd83549af2727db | 91accb1e47998b297c530db3173a0a41613dbb9a00af03f75fc1caa9d91f71b6 |
| `tools/ledger_coverage/engine/schemas/oi-ledger-coverage-5.schema.json` | a8a14c824667872cf4dacba2d4404e94d143f85a | a3ee6813d04a98ee92075e19dec80f8a5cf26433b9182cf484f3654ffacf93a2 |
| `tools/ledger_coverage/adapters/conformance_controls.py` | 07efb49656f224e8dc4b4382a448f6b7adc3a1cc | 0299f9f919005f85f9802019bf95a3e1cab5319ffacd07016c81959823a7ca1f |
| `tools/ledger_coverage/adapters/a1_controls.py` | e2079dfa43e699d090de810bb75f4a41ba217e75 | f438e03eee2a54f2066928552422a059f864432853cf1116f448789789733151 |
| `…/ledger-coverage-tool-20261123/README.md` | 7a02e57247d33c73a49a82ca25ab51196957445e | ed692a77ea4bbda55614610e205d0a5e7667cd90d56e090d02c58f0c23367744 |
| `…/records/side-change-classes-v1.json` | d9f76a1fed447e859935a93697d462c3588c659e | ff31eea1f067848784a246143f46742097407081c9c42bcca68d327fe5058795 |

The path `…/ledger-coverage-tool-20261123/workflow/ledger-coverage.yml` is removed. `git diff -M10%` shows it as a
rename to `.github/workflows/ledger-coverage.yml`. No other file changed: 9 paths in all.

**Staged configuration (not landed).** sha256 **0ba409763b6129fd018cde0c7a5a1c67674b3f8bb25ef5bd8ef43cef79e054f9**,
in `staging-3184c7f9/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json`. It pins:
- the 43 tool files of 3184c7f9;
- `tool.workflow` = `.github/workflows/ledger-coverage.yml` with sha256 4206b6b4…;
- the re-pinned class record.

Its `notes` sentence about `tool.workflow` now names the landed path. Generators: `gen/gen_final_c1.py` and
`gen/gen_config_c1.py`, which are copies of the v6.0e generators that add the one landed path. The generator wrote
into a temporary stage, and the file was then copied to the new folder. `staging/` and `staging-c59b562c/` were not
touched.

## Items

| Item | Change | Evidence |
|---|---|---|
| **B-1** | `checker._uses`: the owner component is `[A-Za-z0-9](?:-?[A-Za-z0-9])*`. Nothing else in the rule changed. EI7 gains three forms in its tool half: `./.github/actions/x@<40 hex>`, `./.github/workflows/w.yml@<40 hex>` (as a job-level `uses:`) and `../x/y@<40 hex>`. The tool half now expects 22 forms. The consumer half (TR28-consumer) evaluates the same three forms beside the original local-action case. | EI7-tool and TR28-consumer PASS. The reviewer's b1a, b1b and b1c are refused, with 0 unexpected across r01-r27, c01, c02, b1* and the new workflow (`logs/corr1/probe/line_rule_c1.out`). Mutants C01-C03 are killed. |
| **D-1** | The workflow is moved (not copied) to `.github/workflows/ledger-coverage.yml`. The README states the exception verbatim, "The tool's landing may add paths only under `tools/`, its audit directory, and the one file `.github/workflows/ledger-coverage.yml`, the workflow that `tool.workflow` pins.", attributed to `amaybaum`, 2026-11-24. The class record pins the file as one exact path, not a prefix; its `prefixes` are unchanged. `conformance_controls.WORKFLOW` and the A1 runner's landed files (`WORKFLOW_PATH`) name the new path. | RT-L2 PASS. Landed paths: 54 (53 tool-landing, 1 class record), none unbound. |
| **D-2** | Inputs: `freeze`, `config`, `check` (type `choice`, 18 values), and the role inputs `h`, `x`, `e`, `m` and `l`. All inputs reach the shell only through `env:` (no `${{` in any `run:`). The run block computes `D="${CFG%/*}"`, sets `set -- --freeze "$F" --config "$F:$CFG" --out "$RUNNER_TEMP/out"`, and runs `case "$CHECK" in` with one fixed `exec python3 -I -S -B tools/ledger_coverage.py …` arm per plan check, every expansion quoted. After `esac` comes `exit 64`. The fetch step is `git fetch --no-tags -- origin "$F"`. The pre-run step is byte-identical to c59b562c's. | Line rule: no problem. The R-e extraction equals the program PyYAML yields, with argv prefix `python3 -I -S -B -c`. `bash -n` on the run block: 0. See `logs/corr1/probe/workflow_yaml_check_c1.out`. |
| **D-6 / N-5** | GV4 case "the HP merge m1": the merge corrupted on disk. Expected: exit 65, no PASS, class `CONFIG_INCONSISTENT` or `UNRESOLVABLE`. | GV4 PASS: exit 65, `CONFIG_INCONSISTENT` "merge 1d55cc32e58c is not resolvable", outcome ERROR. Mutants C09 and C10 are killed. |
| **D-7** | `-S` is compatible: the tool imports only the standard library. The workflow runs the entry point with `python3 -I -S -B`, and the entry docstring and README commands use the same flags. The EI harness runs the entry point with `-I -S -B`. EI6's allowed import directories are the interpreter's `-I -S` path, which is the standard library only. | EI6 PASS: 184 imports, all pinned or standard library, no marker. Mutant C12 (EI runs without `-S`) is killed by EI6, which shows that the narrower predicate bites. |
| **D-11 / N-4** | New control O3-FILTER, from the reviewer's `o3_filter_probe.py`. A global git configuration defines a required smudge filter, and a commit's `.gitattributes` names it. Countercontrol: a plain clone and checkout with the global configuration in force. | `Native.clone` checks out without running the filter, and the countercontrol runs it. PASS. Mutant C07 is killed. The probe itself also agrees (`o3_filter_c1.out`). |
| **N-1** | EI5 case: `M` equals the given first parent and is absent from the store. | EI5 PASS (refused: cannot be read). Mutant C06 (readability clause removed; the review's C16) is now killed. |
| **N-2** | The `/5` schema's `config.required` gains `admission`. `config` is present only in results that reach admission, because `cli.stages` sets both together, so this is the conditional requirement. ACCEPT-SCHEMA checks that the chain result validates and that the same result without `config.admission` gives exactly `$.config: missing admission`. | ACCEPT-SCHEMA PASS. Mutant C05 is killed. |
| **N-3, D-4, D-10** | `IMPLEMENTATION-INVENTORY-r2.md`, a new file that supersedes the old one, which is not edited. "D-18" becomes D-10. The 3a rows for `outcome.py`, `schema.py` and `selftest.py` become "modify". Section 4 corrects D-4's family list: V, S, RT, A, L, G, SW, X and N, 80 entries, verified at 443e871f. Section 5 lists the rows correction 1 changed. | |
| **Caching notes** | `PERF-FIX-r2.md`, a new file. It supersedes the K08 sentence of `PERF-FIX.md`: neither reader's submodule filter in `paths` has an isolating control, at either commit, and no control was added. It also supersedes the runtime and memory table with the reviewer's measured figures: 67bae482 A1 controls 4600.8 s, sweeps 4151.5 s, about 77.8 min, peak 1.20 GB; c59b562c 1180.9 s, 752.9 s, about 20.8 min, 1.48 GB. | |
| **N-4 (implementation review)** | Same as D-11. | |

**`controls.json` is not changed.** Its GV and EI rows are the design's sec. 10.4 text verbatim, which the review
confirmed under D-4. The added cases are owner-authorized extensions, so they are stated in the runner's case and
expected text rather than by rewriting the design's rows. This is recorded as a reading. If the owner wants the rows
amended as well, that is a further change to one file.

**Other changes, all part of the items above:**
- the `ei7_consumer` helper replaces the inline EI7 consumer block, which is needed to run four forms;
- a tool run whose result was never read (`code7, res7 = t7.run(...)`) is dropped with it;
- the module docstring names O3-FILTER;
- `O3-FILTER` is added to `ALL_IDS`.

There are no other code or text changes.

## Escalation (D-2 arm contents): needs the owner or the plan amendment, not decided here

The owner's D-2 decision fixes the form: a choice, quoted env inputs, one fixed command per check. The design's
sec. 11 table does not fully determine every argument of those commands. The arms carry the design's sec. 11
commands verbatim, with these readings:
1. `F:ledger.json` and the other record names are read as files in the configuration's directory at `F`
   (`"$F:$D/…"`, with `D` the directory of `CFG`).
2. Item 2's `--classify F:...` is elided in the design ("F:..."), so the item2-coverage arm has no `--classify`.
3. The design's execution commands carry no `--classify` for the side-change class records. The A1 runner passes
   `--classify` for `records/side-change-classes-v1.json` and the drift classes, so landing-time runs (items 3-14)
   would classify the tool landing only if the plan's command includes it.
4. Items 1 and 2 each have two commands, so each command is its own choice value (`item1-execution`, `item1-terms`,
   `item2-record`, `item2-coverage`).
5. Item 7 has the frozen arm (`item7`, `item7-literal`) and the proposed amendment arm (`item7-amended`).
6. Item 14 has two arms, with and without `--landing`. "Plus the `tex` contract" is read as `--delegation`.
7. A `*)` arm is impossible: a line starting with `*` fails the line rule's anchor/alias clause. So an unknown value
   falls through to `exit 64`, which has the same effect.

The README says that the amended plan's sec. 11 states the commands of record, and that a changed arm is a new blob,
re-pinned by the configuration at `F`. Readings 2, 3 and 1 change what a run checks, and are flagged for decision.

## Full reproduction at 3184c7f9 (`logs/corr1/`)

`logs/corr1/repro.sh` is `logs/perf/repro-after.sh` with:
- the corr1 output directory;
- the staged configuration 0ba40976…;
- the entry point run with `-I -S -B`.

Each step ran under `measure.py`. Head: 3184c7f9. Status: clean.

| Step | Exit | Wall | Peak RSS | At c59b562c (`logs/perf/after-steps.txt`) |
|---|---|---|---|---|
| 1 self-test | 0 | 0.1 s | 25 MB | 0, 0.1 s |
| 2 staged purity lint | 0 (PASS, 0 findings) | 0.9 s | 39 MB | 0, 0.7 s |
| 3 synthetic | 0 | 0.6 s | 29 MB | 0, 0.5 s |
| 4 conformance | 0 (79 PASS, 2 NOT RUN: TR5, G-A1) | 7.4 s | 35 MB | 0 (78 PASS, 2 NOT RUN), 7.3 s |
| 5 A1 conformance | 0 (47 PASS) | 56.9 s | 203 MB | 0 (47 PASS), 57.2 s |
| 6a A1 controls without `--main` | 2 (usage, as before) | 0.1 s | 30 MB | 2 |
| 6 A1 controls, sweeps included | 1 (91 PASS, 1 NOT RUN: RT-T) | 1197.1 s | 1.48 GB | 1 (91 PASS, 1 NOT RUN), 1175.0 s |
| 7 release gate | 1 (the same environment-bound rows) | 92.2 s | 51 MB | 1, 59.6 s; the logs are identical with times removed |

Test counts at 3184c7f9: 347 rows compared, 340 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 4 informational synthetic `_`
fields, 0 FAIL. The rows come from:
- self-test;
- synthetic;
- conformance: 81 = 79 PASS + 2 NOT RUN;
- A1 conformance: 47;
- A1 controls: 92 = 91 PASS + 1 NOT RUN;
- purity.

## Equality against c59b562c (`logs/corr1/compare-c1.json`; `compare_c1.py` is `logs/perf/compare.py` with the corr1 run directory normalized)

Result: 346 controls before and 347 after. **337 identical in id, status and actual. 0 status changes. 0 absent
after. 1 added. 9 differ in `actual` only.** Each difference is explained below.

| Control | Difference | Why |
|---|---|---|
| conformance/O3-FILTER | added, PASS | D-11 |
| conformance/EI7-tool | 3 more forms in `tool` and `rule`, all refused, exit 65 `CONFIG_UNREVIEWED` | B-1 |
| conformance/TR28-consumer | 3 more EI7 cases, all non-acceptance | B-1 consumer half |
| conformance/GV4 | one more case (the HP merge), plus an `outcome` field per case | D-6 |
| conformance/EI5 | one more case, refused | N-1 |
| conformance/ACCEPT-SCHEMA | a `schema` field: chain `[]`, without admission `["$.config: missing admission"]` | N-2 |
| conformance/EI6 | `imports_seen` 191 → 184 (`site` and its imports no longer load under `-S`); otherwise identical | D-7 |
| synthetic/_Y8_engine | the engine's blob hash a7f5da06… → 320a7f07… | `checker.py` and the schema changed |
| a1-controls/K1-GRAPH | `config_edges` (the first 20 of the sorted edge list) gains `.github/workflows/ledger-coverage.yml`, so `engine/__init__.py` drops off the 20-item display; nodes 58, edges 111, no cycle, PASS | D-1: the configuration's `tool.workflow` edge now targets the landed path |
| a1-controls/RT-L2 | landed paths 54, classes `{class-record: 1, tool-landing: 53}`, unbound `[]`, AGENTS.md base-drift reconciled: all unchanged. See the next paragraph for the rest. | D-1 and the changed blobs |

For RT-L2, `logs/corr1/compare_rtl2_c1.py` keys the side changes by path. The positional comparison of
`compare_rtl2.py` shifts when a path is added: that run is kept in `rtl2-c1.out` and shows 112 positional rows. The
keyed comparison (`rtl2-c1.json`) gives:
- 53 predicted-commit ids;
- 7 blobs of changed paths;
- 1 added path (`.github/workflows/ledger-coverage.yml`, class tool-landing);
- 1 removed path (the old audit-directory workflow; the script lists it as "unexplained" only because its rule
  matches a path prefix, and by inspection it is the path D-1 removes).

That leaves 0 unexplained.

The integrity controls are otherwise unchanged in status, and their actuals are identical apart from the rows above:
GV1-GV3, GV5-GV7, GV-CACHE*, EI1-EI4, EI8-EI15, all TR rows, X10, X11.

## Probes against the new rule and the pre-run program (`logs/corr1/probe/`)

| Probe set | Run | Result |
|---|---|---|
| `uses:` rule: v6.0d r01-r27, c01, c02; impl review b1a, b1b, b1c; the new workflow (as c03) | `line_rule_impl.py` on the 3184c7f9 checker | r01-r27 and b1a-c refused; c01, c02, c03 pass; **0 unexpected** (`line_rule_c1.out`) |
| v6.0d pre-run probes: EI8, EI13-EI15, R-d, P4/P7/P9/P10, CX-3 on a branch and on main, refs/heads/main-x, trailing newline, unset `GITHUB_REF`, inner-parent symlink; O-4 cases (EI15) | `run_probes_c1.sh` (the reviewer's script; 3184c7f9 tool, program extracted by R-e from the new workflow, entry `-I -S -B`) | identical to the reviewer's `run_probes_impl.out` apart from the F id and program hash: every refusal case fails before the entry point with no marker, EI8 and CX-3-on-main pass with no marker, and the only marker is the EI15 countercontrol's (`run_probes_c1.out`) |
| CX-3 (`tools/hashlib.py` beside the pinned files) | `cx3_c1.sh`, with `-I -B` and with `-I -S -B` | the shadow module is never loaded; USAGE 64 from the tool (`cx3_c1.out`) |
| YAML reading | `workflow_yaml_check_c1.py` | covered under D-2 above (`workflow_yaml_check_c1.out`) |
| O-3 | `o3_filter_probe.py` on 3184c7f9 | `Native.clone` writes no marker; the countercontrol writes it (`o3_filter_c1.out`) |

## Mutation of the changed code (`mut/runC1/`; harness `mut/scripts/mutate_c1.py`, mutants `mutants_c1.py`)

The 12 mutants ran against self-test, synthetic and conformance of an extraction of 3184c7f9. The audit directory and
the workflow were included, via `checkout-index`. Result: **9 killed, 3 survived.**

| Mutant | Rule | Result |
|---|---|---|
| C01 | owner class as before B-1 | killed (EI7-tool, TR28-consumer) |
| C02 | owner admits `.` | killed (same) |
| C03 | owner admits a `../` prefix | killed (same) |
| C04 | owner may start with `-` | **survived**: there is no hyphen-led owner case; this is outside the B-1 counterexamples, and the local-path refusal is unaffected |
| C05 | schema without `admission` | killed (ACCEPT-SCHEMA) |
| C06 | `resolve_main` readability clause removed | killed (EI5) |
| C07 | delegated clone keeps the global git configuration | killed (O3-FILTER) |
| C08 | delegated clone keeps the system git configuration | **survived**: O3-FILTER exercises the global configuration only, as the reviewer's probe does (a system configuration would need `GIT_CONFIG_SYSTEM` or a system file); extending the control was not authorized |
| C09 | an unresolvable HP merge is skipped | killed (GV4, GV5) |
| C10 | an unresolvable HP merge ends the HP check | killed (GV4, GV5) |
| C11 | EI6's allowed directories from `-I` instead of `-I -S` | **survived, equivalent**: under `-S` nothing loads from the wider set, so the wider predicate cannot be observed |
| C12 | EI runs without `-S` | killed (EI6) |

## Record files

These are new under `impl-v6.0e/`; nothing existing was overwritten:
- `CORRECTION-1.md`, `PERF-FIX-r2.md`, `IMPLEMENTATION-INVENTORY-r2.md`;
- `staging-3184c7f9/…/retirement-config.json`;
- `gen/gen_workflow_c1.py`, `gen/gen_final_c1.py`, `gen/gen_config_c1.py`;
- `logs/corr1/` (`repro.sh`, `repro.out`, `steps.txt`, `full/`, `compare_c1.py`, `compare-c1.json`,
  `compare_rtl2_c1.py`, `rtl2-c1.json`, `rtl2-c1.out`, `probe/`);
- `mut/scripts/mutate_c1.py`, `mut/scripts/mutants_c1.py`, `mut/runC1/`.

`MANIFEST.sha256` is appended, not rewritten.

## Not done

- No push, CI, dispatch or merge.
- The focused independent review of 3184c7f9 against the five criteria is pending.
- Open for the owner: the D-2 readings above, and whether `controls.json` should restate the added cases.
