# r6: the 33 pending requirements, grouped by the owner decision they rest on

This is a read-only presentation. I wrote nothing to the repository, to git or to GitHub. I read the #1169 comments with GET requests only.

**Sources I used:**
- `out-final/DESIGN-r6.md`, which I cite by line number;
- `out-final/REQUIREMENTS.json`, field `pending_owner_confirmation`;
- `out-final/PARAPHRASED-DECISIONS.md`;
- `src/DESIGN-v6.0e.md`, which I cite as "v6.0e:line";
- `DESIGN-v5.5.9.md` from the records branch, section "Status and authority", which I cite as "v5.5.9:line";
- `DESIGN-v3.md`, `DESIGN-v4.md` and `CHANGES-v5.2.md` from the same records branch;
- the #1169 comments, fetched live (642 comments).

**What "the owner's own words" means below.** Every #1169 comment is posted from the `amaybaum` account. The comments that matter here open with "Recorded by the coordinating session". So the account name alone does not show that the words are the owner's. I count text as the owner's own words only where a comment quotes the owner explicitly.

***

## 0. Count check and findings that cut across groups

**The count is right.** Exactly 33 requirements carry the mark, in both the design file and REQUIREMENTS.json. All 33 are covered below, each quoted once in its main group and referred back to elsewhere. PARAPHRASED-DECISIONS.md's per-decision lists match the JSON keys exactly. Every marked requirement can be traced to a decision, but several are traced to the wrong one (F2 and F4).

**Findings the owner should see first:**

- **F1. Comment 7099655517 is a session-written record, not the owner's words.** It does record the substance of D1-D4, V5-D1 and V5-D2, but it quotes no owner text. Its opening: "Recorded by the coordinating session. Every decision below was made by the owner (`amaybaum`) on 2026-11-23 in the coordinating session and is recorded on GitHub here for the first time".
- Comment 7093128173 is the same kind of record: "Recorded by the coordinating session from the owner's direct instruction in this session."
- So no owner words exist on GitHub for V5-D1, V5-D2, D1-D4 or 7093128173.
- There are none at all, not even a paraphrase, for S1-D1 to S1-D3, R-D1/R-D3/R-D5, A-D5, the v6.0e status quotes (lines 17, 31, 54, 75, 95) or the r5 line 7 quote. I searched every comment for distinctive phrases from each quote and found none.
- **F2. V5-D2 is mis-stated in PARAPHRASED-DECISIONS.md.** That file describes V5-D2 as "the W2 allow rules replacing the first two RESIDUAL_ALLOW entries and the blanket (A1) strip".
- The records say otherwise. v5.5.9:117-120 reads "V5-D2, widen `resid` as the v4 review's V8 proposes (sec. 6.6)". Comment 7099655517 says "widen the residual review profile `resid` as the review proposed". Its inventory source, E-1024 (v6.0e:1787-1790), is the `resid` widening.
- The W2 allow rules come from v6.0e sec. 6.5, which presents them as seed rules "for review; not adopted". No owner decision stands behind them.
- **F3. The label "D1-D4" stands for three different things, and "D1-D8" for a fourth.**
- (i) The owner decisions on v3's open points 1-4 (v5.5.9:114-115; v4:19). This is the set 7099655517 paraphrases.
- (ii) The owner's "final decisions of 2026-11-23" D1-D4 (v5.5.9:45-54). D2 there is "The three stricter refusal classes of sec. 6.1 are accepted"; D3 is the freeze ledger and D4 the authority record, both obsolete since v6.0.
- (iii) The Stage 1 review's design corrections D1-D8. These are review findings, not owner decisions; the owner applied them through S1-D2, "apply D1-D8" (CHANGES-v5.2.md:18-22). v6.0e's mapping table names them "Stage 1 D1 … D8" (v6.0e:272-279).
- Six of the requirements r6 files under "D1-D4" actually cite set (iii): R6.ANCH.14, R6.REC.14, R6.CTRL.19, R6.EVID.4, R6.EVID.5 and OBL-15. Their decision is S1-D2, which has no record on GitHub at all, so their support is weaker than PARAPHRASED-DECISIONS.md says.
- R6.PROF.9 also rests on set (ii)'s D2, which is not marked.
- **F4. The attribution rule over-reaches.** The rule marks a requirement if any of its Sources names a decision label. R6.DENY.1 and R6.DENY.2 cite E-1001 only because that item mentions the retired DR-1d and DR-2. Their content (rule records are plan records; controls run on pinned rule inputs) does not depend on V5-D1.
- **F5. Option (b) for V4 collides with the retired identifiers.** R6.DENY.5 and the sec. 33 row "DR-1d, DR-2 | obsolete … never reused" (DESIGN-r6.md sec. 33) retire DR-2. R6.PUR.9 option (b) says "needs DR-2, or a successor rule", and R6.DENY.6 says "DR-2 or an equivalent". Restoring the rule under the id DR-2 would break sec. 33 and AGENTS.md sec. A.30 ("never reuse a retired ID"). A rejection therefore needs a new identifier.
- **F6. "One decision for all four rows" is not one binary choice.** A DR-2-type rule catches V4, V27 and V27-glossary but not V15, whose text DR-2 does not match. V15's FAIL candidate needs a DR-1d-type rule as well (see the table in group A). There are therefore three consistent outcomes, not two.
- **F7. Some requirements rest on a paraphrased or unrecorded decision but are not marked:**
- R6.CTX.4 (`per unit` stays on the required side): this is v3 D2, which 7099655517 records as "per unit stays true".
- R6.OUT.15 (offline replay, "(C3, F2)"), R6.REC.24 (admission snapshot, E-158 "(C3)"), R6.CTRL.17 (TR45) and R6.CTRL.23 (TR46 "sec. 5 (C3)"): these rest on C3/R-D5.
- R6.RULE.7 (D8, source-byte literals), R6.RULE.8 and R6.RULE.9 (D7, `rule-stale`), R6.CTRL.24 (D6; C4/R-D1 chained edits, S11-58j) and OBL-1 (D6): these rest on the Stage 1 corrections, that is, S1-D2.
- R6.REC.6, R6.REC.7 and R6.CTRL.22 (DI-2): PARAPHRASED-DECISIONS.md already lists DI-2 as "not on the owner's list". Comment 7121574479 records DI-2's adoption only in paraphrase.
- R6.PUR.8's informative classes "finite set", "substratum … is finite" and "finite number": these are resid-b and resid-c, which rest on V5-D2. PUR.8 is marked for V5-D1 only.
- The sec. 33 row retiring DR-1d and DR-2 is a table row, not a requirement id, but it rests on V5-D1.
- More broadly, S1-D3 ("specify … B1-B6": admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting) underlies much of r6's secs. 11, 13 and 16. None of those requirements is marked.
- **F8. Formatting defect.** DESIGN-r6.md has no blank line between R6.DENY.5's Sources line (line 1978) and `**R6.DENY.6**` (line 1979), so the two paragraphs merge when the Markdown is rendered.
- **F9. Context, not authorization.** The owner did adopt v6.0e in their own words: comment 7130449822 quotes "Adopt DESIGN-v6.0e.md, exact SHA-256: 4024a31c…5131". v6.0e's text contains most of these requirements, the V4 PASS expectation included. The owner's later quoted instructions then defer the V4 reversal:
- 7160980912: "defer adoption of the V4 reversal";
- 7162098696: "Keep V4, V27, V27-glossary and V15 deferred to an explicit adoption decision";
- 7163402499: "Keep the four V4-group expectations deferred".

