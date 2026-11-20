# Confirmation of the delta-review fixes, PR #1274

**Verdict: ACCEPT.** All five applied findings are in place: R1, R2, R3, C1 and C2. Every line
reference resolves at `d1c25281`, and the copied text is unchanged. The new mathematics is
correct. No new error came in, and two optional wording nits remain.

## Object

- **Commit under check.** `d1c2528138722c215e9f8f762ee8ecf31b98484b` on
  `research/optc-1230-1232-20261113`. Its single parent is `bb80e4201c9917be0a668ced71dedcfe9c2f7aa6`,
  and it is the worktree HEAD.
- **Files changed.** Only three files in the record directory change: `CHANGES.md`,
  `NEW-RESULTS.md` and `STATUS.md`. Nothing in `review/` and nothing outside the directory changes.
- **How it was checked.** Read-only, by hand reasoning. Git was used only for diffs, blob ids,
  digests and line extraction.
- **Departures checked against the coordinator's list.** The scope line is now :302–311, the
  review-trail bullets are in chronological order, the commits-row wording is the coordinator's,
  and the blob table was measured at `d1c25281`.

## Each finding

### R1. Applied

The rows below are `STATUS.md` rows at `d1c25281`. The content column is read from `NEW-RESULTS.md`
at `d1c25281`.

| Row | Reference | Content at `d1c25281` |
|---|---|---|
| 3.1 (:138) | :298–300 and :313–327 | "Hand checks recorded" (:298–300); the [X] hand checks, from the heading (:313) to "−2/5." (:327) |
| 3.2 (:139) | :372–379 | from "Hand checks for the [X] tag and the Husimi bound" to "where it is 1/4 < 1/2" |
| 5 (:142) | :511–514 | the S4 hand check, ending "the PR box" |
| 6 (:143) | :605–609 | "Arithmetic of S7" through "= 1/2 for both b" |

Each range is bounded by blank lines (:301, :312, :328, :371, :380, :515, :604, :610).

### R2. Applied

- **Header (:3–6).** The claims are true:
  - `DEPENDENCIES.md` and `PROVENANCE.md` are unchanged since `d015131d`. So are the three review
    files present there: `REVIEW-r1.md`, `RESPONSE-r1.md` and `CONFIRM-r2.md`.
  - `NEW-RESULTS.md` differs from `d015131d` only in the §3.1 hunks. Those are the scope-line
    insertion after :300 and the "What it adds" sentence.
  - `CHANGES.md` differs only in the header clause and rows Δ30 and Δ31.
- **Blob table (:22–27).** It matches `d1c25281` exactly:
  - `NEW-RESULTS.md`: `b0e930ab5792eb8173e74e3feb18b9262b651109`, SHA-256 `e26cef1c…4ba943`, 641
    lines.
  - `CHANGES.md`: `220c189b0426316f8ce23c2a25e439a0d7d5714a`, SHA-256 `dcd0e147…77b1`, 74 lines.

### R3. Applied

:126 reads "see `NEW-RESULTS.md`:302–311 and :333–336 and `CHANGES.md` Δ30 and Δ31". Both ranges
are exact:

- :302–311 runs from "**Scope of the copied passages.**" to "(`review/NOTES-STATUS.md`, r3)."
- :333–336 is the narrowed "What it adds" sentence.

### C1. Applied, with no change to copied text

- **The scope line (:302–311).** It is the proposed text, re-wrapped.
- **Mathematics.** I re-checked it:
  - The zero-point extension does not span, and every Hadamard representative on it carries −1/2.
    So X5 holds on a non-spanning frame: "not confined to spanning frames" is correct.
  - "Nor does spanning make the test exclude every non-diagonal-preserving unitary" is correct.
    The witness is the cyclic rotation, whose frame matrix on the tetrahedral frame is a
    permutation.
  - Neither claim goes beyond G1.
- **Copied text.** :1–300 are identical to `d015131d`. The only insertion hunk adds lines and
  deletes none.
- **Δ31 (`CHANGES.md`:53).**
  - It names the X5 sentence (S:102), which matches CONFIRM-CORR322 §4's label.
  - It cites :302–311, which is correct.
  - The CHANGES header clause "Δ31 adds a scope line for copied text and changes none" still holds.
- **The STATUS scope paragraph.** :149 cites :333–336. :153–155 names "Finding, X5 sentence and
  closing paragraph" and :302–311. Both are correct.

### C2. Applied

- **Δ30 reason cell.** It now names `review/CONFIRM-CORR322.md` finding 1 and `review/NOTES-STATUS.md`
  r3 for the spanning clause. Both sources contain the cyclic-rotation argument.
- **Review-trail bullets (:38–44).** The commit ids match the commits that added each file:

  | File | Added at |
  |---|---|
  | `CONFIRM-STATUS.md` | `f17020af` |
  | `RESPONSE-STATUS.md` | `4cb2618d` |
  | `CONFIRM-STATUS-r2.md` | `040d929e` |
  | `RESPONSE-CORR322.md` | `0b68c9e1` |
  | `CONFIRM-CORR322.md` | `bb80e420`, blob `9375d5e6`, unchanged at `d1c25281` |

  Review 5900794367 is listed as posted under `amaybaum`, 2026-11-14T02:17:05Z, at `0b68c9e1`,
  REVISE. That matches the review record.
- **Dependencies table (:177–181).** It now lists:
  - #1274 c.6865575359 and #1169 c.6872005186;
  - reviews 5895564670 and 5900794367;
  - commits `f4c300bc` to `bb80e420`.

## New-error scan

- **References into `NEW-RESULTS.md`.** Every one in `STATUS.md` resolves at `d1c25281`: :3–15, :9,
  :11–15, :33–36, :215–224, :298–300, :302–311, :313–327, :333–336, :372–379, :511–514 and
  :605–609. So does `CHANGES.md` Δ31 (:302–311).
- **Owner and review ids.** c.6865575359, c.6872005186, 5895564670 and 5900794367 are unchanged and
  accurate.
- **Register.** The new text is neutral and technical. It has no self-narration, no caps emphasis
  and no claim beyond T5(c)/G1.

## Nits (optional; neither affects the verdict)

- **N3. The commits row claims more sources than it has.** The Dependencies commits row (:179) says
  the commits are named "in Δ30 and Δ31", but neither row names a commit id. Replace "and in Δ30
  and Δ31" with "and in this note's review trail".
- **N4. "Nature of the reviews" (:46–49) names only 5895564670 as posted under the owner's account.**
  For parity with the extended trail, replace "review 5895564670 is a model review posted under the
  owner's account" with "reviews 5895564670 and 5900794367 are model reviews posted under the
  owner's account".

The blob table at :22–27 describes `d1c25281`. Any later edit to `NEW-RESULTS.md` or `CHANGES.md`
requires re-measuring it. N3 and N4 touch only `STATUS.md`, so they do not.
