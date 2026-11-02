# Review of aa667c13 (PE-01 stage plan), parent 25e77a3c

File: `verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/PLAN.md`
(blob `b3988cc7`, the only file changed; tree `169d509e`). Reviewer: independent, read-only. Line numbers are PLAN.md
at aa667c13 unless prefixed. Corpus anchors read at `c37700ad`. `papers/` and `book/` are byte-identical between
`c37700ad` and `25e77a3c` (`git diff --quiet` passes), as the plan says at :5.

Spot-checks: `checks.py` and `checks_emb.py` in this directory, with exact integer and `Fraction` arithmetic and
outputs in `checks.out` and `checks_emb.out`. They check the plan's control facts only. They compute no
verdict-bearing PE-01 measurement.

## Verdict: BLOCK (narrowly)

The plan follows the accepted README and the owner's direction closely. Every mathematical fact I checked is
correct. The controls are mostly non-vacuous, and the decision rule is written as a rule.

Five required fixes (R1–R5) stand before code. Each is one to three lines:
- R1 and R2: the COUNTEREXAMPLE rule leaves two quantifiers open, and both change what qualifies;
- R3: one negative-control mutant cannot be computed as specified, except by the closed form it is meant to test;
- R4: one load-bearing invariant has no checkpoint;
- R5: K0 is left unspecified, or cannot be computed, for two of the four embedded subclasses, and a deterministic-only
  restriction biases K0 toward the favorable reading.

Once R1–R5 are fixed, the plan is ACCEPT WITH NITS.

## A. Mathematical facts: checked

| Claim (line) | Status | How |
|---|---|---|
| φ = τ_f∘κ_σ is a bijection (:14–18) | correct | κ_σ is fibrewise bijective over x, and τ_f is an involution fibrewise over h. Image counts verified for G_lin/filt/clk/dec, n = 3..8. |
| Y_t = f(h_{t+1}) (:21) | correct | Follows from the composition order. |
| (ℓ, L_p) observable; windows of ≤ n+1 symbols uniform (:52–53) | correct | ℓL^i = h_i for i < n (trivially rank n). X_{0:n} ↔ (x_0, s_1..s_n) = (x_0, L h_0), which is invertible because c_0 = 1. |
| p_n primitive, p'_n its reciprocal (:43–46) | correct | ord(z) = 2^n − 1 for all twelve. Reciprocals verified. Primitive counts 2, 2, 6, 6, 18, 16. |
| PC zero at K ≤ n, every class (:165–167) | correct, including the active embedded class | Exhaustive: every 𝒫ᵉᵐᵇ(m ≤ 2) observer (16 + 9216, active included), every F, n = 3, 4, K ≤ n. Max TV is 0. In general, x_{t+1} = x_t ⊕ a(v_{t+1}) ⊕ s_{t+1}, with s_{t+1} fresh and uniform for t < n. |
| PC firing values on G_dec, K = 1 (:168–175) | correct | Record law {00: ½, 11: ½}. U ½; B1 ½; B2 at λ = 1: 1 − ¾ = ¼; B3 ½; B4 at d = 1: ½; 𝒫ᵉᵐᵇ(1) witness Pr_P = 1, Pr_Q = ½, so ½. |
| NC-1: TV = max(0, 1 − 2^{n−K}) (:177–178) | correct | Exact for n = 3..6, both siblings, K ≤ 3n+3. |
| NC-2: LC ≤ n+1 surely; adv = 1 − Pr_Q[LC ≤ n+1] (:182–183) | correct | Pr_P[LC ≤ n+1] = 1 for every enumerated case. |
| LC count N_N(0) = 1, N_N(L) = 2^{min(2L−1, 2N−2L)} (:124) | correct | Matches enumeration for N ≤ 14. Also matches, for N ≤ 59 and N = 255, 256, 1021, an independent Markov-chain DP on the Berlekamp–Massey length process (see N3). |
| 16 / 9216 observers; 256 F at m = 2 (:154, :288) | correct | 2!²·2² and 4!²·2⁴; 2^{2^3}. |
| WHT exact for K ≤ 23 (:123) | correct and feasible | 2^24 int64 entries. Counts are ≤ 512. |
| Affine-hull lower bound for K > 23 (:123) | correct | It is exact for G_lin, G_dec and G_tape, where every bias is 0 or ±1 (N9). |
| B4: adv ≥ 2^{−d} (:126) | correct | Pr_P[q = 0] = 1. wt(q) ≥ 2^{N−d} for nonzero q ∈ RM(d, N), so Pr_Q[q = 0] ≤ 1 − 2^{−d}. Monotonicity in K holds. |
| MO: "B4 d = 1 exists iff B1 has a bias-±1 test" (:213) | correct, both directions | q = c ⊕ ⊕_T X_t vanishes on supp iff D_T is constant there, with T ≠ ∅ because q ≠ 0. |
| MO: 𝒫ᵉᵐᵇ(m) ≤ 𝒫ᵉᵐᵇ(m+1), K0 ≤ K1 forms | correct | Idle-bit embedding; max–min ≤ min–max. |
| K_max ≥ 2L_max (Fine–Wilf calibration) | holds | L_max = 2^n − 1 (lin/filt/dec) and 10, 19, 40, 85, 169, 337 (clk). K_max = 4(2^n − 1) ≥ 2L_max − 2 everywhere. |
| K_cx = ⌊ℓ_med/2⌋ | well defined | 3, 7, 15, 31, 63, 127 (lin/filt) and 5, 9, 20, 42, 84, 168 (clk). For G_lin at n = 3, K_cx = n, so PC already forces 0 there and the window is empty. That is harmless; it may be noted. |

