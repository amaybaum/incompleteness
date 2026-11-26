# A1 ledger coverage tool: implementation plan against design r6 (WIP / UNVERIFIED)

Status: working plan of the tool revision that implements the adopted design r6
(`verification/audits/foundations/a1exit-design-r6-20261125/`). It states no result and certifies
nothing. Every verdict on the tool revision is the gate's (DESIGN-r6.md sec. 16), read from structured
data (AGENTS.md sec. A.44).

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169). The work decides whether the tool revision meets r6's
requirements and expectation file, which gates the tool's landing (DESIGN-r6.md sec. 32). It decides no
scientific question and no plan content.

Authority: owner decision (amaybaum, 2026-11-26T03:54:50Z; #1169 comment 7182134891), quoted: "Authorize
implementation of the A1 verification tool according to the adopted r6 design, subject to completion of
the #1575 post-merge verification and landing record. * Follow the adopted requirements and expectations
without introducing exceptions. * Use a dedicated branch and PR. * Require independent review, complete
controls and exact-head CI. * Return for explicit landing approval. This authorization covers
implementation and verification before landing, not merging into main." The plan's `PREREG.md`
amendment, freezing, trials and retirement execution are not authorized (owner decision A3,
DESIGN-r6.md sec. 0.1). Nothing here runs or touches `.github/workflows/a1exit-trial-verify.yml`, the A1
plan's trial records or its trial procedure (AGENTS.md sec. A.50 item 2).

## 1. Base of the tool revision

- Drafting snapshot `D`: `main` at 3e73633308bdef99f65f6117733aaf86097c7b22 (the #1575 merge, which
  lands the adopted r6 directory).
- `main` holds the v6.0e implementation of the tool (last tool commit 4f4a9d58f). r6 supersedes v6.0e,
  r4 and r5 (R6.STAT.1), so the tool revision must carry the r4 and r5 features as well (the
  record-directory controls RDIR-*, item 2, O9-10). Those were implemented off `main` in the three
  commits 0eac3ec25, e95566090 and a37992449 (single line of descent from e2e2a62, which is on `main`).
  No tool path changed on `main` between e2e2a62 and `D`, so the three commits are cherry-picked onto
  `D` unchanged as the first commits of this branch; the resulting tool tree equals a37992449's.
  This uses a37992449 as a code base only. Under R6.STAT.10 and OBL-26 it supports no requirement:
  every row holds or fails by its own control on this revision, under the gate.

## 2. Method

Mechanical classification (each row of EXPECTATIONS.json, 558 rows; each requirement of
REQUIREMENTS.json, 428):

- `EXISTING`: the row's runner file exists on this branch and records the row id; no flag of the row
  names a defect (VD-RESTORE, a weak predicate, a C-n or VD-n obligation, an OBL-20 to OBL-28 item).
  The predicate logic is in place. The row still needs the cross-cutting evidence contract (sec. 3).
- `CHANGE`: the runner records the id, and the row's flags, its `restored` expectation or OBL-28 name a
  required change (most often the restored case of OBL-20).
- `CHANGE-RENAME`: the runner records the row under its pre-r6 id (`migrated_from`), which the
  identifier migration of sec. 34 (OBL-22) renames.
- `NEW-RUNNER`: `runner` is `null` (the gate reports `missing-id` until implemented).
- `NEW-GATE`: the gate's own controls GATE-1 to GATE-30.
- `NEW-MUT`: mutant rows; the harness exists only off `main` and lands pinned with the tool revision
  (R6.GATE.10, OBL-24).
- `NEW-IN-RUNNER`: the runner file exists but records the row under no known id.

A requirement is `EXISTING` when all its controls are, `NEW` when any is new, otherwise `CHANGE`.
This classification reads code, not results: "existing" means the predicate is implemented, not that it
holds. Only the gate on recorded evidence decides that.

## 3. Cross-cutting changes (every runner)

1. Evidence contract (R6.GATE.5, R6.GATE.7): every runner writes `control-records.json`
   (`oi-control-records/1`, records `{id, status, actual, predicate, evidence}`, status PASS, FAIL or
   NOT RUN, never SKIP) and retains raw evidence under `evidence/<job>/<id>/` with a `manifest.json`
   (`oi-control-evidence/1`: argv, exit file, result file, `--out` listing, input mutation with blob
   ids, bindings, sha256 of every file). Today the runners write summaries
   (`a1-controls.json`, `conformance-controls.json`, ...) with `{id, expected, predicate, actual,
   status}` and `conformance_controls.py` still emits SKIP. One shared recorder module in
   `tools/ledger_coverage/adapters/` replaces the per-runner `record` helpers.
2. Group-error ids and diagnostic keys become records (C-7); the purity job's `outcome` is recorded as
   Z9-STAGED.
3. The independent gate (sec. 16) and the requirement list's drift check: new code, importing nothing
   from the tool's package (R6.GATE.8).
4. The CI job (R6.GATE.14): runner steps, the mutation step and the gate step in the pinned workflow
   `.github/workflows/ledger-coverage.yml` (the only workflow path the landing may touch, R6.PLACE.8),
   with a marker step "control expectations hold".

## 4. Expectation rows by category

| Category | Rows |
|---|---|
| EXISTING | 110 |
| CHANGE | 226 (174 of them only for the restored case) |
| CHANGE-RENAME | 40 (RDIR-1 to RDIR-25, RDIR-12b, TT1 to TT14) |
| NEW-RUNNER | 44 |
| NEW-GATE | 30 |
| NEW-MUT | 107 |
| NEW-IN-RUNNER | 1 (Z9-STAGED, recorded as `outcome`) |
| Total | 558 |

By runner file:

| Runner (as the expectation file names it) | Exists on this branch | EXISTING | CHANGE | RENAME | NEW |
|---|---|---|---|---|---|
| `a1_controls.py` | yes | 23 | 71 | 0 | 0 |
| `a1_conformance.py` | yes | 0 | 47 | 0 | 0 |
| `conformance_controls.py` | yes | 45 | 36 | 0 | 0 |
| `controls_engine.py` | yes | 9 | 61 | 14 | 0 |
| `synthetic_fixture.py` | yes | 25 | 11 | 0 | 0 |
| `record_directory_controls.py` | yes (via the cherry-picked r4/r5 commits; not on `main`) | 8 | 0 | 26 | 0 |
| `selftest.py` | yes | 0 | 0 | 0 | 1 (Z9-STAGED) |
| `gate self-test` | no: new | - | - | - | 30 |
| `ledger-coverage-suite-ci.yml step 9-mutation (mutation harness)` | no: the workflow and its embedded harness exist only on the disposable branch of 233412cc7; the harness lands under `tools/ledger_coverage/` (pinned) and the step in `ledger-coverage.yml` | - | - | - | 107 |
| `null` | no runner | - | - | - | 44 |

The `file:line` cites of the expectation file locate code at a37992449 (provenance, sec. 32 adoption
trace); R6.GATE.2 requires `runner` to be the predicate's `file:line` and the record id to equal `id`.
Any line moved by this revision makes the cite stale; whether the gate checks the line (it reads
only "the recorded id equals `id`") is open question Q5.

Rows without a runner (44): composites EI7, GV7, S11-2, TR28, TR45; EI14-dispatch, TR45-opC (admitted
NOT RUN); EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer, TR52-consumer (OBL-19);
RECLINT-ORPHAN, REPRO-DOUBLE, RT-O9-L2, S11-7; CLASS-RETAINED, CLASS-UNLEDGERED, CLASS-PROV-AMBIGUOUS,
CLASS-PIN-TARGET, CLASS-RECORD-CHECKS, HIT-REPLACEMENT, DELEG-RECDIR, DELEG-REGEN, PROF-PARAMS-LINT,
PROF-LANDING-LIST, RULE-MINLIT, RULE-ZEROFP, OUT-CONFINED, REPRO-PYVER, RT-M, RT-SHIFT, SIDE-NONREG,
VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT, LC-1 to LC-7, REP-BUILD. A composite needs no runner of its own;
the gate composes it (R6.GATE.9).

Rows admitting NOT RUN (10): RT-T, TR5, G-A1, RT-L2, RT-O9-L2 (depends on RT-L2), EI14-dispatch, EI14
(composite), TR45-opB, TR45-opC, TR45 (composite). TR45-opB, TR45-opC, TR45 are deferred by owner
decision A1 (release check constantly false); their runner records NOT RUN with the deferral reason
(C-4, round-4 nit 1).

## 5. Requirements by group

| Group | Requirements | Existing control logic | Control change | New control/runner | No control: kind (verification) |
|---|---|---|---|---|---|
| STAT | 10 | 0 | 0 | 0 | governance 5, scope 1, status 4 |
| NOTE | 13 | 1 | 1 | 0 | definition 11 |
| PUR | 12 | 1 | 4 | 1 | scope 6 |
| PIPE | 15 | 1 | 7 | 1 | definition 1, testable 5 |
| ANCH | 19 | 1 | 14 | 3 | testable 1 |
| HP | 14 | 0 | 11 | 0 | testable 3 |
| CTX | 12 | 0 | 10 | 0 | definition 1, testable 1 |
| OUT | 28 | 5 | 17 | 2 | testable 4 |
| SPLIT | 3 | 0 | 1 | 0 | obligation 1, scope 1 |
| PROF | 12 | 1 | 8 | 2 | obligation 1 |
| RULE | 13 | 0 | 11 | 2 | - |
| REC | 25 | 3 | 18 | 4 | - |
| DENY | 6 | 0 | 5 | 0 | obligation 1 |
| DELEG | 18 | 3 | 12 | 2 | obligation 1 |
| HIT | 6 | 1 | 4 | 1 | - |
| CLASS | 12 | 1 | 3 | 8 | - |
| GATE | 16 | 0 | 0 | 16 | - |
| CTRL | 30 | 0 | 13 | 17 | - |
| PLAN | 18 | 7 | 7 | 3 | obligation 1 |
| PLACE | 12 | 0 | 5 | 2 | governance 5 |
| TREE | 19 | 0 | 15 | 3 | definition 1 |
| RDIR | 14 | 0 | 3 | 11 | - |
| ITEM2 | 4 | 3 | 1 | 0 | - |
| RECON | 21 | 0 | 19 | 2 | - |
| CORE | 8 | 3 | 2 | 3 | - |
| CFG | 8 | 2 | 6 | 0 | - |
| ADAPT | 6 | 1 | 4 | 1 | - |
| A1CFG | 7 | 1 | 4 | 2 | - |
| SYN | 3 | 2 | 1 | 0 | - |
| VALID | 4 | 1 | 3 | 0 | - |
| REPRO | 4 | 0 | 1 | 3 | - |
| EVID | 8 | 1 | 1 | 5 | governance 1 |
| OBL | 28 | 0 | 0 | 0 | obligation 28 |

Totals: 39 EXISTING, 211 CHANGE, 94 NEW, 84 with no control (status 4, scope 8, definition 14,
governance 11, obligation 33, and testable 14: see blocker B1).

## 6. Obligations that gate the tool's landing, and their discharge

| Obligation | Discharge on this branch | External dependency |
|---|---|---|
| OBL-13 RT-L2 release | runner exists (a1_controls.py); RT-L2 to run at `X` = `C` = `X_rep` with predicted `M` = `M0` plus the candidate's landing paths; REP-BUILD (new) builds `X_rep` from the pinned ledger and edit list (blobs ba37c1cd... and ec384fdf..., present in the object store, sha256 verified) | a reviewed reconciliation record for `AGENTS.md` bound to the exact `H`, `M`, `C` blobs, passing record lint, named from a commit outside the tool's landing paths, and side-change class records for the unclassified paths (blocker B4) |
| OBL-14 RT-O9-L2 | new runner; runs with RT-L2 on the predicted `M` plus a stand-in record directory | as OBL-13 |
| OBL-19 consumer halves | EI7-consumer, TR15/TR50/TR51/TR52-consumer: new runners (consumer predicates over retained results, landing record and snapshot) | none |
| OBL-20 second directions | 174 rows need only the restored case executed and recorded; 217 rows carry VD-RESTORE | 42 rows in scope record no second direction in the adopted file (blocker B2) |
| OBL-21 corrections VD-1 to VD-12, RD-12, RD-35 | VD-1 is the gate (first deliverable); VD-2/VD-3 engine changes with VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT; VD-4/VD-5 TT7, TT2; VD-6 S11-7; VD-7 A9r, A11r; VD-8 SW1; VD-9 Z9f; VD-10 emitted quantities; VD-11 RT-T0; VD-12 sitemap `read_entries`; RD-12 SIDE-NONREG; RD-35 items | none |
| OBL-22 identifier migration | 40 rows renamed (O9-n to RDIR-n, R1-R14 to TT1-TT14, RC1-RC13, Dir2-Dir5, `outcome` to Z9-STAGED, reason strings) per MIGRATION.json | owner's advance approval and independent non-author review (AGENTS.md sec. A.48 item 3) (question Q1) |
| OBL-23 `T1'`-input evidence | N10, N11, RT-D, RT-I7, RT-I7A, RT-DR3W, RT-T0 run at `X_rep`; item11-T1p stays candidate evidence | none beyond OBL-13's `X_rep` |
| OBL-24 mutation evidence | land the harness (from the disposable branch of 233412cc7, with mutate_o9.py and mutants_o9.py), pinned, under `tools/ledger_coverage/`; renumber the o9 set to RDIR-m1 to RDIR-m17; write `mutation-records.json`; add K08, I06, P01 distinguishing controls (C08 is TR52-consumer) | the mutation run is heavy: CI only (sec. 9) |
| OBL-25 runner-only predicates | the 32 RD-24 predicates checked against their requirements; the weak ones of C-3 emit the asserted quantity | none |
| OBL-28 C-1 to C-28, Q12, RE-13, RE-18, RE-19, Q13, RE-27, RE-29, OC-3 | per row of the OBL-28 table; RE-18/LC-7 stays REVIEW_REQUIRED as expected (R6.TREE.12); RE-27 and RE-29 are review items | RE-27, RE-29: independent review |

Not gating the tool's landing (out of scope here): OBL-1 to OBL-12, OBL-15, OBL-16, OBL-27 (plan
freeze or retirement execution); OBL-17 (deferred); OBL-18 (post-landing dispatch); OBL-26
(certification of the landed revision).

