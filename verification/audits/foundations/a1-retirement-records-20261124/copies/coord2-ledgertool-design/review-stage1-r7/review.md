# Independent review r7: the ledger coverage tool at 1611c9e8 (design v5.5.9, adversarial, with mutation tests)

Subject: `1611c9e81a3c736b084dd9eaef5a02a6e627cdf3` (branch tools/ledger-coverage-20261123), one commit on a4566dc2.
Authoritative design: `DESIGN-v5.5.9.md`, sha256 cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9
(verified; the diff from v5.5.8 is the status paragraph and sec. 15 item 0a only). r6 review sha256 0bf9a3ad... (verified).
Writer's evidence `impl-stage1-r7/MANIFEST.sha256` 2947bdc9... (verified, every entry OK); diff.patch 3b67501c...;
staged configuration 0daeacb4f5c027e0e6c8d0b733a20e1daa818b4ecb824cab4a3cd0ee2f36a3ab (verified).

I wrote none of the code or earlier reviews. Read-only on the subject: no commits, pushes, GitHub writes or CI. My
detached worktree (`wt/`, at 1611c9e8) was removed with `git worktree remove`.

Labels: **[git]** real git objects; **[sim]** simulated (in-memory) host only; **[NOT RUN]** needs GitHub/CI.

**Verdict: REJECT** under the brief's item-3 rule, on one control gap (BLOCKING B-2, the engine itself is correct).
B-1 is fixed; all 11 r6 survivors are killed with no regression; regression is clean. If the owner's stopping rule is
applied alone, B-2 is a control gap with a correct engine and the verdict would be ACCEPT-WITH-NITS (as r6 classed G-1
to G-9). Counts: 1 BLOCKING (control gap), 0 DESIGN-ISSUE open (D-1 resolved), 7 NON-BLOCKING (N-1 to N-4 carried,
N-5 to N-7 new).

## 1. BLOCKING

### B-2. No control exercises "a snapshot event that conflicts with the thread refuses" [sim]

- **Requirement.** Sec. 6.3, "Reconciliation": "a ledger or snapshot event that conflicts with the thread refuses".
- **Mutant R7-06** (`scripts/mutants.py`): the conflict check is skipped for snapshot events only
  (`if c is not None and ev not in snap_events and (...)`). The full suite (self-test, synthetic fixture, conformance)
  is unchanged: SURVIVED. TR36 tests a conflicting *ledger*; R5-K1 S2 hits the owner-at-creation refusal, not the
  conflict check; TR32-OWN commits only agreeing snapshots.
- **Separation** (`scripts/probe_survivors_r7.py`, `out/probe-survivors-r7-*`): F designated and admitted; its engine
  snapshot committed with the designation event's `first_line` changed (separately, its `author_id`). Engine: refused,
  point `ledger`, "a recorded event conflicts with the thread", full chain exit 65 CONFIG_UNREVIEWED. Mutant: admitted,
  full chain **exit 0**.
- **Smallest fix.** Add a control (e.g. a TR32-OWN case or a TR36 snapshot variant): the engine's own snapshot
  committed with one event whose `first_line`, and separately `author_id`, differs from the thread's comment ->
  refused at point `ledger`, exit 65.

## 2. Items

