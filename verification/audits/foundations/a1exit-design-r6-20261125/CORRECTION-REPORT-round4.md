# r6, round 4: correction report

Generator: build/correct4.py (landed as generator-round4/). Applies owner decisions A1 to A5 of 2026-11-25 and the closing direction (quoted in DESIGN-r6.md sec. 0.1). Nothing is adopted, frozen, merged or executed.

## 1. Inputs

| Input | sha256 or git blob |
|---|---|
| directory at c33d5b71: AUTHORIZATIONS.md | blob 85309f7d35dc9892bb8435fbd0399ae35f12f012 |
| directory at c33d5b71: CHECKS.txt | blob 84230bd2dae6c4d8c81fa0bdacf449f725fcb603 |
| directory at c33d5b71: CONFORMANCE.md | blob 74ecf04de9e2ccd32b7ef4e83138eb49ec5955b1 |
| directory at c33d5b71: CORRECTION-REPORT-round3.md | blob 5049cc257f0521612dea25d9c565aed8b6b53b9e |
| directory at c33d5b71: CORRECTION-REPORT.md | blob 064a5ec624c86abd24db2249ef317bdb20787dac |
| directory at c33d5b71: DECISIONS.md | blob f02b8eebeb1b7db3acce68ac7f29c1f16c52a3cc |
| directory at c33d5b71: DESIGN-r6.md | blob bb1f85d8ff4dfa0d22302be82b97e651c5ac956a |
| directory at c33d5b71: EXPECTATION-SOURCES.json | blob 303f23616d571954a056d5d0bde5fde2faf1c1bc |
| directory at c33d5b71: EXPECTATIONS-REPORT.md | blob 12c3c2fad83616d7c1155e33b6b1dce389eb8f26 |
| directory at c33d5b71: EXPECTATIONS-draft.json | blob 5917b03bc7a57a6c2c517857c0e795365f5de4d3 |
| directory at c33d5b71: EXPECTATIONS.json | blob 895a25b458581619c1b59c487f1b52a959b895cb |
| directory at c33d5b71: FINAL-REPORT.md | blob aa2f161860b40263e4614f07cfc93ca000418610 |
| directory at c33d5b71: FRESH-AUTHORIZATION.md | blob 976fadffb1be3f80e6fe47d783e8473ec07ef9f0 |
| directory at c33d5b71: GATE-draft.md | blob f35e68b9d7c15cb8b1d1cab971286d15ed06c450 |
| directory at c33d5b71: INTEGRATION-REPORT.md | blob 66bbaa563e2c6cec7a8ccc84274e4deb5babb383 |
| directory at c33d5b71: INVENTORY.json | blob 95d693f82be5a121049b5f2e73ca5754d88bddd9 |
| directory at c33d5b71: MAPPING-CHECK.txt | blob c0644e12d0e4bbe67936b24bf3493ebc95d74dc2 |
| directory at c33d5b71: MAPPING.json | blob f5d35cb490b0d8925ea7e242446837d567768021 |
| directory at c33d5b71: MIGRATION.json | blob 4ed66d207198ac12e5b7adcc637ce9325d21199c |
| directory at c33d5b71: OUTLINE.md | blob 81aec76de8dca743467bc64ffd78d81f69eefb19 |
| directory at c33d5b71: PARAPHRASED-DECISIONS.md | blob 682270ac50f58555a77aa7a963267ce03aa7d398 |
| directory at c33d5b71: PENDING-33.md | blob 1e09093faf934094dc201c045468d7f96e77ffc4 |
| directory at c33d5b71: RE2-ROWS.md | blob cde0e3f8b7c357c8c87ec0ee62409fcc35a78c86 |
| directory at c33d5b71: REQUIREMENTS.json | blob f8ae46ab248a8b9a627a8ed21bc02a63116017fa |
| directory at c33d5b71: RESIDUAL-2.md | blob feb9e27cc69fed3e9b90a2147d3ea1272db2dd47 |
| directory at c33d5b71: RESIDUAL.md | blob 6932490ae1db2a1c2375f91359e9ace45fddab33 |
| directory at c33d5b71: REVIEW-r6-round2.md | blob 654bd76776042e1d2a135c8b15d2b447df0ef00a |
| directory at c33d5b71: V4-COMPARISON.md | blob 4efb9826e59b3c58d4209f89fb6ef72549e16bda |
| directory at c33d5b71: generator-round2/PROVENANCE.json | blob aa22337f3ebcff9857f4fc243ecb4138ae627526 |
| directory at c33d5b71: generator-round2/comments-1169.json | blob 318fe33d6e7393184198f7e5af9f1272ad6a991e |
| directory at c33d5b71: generator-round2/correct.py | blob e846064c295cadd999317cd83e9a63386269e29d |
| directory at c33d5b71: generator-round2/correct2.py | blob 809afa8448996c989879e285e6b66bb10033bd1f |
| directory at c33d5b71: generator-round2/report_text.py | blob f71d4c6d2ecf0f9c92a9b5f282592fdcd20c53aa |
| directory at c33d5b71: generator-round2/text2.py | blob 3c469f71083f56c1d328cbcfffd8e529c0d34204 |
| directory at c33d5b71: generator-round3/comments-round3.json | blob 7e4467626c700c23906e2e807dcfb8f55b9e0206 |
| directory at c33d5b71: generator-round3/correct3.py | blob f7a8aa4be68b6b6874e819fe0d9808102da0ef0d |
| directory at c33d5b71: generator-round3/review-r6-round2.md | blob 6f172c4dd1b6e9f57ca969b5e422afb1aa906d1e |
| build/inputs/tree-c33d5b71.json | 82335bd460b7be4c0c119c2dca51722b3e7d0c7912815ceb9623f200d2104114 |
| build/inputs/owner-decisions-A1-A5.json | b5340474a2ef0e8abb146009f9d01a2aadf8791f6a14f352a5963f8c18968d56 |
| build/inputs/review-r6-round3.md | 05b42b1c02bcfdeeecb543ecc0c87df3f8b10db82a8b12fa1343bef15b974fb4 |
| build/inputs/records-1169.json | bc1881208ab198f9427ecc3ba9d1bcdcc46530ff72b5038cd4fd65fdffa3395e |

