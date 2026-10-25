# Passive native readout as the acceptance predicate

25 October 2026. Author computation under #912. The plan was committed before
computation at `631bec0ca55eacbf6a7cf7e72d72c673dfe430da`, whose parent is
#912 at `afc7bced6720ee6b3ce27207423d1f56f5851779`.

## Result and scope

Verdict, generated from the measured values: `NEGATIVE_FOR_CONSTRUCTION`.

The construction class is C(4, 16). The public record is v6's candidate contract
(old whole-q9 record, single whole-V record, the eight old ports), with v6's
pointer replaced by the whole raw triples of an arbitrary set R of native
site-times within Manhattan distance 4 of q9, read through L+17. No gate, pad or
added source is used. The flag may be any predicate of that record; it need not
be v6's A.

In each of the sixteen scaled dirty old-success families, no such R gives
(V, w_R) the complete v6 law, conditional on the complement C0. This holds for
every R, stream-closed or not, and family by family as well as in common. The
measured obstruction is sharper than the absence of a common rule:

- For every family and every value of V, the number of two-block partitions of
  the 64 worlds with that V that carry the target law is zero, among all 3,225
  read site-times.
- Per family, 2,224 to 2,226 site-times are constant given C0. G has not reached
  them yet, or they are at the opposite time parity to G's arrival. Of the
  roughly 1,000 G-dependent site-times, 921 to 925 split some V value into all
  eight triple values. Only 2 to 6 split every V value into at most two blocks,
  and none of those splits has the target law for any V value.
- Single site-times, reported only: none has a (V, w) class with exactly the
  accepted law, so a heralded relaxation that leaves the rejected law free also
  fails at that level. And v6's A is a function of (V, w) at none of them.
- The zero-background diagnostic gives the same result: no admissible R, and two
  nontrivial cells with at most two blocks, neither with the target law.

So passive native readout fails here because of what the cells carry, not
because operands are missing. Native dynamics does deliver the operands: q8, q10
and m at L+1 and V at L+2 are among the read cells, and Native A's triangle and
seven-site inverse hold in every family. But once G arrives, a native cell
almost always carries more than one bit of pool information given V. The few
cells that carry one bit do not carry the 5:4:1 accepted law.

The scope is the following, and no more:
- class C(4, 16) only;
- the scaled control, with n = 6 in place of L and uniformly random dirty
  backgrounds;
- the law conditional on C0, the form in which v6 and v7 state it.

It does not exclude any of the following:
- native predicates that use added fresh pads, prepared sources or a different
  source family;
- native gates or compilation;
- larger regions or later reads, up to the L+73 bound below;
- a law that holds only after averaging over private backgrounds under a
  specified prior;
- a predicate at actual L in its actual background.

It establishes no native storage of the outgoing carrier, which stays v6's
supplied logical storage. It adopts no observer-access rule, clock or premise,
and makes no A1/A2 statement.

## Why this sub-question

