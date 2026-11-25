## Independent review of A1 design r6, second correction round (commit 400e4b4fe5f3474b96ee4faa3c437e76e09db782)

**Verdict: ACCEPT-WITH-NITS.** I found no blocking defect. None of the 77 edits weakens a safeguard. Every finding below is non-blocking.

**How I checked**
- I read every file in the directory at the reviewed commit and the full diff against its parent ad035ff5.
- I fetched the 14 cited #1169 comments plus 7092885251, 7165155374, 7165254136, 7165664044 and 7166418469, using `gh api` GETs only. Every body sha256 and `created_at` matches the AUTHORIZATIONS.md table and `generator-round2/PROVENANCE.json`.
- I fetched all 653 #1169 comments to re-run the phrase search behind class (iii).
- I read DESIGN-v5.5.9.md (blob e5b97ef1) and DESIGN-v6.0e.md from the records branch.
- **Generator: yes, I ran it.** I rebuilt its input layout in my scratch directory: `out-final2/` from the parent commit plus `build/correct.py` and `build/report_text.py`, `PENDING-33.md`, `MAPPING.json`, and `gh7/sel.json` = `comments-1169.json`. All 11 input hashes match CORRECTION-REPORT sec. 1. Running `python3 -I -B correct2.py` exits 0, its self-rerun passes, and all nine outputs are byte-identical to the committed files.
- **Counts hold:**
  - 427 requirements, same id set as the parent.
  - 558 expectation rows. The only EXPECTATIONS.json change is `record_id` r6-final2-1 → r6-final3-1.
  - 217 VD-RESTORE.
  - 44 pending: 33 − DENY.1 − DENY.2 + 13, in both the text and the index.
  - 3 OPEN markers.
  - 8 requirements re-keyed to S1-D2.
  - The "Relied on by" lists in AUTHORIZATIONS.md match the REQUIREMENTS.json keys for all 16 keys.
- I recomputed the V4-COMPARISON regex table myself; all 8 rows match.

## Answers to the review points

**1. F1 classification: correct for every cited decision.**
- **Class (i)** comments 7130449822, 7153270569, 7158516152, 7159270333, 7160281751, 7160980912, 7162098696, 7163402499 and 7164340996 each contain an explicitly quoted owner passage. Each quote is present verbatim.
- **Class (ii)** comments 7093128173, 7099655517 and 7121574479 open with "Recorded by the coordinating session" and quote no owner words. The "Sequencing safeguard (owner)" heading in 7093128173 attributes but does not quote.
- **Class (iii):** no #1169 comment contains R-D1, R-D5, A-D5, "three stricter", "chained edits", "historical authorization verification entirely" or "Authorize the Stage A review". S1-D1 and S1-D2 occur only in later session result comments (7158801838, 7162918338, 7165254136).
- The v5.5.9 line citations (44-46, 58-64, 69-75, 94-98, 114-122) match blob e5b97ef1.
- See R1 and N1 for wording issues.

**2. Does any of the 77 edits weaken a safeguard? No.**
- The edits are attribution and classification text, pending marks and keys, option statements, blank lines, and one `record_id`.
- Edit 2 is stricter: R6.STAT.8 can now be confirmed only by the owner restating the decision.
- F4 removes the pending mark from R6.DENY.1 and R6.DENY.2 but keeps their content and controls and still lists them in FRESH-AUTHORIZATION.md.
- F5 and F6 add constraints: a rejection needs new identifiers, and V15 needs a rule of the DR-1d form. The four rows are unchanged.
- The "none weakened" column in the generator is static text it asserts, not something it measures. My conclusion comes from reading the diff, not from that column.

**3. The 12 flagged requirements:** see the classification table below.

**4. V4-COMPARISON.md: accurate.** The candidate expectations are copied exactly. The pattern match results are correct, and the per-row selection under (a), (b1) and (b2) is consistent with R6.PUR.9, R6.DENY.6, R6.CTRL.15 and OBL-6. The earlier-design references (v2 line 429; v4 lines 1172 and 1185; v6.0e sec. 6.4.1) agree with v6.0e's text. See R4 and N4 for two gaps.

