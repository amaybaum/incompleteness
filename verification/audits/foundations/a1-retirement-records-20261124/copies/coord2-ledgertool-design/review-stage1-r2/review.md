# Independent review: Stage 1 correction (r2) of the ledger coverage tool, commit 75dae645

Reviewer: independent (not the writer). Read-only on the subject. Everything I ran was in my own detached worktree,
`review-stage1-r2/wt`, at 75dae6456195fef3d8fb12190b69844e0d297929. My scripts are in `review-stage1-r2/scripts/` and
their outputs are in `review-stage1-r2/out/`.

## 0. Inputs verified

- `DESIGN-v5.5.3.md` sha256 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379: matches.
- Writer evidence `impl-stage1-r2/MANIFEST.sha256` sha256 ec6c31e0...ae27: matches, and `sha256sum -c` passes.
- Subject: the worktree `coord2-impl-wt` HEAD is 75dae645 and clean. The base 4fb2c1ee is an ancestor, and the 14
  commits after it contain no merges.
- I reviewed against the whole of v5.5.3. The handback states conformance "to v5.5.2, and to v5.5.3 for K7". Since
  v5.5.3 changes only K7, those are the same thing.

## 1. Reproduction (handback section F), run by me

| Step | My outcome | Writer's | Same? |
|---|---|---|---|
| 1 self-test | 87/87 controls passed, exit 0 | 87 | yes |
| 2 purity-lint (A1 config) | PASS, 0 findings | PASS | yes |
| 3 synthetic fixture | 36/36 true; stdout byte-identical to the writer's (after the first line, which holds the injected-fault X7 record) | same | yes |
| 4 conformance controls | 65 PASS, 2 NOT RUN (TR5, G-A1) | same | yes |
| 5 A1 conformance | 46 PASS, 1 FAIL (WB12, `deny-match`) | same | yes |
| 6 A1 controls (20m35s) | 84 PASS, 4 passed without a status field (RT-DR, RT-I7, RT-I7A, V3-countercontrol), RT-L2 FAIL, RT-T NOT RUN | identical, control by control (status and passed) | yes |
| 7 release gate (branch) | 5 FAIL: lean-axioms, legacy-records, v3-corpus, v3-receipts, citation-roles (shallow repository or toolchain); every other step PASS | same step results | yes |

Totals: 322 PASS, 2 FAIL, 3 NOT RUN, the same as the writer's. I did not re-run the gate on main 8e9b8334. The five
failures are environmental (`undecidable:shallow-repository`, no Lean toolchain).

Step 3 note: `synthetic_fixture.py O/syn` crashes when `O/syn` does not exist (`mkdtemp` with a missing dir). The
recipe needs `mkdir -p` first. Non-blocking.

Status of each control:

- **Tested by me** on real git objects or real clones:
  - every control in steps 1-6;
  - my own counterexamples in sections 3-5.
- **Simulated only.** These run on the in-memory host and are not GitHub:
  - TR1-TR53;
  - X11, TR30, TR45/46;
  - my D5, consumer, TR49b and class-record cases.
- **NOT RUN** (they need GitHub, CI or reviewed records):
  - TR5;
  - G-A1;
  - RT-T;
  - TR45 for op C.

## 2. The first review's six blocking defects

| Defect | Status | Evidence |
|---|---|---|
| B1 harness accepted | **Fixed** | `engine/checker.py:33-57`: `accept()` rejects any `harness` key and any mode other than `chain`. `cli.py:330-336` writes `control-result.json` for harness and simulated-host runs. X11 is PASS (re-run). |
| B2 native delegation | **Fixed** (simulated and on small on-disk repos) | `engine/delegation.py:137-160`: `git clone --no-local`, no alternates, commit and tree checked. Checkers come from F's blobs. Runs happen at X and at C. G4-G9 are PASS (re-run). With no F, the result is `delegated-evidence-missing` (seen in my runs). G-A1 is NOT RUN (needs CI). |
| B3 root of trust | **Fixed**, with the exceptions in sec. 3 (D5, consumer A check) | `engine/authority.py:244-445`: points 1-7, pin-table admission (`config.py:192-224`: chain mode reads only pin-table blobs) and the owner field. |
| B4 commits after X; widening chain | **Fixed** | `execution.py` `commits_after`. R16 and R17 are PASS. `records.py:175-205` checks the widening review names both blobs, gives a verdict per changed item, is by a non-author non-regular reviewer and has an owner authorization. A12r is PASS. |
| B5 purity and guard pins | **Fixed** | Guard-pin semantics now sit in the adapter (`a1exit_exact_edit.py:148,214`). The engine reads only `led['guard_pins']` (`execution.py:286`). The value set covers the JSON companions. Z9g and Z9h are PASS. D2 is assessed in sec. 5. |
| B6 control reporting | **Mostly fixed** | Status values, RT-T NOT RUN, the full RT-D predicate, and A1r-A11r through the pipeline are all present. Remaining items are listed in sec. 6: four records without `status`/`predicate`, the RT-T0 count, WB12 and TR49. |