## 2. Edits

| # | Decision | Target | Edit |
|---|---|---|---|
| 1 | A1 | R6.OUT.15 | deferral extended to TR45-opC, TR45 and OBL-17 |
| 2 | A1 | OBL-17 | deferred; gates no step while deferred |
| 3 | A1 | sec. 32 table | text edit |
| 4 | A1 | R6.GATE.15 | TR45-opB admits NOT RUN |
| 5 | A1 | R6.GATE.15 | deferred rows stated |
| 6 | A1 | R6.CTRL.5 | TR45-opB admits NOT RUN |
| 7 | A1 | R6.CTRL.17 | TR45-opC deferred |
| 8 | A1 | R6.GATE.9 | TR45 components named |
| 9 | A1 | Table 17.1 TR45-opB | text edit |
| 10 | A1 | Table 17.1 TR45-opC | text edit |
| 11 | A1 | Table 17.1 TR45 | text edit |
| 12 | A1 | OBL-28 | text edit |
| 13 | A1 | sec. 0.1 decision 1 | text edit |
| 14 | A3 | R6.STAT.8 | restatement given (A3) |
| 15 | A3 | sec. 0.1 decision 5 | text edit |
| 16 | A4 | R6.OUT.12 | pending mark replaced: confirmed (A4) |
| 17 | A4 | R6.REC.5 | pending mark replaced: confirmed (A4) |
| 18 | A4 | R6.REC.13 | pending mark replaced: confirmed (A4) |
| 19 | A4 | R6.REC.16 | pending mark replaced: confirmed (A4) |
| 20 | A4 | R6.REC.17 | pending mark replaced: confirmed (A4) |
| 21 | A4 | R6.DELEG.1 | pending mark replaced: confirmed (A4) |
| 22 | A4 | R6.DELEG.2 | pending mark replaced: confirmed (A4) |
| 23 | A4 | R6.DELEG.3 | pending mark replaced: confirmed (A4) |
| 24 | A4 | R6.DELEG.4 | pending mark replaced: confirmed (A4) |
| 25 | A4 | R6.DELEG.5 | pending mark replaced: confirmed (A4) |
| 26 | A4 | R6.DELEG.6 | pending mark replaced: confirmed (A4) |
| 27 | A4 | R6.DELEG.7 | pending mark replaced: confirmed (A4) |
| 28 | A4 | R6.DELEG.10 | pending mark replaced: confirmed (A4) |
| 29 | A4 | R6.DELEG.12 | pending mark replaced: confirmed (A4) |
| 30 | A4 | R6.DELEG.13 | pending mark replaced: confirmed (A4) |
| 31 | A4 | R6.DELEG.15 | pending mark replaced: confirmed (A4) |
| 32 | A4 | R6.DELEG.16 | pending mark replaced: confirmed (A4) |
| 33 | A4 | R6.DELEG.18 | pending mark replaced: confirmed (A4) |
| 34 | A4 | R6.GATE.5 | pending mark replaced: confirmed (A4) |
| 35 | A4 | R6.GATE.7 | pending mark replaced: confirmed (A4) |
| 36 | A4 | R6.GATE.8 | pending mark replaced: confirmed (A4) |
| 37 | A4 | R6.GATE.9 | pending mark replaced: confirmed (A4) |
| 38 | A4 | R6.GATE.15 | pending mark replaced: confirmed (A4) |
| 39 | A4 | R6.CTRL.4 | pending mark replaced: confirmed (A4) |
| 40 | A4 | R6.CTRL.5 | pending mark replaced: confirmed (A4) |
| 41 | A4 | R6.CTRL.20 | pending mark replaced: confirmed (A4) |
| 42 | A4 | R6.CTRL.25 | pending mark replaced: confirmed (A4) |
| 43 | A4 | R6.PLAN.2 | pending mark replaced: confirmed (A4) |
| 44 | A4 | R6.PLAN.6 | pending mark replaced: confirmed (A4) |
| 45 | A4 | R6.PLACE.2 | pending mark replaced: confirmed (A4) |
| 46 | A4 | R6.PLACE.4 | pending mark replaced: confirmed (A4) |
| 47 | A4 | R6.TREE.1 | pending mark replaced: confirmed (A4) |
| 48 | A4 | R6.TREE.10 | pending mark replaced: confirmed (A4) |
| 49 | A4 | R6.TREE.18 | pending mark replaced: confirmed (A4) |
| 50 | A4 | R6.RDIR.13 | pending mark replaced: confirmed (A4) |
| 51 | A4 | R6.CORE.1 | pending mark replaced: confirmed (A4) |
| 52 | A4 | R6.CORE.2 | pending mark replaced: confirmed (A4) |
| 53 | A4 | R6.CORE.3 | pending mark replaced: confirmed (A4) |
| 54 | A4 | R6.CORE.4 | pending mark replaced: confirmed (A4) |
| 55 | A4 | R6.CORE.5 | pending mark replaced: confirmed (A4) |
| 56 | A4 | R6.CORE.6 | pending mark replaced: confirmed (A4) |
| 57 | A4 | R6.CFG.1 | pending mark replaced: confirmed (A4) |
| 58 | A4 | R6.CFG.2 | pending mark replaced: confirmed (A4) |
| 59 | A4 | R6.CFG.3 | pending mark replaced: confirmed (A4) |
| 60 | A4 | R6.CFG.8 | pending mark replaced: confirmed (A4) |
| 61 | A4 | R6.ADAPT.2 | pending mark replaced: confirmed (A4) |
| 62 | A4 | R6.A1CFG.1 | pending mark replaced: confirmed (A4) |
| 63 | A4 | R6.A1CFG.2 | pending mark replaced: confirmed (A4) |
| 64 | A4 | R6.VALID.3 | pending mark replaced: confirmed (A4) |
| 65 | A4 | R6.REPRO.1 | pending mark replaced: confirmed (A4) |
| 66 | A4 | R6.OUT.5 | confirmed (A4; named by the round-3 delta review, F3) |
| 67 | A4 | R6.OUT.18 | confirmed (A4; named by the round-3 delta review, F3) |
| 68 | A4 | R6.DELEG.8 | confirmed (A4; named by the round-3 delta review, F3) |
| 69 | A4 | sec. 0.1 decision 5 | text edit |
| 70 | CLOSE | R6.TREE.12 | condition: until LC-7's cases are restated |
| 71 | CLOSE | Table 17.1 LC-7 | text edit |
| 72 | CLOSE | sec. 0.1 decision 4 | text edit |
| 73 | CLOSE | R6.TREE.19 | status after the round-3 delta review |
| 74 | NIT | R6.TREE.19 | nit (a): generator, not checker |
| 75 | NIT | R6.TREE.19 | nit (b): R6.DELEG.3 isolation cited; failure classes explained |
| 76 | NIT | R6.TREE.19 | nit (a) |
| 77 | NIT | R6.TREE.19 | nit (a) |
| 78 | NIT | R6.TREE.19 | nit (a) |
| 79 | NIT | R6.TREE.19 | nit (c): consequence for non-deterministic generators |
| 80 | CLOSE | R6.TREE.19 | controls note |
| 81 | A5 | R6.STAT.10 | reviews and landing manifest |
| 82 | A5 | sec. 32 adoption trace | text edit |
| 83 | A5 | sec. 32 adoption trace | text edit |
| 84 | meta | sec. 0.1 | text edit |
| 85 | A1-A5 | sec. 0.1 | owner decisions A1-A5 quoted byte-exact, with how r6 applies them |
| 86 | A4 | REQUIREMENTS.json | 53 entries: pending key removed, owner decision A4 recorded |
| 87 | A3 | REQUIREMENTS.json | R6.STAT.8: owner decision A3 recorded |
| 88 | A1 | REQUIREMENTS.json | R6.OUT.15 and OBL-17: owner decision A1 recorded |
| 89 | meta | EXPECTATIONS.json | record_id r6-final4-1 -> r6-final5-1 |
| 90 | A1 | TR45-opB | NOT RUN admitted with the deferral as reason; flag added; expect and restored unchanged |
| 91 | A1 | TR45-opC | not_run: the deferral replaces the evidence release condition; flag "named blocker" replaced |
| 92 | A1 | TR45 | not_run inherits the deferral; flag added |
| 93 | A2 | item11-T1p | the two flags corrected to "candidate evidence only, not acceptance support"; expect unchanged |
| 94 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.STAT.8 regenerated (1 occurrence(s)) |
| 95 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.OUT.12 regenerated (1 occurrence(s)) |
| 96 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.OUT.15 regenerated (1 occurrence(s)) |
| 97 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.REC.5 regenerated (1 occurrence(s)) |
| 98 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.REC.13 regenerated (1 occurrence(s)) |
| 99 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.REC.16 regenerated (1 occurrence(s)) |
| 100 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.REC.17 regenerated (1 occurrence(s)) |
| 101 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.1 regenerated (1 occurrence(s)) |
| 102 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.2 regenerated (1 occurrence(s)) |
| 103 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.3 regenerated (1 occurrence(s)) |
| 104 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.4 regenerated (1 occurrence(s)) |
| 105 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.5 regenerated (1 occurrence(s)) |
| 106 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.6 regenerated (1 occurrence(s)) |
| 107 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.7 regenerated (1 occurrence(s)) |
| 108 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.10 regenerated (1 occurrence(s)) |
| 109 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.12 regenerated (1 occurrence(s)) |
| 110 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.13 regenerated (1 occurrence(s)) |
| 111 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.15 regenerated (1 occurrence(s)) |
| 112 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.16 regenerated (1 occurrence(s)) |
| 113 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.DELEG.18 regenerated (1 occurrence(s)) |
| 114 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.GATE.5 regenerated (1 occurrence(s)) |
| 115 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.GATE.7 regenerated (1 occurrence(s)) |
| 116 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.GATE.8 regenerated (1 occurrence(s)) |
| 117 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.GATE.9 regenerated (1 occurrence(s)) |
| 118 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.GATE.15 regenerated (1 occurrence(s)) |
| 119 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CTRL.4 regenerated (1 occurrence(s)) |
| 120 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CTRL.5 regenerated (1 occurrence(s)) |
| 121 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CTRL.17 regenerated (1 occurrence(s)) |
| 122 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CTRL.20 regenerated (1 occurrence(s)) |
| 123 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CTRL.25 regenerated (1 occurrence(s)) |
| 124 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.PLAN.2 regenerated (1 occurrence(s)) |
| 125 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.PLAN.6 regenerated (1 occurrence(s)) |
| 126 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.PLACE.2 regenerated (1 occurrence(s)) |
| 127 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.PLACE.4 regenerated (1 occurrence(s)) |
| 128 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.TREE.1 regenerated (1 occurrence(s)) |
| 129 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.TREE.10 regenerated (1 occurrence(s)) |
| 130 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.TREE.18 regenerated (1 occurrence(s)) |
| 131 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.RDIR.13 regenerated (1 occurrence(s)) |
| 132 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.1 regenerated (1 occurrence(s)) |
| 133 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.2 regenerated (1 occurrence(s)) |
| 134 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.3 regenerated (1 occurrence(s)) |
| 135 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.4 regenerated (1 occurrence(s)) |
| 136 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.5 regenerated (1 occurrence(s)) |
| 137 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CORE.6 regenerated (1 occurrence(s)) |
| 138 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CFG.1 regenerated (1 occurrence(s)) |
| 139 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CFG.2 regenerated (1 occurrence(s)) |
| 140 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CFG.3 regenerated (1 occurrence(s)) |
| 141 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.CFG.8 regenerated (1 occurrence(s)) |
| 142 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.ADAPT.2 regenerated (1 occurrence(s)) |
| 143 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.A1CFG.1 regenerated (1 occurrence(s)) |
| 144 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.A1CFG.2 regenerated (1 occurrence(s)) |
| 145 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.VALID.3 regenerated (1 occurrence(s)) |
| 146 | meta | FRESH-AUTHORIZATION.md | quoted wording of R6.REPRO.1 regenerated (1 occurrence(s)) |
| 147 | A4 | FRESH-AUTHORIZATION.md | text edit (1 occurrence(s)) |
| 148 | A4 | FRESH-AUTHORIZATION.md | text edit (1 occurrence(s)) |
| 149 | A4 | FRESH-AUTHORIZATION.md | sec. 3: owner decision A4 quoted |
| 150 | A4 | FRESH-AUTHORIZATION.md | text edit (1 occurrence(s)) |
| 151 | A4 | FRESH-AUTHORIZATION.md | text edit (50 occurrence(s)) |
| 152 | A4 | FRESH-AUTHORIZATION.md | sec. 3: the three requirements named by the review; options paragraph replaced |
| 153 | A4 | FRESH-AUTHORIZATION.md | sec. 3: wording of R6.OUT.5, R6.OUT.18 and R6.DELEG.8 added |
| 154 | A3 | FRESH-AUTHORIZATION.md | text edit (1 occurrence(s)) |
| 155 | A1 | FRESH-AUTHORIZATION.md | text edit (1 occurrence(s)) |
| 156 | A4 | PARAPHRASED-DECISIONS.md | text edit (50 occurrence(s)) |
| 157 | A4 | PARAPHRASED-DECISIONS.md | text edit (1 occurrence(s)) |
| 158 | A4 | PARAPHRASED-DECISIONS.md | text edit (1 occurrence(s)) |
| 159 | A4 | AUTHORIZATIONS.md | text edit (50 occurrence(s)) |
| 160 | A4 | AUTHORIZATIONS.md | text edit (1 occurrence(s)) |
| 161 | A1-A5 | AUTHORIZATIONS.md | entry for owner decisions A1-A5 added to sec. 1 |
| 162 | A5 | AUTHORIZATIONS.md | sec. 5: the round-3 delta review record |
| 163 | A5 | REVIEW-r6-round3.md | review record: header and the reviewer text verbatim |
| 164 | A5 | LANDING-MANIFEST.md | landed files, files left to history, 268 references classified |

