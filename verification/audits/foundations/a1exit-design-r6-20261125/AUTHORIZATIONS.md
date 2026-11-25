# r6: authorizations and decision records the design relies on

Every decision label the design relies on, classified by its record, with the evidence and with what it permits and does not permit. The comments were read with GET requests; for each, the time is the API's `created_at` and the body digest is the sha256 of the body as returned.

Classes: (i) owner's own words on GitHub; (ii) session-written record on GitHub, no owner words; (iii) no GitHub record.

| Comment | created_at | Body sha256 |
|---|---|---|
| 7093128173 | 2026-11-23T06:13:50Z | 8f0c5ad57037e5c42b6a4e92c47c51c721a597e970370fd2d5b9d016194c7818 |
| 7099655517 | 2026-11-23T11:26:50Z | 2bc6fb0b2ba132d1aa7eddb4ac970ead347694dee9eb7de60f133158f074806c |
| 7121574479 | 2026-11-24T03:57:23Z | 834a1ce28ed40ad7428102037fdcfa08347fb9d69abfd270c6a33d1e8158b834 |
| 7130449822 | 2026-11-24T11:42:47Z | 7b50a77025c9ba151608c518cb50bb5c0bb88978b921ff9eabae99a95faab553 |
| 7153270569 | 2026-11-25T04:54:22Z | e258195f4f27007bd19646dea9cdf557c6b4a67257af309662153dd6a1734060 |
| 7158516152 | 2026-11-25T09:34:34Z | 66abea92375b03793e7ce785f7678906f0c1c951088777cd26d48863330c591c |
| 7158801838 | 2026-11-25T09:47:20Z | 4d357fa241d36103d4fac38b841aa34c31cd6367e4ef6fc0378338b502adda3b |
| 7159270333 | 2026-11-25T10:08:02Z | 69895328db345b3df0992043f93c1b006fd50a62443be5ea16c20f3abc673996 |
| 7160281751 | 2026-11-25T10:52:11Z | e4451b76f631efe1c3ce2c079137f5184190c3738f59e31aea5df1d48042c8c1 |
| 7160980912 | 2026-11-25T11:23:22Z | a14e02bf45792f86c396cf3c2eabfa5355f776bfd2fe7149d98c28f03b0d4659 |
| 7162098696 | 2026-11-25T12:14:08Z | 6b5195836312e9a1ca44005ea4e1bfe0cdee0fadbf568252845bd2a54835d226 |
| 7163402499 | 2026-11-25T13:10:44Z | d5a1e5e01cc8d80ff80affffd0c9c88360b6e207ef35765fa4f7ff90ae6d95d5 |
| 7164065815 | 2026-11-25T13:38:08Z | da785f9d2d6bae25ca6fc7863633d0ffb069d2bd568ea7549097e5849f27dd8c |
| 7164340996 | 2026-11-25T13:49:23Z | ac62be9373cdf8e2895cae88460a6e4d1b08cd5c02661ac092dc41ddd28f4ff2 |
| 7166666428 | 2026-11-25T15:19:37Z | e0441dc53e73a3888a800275ff26ce244372b9e32c51ebb0ea597dde41abc74d |
| 7166844576 | 2026-11-25T15:26:24Z | ea7e0eb371df129a747a0353eb72b25be13f3b154aa578e99733dd968149d931 |

***

## 1. Class (i): the owner's own words on GitHub

Each of these comments is posted from the `amaybaum` account by the coordinating session. Each contains a passage introduced as the owner decision and quoted; that passage is the owner's own words. Where the owner approves a proposal "as proposed" or "including the refinements", the proposal text (quoted in the comment as relayed from the owner's independent review) and the session's refinements are approved by reference to that quoted approval; the refinements themselves are the session's words. None of these records adopts r6 or any requirement of it (N1): 7130449822 adopts v6.0e and authorizes its local implementation; 7153270569 starts the design; 7158516152 authorizes a read-only assessment; the others authorize drafting, correction, presentation or the decisions they state on r6, and each excludes adoption of r6.

### #1169 comment 7130449822 (2026-11-24T11:42:47Z): adoption of design v6.0e

Owner's words and approved text (exact):

- "Adopt DESIGN-v6.0e.md, exact SHA-256:"
- "Authorize local implementation of v6.0e on the existing tool branch."

- Permits: v6.0e (sha256 4024a31c...5131) is the authoritative design until r6 is adopted; local implementation of v6.0e on the existing tool branch.
- Does not permit: Adoption of any r6 requirement: r6 names its own adoption as its authority (R6.STAT.1), and the later quoted instructions defer the V4 reversal although v6.0e expects V4 PASS. Push, CI execution and merge ("separately authorized actions").
- Relied on by: context for every requirement restated from v6.0e (the inventory items E-*).

