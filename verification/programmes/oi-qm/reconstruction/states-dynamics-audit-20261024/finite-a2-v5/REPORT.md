# Finite geometric A2 controller with a full record/state bound

Research continuation for #911 from
`088af1453efc7780187bc81f8f765f5005b91870`. This is a constructive finite
approximation of a supplied single-qubit sphere interface. It is not a
native OI implementation, selection of the sphere prior, physical clock or
access derivation, composite-system model, or full A1/A2 reconstruction.

## Result

For a fixed finite rational menu of qubit rotations and rank-one projective
measurements, a fixed finite preparation menu, and at most h adaptive
operations, the controller below has a finite carrier and a finite initially
supplied fair-bit bank. It uses one common geometric response function,
not the unknown preparation label or a table of quantum protocol answers.
Policies are deterministic functions of the public history. Independent
randomized policies inherit the bound by convex mixing, with their extra
initial random resources counted separately.

With N=6M^2, M even and at least8, W>=4, B>=1, put

    eta=(N-1)/2^B,
    e=99/M+16/2^W+2eta,
    alpha=1/(2/3+e),
    kappa=52/M+8/2^W+eta,
    chi=e/(2/3+e).

The fixed decoder is positive on the stated preparation/reset/rotation cone.
For every allowed adaptive protocol, its complete public record and decoded
outgoing qubit state differ from the quantum protocol starting at the decoded
input by classical-quantum trace distance at most

    min(1, h*kappa+2chi)
      <= min(1, (52h+300)/M+(8h+48)/2^W+(h+6)eta).

The smaller bound h*kappa+chi compares to the associated ideal sphere
preparation instead of the exact decoded input. These are different input
comparisons. The main resource certificates cover the single fixed-decoder
input/output comparison.

All randomness can be supplied initially in (h+1)B bits, plus any explicitly
required dyadic preparation-mixture bits. This bit count excludes the large
deterministic controller tables, carrier and retained workspace. The universal
constants are conservative: the concrete certified examples have hundreds
of millions or more grid labels. No efficiency or practical implementation
claim follows.

## Supplied sphere interface and literature boundary

The continuous model uses lambda in S^2, pure preparation density
mu_n(lambda)=(n dot lambda)_+/pi, response sign(a dot lambda), rotations
lambda->R lambda, and an independent fresh preparation mu_(s a) after
the projective outcome s. This is the known qubit Kochen-Specker model;
Ruebeck, Lillystone and Emerson, arXiv:1812.08218v3, section4.1.1 equation16,
give this preparation/transformation/read/update contract. No novelty for
that model is claimed. Architecture_v5 separately audits its exact record
and outgoing-state law. The finite construction and bounds here are derived
directly below.

For completeness, its measurement probability follows without fitting a
threshold: write (n dot lambda)_+=(n dot lambda+|n dot lambda|)/2.
The hemisphere integral of the linear term is pi*n dot a; evenness gives
half of the whole |n dot lambda| integral for the second term. Thus the
probability is (1+n dot a)/2. Its first moment is 2n/3. Mixtures and fresh
rank-one resets give the usual finite adaptive qubit projective law.
The choice of this density, response, rotations and reset is supplied.

## A finite geometric carrier and common controller

Partition S^2 into the six radial images of the cube faces. On each face
use p=(+/-1,u,v), with the corresponding coordinate permutation, and
lambda=p/||p||, -1<=u,v<=1. Face boundaries have zero area. The radial area
Jacobian is (1+u^2+v^2)^(-3/2), so

    mu_n(lambda) dOmega
       = g_n(u,v) du dv / pi,
    g_n(u,v)=(n dot p)_+/(1+u^2+v^2)^2.

This cancellation is useful: g_n is rational at rational midpoints for
rational n. No numerical pi or trigonometric integration is needed in the
finite controller.

Take an M-by-M midpoint grid on each face. There are N=6M^2 labels i,
with p_i=z_i/M for integer z_i, and normalized midpoint lambda_i=z_i/||z_i||.
For each allowed pure preparation/reset direction n, give label i the
integer weight

    I_n(i)=floor(2^W g_n(p_i)).

