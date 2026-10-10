# A38 read-only witness discovery — note (no branch, no freeze)

Base: certified main `5949740297034d0ddc522aff9577bd1fa36fe42f` (A37 landed). All arithmetic exact
(Gaussian rationals; the A37 monomial calculus with canonical points ζ z^s w^t). Toolkit in
`scratchpad/a38/` (`lib38.py`, `lib38b.py`, `lib38c.py`; the landed A37 probe head is loaded verbatim
as `probe37_landed.py`). Nothing here is a certificate; it is the measurement the owner asked for
before any A38 freeze.

## Verdict: NON-DIŢĂ WITNESS (exact-computation layer)

The exponent matrix, rows i = 4a+b, columns j = 4c+d, entries in {0,1}, support 48:

    E[(a,b),(c,d)] = [a odd][b = 3][c odd]  +  [a = 2][d = 1]  +  [a+b odd][(c,d) ∈ {(0,2),(2,0)}]
                   =        A               +        B         +              C

Arc: H(u) = SIG ∘ u^E, u on the unit circle; H(1) = SIG.

Verified exactly:

1. **Realizability identity.** H(u) H(u)^* = 16·I as a Laurent-polynomial identity in u (every level
   set of every row-pair difference has vanishing pair sum; checked by the subset tables and
   independently by direct exact evaluation). Entries are unimodular monomials, so H(u) is a complex
   Hadamard family through SIG.
2. **Generic non-membership, every admissible index map, both forms.** A37's exhaustive structure
   search (`structures`) run on the monomial entries of E and of E^T at a free symbol u returns, for
   every shape 4×4, 8×2, 2×8, (candidates, exact) = (0, 0): at generic u no 8-, 4- or 2-subset of
   columns (or rows) even splits the rows (columns) into proportionality classes of the right size.
   Hence no Diţă structure of any shape holds identically, and also none up to diagonal
   equivalence (proportionality is diagonal-invariant; the relaxed rank-one census at SIG equals the
   strict one, 9 + 9 structures).
3. **Per-class obstruction (the 18 census structures).** Each is admitted only at u = 1; every
   non-identity condition is u^k = 1 with k ∈ {−2, −1, 1, 2} (first-order separation along the arc).
   A kernel-shaped witness identity H p1·H p2 = H p3·H p4 forced by the Diţă form with all four
   SIG entries rational (±1) and u-exponent sums {0,1} exists for 16 of the 18 structures
   (positions in `witness38.json` / the run log); e1-row and t2-column have only non-rational
   `prop` witnesses (k = 1) or rank-one witnesses, to be chosen at freeze time.
4. **Exact exceptional set over all index maps** (A37's sections 4–5 rerun on E and E^T): 40
   candidate points; the point searches find a Diţă structure at exactly two, u = 1 (the 18 census
   structures) and u = −1, where H(−1) admits one 2×8 structure in each form with index maps not
   among the census (column form: blocks by column parity, classes (0,2),(1,3),(4,6),(5,15),
   (7,13),(8,10),(9,11),(12,14)). So for every unit u ∉ {1, −1} the matrix H(u) admits no Diţă
   structure of any shape with any index map, strictly or up to diagonal equivalence.
5. **Controls.** Numeric exhaustive search with factor unitarity at u₅ = (3+4i)/5 and at u₆₀:
   (0,0) for every form and shape; H(u₅), H(u₆₀), H(−1) unitary. The zero matrix is in all 18
   subspaces; a gauge-trivial matrix is relaxed-Diţă for all 18 and strictly for none; W lies
   identically in t1 (column and row) only — all as expected.

Orbit under gauge × stabilizer (1024, with transposition) × sign: 512 gauge-normal images, minimal
support 48 (the representative above); the lexicographically minimal normal form is uglier (values
−2..1, support 156).

## Structure of the witness

The three pieces are each Diţă deformations, and so are the pairwise sums; only the triple is not
(identical membership by the linear conditions, strict = relaxed in every case):

| combination | identically in |
|---|---|
| A | k2 row, k4 row, e2 row, t1 column, t1 row, t2 row, t3 row |
| B | k1 row, k4 column, t1 row, t2 column |
| C | k2 column, t1 column, t2 column, t3 column, t3 row |
| A + B | t1 row |
| A + C | t1 column, t3 row |
| B + C | t2 column |
| A + B + C | none |

Every integer combination xA + yB + zC with |x|,|y|,|z| ≤ 2 is straight, so SIG ∘ u₁^A u₂^B u₃^C is a
three-parameter straight family through SIG whose coordinate planes each lie in one hull and whose
generic point lies in none; the witness is its diagonal. The straight lattice L(Π_E) fixed by E's own
level-set partitions is one-dimensional (the arc is rigid within its partition pattern).

## Tangent-space context

dim T(SIG) = 80 (defect 49 + 31 gauge). dim(L_S ∩ T) per structure: 36 (k1, k3, k4), 46 (k2),
44 (e1, e2), 57 (t1, t2), 49 (t3); relaxed 45/55/51/64/56. The 18 subspaces together span all of T
(also the four 4×4 alone, and the three 2×8 alone; the 8×2 pair spans 73), so no exotic tangent
direction exists — witnesses are non-Diţă *combinations* of Diţă tangent directions that integrate
exactly, as above.

## The census (domain and status)

Domain searched: E ∈ {0,1}^{16×16} with row 0 = 0 (a gauge choice; every class has such a form only
if some member has a zero row, so the domain is a proper subset of "all {0,1} matrices up to gauge",
whose gauge-normalized image is the {−1,0,1} row-0-zero domain — not enumerated). Straight lines in
the domain: admissible rows per index 1328 / 4900 / 12870 (pair tables exact; the naive per-monomial
balance lemma is false — the relation z + w = 2(1 + zw) produces 1024 vanishing subsets over 32 row
pairs that are not per-monomial balanced — so only the exact subset tables are used).

- Solutions in the domain: Knuth estimate ≈ 1.7×10⁸ (high variance). The classifying DFS (`dfs2.py`:
  strict/relaxed membership, one representative per partition signature, all non-members kept) was
  terminated by the container's out-of-memory killer after 3222 s at 10.42 M solutions (437 248 in no
  census subspace, 229 120 strictly outside every class but inside a relaxed one); its output was not
  saved. The count is unfinished and is not part of A38's freeze. A dedicated collector (`first_wit.py`) took the first 416
  non-members: 53 orbits, supports 48/64/80; the representative above is the smallest.
- Classification of the domain so far: DIŢĂ (identically, in at least one census class) — the
  majority; NON-DIŢĂ WITNESS — every non-member found (each is one by the argument of item 2, since
  identically-holding structures at generic u are census structures, and non-identical ones are
  admitted on finite sets); UNDECIDED — none: the linear membership test is exact and decisive.

## What a freeze would need (not done)

Frozen statement candidate: for every unit u ∉ {1, −1}, SIG ∘ u^E admits no Diţă structure of any
shape for any admissible index map (probe layer, exhaustive), and, in the kernel, for each of the
nine A37 classes (18 structures) the witness identity of item 3 (an A37-shaped exclusion lemma per
structure) plus the realizability identity. The exhaustive index-map claim and the exceptional-set
claim stay in the exact-computation layer, as ruled for A37.
