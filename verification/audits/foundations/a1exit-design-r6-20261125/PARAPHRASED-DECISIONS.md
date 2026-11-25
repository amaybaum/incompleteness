# r6: requirements resting on paraphrased or unrecorded owner decisions

This list does not reconstruct any authorization. Each entry names an owner decision that r6's requirements rest on, the class of its record, what the record says, the rule by which the requirements were found, and the requirements found. Each listed requirement is marked in DESIGN-r6.md with "Pending owner confirmation (see PARAPHRASED-DECISIONS.md)." and carries the decision key in the field `pending_owner_confirmation` of REQUIREMENTS.json. The exact wording, purpose and consequences of each listed requirement are in FRESH-AUTHORIZATION.md; the evidence for each class is in AUTHORIZATIONS.md.

Classes of record (verified by reading the #1169 comments with GET requests):

- (i) owner's own words on GitHub: a comment that quotes the owner's words explicitly; such decisions need no entry here and are listed in AUTHORIZATIONS.md;
- (ii) session-written record on GitHub, no owner words: a comment posted from the `amaybaum` account by the coordinating session that records an owner decision in the session's words and quotes no owner words;
- (iii) no GitHub record: the decision is stated only in design documents relayed in session, with no comment id.

Options for every entry:

- (a) confirm in the owner's own words: the owner records the decision in a comment, which r6 quotes byte-exact with author and time (AGENTS.md sec. A.42 item 7);
- (b) fresh authorization: the owner decides the question anew, in a recorded decision, and r6 cites that record;
- (c) withdraw the requirement: the requirement, or the part of it that rests on the decision, is removed or narrowed, with its verification traced (R6.STAT.5).

Requirements marked: 44.

***

## Owner decision V5-D1 (DR-1d and DR-2 dropped from the active deny set; DR-3 kept with its real witness)

- Key: `V5-D1`
- Class: (ii) session-written record on GitHub, no owner words
- Record on GitHub (exact text):
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "drop deny rules DR-1d and DR-2 from the active set, with their purpose and patterns kept in a rejected-candidate history; keep DR-3 with its real witness in AGENTS.md at the scientific base"
- Where else stated: DESIGN-v5.5.9.md (records-branch copy, blob e5b97ef1), lines 116-119; lines 120-122 state that the writer held no comment id.
- What it says: DR-1d and DR-2 are not in the active deny set; their patterns are kept as history; DR-3 is kept with the sentence of AGENTS.md at H, lines 37-39, as its witness. As a consequence the added texts of V4, V27 and V27-glossary PASS with no hit and V15 is REVIEW_REQUIRED only (the V4 reversal). The deferral of the V4 reversal rests on class (i) records: #1169 comments 7160980912 (Q10, RD-14), 7162098696 (RE-1), 7163402499 (item 6) and 7164340996.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names V5-D1 (E-014, E-033, E-034, E-055, E-1001, E-1011, E-1016, E-1113, E-1114, E-1126, E-1364, E-1365, E-1366), and the requirements that state the deferred V4 decision; less R6.DENY.1 and R6.DENY.2, whose content does not depend on the decision (F4).
- Requirements affected: R6.PUR.8, R6.PUR.9, R6.DENY.5, R6.DENY.6, R6.CTRL.7, R6.CTRL.14, R6.CTRL.15, R6.A1CFG.7, OBL-3, OBL-6.
- Note: The four expectation rows V4, V27, V27-glossary and V15 carry both candidate expectations, each "not authoritative; decided at r6 adoption" (RE-1). The row of sec. 33 that retires DR-1d and DR-2 ("obsolete: dropped deny candidates ...; never reused") also rests on V5-D1; it is a table row, not a requirement, and carries no mark.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision V5-D2 (the review profile `resid` widened)

- Key: `V5-D2`
- Class: (ii) session-written record on GitHub, no owner words
- Record on GitHub (exact text):
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "widen the residual review profile `resid` as the review proposed"
- Where else stated: DESIGN-v5.5.9.md, lines 118-119: "V5-D2, widen `resid` as the v4 review's V8 proposes (sec. 6.6)"; the inventory item E-1024 (v6.0e sec. 6.6) records the widening.
- What it says: `resid` is widened by the parts resid-b ("finite set"; a state-space noun followed by "is finite") and resid-c ("substratum", "universe" or "world" followed by "is finite"; "finite number" or "finite count"), as v6.0e sec. 6.6 states them. The W2 allow rules do not rest on V5-D2 or on any other owner decision: v6.0e sec. 6.5 presents them as seed rules "for review; not adopted".
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names V5-D2 (E-014, E-033, E-034, E-1024, E-1364), and R6.PUR.8, whose informative classes include resid-b and resid-c (F7).
- Requirements affected: R6.PUR.8, R6.DENY.5, OBL-3.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions v3 D1-D4 (v3's open points 1-4: adopt the v3 review's recommendations)

- Key: `v3 D1-D4`
- Class: (ii) session-written record on GitHub, no owner words
- Record on GitHub (exact text):
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
  - #1169 comment 7099655517 (2026-11-23T11:26:50Z): "On the v3 review's open points D1 to D4: adopt the reviewer's recommendations (the item-7 restatement is a plan amendment, with the literal check kept as a countercontrol; per unit stays true; preregistered indicators; reproduced counts; the writer, reviewer, owner, frozen configuration and verifier chain for records)."
- Where else stated: DESIGN-v5.5.9.md, lines 114-115; DESIGN-v3.md sec. 15 states the open points.
- What it says: D1: the restatement of item 7 is a plan amendment, with the literal check kept as a countercontrol. D2: the context mapping as proposed, with `per unit` on the required side. D3 and D4: preregistered indicators, reproduced counts, and the writer, reviewer, owner, frozen configuration and verifier chain for records.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names D1, D2, D3 or D4 in this sense (E-076, E-1283, E-1367), and R6.CTX.4 (`per unit` on the required side), whose content the paraphrase states (F7). Requirements citing D1-D8 of the Stage 1 review are keyed S1-D2 instead (F3).
- Requirements affected: R6.CTX.1, R6.CTX.4, R6.CTX.12, R6.PLAN.8.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision S1-D2 (apply the Stage 1 review's design corrections D1-D8)

- Key: `S1-D2`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: DESIGN-v5.5.9.md, lines 94-98, and CHANGES-v5.2.md, lines 18-22 ("S1-D2: apply D1-D8."). D1 to D8 are findings of the Stage 1 review (`review-stage1/review-stage1.md`), not owner decisions; CHANGES-v5.2.md sec. 1 re-derives each. #1169 comment 7158801838, a result comment written by the coordinating session, mentions S1-D2 in passing and is not a record of the decision.
- What it says: D1: W1-c's `negative_allowance` and the self-PASS lint; D2: SW2's expectation; D3: 7 HP structure REVIEWs; D4: the LF-inclusive site span (215 region lines); D5: RT-D's 45 `resid` lines; D6: per-splice `register` and `infinity` semantics with parity to P; D7: `rule-stale` scoping; D8: matching on source bytes.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names D1 to D8 in the Stage 1 sense (E-039, E-046, E-090, E-111, E-115, E-133, E-134, E-163, E-1021, E-1062, E-1188, E-1234). R6.ANCH.14, R6.REC.14, R6.CTRL.19, R6.EVID.4, R6.EVID.5 and OBL-15 were keyed "D1-D4" (F3); R6.DENY.5 and OBL-3 were keyed "D1-D4" through E-1021, whose label "(S1-D1, D1)" is the Stage 1 D1 (F3); R6.RULE.7, R6.RULE.8, R6.RULE.9, R6.CTRL.24 and OBL-1 were unmarked (F7).
- Requirements affected: R6.ANCH.14, R6.RULE.7, R6.RULE.8, R6.RULE.9, R6.REC.14, R6.DENY.5, R6.CTRL.19, R6.CTRL.24, R6.EVID.4, R6.EVID.5, OBL-1, OBL-3, OBL-15.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions S1-D1 to S1-D3 (the Stage 1 review: W1 option B; apply D1-D8; specify B1-B6)

- Key: `S1-D1 to S1-D3`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: DESIGN-v5.5.9.md, lines 94-98; CHANGES-v5.2.md, lines 18-22 and the paragraph "W1 option B (D1 and S1-D1)".
- What it says: S1-D1: the W1 self-match is resolved by option B (the full negative list kept; a fingerprint-bound `negative_allowance`). S1-D3: specify configuration admission, native delegated execution, the classification of `C`, widening reviews, engine purity over the adapter companions, and control reporting (B1-B6).
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names S1-D1, S1-D2 or S1-D3 (E-014, E-034, E-128, E-130, E-1021, E-1192, E-1364). S1-D3 underlies parts of secs. 11, 13 and 16, but no inventory item a requirement cites names it, so the rule marks none of those requirements (open item).
- Requirements affected: R6.RULE.2, R6.RULE.4, R6.DENY.5, R6.CTRL.14, OBL-3.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decisions R-D1, R-D3, R-D5 (on the v5.4 review and its addendum C1-C4)

- Key: `R-D labels`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: DESIGN-v5.5.9.md, lines 58-64 ("stricter refusals, withdrawal integrity, execution identity, the authority configuration, durable evidence").
- What it says: R-D1: the stricter refusals; R-D3: execution identity; R-D5: durable evidence. The labels C3 and C4 are findings of the v5.4 review addendum, applied under these decisions; R6.OUT.14 cites C3 with R-D5 and R6.PROF.9 cites C4 with R-D1.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names R-D1, R-D3 or R-D5 (E-014, E-034, E-097, E-121, E-147), and the requirements whose Sources cite an item that names C3 or C4 (E-098, E-158, E-1218, E-1219, E-1243): R6.OUT.15, R6.REC.24, R6.CTRL.17, R6.CTRL.23 and R6.CTRL.24 (F7).
- Requirements affected: R6.OUT.14, R6.OUT.15, R6.PROF.9, R6.REC.18, R6.REC.24, R6.CTRL.17, R6.CTRL.23, R6.CTRL.24.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision A-D5 (durable evidence; the authority values A-D1 to A-D5)

- Key: `A-D labels`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: DESIGN-v5.5.9.md, lines 69-75.
- What it says: A-D5: durable evidence.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names A-D5 (E-014, E-034, E-097).
- Requirements affected: R6.OUT.14.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner's final decision D2 of 2026-11-23 (the three stricter refusal classes)

- Key: `v5.5.9 final D2`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: DESIGN-v5.5.9.md, lines 44-46: "The three stricter refusal classes of sec. 6.1 are accepted, with the evidence that valid frozen-plan operations are not rejected".
- What it says: The tool refuses (i) a splice for the unselected variant, (ii) one splice covering two edits, (iii) chained edits. The final decisions D3 (the freeze ledger) and D4 (the authority record) of the same list are obsolete since v6.0 and no r6 requirement rests on them.
- Rule used to find the requirements: the requirement that states the three refusal classes, R6.PROF.9 (F3).
- Requirements affected: R6.PROF.9.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision DI-2, option A, narrow (lineage of a superseding record by `record_id`)

- Key: `DI-2`
- Class: (ii) session-written record on GitHub, no owner words
- Record on GitHub (exact text):
  - #1169 comment 7121574479 (2026-11-24T03:57:23Z): "Recorded by the coordinating session."
  - #1169 comment 7121574479 (2026-11-24T03:57:23Z): "DI-2 option A, narrow (lineage of a superseding record by `record_id`)"
- Where else stated: DESIGN-v5.5.8.md and DESIGN-v5.5.9.md (adopted per the same comment).
- What it says: A superseding record shares its predecessor's kind, schema and `record_id`; the chain is valid, acyclic and single-headed.
- Rule used to find the requirements: requirements whose Sources cite an inventory item that names DI-2 (E-141, E-1332 to E-1340): R6.REC.6, R6.REC.7 and R6.CTRL.22 (F7).
- Requirements affected: R6.REC.6, R6.REC.7, R6.CTRL.22.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Owner decision recorded in #1169 comment 7093128173 (landing order; the exception-free route)

- Key: `7093128173`
- Class: (ii) session-written record on GitHub, no owner words
- Record on GitHub (exact text):
  - #1169 comment 7093128173 (2026-11-23T06:13:50Z): "Recorded by the coordinating session from the owner's direct instruction in this session."
  - #1169 comment 7093128173 (2026-11-23T06:13:50Z): "The execution-exception approach of c.7092885251 is superseded and will not be used."
  - #1169 comment 7093128173 (2026-11-23T06:13:50Z): "land the tool through its own reviewed pull request and a separate merge decision;"
  - #1169 comment 7093128173 (2026-11-23T06:13:50Z): "amend `PREREG.md` to specify the new tool and its exact verification commands, so that every mandatory check of sec. 11 passes as written; then independent review and a new freeze"
  - #1169 comment 7093128173 (2026-11-23T06:13:50Z): "The amended plan distinguishes the immutable scientific base H, the current integration base on `main`, the candidate retirement tree and the final landing merge tree"
- Where else stated: the comment itself (2026-11-23T06:13:50Z); paraphrased by the v2 review (RV-002).
- What it says: The tool lands first through its own reviewed pull request; PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written; the four trees are distinguished; the execution-exception route of comment 7092885251 is superseded. The comment quotes no owner words, so R6.STAT.8 can be confirmed only by the owner restating it (RE-26 option (b)).
- Rule used to find the requirements: requirements that cite RV-002 or quote the comment.
- Requirements affected: R6.STAT.8.
- Note: The landing order it states also fixes the gate order traced in sec. 32 of DESIGN-r6.md.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 17 (E-003; the v6.0d editorial correction)

- Key: `v6.0e line 17`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in DESIGN-v6.0e.md, lines 17-21, "no comment id held by this writer".
- What it says: Approve the bounded v6.0d editorial correction (the O-4 fix and the nits) and a focused delta review.
- Rule used to find the requirements: the mapping records the quote as history and locates no requirement that restates it.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 31 (E-004; the v6.0c correction)

- Key: `v6.0e line 31`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in DESIGN-v6.0e.md, lines 31-41, "no comment id held by this writer".
- What it says: Restore the v5.5.9 pre-run pin check; verify executable dependencies before the tool runs; retain the consumer checks; do not reintroduce automated owner-authorization verification.
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-151).
- Requirements affected: R6.REC.19.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 54 (E-005; the v6.0b correction)

- Key: `v6.0e line 54`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in DESIGN-v6.0e.md, lines 54-67, "no comment id held by this writer".
- What it says: The tool commit belongs to main's first-parent history; the workflow's executable dependencies and the import environment are covered by the integrity checks; the hashlib.py negative control.
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-147 to E-155).
- Requirements affected: R6.REC.18, R6.REC.19, R6.REC.20, R6.REC.21, R6.REC.22.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 75 (E-006; the v6.0a correction)

