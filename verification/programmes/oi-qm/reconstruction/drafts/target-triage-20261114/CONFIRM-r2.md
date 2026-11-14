# Delta confirmation of TRIAGE-r2 (non-author, read-only)

This is a model review of the text at the revision below. It is not an owner decision. It proposes
no tier, readiness, authorization, prerequisite, ordering or scientific-status value (`AGENTS.md`
§A.45). Nothing was edited, committed, pushed or posted, no file in any checkout was changed, and
no computation on OI models was run. Every replacement below is wording for a planning record that
the owner decides from.

## 0. Revision reviewed

- Draft PR #1290, branch `records/target-triage-914-20261114`, commit
  `f5b3ee2d9d24b8f752179f9ec1bc0c5dd61def6d` (`git rev-parse HEAD` matched; `git status
  --porcelain` empty).
- Directory `verification/programmes/oi-qm/reconstruction/drafts/target-triage-20261114/`.
  SHA-256 as computed in this pass, all equal to the recorded values:
  - `TRIAGE-r2.md` `6d85d545376be64e3eb8dbeeac7590efe8adad5985f6cef18953336d347d22e6`
  - `OWNER-TABLE-r2.md` `84eb7a6d1e11371ec42abf465488f381441ecc2eb88410ce4002bdb702d61501`
  - `RESPONSE-r1.md` `a8e01f39cce30dcd15969d0ad9b019d8f00577c280a1c19d42287fda1c727455`
- Sources fetched fresh from the public API for this pass (2026-11-14, about 12:12Z), into a new
  directory, not reusing the writer's or the earlier reviewer's downloads: the open-Issue list
  (90 Issues; items with `pull_request` excluded), all 90 bodies, all 90 comment threads
  (974 comments; r2 cites the earlier count of 972), the five owner records named in the brief and
  #1169 c.6875724719; PR #1289 head `927915e9923281dae3da9d414fa349ccbb5d8643`
  (`GATE-A-AMEND-r4.md`, `GATE-A-AMEND-r3.md`, `GATE-A-AMEND-r3-TRACE.md`,
  `OWNER-QUESTIONS-r4.md`, `README.md`, `CONFIRM-r4.md`); the F2 decision memo at `acfef447`;
  `papers/Main.md` and `papers/GR.md` on `main` at `dfeec843`.

## 1. Verdict

**ACCEPT WITH CHANGES.** All 24 findings of `REVIEW-r1.md` are applied as `RESPONSE-r1.md` says and
are right at source; the three modified dispositions are sound. The counts hold (41 affected in 39
rows, 49 unaffected, four conditional on T7, nine role only), every row's unit column is "None
recorded", and all 329 quotations re-match. Seven changes are required before the owner uses the
table; three of them are blocking because they bear on the owner's scope items 5–7:

- **RC1 (blocking):** r2 and the owner table never say the three-part target is adopted, and T0
  reads as if it were not. T0 is reworded to the record it concerns.
