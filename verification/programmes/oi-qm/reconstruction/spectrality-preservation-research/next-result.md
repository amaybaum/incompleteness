# Native-product rigidity of two spectral model families

**Research result:** the generic SP ⇒ stopped-map preservation question
remains OPEN. This branch proves a preservation theorem for every unitarily
tilted coPSD cone meeting the native product domain, and excludes every
normalized centrally symmetric cone base from that domain. Neither result
selects a physical compatibility principle. Classification under AGENTS
§A.31: ELABORATING; the universal family classification is stronger than the
previous single-CNOT rejection and constrains further candidate searches.

This is a forward research/design record following [result.md](result.md),
with its prospective exploratory decision rule in [next-plan.md](next-plan.md).
There is no F, native execution, receipt, adopted Lean theorem or permanent
CI job. No historical output, digest list, maintained manuscript or K2/K3/P0
status changes. Written universal arguments are [W]; exact certificate
checks are [X]. All results below are mathematical model results.

## Common domain and source

Keep the independently specified closed convex cone C of Hermitian
four-by-four matrices, SEP ⊆ C ⊆ maxCone, and normalization Tr X=1.
The separately specified availability premises guarantee the actual maps

    Phi_k = (1−(3/8)^k) Ad_(I⊗D) + (3/8)^k id,
    D = diag(1,(3+4i)/5).

