# REC-1 P0: response to the independent review of r1 (verdict REVISE)

**Corrected copy.** This file is `REC-1-P0-RESPONSE-r1.md` (at `7f465d56`) with item 3's
clarification corrected, as the confirmation of r2 (required change A) asks. The committed file is
left as it stands. Only item 3 and the closing "Disagreements" line differ.

- **Review.** Independent, non-author, relayed by the coordinator on 2026-11-13. Its verdict:
  "The PASS does not stand"; O-U for the class, with a scoped classical sub-result under (LF).
- **Base.** r2 is built from `REC-1-P0.md` (r1).
- **Scope of the change.** The changes are confined to:
  - the title and the Revision paragraph;
  - §2.1 (one sentence on the use time of a preparation herald);
  - N3–N8;
  - §5–§8.

  §1, §3, N1 and N2 are unchanged.
- **Method.** Each item was checked against its source before it was applied. The reviewer's
  countercontrol (§3 of the review) was re-derived by hand, tick by tick:
  - `s0` runs `0, x, y, 0, x, y` and `r_0` runs `0, 0, x, y, u, u′+x`.
  - `V(5)` determines `V(4)`, `V(3)` and the earlier reads, so (H4) holds.
  - The label-free content is `(x, u)` at tick 4 and `(y, u′+x, u)` at tick 5.
  - `A ∼ B`, and R7 applies.

## Dispositions

**1. §6 (outcome replaced): applied verbatim.**
- The O-U paragraph is the reviewer's text exactly. The mixed-case sentence is also the reviewer's
  text exactly, set as one list item.
- Additions, both required by the coordinator's instruction ("present both readings and their
  outcomes for the owner"):
  - a list of the failing or unestablished checks, as r7:335–336 requires;
  - a table "The reading conflict in r7, for the owner", with readings L, B (use time `t_p`) and B
    (use time at each effect's read).
- Source check: r7:254–256, :287–290, :299–300, :320–321, :309–311 and :335–338 were re-read.
  r7:319–321 carries the P0 example; the review's ":320–321" covers it.

**2. N5: applied verbatim.**
- The joint-holding sentence is replaced with the reviewer's text.
- "The witness does not depend on how label cells are delimited" is deleted.
- In N8.3, "so the verdict does not depend on how cells carrying retained herald content are
  delimited" is deleted.
- (LF) is stated in N5. N4–N6 are restated with `H_e`, and N6 marks which noncontextuality step
  needs (LF).
- Agreed on the merits: the review's countercontrol refutes N5's step in the generality in which r1
  argued it. r1's own N8.3 (r1, N8.3) named the delimitation concern but dismissed it on an argument
  that ignored effects read at earlier measurement ticks.

**3. N8.2 and control (iii): applied, with one clarification recorded.**
- Control (iii) carries the reviewer's sentence verbatim.
- In N8.2, the reviewer's construction is added as N8.2(b), with its verdict: (H4) holds, the
  fragment is a preparation-contextual gbit, and it is excluded only by the rule class.
- Clarification, corrected after the confirmation of r2. r1's sketch, now N8.2(a), fails (H4) only
  when made precise: take N8.2(b) with a conveyor of three cells inside `V` (`N = 2`), so the herald
  record of `x` passes into `H` at tick 5, and `V(5) = (y, u′+x, u, y)` does not determine `V(4)`'s
  `s0 = x`. The reason r2 gave first, masking by uniform pads, is wrong: masking alone does not break
  (H4) while the herald register stays in `V`. The review's "for this version" qualifier is consistent
  with this.
- r3 states N8.2(a) in that precise form, and states that the exclusion of N4.2's shape rests on the
  rule class alone (N8.2(b)).

**4. N3, N8.1 and AW-P0-1: applied.**
- N3 states that composability at the common use time needs no retention.
- Checked on the merits: at a fixed use time, every admitted herald event is a function of the
  present `V`, so admitted heralds are closed under conjunction.
- The review assumes the use time is `t_p`. r2 also covers the use time being a later read: the
  admitted heralds are then the preparation-stage content determined by `V(τ)`, which is still closed
  under conjunction. The conclusion is unchanged.
- N8.1 now places the boundary at accessibility (N5).
- AW-P0-1 carries the reviewer's text, set as bullets with a pointer to N8.2(b) added.
- The clause about relaxation to "composites as far as the typing admits" is deleted.

**5. N7: applied verbatim.**
- Added: the out-of-form set that arises under reading B with use time at each effect's read. This is
  needed for the reading table of item 1.

**6. §7: applied.**
- "No content of OBL-SP remains open within its class." is deleted. §7 states that OBL-SP stays open.
- The bearing is restated as conditional on (LF).
- The ordering paragraph is the reviewer's text verbatim.
- N6's S3 sentence is narrowed: "Under (LF) this re-derives S3:206–207's statement for the C-PM
  fragment. Without (LF) it does not."

**7. N8 classification: applied.**
- N8.2(b) is added as NEW, against the favourable branch.
- N3's composability is reclassified POSITIVE.
- The E(b) step 4 / OA-3 N4.3 step 4 indicator assumption is recorded as AW-P0-2, record-only, as
  the coordinator instructed. Source re-read: OA2:534 and OA3:468–469.

**Further items from the review's body, applied.**
- Control (v): Instance II's nontriviality depends on cell-based delimitation, since `x₁(1) = w + c`
  carries the herald value. This is noted in N8.3 and in Instance II, and Instance I suffices.
- Neither instance exercises C3 with several measurement ticks. This is stated in the control table.
- Control (i): it inherits E(b)'s indicator assumption, with a pointer to AW-P0-2.

**Not changed.**
- The §1 quotations, which the review verified verbatim.
- §3.
- N1, N2 and N4's argument.
- Controls (ii), (iv) and (vi).

**Disagreements.** None on substance. The one clarification is item 3, corrected as above.
