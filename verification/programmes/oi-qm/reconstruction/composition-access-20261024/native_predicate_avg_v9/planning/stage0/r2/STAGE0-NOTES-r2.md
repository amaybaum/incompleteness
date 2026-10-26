# Notes on the NP-AVG-1 Stage 0 plan, r2

These notes supplement `STAGE0-NOTES.md` (r1), which is unchanged. The SHA-256
values of the r2 design evidence and of the code runs are in
`npavg/stage0-design-r2/RUN-MANIFEST.json` and `RUN-MANIFEST.md`.

## The r1 parity error (R4)

r1's toy runs used L = 3, which put the Φ analogue (slices 2–3) and the p
analogue in the odd class while the pool was even. Φ therefore never covered a
pool tip in those runs. Two r1 numbers were artifacts of this:
- the parity-mutant differences, which the review found;
- the symmetric-radius difference (160 of 400).

r1's `symmetric` option also kept the parity test, so on the even class it
emptied the far cone instead of widening it.

The r2 re-runs use L = 4, with Φ, p and the pool all even.

## Hand-checked toy instances (C6)

The toy A pair is (n+1, n+2) = (3, 4), with toy n = 2.

1. **The axis pair** q1 = ((0,0,0), 6) and q2 = ((1,0,0), 5). They share the +x
   tip (2,0,0) on slice 4. q1's −x tip (−2,0,0) is outside q2's radius-1 cone,
   so q1 goes; then q2's tips are uncovered. Closure: ∅.
2. **The constraint block at c0 = (5,0,0).** It consists of top (c0, 5), its six
   neighbours on slice 4, and the centre (c0, 3). All 8 are retained.
   - Without the centre, L3′ leaves ∅: top's far tip, the centre, is free.
   - Without the centre, L3 leaves 7.
3. **The toy base context** (the empty record; port (0,0,−2); even port samples
   at slices 0 and 2).
   - **Under A:** (port, 0) is B type at depth 3. Its near tip (0,0,−5) on slice
     3 is free; its +z tip is q10, which Φ covers. So it goes. (port, 2) is B
     type at depth 1. Its tip (0,0,−3) on slice 3 is free, so it goes. Result:
     collapsed.
   - **Under G:** the port samples are in-frame and have no seed tip. Result:
     collapsed.

   The code agrees with all three cases (C6).
4. **The v8 base context** is derived in `STAGE0-PLAN-r2.md` §3, from the
   review, and checked at execution, before its computed value is read.

## Interpretation and method notes

- **Equivalent mutants.** On even-class contexts both "parity filter dropped"
  and "symmetric (parity-blind) radii" are equivalent, by PO1. The meaningful
  radius mutants are the parity-preserving ±2 offsets and "far cone deleted".
- **C7 and the near-only mutant.** C7 agrees with production on all 1,400 toy
  records under the near-only mutant. On this toy class far tips never decide a
  closure, and the near-only mutant is caught only by the planted block (C3).
  This concerns the toy class only.
- **Safeguard 2 (completeness)** combines three checks: C13's manifest and
  independent recount; C17's fixed-point verification with the reference code;
  and C7's agreement with the reference greatest self-supporting subset. The
  un-applied-elimination mutant (stop_after = 0) fails C17, C7, C3 and C6.
- **Safeguard 1 (soundness)** combines two checks: C15, exact, against
  `s0native.py`; and C18, an audit of every logged elimination against
  `s0ref.py`. Over-eliminating mutants fail C15 and C18: far cone deleted,
  radius −2 and wrong far tip.
- **S6 is a proof-check on Φ's reference structure.** Its positive control,
  v6's flag, shows the statistic can pass. Its negative control, the permuted
  thresholds, shows it rejects a wrong flag.
- **Literature (§8)** is listed from memory. Every item is to be read first-hand
  before any novelty statement (owner decision S9).
- **Not run:** anything on v8's configuration class. `s0geom.V8` raises
  PermissionError unless `authorized_v8=True` is passed, and nothing in the
  package passes it. The control suite checks the refusal.
