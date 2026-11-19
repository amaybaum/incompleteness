# Independent proof review: Lemma P (ARP-2 / Q-C2-1)

**Verdict: PROVED.** The statement is true as stated. The complete proof is in §2. The sketch's chain of steps is
sound. Two steps were asserted rather than proved, and both are filled here:
- the existence of an `O`-valued fixed point, without which the affine parts of `Φ^{n_k}` need not converge;
- the rank-2 case, where a free-action argument replaces the polygon-automorphism classification.

The design's reliance on Lemma P survives. It remains conditional on Theorem C(ii), as the design already labels it,
and on the link hypotheses L1–L3 in §4.

- **Reviewer.** An independent model reviewer that did not write the sketch. Paper argument plus exact probes. No C
  gadget orbit was evaluated, and no B fragment was built from OI data.
- **Object reviewed.** `DESIGN-DS.md` r9 (`f4d1c078841f0381313a3a4ea436b47baad48ae3eef4c7f392c8cd91687bbd4b`), §6
  "Lemma P", and §7 "Theorem C". The uses reviewed are in `preregistration.draft.md` r9a
  (`9692dc40f326d4ccc56dd6585f97c0857f5b3c51a7f3f7bcbfd9de90326fa062`): the CC-NAT row, the DSN input row, and decision
  rule C's ABL. `REACHABLE.md` r3 (`718e7dbc…`) supplies Theorem C. The r10 drafts that appeared during this review
  change only the label (`81e102cc…`). The r10 table *Sketches under independent review* is commented on in §7.
