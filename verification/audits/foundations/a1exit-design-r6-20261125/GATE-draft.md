# r6 section 16 (GATE): draft for review, not adopted

## 16. Verification architecture: expectation file, runner evidence, independent gate, correspondence check

### 16.1 Authority

The expected result of every control is stated once, in the expectation file of schema `oi-control-expectations/1`. r6's prose states requirements and names the controls that test each one. It carries no expected-result table (OD-2).

`controls.json` keeps only what the engine reads: each row's `operations` and `direction`, and the file's `control_inputs`. Its `expect`, `reference`, `case` and `by` fields are withdrawn.

A runner's predicate is a diagnostic of the runner. The verdict on a control is the gate's (sec. 16.5). A reference figure never decides a verdict (OD-1).

### 16.2 Expectation file schema `oi-control-expectations/1`

The file is one JSON object with:
- `schema`;
- `record_id`;
- `rows` (array);
- `retired` (array).

Unknown fields are refused. Each row has the following fields.

| Field | Meaning |
|---|---|
| `id` | Control id, unique in the file; never reused (sec. 34). |
| `migrated_from` | The pre-r6 id, when renamed under OD-31. |
| `requirements` | The r6 requirement ids the control tests (at least one). |
| `runner` | `file:line` of the runner predicate. The recorded id equals `id`. `null` when no runner implements the control (the gate then reports it missing). |
| `operations` | As in `controls.json`, when given there. |
| `direction` | `positive`, `adversarial` (the default) or `both`. |
| `predicate_kind` | `declarative` (the default) or `procedural`. |
| `expect` | The full declared expectation (below), or `null` while the owner has not settled it. A `null` row cannot hold. |
| `restored` | The expectation for the restored tree, where the source states one. |
| `procedure` | Procedural rows only: `{name, lib, evidence, note}`. `lib` names an entry of the procedure library (16.4). `evidence` defaults to the library's evidence contract. |
| `composed_of` | For a design id split into recorded halves. The row holds only if every component holds. |
| `depends_on` | Ids whose status must be PASS before this row can be PASS. Otherwise the row may only be NOT RUN with the dependency's release condition. |
| `status_allowed` | Default `["PASS"]`. `NOT RUN` is admitted only together with `not_run`. |
| `not_run` | `{reason, release_condition, release_check}`. `release_check` is a predicate the gate evaluates on the commit under check (16.9). |
| `reference` | Informational figures, never compared for the verdict (16.5). |
| `source` | Governing design cite: `D:` is v6.0e, `r5:`, `v1:` or `v2:`, with the approved translation named (OD-17, OD-19, OD-21, OD-22, MC-n). |
| `flags` | Informational notes for reviewers. |

The `expect` object has these fields:

- **`outcome`.**
  - Tool outcomes: PASS, REVIEW_REQUIRED, FAIL, USAGE, ERROR, VOID, INTERNAL.
  - For subjects that are not a tool run: NO_ITEM, ITEM, ANY, NON_ACCEPTANCE, ACCEPTED, PRE_RUN_PASSED, PRE_RUN_FAILED, LINT_PASS, LINT_FAIL, RC_HOLDS, RC_FAILS, RESULT_EQUAL_CLEAN, RESULT_EQUAL_FULL_STORE, RESULT_EQUAL_WITHOUT_AMENDMENT, REPLAY_EQUAL, LANDING_VERIFIED, LANDING_REFUSED, RESOLVED, TEXT_EQUAL, HASH_EQUAL, PREDICATE, ORACLE, COUNTERCONTROL, REFUSED, NOT_REFUSED, COMPOSITE.
- **`exit`.** It defaults to the outcome's code in sec. 7: 0, 10, 20, 64, 65, 70 or 71. The gate always compares the actual exit against the stated or implied code.
- **`stop_class`.** The ERROR or VOID class in `result.json` `stop.class`.
- **`classes_exact`.** Either a list (the set of item classes of the whole result) or an object mapping an item filter to a list. `classes_include` is the subset form.
- **`counts`.** An object from a count key to an integer. Key grammar:
  - `finding_counts:<OBL>/<DECISION>/<class>` reads the result's `finding_counts`;
  - `site_counts:<state>`;
  - `<unit>[k=v,...]` with unit `items`, `lines`, `sentences`, `hits` or `findings`, counted over the result. Filter keys are item fields (`obligation`, `class`, `decision`, `rule_id`, `profile`, `file`, `subject`, `segment`, `state`, `path`, `literal`, `only_profile`). `|` separates alternatives.