Anchors (`Structure.md:1256`, `Main.md:496–500`, `:544–560`, `:576`, `:708` posit (iv), `Computation.md:15`) are used
correctly. The exception is Main:560 (N7).

## B. Required findings

**R1. The knowledge level of a COUNTEREXAMPLE witness is not stated.** PLAN.md:234–243.
- Condition (d) evaluates adv^pred_O(φ, K) for an O that may be chosen after φ is known. That is a K1 selection. The
  README requires every use to name its knowledge level (README.md:131), and this is the plan's most consequential use.
- *Fix:* add to (d): "O may depend on φ (K1); the verdict also reports whether the same O is a witness for every φ in
  its family 𝔉 (K0, worst case)." Alternatively, restrict to K0. Either way, say which (see §D, Q6).

**R2. The readout at time K is time-dependent, and the evaluation time acts as a free clock.** PLAN.md:142, :146–149,
:243, :327.
- The plan argues that the observer's rule must be time-invariant, and that a time-dependent rule needs a clock that
  the footprint counts (:146–148).
- But the readout `out ← out ⊕ 1[(v_K, x_K) ∈ F]` (:142) is applied only at step K. So the composite is not
  time-invariant, and the plan does not count the clock that would trigger it.
- Together with (d) at a single K, chosen by the analyst after the curve is computed, a witness can be an observer
  whose prediction is good at one isolated time it cannot itself identify. Operationally, it has not predicted.
- *Fix:* preregister one of the following:
  - (i) the footprint of a single-K witness counts ⌈log₂(K+1)⌉ clock bits, and EX1/IM3 run on the clocked composite;
  - (ii) the witness's prediction advantage must hold at every K' in a stated window, for example [K − w, K] with w
    fixed now, or as a time average over it;
  - (iii) drop the embedded `out` bit, treat F as a predicate on the visible state at K, and say explicitly that the
    evaluation time is supplied by the analyst and not charged.

  Option (iii) is admissible only as an owner decision (Q5/Q7). Also make :149 consistent with whichever is chosen.

**R3. The `G_tape(K_max)` mutant cannot be computed as specified, except by the closed form it is meant to test.**
PLAN.md:33–39, :49, :179, :198.
- For n = 8, G_tape(K_max) has 2·2^1020·1021 states. Neither of the following is possible:
  - EX1 "all generators… at every n" (:198) by image count;
  - enumerating the record law at K up to 1020.
- The only way to "compute" adv = 0 there is to use the fact that the record is uniform. That reproduces the claimed
  formula, which the Code Review Rules (exactness and controls) make a vacuous control.
- Separately, the law of x_0 under G_tape is unstated (:49). With x_0 = 0, U would fire at K = 0.
- *Fix:*
  - use G_tape(N) with N = K, evaluated by full enumeration through the actual bijection for K ≤ K_tape, with K_tape
    fixed now (for example 20). n + 1 ≤ 9 < K_tape, so the mutant still covers the horizons where NC-1 and NC-2 fire;
  - state "x_0 uniform, independent of the tape";
  - run EX1 on G_tape(N) for N ≤ K_tape;
  - add the plan's honest scope: the mutant is checked only for K ≤ K_tape.

**R4. "No hidden-sector access" has no checkpoint, and EX7 is vacuous.** PLAN.md:144–145, :204, :97–99.
- The invariant that the observer's maps act as the identity on C_H, and that ρ, a and F read only (v, x), is what
  makes an observer embedded. The §A.41 table does not measure it.
- EX7 checks that the joint prior is μ ⊗ δ_{v0}, which is true by construction for every implementation, including a
  wrong one.
- *Fix:* add a checkpoint, for example EX8: "for every composite step table, the h-component is the identity, and the
  (v, x, out)-component is constant across h for each (v, x, out); exhaustively at n ≤ 4, and for every
  verdict-bearing witness." Then define measurement independence (EX7) as EX8 together with the prior factorisation.

