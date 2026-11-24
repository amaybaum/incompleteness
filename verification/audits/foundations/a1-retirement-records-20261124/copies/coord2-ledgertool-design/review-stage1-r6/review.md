# Independent review r6: the ledger coverage tool at a4566dc2 (design v5.5.8, adversarial, with mutation tests)

Subject: `a4566dc2618edb69c337c64b9d886cb0d1b1d8da` (branch tools/ledger-coverage-20261123), on top of 015edf3f.
Authoritative design: `DESIGN-v5.5.8.md`, sha256 f531948147b3638c5ad567f5ccf0eedfd04650a30be9fd0a9f2084aa13a77ad2
(verified). Writer's evidence `impl-stage1-r6/MANIFEST.sha256` sha256 53809e74d37984bc361caf94482e2b7a9e595e3b31f8fa0698d1d90dcaf1edd2
(verified); staged A1 configuration sha256 e9e0abbabfb5fa30b5e1cd86d94c616f4e65bcb169a0ac1079750680ea95a199 (verified).

I wrote none of the code or earlier reviews. Read-only on the subject: no commits, pushes, GitHub writes or CI. My
detached worktree (`wt/`, at a4566dc2) was removed with `git worktree remove` at the end.

**Verdict: REJECT.** 1 BLOCKING finding on the engine (B-1, demonstrated on the engine's own output), 9 control-gap
findings from surviving mutants (G-1 to G-9; the engine itself behaves correctly in each, see sec. 3 for how they
are classified), 1 DESIGN-ISSUE, 4 NON-BLOCKING.

Labels: **[git]** tested on real git objects; **[sim]** simulated (in-memory) host only; **[NOT RUN]** needs
GitHub/CI.

## 1. BLOCKING

### B-1. A withdrawal or supersession in a committed admission snapshot never binds: the engine ignores the events of its own snapshot format [sim]

- **Requirement.** Sec. 6.3 reconciliation: "a withdrawal or supersession in the ledger or in a committed snapshot
  binds, even if its comment is now deleted, hidden or edited, so it can never silently reactivate an earlier
  freeze"; TR32; "Completed actions": "the events it appended bind under reconciliation".
- **Code.** `engine/authority.py` `admit`, the reconciliation loop: `for ev in list(ledger['events']) + snap_events:
  if ev.get('plan') != plan_id or ev.get('round') != round_id: continue`. The admission snapshot the engine itself
  builds (`snap['events']`, the snapshot an acceptance landing commits as `snapshot.json`, cf. `replay_controls`)
  carries `plan` and `round` only at the snapshot's top level; its events have the keys `author_id, by, comment_id,
  commit, created_at, designates, first_line, kind, owner_comment, processed`. Every event of a real committed
  snapshot is therefore skipped.
- **Counterexample** (`scripts/probe_snapshot.py`, `out/probe-snapshot-a4566dc2/probe_snapshot.json`): owner 4242
  designates F and supersedes F by F2 in the thread; F2 is admitted; its admission snapshot, exactly as `auth.admit`
  returns it, is committed on main at `syn/freeze/landings/round-1/snapshot.json` (the directory the engine reads);
  the supersession comment is deleted. Admission of F: **admitted**; full chain on F: **exit 0**. The superseded
  freeze is reactivated. Control variant (plan and round copied into each event): refused at point 5, exit 65.
- **Why the suite misses it.** TR32 and R5-K1 hand-build snapshot events that carry `plan` and `round`; no control
  commits a snapshot produced by the engine.
- **Pre-existing:** identical at 015edf3f (`out/probe-snapshot-015edf3f/`), present since 380e7d69. In scope as part
  of the acceptance chain.
- **Smallest fix.** In the snapshot loop, give each snapshot event the snapshot's top-level `plan` and `round` (refuse
  a snapshot that has neither per event nor at top level), or write `plan`/`round` into every event of the admission
  snapshot; add a control "TR32 with the engine's own snapshot" (the probe above).

## 2. Item-by-item results

1. **Acceptance routes** (designation, withdrawal, supersession, recorded events, authority changes incl. owner-id
   change, ledger changes on main and at landing, record/authorization lint, predecessor lint, consumer predicate,
   replay). Former-owner, future-owner, away-and-back, replay (single use), late approval, wrong thread, lineage
   (missing/unrelated/fork/two heads/cycle/reuse/invalid predecessor) were all refused in the engine [sim]; the
   forged/committed-snapshot route fails open (B-1). One extra refusal (N-1).
2. **v5.5.8 rules.** Owner at creation for designations, withdrawals, supersession halves, approvals of `A` changes
   and ledger changes, new-id approvals and owner authorizations (incl. predecessors and widening reviews): as
   written. Point 3 extension and snapshot recording (`authority_in_force_sha256`): implemented (snapshot recording
   untested, G-2). C5 "has designated" (`ever`): as written. K1 (recorded supersession only revokes): as written for
   events the engine reads, but see B-1. DI-2 lineage rules incl. reuse (sec. 6.3 line 1247): implemented; reuse
   untested (G-6). One verdict per added ledger event; four-part procedure for every ledger change: as written.
   `A.supersedes` (DI-2 for `A`): as written.
3. **Mutation testing.** 59 mutants (57 applied in the first pass, M31 and M53 corrected and rerun): killed 42;
   survived 17, of which 6 equivalent or redundant (M07, M24, M38, M53, M58, and M13 which removes an extra check
   not in the design) and 11 weaken a v5.5.8 requirement without any control failing (G-1 to G-9). Sec. 3.
4. **Before/after.** Controls of a4566dc2 on the 015edf3f engine [sim; synthetic git objects]: TR55-TR59, TR65-TR70,
   LN1-LN4, LN6-LN9, LN11, LN12 and R6-EV FAIL; TR54, TR60-TR64, LN5, LN10 PASS (positives, or outcomes the old
   current-owner rule already produced); every other control PASS. Identical to the writer's table. At a4566dc2 all
   30 PASS. The predicates match their rows (harness at point 5 where the row says "control harness"; full chain
   with the point-7 refusal for TR54/TR61's second cases). TR57/TR58 and TR26 test both defects at once, as their
   rows state, which is why G-3 and G-8 survive.
5. **Regression [git].** Full repro (steps 1-7) in my own worktree at a4566dc2 with the staged configuration:
   368 PASS, 0 FAIL, 3 NOT RUN (TR5, G-A1, RT-T); A1 controls 90 passed, RT-T NOT RUN; purity PASS, 0 findings.
   Control by control equal to the writer's r6 logs, and every r5 control has the same status (no regression;
   30 added). Release gate: the same 5 environmental failures as r5 (lean toolchain, shallow repository).
6. **Fixture adjustments.** All 8 follow from v5.5.8; no predicate of an existing control was removed or weakened
   (checked on the diff 015edf3f..a4566dc2: removed lines are only fixture construction and docstrings). #1 is the
   consequence verified by probe P3; #5/#6 keep TR25/TR29's meaning.
7. **Writer's choices.** (a) consistent: the design's parenthetical enumerates what the predecessor lint verifies
   (review, authorizations, widening review); (b) consistent for A1 (audit dir = common dir of the referenced
   records), NON-BLOCKING edge in N-3; (c) consistent: a non-timestamp has no version in force (probe S5); (d)
   consistent: the two orders give the same outcome in every case, only the message differs; (e) consistent with
   the rules (probe P3) but in conflict with sec. 15 item 0a (DESIGN-ISSUE D-1).
8. **Scope.** Diff 4fb2c1ee..a4566dc2: 58 files, all added, all under `tools/ledger_coverage*` and
   `verification/audits/foundations/ledger-coverage-tool-20261123/`; nothing pre-existing modified. Added lines: no
   local paths, e-mails, model ids or "workspace" (`.claude/settings.json` occurs only as a repository path in
   records). Z9h control unchanged (byte-identical function at 015edf3f and a4566dc2). origin/research/a1exit-deletion-20261121
   = 4c79be642ca631573f06b444903be75ec4f5e2b6.

## 3. Mutation results (`scripts/mutants.py`, `scripts/mutate.py`, `mut/results.json`, `mut/results-M31-M53.json`)

Each mutant: a copy of `tools/ledger_coverage*` at a4566dc2 with one replacement, run through self-test, the
synthetic fixture and the conformance controls (the A1 controls exercise no admission path and were not rerun per
mutant). Base: 87 self-test + 231 other controls, as expected.

Killed (42): M01 (TR55/66/67), M04 (TR57/68), M05 (TR59), M08 K1 (R5-K1), M09 (TR66), M10 (TR70), M11 (TR69), M12
(TR55/61/66), M14 (TR68), M15 (TR44/62/68), M16, M17 (TR63), M18 (TR68), M19 (TR23), M21 F1 (R3-F1, LN9-12, ...),
M22, M23 B1 (R4-B1-GUARDS), M25-M28 K2 (R5-K2, R3-F1, R4-B1/B2, TR47, R6-EV), M29, M30 (R6-EV), M36, M40 (LN9/12),
M37, M39 (TR65), M41 (TR65, LN9, LN11), M42, M43 (LN3), M44 (LN1/8), M45 (LN4/9/12), M46 (LN6), M47 (LN7), M49, M50
(LN12), M51 (LN8), M52 cycle (hangs; timeout), M54 F2 (R3-F2), M55 F3 (R3-F3), M56 result hash (R4-N2), M57 K7
(TR28/52/53).

Survived, equivalent or redundant (6): M07 (designation author = governing owner: implied by owner comment + no owner
change since), M38 and M58 (authorization owner = governing/configuration owner: implied likewise), M24 (no merge
record: the merge-commit check refuses the same change), M53 (B3: entries without id are refused before
`item_ids`), M13 (removes the engine's extra reconciliation refusal, see N-1).

Survived, requirement weakened (11), each separated from the engine by a probe (`scripts/probe_survivors.py`,
`scripts/survivor_check.py`, `out/probe-survivors-*`): the engine refuses, the mutant admits.

| Id | Mutant | Requirement weakened | Probe | Missing control |
|---|---|---|---|---|
| G-1 | M06 | a comment created when no version of `A` is in force is not an owner comment (designation) | S1 | designation created before the first `A` merged |
| G-2 | M02 | snapshot records the blob of `A` in force at each comment (hunk 10) | code reading | a check of `owner_comments[].authority_in_force_sha256` |
| G-3 | M03, M31, M32 | approvals of a ledger change are owner comments at creation (pre-`A`); each approval form isolated | S2 | ledger approval(s) created before the first `A`; TR57/58-style with one defective approval at a time |
| G-4 | M33 | "in force": merge time strictly before `t` | S3 | comment created in the same second as an owner change merge (realistic at 1 s resolution) |
| G-5 | M35 | authorization `time` must be a host time (choice c) | S5 | authorization with `time` "t0" in the chain |
| G-6 | M48 | a `record_id` reused off the `supersedes` chain is record-invalid (sec. 6.3, S4) | S4 | the writer's `probe_reuse.py` as a control |
| G-7 | M34 | ledger change governed by `A` merged strictly before it | (as G-4) | same-second `A` and ledger merges |
| G-8 | M20 | an `A` change needs an independent review record (TR26 tests review and approval missing together) | code reading | `A` change with approval but no review |
| G-9 | M59 | point 3: unreadable edit status refuses | code reading | comment without edit status |

Classification. The review brief makes a surviving mutant that weakens a v5.5.8 requirement BLOCKING; the owner's
stopping rule blocks only a demonstrated violation by the subject. For G-1 to G-9 the subject's engine is correct
(probes) and every control S13 lists behaves; what is missing is a control. I report them as **BLOCKING under the
brief's item-3 rule, control gaps only (no engine defect)**; smallest fix: add the probes above as controls. If the
owner's stopping rule is applied alone they are NON-BLOCKING. The verdict is REJECT on B-1 either way.

## 4. DESIGN-ISSUE

**D-1.** Sec. 15 item 0a: "The empty freeze ledger lands with it [`A`]." Under "Owner at creation" (a comment
created when no version is in force is not an owner comment) and "the version in force at its merge" (strictly
before), a ledger merged in the same merge as the first `A` can never be approved (probe P3: refused, "merged when
no verified authority record was in force"). The writer follows the rules (choice e). The open-points wording
should say the ledger lands after `A`, in its own merge.

## 5. NON-BLOCKING

- **N-1 (extra refusal, fail-closed).** A recorded ledger event naming a comment present in the thread that was not
  an owner comment at creation refuses the admission (`authority.py`, "was not an owner comment at its creation").
  The design treats such an event as not counting, not as a conflict. Probe P1b [sim]: TR66's first case (F admitted
  by 5555, 5555's earlier withdrawal not processed); a landing appends the withdrawal it observed; the next admission
  of the same F refuses. No safety impact.
- **N-2.** The snapshot's `events` include unprocessed forms (`owner_comment: false`); once B-1 is fixed, N-1 applies
  to committed snapshots as well.
- **N-3 (choice b).** The audit directory is inferred as the deepest directory holding every referenced record; a
  configuration referencing records in only one subdirectory narrows the fork domain, and the plan's record
  directory is taken as the configuration's directory rather than `dirname(pin_table_path)`. The design does not
  say how the tool identifies the audit directory. Correct for A1.
- **N-4 (choice a).** Kind-specific field checks of a predecessor rule file (sec. 6.2 `lint_rule`) are not run.
  Consistent with the design's enumeration; noted for the owner.

## 6. Files

`scripts/repro.sh` (steps 1-7), `scripts/compare.py` -> `out/compare.json`; `out/full/` (my logs, JSON results);
`scripts/mutants.py`, `scripts/mutate.py` -> `mut/results*.json`, `mut/base.json`; `scripts/probes.py`
(P1, P1b, P2, P3) -> `out/probes-a4566dc2/`; `scripts/probe_snapshot.py` (B-1) -> `out/probe-snapshot-*`;
`scripts/probe_survivors.py`, `scripts/survivor_check.py` -> `out/probe-survivors-*`;
`out/conformance-controls-engine-015edf3f.json` (a4566dc2 adapters with the 015edf3f engine: `git archive 015edf3f
tools/ledger_coverage/engine tools/ledger_coverage.py` over a copy of the a4566dc2 tools).
