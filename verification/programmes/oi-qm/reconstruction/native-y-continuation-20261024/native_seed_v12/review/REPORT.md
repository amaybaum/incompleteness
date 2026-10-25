# Separate-author review of Native B's outward seeded port

Verdict: **accept within the stated single-port/source-family scope**, with
no blocking findings.

Author: #910 at `1c91d3158e13eaa69c7fd1710932c9995d0288d7`, under
`native_seed_v12/`. The five changed Git blobs at that commit and the
inherited PLAN blob were checked against the local reviewed files; all six
match. The author's normal and optimized commands reproduce its retained
result byte for byte. `INPUT-HASHES.json` pins those six files and the five
inherited source/proof inputs at the stated base. This is a separate-agent
internal review, not external validation or kernel certification.

## Independent native reconstruction

The review imports no author engine. Its checker uses a distinct interleaved
three-bit lane representation, rather than the author's three separate
bitplanes and expansion maps. It retains signed x and signed y throughout
the upper strip; neither spatial reflection is imposed in the evaluator.
Independent full six-neighbor recursion initializes that strip and checks
1,782 short-time packed values on 891 signed nodes. Each packed comparison
covers 64 distinct upper-source assignments; duplicated lower/pad lanes are
not counted as new independent assignments. Ten initial-strip witnesses
detect an incorrectly imposed x reflection. The unfolded y values do obey
the surviving reflection symmetry.

For origin/W, a separate two-dimensional monotone first-front calculation
is run at the actual gap 76. Both initial sources lie on y+z=0; at the
leading time y+z, only the south and lower-z neighbors can have arrived.
The old-local term, x-transverse directions and forward directions are too
late by at least two ticks. Thus a grid initialized at origin and (-76,76)
computes the full coupled H front directly, without the author's three-layer
recurrence. It agrees with that recurrence on 531 layer/query cases through
j=176. A separate unreflected full three-dimensional native simulation at
small gap four checks 30 scalar first-front cases, including the old-local
term in that simulation.

Those independently computed upper and lower values initialize both slices
of the complete shrinking q10 diamond. The late evaluator retains all six
neighbors and the previous local triple. All 512 q10 triples agree with the
author, including every mask01 physical row. The encoded-table digest is

    8bc1462854ce5fb80c18a48e8208037eb6bd613aa5babb28721e186aec3387f9.

The qY, q7, q8 and actual q9 values also agree in all 512 rows, including
all eight new-N values. The q9 comparison uses the retained earlier native
table, not a newly assumed clean-input formula. As in the source, the
inherited old-front/transport description is a dependency; this review does
not re-certify all earlier compiler applications or the full manuscript.

## Period and geometric arguments

The signed upper strip's budget is 20, with Q/C/G/J/K/N evolved together.
For a layer ell and transverse position, the next axial value is a
permutation of its own previous triple, forced only by lower layers.
The old-local and forward-z terms are in layer ell-2; transverse terms are
in ell-1. The budget ell+|x|+|y|<=20 is closed under these dependencies.
H has exponent 12. After a period of the lower forcing, each same-layer
triple undergoes an eight-element permutation whose order divides 840.
This gives the sufficient common exponent 12*840^20. The argument does not
multiply the exponent once per transverse site, since sites at the same
layer have no same-layer coupling. Actual P is divisible by this bound.

The F0 forcing is the product of a 128-period Lucas-parity condition and
a 12-period H phase, hence has period 384. Its block map is an eight-state
permutation, giving the sufficient period 384*840. Successively forcing F1
and F2 gives 384*840^2 and 384*840^3. Their initial conditions are correct:
the additional south-W forcing vanishes for ell=1,2 because 75 shares a bit
with both ell values. The checker verifies actual P divisibility by the
three-layer bound exactly. The large-time conclusion rests on these written
arguments, not enumeration of P ticks.

An exact causal enumeration gives three W arrivals on the R-1 initializing
slice and none on R-2, at the positions printed by the author. The reduced
queries F0(176), F1(175), F2(174) are correct. A useful benign detail is that
the third entry is actually zero for both x values in this candidate;
its isolated-origin first-front value is also zero after Lucas parity.
Removing only that correction therefore changes no q10 rows. It cannot be
used as a nonvacuous omission control. Removing all coupled W corrections
instead changes 416 of the 512 q10 rows. The independent grid explicitly
checks the third entry rather than inferring it from that mutant.

The source/readiness change is stated correctly. N is an original-time
current source at distance L+1 from q10, L+2 from q9 and L+3 from q8.
It lies outside all 24 earlier ready regions and overwrites no compiled
source. All 1,479 retained compiled positions lie on or outside the new
q10 boundary, with their exceptions retained. The new cone explicitly
replaces the optional F10 uniform factor; it preserves F8 outside the cone.
Consequently the older 64-value pool theorem cannot simply be reused.

