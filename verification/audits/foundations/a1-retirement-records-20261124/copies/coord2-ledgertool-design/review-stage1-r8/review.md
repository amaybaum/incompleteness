# Independent review r8: the ledger coverage tool at 9da5dd5f (B-2 control, N-5 deduplication; design v5.5.9)

Subject: `9da5dd5f415654050afce40f689d55a13b66bad3`, three commits on `1611c9e81a3c736b084dd9eaef5a02a6e627cdf3`
(b8ec348e, 18f9ec5e, 9da5dd5f). Design `DESIGN-v5.5.9.md` sha256 cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9
(verified). r7 review sha256 0e4034339138326302c79e7cdfd377a90e23af0688eddb04f6507d292936b33b (verified). Writer's
evidence `impl-stage1-r8/MANIFEST.sha256` d5efb19d... (verified: every entry OK); `git diff 1611c9e8 9da5dd5f` sha256
e37be54a... equals the writer's `diff.patch`; staged configuration 83c81a65... (verified; differs from r7's 0daeacb4 only
in the side-change-classes blob sha256, now 534e96bd..., which is that record's blob at 9da5dd5f).

I wrote none of the code or earlier reviews. Read-only on the subject: no commits, pushes, GitHub writes, CI or branch
changes; `coord2-impl-wt` left at 9da5dd5f, clean. My detached worktree (`wt/`) was removed with `git worktree remove`.
Labels: **[git]** real git objects; **[sim]** simulated in-memory host (synthetic git objects); **[NOT RUN]**.

**Verdict: ACCEPT-WITH-NITS.** 0 BLOCKING, 0 DESIGN-ISSUE, 5 NON-BLOCKING (N-6 carried; N-8 to N-11 new; N-5 and N-7
resolved).

## 1. Items

