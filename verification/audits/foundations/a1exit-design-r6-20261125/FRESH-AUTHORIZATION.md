# r6: requirements needing confirmation or fresh authorization

State after the owner's decisions of 2026-11-25 (#1169 comment 7166844576, 2026-11-25T15:26:24Z; quoted in DESIGN-r6.md sec. 0.1). Sec. 1 gives the status of the 46 requirements presented in the previous revision; sec. 2 the classes of the flagged requirements (decision 2); sec. 3 the requirements resting on owner decision S1-D3 (decision 5), which are pending owner confirmation for the adoption decision; sec. 4 the entries of sec. 1 with their exact wording. Every requirement of r6 takes effect only by r6's adoption. A requirement that is not confirmed stays pending, and r6 cannot be adopted while it is pending; it is never withdrawn by non-confirmation (owner decision 5, quoted: "Non-confirmation must leave a requirement pending, not withdraw it."). Withdrawal is a separate, explicit owner choice, with its verification traced (R6.STAT.5).

Decision 1 and 2, quoted:

> 1. Approve the proposed classification.
>
> * Confirm the 22 requirements necessary for valid retirement.
>
> * Confirm the 19 requirements necessary for reliable verification.
>
> * Keep R6.STAT.4 and R6.EVID.5 as scope statements without redundant checks.
>
> * Defer R6.OUT.15 and its dependent offline replay mode.

> 2. Approve the reviewer's classification of the 12 requirements.
>
> Accept the six corrections of overly restrictive rules and the two redundant protections. Resolve the four V4-dependent requirements through decision 3.

***

## 1. Status of the requirements presented in the previous revision

| Requirement | Decision basis | Class | Review's class (decision 1) | Status | Decision 2 class |
|---|---|---|---|---|---|
| R6.STAT.4 | v6.0e line 95 | iii | Redundant with an existing safeguard | scope statement without a check of its own (owner decision 1) | (c) |
| R6.STAT.8 | 7093128173 | ii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.PUR.8 | V5-D1; V5-D2 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.PUR.9 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (d) |
| R6.PUR.11 | v6.0e line 95 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) | (c) |
| R6.ANCH.14 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.CTX.1 | v3 D1-D4 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.CTX.4 | v3 D1-D4 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.CTX.12 | v3 D1-D4 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.OUT.14 | R-D labels; A-D labels | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.OUT.15 | R-D labels | iii | Unrelated to A1 retirement, can be deferred | deferred (owner decision 1) |  |
| R6.PROF.9 | R-D labels; v5.5.9 final D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.RULE.2 | S1-D1 to S1-D3 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (b) |
| R6.RULE.4 | S1-D1 to S1-D3 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (b) |
| R6.RULE.7 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.RULE.8 | S1-D2 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) | (b) |
| R6.RULE.9 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.REC.6 | DI-2 | ii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.7 | DI-2 | ii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.14 | S1-D2 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.18 | R-D labels; v6.0e line 54 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.19 | v6.0e line 31; v6.0e line 54 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.20 | v6.0e line 54 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.21 | v6.0e line 54 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.22 | v6.0e line 54 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.REC.24 | R-D labels | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.DENY.5 | V5-D1; S1-D2; V5-D2; S1-D1 to S1-D3 | ii, iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (b) |
| R6.DENY.6 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (d) |
| R6.CTRL.7 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.CTRL.14 | V5-D1; S1-D1 to S1-D3 | ii, iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.CTRL.15 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (d) |
| R6.CTRL.17 | R-D labels | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.CTRL.19 | S1-D2 | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.CTRL.22 | DI-2 | ii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.CTRL.23 | R-D labels | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.CTRL.24 | S1-D2; R-D labels | iii | Necessary for reliable verification | confirmed by owner decision 1 (necessary for reliable verification) |  |
| R6.PLAN.8 | v3 D1-D4 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (b) |
| R6.A1CFG.7 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (c), R6 |
| R6.EVID.4 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.EVID.5 | S1-D2 | iii | Redundant with an existing safeguard | scope statement without a check of its own (owner decision 1) |  |
| OBL-1 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| OBL-3 | V5-D1; S1-D2; V5-D2; S1-D1 to S1-D3 | ii, iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (b) |
| OBL-6 | V5-D1 | ii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) | (d) |
| OBL-15 | S1-D2 | iii | Necessary for scientifically valid retirement | confirmed by owner decision 1 (necessary for scientifically valid retirement) |  |
| R6.DENY.1 | none (F4) | no decision cited | not classed (would be: necessary for reliable verification) | not marked; takes effect only by r6's adoption |  |
| R6.DENY.2 | none (F4) | no decision cited | not classed (would be: necessary for reliable verification) | not marked; takes effect only by r6's adoption |  |

Not a requirement, listed for completeness: the row of sec. 33 "DR-1d, DR-2 | obsolete: dropped deny candidates (rationale in the appendix); never reused" rests on V5-D1 (class (ii)), whose reversal owner decision 3 accepts. A retired identifier is never reused (AGENTS.md sec. A.30).

***

## 2. Flagged requirements (decision 2; R6)

The flag marks a requirement that permits something an earlier design prohibited, or narrows a check. The owner accepted the review's classification of the 12 requirements flagged in the previous revision: (b) corrections of overly restrictive rules, (c) redundant protections, (d) the four V4-dependent requirements, resolved through decision 3. The reasons are the reviewer's, quoted from REVIEW-r6-round2.md.

| Requirement | Class | Reviewer's reason (quoted) | Resolution |
|---|---|---|---|
| R6.STAT.4 | (c) | Owner approval stays required by AGENTS.md §A.50 items 1, 2 and 5 and must be quoted with author and time (§A.42 item 7). The owner confirms the exact F, T and configuration the tool binds (R6.STAT.3, R6.REC.18 to R6.REC.22). The removal is the owner's own v6.0e decision (line-95 quote, adopted at 7130449822); confirming it does not reopen it. | accepted as a redundant protection (decision 2) |
| R6.PUR.11 | (c) | Same removal as STAT.4, with the same protection. Its added constraint (no output implies approval, control B4-MEANING) is stricter. | accepted as a redundant protection (decision 2) |
| R6.RULE.2 | (b) | Without the allowance, W1-c's legitimate lines would FAIL (contradicting RT-D), and the alternative (dropping `finit` from the negative list) is weaker everywhere. The allowance is bound to one fingerprinted sentence, file and location, used once per tree; deny keeps precedence; R6.REC.14 lints it as exact. | accepted as a correction (decision 2) |
| R6.RULE.4 | (b) | As RULE.2. It is the order of application that enforces the binding. | accepted as a correction (decision 2) |
| R6.RULE.8 | (b) | On proper ancestors of `recorded_at` the fingerprinted sentence does not yet exist, so `rule-stale` there is always a false positive. Every candidate and `recorded_at` stay covered, and skipped rules are reported. | accepted as a correction (decision 2) |
| R6.DENY.5 | (b) | Flagged only for W1-c's allowance (as RULE.2). Otherwise it adds blockers, and the W2 rules replace P's blanket `(A1)` strip, which is stricter. | accepted as a correction (decision 2) |
| OBL-3 | (b) | As DENY.5. | accepted as a correction (decision 2) |
| R6.PLAN.8 | (b) | Item 7's literal grep cannot pass on any tree that keeps W1's legitimate "six structural" lines. The literal check stays as a countercontrol, and acceptance moves to a reviewed plan amendment, which itself needs owner approval under §A.50 items 2 and 5. | accepted as a correction (decision 2) |
| R6.PUR.9 | (d) | This is the V4 reversal: (a) permits what v2 and v4 prohibited. It is the substantive decision the owner deferred to adoption (7160980912, 7162098696, 7163402499). As drafted it permits nothing yet: the rows are DEFERRED and the gate fails on them. | resolved by decision 3, resolution (a) |
| R6.DENY.6 | (d) | Same decision as PUR.9, stated again. | resolved by decision 3, resolution (a) |
| R6.CTRL.15 | (d) | Same decision as PUR.9, stated again. | resolved by decision 3, resolution (a) |
| OBL-6 | (d) | Same decision. OBL-6 is the adoption blocker that carries it. | resolved by decision 3, resolution (a) |
| R6.A1CFG.7 | (c) | R6.A1CFG.7 narrows a check: S13 was temporarily narrower than v6.0e's while V4, V27 and V15 were deferred. The review's class: (c), protection provided by R6.GATE.9 (`deferred-expectation` is a gate failure) and OBL-6 (an adoption blocker until the decision). Under owner decision 3 the four rows carry their expectations and count toward S13, so the narrowing ends with r6's adoption. | flagged under R6 in this revision; confirmed by decision 1; the narrowing ends under decision 3 |

Previously flagged: R6.STAT.4, R6.PUR.9, R6.PUR.11, R6.RULE.2, R6.RULE.4, R6.RULE.8, R6.DENY.5, R6.DENY.6, R6.CTRL.15, R6.PLAN.8, OBL-3, OBL-6. Added under R6: R6.A1CFG.7.

***

## 3. Requirements resting on owner decision S1-D3 (pending owner confirmation for the adoption decision)

Owner decision 5, quoted: "However, do not use adoption as blanket authorization for potentially under-marked S1-D3 requirements. Explicitly identify those requirements and establish their authorization status. Include them in the final adoption decision if necessary."

S1-D3 (class (iii), no GitHub record; DESIGN-v5.5.9.md lines 94-98, CHANGES-v5.2.md line 22) asked to specify the fixes of the Stage 1 review's implementation defects B1-B6. v6.0e sec. 0.2 (inventory item E-034) maps each to the passages and controls that answer it:

- B1: acceptance reads admission; harness results never acceptable; inventory items E-095, E-1191, E-1207; controls X11.
- B2: native delegated execution in a clone at `X`; independent verification; inventory items E-1038, E-1039, E-1040, E-1224, E-1225, E-1226, E-1227, E-1229; controls G4, G5, G6, G7, G8.
- B3: configuration admission from `F`'s pin table; inventory items E-143, E-144, E-145, E-1208, E-1209, E-1210, E-1211; controls TR1, TR2, TR3, TR5.
- B4: commits of `C` classified path by path; widening reviews with coverage; inventory items E-1305, E-162, E-1230, E-1231, E-1232; controls R16, R17, A12r.
- B5: engine purity over the adapter companions; guard pins in the adapter; inventory items E-1377, E-1378, E-1428, E-1233, E-1387; controls Z9g, Z9h.
- B6: control reporting with PASS, FAIL, SKIP and NOT RUN; predicates equal to expectations; inventory items E-1189, E-1190, E-1191; controls none of its own (applies to all controls; the items carry the rule).

Rules, fixed before the marking and applied mechanically to the requirement index:

- Rule A (citation): the requirement's Sources cite one of the inventory items above. These are the v6.0e passages labelled with a Stage 1 B label, their continuation paragraphs and the control rows that E-034 assigns to B1-B6. Excluded: E-1092 to E-1097 (the splice boundary cases B1-B6 of v6.0e sec. 10.1, a label collision), E-014, E-034 and E-1364 (lists of labels), and E-1228 (G9, from the v5.2 review's V7).
- Rule B (control): the requirement's Controls include a control that E-034 assigns to B1-B5 (B6 names RT-T and RT-D only for specific clauses, which rule A covers through E-1190).
- Rule C (text): a keyword reading of secs. 11, 13 and 16 ("harness", "full clone", "native", "path by path", "widening", "guard_pins", "adapter companions", "SKIP", "NOT RUN", "--freeze", "pin table", "admission"); each hit not found by rules A and B was read, and is listed below as marked or as read and not marked.

Found: 54 requirements (rule A 22, rule B only 30, rule C 2). Confirmed by owner decision 1: R6.REC.7, R6.REC.24, R6.CTRL.14, R6.CTRL.23. Marked pending: 50.

Rule B is broad by construction: a requirement tested by a control that S1-D3 introduced or extended is listed although its own content may predate S1-D3 (for example Z9g, the real-engine purity PASS, tests R6.CORE.1 and R6.CORE.2). Confirming such a requirement settles only its authorization; withdrawing it remains a separate, explicit choice.

| Requirement | Sec. | Rule | B labels | Items cited | Controls named | Current authorization status |
|---|---|---|---|---|---|---|
| R6.OUT.12 | 7 | A | B1 | E-095 | X11 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REC.5 | 11 | B | B3 | - | TR2, TR3 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REC.7 | 11 | C | B4 | - | - | confirmed by owner decision 1 (necessary for reliable verification) |
| R6.REC.13 | 11 | A | B4 | E-162 | A12r | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REC.16 | 11 | A | B1, B3 | E-143, E-144, E-145 | TR1, TR2, TR3, X11 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REC.17 | 11 | C | B2 | - | - | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REC.24 | 11 | A | B1, B3 | E-145 | TR5, X11 | confirmed by owner decision 1 (necessary for reliable verification) |
| R6.DELEG.1 | 13 | B | B2 | - | G4 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.2 | 13 | B | B2 | - | G5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.3 | 13 | A | B2 | E-1038 | G4, G5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.4 | 13 | A | B2 | E-1039 | G4, G6 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.5 | 13 | A | B2 | E-1040 | G4, G5, G6 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.6 | 13 | B | B2 | - | G7 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.7 | 13 | B | B2 | - | G8 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.10 | 13 | B | B2 | - | G4, G6, G7, G8 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.12 | 13 | B | B2 | - | G6 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.13 | 13 | B | B2 | - | G7 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.15 | 13 | B | B2 | - | G5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.16 | 13 | B | B2 | - | G4 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.DELEG.18 | 13 | A | B2 | E-1038 | - | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.GATE.5 | 16 | A | B1, B6 | E-1191, E-1189, E-1190, E-1191 | X11 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.GATE.7 | 16 | A | B6 | E-1189 | - | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.GATE.8 | 16 | A | B6 | E-1190 | - | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.GATE.9 | 16 | A | B6 | E-1190 | - | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.GATE.15 | 16 | A | B3, B6 | E-1190 | TR5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CTRL.4 | 17 | B | B2 | - | G5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CTRL.5 | 17 | B | B3 | - | TR5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CTRL.14 | 17 | A | B4 | E-1232 | A12r | confirmed by owner decision 1 (necessary for reliable verification) |
| R6.CTRL.20 | 17 | A | B4 | E-1230, E-1231 | R16, R17 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CTRL.23 | 17 | A | B1, B2, B3 | E-1207, E-1224, E-1225, E-1226, E-1227, E-1229, E-1208, E-1209, E-1210, E-1211 | G4, G5, G6, G7, G8, TR1, TR2, TR3, TR5, X11 | confirmed by owner decision 1 (necessary for reliable verification) |
| R6.CTRL.25 | 17 | A | B5 | E-1233, E-1387 | Z9g, Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.PLAN.2 | 18 | B | B3 | - | TR5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.PLAN.6 | 18 | B | B2 | - | G5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.PLACE.2 | 19 | B | B5 | - | Z9g, Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.PLACE.4 | 19 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.TREE.1 | 20 | B | B4 | - | R16 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.TREE.10 | 20 | A | B4 | E-1305 | R16, R17 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.TREE.18 | 20 | B | B4 | - | R16, R17 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.RDIR.13 | 21 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.1 | 24 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.2 | 24 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.3 | 24 | A | B5 | E-1377, E-1378 | Z9g, Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.4 | 24 | A | B5 | E-1378 | Z9g, Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.5 | 24 | A | B5 | E-1378 | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CORE.6 | 24 | B | B5 | - | Z9g, Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CFG.1 | 25 | B | B3 | - | TR2 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CFG.2 | 25 | B | B3 | - | TR2, TR3 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CFG.3 | 25 | B | B3 | - | TR2 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.CFG.8 | 25 | B | B1, B3 | - | TR1, TR5, X11 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.ADAPT.2 | 26 | A | B5 | E-1428 | Z9h | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.A1CFG.1 | 27 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.A1CFG.2 | 27 | B | B5 | - | Z9g | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.VALID.3 | 29 | B | B3 | - | TR2 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |
| R6.REPRO.1 | 30 | B | B3 | - | TR5 | not confirmed; r6's adoption is not used as its authorization; pending owner confirmation for the adoption decision |

Rule C, read and not marked:

- R6.REC.1: "pin table" names where PIN_OK entries are listed; the record chain predates B3 (E-135).
- R6.REC.15: PIN_OK validity (E-164, RV-019); not the admission passage of B3.
- R6.REC.18: execution identity (R-D3); names the native checker runs only to defer to sec. 13.
- R6.REC.23: host reads; "admission refuses" names the consequence of a failed read.
- R6.REC.25: residual trust; names the admission snapshot.
- R6.GATE.2: "mutation harness" and "NOT RUN" in the schema, not the control harness of B1 or the reporting of B6.
- R6.GATE.10: the mutation harness, not the control harness of B1.
- R6.GATE.13: the gate's own controls (Q1, Q8, RD-2).
- R6.GATE.14: CI under AGENTS.md sec. A.44 (V2-098, Q1).
- R6.GATE.16: RT-L2's NOT RUN rule (OD-18, Q2).

Rule C, marked or confirmed:

- R6.REC.7 (B4): states that a superseding record that widens the record it supersedes carries its widening review.
- R6.REC.17 (B2): states that the native clones of sec. 13 are full clones.

For each pending requirement the options are those of PARAPHRASED-DECISIONS.md: (a) confirm in the owner's own words, (b) fresh authorization, or (c) withdraw, only by an explicit owner choice. If not confirmed, the requirement stays pending and r6 cannot be adopted while it is pending. The wording of each pending requirement, quoted mechanically from DESIGN-r6.md:

### R6.OUT.12

