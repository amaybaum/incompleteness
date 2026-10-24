# Independent review: q7 readout and initial correction

24 October 2026. **ACCEPT the conditional native clean-readout construction.**
The uncorrected q7 result, its full nonlinear two-upper-source correction, the
native code `(0,0,y)`, and the stated source/readiness geometry are independently
verified. This is not an arbitrary-input clean socket, a reusable q2 interface,
a native reset, or a complete joint-history/access certificate.

The uncorrected files were supplied as published checkpoint
`6db981c1574ecc6938e9d55388f0ebeea34fab60`; the correction was subsequently
published at `49a391b9c8c3daf02e603e366cb5489d36677c14` with unchanged author
bytes. This review checked the exact local files, not remote content.
Exact reviewed bytes are bound by
`INPUT-HASHES.json`. No remote content was retrieved, no author file was edited,
and no repository action was taken. The independent review is specifically of
q7 and its correction. The broader k1–12 scan was replayed, not independently
rederived.

## Independent actual-scale result

The checker imports no author dynamics. It reuses only generic native-recursion
and geometry helpers from the prior independent v5 review, bound by SHA256, and
implements a separate signed-transverse, lookahead strip. Sixteen bit lanes
retain both values of u and all eight possible initial correction triples C.
The two sources are evolved together; their interaction from tick 7 is not
replaced by an isolated-pulse sum.

Use the old upper pulse as axial origin, with downward z positive. The new
source is at axial -14. Its incoming neighbor at the final update is queried
at axial `P+245`, time `P+259`, layer 14. The previously audited triangular
strip exponent `12*840^14` divides P, giving an exact reduction to axial 245
and time 259. The independent signed strip has 344 coordinates. It agrees
with direct two-source native recursion at 1,720 positions across all sixteen
lanes before being advanced to the required actual-scale reduced positions.

The independently computed incoming maps are:

| Initial C, in A/B/D order | u=0 incoming triple | u=1 incoming triple |
|---|---|---|
| 000 | 110 | 111 |
| 001 | 010 | 110 |
| 010 | 101 | 101 |
| 011 | 111 | 100 |
| 100 | 011 | 000 |
| 101 | 001 | 010 |
| 110 | 000 | 001 |
| 111 | 100 | 011 |

Each column is a permutation. The unique inverse choices producing the desired
net incoming change are C=000 for u=0 and C=101 for u=1. Thus the required
initial payload is exactly `(u,0,u)`. The old local triple at q7, time N-2,
is independently 111 for both u, and is independent of C by finite speed.

The checker then assembles the entire pre-collision fields from the full
two-source strip and the actual giant-integer lower-front parities, and
performs all eight native updates R through R+7. It does not merely inject
the proposed delta into the final update. All 32 assignments of x,u,mY,mR,p
agree with the original and corrected qY diagnostic formulas. A separate
q2.A-only intervention is also evolved and checked in all 32 assignments.

## Why the correction works, and what it does not do

For old local triple W, neighbor sum V and original output
`C_out=W XOR H(V)`, a neighbor change `(u*W.A,0,u)` changes the output by
`(0,u,u*C_out.A)`. The checker verifies this identity for all 128 choices of
W,V,u. Here W.A=1 and the original qY diagnostic A field is
`x(1-u)(1-p)`, whose product with u is zero. Therefore the corrected whole
diagnostic triple is

```
(x(1-u)(1-p), (x XOR u)(1-p), p).
```

On native inputs p=x XOR u=y this is exactly `(0,0,y)`. For arbitrary qY
intervention p the extra fields need not vanish. D=p is universal; a clean
whole arbitrary-input socket is not established.

Replacing only q2.A instead gives

```
((x XOR p2)(1-u), x XOR u XOR p2,
 x XOR xu XOR p2 XOR xp2 XOR xup2).
```

For x=1,u=0,p2=0 the corrected output is111, so D is not p2. None of its
fields or complements is uniformly p2. The new construction reads the
original qY-initiated wave; it does not prove reusable q2-output-to-input
transfer. Information elsewhere in the reversible lattice is not removed.

## Source, readiness and history geometry

