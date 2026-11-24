# Independent review: correction 1 of the v6.0e implementation (3184c7f9)

Reviewer: independent non-author reviewer, 2026-11-24. Review only. Nothing in the tool worktree was modified, nothing
was committed, pushed, dispatched or written to GitHub, and nothing was written under `impl-v6.0e/`.

Object reviewed: commit **3184c7f9075948d8474197eee03ba5b94ba85db5**, tree d34231827c150484ba13be7885a072e56310b72d,
single parent c59b562c168dc24706f51b791ec526dd897c909d, branch `tools/ledger-coverage-20261123`.

Method. I built my own copy of the exact tree through a temporary index under this review's scratch directory
(`GIT_INDEX_FILE=… git read-tree 3184c7f9…; … checkout-index -a --prefix=…`): 3660 files, equal to `git ls-tree -r`,
every file's `git hash-object` equal to its tree entry, `.github/workflows/ledger-coverage.yml` and the audit directory
present. A `git init`'d copy of the same files served the synthetic fixture and the release gate. The runners'
`--repo` pointed at the shared store read-only, and every revision was the full id; nothing read `HEAD`. The staged
configuration was a private copy, hash-checked before use (0ba409763b6129fd018cde0c7a5a1c67674b3f8bb25ef5bd8ef43cef79e054f9).
Scratch: `workspace/rv-corr1/` (`tree/`, `gitcopy/`, `run.sh`, `logs/`, `out/`, `probe/`). Paths `probe/…` and `logs/…` below are relative to it; the probe scripts and outputs cited, my step table and my three control reports are copied into this review's `evidence/`.

## Inputs (sha256 verified before use)

| Input | sha256 | |
|---|---|---|
| `impl-v6.0e/CORRECTION-1.md` | 3352a14ec2700750b81f405079e0f6bc020a0b9605ac70e9379c2add61419213 | match |
| `review-impl-v6.0e/review.md` | 68d4e071a9c83f977051d2eb18f5259d317659a671254de32e50b78f116573f1 | match |
| `review-perf-fix/review.md` | 6def2c2a7561baf089e3d2ae0d73f9caeaa0abecd0a3185fda0eb6900657ae42 | match |
| `DESIGN-v6.0e.md` | 4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131 | match |
| staged configuration (`staging-3184c7f9/…/retirement-config.json`) | 0ba409763b6129fd018cde0c7a5a1c67674b3f8bb25ef5bd8ef43cef79e054f9 | match |

## Verdict

**REJECT** for the exact commit, on one blocking finding (R-B1: the EI6 import predicate that D-7 narrowed admits
installed packages on a standard CPython layout, so EI6's predicate is weaker than the expectation the correction gives
it; a one-function fix or a one-sentence restatement). B-1, D-1 and the form of D-2 are implemented correctly; the
nits and the remaining discrepancies are resolved; there is no unrelated change; governance is clean. The D-2 arm
contents and `controls.json` need owner decisions (below); neither is a weakening of verification, and I do not block
on them. After R-B1 is corrected I expect ACCEPT-WITH-NITS.

## Blocking finding

### R-B1. EI6's narrowed import predicate admits installed packages on a standard CPython layout

**Against:** design v6.0e sec. 10.4 ("A predicate weaker than its expectation is a defect of the control"), and the
expectation that correction 1 itself gives EI6 under D-7.

**What changed.** Under D-7 the correction made EI6's allowed directories "the interpreter's `-I -S` path, which is the
standard library only" (CORRECTION-1, D-7 row), and the runner's EI6 expectation now reads "no imported file outside the
pins and the interpreter's standard library" (before: "its standard library and installed packages").
`_interpreter_dirs` takes `sys.path` of `python3 -I -S`, and the predicate is a prefix test
(`conformance_controls.py`, `allowed_file`: `any(rf.startswith(s + os.sep) for s in stdlib)`).

