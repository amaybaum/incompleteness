# Direct-Y reset avenue: a standalone native candidate with an explicit history tag

24 October 2026. Repository read-only. This avenue writes research files only.
No premise or acceptance-rule change is adopted. This is an author result for
independent review, not certification of a reusable X→Y sequence.

## Result and exact boundary

There is a finite **standalone native apparatus** that accepts the three raw
incoming codes `Q=(y,y,1 XOR xy)`, with Q localized once at the initial origin,
and writes a heralded Y-calibrated output at tick 2700. It does not first
normalize Q. Every source other than Q is an affine function of initially
specified apparatus seeds, independent of Q. The old input's previous triple
can be arbitrary. The rule is unchanged.

The resulting output contains a deterministic public-history tag `g=xy`.
A single fixed extraction splits it into the desired twelve-state carrier and
g. The **entire tagged joint law** is calculated, not merely terminal sign
marginals. The full cell at a later X or R read reveals only the designated
new sign plus already-public `(x,y)`.

Two boundaries remain material:

1. The construction assumes a clean **initial** input socket. It has not been
   embedded into the actual late q2 phase. Translating the time origin and
   silently blanking its neighbourhood is not allowed.
2. At y=1, the two full raw-output distributions for earlier x=0 and x=1 have
   disjoint supports (TV=1). Thus the candidate fails a strict common,
   history-independent raw-carrier encoding. The tagged law proves an exact
   alternative interface, not acceptance under that unchanged stricter rule.
   No tagged-encoding relaxation is adopted. A physical separation of the tag,
   or a reusable native interface proved insensitive to it, remains necessary.

## 1. A native mixer using the actual A operand

Write the unchanged local permutation as

    H(A,B,D)=(B,D,A XOR BD),
    H^-1(A,B,D)=(D XOR AB,A,B),     H^12=id.

Let L be a positive multiple of 12. At initial time zero place arbitrary Q at
0 and a pure-A seed `(a,0,0)` at `2L e_x`. Prepare the receiver's current
radius-L and previous radius-(L-1) dependency balls, keeping those sources.
The receiver is `L e_x`. Each source has a unique axial first-arrival path,
and their separation is 2L, so their waves cannot interact before the final
collision. The old local term and all unarrived neighbour terms vanish there.
Consequently the complete receiver triple is

    H(H^(L-1)(Q) XOR H^(L-1)(a,0,0))
      = H(H^-1(Q) XOR (0,a,0))
      = M_a(Q)=(A XOR a, B, D XOR aB).

M_a is a total involution on all eight Q values, for either a. This formula
uses the actual incoming A, not the incidental equality A=B on native inputs.
Replacing A by p while keeping B,D fixed changes the output A to p XOR a.

Use opposite receivers `+L e_x` and `-L e_x`, with independent seed sources
at `+2L e_x` and `-2L e_x`. They receive M_u(Q), M_v(Q). Add a third receiver
at `+L e_y`; it receives H^L(Q)=Q. Q is placed only once initially. Fanout is
native wave propagation, not distributed copies of the unknown input.
All three receiver prefixes are zero before L. The old previous-slice triple
at the origin lies outside each radius-(L-1) dependency ball.

For the accepted Q=(y,y,1 XOR xy), the three terminal cells are

    X cell = (y XOR u, y, 1 XOR xy XOR uy),
    Y cell = (y, y, 1 XOR xy),
    R cell = (y XOR v, y, 1 XOR xy XOR vy).

A fourth private cell provides `(0,0,z)`, with z fresh and fair. The designated
Y record is the actual A field of the Y cell, and its complete raw triple is
determined by the already-public x and the newly recorded y.

## 2. Native herald and simultaneous geometry

Use six new initially independent fair bits: u, v, three bits for K in 0..7,
and z. They are independent of Q and the earlier public history. Required
source copies of these apparatus bits are affine, and are prepared initially.
The herald accepts

| u,v | Accepted K | Count |
|---|---|---:|
| 0,0 | 0..4 | 5 |
| 1,0 | 0..2 | 3 |
| 1,1 | 0..1 | 2 |
| 0,1 | none | 0 |

This is the supplied Y calibration, not a new derivation of its probabilities.
There are ten accepted configurations out of 32, giving q=5/16. Conditional
on success, plane weights are 5:3:2 and z remains fair.

The inherited fixed-rule Boolean compiler is copied byte-for-byte. The new
predicate is compiled into a register word of length 2684 ending in the A
field. Pad it by identity words to length 2698, append one zero-control H
step, and then apply the compiler's final H. This synchronizes the complete
native herald at L=2700, with raw output `(0,G,0)`. There are 7832 nonzero
affine source entries. Both the program and full source list are retained in
herald.json. The checker recomputes the actual three source-wing recurrences
and all 2700 axis steps, rather than only executing the register word.

Use the following five receiver centres, in units of L:

| Receiver | Centre/L | Initial signal sources |
|---|---|---|
| X | (1,0,0) | Q at0; pure-A u at(2,0,0)L |
| R | (-1,0,0) | Q at0; pure-A v at(-2,0,0)L |
| Y | (0,1,0) | Q at0 |
| G | (12,0,0) | Compiler sources translated by(12L,0,0) |
| Z | (-12,0,0) | Pure-D z at(-12L,-L,0) |

