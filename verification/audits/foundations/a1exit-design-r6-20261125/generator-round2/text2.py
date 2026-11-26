"""Static prose and data for the second r6 correction round (F1-F8, F7, OCFIX).

Imported by correct2.py.  Every quotation of a GitHub comment listed in QUOTES is checked by correct2.py
against the comment body fetched read-only; every quotation of DESIGN-r6.md in FRESH-AUTHORIZATION.md is
extracted mechanically from the generated design, so no quotation in the outputs is typed by hand.
"""

# ---------------------------------------------------------------------------------------------------------
# Comments on #1169 read for this round (all fetched with GET; created_at from the API).
# ---------------------------------------------------------------------------------------------------------
COMMENTS = [
    '7093128173', '7099655517', '7121574479', '7130449822', '7153270569', '7158516152', '7158801838',
    '7159270333', '7160281751', '7160980912', '7162098696', '7163402499', '7164065815', '7164340996',
]

# (comment id, exact substring of its body)
QUOTES = {
    'Q-7093-HEAD': ('7093128173', 'Recorded by the coordinating session from the owner\'s direct instruction in this session.'),
    'Q-7093-LAND': ('7093128173', 'land the tool through its own reviewed pull request and a separate merge decision;'),
    'Q-7093-PREREG': ('7093128173', 'amend `PREREG.md` to specify the new tool and its exact verification commands, so that every mandatory check of sec. 11 passes as written; then independent review and a new freeze'),
    'Q-7093-EXC': ('7093128173', 'The execution-exception approach of c.7092885251 is superseded and will not be used.'),
    'Q-7093-TREES': ('7093128173', 'The amended plan distinguishes the immutable scientific base H, the current integration base on `main`, the candidate retirement tree and the final landing merge tree'),
    'Q-7099-HEAD': ('7099655517', 'Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time'),
    'Q-7099-V3': ('7099655517', 'On the v3 review\'s open points D1 to D4: adopt the reviewer\'s recommendations (the item-7 restatement is a plan amendment, with the literal check kept as a countercontrol; per unit stays true; preregistered indicators; reproduced counts; the writer, reviewer, owner, frozen configuration and verifier chain for records).'),
    'Q-7099-V5D1': ('7099655517', 'drop deny rules DR-1d and DR-2 from the active set, with their purpose and patterns kept in a rejected-candidate history; keep DR-3 with its real witness in AGENTS.md at the scientific base'),
    'Q-7099-V5D2': ('7099655517', 'widen the residual review profile `resid` as the review proposed'),
    'Q-7099-LIMIT': ('7099655517', 'The documented uncaught rephrasings are accepted as a coverage limitation. The tool must not claim complete semantic detection; the known missed forms are kept as limitations and regression controls.'),
    'Q-7121-HEAD': ('7121574479', 'Recorded by the coordinating session.'),
    'Q-7121-DI2': ('7121574479', 'DI-2 option A, narrow (lineage of a superseding record by `record_id`)'),
    'Q-7130-ADOPT': ('7130449822', 'Adopt DESIGN-v6.0e.md, exact SHA-256:'),
    'Q-7130-IMPL': ('7130449822', 'Authorize local implementation of v6.0e on the existing tool branch.'),
    'Q-7153-V1': ('7153270569', 'Accept V1 on the existing evidence and start the design'),
    'Q-7158516-OWN': ('7158516152', 'Recover exact requirements, evidence and owner decisions without reconstructing missing authorization from paraphrases.'),
    'Q-7158801-S1D2': ('7158801838', 'The change from 3 is correction D3 of the Stage 1 review, applied in CHANGES-v5.2 under owner decision S1-D2.'),
    'Q-7158801-NOREC': ('7158801838', 'decision labels S1, R-D and A-D; and the r4/r5 authorization quote at line 7.'),
    'Q-7159-PREP': ('7159270333', 'Authorize preparation of the consolidated, self-contained design r6 as proposed, including the inventory-first approach and the single authoritative machine-readable expectation architecture.'),
    'Q-7159-PRESERVE': ('7159270333', 'The consolidated design must preserve every authoritative requirement unless its supersession is explicitly authorized.'),
    'Q-7159-NO': ('7159270333', 'No design adoption, implementation, control-expectation changes, new exceptions, CI dispatch, merge or A1 retirement execution are authorized.'),
    'Q-7160281-OWN': ('7160281751', 'Approve the proposed authorization with qualifications Q1-Q5 as stated, including the refinements in your latest message.'),
    'Q-7160281-BASIS': ('7160281751', 'Approve the recommended decisions in DECISIONS.md at commit 4e9a1501 as the basis for drafting the consolidated r6 specification, subject to qualifications Q1-Q5 below.'),
    'Q-7160281-MC': ('7160281751', 'Approve the 20 mechanical corrections where they restore unambiguous approved requirements, the specification of corrections for the 12 verification defects, and the OD-31 identifier migration with complete historical traceability.'),
    'Q-7160281-Q5': ('7160281751', 'Q5. Adopt the proposed missing-evidence treatment, subject to preserving transferred requirements as explicit outstanding obligations.'),
    'Q-7160281-PRESERVE': ('7160281751', 'Preserve all existing safeguards unless their withdrawal is explicitly approved.'),
    'Q-7160980-OWN': ('7160980912', 'Approve the proposed authorization with Q6-Q10 as stated, including all refinements in your latest message.'),
    'Q-7160980-V4': ('7160980912', 'Preserve the proximity/similarity prohibition, defer adoption of the V4 reversal, and retain outstanding evidence obligations as named blockers.'),
    'Q-7160980-BASIS': ('7160980912', 'Approve the recommended resolutions of RD-1-RD-35 in RESIDUAL.md at commit c1244459 as the basis for completing the r6 draft, subject to Q6-Q10:'),
    'Q-7160980-Q10': ('7160980912', 'Q10: Preserve substantive safeguards, explicitly describe the V4 reversal and its consequences, and retain unavailable evidence and unexecuted required controls as outstanding obligations.'),
    'Q-7162-OWN': ('7162098696', 'Approve the proposed authorization with Q11-Q16 as stated, including the refinements in your latest message.'),
    'Q-7162-PARA': ('7162098696', 'Present all requirements supported only by paraphrased owner decisions for explicit confirmation or fresh authorization.'),
    'Q-7162-BASIS': ('7162098696', 'Approve the recommended resolutions of RE-1-RE-38 in RESIDUAL-2.md at commit f4e18558, using the revised Section E recommendations where they supersede the original entries, subject to Q11-Q16.'),
    'Q-7162-V4': ('7162098696', 'Keep V4, V27, V27-glossary and V15 deferred to an explicit adoption decision. Recover or freshly authorize any requirement supported only by paraphrased owner decisions; do not reconstruct historical authorization.'),
    'Q-7163-OWN': ('7163402499', 'Authorize the bounded specification correction as proposed, including both refinements in your latest message.'),
    'Q-7163-NO': ('7163402499', 'No governance-rule amendment, exception expansion, design adoption, implementation change, CI dispatch, merge or A1 retirement execution is authorized.'),
    'Q-7163-OC1': ('7163402499', '1. Resolve OBL-16 by specifying TR5 consistently with the §A.39 lifecycle: exact-candidate validation before F designation, designation identity verification, and durable evidence verification at landing. Do not require F to land prematurely.'),
    'Q-7163-OC2': ('7163402499', '2. Resolve OBL-26 by distinguishing specification adoption from certification of implementation conformance. Preserve §A.42\'s durable evidence requirements for every enduring claim. Report any remaining governance conflict explicitly.'),
    'Q-7163-OC3': ('7163402499', '3. For OBL-13, OBL-14, OBL-15 and OBL-23, specify which candidate evidence supports landing decisions and which reproducible evidence supports enduring claims. Investigate replacement controls using reachable pinned inputs where appropriate. Do not substitute byte equality for ancestry where ancestry is material.'),
    'Q-7163-OC4': ('7163402499', '4. Keep LC-7 REVIEW_REQUIRED pending an explicitly specified and independently reviewed regeneration verification procedure.'),
    'Q-7163-OC5': ('7163402499', '6. Keep the four V4-group expectations deferred.'),
    'Q-7163-PEND': ('7163402499', 'Present the 33 pending requirements grouped by underlying owner decision, with exact proposed wording, consequences and safeguards affected, together with any remaining contradictions.'),
    'Q-7164065-ERR': ('7164065815', 'The correction report lists the owner\'s decisions OC-1 to OC-5 as relayed without a comment id. That is incorrect: they are recorded verbatim in comment 7163402499.'),
    'Q-7164340-OWN': ('7164340996', 'A1 design r6: Proceed with the second correction round, addressing F1–F8 and the additional unmarked requirements. Preserve all existing safeguards and keep the V4 group deferred. Prepare the corrected design for independent review. This does not authorize adoption, freezing or execution.'),
}

