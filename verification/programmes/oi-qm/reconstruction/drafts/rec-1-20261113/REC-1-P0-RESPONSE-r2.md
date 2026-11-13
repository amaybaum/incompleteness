# REC-1 P0: response to the confirmation of r2 (ACCEPT WITH CHANGES)

r3 starts from `REC-1-P0-r2.md` at `7f465d56`. That file was checked byte-identical to the
writer's r2 (`cmp` against `git show 7f465d56:…/REC-1-P0-r2.md`). The change from r2 to r3 is
confined to:
- the title;
- the Revision paragraph;
- the passages listed below.

The outcome is unchanged: O-U for the class, a scoped pass under (LF) [W], and no hand-off to
AW-OA2-1.

| Item | Disposition | Check and location |
|---|---|---|
| A (N8.2(a)) | applied verbatim; heading changed as specified | Re-derived by hand for `N = 2`, with `V = {s0, r_0, r_1, r_2}`. The ring holds `r_2(4) = r_0(2) = x`, so `x` reaches `r_3 ∈ H` at tick 5, giving `V(5) = (y, u′+x, u, y)`; `u′` is unknown, so `V(4)`'s `s0 = x` is not recovered, and (H4) fails. The herald is held at `t_p = 3` (`r_0(3) = y`, `r_1(3) = x`), and the label-free content is as in N8.2(b). The new text keeps r2's opening sentence ("Take N4.2's three-cell shift … a conveyor recorder.") and replaces what follows it. RESPONSE-r1 item 3 is corrected in `REC-1-P0-RESPONSE-r1-corrected.md`; the committed `REC-1-P0-RESPONSE-r1.md` is left unchanged. |
| B (§7, not-reached list) | applied verbatim | r7:366 re-read: "other herald typings and record classes (C6, C7)". |
| C (N3 verdict) | applied verbatim | Consistent with N7's third bullet and with the third row of the §6 table. |
| D (§6 table, row 3) | applied verbatim | r7:333–334 ("preparations outside the coset form are exhibited") re-read. |
| E (§8, review row) | applied verbatim | `REC-1-P0-REVIEW-r1.md` is present in the tree at `7f465d56` (`git ls-tree`). |
| Optional ("[W, P0]" in the §7 Bearing bullet) | applied | Plainly correct: the bearing is a reading made in this record and holds under the scoped result's conditions. It is placed before the full stop. |
| Title and Revision | applied | The title reads "(r3)". One Revision sentence cites the confirmation of r2, r2 at `7f465d56` and this file. |

No other text changed (`diff` of r2 against r3).
