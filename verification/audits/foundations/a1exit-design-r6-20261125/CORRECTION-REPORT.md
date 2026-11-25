# r6 correction report, second round (F1 to F8, the unmarked requirements, OC attribution)

Deterministic correction by `build/correct2.py`, which reads `out-final2/` (read only), MAPPING.json and the #1169 comments read with GET requests, and applies the logged edits below. Each edit carries the finding it applies (F1 to F8, F7-<requirement>, OCFIX) or `meta`. Authorization, quoted: #1169 comment 7164340996 (2026-11-25T13:49:23Z): "A1 design r6: Proceed with the second correction round, addressing F1–F8 and the additional unmarked requirements. Preserve all existing safeguards and keep the V4 group deferred. Prepare the corrected design for independent review. This does not authorize adoption, freezing or execution.". No governance rule is amended, no exception is created, no expectation of the V4 group changes, and r6 stays a draft. No git or GitHub write was made.

Findings applied:

- F1: Classify every cited decision as (i) the owner's own words on GitHub, (ii) a session-written record on GitHub without owner words, or (iii) no GitHub record; verified by reading the comments with GET requests.
- F2: Correct the description of V5-D2: it widens `resid`; the W2 allow rules rest on no owner decision.
- F3: Disambiguate the labels D1-D4 (three senses) and D1-D8; re-key the requirements that cite the Stage 1 review's corrections to S1-D2.
- F4: Unmark R6.DENY.1 and R6.DENY.2, whose content does not depend on V5-D1.
- F5: Record that a rejection of the V4 reversal needs a new rule identifier, since DR-2 is retired and never reused.
- F6: Record that V15's FAIL candidate needs a rule of the DR-1d form, so that three consistent resolutions exist; V4, V27, V27-glossary and V15 expectations unchanged.
- F7: Mark the unmarked requirements with their actual decision basis.
- F8: Formatting: a blank line before a requirement that directly follows the previous requirement's Sources line.
- OCFIX: Correct the statement that OC-1 to OC-5 lack a comment id: they are quoted in the owner's words in #1169 comment 7163402499.

Correction of the previous report (OCFIX). The previous report stated that the owner corrections OC-1 to OC-5 "were relayed in session without a comment id". That is incorrect: #1169 comment 7164065815 (2026-11-25T13:38:08Z): "The correction report lists the owner's decisions OC-1 to OC-5 as relayed without a comment id. That is incorrect: they are recorded verbatim in comment 7163402499." The owner's approval quoted there is "Authorize the bounded specification correction as proposed, including both refinements in your latest message.", and items 1 to 4 and 6 of the quoted proposal are OC-1 to OC-5 (AUTHORIZATIONS.md). The statement is corrected in the adoption trace of sec. 32 (edit OCFIX) and in this report; the previous report is a record of its round and is not edited.

***

## 1. Inputs and outputs (sha256)

| Input (read only) | sha256 |
|---|---|
| out-final2/DESIGN-r6.md | a76bcf1c12b745b87586fff9e39cf9331302eae7ab1b352dd0e65466ff08dcec |
| out-final2/EXPECTATIONS.json | c30d1f7a1cda41e442d592831cef5d156885961d9ae8d7c8788b52891fe26a17 |
| out-final2/REQUIREMENTS.json | 159e564b033df76a3e83fea5de80a11c42da65f172a3014152b0fb89e07a982f |
| out-final2/MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| out-final2/PARAPHRASED-DECISIONS.md | 250be39bff7bff6bfce40713bd1473bf28b56009a654a27e556600bf50ad43e3 |
| out-final2/CORRECTION-REPORT.md | 954e984c393486f64f82541b12946e5f148715e668fc5cbce24e08fed462f8a7 |
| out-final2/build/correct.py | 284d2d757dc83705ddf1b923a3b7a04d6d8e84e517fe31f18e32b0311ebaea02 |
| out-final2/build/report_text.py | 41d9dfbfda94a4a29081a010e1dc582a36d79b9554890c48c9471afee1120b01 |
| PENDING-33.md | b1a171a958999bdbb7d576ed835cc95f7789639e23e5ed052f5e40a4de782fe6 |
| MAPPING.json | bd1a8657961fd659b29980178781a7f30fd6e5b53da9a734db28a20130c9ff85 |
| gh7/sel.json | af740cc18fa630358aa618c585508439bde4b8fb7d426ecd6808faa5e95db1e6 |

