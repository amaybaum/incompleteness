# r6 finalization report

Deterministic finalization of design r6 by `build/final.py` from the integration outputs and the review inputs. It applies the owner-approved resolutions of 2026-11-25 (RE-1 to RE-38 with section E of RESIDUAL-2.md, B-1 to B-24, C-1 to C-28 kept as obligations, D-1 to D-14 recorded) under the qualifications Q11 to Q16, RE-1 and the paraphrase list. It adopts nothing: r6 stays a draft until the owner adopts it.

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169). It decides the final form of the tool design for owner adoption; it decides no scientific question.

***

## 1. Inputs and outputs (sha256)

- input `out-int/DESIGN-r6.md` 75da68febf8eec0368b5c481741db9db915fcd58ff9fb8e8cd0208ebf045721e
- input `out-int/EXPECTATIONS.json` 9b39d96a963bcf7c94f0d4ab5a320c48150a4671a9dc0aaf395b2c5c3d5fe7bc
- input `out-int/REQUIREMENTS.json` 9644cbd5b05addd1c5ab43543e084399e1d94c7ec66cfba7e032b8c9b26385c6
- input `out-int/MIGRATION.json` 9e659bc24343564bb8c4ef00ba9624b91e1a199d0e4a6638599cd00adb3bc356
- input `out-int/INTEGRATION-REPORT.md` 8e4ce6dfb83bed460db48515ee0885230fb14c3d9e03bcd185b63c635c9dead6
- input `out-int/RE2-ROWS.md` 12efb2b077dbd866996722c80a51c16fbfc4df0ad8e395c0f6c5a239f0016993
- input `RESIDUAL-2.md` b30244c103048ca7f3040fa7e2f9f09383d3d3ef5c204db3ed3da0a8bfe5afd4
- input `CONFORMANCE.md` 35f32c5518603d3a921c27703a6d498be83966a7f66ab4234e1a954322d5d70e
- input `DECISIONS.md` eff7a158c049d56d26e7229bc8d38b8441a9374cb502167fbc7bbdf5be5f98a8
- input `RESIDUAL.md` db111ea087601ec0581bddaf3f62a30188c2f41904b02abf17bbaa365bf3e1fd
- input `MAPPING.json` bd1a8657961fd659b29980178781a7f30fd6e5b53da9a734db28a20130c9ff85
- input `INVENTORY.json` 42d44fb0624e82fb334d4feeeaceb7787c4309dfde2f52e373e208fe11d0f5dd
- output `DESIGN-r6.md` 4a2faa036511418068e50b986e12eda678569412638ed67d0ebdceb0b54801de
- output `EXPECTATIONS.json` 41ad9875e5f0a036f917d309ad16e1ab264efbdb5767e7de95f294591404ec4f
- output `REQUIREMENTS.json` a2fe59d4542e6de90224f6d7eaad481f7ed8ecfb5957616ba640bf3734469355
- output `MIGRATION.json` b24615f19b936983e6148c536717cde27c7430aaa0cb382e7da6ed10008582f7
- output `PARAPHRASED-DECISIONS.md` 250be39bff7bff6bfce40713bd1473bf28b56009a654a27e556600bf50ad43e3
- generator `build/final.py` e675eeeb77b778afa170c03b6de7ae3568ce9b527d4f5d86c3658f0cd20cdc00

FINAL-REPORT.md does not list its own digest.

***

## 2. Counts

Requirements: 425 (definition 13, governance 10, obligation 33, scope 8, status 4, testable 357).
Expectation rows: 557 (composite (no own runner) 5, control 415, gate self-test 30, mutant 107); retired entries: 66.
Rows added here: GATE-27, GATE-28, GATE-29, GATE-30, LC-1, LC-2, LC-3, LC-4, LC-5, LC-6, LC-7, DELEG-REGEN.
Requirements added here: R6.EVID.7, OBL-27, OBL-28. Requirements marked pending owner confirmation: 33.
Invariant vocabulary: 151 keys. Edits logged: 278.
OPEN flags in the integrated draft: 35 distinct; resolved here: 35; new OPEN flags raised by the Q15 and Q16 work: 3 (section 6).

***

## 3. Edits applied, by decision