### #1169 comment 7153270569 (2026-11-25T04:54:22Z): start of the r5 design amendment

Owner's words and approved text (exact):

- "Accept V1 on the existing evidence and start the design"

- Permits: starting the bounded design amendment for O-9 and the item-2 records after the Stage A review.
- Does not permit: any r6 requirement; implementation; Stage B.
- Relied on by: the provenance of r5 (A-items); r6 cites r5 as provenance only.

### #1169 comment 7158516152 (2026-11-25T09:34:34Z): read-only design dependency and consistency assessment

Owner's words and approved text (exact):

- "Recover exact requirements, evidence and owner decisions without reconstructing missing authorization from paraphrases."

- Permits: the read-only assessment and recording it on #1169.
- Does not permit: changes to the design, implementation, control expectations or exceptions; any commit, push or merge.
- Relied on by: the findings behind DECISIONS.md, including ME-5 and ME-6 (owner decisions without a record or recorded only in paraphrase).

### #1169 comment 7159270333 (2026-11-25T10:08:02Z): preparation of the consolidated design r6

Owner's words and approved text (exact):

- "Authorize preparation of the consolidated, self-contained design r6 as proposed, including the inventory-first approach and the single authoritative machine-readable expectation architecture."
- "The consolidated design must preserve every authoritative requirement unless its supersession is explicitly authorized."
- "No design adoption, implementation, control-expectation changes, new exceptions, CI dispatch, merge or A1 retirement execution are authorized."

- Permits: preparing r6, its inventories, mapping and proposed controls; committing and pushing the design documents to the design branch for exact-head independent review.
- Does not permit: design adoption, implementation, control-expectation changes, new exceptions, CI dispatch, merge, A1 retirement execution; the supersession of an authoritative requirement without explicit authorization.
- Relied on by: the r6 drafting as a whole (R6.STAT.1, R6.STAT.2).

### #1169 comment 7160281751 (2026-11-25T10:52:11Z): DECISIONS.md (OD-1 to OD-31), Q1-Q5, the 20 mechanical corrections, the 12 verification defects, the missing-evidence treatment (ME-*), the OD-31 migration

Owner's words and approved text (exact):

- "Approve the proposed authorization with qualifications Q1-Q5 as stated, including the refinements in your latest message."
- "Approve the recommended decisions in DECISIONS.md at commit 4e9a1501 as the basis for drafting the consolidated r6 specification, subject to qualifications Q1-Q5 below."
- "Approve the 20 mechanical corrections where they restore unambiguous approved requirements, the specification of corrections for the 12 verification defects, and the OD-31 identifier migration with complete historical traceability."
- "Q5. Adopt the proposed missing-evidence treatment, subject to preserving transferred requirements as explicit outstanding obligations."
- "Preserve all existing safeguards unless their withdrawal is explicitly approved."

- Permits: drafting r6 on the basis of those recommended decisions and qualifications.
- Does not permit: adoption of r6 or of any decision as a requirement in force; implementation; control-expectation changes in the executable tool; exceptions; CI dispatch; merge; A1 retirement execution; the withdrawal of a safeguard that is not explicitly approved.
- Relied on by: the Sources labels OD-*, Q1-Q5, MC-*, VD-*, ME-*.

### #1169 comment 7160980912 (2026-11-25T11:23:22Z): RD-1 to RD-35 with Q6-Q10; deferral of the V4 reversal

Owner's words and approved text (exact):

- "Approve the proposed authorization with Q6-Q10 as stated, including all refinements in your latest message."
- "Approve the recommended resolutions of RD-1-RD-35 in RESIDUAL.md at commit c1244459 as the basis for completing the r6 draft, subject to Q6-Q10:"
- "Preserve the proximity/similarity prohibition, defer adoption of the V4 reversal, and retain outstanding evidence obligations as named blockers."
- "Q10: Preserve substantive safeguards, explicitly describe the V4 reversal and its consequences, and retain unavailable evidence and unexecuted required controls as outstanding obligations."

- Permits: completing the r6 draft on the basis of those resolutions; stating the V4 reversal and its consequences for decision at r6 adoption.
- Does not permit: adoption of the V4 reversal ("defer adoption of the V4 reversal"); adoption of r6; implementation; CI dispatch; merge; exceptions; A1 retirement execution.
- Relied on by: the Sources labels RD-* and Q6-Q10; the deferral clauses of R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6 and R6.A1CFG.7.

