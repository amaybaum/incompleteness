# Nonlinear feedback with permutive frontiers

Exploratory independent handoff, 2026-10-23. Read-only with respect to the
repository: no edits, commits, pushes, comments, workflows or premise adoption.
This follows report17 at ce76f0a5 and does not alter its accepted obstruction.

## Result

A new three-field update supports all of the following together:

* exact global reversibility;
* nonlinear feedback among the fields;
* a bounded source word of independent uniform raw triples, proved by a
  bijective extreme-frontier argument rather than linearity;
* a two-stage raw AND computation: three affinely encoded input bits can
  produce their exact zero-detection flag at tick 2;
* a complete specified source/receiver record law on one conditioned prior.

This resolves a compatibility question left open by report17: nonlinear
feedback need not destroy bounded freshness. It is not a derivation of the
new rule from OI, universal computation, a general J-bit readiness detector,
autonomous preparation, a native clock, an angular law or quantum equivalence.

## 1. Relation to report17

I read the review at
https://github.com/amaybaum/incompleteness/blob/ce76f0a5/verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/mc-node9/design/owner-checks/report17/REVIEW.md

Its general conjugacy observation is valid: if F=G^(-1) L G with L linear,
deg(G)=g and deg(G^(-1))=g', then F^t=G^(-1) L^t G has degree at most gg'.
The bound follows directly from the degree bound for polynomial composition.
It applies to a fixed conjugacy on the complete phase state, with the stated
degree bounds. The 16-predicate family has the sharper degree-2 bound because
its A and B waves remain linear and only D receives the quadratic decoder.

The new construction below replaces that update; it does not invalidate any
of the old rule's impossibility statements. The freshness proof also changes.

## 2. One new local reversible rule

Work over F_2 on a cubic torus. Each site has raw triple U=(A,B,D), at both
previous and current times. Let S be the XOR of the six nearest-neighbor
triples. Define the permutation

    H(a,b,d) = (b,d,a+bd),
    H^(-1)(x,y,z) = (z+xy,x,y).

The update is

    U_(t+1)(x) = H(S U_t(x)) + U_(t-1)(x),

or, componentwise,

    A' = SB + A_old,
    B' = SD + B_old,
    D' = SA + (SB)(SD) + D_old.

All sums are XOR. The update is autonomous, translation invariant, cubic
invariant in space, and radius one in phase space. Its current-slice force is
center-free. The all-zero state is fixed. Internal field labels have a supplied
cyclic order; spatial cubic symmetry does not assert internal-label symmetry.

Given (U_t,U_(t+1)), recover U_(t-1)=U_(t+1)+H(SU_t). Thus the full finite
phase map is a bijection and preserves uniform counting. This global inverse
does not even require H to be injective; injectivity of H is the additional
property used for source freshness. The D field feeds back into B, then A,
and the subsequent nonlinear products. This is not the prior rule with a
decoder attached.

No conservation of a physical energy or canonical energy-shell law is proved.
The rule and uniform prior are explicit candidate assumptions.

## 3. General permutive-frontier lemma

More generally, let each site carry a symbol in a finite abelian group V,
and let H:V->V be any bijection. Use the same second-order rule with the
neighbor sum in V. Fix a source q and horizon T with torus side L>2T+1.
Reserve the initial-current symbols

    Z_t = U_0(q+t e_x),  t=1,...,T.

Condition on all other initial-current and initial-previous coordinates.
Suppose the reserved Z_t remain independent uniform symbols in V. Then the
source word U_1(q),...,U_T(q) is uniform on V^T.

Proof. A later Z_t cannot affect an earlier output U_s(q), s<t, by finite
propagation speed and the absence of a shorter wrap-around path. At time t,
Z_t reaches q along the unique length-t extreme path. At each vertex of
that path, only the predecessor neighbor on the path can depend on Z_t at
the relevant time. Other neighbor terms and the previous-slice term cannot
depend on it because they would require a faster path. The local dependence
is therefore z -> H(z+c)+d, a bijection for fixed c,d. Composing along the
path is bijective. The map from (Z_1,...,Z_T) to the source word is triangular
with bijective diagonal maps. It is a bijection of V^T and preserves uniform
counting. This proof is nonlinear and does not assume superposition.

