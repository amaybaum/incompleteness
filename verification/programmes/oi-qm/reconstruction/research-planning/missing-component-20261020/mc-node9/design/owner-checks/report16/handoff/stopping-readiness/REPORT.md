# Readiness resources and a bounded stopping-time extension

Independent read-only research handoff, 2026-10-23. No repository modification,
comment, commit, push, workflow, or premise adoption. This is an exploratory
mathematical result, not a preregistered apparatus acceptance test.

## Result

The carrier construction's fixed-start law extends to a first-ready stopping
time with a finite waiting cap. In its existing geometry L=8K+1 and port
separation 4K, the theorem below allows a cap B<K. In particular K=3 permits
W=0,1,2. Conditional on any successful start time, including all earlier failed
readiness flags, the two payloads remain independent fair bits and the next K
raw source triples remain independent uniform eight-valued symbols. The receiver
has the same silent-then-product record as in the original handoff.

For any finite cap B, enlarging to L=8(K+B)+1 and separation 4(K+B) also suffices.
This consumes space; it does not remove the rarity of readiness. Success by B
is at most (B+1)2^(-J_K). No physical readiness detector or clock is constructed:
the flags and update-count times below are an explicitly supplied ideal interface.

The next native-construction obligation remains to implement that interface,
including its latency, extra records, resource state and backreaction. This
report proves a conditional law that such an implementation would need to retain.

## 1. Fixed-time entropy accounting

Let Omega have M states, U be uniform, and F be a bijection. Let E have
q=|E|/M=2^(-J). For an initial law P, put p=P(F^t X in E). Logs are base 2.
Grouping states inside and outside F^(-t)E gives

    log2(M)-H(P) >= D_Ber(p || q)
                   = p J - h2(p) - (1-p)log2(1-q).

Proof: H(P) <= h2(p)+p log2|E|+(1-p)log2(M-|E|), since conditional entropy
is at most log support size. Rearrange. Equality is attained by a law uniform
within each of the two groups. If p>=1-delta>q, monotonicity in p yields

    log2(M)-H(P) >= (1-delta)J-h2(delta)-delta log2(1-2^(-J)).

For guaranteed readiness the exact deficit is at least J bits. The result
applies to the chosen E, not to every apparatus achieving the same output:
J_K=268 is not a proved minimum. Entropy deficit can be held in marginal
nonuniformity or correlations. Calling it a cold resource is operational
shorthand; no temperature, Hamiltonian, energy conservation or heat bath is
specified, so this counting argument alone is not a thermodynamic heat bound.
The thermodynamic distinction is consistent with Reeb and Wolf,
https://arxiv.org/abs/1306.4352 .

## 2. Return time is not preparation waiting time

Let Sat(E) be the union of permutation cycles intersecting E. If the initial
state is uniform on E and tau is the first positive return time,

    E[tau | X in E] = |Sat(E)|/|E| <= M/|E| = 2^J.

Proof: split each cycle into gaps between consecutive E states. Each gap's
length is the return time from its first E state; the sum of all gaps is
|Sat(E)|. Equality with 2^J holds iff every cycle meets E.
This is the finite permutation form of Kac's return identity; for the standard
ergodic statement see https://www.mat.univie.ac.at/~bruin/ET3.pdf .

Now start uniformly on Omega and define W=min{t>=0:F^t X in E}. Any cycle
avoiding E gives positive probability W=infinity and hence infinite mean.
Even when all cycles meet E, Kac's return mean is not the mean of W. If the
successive cycle gaps have lengths ell_i, then

    E[W | X in Sat(E)] = sum_i ell_i(ell_i-1)/(2|Sat(E)|).

Proof: the waiting times contributed by a gap are 0,1,...,ell_i-1. Thus gap
clustering matters. On a 16-cycle with eight consecutive E states, the return
mean is 2 but the uniform-start first-hit mean is 9/4. On the identity
permutation a state outside E never becomes ready.

There is a robust finite-deadline statement, needing no independence:

    P_U(W<=B) <= min(1,(B+1)2^(-J)).

