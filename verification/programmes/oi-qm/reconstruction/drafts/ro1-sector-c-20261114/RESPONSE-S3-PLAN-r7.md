# Response to the focused review of S3-PLAN-r7

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-S3-PLAN-r7.md` (ACCEPT WITH CHANGES at
`f3cf7994`). The changes are in `S3-PLAN-r8.md`, and nothing else changes. `S3-PLAN-r7.md` is left
unchanged (SHA-256 `bc07875fbc5dfa7f0ea269df90986d19d406e5ef9299a7f89023c2c88b2c61b6`).

Each finding was checked at source on `main`. No finding was found to be wrong.

## Required changes

| Finding | Check at source | Disposition | Where in r8 |
|---|---|---|---|
| **R10(a).** S-L3's verification is only MR★'s report | Confirmed. `MR-star.md`:1297–1300: "The independent review of `fc68d333` returned REVISE … It verified S-L1, S-L3, S-L4 …". `stage1-log.json`:773 calls it "relayed by the coordinator". O-OBSMU `ANALYSIS.md`:485–489: "Under §A.46 item 7, though, that report does not count as verification here, so S-L4 is used only as a named premise" | **Applied.** S-L3 enters as a **named premise**, with the report quoted, the relay noted and the O-OBSMU ruling cited. It is not a sourced disproof and is not upgraded | §8.4, check 1 (miss case) |
| **R10(b).** S-L3's full scope; re-check; conditional count | Confirmed. S-L2 (`MR-star.md`:511–513): "The available transformations of the joint state are the time shifts `φ^n`, `n` within the budget. Observer-side choices change only which region and tick are read". S-L3's proof uses injectivity of `a` with a nonempty neighbour relation, and S-C1(a) (:517–530) | **Applied.** The full scope is stated: K1; MR-1's frozen availability standard (S-L2); the budget below recurrence, with the global wait beyond it; injectivity of `a`; S-C1(a). The miss case is retitled "erasure disproved on K1, conditional on the S-L3 premise", and its conclusion is an [A-inf] conditional on the premise. It does not count toward (a′) until S-L3 is re-checked under the U1 criterion *and* independently verified, and until then it is reported as conditional on a named premise. SNR-1's *disproved* category now says that a reported-only disproof enters as a named premise and counts only after verification and re-check. (a′) carries the same condition, and the U4 row adds the S-L3 re-check | §8.4, check 1; §8.6 (SNR-1, (a′)); §9 (U4) |
| **R11.** The gating sentence omits (b′) | Confirmed | **Applied.** It now names all three: an MR-1 stage-2 authorization, for (e′); #866's σ12 screen, for (c′); and a result on the observer-level lift, for (b′) (OB-a1; #866, #1169) | §8.6 |

## Consistency sweep of S-L3 citations

| Site | Disposition |
|---|---|
| §2.1, MR-1 stage-1 row (quotation of #1023 c.6555169983) | Left verbatim: it is a quotation |
| §8.1, stage-1 GAP bullet (quotation) | Left verbatim: it is a quotation |
| §8.2, class (i) example | Now marks S-L5 and S-L3 as named premises, records on `main` not verified there (§A.46 item 7) |
| §8.3, Point 2 | Marks S-L3 as a named premise within its scope, pointing to §8.4 check 1 |
| §8.4, check 1, miss case | Rewritten per R10 |
| §8.6, SNR-1 *disproved* | Adds the named-premise rule, with S-L3 as its instance |
| §8.6, (a′) | Counts the case only after re-check and independent verification |
| §9, U4 row | Adds "re-check S-L3 under the U1 criterion, as a named premise" |
| Revision notes for r7 and earlier | Historical, and left as written, except the r6 note (below) |

## Optional items

| Item | Disposition | Where in r8 |
|---|---|---|
| CC5 note on conditional fringes | **Applied.** Conditional-fringe recovery is also reproduced by CC5 (M-2), so it falls under (e′) and K-6/M-4, not under S-L3 | §8.4, check 1 |
| r6-note wording | **Applied.** The r6 note now reads "The rule (§8.6), named NC-1 in r6 and renamed SNR-1 in r7", and "Where the rule is applied" | Header |
