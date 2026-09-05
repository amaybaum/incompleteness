# OI-N — the exploratory necessity thread

`OIBridge/PassiveObservation.lean` (N1, N2), `OIBridge/CentralObservation.lean` (N3),
`OIBridge/PassiveIndependence.lean` (N4), `OIBridge/InternalObserver.lean` (N5); guard `R7-OIN` in
`verification/lean/edge_rigidity_probe.py`.

**Status: exploratory.** This thread is deliberately separate from the frozen OI ↔ QM equivalence and
from the concrete-cut freeze. Nothing here may be cited as a consequence of the existing
formalization until it is proved and scoped on its own. It opens from the frozen status of
`CONCRETE-CUT-FREEZE.md` and does not reopen it.

## The question

The kernel result `qm_implies_oiCore` is containment: a theory in the characterized quantum class is
rich enough to realize the sealed OI gadget. It does not say quantum mechanics requires a hidden
ontology, that every quantum state is observationally incomplete, or that OI causes quantumness. The
exploratory question is whether quantum mechanics nevertheless forces a stronger, intrinsic
incompleteness that appeals to no hidden variables:

> is nonclassical quantum structure exactly the obstruction to complete passive observation?

**Passive**: a finite instrument `{F_a}` whose nonselective channel is the identity, `∑ a, F a = id`.
**Complete**: distinct states produce distinct outcome laws. The quantum reading: learn the state
while leaving every state unchanged on average.

## OI-N1 — the full matrix algebra: proved

`passive_branch_scalar`: every branch of a passive instrument on `Matrix S S ℂ` is a scalar multiple
of the identity. `passive_outcome_state_independent`: each outcome's probability is the same for
every state of unit trace. `no_complete_passive_observation`: when `S` has at least two elements, no
passive instrument separates states — two distinct pure states receive the identical outcome law.

The proof is the Choi argument, kernel-closed. The identity channel has the rank-one Choi matrix
`ω ω†` (`choiMatrix_id`, from `choiMatrix_conjChannel` at `V = 1`). The branches' Choi matrices are
positive semidefinite and sum to it. A positive semidefinite summand of a rank-one positive
semidefinite matrix is a scalar multiple of it (`psd_summand_of_rankOne`): the summand kills `v^⊥`,
by `PosSemidef.dotProduct_mulVec_zero_iff`; hermiticity then puts `A v` in the double orthogonal
complement of `v`, which is `span v`, by an elementary computation (`exists_smul_of_orth`); and
comparing on `x = α v + w` finishes. Choi injectivity returns the branch.

All ten named results print `[propext, Classical.choice, Quot.sound]` and nothing else.

## OI-N2 — the commutative control: proved

On the diagonal subalgebra the pinching instrument `X ↦ E_aa X E_aa` is completely positive
(`pinching_cp`), acts as the identity on every diagonal matrix (`pinching_passive_on_diagonal`), and
separates diagonal states (`pinching_separates_diagonal`). The scope point that keeps N2 honest is
also proved: on the full matrix algebra the same instrument's nonselective channel is the dephasing
map (`pinching_sum_apply`), and with two atoms it is not a passive instrument there
(`pinching_not_passive`, witness `E_{st}`). N1 excludes complete passive observation on a full matrix algebra; N2 supplies the diagonal
commutative control. Their contrast identifies noncommutativity as the candidate obstruction whose
exact finite-dimensional boundary is N3 — on the strength of N1 and N2 alone a candidate, not a
generic information–disturbance slogan; N3 below is what makes it the obstruction.

## OI-N3 — the exact boundary: proved, as a classification

`OIBridge/CentralObservation.lean`. The finite-dimensional C*-algebra `⊕_i M_{d_i}` is taken in its
block-diagonal matrix form, for a labelling `blk : S → I` of basis states by blocks; a passive
instrument on it (`IsBlockPassiveInstrument`) is a finite family of maps on the ambient matrix
algebra, completely positive there, whose nonselective channel fixes every block-diagonal matrix.