**R5. K0 for the larger embedded subclasses is unspecified or cannot be computed, and the deterministic-only
restriction biases it.** PLAN.md:92, :155–156, :288–289, :263.
- §8 fixes K0 only for 𝒫ᵉᵐᵇ(m = 2): "all 256 F". For passive m = 3 there are 2^16 sets F per observer, over about 3×10^5
  conjugacy classes. For linear-filter m = 4 there are 2^32 sets F. K0 over all F, as defined at :88–90, is not
  computable there. If left open, K0 for those classes becomes a post-hoc choice.
- K0 worst case over deterministic tests (:92) is only a lower bound on the randomized-test worst case.
  max_w min_φ Σ_D w_D Δ_φ(D) can exceed max_D min_φ |Δ_φ(D)|: with two φ and two tests, each test firing on one φ,
  the deterministic value is 0 and the mixture's is ½.
- So a K0–K1 gap (T3, tagged candidate-NEW at :252) can be an artifact of the restriction, and it falls on the
  favorable side for indistinguishability. The average-case form is not affected, because a pure test attains its
  maximum.
- *Fix:*
  - state K0 per subclass now. For example: K1 only for m = 3 and linear m = 4, or K0 restricted to prediction tests χ,
    with the restricted class named;
  - label the deterministic worst-case K0 a lower bound;
  - require any worst-case T3 gap claimed as candidate-NEW to use either the average-case form or the randomized
    value, which is an exact rational LP over a complement-closed test class at the m ≤ 2 sizes.

## C. Non-blocking findings (nits)

**N1. The limitation stated for NC-2 is false: a separating mutant is already in the plan.** PLAN.md:185–186.
- G_filt keeps the support reason: its records are injective, with |supp| = 2^{n+1}, so U's NC-1 TV is identical.
- It removes the LC reason. B2 at λ = n+1 drops from 0.67–0.9999 on G_lin to 0.008–0.12 on G_filt, over n = 4..7 and
  K ∈ {2n+2, 2n+6, 4n}; see `checks.out`.
- The converse separation (LC deficit kept, support restored) is impossible for N > 2(n+1), because
  |{LC ≤ n+1}| < 2^{2n+3}. So low LC implies a support deficit.
- No verdict is unprotected today. B2 feeds only COVERED tags and T3, not COUNTEREXAMPLE, and IM1/IM2 validate BM and
  Pr_Q independently. Still, the stated limitation should be corrected.
- *Fix:* replace :185–186 with "Specificity: on G_filt, U's NC-1 value must equal G_lin's at every K where both records
  are injective, and B2 at λ = n+1 must be strictly smaller than on G_lin there. The converse separation is impossible
  (LC ≤ n+1 bounds the support)."

**N2. B4's support-counting horizon should be stated, so the COVERED-corpus tag is mechanical.** PLAN.md:126, :250.
- Whenever Σ_{i≤d} C(K+1, i) > 2^{n+1}, an annihilator of degree ≤ d exists for any generator, purely by counting.
  For d = 2 this happens at K = 5, 7, 10, 15, 22, 31 for n = 3..8; for d = 3 at K = 4, 5, 7, 8, 11, 14.
- Beyond that horizon, B4 firing is implied by support size.
- *Fix:* add this bound to §3, and tag B4 results at or beyond it COVERED-corpus.

**N3. Remove the cited-only dependence for N > 20.** PLAN.md:124, :206, :300–303.
- Pr_Q[LC ≤ λ] has an independent exact route. Under fair bits, the BM discrepancy is fair and independent of the
  past, so the length process is a Markov chain: L stays, or becomes i+1−L when 2L ≤ i.
- The resulting DP agrees with the closed form at every N tested, up to 1021.
- *Fix:* make IM2 "closed form = enumeration for N ≤ 20, and = DP for every N used". The DP's own premise is then
  cross-checked by enumeration for N ≤ 20.

**N4. The B4 exact maximum needs its weight method stated.** PLAN.md:126.
- Weights of quadratics follow from the Dickson rank. For d = 3, the weight of a cubic in up to 64 variables is not
  computable by enumeration.
- *Fix:* "exact maximum for d ≤ 2 via Dickson; for d = 3 only where K+1 ≤ 24 (enumeration), otherwise the 2^{−d}
  bound."
- Also define K0 for B4: q annihilating ⋃_φ supp P_φ.
- Optionally, extend IM5 to d = 3 at K ≤ 3.

**N5. U's average-case K0 is missing.** PLAN.md:92 promises both forms, but U (:114–117) gives only the worst case.
- *Fix:* report the average case as the interval [TV(E_ν P_φ, Q), E_ν TV(P_φ, Q)], exact only where the ends
  coincide.

**N6. G_tape doubles as the independent check of Q_p.** PLAN.md:77–79.
- For K ≤ N, P^{G_tape}_p = Q_p for every observer, active included. This is the only check of the Q-side computation
  that is independent of the plan's own Q code.
- *Fix:* say so in the IM rows, as IM6, once R3 is applied.

**N7. The use of Main:560 inverts its resource accounting.** PLAN.md:146–148, :327.
- Main:560 justifies "one dynamics", but its point is that the program is "paid for as an initial condition": a
  read-only program register counted as state.
