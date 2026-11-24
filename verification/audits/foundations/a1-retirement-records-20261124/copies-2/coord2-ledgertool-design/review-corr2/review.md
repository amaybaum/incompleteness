# Independent review: correction 2 of the v6.0e implementation (4f4a9d58)

Reviewer: independent non-author reviewer, 2026-11-24. Review only. Nothing in the tool worktree was modified, nothing
was committed, pushed, dispatched or written to GitHub, and nothing was written under `impl-v6.0e/`.

Object reviewed: commit **4f4a9d58fd0bf41289a4904c9b39c00c711c9093**, tree 82276267baa5518d3d2466b08bc0c88a4bdd1f02,
single parent 3184c7f9075948d8474197eee03ba5b94ba85db5, branch `tools/ledger-coverage-20261123`.

Method. My own copy of the exact tree through a temporary index (`read-tree` + `checkout-index` into
`rv-corr2/tree/`): 3660 files, every `git hash-object` equal to its `ls-tree` entry; the parent's tree likewise in
`rv-corr2/tree0/`. A `git init`'d copy (`gitcopy/`) served the synthetic fixture, the release gate and the arm probe; a
second one (`mutsrc/`) the mutation run. Runners read the shared store read-only with full revisions
(`--config 4f4a9d58…:…/retirement-config.json`); nothing read `HEAD`. The staged configuration was a private copy,
hash-checked (5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0). At most two of my processes ran at
once. Scratch: `workspace/rv-corr2/`; probe scripts, outputs and my control reports are copied into `evidence/`.

## Inputs (sha256 verified before use)

| Input | sha256 | |
|---|---|---|
| `OWNER-DECISIONS-CORR2-20261124.md` | 4ee1c5d8a97c6bdbad97eaa722c1db8601b83e54e61554a6a3eae6499b7692f5 | match |
| `review-corr1/review.md` | 3b99a0899d7cd5b167fa9f557461ea901540f551f85d997cdc8cc9f69c47a68f | match |
| `impl-v6.0e/CORRECTION-2.md` | b555ca5263691d9da453dc659813a63a0b770c211dfad4e6005ac2fa30e9cf7e | match |
| `impl-v6.0e/MANIFEST.sha256` | 2a7e97d218afee75dc7f0048c6f63b8e035437421e33cf05d6fee8b24dc9c793 | match; all 248 entries verify |
| `DESIGN-v6.0e.md` | 4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131 | match |
| staged configuration (`staging-4f4a9d58/…`) | 5072a3b0e25e9283acecf4c3df87f820e34464d8d6e2e501ec672615114a96a0 | match |
| `PREREG-append-s32-r5.diff`, `CHANGES-r4-to-r5.md`, `PROPOSAL-r4.md`, `retirement-config-r5.json.proposed` | dc7616c9…9a5e, a7f45091…4c37, 676810f6…4e74, 7c898472…8a51 | match (as the writer cites) |

The writer's record cites the owner decision as 6bb934c1…a9ed. That is the sha256 of the file's first section (the
decision itself, before the "Review criteria" and "Disposable CI validation run" sections were appended); I computed it
from the current file. Same decision text; nit N-2.

## Verdict

**ACCEPT-WITH-NITS.** No blocking finding. Every hunk maps to an authorized item; EI6 now enforces the
standard-library restriction with a real, non-vacuous negative control; the 18 arms equal an expectation I built
independently from PREREG §32.4 (r5), the r5 configuration's paths and the owner's D-2 (b); C04, C08 and C11 are killed
in my own mutation run, and no previously killed mutant survives; my full-suite rerun at 4f4a9d58 reproduces the
writer's results exactly and differs from 3184c7f9 only where the correction intends. The nits and observations below
are recorded, not required.

## Blocking findings

None.

## Task 1: the diff 3184c7f9..4f4a9d58

`git diff` equals the writer's `logs/corr2/diff-c2.patch` byte for byte (sha256 c6c6c499…). 5 paths, 195 insertions,
69 deletions.

