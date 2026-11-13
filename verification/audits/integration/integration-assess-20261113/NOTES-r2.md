# Notes to INTEGRATION-ASSESS-r2

r2 revises the r1 notes for findings F6, F13 and F17 of `REVIEW-r1.md` and for the heads that moved
after r1 (§2A, §4). Dispositions are in `RESPONSE-r1.md`.

## 1. What was done

- Read `AGENTS.md` (§A.25, §A.28, §A.36, §A.39, §A.42, §A.43, §A.45, §A.46).
- Read the authorization records through the host API: #1169 comment 6863414487 and #1274 comment
  6863419164 (both `amaybaum`, 2026-11-13T19:58Z).
- For each of the nine PRs, read through the host API: the PR body, every review (state, commit id,
  body), every Issue comment and review comment, and the file list. The ChatGPT exact-head reviews
  are reviews posted under the owner's account with the heading "ChatGPT …".
- Fetched `main` and the nine branches by name, full history (no `--depth`). Heads matched the
  task table: `d015131d`, `2a9f10ba`, `c539a60c`, `d8e4f80e`, `703ae20e`, `ffc9cda4`, `9eeee392`,
  `e81e4fb2`, `4cd39871`. Every branch's merge base with `main` is `c3b5f37a`; each is 2–15 commits
  ahead and 0 behind.
- Read in the branches: each record's header, status and §A.42 item 8 table (REC-1 r8 §6,
  TUNE-1-SOURCING r2 §7, BELL-LADDER r3 §6, SYNTHESIS r3 §8, #1274 `DEPENDENCIES.md` and
  `PROVENANCE.md`, Q-868-H `OBJECTS.md`, #1270 `README.md`), RECONCILE r3's header and §4–§5, G3 r5's
  header, §4 and §6. The 47-row REC-1 table, the proofs and the reviews' arguments were not
  re-checked: this is an integration assessment, not a scientific review.
- Read the external dependency PRs' state and reviews (#1267, #1214, #1231, #1232, #1230, #1221,
  #1219, #1211, #1210): all open; #1267, #1231, #1232, #1230 have ChatGPT reviews at their heads;
  #1214 and #1221 have none on the PR.

## 2. Mechanical checks

Commands, per head, in one detached worktree of the shared repository created for this purpose and
removed afterwards (the assigned read-only worktree was not modified; its status is clean at
`c3b5f37a`):

```
git merge-tree --write-tree origin/main <head>
python3 -I -B tools/artifact_placement_check.py
python3 -I -B tools/claims_check.py
python3 -I -B tools/staleness_check.py
python3 -I -B tools/voice_check.py
python3 -I -B tools/duplicate_check.py
python3 -I -B tools/dependency_label_check.py --strict
python3 -I -B tools/legacy_records_check.py <head>
python3 -I -B tools/citation_roles_check.py <head>
python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py --verbose
cmp <its stdout> verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json
```

Control: the same battery on `main` (`c3b5f37a`) exits 0 for every check and the SC-42 output is
byte-equal to the committed result. The SC-42 self-test (mutation controls) was not run; the PRs
touch no manuscript file it mutates.

| Head | merge-tree | placement | claims | staleness | voice | duplicate | dep-label | legacy | citation-roles | SC-42 |
|---|---|---|---|---|---|---|---|---|---|---|
| `d015131d` #1274 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `2a9f10ba` #1268 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `c539a60c` #1272 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `d8e4f80e` #1273 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `703ae20e` #1271 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `ffc9cda4` #1269 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | FAIL: "added-text scan: 3 hit(s)" |
| `9eeee392` #1276 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `e81e4fb2` #1275 | clean | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | equal |
| `4cd39871` #1270 | clean | 0 | **1** | 0 | 0 | 0 | 0 | 0 | 0 | FAIL: "added-text scan: 8 hit(s)" |

- SC-42 hits, all pattern `local-path` on the session-storage word: #1269
  `assess-868-r3a/ASSESS-868.md` (2), `assess-868-r3a/review/REVIEW-868-r3.md` (1); #1270
  `eoi-package/eoi-audit/PACKAGE-r2.md` (2), `PACKAGE.md` (2), `REVIEW-PACKAGE.md` (1),
  `eoi-package/gate/GATE-DRAFT.md` (1), `gate/REVIEW-GATE-r3.md` (1),
  `qphen-review-chain/review/REVIEW-PHASE1-r4.md` (1). These match the lists in #1269 `OBJECTS.md`
  and #1270 `README.md`.