For each of the eight old public-bank rays, the reviewer minimizes its
Manhattan distance over the entire integer time interval by clamping the
single varying-coordinate zero to the interval. Every minimum is strictly
outside the new ready ball, with minimum slack one. This is an interval
argument, not a sample of an astronomical bank. N cannot reach an existing
public port by L. The upper/lower effective front centers remain separated
by at least 2R, and the retained torus is large enough for these source and
horizon envelopes. At the pre-collision boundary the old lower waves are
only at their first fronts; their pure-B inputs share the same H phase,
while the exceptional origin/W interaction is handled by the coupled grid.

Blanking a larger initial region may change the pointwise background of
late public noise. It preserves the inherited chronological-bijection law
conditional on the changed complement because no reserved fair bank triple
is overwritten. The author makes this distinction correctly. No new whole
q10 public-prefix/flag law is established by these geometry checks.

## Controller exclusions and the lost-input branch

The independently reconstructed table gives a permutation of all eight q10
values for every one of the 64 fixed old contexts when N varies. The new
source is genuinely transported; a negative result is not caused by a dead
new control or by replacing the native rule with H of q9 alone.

Both declared affine source families were re-enumerated from the new table:
64 controls without the u XOR a term and 512 with it. Neither has a common
injective s code at each fresh c. The registered clean/mixer/paired targets
all require such an injective code and therefore have no survivor either.
This is a finite result for those specified original-time controls.

The pad-aware extension is sound and its source limitation is explicit.
For each of the 24 known contexts (u,mY,mR,a,b) on accepted old masks,
form the eight held-N pairs of raw q10 values for s=0,1, omitting equal
pairs. A controller depending only on that context and new independent
seeds needs a common ordered pair for a common pointwise raw code. The
intersection sizes begin 8,8,0 and stay zero. The author consequently does
not need to claim an affine-realizability solution for a surviving pair.
An empty common-label intersection alone would not exclude every redundant
decoder; the stronger next observation does.

On accepted u=0,a=b=1, all four pad choices give the same full N permutation

    [4,2,1,0,3,5,6,7]

for both unknown signs. All 32 held-pad/N pairs were re-derived from the
independent native engine. Any N chosen from known context and independent
new resources has the same q10 law for both signs on this branch. Thus a
decoder of current q10 alone cannot recover both different s values, even
if redundant raw labels or nonlinear known-seed N functions are allowed.
The premise that N does not initially copy unknown x/s is essential. This
argument concerns a single seeded current-port adapter, not all possible
physical computation after the unknown sign arrives.

The actual previous q9 triples remain different and retain s. The global
native state has not erased the unknown sign, so a distributed two-slice
code, another port or a later native gate is not excluded. In particular
this is not a full-boundary operational inequivalence or an OI-wide no-go.

The other mechanistic identities also match: 192 accepted unknown-sign
pairs have q10.A(s=0) XOR q10.A(s=1)=u. On mask10, all 64 held-N mR-toggle
pairs flip q10.B. There are 144 pad-sensitive diagnostic rows, 80 on accepted
old masks. The example with identical selected q9=010 and q10 values
001,011,001,011 is correct. Those pad variants have not been shown to have
the same complete earlier public record; informative ciphertexts can differ.
The report correctly calls this selected-boundary response dependence.

## Verification and verdict boundary

Every review control passes with explicit exceptions retained under Python
optimization. Normal and optimized review executions are byte-identical.
The five curated review files are REPORT.md, checks.py, result.json,
INPUT-HASHES.json and SHA256SUMS. The checker accepts the retained native
source root and author root as explicit CLI arguments and has defaults for
both this workspace and its intended nested published location.

The new physical q10 table, source modification, period arguments and
single-port controller exclusions are accepted within their stated scope.
The scope includes the exceptional mask01 raw rows but does not supply a
new joint quantum instrument/failure law: no native predicate, public flag,
reusable output interface or late whole-port access law is constructed.
The old joint public-bank theorem remains an inherited premise. No A1
coverage, A2 protocol error guarantee, composite result, physical premise
adoption, F/E designation, dispatch, merge or #885 edit follows.

Replay locally with:

    python3 checks.py --source-root /path/to/retained/native/root --author-root /path/to/native_seed_v12
    python3 -O checks.py --source-root /path/to/retained/native/root --author-root /path/to/native_seed_v12

Each output must match result.json exactly. Written universal/large-time
arguments were reviewed separately from the bounded computations. Neither
the finite controls nor this internal review are Lean or host attestations.
