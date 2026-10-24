# A calibration bridge and a limit of the selected twelve-code carrier

Research integration diagnostic, 24 October 2026. The calibrated post-X
target and post-Y measure used by the native programme are exactly the
corresponding sign-code projections of the credited sphere model. Their shared finite code nevertheless discards
information needed by a broader measurement direction.

The post-X measure is a supplied target for the current continuation; its
physical native acceptance gate is still unimplemented. This calculation
compares distributions and does not assert construction of that instrument.

The exclusion below assumes an autonomous common twelve-code interface and
one continuation with a common independent apparatus. It does not apply
automatically to the actual native phase, which also retains previous
slices, workspace, phase/clock tags and history correlations. No such
information is discarded from the native candidate by this calculation.

## Fixed sign projection and exact calibrated measures

Let lambda lie on the sphere and let bit0 mean a positive sign. Project to

    X=signbit(lambda_x), Y=signbit(lambda_y),
    R=signbit((4lambda_x+3lambda_y)/5), Z=signbit(lambda_z).

Ignoring measure-zero boundaries, R=X whenever X=Y. The resulting set has
six plane codes and two Z signs, hence twelve codes. This defines the
coarse map; it does not assert an underlying sphere in the native lattice.

For sphere preparation mu_x=(lambda_x)_+/pi, X is positive with certainty.
The allowed plane codes are000,010,011. The already independently proved
hemisphere law gives P(Y=+)=1/2 and P(R=+)=9/10, so their masses are

    000:1/2, 010:2/5, 011:1/10.

Reflection lambda_z->-lambda_z preserves the density and each plane cell.
Thus Z is fair jointly with the plane code. These are exactly the full
native post-X weights5:4:1 with fair Z, not merely matching moments.

For mu_y, the allowed plane codes000,100,101 have masses

    000:1/2, 100:3/10, 101:1/5,

because P(X=+)=1/2 and P(R=+)=4/5. Again Z is jointly fair. These are the
native post-Y5:3:2 weights. Antipodal reflection gives both negative-sign
preparations. No claim is made here about the full native post-Z measure
or an arbitrary native preparation/operation lift.

The checker derives the plane masses independently by exact linear equations
for normalization and the two hemisphere marginals, then compares the whole
twelve-code distributions with the native mask constructions. Sixteen
direct rational complex-matrix projector comparisons check the original
X,Y,R,Z menu on all four X/Y eigenstate preparations.

## A broader read needs more than these selected signs

Place the +X and +Y code measures at one common abstract carrier interface.
Their only shared cells are000 with Z=0 or1, each with mass1/4 in both.
Their classical total variation is therefore

    TV(p_X,p_Y)=1/2.

Consider the same rational direction used by the earlier non-Clifford test,

    a=(3/5,-4/5,0).

The ideal plus-record probabilities on the two quantum preparations are
4/5 and1/10, giving record TV7/10. Direct multiplication of projectors and
density matrices checks these values independently of the finite response
calculation. The hemisphere integral of the continuous model gives the
same answer.

Any common stochastic continuation on the selected code, including the
same independent apparatus or private random resources, contracts TV.
If its two record errors are bounded by epsilon, triangle inequality gives

    7/10 <= epsilon+1/2+epsilon,
    epsilon >=1/10.

This bound concerns this explicit pair and read under this fixed common-code
contract. It is not a minimax result for the full channel or OI generally.
Adding final metadata or an outgoing state cannot repair the designated
record discrepancy. Input-dependent extra resources change the premise.

The binary-record pair bound is sharp for stochastic responses. Output plus
with probability2/5 on the shared000 cells, with probability1 on the +X-only
cells, and0 on the +Y-only cells. This gives probabilities7/10 and1/5,
each exactly1/10 from its target. A uniform five-valued independent apparatus
realizes that response, retaining the input and seed with a reversible
record-XOR map. That apparatus is supplied for this mathematical tightness
control; an exact always-success finite fair-bit implementation or a native
gate is not claimed.

All4096 deterministic Boolean responses on twelve codes independently obey
contraction. Their best worst-pair error is3/20. That distinct deterministic
number is not substituted for the stochastic1/10 bound.

## Where the missing information resides in the geometric comparison

The two sphere points

    (6/7,2/7,3/7), (2/3,2/3,1/3)

are unit vectors with the same0000 code. Their dot products with a have
opposite strict signs. Open neighborhoods of the points share that property,
so the loss is not confined to a zero-measure boundary. The new read splits
an old sign cell.

For any two pure sphere preparations n,m, the sign of
(n dot lambda)_+-(m dot lambda)_+ agrees with (n-m) dot lambda wherever
the difference is nonzero. The hemisphere in direction(n-m)/||n-m||
therefore attains their classical TV. Applying the hemisphere law gives

    TV(mu_n,mu_m)=||n-m||/2.

For +X and +Y this is1/sqrt(2), whose square1/2 exceeds the target record-TV
square49/100. The full sphere model can make the new read; the selected
twelve-code projection has reduced the source distinguishability. This
explains the relation between the finite native calibration and the broader
architecture without declaring their complete states interchangeable.

An additional preparation label gives the joint code/label input TV1.
A controller using that label can reproduce the target probabilities with
a ten-valued seed. This is a countercontrol to the common-apparatus/input
hypothesis, not a legitimate channel on an unknown autonomous code alone.
The actual native phase may carry response-relevant preparation information
in legitimate physical registers; those registers must be included before
applying any bound. Different public histories or phase tags can also change
the full input distinguishability. Same selected code is not same full input.

## Consequence for the three paths

The native5:4:1 and5:3:2 targets are consistent with the geometric qubit
model on these preparations. To extend beyond the restricted menu, however,
one cannot simply identify these twelve selected signs with the entire
autonomous qubit state. A construction must make additional response-relevant
physical information available, enlarge/change the encoding, or explicitly
state another input/operation contract. Native A's retained two-slice
boundary and the larger A2 encoding are not excluded by this common-code
test; their actual bridge and availability still require proof.

The standalone checker uses exact fractions, an independent matrix projector
calculation, finite exhaustive responses, explicit retained-resource controls
and two geometric cell witnesses. Normal and optimized output must reproduce
result.json. General data-processing and sphere statements rest on the written
proofs; no astronomical native replay or formal certification is claimed.

Sources and immutable pins are recorded in PROVENANCE.json. This is a
conditional design constraint and a calibration bridge, not a failed full
native construction, physical premise, source of the cosine prior, general
A1/A2 no-go or composite reconstruction. #885 remains read-only; no merge,
dispatch or F/E designation follows.
