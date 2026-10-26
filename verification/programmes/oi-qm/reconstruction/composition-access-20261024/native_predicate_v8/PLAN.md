# Passive native readout as the acceptance predicate

25 October 2026. Research under #912, starting from
`afc7bced6720ee6b3ce27207423d1f56f5851779`. Fixed before any computation.
No observer access, native storage, compilation, clock or premise is adopted.
#885 is read-only.

## Choice of sub-question

The next gate in `CURRENT-HANDOFF.md` asks for native compilation or a cheaper
native predicate, with operand delivery, a preserved carrier, full pointer
metadata and complete delayed history. Two candidates were considered.

- (a) Native storage of the v6 carrier through L+2..L+91. Left at fixed sites,
  the carrier already fails after one native tick (v6 delay control), long
  before the tail arrives. Re-encoded by the exact native inverse, the decoded
  carrier is the same random variable as the frozen carrier, so its joint law
  with the public record is v7's law by identity; what remains open there is
  the availability of the decoder, which is a compilation question. Neither
  form is a decisive computation.
- (b) A cheaper native predicate before tail arrival. This is upstream of (a):
  if native dynamics supplies the flag, the 89-tick serial circuit, and with
  it the overlap with the L+77 arrival, is not needed. The cheapest conceivable
  native predicate uses no gates and no added resources: the public reads a set
  of native cells, whose values native dynamics has already computed from the
  delivered operands.

This test takes (b), in that cheapest form.

## Fixed question

Construction class C(rho, tau_max). The public record is v6's candidate
contract (old whole-q9 record, single whole-V record, the eight old ports),
with the v6 pointer replaced by the whole raw triples of an arbitrary set R of
native site-times (x, t): q9 + x within Manhattan distance rho of q9, t from
the first slice through L+1+tau_max, with no gate, pad or added source. The
flag is any predicate A' of the public record.

Is there an R, the same in every tested background, whose record has, for
each fixed complement C0, the complete v6 law with some predicate A'? That
is, for every value v of V, every (V = v, w_R) class carries the accepted
v6 carrier law (counts proportional to n(Y XOR s, R XOR s), Z fair) or the
rejected one (proportional to 8 - n). The predicate A' need not equal v6's A.
The law is required conditional on C0, the form in which v6 and v7 state it;
a law that holds only after averaging over private backgrounds under some
prior is not tested.

## Why the delayed history reduces to the cell law

If no tail-bank triple reaches any site-time of R, the record w_R is a
function of (C0, G). v7's written argument then applies unchanged, with
Phi extended by w_R:

    Pr(N_L, N_tail, w_R, V, J | C0)
      = [N_L = N_L(C0)] 2^(-24(H-L)) Pr(w_R, V, J | C0).

So the test is exact integer geometry for tail-freeness at actual L, plus the
law of (w_R, V, J) given C0, which is computed in a scaled native control.

## Inputs, pinned

- `composition_flag_v6/checks.py`
  fa37bef360b5c2ecca4d132265628c7771b43c058fe3a13115d772ef16974f0b and
  `REPORT.md` 425af236158aa9adf2949204fda4e5fc176f020f35264fb445847bbf3b1274ba
  (at afc7bced): phase map, predicate, target counts.
- `delayed_history_v7/checks.py`
  3754fcd40a37153bf2c26312afe77337ed991d474f6694367a73a25c5aefa5b3,
  `result.json` ccc3b9722282cb2381513fb20fa310b2b7257386e96912b4bc580c65595cf46e,
  `REPORT.md` d51685c2274313d88be7b857bc6df03f5bb74b5644449aa081469cb00053cac9
  (at afc7bced): actual-L port, deadline and bank geometry; carrier
  first-tail-arrival table; the factorization argument.
- `native-y-continuation-20261024/native_x_v12/REPORT.md`
  18678f906f6492b13d27152db3f3595361df0414cc4fa8de2f48229fac4e2808 and
  `history_v11/REPORT.md`
  413c9595a6def923ba62e1c0d34c12c0516997fe1c928e5438abaf6a990fdb81
  (at f24a57a7c23cc1818c04265cec7604f8bc2f410d): source triangle and bank.
- `CURRENT-HANDOFF.md`
  89ce8f17492ec7beb5ff808b67b2ab8c50fc657d41b0c5721d8600a2856bf421 (at afc7bced).

The checker reads no repository file; constants it uses from these sources
are written into it and listed in PROVENANCE.json.

## Computation

1. Actual-L exact geometry, with v7's ports, deadlines, axes and signs: for
   each offset x with |x| <= rho, the first time T_free(x) at which a tail
   triple, t in (max(a_i, L), 2L], reaches q9 + x; and the first time G
   reaches q9 + x.