- The plan puts the observer's tables (ρ₀, ρ₁, a, F) in the dynamics and charges nothing for them.
- *Fix:* cite :560 for time-invariance only. State the modelling choice: tables are part of φ', not state. Record
  each witness's table size in bits beside its footprint.

**N8. The universal form needs its realization scope in the verdict text.** PLAN.md:234–236, :271–272.
- "Every finite reversible realization" is broader than the corpus's embedded-observer setting.
- Condition (a) checks only T-level (C1). C2–C4 are neither checked nor stated for G_lin, G_filt and G_clk.
- *Fix:* the generated verdict names the conditions the witness's realization satisfies ("T-level (C1); C2–C4 not
  checked"), so the refuted statement is exactly the one tested.

**N9.** PLAN.md:123: note that the affine-hull method is exact for G_lin, G_dec and G_tape. PLAN.md:69 refers to "a
class's row in §3" for caps, but the m = 2 active cap K ≤ 255 is in §8 (:288). Move it to §3, or refer to §8.

**N10. The CI trigger needs to be stated (§A.43 item 4).** PLAN.md:293.
- If the job is `push`-triggered, pushing the code commit launches it without approval.
- *Fix:* "the job is `workflow_dispatch`-only".
- Also state that CI shard outputs are committed as structured JSON, with commit, recipe and run id (§A.42 item 1),
  and are never relied on as logs.

**N11. Literature before any candidate-NEW tag (Step 4; §A.31).** Passive 𝒫ᵉᵐᵇ(m) are width-2^m oblivious read-once
permutation branching programs. Two results bear directly on T3 and on the candidate-NEW tag (:252), and the rule
should require them to be checked first:
- RSV 2013's Fourier-mass bound for regular branching programs, under which small-bias sources fool them;
- the AGHP LFSR small-bias construction, a random feedback polynomial plus a random seed, which is close to the K0
  average over 𝔉_lin.

  *Fix:* add both to §9 as "read before any candidate-NEW tag". For AGHP, verify the details before use; I did not
  confirm the construction's exact polynomial distribution.

  - Alon–Goldreich–Håstad–Peralta, "Simple constructions of almost k-wise independent random variables", Random
    Struct. Algorithms 3(3) (1992).
  - Width-2 small-bias results: Bogdanov–Dvir–Verbin–Yehudayoff 2013.

  Also list now the closed forms that the COVERED-literature tag (:251) may cite: B1 K1 at n+1, BM at 2·LC, the N2
  counting bound and NC-1. Otherwise the tag is assigned post hoc.

**N12. "Milestone" at §6.7.** PLAN.md:264. The README's first milestone is PE-01 and PE-02 together (README.md:265).
- *Fix:* call §6.7 the "stage outcome", and say the milestone closes after PE-02.

**N13. Runtime.** PLAN.md:288–289.
- The m = 2 active sweep at n = 8 is about 9216 × 48 φ × 512 seeds × 255 steps ≈ 6×10^10 elementary updates. That is
  hours in pure Python and plausible only if vectorised over seeds and observers.
- The m = 3 conjugacy enumeration over S₈² (1.6×10^9 pairs) needs a canonical-form method. A BFS labelling of the
  component reachable from v₀ suffices, because unreachable states never carry mass.
- The 3× stop rule (:292) covers this. Naming the vectorisation in the plan would make the estimate credible.
- The local row (< 10 min) is plausible: the m ≤ 2 sweep at n = 3, 4, K ≤ n took 10 s pure-Python here.

**N14. Unattained horizons.** PLAN.md:101–103. Define the value of K_δ when adv < δ throughout, for example `null`
with the scope K ≤ K_max. That keeps a favorable reading from being encoded as a number.

## D. Faithfulness to the accepted README

- **Three notions:** kept distinct.
  - U and the record entropies are notion 1.
  - The B classes against a fixed Q are a pseudorandomness-type notion 2.
  - 𝒫ᵉᵐᵇ is notion 3.
  - :159–160 and :275 explicitly refuse any identification.
- **K0/K1:** the test is chosen once, before φ (:88–89, K0 checkpoint :214). Both forms are given, apart from N5 and
  R5. K2 is never used.
- **Embedded realizability: drift in the default.**
  - README.md:155–159 says an observer counts against the claim *only if* its memory fits its share of C_V.
  - The plan enlarges C_V per observer, which is necessary, since C_V = {0,1}. It then makes the size comparison a tag
    (:243, §10 Q3), not a condition.
  - The README's first assumption-watch item thus becomes a label by default. It is flagged for the owner, which is
    right, but the plan should say in one line that this is a reading of README.md:155–159 (see Q3).
- **Milestone and outcome rule:** "one or more of", with VOID taking precedence and OPEN otherwise (:221–223, :264–265).
  This matches README.md:268–277, apart from the label (N12).