**The central theorem** (`central_classification`): every passive instrument on `⊕_i M_{d_i}`
induces a classical stochastic observation of the center. There is a matrix `c : O → I → ℂ` with

> `tr (F_a ρ) = ∑_i c_{a,i} · tr (P_i ρ P_i)` for every block-diagonal `ρ`,

`c_{a,i} ≥ 0` on every nonempty block from complete positivity (evaluate on a pure state of the
block and read the diagonal), and `∑_a c_{a,i} = 1` on every nonempty block from passivity. Nothing
inside a block is read.

The two steps beyond the simple case, both proved rather than assumed. **Block preservation**
(`branch_preserves_block`): passivity on the block projector `P_i` says the branches' images of
`P_i` sum to `P_i`, whose diagonal vanishes off block `i`; each image is positive semidefinite, so
each has zero diagonal there; writing the branch in Kraus form (`exists_kraus`, from the kernel's
positive semidefinite factorization `psdFactorization_discharged` and `kraus_of_choi_factor`), the
diagonal of `K P_i K†` at `t` is the squared norm of the block-`i` part of row `t` of `K`, so every
Kraus operator vanishes between distinct blocks (`kraus_block_vanish`) and every branch maps block
`i` into block `i`. This is the step an instrument that moved probability between blocks would
violate; passivity forbids it. **Blockwise scalars** (`branch_scalar_on_block`): restricting a branch
to the fibre of block `i` (`restrictMap`, extension by zero followed by the principal submatrix) has
Choi matrix a principal submatrix of the original (`choiMatrix_restrictMap`), hence completely
positive, and the restricted family is a passive instrument on the fibre in N1's sense
(`restricted_passive`); N1 makes it a scalar `c_{a,i}` there, and block preservation carries the
scalar back to the ambient algebra.

**The control** (`blockPinch`): the branch that keeps block `i` and discards every other block,
`X ↦ P_i X P_i`, is completely positive, passive on the algebra (`blockPinch_passive`), and reads the
block weights exactly (`blockPinch_trace`).

**The boundary.** A block with two basis states carries two pure states every passive instrument
confuses (`no_complete_passive_of_block`); with singleton blocks the control separates states
(`blockPinch_separates`). So some passive instrument observes `⊕_i M_{d_i}` completely if and only if
every `d_i = 1` (`complete_passive_iff_injective`), if and only if the block-diagonal algebra is
commutative (`injective_iff_commutative`, `complete_passive_iff_commutative`). Noncommutativity is the
obstruction, exactly: this is the finite-dimensional boundary the N1/N2 contrast pointed at.

All thirteen named results print `[propext, Classical.choice, Quot.sound]` and nothing else.

**Scope.** The Wedderburn–Artin identification of an abstract finite-dimensional C*-algebra with a
block-diagonal matrix algebra is standard and is not formalized; the theorem is stated for the
block-diagonal form. Intrinsic completely positive instruments on the block-diagonal algebra admit
the corresponding ambient extension by the standard block conditional expectation; that transport
is not formalized here, and the kernel statements are stated for `IsBlockPassiveInstrument` as
defined. The classification is one direction: every passive instrument induces a stochastic
observation of the center; no converse constructing an instrument from an arbitrary stochastic
matrix is stated. "Passive" is the nonselective channel fixing the algebra, and "complete" is
separation of block-diagonal density matrices by outcome laws; both are the definitions N1 fixed,
transported to the direct sum.

## OI-N4 — relation to `OICore`: proved, as theory-insensitivity

`OIBridge/PassiveIndependence.lean`. `OICore T` says a finite operational theory `T` on the qubit
realizes the sealed OI core: the passive step `σ` and the control `τ` of the hidden-memory gadget
are available as permutation channels at ancilla level four, and the native readout reproduces the
classical OI comb (`RealizesSealedOICore`). It is a statement about which operations `T` makes
available. The theory-level passive notion is `PassivelyIncomplete T`: no family `T.avail` makes
available on the system is both passive and state-separating.

