# The OI-N freeze

`verification/OI-N-EXPLORATORY.md` (the thread note), `OIBridge/PassiveObservation.lean` (N1, N2),
`OIBridge/CentralObservation.lean` (N3), `OIBridge/PassiveIndependence.lean` (N4),
`OIBridge/InternalObserver.lean` (N5); guard `R7-OIN` in `verification/lean/edge_rigidity_probe.py`.

**Status: frozen.** The five items of the OI-N thread are proved and merged, and this note states
the endpoint once, in the form the guard enforces, so that later work builds on it rather than
re-deriving or quietly strengthening it. The thread's own status line stays "exploratory" in the
sense the note gives it: separate from the frozen OI ↔ QM equivalence and from the concrete-cut
freeze, and citable only for what its modules prove. Extending the thread needs a new charter; this
note does not open one.

## The endpoint

Four statements, each the name of a kernel theorem.

1. **Noncommutativity forbids complete passive observation.** On a finite-dimensional C*-algebra in
   block-diagonal form, some passive instrument observes the algebra completely if and only if the
   algebra is commutative (`complete_passive_iff_commutative`); every passive instrument induces a
   classical stochastic observation of the center (`central_classification`).
2. **Passive incompleteness does not diagnose `OICore`.** Passive incompleteness holds in every
   finite operational theory on a carrier with two or more states (`passivelyIncomplete_of_card`),
   so it is theory-insensitive and carries no discriminatory information about whether the OI
   core is realized; the forward implication is vacuous (`oiCore_to_passive_vacuous`) and the
   converse fails (`passivelyIncomplete_without_oiCore`, witness `labelTheory`).
3. **A passive internal observer can only read an existing record.** On every block-diagonal
   state each branch of a passive internal observer is the record projection,
   `F_o ρ = P_o ρ P_o` (`internal_branch_eq_blockPart`), with outcome law `tr (P_o ρ P_o)`
   (`internal_outcome_law`).
4. **Creating a genuinely new internal record requires changing the joint system.** The recorder
   that measures the system and writes the register creates a record (`recordInstr_writes`) and is
   not passive on the record-block algebra (`recordInstr_not_passive`); passivity on the full joint
   algebra is incompatible with a two-valued record altogether (`no_full_passive_self_record`).

## What is frozen, and where each statement lives

**N1, N2 — the two ends.** No passive instrument on a full matrix algebra with two or more states
separates states (`no_complete_passive_observation`); the pinching instrument is the commutative
control, passive and complete on diagonal matrices and dephasing, not passive, on the full algebra
(`pinching_passive_on_diagonal`, `pinching_separates_diagonal`, `pinching_not_passive`). N1 and N2
alone name noncommutativity as the candidate obstruction; N3 is what makes it the obstruction.

**N3 — the classification and the boundary.** Block preservation is derived from passivity on the
block projectors through the Kraus form, not assumed (`branch_preserves_block`); restriction to a
block has Choi matrix a principal submatrix (`choiMatrix_restrictMap`); the classification is one
direction, every passive instrument induces a stochastic observation of the center, with no converse
constructor from an arbitrary stochastic matrix; the boundary is injectivity of the labelling —
each block contains at most one basis state, every nonempty block has dimension one
(`complete_passive_iff_injective`, `injective_iff_commutative`). The intrinsic-to-ambient transport
through the block conditional expectation is not formalized; the kernel statements are for
`IsBlockPassiveInstrument` as defined.

**N4 — theory-insensitivity.** One implication holds vacuously and the other fails
(`passive_nondiscriminating`); the two notions are orthogonal, one fixed by the observable algebra
and the other by the theory's hidden-memory and control structure; the sector, not the OI status,
is what varies (`sector_diagram`). `labelTheory` is a witness against `OICore` and nothing more.

**N5 — the internal observer.** Record semantics is the one `Records` fixes: the outcome is a
function of a register, read on block-diagonal inputs. Rigidity (`branch_kills_other_block`,
`branch_fixes_own_block`, `internal_branch_eq_blockPart`), the boundary at injectivity of the record
map (`internal_complete_iff`, `no_complete_internal_observer`), the singleton-partition control
(`classical_control`) and the recorder (`recordInstr_cp`, `recordInstr_records`,
`recordInstr_writes`, `recordInstr_not_passive`, `recordInstr_not_internal`).

Fifty-one named results across the four modules, each printing only `propext`, `Classical.choice`,
`Quot.sound`.

## How the freeze is enforced

`R7-OIN` re-runs on every CI pass. It pins every named result of the four modules by its
`#print axioms` line, the definitions the thread depends on, the verbatim shapes of the
classification, the rigidity statement and the two boundaries, the status line of each item in the
thread note, the candidate-obstruction wording of N1/N2, the one-directional "induces" wording of
N3, the theory-insensitive wording of N4 with the symmetric vocabulary forbidden, the
"at most one carrier state" wording of the boundaries with the literal "every block is
one-dimensional" forbidden, and this note's endpoint. Drift in any of them fails the probe.

## What the freeze does not claim

That quantum mechanics requires OI, or that passive incompleteness is evidence for a hidden
ontology: `qm_implies_oiCore` is containment, and statement 2 says passive facts do not
discriminate the OI core. That the two notions of statement 2 are logically independent or that
neither implies the other: one implication holds, vacuously. That anything here bears on the
OI ↔ QM equivalence, on the concrete-cut freeze, or on CT3. That the stochastic-center
classification has a converse, that the ambient transport is formalized, or that `labelTheory`
satisfies any completion condition. That N5 says anything about consciousness, self-modelling, or
an observer's own ontology, or about an observer whose record is not a function of a register.
That any statement holds in infinite dimension or for infinitely many outcomes.