Comment bodies read (sha256 of the body as returned by the API): see AUTHORIZATIONS.md.

| Output | sha256 |
|---|---|
| DESIGN-r6.md | 5a17b3069bbfaac24b805293443645b0ac4145f6002d6450a3c9247b7682ad14 |
| EXPECTATIONS.json | acd321bca3853d0a4d873d5171bda1b091acb9fce86d5c3e82da14b763db0e9a |
| REQUIREMENTS.json | 6a0beaabec0dbba4e261837246d614ac9cf5fab2dfc5e42ffb07fd5516742ef9 |
| MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| PARAPHRASED-DECISIONS.md | 00b4bb82afb40cbd92ff7ff0d6e68b338c96ec855c6d85f9f64c70783419774a |
| AUTHORIZATIONS.md | afec2e717d359a3a949145ce448366b09c053525f148a08b259d1b3bb4923024 |
| FRESH-AUTHORIZATION.md | 6ad128fcaf4fa7c722bb29427fae9db0097d44f52232d0c057655eef0ceb2cb7 |
| V4-COMPARISON.md | 9ef12011b8613cc8e3133ee522ec61fc816e34bd7a17d85dd2e75031d29df405 |
| CORRECTION-REPORT.md | this file (its digest is reported by the generator run) |

***

## 2. Edits applied

