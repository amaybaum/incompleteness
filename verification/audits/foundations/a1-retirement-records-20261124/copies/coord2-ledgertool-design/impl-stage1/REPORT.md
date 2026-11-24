# Stage 1 implementation report: ledger and terminology verification tool

Writer: the implementation writer (coordinating session `session_013T6pfKuv5mi3MXtKjH2tZb`). Date 2026-11-23.
Authority: owner decision of 2026-11-23, Stage 1 only (local implementation, local commits, local tests; no push,
no GitHub write, no CI). Specification: `DESIGN-v5.1.md` (sha256 0c4ff0e6...a3fe, verified), with
`CHANGES-v5.1.md` (89884a75...43f1, verified) and `review-v5.1/review-v5.1.md` (d0fc4b9c...99f6, verified).

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This report decides nothing about
the retirement, adopts no rule or record, and is not an independent review.

## 1. Commits

Branch `tools/ledger-coverage-20261123` in the worktree created at `main` 4fb2c1eed350edf95da2b316abcca93717246589
(verified: HEAD was 4fb2c1ee, branch as named). Additive commits only; nothing pushed; no amend, rebase or force.

| Commit | Subject |
|---|---|
| 944fc9d19ec8b059da956f0ef26cbc99ee4b070f | engine and entry point |
| 9595265bbb885fe7ea889032c0fe0d62aa24b2f4 | adapters and control runners |
| 6f1ff70fc3c1c2965f9e781cd458babb27df4ae9 | A1 configuration and records as unreviewed drafts |
| aff3cf08761fe5f1c340c26dd8fbb840953f1108 | drop a stale note from the synthetic fixture |
| **8c1e628a08272ad9414929fa8e003020e1cc2234** | Stage 1 control results (unreviewed); **final commit** |

Diff against 4fb2c1ee: **46 files changed, 11660 insertions(+), 0 deletions**. `git diff --name-status` lists
only `A` entries: **no existing file changed** (`logs/name-status.txt`, `logs/diffstat.txt`, full diff in
`diff.patch`). New paths only: `tools/ledger_coverage.py`, `tools/ledger_coverage/{__init__.py,engine/,adapters/}`
and `verification/audits/foundations/ledger-coverage-tool-20261123/`. Committed text was checked for local paths,
model ids, e-mail addresses and the word workspace: none. Full object ids in the committed evidence were checked to
resolve in the object store; two in-memory commit ids were replaced by a marker before commit.

## 2. What was built (S4b-S13)

- **Engine** (`tools/ledger_coverage/engine/`, purity scope): object reader (git cat-file) and in-memory overlay
  commits; anchors, ledgered and unledgered relocation (v1 sec. 4.2-4.4, sec. 5 overlap and image rules); the HP
  region walk with merger reporting, `own_lines` and splice-attribution checks, and `line_splices` by
  `git diff -U0` myers (sec. 3); the context rule, the S0 indicators and structure contexts, all as configuration
  data (sec. 4); profile extraction (`json-pointer`, `python-ast-assign`, `literal-list`) with `pattern_sha256`
  (sec. 6.1); sentence splitter version 2; allow-rule application steps 1-6, deny evaluation on lines, sentences
  and splice images, `item7-literal`, `--check`/`--final` (sec. 5, 6.2); rule lint and widening; the ownership
  chain lint (review record, owner authorization, reviewer not author, verdict coverage, URL/run ids refused)
  (sec. 6.3); configuration loader and fail-closed validator with the classes of sec. 16.6; adapter admission by
  pinned blob; delegation contract (sec. 7); op C with preconditions at `H`, splice postconditions, retained
  edits, mirrors, Lean comment-only check, pins (sec. 11 item 12); the four tree roles, side changes, base-drift,
  reconciliation and the landing composition check (sec. 13); outcomes and exit codes, the wrapper, the result
  schema `oi-ledger-coverage/4` with a subset validator and the independent outcome checker (sec. 5); the Z9
  purity lint and allowlist (sec. 16.1); 83 engine controls.
- **Adapters** (`tools/ledger_coverage/adapters/`): `a1exit-exact-edit/2`, `a1exit-sitemap/2`,
  `python-frozen-replay/1`; delegation class adapters `preserve-check-v1`, `record-dir/1`, `rerun-equal/1`,
  `fingerprint-regen/1`, `host-run/1`; synthetic `line-patch/1`, `artifact-hash/1`. Two control runners:
  `synthetic_fixture.py` (synthetic configuration as in-memory fixture, Y/Z/X controls) and `a1_controls.py`
  (real-tree, adversarial, sec. 11, four-tree controls, Z9g).