- **`sites`.** A list of `{subject, ...fields}` that must hold for the named site or subject.
- **`invariants`.** A list of single-key objects from a closed vocabulary listed in the annex to this section. Examples: `all`/`have`, `none`, `items_include`, `failed_conditions_include`, `per_site`, `drift_state_in`, `marker_written`. An unknown key makes the file invalid.
- **`cases`.** A list of case expectations, each with `case`. A list of names means each named case separately, with the same expectation.

`$name` values are bindings that the runner's evidence manifest supplies. The gate checks each binding against the retained mutation diff: a bound subject must be a path or site the mutant changed. An unbound `$name` is `raw-evidence-missing`.

The `retired` array entries are `{old_id, disposition, underlying}`. `underlying` is one of:
- `preserved-at <ids>`;
- `obsolete: <reason>`;
- `withdrawal-needs-decision` (Q4).

### 16.3 Runner evidence contract

Every runner writes two kinds of output.

**1. A structured record per control**, in the file `control-records.json` (schema `oi-control-records/1`): `{id, status, actual, predicate, evidence}`.
- `status` is one of PASS, FAIL, SKIP, NOT RUN.
- `actual` holds every quantity the runner asserted.
- `evidence` names the control's evidence directory.

**2. The raw evidence per control**, under `evidence/<job>/<id>/`, with a `manifest.json` (schema `oi-control-evidence/1`). For each case the manifest gives:
- the argv;
- the exit status file;
- `result.json` (or `control-result.json`, or the USAGE stderr JSON);
- the listing of `--out`;
- the input mutation (paths with blob ids before and after);
- the bindings;
- the sha256 of every file.

Where a runner keeps only a summary today, r6 requires the raw evidence named in the procedure library (16.4) to be retained:
- for sweeps, per-site item tuples, not whole results;
- for two-run comparisons, both results;
- for the purity lint, the lint report, the linted source map and the value set;
- for host-process properties, the step exit file, the marker-path listing taken after the step, the entry-point sentinel and the import trace;
- for an external oracle, P's outputs as files.

The evidence set is a CI artifact. Its manifest digest is recorded with the run. Retention on `main` follows sec. A.42 when an enduring claim relies on it.

### 16.4 Independent extraction

The gate derives `actual` itself and does not trust the runner's `actual` or `status`. It imports nothing from `tools/ledger_coverage/`.

- **Declarative, one tool run per case.** The gate reads:
  - the exit file;
  - `result.json` (`outcome`, `stop.class`, `items[]` with `obligation`, `class`, `decision`, `subject`, `rule_id`, `alternatives`, `segment` and `fingerprint`, `sites[]`, `finding_counts`, `site_counts`, `hit_counts`).

  It evaluates every `expect` field. It cross-checks `outcome` against the exit file, and it recomputes the outcome from `preflight`, `record_checks` and `items` with its own sec. 7 precedence rule.
- **Procedural, gate-evaluated.** The gate computes the predicate from retained raw evidence:
  - `rel-equal`: equality of the item tuples `(obligation, class, segment, fingerprint)` between the named runs;
  - `sweep`: per site, the set difference against the unmutated tuples;
  - `set`: an expected set computed from a retained tree listing;
  - `replay`: byte equality except `config.admission.mode`;
  - `hash`: equality of `engine.blob_sha256` across two results;
  - `ast`: the gate's own parser or regex applied to retained inputs (a widened rule against its negative examples, the workflow arm text, the clean-path predicate);
  - `rtl2`: the three-valued RT-L2 predicate (16.9).
- **Procedural, attested with checked evidence.** Where re-execution is impractical, the gate verifies the retained evidence named by the library:
  - `prerun`: step exit file, marker listing, sentinel, import trace;
  - `consumer`: the acceptance clauses that decide the case, re-read from the retained result, landing record and snapshot (admission mode, `harness` field, F, pin table, evaluated commits, recorded `T`);
  - `lint`: the findings list and a non-empty linted source map;
  - `oracle`: the tool result against P's retained output;
  - `fixture`: the per-case ls-remote fixture and the landing-check exit.

  In each case the runner's value must equal the value the gate reads.

### 16.5 Verdict rules

The gate fails (exit 20) on each of the following findings:

