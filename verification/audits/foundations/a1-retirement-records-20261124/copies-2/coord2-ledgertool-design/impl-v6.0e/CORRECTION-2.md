# Correction 2 of the v6.0e implementation

Writer's record, 2026-11-24. Local work only: no push, pull request, GitHub write, CI or dispatch. The shared object
store was only read (`read-tree`/`checkout-index` into a temporary index file under the scratch directory; no fetch,
gc, prune, worktree prune or merge-tree).

**Authority.** `OWNER-DECISIONS-CORR2-20261124.md` (sha256 6bb934c1…a9ed, verified), owner `amaybaum`, 2026-11-24:
R-B1 option (a), D-2 option (b) "including --certified C", the four `controls.json` rows, the C04 and C08 tests, C11
through R-B1, the nonblocking observations recorded only, re-pin, new staging directory, full suite; one bounded
commit on 3184c7f9; the frozen plan P and the amendment files not edited. Basis: `review-corr1/review.md` (sha256
3b99a089…a68f, verified). Method followed: `CORRECTION-1.md` (3352a14e…9213, verified).

## Commit

**4f4a9d58fd0bf41289a4904c9b39c00c711c9093**
- tree 82276267baa5518d3d2466b08bc0c88a4bdd1f02; single parent 3184c7f9075948d8474197eee03ba5b94ba85db5;
- author and committer `Claude <<commit-identity-email>>`; SSH-signed with the key that signed 3184c7f9 (the public-key
  block of both signatures is byte-identical; `ssh-keygen` is not installed here, so no local cryptographic verify);
- message ends with the `Co-Authored-By` and `Claude-Session` trailers; branch `tools/ledger-coverage-20261123`.

Committed text check over the 200 added diff lines: no local path, "workspace", e-mail address, model id,
`closes/fixes/resolves #N`, CR or invisible/control character. Paths changed: 5, all landing paths.

| Path | git blob | sha256 | Scope item |
|---|---|---|---|
| `tools/ledger_coverage/adapters/conformance_controls.py` | aebc46d6c18a490bf0f16eb2ff1452d0bbf96987 | db1d6ade3704c988c2baf6e920116121b3d2c783009d940f853265db7169c151 | 1 (EI6 predicate, negative control; C11), 4 (C04 EI7 form; C08 O3-FILTER system case, docstring) |
| `.github/workflows/ledger-coverage.yml` | db4bc1fe95711aad63ef4f601db642e747f1d3d8 | 6014639279ad5725bedcb5573c1819be27b941265e617715f517ed9605b00052 | 2 (D-2 arms, input `c`) |
| `…/ledger-coverage-tool-20261123/README.md` | 9229ce1c656f7c07956636bf0885574a1b9b1a93 | 03f16ba6b49fe4d44cf322bc438e2c01495b943735b3069dd43d906c72eb8edf | 2 (necessary propagation: the sentence "with record paths taken from the configuration's directory at `F`" became false under D-2 (b); one sentence rewritten, nothing else) |
| `…/ledger-coverage-tool-20261123/controls.json` | ddeb43c6e1ad3e6cb9095790779eb2218590faaf | 96f3032097e817f33803d62e75b4055cb2f6111b29dc3a3ed58cb3e4115ce3d8 | 3 (rows EI5, EI6, EI7, GV4 only; every other key and row byte-equal after parse, same serialization) |
| `…/records/side-change-classes-v1.json` | b54b003a29ea9e6961205bf20597f4002da014db | 81af503355585660715e5549a6f1ad2164e142253b6cf7b52cca561755ead216 | 6 (four pins re-pinned: the four files above) |

Class record after the commit: 53 pins equal `git ls-tree -r 4f4a9d58` of the landing paths less the record itself
(entry point, 42 under `tools/ledger_coverage/`, 9 in the audit directory, the workflow); every `git_blob` and
`blob_sha256` matches; prefixes, reason and status unchanged.