> **R6.OUT.12** Acceptance predicate. A consumer (a workflow step, the plan's checker or a reviewer)
> accepts a run only if all of the following hold:
>
> - the exit status is 0;
> - `result.json` exists in `--out` and validates against schema `oi-ledger-coverage/5`;
> - its `outcome` is PASS, and the independent outcome checker (R6.OUT.23) recomputes PASS from its
>   `preflight`, `record_checks` and `items`;
> - its recorded tool commit `T` and tool blobs equal the blobs the consumer reads itself at `T` from
>   its own verified object store, and these equal the `tool` pins of the configuration at `F` (sec. 11);
>   its adapter module blobs equal the configuration's pins; and its configuration
>   `{path, blob_sha256}` equals the frozen one;
> - `config.admission` is an object whose `mode` is `"chain"` and whose `snapshot` names the same `F`
>   and the same pin table `{path, blob_sha256}` as the landing record.
>
> The schema makes `config.admission` required. A result with a mode other than `"chain"`, or with a
> top-level `"harness"` field, is never acceptable, whatever its outcome; a control harness writes
> `control-result.json` with `"harness": true`, never `result.json`. Only exit 0 is acceptance, and no
> flag converts REVIEW_REQUIRED to PASS.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-095, E-099, V2-045. Controls: X10, X11, ACCEPT-SCHEMA, EI3.

### R6.REC.5

> **R6.REC.5** A failing input is classified by its role, as follows. A conformance check of what the
> code raises precedes adoption; each difference found is a verification defect.
> - **The configuration not admitted** from `F`'s pin table (any failure of R6.REC.10 to R6.REC.11),
>   including a configuration blob that is missing, differs, fails schema or lacks review: ERROR
>   `CONFIG_UNREVIEWED`.
> - **Execution identity** not holding (R6.REC.15, R6.REC.16), including a run record that cannot be
>   read and a `head_branch` other than `main`: ERROR `CONFIG_UNREVIEWED`.
> - **A pinned input missing or differing from its pin**: any input the admitted configuration pins
>   (adapter, record, rule file, profile source, delegation contract, `edits.json`, `ledger.json`),
>   absent at `F` at its path or with a blob whose hash differs: ERROR `SOURCE_CHANGED`.
> - **A pinned input whose content fails its integrity rules**: ERROR with the class the integrity
>   stage names (for example `LEDGER_INTEGRITY` and `SCIENTIFIC_BASE_MISMATCH`, and `LEDGER_INTEGRITY`
>   for an unknown ledger schema id or a failed edit/splice correspondence, R6.PROF.8; RE-16).
> - **A pinned role or tree identity that differs** (`PIN_MISMATCH`, `RECORD_TREE_MISMATCH`,
>   `SCIENTIFIC_BASE_MISMATCH`, `MAIN_NOT_DESCENDANT`, `EDITS_HASH_MISMATCH`): ERROR with the named class
>   (RE-17 (i)). A malformed configuration is refused at admission first (`CONFIG_UNREVIEWED`) in a
>   chain-admitted run and is `CONFIG_INVALID` in a control-harness run (RE-17 (ii)).
> - **The configuration malformed or inconsistent**: ERROR `CONFIG_INVALID`, or `CONFIG_INCONSISTENT`
>   for the consistency checks of sec. 29.
> - **A record whose blob matches its pin but whose content fails its lint or its review**, and a
>   record supplied to the run (for example by `--classify`) that the configuration at `F` does not
>   reference: FAIL `record-invalid` (exit 20). An unreferenced record is never used.
>
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-139, E-140, A-116. Controls: TR2, TR3, CHAIN-REFUSAL, ADM-CONFIG-AT-F, EI2, TR29-tool, O6,
> I2-3, Y10, M3, M4, M5, Z1, Z11, I2-4, I2-5, GV6.

### R6.REC.13

> **R6.REC.13** **Widening of an allow rule.** Any of the following, compared with the superseded
> version, is widening: added files; a changed or shorter literal; fewer context or negative literals;
> any change to the fingerprint set, including a swap with the count unchanged; a larger
> `max_instances`; `context_required` turned off; a new allow rule without `supersedes`; any
> `negative_allowance` added, raised or moved to another fingerprint. **Widening of a deny rule.** A
> changed pattern, a narrower scope, removed examples, or a removed or changed countercontrol.
> **Widening of a scope record.** As R6.RULE.13. Widening needs a `widening_review` record by a
> non-author reviewer other than the record's own reviewer, under the same chain as any review: it names
> the superseding record's blob and the superseded record's blob, its `verdicts` cover every item that
> differs between the two (each changed field, added file, fingerprint or allowance), and every verdict
> is `accept`. A widening review that covers only some items, or names other blobs, is invalid. Widening
> of a record without a valid widening review is FAIL `record-invalid`; widening of the configuration
> without one is ERROR `CONFIG_UNREVIEWED` (R6.REC.5).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-162. Controls: A1r, A2r, A3r, A4r, A9r, A10r, A12r, E-A1r, E-A2r, E-A3r, Y4, Z10.

### R6.REC.16

> **R6.REC.16** **Configuration admission.** The run names the plan commit `F` (`--freeze F`) and the
> configuration (`--config F:<path>`) as explicit inputs; neither is inferred, and both are recorded. Any
> step below that fails, or cannot be completed, refuses with ERROR `CONFIG_UNREVIEWED`:
> 1. **`F` and the configuration.** `F` is a full commit id, read through the verified reader. The
>    configuration is read only from `F`'s tree at the named path, never from a file the caller supplies
>    or from another commit.
> 2. **The pin table.** The pin table is derived, not chosen: it is read from the file `PREREG.md` in
>    the same directory of `F`'s tree as the configuration, as a regular file. Within that file it is the
>    last subsection whose heading matches `^### \d+\.\d+ Record pins\b`; its rows are
>    `` | `<file>` | `<sha256>` | ``, each naming a file of that directory. The configuration and its
>    review record are admitted only if listed there with their sha256. Files beside the configuration
>    that the table does not list are never admitted. A missing `PREREG.md`, no such subsection, or a
>    malformed table row refuses. The run takes no pin-table argument.
> 3. **Scope of the refusal.** These refusals, including the refusal of a run without `--freeze`, apply
>    to chain admission. Every invocation of the tool's command line is an attempt at chain admission.
>    Control-harness admission is available only to the in-process control harness (sec. 17), and replay
>    admission only to the offline replay (sec. 7); neither is reached from the command line.
> 4. **Local runs and replay.** A run outside a host CI job, or one whose run record cannot be read
>    (R6.REC.18 point 1), cannot reach `"chain"`. The offline replay writes `config.admission` with
>    `mode: "replay"` and is never acceptable as a new run.
>
> The record directory of the plan is identified by the configuration's path, which the result
> records; the landing record names it with `F`. The tool also checks that directory against the
> admitted record directories of sec. 21, a constant outside the configuration (sec. 19). Whether `F`
> and the configuration path are the plan commit and record directory the owner designated is confirmed
> procedurally (sec. A.50 items 2 and 5), not by the tool.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-143, E-144, E-145, E-146. Controls: TR1, TR2, TR3, TR13, EI4, ADM-CONFIG-AT-F,
> CHAIN-REFUSAL, TR45-opB, X11, RDIR-16, RDIR-20.

### R6.REC.17

> **R6.REC.17** **Object integrity (the verified reader).** Every read of a commit, tree or blob, in a
> run, by the consumer and in the offline replay, goes through one reader over a local git object store:
> - **Each object verified.** Every object is requested by its full id, and its id is recomputed from
>   its type, length and content. An object that is missing, or does not hash to its id, is an
>   unresolvable object (ERROR, sec. 7), or refuses admission (`CONFIG_UNREVIEWED`). A commit's parents
>   and tree, and a tree's entries and their modes, are parsed from the verified content.
> - **Nothing but verified content.** Refs, reflogs and packed refs are never consulted for a role
>   commit: every role commit is an explicit full id (sec. 1), apart from the re-resolution of `M` before
>   landing (sec. 23), whose result is then read through this reader. Replace refs and grafts are never
>   applied. No parent or ancestry is taken from a traversal command, a graft, the store's `shallow` file
>   or a commit-graph file: first-parent chains and ancestry are computed from parsed parents only.
> - **Bounded walks, no fetch.** Every walk runs between explicit commits. A parent the walk needs and
>   the store lacks is an error; no object is fetched on demand. The native clones of sec. 13 are full
>   clones.
> - **Entries.** Records, rule files, the configuration, the pin table, the delegation contract and the
>   tool's files are read only from regular-file entries (mode 100644 or 100755); any other entry at such
>   a path refuses (ERROR `CONFIG_UNREVIEWED` for an admission read; FAIL `record-invalid` for a record).
> - **Caching.** A cache of verified objects or parsed trees serves only bytes the reader has verified,
>   is keyed by exact object or commit id, and is read-only to its users.
>
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-156. Controls: GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk, O6, GV-CACHE, GV-CACHE-AFTER-READ,
> GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH.

### R6.DELEG.1

> **R6.DELEG.1** **The delegation contract.** The contract is one structured record, `delegation.json`,
> schema `oi-delegation/1`, in the amended plan's record directory beside `ledger.json` and `edits.json`.
> It is frozen with the plan at `F`, its SHA-256 is listed in `F`'s PREREG pin table, and it is
> referenced by the configuration. The tool reads it only as `--delegation F:path`; a hash that differs
> from the pin is ERROR `SOURCE_CHANGED`. It enumerates exact paths, with no globs or prefixes. Its path
> set must equal what the ledger implies: `tex_sources(ledger)` for TeX, and the fixed paths of the other
> classes. A changed path at `X` outside the ledger and the contract is FAIL `unauthorized-change`.
> Evidence not named by the frozen contract is never accepted, however and whenever it is supplied; no
> caller-supplied result is evidence for a class.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1033, E-1034, E-1035, E-1036, E-1037, RV-029, RV-025, RV-007, V2-019. Controls: RT-C, G4,
> S11-14, G-A1.

### R6.DELEG.2

> **R6.DELEG.2** **No blanket delegation of a ledgered file.** A ledgered file is checked by op C's
> conformance (its bytes equal `H` with its splices applied), or by a native class that states its
> regeneration rule and verifies its rebuild at the evaluated tree (`coverage-ledger`, R6.DELEG.15). A
> delegation never absorbs a ledgered file.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: RV-006. Controls: RT-C, G3, G5, S11-4.

### R6.DELEG.3

> **R6.DELEG.3** **Native execution.** Every delegated or native-re-execution class is executed by the
> tool itself against every tree whose delegated paths are evaluated. In the integrity stage the tool
> creates a disposable full clone of the repository at exact `X` under `--out` (no `--depth`, no
> alternates; `X`'s commit and tree ids checked in the clone), and, when `C` differs from `X`, a second
> disposable full clone at exact `C`, checked the same way. No clone runs a configured smudge filter.
> Every class is executed and recorded in each clone separately, with the same independent re-derivation;
> a class PASSes for the run only if it PASSes at `X` and at `C`. The checker the contract names
> (preserve_check) runs only from `F`'s blob, written into a directory under `--out`, never from the
> clone's own copy. A class whose rule is to re-execute the evaluated tree's own generator
> (`check_sc42_integration.py` for `sc42`, `tools/proof_census.py` for `coverage-ledger`) runs that tree's
> own blob in its clone. Every such run uses `python3 -I -B`, runs inside a clone under `--out`, and
> never runs in the user's repository or a worktree of it; this contains preserve_check's
> `git worktree add`.
> Execution isolation (RE-24 (a), Q13). The trusted checkers (preserve_check and every checker the
> contract names) run only from `F`'s pinned blobs. A generator that a class re-executes runs from the
> evaluated tree's blob, and the evaluated tree never decides its own acceptance:
> - isolation: the generator runs in its own disposable clone under `--out`, separate from the clone
>   the checker reads; the run has no write access to the user's checkout and no network access; the
>   interpreter is invoked with the fixed flags `-I -B` and a fixed environment;
> - permitted outputs: only the generated artifact paths the class names, inside the generator's clone;
> - trusted comparison: the checker run from `F`'s pinned blob compares each generated output with the
>   committed artifact byte for byte; the generator's own exit status or report is never the verdict;
> - failure handling: a byte difference is FAIL `regeneration-mismatch`, a generated artifact path not
>   written is FAIL `regeneration-output-missing`, a run beyond the class time limit is FAIL
>   `regeneration-timeout`, and a write to any other path is FAIL `regeneration-extra-write`
>   (obligation `DELEGATED`); none of them is ever PASS.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1038, RV-039, A-057. Controls: G9, G4, G5, O3-FILTER, G-A1, DELEG-REGEN.

### R6.DELEG.4

> **R6.DELEG.4** **Recording.** The tool records, for each run, the checker's blob sha256, its exact
> command line, its working directory, its exit status, and the sha256 of each result file it wrote. It
> then reads the result file it produced itself; a result file supplied from outside the run is never
> evidence for a class that the tool can execute.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1039. Controls: G4, G6.

### R6.DELEG.5

> **R6.DELEG.5** **Independent verification of results.** The tool does not take a checker's verdict
> on trust. For each class it re-derives what it can from the clone: `sc42` compares the re-executed
> output bytes with the committed file itself; `coverage-ledger` compares each of the seven values with
> the census output it produced; `tex` checks the `% source-sha256` stamps and the path set itself, in
> addition to reading preserve_check's result. A checker result that disagrees with the tool's own
> re-derivation is FAIL `delegated-evidence-invalid`.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1040. Controls: G4, G5, G6.

### R6.DELEG.6

> **R6.DELEG.6** **Host-run classes** (`pdf`, `ci`). The evidence is the host's run and job records,
> read by the tool from the host's REST API inside the job (R6.REC.23), never a file supplied by a
> caller. The tool checks `head_sha = X`, the named workflow and jobs, and their conclusions, and that
> the run's event is `push` or `workflow_dispatch` and its repository and head repository ids equal the
> configuration's `repository_id`. For `pdf` it also checks that the PDF comparison result names
> `candidate_commit` and `candidate_tree` equal to `X` (fields the amended preserve_check adds, since
> `--tree` records only a path), that it was produced by preserve_check run by this tool from `F`'s blob
> on PDFs built in the clone at `X`, and that the uploaded artifact's sha256 equals the result's. If any
> of these is absent, the class is REVIEW_REQUIRED `delegated-evidence-missing`; if any is inconsistent,
> it is FAIL `delegated-evidence-invalid`.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1041, RV-043. Controls: G7, S11-3, GV7-tool.

### R6.DELEG.7

> **R6.DELEG.7** **No freeze, no PASS.** Without `F`, every delegated class is REVIEW_REQUIRED
> `delegated-evidence-missing` and can never be PASS; a `plan` field that is null or absent is FAIL
> `delegated-evidence-invalid`. Such runs are not chain runs (R6.REC.16 point 3).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1042. Controls: G8.

### R6.DELEG.10

> **R6.DELEG.10** **Evidence defective**: FAIL `delegated-evidence-invalid`. That is any of: a schema
> other than `a1exit-checker-result-v1` (whose fields are `checker`, `mode`, `plan`, `ledger_sha256`,
> `ledger_base`, `candidate`, `base`, `checks`, each with `name`, `status` and `discrepancies`, and
> `verdict`); `checker` other than `preserve_check.py`; `plan` other than `F`; `ledger_base` or `base`
> other than `H`; `ledger_sha256` other than `F`'s ledger; `candidate` other than the evaluated tree's
> full 40-hex id; a nonzero exit; `verdict` other than `pass`; a required check missing, not `pass`, or
> with non-empty discrepancies; a checker blob that differs from `F`'s copy; a result file the tool did
> not produce in this run, for a class it executes; a disagreement between a checker's result and the
> tool's own re-derivation.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1045, RV-041, RV-030. Controls: G1, G4, G6, G7, G8, Y6, S11-13.

### R6.DELEG.12

> **R6.DELEG.12** **`tex`.** Paths: the TeX files of `tex_sources(ledger)` (A1: Complexity,
> Computation, GR, Main, Methodology, SM, Structure, Substratum and FULL). Delegated: `preserve_check.py
> --commit <tree> --plan F --result-json OUT` in the clone, with the commit-mode checks "candidate against
> base, ledger, regenerated artifacts and plan record" and "scope assertions of amendment sec. 31" both
> `pass`. Native as well: each file's last line is `% source-sha256: <sha256 of the tree's .md>`, and the
> path set equals `tex_sources`; a failure of either is FAIL `delegated-evidence-invalid`.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1048, RV-042. Controls: G6, G1.

### R6.DELEG.13

> **R6.DELEG.13** **`pdf`.** Paths: the PDFs of the same sources. Delegated: `preserve_check.py --tree
> ... --pdf-compare BUILT --pdf-out OUT --plan F --result-json OUT` in the exact-head CI run on `X`, with
> the check "committed PDFs against the CI build (pages, pdftotext)" `pass` and its discrepancies empty.
> Required: `candidate_commit` and `candidate_tree` equal to `X`; a host run record with `head_sha = X`,
> the named workflow and job, and conclusion success; the result hash equal to the uploaded artifact.
> Native as well: each PDF blob differs from `H`'s.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1049, RV-043. Controls: G7.

### R6.DELEG.15

> **R6.DELEG.15** **`coverage-ledger`.** Path: `verification/coverage/LEDGER.json`, a ledgered file.
> Native: its bytes at the evaluated tree equal `H` plus its splices, except the fingerprint values of the
> seven STALE ids; each STALE id occurs exactly once (a missing or duplicated id is FAIL); each replaced
> value equals the fingerprint that `tools/proof_census.py --json` (the evaluated tree's blob, run in the
> clone, exit 0) reports for that id; any other byte difference is FAIL. Each FAIL is
> `delegated-evidence-invalid`.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1052, RV-046. Controls: G3, G5, S11-4.

### R6.DELEG.16

> **R6.DELEG.16** **`sc42`.** Path:
> `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json`.
> Native re-execution only, in the clone at the evaluated tree: the clone contains
> `ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`; `python3 -I -B check_sc42_integration.py --verbose`, plain
> and with `-O`, exits 0 and its stdout is byte-identical to the result file; `--self-test`, plain and
> with `-O`, exits 0 and its stdout is byte-identical to the controls file, which equals `H`'s. No
> delegated evidence substitutes for the re-execution.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1051, RV-045. Controls: G4, G9, S11-13.

### R6.DELEG.18

> **R6.DELEG.18** **Outstanding.** The preserve_check gaps that the plan amendment must close, and the
> decision on its gap 6, are requirements of the plan amendment, not of this design; they are outstanding
> obligations, each a named blocker on the execution of the classes they affect (sec. 32).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1038. Controls: none (OBL-8).

### R6.GATE.5

> **R6.GATE.5** Every runner writes a structured record per control, in the file
> `control-records.json` (schema `oi-control-records/1`): `{id, status, actual, predicate, evidence}`.
> - `status` is one of PASS, FAIL and NOT RUN. A status of SKIP does not exist (RD-7): a control that is
>   deliberately not run is NOT RUN, and a summary never counts NOT RUN as met.
> - `actual` holds every quantity the runner asserted.
> - `evidence` names the control's evidence directory.
>
> A control-harness run writes `control-result.json` with `harness: true` and `config.admission.mode`
> `"control-harness"`, never `result.json`; a consumer rejects it as a result (X11).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1189, E-1190, E-1191, RD-7. Controls: GATE-5, GATE-9, GATE-20, X11.

### R6.GATE.7

> **R6.GATE.7** Every runner retains the raw evidence per control, under `evidence/<job>/<id>/`, with a
> `manifest.json` (schema `oi-control-evidence/1`). For each case the manifest gives:
> - the argv;
> - the exit status file;
> - `result.json` (or `control-result.json`, or the USAGE stderr JSON);
> - the listing of `--out`;
> - the input mutation (paths with blob ids before and after);
> - the bindings;
> - the sha256 of every file.
>
> Where a runner keeps only a summary today, r6 requires the raw evidence named in the procedure library
> (R6.GATE.8) to be retained:
> - for sweeps, per-site item tuples, not whole results;
> - for two-run comparisons, both results;
> - for the purity lint, the lint report, the linted source map and the value set;
> - for host-process properties, the step exit file, the marker-path listing taken after the step, the
>   entry-point sentinel and the import trace;
> - for an external oracle, P's outputs as files.
>
> The evidence set is a CI artifact. Its manifest digest is recorded with the run. Retention on `main`
> follows sec. A.42 when an enduring claim relies on it.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1189, Q1. Controls: GATE-9, GATE-10.

### R6.GATE.8

> **R6.GATE.8** The gate derives `actual` itself and does not trust the runner's `actual` or `status`.
> It imports nothing from `tools/ledger_coverage/`.
>
> - **Declarative, one tool run per case.** The gate reads:
>   - the exit file;
>   - `result.json` (`outcome`, `stop.class`, `items[]` with `obligation`, `class`, `decision`,
>     `subject`, `rule_id`, `alternatives`, `segment` and `fingerprint`, `sites[]`, `finding_counts`,
>     `site_counts`, `hit_counts`).
>
>   It evaluates every `expect` field. It cross-checks `outcome` against the exit file, and it
>   recomputes the outcome from `preflight`, `record_checks` and `items` with its own sec. 7 precedence
>   rule.
> - **Procedural, gate-evaluated.** The gate computes the predicate from retained raw evidence:
>   - `rel-equal`: equality of the item tuples `(obligation, class, segment, fingerprint)` between the
>     named runs;
>   - `sweep`: per site, the set difference against the unmutated tuples;
>   - `set`: an expected set computed from a retained tree listing;
>   - `replay`: byte equality except `config.admission.mode`;
>   - `hash`: equality of `engine.blob_sha256` across two results;
>   - `double-run`: byte equality of the two retained `result.json` files of one operation run twice on
>     equal inputs (argv, configuration blob, object ids and environment) into two fresh `--out`
>     directories (REPRO-DOUBLE, R6.REPRO.2);
>   - `ast`: the gate's own parser or regex applied to retained inputs (a widened rule against its
>     negative examples, the workflow arm text, the clean-path predicate);
>   - `rtl2`: the three-valued RT-L2 predicate (R6.GATE.16).
> - **Procedural, attested with checked evidence.** Where re-execution is impractical, the gate verifies
>   the retained evidence named by the library:
>   - `prerun`: step exit file, marker listing, sentinel, import trace;
>   - `consumer`: the acceptance clauses that decide the case, re-read from the retained result, landing
>     record and snapshot (admission mode, `harness` field, F, pin table, evaluated commits, recorded
>     `T`);
>   - `lint`: the findings list and a non-empty linted source map;
>   - `oracle`: the tool result against P's retained output;
>   - `fixture`: the per-case ls-remote fixture and the landing-check exit.
>
>   In each case the runner's value must equal the value the gate reads.
>
> Real-tree controls run in CI, and their decision rules are the declarative `expect` fields the gate
> re-evaluates; counts are informational unless `expect` states them.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: V2-098, E-1190, Q1, RD-2. Controls: GATE-1, GATE-6, GATE-10, GATE-13, GATE-14, GATE-15,
> GATE-25.

### R6.GATE.9

> **R6.GATE.9** The gate fails (GATE_FAIL, exit 20) on each of the following findings:
>
> - `missing-id`: a row id, or a `composed_of` component, has no record;
> - `unexpected-id`: a record id is not in the file;
> - `duplicate-id`: two records carry one id, within a job or across jobs;
> - `status-not-allowed`: the status is not in `status_allowed`, or is NOT RUN while its `release_check`
>   holds;
> - `declarative-mismatch`: an `expect` field differs from the gate-extracted actual;
> - `procedural-failed`: the named procedure does not hold on the retained evidence, or a row with
>   `composed_of` and its own runner record holds on its own record while a component does not hold;
> - `raw-evidence-missing`: the manifest is absent, a named file is absent or does not match its sha256,
>   or a binding is unbound or does not match the mutation;
> - `status-actual-inconsistent`: the runner's status disagrees with the gate's verdict in either
>   direction;
> - `correspondence-orphan-row` and `correspondence-orphan-requirement` (R6.GATE.12);
> - `expect-null`: a row whose `expect` is null;
> - `direction-missing`: a control row in the both-directions scope of R6.CTRL.3 whose second direction
>   is not recorded (no `restored`, no direction `both`, no `paired_with` and no observation exemption),
>   or whose `paired_with` names an id that is not a row (RE-4);
> - `deferred-expectation`: a row whose `expect` outcome is DEFERRED; it never holds while deferred
>   (RE-1).
>
> An invalid expectation file, record file, mutation record file or manifest schema is the finding
> `file-invalid` and a gate ERROR (GATE_ERROR, exit 65). Otherwise the gate holds (GATE_HOLDS, exit 0).
>
> A difference between an extracted figure and `reference` is reported as `reference-difference` and does
> not change the verdict. Under sec. 31 it blocks acceptance of the implementation step until it is
> explained. A status that a row's `status_allowed` admits as a limitation (R6.GATE.10) is reported as
> `limitation-reported` and does not change the verdict.
>
> The gate writes `gate-result.json` (schema `oi-control-gate/1`): one entry per row with the gate
> status, the extracted actual and its findings. The status counts are reported separately; NOT RUN is
> never counted as met.
>
> A composite row (`composed_of`) preserves every component result: its entry in `gate-result.json`
> lists each component's status and findings. Its aggregate status is the highest-ranked status among
> its own record (where it has a runner) and its components, by the precedence ERROR > FAIL > NOT RUN
> > PASS, so that an ERROR or FAIL of any component is never concealed by a component that is NOT
> RUN. A composite whose aggregate is NOT RUN is NOT RUN with the release condition and release check
> of each NOT RUN component, and is admitted only while each such NOT RUN is admitted; TR45 (component
> TR45-opC) and EI14 (component EI14-dispatch) are such composites. A composite whose aggregate is FAIL
> or ERROR fails as `status-not-allowed` (RE-30, Q14; GATE-28).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1190, Q1, VD-1, VD-10. Controls: GATE-1, GATE-2, GATE-3, GATE-4, GATE-9, GATE-10, GATE-12,
> GATE-16, GATE-17, GATE-20, GATE-26, GATE-27, GATE-28, GATE-29.

### R6.GATE.15

> **R6.GATE.15** `NOT RUN` is allowed only where the row lists it, with a reason and a release
> condition, and only while the row's `release_check` is false on the commit under check. The rows that
> admit NOT RUN are RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch. RT-O9 is gated: its
> own record-directory checks run, and only its dependent clause, RT-O9-L2, is NOT RUN while RT-L2 is
> NOT RUN (Q6). RT-T is NOT RUN until the reviewed records it needs exist.
> The composites TR45 and EI14 are NOT RUN by inheritance while their component is (R6.GATE.9).
> EI14-dispatch's release condition is a dispatch of the pinned workflow on a branch holding `T'`,
> after the tool lands, under a launch the owner approves (AGENTS.md sec. A.50, sec. A.51 item 4); it
> gates acceptance of a chain-admitted result in the A1 retirement execution (RE-21; OBL-18).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: V1-121, E-1190, Q6, RD-6, RD-7, RD-25, RD-26. Controls: GATE-5, GATE-11, RT-T, TR5, G-A1,
> RT-L2, RT-O9, RT-O9-L2, TR45-opC, EI14-dispatch, TR45, EI14.

### R6.CTRL.4

> **R6.CTRL.4** Each expected FAIL names the class of sec. 15 that produces it; a FAIL expectation
> without a class is a defect of the expectation (G3, G5 and the countercontrols of sec. 18 items 4, 6
> and 13 name their class). Each expected deny FAIL names the deny rule and the rule alternative that
> produces it, as measured on the control's own text. Each countercontrol of a deny rule asserts the
> target rule id on the named line or sentence, not only the outcome of the run.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1009, RV-052. Controls: RT-DR, RT-DR3W, A5r, V1, V2, V3, G3, G5, S11-4, S11-6, S11-13.

### R6.CTRL.5

> **R6.CTRL.5** A runner records each control with status PASS, FAIL or NOT RUN. A status of SKIP does
> not exist: a control that is deliberately not run is NOT RUN. NOT RUN is admitted only for a row whose
> expectation lists it together with a reason and a release condition, and only while that release
> condition is false; a summary never counts NOT RUN as met. The rows that admit NOT RUN are RT-T, TR5,
> G-A1, RT-L2, RT-O9-L2, TR45-opC and EI14-dispatch, and, by inheritance from those components, the
> composites TR45 and EI14 (R6.GATE.9).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: V2-073. Controls: RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC, EI14-dispatch, GATE-5,
> GATE-11, TR45, EI14.

### R6.CTRL.20

> **R6.CTRL.20** The tree-role controls are TT1-TT14, R15-R19 with their engine forms, RL and
> SIDE-NONREG, and the real-tree controls RT-X, RT-L and RT-L2, each read with `C` for the certified
> head. v2's `unrelated-authorized` is read as "classified by a side-change class record, or
> `record-directory`", and obligation `MAIN` is kept (sec. 20). TT2 runs v2's old-style comparison of
> `X` against `M` as a countercontrol. TT7 asserts its landing run under the computed composition. TT8
> asserts PASS. TT12 names its class. TT14 is evaluated in the landing check of the tool's own pull
> request (sec. 19). The role tests of v2 addendum 2 map to TT1, TT13 (op C on a correctly executed
> candidate), TT3, TT4, TT7, TT8, TT9, R15 (a first parent other than the recorded `M`), R16 (an
> unclassified path in a commit of `C`) and R18, R19, RDIR-5 (an unclassified change on `M`).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1230, E-1231, E-1321, E-1329, V2-149, V2-150, V2-151, V2-152, V2-153, V2-154, V2-155, V2-156, V2-157, V2-158, V2-159, V2-160, V2-161, V2-148, E-1311, RV-ADD2-259-269. Controls: R15, R16, R17, R18, R18-engine, R19, R19-engine, RL, SIDE-NONREG, TT1, TT2, TT3, TT4, TT5, TT6, TT7, TT8, TT9, TT10, TT11, TT12, TT13, TT14.

### R6.CTRL.25

> **R6.CTRL.25** The synthetic configuration controls are Y1-Y10, Z1-Z8, Z6b, Z9a-Z9h, Z9-STAGED, Z10
> and Z11. Each of Z1-Z8 gives one defect of the fail-closed validation table of sec. 29 in the
> synthetic configuration: Z1 an unknown schema, Z2 a missing required field, Z3 an unknown field, Z4
> an operation not in `operations`, Z5 a reviewer equal to the author, Z6 an unknown adapter interface
> version, Z7 a configuration inconsistency (three cases), Z8 an absent controls file; Z6b gives the
> withdrawn argument `--config-sha256`. Z9h's case is the one in Table 17.1, which combines both of its
> earlier statements. Z9-STAGED is the record of the staged purity job (its record id is `outcome`
> today).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1233, E-1330, E-1381, E-1382, E-1383, E-1384, E-1385, E-1386, E-1387, E-1388, E-1439, E-1440, E-1441, E-1442, E-1443, E-1444, E-1445, E-1446, E-1447, E-1448, E-1457, E-1458. Controls: Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Z1, Z2, Z3, Z4, Z5, Z6, Z6b, Z7, Z8, Z9-STAGED, Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z10, Z11.

### R6.PLAN.2

> **R6.PLAN.2** Every command below adds `--freeze F`, `--config F:<record dir>/retirement-config.json`
> and `--out DIR`, and reads `F`'s records by object id. Profiles, rules, the delegation contract and
> the HP obligations come from the configuration record. A path written `F:...` is resolved through the
> configuration. `X` is the execution head.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1268. Controls: S11-1, TR5, ADM-CONFIG-AT-F.

### R6.PLAN.6

> **R6.PLAN.6** Item 4 (the coverage checker; STALE entries re-affirmed) maps to `execution` with the
> class `coverage-ledger` and the `ci` job `coverage_check`, which the `ci` class's job list includes.
> Countercontrol: one STALE value altered; separately, an id removed. The FAIL names its class.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1272. Controls: S11-4, G5.

### R6.PLACE.2

> **R6.PLACE.2** `tools/ledger_coverage/engine/` holds the engine (sec. 24), its JSON Schemas, the
> outcome checker and the in-memory self-test fixtures; no fixture file is tracked. This directory is
> the purity scope of the purity lint.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1292, V2-114. Controls: Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z9-STAGED.

### R6.PLACE.4

> **R6.PLACE.4** Constants that bound what a configuration may claim form a named exception class: such
> a constant lives in a pinned tool file outside the engine, never in a configuration, since a
> configuration cannot admit itself. The class has one member, the tuple of admitted record directories,
> exactly
> `('verification/audits/foundations/a1exit-deletion-20261121',)`,
> held in its own module `tools/ledger_coverage/record_authority.py` (the module keeps its name; it
> predates the term "admitted record directories"). The engine contains no retirement constant. The
> module is a tool file like any other: listed in `tool.files`, pinned by the tool-landing class record
> and checked by the pre-run pin check. No configuration, record or command-line argument adds to the
> tuple; changing it is a tool revision.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: A-009, A-020, A-023, A-024. Controls: RDIR-16, MUT:o9:RDIR-m4, TR48, Z9g.

### R6.TREE.1

> **R6.TREE.1** `execution` takes the roles below as flags, each resolved once to a full commit id and
> recorded in the result's `roles`:
> - scientific base `H` (`--scientific-base`): what the retirement edits are relative to (spans, old
>   hashes, pins, sites);
> - integration base `M` (`--main`): which side changes the landing must carry;
> - candidate `X` (`--candidate`): the retirement's own tree;
> - certified execution head `C` (`--certified`, optional): when absent, `C` equals `X`;
> - landing `L` (`--landing`, optional): the merge commit, or an in-memory merge for prediction.
>
> `C` is the certified execution head throughout; `E` is only the ledger pin.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: V2-124, E-1300. Controls: TT1, TT5, TT6, R16.

### R6.TREE.10

> **R6.TREE.10** When `C` differs from `X`, `C` descends linearly from `X`. Each commit `c` after `X` on
> that chain, with parent `p`, is classified path by path, as `X` is against `H`: every path in the diff
> from `p` to `c` is in exactly one class (ledgered, delegated or record); a ledgered path equals `H`'s
> bytes with the ledger's splices applied; a delegated path is checked by its class at `C`; a record
> path is one the plan's record directory admits after `F`. Any other changed path is FAIL
> `unauthorized-change`, naming the commit. A commit with more than one parent is FAIL
> `candidate-parent`. The tree of `C` is then checked as a whole, as `X` is.
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1305. Controls: R16, R17.

### R6.TREE.18

> **R6.TREE.18** The role cases are each tested: an unclassified change on `M` gives REVIEW_REQUIRED
> (R18, R19, RDIR-5); a first parent other than the recorded `M` fails (R15); an unclassified path in a
> commit of `C` fails (R16, with R17 for a record path admitted after `F`); R18-engine and R19-engine
> are the engine forms of R18 and R19 (B-7); op C on a correctly executed candidate gives PASS (TT13).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: RV-ADD2-259-269. Controls: R18, R19, RDIR-5, R15, R16, TT13, R18-engine, R19-engine, R17.

### R6.RDIR.13

> **R6.RDIR.13** The literals the rule needs in the engine are engine enumerations: the reserved class id
> `record-directory`, the reason strings (`absent at M`, `absent at F`, `differs from F`, `not a regular
> file`, `outside the record directory`, `directory not admitted`) and the reserved prefix `.github/`.
> The reserved class id
> `record-directory` is an enumeration that the purity lint's enumeration rule admits. The reason
> strings pass the lint's occurrence rule and are not allowlisted. The reserved prefix `.github/` is a
> path literal that no enumeration admits; it moves to `record_authority.py`, which bounds what a
> configuration may claim (OD-5's exception class), in the tool revision (RE-19 (b); OBL-28).
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: A-035, A-037, A-041. Controls: Z9g, Z9-STAGED.

### R6.CORE.1

> **R6.CORE.1** The tool has one engine. Every operation (`record`, `coverage`, `execution`, `terms`)
> is a configuration of that engine, not a separate code path. The engine is retirement-independent and
> contains exactly:
> - the pipeline of sec. 3;
> - the outcomes, exit codes, precedence, acceptance checker and result writer of sec. 7;
> - the algorithms: anchors, translation and content search (sec. 4), the overlap and image rules
>   (sec. 4), the region walk and merger reporting (sec. 5), the context hash, the indicator machinery
>   and structure contexts with definitions supplied by the configuration (sec. 6), sentence splitting
>   version 2 with the abbreviation list supplied by the configuration (sec. 8), rule application and
>   record lint (sec. 10, 11);
> - the four role checks (sec. 20);
> - the object reader of sec. 11 (`git cat-file --batch`, with recomputed object ids);
> - the adapter interface definitions (sec. 26) and the loader that admits adapter modules by pinned
>   blob;
> - the configuration loader and validator (sec. 25, 29);
> - the purity lint Z9 (R6.CORE.3).
>
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: V2-012, E-1375. Controls: Y8, Z9g.

### R6.CORE.2

> **R6.CORE.2** The engine contains no commit or tree id, no path of a retirement record, no
> retirement terminology, regex pattern, site or hit count, PR number, delegation class, context-field
> value, adapter name or checker schema. Adapters, which carry their retirement's schema strings (for
> example "a1exit deletion exact-edit ledger v2"), lie outside the engine, in
> `tools/ledger_coverage/adapters/`. The following literals are engine enumerations and are listed by
> name in the allowlist of R6.CORE.5: the reserved side-change class id `record-directory`, the reason
> strings of the record-directory rule (`absent at M`, `absent at F`, `differs from F`,
> `not a regular file`, and the reasons naming DIR2-DIR5 and `directory not admitted`), and the path
> prefix `.github/` used by condition DIR3. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1376, RD-20. Controls: Z9a, Z9b, Z9c, Z9d, Z9g.

### R6.CORE.3

> **R6.CORE.3** Z9, the purity lint, runs over the source blobs of `tools/ledger_coverage/engine/` and
> the entry point `tools/ledger_coverage.py`, parsed by `ast`. Its scope is exactly those blobs; adapter
> modules and `record_authority.py` are outside it. It fails on any of:
> - a hexadecimal literal of 7 or more hex digits standing alone, in a string or as a number, including
>   any 40-hex literal;
> - a string literal equal to a string value of the value set, unless the value is on the allowlist. The
>   value set is every string value occurring in the A1 configuration, in a record it references, in any
>   record its adapters read (the adapter companions: `ledger.json`, `edits.json`, `sitemap.json`,
>   `rows.json`, the Phase-0 `sites.json`, and every other file named in an adapter's `path` or
>   `companion`), and in the synthetic configuration;
> - a string literal or identifier matched by any review or deny profile of the A1 configuration.
>
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1377, E-1378, RD-31. Controls: Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h.

### R6.CORE.4

> **R6.CORE.4** The engine reads nothing from a ledger but the fields of the ledger interface
> (R6.ADAPT.2). Retirement semantics such as guard-pin handling (an edit kind `guard-pin`, `pin_note`
> values, a literal-piece filter, a read of a ledger field outside the interface) belong to the ledger
> adapter, which returns them through the interface field `guard_pins`. With the adapter companions in the
> value set, a planted `'guard-pin'` in an engine module is a lint FAIL (Z9h), and the real engine tree
> with the extended value set gives no finding (Z9g). Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1378, RD-31, MC-9. Controls: Z9g, Z9h.

### R6.CORE.5

> **R6.CORE.5** The allowlist is fixed in the engine and is itself linted to contain only:
> - the interface field names of sec. 26 and of the engine's record schemas (for example `id`, `file`,
>   `start`, `end`, `new`, `old_sha256`, `new_sha256`, `splices`, `sites`, `base`, `files`, `retained`,
>   `mirrors`, `site_id`, `pin_line`, `carried`, `row`, `code`, `owner`, `author`, `reviewer`,
>   `reviewed`, `verdicts`, `supersedes`, `path`, `blob_sha256`, `segment`);
> - the engine's own schema ids, as listed by the schema files of sec. 7 and sec. 11 (among them
>   `oi-ledger-coverage/5`, `oi-retirement-config/1`, `oi-term-rules/2`, `oi-delegation/1`,
>   `oi-hp-adjudication/1`, `oi-context-adjudication/1`, `oi-hit-classification/1`, `oi-scope/1`,
>   `oi-side-change-classes/1`, `oi-reconciliation/1`, `oi-review-record/1`);
> - the engine's own enumerations: outcome names, sec. 15 class names, ERROR and configuration class
>   names, extractor kinds, `review`, `deny`, `tree`, `added-text`, `accept`, `reject`, `dissent`, and the
>   enumerations named in R6.CORE.2.
>
> Allowlisting a value that also occurs in a companion (for example a control id equal to a row code)
> requires that the value be an engine enumeration listed by name. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1379, E-1378, RD-20,
> OD-24. Controls: Z9e, Z9g.

