# r6: the V4 group, three consistent resolutions compared (deferred)

The expected outcomes of V4, V27, V27-glossary and V15 stay deferred (#1169 comments 7160980912, 7162098696, 7163402499 and 7164340996). This document compares the three consistent resolutions; it recommends none and changes no expectation. The four rows of EXPECTATIONS.json are byte-identical to the previous draft.

## 1. Current state

Each row has `expect` DEFERRED and two candidate expectations, each "not authoritative; decided at r6 adoption" (RE-1). The gate reports `deferred-expectation` and never holds on them; S13 leaves them out (R6.A1CFG.7).

| Row | Candidate "reversal adopted" | Candidate "reversal rejected" |
|---|---|---|
| V4 | `{"cases": [{"case": "review and deny profiles", "counts": {"hits": 0}, "outcome": "PASS"}, {"case": "item7-literal", "outcome": "PASS"}]}` | `{"cases": [{"case": "review and deny profiles", "classes_include": ["deny-match"], "outcome": "FAIL"}, {"case": "item7-literal", "outcome": "PASS"}]}` |
| V27 | `{"counts": {"hits": 0}, "outcome": "PASS"}` | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V27-glossary | `{"counts": {"hits": 0}, "outcome": "PASS"}` | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V15 | `{"classes_exact": ["unclassified"], "invariants": [{"all": "hits", "have": {"profiles": ["resid"]}}, {"resid_key": "resid-a"}], "outcome": "REVIEW_REQUIRED"}` | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |

## 2. The two rule forms and what they match

Patterns as v6.0e sec. 6.4.1 records them (DR-1d and DR-2 are retired identifiers, sec. 33 of DESIGN-r6.md; a rule of either form would take a new identifier):

- form of DR-2: `(?i)\b(?:sixth|seventh)\b[^.;]{0,40}\bstructural\s+(?:property|assumption|axiom|posit|premise|condition)\b[^.;]{0,80}\bfinit`
- form of DR-1d: `(?i)\b(?:structural|substratum(?:'s|’s)?)\s+(?:sixth|seventh)\s+(?:assumption|axiom|posit|premise|condition|property)\b`

Computed by the generator of this document (Python `re`, each text as one sentence; the V27-glossary text is the start of book/glossary.md line 13 at `H` with "The sixth of the framework's structural assumptions A1–A6" replaced by the V27 text, truncated after the first clause):

| Text | Form of DR-2 | Form of DR-1d |
|---|---|---|
| V4: "the framework's sixth structural property, finiteness of the bijection" | match | no match |
| V27: "The framework's sixth structural property is finiteness of the substratum" | match | no match |
| V27-glossary: "**Background independence (A6).** The framework's sixth structural property is finiteness of the substratum: the substratum dynamics is covariant under spatially varying internal-index transformations" | match | no match |
| V15: "the substratum's sixth axiom, finiteness" | no match | match |
| PUR.8 example: "the six posits of the substratum" | no match | no match |
| PUR.8 example: "six assumptions about the substratum" | no match | no match |
| PUR.8 example: "The posit ledger lists fourteen." | no match | no match |
| PUR.8 example: "the fourteen-item posit ledger" | no match | no match |

A rule of the DR-2 form catches V4, V27 and V27-glossary but not V15; V15 needs a rule of the DR-1d form. None of the constructed examples of R6.PUR.8 matches either form. The tool measured the four rows under the current rule set (v6.0e sec. 6.4.1, "What removing them costs (measured)"): neither form matches any line of any tree at E, H, W or T1' or any of the 4677 historical corpus blobs, and the distinct deny-line counts at E, H and W are the same with or without them (95, 86, 86). Adding a rule of either form changes outcomes for constructed strings only, and needs reconciliation against N-W and the independent review of the deny set (OBL-3).

## 3. The three resolutions

Earlier designs: v2's demonstration expected V4 FAIL (DESIGN-v2.md line 429); v4 expected V4 FAIL `deny-match` by DR-2 and V15 FAIL `deny-match` by DR-1d (DESIGN-v4.md lines 1172 and 1185); v5.5.9 and v6.0e expect V4 and V27 PASS and V15 REVIEW_REQUIRED.

### (a) accept the reversal

| Row | Expectation selected | Expectation (exact) |
|---|---|---|
| V4 | reversal adopted (accepted residual: PASS, no hit) | `{"cases": [{"case": "review and deny profiles", "counts": {"hits": 0}, "outcome": "PASS"}, {"case": "item7-literal", "outcome": "PASS"}]}` |
| V27 | reversal adopted (accepted residual: PASS, no hit) | `{"counts": {"hits": 0}, "outcome": "PASS"}` |
| V27-glossary | reversal adopted (accepted residual: PASS, no hit) | `{"counts": {"hits": 0}, "outcome": "PASS"}` |
| V15 | reversal adopted (REVIEW_REQUIRED unclassified through resid only) | `{"classes_exact": ["unclassified"], "invariants": [{"all": "hits", "have": {"profiles": ["resid"]}}, {"resid_key": "resid-a"}], "outcome": "REVIEW_REQUIRED"}` |

- Rules needed: none
- Identifiers: none
- What it permits and prohibits: the added texts of V4, V27 and V27-glossary PASS with no hit; that of V15 is REVIEW_REQUIRED through `resid` only, which holds once the reviewed `resid` record with resid-a is frozen at `F` (R6.PUR.8, OBL-3); detection of those forms rests on review outside the tool
- Relative to earlier designs: permits V4 PASS where v2's demonstration and v4 expected FAIL; permits V15 REVIEW_REQUIRED where v4 expected FAIL `deny-match` (DR-1d); equals v5.5.9 and v6.0e
- S13 and obligations: S13 counts the four rows with the "reversal adopted" candidates; R6.PUR.9's outstanding-evidence blocker is discharged by the decision text

### (b1) reject for the ordinal-property form only

| Row | Expectation selected | Expectation (exact) |
|---|---|---|
| V4 | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"cases": [{"case": "review and deny profiles", "classes_include": ["deny-match"], "outcome": "FAIL"}, {"case": "item7-literal", "outcome": "PASS"}]}` |
| V27 | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V27-glossary | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V15 | reversal adopted (REVIEW_REQUIRED unclassified through resid only) | `{"classes_exact": ["unclassified"], "invariants": [{"all": "hits", "have": {"profiles": ["resid"]}}, {"resid_key": "resid-a"}], "outcome": "REVIEW_REQUIRED"}` |

- Rules needed: one plan deny rule of the DR-2 form, adopted with the plan's rule records at `F` after independent review and reconciliation against N-W
- Identifiers: one new identifier, chosen with the plan amendment; never DR-2 (retired and never reused, sec. 33; AGENTS.md sec. A.30)
- What it permits and prohibits: V4, V27 and V27-glossary FAIL `deny-match`; V15 stays REVIEW_REQUIRED through `resid`
- Relative to earlier designs: restores v4's FAIL for V4 (and the former M-DR2 text, V27); keeps v6.0e's REVIEW for V15, where v4 expected FAIL
- S13 and obligations: S13 counts the four rows: three with "reversal rejected", V15 with its "reversal adopted" candidate (the candidate labels no longer describe the choice for V15 and are restated at the decision); OBL-3 gains the new rule

### (b2) reject for all four

| Row | Expectation selected | Expectation (exact) |
|---|---|---|
| V4 | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"cases": [{"case": "review and deny profiles", "classes_include": ["deny-match"], "outcome": "FAIL"}, {"case": "item7-literal", "outcome": "PASS"}]}` |
| V27 | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V27-glossary | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |
| V15 | reversal rejected (a plan rule record restored for this form, sec. 12) | `{"classes_include": ["deny-match"], "outcome": "FAIL"}` |