## 3. Findings

### F1. BLOCKING: a former owner can authorize freeze-ledger changes after a verified owner change (D5)

- **Design requirement.**
  - Sec. 6.3, "The freeze ledger": each append comment must "be authored by numeric owner id `A.owner.id`".
  - Ledger changes otherwise "land through the authority-change procedure", whose approver is the owner of the `A`
    in force.
  - No transition rule lets the id of a superseded `A` keep authority.
- **Code.** `authority.py:337` sets `governing['_owner_ids']` to the owner ids of **every** verified version of
  `A`. `verify_history` then accepts a ledger approval from any of them (`authority.py:207-226`). Nothing checks
  which `A` was in force when the approval was made or when the ledger change merged.
- **Counterexample** (`scripts/d5.py`, `out/d5.txt`, simulated host):
  1. `A` v1 has owner 4242.
  2. A verified change to v2 (owner 5555) is approved by both ids and merged.
  3. After that merge, a ledger change is approved **only by 4242**, through either form (`oi-freeze-ledger/1
     append` in the plan thread, or `oi-authority/1 approve` in the authority thread).
  4. Result: **ACCEPTED**. The same change approved by 31337 is refused.
- **Fix.** For each ledger version, the approver must be the `owner.id` of the `A` version in force at that
  ledger change's merge: the latest verified `A` version merged before it. The approval must also be created
  before that merge.
  - An approval by the then-current owner of a ledger change merged before the owner change stays valid.
  - Any approval of a ledger change merged after the change must come from the new id.

  Add a control for both directions.

### F2. BLOCKING: side-change class records referenced by the configuration are never chain-linted in op C

- **Design requirement.** Sec. 6.3 applies the writer, reviewer and authorization chain to "side-change class
  records". Sec. 13.1 requires "a reviewed side-change class record".
- **Code.** `cli.py:1014-1020` loads every `records` entry of kind `side-change-classes` straight into the class
  set, with no `lint_chain`.
  - Only reconciliation records (`cli.py:1021-1030`) and records given on the command line (`RecordSet.admit`)
    are linted.
  - `config.load` lints the configuration's own chain only (`config.py:235-238`).
- **Counterexample** (`scripts/classrec.py`, `out/classrec.txt`). Synthetic configuration, simulated chain
  admission with record lint active, op C with `--main` = H plus `notes/side.txt`:

  | Class record | Result |
  |---|---|
  | none | `side-change-unclassified` |
  | reviewed and authorized | classified, no item |
  | with **no review and no authorization** | classified, no item, no `record-invalid` |

- **Fix.** Lint every class record the configuration references, as `RecordSet.admit` does: `record-invalid` and
  no classification on failure. Add the missing case to S4a/R18. The same gap applies to the delegation contract
  if it is meant to be a reviewed record (owner condition 2 says "frozen, reviewed"). Sec. 6.3's list of kinds
  does not name it, so I report it only as NON-BLOCKING.

### F3. BLOCKING (small): the consumer predicate does not check that `head_sha` contains `A`

- **Design requirement.** Sec. 5: "`head_sha` is on `main`'s first-parent chain and contains `A`". The consumer
  repeats trust-root points 1-3 itself.
- **Code.** `checker.py:60-104` (`accept_with_host`) never reads `tools/ledger_coverage/authority.json` at
  `head_sha`. Its K7 loop only rejects extra or changed entries, so if the record is absent it raises nothing.
