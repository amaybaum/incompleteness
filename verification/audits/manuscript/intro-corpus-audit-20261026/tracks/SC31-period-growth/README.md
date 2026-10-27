# SC-31: recurrence period growth (#942 / #946)

Base: SC-28 head `42bc4050` (`corpus/sc28-assumption-scope`). SC-28's later heads `df061d64`, `c43347f4` and
`51ba6652` were merged in afterwards by normal merges. SC-28 rewrote sentences in the same region of book ch18 §18.7, and
SC-31 builds on that wording. The review amendments are in a separate commit after `2430948d`. The finding came from SC-28: ch18 §18.7 called lcm(1..|S|) "Landau's
function", gave N ~ e^{|S|} "for a generic permutation", and so presented e^{e^{10^{122}}} as the period when it is
only an upper bound.

## The three quantities

For a permutation σ of n points, ord(σ) is the lcm of its cycle lengths.

| Quantity | Statement | Status | Source |
|---|---|---|---|
| (1) Universal bound | ord(σ) divides lcm(1,…,n) for every σ. ln lcm(1,…,n) = ψ(n) ~ n | Theorem: elementary divisibility, PNT asymptotic | Prime number theorem |
| (2) Maximum order | g(n) = max ord(σ) (Landau's function), ln g(n) ~ √(n ln n). Since √(n ln n) = o(n), g(n) is far below lcm(1,…,n) | Theorem (asymptotic) | Landau 1903 |
| (3) Typical order, uniform σ | ln ord(σ) = (1+o(1)) ½(ln n)² in probability. (ln ord − ½(ln n)²)/√(⅓(ln n)³) → N(0,1) in distribution | Theorem, valid only for σ uniform on S_n | Erdős & Turán 1965 (I), 1967 (III) |

The mean of ord(σ) itself is not the typical order. ln E[ord] ~ C√(n / ln n), with C ≈ 2.99 (Goh & Schmutz 1991). The
mean is dominated by rare permutations. It is not used in the manuscript.

A fourth bound is kept separate from the three generic quantities because it depends on the rule.

| Quantity | Statement | Status | Source |
|---|---|---|---|
| (R) Exactly linear fixed-graph rule only | Let φ be an invertible linear map of (Z/q)^D. Then I, φ, …, φ^{N−1} are distinct and nonzero, and they lie in (Z/q)[φ], which has at most q^D elements by Cayley–Hamilton. So N ≤ q^D − 1 = \|S\| − 1 for every q ≥ 2. For prime q, Singer cycles attain the bound. For composite q the bound holds but need not be attained, and for D = 2 the exhaustive maximum is below q² − 1 at q = 4, 6, 8, 9, 10 and 12 | Theorem (elementary), conditional on A5 (ch02 §2.4). It does not cover the state-dependent-geometry map F(u,v) = (v, WE_{G(v)}(v) − u) (SM §3.1, :158) or the rounded bijection of SM §4.2 (`papers/main_repro/lyapunov_v3.py`, `((nn+1)//3 − prv) % q`). Both are bijections but not linear maps, so only (1) and (2) apply to them | Proved here |
| (R1) Ring wave rule | ord F = qL for q prime with gcd(L, q) = 1 | Corpus theorem | book Theorem B.3.1 and SM Theorem A.1 |

The 3D torus wave rule has a sharper bound, ord F \| 2q(q^{2m} − 1) with m = ord_L(q) ≤ L − 1. It holds for q prime with gcd(L, q) = 1. The argument diagonalizes over F_{q^m}, where each 2×2 mode block has roots in F_{q^{2m}} or is a ±1 Jordan block. The bound is checked for L ≤ 5 in the script, and for L ≤ 7 in a one-off run (orders 6 to 1092). It is not put in the manuscript, since it is not a corpus result. See the owner decision below.

None of the three generic quantities is a typical recurrence time for OI dynamics. Using (3) requires a distribution over φ. The corpus
adopts none. Chapter 3 §3.2 and Structure §2.1 hold that random permutations typically lack the C1–C4 structure. Both
the manuscript and this record therefore state (3) as conditional on the uniform model.

|S| is not fixed by visible data. The corpus bounds only |C_V × C_B| ≤ e^{10^{122}} (Substratum :263), treats |C_D| as
gauge (GR :136, ch18 :178), and says S's information exceeds the Bekenstein–Hawking bound (ch18 :176). So no site
quotes a number as a bound on N. The manuscript uses the following only as an illustration conditional on |S| ~
e^{10^{122}} (ch18 :187–:188). The leading-order expressions are then:

- (1) ln N ≤ ψ(n) = (1+o(1)) e^{10^{122}}. This is an upper bound.
- (2) ln g(n) ~ 10^{61} e^{5×10^{121}}. This is the largest period any bijection of the set can have, as an asymptotic.
- (3) ln ord ≈ 5×10^{243}, with standard deviation ≈ 5.8×10^{182}. This holds under the uniform model only.

- (R) N ≤ |S| − 1, for the exactly linear rule only.

The conversion from steps to seconds (τ ~ t_Pl) shifts ln by about −100, which is negligible.

## References

- E. Landau, "Über die Maximalordnung der Permutationen gegebenen Grades", *Archiv der Mathematik und Physik* (3) 5
  (1903) 92–103.
- P. Erdős and P. Turán, "On some problems of a statistical group-theory. I", *Z. Wahrscheinlichkeitstheorie verw.
  Gebiete* 4 (1965) 175–186, doi:10.1007/BF00536750.
- P. Erdős and P. Turán, "On some problems of a statistical group-theory. III", *Acta Math. Acad. Sci. Hungar.* 18
  (1967) 309–320.
- W. M. Y. Goh and E. Schmutz, "The expected order of a random permutation", *Bull. London Math. Soc.* 23 (1991) 34–42.
  It is cited in this record only.

These were checked against bibliographic records. No page-level citation is given.

## Numerical check

`period_growth_check.py` runs with `python3 -I`, a fixed seed and exact integers, in about 15 s. Its output is
`period_growth_check.out`, and all 11 controls pass:

- ord divides lcm(1..n) for every cycle type up to n = 22.
- ψ(n) computed from the exact lcm agrees with the von Mangoldt sum at n = 10^5. ψ(n)/n = 0.7832, 0.9405, 0.9967,
  1.0013 and 1.0005 at n = 10 through 10^5.
- max ψ(n)/n for n ≤ 2000 is printed as an observation only. No explicit constant is used or attributed.
- The g(n) partition DP equals the brute-force maximum lcm over partitions for n ≤ 40. g(100) = 232792560.
- g(n) divides lcm(1..n) for n ≤ 2000. ln g / √(n ln n) = 0.71, 0.90 and 1.02 at n = 10, 100 and 2000.
- For E[ln ord], the exact cycle-type value at n = 30 is matched by two independent samplers within 4 standard errors.
  For n = 10^3 to 10^9, mean/(½ ln² n) rises from 0.76 to 0.83 and var/(⅓ ln³ n) from 0.21 to 0.53. This is a sanity
  check only: the convergence is slow.
- Every invertible 2×2 matrix over Z/q has order ≤ q² − 1, exhaustively for q ∈ {2,…,6, 8, 9, 10, 12}.
- The ring wave rule has order qL for q ∈ {2, 3, 5, 7} and L ≤ 9 with gcd(L, q) = 1, by brute force. This reproduces
  Theorem B.3.1. The composite cases tested also give qL.
- The 3D torus rule's order divides 2q(q^{2m} − 1) for the (L, q) tested.

## Sites

Sites are listed at their final wording, after the review amendments.

| Site | Was | Anchor | Now |
|---|---|---|---|
| ch18 §18.7 period paragraph (+FULL) | "generic permutation … bounded by lcm(1,…,\|S\|) (Landau's function) … ≈ e^{\|S\|}"; N ~ e^{e^{10^{122}}} | (1)–(3) | For an arbitrary bijection the three quantities are kept distinct. (3) holds under the uniform model only, and no part of the corpus adopts that model (ch03 §3.2 cited). |
| ch18 illustration (+FULL) | "\|S\| ~ e^{10^{122}}, the rough estimate of the substratum's cardinality" | Substratum :263; ch18 :176, :178 | \|S\| is not fixed by visible data, since only \|C_V×C_B\| ≤ e^{10^{122}} is bounded and the deep sector is gauge. The numbers appear "for illustration only, if \|S\| were of order e^{10^{122}}". |
| ch18 linear-rule paragraph (+FULL) | none | (R), (R1) | N ≤ q^D − 1 = \|S\| − 1 with its proof, for the exactly linear fixed-graph rule under A5. Cites B.3.1 (qL on a ring). The bound does not cover the state-dependent-geometry map (SM §3.1) or the rounded bijection (SM §4.2), for which only N ≤ g(\|S\|) and N \| lcm hold. The 3D period is not computed. |
| ch18 return paragraph (+FULL) | "definite quantitative prediction: … after e^{e^{10^{122}}} steps"; "no practical empirical consequences" | (2), (R) | N ≤ g(\|S\|) for any bijection, and N < \|S\| for the exactly linear rule. The framework bounds N but does not compute it, and supplies no lower bound. There are no practical consequences at periods of astronomical size. |
| ch18 Falsifiability (+FULL) | "infinite observation time"; "recurrence at approximately the framework's timescale" | (2), (R) | For given \|S\| and φ, non-recurrence within g(\|S\|) steps contradicts finite S with a bijection, and within \|S\| − 1 steps contradicts only A5. \|S\| is not fixed, so for any finite T, \|S\| > T + 1 is admissible, and no finite observation falsifies the framework as a whole. Records return with S. |
| ch18 :20 overview (+FULL) | "Poincaré recurrence at timescale e^{e^{10^{122}}}" | (2) | Exact recurrence at a period at most Landau's g(\|S\|), not computed because \|S\| is not fixed by visible data |
| ch18 :28 (+FULL) | "cosmic recurrence at e^{e^{10^{122}}}" | (2) | "at a period at most g(\|S\|)" |
| ch18 §18.7 closing summary (+FULL) | "verification would require infinite observation time" | (2) | For given \|S\|, a test needs up to g(\|S\|) steps. No finite observation falsifies the framework as a whole. |
| ch01 §1.5 accessible-timescale lemma (+FULL) | "N can be as large as m!" (hidden m); "t_R ~ e^{10^{122}} years" | (2), (R). m! is \|S_m\|, not an element order: g(m) is far below m! | With n = \|C_V×C_H\|: N ≤ g(n), N divides lcm(1..n), and N < n under the exactly linear rule. N is bounded but not computed, and n is not fixed by visible data. |
| Explainer, Accessible-Timescale Lemma | "it's e^(10^122) years" | (2), (R) | The same correction in the Explainer register |
| Appendix A F8 (+FULL) | "~e^{e^{10^{122}}} timescale" | (2) | "period at most g(\|S\|); \|S\| not fixed" |
| Appendix C, finiteness objection (+FULL) | "cosmic recurrence at timescale ~e^{e^{10^{122}}} … no practical empirical consequences" | (2) | Exact recurrence at a period at most Landau's g(\|S\|), with \|S\| not fixed by visible data |
| book/README ch18 entry | "cosmic recurrence at e^{e^{10^{122}}}" | (2) | "at a period at most Landau's g(\|S\|), with \|S\| not fixed by visible data" |
| Appendix B :420, B.7 role paragraph (+FULL) | "recurrence time ω, which is astronomically large" | No lower bound in the corpus | "can be astronomically large" |
| Bibliography (+FULL) | none | none | Added Erdős–Turán 1965 and 1967 and Landau 1903, under Mathematical foundations |

## Re-grep over `papers/*.md` and `book/*.md`

This re-grep was run after the review amendments, on top of `2430948d`.

The following patterns have zero hits: "Landau's function)", "generic permutation", "grows as approximately
$e^{|S|}$", "N \sim e^{|S|}", "as large as $m!$", "e^{10^{122}}$ years", "e^(10^122) years", "typical period",
"recurrence at $e^{e", "at timescale $\sim e^{e", "\|S\| \sim e^{10^{122}}", "n \sim e^{10^{122}}", "below
$e^{10^{122}}", "is astronomically large for a high-capacity", "1.03883" and "Rosser".

These survive:

- **`e^{e^{10^{122}}}` (2 hits).** These are ch18 :187 and its FULL mirror, the illustrative display under "if \|S\|
  were of order e^{10^{122}}".
- **"infinite observation time" (2 hits).** These are ch18 Falsifiability and FULL, now in the framework-level sense.
- **"Landau" (17 hits).** Two are Aharonov–Jones–Landau 2006 (Computation :246, ch14 :228, and FULL), which is another
  claim. The others are the corrected sites and the bibliography.
- **"lcm" / "least common multiple".** SM :1592 and appendix-b :119 (with FULL) are the order of the ring map, another
  claim. ch01 :111, appendix-b :418 and the ch18 cyclicity paragraph ("least common multiple of the cycle lengths") are
  correct. The rest are the corrected sites.
- **"recurrence time" with a number.** Only Explainer :227 survives: σ² = id, "2 steps", which is exact. No paper other
  than the Explainer quotes a cosmological period.

Left unchanged:

- Main :441, which says finite-dimensional Hamiltonian flow has recurrence "exponentially large in the system size".
  It concerns a different object, approximate quasi-periodic return, and states no number.
- "Poincaré recurrence" in the ch18 §18.7 title and run-in heading, ch01 :119, Explainer :44, and Main :151, :441 and
  :532. After `df061d64`, the substantive ch18, ch02 and ch09 sentences say "exact recurrence". SC-31 changed ch18 :20
  to "exact recurrence" to match.
- "Logically falsifiable only" in Appendix A F8 and App C.

## Owner decisions

1. **The 3D rule's period.** For q prime with gcd(L, q) = 1, the exactly linear torus wave rule has ord F \|
   2q(q^{2m} − 1), where m ≤ L − 1. This is checked for L ≤ 7. If L³ were of order 10^{122}, it would give
   ln N ≲ 10^{41}. It is a new derivation, not a corpus result, so the manuscript states only |S| − 1 and the ring
   theorem B.3.1. Adding it would need a written proof (Appendix B) and a choice of boundary conditions.

The Introduction (`draft/oi-introductory-paper-20261025` at `72014a79`, read-only) states no recurrence-time number.
Its :49 and :146 define L as the order of φ, without size.

Regenerated: Explainer and the book (`.tex` and `.pdf`). After each merge the book `.tex` and `.pdf` were rebuilt, not
hand-merged.
