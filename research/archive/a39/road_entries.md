### The census of `{0, 1}` straight lines at the product stratum

**Future exact enumeration, not an A38 result, and not a dependency of either direction below.** Act 38
(`A38-NON-DITA-WITNESS-PROVED`; receipt `verification/receipts/A38.json`) exhibited one exponent matrix
`E` with entries in `{0, 1}` for which `SIG ∘ u^E` is a complex Hadamard matrix at every unit `u` and,
for every unit `u ∉ {1, −1}`, admits no Diţă structure. Call an exponent matrix with that realizability
property a straight line through the certified stratum point. The census asks for every straight line
in a fixed finite domain — exponent matrices with entries in `{0, 1}` and a zero first row, taken modulo
the gauge, the stabilizer of the point and sign — and for the classification of each against the
eighteen Diţă structures of the point: which lie identically in some structure and which in none.
Membership of a straight line in a structure is a linear condition on its exponent matrix and is
decided exactly.

An exhaustive search of this domain has to be streaming: solutions are produced by a depth-first search
over rows with exact pair-compatibility tables and are reduced, as they are produced, to a canonical
signature — the joint level-set partition, or the orbit representative — so that memory is bounded by
the number of distinct signatures rather than by the number of solutions. No count, classification or
completeness statement is claimed; each would be the object of a round of its own.


### Minimal support of a non-Diţă straight line at the product stratum

**Future classification, not an A38 result, and independent of the census and of the three-parameter
family.** Act 38's witness `E = A + B + C` has 48 nonzero entries. Whether a straight line through the
certified stratum point that lies identically in none of the eighteen Diţă structures can have smaller
support, in any gauge and after the stabilizer action, is open. The question is a minimisation over
stabilizer orbits of straight exponent matrices; an answer would say whether act 38 found a smallest
escape direction or one among escapes of several sizes. A minimality statement requires either an
exhaustive search below a stated support bound, which does not presuppose the full census, or a
structural lower bound.


### The three-parameter family through the product stratum

**Future realizability and structure question, not an A38 result; it neither assumes nor provides the
census or the minimality of the support.** Act 38's witness is a sum of three disjoint `{0, 1}` exponent
matrices, `E = A + B + C`, and its arc is the diagonal `u₁ = u₂ = u₃ = u` of the three-parameter family
`SIG ∘ u₁^A u₂^B u₃^C`. Act 38's probe records, as a control of its classifier and not as a theorem, that
`A`, `B`, `C` and their pairwise sums are straight lines each lying identically in some Diţă structure of
the point while `A + B + C` lies in none. Tests of the one-variable lines `xA + yB + zC` project the joint
exponent triple onto a single integer coordinate and do not establish the three-variable identity.

The first gate is realizability on the whole three-torus: `SIG ∘ u₁^A u₂^B u₃^C` is unitary for all units
`u₁, u₂, u₃` exactly when, for every pair of rows, the columns grouped by the joint difference triple
`(A_rj − A_sj, B_rj − B_sj, C_rj − C_sj)` have vanishing pair sums — a finite exact computation, run as a
pre-freeze measurement. Only if it holds does the structural question follow: which part of the
three-torus admits a Diţă structure, of which shape and index maps, and whether the diagonal arc is
representative of a nonlinear incompatibility among three directions each of which, alone or in pairs,
is Diţă-linear. The direction is subordinate to `P0` in the same sense as the residual-deformation
direction above.


