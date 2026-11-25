# r6: requirements resting on paraphrased or unrecorded owner decisions

This list does not reconstruct any authorization. Each entry names an owner decision that r6's sources record only in paraphrase, or without a record the owner made, the r6 requirements that rest on it (found by the rule stated in the entry), what the paraphrase says, and the three options. Each listed requirement is marked in DESIGN-r6.md with "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." and carries the decision key in the field `pending_owner_confirmation` of REQUIREMENTS.json.

Options for every entry:

- (a) confirm in the owner's own words: the owner records the decision in a comment, which r6 quotes byte-exact with author and time (AGENTS.md sec. A.42 item 7);
- (b) fresh authorization: the owner decides the question anew, in a recorded decision, and r6 cites that record;
- (c) withdraw the requirement: the requirement, or the part of it that rests on the decision, is removed or narrowed, with its verification traced (R6.STAT.5).

***

## Owner decision V5-D1 (DR-2 and DR-1d dropped from the deny set; the V4 group)

- Key: `V5-D1`
- Where recorded: v6.0e, recorded only in paraphrase (#1169 comment 7099655517; DECISIONS ME-6).
- What the paraphrase says: DR-2 and DR-1d are not adopted as deny rules, so the added texts of V4, V27 and V27-glossary PASS with no hit and V15 is REVIEW only (the "V4 reversal").
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names V5-D1 (E-014, E-033, E-034, E-055, E-1001, E-1011, E-1016, E-1113, E-1114, E-1126, E-1364, E-1365, E-1366), and the requirements that state the deferred V4 decision.
- Requirements affected: R6.PUR.8, R6.PUR.9, R6.DENY.1, R6.DENY.2, R6.DENY.5, R6.DENY.6, R6.CTRL.7, R6.CTRL.14, R6.CTRL.15, R6.A1CFG.7, OBL-3, OBL-6.
- Expectation rows affected: V4, V27, V27-glossary and V15, each carrying both candidate expectations marked "not authoritative; decided at r6 adoption" (RE-1).
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions D1 to D4

- Key: `D1-D4`
- Where recorded: v6.0e, recorded only in paraphrase (#1169 comment 7099655517; DECISIONS ME-6).
- What the paraphrase says: decision labels of v6.0e (the deny and context rules, the evidence figures and the selection rules they fix), recorded only in paraphrase
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names the label (E-014, E-034, E-039, E-046, E-076, E-090, E-111, E-163, E-1021, E-1062, E-1188, E-1283, E-1364, E-1367).
- Requirements affected: R6.ANCH.14, R6.CTX.1, R6.CTX.12, R6.REC.14, R6.DENY.5, R6.CTRL.19, R6.PLAN.8, R6.EVID.4, R6.EVID.5, OBL-3, OBL-15.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision V5-D2

- Key: `V5-D2`
- Where recorded: v6.0e, recorded only in paraphrase (#1169 comment 7099655517; DECISIONS ME-6).
- What the paraphrase says: the W2 allow rules replacing the first two RESIDUAL_ALLOW entries and the blanket (A1) strip, recorded only in paraphrase
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names the label (E-014, E-033, E-034, E-1024, E-1364).
- Requirements affected: R6.DENY.5, OBL-3.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions S1-D1 to S1-D3

- Key: `S1-D1 to S1-D3`
- Where recorded: v6.0e, no record on GitHub (DECISIONS ME-5).
- What the paraphrase says: the S1 allow-rule and rule-application decisions of v6.0e, with no recorded owner text
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names the label (E-014, E-034, E-128, E-130, E-1021, E-1192, E-1364).
- Requirements affected: R6.RULE.2, R6.RULE.4, R6.DENY.5, R6.CTRL.14, OBL-3.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions R-D1, R-D3, R-D5

- Key: `R-D labels`
- Where recorded: v6.0e, no record on GitHub (DECISIONS ME-5).
- What the paraphrase says: decisions on profile extraction, execution identity and durable evidence cited in v6.0e, with no recorded owner text
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names the label (E-014, E-034, E-097, E-121, E-147).
- Requirements affected: R6.OUT.14, R6.PROF.9, R6.REC.18.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision A-D5

- Key: `A-D labels`
- Where recorded: v6.0e, no record on GitHub (DECISIONS ME-5).
- What the paraphrase says: the durable-evidence decision cited in v6.0e, with no recorded owner text
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names the label (E-014, E-034, E-097).
- Requirements affected: R6.OUT.14.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision #1169 comment 7093128173 (landing order)

- Key: `7093128173`
- Where recorded: quoted in r6 only from a reviewer's paraphrase (RV-002).
- What the paraphrase says: the tool lands first; the plan's PREREG.md is amended and re-frozen so that every mandatory check of its sec. 11 passes as written; the four trees are distinguished; the execution-exception route of comment 7092885251 is superseded.
- Rule used to find the requirements: requirements that cite RV-002 or quote the comment.
- Requirements affected: R6.STAT.8.
- Note: the landing order it states (tool first) also fixes the gate order traced in sec. 32 of DESIGN-r6.md.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 17 (E-003)

- Key: `v6.0e line 17`
- Where recorded: owner decision of 2026-11-24 relayed in session; no comment id held (DECISIONS ME-5).
- What the paraphrase says: v6.0d bounded editorial correction (O-4 fix and nits)
- Rule used to find the requirements: the mapping records the quote as history and locates no requirement that restates it.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 31 (E-004)

- Key: `v6.0e line 31`
- Where recorded: owner decision of 2026-11-24 relayed in session; no comment id held (DECISIONS ME-5).
- What the paraphrase says: v6.0c correction: restore the v5.5.9 pre-run pin check; keep the consumer checks; no automated owner-authorization verification
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-151).
- Requirements affected: R6.REC.19.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 54 (E-005)

- Key: `v6.0e line 54`
- Where recorded: owner decision of 2026-11-24 relayed in session; no comment id held (DECISIONS ME-5).
- What the paraphrase says: v6.0b correction: the tool commit on main's first-parent history; executable dependencies and the import environment covered by the integrity checks; the hashlib.py negative control
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-147, E-148, E-149, E-150, E-151, E-152, E-153, E-154, E-155).
- Requirements affected: R6.REC.18, R6.REC.19, R6.REC.20, R6.REC.21, R6.REC.22.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 75 (E-006)

- Key: `v6.0e line 75`
- Where recorded: owner decision of 2026-11-24 relayed in session; no comment id held (DECISIONS ME-5).
- What the paraphrase says: v6.0a correction: B-1 to B-3; the fixed meaning table for B-4; ls-remote failure handling and mismatched-identity negative tests; a later A1 plan-amendment requirement
- Rule used to find the requirements: the mapping records the quote as history and locates no requirement that restates it.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 95 (E-008)

- Key: `v6.0e line 95`
- Where recorded: owner decision of 2026-11-24 relayed in session; no comment id held (DECISIONS ME-5).
- What the paraphrase says: remove automated owner-authorization verification; keep explicit owner authorization procedural; preserve every technical verification guarantee
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-010, E-012, E-057).
- Requirements affected: R6.STAT.4, R6.PUR.11.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## r4/r5 authorization quote at r5 line 7 (A-002)

- Key: `r5:7`
- Where recorded: quoted in r5 with author and date, no comment id (DECISIONS ME-5).
- What the paraphrase says: authorizes the Stage A review and the bounded tool design limited to O-9 and the item 2 record interfaces; no implementation or Stage B.
- Rule used to find the requirements: the mapping records the quote as history; r6 takes its authority from its own adoption (ME-5), and no requirement restates the quote.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Labels cited in r6 but not on the owner's list

The labels D5-D8 and DI-2 of v6.0e are also decision labels with no recorded owner text (sec. 34 of DESIGN-r6.md quotes them as labels). They were not on the list this file was asked to cover, and no requirement is marked for them; the owner may add them.
