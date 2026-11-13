# Confirmation of REC-1 P0 r2 (independent reviewer of r1)

**Object.** `research/rec-1-1169-20261113` at `7f465d56a7784f35c6b7180cf5c63ef8ad5124fc`.
- The branch was fetched by name, and `ls-remote` gives the same head.
- The head is a single-parent child of `9f7d2612`.
- It adds 7 files under `drafts/rec-1-20261113/`, all status `A`; no other path changes.
- The work was read-only and by hand.

**Verdict: ACCEPT WITH CHANGES.** Five small required changes are listed below as exact old → new
text. The outcome stands: O-U for the class, with a scoped pass under (LF) [W], and no hand-off to
AW-OA2-1. None of the five changes alters that outcome.

## (4) Byte identity

- `REC-1-P0-REVIEW-r1.md` is byte-identical to my `REVIEW.md` (`cmp`). Its sha256 is
  `91f226b9…61f3b6`.
- All six hashes listed in `REC-1-P0-OBJECTS.md` match the committed blobs.
- `REC-1-P0-r1.md` is identical to the record reviewed in r1.
- Against r1, §1 (the verbatim r7 quotations), §3, N1 and N2 are unchanged by diff.

## (1) Required changes 1–7

| Change | Status |
|---|---|
| 1 | Applied verbatim: the O-U paragraph and the mixed-case sentence (whitespace-normalized match). |
| 2 | Applied verbatim. Both delimitation sentences are deleted (grep finds 0 hits). |
| 3 | Applied verbatim to control (iii); N8.2(b) is added. **N8.2(a) needs a fix: see required change A.** |
| 4 | Applied. N3 states composability at a fixed use time. AW-P0-1 carries my text, in bullets. The relaxation clause is deleted (0 hits). |
| 5 | Applied verbatim. |
| 6 | Applied. The ordering text is mine, split into two sentences with no change of content. "No content of OBL-SP…" is deleted (0 hits). The S3 sentence is narrowed. **One item was dropped without being asked for: see required change B.** |
| 7 | Applied. N8.2(b) is NEW and N3 is POSITIVE. |

## (2) Additions, checked by hand

- **N3 POSITIVE, use time `t_p`: correct.**
  - Each admitted preparation herald event is a function of `V(t_p)`.
  - Heralding on `V(t_p)` is admitted and refines every admitted herald.
  - So `L* = K ∩ ker H_{t_p}` on `r_p + K`.
- **N3 extension to a later use time `τ`: correct for a fixed `τ`.**
  - The admitted events are those measurable with respect to both the preparation-stage reads and
    `V(τ)`. That family is closed under conjunction.
  - For affine reads it is the quotient by `ker G_prep + ker H_τ`, so heralding on it is affine and
    coset-structured.
  - The verdict sentence "`J*` is admitted in every instance" holds only per use time. Under the
    per-effect reading, a single `J*` exists only for the preparations admitted at every effect's
    read time; the remainder is N7's out-of-form set. See required change C.
- **Three-reading table.**
  - Row L is correct.
  - Row B with use time `t_p` is correct: there is nothing out of form, the (LF) argument carries
    over to partially retaining observers through `V(t_p)`, and the outcome is O-U.
  - Row B with use time at each effect's read is correct as a classification of the category. r7's
    out-of-form outcome needs preparations to be "exhibited" (r7:333–334), and none is exhibited in
    an instance of the class. See required change D.
  - "Under every reading the outcome is not a pass" is correct.
- **§6 failing-checks list (r7:335–336): correct.**
  - C4's preparation side needs C3.
  - C4's measurement side follows from C2, since equivalent effects agree on the reachable
    vertices, plus C1, since agreement on the vertices gives agreement on their mixtures.
- **(LF) in N5, and `H_e` in N4–N6: correct.** N6 correctly marks preparation noncontextuality as
  needing (LF) and measurement noncontextuality as not needing it.
- **AW-P0-2: correct and record-only.** OA2:534 and OA3:468–469 are cited correctly, and the remark
  that (SP) fails so E(b) is not refuted is correct.
- **N8.2(b): transcribed correctly.** The feeder indexing is checked: `r_{L−k}` enters `r_0` at tick
  `k+1`. So are `V(5)`, (H4), the herald held at `t_p`, the label-free content and `A ∼ B`.