| # | Finding | Target | Edit | Safeguard |
|---|---|---|---|---|
| 1 | F1 | R6.STAT.8 | attribution classified (class (ii)) | none weakened (stricter or neutral; sec. 3) |
| 2 | F1 | R6.STAT.8 | RE-26 alternative fixed by the record's class | none weakened (stricter or neutral; sec. 3) |
| 3 | F1 | R6.PUR.9 | attribution classified (class (ii)) | none weakened (stricter or neutral; sec. 3) |
| 4 | F1 | R6.DENY.6 | attribution classified (class (ii)) | none weakened (stricter or neutral; sec. 3) |
| 5 | F1 | R6.CTRL.15 | attribution classified (class (ii)) | none weakened (stricter or neutral; sec. 3) |
| 6 | F1 | Appendix H HIST-4 | text edit (1 occurrence(s)) | none weakened (stricter or neutral; sec. 3) |
| 7 | OCFIX | sec. 32 adoption trace | text edit (1 occurrence(s)) | none weakened (neutral; sec. 3) |
| 8 | F3 | R6.NOTE.13 | label senses stated | none weakened (neutral; sec. 3) |
| 9 | F5 | R6.PUR.9 | no reuse of the retired id DR-2 | none weakened (stricter; sec. 3) |
| 10 | F6 | R6.PUR.9 | options restated: (a), (b1), (b2), with new identifiers | none weakened (neutral to stricter; sec. 3) |
| 11 | F6 | R6.PUR.9 | per-row selection of the existing candidates stated | none weakened (neutral to stricter; sec. 3) |
| 12 | F5 | R6.DENY.6 | new identifier required | none weakened (stricter; sec. 3) |
| 13 | F6 | R6.DENY.6 | three resolutions stated | none weakened (neutral to stricter; sec. 3) |
| 14 | F5 | R6.CTRL.15 | new identifier required | none weakened (stricter; sec. 3) |
| 15 | F6 | R6.CTRL.15 | V15 needs a DR-1d-type rule | none weakened (neutral to stricter; sec. 3) |
| 16 | F6 | OBL-6 | discharge names the three resolutions | none weakened (neutral to stricter; sec. 3) |
| 17 | F4 | R6.DENY.1 | pending mark removed | none weakened (neutral; sec. 3) |
| 18 | F4 | R6.DENY.2 | pending mark removed | none weakened (neutral; sec. 3) |
| 19 | F7-R6.CTX.4 | R6.CTX.4 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 20 | F7-R6.OUT.15 | R6.OUT.15 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 21 | F7-R6.REC.24 | R6.REC.24 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 22 | F7-R6.CTRL.17 | R6.CTRL.17 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 23 | F7-R6.CTRL.23 | R6.CTRL.23 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 24 | F7-R6.RULE.7 | R6.RULE.7 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 25 | F7-R6.RULE.8 | R6.RULE.8 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 26 | F7-R6.RULE.9 | R6.RULE.9 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 27 | F7-R6.CTRL.24 | R6.CTRL.24 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 28 | F7-OBL-1 | OBL-1 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 29 | F7-R6.REC.6 | R6.REC.6 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 30 | F7-R6.REC.7 | R6.REC.7 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 31 | F7-R6.CTRL.22 | R6.CTRL.22 | marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." | none weakened (stricter; sec. 3) |
| 32 | F8 | R6.ANCH.11 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 33 | F8 | R6.ANCH.13 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 34 | F8 | R6.ANCH.16 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 35 | F8 | R6.HP.8 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 36 | F8 | R6.OUT.8 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 37 | F8 | R6.OUT.21 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 38 | F8 | R6.REC.11 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 39 | F8 | R6.DENY.6 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 40 | F8 | R6.CLASS.7 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 41 | F8 | R6.CTRL.4 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 42 | F8 | R6.CTRL.17 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 43 | F8 | OBL-21 | blank line inserted before the requirement | none weakened (neutral; sec. 3) |
| 44 | F3 | REQ:R6.PLAN.8 | pending key D1-D4 -> v3 D1-D4 | none weakened (neutral; sec. 3) |
| 45 | F3 | REQ:R6.CTX.1 | pending key D1-D4 -> v3 D1-D4 | none weakened (neutral; sec. 3) |
| 46 | F3 | REQ:R6.CTX.12 | pending key D1-D4 -> v3 D1-D4 | none weakened (neutral; sec. 3) |
| 47 | F3 | REQ:R6.ANCH.14 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 48 | F3 | REQ:R6.REC.14 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 49 | F3 | REQ:R6.CTRL.19 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 50 | F3 | REQ:R6.EVID.4 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 51 | F3 | REQ:R6.EVID.5 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 52 | F3 | REQ:OBL-15 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 53 | F3 | REQ:R6.DENY.5 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 54 | F3 | REQ:OBL-3 | pending key D1-D4 -> S1-D2 | none weakened (neutral; sec. 3) |
| 55 | F4 | REQ:R6.DENY.1 | pending key V5-D1 removed | none weakened (neutral; sec. 3) |
| 56 | F4 | REQ:R6.DENY.2 | pending key V5-D1 removed | none weakened (neutral; sec. 3) |
| 57 | F7-R6.CTX.4 | REQ:R6.CTX.4 | pending keys v3 D1-D4 | none weakened (stricter; sec. 3) |
| 58 | F7-R6.OUT.15 | REQ:R6.OUT.15 | pending keys R-D labels | none weakened (stricter; sec. 3) |
| 59 | F7-R6.REC.24 | REQ:R6.REC.24 | pending keys R-D labels | none weakened (stricter; sec. 3) |
| 60 | F7-R6.CTRL.17 | REQ:R6.CTRL.17 | pending keys R-D labels | none weakened (stricter; sec. 3) |
| 61 | F7-R6.CTRL.23 | REQ:R6.CTRL.23 | pending keys R-D labels | none weakened (stricter; sec. 3) |
| 62 | F7-R6.RULE.7 | REQ:R6.RULE.7 | pending keys S1-D2 | none weakened (stricter; sec. 3) |
| 63 | F7-R6.RULE.8 | REQ:R6.RULE.8 | pending keys S1-D2 | none weakened (stricter; sec. 3) |
| 64 | F7-R6.RULE.9 | REQ:R6.RULE.9 | pending keys S1-D2 | none weakened (stricter; sec. 3) |
| 65 | F7-R6.CTRL.24 | REQ:R6.CTRL.24 | pending keys S1-D2, R-D labels | none weakened (stricter; sec. 3) |
| 66 | F7-OBL-1 | REQ:OBL-1 | pending keys S1-D2 | none weakened (stricter; sec. 3) |
| 67 | F7-R6.REC.6 | REQ:R6.REC.6 | pending keys DI-2 | none weakened (stricter; sec. 3) |
| 68 | F7-R6.REC.7 | REQ:R6.REC.7 | pending keys DI-2 | none weakened (stricter; sec. 3) |
| 69 | F7-R6.CTRL.22 | REQ:R6.CTRL.22 | pending keys DI-2 | none weakened (stricter; sec. 3) |
| 70 | F7-R6.PUR.8 | REQ:R6.PUR.8 | pending key V5-D2 added | none weakened (stricter; sec. 3) |
| 71 | F3 | REQ:R6.PROF.9 | pending key v5.5.9 final D2 added | none weakened (neutral; sec. 3) |
| 72 | meta | EXPECTATIONS.json | record_id r6-final2-1 -> r6-final3-1 (no row changed) | none weakened (neutral; sec. 3) |
| 73 | F1 | PARAPHRASED-DECISIONS.md | each entry carries its record class and, for class (ii), the exact text of the record | none weakened (stricter or neutral; sec. 3) |
| 74 | F2 | PARAPHRASED-DECISIONS.md | V5-D2 described as the widening of `resid`; the W2 allow rules rest on no owner decision | none weakened (neutral; sec. 3) |
| 75 | F3 | PARAPHRASED-DECISIONS.md | entries v3 D1-D4, S1-D2 and v5.5.9 final D2 replace the single entry "D1-D4" | none weakened (neutral; sec. 3) |
| 76 | F4 | PARAPHRASED-DECISIONS.md | R6.DENY.1 and R6.DENY.2 removed from V5-D1 | none weakened (neutral; sec. 3) |
| 77 | F7 | PARAPHRASED-DECISIONS.md | entry DI-2 added; the requirements marked by F7 listed under their keys | none weakened (stricter; sec. 3) |

