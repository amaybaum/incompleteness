# A second native front restores X response but affine source compilation fails

Research checkpoint, 24 October 2026. Plan published on #910 at
`9e92ff42cdb254e0de23202409888c3f5034bf39`; source head
`16b154cefe3acd40d5a60d507905709c3cfc19ca`. This is a changed original-time
source geometry, not a repetition of Native B's excluded one-source route.

## Result and scope

One additional initial source on the lower first front removes Native B's
strong single-port loss of unknown X. Across all24 accepted old apparatus
contexts,32 common injective q10 output pairs are now compatible with some
known-seed E,N controls. However, none can be selected by jointly affine
initial E,N payloads. Of the2^18 affine E maps considered for each compatible
pair, only16 survive the native response constraints in total, and every
one requires a nonaffine N map.

This does not construct a clean native X operand under the allowed affine
source contract. It identifies a specific missing step: native computation
of a known-apparatus-seed control, or a different routing/encoding. It does
not exclude a redundant many-symbol decoder of q10, another source family,
distributed phase processing, Native A, or OI. An arbitrary redundant q10
decoder was not tested. No physical acceptance predicate or reusable quantum
instrument is supplied.

## Original-time geometry and retained phase

Keep T=185, P=12*840^185, S=P+185, R=S+68, L=R+9=P+262 and the inherited
torus. Retain Native B's q10=(0,S,78), deadline L+1=R+10, original-time
current/previous ready cones, old source/bank exceptions and the upper axial
source N=(0,S,S+156). This variant replaces the optional uniform F10 factor
by a ready pin, as Native B did. It does not inherit Native A's six-bit
Q8/Q10 pool unchanged. F8 may remain outside the new ready cone but is not
an additional q10 input by this deadline.

Add one current initial raw triple at

    E=(0,-78,78).

The E payload may be affine in the known old seeds k=(u,mY,mR,a,b), with
no unknown x or s and no precomputed nonlinear predicate. The table first
allows all eight E values, then tests exactly that affine restriction.
No new independent fair bits are needed for this first test. A fresh-c
follow-up was conditional on affine survivors; there are none, so no such
follow-up is executed.

E reaches q10 at distance L+1. Its distances to q9=(0,S,77) and earlier q8
are L+2 and L+3. Thus q9 at L, including s=x XOR u XOR a, is untouched. The
old q9 table is reproduced on all4096 new raw-source rows, including old
mask01 failures. All1479 retained sources avoid the new pins; E and N match
none of them and avoid all24 earlier ready regions. All eight informative
public records are causally unchanged at their respective record deadlines.

The old initial bank rays are neither overwritten nor pinned by the new
q10-ready extension. The exact piecewise-affine distance checks use their
interval endpoints and axial kink where present. E can change late noise
backgrounds before L; equality of every realized public-history string is
not asserted. The inherited chronological bank bijection preserves the old
conditional public-history law given the changed complement. That is a
source/history statement, not a claim that future gate carriers are jointly
independent of all bank variables.

## Exact lower-front calculation

The original unknown source O=(0,0,0), W=(0,-76,76), and E all lie on
y+z=0 with x=0. Their payloads are respectively (0,x,0),111 and E. At the
positive first front t=y+z, all four transverse/forward neighbors and the
old-local term are too late by finite speed. Hence the complete native rule
reduces there to

    F(y,z)=H(F(y-1,z) XOR F(y,z-1)),
    H(A,B,D)=(B,D,A XOR BD).

This is nonlinear coupled evolution of the actual three sources; their
independently evolved responses are never added. Initial data lie on the
y+z=0 diagonal. A finite two-dimensional recursion computes the y=0 values
at z=76,77,78 jointly, including all earlier W/E interactions.

For j>=1 define F_ell(j)=F(j,76+ell). Below z=76, only the original O front
can arrive. Its known parity coefficient gives

    F_0(j)=H(F_0(j-1) XOR [j AND75=0] H^(j+75)(0,x,0)),
    F_ell(j)=H(F_ell(j-1) XOR F_(ell-1)(j)), ell=1,2.

The forcing period is lcm(128,12)=384. Over that block, the map on its own
triple is a permutation of eight values. Every such permutation has order
dividing840. Thus F0 has period dividing384*840; successively F1 and F2
have periods dividing384*840^2 and384*840^3. This holds for each fixed E,
including its changed finite initial value. Actual P is divisible by that
last bound. No simulation of P ticks or observed-period extrapolation occurs.