R6.TREE.19 clarifications of the round-3 delta review applied, each as one sentence or a word substitution (NIT): (a) the program is a generator named by the delegation contract pinned at `F`, a class naming none stays REVIEW_REQUIRED; (b) R6.DELEG.3's isolation cited and the different failure classes explained; (c) the consequence for a generator that is not byte-deterministic stated (fail-closed FAIL). Not applied: the review's nits N-a to N-d; the Table 17.1 description of item11-T1p ("candidate evidence for the landing decision only") is left as it stands, since owner decision A2 changes only the two flags; LC-7's row in the expectation file keeps its flag text until the owner-approved restatement of its cases.

## 3. Values, before (round 3) and after

| Value | Before | After |
|---|---|---|
| requirements | 428 | 428 |
| expectation rows | 558 | 558 |
| rows flagged VD-RESTORE | 217 | 217 |
| requirements marked pending owner confirmation | 50 | 0 |
| testable requirements without a control | 14 | 14 |
| MAPPING rows placed | 1149 | 1149 |
| OPEN markers in the requirement index | 2 | 2 |
| rows with expect DEFERRED | 0 | 0 |

## 4. Self-checks

Round-3 checks (run_checks of correct3.py), before and after:

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

Round-4 checks:

| Check | Result |
|---|---|
| A1: the three rows keep expect, restored, requirements, runner and procedure; NOT RUN admitted with the deferral | pass |
| A1/A2: every other row byte-identical; order, count and retired unchanged | pass |
| A1: OBL-17 gates no step; GATE.15 and CTRL.5 admit NOT RUN for TR45-opB | pass |
| A2: item11-T1p differs only in its two flags, both "candidate evidence only, not acceptance support" | pass |
| A3: the owner's wording quoted byte-exact in sec. 0.1; R6.STAT.8 cites it | pass |
| A4: the 53 carry the confirmation once; no pending mark or key remains | pass |
| CLOSE: R6.TREE.12 condition is the owner-approved restatement of LC-7 | pass |
| preservation: requirement ids unchanged | pass |
| preservation: sources, controls and OPEN markers of every requirement equal the index | pass |
| preservation: sources and controls unchanged from round 3 | pass |
| preservation: requirement blocks without a logged edit unchanged (whitespace-normalized) | pass |
| preservation: sections 33, 34 and Appendix H unchanged | pass |
| FRESH-AUTHORIZATION.md: every quoted requirement wording equals the design | pass |
| REVIEW-r6-round3.md holds the reviewer text verbatim | pass |
| manifest: every reference classified; landed and dropped partition the 37 files | pass |

