# Review of REUSE-TEST-SPEC r3 (focused confirmation)

**Object.** `REUSE-TEST-SPEC-r3.md`, with `RESPONSE-REUSE-TEST-SPEC-r2.md`. They answer
`REVIEW-REUSE-TEST-SPEC-r2.md` (cited REV-2).

**Reviewer.** Independent and not an author. Read-only. Hand checks only, against a line diff of r2
and r3. No edits, commits or GitHub writes.

**Verdict: ACCEPT.** The three required changes are resolved. The β criterion certifies β at its
confidence weight, under the independence and stationarity hypothesis it states. Nothing outside the
listed items changed.

## 1. The three fixes

**C-1. Resolved.**
- Arm W and DR-3a:
  - §5 states that every program `Θ` identifies with arm W is case (N), so DR-3a's strict-(U)
    exclusion there is definitional.
  - The same statement is repeated at DR-3a.
- Outcome map:
  - Rows 9 and 10 record setting-independence (DR-2) and state that L-2's half is not addressed by
    arm W; row 10 adds that L-3's half is not addressed either.
  - A step the fallback removes reads as `ns-unresolved` (DR-3) or `rep-unresolved` (DR-4), so the
    map stays a function.

**C-2. Resolved.**
- `φ_W(s; r)` now counts any of the four applied settings `(x₁, x₂, y₁, y₂)`.
- The inequality `1[w₁ ≠ w₂] ≤ 1[any mismatch]` holds event by event under strict (U): with no
  mismatch, both uses have identical arguments. So `B − φ ≤ 0` under strict (U), and DR-3a cannot
  exclude falsely through setting errors.
- C-13 counts both wings.

**C-3. Resolved.**
- **(a) Bias.** The pass criterion is `UCB(|p − ½|) ≤ β` for each of the four sources.
- **(b) Hypothesis.** Mutual independence, together with independence of the marker, the event
  index and earlier records, is stated as a hypothesis. The χ² tests of it are necessary checks.

## 2. Does the β criterion certify β?

Yes, at the confidence level of C-1's weight, and only under hypothesis (b).
- Under (b), each source's bit is independent of the event index and of earlier records. Its
  probability `p` is therefore one constant for the whole run.
- A valid upper confidence bound then gives `P(|p − ½| > UCB) ≤ w₁`, where `w₁` is C-1's weight. A
  pass therefore implies `|p − ½| ≤ β`, except on an event of probability at most `w₁`.
- That failure probability sits inside the family-wise `α`, since C-1 is tested "at its weight".
- With independence across the four bits, each joint policy probability lies within `(½ ± β)⁴`. That
  is the quantity the inverse-probability weights need.
- What carries the certification is stationarity, that is, independence of the event index. Without
  it, an average-based bound would bound only the average deviation, not each event's conditional
  deviation, and the martingale correction needs the per-event deviation.
- r3 states stationarity as part of (b). That is sufficient, and §8.1's use of β is therefore
  certified conditionally, as stated.

## 3. Nothing else changed

The diff of r2 against r3 contains only the following:
- the title, the new *Scope of r3* block (r2's block is relabelled *Revision r2*), the status line
  and one inputs line;
- C-1: §5 table cell and bullet, DR-3a, the fallback, rows 9 and 10;
- C-2: §7.1 `φ`, C-13;
- C-3: C-1;
- O-a: DR-4's heading, Q-3's scope bullet;
- O-b: CC-1's full verdict vectors, the scope of CC-1, the synthetic sample size [DES], and (i)'s
  `Λ = 1`. I re-derived (iv)'s added `B = 0`, `Λ = ½` and `ns-disagree` in REV-2 §3, and they are
  correct;
- O-c: Appendix B. I checked the figures: `16 · ½ · 34 ≈ 270`, and `128/16 = 8`;
- O-d: §10.3's row list.

No decision rule, statistic, hypothesis or claim changed beyond these items.

## Optional

- §10.3's edited line runs past the column width; this is cosmetic.
- C-1(b) could name stationarity explicitly ("independent of the event index, hence one `p` per
  source"), since it is the part of the hypothesis that the β certification rests on.
