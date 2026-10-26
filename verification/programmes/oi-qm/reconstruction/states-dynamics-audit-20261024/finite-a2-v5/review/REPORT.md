# Separate-author review of finite geometric A2 v5

Verdict: **ACCEPT WITHIN THE STATED SCOPE**, after the phase/word-budget
clarification in the reviewed forward author revision. No mathematical
blocking findings remain.

Reviewed forward author revision:
`dbfaa3c68003bfd5335353829c18cf6f21d300c4`, #911,
`verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/finite-a2-v5/`.
Its predecessor is `6097379b86f319eaa9b258e920f2eb44dc6401a6`.
The only changes within this module are REPORT.md, PROVENANCE.json and
SHA256SUMS; the checker, result and preregistered plan remain byte-identical.
Author revision and its predecessor are pinned in `INPUT-HASHES.json`.
The immutable remote manifest matches all six local author-file hashes.
This is an internal separate-agent review, not external validation or a
Lean certificate. The review checker is a standalone implementation and
does not import or execute the author checker.

## What the result covers

The construction gives a conservative finite reproduction theorem for a
fixed finite rational menu of rotations/projective measurements, a finite
preparation menu and a fixed finite operation horizon. Its main comparison
uses the same positive fixed decoder on input and output. It proves an
adaptive complete-record/outgoing-qubit bound, not merely accuracy of one
Bernoulli marginal.

It does not source the geometric prior, operation availability, public/private
access or clock from native OI. The encoding is larger than the preceding
eight-sign representation and includes bounded word memory. The prior scoped
1/15 and 2/15 fixed-encoding obstructions are not contradicted. General POVMs,
composites/Bell structure, unrestricted horizons in one bounded apparatus,
physical probability selection and full A1/A2 reconstruction remain outside
the result.

## Geometry, normalized cells and sampling

For a cube face p=(+/-1,u,v), the Gram determinant of the radial derivatives
is (1+u^2+v^2)^(-3). Its area Jacobian is therefore r^-3. Multiplying by the
cosine density (n dot p)_+/(pi*r) yields the stated rational face function
g_n=(n dot p)_+/r^4. The independent checker verifies the Gram identity on
both smoke grids without using the author's grid class.

The coordinate derivative bound is valid. On the positive side of the crease,

    |partial_u g_n| <= r^-4+4|u|/r^5 <= 3,

because r>=1 and r^5>=1+u^2>=2|u|. The same holds for v, and continuity
extends the coordinate Lipschitz bound across the positive-part crease.
Each coordinate differs by at most 1/M from its midpoint. Total face area
24 gives integration L1 error at most 144/M. Flooring the scaled midpoint
weights adds at most 24*2^-W in integral units.

The normalization proof correctly compares the rounded unnormalized weights
directly with true cell integrals. For E=sum|q_i-J_i|, rounded sum S>0 and
true sum pi, the normalized L1 distance is bounded by 2E/pi. Hence TV is
at most 48/M+8*2^-W. No lower bound S>=3 is assumed. Positivity S>0 follows
independently from an aligned central face midpoint and a component
|n_f|>1/2, valid for the stated M,W range.

CDF rounding is also correctly separated. If each interior cumulative
rounding error has magnitude below 2^-B, the sum of absolute differences
of consecutive cumulative errors is at most twice their sum. Thus TV is
at most (N-1)*2^-B. The antipodal sampler convention is a permutation of
both the ideal cell law and finite law; it preserves this bound. It must
be retained when specifying actual seed-to-label maps and the reuse control.

For equal cells, radial normalization has derivative norm at most one along
the face segment, so the point error is at most sqrt(2)/M<2/M. Exact word
rotations preserve that error. The antipodally symmetric width-delta band
has mu_n probability at most 2delta, giving the additional 4/M hemisphere
term, including atoms lying exactly on the finite response boundary. This
supports the stated kappa. Ontic atomic/continuous TV is one; the author
explicitly uses cell coupling and operational CQ distance instead.

## Fixed decoder, cone and state coverage

The integer normalizer ceil(||z_i||) gives rational ell_i of norm at most
one and distance at most 1/M from the normalized midpoint. Together with
cell coupling this yields

    ||E[R_w ell_i]-(2/3)R_w n|| <= 3/M+2tau=e.

The fixed alpha=1/(2/3+e) is chosen from the proved bound. On every canonical
preparation/reset ray and exact word rotation, its Bloch norm is at most one.
Positive mixtures preserve this fact. Its trace-distance error relative to
the associated ideal state is at most chi=alpha*e. This does not establish
positivity on arbitrary ontic atoms or on an exposed intermediate read
before resetting.

