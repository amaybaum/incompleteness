# Response to the independent review r1 of the Bell landing plan (#868)

Review: `REVIEW-BELL-PLAN-r1.md` in this directory, on `ed61696d`, verdict ACCEPT WITH CHANGES. Every
finding is applied in place, using the review's replacement text where it gives one. The review file
is unchanged. No input record is modified; no scientific conclusion, verdict or classification of an
input changes. File:line references below are to the files as revised (LP = `LANDING-PLAN.md`,
SBS = `STATUS-BS.md`, SL3 = `STATUS-SB-L3.md`, SLD = `STATUS-LADDER.md`, NP = `NOTES-PLAN.md`).

## Dispositions

| Finding | Disposition | Where |
|---|---|---|
| **B1** STATUS notes cite off-`main` plan files; §6.3 tracing incomplete | Applied. The three notes cite neither plan file: the headers read "(the Bell support and ladder package, #868 comment 6873193841, option (1))"; the OQ-2 and OQ-7 pointers are replaced by the review's wording; the SL3 sentence on landing forms is deleted; the N′ justification is in SL3 itself; SLD's "LANDING-PLAN.md" pointers read "re-measured at the package head". The N4 scope paragraph is in SLD itself (SLD:157–177). LP §6.3 gains the plan-files row, and LP:500 is corrected. | SBS:3–4, :197; SL3:3–4, :26–29; SLD:3–4, :178–181, :208; LP:495, :500–501 |
| **B2** SLD's scoped claim drops hypotheses | Applied with the review's replacement text, including the AL clause's finite abelian site groups and "with every setting pair of positive probability". | SLD:63–69 |
| **S1** Main:360 is not the measurement-dependent witness | Applied: check 2 (LD:150–153) for PR reachability; Main:360's general sentence and Main:416 for the absence of a selector; neither N4 nor Main:360's construction covers that branch. Layer "A; P". | LP:104, :184, :223–226, :348–350, :460; SLD:53, :130, :166–172, :188–192 |
| **S2** LD:284 is an unattributed N4 use | Applied: row added; "three times" → "four times"; SLD lists the four uses. | LP:179, :186; SLD:160–165 |
| **S3** QH sentence: not "narrowing" | Applied with the review's text: the sentence stays support off `main`, is stated with QH's conditions (NNB, P2, H-PREP), and lands as owner-identified non-load-bearing context. No r4. OQ-6 asks whether the merge decision records it under §A.42 item 8's final sentence. | SLD:149, :188–195; LP:361–371, :464; NP OQ-6 |
| **S4** self-referential pending lines | Applied: each note states its package review and merge decision "at the package head `<sha>`", with the merge decision quoted in a forward note after landing. G3 now adds that forward note and a focused exact-head check; G1 gains (i′). | SBS:211–220, :224–226; SL3:165–181; SLD:222–235; LP:52, :54 |
| **S5** C2 sentence misapplied to new landings | Applied with the review's text in LP §7; each note's lead-in now says item 8 requires every one of its five conditions for a record landed after adoption; historical authorization is recorded as provenance. | LP:509–511, :522; SBS:201–205; SL3:155–160, :174–176; SLD:213–217 |
| **S6** "closes" OC's D2/E2 | Applied with the review's text: BS and L3 "put on `main`" the conditions of OC's narrowed rows; OC stays conditional; SLL still needs L2. The OQ-13 forward note keeps OC's conditional wording. | LP:129–135, :333, :423–424, :520; SBS:215–217; SL3:169–171 |
| **S7** SB-L3 extract under-specified | Applied with the review's text: verbatim quotation; every non-verbatim line marked; resolution table for Main:364, Theorem N and (Sep), B1, SB §6 and S5; N′ composition; support layer. LP §6.3 and SL3's table gain the B1, SB §6 and S5 rows. | LP:417, :496–498; SL3:16–23, :128–130 |
| **S8** "however deep" | Applied with the review's text: finite depth only; infinite towers need SB L2 (gap D3); MI kept. | SL3:66–70 |
| **S9** BS whole is an owner choice | Applied: LP §1 and NP decision 2 make it conditional on the owner's choice; OQ-5 states that the whole record lands Lemma G, NBA, §5 and §6, beyond the named components. | LP:56–58; NP decision 2, OQ-5 |
| **S10** probe authorization | Applied with the review's text in SBS Limitations; mirrored in the probe row and the dependency row; LP §6.2 adjusted. | SBS:101–104, :135, :151; LP:480 |
| **S11** L3 load-bearing only for the controlling condition and stage 5 | Applied with the review's text. | LP:146–150; SLD:145; SL3:149–152 |
| **S12** R-b | Applied with the review's text. | LP:51; SBS:201–203; SL3:155–157; SLD:213–215 |
| **S13** evidence-tag definitions | Applied: superseded-line entries for LD:37–39 and BS:21–24. | SLD:196–198; SBS:188–190 |
| **S14** L3 text unchanged from r1 | Applied with one correction of fact. The review states that the L3 paragraph is byte-identical between r1 (lines 153–157) and r2 (lines 167–171). A comparison of `b94b283a` and `86a413c8` shows lines 153–156 and 167–170 identical, while r2's line 171 appends one sentence citing review 5857981727. The added text says so; the conclusion (the r1 review's remark applies to L3's statement and argument as accepted) is unchanged. | LP:193–196; SL3:41–44 |
| **N1** "This plan authorizes no work" | Applied: "A remediation plan does not authorize new work" (#1169 c.6865680499). | SBS:108–109; SL3:99–100; SLD:107–108 |
| **N2** one range for the exogenous theorem | Applied: Main:364–389 throughout SBS; the drift bullet maps BS's own range. | SBS:160–162, :207 |
| **N3** five required fixes | Applied: "among others (CF⇒MI one direction; the O2 window)". | LP:205–206 |
| **N4** quotation of 5858000929 | Applied: the review's words quoted. | LP:191–192 |
| **N5** SLD drift heading | Applied. | SLD:178 |
| **N6** probe output count | Applied: "17 checks PASS, ALL PASS". | SBS:135 |
| **N7** N′ addition is a composition | Applied. | LP:201–202; SL3:26–29 |
| **N8** RC's `D_0` | Applied: "and OA1:556–558 is the support". | LP:115 |
| **N9** one-product-extractor condition | Applied. | SBS:69–70 |
| **N10** BS:421–422 | Applied: superseded-line entry. | SBS:191–192 |
| **N11** independent re-derivation of ids | Applied. | NP "Checks of identity" |

Owner-question recommendations of the review are recorded beside the writer's in NP "Open owner
questions" (OQ-1 to OQ-15).

## Diff summary (against `8b03a04c`)

- `LANDING-PLAN.md`: G0 R-b wording; G1 (i′); G3 forward note; BS-whole as owner choice; stage-7
  measurement-dependent row; §2.3 "addresses" with OC's conditional rows; §2.4 L3 load-bearing scope;
  §2.5 fourth N4 use, S1 attribution, L3 r1/r2 comparison, N′ composition, N3 wording; §4 QH
  classification; §5.2 SB-L3 content; §6 N4, QH, probe and plan-file rows, B1 and S5-provenance rows;
  §7 lead-in, rationale and historical-authorization rows.
- `STATUS-BS.md`: header; claim's extractor condition; probe limitation and rows; remediation
  quotation; drift range; superseded lines for BS:21–24 and :421–422; Landing basis (R-b, five
  conditions, package-head wording, OC conditional).
- `STATUS-SB-L3.md`: header; carried-record composition; N′ justification; r1/r2 comparison;
  finite-depth consequence; remediation quotation; dependency rows for S5, B1 and SB §6; L3
  load-bearing scope; Landing basis.
- `STATUS-LADDER.md`: header; claim's hypotheses (B2); stage-7 support rows; remediation quotation;
  L3 row; QH row; N4 paragraph with four uses; drift heading; QH superseded line; LD:37–39 entry;
  Landing basis.
- `NOTES-PLAN.md`: review read; identity re-derivation; decisions 2, 5, 7 and new decision 10; OQ
  list with writer and reviewer recommendations; "Not done" updated.
- `RESPONSE-BELL-PLAN-r1.md`: this file.
