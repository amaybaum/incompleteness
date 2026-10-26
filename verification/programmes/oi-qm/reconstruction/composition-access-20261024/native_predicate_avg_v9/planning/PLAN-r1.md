# Passive native readout under a declared background prior

26 October 2026. Draft plan for Issue #929 (NP-AVG-1), to sit beside
`native_predicate_v8/` under #912 (or a linked successor draft from a current
`D`). It is fixed before any checker exists and is committed alone. No
observer access, native storage, compilation, clock, gate or premise is
adopted. #885 is read-only. Items marked **(open)** are proposals the owner
fixes before the plan is committed; they are collected in the last section.

## Choice of sub-question

`native_predicate_v8/` is `NEGATIVE_FOR_CONSTRUCTION` for class C(4, 16) in the
scaled control, with the law required conditional on the whole background C0.
Its scope leaves open a law that holds only after averaging over private
backgrounds, and names that branch together with fresh pads: conditioning on
C0 is what stops background bits acting as fair pads. The composition contract
(`REPORT.md:57-69`, "Fresh resources") allows a seed to be averaged with its
advertised law only after its law is established conditional on the public
history and on every non-seed variable the stage uses. This plan tests whether
v8's negative depends on the pointwise convention, for read sets of at most k
site-times, with that freshness condition enforced.

## Fixed question

Construction class C_avg(4, 16, k): v8's class C(4, 16) restricted to read
sets R of at most k native site-times (whole raw triples, Manhattan distance at
most 4 from q9, slices −1 through n+17), with no gate, pad or added source.
The flag is any predicate A′ of the public record; it need not be v6's A.

Is there an R in the class whose public record has the complete v6 law in the
contract's cone form, averaged over the background prior π_bg declared below,
with a conditional-freshness certificate for every background bit acting as a
pad, holding against the carrier and against every later public port within
the horizon T_h?

## Objects and notation (scaled control)

All geometry is v8's: q9 at the origin, n = 6 in place of L, sources
G = (F8, F10, F9) at (−7, 0, −1), (−7, 0, 1), (−8, 0, 0) in the current
initial slice, the complete six-neighbour two-slice rule
x_t = x_{t−2} ⊕ H(Σ_e x_{t−1}(· + e)), H(A, B, D) = (B, D, A ⊕ BD), region of
129 sites, slices −1..23, 3,225 site-times.

- **Phase Φ** (private, the v6 carrier boundary): pool (q8, q10, m) at n+1, the
  other three neighbours at n+1, V = q9 at n+2, old q9 at n. J = (Y, R, Z) is
  read from the pool as in v8 (`checks.py:314-318`).
- **Public record Π_R** = (p, V, N_old, w_R): p the old whole-q9 record, V the
  single whole-V record, N_old the scaled old port stream (below) at slices
  0..n, w_R the whole triples at R.
- **Scaled port (open).** One port at (0, 0, −3), v7's scaled position
  (`delayed_history_v7/checks.py:180`). G reaches it first at slice 9 = n+3,
  after the old record ends; the offsets over n are 3, 5, 5, as in v7. Its
  whole triple is public at every slice 0..T_h.
- **Extended public record E_R**: the port at slices n+1..T_h, and the stream
  closure of R: every slice from −1 through T_h at every site of R.
- **Target law.** With s = p.B and j = (y, r, z), t1(s)_j = n(y ⊕ s, r ⊕ s)
  with n(00, 01, 10, 11) = (5, 0, 4, 1), and t0 = 8 − t1. A value π of a public
  tuple Q with p.A = 0 and positive probability is *accepted-law* if
  Pr(J = j | Q = π) = t1_j / 20 for every j, and *rejected-law* if it equals
  t0_j / 44. Law(Q) holds if every such π is one of the two; A′(π) is 1 or 0
  accordingly. Values with p.A = 1 are retained and carry no requirement (v6
  offers no carrier there).

## Prior and conventions