The admissible cone and closure are phase-tagged. At public clock t, words
have length at most t and only h-t slots remain. The theorem starts at
clock zero on canonical empty-word preparation mixtures. A measurement
clears its word while advancing the same clock; it does not provide a new
h-step budget. This explicit clarification resolves a possible ambiguity
in the initial author text. It is necessary for the stated finite alphabet
N*sum_(j=0)^h g^j and reserved seed blocks.

For the fixed finite preparation menu, the associated ideal states are
approximated within chi. A fixed finite cone is not claimed to equal the
entire Bloch ball. The written cone theorem allows positive mixtures; the
finite fair-bank source count applies to explicitly sampled dyadic mixtures.
Non-dyadic mixture sampling requires an additional resource, as the author
states. No full state/operation coverage is inferred from finite smoke cases.

## Adaptive full record/state bound

Conditional on each public history, actual fresh reset blocks return the
corresponding canonical finite law nu_(s*a); earlier private seeds do not
return-couple. Rotations are represented by exact words. Therefore the
conditional next-record error is uniformly bounded by kappa, and the total
record TV is at most h*kappa, including adaptive settings, flags, scheduled
ticks, stopping padding and zero-mass branches.

The outgoing-state argument properly uses conditioning on the public
history, not conditioning an ontic coupling on a matching-history event.
After the last reset that conditional source state is a known rotated
canonical ray; its decoder error is at most chi. If no measurement occurred,
the input mixture bound applies. Combining branch mass differences with
conditional trace distances yields h*kappa+chi relative to the associated
ideal preparation.

The adaptive reference quantum protocol is a channel to its final classical
record/qubit output. It contracts the initial chi difference between the
associated ideal preparation and the exact decoded source input. Triangle
inequality therefore gives the principal h*kappa+2chi bound. This extra chi
is required for the fixed-decoder input/output comparison. No preparation
label is consulted by the source read controller.

Finally, 2chi<=3e, so the linear certificate actually has coefficients
52h+297,8h+48,h+6. Replacing 297 by 300 is conservative. The stated M,W,B
choices make the three displayed terms at most epsilon/3 each.

## Finite resources and timing

The (h+1)B fair bits comprise one preparation block and one reserved block
for each possible operation slot. Adaptive skips or early stops do not
permit reuse of already consumed blocks. Dyadic mixture labels and optional
randomized policies need their own initial bits. The fair-bit number does
not count the large deterministic tables or private workspace.

The table counts and finite word alphabet establish finite existence, not
practical efficiency. For h=3,epsilon=1/10 the symbolic certificate uses
M=13680,N=1,122,854,400,W=12,B=39 and 156 fair bits before mixture/control
bits. These huge grids were not executed. The checker independently verifies
the exact nonvacuous inequalities and word-label counts for three parameter
choices without materializing those alphabets.

Finite precomputed sign/CDF maps can be represented by finite Boolean
circuits. Full scans and a fixed worst-case circuit schedule give a public
clock independent of seed/label. This is a mathematical existence of a
padded finite schedule; the Python evaluator is not a constant-time
implementation or a native lattice circuit. Circuit tables, blank registers,
old labels and used seeds remain supplied physical resources. The generic
reversible dilation retains all old information, but does not implement the
native H update or justify extra observer access.

## Independent bounded checks

The standalone review implementation reconstructs both M=8,16 grids,
integer weights, floor and CDF inequalities, antipodal distributions, rational
inward points, geometric Gram identities, response signs and exact words.
It uses independent rational complex projectors/unitaries for finite adaptive
protocols and evaluates the whole CQ distance using certified rational
square-root intervals. Both ideal-input and fixed-decoder-input comparisons
are checked. Small-grid universal bounds can be clipped at one; the report
does not present those smoke tests as asymptotic certification.

The independent reconstruction checks 128 protocol/input comparisons,
1,248 emitted branches and 672 complete leaf records, retaining 280 zero-mass
leaves. The author's 368 zero-mass count is over nodes, a different counter.
The largest independently enclosed CQ upper endpoint exactly equals the
author's retained value. Private carrier and hidden timing reads independently
separate two equal-decoder maximally mixed preparation procedures as claimed.

The independent full-scan sampler exhausts all 1,024 seeds of a small CDF.
Reusing the preparation seed in reset produces the claimed 11/256 two-record
gap. Ignoring the adaptive setting produces 153/1024. Insufficient final
provisioning has terminal failure mass 1/2 in the specified continuation.
These are controls for changed contracts, not claims that mutants exceed
the conservative clipped small-grid bound.

Normal and optimized outputs match the retained review result byte for byte,
and the source compiles. No author engine is imported or executed. The review
accepts the written conservative construction and its stated bounds with
their finite-menu, finite-horizon, supplied-prior/access/timing limitations.
It does not establish native sourcing, Emergence, practical efficiency,
full A1 availability or a composite/general-instrument theory.
