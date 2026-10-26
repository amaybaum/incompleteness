# Bounded persistent memory and the depth obstruction: plan

25 October 2026. Research only, under guiding draft #911, drafted at
`49e1a1191c9ea5c303883afd2d8d3c28a233f9e5`. This plan is committed alone before any computation of this round.
It concerns A2 (finite-precision operational approximation) only. Nothing here bears on A1 (exact QM
reconstruction), native availability, physical premises, access rules or OI-to-QM equivalence.

## Question

`a2_depth_v7/` shows that on the in-menu protocol "prepare X+, then read a, X, a, X, ..." the complete-record
total variation T(h) from quantum theory tends to 1 with depth for every controller in the memoryless reset class,
and that the retained-seed reset, which keeps every seed bit it has drawn, gives T <= 1/(2^B - 2) at every depth.
The retained-seed reset's private memory grows with depth: after t reads it holds tB seed bits and an interval
fixed by the record. The open question is whether persistent private memory as such avoids the obstruction, or
only memory that grows without bound.

Exact question: for a controller whose whole persistent state (carrier, private memory, any clock or record
registers it reads) takes values in a fixed finite set, which is updated each slot by a fixed rule from that
state, one fresh block of B fair bits and the setting, does T(h) stay bounded below 1 at every depth on this
protocol? If not, how must memory grow with depth for the retained-seed family?

## Candidate class and family

- **Bounded-state class.** Finite state set Sigma of any size; per slot a time-independent deterministic update
  (state, fresh B-bit block, setting) -> (state, response); any initial law on Sigma, including non-dyadic ones
  (the preparation read is unconstrained). Response records are public; the state is private. The class contains
  the natural slot extension of the executed M=16, W=16, B=24 controller (finite carrier, finite retained
  registers), every memory-reading variant of it with a fixed update, and any bounded periodic clock.
- **Tested family: the restarted retained-seed reset RS(B,k).** The `a2_depth_v7/` retained-seed reset, with its
  memory cleared after every k reads: after reads k, 2k, ..., it discards its retained seed bits and interval and
  begins again with an empty seed. Its memory is at most kB seed bits, k record bits for the interval and a phase
  counter mod k. RS(B,infinity) is the `a2_depth_v7/` reset. Like that reset it reads the quantum cuts, so it is a
  protocol-specific sampler that is given exact knowledge of the target law; that knowledge is a resource the
  family is granted, and a negative result for it holds with the knowledge granted.

## Hypothesis to be proved and checked

H: for every member of the bounded-state class with B fair fresh bits per slot, T(h) -> 1 on this protocol.

Proof route, fixed in advance: (1) the record law of a bounded-state member is a function of a finite Markov
chain Z_t whose agreement-labelled transition matrices D_0, D_1 have entries in 2^-B Z; (2) T(h) tends to the
total variation of the infinite record laws, which is 1 unless the two laws are not mutually singular; (3) by the
ergodic theorem for finite chains, on the event that Z enters a recurrent class C the frequency of the agreement
word 1^n tends to pi_C D_1^n 1, while under quantum theory agreement bits are i.i.d. Bernoulli(4/5) and that
frequency tends to (4/5)^n; (4) equality for n = 0..|C| would make 2^(B+2)/5 an eigenvalue of the integer matrix
2^B D_1 restricted to C, hence a root of a monic integer polynomial, hence an integer, which it is not.
Step (4) is the finite ingredient the checker exercises exactly.

## Computations

1. **Reproduce `a2_depth_v7/`'s memoryless result** (control). Rebuild the executed grid and CDF counts with exact
   integers, without importing the earlier checker; match the retained count digest; recompute A and B and the
   exact T(h) for h = 1..4 and the digests of T(h) for h = 1..64; compare with `a2_depth_v7/result.json`. Compute
   T(h) for h <= 12 a second time with a generic hidden-chain record engine applied to the controller written as
   a finite chain, and require equality.
2. **Reproduce `a2_depth_v7/`'s retained-seed result** (control). Re-implement the retained-seed reset in
   rescaled-cell coordinates (a different representation from the earlier absolute-coordinate range walk) and
   compare its exact T(h) and coupling gaps with every retained value: B=2 (h<=8), B=3 (h<=6), B=4 (h<=5).
3. **Finite step (4) of the proof, exhaustively on small chains.** Enumerate every agreement chain with n states
   and per-state outcome counts summing to 2^B, for (n,B) in {(1,1..8), (2,1), (2,2), (2,3), (3,1)}. For each
   closed communicating class, compute the exact stationary law and the least n <= |C| with pi_C D_1^n 1 !=
   (4/5)^n, and evaluate the integer characteristic polynomial at 2^(B+2)/5 exactly. Report the number of chains,
   the number whose stationary agreement frequency equals 4/5 exactly, and the largest least-mismatch index.
   Apply the same steps to the two concrete class members of computation 1 and to RS(B,k) blocks where feasible.
