# OI-N — the exploratory necessity thread

`OIBridge/PassiveObservation.lean` (N1, N2), `OIBridge/CentralObservation.lean` (N3); guard `R7-OIN`
in `verification/lean/edge_rigidity_probe.py`.

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

**The central theorem** (`central_classification`): a passive instrument on `⊕_i M_{d_i}` is a
classical stochastic observation of the center. There is a matrix `c : O → I → ℂ` with

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
block-diagonal form. "Passive" is the nonselective channel fixing the algebra, and "complete" is
separation of block-diagonal density matrices by outcome laws; both are the definitions N1 fixed,
transported to the direct sum.

## OI-N4 — relation to `OICore`: open

Whether passive incompleteness implies any existing OI condition, whether `OICore` implies passive
incompleteness, or whether they are independent notions with different roles. The likely
distinction — `OICore` is the existence of a hidden-memory/readback realization; OI-N is the
impossibility of complete nondisturbing readout in a noncommutative theory — is not a theorem and
must not be traded on until it is.

## OI-N5 — the internal observer: not started

Deferred until N4 is settled. Imports no hidden-variable or subquantum assumption.

## What this thread does not claim

That `QM ⟹ a hidden OI ontology`; standard quantum mechanics admits informationally complete
measurements, and OI-N concerns the conjunction of completeness with nondisturbance. That N1, N2 or
N3 bears on the OI ↔ QM equivalence, on the concrete-cut freeze, or on CT3. That a passive
instrument's silence is an observer, or that "passive" here coincides with the passive quotient of
`PassiveQuotient.lean`, which is a different object. That N3 says anything about infinite-dimensional
algebras, about instruments with infinitely many outcomes, or about an abstract C*-algebra before it
is put in block-diagonal form.