## 7. Blockers (cannot be implemented as written; reported, no exception introduced)

- **B1. Testable requirements without a control.** 14 requirements of kind `testable` have an empty
  control list and verification `controls` in REQUIREMENTS.json: R6.PIPE.1, R6.PIPE.4, R6.PIPE.6,
  R6.PIPE.7, R6.PIPE.8, R6.ANCH.8, R6.HP.1, R6.HP.5, R6.HP.14, R6.CTX.8, R6.OUT.16, R6.OUT.22,
  R6.OUT.25, R6.OUT.28. Under R6.GATE.12 each is `correspondence-orphan-requirement`, so the gate cannot
  hold on the adopted files. DESIGN-r6.md ("Requirements of sections 0 to 8 with no control") calls each
  "a named blocker on the correspondence check"; OBL-28 C-26 asks for one control each. A control is a
  new expectation row, and EXPECTATIONS.json and REQUIREMENTS.json are adopted: closing B1 needs an
  owner-approved expectation change.
- **B2. Rows in the both-directions scope without a second direction.** 42 rows record none:
  N3 to N18 (with N3-config-route, N16-file, N18-record), R15, R18, R18-engine, R19, R19-engine, RT-L,
  RT-L2, RT-X, TT1 to TT14, Z9h. R6.CTRL.3 states the count; R6.GATE.9 makes each `direction-missing`,
  a gate FAIL. OBL-20 is discharged by a recorded second direction: that is an expectation-file change,
  needing owner approval.