# ---------------------------------------------------------------------------------------------------------
# Decision bases: classification under F1
# ---------------------------------------------------------------------------------------------------------
# Class (i): the owner's own words, quoted on GitHub.  Class (ii): a record written by the coordinating
# session of an owner decision, with no owner words.  Class (iii): no GitHub record.
CLASS_TEXT = {
    'i': "(i) owner's own words on GitHub",
    'ii': '(ii) session-written record on GitHub, no owner words',
    'iii': '(iii) no GitHub record',
}

# key used in REQUIREMENTS.json -> (class, heading, record, what it says, rule used to find requirements)
BASES = [
    ('V5-D1', 'ii', 'Owner decision V5-D1 (DR-1d and DR-2 dropped from the active deny set; DR-3 kept with its real witness)',
     ['Q-7099-HEAD', 'Q-7099-V5D1'],
     'DESIGN-v5.5.9.md (records-branch copy, blob e5b97ef1), lines 116-119; lines 120-122 state that the writer held no comment id.',
     "DR-1d and DR-2 are not in the active deny set; their patterns are kept as history; DR-3 is kept with the sentence of AGENTS.md at H, lines 37-39, as its witness. As a consequence the added texts of V4, V27 and V27-glossary PASS with no hit and V15 is REVIEW_REQUIRED only (the V4 reversal). The deferral of the V4 reversal rests on class (i) records: #1169 comments 7160980912 (Q10, RD-14), 7162098696 (RE-1), 7163402499 (item 6) and 7164340996.",
     'requirements whose Sources cite an inventory item that names V5-D1 (E-014, E-033, E-034, E-055, E-1001, E-1011, E-1016, E-1113, E-1114, E-1126, E-1364, E-1365, E-1366), and the requirements that state the deferred V4 decision; less R6.DENY.1 and R6.DENY.2, whose content does not depend on the decision (F4).',
     'The four expectation rows V4, V27, V27-glossary and V15 carry both candidate expectations, each "not authoritative; decided at r6 adoption" (RE-1). The row of sec. 33 that retires DR-1d and DR-2 ("obsolete: dropped deny candidates ...; never reused") also rests on V5-D1; it is a table row, not a requirement, and carries no mark.'),
    ('V5-D2', 'ii', 'Owner decision V5-D2 (the review profile `resid` widened)',
     ['Q-7099-HEAD', 'Q-7099-V5D2'],
     "DESIGN-v5.5.9.md, lines 118-119: \"V5-D2, widen `resid` as the v4 review's V8 proposes (sec. 6.6)\"; the inventory item E-1024 (v6.0e sec. 6.6) records the widening.",
     "`resid` is widened by the parts resid-b (\"finite set\"; a state-space noun followed by \"is finite\") and resid-c (\"substratum\", \"universe\" or \"world\" followed by \"is finite\"; \"finite number\" or \"finite count\"), as v6.0e sec. 6.6 states them. The W2 allow rules do not rest on V5-D2 or on any other owner decision: v6.0e sec. 6.5 presents them as seed rules \"for review; not adopted\".",
     'requirements whose Sources cite an inventory item that names V5-D2 (E-014, E-033, E-034, E-1024, E-1364), and R6.PUR.8, whose informative classes include resid-b and resid-c (F7).',
     None),
    ('v3 D1-D4', 'ii', "Owner decisions v3 D1-D4 (v3's open points 1-4: adopt the v3 review's recommendations)",
     ['Q-7099-HEAD', 'Q-7099-V3'],
     "DESIGN-v5.5.9.md, lines 114-115; DESIGN-v3.md sec. 15 states the open points.",
     "D1: the restatement of item 7 is a plan amendment, with the literal check kept as a countercontrol. D2: the context mapping as proposed, with `per unit` on the required side. D3 and D4: preregistered indicators, reproduced counts, and the writer, reviewer, owner, frozen configuration and verifier chain for records.",
     "requirements whose Sources cite an inventory item that names D1, D2, D3 or D4 in this sense (E-076, E-1283, E-1367), and R6.CTX.4 (`per unit` on the required side), whose content the paraphrase states (F7). Requirements citing D1-D8 of the Stage 1 review are keyed S1-D2 instead (F3).",
     None),
    ('S1-D2', 'iii', 'Owner decision S1-D2 (apply the Stage 1 review\'s design corrections D1-D8)',
     [],
     "DESIGN-v5.5.9.md, lines 94-98, and CHANGES-v5.2.md, lines 18-22 (\"S1-D2: apply D1-D8.\"). D1 to D8 are findings of the Stage 1 review (`review-stage1/review-stage1.md`), not owner decisions; CHANGES-v5.2.md sec. 1 re-derives each. #1169 comment 7158801838, a result comment written by the coordinating session, mentions S1-D2 in passing and is not a record of the decision.",
     "D1: W1-c's `negative_allowance` and the self-PASS lint; D2: SW2's expectation; D3: 7 HP structure REVIEWs; D4: the LF-inclusive site span (215 region lines); D5: RT-D's 45 `resid` lines; D6: per-splice `register` and `infinity` semantics with parity to P; D7: `rule-stale` scoping; D8: matching on source bytes.",
     'requirements whose Sources cite an inventory item that names D1 to D8 in the Stage 1 sense (E-039, E-046, E-090, E-111, E-115, E-133, E-134, E-163, E-1021, E-1062, E-1188, E-1234). R6.ANCH.14, R6.REC.14, R6.CTRL.19, R6.EVID.4, R6.EVID.5 and OBL-15 were keyed "D1-D4" (F3); R6.DENY.5 and OBL-3 were keyed "D1-D4" through E-1021, whose label "(S1-D1, D1)" is the Stage 1 D1 (F3); R6.RULE.7, R6.RULE.8, R6.RULE.9, R6.CTRL.24 and OBL-1 were unmarked (F7).',
     None),
    ('S1-D1 to S1-D3', 'iii', 'Owner decisions S1-D1 to S1-D3 (the Stage 1 review: W1 option B; apply D1-D8; specify B1-B6)',
     [],
     'DESIGN-v5.5.9.md, lines 94-98; CHANGES-v5.2.md, lines 18-22 and the paragraph "W1 option B (D1 and S1-D1)".',
     'S1-D1: the W1 self-match is resolved by option B (the full negative list kept; a fingerprint-bound `negative_allowance`). S1-D3: specify configuration admission, native delegated execution, the classification of `C`, widening reviews, engine purity over the adapter companions, and control reporting (B1-B6).',
     'requirements whose Sources cite an inventory item that names S1-D1, S1-D2 or S1-D3 (E-014, E-034, E-128, E-130, E-1021, E-1192, E-1364). S1-D3 underlies parts of secs. 11, 13 and 16, but no inventory item a requirement cites names it, so the rule marks none of those requirements (open item).',
     None),
    ('R-D labels', 'iii', 'Owner decisions R-D1, R-D3, R-D5 (on the v5.4 review and its addendum C1-C4)',
     [],
     'DESIGN-v5.5.9.md, lines 58-64 ("stricter refusals, withdrawal integrity, execution identity, the authority configuration, durable evidence").',
     'R-D1: the stricter refusals; R-D3: execution identity; R-D5: durable evidence. The labels C3 and C4 are findings of the v5.4 review addendum, applied under these decisions; R6.OUT.14 cites C3 with R-D5 and R6.PROF.9 cites C4 with R-D1.',
     'requirements whose Sources cite an inventory item that names R-D1, R-D3 or R-D5 (E-014, E-034, E-097, E-121, E-147), and the requirements whose Sources cite an item that names C3 or C4 (E-098, E-158, E-1218, E-1219, E-1243): R6.OUT.15, R6.REC.24, R6.CTRL.17, R6.CTRL.23 and R6.CTRL.24 (F7).',
     None),
    ('A-D labels', 'iii', 'Owner decision A-D5 (durable evidence; the authority values A-D1 to A-D5)',
     [],
     'DESIGN-v5.5.9.md, lines 69-75.',
     'A-D5: durable evidence.',
     'requirements whose Sources cite an inventory item that names A-D5 (E-014, E-034, E-097).',
     None),
    ('v5.5.9 final D2', 'iii', "Owner's final decision D2 of 2026-11-23 (the three stricter refusal classes)",
     [],
     'DESIGN-v5.5.9.md, lines 44-46: "The three stricter refusal classes of sec. 6.1 are accepted, with the evidence that valid frozen-plan operations are not rejected".',
     'The tool refuses (i) a splice for the unselected variant, (ii) one splice covering two edits, (iii) chained edits. The final decisions D3 (the freeze ledger) and D4 (the authority record) of the same list are obsolete since v6.0 and no r6 requirement rests on them.',
     'the requirement that states the three refusal classes, R6.PROF.9 (F3).',
     None),
    ('DI-2', 'ii', 'Owner decision DI-2, option A, narrow (lineage of a superseding record by `record_id`)',
     ['Q-7121-HEAD', 'Q-7121-DI2'],
     'DESIGN-v5.5.8.md and DESIGN-v5.5.9.md (adopted per the same comment).',
     'A superseding record shares its predecessor\'s kind, schema and `record_id`; the chain is valid, acyclic and single-headed.',
     'requirements whose Sources cite an inventory item that names DI-2 (E-141, E-1332 to E-1340): R6.REC.6, R6.REC.7 and R6.CTRL.22 (F7).',
     None),
    ('7093128173', 'ii', 'Owner decision recorded in #1169 comment 7093128173 (landing order; the exception-free route)',
     ['Q-7093-HEAD', 'Q-7093-EXC', 'Q-7093-LAND', 'Q-7093-PREREG', 'Q-7093-TREES'],
     'the comment itself (2026-11-23T06:13:50Z); paraphrased by the v2 review (RV-002).',
     'The tool lands first through its own reviewed pull request; PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written; the four trees are distinguished; the execution-exception route of comment 7092885251 is superseded. The comment quotes no owner words, so R6.STAT.8 can be confirmed only by the owner restating it (RE-26 option (b)).',
     'requirements that cite RV-002 or quote the comment.',
     'The landing order it states also fixes the gate order traced in sec. 32 of DESIGN-r6.md.'),
    ('v6.0e line 17', 'iii', 'v6.0e status quote at line 17 (E-003; the v6.0d editorial correction)',
     [], 'quoted in DESIGN-v6.0e.md, lines 17-21, "no comment id held by this writer".',
     'Approve the bounded v6.0d editorial correction (the O-4 fix and the nits) and a focused delta review.',
     'the mapping records the quote as history and locates no requirement that restates it.', None),
    ('v6.0e line 31', 'iii', 'v6.0e status quote at line 31 (E-004; the v6.0c correction)',
     [], 'quoted in DESIGN-v6.0e.md, lines 31-41, "no comment id held by this writer".',
     'Restore the v5.5.9 pre-run pin check; verify executable dependencies before the tool runs; retain the consumer checks; do not reintroduce automated owner-authorization verification.',
     "requirements whose Sources cite the items that the mapping says restate the quote's substance (E-151).", None),
    ('v6.0e line 54', 'iii', 'v6.0e status quote at line 54 (E-005; the v6.0b correction)',
     [], 'quoted in DESIGN-v6.0e.md, lines 54-67, "no comment id held by this writer".',
     "The tool commit belongs to main's first-parent history; the workflow's executable dependencies and the import environment are covered by the integrity checks; the hashlib.py negative control.",
     "requirements whose Sources cite the items that the mapping says restate the quote's substance (E-147 to E-155).", None),
    ('v6.0e line 75', 'iii', 'v6.0e status quote at line 75 (E-006; the v6.0a correction)',
     [], 'quoted in DESIGN-v6.0e.md, lines 75-87, "no comment id held by this writer".',
     'B-1 to B-3; the fixed meaning table for B-4; ls-remote failure handling and mismatched-identity negative tests; a later A1 plan-amendment requirement.',
     'the mapping records the quote as history and locates no requirement that restates it.', None),
    ('v6.0e line 95', 'iii', 'v6.0e status quote at line 95 (E-008; owner decisions of 2026-11-24 on the reduced design)',
     [], 'quoted in DESIGN-v6.0e.md, lines 95-127, "this writer holds no comment id for them".',
     'Remove automated owner-authorization verification; keep explicit owner authorization procedural; preserve every technical verification guarantee; "the tool verifies which exact plan was executed; the owner confirms that it was the approved plan."',
     "requirements whose Sources cite the items that the mapping says restate the quote's substance (E-010, E-012, E-057).",
     "#1169 comment 7130449822 quotes the owner's adoption of v6.0e, whose text contains this removal; its prose description of v6.0e is the session's. The adoption of v6.0e is context and is not treated as authorizing any r6 requirement (F9 of the grouped presentation)."),
    ('r5:7', 'iii', 'r4/r5 authorization quote at r5 line 7 (A-002)',
     [], 'quoted in r5 (sha256 11a9077c...a653), line 7, with author and date and no comment id.',
     'Authorize the Stage A review and the bounded tool design limited to O-9 and the item 2 record interfaces; no implementation or Stage B.',
     'the mapping records the quote as history; r6 takes its authority from its own adoption, and no requirement restates the quote.',
     'The companion instruction quoted in r5, "Accept V1 on the existing evidence and start the design", is a class (i) record: #1169 comment 7153270569.'),
]