Prepare the union of the five current radius-L balls and previous
radius-(L-1) balls at initial time. Preserve Q and every listed source; all
other entries of that union are zero. The checker examines every source
against every receiver: intended sources are exactly at distance L and all
foreign sources are farther away. Thus shared readiness pins are compatible.
Q is not pinned to any known value and is never copied into the apparatus
prior. The previous unknown at0 is outside every previous ready ball.
A torus side `64L+1` suffices to avoid wraparound in these cones.

The remote herald and Z programmes are causally separate from the three local
receivers through the deadline. The pure-D z source arrives unchanged because
L is divisible by12. Herald and Y prefixes are blank, so the declared public
record contains no early seed disclosure in this standalone construction.
Nothing here proves preservation of the old apparatus's frontier bank when
embedding the construction into its actual late phase. No new preparation,
clock, shutter, or access-closure mechanism is supplied.

## 3. Entire tagged carrier law

Let the decoded carrier be j=(X,Y,R,Z). Define E_(x,y)(j) to be the four raw
cells above, with u=y XOR X and v=y XOR R. This is an injective raw embedding
for each fixed public history (x,y). It is not independent of x.

There is also a fixed extraction, not a separately chosen decoder per history:
read j from the A fields of the X,Y,R cells and the D field of the Z cell,
and extract the tag from either mixed cell `(a,b,d)` by

    g = d XOR 1 XOR ab XOR b.

On all accepted inputs this equals xy. The Y cell independently gives
`g=1 XOR Ycell.D`; the two copies are checked for consistency.

For every allowed point input Q and fixed compatible history (x,y),

    Pr(success, raw=E_(x,y)(j) | x,y)
        = (5/16) mu_(Y,(-1)^y)(j),
    Pr(failure, no offered carrier | x,y) = 11/16.

The public record retains y and the whole herald triple on both branches.
The dynamics still runs on failure, but a carrier is not offered on that
branch under the same supplied failure-access convention as the predecessor.
Failed runs are not discarded or reassigned a successful carrier.

For a terminal X read let r=y XOR u. The entire X cell is

    (r, y, 1 XOR xy XOR (r XOR y)y),

a function only of public (x,y) and the designated new sign r. It reveals no
additional v, K, or z information. The corresponding statement holds for R.
This verifies informational redundancy of the tag at those reads. It does not
prove that subsequent native dynamics ignores the tag or that an arbitrary
observer access class admits this representation.

A strict same-raw-encoding requirement still fails: at y=1, Ycell.D=1 XOR x,
so the full raw distributions for x=0 and1 have disjoint supports and TV1.
Even omitting the copied Y cell does not repair it: each mixed cell exposes
g by the fixed formula above. This distinction is retained explicitly rather
than counting the tagged law as a completed reusable instrument.

## 4. Sequential kernel test and controls

Compose the existing X kernel (weights5:4:1, success5/16) with this candidate
Y kernel using independent preloaded six-bit seed blocks. For each initial x,
all4096 seed pairs are enumerated. The first failure mass is11/16. For each
Y value, the second-failure mass is55/512 and both-success mass25/512. Thus
both success totals25/256, or125/2048 including the older predecessor's5/8
herald. All full raw output probabilities and failure records are checked.
This is composition of exact kernels, not a geometric splice of the native
apparatuses.

The retained controls matter:

- Changing the Y weights to5:2:3 leaves terminal X probabilities unchanged,
  but terminal R separates them by TV1/10 given second success, or1/32
  including second failure. With both5/16 successes the TV is5/512; adding
  the older5/8 predecessor gives25/4096.
- Reusing the old first-reset u as the next u forces Xnew=x, since
  y=x XOR u. This defeats the required fresh, fair post-Y X distribution.
- The strict history-independent raw-output law is explicitly rejected.
- The first-arrival mixer is checked for all eight input triples, so replacing
  only A tests the actual operand rather than the native coincidence A=B.

## 5. Evidence and next obligation

checks.py uses only the standard library, writes nothing, uses no network,
and keeps explicit checks active under Python-O. It checks the general mixer
identity, an independently coded six-neighbour recursion at L12 on256 packed
input/seed/previous-input assignments, blank prefixes, all standalone source
ownership inequalities, the full2700-step native herald recurrence, the full
tagged joint law and8192 sequential seed cases, and the controls above.
Normal/-O outputs match byte for byte. Rebuilding herald.json from the copied
compiler reproduces the frozen bytes.

The next concrete task is to either:

1. embed this standalone gadget into the actual q2 phase while accounting for
   all dirty neighbouring/current/previous fields and original frontier banks;
2. use a native extractor or routing stage that physically separates the
   public tag, then prove the complete combined geometry without a midrun
   clean-socket assumption.

A logically composable or separately cold native gadget cannot simply be
concatenated with another. This avenue has not solved that integration problem.
The shared transport-proof review remains open. Exact-QM reconstruction,
finite-precision OI predictions, probability selection, unrestricted depth and
menu, and composite systems are not settled by this result.

## Replay

From any working directory:

    python3 /path/to/direct_reset/checks.py
    python3 -O /path/to/direct_reset/checks.py

To reconstruct the herald data (writes herald.json in this directory):

    python3 /path/to/direct_reset/derive_herald.py

The copied compiler is self-contained; no baseline path is needed at replay.