- **RC2 (blocking):** three statements (#1234, #1061, D-10) still take the lattice model of Main
  and SM as the common model.
- **RC5 (blocking):** T14 is offered as a quick choice, not as a scientific question needing its
  own assessment.
- RC3, RC4, RC6, RC7: required, not blocking (§5).

## 2. Coverage

| Evidence | Exists | Rechecked independently in this pass | Rests only on earlier work |
| --- | --- | --- | --- |
| Findings of `REVIEW-r1.md` | 24 | 24: each checked against r2's text, and its source re-read or re-matched (§3) | 0 for the disposition check. For S2 and S6 the source check is of the quoted text; #866 and #1143 were not re-read in full |
| Issue bodies | 90 | 39 re-read in full; 25 in part; 26 searched mechanically only (list below) | The unaffected classification of the 25 mechanically searched unaffected bodies rests on the earlier full reading (`REVIEW-r1.md` §1) plus this pass's keyword search, which found no target wording in them. #866's classification rests on earlier reading plus its re-matched quotations |
| Quotations in `TRIAGE-r2.md` | 329 | 329 re-matched mechanically (328 in fresh bodies, comments, owner records, amendment files, memo or `Main.md`; 1, at r2 line 232, in the fresh Issue title of #1216). 286 of them (all of §3) confirmed to sit in the record the text attributes them to | 0 |
| Quotations in `OWNER-TABLE-r2.md` | 7 | 7; one is not in the Issue it is attributed to (RC4) | 0 |
| Comment threads | 90 threads, 974 comments | No thread read in full. 8 comments read in full; 16 read in part (listed below). All 974 downloaded and used for quotation matching; the 334 comments of the 49 unaffected threads searched mechanically for target wording (12 hits, all opened; none restates the superseded requirement) | About 950 comments were not read in this pass; earlier work also left about 900 of 972 unread. The classification stays provisional with respect to them |
| Owner records | 5 named + #1169 c.6875724719 | 6, read in full | 0 |

**Bodies re-read in full (39):** #865, #867, #869, #872, #873, #875, #913, #914, #944, #945, #983,
#1007, #1014, #1015, #1049, #1052, #1055, #1059, #1060, #1061, #1062, #1063, #1064, #1065, #1066,
#1067, #1068, #1069, #1071, #1147, #1210, #1211, #1216, #1217, #1220, #1234, #1236, #1238, #1245
(in a few, the identical closing governance sentence was filtered out).

**Bodies re-read in part (25):** #868, #1143, #1169 (planning block and the passages r2 quotes);
#1010 (lines cut at 600 characters); #1037 (headings and question lines); and the keyword-hit
passages of #871, #896, #897, #898, #899, #900, #902, #929, #970, #979, #1029, #1031, #1032, #1090,
#1092, #1162, #1188, #1190, #1244, #1255.

**Bodies searched mechanically only (26):** #866, #870, #874, #901, #903, #924, #934, #985, #986,
#996, #1004, #1008, #1013, #1028, #1058, #1070, #1072, #1073, #1091, #1112, #1118, #1141, #1142,
#1155, #1163, #1193.

**Comments read in full (8):** #914 c.6875046763, c.6875548603, c.6876304390, c.6876592679,
c.6563412734; #1169 c.6875724719, c.6876591512; #1211 c.6740537555. **In part (16):** #914
c.6777841157 (the three gates), c.6775022284 (opening and table head); #1210 c.6743200254,
c.6874589871 (r7c); the twelve keyword hits #970 c.6561481395, #1028 c.6572625127, c.6657997292,
c.6658060093, #1029 c.6583722893, #1031 c.6567522034, c.6666613671, c.6676219154, c.6677496553,
c.6682459524, #1112 c.6643691865, #1162 c.6682778651. Authors and dates of all 27 comments cited
in r2 §5 and the D-entries were checked mechanically: all posted from `amaybaum`, dates as stated.

**Quotation method.** Every straight-double-quoted string was extracted (329, matching r2's
count), Markdown emphasis and backticks stripped, whitespace normalized, and segments separated by
"…" matched separately. For §3, each string was looked up in the body and comments of the Issue its
D-entry names, any Issue or comment named on the same line, and the amendment, memo and `Main.md`
sources: 276 sat there directly and the other 10 sit in the owner record the sentence names (#914
c.6875046763 or c.6875548603, #1169 c.6876591512, #1169 c.6791556736, the #1216 title, #944
workstream 6), each checked. Of the 32 strings with a comment id on their line, 29 sit in that
comment and 3 are table cells quoting another record the row names (r2 lines 613, 618, 621), each
confirmed by reading. Short generic strings (for example "ready", "Tier: High") were confirmed in
the attributed Issue's text, not separately located in its planning block. No mismatch was found in
`TRIAGE-r2.md`.

## 3. The 24 findings

| Finding | Applied in r2 as `RESPONSE-r1.md` says | Right at source |
| --- | --- | --- |
| B1 | Yes: #914 row, D-1, §6 item 11 | Yes. #914 body §2: rows 3–7, 17c, 21 state forward implications; rows 8, 9, 11, 12 concern what the stated access sources; row 20 reads "→Q (sourcing)" |
| B2 | Yes: five rows, §6 item 1, T7 | Yes for those sites (c.6875548603 names the Standard Model an aim and "makes no claim"; no record selects the lattice model). Residue at #1234, #1061 and D-10 (RC2) |
| B3 | Yes, with the stated modification | Yes. D-6 quotes the c.6875046763 sentence whole ("The common-realization requirement of #1169 and the exact-tunability requirement of #1236 stand as recorded.") and #1236 c.6875058407; the full sentence is verbatim, so the bracketed form is not needed. T5, T11 withdrawn; T4 a note |
| B4 | Yes | Yes. #1015 and #1037 quotations re-matched; #970's body names none of #1060, #868, #873, #983, #1066, while #1060, #1066 and #983 name #970; #944 workstream 6 verified; §6 item 3 and the §1 provisional sentence present |
| B5 | Yes: D-24, row, T12, §5 | Yes. The sentence sits under "## Calculation milestone before explanatory outreach" in #873's body; c.6875553420 and c.6876591512 keep QB5(a) frozen |
| B6 | Yes | Yes for the four answers (verbatim against c.6876591512) and T2, T3, T6, T14. T0's wording, which came from B6's own replacement, blurs adoption (RC1) |
| S1 | Yes | Yes. Memo at `acfef447`: G2 text verbatim; G6 "At least one independent prediction or postdiction"; G7 "no knobs"; decision (c) in #875's body |
| S2 | Yes | Yes at the level of the quoted P0 question; no target record mentions the evolution freedom |
| S3 | Yes | Yes. `papers/Main.md`:66 on `main` at `dfeec843` reads as quoted |
| S4 | Yes | Yes. #914 c.6563412734 puts F2 under "Standing status, unchanged by this record"; decision 9 is the recovery criterion following decision 8 (P2-G) |
| S5 | Yes, modified (no quotation column) | Yes; the modification is acceptable because the quotations are re-matched here. The #1211 c.6740537555 entry, read in full: the owner's direction is quoted verbatim and includes "Complex structure: Yes, track it independently if the review confirms it is an additional premise."; "agrees with decision 4" is a fair reading. The form cell should state this rather than defer to the reviewer (RC7) |
| S6 | Yes | Yes for each quoted claim (re-matched in #1143's body); dispositions agree with c.6875548603 and c.6876591512. SEL-ACCESS-1/SEL-EXCL-1 not opened, as r2 says |
| S7 | Yes | Yes; one wording refinement in RC1(b) |
| S8 | Yes | Yes. "`oiPlusMin_iff_qm` as the target" is in #914 body §4, among the controls of the #1007 candidate |
| S9 | Yes | Yes |
| S10 | Yes | Yes; T7 is neutral |
| N1 | Yes | Yes; the proposal's wording no longer appears |
| N2 | Yes | Yes; all eight statements re-matched in #1169's body |
| N3 | Yes | Yes; c.6775022284 lists #1169, #1143, #1211, #1059, #1210, #1220, #1216 |
| N4 | Yes | Yes; "candidate strengthened principle" is in #1210's body |
| N5 | Yes, in part | Yes. #970 track 6 is named by #1060; #903's body has no Bell, CHSH or Tsirelson wording |
| N6 | Yes | Yes; #1064's prerequisites name access (P/S/R/Acc), #1147's name O-ACC |
| N7 | Yes | Yes; c.6658060093 records the retitle, and `Main.md` on `main` carries "Finite-Observer Representations and Quantum Reconstruction" |
| N8 | Yes | Yes |

## 4. Classifications, units, adoption, questions

**Counts.** §2 has 39 rows naming 41 Issues; §4 names 49; no overlap, none missing, none extra
against the fresh open list; the owner table has the same 39 rows and 41 Issues. Four rows (#983,
#1049, #1065, #1066) read "None as written" with a T7 condition, in r2 and the owner table alike;
nine are role only (eight rows say so; #1069's role-only status is stated in §1 but not in its row,
O2). RC2 does not change the counts: #1234 stays affected through the Bell clause, and #1061
through its cosmological cut.

**Unaffected Issues.** The 12 comment hits and 23 body hits in unaffected Issues are safeguards
("do not infer … full OI↔QM equivalence"), the Main retitle, a §A.34 citation item (#1190 WP6-05)
or uses of "equivalence" unrelated to OI and QM. None restates the superseded class-wide
requirement. The 49 stand.

**Units (scope item 4).** All 39 unit cells begin "None recorded" and all 39 owner-table cells
"Nothing recorded". The four target records each authorize no board, priority or status change
(c.6875046763 and c.6875548603: "No merge, manuscript change, computation or board change is
authorized by this record"; c.6875724719: "changing board priorities" under "Not authorized";
c.6876591512: "authorizes no computation, manuscript change or status change"). No row, question
or owner-table line infers a planning change from the target change.

**Carriers and encodings (scope item 5).** No row assumes an answer to T14: #875 (D-2), #1220
(D-36) and §4's #898 line refer to it neutrally, and #1007's row repeats answer 3's own words.
T14 is not presented as a question needing its own scientific assessment (RC5).

**Adoption (scope item 6).** The records: #914 c.6875548603 records the owner's "Yes proceed as
suggested" to the three-part proposal; #1169 c.6875724719 calls it "the three-part target adopted
in #914"; #1169 c.6876591512 records "I adopt all five Gate A dispositions", states
"`GATE-A-AMEND-r4.md` is not edited by these answers. It remains the reviewed amendment proposal",
and, in item 5 on preparing r4 for preservation, "adoption of the amended target requires an
explicit owner decision". r2 quotes the item 5 sentence right after the three-part target in §1
and in D-3, never says the three-part target is adopted, and T0 and the owner table ask about
"the amended target text" with options tied to r4's landing. A reader can take the three-part
target itself to be unadopted. §1 also calls r4 "not adopted as the target text", and §6 item 12
lists r4 among frozen records; it is an unmerged reviewed proposal. RC1 and RC6.

**Standard Model question (scope item 7).** T7 is neutral, and the four conditional rows are
conditional everywhere they appear, including both count statements and the owner table. Three
other statements still take the lattice model of Main and SM as the common one: the #1234 row
("the common model must eventually carry both its update-rule class", the update rule being Main's
linearity (vii)), against r2's own §6 item 1, which puts #1234's update rule among the lattice
model's clauses; the #1061 row (C4 "at either cut", the lattice cut being [SM] Theorem 22's); and
D-10's sentence placing the meeting of the Bell clause and part 3 at H-Bell, whose graph family is
Main's preparation-indexed Bell branch and whose continuum step is the GR paper's Ollivier–Ricci
route. RC2.

**Owner questions (scope item 8).** Checked against c.6875046763, c.6875548603, c.6875724719,
c.6876591512 and c.6876592679:

| Question | Status at source |
| --- | --- |
| Four Gate A questions | Answered (c.6876591512); r2 §7 states them correctly |
| T0 | Open, as the adoption of r4's amended Gate A text as the governing contract; misdescribed (RC1) |
| T1, T2, T3, T6, T7, T8, T10, T12, T13 | Open; no record answers them. T2's "kind of condition is settled" and T13's "Answer 4 does not address confinement" are right (c.6876591512 lists confinement among remaining obligations) |
| T9 | Open; conditional on T7 for the update-rule half (RC2) |
| T14 | Open; needs its own assessment (RC5) |
| T4 | Not a question; correct as a note |
| T5, T11 | Moot: answered by c.6875046763, #1236 c.6875058407 and the no-board-change clauses |

**Evidence limitation (scope item 9).** r2 §1 keeps it: "about 900 were not read by either
party, and a restatement of the superseded requirement there would not have been seen". The
README keeps it too. Neither claims comprehensive comment coverage. This pass read no comment
thread in full (§2).

**Owner table (scope item 10).** Every line follows from r2 in plain language except four: #875
drops r2's "unless X is read as E with C" and so states the narrowing unconditionally; #1211 quotes
"full equivalence", which is not in #1211 (its body reads "full operational equivalence"); #1234,
#1061 and #1245 carry the defaults of RC2 and RC3; T0 and T14 as above. RC1, RC2, RC3, RC4, RC5.

## 5. Required changes

Old text is copied from the files at the reviewed revision. In short inline old strings, `\n`
marks a line break of the file (followed by its indentation); block-quoted old text keeps the
file's wording with the quote's own line breaks.

### RC1 (blocking). Adoption of the three-part target and the status of r4

(a) `TRIAGE-r2.md` §1, replace

> The same record says "No sector condition C and no extension E is proposed or adopted" and
> "adoption of the amended target requires an explicit owner decision".

with

> The same record says "No sector condition C and no extension E is proposed or adopted". Its item
> 5, on preparing `GATE-A-AMEND-r4.md` for preservation, says "adoption of the amended target
> requires an explicit owner decision". *Reading:* the amended target there is r4's amended Gate A
> text, the record that item preserves; #1169 c.6875724719 already speaks of "the three-part target
> adopted in #914". The three-part target (#914 c.6875548603, the owner's "Yes proceed as
> suggested") and the four answers above are adopted owner decisions; whether r4's text is adopted
> as the governing Gate A contract is open (T0).

(b) §1 "Names of parts", replace "a reviewed proposal that is not adopted as the target text; the
four answers above are owner decisions." with "the reviewed amendment proposal, which is not adopted
as the governing Gate A contract; the three-part target and the four answers above are owner
decisions."

(c) §2, #1169 row, last cell: replace "Adoption of the amended target text" with "T0".

(d) D-3, replace

> - The four Gate A questions are answered (c.6876591512; §7). Open: "adoption of the amended target
>   requires an explicit owner decision".

with

> - The four Gate A questions are answered (c.6876591512; §7). Open (T0): whether the amended Gate A
>   text of `GATE-A-AMEND-r4.md` is adopted as the governing Gate A contract; item 5 of c.6876591512:
>   "adoption of the amended target requires an explicit owner decision".

(e) §7, replace `- T0. Adoption of the amended target text, which "requires an explicit owner
decision".` with

> - T0. Whether the amended Gate A text of `GATE-A-AMEND-r4.md` is adopted as the governing Gate A
>   contract (#1169 c.6876591512, item 5: "adoption of the amended target requires an explicit owner
>   decision"; *reading:* the amended target there is r4's). Not open: the three-part target,
>   adopted on #914 (c.6875548603; #1169 c.6875724719, "the three-part target adopted in #914"), and
>   the four Gate A answers.

(f) `OWNER-TABLE-r2.md`, replace `- T0. Adopt the amended target text: adopt now / adopt after r4
lands / leave as proposal.` with

> - T0. Adopt the amended Gate A text of `GATE-A-AMEND-r4.md` as the governing Gate A contract:
>   adopt now / adopt after r4 lands / leave as proposal. (Already adopted: the three-part target,
>   #914 comment 6875548603, and the four Gate A answers.)

### RC2 (blocking). Remaining lattice-model defaults

(a) §2, replace the #1234 row

> | #1234 (D-16) | Bell; one model | The common model must eventually carry both its update-rule class and a Bell route | None recorded; premise question 6 unchanged, option (c) available | Items 1–5, 7 | T9 |

with

> | #1234 (D-16) | Bell; one model (conditional) | The common model must eventually carry a Bell route. If the lattice model of Main and SM is chosen (T7), it must carry both its update-rule class (vii) and that route | None recorded; premise question 6 unchanged, option (c) available | Items 1–5, 7 | T9, T7 |

(b) D-16, replace "the common model must eventually carry both its\n  update-rule class and a Bell
route." with "the common model must eventually carry a Bell route. The update-rule class (vii) is a
clause of the lattice model of Main and SM and binds the common model only if that model is chosen
(T7; §6 item 1)." In the next bullet, replace "and it then records an incompatibility the target
would require\n  to be resolved." with "and, if the lattice model is chosen as the common model
(T7), it records an incompatibility the target would require to be resolved."

(c) §7, replace `- T9. #1234's premise options, given that the common model must carry a Bell route
(D-16).` with `- T9. #1234's premise options, given that the common model must carry a Bell route;
the options bind the target only if the lattice model of Main and SM is chosen (T7) (D-16).`

(d) §2, #1061 row: replace the cell "C4 at either cut is a condition on the observer of any common
model" with "*Reading:* C4 at the cosmological cut bears on the observer of any common model the
gravity part uses; the lattice cut is that of [SM] Theorem 22 and bears on the common model only if
the lattice model is chosen (T7)", and the last cell "None from the records" with "T7". In D-27,
replace "Target served: C4 at either cut is a condition on the observer of any common model." with
the same reading.

(e) D-10, replace "which is a point where the Bell clause meets part 3's consistency clause." with
"which, as a *reading*, is a point where the Bell clause meets part 3's consistency clause if the
preparation-indexed Bell branch and the Ollivier–Ricci continuum step are those of the common model
(T7)."

(f) `OWNER-TABLE-r2.md`: replace the #1234 line's second cell with "The common model must in the end
carry a Bell route; it must also carry this Issue's update rule only if the papers' lattice model is
chosen as the common model" and its last cell with "T9, T7"; replace the #1061 line's second cell
with "Its cosmological-cut condition bears on the observer of any common model (a reading); its
lattice-cut condition does so only if the papers' lattice model is chosen" and its last cell with
"T7".

### RC3. #1245 and §6 item 4 state more than the records

#1245's body: the H-BD question is the repair of GR §3.2's boundary-only lemma, and its related
list reads "#1060: H-Bell. A Bell mediator is not assumed to lie in GR's hidden sector." r2 requires
H-BD on the common model unconditionally and assigns the Bell role to the hidden sector.

(a) §2, #1245 row: replace "H-BD must hold with the hidden sector's roles in parts 1–2 and Bell on
one model" with "If GR §3.2's route is used for part 3, H-BD must hold on the common model together
with any hidden-sector role parts 1–2 use; #1245 records that a Bell mediator is not assumed to lie
in GR's hidden sector".

(b) D-28, replace "Target served: H-BD must hold together with the hidden sector's roles in parts
1–2 and in the\nBell clause on one model." with "Target served: if GR §3.2's boundary-only lemma is
the route used for part 3, H-BD must hold on the common model together with any hidden-sector role
parts 1–2 use. The related list above states that a Bell mediator is not assumed to lie in GR's
hidden sector."

(c) §6 item 4, replace the item with

> 4. **Hidden-sector roles on one model.** #1245 (weak influence of the deep sector, if GR §3.2's
>    route is used for part 3) and #1236 and #1007 (hidden structure as the source of tunable
>    statistics) would have to hold on one model. #1060's Bell mediator is a further role only if it
>    is placed in the hidden sector; #1245 records "A Bell mediator is not assumed to lie in GR's
>    hidden sector."

(d) `OWNER-TABLE-r2.md`, #1245 line, second cell: "If the GR paper's route is used for gravity, its
deep-sector bound must hold on the common model alongside any hidden-sector role used for the
quantum parts; a Bell mediator is not assumed to lie in that hidden sector".

### RC4. Owner table: one condition dropped, one misquotation

(a) #875 line, second cell: replace "that form now applies to the sector" with "that form is now
required only on the sector, unless X is read as E together with C".

(b) #1211 line, second cell: replace `Its "full equivalence" wording` with `Its "full operational
equivalence" wording` (the string in #1211's body; "full equivalence" occurs neither in the body nor
in its comments).

### RC5 (blocking). T14 as a scientific question

(a) `TRIAGE-r2.md` §7, append to T14: "This is a substantive scientific question, not a planning
choice: which carriers and encodings are permitted fixes what inclusion and the sector equivalence
assert, and an encoding may carry quantum structure into the model rather than derive it. It needs
its own assessment, independently reviewed, before an answer is recorded; no row of this triage
assumes one."

(b) `OWNER-TABLE-r2.md`, replace `- T14. Agreed scope of carriers and permitted encodings: qubit-power
registers first / every finite carrier / other; to be stated.` with

> - T14. Agreed scope of carriers and permitted encodings. A scientific question that needs its own
>   assessment before it is answered; the triage assumes no answer. For now: commission that
>   assessment / record an interim scope (for example qubit-power registers first, or every finite
>   carrier) as provisional pending it.

### RC6. §6 item 12 calls r4 a frozen record

Replace item 12 with

> 12. **Records not reinterpreted.** `endpoints.md` (the accepted Gate A record, which #1169
>     c.6875724719 directs not be altered), the QB5(a) preregistration at `8dd0de90`, #1210's r7c
>     ledger and #1060's legacy round keep their text (§A.39, §A.42 item 6). `GATE-A-AMEND-r4.md` is
>     not a frozen record: it is the reviewed amendment proposal on draft PR #1289, "not edited by
>     these answers" (#1169 c.6876591512), and not adopted as the governing Gate A contract (T0).

### RC7. §5, the #1211 c.6740537555 entry

(a) Replace the row cell "As the reviewer reports" with: `Verbatim: the comment quotes the owner's
direction, including "Complex structure: Yes, track it independently if the review confirms it is
an additional premise."; #1217's body records that decision`.

(b) In the §5 introduction, delete "; the entry for #1211 c.6740537555 was not re-read in full by
the writer" (ending the sentence at "(S5).").

## 6. Optional suggestions

- **O1.** #1217: its premise serves SM's gauge decomposition, an aim rather than a part, as with
  #1066. Consider adding to the row "It bears on the target only if the six-link lattice branch is
  chosen (T7) or decision 4 is read to cover it (T8)". As written it does not assume the lattice
  model, so this is parity, not a correction; adopting it would make five conditional rows and the
  counts would need updating in §1, `RESPONSE-r1.md` and the README.
- **O2.** #1069 row: begin the "Target served" cell with "Role only (*reading*):", so the table
  shows the nine role-only rows the count names.
- **O3.** `RESPONSE-r1.md`, "Checks on r2": one of the 329 strings (r2 line 232) matches the #1216
  Issue title, not a body or comment.
- **O4.** README: once this confirmation is accepted, the sentence "The quotation count reported in
  r2 is the writer's; it is not yet independently confirmed" can say the count was re-matched at
  confirmation; the comment count at this pass is 974.
- **O5.** `RESPONSE-r1.md`, B6 row: "T0 (adoption of the target text)" would follow RC1's wording.
- **O6.** Owner table, #1220 line: add "for a specified family" after "inclusion", as in r2.