### #1169 comment 7162098696 (2026-11-25T12:14:08Z): RE-1 to RE-38 with Q11-Q16; V4 group deferred; paraphrased decisions to be presented

Owner's words and approved text (exact):

- "Approve the proposed authorization with Q11-Q16 as stated, including the refinements in your latest message."
- "Approve the recommended resolutions of RE-1-RE-38 in RESIDUAL-2.md at commit f4e18558, using the revised Section E recommendations where they supersede the original entries, subject to Q11-Q16."
- "Keep V4, V27, V27-glossary and V15 deferred to an explicit adoption decision. Recover or freshly authorize any requirement supported only by paraphrased owner decisions; do not reconstruct historical authorization."
- "Present all requirements supported only by paraphrased owner decisions for explicit confirmation or fresh authorization."

- Permits: completing and regenerating the integrated r6 draft on the basis of those resolutions; presenting the requirements supported only by paraphrased owner decisions for explicit confirmation or fresh authorization.
- Does not permit: deciding the V4 group ("deferred to an explicit adoption decision"); reconstructing historical authorization; adoption; implementation; CI dispatch; merge; exceptions; A1 retirement execution.
- Relied on by: the Sources labels RE-* and Q11-Q16; the `candidate_expectations` and DEFERRED outcome that the four V4-group rows carried until owner decision 3 (RE-1); the marking of requirements as pending owner confirmation.

### #1169 comment 7163402499 (2026-11-25T13:10:44Z): the bounded specification correction OC-1 to OC-5

Owner's words and approved text (exact):

- "Authorize the bounded specification correction as proposed, including both refinements in your latest message."
- "1. Resolve OBL-16 by specifying TR5 consistently with the §A.39 lifecycle: exact-candidate validation before F designation, designation identity verification, and durable evidence verification at landing. Do not require F to land prematurely."
- "2. Resolve OBL-26 by distinguishing specification adoption from certification of implementation conformance. Preserve §A.42's durable evidence requirements for every enduring claim. Report any remaining governance conflict explicitly."
- "3. For OBL-13, OBL-14, OBL-15 and OBL-23, specify which candidate evidence supports landing decisions and which reproducible evidence supports enduring claims. Investigate replacement controls using reachable pinned inputs where appropriate. Do not substitute byte equality for ancestry where ancestry is material."
- "4. Keep LC-7 REVIEW_REQUIRED pending an explicitly specified and independently reviewed regeneration verification procedure."
- "6. Keep the four V4-group expectations deferred."
- "Present the 33 pending requirements grouped by underlying owner decision, with exact proposed wording, consequences and safeguards affected, together with any remaining contradictions."
- "No governance-rule amendment, exception expansion, design adoption, implementation change, CI dispatch, merge or A1 retirement execution is authorized."

- Permits: the corrections OC-1 to OC-5 (items 1 to 4 and 6 of the quoted proposal, which the owner authorized "as proposed"), regeneration of the affected documents, and the grouped presentation of the 33 pending requirements.
- Does not permit: a governance-rule amendment, exception expansion, design adoption, implementation change, CI dispatch, merge or A1 retirement execution.
- Relied on by: the Sources label OC-1 to OC-5 (R6.STAT.10, R6.EVID.8, OBL-13 to OBL-16, OBL-23, OBL-26, LC-7 and the adoption trace of sec. 32).

### #1169 comment 7164340996 (2026-11-25T13:49:23Z): this correction round (F1-F8 and the unmarked requirements)

Owner's words and approved text (exact):

- "A1 design r6: Proceed with the second correction round, addressing F1–F8 and the additional unmarked requirements. Preserve all existing safeguards and keep the V4 group deferred. Prepare the corrected design for independent review. This does not authorize adoption, freezing or execution."

- Permits: correcting F1 to F8 of the grouped presentation and marking the additional unmarked requirements; preparing the corrected design for independent review.
- Does not permit: adoption, freezing or execution; changing the V4 group; weakening any existing safeguard.
- Relied on by: this round's edits (CORRECTION-REPORT.md).

### #1169 comment 7166844576 (2026-11-25T15:26:24Z): owner decisions 1-5 on the decision package of r6

Owner's words and approved text (exact):

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

> 3. Choose option (a).
>
> Accept the reversal and retain human review for V15. Do not introduce additional rules based solely on constructed examples without an established scientific or verification need.
>
> This is a decision about the automated checker's scope, not permission to make scientifically unsupported claims about finiteness.

> 4. Approve all three proposed provenance fixes.
>
> * Prepare the r6 directory and review record for landing on `main`. Merge approval remains separate.
>
> * Establish the LC-7 regeneration and byte-comparison procedure, with independent review.
>
> * Treat the earlier T1′ figure solely as candidate evidence, not acceptance support.