**5. Remaining contradictions and open items.**
- **The three OPEN markers** (R6.STAT.10 off-main support of adoption, R6.TREE.12 / LC-7, OBL-23 / item11-T1p) are the three provenance gaps named in 7165664044.
  - Each is stated as open, and none is resolved by an exception.
  - None is a circular prerequisite. Each has an owner path: an approved merge of the r6 documents and their review before adoption; a reviewed regeneration procedure; and either the T1' objects reachable from `main` or an owner ruling that a figure backed only by candidate evidence suffices.
- **Unmapped S1-D3 requirements:** see R2.
- **A new exact-head review is needed after confirmations:** see R5.

## Findings

**R1. The "class (iii)" basis for v6.0e-derived requirements understates their support.** Non-blocking.
- Location: FRESH-AUTHORIZATION.md entries R6.STAT.4, R6.PUR.11, R6.REC.18 to R6.REC.22; AUTHORIZATIONS.md, keys "v6.0e line 31/54/95".
- Defect: the content of these requirements is in DESIGN-v6.0e.md, which the owner adopted in their own words, bound to its exact SHA (7130449822, class (i)). The line-95 quote also holds the owner's verbatim words ("Remove automated owner-authorization verification …").
- The design deliberately treats that adoption as context, not authorization (F9), and r6's adoption remains the authority. That is conservative and not wrong.
- However, only STAT.4 notes the adoption. REC.18 to REC.22 and the line 31/54 keys omit it. The owner therefore cannot see that these confirmations re-confirm a settled decision, which matters given 7165664044 ("Do not reopen settled design decisions").
- Fix: add the 7130449822 note to those entries.

**R2. F7 is incomplete, and the 44 is a lower bound by construction.** Non-blocking.
- Location: CORRECTION-REPORT sec. 5 (S1-D3).
- Defect: marking is driven by whether a cited inventory item carries a decision label. The report itself says S1-D3 (B1-B6: admission, native delegated execution, the classification of `C`, widening reviews, engine purity, control reporting) underlies parts of secs. 11, 13 and 16 but marks nothing for it.
- The rule also over-marks in places. R6.REC.6 is basic record lint that does not depend on DI-2's lineage choice, the same pattern as F4.
- 7162098696 asks for all requirements resting only on paraphrased decisions. The decision package should either say the 44 is citation-derived and incomplete for S1-D3, or let the owner's quoted adoption of r6 serve explicitly as fresh authorization for every unmarked requirement (ME-5 already treats it that way).

**R3. Every "If not authorized" line presents withdrawal (option (c)) as the outcome.** Non-blocking.
- Location: FRESH-AUTHORIZATION.md, all 46 entries.
- Defect: for the roughly 30 entries marked "Stricter", "Preserved" or "Adds a blocker" (for example REC.6, REC.7, REC.18 to REC.22, OBL-1, OBL-15), non-confirmation would read as removing a safeguard.
- This conflicts with 7160281751 ("Preserve all existing safeguards unless their withdrawal is explicitly approved") and with R6.STAT.5.
- Fix: non-confirmation should leave the requirement pending, so r6 cannot be adopted. Withdrawal should be its own explicit owner choice.

**R4. A load-bearing trade-off in V4-COMPARISON rests on a historical measurement.** Non-blocking.
- Location: V4-COMPARISON.md sec. 2, last paragraph, and sec. 4.
- Defect: "neither form matches any line of any tree … or any of the 4677 historical corpus blobs … Adding a rule of either form changes outcomes for constructed strings only" is presented as measured fact.
- R6.EVID.5 classes the 4677-blob search as historical, provenance only, not an acceptance reference.
- Under (b1) or (b2), RT-DR's asserted deny counts at `H` would re-check this on real trees. The comparison should say that and mark the 4677-blob figure as provenance.

