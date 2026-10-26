# Focused re-review: #911 a2_depth_v7, delta 61d90c4e..26683436 (c9580a0e, 26683436; local)

**Verdict: ACCEPT.** All of findings 1–8 and the nits are resolved. No new overclaim or misstated number.

## Finding status
1. Resolved. REPORT now proves the Hellinger lemma, writes out the joint chain rule for any adaptive member, and
   gives 1−Π(1−c_t) ≥ 1−e^−S ≥ S/(1+S). The verdict string says "proved; checked".
2. Resolved. REPORT gives the coupling argument at every depth, including t=1 and the empty initial seed state. The
   labels come from `union_sum` and the geometric-tail identity. The checks T ≤ gap ≤ partial sum < bound are exact.
   I matched all 19 tv/gap values (B=2 h≤8, B=3 h≤6, B=4 h≤5) with my own brute force.
3. Resolved: "public word" is defined as a function of the public record (the v6 rotation word).
4. Resolved. REPORT names the three controller specifics. The independent Born density-matrix engine is correct,
   (I+o n·σ)/2 with sequential projection, and it catches N4.
5. Resolved: the counterexample is called a sampler, "on this protocol only", and the review narration is gone.
6. Resolved. 340/24851 ≈ 1.37%, 330/14761 ≈ 2.24%, 24851/6376 ≈ 3.90 and 14761/4096 ≈ 3.60 are all verified, scoped
   "B=24, these two reads only, not a scaling law".
7. Resolved. a27e8d8f's parent is 70a8d97f, as stated. "Published" appears nowhere.
8. Resolved: the replacement is labelled.

Nits resolved:
- "only" is dropped.
- The 1/5-or-2/5 step is added.
- Σ sup_past d_t is used.
- The 1/80 derivation is checked: Σ 4^−⌈log2 t⌉ = 3/2, giving 3/320 ≤ 1/80.

## Checks
- Replay: normal and -O runs from empty dirs are byte-identical to result.json.
- SHA256SUMS: 5/5 OK. PLAN.md is unchanged since a27e8d8f.
- result.json changed only in class_statement (B range, counterexample block, two new proof strings), class_verdict,
  controls (one key renamed) and grid_sensitivity. Verdict, depths and the TV table are unchanged.
- Mutants: N4 is caught ("per-record Born mass from independent matrix engine"). N5 is caught ("union-bound label
  derived from the series").

## Residual nits (non-blocking)
- REPORT "Lower bound" bullet: S should read Σ_t inf_past d_t²/4 for adaptive members. The class paragraph's
  (h−1)·dist²/4 already uses the right quantity.
- REPORT line 3 exceeds the file's line width.