> 5. Authorize the final bounded text-only revision and delta review.
>
> Include decisions 1–4 and address R1–R6 and N1–N6 within the identified scope.
>
> However, do not use adoption as blanket authorization for potentially under-marked S1-D3 requirements. Explicitly identify those requirements and establish their authorization status. Include them in the final adoption decision if necessary.
>
> Non-confirmation must leave a requirement pending, not withdraw it.
>
> This authorizes the final design revision and its review, not adoption, implementation, freezing, trial execution or merging.

- Permits: confirming the 41 requirements of decision 1 and the two scope statements; deferring R6.OUT.15 with its replay mode; the classes of the 12 flagged requirements; resolution (a) of the V4 group; the three provenance fixes; this final text-only revision and one bounded delta review.
- Does not permit: adoption, implementation, freezing, trial execution or merging (decision 5); merge approval of the landing (decision 4: "Merge approval remains separate."); using adoption as blanket authorization for the requirements resting on S1-D3 (decision 5); scientifically unsupported claims about finiteness (decision 3).
- Relied on by: the confirmation, scope and deferral notes of decision 1; R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6, R6.A1CFG.7 and the four V4-group rows (decision 3); R6.STAT.10, R6.TREE.19, OBL-23 (decision 4); the S1-D3 marks (decision 5); sec. 0.1 of DESIGN-r6.md.

***

## 2. Class (ii): session-written records without owner words

Each record below opens with "Recorded by the coordinating session" and states owner decisions in the session's words. It shows that a decision was reported, not its wording. By itself it permits nothing for r6: a requirement resting on it needs confirmation in the owner's words or fresh authorization (quoted instruction of #1169 comment 7162098696: "Present all requirements supported only by paraphrased owner decisions for explicit confirmation or fresh authorization."). Owner decision 1 of 2026-11-25 confirms the requirements so marked below.

### Owner decision V5-D1 (DR-1d and DR-2 dropped from the active deny set; DR-3 kept with its real witness)

- Key: `V5-D1`
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "drop deny rules DR-1d and DR-2 from the active set, with their purpose and patterns kept in a rejected-candidate history; keep DR-3 with its real witness in AGENTS.md at the scientific base"
- Where else stated: DESIGN-v5.5.9.md (records-branch copy, blob e5b97ef1), lines 116-119; lines 120-122 state that the writer held no comment id.
- What the record says was decided: DR-1d and DR-2 are not in the active deny set; their patterns are kept as history; DR-3 is kept with the sentence of AGENTS.md at H, lines 37-39, as its witness.
- Note: The four expectation rows V4, V27, V27-glossary and V15 carry the expectations of resolution (a) (owner decision 3). The row of sec. 33 that retires DR-1d and DR-2 ("obsolete: dropped deny candidates ...; never reused") also rests on V5-D1; it is a table row, not a requirement, and carries no mark. Consequence, from v6.0e's measurement and not stated in the record (N2): As a consequence the added texts of V4, V27 and V27-glossary PASS with no hit and V15 is REVIEW_REQUIRED only (the V4 reversal). The deferral of the V4 reversal rests on class (i) records: #1169 comments 7160980912 (Q10, RD-14), 7162098696 (RE-1), 7163402499 (item 6) and 7164340996. Owner decision 3 of 2026-11-25 (#1169 comment 7166844576) accepts the reversal in the owner's words.
- Permits: nothing by itself for r6.
- Does not permit: treating the session's paraphrase as the owner's wording; reconstructing authorization from it.
- Relied on by: R6.PUR.8 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.PUR.9 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.DENY.5 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.DENY.6 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTRL.7 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTRL.14 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.15 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.A1CFG.7 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); OBL-3 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); OBL-6 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### Owner decision V5-D2 (the review profile `resid` widened)

- Key: `V5-D2`
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "widen the residual review profile `resid` as the review proposed"
- Where else stated: DESIGN-v5.5.9.md, lines 118-119: "V5-D2, widen `resid` as the v4 review's V8 proposes (sec. 6.6)"; the inventory item E-1024 (v6.0e sec. 6.6) records the widening.
- What the record says was decided: `resid` is widened by the parts resid-b ("finite set"; a state-space noun followed by "is finite") and resid-c ("substratum", "universe" or "world" followed by "is finite"; "finite number" or "finite count"), as v6.0e sec. 6.6 states them. The W2 allow rules do not rest on V5-D2 or on any other owner decision: v6.0e sec. 6.5 presents them as seed rules "for review; not adopted".
- Note: The same record holds a separate decision, quoted: #1169 comment 7099655517 (2026-11-23T11:26:50Z): "The documented uncaught rephrasings are accepted as a coverage limitation. The tool must not claim complete semantic detection; the known missed forms are kept as limitations and regression controls."; it is the more direct basis for R6.PUR.8 (N2).
- Permits: nothing by itself for r6.
- Does not permit: treating the session's paraphrase as the owner's wording; reconstructing authorization from it.
- Relied on by: R6.PUR.8 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.DENY.5 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); OBL-3 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### Owner decisions v3 D1-D4 (v3's open points 1-4: adopt the v3 review's recommendations)