2. Scaled native control, the complete six-neighbour two-slice rule on the
   infinite lattice: q9 at the origin, n = 6 in place of L, G sources at
   (-(n+1),0,-1), (-(n+1),0,1), (-(n+2),0,0), dirty uniform backgrounds in
   both initial slices out to radius rho + n + 1 + tau_max, which covers the
   backward cone of every read site-time, so no zero cell is read. rho = 4,
   tau_max = 16. Scaled time t corresponds to actual time t + L - n.
   Sixteen old-success backgrounds (old q9.A = 0), eight with s = 0 and
   eight with s = 1, the first found by a fixed seed scan; all 512 G values
   in each, bit-sliced.
3. Exact decision over all R. For a fixed v, the 64 worlds with V = v must
   split into classes whose counts are proportional to the two targets;
   since the targets sum to 20 and 44 and 20a + 44b = 64 only for
   a = b = 1, the join of the cells' partitions must have exactly two
   blocks, one carrying exactly the accepted counts. So every cell of an
   admissible R has at most two blocks given each v, its two-block
   partitions coincide with that one, and at least one cell splits each v.
   The checker searches all such R exactly (per family, then common to all
   families, then stream-closed: a read site is read at every earlier slice).
   If the search space exceeds its stated cap (10^5 partition choices per
   family; 24 common candidates), the result is UNDECIDED and the verdict
   VOID.

## Decision rule

HOLDS_WITHIN_SCOPE: some stream-closed R, the same site-times in all sixteen
families, every site-time tail-free at actual L, gives the complete law in
every family, and the induced accept map, as a function of (old q9, V, w_R),
is consistent across families.

NEGATIVE_FOR_CONSTRUCTION: no such R exists, with all required controls
green. The report states the strongest form measured (for example, families
in which no R at all is admissible).

VOID: any required control fails, or the search is UNDECIDED.

## Required controls (each can fail; mutants of the checker must show it)

- x1 An independent scalar sparse evaluator agrees with the bit-sliced one on
  every read site-time, on three worlds per family.
- x2 Native A in the scaled geometry: the pool map is a bijection of G
  (512 values) and the seven-site inverse recovers old q9 in every world.
- x3 Planted positive: a synthetic cell (0, A, 0), A the v6 predicate on the
  native pool, added to the candidate set, must be found admissible in every
  family and common to all.
- x4 Planted negatives must be rejected: (A, Y, 0) (leaks Y); the predicate
  with n permuted to (5, 4, 0, 1) (wrong mask law); (0, Z, 0) (wrong law).
- x5 The reduction agrees, subset by subset, with a direct brute-force check
  (join and proportionality, no two-block argument) on every subset of a pool
  of planted and native cells, in two families; the pool includes
  (0, A XOR V.B, 0), which passes only with per-V conditioning.
- x6 The geometry reproduces v7's first-tail-arrival table at the seven
  carrier sites (q8, m, q9+x, q9+y at L+77; q9 at L+78; q10, q9-y at L+79).
- x7 Every read site-time is tail-free at actual L; samples before G's first
  arrival are constant in every family.

Reported only: the block-count histogram; single site-times whose (V, w)
classes include an exactly accepted-law class (a heralded relaxation that
leaves the rejected law free); single site-times on which v6's A is a
function of (V, w); the same search in one zero background.

A separate mutant script, kept with its output, applies textual mutations to
the checker: each control is disabled or broken in turn and must give VOID
with exit status 2; and one mutant injects (0, A, 0) into a native cell whose
earlier samples are constant, which must turn the verdict to
HOLDS_WITHIN_SCOPE, showing the native search itself can find a positive.

## Invariant -> checkpoint

| invariant asserted | checkpoint |
| --- | --- |
| native fields are the native rule | x1 |
| operands are Native A's pool and V | x2 |
| the search can accept an admissible readout | x3, injection mutant |
| the statistic rejects leaks and wrong laws | x4 |
| the exact reduction is correct | x5 |
| actual-L geometry is v7's | x6 |
| reads are tail-free; early stream is constant | x7 |
| result is deterministic | normal and -O output byte-identical to result.json |

## Scope

A positive result would show, in the scaled control only, that passive native
readout can serve as the flag with v6's complete law; it would not establish
the actual-L background, native storage of the outgoing carrier, a clock or
an access rule. A negative result excludes only class C(4, 16) in the scaled
dirty families, conditional on C0; it does not exclude native predicates with
added fresh pads or prepared sources, larger regions or later times, gates,
mixtures over backgrounds, or an actual-L predicate. Results to preserve:
v6's logical law (x3), Native A's triangle and inverse (x2), v7's geometry
(x6). Standard library only, exact integers, explicit exceptions; normal and
-O output must equal result.json byte for byte. No A1/A2 equivalence,
dispatch, F/E designation or merge follows.
