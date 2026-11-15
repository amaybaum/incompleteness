# Response to REVIEW-r7 (verdict ACCEPT WITH CHANGES)

This is paper-only, read-only work. Nothing was edited in the repository, nothing was run on OI
rules, and nothing was posted.

`LEDGER-r8.md` is a minimal revision of `LEDGER-r7.md`. r7 is unchanged; its SHA-256 begins
`ce93aba2`. r8 is marked UNREVIEWED. Nothing outside the two items below changed, and no identifier
was added, removed or renumbered. The new Main:74 line is a row of §R.2's trace table, not a registry
row.

| Item | Disposition | Check at source and change |
|---|---|---|
| S1, LC-3 reconciliation with T2 | Applied | **PR #1241:** merge `1257617a9` and commit `e806e52cb` are ancestors of `main` (`git merge-base --is-ancestor`). `e806e52cb` adds "the horizon ratio of (C2)'s realization clause" at three Main sites (:216, :340, :352). **#1234's body, item 3:** "`Main.md:414` and `:416` rest the … graph on a downstream citation ([SM §3.1], G(x))", so Main:20 is not a T2 Bell item. **Main:74:** "Realization — τ_S/τ_B ~ 10⁻³² at the horizon", which is GR:48's ratio, not identified as GR's. **Changes:** §R.2's reconciliation bullets are replaced as proposed. A Main:74 row joins the trace table: an illustration, not a dependency, paired with GR:48 and :456, and an MC-5 candidate. D18 (§11 and §F.1) now cites Main:74 and GR:48. U-10's outcome cell records the reconciliation. |
| N1, superseded citations | Applied in modified form | **Correct:** the manuscripts make three superseded citations, not the two r7 counted. `oiPlusPos_iff_qm` (GR:242) and `carrier_general_oiPlusPos` appear at three sites: GR:242 (both identifiers) and Main:588 (`carrier_general_oiPlusPos`). r7 had missed GR:242 for `carrier_general_oiPlusPos`. **Wrong:** the review's third item. `git grep` of `papers/` and `book/` finds no unprimed `derivedOI_qm_iff_layerFlowExecutable`. GR:266 and Main:588 cite only `derivedOI_qm_iff_layerFlowExecutable'` (and, at GR:266, `…_swap'`). §R.5 now states the two identifiers, the three sites, and the absence of the unprimed key. Each cited superseded identifier sits beside its successor, as the census rule requires. |
