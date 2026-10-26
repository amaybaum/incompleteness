# Passive native readout under a declared background prior

26 October 2026, draft r2. A plan for Issue #929 (NP-AVG-1), to sit beside
`native_predicate_v8/` (location: O6). It revises draft r1 (`PLAN.md`, SHA-256
`b0be3278757c193e76465601793cda6d70e777d5f49f38296a8dac1c348d9b00`) after the
pre-freeze review (`REVIEW.md`, SHA-256
`4d77c7c23d6b08d3467b0096a08365fe9ee7cce27f432de5018819bd723583dd`). It is
fixed before any checker exists and is committed alone, on a base that
contains `fc452ea825b986a3babab5d110626e0019c39847`. No observer access, native
storage, compilation, clock, gate or premise is adopted. #885 is read-only.

The owner decisions O1–O9 (last section) are open. Each is written in at the
value the review recommends, and the plan is complete at those values; the
alternative for each is stated in the same section.

## Choice of sub-question

`native_predicate_v8/` is `NEGATIVE_FOR_CONSTRUCTION` for class C(4, 16) in the
scaled control, with the law required conditional on the whole background C0.
Its scope leaves open two branches: a law that holds only after averaging over
private backgrounds, and fresh pads. They are one open branch, because
conditioning on C0 is what stops background bits from acting as fair pads.

