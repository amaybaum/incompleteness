# Finite reconstruction: exact reachability and the descent interface

Research/design record, 2026-10-13. Base D: `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.
This is a written all-k argument, an exact three-token design check and
compiled research Lean sources for the conditional all-k theorem. It is neither
an adopted Lean theorem nor a native round execution. No F is designated. This
directory is on a research branch and is not on main; until it lands there,
nothing in it is an authoritative reference. References outside this directory
that are not adopted on main are marked as off main.

The source drafts are [#829](https://github.com/amaybaum/incompleteness/pull/829)
at `625f853ff70546f6e8d56d22fad15e968ad48354` and
[#823](https://github.com/amaybaum/incompleteness/pull/823) at
`c83954a5b7b8971eb3e5296912e403423fe0167e`, both open pull requests and off
main. The first proposes a k-token table theorem; the second compresses
implementation repertoires. They concern different objects and need a separate
interface.

## 1. Carrier and premises

Put H_k = (C²) tensor k, with binary strings as an orthonormal basis, and let
V_k be its real Hermitian matrix space. The table carrier in #829 is
W_k = R^{ {0,1,2,3}^k }. With sigma_0 = I and the three Pauli matrices, set

    P_mu = tensor_i sigma_(mu_i)
    dictionary(w) = 2^(-k) sum_mu w_mu P_mu.

Pauli orthogonality gives Tr(P_mu P_nu) = 2^k delta_(mu,nu), so the inverse is
w_mu = Tr(A P_mu). Hermitian A gives real coordinates. This is a real-linear
isomorphism; the scalar empty tensor handles k = 0. Its physical use assumes
the proposed locally tomographic k-token carrier, rather than deriving it.

Translate the proposed hypotheses to an exogenously specified C subset V_k:

1. C contains tensor products of trace-one qubit PSD states.
2. C is closed under addition and nonnegative real scaling.
3. Every A in C has nonnegative pairing with every product of local positive
   effects; equivalently it has nonnegative expectation on every product vector.
4. Conjugation by CNOT(i -> j) preserves C whenever i < j.
5. At every token j > 0, the entire third-axis rotation flow and the cyclic
   Pauli-axis rotation preserve C.

For the equivalence in item 3, scaled rank-one local projectors give one direction
(compiled for tables as `lorPair_nonneg_of_maxConeTab`, used in
`tableCone_eq_psd_of_drive_maxConeTab`, and for Hermitian matrices as
`prodVec_nonneg_of_maxConeTab`). Conversely, spectral decompositions of each
local effect expand the product effect into a finite nonnegative sum of product
rank-one projectors: compiled as `maxConeTab_of_prodVec_nonneg`, through
`lor_blochH_decomp`, which writes each forward-cone vector as a nonnegative
combination of two Bloch vectors, and `lorTests_of_blochTests`, which replaces
the tokens one at a time. `maxConeTab_iff_prodVec_nonneg` states the
equivalence with these two witnesses. No global PSD assumption is used. Effect
normalizations only introduce positive factors.

The desired conclusion is C = PSD(H_k). Closedness, self-duality, fixed-gate
density and full unitary invariance are not premises of the argument below.

## 2. Exact elementary actions and their inverses

The landed `EqvK2Generation.conjInv_idle` establishes the local algebra needed
here: full third-axis flow plus the cyclic rotation gives every SU(2) action on
the driven token by an exact Euler word. The same 2-by-2 identities act on an
arbitrary spectator space. For qubit spectators and every token count, the
research module `FiniteReach.lean` proves the controlled form used below
(`isWord_suFam`, `isWord_lift`).

All generator conjugations have available inverse words. CNOT squares to I.
Rotation inverses use negative angles. The cyclic action has order three (its
SU(2) lift may cube to a scalar), so its conjugation inverse is its square.
Consequently preservation under the generators entails preservation under a
finite word and under the inverse word. The words also contain unit scalars:
the third-axis flow diag(1, e^(it)) has determinant e^(it), and a unit scalar
times it gives each diagonal special unitary. Scalar conjugation is the
identity, so unit scalars need no preservation hypothesis. This does not assert
physical availability of any of these operations; preservation is the given
hypothesis.

## 3. A finite multiplexor identity

Let R(theta) be a one-parameter SU(2) group with X R(theta) X = R(-theta), for
example a real y-rotation or a diagonal z-rotation. The inventory supplies the
diagonal family directly. The real family is its conjugate by the cyclic action
on the target. That action is the same in every control branch, so conjugation
acts branchwise and a real-rotation multiplexor is the cyclic conjugate of a
diagonal one. Take n controls, a later
target, and a cyclic binary reflected Gray order
g_0 = 0, ..., g_(L-1), g_L = 0, L = 2^n. Consecutive strings differ in one bit.
For n = 0 use a single local rotation with no CNOT. For n > 0 use this chronological
circuit:

    for j = 0,...,L-1:
        R(alpha_j) on target
        CNOT(control bit changed between g_j and g_(j+1) -> target).

For a fixed control word b, move all X factors to the left using the displayed
identity. The remaining target flip is b dot g_L = 0. The target rotation is

    R(sum_j (-1)^(b dot g_j) alpha_j).

The matrix M_(b,j) = (-1)^(b dot g_j) is a column permutation of the Walsh matrix.
Character orthogonality gives M M^T = L I, by summing separately over each binary
coordinate. Thus any prescribed angles theta_b are realized exactly by

    alpha_j = L^(-1) sum_b (-1)^(b dot g_j) theta_b.

All control indices precede the target. No reverse CNOT and no operation on the
first token is needed. This is a finite identity, not an approximation argument.
The compiled proof realizes the same multiplexors by a different finite word:
every real function of the control word is generated from constants by sums and
by multiplication with single-bit signs, and each such sign is conjugation by
the CNOT from that bit to the target. It does not use the Gray order.
Every branch SU(2) matrix has an Euler decomposition into three one-axis rotations.
Apply the construction to the three branch-dependent angle lists and concatenate
the three multiplexors. This realizes every block diagonal SU(2) family controlled
by earlier tokens. The Euler order must be kept consistently with circuit order.

The exact checker builds its Gray circuit from rational rotation entries and
computes the independently prescribed block matrices from signed products, rather
than evaluating the Walsh formula twice. Its open-cycle mutation checks the final
return to zero, which matters even though the controls never change.

## 4. Universal pure-state reachability

For a vector x on k tokens, split it by the last bit. For each earlier word b,
put v_b = (x_(b,0), x_(b,1)), r_b = sqrt(|x_(b,0)|² + |x_(b,1)|²). When r_b > 0,

    U_b = [[x_(b,0), -conj(x_(b,1))],
           [x_(b,1),  conj(x_(b,0))]] / r_b.

This is SU(2) and maps (r_b,0) to v_b. When r_b = 0, v_b = 0 and take U_b = I.
The multiplexor in section 3 therefore maps r tensor |0> to x exactly.
Apply the same argument recursively to the (k-1)-token vector r. At k = 1,
start with the arbitrary first-token pure state represented by r (including its
phase if x itself has only one token). At k = 0 there is only a scalar ray.

For nonzero x the result is

    x x† = c U (P_first tensor |0><0| tensor ... tensor |0><0|) U†,
    c = ||x||² >= 0,

where U is a finite word in the proposed generators. For x = 0 use scaling by
zero. The first token is free in the initial product preparation and is never
driven. This matters: the argument proves the pure-state reachability needed
for the cone theorem; it does not prove arbitrary unitary synthesis under this
asymmetric gate inventory.

For comparison, [Barenco et al. (1995), section 8](https://arxiv.org/html/quant-ph/9503016v1#S8)
prove exact universality with all one-qubit gates and XOR gates. Their gate
inventory is stronger than this asymmetric inventory. We do not substitute
their full universality theorem for the preceding reachability argument or
replace the continuous local flow with a fixed dense gate set.

## 5. The two inclusions and both directions

**Lower inclusion.** Products, scaling and generator preservation put every
x x† in C by section 4. The finite spectral decomposition of a PSD matrix is a
sum of such matrices, so addition gives PSD(H_k) subset C. This direction does
not need the product-test upper bound.

**Upper inclusion.** Let A be in C and choose any x. Section 4 gives x = sqrt(c) U p
up to an irrelevant scalar phase, with p a unit product vector. The inverse-word
argument gives U† A U in C. Product-test positivity implies

    x† A x = c p† U† A U p >= 0.

Thus A is PSD. This direction needs neither product-state inclusion nor cone
closure. It uses pure-state reachability as a matrix construction, independently
of what C contains. For k = 1 and k = 0 both inclusions are direct: the normalized
products already cover their nonzero PSD rays and the corresponding tests cover
all positive quadratic directions.

**Equivalence.** Given the product/cone/maxCone premises, generator preservation
implies C = PSD by these two separate witnesses. Conversely C = PSD implies
preservation because each named generator is unitary. This forward witness uses
PSD conjugation, not the preceding reverse witness. No direction sources a
physical premise.

At k = 2, identify (mu_0,mu_1) with the existing `W 3` table slots and identify
binary words with `Fin 2 × Fin 2`. The Pauli dictionary, products, pairing,
CNOT(0 -> 1) and actions on token 1 then agree with the landed definitions.
The written proof therefore recovers the statement of `pairCone_eq_Q3_of_drive_maxCone`
without using that theorem as a premise. The research module
`FiniteReachTable.lean` implements the five transports
(`pairCarrierEquiv_prodState`, `pairCarrierEquiv_maxCone` with
`maxCone_of_pairCarrierEquiv`, `mem_Q3_iff_pairCarrier`, `pairCarrierEquiv_cnot`,
`pairCarrierEquiv_actT`) and proves that statement as `pairCone_eq_Q3_of_kToken`
from its k-token theorem at k = 2. The adopted two-token theorem is not in that
module's environment, which its compilation checks.

## 6. What does and does not combine with KN-DESC

KN-DESC is an implementation-class theorem. Its premises are Architecture,
ContextStable, LabelInvariant and admitted elementary implementations at each
qubit-power carrier. It then compresses implementations to arbitrary finite
carriers. With DaggerStable added, it gives the corresponding QuantumArchitecture
equivalence. Neither its input nor its output is a theorem about state cones.

The compression construction is explicit. Given an injection iota: S -> T and
s_0 in nonempty S, ContextStable admits I_S tensor K on S × T. Extend the
partial correspondence (s_0, iota(s)) -> (s, k_0) to a bijection from S × T to
S × Fin |T|. LabelInvariant admits the reindexed matrix. Architecture.block
extracts its (k_0,k_0) block, which is exactly K_(iota(s),iota(t)). This can
compress a unitary to a nonunitary contraction when its image subspace is not
invariant; the elementary generator compressions separately prove invariance
of that coordinate subspace.

The initial k-token cone result supplies none of these implementation memberships.
A valid combined finite theorem must additionally name:

- a dictionary identifying the physical k-token carrier with H_k;
- a common implementation class and its closure clauses;
- an admitted repertoire on every qubit-power carrier strong enough for the
  three `DrivesElementaryAt` families (including each parameterized transition
  flow, swap and quarter phase), rather than cone preservation alone;
- the state/operation compatibility premises for that same class and cone family.

Even full state-space equality does not imply a complete operational repertoire:
the identity-only inventory preserves the whole PSD cone and drives no nontrivial
transition. Spectator stability used in descent also covers arbitrary finite,
including odd-sized, spectators. Descent does not manufacture a three-level
physical system out of qubit registers.

## 7. Evidence, limits and next formal milestone

The eight countercontrols have these written family justifications at k = 3.
They concern the mathematical hypotheses, not physically realized alternative
theories. A finite witness alone establishes the named failure; the following
arguments establish the retained premises.

| Code | Family and the one hypothesis or proposed shortcut it fails |
| --- | --- |
| ZERO3 | The zero cone is closed, product-test positive and invariant under every unitary, but excludes every nonzero product state. |
| SCALE3 | PSD matrices of trace at least one contain normalized products, are closed under addition, are product-test positive and unitarily invariant; scaling a trace-one state by 1/2 leaves the set. |
| ADD3 | PSD matrices with rank in {0,1,2,4,8} contain every three-qubit product state (the rank is a product of three numbers in {1,2}), are closed under nonnegative scaling and invariant under every unitary. Orthogonal rank-two and rank-one matrices sum to rank three. |
| SHIFT3 | The cone {A : A + Tr(A) I/6 is PSD} is additive, closed under nonnegative scaling, contains PSD products and is unitarily invariant. I - 2P_000 is in it but has product expectation -1. |
| SEP3 | The separable cone contains products, is a cone, is product-test positive and is invariant under every local unitary. CNOT(0 -> 1) sends a product pure state to a state with a partial-transpose minor -1/4, hence outside SEP. |
| ORBIT3 | The conic hull of product PSD states conjugated by all binary invertible basis permutations is product-containing, a cone, product-test positive and invariant under every CNOT. A rank-one element in this hull must be proportional to a product pure-state generator conjugated by one of its permutations: positive summands in a rank-one PSD matrix all have its support. For the tested cyclic image, every one of the 168 inverse permutations fails a product flattening. It therefore leaves the hull. This proves failure of the local cyclic clause on tokens 1 and 2. |
| CUT3 | The cone separable across 01 / 2 contains products, is a cone, is product-test positive, and is invariant under local unitaries and CNOT(0 -> 1). CNOT(1 -> 2) sends Bell_01 tensor the token-2 north pole to GHZ, which has a partial-transpose minor -1/4 across this cut. This tests connectivity across the cut, not independence of every possible CNOT edge. |
| SLICE3 | W = I - (3/4)gg†, g = the unnormalized GHZ vector, has g†Wg = -1. Any normalized one-token contraction is I_4 - (3/4)rr† with norm(r) = 1, hence PSD. Thus even universal positivity of two-token conditional slices does not force global PSD. Product vectors have abs(<g,p>) <= 1 by the Schmidt bound, so W is also product-test positive. CNOT(0 -> 2) CNOT(0 -> 1) exposes the expectation -1/2 on the product vector +00. |

ORBIT3 exhausts a finite group exactly, rather than an angle or state grid. The
SLICE3 product grid is only a supplementary control; its universal positivity
is the displayed Schmidt bound. PSD and classical diagonal positive comparisons
are immediate on their respective actual gate inventories; a classical diagonal
cone does not claim invariance under arbitrary quantum local rotations.

`exact_check.py` tests the k = 3 dictionary inverse, local positivity/negative
directions, rational Gray multiplexors on both axes, SU(2) block preparation,
partial transpose witnesses, hypothesis countercontrols and literal repertoire
compression. It includes five fail-closed mutations. `output.txt` is its saved
run. Finite checks support the written argument; they do not certify all k.

The saved run has 242 checks and no failures; all five named mutations are
rejected at their expected labels. The first development run stopped at SEP3
before printing any result: the test selected the wrong partial-transpose minor
(indices 0,6 instead of 2,4). The corrected index pair has determinant -1/4.
This was a harness correction, not a change to the witness or decision rule.

There is no Lean executable or Mathlib cache in this execution environment.
The research Lean sources are recorded in [formalization.md](formalization.md),
with their compilation status and remaining obligations. At design head
`30a65288c06aec5f598ab088fb91fd177150157f`, in all-green run `38880722296`
(a GitHub Actions record outside the repository), they compile the all-k
dictionary, angle inversion and abstract finite-circuit identities, the exact
reachability of section 4, both inclusions of section 5 with separate
witnesses, the matrix and table forms of the conditional equivalence, both
directions of the equivalence in section 1 item 3, the coordinate formulas of
the table actions proposed in #829 for every k, the reindexing to the carriers
of section 1, the statement surface proposed in #829 with its two inclusions
and both directions, and the five k = 2 transports with the recovery of
section 5. These are research sources, not adopted theorems; adoption and the
controls proposed in #829 are not executed here. The same run freshly compiles
the historical KN-DESC design against D, from the sibling research directory
`carrier-descent-design` (off main); that design build is distinct from native
execution and adoption. No current K2, Kn, manuscript, registry, receipt or
native draft record is changed by this research record. Research-only
compilation workflows provide design evidence and do not designate F.

Productivity classification: ELABORATING on the consistency axis. The two-sided
conditional argument is supplied here and compiled in research form; it is not
adopted. No physical source is supplied.
