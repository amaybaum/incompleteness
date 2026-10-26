# Native extrusion and chronological frontier: proof audit

24 October 2026. **ACCEPT the scoped extrusion, unique-axis response, and
chronological-frontier lemmas below.** No contradiction was found in their
written arguments. These are mathematical proofs with new bounded controls,
not an astronomical simulation. The proof audit is a separate-author internal
review within the #910 effort. It does not discharge the programme's distinct
coordinator-independent or external-review requirement.

The audit also gives a concrete native counterexample to replacing the joint
acyclic frontier hypothesis by separate own-port bijectivity: two distinct
initial fair triples, invisible at both ports before their deadline, can
produce only eight joint outputs instead of 64. This is a resource-composition
hazard, not a counterexample to the stated chronological theorem.

## Sources and exact claim boundary

The inherited result is `oi_native_transfer_v1/REPORT.md`, especially sections
3 and 5, in the retained combined handoff identified in PLAN.md. The relevant
report hash is
`11f66eb63492b1b563b3f83c51929fa1d2104f91a88b6a6bbb0216bdde3bfcf0`.
PROVENANCE.json identifies every inspected source. Current source reference:
#910 at `71d291297d0a662cbb9377ab48eef7aa4b839e77`.

The theorem concerns sources on a rear hemisphere of an initially blank
two-slice causal cone. It is not a theorem that every native output, with
its actual correlated neighborhood and previous slice, can be placed in that
source family without further preparation. It is also not a theorem about
the quantum probabilities supplied by the apparatus.

## 1. Global reversibility and the local permutation

Write a whole two-slice configuration as `(V,U)`. The update is

    Phi(V,U) = (U, V XOR H(SU)),

where S XORs the six neighboring triples. The inverse, for a given `(U,W)`, is

    Phi^-1(U,W) = (W XOR H(SU), U).

This identity is valid on the infinite cubic lattice, any finite torus,
and any boundary convention using the same S in the forward and inverse
maps. Global reversibility does not require H to be invertible: the inverse
retains U and recomputes H(SU). The checker also uses a constant local map to
test this distinction.

Transport does require the extra fact that

    H(A,B,D)=(B,D,A XOR BD),
    H^-1(A,B,D)=(D XOR AB,A,B)

are inverse permutations of the eight triples. H has order 12. The pure-bit
field cycle has order three, but H cubed is not identity on all raw triples:
the code 011 maps to 101. Also H is not additive; 010 and 001 give a direct
countercontrol. Thus raw-triple transport cannot be justified by single-bit
rotation or addition of independently evolved interacting pulses.

## 2. Extrusion recurrence from the full cubic rule

Fix radius r and delay D. The final receiver is `(0,D,0)` at time r+D.
Prepare its current ball of radius r+D and previous ball of radius r+D-1
blank, except for arbitrary current source triples on

    y<=0,  |x|+|y|+|z|=r.

Every other coordinate outside those prepared balls may be arbitrary.
For transverse v=(x,z), put |v|=|x|+|z| and define

    W_d(v)=U_(r-|v|+d)(x,d,z),   |v|<=r, 0<=d<=D.

These are staggered spacetime values. They are not a simultaneous lattice
slice. A source s on the rear shell has distance to `(x,d,z)` at least
r+d-|v|. Consequently that value, its previous local value two ticks
earlier, its forward-y neighbor one tick earlier, and its transverse inward
neighbors one tick earlier have the required first-arrival exclusion.
More explicitly, the latter three types cannot receive a source by the
times at which the update requests them. The remaining dependencies are
the backward-y neighbor W_(d-1)(v) and the transverse outward neighbors
W_d(u), |u|=|v|+1. The full update therefore gives

    W_d(v)=H(W_(d-1)(v) XOR XOR_(u outward from v) W_d(u)).

No symmetry, linearity of H, or isolated-pulse addition is used. The geometry
also excludes any influence from arbitrary exteriors: each spacetime point
needed in this recurrence has its current backward cone inside the prepared
radius-(r+D) ball, since

    distance((x,d,z),(0,D,0)) + (r-|v|+d) = r+D.

