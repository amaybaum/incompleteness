# Native B: a single seeded outward port loses X on an accepted branch

Research checkpoint on #910, base
`00e85e748cf8e5ada75f4e1a22aef87eb0a823a2`. The original source-family plan
was published before computation at
`05397c79370f66c88f0bf8fdaedb09297ba358a9`; the bounded pad-aware follow-up
was published before its computation at
`8dd2bc32ae30223db4238669b041ca4a259287e1`. Separate-author review pending.

## Result

This original-time source-compatible route does not transmit the actual
retained X sign into the single current q10 port. The native calculation
preserves the old q9 phase, brings a new affine source into q10, and keeps
the actual dirty six-neighbor and old-local contributions. Nevertheless,
on the accepted old branch u=0,a=b=1, the q10 triple is independent of
unknown x for every new source payload and every old selector-pad pair.

Thus no controller N(k,c) depending only on known old apparatus seeds/pads
and independent new seeds can make q10 alone a pointwise encoding of
s=x XOR u XOR a on all retained accepted worlds. A redundant deterministic
decoder of q10 alone does not repair the loss. The actual previous q9 still
contains s; the full two-slice phase has not erased it. This is a failed
single-port adapter, not a no-go for distributed encodings, multi-source
native processing, quantum instrument laws or OI generally.

## Physical candidate and changed initial resource

Keep T=185, P=12*840^185, S=P+185, R=S+68 and L=R+9. The accepted old
q9 at (0,S,77), time L, is

    (0,s,r_old), s=x XOR u XOR a, r_old=s XOR(a XOR b),

for old masks00,10,11. All original W/Q/C/G/J/K source payloads are retained.
Extend the original-time current ready region to B_(R+10)(q10), and the
previous one to B_(R+9)(q10), at q10=(0,S,78). Preserve the existing source
and bank exceptions. Add a current initial source at

    position N=(0,S,S+156).

The same letter denotes its variable raw triple when no position is shown.
Its distance to q10 is R+10=L+1; distance to q9 is L+2. It arrives natively
at the new port and cannot change the old prepared q9 or its record at L.

This candidate explicitly replaces the optional uniform F10 factor at
(-(L+1),S,78) by a specified boundary pin. F8=(-(L+1),S,76) is outside the
new ready cone and may remain independent. The canonical64-value Q8/Q10
pool theorem is therefore not inherited unchanged. This is a candidate
resource contract, not adoption of a preparation rule.

All1479 old compiled source positions are on or outside the new q10
boundary. N matches none and is outside all24 earlier ready regions.
Every old/new public-bank ray through L+1 remains outside the new ready
pins. The smallest bank slack is one. N cannot reach any old/new designated
public port by L. The old informative phase is therefore preserved, and
the existing chronological bank bijection preserves the complete old
public-history law conditional on the changed complement. Pointwise noise
backgrounds need not be equal after adding initial zero constraints. No
late readiness, unknown-s copy or erased reserved bank is used.

## Exact native kernel

The retained q10 table has512 rows, ordered lexicographically as

    x,u,mY,mR,a,b,Ncode,    code=4A+2B+D.

Its hexadecimal form in result.json includes all eight N triples and all
old mask01 failures. The encoded-table SHA-256 is
`8bc1462854ce5fb80c18a48e8208037eb6bd613aa5babb28721e186aec3387f9`.
This is a compact encoding of complete native raw triples, not selected
moments. The entire old q9 table is unchanged in all512 rows.

For every fixed old x,u,mY,mR,a,b, the N-to-q10 map is a permutation of all
eight triples, as expected for a unique axial first arrival. This useful
fresh-source response does not imply that the port also transmits s.

The first64 affine controls were

    N=(a XOR b)*C XOR c*V.

The only extended512 family was

    N=(u XOR a)*B XOR(a XOR b)*C XOR c*V.

B,C,V each range over the eight constant triples. Both families contain
no common whole-triple code of s,c across all actual accepted old contexts.
Neither implements any of the registered clean, mixer or paired-sign
targets. Results retain counts, survivor lists and multiplicity histograms;
the full512-byte native table reconstructs the family exclusion.

## Two independent adapter obstructions from that kernel

### Used recording pad re-enters the next port

On accepted old mask10, toggling mR always flips q10.B when x,u,mY,N are
held fixed. All64 paired checks pass. For example, with x=u=0,a=1,b=0,N=000:

| mY,mR | q9 at L | q10 at L+1 |
| --- | --- | --- |
| 00 | 010 | 001 |
| 01 | 010 | 011 |
| 10 | 010 | 001 |
| 11 | 010 | 011 |

Thus a control that ignores mR cannot give a common whole-triple output code.
This is selected-boundary noncongruence: equality of the complete earlier
public record between these pad variants is not established. Old informative
ciphertexts may differ. No operational inequivalence is inferred from this
pointwise witness. Overall144 of512 diagnostic rows, including80 accepted
rows, differ when pads are changed from00.