Normalize these weights, and round their cumulative probabilities down to
multiples of 2^-B. A uniform B-bit integer selects a label by this CDF.
Opposite directions use antipodal CDF ordering: sampling -n mirrors the
sample for n. This keeps the exact mean of antipodal mixtures zero without
changing the approximation bound. We denote the resulting law by nu_n.

Every normalization is positive on the theorem's whole parameter domain.
Choose a component with |n_f|>1/2, its aligned cube face, and a central
midpoint u,v=+/-1/M aligned with the other component signs. Its dot product
with n is>1/2 and (1+u^2+v^2)^2<2 for M>=8. Therefore g_n>1/4 and W>=4
gives a nonzero integer weight. A claim for arbitrarily small W is not made.

The current finite carrier is (i,w), where w is a word of at most h known
rotation generators. A unitary appends its generator, and R_w is its exact
rational rotation matrix. The measurement response is

    s=+1 if a dot R_w z_i >=0, and s=-1 otherwise.

The zero convention is fixed. Its atoms are included in the error band,
not discarded. The controller uses the actual index, stored word and known
setting. It does not consult an external unknown-preparation label. On a
measurement it draws a fresh index from nu_(s a) and sets the current word
empty. Keeping exact words avoids per-unitary geometric rounding drift.

Preparation may use its known preparation instruction n to compile the
source table. After the carrier is offered, every retained preparation
label, source seed and spent workspace is private and has no permitted
return coupling. Public measurements of those registers change the model.

## Cell, sampling and hemisphere bounds

Let r=||p||. Where n dot p is positive,

    partial_u g_n=n_u/r^4-4u(n dot p)/r^6.

Since |n_u|<=1, |n dot p|<=r, r>=1 and r^5>=1+u^2>=2|u|,
the absolute derivative is at most3. The same holds for v; continuity of
the positive-part function extends this Lipschitz bound across its crease.
Each midpoint differs from its cell points by at most1/M per coordinate.
Thus the total unnormalized cell-integration L1 error over face area24 is
at most144/M. Integer flooring adds at most24/2^W after multiplication by
the cell area4/M^2.

This proof compares rounded weights directly with the true cell integrals,
not with a separately normalized midpoint rule. Write the rounded cell
weights as q_i, true unnormalized integrals as J_i, their sums S>0 and pi,
and E=sum|q_i-J_i|. Then

    sum|q_i/S-J_i/pi| <= (E+|S-pi|)/pi <= 2E/pi.

Since pi>3, normalized cell TV is at most48/M+8/2^W. This argument needs
S>0, already proved, and does not assume an unproved lower bound S>=3.
Rounding the CDF contributes at most eta=(N-1)/2^B in TV, by telescoping
the cumulative rounding errors. Hence the sampled finite cell law can be
coupled to the ideal sphere preparation with mismatch probability at most

    tau=48/M+8/2^W+eta.

On a matching cell the normalized midpoint is within2/M of its sphere
point: radial normalization on each face is1-Lipschitz and the midpoint
coordinate distance is at most sqrt(2)/M. Exact rotations preserve this
distance. A hemisphere response can disagree only in the band
|a dot lambda|<=2/M. For every mu_n, and therefore every positive mixture,
that antipodally symmetric band's probability is at most4/M. Indeed its
area is4pi*delta for band width delta, and antipodal symmetry replaces
(n dot lambda)_+ by |n dot lambda|/2, yielding probability<=2delta.
Thus a single read differs with probability at most kappa=tau+4/M.

Total variation between an atomic ontic measure and a continuous density
is1. It is not the approximation metric here. The cell coupling and the
operational record/state metric are explicit alternatives.

## Fixed positive decoder

To make its entries rational, set

    ell_i=z_i/ceil(sqrt(z_i dot z_i)).

The denominator is at least M. These points have norm at most1 and are
within1/M of lambda_i. On a matched cell their error from the ideal sphere
point is therefore at most3/M. On a mismatched cell use the distance bound2.
For nu_n, after any allowed exact rotation word,

    || E[R_w ell_i]-(2/3)R_w n || <=3/M+2tau=e.