- `claims_check` on #1270: `eoi-package/eoi-audit/AUDIT-C5.md`:149, rule "GR: thermality asserted
  purely kinematic (H-balance)". Matches the README.
- Path overlap: no path is added by more than one of the nine PRs (all changes are additions), so
  any landing order merges without conflict against `main` at `c3b5f37a`.

CI at each head (check runs attached to the head commit, read through the host API): 26 success
and 1 skipped for #1274, #1268, #1272, #1273, #1271, #1276. Failures: #1269 "Numerical probes /
core B" at step "SC-42 integration source scope and must-fail controls", and the aggregating
"Numerical probes"; #1275 "Mathlib bridge" at step "Install elan", then the Lean steps that need it
(KTOKEN-MAXCONE-1 A3, KTRANS-SEP-2 build/elaborate/axioms) — an installation failure: the Release
gate step was skipped, not run. The job succeeded at the later head `46a548fb`; #1270 the SC-42 step, "Numerical probes", and
"Mathlib bridge" at step "Release gate" (the `claims_check` hit).

## 2A. Re-check at the moved heads (r2)

All heads were re-fetched by branch name with full history. Unchanged: #1274 `d015131d`, #1272
`c539a60c`, #1273 `d8e4f80e`, #1271 `703ae20e`, #1269 `ffc9cda4`, #1276 `9eeee392`, #1270
`4cd39871`. Moved: #1268 to `3a3aa146` (adds `REC-1-r9.md`, `REC-1-NOTES-r9.md`,
`REC-1-CONFIRM-r9.md`); #1275 to `1ad01923` (adds unit 2(a): `G3-UNIT2A-r1/r2/r3.md`,
`NOTES-U2A-r1/r2/r3.md`, `REVIEW-U2A-r1.md`, `CONFIRM-U2A-r2.md`, `RESPONSE-U2A-r1/r2.md`). New, not
candidates: #1282 at `a03af682` (`drafts/c3-rlin-xiii-20261113/`), #1279 at `cc297f16`
(`verification/audits/integration/integration-assess-20261113/`).

The same battery, in one temporary detached worktree removed afterwards with `git worktree remove`,
exits 0 for every check, with SC-42 byte-equal, at `3a3aa146`, `1ad01923` and `a03af682`;
`git merge-tree --write-tree origin/main` exits 0 at each. Both moved PRs remain add-only (status `A`
only); across the eleven current heads no path is added twice. Added 40-hex ids: 19 at `3a3aa146`, 10
at `1ad01923`, all resolving; the sensitive-pattern scan finds nothing.

Reviews and records posted after r1's inputs were read: #1269 ChatGPT focused recheck 5897397957 at
`ffc9cda4` (20:15:15Z, ACCEPT); #1268 owner record c.6863753317 (20:14:06Z, P5 "Name both"); #1268
ChatGPT 5897679945 at `3a3aa146` (20:34:33Z, ACCEPT, bounded housekeeping); #1275 checkpoint
c.6864323211 (20:38:22Z, unit 2(a) r3). Read as well: #873 c.6863416405 (19:58:10Z; Q4, Q7, Q8) and
#1265 c.6846206075 (06:44:20Z; the landing-package pattern).

CI: at `3a3aa146` 26 success, 1 skipped; at `46a548fb` 26 success, 1 skipped (Mathlib bridge
succeeded); at `1ad01923` 25 queued, 1 skipped at reading. The Mathlib bridge job at `e81e4fb2` shows
step 3 "Install elan" failure and step 6 "Release gate" skipped.

Blobs at the moved heads: `REC-1-r7.md` `f1ffac0e`, `REC-1-r8.md` `615b7de8`, `REC-1-P0-r3.md`
`611a4d9a` unchanged at `3a3aa146`; `REC-1-r9.md` `945b7982`; `G3-UNIT1-r5.md` `816f91a2` unchanged
at `1ad01923`; `G3-UNIT2A-r3.md` `ff1875d4`. `REC-1-r9.md`:496 keeps r8's landing bar.