- Key: `v3 D1-D4`
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time"
- #1169 comment 7099655517 (2026-11-23T11:26:50Z): "On the v3 review's open points D1 to D4: adopt the reviewer's recommendations (the item-7 restatement is a plan amendment, with the literal check kept as a countercontrol; per unit stays true; preregistered indicators; reproduced counts; the writer, reviewer, owner, frozen configuration and verifier chain for records)."
- Where else stated: DESIGN-v5.5.9.md, lines 114-115; DESIGN-v3.md sec. 15 states the open points.
- What the record says was decided: D1: the restatement of item 7 is a plan amendment, with the literal check kept as a countercontrol. D2: the context mapping as proposed, with `per unit` on the required side. D3 and D4: preregistered indicators, reproduced counts, and the writer, reviewer, owner, frozen configuration and verifier chain for records.
- Permits: nothing by itself for r6.
- Does not permit: treating the session's paraphrase as the owner's wording; reconstructing authorization from it.
- Relied on by: R6.CTX.1 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTX.4 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTX.12 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.PLAN.8 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### Owner decision DI-2, option A, narrow (lineage of a superseding record by `record_id`)

- Key: `DI-2`
- #1169 comment 7121574479 (2026-11-24T03:57:23Z): "Recorded by the coordinating session."
- #1169 comment 7121574479 (2026-11-24T03:57:23Z): "DI-2 option A, narrow (lineage of a superseding record by `record_id`)"
- Where else stated: DESIGN-v5.5.8.md and DESIGN-v5.5.9.md (adopted per the same comment).
- What the record says was decided: A superseding record shares its predecessor's kind, schema and `record_id`; the chain is valid, acyclic and single-headed.
- Permits: nothing by itself for r6.
- Does not permit: treating the session's paraphrase as the owner's wording; reconstructing authorization from it.
- Relied on by: R6.REC.6 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.7 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.22 (confirmed by owner decision 1 (necessary for reliable verification))

### Owner decision recorded in #1169 comment 7093128173 (landing order; the exception-free route)

- Key: `7093128173`
- #1169 comment 7093128173 (2026-11-23T06:13:50Z): "Recorded by the coordinating session from the owner's direct instruction in this session."
- #1169 comment 7093128173 (2026-11-23T06:13:50Z): "The execution-exception approach of c.7092885251 is superseded and will not be used."
- #1169 comment 7093128173 (2026-11-23T06:13:50Z): "land the tool through its own reviewed pull request and a separate merge decision;"
- #1169 comment 7093128173 (2026-11-23T06:13:50Z): "amend `PREREG.md` to specify the new tool and its exact verification commands, so that every mandatory check of sec. 11 passes as written; then independent review and a new freeze"
- #1169 comment 7093128173 (2026-11-23T06:13:50Z): "The amended plan distinguishes the immutable scientific base H, the current integration base on `main`, the candidate retirement tree and the final landing merge tree"
- Where else stated: the comment itself (2026-11-23T06:13:50Z); paraphrased by the v2 review (RV-002).
- What the record says was decided: The tool lands first through its own reviewed pull request; PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written; the four trees are distinguished; the execution-exception route of comment 7092885251 is superseded. The comment quotes no owner words, so R6.STAT.8 can be confirmed only by the owner restating it (RE-26 option (b)).
- Note: The landing order it states also fixes the gate order traced in sec. 32 of DESIGN-r6.md.
- Permits: nothing by itself for r6.
- Does not permit: treating the session's paraphrase as the owner's wording; reconstructing authorization from it.
- Relied on by: R6.STAT.8 (confirmed by owner decision 1 (necessary for reliable verification))

***

## 3. Class (iii): no GitHub record

These decisions are stated only in design documents relayed in session, each without a comment id. A search of all comments on #1169 for distinctive phrases of each (for example "S1-D1", "R-D1", "A-D5", "three stricter", "chained edits", "Approve O-1 option (b)", "historical authorization verification entirely", "Authorize the Stage A review") found no record of the decision; the labels S1-D1, S1-D2 and S1-D3 occur only in later session-written result comments. #1169 comment 7158801838 lists them as owner decisions without a record: "decision labels S1, R-D and A-D; and the r4/r5 authorization quote at line 7."