Use the single linear decoder

    D(mu)=(mass(mu) I+alpha E_mu[R_w ell_i] dot sigma)/2,
    alpha=1/(2/3+e).

For every normalized canonical preparation/reset ray and its rotations,
the decoded Bloch norm is at most alpha(2/3+e)=1. Positive mixtures preserve
positivity, and mass is preserved. These rays generate the admissible cone.
After completed measurement instruments the fresh reset returns a canonical
ray; rotations preserve its form while word capacity remains. Hence the
declared cone is closed at the permitted completed-instrument cuts.

Compared with its associated ideal state R_w n, the decoded Bloch error is
at most2alpha*e, giving qubit trace-distance error at most chi=alpha*e.
The factor is fixed by the proved bound; it is not fitted to measured data.
The unshrunk3/2 moment map is not assumed positive after arbitrary rounding
or conditioning on a private atom. Positivity at an exposed pre-reset
partial-read cut is also not claimed.

## Adaptive complete record and outgoing-state law

For a normalized initial positive mixture of canonical rays, fix the same
adaptive public controller in the source and reference. Between projective
reads exact stored rotations preserve the geometric coupling. At a read,
record disagreement probability is at most kappa. After each read the
source draws nu_(s a) from a fresh block independent of the earlier carrier
and history; the ideal comparison draws mu_(s a). This gives

    TV(source complete record, ideal complete record)<=min(1,h*kappa).

The outgoing-state argument is separate from conditioning an ontic coupling
on matching records. Given any complete public history, the last fresh reset
makes the source's current normalized law a rotated nu_(s a), independent
of the older history. Its ideal conditional outgoing state is the same
rotated eigenstate. The fixed decoded state is therefore within chi on
that history. If no read occurred, the initial-mixture bound applies.

For branch masses p_r,q_r and conditional density operators A_r,B_r,

    (1/2)||p_r A_r-q_r B_r||_1
        <= |p_r-q_r|/2+min(p_r,q_r)D_tr(A_r,B_r).

Summing gives joint classical-record/quantum-state trace distance at most
h*kappa+chi. A zero-mass branch contributes its actual subnormalized
operator without normalization. Early stops retain the state and use the
same absorbing public padding through h. Success flags are always1 for the
properly provisioned source and reference; no failure is postselected.

The initial decoded state is itself within chi of its associated ideal
preparation. The entire adaptive quantum protocol is a trace-preserving
quantum channel to the final record/state system and contracts trace
distance. A triangle inequality therefore gives the fixed-decoder operation
bound h*kappa+2chi stated first. The source controller never needs a
decomposition label for this proof. The bound holds for every admissible
source measure and any generating-mixture decomposition.

An existing terminal-failure sector may be adjoined identically on both
sides; it contributes zero error. The offered-carrier sector gets its
actual mass times the bound. This observation supplies no native flag or
failure-reset implementation.

## Explicit resources, timing and information retention

For any epsilon in(0,1], choose even M>=max(8,3(52h+300)/epsilon), and

    W>=max(4, ceil(log2(3(8h+48)/epsilon))),
    B>=max(1, ceil(log2(3(N-1)(h+6)/epsilon))).

Each of the three terms in the fixed-decoder upper bound is then at most
epsilon/3. The finite evaluator checks these inequalities exactly without
materializing the huge certified grids. For h=3 and epsilon=1/10 it gives
M=13680, W=12, B=39: N=1,122,854,400 grid labels and156 initially supplied
fair bits, plus any mixture-label bits. The bounded numerical certificate is
below1/10. This is a deliberately loose existence/resource bound, not an
efficient or practical recipe. The exact large grid is not executed locally.

For g declared rotation generators, at most

    L_carrier=N sum_(j=0)^h g^j