SP retains its definition and external source from
[spectrality.md](https://github.com/amaybaum/incompleteness/blob/1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37/verification/programmes/oi-qm/reconstruction/physical-state-operation-compatibility/spectrality.md):
every normalized state decomposes into perfectly distinguishable pure
states. The source is Barnum–Müller–Ududec, arXiv:1403.4147v4, §III,
Postulate 1. It is a postulate, not an OI derivation. No strong symmetry,
homogeneity, purification, no-restriction assumption or Jordan classification
is imported. Mathematical spectral decompositions in the family below have
explicit transformed distinguishing effects; the availability of all such
tests as physical OI tests remains unsourced.

## 1. Every admissible unitary tilt is the original coPSD cone [W]

Let Q be the quantum PSD cone, Γ partial transpose on the second native
token, and U an arbitrary complex four-by-four unitary. Define

    C_U = Ad_U Γ(Q).

This family has closed convex cones and trace-normalized SP: the invertible
trace-preserving map Ad_U Γ transports quantum pure rays, spectral frames
and distinguishing effects. It is also an isometry of the real Hermitian
trace pairing, hence C_U is trace self-dual. Consequently product admission
SEP ⊆ C_U and the bound C_U ⊆ maxCone are equivalent for this family:
dualizing either inclusion yields the other. Neither inclusion is automatic.

**Theorem.** If SEP ⊆ C_U, then U is a local unitary or a local unitary
composed with SWAP. In either case C_U = Γ(Q), so every guaranteed Phi_k
preserves C_U.

**Step 1: product admission forces a product-vector preserver.**
For any nonzero product vector p=a⊗b, its projector lies in C_U exactly
when Γ(U†|p><p|U) is PSD. The partial transpose of a pure projector is PSD
exactly when the vector is product. Indeed, write a Schmidt decomposition
with coefficients s,t≥0. The partial-transpose eigenvalues are
s²,t²,st,−st, and their nonnegativity is equivalent to st=0. This is a
two-by-two linear-algebra fact, not a reconstruction postulate. Product
admission therefore says T=U† sends every product vector to a product vector.

**Step 2: classify the invertible two-qubit product preserver.**
A two-dimensional linear subspace consisting entirely of product vectors
has a fixed factor: it is a⊗C² or C²⊗b. To prove this, choose independent
product vectors x⊗y and r⊗t spanning the subspace. The determinant of their
two-by-two coefficient matrix after addition is

    det(x y^T + r t^T) = det[x,r] det[y,t].

Because their sum is product, one factor determinant vanishes. Independence
of the tensor vectors then leaves precisely one shared factor. This covers
complex vectors and all degenerate coordinate cases.

Apply the lemma to L_i=T(e_i⊗C²), i=0,1. Each is two-dimensional and their
intersection is zero by invertibility of T. They cannot have opposite
fixed-factor types: a⊗C² and C²⊗b intersect in the line a⊗b. After possibly
swapping the output tokens, both are a_i⊗C², with a_0,a_1 independent.
There are invertible two-by-two maps B_i with

    T(e_i⊗y)=a_i⊗B_i y.

Since T((e_0+e_1)⊗y) is product for every y, B_0 y and B_1 y must be
dependent for every y. Thus B_1 B_0⁻¹ preserves every one-dimensional
subspace. A linear map with that property is scalar: its values on the two
basis vectors give two scalars, and their sum forces those scalars equal.
Absorbing that scalar into a_1 yields T=A⊗B, or T=(A⊗B)SWAP.

Unitarity removes nonunitary local factors. From
(A†A)⊗(B†B)=I, the positive eigenvalues of the two factors have constant
products; hence A†A=αI and B†B=α⁻¹I for α>0. Rescaling gives two local
unitaries. The inverse T⁻¹=U has the same local/SWAP form. This elementary
proof uses no assumed transitivity of physical operations.

**Step 3: cone equality and actual-map preservation.**
For all matrices Y and all local matrices A,B,

    Γ(Ad_(A⊗B) Γ(Y)) = Ad_(A⊗B̄)(Y).

For local unitaries this conjugates Q onto itself, so local Ad maps Γ(Q)
onto itself. SWAP transports second partial transpose to first partial
transpose; the two images of Q agree because full transpose preserves Q.
Equivalently, with S=SWAP,

    Γ(Ad_((A⊗B)S) Γ(Y)) = Ad_((A⊗B̄)S)(Y^T).

This proves C_U=Γ(Q) for every admitted tilt. On that cone, specifically,

    Γ(Phi_k(Γ(Y)))
      = (1−(3/8)^k) Ad_(I⊗D̄)(Y) + (3/8)^k Y.

The right side is PSD for every Y≥0, proving preservation for every k.
In fact the family admits all local CP branches by the same pullback
identity, including both local rotation flows. This is a cone theorem,
not a claim that every such operation is physically available.

### A rejected entangling tilt, with the native product test [X]

Take U=diag(1,1,1,(3+4i)/5) and p=(1,1,1,1)/2, a native product vector.
For its normalized projector P,

    det Γ(U† P U) = −1/400.

Thus this tilt fails product admission. Self-duality then also prevents it
from meeting the maxCone bound. This example exercises an entangling tilt
different from CNOT, but the theorem above covers arbitrary U rather than
inferring a classification from sampled unitaries. It is not a
common-domain counterexample to SP ⇒ preservation.

## 2. No centrally symmetric normalized pair base meets the domain [W]

Suppose Ω={X∈C:Tr X=1} is centrally symmetric about some M. Necessarily
Tr M=1, and 2M−P_j lies in Ω for each of the four computational product
projectors P_j. Since C ⊆ maxCone, testing with P_j gives

    2 Tr(P_j M)−1 ≥ 0,  j=0,1,2,3.

Summing, using Σ P_j=I, gives 2 Tr M−4=−2≥0, a contradiction. The center
need not be maximally mixed, diagonal or PSD. This rules out every centrally
symmetric normalized base, with or without SP; in particular it rules out
every ellipsoidal base and every linearly transported Lorentz-cone model.

For completeness, an arbitrary trace-normalized section of a Lorentz cone
is an ellipsoid when its normal is strictly positive on the nonzero cone.
That strict positivity is required here, not silently added: trace is
strictly positive on nonzero maxCone elements. To see this, every product
orthonormal basis has nonnegative expectation values summing to trace.
If trace were zero, every such product expectation would vanish; product
projectors span the Hermitian matrices, so the matrix itself would be zero.
The same holds on C. In finite dimensions the trace functional therefore
lies in the interior of C*, and its normalized base is compact.

Under a Lorentz-cone isomorphism write this functional as
ℓ(t,x)=αt+b·x, where α>||b||. Eliminating t from ℓ=1 and the boundary
t²=||x||² yields a positive-definite quadratic form with matrix
α²I−bb^T, hence an ellipsoid, centrally symmetric about

    x_0 = −b/(α²−||b||²),
    t_0 =  α/(α²−||b||²).

This proves the Lorentz rejection for arbitrary positive normalizations,
not just a conventional round-ball section. It does not exclude the
single-qubit ball: the obstruction uses four distinguishable native product
outcomes of the pair. A four-outcome classical simplex is likewise not
centrally symmetric and is not rejected by this argument.

## Evidence, positive comparisons and retained gates

[next_check.py](next_check.py) uses SymPy 1.14.0: 82 exact controls, including
the symbolic product-subspace determinant identity and a symbolic complex
pure-projector partial-transpose determinant in a phase-fixed chart.
[next_independent.py](next_independent.py) uses only stdlib rational-complex
arithmetic: 341 controls, including separate complex determinant cases and
256 finite product-subspace certificates. Both check local and local/SWAP
covariance on all 16 matrix units, which certifies those linear identities
on every matrix. Both reject four mutations and agree on −1/400 and −2.
The second imports neither SymPy nor the first checker; both were written
by the same assistant, so this is implementation independence, not independent
authorship. All required controls passed on their first runs. Saved outputs
and a separate NEXT-SHA256SUMS pin only these new files.

The quantum comparison uses the actual Phi_1(B): its nonzero two-by-two
block has determinant 3/64. The classical comparison checks that Phi_1 fixes
every diagonal matrix unit, hence the whole diagonal cone. Quantum SP and
classical SP remain the spectral and coordinate-frame constructions in the
prior record. Neither comparison claims to derive their physical premises.

Both original fixtures K_B and K(Z_F) still fail SP for the independent
state/test reasons already recorded; neither fixture is silently repaired or
discarded. The input gate still has its witness Γ(Q): it admits native
products and product-test positivity, passes SP, and excludes the quantum
Bell projector since Γ(B) has eigenvalue −1/2. Therefore these family results
do not force Q3⊆C. That witness still fails native CNOT preservation and
does not settle the stronger H3/CNOT lane.

The disguise test retains both directions separately. SEP preserves every
local flow and stopped map yet fails SP, so preservation does not imply SP.
For this resolved model family, preservation follows because the domain
classifies the cone as coPSD; SP adds nothing to that classification.
Generic SP ⇒ preservation remains open. If it were proved for every Phi_k
on a closed cone, the third-axis flow consequence from the bridge record
would still apply; no new result removes that obligation. SP's physical
source, the generic J-conjugate implication and OI⁺-1 relation remain open.

**Next fork:** a common-domain counterexample must leave both the entire
unitary-tilted coPSD family and the centrally symmetric-base family, or a
general theorem must control a wider asymmetric cone class without importing
strong symmetry. These eliminations do not exhaust spectral cones or answer
the physical source question.
