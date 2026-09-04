# OI-N — the exploratory necessity thread

`OIBridge/PassiveObservation.lean`; guard `R7-OIN` in `verification/lean/edge_rigidity_probe.py`.

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
exact finite-dimensional boundary is N3 — not as a proved obstruction, and not as a generic
information–disturbance slogan either.

## OI-N3 — the exact boundary: open

Target: *complete passive observability iff the finite-dimensional observable algebra is
commutative.* The commutative direction is N2. The converse for a general `⊕_i M_{d_i}` is the real
content and is **not** proved here. The one step where inferring it from the simple case would be a
gap: an instrument on a direct sum may move probability *between* blocks while still summing to the
identity, so the block-diagonal restriction has to be argued, not assumed. N1 applies within a block
of dimension `d_i > 1` only once that restriction is in hand.

## OI-N4 — relation to `OICore`: open

Whether passive incompleteness implies any existing OI condition, whether `OICore` implies passive
incompleteness, or whether they are independent notions with different roles. The likely
distinction — `OICore` is the existence of a hidden-memory/readback realization; OI-N is the
impossibility of complete nondisturbing readout in a noncommutative theory — is not a theorem and
must not be traded on until it is.

## OI-N5 — the internal observer: not started

Deferred until N1–N4 are settled. Imports no hidden-variable or subquantum assumption.

## What this thread does not claim

That `QM ⟹ a hidden OI ontology`; standard quantum mechanics admits informationally complete
measurements, and OI-N concerns the conjunction of completeness with nondisturbance. That N1 or N2
bears on the OI ↔ QM equivalence, on the concrete-cut freeze, or on CT3. That a passive instrument's
silence is an observer, or that "passive" here coincides with the passive quotient of
`PassiveQuotient.lean`, which is a different object. That N3's converse holds.