- **Counterexample** (`scripts/consumer_noA.py`, `out/consumer_noA.txt`): the run's head is a main commit without
  the authority record, and the snapshot is consistent. `accept_with_host` returns **True**.
  - **Impact.** Limited. The pinned tool refuses this case itself (`authority.py:285-286`), so exploiting it would
    need an unpinned producer. Even so, the consumer side of the stated predicate is incomplete.
- **Fix.** Require the file at `head_sha` to be present, regular and equal to `pins['authority_blob_sha256']`.

### F4. BLOCKING: the RT-L2 failure comes from the landing composition, not from the design (K1)

- **What fails.** RT-L2 (sec. 13.4, a precondition for landing) fails because the draft configuration
  `a1exit-retirement-config.json` lands with the tool. It pins the class record, so the tool-landing class cannot
  pin it.
- **Not a design contradiction.** Sec. 16.2 places the configuration "in the retirement plan's record directory,
  frozen with the plan at `F`". It is not a tool-landing path.
- **Demonstrated** (`scripts/rtl2_placement.py`, `out/rtl2.txt`, A1 objects, harness). Rebuilding the predicted
  main with every tool-landing file **except** the configuration, which is still read from the reviewed commit
  standing in for `F`:
  - RT-L2 gives no `base-drift` and no `side-change-unclassified`: **PASS**;
  - with the configuration landed, as the writer had it: FAIL.
- **Fix.** Do not land the configuration, or any record that must name the class record's blob (its review and
  authorization), in the tool's landing. They belong with `F` (sec. 6.3: "or in the amended plan's record
  directory for records frozen with the plan"). Then re-run RT-L2.

  The test harness can keep reading a draft configuration from a commit that is not part of the landing.

### F5. BLOCKING (control): RT-T0 does not test "215 region lines"

- **Design requirement.** Sec. 10.4: "A control's predicate must test its whole stated expectation: every …
  count it names". Sec. 0.3: a reference count that is not reproduced "blocks acceptance of the implementation
  step until it is explained".
- **What is missing.** RT-T0 names 215 region lines. The writer's predicate leaves it out (D8;
  `a1_controls.py:227`), and op B does not output the count, so no one has checked the figure at this commit.
- **Fix.** Have op B emit the region-line count under the D4 span and assert 215.

### F6. NON-BLOCKING (control defect; the tool is correct): WB12 (writer's D1)

- **The writer's claim** is that WB12's expectation conflicts with the deny-before-negative order of sec. 6.2.
  That is not so.
- **The order.** Deny-first precedence is required. Sec. 6.2 says "the steps run in this order", with step 2 "If
  any deny profile matches the sentence, the result is FAIL `deny-match`" before step 3.
- **What WB12 is.** WB12 is defined as "**V7a** on the W1-c sentence". V7a (sec. 10.2) is "V2 **with DR-3 removed
  from the profile set**", and is expected to give `rule-negative-match`.
- **The control error.** The writer's WB12 (`a1_conformance.py:168-171`) runs `--check item7`, which keeps DR-3.
  The same writer's V7a (`a1_controls.py:518`) correctly drops DR-3 and passes.
- **My re-run of WB12 as defined** (`scripts/wb12.py`, `out/wb12.txt`):

  | Profile set | Result on the line |
  |---|---|
  | item7, DR-3 present | `deny-match` (DR-3) |
  | item7 less DR-3 | `rule-negative-match` (W1-c), as expected: **PASS** |
  | no deny profile at all | `rule-negative-match` |

- **Smallest correction.** Change the control, not the expectation: run WB12 with
  `--profile ptr,count-grep,resid,DR-1,DR-4,DR-5`. The design needs no change.
- **If the owner adopts the writer's correction instead** (expect `deny-match` with DR-3 present):
  - Acceptance is not weakened. The tool's code is unchanged, both outcomes are FAIL with exit 20, and deny-first
    precedence means no input moves from FAIL to PASS or REVIEW.
  - It does lose WB12's coverage of step 3 for an over-allowance edit of the W1-c sentence.

### F7. K1 and the writer's proposed sentence