- **RE-1** (14): EXP:V4: expect DEFERRED with both candidate expectations, each "not authoritative; decided at r6 adoption"; EXP:V27: expect DEFERRED with both candidate expectations, each "not authoritative; decided at r6 adoption"; EXP:V27-glossary: expect DEFERRED with both candidate expectations, each "not authoritative; decided at r6 adoption"; EXP:V15: expect DEFERRED with both candidate expectations, each "not authoritative; decided at r6 adoption"; EXP:GATE-29: row added; R6.PUR.9: text edit; R6.DENY.6: text edit; R6.GATE.2: text edit; R6.GATE.3: text edit; R6.CTRL.15: text edit; R6.CTRL.15: text edit; R6.CTRL.28: text edit; R6.A1CFG.7: text edit; OBL-6: text edit
- **Q11** (4): EXP: per-row direction decisions recorded on the 43 rows of RE2-ROWS.md (3 exempt, 40 required); R6.GATE.2: text edit; R6.CTRL.3: requirement block restated; OBL-20: requirement block restated
- **RE-4** (13): EXP:RT-T: paired_with RT-T0; EXP:RT-D-gr58: paired_with RT-D; EXP:RT-E: paired_with SW1; EXP:RT-T0: paired_with RT-T; EXP:RT-M: paired_with RT-T0; EXP:RT-SHIFT: paired_with RT-E; EXP:GATE-27: row added; R6.GATE.9: text edit; R6.GATE.13: text edit; R6.GATE.13: text edit; R6.GATE.13: Controls: added GATE-27, GATE-28, GATE-29, GATE-30; R6.CTRL.30: text edit; R6.CTRL.30: Controls: added GATE-27, GATE-28, GATE-29, GATE-30
- **C-1** (5): EXP:K3: flagged VD-RESTORE; EXP:K4: flagged VD-RESTORE; EXP:SW1: flagged VD-RESTORE; EXP:EI7-consumer: flagged VD-RESTORE; EXP:Z9h: flagged VD-RESTORE
- **RE-3** (1): EXP: scope (c) applied: 13 rows moved out of scope lose their VD-RESTORE flag (CLASS-RETAINED, CLASS-UNLEDGERED, CLASS-PROV-AMBIGUOUS, CLASS-PIN-TARGET, CLASS-RECORD-CHECKS, HIT-REPLACEMENT, PROF-LANDING-LIST, RULE-MINLIT, OUT-CONFINED, REPRO-PYVER, SIDE-NONREG, VD3-COUNT, VD3-CONTEXT); 41 in-scope rows without a second direction flagged (N10, N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, N3, N3-config-route, N4, N5, N6, N7, N8, N9, R15, R18, R18-engine, R19, R19-engine, RT-L, RT-L2, RT-X, TT1, TT10, TT11, TT12, TT13, TT14, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9)
- **Q12** (14): EXP:U14: positive case: state provenance-adjudicated and its count; wrong-hash case: exactly provenance-mismatch and stale-adjudication; EXP:RECLINT-ORPHAN: orphan HP entry: stale-adjudication; other orphan entries and duplicates: record-invalid; out-of-scope tree or segment: no finding; EXP:retired: U15 entry restated; EXP:retired: entry "stale-adjudication (class name)" removed: the class is live with v1 4.6's meaning; R6.HP.7: text edit; R6.CLASS.4: text edit; R6.CLASS.4: Controls: added RECLINT-ORPHAN, U14; R6.CLASS.4: Sources: added V1-061, V2-029, Q12; R6.CLASS.5: text edit; R6.CLASS.6: requirement block restated; R6.CTRL.9: text edit; R6.CTRL.16: requirement block restated; sec. 33 U15: text edit (1 occurrence(s)); sec. 33 stale-adjudication row: text edit (1 occurrence(s))
- **RE-16** (13): EXP:S11-57c: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; EXP:S11-58a-f: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; EXP:S11-58g: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; EXP:S11-58h: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; EXP:S11-58j: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; EXP:S11-58k: stop_class SOURCE_CHANGED -> LEDGER_INTEGRITY; R6.PIPE.11: text edit; R6.PIPE.15: text edit; R6.OUT.5: text edit; sec. 9.4 selection: text edit (1 occurrence(s)); sec. 9.4 binding: text edit (1 occurrence(s)); sec. 11.2: text edit (1 occurrence(s)); R6.VALID.3: text edit
- **RE-21** (4): EXP:EI14-dispatch: release condition: dispatch on a branch holding T' after the tool lands, owner-approved launch; R6.GATE.15: text edit; OBL-18: text edit; OBL-18: text edit
- **Q14** (22): EXP:TR45: NOT RUN admitted by inheritance from TR45-opC; EXP:EI14: NOT RUN admitted by inheritance from EI14-dispatch; EXP:EI2: composite precedence stated; EXP:EI7: composite precedence stated; EXP:GV6: composite precedence stated; EXP:GV7: composite precedence stated; EXP:RT-D: composite precedence stated; EXP:S11-2: composite precedence stated; EXP:TR14: composite precedence stated; EXP:TR15: composite precedence stated; EXP:TR28: composite precedence stated; EXP:TR29: composite precedence stated; EXP:TR50: composite precedence stated; EXP:TR51: composite precedence stated; EXP:TR52: composite precedence stated; EXP:V27: composite precedence stated; EXP:GATE-28: row added; R6.GATE.9: text edit; R6.GATE.9: Controls: added GATE-27, GATE-28, GATE-29; R6.GATE.15: Controls: added TR45, EI14; R6.CTRL.5: text edit; R6.CTRL.5: Controls: added TR45, EI14
- **B-18** (3): EXP:RT-M: OPEN flag removed (approved resolution); EXP:RT-SHIFT: OPEN flag removed (approved resolution); R6.CTRL.11: text edit
- **RE-15** (3): EXP:SIDE-NONREG: OPEN flag removed (approved resolution); R6.PUR.12: text edit; R6.RDIR.7: text edit
- **RE-23** (3): EXP:CLASS-RECORD-CHECKS: OPEN flag removed (approved resolution); R6.CLASS.1: text edit; R6.CLASS.11: OPEN flag resolved: op A record-check item
- **RE-35** (2): EXP:PROF-LANDING-LIST: OPEN flag removed (approved resolution); R6.PROF.11: text edit
- **RE-10** (4): EXP:MUT:cache:K08: verification defect with distinguishing control recorded; EXP:MUT:v60e:C08: verification defect with distinguishing control recorded; EXP:MUT:v60e:I06: verification defect with distinguishing control recorded; EXP:MUT:v60e:P01: verification defect with distinguishing control recorded
- **RE-20** (3): EXP:A2r: case on W2-a with "(A1)"; flag restated; R6.CTRL.29: text edit; OBL-21: text edit
- **RE-28** (8): EXP:RDIR-11: RD2-RD5 -> DIR2-DIR5; EXP:RDIR-12: RD2-RD5 -> DIR2-DIR5; EXP:RDIR-17: RD2-RD5 -> DIR2-DIR5; EXP:RDIR-24: RD2-RD5 -> DIR2-DIR5; EXP:RDIR-9: RD2-RD5 -> DIR2-DIR5; R6.RDIR.5: text edit; design: directory conditions RD2-RD5 renamed DIR2-DIR5 (37 occurrences); sec. 34 D2-D5: text edit (1 occurrence(s))
- **RE-11** (7): EXP:GATE-30: row added; sec. 0-8 no-control list: text edit (1 occurrence(s)); R6.GATE.12: text edit; R6.GATE.12: Controls: added GATE-30; R6.PLAN.17: OPEN flag resolved: correspondence exemption for non-testable requirements; R6.PLACE.5: OPEN flag resolved: correspondence exemption for non-testable requirements; REQUIREMENTS.json: field verification added (controls, review, or the OBL ids that carry a non-testable requirement)
- **Q15** (11): EXP:LC-1: row added; EXP:LC-2: row added; EXP:LC-3: row added; EXP:LC-4: row added; EXP:LC-5: row added; EXP:LC-6: row added; EXP:LC-7: row added; R6.TREE.13: text edit; R6.TREE.13: Controls: added LC-1, LC-2, LC-3, LC-4, LC-5, LC-6; R6.TREE.12: Controls: added LC-1, LC-2, LC-3, LC-4, LC-5, LC-6, LC-7; annex 16.10: invariant vocabulary regenerated (151 keys)
- **Q13** (5): EXP:DELEG-REGEN: row added; R6.DELEG.3: text edit; R6.DELEG.3: Controls: added DELEG-REGEN; R6.CLASS.9: text edit; R6.CLASS.9: Controls: added DELEG-REGEN
- **B-4** (1): EXP:retired: grouped entry replaced by 58 per-id entries read from r6 sec. 33
- **meta** (2): title: text edit (1 occurrence(s)); EXPECTATIONS.json: record_id r6-int-1 -> r6-final-1
- **RE-26** (1): R6.STAT.8: text edit
- **B-10** (1): R6.NOTE.8: text edit
- **B-20** (1): R6.NOTE.13: text edit
- **B-13** (1): R6.PIPE.6: text edit
- **B-12** (1): sec. 3 table op C: text edit (1 occurrence(s))
- **B-14** (1): R6.ANCH.6: text edit
- **RE-31** (1): R6.HP.1: text edit
- **RE-14** (4): R6.OUT.4: text edit; R6.OUT.4: text edit; R6.REC.20: text edit (1 occurrence(s)); R6.REC.20: OPEN flag resolved: isolation class name
- **RE-17** (1): R6.OUT.5: text edit
- **RE-13** (2): R6.OUT.18: text edit; R6.OUT.18: OPEN flag resolved: emitted result fields
- **RE-27** (2): R6.OUT.24: text edit; R6.CLASS.7: text edit
- **RE-32** (1): R6.SPLIT.3: text edit
- **RE-8** (1): R6.REC.10: requirement block restated
- **RE-25** (1): R6.HIT.2: text edit
- **RE-9** (3): R6.GATE.10: text edit; R6.CTRL.27: text edit; OBL-24: text edit
- **B-19** (3): R6.PLAN.16: text edit; R6.PLAN.16: OPEN flag resolved: PLAN.16 countercontrol obligation id; sec. 32 OBL-27/OBL-28: text edit (1 occurrence(s))
- **RE-34** (1): R6.PLACE.8: text edit
- **RE-18** (1): R6.TREE.12: OPEN flag added (remaining): derived-artifact landing blob
- **B-7** (2): R6.TREE.18: Controls: added R18-engine, R19-engine, R17; R6.TREE.18: text edit
- **RE-19** (1): R6.RDIR.13: text edit
- **RE-5** (2): R6.RDIR.14: text edit; OBL-14: text edit
- **C-19** (1): R6.RECON.11: text edit
- **RE-29** (1): R6.RECON.14: text edit
- **RE-22** (2): R6.RECON.20: text edit; R6.RECON.20: Controls: added RT-L2
- **B-11** (1): R6.VALID.1: text edit (1 occurrence(s))
- **Q16** (5): R6.EVID.1: text edit; sec. 31 R6.EVID.7: text edit (1 occurrence(s)); sec. 32 trace table: text edit (1 occurrence(s)); OBL-15: OPEN flag added (remaining): T1'-bound evidence cannot qualify; OBL-16: OPEN flag added (remaining): circular evidence dependency
- **RE-38** (1): OBL-11: Sources: added RE-38
- **RE-37** (3): OBL-13: text edit; OBL-14: text edit; OBL-26: text edit
- **B-9** (1): OBL-21: text edit
- **RE-36** (1): OBL-23: text edit
- **B-6** (1): sec. 33 C1: text edit (1 occurrence(s))
- **B-5** (1): sec. 33 U14: text edit (1 occurrence(s))
- **RE-12** (83): sec. 34 new identifiers: text edit (1 occurrence(s)); EXP:EI14: requirements re-keyed to the requirements that name the row; EXP:EI14-dispatch: requirements re-keyed to the requirements that name the row; EXP:G-A1: requirements re-keyed to the requirements that name the row; EXP:R17: requirements re-keyed to the requirements that name the row; EXP:R18-engine: requirements re-keyed to the requirements that name the row; EXP:R19-engine: requirements re-keyed to the requirements that name the row; EXP:RECLINT-ORPHAN: requirements re-keyed to the requirements that name the row; EXP:RT-L2: requirements re-keyed to the requirements that name the row; EXP:RT-O9: requirements re-keyed to the requirements that name the row; EXP:RT-O9-L2: requirements re-keyed to the requirements that name the row; EXP:RT-T: requirements re-keyed to the requirements that name the row; EXP:TR45: requirements re-keyed to the requirements that name the row; EXP:TR45-opC: requirements re-keyed to the requirements that name the row; EXP:TR5: requirements re-keyed to the requirements that name the row; EXP:U14: requirements re-keyed to the requirements that name the row; EXP:V15: requirements re-keyed to the requirements that name the row; EXP:V27-glossary: requirements re-keyed to the requirements that name the row; EXP:X11: requirements re-keyed to the requirements that name the row; EXP:GATE-1: requirements re-keyed to the requirements that name the row; EXP:GATE-2: requirements re-keyed to the requirements that name the row; EXP:GATE-3: requirements re-keyed to the requirements that name the row; EXP:GATE-4: requirements re-keyed to the requirements that name the row; EXP:GATE-5: requirements re-keyed to the requirements that name the row; EXP:GATE-6: requirements re-keyed to the requirements that name the row; EXP:GATE-7: requirements re-keyed to the requirements that name the row; EXP:GATE-8: requirements re-keyed to the requirements that name the row; EXP:GATE-9: requirements re-keyed to the requirements that name the row; EXP:GATE-10: requirements re-keyed to the requirements that name the row; EXP:GATE-11: requirements re-keyed to the requirements that name the row; EXP:GATE-12: requirements re-keyed to the requirements that name the row; EXP:GATE-13: requirements re-keyed to the requirements that name the row; EXP:GATE-14: requirements re-keyed to the requirements that name the row; EXP:GATE-15: requirements re-keyed to the requirements that name the row; EXP:GATE-16: requirements re-keyed to the requirements that name the row; EXP:GATE-17: requirements re-keyed to the requirements that name the row; EXP:GATE-18: requirements re-keyed to the requirements that name the row; EXP:GATE-19: requirements re-keyed to the requirements that name the row; EXP:GATE-20: requirements re-keyed to the requirements that name the row; EXP:GATE-21: requirements re-keyed to the requirements that name the row; EXP:GATE-22: requirements re-keyed to the requirements that name the row; EXP:GATE-23: requirements re-keyed to the requirements that name the row; EXP:GATE-24: requirements re-keyed to the requirements that name the row; EXP:GATE-25: requirements re-keyed to the requirements that name the row; EXP:GATE-26: requirements re-keyed to the requirements that name the row; EXP:MUT:c2:D02: requirements re-keyed to the requirements that name the row; EXP:MUT:cache:K08: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m1: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m10: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m11: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m12: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m13: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m14: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m15: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m16: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m17: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m2: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m3: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m4: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m5: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m6: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m7: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m8: requirements re-keyed to the requirements that name the row; EXP:MUT:o9:RDIR-m9: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:C08: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:H03: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:I06: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:P01: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:U01: requirements re-keyed to the requirements that name the row; EXP:MUT:v60e:V05: requirements re-keyed to the requirements that name the row; EXP:GATE-27: requirements re-keyed to the requirements that name the row; EXP:GATE-28: requirements re-keyed to the requirements that name the row; EXP:GATE-29: requirements re-keyed to the requirements that name the row; EXP:GATE-30: requirements re-keyed to the requirements that name the row; EXP:LC-1: requirements re-keyed to the requirements that name the row; EXP:LC-2: requirements re-keyed to the requirements that name the row; EXP:LC-3: requirements re-keyed to the requirements that name the row; EXP:LC-4: requirements re-keyed to the requirements that name the row; EXP:LC-5: requirements re-keyed to the requirements that name the row; EXP:LC-6: requirements re-keyed to the requirements that name the row; EXP:LC-7: requirements re-keyed to the requirements that name the row; EXP:DELEG-REGEN: requirements re-keyed to the requirements that name the row; Table 17.1: Requirements column regenerated; rows added: GATE-27 to GATE-30, LC-1 to LC-7, DELEG-REGEN
- **paraphrase** (2): design: 33 requirements marked "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)."; REQUIREMENTS.json: field pending_owner_confirmation added
- **D-1..D-14** (1): MIGRATION.json: record corrections recorded (14)

