# Finite availability and pair-cone preservation: exploratory audit

Baseline: `d69acffa6d2a1067c7a9162446d09b0db3b28c93` (main after #816 and
#817). This research record changes no maintained claim, kernel module, registry,
roadmap status or frozen round. It has no native receipt.

**Result [W + X]: the finite-protocol availability conditions do not imply
preservation of a given pair cone satisfying the product, cone and maxCone
conditions below.** One available depth-one operation sends an explicit member
outside the cone. This does not say that preservation cannot be obtained from
additional, independently sourced compatibility premises, or that the example
is a complete physical OI model.

Here [W] means a written universal argument, [X] exact computation, [K] an
existing adopted Lean theorem, [A] a cited audited historical record, and [D]
design validation. The computations supplement the universal arguments;
sampling never establishes a cone-wide statement.

Under AGENTS §A.31 this audit is **CONFIRMING**: availability's premises do
not mention the given cone, and the physical compatibility gap was already
named. Its contribution is the exact depth-one failure and reusable fixtures,
not a newly discovered foundational gap or a full-model independence result.

## Exact witness

Use the adopted Pauli dictionary in `EqvK2Schema.lean`: a pair table maps to
one quarter of its Pauli tensor expansion. Let SEP be the cone of all PSD
products on the two token balls, and let

```
B = |00 + 11><00 + 11| / 2,
K_B = SEP + {lambda B : lambda >= 0}.
```

B is a generator of K_B. SEP and B are PSD, so K_B is contained in Q3 and
therefore in maxCone. It contains every ball product and is closed under
addition and nonnegative scaling. It is also closed: its trace-one base is the
convex hull of the compact trace-one separable base and B; the cone over this
compact base, whose trace is bounded away from zero, is closed. These are [W].

Put `v = (0,1,-i,0)` and `P = vv†/2`, and transpose the second token to obtain
W. Explicitly,

```
W = [[0, 0,   0,  i/2],
     [0, 1/2, 0,  0  ],
     [0, 0,   1/2,0  ],
     [-i/2,0, 0,  0  ]].
```

For every PSD product A tensor C,
`Tr(W(A tensor C)) = Tr(P(A tensor C^T)) >= 0`, since transpose preserves
PSD and the trace pairing of PSD matrices is nonnegative. Also `Tr(WB)=0`.
Thus W is nonnegative on **every** element of K_B [W], not just the 64 product
controls. P's positive-projector identity and the zero pairing are checked [X].

The actual adopted circuit, reset and conditional correction give success
`(5/8) Ad_D` and three failures `(1/8) id`, with
`D = diag(1,(3+4i)/5)`. With the other token as spectator, the depth-one
stopped map is the sum of all four branches. Direct execution gives [X]

```
Phi_1(B) = [[1/2, 0, 0, 3/8-i/4],
            [0,   0, 0, 0      ],
            [0,   0, 0, 0      ],
            [3/8+i/4,0,0,1/2   ]],
Tr(W Phi_1(B)) = -1/4.
```

The output is Hermitian, trace one and PSD: its only nonzero block has positive
diagonal and determinant `3/64`. Hence the failure is preservation of K_B,
even though the channel preserves quantum positivity. The native unscaled
table pairing is four times this matrix trace, namely −1. W's Pauli table has
entries `00=1`, `33=-1`, `12=21=-1`, all others zero.

The existing all-depth formula [K] and the same trace algebra [W] give
`Tr(W Phi_k(B)) = -(2/5)(1-(3/8)^k)` for k>=1. Depths 1–8 are checked [X];
the general statement is not inferred from those eight samples. Depth one
already resolves the implication under test, without a limit argument.

## Closed-cone equivalence with the third-axis flow [W]

For **any closed convex cone C** on the pair carrier, the following are
equivalent:

1. Every finite stopped spectator map Phi_k preserves C.
2. Ad_(I tensor D) preserves C.
3. The whole third-axis rotation flow on the target token preserves C.

For 1 ⇒ 2, fix x in C. The adopted formula gives Phi_k(x) → Ad_(I tensor D)(x);
closedness of C puts the limit in C. This is a limit of states, requiring no
availability of the limiting channel. For 2 ⇒ 3, set lambda=(3+4i)/5.
It has unit modulus and is not a root of unity: if it were, lambda+lambda^(-1)
would be a rational algebraic integer, hence an integer, whereas it is 6/5.
The nonnegative powers of lambda are therefore dense in the unit circle
(an infinite cyclic subgroup of the circle has full closure, and the closure
of its nonnegative powers also contains its inverses). Preservation by D
implies preservation by every nonnegative power. Continuity of conjugation
and closedness of C then give preservation by every diag(1,exp(i theta)),
with the spectator untouched. In the native Pauli dictionary these are exactly
the target's third-axis rotations, up to the harmless choice of angle sign.
Both angle signs are included, so preservation is also equality of the cone
with its rotated image. For 3 ⇒ 1, the identity and Ad_(I tensor D) preserve C,
and each Phi_k is their convex combination with weights in [0,1].

Thus closure under the protocol's guaranteed operations already implies this
rotation-flow clause of the stage-6 missing assumption. Deferring availability
of Ad_D does not weaken that preservation consequence. This equivalence does
**not** supply the J-conjugate/off-frame flow or the whole rotation group, nor
does preservation by Phi_1 alone establish preservation by all Phi_k. It is
a written argument, not a new kernel theorem or a claim inferred from samples.

## Availability: every explicit premise

Take `I = InterventionLocality.fullClass`, whose membership predicate is
True for every matrix at every finite carrier. This is a deliberately
permissive mathematical inventory, supplied independently of K_B. It is not
claimed to be a physically compatible inventory for K_B.

| Premise of the adopted availability theorems | Discharge |
|---|---|
| Finite, decidable Token, Work, readout, spectator | Token=Fin 2; Work=Fin 2 × Fin 4; readout=Fin 4; spectator=Fin 2 |
| Architecture.one | Every identity is a member because membership is True |
| Architecture.mul | Every product is a member, irrespective of the two input memberships |
| Architecture.smul, including norm bound | Every scalar multiple is a member; the norm bound places no additional membership restriction |
| Architecture.proj | Every register projector is a member |
| Architecture.block | Every extracted ancilla block is a member |
| Circuit membership | fullClass Work balancedCircuit is True |
| Circuit isometry | `balancedCircuit_isometry` [K]; both exact implementations independently verify it [X] |
| All reset memberships | Each resetPerm j is a member, for all four j |
| All correction memberships | Each correction j is a member, for all four j |
| ContextStable, for every finite context | `fullClass_contextStable` [K]: every enlarged matrix is a member |
| LabelInvariant, for every finite relabelling | `fullClass_labelInvariant` [K]: every relabelled matrix is a member |
| Any finite depth | `finite_protocol_available`, specialized below, quantifies over every natural k [K] |

Architecture's five clauses are universally satisfied, not inferred from a
finite collection of matrix tests. The adopted `fullClass_arch` proves this
directly with True witnesses. At the baseline, the declarations are in
`ImplementationLocality.lean` (fullClass and the two stability theorems;
Architecture and fullClass_arch) and `BridgeFiniteProtocol.lean` (the circuit
isometry and availability theorems). Their digests are pinned in
[original-plan.txt](original-plan.txt).

The exact existing-theorem specialization is [W], with no new kernel claim:

```lean
OIBridge.BridgeFiniteProtocol.finite_protocol_spectator
  OIBridge.InterventionLocality.fullClass_arch
  OIBridge.InterventionLocality.fullClass_contextStable
  OIBridge.InterventionLocality.fullClass_labelInvariant
  (Fin 2)
  OIBridge.BridgeFiniteProtocol.balancedCircuit (by trivial)
  OIBridge.BridgeFiniteProtocol.balancedCircuit_isometry
  (fun _ => by trivial) (fun _ => by trivial) k
```

This supplies `InstAvail fullClass (Fin 2 × Token) Unit` for the spectator
stopped map, including k=1. The application is a written instantiation of
adopted kernel statements, not a new named or adopted kernel theorem.
Actual physical sourcing of the eight-dimensional matrix carrier and its
primitive inventory remains upstream, rather than being a reconstruction
conclusion of this audit.

The research-only [availability_example.lean](availability_example.lean)
contains an anonymous example of the same specialization at every k. The
branch workflow compiles it separately against the adopted module; it is not
imported into OIBridge or claimed as a new adopted reconstruction theorem.

## Retained and excluded pair premises

The successor draft's common test domain retains the ball-product inclusion,
closed convex cone structure and maxCone bound, together with separately
specified availability data. K_B satisfies all those clauses by the proofs
above. Sharp product tests are valid by the maxCone bound. If sharp-test
inventory membership is also requested, fullClass grants every such matrix;
that still supplies no physical identification between the inventory and K_B.

The following distinctions prevent this weaker example from being promoted to
a countermodel for a stronger premise set:

| Clause | K_B | K(Z_F) |
|---|---|---|
| Ball products, closed convex cone, maxCone | Satisfied [W] | Satisfied in stage 6, R6 N5 and REASSESSMENT §4 [A] |
| Every finite-protocol inventory premise | Satisfied with fullClass as above | Same inventory specialization; independent of the cone |
| Self-duality (stage-6 H3) | Fails: W is in K_B's dual but has a negative eigenvalue and cannot belong to K_B | Satisfied in stage 6 [A] |
| CNOT preservation | Fails, explicit product witness below [X] | Satisfied in stage 6 [A] |
| Full-flow and cyclic preservation | Fails; the displayed stopped-channel witness prevents the target drive preserving K_B | Fails in stage 6; a fresh depth-one witness is below |
| Embedded-observer physical realization | Not supplied | Not supplied by stage 6; no obstruction established there |

For the CNOT failure, take the product projector onto
`(|0>+i|1>)/sqrt(2) tensor |0>`. Its CNOT image has W trace −1/2 [X].
Therefore K_B cannot be used as a counterexample while retaining CNOT
preservation or H3. The successor must test the new compatibility premise on
K_B in the common domain before adding such stronger assumptions. Its separate
stronger stage-6 lane uses K(Z_F). No claim is made that K_B meets every item in
the 199-item historical inventory.

## Historical K(Z_F): an explicit finite witness

The historical definition is
`K(Z_F)=(Q3 intersect Z_F*) + cone(Z_F)`, with native tables
`z_(s,t)=(E00+s E13+t E22-s t E31)/4`. Its four matrix defects are

`e_(s,t)=(I+s X tensor Z+t Y tensor Y-s t Z tensor X)/16`.

Products lie in Q3 intersect Z_F*: the product pairing with a defect is
`(1+s a1 c3+t a2 c2-s t a3 c1)/16 >= 0` on the two unit balls, by
Cauchy–Schwarz for the signed permutation of c. Each defect also has
nonnegative product pairings, so the sum cone satisfies maxCone [W]. The
historical closedness, self-duality and CNOT invariance are cited [A], not
newly established by a finite generator sample.

Use the generator e_(-1,+1) (index 1 in lexicographic sign order) and the
positive projector `T=uu†`, with `u=(1,-i,1,i)/2`. Its pairings with the four
defects are `(0,0,1/8,1/8)`. Since T is PSD, it is also nonnegative on Q3
intersect Z_F*, and hence on **all** of K(Z_F) [W]. The separate checker
verifies T's projector identity, each generator pairing and [X]

```
Tr(T e_(-1,+1)) = 0,
Tr(T Ad_(I tensor D)(e_(-1,+1))) = -1/10,
Tr(T Phi_1(e_(-1,+1))) = -1/16.
```

The last value is computed by the full-register simulation, not by using the
displayed channel formula. The historical defect has trace 1/4; these values
use that exact scaling. Multiplying the generator by four normalizes its
trace and multiplies the three pairings by four.

Historical references, frozen at `e7d380fcb9881e3063243aaa149e85be3cd0a914`:
[R6 NOTES N2/N5](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/R6/NOTES.md),
[R6 REASSESSMENT §4](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/R6/REASSESSMENT.md),
and [stage-6 integration §5, disguise test](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/INTEGRATION-NOTE-STAGE6.md).
The adopted `round-oi-channel-1-audit/result.md` separately preserves the
historical inventory's 118 satisfied, 13 failed-hypothesis and 68 unreached rows.
Those historical counts and evidence statuses remain unchanged.

## Inventory-size confound and the fixture rule

fullClass is convenient for the availability instantiation, but its extra
operations cannot earn a candidate compatibility principle an exclusion.
`InterventionLocality.instAvail_fullClass_of_krausFamily` [K] makes every
finite quantum channel available, including replacement by any density matrix
sigma. Generic closure under that inventory, applied to any normalized input,
therefore forces Q3 ⊆ C by nonnegative scaling. This is already a quantum
state-inclusion assumption, even without self-duality or C=Q3.

Both fixtures can be excluded this way. The displayed Phi_1(B) is a PSD state
outside K_B. For K(Z_F), the PSD rank-one projector
`P_+=(I-8 e_(1,1))/2` has pairing −1/8 with e_(1,1). That defect is nonnegative
on Q3 intersect Z_F* by definition and on all four defects because
`Tr(e_(s,t) e_(s',t'))` is 1/16 for identical signs and zero otherwise.
It is consequently nonnegative on all K(Z_F), so P_+ is outside that cone.
No self-duality is needed for this exclusion [W].

An exclusion witness counts in the successor only if **each operation used
is available in every inventory satisfying the retained availability premises**,
with a named uniform theorem or construction. The displayed Phi_1 witnesses
qualify by finite_protocol_spectator; an arbitrary replacement channel granted
only by fullClass does not. The successor also checks assumptions and fixture
inventories for unearned Q3 ⊆ C, not just C=Q3. These corrections prevent the
two negative fixtures alone from certifying a useful new physical principle.

## Reproduction and independence

From the repository root:

```sh
python3 -I -B verification/programmes/oi-qm/reconstruction/bridge-compatibility-audit/independent_check.py
python3 -I -B verification/programmes/oi-qm/reconstruction/bridge-compatibility-audit/probe.py
```

The second command requires SymPy (validated with 1.14.0); the first uses only
the Python standard library. Both fail before a verdict if a control fails.

The branch's `bridge compatibility research` workflow repeats both calculations,
compares the saved outputs and checks the digest manifest. It is a research
replay and separate Lean design compilation, not a native F/E attestation.

- [probe.py](probe.py): 197 exact controls, rederived corrected Kraus blocks,
  stopped recurrence, Pauli round trips, trace normalization, density checks
  and reset/correction/identity/phase countercontrols. Its only change from the
  originally saved source is replacing the absolute ROOT assignment by
  repository discovery. Reversing that one line recovers SHA256
  `e60d4cafac9d1a72cc9635fd49198f33863d39043844d9fdbfc1de930478f431`.
  The original line, verbatim, is `ROOT = Path('/workspace/pr817-review')`;
  its published replacement is `ROOT = Path(__file__).resolve().parents[5]`.
- [independent_check.py](independent_check.py): 53 exact controls, rational
  pairs and sparse matrices, gate-composed circuit, explicit uniform
  attachment, reset/readout, feed-forward and partial-trace simulation on
  all 16 pair matrix units. It imports neither the probe nor its arithmetic,
  branch extraction or stopped recurrence. It checks both cone witnesses.
  This is a separately implemented checker by the same assistant, not a claim
  of independent authorship or external review.
- [original-plan.txt](original-plan.txt), [original-output.txt](original-output.txt)
  and [original-replay.txt](original-replay.txt) preserve the earlier locally
  saved evidence byte for byte. The plan is a historical exploratory decision
  rule, not a native preregistration. The new checker and ZF supplement are
  post-result verification and are not represented as prospectively frozen.
- [independent-output.txt](independent-output.txt) records the separate run.
  Replay equality checks determinism; the different implementation checks the
  calculation. Neither replay alone proves the model.
- [SHA256SUMS](SHA256SUMS) pins the saved record and scripts. New source changes
  should be recorded as revisions, not silently treated as the old audit.

No full physical independence conclusion follows. The missing question is why
an independently identified physical state cone must be compatible with the
supplied operation inventory. A preservation assumption can close the
conditional interface; establishing its physical source remains separate.
