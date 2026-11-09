# Confirming check: Q-C2-1 r11a (ARP-2-QC21)

**Reviewer.** The same independent model reviewer, 2026-11-09. Read-only. Inputs:
- `preregistration.draft.md` `0277db2d…`;
- `PLAN.md` `d443c1e3…`;
- `DESIGN-DS.md` unchanged at `f0cb090e…`.

All three were verified and diffed against `r11/`.

## Verdict: **REVISE (minor)**: one new blocker, in GT-ACT

**The diff is confined to R11-B1 and r11-N1 to N3.**
- **R11-B1 is fully fixed.**
  - The post-landing sentence now reads "prevents them for the frozen splice, except through three routes", and names
    them: (a) a fast-forward push deleting the receipt; (b) deletion and re-creation; (c) a force-move.
  - The limits bullet is added, with the attestation-hygiene note.
  - Two three-way rows and one credential row are added, marked unobservable and not independent.
  - The owner's freeze commitment is extended: after `Q`, no push to, deletion of or re-creation of the round branch.
  - The invariant row is updated.
- **r11-N1.** UPR-BC moved to fixture mode, consistently in both lists.
- **r11-N2.** The re-wrap and the heading changes are logged in the Appendix C header.
- **The activity API's horizon** is correctly observed and marked `PENDING`. I confirmed read-only that the oldest
  `activity?direction=asc` entry is 2026-02-12T12:35:51Z, `branch_creation` of `refs/heads/main`, against the
  repository's `created_at` of 2026-02-12T12:34:11Z. The documented retention correctly stays `PENDING`.

**GT-ACT, however, is not sound as frozen (R11a-B1).**
- It force-pushes **the gate-test branch**.
- C.3 lists the gate-test branch among the recorded branches (line 1866) and makes any `force_push` or `branch_deletion`
  entry on a recorded branch a violation (line 1889).
- Every capture would therefore read GT-ACT's own entry and halt the round VOID.
- The force-push would also orphan gate-test commits that `order.json` lists.

**Fix.**
- Run GT-ACT on a dedicated disposable branch that is **not** a recorded branch. Create it from `D`, so that its tree
  carries neither the pinned checker blob nor the frozen job or step names. That way its push runs are not
  checker-bearing and cannot trip rule (d).
- Read `GET activity?ref=refs/heads/<that branch>` once and record the entry in `gate-tests.json`.
- The alternative is a frozen exception admitting exactly that activity entry by id. It is weaker, because it adds an
  exception to an absolute rule.

With that change, I expect ACCEPT. A one-line confirming check is enough.

**Remaining before `F`** (once R11a-B1 is applied):
1. **The two sketch reviews** (Lemma P and the cone argument). Their verdicts are quoted, or the withholding rows apply.
2. **The `PENDING` fields:**
   - the record-directory date and digest;
   - the REACHABLE path and blob;
   - the benchmark;
   - the design-run anchors and records, the stress seeds, the budgets and the timeout-test count;
   - `T0`;
   - the pins of `design-run.json`, `stress.json` and `gate-tests.json`;
   - the activity API's documented retention.
3. **D9(a).** Land REACHABLE r3 and DESIGN-DS as paper records before `D`.
4. **The scripts** (`qc21_check.py`, `controls.py`) with self-tests; the design run, the confirmation run and C.7's
   gate tests, GT-ACT on its non-recorded branch included.
5. **The owner's freeze commitments, recorded:**
   - no run, log or artifact deleted until `Q`;
   - ratification at `E`;
   - no force-move or deletion of recorded branches;
   - after `Q`, no push to, deletion of or re-creation of the round branch.
6. **The freeze.** The `F` dispatch with its approval entry, and the designation request.
