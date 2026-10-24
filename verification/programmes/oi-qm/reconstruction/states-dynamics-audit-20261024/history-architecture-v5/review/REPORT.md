# Separate-author review of the continuous positive qubit interface

Author checkpoint: `51d8956100cf76d24b6810f1853c9f714f596c35`,
`history-architecture-v5/` on #911. **Accept within the stated scope;
no blocking findings.** The result is a credited known single-qubit
projective/unitary model with supplied operations, preparation laws,
continuum resources and access restrictions. It is not native availability,
probability selection, full POVM/instrument coverage or a composite/A1
reconstruction. This is separate-agent internal review, not external
validation or formal certification.

The reviewer directly checked the primary Ruebeck–Lillystone–Emerson paper,
sections 2.3 and 4.1.1 Eq.16. It explicitly supplies the sphere density,
rotations, hemisphere responses and measured-state re-preparation, crediting
Kochen and Specker. The author correctly claims a positive architecture
control, not novelty for that model. Primary source:
<https://arxiv.org/html/1812.08218v3>.

## Cone, fixed decoder and the integral

For the pure density `(n dot lambda)_+/pi`, choose n as the polar axis.
Integrating the area element `dphi dc` over c from 0 to 1 gives normalization
`2 integral c dc=1`. The first moment along n is
`2 integral c^2 dc=2/3`, with transverse moments zero by symmetry. Thus
the fixed decoder mass and `(3/2)`first moment sends mu_n to the pure
qubit operator with Bloch vector n.

On the specified cone of finite nonnegative mixtures, the decoded vector
is `r=sum w_i*n_i`, with mass `w=sum w_i`. The triangle inequality gives
`norm(r)<=w`, proving positivity and mass preservation. Conversely any
positive qubit operator is covered by a mixture of at most two antipodal
pure densities with weights `(w+norm(r))/2` and `(w-norm(r))/2`. The zero
and zero-vector cases cause no singularity. This is exact state coverage
for the supplied cone, not a physical preparation construction.

For any hemisphere H_a, symmetry gives `integral_Ha lambda=pi*a`.
The term `abs(n dot lambda)` is antipodally even, so each hemisphere has
half its full-sphere integral, namely pi. Splitting the positive part into
the linear and absolute-value terms proves

    integral_Ha mu_n = (1+n dot a)/2.

This derivation uses the specified density and response, rather than
assuming a probability table. It does not derive why nature or native OI
selects those ingredients.

The independent checker exercises a different exact integral algorithm
from the author. Rational stereographic coordinates parameterize the
measurement plane as

    (x,z)=((1-t^2)/(1+t^2),2t/(1+t^2)).

After the polar integration the primitive is
`(n_x*t-n_z)/(1+t^2)`. All hemisphere boundaries occur at rational roots
`(n_z+/-1)/n_x`, with the axial cases handled separately. Exact interval
integration uses those roots and the zero limits at both infinities. No
Born expression or author's angular ordering computes this integral.
All 144 tests on rational directions with denominators 13 and 17 agree with
independent matrix traces and the general identity. The same algorithm
checks multi-hemisphere intersections in the access countercontrols.

The decoder is positive only on its declared cone. A point measure is
outside that cone and has decoded Bloch length 3/2. Thus this architecture
does not assert the old pointwise/G3 identification on all positive
classical priors, and it does not contradict the earlier fixed-map
obstruction by simply enlarging the carrier cardinality.

## Operations and arbitrary finite adaptive branches

Every supplied SO(3) rotation is a sphere bijection preserving area. Its
push-forward sends mu_n exactly to mu_(Rn), so it preserves the cone and
intertwines with unitary conjugation. The actual measurement response is
the sign of a dot lambda. The apparatus need not know a preparation label.
Fresh re-preparation gives the linear subnormalized kernel

    K_(a,s)(nu)=nu(H_(s*a))*mu_(s*a).

The integral and rank-one projector identity prove
`D(K_(a,s)(nu))=P_(a,s) D(nu) P_(a,s)`. Both outcomes, including zero
branches, are present; the two masses sum to the input mass. The output
lies in the same cone.

Induct on a finite adaptive tree, with actions common functions of the
already public history. Each rotation and measurement preserves the
decoded quantum branch, so every complete record and its outgoing
subnormalized state agree jointly. The proof covers zero branches without
renormalization and fixed ticks/flags with the declared record contract.
It is an all-finite-depth mathematical theorem for that interface; finite
checker depth is a control, not its proof.