**π_bg (frozen):** i.i.d. fair on every non-source initial variable, both
initial slices, the infinite lattice; G uniform on 512 values and independent
(Native A's source law). The joint prior is the product law π on all initial
variables.

Three conventions for computing Law(Q):

- **P (pointwise):** conditional on the whole C0, as in v8. Frames: v8's
  sixteen families and the zero background.
- **A (averaged):** under π, conditional on Q only. This is the cone form the
  question asks for.
- **G (frame-conditioned):** conditional on the *frame*, the background
  variables in the union of the backward cones of Φ and N_old, and averaged
  under π_bg over every other background variable. Averaging is then exactly
  over variables independent, by construction, of the public history and of
  every input the carrier uses: the contract's licensed form. Frames: the
  values of v8's sixteen families on the frame, and the zero frame.

If Law holds in P on every C0 with one accept map, it holds in G; if it holds
in G on every frame with one accept map, it holds in A (each is a mixture of
the finer one). The converses fail. Because G is checked only on seventeen
frames, a G result never implies an A result here.

## Freshness certificate

For an R with Law_A(Π_R):

- **F1a, against the carrier (exact, convention A).** w_R is conditionally
  independent of Φ given (p, V, N_old, A′(Π_R)): the record carries no
  information about the stored phase beyond its flag. v6's pointer
  (pad_A, A, pad_D) satisfies it; a pad correlated with a hidden input does
  not.
- **F1b, against every stage input (convention G, seventeen frames).**
  Law_G(Π_R) holds on every frame with the same A′ as a function of Π_R.
- **F2, against later public ports (exact, convention A).** Law_A(Π_R ∪ E_R)
  holds with A′ unchanged as a function of Π_R: the port through T_h and R's
  stream closure carry no further information about J.

Unrestricted later native access is not a port. The dynamics is a bijection on
slice pairs, so a later slice pair on a large enough window determines every
initial variable, and no background bit is fresh against it. The later public
ports are therefore exactly those of E_R.

## Exact reductions (written proofs in the report; each gated by a control)

- **L1, parity.** x at (c, t) depends only on initial variables whose
  space-time parity |c| + t matches. Φ, p, V and G all lie in the even class.
  Under π every odd-class quantity is independent of every even-class
  quantity, and under P or G it is a function of background alone, so
  odd-class read samples and port samples are dropped jointly from every law.
- **L2, uniform slice pairs.** Under π the slice pair (t−1, t) is i.i.d. fair
  on every finite window, for every t (induction: x_{t+1}(c) = x_{t−1}(c) ⊕ f,
  with x_{t−1}(c) fair and independent of slice t). Convention A is computed in
  the coordinates of the pair (n+1, n+2), where Φ is seven triples and every
  other quantity is a forward or backward image. L2 is used only under the
  fair prior.
- **L3, free-extreme elimination.** Let a site-time lie d ticks after the later
  slice of the coordinate pair (initial slice 0, or reference slice n+2), and
  let u be the triple in that slice at exact distance d along a lattice axis;
  backward in time, the same with the earlier slice of the pair (reference
  slice n+1). Then for every fixed value of all other variables the
  site-time's triple is a bijection of u (unique straight path; H is a
  permutation). If no other
  retained quantity has u in its cone, that triple is uniform and independent
  of all the others, and is removed. The rule is iterated. Cones are exact
  over-approximations of dependence, so the rule is sound.

After L1 to L3, the remaining quantities are enumerated exhaustively over the
union of their supports: in A, reference-pair variables; in G and P, G and the
non-frame background, with the frame fixed. A record whose residual support
exceeds **S_max = 27 bits (open)** is *not decided* for that convention and
check. Counts are integers; every probability is a `Fraction`. The biased-prior
control K4 is computed in initial coordinates without L2 or L3.

## Computation

1. v8's domain and geometry (x0, x6, x7 as in v8; every read tail-free at
   actual L).
2. For every R with |R| ≤ **k = 2 (open)**: all 3,225 singletons and all
   5,198,700 pairs. Stream closure is not imposed on R (with |R| ≤ 2 it would
   leave only the two initial slices); it enters through F2.
