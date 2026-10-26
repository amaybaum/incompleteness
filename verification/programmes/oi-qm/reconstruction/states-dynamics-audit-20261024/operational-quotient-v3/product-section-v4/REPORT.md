# Product preparations do not remove the fixed-map operation obstruction

Research follow-up for #911, 24 October 2026. The predecessor's author
checkpoint is `fb0f799d94b621cdb82a8e06183f07afc070f14c` under
`operational-quotient-v3/`. This follow-up leaves its files unchanged.
No preparation rule, operational map, physical premise or access restriction
is adopted. This is an abstract eight-sign representation diagnostic, not
a native OI construction or a general OI/A2 no-go.

## Result

Replacing the preceding full preparation fibres by the canonical product
section does not escape the positive-kernel obstruction for the same fixed
first-moment decoder. Eight allowed product priors already span the whole
eight-dimensional hidden measure space. A single stochastic continuation
that implements a Bloch rotation on every product prior must therefore
intertwine that rotation on all hidden vectors. Cube preservation again
restricts its unitary Bloch rotations to signed permutations, with 24 proper
Clifford actions. Physical mixture closure is not needed for this conclusion.

A second exact control gives a direct record approximation bound. For
product priors with Bloch vectors r+=(2/3,-2/3,0) and r-=-r+, the source
ontic TV is 2/3, while the target rational rotation followed by X read has
record TV 14/15. Any fixed classical continuation with independent apparatus
therefore has worst error at least 2/15 on this pair. The ordinary X sign
read attains the bound for this binary-record pair. This is not a full-channel
minimax theorem. It permits arbitrary output-state geometry and additional
classical output memory.

## Changed preparation contract

Keep hidden Omega={-1,+1}^3 and the same fixed moment map

    D(p)=(I+E_p(x)sigma_x+E_p(y)sigma_y+E_p(z)sigma_z)/2.

The proposed canonical preparation for a Bloch vector r is

    p_r(lambda)=product_(a=x,y,z)(1+r_a lambda_a)/8,
    ||r||_2<=1.

These priors are positive, normalized and have first moments r. Thus the
product section represents every Bloch state. Unlike the predecessor's
P_oct, it includes states whose l1 norm exceeds one. The map is a supplied
preparation prescription; no native preparation availability is asserted.

The continuation under test is one stochastic kernel independent of the
unknown preparation label. It may include initialized classical apparatus,
private random resources, adaptive classical computation and discarded
workspace, provided their initial law and controller do not depend on which
unknown input preparation was used. Such a process induces a common Markov
kernel from the input hidden carrier to its final public record. Any raw
metadata must also satisfy that kernel contract. No herald is introduced
or postselected in this test.

## Eight finite product priors suffice

Let a=1/3 and select the eight product priors with r=a*s for every sign
vector s in {-1,+1}^3. All atoms are strictly positive (minimum 1/27), and
every input has squared Bloch norm 1/3. Let M have these distributions as
its columns in consistent sign order. It is the threefold tensor product
of the two-by-two stochastic matrix

    [[(1+a)/2,(1-a)/2],[(1-a)/2,(1+a)/2]].

The two eigenvalues of the one-coordinate matrix are 1 and a. Consequently
M is invertible, with determinant a^12=1/531441. Equivalently, the Fourier
moment of each character chi_S on p_(a*s) is a^|S| chi_S(s); the Walsh basis
is invertible and every a^|S| is nonzero. The checker independently measures
rank eight by rational elimination and all 64 Fourier moments.

Let A be the three-by-eight sign matrix. If a fixed stochastic kernel T
satisfies A T p_r=R r for every product input, then in particular

    (A T-R A) M=0.

Invertibility gives A T=R A. This uses all hidden point priors only as a
linear basis for an operator identity; it does not admit them as physical
preparations. The checker also reconstructs each hidden point vector as
an affine linear combination of the eight allowed product priors. Negative
coefficients are algebraic interpolation weights, not physical mixtures.

For every hidden vertex lambda, A T delta_lambda belongs to the sign cube
[-1,1]^3 because T is stochastic. Therefore R must map the cube into itself.
If R is orthogonal, each row has l2 norm one and l1 norm at most one, forcing
one entry of magnitude one per row. Orthogonality forces distinct columns.
Hence R is a signed permutation; proper rotations give the Clifford group.

In particular,

    R=[[3/5,-4/5,0],[4/5,3/5,0],[0,0,1]]

sends (1,-1,1) to a vector whose first coordinate is 7/5 and cannot have such
a stochastic implementation. This is the same fixed rational rotation as
the predecessor. Its action is checked independently by conjugating density
matrices with diag(2-i,2+i)/sqrt(5), using exact rational complex arithmetic.

The full-fibre assumption of the predecessor was sufficient but stronger
than necessary for this candidate. The natural product-preparation section
already contains enough inputs to force the same operator identity.

## A sharp two-preparation record bound

