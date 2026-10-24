# An initial seed-only pulse produces a clean native q7 Y code

24 October 2026. Constructive follow-up to the uncorrected outward-port scan.
Author-checked result; independent review pending. This is a different initial
apparatus preparation, explicitly specified below, not an operation performed
mid-run. Repository read-only.

## Result and scope

Keep the q7 depth-seven initial ready extension and add the initial source

    f=(0,S,S+2d+14),   U_0(f)=(u,0,u),   d=68.

All other sources and initial conditions remain those of the uncorrected q7
construction. Only the q7 ready prescription is adopted for this candidate;
the separate k8..12 scan preparations are not jointly adopted. The payload depends only on the existing apparatus seed u, not
on unknown input x or the arriving operand. It is affine in u and needs no
additional independent random bit.

At q7=qY+7e_z and N=R+7 the native full triple becomes exactly

    U_N(q7)=(0,0,y),   y=x XOR u.

The originally arriving qY.D operand is transferred genuinely: replacing only
qY.D at tickR by diagnostic p yields

    (x(1 XOR u)(1 XOR p), (x XOR u)(1 XOR p), p).

Thus D=p for every assignment, and both other fields vanish on native runs.
For arbitrary diagnostic p the whole triple is not always clean; only D=p
is universal.
This is a native clean readout of the original qY operand under the modified
initial preparation. It is not a Y reset, and not an arbitrary reusable q2
input socket. The distinction is tested again after the correction below.

## 1. Initial source and causal compatibility

The source lies14 cells beyond the old upper pulse Q=(u,0,1) at
`(0,S,S+2d)`. It lies exactly on q7's current ready boundary:

    dist(f,q7)=N,   dist(f,q7+e_z)=N-1.

It is outside all fifteen inherited current ready regions, including q2 and
the optional q3 extension, and overwrites no entry in the1,479-source table.
It is disjoint from all protected frontier families: the near families have
z=0 or negative z, and the remote families have separated x coordinates.
The new source is an explicit exception to the new q7 ready-zero prescription.
Relative to the earlier uncorrected q7 scan, this changes the source value
that was zero. It does not silently claim the same full initial preparation.

The existing u seed is copied into two fields at f. Every field is affine in
that already present seed, so the initial seed rank does not increase. This
is still a supplied initial correlation/readiness resource, not a constructed
native initializer or a free preparation theorem. No unknown x, later p, or
native y is preloaded at f.

Finite speed gives stronger endpoint exclusions:

- f cannot affect any q7 prefix before N, or its old local term at N-2;
- at the final neighbour slice N-1, only the upper neighbour q7+e_z can depend
  on f. Its distance isN-1; the other five neighbours are at distanceN+1;
- all fifteen old receiver centers are farther thanN from f, so their complete
  histories throughN are unchanged by this source correction;
- every earlier straight-outward endpoint k<=6 is outside f's cone at R+k.

Each of the four lower source positions has distance2N from f. Along the unique
first-arrival path from f to the upper neighbour, no lower-source contribution
can arrive in time. The qY.D and q2.A diagnostic interventions are also outside
that neighbour's backward cone. Its value is therefore an exact upper/C dipole
calculation, with the lower sources absent, even though lower/old-upper
interactions have occurred elsewhere earlier.

## 2. Full nonlinear dipole calculation

Allow the new source C to range over all eight triples while fixing u. Use an
axial coordinate directed inward from the old upper pulse. The two sources are

    axial0: Q=(u,0,1),   axial-14: C.

The upper neighbour at N-1 is queried at

    n=R-8=P+245,   t=N-1=P+259,   ell=t-n=14.

The closed strip of budget14 is sufficient. Its universal identity exponent
`12*840^14` divides actual P, so the query is exactly equivalent to the same
full two-source evolution at n'=245,t'=259. This reduction does not add the
isolated pulse solutions. The sources can interact at tick7, and that
interaction is retained in the directly computed initial strip and all later
native updates.

The complete C-to-upper-neighbour maps are:

| C | u=0 | u=1 |
|---|---|---|
| 000 | 110 | 111 |
| 001 | 010 | 110 |
| 010 | 101 | 101 |
| 011 | 111 | 100 |
| 100 | 011 | 000 |
| 101 | 001 | 010 |
| 110 | 000 | 001 |
| 111 | 100 | 011 |

