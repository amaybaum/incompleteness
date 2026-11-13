# Response to REVIEW-r1 of the integration assessment

**Object.** `REVIEW-r1.md` (ACCEPT WITH CHANGES) of `INTEGRATION-ASSESS-r1.md` and `NOTES-r1.md` at
`79b4d4cd`, committed unchanged at `cc297f16` on `research/integration-assess-20261113` (fetched by
branch name; byte-identical to the review's working copy). r2 is `INTEGRATION-ASSESS-r2.md` (IA2) and
`NOTES-r2.md` (N2). r1 is unchanged. Every finding is applied; none is disputed. Where the state has
moved past the review, the r2 text follows the current state and says so below.

Line references are IA2:n and N2:n.

## Dispositions

| Finding | Disposition | r2 location |
|---|---|---|
| **F1** (Medium) #1275 not landable "any time" | Applied. Re-pinned at the current head `1ad01923` rather than `46a548fb`: unit 2(a) has moved to r3 (REVIEW-U2A-r1 REVISE, CONFIRM-U2A-r2 confirmed, r3 applying Y-1 to Y-5; #1275 c.6864323211), still without a ChatGPT exact-head review. Added that unit 2(a)'s QU4 (revise unit 1 or carry forward) bears on unit 1's Part 2. Step 2 retitled with item 0 and options (a)/(b); #873 c.6863416405 quoted for Q4, Q7, Q8 with author and time; #1275 added to §5; OQ-6 reworded. | IA2:40–45, :87, :112, :232–238, :385–410, :481–496, :585, :656–658 |
| **F2** (Medium) #1269 focused recheck 5897397957 | Applied as specified: summary, review trail, its integration sentence in Gates, step 3.4 review trail, §5 row. | IA2:46–50, :352–358, :517–519, :590 |
| **F3** (Medium) REC-1 r9 confirmed; c.6863753317 | Applied, and updated past the review: ChatGPT 5897679945 (20:34:33Z) now accepts r9 at `3a3aa146`, so step 4.1 records it instead of "a ChatGPT exact-head review is outstanding". Its optional LOW is recorded. c.6863753317 and c.6863414487 added to the owner records; pins, §1 row, §2.2 table, §5 row and r9:496 bar updated. | IA2:25–29, :50–52, :81, :162–163, :177, :287–300, :526–539, :588 |
| **F4** (Medium) QPHEN r5: narrowing option; untraced references | Applied: step 3.2 offers (a) land with own item 8 table, SC-42 disposition and stated status (REVIEW-PHASE1-r4 REVISE on r4), or (b) narrow to a named draft hypothesis. Mirrored in the summary, §2.1, §2.2, §3 #1269 item 8 and OQ-7. | IA2:46–50, :118–119, :221, :361–362, :506–512, :659–662 |
| **F5** (Medium) OQ-2(b) and r7's C6 | Applied at step 5.1, step 7.1 and OQ-2. | IA2:545–548, :569–572, :646–648 |
| **F6** (Medium) §A.46 basis | Applied: §6 "Basis" paragraph (with c.6846206075 quoted), OQ-10, a "§A.46 basis" bullet in every §3 entry giving both readings, #1271's reason restated as its item 8 gap and option (c), N2's sentence corrected. The #1270 EOI wording now matches (no `main` gap needs it). | IA2:66–67, :114, :254–256, :274–277, :297–298, :312–313, :330–331, :343–345, :363–365, :376–381, :402–404, :421–425, :475–476, :603–611, :669–671; N2:146–151 |
| **F7** (Low) `STATUS.md` heading, §A.46 item 4 | Applied: heading renamed; verification-status line and per-gap remediation added. | IA2:458–467 |
| **F8** (Low) true lines listed as superseded | Applied: reduced to row H as drafting-time state, head to be measured at landing. | IA2:280–282, :471–472 |
| **F9** (Low) reason for skipping the nit | Applied: new reason; step 7.1 restricted to blobs used as support (`6c127b0a` is provenance); OQ-1 and N2 updated. #1276's `DEPENDENCIES.md` row noted as provenance in §2.2. | IA2:229–230, :283–285, :569–571, :645; N2:160 |
| **F10** (Low) §4 preamble vs step 3 | Applied as specified. | IA2:439–442 |
| **F11** (Low) own-branch commits | Applied at both places (verified: `bac44eeb` in REVIEW-r1:16; `3f56d543` in CONFIRM-r2 and RESPONSE-r1; both ancestors of `d015131d`). | IA2:160, :468–469 |
| **F12** (Low) GR:426 book mirror | Applied (verified: ch19:116 and FULL:5263 state ρ_s = ρ_crit "by the Clausius relation and the shell theorem"; GR.tex:3030 carries the GR:426 sentence). | IA2:619–621 |
| **F13** (Low) skipped step | Applied in N2 and in IA2 §1 and §3 #1275 (verified through the jobs API: step 3 failure, step 6 skipped). | IA2:96–97, :400–402; N2:78–79, :105–106 |
| **F14** (Low) #1273 attribution; avoidable wait | Applied: SB rows split into #1273's classification and the assessor's reading; the narrowing alternative added to the summary, §3, step 6.2 and §5. | IA2:54–57, :128–131, :198–199, :329, :559–560, :591 |
| **F15** (Low) `0e0b3ddc` | Applied (verified: `ASSESS-868.md`:139–140, provenance; not an ancestor of `main`); carried into step 3.4. | IA2:215, :222, :517–519 |
| **F16** (Low) #1276 basis mixes claim and ranking | Applied, with OQ-11 and the step 7.3 status line. | IA2:58–59, :373–381, :575–576, :672–673 |
| **F17** (Low) unclosed gap wording | Applied as specified. | N2:154–156 |
| **F18** (Low) own disposition; #1270 standing | Applied: Standing states this record is not proposed for landing; #1270's PR-body standing quoted in the summary, §3 and §5; #1279 and #1282 added as non-candidates. | IA2:7–8, :61–64, :414–415, :595–596 |

Also changed for the moved heads, beyond the findings: §1 rows for #1268 (41 files) and #1275 (28
files, CI queued at `1ad01923`), the #1282 remark in §2.1, the AW-C3-1 cross-reference in §6
(IA2:630), unit 2(a)'s QU3 in §6 (IA2:628–629), and N2 §2A (re-run battery, merge-tree, ids and CI at
the moved heads; new records read) and §4.