- **Owner instruction** (#1169 c.6735014875, amaybaum, 2026-11-09T07:52:50Z): "Each review should check the complete
  proof, assumptions, counterexamples, and whether the result depends on quantum structure that OI has not generated.
  A failed proof review should block reliance on that sketch, not automatically invalidate the rest of Q-C2-1."

***

## 1. The exact claim and its hypotheses as used

**Lemma P.** Let `O = {r ∈ ℝ³ : |r_x| + |r_y| + |r_z| ≤ 1}`, and let `Φ(r) = α + βr` be an affine map with
`Φ(O) ⊆ O`. Then the multiset of unit-modulus eigenvalues of `β`, counted with algebraic multiplicity, is a
sub-multiset of the spectrum of some 3×3 signed permutation matrix.

The 48 signed permutations have eight distinct spectra (probe §1):
- `{±1}`-multisets;
- `{1, i, −i}` and `{−1, i, −i}`;
- `{1, ω, ω²}`;
- `{−1, e^{±iπ/3}}`.

Among multisets of roots of unity of size at most 3, closed under conjugation, exactly two are excluded: `{1, e^{±iπ/3}}`
(R60 type) and `{−1, ω, ω²}` (S₃ type).

**How the design uses it** (DESIGN-DS §6, §7, §8 row "affine `g`"; prereg CC-NAT and ABL):
- For the four affine rules, the induced map `Φ` is fitted from `R_op(πΛ_0)` and `R_op(πΛ_{a,0})`. CONS checks it on
  all seven QA laws, and further along the orbit.
- Theorem C(ii) gives `R(πΛ) ∈ O`, so `Φ` is a self-map of `O`.
- Lemma P then gives "no W-CL". Applied to `P^k β`, where the frame transposition `P ∈ O_h` preserves `O`, it also gives
  no W-CL in the encoded frame.

## 2. Complete proof

Notation: `E_1` is the real β-invariant subspace that is the sum of the generalized eigenspaces for eigenvalues of
modulus 1, `E_<` is the sum for the rest, and `d = dim E_1`.

| step | content | status |
| --- | --- | --- |
| 1. Power-boundedness | `Φ^n(O) ⊆ O`, and `β^n r = Φ^n(r) − Φ^n(0) ∈ O − O = 2O` for `r ∈ O`. `O` contains the Euclidean ball of radius `1/√3`, so `‖β^n‖₂ ≤ 2√3` for all `n`. In particular every eigenvalue has `|λ| ≤ 1` | rigorous |
| 2. Semisimplicity at `|λ| = 1` | A Jordan block of size ≥ 2 at `|λ| = 1` has `‖J^n‖ ≥ n`, which contradicts step 1. So `β|_{E_1}` is diagonalizable over ℂ, and the unit-modulus eigenvalues of `β`, with algebraic multiplicity, are exactly the eigenvalues of `β|_{E_1}` | rigorous (standard; e.g. Horn and Johnson, *Matrix Analysis*, Jordan form) |
| 3. A fixed point `p ∈ O` (**gap in the sketch, filled**) | Let `a_N = (1/N) Σ_{i<N} Φ^i(0)`. Then `a_N ∈ O` by convexity, and `Φ(a_N) − a_N = Φ^N(0)/N`, whose ℓ1 norm is at most `1/N`. `O` is compact, so a limit point `p` exists, and `Φ(p) = p`. Hence `Φ(r) = p + β(r − p)`. The sketch asserts `Φ^{n_k} → Ψ` without this step: boundedness of `Φ^n(0)` alone gives only subsequential limits of the translation parts, not an idempotent limit | rigorous |
| 4. Spectral projection | Let `Π` be the projection onto `E_1` along `E_<`. It is a real polynomial in `β`, so `Πβ = βΠ`. By simultaneous Dirichlet approximation there are `n_k → ∞` with `λ^{n_k} → 1` for every unit eigenvalue `λ`. On `E_<`, `β^n → 0`. So `β^{n_k} → Π` | rigorous (Dirichlet / compactness of the torus) |
| 5. The limit `Ψ` | `Ψ(r) := p + Π(r − p) = lim_k Φ^{n_k}(r)`. It is affine, `Ψ∘Ψ = Ψ` and `Φ∘Ψ = Ψ∘Φ`. Since `O` is closed, `Ψ(O) ⊆ O` | rigorous |
| 6. `Φ` permutes the vertices of `Q = Ψ(O)` | `Q` is a polytope, the affine image of `O`. Its affine hull is `p + E_1`, because `O − p` spans ℝ³. `Φ(Q) = Ψ(Φ(O)) ⊆ Q`. On `p + E_1`, `Φ` is the affine bijection `y ↦ p + β|_{E_1}(y − p)`, with `|det β|_{E_1}| = 1` (step 2). So `vol_d Φ(Q) = vol_d Q > 0`. A compact convex `Φ(Q) ⊆ Q` of equal positive volume equals `Q`: if `y ∈ Q \ Φ(Q)`, then a relative neighbourhood of `y` misses the closed set `Φ(Q)` and meets `Q` in positive volume, because `Q` is the closure of its relative interior. An affine bijection of `Q` maps vertices to vertices. The vertex set `V_Q ⊆ Ψ({±e_a})`, so `|V_Q| ≤ 6`, and `Φ` permutes `V_Q` | rigorous |
| 7. Finite order | `V_Q` affinely spans `p + E_1`. If `m` is the order of the permutation, `Φ^m` fixes `V_Q` pointwise, hence fixes `p + E_1`. So `(β|_{E_1})^m = I`, and every unit eigenvalue of `β` is an `m`-th root of unity | rigorous |
| 8a. `d = 0` | empty multiset | rigorous |
| 8b. `d = 1` | one real unit eigenvalue, `±1`, contained in the spectrum of `diag(±1, 1, 1)` | rigorous |
| 8c. `d = 2` (**sketch's classification replaced**) | `β₁ = β|_{E_1}` is a real 2×2 matrix of finite order. If its eigenvalues are real, they are `±1` (contained in the `{±1}³` spectra). Otherwise `β₁` is conjugate to a rotation of exact order `m′ ≥ 3`. Its unique fixed point on the plane is `p`. `Q = (p − Πp) + Π(O)` is centrally symmetric, and `Φ` fixes its centre, so the centre is `p`, an interior point and not a vertex. Every non-trivial power of `Φ` on the plane therefore fixes no vertex, and the cyclic group of order `m′` acts freely on `V_Q`. So `m′` divides `|V_Q|`, which is even (central symmetry) with `4 ≤ |V_Q| ≤ 6`. Hence `m′ ∈ {3, 4, 6}`, and the pair is `{ω, ω²}`, `{±i}` or `{e^{±iπ/3}}`. These are contained in `{1, ω, ω²}`, `{1, ±i}` and `{−1, e^{±iπ/3}}` respectively. No automorphism-group classification of polygons is needed, so the sketch's remark about non-affinely-regular hexagons is unnecessary | rigorous |
| 8d. `d = 3` | `Π = I`, so `Ψ = id` and `Q = O`. `Φ` is an affine bijection of `O`. It permutes the six vertices `±e_a` and fixes their centroid `0`, so `α = 0`. Then `β` maps `{±e_a}` to itself linearly, so `β` is a signed permutation | rigorous |

∎ The proof uses only the convexity, boundedness, full dimension and vertex count of `O`, and its central symmetry in
step 8c.

**Strengthening observed, not needed and not proved.** In the rank-2 case the exact search found only parallelograms,
never a hexagon: 204 idempotents `Ψ` with `Ψ(O) ⊆ O` on a denominator-≤-6 grid gave 0 hexagonal images. It also found
no affine self-map of `O` with an order-3 or order-6 unit pair outside `O_h`. A one-line computation (paper, this review) shows why
the regular hexagon section is not reached centrally: a projection `r ↦ r − (n·r)w` onto `x + y + z = 0` (`n = (1,1,1)`,
`n·w = 1`) keeps `e_a` in `O` only if `w_a ≥ 1/2`, impossible for all three `a` with `Σ w_a = 1`. If proved, this would sharpen Lemma P to "orders 3 and 6 occur only
inside `O_h`". The design does not need it.

## 3. Counterexample hunt (exact; `probe_lemma_p.py`)

| search | size | violations |
| --- | --- | --- |
| exhaustive grid: columns of `β` and `α` on `{k/4}`, with five `α`s including off-centre ones, filtered by `Φ(V₀) ⊆ O` | 2,574,803 maps | 0 |
| random rational maps with denominators ≤ 12 | 20,000 | 0 |
| all affine symplectic bijections of `F₂⁴` (`|Sp(4,2)| = 720`, × 16 translations), acting on the QA family | 11,520 QA-consistent maps | 0 (all have `Φ(V₀) ⊆ O`, and every unit multiset is allowed) |
| R60 and S₃ themselves | 2 | both fail `Φ(O) ⊆ O` (column ℓ1 = 5/3). `c·R60` is a self-map only for `c ≤ 3/5`, which leaves no unit spectrum |
| proof objects, exact, on 248 grid maps with non-empty unit spectrum, including `α ≠ 0` | 248 | 0 failures. Each checked: a fixed point in `O`; the Bézout projection `Π = u(β) p_<(β)`; `Ψ` idempotent, commuting with `Φ`, `Ψ(O) ⊆ O`; and `Φ¹² = id` on `Ψ(O)` |
| rank-2 tightness | `R90 ∘ proj_xy` | a self-map with unit spectrum `{±i}`, allowed. The rank-2 case is not vacuous |

The unit multisets seen on the grid are, with counts:
- `∅` (2,433,971);
- `{1}` and `{−1}` (68,652 each);
- `{−1, 1}` (1,740);
- `{±i}` (798);
- `{1, 1}` and `{−1, −1}` (471 each);
- the eight full `O_h` spectra.

The spectrum routine was cross-checked against sympy factorization on 400 sampled matrices, with 0 mismatches.

## 4. Assumptions, typed

**Lemma P itself.** It assumes only that `Φ` is affine and `Φ(O) ⊆ O`. It is pure convex geometry and linear
algebra.

**The chain that makes the lemma applicable** (§7 of the design):

| link | content | type |
| --- | --- | --- |
| L1 | Records factor through `R`: the detectors `S_Z`, `S_X` and `S_Y` read `f_z`, `f_x` and `f_y`, and `R_op = R` on outputs | imported representation (L-UPRIME, L-CAL); native meters |
| L2 | `R(Q) = V₀ = {0, ±e_a}`, so `conv R(Q) = O`. This needs `Λ_{y,b}` in the source | `Λ_{y,b}` is an H-PREP preparation obtainable under NNB: candidate strengthened (H-PREP, open hypothesis) plus a supplied conditional premise (NNB); N2 for its unknown slots. Probe: `R(Λ_{a,b}) = (−1)^b e_a`, `R(Λ_0) = 0`, `Λ_{a,1} = 2Λ_0 − Λ_{a,0}` |
| L3 | CONS at `j = 0` on all seven QA laws, so `Φ(±e_a) = R(πΛ_{a,b})`. Herald constancy is **not** needed: CONS on `Λ_{a,1}` already places `Φ(−e_a)` | measured (CONS) |
| L4 | Theorem C(ii), `R(πΛ) ∈ O` for the affine rules | conditional on three WIP records (AP1 Lemma 3, QA Lemma Q(iii), MI-R C-LIN), on P1 (candidate strengthened, RET-s), P2/SA-1(c) (posited), N2, H-INF-μ and forward conditioning. One model review. Not established (§A.46 item 1), as REACHABLE says |
| L5 | The comparator: signed-permutation spectra as "Clifford class" | imported quantum structure, confined to the witness definition (comparator only) |

**Quantum structure.** None enters the proof:
- no Hilbert space, inner product, Born weight, unitarity or Clifford/stabilizer formalism;
- `O` enters as the ℓ1 unit ball in bias coordinates `r_a = P(f_a = 0) − P(f_a = 1)`;
- the words "stabilizer octahedron" and "Clifford class" are comparator labels (L5).

The only quantum-flavoured inputs are upstream of the lemma, in L1's identification and L4's posits, and the design
already types them.

**Design wording (minor finding LP-1).** DESIGN-DS §6 justifies the self-map property by "Theorem C(ii) under NNB
(`O = conv R(L)`)". The property that is used, and sufficient, is `conv R(Q) = O` (L2) together with
`R(πQ) ⊆ R(L) ⊆ O` (L4). Proposition L's equality `O = conv R(L)` is neither needed nor sufficient on its own,
because CONS constrains `Φ` only on the orbit of `Q`, not on all of `L`. NNB enters only through `Λ_{y,b} ∈ Q`.

## 5. §A.34 directionality

Lemma P is a one-way implication: self-map of `O` ⇒ allowed unit spectrum. The design uses it only in that direction:
- affine rule, plus Theorem C(ii), plus L1–L3 ⇒ self-map ⇒ no W-CL (CC-NAT's expectation, §7's "direction that
  holds", §8's ABL row);
- equivalently, by contraposition, W-CL ⇒ not a self-map of `O`, which is valid.

The converse (an allowed spectrum ⇒ a self-map of `O`) is false, e.g. `2I` has empty unit spectrum and is not a
self-map, and it is nowhere used; nor is the lemma read as an equivalence anywhere. `W-OCT` rests on Theorem C(ii)
directly, not on Lemma P.

## 6. What relies on Lemma P, and whether that reliance survives

| reliance | survives? |
| --- | --- |
| CC-NAT's green-when column ("no W-CL with CONS") | **Yes.** Lemma P is proved. The paper expectation is now conditional only on Theorem C(ii) and L1–L3. CC-NAT's route to failure should keep "a failure of Theorem C(ii)" and can drop "a failure of Lemma P" |
| DESIGN-DS §7: "Every composition-consistent record operation is a self-map of `O`, so W-CL does not fire" | **Yes**, conditional on Theorem C(ii). Apply LP-1's wording correction |
| §8, ABL row "Theorem C with Lemma P: no W-CL" | **Yes**, same condition. ABL is measured directly in any case |
| the W-CL frame rule: "sound because `P ∈ O_h`" | **Yes.** `P^kΦ` and `P^{k+1}ΦP` are self-maps of `O` whenever `Φ` is |

Lemma P adds no physics. It converts the octahedral confinement of laws (Theorem C(ii)) into a spectral confinement of
composition-consistent maps, and so inherits Theorem C(ii)'s conditional status. It does not by itself make CC-NAT's
expectation unconditional.

## 7. Notes for r10

- The r10 table *Sketches under independent review* withholds CC-NAT's paper expectation, and demotes CC-NAT, if this
  review fails. This review passes, so that row does not apply.
- CC-NAT's paper basis should then read "Theorem C(ii) (conditional) and Lemma P (proved, independently reviewed)".
- Keep "or a failure of Theorem C(ii)" in its route to failure. A red CC-NAT then points at Theorem C(ii), L1–L3, or a
  propagation error, but not at Lemma P.
- Quote this verdict in the PENDING slot.

## 8. Probe

| file | sha256 | content |
| --- | --- | --- |
| `review/proofs/probe_lemma_p.py` | `6ba8e0bc2ea87290793c1d3d5449afb05f05fbe0a8165587a4bc2f6014daf760` | §3's searches and checks. Exact (`fractions`, sympy over ℚ). Prints `ALL LEMMA-P PROBES GREEN`. Runtime ≈ 4 min |