- **Is the cycle genuine?** It is not a contradiction of the frozen design (F4). A placement consistent with
  sec. 16.2 and 6.3 exists, and RT-L2 passes under it.
- **Does the sentence break every cycle?** No. It breaks:
  - configuration ↔ class record (via the pin table);
  - class record ↔ its review and authorization (via the configuration's references).

  It does **not** break configuration → class record → configuration review (or authorization) → configuration
  when those two records land with the tool:
  - the configuration's review and authorization are listed in `F`'s pin table, not referenced by the
    configuration, because they name its blob;
  - the sentence classifies only "the configuration itself" by the pin table.

  So the class record must pin the review `RC`, and `RC.reviewed.blob_sha256 = sha256(C)`, where `C` pins the
  class record. No such fixed point exists.
- **Is it too wide?** It classifies any `M` path whose blob equals a configuration reference, with no exclusion
  for ledgered or corpus paths. That cuts across the rule that such side changes are `base-drift` unless
  reconciled (sec. 13.1, 13.3).
- **Self-authentication.** The sentence does not let the configuration authenticate itself: its own path is tied
  to `F`'s pin table. Every path stays bound to one exact blob.
- **Recommendation.** Make no design change, and fix the placement (F4). If the owner still wants landed drafts
  covered, the smallest sentence that passes all three tests is:

  > "A side-changed path on `M` under the tool-landing prefixes that is neither ledgered nor in the corpus is also
  > classified when its sha256 equals the sha256 that `F`'s pin table lists for that path, or a
  > `{path, blob_sha256}` that the configuration admitted from that table references in `roles` or `records`; a
  > class record pins every other landed path."

  This sentence covers the configuration, its review and its authorization through the pin table, and the class
  record's review and authorization through the admitted configuration. Admission still rests on the
  designation, the pin table and `A`.

## 4. The six design points

**Trust root and acceptance.**
- Local runs: without the GitHub environment, admission refuses (`cli.py:376-379`).
- Harness and simulated-host results are never `result.json`, and `accept()` rejects them (X11 re-run).
- K7 (`authority.py:288-302`): pins plus exactly two permitted regular files, plus an equality check of the record
  at `head_sha`.
  - TR48-TR53 pass.
  - The writer's TR49 refuses on `main`'s history before K7 (D8). My variant `scripts/tr49b.py`, where `head_sha`
    holds an earlier approved `A`, reaches K7 and gives ERROR, "the authority record at the run's commit differs".
    The control is weak, but the code is right.
- **NON-BLOCKING.** `RestHost.detect` takes the API base from `GITHUB_API_URL` in the environment
  (`host.py:145-149`). A local caller who sets `GITHUB_ACTIONS`, `GITHUB_RUN_ID`, `GITHUB_TOKEN` and that URL can
  point the tool at a fake host and get `"chain"` written locally. This sits poorly with point 9 and with "no
  environment value can set" the authority. Acceptance is unaffected: the consumer re-reads its own host, and the
  artifact sha256 must match the run's upload. Pin the API base, or take it from `A`. (Not executed; code reading
  only.)

**Ownership chain** (`records.py:101-172`).
- Checked: author ≠ reviewer, per-item verdicts all `accept`, an authorization listing both blobs with the owner
  id, a comment id and a time, a path without a hash flagged, and `supersedes` checked for every kind with loop
  detection.
- Lineage is checked only for configurations (by `config_id`). For other kinds only the schema is compared.
  NON-BLOCKING.
- Exception: F2 (class records are not linted).

**Reconciliation R1-R13 and S6.**
- `reconcile.py` checks R13 first and evaluates every condition from objects.
- The composition is computed regardless of the record.
- N10 (the landing blob 9f4fc3e8 against the composition 86d79863) gives `landing-conflict-unresolved` plus
  `record-invalid`, and N11 is PASS (re-run).
- N6 shifts the recorded range rather than the landing bytes, and N12 also trips R13. Both still name the target
  condition. NON-BLOCKING.