Proof: union bound over F^(-t)E, t=0,...,B, all of equal cardinality.
Consequently high success from a uniform start requires a very large deadline,
but neither a typical waiting time nor an upper mean bound follows from q alone.

For the actual three-field construction there are states that never enter E_K:
take A=1 everywhere on both initial slices and B=D=0 everywhere. The neighbor
sum of six ones vanishes in F_2, so this state is fixed; E_K requires many A
coordinates to be zero. Thus waiting for this event from the full uniform
finite ensemble has a nonzero never-ready probability and an infinite
unconditional first-hit mean. This observation does not quantify its practical
size and is not a no-go for a prepared initial ensemble.

## 3. Self-contained rule and readiness definition

Use binary fields A,B,D on a cubic torus of side L. S is XOR of the six nearest
neighbors, and 'old' denotes the preceding time slice. The fixed raw update is

    A' = SA + A_old
    B' = SB + B_old
    D' = SD + D_old + S(AB) + (SA)(SB) + (SA)B_old + (SB)A_old.

All sums are in F_2, products are pointwise. The pointwise bijection
C=D+AB on each phase slice conjugates this to three independent waves:
U'=SU+U_old for U=A,B,C. The initial uniform full raw phase distribution
becomes the uniform product distribution of A,B,C at times -1 and 0.

Receiver o=(0,0,0); payload positions pA=(K,0,0), pB=(0,K,0).
Let B_r(o) be the lattice L1 ball. At each time t, define E_t by:

* current A=0 on B_K except pA;
* current B=0 on B_K except pB;
* current D=0 on B_K;
* previous A,B,D=0 on B_(K-1);
* previous and current A,B,D=0 at the source q.

Because A and B have disjoint allowed supports on the ready ball, AB=0 there;
the same is true in the previous ball and at q. Thus E_t is exactly the same
set of zero constraints with D replaced by C, and is a linear subspace in the
linear-wave coordinates. Its codimension is

    J_K=3(v_K+v_(K-1))+4,  v_r=(4r^3+6r^2+8r+3)/3.

Here E_t means readiness of the evolved phase state, not that a device has
measured it without disturbance. Define W as the first successful E_t among
t=0,...,B, and W=infinity if there is no success within this cap. This capped
failure convention differs from an unbounded first hit.

## 4. Exact stopped joint law

Choose either:

* original geometry L=8K+1, q=(4K,0,0), and 0<=B<K; or
* enlarged geometry L=8(K+B)+1, q=(4(K+B),0,0), with any finite B>=0.

On W=w<=B let a=A_pA(w), b=B_pB(w). Let Z be the K raw source triples at
w+1,...,w+K, and R the receiver triples at those same times. Put
r(a,b)=((0,0,0),...,(0,0,0),(a,b,ab)). The full successful record law is

    P(W=w, a,b,Z=z,R=r)
       = P(W=w) * (1/4) * 8^(-K) * 1{r=r(a,b)}.

The flags are w failures then a success, so they are included by W. The failed
branch has B+1 failures and no subsequent carrier/source window. Its probability
is 1-sum_(w=0)^B P(W=w). All probabilities include failures, with no
renormalization of completion probability.

### Proof of the law at the stopping time

Fix a successful branch w and work in initial A,B,C coordinates.

First reserve two initial-current payload frontier bits: the A bit at
(K+w,0,0) and the B bit at (0,K+w,0). Each reaches its respective payload
position at time w with coefficient one along a unique extreme path. Neither
can affect any receiver readiness constraint at an earlier candidate time
i<w, since its distance from B_K exceeds i. At time w the only point of B_K
it can reach is the corresponding excluded payload position. It cannot reach
the previous B_(K-1) constraints. The source is sufficiently far away that
neither frontier affects the source readiness constraints. Hence all E_i for
i<=w, and the event W=w itself, are independent of these two reserved bits.

Next reserve the 3K current bits in fields A,B,C at positions q+(w+t,0,0),
t=1,...,K. They are outside the initial dependency cones of every source
readiness test through w. They are also outside all receiver readiness cones
through w and the receiver's subsequent observation cone through w+K.
For the original geometry, both radius-(w+K) cones are disjoint because
w+K<2K and the centers are 4K apart on the torus. For the enlarged geometry,
w+K<=K+B and the separation is 4(K+B). L prevents competing wrap-around
paths at these times. The payload frontier bits are likewise disjoint from
the source window cone.