The committed copies of `INTEGRATION-ASSESS-r1.md` and `NOTES-r1.md` at `cc297f16` are byte-identical
to the r1 working files, and the committed `REVIEW-r1.md` is byte-identical to the review's working
copy.

## 3. Identifiers and data hygiene

- Every full 40-hex id added by each PR (10, 16, 4, 3, 3, 55, 3, 6 and 102 distinct ids) resolves
  to an object in a full clone of the repository (§A.42 item 3).
- Commit ids classified by reachability (on `main` / only on the PR's own branch / on another
  branch): the off-`main`, other-branch ids are the ones in §2.2 of the assessment (`ea12fde1`,
  `86a413c8`, `e1534b08`, `e41cf613`, `703ae20e` in #1274; `77226128`, `8228b3c2` in #1268;
  `8228b3c2`, `9f7d2612` in #1272; `ea12fde1`, `86a413c8` in #1271; `820519cf` in #1269; in #1270
  `820519cf`, `44f7c328`, `c9d14e11`, `4c7f3f86`, `f1336264`, `f634f8e3`, the four recovered qc21
  commits and the FHE-SEL-1 heads `cc453774`, `7d707bb5`, `83eca7cd`). Own-branch ids become
  reachable from `main` only through a merge-commit landing.
- No added line in any PR matches an e-mail, GitHub-token, AWS-key, signed-URL, IPv4 or absolute
  local-path pattern.
- Blobs that later records pin and that a landing must not change: #1274 `NEW-RESULTS.md`
  `1859e8c5`, `DEPENDENCIES.md` `6c127b0a`; REC-1 `REC-1-r7.md` `f1ffac0e`, `REC-1-r8.md`
  `615b7de8`, `REC-1-P0-r3.md` `611a4d9a` (unchanged at `2594d474`); TUNE-1-SOURCING r2 `35c5c116`;
  BELL-LADDER r3 `0298088d`, NOTES-r3 `963d7352`; Q868H-UNIT1 r3 `ebf5215b`; G3-UNIT1 r5
  `816f91a2`.

## 4. Parallel work observed

- REC-1 r9 (`2594d474`) and its confirmation (`3a3aa146`): read at header, P5, §6 bar and the
  confirmation's verdict; r9's 30 new §6 rows were not re-traced (review 5897679945 checked them).
- G3 unit 2(a) r1–r3 (`46a548fb` … `1ad01923`): read at header, the checkpoint comment and the effect
  on unit 1; not reviewed here, and its references not traced.
- #1282 (C3 check, r1 at `a03af682`, r2 in progress): read at its PR body only.
- No branch, PR, Issue or comment was written by this assessment.

## 5. Judgement calls the owner may want to revisit

- **§A.46 item 2 basis.** I followed the #1265 precedent (#1265 c.6846206075;
  `oa-1-20261112/STATUS.md`, "Landing"): a record lands as the evidence for the scoped claim it
  states. A stricter reading (land only what an established claim, reproducibility or a record
  already on `main` needs) would hold back all nine PRs: no record on `main` has an item 8 gap that
  any of them closes (ARP-1-MARC classes the EOI package as provenance, `preregistration.md`:124).
  Stated in the assessment itself at §6, with OQ-10.
- **#1271.** Kept on its branch because its verdicts are about off-`main` commits. If the owner wants
  the reconciliation's hand checks (RV:47–62) resolvable from `main` for readers of #1274, it can
  land with an item 8 table that labels the drafts as its objects of study; the gap would then be
  closed by landing #1230/#1232, or landed under a recorded owner exception (§A.42 item 8), which
  leaves those verdicts not established (§A.46 item 1).
- **#1273 safeguards.** Judged already reflected in r3's text (r3:79–81 conditional MI*; AL4 fixed
  regions, r3:198–200); a reviewer may still want the operational definition of "complete record"
  (heralds and failures included) stated in the record rather than only in the status note.
- **#1274 optional nit.** Recommended not to apply: it corrects no defect.
- **G3 placement.** A new `programmes/gravity/` directory is compliant with §A.36; placing it
  instead under `verification/audits/manuscript/` (it audits GR §6.2) is the alternative.
