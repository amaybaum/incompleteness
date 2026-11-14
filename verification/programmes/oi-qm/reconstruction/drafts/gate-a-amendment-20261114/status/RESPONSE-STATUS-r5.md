# Response: what STATUS-r5.md changes from STATUS-r4.md

r5 applies only what follows from the owner's decisions of 2026-11-14 recorded in #1291 ("I adopt
all three") and the head and CI that have changed since r4 was written. `STATUS-r4.md` is
unchanged (byte-identical to `status/STATUS-r4.md` at `c7806483`). Read-only and paper-only: public
GitHub API reads and `git ls-remote`, 2026-11-14 about 13:01Z–13:03Z.

| Item | Checked at source | Change in r5 | Where |
| --- | --- | --- | --- |
| 1. #1291 as accountable Issue | #1291 body (opened from `amaybaum`, 13:00:58Z): question, planning block (tier, prerequisites, readiness "undetermined pending owner decision"; authorization "not authorized"), five requirements, status section; pointers #1060 comment 6877627984, #868 comment 6877628305, #914 comment 6877628626 (13:01:10Z–13:01:13Z) | B⇒ row names #1291 for the exclusion beyond the Tsirelson bound, quoting its question, planning block and fifth requirement; §2 quotes the decision, the three adopted items and the pointers; §3 lists them as quoted. The #1291 text says the decision leaves "Tier, Readiness and Authorization undetermined", while its block reads Authorization "not authorized"; r5 states both | §1; §2; §3 |
| 2. Conditions restated | §A.46 items 4 and 8 and §A.45 rule 6 at `dfeec843` | §A.46 item 8's own condition stated as met; §A.45 rule 6 stated as met for that obligation, since #1291 is opened and linked; the scientific obligation stated as open | §3, item 8 table |
| 3. S-J and exactness | §1 rows | kept as an open owner question, not assigned; §6 item 8 reduced to this point, since the Bell residual now has #1291 | §6 item 8 |
| 4. Owner's acceptance condition | #1291 body: "accept the Gate A landing-status note r4 only after its corrections are confirmed, an independent focused review returns ACCEPT on its exact head, and CI passes" | quoted as a gate and stated as not yet met; r5 notes that the condition names r4 and that r5 is a later revision, and §6 item 4 asks whether it applies to r5 | header; §4; §6 item 4 |
| 5. Head and CI | `git ls-remote origin` (branch `c7806483`, `main` `dfeec843`); PR API (9 commits, 28 files, 5513 added lines, `behind`, test-merge `0cdbe5c2`); runs 43596974572 at `acfdbd0f` (completed 13:01:49Z, 26 success, 1 skipped) and 43597480770 at `c7806483` (in progress at 13:02Z) | head pin and CI, exact-head and draft rows updated; the `c7806483` run is stated as in progress with no outcome given; the `acfdbd0f` run is stated as completed, as read | §0; §4 |
| Status line | — | header states r4 unreviewed and r5 applying the #1291 decisions, itself unreviewed; r3's review file now named under `status/`, where it is at `c7806483` | header; §3; §4 |

Nothing else in r4 is changed. `STATUS-r5.md` is 278 lines.