Choose r+=(2/3,-2/3,0) and r-=-r+. These are valid mixed Bloch states with
squared norm 8/9. Their product priors have atoms, in lexicographic hidden
sign order,

    p+ = (5,5,1,1,25,25,5,5)/72,
    p- = (5,5,25,25,1,1,5,5)/72.

Thus both priors are strictly positive and

    TV(p+,p-)=2/3.

The target R-then-X protocol gives X expectation +/-14/15 and binary laws

    q+=(29/30,1/30),  q-=(1/30,29/30),
    TV(q+,q-)=14/15.

For any common classical continuation kernel, the output record laws a+,a-
have distance at most 2/3 by data processing. If each approximation error is
at most epsilon, the triangle inequality gives

    14/15 <= epsilon+2/3+epsilon,
    epsilon >= 2/15.

The ordinary unrotated X sign read produces (5/6,1/6) and (1/6,5/6), each
exactly 2/15 from its target. All 256 deterministic binary response functions
are independently checked: none exceeds source distinguishability and none
has smaller worst-pair error. General stochastic binary responses obey the
same lower bound by data processing. Therefore the pair bound is sharp.

The proof concerns only the final designated binary record. It survives
allowing all valid Bloch outputs, arbitrary additional classical output
memory and discarded private ancillas. Enlarging the output-state region
cannot restore distinguishability already absent in the input pair. It does
not by itself address a different input encoding or an apparatus correlated
with the unknown preparation.

The predecessor's 1/15 bound and this 2/15 bound use different preparation
pairs and different preparation domains. The present pair is outside P_oct
because ||r+||_1=4/3. Neither number is asserted to be the minimax error of
the full channel, and their comparison is not a global improvement theorem.

## Physical mixtures and the preparation-dependent control

The product section itself is nonconvex. The equal mixture of p+ and p-
has zero first moments, like the uniform p_0, but retains xy correlation
-4/9 instead of zero. If physical forgotten mixtures are admitted, their
closure therefore contains distinct hidden distributions for the same
decoded state. The classical mixture cannot simply be replaced by p_0
without establishing that all future permitted kernels preserve their
operational equivalence. For the Pauli/Clifford/fresh-reset interface of
the predecessor, the moment congruence does provide that equivalence.

Admitting mixture closure cannot remove the current obstruction: the
spanning product preparations and the distinguishability pair are already
present before closure. Conversely, forbidding all mixtures would not
save this particular product-section operation test; it would merely
change another physical preparation assumption.

A positive control exposes the independent-apparatus hypothesis. Supply
an external preparation label and a uniform 30-valued seed. A controller
that knows the label can accept 29 of 30 seeds for r+ and one of 30 for
r-, reproducing the target binary laws exactly. Its enlarged input
distributions, including that label, have TV one rather than 2/3. This is
not a fixed channel on an unknown carrier preparation: the additional label
or preparation-dependent resource law changes the premise. The uniform
30-valued seed is explicitly supplied; it is not claimed to come from an
always-success finite fair-bit sampler or a native source. This control
does not reproduce the full quantum instrument or solve physical sourcing.

The positive Clifford control also remains intact: signed coordinate
permutations map each product prior p_r to p_(Rr), and Pauli-eigenstate
fresh resets return product priors. Thus the negative result is not caused
by rejecting every transformation or by loss of state representability.

## Evidence and next implication

The standalone `checks.py` imports no predecessor checker and uses only
standard-library exact fractions and rational complex matrix operations.
It checks the eight-prior positivity/norm/rank, 64 Fourier moments, eight
affine interpolation identities, ten quantum-matrix rotation cases, the
explicit approximation pair, all 256 binary responses, the nonconvexity
control, 20 Clifford product-closure cases and the preparation-dependent
controller. Normal and optimized outputs must be byte-identical to the
retained `result.json`. Source compilation is checked separately. No Lean
certificate, native simulation, CI attestation or empirical result is claimed.

This settles one obvious proposed escape from the preceding obstruction:
replacing full fibres by the natural product section alone is insufficient
for this decoder and these inputs. A viable next correspondence must change
the input encoding/preparation assignment, the update/resource contract or
another explicit load-bearing assumption, then re-establish actual availability
and the entire full-record continuation law. It cannot silently make the
unknown preparation label a new apparatus input.

The result does not refute OI generally, the native #910 encoding, a different
operational quotient or a separately specified A2 architecture. #885 remains
untouched, and no physical premise, F/E designation, dispatch or merge follows.

## Source boundary

The predecessor `fb0f799d94b621cdb82a8e06183f07afc070f14c` supplies the fixed
eight-sign moment map, standard Clifford positive control and the earlier
full-fibre obstruction. Its standard stabilizer model is prior literature,
credited there to Lillystone, Wallman and Emerson, arXiv:1802.06121v2.
This follow-up supplies the explicit product-section span and pair controls.
All claims here are local mathematical implications of the stated candidate,
not an absence claim about the full manuscript corpus. Off-main evidence
remains research provenance until any dependent enduring claim lands with
its required source and executable evidence on main.