The composition contract (#912 `REPORT.md:57-69`, "Fresh resources") allows a
seed to be averaged with its advertised law only after two things are
established: its law conditional on the public history, and its law
conditional on every non-seed variable the stage uses.

This plan tests whether v8's negative depends on the pointwise convention. It
restricts to read records of at most k stream items and enforces that freshness
condition.

## Fixed question

**Class C_avg(4, 16, k).** Its elements are v8's stream items
(`native_predicate_v8/checks.py:503-508`). An item (x, t) is a site x within
Manhattan distance 4 of q9 and a last slice t in −1..n+17, read as whole raw
triples at every slice −1..t. There are 3,225 items.

A read record R is a set of at most k items at distinct sites. Two items at
one site reduce to the longer of the two. No gate, pad or added source is
used. The flag A′ is any predicate of the public record, which includes R's
whole backward-closed streams. A′ need not be v6's A.

**The question.** Is there an R in the class that meets both conditions below?
- Its public record has the complete v6 law in the contract's cone form,
  averaged over the background prior π_bg declared below.
- A conditional-freshness certificate holds for every background bit acting as
  a pad: against the carrier, against every input of the stage, and against
  the declared later public reads through T_h.

## Objects and notation (scaled control)

All geometry is v8's:
- q9 at the origin, with n = 6 in place of L;
- sources G = (F8, F10, F9) at (−7, 0, −1), (−7, 0, 1) and (−8, 0, 0) in the
  current initial slice;
- the complete six-neighbour two-slice rule
  x_t = x_{t−2} ⊕ H(Σ_e x_{t−1}(· + e)), with H(A, B, D) = (B, D, A ⊕ BD);
- a region of 129 sites.

- **Carrier boundary Φ** (p and V public; the rest private): the pool
  (q8, q10, m) at n+1, the other three neighbours at n+1, V = q9 at n+2, and
  old q9 at n, recorded as p. J = (Y, R, Z) is read from the pool as in v8
  (`native_predicate_v8/checks.py:314-318`).
- **Port stream N.** One scaled port at (0, 0, −3), v7's position
  (`delayed_history_v7/checks.py:180`). Its whole triple is public at every
  slice 0..T_h. N[0..n] is pre-use history. N[n+1..T_h] is a later read. G
  first reaches the port at slice n+3 = 9, at offsets over n of 3, 5 and 5, as
  in v7. (The eight actual-L ports are not modelled.)
- **Public record** Π_R = (p, V, N[0..n], w_R), where w_R is every triple read
  by R's items.
- **Declared later reads** 𝓛_R (O4). Each member S consists of:
  - (i) the port N[n+1..T_h];
  - (ii) each item's own continuation, its samples after its last slice
    through T_h;
  - (iii) any set of at most k later segments {(x, u) : t_R < u ≤ t′}, where x
    is a region site, t′ ≤ T_h, and t_R is R's last slice.
- **Target law.** Let s = p.B and j = (y, r, z). Then
  t1(s)_j = n(y ⊕ s, r ⊕ s), with n(00, 01, 10, 11) = (5, 0, 4, 1), and
  t0 = 8 − t1. Take a value π of a public tuple Q that has p.A = 0 and positive
  probability.
  - π is *accepted-law* if Pr(J = j | Q = π) = t1_j / 20 for every j.
  - π is *rejected-law* if Pr(J = j | Q = π) = t0_j / 44 for every j.

  Law(Q) holds if every such π is one of the two, with A′(π) = 1 or 0
  accordingly. Values with p.A = 1 are retained and carry no requirement,
  since v6 offers no carrier there.

## Prior, conventions and seed declaration

**π_bg (frozen):** i.i.d. fair on every non-source initial variable, in both
initial slices, on the infinite lattice. G is uniform on 512 values and
independent (Native A's source law). The joint prior π is the product law on
all initial variables.

- **P (pointwise):** conditional on the whole C0, as in v8. Frames: v8's
  sixteen families and the zero background (O8).
- **A (averaged):** under π, conditional on the public tuple only. This is the
  averaging the question names. It is a necessary screen: if Law_G holds on
  every frame with one accept map, Law_A holds, because A is a mixture of G.
- **G (licensed under the seed declaration):** conditional on the frame, and
  averaged under π_bg over the seeds. Seeds are averaged as fair on the
  infinite lattice, including where v8's families are zero outside radius 27.
  - **Frame:** the background variables inside the light cones of Φ, of p and
    of N[0..n].
  - **Seeds:** every other background variable.

  The declaration is conservative. Background inside those cones that the
  history does not reveal, or that Φ does not depend on, would be an
  admissible seed under the contract, but G freezes it. A G failure is
  therefore an exact witness against this declaration only.

If Law holds in P on every C0 with one accept map, it holds in G on every
frame. The converses fail. G is checked on the sampled frames unless the
frame-uniform certificate (O3) applies.

## Freshness certificate

For an R with Law_A(Π_R), each part is required in both conventions. A is the
exact screen; G is the licensed check, on each frame.

- **F1a, against the carrier.** w_R is conditionally independent of Φ given
  (p, V, N[0..n], A′(Π_R)) under A, and given the same tuple and the frame
  under G. The record carries no information about the stored phase beyond its
  flag.
- **F1b, against every stage input.** Law_G(Π_R) holds on every frame, with
  one A′ as a function of Π_R.
- **F2, against later reads.** For every member S of 𝓛_R,
  Law(Π_R ∪ S) holds with A′ unchanged as a function of Π_R, under A and under
  G on every frame.

Later reads are the declared family 𝓛_R. Unrestricted later native access is
excluded: a large enough later window determines every initial variable,
including Φ, so it contradicts the supplied access contract on which the v6
and v7 reference rests. Under A, L3 masks most samples of a single fixed port.
F2 against the port alone would therefore be close to vacuous for a native R,
which is why item (iii) is included (O4).

## Exact reductions (written proofs in the report; each gated by controls)

- **L1, parity.** The value at (c, t) depends only on initial variables of
  matching space-time parity, |c| + t mod 2. Φ, p, V and G all lie in the even
  class. Under π, every odd-class quantity is independent of every even-class
  quantity. Under P or G, an odd-class quantity is a function of the
  odd-class background alone. Odd-class read and port samples are therefore
  dropped jointly from every law.
- **L2, uniform slice pairs.** Under π the slice pair (t−1, t) is i.i.d. fair
  on every finite window, for every t. The proof is by induction, forward and
  backward: x_{t+1}(c) = x_{t−1}(c) ⊕ f, where x_{t−1}(c) is fair and
  independent of slice t. L2 needs G uniform as well.
  - Convention A is computed in the coordinates of the pair (n+1, n+2). There
    Φ is seven triples, and every other quantity is a forward or backward
    image.
  - L2 is used only under the fair prior.
- **L3, free-extreme elimination.**
  - *Setting.* A site-time lies d ticks after the later slice of the coordinate
    pair: initial slice 0, or reference slice n+2. Let u be the triple in that
    slice at exact distance d along a lattice axis. Backward in time, the same
    holds with the earlier slice of the pair, reference slice n+1.
  - *Bijection.* For every fixed value of all other variables, the site-time's
    triple is a bijection of u. The proof is the unique straight path, and H
    is a permutation.
  - *Removal.* If u is fair and no other retained quantity has u in its light
    cone, the triple is uniform and independent of all the others, and is
    removed.
  - *Iteration.* The rule is iterated. Removing a quantity can only free
    further extremes, so the result does not depend on the order, and the
    eliminated set is jointly independent of the retained set. The report
    writes out the induction.
  - *Soundness.* Light cones over-approximate dependence, so the rule is sound.
  - *Scope.* L3 applies only to fair variables: every variable under A, and
    the seeds under G. It never applies to frame variables.

After L1–L3, the remaining quantities are enumerated exhaustively over the
union of their supports:
- in A, reference-pair variables;
- in G, G and the residual seeds, with the frame fixed.

If a record's residual support exceeds **S_max = 27 bits** (O9), that record is
*not decided* for that convention and check. Counts are integers, and every
probability is a `Fraction`.

**Later reads (F2).** For each R, L3 is first run on Π_R, Φ and the union of all
members of 𝓛_R. The family is downward closed and elimination is monotone, so
a later sample eliminated in the union is eliminated in every member.
- If the union leaves no later sample, F2 holds for every member.
- Otherwise, let Ω_R be the residual later samples. Every member is restricted
  to Ω_R and checked exactly. If the count or a residual exceeds the cap, F2 is
  not decided.

## Computation

1. v8's domain and geometry: x0, x6 and x7 as in v8, so every read is
   tail-free at actual L.
2. The class at **k = 2** (O1, O2): 3,225 single items and
   C(129, 2) · 25² = 5,160,000 two-site pairs, 5,163,225 read records in all.
   The verdict sweep is over native records only. Every planted control is a
   separate run of the same classifier, outside the sweep.
3. For each R:
   - compute Law_A(Π_R);
   - if it holds, compute F1a, F1b and F2 in A and in G on every frame;
   - report Law_G on every frame.

   The P engine implements v8's full search over every R in C(4, 16) on each
   frame (K1b). Its per-R status is v8's.
4. **Horizon T_h = 46** (O9): twice the last read slice, by analogy with v7's
   bound H ≤ 2L.
5. **Shards and merge** (§A.44).
   - The sweep is sharded by the first item's site index.
   - Each shard writes `shard-<s>.json` in a stated schema, containing:
     - the parameter digest;
     - the exact index ranges it covers and their count;
     - per-R codes (law status in A, reason code, decided or not);
     - counts per reason code;
     - witnesses;
     - residual-support histograms;
     - its own SHA-256.
   - The merge reads only these files and the shards' exit status. It verifies
     that the union of covered ranges is exactly the class, with no overlap,
     and recomputes the totals.
   - NEG_BOTH or PADS_NOT_FRESH can print only after that check passes. A
     missing, failed or non-deterministic shard gives NOT_DECIDED, with the
     shard named.

## Decision rule

Precedence, first match. The verdict text is generated from the measured
values.

- **VOID:** any required control or any internal consistency check (IC1–IC6)
  fails.
- **POS_A:** some R meets every one of the following:
  - Law_A(Π_R);
  - F1a, F1b and F2 in both conventions;
  - the frame-uniform certificate (O3);
  - the protocol below, including the separate-agent reproduction.
- **POS_A_SAMPLED_FRAMES:** as POS_A, except that the G parts are established
  on the sampled frames only. Its text says: "freshness against stage inputs
  checked on seventeen frames; not certified on other frames".
- **PADS_NOT_FRESH:** every R in the class is decided for Law_A, at least one
  has Law_A(Π_R), and each such R has a decided failure of F1a, F1b or F2, in
  either convention, with an exact witness. The text states:
  - the counts per reason code;
  - that the failures are relative to the seed declaration (seeds = background
    outside the light cones of Φ, p and N[0..n]);
  - that it does not assert the pointwise convention beyond that declaration.
- **NEG_BOTH:** every R in the class is decided for Law_A and none has it, and
  K1 holds (v8's pointwise negative for every R in C(4, 16)). The text gives
  the counts by mechanism: records reduced to independence of Φ by L1 or L3,
  and records enumerated that failed.
- **NOT_DECIDED:** otherwise. The undecided records and checks are listed.
  This is scope, not a verdict.

Separate-agent reproduction (protocol step 3c) is not a computation of the
checker. A candidate that passes everything the checker computes prints as
`POS_A_PENDING_REVIEW` or `POS_A_SAMPLED_FRAMES_PENDING_REVIEW`. The report
carries the unsuffixed class only after the review reproduces it.

**Reason codes**, printed with counts in every verdict:

| code | meaning |
| --- | --- |
| `F1a-A`, `F1a-G[frame]` | carrier leak |
| `F1b[frame]` | input-correlated pad, under the seed declaration |
| `F2-A[member]`, `F2-G[frame, member]` | later reuse |

## Internal consistency checks (any failure gives VOID)

- **IC1:** for every R and frame, Law_P on the frame implies Law_G on that
  frame, with the same A′.
- **IC2:** Law_G on every frame implies that the per-frame accept maps agree as
  functions of Π_R.
- **IC3:** F2, for any member, implies Law_A(Π_R), and likewise in G.
- **IC4:** probability mass is conserved: each class's J-law sums to its class
  probability, and the classes sum to 1.
- **IC5:** the shard union is the class, and the shards are disjoint.
- **IC6:** elimination does not depend on order, checked on a deterministic
  sample of R by reversing the elimination order.

## Required controls (each can fail)

**Domain and provenance**
- **K0, domain.** The following equal their frozen values, and the scope
  string is generated from them:
  - n, ρ, τ_max, k, T_h, S_max and the prior;
  - the item counts, 3,225 and 5,160,000;
  - the port geometry: first G arrival at slice 9, offsets 3, 5 and 5;
  - the SHA-256 of the sorted frame-coordinate list;
  - the frame list: v8's seeds with their `native_table_sha256`.
- **K1a, provenance replay (precondition).** v8's `checks.py` output equals its
  `result.json` byte for byte, in normal and `-O` runs (pins below). This tests
  the inputs, not the new checker.
- **K1b, pointwise reproduction.** The new P engine runs v8's full all-R
  search. For each family it reproduces, field for field:
  - `native_table_sha256`;
  - the block histogram;
  - the law-good partitions per V value;
  - `admissible_R_exists`;
  - the zero-background diagnostic.

  The expected values are constants transcribed from v8's `result.json`
  (SHA-256 above), since the checker reads no repository file.

**Planted records**
- **K2, planted positive.** w = (A, Y ⊕ c, 0), where c is one bit of an initial
  background triple outside every light cone within T_h. Law_A, F1a, F1b and
  F2 pass in both conventions. Law_P fails on every frame.
- **K3, planted reuse.** K2, with c appended in the clear to the later port
  record at slice n+5, as an extra public symbol rather than an XOR into the
  native triple. Law_A(Π_R) passes, and F2 fails in A and in G (code F2).
- **K3b, pad correlated with a hidden input.** w = (A, Y ⊕ o.B, 0), with o the
  private +x neighbour at n+1. Law_A(Π_R) passes. F1a fails in A and G, and
  F1b fails.
- **K3c, fair after heralding, then reused.** K2 plus a public herald [c = c2]
  at slice 0, in Π_R as pre-use history, where c2 is a second fresh bit. c2 is
  also appended in the clear to the port record at slice n+5. c is fair given
  each herald value (reported), and F2 fails.
- **K3d, fair after heralding, hidden input** (`REPORT.md:151-157`). K2 plus a
  public herald [c = o.B] in Π_R. c is fair given each herald value. Law_A(Π_R)
  passes, and F1a fails in A and G.
- **K4, biased prior** (O5). With Pr(c = 1) = 1/4 for c alone, K2's plant fails
  Law_A, and its TV from the target law is reported exactly. c is independent
  of every other quantity within T_h, so the joint law is an exact product with
  c's weighted factor.
- **K5, right rate, wrong flag.** (f, 0, 0), where f = [four fresh fair bits
  encode a value below 5]. It is rejected by Law_A, and the complete flag and
  offered-carrier TV equals v6's 1/8 for both s.
- **K6, joint hazard.**
  - *Construction.* (u0, u1) = (U_3(p0), U_3(p1)) of the transport audit's
    counterexample, built in a separate block by the general-prior engine GB:
    sources a at (0, 3, 0) and b at (−2, 1, 0) fair, everything else zero,
    reads at (0, 0, 0) and (1, 1, 0) at tick 3. Both equal H(H(H(a) ⊕ H(b))).
  - *Records.* w1 = (A, Y ⊕ u0.B, 0) and w2 = (A, R ⊕ u1.B, 0).
  - *Each alone* passes Law_A and F1a.
  - *The pair* fails Law_A, because it reveals Y ⊕ R. The joint (u0, u1)
    support is 8 of 64, and L3 must not eliminate either cell in the pair
    context. A per-cell check that accepts the pair fails the control.

**Engines**
- **GB, general-prior brute force.** A separate engine, in initial
  coordinates with every variable enumerated, accepts an arbitrary product
  prior. It is used on reduced instances: the 1D and 2D analogues of the rule
  on small windows, and K6's block.
- **Z0, averaging is the only difference from P.** On the reduced instances:
  - GB under the fair prior equals the A engine (L2/L3, the same code with the
    dimension as a parameter);
  - GB under the zero point mass equals the P engine on the zero background;
  - GB under bias 1/4 differs from the A engine wherever the A engine uses L2.

  In 3D, K2 with c fixed at 0 fails, and equals P.
- **L1c, measured dependence.** On every family, a deterministic sample of
  single initial-variable perturbations is applied in the native scalar
  evaluator:
  - no value changes outside the perturbed parity class;
  - at least one same-parity value changes in every sample, so the check is
    not vacuous.

  In addition, one law on a reduced instance, computed by GB without L1 and
  with an odd-class read included, equals the law without that read.
- **L2c, uniform pairs on reduced instances.**
  - On the exhaustive 1D instance (pair (1, 2) at one site, 2^24 worlds) and on
    a 2D instance, GB gives an exactly uniform pair under the fair prior.
  - The A engine's reference-coordinate laws for the Φ-analogue quantities
    equal GB's.
  - Under bias 1/4, GB's pair is not uniform.
- **L3c.** On every subset of a pool of planted and native quantities with small
  cones, the eliminated law equals GB's brute force. Two planted cases must not
  be eliminated: a quantity that shares its extreme with another, and an
  off-axis extreme at the same distance.
- **IM1, the image engine is the native rule.** On all sixteen families and the
  zero background, over all 512 worlds, the reference-coordinate forward and
  backward images evaluated from v8's native pair (n+1, n+2) reproduce v8's
  native value at every point of the domain through T_h: the region, the port
  and the initial pair.
- **IM2, L3 soundness on the sweep's own eliminations.** IM2 covers a
  deterministic sample of the eliminations the sweep performs (every 1,000th),
  and every elimination in any R that reaches Law_A or a witness. On each:
  - the image engine shows a bijection in u at four deterministic fixed values
    of the other variables;
  - perturbing u changes no other retained quantity.
- **FR, frame soundness.** On every family, a deterministic sample of seed
  perturbations leaves p, N[0..n] and Φ unchanged. This is the measured basis
  of the seed declaration.
- **W1, witness replay.** Every PADS_NOT_FRESH witness and every positive
  candidate class is recomputed by a residual enumerator written separately
  from the main one, using IM1-checked images.
- **x1, x2, x6, x7,** as in v8:
  - x1: the scalar evaluator;
  - x2: Native A's pool bijection and seven-site inverse, used in P and G;
  - x6: v7's carrier table;
  - x7: tail-freeness and early constancy.
- **ST, static checks.** An AST scan finds no floating-point literal or
  operation, no file read, and no import outside the stated standard-library
  modules or of any author engine.
- **Determinism.** Normal and `-O` output are byte-identical, per shard and
  for the merged result.

## Mutants

A mutant script, kept with its output, breaks each required control in turn.
Each must give `VOID` with exit status 2, naming its target. A mutant counts as
caught only when it fails on its named case.

The injection mutants run on a fixed restricted candidate set M:
- v8's two recurring two-block cells, (−2, 0, 0) at slice 6 and (2, 0, 0) at
  slice 10, as items;
- four further items fixed by index;
- the injected records.

They state per-record outcomes, not global verdicts:

| mutant | change | expected outcome |
| --- | --- | --- |
| I1 | K2's plant written into a native even-class site-time | that record passes Law_A, F1a, F1b and F2 in A and G |
| I2 | I1 plus K3's reuse | that record fails with code F2 |
| I3 | L3 accepts off-axis extremes | L3c gives VOID |
| I4 | L3's sharing test disabled | L3c or K6 gives VOID |

## Maximum-skepticism protocol for a positive candidate

These steps run on the actual candidate R before any positive class prints.

1. **Pads are load-bearing.** Take the residual variables Law_A(Π_R) averages
   over, excluding Φ's seven triples (in G, the residual seeds). Append them in
   the clear to the later port record at slice n+5.
   - F2 must then fail. If it does not, the result is VOID.
   - If that set is empty, R's record is a function of Φ and has no pads. The
     step is then recorded as not applicable, and is not VOID.
2. **Joint pad law** (report-only). The joint law and support of R's residual
   pad variables, with each other and with Φ. Under the seed declaration,
   P(U_R | H = h, frame, Φ) = ν holds by construction; FR checks the
   construction.
3. **Second engine.**
   - (a) IM2 runs on every elimination performed for R, exhaustively over u, on
     every frame.
   - (b) If R's support after L1 and L2 alone is at most S_max, R's laws are
     recomputed by brute force without L3.
   - (c) A separate-agent review recomputes, with its own implementation,
     Law_A, F1a and F2 for R and the G parts on the frames. Until it does, the
     checker's class carries `_PENDING_REVIEW`.
4. **Prior.**
   - For a planted pad, prior dependence is K4.
   - For a native R, the verdict text says "prior dependence not computed",
     unless (3b) applied and GB ran under bias 1/4.
   - R's law under P on the zero frame is reported.
5. **Geometry.** Every site-time of R is tail-free at actual L (x7).
6. **Verdict text** states the following, together with the frame scope:
   - the result is conditional on π_bg, on Native A's source law, on the
     scaled control with one port, and on supplied access;
   - the pads are initial background bits, whose fairness at actual L is the
     named F2-ledger item.

## Reported only

- Law_G on every frame for every decided R, including any R with sampled-frame
  passes and Law_A failing.
- Decided and undecided counts per convention and check.
- Residual-support histograms.
- For each site-time on which v8 found G-dependent information: its
  eliminated or residual status in A and in G.

## Invariant → checkpoint

| invariant asserted | checkpoint |
| --- | --- |
| domain, parameters, port geometry, frame definition and frame list are the frozen ones | K0 |
| inputs are v8's, unchanged | K1a, pins |
| the P engine is v8's search | K1b |
| native fields are the native rule (initial coordinates) | x1 |
| the reference-coordinate image engine is the native rule | IM1 |
| operands are Native A's pool and V | x2 |
| actual-L geometry and tail-freeness | x6, x7 |
| parity reduction holds for actual dependence | L1c |
| the reference-pair change of variables is exact under π, and only under π | L2c, Z0 |
| elimination is sound, also on the sweep's own eliminations, and does not fire on shared or off-axis extremes | L3c, IM2, I3, I4 |
| elimination does not depend on order | IC6 |
| the seed declaration is independent of history and carrier | FR |
| averaging can admit a fresh-pad record that P rejects | K2, I1 |
| later reuse is detected | K3, K3c, I2, protocol 1 |
| a hidden-input pad is detected | K3b, K3d |
| the result depends on the prior where it should | K4 |
| a right-rate wrong flag is rejected | K5 |
| joint pad laws are checked, not per-cell | K6 |
| averaging is the only difference from P | Z0 |
| P ⇒ G per frame; consistent maps; F2 ⇒ Law; mass conserved | IC1–IC4 |
| the sweep covers exactly the class | IC5, merge coverage check |
| witnesses replay independently | W1 |
| a positive is reproduced independently | protocol 3 |
| every control can fail | mutant campaign |
| arithmetic is exact; no file read; no author engine | ST |
| the result is deterministic | normal and `-O` output equal per shard and merged |

## Scope

- No claim at actual L, where there are eight ports and two-port simultaneous
  arrival (v7).
- Read records of at most k stream items only. Larger records are outside the
  class.
- One background prior. A positive moves the burden onto it.
- One scaled port. The eight actual ports are not modelled.
- Freshness is not tested beyond T_h, or against later reads outside 𝓛_R. #929
  names leaks beyond the declared horizon as a hazard.
- The G parts cover seventeen frames, unless the frame-uniform certificate
  applies.
- Failures in G are relative to the seed declaration.
- No access rule is adopted; a passive flag is not an observer read.
- No native storage, gate, reset or compilation is implied. The carrier stays
  in v6's supplied logical storage.
- No A1/A2 statement. A positive would be a conditional F2 ingredient, not an
  equivalence step (`PROGRAMME.md:40`, `:634`).
- A negative excludes C_avg(4, 16, k) in the scaled control under π_bg. It
  does not exclude OI, nor native predicates with gates, prepared sources or
  larger reads.

Results to preserve: v8's pointwise negative (K1), v6's logical law (x2, K2)
and v7's geometry (x6).

## Inputs, pinned (SHA-256)

At #912 `2af1d5d5b5fff4375e9fe9460f892c680ae99f0c`, under
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/`.
Every v8, v6 and v7 file listed is identical at
`fc452ea825b986a3babab5d110626e0019c39847`.

- `REPORT.md` (the contract and its G9 condition):
  fe7033502df5b041d48e941f166da7e5092ec72f289d4a6059b782c689a5b350
- `CURRENT-HANDOFF.md` (at `2af1d5d5`):
  a7187ed4860723f361d24961da2858403f29306f0acccf8018b8552a19b41817
- `native_predicate_v8/`:
  - `PLAN.md`
    86d3970efd650a23ba37543fca730cbcff3d746a3c868889d976f76629bd104a
  - `REPORT.md`
    906a9007d1116098f6ca1f2084c2b645f62955217da4e5be27b371296efe410d
  - `checks.py`
    2c3ccccc72df5d7245079d4271e2a9550640b5fb793af1ba3a816c7397688589
  - `result.json`
    70f7848aa5f1f3deb9ccfa018580a84995c25cb5dcae56db5682dbbaf94058f0
  - `PROVENANCE.json`
    c64b5c735b79e5589f16c58463f78e958e3d3f89774a8053b212c927f51cabcc
  - `mutants/run_mutants.py`
    56e41430562d012d6a351a4c1f521b4852038781ae760c01334745791ca78432
  - `mutants/mutants.out`
    51cb929fed1eb7048678801f780ce1656f97475d4076b5ba33ac49e904db87a6
- `composition_flag_v6/`:
  - `PLAN.md`
    fe75a3d50744dbfb566e1119358993c0bc5141a0f0a19166405b178c4e93fa4e
  - `REPORT.md`
    425af236158aa9adf2949204fda4e5fc176f020f35264fb445847bbf3b1274ba
  - `checks.py`
    fa37bef360b5c2ecca4d132265628c7771b43c058fe3a13115d772ef16974f0b
- `delayed_history_v7/`:
  - `PLAN.md`
    3c60f7efa5b38ee6a4b9cf20e205348da4cdd405f770a81883e7007fc3ad1b58
  - `REPORT.md`
    d51685c2274313d88be7b857bc6df03f5bb74b5644449aa081469cb00053cac9
  - `checks.py`
    3754fcd40a37153bf2c26312afe77337ed991d474f6694367a73a25c5aefa5b3
  - `result.json`
    ccc3b9722282cb2381513fb20fa310b2b7257386e96912b4bc580c65595cf46e

On `main` at `52e2db4058539e510d5e948d1cc94954dc64c0f0`, under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:
- `transport_audit_v1/REPORT.md` (K6):
  d9a1e3ef8c063bafe3e1c16573a0feb3ec07ed6a7b239103db75444de9c67670
- `transport_audit_v1/checks.py`:
  a9e95272604157a35d128831dfa7b9e0e48ac53e4f9a16cd633a3037a0c5aec2
- `history_v11/REPORT.md`:
  413c9595a6def923ba62e1c0d34c12c0516997fe1c928e5438abaf6a990fdb81
- `history_v11/review/REPORT.md`:
  dba6f7bde248b5c5b3a0472c7455afd828a61d265ee93577d4355fc8e246ea59
- `native_x_v12/REPORT.md` (Native A):
  18678f906f6492b13d27152db3f3595361df0414cc4fa8de2f48229fac4e2808
- `verification/programmes/oi-qm/PROGRAMME.md`:
  1e15ffb39f7910bd85fab1c8c538ec2ab4f888ef878724a334814dfc54121718

Also pinned:
- PE-01 `PLAN.md` at `47a1f19bbfe1aca2ddd925fe934f7d30b3d1f13d`
  (`research/oi-pseudoentropy-20261025`):
  bf7b0cb9387eb69b8ffc925c0ed09a789911c670da2a0144408f3d473dd5e091
- Issue #929 body as read (`ISSUE-929.md`):
  74a05798e0689d42e6f58f414ab2df11ec63786b7effb7537d463b0046afef7c

The checker reads no repository file. The constants it uses from these sources
are written into it and listed in `PROVENANCE.json`.

## Resources

Standard library only, with exact integers and fractions and explicit
exceptions.

**Locally before any push** (§A.40):
- K1a (about one minute);
- the GB, L1c, L2c, L3c, K6 and Z0 self-tests on the reduced instances;
- ST;
- compilation.

**In CI**, through structured shard files (§A.44):
- the sweep, 5,163,225 records with F checks in A and on seventeen frames;
- IM1 and IM2;
- the mutant campaign.

A dry-run mode prints the shard plan and record counts without evaluating any
law. If the projected cost exceeds **8 runner-hours** (O8), the run stops and
reports the partial state.

Adding the workflow, and every dispatch, needs owner approval (§A.43 item 4).
No F/E designation, merge or special launch follows.

## Dependencies

- **Base.** The plan is committed on a base that contains `fc452ea8`, since K1a
  needs v8's files (O6). Under §A.42 neither this plan nor any result citing
  `fc452ea8` lands on `main` before v8's files are reachable from `main`.
- **G9 contract:** #912 `REPORT.md:57-69`.
- **#923 (OI-PE-1).** A read-only compatibility check finds that PE-01 uses no
  background prior of this kind. Its priors are:
  - a uniform initial law on its own generator state (PE-01 `PLAN.md:56`);
  - a uniform tape (`:45`);
  - uniform polynomial families (`:70`).

  Its observer memory starts at a fixed value. π_bg is compatible with these.
  Coordination itself is the owner's call (O7).
- **Native A** (#910), the transport audit and `history_v11` are on `main`.

## Relation to PE-01's open question

PE-01's open question on charged lookup tables and description complexity
does not bear on this plan. The predicate A′ here is unrestricted and
uncharged, and that question belongs to PE-02.

## Open items for the owner (O1–O9)

Each is written into the plan at the review's recommended value.

- **O1. k = 2**, counted in stream items: 3,225 singles and 5,160,000 pairs.
  - *Alternative:* k = 1.
  - k = 3 needs a structural restriction.
- **O2. Class elements:** v8's backward-closed stream items, with F2 forward
  only.
  - *Alternative:* bare site-times (3,225 and 5,198,700). In that case F2 must
    not require A′ unchanged on samples before the record.
- **O3. All-frame freshness.** POS_A requires the frame-uniform certificate,
  which has two parts:
  - (a) every variable averaged in R's G computation is removed by L3, which
    holds for every fixed value of all other variables, the frame included;
  - (b) a written argument of the Native A kind (an all-C0 statement) shows
    that the J-law of every retained class holds on every frame, checked on
    the seventeen frames.

  Without the certificate, the result prints POS_A_SAMPLED_FRAMES.
  - *Alternative:* none that reports POS_A unqualified on seventeen frames.
- **O4. Later reads 𝓛_R** = the port, each item's own continuation, and any at
  most k later in-region segments through T_h.
  - *Alternative:* the port and each item's own continuation only. The verdict
    text must then record that F2 is near-vacuous under A.
- **O5. K4:** bias 1/4 on c alone. A native result's prior dependence is
  recorded as "not computed" where it is not computable.
  - *Alternative:* bias on every non-source bit. It has no feasible exact
    method here.
- **O6. Location and base:** `native_predicate_avg_v9/` beside v8, on #912's
  guiding draft, or on a successor based on a commit that contains `fc452ea8`.
- **O7. #923 coordination:** the owner confirms or cross-links before freeze.
- **O8. Frames and budget:** v8's sixteen families plus zero, and 8
  runner-hours.
  - *Option:* sixteen further old-success frames chosen by v8's rule, continuing
    its seed scan after v8's last chosen seed. They are not adopted unless the
    owner chooses them.
- **O9. T_h = 46 and S_max = 27 bits.**
  - *Alternative for T_h:* v7's form, slice 11.