At the pre-collision slice R-1, E enters the full q10 diamond at exactly
local (0,-11,10), absolute (0,S-11,78), requiring F2(174) after the period
reduction. It reaches no required R-2 entry. The W/origin levels are the
same three coupled entries already used by Native B. The signed upper strip,
including N, retains its budget20 and period12*840^20, also dividing P.
These initial upper/lower fields then evolve together through the full
shrinking three-dimensional q10 diamond. All six neighbors and old-local
terms are retained after collision.

Native B's signed upper evaluator and collision engine are adapted and
credited in PROVENANCE.json. The new E lower front, table expansion and
complete affine-source decision are implemented here. Separate internal
review must revalidate the new reduction and scope independently.

## Native response and exact affine decision

The full4096-row q10 table is stored in result.json in lexicographic order

    x,u,mY,mR,a,b,Ecode,Ncode, code=4A+2B+D.

Its ASCII-hex SHA-256 is
`b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc`.
This table includes all raw triples and old failures; it is not a selected
moment calculation. The E=000 subtable reproduces all512 old q10 rows.
For every fixed old context and held other source, varying E or N permutes
all eight output triples. Omitting E changes3584 of4096 rows. The additional
front has therefore changed the physical unknown-input response, rather
than merely relabeling Native B's old table.

For each accepted known context k, form every ordered pair
(q10 for s=0,E,N; q10 for s=1,E,N) with the same E,N. Their common injective
intersection now has32 pairs. It includes (000,101), among others; the
E=000-only intersection remains empty. This is native response compatibility
under known-seed controls, not permission to prepare those controls
nonlinearly at time0.

An arbitrary affine E(k) has18 binary coefficients: three fields times six
features (1,u,mY,mR,a,b). The checker represents every64^3 coefficient triple.
Exact bit-set elimination rejects inconsistent E maps without an unbounded
search. For a retained E map and a desired first raw symbol, the own-N
permutation gives a unique N(k). Gaussian elimination then tests that entire
N law on all24 contexts for the same six affine features. Eight of the32
raw pairs admit exactly two affine E maps each; the other24 admit none.
None of the16 resulting N laws is affine.

One explicit rejection illustrates the missing computation. For the raw
pair (000,101), an allowed affine candidate is

    Ecode=5 XOR u,  i.e. E=(1,0,1 XOR u).

Holding mY=mR=b=0, the uniquely required N values are:

| u | a | required N code |
|---|---|---|
|0|0|0|
|0|1|6|
|1|0|7|
|1|1|6|

The four affine feature rows XOR to zero, but the four N triples XOR to111.
Every affine source must give zero on this relation. This is an explicit
known-seed interaction that cannot be silently inserted into the initial
prior. The checker retains analogous rejection witnesses for each pair
with affine E survivors. It does not claim a native implementation of any
nonlinear N law, nor that only one nonlinear gate would suffice.

The failed decision concerns one common raw binary X code across accepted
old contexts in this fixed two-front geometry. It does not rule out a
weaker distribution-level quantum instrument, a redundant raw alphabet,
record-aware output decoding or a changed physical preparation contract.

## Controls, replay and remaining gate

All controls succeed before the route verdict is emitted:

- 97152 signed-upper scalar comparisons against full native recursion;
- 144 lower scalar comparisons at the actual W/E gaps against independent
  full six-neighbor native recursion;
- 640 scalar front comparisons against an independently advanced small
  full three-dimensional sparse native world;
- exact upper/lower period divisibility, source/readiness/bank geometry,
  all4096 old q9 rows, and the512-row E=0 old q10 subtable;
- 512 own-E and512 own-N permutation contexts, the3584-row omitted-E
  countercontrol, and the retained old single-N failure;
- exact affine solver positive/negative controls and explicit nonaffine
  required-N relation witnesses.

Run `python3 checks.py --source-root <retained-native-root>` and repeat
with `python3 -O`; both must reproduce result.json byte for byte. The default
source root accepts the canonical sibling checkpoint_v12 while developing,
or the retained native package root after publication. Source/proof bytes
are hash pinned in PROVENANCE.json. SHA256SUMS covers the five companion files; the package has six curated files.

This is a bounded exact native source-family result with a written
large-time reduction, not a general OI no-go or a complete instrument.
The next constructive step is a physical known-seed control computation,
a different source layout, or distributed processing of the retained phase.
The correct acceptance event, complete new pointer/prefix law, reusable
outgoing boundary, access closure, A1/A2 reconstruction and composites remain
open. No new premise/access adoption, #885 write, F/E designation, dispatch
or merge is included.