Adopt only the q7 initial preparation, with q7=(0,S,d+7), N=R+7 and
`f=(0,S,S+2d+14)`. The k8–12 scan preparations are alternatives and are not
simultaneously imposed. The new source is an explicit exception to q7's
current ready-zero prescription: f has distance N from q7, hence lies on
the current boundary and outside the previous ball of radius N-1. Relative
to the uncorrected q7 preparation, a formerly zero coordinate is changed.

The correction payload uses only the already supplied apparatus seed u. It
contains neither unknown x nor diagnostic p nor precomputed y. Copying u into
two initial fields adds a supplied initial correlation and one controlled
source location, but no new independent random bit. No native initializer
for this correlation is supplied or inferred.

The source export was checked by its existing SHA256 digest, without copying
it into this review. All 1,479 old source positions remain outside or on the
q7 boundary; the only inherited boundary entry is the unknown origin. The
new f overwrites none. The three selector controls remain boundary sources,
the old upper pulse is inside, the previous unknown is outside the previous
ball, and the opposite pulse and remote blocks are outside. The unwrapped
cones fit the inherited torus; no global checkerboard assertion on its odd
size is needed.

The all-index distances of protected frontier families from q7 exceed N by:

| Family | Positive slack, for index j>0 |
|---|---:|
| M_j | j |
| N_j | 9T+j |
| Selector X/Y/R frontiers | j |
| Selector Z frontier | 3T+j |

The new f is disjoint from these banks: the near families have zero or
negative z, and the remote banks have separated x. Thus their prescribed
independent fair coordinates are not overwritten by the correction or pinned
by the new ready ball.

The reviewer checked all fifteen inherited current ready balls, including
qY, q2, optional q3 and remote centers: f is outside every ball and farther
than N from every center. Consequently **the added correction source** cannot
change those receiver histories through N relative to the uncorrected q7
preparation. It also cannot change the earlier sidecar, or outward endpoint
k<=6 at its R+k deadline. No unchanged-output claim is made for k8–12.

At N-1 only q7+e_z can depend on f; the other five neighbors are distance N+1
from f. The old local N-2 term is also unaffected. Each lower source is
distance 2N from f. Along the incoming ray, at height h>0 above q7, the
lower-source distance is N+h and the available time is N-h. Thus no lower
source, qY intervention or q2 intervention can enter that incoming neighbor's
past cone. Its map depends only on the full upper/C dipole, as calculated.

## Access, resources and remaining boundary

The new source first reaches q7 at N, so **every earlier q7 prefix is
unchanged**. In particular the prefix at R-7 is `(u,u,1)` and reveals u.
The receiver must remain private until its designated read under the supplied
access rule. No native shutter, clock or access-closure construction has been
verified here.

Keeping the seven old public ports exposed through R+7 requires the inherited
147 extra independent fair bits beyond R (105 beyond the depth-two window).
The geometry preserves the reserved frontier families; this review does not
independently close the full inherited joint-frontier theorem. The initial
ready extension can affect later old-port dynamics, so that theorem remains
relevant even though the added correction source itself is causally excluded
from their histories through N.

There is no new herald or second reset. Existing success/failure probabilities
are inherited claims, not recomputed or upgraded by this endpoint proof.
No failed branch is removed. A common native terminal code has now been
constructed, but a complete joint-record law, arbitrary-input interface,
post-Y conditional resource preparation, native access mechanism and reusable
reset remain open. The broader inherited transport-proof audit also remains
open.

## Reproduction

Place this directory at `outward_v6/review/` alongside the published outward
files and the prior `six_source_v5/review/checks.py`. Then run:

```
python3 outward_v6/review/checks.py
python3 -O outward_v6/review/checks.py
```

The isolated workspace layout is also supported. The checker reads the
existing source geometry, verifies all eight author-file hashes, and binds
the independent v5 helper to SHA256
`467fbff795407b2a2744465166ac6fd0958dbef768606b2a40a9ed6b97120728`.
It writes no files and needs only Python's standard library. Independent,
author-scan and author-correction replay groups each have byte-identical
normal/-O outputs. `INPUT-HASHES.json` and `SHA256SUMS` identify the exact
reviewed author bytes and the delivered review artifacts respectively.
