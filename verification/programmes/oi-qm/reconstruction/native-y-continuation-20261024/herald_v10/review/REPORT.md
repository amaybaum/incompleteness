# Separate-author review of the synchronized remote Y herald

Author checkpoint: `25220128c3c7991e4c22c917af56b68c02ab8051`, under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/herald_v10/`.
Verdict: **accept the conditional remote-herald and fair-z construction;
no blocking findings**. This internal separate-agent review certifies no
local three-sign controller, complete carrier or reusable interface.

## Inputs and independent execution

The immutable published report, checker, provenance, result and checksum
blobs match the local review inputs. The manifest verifies and both author
replays match result.json exactly. The retained upstream herald JSON also
matches its published blob `e48fb2f99382336489537c5ae7d0ada4a2e04972` and the
claimed SHA-256 `406befa2c8d1f663856a78ca6cb632e9c61d1233b02a9d532c7cb43d6261ce64`.
The review checker imports no author code or predecessor compiler.

An independent evaluation of the first 2,684 retained steps gives (G,0,0)
on every one of the 32 seeds, with acceptance counts 5,0,3,2 in order
00,01,10,11. The constant word (2,3,3,3,3,7) is identity on all eight register
states. The five-dimensional affine coefficient span is verified. The
source transform has unit diagonal, so retaining all transformed rows also
retains those seed dimensions; z supplies the sixth independent dimension.

With actual P=12*840^185, m=(P-2424)/6 is a nonnegative integer and
2684+6m+2=P+262=R+9 exactly. Both final H applications are necessary for
the stated herald phase. Since L=1 mod3, a pure-A z source gives the raw
triple (0,0,z). Omitting one final H or choosing the wrong initial z field
fails the complete-triple check. No P change or inferred 2,700-layer period
is used.

## Arbitrary-length source formula

The three wing sources have coordinates (L-1-q,+/-[q+1],0) and
(L-1-q,0,q+1), translated by the remote center, for every 0<=q<L. Each
lies on the current radius-L boundary and outside the previous radius-L-1
ball. This includes q=L-1; its terminal-axis contribution cannot be dropped
merely because the desired last control is zero.

On the first front, shortest paths from different wings intersect only on
the spine. Before that intersection, each wing carries one rotating field,
so H's nonlinear product vanishes and the scalar recurrence is Pascal XOR.
At spine step t the contribution from row q has coefficient binom(t,q) mod2.
Lucas parity identifies the contributing q as binary subsets of t. The
subset-zeta transform is involutory over characteristic two: the coefficient
of a proper subset is an even power of two, while the diagonal is one.
The author's A_w(q) formula consequently produces the desired B_w(t) at
every step, including the terminal zero input. Rotating the field by t
puts it in component (w-t) mod3. The three injections combine to g_t, and
the native spine applies exactly H(state XOR g_t).

The old-local slice is blank on this first front. Every source is initially
on the radius-L boundary, so the full receiver triple is zero at every
earlier tick. The proof is valid for any finite L; its application to the
astronomical L is a written combinatorial proof, not a bounded-run extrapolation.

The independent checker constructs the inverse profile using a binary-zeta
butterfly, rather than the author's submask loop, then runs the complete
native wing/spine recurrence at bounded deadline 2,686. It checks 85,952
seed-level injections and obtains (0,G,0) for all 32 seeds. Separately,
full six-neighbor three-dimensional native recursion at lengths 3,5,7
reproduces arbitrary affine programs for 96 seed cases and verifies every
blank prefix. Direct binomial coefficients check each small source row.
Deleting q=L-1 fails all three source-omission controls. This exercises
the terminal-row point independently of the abstract word evaluation.

## Geometry and joint law

The existing source/ready/bank envelope is |x|<=13R. The new ready cones
occupy |x|>=47L, with centers +/-48L, and have separation 96L>2L. The
new source hemisphere is x>=48L, while the z source is on the opposite
boundary. Thus neither new ready pins nor source values consume an old
frontier coordinate or change an old informative deadline; old sources
cannot reach the new receivers through L. The source formulas' endpoint
bounds establish these inequalities for every indexed source, not merely
sampled rows.

All relevant x coordinates are in [-49L,49L]; y,z magnitudes have a smaller
bound. The chosen side 256L+64T+1 exceeds twice every relevant coordinate
difference. The integer geometry checks therefore support a single no-wrap
lift throughout all involved cones. This enlarges the finite resource
geometry while leaving P and the old local dynamics unchanged.

The remote herald port reveals only a blank prefix and (0,G,0) at L.
The private z port has a blank prefix and remains inaccessible until the
specified terminal access. The old seven-stream triangular proof still
applies because its bank is free and remote additions are in its complement.
Its complete noise word is independent of the new seed bank before either
herald branch. On the stated independent seed prior, the new G leaves
(a,b) weights 5:3:2 and z independent fair jointly with them.

Independent enumeration retains all 64 new seed assignments: 20 successes
and 44 failures. Rejected counts are 3,8,5,6 for each fixed z. Sharing z=a
retains a fair z marginal but changes the joint successful law by TV=1/2,
and the checker rejects it. Conditioning on G intentionally changes the
(a,b) law; the result does not assert that used a or b remains an independent
fair bit after heralding.

A later joint construction must use the same a,b in the local masks and
remote source encoding, verify those local copies' geometry, and establish
the complete physical carrier law. Those correlations are not extra fresh
resources. This review assumes no unreviewed local-controller formula and
proves no post-failure carrier, later-time public history, unrestricted
access policy, native preparation of fair resources or full equivalence.

## Replay

From this retained review directory run `python3 checks.py` and
`python3 -O checks.py`; both match result.json. They use the existing
hash-pinned `parallel_v3/direct_reset/herald.json`, with an optional
`--herald path` for sparse checkouts. Normal and optimized outputs match
byte-for-byte; all controls use explicit exceptions. INPUT-HASHES.json pins
the author inputs and SHA256SUMS covers the review artifacts.