3. For each R: Law_A(Π_R), then, if it holds, F1a, F1b and F2; Law_P on the
   seventeen frames (K1b ties it to v8); Law_G reported.
4. Horizon **T_h = 46 = 2(n+17) (open)**, twice the last read slice, by
   analogy with v7's bound H ≤ 2L.

## Decision rule

Precedence, first match:

- **VOID:** any required control fails, or any internal consistency check
  fails.
- **POS_A:** some R has Law_A(Π_R), F1a, F1b and F2, and passes the
  maximum-skepticism protocol below.
- **PADS_NOT_FRESH:** every R in the class is decided for Law_A; at least one
  has Law_A(Π_R); each such R has a decided failure of at least one of F1a,
  F1b and F2, with an exact witness recorded (value of Π_R and Φ, frame, or
  port value).
- **NEG_BOTH:** every R in the class is decided for Law_A and none has it, and
  K1 holds (v8's pointwise negative for every R in C(4, 16)).
- **NOT_DECIDED:** otherwise. The undecided read sets and checks are listed.
  This is scope, not a verdict.

The report prints the decided counts per convention and check, and the
decided status of each site-time on which v8 found G-dependent information.
Verdict text is generated from the measured values.

## Required controls (each can fail)

- **K0, domain.** n, ρ, τ_max, k, T_h, port, S_max and prior equal the frozen
  values; the scope string is generated from them.
- **K1a, provenance replay (precondition).** v8's `checks.py` (blob
  `0a53c776`) output equals its `result.json` (blob `9ef92ae4`) byte for byte,
  normal and `-O`. It tests the inputs, not the new checker.
- **K1b, pointwise reproduction.** The new engine in P reproduces, field for
  field, each family's `native_table_sha256`, block histogram, law-good
  partitions per V value and `admissible_R_exists` in v8's `result.json`, and
  its zero-background diagnostic.
- **K2, planted positive.** w = (A, Y ⊕ c, 0), c one bit of an initial
  background triple outside every cone within T_h: Law_A, F1a, F1b and F2 pass;
  Law_P fails on every frame.
- **K3, planted reuse.** K2 with c added to the port at slice n+5: Law_A(Π_R)
  passes and F2 fails; classified PADS_NOT_FRESH.
- **K3b, pad correlated with a hidden input.** w = (A, Y ⊕ o.B, 0), o the
  private +x neighbour at n+1: Law_A(Π_R) passes and F1a and F1b fail.
- **K3c, fair after heralding.** K2 with c2 a second fresh bit, a public herald
  [c = c2] at slice 0 and c2 on the port at slice n+5: c is fair given each
  herald value (reported), and F2 fails.
- **K4, biased prior.** Under π_bg with Pr(1) = 1/4 on every non-source bit
  **(open: or on c alone)**, K2's plant fails Law_A; the TV from the target law
  is reported exactly.
- **K5, right rate, wrong flag.** (f, 0, 0) with f = [four fresh fair bits
  encode a value below 5]: rejected by Law_A, and the complete flag and
  offered-carrier TV equals v6's 1/8 for both s.
- **K6, joint hazard.** (u0, u1) = (U_3(p0), U_3(p1)) of the transport audit's
  zero-background counterexample (sources a at (0, 3, 0), b at (−2, 1, 0),
  reads at (0, 0, 0) and (1, 1, 0), tick 3; both equal H(H(H(a) ⊕ H(b)))),
  built in a separate block. Each of w1 = (A, Y ⊕ u0.B, 0) and
  w2 = (0, R ⊕ u1.B, 0) alone passes Law_A and F1a; the pair fails, and the
  joint (u0, u1) support is 8 of 64. A per-cell check that accepts the pair
  fails the control.
- **Z0, zero background.** With π_bg replaced by the point mass on zero,
  convention A equals P on the zero background (v8's zero diagnostic
  reproduced) and K2 fails.
