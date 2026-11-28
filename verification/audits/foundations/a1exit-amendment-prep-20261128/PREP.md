# A1 retirement: what the amendment of P must contain (preparation package, paper only)

Task P, retirement preparation (#1477). Local only: no push, PR, comment, CI or dispatch. Prepared 2026-11-28 under
the owner's authorization "Authorize bounded preparation and audit work, without executing retirement or any
reserved procedure" (amaybaum, #1577 comment 7238783221, recorded on #1477 at comment 7238789381). This package
amends nothing. Amending the frozen plan, designating `F`, trials and execution each still need the owner's approval
(AGENTS.md §A.50 items 2 and 5).

Inputs, by exact commit:

| Input | Commit | Notes |
|---|---|---|
| Frozen plan P | `4c79be642ca631573f06b444903be75ec4f5e2b6` (`research/a1exit-deletion-20261121`) | PREREG.md, edits.json, ledger.json, three checkers, T0 jobs fixture |
| Tool and adopted design r6 | `e9d75a323dee65ce62a67562be78f2cf6bc97f9a` (`tools/a1-ledger-coverage-r6`) | DESIGN-r6.md (amendments 1–8 folded in), AMENDMENT-8/9/10/11, staging r2 and S-1/S-2/S11-2a, the workflow, the engine |
| `main` (drafting measurement only) | `9be526b6458c53bb7801d094227ec27503121269` | final H is not chosen; every figure measured here is provisional |
| Staging drafts (unreviewed) | `fd0f2f81c`, `8f668f555` | allow-root, rule and descriptor skeletons derived at the old H |
| r5 proposal (superseded) | `27370bb3` (`records/a1-retirement-preservation-20261124`) | PROPOSAL-r4, CHANGES-r4-to-r5, diffs-r5, O13 records |

Throughout, `H` is the final scientific base (not yet chosen), `E` the ledger pin, `T_land` the tool's landing
commit on `main`, `B` the staging preparation base, `S` the representative record snapshot, `M_rep` the
representative main anchor, `F` the plan commit to be designated, `X` the candidate, `C` the certified head, `M`
the integration base re-resolved at landing and `L` the landing merge (r6 §1, §20; Amendment 11 §2).

***

## 1. Dependency chain from tool landing to retirement landing

Each step names its owner gate. "Gate" means an act that needs the owner's explicit approval each time
(AGENTS.md §A.50); a step without one runs under the existing preparation authority.

| # | Step | Owner gate | What it needs | Source |
|---|---|---|---|---|
| 1 | Tool readiness: Amendment 11 implementation, gate on the M8-3 rows, S11-2c CK5 evidence, five conformance-FAIL dispositions, fixture REP-BUILD cases, focused delta review | none (authorized, #1577 c.7233646703, c.7238589944) | exact-head review; mutation-sweep dispatch has its own gate (c.7238783221) | A8 §3; A11 §2.1 |
| 2 | **DP-2**: the tool's exact validation launch and conditional merge of #1577 (designs land with it, M8-11) | **DP-2** (§A.50 item 1) | green validation run on the exact candidate, accepted delta review, landing check of R6.PLACE.8 incl. disjointness from the plan's authorized edit-path set (A11 §2.1) | A8 §5; A11 §2.1 |
| 3 | Post-merge verification of `T_land` | none | `T_land` preserves the reviewed tool, workflow, template and control-input bytes | A11 §2.1 |
| 4 | **Choose final H** on `main`'s first-parent chain at or after `T_land` | owner choice (DP-1: "Choose H only after the tool lands"); S-3: H is selected and pinned together with the plan amendment | merge freeze on papers/, book/ and ledgered paths held from H to L (DP-1) | #1169 c.7214186738; c.7208869709 (S-3); A8 §4 |
| 5 | **Authorize amending the frozen plan** (writing the candidate commits that carry the amendment) | **§A.50 items 2 and 5** (not named in DP-2 or DP-3/4; see O-1) | H chosen | owner restriction quoted on #1477 c.7238789381 |
| 6 | Re-base and records at H: §9 reconciliation (ledger and edits re-derived at H), HP, context and hit records, rule records (OBL-3), allow root, class root, repo scope, delegation contract, OBL-1 parity script, configuration and reviews | none for drafting; non-author reviews required | H; `T_land` bytes for `tool` pins | §2 below |
| 7 | **Place `B` on `main`**: a merge carrying the class root (`ledger-coverage-tool-20261123/records/a1-staging-class-root.json`), the allow root (in `D_rec`), their reviews, and (recommended) the OBL-1 script | **merge, §A.50 item 1** (not named in DP-2 or DP-3/4; see O-2) | reviewed roots; B after H on first parent; T_land a strict predecessor of B | staging r2 §2; A11 §2.2 |
| 8 | Fix `M_rep` (a main commit at or after B) and `S` (B..S first-parent), write `a1-staging-transition.json` | none (part of the amendment) | B exists | staging r2 §2; A11 §2.2; M8-10 |
| 9 | Candidate F: amendment text, Record pins, configuration and its ordinary review; independent focused delta review of the candidate (M8-12; PREREG §25.7 item 3, §31.12.18 item 10) | none (review) | steps 6–8 | M8-12 |
| 10 | Pre-freeze gate at the candidate: PREREG §31.12.17 items 1–5 and §31.12.18 items 6–8 (item 9 optional, M8-13); OBL-16(a): §A.39 exact-head check-run and TR5 chain-admitted run; control-suite at candidate F with live REP-BUILD, the 75 Amendment-9 rows, RT-T and S11-2 all PASS | **DP-3** (pre-freeze dispatches) | branch held at the candidate (§A.43 item 3) | OBL-15, OBL-16; A9 §1; A11 §2.2 |
| 11 | **Designate F**, quoting the transition descriptor (M8-10); OBL-16(b) identity comparison | **DP-3** (§A.50 items 2, 5) | step 10 green | M8-10; OBL-16(b) |
| 12 | Trials T0″/T1″ (re-based §31.8), EI14-dispatch | **DP-3** (§A.50 item 2) | F | §31.8, §31.12.7; OBL-18 |
| 13 | Independent scientific delta review (7.1) and final #1468 regression audit | none (reviews); #1468 has its writer (c.7238783221) | F, trial results | A11 §2.3; A8 §3 |
| 14 | Execution: X (and C), the 14 plan checks through the pinned workflow on `main`, G-A1, narrow SC-42 regeneration approval | **DP-4** (§A.50 items 2, 6) | steps 11–13 | A8 §5; OBL-16 (G-A1) |
| 15 | Merge the plan PR into `main` (r6 §21: "The amended plan merges its pull request into `main` before the landing `L`"); re-resolve M | **merge, §A.50 item 1** (O-3: confirm inside DP-4) | F reachable from main afterwards (§A.42) | r6 §21; R6.TREE.4 |
| 16 | Landing L = merge(M, C): item 14-landing (RT-L, four-tree check), reconciliation records only if ledgered paths drifted H..M | **DP-4** (§A.50 item 1) | step 15 | R6.TREE.11–14; M8-2 |
| 17 | TeX/PDF regeneration verified (FULL.pdf, §31.8), census update, post-merge verify | none | L | A8 §3 |

DP-1 asked for DP-3 and DP-4 to be one consolidated conditional approval "without requiring separate owner
interventions between successful gates" (#1169 c.7214186738). Steps 5, 7 and 15 are owner gates under §A.50 that the
DP definitions of A8 §5 do not name; the shortest path folds step 5 into the H choice, and steps 7 and 15 into the
DP-3/4 package (O-1 to O-3).

Custody (B0, bootstrap, custody file, R6.CUST.10, freeze/close entries) is not on this path: M8-1 makes it required
only before the first freeze of a discharge-bearing configuration. The A1 configuration must therefore cite no
`reassessment` record (§2.1 item C-14).

***

## 2. The amendment changes to P, each with its governing requirement

### 2.1 Configuration `retirement-config.json` (in `D_rec` = `verification/audits/foundations/a1exit-deletion-20261121`)

| # | Field / property | Required content | Governing requirement |
|---|---|---|---|
| C-1 | location and identity | in `D_rec` beside `PREREG.md`; `schema` `oi-retirement-config/1`; `config_id` `a1exit-retirement-config`; `version` 1; `supersedes` null | R6.CFG.1, R6.CFG.4, R6.A1CFG.1 |
| C-2 | fields | exactly the required set `schema, config_id, version, supersedes, retirement, roles, corpus, adapters, profiles, checks, rules, context_mapping, indicators, sentence, hp_obligations, delegation, records, tool, repository_id, operations, controls, author` (optional `notes`, `sites`); no own-review reference in `records` and no `widening_review` key | R6.CFG.4; `engine/config.py` `required`; staging r2 §3 |
| C-3 | `retirement` | `{name, issue}` (#1477 or #1169: O-7) | R6.CFG.4, R6.RECON.33 |
| C-4 | `roles` | `scientific_base` = final H; `pin` = E; `record_commit`; `side_change_classes` = the class-root lineage tip `{path, blob_sha256}` | R6.CFG.4, R6.A1CFG.2, R6.TREE.2, staging r2 §2 |
| C-5 | `corpus` | `papers/*.md`, `book/*.md` (scope record under `records`) | R6.A1CFG.2, R6.A1CFG.5 |
| C-6 | `adapters` | `ledger` `a1exit-exact-edit/2` (ledger.json, companion edits.json), `sitemap` `a1exit-sitemap/2`, `replay` `python-frozen-replay/1` with record tree `b05efdca…`; module pins at `T_land` | R6.A1CFG.2, R6.A1CFG.3, R6.ADAPT.1–5 |
| C-7 | `profiles` | p0-core, p0-para, ledger-ext, ptr, repo, count-grep, item7-literal, register, register-caps, infinity, resid, DR-1/3/4/5, with sources and `pattern_sha256` | R6.A1CFG.2, R6.CFG.5; staging r2 §1 and DELTA-PROPOSAL.json for the item-2 pins |
| C-8 | `checks` | `item2` (coverage): p0-core, p0-para, ledger-ext, `final_profiles: []`; `item7`: ptr, count-grep, resid, DR-1, DR-3, DR-4, DR-5, final ptr, count-grep; `item11`: repo, final repo; no `default_for` | staging r2 §1; R6.A1CFG.2; R6.PLAN.18; OBL-5 |
| C-9 | `executed_suffixes` | contains `.py .lean .yml .yaml .sh` | R6.CFG.4 |
| C-10 | `rules` | the allow-root tip in `D_rec` (W1-b, W1-c, W1-d, W2-a, W2-b; never W1-a), DR and resid rule files, converted EXPLAINED entries | OBL-3; staging r2 §2 "Allow-rule record"; M8-9 (ESC-1) |
| C-11 | `context_mapping`, `indicators`, `sentence` | s3 mapping; ANAPH, LIST, TABLE, PARTIAL; splitter version 2 | R6.A1CFG.2; r6 §6, §8 |
| C-12 | `hp_obligations[0]` | segment `[E, H]` with every first-parent merge on E..H that changes the corpus, each `{pr, commit, first_parent}`; must end at `scientific_base` | R6.CFG.6, R6.HP.1–2; R6.A1CFG.4 (see F-3) |
| C-13 | `delegation` | `{path, blob_sha256}` of the contract the workflow passes, plus `class_adapters` (preserve-check-v1, record-dir/1, rerun-equal/1, fingerprint-regen/1, host-run/1) | R6.CFG.4, R6.A1CFG.3; `cli.py` l.1629–1633 (see F-1) |
| C-14 | `records` | every record and review the run uses: hp.json, context-adjudications.json, hit-classifications.json, gr58 classification v3, repo scope record, rule records, delegation, each with its non-author review; **no `reassessment` kind** | R6.CFG.4, R6.REC.9, R6.ITEM2.3, R6.VALID.3; M8-1 |
| C-15 | `tool` | `files`: the entry point and every file under `tools/ledger_coverage/` at `T_land` (incl. `record_authority.py`); `workflow`: `.github/workflows/ledger-coverage.yml` blob at `T_land` | R6.CFG.4, R6.CFG.6, R6.REC.18, R6.REC.19, OBL-10, OBL-11 |
| C-16 | `repository_id` | 1156244443 | R6.A1CFG.2, R6.REC.18 |
| C-17 | `operations`, `controls`, `author` | all four operations; the tool's `controls.json` pin; the writer | R6.CFG.4, R6.CFG.6 |

### 2.2 Record files in `D_rec` (each a direct child: the pin-table row form admits no `/`)

| # | File | Content | Governing requirement |
|---|---|---|---|
| R-1 | `ledger.json`, `edits.json` | re-derived at H by §9 (redraft each failing `old`, re-pin, explain every changed splice) | PREREG §9; R6.TREE.2; owner safeguard #1169 c.7074829849 ("Every changed splice gets an explicit explanation") |
| R-2 | `edits_check.py`, `guards_check.py`, `preserve_check.py` | preserve_check closes OBL-8 gaps 1, 2, 5, 7; records the gap-6 decision; corrects the gap-8 docstring; self-test fixtures and `STALE` re-checked at H | OBL-8; R6.PLAN.17 |
| R-3 | `hp.json` | one `oi-hp-adjudication/1` record, `sites` for every E..H site change (steps, row/code/owner, own_lines, semantic_classification, splice_attribution, hit_classifications, context) | R6.HP.4–6, R6.HP.14; R6.PLACE.6; OBL-15; r5 obligation "Supply and independently review `hp.json`" |
| R-4 | `context-adjudications.json` | `oi-context-adjudication/1`, `entries` (meaning-context and indicator adjudications); may be empty with `record_id` and a review stating why | R6.ITEM2.3, R6.ITEM2.4, R6.REC.9 |
| R-5 | `hit-classifications.json` | `oi-hit-classification/1`, `classifications` for replacement-region and unheld hit lines; may be empty likewise | R6.ITEM2.3, R6.ITEM2.4; OBL-15 |
| R-6 | `a1-staging-allow-root.json` + ordinary review + widening review (`replaces: null`) by distinct reviewers | five allowances re-derived from bytes at H; `record_id` `a1-staging-w1-w2`; `supersedes` null | staging r2 §2 ("Allow-rule record", "Initial widening review"); S-2 (declared non-authorship) |
| R-7 | rule records DR-1 (a, b, c), DR-3, DR-4, DR-5, resid (a, b, c), converted EXPLAINED, each reviewed | frozen at F | OBL-3; A9 §1 release check |
| R-8 | `a1-staging-transition.json` | closed keys `schema` (`oi-a1-staging-transition/1`), `base` (B), `custody` (`{path, blob_sha256}` of CUSTODY.json), `class_root`, `allow_root` | staging r2 §2; M8-10; `record_authority.py` |
| R-9 | `a1-staging-prior.json` | `{"schema": "oi-a1-staging-prior/1", "freeze": null}` (initial designation) | staging r2 §2 "Prior-freeze continuity" |
| R-10 | configuration ordinary review (and a widening review only if R6.CFG.7 requires one; none for version 1 with `supersedes` null) | names the exact config path and digest; declared non-authorship | staging r2 §3; S-2 |
| R-11 | reviews of the delegation contract, repo scope record and gr58 classification (these three files lie in the tool directory, see F-1) | non-author reviews in `D_rec`, referenced by `records` | R6.REC.1–6; R6.VALID.3 |
| R-12 | `PREREG.md` | the amendment text of §2.3, ending with the last `### N.N Record pins` subsection | R6.REC.16; R6.CFG.1 |

Not carried: `a1-staging-sessions.json` (S-1 registry, superseded by S-2, #1169 c.7213920280). The skeleton on
`8f668f555` is dropped.

### 2.3 PREREG.md text (append-only §32, as §28–§31 were)

| # | Content | Governing requirement |
|---|---|---|
| P-1 | Authority and goal link: the owner decisions relied on, quoted with author and time | §A.42 item 7; §A.47 |
| P-2 | New base H, the §9 reconciliation record and the changed-splice explanations; disposition of the P and O-13 edits whose `old` is gone (F-2) | PREREG §9; S-3; O-13 adoption record item 2 |
| P-3 | §11 items 1–14 restated as the exact workflow arms (table in DRAFT §32.4), each with the structured result field it reads | R6.PLACE.10; R6.PLAN.1–15; R6.STAT.8; §A.44 |
| P-4 | Item 4 "four entries" becomes the seven STALE ids; item 12 "execution head's parent" becomes "the ledger base H" | OBL-9; R6.PLAN.18 |
| P-5 | Item 7: decision rule (keep as frozen if `item7` passes at X; otherwise the OBL-5 restatement with its own review and owner authorization) and the scope statement (OBL-4) | R6.PLAN.8, R6.PLAN.18; OBL-4, OBL-5; O-13 "Item 7, exactly as frozen" |
| P-6 | Item 11 under `--final`; each line of the review load needs an exact rule | R6.PLAN.12 |
| P-7 | Plan-checker obligations: the plan's own check fails on each countercontrol mutant; P-parity of register/infinity by a script on `main` before F | R6.PLAN.16; OBL-27; OBL-1 |
| P-8 | OBL-8 gaps closed and gap 6 decided | OBL-8; R6.PLAN.17 |
| P-9 | Pre-freeze gate: §31.12.17 items 1–5, §31.12.18 items 6–8 and 10; item 9 optional; plus OBL-16(a) and the control-suite at candidate F (live REP-BUILD, the 75 rows, RT-T, S11-2 PASS) | M8-12, M8-13; OBL-15, OBL-16; A9 §1; A11 §2.2 |
| P-10 | Trials T0″/T1″: §31.8 and §31.12.7 with H the new base, `plan_sha` = F, workflow base W unchanged (`a1exit-trial-verify.yml` blob `bca44ac0…` at `413b0bb8` and at `main`) | PREREG §31.8, §31.12.7; §A.50 item 2 |
| P-11 | Execution and landing: the plan PR merged before L; X single parent H; C linear; L two parents (M, C) | r6 §20–21; R6.TREE.9–14 |
| P-12 | Record pins: the last `### 32.N Record pins` subsection lists every file of R-1 to R-11 that lies in `D_rec`; nothing after it until the next `#` heading | R6.REC.16; `engine/config.py` `read_pin_table` |
| P-13 | Verification status and off-main references | §A.46 item 4; §A.42 item 8 |
| P-14 | No-regress rule: gate and trial results recorded outside `D_rec` | PREREG §31.12.17 "The regress" |

### 2.4 Per-check commands the plan must name (from the workflow at `e9d75a32`; re-verify against `T_land`'s blob)

Common prefix (R6.PLAN.2): `--freeze "$F" --config "$F:$CFG" --out "$RUNNER_TEMP/out"`, with `D="${CFG%/*}"` and
`A=verification/audits/foundations/ledger-coverage-tool-20261123`. Dispatched on `main` (`job` = `plan-check`), the
pre-run pin check refusing any other ref (R6.REC.19).

| §11 item | `check` input | Command (after the prefix) | Inputs |
|---|---|---|---|
| 1 | `item1-execution` | `execution --scientific-base "$H" --candidate "$X" --ledger "$F:$D/ledger.json" --edits "$F:$D/edits.json"` | h, x |
| 1 | `item1-terms` | `terms --commit "$X" --profile ptr --classify "$F:$A/records/gr58-hit-classification-v3.json"` | x |
| 2 | `item2-record` | `record --pin "$E" --record "$F"` | e |
| 2 | `item2-coverage` | `coverage --commit "$X" --check item2 --segment "$E..$H" --segment "$H..$X=$F:$D/ledger.json" --hp "$F:$D/hp.json" --classify "$F:$A/records/gr58-hit-classification-v3.json" --classify "$F:$D/context-adjudications.json" --classify "$F:$D/hit-classifications.json"` | x, e, h |
| 3, 4, 5, 6, 8, 9, 10, 12, 13 | `item3` … `item13` | `execution --scientific-base "$H" --candidate "$X" --ledger "$F:$D/ledger.json" --edits "$F:$D/edits.json" --delegation "$F:$A/delegation-draft.json"` (one command; the item is read from its subject, class or profile verdict in the result) | h, x |
| 7 | `item7` / `item7-amended` | `terms --commit "$X" --profile item7-literal` / `terms --commit "$X" --base "$H" --ledger "$F:$D/ledger.json" --check item7 --final --classify "$F:$A/records/gr58-hit-classification-v3.json"` | x (h) |
| 11 | `item11` | `terms --commit "$X" --check item11 --scope "$F:$A/records/repo-scope-v1.json" --final` | x |
| 14 | `item14` | `execution --scientific-base "$H" --main "$M" --candidate "$X" --ledger … --edits … --delegation "$F:$A/delegation-draft.json"` | h, m, x |
| 14 | `item14-landing` | as `item14` with `--certified "$C" --landing "$L"` | h, m, c, l, x |

Candidate-F assessment (OBL-16(a); A9; A11 §2.2): `job` = `control-suite`, inputs `freeze` (candidate F), `config`,
`m` (M_rep), `rep_snapshot` (S), `tool_landing` (T_land), `accepted_tool`, `tool_base`, `fixed_config`; the `A1
controls` step reads `${CFG%/*}/a1-staging-transition.json` at S.

***

## 3. Findings that bear on the shortest path

**F-1. Three plan inputs are read from the tool's directory, so they are fixed at the tool's landing.** The workflow
passes `--delegation "$F:$A/delegation-draft.json"`, `--scope "$F:$A/records/repo-scope-v1.json"` and
`--classify "$F:$A/records/gr58-hit-classification-v3.json"`; `cli.py` refuses a `--delegation` whose path is not
`cfg['delegation']['path']` (l.1631–1633). R6.PLACE.6 places the delegation contract in the plan's record directory,
and the draft itself says "the contract itself belongs in the amended plan record directory at F". `A` is landed
with the tool and pinned by the tool-landing class (R6.TREE.5, R6.PLACE.8), so F cannot change these files. The
delegation contract's `checker_sha256` is P's `preserve_check.py` (`101ecdf4…`), and `deleg_preserve_check.py`
(l.85–86, l.134) refuses any other checker; OBL-8 requires that checker to change, and its self-test and `STALE`
list depend on the ledger base (`preserve_check.py` l.78, l.1245). The contract therefore depends on final H, which is
chosen after the tool lands. As written, items 3, 4 and 8–14 cannot pass at the final H. Two routes, both
requiring no new mechanism: (a) before DP-2, change the arms to read `$F:$D/delegation.json` (and, for symmetry,
`$F:$D/` copies of the scope and gr58 records), matching R6.PLACE.6 and R6.PLAN.12's `F:repo-scope.json`; or (b) a
reviewed tool revision after landing. (a) is the shorter path and is an implementation correction against the
adopted placement rule, not a design change. For the coordinating writer before DP-2.

**F-2. Part of the edit list no longer applies at `main`.** Drafting measurement at `9be526b6`: of 401 P edits, 10
have their `old` absent (D184, D185, D255, D256, D366, D369, D375, D376, D385, D386); of the 11 O-13 edits, 7 (D402,
D404–D409) have their `old` absent, their sites rewritten on `main` by #1589 and #1591 (the six-properties
corrections). The O-13 adoption binds each edit by its old and new sha256 at `53c6601a` and states "Any change to the
old or new bytes of D402–D412, and any further edit, needs a new owner decision", and its file digests change with
any re-base. Seven corpus-changing first-parent merges lie on `53c6601a..main` (#1560, #1580, #1582, #1589, #1591,
#1606, #1607).

**F-3. The design's HP table ends at the old H.** R6.A1CFG.4 lists six merges ending at `53c6601a (= H)`. At a later
H every corpus change on E..H at a merge not pinned is FAIL `provenance-foreign` (R6.HP.2), and R6.CFG.6 requires the
segments to end at `scientific_base`. The final configuration must pin the seven merges above (and any later ones)
with HP adjudications for their sites. A11 separates H_rep (fixed control inputs) from final H but does not restate
R6.A1CFG.4; whether its table is read as the H_rep obligation needs one confirming sentence (O-5).

**F-4. B needs a merge to `main` after H.** A11 §2.2: "A real preparation base B containing the reviewed roots and
archive needs an authorized placement on main's first-parent chain after final H". DP-2 and DP-3/4 (A8 §5) do not
name it.

**F-5. Side changes on H..M other than B and the plan PR are REVIEW_REQUIRED unless a class record covers them**
(R6.TREE.5–6). The DP-1 freeze covers papers/, book/ and ledgered paths only. Holding every merge to `main` between H
and L except B and the plan PR removes the need for any further class record; otherwise each unrelated merge needs a
reviewed class entry (O-4). If no ledgered path changes on H..M, no reconciliation record is needed (R6.TREE.7; M8-2).

**F-6. Item 7 may pass as frozen at the final X.** Item-7 count literals in the corpus fell from 14 lines at
`53c6601a` to 5 at `main` (the remaining 5 are sites of the 399 splices). R6.PLAN.8's "does not pass" was measured at
T1′ and `X_rep`. The amendment should preregister the rule of P-5 rather than adopt the OBL-5 restatement in advance,
which also keeps O-13's "Item 7, exactly as frozen" where the measurement allows.

***

## 4. Drafted now, or waiting for final H or the landed tool

| Item | Now | Needs final H | Needs T_land | Needs B/S/M_rep |
|---|---|---|---|---|
| §32 text: authority, goal link, structure, commands table, OBL-4/5/9 wording, pre-freeze gate, trials, landing, status | **drafted** (DRAFT §32) | values of H, counts | command bytes re-checked against the landed workflow | – |
| preserve_check OBL-8 gap closures (1, 2, 5, 7, 8; gap-6 decision) | code can be drafted | self-test fixtures and `STALE` at H | – | – |
| Configuration | skeleton (field list) | roles, hp_obligations, records digests | tool.files, workflow, controls, adapter module pins | side_change_classes tip |
| ledger.json / edits.json re-derivation; 10 + 7 redrafts | – | yes (§9) | – | – |
| hp.json, context and hit records | schema only | yes | – | – |
| Allow root and rule records (OBL-3) | method (8f668f55 re-derivation scripts) | re-derivation from bytes at H | – | – |
| Class root | – | – | pins from T_land's delta | – |
| Delegation contract | – | yes (checker digest, STALE ids) | route depends on F-1 | – |
| OBL-1 parity script | draft exists (`a1exit-parity-20261127`) | re-run at H | – | lands at B |
| Transition descriptor | form | – | – | values |
| Record pins table | form | digests | digests | digests |

***

## 5. r5 (superseded) carried into r6

Reused: the §32 structure and its §11-to-command table; the item-7 negative controls NC1–NC5; the O-13 method and
its adopted texts for D403, D410, D411, D412 (old text still present at `main`); the reconciliation battery
(`--static`, `--commit H --simulate`, `--pins`, `--repo-scan --final`, both self-tests, `--verify-ledger`,
`--verify-pins`, `duplicate_check`); the obligation to supply and review `hp.json`.

Changed by r6 and its amendments: H chosen after the tool lands (r5 kept `53c6601a`); the configuration admitted
through the pin table, with no own-review reference and no `widening_review` key (staging r2 §3; r5 drafted the
v6.0e form); the named `item2` check and `--check item2` (staging r2 §1); the item-2 context question is settled,
since both item-2 files are required, possibly empty (R6.ITEM2.3–4); the allow rules move from the
`w1-w2-allow-v1..v3` chain to the new allow root without W1-a (staging r2 §2; r5's ESC1 v1-to-v2 diff is obsolete);
the plan's record directory at M is classified by the record-directory rule (r6 §21; r5 left it open); custody
conditional (M8-1); RT-L2 decided at the retirement landing (M8-2); delta reviews (M8-12); CI diagnostic optional
(M8-13); staging activation folded into F's designation (M8-10); session identities by S-2 (no registry); the 75
rule-record rows and live REP-BUILD gate the candidate F (A9, A11).

***

## 6. Open owner decisions

| # | Decision | Why | Source |
|---|---|---|---|
| O-1 | Authorize amending the frozen plan, ideally together with the choice of H | §A.50 items 2, 5; not inside DP-2 or DP-3/4 | #1477 c.7238789381 |
| O-2 | The merge placing B (roots, reviews, OBL-1 script) on `main` after H: fold into DP-3/4 or approve separately | §A.50 item 1; A11 §2.2 | F-4 |
| O-3 | Confirm that DP-4 covers the plan-PR merge before L as well as the landing merge | §A.50 item 1; r6 §21 | §1 step 15 |
| O-4 | Extend the H-drift freeze to every merge to `main` between H and L other than B and the plan PR, or accept class records for them | R6.TREE.5–6 | F-5 |
| O-5 | Read R6.A1CFG.4's merge table as the H_rep obligation, the final configuration pinning the merges on E..H | R6.CFG.6, R6.HP.2; A11 | F-3 |
| O-6 | Disposition of D402 and D404–D409 (sites rewritten by #1589/#1591): withdraw as already corrected on `main`, or redraft (new O-13 decision); confirm that O-13's adoption of D403 and D410–D412 carries over to the re-based files when their per-edit hashes are unchanged | O-13 item 2 binding | F-2 |
| O-7 | `retirement.issue`: #1477 or #1169 | R6.CFG.4 | – |
| O-8 | Route for F-1, (a) before DP-2 or (b) a later tool revision | R6.PLACE.6; `cli.py` | F-1 |
| O-9 | Whether H may equal `T_land`, and whether S may be the candidate F itself | A11 §3 ordering | shortest path |
| O-10 | Item 7: confirm the preregistered rule P-5 | R6.PLAN.18; O-13 | F-6 |
| O-11 | OBL-8 gap 6 (`--commit` mode runs `git worktree add`): accept with a disposable clone, or change | OBL-8 | – |

***

## 7. Local branch and files

- Branch `research/a1exit-amendment-prep-20261128` (local), from `4c79be64`; `research/a1exit-deletion-20261121` not
  moved. The draft is outside `D_rec`, in `verification/audits/foundations/a1exit-amendment-prep-20261128/`, so the
  plan's directory is untouched.
- `DRAFT-PREREG-s32.md`: the now-draftable §32 text, marked DRAFT, with `PENDING-…` markers for every value that waits
  on H, `T_land`, B, S or M_rep.
- `DRAFT-CONFIG-SKELETON.json`: the configuration's field skeleton.

Hashes are in the task report and in `SHA256SUMS` beside this file.