***

## 3. Safeguards, per finding

No edit weakens a safeguard. Per finding:

- F1: stricter or neutral: the attributions now state the class of each record; R6.STAT.8 can be confirmed only by the owner restating the decision, the comment holding no owner words; no check, expectation or obligation changes.
- OCFIX: neutral: the attribution of OC-1 to OC-5 is corrected; their classification as support off `main` until quoted in a record on `main` is unchanged.
- F3: neutral: labels disambiguated and decision keys corrected; no requirement content changes.
- F5: stricter: a rejection can no longer be implemented by reusing DR-2 (sec. 33, AGENTS.md sec. A.30); expectations of V4, V27, V27-glossary and V15 unchanged (checked byte for byte).
- F6: neutral to stricter: the decision space is stated completely; no resolution is chosen; the four rows stay DEFERRED and their candidates unchanged (checked byte for byte).
- F4: neutral: the requirements keep their content and controls and still take effect only by r6's adoption; only the claim that they rest on V5-D1 is removed. They are listed in FRESH-AUTHORIZATION.md so that their authorization stays explicit.
- F7: stricter: requirements whose decision basis was not shown are now marked and listed for confirmation or fresh authorization; no content changes.
- F8: neutral: Markdown rendering only; no text changes.
- F2: neutral: the description of V5-D2 in PARAPHRASED-DECISIONS.md is corrected; the design's requirements and the rule obligations of R6.DENY.5 and OBL-3 are unchanged.

