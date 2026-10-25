# Native read v15: one native tick from q10 into the declared whole-V read

Research only, 25 October 2026. Base #910 is
`bef79f6f3daec0b734a7d9c6a9423ed634852818`. This plan is committed before
the checker is written. No access rule, preparation change or physical
premise is adopted by it.

Before writing this plan the author read the handoff, the v12-v14 reports
and the v13 geometry code, and estimated by hand that one of the key cells
defined below lies outside the declared ready regions. The checks below
replace that estimate; the decision rule does not depend on it.

## Inputs (all at the base commit, pinned by SHA-256)

| File | Role | SHA-256 |
| --- | --- | --- |
| `native_route_v13/result.json` | 4096-row q10 table at L+1 | `762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02` |
| `native_route_v13/review/result.json` | separate-engine table digest | `73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e4` |
| `native_decode_v14/result.json` | fewest-seed q10.A=s law and counts | `3172e7d013c09cdcdf638a7ace68e0eff98bb3cd0411e8666b76a8226ad59034` |
| `branch_v10/local-controller/symmetric-result.json` | old q9 table at L | `d8e7c1f5841192165beefb3fe35b069cc14cc93f2faa2bd68619aa7748b3db2f` |
| `parallel_v3/history_control/SOURCE-GEOMETRY.json` | 1479 inherited sources | `2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d` |

The q10 table string must hash to
`b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc`.
No earlier engine is imported; all inputs are read as data.

## Which reads are permitted

No access rule is adopted on this branch (CURRENT-HANDOFF.md:6-7). The
reads that the retained candidate contracts declare, and which this plan
uses as the permitted public record through L+2, are:

1. the full raw triples of the eight old public ports at every tick
   (history_v9/REPORT.md, "Fixed dynamics, ports and bank"; herald port
   c_G=(48L,0,0) from herald_v10), extended through L+2 by Native A
   (native_x_v12/REPORT.md section 4);
2. the old whole-q9 terminal record at L, (0,s,r_old) on accepted rows
   (shared_v12/INTERFACE-CONTRACT.md:38-40; native_x_v12 section 4);
3. Native A's single whole-V read, V=U_(L+2)(q9), the whole triple
   (CURRENT-HANDOFF.md:30; native_x_v12 section 4, which does not
   authorize continuous q9 access or any later read).

q10 at any tick, and every previous-slice neighbor of q9, are private.
Read 3 is the only declared read that q10 at L+1 reaches in one native
tick: q10 is a neighbor of q9, and V is the next q9 value.

This plan applies read 3 to the native_route_v13 source geometry, which is
not Native A: it pins F10, has no F9 resource and keeps its own readiness
extension B_(L+1)(q10). The combination is a test case, not an adopted
contract.

## Question and candidate stage

Candidate stage: the unchanged native update at q9 at L+2,

    V = p XOR H(Sigma),  Sigma = XOR of the six q9 neighbors at L+1,
    p = U_L(q9),  H(A,B,D) = (B,D,A XOR BD),

with q10 at L+1 taken from the retained table. No new source, readiness,
gate or read is introduced.

Question: does the permitted whole-V read deliver the content of q10.A,
and what does the complete permitted public record through L+2 then
reveal, under the native_route_v13 source contract, whose initial variables
outside its ready regions, sources and banks form a complement of
unrestricted law (native_v11/REPORT.md, "outside-ready qualification";
history_v9 joint chronological proof)?

## Key cells

A key for neighbor w=q9+e of q9 is a current-slice initial cell that
reaches w by L+1 and reaches neither q9 by L nor any other neighbor of q9
by L+1. Lemma (to be checked by brute force for small n in control K2):
the only such cells are the six axial cells c_e = q9 + (L+2)e. Proof
sketch: such a cell c is at distance L+1 from w and at least L+1 from q9,
so |c-q9|=L+2; if c-q9 had a nonzero component along e' other than e, c
would be at distance L+1 from q9+e'.

For each e other than +z (the q10 direction), classify c_e at actual scale
with exact integers as

- PINNED: inside one of the current ready balls of the native_route_v13
  contract (the 24 inherited balls and B_(L+1)(q10)), or equal to a
  declared source position (the 1479 inherited sources, O, W, E, N, the
  upper Q/C/G/J/K cluster, the three pure-B selector sources, the F10 pin,
  the z source);
- BANK: on a reserved bank ray of one of the eight ports at an index t with
  deadline < t <= 2L;
- FREE: otherwise, i.e. a complement variable.

A FREE key must also be at distance greater than L+2 from every public
port and from c_Z=(-48L,0,0), so that no other permitted record through
L+2 depends on it.

## Native statement under test