### R6.CORE.6

> **R6.CORE.6** Z9's controls run the lint on an in-memory engine tree (Z9a-Z9f) and on the real engine
> tree (Z9g). Z9f's adapter half lints the real adapter sources: its linted source map is non-empty and
> includes the adapter modules. Z9 runs in CI and in `self-test`; a failure in `self-test` is VOID. The
> purity job records its result under the control id Z9-STAGED. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1380, VD-9, RD-25. Controls:
> Z9a, Z9b, Z9c, Z9d, Z9e, Z9f, Z9g, Z9h, Z9-STAGED.

### R6.CFG.1

> **R6.CFG.1** A retirement is configured by one reviewed, versioned JSON record,
> `retirement-config.json`, in the retirement plan's record directory, frozen with the plan at `F` and
> held under the ownership chain of sec. 11. Its SHA-256 is listed in the pin table of `F`: the last
> `Record pins` subsection of the `PREREG.md` beside the configuration in `F`'s tree (sec. 11). Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources:
> E-1389, E-1390. Controls: TR2, ADM-CONFIG-AT-F.

### R6.CFG.2

> **R6.CFG.2** The tool reads the configuration only as `--config F:<path>` from the object store,
> never from a caller-supplied file or another commit. A configuration that is not admitted from `F`'s
> pin table (absent from it, or with a hash different from its listed SHA-256) is ERROR
> `CONFIG_UNREVIEWED`, exit 65. ERROR `SOURCE_CHANGED` is reserved for an input that the admitted
> configuration pins (R6.VALID.3). Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1391, OD-4. Controls: TR2, TR3, EI4, ADM-CONFIG-AT-F.

