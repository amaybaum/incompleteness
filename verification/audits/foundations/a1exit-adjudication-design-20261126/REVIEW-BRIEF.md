# Formal adjudication design r1: independent review brief

Review DESIGN.md and CONTROLS.json at the same revision. The design is a paper design and is not
adopted. It changes no schema, admission rule, tool, configuration or record. The authority is the
owner decision of amaybaum, received 2026-11-26T16:17Z (#1169 comment 7197443528, item 1), which
requires independent non-author review. The same decision authorizes no schema or admission-rule
modification, implementation, freeze, trial, dispatch or merge. Compare against adopted Amendment 6
r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`
(`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md`, read with `git show`)
and OBL-29 remedy r9 at `77a73c022091f598cf807fcf89d66c3cf43208de`
(`verification/audits/foundations/a1exit-obl29-remedy-20261126/DESIGN.md`). The gap the design
answers is #1601 comment 7197262397, finding 4.

Return a verdict (ACCEPT or REVISE) with a finding for each claim below that fails, and state which
claims you checked.

## Claims to verify

1. **Status and scope.** The files state that the design is not adopted and changes nothing. Its
   proposed requirements (R6.ADJ.1 to R6.ADJ.14) are marked as proposals. The commit adds only the
   three files of this directory.
2. **Claim I (DESIGN §2.1).** Under r13 R6.REC.3 and unauthenticated identity strings (r9 R-8), no
   alternative makes the owner's authorization mechanically verifiable. Check the argument: whether
   any byte the tool reads (trees of `M`, `F`, `REV`, `R*`, pinned records, tool constants) can only
   be produced by an authorized party. Check whether the host's signature on merge commits, the
   pinned tool files or a configuration pin changes the conclusion.
3. **What is mechanical (§2.2).** Each of M1 to M7 is checkable from git objects, and the
   distinguishability table is correct for S1 to S7. In particular, check that S6 (a forged quotation
   accepted by a colluding reviewer) and S7 (impersonation) are the only remaining substitution
   cases, and that the design does not claim more.
4. **Strengthenings (§2.3).** The assessment of a separate authorization record, a tool-constant
   registry (and its pre-dispute variant), a configuration registry, a quorum and an authenticated
   channel is correct. Check especially that a configuration registry is unsound for the reason the
   r8 review gives, and that the pre-dispute registry fails RQ7 for existing disputes.
5. **Comparison (§3).** Each cell of the requirement table is correct for (A), (B1), (B2) and (C1)
   to (C4). Check:
   - the (B1) detection hazard against R6.RECON.35 and R6.RECON.31's closed key set;
   - that (B2) fails RQ2 because the reassessment's author is a party;
   - that (C1) and (C2) fail RQ1;
   - that (C4) is excluded by owner decision item 2;
   - that (C3) cannot express the disposition, the dissents addressed or the reviewer's role without
     putting decision meaning into `accept`/`reject` or free text.
6. **Smallest sound option (§4).** (A) is the smallest alternative that meets RQ2 to RQ6 with typed
   fields and meets RQ1 to the limit of Claim I. Check whether a smaller sound variant exists,
   including (C3) with typed additions that would not amount to a schema change.
7. **Unmet requirements (§4).** The two stated limits are real and are not artifacts of (A): RQ1's
   "verifiable", and the tension between RQ6 and RQ7 against a persistent disputant. Check that no
   alternative removes either without an R6.REC.3 change or a narrowing of RQ6.
8. **Safety: no bypass (§6).** Every discharge that r9 blocks stays blocked unless R6.ADJ.9 holds.
   Try to construct a clearance by any of the following:
   - an adjudication without authorization, or with authorization in free text or tokens;
   - an authorization attributed to a non-owner or scoped to another dispute;
   - a conflicted adjudicator or reviewer, including the author of the disputed record `Q`, the
     original reviewer `v`, the author of `R` or `A`, and a self-review;
   - grounds that miss an adverse item or a dissent;
   - an adjudication bound to another finding, witness, replacement, reassessment or original
     configuration;
   - an adjudication not on `main` before `F'`, not cited, or in the wrong directory;
   - an upheld or contradicting adjudication, whether valid, unresolvable or deleted;
   - a supersession or a disposition outside the enum;
   - deleting `V` or rewriting the finding at the adjudication's landing;
   - a dissent on `R` or on the adjudication after it lands;
   - an adjudication covering one of two witnesses;
   - a cited adjudication without a reassessment.

   Check that R6.ADJ.12's exception to R6.REC.6 and to r9 NR-3 and NR-5 cannot be used by a
   discharge for which some relying witness is not adjudicated.
9. **Reachability (§6).** A legitimate clearance is possible when `V`'s reviewer is unavailable
   (ADJ-P-UNAVAILABLE), has an unusable identity (ADJ-P-UNUSABLE-IDENTITY) or disputes `R` with
   reviews landed before the adjudication (ADJ-P-DISPUTED), and for a lineage witness
   (ADJ-P-LINEAGE). Walk each positive control through R6.ADJ.3 to R6.ADJ.12 and through r9's
   decision and R6.RECON.27, and check that no condition is unsatisfiable. In particular check:
   - the independence sets against the fixture identities;
   - the landing condition against R6.RECON.33's resolution from `F'`;
   - the reconciliation-directory location against R6.RECON.1.
10. **Preservation (R6.ADJ.10, R6.ADJ.13).** No path erases or narrows the original finding, the
    witness or an earlier adjudication. A removed adjudication is evaluated from `R*`. The result
    reports every adjudication with its failures.
11. **Fail-closed (R6.ADJ.11).** Missing, ambiguous, unresolvable and contradictory inputs give a
    false `Adjudicated`, and unreadable required objects give ERROR. Check the rule under which a
    definitely invalid upheld adjudication does not contradict while an unresolvable one does
    (ADJ-N-CONTRADICTION-INVALID-IGNORED, ADJ-N-CONTRADICTION-UNRESOLVABLE).
12. **Compatibility (§6).** The change list against r9 and r13 is complete, and the items listed as
    unchanged are unchanged. Check R6.ADJ.14 against R6.RECON.35 classes (a) to (c). Check that
    `adjudications` does not collide with r9 R6.OBL29.8's `witness`. Check the proposed R6.REC.3
    sentence against R6.REC.3's present text and the migration `approval` precedent.
13. **Controls.** CONTROLS.json is valid JSON with 39 unique ids. Every R6.ADJ requirement has at
    least one control. Every failure condition id used is defined in DESIGN §5. Each of the owner's
    listed cases is present:
    - an authorized, independent, substantive adjudication clears;
    - clearance when the original reviewer is unavailable, and when they dispute;
    - an unauthorized adjudicator; a conflicted adjudicator; the disputed record's author as
      adjudicator;
    - an administrative override without substance;
    - a misbound adjudication;
    - a forged authorization;
    - a deleted or contradicted adjudication;
    - an attempt to erase the original finding.

    The residual control ADJ-R-FORGED-AUTH-COLLUSION documents R-ADJ-1 and implies no owner
    acceptance.
14. **Owner decisions (§8).** OD-1 to OD-7 are the open choices, each with its consequences stated.
    No choice is made silently in the requirement text: check the defaults of OD-2, OD-4, OD-6 and
    OD-7 against R6.ADJ.4, R6.ADJ.9 and R6.ADJ.12.
15. **Register.** The files contain no model identifiers and no GitHub writes are implied. Each
    reference to content off `main` is classified in DESIGN §9 (AGENTS.md §A.42 item 8).
