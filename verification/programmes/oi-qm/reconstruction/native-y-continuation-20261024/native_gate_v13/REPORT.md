# Native nonlinear processing and the short physical-pointer window

Research checkpoint, 24 October 2026. The preregistered bounded families
contain genuine native products of the old unknown sign with actual fresh
pool operands. They do not yet supply the intended acceptance flag: none
of the 525 tested whole-cell terminal pointers determines that flag, even
with arbitrary Boolean relabelling. This failure also holds on the
prepared-shape sector P.A=0, and for the complete same-site prefixes
examined here.

These are seven explicit small original-time lattice families. They do not
simulate the enormous-L programme boundary and establish no no-go at that
boundary, for distributed circuits, later times, other source geometry or
OI generally. The positive polynomial below is a native masked nonlinear
coupling, not an isolated available logic gate or a quantum instrument.

The plan was published on #910 at
`9e92ff42cdb254e0de23202409888c3f5034bf39` before execution. The inherited
Native A source report is author
`f24a57a7c23cc1818c04265cec7604f8bc2f410d`, included in the source
snapshot `16b154cefe3acd40d5a60d507905709c3cfc19ca`.

## 1. The exact native family and the decision tested

Use the complete cubic-lattice rule

    U_(t+1)(v) = U_(t-1)(v) XOR H(XOR_(w~v) U_t(w)),
    H(A,B,D) = (B,D,A XOR BD).

For n=1,2,3, place four triples in the initial current slice at

    f_old=(-(n-1),0,0),
    f8=(-n,0,-1), f10=(-n,0,+1), f9=(-n-1,0,0).

Each payload independently takes all eight values. The 4096 worlds are an
exhaustive equal-weight comparison ensemble, not an adopted physical prior
for the old carrier. The old-input source is the sole initial unknown-input
location. No extra copy of the unknown sign or nonlinear predicate is
preloaded. The other three triples are nine initially supplied apparatus
bits. The previous slice and all other initial current sites are fixed by

    background(seed,t,x,y,z)
      = ((x*x+3*y*y+7*z+13*t+seed)
         XOR (x*y+z*z+11*seed*t)) AND 7,

for seed=0,3. A seventh family uses n=1 with both complementary slices zero.
All nonzero native paths, six neighbors and old-local terms are retained;
there is no late-time cold apparatus splice or truncation of the cone.

The old physical field P=U_(n-1)(0) is a bijective function of f_old and
is independent of the three fresh payloads. At time n the three fresh
sources map bijectively to the actual fields (Q8,Q10,M) at (0,0,-1),
(0,0,+1),(-1,0,0), conditional on each old input. The source distances to
these targets, minus n, are (0,2,0),(2,0,0),(2,2,0). Their distance to 0
is n+1, so they cannot change P. The actual pool/ciphertext map
(Q8,Q10,V), with V=U_(n+1)(0), is also bijective on 512 values for each old
input. All eight P values occur; P is not silently assumed clean.

The tested event uses actual fields:

    s=P.B, Y=Q8.B, R=Q10.D,
    K=Q8.A+2 Q8.D+4 Q10.A,
    A=[K<threshold(Y XOR s,R XOR s)],
    threshold(00,01,10,11)=(5,0,4,1).

For each old input, 160 of 512 fresh worlds satisfy A. On P.A=0 there are
2048 worlds, with 640 accepted. This is the intended abstract comparison
event. It is not a native public flag.

## 2. A native product of the old sign and pool operands

For the n=1 zero-complement family, write the four initial triples as
P=(pA,pB,pD), x, y, g. Direct native propagation gives

    Q8=H(P XOR x), Q10=H(P XOR y),
    M=H(P XOR x XOR y XOR g),
    other three current neighbors=H(P).

Define

    J = gA XOR pB*gD XOR pD*gB
        XOR xB*yD XOR yB*xD
        XOR gB*(xD XOR yD) XOR gD*(xB XOR yB) XOR gB*gD.

Then the actual two-tick origin is

    V=(pA XOR gD, pB XOR J, pD XOR gB XOR gD*J).

The formula is checked against all 4096 complete native worlds, and a
Boolean Möbius transform independently reconstructs the polynomial. It
contains pB*gD and pD*gB, and the D field also contains pD*gB*gD. Removing
the native B*D term changes 2432 physical worlds; removing the old-local
term changes 3584. Thus the apparent products are not produced by a decoder
alone or by omitting nonlinear propagation.

The same actual world table has a bijective change of coordinates to
(P,Q8,Q10,M). On its attained affine old-input sector P=(0,s,1), put

    E=Q8.A XOR Q10.A XOR M.A,
    B=Q8.B XOR Q10.B XOR M.B,
    D=Q8.D XOR Q10.D XOR M.D.

The physical current triple becomes

    V=(B XOR 1, D, 1 XOR E XOR D XOR B*D XOR s*B).

