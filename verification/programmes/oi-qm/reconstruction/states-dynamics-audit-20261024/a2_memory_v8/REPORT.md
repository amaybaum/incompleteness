# Bounded persistent memory does not escape the depth obstruction

25 October 2026. Author computation under #911, A2 (finite-precision operational approximation) only. The plan was
committed at `1dfec979721336cc9f0ce703b544f9d6be8e906c` (03:52:56 UTC), a single-parent child of #911's head
`49e1a1191c9ea5c303883afd2d8d3c28a233f9e5`. One exploration preceded it; see *Preregistration record*. The first
execution was `200fcd9f`. This revision follows an independent internal review of `200fcd9f` (accept with nits).
Nothing here concerns A1 (exact QM reconstruction), native availability, physical premises, access rules or OI. The
`a2_efficiency_v6/` h=3 certificate and the `a2_depth_v7/` results are unchanged and are reproduced as controls.

## Result and scope

Protocol, as in `a2_depth_v7/`: prepare X+, then read a, X, a, X, ... for h reads. T(h) is the complete-record total
variation from quantum theory, in which every read agrees in sign with the preceding pole with probability 4/5.

The verdicts, quoted verbatim from `result.json` (`class_verdict`, `family_verdict`, `resource_statement`):

```
BOUNDED_STATE_CLASS_NO_ESCAPE: every bounded-state controller with B fair fresh bits per slot and a time-independent update has T(h)->1 on this protocol (proof in REPORT.md); finite step checked on 38329 enumerated dyadic chains (39425 closed classes, 182 with exact stationary frequency 4/5, least run mismatch at most n=2), on the executed controller chain and on three RS chains (post-review: also on 15 floor-truncated decoder chains, 16 closed classes); base-5 countercontrol matches exactly
```

```
RS_FAMILY_FINITE_FAILURE_DEPTH_EVERY_TESTED_MEMBER: preregistered rule: B=2: each k=1..16 certified T>1/2 beyond a finite depth (nc/(1+nc) rule), largest h=64 (k=16); B=3: each k=1..16 certified T>1/2 beyond a finite depth (nc/(1+nc) rule), largest h=244 (k=2); B=4: each k=1..16 certified T>1/2 beyond a finite depth (nc/(1+nc) rule), largest h=9196 (k=2) | post-plan (power rule, exact memoryless comparators): B=2: power-rule depths from h=7 (k=1, 0 memory bits) to h=48 (k=16); nearest-dyadic i.i.d. reset (agreement 3/4; best i.i.d. B-bit law at this B by first crossing, other neighbour 1 crossing at h=4; not compared with record-dependent or time-varying controllers) first exceeds T=1/2 at h=127 (exact); certified to fail before it for k in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]; certified to outlast it for k in []; ordering undetermined for k in []; ceiling-rounded reset RS(B,1) (agreement 1) first exceeds 1/2 at h=4; B=3: power-rule depths from h=60 (k=6, 23 memory bits) to h=170 (k=2); nearest-dyadic i.i.d. reset (agreement 3/4; best i.i.d. B-bit law at this B by first crossing, other neighbour 7/8 crossing at h=45; not compared with record-dependent or time-varying controllers) first exceeds T=1/2 at h=127 (exact); certified to fail before it for k in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]; certified to outlast it for k in []; ordering undetermined for k in [2, 16]; ceiling-rounded reset RS(B,1) (agreement 7/8) first exceeds 1/2 at h=45; B=4: power-rule depths from h=742 (k=14, 69 memory bits) to h=6374 (k=2); nearest-dyadic i.i.d. reset (agreement 13/16; best i.i.d. B-bit law at this B by first crossing, other neighbour 3/4 crossing at h=127; not compared with record-dependent or time-varying controllers) first exceeds T=1/2 at h=1819 (exact); certified to fail before it for k in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]; certified to outlast it for k in []; ordering undetermined for k in [2, 3]; ceiling-rounded reset RS(B,1) (agreement 13/16) first exceeds 1/2 at h=1819
```