***

## 3a. Resolution of the 35 OPEN flags of the integrated draft

| OPEN flag | Resolution (decision; where) |
|---|---|
| isolation class name | RE-14: `NOT_ISOLATED`, stderr JSON line (R6.OUT.4, R6.REC.20) |
| V4 reversal scope | RE-1 as qualified: V4, V27, V27-glossary and V15 deferred together, both candidates recorded, gate `deferred-expectation` |
| restored case of no-mutation controls | RE-2 (b) and (c) as qualified by Q11: per-row decisions, 3 exemptions, pairings (R6.CTRL.3, OBL-20) |
| U14 wrong-region-hash class | Q12: exactly `provenance-mismatch` and `stale-adjudication` (R6.HP.7, U14) |
| both-directions scope | RE-3 (c) (R6.CTRL.3) |
| mutation harness location | RE-9 (a): harness and names land, pinned, with the tool revision (R6.GATE.10, R6.CTRL.27, OBL-24) |
| RT-O9 base-drift clause | RE-5 (a): in RT-O9-L2 (R6.RDIR.14, OBL-14) |
| survivors without an equivalence argument | RE-10 (b): limitation and verification defect with a distinguishing control each |
| side-change entry type outcome | RE-15 (a): REVIEW_REQUIRED `side-change-unclassified` (R6.PUR.12, R6.RDIR.7) |
| emitted result fields | RE-13: named fields read by a control or the gate, the rest declared diagnostics (R6.OUT.18) |
| HP merge cross-check | RE-31 (a): ERROR `CONFIG_INVALID` (R6.HP.1) |
| correspondence exemption for non-testable requirements | RE-11 (a): exempt when a verification is named (R6.GATE.12, GATE-30, field `verification`) |
| owner decision quote 7093128173 | RE-26 (a)/(b); R6.STAT.8 marked pending owner confirmation |
| default segment composition | B-13 (R6.PIPE.6) |
| obligation definitions | RE-27 (a) (R6.OUT.24); pin classes RE-27 (b) (R6.CLASS.7) |
| splitter abbreviation match | RE-32 (a): the code's precise readings stated (R6.SPLIT.3) |
| finding-label collision O6 | B-20 (R6.NOTE.13) |
| orphan-record trees | RE-8 as revised in sec. E with Q12 (R6.REC.10, RECLINT-ORPHAN) |
| op A record-check item | RE-23 (a) (R6.CLASS.1, R6.CLASS.11) |
| checker blob source | RE-24 (a) with the Q13 isolation specification (R6.DELEG.3, DELEG-REGEN) |
| HP-region hit class | RE-25 (a): `unclassified`, confirmed by reading the tool commit (R6.HIT.2) |
| landing-list tree | RE-35: the candidate `X` (R6.PROF.11) |
| direction recording field | RE-4 (a): `paired_with`, `direction-missing`, GATE-27 |
| translation implementation | RE-33 (a) with Q15: one definition; LC-1 to LC-7 (R6.TREE.13) |
| RC6 and RC9 | RE-29 (a) for RC9; RC6 a defect, C-19 (R6.RECON.11, R6.RECON.14) |
| RT-L2 on the re-resolved M | RE-22 (a) (R6.RECON.20) |
| EI14-dispatch release condition | RE-21 (R6.GATE.15, OBL-18, EI14-dispatch) |
| tool landing check corpus paths | RE-34 (a) (R6.PLACE.8) |
| engine literals check | RE-19 (b); the check is done (D-4) (R6.RDIR.13) |
| T1' input list | RE-36 (a) (OBL-23); the Q16 trace adds the open item that T1'-bound evidence cannot qualify |
| RD2-RD5 names | RE-28 (b): DIR2-DIR5 (R6.RDIR.5, sec. 34) |
| gate assignments of obligations | RE-37 confirmed; Q16 trace (sec. 32) |
| composite with a NOT RUN component | RE-30 with Q14: precedence ERROR > FAIL > NOT RUN > PASS (R6.GATE.9, GATE-28) |
| PLAN.16 countercontrol obligation id | B-19: OBL-27 |
| expectation of RT-M and RT-SHIFT | B-18: from the cited sources V1-120 and V1-124 (R6.CTRL.11) |

