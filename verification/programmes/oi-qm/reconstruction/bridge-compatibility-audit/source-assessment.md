# Physical state–operation compatibility: four source readings

**Status: CONFIRMING research, not a native execution.** This assessment
replaces the proposed native round in [draft PR #819](https://github.com/amaybaum/incompleteness/pull/819),
withdrawn before any owner designation of F. It supplies no new physical
compatibility principle, adopted theorem, main CI job or receipt.

The independently given preparation cone C is closed and convex, with
SEP ⊆ C ⊆ maxCone. The inventory retains the explicit finite-protocol
premises, guaranteeing every stopped map Phi_k by `finite_protocol_spectator`.
No fullClass-only replacement channel is used. Negative fixtures are the
bridge audit's K_B and stage-6 K(Z_F); positive comparisons are quantum PSD
and classical diagonal cones.

## Restricted rank-one filter/readout consistency (LC)

For block-positive X and a unit local vector a, the conditional matrix
sigma_a=(<a| tensor I)X(|a> tensor I) is PSD: its quadratic form at b is the
nonnegative product pairing at a tensor b. The rank-one filter therefore has
output P_a tensor sigma_a in SEP, and hence in C. The same proof holds on
the other token, including zero branches. Complementary readout weights are
nonnegative and sum to Tr(X).

For any PSD product test A tensor B, its Phi_k pullback is a convex combination
of A tensor D†BD and A tensor B, both PSD products. Thus Phi_k preserves
maxCone and local readout validity even when it fails to preserve C.

LC holds for every cone in the retained interval, for every sharp direction.
Both fixtures satisfy LC but fail preservation under the uniformly available
Phi_1, with separators −1/4 and −1/16. This proves only that **restricted
rank-one filter/readout consistency is insufficient**. It does not extend
that conclusion to consistency under local operations generally.

## General available one-token operations (LO)

The constructed operation is Phi_1=id tensor phi_1, where
phi_1=(5/8)Ad_D+(3/8)id and D=diag(1,(3+4i)/5). Requiring admitted preparations
to remain admitted under every available one-token operation already requires
preservation under this witness. Both fixtures violate that named clause.

LO directly asserts the desired local state–operation compatibility; it does
not independently explain it. Further local operations can make LO stronger
than preservation under only the stopped sequence. No equivalence with that
single map is claimed. LO includes every guaranteed Phi_k and implies the
third-axis flow clause for closed cones by the equivalence in [result.md](result.md).
It supplies neither the J-conjugate clause nor an independent physical source.

## Complete dual-test closure (DT)

Finite-dimensional separation gives C=C** for a closed convex cone. For a
real-linear map F, <F*e,x>=<e,Fx> proves

    F(C) ⊆ C  iff  F*(C*) ⊆ C*.

Closure of all complete joint tests under protocol pullback is preservation
in dual language. It needs neither self-duality nor C=Q3, but fails the
disguise test as an independently sourced principle. A smaller available
test family needs a separate completeness argument; product tests alone
identify maxCone, not C.

## Product-test saturation (PS)

Declaring every product-positive vector to be a preparation gives maxCone
and already forces Q3 ⊆ C. That violates the widened input gate without
self-duality. It also rejects the quantum PSD positive comparison: the
block-positive defect e_(1,1) has eigenvalue −1/8 and lies outside PSD.
Excluding the fixtures this way supplies no new selection of quantum states.

## Classical comparisons bearing on the actual claims

Conjugation by diagonal I tensor D fixes every diagonal matrix, so the actual
Phi_1 fixes the entire classical diagonal cone. Exact checks on the four
diagonal matrix units extend by linearity to the whole cone. Native coordinate
filters preserve it; Phi_1's dual pullback fixes every coordinate test and
its nonnegative span.

For diag(d_0,...,d_3), the four diagonal product tests return exactly those
coordinates. Their positivity is equivalent to membership in the nonnegative
diagonal cone. PS therefore **admits classical theory and rejects quantum PSD
theory**. These controls test the protocol, filters, dual closure and saturation;
the unrelated bit-flip comparison has been removed. The classical comparison
does not claim ball tokens or availability of the balanced circuit: the
restriction of the actual map is its identity operation.

## Evidence and disposition

The universal conclusions above are written arguments, not finite-sample
claims or new Lean theorems. Exact design evidence is pinned at
[`b65c538a`](https://github.com/amaybaum/incompleteness/tree/b65c538a9a081881863a9c52cc89d1dea7d21383/verification/programmes/oi-qm/reconstruction/round-oi-state-operation-source-1).
Its argument, probe, independently implemented fixture checker and design
controls remain on that research commit. The drafting snapshot was main at
`dee3b5ae` after #818; the bridge audit's baseline remains `d69acffa`. The
cited Lean sources are unchanged between those snapshots.

The corrected self-test passes 1,181 exact controls (640 readout and 320
filter cases), the separate 53-control fixture check, and rejects all 14
mutations (four construction and ten policy mutations).
[Design CI run 38392163169](https://github.com/amaybaum/incompleteness/actions/runs/38392163169)
passed at the pinned commit. This is disclosed post-review design validation,
not a native F/E attestation. Original bridge scripts and saved evidence
remain unchanged; the bridge workflow continues their separate replay.

The prospective native workflow selects the PR head SHA rather than GitHub's
synthetic merge HEAD. That corrected prototype remains research-only; no
additional job is adopted on main. No F was designated, so the abandoned
draft has no execution or halted receipt.

LC is too weak, LO asserts the target, DT is its dual restatement, and PS
grants unearned quantum inclusion. None yields an independently sourced
physical principle. This closes only these four readings, not all possible
physical compatibility principles. A future candidate must satisfy the
[research criteria](../physical-state-operation-compatibility/preregistration.md)
with a new independent source. Existing stage-6 and P0 statuses are unchanged.
