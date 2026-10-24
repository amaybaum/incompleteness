# Re-review: #911 a2_depth_v7, local 61d90c4e (on 70a8d97f; d981eff7/61d90c4e not yet pushed)

**Verdict: BLOCK (narrow).** Every number is correct, and the mathematics holds for the joint record law; I
re-derived it independently. What is missing is the written proof: two universal steps rest in REPORT.md on finite
checks or on a formula given without its derivation (finite → universal). Text fixes and one added check close it.

## Blocking findings
1. **Per-read Hellinger lemma: only a finite check backs a universal step** (REPORT.md:92-93; result.json `class_verdict`).
   - The class claim "for every fixed B" needs H²(p,4/5) ≥ (p−4/5)²/4 for every p in 2^-B Z and every B.
   - The report supports it only by "checked … on 1,706 rational pairs" (and checks.py:325 at B=24).
   - The verdict string also says "(distance formula verified B=1..200), so T(h)->1", which makes the finite check
     the premise.
   - **Safe fix:** add the proof. 2H² = (√p−√q)² + (√(1−p)−√(1−q))², and |p−q| = |√p−√q|(√p+√q) ≤ 2|√p−√q|.
     The same holds for 1−p and 1−q, so H² ≥ d²/4. Say "proved; checked B=1..200" in the verdict string.
   - Also write out the joint-law chain (lines 94-96):
     - BC(P_h,Q_h) = Σ_past √(P Q)(past)·BC_t(past) ≤ BC(P_{h−1},Q_{h−1})·sup_past BC_t, valid for any adaptive member;
     - TV ≥ 1−BC;
     - 1−Π(1−c_t) ≥ 1−e^{−S} ≥ S/(1+S).
2. **The counterexample's all-depth bound is stated, not derived** (REPORT.md:149; checks.py:567, :569, :600).
   - "T(h) ≤ Σ_t 2^(t−1)·2^(−tB)" is given with no argument. The code checks it only at B=4, against a hard-coded
     1/14, for h ≤ 16.
   - The B=2 and B=3 labels (1/2, 1/6) are strings with no computational control: my mutant N5 (1/(2^B−1)) stays green.
   - The argument holds, and it bounds the **joint** TV. Couple both laws through one uniform U, with the seed equal to
     U's leading bits. While the records agree they use the same cut. At read t (t=1 included: one cut 4/5, B fresh
     bits, empty initial seed state) they can first differ only if one of the 2^(t−1) depth-t cuts lies inside U's
     tB-bit cell. That has probability ≤ 2^(t−1)·2^(−tB), and the infinite sum is 2^−B/(1−2^(1−B)) = 1/(2^B−2).
   - **Safe fix:** put this paragraph in REPORT.md, state the initial seed state, and derive the label from the sum.
     Check T ≤ coupling gap ≤ partial sum for B=2,3 as well (I did: B=2 h≤8, B=3 h≤6, B=4 h≤5, exact).

## Minor findings
3. **REPORT.md:20, "public word", is undefined.**
   - The step into 2^-B Z needs it to be a function of the public record.
   - In v6 it is the rotation word since the last read, which public instructions fix (a2_efficiency_v6/REPORT.md:66-72).
   - **Fix:** define it there.
4. **The extension verdict rests on controller specifics** (REPORT.md:57-58); name them.
   - The executed reset is memoryless, per v6 REPORT:70-72. Seeded exhaustion checks this only at M=8, h=2.
   - A+ = A− and B+ = B− (computed).
   - Records and agreement bits correspond one-to-one.
   - Mutant N4 (pole sign frozen at + in `controller_record_enumeration`, checks.py:421) gives byte-identical output.
     Given sign symmetry, that enumeration therefore cannot detect pole propagation. Fix REPORT.md:161-163 to say so.
5. **REPORT.md:139-141: the counterexample is not a geometric controller.** It is a protocol-specific sampler that
   reads the quantum cuts, like the samplers at :128. Say so, and that it escapes the obstruction on this protocol only.
   Line 140 ("The independent review proposed it; …") is process narration that PROVENANCE already credits; drop it.
6. **Grid sensitivity (REPORT.md:69-70).** It is worded as single-step facts, which is acceptable. But "moves by about
   1.4%" holds for dA only (dB moves 2.2%), and "doubling M reduces it about fourfold" reads as a scaling law (3.9× and
   3.6×). **Fix:** "from M=16 to M=32 at W=16, B=24, dA falls 3.9× and dB 3.6×; for these two reads only."
7. **Provenance (REPORT.md:3-5; PROVENANCE `plan_commit_note`).**
   - "on #911 at 70a8d97f" reads as if the plan were on #911, but these commits are a local child of #911's pushed head.
   - "not published at that time" will read oddly once pushed.
   - **Fix:** "committed at a27e8d8f (15:17:55 UTC), a child of #911's head 70a8d97f, before 1949a902 (15:25:15 UTC)."
8. **Departures (REPORT.md:176-178).** PLAN.md:59-60 promised a seeded enumeration "for h<=12". The delivery is a
   per-slot seed-count enumeration, with seeding only at M=8, h=2. Label this as a replacement, not only as "not in
   the plan".

## Nits
- REPORT.md:121, "certifies T > 1/2 only for h ≥ …602": the depth is specific to the S/(1+S) rule. The product form
  1−(1−c)^(h−1) already crosses at ≈1.95e16 (my numeric calculation). Drop "only".
- REPORT.md:116 proof: add "so 2^(B+2)/5 lies 1/5 or 2/5 from the nearest integer".
- REPORT.md:97: say Σd_t is the coupling bound for the executed product law (in general, Σ sup_past d_t).
- REPORT.md:127: the 1/80 derivation is still only in checks.py:351.

## Owner requirements
1. Universality: the order (every B, every member, then h→∞) and the metric (joint complete-record TV against QM, one
   protocol) are correct. The bound depends on B only. The conditional laws lie in 2^-B Z under the stated
   hypothesis plus finding 3. The gaps are findings 1 and 3.
2. Counterexample: 11/16, 41/56, 41/52 and B=4 T(1..5) = 1/80, 1/80, 1763/128000, 120389/8192000, 24264001/1638400000
   are re-derived by my own brute force. The coupling gaps are 1/80, 9/640, 151/10240, 971/65536 and 77721/5242880,
   all ≤ the partial sums ≤ 1/14. The proof is missing from the report (finding 2).
3. Grid: finding 6.
4. Delta:
   - the record enumeration is real but weaker than worded (finding 4);
   - the depth …602 is minimal under its rule;
   - the distance proof is correct (B=1..300 checked);
   - depths 7,486,900, 67,382,091 and 606,438,812 and the coupling depth 8,388,608 are minimal;
   - "committed" is used, with finding 7;
   - the replay commands work.
5. Replay and mutants:
   - normal and -O runs from empty directories are byte-identical to result.json (17.5 s);
   - SHA256SUMS 5/5 OK; PLAN.md is unchanged since a27e8d8f; the PROVENANCE hashes match 70a8d97f;
   - the exact TV table is unchanged since a3547ca8 (it was verified in the first review);
   - first-review mutants: M1–M8 are all caught now (M4, M5 and M7 previously survived);
   - new mutants: N1, N2, N3 and N6 are caught; N4 and N5 survive (findings 4 and 2).
6. Voice: findings 5 and 7, and the nit on :121; no caps or history phrases otherwise.

Files: rereview2.py / rereview2.out (24 PASS, 0 FAIL, including 40 random adaptive class members with exact
joint-law bounds and certified BC chain rule); mutants/mk2.py and mutants/run_*.