1. **Gate (B-2, N-5 against v5.5.9).** I re-read lines 805-818, 1355-1367, 1447-1525 and 1548-1551 myself. B-2 changes
   no engine code and only adds a control for 1481 ("a ledger or snapshot event that conflicts with the thread
   refuses"), which the 1611c9e8 engine already implemented (confirmed: R7-B2 PASSes over the 1611c9e8 engine). For N-5:
   a ledger event is a designation, withdrawal or supersession *with its comment id* (1450-1452); a landing records the
   same observation in the snapshot and appends it to the ledger (814-818); point 5 processes events "in order of
   creation time, then comment id" (1513-1514) and "a withdrawal of F makes it withdrawn" (1517); a recorded withdrawal
   binds even when deleted (1476-1478); F is admitted if it is "the one designated commit" (1521). The refusal the
   1611c9e8 engine gave ("a withdraw names a revoked commit") is not among 1522-1525's listed refusals and arises only
   from counting one comment twice; it makes every admission after a landing plus deletion impossible, against 1521.
   Processing each comment id once is the reading the text prescribes, not a new rule. Refusing two differing records
   of one id is grounded in 1481 (comment present: one record conflicts with the thread) and 1524-1525 / 1488-1489
   (comment deleted: the event cannot be established; "any other conflict"). It only adds refusals. **Agree: implementation
   defect, no normative change; no DESIGN-ISSUE.**
2. **B-2 [sim].** R7-B2: the engine's own snapshot committed with the designation event's `first_line` altered
   (separately `author_id`): point 5 refused at `ledger` "a recorded event conflicts with the thread", full chain exit 65
   CONFIG_UNREVIEWED; positive (as built) admitted, exit 0. Mutant R7-06 (conflict check skipped for snapshot events):
   **KILLED** by R7-B2 and R7-N5-FORGED in my mutation run. r7's own separation probe (`probe_survivors_r7.py`) gives the
   same refusals at 9da5dd5f.
3. **N-5 [sim].** r7's probe `probe_b1_attack.py` case H (ledger+snapshot; two snapshots; one snapshot listing W twice),
   W deleted: at 1611c9e8 F2 **refused** "a withdraw names a revoked commit"; at 9da5dd5f F2 **admitted** (designation
   9005), F refused at `state`. Control R7-N5 run over the 1611c9e8 engine with the 9da5dd5f controls: R7-N5 and all
   R7-N5-* FAIL (F2 refused, exit 65); over 9da5dd5f: all PASS. All other probe_b1_attack cases are unchanged between the
   two heads.
4. **Dedup safety [sim]** (writer's controls, plus my `probe_r8_dedup.py`, run at both heads):
   - conflicting duplicates refuse, not merged: R7-N5-CONFLICT (first line, author, kind, creation time, commit, body
     sha256); mine: forged ledger record **ordered first** under W's id withdrawing F2 -> refused `ledger` "two records of
     comment 9004 differ (commit, first_line)", exit 65 (C); ledger record of W with kind `designate` -> refused (C2);
     `created_at` differing, W present and deleted -> refused (D; 1611c9e8 admitted: fail-closed tightening);
   - forged event not concealed: R7-N5-FORGED (beside / in place / W deleted) and my C, C2. A record equal on every
     compared field to the genuine one is a no-op;
   - K1: R7-N5-SUPERSEDE (supersession in ledger and two snapshots, deleted: never designates F2; F3 later admitted).
     Mine: F2's designation recorded in ledger and snapshot, then deleted -> F2 refused "designated: []" (E); a
     designation recorded in two snapshots, then deleted -> never designates (E3);
   - other plans/rounds not merged: R7-N5-ROUND (filter precedes dedup);
   - distinct events both bind: R7-N5-DISTINCT. Mine: two landings, W re-recorded as `bound` in snapshot 2 and
     re-appended to the ledger -> F2 still admitted, exit 0; F refused (G; 1611c9e8 refused F2);
   - fields not compared (`edited`, `hidden`, derived `processed`/`designates`) differing -> merged, admitted (A): they
     do not enter the state, and `designates` is recomputed; body_sha256 on one record only -> not compared (B; see N-9).
   No case found in which deduplication admits a commit the design requires refused.
5. **Mutation [sim]** (sec. 2): 81 mutants, 73 killed, 8 survived. All 59 r7 kills still killed (incl. the 53 r6-era
   meaningful kills); R7-06 and R7-07 killed; the six r6/r7 equivalents survive as before; of my 7 new dedup mutants 5
   killed, 2 survive (RV-05: N-8; RV-06: equivalent).
6. **B-1 [sim].** r6's `probe_snapshot.py` at 9da5dd5f: F refused at `state` after the supersession comment is deleted,
   full chain exit 65; output identical to 1611c9e8.
7. **Regression [git]** in my detached worktree at 9da5dd5f with the r8 staged configuration, repro steps 1-7: **385 PASS,
   0 FAIL, 3 NOT RUN (TR5, G-A1, RT-T)**. Exits 0,0,0,0,0,1,1 (step 6: RT-T NOT RUN; A1 controls 1104 s). Control by control:
   vs writer's r7 logs (self-test rows included) the only differences are the 7 added controls (R7-B2, R7-N5,
   -CONFLICT, -FORGED, -SUPERSEDE, -ROUND, -DISTINCT), all PASS; vs the r7 review's run the same; vs the writer's r8
   logs 0 differences. Purity PASS, 0 findings. Release gate: the same 5 environmental failures as r7 (lean-axioms
   toolchain; legacy-records, v3-receipts, citation-roles: shallow repository; v3-corpus).
8. **N-6, N-7.** N-7 resolved: R7-07 is killed by R7-N5-ROUND (under the mutant, the other round's record with W's id
   is processed first and this round's W record then differs, so F2 is refused); the engine filters per plan and round
   before dedup, matching "an append-only list of observed events per plan and round" (1450). N-6 unchanged (sec. 3);
   it ends in INTERNAL, exit 71, which v5.5.9 gives precedence over ERROR "at any stage" (line 860) and which is never
   acceptable; no mandatory requirement violated.
9. **Scope [git].** `git diff --name-only 1611c9e8 9da5dd5f`: `tools/ledger_coverage/adapters/conformance_controls.py`,
   `tools/ledger_coverage/authority.json`, `tools/ledger_coverage/engine/authority.py`,
   `verification/audits/foundations/ledger-coverage-tool-20261123/records/side-change-classes-v1.json`. 4fb2c1ee is an
   ancestor; `diff 4fb2c1ee..9da5dd5f`: 58 files, all added, all under `tools/ledger_coverage*` or the audit directory;
   nothing pre-existing modified. Added lines: no local paths, e-mails, model ids or "workspace". `engine/authority.py`
   line by line: only the `observed_fields` constant and the dedup block in `admit` before the thread comparison; no
   other engine behaviour changed. `conformance_controls.py`: removed lines are only the docstring tail and the two
   control lists, re-added extended; Z9h's function unchanged and PASS. Pins at 9da5dd5f: all 44 `engine_pins` and all
   57 class-record pins match (sha256 and git blob), workflow pin matches, nothing unpinned. b8ec348e **and** 18f9ec5e
   carry stale pins for `conformance_controls.py` (N-10). `origin/research/a1exit-deletion-20261121` =
   4c79be642ca631573f06b444903be75ec4f5e2b6.

## 2. Mutation (`scripts/mutants.py`, `scripts/mutate.py` -> `mut/results.json`, `mut/summary.json`, `mut/mutate.stdout`)

r7's harness unchanged (3 workers); mutants = r7's set (R7-07 re-anchored to the new following line `first = recorded`,
the same mutation of the plan/round filter, identical to the writer's re-anchoring) + the writer's R8-00..06 + my RV-01..07.
Base: no non-PASS row except TR5 and G-A1 NOT RUN (the writer's base had `synthetic/M10` FAIL, a harness artifact of
their run; mine does not). All 81 applied exactly once. Statuses of the 74 shared mutants are identical to the
writer's (68 killed, 6 survived; the writer's "67 killed, 7 survived" is a miscount in the claim, N-11).

| Id | Mutation | Result |
|---|---|---|
| R7-06 | thread-conflict check skipped for snapshot events | KILLED (R7-B2, R7-N5-FORGED) |
| R7-07 | snapshot events of other plans/rounds processed | KILLED (R7-N5-ROUND) |
| R8-00..06 | writer's dedup mutants | all KILLED |
| RV-01 | differing duplicates refuse only if the comment is deleted | KILLED (R7-N5-CONFLICT, -FORGED) |
| RV-02 | `created_at` not compared | KILLED (R7-N5-CONFLICT) |
| RV-03 | `kind` not compared | KILLED (R7-N5-CONFLICT) |
| RV-04 | `commit` not compared | KILLED (R7-N5-CONFLICT) |
| RV-05 | `by` not compared | SURVIVED -> N-8 (no state effect) |
| RV-06 | the last record kept instead of the first | SURVIVED, equivalent (kept records equal on every field the state reads) |
| RV-07 | a duplicate compared, then processed again | KILLED (R7-N5, -DISTINCT, -ROUND, -SUPERSEDE) |

Survivors M07, M13, M24, M38, M53, M58: as r6/r7 (equivalent or redundant).

## 3. NON-BLOCKING

- **N-6 (carried).** A committed snapshot record without `comment_id` raises KeyError (probe I), and one whose
  `comment_id` is a string raises TypeError in the sort (probe F), at both heads: INTERNAL exit 71, not ERROR 65.
  Fail-closed; snapshots are engine-built.
- **N-8 (new).** No control varies `by` between two records of one comment (RV-05 survives). The engine compares it; a
  bound supersession's `by` is never used (it only revokes), so the mutant changes only whether such a pair refuses.
  Smallest fix if wanted: a `by` case in R7-N5-CONFLICT.
- **N-9 (new, pre-existing).** `body_sha256` is compared only when both records carry it, and recorded events are
  compared with a present comment on author and first line only (not creation time or body sha256): a ledger record
  of a present W with a wrong `body_sha256` is admitted at both heads (probe B). The event's meaning is its first line;
  no state effect found; the writer named this narrowness as not acted on.
- **N-10 (new).** Intermediate commits b8ec348e and 18f9ec5e pin a stale `conformance_controls.py` (engine pin and class
  record); the final head's pins are correct. Only the final head is the subject.
- **N-11 (new).** The writer's survivor count says 7 survived (6 equivalents plus synthetic M10); their own results show
  68 killed / 6 survived, the M10 item being a FAIL row in their harness base, not a survivor. Not reproduced in my
  base. Also out of scope and pre-existing: two distinct owner comments both withdrawing F refuse "a withdraw names a
  revoked commit" (probe H, both heads), which point 5 can cover as "any other conflict".

## 4. Files

`scripts/repro.sh` (steps 1-7) -> `results/full/`; `scripts/compare.py` -> `results/compare.json`;
`scripts/check_pins.py` -> `results/pins.jsonl`; `scripts/mutants.py`, `scripts/mutate.py` -> `mut/`;
`scripts/probe_snapshot.py` (r6), `probe_b1_attack.py`, `probe_survivors_r7.py`, `probe_n2.py`,
`probe_ledger_malformed.py` (r7, copied; the last two not re-run) and `probe_r8_dedup.py` (mine) -> `out/<probe>-<head>.stdout` and json;
`out/old-engine-new-controls/` (9da5dd5f controls over the 1611c9e8 engine); `authority-9da5.py` (engine at the
subject, for reading).