***

## 4. Both directions (Q11, RE-2, RE-3 (c), RE-4) and the derived VD-RESTORE count

Criterion, fixed before the per-row reading: a row is exempt only if (M) its case constructs or applies no change to its input and (A) it is not a positive control asserting acceptance of a valid input; every "yes" or "check" row of RE2-ROWS.md keeps a required opposite direction. A pairing counts as executed only when the paired row has a runner and admits no NOT RUN.

Of the 33 "no" rows, 3 were confirmed to apply no mutation and assert no acceptance (exempt); the other 30 either apply a mutation the mechanical scan missed or are positive acceptance controls, and keep a required opposite direction.

| Row | Scan | Decision | Reason | paired_with |
|---|---|---|---|---|
| B1 | yes | required | the mechanical scan found a mutation or needs a check ("yes"); Q11 keeps a required opposite direction | - |
| B2 | no | required | mutation: the case applies a multi-line splice to the synthetic tree | - |
| B3 | no | required | mutation: the case applies a zero-length insertion (two cases) | - |
| B4 | no | required | mutation: a splice-boundary control (sec. 17 B1-B6) applying a splice at a last line without LF; also asserts acceptance (PASS) | - |
| B6 | yes | required | the mechanical scan found a mutation or needs a check ("yes"); Q11 keeps a required opposite direction | - |
| EI8 | no | required | no mutation, but a positive control asserting acceptance of a valid input (the pre-run check passes on a clean checkout of a valid T) | - |
| K10 | no | required | mutation: a context change on a meaning-context site; also asserts acceptance with a matching adjudication | - |
| K2 | yes | required | the mechanical scan found a mutation or needs a check ("yes"); Q11 keeps a required opposite direction | - |
| K9 | no | required | no further change, but a positive control asserting acceptance (PASS) of a PARTIAL site | - |
| L1 | no | required | mutation: the W1 sentence shifted by 40 lines; also asserts acceptance (PASS) | - |
| L2 | no | required | mutation: the W2 lines moved; also asserts acceptance (PASS) | - |
| N-W | no | required | no mutation, but a positive control asserting acceptance of valid lines (no deny match on the W1 and W2 lines) | - |
| O9 | no | required | no mutation, but a positive control asserting acceptance of a valid input (a complete chain admitted) | - |
| R17 | no | required | mutation: one commit added after X; also asserts acceptance (NO_ITEM) | - |
| RT-A | no | required | no mutation, but a positive control asserting acceptance of a valid record (replay without error, 697 anchors) | - |
| RT-C | no | required | no mutation, but a positive control asserting that 399 splices verify and 44 files conform (acceptance of valid splices) | - |
| RT-D | no | required | no mutation, but a positive control asserting acceptance of the 11 W1/W2 lines by their allow rules | - |
| RT-D-gr58 | no | required | no mutation, but a positive control asserting acceptance of papers/GR.md:58 by its hit classification record | RT-D |
| RT-DR | check | required | the mechanical scan found a mutation or needs a check ("check"); Q11 keeps a required opposite direction | - |
| RT-DR3W | no | exempt (observation) | runs DR-3 alone on two pinned control inputs (AGENTS.md at H and at T1') without constructing any change; asserts the DR-3 sentence count measured on each (one at H, none at T1'), outcome ANY; asserts no acceptance of a valid input | - |
| RT-E | yes | required | the mechanical scan found a mutation or needs a check ("yes"); Q11 keeps a required opposite direction | SW1 |
| RT-H0 | check | required | the mechanical scan found a mutation or needs a check ("check"); Q11 keeps a required opposite direction | - |
| RT-I7 | no | exempt (observation) | runs the item7-literal countercontrol profile on the unmodified trees T1' and H; asserts the per-literal counts measured on them; constructs no change and asserts no acceptance of a valid input | - |
| RT-I7A | no | exempt (observation) | runs the proposed item-7 check on the unmodified trees H and T1' with no records; asserts the FAIL counts measured on them; constructs no change and asserts no acceptance of a valid input | - |
| RT-T | no | required | no mutation, but a positive control asserting acceptance with every reviewed record | RT-T0 |
| RT-T0 | check | required | the mechanical scan found a mutation or needs a check ("check"); Q11 keeps a required opposite direction | RT-T |
| S11-56 | yes | required | the mechanical scan found a mutation or needs a check ("yes"); Q11 keeps a required opposite direction | - |
| S11-57d | no | required | mutation: an added sentence pair; also asserts acceptance (PASS) | - |
| TR48 | no | required | no mutation, but a positive control asserting acceptance of a valid T | - |
| TR5 | no | required | no mutation, but a positive control asserting acceptance of a complete chain-admitted run | - |
| TR5-sim | no | required | no mutation, but a positive control asserting acceptance of a complete control-harness run | - |
| U1 | check | required | the mechanical scan found a mutation or needs a check ("check"); Q11 keeps a required opposite direction | - |
| U10 | no | required | mutation: a ledgered splice rewriting a site line; also asserts acceptance (PASS) | - |
| U11 | check | required | the mechanical scan found a mutation or needs a check ("check"); Q11 keeps a required opposite direction | - |
| U2 | no | required | mutation: three lines inserted above a site; also asserts acceptance (PASS) | - |
| U3 | no | required | mutation: a shift produced by a ledgered splice; also asserts acceptance (PASS) | - |
| U6 | no | required | a synthetic candidate built with a pin-duplicated line; asserts acceptance (PASS) | - |
| V27 | no | required | mutation: added text, alone and as the edited glossary line | - |
| V27-glossary | no | required | mutation: added text as the edited glossary line | - |
| V4 | no | required | mutation: added text (V controls are splices adding the stated text, R6.CTRL.6) | - |
| WB1 | no | required | no mutation, but a positive control asserting acceptance of the W1-c sentence by its allow rule | - |
| WB13 | no | required | mutation: the fingerprinted sentence moved with its neighbours; also asserts acceptance (PASS) | - |
| WB8 | no | required | mutation: the fingerprinted sentence and neighbours shifted by 40 lines; also asserts acceptance (PASS) | - |