- **Authority limits:** :267–277 matches README.md:252–261.
- **Owner's direction:** satisfied.
  - Knowledge levels, distinguishers, reference law and horizons are fixed before code.
  - Bounded tests come first, and U is calibration only (:9–10).
  - "Which restrictions and for how long" is answered by K_zero, K_δ and the full curves.

## E. Decision rule

- It is a rule, not a list of expected numbers.
  - δ, δ_cx, K_max and the K_cx formula are fixed before computation.
  - The only expected numbers are the control values. That is what controls are for, and each is proved independently.
  - T1–T3 are posed as questions.
- The COUNTEREXAMPLE criterion is not immunizing. It can fire, and its exclusions (recurrence scale; distinguishing
  only) are stated in advance with reasons.
- It is not yet fully well posed: R1 (knowledge level) and R2 (free clock).
- Prediction against distinguishing: ch18:114's "unpredictable" is matched literally by next-symbol prediction, which
  is correct.
  - The same sentence's second clause ("the cryptographic properties depend on unpredictability") is about
    indistinguishability.
  - For 𝒫ᵉᵐᵇ, Yao's reduction does not stay inside the class, because it needs a hybrid position and random
    completions. Distinguishing witnesses therefore bear on that clause and not on the first.
  - Reporting them as measurements is correct. They should be labelled as bearing on the second clause (Q2).
- The footprint question is flagged for the owner (§10 Q3), not silently decided. The clock part of the footprint is
  silently decided (R2).

## F. Literature (§9)

All three flagged citations exist with the stated details:
- Gustavson, "Analysis of the Berlekamp–Massey linear feedback shift-register synthesis algorithm", IBM J. Res. Dev.
  20(3):204–212 (1976).
  - I did not see its text, so its attribution of the length-count formula is unconfirmed.
  - N3 removes the need to rely on it.
- Gollmann and Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989),
  doi:10.1109/49.17716.
- Reingold, Steinke and Vadhan, "Pseudorandomness for regular branching programs via Fourier analysis", RANDOM 2013,
  LNCS 8096, pp. 655–670, arXiv:1306.3004.
  - Its subject (oblivious read-once regular and permutation branching programs) is exactly the passive 𝒫ᵉᵐᵇ class, so
    it is more than positioning (N11).

Cited results are cited, not rederived. Where the verdict path uses one, it carries an independent check: IM1 for BM,
IM2 for the count, and the RM bound is proved inline above.

## G. Overclaim, prejudgement and register

No overclaim or prejudgement found:
- Favorable readings carry their enumerated scope (:255–257).
- §7's non-claims are complete.
- "Questions, not expectations" (:258).

Register: the status capitals (VOID, OPEN, …) are labels in a verification file, so §A.33 does not apply. No
manuscript text and no internal-ledger vocabulary aimed at readers.

## H. The §10 design questions (recommendations; the owner decides)

§10 lists five items, not seven. I comment on those five, and on two more that the findings above show belong in §10.

1. **Q fixed and uniform; class 𝒬 deferred.** *Recommend: keep.* The class forms only matter for the comparison with
   HILL and metric pseudoentropy, which is PE-02's question.
2. **Prediction-based COUNTEREXAMPLE.** *Recommend: keep.* Also label distinguishing witnesses as bearing on ch18:114's
   second clause (the cryptographic-properties inference), and keep them out of COUNTEREXAMPLE (§E).
3. **Footprint as a tag only.** *Recommend: make it an admissibility condition.* A COUNTEREXAMPLE requires total
   footprint (memory + clock, per R2, + output) ≤ n. Large-regime witnesses are reported as measurements.
   - This is the README's embedded-realizability rule (README.md:155–159) and its first assumption-watch item.
   - n is the natural threshold: at footprint n+1 a window-holding observer matches U's K1 predictor, which is
     perfect at K = n+1 on G_lin.
4. **δ_cx = 1/8, K_cx = ⌊ℓ_med/2⌋.** *Recommend: keep.* Add the R2 window, or the clock charge.
5. **Readout costs one bit, no workspace.** *Recommend: charge the clock* (R2 option (i)), and record the table size
   (N7). Otherwise the evaluation time is free information.
6. **(Proposed) Knowledge level of a witness.** *Recommend:* a K1 witness qualifies, following the Kerckhoffs
   convention the README adopts as the cryptographic default (README.md:112). The verdict also reports K0 status (R1).
7. **(Proposed) Randomized tests at K0.** *Recommend:* use average-case K0 for T3, or compute the randomized
   worst case by exact LP at m ≤ 2. Label the deterministic worst case a lower bound (R5).

***

## Addendum: re-check of 6e5db447 (tree ee07adef, parent aa667c13, PLAN.md only, +144/−54)

Line numbers in this addendum refer to PLAN.md at 6e5db447. New exact checks are in `checks2.py`, with output in
`checks2.out`.

### Verdict: BLOCK (narrowly)