### Even pad-aware seed-only N cannot make q10 retain s

For each of the24 known contexts k=(u,mY,mR,a,b) with accepted old mask,
form the eight ordered raw pairs

    (q10 for s=0,N; q10 for s=1,N).

A seed-only controller N(k,c), even nonlinear and pad-aware, would need a
common injective pair for every fixed c. Their intersection is empty; it
is already empty after the first three contexts. Consequently there is no
affine-realizability problem left to solve in this geometry.

The reason is stronger than incompatible common raw labels. On the accepted
branch u=0,a=b=1, for every mY,mR the complete N-to-q10 table is

| N code | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| q10 code for s=0 | 4 | 2 | 1 | 0 | 3 | 5 | 6 | 7 |
| q10 code for s=1 | 4 | 2 | 1 | 0 | 3 | 5 | 6 | 7 |

All32 unknown-sign pairs agree. A decoder of that one triple cannot return
two different unknown signs from these identical inputs. Allowing N to
depend on more known pads, independent random seeds or a nonlinear known-seed
function does not help this branch; N still cannot depend on unknown s.
For a seed-only random controller its conditional q10 laws on the two s
values are identical as well. This does not exclude a distribution-level
instrument using other retained physical fields or records.

A second exact identity, checked on192 accepted known-context/N pairs, is

    q10.A(s=0,N) XOR q10.A(s=1,N)=u.

It exposes an old-history-dependent response to the actual unknown sign.
The new source moves through the port bijectively, while the unknown-input
coupling depends on the old native background. Applying H only to the clean
q9 triple would omit precisely this retained dependence.

## Justification of the astronomical reduction

### Upper coupled cluster

Relative to upper Q, source offsets are Q at0, C at14, G at16, J at18,
Kplus/Kminus at signed transverse x=+/-1 and axial17, and N at20. All are
evolved together. Reflection survives only in transverse y. The closed
signed strip has budget20. At each layer its advance is a permutation of
its own triple forced only by lower layers; the same triangular argument
as the retained strip proof gives12*840^20. Actual P is divisible by it.
The evaluator retains signed x and does not add independently evolved
interacting upper sources.

### Lower origin/W three-layer front

Let F_ell(j) be the actual first-front value at (0,j,76+ell), time
j+76+ell, from origin (0,x,0) and W=111 at (0,-76,76). For ell=0,

    F_0(0)=H(H^75(0,x,0) XOR H^75(W)),
    F_0(j)=H(F_0(j-1) XOR [j AND75=0] H^(j+75)(0,x,0)).

For ell=1,2 the additional initial south-W term vanishes because75 ANDell
is nonzero. Thus F_ell(0)=H(F_(ell-1)(0)), and for j>=1,

    F_ell(j)=H(F_ell(j-1) XOR F_(ell-1)(j)).

This is the full native first-front recurrence: x-transverse and forward
neighbors and the old-local term arrive too late. The forcing of F0 has
period lcm(128,12)=384. Over that block its own state undergoes an
eight-symbol permutation, so F0 has period dividing384*840. Successively
F1 and F2 have periods dividing384*840^2 and384*840^3. Actual P is divisible
by the latter, hence it can be removed from all three required queries.

On the pre-collision slice R-1, W reaches exactly local points
(0,-9,8),(0,-10,9),(0,-11,10), requiring reduced queries
F0(176),F1(175),F2(174). It reaches none of the required R-2 slice. These
coupled values replace the isolated-origin contribution at those entries.
All subsequent upper/lower interactions are evolved together through the
full shrinking cubic q10 diamond. No old-local term or transverse neighbor
is discarded after the first collision.

## Controls and replay

Controls pass before the scoped verdict:

- 97,152 scalar-lane signed-upper comparisons with direct native recursion;
- 54 direct origin/W three-layer scalar comparisons at the actual gap76;
- exact period divisibility and three-entry/no-old-entry geometry;
- all1479 retained source and24 earlier-ready-region exclusions;
- exact piecewise-affine checks of all eight bank rays through L+1;
- preservation of qY,q7,q8 and all512 actual q9 rows;
- all64 own-N eight-value permutations;
- the64 pad pairs,192 unknown-sign derivative pairs and32 lost-input pairs.

Run `python3 checks.py --source-root <retained-native-root>` and compare
stdout with result.json; repeat with `python3 -O`. Both executions pass
byte-identically with explicit exceptions. PROVENANCE.json pins the source
data and proof dependencies. Large-time conclusions rest on the written
period arguments, not a simulation of P ticks.

The next viable route must retain actual s elsewhere in the physical phase,
use additional native processing/workspace, or demonstrate another accepted
boundary. The Native A distributed route is a separate candidate. No
physical premise/access adoption, native predicate or full reset, full
delayed-record law, arbitrary depth, A1 equivalence, A2 bound or composite
model is established here.
