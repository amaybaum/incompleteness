# OBL-29 remedy r7 independent review brief

Review DESIGN.md and CONTROLS.json at the same r7 revision. Use amendment 6 r5 at
`1f5764572a98b7ae2f306e121e2e410f79c29daf` to reconstruct the defect. Verify
compatibility with the adopted Amendment 6 r13 contract at
`5ad8837521de0a26734266a64f91548fd3dcff1e` (#1593 comment 7193277489).
The bounded paper authority and owner policy are in #1169 comments 7191104852,
7191665350 and 7193274406, the last from amaybaum recorded 2026-11-26 at 13:22 UTC. The r1 verdict was
REVISE at `0b06363c8dbb3d2c7e95a6ca7ab22cdc8cc7d234` (#1601 comment 7191637164).
The r2 verdict was REVISE at `1a067396370ecbd36acd1c35aec79c674de4f8e3`
(#1601 comment 7192414933). R3 at `36d9071cac29075e2b57db11a17031760dbfd836`
received focused REVISE on lineage dependencies (#1601 comment 7192615596). R4 at
`dd1ca3bc40ffe822928986bba9b8a5d67e8a91b9` received focused REVISE on mutable
competing-successor evidence (#1601 comment 7192760996). The r5 review at
`c11e8d4aa82aa46f0557513d476c6fd5e4f03576` accepted the same-freeze correction
and identified re-freeze bypasses (#1601 comment 7192888727). The r6 review at
`af8ede8203a86532c8a7126be4be0e7fdb64735d` found that a record-wide lineage witness
could be missed through another path entry of the same multi-path record (#1601 comment
7195199735). The focused r7 correction is authorized by amaybaum, received 2026-11-26 at
15:48 UTC (#1169 comment 7196789498, item 1). OBL-29 remains an explicit retirement
blocker until its remedy is implemented and
independently verified. Adoption, implementation and trial execution require separate
authorization.

1. **Failure and scope (§1).** Verify the snapshot counterexample, including deletion, rewrite,
   rename, mode and encoding changes, selector widening and disappearance before `F`. Check
   whether any discharge condition can still be relaxed by removing its evidence.
2. **Common evidence for bindings and discharges (R6.OBL29.3–.4).** Verify Form (i), Form (iv)
   and Keys (a)–(b) against the same cumulative records. Check that removing the reviewed entry
   neither makes a same-author review count nor changes an edit binding into a run-level one.
   Look for any remaining use of a different basis for "the scan finds". Verify that the repair
   entry and its positive review still require the current evidence specified by R6.RECON.27.
3. **Historical review lint and lineage (R6.OBL29.3).** Verify exact-reference review
   lint on the reassessment and the current repair record, including location, dissent,
   omitted items and duplicate accepted items. Check the existing lineage anchors and
   normal positive reviews. In the applying A–Q–P case, verify that dissent of an
   operative predecessor remains effective after deletion, including at a second hop.
   Verify the missing-anchor and M-only Q controls. For the new sibling successor
   check, verify the exact edge, eligibility under R6.RECON.2 (d), and the difference
   between the fixed `F` view, live `REV` scan and cumulative negative evidence.
   Check the applying baseline, the live conflict, the rerun after deletion and the
   case that omits `REV`. Verify that none of these supplies a new positive input
   or anchors a repair found only at `M`. Check requalification under the original
   freeze in both new re-freeze fixtures, including an earlier adverse review whose
   operative pin is later removed. Compare the out-of-scope control and check that
   unverifiable custody of an old-`REV`-only witness leaves discharge inapplicable.
4. **Reachability and host methods (§2.3 and §6).** Check the proof under ancestry extension
   and both foxtrot controls, including the loss of first-parent reachability for the exact
   side-change id. Check the distinct outcomes of a merge commit, a squash losing an intermediate
   witness and a rebase that preserves bytes but rewrites commit ids used by applicability.
   The before-replay comparator is a synthetic topic graph. Check how a changed or abandoned `REV`,
   a rewritten branch, a tag-only or uncommitted finding, a rewrite of `main`, and a file
   always outside the selector limit the guarantee. Evaluate the consequences of losing a
   prior run's finding, reviewed reference, lint-relevant review or qualifying competing successor. Check that the
   land-at-once rule for findings leaves related evidence uncovered. Squash/rebase acceptance
   remains unaccepted without independently demonstrated equivalent evidence custody
   and lineage preservation.
5. **Roots and selector (R6.OBL29.1 and .5).** Check that `M`, `F`, `REV`, the predicted
   `M` chain and explicitly read records account for existing category-3 inputs. Check
   B-CANDIDATE-ONLY on both admitted chain and harness runs, including the observable
   binding finding and the absence of the candidate-only marker. Verify that
   tool-prefix widening cannot hide a finding and that R6.RECON.2 (d) and (e) keep
   their admission set. Check the distinction between a newly excluded external path and an
   originally in-scope record moved out later.
6. **Malformed content (R6.OBL29.2, §6 R-3).** Check that classes (b) and (c) without an
   invalidation signal cannot create a lasting block, and that ordinary current
   malformed-nonfinding lint retains its tool-landing exclusion while finding detection
   still covers those paths. Check malformed finding retention and
   the reviewed run-level D3 discharge, including whether a false positive can leave an
   unliftable historical lint failure. Confirm the class (c) hazard for a JSON-leading
   artifact corrupted while carrying both token types.
7. **Legitimate removal (§3).** Verify a revised plan without the bound edit, the applying
   reassessment of the original reference and item, and D3 where eligible. Check that
   a deletion, withdrawal, owner approval, supersession or absent evidence cannot
   stand in for discharge. Check that R6.RECON.26 still distinguishes a detected
   finding from one whose side-change condition makes it bind. Verify the scoped repair
   identity and exact links to the originating witness. Check substantive, independently
   verified replacement evidence and the conditional properly authorized adjudication
   route. Confirm retention of the original evidence and full adjudication history.
   An unresolved witness must survive repeated execution with identical frozen inputs.
8. **Walk and output (§2 and §4).** Verify that the all-parent walk terminates at verified
   parentless commits, the first-parent-diff calculation returns the same entry set, and
   any unreadable required object produces ERROR with no verdict. Check that the
   witness can be chosen deterministically for real commits, predicted `M` and
   explicitly read records. Verify that `present_at_M` and `witness` require an eligible
   regular mode even when a non-regular entry preserves the same blob id.
9. **Amendment 6 compatibility (§5.5).** Verify the complete affected inventory,
   including R6.REC.6, the scoped negative addition to R6.REC.7, its preserved
   anchors and the last reference-resolution sentence of R6.RECON.33.
   Check that R6.EVID.8 keeps `scanned_paths_within` for the representative scope and
   verifies category-3 reads separately in N10, N11, RT-L2 and RT-O9-L2. Verify the
   REASSESS-FORM lookup wording. Confirm
   R6.RECON.23 and adopted r13's retained-result and input verification for
   RECON-ENUM compose with the category-3 additions.
   Check RECON-BLOCK, GV5’s shallow `terms` case and existing op C fixture object completeness.
10. **Controls.** Check both re-freeze bypasses, the two substantive clearance routes
    and the unsupported-clearance and incomplete-custody controls. Verify the r2–r5
    corrections are preserved, with the earlier missing-custody case now failing closed.
    Check the q1 presence assertion, the still-current finding in the reassessment and
    repair deletion comparisons, the historical self-review case and the true category-3
    result needed by B-CANDIDATE-ONLY. Check that the assertions distinguish missing or
    nonbinding evidence, an applying discharge and object-read ERROR.
11. **Actual history and predicted landing.** The r1 reviewer reported zero class (a),
    (b) or (c) entries at `4bb48cddec206e567639fa863ecce852ddd8350e`. Independently
    assess P-ACTUAL-MAIN on full history at `942bd5ea1fd09f4223012b0755bce2d6da07c44a`
    and P-TL-CLEAN on the complete predicted `R*`, including inherited history, when
    independently evaluated. Those exact-history checks remain unverified. The r7 revision
    adds no history scan or trial execution.
12. **Owner decisions (§5.6).** Check the proposed implementation of the recorded
    retention and clearance policy. Review the evidence needed to verify a complete
    custody starting point and the limits of current clearance inputs. Scope decisions
    on broader lint, lineage admission for M-only repairs, mistaken-finding correction
    and rename granularity remain separate. OBL-29 adoption and any new adjudication
    admission mechanism require separate authority.
13. **Record-wide reliance (§2.2, r7).** Check that a witness qualified by R6.REC.7 or
    R6.REC.6 binds the whole disputed record unless custody shows an entry-level check,
    and that (r1)–(r3) decide reliance from records and trees alone, with an undecidable
    case counting as reliance. Verify that another entry or a byte-identical copy of the
    same multi-path record stays blocked whatever its entry path or repair commits
    (N-REFREEZE-OTHER-ENTRY-SAME-Q). Check that NR-1 to NR-4 rebut only (r3), that a
    genuinely independent replacement clears with that evidence
    (P-REFREEZE-INDEPENDENT-REPLACEMENT), that each missing, forged or self-reviewed
    element fails closed (N-REFREEZE-NONRELIANCE-UNSUPPORTED) and that a freeze meeting
    none of (r1)–(r3) is not burdened (P-UNRELATED-FREEZE-NOT-BURDENED). Check whether
    the existing record route can carry NR-4's audit references; if it cannot, NR-4
    cannot be met and only the other clearance routes remain.