All of R1–R5 and N1–N14 are addressed. Two new definitions would make the stage VOID by construction:
- **S1:** EX8 as worded, which follows my own R4 wording.
- **S2:** the strict G_filt specificity rule at n = 3, 4.

Each fix is one line. With S1 and S2 fixed, the plan is ACCEPT WITH NITS.

### Status of R1–R5 and N1–N14

| # | Status | Where |
|---|---|---|
| R1 knowledge level of a witness | resolved | :279–280. The witness is K1, and its K0 status is reported. |
| R2 readout time / clock | resolved | :156–159 and :283 charge the clock; the window is in (d) at :275–276. Both options are adopted, which is stricter. |
| R3 G_tape | resolved | :40–42 (N = K, K_tape = 20, x_0 uniform, full enumeration); EX1 at :231; NC caps at :209–211. |
| R4 hidden-access checkpoint | resolved in intent, but the wording is wrong | EX8 at :237 (S1); EX7 at :238 now builds on EX8. |
| R5 K0 per subclass, deterministic K0 as a lower bound | resolved | :95–97, :178–186, :309–310, :323–324. Nit A3 on the LP's cost. |
| N1 G_filt specificity | resolved in intent; the rule fails at n = 3, 4 | :216–219 (S2) |
| N2 B4 counting horizon | resolved | :137–139, :299–300 |
| N3 DP for the LC count | resolved | :240, :370–371 |
| N4 B4 weight method, B4 K0, IM5 d = 3 | resolved | :135, :243 |
| N5 U average-case K0 | resolved | :123–124 |
| N6 IM6 | resolved | :244 |
| N7 Main:560, table size | resolved | :163–167. The formula is correct (A2). |
| N8 realization conditions | resolved | :287–288 |
| N9 affine hull exact; cap cross-reference | resolved | :132, :72, :179 |
| N10 workflow_dispatch, JSON | resolved | :357–360 |
| N11 literature, closed-form list | resolved, with a gap | :301–312, :387–394 (A4) |
| N12 stage outcome / milestone | resolved | :325–327 |
| N13 vectorisation, BFS canonical form | resolved | :350–351 |
| N14 null K_δ | resolved | :108–109 |

### Required

**S1. EX8 fails on every implementation (:237).**
- "For every composite step table, the h-component is the identity" cannot hold. The composite round includes φ,
  which changes h and reads it by design.
- As written, EX8 fails on every implementation, so the stage is VOID by construction. My R4 fix text carried the
  same wording; the defect is mine.
- *Fix:* "For each observer map, as a table on C_V′ × C_H: the ρ-step, the a-step, the clock tick and the readout. The
  h-component is the identity, and the (v, clk, x, out)-component is constant across h. Also, φ acts as the identity
  on (v, clk, out)."
- The last sentence is the converse non-interference: the generator never touches the observer's registers.

**S2. The strict specificity rule fails on correct code at n = 3, 4 (:216–218).**
- "At every K where both records are injective… B2 at λ = n+1 must be strictly smaller on G_filt" fails on correct
  code, with exact equality:
  - n = 3, K = 5: both advantages are 5/64;
  - n = 4, K = 6: both are 5/128.
- At those K, both are the first K with both records injective. The rule holds strictly at every other injective K
  checked (up to 4n+5, n = 3..8).
- *Fix:* "≤ at every such K, and < at some such K, for each n".

### New definitions checked

- **A1. Window, (d) at :275–276.**
  - Well defined: the same O and χ, adv^pred ≥ 1/8 exactly at every K′ ∈ [K−3, K], K ≥ 3, and K ≤ K_cx bounds the
    whole window.
  - For G_lin, PC forces K − 3 ≥ n+1, so K ≥ n+4. That is correct and implicit. For G_filt and G_clk, no PC zero is
    claimed, so it does not apply there.
- **A2. Clock ⌈log₂(K+1)⌉.** Correct. A trigger at step K needs K+1 counter values, and a counter mod 2^c is a
  permutation, so the composite stays bijective. Two nits:
  - the charge is an upper bound, and it overcharges a witness whose own memory already realizes the trigger (for
    example a cyclic ρ₀ = ρ₁). Allow the footprint of an explicit clocked composite instead, when that is smaller and
    verified by EX1, EX8 and IM3. Otherwise the overcharge leans toward the favorable reading;
  - the table size (:167) omits the trigger constant, which is ⌈log₂(K+1)⌉ bits.
- **Table size 2m·2^m + 2^m + 2^{m+1}.** Correct as raw table bits: two permutation tables of 2^m entries of m bits,
  plus a, plus F. That gives 10, 28, 72 and 176 bits for m = 1..4.
