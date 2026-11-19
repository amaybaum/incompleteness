ACCEPT WITH CHANGES — `S3-PLAN-r6.md` at `a756262d426fd29e16912d9893bfbaaa9d994c0d` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused confirmation of the S3 plan, r6

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r6.md` and `RESPONSE-S3-PLAN-r5.md`, including its 26-site table. The copies supplied to
  me are identical to the committed files.
- `S3-PLAN-r5.md` is unchanged, and `REVIEW-S3-PLAN-r5.md` is preserved as delivered.
- The full diff from r5 to r6.

**Line numbers** are r6's.

## Summary

- **R6 is resolved, and the root-cause rule is sound in its direction.**
- **Coverage.** I found no negative-closure site the writer missed.
- **Three changes are needed**, all small:
  - **R7.** The label "NC-1" collides with an existing label, inside this same document.
  - **R8.** The rule has no place for a capability that has been *disproved*, as opposed to
    unsourced. That removes a sourced path to closing route M.
  - **R9.** At H-RR's second and third refutation routes, the rule is over-applied. It makes H-RR
    unrefutable while track (a) is open, and it is inconsistent with the plan's own treatment of
    AC-1.

## 1. R6 and the rule's coverage

**R6: resolved (ll. 588–594).**
- A native-marker miss requires "(β) to hold with a sourced retention of `s_A`", and an erasure that is
  "an executable uncomputation". An assumed retention or erasure is "an assumed apparatus … and does
  not count toward (a′)".
- The quiet marker "does not count toward (a′)".

**The rule's sites (ll. 677–683).** All are applied as claimed:
- "empty on K1" (l. 581);
- (a′) (ll. 687–690);
- (b′) (ll. 692–694);
- (c′) (l. 696);
- (e′) (ll. 707–709);
- H-RR's refutation routes (ll. 321–331);
- the U4 row (l. 742);
- D-1's falsification sentence (l. 598);
- owner question 6 (l. 785).

**Missed sites: none.** I grepped r6 for refut-, negative, closes, falsif-, "counts toward", "not
available" and disprov-. Every hit is either in the writer's 26-site table or a status record of
another Issue (site 26).
- (d′) is a reduction, and the "each subject to" heading (l. 685) covers it.
- K-1 ("If the PR program is excluded, U1 must name the native fact … with its source") is a
  positive exclusion that already requires a source.

## 2. Is the rule over-applied?

**Positive results are not blocked unfairly.** Positive outcomes already need class-(i), sourced
support: the strongest tier, H-RR support, and the §3 criterion. The rule makes negatives symmetric
with them.

**R8. "Disproved" is a sourced finding, and the rule does not say so (ll. 588–590, 677–683, 687–690).**
- The rule sorts capabilities into *sourced*, and *unsourced or assumed*. The plan's own vocabulary
  has a fourth value, #866's "derived / assumed / unsourced / **disproved**" (§3, l. 233).
- On K1, erasure by uncomputation is not merely unsourced. It is proved not available: S-L3, "the
  inverse is representable but not available" (l. 500), at MR-1 stage-1 scope.
- So on K1 the native-marker miss branch, which requires "an executable uncomputation", can never be
  reached.
- Meanwhile the *disproof* of erasure is itself a negative resting only on a proved fact. Observed
  quantum-eraser behaviour is a raw-direct observable (§A.24), so the disproof bears on it directly.
  The rule neither counts it nor sends it anywhere.
- **Fix:** add to the rule: "A capability shown not available (disproved) is a sourced fact. A
  negative that follows from it counts at that fact's scope." In the miss branch, add a
  native-marker case "erasure disproved (S-L3, on K1)". That case is reported as a candidate
  raw-direct miss on eraser behaviour, conditional on (α)–(δ) and (γ), and counted toward (a′) under
  the same conditions.

**R9. H-RR's second and third refutation routes require sourced quantum references (ll. 324–327).**
- The text: "where the reference's operations on that interface are sourced", and "where both sets
  of operations are sourced".
- Coherent operations are exactly what track (a) has not sourced. So with this wording, H-RR cannot
  be refuted by either route until track (a) succeeds positively.
- The plan treats AC-1 differently. The writer's own site 21 records "reported as failing AC-1" as a
  negative finding about a restriction's *content* that does not need the reference sourced.
- Route 2 is the same kind of finding: "every renewal limit excluding fresh PR also excludes the
  quantum Bell reference (failing AC-1)". What must be sourced there is the *limit*, a native fact
  about renewal. The quantum reference is a target law under `Θ`, not an executed experiment.
- **Fix:** in routes 2 and 3, require the renewal limit, or the cost comparison, to be sourced, and
  take the quantum references as target laws under `Θ`. This matches AC-1.
- Route 1 ("every operation the execution uses sourced") is correct as written.

**A sourced path to negative closure still exists, with R8 applied.**
- (a′) can be reached through a structural failure of (β), or through the disproved-erasure case.
- (b′) can be reached through a theorem on the observer-level lift.
- (c′) can be reached through a σ12 screen resting on sourced capabilities.
- (d′) is a reduction.
- (e′) is pending until M-1 and M-2 are fully specified, which needs an MR-1 stage-2 authorization.
- So route M is closable in principle, and remains falsifiable. Negative closure is gated on owner
  authorization of MR-1 stage 2 and on #866's σ12 screen. §8.6 should say that gating in one
  sentence; it is now implicit across (c′) and (e′).

## 3. The label "NC-1"

**R7. Rename it.**
- "NC-1" already names the setting-dependent interaction definition: "O-SET (setting-dependent
  interaction, NC-1)", at l. 144 of this same document.
- The same label is #866's O-SET row and #1009's NC-1 definition round.
- Rename the rule, for example to "SRC-NEG" or "the sourcing rule for negatives", at all eleven uses:
  ll. 23, 26, 321, 581, 598, 677, 685, 697, 707, 742, 785.

## 4. Other changes in the diff

None. The diff touches only:
- the title and the revision header;
- H-RR's refutation routes;
- the D-1 outcomes;
- the new rule paragraph;
- (a′), (b′), (c′) and (e′);
- the U4 row;
- owner question 6.

## 5. Verdict

**ACCEPT WITH CHANGES.**
- **Required:** R7 (rename), R8 (a disproved capability is a sourced fact; the disproved-erasure case
  on K1) and R9 (H-RR routes 2 and 3 to source the limit, not the reference).
- **Recommended:** one sentence stating the gating of negative closure on MR-1 stage 2 and the σ12
  screen.
- All of these are local. A diff check suffices.
