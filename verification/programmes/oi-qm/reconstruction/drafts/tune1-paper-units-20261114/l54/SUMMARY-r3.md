# L5.4: summary of `L54-r3.md`

**Headline.** Classes A, B and C fail Q5′ under its specified target and record conventions.
**Status.** Paper-only; nothing computed; not independently verified. One non-author model
reviewer: r1 reviewed (ACCEPT WITH CHANGES), r2 confirmed (ACCEPT WITH CHANGES, C1–C5); r3 applies
C1–C5 and is itself unreviewed.

**The question.** TUNE-1 asks whether the linear rule R-lin, watched through one fixed region, can
imitate a single qubit to any accuracy. Gap L5.4 asked whether a family that prepares its test
states with heralds (runs kept only when a chosen record occurs) can meet the gate, read and
state-preparation conditions (Q3′, Q5′, Q6′) together.
**The answer.** No, within that scope: the read condition Q5′ already fails before any herald.

**Theorem 1.** Take one TUNE-1 interface and assume all of the following.
1. The rule is additive: R-lin, any alphabet size `q`.
2. The world is a finite torus, or the infinite lattice under the named hypothesis H-∞.
3. Labels are the starting content of program blocks outside the read region, or are written each
   round under the named hypothesis H-write, in an order fixed in advance.
4. H-μ: the law of the unread world is the same whatever labels are used. Any such law is allowed.
5. One apparatus: the same region, control cells, round length, ready state and layout throughout.
6. Each round's record is the complete history of the read region (clause D4).
7. The two reads are compared with ideal repeatable ("Lüders") reads whose record law depends on
   the label and the outcome class only, with directions satisfying `a·b ∈ [−1/2, 1/2]`.
8. The read condition is posed for the empty preparation, with at least two rounds.

Then the read condition cannot hold with error below 1/96. Without item 8, with at least three
rounds, it cannot hold below 1/128.
**Why.** Under an additive rule a label only shifts each round's complete record by a fixed amount,
so the dependence between two consecutive complete records is the same for every choice of labels.
The ideal reads require it to differ between "read `a` twice" and "read `a`, then `b`".

**What it settles.** Under 1–7, every R-lin interface (classes A, B, C) fails Q5′ under its
specified target and record conventions, and so fails the single-qubit target. Within that scope
L5.4, L5.5 and L5.6 have a definite answer, for any witnesses, listed law and control-region size.
**What stays open.** The nonlinear rule R-nl: nothing follows for it. Whether label shifts can
supply the gate family. Coarser records (outcome class only), where the argument is unavailable.

**What the result depends on.** Records are complete histories (item 6); with class-only records
the invariant is lost. The target has no persistent memory (item 7): each round's record is drawn
afresh given its class. The proof compares complete records; change either and it does not carry over.

**Relation to `main`.** The mechanism is already recorded (MECH-1 Corollary A′; OA-1 nodes N2,
N3). New here: the explicit bounds against Q5′ and the consequence for the three open rows;
classified as elaborating, nothing as new. The reviewer-authored results of the confirmation
review (its section 6) are under separate independent check and are not part of the theorem.
