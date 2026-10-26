# Fixed continuous vectors do not supply a reusable projective reset

Research checkpoint for #911, 24 October 2026. Iterating the specified
fixed-vector/two-bit update gives the correct first quantum read but fails
already on the next read. Starting at Z+, the public sequence X then Z has
final Z+ probability2/3 instead of1/2 and complete-record TV distance1/6.
The initial two-vector resource therefore cannot replace the fresh reset
source in our preceding all-finite-depth architecture comparison by this
particular update alone.

This is a scoped extension test. Montina's original primary paper,
[arXiv:1108.5138v3](https://arxiv.org/abs/1108.5138v3), explicitly studies
transitions between two consecutive measurements with time-correlated
noise; its proven two-time result is preserved. We instantiate the maps
in Ruebeck, Lillystone and Emerson,
[arXiv:1812.08218v3, section4.1.2 Eq.17](https://arxiv.org/html/1812.08218v3),
and test repeated use. Both sources are credited; no novelty for their
models or two-time result is claimed. Our negative conclusion concerns the
fixed-vector iteration written below, not a refutation of the original
scoped theorem, every possible noise process, OI or exact reconstruction.

The plan was published before computation at
cf1855ed1576adf446fbc505c027928bce4c4cb7. #885 remains read-only. No physical
premise, access rule or operational correspondence is adopted.

## Explicit source and update

Let u0,u1 be independent uniform points of S^2. They are present at the
start. Store an active index r in{0,1} and an orientation sign t in{+1,-1}.
For a direction a write

    m_a(i)=sign(a dot ui),
    j_a=argmax_i |a dot ui|.

Ties have probability zero for the stated prior; a fixed index convention
makes every map total. Preparation at unit Bloch pole n means

    r=j_n,   t=m_n(r).

A read at a reports and updates

    k=t*m_a(r),   r'=j_a,   t'=k*m_a(r').

Both continuous vectors remain unchanged. A rotation R rotates both vectors
and leaves r,t unchanged. This is a supplied exact real operation, not a
compiled native lattice gate. In the paper's reference n0=Z convention,
t=s*sign(Z dot u_r). Substitution gives its response and Eq.17 bit update.
The checker evaluates that reference-basis formula separately on every
bounded step, rather than trusting a relabeling of the t implementation.

This initial distribution uses known preparation settings to choose r,t;
it does not supply an unknown preparation label to the later reader. The
same physical u0,u1,r,t are the entire tested autonomous carrier. Any extra
renewal, later clock dependence or response-relevant memory changes this
specific continuation and must be stated.

## Why the two-time control works

For a fixed incoming preparation n, a particular vector u wins when the
other vector has |n dot u_other|<|n dot u|. The absolute projection of a
uniform sphere point is uniform on[0,1], so that event has probability
|n dot u|. Either of the two vectors can win. Consequently the selected
vector has density |n dot u|/(2pi).

Fold its sign toward n: lambda=sign(n dot u_r)*u_r. Antipodal contributions
then add, giving the density

    (n dot lambda)_+/pi.

The reported k is sign(a dot lambda). Thus the independent cosine-density
hemisphere integral from the preceding architecture gives probability
(1+n dot a)/2. The winning-vector construction changes a uniform point into
the required preparation without inserting a quantum probability table.
All first measurements and intervening supplied rotations have the right
quantum law under this initial preparation.

Our checker independently integrates the cosine density in an XZ plane:
polar integration leaves one-half the integral of a linear sine/cosine over
the intersecting azimuth intervals. Its primitive is evaluated at rational
unit endpoints, and compared with a separate rational2x2 projector engine
on144 preparation/read pairs. This controls the analytic reduction to the
known first-read model; it is not evidence that a post-read two-vector
ensemble has been restored to its original preparation family.

## Exact three-measurement witness, counting preparation

Prepare Z+, then read X and Z, retaining both public outcomes. Let

    i=j_Z,   j=j_X,
    e_l=sign(u_l.z*u_l.x).

The X outcome is k=e_i. Applying the same specified update and returning
to Z gives

    ell=e_i*e_j.

If i=j then ell=+1 with certainty. If i!=j, the X/Z coordinate signs of the
two independent sphere points are fair and independent of their absolute
coordinates. In that case k and ell are independent fair signs.

The remaining geometric probability is exact. Set

    D_x=u0.x^2-u1.x^2,
    D_y=u0.y^2-u1.y^2,
    D_z=u0.z^2-u1.z^2.

Their sum is zero. Apart from zero-measure ties, their sign pattern has
either one positive or two positive coordinates. Coordinate permutations
and exchange u0<->u1 act transitively on the six possible patterns, while
preserving the source measure. Each pattern therefore has mass1/6.
The event i=j is D_x D_z>0; precisely two patterns have that property.
Hence

    Pr(i=j)=1/3,
    Pr(ell=+)=1/3+(2/3)(1/2)=2/3.

The complete public law is:

| X outcome | Z outcome | Fixed-vector update | Quantum instrument |
| --- | --- | ---: | ---: |
| + | + | 1/3 | 1/4 |
| + | - | 1/6 | 1/4 |
| - | + | 1/3 | 1/4 |
| - | - | 1/6 | 1/4 |

Their total variation distance is1/6. No outgoing decoder choice can repair
the difference in these already public records. A new conditional
freshness or ensemble-closure theorem is therefore needed before promoting
the two-time source construction to repeated projective instruments.

The computation uses96 equal-measure response cells: six magnitude-order
sign patterns times16 independent X/Z reflection choices. The rational
unit-vector pair(2,3,6)/7 and(6,2,3)/7, coordinate permutations and pair
exchange supply strict interior witnesses for every magnitude pattern.
These points are witnesses for the constant response cell, not a finite
approximation to sphere area. The symmetry proof establishes the exact
cell weights; the finite engine evaluates the actual response on each cell.

## Longer records expose persistent source reuse

Continue the fixed sequence X,Z,X,Z,... from Z+. With the same definitions,
e=e_i e_j is fixed forever. After every completed pair, the Z outcome is
multiplied by e. The X outcomes change by the same factor on the next pair.
Thus every record is determined by the initial k and e. There are only
four possible records once two reads have been made, with masses
1/3,1/3,1/6,1/6. The quantum alternating projective process has every h-bit
record with probability2^-h.

For h>=3 all four model masses exceed2^-h, so the complete-record TV is

    1-4/2^h.

The checker confirms h=1,2,3,4,6,8,10 by the actual fixed-vector update
and independent projector products. The ten-read TV is255/256. The
all-h expression follows from the explicit four-record recurrence,
not extrapolation from those bounded checks. This does not exclude a
controller with an additional resource stream or another update.

## Reversibility costs a retained bit even before source renewal

For fixed vectors and a fixed read direction a, the logical map above
sends four incoming(r,t) values into two outgoing(k,r',t') values: r' is
fixed at j_a and t' determines k. The public record does not make it
injective. An implementation preserving this explicit microscopic update
must retain the missing active-index distinction somewhere.

One blank garbage bit g and a public pointer bit c give a concrete total
bijection. Encode r,g,c as bits and keep t as a sign:

    k=t*m_a(r),
    r_new=g XOR j_a,
    t_new=k*m_a(r_new),
    g_new=r,
    c_new=c XOR 1[k=-1].

On g=c=0 it is exactly the specified update and public sign. Given the
output, first recover k=t_new*m_a(r_new), then r=g_new,
g=r_new XOR j_a, t=k*m_a(r), and undo the pointer XOR. This proves global
invertibility even off the ready subspace. The checker exhausts all16 bit
inputs on1152 vector/setting cases, with18432 inverse tests. Supplied
rotations have384 exact inverse and orientation-parity controls.

This is a generic reversible bit map for the fixed pair. It is neither a
native compiler nor a cure for the record discrepancy. The stated dilation
retains one garbage bit per invocation and one public pointer bit. No
universal lower bound on every realization's memory or entropy is claimed.

## A supplied-resource repair and its cost

A simple repair discards no physical information: after each read, retain
the used pair privately and take the next independent initially supplied
uniform pair. Choose its r,t from the known outgoing pole k*a. Conditional
on the complete earlier public history, its law is again exactly the
preparation family proved above. The first-read proof therefore applies
again. Induction gives the correct complete adaptive records and outgoing
quantum state for every finite horizon, under this explicit renewal and
private-memory isolation contract.

For h measurements including an outgoing reset after the last read, this
particular pair-based repair provisions2(h+1) sphere points initially:
two for initial preparation and two per reset. Used points, active-index
garbage and records are retained. A finite bank is consumed according to
the scheduled clock, rather than replenished during the experiment.
The bit-map dilation above accounts for its own lost index; additional
vector storage and reset routing are separate supplied resources.

A second, independent branch engine computes the renewed geometric kernel
through four adaptive levels. Across four input preparations and four
policies it agrees with rational matrix products on all256 leaf records,
including32 zero-mass leaves and the decoded outgoing state on each branch.
The result is a positive mathematical control for renewal, not a native
operation-availability theorem. It makes no claim that this much continuous
renewal is necessary for every possible repair. Counting a continuum
register as a single resource also does not bound the information in its
exact real value.

Removing the winning-vector selection is separately tested. A uniform
single vector folded toward Z and then read along(X+Z)/sqrt(2) gives3/4:
an exact eight-azimuth-octant response count derives that mass. The quantum
projector gives(2+sqrt(2))/4; their gap(sqrt(2)-1)/4 is strictly positive.
This countercontrol tests an actual changed geometric source, rather than
comparing two stipulated numbers.

## Consequence and retained evidence

The credited minimal-bit disturbance mechanism does preserve the first
quantum transition. Its deterministic fixed-vector reuse cannot supply our
required all-finite-depth interface. Generic reversible retention of the
changed bit is feasible, but restores no missing conditional source law.
The simple independent-pair repair keeps the continuous reset-resource gap
explicit. It provides no reduction relative to the preceding supplied KS
reset source, and no OI probability-selection principle.

All calculations are bounded exact rational/combinatorial controls.
The continuum and arbitrary-depth conclusions rest on the written symmetry,
density and recurrence proofs. Normal and optimized checker outputs are
byte-identical to result.json. The six curated files are PLAN.md, REPORT.md,
checks.py, result.json, PROVENANCE.json and SHA256SUMS. No mathematical
library, Lean certificate, full-suite verdict, exact-head attestation,
new public native access, F/E designation, dispatch or merge is asserted.