- Rules needed: as (b1), and a second plan deny rule of the DR-1d form, reviewed and reconciled in the same way
- Identifiers: two new identifiers; never DR-1d or DR-2 (both retired, sec. 33)
- What it permits and prohibits: all four FAIL `deny-match`
- Relative to earlier designs: restores v4's expectations for V4 and V15 (and V27 as v4's M-DR2 countercontrol)
- S13 and obligations: S13 counts the four rows with the "reversal rejected" candidates; OBL-3 gains two rules

## 4. Trade-offs

- (a) needs no new rule and no review of new patterns, and leaves the ordinal-property and reversed-ordinal forms to review outside the tool (V15 at least REVIEW_REQUIRED). It permits what v2 and v4 prohibited.
- (b1) restores tool detection of the form v2 and v4 named for V4 at the cost of one new rule, its review and its reconciliation; V15 stays REVIEW_REQUIRED, which v4 did not permit.
- (b2) restores v4's detection for both forms at the cost of two new rules; neither form has a real-tree witness (v6.0e sec. 6.4.1), so both rules are justified by constructed strings only.
- In every resolution the retired identifiers DR-1d and DR-2 stay retired; the decision text names the new identifiers (b1, b2) or confirms that none is added (a).

## 5. Draft decision texts (for the owner's choice at r6 adoption; not adopted)

- (a): "I confirm that the A1 plan's active deny set contains no rule of the DR-1d or DR-2 form, and I accept knowingly that the added texts of V4, V27 and V27-glossary PASS with no hit and that of V15 is REVIEW_REQUIRED only, with detection of those forms resting on review outside the tool."
- (b1): "I reject the V4 reversal for the ordinal-property form: the amended plan's rule records at `F` include an independently reviewed deny rule of the DR-2 form under a new identifier, so that V4, V27 and V27-glossary FAIL `deny-match`, while V15 stays REVIEW_REQUIRED through `resid`."
- (b2): as (b1), "and a second independently reviewed deny rule of the DR-1d form under a second new identifier, so that V15 also FAILs `deny-match`."
