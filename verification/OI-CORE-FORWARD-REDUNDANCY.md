# The forward redundancy of the OI core

`OIBridge/CompletedOI.lean` §F — `qm_implies_oiCore`, `oiCore_forward_redundancy`.

This is not a round. It is a reading, frozen, because the equivalence theorem admits a stronger
paraphrase than the formalization supports and the paraphrase is the natural one to reach for.

## The three statements, and only these three

**Containment.** Every theory in the characterized quantum class realizes the sealed OI core:

> `qm_implies_oiCore : ExactAllFiniteEndomorphicQuantumOps T → OICore T`

The route is `QM → full composite unitary control → RealizesSealedOICore`. The implication was
always present inside `oiPlus_of_qm`, whose first conjunct is exactly
`realizesSealedOICore_of_control T (physical_of_exactAll T h).2.2.1`; it is stated separately here
because it is easy to miss and easier to misread.

**Redundancy.** The OI conjunct does no work in the forward derivation:

> `completedOI_iff_physical : CompletedOI T ↔ PhysicalCompletionConditions T`

Completed OI is the core plus the five physical conditions, and the five conditions alone are
already equivalent to finite operational QM, because full control realizes the core. Delete the
core conjunct and the characterization is unchanged. What selects quantum mechanics from the
OI-compatible class is coherent controllability, not observational incompleteness.

**No ontological necessity.** Neither statement shows that quantum mechanics needs a hidden
sub-quantum level, and nothing in the tree proves it. `OICore` unfolds to `RealizesSealedOICore`,
which is `CoreC1C4` together with availability of the core's relabellings and readouts: an
**existential realizability** condition — the theory *can implement* a particular four-state gadget
with hidden memory and history readback. A containment theorem about such a condition is not an
explanatory one. Read in the narrow core-containment sense the phrase "quantum mechanics requires
OI" is just `qm_implies_oiCore`; read as a claim about ontology it is unsupported.

There is also a specific place the strong reading breaks, worth recording so it is not
rediscovered. If the state is the density matrix then informationally complete measurement families
exist, so the universally quantified form of observational incompleteness — *no* accessible readout
family determines the underlying state — is false at the quantum-state level. Any necessity theorem
of the strong kind would therefore have to quantify over a level beneath the density matrix, and
asserting that such a level exists is a hidden-variable commitment rather than a consequence of
quantum mechanics.

## The audit entry

`oiCore_forward_redundancy` collects the three in one place: containment holds, the core is
redundant in the forward direction, and the converse fails —

> `(∀ T, QM T → OICore T) ∧ (∀ T, CompletedOI T ↔ PhysicalCompletionConditions T)`
> `∧ (∃ T, OICore T ∧ ¬ QM T)`

the third conjunct being `oiCore_not_completedOI` transported through `completedOI_iff_qm`, and
witnessed by `diagTheory`.

## What the core is still for, which is not nothing

`OICore` **defines what counts as an OI realization**. That is what gives `oiCore_not_completedOI`
and `oi_alone_not_qm` their content: non-quantum theories satisfy the core, so "bare OI is not
enough" is a statement about a populated class rather than an empty one, and every countermodel in
the programme is built to satisfy it. Its job is to seal the class. It is not the ingredient that
produces the theorem, and the two roles must not be traded for one another.

The one-line reading:

> the OI core defines what counts as an OI realization; controllability is what selects quantum
> mechanics from within it.

## The lint

`tools/claims_check.py` carries an `OI_CLAIMS` class with its own marker list, separate from the
general one — the general markers include "cannot" and "does not", which would let the dangerous
sentences escape through the very words that make them dangerous. The guarded forms are: QM
requiring OI or observational incompleteness; quantum mechanics being unable to exist without
something; QM requiring hidden information, variables, states or ontology; OI or ignorance causing,
producing or explaining quantum mechanics; and the contrapositive. Each is accepted only when the
paragraph carries the core-containment qualification. The guard is exercised against a fixture that
makes it fire, so it is a gate rather than a decoration.

## What this record does not say

That the equivalence theorem is weakened. `oiPlus_iff_qm` and `carrier_general_oiPlus` are
untouched: the completion conditions remain necessary and sufficient for finite operational QM in
the stated frame, and that is the load-bearing result. That the OI programme is circular — it is
not; the core is satisfiable by non-quantum theories, which is what makes the negative results
meaningful. That anything here bears on CT1–CT3 or on the manuscripts' physical content. That the
redundancy is new: `completedOI_iff_physical` has been in the kernel and is already labelled
**THE REDUNDANCY, MADE EXPLICIT**; what is new is that the forward implication now has a name of
its own and that the reading is frozen against paraphrase.
