# Record feedback, the quarter phase and the complete operation set

**WIP / author paper result; independent review pending.** Accountable home:
#1169. This is a bounded follow-up to the merged Q-A study, not a physical
apparatus proposal. Author: root, Codex session, 7 November 2026.
[Owner scope and writer separation](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6713553987).
Source snapshot: main `499463f0345e8be5c9d445db7aa7488310d52df5`;
AGENTS blob `496eb7018c736a064dddcf00fd1a278790872f49`.

## 1. Question and scoped answer

Can adaptive record feedback supply the quarter phase while retaining Q-A's
requirement C-CP, that every available encoded operation have a completely
positive quantum realization?

For the **homogeneous linear Pauli encodings and common preparation lift
defined below**, the answer is no as long as all constant slot translations
remain available. This conclusion does not depend on whether the isolated
quarter phase can be synthesized adaptively.

- If the three functionals have identically zero sum, even a successful
  heralded quarter-phase branch is impossible for any common stochastic
  protocol.
- If their sum is nonzero, an already available constant translation induces
  a non-CP encoded reflection.

This is a paper obstruction for that combined target. It neither proves a
general impossibility for OI nor settles bare adaptive S reachability for an
encoding with nonzero parity. No new physical resource is sourced.

## 2. Hypotheses, with the physical assumptions visible

Let `V = F_2^d` be the finite configuration vector of the encoded carrier.
Take three nonzero, pairwise distinct linear functionals
`f_x,f_y,f_z : V -> F_2`. Define `p=f_x+f_y+f_z`.
Over F_2 the pairwise distinction makes any pair independent.

**H-L (encoding and preparations).** The six Pauli eigenstate preparations
are the laws

    sigma_(a,b)(v) = (2/|V|) [f_a(v)=b],    a in {x,y,z}, b in {0,1}.

Their convex mixtures use the same convex mixtures of these laws. A read of
axis a returns f_a; bit 0 denotes the + eigenvalue. These are Q-A node 8's
uniform level-set preparations, not a newly fitted probability law.

**H-C (common lift and operation).** Extra apparatus/hidden variables may
have any normalized conditional law kappa_v, shared by all six preparations.
Thus their joint inputs are sigma_(a,b)(v) kappa_v. The selected operation
uses the same dynamics, program and record policy on every preparation.
After integrating over kappa_v, every finite adaptive protocol defines one
Markov kernel from v to the outgoing carrier, the full accessible record
and any declared failure. We assume neither memoryless reduced dynamics nor
a finite underlying universe. A finite dependency cone and a normalized
product-law marginal are sufficient for the finite V model; an infinite
hidden sector is allowed in kappa_v.

Preparation-dependent lifts kappa_(a,b,v), or a device that is told the
preparation label and changes its operation accordingly, are not H-C.
A single physical theory can have preparation-contextual realizations; this
paper does not exclude or identify them with H-C.

**H-T (available operations).** Every constant translation
`t_w(v)=v+w` is an available encoded-carrier process, for each w in V.
This is the generous supplied translation resource in Q-A's N
(DESIGN §1.2, node 9 and ledger P2/H-PREP). It is not derived physical
availability. It is enough that each such translation have an available
positive-weight heralded branch with its declared record retained.

**Target S and failures.** The quantum comparator sends
Z_b to Z_b, X_b to Y_b, and Y_b to X_(b+1).
An exact successful S branch must have those output laws and the agreed
success law. Arbitrary failure states and full records are retained.
The proof below only uses the certain Pauli outcomes on that successful
branch; it does not discard a failure to manufacture a pass.

**Target C-CP.** Every available encoded branch, and any permitted
coarse-graining of branches, must admit a completely positive linear map
on qubit matrices agreeing with its action on the six Pauli eigenstates.
The six states span the qubit operator space, so such a linear extension,
if it exists, is unique. This is the comparator's complete-positivity
requirement, not a claim that a native Bell apparatus is already available.

## 3. A parity-flip necessity, including adaptive protocols