**Passive incompleteness is carrier-intrinsic** (`passivelyIncomplete_of_card`,
`passivelyIncomplete_qubit`). By N1 it holds for every theory on a carrier with two or more states,
whatever `T` makes available. The property does not vary with `T` at all.

**The OI core varies with `T`.** `diagTheory` realizes it (`diag_realizesSealedOICore`, from the
minimality audit). `labelTheory`, built here, does not: it is `diagTheory` with diagonal preservation
on composite operations replaced by ancilla-label preservation (`KeepsLabels` — every ancilla block
is mapped into itself, so nothing moves information between ancilla values) and with reference-tested
preparations alone. The local Lüders readout keeps labels (`keepsLabels_localLuders`), so the theory
closes under the structure's rules; the OI control `τ` flips the ancilla's second bit and carries the
unit at composite index `(0, 0)` to `(0, 1)` (`coreIdx_tau_symm`, `tau_moves_label`), so it is
unavailable, and `labelTheory` does not realize the core (`label_not_oiCore`).

**The diagram** (`passive_nondiscriminating`):

> every `T` is passively incomplete; some `T` realizes the OI core (`diagTheory`); some `T` does not
> (`labelTheory`).

So `OICore T → PassivelyIncomplete T` holds for every `T`, but the proof does not consult the
hypothesis (`oiCore_to_passive_vacuous` is N1 on the carrier); and `PassivelyIncomplete T → OICore T`
fails (`passive_not_implies_oiCore`, `passivelyIncomplete_without_oiCore`). The exact logic is
asymmetric — one implication holds, vacuously, and the other does not — and the content is that
passive incompleteness is theory-insensitive on a nontrivial full matrix algebra, so it carries no
discriminatory information about whether the OI core is realized. The two notions are orthogonal:
one is fixed by the observable algebra, the other by the theory's hidden-memory and control
structure. This is the result that keeps OI-N from being misread as a hidden-ontology necessity
theorem — passive incompleteness holds in a theory that realizes no OI core whatever.