## 5. Outputs

| File | sha256 |
|---|---|
| DESIGN-r6.md | 20f19f975513ed6181291a610961d2d5089cdd0d31fb13409e25fad05284d525 |
| EXPECTATIONS.json | a24a7b2bcaf5cdaeee6ca791cd4af11d1787043252d96bcb512825c9df17e847 |
| REQUIREMENTS.json | dbdba73379e99c7a4d66228aa7a60fe64af7154efbe9c836b814c768f6988167 |
| PARAPHRASED-DECISIONS.md | 05602f3ec2f971ad860bc864a2ad8fce2d115948b0d3ac369ef17874746b65ce |
| AUTHORIZATIONS.md | 168995ee25853891c68bdb1f634155bdd1940d780b482e720fa45d670977c97d |
| FRESH-AUTHORIZATION.md | c80508e3c9ae7872fbee427d51ba37080749d242ed8f14e17952982e2e20f217 |
| REVIEW-r6-round3.md | 546188124cfe34c3924e032879c4bb1ae80ea17e619586283927840ccdd6fd99 |
| LANDING-MANIFEST.md | 3ae6b8b225087cfe35ba9c3fc00be0de1144e96dbc7af135e462ddc3976fefcf |
| MIGRATION.json | 9188e876ffce703df20710b1285f4ff0ca9145ad656e3617e30feef56bcdaf08 |
| V4-COMPARISON.md | 76970c73eeb45d8f81c4665b8e7b72e90f29ecfe2747cf7b0440a697d5bd9edf |
| REVIEW-r6-round2.md | 8875ffd240989348f2c647b3187146e24c5454b5edc70c81817c9263a46c9912 |

MIGRATION.json, V4-COMPARISON.md and REVIEW-r6-round2.md are written unchanged. The generator re-runs itself in a separate process and writes only if every output's sha256 is equal.

## 6. Before adoption

- Done: the owner decisions A1-A5 and the round-3 delta review are recorded at #1169 comments 7169906297 and 7169923380.
- One short independent delta review of this revision (closing direction; R6.STAT.10).
- `P`'s edits_check.py semantics: support off main relied on by adoption (LANDING-MANIFEST.md sec. 4); an owner decision lands the blob or narrows the requirements.
- The landing: the owner-approved merge of the files of LANDING-MANIFEST.md sec. 1, keeping the branch history, with the remaining item 8 gaps of its sec. 4 closed or named by an owner decision (AGENTS.md sec. A.42 item 8, sec. A.50 item 1).
