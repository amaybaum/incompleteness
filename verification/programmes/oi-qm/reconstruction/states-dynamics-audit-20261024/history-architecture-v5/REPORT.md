# A continuous positive qubit interface that passes the non-Clifford test

Research checkpoint for #911, 24 October 2026. This is an explicit alternative
encoding with supplied operations and resources. It is not a native OI
construction, an adopted G3 identification, a derivation selecting quantum
probabilities, full POVM/instrument coverage or a composite reconstruction.
A1 and A2 retain separate targets. #885 remains read-only.

## Result and relation to the preceding obstruction

The standard Kochen-Specker qubit sphere model provides a concrete positive
control beyond the preceding eight-sign architecture. Under the fixed
preparation, reset and access contract stated here, it represents every
single-qubit state and every unitary rotation, and its arbitrary finite
adaptive rank-one projective instrument records and outgoing density operators
agree jointly with the quantum reference. The old rational non-Clifford
rotation test passes, with no unknown preparation label supplied to the
measurement apparatus.

This is prior mathematics used as an architecture control. Ruebeck,
Lillystone and Emerson's primary research paper, arXiv:1812.08218v3,
section 4.1.1, Eq.16, explicitly gives the sphere preparation, rotation,
hemisphere response and re-preparation update, crediting Kochen and Specker.
The independent derivations and exact controls below make its full-record
contract and supplied resources explicit for this programme. Novelty for
the model or its quantum reproduction is not claimed.

The eight-sign no-go remains valid for its stated decoder and input priors.
The new hidden encoding has different input distinguishability and does not
satisfy that finite cube premise. The present positive result establishes
an abstract single-qubit projective/unitary interface, not the full A1
target or the availability of its primitives under native lattice dynamics.

## Fixed preparation cone and decoder

Let the hidden carrier lambda be a point of the unit sphere S^2, with area
measure dOmega. For each unit Bloch vector n define the density

    mu_n(lambda) = max(0,n dot lambda)/pi.

The allowed subnormalized preparation cone C consists of finite positive
mixtures sum_i w_i mu_(n_i), with w_i>=0. It is a specified cone, not the
set of all positive sphere measures. Mixed quantum preparations may have
different hidden decompositions; preparation noncontextuality is not assumed.

For an arbitrary finite carrier measure nu, extend a fixed linear map by

    w=nu(S^2),   r=(3/2) integral lambda dnu(lambda),
    D(nu)=(w I + r dot sigma)/2.

Only its restriction to C is claimed positive. The decoder has no dependence
on public history or on a chosen preparation decomposition.

In polar coordinates c=n dot lambda on the positive hemisphere,

    integral (n dot lambda)_+ dOmega = 2pi integral_0^1 c dc = pi,
    integral lambda dmu_n = (2/3)n.

The transverse first moments vanish by azimuthal symmetry. Hence a mixture
in C has mass w=sum_i w_i and decoded Bloch vector r=sum_i w_i n_i. The
triangle inequality gives ||r||<=w, so D is positive and mass preserving.

Conversely, every positive qubit operator of mass w and Bloch vector r with
||r||<=w is covered. For r!=0 choose n=r/||r|| and weights
(w+||r||)/2 and (w-||r||)/2 on mu_n and mu_-n. For r=0 use equal weights
on any antipodal pair. Two pure-component priors therefore suffice for
state coverage. This does not supply their physical preparation mechanism.

The public/private boundary is part of the contract. The carrier, retained
old carrier values, used random seeds and residual workspace are private.
Future allowed carrier operations do not return-couple those spent registers.
Unused seeds are initially independent of the entire incoming carrier,
workspace and earlier resources. Allowing correlated private memory is
harmless only when its subsequent response is restricted in this stated way;
privacy of direct reads alone does not establish isolation for a native
neighborhood.

## Independent probability integral

A projective setting is a unit vector a. Its public sign is

    s=sign(a dot lambda).

Equatorial ties may follow any fixed convention, since the allowed densities
give every such equator zero probability. For the plus hemisphere H_a,

    mu_n(lambda)=(n dot lambda+|n dot lambda|)/(2pi).

