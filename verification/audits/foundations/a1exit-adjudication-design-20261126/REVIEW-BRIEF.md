# Formal adjudication design r4: independent review brief

Review DESIGN.md and CONTROLS.json at the same revision. The design is a paper design and is not
adopted. It changes no schema, admission rule, tool, configuration or record. The authority is the
owner decision of amaybaum, received 2026-11-26T16:17Z (#1169 comment 7197443528, item 1), which
requires independent non-author review. The same decision authorizes no schema or admission-rule
modification, implementation, freeze, trial, dispatch or merge. Compare against:
- adopted Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`
  (`verification/audits/foundations/a1exit-design-r6-20261125/DESIGN-r6.md`, read with `git show`);
- OBL-29 remedy r9 at `77a73c022091f598cf807fcf89d66c3cf43208de`
  (`verification/audits/foundations/a1exit-obl29-remedy-20261126/DESIGN.md`).

The gap the design answers is #1601 comment 7197262397, finding 4. r1 at
`2de8462946c65dcf0f004a559fd12b9c18c22ceb` received REVISE (#1605 comment 7197900888, findings F1
to F12). r2 at `6a0afe052b30c6a14d32e03960df3c1df72c4101` received a narrow REVISE
(#1605 comment 7198103680, findings N1 to N5). r3 makes only those textual fixes. A focused review of
r3 should check the r2 → r3 map first, then the claims. The re-check of r3 at
`40740982a75194ed94f005cfa7ad34159ce1a24f` returned ACCEPT WITH NITS (#1605 comment 7198180593). r4
makes only its three nits, under the owner's bounded authorization.

Return a verdict (ACCEPT or REVISE) with a finding for each claim that fails, and state which claims
you checked.

## Nit map (r3 re-check → r4)

| Nit | r4 change |
|---|---|
| 1 | §5 terms: `L(J)` is defined with `Parties_J(C)`, which depends only on `J`'s own bindings, instead of `Parties` at `C`. |
| 2 | R-ADJ-4 and the OD-2 row state the deliberate trade-off: under the authorization veto, an answered reviewer can defeat each new adjudication by rejecting its `authorization` item, even when the quotation is genuine. |
| 3 | New boundary control ADJ-B-DISJOINT-WITNESSES: two witnesses with disjoint sources against the same `Q` and `R`, one upheld and one cleared; no `ADJ-CONTRA` expected. |

## Finding map (r2 re-review → r3)

| Finding | r3 change |
|---|---|
| N1 | R6.ADJ.8 defines *pre-admitted* (R6.ADJ.2–6 at `M`, a qualifying review, citation, location, landing, dedicated landing). Admission adds "no non-exempt adverse review of `J`". R6.ADJ.12 is evaluated in four strata: pre-admission, then exemption and `Answered(J)` over pre-admitted adjudications, then admission, then the effect on `R` and the precondition. Dissent items on `R` are exempt in stratum 2 and disregarded in stratum 4 only through an admitted adjudication. The non-circularity claim is restated per stratum. ADJ-P-ADDRESSED-REDISSENT now states how it is determined. The result field `valid_clearing` becomes `pre_admitted`. |
| N2 | R6.ADJ.4 adds `Parties_J(L(J))`, computed from `J`'s own bindings (finding, `Q`, `R`, `A`, witness sources, predecessor) with reviews from `R*(L(J))` and no citing configuration. R6.ADJ.8 uses it for adverse validity. R-ADJ-2 is corrected. New countercase ADJ-N-UPHELD-A-AUTHOR-J2. |
| N3 | R6.ADJ.9 defines *match* by finding reference and item, replacement `blob_sha256` and `entry_path`, disputed `blob_sha256` and a shared source `blob_sha256`. Reversal needs a replacement with another blob. New countercase ADJ-N-RENAMED-REPLACEMENT. |
| N4 | The exemption of an adverse review of `J` covers only verdicts on `ground:<id>`, `disposition` and `dissents`. Verdicts on `authorization`, `binding` or `conflicts` are never exempt (R6.ADJ.12 stratum 2, R-ADJ-1, OD-2). New control ADJ-N-ANSWERED-AUTH-VETO. |
| N5 | R6.ADJ.3 and `adj.authorization` state that `ADJ-AUTH-TIME` is a form check only (committer times are self-declared). |

## Finding map (r1 review → r2)

| Finding | r2 change |
|---|---|
| F1 | R6.ADJ.8 separates validity from admission. Validity for adverse use needs R6.ADJ.2 to R6.ADJ.6 and a qualifying non-party review in `R*`, with no citation. The contradiction rule (R6.ADJ.9 (4)) and `ADJ-UPHELD` use validity only. R6.ADJ.7 no longer requires citation; citation of exactly one review moved to admission. |
| F2 | Validity for adverse use is evaluated at the landing commit `L(J)`, over `R*(L(J))` with `Parties` at `L(J)` (§5 terms, R6.ADJ.4, R6.ADJ.8). Later reviews of an upheld adjudication, and later growth of `Parties`, are preserved and do not cancel it. R6.ADJ.9 and R-ADJ-7: a wrongly upheld adjudication is reversed only through a new replacement. |
| F3 | Refined (ii) is the recommended default for OD-2 (§5.10, R6.ADJ.12 items 2 and 3), tied to the owner's principle that adjudication remain available. (i) is kept with its conflict stated (§4, §8). OD-2 is not decided. |
| F4 | R6.ADJ.8 landing: the blob is present at its path in some commit `C` on `M`'s first-parent chain, with `C` an ancestor of `F'`. |
| F5 | (a) The usable-identity rule applies to the adjudicator and the technical reviewer only. (b) Missing or malformed party identities are left out of `Parties`, and R6.ADJ.11 does not cover them. (c) The finding's party is "the author or reviewer of the record carrying the finding". (d) The owner is barred as technical reviewer by default (R6.ADJ.4, OD-4). |
| F6 | §3: the (C3) rejection is restated on four grounds (no review of the adjudication, upheld only as a dissent, free-text overloading, tool code as a dispute ledger). The RQ1, RQ4 and RQ6 cells are corrected. A per-dispute registry entry is OD-3 (b'). (A) stays recommended. |
| F7 | §2.1: the host-signature statement is corrected, and the web-flow variant of OD-3 (e) is noted with the API-commit caveat. M5' adds a dedicated landing (`ADJ-DEDICATED`, R6.ADJ.8), recommended under OD-3 (a). |
| F8 | `authorization.replacement` is bound (R6.ADJ.2, R6.ADJ.3). `authorization.time` must precede the committer time of `L(J)` (`ADJ-AUTH-TIME`). |
| F9 | R6.ADJ.12 item 4: every relying witness is cleared by some route, and every dissent item on `R` is addressed or exempt. The per-adjudication dissent coverage is replaced by this discharge-level condition. |
| F10 | §6 adds R6.REC.1, R6.RECON.1, R6.REC.4, R6.REC.5, R6.RECON.36, R6.OUT.18, the result schema and the generators, and states the `OWNER_IDENTITIES` check as a deliberate R6.REC.3 change. |
| F11 | R6.ADJ.14 adds the class (c) risk and two practices: cite records by blob id rather than schema string, and parse-check before landing. ADJ-B-DETECTION-SHAPE gains a class (c) variant. |
| F12 | ADJ-N-NO-REASSESSMENT now asserts that the witness is cleared and the block stands. ADJ-N-AUTH-IN-FREE-TEXT is folded into ADJ-N-UNAUTHORIZED. The two reviewer-judgement controls carry `decided_by`. ADJ-N-REVIEWER-CONFLICTED variant b also expects `ADJ-REVIEW`. Added: ADJ-N-UPHELD-UNCITED, ADJ-N-UPHELD-LATER-REJECT, ADJ-N-UPHELD-ADJUDICATOR-LATER-PARTY, ADJ-P-MISSING-REVIEWER, ADJ-N-OWNER-TECH-REVIEWER, ADJ-P-LANDING-SEARCH-AT-F, ADJ-P-MIXED-NR5, ADJ-N-NOT-DEDICATED-LANDING, ADJ-N-AUTH-TIME, ADJ-P-ADDRESSED-REDISSENT, ADJ-N-NEW-DISSENTER, ADJ-P-NEW-SUBSTANCE-AS-FINDING, ADJ-P-REVERSAL-NEW-REPLACEMENT, ADJ-N-CORRECTION-SAME-R. |

## Claims to verify

1. **Status and scope.** The files state that the design is not adopted and changes nothing. The
   r4 commit changes only the three files of this directory.
2. **Claim I and its qualification (§2.1).** No alternative makes the owner's authorization
   mechanically verifiable under R6.REC.3. The web-flow statement and its caveat are accurate.
3. **Mechanical properties (§2.2).** M1 to M7 are checkable from git objects. S6 and S7 are the only
   substitution cases that remain.
4. **Comparison (§3).** Each cell is correct, and the (C3) rejection rests on the four stated
   grounds. (A) is the smallest sound option.
5. **Validity versus admission (R6.ADJ.7, R6.ADJ.8, R6.ADJ.9).** An upheld adjudication valid for
   adverse use takes effect whether or not any freeze cites it. Nothing cancels it: not a later
   review, not later growth of `Parties`, not a reassessment or configuration it does not bind, and
   not a byte-identical copy of `R` at another path. Check `L(J)` for well-definedness, including the case of a
   qualifying review that never coexists with `J` on `M`'s first-parent chain.
6. **Safety: no bypass (§6).** Every discharge that r9 blocks stays blocked unless R6.ADJ.9 holds.
   Try each r1 attack again, and these new ones:
   - leaving an upheld adjudication uncited;
   - a plan-side rejecting review of an upheld adjudication;
   - making its adjudicator a party after landing;
   - reusing an authorization for another replacement, or dating it after the landing;
   - a non-dedicated landing;
   - using refined (ii)'s exemption with a reviewer outside `Answered(J)`;
   - using R6.ADJ.12's disregard when some relying witness is uncleared.
7. **Reachability (§6).** These clear:
   - ADJ-P-UNAVAILABLE, ADJ-P-LANDING-SEARCH-AT-F, ADJ-P-DISPUTED and ADJ-P-ADDRESSED-REDISSENT;
   - ADJ-P-UNUSABLE-IDENTITY, ADJ-P-MISSING-REVIEWER and ADJ-P-LINEAGE;
   - ADJ-P-MIXED-NR5 and ADJ-P-REVERSAL-NEW-REPLACEMENT.

   Walk each through R6.ADJ.3 to R6.ADJ.12, r9's decision and R6.RECON.27.
8. **Refined (ii) (R6.ADJ.12).** Exemption is limited to later reviews by `Answered(J)`, and for
   reviews of `J` to verdicts on grounds, disposition and dissents. Check that the four strata are
   well-founded, so that every input has exactly one result. Any other
   later dissent defeats the adjudication. New substance enters as a category-3 finding. Check the
   claim that this adds no path to non-termination beyond what r13 already allows, and that the
   definitions are not circular.
9. **Unmet requirements (§4).** RQ1's "verifiable" is unmeetable under R6.REC.3. The RQ6 and RQ7
   trade-off is stated as a choice (OD-2), not as an impossibility of RQ7.
10. **Preservation and fail-closed (R6.ADJ.10, R6.ADJ.11).** Unchanged in substance from r1, apart
    from the party-identity exclusion of F5 (b).
11. **Compatibility (§6).** The change list is complete, including the R6.REC.3 change, which is
    stated as deliberate.
12. **Controls.** CONTROLS.json is valid JSON with 55 unique ids. Every R6.ADJ requirement has a
    control, and every failure condition id used is defined in §5. Each control's expectation
    follows from the text.
13. **Owner decisions (§8).** OD-1 to OD-7 show the design default and the reviewer's
    recommendation side by side, and none is decided.
14. **Register.** No model identifiers. Each reference to content off `main` is classified in
    DESIGN §9.
