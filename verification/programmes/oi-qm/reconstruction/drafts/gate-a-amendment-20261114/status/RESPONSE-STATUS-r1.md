# Response to REVIEW-STATUS-r1.md

Dispositions of the review of `STATUS-r1.md` (ACCEPT WITH CHANGES; F1–F4 medium, F5–F16 low, none
blocking). Each finding was checked at its source before it was applied; `STATUS-r1.md` is
unchanged, and `STATUS-r2.md` carries the changes. Read-only and paper-only: `git` inspection of
the record checkout and public GitHub API reads, 2026-11-14 about 12:25Z–12:35Z. At 12:33Z the
branch head was still `927915e9`, `main` was still `dfeec843`, PR #1289 had no comments or reviews,
and #1169 and #914 had no comment after 11:28:26Z.

| Finding | Checked at source | Disposition | Where in r2 |
| --- | --- | --- | --- |
| F1 (medium), CI row names the tested merge commit | `verify.yml` at `927915e9`: triggers `pull_request`, `push` for `main` only, `workflow_dispatch`; job `Numerical probes / A42 exclusion` has `if: github.event_name == 'workflow_dispatch'`; compare `927915e9...29dd4cda`: `AGENTS.md` only; run record carries `head_sha` only | applied in modified form: the review's text, except that "none is authorized by item 5 of #1169 comment 6876591512" becomes "a dispatch needs its own owner authorization (§A.43 item 4)", since item 5 names "CI" without saying whether a dispatch is included | §4, CI row |
| F2 (medium), up-to-date rule and merge methods | rules API for `main` (ruleset 21725642): `strict_required_status_checks_policy: true`, contexts `Lean kernel check`, `Mathlib bridge`, `Numerical probes`; `allowed_merge_methods` merge, squash, rebase; also `require_code_owner_review: true`, and no `CODEOWNERS` file at `dfeec843` | applied, with one added fact (the code-owner setting and the absent `CODEOWNERS` file) | §3 review-heads row; §4 draft/base row; §6 item 5 |
| F3 (medium), #1169 comment 6703342848 | comment text (`amaybaum`, 2026-11-07T06:25:11Z) contains both quoted phrases verbatim and "Deterministic hidden dynamics and indirect recovery of hidden information are admissible."; r4:54–56, r4:144, r4:430–433, `OWNER-QUESTIONS-r4.md`:44–47 | applied: split into a support row quoting the comment and a provenance row for its trace §2 use; the addition on r4:54's classification made to the owner-records row | §3, off-`main` table |
| F4 (medium), item 8 condition shown as met | §A.46 items 4 and 8 at `dfeec843`; §A.45 rule 6; r1 Bell and kinematics rows | applied: three columns added to the verification-status table; the item 8 row states the condition is not met for the Bell clause and the kinematics input and what would close it; §6 item 8 added | §1 status table; §3 item 8 table; §6 item 8 |
| F5 (low), review self-descriptions | `REVIEW-r1.md`:3, `CONFIRM-r2.md`:3 (non-author, paper-only only); `CONFIRM-r3.md`:3–5, `CONFIRM-r4.md`:3–5; `README.md`:56 | applied | §1, after the review table |
| F6 (low), contents of `927915e9` | `git diff eb515150 927915e9`: `README.md`:17 changed ("The current text" to "The final text of the amendment cycle"), not requested by `CONFIRM-r4.md`:194–206 | applied | §1 table, CONFIRM-r4 row; sentence after the table |
| F7 (low), `ae2de57a` and `cea26912` | `git diff 65b0a929 ae2de57a -- README.md` removes the owner-confirmation sentence; `cea26912` as described | applied | §1 table, CONFIRM-r3 row |
| F8 (low), superseded necessity statements | r3:213, :272–273, :339–340, :378, :381; r2:209, :255, :258, :327, :363; `CONFIRM-r2.md`:58; `CONFIRM-r3.md` §B.3 | applied as a new row classed "superseded", not "known-invalid", since the statements hold under their stated restriction | §1 status table |
| F9 (low), r4 lines presenting the questions as open | r4:224, :283–284, :308–309, :382–383, :410; `OWNER-QUESTIONS-r4.md`:2 | applied | §5 |
| F10 (low), answers 1 and 3 against r4 | r4:229, :247–248, :422–425, :193; answer texts | applied | §2, relation paragraph |
| F11 (low), pointer comment | #914 comment 6876592679 text | applied | §2 |
| F12 (low), adoption reads as a rule | item 5 of #1169 comment 6876591512 | applied, with the time of the latest re-check added | §2 |
| F13 (low), accepted head | `oi-qm-ext-1/two-mode-drive.md`:3 at `dfeec843` ("The accepted Gate A contract is `endpoints.md` at `fdc3dd7f…`"); `oi-qm-ext-1/README.md`:26 links #1173 comment 6686122542 as "Gate A" | applied | §3, accepted-head row |
| F14 (low), untraced references | `NOTES-r1.md`:33, :58; `CONFIRM-r3.md`:34–38 | applied: two rows added | §3, off-`main` table |
| F15 (low), the note's own status and landing path | the review file is held outside the repository; no commit pins it | applied in modified form: no placeholders; the header states the proposed path `STATUS.md`, the README listing, r1's review verdict and that r2 is unreviewed; the review-gate row states the same; the review of this note is added to the off-`main` table as support off `main`, closed by landing the review and this response with the note; §6 item 4 asks about the exact-head review and a confirmation of r2; §6 item 9 added | header; §3 item 8 table and off-`main` table; §4; §6 items 4, 9 |
| F16 (low), three wordings | `GATE-A-AMEND-r2-TRACE.md` is 101 lines; r4:10–11 | applied | §0; §1 table; §3 item 8 table |

No finding is declined. `STATUS-r2.md` is 214 lines.