- **N8.2(a) (the writer's "clarification"): inaccurate as stated.**
  - Masking by pads does not by itself break (H4). While the herald register holding `x` stays in
    `V`, the masked front `u′+x` and every other content of `V(4)` can be recovered from `V(5)`.
  - (H4) fails only if retained content leaves `V`, for example a conveyor of three cells
    (`N = 2`). Then `r_2` holds `x` at tick 4, `x` passes into `H` at tick 5, and `V(5)` cannot
    recover `x`.
  - Checked by hand for `N = 2`:
    - `V(5)` is `(s0, r_0, r_1, r_2) = (y, u′+x, u, y)`;
    - the herald is held at `t_p = 3`, since `r_0(3) = y` and `r_1(3) = x`;
    - the label-free content and the gbit are as in (b).

  My r1 review's "for this version" qualifier is consistent with this. Row B (`t_p`) of the table
  then rests correctly on the corrected (a).

## (3) Scope

- **Scoped result.** It is one direction only, labelled [W], conditional on (H3), the record class,
  the typing, C-PM, H-xiv, `D_0` and (LF), and stated as not closing OBL-SP.
- **Ordering rule.** It does not fire.
- **OI-wide claims.** None.
- **"Not reached" list.** It omits r1's "observers that do not retain every read inside `S` (C6)".
  r7:366 names "other herald typings and record classes (C6, C7)" as remaining routes.
  RESPONSE-r1 gives no reason for the omission. See required change B.

## (5) Controls

The table is accurate:
- (i) carries the AW-P0-2 pointer;
- (iii) is my sentence, and its status is "green for the cited artefact";
- (v) adds (LF), notes the cell-delimitation dependence of Instance II, and records "one
  measurement tick each";
- (ii), (iv) and (vi) are unchanged and were verified in r1.

The bullet "What the verdict rests on" is accurate.

## Required changes (exact old → new)

**A. N8.2(a).**
- Old: "It has two designated blank cells at ticks 1 and 2, and uniform pads at every other tick.
  Later records are masked by the pads, so `V(5)` does not determine `V(4)`. This sketch fails (H4)
  and fails (V-ii-H) under the typing."
- New: "Take it as N8.2(b) with a conveyor of three cells inside `V` (`N = 2`), so the herald record
  of `x` passes into `H` at tick 5. Then `V(5) = (y, u′+x, u, y)` does not determine `V(4)`'s
  `s0 = x`, and the sketch fails (H4) and fails (V-ii-H) under the typing. Masking by pads alone
  does not break (H4) while the herald register stays in `V` (N8.2(b)). The label-free effects and
  the gbit are as in N8.2(b)."
- Also change the heading "*(a) r1's sketch: fails (H4).*" to "*(a) r1's sketch, made precise:
  fails (H4).*". In RESPONSE-r1 item 3 the "Clarification" bullets should be corrected to match.

**B. §7, "What the result does not reach".**
- Old: "  - non-affine rules (C2);"
- New: "  - other record classes (C6), as r7:366 names them;\n  - non-affine rules (C2);"

**C. N3 verdict.**
- Old: "Verdict: `J*` is admitted in every instance (POSITIVE: the preparation side needs no
  retention)."
- New: "Verdict: for each fixed use time, `J*` is admitted in every instance (POSITIVE: the
  preparation side needs no retention). Under use at each effect's read, a single `J*` exists for
  the preparations admitted at every effect's read time; the rest are N7's out-of-form set."
- The extension to a later use time is the writer's; it has been checked by hand in this
  confirmation.

**D. §6 table, row "B, with use time at each effect's read", last cell.**
- Old: "out-of-form list (these preparations) together with O-U for the in-form preparations;
  scoped pass under (LF)"
- New: "out-of-form list (these preparations, once exhibited in an instance of the class; none is
  exhibited here) together with O-U for the in-form preparations; scoped pass under (LF)"

**E. §8, the review row, which is stale.**
- Old: "relayed by the coordinator, 2026-11-13; not on any branch)" and "the review itself is not on
  any branch, so this is a gap until landed."
- New: "`REC-1-P0-REVIEW-r1.md` at `7f465d56`, branch `research/rec-1-1169-20261113`)" and "the
  review is on the branch, off `main`, so this is a gap until landed."

**Optional.** In the §7 "Bearing" bullet, append "[W, P0], under the conditions of the scoped
result above".