### Owner decision S1-D2 (apply the Stage 1 review's design corrections D1-D8)

- Key: `S1-D2`
- Where stated: DESIGN-v5.5.9.md, lines 94-98, and CHANGES-v5.2.md, lines 18-22 ("S1-D2: apply D1-D8."). D1 to D8 are findings of the Stage 1 review (`review-stage1/review-stage1.md`), not owner decisions; CHANGES-v5.2.md sec. 1 re-derives each. #1169 comment 7158801838, a result comment written by the coordinating session, mentions S1-D2 in passing and is not a record of the decision.
- What it says: D1: W1-c's `negative_allowance` and the self-PASS lint; D2: SW2's expectation; D3: 7 HP structure REVIEWs; D4: the LF-inclusive site span (215 region lines); D5: RT-D's 45 `resid` lines; D6: per-splice `register` and `infinity` semantics with parity to P; D7: `rule-stale` scoping; D8: matching on source bytes.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.ANCH.14 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.RULE.7 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.RULE.8 (confirmed by owner decision 1 (necessary for reliable verification)); R6.RULE.9 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.REC.14 (confirmed by owner decision 1 (necessary for reliable verification)); R6.DENY.5 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTRL.19 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.24 (confirmed by owner decision 1 (necessary for reliable verification)); R6.EVID.4 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.EVID.5 (scope statement without a check of its own (owner decision 1)); OBL-1 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); OBL-3 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); OBL-15 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### Owner decisions S1-D1 to S1-D3 (the Stage 1 review: W1 option B; apply D1-D8; specify B1-B6)

- Key: `S1-D1 to S1-D3`
- Where stated: DESIGN-v5.5.9.md, lines 94-98; CHANGES-v5.2.md, lines 18-22 and the paragraph "W1 option B (D1 and S1-D1)".
- What it says: S1-D1: the W1 self-match is resolved by option B (the full negative list kept; a fingerprint-bound `negative_allowance`). S1-D3: specify configuration admission, native delegated execution, the classification of `C`, widening reviews, engine purity over the adapter companions, and control reporting (B1-B6).
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.RULE.2 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.RULE.4 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.DENY.5 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.CTRL.14 (confirmed by owner decision 1 (necessary for reliable verification)); OBL-3 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### Owner decisions R-D1, R-D3, R-D5 (on the v5.4 review and its addendum C1-C4)

- Key: `R-D labels`
- Where stated: DESIGN-v5.5.9.md, lines 58-64 ("stricter refusals, withdrawal integrity, execution identity, the authority configuration, durable evidence").
- What it says: R-D1: the stricter refusals; R-D3: execution identity; R-D5: durable evidence. The labels C3 and C4 are findings of the v5.4 review addendum, applied under these decisions; R6.OUT.14 cites C3 with R-D5 and R6.PROF.9 cites C4 with R-D1.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.OUT.14 (confirmed by owner decision 1 (necessary for reliable verification)); R6.OUT.15 (deferred (owner decision 1)); R6.PROF.9 (confirmed by owner decision 1 (necessary for scientifically valid retirement)); R6.REC.18 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.24 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.17 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.23 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.24 (confirmed by owner decision 1 (necessary for reliable verification))

### Owner decision A-D5 (durable evidence; the authority values A-D1 to A-D5)

- Key: `A-D labels`
- Where stated: DESIGN-v5.5.9.md, lines 69-75.
- What it says: A-D5: durable evidence.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.OUT.14 (confirmed by owner decision 1 (necessary for reliable verification))

### Owner's final decision D2 of 2026-11-23 (the three stricter refusal classes)

- Key: `v5.5.9 final D2`
- Where stated: DESIGN-v5.5.9.md, lines 44-46: "The three stricter refusal classes of sec. 6.1 are accepted, with the evidence that valid frozen-plan operations are not rejected".
- What it says: The tool refuses (i) a splice for the unselected variant, (ii) one splice covering two edits, (iii) chained edits. The final decisions D3 (the freeze ledger) and D4 (the authority record) of the same list are obsolete since v6.0 and no r6 requirement rests on them.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.PROF.9 (confirmed by owner decision 1 (necessary for scientifically valid retirement))

### v6.0e status quote at line 17 (E-003; the v6.0d editorial correction)

- Key: `v6.0e line 17`
- Where stated: quoted in DESIGN-v6.0e.md, lines 17-21, "no comment id held by this writer".
- What it says: Approve the bounded v6.0d editorial correction (the O-4 fix and the nits) and a focused delta review.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: no requirement

