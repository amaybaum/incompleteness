# r6 correction report, third round: final text-only revision (owner decisions 1-5 of 2026-11-25)

Deterministic revision by `build/correct3.py`, which reads the round-2 outputs (read only), the review text recorded at #1169 comment 7166666428 and the owner's decisions recorded at #1169 comment 7166844576 (read with GET requests), and applies the logged edits below. Each edit carries the owner decision (D1-D5) or the review finding (R1-R6, N1-N6) it applies, or `meta`. Authorization, quoted: #1169 comment 7166844576 (2026-11-25T15:26:24Z): "This authorizes the final design revision and its review, not adoption, implementation, freezing, trial execution or merging.". Decision 5 authorizes this revision and one bounded delta review, not adoption, implementation, freezing, trial execution or merging. No governance rule is amended, no exception is created, no expectation changes except decision 3's selection, and r6 stays a draft. No git or GitHub write was made.

Items applied:

- D1: Decision 1: 22 + 19 requirements confirmed; R6.STAT.4 and R6.EVID.5 scope statements without a check of their own.
- D1-scope: Decision 1: the two scope statements.
- D1-defer: Decision 1: R6.OUT.15 deferred with the `replay` mode of R6.REC.24 and TR45-opB; accountable Issue #1169; text kept.
- D2: Decision 2: the reviewer's classes of the 12 flagged requirements accepted.
- D3: Decision 3: resolution (a) for V4, V27, V27-glossary and V15; candidate labels restated; the owner's caveat quoted; R6.PUR.9's blocker discharged by the decision text.
- D4i: Decision 4 (i): the review record REVIEW-r6-round2.md; adoption needs the landing pull request's separate merge approval.
- D4ii: Decision 4 (ii): the LC-7 regeneration and byte-comparison procedure, R6.TREE.19, for the delta review.
- D4iii: Decision 4 (iii): the T1' figure of item11-T1p is candidate evidence only.
- D5: Decision 5: decisions 1-4 quoted into r6 (sec. 0.1); the bounded scope of this revision.
- D5-S1D3: Decision 5: the requirements resting on S1-D3 identified, listed and marked pending for the adoption decision.
- R1: R1: the 7130449822 adoption of v6.0e noted on R6.REC.18 to R6.REC.22 (and R6.STAT.4, R6.PUR.11) and on the line 31/54 keys.
- R3: R3: non-confirmation leaves a requirement pending; withdrawal is a separate explicit owner choice.
- R4: R4: the 4677-blob figure marked provenance; RT-DR's re-check under (b) stated, moot under (a).
- R6: R6: R6.A1CFG.7 flagged as narrowing, class (c), protected by R6.GATE.9 and OBL-6.
- N1: N1: what each class (i) record authorizes; none adopts r6.
- N2: N2: V5-D1's consequence attributed to v6.0e's measurement; 7099655517's coverage-limitation decision named as R6.PUR.8's direct basis.
- N4: N4: the blocker's discharge stated for every resolution.
- N5: N5: "r6 expects ..., and no such rule is required".
- N6: N6: HIST-4 disambiguated (the E-008 decisions of 2026-11-24; DI-2's class (ii) record).
- meta: Mechanical consequences: record id, index fields, blank lines.
- R2: addressed by decision 5 and the S1-D3 identification (FRESH-AUTHORIZATION.md, sec. 3).
- R5: R6.STAT.10 and sec. 0.1 state that one bounded delta review covers this revision before adoption.
- N3: see sec. 6.

***

## 1. Inputs and outputs (sha256)

| Input (read only) | In the directory or record | sha256 |
|---|---|---|
| out-final3/DESIGN-r6.md | directory file DESIGN-r6.md | 5a17b3069bbfaac24b805293443645b0ac4145f6002d6450a3c9247b7682ad14 |
| out-final3/EXPECTATIONS.json | directory file EXPECTATIONS.json | acd321bca3853d0a4d873d5171bda1b091acb9fce86d5c3e82da14b763db0e9a |
| out-final3/REQUIREMENTS.json | directory file REQUIREMENTS.json | 6a0beaabec0dbba4e261837246d614ac9cf5fab2dfc5e42ffb07fd5516742ef9 |
| out-final3/MIGRATION.json | directory file MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| out-final3/PARAPHRASED-DECISIONS.md | directory file PARAPHRASED-DECISIONS.md | 00b4bb82afb40cbd92ff7ff0d6e68b338c96ec855c6d85f9f64c70783419774a |
| out-final3/AUTHORIZATIONS.md | directory file AUTHORIZATIONS.md | afec2e717d359a3a949145ce448366b09c053525f148a08b259d1b3bb4923024 |
| out-final3/FRESH-AUTHORIZATION.md | directory file FRESH-AUTHORIZATION.md | 6ad128fcaf4fa7c722bb29427fae9db0097d44f52232d0c057655eef0ceb2cb7 |
| out-final3/V4-COMPARISON.md | directory file V4-COMPARISON.md | 9ef12011b8613cc8e3133ee522ec61fc816e34bd7a17d85dd2e75031d29df405 |
| out-final3/CORRECTION-REPORT.md | directory file CORRECTION-REPORT.md | a26fe36ba0799f0a5c0ad4186d197c894bd9e568717149e27b60b0fb692b5980 |
| out-final3/build/text2.py | generator-round2/text2.py | b9002bd5486da16f2d3ce1cabe659c951efdafeaa643af5ef72608803947ee30 |
| out-final3/build/correct2.py | generator-round2/correct2.py (not executed; its functions are restated here) | 2599f03dd99ca9bcc9bfaf47179b45014b91786ae1c23652c7a95074ec4006f6 |
| gh7/sel.json | generator-round2/comments-1169.json | af740cc18fa630358aa618c585508439bde4b8fb7d426ecd6808faa5e95db1e6 |
| MAPPING.json | directory file MAPPING.json | bd1a8657961fd659b29980178781a7f30fd6e5b53da9a734db28a20130c9ff85 |
| INVENTORY.json | directory file INVENTORY.json | 42d44fb0624e82fb334d4feeeaceb7787c4309dfde2f52e373e208fe11d0f5dd |
| out-final4/build/inputs/review-r6-round2.md | the reviewer text of #1169 comment 7166666428 | f09d7cb057cd33bddc13a375960305b0a8956b8fd0bc7fe2987cd4d6f0f19619 |
| out-final4/build/inputs/comments-round3.json | #1169 comments 7166666428 and 7166844576 (GET; body, user.login, created_at) | 46619e1a198d7c7633c135d3da79b4f702746f3500d7a0e9ada9b7b0423df00b |

| Output | sha256 |
|---|---|
| DESIGN-r6.md | ff950aecf15bdef20962957fe5811b7594d77bdb4674139e837d43933dae4598 |
| EXPECTATIONS.json | f49ba37a0b64b262cfa44ca566276707e4554f63e08d1c12ef323599b9c0443f |
| REQUIREMENTS.json | 00025962ea375bc436674faf361745f206b6899c3b14560af7637091e6e5892b |
| MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| PARAPHRASED-DECISIONS.md | 29aa08611c4f984288dfd08063a8fe138a12ec16fdc677c9d848655a27b7b123 |
| AUTHORIZATIONS.md | 8c13e385adb0ded5169453f8d8f2ace33af2b5c15984a1fa65215a3d00ac03f4 |
| FRESH-AUTHORIZATION.md | e25d41bb4f4f45d9c03f62ac9e8105db43fc84a8c153f9f5eed8a59b8c7a8ca0 |
| V4-COMPARISON.md | 76970c73eeb45d8f81c4665b8e7b72e90f29ecfe2747cf7b0440a697d5bd9edf |
| REVIEW-r6-round2.md | 8875ffd240989348f2c647b3187146e24c5454b5edc70c81817c9263a46c9912 |
| CORRECTION-REPORT.md | a26fe36ba0799f0a5c0ad4186d197c894bd9e568717149e27b60b0fb692b5980 |
| CORRECTION-REPORT-round3.md | this file (its digest is reported by the generator run) |

CORRECTION-REPORT.md and MIGRATION.json are copied byte-identical from the round-2 outputs.

***

## 2. Edits applied

| # | Item | Target | Edit | Safeguard |
|---|---|---|---|---|
| 1 | D1-scope | R6.STAT.4 | pending mark replaced: scope statement | neutral: decision 1; no check removed (GATE-16 stays named by R6.EVID.5 and its other requirements) |
| 2 | D1 | R6.STAT.8 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 3 | D1 | R6.PUR.8 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 4 | D1 | R6.PUR.9 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 5 | D1 | R6.PUR.11 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 6 | D1 | R6.ANCH.14 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 7 | D1 | R6.CTX.1 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 8 | D1 | R6.CTX.4 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 9 | D1 | R6.CTX.12 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 10 | D1 | R6.OUT.14 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 11 | D1-defer | R6.OUT.15 | pending mark replaced: deferred | owner-decided deferral; the text, the rows TR45-opB and TR45 and every other check are kept |
| 12 | D1 | R6.PROF.9 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 13 | D1 | R6.RULE.2 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 14 | D1 | R6.RULE.4 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 15 | D1 | R6.RULE.7 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 16 | D1 | R6.RULE.8 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 17 | D1 | R6.RULE.9 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 18 | D1 | R6.REC.6 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 19 | D1 | R6.REC.7 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 20 | D1 | R6.REC.14 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 21 | D1 | R6.REC.18 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 22 | D1 | R6.REC.19 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 23 | D1 | R6.REC.20 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 24 | D1 | R6.REC.21 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 25 | D1 | R6.REC.22 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 26 | D1 | R6.REC.24 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 27 | D1 | R6.DENY.5 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 28 | D1 | R6.DENY.6 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 29 | D1 | R6.CTRL.7 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 30 | D1 | R6.CTRL.14 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 31 | D1 | R6.CTRL.15 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 32 | D1 | R6.CTRL.17 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 33 | D1 | R6.CTRL.19 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 34 | D1 | R6.CTRL.22 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 35 | D1 | R6.CTRL.23 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 36 | D1 | R6.CTRL.24 | pending mark replaced: confirmed (reliable verification) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 37 | D1 | R6.PLAN.8 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 38 | D1 | R6.A1CFG.7 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 39 | D1 | R6.EVID.4 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 40 | D1-scope | R6.EVID.5 | pending mark replaced: scope statement | neutral: decision 1; no check removed (GATE-16 stays named by R6.EVID.5 and its other requirements) |
| 41 | D1 | OBL-1 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 42 | D1 | OBL-3 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 43 | D1 | OBL-6 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 44 | D1 | OBL-15 | pending mark replaced: confirmed (valid retirement) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 45 | D1-defer | R6.REC.24 | replay mode marked deferred | owner-decided deferral; the text, the rows TR45-opB and TR45 and every other check are kept |
| 46 | D3 | R6.PUR.9 | status: decided (a) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 47 | D3 | R6.PUR.9 | options stated as the decision space | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 48 | D3 | R6.PUR.9 | decision (a) recorded with the owner's words and caveat; outstanding-evidence blocker discharged by the decision text | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 49 | D3 | R6.DENY.6 | status: confirmed (a) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 50 | D3 | R6.DENY.6 | V5-D1 accepted by decision 3 | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 51 | D3 | R6.DENY.6 | deferral replaced by the decision | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 52 | D3 | R6.CTRL.15 | reversal accepted; alternatives stated as not chosen | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 53 | D3 | R6.CTRL.15 | alternatives in the past conditional | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 54 | D3 | OBL-6 | discharge: decision 3 and the rule records at F | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 55 | D3 | R6.A1CFG.7 | S13 counts the four rows (the temporary narrowing of R6 ends) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 56 | D3 | R6.CTRL.28 | four rows decided | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 57 | D3 | sec. 32 table, OBL-6 | text edit (1 occurrence(s)) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 58 | D4iii | R6.EVID.4 | item11-T1p: candidate evidence only | stricter: the T1' figure supports no acceptance |
| 59 | D4iii | R6.EVID.8 | item11-T1p: candidate evidence only | stricter: the T1' figure supports no acceptance |
| 60 | D4iii | R6.CTRL.19 | T1' figure: candidate evidence only | stricter: the T1' figure supports no acceptance |
| 61 | D4iii | OBL-23 | owner question answered: candidate evidence only | stricter: the T1' figure supports no acceptance |
| 62 | D4iii | OBL-23 | discharge for item11-T1p | stricter: the T1' figure supports no acceptance |
| 63 | D4iii | OBL-23 | OPEN marker removed: the gap is closed by narrowing the claim (AGENTS.md sec. A.42 item 8), as decision 4 (iii) directs | stricter: the T1' figure supports no acceptance |
| 64 | D4iii | sec. 32 table, OBL-23 | text edit (1 occurrence(s)) | stricter: the T1' figure supports no acceptance |
| 65 | D4iii | sec. 32 adoption trace, item11-T1p | text edit (1 occurrence(s)) | stricter: the T1' figure supports no acceptance |
| 66 | D4i | R6.STAT.10 | review record, delta review and separate merge approval stated (D4 (i), R5) | neutral or stricter: separate merge approval stated |
| 67 | D4i | sec. 32 adoption trace, R6.STAT.10 | text edit (1 occurrence(s)) | neutral or stricter: separate merge approval stated |
| 68 | D5 | sec. 32 adoption trace, owner decisions | text edit (1 occurrence(s)) | neutral: quotation and scope |
| 69 | D4ii | R6.TREE.12 | points to the procedure; REVIEW_REQUIRED kept until it is reviewed | stricter: LC-7 stays REVIEW_REQUIRED until the delta review accepts the procedure |
| 70 | D4ii | R6.TREE.19 (new, after R6.TREE.12) | text edit (1 occurrence(s)) | stricter: LC-7 stays REVIEW_REQUIRED until the delta review accepts the procedure |
| 71 | N6 | Appendix H HIST-4 | text edit (1 occurrence(s)) | neutral |
| 72 | D5-S1D3 | R6.OUT.12 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 73 | D5-S1D3 | R6.REC.5 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 74 | D5-S1D3 | R6.REC.13 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 75 | D5-S1D3 | R6.REC.16 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 76 | D5-S1D3 | R6.REC.17 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule C) | stricter: 50 requirements marked pending for the adoption decision |
| 77 | D5-S1D3 | R6.DELEG.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 78 | D5-S1D3 | R6.DELEG.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 79 | D5-S1D3 | R6.DELEG.3 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 80 | D5-S1D3 | R6.DELEG.4 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 81 | D5-S1D3 | R6.DELEG.5 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 82 | D5-S1D3 | R6.DELEG.6 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 83 | D5-S1D3 | R6.DELEG.7 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 84 | D5-S1D3 | R6.DELEG.10 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 85 | D5-S1D3 | R6.DELEG.12 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 86 | D5-S1D3 | R6.DELEG.13 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 87 | D5-S1D3 | R6.DELEG.15 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 88 | D5-S1D3 | R6.DELEG.16 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 89 | D5-S1D3 | R6.DELEG.18 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 90 | D5-S1D3 | R6.GATE.5 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 91 | D5-S1D3 | R6.GATE.7 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 92 | D5-S1D3 | R6.GATE.8 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 93 | D5-S1D3 | R6.GATE.9 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 94 | D5-S1D3 | R6.GATE.15 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 95 | D5-S1D3 | R6.CTRL.4 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 96 | D5-S1D3 | R6.CTRL.5 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 97 | D5-S1D3 | R6.CTRL.20 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 98 | D5-S1D3 | R6.CTRL.25 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 99 | D5-S1D3 | R6.PLAN.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 100 | D5-S1D3 | R6.PLAN.6 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 101 | D5-S1D3 | R6.PLACE.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 102 | D5-S1D3 | R6.PLACE.4 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 103 | D5-S1D3 | R6.TREE.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 104 | D5-S1D3 | R6.TREE.10 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 105 | D5-S1D3 | R6.TREE.18 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 106 | D5-S1D3 | R6.RDIR.13 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 107 | D5-S1D3 | R6.CORE.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 108 | D5-S1D3 | R6.CORE.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 109 | D5-S1D3 | R6.CORE.3 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 110 | D5-S1D3 | R6.CORE.4 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 111 | D5-S1D3 | R6.CORE.5 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 112 | D5-S1D3 | R6.CORE.6 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 113 | D5-S1D3 | R6.CFG.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 114 | D5-S1D3 | R6.CFG.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 115 | D5-S1D3 | R6.CFG.3 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 116 | D5-S1D3 | R6.CFG.8 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 117 | D5-S1D3 | R6.ADAPT.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule A) | stricter: 50 requirements marked pending for the adoption decision |
| 118 | D5-S1D3 | R6.A1CFG.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 119 | D5-S1D3 | R6.A1CFG.2 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 120 | D5-S1D3 | R6.VALID.3 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 121 | D5-S1D3 | R6.REPRO.1 | marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." (rule B) | stricter: 50 requirements marked pending for the adoption decision |
| 122 | D5 | sec. 0.1 (new) | text edit (1 occurrence(s)) | neutral: quotation and scope |
| 123 | D5-S1D3 | REQ:R6.OUT.12 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 124 | D5-S1D3 | REQ:R6.REC.5 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 125 | D5-S1D3 | REQ:R6.REC.13 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 126 | D5-S1D3 | REQ:R6.REC.16 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 127 | D5-S1D3 | REQ:R6.REC.17 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 128 | D5-S1D3 | REQ:R6.DELEG.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 129 | D5-S1D3 | REQ:R6.DELEG.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 130 | D5-S1D3 | REQ:R6.DELEG.3 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 131 | D5-S1D3 | REQ:R6.DELEG.4 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 132 | D5-S1D3 | REQ:R6.DELEG.5 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 133 | D5-S1D3 | REQ:R6.DELEG.6 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 134 | D5-S1D3 | REQ:R6.DELEG.7 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 135 | D5-S1D3 | REQ:R6.DELEG.10 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 136 | D5-S1D3 | REQ:R6.DELEG.12 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 137 | D5-S1D3 | REQ:R6.DELEG.13 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 138 | D5-S1D3 | REQ:R6.DELEG.15 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 139 | D5-S1D3 | REQ:R6.DELEG.16 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 140 | D5-S1D3 | REQ:R6.DELEG.18 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 141 | D5-S1D3 | REQ:R6.GATE.5 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 142 | D5-S1D3 | REQ:R6.GATE.7 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 143 | D5-S1D3 | REQ:R6.GATE.8 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 144 | D5-S1D3 | REQ:R6.GATE.9 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 145 | D5-S1D3 | REQ:R6.GATE.15 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 146 | D5-S1D3 | REQ:R6.CTRL.4 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 147 | D5-S1D3 | REQ:R6.CTRL.5 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 148 | D5-S1D3 | REQ:R6.CTRL.20 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 149 | D5-S1D3 | REQ:R6.CTRL.25 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 150 | D5-S1D3 | REQ:R6.PLAN.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 151 | D5-S1D3 | REQ:R6.PLAN.6 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 152 | D5-S1D3 | REQ:R6.PLACE.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 153 | D5-S1D3 | REQ:R6.PLACE.4 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 154 | D5-S1D3 | REQ:R6.TREE.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 155 | D5-S1D3 | REQ:R6.TREE.10 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 156 | D5-S1D3 | REQ:R6.TREE.18 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 157 | D5-S1D3 | REQ:R6.RDIR.13 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 158 | D5-S1D3 | REQ:R6.CORE.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 159 | D5-S1D3 | REQ:R6.CORE.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 160 | D5-S1D3 | REQ:R6.CORE.3 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 161 | D5-S1D3 | REQ:R6.CORE.4 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 162 | D5-S1D3 | REQ:R6.CORE.5 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 163 | D5-S1D3 | REQ:R6.CORE.6 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 164 | D5-S1D3 | REQ:R6.CFG.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 165 | D5-S1D3 | REQ:R6.CFG.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 166 | D5-S1D3 | REQ:R6.CFG.3 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 167 | D5-S1D3 | REQ:R6.CFG.8 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 168 | D5-S1D3 | REQ:R6.ADAPT.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 169 | D5-S1D3 | REQ:R6.A1CFG.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 170 | D5-S1D3 | REQ:R6.A1CFG.2 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 171 | D5-S1D3 | REQ:R6.VALID.3 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 172 | D5-S1D3 | REQ:R6.REPRO.1 | pending key S1-D3 | stricter: 50 requirements marked pending for the adoption decision |
| 173 | D1-scope | REQ:R6.STAT.4 | pending keys v6.0e line 95 moved to owner_decision (decision 1) | neutral: decision 1; no check removed (GATE-16 stays named by R6.EVID.5 and its other requirements) |
| 174 | D1 | REQ:R6.STAT.8 | pending keys 7093128173 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 175 | D1 | REQ:R6.PUR.8 | pending keys V5-D1, V5-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 176 | D1 | REQ:R6.PUR.9 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 177 | D1 | REQ:R6.PUR.11 | pending keys v6.0e line 95 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 178 | D1 | REQ:R6.ANCH.14 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 179 | D1 | REQ:R6.CTX.1 | pending keys v3 D1-D4 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 180 | D1 | REQ:R6.CTX.4 | pending keys v3 D1-D4 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 181 | D1 | REQ:R6.CTX.12 | pending keys v3 D1-D4 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 182 | D1 | REQ:R6.OUT.14 | pending keys R-D labels, A-D labels moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 183 | D1-defer | REQ:R6.OUT.15 | pending keys R-D labels moved to owner_decision (decision 1) | owner-decided deferral; the text, the rows TR45-opB and TR45 and every other check are kept |
| 184 | D1 | REQ:R6.PROF.9 | pending keys R-D labels, v5.5.9 final D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 185 | D1 | REQ:R6.RULE.2 | pending keys S1-D1 to S1-D3 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 186 | D1 | REQ:R6.RULE.4 | pending keys S1-D1 to S1-D3 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 187 | D1 | REQ:R6.RULE.7 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 188 | D1 | REQ:R6.RULE.8 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 189 | D1 | REQ:R6.RULE.9 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 190 | D1 | REQ:R6.REC.6 | pending keys DI-2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 191 | D1 | REQ:R6.REC.7 | pending keys DI-2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 192 | D1 | REQ:R6.REC.14 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 193 | D1 | REQ:R6.REC.18 | pending keys R-D labels, v6.0e line 54 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 194 | D1 | REQ:R6.REC.19 | pending keys v6.0e line 31, v6.0e line 54 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 195 | D1 | REQ:R6.REC.20 | pending keys v6.0e line 54 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 196 | D1 | REQ:R6.REC.21 | pending keys v6.0e line 54 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 197 | D1 | REQ:R6.REC.22 | pending keys v6.0e line 54 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 198 | D1 | REQ:R6.REC.24 | pending keys R-D labels moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 199 | D1 | REQ:R6.DENY.5 | pending keys V5-D1, S1-D2, V5-D2, S1-D1 to S1-D3 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 200 | D1 | REQ:R6.DENY.6 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 201 | D1 | REQ:R6.CTRL.7 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 202 | D1 | REQ:R6.CTRL.14 | pending keys V5-D1, S1-D1 to S1-D3 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 203 | D1 | REQ:R6.CTRL.15 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 204 | D1 | REQ:R6.CTRL.17 | pending keys R-D labels moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 205 | D1 | REQ:R6.CTRL.19 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 206 | D1 | REQ:R6.CTRL.22 | pending keys DI-2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 207 | D1 | REQ:R6.CTRL.23 | pending keys R-D labels moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 208 | D1 | REQ:R6.CTRL.24 | pending keys S1-D2, R-D labels moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 209 | D1 | REQ:R6.PLAN.8 | pending keys v3 D1-D4 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 210 | D1 | REQ:R6.A1CFG.7 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 211 | D1 | REQ:R6.EVID.4 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 212 | D1-scope | REQ:R6.EVID.5 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: decision 1; no check removed (GATE-16 stays named by R6.EVID.5 and its other requirements) |
| 213 | D1 | REQ:OBL-1 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 214 | D1 | REQ:OBL-3 | pending keys V5-D1, S1-D2, V5-D2, S1-D1 to S1-D3 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 215 | D1 | REQ:OBL-6 | pending keys V5-D1 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 216 | D1 | REQ:OBL-15 | pending keys S1-D2 moved to owner_decision (decision 1) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 217 | meta | REQUIREMENTS.json | field owner_decision added to every entry (the record, decision, effect and the decision basis keys); pending keys now S1-D3 only; R6.TREE.19 added | neutral |
| 218 | meta | EXPECTATIONS.json | record_id r6-final3-1 -> r6-final4-1 | neutral |
| 219 | D3 | EXP:V15 | expect := the "reversal adopted" candidate; candidate_expectations removed (R6.GATE.2: deferred rows only); flags restated | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 220 | D3 | EXP:V27 | expect := the "reversal adopted" candidate; candidate_expectations removed (R6.GATE.2: deferred rows only); flags restated | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 221 | D3 | EXP:V27-glossary | expect := the "reversal adopted" candidate; candidate_expectations removed (R6.GATE.2: deferred rows only); flags restated | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 222 | D3 | EXP:V4 | expect := the "reversal adopted" candidate; candidate_expectations removed (R6.GATE.2: deferred rows only); flags restated | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 223 | D3 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D1 | note: the four rows carry the expectations of resolution (a) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 224 | N2 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D1 | the v6.0e-derived consequence moved out of "what the record says" | neutral |
| 225 | N2 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: V5-D2 | the coverage-limitation decision named as the direct basis of R6.PUR.8 | neutral |
| 226 | R1 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: v6.0e line 31 | the 7130449822 adoption of v6.0e noted | neutral: notes |
| 227 | R1 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: v6.0e line 54 | the 7130449822 adoption of v6.0e noted | neutral: notes |
| 228 | R1 | AUTHORIZATIONS.md / PARAPHRASED-DECISIONS.md: v6.0e line 95 | re-confirmation of a settled decision noted | neutral: notes |
| 229 | D1 | PARAPHRASED-DECISIONS.md | regenerated: every listed requirement with its status after decision 1 | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 230 | R3 | PARAPHRASED-DECISIONS.md | option (c) only by explicit owner choice; non-confirmation leaves a requirement pending | stricter: no requirement is withdrawn by non-confirmation |
| 231 | D5-S1D3 | PARAPHRASED-DECISIONS.md | entry S1-D3 added with the identified requirements | stricter: 50 requirements marked pending for the adoption decision |
| 232 | D3 | AUTHORIZATIONS.md: 7162098696 | relied-on text: the V4-group candidates carried until decision 3 | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 233 | N1 | AUTHORIZATIONS.md sec. 1 | what each class (i) record authorizes stated; none adopts r6 | neutral |
| 234 | D5 | AUTHORIZATIONS.md | comments 7166666428 and 7166844576 added; 7166844576 as a class (i) record | neutral: quotation and scope |
| 235 | D3 | FRESH-AUTHORIZATION.md: R6.PUR.9, R6.A1CFG.7 | analysis restated for the decision (a) | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 236 | D4iii | FRESH-AUTHORIZATION.md: R6.CTRL.19 | analysis restated: the T1' figure is candidate evidence only | stricter: the T1' figure supports no acceptance |
| 237 | D1 | FRESH-AUTHORIZATION.md | status of every entry after decision 1 (confirmed, scope statement, deferred) | neutral: the confirmations are the owner's; no content, check or expectation changes |
| 238 | D2 | FRESH-AUTHORIZATION.md | sec. 2: the reviewer's classes of the 12 flagged requirements, accepted | neutral: classification only |
| 239 | R6 | FRESH-AUTHORIZATION.md | R6.A1CFG.7 flagged as narrowing, class (c), protected by R6.GATE.9 and OBL-6 | neutral: flag |
| 240 | R3 | FRESH-AUTHORIZATION.md | "If not authorized" replaced by "If not confirmed: ... stays pending"; withdrawal stated as a separate explicit owner choice | stricter: no requirement is withdrawn by non-confirmation |
| 241 | R1 | FRESH-AUTHORIZATION.md | the 7130449822 adoption noted on R6.STAT.4, R6.PUR.11 and R6.REC.18 to R6.REC.22 | neutral: notes |
| 242 | D5-S1D3 | FRESH-AUTHORIZATION.md | sec. 3 (new): the requirements resting on S1-D3, rules, status and wording | stricter: 50 requirements marked pending for the adoption decision |
| 243 | D3 | V4-COMPARISON.md | regenerated as decided: decision 3 quoted, selection per row, labels of the rejected candidate restated | the owner's decision; permits what v2 and v4 prohibited, as V4-COMPARISON.md states; V15 keeps human review |
| 244 | R4 | V4-COMPARISON.md | the 4677-blob search marked provenance (R6.EVID.5); RT-DR re-check under (b) stated as moot under (a) | neutral |
| 245 | N4 | V4-COMPARISON.md | the blocker's discharge stated for every resolution | neutral |
| 246 | N5 | V4-COMPARISON.md | wording: r6 expects the outcomes of (a), and no such rule is required | neutral |
| 247 | D4i | REVIEW-r6-round2.md | review record: header (reviewer, commit, date, comment) and the reviewer text verbatim | neutral or stricter: separate merge approval stated |