# ---------------------------------------------------------------------------------------------------------
# Class (i) authorizations the design relies on, with what each permits and does not permit
# ---------------------------------------------------------------------------------------------------------
CLASS_I = [
    ('7130449822', '2026-11-24T11:42:47Z', 'adoption of design v6.0e', ['Q-7130-ADOPT', 'Q-7130-IMPL'],
     'v6.0e (sha256 4024a31c...5131) is the authoritative design until r6 is adopted; local implementation of v6.0e on the existing tool branch.',
     'Adoption of any r6 requirement: r6 names its own adoption as its authority (R6.STAT.1), and the later quoted instructions defer the V4 reversal although v6.0e expects V4 PASS. Push, CI execution and merge ("separately authorized actions").',
     'context for every requirement restated from v6.0e (the inventory items E-*).'),
    ('7153270569', '2026-11-25T04:54:22Z', 'start of the r5 design amendment', ['Q-7153-V1'],
     'starting the bounded design amendment for O-9 and the item-2 records after the Stage A review.',
     'any r6 requirement; implementation; Stage B.',
     'the provenance of r5 (A-items); r6 cites r5 as provenance only.'),
    ('7158516152', '2026-11-25T09:34:34Z', 'read-only design dependency and consistency assessment', ['Q-7158516-OWN'],
     'the read-only assessment and recording it on #1169.',
     'changes to the design, implementation, control expectations or exceptions; any commit, push or merge.',
     'the findings behind DECISIONS.md, including ME-5 and ME-6 (owner decisions without a record or recorded only in paraphrase).'),
    ('7159270333', '2026-11-25T10:08:02Z', 'preparation of the consolidated design r6', ['Q-7159-PREP', 'Q-7159-PRESERVE', 'Q-7159-NO'],
     'preparing r6, its inventories, mapping and proposed controls; committing and pushing the design documents to the design branch for exact-head independent review.',
     'design adoption, implementation, control-expectation changes, new exceptions, CI dispatch, merge, A1 retirement execution; the supersession of an authoritative requirement without explicit authorization.',
     'the r6 drafting as a whole (R6.STAT.1, R6.STAT.2).'),
    ('7160281751', '2026-11-25T10:52:11Z', 'DECISIONS.md (OD-1 to OD-31), Q1-Q5, the 20 mechanical corrections, the 12 verification defects, the missing-evidence treatment (ME-*), the OD-31 migration', ['Q-7160281-OWN', 'Q-7160281-BASIS', 'Q-7160281-MC', 'Q-7160281-Q5', 'Q-7160281-PRESERVE'],
     'drafting r6 on the basis of those recommended decisions and qualifications.',
     'adoption of r6 or of any decision as a requirement in force; implementation; control-expectation changes in the executable tool; exceptions; CI dispatch; merge; A1 retirement execution; the withdrawal of a safeguard that is not explicitly approved.',
     'the Sources labels OD-*, Q1-Q5, MC-*, VD-*, ME-*.'),
    ('7160980912', '2026-11-25T11:23:22Z', 'RD-1 to RD-35 with Q6-Q10; deferral of the V4 reversal', ['Q-7160980-OWN', 'Q-7160980-BASIS', 'Q-7160980-V4', 'Q-7160980-Q10'],
     'completing the r6 draft on the basis of those resolutions; stating the V4 reversal and its consequences for decision at r6 adoption.',
     'adoption of the V4 reversal ("defer adoption of the V4 reversal"); adoption of r6; implementation; CI dispatch; merge; exceptions; A1 retirement execution.',
     'the Sources labels RD-* and Q6-Q10; the deferral clauses of R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6 and R6.A1CFG.7.'),
    ('7162098696', '2026-11-25T12:14:08Z', 'RE-1 to RE-38 with Q11-Q16; V4 group deferred; paraphrased decisions to be presented', ['Q-7162-OWN', 'Q-7162-BASIS', 'Q-7162-V4', 'Q-7162-PARA'],
     'completing and regenerating the integrated r6 draft on the basis of those resolutions; presenting the requirements supported only by paraphrased owner decisions for explicit confirmation or fresh authorization.',
     'deciding the V4 group ("deferred to an explicit adoption decision"); reconstructing historical authorization; adoption; implementation; CI dispatch; merge; exceptions; A1 retirement execution.',
     'the Sources labels RE-* and Q11-Q16; the `candidate_expectations` and DEFERRED outcome of the four V4-group rows (RE-1); the marking of requirements as pending owner confirmation.'),
    ('7163402499', '2026-11-25T13:10:44Z', 'the bounded specification correction OC-1 to OC-5', ['Q-7163-OWN', 'Q-7163-OC1', 'Q-7163-OC2', 'Q-7163-OC3', 'Q-7163-OC4', 'Q-7163-OC5', 'Q-7163-PEND', 'Q-7163-NO'],
     'the corrections OC-1 to OC-5 (items 1 to 4 and 6 of the quoted proposal, which the owner authorized "as proposed"), regeneration of the affected documents, and the grouped presentation of the 33 pending requirements.',
     'a governance-rule amendment, exception expansion, design adoption, implementation change, CI dispatch, merge or A1 retirement execution.',
     'the Sources label OC-1 to OC-5 (R6.STAT.10, R6.EVID.8, OBL-13 to OBL-16, OBL-23, OBL-26, LC-7 and the adoption trace of sec. 32).'),
    ('7164340996', '2026-11-25T13:49:23Z', 'this correction round (F1-F8 and the unmarked requirements)', ['Q-7164340-OWN'],
     'correcting F1 to F8 of the grouped presentation and marking the additional unmarked requirements; preparing the corrected design for independent review.',
     'adoption, freezing or execution; changing the V4 group; weakening any existing safeguard.',
     'this round\'s edits (CORRECTION-REPORT.md).'),
]