### R6.CFG.3

> **R6.CFG.3** A change to the configuration after `F` requires a new configuration version, with
> `supersedes` naming its predecessor, and a new freeze. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1392. Controls: TR2, LN4.

### R6.CFG.8

> **R6.CFG.8** Admission is recorded in `result.json` as the object `config.admission` with members
> `mode` and `snapshot`. `mode` is one of `chain`, `replay` and `control-harness`; only `chain` is
> acceptable (sec. 7, sec. 11). For `chain`, `snapshot` carries the fields sec. 11 lists: the producing
> run, `T` and its tool blobs, `F`, the pin table and the evaluated commits. The requirement that a run
> have `--freeze` (TR1) applies to chain admission only. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: OD-29, OD-28, E-1459. Controls: TR1,
> TR5, TR13, TR45-opB, X11.

### R6.ADAPT.2

> **R6.ADAPT.2** The ledger interface returns: `base`; `splices [{id, file, start, end, old_sha256,
> new_sha256, new}]` (byte spans at `base`); `files {path: {base_sha256, expected_sha256}}`;
> `retained [{id, site_ref}]`; `mirrors [{id, mirror_of}]`; `guard_pins [{id, file, pieces, targets}]`
> (the updated pin literals the edit list requires, with the retirement's own selection rules applied
> inside the adapter); `ignored_fields`; and its validation errors (overlap, hash, schema). Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources:
> E-1428. Controls: U10, U11, M3, M4, M5, Z9h.

### R6.A1CFG.1

> **R6.A1CFG.1** The A1 configuration is `a1exit-retirement-config`, version 1. Every A1 constant lies
> in that configuration, in a record it pins, or in an A1 adapter module it pins, with one named
> exception class: constants that bound what a configuration may claim. Its one member is the tuple of
> admitted record directories, held in `tools/ledger_coverage/record_authority.py`, a tool file outside
> the engine, listed in `tool.files`, pinned by the tool-landing class record and checked by the pre-run
> pin check. No configuration, record or command-line argument can add to it; changing it is a tool
> revision. For this revision the tuple is exactly
> `('verification/audits/foundations/a1exit-deletion-20261121',)`. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1433, A-019, A-020,
> A-022, A-024, OD-5, OD-6. Controls: RDIR-16, RDIR-20, Z9g, EI1.

### R6.A1CFG.2

> **R6.A1CFG.2** The A1 constants have these destinations:
>
> | Constant | Destination |
> |---|---|
> | `E`, record commit, `R` tree b05efdca935a42b9c94ef1748c964696bf58fcd9 | `roles.pin`, `roles.record_commit`, `adapters.replay.record_tree` |
> | `H` | `roles.scientific_base` |
> | `R` paths and the Phase-0/2 record paths | `adapters.sitemap`, `adapters.replay.module_path` |
> | ledger and edits schema ids, `retained_unchanged`, `mirror_of` | the `a1exit-exact-edit/2` module, `adapters.ledger.companion` |
> | frozen function names, line-523 handling | the `python-frozen-replay/1` module, `adapters.replay.functions` |
> | corpus `papers/*.md`, `book/*.md` | `corpus` |
> | profiles p0-core, p0-para, ledger-ext, ptr, repo, count-grep, item7-literal, register, infinity | `profiles` (sources: Phase-0 `sites.json`; `R/ledger_check.py` `EXTENDED_PATTERNS`; `P` `edits_check.py` `PTR`, `REPO_PAT`, `REG`, `CAPS`, `CAPS_OK`, `INF`, `NEUTRAL`; the item 7 literals of sec. 18) |
> | `resid` (resid-a, resid-b, resid-c), DR-1, DR-3, DR-4, DR-5, W1, W2, the converted `EXPLAINED` entries | rule files under `rules` (plan records adopted at `F`, sec. 12), profiles naming them |
> | item 7 and item 11 profile sets and `final_profiles` (`item7`: `ptr`, `count-grep`; `item11`: `repo`) | `checks` |
> | DR-3's control-only witness input (`AGENTS.md` at `H`) | `controls` |
> | repo scope (historical prefixes and files, generated artifacts) | a scope record under `records` |
> | s3 mapping (sec. 6) | `context_mapping` (`source_field: s3`) |
> | ANAPH, LIST, TABLE, PARTIAL definitions and effects | `indicators` |
> | sentence abbreviations | `sentence.abbreviations` |
> | the six pinned merges and PR numbers (R6.A1CFG.4) | `hp_obligations[0]` (segment `[E, H]`) |
> | tex/pdf/record-dir/sc42/coverage-ledger/ci classes, STALE ids, SC42_BASE ca3a5bb2, `tex_sources` rule, `a1exit-checker-result-v1` | `delegation.json` and the class adapters' parameters in it |
> | the tool's file and workflow pins; the repository id 1156244443 | `tool`, `repository_id` |
> | W's workflow, the tool's landing paths | `roles.side_change_classes` |
> | every HP, context, hit classification and review record, including `context-adjudications.json` and `hit-classifications.json` | `records` |
> | the admitted record-directory tuple | `record_authority.py` (the exception of R6.A1CFG.1) |
> | controls RT-*, SW*, the sec. 18 mapping and countercontrols | `controls` (operations, direction, control inputs); expected results in the expectation file |
>
> Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3).
> Sources: E-1434, A-019, A-020, A-022, A-115, OD-5, OD-8. Controls: Z9a, Z9b, Z9c, Z9d, Z9g.

### R6.VALID.3

> **R6.VALID.3** A pinned or configuration input that fails is classified by its role:
> - the configuration is not admitted from `F`'s pin table, its review chain is missing or failing, its
>   reviewer equals its author, or it widens without review: ERROR `CONFIG_UNREVIEWED`;
> - an input that the admitted configuration pins (adapter module, record, rule file, profile source,
>   companion) is missing or differs from its pin: ERROR `SOURCE_CHANGED`;
> - the configuration is malformed or names an undefined record kind: ERROR `CONFIG_INVALID`;
> - the configuration is internally inconsistent: ERROR `CONFIG_INCONSISTENT` (R6.VALID.4);
> - an execution-identity failure, such as a producing run whose head branch is not `main`: ERROR
>   `CONFIG_UNREVIEWED`;
> - a pinned input whose blob matches its pin but whose content fails its integrity rules (an unknown
>   ledger schema id; the ledger integrity failures of M3-M5): ERROR `LEDGER_INTEGRITY`, or the
>   named integrity class (`SCIENTIFIC_BASE_MISMATCH`); never `SOURCE_CHANGED` (RE-16);
> - a pinned role or tree identity that differs: ERROR with the named class (RE-17 (i)); a malformed
>   configuration is refused at admission first in a chain-admitted run (`CONFIG_UNREVIEWED`) and is
>   `CONFIG_INVALID` in a control-harness run (RE-17 (ii));
> - a record whose blob matches its pin but whose content fails its lint or its review, or a record
>   passed with `--classify` that the configuration does not reference: FAIL `record-invalid`.
>
> All ERROR outcomes here exit 65. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1453, E-1454, A-116, OD-4, RD-18. Controls: TR2, Z5,
> Y10, O6, I2-3, I2-4, Z1, TR29-tool, M3, M4, M5, TT5, O2.

### R6.REPRO.1

> **R6.REPRO.1** Every `result.json` records:
> - `config`: `{config_id, version, path, commit, blob_sha256, admission: {mode, snapshot}}`
>   (R6.CFG.8);
> - each adapter's interface, name, version, module blob hash and input blob hashes;
> - each profile's name, source commit, path, blob and `pattern_sha256`;
> - every rule file's path and blob, and the id of every rule applied (in each explanation);
> - every record and review record used, by path and blob;
> - the delegation record hash and each class adapter version;
> - the HP obligation's pinned merges;
> - the tool commit `T`, the run's repository, head repository and event, and the engine blob hash (the
>   entry point and every engine module), each tool blob equal to its `tool` pin;
> - for the record-directory rule: the directory `D_rec`, the admission match, the outcomes of DIR2-DIR5,
>   and the directory-completeness counts (paths equal, paths unequal by reason), with each classified
>   side change listed as in sec. 21.
>
> The complete field list is the result schema of sec. 7. Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3). Sources: E-1459, A-058, A-059, OD-24, OD-29,
> OD-6. Controls: ACCEPT-SCHEMA, S7-schema-and-checker, TR5, X10, Y8.

***

## 4. Entries of sec. 1

### R6.STAT.4

Status: scope statement without a check of its own (owner decision 1).
Decision basis: `v6.0e line 95`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.STAT.4** Owner authorization is procedural. The approvals AGENTS.md requires (sec. A.50: freezing
> and designating the plan, dispatching its trials, executing it, merging into `main`; sec. A.45 rule 3
> and sec. A.51 for work) are given by the owner and quoted with author and time in the record that
> relies on them (AGENTS.md sec. A.42 item 7). The tool neither reads nor checks them. No check of this
> design is waived by r6, and every later step keeps its own owner gate (sec. 19).
> Scope statement by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1); it has no check of its own.
> Sources: E-012. Controls: none (procedural boundary).

- Purpose: Fixes the boundary between technical verification and owner authorization: approvals are procedural, quoted in the relying record, and the tool neither reads nor checks them.
- If confirmed: The tool accepts a run on a plan commit `F` whose technical identity checks hold, whether or not the owner designated it; only the owner's procedural confirmation and the quoted record establish approval.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): r6 states no boundary for authorization. v6.0e (adopted, #1169 comment 7130449822) contains the same boundary, so withdrawal would need a replacement statement.
- Safeguards affected: Removes, relative to v5.5.9, the automated detection of an undesignated plan or an unapproved authority change; every technical identity check (R6.REC.18 to R6.REC.22) is kept.
- Flag, earlier designs: v5.5.9 (final decision D4) required automated verification of owner authorization through the authority record, versioned comment forms and numeric owner id 7273571; r6, like v6.0e, does not.
- Decision 2: class (c).
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.STAT.8

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `7093128173`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.STAT.8** Landing order. The owner decision recorded by the coordinating session in #1169 comment
> 7093128173 (posted from the `amaybaum` account, 2026-11-23T06:13:50Z; a session-written record that
> quotes no owner words) approved in principle that the tool lands first, that the plan's `PREREG.md` is
> amended and re-frozen so that every mandatory check of its sec. 11 passes as written, and that the four
> trees are distinguished (sec. 20). It superseded the execution-exception route of comment 7092885251.
> The steps it held (implementation, push, pull request, merge and the plan edit) are each governed by
> their own owner record; r6 releases none of them. Before adoption the decision is quoted in r6 in the
> owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26);
> since the comment holds no owner words, the owner restates it.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: RV-002. Controls: none (governance record).

- Purpose: Records the landing order of the exception-free route: the tool lands first, then PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written, with the four trees distinguished.
- If confirmed: r6 records the route as the basis of its gate order (sec. 32); the steps it held stay governed by their own owner records.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The gate order of sec. 32 loses its recorded basis and would need another.
- Safeguards affected: Preserves the absence of an execution exception and the requirement that the plan passes as written.
- Note: confirmed as a requirement; the restatement of the landing-order decision in the owner's words, which the requirement itself needs before adoption, is still owed.