### v6.0e status quote at line 31 (E-004; the v6.0c correction)

- Key: `v6.0e line 31`
- Where stated: quoted in DESIGN-v6.0e.md, lines 31-41, "no comment id held by this writer".
- What it says: Restore the v5.5.9 pre-run pin check; verify executable dependencies before the tool runs; retain the consumer checks; do not reintroduce automated owner-authorization verification.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.REC.19 (confirmed by owner decision 1 (necessary for reliable verification))
- Note: #1169 comment 7130449822 quotes the owner's adoption, in the owner's words, of DESIGN-v6.0e.md at its exact SHA-256, whose text contains this quote; confirming the requirements keyed here re-confirms a settled decision (R1). The adoption of v6.0e is context and is not treated as authorizing any r6 requirement (F9 of the grouped presentation); r6's adoption, and for these requirements owner decision 1, is the authority.

### v6.0e status quote at line 54 (E-005; the v6.0b correction)

- Key: `v6.0e line 54`
- Where stated: quoted in DESIGN-v6.0e.md, lines 54-67, "no comment id held by this writer".
- What it says: The tool commit belongs to main's first-parent history; the workflow's executable dependencies and the import environment are covered by the integrity checks; the hashlib.py negative control.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.REC.18 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.19 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.20 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.21 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.22 (confirmed by owner decision 1 (necessary for reliable verification))
- Note: #1169 comment 7130449822 quotes the owner's adoption, in the owner's words, of DESIGN-v6.0e.md at its exact SHA-256, whose text contains this quote; confirming the requirements keyed here re-confirms a settled decision (R1). The adoption of v6.0e is context and is not treated as authorizing any r6 requirement (F9 of the grouped presentation); r6's adoption, and for these requirements owner decision 1, is the authority.

### v6.0e status quote at line 75 (E-006; the v6.0a correction)

- Key: `v6.0e line 75`
- Where stated: quoted in DESIGN-v6.0e.md, lines 75-87, "no comment id held by this writer".
- What it says: B-1 to B-3; the fixed meaning table for B-4; ls-remote failure handling and mismatched-identity negative tests; a later A1 plan-amendment requirement.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: no requirement

### v6.0e status quote at line 95 (E-008; owner decisions of 2026-11-24 on the reduced design)

- Key: `v6.0e line 95`
- Where stated: quoted in DESIGN-v6.0e.md, lines 95-127, "this writer holds no comment id for them".
- What it says: Remove automated owner-authorization verification; keep explicit owner authorization procedural; preserve every technical verification guarantee; "the tool verifies which exact plan was executed; the owner confirms that it was the approved plan."
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.STAT.4 (scope statement without a check of its own (owner decision 1)); R6.PUR.11 (confirmed by owner decision 1 (necessary for reliable verification))
- Note: #1169 comment 7130449822 quotes the owner's adoption of v6.0e, whose text contains this removal; its prose description of v6.0e is the session's. The adoption of v6.0e is context and is not treated as authorizing any r6 requirement (F9 of the grouped presentation). Confirming the requirements keyed here re-confirms a settled decision (R1).

### r4/r5 authorization quote at r5 line 7 (A-002)

- Key: `r5:7`
- Where stated: quoted in r5 (sha256 11a9077c...a653), line 7, with author and date and no comment id.
- What it says: Authorize the Stage A review and the bounded tool design limited to O-9 and the item 2 record interfaces; no implementation or Stage B.
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: no requirement
- Note: The companion instruction quoted in r5, "Accept V1 on the existing evidence and start the design", is a class (i) record: #1169 comment 7153270569.

### Owner decision S1-D3 (specify B1-B6: admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting)