# Pattern common to the class (i) records above (stated once in AUTHORIZATIONS.md)
CLASS_I_PATTERN = (
    'Each of these comments is posted from the `amaybaum` account by the coordinating session. Each '
    'contains a passage introduced as the owner decision and quoted; that passage is the owner\'s own '
    'words. Where the owner approves a proposal "as proposed" or "including the refinements", the '
    'proposal text (quoted in the comment as relayed from the owner\'s independent review) and the '
    'session\'s refinements are approved by reference to that quoted approval; the refinements themselves '
    'are the session\'s words. None of these authorizations adopts r6 or any requirement of it: each '
    'authorizes drafting, correction or presentation, and each excludes adoption.')

# ---------------------------------------------------------------------------------------------------------
# Per-requirement analysis for FRESH-AUTHORIZATION.md
# (purpose, if authorized, if not authorized, safeguards, earlier-design flag or None)
# ---------------------------------------------------------------------------------------------------------
NOT_AUTH_GENERIC = 'option (c) of PARAPHRASED-DECISIONS.md applies: the requirement, or the part that rests on the decision, is withdrawn or narrowed with its verification traced (R6.STAT.5)'

NOTES = {
 'R6.STAT.4': (
  'Fixes the boundary between technical verification and owner authorization: approvals are procedural, quoted in the relying record, and the tool neither reads nor checks them.',
  'The tool accepts a run on a plan commit `F` whose technical identity checks hold, whether or not the owner designated it; only the owner\'s procedural confirmation and the quoted record establish approval.',
  'r6 states no boundary for authorization; ' + NOT_AUTH_GENERIC + '. v6.0e (adopted, #1169 comment 7130449822) contains the same boundary, so withdrawal would need a replacement statement.',
  'Removes, relative to v5.5.9, the automated detection of an undesignated plan or an unapproved authority change; every technical identity check (R6.REC.18 to R6.REC.22) is kept.',
  'v5.5.9 (final decision D4) required automated verification of owner authorization through the authority record, versioned comment forms and numeric owner id 7273571; r6, like v6.0e, does not.'),
 'R6.STAT.8': (
  'Records the landing order of the exception-free route: the tool lands first, then PREREG.md is amended and re-frozen so that every mandatory check of sec. 11 passes as written, with the four trees distinguished.',
  'r6 records the route as the basis of its gate order (sec. 32); the steps it held stay governed by their own owner records.',
  'The gate order of sec. 32 loses its recorded basis and would need another; ' + NOT_AUTH_GENERIC + '.',
  'Preserves the absence of an execution exception and the requirement that the plan passes as written.',
  None),
 'R6.PUR.8': (
  'States the coverage limitation for lexically unanchored paraphrases: only the classes the pinned `resid` rule file or another review profile matches reach REVIEW_REQUIRED.',
  'Constructed paraphrases outside the pinned classes PASS; the tool claims no complete semantic detection; the classes are plan-record content frozen at `F` (OBL-3).',
  'The limitation is unstated, which would leave the tool\'s coverage claim undefined; ' + NOT_AUTH_GENERIC + '.',
  'Matches v6.0e sec. 1 and the limitation recorded in #1169 comment 7099655517. The REVIEW guarantee for the listed classes holds only once the reviewed `resid` record is frozen at `F`; resid-b and resid-c rest on V5-D2. None of the listed constructed examples matches the form of DR-1d or DR-2 (computed, V4-COMPARISON.md), so dropping those rules did not change their outcome; whether any other v4 rule caught them was not determined in this round.',
  None),
 'R6.PUR.9': (
  'States the deferred decision on the V4 reversal and its three consistent resolutions.',
  'The owner decides at r6 adoption among (a), (b1) and (b2); until then the four rows stay DEFERRED and do not count toward S13.',
  'The deferral and the option statement are lost; the four rows would have no stated decision procedure; ' + NOT_AUTH_GENERIC + '.',
  'Preserves the quoted deferral instructions; adds that a rejection needs a new rule identifier (F5) and that V15 needs a DR-1d-type rule (F6).',
  'Resolution (a) permits V4, V27 and V27-glossary to PASS and V15 to be REVIEW_REQUIRED, where v2\'s demonstration expected V4 FAIL and v4 expected V4 and V15 FAIL `deny-match` (DR-2, DR-1d). Deferred (V4-COMPARISON.md).'),
 'R6.PUR.11': (
  'Keeps approval outside the tool: no output, outcome, field or control states or implies approval or authorization.',
  'Outputs carry no approval vocabulary (B4-MEANING); admitted record directories are "admitted".',
  NOT_AUTH_GENERIC + '; B4-MEANING would lose its requirement.',
  'Prevents a technical result from being read as an authorization; it removes no technical check.',
  'Same removal as R6.STAT.4 relative to v5.5.9.'),
 'R6.ANCH.14': (
  'Fixes the boundary cases of splice overlap and site spans (the LF-inclusive span of Stage 1 D4).',
  'A splice starting at a site line\'s LF overlaps the site; the replacement region includes inserted lines (215 region lines rather than 203).',
  'The boundary cases are unspecified; the region count would not be determined; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than v4 (more regions attributed).',
  None),
 'R6.CTX.1': (
  'Preregisters the context rule at S0, per frozen s3 value and indicator, with its counts reported and never tuned.',
  'The mapping is fixed before any counts; T1\' counts cannot be used to adjust it.',
  'The context rule loses its preregistration requirement; ' + NOT_AUTH_GENERIC + '.',
  'Preserves preregistration (v3 D2).',
  None),
 'R6.CTX.4': (
  'Defines when context is required for meaning and fixes the s3-to-`meaning_context` mapping, with `per unit` on the required side.',
  'Sites with a `per unit` status require context (12 meaning-context failures rather than 8).',
  'The mapping, or the `per unit` reading, is undecided; narrowing `per unit` to false would remove 4 failures; ' + NOT_AUTH_GENERIC + '.',
  'Stricter reading kept (v3 D2: "per unit stays true").',
  None),
 'R6.CTX.12': (
  'Keeps the neighbour context for LIST and TABLE sites in addition to the structure contexts.',
  'A change of either context gives the result of R6.CTX.6.',
  'Only the structure contexts would apply to LIST and TABLE sites; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than D2\'s wording; the v4 review found it correct.',
  None),
 'R6.OUT.14': (
  'Requires acceptance to be recorded only by an owner-approved landing record on `main` that commits the deterministic compressed result, the admission snapshot and the reproducibility recipe.',
  'No result is accepted until it lands; a compressed blob whose uncompressed hash differs is refused (TR46); CI identifiers are provenance only.',
  'Durable evidence for tool results is unstated in r6, although AGENTS.md sec. A.42 items 1-2 and sec. A.50 item 1 still require its substance; ' + NOT_AUTH_GENERIC + '.',
  'Preserves v5.5\'s durable evidence; the clause "the tool does not read or check that quotation" is the same boundary as R6.STAT.4.',
  None),
 'R6.OUT.15': (
  'Specifies offline replay from git objects and the committed snapshot alone, re-applying the tool\'s verification rules to the recorded host records.',
  'A committed result can be re-established without the host; a replay is never acceptable as a new run.',
  'No offline replay is specified, so a committed result could be re-checked only by a new host run; ' + NOT_AUTH_GENERIC + '.',
  'Adds a check (TR45-opB); the snapshot\'s genuineness at capture stays host-attested.',
  None),
 'R6.PROF.9': (
  'States the three input classes the tool refuses beyond P, while recording P\'s per-edit items 5 and 6 results in every case.',
  'Unselected-variant splices, two-edit splices and chained edits are refused; no item-5 or item-6 verdict differs from P\'s.',
  'These inputs would not be refused; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than P.',
  None),
 'R6.RULE.2': (
  'Defines the allow-rule schema, including the fingerprint field `negative_allowance` (S1-D1 option B).',
  'A fingerprint may carry an exact per-literal allowance bound to one sentence.',
  'The schema has no allowance; W1-c\'s lines would FAIL `rule-negative-match`, contradicting RT-D, unless `finit` were dropped from the negative list; ' + NOT_AUTH_GENERIC + '.',
  'A narrowly bounded exception to the negative matcher; the alternative (dropping `finit` from the list) would weaken it for every sentence. The last sentence ("Owner approval is procedural") rests on the line-95 decision.',
  'v5.1 had no allowance, so W1-c\'s lines were FAIL `rule-negative-match`; option B permits one exact match per fingerprinted sentence.'),
 'R6.RULE.4': (
  'Fixes the order of allow-rule application, with deny taking precedence and the allowance bound to one fingerprint once per tree.',
  'A negative-literal match is tolerated only within one exact sentence\'s allowance at one location, once per tree; anything else FAILs.',
  'As for R6.RULE.2; ' + NOT_AUTH_GENERIC + '.',
  'As for R6.RULE.2; deny still overrides everything.',
  'As for R6.RULE.2.'),
 'R6.RULE.7': (
  'Matches negative literals case-insensitively and matches every rule literal on source bytes (Stage 1 D8).',
  'Literals cannot be evaded by case or by rendering differences.',
  'Case and rendering are unspecified; a context literal could be matched against rendered text; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.RULE.8': (
  'Scopes `rule-stale`: not evaluated on proper ancestors of `recorded_at`; always evaluated on the candidates and on `recorded_at`, with skipped rules listed (Stage 1 D7).',
  'A fingerprint missing on an ancestor of `recorded_at` raises no item; at `recorded_at` it is a lint failure.',
  'The scope of `rule-stale` is unspecified; ' + NOT_AUTH_GENERIC + '.',
  'Narrows where `rule-stale` is raised (proper ancestors are excluded); every candidate and `recorded_at` stay covered, and the skipped rules are reported.',
  'Narrows v2: DESIGN-v2.md sec. 3.3 (V2-028) makes `rule-stale` REVIEW_REQUIRED whenever "a rule\'s fingerprinted instance occurs nowhere in the tree", with no scope; r6, like v6.0e (E-134), does not raise it on proper ancestors of `recorded_at`, where the fingerprinted text had not yet been written.'),
 'R6.RULE.9': (
  'Forbids deleting text before testing: a classified hit\'s sentence is tested whole.',
  'Deny profiles and negative matchers see the whole sentence.',
  'Residual testing by deletion would be possible; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than v2\'s residual-test mutation.',
  None),
 'R6.REC.6': (
  'Lists the conditions under which a record fails lint with `record-invalid`.',
  'Records without an exact review, with self-review, incomplete verdicts or non-person reviewers FAIL.',
  'The record lint loses its failure conditions; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.REC.7': (
  'Specifies supersession and lineage of records by `record_id` (DI-2, option A, narrow).',
  'Chains to nonexistent records, kind or schema changes, cycles, ambiguous ancestry and reused ids FAIL `record-invalid`.',
  'Lineage is unspecified; superseding records could change kind or identity; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.REC.14': (
  'Requires each fingerprinted sentence to PASS its own rule and each allowance to equal the exact literal count (Stage 1 D1).',
  'A rule whose own sentence does not PASS, or whose allowance is inexact, is `record-invalid`.',
  'The lint would not catch a self-contradictory rule; ' + NOT_AUTH_GENERIC + '.',
  'New and stricter.',
  None),
 'R6.REC.18': (
  'Binds an acceptable result to the tool files, workflow and repository pinned by the configuration at `F`, with the tool commit on `main`.',
  'Runs from another repository or event, off `main`, or with unpinned or extra tool files are refused, by the tool and by the consumer.',
  'Execution identity is unspecified; ' + NOT_AUTH_GENERIC + '.',
  'Preserves v5.5.9\'s technical identity guarantees, pinned through the configuration at `F` rather than the authority record.',
  None),
 'R6.REC.19': (
  'Specifies the pre-run pin check that runs before any file of the checkout.',
  'The job ends before any tool code runs if a tool file is missing, extra or differs from its pin.',
  'An unverified file could execute before the tool\'s own checks; ' + NOT_AUTH_GENERIC + '.',
  'Preserves the v5.5.9 pre-run check restored in v6.0c.',
  None),
 'R6.REC.20': (
  'Requires an isolated interpreter with no `sys.path` entry inside the checkout before any import.',
  'A shadow module (for example hashlib.py) cannot execute; the refusal is ERROR `NOT_ISOLATED`.',
  'Import isolation is unspecified; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than v5.5.9 (control EI6). Records a known implementation defect (exit 65 with no class).',
  None),
 'R6.REC.21': (
  'Refuses unpinned workflow dependencies by a raw-text line rule.',
  'Workflows with unpinned `uses` or the listed YAML forms are refused.',
  'Workflow dependencies are unchecked; ' + NOT_AUTH_GENERIC + '.',
  'Stricter than v5.5.9.',
  None),
 'R6.REC.22': (
  'Lists the workflow content the review checks before the pin fixes it.',
  'Triggers, permissions, runners, environment, actions and run lines are reviewed against a fixed list.',
  'The workflow review has no fixed list; ' + NOT_AUTH_GENERIC + '.',
  'Preserved.',
  None),
 'R6.REC.24': (
  'Defines the admission object and its three modes; only `"chain"` is acceptable.',
  'Harness and replay results can never be written as acceptable results.',
  'The admission modes are unspecified; ' + NOT_AUTH_GENERIC + '.',
  'Preserved.',
  None),
 'R6.DENY.1': (
  'Makes the rule records (deny, plan allow, `resid`) plan records frozen at `F`; the tool\'s requirement is the rule mechanism.',
  'The tool runs whatever reviewed rule content is frozen at `F`; r6 states no rule content.',
  'The place of rule content would be undecided; ' + NOT_AUTH_GENERIC + '.',
  'Preserved: v6.0e left the rules "for independent review ... not adopted"; verification of rule content moves from the design to the review at `F`.',
  None),
 'R6.DENY.2': (
  'Runs the rule-mechanism controls on the rule files current at the commit under check, as pinned control inputs.',
  'A changed rule file forces the affected expectations to be re-established before the gate can hold.',
  'The controls\' rule inputs are unpinned; ' + NOT_AUTH_GENERIC + '.',
  'Preserved.',
  None),
 'R6.DENY.5': (
  'Transfers the rule content to the plan amendment as outstanding obligations (named blockers).',
  'The plan cannot reach the gated steps until the deny rules, the W1 and W2 allow rules and `resid` exist as reviewed records.',
  'The rule content would have no stated obligation; ' + NOT_AUTH_GENERIC + '.',
  'Adds a blocker; leaving out resid-b and resid-c (V5-D2) would weaken REVIEW coverage (V26); W1-c\'s allowance is the bounded exception of S1-D1; the W2 allow rules rest on no owner decision.',
  'W1-c\'s `negative_allowance` as for R6.RULE.2.'),
 'R6.DENY.6': (
  'States the accepted-residual question for V4 and V27 and its consequences, for decision at adoption.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.'),
 'R6.CTRL.7': (
  'Defines control-only inputs and fixes DR-3\'s witness as the sentence of AGENTS.md at `H`, lines 37-39.',
  'DR-3 is tested on a real sentence; the production scan is not widened; no historical text is constructed as a witness.',
  'DR-3 would have no real witness; ' + NOT_AUTH_GENERIC + '.',
  'Preserves v6.0e; rests on V5-D1\'s second limb.',
  None),
 'R6.CTRL.14': (
  'Fixes the rule controls (L, V, A, S, WB, N-W and lint) and the basis of V1-V3.',
  'The control set is fixed; the V4-group rows follow the separate decision.',
  'The rule controls are unlisted; ' + NOT_AUTH_GENERIC + '.',
  'Preserves v6.0e\'s controls.',
  None),
 'R6.CTRL.15': (
  'Describes the V4 reversal: what it permits and its consequence.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.'),
 'R6.CTRL.17': (
  'Splits dependent rows: RT-O9\'s own checks run independently of RT-L2; TR45-opC and EI14-dispatch are NOT RUN until their evidence exists; consumer halves are rows.',
  'No actual failure is hidden behind a dependent NOT RUN.',
  'Dependent clauses would be merged with independent checks; ' + NOT_AUTH_GENERIC + '.',
  'Preserved (Q6, Q14).',
  None),
 'R6.CTRL.19': (
  'Lists the real-tree controls and makes reproducible figures asserted counts.',
  'Figures become asserted counts; T1\'-bound figures are conditional (OBL-23).',
  'Figures would be informational; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.CTRL.22': (
  'Lists the record controls and requires emitted FAIL `record-invalid`, not only a lint problem.',
  'Record controls assert the emitted outcome.',
  'The record controls are unlisted; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.CTRL.23': (
  'Lists the delegation, output, admission, execution-identity and object-integrity controls.',
  'The control set is fixed.',
  'These controls are unlisted; ' + NOT_AUTH_GENERIC + '.',
  'Preserved.',
  None),
 'R6.CTRL.24': (
  'Lists the plan-mapping and per-edit controls; S11-56 tests the tool\'s side only, and parity with P is an obligation.',
  'The control set is fixed; parity stays outstanding (OBL-1).',
  'These controls are unlisted; ' + NOT_AUTH_GENERIC + '.',
  'Preserved.',
  None),
 'R6.PLAN.8': (
  'Maps item 7 as frozen to the literal check, kept as the countercontrol `item7-literal`, with a restatement of item 7 as a plan amendment.',
  'Item 7 as frozen FAILs at T1\' and at `X_rep`; passing needs a reviewed plan amendment.',
  'Item 7 would have either no mapping or the literal grep as the acceptance criterion, which no tree keeping W1\'s legitimate sentences can pass; ' + NOT_AUTH_GENERIC + '.',
  'The literal check survives as a countercontrol; acceptance moves to a reviewed amendment.',
  'Permits the plan to pass, after a reviewed amendment, with item 7\'s literal grep failing; v3\'s alternative was that the literal grep must stand.'),
 'R6.A1CFG.7': (
  'States acceptance criterion S13 for the configured engine.',
  'S13 counts every stated A1 control outcome except the four deferred V4-group rows until the decision.',
  'S13 is unstated; ' + NOT_AUTH_GENERIC + '.',
  'S13 is temporarily narrower than v6.0e\'s, which counted V4, V27 and V15.',
  None),
 'R6.EVID.4': (
  'Lists the acceptance references and the controls that establish them.',
  'The listed figures are gated through their controls.',
  'No figure is an acceptance reference; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
 'R6.EVID.5': (
  'Lists the historical measurements that are not acceptance references.',
  'These figures stop supporting acceptance and are provenance.',
  'Their standing is undefined; ' + NOT_AUTH_GENERIC + '.',
  'No protection is lost (under AGENTS.md sec. A.42 they could not support an enduring claim); the 4677-blob history search, which supported dropping DR-1d and DR-2, becomes provenance.',
  None),
 'OBL-1': (
  'Requires P-parity of `register` and `infinity` with P\'s frozen checker, recorded at `F`.',
  'The plan freeze and any trial claiming items 5 or 6 are blocked until the comparison is recorded.',
  'Parity would be unrequired; ' + NOT_AUTH_GENERIC + '.',
  'Adds a blocker.',
  None),
 'OBL-3': (
  'Makes the rule records obligations adopted at `F`.',
  'As for R6.DENY.5.',
  'As for R6.DENY.5.',
  'As for R6.DENY.5.',
  'As for R6.DENY.5.'),
 'OBL-6': (
  'Records the accepted residuals and the V4 reversal as an obligation discharged at r6 adoption and at `F`.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.',
  'As for R6.PUR.9.'),
 'OBL-15': (
  'Keeps RT-T NOT RUN until every reviewed record of the review load exists at `F`.',
  'Freezing at `F` and execution are blocked until every record exists.',
  'RT-T would have no release condition; ' + NOT_AUTH_GENERIC + '.',
  'Stricter.',
  None),
}

# ---------------------------------------------------------------------------------------------------------
# V4-COMPARISON.md data
# ---------------------------------------------------------------------------------------------------------
DR_PATTERNS = {
    'DR-1d': r"(?i)\b(?:structural|substratum(?:'s|’s)?)\s+(?:sixth|seventh)\s+(?:assumption|axiom|posit|premise|condition|property)\b",
    'DR-2': r"(?i)\b(?:sixth|seventh)\b[^.;]{0,40}\bstructural\s+(?:property|assumption|axiom|posit|premise|condition)\b[^.;]{0,80}\bfinit",
}
V_TEXTS = [
    ('V4', "the framework's sixth structural property, finiteness of the bijection"),
    ('V27', "The framework's sixth structural property is finiteness of the substratum"),
    ('V27-glossary', "**Background independence (A6).** The framework's sixth structural property is finiteness of the substratum: the substratum dynamics is covariant under spatially varying internal-index transformations"),
    ('V15', "the substratum's sixth axiom, finiteness"),
    ('PUR.8 example', 'the six posits of the substratum'),
    ('PUR.8 example', 'six assumptions about the substratum'),
    ('PUR.8 example', 'The posit ledger lists fourteen.'),
    ('PUR.8 example', 'the fourteen-item posit ledger'),
]

RESOLUTIONS = [
    ('(a) accept the reversal',
     {'V4': 'reversal adopted', 'V27': 'reversal adopted', 'V27-glossary': 'reversal adopted', 'V15': 'reversal adopted'},
     'none',
     'none',
     'the added texts of V4, V27 and V27-glossary PASS with no hit; that of V15 is REVIEW_REQUIRED through `resid` only, which holds once the reviewed `resid` record with resid-a is frozen at `F` (R6.PUR.8, OBL-3); detection of those forms rests on review outside the tool',
     'permits V4 PASS where v2\'s demonstration and v4 expected FAIL; permits V15 REVIEW_REQUIRED where v4 expected FAIL `deny-match` (DR-1d); equals v5.5.9 and v6.0e',
     'S13 counts the four rows with the "reversal adopted" candidates; R6.PUR.9\'s outstanding-evidence blocker is discharged by the decision text'),
    ('(b1) reject for the ordinal-property form only',
     {'V4': 'reversal rejected', 'V27': 'reversal rejected', 'V27-glossary': 'reversal rejected', 'V15': 'reversal adopted'},
     'one plan deny rule of the DR-2 form, adopted with the plan\'s rule records at `F` after independent review and reconciliation against N-W',
     'one new identifier, chosen with the plan amendment; never DR-2 (retired and never reused, sec. 33; AGENTS.md sec. A.30)',
     'V4, V27 and V27-glossary FAIL `deny-match`; V15 stays REVIEW_REQUIRED through `resid`',
     'restores v4\'s FAIL for V4 (and the former M-DR2 text, V27); keeps v6.0e\'s REVIEW for V15, where v4 expected FAIL',
     'S13 counts the four rows: three with "reversal rejected", V15 with its "reversal adopted" candidate (the candidate labels no longer describe the choice for V15 and are restated at the decision); OBL-3 gains the new rule'),
    ('(b2) reject for all four',
     {'V4': 'reversal rejected', 'V27': 'reversal rejected', 'V27-glossary': 'reversal rejected', 'V15': 'reversal rejected'},
     'as (b1), and a second plan deny rule of the DR-1d form, reviewed and reconciled in the same way',
     'two new identifiers; never DR-1d or DR-2 (both retired, sec. 33)',
     'all four FAIL `deny-match`',
     'restores v4\'s expectations for V4 and V15 (and V27 as v4\'s M-DR2 countercontrol)',
     'S13 counts the four rows with the "reversal rejected" candidates; OBL-3 gains two rules'),
]

# ---------------------------------------------------------------------------------------------------------
# Report prose
# ---------------------------------------------------------------------------------------------------------
FINDINGS = {
    'F1': 'Classify every cited decision as (i) the owner\'s own words on GitHub, (ii) a session-written record on GitHub without owner words, or (iii) no GitHub record; verified by reading the comments with GET requests.',
    'F2': 'Correct the description of V5-D2: it widens `resid`; the W2 allow rules rest on no owner decision.',
    'F3': 'Disambiguate the labels D1-D4 (three senses) and D1-D8; re-key the requirements that cite the Stage 1 review\'s corrections to S1-D2.',
    'F4': 'Unmark R6.DENY.1 and R6.DENY.2, whose content does not depend on V5-D1.',
    'F5': 'Record that a rejection of the V4 reversal needs a new rule identifier, since DR-2 is retired and never reused.',
    'F6': 'Record that V15\'s FAIL candidate needs a rule of the DR-1d form, so that three consistent resolutions exist; V4, V27, V27-glossary and V15 expectations unchanged.',
    'F7': 'Mark the unmarked requirements with their actual decision basis.',
    'F8': 'Formatting: a blank line before a requirement that directly follows the previous requirement\'s Sources line.',
    'OCFIX': 'Correct the statement that OC-1 to OC-5 lack a comment id: they are quoted in the owner\'s words in #1169 comment 7163402499.',
}

OPEN_ITEMS = [
    'Requirements pending owner confirmation or fresh authorization: see FRESH-AUTHORIZATION.md (each listed with its exact wording, purpose and consequences). None is adopted by this round.',
    'The V4 group (V4, V27, V27-glossary, V15): deferred; the three consistent resolutions are compared in V4-COMPARISON.md. Under resolution (b1) the per-row candidate labels ("reversal adopted" for V15) no longer describe the choice and are restated at the decision; the expectations themselves are unchanged.',
    'S1-D3 (specify B1-B6: admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting) underlies parts of secs. 11, 13 and 16, but no inventory item cited by a requirement names it, so the attribution rule marks none. Identifying those requirements needs a mapping not made in this round.',
    'The sec. 33 row retiring DR-1d and DR-2 rests on V5-D1 (class (ii)); it is a table row, not a requirement, and is unmarked. It is listed in FRESH-AUTHORIZATION.md.',
    'Every class (i) authorization relied on authorizes drafting, correction or presentation and excludes adoption (AUTHORIZATIONS.md); every r6 requirement, marked or not, takes effect only by r6\'s adoption.',
    'Off-main support of adoption (R6.STAT.10, sec. 32 adoption trace): unchanged by this round, except that the owner corrections OC-1 to OC-5 are now attributed to #1169 comment 7163402499; they, like the other owner records, remain support off `main` until quoted with author and time in a record on `main`.',
    'item11-T1p, the controls that still read T1\' or P, LC-7 (OC-4) and the implementation obligations of OC-3: unchanged and open, as stated in the previous correction report.',
]

CONTRADICTIONS = [
    'The grouped presentation (group C) traced the "D1-D4" mark of R6.DENY.5 and OBL-3 to v3 D1. The attribution rule finds it through E-1021, whose label "(S1-D1, D1)" is the Stage 1 review\'s D1 (W1-c\'s allowance and the self-PASS lint, CHANGES-v5.2.md sec. 1). This round re-keys both to S1-D2 (F3). Their content still relates to v3 D1 (an item-7 restatement as a plan amendment needs a reviewed deny set); that link is not a source citation and is not marked.',
    'The grouped presentation cites DESIGN-v5.5.9.md by line numbers (for example 45-54, 68-73, 108-111) that do not match the records-branch copy read here (blob e5b97ef1: 40-50, 58-64, 94-98). The content is the same; this round cites the copy\'s lines.',
    'Appendix H, HIST-4 stated that the route authority of #1169 comment 7093128173 and the decisions D1-D4, V5-D1 and V5-D2 have no GitHub record. They have session-written records (class (ii)); HIST-4 is corrected (F1). This changes Appendix H, which the previous round kept unchanged; sections 33 and 34 stay unchanged.',
    'v5.5.9 and the inventory use "D1-D4" for both v3\'s open points and the owner\'s final decisions, and "D1-D8" for the Stage 1 corrections; R6.NOTE.13 now states the three senses (F3).',
    'Completeness scan of the attribution rule: after this round, 15 unmarked requirements cite inventory items containing label-like tokens. Two are R6.DENY.1 and R6.DENY.2 (F4). In the other 13 the tokens are not decision labels: "C3" in RV-056 (R6.CTRL.2) is the v2 control C3, and "D2" to "D5" in the A-items (R6.CTRL.26, R6.CTRL.27, R6.TREE.7, R6.RDIR.1, R6.RDIR.4, R6.RDIR.5, R6.RDIR.10, R6.RDIR.11, R6.RDIR.12, R6.RDIR.13, R6.VALID.4, R6.REPRO.1) are r5\'s directory conditions, renamed DIR2-DIR5 (sec. 34). None is marked.',
    'The candidate label "reversal rejected (a plan rule record restored for this form, sec. 12)" on the four V4-group rows speaks of restoring a rule for the form; under F5 the rule takes a new identifier. The label is part of the rows, which this round keeps byte-identical; it is restated, with the V15 label under (b1), when the owner decides.',
]
