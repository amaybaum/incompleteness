# KERNEL-VAC-1 — checkpoint 2: the sole monomial-source witness

Status: candidate proof, ordinary CI and independent non-author review pending.
This is execution checkpoint **2 of at most 3**. It does not designate E or
claim a final REPAIRED disposition. [Checkpoint 1](checkpoint-1.md) is preserved
at `c478b77386fffa6e1eebb93a2d2c6091d26d9139`.

The exact new target is
`SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2))`,
named `OIBridge.ReadWriteNonvacuity.permTheory_fin2_monomialSource`.
The source proof introduces `n`, `V` and the original availability hypothesis
without restricting `n`, the rank, norm, isometry status or choice of `V`.

`permTheory` is the existing `genTheory permClass permClass_arch`. Its
`availExt` is `InstAvail permClass`; `realized_of_instAvail permClass_arch`
supplies a finite Kraus family in the same class for each available branch.
The unchanged `genTheory` supplies identity, coarse-graining, feed-forward,
uniform preparation, post-composition, native readout and discard fields.
The unchanged `permClass_arch` proves the class closure obligations used by
that construction. This reuses the actual structure, not an assumed source
predicate, an altered operation set or a newly postulated theory.

For the same available channel, evaluation on each matrix unit equates
`V a b * star (V c d)` to the sum of the corresponding Kraus products. Every
product with two distinct entries in one row or column is zero for every
class member. The same products therefore vanish for `V`, giving
`IsSubmonomial V`; the existing `submonomial_monomial` converts that to the
unchanged `IsMonomial V`. This proves the statement for **every matrix
representative**, not just the selected Kraus family. The proof lemmas need
no `Nonempty` instance: at `n = 0`, the row/column obligations quantify over
the empty carrier and the existing finite partial-injection extension theorem
still applies. Zero and rank-deficient representatives are included.

This is a mathematical theory witness, not evidence that a native observer
physically realizes `permTheory`. The surviving implications retain exactly
their conditional scope:

> A theory whose available composite conjugations are all monomial has no
> composite unitary control on `Fin 2`, because control would make the
> non-monomial `rot` available.

Its existing QM corollary excludes `ExactAllFiniteEndomorphicQuantumOps` for
that same theory under that same hypothesis. Neither theorem is duplicated
or changed here. No universal read/write physical impossibility follows.

The census changes with this proof extension; the root import from checkpoint
1 remains in place. No local Lean, numerical research, special dispatch or
rerun was performed. Remaining obligations are kernel/axiom validation,
independent review and checkpoint 3's citation/registry closeout. If this
target remains unestablished within the three-checkpoint cap after the defect
control passes, its status must be recorded as refuted, unproved or unfinished
and the old antecedent retired as evidence. No second candidate is authorized.

Goal: [OI correctness issue #1188](https://github.com/amaybaum/incompleteness/issues/1188).