Rotational symmetry gives integral_(H_a) lambda dOmega=pi*a. The absolute-value
term is antipodally even, so its integral over H_a is half its full-sphere
integral, namely pi. Thus, independently of a quantum probability table,

    integral_(H_a) dmu_n
      =(pi n dot a+pi)/(2pi)=(1+n dot a)/2.

Linearity extends this result to every mixture in C. This is a mathematical
consequence of the specified cosine density and hemisphere response. It does
not explain why native OI selects those resources or this operational map.

The checker supplies a second derivation on rational coplanar directions.
Parameterize lambda with its polar axis perpendicular to the preparation/
measurement plane. The polar integral is pi/2; the azimuthal integrand is
n_x cos(phi)+n_z sin(phi) on the intersection of the selected hemispheres.
The checker sorts every boundary direction using exact cross products and
evaluates the primitive n_x sin(phi)-n_z cos(phi) at rational unit endpoints.
It does not call the Born expression to compute that angular integral.
These exact integrals also evaluate the multi-hemisphere countercontrols.

## Rotations and complete projective instruments

For a unitary conjugation with Bloch rotation R in SO(3), use the explicit
hidden permutation lambda -> R lambda. Area invariance sends mu_n to
mu_(Rn), preserves C, and gives D(R_*nu)=U D(nu) U^dagger. Every R is an
allowed primitive of this abstract model; its native availability is not
derived. Unobservable single-qubit global phases are not additional operations.

After exposing s at setting a, the instrument resets the outgoing carrier
with a fresh mu_(s*a) distribution. Its actual subnormalized kernel is

    K_(a,s)(nu)=nu({lambda:sign(a dot lambda)=s}) mu_(s*a).

It uses only the physical incoming lambda and the chosen setting to obtain
s. The reset depends on a,s and fresh resources, not an unknown input-state
label. The hemisphere integral and the rank-one identity give

    D(K_(a,s)(nu)) = P_(a,s) D(nu) P_(a,s).

Both signs, including zero-mass branches, remain in the instrument. Their
probabilities sum to the incoming mass. The output is again in C. There is
no heralding failure, timeout or postselection in this positive control;
the public success flag is always one.

Each complete public increment contains the chosen operation/setting,
outcome sign, success flag and a fixed scheduled completion tick. The model
has one public sign pointer, with no omitted additional raw pointer fields.
Supplying such an interface for an actual native whole-triple port is a
separate readout/access task, not a consequence of this mathematical kernel.
No physical implementation time or gate side-channel is inferred from its
abstract fixed clock.

## Fresh initial resources and retained reversible memory

An explicit reset sampler shows what is supplied. For setting a choose a
fixed measurable orthonormal tangent frame e1(a),e2(a). For independent
initial uniforms U,V on [0,1], let

    g_(a,s)(U,V)=sqrt(1-U)[cos(2pi V)e1+sin(2pi V)e2]+sqrt(U)*s*a.

The polar cosine c=sqrt(U) has density 2c on [0,1], and the azimuth is
uniform. Since dOmega=dphi dc, the resulting density is c/pi, exactly
mu_(s*a). The frames may be defined piecewise with fixed tie conventions;
global smoothness is not required. This sampler uses continuum uniforms and
exact real operations, not a finite bank of fair bits or a native compiler.

For any fixed finite horizon h, all 2h independent uniforms and blank
registers are specified initially. Later encounters consume their preassigned
unused pair. The finite-depth theorem does not insert random data between
encounters. Uniformly treating every finite h permits growing resources; it
does not establish a single bounded apparatus for unbounded depth.

There is also an explicit global reversible dilation retaining old information.
Let b be a second sphere register initially at e_z, and c a blank record bit.
For g=g_(a,s(lambda))(U,V), choose an orthogonal rotation Q_g sending e_z to
g, and define

    (lambda,b,U,V,c) ->
        (Q_g b,lambda,U,V,c XOR 1[s(lambda)=-1]).

An explicit measurable choice is Q_g=H_(e_z-g) J for g!=e_z, where H is the
Householder reflection with normal e_z-g and J=diag(-1,1,1); set Q_(e_z)=I.
Both reflections have determinant -1, and J fixes e_z, so Q_g is a proper
rotation sending e_z to g. The map is invertible on the full space: recover
lambda from the retained second register, recompute g and Q_g from that
lambda and the unchanged seed, recover b with Q_g^T, and undo the record XOR.
On b=e_z,c=0 it gives exactly the required sign and fresh reset sample.