- **L1c.** On every site-time of the domain, the exact cone dependence set has
  the stated parity; a planted odd-class read leaves every law unchanged.
- **L2c.** On small windows, exhaustive enumeration in initial coordinates and
  the reference-pair computation give identical joint laws for Φ, p, V and
  three nearby site-times; under the bias-1/4 prior they must differ.
- **L3c.** On every subset of a pool of planted and native quantities with
  small cones, the eliminated law equals brute force; a planted quantity that
  shares its extreme triple with another must not be eliminated, and brute
  force shows its dependence.
- **x1, x2, x6, x7** as in v8 (scalar evaluator; Native A's pool bijection and
  seven-site inverse, used in P and G; v7's carrier table; tail-freeness and
  early constancy).
- **Determinism.** Normal and `-O` output byte-identical to `result.json`.

## Mutants

A mutant script, kept with its output, breaks each required control in turn;
each must give `VOID`, exit 2, naming its target. Three injection mutants must
change the verdict: K2's plant written into a native even-class site-time
gives POS_A; adding K3's reuse to it gives PADS_NOT_FRESH; disabling L3's
sharing test is caught by L3c. A mutant counts as caught only when it fails on
its named case.

## Maximum-skepticism protocol for POS_A

Before POS_A is reported, on the actual winning R:

1. **Reuse.** Add to the port, at slice n+5, the residual variables Law_A(Π_R)
   averages over. F2 must then fail; if it does not, the verdict is VOID.
2. **Joint hazard.** The joint law of all of R's residual pad variables, with
   each other and with Φ, is computed exactly and reported with its support;
   per-cell freshness is not accepted.
3. **Second engine.** An independent implementation in initial coordinates,
   using neither L2 nor L3, recomputes Law_A, F1a and F2 for R on a window that
   covers R's residual support. If that exceeds the cap, a separate-agent
   review's independent implementation is required before any report.
4. **Prior and frames.** Law_A for R under bias 1/4 and under the zero
   background (reported); F1b on all seventeen frames (required).
5. **Geometry.** Every site-time of R is tail-free at actual L (x7).
6. **Scope.** POS_A is stated as conditional on π_bg, on Native A's source law,
   on the scaled control with one port, and on supplied access. F1b covers the
   seventeen frames; a written argument for every frame is owed before any
   wider claim.

## Reported only

Law_G for every decided R; the decided and undecided counts; residual-support
histograms; for each site-time with G-dependent information in v8, its
eliminated or residual status in A and G.

## Invariant → checkpoint

| invariant asserted | checkpoint |
| --- | --- |
| domain and parameters are the frozen ones | K0 |
| inputs are v8's, unchanged | K1a |
| pointwise engine is v8's | K1b, Z0 |
| native fields are the native rule | x1 |
| operands are Native A's pool and V | x2 |
| actual-L geometry and tail-freeness | x6, x7 |
| parity reduction is exact | L1c |
| reference-pair change of variables is exact under π, and only under π | L2c |
| elimination is sound and does not fire on shared extremes | L3c, L3 mutant |
| averaging can admit a fresh-pad record that P rejects | K2, injection mutant |
| later-port reuse is detected | K3, K3c, protocol 1 |
| a hidden-input pad is detected | K3b |
| the result depends on the prior where it should | K4 |
| a right-rate wrong flag is rejected | K5 |
| joint pad laws are checked, not per-cell | K6, protocol 2 |
| averaging is the only difference from P | Z0 |
| every control can fail | mutant campaign |
| result is deterministic | normal and `-O` output equal `result.json` |
| arithmetic is exact | integer counts and `Fraction` only; no float in the checker (static check) |

## Scope

- No claim at actual L, where there are eight ports and two-port simultaneous
  arrival (v7).
- Read sets of at most k site-times only; larger sets are outside the class.
- One background prior; a POS_A moves the burden onto it.
- One scaled port; the eight actual ports are not modelled.
- No access rule adopted; a passive flag is not an observer read.
- No native storage, gate, reset or compilation implied; the carrier stays in
  v6's supplied logical storage.