### R6.PUR.8

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `V5-D2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PUR.8** Lexically unanchored paraphrases. The deny rules close only forms with a fixed lexical
> anchor. A paraphrase without such an anchor cannot be closed by a regular expression. On added text,
> the outcome is at least REVIEW_REQUIRED only for the classes that the plan's pinned `resid` rule file
> (sec. 12) or another review profile matches. Those classes are the content of the plan's rule files,
> which are control inputs pinned at `F`, not requirements of the tool. For the rule files current when
> r6 was drafted they are, informatively:
>
> - a finiteness word together with a posit noun (posit, premise, axiom, assumption, hypothesis) within
>   a 60-character window of one sentence;
> - a state-space noun (configuration, state or phase space) followed by "is finite" or a similar
>   copula;
> - "finite set", with at most one word between;
> - "substratum", "universe" or "world" followed within 40 characters by "is", "be", "being" or "are",
>   an optional article and at most one word, and "finite";
> - "finite number" or "finite count" of states, configurations, elements, points or sites.
>
> A paraphrase outside the classes the pinned rule files match stays outside the tool; its detection
> rests on the plan's independent review of the exact head. Constructed examples outside those classes,
> which PASS when added: "the six posits of the substratum", "six assumptions about the substratum",
> "The posit ledger lists fourteen.", "the fourteen-item posit ledger" and "$A_1$–$A_6$". The plan's
> original literal item 7 misses each of these too. The two examples of R6.PUR.9 are not part of this
> requirement.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-055. Controls: V15, V21, V26.

- Purpose: States the coverage limitation for lexically unanchored paraphrases: only the classes the pinned `resid` rule file or another review profile matches reach REVIEW_REQUIRED.
- If confirmed: Constructed paraphrases outside the pinned classes PASS; the tool claims no complete semantic detection; the classes are plan-record content frozen at `F` (OBL-3).
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The limitation is unstated, which would leave the tool's coverage claim undefined.
- Safeguards affected: Matches v6.0e sec. 1 and the limitation recorded in #1169 comment 7099655517. The REVIEW guarantee for the listed classes holds only once the reviewed `resid` record is frozen at `F`; resid-b and resid-c rest on V5-D2. None of the listed constructed examples matches the form of DR-1d or DR-2 (computed, V4-COMPARISON.md), so dropping those rules did not change their outcome; whether any other v4 rule caught them was not determined in this round.

### R6.PUR.9

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PUR.9** The residual for the deny rule DR-2, decided by owner decision 3 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1); the decision takes effect
> with r6's adoption. The two texts "the framework's sixth structural property, finiteness of the bijection" (control
> V4) and "The framework's sixth structural property is finiteness of the substratum" (control V27)
> match no deny rule once DR-2 is not in the active rule set, and PASS when added; the plan's original
> literal item 7 misses both. Whether the tool's expected outcome for these texts is PASS (an accepted
> residual) or FAIL (the expectation of DR-2's form restored) was an owner decision (RD-14, Q10) among
> these options:
>
> - (a) confirm the accepted residual: V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED,
>   kept so that a change in their outcome is visible;
> - (b1) restore the FAIL expectation of V4, V27 and V27-glossary, which needs a plan rule record of the
>   DR-2 form in the plan's active rule set under a new identifier (DR-2 is retired and never reused,
>   sec. 33), while V15 stays REVIEW_REQUIRED through `resid`;
> - (b2) as (b1), and restore V15's FAIL expectation as well, which needs a second plan rule record, of
>   the DR-1d form, under a second new identifier (DR-1d is retired, sec. 33); a rule of the DR-2 form
>   does not match V15's text.
>
> The decision covers V4, V27, V27-glossary and V15 together, which rest on the same decision V5-D1
> (RE-1). For each row, (a) selects the candidate "reversal adopted" and (b2) the candidate "reversal
> rejected"; (b1) selects "reversal rejected" for V4, V27 and V27-glossary and "reversal adopted" for
> V15. Owner decision 3 chose (a), in the owner's words: "Accept the reversal and retain human review for V15." and "Do not introduce additional rules based solely on constructed examples without an established scientific or verification need." The owner's caveat, quoted: "This is a decision about the automated checker's scope, not permission to make scientifically unsupported claims about finiteness." Each of
> the four rows carries the expectation of the candidate "reversal adopted" as its `expect`, and no deny
> rule is added. The outstanding-evidence blocker on this requirement, that the owner decision V5-D1 that
> dropped DR-2 was recorded only in paraphrase in the session-written #1169 comment 7099655517 (ME-6), is
> discharged by the text of decision 3.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-055, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: States the decision on the V4 reversal, resolution (a) of owner decision 3, and the resolutions not chosen.
- If confirmed: V4, V27 and V27-glossary expect PASS and V15 REVIEW_REQUIRED through `resid`; the four rows count toward S13; no deny rule is added.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The decision and the option statement are lost; the four rows would have no stated basis.
- Safeguards affected: Records the owner's decision and caveat; a rejection would have needed a new rule identifier (F5), and V15's FAIL a rule of the DR-1d form (F6).
- Flag, earlier designs: Resolution (a) permits V4, V27 and V27-glossary to PASS and V15 to be REVIEW_REQUIRED, where v2's demonstration expected V4 FAIL and v4 expected V4 and V15 FAIL `deny-match` (DR-2, DR-1d). Chosen by owner decision 3 (V4-COMPARISON.md).
- Decision 2: class (d).

### R6.PUR.11

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `v6.0e line 95`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.PUR.11** Approval is outside the tool. The tool verifies which exact plan, configuration, tool and
> evaluated commits a run checked, and identifies them in its result. Whether that plan is the one the
> owner approved is confirmed by the owner, procedurally (R6.STAT.4). No output, outcome, field or
> control of the tool states or implies that a plan, a record, a run or a result was approved or
> authorized. Admitted record directories are named "admitted", never "authorized" (sec. 21).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-057. Controls: B4-MEANING.

- Purpose: Keeps approval outside the tool: no output, outcome, field or control states or implies approval or authorization.
- If confirmed: Outputs carry no approval vocabulary (B4-MEANING); admitted record directories are "admitted".
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): B4-MEANING would lose its requirement.
- Safeguards affected: Prevents a technical result from being read as an authorization; it removes no technical check.
- Flag, earlier designs: Same removal as R6.STAT.4 relative to v5.5.9.
- Decision 2: class (c).
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.ANCH.14

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.ANCH.14** Boundary cases.
>
> - A splice overlaps a site if `start < site_end` and `end > site_start`. A zero-length splice at an
>   interior offset also overlaps. A splice that only touches a site's boundary does not.
> - A hit line is "in a splice image" if it contains the splice's offset in `X`. Empty images are
>   included (for example D029 at Substratum.md:268).
> - A removed site (empty image) has no replacement region; the line holding its offset is reported with
>   the removal, not counted as a region line.
> - A last line without LF is a line. Its span ends at end of file.
> - A site's span is its line's bytes plus its terminating LF. A splice that starts at the site line's LF
>   therefore overlaps the site, and the replacement region includes the lines it inserts.
>
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-110, E-111. Controls: B1, B2, B3, B4, B6.

- Purpose: Fixes the boundary cases of splice overlap and site spans (the LF-inclusive span of Stage 1 D4).
- If confirmed: A splice starting at a site line's LF overlaps the site; the replacement region includes inserted lines (215 region lines rather than 203).
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The boundary cases are unspecified; the region count would not be determined.
- Safeguards affected: Stricter than v4 (more regions attributed).

### R6.CTX.1

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.1** Preregistration. The context rule was decided at S0, before any implementation output. It
> is stated per frozen s3 value and per indicator. Its authority is r6's adoption. Its counts at `T1'`
> are reported, never tuned.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-076. Controls: none (definition).

- Purpose: Preregisters the context rule at S0, per frozen s3 value and indicator, with its counts reported and never tuned.
- If confirmed: The mapping is fixed before any counts; T1' counts cannot be used to adjust it.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The context rule loses its preregistration requirement.
- Safeguards affected: Preserves preregistration (v3 D2).