Within the cone, equal decoder values give identical permitted future
records by this induction. Conversely, stopping separates unequal mass,
and some projective direction separates unequal Bloch vectors of equal
mass. Therefore the proposed operational relation is a congruence for the
stated operations. Distinct hidden mixture decompositions can remain
operationally equivalent; preparation noncontextuality is not required.

Independent quaternion and rational complex-matrix controls cover 50
rotation intertwinings and 100 complete projective branches. Two adaptive
policies at depth four check 360 branch nodes and 192 full leaf records,
including zero-mass histories, settings, gates, signs, certain-success flags
and scheduled ticks. The checker imports no author implementation.

## Reset resources and global reversible extension

With preassigned independent initial uniforms U,V, the reset has polar
cosine `c=sqrt(U)` and uniform azimuth. Since `dU=2c dc`, its area density
is `c/pi`, exactly the required hemisphere preparation. The fixed tangent
frame may be merely measurable. No global smooth frame is needed.

The claimed global reversible dilation is valid on the full register
space, not just the ready slice. Its second output retains old lambda.
That value, unchanged seeds and the chosen setting recompute the sign,
sample g and rotation Q_g. Applying Q_g transpose recovers the arbitrary
old blank register, and XORing the sign bit again recovers its arbitrary
old record value. The Householder construction sends e_z to g with
determinant +1; its exceptional e_z case is separately defined. This proves
bijectivity, including equatorial ties under the fixed convention.

The new checker verifies 448 reset sample geometries, properness and
orthogonality of their transfers, and 3,584 full inverse cases with nonblank
auxiliary registers and either record bit. It also includes the exceptional
poles. Finite sample geometries do not certify a continuum sampling law;
the density transformation above supplies that proof.

For each finite horizon, all unused continuum pairs and blank registers
are provided initially. Freshness after the public past follows because
earlier kernels do not use them. Retained old carriers and used seeds
remain private and cannot return-couple to future allowed carrier
operations. A native realization must establish that isolation physically;
privacy of direct reads alone is insufficient. The fixed scheduled clock
and single public sign pointer are supplied interface features, not a
derived native whole-triple port or physical operation-time bound.

## Non-Clifford witness and restriction controls

The stated two-pole preparations have Bloch vectors
`r_+=(2/3,-2/3,0)` and its negative. The rational rotation with first row
`(3/5,-4/5,0)` gives X expectation 14/15 and hence the exact 29/30 versus 1/30
record laws, with the appropriate X-eigenstate on each outgoing branch.
The new encoding passes the old operation test with one common rotation.

Its source distinguishability also changes. The antipodal difference is
`(r_+ dot lambda)/pi`; integrating its absolute value gives ontic
TV=`2sqrt(2)/3`. Its square 8/9 exceeds the target record-TV square by 4/225.
This respects classical data processing and leaves the old product-prior
bound intact.

The independent exact intersection integral confirms that eta_z and eta_x
both decode to I/2 but, without reset, yield respectively
`(9,1,1,9)/20` and `(7,3,3,7)/20` for the stated two reads: TV 1/5. Correct
fresh reset restores the common first law. Reading retained old workspace
recreates the gap. Hidden-Z-dependent timing likewise gives a full-record
gap of one despite identical X-sign marginals.

Exposed reset seeds give a point law with decoder determinant -5/16. Even
the single flag `U>4/9` has probability 5/9, conditional polar mean 38/45,
decoded Bloch length 19/15 and determinant -34/225. This is failure of the
fixed cone/decoder under changed access. It does not invalidate the private
reset or rule out every possible extended decoder.

These controls confirm that reset, fresh resources, memory isolation,
private seeds and fixed timing are load-bearing. The model credits and
supplies them honestly. Native lattice preparation, primitive availability,
their physical probability selection, general POVMs/instruments and
ancillary/composite/Bell structure remain open; full A1 or an A2 finite
resource/error theorem does not follow.

## Replay

Run `python3 checks.py` and `python3 -O checks.py`; both equal result.json.
An optional `--author-root` selects the immutable author module in a sparse
checkout. INPUT-HASHES.json pins its six curated files and identifies the
primary literature review. Runtime checks need no author imports or
network. SHA256SUMS covers the five review files; explicit exceptions
remain active in optimized Python. No author file was edited.