- No A1/A2 statement. A positive would be a conditional F2 ingredient, not an
  equivalence step (`PROGRAMME.md:40`, `:634`).
- A negative excludes C_avg(4, 16, k) in the scaled control under π_bg, not OI,
  not native predicates with gates, prepared sources or larger reads.

Results to preserve: v8's pointwise negative (K1), v6's logical law (x2, K2),
v7's geometry (x6).

## Resources (§A.40, §A.43)

Standard library only, exact integers and fractions, explicit exceptions; the
checker imports no author engine and reads no repository file. Run locally
before any push: K1a (about one minute), the L1c to L3c self-tests on small
windows, compilation and static checks. The sweep over 5.2 million pairs, the
F checks and the mutant campaign run in CI, sharded by the first cell of R.
A dry-run mode prints the shard plan and set counts without evaluating any law;
if the projected cost exceeds **8 runner-hours (open)** the run stops and
reports the partial state. Adding the workflow and every dispatch need owner
approval (§A.43 item 4). No F/E designation, merge or special launch follows.

## Dependencies

- **v8 retention.** v8 is cited at `fc452ea8`, which is not reachable from
  `main` (checked against `main` at `52e2db40`). Under §A.42 no result citing
  it lands before v8's files are on `main`, through #912's landing or
  otherwise.
- **G9 contract:** #912 `REPORT.md:57-69`.
- **#923 (OI-PE-1).** PE-01 uses no background prior of this kind. Its priors
  are a uniform initial law on its own generator state (PE-01 `PLAN.md:56`),
  a uniform tape (`:45`) and uniform polynomial families (`:70`); its observer
  memory starts at a fixed value. There is no private lattice background
  averaged against a pointwise convention. π_bg is compatible with those
  uniform priors; a later non-uniform environment prior in either thread needs
  coordination.
- **Native A** (#910, on `main`) and the transport audit and `history_v11`
  (on `main`, the sources of K6).

## Relation to PE-01's open question

PE-01's open question on charged lookup tables and description complexity
does not bear on this plan: the predicate A′ here is unrestricted and
uncharged, and that question belongs to PE-02.

## Open items for the owner

1. **k = 2.** The smallest k at which a predicate can combine two native cells;
   k = 1 is the shape of v6's single pointer. k = 3 (about 5.6 × 10⁹ sets)
   needs a structural restriction, for example to sets connected by shared
   cones.
2. **S_max = 27 residual bits.** Covers Φ's seven triples plus two, and fits
   2^27-lane bit-slicing (16 MiB per plane). Chosen for feasibility, not by
   anticipated outcome.
3. **T_h = 46.** Twice the last read slice. An alternative is v7's form, the
   last first G arrival at the port.
4. **Port model.** One port at (0, 0, −3) as in v7, public from slice 0. Under
   averaging the old port records are random public functions of the
   background (v7: exposed pre-tail bank reaches q8, m, q9, q9 ± y and q9 + x
   at L+1 and L+2), so they cannot be dropped as in v8; v8's scaled control has
   no port. Alternatives: several ports, or a declared contract without ports,
   which could not support POS_A.
5. **Freshness split.** F1a exact; F1b on seventeen frames. Whether POS_A
   should also require a written all-frame argument before it is reported, or
   only before wider claims.
6. **Stream closure in F2,** in both directions. v8's positive rule required
   stream-closed R.
7. **K1 restated** as K1a (precondition) and K1b (field equality); a
   byte-for-byte reproduction of v8's file by new code is not a meaningful
   control.
8. **K6 instantiation** from the transport audit's construction; its "8 of
   64" also appears as `history_v11`'s access control.
9. **K4 scope:** bias on every non-source bit, or on c alone.
10. **Frames:** v8's sixteen families plus zero.
11. **Location:** `native_predicate_avg_v9/` beside v8, on #912's guiding
    draft or a linked successor from a current `D`.
12. **CI budget:** 8 runner-hours.