Let T(v;v') be the sub-Markov kernel of an alleged successful S branch
after the accessible history is summed out. If exact S is reproduced on
all six preparations, every transition of positive T weight must obey

    f_z(v') = f_z(v),
    f_y(v') = f_x(v),
    f_x(v') = f_y(v) + 1.

**Proof.** On input sigma_(z,b), successful S followed by a Z read returns
b with certainty. Every term of the corresponding probability sum is
nonnegative, and every v with f_z(v)=b has positive preparation weight.
Therefore T(v;v') is zero whenever f_z(v') differs from f_z(v).
Apply the same argument to X_b followed by Y, and Y_b followed by X.
H-C makes T the same kernel in these three comparisons. This proves all
three identities on the support of T, regardless of its internal history,
fresh random variables, adaptive choices or discarded apparatus. Add them:

    p(v') = p(v) + 1.                                      (1)

No affine form for the process, non-adaptivity, or kernel no-go theorem
was used. In particular, an affine output must not be confused with an
assumption that its implementation used no feedback.

**Zero-parity case.** If p is identically zero, (1) is impossible.
Then T has no nonzero entry and no preparation can have positive success
probability. This excludes even a heralded S branch under H-L/H-C.
The one-cell R1 encoding f_y=f_x+f_z is the familiar special case.

## 4. A nonzero parity makes a forbidden translation available

If p is a nonzero linear functional, choose w with p(w)=1. By H-T, t_w
is available. It sends sigma_(a,b) to sigma_(a,b+f_a(w)), exactly.
On the Bloch coordinates its linear action is

    D_w = diag((-1)^f_x(w), (-1)^f_y(w), (-1)^f_z(w)),
    det(D_w) = (-1)^p(w) = -1.                             (2)

Its three signs contain an odd number of minus signs. Every such sign
pattern is a Pauli-unitary conjugation composed with matrix transpose
(the transpose has signs (+,-,+)). Hence no CP extension exists.

For completeness, the obstruction is explicit. Write
`|Phi+>=(|00>+|11>)/sqrt(2)`. Partial transpose gives

    (transpose tensor id)(|Phi+><Phi+|)
      = (|00><00| + |10><01| + |01><10| + |11><11|)/2.

Its action on `(|01>-|10>)/sqrt(2)` has eigenvalue -1/2.
An output Pauli unitary preserves that negative eigenvalue. Thus the
unique linear map agreeing with (2) on all six preparations is not CP.
A positive branch weight only scales the negative eigenvalue.
Additional records cannot repair the same marginal: a sum of CP
record branches would be CP.

The Bell state here is an imported mathematical test of complete
positivity. This proof does not assert that OI prepares that state.

## 5. Combined result and stopping rule

**Proposition.** Under H-L, H-C and H-T, no adaptive protocol can supply
an exact S branch while the available encoded operation set satisfies
C-CP. If p=0, S fails by §3. If p is nonzero, C-CP fails by §4.
This dichotomy exhausts the stated linear encodings.

The nonzero-parity obstruction already exists before any proposed
feedback protocol or NNB coupling. Synthesizing S alone therefore cannot
pass the complete target in this class. This is not a proof that bare
adaptive S is unavailable; for that isolated question Q-A §4.3 remains open.

A next physical proposal would have to change and source at least one
of the actual hypotheses: the uniform linear preparation/encoding,
the common lift, or the independently selectable translations.
Which alteration is physically justified is not decided here.
Restricting translations solely because the unwanted reflection must
disappear would repeat target-defined premise I, not derive it.

This result does not demand direct decoding of hidden information.
Indirect recovery, deterministic dynamics and arbitrary internal memory
were allowed in the common kernel. It supplies no Born-rule selection,
coherence-through-read mechanism, quantum pair or full equivalence proof.

## 6. Relation to the existing sources and verification

- [Q-A DESIGN at the source snapshot](https://github.com/amaybaum/incompleteness/blob/499463f0345e8be5c9d445db7aa7488310d52df5/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md):
  §1.2 defines the supplied translations; node 8 gives the level-set
  preparations; node 9 gives the affine reflection argument; §4.3 keeps
  adaptive S open. The present proof explicitly allows a stochastic,
  record-adaptive S process and proves only the combined-target obstruction.
- [Apparatus-1 DESIGN, Lemma 5](https://github.com/amaybaum/incompleteness/blob/499463f0345e8be5c9d445db7aa7488310d52df5/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L731):
  the earlier four-point obstruction is consistent with the p=0 case.
- [Lillystone–Wallman–Emerson, arXiv:1802.06121v2](https://arxiv.org/pdf/1802.06121v2):
  the single-qubit stabilizer comparator and its operational scope.
  Read first-hand; not a premise of the elementary proofs above.
- #1185/#1186 remain separate stopped physical-source screens.
  No positive source or Q-A compatibility is inferred from them.

The proofs are hand derivations. No simulation, enumeration, scientific
program, Lean build, execution round, freeze or workflow launch was
performed. Ordinary PR CI checks repository verification only.
This is paper mathematics, not a new kernel theorem. Neither the vacuous
ReadWriteSourced result nor the disputed R1 C-CP proof is used.
Independent review of the exact pushed paper is required before its
author result can be treated as accepted. No merge or premise adoption
is authorized by its publication.