1. **B-1 fixed [sim].** `snapshot_events` gives every event of a committed snapshot the top-level `plan`/`round`,
   refuses an event with neither, and refuses an event contradicting the top level; it is the only reader of
   committed snapshots (the ledger is read separately and validated at landing). r6's probe reproduced: at a4566dc2
   F is **admitted** (full chain exit 0) after the supersession comment is deleted; at 1611c9e8 refused at point
   `state`, exit 65 (`out/probe-snapshot-*`). Attacks (`scripts/probe_b1_attack.py`, `out/probe-b1-attack-*`):
   top level naming another plan or round -> its events do not bind here (correct); top-level plan or round missing ->
   refused; top level null with events carrying plan/round -> those bind; a later event contradicting -> refused;
   K1: engine snapshot with the supersession deleted, a forged `designate` event with `designates/processed: true`, a
   forged `supersede` with `designates: true` -> never designate (F2 refused; `designates` is recomputed and bound
   events are excluded); snapshot merged by a non-owner -> can only revoke (design trusts `main`'s access control, sec.
   6.3 residuals); reversed events -> same result (events are sorted); events not a list / an event not an object /
   top level a list / not UTF-8 / not JSON -> refused at `ledger`. Snapshots outside `<ledger dir>/landings/` are not
   read (the tool's own landing path; design names no path). Weak points: duplicates (N-5) and missing event keys
   (N-6).
2. **Controls.** Diff a4566dc2..1611c9e8 of `conformance_controls.py`: additions only (docstring line, helpers,
   eleven controls, the main list and the "every control reported" list); no existing predicate removed or weakened.
   TR32-OWN matches TR32 and sec. 6.3 (engine-built snapshot, plan/round only at top level, deletion, malformed and
   positive cases). R6-G1..G9 match v5.5.9: "Owner at creation" incl. strictly-before at 1 s (G1, G4, G7), snapshot
   `authority_in_force_sha256` (G2), approvals of a ledger change one defective form at a time (G3), host-timestamp
   authorization time (G5, writer's choice c), reused `record_id` (G6), A-change review record (G8), unreadable edit
   status (G9). My run of the new controls over the a4566dc2 engine: only TR32-OWN FAILs (the G controls pass on the
   old, correct engine), as the writer reports. Each G control fails on its mutant (sec. 3).
3. **Mutation** (sec. 3): r6 set 53 killed / 6 survived (the six r6 classed equivalent/redundant); all 11 targets
   killed; none of the 42 earlier kills regressed. New R7 mutants: 6 killed, 2 survived (R7-06 -> B-2; R7-07 -> N-7).
4. **Regression [git]** in my detached worktree at 1611c9e8, staged configuration 0daeacb4, steps 1-7: **378 PASS,
   0 FAIL, 3 NOT RUN** (TR5, G-A1, RT-T). Control by control identical to the writer's r7 logs (0 differences, self-test
   rows included); every r6 control has the same status; 10 added (TR32-OWN, R6-G1..G9). Exits 0,0,0,0,0,1,1 as r6
   (step 6: RT-T NOT RUN; A1 controls 1127 s). Purity PASS, 0 findings. Release gate: the same 5 environmental failures
   as r6 (lean-axioms toolchain; legacy-records, v3-receipts, citation-roles shallow repository; v3-corpus).
5. **N-1..N-4** (sec. 5): none contradicts a mandatory v5.5.9 requirement; documentation status noted per item.
6. **D-1 resolved.** Every fixture world (`host_fixture.bootstrap`) lands the empty ledger in its own merge `c1l`
   after `A`'s merge `c1`, approved after `A` is in force, and every positive control admits there; r6 probe P3 at
   1611c9e8: ledger in the same merge as the first `A` refused ("merged when no verified authority record was in
   force"). This is exactly v5.5.9 sec. 15 item 0a: "lands in its own merge after it, approved under 'Owner at
   creation'".
7. **Scope [git].** 4fb2c1ee is an ancestor; diff 4fb2c1ee..1611c9e8: 58 files, all `A`, all under
   `tools/ledger_coverage*` or `verification/audits/foundations/ledger-coverage-tool-20261123/`; nothing pre-existing
   modified. Added lines: no local paths, e-mails, model ids or "workspace". Z9h control and every purity file
   unchanged since a4566dc2 (only `conformance_controls.py`, `authority.py`, `authority.json` and the class record
   changed; `engine_pins` all match). origin/research/a1exit-deletion-20261121 = 4c79be642ca631573f06b444903be75ec4f5e2b6.

## 3. Mutation results (`scripts/mutants.py`, `scripts/mutate.py`, `mut/results.json`, `mut/compare-r6.json`)

r6's harness unchanged (3 workers instead of 8); each mutant a copy of `tools/ledger_coverage*` at 1611c9e8 with one
replacement, run through self-test, synthetic fixture and conformance controls [sim; synthetic git objects]. Base:
241 PASS + 2 NOT RUN of the non-self-test rows (r6: 231; +10 new controls). All 67 mutants applied exactly once.

- **r6 targets, now killed (11):** M02 (R6-G2), M03 (R6-G3), M06 (R6-G1, R6-G4), M20 (R6-G8), M31, M32 (R6-G3),
  M33 (R6-G1, R6-G4), M34 (R6-G7), M35 (R6-G5), M48 (R6-G6), M59 (R6-G9).
- **r6 kills (42):** all still killed (same or additional controls).
- **Survived (6), as in r6:** M07, M13, M24, M38, M53, M58 (equivalent or redundant per r6; I agree: M07/M38/M58 are
  implied by owner-comment-at-creation plus no owner change since; M24 by the merge-commit check; M53 by the earlier
  per-entry refusal; M13 removes the extra refusal N-1).
- **New mutants of the B-1 fix:**

| Id | Mutation | Result |
|---|---|---|
| R7-01 | top-level default dropped (`ev[key] = top` -> `pass`) | KILLED (TR32-OWN) |
| R7-02 | contradiction check dropped | KILLED (TR32-OWN) |
| R7-03 | missing plan/round accepted | KILLED (TR32-OWN) |
| R7-04 | committed snapshots skipped | KILLED (R5-K1, TR32, TR32-OWN) |
| R7-05 | a snapshot event is not `bound` (a snapshot supersession designates) | KILLED (R5-K1) |
| R7-06 | conflict check skipped for snapshot events | **SURVIVED -> B-2** |
| R7-07 | snapshot events of other plans/rounds bind | SURVIVED -> N-7 (only adds refusals) |
| R7-08 | only `landings/round-0/` read | KILLED (R5-K1, TR32, TR32-OWN) |

## 4. DESIGN-ISSUE

None open. D-1 is resolved by v5.5.9 and the code matches it (item 6).

## 5. NON-BLOCKING

- **N-1 (carried, now reachable through snapshots).** A recorded event naming a present comment that was not an owner
  comment at creation refuses; the design says such a form is "not processed" and refuses only a *conflicting*
  event. With B-1 fixed this reaches committed snapshots (N-2): TR66's first case, F admitted, its engine snapshot
  committed, F admitted again -> refused "a recorded event names comment 9004, which was not an owner comment at its
  creation" (`scripts/probe_n2.py`, `out/probe-n2-*`: admitted at a4566dc2, refused at 1611c9e8) [sim]. Fail-closed;
  contradicts no mandatory text (TR66's expectation concerns admission before any landing; point 5's refusal list ends
  "any other conflict"). Documented: a code comment in `admit` (stated as the engine's reading of sec. 6.3) and the r6
  review; not in the README.
- **N-2 (carried).** Snapshots record unprocessed forms (`owner_comment: false`); consequence as N-1. Documented only
  in the r6 review and here.
- **N-3 (carried).** Audit directory = deepest common directory of referenced records; documented in the docstring of
  `scan` in `engine/config.py`. The design does not say how it is identified; no mandatory requirement contradicted.
- **N-4 (carried).** Kind-specific field checks of a predecessor rule file not run; consistent with the design's
  enumeration of what the predecessor lint verifies; documented in `records.py` (`lint_chain`/`predecessor_problems`
  docstrings). No mandatory requirement contradicted.
- **N-5 (new, introduced into reach by the fix).** The same event recorded twice is processed twice. A landing commits
  the snapshot *and* appends the observed events to the ledger (sec. 5, "Durable evidence"), so a withdrawal W of F
  is then in both. F withdrawn, F2 designated, F2 admitted and landed; W's comment deleted (host without deletion
  events): F2's next admission refuses "a withdraw names a revoked commit" (`probe_b1_attack.py` case H; also two
  snapshots, or one snapshot listing W twice). At a4566dc2 the ledger+snapshot case admitted F2. F stays withdrawn
  (TR31 holds); fail-closed. Smallest fix: deduplicate bound events by `comment_id` (refusing if two records of one
  id differ).
- **N-6 (new).** A committed snapshot event lacking `comment_id`, `kind` or `created_at` raises KeyError: exit 71
  INTERNAL instead of ERROR CONFIG_UNREVIEWED (exit 65) (case I). Ledger events are validated at landing (exit 65,
  `probe_ledger_malformed.py`). Fail-closed; snapshots are engine-built.
- **N-7 (new).** No control shows that a committed snapshot of another round does not bind in this round (R7-07
  survives). Engine correct: a round-r0 snapshot withdrawal of X does not affect round r1 (admitted); the mutant
  refuses r1 "a withdrawal names a commit never designated" (`probe_survivors_r7.py`). Only adds refusals.

## 6. Files

`scripts/repro.sh` (steps 1-7) -> `out/full/`; `scripts/compare.py` -> `out/compare.json`; `scripts/mutants.py`
(r6 set + R7-01..08), `scripts/mutate.py` -> `mut/results.json`, `mut/base.json`, `mut/mutate.stdout`,
`mut/compare-r6.json`; `out/probe-snapshot-{a4566dc2,1611c9e8}/` (r6's probe); `scripts/probe_b1_attack.py` ->
`out/probe-b1-attack-*`; `scripts/probe_n2.py` -> `out/probe-n2-*`; `scripts/probe_ledger_malformed.py`;
`scripts/probe_survivors_r7.py` -> `out/probe-survivors-r7-*`; `out/probes-1611c9e8/` (r6 probes P1-P3);
`out/old-engine-new-controls/` (1611c9e8 controls over the a4566dc2 engine). `exp-*`, `mutsrc/` are `git archive`
exports and mutant sources.
