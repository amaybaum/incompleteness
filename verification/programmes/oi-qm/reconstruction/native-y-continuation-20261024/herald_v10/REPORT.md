# Initial-source Y herald and fair z synchronized at R+9

Research checkpoint based on #910 at
`3f440c59660d7255aa8a727ff8b5de8289004f80`. The construction gives two remote
native outputs at the unchanged local deadline L=R+9: a herald with raw triple
(0,G,0), and an independent fair-z cell with raw triple (0,0,z). All sources
and ready regions are prepared at the original initial time. The 5:3:2
calibration is supplied, not derived from OI.

This closes the remote synchronization subproblem. It does not build the
three simultaneous local post-Y sign outputs or certify a joint reusable
carrier. Those local geometric and interface obligations remain separate.

## Seed law and target predicate

Use five initially independent fair bits a,b,k0,k1,k2, with
K=k0+2k1+4k2, and one additional independent fair bit z. They are independent
of the incoming system and old apparatus variables under the candidate's
supplied preparation. Copies used by the local masks and remote compiler are
correlations of these same seeds, not independently redrawn resources.

The native predicate is G=1 iff K<n(a,b), where

| (a,b) | n(a,b) | Rejected K count |
| --- | ---: | ---: |
| 00 | 5 | 3 |
| 01 | 0 | 8 |
| 10 | 3 | 5 |
| 11 | 2 | 6 |

There are 10 accepted seeds among 32, so success is 5/16 and failure 11/16.
Conditioned on success the plane weights are 5:3:2 and z is fair jointly
with (a,b). Every failure remains in the complete herald record; private
fields continue evolving. A failure does not create an offered carrier.

## Exact schedule without changing P

Keep T=185, P=12*840^185, S=T+P, d=68, R=S+d. Thus

    L=R+9=P+262.

Let W be the first 2,684 affine-controlled H steps in the retained
`parallel_v3/direct_reset/herald.json`. Its source construction and derivation
remain retained in that directory. Starting from the zero register, W writes
(G,0,0) for all 32 assignments of its five seeds. This checker independently
re-evaluates that complete truth table.

The six constant controls, encoded as 4A+2B+D, are

    I6 = (2,3,3,3,3,7).

They compose to identity on all eight register states. Set

    m=(P-2424)/6.

This is a nonnegative integer. Use W followed by m copies of I6, followed
by one zero-control H step. That program has length L-1; the native compiler's
terminal H is the Lth step. The exact accounting is

    2684 + 6m + 2 = L.

The two final H applications send (G,0,0) first to (0,0,G), then to (0,G,0).
The complete output therefore has the desired phase at R+9. No value of P
is changed, and no 2,700-layer period is asserted. The long operation is a
symbolically specified finite first-arrival program, not transport of the
old small apparatus using an unsupported strip-period extrapolation.

## Explicit original-time herald sources

The new herald receiver is c_G=(48L,0,0). Its source cone is oriented outward
along +x. Let g_t be the affine control triple of the above program for
0<=t<L-1, and let g_(L-1)=0 be the terminal native input. Affine masks encode
constant bit 0 and seed coefficients in bits 1 through 5.

For each wing w in {0,1,2}, define the affine bit profile

    B_w(t) = component_(w-t mod 3)(g_t).

For every integer 0<=q<L, form the affine source bit

    A_w(q) = XOR_(e subset q) B_w(e),

where e subset q means every binary one of e is also a one of q. Place it
in initial field w at these coordinates, omitting zero masks:

    w=0: c_G + (L-1-q, q+1, 0),
    w=1: c_G + (L-1-q,-q-1, 0),
    w=2: c_G + (L-1-q, 0, q+1).

This finite indexed formula specifies every initial source, including q=L-1;
there is no unlisted terminal correction. Every source lies at distance L
from c_G. Its value is affine in the five seeds, never a precomputed G.
At most 3L nonzero entries are needed; the huge list is deliberately not
materialized. `source_mask` in the checker evaluates the exact formula,
although evaluating all actual giant indices is not part of the bounded test.

Prepare the current ball B_L(c_G) and previous ball B_(L-1)(c_G), preserving
these source entries and setting the other entries to zero. Each source is
on the current boundary and outside the previous ball. The herald's whole
raw prefix is therefore blank before L.