### R6.CTX.4

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.4** Meaning. Context is required for meaning exactly when the frozen record does not establish
> that the qualification is visible on the site's own line. A `per unit` status stays on the required
> side: it means the qualification was established by a unit's correction, which may sit in a
> neighbouring sentence. The mapping from each frozen s3 value to `meaning_context` is part of the A1
> configuration (sec. 27):
>
> | Frozen s3 value | Sites at `E` (informative) | `meaning_context` |
> |---|---|---|
> | visible (names the hypothesis); rewritten at deletion | 194 | false |
> | visible (P0/P1/P2 disposition) | 144 | false |
> | visible (applied splice) | 5 | false |
> | visible (none: the (NR) corollary ...) | 3 | false |
> | n/a | 136 | false |
> | not determined: Q3 census | 81 | true |
> | not determined | 28 | true |
> | per unit regression audit (#1468) | 45 | true |
> | per unit Q1 corrections (Step 2) | 28 | true |
> | per unit Step-2 phase | 15 | true |
> | per unit R6 corrections (Step 2) | 9 | true |
> | per unit R1/R2 scoping | 8 | true |
> | per unit Q2 | 1 | true |
>
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-079, RV-012, V2-032. Controls: K1, K3, K4.

- Purpose: Defines when context is required for meaning and fixes the s3-to-`meaning_context` mapping, with `per unit` on the required side.
- If confirmed: Sites with a `per unit` status require context (12 meaning-context failures rather than 8).
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The mapping, or the `per unit` reading, is undecided; narrowing `per unit` to false would remove 4 failures.
- Safeguards affected: Stricter reading kept (v3 D2: "per unit stays true").

### R6.CTX.12

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTX.12** For LIST and TABLE sites the neighbour context of R6.CTX.2 is kept in addition to the
> structure contexts of R6.CTX.11: a change of either gives the result of R6.CTX.6.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1367. Controls: K7.

- Purpose: Keeps the neighbour context for LIST and TABLE sites in addition to the structure contexts.
- If confirmed: A change of either context gives the result of R6.CTX.6.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Only the structure contexts would apply to LIST and TABLE sites.
- Safeguards affected: Stricter than D2's wording; the v4 review found it correct.

### R6.OUT.14

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `R-D labels`, class (iii) no GitHub record; `A-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.OUT.14** Durable evidence (A-D5, C3, R-D5). Acceptance is recorded only by landing it on `main` in
> a landing record, the result commit. The landing merges only with the owner's approval (AGENTS.md
> sec. A.50 item 1), which the record quotes with author and time; the tool does not read or check that
> quotation. The record commits:
>
> - the result, compressed deterministically: `result.json.gz`, the gzip of the exact result bytes with
>   a modification time of 0, no file name, compression level 9 and the operating-system field 255; the
>   sha256 of the uncompressed bytes decides, and the compressed bytes' sha256 is recorded as well;
> - the admission snapshot of sec. 11, and its sha256;
> - the reproducibility recipe: the commits, including `F` and `T`; the configuration, pin table,
>   engine, adapter and workflow blob hashes; the exact command; and the tool version.
>
> CI run ids, job ids and log references are recorded as provenance only (AGENTS.md sec. A.42 item 2).
> Committing a result preserves it; it never makes an invalid run acceptable. The predicate of
> R6.OUT.12 is re-checked from the committed data before the landing merges.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-097. Controls: TR46.

- Purpose: Requires acceptance to be recorded only by an owner-approved landing record on `main` that commits the deterministic compressed result, the admission snapshot and the reproducibility recipe.
- If confirmed: No result is accepted until it lands; a compressed blob whose uncompressed hash differs is refused (TR46); CI identifiers are provenance only.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Durable evidence for tool results is unstated in r6, although AGENTS.md sec. A.42 items 1-2 and sec. A.50 item 1 still require its substance.
- Safeguards affected: Preserves v5.5's durable evidence; the clause "the tool does not read or check that quotation" is the same boundary as R6.STAT.4.

### R6.OUT.15

Status: deferred (owner decision 1).
Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.OUT.15** Offline replay (C3, F2). `replay --snapshot <path> --out DIR` recomputes the result from
> git objects and the committed snapshot alone. Admission is taken from the snapshot and written as
> `"admission": {"mode": "replay", ...}`. For op C, every delegated and native class is decided from the
> snapshot's delegated evidence (sec. 11). Replay does not call the host, clone the repository, build
> PDFs or rerun any checker. It re-applies the tool's own verification rules of sec. 13 to the recorded
> host records, hashes and checker outputs and to the git objects, for example: the TeX stamps and path
> set; LEDGER.json against `H` plus its splices and the recorded census values; SC-42's committed file
> against the recorded `--verbose` output; and the recorded `pdf` and `ci` records against `X`'s ids and
> the artifact hash. Every recorded result file must hash to the sha256 recorded beside it. Apart from
> the admission field, the replay's output equals the committed result byte for byte (canonical JSON,
> R6.OUT.19), for op B and op D results as well as for op C results. A replay is never acceptable as a new
> run. One thing remains host-attested and cannot be reproduced offline: that the snapshot was genuine
> when it was taken.
> Deferred by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1), together with the `replay` mode of R6.REC.24 and control TR45-opB. The text above is kept as the deferred specification; it binds no tool revision until a recorded owner decision takes it up. Accountable Issue: #1169. A committed result is re-established under AGENTS.md sec. A.42 item 1 by R6.OUT.14's recipe and a re-run on `main`.
> Sources: E-098. Controls: TR45-opB.

- Purpose: Specifies offline replay from git objects and the committed snapshot alone, re-applying the tool's verification rules to the recorded host records.
- If confirmed: A committed result can be re-established without the host; a replay is never acceptable as a new run.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): No offline replay is specified, so a committed result could be re-checked only by a new host run.
- Safeguards affected: Adds a check (TR45-opB); the snapshot's genuineness at capture stays host-attested.
- Deferral: with the `replay` mode of R6.REC.24 and control TR45-opB; accountable Issue #1169; the expectation rows TR45-opB and TR45 are unchanged in this revision (DESIGN-r6.md sec. 0.1).

### R6.PROF.9

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `R-D labels`, class (iii) no GitHub record; `v5.5.9 final D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.PROF.9** **Where the tool is stricter than P.** The tool computes and records P's per-edit
> result for items 5 and 6 in every case, including a refusal, so no item-5 or item-6 verdict differs
> from P's. It refuses three kinds of input that P, which has no splices, would not refuse, each because
> it is an invalid or ambiguous input: (i) a splice for the variant P does not select (the frozen ledger
> then misrepresents the frozen edit list); (ii) one splice covering two edits (the ledger schema gives
> each splice exactly one edit `id`), even where its bytes equal P's combined application; (iii) chained
> edits: a later edit's selected occurrence lies wholly or partly inside an image an earlier edit
> inserted, or spans the point where an earlier edit's image, possibly empty, was inserted, so that in
> the segment model it crosses more than one segment. No set of disjoint splices at `H` can express such
> an application, and a frozen plan containing one is invalid.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-121. Controls: S11-58g, S11-57c, S11-58j, S11-58k.

- Purpose: States the three input classes the tool refuses beyond P, while recording P's per-edit items 5 and 6 results in every case.
- If confirmed: Unselected-variant splices, two-edit splices and chained edits are refused; no item-5 or item-6 verdict differs from P's.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): These inputs would not be refused.
- Safeguards affected: Stricter than P.

### R6.RULE.2

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.2** **Allow rule.** Its fields: `id` (never reused); `profiles` it addresses;
> `scope.files`, exact paths, mirrors named explicitly; `matcher.literal`, which must contain the
> trigger, defined as the profile match span of each fingerprinted sentence at `recorded_at`;
> `matcher.context`, required co-occurring literals in the sentence or its neighbouring sentences (for
> example the enumerated list); `matcher.negative`, literals or regexes that must not match;
> `context_required`; `max_instances`, equal to the number of fingerprints; `fingerprints`, each
> `{file, sentence_sha256, context_sha256, negative_allowance}`, where the optional `negative_allowance`
> maps a negative literal to the number of its matches in that exact fingerprinted sentence;
> `recorded_at`, the commit at which the fingerprints were taken; `positive_examples` and
> `negative_examples`, at least one of each, which become controls; `reason`, the semantic reason in one
> or two sentences; `author`. The reviewer and the review are a separate review record bound by blob
> (sec. 11). Owner approval is procedural and is not a rule field (R6.REC.3).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-128, V2-048, RV-015. Controls: A6r, A8r, A7r, E-A6r, E-A8r, lint-ok.

- Purpose: Defines the allow-rule schema, including the fingerprint field `negative_allowance` (S1-D1 option B).
- If confirmed: A fingerprint may carry an exact per-literal allowance bound to one sentence.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The schema has no allowance; W1-c's lines would FAIL `rule-negative-match`, contradicting RT-D, unless `finit` were dropped from the negative list.
- Safeguards affected: A narrowly bounded exception to the negative matcher; the alternative (dropping `finit` from the list) would weaken it for every sentence. The last sentence ("Owner approval is procedural") rests on the line-95 decision.
- Flag, earlier designs: v5.1 had no allowance, so W1-c's lines were FAIL `rule-negative-match`; option B permits one exact match per fingerprinted sentence.
- Decision 2: class (b).

### R6.RULE.4

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.4** For a hit, the steps run in this order:
> 1. If no allow rule has the hit's file in scope, with a literal covering the trigger and a context
>    matcher that holds, the hit stays REVIEW_REQUIRED `unclassified`.
> 2. If any deny profile matches the sentence, the result is FAIL `deny-match`. Deny takes precedence.
> 3. The rule's negative matcher is applied to the whole sentence, with every negative literal counted.
>    The allowance for the sentence is the `negative_allowance` of a fingerprint only if all of the
>    following hold, and is zero otherwise: the hit's file is the fingerprint's `file`; the sentence's
>    sha256 equals the fingerprint's `sentence_sha256`; the context sha256 equals the fingerprint's
>    `context_sha256`, whether or not the rule sets `context_required`; and that fingerprint has not
>    already granted its allowance to another sentence in this tree. If, for any negative literal, the
>    sentence has more matches than the allowance grants, the result is FAIL `rule-negative-match`. The
>    allowance is bound to one fingerprint, that is, one fingerprinted sentence at one fingerprinted
>    location; it is never a global count and cannot be used by any other sentence, file or location.
> 4. If the sentence or, when required, the context differs from every fingerprint, the result is
>    REVIEW_REQUIRED `rule-fingerprint-mismatch`.
> 5. If the rule has already been applied `max_instances` times in the tree, the result is FAIL
>    `rule-overreach`.
> 6. Otherwise the hit is classified by the rule.
>
> A fingerprint with no `negative_allowance` grants none. A literal's matches are counted as
> non-overlapping matches of the literal (or regex) in the sentence's source bytes. The explanation of
> the hit records each step with its result (sec. 7).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-130, V2-050, V2-052. Controls: L1, L2, L3, L4, S1r, V7a, V7c, A5r, A5r-generic, E-L1, E-L3,
> E-S1r, rule-negative, WB1, WB4, WB6, WB7.

- Purpose: Fixes the order of allow-rule application, with deny taking precedence and the allowance bound to one fingerprint once per tree.
- If confirmed: A negative-literal match is tolerated only within one exact sentence's allowance at one location, once per tree; anything else FAILs.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): As for R6.RULE.2.
- Safeguards affected: As for R6.RULE.2; deny still overrides everything.
- Flag, earlier designs: As for R6.RULE.2.
- Decision 2: class (b).

### R6.RULE.7

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.7** **Case.** Literal entries of an allow rule's negative matcher are matched
> case-insensitively, for every allow rule; a regex entry keeps its own flags. Allowances count
> case-insensitive matches. **Matching on source bytes.** Every literal of an allow or deny rule
> (trigger, context, negative, fingerprinted sentence) is matched against the source bytes of the file
> as committed, after the splitter's whitespace normalization (sec. 8), never against rendered text
> (for example a context literal `\mathrm{SU}(3)`, as the source line holds it, not "SU(3)").
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-133. Controls: WB15, L2, V7a.

- Purpose: Matches negative literals case-insensitively and matches every rule literal on source bytes (Stage 1 D8).
- If confirmed: Literals cannot be evaded by case or by rendering differences.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Case and rendering are unspecified; a context literal could be matched against rendered text.
- Safeguards affected: Stricter.

### R6.RULE.8

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.8** **`rule-stale` scoping.** REVIEW_REQUIRED `rule-stale` (a fingerprinted sentence no
> longer present) is evaluated on every tree except those that are proper ancestors of the rule's
> `recorded_at`, computed from parsed parents (R6.REC.17). A candidate `X`, `C`, `L` or `M`, and
> `recorded_at` itself, are always evaluated. `result.json` lists, per tree, the rules not evaluated for
> staleness and why. At `recorded_at` a missing fingerprint is a lint failure of the rule (R6.RULE.10),
> not a `rule-stale` item.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-134, V2-028. Controls: S2r, WB5, E-S2r, GV3.

- Purpose: Scopes `rule-stale`: not evaluated on proper ancestors of `recorded_at`; always evaluated on the candidates and on `recorded_at`, with skipped rules listed (Stage 1 D7).
- If confirmed: A fingerprint missing on an ancestor of `recorded_at` raises no item; at `recorded_at` it is a lint failure.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The scope of `rule-stale` is unspecified.
- Safeguards affected: Narrows where `rule-stale` is raised (proper ancestors are excluded); every candidate and `recorded_at` stay covered, and the skipped rules are reported.
- Flag, earlier designs: Narrows v2: DESIGN-v2.md sec. 3.3 (V2-028) makes `rule-stale` REVIEW_REQUIRED whenever "a rule's fingerprinted instance occurs nowhere in the tree", with no scope; r6, like v6.0e (E-134), does not raise it on proper ancestors of `recorded_at`, where the fingerprinted text had not yet been written.
- Decision 2: class (b).

### R6.RULE.9

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.RULE.9** **Residual testing.** No rule ever deletes text from the line or sentence before
> testing. A classified hit's sentence is tested whole, with the classified literal in place: every
> deny profile (step 2) and the rule's negative matcher (step 3) are applied to the whole sentence, and
> every other profile's hits in it are decided on their own.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-134, V2-051. Controls: V7a, WB2, WB12, A5r.

- Purpose: Forbids deleting text before testing: a classified hit's sentence is tested whole.
- If confirmed: Deny profiles and negative matchers see the whole sentence.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Residual testing by deletion would be possible.
- Safeguards affected: Stricter than v2's residual-test mutation.

### R6.REC.6

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.REC.6** A record fails, with FAIL `record-invalid`, on any of these: a schema or field error, or
> a missing field; no review record naming exactly this record's blob, or a review record naming another
> blob; `reviewer` equal to `author`; a review whose `verdicts` do not cover every item id of the record,
> or any item not `accept`; a duplicated item id or verdict; a `reviewer` value that points to a tool
> run, a CI run, a check run or an Issue (a URL or run id rather than a person); a record entry at a
> path that is not a regular file (R6.REC.17); a record not read from the git object store.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-140, E-141. Controls: O1, O2, O3, O5, R3-F2, R4-B3, R4-B3-DUP, R5-N6, GV6.

- Purpose: Lists the conditions under which a record fails lint with `record-invalid`.
- If confirmed: Records without an exact review, with self-review, incomplete verdicts or non-person reviewers FAIL.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The record lint loses its failure conditions.
- Safeguards affected: Stricter.

### R6.REC.7

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.REC.7** **Supersession and lineage**, for every record kind that carries `supersedes`. Each
> `supersedes` names a `{path, blob_sha256}` that exists in the object store at or before `F` and is a
> record of the same kind, schema and lineage; a first record has `supersedes: null`. A record's lineage
> is its `record_id`, a non-empty string at the record's top level; for the configuration it is its
> `config_id` (sec. 25). `record_id` is immutable within a lineage: a superseding record has the same
> kind, schema and `record_id` as the record it names. Sharing a `record_id` within one lineage is not
> reuse; a `record_id` carried by two records that do not lie on one `supersedes` chain is. Each of the
> following is FAIL `record-invalid`:
> - a chain naming an id or blob that never existed as a record (for example an off-repository draft);
> - a record without a valid `record_id` (missing, empty or not a string) that supersedes another
>   record or is named by a `supersedes`;
> - a `supersedes` naming a record whose kind, schema or `record_id` differs, at any step of the chain;
> - a `supersedes` naming a predecessor that does not itself pass this lint, read from the object store
>   at or before `F` and verified independently of the superseding record (its own review and, where it
>   widens the record it supersedes, its widening review);
> - a cycle in a `supersedes` chain;
> - ambiguous ancestry: two records superseding the same predecessor, among the records in the audit
>   directory and the plan's record directory at `F` and the records the run reads; or a lineage with
>   two heads used in one run, a head being a record of the lineage that no other record the run reads
>   (the records the configuration references and every record their chains name) supersedes;
> - a reused `record_id`.
>
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-141. Controls: S4a, LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, R6-G6.

- Purpose: Specifies supersession and lineage of records by `record_id` (DI-2, option A, narrow).
- If confirmed: Chains to nonexistent records, kind or schema changes, cycles, ambiguous ancestry and reused ids FAIL `record-invalid`.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Lineage is unspecified; superseding records could change kind or identity.
- Safeguards affected: Stricter.

### R6.REC.14

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.14** **Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its
> named file at `recorded_at`. Each example and countercontrol must behave as stated. Every fingerprinted
> sentence, read at `recorded_at` in its named file, must be classified PASS by its own rule through
> steps 1-6 of R6.RULE.4, with its own allowance. Every `negative_allowance` must equal, literal by
> literal, the number of matches of that negative literal in its fingerprinted sentence, and may name
> only literals of the rule's negative matcher. A rule's positive examples include each fingerprinted
> sentence in full, not a fragment of it. Otherwise the record fails the lint (FAIL `record-invalid`).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-163. Controls: A6r, A8r, A9r, A11r, WB10, WB11.

- Purpose: Requires each fingerprinted sentence to PASS its own rule and each allowance to equal the exact literal count (Stage 1 D1).
- If confirmed: A rule whose own sentence does not PASS, or whose allowance is inexact, is `record-invalid`.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The lint would not catch a self-contradictory rule.
- Safeguards affected: New and stricter.

### R6.REC.18

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `R-D labels`, class (iii) no GitHub record; `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.18** **Execution identity.** An acceptable result is computed by the tool files and run by
> the workflow that the configuration at `F` pins, in the repository it names:
> 1. **The run record.** The tool reads its own run record by the run id the host assigns, from the
>    host's REST API in the repository the job runs in: the repository id, the head repository id, the
>    event, the head branch, the workflow path and the run's `head_sha`. `T`, the tool commit, is that
>    `head_sha`. The run's `repository.id` and `head_repository.id` must both equal the configuration's
>    `repository_id`, and its `event` must be `push` or `workflow_dispatch`.
> 2. **The tool's files and the workflow.** `T`'s tree is read through the verified reader. Under
>    `tools/ledger_coverage/`, together with the entry point `tools/ledger_coverage.py`, it must hold
>    exactly the files of the configuration's `tool.files`, each a regular file whose blob sha256 equals
>    its pin; a further file, a missing file, a differing blob, or a symlink, submodule or other
>    non-regular entry refuses. The run record's workflow path must equal `tool.workflow.path`, and the
>    blob at that path in `T` must equal `tool.workflow.blob_sha256`. The workflow runs the tool with
>    `python3 -I -B` from a checkout of `T`. Before evaluating anything, the tool compares the entry point
>    and every file under `tools/ledger_coverage/` in that checkout with `T`'s tree: the same set of
>    paths, each byte-identical. Any difference, including a file on disk that `T` does not hold (for
>    example a compiled-bytecode file), refuses.
> 3. **Evaluated commits are inputs.** The commits evaluated (`X`, `C`, `L`, `M`, `H` and `E`) are
>    explicit full ids, read through the verified reader and recorded. They are never the run's
>    `head_sha`.
> 4. **The consumer repeats it.** The consumer repeats points 1-3 and the `uses:` check of point 5 for
>    the producing run itself (sec. 7), from the host's REST API and from its own verified object store,
>    against the configuration at `F` that the landing record names. A run whose repository, head
>    repository or event fails point 1, a `head_sha` other than the `T` the result records, or a tool or
>    workflow blob that differs from the configuration's pins is non-acceptance.
> 5. **Nothing unpinned executes.** In every run of the pinned workflow, no file outside `tool.files`,
>    the pinned workflow, the actions it names by commit id and the interpreter's own standard library
>    executes in the job, before or after the tool's own checks. The delegated and native checker runs
>    are outside this rule and are governed by sec. 13 (R6.DELEG.3).
> 6. **The tool commit is on `main`.** The tool refuses (ERROR `CONFIG_UNREVIEWED`, before any
>    evaluation) unless the run record's `head_branch` is `main`. The consumer requires `T` to lie on the
>    first-parent chain of `M`, the `main` resolved by `git ls-remote` as sec. 23 states, walked by the
>    verified reader.
>
> No command-line option, environment value or other configuration field sets `tool` or
> `repository_id`; they are read only from the configuration at `F`.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-147, E-148, E-149, E-150, E-155. Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer,
> TR29, TR29-tool, TR30, TR48, TR50, TR51, TR52, EI1, EI2, EI2-consumer, EI3, EI5, EI14.

- Purpose: Binds an acceptable result to the tool files, workflow and repository pinned by the configuration at `F`, with the tool commit on `main`.
- If confirmed: Runs from another repository or event, off `main`, or with unpinned or extra tool files are refused, by the tool and by the consumer.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Execution identity is unspecified.
- Safeguards affected: Preserves v5.5.9's technical identity guarantees, pinned through the configuration at `F` rather than the authority record.
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.REC.19

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `v6.0e line 31`, class (iii) no GitHub record; `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.19** **The pre-run pin check.** The first step after the checkout and the fetch of `F`,
> before the entry point or any file of the checkout runs, is one fixed inline step of the pinned
> workflow, whose `name:` is exactly `pre-run pin check`, run as `python3 -I -S -B -c '<program>'` with
> the program given in the workflow text on its single `run:` line, so that it executes no file of the
> checkout. The workflow fetches `F` by its full id. The step refuses unless the environment value
> `GITHUB_REF` is `refs/heads/main` and `F` matches `^[0-9a-f]{40}$`. It reads the configuration blob at
> `F` with `git cat-file blob`, at the path the run passes to the tool as `--config`, and takes
> `tool.files`. It examines the entry point and the directory `tools/ledger_coverage/` on disk with
> `os.lstat`, never following a link: `tools` and every other parent directory of a checked path must be
> a real directory; every entry must be a regular file or a directory; the set of regular-file paths must
> equal the paths of `tool.files` exactly; and each file's sha256 must equal its pin. Any failure, a
> missing `F` or configuration, or an unreadable `tool.files` fails the step, and the job ends before any
> tool code runs. A workflow blob with no such step, more than one, or a `run:` value that is not one
> such line is refused by the review and fails the controls, whose runner extracts the program by this
> rule.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-151. Controls: EI8, EI9, EI10, EI11, EI12, EI13, EI15.

- Purpose: Specifies the pre-run pin check that runs before any file of the checkout.
- If confirmed: The job ends before any tool code runs if a tool file is missing, extra or differs from its pin.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): An unverified file could execute before the tool's own checks.
- Safeguards affected: Preserves the v5.5.9 pre-run check restored in v6.0c.
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.REC.20

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.20** **The import path.** The workflow invokes `python3 -I -B tools/ledger_coverage.py`. The
> entry point does not insert any directory of the checkout into `sys.path`; it loads the package
> `tools/ledger_coverage/` by its location. Before any import of a module not already loaded at
> interpreter start (only `sys` and `os` precede it), the entry point refuses unless the interpreter runs
> in isolated mode and no `sys.path` entry lies inside the checkout. The refusal is ERROR, exit 65, with
> the stop class `NOT_ISOLATED`, written to stderr as one JSON object with that class and the reason (RE-14). Because it fires
> before any import, it writes no `result.json`; it is, with USAGE, one of the two documented cases that
> write no `result.json`. The implementation exits 65 with a message and no class today; that is a
> verification defect, corrected in the tool revision.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-152. Controls: EI6.

- Purpose: Requires an isolated interpreter with no `sys.path` entry inside the checkout before any import.
- If confirmed: A shadow module (for example hashlib.py) cannot execute; the refusal is ERROR `NOT_ISOLATED`.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Import isolation is unspecified.
- Safeguards affected: Stricter than v5.5.9 (control EI6). Records a known implementation defect (exit 65 with no class).
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.REC.21

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.21** **The workflow's executable dependencies.** The pinned workflow executes only the
> pre-run check, the entry point, fixed `git` commands and the actions it names by commit id. The tool
> and the consumer check the workflow blob at `T` by a line rule on its raw text, with no YAML parser.
> The blob is refused if any line:
> - contains `uses`, in any letter case, and does not match
>   `^\s*(- )?uses: <owner>/<repo>[/<path>]<AT><40 lowercase hex>\s*$`, where `<AT>` denotes the
>   at-sign character (U+0040), written here by name, and with literal `<owner>` and `<repo>` names;
> - begins, after its indentation and any number of `-` or `---` markers each followed by whitespace
>   (the prefix `^\s*((-|---)\s+)*`), with `"`, `'`, `{`, `[`, `?`, `&`, `*` or `!`;
> - contains a colon followed by any whitespace and then `{`, `[`, `&`, `*` or `!` (the pattern
>   `:\s+[{[&*!]`).
>
> The rule only refuses; a form it refuses that YAML would read harmlessly is written another way in the
> pinned workflow.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-153. Controls: EI7, EI7-tool.

