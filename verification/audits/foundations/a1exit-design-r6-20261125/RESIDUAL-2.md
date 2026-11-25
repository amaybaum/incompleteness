# r6 consolidated owner list: residual decisions, mechanical corrections, implementation obligations and record corrections (read-only consolidation)

I wrote no files and made no git or GitHub writes. All inputs were read from the r6 scratchpad folder.

**Source abbreviations**
- DEC: DECISIONS.md (OD, MC, VD, ME; approved with Q1-Q5)
- RES: RESIDUAL.md (RD-1 to RD-35; approved with Q6-Q10)
- CONF: CONFORMANCE.md (checks 1-13; new differences #1-#25)
- REP: out-expect/REPORT.md (sec. 8: R-1 to R-7, D-1)
- sec-A, sec-B, sec-C, sec-D: the drafting agents' reports
  - sec-A points are numbered 1-10.
  - sec-B points are RO-1 to RO-7, plus "gap n".
  - sec-C points are numbered 1-12.
  - sec-D points are numbered 1-9.
- B1-B6: the mapping-batch tails
- "Q6-Q10 comment": the #1169 comment recording the Q6-Q10 authorization
- "progress comment": the #1169 comment announcing commit c1244459

**Two overriding facts are applied throughout.**
- RD-9's real gap is orphan and duplicate HP records. Z10 (synthetic_fixture.py:436-449) and H4 (controls_engine.py:390-394) already assert that a matching HP adjudication holds, and no status `adjudicated` exists in the code.
- The RD-20 literals pass Z9's occurrence rule. The issue is that `.github/` is a path literal in the engine, and it cannot be an enumeration under `_enum_rx`.

***

## A. Owner decisions (RE-1 to RE-38)

**RE-1. Scope of the deferred V4 reversal, and how the gate represents a deferred expectation.**
- **Question:** which controls the deferral covers, and how the file records them until r6 adoption.
- **Competing statements:**
  - Q10 and RD-14 defer V4 only.
  - V27, V27-glossary and V15 rest on the same decision, V5-D1, which exists only in paraphrase (ME-6). V4 and V27 PASS with no hit; V15 gives only REVIEW.
  - REP flags V4, V27, V27-glossary and V15 but keeps the file at 0 nulls.
  - sec-B RO-6 and sec-C treat V4 (sec-B also V27 and V27-glossary) as `expect: null`, so the gate cannot hold.
- **Options:**
  - (a) V4 only.
  - (b) All four, decided together at r6 adoption.
  - (c) Reject now: restore DR-2 and DR-1d as plan rule records with FAIL deny-match (OD-8).
- **Recommendation: (b).**
  - The file records both candidate expectations for each of the four rows, with a named blocker "decided at r6 adoption", rather than a silent null.
  - Consequence: the draft can be reviewed with the gate defined. Adoption then picks one expectation per row, and restating A1 in those forms is never FAIL if the reversal is adopted.
- **Depends on:** ME-6, RD-14, Q10, OD-8.
- **Raised by:** REP R-1, sec-B RO-6, sec-C 6, sec-A (Q10 note), sec-D (A1CFG.7, OBL-6), B2.

**RE-2. Restored case for controls with no mutation, and counterparts in other rows.**
- **Question:** what counts as the other direction for the 43 positive or observation-only rows (REP sec. 4(a)), and whether a counterpart in another row (TR48, EI8, N-W, RT-D) counts for an adversarial row.
- **Competing statements:**
  - Q7 and the owner's wording: "every control runs in both directions; every missing required restored case becomes a verification defect".
  - CONF 12 classes these 43 rows (and G2, X6, S11-58i, V25) as "not applicable".
- **Options:**
  - (a) Literal: each row needs its own executed counterpart.
  - (b) For a control with no mutation, its own run is the restored outcome (`baseline: identity`).
  - (c) As (b), and also accept a declared counterpart in another row.
- **Recommendation: (b) for observation-only reference figures, and (c) only through an explicit pairing (RE-4).**
  - The counterpart must run the same input, differing only in the mutation.
  - A positive control's missing direction is the adversarial one, so it names a mutation row or an adversarial row.
  - Consequence: about 43 rows leave VD-RESTORE (177 down to about 134), and each remaining pairing is checkable.
- **Depends on:** Q7, RE-4.
- **Raised by:** REP R-2, CONF 12.

**RE-3. Does the both-directions rule reach controls defined outside sec. 10?**
- **The controls in question:**
  - sec. 13.2: TT, R15-R19, N3-N18, RT-X, RT-L and RT-L2. v2 put the R controls "in the test matrix", and the addendum-2 role tests "run in both directions" (B2).
  - sec. 16.5: Y, Z and Z9.
  - sec. 11: S11.
  - r5: RDIR, I2 and RT-O9.
- **Options:**
  - (a) sec. 10 only.
  - (b) Every control.
  - (c) sec. 10 plus every control a source places under the rule (sec. 13.2, the addendum-2 role tests).
- **Recommendation: (c).** Q7 preserves "any authoritative requirement for both directions".
  - Consequence: more VD-RESTORE rows in sec. 13.2.
  - (b) would be new work beyond consolidation.
- **Depends on:** Q7, RE-2.
- **Raised by:** REP R-4, B2.

**RE-4. A `paired_with` field and a gate finding `direction-missing`.**
- The schema cannot name a row's opposite-direction row. 384 of the 419 rows in sec-C's table declare neither direction.
- **Options:**
  - (a) Add the field and the finding, with a GATE control.
  - (b) Record the defects in prose only.
- **Recommendation: (a).** Without it the Q7 defects are not machine-checked.
- **Depends on:** RE-2, RE-3, RE-12.
- **Raised by:** sec-C 2.

**RE-5. RT-O9's "no base-drift" clause.**
- Q6 names only "RT-L2 still PASS" as dependent. In the RT-O9 run, "no base-drift" holds only because of the drafted, unreviewed AGENTS.md reconciliation record.
- **Options:**
  - (a) Put the clause in RT-O9-L2, which is NOT RUN under RT-L2's release condition (as drafted).
  - (b) Keep it in RT-O9, which would then pass on an unreviewed record.
- **Recommendation: (a).** OD-18 and Q2 reject a PASS on a draft record.
- **Depends on:** Q6, OD-18, Q2.
- **Raised by:** REP R-6, B6 C-4.

**RE-6. Form of U14's restated positive case.**
- **Competing statements:**
  - RD-9 and REP say the site is "left `adjudicated`", and REP's Q9 flag says U14 "does not assert status adjudicated".
  - The code has no such status: pipeline.py:244-248 sets `site.provenance` only.
  - v1 4.6 defines a distinct status (CONF 11).
- **Options:**
  - (a) State the case as the code does: provenance set, no item.
  - (b) Reinstate v1's status `adjudicated`, which is a code change.
- **Recommendation: (a)**, after a Q3 purpose trace showing that the provenance field serves v1's visibility purpose.
  - Consequence: the U14 positive case overlaps Z10 and H4. Keep U14 as a row (Q4 safest) and delete the Q9 flag.
- **Depends on:** RD-9, Q3, RE-7.
- **Raised by:** CONF 11, #16, REP sec. 5, coordinating-session fact.

**RE-7. Class for U14's wrong-region-hash case.**
- **Competing statements:**
  - RD-9: FAILs "through unauthorized-change".
  - The runner and v6.0e sec. 9: `provenance-mismatch`.
  - v1: unauthorized-change plus stale-adjudication.
- **Options:**
  - (a) provenance-mismatch.
  - (b) Both provenance-mismatch and unauthorized-change, which needs a code check.
  - (c) unauthorized-change only.
- **Recommendation: (a)**, unless a code reading shows both are emitted. The U15 retired entry follows.
- **Depends on:** RE-6.
- **Raised by:** REP R-3.

**RE-8. Orphan and duplicate records (RD-9's real gap).**
- **Question:** which trees and segments the orphan rule checks, how a duplicate is handled, and the control id.
- **Competing statements:**
  - RD-9(a): orphan gives record-invalid.
  - sec-B RO-2: a record checked where its subject is legitimately absent (a classification at C or L, an HP record outside E..H) would falsely fail.
  - CONF 11: duplicate HP entries are silently overwritten (pipeline.py:106).
  - The control id differs by draft: RECLINT-ORPHAN (REP), REC-ORPHAN (sec-B), none (sec-D 3).
- **Options:**
  - (a) Check only the trees and segments a record applies to; a duplicate gives FAIL record-invalid; one control with an orphan case and a duplicate case.
  - (b) Diagnostics only, which leaves the gap open.
- **Recommendation: (a)**, with the id RECLINT-ORPHAN, the one already in the file.
- **Depends on:** RD-9, RE-12.
- **Raised by:** sec-B RO-2, sec-D 3, CONF 11, #9.

**RE-9. Where the mutation harness lands, and the mutant names.**
- **The facts:**
  - The harness and mutants are in `ledger-coverage-suite-ci.yml` at CI commit 233412cc, on a CI branch, not on main.
  - The 107 names are enumerated in REP from the CI run's `9-mutation-results.json`.
  - sec-C took the survivor names from the same branch, so a sec. A.42 item 8 trace is needed.
- **Options:**
  - (a) Land the harness and the name list, pinned, with the tool revision.
  - (b) Keep them CI-only, so the MUT rows rest on provenance, against RD-1.
- **Recommendation: (a).** This is also a named evidence blocker under Q10.
- **Depends on:** RD-1, Q8, RE-36.
- **Raised by:** REP R-5, sec-C 3.

**RE-10. Survivors with no equivalence argument (K08, C08, I06, P01).**
- **Options:**
  - (a) Limitation only.
  - (b) Limitation plus a verification defect each, with a distinguishing control.
- **Recommendation: (b).** TR52-consumer closes C08. K08 (submodules in the path map), I06 (TR51's regular-files check) and P01 (the Z9 allowlist) each need one control.
- **Depends on:** Q8.
- **Raised by:** REP R-7.

**RE-11. Requirements with no control, against GATE-8 (the correspondence check).**
- **The cases:**
  - sec-A: 51 requirements with no control, of which 30 are untestable (status, definition, scope).
  - sec-C: PLAN.17 and PLACE.5, 9, 10, 11, 12.
  - sec-D: E-1373 (scope), V1-113, MC-20 and V1-139.
  - sec-B: PROF.12, DENY.5 and DELEG.18 point to OBL.
- **Options:**
  - (a) A declared kind (status, definition, scope, governance, obligation) is exempt from GATE-8, but must name its verification: review, or an OBL id.
  - (b) Move such statements out of the requirement list.
  - (c) Add a control for each.
- **Recommendation: (a) for the untestable kinds.** Every testable requirement gets a control (C-26).
  - PLAN.17 is a pointer to sec. 32 and becomes an OBL reference.
- **Depends on:** OD-1, OD-2, RE-12.
- **Raised by:** sec-A 5, sec-C 1, sec-D 4, sec-B.

**RE-12. Requirement-id scheme and the ids of new control rows.**
- **Competing statements:**
  - OUTLINE uses numbered `R6.<SEC>.<n>`.
  - The expectation file uses named ids (R6.CORE.purity, R6.HP.adjudication). REP adds R6.REPRO.mutation and R6.REPRO.double-run; sec-C invents R6.REPRO.determinism and R6.OUT.usage.
  - New control ids collide or diverge:
    - orphan: RECLINT-ORPHAN against REC-ORPHAN;
    - clean clone: OUT-CONFINED (sec-C) against REPRO-CLEAN (sec-D);
    - demo 2: RT-SHIFT (sec-C) against "demo 2" (sec-D).
  - Ids proposed but absent from the file: RULE-MINLIT, RULE-ZEROFP, CLASS-RETAINED, CLASS-UNLEDGERED, CLASS-PROV-AMBIGUOUS, CLASS-PIN-TARGET, CLASS-RECORD-CHECKS, HIT-REPLACEMENT, DELEG-RECDIR, PROF-PARAMS-LINT, PROF-LANDING-LIST, REPRO-PYVER, RT-M, RT-SHIFT, SIDE-NONREG, VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT.
- **Options:**
  - (a) Numbered ids everywhere: re-key the file with the alias maps (sec-A `expectation_keys`, the sec-C label table, the sec-D alias map), with no aliases accepted by the check.
  - (b) Named ids alias numbered ones in the check.
- **Recommendation: (a)**, and one id per new control, as follows:
  - RECLINT-ORPHAN;
  - OUT-CONFINED, which covers V1-127 and V1-131;
  - RT-SHIFT;
  - the remainder as sec-B and sec-C named them.
  - Consequence: one mechanical re-key before the correspondence check. New ids are not sec. A.48 migrations, but they are recorded in MIG.
- **Depends on:** OD-31, RD-5.
- **Raised by:** sec-D 1, 2, sec-C (labels), sec-A (index), REP sec. 7.

**RE-13. Result fields the code emits that no design lists, and the members of `inputs` and `pins`.**
- **The fields:**
  - sec-A lists 18: invocation, rule_files, hp_merges, records_used, per_edit, evaluated, segments, merger_groups, region_lines, reports, added_text_lines, reconciliation_x_identity, delegation, side_changes, record_directory, checks, landing_compositions, roles.
  - CONF 6 finds 8 more: finding_counts, hit_counts, site_counts, covered_paths, file_conformance, profiles_evaluated, harness, control.
- **Options for each field:**
  - (a) Adopt it.
  - (b) Fold it into `inputs`.
  - (c) Remove it.
- **Recommendation:**
  - Adopt as named fields every field that a control or the gate reads. Adopt the rest as declared diagnostics.
  - Remove none without a Q3 trace.
  - For `inputs` and `pins`, apply RD-10(a): restate the members CONF 6 finds unbound (C-24).
  - Consequence: the schema file grows by 26 fields, and the correspondence check covers them.
- **Depends on:** RD-10, OD-24, Q3, RE-12.
- **Raised by:** sec-A 3, CONF 6, #14, B1(b)1, B2, B3.

**RE-14. Name of the isolation-refusal class.**
- **Competing statements:** `ISOLATION_REFUSED` (sec-A); `NOT_ISOLATED`, written to stderr as JSON (sec-B); reuse of CONFIG_UNREVIEWED.
- **Recommendation: `NOT_ISOLATED`**, in the state form of MAIN_NOT_DESCENDANT, with a stderr JSON line. It is a new identifier and gets a MIG entry.
- **Depends on:** RD-19.
- **Raised by:** sec-A 1, sec-B RO-1.

**RE-15. Outcome for a symlink or submodule side change outside D_rec.**
- RD-12 fixed only "check the entry type before any read".
- **Options:**
  - (a) REVIEW `side-change-unclassified`, with the reason `not a regular file`, as inside the directory.
  - (b) ERROR with a named class, before any read.
- **Recommendation: (a)**, which both drafts propose. Control: SIDE-NONREG.
- **Depends on:** RD-12.
- **Raised by:** sec-A 2, sec-C 7, B6 R-7.

**RE-16. SOURCE_CHANGED raised for content failures of a blob that matches its pin.**
- The cases are an unknown ledger schema id and a correspondence failure (adapters/a1exit_exact_edit.py:164-165; cli.py:713-715).
- **Options:**
  - (a) Rename them to LEDGER_INTEGRITY, which is RD-18's role 2.
  - (b) Redefine SOURCE_CHANGED to cover content failures too.
- **Recommendation: (a).** OD-4's "differs" role stays exact. Code change: C-14.
- **Depends on:** OD-4, RD-18.
- **Raised by:** CONF 1(a), #19, B3.

**RE-17. Completing the OD-4 and RD-18 role table.**
- **Two parts:**
  - (i) PIN_MISMATCH, RECORD_TREE_MISMATCH, SCIENTIFIC_BASE_MISMATCH, MAIN_NOT_DESCENDANT and EDITS_HASH_MISMATCH fit no role.
  - (ii) A malformed configuration is CONFIG_UNREVIEWED in chain mode (cli.py:424-429) but CONFIG_INVALID in harness mode (config.py:241-257).
- **Options for (i):**
  - (a) Add a role "pinned role or tree identity differs: named class".
  - (b) Fold these into SOURCE_CHANGED.
- **Options for (ii):**
  - (a) State the precedence "admission refusal first".
  - (b) Make both CONFIG_INVALID.
- **Recommendation: (i)(a) and (ii)(a).** (ii)(a) documents a fail-closed order.
- **Depends on:** OD-4, RD-18, RE-16.
- **Raised by:** CONF 1(b), 1(c), #1, #12, B3, B1(b)4.

**RE-18. OD-11: derived artifacts changed on both sides.**
- **The code:** always REVIEW `delegated-evidence-missing`, and regeneration is never verified (execution.py:438-441). The derived set is an engine regex (cli.py:1262).
- **Options:**
  - (a) Specify a regeneration check, for example a delegation class at L. REVIEW applies until it passes.
  - (b) Adopt "always REVIEW" as the rule.
- **Recommendation: (a)**, with (b) as the interim behaviour (it fails closed). Move the pattern into the configuration (C-20).
- **Depends on:** OD-11.
- **Raised by:** CONF 2, #20.

**RE-19. Where `.github/` lives, and the other r5 engine literals (RD-20 corrected).**
- **Options:**
  - (a) A new linted category, by the `interface_names` precedent.
  - (b) Move it to `record_authority.py`.
- **Recommendation: (b).**
  - It bounds what a configuration may claim, which is OD-5's exception class.
  - Enumerate `record-directory`, which passes `_enum_rx`.
  - Leave the reason strings unallowlisted, since they pass the occurrence rule.
- **Depends on:** OD-5, RD-20.
- **Raised by:** CONF 7, #17, #21, sec-C 12, B5 b.

**RE-20. A2r's mutated literal.**
- **Competing statements:**
  - The design and REP's applied RD-35 say `(A1)`, which is a prefix of W2-a and W2-b's literals, not W1-d's.
  - The runner shortens W1-d to `six structural` (a1_controls.py:681, 700).
  - Neither case distinguishes a shortening from another change, because `allow_widening` flags any changed literal.
- **Options:**
  - (a) Restate the design as "W1-d shortened to `six structural`".
  - (b) Run on W2-a with `(A1)`.
- **Recommendation: (b)**, the design's literal on the rule where it is a true shortening, plus an assertion that the finding is widening by shortening. REP's row then needs re-checking.
- **Depends on:** RD-35.
- **Raised by:** CONF 13, #22, B4.

**RE-21. EI14-dispatch: release condition and what it gates.**
- **Three drafts:**
  - REP: "the pinned workflow dispatched on a branch with the CX-3 tree after F".
  - sec-C: "a dispatch of the pinned workflow on a branch holding T', after the tool lands, under a launch the owner approves".
  - sec-D: an owner-approved dispatch on a non-main branch, gating acceptance of a chain-admitted result.
- **Recommendation:** sec-C's condition with sec-D's gate. The dispatch needs owner approval (sec. A.51 item 4, sec. A.50).
- **Depends on:** RD-26.
- **Raised by:** sec-C 10, sec-D 9, REP.

**RE-22. RT-L2 when M is re-resolved just before landing (RECON.20).**
- **Options:**
  - (a) RT-L2 must hold on the re-resolved M.
  - (b) Leave it as is: a record bound to the old M fails closed.
- **Recommendation: (a).**
- **Depends on:** OD-18, Q2.
- **Raised by:** sec-C 9.

**RE-23. FAILs that emit no item.**
- **The cases:** the op A record check, replay equality, `ck_errors` and `extended_unmapped` all FAIL through `outcome.compute` with no item (cli.py:763-780).
- **Options:**
  - (a) Emit a `record-invalid` item (obligation RECORD) for each pin finding, a named item for the other three, and require in CLASS.1 that every FAIL has an item.
  - (b) Keep outcome-only FAILs and drop the clause.
- **Recommendation: (a).** Code change: C-23.
- **Depends on:** RD-27, OD-25.
- **Raised by:** sec-B RO-3, CONF 8, #10, B4 a2.

**RE-24. Whose blobs the checkers run from.**
- v6.0e 7.2 says "only F's blobs". E-150 and RV-045 run the evaluated tree's `proof_census.py` and `check_sc42_integration.py`.
- **Options:**
  - (a) preserve_check runs from F's blob; each re-executed generator runs from the evaluated tree's blob in its clone.
  - (b) Everything runs from F's blobs.
- **Recommendation: (a).** (b) would change what the re-execution verifies.
- **Raised by:** sec-B RO-4.

**RE-25. Class of a hit in an HP region.**
- v6.0e says only "REVIEW_REQUIRED". The draft uses `unclassified`, which the code does not confirm.
- **Options:**
  - (a) `unclassified`.
  - (b) A distinct class.
- **Recommendation: (a)**, if a code reading confirms it. Otherwise (b), with a control.
- **Raised by:** sec-B RO-5.

**RE-26. Owner decision 7093128173 (R6.STAT.8).**
- It is recorded only in a reviewer's paraphrase. sec. A.42 item 7 needs the owner's words.
- **Options:**
  - (a) Quote it from the comment, byte-exact, before adoption.
  - (b) The owner restates it.
- **Recommendation: (a)** if the comment holds the owner's own words; otherwise (b).
- **Raised by:** sec-A 6.

**RE-27. Definitions drawn from the code.**
- **The definitions:** the six obligations HP, RET, MAIN, RECORD, TERMS and DELEGATED (OD-14), and `pin-target-missing` and `pin-broken`, which v6.0e never defines and the draft takes from execution.py.
- **Options:**
  - (a) Confirm the code-derived definitions after a Q3 trace.
  - (b) Define them independently, and record differences as defects (the RD-21 approach).
- **Recommendation: (b) for the pin classes**, consistent with RD-21. **(a) for the obligations**, because OD-14 already enumerates the code's set.
- **Depends on:** OD-14, Q3, RD-21.
- **Raised by:** sec-A 8, sec-B gap 4.

**RE-28. RD2-RD5 (directory conditions) against RD-n (residual-decision labels).**
- They differ only by a hyphen.
- **Options:**
  - (a) Keep RD2-RD5, and quote RD-n labels only.
  - (b) Rename the conditions to DIR2-DIR5 before the migration is frozen.
- **Recommendation: (b).** This amends OD-31's approved table, so it needs the owner and a sec. A.48 item 3 review.
- **Depends on:** OD-31.
- **Raised by:** sec-D 6.

**RE-29. RC9's strictness.**
- The code also requires every protected range to lie after the last splice and to have integer offsets.
- **Options:**
  - (a) Adopt the stricter rule into RC9.
  - (b) Relax the code to the design's form.
- **Recommendation: (a).** It is stricter and fails closed, but needs a purpose check that it rejects no valid record. (RC6 is a defect: C-19.)
- **Depends on:** RD-21.
- **Raised by:** sec-C 5.

**RE-30. Composite parents TR28 and TR45, and a composite with a NOT RUN component.**
- **Competing statements:** sec-C says no parents; REP added TR28 and TR45 composites; sec-D wants parents.
- **Recommendation:** keep the composites (REP), with a gate rule: a composite is NOT RUN, inheriting the component's release condition, while any component is NOT RUN (extend GATE-26).
- **Depends on:** RD-4, RD-26.
- **Raised by:** sec-C 8, sec-D 2, REP.

**RE-31. HP merge cross-check (R6.HP.1).**
- No source says what happens when a pinned merge's subject PR number disagrees.
- **Options:**
  - (a) ERROR CONFIG_INVALID.
  - (b) FAIL `provenance-foreign`.
- **Recommendation: (a).** It is a configuration inconsistency detectable before any subject.
- **Raised by:** sec-A 4.

**RE-32. Splitter edge readings (OD-23 check).**
- **The differences:**
  - "uppercase" is ASCII-only;
  - the abbreviation match has no word boundary (`prev.endswith`, so "parsec." matches "sec." and "WhatsApp." matches "App.");
  - `$$` display math is not masked;
  - a version other than 2 gives INTERNAL.
- **Options:**
  - (a) Restate v5.2 verbatim plus the code's precise readings.
  - (b) Fix the code to word-bounded and Unicode behaviour.
- **Recommendation: (a)**, because ME-1 requires splitting equal to P's checker. Any change is verified against P under ME-1, and lint `splitter_version` (C-14).
- **Depends on:** OD-23, ME-1.
- **Raised by:** CONF 3, #15, sec-A 9.

**RE-33. Defining "translation" (OD-10), and the control builder.**
- **Competing statements:**
  - OD-10 defines translation as "ledger splices at their M-translated offsets".
  - The check composes by unique occurrence of the old bytes at M, with old_sha256 re-verified (reconcile.py:232-254).
  - `compose_landing`, which R7, R8, RL and RT-L use, uses a difflib line mapping and falls back to C's bytes (execution.py:444-487).
- **Options:**
  - (a) Define translation as reconcile.compose does, and make the builder use it.
  - (b) Accept the two mechanisms, since a mismatch fails closed.
- **Recommendation: (a).** Code change: C-18.
- **Depends on:** OD-10.
- **Raised by:** CONF 2, #11, #18, sec-C 4.

**RE-34. Scope of the landing check on the tool's own pull request (PLACE.8, OD-26).**
- **Options:**
  - (a) Ledgered paths only.
  - (b) Corpus paths excluded as well.
- **Recommendation: (a)**, as written. No source requires (b).
- **Depends on:** OD-26.
- **Raised by:** sec-C 11.

**RE-35. E-126: "T1' splice images" becomes "X's splice images".**
- **Recommendation:** confirm. The matches must come from the candidate, not an off-main tree.
- **Raised by:** sec-B RO-7, B3.

**RE-36. T1', P and the tool commit are not reachable from main.**
- **The facts:**
  - sec-D checked origin/main at e2e2a623: T1' (14ac71b4), P (4c79be64) and a3799244 are all unreachable.
  - So CI run 45569710442 ran on a commit not on main.
  - RD-23's list misses RT-D, RT-I7A's T1' case and RT-DR3W's T1' case.
- **Options:**
  - (a) Confirm the extended list under RD-23(a). Every T1'-dependent figure is historical, and no figure is a reproduced-on-main acceptance reference until the tool revision lands.
  - (b) Land T1''s objects.
- **Recommendation: (a).** Consequence: r6's EVID section states that no current figure is an acceptance reference, and CI evidence is provenance.
- **Depends on:** ME-3, RD-23, RE-9.
- **Raised by:** sec-D 5, B5(b)1, B3.

**RE-37. OBL gating assignments.**
- OBL-13 and OBL-14 (RT-L2, RT-O9) gate the tool's landing. OBL-26 (the conformance checks) gates r6 adoption.
- **Recommendation:** confirm.
- **Raised by:** sec-D 9.

**RE-38. A-131 (the staged configuration's pins) moved to OBL.**
- It is not among the transfers OD-30 or ME-1 name.
- **Recommendation:** confirm under Q5.
- **Raised by:** B6 C-5.

***

## B. Mechanical corrections (confirmation only)

| # | Correction | Approved requirement it restores | Raised by |
|---|---|---|---|
| B-1 | GATE-draft 16.3: remove SKIP from the record statuses | RD-7 | sec-C, REP sec. 7 |
| B-2 | GATE-draft 16.9: NOT RUN list becomes RT-T, TR5, G-A1, RT-L2, RT-O9-L2, TR45-opC, EI14-dispatch; RT-O9 removed | RD-26, Q6 | sec-C, REP |
| B-3 | GATE-draft 16.2, 16.4, 16.5, 16.7: add `case`, `composed_of` semantics, `gate_findings_include` and `_exact`, the mutation outcomes, library entry `double-run`, `limitation-reported`, GATE-21 to GATE-26, an invariant annex of 136 keys, and a mutation record schema | RD-1, RD-2, Q1, Q8 | REP sec. 7 |
| B-4 | Retired v6.0e ids (O4, TR4, ..., LN12): copy sec-D's 58 per-id RET rows, read from INVENTORY-v6.0e table 2, into the file's `retired`; REP's D-1 is then resolved | RD-13(a), Q4 | REP D-1, sec-D |
| B-5 | The U14 retired entry and "withdrawal-needs-decision" labels in the draft; MAPPING rows V1-099 and V2-072, which say retired | RD-9(a) | sec-D 8, sec-D mapping notes |
| B-6 | C1's preserved-at is confirmed: TT1 and TT13 (engine R1 and R13) and Y6 (synthetic_fixture.py:343-349), plus RL; sec-D's conditional is released | RD-17, OD-20 | CONF 10, sec-D |
| B-7 | The three role tests map to R18-engine and R19-engine (unclassified change on M gives REVIEW), R15 (first parent) and R16 with R17 (unclassified path in C); add them to the rows' requirement lists | RD-17 | CONF 10 |
| B-8 | EXPECTATION-SOURCES Z1-Z8 cites are one line off (D:3080-3086) | RD-35 | B5(b)5, RES |
| B-9 | E-060: drop "(and L)" from op B | OD-13 | CONF 2 |
| B-10 | Restate how C is supplied: `--certified REV`, defaulting to X (cli.py:71; execution.py:61) | RD-33 | CONF 9 |
| B-11 | The 16.6 amendment lists every role-dependent validation: r5 D2-D5, delegation contract, `--classify` duplicate class ids, declared-site uniqueness, HP segment chain | OD-27 | CONF 5, #13 |
| B-12 | State the landing equation with C, not X | OD-10 | CONF 2 |
| B-13 | Default segmentation stated from the code: one segment pin..commit, unledgered, or `hp` if an HP obligation names it (cli.py:795); sec-A 7 is resolved | OD-25 | CONF 4, sec-A 7 |
| B-14 | `whitespace_only`: state its scope (single-line sites, unledgered search, replace opcode; otherwise False) | RD-11 | CONF 4 |
| B-15 | Define RC10 and RC11 independently; sec-C stated RC1-RC13 from `reconcile.evaluate` | RD-21 | sec-C |
| B-16 | RDIR-16 and RDIR-20 invariants: "authority" becomes "directory not admitted"; always write "directory admission" | OD-6 | sec-D 7, B6 C-3 |
| B-17 | Add the requirement to the 58 `xref_controls` rows | OD-2 (correspondence both ways) | sec-A |
| B-18 | Add the rows that approved decisions require: RT-M and RT-SHIFT (demo 2), REPRO-PYVER, OUT-CONFINED (RD-11); SIDE-NONREG (RD-12); RULE-MINLIT and RULE-ZEROFP (RD-11); VD2-HP-SEARCH, VD3-COUNT, VD3-CONTEXT (VD-2, VD-3). Ids per RE-12 | the cited RDs and VDs | sec-B, sec-C, sec-D 2 |
| B-19 | Give OBL ids to PLAN.16, PLAN.17, PLAN.18 and RECON.21, cross-linked to sec-D's OBL-1 to OBL-26 | Q5 | sec-C |
| B-20 | "O6" in the verbatim splitter heading is a finding label, not an identifier (NOTE.13) | OD-31 | sec-A 10 |
| B-21 | E-018 read as "implementation never adopted by default" | Q3 | B3 |
| B-22 | TT12's cite is execution.py:420-423; line 414 is a dead identical conditional | RD-25 | CONF 2, REP |
| B-23 | RD-19's cite is tools/ledger_coverage.py:29-32 | RD-19 | CONF 1 |
| B-24 | Confirm by reading that the result names the tool's blob (V2-010's retirement condition) | OD-25 | B2 |

The approved MC-1 to MC-20 stand. MC-2 and MC-3 are runner edits made in the tool revision.

***

## C. Verification defects and implementation obligations

All of these remain explicit obligations of the later tool revision, under its own authorization.

### C-1. VD-RESTORE (Q7): the two lists reconciled

**The counts.**
- Expectation file: 223 rows carry `restored`. 177 of them are flagged VD-RESTORE: 43 no-mutation rows in REP (a) and 134 adversarial rows in REP (b).
- CONF 12: 112 ids listed WITHOUT a restored case (including EI7-consumer), 36 WITH and 37 not applicable. U1-U12 and M1-M11 were not assessed.

**Differences, found mechanically:**
- **WITHOUT in CONF but not VD-RESTORE in the file (5):**
  - K3 and K4: the file uses the row's own "non-required site" case as the baseline.
  - SW1: the file counts the unmutated baseline, which is computed but not asserted (VD-8).
  - EI7-consumer: not implemented.
  - Z9h: carries no `restored` at all, although D:2291 is inside sec. 10.

  Correction: flag all five. Under Q7, Z9h needs a `restored` row (Z9g is its counterpart).
- **WITH in CONF but VD-RESTORE in the file (8):** A5r (partial in both), GV7-tool, H4 (contrast tree x0), H7, S11-56, S11-58a-f, TR46, X9. Settle each by reading its predicate before freezing the flag.
- **Not applicable in CONF but VD-RESTORE in the file (36):** B1-B4, B6, EI8, G2, K2, K9, K10, L1, L2, N-W, O9, R17, RT-A, RT-C, RT-D, RT-DR, RT-DR3W, RT-E, RT-H0, RT-I7, RT-I7A, RT-T, RT-T0, S11-57d, S11-58i, TR48, TR5, V27, V4, WB1, WB8, WB13, X6.
  - These are decided by RE-2.
  - G2, X6 and S11-58i are adversarial in REP (b) but positive in CONF. Re-read them.
  - V25 has a restored case in the file and is not applicable in CONF.
- **In the file only (not assessed by CONF):**
  - M2, M4-M11, U4, U5, U7, U8, U9 and U12 (adversarial VD-RESTORE);
  - U1, U2, U3, U6, U10 and U11 (no-mutation);
  - GV6-disk, RT-D-gr58, TR5-sim, V27-glossary and EI14-dispatch.

**After RE-2(b), about 134 adversarial rows remain obligations.** RE-3(c) adds sec. 13.2 rows.

### C-2 to C-38: other obligations

| # | Requirement | Defect (file:line) | Distinguishing control | Source |
|---|---|---|---|---|
| C-2 | DEC sec. 4 | Approved VD-1 to VD-12 stand: VD-2 pipeline.py:342-374; VD-3 segments.py:158-161; VD-4 controls_engine.py:538-539; VD-5 R2 old-style comparison (implement per OD-17); VD-6 S11-7; VD-7 a1_controls.py:758-765; VD-8 SW1; VD-9 synthetic_fixture.py:573; VD-10 weak predicates; VD-11; VD-12 a1exit_sitemap.py:25-30 | as in DEC | DEC |
| C-3 | Q9 | 13 weak predicates: E-A1r, E-A2r, E-A3r, E-A6r, E-A8r (no emitted FAIL record-invalid, D:2238-2240); E-S1r, E-S2r, rule-negative (class inclusion only); A5r-generic (no rule); R4-B3-DUP; S7-schema-and-checker (vacuous pass); V3-countercontrol (does not assert 95). U14's flag is withdrawn per RE-6 | the gate re-evaluates `expect`; each runner emits the asserted quantity | REP sec. 5 |
| C-4 | Q10 named blockers | 10 rows have no runner today: EI14-dispatch, EI7-consumer, RECLINT-ORPHAN, REPRO-DOUBLE, RT-O9-L2, TR15-, TR50-, TR51-, TR52-consumer, TR45-opC; plus S11-7 | gate `missing-id` until implemented | REP sec. 3 |
| C-5 | RD-3 | Figures the runner does not assert today: RT-T0's 383, 18 and D029 overlap; RT-I7's H split; RT-C 399/23/21; item11-T1p's 176 lines; RT-D's 45 missing from controls.json | promoted `expect.counts` | REP sec. 6, CONF 13 |
| C-6 | RD-35, D:2083-2084 | K4 asserts only the K1 half (controls_engine.py:291-292); A5r does not name DR-3 (a1_controls.py:747-753); V6 does not assert DR-1b (a1_controls.py:476-478) | assert the K2 half; assert `rule_id` and alternative | CONF 13, #24 |
| C-7 | OD-1, Q1 | Group-error ids (H, U, X-group-error, GV-CACHE-group, TR-group, acceptance-group) and diagnostic keys (`_S7_bad`, `_Z10_detail`) are recorded as records. U13, U15 and `outcome` are still recorded (they would be unexpected-id) | one failed record per member; drop diagnostics; rename `outcome` to Z9-STAGED | REP sec. 3 |
| C-8 | RD-11 (V2-054, V2-055) | Rule lint lacks the 8-character minimum and the zero-fingerprint check. A 0/0 rule is admitted and shadows later rules (rules.py:73-167) | RULE-MINLIT, RULE-ZEROFP | CONF 4, #7, sec-B gap 1 |
| C-9 | OD-25 (`--out` guard) | No rev-parse check; fails open if `git worktree list` fails or the repository is another one (cli.py:104-119); the INTERNAL handler writes without the guard (tools/ledger_coverage.py:53-67) | planted worktree directory; a failing worktree list | CONF 4, #5 |
| C-10 | RD-11 (V1-127, V1-131) | No control for "no writes outside --out, clean clone"; X7 writes to the system temp directory (synthetic_fixture.py:492) | OUT-CONFINED | CONF 4, #23 |
| C-11 | OD-25 | PIN_MISMATCH lacks record_digest and computed_digest (cli.py:740-741) | assert the four fields | CONF 4, #6 |
| C-12 | OD-25 | A broken segment chain gives USAGE 64 with no result (pipeline.py:134-147) | ERROR class with result.json | CONF 4, #4 |
| C-13 | OD-25 (pin check) | Any splice exempts removed checker literals, not only guard-pin splices; literals new at C are unchecked; only literals near a splice are checked; the `pin_ok` freeze path is never fed (execution.py:235-303; cli.py:1219-1220) | a non-guard splice removing a pinned literal must FAIL | CONF 4, #8 |
| C-14 | OD-4, OD-23, RE-16 | Nested config malformation and splitter_version other than 2 give INTERNAL 71 (util.py:170-171); pin-matching content failures give SOURCE_CHANGED | malformed nested field gives CONFIG_INVALID | CONF 1(d), #1 |
| C-15 | RD-18, r5 I2-4 | A missing CLI record gives SOURCE_CHANGED before the admission check; a non-JSON record gives INTERNAL (cli.py:174-177) | both give record-invalid | CONF 1(e), #2 |
| C-16 | OD-4 (record-invalid); intent at config.py:279-280 | A config-referenced class or reconciliation record that is absent, non-regular or of another schema is silently skipped in op C (cli.py:1157-1162) | each case gives record-invalid | CONF 1(f), #3 |
| C-17 | RD-9(a), RE-8 | Orphan HP and context records are never reported; duplicate HP entries are overwritten (pipeline.py:106; context.py:97) | RECLINT-ORPHAN with orphan and duplicate cases | CONF 11, #9 |
| C-18 | RE-33 | `compose_landing` uses difflib (execution.py:444-487) | builder parity control | CONF 2, #11 |
| C-19 | design RC6 | RC6 reads the candidate's bytes at the splice's H offset, which is wrong after an earlier length-changing splice in the same file (fails closed) | two splices in one file, the first changing length | sec-C 5 |
| C-20 | RE-18 | Derived-artifact regex hard-coded in the engine (cli.py:1262) | config-driven derived set | CONF 2 |
| C-21 | RD-12, RE-15 | Entry type is not checked before the read outside D_rec | SIDE-NONREG | RES, B6 R-7 |
| C-22 | RD-19, RE-14 | Isolation refusal has no class (tools/ledger_coverage.py:29-32) | stderr JSON class | CONF 1 |
| C-23 | RD-27, RE-23 | Itemless FAILs (cli.py:763-780) | an item per finding | CONF 8 |
| C-24 | RD-10(a), OD-19(e) | Not emitted: inputs.pin, inputs.record commit and tree, prior, repo_head, ledger sha256, `pins`, per-splice old/new sha256 (needed by U2 and U10); `anchors_sha256` is absent for op B | U2 and U10 assert per-splice hashes | CONF 6, #14 |
| C-25 | v6.0e sec. 9 classes, MC-16 | No control for `retained-changed`, `unledgered-file-change`, `provenance-ambiguous`, `new-pattern-in-replacement`, `unclassified-in-replacement`. Coverage is only indirect for PROF.2 (Y10 changes an adapter, not a profile source), HIT.1 ("held"), the delegation-hash refusal and the `coverage_check` job | CLASS-*, HIT-REPLACEMENT, PROF-*, DELEG-RECDIR rows | sec-B gaps 5, 6 |
| C-26 | RE-11 | Testable requirements with no control: sec-A's 21 (PUR.12, PIPE.1, 4, 6, 7, 8, 15, ANCH.8, 10, 12, 15, HP.1, 5, 7, 14, CTX.8, OUT.16, 20, 22, 25, 28); V1-113, MC-20 and V1-139 (sec-D) | one control each | sec-A, sec-D 4 |
| C-27 | OD-17, VD-4, VD-10 | TT7's landing not asserted; TT8 needs PASS asserted; TT2 (R2) not implemented | as in DEC | B2 |
| C-28 | OD-1 consequence | Mutation evidence is re-established for the changed code, including KILLED-set changes | MUT rows | DEC OD-1 |

***

## D. Corrections to earlier records

| # | Wrong statement | Where | Evidence |
|---|---|---|---|
| D-1 | "The H-series has only negative cases; no Z10 row concerns adjudication"; U14 is "the only synthetic positive case" | RES Basis and RD-9; progress comment; B1(b)3; B2 | Z10 (synthetic_fixture.py:436-449) and H4 (controls_engine.py:390-394) assert a matching HP adjudication. The draft's "preserved-at Z10 and K10" was half right: Z10 is right, K10 is not (CONF 11) |
| D-2 | A matching adjudication holds "with status `adjudicated`"; U14 "does not assert status adjudicated" | RES RD-9; REP sec. 5, sec. 6 | No such status in the code; only `site.provenance` is set (pipeline.py:244-248) |
| D-3 | A wrong region hash FAILs "through unauthorized-change" | RES RD-9 | The runner asserts `provenance-mismatch` (REP R-3); a code check is pending (RE-7) |
| D-4 | r5's engine literals are "against the purity rule" | RES RD-20 | They pass Z9's occurrence rule (purity.py:168-181). `.github/` cannot match `_enum_rx` and is a path literal (reconcile.py:145) (CONF 7) |
| D-5 | RD-8's recommendation (b) | RES | Superseded by Q7 (the Q6-Q10 comment): every sec. 10 control runs in both directions |
| D-6 | "31 runner-only controls"; "34 null rows against 32 + 3" | RES RD-24 heading; Q6-Q10 comment; progress comment | The list names 32. The 34 nulls are 32 + G-A1 + TT12; RT-L's null was case-level; Z9-STAGED was not a row; TT7 already had its class (REP sec. 3) |
| D-7 | The schema extension lists the emitted fields, including "per-splice ids and hashes" | RES RD-10; DEC OD-19(e) | 26 more top-level fields are emitted. Per-splice old/new sha256 are not emitted, only `splice_ids` and `new_region_sha256` (CONF 6) |
| D-8 | Three role tests "have no confirmed control"; C1 needs a check | RES RD-17 | Present: R18-engine and R19-engine, R15, R16 and R17, Y6, R1, RL, R13 (CONF 10) |
| D-9 | RD-23's list of T1' controls; the implicit assumption that CI evidence is reproducible from main | RES RD-23; DEC sec. 0, ME-3 | RT-D, RT-I7A (T1') and RT-DR3W (T1') are missing. T1', P and a3799244 are not reachable from main (sec-D 5) |
| D-10 | "OD-4 needs a conformance check (not yet done)"; RD-27 "needs a check"; E-060 "needs a check" | DEC OD-4; RES RD-27, RD-35 | Done. OD-4: the core roles hold, with the differences in RE-16 and RE-17. RD-27: no item is emitted. E-060: a specification defect (CONF 1, 8, 2) |
| D-11 | A2r applied with literal `(A1)` | REP sec. 6 | `(A1)` is not a prefix of W1-d's literal (CONF 13); RE-20 |
| D-12 | All 223 `restored` rows are sec. 10 controls with U and M | REP sec. 2 | Z9h (D:2291) has none; 13 rows disagree with CONF (C-1) |
| D-13 | Rows still without an expectation: "32 runner-only and V4"; engine literals "not checked" | sec-C | REP has 0 nulls (RE-1); CONF 7 did the check |
| D-14 | TT12 "agrees with execution.py:414"; isolation cite 28-31 | REP sec. 6; RES RD-19 | 420-423; 29-32 (CONF 2, 1) |

***

## Dependency summary

- **RE-12 (ids)** comes before RE-4, RE-8, RE-11, RE-13, B-17, B-18 and C-25.
- **RE-2** depends on RE-4. RE-2 and RE-3 decide the size of C-1. RE-3 depends on Q7.
- **RE-6 and RE-7 depend on RD-9.** RE-8 depends on RD-9 and fixes C-17 and the U15 and stale-adjudication retired entries.
- **RE-1** depends on ME-6, RD-14, Q10 and OD-8, and it decides whether the gate can hold.
- **RE-16 and RE-17 depend on OD-4 and RD-18.** They fix C-14 and the error table in OUT and VALID.
- **RE-36** depends on ME-3 and RD-23. It conditions RE-9, the MUT rows and the whole EVID section.
- **RE-33** depends on OD-10 (it fixes B-12 and C-18). RE-29 depends on RD-21 (with B-15). RE-27 depends on OD-14 and RD-21.
- **RE-30** depends on RD-4 and RD-26. RE-21 depends on RD-26. RE-5 and RE-22 depend on OD-18, Q2 and Q6.
- **RE-19 depends on OD-5 and RD-20; RE-28 on OD-31; RE-32 on OD-23 and ME-1; RE-18 on OD-11; RE-23 on RD-27; RE-14 on RD-19; RE-15 on RD-12.**
- **Independent:** RE-24, RE-25, RE-26, RE-31, RE-34, RE-35, RE-37, RE-38.

## Decisions to settle first

These most affect the design's consistency:
1. **RE-12:** the requirement and control id scheme. Every index, row and the correspondence check depend on it.
2. **RE-2, RE-3 and RE-4 together:** the both-directions scope and the pairing field. They decide whether about 177 or about 134 (or more) rows are defects, and the gate schema.
3. **RE-1:** the V4 deferral scope and its representation. As drafted, the gate cannot hold.
4. **RE-11:** requirements with no control against GATE-8. Otherwise about 50 requirements fail correspondence.
5. **RE-36:** T1', P and the tool commit are off main. This decides the status of every figure and of the MUT and CI evidence.
6. **RE-6, RE-7 and RE-8:** the U14 and orphan cluster that replaces stale-adjudication. Three drafts and the retired entries disagree today.
7. **RE-16 and RE-17:** the completed error-class table. Several C items and the OUT and VALID sections follow from it.
8. **RE-13:** the result field list. The schema file, the gate's `actual` and C-24 depend on it.

***

## E. Coordinator analysis of the four decisions the owner singled out (2026-11-25)

**RE-2 to RE-4 (both directions).** The basis is the wording of v6.0e sec. 10 (D:2081-2082): "Each control runs in both directions: the mutant gives the stated outcome, and the restored tree returns to its control outcome." The second direction is defined through a mutant. A control that applies no mutation has no restored tree, and its own run is its control outcome. That textual argument, not the verification burden, is the only basis for RE-2(b).
- `RE2-ROWS.md` applies it row by row to the 43 rows. A mechanical scan of each row and its design text finds no mutation in 33 rows. Five rows mention a mutation, and five need checking.
- Those 10 stay verification defects unless review shows that no mutation is applied.
- The supported reduction is therefore about 177 to 144, not 177 to 134. The earlier figure is withdrawn.

**RE-1 (V4).** Both candidate expectations are recorded for V4, V27, V27-glossary and V15, each marked "not authoritative; decided at r6 adoption". The gate treats these rows as unsettled, never as holding. Neither candidate becomes authoritative without an explicit adoption decision.

**RE-6 to RE-8 (adjudication).** The recommendation changes. v1 4.6 (DESIGN.md:229-237) gives the status `adjudicated` two purposes:
- (1) "Status `adjudicated` is distinct from `moved` and `authorized-replacement` in every count";
- (2) "A non-matching entry resolves nothing and is itself reported (`stale-adjudication`, a finding)".

The code preserves neither. `site_counts` (engine/cli.py:960-965) counts only the last segment status. An adjudicated HP site is marked only by `st.adjudicated` and a per-site `provenance` reference (engine/pipeline.py:236-249), and is not counted apart from an unadjudicated one. Non-matching entries are never reported.

Revised recommendations:
- RE-6: keep a distinct adjudicated status, or a distinct count key, as v1 requires. This is an implementation obligation. The provenance field alone does not preserve purpose (1).
- RE-8: keep the class `stale-adjudication` with v1's own meaning, a non-matching entry, checked only on the trees and segments the entry applies to (RO-2). Duplicates are reported too. This reverses RD-9's retirement of the class name, and RECLINT-ORPHAN is the control for it.
- RE-7: U14's wrong-region-hash case expects `provenance-mismatch` and `stale-adjudication`, the v1 pair adapted to v6.0e's class. A code check is pending.

**RE-36 (historical evidence).** r6's evidence section must keep two separate attributes for every figure:
- **obtained:** the run, its commit and what it showed, recorded as provenance;
- **qualifies for current acceptance:** reproducible from `main` under sec. A.42.

T1', P and the tool commit a3799244 are not reachable from `main`. So every figure is "obtained" and none currently "qualifies". A figure qualifies only after the tool revision and its inputs are reachable from `main` and the run is repeated there. The integrated draft's EVID section is to be checked against this two-attribute rule before review.
