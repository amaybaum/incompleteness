# DRAFT — not adopted, not frozen, not reviewed

This file is a paper draft of the text that the amendment of the frozen plan `4c79be642ca631573f06b444903be75ec4f5e2b6`
would append to `verification/audits/foundations/a1exit-deletion-20261121/PREREG.md` as §32. It is prepared under the
owner's authorization of bounded preparation work (amaybaum, 2026-11-28, #1577 comment 7238783221) and is not the
amendment. Amending the frozen plan, designating `F`, the trials and the execution each need the owner's approval
(AGENTS.md §A.50 items 2 and 5). Every value written `PENDING-…` waits on the final `H`, the landed tool `T_land`, the
preparation base `B`, the snapshot `S` or the representative anchor `M_rep`. Bracketed notes `[NOTE: …]` are drafting
notes and are removed before review.

***

## 32. Amendment, preregistered: verification through the ledger coverage tool at the base H

**Owner decisions.** [NOTE: each quoted with author and time (§A.42 item 7). The authorization to amend the frozen plan
and the choice of H are PENDING-O-1.]

- amaybaum, 2026-11-23, #1169 comment 7093128173, as restated by owner decision A3 of 2026-11-25 (r6 R6.STAT.8): the
  tool lands first; this plan is amended and re-frozen so that every mandatory check of §11 passes as written.
- amaybaum, 2026-11-27T09:01:16Z, #1169 comment 7214186738 (DP-1): Amendment 8 adopted; "Choose H only after the tool
  lands and suspend unrelated merges affecting the paper, book or ledgered paths until retirement lands."
- amaybaum, 2026-11-27, #1169 comment 7208869709: "S-3: select and pin base H together with the plan amendment."
- amaybaum, 2026-11-24, O-13 adoption (#1169 comment 7132479512): D402–D412, bound to their hashes. [NOTE: disposition
  at H is PENDING-O-6.]
- PENDING-O-1: the owner's approval of this amendment.