**Counterexample (reproducible, `probe/ei6_predicate_probe.py`, output `probe/ei6_predicate.out`).** On this machine
the `-I -S` path is `/usr/local/lib/python313.zip`, `/usr/local/lib/python3.13`, `/usr/local/lib/python3.13/lib-dynload`.
The installed-package directory (`sysconfig` purelib and platlib) is `/usr/local/lib/python3.13/site-packages`, a
symlink to `/usr/local/lib/python3.13/dist-packages`. Both lie inside `/usr/local/lib/python3.13`, the default CPython
layout (also that of `actions/setup-python` and the official Python images). A real import of the installed package
`certifi`, traced as EI6 traces imports, loads `/usr/local/lib/python3.13/dist-packages/certifi/__init__.py` and
`core.py`. EI6's predicate admits both. So on this layout the control passes a run that imports installed packages;
its predicate does not test the expectation "standard library". The only installed-package directory it refuses here is
`/usr/lib/python3/dist-packages`, which is why mutant C12 (the EI runs without `-S`) is killed: only by
`/usr/lib/python3/dist-packages/_distutils_hack` (`mut/runC1/mut/C12/out/conf/conformance-controls.json`). A `site`
hook that loaded from `/usr/local/lib/python3.13/dist-packages` would not be detected.

**Impact.** No guarantee of sec. 6.3 point 5 is weakened: no checkout file outside `tool.files` executes (the checkout
is excluded from the allowed set, and EI6's shadow run, EI8-EI15, CX-3 and the pre-run probes all hold); `-S` itself
keeps installed packages off `sys.path` in the workflow; and on the hosted runner's system interpreter (Debian layout,
packages under `/usr/lib/python3/dist-packages` and `/usr/local/lib/python3.12/dist-packages`, outside
`/usr/lib/python3.12`) the prefix test happens to discriminate. The defect is the control's claim: the correction's
record and the runner's expectation state a narrower guarantee than the predicate tests on the layout where the full
suite actually ran. Before the correction the expectation and the predicate agreed (both admitted installed packages).

**Smallest correction (one of):**
- exclude the interpreter's purelib and platlib, by real path, from the allowed directories. I checked this candidate
  (`probe/ei6_fix_check.py`, output `probe/ei6_fix_check.out`): it refuses `certifi`, and it admits every one of the 162
  out-of-tree imports of a `python3 -I -S -B tools/ledger_coverage.py self-test` run. Add one countercontrol case (a run
  that imports an installed package must be refused by the predicate); that case would also kill C11; or
- restate EI6's expectation and the record as "the interpreter's `-I -S` import path", with no claim about installed
  packages.

Either way the class record and the staged configuration are re-pinned for `conformance_controls.py`.

## Task 1: the diff c59b562c..3184c7f9

`git diff -M10% --name-status`: 9 paths, all mapped to an authorized item. Nothing else changed.

| Path | Change | Item |
|---|---|---|
| `…/ledger-coverage-tool-20261123/workflow/ledger-coverage.yml` → `.github/workflows/ledger-coverage.yml` | rename (46% similar); input `operation` replaced by `check` (choice) and `h`, `x`, `e`, `m`, `l`; run block a `case` with fixed arms | D-1, D-2, D-7 (`-I -S -B`) |
| `tools/ledger_coverage.py` | docstring usage `-I -S -B` | D-7 |
| `engine/checker.py` | `_uses` owner class `[A-Za-z0-9](?:-?[A-Za-z0-9])*`; comment | B-1 |
| `engine/schemas/oi-ledger-coverage-5.schema.json` | `config.required` gains `admission` | N-2 |
| `adapters/conformance_controls.py` | `WORKFLOW` path; EI7 three forms and `len(tool) == 22`; `ei7_consumer` helper and three consumer cases; ACCEPT-SCHEMA schema check; EI5 case; `o3_controls` (O3-FILTER) and its group and id; GV4 HP-merge case and `outcome`; EI entry and EI6 runs and `_interpreter_dirs` with `-S` | B-1, D-1, N-2, N-1, D-11/N-4, D-6/N-5, D-7 |
| `adapters/a1_controls.py` | `WORKFLOW_PATH` added to the A1 runner's landed files (both modes) | D-1 |
| audit `README.md` | the workflow row removed from the file table; the exception sentence verbatim with attribution; the D-2 workflow description; `-I -S -B` in commands | D-1, D-2, D-7 |
| `records/side-change-classes-v1.json` | the workflow as one exact path with blob; 6 blobs re-pinned; old workflow pin removed; `reason` sentence | D-1, re-pin |

