# Physical state–operation compatibility: four source readings

**Status: CONFIRMING research, not a native execution.** This assessment
replaces the proposed native round in [draft PR #819](https://github.com/amaybaum/incompleteness/pull/819),
withdrawn before any owner designation of F. It supplies no new physical
compatibility principle, adopted theorem or receipt.

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
Phi_1 fixes the entire classical diagonal cone: D is diagonal and unitary, so
each diagonal matrix unit is fixed, and linearity extends this to the whole
cone. Native coordinate
filters preserve it; Phi_1's dual pullback fixes every coordinate test and
its nonnegative span.

For diag(d_0,...,d_3), the four diagonal product tests return exactly those
coordinates. Their positivity is equivalent to membership in the nonnegative
diagonal cone. PS therefore **admits classical theory and rejects quantum PSD
theory**. These comparisons bear on the protocol, filters, dual closure and
saturation. The classical comparison
does not claim ball tokens or availability of the balanced circuit: the
restriction of the actual map is its identity operation.

## Evidence and disposition

The universal conclusions above are written arguments, not finite-sample
claims or new Lean theorems, and that is their evidence level. The
separators −1/4 and −1/16 they use are the bridge audit's exact results,
replayed with its expected results. The drafting snapshot was main at
`dee3b5ae` after #818; the bridge audit's baseline remains `d69acffa`. The
cited Lean sources are unchanged between those snapshots.

The withdrawn draft's argument, probe, fixture checker and design controls
were developed at the research commit
[`b65c538a`](https://github.com/amaybaum/incompleteness/tree/b65c538a9a081881863a9c52cc89d1dea7d21383/verification/programmes/oi-qm/reconstruction/round-oi-state-operation-source-1)
and run by
[design CI run 38392163169](https://github.com/amaybaum/incompleteness/actions/runs/38392163169)
at that commit. Neither the commit nor the run's log is retained on main, so
they are provenance only and no conclusion here rests on them. The draft's
prototype workflow is not adopted. No F was designated, so the draft has no
execution or halted receipt.

LC is too weak, LO asserts the target, DT is its dual restatement, and PS
grants unearned quantum inclusion. None yields an independently sourced
physical principle. This closes only these four readings, not all possible
physical compatibility principles. A future candidate must satisfy the
[research criteria](../physical-state-operation-compatibility/criteria.md)
with a new independent source. Existing stage-6 and P0 statuses are unchanged.