- Purpose: Refuses unpinned workflow dependencies by a raw-text line rule.
- If confirmed: Workflows with unpinned `uses` or the listed YAML forms are refused.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Workflow dependencies are unchecked.
- Safeguards affected: Stricter than v5.5.9.
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.REC.22

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `v6.0e line 54`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.22** **Workflow content review.** The rest of the workflow's content is checked against this
> list when the configuration's review covers `tool.workflow`, and the pin then fixes it: its triggers and
> inputs (the run receives `F` and the configuration path as inputs, and a run without them fails the
> pre-run check); `permissions` read-only except artifact upload; a GitHub-hosted `runs-on`, with no
> `container:` and no `services:`; no `env`, `GITHUB_ENV` or `GITHUB_PATH` change of `PATH`, `LD_*`,
> `GIT_*` or `PYTHON*`; no `shell:` override; the named actions only (no `setup-*` action, and no
> composite or docker action that installs or downloads executables or refers to other actions by tag);
> the exact run lines (the fetch of `F`, the pre-run check, and the entry point's command); the inputs
> reach the shell only through `env:`, and the fetch of `F` is `git fetch --no-tags -- origin "$F"`, with
> no `run:` line interpolating `${{ inputs.* }}`; no `continue-on-error`, and no `if:` on the steps after
> the pre-run check; no reusable workflow.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-154. Controls: TR15, TR50, EI7.

- Purpose: Lists the workflow content the review checks before the pin fixes it.
- If confirmed: Triggers, permissions, runners, environment, actions and run lines are reviewed against a fixed list.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The workflow review has no fixed list.
- Safeguards affected: Preserved.
- Note (R1): The content is in DESIGN-v6.0e.md, which the owner adopted in the owner's words (#1169 comment 7130449822, class (i)); confirming it re-confirms a settled decision (R1).

### R6.REC.24

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.REC.24** **The admission object.** `result.json` records `config.admission`, an object with a
> `mode` field: `"chain"`, `"control-harness"` or `"replay"`. Its mode is `"chain"` only when
> configuration admission and execution identity held, and only then does it carry `snapshot`:
> - the run record fields read: run id, repository id, head repository id, event, workflow path and
>   `head_sha` (`T`); the workflow file's blob sha256 at `T`; the tool blob hashes at `T`;
> - the evaluated commits `E`, `H`, `X`, `C`, `L` and `M`;
> - `F`, the pin table's `{path, blob_sha256}`, and the configuration's and its review record's
>   `{path, blob_sha256}`;
> - the delegated evidence, for every delegated and native class of sec. 13, at `X` and, where `C`
>   differs, at `C`: the host records the tool read for the class, as the host returned them, in
>   canonical JSON; the sha256 of every artifact and result file the class used; the outputs of every
>   checker the tool ran natively (for each run, the checker blob sha256, the exact command line, the
>   working directory, the exit status, and the complete bytes of each result file it wrote and of each
>   output the class compares); and the class's own recorded re-derivations;
> - the sha256 of the canonical JSON of the snapshot itself.
>
> Only `"chain"` is acceptable (sec. 7). The control harness (sec. 17) may admit a draft configuration
> without its chain; its results carry `mode: "control-harness"` (with any simulated snapshot the control
> supplies, never mode `"chain"`), are written as `control-result.json` with `"harness": true`, and are
> never written as an acceptable result. The offline replay writes `mode: "replay"`; that mode is deferred with R6.OUT.15 (owner decision 1,
> sec. 0.1).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-158, E-159, E-145. Controls: TR5, TR5-sim, X11, TR45-opB, TR46.

- Purpose: Defines the admission object and its three modes; only `"chain"` is acceptable.
- If confirmed: Harness and replay results can never be written as acceptable results.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The admission modes are unspecified.
- Safeguards affected: Preserved.

### R6.DENY.5

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D2`, class (iii) no GitHub record; `V5-D2`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.DENY.5** **Outstanding rule content.** The content of the plan's rule records is transferred to
> the plan amendment as outstanding obligations, each a named blocker on the execution it gates (sec.
> 32): the deny rules DR-1, DR-3, DR-4 and DR-5 with their definitions and patterns (the identifiers
> DR-1d and DR-2 are retired, sec. 33, and never reused); the W1 allow rules, including W1-c's
> fingerprints and its `negative_allowance`; the W2 allow rules, replacing P's corresponding
> `RESIDUAL_ALLOW` and `EXPLAINED` entries and its blanket `(A1)` strip; and the `resid` pattern with its
> parts resid-a, resid-b and resid-c.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1001, E-1002, E-1003, E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025,
> E-1026, E-1027, E-1032. Controls: none (OBL-3).

- Purpose: Transfers the rule content to the plan amendment as outstanding obligations (named blockers).
- If confirmed: The plan cannot reach the gated steps until the deny rules, the W1 and W2 allow rules and `resid` exist as reviewed records.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The rule content would have no stated obligation.
- Safeguards affected: Adds a blocker; leaving out resid-b and resid-c (V5-D2) would weaken REVIEW coverage (V26); W1-c's allowance is the bounded exception of S1-D1; the W2 allow rules rest on no owner decision.
- Flag, earlier designs: W1-c's `negative_allowance` as for R6.RULE.2.
- Decision 2: class (b).

### R6.DENY.6

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.DENY.6** **Accepted residual: V4 and V27 (confirmed by owner decision 3 of 2026-11-25,
> sec. 0.1).** The question: with the deny rules DR-1, DR-3, DR-4 and DR-5 and the review profiles of the
> A1 configuration, the added text of control V4 ("the framework's sixth structural property, finiteness
> of the bijection") and of control V27 ("The framework's sixth structural property is finiteness of the
> substratum", added alone and as the edited glossary line) produce no hit of any review or deny profile.
> The expectation for both would then be PASS with zero hits, recorded as an accepted residual after the
> candidate rule DR-2, which caught V4, was not adopted. That decision (V5-D1) is recorded only in
> paraphrase, in the session-written #1169 comment 7099655517; owner decision 3 accepts the reversal in
> the owner's words. Consequences of confirming: an added sentence that asserts finiteness as an ordinal
> structural property of the bijection or substratum, in the forms of V4 and V27, passes the tool
> undetected; the original item 7 check also misses it; its detection rests on review outside the tool;
> V4 and V27 are kept as controls so that a change in their outcome is visible. Consequence of
> restoring: V4 (and V27) expect FAIL `deny-match`, which requires a plan rule record that catches them
> (a rule of the DR-2 form under a new identifier, since DR-2 is retired and never reused (sec. 33);
> plan content under R6.DENY.1, reviewed with the deny set), and the
> reconciliation of that rule against the negative examples. The owner decides at adoption among (a)
> confirming the PASS expectation knowingly, (b1) restoring the FAIL expectation of V4, V27 and
> V27-glossary, with V15 REVIEW_REQUIRED, and (b2) restoring it for V15 as well, which needs a second
> new rule, of the DR-1d form, since a rule of the DR-2 form does not match V15's text (R6.PUR.9). Owner decision 3
> chose (a), confirming the PASS expectation knowingly. The decision covers V4, V27, V27-glossary and V15
> together (RE-1): each of the four rows carries the expectation of the candidate "reversal adopted" as
> its `expect` (R6.PUR.9).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1001, V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: States the accepted-residual question for V4 and V27 and its consequences, for decision at adoption.
- If confirmed: As for R6.PUR.9.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- Flag, earlier designs: As for R6.PUR.9.
- Decision 2: class (d).

### R6.CTRL.7

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.7** A control-only input is a pinned object (commit, path, git blob id and sha256) named by
> one control in the controls file. It is read only by the control that names it, changes no profile's
> scope and no production result, and adding or changing one changes the controls file and is reviewed
> with it. No historical text is constructed for this purpose. DR-3's witness is such an input: the
> sentence of `AGENTS.md` at `H`, lines 37-39 (blob 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256
> d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27), which RT-DR3W scans at `H` and,
> as its countercontrol, in `X_rep` (R6.EVID.8), whose `AGENTS.md` is `H`'s with the ledger's splices
> applied.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1011, E-1013, E-1014, E-1015, OC-3. Controls: RT-DR3W.

- Purpose: Defines control-only inputs and fixes DR-3's witness as the sentence of AGENTS.md at `H`, lines 37-39.
- If confirmed: DR-3 is tested on a real sentence; the production scan is not widened; no historical text is constructed as a witness.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): DR-3 would have no real witness.
- Safeguards affected: Preserves v6.0e; rests on V5-D1's second limb.

### R6.CTRL.14

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.14** The rule controls are L1-L4, V1-V27 (V7a, V7b, V7c; no V8), A1r-A12r, S1r, S2r,
> WB1-WB15, N-W, their engine analogues and the rule-lint controls. v2's class `rule-invalid` is
> `record-invalid` (exit 20) throughout. V2 FAILs by DR-3 and V3 by DR-4; v2's fingerprint-mismatch and
> residual-test basis for them is superseded, since no rule deletes text and overlap is strict (sec.
> 10). V1 FAILs by DR-1, alternative b. The deny rules and the seed allow rules are plan records adopted
> with the amended plan; the controls use the current rule files as pinned control inputs and test the
> rule mechanism (sec. 12).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1106, E-1107, E-1108, E-1109, E-1110, E-1111, E-1112, E-1113, E-1114, E-1115, E-1116, E-1117, E-1118, E-1119, E-1120, E-1121, E-1122, E-1123, E-1124, E-1125, E-1126, E-1127, E-1128, E-1129, E-1130, E-1131, E-1132, E-1133, E-1135, E-1136, E-1137, E-1138, E-1139, E-1140, E-1141, E-1142, E-1143, E-1144, E-1145, E-1146, E-1147, E-1148, E-1149, E-1150, E-1151, E-1192, E-1193, E-1194, E-1195, E-1196, E-1197, E-1198, E-1199, E-1200, E-1201, E-1202, E-1203, E-1204, E-1205, E-1206, E-1232, V2-074, V2-075, V2-076, V2-077, V2-078, V2-079, V2-081, V2-082, V2-083, V2-084, V2-085, V2-086, V2-087, V2-088, V2-089, RV-050, RV-052. Controls: A1r, A2r, A3r, A4r, A5r, A5r-generic, A6r, A7r, A8r, A9r, A10r, A11r, A12r, E-A1r, E-A2r, E-A3r, E-A6r, E-A8r, E-L1, E-L3, E-S1r, E-S2r, L1, L2, L3, L4, S1r, S2r, V1, V2, V3, V3-countercontrol, V4, V5, V6, V7a, V7b, V7c, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V27-glossary, WB1, WB2, WB3, WB4, WB5, WB6, WB7, WB8, WB9, WB10, WB11, WB12, WB13, WB14, WB15, lint-ok, rule-negative.

- Purpose: Fixes the rule controls (L, V, A, S, WB, N-W and lint) and the basis of V1-V3.
- If confirmed: The control set is fixed; the V4-group rows follow the separate decision.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The rule controls are unlisted.
- Safeguards affected: Preserves v6.0e's controls.

### R6.CTRL.15

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.15** V4 adds "the framework's sixth structural property, finiteness of the bijection" to
> the file of a W1 rule. Under the deny set without DR-2 the sentence produces no hit, so the run is
> PASS: this is the V4 reversal. What it permits: a reintroduction of the counted premise in the form
> "sixth structural property, finiteness of ..." passes the deny profiles and the residual profile
> unclassified by any FAIL, and the original item 7 misses it as well. Its consequence: the tool does
> not detect that form, and detection rests on review of the residual hits. The reversal rests on an
> owner decision recorded only in paraphrase (V5-D1, in the session-written #1169 comment 7099655517). Owner decision 3 of 2026-11-25 (sec. 0.1) accepts it (resolution (a) of
> R6.PUR.9), with effect from r6's adoption: V4, V27 and V27-glossary expect PASS and V15
> REVIEW_REQUIRED through `resid` (RE-1). The resolutions not chosen were these: had the reversal been
> rejected, V4's expectation would be FAIL `deny-match` and the deny set would need a rule matching that form, under a new identifier (DR-2 is retired and never reused, sec. 33),
> which is a plan-record change (sec. 12). V27 tests a sentence of the
> same form and rests on the same decision, as do V27-glossary and V15, whose candidates were
> REVIEW_REQUIRED `unclassified` and FAIL `deny-match`; V15's FAIL candidate would have needed, in addition, a rule
> of the DR-1d form under a second new identifier, since a rule of the DR-2 form does not match V15's
> text (R6.PUR.9, resolutions (b1) and (b2)).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

- Purpose: Describes the V4 reversal: what it permits and its consequence.
- If confirmed: As for R6.PUR.9.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- Flag, earlier designs: As for R6.PUR.9.
- Decision 2: class (d).

### R6.CTRL.17

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.17** Split and dependent rows. RT-O9's own checks (the expected set of record-directory
> entries computed independently from the stand-in `F` tree, compared exactly; no unequal path; no
> `side-change-unclassified`) run and are gated whenever RT-O9 runs, independently of RT-L2. Its clause
> that RT-L2 still holds is the separate row RT-O9-L2, which depends on RT-L2 and is NOT RUN with
> RT-L2's release condition. TR45's op-C half is the row TR45-opC, NOT RUN until delegated evidence is
> recorded by native runs at `X` and `C`. EI14's branch-dispatch half is the row EI14-dispatch, NOT RUN
> until a dispatch of the pinned workflow on a branch holding `T'` is made, after the tool lands, under
> a launch the owner approves; EI14's other cases stay in EI14. The consumer halves of EI7, TR15, TR50,
> TR51 and TR52 are rows of their own (EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer,
> TR52-consumer), implemented in the tool revision; until then the gate reports them missing.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1218. Controls: RT-O9, RT-O9-L2, TR45-opB, TR45-opC, EI14, EI14-dispatch, EI7,
> EI7-consumer, TR15-consumer, TR50-consumer, TR51-consumer, TR52-consumer.

- Purpose: Splits dependent rows: RT-O9's own checks run independently of RT-L2; TR45-opC and EI14-dispatch are NOT RUN until their evidence exists; consumer halves are rows.
- If confirmed: No actual failure is hidden behind a dependent NOT RUN.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Dependent clauses would be merged with independent checks.
- Safeguards affected: Preserved (Q6, Q14).

### R6.CTRL.19

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.19** The real-tree controls run in CI on real objects: RT-A, RT-E, RT-H0, RT-T0, RT-T, RT-C,
> RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-I7, RT-I7A, SW1, SW2, item11-T1p, N-W, RT-M, RT-SHIFT, RT-X, RT-L,
> RT-L2, RT-O9 and RT-O9-L2. v1's `verify-record` is `record` and `check-coverage` is `coverage`. Every
> figure a runner asserts today that is reproducible from inputs on `main` (among them RT-H0's 113/7/7,
> RT-A's and RT-E's 697, the RT-DR counts at `H`, RT-T0's site and region counts, RT-I7's split at `H`,
> RT-I7A and RT-C, and RT-D's 45 `resid` lines) is an asserted count in the expectation file, not an
> informational figure. A control whose verdict reads only what `H` and the ledger determine runs on
> `X_rep` (R6.EVID.8); a figure that needs T1' itself is candidate evidence only, not acceptance support
> (OBL-23); its standing as evidence follows sec. 31. RT-C is PASS only with contract
> evidence; without it the expected result is the one the expectation file states for missing
> evidence. RT-T is NOT RUN until every reviewed record of sec. 14 exists. The two `not determined`
> H..T1' cases of sec. 6 are RET FAILs, and RT-T's expectation says so; it does not claim that no RET
> FAIL exists.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1134, E-1176, E-1177, E-1178, E-1179, E-1180, E-1181, E-1182, E-1183, E-1184, E-1185, E-1186, E-1187, E-1188, V1-115, V1-117, V1-119, V2-099, V2-100, V2-101, V2-103, V2-104, V2-105, V2-162, V2-163, V2-164, RV-028, RV-051, E-091, E-1010, V1-132, V1-136, OC-3. Controls: N-W, RT-A, RT-C, RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-E, RT-H0, RT-I7, RT-I7A, RT-L, RT-L2, RT-O9, RT-O9-L2, RT-T, RT-T0, RT-X, SW1, SW2, item11-T1p.

- Purpose: Lists the real-tree controls and makes reproducible figures asserted counts.
- If confirmed: Figures become asserted counts; the `T1'`-bound figure of item11-T1p is candidate evidence only (OBL-23, owner decision 4).
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Figures would be informational.
- Safeguards affected: Stricter.

### R6.CTRL.22

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `DI-2`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.CTRL.22** The record controls are O1-O9 (O4 retired), N1, S4a, LN1-LN8 and LN10 (LN9 retired),
> and the record-lint controls R3-F2, R4-B3, R4-B3-DUP, R5-N6 and R6-G6. O1, O2, O3, O5 and O7 assert
> an emitted FAIL `record-invalid`, not only a lint problem; O6 asserts the emitted outcome, not only the
> absence of an ERROR.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1154, E-1155, E-1156, E-1157, E-1158, E-1159, E-1160, E-1161, E-1331, E-1332, E-1333, E-1334, E-1335, E-1336, E-1337, E-1338, E-1339, E-1340. Controls: LN1, LN2, LN3, LN4, LN5, LN6, LN7, LN8, LN10, O1, O2, O3, O5, O6, O7, O8, O9, R3-F2, R4-B3, R4-B3-DUP, R5-N6, R6-G6, S4a.

- Purpose: Lists the record controls and requires emitted FAIL `record-invalid`, not only a lint problem.
- If confirmed: Record controls assert the emitted outcome.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The record controls are unlisted.
- Safeguards affected: Stricter.

### R6.CTRL.23

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.23** The delegation controls are G1-G9 and G-A1; the output controls are X1-X11,
> S7-schema-and-checker, ACCEPT-SCHEMA and B4-MEANING; the admission, execution-identity and
> object-integrity controls are TR1-TR3, TR5, TR5-sim, TR13-TR15, TR14-tool, TR28-tool, TR28-consumer,
> TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50-TR52 and their consumer halves, EI1-EI15
> with EI2-consumer, EI7-tool, EI7-consumer and EI14-dispatch, GV1-GV7 with GV6-disk, GV7-tool and
> GV7-consumer, the cache controls GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE and GV-CACHE-KEY,
> CHAIN-REFUSAL, ADM-CONFIG-AT-F, CONFIG-LINT, O3-FILTER and K1-GRAPH. v1's RT-A' (op A with `--pin H`)
> is X1. GV4 includes the HP-merge case; EI6 includes its third case and the `json.py` and
> `importlib.py` shadow files; EI5 and EI7 include their countercontrols. TR1 applies to chain
> admission only.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1162, E-1163, E-1164, E-1224, E-1225, E-1226, E-1227, E-1228, E-1229, E-1165, E-1166, E-1167, E-1168, E-1169, E-1170, E-1171, E-1172, E-1173, E-1174, E-1207, V2-096, V2-097, E-1208, E-1209, E-1210, E-1211, E-1212, E-1213, E-1214, E-1215, E-1216, E-1217, E-1219, E-1220, E-1221, E-1222, E-1223, E-1246, E-1247, E-1248, E-1249, E-1250, E-1251, E-1252, E-1253, E-1254, E-1255, E-1256, E-1257, E-1258, E-1259, E-1260, E-1261, E-1262, E-1263, E-1264, E-1265, E-1266, E-1267, V1-116. Controls: G1, G2, G3, G4, G5, G6, G7, G8, G9, G-A1, ACCEPT-SCHEMA, B4-MEANING, S7-schema-and-checker, X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, X11,
> ADM-CONFIG-AT-F, CHAIN-REFUSAL, CONFIG-LINT, EI1, EI2, EI2-consumer, EI3, EI4, EI5, EI6, EI7, EI7-consumer, EI7-tool, EI8, EI9, EI10, EI11, EI12, EI13, EI14, EI14-dispatch, EI15, GV1, GV2, GV3, GV4, GV5, GV6, GV6-disk, GV7, GV7-consumer, GV7-tool, GV-CACHE, GV-CACHE-AFTER-READ, GV-CACHE-IMMUTABLE, GV-CACHE-KEY, K1-GRAPH, O3-FILTER, TR1, TR2, TR3, TR5, TR5-sim, TR13, TR14, TR14-tool, TR15, TR15-consumer, TR28-consumer, TR28-tool, TR29, TR29-tool, TR30, TR45-opB, TR45-opC, TR46, TR48, TR50, TR50-consumer, TR51, TR51-consumer, TR52, TR52-consumer.

- Purpose: Lists the delegation, output, admission, execution-identity and object-integrity controls.
- If confirmed: The control set is fixed.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): These controls are unlisted.
- Safeguards affected: Preserved.

### R6.CTRL.24

Status: confirmed by owner decision 1 (necessary for reliable verification).
Decision basis: `S1-D2`, class (iii) no GitHub record; `R-D labels`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.CTRL.24** The plan-mapping controls are S11-1 to S11-14 (S11-2 composed of S11-2a, S11-2b and
> S11-2c) and the per-edit controls S11-56, S11-57a-d, S11-58a-f and S11-58g-k. S11-56 tests the tool's
> side only: the equality of its result with the plan's own checker is an outstanding obligation (sec.
> 18). S11-7 is implemented in the tool revision; it plants a literal and a DR-5 match and requires both
> to FAIL.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for reliable verification.
> Sources: E-1234, E-1235, E-1236, E-1237, E-1238, E-1239, E-1240, E-1241, E-1242, E-1243, E-1244, E-125. Controls: S11-1, S11-2, S11-2a, S11-2b, S11-2c, S11-3, S11-4, S11-5, S11-6, S11-7, S11-8, S11-9, S11-10, S11-11, S11-12, S11-13, S11-14, S11-56, S11-57a, S11-57b, S11-57c, S11-57d, S11-58a-f, S11-58g, S11-58h, S11-58i, S11-58j, S11-58k.

