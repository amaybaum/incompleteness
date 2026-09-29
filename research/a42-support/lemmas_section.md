## Pruning lemmas (each stated, proved or checked exactly)

Notation: for a representative E, Z = its set of zero rows, R = the rest (r = |R|), msize(i, Z) = least size of a
nonempty column set K with Σ_{k∈K} SIG_ik conj(SIG_zk) = 0 for every z ∈ Z (exact tables, `cvsize.py`), and
LB(R) = Σ_{i∈R} msize(i, Z).

- **VS (pair structure).** For each of the 120 row pairs the vanishing column sets are: antipodally balanced sets
  (columns with pair product v matched with columns with −v) for 88 pairs (64 of type 4|4+4|4, 24 of type 8|8), and for
  the 32 remaining pairs balanced sets plus 32 exceptional sets (from relations like z + w = 2(1 + zw)). Minimal
  vanishing sets have sizes 2 and 6 only (`pairtypes.py`, `lemmas42.py` L1). Hence no level set of a row difference is
  a singleton. Used by the SAT encoding and by G1/M1.
- **CV (common vanishing).** If z is a zero row, every level set of E_i equals a level set of E_i − E_z and so
  vanishes for the pair (i, z). A nonzero row i is therefore a labelled packing of sets that vanish against every zero
  row; every such set is a disjoint union of minimal ones (difference of two vanishing sets vanishes).
- **U (uncertainty; general integers).** Each nonzero level set K of a nonzero row satisfies |K| ≥ 16/r; hence every
  representative of every straight line that is not gauge-trivial has at least 16 nonzero entries. Proof: v = 1_K∘SIG_i
  is orthogonal to the rows SIG_z, z ∈ Z (Lemma CV), so its coordinate vector in the orthonormal basis SIG/4 has at most
  r nonzero entries; the basis matrix is unitary with all entries of modulus 1/4, and Donoho–Stark
  (‖x‖₂ ≤ √|supp ŷ|·‖ŷ‖_∞ ≤ √|supp ŷ|·¼‖x‖₁ ≤ ¼√(|supp ŷ||supp x|)‖x‖₂) gives |K|·r ≥ 16. Summing over the r nonzero
  rows, |supp E| ≥ r·⌈16/r⌉ ≥ 16 (r = 16 included; r = 1 forces a constant row, i.e. gauge-trivial, since 1_K∘SIG_i ∈
  span(SIG_i) forces K = ∅ or all columns). Exact cross-check: msize(i, Z) ≥ ⌈16/(16−|Z|)⌉ for all 16·2¹⁵ pairs
  (`lemmas42.py` L2).
- **LB.** |supp E| ≥ LB(R) for the exact zero-row set; the searches enumerate only row sets with LB(R) ≤ budget.
- **P (projection; {0,1} representatives).** For E ∈ {0,1}^{16×16}, U(u) = (SIG∘u^E)SIG*/16 = (I − Q) + uQ with
  Q = (SIG∘E)SIG*/16. U(u) unitary for all u ⇔ Q(I − Q*) = 0 and its adjoint ⇔ Q is an orthogonal projection. Then
  rank Q = tr Q = Σ_i (row sum of E_i)/16 = |supp E|/16. So a {0,1} straight line has support 16·rank(SIG∘E) ∈ 16Z.
  Checked exactly (rank over Q(i)) on A, B, C, the act-38 witness and all 12 808 {0,1} leaves (`lemmas42.py` L4).
- **D (determinant; general integers).** det(SIG∘u^E) is a Laurent polynomial of constant modulus on the circle, hence
  c·u^δ, and δ = tr((SIG∘E)SIG⁻¹) = ΣE/16. So ΣE ≡ 0 (mod 16) for every straight line (checked on every classified
  leaf: `sum_mod16` = 0). Not used for pruning.
- **G1 ({0,1}, support-1 row).** If a {0,1} straight line has a row e_k then column k is all ones (else the level set
  {k} of value −1 in E_i − e_k is a singleton, contradicting VS); subtracting that column (gauge) gives a {0,1} straight
  line of support s − 16 with a zero row.
- **RS (row-set span; general integers).** By CV, a straight line with zero-row set exactly Z lies in
  W_R = ⊕_{i∈R} span{1_K : K vanishes for row i against every z ∈ Z}. If W_R lies in one census subspace L_S, every
  straight line (any integer values) with that zero-row set is Diţă. Exhaustive over all 65 390 row sets with r ≥ 2 and
  LB(R) ≤ 77 (`spanAll.py`): 13 922 dead; the smallest LB of a live row set is 24, and all 50 row sets with LB < 24
  (LB = 16) are dead.
- **M (minimum line; no zero line).** Let m be the least support of a row or column of a min representative. m ≥ 3
  forces s ≥ 48; m = 2 forces s ≥ 32. Two rows of support 1, v e_k and v′ e_k′, are equal, or have k ≠ k′, v′ = −v and
  {k, k′} antipodal for the pair (VS); so the support-1 rows take at most two vector values.
- **M1 (general integers, s ≤ 19).** If m = 1 and s ≤ 19, at least 13 rows have support 1, so one vector value v e_k
  is carried by a set C of at least 7 rows; E′ = E − 1(v e_k)ᵀ (gauge) has C among its zero rows and support at most
  (s − |C|) + (16 − |C|) ≤ 21 < 24, so by RS it is Diţă.
- **NS (subtree Diţă pruning).** At a DFS node, if for some census subspace every free row's candidates contribute the
  same vector to the subspace's equations and fixed part + contributions = 0, every leaf below lies in L_S; the subtree
  is skipped. Sound by linearity. Countercontrol: dropping the "= 0" clause loses every witness leaf at budget 48.
- **O (orbit support = gauge support)** — above.
- **Transposition.** SIG is symmetric and the census contains both forms of each structure (the row form is the column
  form applied to Eᵀ), so straightness, N18, Ncomplete and support are transpose-invariant; a min representative with a
  zero column but no zero row is handled as its transpose.