Conditional on every unreserved initial bit and W=w, all 2+3K reserved bits
remain independent fair bits. The payload map is a separate bijection on two
bits. At each source time w+t the new frontier coefficient is one, and no
later frontier bit has yet arrived. The map from 3K frontier bits to source
words in A,B,C is triangular with identity diagonal blocks, hence bijective.
The raw map (A,B,C)->(A,B,C+AB) is bijective at every reading, so the raw
source words are uniform too. This proves independence jointly, including W.

Finally E_w fixes the receiver cone so the wave solution is zero before K
and equals a,b at K; C is zero on that whole cone. Therefore raw D=AB and
R=r(a,b). Averaging over unreserved bits proves the displayed law.

This proof uses the exact readiness flags specified here. It does not authorize
extra records revealing a reserved frontier bit, an unbounded waiting history,
or physical interventions. Any actual detector/clock must be incorporated
before calling its records covered.

## 5. Exact first-success probabilities and checks

Each E_i is a homogeneous linear constraint system in the initial wave bits.
For any finite I, P(intersection_(i in I) E_i)=2^(-rank H_I). Inclusion-exclusion
therefore gives

    P(W=w)=sum_(S subset {0,...,w-1}) (-1)^|S| 2^(-rank H_(S union {w})).

For K=3, L=25, q=(12,0,0), the independently built wave rows yield

    P(W=0) = 2^-268
    P(W=1) = 2^-268 - 2^-385
    P(W=2) = 2^-268 - 2^-442 - 2^-385 + 2^-502.

Thus readiness attempts are not independent. Nevertheless the successful
payload/source law factors exactly as above. With B=2, success probability
is 3*2^-268 - 2*2^-385 - 2^-442 + 2^-502, not a practical preparation rate.

The standard-library, stdout-only checker constructs initial-bit linear forms
by wave recursion on the actual torus, not by assuming the frontier theorem.
For all 48 readiness intersections across six (K,B,L) geometries it checks
the exact rank increase 2+3K for the payload and all future source coordinates.
This proves their joint uniformity on each intersection, so inclusion-exclusion
also proves it on each first-success branch. It verifies the receiver identities
by subspace membership on the entire ready subspace, not a zero-background slice.

An independent direct raw-update implementation compares these linear forms
against 60 transitions from dense deterministic-pseudorandom backgrounds,
including wrap-around on small tori. Other checks cover 1,872 exact integer
entropy inequalities and 3,769 permutation/event cases for return and first-hit
times and the deadline bound. Logs are not used in those integer comparisons.

Stopping countercontrols use a five-bit uniform circular tape advanced by a
bijective shift. At the first observed 1 the selected bit is certainly 1.
The strictly next bit remains fair before wrap-around, but when the first 1
occurs at position 4 the next bit is the already observed initial 0. This
separates selection bias, valid future freshness and finite-resource recurrence.

## 6. What is and is not advanced

Advanced: bounded freshness at the actual stopping time, complete failure-flag
conditioning, fair payloads at that stopping time, exact first-success laws,
and explicit resource/waiting bounds. Overlapping cones outside the theorem's
range invalidate this proof; they do not by themselves prove an actual leak.

Not constructed: a native local readiness detector, an autonomous clock,
finite-latency recognition of the spatial readiness event, controlled payload
injection, a practical supply of ready resources, backreaction-safe readout,
station-indexed preparations, an angular law, or quantum equivalence. The
uniform starting ensemble here makes successes rare; no entropy deficit is
silently inserted to improve that rate. Extra prepared clock/register resources
would need to be included in the entropy budget and the joint record law.

Suggested next construction target: implement a bounded-latency readiness flag
and clock with an explicit initial resource state, then check which extra
records or causal dependencies change Section 4. No accuracy refinement of
C-SPH-1 and no composite/Yang-Mills claim follows from this result.