In particular V.D contains the actual logical products

    s*Q8.B, s*Q10.B, s*M.B.

The first factor Q8.B is the prospective Y operand, not a stand-in source
bit. This is a positive native processing witness in the stated small
source family. E and the other terms remain physical masks/workspace;
there is no claimed local operation that removes them, no clean Toffoli
implementation and no new permission to read the masks. Whole V remains
uniform conditional on P, as required by the independent source control.

The intended A has Boolean degree four and 28 ANF monomials in independent
(s,Q8,Q10). Substituting the fixed seven-site inverse for s gives degree
four and 72 monomials in that formal phase basis. These are complexity
diagnostics only. A native output coordinate is at most quadratic in an
unconstrained one-tick phase input, but actual prepared fields have causal
relations. No native-family exclusion here is inferred from formal degree.

## 3. The fixed single-cell pointer test

Candidate terminal cells are the 25 positions in the radius-two Manhattan
ball about 0, at deadlines n+d for d=1,2,3. Each candidate may use any of
all 256 Boolean functions of its complete terminal triple. For a raw value
v let c(v,a) count source worlds with that value and event A=a. Its optimal
flag error is

    sum_v min(c(v,0),c(v,1)) / total_worlds.

Zero error occurs precisely when every nonempty raw cell has only one
A value. The checker independently exhausts the 256 readouts, checks exact
raw collisions, and retains a compact opposite-A payload witness for each
reported best pointer. It checks both all eight old P values and the
prepared-shape sector P.A=0. A synthetic record containing A passes the
same classification, so the procedure is capable of a positive verdict.

The best prepared-sector terminal error across all 25 sites is:

| Family | d=1 | d=2 | d=3 |
| --- | --- | --- | --- |
| n=1, seed=0 | 19/64 | 5/16 | 5/16 |
| n=1, seed=3 | 19/64 | 5/16 | 5/16 |
| n=2, seed=0 | 5/32 | 39/128 | 5/16 |
| n=2, seed=3 | 3/16 | 143/512 | 5/16 |
| n=3, seed=0 | 9/32 | 5/16 | 5/16 |
| n=3, seed=3 | 9/32 | 5/16 | 5/16 |
| n=1, zero complement | 19/64 | 5/16 | 5/16 |

None is zero. On the full eight-P comparison ensemble, the best terminal
error over all families/sites/deadlines is also 5/32. These are exact
errors for equal-weight declared ensembles, not quantum prediction errors
or general OI approximation floors. An operation that must work on every
world in one of these families already fails on an explicit collision.

For each fixed site the complete whole-triple prefix from time n through
its deadline is also retained in the computation. No one of those prefixes
determines A exactly. The smallest prepared-sector prefix error over the
window is 37/256, attained for n=2, seed=0 at d=3. A prefix decoder is only
an additional information diagnostic; it is not counted as a physical
terminal acceptance flag. This calculation neither grants access to these
prefixes nor proves their public safety. The programme's actual complete
public past is not identified with this short local trace.

Pooling all seven ensembles and requiring one common terminal relabelling
leaves optimal error 5/16 at all three deadlines. That stronger readout
uniformity requirement is reported separately; the per-family collisions
already establish the scoped failure.

## 4. Evidence, replay and remaining gate

The checker uses only standard-library exact integers and fractions. Seven
packed native families cover 28,672 full worlds, 525 terminal pointer cases
and 525 complete local prefixes, each on both old-P sectors. An independent
scalar integer recursion agrees on 168 selected actual field values,
including the latest declared deadline. The triangular source/ciphertext
controls verify 56 old-input sectors, each with two full 512-state bijections. The fixed inverse is checked
on every world. All 256 terminal readouts are exhausted per candidate and
sector; logical/physical ANFs are reconstructed exactly. No floating-point
acceptance threshold is used.

Run:

    python3 checks.py
    python3 -O checks.py

Both outputs must equal result.json byte for byte. The structured output
retains the measured error tables, compact collision payloads, complete
raw-prefix count fingerprints and native polynomial data. Deterministic
code regenerates the full bounded counters; large raw world/trace dumps
are not retained. The initial implementation run took under four seconds
and about 22 MB of peak resident memory; this is a bounded local check,
not an unbounded search or giant-time simulation.

The productive positive result is actual nonlinear old-X/pool coupling.
The negative result closes the specified passive short single-cell pointer
route in the stated small source families. A physical acceptance gate still
needs a source-compatible controlled circuit or new native geometry, full
pointer metadata/history checks and an outgoing boundary another native
stage can use. The distributed two-slice route, the actual huge-L boundary,
probability selection, access closure, general menus/depth and composites
remain open. No physical premise/access/map adoption, F/E designation,
special dispatch, merge, external validation or full-equivalence verdict
is claimed.