**Staged configuration (not landed).** sha256 **5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0**,
`staging-4f4a9d58/verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json` (new directory;
`staging/`, `staging-c59b562c/`, `staging-3184c7f9/` untouched). Generators `gen/gen_final_c2.py` and
`gen/gen_config_c2.py`, copies of the `_c1` generators with only their docstring (and the called file name) changed,
written to a temporary stage and copied. Against `staging-3184c7f9/` it differs exactly in: the class-record pin (two
places), `conformance_controls.py`, `tool.workflow` and `controls`. Checked: 43 `tool.files` equal the tree by
sha256, the workflow pin, `controls`, the three records and `roles.side_change_classes` all equal the commit's blobs.

## Item 1. R-B1 option (a): EI6 enforces "standard library only"

`conformance_controls.py`:
- `INSTALLED_NAMES = ('site-packages', 'dist-packages')`;
- `_installed_dirs()`: real paths of sysconfig `purelib` and `platlib` under every scheme the interpreter defines,
  `site.getsitepackages()` and `site.getusersitepackages()` (read in a `-I -S` subprocess), and every
  `site-packages`/`dist-packages` directory on the interpreter's `-I` path (no `-S`);
- `ei6_allowed(rf, pinned, stdlib, installed)`: pinned, or under a `-I -S` directory and neither at/under an installed
  directory nor below a `site-packages`/`dist-packages` directory inside that standard-library directory. The shadow
  run's predicate now calls it; `_interpreter_dirs` (the `-I -S` path) is unchanged apart from its docstring;