| Path | Hunks | Authorized item |
|---|---|---|
| `tools/ledger_coverage/adapters/conformance_controls.py` | `EI7_FORMS` + hyphen-owner form, EI7-tool text and `len(tool) == 23` | 4 (C04) |
| | `o3_controls` split into a global and a system case, docstring | 4 (C08) |
| | EI6: `_installed_dirs()`, `ei6_allowed()`, `ei6_installed_cases()`, `INSTALLED_NAMES`, `_TRACE`; shadow-run predicate calls `ei6_allowed`; `installed packages` added to the actual and to the predicate; EI6 texts; `_interpreter_dirs` docstring | 1 (R-B1 (a), negative control) and 4 (C11 through R-B1) |
| `.github/workflows/ledger-coverage.yml` | input `c` and env `C`; line `A=…/ledger-coverage-tool-20261123`; arms item1-terms, item2-coverage, items 3–13, item7-amended, item11, item14, item14-landing | 2 (D-2 (b)) |
| audit `README.md` | one sentence (the arms' record paths) | 2, necessary propagation: the old sentence "with record paths taken from the configuration's directory at `F`" is false after D-2 (b). Nothing else in the file changed |
| audit `controls.json` | rows GV4, EI5, EI6, EI7: `case` and `expect` only; all other keys and 100 rows equal after parse; serialization (`indent=1, ensure_ascii=False`) reproduces both blobs | 3 |
| `records/side-change-classes-v1.json` | 4 pins re-pinned (the four files above) | 6 |

The pre-run step, the fetch step, the choice values, the `-I -S -B` flags and the execution arms' lack of `--classify`
(reading 3) are unchanged. There are no unrelated changes.

## Task 2: the import restriction (R-B1)

**Predicate.** `ei6_allowed(rf, pinned, stdlib, installed)`: a pinned file; otherwise refused if at or under an
installed-package directory (real paths: sysconfig purelib/platlib of every scheme, `site.getsitepackages()`, the user
site, and every `site-packages`/`dist-packages` entry of the `-I` path); otherwise admitted only under a `-I -S` path
directory with no `site-packages`/`dist-packages` component between that directory and the file. The shadow run
and the negative control use the same function and the same `stdlib` and `installed` sets.

**Attempts to break it** (`evidence/ei6_break.py`, `.out`; 18 cases, real paths of this image):

| Case | Result |
|---|---|
| `certifi` by real path (`/usr/local/lib/python3.13/dist-packages/…`) and through the `site-packages` symlink | refused |
| Debian `/usr/lib/python3/dist-packages`, user site, an `.egg` inside site-packages | refused |
| a sibling directory sharing the stdlib prefix (`python3.13-evil`, `python3.13x`) | refused (separator-anchored) |
| a nested `a/b/site-packages/c/d.py` under the stdlib directory | refused (name rule) |
| a site directory that is a symlink to a differently named directory under a stdlib directory (`site-packages -> vendor`) | refused (real-path rule only) |
| stdlib `json`, `__pycache__`, `lib-dynload` `.so`, a `python313.zip` member | admitted |
| `.pth` | not processed under `-S` (a module reachable only through a site path is not importable) |
| namespace packages | contribute no traced file; their portions in `dist-packages` are refused |
| a real `-I -B` (site active) `import certifi`: 101 traced files | 4 refused: `certifi/{__init__,core}.py` and `_distutils_hack` (the `.pth` hook); the other 97 are stdlib files and `sitecustomize.py` (observation O-r1) |

**Negative control is real.** In my conformance run EI6 PASS with `installed packages`: allowed directories at/under an
installed directory `[]`; fixture: exit 0, 1 file traced, 0 admitted; `certifi`: present, 2 traced, 0 admitted;
self-test: exit 0, **162 out-of-tree imports, 0 refused**; shadow run 184 imports, 0 stray, no marker, result equal.
`holds` requires each traced count to be non-zero, so the control cannot pass vacuously. Mutants D01 (the 3184c7f9
prefix predicate), D03 (name rule removed), C11 (`-I` path) and C12 (EI runs without `-S`) are killed by EI6 in my run.

**Legitimate imports.** Every out-of-tree import of a real `-I -S -B` self-test (162) and of the shadow run of the entry
point (184) is accepted; steps 1–6 of the suite pass unchanged.

**D02** (real-path exclusion removed, name rule kept). On every layout I can find (CPython `posix_prefix`/`posix_home`/
user schemes, Debian/Ubuntu `dist-packages`, venvs) each installed-package directory carries one of the two names, so
whenever a file lies under a stdlib directory the name rule refuses exactly what the real-path rule refuses, and when it
does not, the stdlib-prefix requirement refuses it. My probe shows D02 differs only on a constructed layout (a site
directory resolving to a differently named directory under the stdlib directory). So D02 is equivalent on the supported
layouts, and the real-path rule is a second layer that no case exercises independently. The owner's "test it" is met
for the restriction itself (non-vacuous negative control killing D01, D03, C11, C12); the untested second layer is a
test gap (nit N-4), not a weakness: there is no counterexample on a supported layout, and the removal would not admit
an installed file there.

**Conclusion: the import restriction is actually enforced.**

## Task 3: the 18 workflow commands

`evidence/wf_check.py`, `.out`:
- YAML (PyYAML) parse: the pre-run program equals the tool's `extract_prerun` extraction (1645 bytes, 001a3357…); argv
  prefix `python3 -I -S -B -c`; the pre-run and fetch steps are **raw-byte identical** to 3184c7f9's; the 18 choice
  values are unchanged; 9 inputs (`c` new, optional string); every env value is a single `${{ inputs.<name> }}` or
  `github.token`; no `${{` in any `run:`; no unquoted expansion in the run block; all 10 `exec python3` lines are
  `-I -S -B`; `bash -n` 0.
- With a stub `python3`, each of the 18 values produces **exactly** the argv of my independent expectation (0
  mismatches).
- Unknown values (`bogus`, `*`, `item3 item4`, `item1-terms;id`, empty, `item1-term?`, `ITEM3`, `item3|item4`,
  ` item3`, a trailing newline) exit 64 with nothing run.
- Injection in every input at once (`C=--landing=evil`, `$(…)`, backticks, `;`, `*`, spaces, `F=--repo=<tmp>/x`,
  `CFG` with `$(…)`): each value stays one argv element, nothing executes, no file is created. The real entry point
  given `--certified` followed by `--landing=evil`, `--repo=/x` or `--rep=/x` exits 64 ("expected one argument")
  before any read.
- Against the staged configuration I re-ran the writer's arm probe (`arms_c2.py`, hash equal to its manifest entry) on
  the same in-memory stand-in `F` (4eee7077…): results identical to the writer's `arms-new`. Every record argument is
  named by the configuration, present at `F` and equal to its pin, except item 2's `--hp F:hp.json`; item1-terms PASS
  (GR.md:58 by its record), item7-amended REVIEW_REQUIRED (45 `resid`), item11 FAIL (172 `final-unclassified`, no USAGE
  error, so `--scope` is required and correct), executions FAIL only on delegated evidence and the RET findings of the
  stand-in, item14-landing adds `landing-parents` (stand-in `L`), item 2 ERROR `SOURCE_CHANGED` on `hp.json` and FAIL
  without the `--hp` pair.

**Rulings on the writer's choices.**
- Item 11: dropping `--rules` and keeping `--scope` is right. §32.4 item 11 has no `--rules`; neither configuration
  names a `repo-rules` file; `op_terms` reads rules from the configuration whatever `--rules` says (the option only adds
  a `record-invalid` item for an unreferenced path), and it raises USAGE without `--scope` for the repo-scoped profile.
  `--scope` names the configured `scope` record.
- No context records passed: right. Neither configuration references a context adjudication record; passing none is
  what "the records the configuration references" means today.
- `--certified "$C"`: implements §32.4 item 14 ("then `--certified C --landing L`"), as the owner required.
- Reading 3 unchanged: confirmed (no `--classify` in execution arms; the class record comes through the
  configuration).

**HP / item 2 ruling.** Keeping `--hp "$F:$D/hp.json"` is the right reading of "match the r5 plan requirements". §32.4
defines its notation: "A path written `F:<name>` is a file of this directory at `F`, resolved through the
configuration", and item 2 reads `--hp F:hp.json`; the design (sec. 11, 12.1) places `hp.json` in the plan directory
too. §32.8 lists `hp.json` and "the HP, context and hit records that items 2 and 11 need" as missing. The tool admits a
command-line record only if its blob sha256 is referenced by the frozen configuration, and stops with
`SOURCE_CHANGED` when the file is absent, so until the amendment supplies it the arm is fail-closed (ERROR), never a
pass. Inventing another path, or dropping `--hp`, would have departed from the plan. What the amendment must supply
before `F`:
1. an HP adjudication record at `verification/audits/foundations/a1exit-deletion-20261121/hp.json`, referenced by the
   configuration's `records` with its blob sha256, and its non-author review record;
2. any context adjudication record item 2 needs, referenced by the configuration; if one is added, the item-2 arm's
   `--classify` list must name it, which is a new workflow blob re-pinned by the class record and the configuration
   before `F` (the README already states this);
3. §32.4's text brought to the commands of record as landed: item 1's `terms` with `--classify` of the hit
   classification record, item 11 with `--scope` of the configured scope record, the amended item 7 with `--classify`,
   item 14's landing with `--certified C`, and the prefix `python3 -I -S -B` (N-c3).

**Conclusion: all 18 workflow commands perform their intended checks against the amended plan**, with item 2's coverage
arm correctly blocked until the amendment supplies the HP record that §32.8 lists as missing.

## Task 4: mutants

My run of the writer's harness (scripts hash-equal to its manifest) at 4f4a9d58, all four sets, one worker
(`evidence/mutate.stdout`, `mutate-results.json`): base 201 PASS, 2 NOT RUN (equal to the writer's base);
**82 killed, 7 survived, 1 not applied**, every status identical to the writer's `runC2`.
- **C04** killed by EI7-tool; **C08** killed by O3-FILTER; **C11** killed by EI6. C07, C12, D01, D03 killed.
- Compared with run2 (v60e set), runC1 and runK: the only previously killed mutant not killed now is v60e:U01, which no
  longer applies (its old string is the pre-B-1 rule). I ran it adapted to the current rule (any `x@y`, `mutants_rv.py`):
  **killed** by EI7-tool and TR28-consumer. A04, C02, C16 (survivors in run2) are now killed.
- Survivors: D02 (task 2), and V05, I06, C08 (v60e), H03, P01, K08, all survivors in their earlier runs and assessed
  there.

**Conclusion: the three previously surviving mutations are now detected.**

## Task 5: guarantees and governance

**Full suite at 4f4a9d58** (`evidence/run.sh`, `steps.txt`):

| Step | Exit | Wall | Peak RSS | Writer's `logs/corr2/full/` | 3184c7f9 (review-corr1 run) |
|---|---|---|---|---|---|
| 1 self-test | 0 | 0.1 s | 25 MB | stdout and result identical | identical |
| 2 staged purity lint | 0 (PASS) | 0.7 s | 39 MB | identical | identical |
| 3 synthetic | 0 | 0.5 s | 28 MB | stdout identical | identical |
| 4 conformance | 0: 79 PASS, 2 NOT RUN | 7.9 s | 36 MB | 0 differences | actual differs only in EI6 (+`installed packages`; rest identical), EI7-tool (+ the hyphen form; rest identical), O3-FILTER (`global` equals the old actual; `system` added) |
| 5 A1 conformance | 0: 47 PASS | 54.6 s | 203 MB | 0 differences | 0 differences |
| 6 A1 controls, sweeps (`--main 9deb6956…`) | 1: 91 PASS, 1 NOT RUN (RT-T) | 1132.7 s | 1.48 GB | 0 status, expected, predicate or actual differences | only RT-L2's actual: equal after 6 consistent substitutions (the 5 changed-path blobs and one predicted commit id); PASS, 54 landed (53 tool-landing, 1 class record), none unbound, `AGENTS.md` base-drift reconciled |
| 7 release gate (git copy) | 1 | 58.6 s | 51 MB | | the same 22 rows as at 3184c7f9: `lean-axioms`, `v3-corpus`, `v3-receipts` fail on the environment |

No status changed anywhere; nothing was added or lost. The writer's record was produced at 4f4a9d58 with configuration
5072a3b0 (`head.txt`, empty `status.txt`, `staged-config.sha256`) and my run reproduces it.

Provenance note on my run: a probe of mine (run without `-B`) wrote `__pycache__` into my tree copy during step 5. I
moved those files out (`rv-corr2/own-pycache/`), confirmed the tree again equals `ls-tree` (0 mismatches), and reran
steps 4 and 5 clean: identical to the first run. Step 6 is identical to the writer's in every field, so the cached
bytecode (compiled from the same sources) had no effect.

**`controls.json` rows vs the runner.** GV4: the HP merge case and "exit 65 and no PASS … `CONFIG_INCONSISTENT` or the
unresolvable-object error" match the runner's case list and predicate. EI5: the equal-to-first-parent case and the
countercontrol match. EI6: `json.py`/`importlib.py`, `-I -S -B`, the standard-library definition and the three
negative-control cases match `ei6_installed_cases` and the predicate. EI7: the upper-case key, the three 40-hex-suffix
forms, the hyphen owner, exit 65 `CONFIG_UNREVIEWED` naming the line rule, and the conforming workflow exiting 0 match
EI7-tool and TR28-consumer.

**Pins.** Class record: 53 pins equal `ls-tree -r 4f4a9d58` of the landing paths less the record itself; every
`git_blob` and `blob_sha256` matches; one class, prefixes, reason and status unchanged. Staged configuration: all 83
`{path, blob_sha256}` references match the tree or their pinned commits; 43 `tool.files` equal the tree's tool files
by path set and sha256; `tool.workflow` is 6014639…; against `staging-3184c7f9/` (0ba40976) it differs only in
`controls`, the class record pin (two places), `conformance_controls.py` and the workflow. The generators `_c2` differ
from `_c1` in their docstring and the called file name only. `staging/`, `staging-c59b562c/`, `staging-3184c7f9/`
intact (5af8f07e, b45be784, 0ba40976).

**Governance.** Single parent 3184c7f9; author and committer `Claude <<commit-identity-email>>`; the message ends with
the `Co-Authored-By` and `Claude-Session` trailers. Signature: SSH ed25519, namespace `git`, verified cryptographically
over the commit payload (Python ed25519; a tampered payload fails, the countercontrol), same key as 3184c7f9. The 195
added lines carry no local path, workspace reference, e-mail address, model id, `closes/fixes/resolves #N`, CR or
control/invisible character; review ids in added lines are the pre-existing "review v6.0d B-1" and the kept O3 prefix
(N-c1). `MANIFEST.sha256`: 248 entries, all verify; lines 1–191 hold no correction-2 path, no duplicate, and their first
57 lines hash to e65ee36d… as recorded by the earlier reviews; correction 2's entries start at line 192.

**Conclusion: all existing verification guarantees remain intact; no unrelated changes were introduced.**

## Per-criterion conclusions

| Owner criterion | Conclusion |
|---|---|
| The import restriction is actually enforced | **met** (task 2) |
| All 18 workflow commands perform their intended checks against the amended plan | **met** (task 3); item 2's coverage arm is fail-closed until the amendment supplies `hp.json` (§32.8 missing) |
| The three previously surviving mutations are now detected | **met**: C04, C08, C11 killed in my run |
| All existing verification guarantees remain intact | **met** (task 5) |
| No unrelated changes have been introduced | **met** (task 1) |
| No further optional improvements or design revisions are needed | **met**: nothing below is needed for acceptance |

## Nits and observations (not blocking)

- **N-1.** The new README sentence lists "the HP record in the configuration's directory" among the records "read at
  `F` from the path the configuration names"; neither configuration names an HP record yet (the path is §32.4's
  `F:hp.json`). Wording only.
- **N-2.** CORRECTION-2.md cites the owner decision as 6bb934c1…, the hash of the decision section before the review
  criteria and the CI authorization were appended; the file is now 4ee1c5d8….
- **N-3.** CORRECTION-2.md's "200 added diff lines" counts the five `+++` headers; the diff adds 195 lines.
- **N-4 (D02).** The real-path exclusion is not exercised independently. A one-line case calling `ei6_allowed` with an
  injected installed directory of another name would kill D02. Equivalent on supported layouts (task 2).
- **O-r1.** By its definition the standard library is the `-I -S` path less installed-package directories, so a file
  the image places directly in a stdlib directory (`sitecustomize.py` here) is admitted. Under `-S` it is never
  loaded; no guarantee is affected.
- **O-r2.** An empty optional input becomes an empty argv value that the tool treats as absent: empty `c` gives `C = X`
  (fail-closed when the real `C ≠ X`), empty `l` turns the item14-landing run into a candidate-only run (pre-existing).
  Both are recorded in the result's `roles`, which the consumer can check.
- The writer's O-1, O-2, N-c1 and N-c3 stand as recorded.

## Files

`review.md` (this file), `MANIFEST.sha256`, `CHECKPOINT.md`, and `evidence/` (probe scripts and outputs, my step table,
control reports, gate log, mutation results, my arm-probe output). Full outputs remain in `workspace/rv-corr2/`.