***

## 3. Safeguards

No safeguard is weakened by an edit of this round on its own authority. Decision 3 is the owner's choice of resolution (a), which permits what v2 and v4 prohibited (V4-COMPARISON.md), with V15 kept under human review; decision 1 defers R6.OUT.15 and its replay mode, keeping its text and rows. The "Safeguard" column above states the reason for each edit; it is asserted text, and the checks of sec. 4 measure what they name.

***

## 4. Self-checks (before: out-final3; after: out-final4)

| Check (round 2's run_checks; the mark is round 2's before and the S1-D3 mark after) | Before | After |
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
| requirements | 427 | 428 | R6.TREE.19 added (decision 4 (ii)) |
| expectation rows | 558 | 558 |  |
| rows flagged VD-RESTORE | 217 | 217 |  |
| requirements marked pending owner confirmation | 44 | 50 | 44 decided by decision 1 (41 confirmed, 2 scope, 1 deferred); 50 S1-D3 requirements marked (decision 5) |
| testable requirements without a control | 14 | 14 |  |
| MAPPING rows placed | 1149 | 1149 |  |
| OPEN markers in the requirement index | 3 | 2 | OBL-23's marker removed: decision 4 (iii) narrows the claim |
| rows with expect DEFERRED | 4 | 0 | decision 3 selects the four expectations |

