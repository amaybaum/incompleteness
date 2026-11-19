# R1-INF — a default probability law on an infinite configuration space

**Status.** Writer's paper-only research record, revised after the independent review of
`229112b8` ([#1431 comment 7025214238](https://github.com/amaybaum/incompleteness/pull/1431#issuecomment-7025214238),
REVISE). A delta review of the revised head is required. Paper proofs, standard citations and exact
finite computations (`r1_inf_checks.py`, §9) only. No Lean module, manuscript edit, premise adoption
or merge. A1 (Main posit ledger item (ii)) remains open and unadopted. No statement here is a premise
of an established claim.

**Authorization.** Owner `amaybaum`, [#1169 comment 7023834853](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7023834853),
2026-11-19T22:21:00Z, item 3, row P2: "**R1-INF** (#1055): a default probability law on an
infinite configuration space | Distinguish existence, normalization and uniqueness. Test
countermodels; do not assume the law exists". The same comment states: "These are investigation
only. None adopts a premise. Each needs independent non-author review, and each needs its own merge
decision."

**Goal link (§A.47), from the authorization.** "P2 is the A1-free foundations." This unit decides,
for the R1 consumers named below, whether a principled normalized invariant law exists on an
infinite carrier for OI's rule class, so that R1 is either closed by a stated selection or recorded
as an obstruction with countermodels.

**Source pin.** `main` at `bae5cfdd8` (drafted at `21e16c61e4dfa07f5902fdc113fbf8eeb974d441`; the
`papers/*.md` sources and the NR-1 and OA-1 records cited are byte-identical between the two).
`M:n`, `GR:n`, `SM:n` are lines of `papers/Main.md`, `papers/GR.md`, `papers/SM.md` at the pin. NR-1
is `verification/audits/foundations/nr1-near-return-20261116/NR-1.md`; A1-REMAINDER is
`verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` (on `main` from `2be3cfad`).

**Question (as authorized, with the coordinating brief's split).** Is there a principled default
probability law on an infinite configuration space that does the work R1 needs? Three parts are kept
separate: **(E)** existence of an invariant probability law for the OI update; **(N)**
normalization (a probability law, not an infinite invariant measure); **(U)** uniqueness or
canonical selection without fitting.

**R1 consumers** (A1-REMAINDER §2 R1 and rows M1–M3, C1, C4; each is cited here from its source):
Lemma 3's selection clause (M:54, M:58); posit (iv) (M:730) with μ-G, μ-O, μ-R (OA-1 r5:100–109);
the doubly stochastic corner (M:60, prong 1; "L3"); the uniform counting of GR:58 (H-count, coupled
case) and of H-BD (GR:122, proof GR:126).

**Answer.** E and N hold for every injective cellular automaton on a full finite-alphabet site
product. U holds for the uniform Bernoulli law `β_A` once the admissible laws are required to be
translation invariant (G3) and the selection functional is entropy per site (G4) (Proposition 3,
"P-ED"). Under (G3) the rule plays no role in the selection: P-ED selects the same law for every
surjective cellular automaton, so it restates A1's uniform choice in per-site form rather than
deriving it. Without (G3), the selected update itself selects `β_A` in `d = 1` (Proposition 9 (a)).
In `d ≥ 2`, including the physical `d = 3`, it does not: a second rule-invariant law has full
entropy density (Proposition 9 (b)), so P-ED's uniqueness there rests entirely on (G3).

## 1. Productivity test (fixed before the nodes, §A.31)

Fixed in the brief and adopted unchanged. The result is a gem iff it gives (i) a candidate
satisfying E+N+U for the OI rule class that restores at least one R1 consumer, with its hypotheses
explicit, or (ii) a scoped obstruction showing that U fails for that class, with countermodels.
Anything else is relabelling. Favourable branches are pressure-tested where they occur (§6).

## 2. Setting

**Carrier and rule class.** A finite alphabet `A`, `d ≥ 1`, `Ω = A^{Z^d}` with the product topology
(compact, metrizable), lattice translations `τ_g`. A **cellular automaton (CA)** is a continuous map
`F: Ω → Ω` commuting with every `τ_g`; equivalently (Curtis–Hedlund–Lyndon; Hedlund 1969) `F(x)(z)`
is a fixed local rule applied to `x|_{z+N}` for a finite neighbourhood `N`. The **OI rule class**
used here is: injective CA on a full site product (on a full shift these are bijective: Hedlund
1969; Richardson 1972, J. Comput. System Sci. 6:373–388). It contains the selected update.

**Selected update** (NR-1 §2 (U); M:730 item (xiii); SM:224–228): `A = Z_q^2`, state `(u, v)`,
`F(u, v) = (αSu − v, u)` with `(Sf)(z) = Σ_j f(z+e_j) + f(z−e_j)`. It is a bijective CA for every
`q, α`: `F^{-1}(u, v) = (v, αSv − u)`. `x_t` denotes the first component of `F^t(u, v)`, so
`x_0 = u`, `x_{−1} = v` and `x_{t+1} + x_{t−1} = αSx_t` for all `t ∈ Z`.

**Notation.** `β_A` is the uniform Bernoulli law on `Ω` (for the selected update, Haar measure of
the compact group `Ω`; NR-1 Lemma 2.1). `Per_L` is the finite set of configurations invariant under
`τ_{L e_j}` for all `j` (the cubic torus). `X_fin ⊂ Ω` is the countable set of finitely supported
configurations (relative to a quiescent symbol `0`). For a translation-invariant law `μ`, `H_n(μ)` is
the Shannon entropy of the marginal of `μ` on the cube `[0, n)^d`, and the **entropy density** is
`h(μ) = lim_k H_{2^k}(μ)/2^{dk}` (the limit exists by Lemma 2's monotonicity; it agrees with the
limit over all cubes, Georgii 1988, Ch. 15, which is not used). For an arbitrary law, the **centred
upper entropy density** is `h̄(μ) = limsup_n H(μ|_{Λ_n})/|Λ_n|` with `Λ_n = [−n, n]^d`; it is the
functional used when (G3) is dropped (Proposition 9). `R_Λ` is the set of characters of `Ω`
supported in `Λ`.

## 3. Results (paper proofs; exact checks in §9)

**Lemma 1 (E, N; the torus limit).** Let `F` be an injective CA on `Ω`. Then (a) for every `L` the
counting probability `μ_L` on `Per_L` is `F`-invariant; (b) `μ_L → β_A` on every cylinder; (c)
`β_A` is `F`-invariant.

*Proof.* (a) `F` commutes with translations, so `F(Per_L) ⊂ Per_L`; `F` is injective, `Per_L` is
finite, so `F|Per_L` is a bijection and preserves counting. (b) For a box `B` and `L` larger than
the side of `B`, `B` embeds injectively in the torus, so the restriction `Per_L → A^B` is onto and
every fibre has the same size: the marginal of `μ_L` on `B` is uniform. (c) Let `[P]` be a cylinder
on a box `B`. `F^{-1}[P]` is a finite union of cylinders on `B + N`. Take `L` larger than the side
of `B + N`. Then `β_A(F^{-1}[P]) = μ_L(F^{-1}[P] ∩ Per_L) = μ_L((F|Per_L)^{-1}([P] ∩ Per_L)) =
μ_L([P] ∩ Per_L) = β_A([P])`, by (b), (a) and (b). Cylinders form a generating π-system, so
`F_*β_A = β_A`. `□`

The proof uses injectivity on each `Per_L` only. For surjective CA in general the invariance of
`β_A` is Hedlund's (Hedlund 1969, Thm. 5.4, as cited by Kari–Taati 2015, §4.2), and it is the
`f ≡ 0` case of Kari–Taati's Theorem 41. For the selected update (c) is NR-1 Lemma 2.1, and (b) is
NR-1 Prop. 4.3.

**Lemma 2 (U: uniqueness of maximal entropy density).** Among translation-invariant probability laws
on `Ω`, `h(μ) ≤ log|A|`, with equality iff `μ = β_A`.

*Proof.* `[0, 2n)^d` is the disjoint union of `2^d` translates of `[0, n)^d`; subadditivity of
Shannon entropy and translation invariance give `H_{2n} ≤ 2^d H_n`, so `H_{2^k}/2^{dk}` is
nonincreasing in `k` and bounded by `log|A|`. If its limit is `log|A|`, every term equals
`log|A|`, so every dyadic cube marginal is uniform. Every finite set lies in a translate of a dyadic
cube, and marginals of a uniform law are uniform, so all finite marginals of `μ` are those of
`β_A`. Conversely `h(β_A) = log|A|`. `□`

The lemma involves no rule: it is the uniqueness of the measure of maximal entropy of the full
`Z^d` shift.

**Proposition 3 (P-ED: selection under translation invariance).** Assume

- (G1) the carrier is the full site product `Ω = A^{Z^d}`, `A` finite;
- (G2) the rule `F` is an injective CA;
- (G3) the admissible laws are the Borel probabilities invariant under `F` **and** under every
  lattice translation;
- (G4) the selection functional is the entropy density `h`.

Then exactly one admissible law maximizes `h`: the uniform Bernoulli law `β_A`. It is the cylinder
limit of the counting laws `μ_L` on the periodic tori, which Lemma 3 of Main selects on each
`Per_L`.

*Proof.* `β_A` is translation invariant and `F`-invariant (Lemma 1), and is the unique maximizer of
`h` among all translation-invariant laws (Lemma 2), hence among admissible ones. The limit statement
is Lemma 1 (b). `□`

*Role of the rule.* `F` enters only through admissibility (Lemma 1). The maximizer is fixed by
(G3) and (G4) alone and is the same for every surjective CA on `Ω`. On a finite carrier Lemma 3 of
Main has the same structure: the uniform law maximizes Shannon entropy over all laws, and its
invariance is checked afterwards. P-ED therefore replaces "finite carrier with counting" by
"translation-invariant laws with entropy per site relative to product counting"; it relocates the
uniform posit rather than deriving it from the dynamics.

**Lemma 4 (selected update, `q` prime, `α ≠ 0`: no finite orbits, mixing).** Let `R =
F_q[x_1^{±1}, …, x_d^{±1}]`, `s = Σ_j (x_j + x_j^{-1})`. (a) No nonzero `x ∈ X_fin` has a finite
`F`-orbit. (b) No nontrivial character of `Ω` has a finite orbit under the dual automorphism.
(c) Haar measure `β_A` is ergodic and mixing for `F`. (d) The set of `F`-periodic points has Haar
measure zero.

*Proof.* Identify `X_fin` with `R^2`; `F` acts by `P = [[αs, −1], [1, 0]]`. Characters of `Ω` are
finitely supported `(χ_u, χ_v)`, and `⟨χ, F(u,v)⟩ = Σ (αSχ_u + χ_v)u − χ_u v` (S is symmetric), so
the dual acts on `R^2` by `M = [[αs, 1], [−1, 0]]`. Both have characteristic polynomial
`λ² − αsλ + 1`. If `P^n w = w` (or `M^n w = w`) with `w ≠ 0`, `n ≥ 1`, then `P^n − I` is singular
over `K = Frac(R)`, so an eigenvalue `λ` in an algebraic closure of `K` satisfies `λ^n = 1`; it is
algebraic over `F_q`, and so is `λ + λ^{-1} = αs ∈ K`. But `F_q` is algebraically closed in the
rational function field `K`, and `αs` is nonconstant (`α ≠ 0`, `d ≥ 1`): contradiction. This
gives (a) and (b).

(c) For characters `χ, ψ` (written `e(⟨χ, x⟩)` with `e(k) = exp(2πik/q)`), orthogonality of
characters under Haar measure gives `∫ e(⟨χ, F^n x⟩) \overline{e(⟨ψ, x⟩)} dβ_A = 1` if
`M^n χ = ψ` and `0` otherwise. For nontrivial `χ` the points `M^n χ`, `n ≥ 0`, are pairwise
distinct by (b) (`M` is bijective, so a repetition gives a finite orbit), so for each `ψ` the
correlation is nonzero for at most one `n`. Hence `⟨f∘F^n, g⟩ → ∫f ∫ḡ` for all trigonometric
polynomials `f, g`. These are dense in `L²(β_A)`: the functions of finitely many coordinates are
dense, and each is a finite combination of characters (finite Fourier transform on
`(Z_q^2)^B`). A uniform `L²` approximation argument extends the limit to all `f, g ∈ L²`: `F` is
mixing, hence ergodic. (This is the argument of Halmos 1943 for automorphisms of compact abelian
groups; it is written out here because the source was not consulted.)

(d) `Fix(F^n)` is `F`-invariant; by ergodicity its measure is 0 or 1. If it were 1, then
`β_A(A ∩ F^{-nk}A) = β_A(A)` for every Borel `A` and every `k`, while mixing gives the limit
`β_A(A)²`; a cylinder with `0 < β_A(A) < 1` contradicts this. A countable union of null sets is
null. `□`

Proposition 5 below gives (c) and (d) for every `q` with `α ∈ Z_q^×`, by a conjugacy to a Bernoulli
shift. (a) and (b) for composite `q` are not settled here.

NR-1 does not state mixing: it proves invariance (Lemma 2.1) and that hidden data reach the window
at every time (Prop. 2.3), and it records that the RO-3 mixing unit it mentions is on an unmerged
branch and was not used (NR-1:27–29). Mixing is proved here.

**Proposition 5 (candidate (b): measures of maximal entropy of `F` as a `Z`-action).**
`α ∈ Z_q^×` (any `q ≥ 2`) unless stated.

1. *`d = 1`: E+N+U hold.* The map `Φ(u,v) = (x_t(0), x_t(1))_{t∈Z}` is a topological conjugacy of
   `F` onto the full shift on `q²` symbols and a group isomorphism. *Proof.* The rule
   `x_{t+1}(z) + x_{t−1}(z) = α(x_t(z−1) + x_t(z+1))` can be solved for `x_t(z+1)` and for
   `x_t(z−1)` because `α` is a unit; given two full columns, the remaining columns are determined,
   and any pair of column sequences extends to a space-time configuration satisfying the rule at
   every site (each new column enforces the rule on its neighbour). `Φ` is a continuous bijection of
   compact metric spaces commuting with the dynamics. `□` Hence `h_top(F) = 2 log q` and the unique
   measure of maximal entropy is `Φ^{-1}` of the uniform Bernoulli law, which is Haar (a group
   isomorphism carries Haar to Haar). Uniqueness for the full shift is Lemma 2 with `d = 1`, since
   the Kolmogorov–Sinai entropy of a shift-invariant law on a full shift equals its entropy density
   along `Z` (the time-zero partition generates). In `d = 1` candidate (b) coincides with P-ED.
2. *`d ≥ 2`: Haar has infinite entropy and U fails.* Write `z = (z_1, y)`, `y ∈ Z^{d−1}`, and let
   `B = (Z_q^2)^{Z^{d−1}}`. The map `Ψ(x) = (x_t(0, ·), x_t(1, ·))_{t∈Z} ∈ B^Z` (the two planes
   `z_1 ∈ {0, 1}`, all transverse sites, all times) is a continuous group isomorphism conjugating
   `F` to the shift on `B^Z`. *Proof.* As in item 1, with planes for columns:
   `x_t(z_1+1, y) = α^{-1}(x_{t+1}(z_1, y) + x_{t−1}(z_1, y)) − x_t(z_1−1, y) − Σ_{j≥2}
   (x_t(z_1, y+e_j) + x_t(z_1, y−e_j))`, whose right side involves only the two known planes;
   symmetrically towards `z_1 − 1`. Every pair of plane sequences extends to a space-time solution,
   and `Ψ` is continuous because each `x_t(z)` depends on finitely many coordinates. `□` Haar is
   carried to Haar on `B^Z`, the product of Haar measures on `B`: `(Ω, F, β_A)` is a Bernoulli shift
   with non-atomic base. For any finite set `Y` of transverse sites, the time-zero partition by the
   coordinates on `{0, 1} × Y` has independent shift iterates, so `h_{β_A}(F) ≥ 4|Y| log q` for all
   `Y`: `h_{β_A}(F) = h_top(F) = ∞`. Then `β_A` and `(β_A + δ_0)/2` (affinity of entropy, Walters
   1982, Ch. 8) are two distinct measures of maximal entropy. Items 1 and 2 also show that `β_A` is
   Bernoulli, hence mixing of all orders, for every `q` with `α` a unit and every `d`.
3. *Zero entropy: U fails maximally.* If `α` is a nonzero nilpotent in every primary component in
   which it is not zero (some non-squarefree `q`, NR-1 Prop. 5.1), or `α = 0` (`F^4 = id`), then
   `F^N = id` for some `N`, `h_top(F) = h_top(F^N)/N = 0`, and every invariant law is a measure of
   maximal entropy. These parameter values are admitted by the form lemma (NR-1 node 5
   assumption-watch marker).
4. *Nonzero potentials.* For `d = 1` the full-shift conjugacy gives, for every Hölder potential, a
   unique equilibrium state (Bowen 1975, LNM 470); the potential is a free function, so this family
   can fit any fully supported Gibbs law along time and is excluded as a selection under §A.29.

**Proposition 6 (candidate (c): Gibbs/DLR states; `d = 1`, `α² ≡ 1 mod q`).** (a) The zero
interaction has the product uniform specification, whose unique DLR state is `β_A`; this is P-ED.
(b) For the selected update with `d = 1` and `α² ≡ 1`, the **movers** `a_z = u_z − αv_{z+1}`,
`b_z = u_{z+1} − αv_z` satisfy `a'_z = α a_{z−1}`, `b'_z = α b_{z+1}` (direct substitution, using
`α² = 1`; checked in §9 E). The homomorphism `Ψ_1: (u,v) ↦ (a,b)` is onto with kernel `K` of order
`q²` (given `(a,b)`, `v_{z+2} = v_z + α(b_z − a_{z+1})` with `v_0, v_1` free, then
`u_{z+1} = b_z + αv_z`), and it intertwines `F` with `αR × αL` (`R`, `L` the right and left
shifts). Lifting any law `λ` of `(a,b)` by the uniform law on the fibres (cosets of `K`, which `F`
and the translations permute affinely) gives a law that is `F`-invariant iff `λ` is
`αR × αL`-invariant, and translation invariant iff `λ` is. Taking `λ = π_a^{⊗Z} ⊗ π_b^{⊗Z}` with
marginals invariant under `x ↦ αx` gives a family of `F`- and translation-invariant laws with
`2(q−1)` free parameters when `α = 1` (two for `q = 3`, `α = 2`). Their entropy density is
`H(π_a) + H(π_b)` (finite fibres do not change the density), maximal exactly at uniform marginals,
i.e. at `β_A`. The mover densities are additive real-valued conserved quantities of range 2; the
rational linear algebra of §9 E finds that, on the tori tested, the conserved range-2 quantities
exceed the trivial ones (constants and coboundaries) by exactly the mover count. (c) Kari–Taati
2015 (J. Stat. Phys. 160:1198–1243; arXiv:1311.2319), for a surjective CA on a strongly irreducible
shift of finite type on `Z^d` (a full shift is one) and an observable `f` with summable variations:
**Theorem 41**, the CA conserves `f` iff it maps the set of shift-invariant equilibrium measures of
`f` (equal to the shift-invariant Gibbs measures, their Theorem 12) onto itself, iff it maps one
such measure into that set; **Theorem 42**, conservation implies that the set of measures of maximal
entropy at a fixed density of `f` is mapped onto itself (one direction only), so an invariant
measure exists in each such set. So (E) for constrained Gibbs selection is a question about
conservation laws of `F`, and where conservation laws exist, (U) needs the conserved densities,
which are free parameters.

*Consequence for the selected update in `d = 1`.* "Maximal entropy at fixed conserved densities" is a
`2(q−1)`-parameter generalized Gibbs family; "maximal entropy among invariant laws" without
constraint is P-ED. Whether the selected update has real-valued additive conserved quantities for
`d ≥ 2` is not determined here. SM:292 records that the exact linear rule conserves its quadratic
energy only modulo `q`, and that neither that fact nor the rounded rule supplies "the required real
positive-definite conserved energy"; the movers are not such an energy and are specific to `d = 1`,
so this record makes no finding against SM:292.

**Proposition 7 (candidate (e) and the orbit-level measures).** `α ∈ Z_q^×`, `β_A` Haar.

1. *μ-O collapses to μ-G.* For `β_A`-almost every microstate the orbit is infinite (Lemma 4 (d),
   extended to unit `α` by Prop. 5) and its empirical measures `(1/n)Σ_{t<n} δ_{F^t x}` converge
   weak-* to `β_A` (ergodicity and Birkhoff's theorem applied to a countable dense set of continuous
   functions). The orbit-level law of a typical microstate is therefore `β_A`, which is μ-G; the
   orbit itself has measure zero. A1-REMAINDER's lemma L2 asks for μ-O "with its static budget": the
   budget is not supplied, since the orbit capacity `log₂ p` of M:60 is infinite. "Typical" is
   relative to `β_A` itself; for example, nonzero points of `X_fin` and periodic points have other
   empirical limits.
2. *μ-R collapses to μ-G.* For a record cylinder `[P]` of positive measure, the union of the orbits
   meeting it, `E = ∪_{t∈Z} F^{-t}[P]`, is `F`-invariant with `β_A(E) ≥ β_A([P]) > 0`, so
   `β_A(E) = 1` by ergodicity. "Uniform on the record-compatible orbits" is `β_A`: at the orbit level
   the records exclude nothing.
3. *Without a reference law, (e) is ill-posed.* Every non-atomic law has infinite Shannon entropy,
   and entropy density does not see a finite window: for `F = id` (an injective CA), every law that
   fixes the record on a finite window and is uniform and independent elsewhere has density
   `log|A|`. With `β_A` as reference, "maximal entropy compatible with the records" becomes the
   minimum-relative-entropy law subject to the record, which is the conditional law `β_A(·|[P])`
   (Csiszár 1975, Ann. Probab. 3:146–158); it is a preparation, not an invariant law. Candidate (e)
   therefore does not select independently of (a)/P-ED.

**Lemma 8 (L3 under P-ED).** Let `μ = ν ⊗ ρ` on `V × H` be `F`-invariant with `ν` uniform on the
finite visible set `V`, and `Γ_t(a,b) = ρ{h : π F^t(a,h) = b}` (M:135). Then every `Γ_t` is doubly
stochastic. *Proof.* Rows sum to one because `ρ` is a probability. `Σ_a Γ_t(a,b) = |V| μ(π∘F^t = b) =
|V| μ(π = b) = |V| ν(b) = 1`, by invariance (uniformity of `ν` is used in the first and last
steps). `□` Under P-ED, `β_A = Unif(V) ⊗ β_A|_H` whenever the visible variable is a window
(coordinate) readout `π = x|_W`, `W` finite. For such readouts the doubly stochastic corner of M3 and
the premise of prong 1 at M:60 ("the marginal of a bijection under the uniform prior is doubly
stochastic") hold for every injective CA on a full site product, with no finiteness of the carrier.
Main's visible partition is a general coarse-graining; readouts that are not coordinate projections
are not covered here. The §9 C countercontrol shows the conclusion failing under the non-invariant
product `Unif(V) ⊗ δ_0`.

**Proposition 9 (U without (G3), for the selected update).** The arguments of (a) and (b) were
supplied by the independent review of `229112b8` (#1431 comment 7025214238); they are written out
and checked here (§9 A, G).

(a) *`d = 1`, `α ∈ Z_q^×`: (G3) is not needed.* If `μ` is `F`-invariant and `h̄(μ) = log|A|`
(centred intervals `Λ_n = [−n, n]`), then `μ = β_A`.

*Proof.* By the column reconstruction of Prop. 5.1, `(u, v)|_{Λ_n}` is a function of
`w_t = (x_t(0), x_t(1))` for `|t| ≤ n + 1`: the trajectory over `[−T, T]` determines columns
`−(T−1), …, T` at times `0` and `−1`, one column per time step lost at each end (§9 A checks the
columns `−4, …, 5` at `T = 6`). So
`H(μ|_{Λ_n}) ≤ H_μ(w_{−n−1}, …, w_{n+1})`. Under `μ` the process `(w_t)` is stationary, so
`G_m := H(w_1, …, w_m)` satisfies `G_m/m` nonincreasing with `G_m ≤ m · 2 log q`. Then
`h̄(μ) = log|A| = 2 log q` forces `lim G_m/m ≥ 2 log q`, hence `G_m = m · 2 log q` for every `m`:
`(w_t)` is i.i.d. uniform, `Φ_*μ` is the uniform Bernoulli law, and `μ = Φ^{-1}_*(uniform) = β_A`.
`□` This is Prop. 5.1's uniqueness transferred to the spatial functional: in `d = 1` the rule, not
(G3), selects.

(b) *`d ≥ 2`, `q` prime, `α ≠ 0`: U fails without (G3).* Let `Γ = span{x_t(0) : t ∈ Z}`, viewed as
characters of `Ω`, and `H = Γ^⊥ = {x ∈ Ω : x_t(0) = 0 for all t}`. Then `H` is a closed subgroup
with `F(H) = H`, so Haar measure `m_H` on `H` is `F`-invariant. It differs from `β_A` (`u(0) = 0`
almost surely), it is not translation invariant, and `h̄(m_H) = log|A|`.

*Proof.* `F(H) = H` because `(Fx)_t(0) = x_{t+1}(0)`; `F|_H` is a continuous automorphism of the
compact group `H`, so it preserves `m_H`. Define `A_{−1} = 0`, `A_0 = 1`,
`A_{m+1} = αsA_m − A_{m−1}`. The recurrence `x_{t+1}(0) + x_{t−1}(0) = α Σ_{nb} x_t(nb)`, with each
`x_t(nb)` the translate of `x_t(0)`, gives, as characters `(u-part, v-part)`,
`x_t(0) = (A_t, −A_{t−1})` for `t ≥ 0` and `x_{−1−k}(0) = (−A_{k−1}, A_k)` for `k ≥ 0`. `A_m` is
supported in the `ℓ¹`-ball of radius `m`, and contains `x_1^m` with coefficient `α^m ≠ 0`, while
`A_j`, `j < m`, does not contain `x_1^m`. Hence `x_t(0) ∈ R_{Λ_n}` for `−n−1 ≤ t ≤ n`. Conversely,
let `g = Σ_{t=0}^{T*} a_t x_t(0) + Σ_{k=0}^{K*} b_k x_{−1−k}(0)` with `a_{T*} ≠ 0` and
`b_{K*} ≠ 0` (one family may be empty). If `T* ≥ K*`, the u-part `Σ a_t A_t − Σ b_k A_{k−1}`
contains `x_1^{T*}` with coefficient `a_{T*}α^{T*} ≠ 0`; if `K* > T*`, the v-part
`−Σ a_t A_{t−1} + Σ b_k A_k` contains `x_1^{K*}` with coefficient `b_{K*}α^{K*} ≠ 0`. So `g ≠ 0`,
and `g ∈ R_{Λ_n}` forces `T*, K* ≤ n`. Therefore the `2n + 2` characters `x_t(0)`,
`−n−1 ≤ t ≤ n`, are independent and span `Γ ∩ R_{Λ_n}`: `dim(Γ ∩ R_{Λ_n}) = 2n + 2`. By duality the
image of `H` under restriction to `Λ_n` is the annihilator of `Γ ∩ R_{Λ_n}`, and `m_H` projects to
the uniform law on it, so `H(m_H|_{Λ_n}) = (2|Λ_n| − 2n − 2) log q`. With `|Λ_n| = (2n+1)^d`,
`h̄(m_H) = 2 log q = log|A|` for `d ≥ 2`. The character `u(e_1)` is not in `Γ` (§9 G; in
`R_{Λ_1}` the only elements of `Γ` are the span of `u(0)`, `v(0)`, `(αs, −1)` and `(−1, αs)`, and
`s` is symmetric in `x_1^{±1}`), so `τ_{e_1}H ≠ H` and `m_H` is not translation invariant. `□`

In `d = 1` the same construction has `h̄(m_H) = ½ log|A|`, consistent with (a). §9 G computes
`dim(Γ ∩ R_{Λ_n}) = 2n + 2` exactly for `d = 1` (`n ≤ 5`) and `d = 2` (`n ≤ 3`), for
`(q, α) ∈ {(2,1), (3,1), (3,2)}`, stable under the horizon used. Its countercontrol `α = 0` gives
`2`, not `2n + 2`.

*Consequence.* For the selected update in `d ≥ 2`, including the physical `d = 3`, the rule-invariant
laws of maximal centred entropy density include `β_A` and `m_H` (and translates of `m_H`). P-ED's
uniqueness there rests entirely on (G3). The dynamics selects `β_A` only in `d = 1`, where
candidate (b) already does.

## 4. E/N/U table

| Candidate | (E) existence | (N) normalization | (U) selection | Scope |
|---|---|---|---|---|
| (a) product Haar / uniform Bernoulli `β_A` | Yes for every injective CA on a full product (Lemma 1); selected update NR-1 Lemma 2.1 | Yes | Not by itself: declared, it is H-μ. Selected by P-ED or (d) | Full product carrier |
| (b) measure of maximal entropy of `F` (Z-action), potential 0 | Yes (`d ≥ 2`: `β_A` has `h = ∞`) | Yes | `d = 1`, `α` a unit: yes, Haar (Prop. 5.1). `d ≥ 2`: no (Prop. 5.2). `F^N = id` cases: no, every law (Prop. 5.3) | Selected update |
| (b′) **P-ED**: maximal entropy density among laws invariant under `F` and translations | Yes (Lemma 1) | Yes | Yes, `β_A` (Lemma 2, Prop. 3), fixed by (G3)+(G4) for every surjective CA. Without (G3): yes in `d = 1` (Prop. 9 (a)), no in `d ≥ 2` (Prop. 9 (b)) | (G1)–(G4) |
| (c) Gibbs/DLR, zero interaction | Yes | Yes | Yes, `β_A` (= P-ED) | Full product |
| (c) Gibbs/DLR, nonzero interaction (summable variations) | Iff `F` conserves it (Kari–Taati 2015, Thm. 41) | Yes | No in general: conserved densities are free parameters (Prop. 6; Kari–Taati Thm. 42); phase coexistence (countermodel C5) | — |
| (d) cylinder limit of counting laws on `Per_L` | Yes (Lemma 1) | Yes | Yes: the limit is unique and is `β_A` | Injective CA on full product |
| (e) maximal entropy compatible with records | Needs a reference law | — | Ill-posed without reference; with `β_A` it is conditioning (a preparation), and at the orbit level it collapses to `β_A` (Prop. 7) | — |

## 5. Countermodels

| # | Target | Countermodel | Status |
|---|---|---|---|
| C1 | E fails (no invariant probability) | The selected update (`q` prime, `α ≠ 0`) restricted to the countable carrier `X_fin \ {0}`: a bijection with no finite orbit (Lemma 4 (a)); an invariant probability on a countable set is constant on orbits, hence zero. The counting measure on `X_fin` is invariant, σ-finite and infinite (N fails) | Proved |
| C2 | E fails, infinite local alphabet | `F(x)(z) = x(z) + 1` on `Z^{Z^d}`: local and bijective; an invariant probability would have a site marginal that is a translation-invariant probability on `Z` | Proved |
| C3 | E on compact carriers | Not a countermodel: every continuous map of a compact metrizable space has an invariant Borel probability (Krylov–Bogolyubov; Walters 1982, Ch. 6). E fails only off compactness (C1, C2) | Cited |
| C4 | Several measures of maximal entropy | (i) `F^N = id` members of the OI form (`q = 4`, `α = 2`; `α = 0`): every invariant law (Prop. 5.3). (ii) Selected update, `d ≥ 2`: `β_A` and `(β_A + δ_0)/2` (Prop. 5.2). (iii) Constrained carrier: strongly irreducible `Z²` subshifts of finite type with two ergodic measures of maximal entropy (Burton–Steif 1994, ETDS 14:213–235); the identity CA on such a carrier makes both P-ED maximizers admissible, so (G1) is load-bearing. In `d = 1` irreducible SFTs have a unique one (Parry 1964) | Proved / cited |
| C5 | U fails for constrained (Gibbs) selection | (i) Selected update `d = 1`, `α² = 1`: generalized Gibbs family (Prop. 6). (ii) `F` = a lattice translation or the identity (injective CA): every translation-invariant law is admissible. By the variational principle (Georgii 1988, Ch. 15), the maximizers of entropy density at fixed energy density are the translation-invariant Gibbs measures at the conjugate inverse temperature, and for the nearest-neighbour Ising model in `d = 2` below the critical temperature these include two extremal phases (Georgii 1988, Ch. 6) | Proved / cited |
| C6 | U fails without translation invariance (G3) | (i) `F = id`: `δ_a` at the origin `⊗ β_A` elsewhere is invariant, has full centred entropy density and differs from `β_A`. (ii) The selected update itself, `d ≥ 2`, `q` prime, `α ≠ 0`: Haar measure on `H = {x : x_t(0) = 0 ∀t}` (Prop. 9 (b)). In `d = 1` with `α` a unit, U holds without (G3) (Prop. 9 (a)) | Proved |
| C7 | Product law not invariant | (i) Selected update `q = 2`, `α = 1`, with `Bern(1/4)` for `u` and `v`: `P(u'(0) = 1) = 7/16` (§9 D). (ii) The AND rule (not surjective, outside the class): `β_A` is not invariant (`1/4` vs `1/2`). (iii) A non-local bijection: exchange the clopen sets `[1]` and `[00]` of `{0,1}^Z` by a homeomorphism and fix the rest; measurable involution, not `β_A`-preserving (`1/2` vs `1/4`). (ii) and (iii) show surjectivity and locality are load-bearing for Lemma 1 | Proved |

## 6. Pressure on the favourable branch (P-ED), and what it restores

1. *(G3) carries the selection in `d ≥ 2`.* Lemma 3 of Main needs no translation invariance on a
   finite carrier (where `μ_L` is translation invariant automatically). In infinite volume, for the
   selected update in `d ≥ 2`, including `d = 3`, U fails without (G3) (Prop. 9 (b)); in `d = 1`
   the rule selects without it (Prop. 9 (a)). (G3) is a homogeneity posit on the admissible laws,
   not a finiteness posit, and it is not derived from the Definition or the axioms.
2. *(G1) is load-bearing.* With local constraints the analogous selection can be non-unique (C4
   (iii)). OI's site factorization (M:730 (viii), (xiii)) gives a full product.
3. *The literal counting measure survives only without normalization.* On `X_fin` it is invariant
   and infinite (C1); on `Ω` it is not σ-finite. The normalized continuation is `β_A`, which gives
   `X_fin` measure zero.
4. *Is it H-μ relabelled?* In observability, yes: P-ED's finite-window content (i.i.d. uniform
   substratum frequencies by the strong law of large numbers; temporal decorrelation by mixing)
   equals that of the torus counting law on every window and horizon inside the light cone (NR-1
   Prop. 4.1), and substratum cells are not observed (M:706 states that `ε` is stipulated). In
   logical role, P-ED replaces a declared law (H-μ) by declared admissibility and entropy
   conditions, (G3) and (G4), which fix the same uniform law for every surjective CA (Prop. 3, role
   of the rule). This restates A1's uniform choice in per-site form; it is not a derivation from the
   dynamics.

**R1 consumers under P-ED.**

| Consumer | Restored? | Basis |
|---|---|---|
| Lemma 3 selection clause (M:54, M:58); μ-G | Yes, in entropy-density form, under (G1)–(G4); the selection is fixed by (G3)+(G4), not by the rule | Prop. 3 |
| Doubly stochastic corner (M3, L3); prong 1 premise (M:60) | Yes for window (coordinate) readouts, any injective CA | Lemma 8 |
| μ-O (L2) | Collapses to μ-G for `β_A`-typical points (`α` a unit); L2's static budget is not supplied (infinite) | Prop. 7.1 |
| μ-R; orbit selection "compatible with the observer's records" (M:60; M:730 (iv)) | Collapses to μ-G; the orbit-level selection is vacuous | Prop. 7.2 |
| GR:58 H-count, coupled case | No: P-ED is the unconstrained (`β = 0`) law; no shell and no temperature. A shell analogue needs a real conserved energy and a density, which are free parameters (Prop. 6) | — |
| P7B node 6.3 (invariant shell law, coupled case) | Not closed; in `d = 1`, `α² = 1`, invariant laws at fixed mover densities exist (Prop. 6), which are not GR's energy shell | — |
| H-BD (GR:122, proof GR:126) | No (L10 open); a normalized deep law is available | — |

*Outside R1.* Typicality is filed under R5 in A1-REMAINDER (M19). Under P-ED it holds at
substratum level only (spatial frequencies by the strong law for the i.i.d. law `β_A`; temporal
averages by the ergodic theorem), not as M:762's canonical typicality (quantum, finite-dimensional).

**Further consequence, not an R1 consumer.** SM:811 takes its matter measure to be "the uniform
measure on the energy shell of a real-valued conserved energy, not the independent-uniform measure
on (Z/qZ)^{K×N}", and records that the polar candidate returns Haar on "the (inconsistent)
independent-uniform field". P-ED selects exactly the independent-uniform field. The finite counting
measure of Lemma 3 selects it too, so the tension is independent of A1; P-ED does not supply SM's
candidate measure.

## 7. §A.29 assessment of P-ED as a possible replacement of A1's measure role

- *Results preserved (controls).* Everything that uses only Lemma 1 of Main, the
  `S ⇔ D ⇔ Q_fb` equivalence (finite visible laws, constructed witnesses), and every finite-carrier
  theorem, since `β_A` is the cylinder limit of the counting laws they use (Lemma 1 (b)).
- *What it adds over A1's uniform choice.* No derivation: under (G3) the selection does not depend
  on the rule (Prop. 3), and without (G3) the rule selects only in `d = 1` (Prop. 9). In the
  physical `d = 3` the uniform law is posited through (G3)+(G4) as it is posited through finiteness
  and counting under A1.
- *Consequences.* Given the posited (G3) and (G4), the infinite lattice and the selected update
  (`q` prime, `α ≠ 0`), P-ED fixes NR-1's hidden prior (Haar), and NR-1's verdicts follow: no
  near-return, no rigidity (Prop. 2.3), and for lattice-convex windows no revival and
  P-divisibility at every horizon (Thm. 3.3). NR-1 already posited Haar for that analysis, so this
  is not a consequence beyond what positing Haar gives, and it is not an empirical prediction.
- *Empirical content.* None that discriminates it from A1 at accessible scales (§6 item 4).
- *Variability.* No free parameter under (G1)–(G4). The variants (local constraints, conserved
  densities, potentials, non-translation-invariant laws) each add parameters or lose uniqueness
  (C4–C6, Prop. 5.4, Prop. 6, Prop. 9 (b)) and are excluded as fit-anything.
- *Verdict.* P-ED fails §A.29 as a Layer-0 revision: it restates the uniform posit and delivers no
  independent prediction or postdiction. It is recorded as a mathematical selection result under
  stated hypotheses, not as a proposed premise.

## 8. Productivity verdict and classification

**Gem under (ii), with (i) met only formally.**

- *(i).* P-ED satisfies E+N+U for injective CA on a full finite-alphabet site product under
  (G1)–(G4), and restores Lemma 3's selection role in entropy-density form and the doubly
  stochastic corner (L3, window readouts). Because the selection is fixed by (G3)+(G4) for every
  surjective CA, this is L1 delivered in the form A1-REMAINDER §2 R1 already named ("the product
  uniform law as maximal entropy density among invariant laws"). It does not restore μ-O's distinct
  role or static budget, GR:58, H-BD (L10) or canonical typicality.
- *(ii).* For the selected update in `d ≥ 2` (`q` prime, `α ≠ 0`), U fails among rule-invariant laws
  without (G3) (Prop. 9 (b)), and fails for the dynamical-entropy reading (Prop. 5.2). It also fails
  for zero-entropy members of the OI form (Prop. 5.3), for constrained Gibbs selection when
  conserved densities exist (Prop. 6), and on constrained carriers (C4 (iii)). In `d = 1` with `α` a
  unit the rule selects `β_A` without (G3) (Props. 5.1, 9 (a)).

§A.31 classes:
- **ELABORATING** — P-ED (Lemmas 1–2, Prop. 3): L1 in the anticipated form, with (G3) as its added
  hypothesis.
- **NEW** — Prop. 9: in `d ≥ 2` the selected update does not select its law without (G3), and in
  `d = 1` it does. The argument originates in the independent review and is verified here.
- **NEW** — the `d = 1` mover conservation laws and generalized Gibbs family of the selected update
  (Prop. 6); the collapse of μ-O and μ-R to μ-G (Prop. 7); the Bernoulli conjugacy for unit `α`
  (Prop. 5.2), which gives infinite Haar entropy for `d ≥ 2` and mixing for composite `q`.
- **POSITIVE** — L3 is immediate from invariance (Lemma 8), as the A1-REMAINDER record expected.

**Assumption-watch markers.**
1. Any infinite-volume reading of "the maximal-entropy invariant measure" must state its admissible
   symmetry class (G3) and its entropy functional (G4). In `d ≥ 2` the symmetry class, not the rule,
   decides the answer (Prop. 9), and the two natural entropy readings (entropy density, dynamical
   entropy) differ (Prop. 5.2).
2. M:60's orbit-level "selection among orbits … compatible with the observer's records" uses finite
   orbits; under an ergodic infinite-volume law it selects nothing, and μ-O coincides with μ-G
   (Prop. 7).
3. The parameters `(q, α)` decide the mixing property (Lemma 4; Prop. 5 for unit `α`) and the
   zero-entropy branch (Prop. 5.3), extending NR-1's node 5 marker.

**Open.** Real-valued conserved quantities of the selected update for `d ≥ 2`; Lemma 4 (a), (b)
for composite `q`; a measure-theoretic H-BD (L10); the GR:58 shell in infinite volume.

## 9. Reproducible computation

Command (from the repository root, stdlib Python 3 only, about two minutes):
`python3 -I verification/audits/foundations/r1-inf-20261119/r1_inf_checks.py`, at the commit that
lands this record. Expected output (deterministic):

```
== A. d = 1: window {0,1} trajectory, onto and determining ==
q=2 alpha=1 T=6: onto rank 14/14 OK; central interval [-4,5] determined: True (20/20 coords)
q=3 alpha=1 T=6: onto rank 14/14 OK; central interval [-4,5] determined: True (20/20 coords)
q=3 alpha=2 T=6: onto rank 14/14 OK; central interval [-4,5] determined: True (20/20 coords)
q=5 alpha=1 T=6: onto rank 14/14 OK; central interval [-4,5] determined: True (20/20 coords)
q=5 alpha=3 T=6: onto rank 14/14 OK; central interval [-4,5] determined: True (20/20 coords)
countercontrol q=3 alpha=0: window rank 4 (bounded); u0(2) determined: False
== B. d = 2, q = 2, alpha = 1: rank increments of the n x n box-window trajectory ==
n=1: rank(T), T=1..8: [1, 2, 3, 4, 5, 6, 7, 8]; increments [1, 1, 1, 1, 1, 1, 1, 1]
n=2: rank(T), T=1..8: [4, 8, 12, 16, 20, 24, 28, 32]; increments [4, 4, 4, 4, 4, 4, 4, 4]
n=3: rank(T), T=1..8: [9, 18, 26, 34, 42, 50, 58, 66]; increments [9, 9, 8, 8, 8, 8, 8, 8]
n=4: rank(T), T=1..8: [16, 32, 44, 56, 68, 80, 92, 104]; increments [16, 16, 12, 12, 12, 12, 12, 12]
== C. rooted maps, d = 1, W = {0,1}: row sums and column sums (L3) ==
uniform hidden prior q=2 alpha=1 t=1: rows sum to 1: True; columns sum to 1: True
uniform hidden prior q=2 alpha=1 t=2: rows sum to 1: True; columns sum to 1: True
uniform hidden prior q=2 alpha=1 t=3: rows sum to 1: True; columns sum to 1: True
uniform hidden prior q=3 alpha=1 t=1: rows sum to 1: True; columns sum to 1: True
uniform hidden prior q=3 alpha=1 t=2: rows sum to 1: True; columns sum to 1: True
countercontrol hidden delta_0 q=2 t=2: rows sum to 1: True; column sums ['0', '4']
countercontrol hidden delta_0 q=3 t=2: rows sum to 1: True; column sums ['0', '9']
== D. product laws that are not invariant ==
selected rule q=2 alpha=1 under Bern(1/4)^Z for u and v: P(u'(0)=1) = 7/16 (input marginal 1/4)
AND rule (not surjective) under uniform Bernoulli: P(y(0)=1) = 1/4 (input marginal 1/2)
== E. real-valued additive conserved quantities of range k (tori), dim vs trivial dim ==
identity (control), k=2, L=3..8: solution dim 4, trivial dim 2 -> nontrivial conserved quantity
rule 184 (control), k=2, L=3..10: solution dim 3, trivial dim 2 -> nontrivial conserved quantity
selected q=2 alpha=1, k=1, L=3..8: solution dim 1, trivial dim 1 -> only trivial
selected q=2 alpha=1, k=2, L=3..7: solution dim 6, trivial dim 4 -> nontrivial conserved quantity
selected q=3 alpha=1, k=1, L=3..5: solution dim 1, trivial dim 1 -> only trivial
selected q=3 alpha=1, k=2, L=3..5: solution dim 13, trivial dim 9 -> nontrivial conserved quantity
selected q=3 alpha=2, k=2, L=3..5: solution dim 11, trivial dim 9 -> nontrivial conserved quantity
movers q=2 alpha=1 (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): True
movers q=3 alpha=1 (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): True
movers q=3 alpha=2 (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): True
movers q=5 alpha=1 (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): True
movers q=5 alpha=4 (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): True
== F. finitely supported seeds: no return (illustration) ==
d=1 q=2 alpha=1: single-site seed returns within 400 steps: False; final support 801
d=1 q=3 alpha=1: single-site seed returns within 400 steps: False; final support 801
d=1 q=5 alpha=2: single-site seed returns within 400 steps: False; final support 309
== G. U without translation invariance: H = {x : x_t(0) = 0 for all t} ==
functionals x_t(0) agree with direct evolution on tori: True
d=1 q=2 alpha=1: deficit dim(Gamma ∩ R_Lambda_n), n=1..5: [4, 6, 8, 10, 12]; equals 2n+2: True
d=1 q=3 alpha=1: deficit dim(Gamma ∩ R_Lambda_n), n=1..5: [4, 6, 8, 10, 12]; equals 2n+2: True
d=1 q=3 alpha=2: deficit dim(Gamma ∩ R_Lambda_n), n=1..5: [4, 6, 8, 10, 12]; equals 2n+2: True
d=1 q=3 alpha=0 [countercontrol alpha=0]: deficit dim(Gamma ∩ R_Lambda_n), n=1..5: [2, 2, 2, 2, 2]; equals 2n+2: False
d=2 q=2 alpha=1: deficit dim(Gamma ∩ R_Lambda_n), n=1..3: [4, 6, 8]; equals 2n+2: True
d=2 q=3 alpha=1: deficit dim(Gamma ∩ R_Lambda_n), n=1..3: [4, 6, 8]; equals 2n+2: True
d=2 q=3 alpha=2: deficit dim(Gamma ∩ R_Lambda_n), n=1..3: [4, 6, 8]; equals 2n+2: True
d=2 q=3 alpha=0 [countercontrol alpha=0]: deficit dim(Gamma ∩ R_Lambda_n), n=1..3: [2, 2, 2]; equals 2n+2: False
d=2 q=2 alpha=1: u(e_1) in span{x_t(0): |t|<=7}: False
== H. d = 2: two-plane trajectory {z_1 in {0,1}} x [-m,m] is onto and determining ==
q=2 alpha=1: forward rank 56/56; u0,v0 at (2,0), u0 at (-1,0), v0 at (-1,1) determined: True
q=3 alpha=1: forward rank 56/56; u0,v0 at (2,0), u0 at (-1,0), v0 at (-1,1) determined: True
q=3 alpha=2: forward rank 56/56; u0,v0 at (2,0), u0 at (-1,0), v0 at (-1,1) determined: True
q=5 alpha=3: forward rank 56/56; u0,v0 at (2,0), u0 at (-1,0), v0 at (-1,1) determined: True
countercontrol q=3 alpha=0: u0 at (2,0) determined: False
```

**What each part supports.**
- A: both halves of the `d = 1` conjugacy (Prop. 5.1) at `T = 6`, as finite instances of the proof's
  column argument; the `α = 0` countercontrol, where the window is uninformative. It also checks the
  reconstruction step used in Prop. 9 (a).
- B: illustration only of Prop. 5.2's infinite entropy; finite ranks prove no limit.
- C: Lemma 8 by brute force over the hidden light cone, using no linearity, and its countercontrol.
- D: C7 (i), (ii).
- E: the controls detect the known conserved quantities (all functions for the identity; particle
  number for rule 184). The excess dimensions for the selected update (2, 4, 2) equal the mover
  counts of Prop. 6 (`2(q−1)` for `α = 1`; one even nonconstant function per mover for `q = 3`,
  `α = 2`), and the identification is checked on random tori. Torus equations are necessary
  conditions for conservation on `Z`, so they bound the conserved space from above; the movers
  bound it from below.
- F: illustration of Lemma 4 (a), whose proof is algebraic.
- G: Prop. 9 (b). The site functionals `x_t(0)` are built by the recurrence and cross-checked
  against direct evolution on tori. `dim(Γ ∩ R_{Λ_n})` equals `2n + 2` for every case and every
  horizon `T ∈ {n+1, n+3, n+5}`. The `α = 0` countercontrol gives 2. `u(e_1) ∉ Γ`.
- H: Prop. 5.2's two-plane conjugacy in `d = 2`: the forward plane trajectory has full rank (onto),
  and the plane trajectory over `[−T, T]` determines the neighbouring planes' state at time 0. The
  `α = 0` countercontrol fails to determine.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7023834853 | Authorization | Provenance; quoted with author and time |
| PR #1421 (A1-REMAINDER) | The list of R1 consumers and the lemma names L1, L2, L3, L10 | Support on `main`: the record is on `main` from `2be3cfad` at the path in the source pin; it frames the question only, and no result here uses its content as a premise |
| #1431 comment 7025214238 (independent review of `229112b8`) | The arguments of Prop. 9 and of the Bernoulli conjugacy in Prop. 5.2; the Kari–Taati theorem numbers | Provenance: the proofs are written out in this record and checked in §9; the Kari–Taati statements are cited from the paper |
| #1055 | Accountable Issue | Provenance |

External literature: Bowen, *Equilibrium States and the Ergodic Theory of Anosov Diffeomorphisms*,
LNM 470 (1975); Burton and Steif, Ergodic Theory Dynam. Systems 14 (1994) 213–235; Csiszár, Ann.
Probab. 3 (1975) 146–158; Georgii, *Gibbs Measures and Phase Transitions* (de Gruyter, 1988), Chs. 6
and 15; Halmos, Bull. Amer. Math. Soc. 49 (1943) 619–624 (attribution of the argument in Lemma 4
(c); not consulted); Hedlund, Math. Systems Theory 3 (1969) 320–375; Kari and Taati, J. Stat.
Phys. 160 (2015) 1198–1243 (arXiv:1311.2319), Theorems 12, 41, 42; Lind and Marcus, *An Introduction
to Symbolic Dynamics and Coding* (CUP, 1995), Chs. 1–4 (shifts, sliding block codes, conjugacy,
entropy); Parry, Trans. Amer. Math. Soc. 112 (1964) 55–66; Richardson, J. Comput. System Sci. 6
(1972) 373–388; Walters, *An Introduction to Ergodic Theory*, GTM 79 (Springer, 1982), Chs. 6 and
8. Textbook statements are cited by chapter; their theorem numbers were not rechecked.

## 11. Verification status and remediation (§A.46 item 4)

Evidence layers: paper proofs (Lemmas 1, 2, 4, 8; Props. 3, 5, 6, 7, 9), citations (Kari–Taati
2015, Burton–Steif 1994, Parry 1964, Georgii, Walters, Bowen), exact finite computations (§9). The
independent review of `229112b8` (#1431 comment 7025214238) verified Lemmas 1, 2, 4 and 8,
Props. 5–7 and C1–C7 as then written. Missing: a delta review of this revision. Accountable Issue:
#1055. Resolution: a delta review recorded on the guiding PR.

**What the delta reviewer must check.**

1. Prop. 3's "role of the rule" paragraph, §6 item 4, §7 and §8: that P-ED is presented as a
   restatement of the uniform posit under (G3)+(G4), not a derivation, and is classed ELABORATING.
2. Prop. 9 (a): the reconstruction radius `|t| ≤ n + 1` and the stationary-entropy step.
3. Prop. 9 (b): the formulas `x_t(0) = (A_t, −A_{t−1})`, `x_{−1−k}(0) = (−A_{k−1}, A_k)`, the
   leading-term argument giving `dim(Γ ∩ R_{Λ_n}) = 2n + 2`, the duality step for the marginal
   entropy, and the translation non-invariance.
4. Lemma 4 (c), (d): the inline mixing proof and the periodic-point argument.
5. Prop. 5.2: the two-plane conjugacy (onto and injective), the Bernoulli identification and
   `h_{β_A}(F) = ∞`, and the claim of mixing of all orders for every `q` with `α` a unit.
6. The μ-O row (Prop. 7.1), the H-BD row, Lemma 8's restriction to window readouts, the typicality
   note moved outside R1, the Kari–Taati citations (Thms. 12, 41, 42, with summable variations),
   and the variational-principle citation in C5.
7. §9 G and H: that the cross-check, the horizon stability and the `α = 0` countercontrols are not
   vacuous.