Two candidates were considered: (a) native storage of the v6 carrier through
L+2..L+91, and (b) a cheaper native predicate before tail arrival. (a) is not
decisive as a computation. Left at fixed sites, the carrier fails after one
native tick (v6's delay control). Re-encoded by the exact native inverse, the
decoded carrier is the same random variable as the frozen carrier, so its joint
law with the public record equals v7's by identity, and the open question
becomes whether the decoder is available, which is a compilation question. (b)
is upstream: if native dynamics supplied an admissible flag before the tail
arrives, the 89-tick serial circuit, and its overlap with the L+77 arrival,
would not be needed. Its cheapest form is passive readout, with no gates and no
added resources. This test settles that form for the class above.

## Delayed history

If no tail-bank triple reaches any site-time of R, then w_R is a function of
(C0, G). v7's written argument applies with Φ extended by w_R:

    Pr(N_L, N_tail, w_R, V, J | C0)
      = [N_L = N_L(C0)] · 2^(−24(H−L)) · Pr(w_R, V, J | C0),   L < H ≤ 2L.

So the complete delayed-history law for a tail-free read set is the law of
(w_R, V, J) given C0. That law is what the scaled control computes. The
factorization is inherited (v7, `history_v11`, Native A) and is not recomputed
here.

## Actual-L geometry (exact integers)

- The first tail arrival over the 129 region offsets is between L+74 and L+82.
  The last read is at L+17, so every read is tail-free (x7). Native reads in
  this region could continue to L+73 before the tail can reach them. The scaled
  control covers only L−7..L+17 of that window.
- G first reaches the region at L−2. For every one of the 129 offsets, the
  scaled G arrival equals the actual arrival minus (L−n) (x7).
- The carrier first-tail-arrival table reproduces v7's (x6): q8, m, q9+x and
  q9+y at L+77; q9 at L+78; q10 and q9−y at L+79.

## Exact search over every read set

Fix a value v of V; there are 64 worlds with V = v. Each class of an admissible
record must carry counts proportional to the accepted target, which sums to 20,
or to the rejected target, which sums to 44. Since 20a + 44b = 64 only for
a = b = 1, the join of the partitions of R's cells must have exactly two blocks,
with exactly the target counts. Every cell of an admissible R therefore has at
most two blocks given each v, and all its nontrivial two-block partitions are
that one. The checker decides existence exactly over all R from these per-v
partitions: per family, then common to all sixteen, then stream-closed. The
search never reached its caps (10^5 partition choices per family, 24 common
candidates).

The argument is checked independently in x5: on 2,046 subsets of a pool of
planted and native cells in two families, a brute-force join with a
proportionality test, which does not use the two-block argument, agrees subset
by subset; 28 of the subsets pass.

## Controls (all required, all green)

| control | result |
| --- | --- |
| x1 | An independent scalar evaluator (dict-based, explicit Boolean H) agrees on all 3,225 read site-times, on three worlds per family. |
| x2 | In every family the pool (q8, q10, m) at n+1 is a bijection of G on 512 values, the seven-site inverse recovers old q9 in every world, the phase sign equals old q9.B, and V is uniform. |
| x3 | A planted (0, A, 0), passed through the full search, is admissible in every family, common to all, and passes the direct check. |
| x4 | Planted negatives are rejected by both statistics: (A, Y, 0), A with n permuted to (5, 4, 0, 1), and (0, Z, 0). Planted (0, A ⊕ V.B, 0) and (1, A, 1) are accepted. |
| x5 | The reduction equals brute force on 2,046 subsets. |
| x6 | The geometry reproduces v7's carrier table. |
| x7 | Every read is tail-free at actual L; scaled G arrival maps to actual arrival; every sample before G's first arrival is constant in every family. |

## Mutants

`mutants/run_mutants.py` applies one textual mutation at a time and runs the
mutant checker; `mutants/mutants.out` is its output. Each control mutant must
exit 2 with verdict `VOID` naming its target. The injection mutant must turn the
verdict to `HOLDS_WITHIN_SCOPE`.

| mutant | change | outcome |
| --- | --- | --- |
| m1 | scalar H uses OR | VOID, x1 |
| m2 | inverse offset by one | VOID, x2 |
| m3 | law statistic rejects everything | VOID, x3 |
| m4a | direct proportionality test accepts everything | VOID, x4 |
| m4b | law statistic accepts any two-block split | VOID, at the family search cap, before x4 |
| m5 | reduction allows an uncovered V value | VOID, x5 |
| m6 | tail window shifted by one tick | VOID, x6 |
| m7a | actual F9 moved one site | VOID, x7 (geometry) |
| m7b | early-constancy check includes the arrival slice | VOID, x7 (early samples) |
| m8 | bit-sliced native rule uses OR | VOID, x2 |
| m9 | (0, A, 0) injected into the native cell (4, 0, 0) at its first G arrival, slice 12 | `HOLDS_WITHIN_SCOPE`, with the stream of (4, 0, 0) through slice 13 |

m9 shows that the native search itself, and not only the planted pool, finds an
admissible cell when one exists. The stream it returns runs through slice 13
because, by time parity, (4, 0, 0) does not depend on G at slice 13.

## Reported only

Each family row in `result.json` gives:
- the block-count histogram;
- the two-block cells, with their position, slice, G-arrival slice and how many
  V values they split;
- the heralded and A-function counts;
- a SHA-256 of the native table.

The two-block cells are mostly (−2, 0, 0) at slice 6 and (2, 0, 0) at slice 10.
The list of them was added after the plan.

## Points for review

- The negative is for the C0-conditional law. A mixture over private backgrounds
  is not tested.
- The backgrounds are uniform random. The actual-L background near q9 is
  whatever the inherited preparation gives at L. The scaled G path crosses n = 6
  dirty ticks, not L.
- The read set is limited to radius 4 and slices up to n+17. Native reads to
  L+73 are tail-free and untested.
- Fresh initially-fair pads, as in v6's pointer or Native A's f9, would change
  the class sizes and are the next branch; they are not tested here.

## Replay

    D=<repository root>/verification/programmes/oi-qm/reconstruction/composition-access-20261024/native_predicate_v8
    python3 -I -B "$D/checks.py" > out.json && cmp out.json "$D/result.json"
    python3 -I -B -O "$D/checks.py" > out.json && cmp out.json "$D/result.json"
    mkdir mut && python3 -I -B "$D/mutants/run_mutants.py" "$D/checks.py" mut > mutants.out \
      && cmp mutants.out "$D/mutants/mutants.out"

Run from an empty working directory. Each checker run takes about 75 seconds,
and the mutant run about five minutes. If a required control fails, the checker
prints `VOID` and exits with status 2. The checker uses the standard library
only, imports no author engine and reads no repository file. `SHA256SUMS` lists
`PLAN.md`, `REPORT.md`, `checks.py`, `result.json`, `PROVENANCE.json`,
`mutants/run_mutants.py` and `mutants/mutants.out`.