Checks of this round:

- replay: the index rule reproduces out-final3/REQUIREMENTS.json from out-final3/DESIGN-r6.md: 0
- D1: the review's classes (22, 19, 2, 1) parsed and equal to the 44 previously marked requirements: 0
- D1: each of the 44 carries exactly its decision-1 text and no round-2 mark: 0
- D1: no requirement anywhere carries the round-2 mark: 0
- D2: 12 flagged rows parsed, classes (b) x6, (c) x2, (d) x4: 0
- D3: the four rows' expect equals the out-final3 "reversal adopted" candidate, byte for byte; no candidates left: 0
- D3: every other expectation row byte-identical to out-final3 (554 rows): 0
- D3: the four rows differ from out-final3 only in expect, candidate_expectations and two flags: 0
- preservation: retired list unchanged: 0
- preservation: requirement ids: only R6.TREE.19 added, none removed: 0
- preservation: sources and controls of every earlier requirement unchanged: 0
- preservation: sections 33 and 34 unchanged: 0
- preservation: Appendix H changed only in HIST-4: 0
- preservation: MIGRATION.json and CORRECTION-REPORT.md unchanged: 0
- preservation: requirement blocks without a logged edit unchanged (whitespace-normalized): 0
- D4 (iii): OBL-23 carries no OPEN marker; OPEN markers are those of R6.STAT.10 and R6.TREE.12: 0
- D4 (i): REVIEW-r6-round2.md holds the reviewer text verbatim; its sha256 equals the digest in comment 7166666428: 0
- D5: decisions 1 to 4 quoted byte-exact in sec. 0.1: 0
- D5: S1-D3 marks equal the identified requirements less those decision 1 confirmed: 0
- R3: no "If not authorized" line; every entry has "If not confirmed: ... stays pending": 0
- quotes: every quotation of a comment occurs in its body: 0
- V4-COMPARISON: rule-form matches as expected: 0
- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return, no invisible formatting character, no non-ASCII space, and no non-ASCII character outside those of the inputs and the quoted texts, in any output: checked
- reproducibility: the generator re-ran itself in a separate process (`python3 -I -B`) and compared the sha256 of every output before writing; identical
- generator problems: 0