- **Claim: footprint ≤ n with the clock admits only K < 2^{n−m−1} (:407).** Correct: m + ⌈log₂(K+1)⌉ + 1 ≤ n iff
  K + 1 ≤ 2^{n−m−1}, which was verified exhaustively. But the statement is incomplete for the owner. Together with the
  window (K ≥ n+4 on G_lin) and K_cx, the admissible region is:

  | n | admissible K, footprint ≤ n |
  |---|---|
  | 3, 4, 5 | none, for every m |
  | 6 | m = 1: [10, 15] |
  | 7 | m = 1: [11, 31]; m = 2: [11, 15] |
  | 8 | m = 1: [12, 63]; m = 2: [12, 31]; m = 3: [12, 15]; m = 4: none |

  Consequences:
  - Under that option, the passive m = 3 sweep (CI, n ≤ 6) and the linear m = 4 sweep can never yield a
    COUNTEREXAMPLE.
  - "No witness found" would be partly structural. That is a favorable reading, and it must be reported with this
    table.
  - For comparison, a threshold of n+1 = log₂|C_V × C_H| (the whole generator) gives:
    - n = 5, m = 1: [9, 15];
    - n = 6: m ≤ 2;
    - n = 7: m ≤ 3;
    - n = 8: m ≤ 4, with [12, 15] at m = 4.
  - *Fix:* print this table in §10 item 3 beside the K < 2^{n−m−1} sentence, so the owner decides with the full
    consequence. My recommendation on item 3 now reads: admissibility, with the threshold (n or n+1) the owner's choice
    in light of this table.
- **A3. LP-randomized K0, m ≤ 2, n ≤ 6 (:182–184).** The formulation is correct.
  - With a complement-closed class, max_w min_φ |Σ_D w_D Δ_φ(D)| = max over sign patterns s of the LP
    max_w min_φ s_φ Σ_D w_D Δ_φ(D).
  - s and −s give the same value, so 2^{|𝔉|−1} ≤ 32 LPs suffice. |𝔉| = 2, 2, 6, 6 for n = 3..6.
  - The primal has 9216 × 256 ≈ 2.4×10^6 test variables per K, for K ≤ 255, in exact rationals. It is not costed in §8.
  - *Nit:* state the dual form: |𝔉| variables, and per observer the inner maximum over F is a sum of positive parts.
    Cap its K range, for example at K ≤ K_cx, and add a §8 row.
  - No verdict is at risk, because T3 also accepts the average-case form.
- **B1 K0 beyond K = 23 (:132).** "The affine hull of ⋃_φ supp P_φ" requires the same constant on every support. But
  adv_{D_T}(φ) = ½ whenever D_T is constant on each support separately, because of the absolute value. The method is
  still a valid lower bound, and it is exact for G_lin, whose supports are linear subspaces. *Nit:* use T in the
  intersection over φ of the annihilators of each support's direction space.
- **A4. Tag gap (:301–312).** The COVERED-literature list is closed ("no other closed form"). But §9 requires reading
  RSV, AGHP and BDVY before any candidate-NEW tag, and no rule says how to tag a result one of them covers.
  *Fix:* "a candidate that a §9 result covers is tagged COVERED-literature, citing it".
- **IM6 / NC caps.** The K ≤ 12 and K ≤ 20 caps are stated and costed. EX1 on G_tape(20), with about 4.4×10^7
  states, is feasible vectorised.

### Prejudgement, vacuity, §10

- **Prejudgement:** none found. T1–T3 are still questions, and favorable readings carry their scope.
- **Vacuous controls:** none. EX7 now rests on EX8. G_tape is enumerated, never taken from the closed form. The two
  defects (S1, S2) go the other way: controls that fail on correct code.
- **§10 (:396–417):** neutral. Each item gives the default in force and the review's recommendation, marked as such
  and attributed. The owner decides. The recommendations are reproduced faithfully. Two exceptions:
  - item 3 needs the admissible-region table (A2);
  - item 5's sentence "makes it free information" is the review's rationale. It sits under the recommendation, which
    is acceptable.

### The owner's two confirmations (re-check of 6e5db447, continued)

**(a) Is the footprint (memory + clock + output) applied consistently? Not yet.** It is applied consistently for
witnesses, but not wherever a footprint is used.

- **Consistent:**
  - :158–159 counts the clock in a verdict-bearing witness's footprint;
  - :283 prints m + ⌈log₂(K+1)⌉ + 1;
  - :285 bases the regime tag on that printed value;
  - §10 item 3 (:406) uses memory + clock + output.

  For a window witness, the clock is sized by the top of the window K, which covers every K′ ≤ K, so that is
  consistent too.
- **Inconsistent or unmeasured:**
  - :142 still defines "the observer's footprint" as m+1 bits, and :157 leaves the evaluation time uncharged in the
    reported curves. So "footprint" means two things in the plan.
  - Nothing measures the footprint. It is a formula in the verdict text. EX1, EX8 and IM3 run on the clocked composite,
    but no checkpoint reads its register widths.