**R5. Confirmations quoted into r6 change its bytes.** Non-blocking (sequencing; no new feature).
- Location: R6.STAT.8 and option (a) of PARAPHRASED-DECISIONS.md ("r6 quotes byte-exact").
- R6.STAT.10 requires the exact-head review of the text that lands before adoption. Quoting confirmations, the R6.STAT.8 restatement and the V4 decision text into r6 means this review is not that final review; a bounded delta review is still owed.
- To converge, collect all owner confirmations in one decision so that one delta review covers them.

**R6. The flag set leaves out R6.A1CFG.7, which narrows a check.** Non-blocking.
- Location: FRESH-AUTHORIZATION.md flag list.
- Defect: the entry itself says "S13 is temporarily narrower than v6.0e's" (V4, V27 and V15 excluded until the decision), which meets the stated flag criterion.
- Little practical risk: R6.GATE.9 makes `deferred-expectation` a gate failure, and OBL-6 blocks adoption until the decision. It should still be flagged, and would class as (c): protection provided by R6.GATE.9 and OBL-6.

## The 12 flagged requirements

| Requirement | Class | Reason |
|---|---|---|
| R6.STAT.4 | (c) | Owner approval stays required by AGENTS.md §A.50 items 1, 2 and 5 and must be quoted with author and time (§A.42 item 7). The owner confirms the exact F, T and configuration the tool binds (R6.STAT.3, R6.REC.18 to R6.REC.22). The removal is the owner's own v6.0e decision (line-95 quote, adopted at 7130449822); confirming it does not reopen it. |
| R6.PUR.11 | (c) | Same removal as STAT.4, with the same protection. Its added constraint (no output implies approval, control B4-MEANING) is stricter. |
| R6.RULE.2 | (b) | Without the allowance, W1-c's legitimate lines would FAIL (contradicting RT-D), and the alternative (dropping `finit` from the negative list) is weaker everywhere. The allowance is bound to one fingerprinted sentence, file and location, used once per tree; deny keeps precedence; R6.REC.14 lints it as exact. |
| R6.RULE.4 | (b) | As RULE.2. It is the order of application that enforces the binding. |
| R6.RULE.8 | (b) | On proper ancestors of `recorded_at` the fingerprinted sentence does not yet exist, so `rule-stale` there is always a false positive. Every candidate and `recorded_at` stay covered, and skipped rules are reported. |
| R6.DENY.5 | (b) | Flagged only for W1-c's allowance (as RULE.2). Otherwise it adds blockers, and the W2 rules replace P's blanket `(A1)` strip, which is stricter. |
| OBL-3 | (b) | As DENY.5. |
| R6.PLAN.8 | (b) | Item 7's literal grep cannot pass on any tree that keeps W1's legitimate "six structural" lines. The literal check stays as a countercontrol, and acceptance moves to a reviewed plan amendment, which itself needs owner approval under §A.50 items 2 and 5. |
| R6.PUR.9 | (d) | This is the V4 reversal: (a) permits what v2 and v4 prohibited. It is the substantive decision the owner deferred to adoption (7160980912, 7162098696, 7163402499). As drafted it permits nothing yet: the rows are DEFERRED and the gate fails on them. |
| R6.DENY.6 | (d) | Same decision as PUR.9, stated again. |
| R6.CTRL.15 | (d) | Same decision as PUR.9, stated again. |
| OBL-6 | (d) | Same decision. OBL-6 is the adoption blocker that carries it. |

None is (a).

## The four classes for the 44 pending requirements (all 44 classified)

