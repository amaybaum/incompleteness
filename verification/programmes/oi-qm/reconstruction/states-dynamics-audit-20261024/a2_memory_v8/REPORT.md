# Bounded persistent memory does not escape the depth obstruction

25 October 2026. Author computation under #911, A2 (finite-precision operational approximation) only. The plan was
committed at `1dfec979721336cc9f0ce703b544f9d6be8e906c` (03:52:56 UTC), a single-parent child of #911's head
`49e1a1191c9ea5c303883afd2d8d3c28a233f9e5`, before any computation on the tested class or family. Nothing here
concerns A1 (exact QM reconstruction), native availability, physical premises, access rules or OI. The
`a2_efficiency_v6/` h=3 certificate and the `a2_depth_v7/` results are unchanged and are reproduced as controls.

## Result and scope

Protocol, as in `a2_depth_v7/`: prepare X+, then read a, X, a, X, ... for h reads; T(h) is the complete-record
total variation from quantum theory, in which every read agrees in sign with the preceding pole with probability
4/5. The verdicts, generated from the measured values:

    BOUNDED_STATE_CLASS_NO_ESCAPE: every bounded-state controller with B fair fresh bits per slot and a
    time-independent update has T(h)->1 on this protocol (proof below); finite step checked on 38329 enumerated
    dyadic chains (39425 closed classes, 182 with exact stationary frequency 4/5, least run mismatch at most n=2),
    on the executed controller chain and on three RS chains; base-5 countercontrol matches exactly

    RS_FAMILY_FINITE_FAILURE_DEPTH_EVERY_TESTED_MEMBER (B=2,3,4; k=1..16; details in the table below)

**The bounded-state class.**
- The controller's whole persistent state (carrier, private memory, any clock or record register it reads) takes
  values in a finite set Σ.
- Each slot, a fixed time-independent rule maps (state, one fresh block of B fair bits, setting) to
  (state, response).
- The initial law is arbitrary, non-dyadic laws included; the preparation read is unconstrained.

The class contains the natural slot extension of the executed M=16, W=16, B=24 controller and every variant of it
whose reset reads its retained carrier registers or any other bounded private memory under a fixed rule. It also
contains every bounded periodic clock and every finite-state function of the record.

**Consequence for resources.** With B fair fresh bits per slot and a time-independent update, keeping T(h) bounded
below 1 at every depth requires the number of persistent states reachable within h slots to grow without bound in
h. The `a2_depth_v7/` retained-seed reset holds tB seed bits and the record after t reads, and keeps
T ≤ 1/(2^B − 2) at every depth for B ≥ 2. So growing state suffices on this protocol and bounded state does not.
The least growth rate is not determined here.

**Where the obstruction comes from.** It is arithmetic. The quantum run law (4/5)^n has the ratio 4/5, whose
denominator contains 5. No finite chain with transition probabilities in 2^-B Z has a stationary run law with
that ratio. Carrying randomness across slots in bounded memory does not remove it. A fair five-valued source
removes it at once, with no memory (countercontrol K4).

**Not covered:**
- any rate for the class;
- bounded private memory with unbounded public state, such as an unbounded clock or full-record dependence (the
  `a2_depth_v7/` memoryless class allows the latter but no private memory; neither class contains the other);
- time-dependent updates and growing per-slot blocks;
- non-dyadic fresh sources, other protocols and worst-case adaptive policies;
- the minimal memory growth.

## The theorem and its proof

**Theorem.** Let a controller in the bounded-state class run the protocol. Then T(h) → 1.

**Proof.**

