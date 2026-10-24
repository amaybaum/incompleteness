# Separate review of the native transport proof audit

**ACCEPT within the stated scope, with no blocking findings.** Reviewed author
revision `a3e8b7a201aae9f7ac6babf93173188f87ed8bb8`, directory
`transport_audit_v1/` on #910. All six local source files were checked against
the immutable GitHub blob IDs and pinned in INPUT-HASHES.json. The reviewer
does not import the author checker or any author engine.

This is a separate-author internal review within the same research effort.
It does not discharge the programme's coordinator-independent or external
proof-review requirement and is not a Lean/kernel certificate. The accepted
proofs do not adapt the dirty post-Y boundary into a reusable instrument.

## Re-derived statements

### Complete reversibility and the role of H

For a phase (V,U), the native next phase is (U,V XOR H(SU)). Given (U,W),
the preceding phase is (W XOR H(SU),U). The algebra requires no inverse of H.
In contrast, the first-front and triangular transport arguments require
the permutation property of H. Its inverse on a local triple is
(A,B,D) -> (D XOR AB,A,B). Direct eight-value checks agree, and H^12 is
identity. Three-step rotation on pure bits is insufficient for raw triples.

### Rear-hemisphere extrusion

Take current sources s on y<=0 and |s|_1=r; prepare the current receiver ball
of radius r+D and previous ball of radius r+D-1, with these source exceptions.
For v=(x,z) of transverse norm k<=r, the queried front value at height d has
time t=r-k+d. Every source has distance at least t from that point.
The old local term at time t-2, forward-y neighbor and transverse inward
neighbors at time t-1 therefore vanish. The only possible terms are the
backward-y predecessor and outward transverse first-front neighbors. The
recurrence follows from the original six-neighbor rule:

    W_d(v)=H(W_(d-1)(v) XOR XOR_outward W_d(u)).

For 0<=d<=D, distance to the final receiver plus t equals r+D. This verifies
that the complete dependencies lie inside the prepared balls; arbitrary
exterior current and previous fields cannot enter. It also proves the
receiver's blank prefix. These are staggered spacetime values, not a clean
simultaneous layer that may be inserted after another measurement.

### Triangular inverse and exponent

The front map is computed from the outer ring inward. Once its outer new
values are given, each old symbol is H^-1(new) XOR the outward new sum.
This proves a permutation on every abstract front, irrespective of whether
the chosen initial source geometry realizes that front.

The outer ring has common period12. If the outer rings have common period Q,
then their entire forcing sequence repeats after Q. Each site in the next
ring undergoes an eight-symbol permutation per Q-block. Its order divides
840, because a permutation decomposes into cycles of lengths at most8.
There are no same-ring edges. Thus all sites in that ring and all outer
rings return after 840Q, for every initial state. Induction through r
inner rings gives 12*840^r. This proves the claimed bound, including r=185;
it does not make that number a period for an arbitrary deeper/different strip.

The independent radius-one closed map has four H-updated outer symbols and
center H(oldcenter XOR their XOR). Its full 32,768-state census gives 1,804
cycles and exact order720. The 22 integer partitions of8 independently
cover all permutation cycle types and verify the universal exponent840.
Actual P is divisible by the audited smaller front bounds; the same argument
does not cover radius186. These checks validate the algebraic mechanisms;
the general induction is the all-radius proof.

### Dirty axial response and whole chronological records

At the first axial arrival from an initial current triple, only one current
neighbor on the unique path can depend on that triple. The old local term
and all other neighbors are too early. Each step is an XOR translation,
followed by H, followed by an XOR translation. Their composition is a
permutation for every fixed, possibly dense, two-slice background.

For several bank blocks, chronological ordering plus an acyclic same-time
graph makes each output depend only on earlier blocks and its own triple.
Conditional on those earlier blocks and the complete initial complement,
the own-triple map is the axial permutation above. Sequential inversion
establishes the whole bank-to-record bijection. Uniform independent bank
triples consequently yield a full uniform word independent of that
complement. This conclusion applies to flags/carriers only when they are
complement functions; it says nothing about a later boundary containing bank
information.

The author cycle countercontrol is correct. With sources (0,3,0),(-2,1,0),
ports (0,0,0),(1,1,0) and tick3 in zero background, both complete outputs
are H(H(H(a) XOR H(b))). The new forward evaluator independently verifies
all64 assignments, blank prefixes, every own-port eight-value permutation,
and only8 joint outputs. Own-port bijectivity therefore cannot replace the
joint acyclic hypothesis. A distinct acyclic native fixture gives64 outputs.
The two-shortest-path source (1,1,0) also gives a zero tick2 receiver for all
eight source values, independently confirming that axial uniqueness matters.

### Wing words and the terminal source row

Within the relevant first-arrival cone, shortest paths from different wings
can meet only on the spine. Before meeting, each wing carries a single
rotating field, so its scalar propagation follows Pascal addition over F2.
For wing w at incoming spine step t, the initial field has rotated to
component (w-t) mod3. Source row q contributes binomial(t,q) modulo2.

The triangular Pascal matrix is its own inverse in characteristic2:
its doubled-transform off-diagonal entry is binomial(n,k)*2^(n-k), which
vanishes modulo2; the diagonal is1. The stated subset-source formula
therefore realizes every finite affine control word. This also preserves
affineness of the initial source functions. The last row q=ell-1 cannot be
dropped merely because the desired terminal control is zero: it may cancel
propagation from earlier rows.

The independent checker obtains the source coefficients by triangular
elimination using ordinary integer binomial coefficients, compares them to
the subset formula, then evolves the full native three-dimensional cones.
Fifteen words, 180 Pascal entries and60 complete spine steps pass. Omitting
the last source row changes14 of these complete endpoints. The exact number
differs from the author's24 because the review uses different control words.

## Radius-185 application and scope

The review also reads the retained1479-entry concrete source geometry.
For each of the four translated carrier receivers, every intended source
has y no greater than the receiver's y and signed rear distance sigma=185;
each foreign source has sigma>185. All5,916 source/receiver comparisons
pass, including exact distances at P=12*840^185. The old unknown previous
origin is outside each enlarged previous ball. The old two public-bank ray
families remain outside the relay cones for every positive index, because
each index increases their signed-distance slack.

This verifies the geometric application of the general lemma. The concrete
compiler word semantics remain the separately retained application audit's
responsibility; this review neither reruns that compiler nor certifies its
all-formula behavior. The larger torus and coordinate lift stipulated by the
current layout are necessary premises. The accepted geometry cannot be
silently transferred to a dirty late q8/q9 neighborhood.

## Reproduction

Run `python3 checks.py --author-root <transport_audit_v1> --source-root
<retained-native-root>` and compare stdout to result.json. Repeat with `-O`.
Both runs pass byte-identically with explicit exceptions enabled. The new
checker uses forward evolution over unions of full backward cones, rather
than the author's recursive native evaluator. It verifies880 staggered-front
values,384 dirty axial values, the complete radius-one map, the native
acyclic/cyclic controls, the wing words and the concrete source geometry.

The accepted result is a set of scoped mathematical transport and record
lemmas with independent internal controls. Native preparation, physical
settings/clock, access closure, probability selection, reusable measurement
back-action, composites, A1 coverage and A2 bounds remain separate work.
