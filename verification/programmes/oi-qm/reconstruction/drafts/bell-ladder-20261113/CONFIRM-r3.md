# Focused confirmation: Bell ladder r3 (#868, #1273)

The reviewer is the author of REVIEW-r1 and CONFIRM-r2. This check is read-only and by hand.

**Object.** I fetched `research/bell-ladder-868-20261113` by name, at head
`c4781c9378f4f6340554b15418f76399f5462711`. Its single parent is `b8096c79`.

- The diff from `b8096c79` adds BELL-LADDER-r3.md, NOTES-r3.md, RESPONSE-r2.md and CONFIRM-r2.md.
- It also modifies OBJECTS.md.
- No earlier file is touched: r1, r2, REVIEW-r1 and RESPONSE-r1 are unchanged.

## Verdict: ACCEPT

**(1) R1–R3 are applied as specified.**
- R1 is at NOTES-r3:61–62.
- R2 is at NOTES-r3:95–98.
- R3 is at BELL-LADDER-r3:273–274: the status row of Proposition AL is updated, and the new row "Record convention
  for (AL4)" follows it.

**(2) N1–N4 are applied correctly.**
- N1 is at NOTES-r3:34–35.
- N3 is at BELL-LADDER-r3:300.
- N4 is in the stage-6 row, BELL-LADDER-r3:103.
- N2 is handled correctly:
  - RESPONSE-r1 is left byte-unchanged as a committed record.
  - RESPONSE-r2 corrects it forward: the cited file is `REVIEW-r1.md`, and "nothing committed" described the time
    of writing.
  - NOTES-r3:10–11 states that the coordinator committed r2 at `b8096c79`.

**(3) r2→r3 differs only by those items and the revision or title lines.**
- In BELL-LADDER, `diff` shows four hunks: the status line (3–5), stage 6, the §5 rows and the QH row.
- In NOTES, `diff` shows the title and lines 3–4, line 10, N1, R1 and R2.
- Nothing else changed. Q4, which the new §5 row cites, is still present at NOTES-r3:102.

**(4) CONFIRM-r2.md is byte-identical to my working copy (`cmp`).**
All ten rows of OBJECTS.md match the sha256 of the committed blobs, with no substitutions. The four new rows are:

| File | sha256 (prefix) |
|---|---|
| CONFIRM-r2 | `c68dd910` |
| BELL-LADDER-r3 | `6e7708ce` |
| NOTES-r3 | `831554fb` |
| RESPONSE-r2 | `e02e0928` |

The six earlier rows are unchanged and still match.

**(5) No new overclaim.**
- Every change narrows a claim or adds a condition.
- The new §5 row restates the scoped **Histories** finding at its scope.
- No verdict, classification or proof changed.
