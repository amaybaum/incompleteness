# NOTES-BG-r5: working log for G3 unit 2(b), revision 5

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree.
  - Head at reading time: `905b68cc7af2b183c8230fe4f5ccc3b9a7390768`.
  - `297ee246` adds r4 (`G3-UNIT2B-BG-r4.md`, `NOTES-BG-r4.md`, `RESPONSE-BG-r3.md`). These are
    byte-identical to the writer's r4 (`cmp`).
  - `905b68cc` adds `CONFIRM-BG-r4.md`, and nothing else.
- **Commit state, as observed when this file was written.**
  - r4 is committed at `297ee246` by the coordinator.
  - r5 is not committed.
  - The writer does not commit, push or post. The branch history records commits.
- **Authority.** #873 c.6865179466, QU5. The coordinator's request for r5 is a session message, not an
  owner record.

## 2. Scope of r5

r5 applies CONFIRM-BG-r4 DF-1 to DF-4 and nothing else, using the review's replacement text wherever the
review gives one.

The only other change is bookkeeping: the title, and one revision-history line naming r5 and its review.
RESPONSE-BG-r4 lists every hunk.

## 3. K3's reading (CONFIRM-BG-r4 DF-4 item 4)

NOTES-BG-r4 (N4:49–53) paraphrased K3 loosely. The correct reading is:

> K3 fails a carve for which no difference relevant to grounding is stated; each carve stated so far is
> of that kind.

A class that covers `ρ_Z`, such as partition-definedness, is not an instance of F4-c, because F4-c
requires the witness's term to be grounding. Such a class could meet F4-c's form only if `ρ_Z` were
removed from it ad hoc, and that removal fails K3.

## 4. Checks

- No computation, script or build was run apart from the three permitted checks.
- **The r4→r5 diff.** `diff G3-UNIT2B-BG-r4.md G3-UNIT2B-BG-r5.md` gives 11 hunks. r5 has 902 lines.
- **Barred-string scan of the three r5 files.** No hits.

| Check (worktree at `905b68cc`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. The worktree stayed clean.

## 5. Off-`main` references (§A.42 item 8)

These are as in NOTES-BG-r4 §6, with the following additions:

| Reference | Claim it is attached to | Class |
|---|---|---|
| `CONFIRM-BG-r4.md` at `905b68cc` (branch) | DF-1 to DF-4 and their replacement text | support off `main`; lands with #1275 |
| `G3-UNIT2B-BG-r4.md` at `297ee246` (branch) | the base of r5 | support off `main`; lands with #1275 |