current labels suffice. Their binary width is ceil(log2 L_carrier), with
a separately declared finite clock. Preparation uses one B-bit block and
each operation slot reserves one more, even if unused by a unitary or stop.
This fixed allocation preserves conditional freshness under adaptive choices.
An explicit forgotten dyadic preparation mixture has its own initial bits.
Arbitrary non-dyadic mixture weights need their own sampling resource and
are not included in this fair-bank count.

The deterministic controller also costs memory and time. CDF tables for f
preparation instructions and the2a reset directions use at most
(f+2a)N(B+1) bits of cut data, and hemisphere response tables can use at most
a*L_carrier bits. These very large description costs are not hidden in the
fair-bit number. They are computed from the geometric formulas, not quantum
protocol-output tables. Exact rational word matrices and signs provide a
finite algorithm for producing them.

Each finite table/word/sign map can be implemented by a fixed-width finite
Boolean circuit. A full scan instead of an early-exit search, and padding
each operation slot to the maximum declared circuit schedule, makes the
public completion tick independent of the hidden label and seed. The
Python checker is a mathematical evaluator, not a constant-time hardware
implementation. This is a supplied/padded finite classical clock contract,
not a native lattice clock or gate-availability proof.

All current-state information can be retained reversibly. For a deterministic
step function F_a(lambda,z) and record bit G_a(lambda), use fresh blank
output/record registers and the map

    (lambda,b,z,c) ->
      (b XOR F_a(lambda,z), lambda, z, c XOR G_a(lambda)).

The retained lambda,z recover b,c, so this is globally bijective after a
total extension to unused binary labels. No current state or seed is erased.
At most h old carrier labels and all seeds are retained as private workspace;
they have no permitted return coupling. This is a generic finite reversible
dilation, not the native H update. Exposing it changes the access contract.

## Exact controls and limitations

The standard-library checker uses rational grid weights, integer CDFs and
response signs. Independent rational complex matrices implement H, quarter-Z
and diag(2-i,2+i)/sqrt(5), checking the non-Clifford rotation with first row
(3/5,-4/5,0). Its adaptive tests include Pauli axes, the(3/5,4/5,0) axis,
and mixed inputs +/-(2/3,-2/3,0) prepared as explicit dyadic mixtures of
rational pure directions.

On M=8,16 the conservative universal bounds are often vacuous after clipping
at1. These finite smoke tests validate kernels, branch bookkeeping, decoder
positivity and exact resource logic; they do not establish the asymptotic
bound by extrapolation. That bound rests on the preceding proofs and exact
nonvacuous symbolic parameter certificates.

There are128 adaptive cases,1,248 nodes,672 complete leaf records and368
retained zero-mass nodes, covering both input comparisons. All64 independent
matrix controls and16 inverse-word controls pass. All1,024 seeds of a small
CDF are exhausted and agree with an independent fixed full-scan sampler.
The decoded source/reference CQ distances are enclosed by certified rational
square-root intervals rather than floating-point eigenvalues.

Reusing a preparation seed for reset changes the next two-record law by
TV11/256. Ignoring an adaptive axis choice changes it by153/1024. An
insufficient final block produces terminal-failure mass1/2 in the specified
continuing branch. Exposing a private carrier or a hidden-dependent timing
label distinguishes antipodal-mixture preparations with the same decoded
maximally mixed state. These controls detect changed laws/contracts; they
are not claimed to exceed the loose clipped smoke-grid upper bound.

Normal and optimized runs reproduce result.json byte for byte. No empirical
result, Lean certificate, full repository gate or exact-head CI attestation
is claimed. The construction is conditional A2 reproduction for the stated
single-qubit projective/unitary finite-menu/horizon class. It supplies no
generalized instrument, composite/Bell structure, native read/reset or
selection principle for the geometric prior. Its larger encoding and
bounded word memory differ from the preceding eight-sign model; the earlier
scoped1/15 and2/15 obstructions remain valid under their own contracts.

Replay from this directory: `python3 checks.py` and `python3 -O checks.py`.
Only six curated files are part of this author checkpoint. Source/evidence
remain off-main research provenance until any dependent enduring claim lands
with its required evidence under AGENTS sectionA.42.