- **Audit directory** (`verification/audits/foundations/ledger-coverage-tool-20261123/`): A1 configuration,
  controls file, deny/resid/W1-W2 rule files, GR.md:58 hit classification, repo scope record, side-change classes,
  draft delegation contract, README, and `evidence/stage1-controls.json`. **All unreviewed drafts**, marked so in
  each file. Under the review chain the configuration is refused: ERROR `CONFIG_UNREVIEWED`, exit 65 (control
  CHAIN-REFUSAL, and through the real interpreter in `logs/cli-smoke.log`). Every A1 control therefore ran
  through the control harness, which admits the draft configuration without its chain and records
  `"admission": "control-harness: configuration admitted without its review chain"` in each result.

## 3. Control results

Totals: engine controls 83/83; synthetic controls 36/36 (Y1-Y7, Y9, Y10, Z1-Z8 with Z6b, Z9a-Z9f, Z10, X2-X10,
M10, S7 schema-and-checker); A1 controls 88 of 91 meet their stated expectation. The three that do not are
reported, not adjusted: **RT-L2** (sec. 6), **SW2** under its strict reading (sec. 5) and **Y8** (the runner was
given a placeholder; the recorded engine hashes are equal, 204a2d8b...d681 for both configurations, so Y8 holds on
the recorded values). Byte-identical output over two runs: yes (`logs/determinism.json`, coverage at T1',
1.26 MB result). Z9g on the real engine with every string value of the A1 configuration, its rule files, records,
controls and delegation contract, and of the synthetic configuration, and every A1 review and deny profile:
0 findings (also through `purity-lint --config`, `logs/purity-lint-result.json`).

The full table, one row per A1 control with the design's expected outcome and the measured outcome:

