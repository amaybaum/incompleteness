# Confirming check: Q-C2-1 r11b (ARP-2-QC21)

**Reviewer.** The same independent model reviewer, 2026-11-09. Read-only. Inputs:
- `preregistration.draft.md` `f0436d4a719fb0e570a40fab32726fb603376e6a3c317b41f1881e74ea3612a6`;
- `PLAN.md` `e304549959cbab32a24e7db70c27a2af4c14df98b553d2271a9c4e7c7dce9795`;
- `DESIGN-DS.md` unchanged at `f0cb090e…`.

All three were verified and diffed against `r11a/`.

## Verdict: **ACCEPT**

The diff against r11a contains only:
- the r11b status line;
- C.3's statement that the GT-ACT branch is not a recorded branch;
- C.7's GT-ACT row moved to a dedicated disposable branch created from `D`;
- PLAN §17.

**R11a-B1 is fixed.** `D` (`fd539e15`) predates the splice, so the GT-ACT branch carries neither the pinned checker blob
nor the frozen job or step names. Its push runs are not checker-bearing, so neither rule (d) nor the closing violation
clause applies to them. The ref-move rule reads recorded branches only, so GT-ACT's own `force_push` entry cannot VOID
the round. The test still shows that the activity read sees a force-push, and records the entry in `gate-tests.json`.

No blocking finding remains from the reviews r6 through r11b.

## What remains before `F` (final list)

1. **The sketch reviews.** The verdicts of the independent reviews of Lemma P and of the cone argument, quoted in
   *Sketches under independent review*. A review still pending at `F` counts as failed, and its withholding row
   applies.
2. **The `PENDING` fields:**
   - the record-directory date and the governed-paths digest;
   - the REACHABLE path and blob on `main`;
   - the benchmark;
   - the design-run anchors and records;
   - the stress-fixture generator and seeds;
   - `P_max`, `B_max` and `W_max`;
   - the timeout-test term count;
   - `T0`;
   - the pins of `design-run.json`, `stress.json` and `gate-tests.json`;
   - the activity API's documented retention.
3. **D9(a).** Land REACHABLE r3 and DESIGN-DS as separate paper records on `main` before `D`, pinned by blob. Re-confirm
   `D`.
4. **The scripts.** Write `qc21_check.py` and `controls.py` with their self-tests. Run the design run (C.7 6) and the
   confirmation run (6′). Run C.7's gate tests GT-B3, GT-REF, GT-RERUN, GT-PLAIN, GT-PR, GT-LIST, and GT-ACT on its
   non-recorded branch, each owner-authorized where it dispatches, re-runs or force-pushes.
5. **The owner's freeze commitments**, recorded under precondition 2:
   - no workflow run, run log or artifact is deleted until `Q`;
   - the designation of `E` ratifies the run list and every approval entry, by `order.json`'s sha256;
   - no force-move or deletion of a recorded branch without recorded authorization;
   - after `Q`, no push to, deletion of or re-creation of the round branch without recorded authorization.
6. **The round PR.** Open it from `D`, filling every `PENDING` field. Control P must find none unbackticked.
   Precondition 5's independent review of the control plane must then be recorded with no open blocking finding. It
   covers the filled fields and the scripts' blobs; the text reviewed here is unchanged.
7. **The freeze.** The `F` dispatch with its approval entry and green result, then the designation request to the
   owner.
