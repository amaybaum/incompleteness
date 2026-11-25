# r6, round 5: correction report

Generator: build/correct5.py (landed as generator-round5/). Applies item 2 of the owner decision of 2026-11-25T18:50:53Z (#1169 comment 7171541574, quoted in DESIGN-r6.md sec. 0.1) and nits 1 to 5 of the round-4 delta review (#1169 comment 7170390944). Preparation only: nothing is adopted, frozen, merged or executed.

## 1. Inputs

| Input | sha256 or git blob |
|---|---|
| directory at 2aec244e: AUTHORIZATIONS.md | blob b7dc931b1daa3d6996923c6c5e8bc35806ae252c |
| directory at 2aec244e: CHECKS.txt | blob 84230bd2dae6c4d8c81fa0bdacf449f725fcb603 |
| directory at 2aec244e: CONFORMANCE.md | blob 74ecf04de9e2ccd32b7ef4e83138eb49ec5955b1 |
| directory at 2aec244e: CORRECTION-REPORT-round3.md | blob 5049cc257f0521612dea25d9c565aed8b6b53b9e |
| directory at 2aec244e: CORRECTION-REPORT-round4.md | blob a24abbf05c34d7dfe3495c165368d3001b0213cf |
| directory at 2aec244e: CORRECTION-REPORT.md | blob 064a5ec624c86abd24db2249ef317bdb20787dac |
| directory at 2aec244e: DECISIONS.md | blob f02b8eebeb1b7db3acce68ac7f29c1f16c52a3cc |
| directory at 2aec244e: DESIGN-r6.md | blob b560e0a6f0a692889076eece75cf135648872c7c |
| directory at 2aec244e: EXPECTATION-SOURCES.json | blob 303f23616d571954a056d5d0bde5fde2faf1c1bc |
| directory at 2aec244e: EXPECTATIONS-REPORT.md | blob 12c3c2fad83616d7c1155e33b6b1dce389eb8f26 |
| directory at 2aec244e: EXPECTATIONS-draft.json | blob 5917b03bc7a57a6c2c517857c0e795365f5de4d3 |
| directory at 2aec244e: EXPECTATIONS.json | blob 7ae3ce0de30b959914e3cd63eec6713eb9a94413 |
| directory at 2aec244e: FINAL-REPORT.md | blob aa2f161860b40263e4614f07cfc93ca000418610 |
| directory at 2aec244e: FRESH-AUTHORIZATION.md | blob 39dfdc65290cbfca706046db2b28523fb7792e4b |
| directory at 2aec244e: GATE-draft.md | blob f35e68b9d7c15cb8b1d1cab971286d15ed06c450 |
| directory at 2aec244e: INTEGRATION-REPORT.md | blob 66bbaa563e2c6cec7a8ccc84274e4deb5babb383 |
| directory at 2aec244e: INVENTORY.json | blob 95d693f82be5a121049b5f2e73ca5754d88bddd9 |
| directory at 2aec244e: LANDING-MANIFEST.md | blob 07c434a42f0ca14553c7b5682f0bf8a1c8f8e1d7 |
| directory at 2aec244e: MAPPING-CHECK.txt | blob c0644e12d0e4bbe67936b24bf3493ebc95d74dc2 |
| directory at 2aec244e: MAPPING.json | blob f5d35cb490b0d8925ea7e242446837d567768021 |
| directory at 2aec244e: MIGRATION.json | blob 4ed66d207198ac12e5b7adcc637ce9325d21199c |
| directory at 2aec244e: OUTLINE.md | blob 81aec76de8dca743467bc64ffd78d81f69eefb19 |
| directory at 2aec244e: PARAPHRASED-DECISIONS.md | blob c37ba6f982433ffafe8ed00b9cdf9bd10d45f40d |
| directory at 2aec244e: PENDING-33.md | blob 1e09093faf934094dc201c045468d7f96e77ffc4 |
| directory at 2aec244e: RE2-ROWS.md | blob cde0e3f8b7c357c8c87ec0ee62409fcc35a78c86 |
| directory at 2aec244e: REQUIREMENTS.json | blob 3fb0ce009fd4a7414defaf9cdff3d4d9eee39ccb |
| directory at 2aec244e: RESIDUAL-2.md | blob feb9e27cc69fed3e9b90a2147d3ea1272db2dd47 |
| directory at 2aec244e: RESIDUAL.md | blob 6932490ae1db2a1c2375f91359e9ace45fddab33 |
| directory at 2aec244e: REVIEW-r6-round2.md | blob 654bd76776042e1d2a135c8b15d2b447df0ef00a |
| directory at 2aec244e: REVIEW-r6-round3.md | blob ed0dfb3c5a70d74c256bb8fbb34ece43cc735039 |
| directory at 2aec244e: V4-COMPARISON.md | blob 4efb9826e59b3c58d4209f89fb6ef72549e16bda |
| directory at 2aec244e: generator-round2/PROVENANCE.json | blob aa22337f3ebcff9857f4fc243ecb4138ae627526 |
| directory at 2aec244e: generator-round2/comments-1169.json | blob 318fe33d6e7393184198f7e5af9f1272ad6a991e |
| directory at 2aec244e: generator-round2/correct.py | blob e846064c295cadd999317cd83e9a63386269e29d |
| directory at 2aec244e: generator-round2/correct2.py | blob 809afa8448996c989879e285e6b66bb10033bd1f |
| directory at 2aec244e: generator-round2/report_text.py | blob f71d4c6d2ecf0f9c92a9b5f282592fdcd20c53aa |
| directory at 2aec244e: generator-round2/text2.py | blob 3c469f71083f56c1d328cbcfffd8e529c0d34204 |
| directory at 2aec244e: generator-round3/comments-round3.json | blob 7e4467626c700c23906e2e807dcfb8f55b9e0206 |
| directory at 2aec244e: generator-round3/correct3.py | blob f7a8aa4be68b6b6874e819fe0d9808102da0ef0d |
| directory at 2aec244e: generator-round3/review-r6-round2.md | blob 6f172c4dd1b6e9f57ca969b5e422afb1aa906d1e |
| directory at 2aec244e: generator-round4/correct4.py | blob c9a1c5afe8ad9443da854c71ac5362c19a529194 |
| directory at 2aec244e: generator-round4/owner-decisions-A1-A5.json | blob 4e54a7017a26890373d9077bedff1adc5611382f |
| directory at 2aec244e: generator-round4/records-1169.json | blob 1092e1e4f690fa16a61fc884711d70306441cb08 |
| directory at 2aec244e: generator-round4/review-r6-round3.md | blob 4dbaa046434e3b782c31b07b44b084bab872a2e9 |
| directory at 2aec244e: generator-round4/tree-c33d5b71.json | blob bbb88b7d08977326672b4482ce49bbf59d1e9869 |
| build/inputs/tree-2aec244e.json | 937e8885786f33995ea93c0bf0d865cbd99679e95431402d93c36fb044b9dae0 |
| build/inputs/records-1169-round5.json | 20e1b1931a7f3d2fde178128d721df793bcf822f4006f9f1c7910f8a53026218 |
| build/inputs/edits_check.py | 2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c |

generator-round4 is executed in-process up to its report; it checks its own inputs against c33d5b71 and regenerated 11 outputs, each byte-identical to 2aec244e.

## 2. Edits

| # | Item | Target | Edit |
|---|---|---|---|
| 1 | D1-D3 | sec. 0.1 | the owner decision of 2026-11-25T18:50:53Z quoted byte-exact (opening line, item 2, general constraints), with how r6 applies it |
| 2 | NIT2 | sec. 0.1 | text edit |
| 3 | D1 | sec. 32 adoption trace | text edit |
| 4 | D3 | sec. 32 adoption trace | statements row: unsupported on main, named in the list of historical statements |
| 5 | D3 | sec. 32 adoption trace | text edit |
| 6 | D3 | sec. 32 | list of historical statements: 53 rows, each unsupported on main |
| 7 | D3 | OBL-26 | text edit |
| 8 | NIT1 | OBL-28 | C-4: the TR45-opC runner left to the tool revision |
| 9 | D1-D3 | AUTHORIZATIONS.md | entry for the owner decision of 2026-11-25T18:50:53Z added to sec. 1 |
| 10 | meta | AUTHORIZATIONS.md | sec. 5: the round-4 delta review record |
| 11 | D1-D3 | LANDING-MANIFEST.md | regenerated: 32 landed files, 17 left to history, 306 references classified |
| 12 | NIT3 | LANDING-MANIFEST.md | comment ids matched only outside longer hexadecimal strings; the four false rows dropped (the three the review names, and 7156468072, of the same kind) |
| 13 | NIT4 | LANDING-MANIFEST.md | note on the generator programs completed with the references not in the table |
| 14 | NIT5 | LANDING-MANIFEST.md | 86d79863: not a reference |
| 15 | D2 | LANDING-MANIFEST.md | generator-round4 and generator-round5 land; the caveat on generator-round4 replaced by the decision |

Items: D1, `edits_check.py` lands as `inputs/edits_check.py`; D2, generator-round4 and generator-round5 land; D3, the historical statements narrowed and named; NIT1 to NIT5, the round-4 delta review's nits (nit 1 only as the C-4 sentence; its runner is left to the tool revision).

## 3. Values, before (round 4) and after

| Value | Before | After |
|---|---|---|
| requirements | 428 | 428 |
| expectation rows | 558 | 558 |
| rows flagged VD-RESTORE | 217 | 217 |
| requirements marked pending owner confirmation | 0 | 0 |
| testable requirements without a control | 14 | 14 |
| MAPPING rows placed | 1149 | 1149 |
| OPEN markers in the requirement index | 2 | 2 |
| rows with expect DEFERRED | 0 | 0 |
| historical statements named unsupported (rows of the list) | 0 | 53 |
| references classified in the manifest | 268 | 306 |
| references classified support off main relied on by adoption | 3 | 0 |
| files that land (with this manifest) | 28 | 32 |
| files left to Git history | 16 | 17 |

## 4. Self-checks

Round-3 checks (run_checks of correct3.py), before (round-4 outputs) and after:

| Check | Before | After |
|---|---|---|
| completeness: MAPPING rows not cited in DESIGN-r6.md | pass | pass |
| consistency: named controls without a row | pass | pass |
| consistency: rows naming an unknown requirement | pass | pass |
| consistency: rows named by no requirement | pass | pass |
| consistency: one-way links | pass | pass |
| consistency: rows with expect null | pass | pass |
| consistency: retired ids live (row or named control) | pass | pass |
| consistency: Table 17.1 ids without a row, rows missing from Table 17.1 | pass | pass |
| consistency: cited requirement ids that do not exist | pass | pass |
| consistency: cited OBL ids that do not exist | pass | pass |
| consistency: GATE-1 to GATE-30 rows present | pass | pass |
| consistency: rows with candidate expectations not DEFERRED | pass | pass |
| consistency: superseded names remaining (ISOLATION_REFUSED, RD2-RD5, ...) | pass | pass |
| consistency: paired_with naming an id that is not a row | pass | pass |
| coverage: non-testable requirements without verification | pass | pass |
| consistency: requirement ids in the text equal the requirement index | pass | pass |
| consistency: marked requirements in the text equal those keyed in the index | pass | pass |
| OC-1: OBL-16 carries no OPEN marker and no "F on main" condition | pass | pass |
| OC-2: OBL-26 carries no circularity marker and is not gated on adoption | pass | pass |
| OC-4: LC-7 expects REVIEW_REQUIRED in every case and keeps its OPEN flag | pass | pass |
| OC-3: rows on X_rep carry both invariants; item11-T1p does not | pass | pass |

Round-4 checks (generator-round4's own check code, run on the round-4 outputs and on the round-5 outputs):

| Check | Before | After |
|---|---|---|
| A1: the three rows keep expect, restored, requirements, runner and procedure; NOT RUN admitted with the deferral | pass | pass |
| A1/A2: every other row byte-identical; order, count and retired unchanged | pass | pass |
| A1: OBL-17 gates no step; GATE.15 and CTRL.5 admit NOT RUN for TR45-opB | pass | pass |
| A2: item11-T1p differs only in its two flags, both "candidate evidence only, not acceptance support" | pass | pass |
| A3: the owner's wording quoted byte-exact in sec. 0.1; R6.STAT.8 cites it | pass | pass |
| A4: the 53 carry the confirmation once; no pending mark or key remains | pass | pass |
| CLOSE: R6.TREE.12 condition is the owner-approved restatement of LC-7 | pass | pass |
| preservation: requirement ids unchanged | pass | pass |
| preservation: sources, controls and OPEN markers of every requirement equal the index | pass | pass |
| preservation: sources and controls unchanged from round 3 | pass | pass |
| preservation: requirement blocks without a logged edit unchanged (whitespace-normalized) | pass | pass |
| preservation: sections 33, 34 and Appendix H unchanged | pass | pass |
| FRESH-AUTHORIZATION.md: every quoted requirement wording equals the design | pass | pass |
| REVIEW-r6-round3.md holds the reviewer text verbatim | pass | pass |
| manifest: every reference classified; landed and dropped partition the 37 files | pass | pass |

Round-5 checks:

| Check | Result |
|---|---|
| inputs: every round-4 output and generator-round4 file equals its git blob at 2aec244e; edits_check.py is blob 1153e039 with sha256 2856e58c...d98c | pass |
| generator-round4 regenerates every round-4 output byte-identical to 2aec244e | pass |
| records: the decision lines quoted occur verbatim in comment 7171541574; the review text has the sha256 its record states | pass |
| D1: edits_check.py lands byte-exact; the 12 requirement blocks and REQUIREMENTS.json unchanged | pass |
| D1: no reference is support off main relied on by adoption; the P rows are support on main once landed | pass |
| D2: generator-round4 lands byte-identical to 2aec244e, generator-round5 lands, no merge caveat remains | pass |
| D3: every passage of the round-4 design found by the scan is listed or excluded with a reason; no stale entry | pass |
| D3: the list of unsupported statements is the same in DESIGN-r6.md sec. 32 and LANDING-MANIFEST.md sec. 4 | pass |
| D3: every row of the manifest naming the tool commit, the run or `T1'` as support off main names the list | pass |
| NIT3: the hardened comment pattern drops exactly the four false ids (three named by the review, and 7156468072), and no other; none is classified a comment | pass |
| NIT4: the references of correct4.py and correct5.py outside the table are listed in the note | pass |
| NIT5: 86d79863 is classified "not a reference" | pass |
| NIT1/NIT2: the C-4 sentence and the A3 note applied once each | pass |
| preservation: EXPECTATIONS.json byte-identical (rows, controls, expectations); requirement count and ids unchanged | pass |
| preservation: requirement blocks changed only where logged (OBL-26, OBL-28) | pass |
| preservation: unchanged outputs byte-identical to 2aec244e | pass |
| manifest: every reference classified; landed and dropped partition the 45 files | pass |

## 5. Historical statements left unsupported

Named in DESIGN-r6.md sec. 32 and LANDING-MANIFEST.md sec. 4 (53 rows): R6.PUR.12; R6.PIPE.3; R6.ANCH.10; R6.ANCH.12; R6.HP.7; R6.OUT.4; R6.OUT.18; R6.OUT.24; R6.SPLIT.3; R6.RULE.11; R6.RULE.12; R6.REC.20; R6.HIT.2; R6.CLASS.1; R6.CLASS.11; R6.GATE.7; R6.GATE.10; R6.CTRL.19; R6.CTRL.25; R6.CTRL.27; R6.CTRL.29; R6.CTRL.30; R6.TREE.13; R6.RDIR.7; R6.RECON.11; OBL-21; OBL-24; OBL-28; sec. 34, migration table; R6.EVID.6; R6.GATE.16; R6.RECON.21; OBL-13; R6.NOTE.3; R6.SPLIT.1; R6.PLAN.8; R6.EVID.4; R6.EVID.5; R6.EVID.7; R6.EVID.8; OBL-7; OBL-23; Appendix H, HIST-11; Appendix H, HIST-15; Appendix H, HIST-16; Appendix H, HIST-20; Appendix H, HIST-21; Appendix H, HIST-23; EXPECTATIONS.json, `reference` fields (106 rows); EXPECTATIONS.json, `source` fields (107 rows); EXPECTATIONS.json, `flags` (1 row); FRESH-AUTHORIZATION.md; V4-COMPARISON.md.

Passages found by the scan and excluded, with the reason: R6.STAT.3 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); R6.NOTE.7 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); R6.OUT.12 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); R6.REC.18 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); R6.REPRO.1 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); OBL-16 (the run variable `T` (R6.NOTE.7), not the tool commit a3799244); HIST-3 (v6.0b's rule that the run's tool commit be on `main`'s first-parent chain (the run variable)); R6.STAT.5 (a rule for differences from the implementation; states no content of it); R6.CLASS.7 (a rule for differences from the tool commit; states no content of it); R6.STAT.10 (states that adoption uses none of this content); R6.STAT.9 (names the `T1'` cases of sec. 6 as a topic; states no content); sec. 0.1 para 5 (owner decision 4 on item11-T1p's earlier figure (the figure is listed under OBL-23)); R6.CTX.1 (a rule for the counts at `T1'`; states none); R6.PROF.11 (excludes `T1'` as a source); R6.CTRL.11 (names `T1'` as RT-M's input (a control input; adoption-trace row of controls reading `T1'` or `P`)); R6.SPLIT.2 (classifies R6.SPLIT.1's measurement sentence as history (R6.SPLIT.1 is listed)); R6.ANCH.18 ("the implementation" in general; states nothing the tool commit does); R6.GATE.9 ("the implementation" in general; states nothing the tool commit does); R6.GATE.11 ("the implementation" in general; states nothing the tool commit does); R6.EVID.1 ("the implementation" in general; states nothing the tool commit does); R6.EVID.2 ("the implementation" in general; states nothing the tool commit does); R6.OUT.13 (a CI run in general, not CI run 45569710442); R6.OUT.14 (a CI run in general, not CI run 45569710442); R6.REC.6 (a CI run in general, not CI run 45569710442); R6.DELEG.13 (a CI run in general, not CI run 45569710442); R6.REPRO.2 (a CI run in general, not CI run 45569710442); R6.GATE.13 (gate self-test cases (survivors in general)); R6.CTRL.1 (the runner-cite convention of Table 17.1 (provenance; adoption-trace row of the runner cites)); sec. 32 para 1 (the gates of sec. 32 (implementation certification in general)); sec. 32 para 2 (the gates of sec. 32 (implementation certification in general)); OBL-26 (classifies the conformance assessment as provenance and states the certification gate; its pointer to the statements that describe the tool commit names this list); and every row of the obligation table and the adoption trace of sec. 32 (a classification, not a statement of content).

## 6. Outputs

| File | sha256 |
|---|---|
| DESIGN-r6.md | aac0f20ac75b6c499161d512e26dc32fd597624d88d311f1bbc1cb87e17a18e3 |
| AUTHORIZATIONS.md | 6a7e01ac906512c420db05ff0f07a54091978d6a257488ad4a3dc3d4d97c1238 |
| FRESH-AUTHORIZATION.md | c80508e3c9ae7872fbee427d51ba37080749d242ed8f14e17952982e2e20f217 |
| LANDING-MANIFEST.md | e01677b58922ba1140dd52addb71ffb7ad42183a33547b7044ca4bc1aef4bf9b |
| EXPECTATIONS.json | a24a7b2bcaf5cdaeee6ca791cd4af11d1787043252d96bcb512825c9df17e847 |
| REQUIREMENTS.json | dbdba73379e99c7a4d66228aa7a60fe64af7154efbe9c836b814c768f6988167 |
| PARAPHRASED-DECISIONS.md | 05602f3ec2f971ad860bc864a2ad8fce2d115948b0d3ac369ef17874746b65ce |
| REVIEW-r6-round3.md | 546188124cfe34c3924e032879c4bb1ae80ea17e619586283927840ccdd6fd99 |
| MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| V4-COMPARISON.md | 76970c73eeb45d8f81c4665b8e7b72e90f29ecfe2747cf7b0440a697d5bd9edf |
| REVIEW-r6-round2.md | 8875ffd240989348f2c647b3187146e24c5454b5edc70c81817c9263a46c9912 |
| inputs/edits_check.py | 2856e58c65817865a57fc34851ab3319d1cdda86f72f76a77fc6c063b2f1d98c |

EXPECTATIONS.json, REQUIREMENTS.json, PARAPHRASED-DECISIONS.md, REVIEW-r6-round3.md, MIGRATION.json, V4-COMPARISON.md and REVIEW-r6-round2.md are written unchanged; `inputs/edits_check.py` is written byte-exact. The generator re-runs itself in a separate process and writes only if every output's sha256 is equal.

## 7. Before adoption

- One focused independent review of this revision (owner decision of 2026-11-25T18:50:53Z, item 2).
- The landing: the owner-approved merge of the files of LANDING-MANIFEST.md sec. 1, keeping the branch history (AGENTS.md sec. A.50 item 1); the statements of its sec. 4 land named as unsupported.
- Design adoption: a separate owner approval.