**Goal link (§A.47).** A1 retirement (#1477): this section decides which exact commands verify the retirement at the
base H, which records they read and how the plan is frozen, tried and landed. It decides no scientific question
beyond the edit list it pins.

**Order.** This section is committed first; the edit-list, ledger, checker and record changes follow in later
additive commits; the Record pins of §32.11 are the last subsection of this file. No earlier section is edited: where
an earlier count, base, command or pin table differs from this section, this section governs, and the earlier text
stays as the record of `4c79be64`.

### 32.1 Base and scope

- **H** = `PENDING-H`, a commit on `main`'s first-parent chain at or after the tool's landing `T_land` =
  `PENDING-T_LAND`. From H to the landing, nothing is merged into `main` that touches `papers/`, `book/` or a ledgered
  path, except this retirement (DP-1). [NOTE: O-4 would extend this to every path except B and this plan's pull
  request.]
- **E** = the ledger pin of the frozen site map, unchanged.
- The tool is `tools/ledger_coverage.py` with the package `tools/ledger_coverage/` and the workflow
  `.github/workflows/ledger-coverage.yml`, all as landed at `T_land`, pinned by the configuration (§32.3).
- The frozen plan `4c79be64`, P\* `55544cc3`, their ledgers and the T0/T1 and T0′/T1′ evidence stay unchanged as
  historical baseline. They record what those plans tested; they are not evidence for this amendment.

### 32.2 Reconciliation at H (§9)

The procedure of §9 is run at H. Its record lists, for each edit:

- edits whose `old` occurs exactly once at H and whose bytes are unchanged: carried, with their splice re-pinned;
- edits whose `old` no longer occurs at H: redrafted from H by the rule of §9 step 3, or withdrawn where the site
  already carries the corrected statement, each with its reason and the commit on `main` that changed the site;
- every changed splice, with an explicit explanation (owner, #1169 comment 7074829849).

Drafting measurement at `main` `9be526b6` (provisional; H is later): `old` absent for D184, D185, D255, D256, D366,
D369, D375, D376, D385 and D386, and for D402 and D404–D409; corpus-changing first-parent merges since `53c6601a`:
#1560, #1580, #1582, #1589, #1591, #1606, #1607. [NOTE: D402 and D404–D409 are sites rewritten by #1589 and #1591;
PENDING-O-6.]

### 32.3 The configuration

`retirement-config.json` in this directory, schema `oi-retirement-config/1`, `config_id` `a1exit-retirement-config`,
version 1, `supersedes` null. It carries:

- `roles.scientific_base` = H; `roles.pin` = E; `roles.side_change_classes` = the class-root lineage tip at
  `PENDING-B`;
- `checks`: `item2` (coverage; `p0-core`, `p0-para`, `ledger-ext`; no final profile), `item7` (`ptr`, `count-grep`,
  `resid`, DR-1, DR-3, DR-4, DR-5; final `ptr`, `count-grep`) and `item11` (`repo`; final `repo`);
- `hp_obligations[0]`: segment `[E, H]`, with every first-parent merge on that segment that changes the corpus, each
  `{pr, commit, first_parent}`;
- `delegation`: the contract the workflow passes (`PENDING-O-8`), with its class adapters;
- `records`: every record and review the checks read, including `hp.json`, `context-adjudications.json`,
  `hit-classifications.json` and the rule records; no `reassessment` record, so the configuration is not
  discharge-bearing and needs no custody entry (Amendment 8, M8-1);
- `tool`: every tool file and the workflow at `T_land`; `repository_id` 1156244443.

Its ordinary review is a file of this directory listed in §32.11; it names the configuration's exact path and
SHA-256 and declares non-authorship. The configuration holds no reference to its own review.

### 32.4 The checks of §11 as tool commands

Each check runs only through the pinned workflow, dispatched on `main` with `job` `plan-check`, `freeze` = F and
`config` = `verification/audits/foundations/a1exit-deletion-20261121/retirement-config.json`. The workflow runs
`python3 -I -S -B tools/ledger_coverage.py <operation> --freeze "$F" --config "$F:$CFG" --out "$RUNNER_TEMP/out"`
followed by the arguments of the selected arm. `X` is the execution head, `C` the certified head, `M` `main` as
re-resolved before landing and `L` the landing. A check passes only when the run exits 0 and its `result.json` has
outcome PASS under chain admission naming this F; the verdict reads the structured result, never log text (§A.44).

| §11 item | `check` | Arguments after the common prefix | Read from the result |
|---|---|---|---|
| 1 | `item1-execution`; `item1-terms` | `execution --scientific-base H --candidate X --ledger F:ledger.json --edits F:edits.json`; `terms --commit X --profile ptr --classify <gr58 record>` | splice postconditions; `ptr` hits |
| 2 | `item2-record`; `item2-coverage` | `record --pin E --record F`; `coverage --commit X --check item2 --segment E..H --segment H..X=F:ledger.json --hp F:hp.json --classify <gr58 record> --classify F:context-adjudications.json --classify F:hit-classifications.json` | CK1–CK8; coverage of the item-2 profiles |
| 3 | `item3` | `execution … --delegation <contract>` | classes `tex`, `pdf`, `ci` |
| 4 | `item4` | same | class `coverage-ledger` and `ci` job `coverage_check` |
| 5 | `item5` | same | profiles `register`, `register-caps` (per edit, per step, per splice) |
| 6 | `item6` | same | profile `infinity` (splitter version 2) |
| 7 | `item7` | `terms --commit X --profile item7-literal` | literal matches |
| 8 | `item8` | `execution … --delegation <contract>` | subject `mirror` |
| 9 | `item9` | same | conformance of `verification/lean-manuscript-census.json` |
| 10 | `item10` | same | subject `lean`; class `ci` |
| 11 | `item11` | `terms --commit X --check item11 --scope <scope record> --final` | `final-unclassified` count |
| 12 | `item12` | `execution … --delegation <contract>` | subject `pin` at H and at X; class `ci` |
| 13 | `item13` | same | class `sc42` |
| 14 | `item14`; `item14-landing` | `execution --scientific-base H --main M --candidate X …`; the same with `--certified C --landing L` | candidate against H; four-tree landing |

[NOTE: the gr58 record, the scope record and the contract are read at `$F:$A/…` in the workflow at `e9d75a32`, with
`A` the tool's directory. PENDING-O-8. The "Read from the result" column names fields of the landed result schema,
PENDING-T_LAND.]

**Wording corrections.** Item 4 reads: the edits make seven entries of `verification/coverage/LEDGER.json` stale,
`MAIN:L-3`, `STRUCTURE:P-9.5`, `SUBSTRATUM:C-effective-finiteness-gauge-class-transfer`, `SUBSTRATUM:T-23`,
`SM:L-1c-canonical-projection-resummed-kernel`, `SM:P-4b-symmetric-point-custodial-scalarity-component` and
`SM:T-19`, each re-affirmed in the execution commit. Item 12 reads "the ledger base H" in place of "execution head's
parent". [NOTE: the stale set is re-checked at H.]

**Item 7.** Item 7 keeps its frozen statement. Its scope is `papers/*.md` and `book/*.md`. Active files outside that
scope that carry "the sixth structural assumption" as a reference to A6 are outside item 7. Decision rule, fixed
before any run at H: if `item7` passes at the predicted X, item 7 is checked as frozen; if it does not, the
restatement `item7-amended` (`terms --commit X --base H --ledger F:ledger.json --check item7 --final`) applies only
after its own preregistered text, an independent review of the deny set, the `resid` profile and the W1 rules, and
the owner's authorization, before any trial claims item 7. [NOTE: PENDING-O-10.]

**Item 11.** Without `--final` an unexplained line is REVIEW_REQUIRED; under `--final` it is FAIL
`final-unclassified`. Each line of the item-11 review load passes only with an exact rule.

**The plan checker.** At F the plan's own checks fail on each countercontrol mutant named in r6 §18, and the engine's
`register`, `register-caps` and `infinity` results equal the plan checker's `static_new` on the per-edit unit, by a
script on `main` before F (`PENDING-OBL1-SCRIPT`).

### 32.5 `preserve_check.py`

The checker:

1. records the candidate as the full commit id it resolves to, and in `--tree` mode the tree id of the directory;
2. records its own blob, and checks it against the plan's copy in every mode;
3. writes a result file with a failure status on an argument error or an uncaught exception;
4. fails `set_fingerprints` when a coverage id is not found;
5. carries the seven STALE entries in its docstring.

`--commit` mode: PENDING-O-11 (OBL-8 gap 6). PDFs are compared by the tool's `pdf` class; the named checks are read by
their `status` and the emptiness of their `discrepancies`.

### 32.6 The records

In this directory, each referenced by the configuration with its SHA-256 and reviewed by a non-author who declares
non-authorship:

- `hp.json`: one `oi-hp-adjudication/1` record with a site entry for every site change on E..H;
- `context-adjudications.json` and `hit-classifications.json`: each present, possibly with an empty list, and then
  with its `record_id` and a review stating why the list is empty;
- `a1-staging-allow-root.json`: W1-b, W1-c, W1-d, W2-a and W2-b re-derived from bytes at H, `record_id`
  `a1-staging-w1-w2`, `supersedes` null, with its ordinary review and a widening review by a different reviewer whose
  `replaces` is null; W1-a and any equivalent are not carried;
- the rule records DR-1 (a, b, c), DR-3, DR-4, DR-5, `resid` (a, b, c) and the converted EXPLAINED entries;
- `a1-staging-transition.json`: `base` B = `PENDING-B`, `custody` = the path and SHA-256 of
  `verification/audits/foundations/a1exit-staging-amendment-20261126/CUSTODY.json`, `class_root` and `allow_root`;
- `a1-staging-prior.json`: `freeze` null.

The class root lies at `verification/audits/foundations/ledger-coverage-tool-20261123/records/a1-staging-class-root.json`.
Both roots are on `main` at B, a commit after H on its first-parent chain, before F.

### 32.7 Pre-freeze gate

At the exact candidate head, before a freeze is requested, with the branch held at that head:

1. items 1–5 of §31.12.17 and items 6–8 of §31.12.18, with T0″ built from the candidate (item 9 is optional and, if
   used, runs under the owner's launch approval);
2. the exact-head check-run of §A.39 on the candidate, and the chain-admitted run of the pinned workflow dispatched on
   `main` with `freeze` the candidate's full id;
3. the control-suite run of the pinned workflow with `freeze` the candidate, `m` = M_rep, `rep_snapshot` = S,
   `tool_landing` = `T_land`, in which REP-BUILD, the rule-record rows, RT-T and S11-2 each pass;
4. a focused independent delta review of the candidate.

Results are recorded outside this directory and never committed into the plan (§31.12.17).

### 32.8 Designation of F

The owner designates F by its full id, quoting the transition descriptor's B and root digests. The reviewer of that
record compares the designated id with the `head_sha` of the check-run and the `F` of the chain-admitted run.

### 32.9 Trials T0″ and T1″

As §31.8 and §31.12.7, with H the base of §32.1 and `plan_sha` F:

- T0″ and T1″ are single-parent children of H; T0″'s tree is `guards_check.py --predict` at F; T1″ is T0″'s tree with
  the PDFs of the ledgered sources replaced by T0″'s CI-built PDFs;
- the workflow base W is a commit on `main` that has `413b0bb8` as an ancestor and whose
  `.github/workflows/a1exit-trial-verify.yml` blob equals its blob at `413b0bb8`;
- every run is checked by `preserve_check.py --verify-run`; a run that fails it is void and repeated;
- the plan branch does not move between building T0″ and the last T1″ dispatch;
- T1″'s `FULL.pdf` is verified to print the corrected statement (§31.8).

### 32.10 Execution and landing

- X has exactly one parent, H; C, where it differs from X, descends linearly from X.
- The checks of §32.4 run at X (and C).
- The plan's pull request is merged into `main` by a merge commit before the landing, so that F and `4c79be64` are
  reachable from `main`; this directory's files are then side changes on M, classified by the record-directory rule.
- L has two parents, M and C, and carries exactly the execution's own diff; `item14-landing` passes on it.
- The TeX and PDF artifacts are regenerated and verified, and the census registry is updated (§11 items 3 and 9).

### 32.11 Record pins

[NOTE: the last `### N.N Record pins` subsection of the file; every row names a direct file of this directory.]

| File | SHA-256 |
|---|---|
| `retirement-config.json` | `PENDING` |
| `<configuration review>` | `PENDING` |
| `ledger.json` | `PENDING` |
| `edits.json` | `PENDING` |
| `edits_check.py` | `PENDING` |
| `guards_check.py` | `PENDING` |
| `preserve_check.py` | `PENDING` |
| `t0_jobs_44939798305.json` | `8c5edab3c18cf9de86c33e406a30fe1a6957e8cc881e26d2bae9f7e2a7fe5bce` |
| `hp.json` | `PENDING` |
| `context-adjudications.json` | `PENDING` |
| `hit-classifications.json` | `PENDING` |
| `a1-staging-allow-root.json` | `PENDING` |
| `a1-staging-transition.json` | `PENDING` |
| `a1-staging-prior.json` | `PENDING` |
| `<rule records and reviews>` | `PENDING` |
