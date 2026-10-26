# Independent review: #911 a2_depth_v7 (local a27e8d8f / 1949a902 / a3547ca8 on 70a8d97f)

**Verdict: BLOCK.** The controller-extension result is reproduced exactly by a separate engine. The class
statement does not hold as worded, and one control is described as testing more than it does.

## Blocking findings
1. **The class hypothesis is too weak for the class claim** (REPORT.md:1, :17-18, :93, :125; result.json `scope`;
   PROVENANCE `comparison`).
   - "Resets draw a fresh independent block of at most B fair bits per slot" allows a reset that also reads
     retained private registers. The v6 architecture retains every used seed.
   - Counterexample (`probes.py`): B fresh bits per slot, with interval decoding over all bits drawn so far.
     - Its conditional agreement law leaves 2^-B Z: 11/16 at B=2, 41/56 at B=3, 41/52 at B=4.
     - Union bound: T(h) <= (1/2)/(2^(B-1)-1) for every h when B >= 2.
     - Exact values at B=4: T = 0.0125, 0.0125, 0.01377, 0.01470, 0.01481 for h = 1–5. The memoryless 4-bit
       sampler reaches T(4096) = 0.689.
   - So line 125 misattributes the obstruction. The cause is a memoryless reset, not bounded per-slot freshness.
     The pooled bank does not separate these two.
   - **Safe fix:** state the hypothesis as "the post-reset carrier is a function of that slot's fresh block and the
     public record only, and responses depend only on carrier, public word and setting". Use that wording in the
     title, line 17, line 93, line 125 and the scope/provenance strings, then regenerate result.json and SHA256SUMS.
   - The executed controller satisfies this hypothesis: its reset ignores retained registers. So the extension
     verdict stands.
2. **The record-enumeration control does not cover the seeded controller** (REPORT.md:119-120; checks.py:358-364;
   PLAN.md:59-60).
   - `tv_records(lambda s: pb if s%2 else pa)` enumerates the assumed product law of agreement bits. It never
     propagates outcome records, poles or seeded resets, so it restates the claimed formula.
   - The only seeded test is h=2 on the M=8 grid.
   - My literal engine closes the gap: outcome records, actual ±pole counts and quantum Born law, h=1–10. It equals
     the product engine exactly, so the numbers are right.
   - **Safe fix:** propagate actual records and poles in the control, or describe it as an enumeration of the
     product formula.

## Minor findings
3. **REPORT.md:96-98.** The closed form is only checked for B ≤ 64, which is a finite check behind a universal
   claim. Add the proof: 4 ≡ -1 (mod 5), so 2^(B+2) ≡ ±1 (mod 5) for B even and ±2 for B odd, giving distance 1/5 or
   2/5 of 2^-B. I checked B=1–200.
4. **REPORT.md:100-101 and checks.py:305 (off by one).** The depth 28,147,497,671,065,601 counts h constrained reads.
   The class constrains only reads after the first, so the depth is 28,147,497,671,065,602 unless preparation is
   also constrained. Fix the number, or add preparation to the hypothesis.
5. **REPORT.md:77 and :104-105.** Class members may have history-dependent reset laws, so their reads need not be
   independent. Add the chain-rule step: BC(P,Q) <= Π_t sup_past BC_t ≤ (1-δ²/4)^(n). The claim holds with it.
6. **REPORT.md:3-4.** "Published before computation at a27e8d8f on #911" is false while the commits are unpushed.
   Say "committed before computation (15:17:55 vs 15:25:15 UTC)". The `published_plan_commit` key has the same issue.

## Nits
- REPORT.md:59 says "rounded display", but `display()` truncates. At h=256 the rounded value is …447, not …446.
- REPORT.md:102 "mainly from its M=16 grid" was not computed. My probe supports it:
  - W 16→40 at M=16: dA 2.963→2.922 (×1e-4);
  - M 16→32: dA → 0.760.
  Add that probe or drop the sentence.
- The REPORT.md:108 bound of 1/80 is proved only in a code comment (checks.py:324); add the line to the report. The
  exact Σd_t is 3/640.
- REPORT.md:138-141 runs `checks.py` by relative path, which cannot work from an empty directory; give its path.
  PROVENANCE `replay` omits `-I -B`.
- Voice: "no retained review yet" (line 3) and "no novelty is claimed" (line 32) are mild self-narration.
- Mutants M4 and M5 (certified-depth ±1) and M7 (Hellinger constant ×16) leave the checker green. The depths and the
  bracket constant have no computational control; my engine supplies an independent one.

## Independent values (review_checks.py, exact)
- v6 count digest 0637f008… matches.
- A(+) = A(−) = 13426743/2^24 and B(+) = B(−) = 13424725/2^24, with no zero responses.
- dA = 24851/83886080 and dB = 14761/83886080; both ≤ κ.
- Exact T(h):
  - T1 = 14761/83886080;
  - T2 = 2658683146379/7036874417766400;
  - T3 = 244938084610979995331/590295810358705651712000;
  - T4 = 24767723195574940618231305351/49517601571415210995964968960000.
- All 69 tabulated values (h = 1–64 and powers of two to 2048) match result.json's hex sha256 and its truncated display.
  For example, T(2048) = 0.010999882464.
- Every T lies inside the bracket, and T(3) is below the h=3 certificate.
- Depths: 1/10 → 7,486,900; 1/2 → 67,382,091; 9/10 → 606,438,812.
- Hellinger bound: d²/4 holds on 19,701 rational pairs (Le Cam gives d²/2).
- dist(24) = 1/83886080, and the coupling depth 8,388,608 is confirmed.
- Growing sampler: T = 1/320 for h = 1, 2, 4, 8, 12, using 138 bits.
- Fixed B0=6:
  - T(12) = 0.011050219194, T(256) = 0.049751479020, T(2048) = 0.139918379698;
  - certified depth 409,601.
- Bijection and independence: faithful for the executed reset rule, which is fresh, memoryless and sign-symmetric.
- Replay: the author checker is byte-identical to result.json under normal and `-O` runs from empty dirs (≈10 s).
  SHA256SUMS: 5/5 OK.
- Mutants: M1 (slot parity), M2 (grid order), M3 (sign control), M6 (MLR direction) and M8 (enumeration parity) are
  caught; M4, M5 and M7 survive.
