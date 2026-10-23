# Spectrality: an externally motivated candidate, not a compatibility derivation

**Status: research candidate for review; the K(Z_F) exclusion is conditional
on H3; source and preservation implication UNRESOLVED.** No native control plane, F designation, adopted axiom or receipt.
This exploratory screen follows the [research criteria](criteria.md)
and the [four-reading assessment](../bridge-compatibility-audit/source-assessment.md).
The arguments were constructed before the scripts were run; computations
check disclosed certificates, not blind predictions. Classification under
AGENTS §A.31: ELABORATING, with no claim to a new physical-source result.

Snapshot: bridge research after `c83aa437`; main at
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`. The cited Lean sources and the
two fixtures are unchanged. Historical stage-6 satisfied/failed/unreached
counts and their evidence levels are retained, not upgraded by this screen.

## Candidate and its source

Barnum, Müller and Ududec, *Higher-order interference and single-system
postulates characterizing quantum theory*, NJP 16 (2014) 123029,
[version 4, §III, Postulate 1](https://arxiv.org/html/1403.4147v4#S3), state:

> “Every state lies in some classical subspace”.

Here a classical subspace is the convex hull of a frame of perfectly
distinguishable pure states. Apply only that postulate, called **SP** here,
to the independently specified normalized pair preparation space
Ω={X∈C : Tr X=1}. Explicitly, every X∈Ω must have a finite decomposition
X=Σ p_i X_i, where p_i≥0, Σ p_i=1, the X_i are extreme points of Ω, and one
measurement distinguishes all X_i with certainty. Its effects are linear,
nonnegative on C, and sum to the normalization functional.

This is a state/test property, motivated in that paper by informational and
thermodynamic considerations. It is not a statement about a flow or available
operation. The source treats it as a postulate; it does **not** derive it from
OI, and this record supplies no such derivation. Applying it to the physical
pair is a new, still unsourced bridge premise. Strong symmetry, homogeneity,
purification, all-effects availability and the paper's other postulates are
not imported. Matrix spectral decomposition is not SP's definition.

For exclusion, allow even the largest possible effect interval [0,I] in C*.
Failure with this enlarged test set entails failure with any physical subset;
no no-restriction premise is required. No operation is used in the exclusion
proofs, so fullClass inventory size is irrelevant. The earlier uniformly
available Phi_1 remains the independent preservation failure, not a new SP
assumption.

| Premise or obligation | Status in this screen |
|---|---|
| Closed convex C, ball products, C⊆maxCone, trace normalization | Common domain, as in the bridge audit |
| Full finite-protocol availability premises | Retained at their original status; no extra operation used |
| K_B=SEP+R+ B | Same explicit fixture; no CNOT or self-duality assumption |
| K(Z_F)=(Q3∩Z_F*)+cone Z_F | Same explicit fixture; product and maxCone clauses proved in the bridge audit |
| Trace self-duality (H3) of K(Z_F) | Condition of the K(Z_F) exclusion; its stage-6 written proof is not retained on main and not verified here |
| SP on the physical pair | External postulate; not derived from existing OI premises |
| SP ⇒ guaranteed stopped-map preservation | UNRESOLVED |
| SP with extra H3/CNOT premises | Stronger-lane implication and input gate UNRESOLVED; not used as a baseline |

Stage-6 provenance, at the off-main commit
`e7d380fcb9881e3063243aaa149e85be3cd0a914`:
[integration §§2–4](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/INTEGRATION-NOTE-STAGE6.md)
(blob `22261d7c8f5963b45bdabefab8badae30a23d250`) and
[R6 reassessment](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/R6/REASSESSMENT.md)
(blob `04e35df63bade710994d57b317bc0a599551277c`). These two files record H3
for K(Z_F); the complete written proof they rely on is `pt/T6/TEST.md` §3.3
at that commit (blob `335cdc08701306d77670b6836e8081e244068de4`). None of
the three is retained on main. From that commit, the evidence-retention archive in main's history
(`verification/audits/evidence-retention/objects/` at `48b18ac5`) retains the R6 tree and `R6/NOTES.md` (blob `62cdd79871c0fd78215be69f4d4ea630e178273d`),
whose N5 entry records that the stage-6 H3 certificates passed but does not
contain the proof.
Current availability is the existing `finite_protocol_spectator`, and the
coordinate representation is the adopted Pauli dictionary; neither derives SP.

## K_B violates SP: two close product rays

Let u=(12/13,5/13), p=|00>, q=u tensor u and
X_B=(|p><p|+|q><q|)/2. This is a normalized member of SEP⊆K_B of rank two.
For a vector αp+βq, the determinant of its two-by-two coefficient matrix is
(25/169)αβ. Thus the only product rays in its support S are p and q.
The Bell vector is outside S. The PSD support-complement projector F_B has
Tr(F_B B)=144/313>0 and Tr(F_B X_B)=0.

Every K_B term is PSD. A decomposition of X_B into K_B states must therefore
stay in S; it cannot contain the Bell generator, and its separable pieces
can use only p and q. Its face has exactly those two pure preparations.

For any maximal allowed binary effect E, both E and I−E are nonnegative on
every PSD product. Fixing one token therefore gives an ordinary qubit effect
0≤E_local≤I on the other. Its expectation difference between |0> and u is
at most their trace distance, 5/13. Telescoping from (0,0) through (u,0)
to (u,u) bounds every joint effect difference by 10/13<1. Consequently p and
q cannot be perfectly distinguished, even with all mathematically positive
effects. The nontrivial mixture X_B has no frame decomposition: K_B fails SP.

This also proves SP's failure for SEP itself; the Bell exclusion step is then
unnecessary. This is a universal effect bound, not a sample of measurements.

## K(Z_F) violates SP if it is trace self-dual

Rescale the historical defects as z_i=4e_i, so Tr z_i=1. Set
P_i=I/2−z_i. These are four orthogonal rank-one Bell-type projectors summing
to I. Their normalized eigenvectors form the unitary U whose i-th column is
2P_i|00>. This follows directly from the audit's actual Pauli formulas.

In these Bell coordinates choose orthonormal vectors

    v=(√3/2, 1/(2√3), 1/(2√3), 1/(2√3)),
    w=√(5/14) (0, 1, (−3+4i)/5, (−2−4i)/5).

Write V for the isometry with columns Uv, Uw; P_S=VV† and F=I−P_S.
The squared Bell projections are
r_i=Tr(P_i P_S)=(3/4,37/84,37/84,31/84). All are positive; only r_1 exceeds
1/2. Since Tr(F z_i)=r_i>0, F is nonnegative on the whole cone, and any
state in its zero face has no defect-ray component. Such states are PSD
and supported in S.

The normalized state X_Z=(2/3)|Uv><Uv|+(1/3)|Uw><Uw| belongs to the cut PSD
base: its pairings against z_i are (0,41/126,41/126,22/63). The exposing test
F+z_1 is in the dual cone and vanishes on X_Z. Its normalized zero face is
exactly the disk of two-by-two PSD matrices, in the v,w basis, with diagonals
(2/3,1/3). The other cuts are automatic since r_j<1/2 for j>1. Its pure
points are rank-one vectors a with |a_1|²=2/3, |a_2|²=1/3; X_Z is not pure.

Assume H3, trace self-duality of K(Z_F). Suppose two pure points a,b in
this disk were perfectly distinguishable. By H3, a binary effect E and I−E
belong to K(Z_F). Compress their PSD-plus-defect decompositions to S.
All z_j with j>1 compress to PSD matrices, because their eigenvalues are
1/2 and 1/2−r_j. The exceptional compression is

    Z=V†z_1 V=diag(−1/4,1/2).

Hence E_S=H+λZ and (I−E)_S=J+μZ for H,J PSD and λ,μ≥0. Put t=λ+μ.
Then H+J=diag(1+t/4,1−t/2), so 0≤t≤2. A zero probability at a implies
Ha=0; a unit probability at b implies Jb=0, since both have zero Z pairing.
It follows that a†(H+J)b=0. But the triangle inequality gives, for all their
phases,

    |a†(H+J)b| ≥ (2/3)(1+t/4)−(1/3)(1−t/2)
                 = (1+t)/3 > 0.

This contradiction rules out every distinguishable pair in the exposed face,
even using all dual effects. A frame of size at least two would contain such
a pair; a singleton cannot decompose its mixed center. Thus, under H3, X_Z
has no SP decomposition and K(Z_F) fails SP. The exclusion is conditional on
H3, whose stage-6 written proof is not retained on main and is not
re-verified here; the finite checks below do not establish self-duality.

## Positive comparisons and the input/disguise gates

Quantum PSD satisfies SP by the ordinary spectral theorem: orthogonal
eigenprojectors are both pure states and distinguishing effects. Both displayed
witnesses have explicit quantum spectral decompositions checked exactly.
Classical diagonal states decompose into coordinate preparations, distinguished
by coordinate readouts. SP therefore passes both required comparisons.

SP does not, in the common domain, already grant Q3⊆C. The cone
C_co=Γ(Q3), with Γ partial transpose on the second token, is order-isomorphic
to PSD. Γ preserves trace and the trace pairing, so transformed orthogonal
projectors give SP decompositions and distinguishing tests. C_co contains
all PSD products and lies in maxCone: its pairing with a product equals a
PSD pairing with the transposed local factor. Yet B is absent because Γ(B)
has eigenvalue −1/2. This is an input-gate witness, not a stronger-lane model:
C_co fails the native CNOT requirement. The product state |+⟩⊗|0⟩ is fixed
by Γ and so lies in C_co; CNOT maps it to B, which lies outside C_co.
Adding H3/CNOT/extra reconstruction postulates needs a separate implication and gate audit; none is silently added.

The target third-axis flow does not imply SP: SEP is invariant under all
local unitary flows and all stopped maps, but the X_B argument excludes its
SP decomposition. Thus SP is not equivalent to that flow or to preservation
of the stopped family in the common domain. No inference from this direction
to SP ⇒ preservation is made. That reverse implication, the J-conjugate
clause, OI⁺-1 and a physical source for SP remain unresolved. Excluding two
cones cannot substitute for proving any of those implications.

## Evidence, reproduction and limits

[spectrality_check.py](spectrality_check.py) checks 79 exact certificates and
rejects four mutations: distinguishable product inputs, the wrong defect,
the wrong cap and an indefinite quantum comparison.
[spectrality_independent.py](spectrality_independent.py) uses a separately
written standard-library rational complex matrix implementation: 76 controls,
no import of SymPy or the first checker. From the actual Pauli defects, both
compute the Bell support gap 144/313, the K_B effect bound 10/13 (the
independent checker as the sum of the two local Helstrom gaps), the
projection weights, the cut pairings and the K(Z_F) overlap bound (1+t)/3
(the independent checker from the compressed defect and the face diagonal,
on 0≤t≤2), and both check the CNOT witness for C_co. They verify
certificates supporting the written proofs; they do not computationally establish all effects, all decompositions
or a source implication. Same assistant, distinct implementations, no claim
of independent authorship.

Run each from the repository root with `python3 -I -B` (the first requires
SymPy 1.14.0). Their expected results,
[spectrality-output.txt](spectrality-output.txt) and
[spectrality-independent-output.txt](spectrality-independent-output.txt),
name their recipe, form and script digest in a header. The
`bridge compatibility research` workflow replays both beside the bridge
checks on every push and pull request touching these two record
directories, `BridgeFiniteProtocol.lean` or the workflow itself. It is a
research replay, not a native F/E attestation.
The first matrix self-test rejected its wrong-defect mutation at rank/trace,
while the harness initially expected idempotence to fail: the wrong matrix
is a rank-three projector. Correcting that expected failure label yielded
the green rerun; no verdict was printed by the failed harness.

**Outcome:** SP is an externally motivated candidate that excludes K_B, and
K(Z_F) conditionally on H3, by a different, static state/test clause, and
passes the two positive comparisons. It is not yet a physical compatibility
principle established from OI, and no preservation theorem is supplied. The next obligation is the
source/implication question, not a native execution of these exclusion checks.
Existing K2, K3, arbitrary-carrier and P0 classifications remain unchanged.