- **S4 (required).**
  - Rewrite :142–143 as: "memory + output = m+1 bits. Every footprint-bearing statement uses the footprint
    m + ⌈log₂(K+1)⌉ + 1: tags, admissibility, any bounded-resource claim, and any statement of the form 'for observers of
    footprint ≤ f'. The reported curves are indexed by m, with the evaluation time uncharged, and are labelled so."
  - Add a §A.41 row **FP**: the footprint printed for a witness equals the total bit width of the visible registers
    of its clocked composite, as checked by EX1/EX8/IM3, minus the system bit. It is computed from the composite, not
    from the formula, and compared with the formula.

**(b) Is the four-step window enforced by a named checkpoint? No.** Condition (d) at :275–276 is prose.
- No §5 row names the window, and VG (:252) only regenerates the verdict from the JSON.
- So a checker would print a COUNTEREXAMPLE from whatever `verdict.py` computes, without any check that the
  advantage was measured at all four K′.
- **S3 (required).** Add a §A.41 row **CX**. For every candidate witness, the JSON records:
  - the exact adv^pred_O(φ, K′) for each K′ ∈ [K−3, K], computed by full-state simulation of the clocked composite
    (the IM3 path);
  - K_cx(φ);
  - the footprint (FP);
  - EX6.

  The checker evaluates (a)–(e), and the footprint admissibility condition, from those fields alone, and prints a
  COUNTEREXAMPLE only if all of them hold.

  Self-test: each of three mutant witnesses must be refused and reported as a measurement:
  - one K′ in the window at 1/8 − 2^{−K−2};
  - footprint n+1;
  - K = K_cx + 1.

  A refusal is caught only when it fails on that condition.

### Owner decisions against the plan as written

| # | Decision | Conflict with 6e5db447? |
|---|---|---|
| 1 | Footprint is an admissibility condition; unrestricted results are also reported | **Yes, by design.** :285 and §10 item 3 make it a tag. To implement it, add (f) "footprint ≤ θ" to the COUNTEREXAMPLE conditions. Large-regime witnesses and the uncharged curves become the comparison results. The threshold θ is not fixed by the decision. §10 item 3 recommends θ = n; θ must be fixed in the plan before any run (decision 4). "Bounded-resource claim" is not a term the plan uses: define it as a COUNTEREXAMPLE meeting (f). |
| 2 | Clock charge and fixed four-step window approved | **None.** w = 3 gives the four steps K−3..K. This supersedes my nit A2 (allowing a smaller explicit-composite footprint), which I withdraw. The fixed charge may overcharge an observer whose memory already keeps time. That makes the condition stricter, which is conservative toward the claim under audit, and the report should say so. |
| 3 | K1 observers allowed; family-wide (K0) status reported separately | **None.** :279–280. |
| 4 | δ_cx = 1/8; all other thresholds fixed before any run | **Partly unfixed.** Two values are open: θ (decision 1), and the K range of the randomized LP. :179 implies K ≤ 255; if my A3 cap (e.g. K ≤ K_cx) is adopted, it must be fixed in the plan now. All other thresholds are fixed: δ ∈ {1/8, 1/4}, w = 3, K_cx, K_max, K_tape = 20, the 𝒫ᵉᵐᵇ cap of 12, the K ≤ 255 cap, the B4 dimension limit 20 and K+1 ≤ 24, and the IM ranges. |
| 5 | Reference fixed throughout PE-01 | **None.** :79–82, :338. |
| 6 | Prediction and distinguishing both recorded; distinguishing alone is not proof of predictability | **None.** K1 with optimal F is recorded. :293–296 keeps distinguishing witnesses out of COUNTEREXAMPLE. |
| 7 | Average-case or exact randomized for any claimed gap; deterministic worst case as bounds only | **None.** :95–96, :180, :309–310, :323–324. For passive m = 3 and linear m ≤ 4, only deterministic prediction-test K0 is computed, so a gap claim there can only be average-case. This follows from :95–96 and is consistent. |

**Horizon limitation (the owner's instruction).** The plan states K < 2^{n−m−1} only inside §10 (:407), as a
consequence of a recommendation.
- *Required with decisions 1–2 (S5):* add to §7, and to the generated verdict text, one sentence of the form: "the
  horizon bound K < 2^{n−m−1} is a consequence of the selected resource model (memory + clock + output ≤ θ); it is not
  a limit OI imposes on observers."
- Print the admissible-region table of A2 with it. At θ = n it is empty for n ≤ 5, and for the m = 3 passive and m = 4
  linear sweeps. So "no admissible witness" there is a fact about the model, not a measurement.

### Verdict on 6e5db447, updated

**BLOCK (narrowly).** Five fixes are required, each a line or a table row:
- S1: EX8's wording;
- S2: the strict specificity rule;
- S3: the CX checkpoint for the window;
- S4: footprint consistency and the FP checkpoint;
- S5: the resource-model limitation sentence.

The owner's decisions conflict with nothing except where they amend the plan's defaults. Implementing them needs θ
and the LP K range fixed before any run.

Once these are in, the plan is ACCEPT WITH NITS: A2's table-size nit, A3, the B1 K0 nit, and A4.
