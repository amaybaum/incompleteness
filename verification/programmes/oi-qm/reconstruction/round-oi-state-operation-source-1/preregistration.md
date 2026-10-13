# OI-STATE-OPERATION-SOURCE-1 — local consistency and the physical pair-state source

Status: candidate freeze, native V3 draft for owner review. This is a bounded
source audit, not a proposed new physical axiom. No compatibility source or
native execution is claimed by drafting it. Execution waits for an exact-head
all-green workflow_dispatch run and the owner's designation of F under
AGENTS §A.39. The instruction to proceed is not an F designation.

```v3-round
round OI-STATE-OPERATION-SOURCE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-oi-state-operation-source-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-oi-state-operation-source-1/
record AM verification/receipts/OI-STATE-OPERATION-SOURCE-1.json
execution M .github/workflows/verify.yml
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4.
This is main after #818. Delta(D,F) contains only this preregistration and any
review amendments in this round's amendments directory. The older bridge
research branch is evidence, not the drafting base, and is not merged into
this control-plane branch. No kernel, manuscript, ROADMAP, registry, legacy
record, other round's record or seal changes are authorized.

## Bounded question and independently given states

Does local preparation/test and repeatable conditioning consistency supply
preservation of the independently given pair cone under the guaranteed finite
protocol? If it does not, do either of two specified strengthenings provide an
independent physical source, rather than restating preservation or assuming
quantum state inclusion?

The carrier is W(3) with its adopted real-linear Pauli dictionary. The physical
preparation cone C is specified independently of the operation inventory.
Retain closed convex cone structure, all ball products and the maxCone bound.
The normalization is the trace under the dictionary; product tests and their
pairing are specified independently. Do not define C as an operation-generated
orbit or reachable closure. The dictionary is a coordinate representation,
not a physical identification of C with PSD matrices.

The inventory has Architecture, the balanced circuit/reset/correction
memberships and isometry, ContextStable and LabelInvariant. Each exclusion
operation must be available in **every** inventory satisfying those premises.
The exclusion operation here is Phi_1, licensed by finite_protocol_spectator.
fullClass supplies a convenient fixture instantiation but its extra operations,
especially arbitrary state replacements, earn no exclusion.

The common domain does not assume self-duality, CNOT preservation, full-flow
invariance, cyclic invariance, complete dual-test availability or an embedded
history realization of the pair. A stronger stage-6 lane may cite K(Z_F)'s
historical H3/CNOT certificates, but K_B is not eligible in that lane. These
extra certificates do not enter the local-consistency argument.

## The three fixed candidate readings

| id | exact candidate reading | independently meaningful input and status at D | test |
|---|---|---|---|
| LC | Product sharp readouts have nonnegative normalized outcome weights on admitted preparations; a rank-one local conditional update L_a(X)=(P_a tensor I)X(P_a tensor I), or its other-token analogue, returns an admitted unnormalized preparation | Valid local probabilities are a physical consistency requirement. maxCone encodes their mathematical bound. The specific repeatable update and its physical identification/availability are granted design premises, not sourced by bare OI | Determine whether either qualified cone violates this candidate despite satisfying the retained premises; compare with its Phi_1 preservation failure |
| DT | Every joint dual-valid test remains dual-valid under pullback by every guaranteed Phi_k, and the tests completely separate the physical preparation cone C | Completeness means C=C** for the mathematical dual; identifying independently available physical joint tests with C* is additional and unsourced. Closure under their pullbacks is the proposed strengthening | Prove both directions of the dual preservation equivalence under only closed convex cone structure; apply the stage-6 disguise test |
| PS | Every vector positive on the independently specified product sharp test family is a physical preparation | A state-saturation/no-restriction proposal, not an OI theorem. EffectSpace identifies the resulting cone as maxCone under its stated coverage hypotheses | Check Q3 ⊆ C before compatibility is used, and test the quantum PSD comparison as a saturation model |

These are the entire candidate set for this round. No further axiom or updated
state definition is introduced after a candidate fails. Failure closes this
bounded source route, not every possible physical compatibility principle.

## Premise and level ledger

[K] means an existing adopted kernel statement, [W] a written universal
argument, [X] exact computation, [A] a cited audited historical record, and
[D] design evidence. The levels remain distinct: H history, O elementary
operational, P pair cone, M matrix theory. No H/M fact is transported to P
without a named bridge and its hypotheses.

| premise/source at D | level/status | bearing and checkpoint |
|---|---|---|
| CompositeDimension.maxCone and the adopted product dictionary, EqvK2Schema.dict_prodState | P, definitions/[K] linear identity | State/test pairing; symbolic whole-product identities and [W] block-positivity argument |
| EffectSpace.maxConeOf_sharpFamily and maxConeOf_avail_eq | P/O, conditional [K] on sharp coverage/effect and orbit hypotheses | Product positivity upper bound; does not source physical state saturation, the update or compatible actions |
| Architecture and the circuit/reset/correction memberships | M, explicit hypotheses; fullClass_arch supplies one [K] instantiation | Availability ledger retained exactly; source bytes unchanged from D |
| ContextStable and LabelInvariant | M, explicit hypotheses; fullClass stability instances [K] | Needed for finite_protocol_spectator; not physical preservation of C |
| finite_protocol_spectator and balanced_stopped_formula | M, conditional availability and formula [K] | Uniform Phi_k availability; independent fixture replay and exact branch derivation |
| Closedness, convexity, SEP ⊆ C ⊆ maxCone | P, retained assumptions | K_B [W] certificate and K(Z_F) [A] certificates; universal local-filter argument |
| CNOT and H3 | P, additional stage-6 certificates only for K(Z_F) | Not retained for K_B; original independent checker verifies its CNOT countercontrol |
| CompositeOperationalValidity | M, assumed condition with conditional theorems [K] | Quantifies over PSD matrices; no identified arbitrary pair C in that definition. It is not LC's physical source |
| Main's operational gluing theorem, composition clause | H/M, stated realization with joint maps as input | Does not derive the local instrument action on this C; joint-action input is recorded, not assumed away |
| Full-flow (b), OI⁺-1, idle extension, frame covariance | P/M, additional/open or do-not-assume items in stage 6 | Excluded as source premises; DT's exact logical content is assessed explicitly |

The source audit is bounded to the above statements and readings. It does not
recensus all 199 stage-6 items or turn a previously unreached history bridge
into a proved one. The historical 118 satisfied, 13 failed-hypothesis and 68
unreached rows remain distinct and unchanged. A future bridge audit needs its
own scope and control plane.

The frozen historical references are the
[bridge audit at eda945a](https://github.com/amaybaum/incompleteness/blob/eda945a6a94251878ac56c7ddb67e148a82e3dd5/verification/programmes/oi-qm/reconstruction/bridge-compatibility-audit/result.md),
[R6 NOTES N2/N5](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/R6/NOTES.md),
and [stage-6 integration §5](https://github.com/amaybaum/incompleteness/blob/e7d380fcb9881e3063243aaa149e85be3cd0a914/research/archive/pt/INTEGRATION-NOTE-STAGE6.md).
They supply the cited fixture certificates and disguise assessment; their
statuses are not strengthened by this round.

## Mandatory fixtures, comparisons and inventory-size gate

1. K_B=SEP+R+ B, where B is the Bell projector. Its product, closed-cone and
   maxCone premises have written certificates. W is nonnegative on every
   element of K_B; Phi_1(B) has negative W pairing. CNOT preservation and
   self-duality fail and are not retained here.
2. Stage-6 K(Z_F)=(Q3 intersect Z_F*)+cone(Z_F), at its historical scaling.
   Its product/maxCone/closedness and the stronger H3/CNOT claims keep their
   [A] evidence levels. The exact positive dual test T is nonnegative on all
   four defects and the PSD summand; its Phi_1 pairing is negative.
3. Independently specified quantum PSD states with the actual quantum
   instruments are the positive comparison. No equality C=Q3 is inferred
   from using that comparison.
4. Independently specified classical diagonal states with their native
   coordinate readouts and monomial operations are the non-quantum positive
   interface comparison. This is not a ball-token fixture and does not claim
   the classical inventory contains the balanced circuit.

A principle excluding everything fails the two positive-comparison gate.
A fixture exclusion counts only when the fixture satisfies every retained
premise and is violated at a named clause of the candidate. The operation
used must have a uniform availability theorem; fullClass-only replacement
channels do not count. Check all assumptions and fixture inventories for
unearned **Q3 ⊆ C**, not merely C=Q3. Quantum pure-state reachability,
product-test saturation or generic closure plus a full replacement inventory
cannot be smuggled into the source.

## Universal arguments and the disguise checkpoint

The fixed [W] arguments are in the prospective argument.md below:

- maxCone/product positivity makes every local rank-one conditional matrix
  PSD, so a conditional update has product form P_a tensor sigma_a and lies
  in SEP. Therefore LC holds for every cone in the retained interval, not
  just for the sampled sharp directions.
- Local stopped maps preserve maxCone: product-test pullbacks remain convex
  combinations of PSD products. Valid local readouts on protocol outputs do
  not thereby identify those outputs as members of C.
- For a closed convex cone, F(C) ⊆ C iff F*(C*) ⊆ C*, by the finite-dimensional
  separation theorem. Thus complete dual-test closure is the same preservation
  statement in dual language. Physical sourcing of the complete joint test
  family would be additional, not provided by this equivalence.
- Preservation by all Phi_k is equivalent to the target's complete third-axis
  flow: closedness gives the D limit; (3+4i)/5 is not a root of unity because
  its sum with its inverse is 6/5, a noninteger rational algebraic integer if
  it were; dense powers and closedness give the flow; convexity gives the
  converse. No availability of the limiting channel is required. The
  J-conjugate/off-frame clause is not reached.
- Product-test state saturation gives maxCone and hence Q3 inclusion before
  any compatibility derivation. A block-positive defect outside PSD makes the
  quantum PSD comparison fail saturation.

Apply stage 6's disguise test by expanding the candidate and checking logical
implications in both directions under only retained premises. LC is tested
separately from stronger complete-joint-test or all-intervention conditions.
Assuming preservation of all primitive and spectator actions then inducting
over InstAvail remains a CONDITIONAL interface lemma, not a newly sourced
physical principle. These [W] arguments are not labelled new kernel proofs.

## Frozen prospective files and workflow

Read the following files byte for byte from design commit
`1a5105507f6d13cca4bbb2c94b6a49644a866e52` on
research/state-operation-source-design-20261013. The first four are added to
this round's record directory after F. The design-only workflow is not adopted.

| source/destination | SHA256 |
|---|---|
| record directory probe.py | 7dcea2e0df5980acd7afe78c828dd932544e506e6fc19cc8bf6fbe6511e1dc28 |
| record directory fixture_check.py | b8e316ee44c80e366a65c5d95bf4a5ef699d8bc556583c1fe9bac4c314750532 |
| record directory argument.md | b7f31ee700a3ec928bcc7146a468ae78f9776e56e6b8b5fca5e7f32e68ea9189 |
| record directory controls.py | 6342c5599fc70f03d98d07cd8461cb5ba655fd67523b348149ce59eee0620ffb |
| .github/workflows/verify.yml | fc9edd8035ae846d440529f09993b89be9172c466762874735e17d0f6e0eec05 |

Controls SHA256: 6342c5599fc70f03d98d07cd8461cb5ba655fd67523b348149ce59eee0620ffb

The verify workflow differs from D in exactly five splices: add the
probes_oistateoperationsource1 job; add it to Numerical probes' needs; add its
result environment variable; add its result echo; require its success. The
job fetches full history, uses Python 3.11 with SymPy 1.14.0, runs native object
controls and mutation tests. No other job changes. Freeze D's workflow and
the exact predicted workflow, and check the source diff before adoption.

fixture_check.py is the unchanged separately implemented 53-control checker
from bridge research at `eda945a6a94251878ac56c7ddb67e148a82e3dd5`.
It uses standard-library rational pairs and a full-register simulation.
probe.py independently composes the actual eight-dimensional gates, checks
the corrected branches, uses SymPy for the local filters and probability
controls, and checks symbolic product identities. Neither finite probe proves
the universal cone assertions; their [W] proofs remain separately reviewable.

## Decision rules and evidence boundary

No verdict is earned after a failed control, nonzero exit or nonempty stderr.
The fixed finite domain is five fixture generators (B and the four ZF
defects), before and after Phi_1, eight exact local sharp frames, both sides
and both complementary outcomes. Counts are coverage checkpoints, not an
inference of universal positivity from samples.

- **LC insufficient:** both qualified fixtures satisfy local readout/update
  consistency by the universal argument, and a uniformly available Phi_1
  still separates each from its cone. Finite controls must agree.
- **DT disguised:** the two-direction written equivalence shows that the
  proposed complete-dual-test clause merely restates preservation; fixture
  pullback violations and both positive comparisons must agree. This earns
  no physical source.
- **PS disqualified:** its written implication already grants Q3 inclusion,
  or it fails the quantum PSD comparison. Do not use its fixture exclusions
  to claim an independent source.
- **UNRESOLVED/control failure:** a universal premise check, comparison or
  exact control disagrees or is missing. Record that limitation; do not
  repair the frozen scope or promote a finite sample. After F a failed frozen
  script/control halts the round under V3 S12.

No SOURCE-DERIVATION label is available from the finite computation alone.
The result note carries Outcome: OI-STATE-OPERATION-SOURCE-1-READ only when
the bounded read and all exact/native controls hold. Its earned reading is
exactly this sentence, once:

Local product-test and rank-one update consistency does not imply preservation of the given pair cone; complete-dual-test pullback closure restates that preservation; product-test state saturation grants Q3 inclusion and fails the quantum PSD comparison. No physical compatibility source is derived by this bounded audit.

The result distinguishes [W], [X], [A] and [D], records no new kernel theorem,
does not claim a full physical countermodel and preserves all K2/K3/P0 and
finite-carrier statuses. Under §A.31 the prior bridge non-implication stays
CONFIRMING; this round adds a bounded source-route assessment, not a new
foundational gap or an exhaustive impossibility statement.

## Invariants and checkpoints

| invariant | checkpoint |
|---|---|
| D is current #818 main, not the old bridge base | exact D object and delta(D,F) control-plane-only check |
| state cone and tests fixed independently of operations | LC/DT/PS definitions and [W] state/filter argument; no reachable-state definition |
| every retained premise explicit for both fixtures | premise ledger; K_B [W] and ZF [A] proofs; original independent fixture checker |
| every exclusion operation uniformly available | Phi_1 / finite_protocol_spectator license; metadata mutation substituting fullClass-only theorem rejected |
| no unearned quantum inclusion/equality | PS and replacement confound argument, indefinite defect and omitted PSD projector controls |
| all positive comparisons present | quantum PSD and classical diagonal checks; either missing flag rejected by policy mutations |
| no flow/duality disguise | two-direction [W] duality and closed-cone-flow proofs; off-frame obligation kept separate |
| exact adopted construction | kernel-source digest; independently composed circuit and branch identities |
| declared finite coverage | 640 readout and 320 conditional-filter cases; reduced coverage rejected |
| frozen source, working scripts and workflow | object and working-byte hashes; predicted workflow digest |
| control plane unchanged after F | object comparison of preregistration/amendments; native V3 G7 |
| bounded execution and record population | controls' D-to-subject path check and record allowlist; V3 governed paths |
| fresh computations, deterministic record | fresh stdout versus saved probe-output.json and fixture-output.txt; empty stderr and zero exit |
| scoped result, no source promotion | exact earned reading and outcome; no SOURCE-DERIVATION in result |
| constructions and policy gates discriminate | 4 script mutations, 6 metadata mutations, positive native object fixture and 5 object mutations in design validation |
| historical records preserved | legacy_records_check.py; v3_verifier.py --receipts; artifact placement |

## Disclosed design evidence and prospective stages

Design computations preceded this native freeze. They are disclosed [D], not
blind predictions: the local controls passed with both comparison flags true
and the two negative separations; the unchanged independent checker passed
53 controls. The new probe passed 1161 controls, including 640 product-readout
and 320 conditional-filter cases. The prospective controls pass a positive fixture, four
construction mutations (identity, witness phase, sharp normalization,
non-PSD positive input) and six policy mutations (inventory-only theorem,
missing quantum/classical comparison, missing fixture, missing coverage,
upgraded universal evidence). Design run
[38384380519](https://github.com/amaybaum/incompleteness/actions/runs/38384380519)
at source commit 1a5105507f6d13cca4bbb2c94b6a49644a866e52 passed; its legacy
records, native receipts and placement checks passed. It is not F's attestation.
Local disposable Git objects also passed the native object controls. Five
object mutations were rejected: changed control plane, changed probe bytes,
changed workflow, an unowned changed path and an unexpected record file.
These temporary objects are [D] validation, not owner-designated F/E or native
execution. The V3 parser accepts the control-plane-only delta, the verifier's
self-test and 140-vector corpus pass, and the local legacy/receipt checks
retain all 303 records and 46 receipts.
The bridge's anonymous Lean instance was separately compiled at eda945a in
run 38353551590; no Lean source changed between its base and D.

1. Review this concrete control plane on its one PR from D. Hold the branch
   at the proposed exact F; obtain an all-green workflow_dispatch run with
   that head_sha, then the owner's F designation. No execution before it.
2. S1, linear child of F: add the four frozen record files and predicted verify
   workflow. Run fresh probe/fixture checks with empty stderr; save stdout as
   probe-output.json and fixture-output.txt. Commit those saved outputs with
   the files. Run native controls against that exact object and the mutation
   tests. Keep the original design computations separate from this execution.
3. S2: add result.md with the scoped outcome and earned reading, the saved
   measurements, labelled universal arguments and unchanged historical
   statuses. Native controls must pass. Obtain E's exact-head all-green
   workflow_dispatch run and the owner's E designation.
4. Reconcile later main only after E, by merits. Build the non-sealing native
   receipt; require v3_verifier --verify-round Q to print VERDICT HOLDS before
   ordinary review and merge. The design-only workflow never lands.

No step here sources a working physical state–operation compatibility
principle. Subsequent candidates, including any independently derived
history-to-pair bridge, need a new bounded assessment/control plane. Limit
availability remains deferred, with its irrelevance to the closed-cone
preservation implication already explicit.