- `ei6_installed_cases()` (EI6's negative control, reported under the shadow run as `installed packages`, required by
  EI6's predicate): (a) no allowed directory is or lies under an installed-package directory or carries such a name;
  (b) a real `-I -S -B -v` traced import of a fixture package `ei6fixture` from `<out>/ei6-installed/lib/python3/
  site-packages` (a symlink to `dist-packages`, the CPython layout) with that `lib/python3` treated as a
  standard-library directory: every traced file refused; (c) a real traced import of the interpreter's installed
  `certifi` (`-I -B -v`, `site` active) where present: every traced file refused; (d) every out-of-tree import of a
  real `-I -S -B -v tools/ledger_coverage.py self-test` run in a fresh checkout copy: accepted.
- EI6's `case` and `expected` texts state the definition and the three cases.

Result at 4f4a9d58 (`logs/corr2/full/conformance-controls.json`): EI6 PASS; allowed directories at/under an installed
directory `[]`; fixture: exit 0, 1 file traced, 0 admitted; `certifi`: present, 2 files traced
(`/usr/local/lib/python3.13/dist-packages/certifi/{__init__,core}.py`, the reviewer's counterexample), 0 admitted;
self-test: exit 0, **162 out-of-tree imports, 0 refused** (the reviewer's count); shadow run 184 imports, no stray, no
marker, result equal. Mutation: C11 (allowed directories from `-I`) is now **killed** by EI6 (check (a));
D01 (the predicate reverted to 3184c7f9's prefix test) killed; D03 (name rule removed) killed. The runner's EI
subprocesses keep `-I -S -B`.

## Item 2. D-2 option (b): the workflow's fixed commands

Sources: PREREG §32.4 in `diffs-r5/PREREG-append-s32-r5.diff` (sha256 dc7616c9…9a5e), `CHANGES-r4-to-r5.md`
(a7f45091…4c37), `PROPOSAL-r4.md` (676810f6…4e74), the r5 configuration `retirement-config-r5.json.proposed`
(7c898472…8a51). None edited; P (4c79be64…) not touched.

What the r5 configuration names: `adapters.ledger` and its `edits`/`checker` companions in the plan directory
(`a1exit-deletion-20261121/`, the configuration's directory); `delegation.path` =
`ledger-coverage-tool-20261123/delegation-draft.json`; `records` kind `scope` =
`…/records/repo-scope-v1.json`, kind `hit-classification` = `…/records/gr58-hit-classification-v1.json`; no context
adjudication record, no HP record, no `repo-rules` file. The staged configuration names the same paths. The run block
gains one fixed line `A=verification/audits/foundations/ledger-coverage-tool-20261123`; `D="${CFG%/*}"` stays for the
plan-directory files.

| Arm | 3184c7f9 | 4f4a9d58 | Justification | Run against the staged configuration (3184c7f9 arm → 4f4a9d58 arm) |
|---|---|---|---|---|
| item1-execution | `--ledger F:$D/ledger.json --edits F:$D/edits.json` | unchanged | §32.4 item 1; paths named by `adapters.ledger` | FAIL → FAIL (no path error; RET findings at the stand-in, no host) |
| item1-terms | `terms --commit X --profile ptr` | `+ --classify "$F:$A/records/gr58-hit-classification-v1.json"` | §32.4 item 1 expects the `ptr` hits to PASS "by W2's rules and the classification of `papers/GR.md:58`"; `op_terms` reads hit records only from `--classify`; the record is the configured `hit-classification` | REVIEW_REQUIRED (1 unclassified: GR.md:58) → **PASS** |
| item2-record | `record --pin E --record F` | unchanged | §32.4 item 2 | PASS → PASS |
| item2-coverage | `… --hp F:$D/hp.json` | `… --hp "$F:$D/hp.json" --classify "$F:$A/records/gr58-hit-classification-v1.json"` | §32.4 item 2: `--hp F:hp.json --classify <records>`, "PASS only with the HP, context and hit records the configuration references"; the configuration references the one hit record and no context record. `--hp` stays at `F:hp.json` (a file of the plan directory, §32.4 notation); §32.8 lists `hp.json` and the HP/context records as **missing** until the configuration references them before `F` | ERROR `SOURCE_CHANGED` (hp.json not present) → the same; with the `--hp` pair removed the 4f4a9d58 arm runs (FAIL, no path or record error) |
| item3…item13 (one arm) | `--delegation F:$D/delegation.json` | `--delegation "$F:$A/delegation-draft.json"` | §32.4 items 3–13 "`--delegation <configured contract>`"; `delegation.path` of the r5 configuration | ERROR `SOURCE_CHANGED` "--delegation is not the configured contract" → FAIL (delegated evidence invalid/missing: no host run locally), each of the 9 values |
| item7 | `terms --commit X --profile item7-literal` | unchanged | §32.4 item 7 "as frozen" | FAIL (7 literal lines at T1′) → FAIL |
| item7-amended | `terms … --base H --ledger F:$D/ledger.json --check item7 --final` | `+ --classify "$F:$A/records/gr58-hit-classification-v1.json"` | owner's D-2 (b) instruction restores `--classify` for amended item 7; the review's reading 2 (the plan expects GR.md:58 PASS by its record, which only `--classify` supplies) | FAIL (GR.md:58 final-unclassified + 45 REVIEW) → REVIEW_REQUIRED (the 45 `resid` lines only, as RT-D) |
| item11 | `--scope F:$D/repo-scope.json --rules F:$D/repo-rules.json` | `--scope "$F:$A/records/repo-scope-v1.json"` | §32.4 item 11 is `terms --commit X --check item11 --final` (no `--rules`; neither configuration names a `repo-rules` file, and rules are read from `rules` of the configuration whatever `--rules` says); `--scope` stays because `op_terms` requires it for the repo-scoped profile, at the configured `scope` record | ERROR `SOURCE_CHANGED` (repo-scope.json not present) → FAIL (172 final-unclassified: the expected state until each line has a rule, cf. RT item11-T1p) |
| item14 | `… --delegation F:$D/delegation.json` | `… --delegation "$F:$A/delegation-draft.json"` | as items 3–13; `--delegation` for "plus the `tex` contract" (reading 6 unchanged) | ERROR `SOURCE_CHANGED` → FAIL (delegated evidence; base-drift and side-change findings against `main`) |
| item14-landing | `--main M --landing L …` | `--main "$M" --certified "$C" --landing "$L" …`; new input `c` ("the certified head C, a full 40-hex id"), env `C` | §32.4 item 14: "then `--certified C --landing L` before landing"; without it `C` defaults to `X` | ERROR `SOURCE_CHANGED` → FAIL (`landing-parents`: the stand-in `L` is `main`, not a landing merge) |

Unchanged: the pre-run step (byte-identical; extracted program 1645 bytes, sha256 001a3357…, as at 3184c7f9),
`-I -S -B` everywhere, reading 3 (no `--classify` of class records in execution arms), the fetch step, `exit 64` after
`esac`, every input only through `env:`.

Probes (`logs/corr2/probe/`):
- `workflow_yaml_check_c2.out`: PyYAML program equals the R-e extraction; argv prefix `python3 -I -S -B -c`; line rule
  on the workflow `[]`; no `${{` in any `run:`; 9 inputs (`check` a choice of the same 18 values); `bash -n` 0;
  pre-run step byte-identical to 3184c7f9's.
- `runblock_args_c2.out` (run block under bash with a stub `python3`): each of the 18 values gives its fixed argv; the
  5 unknown values (`bogus`, `*`, `item3 item4`, `item1-terms;id`, empty) exit 64 with nothing run; injection-shaped
  inputs (spaces, `$(…)`, backticks, `;`, globs, `--landing=evil` as `C`, `--repo=` in `F`) each stay one argv
  element and nothing executes.
- `inj_certified_c2.out`: the real entry point given `--certified` followed by `--landing=evil`, `--repo=/x` or
  `--rep=/x` exits 64 (USAGE, "expected one argument") before any read; no output directory created.
- `arms_c2.py` → `arms-new/arms_c2.json` (4f4a9d58 workflow) and `arms-old/arms_c2.json` (3184c7f9 workflow,
  `workflow-3184c7f9.yml`): each arm's argv as the run block produces it, run in-process against the staged
  configuration 5072a3b0… in control-harness mode (the configuration cannot be admitted without an `F`) on an
  in-memory stand-in `F` 4eee7077… (3184c7f9's tree plus the staged configuration, P's `ledger.json`, `edits.json`,
  `edits_check.py` in the plan directory, and the working tree's class record and `controls.json`), with a static
  check of every record argument against the paths and sha256 the configuration names. New arms: every record
  argument is named by the configuration, present at `F` and equal to its pin, except item 2's `--hp F:hp.json`
  (named by no configuration; §32.8 missing); no other arm ends in a path or record error. Old arms: items 3–13, 14,
  14-landing and 11 end in `SOURCE_CHANGED`, item 2 as the new.

Not resolvable within this scope: item 2's coverage arm reaches no PASS until an HP record (and any context record) is
written and referenced by the configuration (PREREG §32.8 "Missing").

## Item 3. `controls.json`: rows EI5, EI6, EI7, GV4

Only these rows changed (all other keys and rows equal after parse; serialization `indent=1, ensure_ascii=False`
as before). New text cites no review id.
- **GV4**: case adds "the HP merge"; expect: exit 65 and no PASS; the HP merge, read first by the HP chain check,
  `CONFIG_INCONSISTENT` or the unresolvable-object error.
- **EI5**: case adds "including one equal to `L`'s given first parent"; expect adds the countercontrol (one main line
  equal to `L`'s first parent resolves to it).
- **EI6**: case adds `tools/json.py`, `tools/importlib.py`, the flags `-I -S -B`, and the predicate's third case
  (fixture in `site-packages` inside a standard-library-like directory, installed `certifi` where present, every
  import of a real `-I -S -B` self-test run); expect defines the standard library as the `-I -S` path less the
  installed-package directories (purelib, platlib, `site-packages`, `dist-packages`, by real path).
- **EI7**: case adds the upper-case key, the three 40-hex-suffix local/parent forms, and `uses: -foo/bar@<40 hex>`;
  expect: exit 65 `CONFIG_UNREVIEWED` naming the line rule, non-acceptance at the consumer, the conforming workflow
  exits 0.

## Item 4. C04 and C08 tests

- **C04**: `EI7_FORMS` gains "an owner name beginning with a hyphen, with a 40-hex suffix" (`- uses:
  -foo/bar@<40 hex>`); EI7-tool expects 23 forms. Result: exit 65 `CONFIG_UNREVIEWED` (line 8), rule refuses. Mutant
  C04 **killed** (EI7-tool).
- **C08**: `o3_controls` runs two cases, the smudge filter in a global configuration file (`GIT_CONFIG_GLOBAL`, as
  before; `GIT_CONFIG_SYSTEM` left as the environment has it) and in a system configuration file
  (`GIT_CONFIG_SYSTEM`, global set to `/dev/null`), each with its countercontrol; the docstring now states the two
  cases. Result: both cases Native.clone no marker, countercontrol marker written. Mutant C08 **killed** (O3-FILTER),
  C07 still killed.

## Item 5. Observations and nits (recorded only; no code change)

- **O-1** (`uses:` rule): `foo/..@<hex>` and `foo/bar/../../x@<hex>` are admitted by the line rule; `.`/`..` as repo
  or path segments are not refused. Candidate for a later owner decision.
- **O-2** (O-3 scope): `Native.clone` clears the global and system configuration but not configuration given through
  `GIT_CONFIG_COUNT`/`GIT_CONFIG_KEY_n`/`GIT_CONFIG_VALUE_n` or `GIT_CONFIG_PARAMETERS`; a filter given that way runs.
  The pinned workflow sets none; residual trust in the runner environment.
- **N-c1**: control texts cite review ids ("review impl-v6.0e D-11", "review v6.0d B-1"); left as is (the O3 text
  keeps its existing prefix; no new review id was added).
- **N-c3**: PREREG §32.4 (and §32.2) of the amendment proposal state the prefix `python3 -I -B`; the workflow uses
  `-I -S -B`. To be fixed in the amendment, not here.
- New, from this correction's mutation run: **D02** (removing the real-path exclusion of the installed directories,
  keeping the name rule) survives: on CPython and Debian layouts every installed directory is named `site-packages` or
  `dist-packages`, so the name rule alone refuses the same files. It is a second layer for a non-standard purelib
  name; no case exercises it. Not added (outside the authorized scope; would need a further commit).

## Item 6. Re-pin, staging, full suite, equality

Full suite `logs/corr2/repro.sh` (a copy of `logs/corr1/repro.sh` with the corr2 output directory and
`staging-4f4a9d58`; entry point `-I -S -B`; each step under `logs/perf/measure.py`). `full/head.txt` 4f4a9d58,
`full/status.txt` empty (clean), `full/staged-config.sha256` 5072a3b0….

| Step | Exit | Wall | Peak RSS | At 3184c7f9 (`logs/corr1/steps.txt`) |
|---|---|---|---|---|
| 1 self-test | 0 (86 PASS) | 0.1 s | 22 MB | 0, 0.1 s |
| 2 staged purity lint | 0 (PASS) | 0.7 s | 38 MB | 0, 0.9 s |
| 3 synthetic | 0 (36 PASS, 4 info) | 0.5 s | 26 MB | 0, 0.6 s |
| 4 conformance | 0 (79 PASS, 2 NOT RUN: TR5, G-A1) | 8.1 s | 35 MB | 0 (79/2), 7.4 s |
| 5 A1 conformance | 0 (47 PASS) | 55.8 s | 203 MB | 0 (47), 56.9 s |
| 6a A1 controls without `--main` | 2 (usage) | 0.1 s | 27 MB | 2 |
| 6 A1 controls, sweeps | 1 (91 PASS, 1 NOT RUN: RT-T) | 1148.8 s | 1.48 GB | 1 (91/1), 1197.1 s |
| 7 release gate | 1 (lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles: environment, shallow store) | 67.0 s | 51 MB | 1; log identical with times removed |

Totals: 347 rows, 340 PASS, 3 NOT RUN (TR5, G-A1, RT-T), 4 informational, 0 FAIL. (Steps 4–6 overlapped in time with
the arm probe and the mutation run; at most two of my processes ran at once.)

**Equality against 3184c7f9** (`logs/corr2/compare_c2.py` = `compare_c1.py` with the corr2 directory normalized;
`compare-c2.json`; detail `compare-c2-detail.txt`): 347 before, 347 after; **343 identical in id, status and actual;
0 status changes; 0 added; 0 absent; 4 differ in `actual` only**:

| Control | Difference | Why |
|---|---|---|
| conformance/EI6 | adds `installed packages` (the negative control above); every other field identical | item 1 |
| conformance/EI7-tool | adds the hyphen-owner form (tool exit 65 `CONFIG_UNREVIEWED`, rule refuses); 23 forms; rest identical | item 4 (C04) |
| conformance/O3-FILTER | `{native, countercontrol}` becomes `{global: …, system: …}`; `global` equals the 3184c7f9 actual | item 4 (C08) |
| a1-controls/RT-L2 | keyed comparison (`compare_rtl2_c2.py`, `rtl2-c2.out`): 54 predicted-commit ids and the 5 blobs of the changed paths; 0 unexplained; landed paths 54, classes `{class-record: 1, tool-landing: 53}`, unbound `[]`, AGENTS.md base-drift reconciled, all unchanged | the commit's 5 changed blobs |

The `expected` texts of EI6, EI7-tool and O3-FILTER changed with their cases. `synthetic/_Y8_engine` and K1-GRAPH are
unchanged (no engine file and no configuration edge changed).

## Mutation (`mut/runC2/`; harness `mut/scripts/mutate_c2.py` = `mutate_c1.py` with set selection, set-prefixed ids and one worker; new mutants `mutants_c2.py`)

Source: a `checkout-index` extraction of 4f4a9d58 (3660 files). Base run: 201 PASS, 2 NOT RUN. Sets: c1 (12), c2 (3,
new), v60e (67, `mutants.py`), cache (8). **82 killed, 7 survived, 1 not applied.**

| Set | Result | Change from the previous run of the set |
|---|---|---|
| c1 (C01–C12; runC1 at 3184c7f9) | 12/12 killed | **C04, C08, C11: survived → killed**; the other nine stay killed |
| c2 (new) | D01, D03 killed; D02 survived (item 5) | new |
| v60e (run2 at 1c6dcd09) | 61 killed, 5 survived (V05, I06, C08, H03, P01, all survivors in run2 too), U01 not applied | A04, C02, C16: survived in run2 → killed now (C16 was already killed as C1's C06 at 3184c7f9). **No previously killed mutant survives.** U01 not applied: its old string is the pre-B-1 `uses:` rule replaced in correction 1 (the corresponding mutant C1:C01 is killed) |
| cache (runK at c59b562c) | 7 killed, K08 survived | unchanged |

(The v60e survivors V05, I06, C08, H03, P01 and cache K08 are the survivors assessed in the earlier records.)

## Record files (new; nothing existing overwritten; `MANIFEST.sha256` appended)

- `CORRECTION-2.md`, `CORRECTION-2-CHECKPOINT.md`;
- `staging-4f4a9d58/…/retirement-config.json`;
- `gen/gen_final_c2.py`, `gen/gen_config_c2.py`;
- `logs/corr2/`: `repro.sh`, `repro.out`, `steps.txt`, `full/`, `diff-c2.patch`, `compare_c2.py`, `compare-c2.json`,
  `compare-c2-detail.txt`, `compare_rtl2_c2.py`, `rtl2-c2.out`, `probe/` (`workflow_yaml_check_c2.{py,out}`,
  `prog_c2.txt`, `runblock_args_c2.{py,out}`, `stub/python3`, `inj_certified_c2.out`, `arms_c2.py`,
  `workflow-3184c7f9.yml`, `arms-new/`, `arms-old/`);
- `mut/scripts/mutate_c2.py`, `mut/scripts/mutants_c2.py`, `mut/runC2/` (`base.json`, `results.json`,
  `mutate.stdout`, `source-commit.txt` in the manifest; the per-mutant output trees are not).

## Not done

- No push, CI, dispatch, merge or GitHub write.
- The focused independent review of 4f4a9d58 (owner decision item 7) is pending.
- Item 2's coverage arm cannot be shown to run with `--hp` locally: the HP record does not exist in any configuration
  (§32.8). D02 survives (item 5). O-1 and O-2 are open for the owner.