| Class | Count | Requirements |
|---|---|---|
| Necessary for scientifically valid retirement | 22 | R6.PUR.8, R6.PUR.9, R6.ANCH.14, R6.CTX.1, R6.CTX.4, R6.CTX.12, R6.PROF.9, R6.RULE.2, R6.RULE.4, R6.RULE.7, R6.RULE.9, R6.DENY.5, R6.DENY.6, R6.CTRL.7, R6.CTRL.15, R6.PLAN.8, R6.A1CFG.7, R6.EVID.4, OBL-1, OBL-3, OBL-6, OBL-15 |
| Necessary for reliable verification | 19 | R6.STAT.8, R6.PUR.11, R6.OUT.14, R6.RULE.8, R6.REC.6, R6.REC.7, R6.REC.14, R6.REC.18, R6.REC.19, R6.REC.20, R6.REC.21, R6.REC.22, R6.REC.24, R6.CTRL.14, R6.CTRL.17, R6.CTRL.19, R6.CTRL.22, R6.CTRL.23, R6.CTRL.24 |
| Redundant with an existing safeguard | 2 | R6.STAT.4 (AGENTS.md §A.50, §A.42 item 7, §A.51; keep as a scope statement, no check); R6.EVID.5 (§A.42 items 1-2 and R6.EVID.1/4 already bar these figures as support; keep as a clarifying list) |
| Unrelated to A1 retirement, can be deferred | 1 | R6.OUT.15, offline replay: §A.42 item 1 is met by OUT.14's committed recipe plus a re-run on `main`. If deferred, the `replay` mode of R6.REC.24 and control TR45-opB go with it. |

Notes on the table:
- PUR.9, DENY.6, CTRL.15 and OBL-6 are one decision stated four times. Confirming one should settle all four.
- CTRL.17's EI14-dispatch row runs only after the tool lands and does not gate retirement.
- The two F4 requirements outside the 44 (R6.DENY.1, R6.DENY.2) would class as necessary for reliable verification.

## Nits

- **N1.** AUTHORIZATIONS.md sec. 1 and CORRECTION-REPORT sec. 5 say every class (i) authorization "excludes adoption". Not quite: 7130449822 adopts v6.0e and authorizes local implementation; 7153270569 starts the design; 7158516152 is a read-only assessment. The point that none adopts r6 holds.
- **N2.** In AUTHORIZATIONS.md (V5-D1), the consequence "V4, V27 and V27-glossary PASS … V15 REVIEW_REQUIRED" appears under "What the record says was decided". 7099655517 does not say this; it comes from v6.0e's measurement. Also, the same comment's separate decision ("documented uncaught rephrasings are accepted as a coverage limitation") is the more direct basis for R6.PUR.8.
- **N3.** CORRECTION-REPORT says the previous report "is a record of its round and is not edited", but CORRECTION-REPORT.md was overwritten in place. The previous text survives only in history at ad035ff5. It also cites the generator as `build/correct2.py` and inputs as `out-final2/` and `gh7/sel.json`, while the committed paths are `generator-round2/…`. PROVENANCE.json explains the mapping, but the report should point to it.
- **N4.** V4-COMPARISON says how R6.PUR.9's outstanding-evidence blocker is discharged under (a) but not under (b1) or (b2). Presumably the decision text discharges it in every case.
- **N5.** Draft decision text (a) says the plan's active deny set "contains no rule of the DR-1d or DR-2 form". R6.DENY.1 makes rule content plan content reviewed at `F`. Wording such as "r6 expects …, and no such rule is required" would keep the two consistent.
- **N6.** HIST-4's "the decisions of 2026-11-24" is ambiguous: DI-2 of the same date has a class (ii) record (7121574479), while the E-008 decisions have none.

## Limitations of this review

- I did not re-check the parts of DESIGN-r6.md that this round did not change (about 5,600 lines) beyond the passages the review points touch. I did not re-verify MAPPING.json, MIGRATION.json, INVENTORY.json or EXPECTATION-SOURCES.json, nor the generator's other self-checks, apart from confirming they reproduce.
- I did not run the tool, its controls or any real-tree measurement. The 4677-blob result and the counts at E, H and W are taken from v6.0e's text.
- I did not verify the records-branch copies against the hashes stated in v6.0e, or the content of review-stage1, review-v4, CHANGES-v5.2 or DESIGN-v2/v3/v4 beyond the lines cited.
- My four-class assignment is a reviewer's judgment for the owner's decision package, not a derived result.
- This review was run by a Claude agent launched by the coordinating session, from the same model family (as 7166418469 records). It is non-author only in that it wrote none of the reviewed work.