For V=F_2^3, each symbol is a raw three-bit triple, so every source word has
probability 8^(-T). The initial port pair may be fixed to zero or any other
values: these are unreserved coordinates. Likewise the complement can be
nonuniform or internally correlated provided the frontier remains independently
uniform conditional on it. This does not assert freshness after arbitrary
records that reveal frontier coordinates.

### Bounded stopping and record conditioning

The same argument applies branchwise at a start W=w, reserving current
coordinates q+(w+t)e_x for t=1,...,K. If the entire history deciding W=w
depends only on the complement, then after conditioning on that history the
next K source triples remain uniform. Any receiver record that depends only
on that complement is independent of those triples as well.

A sufficient geometric arrangement for an ideal flag history is as follows.
Let the wait cap be B, receiver readiness tests inspect its radius-r region,
and the post-start receiver/source windows last K. Set T=B+r+K, side
L=8T+1 and source q=(4T,0,0). Records through W may inspect that receiver
region and the source's past and current port values. Receiver dependency
cones and the post-start source cone are disjoint in the initial data; the
new source frontier coordinates are outside every earlier source cone.
Thus these histories cannot select the future frontier variables.

This is a source-only conditional statement. It does not prove fair payloads
after arbitrary readiness histories, implement the flags, or transfer all
of report16's linear-rank formulas to the new nonlinear rule. A native
controller would have to satisfy the same record/dependency conditions.

The checker includes an exact stopping control with the nonlinear source:
start at the first tick 1 or 2 where its A bit is 1, expose the entire source
prefix, then read the next triple. It remains exactly uniform on every
successful prefix. No physical clock is implemented by that control.

## 4. A raw two-stage AND computation

Use horizon K=2, side L=17, receiver o=(0,0,0), source q=(8,0,0).
The three input slots on the current slice are

    B_(1,1,0) = a,
    D_(1,-1,0) = b,
    D_(0,0,2) = c.

Fix every other current raw bit in the receiver's radius-2 ball to zero,
and all previous raw bits in its radius-1 ball to zero. Values outside this
two-slice cone can be arbitrary. The receiver begins blank.

At tick 1, the intermediate site u=(1,0,0) has raw triple (a,b,ab). The
receiver is still (0,0,0). At tick 2, the receiver has

    (A_o(2),B_o(2),D_o(2)) = (c,ab,abc).

Derivation: in F_2, S^2 is the sum of the six displacements by two steps
along a single coordinate axis. The mixed-diagonal a and b inputs make no
contribution to S^2 at o, while the axial c input contributes once.
The only neighbor u of o receiving both the a and b inputs at tick 1 is
(1,0,0). Hence

    S B_1(o)=c,
    S D_1(o)=ab,
    S A_1(o)=0.

Previous receiver bits are zero, yielding the displayed output. The first
AND product is used as an input to the next AND under the unchanged new
update; there is no intervening external reset or gate selection.

Set a=1+x, b=1+y, c=1+z as an affine input encoding. The raw D output is
(1+x)(1+y)(1+z), exactly testing whether three freely varying input bits
are all zero. This evades the old rule's degree-2 obstruction. The other
raw receiver bits still reveal c and ab; the construction claims no privacy
for them. Nor does it autonomously load the input slots.

This is one two-stage circuit, not a universal-computation theorem or a
construction of the full 99-bit ready-event detector.

## 5. One prior and the complete specified joint record

Start with uniform counting over the entire raw two-slice phase space.
Condition on the receiver constraints above, and on previous and current
raw source triples at q being zero. Call this event E. Every unlisted bit
remains independent and fair. In particular a,b,c remain independent fair
payload bits.