| Control | Expected (design) | Actual | Result |
|---|---|---|---|
| A10r | deny widening (narrower scope) -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A11r | lint: countercontrol does not match -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A1r | widening (added files) -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A2r | widening (literal) -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A3r | widening (fingerprint swap) -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A4r | widening review by the author rejected -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A5r | FAIL deny-match -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A6r | lint: literal does not cover the trigger -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A7r | reused id -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A8r | lint: no negative example -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| A9r | deny widening and its own negative example matched -> FAIL record-invalid (A5r: deny-match) | {"detected": true, "unmutated_rule_lints_clean": true} | meets |
| CHAIN-REFUSAL | the unreviewed draft configuration is refused under the review chain: ERROR CONFIG_UNREVIEWED | {"exit": 65, "stop": {"class": "CONFIG_UNREVIEWED", "detail": {}, "message": "configuration review chain: record verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json: no review record"}} | meets |
| G1 | FAIL delegated-evidence-invalid | ["tex: tex-preserve-check.json: ledger_sha256, candidate, check candidate against "] | meets |
| G2 | REVIEW delegated-evidence-missing | as RT-C | meets |
| G3 | FAIL | ["coverage-ledger: id MAIN:L-3 does not occur exactly once at X", "coverage-ledger: verification/coverage/LEDGER.json differs from the base plus its splices "] | meets |
| L1 | PASS (W1 rule) | {"file": "book/ch19-open-problems.md", "keys": {"count-grep": ["L2"]}, "line": 252, "line_sha256": "239dc82db96bb81b8cf95bb950f78eb07874432253a46118ad8e8ca935468267", "profiles": ["count-grep"], "rule_id": "W1-d", "state": "PASS", ... | meets |
| L2 | PASS (W2 rule) | ["PASS", "PASS"] | meets |
| L3 | FAIL rule-overreach | ["rule-overreach"] | meets |
| L4 | REVIEW unclassified | ["unclassified"] | meets |
| M7 | FAILS rebuild_equal false (v1); under v5.1 the pinned record tree refuses the altered record first | {"cli": [65, "RECORD_TREE_MISMATCH"], "replay_equalities": {"ck_errors_empty": false, "digest_equal": true, "extended_unmapped_empty": true, "rebuild_equal": false, "render_equal": false}} | meets |
| M8 | FAILS render_equal false (v1); refused at integrity | {"cli": [65, "RECORD_TREE_MISMATCH"], "replay_equalities": {"ck_errors_empty": true, "digest_equal": true, "extended_unmapped_empty": true, "rebuild_equal": true, "render_equal": false}} | meets |
| M9 | ERROR record tree | {"cli": [65, "RECORD_TREE_MISMATCH"]} | meets |
| N-W | no deny match | {"exit": 0} | meets |
| RT-A | PASS; 0 errors; 697 anchors | {"anchors": 697, "ck_errors": [], "equalities": [{"equal": true, "name": "digest_equal"}, {"equal": true, "name": "rebuild_equal"}, {"equal": true, "name": "render_equal"}, {"equal": true, "name": "ck_errors_empty"}, {"equal": tru ... | meets |
| RT-C | candidate checks as sec. 11; PASS only with contract evidence; without it REVIEW delegated-evidence-missing | {"checks": [{"edits": 401, "holds": true, "name": "preconditions-at-H", "splices": 399}, {"conforming_changed_files": 43, "ledgered_files": 44, "name": "ledgered-files-conform"}, {"broken": 0, "name": "pins", "python_files": 547}] ... | meets |
| RT-D | 0 deny; W1 and W2 PASS with their rules; GR.md:58 PASS with its record, else REVIEW; resid 17 lines | {"exit": 20, "finding_counts": {"TERMS/FAIL/rule-negative-match": 2, "TERMS/REVIEW_REQUIRED/unclassified": 46}, "pass_lines": ["book/The-Incompleteness-of-Observation-FULL.md:2554", "book/The-Incompleteness-of-Observation-FULL.md: ... | meets |
| RT-D-gr58 | GR.md:58 PASS with its record | {"gr58": {"classified_by": {"blob_sha256": "8177b0923a7eddf09c473ce541e4c23de53067429a31d52260aa35f0bafa8410", "path": "verification/audits/foundations/ledger-coverage-tool-20261123/records/gr58-hit-classification-v1.json"}, "file ... | meets |
| RT-DR | H: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 lines; E: 95; T1': 0 / 0 | {"E": {"alternatives": {"DR-1a": 6, "DR-1b": 2, "DR-1c": 59, "DR-4": 33, "DR-5": 1}, "distinct_lines": 95, "exit": 20, "per_rule_lines": {"DR-1": 65, "DR-4": 33, "DR-5": 1}, "with_sentence_lines": 102}, "H": {"alternatives": {"DR- ... | meets |
| RT-DR3W | exactly one DR-3 sentence at H starting on line 37 and including lines 37-38; 0 at T1' | {"agents-md-at-H": [[37, 39]], "agents-md-at-T1p": []} | meets |
| RT-E | PASS; 697 unchanged | {"exit": 0, "hit_counts": {"PASS": 595}, "seconds": 2.4, "site_counts": {"unchanged": 697}} | meets |
| RT-H0 | FAIL; every FAIL and indicator item HP; 113 hp-unadjudicated; 7 HP meaning; 3 HP structure (reference) | {"exit": 20, "finding_counts": {"HP/FAIL/context-meaning-unverified": 7, "HP/FAIL/hp-unadjudicated": 113, "HP/REVIEW_REQUIRED/context-structure-changed": 7, "HP/REVIEW_REQUIRED/unclassified": 110}, "structure_sites": ["book/The-In ... | meets |
| RT-I7 | FAIL at both; T1': 7 / 0 / 0, A1 4; H: 11 / 1 / 2, A1 179 | {"H": {"A1_lines": 179, "exit": 20, "lines": 14, "literals": {"Fourteen": 1, "six structural": 11, "sixth of": 2}}, "T1p": {"A1_lines": 4, "exit": 20, "lines": 7, "literals": {"six structural": 7}}} | meets |
| RT-I7A | H: 86 deny + 123 final-unclassified = 209 (93 / 216 with sentences); all 95 retired lines FAIL. T1': 0 deny; 12 final-unclassified | {"H": {"deny_lines": 86, "deny_lines_with_sentences": 93, "exit": 20, "fail_lines": 209, "fail_lines_with_sentences": 216, "final_unclassified": 123, "retired_FAIL": 95, "retired_lines": 95, "retired_only_review": []}, "T1p": {"de ... | meets |
| RT-L | composition PASS; the workflow at L equals W's blob; the mutant with H's copy FAILs landing-drops-main-change | {"exit": 10, "mutant": ["delegated-evidence-missing", "landing-drops-main-change"]} | meets |
| RT-L2 | every side change classified and no base-drift (sec. 13.4 sequencing safeguard) | {"main": {"M": "4fb2c1eed350edf95da2b316abcca93717246589", "exit": 20, "main_items": [["base-drift", "AGENTS.md"], ["side-change-unclassified", ".claude/settings.json"]], "side_changes": [{"class": null, "commit": "4fb2c1eed350edf ... | **does not meet** |
| RT-T | PASS only when every record verifies; any missing record leaves REVIEW_REQUIRED or FAIL | {"exit": 20, "note": "no reviewed record exists; RT-T0 shows the result without them"} | meets |
| RT-T0 | FAIL; HP 113/7/3; RET 19/5/3; deny 0; 383 unchanged (168 moved), 197 replaced, 4 removed; 9 merger groups, 22 sites | {"exit": 20, "finding_counts": {"HP/FAIL/context-meaning-unverified": 7, "HP/FAIL/hp-unadjudicated": 113, "HP/REVIEW_REQUIRED/context-structure-changed": 7, "HP/REVIEW_REQUIRED/unclassified": 93, "RET/FAIL/context-meaning-unverifi ... | meets |
| RT-X | one side change (the trial workflow) classified; no RET item from it | {"exit": 10, "finding_counts": {"DELEGATED/REVIEW_REQUIRED/delegated-evidence-missing": 7}, "side_changes": [{"class": "trial-workflow", "commit": "413b0bb88f39cad901befcf4684355c7ee39480b", "h": "dfcfd732b567304db1db5181133da8440 ... | meets |
| S11-1 | FAIL unauthorized-edit | ["delegated-evidence-invalid", "delegated-evidence-missing", "unauthorized-edit"] | meets |
| S11-10 | FAIL lean-code-change | ["delegated-evidence-missing", "lean-code-change", "unauthorized-edit"] | meets |
| S11-11 | FAIL final-unclassified | new active file | meets |
| S11-12 | FAIL pin-broken (a guard-pin splice dropped) | ["delegated-evidence-missing", "pin-broken", "pin-target-missing", "unauthorized-edit"] | meets |
| S11-13 | FAIL (the re-execution does not reproduce the hand-edited file) | control evidence states verbose_equal false | meets |
| S11-14 | FAIL unauthorized-change | ["delegated-evidence-missing", "unauthorized-change"] | meets |
| S11-2a | unclassified new site gives REVIEW_REQUIRED | {"items_on_new_line": ["unclassified"], "note": "the mutant of E is not E, so the deny profiles run on it (sec. 2.3) and its retired forms give deny-match FAILs as well", "run_outcome": "FAIL"} | meets |
| S11-2b | dropped Phase-3 site gives FAIL missing | ["missing"] | meets |
| S11-2c | J row with S1 Yes gives FAIL (op A record_checks) | {"ck_errors": ["CK5 X-13 J with S1 'Yes'"]} | meets |
| S11-3 | FAIL delegated-evidence-invalid (another head_sha) |  | meets |
| S11-4 | FAIL (one STALE value differs from the census) |  | meets |
| S11-5 | FAIL deny-match (register) | [["deny-match", "register"], ["pin-broken", "None"]] | meets |
| S11-6 | FAIL deny-match (infinity) | [["deny-match", "infinity"], ["pin-broken", "None"]] | meets |
| S11-8 | FAIL mirror-mismatch | ["delegated-evidence-missing", "mirror-mismatch", "pin-broken", "unauthorized-edit"] | meets |
| S11-9 | FAIL unauthorized-edit (15 census splices) | ["delegated-evidence-missing", "unauthorized-edit"] | meets |
| S1r | REVIEW rule-fingerprint-mismatch | as V7c | meets |
| S2r | REVIEW rule-stale | [["rule-negative-match", "W1-c"], ["rule-stale", "W1-d"]] | meets |
| SW1 | exactly one FAIL naming each site (697 at E) | {"not_exactly_one_fail": [], "not_exactly_one_new_fail_against_the_unmutated_tree": [], "seconds": 394.1, "sites": 697} | meets |
| SW2 | exactly one FAIL naming each site (584 at H) | {"not_exactly_one_fail": [["book/The-Incompleteness-of-Observation-FULL.md:4895@e837e3db", ["context-meaning-unverified", "unauthorized-change"]], ["book/The-Incompleteness-of-Observation-FULL.md:4905@e837e3db", ["context-meaning- ... | **does not meet** |
| V1 | FAIL deny-match by DR-1b | {"deny": [["DR-1", ["b"], "line"], ["DR-1", ["b"], "sentence"]], "exit": 20} | meets |
| V10 | FAIL deny-match by DR-1a | {"deny": [["DR-1", ["a"], "line"], ["DR-1", ["a"], "sentence"]], "exit": 20} | meets |
| V11 | FAIL deny-match by DR-1a | {"deny": [["DR-1", ["a"], "line"], ["DR-1", ["a"], "sentence"]], "exit": 20} | meets |
| V12 | FAIL deny-match by DR-1a | {"deny": [["DR-1", ["a"], "line"], ["DR-1", ["a"], "sentence"]], "exit": 20} | meets |
| V13 | FAIL deny-match by DR-1c | {"deny": [["DR-1", ["c"], "line"], ["DR-1", ["c"], "sentence"]], "exit": 20} | meets |
| V14 | FAIL deny-match DR-1c, each of four | [true, true, true, true] | meets |
| V15 | REVIEW unclassified via resid only | {"hits": [["resid"]], "items": [["unclassified", ["resid"]]]} | meets |
| V16 | FAIL deny-match by DR-4a | {"deny": [["DR-4", ["a"], "line"], ["DR-4", ["a"], "sentence"]], "exit": 20} | meets |
| V17 | FAIL deny-match by DR-4a | {"deny": [["DR-4", ["a"], "line"], ["DR-4", ["a"], "sentence"]], "exit": 20} | meets |
| V18 | FAIL deny-match by DR-4a | {"deny": [["DR-4", ["a"], "line"], ["DR-4", ["a"], "sentence"]], "exit": 20} | meets |
| V19 | FAIL deny-match by DR-5a | {"deny": [["DR-5", ["a"], "line"], ["DR-5", ["a"], "sentence"]], "exit": 20} | meets |
| V2 | FAIL deny-match DR-3 | [["deny-match", "DR-3"], ["deny-match", "W1-d"], ["rule-negative-match", "W1-c"], ["rule-stale", "W1-d"]] | meets |
| V20 | FAIL deny-match by DR-3 | {"deny": [["DR-3", ["count", "tail"], "sentence"]], "exit": 20} | meets |
| V21 | REVIEW unclassified via resid only | {"hits": [["resid"]], "items": [["unclassified", ["resid"]]]} | meets |
| V22 | FAIL deny-match DR-5; the literal item 7 fails too | {"literal_exit": 20, "rules": ["DR-5"]} | meets |
| V23 | FAIL final-unclassified (ptr hit; no deny) | [["final-unclassified", ["ptr"]]] | meets |
| V24 | FAIL final-unclassified (count-grep hit; no deny) | [["final-unclassified", ["count-grep"]]] | meets |
| V25 | without --final REVIEW; W2 line with its rule under --final PASS; resid-only stays REVIEW under --final | {"resid_final": ["unclassified"], "v23": ["unclassified"], "v24": ["unclassified"], "w2_states": ["PASS", "PASS"]} | meets |
| V26 | REVIEW unclassified each, resid (b, b, b, b, c) | [[true, {"resid": ["b"]}], [true, {"resid": ["b"]}], [true, {"resid": ["b"]}], [true, {"resid": ["b"]}], [true, {"resid": ["c"]}]] | meets |
| V27 | PASS (no hit); accepted residual (sec. 1, sec. 15 items 2 and 3) | {"hits": [], "items": []} | meets |
| V27-glossary | PASS (no hit) as the edited glossary.md:13 line | {"hits": [], "items": [], "line": "**Background independence (A6).** The framework's sixth structural property is finiteness of the substratum: the substratum dynamics is cova"} | meets |
| V3 | FAIL deny-match by DR-4a | {"deny": [["DR-4", ["a"], "line"], ["DR-4", ["a"], "sentence"]], "exit": 20} | meets |
| V3-countercontrol | without --final each of the 95 is REVIEW (unclassified); with --final FAIL (RT-I7A) | {"review_without_final": 95} | meets |
| V4 | PASS (no hit); accepted residual (sec. 1, sec. 15 items 2 and 3) | {"hits": [], "items": []} | meets |
| V5 | FAIL deny-match by DR-4a | {"deny": [["DR-4", ["a"], "line"], ["DR-4", ["a"], "sentence"]], "exit": 20} | meets |
| V6 | FAIL deny-match DR-1b and DR-3 | ["DR-1", "DR-3"] | meets |
| V7a | FAIL rule-negative-match (W1's negative matcher) | [["rule-negative-match", "W1-d"]] | meets |
| V7b | REVIEW unclassified (p0-core and count-grep hits, no rule) | [["unclassified", ["count-grep", "p0-core"]]] | meets |
| V7c | REVIEW rule-fingerprint-mismatch | [["rule-fingerprint-mismatch", "W1-b"]] | meets |
| V9 | FAIL deny-match by DR-1a | {"deny": [["DR-1", ["a"], "line"], ["DR-1", ["a"], "sentence"]], "exit": 20} | meets |
| X1 | ERROR PIN_MISMATCH, exit 65 | {"exit": 65, "stop": "PIN_MISMATCH"} | meets |
| Y8 | identical engine hash recorded for the A1 and the synthetic configuration | {"a1": "204a2d8b09ca63983e42f4eec8db82d266a3dc56f0b8cf054770ddf4f7bed81e", "synthetic": "PLACEHOLDER"} | **does not meet** |
| Z9g | the real engine tree: lint PASS | [] | meets |
| item11-T1p | FAIL final-unclassified for each of the 176 lines (sec. 8.2) until each has an exact rule | {"exit": 20, "final_unclassified": 172, "hit_pass": 4, "of_them_corpus": 14} | meets |

Engine controls (in memory, neutral trees): U1 ok, U10 ok, U11 ok, U12 ok, U13 ok, U14 ok, U15 ok, U2 ok, U3 ok, U4 ok, U5 ok, U6 ok, U7 ok, U8 ok, U9 ok, M1 ok, M11 ok, M2 ok, M3 ok, M4 ok, M5 ok, M6 ok, K1 ok, K2 ok, K3 ok, K4 ok, K5 ok, K6 ok, K7 ok, K8 ok, K9 ok, B1 ok, B2 ok, B3 ok, B4 ok, B5 ok, B6 ok, H1 ok, H2 ok, H3 ok, H4 ok, H5 ok, H6 ok, H7 ok, O1 ok, O2 ok, O3 ok, O4 ok, O5 ok, O6 ok, O7 ok, O8 ok, O9 ok, N1 ok, N2 ok, R1 ok, R10 ok, R11 ok, R12 ok, R13 ok, R14 ok, R15 ok, R2 ok, R3 ok, R4 ok, R5 ok, R6 ok, R7 ok, R8 ok, R9 ok, RL ok, A5r-generic ok, E-A1r ok, E-A2r ok, E-A3r ok, E-A6r ok, E-A8r ok, E-L1 ok, E-L3 ok, E-S1r ok, E-S2r ok, lint-ok ok, rule-negative ok

Synthetic configuration controls: M10 ok, S7-schema-and-checker ok, X10 ok, X2 ok, X3 ok, X4 ok, X5 ok, X6 ok, X7 ok, X8 ok, X9 ok, Y1 ok, Y10 ok, Y2 ok, Y3 ok, Y4 ok, Y5 ok, Y6 ok, Y7 ok, Y9 ok, Z1 ok, Z10 ok, Z2 ok, Z3 ok, Z4 ok, Z5 ok, Z6 ok, Z6b ok, Z7 ok, Z8 ok, Z9a ok, Z9b ok, Z9c ok, Z9d ok, Z9e ok, Z9f ok

Engine-level ids in the table above that are prefixed `E-` (E-L1, E-L3, E-S1r, E-S2r, E-A1r, E-A2r, E-A3r, E-A6r,
E-A8r) are the same mechanisms on neutral text; the A1 versions are the rows without prefix. Some engine controls
check only the mutant direction; the restored direction is the unmutated world of the same control, which is
PASS in each case (U1, the base worlds of K, B, M, H), but it is not asserted separately for every id.

## 4. Reference figures (sec. 0.3)

| Figure | Design | Measured |
|---|---|---|
| sites; s3 categories | 697; 346 / 136 / 109 / 106 | 697; s3 values as the 13-row table of sec. 4 (194+144+5+3 / 136 / 81+28 / 45+28+15+9+8+1) |
| E..H site changes and attribution | 113; #1475 48, #1474 23, #1470 15, #1473 15, #1472 12 | 113; 48 / 23 / 15 / 15 / 12 |
| multi-step HP sites | 3 (Main.md:224, :732, Substratum.md:92) | the same 3 |
| region mergers | 9 groups, 22 sites | 9 groups, 22 sites |
| HP sites overlapped by H..T1' splices | 19 sites / 31 splices (region); 18 / 31 (line); difference Substratum.md:266 | 19 / 31; 18 / 31; the one difference is Substratum.md:266 |
| site outcome at T1' | 383 unchanged (168 moved), 197 replaced, 4 removed | 383 (215 + 168 moved), 197, 4 |
| region lines | 203 | **215** (see sec. 7, item 2) |
| hit lines p0+ext | 84 in regions; 200 unheld; 116 outside = 93 + 16 + 7 | 84; 200; 93 pre-existing + 23 (16 over HP-site splices + the 7 D237, D238, D241, D242, D246, D247, D388) |
| meaning-context FAILs | 12 (7 E..H, 5 H..T1'), the named sites | 12, the same sites (7 HP, 5 RET) |
| indicators | ANAPH 23, LIST 49, TABLE 6, PARTIAL 521 | 23, 49, 6, 521 |
| structure items | 3 HP, 3 RET | **7 HP**, 3 RET (sec. 7, item 1) |
| item-7 literal greps | T1' 7 / 0 / 0, A1 4; H 11 / 1 / 2, A1 179 | the same |
| deny lines | H 86 (DR-1 61: a 6, b 2, c 55; DR-3 0; DR-4 28; DR-5 1); E 95; T1' 0 lines, 0 sentences | the same |
| deny per sentence | H DR-1a 6, b 2, c 65, DR-4 28, DR-5 1; E DR-1c 70 | the same (`logs/sentence-alternatives.json`) |
| DR-3 on AGENTS.md | one sentence at H, lines 37-39; none at T1' | one sentence at H starting on line 37, ending on 39; none at T1' |
| item-7 amendment check, no records | H 86 + 123 = 209 (93 / 216 with sentences); T1' 0 + 12 | H 86 + 123 = 209 (93 / 216); T1' 0 + 12, the named 12 lines |
| retired lines at H (V3) | 95, all FAIL | 95, all `final-unclassified`, none only REVIEW; without `--final` all 95 REVIEW |
| resid table | E 141 / 75 / 41; H 138 / 79 / 42; T1' 98 / 88 / 46; added text 287 lines, 45 hits, 17 resid-only, 4 new | the same (`logs/resid-table.json`); the 4 new lines FULL:6265, appendix-c:108, Complexity.md:206, Structure.md:1010 |
| repo profile at T1' (item 11) | 176 active lines needing an exact rule | 176 (172 final-unclassified + the 4 W2 lines PASS by their rules) |
| E..H chain | 14 commits, 6 change the corpus | 14, 6 |
| op C at T1' | 399 splices verified at H; 23 corpus + 21 other ledgered files conform, LEDGER.json under coverage-ledger | 399 splices and 401 edits verified at H (every `old` unique); 43 changed ledgered files conform plus LEDGER.json under its class; pins 0 broken over 547 Python files |
| frozen replay | 0 errors, 697 anchors | digest, rebuild, render equal; CK errors 0; extended 0; frozen self-test true; 697 anchors |

## 5. Sweeps

- **SW1** (E, 697 sites, last token of the site line deleted, unledgered segment E..X): every site gives exactly
  one FAIL naming it (`unauthorized-change`). 697/697. 394 s.
- **SW2** (H, 584 sites, segments E..H HP and H..X unledgered): every site gains exactly one new FAIL naming it
  (584/584). Under the strict reading ("exactly one FAIL naming that site") 577/584: the 7 sites FULL:4895, 4905,
  4919, ch18:164, 174, 188 and Main.md:332 already carry their E..H `context-meaning-unverified` FAIL at the
  unmutated H (they are the 7 HP meaning items of RT-H0), so they show that FAIL plus the new
  `unauthorized-change`. Recorded as not meeting the strict expectation. 360 s.

## 6. Drift and RT-L2

`main` (4fb2c1ee) differs from `H` in three paths:

| Path | Commit that changed it | Tool result |
|---|---|---|
| `.github/workflows/a1exit-trial-verify.yml` | 413b0bb8 (W) | side change, class `trial-workflow` (draft side-change record, harness) |
| `AGENTS.md` (ledgered; splice D296) | 4fb2c1ee (the sec. A.49 merge) | **FAIL `base-drift`** (no reconciliation record) |
| `.claude/settings.json` | 4fb2c1ee | **REVIEW `side-change-unclassified`** (no class covers it) |

RT-L2 (sec. 13.4) against a predicted `M` = main 4fb2c1ee plus this tool's landing paths (an in-memory commit):
the 45 tool paths are classified `tool-landing`, the workflow `trial-workflow`; **`AGENTS.md` base-drift (FAIL)
and `.claude/settings.json` unclassified (REVIEW)** remain; exit 20. With an in-memory landing composed on that
`M` the same two items remain (D296 translates onto main's AGENTS.md without a composition conflict). Under the
review chain the same run is ERROR `CONFIG_UNREVIEWED` (the side-change record is a draft as well). The sequencing
safeguard of sec. 13.4 ("every side change classified and no base-drift") therefore **does not hold** at the
current main. Nothing was suppressed or relabelled and no baseline was changed. Resolving it needs a reviewed
reconciliation record for AGENTS.md (or a new base) and a reviewed side-change class for `.claude/settings.json`;
both are owner/reviewer decisions outside Stage 1.

RT-X (M = W) holds: one side change, classified, no RET item. RT-L holds: composition passes, the workflow at `L`
equals W's blob, and the mutant carrying H's workflow FAILs `landing-drops-main-change`.

## 7. Not implemented, or not matching the design

1. **Structure REVIEWs at H: 7, not 3** (RT-H0, RT-T0). The 4 further sites (FULL:706, ch02:76, Substratum.md:94,
   :253) are LIST sites unique at E and H whose list context changed in E..H; they are rewritten in H..T1'. The
   reference population (sec. 14) required uniqueness at T1' as well, so it excluded them. The rule was not
   changed. HP outcome unchanged (FAIL).
2. **Region lines 215, not 203.** v1 sec. 4.3 includes the LF in the site span; the measurement script excluded
   it, so a splice that starts at a site's LF overlaps it here and the region grows by whole lines. Site counts (197/4) and the 84 hit
   lines are unaffected.
3. **RT-D:** 45 lines are REVIEW through `resid` under item 7's profile set; the design's 17 counts only lines no
   other review profile (incl. p0-core, p0-para, ledger-ext) hits. Not a rule change; a counting-basis difference.
4. **Seed rule W1 for ch19:198 / FULL:5270 fails its own negative matcher.** The sentence contains "finite periodic
   quotient"; the design's W1 negative list contains `finit`. With the drafts, those two lines are FAIL
   `rule-negative-match` instead of PASS. Left as specified for the reviewer (a narrower negative literal would
   be a rule decision). The W2-b context literal is `\mathrm{SU}(3)` because "SU(3)" does not occur literally in
   the sentence; W1-b's context is "isotropy, sublattice structure, link content" rather than the full list, so
   that V7c gives `rule-fingerprint-mismatch` as specified.
5. **Added-text deny profiles** are evaluated on each splice image net of equal matches in the replaced text
   (the frozen checker's comparison). Line-level evaluation gave 30 false deny matches at T1'. Reproducing P's
   recorded 0 for items 5 and 6 needed three A1 parameters, carried as configuration data, not engine code: CAPS
   only for edit kinds ptr/consistency/handoff (`splice_kinds`), the replaced text read with `A1` as
   "finiteness" (`replaced_text_rewrite`), and the "finiteness ... fails" key (`match_keys`). `register` is split
   into two profiles, `register` (REG) and `register-caps` (CAPS less CAPS_OK).
6. **Schema additions** beyond the field table of sec. 16.2: profile fields `levels`, `combine`, `except`,
   `report_regex`, `splice_kinds`, `replaced_text_rewrite`, `match_keys`; `checks[].default_for`; optional
   `notes` and `sites` (synthetic declared sites); `commit` on ledger/sitemap references and companions (the
   ledger is pinned at P until F exists); `item7-literal` has kind `countercontrol`. The rule-file kind
   `review-pattern` holds `resid`.
7. **Root of trust.** `--config-sha256` stands in for F's pin table; the configuration's own review and
   authorization are found beside it (naming its blob). The check that `retirement.owner` equals the owner who
   designated F (O5 root of trust) is not implemented: no designation record exists.
8. **Widening reviews** are separate review records of kind `widening` naming the record's blob and admitted by
   the configuration, not a field inside the record (a field would make the hashes circular).
9. **Delegation.** Classes needing a disposable full clone at X (preserve_check runs, SC-42 re-execution, the
   census for LEDGER.json) are not executed locally (sec. A.40); the evidence files the contract names are read
   when supplied, and without them the class is REVIEW `delegated-evidence-missing`. Native parts run (TeX source
   stamps, PDFs changed, LEDGER.json equal to H plus splices outside the seven values, ids exactly once). So RT-C
   is REVIEW, not PASS. CI plan: one job materializes a clone at X, runs `preserve_check.py --commit X --plan F
   --result-json`, the SC-42 checker (plain and -O), `proof_census.py --json`, uploads the result files, and runs
   `execution ... --evidence DIR`; the host-run record is read from the API.
10. **M7/M8** (altered frozen sitemap/LEDGER.md): at the CLI the pinned record tree refuses them first (ERROR
    `RECORD_TREE_MISMATCH`); the replay adapter on the altered materialization reports `rebuild_equal` false and
    `render_equal` false as v1 expected.
11. **rule-stale** is not evaluated on trees that are ancestors of the rule's `recorded_at` (E and H cannot hold
    T1' fingerprints); otherwise RT-E would be REVIEW. Stated scoping choice.
12. **`self-test --real-trees`** is not in the engine CLI (the engine names no adapter). Real-tree controls run
    through `adapters/a1_controls.py`, the synthetic ones through `adapters/synthetic_fixture.py`.
13. **Explanations** carry the class, rule id, detail and `resolution_needed` for REVIEW items, but not the full
    per-subject explanation object of sec. 5 for every PASS site and hit. The JSON Schema covers the top level,
    items, sites and hits, and is checked by a subset validator.
14. **Partial or simplified:** C's further commits are checked for linear parentage only, not classified path by
    path; the landing "diff M..L equals diff H..C after translation" is enforced through the per-path composition
    rules (R12 surfaces as `landing-extra-change`); a generated-artifact conflict is reported as
    `delegated-evidence-missing`; context adjudications are implemented but exercised only through the FAIL and
    REVIEW paths; PIN_OK after F (N1) is "recorded_at not an ancestor of F"; N2 makes a reconciliation entry on a
    candidate path `record-invalid` without changing the candidate's items.
15. **Z9 interpretation.** The allowlist exempts a literal from both the equality and the profile-match clauses
    (outcome names are matched by `register-caps`); `list` and `check` are on it as output/CLI field names.
16. **Synthetic configuration** is in-memory fixture data in `adapters/synthetic_fixture.py`, never committed as
    a record (design sec. 16.5), although the task wording listed synthetic configuration records for the audit
    directory. The control runners sit in `adapters/`, outside the purity scope.
17. **Not run:** RT-T (needs reviewed records; none exist); the sec. 11 row-3 PDF case with a real host run (CI
    only). O9 and O10 (deferred) were not implemented.

## 8. Repository checks

`tools/release_gate.py` on the final branch and on unchanged main 4fb2c1ee (same worktree, the three new paths
moved aside and restored) gives the same step results: PASS on 17 steps; FAIL on `lean-axioms` (no Lean
toolchain), `legacy-records`, `v3-receipts`, `citation-roles` (undecidable: shallow repository) and `v3-corpus`.
All five fail identically on main: environmental, not caused by this change (`logs/release-gate-*.log`).

## 9. Reproduction

From the worktree at 8c1e628a (any empty output directory outside the worktree):

    python3 -I -B tools/ledger_coverage.py self-test --out OUT/selftest
    python3 -I -B tools/ledger_coverage.py purity-lint --out OUT/purity --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json
    python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py OUT .
    python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --out OUT/a1   # about 20 min; --skip-sweeps about 7 min
    python3 -I -B tools/ledger_coverage.py coverage --config HEAD:verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json --config-sha256 3ac12e24e58fe1494f35532f1720476d89696b7bc1d97df426a1d7e21bf8b913 --commit e837e3dbaa605efc867a213f3345cee14c36d8f5 --out OUT/chain   # ERROR CONFIG_UNREVIEWED, exit 65
    python3 tools/release_gate.py

## 10. Files here

`REPORT.md` (this file), `diff.patch` (full diff 4fb2c1ee..8c1e628a), `logs/` (commit list, name-status, diffstat,
A1 control JSON and stdout, engine self-test result, synthetic stdout, determinism, CLI smoke, sentence and resid
recounts, purity lint, both release-gate logs, the controls table), `MANIFEST.sha256`.