**P parity** (`a1exit_exact_edit.py:38-145`).
- Selection uses `str.count == 1` in pair order.
- The running copy is kept as segments.
- A chained edit (an occurrence crossing an image, including an empty one) is refused.
- Byte offsets are mapped back to `H`.
- Retained edits must have no splice, and an orphan splice is refused.
- S11-56, S11-57a-d and S11-58a-k are PASS (re-run). I found no counterexample.

**W1 option B** (`rules.py:60-95`, `pipeline.py:690-700`).
- The allowance needs file, sentence sha and context sha to match.
- There is one grant, at the smallest index.
- Negative literals are case-insensitive.
- WB1-WB11 and WB13-WB15 are PASS (re-run). On WB12 see F6.

**Purity and generality.**
- Z9 passes on the real engine.
- The synthetic second configuration's Y/Z/X controls pass (re-run).
- My counterexample F2 runs on the synthetic configuration through the general engine.

## 5. The writer's deviations

- **D5: BLOCKING** (F1, demonstrated). A former owner keeps authority to approve new ledger changes. An approval
  by the then-current owner for a change merged before the owner change should stay valid, and the fix in F1
  keeps it valid.
- **D2: acceptable, NON-BLOCKING.**
  - The design's explicit list of companions consists of JSON records ("in any record its adapters read").
  - P's `edits_check.py` shares 50 string literals with the engine (`scripts/d2.py`, `out/d2.txt`).
  - The 20 that are not allowlisted are generic: `'utf-8'`, `'git'`, `'ls-tree'`, `'--commit'`, `'%s:%s'`, and so
    on. None of them is retirement semantics.
  - Including the checker would force allowlist entries outside the categories the design permits. No hidden
    defect.
- **D7: acceptable, NON-BLOCKING.** `F`'s blob is written at its own path inside the disposable clone, which lies
  under `--out`. That keeps the rule "run from `F`'s blobs, under `--out`, never from the clone's copy". The
  clone's commit and tree are checked before the write.
- **D8:**
  - The RT-T0 count is BLOCKING (F5).
  - N6, N12 and TR49 are weaker predicates. I verified the tool's behaviour directly for TR49 and through the
    naming checks for N6 and N12. NON-BLOCKING, but correct the controls.
  - "Unchanged Stage 1 controls use the runner's code as their predicate" stays a sec. 10.4 weakness.
    NON-BLOCKING.
- **D1:** see F6.
- **D3:** the authority-path allowlist category is not among sec. 16.1's three categories. It is a needed generic
  constant (sec. 6.3 fixes the path). NON-BLOCKING; the design text could add it.
- **D4, D6, D9, D10:** NON-BLOCKING.

## 6. Other NON-BLOCKING points

- In the A1 report, RT-DR, RT-I7, RT-I7A and V3-countercontrol have no `status` or `predicate` field. Sec. 10.4
  requires both.
- The handback says "Against main base 4fb2c1ee: 59 new files, +16755/−27". The actual figure is 58 added files,
  +16750/−0. The handback's figure is the diff against 8e9b8334.
- `records.item_ids` falls back to `['*']` for an unrecognized record shape. A review can then cover a whole
  record with one verdict.
- `synthetic_fixture.py` needs its output directory to exist already.

## 7. Scope

- `git diff --name-status 4fb2c1ee 75dae645` gives 58 entries, all `A`, all under `tools/ledger_coverage*` or
  `verification/audits/foundations/ledger-coverage-tool-20261123/`. No pre-existing file is modified.
- `authority.json` engine pins: 43 pins, which equal the 44 tool files minus `authority.json`.
- The workflow draft hash equals `A.workflow.content_sha256`.

## 8. Verdict

**REJECT.** There are blocking implementation defects:

- F1: D5, former-owner ledger approvals;
- F2: unlinted class records;
- F3: the consumer's "contains A" check;
- F4: the landing composition that causes RT-L2 to fail;
- F5: the RT-T0 count.

There is **no DESIGN-ISSUE**:

- K1 is resolved by the placement the design already prescribes (sec. 16.2), and that is demonstrated.
- WB12's expectation is consistent with sec. 6.2; the control misconstructs V7a.

All five fixes are small and local.

Counts: 5 BLOCKING, 0 DESIGN-ISSUE, NON-BLOCKING as listed in sections 3 (F6), 4, 5 and 6.