The old carrier and used seeds are retained as private workspace. No erasure,
copy of the unknown quantum preparation label or late ready-state substitution
is used in this abstract dilation. Its existence does not implement it with
the native second-order lattice rule. Unused independent seeds remain fresh
conditional on every prior public history because only earlier designated
seed pairs have entered those earlier kernels.

## Fixed operational relation and arbitrary finite adaptive composition

Define operational equivalence by all allowed finite adaptive future-record
laws, with the public history, setting choices, scheduled ticks and flags
retained. Include zero-step stopping for subnormalized mass. On C, equality
of D is exactly this equivalence. Unequal mass is separated by stopping;
unequal Bloch vectors are separated by some allowed projective direction.

For sufficiency, a rotation preserves equality of D. Every projective outcome
has the same mass on equal-D inputs, and then returns the same subnormalized
measure mu_(s*a) times that mass. Induction on a finite adaptive tree therefore
preserves every complete branch law. Adaptive choices are common functions
of the same already public history. They are not new decoders selected after
an outcome. If a protocol ends with unitary operations, the two outgoing
hidden measures may differ, but their D images and all permitted future
responses agree.

More strongly, for every complete record h the decoded outgoing measure
equals the corresponding subnormalized quantum instrument branch, so record
and outgoing state are checked jointly. Zero-mass branches compare zero
operators without renormalization. Classical mixtures of protocols obey the
same equality when their independent classical-control resource and record
convention are also stated.

This is a conditional all-finite-depth theorem for this single-carrier
kernel/access contract. It is not a proof that the actual native output cone
in #910 satisfies it, an arbitrary native depth theorem or a multi-system
composition result.

## Concrete countercontrols for the supplied restrictions

Let eta_z=(mu_z+mu_-z)/2 and eta_x=(mu_x+mu_-x)/2. Both decode to I/2, but
their hidden densities are |z dot lambda|/(2pi) and |x dot lambda|/(2pi).
They are distinct admissible preparation procedures for the same state.

**Reset and retained workspace.** Take a first Z read followed by direction
b=(3/5,0,4/5). If the hidden carrier is left unchanged between reads, exact
angular integration gives joint sign laws, in (--,-+,+-,++) order,

    eta_z: (9,1,1,9)/20,
    eta_x: (7,3,3,7)/20.

Their TV distance is 1/5 although every individual one-read marginal is
fair. The proper first reset instead gives (9,1,1,9)/20 for both preparations.
Reading the retained old workspace direction b after a correct Z reset
recreates the same 1/5 joint-record gap. Such an added access/return path
breaks the specified congruence. It is a control, not an assertion that a
forbidden native read is physically available.

**Fresh-seed access.** Exposing U,V and s fixes the new hidden point g.
The extended moment decoder of that conditional point law has Bloch length
3/2 and determinant -5/16, outside the positive cone. Even the single seed
bit U>4/9 suffices: it occurs with probability 5/9 and has conditional polar
mean

    E[sqrt(U)|U>4/9] = (2/3)(1-(2/3)^3)/(1-(2/3)^2)=38/45.

Its decoded Bloch vector is (19/15)*s*a and determinant -34/225. The flag's
own marginal is preparation independent, but the flag/outgoing-carrier law
does not preserve this decoder's positivity. This is a fixed-cone failure
for that altered access, not a claim that the original private reset fails.

**Timing.** In an X measurement with proper reset, set an extra completion
label to one if the old hidden Z sign is positive and two otherwise. On
mu_z and mu_-z the designated X record is fair in both cases, but the joint
X/timing laws have disjoint timing support and TV one. A supposed refinement
kappa(s,t) independent of the input would need kappa(+,1)=1 and zero at
once. The fixed scheduled clock in the positive model is therefore a real
contract assumption, not something established by a correct sign marginal.

These controls test changes to reset, workspace return coupling, private
seed access and timing. A native realization must supply the corresponding
isolation/readout/history arguments for all of its actual public metadata.

## The previous rational non-Clifford witness now passes

Use r+=(2/3,-2/3,0) and r-=-r+, the pair that produced the preceding product
encoding's sharp 2/15 record bound. They have concrete sphere preparations:

    nu_+ = (mu_(2/3,-2/3,1/3)+mu_(2/3,-2/3,-1/3))/2,
    nu_- = the antipodal preparation with both poles negated.