The dropped unused call `code7, res7 = t7.run(...)` (replaced by `ei7_consumer`) is part of the B-1 consumer change; it
changed no recorded outcome. `git diff --name-only 443e871f 3184c7f9` lies entirely in `tools/ledger_coverage/`,
`tools/ledger_coverage.py`, the audit directory and `.github/workflows/ledger-coverage.yml`: the landing respects the
owner's exception. The README sentence equals the owner's wording verbatim.

## Task 2: the five acceptance criteria

| Criterion | Result | Evidence |
|---|---|---|
| 1. B-1 closed | **met** | the rule refuses `./` and `../` owners with a 40-hex suffix; EI7-tool (22 forms) and TR28-consumer (4 local forms) PASS in my run; line-rule probe 0 unexpected over r01-r27, c01, c02, b1a-c and the new workflow |
| 2. D-1 and D-2 implemented correctly | **met for D-1 and for D-2's form**; D-2's arm contents need an owner decision (task 3) | file moved, not copied; class record lists it as one exact path (prefixes unchanged); staged `tool.workflow` = that path and blob; RT-L2 PASS, 54 landed, none unbound. D-2: choice input, every input via `env:`, no `${{` in any `run:`, every expansion quoted, fixed argv per value, unknown values exit 64, `bash -n` 0 |
| 3. remaining discrepancies and nits resolved | **met except R-B1** | N-1 (EI5 case), N-2 (schema), N-3 (D-18 → D-10), N-4/D-11 (O3-FILTER), N-5/D-6 (GV4) present and passing; D-4 and D-10 corrected in `IMPLEMENTATION-INVENTORY-r2.md` (80 entries at 443e871f verified: V 28, S 16, RT 14, A 11, L 4, G 3, SW 2, X 1, N 1); D-7 `-S` added; caching notes corrected in `PERF-FIX-r2.md` (figures equal the perf review's sec. 6 and N-1/N-3) |
| 4. complete verification guarantees intact | **met**, with R-B1 as a defect of a control's claim, not of a guarantee | every control status and actual equal to c59b562c's apart from the nine explained differences; no status change; mutation of the changed code 9/12 killed, survivors assessed in task 5 |
| 5. no unrelated changes | **met** | task 1 |

### Re-runs at 3184c7f9 (`workspace/rv-corr1/run.sh`; all revisions full ids)

Each step under `wait4` measurement (`meas.py`), the entry point with `-I -S -B`, staged configuration 0ba40976:

| Step | Exit | Wall | Peak RSS | Equal to the writer's `logs/corr1/full/` |
|---|---|---|---|---|
| 1 self-test | 0 | 0.2 s | 25 MB | yes (stdout identical) |
| 2 staged purity lint | 0 | 0.8 s | 38 MB | yes (result identical apart from paths and times) |
| 3 synthetic (on the `git init`'d copy) | 0 | 0.7 s | 28 MB | yes (stdout identical) |
| 4 conformance | 0: 79 PASS, 2 NOT RUN (TR5, G-A1) | 7.5 s | 35 MB | yes: 81 ids, 0 status and 0 actual differences |
| 5 A1 conformance | 0: 47 PASS | 56.7 s | 202 MB | yes: 0 differences |
| 6 A1 controls, sweeps included (`--main 9deb6956…`) | 1: 91 PASS, 1 NOT RUN (RT-T) | 1188.6 s | 1.48 GB | yes: 92 ids, 0 status differences, `actual` identical apart from the `seconds` fields of RT-A, RT-C, RT-E, SW1, SW2; `expected` and `predicate` identical |
| 7 release gate (on the `git init`'d copy) | 1 | | | the same rows as the writer's, except `legacy-records` and `citation-roles` PASS here (my copy is not shallow); `lean-axioms`, `v3-corpus` and `v3-receipts` fail on the environment as at c59b562c |

So the writer's full-suite record was produced at 3184c7f9 with configuration 0ba40976 (its `head.txt`, empty
`status.txt` and `staged-config.sha256`), and my independent run reproduces it. In my run RT-L2 PASS (54 landed paths:
53 tool-landing, 1 class record; none unbound; `AGENTS.md` base-drift reconciled), RT-D PASS (`papers/GR.md:58`
REVIEW_REQUIRED without its record) and RT-D-gr58 PASS (PASS with it), K1-GRAPH PASS with the workflow edge.

### Probes

| Probe | Result | Output |
|---|---|---|
| `uses:` rule, r01-r27, c01, c02, b1a-c, the new workflow, and 11 cases of mine | 0 unexpected on the writer's set; of mine, `-foo`, `foo-`, `fo--o`, `fo_o`, `.`, `docker://`, upper-case hex refused; `my-org`, a digits-and-dots repo with a path admitted; **`foo/..@<hex>` and `foo/bar/../../x@<hex>` admitted** (observation O-1) | `probe/line_rule.out` |
| YAML (PyYAML 6.0.3) vs R-e extraction | equal; argv prefix `python3 -I -S -B -c`; output identical to the writer's | `probe/yaml_check.out` |
| `bash -n` of the run block | 0 | same |
| pre-run step | byte-identical to c59b562c's; extracted program 1645 bytes, sha256 001a3357…, the same as at 67bae482 | `probe/pre_*.txt`, `probe/run_probes.out` |
| pre-run probes (EI8, EI13-EI15, R-d, P4/P7/P9/P10, CX-3, `main-x`, trailing newline, unset `GITHUB_REF`, inner symlink) | identical to the writer's output apart from `F` ids; the only marker is the EI15 countercontrol's | `probe/run_probes.out` |
| CX-3 (`tools/hashlib.py`), `-I -B` and `-I -S -B` | shadow never loaded; USAGE 64 | `probe/cx3.out` |
| run block with a stub `python3`, each of the 18 values and 5 unknown values (`bogus`, `*`, `item3 item4`, `item1-terms;id`, empty) | each known value gives its fixed argv; each unknown value exits 64 with nothing run | `probe/runblock_args.out` |
| injection: inputs with spaces, `$(…)`, globs, `;`, leading `--repo=` | each input stays one argv element; nothing expands or executes; the real entry point refuses option-like values (`--segment --repo=…`, `--scientific-base --repo=…`, the abbreviation `--commit --rep=…`): USAGE 64 before any read | `probe/runblock_args.out`, `probe/inj/` |
| D-11 control | O3-FILTER PASS in my conformance run; the reviewer's probe agrees | `logs/4.out` |
| system git configuration (C08), and `GIT_CONFIG_COUNT` | `Native.clone` ignores a filter in `GIT_CONFIG_SYSTEM` (the countercontrol runs it); a filter given through `GIT_CONFIG_COUNT`/`KEY`/`VALUE` environment variables **does** run in `Native.clone` (observation O-2) | `probe/o3_sys.out` |

## Task 3: D-2

**Form: implemented correctly.** Every arm's argv is fixed text with quoted expansions; the inputs reach the shell only
through `env:`; the role inputs cannot add an argument (each is one argv element), and the tool's argparse refuses any
value that looks like an option (an option given as the value of another fails with "expected one argument"); unknown
check values fall through to `exit 64` (a `*)` arm would fail the line rule's alias clause, so the writer's reading 7 is
right). `--repo` is passed by no arm. Items 3-13 share one arm, which is the design's single `execution` command for
those items; each choice value still selects one explicit command.

**Arm contents.** Compared with design sec. 11 (and sec. 6.3, 12.1, 13), the A1 runner, and the amendment proposal's
sec. 32.4 (`PREREG-append-s32-r5.diff`) with its proposed configuration (`retirement-config-r5.json.proposed`):

| Reading | Design | Effect at runtime | Coverage vs design / A1 runner |
|---|---|---|---|
| 1. `F:<name>` = `"$F:$D/<name>"`, `D` the configuration's directory | sec. 11: "Paths given as `F:...` below are resolved through [the configuration]"; sec. 12.1 places the plan's `ledger.json`, `delegation.json`, `hp.json` and rule files in the plan directory, but scope records in the tool's audit directory | the tool compares each path with the configuration (`load_adapter_input`, `op_execution`: `SOURCE_CHANGED` on a different path; blobs pinned by sha256). Under the staged configuration 0ba40976 and the proposed r5 configuration, `delegation` is `ledger-coverage-tool-20261123/delegation-draft.json` and the scope record `…/records/repo-scope-v1.json`, so **every arm with `--delegation` (items 3-6, 8-10, 12-14) and the item-11 arm (`--scope`) would end ERROR 65**, not run | no weakening: a wrong path can only refuse. But these arms cannot execute against the proposed configuration |
| 2. item 2's `--classify F:...` dropped | sec. 11 elides it; proposal sec. 32.4 requires `--classify <records>` ("PASS only with the HP, context and hit records the configuration references") | `op_coverage` reads context adjudications and hit records only from `--classify`; both can only clear an item (`context.decide`, `Terms.review`) | no weakening (fail-closed), but the item-2 arm can never reach the PASS the plan expects. The same holds for **item 1's `terms` arm and `item7-amended`**: the plan expects `papers/GR.md:58` PASS by its hit classification record, which only `--classify` supplies (my A1 run: RT-D shows it REVIEW without the record, RT-D-gr58 PASS with it) |
| 3. no `--classify` for side-change class records in execution arms | sec. 13.1: classes and reconciliation records come from records the configuration references | `op_execution` takes the class and reconciliation records from `cfg['records']` whether or not `--classify` is passed (`cli.py`, the `for r in cfg['records']` loop); a `--classify` record the configuration does not reference is `record-invalid` in a real run (`RecordSet.admit`). The staged configuration and the r5 configuration reference the class record (and r5 the drift classes and the `AGENTS.md` reconciliation record) | **none.** The writer's stated consequence ("classifies the tool landing only if the plan's command includes it") does not hold for these configurations: the tool landing is classified through the configuration. The A1 runner's `--classify` of the class record is deduplicated against it; its drift and reconciliation records are harness inputs |
| items 1, 2 split; item 7 frozen and amended arms; item 14 with and without `--landing` | as sec. 11 and its note 1 | as written | none |
| item 14 "plus the `tex` contract" as `--delegation` | sec. 11 | as reading 1 | as reading 1 |
| not raised by the writer: no `--certified` | sec. 13.1: `C` is the certified head; proposal sec. 32.4 item 14: "then `--certified C --landing L` before landing" | `Execution` defaults `C` to `X`, so with `C ≠ X` the landing check requires `L`'s second parent to be `X` and fails; commits after `X` are never checked | no weakening (a `C ≠ X` landing fails), but the landing arm does not implement the plan's command |

**Conclusion.** No reading lets a run pass that the design's command would fail: every departure refuses or leaves an
item REVIEW/FAIL. Relative to the design and to the A1 runner, verification coverage is **not weakened**, but it is
**changed in the strict direction**: as landed, the workflow cannot produce a PASS for items 1, 2 and 7 (amended), and
against the proposed configuration it ends in ERROR for items 3-6, 8-14. The writer's reading 3 is harmless and its
stated consequence is incorrect.

**Smallest correction or owner decision.** The arms' record paths and record arguments depend on the amended plan's
configuration, which is not frozen; the README already says a changed arm is a new workflow blob re-pinned at `F`.
The owner should decide one of:
- (a) accept the landed arms as provisional, with a recorded statement that before `F` the arms are rewritten to the
  amended plan's sec. 11 commands (paths as the configuration names them; `--classify` with the configured hit,
  context and HP records for items 1, 2 and 7; `--certified "$C"` with a `c` input for the landing arm), and that a
  workflow change is a new tool-landing blob re-pinned by the class record and the configuration; or
- (b) rewrite the arms now to the proposal r5 configuration's paths and record arguments, as above.

Either is within D-2's form; neither needs a design change.

## Task 4: `controls.json` and the runners

**What it is.** The staged configuration pins it as `controls` (design sec. 16.2: "the retirement's preregistered
control set (sec. 10, 11) with expected outcome rules"; sec. 16.4 places RT-*, SW*, the sec. 11 mapping and the
countercontrols there). The tools read only its `control_inputs` (`a1_controls.py`, RT-DR3W); the runners hard-code
their own expectations. Design sec. 10.4 makes each runner's report, with `expected` and `predicate`, the reported
control record. So by the design it is the retirement's preregistered control set, **not** the canonical inventory of
the runners' controls: TR, LN, WB, R16/R17, G4-G9, GV-CACHE, ACCEPT-SCHEMA, X10/X11 and others were never in it
(D-4).

**Disagreements with the runner at 3184c7f9** (it lists 102 ids; the runner rows it shares):
- **EI7**: the file lists the forms up to review v6.0d's B-1; the runner adds the upper-case key (already before
  correction 1) and the three 40-hex-suffix forms of B-1, and checks 22 forms at the tool and 4 local forms at the
  consumer;
