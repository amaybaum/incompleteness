# Changes in revision 3 (MIGRATION-r3.md, RETIREMENT-r3.md)

**Source.** `S/paper/retire-review/RECHECK-r2.md` (ACCEPT WITH NITS). This revision applies N1–N4 and
nothing else. The r2 files are kept unchanged as the re-checked object. No repository file was
changed. Every git command ran with `-c gc.auto=0 -c maintenance.auto=false`.

| Nit | Change | Where |
|---|---|---|
| N1 | Row 19's (d) now rests on Explainer:551, "predicts the observed value", alone, against `GR.md:360`. Two parts of :549 are stated as not (d): "The framework explains why: there is nothing to cancel" refers to the 122-digit cancellation, which GR:360 says the framework eliminates; "sits exactly at the classical geometric scale" is close to GR:358 | MIGRATION-r3 §2 row 19 |
| N2 | The owner option to edit `LEDGER.json:3100` is removed. Leaving the line unchanged is stated as the only compliant choice: all its "Explainer" mentions, the pending-action sentences included, sit inside the block the route labels historical (§A.27; §A.42 item 4). Survivor-list caveat removed | RETIREMENT-r3 §2.4 (row and survivor list); §5 PD6 |
| N3 | §2.5 names CC-1 as a halted round. Its receipt has `status: halted` and no `e`; its trees are D `0f2687b7` and the withdrawn candidate `342fb68f` (withdrawal `5ae15444`), and `--check E` runs at that candidate. CC-2 is complete: D `6d335d0a`, E `36b12c4c`. The required commit-message sentence names CC-1's D and withdrawn candidate. For CC-2, A45 and CONSC-2 (all `complete`, checked in their receipts) it says D and E | RETIREMENT-r3 §2.5 (table row; commit-message text) |
| N4 | §4.1(7) writes the base blob to a temporary file (`git show <base>:papers/Explainer.md > "$TMPDIR/explainer-base.md"`) before `git diff --no-index`. Process substitution works there only on git ≥ 2.42. The dry-run comment in §4.2 matches | RETIREMENT-r3 §4.1(7), §4.2 |