The same inclusion with one less time step handles the previous slice.
The receiver is blank at every time before r+D.

## 3. Finite front map, inverse and exponent

Compute the recurrence from transverse radius r inward. Denote the resulting
front map by F. At each site its dependence on the old value is H preceded
by an XOR translation, with its forcing fixed by already computed outer
sites. Its inverse is explicit:

    old(v)=H^-1(new(v)) XOR XOR_(u outward from v) new(u).

Thus F permutes all abstract fronts, including those that are not physically
reachable from the particular rear shell. This stronger algebraic statement
is legitimate; it does not assert that such fronts are physically preloaded.

On the outer ring F is H independently at every site, so 12 steps return
every outer ring. Suppose all strictly outer rings return after Q steps for
every initial outer state. Their Q-periodic evolution forces each site of
the next ring. Over Q steps that site's own symbol undergoes a permutation
of eight values. Every permutation of eight symbols has order dividing

    lcm(1,2,3,4,5,6,7,8)=840.

After 840Q steps that ring and all the outer rings return. Sites within a
ring have no same-ring neighbors, so this holds for every site at once.
Induction over the r further rings proves

    F^(12*840^r)=identity.

It follows that delay D=12*840^r, or any positive integer multiple, returns
the whole center triple to its original first-arrival value. The initial
preparation does not depend on that computed value. For the inherited
radius-185 source application, r=185 is exactly the theorem's radius and
P=12*840^185 is therefore a valid exponent. The source/application audit
is a separately retained dependency; this audit does not recompute its
1,479 compiled entries.

This exponent is a bound, not the minimal period. The independent complete
radius-one census gives order 720 over all 32,768 fronts, dividing 10,080.
Nor does P automatically cover a larger or differently defined strip. A
strip reduction needs its own closure proof, its own exponent prefactor,
and exact divisibility. A budget of 186 does not inherit the radius-185
bound by this argument. This report does not audit every signed-strip
reduction used later in #910.

An intervention in the center output at its first-arrival time is also
carried by the abstract-front identity, as a diagnostic. Other initial-front
values have earlier times; their future translated values cannot receive
that intervention early enough to change the recurrence. This does not make
the intervention an available native observer operation.

## 4. Unique axial arrival in an arbitrary dirty background

Let an initial current triple B be at an axial displacement t from a port.
Fix every other initial current and previous coordinate. At step k along
the unique straight path, only the immediately preceding path vertex can
already depend on B. Each other neighbor has a longer route; the old-local
slice is two ticks too early. The step therefore has the form

    z -> c_k XOR H(z XOR b_k),

where b_k and c_k can be arbitrary background-dependent triples but do not
depend on B. Its composition is a permutation of B. Dense dirty background
does not invalidate this conclusion.

The conclusion is functional, conditional on the full complement. It does
not itself give a usable output decoder when that complement is unknown or
correlated with B. In particular it cannot replace an actual instrument's
back-action/reset or prove independence of a whole next-stage neighborhood.

Uniqueness matters. With a source at `(1,1,0)` and receiver at the origin,
tick two has two shortest paths. In a zero background the two intermediate
H images cancel, and the receiver is zero for all eight source values.
Being on a causal boundary alone does not imply a permutation response.

## 5. Chronological multi-port theorem and a native cycle obstruction

Let each designated raw output block have one distinct initial current
triple assigned to it by a unique axial path. Suppose no later-assigned
triple reaches an earlier output, and the equal-time dependency graph is
acyclic. Choose chronological order, breaking equal times by a topological
order. Each output is then a permutation of its own triple for fixed earlier
triples and the initial complement C. Successively invert these permutations.
The complete bank-to-record map is a bijection for every C.

If all bank triples are independent uniform conditional on C, the full record
word is uniform independent of C. This implies independence from a selected
carrier, flag or earlier history only when that object is a function of C.
It does not imply independence from an entire later physical boundary that
may itself depend on the bank. Readiness must leave these bank coordinates
free. Correlations or pins can violate the conclusion.