- **GV4**: the file lists five corrupted objects; the runner adds the HP merge with "ERROR 65, no PASS, class
  `CONFIG_INCONSISTENT` or `UNRESOLVABLE`";
- **EI5**: the file has no case of an id equal to `L`'s given first parent;
- **EI6**: the file's "the interpreter's standard library" now matches the runner's text but not the runner's
  predicate (R-B1); the file does not say that the EI runs use `-I -S -B`;
- **O3-FILTER** and **ACCEPT-SCHEMA** are runner-only, as other implementation controls are.

In each shared row the runner is a superset of the file; nothing in the file contradicts what the runner checks.

**Recommendation.** If the owner intends `controls.json` to state every case of the tool-level rows it already carries
(GV and EI), amend the EI5, EI7 and GV4 rows (and EI6's flags) to add the cases, as one new blob, re-pinned by the
class record and the configuration; O3-FILTER may be added as a GV/EI-style row or left runner-only like the other
implementation controls. If it is meant as the design's verbatim preregistered set, record that reading and that the
runner's `expected` text is the authority for added cases. The design supports the second reading; the owner's "the
inventory and actual test runner should agree" favors the first for the rows the file already holds.

## Task 5: mutants C04, C08, C11

| Mutant | Assessment | Guarantee affected |
|---|---|---|
| C04 (owner may start with `-`) | **test gap**, not a weakness. The real rule refuses `-foo/bar@<hex>` (my probe x01); under the mutant local and parent paths are still refused, and GitHub owner names cannot start with `-`, so such a line names no action. Killing it needs one EI7 case | none |
| C08 (delegated clone keeps the system configuration) | **test gap**. My probe: with a required smudge filter in `GIT_CONFIG_SYSTEM`, `Native.clone` does not run it and the countercontrol does; the implementation is right. O3-FILTER tests only the global configuration, while `o3_controls`' docstring and the inventory row say "system and global". One more case (the same filter in a `GIT_CONFIG_SYSTEM` file) kills it | none |
| C11 (EI6's allowed directories from `-I` instead of `-I -S`) | **equivalent at this commit, but it exposes a real control weakness (R-B1).** Here the two predicates differ only on `/usr/lib/python3/dist-packages`, from which nothing loads under `-S`. The mutant survives also because the narrowed predicate already admits `/usr/local/lib/python3.13/dist-packages` (inside the stdlib directory). No countercontrol tests the predicate itself; the C12 kill depends on a Debian `.pth` hook in this image | the EI6 claim (R-B1); not point 5 |

## Task 6: governance

- **Commit.** Single parent c59b562c; author and committer `Claude <<commit-identity-email>>`; message ends with the
  `Co-Authored-By` and `Claude-Session` trailers. Signature: SSH ed25519, namespace `git`, verified cryptographically
  over the commit payload (git cannot verify here: no allowed-signers file); the key is the one that signed c59b562c.
- **Committed text.** The 274 added lines contain no workspace or local path, no e-mail address, no model id, no
  `closes/fixes/resolves #N`. The new control strings cite "review impl-v6.0e", as the existing code cites "review
  v6.0d" (nit N-c1).
- **Class record.** 53 pins equal `git ls-tree -r 3184c7f9` of the landing paths less the record itself (entry point,
  42 under `tools/ledger_coverage/`, 9 in the audit directory, the workflow); every `git_blob` and `blob_sha256`
  matches; prefixes unchanged; the old audit-directory workflow pin removed.
- **Staged configuration.** 43 `tool.files` equal the tree's tool files by sha256; `tool.workflow` names
  `.github/workflows/ledger-coverage.yml` with its sha256; all 83 `{path, blob_sha256}` references in the file resolve
  and match (at their pinned commits where given). Against `staging-c59b562c/`'s configuration it differs only in the
  `notes` sentence, the class record pin (two places), the five changed tool files and the workflow pin.
- **Record directory.** `impl-v6.0e/MANIFEST.sha256`: 191 entries, all verify; its first 57 lines hash to e65ee36d…
  (the manifest the implementation review recorded) and correction 1's entries begin at line 132, so it was appended.
  `staging/` (5af8f07e…) and `staging-c59b562c/` (b45be784…) are intact. The manifests of `review-impl-v6.0e/` (32) and
  `review-perf-fix/` (31) verify. The writer's `logs/corr1/full/` names head 3184c7f9, a clean status and staged
  configuration 0ba40976, and my run reproduces it.

## Observations and nits (not blocking)

- **O-1 (`uses:` rule).** `foo/..@<hex>` and `foo/bar/../../x@<hex>` pass the rule. Design R-a requires literal
  `<owner>` and `<repo>` names; `..` is not a GitHub repository name, and a `..` segment in the path could address
  outside the action's checkout on the runner. Not demonstrated against GitHub, and outside B-1's authorized scope
  (owner-name validation); the workflow blob is pinned and reviewed. Candidate for a later owner decision: refuse `.`
  and `..` as repo or path segments.
- **O-2 (O-3 scope).** `Native.clone` clears the global and system configuration but not configuration given through
  `GIT_CONFIG_COUNT`/`GIT_CONFIG_KEY_n`/`GIT_CONFIG_VALUE_n` (or `GIT_CONFIG_PARAMETERS`); a smudge filter given that way
  runs (`probe/o3_sys.out`). O-3 names the global configuration only, and the pinned workflow sets none of these
  variables, so the runner image's environment is in the residual trust. Clearing those variables in `env` would close
  it.
- **N-c1.** Control texts cite review ids ("review impl-v6.0e D-11"), following the existing "review v6.0d" precedent.
- **N-c2.** `o3_controls`' docstring says the system and global configuration; the control tests the global one only
  (C08).
- **N-c3.** The amendment proposal's sec. 32.4 still states the command prefix `python3 -I -B`; the workflow uses
  `-I -S -B` (D-7). The amendment, not this commit, needs the change.

## Files

`review.md` (this file), `MANIFEST.sha256`, `CHECKPOINT.md`, and `evidence/` (copies of the probe scripts and outputs
named above, and my run's step table and control reports). Full outputs remain in `workspace/rv-corr1/`.