- Key: `v6.0e line 75`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in DESIGN-v6.0e.md, lines 75-87, "no comment id held by this writer".
- What it says: B-1 to B-3; the fixed meaning table for B-4; ls-remote failure handling and mismatched-identity negative tests; a later A1 plan-amendment requirement.
- Rule used to find the requirements: the mapping records the quote as history and locates no requirement that restates it.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## v6.0e status quote at line 95 (E-008; owner decisions of 2026-11-24 on the reduced design)

- Key: `v6.0e line 95`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in DESIGN-v6.0e.md, lines 95-127, "this writer holds no comment id for them".
- What it says: Remove automated owner-authorization verification; keep explicit owner authorization procedural; preserve every technical verification guarantee; "the tool verifies which exact plan was executed; the owner confirms that it was the approved plan."
- Rule used to find the requirements: requirements whose Sources cite the items that the mapping says restate the quote's substance (E-010, E-012, E-057).
- Requirements affected: R6.STAT.4, R6.PUR.11.
- Note: #1169 comment 7130449822 quotes the owner's adoption of v6.0e, whose text contains this removal; its prose description of v6.0e is the session's. The adoption of v6.0e is context and is not treated as authorizing any r6 requirement (F9 of the grouped presentation).
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## r4/r5 authorization quote at r5 line 7 (A-002)

- Key: `r5:7`
- Class: (iii) no GitHub record
- Record on GitHub: none.
- Where else stated: quoted in r5 (sha256 11a9077c...a653), line 7, with author and date and no comment id.
- What it says: Authorize the Stage A review and the bounded tool design limited to O-9 and the item 2 record interfaces; no implementation or Stage B.
- Rule used to find the requirements: the mapping records the quote as history; r6 takes its authority from its own adoption, and no requirement restates the quote.
- Requirements affected: none found by the rule; nothing in r6 is marked for this entry, and it is listed so that the owner can confirm, re-authorize or withdraw it.
- Note: The companion instruction quoted in r5, "Accept V1 on the existing evidence and start the design", is a class (i) record: #1169 comment 7153270569.
- Options: (a) confirm in the owner's own words; (b) fresh authorization; (c) withdraw the requirement.

***

## Requirements no longer marked

- R6.DENY.1 and R6.DENY.2 cited E-1001 only because that item mentions the retired DR-1d and DR-2. Their content (rule records are plan records; the controls run on pinned rule inputs) does not depend on V5-D1, so they are not marked. Like every requirement of r6 they take effect only by r6's adoption; they are listed in FRESH-AUTHORIZATION.md.
