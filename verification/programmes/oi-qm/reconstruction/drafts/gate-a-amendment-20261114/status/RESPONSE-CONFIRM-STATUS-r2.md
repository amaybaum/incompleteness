# Response to CONFIRM-STATUS-r2.md

Dispositions of the confirmation of `STATUS-r2.md` at `120ecb97` (ACCEPT WITH CHANGES; RC-1 to RC-7,
optional O-1 to O-5), and of the coordinator's instructions for r3 (the later owner record and the
accountable-Issue mapping). `STATUS-r1.md` and `STATUS-r2.md` are unchanged; `STATUS-r3.md` carries
the changes. Read-only and paper-only: `git` inspection of the record checkout and public GitHub
API reads, 2026-11-14 about 12:48Z–12:52Z. At 12:51Z the branch head was `b3cc7182`, one commit
after the confirmed head; its `status/CONFIRM-STATUS-r2.md` (blob `ff687f78`) is the file answered
here.

| Change | Checked at source | Disposition | Where in r3 |
| --- | --- | --- | --- |
| RC-1, header | `status/` files at `120ecb97` and `b3cc7182` | applied, with the confirmation's file now named under `status/` (it is on the branch at `b3cc7182`) and r3's read times added | header |
| RC-2, record pin | `git log` at `120ecb97`; PR API and compare `c3b5f37a...b3cc7182` (23 files, 4701 added lines, all in the record directory) | applied in modified form: the content head `927915e9` and the later commits are described separately, and the branch head is `b3cc7182`, which postdates the confirmation | §0 |
| RC-3, review files as support off `main` | file list at `b3cc7182` | applied, naming all three `status/` review files on the branch | §3, off-`main` table |
| RC-4, count of modified dispositions | `RESPONSE-STATUS-r1.md` (F1, F15 modified) | applied: "two in modified form, F1 and F15" | §4, review row |
| RC-5, exact-head and CI rows | runs for `120ecb97` (43595811887: `pull_request`, attempt 1, 12:38:22Z–12:46:50Z, 26 success, 1 skipped, all check runs `head_sha` `120ecb97`) and for `b3cc7182` (43596656232, in progress at 12:51Z); commits `b1355802` (parents `dfeec843`, `120ecb97`) and `1d9ec199` (parents `dfeec843`, `b3cc7182`) | applied, with the test-merge commit described as a GitHub-generated commit, not the head; the run at the current head `b3cc7182` is recorded as the confirmation instructs for a later push | §4, two rows |
| RC-6, ruleset row and §6 item 4 | ruleset 21725642: `guardrail`, active, `~DEFAULT_BRANCH`; rules `deletion`, `non_fast_forward`, `required_status_checks` (three contexts, strict), `pull_request` (`required_approving_review_count` 0, `require_code_owner_review` true, merge/squash/rebase); `bypass_actors`: one, `RepositoryRole` id 5, mode `pull_request`; no `CODEOWNERS` path anywhere in the tree at `dfeec843` | applied: "not visible through the public API" dropped; zero approving reviews stated; the §A.46 item 8 reviews stated as policy, not ruleset rules; "7 ahead" for the current head. §6 item 4 kept with "whether r3 needs a confirmation review", since r3 is unreviewed | §4, draft/base row; §3, item 8 table; §6 item 4 |
| RC-7, later owner record | #914 comment 6877420015 (`amaybaum`, OWNER, 2026-11-14T12:42:16Z) and #1169 comment 6877420524 (12:42:18Z), read in full; no later comment on #914, #1169, #868, #1060 or #1217 at 12:50Z | applied, with the summary sentence on PR #1289 also quoted and the consequence stated: reconciliation of r4 with the four-part target is a prerequisite to adoption, and preservation does not perform it | §2; §3, off-`main` table; §6 item 1 |
| Accountable-Issue mapping (coordinator, owner-approved in session) | bodies of #868, #1060, #1217 in full; #1169 body (assumed setting, objective, routing to #866 and #913); #914 decision 4 | applied: the Bell row split into B⇐ (#868) and B⇒ (#1060), the kinematics row under #1169 with #914 as index, and a separate related row for #1217; each with the missing proof and its remediation, scopes quoted from the bodies, and the caveats stated. The approval itself is not on GitHub, so it is listed as support off `main` and as §6 item 8 | §1 obligations table; §3; §6 item 8 |
| §A.46 item 8 condition restated | §A.46 item 4 and item 8 at `dfeec843` | applied: partly met; not met for exclusion of supraquantum correlations other than the Tsirelson bound (no accountable Issue) and for the unrecorded approval of the mapping | §3, item 8 table |
| O-1 | obligations table | applied | §1 status table |
| O-2 | §A.40 | applied | §4, CI row |
| O-3 | #1169 comment 6876591512, section "What this does and does not change" | applied | §4 |
| O-4 | #914 comment 6877420015, item 4 | applied | §1, gravity row |
| O-5 | (the mapping) | applied with the mapping | §1 obligations table |

No change is declined. `STATUS-r3.md` is 247 lines; it exceeds the earlier length aim because of
the split Bell rows, the #1217 row and the later owner record.
