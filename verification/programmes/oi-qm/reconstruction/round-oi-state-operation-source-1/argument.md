# Local test/update consistency and the pair-state source

Design arguments at D=`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.
These are [W] written arguments, supplemented by exact [X] controls in probe.py.
They are not new Lean theorems or a physical realization of an exotic cone.
The initial computations are disclosed design evidence, not blind predictions.

## 1. Independently given states and the candidate

Fix a closed convex pair cone C on W(3), independently of the operation
inventory. Retain SEP ⊆ C ⊆ maxCone and the explicit finite-protocol inventory
premises, including context and label stability. Use the adopted Pauli
dictionary only as a linear coordinate representation. Do not identify C
with all PSD states or with an operation-generated reachable closure.

The restricted candidate LC is **rank-one filter/readout consistency**:
product sharp readouts give nonnegative outcome weights on each preparation;
the weights sum to its normalization; and a conditional rank-one local
readout returns an admitted, possibly unnormalized, preparation. This has a
physical meaning separate from demanding invariance under a continuous flow.
The particular repeatable update tested is L_a(X)=(P_a tensor I)X(P_a tensor I),
and likewise on the other token. Its physical availability and identification
are granted for this diagnostic, not derived from bare OI. Even this grant does
not settle the requested preservation. No stronger rule for joint measurements
or arbitrary interventions is silently substituted for the local candidate.

Source at D: CompositeDimension.maxCone is positivity on ball-product tests;
EffectSpace.maxConeOf_avail_eq identifies the same bound under its explicitly
assumed effect and orbit hypotheses. Neither supplies the local update rule
or invariance of the independently given preparation cone. OperationalValidity's
CompositeOperationalValidity quantifies over PSD matrix states. Transporting it
to C needs an additional state-space bridge, absent from the cited statement.

## 2. Local readouts and filters do not distinguish any cone in the interval

Under the Pauli dictionary, maxCone is the cone of Hermitian matrices with
nonnegative trace against every PSD product. Rank-one products suffice, since
each local PSD factor has a spectral decomposition into nonnegative rank-one
terms. This is a written consequence of the product dictionary and the ball's
PSD representation; it is not a new kernel equivalence claimed here.

Let X be block-positive and a a unit vector. The conditional matrix
sigma_a=(<a| tensor I)X(|a> tensor I) is PSD: for every b its quadratic form
is (<a| tensor <b|)X(|a> tensor |b>) >= 0. Thus

    L_a(X)=P_a tensor sigma_a belongs to SEP.

The same holds on the other token, including zero branches. Since SEP ⊆ C,
every such filter preserves C, regardless of which C in the interval was
chosen. Complementary projectors give nonnegative branch traces summing to
Tr(X). Positivity of the one-token conditional matrix follows from all product
tests, not from the finite sample in probe.py.

The guaranteed stopped map acts locally:
Phi_k=(1-(3/8)^k)Ad_(I tensor D)+(3/8)^k id. For any product test A tensor B,
its pullback is the corresponding convex combination of A tensor D†BD and
A tensor B, which are PSD products. Every Phi_k consequently preserves
maxCone, and all subsequent local sharp readouts remain valid on its output.
Each rank-one conditional output again lies in SEP. This does not say Phi_k
preserves C itself.

K_B=SEP+R+ B and stage-6 K(Z_F) lie in that interval. They satisfy the candidate
for every local sharp direction and every finite k by this argument, while
their uniformly available Phi_1 images are outside their own cones. The
separating traces are checked as -1/4 and -1/16 at the historical scaling.
The exclusion operations are guaranteed by finite_protocol_spectator for every
inventory meeting the retained hypotheses; fullClass-only replacements are
not used. Hence this **restricted rank-one filter/readout** candidate is
INSUFFICIENT, even when the update rule is granted. This does not show that
consistency under local operations generally is insufficient. The restriction
to rank-one filters is precisely why the argument covers every cone in the
interval and cannot discriminate between them.

## 3. General available one-token operations assert the target directly

The obvious general local-operation reading LO is: every available one-token
operation, with the other token idle, preserves the admitted preparation cone.
This is explicitly a fourth reading, distinct from restricted LC.

Write phi_1=(5/8)Ad_D+(3/8)id on one token. The actual constructed map obeys
Phi_1=id tensor phi_1, as the independent gate/branch derivation and all sixteen
pair matrix units check exactly. Thus requiring preservation under every
available one-token operation already requires preservation under this
uniformly available witness. Both cones violate that clause, at the familiar
negative separators. LO asserts the desired local state-operation compatibility;
it is not an independently sourced explanation of it.

This is a family-preservation reading, so it may demand more than preservation
of only Phi_1 or the specified stopped sequence if the inventory contains more
local operations. No equivalence between the full inventory and that one map
is claimed. It includes every guaranteed Phi_k and consequently entails the
third-axis flow clause on closed cones. Its physical source and the off-frame
clause remain unsupplied. The insufficiency conclusion for restricted LC is
not extended to LO.

## 4. Complete joint tests convert the requirement into its dual form

For a closed convex cone C in this finite-dimensional real space, write C* for
its mathematical dual. The nondegenerate trace pairing (or four times it in
native tables) gives C=C** by the finite-dimensional separation theorem.
For any real-linear map F,

    F(C) ⊆ C  iff  F*(C*) ⊆ C*.

Forward: for x in C and e in C*, <F*e,x>=<e,Fx> >= 0. Reverse: if all such
pairings are nonnegative, Fx is in C**=C. This uses closed convex cone
structure, not self-duality or C=Q3.

The second candidate strengthens local consistency to closure of **all** joint
valid tests under protocol pullback, together with their complete separation
of the physical preparation cone. If the tests are C*, this is precisely cone
preservation in dual language. If only a smaller independently available test
family is provided, completeness relative to C needs its own source; the
product family alone yields maxCone, not C. Stipulating that missing
identification does not derive it.

The fixture witnesses explicitly expose the failed pullback: W is in K_B*
and T in K(Z_F)*, but their Phi_1 pullbacks have negative pairing with an
admitted generator. Quantum PSD and classical diagonal/monomial interfaces
pass dual closure, so this is not an exclude-everything test. Nevertheless,
the proposed complete-dual-test premise **fails the disguise test**: it merely
restates preservation of the independently given state cone. Applying it to
all guaranteed Phi_k entails the entire target third-axis flow by the
closed-cone equivalence in the bridge research record. It supplies neither
an independent source nor the J-conjugate/off-frame clause. A primitive
constructor soundness proof based on it remains CONDITIONAL.

## 5. Saturating the product tests already grants quantum state inclusion

The third candidate declares every vector nonnegative on the product sharp
test family to be a physical preparation. The cone is then maxCone, by the
definition and EffectSpace's sharp-product characterization. It contains Q3
before any compatibility argument. Thus it violates the draft's Q3 ⊆ C
input gate, even though no self-duality was retained.

It also fails the quantum PSD positive control as a saturation principle:
e_(1,1) is block-positive but has eigenvalue -1/8, so PSD does not contain every
product-positive vector. A rule rejecting this legitimate positive comparison
cannot earn SOURCE-DERIVATION. K_B and K(Z_F) are proper subsets of maxCone:
Phi_1(B) is an omitted PSD state for K_B, and (I-8e_(1,1))/2 is an omitted PSD
projector for K(Z_F), detected by e_(1,1)'s nonnegative pairing on that cone.
Their rejection by saturation therefore supplies no independently sourced
selection of quantum kinematics.

The separate fullClass confound remains excluded: generic closure under all
its replacement channels forces Q3 ⊆ C. Those channels are not shown available
in every retained inventory and cannot be used as the successor's witnesses.

## 6. Classical comparisons actually test the readings

For any classical diagonal pair state, conjugation by the diagonal I tensor D
is the identity. Phi_1 therefore leaves the **entire** diagonal cone unchanged.
The exact probe verifies the four diagonal matrix units; linearity extends
that equality to every diagonal matrix, not just the four basis states. The
protocol is thus a positive preservation control for the actual witness map.

Classical local sharp filters use the native coordinate projectors on each
token. They retain nonnegative diagonal entries and remove others, preserving
the classical cone. The probe checks their action on each basis state; its
nonnegative span is the cone. Dual pullback by Phi_1 fixes each classical
coordinate effect and hence their nonnegative span.

For a diagonal vector diag(d_0,...,d_3), the four diagonal product tests return
exactly d_0,...,d_3. Positivity on those tests is therefore equivalent to
membership in the nonnegative diagonal cone. Product-test saturation **holds
in the classical model**, while it fails in the quantum PSD model because
of the block-positive indefinite defect. This is the useful PS comparison:
saturation admits the classical interface and rejects the quantum one.
It is not replaced by a test of an unrelated fixed permutation.

The classical interface still does not claim ball tokens or an inventory
containing the balanced circuit. The actual Phi_1 map restricts to its identity
operation, so this comparison is available without inventing such a circuit.

## 7. Scope of the source assessment

The restricted rank-one filter/readout requirement is too weak. The general
one-token-operation reading asserts the target directly. Complete-joint-test
closure is its dual preservation statement. Product-test saturation supplies
unearned quantum inclusion and fails the quantum positive comparison while
admitting the classical one. None of these four readings provides an
independently sourced physical compatibility principle.

This is a source audit of those three readings, not an exhaustive no-go for all
physical principles. Main's gluing theorem takes joint local instrument maps
as input; it is not an additional derivation of them on an arbitrary pair cone.
The historical stage-6 118 satisfied, 13 failed-hypothesis and 68 unreached rows
are not upgraded. H3 and CNOT are not silently retained for K_B; the stronger
stage-6 lane uses K(Z_F), which has those historical certificates. The present
argument requires neither to show the candidate's insufficiency.

K2, K3, arbitrary finite-carrier sourcing, hidden-history realization and P0
retain their existing statuses. No change to a foundational axiom, physical
law, matrix validity theorem, manuscript or ROADMAP is adopted here.