4. **The family RS(B,k), B in {2,3,4}, k = 1..16** (k*B and 2^k bounded so the run stays within ten minutes).
   Exact block law P_k (2^k records); exact block TV T_k; certified Bhattacharyya enclosure BC_k from rational
   square-root endpoints. Certified depths: T(h) > 1/2 for every h >= k*n_half, from T(nk) >= nc/(1+nc) with
   c = 1 - BC_k upper; T(h) <= 1/10 for every h <= k*n_tenth, from T(nk) <= min(n*T_k, sqrt(2n(1 - BC_k lower))).
   Both depths are checked minimal or maximal for their rules. Also the memory in bits of each member.
5. **Brute-force mechanics check.** For small h*B, enumerate every fresh-bit string through an explicit
   state-machine implementation of RS(B,k) (seed register, interval, phase, clearing) and compare the record law
   with the product of block laws from computation 4.

## Decision rule

- **Class.** Over green controls: if every enumerated dyadic chain's every recurrent class shows a mismatch at
  some n <= |C| with nonzero characteristic-polynomial value, and the base-5 countercontrol shows an exact match,
  print the class verdict that bounded persistent state does not escape the obstruction, with the counts measured.
  If any dyadic chain has no mismatch for n <= |C|, the proof route is contradicted: print VOID, exit 2, and report
  the chain.
- **Family.** For each tested (B,k): if the certified c is positive, report the measured certified depths for
  that member; otherwise report it as not certified at the working precision. The family verdict is generated
  from those entries.
- **Resource statement.** Generated from the measured table: certified failure depth against memory bits for each
  B, together with the class statement (finite failure for every bounded memory) and the `a2_depth_v7/` value for
  unbounded memory. The growth form is reported as measured for this family only; no law is fitted.
- All verdict text is generated from measured values. A failed required control prints VOID and exits 2.

## Controls and countercontrols

- **K1 memoryless reproduction** (computation 1): digest, A, B, exact T(1..4), T-digests h<=64, generic-engine
  agreement h<=12.
- **K2 retained-seed reproduction** (computation 2): every retained exact value and display string.
- **K3 engine positive control:** a base-5 source with exact agreement law 4/5 gives T=0 through h=12 in the
  generic engine.
- **K4 base-5 countercontrol for step (4):** the enumeration with one fair five-valued symbol per slot must find
  chains whose stationary run law matches (4/5)^n for every n <= |C|. This shows the check can fail and that the
  dyadic source is load-bearing.
- **K5 marginal-insufficiency control:** there must be dyadic chains whose stationary agreement frequency equals
  4/5 exactly (a frequency-only test would miss them); for each, the mismatch must be found at some n >= 2.
- **K6 unbounded-memory countercontrol:** RS(B,k) with k >= h equals the `a2_depth_v7/` retained-seed law on h
  reads, so the obstruction appears only through the finite k; the bound 1/(2^B - 2) at every depth is preserved.
- **K7 certified enclosures:** square-root endpoints verified by squaring; for every (B,k,n) with n*k <= 16 the
  exact T(nk) of the product law lies inside the certified bracket.
- **K8 brute-force mechanics** (computation 5).
- Mutants, kept with their script and output: one per control (grid constant, cut rounding, mismatch range limited
  to n=1, base-5 replaced by base-4, square-root endpoint rounding, missing restart, depth off by one, wrong initial
  phase). Each must make the checker fail on the named control.

## Invariant -> checkpoint table

| invariant asserted | checkpoint |
| --- | --- |
| the memoryless controller rebuilt is the executed one | K1 digest and A, B equality |
| the record engine is faithful | K1 generic-engine equality, K3 zero TV |
| the retained-seed reset is the earlier one | K2 value equality |
| step (4) holds on every enumerated dyadic chain | computation 3, VOID on any exception |
| the step-(4) check can fail | K4 base-5 exact match |
| a frequency-only test is insufficient | K5 |
| the obstruction needs bounded memory | K6 |
| certified depths are valid and tight for their rules | K7 and the minimality checks |
| RS(B,k) mechanics equal the product law | K8 |
| outputs are deterministic | byte-identical replay under -I -B and -I -B -O |

## Existing results to preserve

The `a2_depth_v7/` verdict, A, B, T table and class statement, and its retained-seed values, must be reproduced
unchanged (K1, K2). The `a2_efficiency_v6/` h=3 certificate is not touched. No existing file is edited.

## Scope fixed in advance

- **Would establish:** a proved statement, with its finite step checked exactly on the listed chains, that every
  bounded-state controller with fixed fair dyadic fresh randomness per slot has T(h) -> 1 on this protocol;
  certified finite-depth failures and a measured memory-depth table for RS(B,k) at the tested sizes.
- **Would not establish:** any rate of failure for the class; anything about controllers with bounded private
  memory but unbounded public state (an unbounded clock or full-record dependence), time-dependent updates,
  growing per-slot blocks, non-dyadic sources, other protocols or worst-case adaptive policies; the minimal memory
  growth that keeps T bounded; anything about A1, native sourcing or OI.
- Deliverables: PLAN.md, REPORT.md, checks.py, result.json, PROVENANCE.json, SHA256SUMS and a mutants directory,
  with byte-identical normal and -O replay. No push, dispatch, F/E designation, merge or #885 write.