Further pairings recorded outside the 43 rows: RT-M with RT-T0 and RT-SHIFT with RT-E (the restored tree of each mutant), and RT-T0 with RT-T (not executed: RT-T is NOT RUN).

Derivation of the VD-RESTORE count (mechanical, in `final.py` section 2):

- integrated file: 192 rows flagged VD-RESTORE;
- exempt as observations: 3 (RT-DR3W, RT-I7, RT-I7A);
- cleared by an executed pairing: RT-T, RT-D-gr58, RT-E, RT-M, RT-SHIFT (5);
- moved out of scope by RE-3 (c) (r6 rows whose source no rule places under it): 13 (CLASS-RETAINED, CLASS-UNLEDGERED, CLASS-PROV-AMBIGUOUS, CLASS-PIN-TARGET, CLASS-RECORD-CHECKS, HIT-REPLACEMENT, PROF-LANDING-LIST, RULE-MINLIT, OUT-CONFINED, REPRO-PYVER, SIDE-NONREG, VD3-COUNT, VD3-CONTEXT);
- in scope by RE-3 (c) with no second direction, newly flagged: 41 (N10, N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, N3, N3-config-route, N4, N5, N6, N7, N8, N9, R15, R18, R18-engine, R19, R19-engine, RT-L, RT-L2, RT-X, TT1, TT10, TT11, TT12, TT13, TT14, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9);
- flagged under C-1 (correction "flag all five"): K3, K4, SW1, EI7-consumer, Z9h (5);
- **final VD-RESTORE count: 217** (192 - 3 - 5 - 13 + 41 + 5).

