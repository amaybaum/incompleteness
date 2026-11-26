# OBL-29 remedy: brief for the independent design review

Scope: DESIGN.md and CONTROLS.json in this directory, read against design r6 amendment 6 r5 at
`1f5764572a98b7ae2f306e121e2e410f79c29daf` (`verification/audits/foundations/a1exit-design-r6-20261125/`).
Authority: owner decision, amaybaum, #1169 comment 7191104852, item 2 (paper-only design and
independent design review). The design is not implemented or adopted. The review decides nothing
for the owner.

Claims to verify:

1. **Failure statement (DESIGN sec. 1.3).** Check that the block decision is required to be monotone
   in recorded history (R6.RECON.26, the lifecycle tables), and that r5 evaluates it over current
   content. Check that this one statement accounts for every OBL-29 and #1598 case. Check whether
   it misses a removal path.
2. **Antitone predicates (sec. 1.3, R6.OBL29.3).** Check that deleting the reconciliation record a
   second-kind review names, or deleting an accepting review of a first-kind entry, makes r5's
   R6.RECON.27 Keys (b) or (a) admit `repair: null`. Check whether r5 has further predicates that
   relax a block or a discharge when evidence is removed and that the list omits.
3. **Pre-`F` and merge cases (sec. 1.3).** Check that a finding landed after `H` and removed before
   `F`, and a post-freeze record seen through one `REV` and dropped when `REV` is merged, both escape
   r5, so that OBL-29's post-`F` statement is narrower than the defect.
4. **Coverage argument (sec. 2.3).** Check the argument that, under P-1, a complete store and an
   unchanged detection function, no change lifts a finding carried by a reachable entry. Check that
   the only uncovered routes are a history rewrite of `main` and an unreachable or uncommitted
   finding.
5. **Fixed selector (R6.OBL29.5, sec. 5.3).** Check that a later freeze can widen a tool-landing
   prefix, or pin a blob, so that a finding leaves r5's detection. Check that removing the exclusion
   for detection only leaves R6.RECON.2 (d) and (e) unchanged. Check that P-TL-CLEAN is the
   necessary precondition.
6. **Presence-based conditions (R6.OBL29.4).** Check that reading the repair and the reassessment
   at `M` and `F` (not from `R*`) can only make a discharge fail when content is removed.
7. **Legitimate removal rule (sec. 3).** Check that every legitimate route (reassessment, a revised
   plan without the edit, D3's `repair: null`) remains available on the original reference.
   Check that no route depends on an authorization the tool would have to read (R6.STAT.4,
   R6.PUR.11). Check that missing evidence fails closed.
8. **Walk (R6.OBL29.7, sec. 4).** Check that the ancestry walk terminates, has no depth limit,
   reads parents only from verified content, and gives ERROR, never a verdict, on a missing,
   pruned, corrupt or shallow object. Check that the first-parent-diff computation is equivalent
   to the union over trees.
9. **Amendment 6 compatibility (sec. 5).** Check that the requirement-change table is complete and
   minimal. Check that R6.RECON.23, R6.RECON.28, R6.RECON.33 and R6.CFG.* need no change. Check
   that no expectation row at `1f576457` changes.
10. **Controls (CONTROLS.json).** Check that each control's expected outcome follows from the
    requirements it names. Check that every R6.OBL29 requirement with a check has both a control
    that must fail and one that must pass. Check that the countercases would catch an
    implementation that scans only `M`, scans only the first-parent chain, applies a depth limit,
    keeps the tool-landing exclusion, or reads Keys eligibility at `M`.
11. **Full-history check (residual R-3).** On a full clone of `main`, run R6.RECON.35's classes over
    every reachable entry under `verification/audits/`, and report any entry the remedy would newly
    bind. The design's own check covered only the 81 first-parent commits of a shallow clone.
12. **Owner points (sec. 5.5).** Assess the four points: ancestry or first-parent, mistaken
    independent findings, R6.REC.6, and the rename burden. Say whether any is a correctness
    question rather than a choice.