As instructed, I do not treat the v6.0e adoption as authorizing any r6 requirement. r6's own adoption (ME-5) is the authority it claims.

***

## A. V5-D1, the V4 group (kept separately deferred)

**What the record shows:**
- v5.5.9:116-118: "V5-D1, drop DR-1d and DR-2 from the active deny set with a recorded history, and keep DR-3 with its real witness in `AGENTS.md` at `H` (sec. 6.4, 6.4.1)".
- v5.5.9:121-124: "All of these decisions … reached this writer through the coordinating session … This writer holds no comment id for them".
- On GitHub, paraphrase only (7099655517): "drop deny rules DR-1d and DR-2 from the active set, with their purpose and patterns kept in a rejected-candidate history; keep DR-3 with its real witness in AGENTS.md at the scientific base". The same comment also says "The documented uncaught rephrasings are accepted as a coverage limitation."
- There are no owner words for V5-D1. There are quoted owner words for deferring it (F9).

**The strictest earlier statement** is v4:1172 and v4:1185, where V4 and V15 expect FAIL `deny-match` through DR-2 and DR-1d. v2's demonstration (DESIGN-v2.md:429) also expects V4 to FAIL. v5.5.9 and v6.0e expect V4 and V27 to PASS and V15 to be REVIEW.

### The five requirements that state the deferred decision