```
Necessity: with B fair fresh bits per slot and a time-independent update, T(h)->1 whenever the persistent state set is finite; so a controller keeping T(h) bounded below 1 at every depth needs the number of persistent states reachable within h slots, from a finite initial support, to grow without bound in h. Growth is not sufficient by itself: the a2_depth_v7 full-record memoryless controllers have growing state and T(h)->1. One controller with linearly growing private memory, the a2_depth_v7 retained-seed reset granted the target cuts, keeps T<=1/(2^B-2) at every depth for B>=2. The least sufficient growth rate is not determined here.
```

**The bounded-state class.**
- The controller's whole persistent state (carrier, private memory, any clock or record register it reads) takes
  values in a finite set Σ.
- Each slot, a fixed time-independent rule maps (state, one fresh block of B fair bits, setting) to
  (state, response).
- The initial law is arbitrary, non-dyadic laws included; the preparation read is unconstrained.

The class contains the natural slot extension of the executed M=16, W=16, B=24 controller and every variant of it
whose reset reads its retained carrier registers or other bounded private memory under a fixed rule. It also
contains every bounded periodic clock and every finite-state function of the record.

**Attribution.** On this protocol the obstruction is arithmetic: dyadic fresh randomness against a run law with
ratio 4/5.
- It holds for every reset that carries no private randomness across slots, whatever its record dependence
  (`a2_depth_v7/`).
- It holds for every controller with finite whole state (this package).
- The retained-seed reset escapes it. Its private memory grows linearly, and it is granted the target cuts.
- Bounded private memory with unbounded public state is open.

**Necessity, not sufficiency.**
- *Necessary:* the theorem shows that a controller keeping T bounded below 1 at every depth must reach unboundedly
  many persistent states, from a finite initial support.
- *Not sufficient:* growth alone does not avoid failure. The `a2_depth_v7/` full-record memoryless controllers have
  growing state and still have T(h) → 1.
- *What escapes:* one controller with linearly growing private memory, the retained-seed reset granted the target
  cuts, keeps T ≤ 1/(2^B − 2) at every depth for B ≥ 2.
- The least sufficient growth rate is not determined.

**Not covered:**
- any rate for the class;
- bounded private memory with unbounded public state, such as an unbounded clock or full-record dependence (the
  `a2_depth_v7/` memoryless class allows the latter but no private memory; neither class contains the other);
- time-dependent updates and growing per-slot blocks;
- non-dyadic fresh sources, other protocols and worst-case adaptive policies.

## The theorem and its proof

**Theorem.** Let a controller in the bounded-state class run the protocol. Then T(h) → 1.

**Proof.**