## r1 → r2 delta (`diff INTEGRATION-ASSESS-r1.md INTEGRATION-ASSESS-r2.md`)

177 lines removed, 268 added, in 70 hunks (grouped by section below).

| r1 lines | r2 lines | Section | Change | Finding |
|---|---|---|---|---|
| 1 | 1 | title | r1 → r2 | — |
| 7 | 7–12 | Standing | own disposition; revision line | F18 |
| 21–24 | 26–29 | Pins | moved heads, #1279, #1282 | F1, F3 |
| 35–44 | 40–52 | §0 order 2–4 | #1275 conditional; #1269 recheck, QPHEN options; REC-1 r9 accepted | F1, F2, F3, F4 |
| 46–58 | 54–72 | §0 order 6–7, stays, basis, mechanics | narrowing of stage 7; ranking; #1271 reason; #1270 standing; basis line; #1279/#1282 | F14, F16, F6, F18 |
| 67, 73, 82 | 81, 87, 96–97 | §1 | #1268 and #1275 rows; skipped Release gate | F3, F1, F13 |
| 97–113 | 112–131 | §2.1 | #1275, #1270 EOI, #1269 QPHEN refs, topology, #1282 | F1, F6, F4, F14 |
| 142–158 | 160–177 | §2.2 #1274, #1268 | own-branch commits; r9 rows | F11, F3 |
| 179 | 198–199 | §2.2 #1273 | SB rows split | F14 |
| 195–201 | 215–222 | §2.2 #1269 | hypotheses block; QPHEN untraced refs; `0e0b3ddc` | F4, F15 |
| 208–216 | 229–238 | §2.2 #1276, #1275 | DEP provenance; unit 1 only; unit 2(a) untraced | F9, F1 |
| 231 | 254–256 | §3 preamble | basis pointer | F6 |
| 249–260 | 274–285 | §3 #1274 | basis; drafting-time state; nit reason | F6, F8, F9 |
| 265–275 | 289–300 | §3 #1268 | r9 reviews, gates, basis | F3, F6 |
| 287, 301–303 | 312–313, 327–331 | §3 #1272, #1273 | basis; narrowing option | F6, F14 |
| 315–316 | 343–345 | §3 #1271 | reason restated | F6 |
| 320–332 | 349–365 | §3 #1269 | heading; recheck; gates; hypotheses; basis | F2, F4, F6 |
| 343–345 | 376–381 | §3 #1276 | classifications vs ranking; basis | F16, F6 |
| 349–366 | 385–410 | §3 #1275 | heading; unit 2(a); owner Q4/Q7/Q8; CI; basis | F1, F13, F6 |
| 369–384 | 414–430 | §3 #1270 | standing; basis per part | F18, F6, F4 |
| 393–395 | 439–442 | §4 preamble | SC-42 exception | F10 |
| 411–425 | 458–476 | step 1 | heading; verification status; remediation; commits; drafting state; basis | F7, F11, F8, F6 |
| 430–439 | 481–496 | step 2 | conditional step, options (a)/(b) | F1 |
| 441–461 | 498–521 | step 3 | QPHEN options; BRIDGE treatment; status note with 5897397957 and `0e0b3ddc` | F4, F2, F15 |
| 466–477 | 526–539 | step 4 | r9 accepted; owner records; r9:496 | F3 |
| 483 | 545–548 | step 5.1 | OQ-2(b) re-pointing | F5 |
| 494 | 559–560 | step 6.2 | narrowing alternative | F14 |
| 503–509 | 569–576 | step 7 | support blobs only; OQ-2(b); OQ-11 | F9, F5, F16 |
| 518–527 | 585–596 | §5 | #1275 row; reasons for #1268, #1273, #1269, #1271, #1270; #1279/#1282 | F1, F3, F14, F2, F6, F18 |
| 533 | 603–611 | §6 | Basis paragraph | F6 |
| 541–542 | 619–621 | §6 | GR:426 mirrors | F12 |
| 546–552 | 625–633 | §6 | owner Q8 quote; unit 2(a) QU3; AW-C3-1 | F1 |
| 554 | 635–636 | §6 | line rewrap only, wording unchanged | — |
| 563–582 | 645–673 | §7 | OQ-1, OQ-2, OQ-6, OQ-7 reworded; OQ-10, OQ-11 added | F9, F5, F1, F4, F6, F16 |

## r1 → r2 delta (`diff NOTES-r1.md NOTES-r2.md`)

16 lines removed, 57 added, in 9 hunks.

| r1 lines | r2 lines | Change | Finding |
|---|---|---|---|
| 1 | 1–4 | title; revision note | — |
| 75–76 | 78–79 | skipped Release gate | F13 |
| after 78 | 82–115 | new §2A: re-check at the moved heads | F1, F2, F3 |
| 98, 100–103 | 135, 137–141 | §4 parallel work updated | F1, F3 |
| 108–111 | 146–151 | stricter reading corrected | F6 |
| 114–115 | 154–156 | owner-exception wording | F17 |
| 117 | 158 | r3:198–200 | consistency with the review's check |
| 119 | 160 | nit reason | F9 |