**What varies is the sector, not the OI status** (`sector_diagram`). `PassivelyCompleteOnDiagonal T`
asks for an available family, completely positive, whose nonselective channel fixes every diagonal
matrix and which separates diagonal matrices by outcome law. The pinching instrument is a Kraus family
(`pinching_isKrausFamily`, through the kernel's factorization) and preserves diagonal states
(`pinching_preservesDiag`), so it is available in both `diagTheory` and `labelTheory`, and N2 makes
both theories passively complete on their commutative sector
(`diag_passivelyCompleteOnDiagonal`, `label_passivelyCompleteOnDiagonal`) while both are passively
incomplete on the full algebra. Passive (in)completeness tracks the observable algebra the states live
in — the N3 boundary — and is the same on both sides of the OI-core line.

All fourteen named results print `[propext, Classical.choice, Quot.sound]` and nothing else.

**Scope.** `labelTheory` is a witness against `OICore` and nothing more: none of the five physical
completion conditions is claimed for it. The cell `OICore ∧ ¬ PassivelyCompleteOnDiagonal` is neither
inhabited nor shown empty; the sector diagram does not need it. `PassivelyIncomplete` quantifies over
system-level availability; a notion relativized to composite carriers is not defined.

## OI-N5 — the internal observer: proved, as rigidity

`OIBridge/InternalObserver.lean`. An internal observer stores its outcome inside the system it
observes. On a carrier `S` with a **record map** `blk : S → O` — for a system-plus-register carrier
`A × B` the record is a visible function `rec : B → O` of the register, `blk (x, b) = rec b`
(`recBlk`) — an instrument **records** (`Records`) when the output of branch `o` on every
block-diagonal input lies in record block `o`, and an **internal observer** (`IsInternalObserver`)
is a recording instrument that is passive on the record-block algebra, in N3's sense. Imports no
hidden-variable or subquantum assumption.

**N5.0 — full-joint passivity and nontrivial self-recording are incompatible**
(`no_full_passive_self_record`). If the instrument is passive on the full joint algebra and the
record can take two values, N1 makes every branch a scalar multiple of the identity; a scalar
multiple of the identity whose output on the projector of a different nonempty block must lie in
record block `o` is zero; so every branch vanishes and the branches cannot sum to the identity.

**N5.1 — rigidity** (`branch_kills_other_block`, `branch_fixes_own_block`,
`internal_branch_eq_blockPart`, `internal_outcome_law`). Record-block passivity gives block
preservation (N3, `branch_preserves_block`), the record condition gives the opposite confinement,
and a matrix supported in two distinct blocks is zero; so branch `o` annihilates every other record
block, and, since the branches sum to the identity, fixes its own. On every block-diagonal state

> `F_o ρ = P_o ρ P_o` and `p(o | ρ) = tr (P_o ρ P_o)`.

A passive internal observer cannot write a new record; it can only reveal which record was already
present.

**N5.2 — the boundary** (`internal_complete_iff`, `recBlk_not_injective`,
`no_complete_internal_observer`). Some internal observer observes the algebra completely if and
only if every record block is one-dimensional, i.e. the record map is injective — the block-label
instrument records (`blockPinch_records`, `blockPinch_internal`) and is the witness. For a separate
register recording a system with more than one state every record block contains all of `A`, so no
internal observer using the register as its record observes `A × B` completely and passively,
whatever function of the register the record is.

**Controls.** The singleton record partition (`classical_control`): when the record resolves the
whole joint classical state, the block-label instrument is a complete passive internal observer,
by N3 at `blk = id`. The non-passive recorder (`recordInstr`, "measure `A` in its basis and write
the result into the register", `F_a = ∑_b (E_aa ⊗ |a⟩⟨b|)(·)(E_aa ⊗ |a⟩⟨b|)†`): completely positive
(`recordInstr_cp`), records (`recordInstr_records`), and genuinely creates a record — a state whose
register reads `b ≠ a` is carried by branch `a` to a nonzero state whose register reads `a`
(`recordInstr_writes`) — but its nonselective channel dephases the system and resets the register,
so it is not passive even on the record-block algebra (`recordInstr_not_passive`) and is not an
internal observer (`recordInstr_not_internal`). Acquiring a genuinely new record changes the joint
system; passive self-observation can only read an existing classical record.

All fourteen named results print `[propext, Classical.choice, Quot.sound]` and nothing else.

**Scope.** The record semantics is the one `Records` fixes — the outcome is a function of a
register, read on block-diagonal inputs; an observer whose record is not of that form is not
modelled. Nothing here concerns consciousness, self-modelling, or an observer's own ontology, and
nothing here bears on `OICore`: N4 shows passive facts do not discriminate it, and N5 does not
reopen that.

## What this thread does not claim

That `QM ⟹ a hidden OI ontology`; standard quantum mechanics admits informationally complete
measurements, and OI-N concerns the conjunction of completeness with nondisturbance; N4 makes the
point a theorem, since passive incompleteness holds in `labelTheory`, which realizes no OI core. That
N1–N5 bear on the OI ↔ QM equivalence, on the concrete-cut freeze, or on CT3. That N5 says anything
about consciousness, self-modelling, or an observer's own ontology. That a passive
instrument's silence is an observer, or that "passive" here coincides with the passive quotient of
`PassiveQuotient.lean`, which is a different object. That N3 says anything about infinite-dimensional
algebras, about instruments with infinitely many outcomes, or about an abstract C*-algebra before it
is put in block-diagonal form.