For a FREE key c_e and every fixed value of all other initial variables,
the neighbor q9+e at L+1 is a permutation of the key triple (unique axial
first arrival in arbitrary background, native_v11/REPORT.md, "Native proof
in arbitrary background"), and p, q10 and the other four neighbors are
unchanged (finite speed). Hence V is a permutation of the key triple.
Controls K3 and K4 check this on complete small native worlds.

## Preregistered decision rule

1. If any control below fails, print VOID with the failing label and exit
   with status 2. No verdict text is written.
2. If at least one non-q10 key is FREE and passes the receiver check:
   **NEGATIVE_FOR_CONSTRUCTION**. The generated verdict states, for the FREE
   keys found: (i) no nonconstant fixed readout of the whole V equals s for
   every complement value; (ii) under any complement law in which a FREE key
   is uniform conditional on all other initial variables, V is uniform and
   independent of every other initial variable and of every other permitted
   record through L+2, so the read carries no information about q10.A;
   (iii) delivery through this read would need that key known, which means
   pinning the key cell (a preparation change) or reading q9+e at L+1 (an
   access change); this plan adopts neither and stops there.
3. If no non-q10 key is FREE: **NOT_DECIDED_BY_THIS_PLAN**. Delivery and
   leakage then depend on the full native V kernel and its joint law with
   the public ports, which this plan does not compute.

HOLDS_WITHIN_SCOPE is not reachable under this plan: it would require the
V kernel of outcome 3 and a joint public-record audit, both outside it. A
BANK key is not FREE for this rule; it is reported.

## Controls and countercontrols (each shown able to fail)

- **K1 input pins.** Five file hashes; the recomputed table digest equals
  the recorded one and the review's; 4096 table rows, 32768 q9 rows.
- **K2 key lemma.** For n=2..7, brute force over all cells within distance
  n+2 of q9 in a small lattice: the set of keys (distance n to exactly one
  non-q9 neighbor at time n, all others and q9 at time n-1 unreached) is
  exactly the six axial cells. Countercontrol: some non-axial cell at
  distance n+1 reaches two or more neighbors; it must be found.
- **K3 native key permutation.** Complete second-order native rule, dirty
  deterministic backgrounds in both initial slices, n=1..4, three seeds,
  every one of the six axial keys. Two evaluators (bit-parallel lanes and
  scalar recursion) must agree on V, q9 at n-1 and all neighbors at n. V
  takes all 8 values over the key, and q9 at n-1 and the five other
  neighbors do not change. Countercontrol: the off-axis cell (-n,0,-1)
  changes at least two neighbors; this must be observed.
- **K4 delivery detector.** An operand triple at the q10 key (0,0,n+1) and
  the m key (-(n+1),0,0). With the m key held fixed, V separates the
  operands (positive: total variation 1 between two operand values); with
  the m key uniform, the V laws for all operands are equal (null: total
  variation 0). Both must hold in every small world.
- **K5 geometry anchors.** The classifier must return PINNED for the q10
  axial cell (inside B_(L+1)(q10)), for E, N and the F10 position; FREE for
  F8=(-(L+1),S,76), which native_seed_v12 keeps outside the ready cone;
  BANK for (0,-2,0) on port 0's ray.
- **K6 preserved results.** E and N avoid every inherited ready ball (as
  native_route_v13 checks); old q9 at L equals (0,s,s XOR a XOR b) on all
  accepted rows (native_seed_v12); the v14 fewest-seed law
  [1,5,1,4,1,5] gives q10.A=s on all 48 accepted rows and v14 records 1456
  q10.A laws; the radius-(L+2) q9 shell meets 8 reserved bank coordinates,
  4 at distance exactly L+2 in the active component (native_x_v12); the
  Native A f9 cell (-(L+2),S,77) has public-port slack 79 over L
  (native_x_v12).

Mutants of the checker, kept with their outputs, must make each of K1-K6
fail on its own label.

## Invariant to checkpoint table (section A.41)

| Invariant asserted | Checkpoint |
| --- | --- |
| Inputs are the retained bytes | K1 |
| Only axial cells are private keys | K2 (brute force); written proof above |
| A FREE key permutes V and nothing else permitted | K3; receiver check in stage G |
| The detector can return both outcomes | K4 |
| The classifier agrees with declared pins, frees and banks | K5 |
| Earlier results are reproduced, not contradicted | K6 |
| Output is deterministic | result.json byte-identical under -I -B and -I -B -O |

## Diagnostics outside the rule

- Read algebra: given p, Sigma -> V is a bijection with V.A=Sigma.B,
  V.B=p.B XOR Sigma.D, V.D=p.D XOR Sigma.A XOR Sigma.B*Sigma.D. So the read
  exposes the whole triple q10 XOR (other neighbors), never q10.A alone; on
  accepted rows with q10.A=s, q10.A XOR p.D = a XOR b.
- For the fewest-seed law, the number of distinct whole q10 codes for each
  s across the 24 contexts.
- The bank coordinates within distance L+2 of q9, their port indices, and
  which q9 neighbors each reaches at L+1: the coordinates a readiness
  extension pinning the q9 shell could not pin.

## What this would and would not establish

A NEGATIVE outcome would establish, for this one-tick stage, this source
geometry and this declared read only, that the read is a one-time-pad
ciphertext keyed by a complement cell, so that the transport of s into
q10.A is not made accessible by it. It would not exclude multi-tick
stages, other reads, other layouts, a readiness extension or a different
complement law, Native A's own geometry, or OI generally, and it would not
establish privacy under a complement law in which the key is not uniform.
No HOLDS outcome is possible here. A1 and A2 targets are not addressed.

## Execution

Standard library, exact integers, `python3 -I -B checks.py` and
`python3 -I -B -O checks.py` byte-identical to result.json. No dispatch,
push, merge, F/E designation or #885 write.
