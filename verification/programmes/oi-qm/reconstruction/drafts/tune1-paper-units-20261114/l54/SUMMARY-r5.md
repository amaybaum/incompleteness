# L5.4: summary of `L54-r5.md`

**Headline.** Classes A, B and C fail Q5′ under the stated additive-rule, target and record
conditions. L5.4, L5.5 and L5.6 are decided only within that scope.
**Status.** Paper-only; nothing computed; not independently verified. r1 reviewed and r2 confirmed
(both ACCEPT WITH CHANGES, one non-author model reviewer); r3 applies C1–C5; r4 applies the
independent check's eight corrections and was confirmed at `de22ceab` (ACCEPT WITH CHANGES); r5
applies those changes and is itself unreviewed.

**The question.** Can the linear rule R-lin, watched through one fixed region, imitate one qubit?
L5.4 asked whether heralded preparations let it meet the gate, read and preparation conditions.

**Theorem 1.** Assume: (1) an additive rule, R-lin at any alphabet size; (2) a finite torus, or the
infinite lattice under H-∞; (3) labels as block content, or written each round under H-write, in an
order fixed in advance; (4) H-μ, with any law; (5) one apparatus; (6) each round's record is the
complete history of the read region; (7) the two reads are compared with ideal repeatable reads
whose record law depends on label and class only, `a·b ∈ [−1/2, 1/2]`; (8) the read condition is
posed for the empty preparation. Then Q5′ cannot hold below error 1/96 (below 1/128 without (8)).

**Why.** An additive rule only shifts each complete record by a fixed amount, so the dependence
between consecutive records cannot change with the labels; the ideal reads need it to change.

**What it is not.** It is specific to additive dynamics, through a property additivity implies, and
is not a no-go for every rule under this interface. A designed non-additive rule outside the schema
meets Q5′ in exchange mode under H-write (one author, one independent check); it fails Q3′ and Q6′
(one author, one independent check) and Q2 (one derivation, not checked), and is not in class D,
so it is no evidence for any OI rule.

**Dependence on the record convention and the target.** The proof needs complete-history records
and the product form of the target given the classes. It does not use the slice two consecutive
records share. A separate rule-free lemma about that slice is definitional: a property of how the
records are cut into rounds, not of any dynamics (one author, one independent check). Retained
memory is compatible with the selection requirement if each record is split, the same way for
every label, into a retained part and an outcome part (checker's addition: one derivation, not
checked). Under an outcome-class-only comparison the argument is unavailable.

**Still open.** The rounded non-linear rule R-nl (class D); whether label shifts can supply the
gate family; record conventions other than complete histories.

**Relation to `main`.** The mechanism is already recorded (MECH-1 Corollary A′; OA-1 nodes N2,
N3). New here: the explicit bounds and their consequence for the three open rows. Classified as
elaborating; nothing as new.