Flagged for the owner (not weakened by this round, but listed in FRESH-AUTHORIZATION.md as permitting what an earlier design prohibited or narrowing a check): R6.STAT.4, R6.PUR.9, R6.PUR.11, R6.RULE.2, R6.RULE.4, R6.RULE.8, R6.DENY.5, R6.DENY.6, R6.CTRL.15, R6.PLAN.8, OBL-3, OBL-6.

***

## 4. Self-checks (before: out-final2; after: out-final3)

| Check (correct.py, parameterized) | Before | After |
|---|---|---|
| completeness: MAPPING rows not cited in DESIGN-r6.md | 0 | 0 |
| consistency: named controls without a row | 0 | 0 |
| consistency: rows naming an unknown requirement | 0 | 0 |
| consistency: rows named by no requirement | 0 | 0 |
| consistency: one-way links | 0 | 0 |
| consistency: rows with expect null | 0 | 0 |
| consistency: retired ids live (row or named control) | 0 | 0 |
| consistency: Table 17.1 ids without a row, rows missing from Table 17.1 | 0 | 0 |
| consistency: cited requirement ids that do not exist | 0 | 0 |
| consistency: cited OBL ids that do not exist | 0 | 0 |
| consistency: GATE-1 to GATE-30 rows present | 0 | 0 |
| consistency: rows with candidate expectations not DEFERRED | 0 | 0 |
| consistency: superseded names remaining (ISOLATION_REFUSED, RD2-RD5, ...) | 0 | 0 |
| consistency: paired_with naming an id that is not a row | 0 | 0 |
| coverage: non-testable requirements without verification | 0 | 0 |
| consistency: requirement ids in the text equal the requirement index | 0 | 0 |
| consistency: marked requirements in the text equal those keyed in the index | 0 | 0 |
| OC-1: OBL-16 carries no OPEN marker and no "F on main" condition | 0 | 0 |
| OC-2: OBL-26 carries no circularity marker and is not gated on adoption | 0 | 0 |
| OC-4: LC-7 expects REVIEW_REQUIRED in every case and keeps its OPEN flag | 0 | 0 |
| OC-3: rows on X_rep carry both invariants; item11-T1p does not | 0 | 0 |

| Value | Before | After | Why it changed |
|---|---|---|---|
| requirements | 427 | 427 |  |
| expectation rows | 558 | 558 |  |
| rows flagged VD-RESTORE | 217 | 217 |  |
| requirements marked pending owner confirmation | 33 | 44 | F7 marks 13 requirements and F4 unmarks 2 (33 - 2 + 13) |
| testable requirements without a control | 14 | 14 |  |
| MAPPING rows placed | 1149 | 1149 |  |
| OPEN markers in the requirement index | 3 | 3 |  |

Checks of this round:

- replay: correct.py's index rule reproduces out-final2/REQUIREMENTS.json from out-final2/DESIGN-r6.md: 0
- F5/F6: V4, V27, V27-glossary, V15 rows byte-identical to out-final2 and DEFERRED: 0
- preservation: every expectation row byte-identical to out-final2: 0
- preservation: retired list unchanged: 0
- preservation: no requirement id removed or added: 0
- preservation: sources and controls of every requirement unchanged: 0
- preservation: sections 33 and 34 unchanged: 0
- preservation: Appendix H changed only in HIST-4: 0
- preservation: MIGRATION.json unchanged: 0
- F8: design text unchanged apart from the logged edits (whitespace-normalized diff limited to edited blocks): 0
- F7/F3/F4: pending keys equal the intended map: 0
- quotes: every quotation of a comment occurs in its body: 0
- V4-COMPARISON: rule-form matches as expected: 0
- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return, no invisible formatting character, no non-ASCII space, and no non-ASCII character outside those of the inputs and the quoted comments, in any output: checked
- reproducibility: the generator re-ran itself in a separate process (`python3 -I -B`) and compared the sha256 of every output before writing; identical
- generator problems: 0