- Purpose: Lists the plan-mapping and per-edit controls; S11-56 tests the tool's side only, and parity with P is an obligation.
- If confirmed: The control set is fixed; parity stays outstanding (OBL-1).
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): These controls are unlisted.
- Safeguards affected: Preserved.

### R6.PLAN.8

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `v3 D1-D4`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.PLAN.8** Item 7 (a corpus grep for `\bA1\b` and related terms with only ledger false positives,
> and zero posit counts "Fourteen", "six structural" and "sixth of") maps, as frozen, to `terms --commit
> X --profile item7-literal`. The literal check is kept as the named countercontrol `item7-literal`, with
> RT-I7. Item 7 as frozen does not pass at T1' or at `X_rep`: seven lines contain the legitimate count of
> the bijection's properties (W1); RT-I7 asserts the counts at `X_rep` (R6.EVID.8), and the measurement
> at T1' is historical. Countercontrol: the H-form
> "Fourteen items" reinstated, which must FAIL in both the literal check and DR-5 (S11-7). DR-5 is a plan
> record. RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at `X_rep` as a test of the
> mechanism.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1275, E-1283, OC-3. Controls: S11-7, RT-I7, RT-I7A.

- Purpose: Maps item 7 as frozen to the literal check, kept as the countercontrol `item7-literal`, with a restatement of item 7 as a plan amendment.
- If confirmed: Item 7 as frozen FAILs at T1' and at `X_rep`; passing needs a reviewed plan amendment.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Item 7 would have either no mapping or the literal grep as the acceptance criterion, which no tree keeping W1's legitimate sentences can pass.
- Safeguards affected: The literal check survives as a countercontrol; acceptance moves to a reviewed amendment.
- Flag, earlier designs: Permits the plan to pass, after a reviewed amendment, with item 7's literal grep failing; v3's alternative was that the literal grep must stand.
- Decision 2: class (b).

### R6.A1CFG.7

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **R6.A1CFG.7** Acceptance criterion S13: the configured engine reproduces, item by item, every A1
> control outcome of sec. 17 that the expectation file states, including the record-directory controls
> RDIR-1 to RDIR-25 and RDIR-12b, RT-O9 (with its dependent clause as in OBL-14) and the item-2 controls
> I2-1 to I2-8. Rule outcomes (deny, allow, `resid`) are measured with the plan's rule files as pinned
> control inputs; the rules themselves are plan records adopted at `F` (sec. 12, OBL-3). The expected
> outcomes of V4, V27, V27-glossary and V15 are those of owner decision 3 of 2026-11-25 (sec. 0.1;
> RE-1, OBL-6), and they count toward S13.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1436, MC-13, OD-8, RD-14. Controls: GATE-18,
> V5, V15, V27, V7a, V7b, V7c, V23, V24, V25, V26, RT-I7, RT-I7A, RT-DR, RT-DR3W.

- Purpose: States acceptance criterion S13 for the configured engine.
- If confirmed: S13 counts every stated A1 control outcome, including the four V4-group rows with the expectations of owner decision 3.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): S13 is unstated.
- Safeguards affected: S13 was temporarily narrower than v6.0e's, which counted V4, V27 and V15, while those rows were deferred; under owner decision 3 it counts them again.
- Flag (R6): R6.A1CFG.7 narrows a check: S13 was temporarily narrower than v6.0e's while V4, V27 and V15 were deferred. The review's class: (c), protection provided by R6.GATE.9 (`deferred-expectation` is a gate failure) and OBL-6 (an adoption blocker until the decision). Under owner decision 3 the four rows carry their expectations and count toward S13, so the narrowing ends with r6's adoption.

### R6.EVID.4

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.EVID.4** Acceptance references. The following figures are acceptance references, each through
> the control named, on the condition of R6.EVID.1. Figures whose control runs on `X_rep` are acceptance
> references through runs whose inputs are all reachable from `main` (R6.EVID.8). The figure whose
> control needs `T1'` itself (item11-T1p) is listed for identification only: it is candidate evidence,
> not acceptance support (owner decision 4 of 2026-11-25, sec. 0.1; OBL-23).
>
> | Figure | Control | Input |
> |---|---|---|
> | 697 sites; replay errors 0 | RT-A, RT-E | `E`, record commit |
> | 113 `E..H` site changes (`hp-unadjudicated`); 7 HP `context-meaning-unverified`; 7 HP `context-structure-changed` | RT-H0, RT-T0 | `H` |
> | 9 merger groups covering 22 sites | RT-T0 | `H`, `X_rep` |
> | 19 region-attributed sites with untracked HP overlap (18 line-attributed); `papers/Substratum.md:266` with splice D029 | RT-T0 | `X_rep` |
> | 383 unchanged, 197 replaced, 4 removed sites; 215 region lines; 168 sites moved by `H..X_rep` splices | RT-T0 | `X_rep` |
> | 5 RET `context-meaning-unverified`; 3 RET `context-structure-changed` | RT-T0 | `X_rep` |
> | `resid`: 45 REVIEW lines, 17 hit by no other profile; 11 W1/W2 lines PASS | RT-D | `X_rep` |
> | literal item-7 greps at `X_rep`: "six structural" 7, "Fourteen" 0, "sixth of" 0, `\bA1\b` 4 | RT-I7 | `X_rep` |
> | literal item-7 greps at `H`: 11, 1, 2, 179 | RT-I7 (after RD-3) | `H` |
> | deny lines at `H`: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct; at `E` 95 distinct | RT-DR (after RD-3) | `H`, `E` |
> | DR-3 on `AGENTS.md`: one sentence at `H` (lines 37-39), none in `X_rep` | RT-DR3W | control inputs |
> | 95 retired lines, each FAIL `final-unclassified` at `H`; at `H` 86 deny, 123 `final-unclassified`, 209 FAIL lines (93 and 216 with multi-line counting); at `X_rep` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `X_rep` |
> | 176 `final-unclassified` lines of the `repo` profile | item11-T1p | `T1'` |
> | 584 sites swept, each with exactly one new RET FAIL | SW2 | `H` |
> | 697 sites swept, each with exactly one new FAIL | SW1 | `E` |
> | 399 splices verified at `H`; 23 corpus files and 21 other ledgered files conform | RT-C (after RD-3) | `H` |
>
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-037, E-038, E-074, E-039, E-042, E-045, E-046, E-047, E-049, E-089, E-090, ME-3, RD-3,
> RD-23, MC-1, MC-2, VD-10, RD-11, OC-3. Controls: RT-A, RT-E, RT-H0, RT-T0, RT-D, RT-I7, RT-DR, RT-DR3W,
> RT-I7A, item11-T1p, SW1, SW2, RT-C.

- Purpose: Lists the acceptance references and the controls that establish them.
- If confirmed: The listed figures are gated through their controls.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): No figure is an acceptance reference.
- Safeguards affected: Stricter.

### R6.EVID.5

Status: scope statement without a check of its own (owner decision 1).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **R6.EVID.5** Historical measurements. The following figures are not acceptance references. No
> control on `main` reproduces them, or they were measured with P's code, at `T1'` by scripts that are not
> retained, or under definitions r6 does not use. They are provenance (sec. A.42 item 2) and are kept in
> the appendix:
> - the s3 categories 346 / 136 / 109 / 106 and the per-merge attribution 48 / 23 / 15 / 15 / 12, and
>   the three two-step HP sites (`papers/Main.md:224`, `papers/Main.md:732`,
>   `papers/Substratum.md:92`);
> - "31 distinct splices" over the `H..T1'` HP overlaps;
> - v4's 203 region lines and its explanation;
> - v4's `resid` figures 287 / 28 / 13 and the four lines added by the v5 widening;
> - P's `classify()` breakdown of the 176 `repo` lines (96 / 31 / 14 / 35), 5486 lines in historical
>   records and 2 in generated artifacts;
> - the 12 meaning-context total, the "per unit" alternative 8, the 52 context changes and their split
>   27 / 22 / 3, and the S0 indicator counts;
> - the per-sentence deny counts under the unversioned "v5 splitter";
> - 84 and 86 hit lines, 200 / 116 / 93 / 16 / 7 unheld lines, 226 distinct lines needing a record, the
>   `ptr` 5 lines at `T1'`, the 4677-blob history search, and the reference rates of the indicator
>   definitions;
> - the parity figures 2822 / 2822, 16905 / 16905, 273, 4000 cases and 401 / 399 (OBL-2);
> - every figure of v6.0e sec. 14 not listed in R6.EVID.4.
>
> Scope statement by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1); it has no check of its own. GATE-16, named below, is the gate's reference-difference control of R6.GATE.9; it checks only that a figure kept as `reference` never changes a verdict.
> Sources: E-037, E-038, E-039, E-042, E-045, E-046, E-047, E-089, E-040, E-041, E-043, E-044, E-048,
> E-088, E-1356, E-1357, E-1358, E-1359, E-1360, E-1361, E-1362, ME-2, ME-3. Controls: GATE-16.

- Purpose: Lists the historical measurements that are not acceptance references.
- If confirmed: These figures stop supporting acceptance and are provenance.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Their standing is undefined.
- Safeguards affected: No protection is lost (under AGENTS.md sec. A.42 they could not support an enduring claim); the 4677-blob history search, which supported dropping DR-1d and DR-2, becomes provenance.

### OBL-1

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-1** P-parity of `register` and `infinity`. The engine's `register` and `infinity` profiles
> implement items 5 and 6 of P's plan as P's frozen checker defines them: per edit and per step of the
> edit list, not per splice, with P's selection, counting and sentence splitting (P's `edits_check.py`,
> blob sha256 2856e58c...d98c, functions `static_new`, `inf_key` and `sentences`). Gates: plan freeze `F`
> and any trial that claims items 5 or 6. Discharged by: a comparison, recorded at `F` by a script
> retained on `main`, of the engine's outputs against P's checker as frozen with the plan. Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement. Sources:
> E-115, E-1371, ME-1.

- Purpose: Requires P-parity of `register` and `infinity` with P's frozen checker, recorded at `F`.
- If confirmed: The plan freeze and any trial claiming items 5 or 6 are blocked until the comparison is recorded.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): Parity would be unrequired.
- Safeguards affected: Adds a blocker.

### OBL-3

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words; `S1-D2`, class (iii) no GitHub record; `V5-D2`, class (ii) session-written record on GitHub, no owner words; `S1-D1 to S1-D3`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-3** Rule records adopted at `F`. The deny rules DR-1 (alternatives a, b, c), DR-3, DR-4 and
> DR-5; the review profile `resid` (resid-a, resid-b, resid-c); the W1 allow rules with W1-c's
> `negative_allowance: {"finit": 1}`; the W2 allow rules replacing the first two `RESIDUAL_ALLOW`
> entries, their `EXPLAINED` substring entries and the blanket `(A1)` strip; and the converted
> `EXPLAINED` entries are plan records. Each is independently reviewed and adopted with the amended
> plan at `F`. Until then the controls use the current rule files as pinned control inputs. Gates: plan
> freeze `F`. Discharged by: the reviewed rule records frozen at `F`. Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement. Sources: E-1001, E-1002, E-1003,
> E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025, E-1026, E-1027, OD-8.

- Purpose: Makes the rule records obligations adopted at `F`.
- If confirmed: As for R6.DENY.5.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): As for R6.DENY.5.
- Safeguards affected: As for R6.DENY.5.
- Flag, earlier designs: As for R6.DENY.5.
- Decision 2: class (b).

### OBL-6

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `V5-D1`, class (ii) session-written record on GitHub, no owner words.

Current wording (DESIGN-r6.md):

> **OBL-6** Accepted residuals and the V4 reversal. With DR-1d and DR-2 dropped, "the framework's sixth
> structural property, finiteness of the bijection" PASSes when added (control V4, whose expectation in
> v2's demonstration was FAIL); "the substratum's sixth axiom, finiteness" is REVIEW only (V15); "The
> framework's sixth structural property is finiteness of the substratum" PASSes (V27). Constructed forms
> outside `resid`'s classes PASS ("the six posits of the substratum", "six assumptions about the
> substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger", and "$A_1$" joined to "$A_6$" by an en dash).
> Consequence of the reversal: an added sentence of V4's form reaches PASS without review. Gates: r6's
> adoption (the V4 reversal, adopted or rejected at that step); plan freeze `F` (acceptance of the residual
> forms or further rules, as rule records). Discharged by: owner decision 3 of 2026-11-25 (sec. 0.1),
> which chose resolution (a) of R6.PUR.9 and takes effect with r6's adoption, and the reviewed rule
> records at `F`; r6 expects the outcomes of resolution (a), and no rule of the DR-1d or DR-2 form is
> required (rule content is plan content, R6.DENY.1; N5).
> The decision covers V4, V27, V27-glossary and V15 together (RE-1).
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1365, E-1366, RD-14, Q10.

- Purpose: Records the accepted residuals and the V4 reversal as an obligation discharged at r6 adoption and at `F`.
- If confirmed: As for R6.PUR.9.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): As for R6.PUR.9.
- Safeguards affected: As for R6.PUR.9.
- Flag, earlier designs: As for R6.PUR.9.
- Decision 2: class (d).

### OBL-15

Status: confirmed by owner decision 1 (necessary for scientifically valid retirement).
Decision basis: `S1-D2`, class (iii) no GitHub record.

Current wording (DESIGN-r6.md):

> **OBL-15** Reviewed records for RT-T. RT-T is NOT RUN until every reviewed record of sec. 14's review
> load exists at `F` and verifies: HP adjudications for the 113 `E..H` site changes, context
> adjudications for the meaning-context sites, structure reviews, and hit classification records for the
> replacement-region and unheld hit lines (including `papers/GR.md:58`). RT-T runs at `X_rep` built from
> `F`'s ledger (R6.EVID.8): op B reads only the corpus and the segments `E..H` and `H..X` (R6.PUR.5),
> whose bytes `H` and `F`'s ledger fix for every conforming candidate. Gates: plan freeze `F`; the A1
> retirement execution. Discharged by: RT-T run and PASS with every record: before the designation of
> `F`, on the candidate `F` within its exact-candidate validation (kind 1, OBL-16 (a)); in the
> retirement execution, at the executed candidate (kind 4); both qualify as kind 2 once the round's
> landing is on `main`.
> Confirmed by owner decision 1 of 2026-11-25 (#1169 comment 7166844576; sec. 0.1) as necessary for scientifically valid retirement.
> Sources: E-1062, E-1063,
> RD-9, OD-20, OC-3.

- Purpose: Keeps RT-T NOT RUN until every reviewed record of the review load exists at `F`.
- If confirmed: Freezing at `F` and execution are blocked until every record exists.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): RT-T would have no release condition.
- Safeguards affected: Stricter.

### R6.DENY.1

Status: not marked; takes effect only by r6's adoption.
Decision basis: none cited (unmarked by F4); authorized only by r6's adoption.

Current wording (DESIGN-r6.md):

> **R6.DENY.1** **Rule records are plan records.** The deny rules, the allow rules for the plan's own
> cases, and the review-profile rule `resid` that a configuration uses are rule records of the plan, in
> the schemas of sec. 10. They are frozen and adopted with the amended plan at `F`, after independent
> review, and referenced by the configuration at `F`. The tool's requirement is the rule mechanism:
> sec. 9 (profiles), sec. 10 (schema, application, lint), sec. 11 (records) and sec. 14 (hit
> classification). r6 states no rule content.
> Sources: E-1001, V2-059, V2-060, V2-061, RV-049. Controls: RT-DR, RT-D, RT-D-gr58, L1, L2.

- Purpose: Makes the rule records (deny, plan allow, `resid`) plan records frozen at `F`; the tool's requirement is the rule mechanism.
- If confirmed: The tool runs whatever reviewed rule content is frozen at `F`; r6 states no rule content.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The place of rule content would be undecided.
- Safeguards affected: Preserved: v6.0e left the rules "for independent review ... not adopted"; verification of rule content moves from the design to the review at `F`.

### R6.DENY.2

Status: not marked; takes effect only by r6's adoption.
Decision basis: none cited (unmarked by F4); authorized only by r6's adoption.

Current wording (DESIGN-r6.md):

> **R6.DENY.2** **Controls on pinned rule inputs.** The controls of the rule mechanism use the rule
> files current at the commit under check as pinned control inputs, named with their blobs in the
> expectation file (sec. 16). Acceptance of the mechanism (sec. 18) is its behaviour on those inputs. A
> changed rule file is a changed control input: the affected expectations are re-established in the
> expectation file before the gate can hold.
> Sources: E-1001. Controls: V1, V2, V3, V5, V6, V9, V10, V11, V12, V13, V14, V16, V17, V18, V19, V20,
> V22, N-W, RT-DR3W.

- Purpose: Runs the rule-mechanism controls on the rule files current at the commit under check, as pinned control inputs.
- If confirmed: A changed rule file forces the affected expectations to be re-established before the gate can hold.
- If not confirmed: the requirement stays pending, and r6 cannot be adopted while it is pending (R3).
- If withdrawn, only by an explicit owner choice with its verification traced (R6.STAT.5): The controls' rule inputs are unpinned.
- Safeguards affected: Preserved.