The checker independently evaluates a dirty-background two-port acyclic
block, obtaining all 64 output pairs. Duplicating its fair symbol or pinning
one source gives eight possibilities. A separate exact counterexample shows
why individual own-port response does not establish the joint premise.

Take zero previous/background fields and two current triples a,b at

    f0=(0,3,0), f1=(-2,1,0).

Read the whole triples at p0=(0,0,0), p1=(1,1,0), tick three. Both source
distances to both ports are three, and each assigned own path is straight.
Neither port sees either source before tick three. Nevertheless the equal-time
dependency graph has edges in both directions. Direct use of the full native
rule gives

    U_3(p0)=U_3(p1)=H(H(H(a) XOR H(b))).

For every fixed b the own-port map in a is a permutation, and conversely
for fixed a. But the joint pair has only eight values under the 64 fair
assignments. Thus separate per-port freshness and even conditional own-port
bijectivity are insufficient. The acyclic hypothesis is a sufficient joint
criterion. This one cyclic counterexample does not rule out every cyclic
layout.

The existing seven-port theorem explicitly checks its acyclic edge set.
Any enlarged access class, including the new herald port after L, must
check its complete ray geometry and new equal-time edges again.

## 6. Wing-source compiler and terminal row

At a deadline ell, let g_t be any affine control triple for 0<=t<ell,
including its desired terminal control. The three initial wings at

    (ell-1-q, q+1,0), (ell-1-q,-q-1,0), (ell-1-q,0,q+1)

carry one field each, at every q from zero through ell-1. Shortest paths
from different wings meet only on the spine. Before meeting, each pure
field rotates A->D->B->A; its nonlinear product vanishes. Its scalar
first-front propagation is the Pascal recurrence over F2. Thus source
row q contributes binomial(t,q) modulo two to spine step t.

Let B_w(t) be the component of g_t which rotates from wing field w after
t steps. Define A_w(q) as the XOR of B_w(e) over all binary subsets e of q.
The Pascal/subset transform is its own inverse over F2: in the double sum,
each proper subset occurs 2^k times for k>0, and the diagonal once.
Consequently these affine initial sources inject exactly g_t. The spine
executes H(state XOR g_t); the old-local term is blank on the first front.

The formula is valid for every finite ell. It includes q=ell-1 even when
the last desired control is zero, because cancelling earlier propagation
can require a nonzero terminal source. All 24 small source-program cases
in the new checker detect wrong whole outputs when that last row is removed.
Current herald synchronization still needs its separately checked affine
word, padding count and source/readiness geometry; a generic source formula
does not choose its probability calibration.

## 7. Torus and evidence boundaries

The preceding arguments take place in an integer-coordinate causal cone.
For one horizon h, a torus side larger than 2h+1 embeds the radius-h cone
without an alternative short path. With several cones, sources and bank
rays, one must verify a single consistent coordinate lift or check torus
distances directly for their complete ranges. In the current #910 remote
layout, the stated side 256L+64T+1 and coordinate envelope [-49L,49L]
in x leave each relevant difference below half the side; y,z are smaller.
No wrap shortcut then changes the documented distances. The small side-three
control demonstrates early arrival when this condition is dropped.

These conclusions preserve all source and failure information. They neither
derive the supplied fair prior/readiness nor provide a physical clock,
setting actuator, access restriction, calibration selection, arbitrary menu,
unlimited history on one fixed finite apparatus, or composite quantum model.
Most importantly, they do not turn the accepted selected post-Y phase into
a natively accepted reusable instrument boundary.

## Replay

`checks.py` imports no author module and reads no external file. Run
`python3 checks.py` and `python3 -O checks.py`; each output equals result.json.
Both executions use explicit exceptions. The result records all 40,320
eight-symbol permutation exponent checks, 648 inverse-site comparisons,
48 dirty-background axis maps/384 value comparisons, 645 actual native
front values, the 32,768-state radius-one census, 84 native wing/spine
steps, and the stated negative controls. These bounded controls support
the proof mechanisms; the all-radius and arbitrary finite-length results
are established by the written induction and combinatorial arguments.