***

## 5. Remaining open items

- Requirements pending owner confirmation or fresh authorization: see FRESH-AUTHORIZATION.md (each listed with its exact wording, purpose and consequences). None is adopted by this round.
- The V4 group (V4, V27, V27-glossary, V15): deferred; the three consistent resolutions are compared in V4-COMPARISON.md. Under resolution (b1) the per-row candidate labels ("reversal adopted" for V15) no longer describe the choice and are restated at the decision; the expectations themselves are unchanged.
- S1-D3 (specify B1-B6: admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting) underlies parts of secs. 11, 13 and 16, but no inventory item cited by a requirement names it, so the attribution rule marks none. Identifying those requirements needs a mapping not made in this round.
- The sec. 33 row retiring DR-1d and DR-2 rests on V5-D1 (class (ii)); it is a table row, not a requirement, and is unmarked. It is listed in FRESH-AUTHORIZATION.md.
- Every class (i) authorization relied on authorizes drafting, correction or presentation and excludes adoption (AUTHORIZATIONS.md); every r6 requirement, marked or not, takes effect only by r6's adoption.
- Off-main support of adoption (R6.STAT.10, sec. 32 adoption trace): unchanged by this round, except that the owner corrections OC-1 to OC-5 are now attributed to #1169 comment 7163402499; they, like the other owner records, remain support off `main` until quoted with author and time in a record on `main`.
- item11-T1p, the controls that still read T1' or P, LC-7 (OC-4) and the implementation obligations of OC-3: unchanged and open, as stated in the previous correction report.

## 6. Contradictions and departures found while correcting

- The grouped presentation (group C) traced the "D1-D4" mark of R6.DENY.5 and OBL-3 to v3 D1. The attribution rule finds it through E-1021, whose label "(S1-D1, D1)" is the Stage 1 review's D1 (W1-c's allowance and the self-PASS lint, CHANGES-v5.2.md sec. 1). This round re-keys both to S1-D2 (F3). Their content still relates to v3 D1 (an item-7 restatement as a plan amendment needs a reviewed deny set); that link is not a source citation and is not marked.
- The grouped presentation cites DESIGN-v5.5.9.md by line numbers (for example 45-54, 68-73, 108-111) that do not match the records-branch copy read here (blob e5b97ef1: 40-50, 58-64, 94-98). The content is the same; this round cites the copy's lines.
- Appendix H, HIST-4 stated that the route authority of #1169 comment 7093128173 and the decisions D1-D4, V5-D1 and V5-D2 have no GitHub record. They have session-written records (class (ii)); HIST-4 is corrected (F1). This changes Appendix H, which the previous round kept unchanged; sections 33 and 34 stay unchanged.
- v5.5.9 and the inventory use "D1-D4" for both v3's open points and the owner's final decisions, and "D1-D8" for the Stage 1 corrections; R6.NOTE.13 now states the three senses (F3).
- Completeness scan of the attribution rule: after this round, 15 unmarked requirements cite inventory items containing label-like tokens. Two are R6.DENY.1 and R6.DENY.2 (F4). In the other 13 the tokens are not decision labels: "C3" in RV-056 (R6.CTRL.2) is the v2 control C3, and "D2" to "D5" in the A-items (R6.CTRL.26, R6.CTRL.27, R6.TREE.7, R6.RDIR.1, R6.RDIR.4, R6.RDIR.5, R6.RDIR.10, R6.RDIR.11, R6.RDIR.12, R6.RDIR.13, R6.VALID.4, R6.REPRO.1) are r5's directory conditions, renamed DIR2-DIR5 (sec. 34). None is marked.
- The candidate label "reversal rejected (a plan rule record restored for this form, sec. 12)" on the four V4-group rows speaks of restoring a rule for the form; under F5 the rule takes a new identifier. The label is part of the rows, which this round keeps byte-identical; it is restated, with the V15 label under (b1), when the owner decides.