The number of fixed independent raw bits is

    J = 3(|B_2|+|B_1|)-3+6 = 3(25+7)+3 = 99.

Thus P(E)=2^-99. This is the cost of this event, not a minimum, and is not
an efficiency comparison with the earlier K=3 event of codimension 268.
Native preparation, recognition and waiting for E remain unresolved.

The source/receiver initial cones through tick 2 are disjoint. The source
frontier triples at q+e_x and q+2e_x are not constrained by E. By the new
frontier lemma and receiver locality, for every payload and source word z,

    P(source=z, receiver=r | E,a,b,c)
       = 8^-2 * 1{r=((0,0,0),(c,ab,abc))}.

Without conditioning on the payload, each such joint assignment has
probability (1/8)8^-2. The specified record exposes both raw port triples
at ticks 1 and 2. An ideal initial readiness flag can be included, with
failure probability 1-2^-99; failures terminate without the subsequent
window. This last interface is stated, not physically derived.

For the three-input zero test, condition instead on the affinely encoded
input x,y,z; the same source law holds, and the full receiver record is
(0,0,0) followed by (1+z,(1+x)(1+y),(1+x)(1+y)(1+z)).

## 6. Checks and countercontrols

frontier_checks.py is standard library, stdout only, with fixed random seeds.
It imports no earlier handoff code.

1. Exhaust all eight values of H and its inverse. Check the global raw
   inverse on 24 dense transitions on sides 3,4,5, including wrap-around.
2. Enumerate all 8^K frontier assignments for K=1,2,3 on each of two fixed
   backgrounds, six complete tests. Every source word occurs exactly once.
   The second background assigns arbitrary seeded values to the remaining
   relevant cone bits; the proof covers all complement assignments.
3. On the K=3 source tables, verify exact next-triple freshness after a
   first-A=1 stopping test at tick 1 or 2 with the complete past prefix visible.
4. Replace H by H_bad(a,b,d)=(b,d,bd). The global second-order update remains
   invertible, but at tick 1 only four of eight source triples occur. TV from
   uniform is 1/2. Thus global reversibility alone does not prove freshness.
5. Exhaust all 512 payload/frontier assignments for the joint two-tick
   apparatus, separately for AND3 and complemented-input zero detection.
   All 64 source words occur once per input; the full receiver record holds.
6. Independently fill all unconstrained phase bits on the entire 17^3 torus
   with two dense seeded backgrounds. For all eight payloads in each, the
   receiver record is exact and source readings do not change with payload.
7. Evolve exact bit-packed truth tables on six selected free input bits
   with a fixed dense background on a 5^3 torus. Maximum output degrees at
   ticks 1,...,8 are [1,2,3,4,6,6,6,6]. This is finite evidence of degree
   growth, not a proof of unbounded degree or universal computation. The
   explicit AND3 example already proves degree 3 is attained at tick 2 on
   its different input subcube.

During exploratory development, the first joint-record assertion incorrectly
put zero in the terminal A register. The check rejected it. Direct calculation
gives A_o(2)=c, so the final record and all saved checks include that exposed
input. This was an unfrozen exploratory correction, not a changed acceptance
criterion. The receiver's D=abc claim was unchanged.

## 7. What this changes next

The apparent choice between nonlinear feedback and exact bounded source
freshness is not forced. Local permutivity supplies a replacement for the
linear-wave freshness proof. The demonstrated gate composition moves beyond
the old degree ceiling, but neither selects a physical law nor supplies the
large detector/clock/preparation assembly.

The next construction target is a larger native aggregation/clock circuit
under this same candidate, with explicit prepared resources, signal routing,
latency, exposed side records and source frontier separation. First establish
whether AND aggregation can scale without undesired wave interference; do
not infer general composability just from this two-stage example. Any change
of update or interface must be stated. Angular emission and station-indexed
preparation equivalence remain separate open targets.