Of these, 42 rows record no second direction at all and are reported by the gate as `direction-missing` (GATE-27): N10, N11, N12, N13, N14, N15, N16, N16-file, N17, N18, N18-record, N3, N3-config-route, N4, N5, N6, N7, N8, N9, R15, R18, R18-engine, R19, R19-engine, RT-L, RT-L2, RT-X, TT1, TT10, TT11, TT12, TT13, TT14, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9, Z9h.
In scope: 267 control rows; outside: 153.

***

## 5. Q16: evidence kinds and the trace of every obligation gate

Kinds (R6.EVID.7): 1 pre-merge candidate validation (provenance until merged); 2 qualifying landing evidence (the candidate reachable from `main` after the landing merge, AGENTS.md sec. A.42 item 1); 3 post-merge confirmation on `main`; 4 A1 execution evidence gated at `F`.

| Obligation | Gates | Kind | Trace |
|---|---|---|---|
| OBL-1 | plan freeze `F`; trials claiming items 5 or 6 | 4 (the comparison recorded at `F`), by a script landed on `main` before `F` (2) | no cycle |
| OBL-2 | plan freeze `F` | 2 (a retained script on `main` before `F`), or the narrowing | no cycle |
| OBL-3 | plan freeze `F` | 4 (reviewed rule records frozen at `F`) | no cycle |
| OBL-4 | plan freeze `F` | 4 | no cycle |
| OBL-5 | plan freeze `F`; trials claiming item 7 | 4 | no cycle |
| OBL-6 | r6's adoption; plan freeze `F` | the owner's recorded decision (none of the four kinds); 4 for the rule records | no cycle; rests on V5-D1, pending owner confirmation |
| OBL-7 | plan freeze `F`; RT-T's release | 4 | no cycle; RT-T's run at `T1'` cannot qualify (OBL-15) |
| OBL-8 | plan freeze `F`; acceptance of the affected delegated classes | 4 | no cycle |
| OBL-9 | plan freeze `F` | 4 | no cycle |
| OBL-10 | plan freeze `F` | 4 | no cycle |
| OBL-11 | plan freeze `F` | 4 | no cycle |
| OBL-12 | the A1 retirement execution | 4 | no cycle |
| OBL-13 | the tool's landing | 1 only: RT-L2 runs before the tool lands, on the predicted `M`, with `X` = `T1'` and the stand-in `F` | no cycle; the evidence cannot become kind 2 or 3: `T1'` and the stand-in `F` are not reachable from `main` and the predicted `M` exists only before the landing (open) |
| OBL-14 | the tool's landing | as OBL-13 | as OBL-13 (open) |
| OBL-15 | plan freeze `F`; the A1 retirement execution | 4 (records at `F`); RT-T runs at `X` = `T1'` | no cycle; RT-T's run at `T1'` cannot qualify while `T1'` is not reachable from `main` (open) |
| OBL-16 | plan freeze `F` (TR5); the A1 retirement execution (G-A1) | TR5: a host run that needs `F` on `main`; G-A1: 4 | cycle: the freeze of `F` waits for TR5, and TR5 needs `F` on `main`; under AGENTS.md sec. A.39 `F` reaches `main` only with the round's landing after `E` (open) |
| OBL-17 | the A1 retirement execution | 4 | no cycle |
| OBL-18 | acceptance of a chain-admitted result in the A1 retirement execution | a dispatch after the tool lands (3-type, on a branch holding `T'`) | no cycle |
| OBL-19 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-20 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-21 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-22 | the tool's landing | the owner's advance approval and an independent review (governance), with 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-23 | the use of `T1'` figures as acceptance references for the tool's landing | 2 only when the objects of `T1'` are reachable from `main` | no cycle; blocked until those objects land; until then the figures stay historical (RE-36 (a)) (open) |
| OBL-24 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm; the harness lands with the tool revision (RE-9 (a)) | no cycle |
| OBL-25 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |
| OBL-26 | r6's adoption | conformance records of the tool commit a3799244 (provenance) | cycle: r6's adoption is a governed decision whose support must be re-established from `main` (AGENTS.md sec. A.42), the checks read a3799244, which is not reachable from `main`, and a3799244 reaches `main` only through the tool's landing, which follows r6's adoption (open) |
| OBL-27 | plan freeze `F` | 4 | no cycle |
| OBL-28 | the tool's landing | 1 for the landing decision; 2 once the landing merge is on `main`; 3 to confirm | no cycle |

Genuine circular dependencies found (open items, not resolved by any exception):

- OBL-16 (TR5): the gate is the plan freeze `F`; TR5 needs "a plan commit `F` on `main`" (OBL-16 text) and a host `workflow_dispatch` run on it; under AGENTS.md sec. A.39 a round's `F` is designated on its pull-request branch and reaches `main` only with the round's landing after `E`. The freeze would wait for evidence that exists only after the freeze has landed. The cycle disappears only if the plan commit reaches `main` before its freeze is designated, which is an owner decision on the plan's lifecycle.
- OBL-26 (conformance checks): the gate is r6's adoption, a governed decision whose support must be re-established from `main` alone (AGENTS.md sec. A.42); the checks read the tool commit a37992449b452021001277c06c524a30c92dfb87, which is not reachable from `main` and would reach it only through the tool's landing, which follows r6's adoption. Closing it needs either the checked content landed on `main` before adoption (sec. A.42 item 8) or an owner decision.

Evidence that cannot qualify (no cycle, open): OBL-13 and OBL-14 (RT-L2 and RT-O9-L2 run only before the tool lands, on the predicted `M`, with `T1'` and the stand-in `F`, none reachable from `main`, so kind 1 is the only kind they can reach); OBL-15 (RT-T at `X` = `T1'`); OBL-23 (every `T1'` figure). Whether a kind-1-only discharge suffices for the tool's landing gate is an owner question.