1. **The record is driven by a finite chain.** Let Z_t = (σ_t, o_t, t mod 2): the state after read t, the
   response, and the phase that fixes the next setting. For t ≥ 1 the law of Z_(t+1) given the whole past is the
   fraction of the 2^B fresh blocks that the fixed rule sends from Z_t to each value. So Z is a time-homogeneous
   Markov chain on a finite set from read 1 on, with an arbitrary initial law for Z_1. The agreement bit
   g_(t+1) = [o_(t+1) = o_t] is a function of (Z_t, Z_(t+1)). Write D_g[z,z'] for the probability of moving from z
   to z' with agreement bit g. Every entry of D_0 and D_1 lies in 2^-B Z, and D_0 + D_1 is stochastic.
2. **The limit is the total variation of the infinite laws.** Records of h reads correspond one-to-one to
   agreement words g_1..g_h. T(h) is nondecreasing and tends to T_∞ = TV(P, Q) on {0,1}^N, because the cylinder
   algebras increase and generate the product σ-field.
3. **A common part forces equal run frequencies.** Suppose T_∞ < 1. Then ν = P ∧ Q has mass 1 − T_∞ > 0. For each
   n ≥ 1, let F_n be the set of sequences in which the frequency of windows equal to 1^n tends to (4/5)^n. Under
   Q the agreement bits are i.i.d. Bernoulli(4/5), so Q(F_n) = 1 by the strong law. Hence ν(F_n^c) = 0, and
   P(∩_n F_n) ≥ ν(∩_n F_n) = 1 − T_∞ > 0.
4. **Under P the frequencies are stationary run laws.** A finite chain enters a closed class almost surely. Let
   C be a closed class and π_C its stationary law. On the event that Z enters C, the ergodic theorem for the
   irreducible block chain (Z_k, …, Z_(k+n)) gives, almost surely, window frequency of 1^n → a_n = π_C D_1^n 1.
   Periodicity does not matter for Cesàro averages. So some C entered with positive probability has
   a_n = (4/5)^n for every n ≥ 0.
5. **That is impossible with dyadic transitions.** Let A = 2^B·D_1 restricted to C, an m×m matrix of
   nonnegative integers, m = |C|. Its characteristic polynomial χ(x) = x^m + c_(m−1)x^(m−1) + … + c_0 has integer
   coefficients. By Cayley–Hamilton, Σ_i c_i·π_C A^i 1 = 0, and π_C A^i 1 = 2^(Bi)·a_i = λ^i with λ = 2^(B+2)/5.
   So χ(λ) = 0. A rational root of a monic integer polynomial is an integer, and λ is not. This contradicts
   step 4, so T_∞ = 1. ∎

Remarks.
- Step 5 uses only a_0, …, a_m. Every closed class therefore shows a run mismatch at some n ≤ |C|. The checker
  computes that index exactly, together with χ(λ).
- Only the denominators matter. The proof holds for any fresh source whose probabilities lie in (1/N)Z with
  5 ∤ N. For a fair five-valued symbol, λ = 4 and the argument fails, as K4 shows.
- **Uniformity, without a computed depth.** For fixed |Σ| and B there are finitely many update rules. For an
  initial law μ, the overlap 1 − T_μ(h) is at most the sum over starting states z of 1 − T_z(h). So T(h) → 1
  uniformly over every controller with at most |Σ| states and every initial law. Some finite h*(|Σ|, B) therefore
  makes T > 1/2 for all of them. Here h* is not computed, and no rate is claimed.
- Standard facts used: the Cayley–Hamilton theorem, the rational root theorem, the strong law for i.i.d.
  sequences, the ergodic theorem for finite irreducible chains, and total variation over increasing generating
  algebras. Kakutani (*Ann. Math.* 49 (1948) 214–224) is credited, as in `a2_depth_v7/`, for the product case.

## Finite checks of step 5

| population | chains | closed classes | exact frequency 4/5 | largest least-mismatch n |
| --- | --- | --- | --- | --- |
| n=1 states, B=1..8 | 518 | 518 | 0 | 1 |
| n=2, B=1 | 100 | 109 | 0 | 1 |
| n=2, B=2 | 1,225 | 1,250 | 10 | 2 |
| n=2, B=3 | 27,225 | 27,306 | 88 | 2 |
| n=3, B=1 | 9,261 | 10,242 | 84 | 2 |

- The enumeration covers every n-state agreement chain in which each state's 2^B outcome counts are spread over
  (next state, agreement bit).
- In each closed class, the stationary law and the run masses a_n are computed exactly for n ≤ |C|, and χ(λ) is
  checked to be nonzero.
- A class without a mismatch would print VOID; none occurred.
- 182 classes have stationary agreement frequency exactly 4/5, so a frequency test alone would not separate them.
  Each of them mismatches at n = 2 (K5).

The same steps were applied to concrete class members:
- **The executed controller**, written as a 4-state chain on signed poles: one closed class, stationary agreement
  frequency 6712867/8388608, mismatch at n = 1.
- **Explicit state-machine chains of the restarted family:**

  | member | persistent states | closed class size | stationary agreement frequency | mismatch at |
  | --- | --- | --- | --- | --- |
  | RS(2,2) | 9 | 5 | 27/32 | n = 1 |
  | RS(2,3) | 73 | 21 | 49/64 | n = 1 |
  | RS(3,2) | 17 | 9 | 103/128 | n = 1 |

## The restarted retained-seed reset RS(B,k)

RS(B,k) is the `a2_depth_v7/` retained-seed reset with its memory cleared after every k reads.
- Between slots it holds at most (k−1)B seed bits, k−1 record bits and a phase counter mod k. The table's memory
  column is this upper bound. RS(B,1) is the memoryless B-bit reset, with agreement ⌈4·2^B/5⌉/2^B at every read.
- Its record law is a product of independent k-read block laws P_k. Each block law is the `a2_depth_v7/` law on k
  reads (K2, K8).
- Like that reset, it reads the quantum cuts: it is granted exact knowledge of the target law. The negative result
  holds with that knowledge granted.

**Certified depths**, exact rationals with outward-rounded square roots, where BC_k is the block Bhattacharyya
coefficient:
- **Preregistered rules:** T(nk) ≥ nc/(1+nc) with c = 1 − BC_k; T(nk) ≤ min(n·T_k, sqrt(2n(1 − BC_k))).
- **Added after the plan, tighter (power rule):** T(nk) ≥ 1 − BC_k^n, and T(nk) ≤ sqrt(1 − BC_k^(2n)) or n·T_k.
- T(h) is nondecreasing in h, so each depth bound extends to every h beyond it, or before it.
- The memoryless B-bit reset's first exact crossing of 1/2 is located by exact evaluation and bisection.

Selected rows (all 48 members are in `result.json`; decimals are truncated toward zero):

| B | k | memory bits ≤ | block TV T_k | 1 − BC_k ≥ | T > 1/2 for h ≥ (power rule) | T ≤ 1/2 for h ≤ |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | 1 | 0 | 0.012500000000 | 0.000125057859 | 5,543 | 1,150 |
| 4 | 2 | 6 | 0.012500000000 | 0.000217515912 | 6,374 | 1,322 |
| 4 | 4 | 17 | 0.014695922851 | 0.001876935716 | 1,476 | 304 |
| 4 | 8 | 38 | 0.014825309930 | 0.007175833768 | 776 | 264 |
| 4 | 14 | 69 | 0.014825339041 | 0.013110278054 | 742 | 462 |
| 4 | 16 | 79 | 0.014825339041 | 0.013359223380 | 832 | 528 |
| 3 | 1 | 0 | 0.075000000000 | 0.005226090457 | 133 | 27 |
| 3 | 6 | 23 | 0.090461670410 | 0.071633886982 | 60 | 30 |
| 3 | 9 | 36 | 0.090621126639 | 0.085325126151 | 72 | 45 |
| 3 | 16 | 64 | 0.090623351846 | 0.088160851929 | 128 | 80 |
| 2 | 1 | 0 | 0.200000000000 | 0.105572809000 | 7 | 2 |
| 2 | 16 | 49 | 0.283262294945 | 0.278560939924 | 48 | 16 |

Comparison with the memoryless reset at the same fresh-bit rate. Its exact first depths with T > 1/2 are h = 4
(B=2, agreement 1), h = 45 (B=3, agreement 7/8) and h = 1819 (B=4, agreement 13/16).
- **B=4.** Every k = 4..16 is certified to exceed T = 1/2 before the memoryless reset does: for example RS(4,8),
  holding up to 38 memory bits, by h = 776, and RS(4,14) by h = 742. On those depths, retaining seed bits within
  blocks makes the record law worse than resetting from fresh bits alone.
- **B=3.** k = 9..16 are certified to stay at T ≤ 1/2 through h = 45, so they outlast the memoryless reset. No
  ordering is certified for k = 2..8.
- **B=2.** Every k ≥ 2 outlasts the memoryless reset, whose agreement is 1.

**Why bounded retained seeds can hurt.** Repeated blocks compound through the Bhattacharyya coefficient, not
through total variation.
- For RS(4,k) the block TV stays near 0.01483, while 1 − BC_k grows from 0.000125 (k=1) to 0.0134 (k=16).
- The misdecoded mass concentrates on atypical records. At B=4, k=16, the records ending in 8 disagreements carry
  source mass 0.014827896867 against quantum mass 0.000002560000. At B=3, k=16, they carry 0.090624503454.
- So the block law is close to quantum theory plus a nearly singular part of mass close to its TV.
- An all-depth TV bound for a sampler with growing memory, such as the `a2_depth_v7/` 1/(2^B − 2), therefore does
  not carry over to a bounded-memory version of that sampler used repeatedly.

This is measured for the RS family only; it is not a statement about the best bounded-memory controller.

## Controls

| control | what it checks | result |
| --- | --- | --- |
| K1 memoryless reproduction | rebuilt M=16 grid and counts (digest), A, B, exact T(1..4), SHA-256 digests of T(h) for h=1..64, all against the pinned `a2_depth_v7/result.json`; a generic hidden-chain record engine on the 4-state chain equals the product engine for h ≤ 12 | green |
| K2 retained-seed reproduction | rescaled-cell re-implementation, a different representation from the earlier absolute-coordinate walk, reproduces all 43 retained TV, coupling-gap and display values (B=2 h≤8, B=3 h≤6, B=4 h≤5 and h=8,12,16) | green |
| K3 engine zero | an exact base-5 Bernoulli(4/5) chain gives T=0 through h=12 | green |
| K4 base-5 countercontrol | with one fair five-valued symbol per slot, 1 of 6 one-state chains and 209 classes among 3,136 two-state chains match (4/5)^n for every n ≤ \|C\|, with χ(4)=0: the step-5 check can fail and the dyadic source is load-bearing | green |
| K5 frequency insufficiency | 182 dyadic classes have exact stationary frequency 4/5; each mismatches at n=2 | green |
| K6 unbounded memory | the unrestarted state machine equals the retained-seed law (B=2 h=6, B=3 h=4); every block TV is below 1/(2^B − 2); RS(4,1) is the 13/16 memoryless reset and reproduces its retained T(4096) display | green |
| K7 enclosures | square-root endpoints checked by squaring; the Le Cam inequalities 1 − BC ≤ TV ≤ sqrt(1 − BC²) hold for every block; for every n·k ≤ 16 the exact product TV lies inside both brackets; every certified depth is minimal or maximal for its rule; at k=1 the power rule brackets the exact memoryless crossing | green |
| K8 restart mechanics | an explicit state machine (seed register, exact interval, phase, clearing), enumerated over every fresh-bit string, and its chain form both equal the product of block laws (B,k,h) = (2,2,8), (2,3,7), (3,2,5), (4,3,4) | green |

**Mutants** (`mutants/run_mutants.py`, output in `mutants/mutants.out`). The unmodified checker must first
reproduce `result.json` byte for byte. Each mutant is then run separately, and counts as caught only if it exits 2
with VOID and the targeted control's label.
- M1 changes a grid constant (K1).
- M2 changes the cut rounding (K2).
- M3 limits the mismatch search to n=1 (step 5 and K5).
- M4 replaces the base-5 source with base 4 (K4).
- M5 rounds the square-root endpoint down (K7).
- M6 removes the restart (K8).
- M7 moves the half-depth off by one (K7).
- M8 uses the wrong initial phase (K1 generic engine).
- M9 alters the pinned input hash.
- M10 changes the RS(4,1) rounding (K6).

## Departures from the plan

- **Ran before the plan:** one floating-point exploration of a different candidate, a floor-truncated rescaling
  decoder. It is not adopted, and nothing from it is reported.
- **Added after the plan:**
  - the power-rule depths;
  - the exact memoryless crossings and the comparisons with them;
  - the Le Cam checks;
  - the trailing-disagreement diagnostic.

  All were added after the first execution showed that RS(4,k) blocks have large Hellinger defects. The
  preregistered rules are kept, and their depths are in `result.json`.
- **Mutant runner corrected:** its first version compared the whole VOID line with the label, and so reported M3
  and M8 as not caught although each failed on its targeted control with a label carrying a suffix. It now
  requires the line to begin with the label; the recorded output is from the corrected runner.
- **K6 implemented differently:** it is checked through the unrestarted state machine and the retained values,
  not by running RS(B,k) at k ≥ h for every h.

## What this does not show

- A rate of failure, or a computed h*(|Σ|, B), for the bounded-state class.
- Anything about bounded private memory with an unbounded clock or full-record dependence, time-dependent rules,
  growing blocks or non-dyadic sources.
- The least memory growth that keeps T bounded. The retained-seed reset's linear growth is sufficient; whether
  logarithmic growth suffices is open.
- Worst-case behaviour over adaptive policies or other protocols.
- Anything about A1, native sourcing, availability or OI.

## Replay

Timings on the author's container: about 72 s for the checker, normal or -O, and about 2.5 minutes for the
mutant run. From an empty working directory, with the repository root as R and
D = R/verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a2_memory_v8:

    python3 -I -B D/checks.py > out.json && cmp out.json D/result.json
    python3 -I -B -O D/checks.py > out.json && cmp out.json D/result.json
    python3 -I -B D/mutants/run_mutants.py > m.out && cmp m.out D/mutants/mutants.out

`SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json`, `PROVENANCE.json`,
`mutants/run_mutants.py` and `mutants/mutants.out`.
