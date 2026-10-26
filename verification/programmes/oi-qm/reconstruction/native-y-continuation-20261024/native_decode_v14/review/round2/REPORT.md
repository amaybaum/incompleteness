# rev910b re-review: #910 text correction 96b92f39 (on cd9390a0)

**Verdict: BLOCK.** The evidence is byte-identical and the counts are right. The block is owner requirement 1: three status surfaces state review-only results without attributing them to the review. Fixing this is text-only.

## Evidence (requirement 5): holds
- `git diff cd9390a0 96b92f39 -- '*checks.py' '*result.json' '*PLAN.md' '*PROVENANCE.json'` is empty, 0 bytes.
- Only six files changed: REPORT, HANDOFF, EQUIVALENCE, CHECKPOINT-CHECKS and the two SHA256SUMS.
- The v14 replay at 96b92f39 is byte-identical to result.json, both normally and with -O.
- The top-level SHA256SUMS verifies 349 of 349 files and the v14 SHA256SUMS 5 of 5. Their changed rows are exactly the changed files.

## Counts (requirement 2): accurate
- From result.json `readout_solution_counts`:
  - B, ¬B, D, ¬D, A⊕B⊕D and ¬(A⊕B⊕D) are all 0;
  - the total is 7464 over 78 readouts;
  - 8 of the 14 degree-one readouts succeed, with the stated counts.
- From my review's computation:
  - 64 affine f, 512–2016 laws each;
  - q10.A = x under 992 laws;
  - B alone s-free in 8 laws;
  - D alone depends on s on at least 4 contexts in every law.

## Findings
1. **Blocking: attribution missing (requirement 1).**
   - CURRENT-HANDOFF.md:105-106 says "(B alone is s-free in 8 laws)" inside the "Post hoc:" checker list.
   - CHECKPOINT-CHECKS.json:54 says "(B alone is s-free in 8)" without attribution.
   - EQUIVALENCE-OBLIGATIONS.md:64-65 says "more generally x XOR f(k) for each affine f … under a law depending on f" without attribution.
   - Fix: add "(separate review)", as REPORT:39-40,73 and HANDOFF:100 already do.
2. **Non-blocking: inconsistent review status.**
   - REPORT.md:12 says "Separate review of this checkpoint is pending", yet REPORT:39 and :73 cite "the independent review of this checkpoint".
   - HANDOFF:110 has "corrected text", which is revision-history voice (§A.33).
   - The cited computation is not retained on the branch.
   - Fix: name it as the separate-agent internal review, not yet retained, and cite its path once it is retained. Change the HANDOFF line to "Separate review is pending."
3. **Minor.**
   - REPORT.md:62 repeats itself: "No affine law with E identically 000. No solution has E identically 000." Drop the second sentence.
   - EQUIVALENCE-OBLIGATIONS.md:66 is 104 characters long, which breaks the paragraph's line wrap.

## Requirements that hold
- **Access (requirement 3).** Every surface calls q10 a private cell under Native A and not a permitted read: HANDOFF:103, REPORT:37,135-138, EQUIVALENCE:14,66 and CHECKPOINT-CHECKS. REPORT:139-142 states that no read, post-read law or carrier law is modelled. No surface introduces a new access rule or a reusable interface.
- **Quantifier scope (requirement 4).**
  - REPORT:40-44 says "for each … there exist … the law depends on f, and no single law serves every f".
  - HANDOFF:101-102 says "for each affine function f … some law gives".
  - EQUIVALENCE:64-65 says "under a law depending on f", and CHECKPOINT-CHECKS says "f-dependent law".
  - No sentence reads as a single law serving every f.
- **Status lines.** EQUIVALENCE:4-6 now excepts the unreviewed v14 group, and EQUIVALENCE:35-39 adds plan 36213be6, which predates 7f843073. Both are correct.
- **Voice.** No caps emphasis or reader instructions. Only the "corrected text" phrase in finding 2.
