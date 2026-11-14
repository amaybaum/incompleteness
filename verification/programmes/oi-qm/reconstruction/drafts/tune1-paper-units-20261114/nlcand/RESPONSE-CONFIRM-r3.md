# RESPONSE to CONFIRM-r3: dispositions, applied in NLCAND-r4 and SUMMARY-r4

Writer's dispositions of `CONFIRM-r3.md`, the exact-head confirmation of `NLCAND-r3.md` at `485f9a2d`
(ACCEPT WITH CHANGES; required R1–R4, optional S1–S7). Each change was checked at its source before it was
made. `NLCAND-r3.md`, `SUMMARY-r3.md` and `RESPONSE-r1.md` are unchanged. The README named in R2 and S4, S6
belongs to the coordinator and is not edited here. Paper-only; no computation on any OI rule.

## Required

| # | Disposition | Source check | Where |
|---|---|---|---|
| R1 | Applied, in modified form | r3's header against `CONFIRM-r3.md` §1 (hunk 2) | `NLCAND-r4.md` status paragraph. "independent" is dropped before "non-author review". The reviewer's text described r3; r4's paragraph instead names all three reviews, says r4 applies the `CONFIRM-r3.md` changes and two factual corrections with no change of verdict, and says r4 itself is unreviewed, as the coordinator asked |
| R2 | Applied in r4 and the summary; README not edited | S4:30–39: R-nl is "the rounded bijection of SM:294"; H-nl is "the named hypothesis 'the world's rule is R-nl'" | `NLCAND-r4.md` header, with the citation widened to S4:30–39 as the reviewer gives it; `SUMMARY-r4.md` status, with "r3's hypothesis" replaced by "that it is this ring rule" so that the summary of r4 does not name r3 as its source |
| R3 | Applied, in modified form | `CONFIRM-r2.md` (confirmation of r2); `CONFIRM-r3.md` (confirmation of r3) | `SUMMARY-r4.md` status: "a non-author model review of r1, its confirmation of r2, and an exact-head confirmation of r3; r4 itself is unreviewed; not independently verified" |
| R4 | Applied as given | Main:724, ledger item (xiv), "measurement independence"; r3's B2 and Verdict (b) state the Bell-local claim "under (xiv)" | `SUMMARY-r4.md`, Bell, first bullet |

## Optional

| # | Disposition | Reason |
|---|---|---|
| S1 | Applied | Factual: `sourcing_rule_independent` runs from `FrozenSourcing.lean`:295 to its proof term `Iff.rfl` at :299; r4's A3 cites :295–299 |
| S2 | Applied | Factual: "H-ring" occurs only in the header, so "written H-ring below" was inaccurate; r4 reads "written H-ring" |
| S3 | Not applied | Not a factual error: the label `u_{a+2}(0)` is in the block's tick-1 state. The point is about which readout region B7 uses, and B7 already uses only the declared label with region `{a, a+1}` |
| S4 | Not applied | README text, not the writer's file |
| S5 | Not applied | A scope refinement, not a correction: for the one-cell variant as specified there is no declared record cell, so "absent under S" is true; B5 states when the table returns |
| S6 | Not applied | README text, not the writer's file |
| S7 | Not applied | Cosmetic line lengths |

## Other differences between r3 and r4

The title; the §8 fixed-point sentence ("r3 and r4 add wording edits only"); the review row of §10, which now
lists `CONFIRM-r3.md` and this file. No node, derivation or verdict differs. The summary differs from
`SUMMARY-r3.md` only in its title, R3, R4 and R2, and in two removed blank lines.
