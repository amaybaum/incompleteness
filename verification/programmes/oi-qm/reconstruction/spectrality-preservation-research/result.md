# Spectrality and the stopped maps: one model family resolved

**Research result: SP ⇒ guaranteed stopped-map preservation remains OPEN on
SEP ⊆ C ⊆ maxCone.** This bounded branch resolves the tempting
order-isomorphic-quantum examples, rather than establishing a general
implication or supplying an independently derived physical principle.
Classification under AGENTS §A.31: ELABORATING. The original two-fixture SP
exclusions and their historical evidence levels are unchanged.

The starting tree is bridge research `1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37`;
main's mathematical sources at `dee3b5ae` agree with that tree. This record is
research/design, has no F or native receipt, changes no maintained manuscript
claim, and adds no permanent CI job. [plan.md](plan.md) is the exploratory
decision rule written before these certificate runs, not a prospectively
frozen prediction. The matrices were chosen algebraically and the bad-domain
phase separator found by an exact finite vector search; these computations
are disclosed post-construction checks, not a blind candidate selection.

## Source and the exact question

SP is the classical-decomposability postulate defined in the
[existing screen](https://github.com/amaybaum/incompleteness/blob/1d4606b2f8b91d25b8620d0f0ee7d5c6d6c1fa37/verification/programmes/oi-qm/reconstruction/physical-state-operation-compatibility/spectrality.md).
The original [Barnum–Müller–Ududec paper, §§I and III](https://arxiv.org/html/1403.4147v4#S3)
states SP separately from strong symmetry. Its reconstruction theorems use
additional postulates; they do not license applying their conclusion with SP
alone. The later [Barnum–Hilgert classification](https://arxiv.org/abs/1904.03753)
also retains strong symmetry. Adding that symmetry here would change the
research question and require an independent source and gate audit.

The question retains an independently specified closed convex pair cone,
all ball-product preparations, product-test positivity, and the separately
specified availability premises. The latter guarantee the actual
Phi_k = (1−(3/8)^k) Ad_(I⊗D) + (3/8)^k id,
where D=diag(1,(3+4i)/5), by the existing kernel statements. The target is
preservation of that same C, not merely valid product-test probabilities.

Written arguments below are [W]; script certificates are [X]. There is no
new Lean certification. A finite basis check certifies a linear map identity,
not a universally quantified cone claim by sampling preparations.

## Untilted coPSD: a universal positive answer for this family [W]

Let Γ transpose the second token and C_co=Γ(Q3). Γ is an invertible real-linear
trace-preserving isometry of the Hermitian trace pairing, so C_co is closed,
convex and trace self-dual. It contains SEP and lies in maxCone:
Γ(A⊗B)=A⊗B^T is a PSD product, and pairing Γ(Y) with A⊗B equals the
nonnegative pairing of Y≥0 with A⊗B^T.

For every quantum spectral resolution Y=Σ p_i P_i, Γ(Y)=Σ p_i Γ(P_i)
is an SP resolution in C_co. The Γ(P_i) are extreme normalized states because
an invertible order isomorphism preserves extreme rays. They also furnish
distinguishing effects: their pairings are δ_ij and they sum to I, after
extending to a full orthogonal projector frame. This is a static GPT with
those effects; physical availability of all such tests is not derived from OI.

For every complex two-by-two K and every matrix Y,

    Γ((I⊗K) Γ(Y) (I⊗K)†) = (I⊗K̄) Y (I⊗K̄)†.

Thus every local quantum CP branch on the second token preserves C_co.
A first-token branch commutes with Γ and has the same property. Sums of
branches preserve C_co by convex cone closure. In particular every Phi_k
preserves C_co, as do all local unitary flows, including both third-axis and
J-conjugate rotations. This supplies no availability claim for those flows.

Allowing a local invertible congruence does not produce a different cone:
congruence maps the entire PSD cone onto itself; after Γ its image is still
C_co. Local invertible congruence directly on C_co also maps it onto itself
by the displayed identity. Neither construction produces a preservation
counterexample.

The family does not force Q3 ⊆ C: the Bell projector B is excluded, since
Γ(B) has eigenvalue −1/2. It therefore passes the common-domain input gate.
C_co fails native CNOT preservation, so it gives no input-gate witness for
the stronger lane that adds CNOT or other stage-6 premises. The all-local-CP
preservation result is a statement about this mathematical model, not a
source for actual physical state–operation compatibility.

## CNOT-tilted coPSD: actual failure, rejected domain [W + X]

Let U=CNOT and C_t=Ad_U Γ(Q3). As another trace-preserving order-isomorphic
copy of quantum PSD, C_t is closed, convex, normalized, self-dual and SP.
Unlike C_co, its tensor axes disagree with the native ball-product axes.

Take Q=|v><v|/3 with v=(1,1,1,0), x=Ad_U Γ(Q),
R=|w><w|/3 with w=(1,i,−i,0), and e=Ad_U Γ(R).
Then x∈C_t and e∈C_t*=C_t; I−e also belongs to C_t. Exact computation gives

    Tr(e x)=1/9,
    Tr(e Phi_1(x))=−1/9.

This is a real failure under the protocol's actual depth-one map, not an
arbitrary inventory operation. It proves that SP by itself, with no native
product-domain requirement, does not entail that map's preservation. It
does **not** answer the common-domain question. The missing premises fail
explicitly in both directions:

* P=|+0><+0| is a native PSD product but U† P U=B. Its preimage under
  the cone isomorphism is Γ(B), with eigenvalue −1/2. Hence SEP ⊄ C_t.
* If S=|01−10><01−10|/2, the state z=Ad_U Γ(S) belongs to C_t, but
  Tr(z P)=−1/2. Hence C_t ⊄ maxCone.

These failures disqualify the model before any compatibility verdict. The
bad-domain witness is retained to make the scope of the tempting SP argument
reviewable, not promoted to a physical no-go theorem or full-model example.

## Positive comparisons, controls and next fork

Quantum PSD passes SP by its spectral theorem and Phi_k preservation by
unitary conjugation and convexity. The actual Phi_1(B) has nonzero-block
determinant 3/64. Classical diagonal states pass SP by coordinate frames,
and the actual Phi_1 fixes every diagonal matrix unit and consequently the
whole diagonal cone. The classical comparison is a restriction of the map,
not a claim that classical tokens satisfy the balanced-circuit inventory.

[check.py](check.py) uses SymPy 1.14.0 and checks 109 exact controls.
[independent.py](independent.py) is a separate stdlib Fraction rational-complex
matrix implementation with 112 controls. It imports neither SymPy nor the
first script and writes the Bell frame and CNOT action by different routes.
Both reject four mutations: missing complex conjugation, wrong phase,
wrong distinguishing effect, and false product membership. Same assistant,
different implementations; no claim of independent authorship. Initial
SymPy runs rejected unsimplified symbolic equalities for a frame trace and
classical phase cancellation; exact simplification repaired the harness,
and no verdict printed on either failed run.

Run from the repository root with `python3 -I -B` (using the SymPy interpreter
for check.py). Saved outputs and SHA256SUMS pin this record; replay equality
checks determinism, while the different implementation checks arithmetic.
No original bridge scripts, outputs, digest list or workflow are modified.

The remaining fork is precise: construct an SP cone inside the actual
SEP/maxCone interval that breaks Phi_1, or prove that this interval plus SP
already entails all Phi_k preservation. Neither the rejected tilt, the two
SP exclusions, nor a classification importing strong symmetry settles it.
For closed cones, a proof for every Phi_k would entail the full third-axis
flow by the existing bridge argument, so that consequence must enter its
disguise audit. SP's physical source, the stronger CNOT/self-dual implication,
and the OI⁺-1 relation remain open; existing K2/K3/P0 statuses are unchanged.