- `missing-id`: a row id, or a `composed_of` component, has no record;
- `unexpected-id`: a record id is not in the file;
- `duplicate-id`: two records carry one id, within a job or across jobs;
- `status-not-allowed`: the status is not in `status_allowed`, or is NOT RUN while its `release_check` holds;
- `declarative-mismatch`: an `expect` field differs from the gate-extracted actual;
- `procedural-failed`: the named procedure does not hold on the retained evidence;
- `raw-evidence-missing`: the manifest is absent, a named file is absent or does not match its sha256, or a binding is unbound or does not match the mutation;
- `status-actual-inconsistent`: the runner's status disagrees with the gate's verdict in either direction;
- `correspondence-orphan-row` and `correspondence-orphan-requirement` (16.6);
- `expect-null`: a row whose `expect` is null.

An invalid expectation file, record file or manifest schema is a gate ERROR (exit 65).

A difference between an extracted figure and `reference` is reported as `reference-difference` and does not change the verdict. Under sec. 31 it blocks acceptance of the implementation step until it is explained.

The gate writes `gate-result.json` (schema `oi-control-gate/1`): one entry per row with the gate status, the extracted actual and its findings.

### 16.6 Correspondence check

The gate checks the correspondence between r6 and the file in both directions:
- every row's `requirements` exist in r6's requirement list;
- every r6 requirement names at least one control id;
- every named id is a row or a `retired` entry;
- every row is named by some requirement.

The requirement list is the machine form of r6's requirement ids and their control lists, generated from r6 and checked for drift. A row or requirement without a counterpart fails the check. A retired id named as a live control also fails it.

### 16.7 The gate's own controls

These are GATE-1 to GATE-20. Their expected verdicts are in the file; they are summarized here.

| Id | Case | Expected verdict |
|---|---|---|
| GATE-1 | false actual value | `declarative-mismatch` |
| GATE-2 | missing result | `missing-id` |
| GATE-3 | duplicate id | `duplicate-id` |
| GATE-4 | unexpected id | `unexpected-id` |
| GATE-5 | unauthorized NOT RUN | `status-not-allowed` |
| GATE-6 | weak runner predicate passing a wrong result | `declarative-mismatch` |
| GATE-7 | row with no requirement | `correspondence-orphan-row` |
| GATE-8 | requirement with no control | `correspondence-orphan-requirement` |
| GATE-9 | raw evidence missing or hash mismatch | `raw-evidence-missing` |
| GATE-10 | sweep evidence contradicts a runner PASS | `procedural-failed` |
| GATE-11 | NOT RUN after release | `status-not-allowed` |
| GATE-12 | composite component missing | `missing-id` |
| GATE-13 | RT-L2 run on a drafted record | `procedural-failed` |
| GATE-14 | RT-L2 record bound to another M | `procedural-failed` |
| GATE-15 | RT-L2 partial coverage | `procedural-failed` |
| GATE-16 | reference difference only | holds, with `reference-difference` reported |
| GATE-17 | malformed file | ERROR 65 |
| GATE-18 | complete correct fixture (positive) | holds |
| GATE-19 | RT-L2 validly reconciled (positive) | holds |
| GATE-20 | runner FAIL while the actual meets expect | `status-actual-inconsistent` |

The gate self-test runs these before the gate evaluates the real records. A self-test failure is VOID (70).

### 16.8 CI under sec. A.44

The gate is its own job step, after the runner steps, in the pinned workflow. It reads only structured data:
- the runner steps' exit files;
- `control-records.json`;
- the evidence manifests and files in the run's own artifact directory;
- the expectation file and the requirement list at the commit under check.

It never parses log text. The step's exit status is the verdict. A marker step named for the fact it records ("control expectations hold") carries the step conclusion. Runner steps may exit nonzero by design (a control that ends in NOT RUN, or a negative-path step); the gate reads their structured records, not their badge. The gate's output and the evidence digest are uploaded as artifacts and recorded as provenance (sec. A.42 item 2).

### 16.9 NOT RUN rule and RT-L2

`NOT RUN` is allowed only where the row lists it, with a reason and a release condition, and only while the row's `release_check` is false on the commit under check. Today that is RT-T, TR5, G-A1, RT-L2, and RT-O9 through its dependency.

RT-L2 is three-valued:

| Result | Condition | Verdict |
|---|---|---|
| no drift | no `base-drift` at the predicted `M` | PASS |
| validly reconciled | every drifted path is covered by a reviewed reconciliation record whose review passes record lint and which is bound to the exact `H`, `M` and `C` blobs of the run | PASS |
| unresolved | anything else, including a drafted or unreviewed record | FAIL |

RT-L2 is NOT RUN until a reviewed record exists. The RT-L2 PASS recorded by CI run 45569710442, made on a drafted record, does not establish the safeguard (sec. 31).