Each column is a permutation of all eight triples, consistent with the unique
first-arrival path. C=000 is the uncorrected background. Choosing C=(u,0,u)
gives the upper-neighbour change

    delta(u)=(u,0,u).

The unique choices are C000 for u=0 and C101 for u=1. The old local triple
`U_(N-2)(q7)` is111 for either u, independently verified by the separate
single-pulse strip and by the retained full shrinking diamond.

## 3. Full final native update

Let the uncorrected neighbour XOR at timeN-1 be(A,B,D), and the old local term
be111. The unchanged rule gives

    old_output = 111 XOR H(A,B,D).

Only the upper neighbour changes, by the computed delta=(u,0,u). Therefore the
new output has the same A field, its B field toggles byu, and its D field
changes by

    deltaD=u XOR uB = u*(old_output.A).

For the uncorrected qY.D diagnostic,
`old_output.A=x(1 XOR u)(1 XOR p)`, so this product vanishes for every assignment.
Consequently the full corrected diagnostic is

    (x(1 XOR u)(1 XOR p), (x XOR u)(1 XOR p), p).

Substituting native p=x XOR u makes the first two entries zero. No neighbour
field was manually blanked; the clean code emerges under the original native
update from the specified initial sources. This is not a bijection on one
isolated three-bit cell. Information remains elsewhere in the reversible
lattice and its correlated apparatus state, so the earlier three-code counting
obstruction is not contradicted.

## 4. The q2 reuse diagnostic still fails

A separate test leaves qY native and replaces only q2.A at R+2 by p2, keeping
q2's other two native fields. After the new source correction, q7 equals

    ((x XOR p2)(1 XOR u),
     x XOR u XOR p2,
     x XOR xu XOR p2 XOR xp2 XOR xup2).

All32 x,u,mY,mR,p2 assignments are checked after correction. In particular
x=1,u=0,p2=0 gives111, whose D field is not p2. The correction cannot influence
the upper neighbour through this late intervention, and its D adjustment
again vanishes because u times the relevant old A field iszero.

Thus the native q7 clean code is a constructive readout result for the existing
qY-initiated wave. The proof does not turn a later arbitrary q2 input into a
clean reusable socket. A subsequent native measurement/reset still requires
its own interface and conditional-resource construction.

## 5. Privacy, resources, and probability boundary

Because f first reaches q7 only atN, it cannot repair the informative early
prefix. The uncorrected prefix atR-7 remains(u,u,1). The receiver must remain
private until the designated read under the inherited supplied access rule.
No native shutter, clock, or access-closure mechanism is added.

The source change does not consume or pin any reserved frontier coordinate.
The depth-seven geometry still requires147 extra initially independent fair
bits to extend the seven old public records fromR toR+7, using the inherited
joint-frontier theorem. This is105 more than the earlier depth-two window.
The correction itself adds no independent random seed. The old receiver
histories are unchanged throughN by finite speed. A complete independent
joint-history certification is not supplied by this local calculation.

There is no new herald. The established first-reset success/failure accounting
remains the one inherited from the earlier construction:5/16 success,11/16
failure given earlierx. On success each native y has mass5/32 unconditionally
with respect to that first reset. The correction creates neither a second
successful carrier nor the required5:3:2 post-Y distribution. Failed runs are
not discarded or reclassified. A clean readout code alone is not a reset.

## Checks and replay

`correction_checks.py` verifies10,080 direct spatial-recursion/strip comparisons
for all16 u/C inputs, all70 strip entries and n0..8; both complete source
permutation tables; the exact universal-period divisibility; the zero-C
single-pulse baseline; the old local111 triple; source and receiver exclusions;
the complete final native update; all32 qY.D and all32 q2.A interventions;
all native clean codes; and the unchanged early prefix.

Run `python3 /path/to/outward_v6_geometry/correction_checks.py` and repeat with
`-O`. The script needs model.py, correction_model.py, PROVENANCE.json and the
same hash-verified geometry source as the uncorrected scan. Normal/-O outputs
match. Replay writes no files and uses no network. CORRECTION-SHA256SUMS pins
this constructive milestone separately from the uncorrected scan.

The universal strip theorem and inherited preparation/access framework remain
explicit dependencies. This is an author result pending independent review,
not a Lean certificate, a completed native instrument, or full QM equivalence.