**R6.PUR.9** (lines 255-275):
> **R6.PUR.9** For decision at adoption (not adopted by this draft): the residual for the deny rule
> DR-2. The two texts "the framework's sixth structural property, finiteness of the bijection" (control
> V4) and "The framework's sixth structural property is finiteness of the substratum" (control V27)
> match no deny rule once DR-2 is not in the active rule set, and PASS when added; the plan's original
> literal item 7 misses both. Whether the tool's expected outcome for these texts is PASS (an accepted
> residual) or FAIL (DR-2's expectation restored) is an owner decision at adoption (RD-14, Q10), with
> these options:
>
> - (a) confirm the accepted residual: V4 and V27 expect PASS, kept so that a change in their outcome
>   is visible;
> - (b) restore V4's FAIL expectation, which needs DR-2, or a successor rule, in the plan's active rule
>   set.
>
> The decision covers V4, V27, V27-glossary and V15 together, which rest on the same decision V5-D1
> (RE-1). Until it is made, each of the four rows carries both candidate expectations, each marked
> "not authoritative; decided at r6 adoption", and an `expect` of outcome DEFERRED; the gate reports
> `deferred-expectation` for each and never holds on it (R6.GATE.9). Outstanding evidence, a named
> blocker on adoption of this requirement: the owner decision V5-D1 that dropped DR-2 is recorded only
> in paraphrase (ME-6); its text is to be recorded by the owner.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-055, RE-1. Controls: V4, V27, V27-glossary, V15.

**R6.DENY.6** (lines 1979-1998):
> **R6.DENY.6** **Accepted residual: V4 and V27 (for decision at adoption; not adopted by this
> draft).** The question: with the deny rules DR-1, DR-3, DR-4 and DR-5 and the review profiles of the
> A1 configuration, the added text of control V4 ("the framework's sixth structural property, finiteness
> of the bijection") and of control V27 ("The framework's sixth structural property is finiteness of the
> substratum", added alone and as the edited glossary line) produce no hit of any review or deny profile.
> The expectation for both would then be PASS with zero hits, recorded as an accepted residual after the
> candidate rule DR-2, which caught V4, was not adopted. That decision (V5-D1) is recorded only in
> paraphrase. Consequences of confirming: an added sentence that asserts finiteness as an ordinal
> structural property of the bijection or substratum, in the forms of V4 and V27, passes the tool
> undetected; the original item 7 check also misses it; its detection rests on review outside the tool;
> V4 and V27 are kept as controls so that a change in their outcome is visible. Consequence of
> restoring: V4 (and V27) expect FAIL `deny-match`, which requires a plan rule record that catches them
> (DR-2 or an equivalent, plan content under R6.DENY.1, reviewed with the deny set), and the
> reconciliation of that rule against the negative examples. The owner decides at adoption between (a)
> confirming the PASS expectation knowingly and (b) restoring the FAIL expectation. Until then the
> expectations are deferred. The decision covers V4, V27, V27-glossary and V15 together (RE-1). Until it is made, each of the four
> rows carries both candidate expectations, each marked "not authoritative; decided at r6 adoption",
> and the gate reports `deferred-expectation` for it and never holds (sec. 16.5).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001, V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

**R6.CTRL.15** (lines 2896-2910):
> **R6.CTRL.15** V4 adds "the framework's sixth structural property, finiteness of the bijection" to
> the file of a W1 rule. Under the deny set without DR-2 the sentence produces no hit, so the run is
> PASS: this is the V4 reversal. What it permits: a reintroduction of the counted premise in the form
> "sixth structural property, finiteness of ..." passes the deny profiles and the residual profile
> unclassified by any FAIL, and the original item 7 misses it as well. Its consequence: the tool does
> not detect that form, and detection rests on review of the residual hits. The reversal rests on an
> owner decision recorded only in paraphrase. It is adopted or rejected by the owner at r6's adoption;
> approving this draft does not adopt it. Until that decision, V4, V27, V27-glossary and V15 each
> carry both candidate expectations, marked "not authoritative; decided at r6 adoption", and the gate
> reports `deferred-expectation` for each (RE-1). If the reversal is rejected, V4's expectation is FAIL `deny-match` and the deny set
> needs a rule matching that form, which is a plan-record change (sec. 12). V27 tests a sentence of the
> same form and rests on the same decision, as do V27-glossary and V15, whose candidates are
> REVIEW_REQUIRED `unclassified` and FAIL `deny-match`.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: V2-080, RE-1. Controls: V4, V27, V27-glossary, V15.

**OBL-6** (lines 4947-4959):
> **OBL-6** Accepted residuals and the V4 reversal. With DR-1d and DR-2 dropped, "the framework's sixth
> structural property, finiteness of the bijection" PASSes when added (control V4, whose expectation in
> v2's demonstration was FAIL); "the substratum's sixth axiom, finiteness" is REVIEW only (V15); "The
> framework's sixth structural property is finiteness of the substratum" PASSes (V27). Constructed forms
> outside `resid`'s classes PASS ("the six posits of the substratum", "six assumptions about the
> substratum", "The posit ledger lists fourteen.", "the fourteen-item posit ledger", and "$A_1$" joined to "$A_6$" by an en dash).
> Consequence of the reversal: an added sentence of V4's form reaches PASS without review. Gates: r6's
> adoption (the V4 reversal, adopted or rejected at that step); plan freeze `F` (acceptance of the residual
> forms or further rules, as rule records). Discharged by: the owner's recorded decision on the V4
> reversal at r6's adoption, and the reviewed rule records at `F`.
> The decision covers V4, V27, V27-glossary and V15 together (RE-1).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1365, E-1366, RD-14, Q10.

**R6.A1CFG.7** (lines 4631-4640):
> **R6.A1CFG.7** Acceptance criterion S13: the configured engine reproduces, item by item, every A1
> control outcome of sec. 17 that the expectation file states, including the record-directory controls
> RDIR-1 to RDIR-25 and RDIR-12b, RT-O9 (with its dependent clause as in OBL-14) and the item-2 controls
> I2-1 to I2-8. Rule outcomes (deny, allow, `resid`) are measured with the plan's rule files as pinned
> control inputs; the rules themselves are plan records adopted at `F` (sec. 12, OBL-3). The expected
> outcomes of V4, V27, V27-glossary and V15 are deferred until the owner's decision on the V4 reversal
> at r6's adoption (RE-1, OBL-6); until then they do not count toward S13.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1436, MC-13, OD-8, RD-14. Controls: GATE-18,
> V5, V15, V27, V7a, V7b, V7c, V23, V24, V25, V26, RT-I7, RT-I7A, RT-DR, RT-DR3W.

**Practical consequence as drafted.** The four rows have `expect` set to DEFERRED. The gate reports `deferred-expectation` and never holds on them. S13 leaves out those four outcomes.

**Effect on safeguards.**
- Deferring preserves the owner's quoted instructions to defer.
- S13 is temporarily narrower than v6.0e's S13 (E-1436), which counted V4, V27 and V15.
- The deferral clauses themselves rest on quoted owner instructions (7160980912 Q10 / RD-14 and 7162098696 RE-1). Only the premise "DR-2 is not in the active set" rests on paraphrase.

### What each candidate does to the four rows

The candidates come from EXPECTATIONS.json; both carry "not authoritative; decided at r6 adoption".

| Row | Candidate "reversal adopted" | Candidate "reversal rejected" | What the rejected candidate requires |
|---|---|---|---|
| V4 (`a1_controls.py:493`) | PASS, 0 hits for the review and deny profiles; `item7-literal` PASS | FAIL `deny-match`; `item7-literal` PASS | a plan rule of the DR-2 type, under a new id (F5) |
| V27 | PASS, 0 hits | FAIL `deny-match` | the same DR-2-type rule |
| V27-glossary (glossary.md:13 at H, with "The sixth of the framework's structural assumptions A1–A6" replaced by the V27 text) | PASS, 0 hits | FAIL `deny-match` | the same DR-2-type rule |
| V15 | REVIEW_REQUIRED `unclassified`, all hits `resid`, `resid` key resid-a | FAIL `deny-match` | a DR-1d-type rule; DR-2 does not match V15 (F6) |

### How A1 restatements would come out under each candidate

I ran this probe myself. It applies the v6.0e patterns only: DR-1a/b/c, DR-3, DR-4 and DR-5 from sec. 6.4, DR-1d and DR-2 from sec. 6.4.1, and resid-a/b/c from sec. 6.6. It does not apply the other review profiles (count-grep, ptr, repo), so those could add REVIEW hits. The tool itself measured the four control rows (v6.0e:1722-1737). The x-rows are strings I constructed to illustrate the boundaries.

| Text | Current set (reversal adopted) | + DR-2 successor | + DR-2 and DR-1d successors |
|---|---|---|---|
| V4 "the framework's sixth structural property, finiteness of the bijection" | PASS | FAIL | FAIL |
| V27 "The framework's sixth structural property is finiteness of the substratum" | PASS | FAIL | FAIL |
| V15 "the substratum's sixth axiom, finiteness" | REVIEW (resid-a) | REVIEW (resid-a) | FAIL (DR-1d) |
| x "The seventh structural property is finiteness of the substratum" | PASS | FAIL | FAIL |
| x "its sixth structural property, total finiteness" | PASS | FAIL | FAIL |
| x "the framework's sixth structural property is that the state space is finite" | REVIEW (resid-a) | FAIL | FAIL |
| x "The substratum's sixth property is finiteness" | PASS | PASS | FAIL |
| x "the structural sixth premise, finiteness" | REVIEW (resid-a) | REVIEW | FAIL |
| x "finiteness is the framework's sixth structural property" (finiteness before the ordinal) | PASS | PASS | PASS |
| x "the sixth property of the substratum is finiteness" | PASS | PASS | PASS |
| x "the framework's sixth structural assumption is finiteness" | FAIL (DR-1a) | FAIL | FAIL |
| x "finiteness, the sixth structural property of the substratum" | FAIL (DR-1b) | FAIL | FAIL |
| legitimate W1 form "the six structural properties of the bijection" | PASS | PASS | PASS (both rules need "sixth" or "seventh") |

v6.0e reports measured costs at v6.0e:1716-1737:
- Neither DR-1d nor DR-2 matches any line of any tree at E, H, W or T1', or any of the 4677 historical corpus blobs.
- The distinct deny-line counts at E, H and W are the same with or without them (95, 86, 86).
- Restoring them therefore changes outcomes for constructed strings only. It needs reconciliation against N-W (every W1 and W2 line, and Main.md:738) and an independent review of the deny set (OBL-3).

### Proposed decision texts (the owner chooses one at r6's adoption)

- **(a) Accept:** "I confirm that the A1 plan's active deny set does not contain the DR-1d and DR-2 forms, and I accept knowingly that the added texts of V4, V27 and V27-glossary PASS with no hit and that of V15 is REVIEW_REQUIRED only, with detection of those forms resting on review outside the tool."
- **(b1) Reject for V4, V27 and V27-glossary only:** "I reject the V4 reversal for the ordinal-property form: the amended plan's rule records at `F` include an independently reviewed deny rule, under a new identifier, that makes V4, V27 and V27-glossary FAIL `deny-match`, while V15 stays REVIEW_REQUIRED through `resid`."
- **(b2) Reject for all four:** as (b1), "and a second new deny rule of the DR-1d form, so that V15 also FAILs `deny-match`."

R6.PUR.9, R6.DENY.6, R6.CTRL.15, OBL-6 and R6.A1CFG.7 then need these edits:
- name the new identifier rather than "DR-2" (F5);
- state V15's outcome under the option chosen (F6);
- R6.PUR.9's sentence "Outstanding evidence … recorded only in paraphrase" is discharged by the decision text itself, whichever option is chosen.

***

## B. V5-D1, the other parts (DR-3's witness, retired identifiers, the rule mechanism)

The record is the same as in group A.

**R6.PUR.8** (lines 230-253):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-055. Controls: V15, V21, V26.

- **Consequence.** Constructed paraphrases outside the pinned classes PASS. The tool claims no complete semantic detection.
- **Safeguard.** Coverage equals v6.0e sec. 1 and the limitation 7099655517 accepted. One thing changes: the classes become plan-record content (OBL-3) rather than design content, so the REVIEW guarantee exists only once the reviewed `resid` record is frozen at `F`.
- **Action.** Confirm or freshly authorize: "I accept as a coverage limitation that lexically unanchored paraphrases outside the classes the plan's pinned rule files match PASS the tool, and that their detection rests on independent review of the exact head." Also add the V5-D2 key (F7).

**R6.DENY.1** (lines 1939-1946):
> **R6.DENY.1** **Rule records are plan records.** The deny rules, the allow rules for the plan's own
> cases, and the review-profile rule `resid` that a configuration uses are rule records of the plan, in
> the schemas of sec. 10. They are frozen and adopted with the amended plan at `F`, after independent
> review, and referenced by the configuration at `F`. The tool's requirement is the rule mechanism:
> sec. 9 (profiles), sec. 10 (schema, application, lint), sec. 11 (records) and sec. 14 (hit
> classification). r6 states no rule content.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001, V2-059, V2-060, V2-061, RV-049. Controls: RT-DR, RT-D, RT-D-gr58, L1, L2.

**R6.DENY.2** (lines 1948-1955):
> **R6.DENY.2** **Controls on pinned rule inputs.** The controls of the rule mechanism use the rule
> files current at the commit under check as pinned control inputs, named with their blobs in the
> expectation file (sec. 16). Acceptance of the mechanism (sec. 18) is its behaviour on those inputs. A
> changed rule file is a changed control input: the affected expectations are re-established in the
> expectation file before the gate can hold.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001. Controls: V1, V2, V3, V5, V6, V9, V10, V11, V12, V13, V14, V16, V17, V18, V19, V20,
> V22, N-W, RT-DR3W.

- **Consequence.** The tool accepts any rule content frozen at `F`. The controls test the mechanism, and a changed rule file forces the expectations to be re-established.
- **Safeguard.** Preserved: v6.0e:1613-1620 also left the rules "for independent review … not adopted". Where the rule content is verified moves from the design to the review at `F`.
- **Action.** Neither depends on V5-D1 (F4). Recommend fresh authorization through r6's adoption, and drop the V5-D1 mark: "Deny rules, plan allow rules and the `resid` profile are plan records reviewed and frozen with the amended plan at `F`; the tool's requirement is the rule mechanism, tested on pinned rule files."

**R6.CTRL.7** (lines 2828-2836):
> **R6.CTRL.7** A control-only input is a pinned object (commit, path, git blob id and sha256) named by
> one control in the controls file. It is read only by the control that names it, changes no profile's
> scope and no production result, and adding or changing one changes the controls file and is reviewed
> with it. No historical text is constructed for this purpose. DR-3's witness is such an input: the
> sentence of `AGENTS.md` at `H`, lines 37-39 (blob 12a9281fb88c14395b6715a3bf4b4f6b030f433c, sha256
> d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27), which RT-DR3W scans at `H` and,
> as its countercontrol, at T1'.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1011, E-1013, E-1014, E-1015. Controls: RT-DR3W.

- **Consequence.** DR-3 is tested on a real sentence, not a constructed mutant. The production scan is not widened.
- **Safeguard.** Preserves v6.0e:1657-1677 exactly. This rests on V5-D1's second limb ("keep DR-3 with its real witness").
- **Action.** Confirm: "DR-3 is kept with its witness the sentence of `AGENTS.md` at `H`, lines 37-39, read only as a pinned control-only input by RT-DR3W, and no historical text is constructed as a rule witness."

**R6.CTRL.14** (lines 2886-2894; the Sources and Controls lists are abbreviated here and given in full at lines 2893-2894):
> **R6.CTRL.14** The rule controls are L1-L4, V1-V27 (V7a, V7b, V7c; no V8), A1r-A12r, S1r, S2r,
> WB1-WB15, N-W, their engine analogues and the rule-lint controls. v2's class `rule-invalid` is
> `record-invalid` (exit 20) throughout. V2 FAILs by DR-3 and V3 by DR-4; v2's fingerprint-mismatch and
> residual-test basis for them is superseded, since no rule deletes text and overlap is strict (sec.
> 10). V1 FAILs by DR-1, alternative b. The deny rules and the seed allow rules are plan records adopted
> with the amended plan; the controls use the current rule files as pinned control inputs and test the
> rule mechanism (sec. 12).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1106 … E-1232, V2-074 … V2-089, RV-050, RV-052 [78 items]. Controls: A1r … rule-negative [79 ids, including V4, V15, V27, V27-glossary, WB1-WB15].

- **Consequence.** The control set is fixed. It rests on V5-D1 only through the deferred V4-group rows, and on S1-D1 through WB1-WB15 (group F).
- **Safeguard.** Preserves v6.0e's controls.
- **Action.** Fresh authorization through r6's adoption, with the V4-group rows governed by group A's decision.

***

## C. One requirement pair resting on four decisions: rule content as plan obligations

The decisions are V5-D1 (DR-1d and DR-2 retired), V5-D2 (`resid` widened, which gives resid-b and resid-c), S1-D1 (W1-c's allowance) and v3 D1 (an item-7 restatement is a plan amendment needing a reviewed deny set). For V5-D2, see F2: the PARAPHRASED-DECISIONS.md text for it is wrong.

**R6.DENY.5** (lines 1969-1978):
> **R6.DENY.5** **Outstanding rule content.** The content of the plan's rule records is transferred to
> the plan amendment as outstanding obligations, each a named blocker on the execution it gates (sec.
> 32): the deny rules DR-1, DR-3, DR-4 and DR-5 with their definitions and patterns (the identifiers
> DR-1d and DR-2 are retired, sec. 33, and never reused); the W1 allow rules, including W1-c's
> fingerprints and its `negative_allowance`; the W2 allow rules, replacing P's corresponding
> `RESIDUAL_ALLOW` and `EXPLAINED` entries and its blanket `(A1)` strip; and the `resid` pattern with its
> parts resid-a, resid-b and resid-c.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1001, E-1002, E-1003, E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025,
> E-1026, E-1027, E-1032. Controls: none (OBL-3).

**OBL-3** (lines 4923-4930):
> **OBL-3** Rule records adopted at `F`. The deny rules DR-1 (alternatives a, b, c), DR-3, DR-4 and
> DR-5; the review profile `resid` (resid-a, resid-b, resid-c); the W1 allow rules with W1-c's
> `negative_allowance: {"finit": 1}`; the W2 allow rules replacing the first two `RESIDUAL_ALLOW`
> entries, their `EXPLAINED` substring entries and the blanket `(A1)` strip; and the converted
> `EXPLAINED` entries are plan records. Each is independently reviewed and adopted with the amended
> plan at `F`. Until then the controls use the current rule files as pinned control inputs. Gates: plan
> freeze `F`. Discharged by: the reviewed rule records frozen at `F`. Pending owner confirmation (see PARAPHRASED-DECISIONS.md). Sources: E-1001, E-1002, E-1003,
> E-1004, E-1005, E-1006, E-1020, E-1021, E-1022, E-1024, E-1025, E-1026, E-1027, OD-8.

- **Consequence.** The plan cannot be frozen at `F` until these records exist and have been reviewed. The tool runs whatever content is frozen.
- **Safeguard.** Preserves the v6.0e content and adds a blocker at `F`. Leaving out resid-b and resid-c (if V5-D2 were withdrawn) would weaken REVIEW coverage (V26). W1-c's allowance is the exception bounded by S1-D1 (group F).
- **Action.** Fresh authorization: "The amended A1 plan carries, as independently reviewed rule records frozen at `F`, deny rules DR-1 (a, b, c), DR-3, DR-4 and DR-5, the `resid` profile with resid-a, resid-b and resid-c, the W1 allow rules with W1-c's `negative_allowance: {"finit": 1}`, and the W2 allow rules replacing P's first two `RESIDUAL_ALLOW` entries, their `EXPLAINED` entries and the blanket `(A1)` strip; the V4-group rules are decided separately."
- Move the retirement clause "(DR-1d and DR-2 … never reused)" under group A's decision (F5).
- Correct V5-D2's description in PARAPHRASED-DECISIONS.md (F2).

***

## D. The owner decisions D1-D4 on v3's open points (set (i))

**What the record shows:**
- v5.5.9:114-115: "Owner decisions of 2026-11-23 on v3's open points 1-4 (D1-D4 below): adopt the v3 review's recommendations."
- Paraphrase on GitHub (7099655517): "On the v3 review's open points D1 to D4: adopt the reviewer's recommendations (the item-7 restatement is a plan amendment, with the literal check kept as a countercontrol; per unit stays true; preregistered indicators; reproduced counts; the writer, reviewer, owner, frozen configuration and verifier chain for records)."
- No owner words exist. The open points themselves are at DESIGN-v3.md:1034-1048.

**R6.PLAN.8** (lines 3624-3633; v3 D1):
> **R6.PLAN.8** Item 7 (a corpus grep for `\bA1\b` and related terms with only ledger false positives,
> and zero posit counts "Fourteen", "six structural" and "sixth of") maps, as frozen, to `terms --commit
> X --profile item7-literal`. The literal check is kept as the named countercontrol `item7-literal`, with
> RT-I7. Item 7 as frozen does not pass at T1': seven lines contain the legitimate count of the
> bijection's properties (W1); the T1' counts are historical measurements. Countercontrol: the H-form
> "Fourteen items" reinstated, which must FAIL in both the literal check and DR-5 (S11-7). DR-5 is a plan
> record. RT-I7A runs the proposed amendment check of R6.PLAN.18 at `H` and at T1' as a test of the
> mechanism.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1275, E-1283. Controls: S11-7, RT-I7, RT-I7A.

- **Consequence.** Item 7 as frozen FAILs at T1'. It survives as a countercontrol, and passing needs a plan amendment.
- **Safeguard.** The literal check is preserved as a countercontrol. Acceptance moves from the literal grep to a reviewed amendment. v3's alternative ("the literal grep must stand") would make the plan unpassable.
- **Action.** Confirm: "Item 7 as frozen is kept only as the countercontrol `item7-literal` with RT-I7, and any restatement of item 7 is a plan amendment frozen with its reviewed rule records at `F`."

**R6.CTX.1** (lines 737-741; v3 D2):
> **R6.CTX.1** Preregistration. The context rule was decided at S0, before any implementation output. It
> is stated per frozen s3 value and per indicator. Its authority is r6's adoption. Its counts at `T1'`
> are reported, never tuned.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-076. Controls: none (definition).

**R6.CTX.12** (lines 850-853; v3 D2, the stricter reading in v6.0e sec. 15 item 4):
> **R6.CTX.12** For LIST and TABLE sites the neighbour context of R6.CTX.2 is kept in addition to the
> structure contexts of R6.CTX.11: a change of either gives the result of R6.CTX.6.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1367. Controls: K7.

- **Consequence.** The context mapping is fixed before any counts. LIST and TABLE sites fail on either kind of context change.
- **Safeguard.** Preserved. CTX.12 is stricter than D2's wording (v6.0e:2780-2782), and the v4 review found it correct.
- **Action.** Confirm: "The context rule is the one preregistered at S0, per frozen s3 value and indicator, with `per unit` on the required side and its T1' counts reported, never tuned; for LIST and TABLE sites the neighbour context is kept in addition to the structure contexts." This also covers the unmarked R6.CTX.4 (F7).

***

## E. Requirements r6 files under "D1-D4" that rest on the Stage 1 corrections (set (iii), under S1-D2)

**What the record shows.** CHANGES-v5.2.md:18-22 reads "S1-D1: W1, option B. S1-D2: apply D1-D8. S1-D3: specify the fixes for B1-B6." The D items are the review's corrections, and each is re-derived in CHANGES-v5.2.md:36-43. No record exists on GitHub (ME-5). The citations:
- E-111 "(v1 sec. 4.3; D4)" is Stage 1 D4, the LF-inclusive span.
- E-163 "(D1)" is Stage 1 D1, the self-PASS lint.
- E-1188 "(D2)" is Stage 1 D2, the SW2 expectation.
- E-039, E-046, E-090 and E-1062 are Stage 1 D3, D4 and D5.

**R6.ANCH.14** (lines 535-548):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-110, E-111. Controls: B1, B2, B3, B4, B6.

**Consequence and safeguard.** With the LF-inclusive span, a splice starting at the LF overlaps the site (203 region lines become 215). This is stricter than v4.

**R6.REC.14** (lines 1715-1723):
> **R6.REC.14** **Examples and fingerprints.** Each fingerprint must be reproduced by a sentence of its
> named file at `recorded_at`. Each example and countercontrol must behave as stated. Every fingerprinted
> sentence, read at `recorded_at` in its named file, must be classified PASS by its own rule through
> steps 1-6 of R6.RULE.4, with its own allowance. Every `negative_allowance` must equal, literal by
> literal, the number of matches of that negative literal in its fingerprinted sentence, and may name
> only literals of the rule's negative matcher. A rule's positive examples include each fingerprinted
> sentence in full, not a fragment of it. Otherwise the record fails the lint (FAIL `record-invalid`).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-163. Controls: A6r, A8r, A9r, A11r, WB10, WB11.

**Consequence and safeguard.** A rule whose own sentence does not PASS, or whose allowance is inexact, is `record-invalid`. This is new and stricter (it closes v5.1's self-contradiction).

**R6.CTRL.19** (lines 2939-2952; the Sources and Controls lists are abbreviated here and given in full at lines 2951-2952):
> **R6.CTRL.19** The real-tree controls run in CI on real objects: RT-A, RT-E, RT-H0, RT-T0, RT-T, RT-C,
> RT-D, RT-D-gr58, RT-DR, RT-DR3W, RT-I7, RT-I7A, SW1, SW2, item11-T1p, N-W, RT-M, RT-SHIFT, RT-X, RT-L,
> RT-L2, RT-O9 and RT-O9-L2. v1's `verify-record` is `record` and `check-coverage` is `coverage`. Every
> figure a runner asserts today that is reproducible from inputs on `main` (among them RT-H0's 113/7/7,
> RT-A's and RT-E's 697, the RT-DR counts at `H`, RT-T0's site and region counts, RT-I7's split at `H`,
> RT-I7A and RT-C, and RT-D's 45 `resid` lines) is an asserted count in the expectation file, not an
> informational figure. A figure measured on T1' is an acceptance reference only for a run that has
> T1' among its inputs; its standing as evidence follows sec. 31. RT-C is PASS only with contract
> evidence; without it the expected result is the one the expectation file states for missing
> evidence. RT-T is NOT RUN until every reviewed record of sec. 14 exists. The two `not determined`
> H..T1' cases of sec. 6 are RET FAILs, and RT-T's expectation says so; it does not claim that no RET
> FAIL exists.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1134 … E-1188, V1-115 … V1-136, V2-099 … V2-164, RV-028, RV-051, E-091, E-1010 [32 items]. Controls: N-W, RT-A, … item11-T1p [21 ids].

**Consequence and safeguard.** Figures become asserted counts, which is stricter than informational ones. T1'-bound figures are conditional (OBL-23).

**R6.EVID.4** (lines 4783-4810):
> **R6.EVID.4** Acceptance references. The following figures are acceptance references, each through
> the control named, on the condition of R6.EVID.1. Figures whose control runs on `T1'` are acceptance
> references only while the objects of `T1'` the control needs are reachable from `main`; otherwise they
> are historical measurements (OBL-23).
>
> | Figure | Control | Input |
> |---|---|---|
> | 697 sites; replay errors 0 | RT-A, RT-E | `E`, record commit |
> | 113 `E..H` site changes (`hp-unadjudicated`); 7 HP `context-meaning-unverified`; 7 HP `context-structure-changed` | RT-H0, RT-T0 | `H` |
> | 9 merger groups covering 22 sites | RT-T0 | `H`, `T1'` |
> | 19 region-attributed sites with untracked HP overlap (18 line-attributed); `papers/Substratum.md:266` with splice D029 | RT-T0 | `T1'` |
> | 383 unchanged, 197 replaced, 4 removed sites; 215 region lines; 168 sites moved by `H..T1'` splices | RT-T0 | `T1'` |
> | 5 RET `context-meaning-unverified`; 3 RET `context-structure-changed` | RT-T0 | `T1'` |
> | `resid`: 45 REVIEW lines, 17 hit by no other profile; 11 W1/W2 lines PASS | RT-D | `T1'` |
> | literal item-7 greps at `T1'`: "six structural" 7, "Fourteen" 0, "sixth of" 0, `\bA1\b` 4 | RT-I7 | `T1'` |
> | literal item-7 greps at `H`: 11, 1, 2, 179 | RT-I7 (after RD-3) | `H` |
> | deny lines at `H`: DR-1 61 (a 6, b 2, c 55), DR-3 0, DR-4 28, DR-5 1, 86 distinct; at `E` 95 distinct | RT-DR (after RD-3) | `H`, `E` |
> | DR-3 on `AGENTS.md`: one sentence at `H` (lines 37-39), none at `T1'` | RT-DR3W | control inputs |
> | 95 retired lines, each FAIL `final-unclassified` at `H`; at `H` 86 deny, 123 `final-unclassified`, 209 FAIL lines (93 and 216 with multi-line counting); at `T1'` 0 deny, 12 `final-unclassified` | RT-I7A (after RD-3) | `H`, `T1'` |
> | 176 `final-unclassified` lines of the `repo` profile | item11-T1p | `T1'` |
> | 584 sites swept, each with exactly one new RET FAIL | SW2 | `H` |
> | 697 sites swept, each with exactly one new FAIL | SW1 | `E` |
> | 399 splices verified at `H`; 23 corpus files and 21 other ledgered files conform | RT-C (after RD-3) | `H` |
>
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-037, E-038, E-074, E-039, E-042, E-045, E-046, E-047, E-049, E-089, E-090, ME-3, RD-3,
> RD-23, MC-1, MC-2, VD-10, RD-11. Controls: RT-A, RT-E, RT-H0, RT-T0, RT-D, RT-I7, RT-DR, RT-DR3W,
> RT-I7A, item11-T1p, SW1, SW2, RT-C.

**R6.EVID.5** (lines 4812-4835):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-037, E-038, E-039, E-042, E-045, E-046, E-047, E-089, E-040, E-041, E-043, E-044, E-048,
> E-088, E-1356, E-1357, E-1358, E-1359, E-1360, E-1361, E-1362, ME-2, ME-3. Controls: GATE-16.

**Consequence and safeguard (EVID.4 and EVID.5).**
- EVID.4's figures become gated acceptance references.
- EVID.5's figures stop supporting acceptance. No protection is lost: under AGENTS.md sec. A.42 they could not have supported an enduring claim.
- EVID.5 does change the reach of the historical record, because the 4677-blob search was the basis for dropping DR-1d and DR-2.

**OBL-15** (lines 5025-5033):
> **OBL-15** Reviewed records for RT-T. RT-T is NOT RUN until every reviewed record of sec. 14's review
> load exists at `F` and verifies: HP adjudications for the 113 `E..H` site changes, context
> adjudications for the meaning-context sites, structure reviews, and hit classification records for the
> replacement-region and unheld hit lines (including `papers/GR.md:58`). Gates: plan freeze `F`; the A1
> retirement execution. Discharged by: RT-T run and PASS with every record.
> OPEN: T1'-bound evidence cannot qualify.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-1062, E-1063,
> RD-9, OD-20.

**Consequence and safeguard.** Freezing at `F` and executing the retirement are blocked until every record exists. Preserved and stricter. It also touches v3 D4's record chain.

**Action for the whole group.** Fresh authorization, since no record exists to confirm: "I adopt, on the authority of r6's adoption and not of any earlier decision, the Stage 1 review's design corrections D1 to D8 as r6 states them, including R6.ANCH.14, R6.REC.14, R6.CTRL.19, R6.EVID.4, R6.EVID.5 and OBL-15."
- Re-key these six from "D1-D4" to "S1-D2".
- Add the unmarked R6.RULE.7, R6.RULE.8, R6.RULE.9, R6.CTRL.24 and OBL-1 (F3, F7).

***

## F. S1-D1: the W1 self-match, option B

**What the record shows.** v5.5.9:108-111: "S1-D1, the W1 self-match is resolved by option B (sec. 6.2 step 3)". CHANGES-v5.2.md:45-52 describes option B: "The full negative list is kept, `finit` included. Each W1-c fingerprint carries `negative_allowance: {"finit": 1}`…". No GitHub record exists.

**The strictest earlier statement** is v5.1: no allowance, so W1-c's lines were FAIL `rule-negative-match`. That contradicted RT-D and the other stated outcomes (v6.0e:1762-1764).

**R6.RULE.2** (lines 1434-1447):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-128, V2-048, RV-015. Controls: A6r, A8r, A7r, E-A6r, E-A8r, lint-ok.

**R6.RULE.4** (lines 1461-1485):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-130, V2-050, V2-052. Controls: L1, L2, L3, L4, S1r, V7a, V7c, A5r, A5r-generic, E-L1, E-L3,
> E-S1r, rule-negative, WB1, WB4, WB6, WB7.

**Consequence.** Deny still overrides everything. A negative-literal match is tolerated only within one exact sentence's allowance, at one location, once per tree; anything else FAILs.

**Safeguard.** This changes one protection: a narrowly bounded exception to the negative matcher. The alternative, dropping `finit` from the negative list, would weaken it for every sentence. RULE.2's last sentence also rests on the line 95 decision (group I).

**Action.** Fresh authorization: "W1's self-match is resolved by option B: the full negative list is kept, and only a fingerprint's `negative_allowance`, bound to one exact sentence, context and file and granted once per tree, may permit a negative-literal match."

***

## G. The R-D and A-D labels: durable evidence and the stricter refusals

**What the record shows.**
- v5.5.9:68-73: "the owner decisions of 2026-11-23 on that review, called R-D1 to R-D5 here (stricter refusals, withdrawal integrity, execution identity, the authority configuration, durable evidence)".
- v5.5.9:81-84: "the owner decisions of 2026-11-23 on the authority values, called A-D1 to A-D5 here (… durable evidence)".
- The owner's "final decision" D2 (v5.5.9:49-51) also accepts the three stricter refusal classes.
- None of these has a GitHub record.

**R6.OUT.14** (lines 1004-1020; R-D labels and A-D labels):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-097. Controls: TR46.

- **Consequence.** No result is accepted until it lands on `main`. A compressed blob whose uncompressed hash is off is refused (TR46).
- **Safeguard.** Preserves v5.5's durable evidence. Its substance is already required by AGENTS.md sec. A.42 items 1-2 and sec. A.50 item 1.
- **Action.** Either re-anchor the requirement to AGENTS.md sec. A.42 and sec. A.50, which removes the label dependency, or adopt it freshly: "Acceptance of a tool result is recorded only by an owner-approved landing record on `main` committing the deterministic `result.json.gz`, the admission snapshot and the reproducibility recipe, with CI identifiers as provenance only." Add the unmarked OUT.15, REC.24, CTRL.17 and CTRL.23 (F7).

**R6.PROF.9** (lines 1388-1399; R-D1 and C4; also v5.5.9 final D2):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-121. Controls: S11-58g, S11-57c, S11-58j, S11-58k.

- **Consequence.** The tool refuses the three ambiguous ledger forms and keeps P's item 5 and 6 verdicts.
- **Safeguard.** Preserved, and stricter than P.
- **Action.** Fresh authorization: "The tool refuses the three stricter input classes of R6.PROF.9 (unselected-variant splices, two-edit splices, chained edits) while recording P's per-edit items 5 and 6 results in every case."

R6.REC.18, which rests on R-D3, is quoted in group H.

***

## H. The v6.0e status quote at line 54 (with R-D3, and line 31 for REC.19)

**What the record shows.** These are quotes inside v6.0e, relayed in session, with no comment id and nothing on GitHub.
- The line 54 decision (v6.0e:54-67): "Restore the requirement that the tool commit belongs to main's first-parent history. - Require the workflow's executable dependencies and the tool's import environment to be covered by the integrity checks. - Add the proposed hashlib.py negative control. An unverified file must not execute, even before the tool performs its own integrity checks. … Preserve the removal of automated owner-authorization verification."
- The line 31 decision (v6.0e:31-41): "Approve O-1 option (b): restore the v5.5.9 pre-run pin check in the workflow. … Verify executable dependencies before the verification tool runs. - Retain the independent consumer checks. - Preserve all scientific and technical guarantees. - Do not reintroduce automated owner-authorization verification."

**The strictest earlier statement** is v5.5.9's execution identity: tool files pinned through the authority record `A` (`A.engine_pins`, `A.workflow.path`, K7, v5.5.9:30-39) plus a pre-run pin check. v6.0 dropped the pre-run check, and v6.0b and v6.0c restored it.

**R6.REC.18** (lines 1785-1823; line 54 and R-D3):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-147, E-148, E-149, E-150, E-155. Controls: TR14, TR14-tool, TR15, TR28-tool, TR28-consumer,
> TR29, TR29-tool, TR30, TR48, TR50, TR51, TR52, EI1, EI2, EI2-consumer, EI3, EI5, EI14.

**R6.REC.19** (lines 1825-1841; line 31 and line 54):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-151. Controls: EI8, EI9, EI10, EI11, EI12, EI13, EI15.

**R6.REC.20** (lines 1843-1853; line 54):
> **R6.REC.20** **The import path.** The workflow invokes `python3 -I -B tools/ledger_coverage.py`. The
> entry point does not insert any directory of the checkout into `sys.path`; it loads the package
> `tools/ledger_coverage/` by its location. Before any import of a module not already loaded at
> interpreter start (only `sys` and `os` precede it), the entry point refuses unless the interpreter runs
> in isolated mode and no `sys.path` entry lies inside the checkout. The refusal is ERROR, exit 65, with
> the stop class `NOT_ISOLATED`, written to stderr as one JSON object with that class and the reason (RE-14). Because it fires
> before any import, it writes no `result.json`; it is, with USAGE, one of the two documented cases that
> write no `result.json`. The implementation exits 65 with a message and no class today; that is a
> verification defect, corrected in the tool revision.
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-152. Controls: EI6.

**R6.REC.21** (lines 1855-1870; line 54):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-153. Controls: EI7, EI7-tool.

**R6.REC.22** (lines 1872-1884; line 54):
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
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-154. Controls: TR15, TR50, EI7.

**Consequence.** The tool refuses:
- runs from another repository or event, or not on `main`;
- unpinned or extra tool files, bytecode, an unisolated interpreter, or `sys.path` inside the checkout;
- workflows with unpinned `uses` or the forbidden YAML forms.

The pre-run check ends the job before any tool code runs.

**Safeguard.**
- Preserves the technical identity guarantees of v5.5.9: tool files and workflow are pinned (now through the configuration at `F` rather than `A`), the pre-run pin check is kept, and `T` must be on `main`'s first-parent chain.
- REC.20 and REC.21 are stricter than v5.5.9 (the hashlib.py control EI6; the raw-text line rule).
- REC.20 records a known implementation defect: the tool currently exits 65 with no class.

**Action.** Confirm in the owner's own words, since the quotes exist only inside v6.0e: "The tool binds each result to the tool files, workflow and repository pinned by the configuration at `F`, requires the tool commit on `main`'s first-parent history, runs a pre-run pin check before any tool code, refuses an unisolated import path, and refuses unpinned workflow dependencies by a raw-text line rule (R6.REC.18 to R6.REC.22)."

***

## I. The v6.0e status quote at line 95: authorization is procedural

**What the record shows.** These quotes are inside v6.0e:95-127, relayed in session, with no comment id. Among them:
- "No, let's remove automated historical authorization verification entirely while retaining explicit owner authorization as a procedural requirement."
- "the tool verifies which exact plan was executed; the owner confirms that it was the approved plan. The tool itself makes no claim about authorization."

None of these is on GitHub. Comment 7130449822's prose summary is the session's description, not the owner's words.

**The strictest earlier statement** is v5.5.9's D4 (v5.5.9:53-54): "The authority record …, the versioned comment forms, authority changes that are independently reviewed and owner-approved, and numeric owner id 7273571 are adopted". This was automated verification of owner authorization, together with "Owner at creation" and the freeze ledger.

**R6.STAT.4** (lines 40-46):
> **R6.STAT.4** Owner authorization is procedural. The approvals AGENTS.md requires (sec. A.50: freezing
> and designating the plan, dispatching its trials, executing it, merging into `main`; sec. A.45 rule 3
> and sec. A.51 for work) are given by the owner and quoted with author and time in the record that
> relies on them (AGENTS.md sec. A.42 item 7). The tool neither reads nor checks them. No check of this
> design is waived by r6, and every later step keeps its own owner gate (sec. 19).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-012. Controls: none (procedural boundary).

**R6.PUR.11** (lines 282-288):
> **R6.PUR.11** Approval is outside the tool. The tool verifies which exact plan, configuration, tool and
> evaluated commits a run checked, and identifies them in its result. Whether that plan is the one the
> owner approved is confirmed by the owner, procedurally (R6.STAT.4). No output, outcome, field or
> control of the tool states or implies that a plan, a record, a run or a result was approved or
> authorized. Admitted record directories are named "admitted", never "authorized" (sec. 21).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: E-057. Controls: B4-MEANING.

**Consequence.** The tool will accept a run on a plan commit `F` that the owner never designated, if every technical check passes. Only the owner's procedural confirmation and the quoted record catch that. No output may use approval vocabulary (B4-MEANING).

**Safeguard.** This removes, compared with v5.5.9, the automated detection of an un-designated plan or an unapproved authority change. It preserves every technical identity check (group H). The substance of the procedural part is AGENTS.md sec. A.42 item 7 and sec. A.50; only "the tool neither reads nor checks them" needs the owner's decision.

**Action.** Confirm in the owner's own words: "The tool neither reads nor checks owner authorization: I give the required approvals procedurally, quoted with author and time in the relying record, and no tool output states or implies that anything was approved." The same decision also covers RULE.2's last sentence and OUT.14's clause "the tool does not read or check that quotation".

***

## J. Comment 7093128173: the landing order

**What the record shows.** The comment exists on GitHub (2026-11-23T06:13:50Z), but as a session-written record: "Recorded by the coordinating session from the owner's direct instruction in this session." It quotes no owner words. RV-002 (review-v2.md:271-273) paraphrases it. Its relevant passages:
- "The execution-exception approach of c.7092885251 is superseded and will not be used."
- "land the tool through its own reviewed pull request and a separate merge decision; amend `PREREG.md` to specify the new tool and its exact verification commands, so that every mandatory check of sec. 11 passes as written; then independent review and a new freeze"
- "The amended plan distinguishes the immutable scientific base H, the current integration base on `main`, the candidate retirement tree and the final landing merge tree"

**R6.STAT.8** (lines 68-76):
> **R6.STAT.8** Landing order. Owner decision #1169 comment 7093128173 (`amaybaum`,
> 2026-11-23T06:13:50Z) approved in principle that the tool lands first, that the plan's `PREREG.md` is
> amended and re-frozen so that every mandatory check of its sec. 11 passes as written, and that the four
> trees are distinguished (sec. 20). It superseded the execution-exception route of comment 7092885251.
> The steps it held (implementation, push, pull request, merge and the plan edit) are each governed by
> their own owner record; r6 releases none of them. Before adoption the decision is quoted in r6 in the
> owner's own words, byte-exact from the comment if it holds them, or as the owner restates it (RE-26).
> Pending owner confirmation (see PARAPHRASED-DECISIONS.md).
> Sources: RV-002. Controls: none (governance record).

**Consequence.** The order of gates traced in sec. 32: the tool lands, then the plan is amended and re-frozen, then the trials are rerun, then execution.
- The tool has since landed (comment 7146079156; merge `e2e2a623`), so the first step is history.
- R6.STAT.8's summary leaves out the comment's "Sequencing safeguard (owner)" and the rerun of T0', T1' and `verify.yml`. The four-tree part is carried by sec. 20.

**Safeguard.** Preserved: no execution exception, and the plan must pass as written.

**Action.** The comment holds no owner words, so RE-26 option (b) applies: the owner restates the decision. Proposed text: "Comment 7093128173 records my decision: the tool lands first through its own reviewed pull request, `PREREG.md` is then amended and re-frozen so that every mandatory check of its sec. 11 passes as written, the four trees (H, current `main`, candidate, landing merge) are distinguished, and the execution-exception route of comment 7092885251 is superseded."

***

## K. Entries with no marked requirement

- **v6.0e line 17** (the v6.0d editorial correction) and **line 75** (v6.0a: B-1 to B-3, the meaning table, ls-remote handling, "Record the additional requirement for the later A1 plan amendment"). Nothing in r6 rests on them. Neither is on GitHub.
- The inventory notes for line 75 that its item 4 "is not located in range".
- Recommend: no action, kept as history. The owner may simply withdraw them from the list.
- **r5:7** ("Authorize the Stage A review and the bounded tool design …"). This is not on GitHub. The companion instruction quoted in r5, "Accept V1 on the existing evidence and start the design", is quoted verbatim in comment 7153270569.
- r6 claims its authority from its own adoption, and no requirement restates the quote.
- Recommend: no action.
- **D5-D8 and DI-2.** These are labels with no owner text. Rules cite them in R6.RULE.7-9, R6.CTRL.24, OBL-1, R6.REC.6, R6.REC.7 and R6.CTRL.22, none of which is marked (F7).
- D5-D8 are Stage 1 corrections and fold into group E's decision text.
- DI-2 needs its own confirmation: "A superseding record must share its predecessor's kind, schema and `record_id`, with a valid, acyclic, single-headed chain."

***

## Summary of the recommended actions

| Group | Requirements | Owner's words on GitHub? | Recommended action |
|---|---|---|---|
| A (V4, deferred) | PUR.9, DENY.6, CTRL.15, OBL-6, A1CFG.7 | No for V5-D1; yes for deferring it | (a), (b1) or (b2) at adoption; new rule id if rejected (F5, F6) |
| B | PUR.8, DENY.1, DENY.2, CTRL.7, CTRL.14 | No (paraphrase in 7099655517) | Confirm CTRL.7 and PUR.8; unmark DENY.1 and DENY.2 (F4) |
| C | DENY.5, OBL-3 | No | Fresh authorization; fix V5-D2's text (F2) |
| D (v3 D1-D4) | PLAN.8, CTX.1, CTX.12 | No (paraphrase) | Confirm; add CTX.4 |
| E (Stage 1 corrections, S1-D2) | ANCH.14, REC.14, CTRL.19, EVID.4, EVID.5, OBL-15 | No record | Fresh authorization; re-key (F3) |
| F (S1-D1) | RULE.2, RULE.4 | No record | Fresh authorization |
| G (R-D, A-D) | OUT.14, PROF.9 | No record | Re-anchor OUT.14 to sec. A.42 or adopt freshly; adopt PROF.9 freshly |
| H (line 54, line 31, R-D3) | REC.18 to REC.22 | No (quotes inside v6.0e only) | Confirm in the owner's words |
| I (line 95) | STAT.4, PUR.11 | No | Confirm in the owner's words |
| J (7093128173) | STAT.8 | Record yes, owner's words no | Owner restates (RE-26 option (b)) |

The total is 33 = 5 + 5 + 2 + 3 + 6 + 2 + 2 + 5 + 2 + 1. Every marked requirement appears once in the main groups above.