1. **The record is driven by a finite chain.** Let Z_t = (σ_t, o_t, t mod 2): the state after read t, the
   response, and the phase that fixes the next setting. For t ≥ 1 the law of Z_(t+1) given the whole past is the
   fraction of the 2^B fresh blocks that the fixed rule sends from Z_t to each value. So Z is a time-homogeneous
   Markov chain on a finite set from read 1 on, with an arbitrary initial law for Z_1. The agreement bit
   g_(t+1) = [o_(t+1) = o_t] is a function of (Z_t, Z_(t+1)). Write D_g[z,z'] for the probability of moving from z
   to z' with agreement bit g. Every entry of D_0 and D_1 lies in 2^-B Z, and D_0 + D_1 is stochastic.
2. **The limit is the total variation of the infinite laws.** Records of h reads correspond one-to-one to agreement
   words g_1..g_h. T(h) is nondecreasing and tends to T_∞ = TV(P, Q) on {0,1}^N, because the cylinder algebras
   increase and generate the product σ-field.
3. **A common part forces equal run frequencies.** Suppose T_∞ < 1. Then ν = P ∧ Q has mass 1 − T_∞ > 0. For each
   n ≥ 1, let F_n be the set of sequences in which the frequency of windows equal to 1^n tends to (4/5)^n.
   - Under Q the agreement bits are i.i.d. Bernoulli(4/5). Overlapping windows are not independent.
   - For each residue r mod n, the windows starting at positions ≡ r are disjoint and i.i.d., so the strong law
     applies to each residue class. Averaging the n classes gives Q(F_n) = 1. (The ergodic theorem for the Bernoulli
     shift gives the same.)
   - Hence ν(F_n^c) = 0, and P(∩_n F_n) ≥ ν(∩_n F_n) = 1 − T_∞ > 0.
4. **Under P the frequencies are stationary run laws.** A finite chain enters a closed class almost surely. Let C be
   a closed class and π_C its stationary law. On the event that Z enters C, the ergodic theorem for the irreducible
   block chain (Z_k, …, Z_(k+n)) gives, almost surely, window frequency of 1^n → a_n = π_C D_1^n 1. Periodicity
   does not matter for Cesàro averages. There are finitely many classes, so some C entered with positive probability
   has a_n = (4/5)^n for every n ≥ 0.
5. **That is impossible with dyadic transitions.** Let A = 2^B·D_1 restricted to C, an m×m matrix of nonnegative
   integers, m = |C|. Its characteristic polynomial χ(x) = x^m + c_(m−1)x^(m−1) + … + c_0 has integer
   coefficients. By Cayley–Hamilton, Σ_i c_i·π_C A^i 1 = 0, and π_C A^i 1 = 2^(Bi)·a_i = λ^i with λ = 2^(B+2)/5.
   So χ(λ) = 0. A rational root of a monic integer polynomial is an integer, and λ is not. This contradicts step 4,
   so T_∞ = 1. ∎

Remarks.
- Step 5 uses only a_0, …, a_m. Every closed class therefore shows a run mismatch at some n ≤ |C|. The checker
  computes that index exactly, together with χ(λ).
- Only the denominators matter. The proof holds for any fresh source whose probabilities lie in (1/N)Z with
  5 ∤ N. For a fair five-valued symbol, λ = 4 and the argument fails, as K4 shows.
- **Uniformity, without a computed depth.** For fixed |Σ| and B there are finitely many update rules. For an
  initial law μ, the overlap 1 − T_μ(h) is at most the sum over starting states z of 1 − T_z(h). So T(h) → 1
  uniformly over every controller with at most |Σ| states and every initial law. Some finite h*(|Σ|, B) therefore
  makes T > 1/2 for all of them. Here h* is not computed, and no rate is claimed.
- Standard facts used: the Cayley–Hamilton theorem, the rational root theorem, the strong law for i.i.d. sequences,
  the ergodic theorem for finite irreducible chains, and total variation over increasing generating algebras.
  Kakutani (*Ann. Math.* 49 (1948) 214–224) is credited, as in `a2_depth_v7/`, for the product case.

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
- The chain counts are checked against C(2^B+2n−1, 2n−1)^n.
- In each closed class, the stationary law and the run masses a_n are computed exactly for n ≤ |C|, and χ(λ) is
  checked to be nonzero.
- A class without a mismatch, or a singular stationary system, would print VOID; neither occurred.
- 182 classes have stationary agreement frequency exactly 4/5, so a frequency test alone would not separate them.
  Each of them mismatches at n = 2 (K5).

**Concrete class members.**
- **The executed controller**, written as a 4-state chain on signed poles: one closed class, stationary agreement
  frequency 6712867/8388608, mismatch at n = 1.
- **Explicit RS chains:** RS(2,2), RS(2,3), RS(3,2) have 9, 73 and 17 persistent states. Each has one closed class
  (sizes 5, 21, 9), mismatching at n = 1.
- **A second construction, added after the review:** the floor-truncated rescaling decoder FD(B,m).
  - *Rule:* an m-bit register r; append B fresh bits to form v; agree iff v < ⌈4·2^(m+B)/5⌉; rescale the left end
    by 5/4 or 5, then truncate to m bits.
  - *Why it is in the class:* it has finite state and a fixed rule, and it is granted the quantum cut.
  - *Checked:* every (B,m) with B=2,3,4 and m=1..5 (15 chains, 16 closed classes). Every class mismatches.
  - *A notable member:* FD(2,4) has a 15-state class whose stationary agreement frequency is exactly 4/5. It still
    mismatches at n = 2. The others mismatch at n = 1.
  - PLAN computation 3 refers to "the two concrete class members of computation 1", but computation 1 contains one
    member, the executed controller. FD is the second member reported.

## The restarted retained-seed reset RS(B,k)

RS(B,k) is the `a2_depth_v7/` retained-seed reset with its memory cleared after every k reads.
- Between slots it holds at most (k−1)B seed bits, k−1 record bits and a phase counter mod k. The record bits are
  redundant, since the record is a function of the seed, so the memory column is an upper bound. It is checked
  against the persistent-state count Σ_(j<k) 2^(j(B+1)), which equals the explicit chain size where the chain is
  built.
- RS(B,1) is the **ceiling-rounded** B-bit reset, with agreement ⌈4·2^B/5⌉/2^B. That is 1 at B=2, 7/8 at B=3
  and 13/16 at B=4.
- Its record law is a product of independent k-read block laws. Each block law is the `a2_depth_v7/` law on k
  reads (K2, K8).
- It reads the quantum cuts, so the negative result holds with that knowledge granted.

**Preregistered certified depths:** T(nk) ≥ nc/(1+nc) with c = 1 − BC_k, and T(nk) ≤ min(n·T_k, sqrt(2n(1 − BC_k)))
at the 1/10 level. Every member is certified T > 1/2 beyond a finite depth (`family_verdict`, first part).

**Post-plan.** Everything below in this section was added after the plan:
- the power rule, T(nk) ≥ 1 − BC_k^n and T(nk) ≤ sqrt(1 − BC_k^(2n)) or n·T_k, at the 1/2 level;
- the exact memoryless comparators;
- the comparisons and the mechanism paragraph.

**The memoryless comparator** is the **nearest-dyadic i.i.d. reset**: the multiple of 2^-B nearest to 4/5 in
distance, used at every read.
- Its agreement is 3/4 at B=2 and B=3, and 13/16 at B=4. Its exact first depths with T > 1/2 are 127, 127 and 1819.
- **Why it is the best i.i.d. law at these B.** For i.i.d. laws, T(h) is nondecreasing as the agreement moves away
  from 4/5 on either side, by the monotone likelihood ratio. So the best i.i.d. B-bit law in the first-crossing
  sense is one of the two neighbours of 4/5. The checker computes the other neighbour's exact crossing and requires
  it to be no later: 1 at B=2 crosses at 4, 7/8 at B=3 at 45, and 12/16 at B=4 at 127.
- **Its limit.** It is best among i.i.d. B-bit laws at the tested B only. It is not compared with the
  record-dependent or time-varying controllers of the `a2_depth_v7/` memoryless class.

Selected rows (all 48 members are in `result.json`; decimals are truncated toward zero; the last two columns are
post-plan):

| B | k | memory bits ≤ | block TV T_k | 1 − BC_k ≥ | T > 1/2 for h ≥ (power rule) | T ≤ 1/2 for h ≤ (power rule) |
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

**Against the nearest-dyadic i.i.d. reset** (post-plan):
- B=2: every k = 2..16 is certified to exceed T = 1/2 before it does (by h ≤ 48 < 127).
- B=3: k = 3..15 are certified to fail before it; k = 2 (170) and k = 16 (128) are undetermined.
- B=4: k = 4..16 are certified to fail before it; for example RS(4,8), holding up to 38 memory bits, by h = 776,
  and RS(4,14) by h = 742. k = 2, 3 are undetermined.
- No tested member is certified to outlast it.

So, on the certified depths, retaining seed bits within blocks makes the record law worse than the nearest-dyadic
i.i.d. reset at the same fresh-bit rate, for every member whose ordering is certified. That is all members except
B=3, k=2 and 16, and B=4, k=2 and 3, whose ordering is undetermined. None is certified to outlast it.

Against the suboptimal ceiling-rounded reset (crossings 4, 45, 1819), some members outlast it (B=2: every k ≥ 2;
B=3: k ≥ 9). That comparison is recorded in `result.json`, but it does not compare RS with the nearest-dyadic
i.i.d. reset.

**Why bounded retained seeds can hurt** (post-plan, measured for the RS family only). Repeated blocks compound
through the Bhattacharyya coefficient, not through total variation.
- For RS(4,k) the block TV stays near 0.01483, while 1 − BC_k grows from 0.000125 (k=1) to 0.0134 (k=16).
- The misdecoded mass sits on atypical records. At B=4, k=16, the records ending in 8 disagreements carry source
  mass 0.014827896867 against quantum mass 0.000002560000. At B=3, k=16, they carry 0.090624503454.
- So the block law is close to quantum theory plus a nearly singular part of mass close to its TV.
- An all-depth TV bound for a sampler with growing memory, such as the `a2_depth_v7/` 1/(2^B − 2), therefore does
  not carry over to a bounded-memory reuse of that sampler.

This is not a statement about the best bounded-memory controller.

## Controls

| control | what it checks | result |
| --- | --- | --- |
| K1 memoryless reproduction | rebuilt M=16 grid and counts (digest), A, B, exact T(1..4), SHA-256 digests of T(h) for h=1..64, all against the pinned `a2_depth_v7/result.json`; a generic hidden-chain record engine on the 4-state chain equals the product engine for h ≤ 12 | green |
| K2 retained-seed reproduction | rescaled-cell re-implementation, a different representation from the earlier absolute-coordinate walk, reproduces all 41 retained TV, coupling-gap and display values (B=2 h≤8, B=3 h≤6, B=4 h≤5 and h=8,12,16) | green |
| K3 engine zero | an exact base-5 Bernoulli(4/5) chain gives T=0 through h=12 | green |
| K4 base-5 countercontrol | with one fair five-valued symbol per slot, 1 of 6 one-state chains and 209 classes among 3,136 two-state chains match (4/5)^n for every n ≤ \|C\|, with χ(4)=0; the counts are checked in closed form | green |
| K5 frequency insufficiency | 182 dyadic classes have exact stationary frequency 4/5; each mismatches at n=2 | green |
| K6 unbounded memory | the unrestarted state machine equals the retained-seed law (B=2 h=6, B=3 h=4); every block TV is below 1/(2^B − 2); three checks on retained values (RS(4,1) is the 13/16 reset, two engines agree, its T(4096) display equals the retained one) | green |
| K7 enclosures | square-root endpoints checked by squaring; Le Cam inequalities 1 − BC ≤ TV ≤ sqrt(1 − BC²) for every block; for n·k ≤ 16 the exact product TV lies inside the preregistered and power-rule brackets; every certified depth is minimal or maximal for its rule; the power-rule lower bound 1 − BC_upper^n is one function, used by the depth search, the k=1 exact check and the product check; at k=1, exact T(h) ≥ 1 − BC_upper^h and T(h) ≤ min(sqrt(1 − BC_lower^(2h)), h·T_1), for every h ≤ 600, every multiple of 1024 up to twice the preregistered depth, and n_hp ± 1; the depths checked do not depend on the power-rule depth except for the points n_hp ± 1, but their upper end, twice n_half, depends on the shared BC enclosure through n_half, which the independent audit recomputes (B=2,3: every h ≤ 600; B=4: 618 depths to h=15,360) | green |
| K8 restart mechanics | an explicit state machine (seed register, exact interval, phase, clearing), enumerated over every fresh-bit string, and its chain form both equal the product of block laws (B,k,h) = (2,2,8), (2,3,7), (3,2,5), (4,3,4) | green |
| counts | census chain counts in closed form; memory column bounds the persistent-state count; that count equals the explicit chain size for RS(2,2), RS(2,3), RS(3,2) | green |
| power-rule cross-checks | (i) exact T(h) at k=1 from the binomial engine `tv_iid` must be ≥ the bound at every checked h, and the exact first crossing must lie at or before the reported depth; (ii) for n·k ≤ 16, the exact product TV must lie inside the power-rule bracket; (iii) the reported depth must be no later than the preregistered nc/(1+nc) depth; (iv) T ≤ 1/2 may be certified only at depths before T > 1/2 is. (i)–(iv) all read the same BC enclosure, and (i) and (ii) are one-sided with slack, so they catch only errors large enough to cross them; the independent audit below is what checks the enclosure and the exact depths | green |
| preregistered scope | the RS scope (B ∈ {2,3,4}, k = 1..16) and the thresholds 1/2 and 1/10 are parsed from PLAN.md after checking its pinned SHA-256, not taken from code defaults. The reported member set, the enclosure set and the audited member set must each equal that 48-member set; a missing, extra or mismatched member, or a lookup failure anywhere, prints VOID and exits 2 | green |
| independent certificate audit | separately written code. It does not call `retained_seed_runs`, `block_law`, `bc_enclosure`, `root_lo`/`root_hi`, `power_rule_lower`, `least_n_above`, `least_power_below` or `tv_of`. It does share `tv_iid` (for the k=1 certificates), `digest`, the constants `HALF` and `TENTH`, `check`, `Q` and the standard-library `isqrt` and `product`, and it reads the reported entries and the reported enclosure. Single edits to the shared pieces are caught elsewhere in the review's mutants A1 (`HALF`), A2 (`digest`), A3 (`isqrt`) and A6 (`tv_iid`). The audit builds integer-only block laws in absolute coordinates (the block TV digest must match), and an integer square-root enclosure of BC that must overlap the enclosure every reported depth was built from. It recomputes every reported depth from its stated definition with its own integer powers: the preregistered half and tenth depths, and the power-rule half and upper depths; each must equal the reported value. It checks every certificate against exact TV where exact TV is enumerable: for every member and every n with n·k ≤ 16, from its own product enumeration, T(nk) > 1/2 when n ≥ n_hp or n ≥ n_half, T ≤ 1/2 when n ≤ n_lp, and T ≤ 1/10 when n ≤ n_tenth; and at k=1 the same at the reported depths, with `tv_iid`. In all, 48 members and 212 certificate checks. The T > 1/2 certificate is checked against exact TV for 7 of the 48 members (B=2, k=1..5; B=3, k=1; B=4, k=1); for the other 41 the T > 1/2 depth lies beyond the enumerable range and rests on the independent BC enclosure and depth recomputation | green |
| comparators | the nearest-dyadic agreement is distance-minimal over 2^-B Z; its exact crossing is no earlier than the other neighbour's; the fails-before and outlasts lists in `family_verdict` are recomputed from the stored depths and the nearest-dyadic crossing and must equal the per-member flags | green |

**Mutants** (`mutants/run_mutants.py`, output in `mutants/mutants.out`). The unmodified checker first reproduces
`result.json` byte for byte. Each mutant is then run separately. It counts as caught only if it exits 2 and its
first line begins with VOID and the targeted control's label.
- M1 grid constant (K1)
- M2 cut rounding (K2)
- M3 mismatch search limited to n=1 (step 5 / K5)
- M4 base 5 replaced by base 4 (K4)
- M5 square-root endpoint rounded down (K7)
- M6 missing restart (K8)
- M7 half-depth off by one (K7)
- M8 wrong initial phase (K1)
- M9 pinned input hash
- M10 RS(4,1) rounding (K6)
- M11 power-rule exponent doubled (K7 power-rule control)
- M12 closedness test removed (singular-system VOID)
- M13 one composition dropped (census count)
- M14 record bits dropped from the memory column (memory control)
- M15 exponent doubled inside the shared power-rule lower bound (exact product TV)
- M16 comparison flags computed against the ceiling-rounded crossing (flag recomputation)
- M17 threshold 1/2 → 1/4 changed in the depth search and in its own minimality check together (exact crossing)
- M18 weaker bound 1 − BC^⌈n/2⌉ inside the shared function (preregistered-rule comparison)
- M19 is M15 with the product-loop and k=1 exact checks disabled (caught by certificate consistency alone)
- M20 is M15 with the product-loop and consistency checks disabled (caught by the exact k=1 TV alone). In a first
  version the k=1 range was tied to the mutated power-rule depth and M20 passed; the range now uses the
  preregistered depth
- M21, M22 BC enclosure scaled by 0.9999 and by 1 − 10^-6 (independent BC enclosure)
- M23 shared bound 1 − BC^(n+⌊n/20⌋) (independent depth recomputation)
- M24 depth search and its minimality check one block early (independent depth recomputation)
- M25 is M24 with the depth recomputation disabled (certificate-level exact check). In a first version the
  certificate checks used the audit's own recomputed depths, not the reported ones, and M25 passed; they now use
  the reported depths
- M26–M30 (the review's L1, L2, L3b, L5, L6) narrow the k range in both paths or in the main path only, delete a
  member, narrow the B range in both paths, or restrict the audit to four members (preregistered-scope control)

M11–M14 re-implement the review's mutants R1, R4, R10 and R15. M15 and M16 re-implement the re-check's D1 and D5.

**Consistent wrong-bound mutants.** M15, M17, M18 and M21–M25 each change the bound, the enclosure or the depth
search together with every check that restates it. The reported depths change, so no self-consistency check can see
the change.
- M15 is caught first by the exact product TV. It is also caught by certificate consistency alone (M19), and by
  the exact k=1 TV alone (M20).
- M17 is caught by the exact crossing.
- M18 is caught by the preregistered-rule comparison.
- M21 and M22 (the BC enclosure scaled down by 10^-4 and 10^-6, the re-check's W1a and W1b) are caught by the
  independent BC enclosure.
- M23 (bound 5% too strong, W3) and M24 (every depth one block early, W4) are caught by the independent depth
  recomputation.
- M25 is M24 with that recomputation disabled. It is caught by the certificate-level exact check at a depth the
  checker enumerates exactly.

These results hold for the mutants listed; they do not show that every possible error is caught. One limit is
inherent: the audit's definitions and the main rules are two codings of the same stated formulas. If both are
edited to agree, as in the review's mutant A5 (main bound and audit definition both 5% too strong), a second
implementation cannot detect it. Only an exact certificate inside the affected range can, and A5 passes because
⌊n/20⌋ = 0 for every n ≤ 16. Agreement of both codings with the definitions stated in this report rests on review. Before the audit
was added, the re-check found that W1a, W1b, W3 and W4 passed every control, and that W4 reported a false
certificate: T > 1/2 for h ≥ 10 at RS(2,5), whose exact T(10) is 0.4637.

The reviewers' scripts were rerun on copies against this revision:
- **The first round's script** (15 code mutants and one tampered input). Its R1 targets a line the shared function
  replaced, so the copy's R1 strings were adapted to the new line.
- **The re-check's script** (D1, D4, D5). Its D1 strings were adapted to the shared function.
- **The third re-check's scripts** (A1–A7 and L1–L6) were run on copies. Because PLAN.md is now a pinned input
  of the checker, every reviewer script copy was adapted to copy PLAN.md beside the mutated checker; nothing else
  in them was changed.
- **The second re-check's scripts** (the first-round set with R1 adapted, and W1a, W1b, W2–W5) were run with
  the same PLAN.md adaptation.
- Results are given with this revision.

Two controls were reordered so that M3 and M4 fail on their targeted labels and not on a later-added check: the
floor-decoder member now runs after the census, and the K4 count check after the exact-match check.

## Preregistration record and departures

**Correction.** PLAN.md says it was committed "alone before any computation of this round". That is inaccurate,
and PLAN.md is left as committed.

**What the repository establishes:** PLAN.md was committed alone at `1dfec979`, before any other file of this
package, and the execution code postdates it.

**By the author's account** (no artifact of the exploration is retained, and the repository cannot corroborate
it), the following holds.
- **What ran before the plan:** one floating-point exploration of the floor-truncated rescaling decoder with a
  fixed-width m-bit register (B=1..4, m=0..8). It is a finite-state member of the bounded-state class, not a member
  of the RS family.
- **What it showed, qualitatively:**
  - several closed classes and absorbing states;
  - stationary agreement defects that did not shrink steadily with m;
  - at B=2, m=4, a class matching frequency 4/5 to float precision while its run masses differed at n ≥ 2.
- **What it influenced:**
  - It steered the choice of tested family away from that decoder to RS(B,k).
  - Its frequency-4/5 class with differing run masses may have informed K5 (the preregistered expectation that
    exact-frequency dyadic classes exist and mismatch at some n ≥ 2). It may also have informed the choice of run
    masses rather than frequency in the proof route.
  - It may equally have informed the census populations, the expectation behind computation 3 that every class
    mismatches at small n, and the choice to compute exact stationary laws rather than frequencies.
  - These are disclosed as possible influences. How much influence there was cannot be measured after the fact,
    and the repository cannot establish the order in which the proof route and the exploration arose.
  - It did not compute on RS(B,k), on the census populations or on the decision rule (author's account).
- **The exact recomputation:** after the review, the decoder is recomputed exactly as the second concrete member.
  The B=2, m=4 class has frequency exactly 4/5 and mismatches at n=2.

**Preregistered:**
- the class, H and its proof route;
- the census populations and K1–K8;
- RS(B,k) for B=2,3,4 and k=1..16;
- the nc/(1+nc) and min(nT_k, sqrt(2nc)) rules with their 1/2 and 1/10 thresholds;
- the memory bits, the VOID rule and the verdict labels.

**Post-plan, before the review:**
- the power-rule depths and the T ≤ 1/2 threshold for the upper depth (the plan had 1/10);
- the exact memoryless crossings and every comparison;
- the Le Cam checks and the trailing-run diagnostic;
- the mechanism paragraph;
- K6 implemented through the unrestarted state machine and retained values, rather than RS(B,k) at k ≥ h for
  every h;
- mutants M9 and M10;
- the mutant-runner prefix match. The first version compared the whole VOID line with the label, and reported M3
  and M8 as not caught.

**Post-review:**
- the nearest-dyadic comparator and its regenerated comparisons;
- RS(B,1) renamed the ceiling-rounded reset;
- post-plan labels inside `family_verdict`;
- the power-rule controls (K7) and the singular-system VOID;
- closed-form census counts and the memory-column control;
- the floor-truncated decoder member;
- wording on necessity versus sufficiency, verbatim verdicts, proof step 3 and attribution;
- the K2/K6 count split (41 and 3), the corrected K6 string, a faster exact `tv_iid`, and mutants M11–M14.

**Post-re-check:**
- the comparator wording narrowed to the nearest-dyadic i.i.d. reset, with the other neighbour's exact crossing
  as a control;
- the ordering sentence limited to members whose ordering is certified;
- one shared power-rule lower-bound function, constrained independently (exact k=1 TV and crossing, exact product
  TV, the preregistered-rule comparison, upper/lower certificate consistency);
- the flag-recomputation control, and mutants M15–M18;
- K5 and the run-mass route added to what the exploration may have informed, with the unverifiable sentence
  removed;
- the post-review label on the floor-decoder counts inside `class_verdict`.

**Post-re-check 2:**
- the independent certificate audit (integer block laws, integer BC enclosure, depth recomputation, and
  certificate-level exact checks);
- mutants M21–M25;
- the control descriptions narrowed to what the demonstrated mutants show;
- the k=1 range's dependence on the shared enclosure stated;
- the disclosure wording ("did not compute on"), mirrored into PROVENANCE.

**Post-re-check 3:**
- the preregistered scope parsed from the hash-pinned PLAN.md, with reported, enclosure and audited member sets
  required to equal it;
- lookup failures converted to VOID;
- mutants M26–M30;
- the audit's shared and unshared helpers listed;
- the A5 limit stated;
- the count of members whose T > 1/2 certificate meets exact TV (7 of 48) stated;
- the exploration account attributed to the author, with what the repository establishes.

## What this does not show

- A rate of failure, or a computed h*(|Σ|, B), for the bounded-state class.
- Anything about bounded private memory with an unbounded clock or full-record dependence, time-dependent rules,
  growing blocks or non-dyadic sources.
- The least memory growth that keeps T bounded. One linearly growing sampler escapes; whether logarithmic growth
  can suffice is open.
- Worst-case behaviour over adaptive policies or other protocols.
- Anything about A1, native sourcing, availability or OI.

## Replay

Timings on the author's container: about 3 minutes for the checker, normal or -O, on a lightly loaded machine (7 minutes
measured under heavy shared load), and about 95 minutes for the 30-mutant run under that load. From an empty working directory, with the repository root as R and
D = R/verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a2_memory_v8:

    python3 -I -B D/checks.py > out.json && cmp out.json D/result.json
    python3 -I -B -O D/checks.py > out.json && cmp out.json D/result.json
    python3 -I -B D/mutants/run_mutants.py > m.out && cmp m.out D/mutants/mutants.out

`SHA256SUMS` lists `PLAN.md`, `REPORT.md`, `checks.py`, `result.json`, `PROVENANCE.json`,
`mutants/run_mutants.py` and `mutants/mutants.out`.