All four poles are rational unit vectors. Apply the previous R_z rotation
with first row (3/5,-4/5,0), then X read. The exact laws are

    (29/30,1/30),  (1/30,29/30),

and each outgoing branch is the appropriate X eigenstate. The same R is a
positive sphere permutation independent of which preparation was used.

The source distinguishability has changed. Since mu_n-mu_-n=(n dot lambda)/pi,

    nu_+-nu_-=(r+ dot lambda)/pi,
    TV(nu_+,nu_-)=||r+||=2sqrt(2)/3.

The last equality follows by integrating |r+ dot lambda| over the sphere.
Its square 8/9 exceeds the target record-TV square (14/15)^2 by 4/225.
Thus classical data processing no longer conflicts with that target. The
old product priors had TV 2/3; these are different positive encodings, not a
violation of that earlier theorem or a preparation-dependent apparatus fix.

## Exact bounded evidence and supplied/open gates

`checks.py` uses the Python standard library, fractions and rational complex
matrices. It checks 144 independent angular integrals and 432 corresponding
matrix controls; 17 three-dimensional preparations; 238 complete projective
branches; five rotation generators including rational non-Clifford rotations;
952 adaptive branch nodes with 544 leaf records at depth three; 1,920 reset
sample geometries and 30,720 reversible-dilation inverse cases; plus the
workspace, reset, seed, timing and previous-operation controls. The sampler
distribution and all-depth statements rest on the written continuum proofs,
not on finite sample geometries. No numerical integration is certification.

Run `python3 checks.py` and `python3 -O checks.py`; both must reproduce the
retained structured result byte for byte. Failed controls raise before any
pass verdict. Source compilation is checked separately. No Lean build or
CI attestation is claimed.

The model explicitly supplies:

- a continuum hidden sphere and exact cosine-hemisphere preparation laws;
- arbitrary exact real setting directions and unitary rotation primitives;
- initially independent continuum uniforms, blank registers, and a reset
  controller that computes the geometric map from the actual sign;
- fixed timing, a one-bit public pointer and private workspace/seed isolation.

None is sourced here by the native lattice or derived from OI's conditions.
The density/response choice reproduces quantum probabilities; it does not
derive their physical selection. Enlarging a classical hidden space alone
was insufficient under the old pointwise/G3 map: this candidate also changes
the operational correspondence, preparation cone and supplied availability.
It is not an adopted interpretation of that old G3 architecture.

The remaining gates include native preparation/transport/readout/back-action,
the bridge from the actual finite native phase to this interface, physical
setting and clock selection, access closure, general POVMs and instruments,
ancillary/composite/Bell reconstruction, full A1 sourcing and separately
quantified A2 finite implementations. The A2 lane is examining a finite
approximation of this same geometric interface; this report makes no claim
for that approximation's error or resources.

## Sources and provenance

- Shared five-path comparison: `shared_v12/INTERFACE-CONTRACT.md`.
- #911 source `088af1453efc7780187bc81f8f765f5005b91870`, with the reviewed
  `operational-quotient-v3/` and `product-section-v4/` evidence unchanged.
- J. B. Ruebeck, P. Lillystone and J. Emerson, *Psi-epistemic interpretations
  of quantum theory have a measurement problem*, Quantum 4,242 (2020),
  <https://arxiv.org/html/1812.08218v3>, section 4.1.1 Eq.16, and section 2.3's
  rank-one state-update discussion. This primary research paper supplies
  the standard model and explicitly discusses its limited dimension and
  the explanatory weakness of re-preparing independently of old lambda.
- Original model credit: S. Kochen and E. P. Specker, *The Problem of Hidden
  Variables in Quantum Mechanics*, J. Math. Mech.17,59-87 (1967),
  DOI10.1512/iumj.1968.17.17004, as cited by the read primary source. No claim
  to have re-audited every result in the original paper is made.

This checkpoint's proofs are written mathematics and its computations are
bounded exact controls. Separate-author review is pending publication of
the author snapshot. No manuscript status, new empirical prediction, F/E
designation, dispatch or merge follows. Off-main source/evidence must become
reachable from main before a dependent enduring claim lands.