- Key: `S1-D3`
- Where stated: DESIGN-v5.5.9.md, lines 94-98; CHANGES-v5.2.md, line 22 ("S1-D3: specify the fixes for B1-B6.") and sec. 2; v6.0e sec. 0.2 (inventory item E-034) maps B1-B6 to the v6.0e passages and controls that answer them.
- What it says: specify configuration admission, native delegated execution, the classification of `C`, widening reviews, engine purity over the adapter companions, and control reporting (B1-B6).
- Permits: nothing for r6.
- Does not permit: citing the design document's quotation or label as an owner record.
- Relied on by: R6.OUT.12 (pending owner confirmation for the adoption decision (S1-D3)); R6.REC.5 (pending owner confirmation for the adoption decision (S1-D3)); R6.REC.7 (confirmed by owner decision 1 (necessary for reliable verification)); R6.REC.13 (pending owner confirmation for the adoption decision (S1-D3)); R6.REC.16 (pending owner confirmation for the adoption decision (S1-D3)); R6.REC.17 (pending owner confirmation for the adoption decision (S1-D3)); R6.REC.24 (confirmed by owner decision 1 (necessary for reliable verification)); R6.DELEG.1 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.3 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.4 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.5 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.6 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.7 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.10 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.12 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.13 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.15 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.16 (pending owner confirmation for the adoption decision (S1-D3)); R6.DELEG.18 (pending owner confirmation for the adoption decision (S1-D3)); R6.GATE.5 (pending owner confirmation for the adoption decision (S1-D3)); R6.GATE.7 (pending owner confirmation for the adoption decision (S1-D3)); R6.GATE.8 (pending owner confirmation for the adoption decision (S1-D3)); R6.GATE.9 (pending owner confirmation for the adoption decision (S1-D3)); R6.GATE.15 (pending owner confirmation for the adoption decision (S1-D3)); R6.CTRL.4 (pending owner confirmation for the adoption decision (S1-D3)); R6.CTRL.5 (pending owner confirmation for the adoption decision (S1-D3)); R6.CTRL.14 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.20 (pending owner confirmation for the adoption decision (S1-D3)); R6.CTRL.23 (confirmed by owner decision 1 (necessary for reliable verification)); R6.CTRL.25 (pending owner confirmation for the adoption decision (S1-D3)); R6.PLAN.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.PLAN.6 (pending owner confirmation for the adoption decision (S1-D3)); R6.PLACE.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.PLACE.4 (pending owner confirmation for the adoption decision (S1-D3)); R6.TREE.1 (pending owner confirmation for the adoption decision (S1-D3)); R6.TREE.10 (pending owner confirmation for the adoption decision (S1-D3)); R6.TREE.18 (pending owner confirmation for the adoption decision (S1-D3)); R6.RDIR.13 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.1 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.3 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.4 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.5 (pending owner confirmation for the adoption decision (S1-D3)); R6.CORE.6 (pending owner confirmation for the adoption decision (S1-D3)); R6.CFG.1 (pending owner confirmation for the adoption decision (S1-D3)); R6.CFG.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.CFG.3 (pending owner confirmation for the adoption decision (S1-D3)); R6.CFG.8 (pending owner confirmation for the adoption decision (S1-D3)); R6.ADAPT.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.A1CFG.1 (pending owner confirmation for the adoption decision (S1-D3)); R6.A1CFG.2 (pending owner confirmation for the adoption decision (S1-D3)); R6.VALID.3 (pending owner confirmation for the adoption decision (S1-D3)); R6.REPRO.1 (pending owner confirmation for the adoption decision (S1-D3))
- Note: Identified under owner decision 5; marked "Pending owner confirmation for the adoption decision (S1-D3; see FRESH-AUTHORIZATION.md, sec. 3)." except where decision 1 confirmed the requirement.

***

## 4. Labels that are not owner decisions

- D1 to D8 of the Stage 1 review: review findings, applied by owner decision S1-D2 (class (iii)).
- B1 to B6 of the Stage 1 review: implementation defects, whose fixes owner decision S1-D3 (class (iii)) asked to be specified; not the splice boundary cases B1-B6 of v6.0e sec. 10.1 (E-1092 to E-1097) or the r5 findings B1-B6.
- C3 and C4: findings of the v5.4 review addendum, applied under the owner decisions R-D1 to R-D5 (class (iii)).
- OD-1 to OD-31, MC-*, VD-*, ME-* (DECISIONS.md), RD-1 to RD-35 (RESIDUAL.md), RE-1 to RE-38 (RESIDUAL-2.md): recommendations prepared by the coordinating session, approved by the owner as the basis for drafting r6 (class (i): #1169 comments 7160281751, 7160980912, 7162098696). The approval covers drafting; the content takes effect only by r6's adoption.
- OC-1 to OC-5: items 1 to 4 and 6 of the proposal quoted in #1169 comment 7163402499, authorized by the owner "as proposed" in the same comment (class (i)).
- R1 to R6 and N1 to N6: findings of the independent review recorded at #1169 comment 7166666428 (REVIEW-r6-round2.md), addressed under owner decision 5.
- E-*, V1-*, V2-*, A-*, RV-*: inventory and review items (provenance), not decisions.

***

## 5. Review records

- #1169 comment 7166666428 (2026-11-25T15:19:37Z) records the independent review of the second correction round, reviewer text verbatim (REVIEW-r6-round2.md). It is a review record, not an owner decision: "Independent review of A1 design r6 at `400e4b4fe5f3474b96ee4faa3c437e76e09db782`: reviewer text, verbatim."