- **B3. Orphan row TR28.** The composite row TR28 lists R6.REC.18 and R6.CTRL.23, neither of which names
  it (they name TR28-tool and TR28-consumer). Under R6.GATE.12 ("every row is named by some
  requirement") it is `correspondence-orphan-row`. Closing it needs a requirement-list or expectation
  change, or a ruling that a composite is covered through its components (not stated in r6).
- **B4. RT-L2 needs an external reviewed record.** OBL-13 gates the tool's landing on RT-L2 run and
  PASS. That needs a reviewed reconciliation record for `AGENTS.md`, bound to exact blobs, named from a
  commit outside the tool's landing paths, and side-change class records. Their drafting and independent
  review are outside this branch's paths and authority. Until they exist RT-L2 and RT-O9-L2 are
  admitted NOT RUN (the gate can hold), but OBL-13 and OBL-14 stay open, so the landing decision cannot
  be made.

B1 to B3 mean the gate returns GATE_FAIL on the adopted expectation file whatever the implementation
does. This is a finding for the owner: the adopted requirements and expectations cannot be met without
introducing exceptions. Not introducing exceptions requires an owner-approved expectation change.

## 8. Order of work and size

1. The independent gate, `tools/ledger_coverage/gate/control_gate.py` (stdlib only; imports nothing from
   the tool's package, checked by its self-test). It provides the expectation-file schema and invariant
   vocabulary, the correspondence check against REQUIREMENTS.json, record, mutation-record and manifest
   validation, declarative and procedural evaluation, composites, NOT RUN with release checks,
   `gate-result.json` (`oi-control-gate/1`), and the self-test GATE-1 to GATE-30 on in-memory fixtures
   (VOID 70 on a self-test failure). About 1,500 lines.
2. The shared evidence recorder and the conversion of the runners to `control-records.json` with
   manifests. About 800 lines, plus mechanical edits at roughly 600 record calls.
3. Migration (OBL-22), once approved: about 300 lines.
4. The 44 new runners, then the 174 restored cases and the other CHANGE rows. About 4,000 to 5,000
   lines.
5. OBL-21 engine corrections, then the C-rows of OBL-28. About 1,000 to 1,500 lines.
6. The mutation harness landing and the CI job. About 1,500 lines, mostly existing code.

Total of the order of 10,000 changed lines. This is a multi-session tool revision; each stage is pushed
as a WIP checkpoint by the coordinator.

## 9. What runs where (AGENTS.md sec. A.40)

Locally (bounded): the gate's self-test; the gate over the adopted files (correspondence, schema,
direction); the entry point's self-test; the staged purity lint; unit tests of new code.

CI only: the conformance controls, A1 conformance and A1 controls over the real tree, the synthetic
fixture, the mutation run (sets c1, c2, v60e, cache, o9; hours), REPRO-DOUBLE, and the gate over the
complete record set. These run as one job in `.github/workflows/ledger-coverage.yml` on the exact
implementation commit, as the disposable CI validation run of R6.PLACE.11. That run is a launch that
needs the owner's approval; nothing is dispatched from this branch.

## 10. Open questions for the owner

- Q1. Does the implementation authorization count as the advance approval that AGENTS.md sec. A.48
  item 3 and OBL-22 require for the identifier migration, or is a separate approval needed? Until it is
  answered, the 40 renamed rows stay `missing-id`.
- Q2. B1 to B3: approve an expectation change (new rows for the 14 requirements, second directions for
  the 42 rows, TR28's naming), or rule otherwise.
- Q3. R6.PLACE.8 allows the landing to add paths only under `tools/`, the tool's audit directory and the
  pinned workflow. Is this directory the tool's audit directory (R6.PLACE.5), or should the plan move
  under `ledger-coverage-tool-20261123/`?
- Q4. CI trigger: the pinned workflow is dispatch-only and refuses any ref but `main` in its pre-run
  check. The suite and gate job needs either an owner-approved dispatch of the exact commit (R6.PLACE.11)
  or a `pull_request` trigger, about which r6 says nothing.
- Q5. The `runner` field cites `file:line` at a37992449. When this revision moves a line, is the field
  updated by an expectation change, or does the gate check only that the recorded id equals `id`
  (R6.GATE.2)?
- Q6. Release checks are stated in prose. The gate evaluates each by a fixed evaluator keyed to its exact
  text; an unknown text is `file-invalid`. Is that the intended reading of R6.GATE.15?

## 11. State of the branch (WIP / UNVERIFIED)

Done:

- The gate, `tools/ledger_coverage/gate/control_gate.py`, and its self-test, `gate_selftest.py` (GATE-1 to
  GATE-30, each case a fixture run in-process; standard library only, checked by an AST scan of both files).
  Six countercontrol mutants of the gate were each caught by the intended GATE row: duplicate detection
  (GATE-3), the RT-L2 release check (GATE-11), composite precedence (GATE-28), the sha256 check (GATE-9),
  direction-missing (GATE-27), the sweep count (GATE-10).
- The runner evidence contract, `tools/ledger_coverage/adapters/control_records.py`, wired into
  `a1_controls.py`, with restored cases for the rule-widening rows.
- The tool's own self-test still passes with the gate files in the package (86 controls).

Gate over the adopted files (local; only the self-test's records and the pilot): GATE_FAIL, as section 7
predicts. Findings: `correspondence-orphan-requirement` 14 (B1), `direction-missing` 42 (B2),
`correspondence-orphan-row` 1 (TR28, B3), and `missing-id` for every row without a record. All 30 GATE
rows hold against the adopted expectations. Pilot on the `rules` group of `a1_controls.py` (harness
admission, the staged draft configuration): A1r, A3r, A6r, A8r, A10r and A11r hold. A2r, A4r, A5r, A7r and
A9r still lack evidence their expectations name (attested invariants, bindings, named cases, the `ast`
procedure inputs).

- **B5. Compound invariants.** R6.GATE.3 says `invariants` holds single-key objects. 28 invariant objects of
  the adopted file have two keys (for example `{"all": ..., "have": ...}`, `{"condition": "RC11", "holds":
  ...}`), all from the vocabulary of sec. 16.10. Read strictly, the file is invalid (GATE_ERROR). The gate
  accepts an object whose every key is in the vocabulary, evaluates it as one invariant, and lists each
  occurrence in `gate-result.json` `compound_invariants`. This reading is for the owner to confirm or
  correct.

Limitations of the gate as implemented, each to close or to put to the owner:

- L1. Invariants. The gate computes `no_stop`, `stop_class_in`, `admission_mode`, `admission_mode_not`,
  `not_class`, `items_include`, `tool_run_exit`, `stderr_json_outcome`, `no_result_written`,
  `composite_status` and `component_results_preserved` from the retained results. Every other key, and
  every compound invariant, must be attested in a sha256-checked file of the case and equal the expected
  value. Many values are prose ("exactly one FAIL item names the site"), so an attested value amounts to a
  runner's statement checked only for presence and integrity. Each key needs its own evaluator before it
  is independent extraction in the sense of R6.GATE.8.
- L2. Release checks. TR5's check and the constant-false deferral are evaluated from git objects or a
  constant. The checks of EI14-dispatch, RT-L2 and RT-O9-L2, and RT-T read release facts retained in the
  evidence named at the commit under check (`--release-evidence`). An absent fact counts as false, which
  admits NOT RUN.
- L3. Count keys. The adopted file uses keys outside R6.GATE.3's grammar (dotted paths such as
  `region_lines.count`, `sites[...]`, and plain keys such as `merger_groups` and `sites_swept`). The gate reads
  them from the result, falling back to an attested value.
- L4. NO_ITEM and ITEM are evaluated over the items that the case's `classes_exact` filter selects, when it
  states one.
- L5. A `sites` entry without a `subject` (for example "all other merger-group sites") is attested.

## 12. What must run in CI for the exact-head check

Nothing has been dispatched. One job in `.github/workflows/ledger-coverage.yml`, on the exact
implementation commit (a launch that needs the owner's approval, R6.PLACE.11 and AGENTS.md sec. A.40):

1. Pre-run pin check of the tool files against the configuration under test (a re-staged configuration
   whose `tool.files` includes the gate and recorder files).
2. The entry point's self-test (`python3 -I -S -B tools/ledger_coverage.py self-test`).
3. The staged purity lint (`adapters/staged_purity_lint.py`).
4. The synthetic fixture (`adapters/synthetic_fixture.py`), the conformance controls
   (`adapters/conformance_controls.py`) and the A1 conformance (`adapters/a1_conformance.py`).
5. The record-directory controls (`adapters/record_directory_controls.py`).
6. The A1 controls (`adapters/a1_controls.py --main M0`, including the sweeps), once without `--main` (USAGE).
7. Y8 (`--syn-engine`).
8. The mutation run, sets c1, c2, v60e, cache and o9 (renamed RDIR-m1 to RDIR-m17), writing
   `mutation-records.json`.
9. REPRO-DOUBLE (every operation run twice into fresh `--out` directories).
10. The gate: `python3 -I -S -B tools/ledger_coverage/gate/control_gate.py --expectations
    verification/audits/foundations/a1exit-design-r6-20261125/EXPECTATIONS.json --requirements
    verification/audits/foundations/a1exit-design-r6-20261125/REQUIREMENTS.json --records <each job's
    control-records.json> --mutation-records <file> --repo . --out <dir>`, its exit status the step's
    conclusion, and a marker step "control expectations hold". Upload `gate-result.json` and the evidence
    with its manifest digest.

Runners 2 to 9 must first emit `control-records.json` and evidence (only `a1_controls.py` does so). The
gate cannot hold until B1 to B3 are resolved by an owner-approved expectation change.

## Appendix: per-row classification (generated from EXPECTATIONS.json and the runner sources)

| Row | Category | Runner | Notes |
|---|---|---|---|
| `A10r` | CHANGE | a1_controls.py:653 | restore |
| `A11r` | CHANGE | a1_controls.py:653 | restore; flag |
| `A12r` | EXISTING | conformance_controls.py:2494 | - |
| `A1r` | CHANGE | a1_controls.py:653 | restore |
| `A2r` | CHANGE | a1_controls.py:653 | restore; flag |
| `A3r` | CHANGE | a1_controls.py:653 | restore |
| `A4r` | CHANGE | a1_controls.py:668 | restore |
| `A5r` | CHANGE | a1_controls.py:753 | restore |
| `A5r-generic` | CHANGE | controls_engine.py:634 | flag |
| `A6r` | CHANGE | a1_controls.py:653 | restore |
| `A7r` | CHANGE | a1_controls.py:679 | restore |
| `A8r` | CHANGE | a1_controls.py:653 | restore |
| `A9r` | CHANGE | a1_controls.py:653 | restore; flag |
| `ACCEPT-SCHEMA` | EXISTING | conformance_controls.py:514 | - |
| `ADM-CONFIG-AT-F` | EXISTING | conformance_controls.py:177 | - |
| `B1` | CHANGE | controls_engine.py:334 | restore |
| `B2` | CHANGE | controls_engine.py:343 | restore |
| `B3` | CHANGE | controls_engine.py:353 | restore |
| `B4` | CHANGE | controls_engine.py:357 | restore |
| `B4-MEANING` | EXISTING | conformance_controls.py:1734 | - |
| `B5` | CHANGE | controls_engine.py:361 | restore |
| `B6` | CHANGE | controls_engine.py:366 | restore |
| `CHAIN-REFUSAL` | EXISTING | a1_controls.py:1150 | - |
| `CONFIG-LINT` | EXISTING | conformance_controls.py:1698 | - |
| `E-A1r` | CHANGE | controls_engine.py:642 | flag |
| `E-A2r` | CHANGE | controls_engine.py:643 | flag |
| `E-A3r` | CHANGE | controls_engine.py:645 | flag |
| `E-A6r` | CHANGE | controls_engine.py:639 | flag |
| `E-A8r` | CHANGE | controls_engine.py:641 | flag |
| `E-L1` | EXISTING | controls_engine.py:623 | - |
| `E-L3` | EXISTING | controls_engine.py:625 | - |
| `E-S1r` | CHANGE | controls_engine.py:628 | flag |
| `E-S2r` | CHANGE | controls_engine.py:630 | flag |
| `EI1` | EXISTING | conformance_controls.py:265 | - |
| `EI10` | CHANGE | conformance_controls.py:1388 | restore |
| `EI11` | CHANGE | conformance_controls.py:1405 | restore |
| `EI12` | CHANGE | conformance_controls.py:1421 | restore |
| `EI13` | CHANGE | conformance_controls.py:1458 | restore |
| `EI14` | CHANGE | conformance_controls.py:1475 | not-run; admits NOT RUN |
| `EI14-dispatch` | NEW-RUNNER | null | admits NOT RUN |
| `EI15` | EXISTING | conformance_controls.py:1500 | - |
| `EI2` | EXISTING | conformance_controls.py:274 | - |
| `EI2-consumer` | EXISTING | conformance_controls.py:600 | - |
| `EI3` | EXISTING | conformance_controls.py:610 | - |
| `EI4` | EXISTING | conformance_controls.py:321 | - |
| `EI5` | EXISTING | conformance_controls.py:662 | - |
| `EI6` | EXISTING | conformance_controls.py:1545 | - |
| `EI7` | NEW-RUNNER | null | - |
| `EI7-consumer` | NEW-RUNNER | null | - |
| `EI7-tool` | EXISTING | conformance_controls.py:441 | - |
| `EI8` | CHANGE | conformance_controls.py:1339 | restore |
| `EI9` | CHANGE | conformance_controls.py:1360 | restore |
| `G-A1` | CHANGE | conformance_controls.py:2434 | not-run; admits NOT RUN |
| `G1` | CHANGE | a1_controls.py:815 | restore |
| `G2` | CHANGE | a1_controls.py:818 | restore |
| `G3` | CHANGE | a1_controls.py:823 | restore; flag |
| `G4` | EXISTING | conformance_controls.py:2332 | - |
| `G5` | CHANGE | conformance_controls.py:2380 | flag |
| `G6` | EXISTING | conformance_controls.py:2402 | - |
| `G7` | EXISTING | conformance_controls.py:2430 | - |
| `G8` | CHANGE | conformance_controls.py:2355 | restore |
| `G9` | EXISTING | conformance_controls.py:2343 | - |
| `GV-CACHE` | EXISTING | conformance_controls.py:1058 | - |
| `GV-CACHE-AFTER-READ` | EXISTING | conformance_controls.py:1145 | - |
| `GV-CACHE-IMMUTABLE` | EXISTING | conformance_controls.py:1154 | - |
| `GV-CACHE-KEY` | EXISTING | conformance_controls.py:1122 | - |
| `GV1` | EXISTING | conformance_controls.py:869 | - |
| `GV2` | EXISTING | conformance_controls.py:882 | - |
| `GV3` | EXISTING | conformance_controls.py:903 | - |
| `GV4` | CHANGE | conformance_controls.py:943 | restore |
| `GV5` | EXISTING | conformance_controls.py:981 | - |
| `GV6` | CHANGE | conformance_controls.py:343 | restore |
| `GV6-disk` | CHANGE | conformance_controls.py:1008 | restore |
| `GV7` | NEW-RUNNER | null | - |
| `GV7-consumer` | CHANGE | conformance_controls.py:624 | restore |
| `GV7-tool` | CHANGE | conformance_controls.py:379 | restore |
| `H1` | CHANGE | controls_engine.py:379 | restore |
| `H2` | CHANGE | controls_engine.py:385 | restore |
| `H3` | CHANGE | controls_engine.py:388 | restore |
| `H4` | CHANGE | controls_engine.py:393 | restore |
| `H5` | CHANGE | controls_engine.py:400 | restore |
| `H6` | CHANGE | controls_engine.py:404 | restore |
| `H7` | CHANGE | controls_engine.py:432 | restore |
| `I2-1` | EXISTING | record_directory_controls.py:646 | - |
| `I2-2` | EXISTING | record_directory_controls.py:662 | - |
| `I2-3` | EXISTING | record_directory_controls.py:675 | - |
| `I2-4` | EXISTING | record_directory_controls.py:697 | - |
| `I2-5` | EXISTING | record_directory_controls.py:709 | - |
| `I2-6` | EXISTING | record_directory_controls.py:724 | - |
| `I2-7` | EXISTING | record_directory_controls.py:747 | - |
| `I2-8` | EXISTING | record_directory_controls.py:774 | - |
| `K1` | CHANGE | controls_engine.py:272 | restore |
| `K1-GRAPH` | EXISTING | a1_controls.py:1139 | - |
| `K10` | CHANGE | controls_engine.py:281 | restore |
| `K2` | CHANGE | controls_engine.py:282 | restore |
| `K3` | CHANGE | controls_engine.py:287 | restore; flag |
| `K4` | CHANGE | controls_engine.py:292 | restore; flag |
| `K5` | CHANGE | controls_engine.py:297 | restore |
| `K6` | CHANGE | controls_engine.py:302 | restore |
| `K7` | CHANGE | controls_engine.py:310 | restore |
| `K8` | CHANGE | controls_engine.py:313 | restore |
| `K9` | CHANGE | controls_engine.py:320 | restore |
| `L1` | CHANGE | a1_controls.py:586 | restore |
| `L2` | CHANGE | a1_controls.py:593 | restore |
| `L3` | CHANGE | a1_controls.py:595 | restore |
| `L4` | CHANGE | a1_controls.py:597 | restore |
| `LN1` | EXISTING | conformance_controls.py:2072 | - |
| `LN10` | CHANGE | conformance_controls.py:2223 | flag |
| `LN2` | EXISTING | conformance_controls.py:2079 | - |
| `LN3` | EXISTING | conformance_controls.py:2091 | - |
| `LN4` | EXISTING | conformance_controls.py:2127 | - |
| `LN5` | EXISTING | conformance_controls.py:2164 | - |
| `LN6` | EXISTING | conformance_controls.py:2175 | - |
| `LN7` | EXISTING | conformance_controls.py:2193 | - |
| `LN8` | EXISTING | conformance_controls.py:2210 | - |
| `M1` | EXISTING | controls_engine.py:233 | - |
| `M10` | CHANGE | synthetic_fixture.py:543 | restore |
| `M11` | CHANGE | controls_engine.py:258 | restore |
| `M2` | CHANGE | controls_engine.py:236 | restore |
| `M3` | EXISTING | controls_engine.py:247 | - |
| `M4` | CHANGE | controls_engine.py:249 | restore |
| `M5` | CHANGE | controls_engine.py:250 | restore |
| `M6` | CHANGE | controls_engine.py:254 | restore |
| `M7` | CHANGE | a1_controls.py:206 | restore |
| `M8` | CHANGE | a1_controls.py:209 | restore |
| `M9` | CHANGE | a1_controls.py:211 | restore |
| `N-W` | CHANGE | a1_controls.py:600 | restore |
| `N1` | EXISTING | controls_engine.py:574 | - |
| `N10` | CHANGE | a1_conformance.py:505 | restore; flag |
| `N11` | CHANGE | a1_conformance.py:517 | restore; flag |
| `N12` | CHANGE | a1_conformance.py:477 | restore |
| `N13` | CHANGE | a1_conformance.py:480 | restore |
| `N14` | CHANGE | a1_conformance.py:482 | restore |
| `N15` | CHANGE | a1_conformance.py:484 | restore |
| `N16` | CHANGE | a1_conformance.py:488 | restore |
| `N16-file` | CHANGE | a1_conformance.py:490 | restore |
| `N17` | CHANGE | a1_conformance.py:493 | restore |
| `N18` | CHANGE | a1_conformance.py:494 | restore |
| `N18-record` | CHANGE | a1_conformance.py:496 | restore |
| `N2` | EXISTING | controls_engine.py:577 | - |
| `N3` | CHANGE | a1_conformance.py:435 | restore |
| `N3-config-route` | CHANGE | a1_conformance.py:542 | restore |
| `N4` | CHANGE | a1_conformance.py:456 | restore |
| `N5` | CHANGE | a1_conformance.py:460 | restore |
| `N6` | CHANGE | a1_conformance.py:461 | restore |
| `N7` | CHANGE | a1_conformance.py:465 | restore |
| `N8` | CHANGE | a1_conformance.py:470 | restore |
| `N9` | CHANGE | a1_conformance.py:471 | restore |
| `O1` | CHANGE | controls_engine.py:462 | restore; flag |
| `O2` | CHANGE | controls_engine.py:465 | restore; flag |
| `O3` | CHANGE | controls_engine.py:469 | restore; flag |
| `O3-FILTER` | EXISTING | conformance_controls.py:719 | - |
| `O5` | CHANGE | controls_engine.py:470 | restore; flag |
| `O6` | CHANGE | controls_engine.py:473 | restore; flag |
| `O7` | CHANGE | controls_engine.py:475 | restore; flag |
| `O8` | CHANGE | controls_engine.py:479 | restore |
| `O9` | CHANGE | controls_engine.py:461 | restore |
| `R15` | CHANGE | controls_engine.py:566 | restore |
| `R16` | CHANGE | conformance_controls.py:2469 | restore |
| `R17` | CHANGE | conformance_controls.py:2472 | restore |
| `R18` | CHANGE | a1_conformance.py:552 | restore |
| `R18-engine` | CHANGE | controls_engine.py:513 | restore |
| `R19` | CHANGE | a1_conformance.py:563 | restore |
| `R19-engine` | CHANGE | controls_engine.py:561 | restore |
| `R3-F2` | EXISTING | conformance_controls.py:1789 | - |
| `R4-B3` | EXISTING | conformance_controls.py:1864 | - |
| `R4-B3-DUP` | CHANGE | conformance_controls.py:1903 | flag |
| `R5-N6` | EXISTING | conformance_controls.py:1924 | - |
| `R6-G6` | EXISTING | conformance_controls.py:2235 | - |
| `R8-S6` | EXISTING | controls_engine.py:546 | - |
| `RDIR-1` | CHANGE-RENAME | record_directory_controls.py:242 | migrated from O9-1 |
| `RDIR-10` | CHANGE-RENAME | record_directory_controls.py:337 | migrated from O9-10 |
| `RDIR-11` | CHANGE-RENAME | record_directory_controls.py:349 | migrated from O9-11 |
| `RDIR-12` | CHANGE-RENAME | record_directory_controls.py:357 | migrated from O9-12 |
| `RDIR-12b` | CHANGE-RENAME | record_directory_controls.py:368 | migrated from O9-12b |
| `RDIR-13` | CHANGE-RENAME | record_directory_controls.py:382 | migrated from O9-13 |
| `RDIR-14` | CHANGE-RENAME | record_directory_controls.py:397 | migrated from O9-14 |
| `RDIR-15` | CHANGE-RENAME | record_directory_controls.py:409 | migrated from O9-15 |
| `RDIR-16` | CHANGE-RENAME | record_directory_controls.py:420 | migrated from O9-16 |
| `RDIR-17` | CHANGE-RENAME | record_directory_controls.py:429 | migrated from O9-17 |
| `RDIR-18` | CHANGE-RENAME | record_directory_controls.py:410 | migrated from O9-18 |
| `RDIR-19` | CHANGE-RENAME | record_directory_controls.py:412 | migrated from O9-19 |
| `RDIR-2` | CHANGE-RENAME | record_directory_controls.py:252 | migrated from O9-2 |
| `RDIR-20` | CHANGE-RENAME | record_directory_controls.py:480 | migrated from O9-20 |
| `RDIR-21` | CHANGE-RENAME | record_directory_controls.py:491 | migrated from O9-21 |
| `RDIR-22` | CHANGE-RENAME | record_directory_controls.py:502 | migrated from O9-22 |
| `RDIR-23` | CHANGE-RENAME | record_directory_controls.py:526 | migrated from O9-23 |
| `RDIR-24` | CHANGE-RENAME | record_directory_controls.py:450 | migrated from O9-24 |
| `RDIR-25` | CHANGE-RENAME | record_directory_controls.py:538 | migrated from O9-25 |
| `RDIR-3` | CHANGE-RENAME | record_directory_controls.py:261 | migrated from O9-3 |
| `RDIR-4` | CHANGE-RENAME | record_directory_controls.py:270 | migrated from O9-4 |
| `RDIR-5` | CHANGE-RENAME | record_directory_controls.py:279 | migrated from O9-5 |
| `RDIR-6` | CHANGE-RENAME | record_directory_controls.py:287 | migrated from O9-6 |
| `RDIR-7` | CHANGE-RENAME | record_directory_controls.py:296 | migrated from O9-7 |
| `RDIR-8` | CHANGE-RENAME | record_directory_controls.py:313 | migrated from O9-8 |
| `RDIR-9` | CHANGE-RENAME | record_directory_controls.py:326 | migrated from O9-9 |
| `RECLINT-ORPHAN` | NEW-RUNNER | null | - |
| `REPRO-DOUBLE` | NEW-RUNNER | null | - |
| `RL` | EXISTING | controls_engine.py:548 | - |
| `RT-A` | CHANGE | a1_controls.py:171 | restore |
| `RT-C` | CHANGE | a1_controls.py:805 | restore |
| `RT-D` | CHANGE | a1_controls.py:374 | restore; flag |
| `RT-D-gr58` | EXISTING | a1_controls.py:389 | - |
| `RT-DR` | CHANGE | a1_controls.py:296 | restore |
| `RT-DR3W` | CHANGE | a1_controls.py:317 | flag |
| `RT-E` | EXISTING | a1_controls.py:224 | - |
| `RT-H0` | CHANGE | a1_controls.py:235 | restore; flag |
| `RT-I7` | CHANGE | a1_controls.py:327 | flag |
| `RT-I7A` | CHANGE | a1_controls.py:342 | flag |
| `RT-L` | CHANGE | a1_controls.py:930 | restore |
| `RT-L2` | CHANGE | a1_controls.py:976 | restore; not-run; flag; admits NOT RUN |
| `RT-O9` | EXISTING | a1_controls.py:1025 | - |
| `RT-O9-L2` | NEW-RUNNER | null | admits NOT RUN |
| `RT-T` | CHANGE | a1_controls.py:271 | not-run; flag; admits NOT RUN |
| `RT-T0` | CHANGE | a1_controls.py:262 | restore; flag |
| `RT-X` | CHANGE | a1_controls.py:921 | restore |
| `S11-1` | EXISTING | a1_controls.py:832 | - |
| `S11-10` | EXISTING | a1_controls.py:860 | - |
| `S11-11` | EXISTING | a1_controls.py:869 | - |
| `S11-12` | EXISTING | a1_controls.py:864 | - |
| `S11-13` | EXISTING | a1_controls.py:879 | - |
| `S11-14` | CHANGE | a1_controls.py:873 | flag |
| `S11-2` | NEW-RUNNER | null | - |
| `S11-2a` | EXISTING | a1_controls.py:902 | - |
| `S11-2b` | EXISTING | a1_controls.py:913 | - |
| `S11-2c` | EXISTING | a1_controls.py:218 | - |
| `S11-3` | EXISTING | a1_controls.py:887 | - |
| `S11-4` | EXISTING | a1_controls.py:893 | - |
| `S11-5` | EXISTING | a1_controls.py:841 | - |
| `S11-56` | CHANGE | a1_conformance.py:278 | restore |
| `S11-57a` | CHANGE | a1_conformance.py:299 | restore |
| `S11-57b` | CHANGE | a1_conformance.py:304 | restore |
| `S11-57c` | CHANGE | a1_conformance.py:318 | restore; flag |
| `S11-57d` | CHANGE | a1_conformance.py:326 | restore |
| `S11-58a-f` | CHANGE | a1_conformance.py:344 | restore; flag |
| `S11-58g` | CHANGE | a1_conformance.py:352 | restore; flag |
| `S11-58h` | CHANGE | a1_conformance.py:358 | restore; flag |
| `S11-58i` | CHANGE | a1_conformance.py:365 | restore |
| `S11-58j` | CHANGE | a1_conformance.py:373 | restore; flag |
| `S11-58k` | CHANGE | a1_conformance.py:386 | restore; flag |
| `S11-6` | EXISTING | a1_controls.py:841 | - |
| `S11-7` | NEW-RUNNER | null | - |
| `S11-8` | EXISTING | a1_controls.py:850 | - |
| `S11-9` | EXISTING | a1_controls.py:855 | - |
| `S1r` | CHANGE | a1_controls.py:572 | restore |
| `S2r` | CHANGE | a1_controls.py:578 | restore |
| `S4a` | EXISTING | conformance_controls.py:2543 | - |
| `S7-schema-and-checker` | CHANGE | synthetic_fixture.py:555 | flag |
| `SW1` | CHANGE | a1_controls.py:1240 | restore; flag |
| `SW2` | EXISTING | a1_controls.py:1238 | - |
| `TR1` | CHANGE | conformance_controls.py:157 | restore |
| `TR13` | CHANGE | conformance_controls.py:184 | restore |
| `TR14` | EXISTING | conformance_controls.py:541 | - |
| `TR14-tool` | CHANGE | conformance_controls.py:196 | restore |
| `TR15` | CHANGE | conformance_controls.py:211 | restore |
| `TR15-consumer` | NEW-RUNNER | null | - |
| `TR2` | CHANGE | conformance_controls.py:164 | restore |
| `TR28` | NEW-RUNNER | null | - |
| `TR28-consumer` | EXISTING | conformance_controls.py:578 | - |
| `TR28-tool` | CHANGE | conformance_controls.py:219 | restore |
| `TR29` | EXISTING | conformance_controls.py:591 | - |
| `TR29-tool` | CHANGE | conformance_controls.py:254 | restore |
| `TR3` | CHANGE | conformance_controls.py:170 | restore |
| `TR30` | EXISTING | conformance_controls.py:521 | - |
| `TR45` | NEW-RUNNER | null | admits NOT RUN |
| `TR45-opB` | CHANGE | conformance_controls.py:2263 | not-run; admits NOT RUN |
| `TR45-opC` | NEW-RUNNER | null | admits NOT RUN |
| `TR46` | CHANGE | conformance_controls.py:526 | restore |
| `TR48` | CHANGE | conformance_controls.py:228 | restore |
| `TR5` | CHANGE | conformance_controls.py:151 | restore; not-run; flag; admits NOT RUN |
| `TR5-sim` | CHANGE | conformance_controls.py:142 | restore |
| `TR50` | CHANGE | conformance_controls.py:239 | restore |
| `TR50-consumer` | NEW-RUNNER | null | - |
| `TR51` | CHANGE | conformance_controls.py:246 | restore |
| `TR51-consumer` | NEW-RUNNER | null | - |
| `TR52` | CHANGE | conformance_controls.py:224 | restore |
| `TR52-consumer` | NEW-RUNNER | null | - |
| `TT1` | CHANGE-RENAME | controls_engine.py:511 | migrated from R1 |
| `TT10` | CHANGE-RENAME | controls_engine.py:552 | migrated from R10 |
| `TT11` | CHANGE-RENAME | controls_engine.py:554 | migrated from R11 |
| `TT12` | CHANGE-RENAME | controls_engine.py:556 | migrated from R12 |
| `TT13` | CHANGE-RENAME | controls_engine.py:559 | migrated from R13 |
| `TT14` | CHANGE-RENAME | controls_engine.py:563 | migrated from R14 |
| `TT2` | CHANGE-RENAME | controls_engine.py:517 | migrated from R2 |
| `TT3` | CHANGE-RENAME | controls_engine.py:519 | migrated from R3 |
| `TT4` | CHANGE-RENAME | controls_engine.py:521 | migrated from R4 |
| `TT5` | CHANGE-RENAME | controls_engine.py:526 | migrated from R5 |
| `TT6` | CHANGE-RENAME | controls_engine.py:532 | migrated from R6 |
| `TT7` | CHANGE-RENAME | controls_engine.py:539 | migrated from R7 |
| `TT8` | CHANGE-RENAME | controls_engine.py:542 | migrated from R8 |
| `TT9` | CHANGE-RENAME | controls_engine.py:550 | migrated from R9 |
| `U1` | CHANGE | controls_engine.py:123 | restore |
| `U10` | CHANGE | controls_engine.py:157 | restore |
| `U11` | CHANGE | controls_engine.py:162 | restore |
| `U12` | CHANGE | controls_engine.py:166 | restore |
| `U14` | CHANGE | controls_engine.py:229 | flag |
| `U2` | CHANGE | controls_engine.py:126 | restore |
| `U3` | CHANGE | controls_engine.py:130 | restore |
| `U4` | CHANGE | controls_engine.py:133 | restore |
| `U5` | CHANGE | controls_engine.py:136 | restore |
| `U6` | CHANGE | controls_engine.py:141 | restore |
| `U7` | CHANGE | controls_engine.py:145 | restore |
| `U8` | CHANGE | controls_engine.py:148 | restore |
| `U9` | CHANGE | controls_engine.py:151 | restore |
| `V1` | CHANGE | a1_controls.py:466 | restore |
| `V10` | CHANGE | a1_controls.py:466 | restore |
| `V11` | CHANGE | a1_controls.py:466 | restore |
| `V12` | CHANGE | a1_controls.py:466 | restore |
| `V13` | CHANGE | a1_controls.py:466 | restore |
| `V14` | CHANGE | a1_controls.py:474 | restore |
| `V15` | CHANGE | a1_controls.py:499 | restore |
| `V16` | CHANGE | a1_controls.py:466 | restore |
| `V17` | CHANGE | a1_controls.py:466 | restore |
| `V18` | CHANGE | a1_controls.py:466 | restore |
| `V19` | CHANGE | a1_controls.py:466 | restore |
| `V2` | CHANGE | a1_controls.py:555 | restore |
| `V20` | CHANGE | a1_controls.py:466 | restore |
| `V21` | CHANGE | a1_controls.py:499 | restore |
| `V22` | CHANGE | a1_controls.py:485 | restore |
| `V23` | CHANGE | a1_controls.py:522 | restore |
| `V24` | CHANGE | a1_controls.py:526 | restore |
| `V25` | EXISTING | a1_controls.py:535 | - |
| `V26` | CHANGE | a1_controls.py:518 | restore |
| `V27` | CHANGE | a1_controls.py:493 | restore |
| `V27-glossary` | CHANGE | a1_controls.py:507 | restore |
| `V3` | CHANGE | a1_controls.py:466 | restore |
| `V3-countercontrol` | CHANGE | a1_controls.py:425 | flag |
| `V4` | CHANGE | a1_controls.py:493 | restore |
| `V5` | CHANGE | a1_controls.py:466 | restore |
| `V6` | CHANGE | a1_controls.py:478 | restore |
| `V7a` | CHANGE | a1_controls.py:560 | restore |
| `V7b` | CHANGE | a1_controls.py:565 | restore |
| `V7c` | CHANGE | a1_controls.py:570 | restore |
| `V9` | CHANGE | a1_controls.py:466 | restore |
| `WB1` | CHANGE | a1_conformance.py:94 | restore |
| `WB10` | CHANGE | a1_conformance.py:165 | restore |
| `WB11` | CHANGE | a1_conformance.py:173 | restore |
| `WB12` | CHANGE | a1_conformance.py:184 | restore |
| `WB13` | CHANGE | a1_conformance.py:193 | restore |
| `WB14` | CHANGE | a1_conformance.py:205 | restore |
| `WB15` | CHANGE | a1_conformance.py:210 | restore |
| `WB2` | CHANGE | a1_conformance.py:98 | restore |
| `WB3` | CHANGE | a1_conformance.py:103 | restore |
| `WB4` | CHANGE | a1_conformance.py:112 | restore |
| `WB5` | CHANGE | a1_conformance.py:120 | restore |
| `WB6` | CHANGE | a1_conformance.py:125 | restore |
| `WB7` | CHANGE | a1_conformance.py:129 | restore |
| `WB8` | CHANGE | a1_conformance.py:133 | restore |
| `WB9` | CHANGE | a1_conformance.py:140 | restore |
| `X1` | CHANGE | a1_controls.py:176 | restore |
| `X10` | EXISTING | synthetic_fixture.py:536 | - |
| `X11` | CHANGE | conformance_controls.py:472 | restore |
| `X2` | CHANGE | synthetic_fixture.py:478 | restore |
| `X3` | CHANGE | synthetic_fixture.py:482 | restore |
| `X4` | CHANGE | synthetic_fixture.py:485 | restore |
| `X5` | CHANGE | synthetic_fixture.py:487 | restore |
| `X6` | CHANGE | synthetic_fixture.py:490 | restore |
| `X7` | CHANGE | synthetic_fixture.py:504 | restore |
| `X8` | CHANGE | synthetic_fixture.py:510 | restore |
| `X9` | CHANGE | synthetic_fixture.py:517 | restore |
| `Y1` | EXISTING | synthetic_fixture.py:314 | - |
| `Y10` | EXISTING | synthetic_fixture.py:362 | - |
| `Y2` | EXISTING | synthetic_fixture.py:321 | - |
| `Y3` | EXISTING | synthetic_fixture.py:326 | - |
| `Y4` | EXISTING | synthetic_fixture.py:334 | - |
| `Y5` | EXISTING | synthetic_fixture.py:340 | - |
| `Y6` | EXISTING | synthetic_fixture.py:349 | - |
| `Y7` | EXISTING | synthetic_fixture.py:352 | - |
| `Y8` | EXISTING | a1_controls.py:1262 | - |
| `Y9` | EXISTING | synthetic_fixture.py:358 | - |
| `Z1` | EXISTING | synthetic_fixture.py:385 | - |
| `Z10` | EXISTING | synthetic_fixture.py:449 | - |
| `Z11` | EXISTING | conformance_controls.py:2524 | - |
| `Z2` | EXISTING | synthetic_fixture.py:386 | - |
| `Z3` | EXISTING | synthetic_fixture.py:387 | - |
| `Z4` | EXISTING | synthetic_fixture.py:388 | - |
| `Z5` | EXISTING | synthetic_fixture.py:389 | - |
| `Z6` | EXISTING | synthetic_fixture.py:390 | - |
| `Z6b` | EXISTING | synthetic_fixture.py:394 | - |
| `Z7` | EXISTING | synthetic_fixture.py:395 | - |
| `Z8` | EXISTING | synthetic_fixture.py:398 | - |
| `Z9-STAGED` | NEW-IN-RUNNER | selftest.py:30 | migrated from outcome (purity job record id) |
| `Z9a` | EXISTING | synthetic_fixture.py:570 | - |
| `Z9b` | EXISTING | synthetic_fixture.py:570 | - |
| `Z9c` | EXISTING | synthetic_fixture.py:571 | - |
| `Z9d` | EXISTING | synthetic_fixture.py:571 | - |
| `Z9e` | EXISTING | synthetic_fixture.py:572 | - |
| `Z9f` | CHANGE | synthetic_fixture.py:573 | flag |
| `Z9g` | EXISTING | a1_controls.py:1169 | - |
| `Z9h` | CHANGE | a1_controls.py:1175 | restore; flag |
| `item11-T1p` | CHANGE | a1_controls.py:396 | flag |
| `lint-ok` | EXISTING | controls_engine.py:638 | - |
| `rule-negative` | CHANGE | controls_engine.py:632 | flag |
| `GATE-1` | NEW-GATE | gate self-test | - |
| `GATE-2` | NEW-GATE | gate self-test | - |
| `GATE-3` | NEW-GATE | gate self-test | - |
| `GATE-4` | NEW-GATE | gate self-test | - |
| `GATE-5` | NEW-GATE | gate self-test | - |
| `GATE-6` | NEW-GATE | gate self-test | - |
| `GATE-7` | NEW-GATE | gate self-test | - |
| `GATE-8` | NEW-GATE | gate self-test | - |
| `GATE-9` | NEW-GATE | gate self-test | - |
| `GATE-10` | NEW-GATE | gate self-test | - |
| `GATE-11` | NEW-GATE | gate self-test | - |
| `GATE-12` | NEW-GATE | gate self-test | - |
| `GATE-13` | NEW-GATE | gate self-test | - |
| `GATE-14` | NEW-GATE | gate self-test | - |
| `GATE-15` | NEW-GATE | gate self-test | - |
| `GATE-16` | NEW-GATE | gate self-test | - |
| `GATE-17` | NEW-GATE | gate self-test | - |
| `GATE-18` | NEW-GATE | gate self-test | - |
| `GATE-19` | NEW-GATE | gate self-test | - |
| `GATE-20` | NEW-GATE | gate self-test | - |
| `GATE-21` | NEW-GATE | gate self-test | - |
| `GATE-22` | NEW-GATE | gate self-test | - |
| `GATE-23` | NEW-GATE | gate self-test | - |
| `GATE-24` | NEW-GATE | gate self-test | - |
| `GATE-25` | NEW-GATE | gate self-test | - |
| `GATE-26` | NEW-GATE | gate self-test | - |
| `MUT:c1:C01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C08` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C09` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C10` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C11` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c1:C12` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c2:D01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c2:D02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:c2:D03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:cache:K08` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:o9:RDIR-m1` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m1 |
| `MUT:o9:RDIR-m10` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m10 |
| `MUT:o9:RDIR-m11` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m11 |
| `MUT:o9:RDIR-m12` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m12 |
| `MUT:o9:RDIR-m13` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m13 |
| `MUT:o9:RDIR-m14` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m14 |
| `MUT:o9:RDIR-m15` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m15 |
| `MUT:o9:RDIR-m16` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m16 |
| `MUT:o9:RDIR-m17` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m17 |
| `MUT:o9:RDIR-m2` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m2 |
| `MUT:o9:RDIR-m3` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m3 |
| `MUT:o9:RDIR-m4` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m4 |
| `MUT:o9:RDIR-m5` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m5 |
| `MUT:o9:RDIR-m6` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m6 |
| `MUT:o9:RDIR-m7` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m7 |
| `MUT:o9:RDIR-m8` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m8 |
| `MUT:o9:RDIR-m9` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | migrated from o9:O9-m9 |
| `MUT:v60e:A01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A08` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A09` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A10` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A11` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A12` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A13` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:A14` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C08` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C09` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C10` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C11` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C12` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C13` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C14` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C15` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:C16` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:E01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:E02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:H01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:H02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:H03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I08` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I09` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I10` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I11` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I12` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I13` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:I14` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:O01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:O02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:P01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:R01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:R02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:R03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:U01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:U02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:U03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:U04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:U05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V01` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V02` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V03` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V04` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V05` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V06` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `MUT:v60e:V07` | NEW-MUT | ledger-coverage-suite-ci.yml step 9-mutation (mutation harness) | - |
| `CLASS-RETAINED` | NEW-RUNNER | null | - |
| `CLASS-UNLEDGERED` | NEW-RUNNER | null | - |
| `CLASS-PROV-AMBIGUOUS` | NEW-RUNNER | null | - |
| `CLASS-PIN-TARGET` | NEW-RUNNER | null | - |
| `CLASS-RECORD-CHECKS` | NEW-RUNNER | null | - |
| `HIT-REPLACEMENT` | NEW-RUNNER | null | - |
| `DELEG-RECDIR` | NEW-RUNNER | null | - |
| `PROF-PARAMS-LINT` | NEW-RUNNER | null | - |
| `PROF-LANDING-LIST` | NEW-RUNNER | null | - |
| `RULE-MINLIT` | NEW-RUNNER | null | - |
| `RULE-ZEROFP` | NEW-RUNNER | null | - |
| `OUT-CONFINED` | NEW-RUNNER | null | - |
| `REPRO-PYVER` | NEW-RUNNER | null | - |
| `RT-M` | NEW-RUNNER | null | - |
| `RT-SHIFT` | NEW-RUNNER | null | - |
| `SIDE-NONREG` | NEW-RUNNER | null | - |
| `VD2-HP-SEARCH` | NEW-RUNNER | null | - |
| `VD3-COUNT` | NEW-RUNNER | null | - |
| `VD3-CONTEXT` | NEW-RUNNER | null | - |
| `GATE-27` | NEW-GATE | gate self-test | - |
| `GATE-28` | NEW-GATE | gate self-test | - |
| `GATE-29` | NEW-GATE | gate self-test | - |
| `GATE-30` | NEW-GATE | gate self-test | - |
| `LC-1` | NEW-RUNNER | null | - |
| `LC-2` | NEW-RUNNER | null | - |
| `LC-3` | NEW-RUNNER | null | - |
| `LC-4` | NEW-RUNNER | null | - |
| `LC-5` | NEW-RUNNER | null | - |
| `LC-6` | NEW-RUNNER | null | - |
| `LC-7` | NEW-RUNNER | null | - |
| `DELEG-REGEN` | NEW-RUNNER | null | - |
| `REP-BUILD` | NEW-RUNNER | null | - |

## 13. Progress after the owner decision of 2026-11-26T04:39:58Z (WIP / UNVERIFIED)

- The plan lives in the tool's audit directory, an implementation choice the owner accepted.
- Design amendment 1 (B1, B2, B3, B5) is a separate branch under its own independent review. Run over the
  amended files with only the self-test's records, the gate reports only `missing-id` for rows that have no
  record, plus `status-not-allowed` on the 16 composites whose components have no record.
- Identifier migration (OBL-22, approved by the owner under AGENTS.md sec. A.48): the r5 directory controls
  O9-n become RDIR-n (runner and `controls.json`); the v2 four-tree controls R1 to R14 become TT1 to TT14; the
  record conditions R1 to R13 become RC1 to RC13; the directory conditions D2 to D5 become Dir2 to Dir5; the
  reason "(authority)" becomes "(directory not admitted)". Local checks: tool self-test PASS (86 controls,
  TT1 to TT14 among them); conformance 113 PASS and 2 NOT RUN (TR5, G-A1), RDIR-1 to RDIR-25 and RDIR-12b among
  them; A1 conformance 47 PASS.
- Still to migrate: the purity job's record id `outcome` (becomes Z9-STAGED when that runner gains the
  evidence contract); the o9 mutant names (RDIR-m1 to RDIR-m17), which go with the harness when it lands; the
  result field "authority match", which occurs in no tool file.

## 14. Progress on the evidence contract, second directions and release checks (WIP / UNVERIFIED)

Counted over the amended expectation file of design amendment 1 (572 rows), with the local records of the
engine controls, the staged purity lint, the synthetic fixture, the conformance controls (with the RDIR and I2
groups), the A1 conformance and an A1 controls run with sweeps: before this stage 30 rows held (the GATE rows) with
`missing-id` 542 and `status-not-allowed` 16; after it 89 hold, with `missing-id` 166 (107 mutant rows, 44 rows
with no runner, the rest ids no runner records yet), `raw-evidence-missing` 301, `declarative-mismatch` 55,
`status-actual-inconsistent` 312 and `status-not-allowed` 20. The gate reports GATE_FAIL; the counts measure
progress only.

Done:

- Every runner writes `control-records.json` and `evidence/<job>/<id>/` (`engine_controls.py` records the engine
  controls through a capture hook that the self-test and the preflight leave unset; `staged_purity_lint.py`
  records Z9-STAGED). In-process stage results are retained with argv `['in-process', label]` and the outcome of
  the tool's own outcome function. No runner emits SKIP.
- Second directions executed: the WB rows, the N rows evaluated by a mutated record, `M` or class set, R18, U14 and
  the unledgered engine controls U2, U4 to U9, U12, K1, K5, K6 and K8. U13 is retired and U15 is U14's
  wrong-region-hash case (C-7).
- New runners: HP-MERGE-PR and OUT-NOTRUNC (synthetic fixture). The merge cross-check now gives ERROR
  `CONFIG_INVALID` for a subject naming another pull-request number (R6.HP.1); it gave `CONFIG_INCONSISTENT`, and a
  subject naming #70 satisfied a pin of #7.
- RT-L2 with drift is recorded NOT RUN until a reviewed reconciliation record exists (R6.GATE.16); RT-O9 records
  its own record-directory checks and RT-O9-L2 is NOT RUN while RT-L2 is.
- Release checks read their facts from git objects at the commit under check (`--commit`; the file
  `release/<row>.json` of the tool's audit directory in that tree names the objects each evaluator checks). This
  replaces L2. RT-T's kinds of "sec. 8.2" are taken as `hp`, `context-adjudication` and `hit-classification`, a
  reading the expectation file does not state.
- The gate reads a stop's outcome from the result's `outcome` (a stop is `{class, message, detail}` and names
  none), cross-checked with the exit file; `failed_conditions_include` is read from the result's side changes.
- The pinned workflow carries a dispatch-only `suite` job (input `job: control-suite`), with its own guard, the
  runner steps, the gate as its own step and the marker step "control expectations hold". It has not been
  dispatched.

Findings for the owner (none resolved by exception):

- F1. Z9-STAGED and Z9g: the directory condition ids are string literals in `engine/reconcile.py`, linted against the
  A1 profile `register-caps` (the plan checker's `CAPS`, three or more capitals not followed by a letter). The ids
  are Dir2 to Dir5 (design amendment 2, MIGRATION.json), which that profile does not match; no allowlist entry names
  them.
- F2. RT-O9 FAILs at `origin/main`: its predicate requires no `side-change-unclassified`, and `main` carries over a
  hundred paths changed after `H` that no class covers (other audits, the r6 design directory, generated `.tex`
  files), besides the tool files whose pins this stage refreshes.
- F3. Many WB, N and engine rows state whole-result expectations (outcome, `classes_exact`) where the runner's
  predicate reads one line or one subject; on the real tree the result carries other items (for example WB2:
  `rule-stale` and `unclassified` beside `rule-negative-match`). The gate reports `declarative-mismatch`.

Remaining: restored cases for the other rows (a1_controls beyond the rule rows, the ledgered engine controls, the
conformance rows with named positive cases, S11); runners for the other 12 B1 rows and the rows without a runner;
named cases and bindings for multi-case rows; evaluators for attested invariants (L1); the mutation harness and its
step (OBL-24); the A1 controls run without `--main`, Y8 and REPRO-DOUBLE in the suite job.

## 15. Second stage: expectations checked as stated (WIP / UNVERIFIED)

Owner rulings of 2026-11-26T05:53:39Z (#1169 comment 7183914927): F1 is resolved by compliant replacement
identifiers under a separately reviewed mapping (design amendment 2: Dir2 to Dir5, approved under AGENTS.md sec. A.48
at #1169 comment 7184425769); F2 by complete B4 side-change classification records, built separately; RT-T's record kinds are `hp`,
`context-adjudication` and `hit-classification`; the suite-job dispatch waits for a complete candidate.

Done in this stage:

- The gate reads from the result what it can: item patterns (`<field>_include`, `profile` against `profiles`),
  delegated-class sites, `<file>:<line>` site subjects, site fields from the site's items, flat `finding_counts`
  keys, list counts, the USAGE stderr object, the purity lint's findings, `none`, `{all, have}` over literal
  fields, `{condition, holds}`, `composed_blob`, `a5_unequal_paths`, `rule_active`, all-sites conditions and
  `out_dir_created` (from the manifest). Every other invariant stays attested (L1).
- Tool: every result site carries `state` (unresolved, provenance-adjudicated or its last segment status), counted
  in `site_counts`; an HP adjudication entry naming no tracked site is FAIL `stale-adjudication` (R6.REC.10); a
  merge whose subject names another pull request is ERROR `CONFIG_INVALID` (R6.HP.1).
- Runners: restored cases for the U, B, K, M and TT engine controls, R15, R18-engine and R19-engine, the synthetic X
  rows and M10; stopped stages retained with their stop; named cases and bindings for I2-4, Y4, Y6, X9, Z7, Z10,
  B3 and the U, B and K rows; new runners RECLINT-ORPHAN (the HP orphan and positive cases only) and
  PIPE-UNRESOLVED.

Rows whose expectation conflicts with the design or the real tree, listed for the owner with both left unchanged:
M1 and M2 (classes_exact `[unauthorized-edit]`, while R6.ANCH.9 adds `unauthorized-change` for the file's changed
sites); B5 (`ambiguous` beside `duplicated`); H5 (`untracked-hp-overlap` with obligation HP, which the tool and
RT-T0 count under RET); U14's second case (R6.HP.7 expects `stale-adjudication` for an entry that names an existing
site, R6.REC.10 decides such an entry by the site's own rule); Y4 (`unclassified` follows from the rejected allow
rule); R18 (RC11 fails with the class, so AGENTS.md is `base-drift` and the run FAILs); S11-1 (delegated-evidence
items in harness admission); S11-2a (deny-match on the mutant of E, as the runner notes); S11-5 and S11-6 (items
carry `rule_id`, not `profile`); and the whole-result expectations on the real tree (WB1, WB2, WB6 to WB8, WB11 to
WB13, WB15, V7a, V7c, V15, V21, V23, V24, V27, V27-glossary, L2, RT-D, RT-D-gr58, item11-T1p), where the result
carries items of lines the row does not touch.