No other gate assignment needs evidence to qualify before the merge that makes it qualify: the tool's landing obligations (OBL-19 to OBL-22, OBL-24, OBL-25, OBL-28) are decided on kind 1 and qualify as kind 2 when the landing merge is on `main`, provided their other inputs are on `main`.

***

## 6. Remaining OPEN items

- `derived-artifact landing blob`: R6.TREE.12.
- `T1'-bound evidence cannot qualify`: OBL-13, OBL-14, OBL-15, OBL-23.
- `circular evidence dependency`: OBL-16, OBL-26.
- row flag on LC-7: the byte-exact expected landing blob of a derived artifact needs the regeneration check of RE-18 (a), which no approved text specifies.
- pending owner confirmation: 33 requirements (PARAPHRASED-DECISIONS.md).
- deferred expectations: V4, V27, V27-glossary and V15 (RE-1), decided at r6 adoption.

***

## 7. Residual substantive contradictions and limits

- Testable requirements still without a control (C-26; listed as obligations, not exempt): R6.PIPE.1, R6.PIPE.4, R6.PIPE.6, R6.PIPE.7, R6.PIPE.8, R6.ANCH.8, R6.HP.1, R6.HP.5, R6.HP.14, R6.CTX.8, R6.OUT.16, R6.OUT.22, R6.OUT.25, R6.OUT.28.
- C-1: the eight rows the conformance check lists with a restored case but the file flags VD-RESTORE (A5r, GV7-tool, H4, H7, S11-56, S11-58a-f, TR46, X9), and the direction of G2, X6 and S11-58i, are left flagged until each predicate is read; they are not settled here.
- The gate cannot hold on the final file while any row is `direction-missing` (42 rows), deferred (4 rows), or has no runner; this is the intended fail-closed state of the draft, not a defect of the gate.
- RE-28 renames DIR2-DIR5 by amending OD-31's approved table; the rename needs the independent non-author review of AGENTS.md sec. A.48 item 3 with the migration (OBL-22).
- Q12 applied: `stale-adjudication` is emitted for HP adjudication entries (v1 4.6's scope); orphan context adjudication and hit classification entries stay `record-invalid` under RD-9 (a). This split follows the two approved texts and makes no new choice; the obligation of a `stale-adjudication` item is `HP`, as its table group.
- RE-13: the field classification (named or declared diagnostic) is mechanical, from the keys and count paths the expectations read and the gate's extraction text; a field a future control reads moves to named.
- RE-3 (c) removes the VD-RESTORE flag from 13 r6 rows whose governing source is r6 itself; no approved rule places them under the both-directions requirement. If the owner wants r6's own controls under it, that is option (b) of RE-3, rejected as new work.
- The status quotes at v6.0e lines 17 and 75 and the r5 line 7 authorization are restated by no requirement the mapping locates; v6.0a's item 4 (a later A1 plan-amendment requirement) is not located in r6 (MAPPING note on E-006).
- B-8 (the Z1-Z8 cites of EXPECTATION-SOURCES.json, an input not regenerated here) and B-5's MAPPING rows V1-099 and V2-072 are corrections of input records; they are recorded, not applied to those inputs.

***

## 8. Dispositions of B, C and D

- B-1 (GATE-draft 16.3: remove SKIP from the record statuses): confirmed present (R6.GATE.5).
- B-2 (GATE-draft 16.9: NOT RUN list becomes RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC, EI14-dis): confirmed present (R6.GATE.15, R6.CTRL.5); composites TR45 and EI14 added by inheritance (Q14).
- B-3 (GATE-draft 16.2, 16.4, 16.5, 16.7: add `case`, `composed_of` semantics, `gate_findings_inc): confirmed present (sec. 16); GATE-27 to GATE-30 added.
- B-4 (Retired v6.0e ids (O4, TR4, ..., LN12): copy sec-D's 58 per-id RET rows, read from INVENTO): applied: 58 per-id retired entries.
- B-5 (The U14 retired entry and "withdrawal-needs-decision" labels in the draft; MAPPING rows V1): applied in sec. 33 (U14 not retired); MAPPING rows are input records, not regenerated.
- B-6 (C1's preserved-at is confirmed: TT1 and TT13 (engine R1 and R13) and Y6 (synthetic_fixture): applied (sec. 33 C1 row).
- B-7 (The three role tests map to R18-engine and R19-engine (unclassified change on M gives REVI): applied (R6.TREE.18 names R18-engine, R19-engine and R17).
- B-8 (EXPECTATION-SOURCES Z1-Z8 cites are one line off (D:3080-3086)): kept as the OBL-21 bullet (input record).
- B-9 (E-060: drop "(and L)" from op B): applied (OBL-21).
- B-10 (Restate how C is supplied: `--certified REV`, defaulting to X (cli.py:71; execution.py:61)): applied (R6.NOTE.8).
- B-11 (The 16.6 amendment lists every role-dependent validation: r5 D2-D5, delegation contract, `): applied (R6.VALID.1).
- B-12 (State the landing equation with C, not X): applied (sec. 3 operations table).
- B-13 (Default segmentation stated from the code: one segment pin..commit, unledgered, or `hp` if): applied (R6.PIPE.6).
- B-14 (`whitespace_only`: state its scope (single-line sites, unledgered search, replace opcode;): applied (R6.ANCH.6).
- B-15 (Define RC10 and RC11 independently; sec-C stated RC1-RC13 from `reconcile.evaluate`): confirmed present (R6.RECON.15, R6.RECON.16).
- B-16 (RDIR-16 and RDIR-20 invariants: "authority" becomes "directory not admitted"; always write): confirmed present (RDIR-12b, RDIR-16, RDIR-20).
- B-17 (Add the requirement to the 58 `xref_controls` rows): confirmed by the two-way link check (rows carry the requirements that name them).
- B-18 (Add the rows that approved decisions require: RT-M and RT-SHIFT (demo 2), REPRO-PYVER, OUT): confirmed present; OPEN flag of RT-M and RT-SHIFT resolved.
- B-19 (Give OBL ids to PLAN.16, PLAN.17, PLAN.18 and RECON.21, cross-linked to sec-D's OBL-1 to O): applied (OBL-27 for R6.PLAN.16; PLAN.17 OBL-8, PLAN.18 OBL-4/5/9, RECON.21 OBL-13 present).
- B-20 ("O6" in the verbatim splitter heading is a finding label, not an identifier (NOTE.13)): applied (R6.NOTE.13).
- B-21 (E-018 read as "implementation never adopted by default"): confirmed present (R6.STAT.5).
- B-22 (TT12's cite is execution.py:420-423; line 414 is a dead identical conditional): no execution.py:414 cite remains in the outputs.
- B-23 (RD-19's cite is tools/ledger_coverage.py:29-32): no isolation line cite remains in the outputs.
- B-24 (Confirm by reading that the result names the tool's blob (V2-010's retirement condition)): confirmed by reading the tool commit: `engine.modules` carries the entry point's sha256 and chain-mode snapshots carry `tool_blobs`.

C-1 to C-28: every item is kept as a row of OBL-28 (C-1 also applied its own correction "flag all five"); C-2 and C-8, C-10, C-17, C-21, C-23, C-25 also map to the controls and obligations named in that table.

- D-1 recorded (MIGRATION.json `record_corrections`): "The H-series has only negative cases; no Z10 row concerns adjudication"; U14 is "the only synthetic positive case"
- D-2 recorded (MIGRATION.json `record_corrections`): A matching adjudication holds "with status `adjudicated`"; U14 "does not assert status adjudicated"
- D-3 recorded (MIGRATION.json `record_corrections`): A wrong region hash FAILs "through unauthorized-change"
- D-4 recorded (MIGRATION.json `record_corrections`): r5's engine literals are "against the purity rule"
- D-5 recorded (MIGRATION.json `record_corrections`): RD-8's recommendation (b)
- D-6 recorded (MIGRATION.json `record_corrections`): "31 runner-only controls"; "34 null rows against 32 + 3"
- D-7 recorded (MIGRATION.json `record_corrections`): The schema extension lists the emitted fields, including "per-splice ids and hashes"
- D-8 recorded (MIGRATION.json `record_corrections`): Three role tests "have no confirmed control"; C1 needs a check
- D-9 recorded (MIGRATION.json `record_corrections`): RD-23's list of T1' controls; the implicit assumption that CI evidence is reproducible from main
- D-10 recorded (MIGRATION.json `record_corrections`): "OD-4 needs a conformance check (not yet done)"; RD-27 "needs a check"; E-060 "needs a check"
- D-11 recorded (MIGRATION.json `record_corrections`): A2r applied with literal `(A1)`
- D-12 recorded (MIGRATION.json `record_corrections`): All 223 `restored` rows are sec. 10 controls with U and M
- D-13 recorded (MIGRATION.json `record_corrections`): Rows still without an expectation: "32 runner-only and V4"; engine literals "not checked"
- D-14 recorded (MIGRATION.json `record_corrections`): TT12 "agrees with execution.py:414"; isolation cite 28-31

***

## 9. Self-checks

- completeness: MAPPING rows not cited in DESIGN-r6.md: 0
- consistency: named controls without a row: 0
- consistency: rows naming an unknown requirement: 0
- consistency: rows named by no requirement: 0
- consistency: one-way links: 0
- consistency: rows with expect null: 0
- consistency: retired ids live (row or named control): 0
- consistency: Table 17.1 ids without a row, rows missing from Table 17.1: 0
- consistency: cited requirement ids that do not exist: 0
- consistency: cited OBL ids that do not exist: 0
- consistency: GATE-1 to GATE-30 rows present: 0
- consistency: rows with candidate expectations not DEFERRED: 0
- consistency: superseded names remaining (ISOLATION_REFUSED, RD2-RD5, ...): 0
- consistency: paired_with naming an id that is not a row: 0
- coverage: non-testable requirements without verification: 0
- coverage: testable requirements without a control: 14 (section 7)
- hygiene: no at sign, no temporary-directory path, no github URL, no carriage return and no non-ASCII space in any output: checked
- reproducibility: the generator re-ran itself in a separate process and compared the sha256 of every output before writing; identical
- generator problems: 0