To see the native realization, restrict to shortest paths from the boundary
to c_G. Paths from the three wings meet only on the axial spine. Before
that meeting, each wing has a single rotating field, so the native update
is the XOR Pascal recurrence there. The injected wing bit at spine step t
is XOR_(q subset t) A_w(q). The binary subset-sum transform is its own inverse:
each proper subset coefficient occurs an even number of times, while the
diagonal occurs once. Hence the injection is B_w(t), rotated into the
component (w-t mod 3), and the sum of the three wings is exactly g_t.
The old-local field on the first front is causally blank. The spine therefore
performs precisely H(state XOR g_t) at every step, including the terminal
zero input. This proves the arbitrary finite-length source formula used at L.

The first 2,684 profile rows have coefficient rank five. Since the source
transform is triangular with diagonal one, the source encoding retains those
five independent seed dimensions. The padding is constant and adds no seed.
Adding independent z gives six dimensions in the full new seed bank. If a or
b was already counted in a proposed local masking branch, it is shared here
and must not be counted again as a fresh independent bit.

## Native fair z and simultaneous geometry

Put the private z receiver at c_Z=(-48L,0,0). At its original-time source
c_Z+(0,-L,0), place the pure-A triple (z,0,0). Prepare the current radius-L
and previous radius-(L-1) balls around c_Z, with that source preserved and
all other entries zero. The straight axial first-arrival path is unique.
Since L=1 modulo 3, H^L(z,0,0)=(0,0,z). Its whole earlier prefix is blank.
No z-dependent field is used by the herald.

All old sources, ready regions and reserved public-bank coordinates through
L have |x|<=13R: the previous remote herald occupies x up to 13R, the previous
remote z apparatus down to -13R, and the local/selector sources and banks
have smaller x bounds. Both new ready cones have |x|>=47L. They therefore
consume no old source or bank coordinate. Conversely old sources cannot
reach either new receiver by L. The new herald hemisphere lies at x>=48L;
it cannot reach any local or old receiver by its designated time. The z
source is separated in the opposite direction. The two new current cones
are disjoint since their centers are 96L apart.

Use a no-wrap torus large enough for this enlarged initial apparatus, for
example side 256L+64T+1. All relevant signed x coordinates have magnitude
at most 49L and their pairwise differences are smaller than half this side;
the y,z ranges are smaller. This is an explicit resource enlargement for the
candidate and does not alter P or the previously checked local causal cones.
No new physical premise or change of availability is adopted by this report.

Through L, the only new public port needed is c_G. Its full prefix is blank
and its final whole triple is (0,G,0), so it needs no additional public-noise
frontier before or at L. The z port remains private until the intended
terminal access. Later readout times would need a new history/boundary audit.

The existing seven-port chronological-bijection argument tolerates arbitrary
complementary background and still applies because its reserved bank remains
free. Its whole noise word is therefore independent of the new seed bank
under the stated initial independence. The new herald refines that law by
the explicitly computed G, without leaking extra fields or suppressing
failures. This argument does not certify simultaneous local carrier outputs
that have not yet been constructed.

## Controls and replay

The bounded test checks all 32 predicate assignments, all eight identity-word
register states, the exact giant integer schedule, affine rank, and actual
geometry bounds. It then independently constructs a 2,698-step native-wing
realization using two identity blocks and replays every wing recurrence on
32 packed seed cases: 86,336 input comparisons. This is a direct source-to-
spine check, not merely evaluation of the abstract word. The general source
identity above justifies the actual m; the bounded realization is not claimed
to simulate L steps.

Both wrong-phase controls are rejected: omitting the extra zero H puts the
herald in the wrong field, and putting z in the wrong initial field gives the
wrong whole raw z output. A shared z=a source keeps z marginally fair on
success but changes its joint law with (a,b) by TV=1/2; this negative control
is also detected. All 64 new seed assignments are enumerated with successful
and failed plane/z counts retained.

From this directory in the retained tree, run `python3 checks.py` and
`python3 -O checks.py`; both outputs equal `result.json`. The only non-stdlib
input is the hash-pinned retained herald JSON. No new Lean certificate,
full-equivalence claim, dispatch, F/E designation or merge is asserted.
