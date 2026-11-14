# Response to REVIEW-QUEUE-r3

**UNREVIEWED.** This file gives the disposition of each finding of `REVIEW-QUEUE-r3.md` (ACCEPT WITH
CHANGES) and of the coordinator's five items, as applied in `QUEUE-PROPOSAL-r4.md`, a minimal revision.
`QUEUE-PROPOSAL-r3.md` is left unchanged.

The work was read-only and paper-only. Nothing was committed, pushed or posted, and no wording, tier,
readiness, authorization or queue item changed. The sources read:
- PRs #1253, #1261 and #1262, through the API;
- `main` at `dfeec843`, through `git show`, `git diff` of `fba459cb`, `git log` and `git blame`.

## Should-fix

**S1 (coordinator item 1). #1244's vehicles have merged.** Applied.

**The merges, as checked.** Both are ancestors of `dfeec843`:
- #1261 merged at 2026-11-12T18:40:51Z, as `0ebf90db`;
- #1262 merged at 2026-11-12T19:18:05Z, as `fba459cb`.

r4 §A.3 #1244 now records both merges, quoting each PR body. The body status note on #1244 predates
both merges. r4 records that as a sourced fact the owner may note under §A.45 rule 3's maintenance
clause.

**Each item, at `main`:**

| Item | Status on `main` | r4 |
|---|---|---|
| F-17 at :179 | **Not corrected.** #1261 removed only A/4 from the row. :179 still places Cabibbo, Koide and the dark-sector phenomenology at "Level G3 × Level D", against :191–192 ("Level D × Levels G1–G2") | Kept, as a new unit on #1244 |
| G-2 | **Unchanged.** GR:12 still says the counting is "itself unconditional". #1262 reported "(b) Unconditional mode count or geometry: 0. No conditions were added", and its commit `64aeb44c` says "Unconditional counting statements are unchanged (no class-(b) sites)". The owner's rule was applied | Kept, only as owner question 4, on whether to revisit the applied rule. No unit is proposed unless the owner does |
| T-4 | **Partly addressed.** Structure:453 was last changed by `6cf861e0` ("A/4 conditions point to GR §8.5(b) at the three #1253 sites"), part of #1253, merged as `609bd663` before the audit read it. It already carries the calibration's conditions. What remains is the form of the claim: a bound on "any horizon entropy", where an equality is established and the GSL is open | Kept for the remaining part only, as a new unit |
| G-30 | GR:615 is unchanged | Kept, as a new unit under item 1 |

**Owner questions and §1.6:**
- **Question 3** now asks whether to open a new unit for F-17 at :179.
- **Question 4** says that the merged sweep applied the owner's rule and left GR:12 as it is, and asks
  whether to revisit that rule. It also carries the stale-note fact.
- **§1.6.** The sentence about "one authorized draft on a line listed here" is removed.

**S2 (coordinator item 2). RO-2's wording.** Applied, and disclosed.

r4 restores r2's wording: "its verdict may be the residual class (C)".

**Disclosure.** The change in r3 was substantive and unintended:
- **What it did.** r3 reverted, without any decision to do so, to a sentence that r2's assembly had
  already replaced. r3's Part 3 was built from a working copy of r2's Part 3 taken before that
  replacement was applied.
- **Why it was missed.** `RESPONSE-QUEUE-r2.md` did not list it, because it was not a deliberate edit.
- **What was checked.** A diff of r3's Part 3 against r2 shows no other unintended reversion. The only
  other differences are the grouping edits that `RESPONSE-QUEUE-r2.md` lists.

**S3 (coordinator item 3). RO-3's readiness.** Applied. RO-3 no longer borrows #1055's readiness.
- **§3.1 table.** RO-3's cell reads "readiness undetermined (no row records the inventory's
  readiness)".
- **"What the evidence shows".** The sentence "RO-3 now sits at a ready Issue (#1055), as RO-2 does" is
  replaced by: "#1055's readiness is for its recorded question; no row records the readiness of the
  inventory".
- **RO-3's "Recorded planning".** It qualifies #1055's "ready" in the same way.
- **The ranking.** The reason is kept: RO-3 ranks below RO-2 because its scope is not frozen, and below
  RO-1 on reach.

## Nits

- **N1. D1 and CON-04.** Applied. r4 §A.1 and the MC-1 row say that #1028 comment 6628572816 lists
  ch19:20 under CON-04. CON-04 concerns a cosmological-constant "dissolution" stated without its G3
  condition, which is a different defect from D1. The rows say it is "the same line, under CON-04", so
  that one unit can take both.
- **N2 (coordinator item 4). #1238 is a partial fit.** Applied.
  - S-1 and S-2 stay on #1238, marked as a partial fit: their GR half is outside the "QM is / is derived"
    scope. The proposal widens #1238's scope to that half for these two passages, so that one unit
    corrects each sentence.
  - S-17 ("every concept") and K-5 ("the fundamental laws") move to #1028, under MC-3 Substratum and
    MC-3 book.
  - §A.1 and owner question 2 are updated to match.
- **N3. Items split across two Issues.** Applied. r4 §A.0 states that F-3 and F-17 are split by clause,
  and that each part appears under exactly one Issue, with both placements named.
- **N4 (coordinator item 4). #1062 is a partial fit.** Applied, though the review found the existing
  wording adequate.
  - RO-9's row now carries an explicit "Partial fit" note: #1062 asks whether a native rule produces a
    persistent observer, and U-2 asks whether typical bijections admit one.
  - §A.4 and owner question 16 say the fit is partial.
  - U-2 is kept there as the closest scope found. No better home was found.

## Coordinator item 5

All findings are applied (S1–S3, N1–N4). Two small corrections were also made:
- **The section heading.** "How r3 is organized" is renamed "How this proposal is organized".
- **The off-`main` table.** It adds PRs #1253, #1261 and #1262, classified as support on `main`,
  because their merges are on `main`. It also adds `REVIEW-QUEUE-r3.md` and the earlier proposals as
  provenance.

No other text changed. `diff` of r3 against r4 shows only the edits listed here.