***

## 5. Remaining open items

- Pending for the adoption decision: the 50 requirements resting on S1-D3 that decision 1 did not confirm (FRESH-AUTHORIZATION.md, sec. 3); R6.STAT.8's own condition, the restatement of the landing-order decision in the owner's words.
- R6.DENY.1 and R6.DENY.2 are not marked and were not among the requirements decision 1 confirmed; they take effect only by r6's adoption (the review would class both as necessary for reliable verification).
- R6.STAT.10, off-main support of adoption: open until the r6 documents, REVIEW-r6-round2.md and the delta review reach `main` by an owner-approved merge.
- R6.TREE.12 / LC-7: the procedure R6.TREE.19 awaits the delta review; LC-7's expectation is unchanged (REVIEW_REQUIRED) and its OPEN flag is kept; once the procedure is accepted, LC-7's cases need an owner-approved expectation change.
- The deferred R6.OUT.15: the expectation rows TR45-opB and TR45 (composite of TR45-opB and TR45-opC) are unchanged, as this revision changes no expectation except decision 3's selection; carried as they are, a tool revision without the replay mode would leave TR45-opB without a record (`missing-id`). Their treatment in the expectation file is for the delta review and a later owner-approved expectation change. R6.REC.24 still lists `"replay"` among the modes, marked deferred.
- R6.EVID.5 still names GATE-16 under Controls (its link in GATE-16's row is unchanged); GATE-16 is the gate's reference-difference control, not a check of R6.EVID.5's list.
- The expectation row item11-T1p is byte-identical; its flag "inputs off main: acceptance reference only for runs with those pinned inputs (RD-23)" predates decision 4 (iii), which OBL-23 now states; the flag is for the delta review.

***

## 6. Contradictions and departures found

- CORRECTION-REPORT.md (round 2) says the previous report "is a record of its round and is not edited", yet it replaced the round-1 report in place; the round-1 text is in history at ad035ff5. It cites its generator and inputs as `build/correct2.py`, `out-final2/` and `gh7/sel.json`; in the directory these are `generator-round2/correct2.py`, the round-1 outputs at ad035ff5 and `generator-round2/comments-1169.json`, as `generator-round2/PROVENANCE.json` maps them (N3). This round leaves CORRECTION-REPORT.md byte-identical as the round-2 record and writes its own report to this file.
- Decision 1 confirms R6.STAT.8 as a requirement; the requirement itself asks that the landing-order decision be restated in the owner's words before adoption, which decision 1 does not do. Recorded as owed (sec. 0.1, FRESH-AUTHORIZATION.md).
- The review counts 44 pending requirements and 12 flagged; R6.A1CFG.7, flagged under R6, is one of the 22 decision 1 confirms, so its flag changes no status.
