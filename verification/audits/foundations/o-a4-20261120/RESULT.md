# O-A4 — the reconstruction chain without A4's finite periodic lattice

**Status.** Writer's paper-only research record. Paper arguments, reading of the cited Lean modules
(none built here) and exact finite computations (`checks/o_a4_checks.py`, §11). No manuscript edit,
no Lean implementation, no premise adoption, no merge. A1 (Main posit ledger item (ii)) and A4 are
unchanged; nothing here is a premise of an established claim. Independent non-author review is
required (§13).

**Authorization.** Owner `amaybaum`, [#1055 comment 7030993647](https://github.com/amaybaum/incompleteness/issues/1055#issuecomment-7030993647),
2026-11-20T05:06:11Z, item 2: "**O-A4: a separate paper-only investigation, run in parallel.** It
rechecks Substratum's and SM's dependencies on the finite periodic lattice, including Theorem 19's
normalizer and the Stage-2 steps that lead to Theorem 23. It classifies each step as surviving
without finiteness, needing weaker assumptions, or holding only for finite models. It makes no
manuscript changes, adopts no premise and implements nothing in Lean." The A1-SCOPE Phase 0 census
is a separate writer's unit and is not done here.

**Goal link (§A.47).** #1055 (A1-SCOPE, residue R4 of A1-REMAINDER). This unit decides, for each
step of the reconstruction chain that uses A4's finite periodic lattice, whether it survives on an
infinite lattice, needs a named weaker assumption, or holds for finite models only.

**Source pin.** `main` at `d5735bedb3958394e3e095a4513d9fb5996d079d`. `Sub:n`, `SM:n`, `GR:n` are
lines of `papers/Substratum.md`, `papers/SM.md`, `papers/GR.md` at the pin. Lean paths are relative
to `verification/lean-mathlib/OIBridge/`. A1-REMAINDER is
`verification/audits/foundations/a1-remainder-20261119/REMAINDER.md`; CENSUS is
`verification/audits/foundations/a1-09-dependency-census/CENSUS.md`; A1-01 is
`verification/audits/foundations/a1-free-p12b-observer/TRACE.md`; P6 is
`verification/audits/foundations/p6-reciprocity-20261116/P6-RECIPROCITY.md`; A1-11 is
`verification/audits/foundations/a1-11-local-gauge-forward/FORWARD-ALGEBRA.md`; R1-INF is
`verification/audits/foundations/r1-inf-20261119/RESULT.md`.

## 1. Controls and productivity test (fixed before the trace)

**Controls.** (K1) Theorem 23's conclusion at its current finite scope stays true: every
classification below concerns an extension of a step, and no finite statement is weakened.
(K2) The kernel predicate `SubstratumInterfaceAudit.A4` (:98) is untouched. (K3)
`SubstratumInterfaceAudit.a1_of_finite` (:109) remains a correct statement about finite sites and
finite alphabets. All three hold: this record changes no file outside its own directory (§13).

**Productivity test (from the brief, adopted unchanged).** The unit is a gem iff it either (i)
shows that the chain to Theorem 23 survives on an infinite lattice with named weaker assumptions,
or (ii) locates a specific finite-model-only step, with its reason or a countermodel. Anything else
is relabelling.

**Classification key.** (a) survives on `ℤ^d` with the same local rule; (b) needs a named weaker
assumption; (c) holds for finite models only, with the place where finiteness is used.

## 2. Setting and named assumptions

**The printed class (F).** Sub:98: the coupling graph is "a finite periodic lattice, the quotient of
a rank-`d` lattice by a finite-index sublattice". With a finite site alphabet this gives A1 through
`a1_of_finite` (A1-REMAINDER R4).

**The infinite classes.** (Z) `ℤ^d` with the same local rule: finite alphabet, finite reading sets,
translation-invariant update. (P∞) a coupling graph with a free cocompact `ℤ^d` action: periodic,
infinite, finite unit cell. (Z) is the case of (P∞) with one site per cell.

**Named assumptions used below.** None is adopted; each is the hypothesis a step needs.

| Name | Content | Where it is satisfied |
|---|---|---|
| A4∞ | A4's translation clause on (Z) or (P∞) instead of a finite quotient; the no-self-input clause unchanged | The kernel predicate `A4` (:98) already has this form: it quantifies over translations of an arbitrary additive group of sites (§8) |
| LF | Finite local data: finite alphabet, finite reading sets, finite point group | (Z), (P∞) and every finite quotient |
| H-μ(φ,Θ) | One normalized probability law invariant under the update φ and the reversal Θ, with product form `u_V ⊗ ν` at the visible window | Uniform Bernoulli law on (Z) for every second-order rule (Lemma U) |
| H-μ(sp) | As H-μ(φ,Θ), and invariant under signed permutations of the six carrier components | Uniform Bernoulli law: signed permutations act site-wise by bijections of the alphabet |
| H-Bloch | The operator in question is translation invariant on (Z) or (P∞) with finite-dimensional cell data, so it fibres over the Brillouin torus into finite matrices | The linear observer-level operators of SM §4.1 |

**Lemma U (uniform Bernoulli law for the second-order rule class).** Let `A` be a finite abelian
group, `F` a finite-range translation-invariant map on `A^{ℤ^d}`, `φ(p, c) = (c, F(c) − p)` on
`Ω = (A×A)^{ℤ^d}`, `Θ(p, c) = (c, p)`, and `β` the uniform product law on `Ω`. Then `φ_*β = β`,
`Θ_*β = β` and `Θφ Θ = φ^{-1}`.

*Proof.* Write `β = β_p ⊗ β_c` with `β_p`, `β_c` Haar on the compact group `A^{ℤ^d}`. For Borel `E`,
`E'`, `β(φ^{-1}(E × E')) = ∫ 1_E(c) β_p({p : F(c) − p ∈ E'}) dβ_c(c) = β_c(E) β_p(E')`, because
`p ↦ F(c) − p` is a translation composed with inversion and Haar measure is invariant under both
(`F` is continuous, so the integrand is measurable). Rectangles generate the product σ-algebra, so
`φ_*β = β`. `Θ` exchanges two identical factors. `ΘφΘ(a, b) = Θ(a, F(a) − b) = (F(a) − b, a) =
φ^{-1}(a, b)`. `□`

No injectivity hypothesis on `F` is needed: the phase map is bijective for every `F` (SM:106). For
first-order bijective cellular automata the corresponding fact is Hedlund's (1969); the second-order
case above is a direct fibre argument. Part B of §11 checks the cylinder marginals exactly.

## 3. The chain as the manuscripts state it

1. **A4** (Sub:98): finite periodic lattice of rank `d`; translation commutation up to gauge; no
   self-input. Together with finite alphabets it re-implies A1 (`a1_of_finite`).
2. **Stage 1** (Sub:121–141): per finite experimental context, a finite reversible realization
   `(S, φ, V)` of the supplied law (S ⇒ D), C1/C3/C4 under M1-T, C2 in its two forms.
3. **Stage 2** (Sub:143–173): (a) dimension via A4's rank and E5–E7 (Sub:157; SM:170–210, with
   Corollary SM:210); (b) wave-equation form (Sub:159; SM:224); (c) link count (SM:366); (d) six-link
   representation and stabilizer (SM:340, :374, :390); (e) staggered tastes and matter (SM:434–456,
   :535–547, :575–603); (f) discrete symmetries (SM:625–651, Theorem 19 at SM:641).
4. **Observer branch used by Stage 2** (SM §4.1): Theorem 1a (SM:242), Lemma 1c (SM:252),
   Corollary 1a (SM:258), Corollary 1b (SM:270), Theorem 1 (SM:278), Proposition 4b (SM:334).
5. **Stage 3** (Sub:175–185): gap equation under H-slope, H-count and GR §8.5(b).
6. **Lemma 23.0 and Theorem 23** (Sub:189–195), with Theorem 24 (Sub:251–268) for representative
   changes.

## 4. Step table

| # | Step (source) | Use of finiteness or periodicity | Class | Argument or citation |
|---|---|---|---|---|
| 1 | A4's finite quotient (Sub:98) | Defines the class; with finite alphabet gives A1 | (b) A4∞ | The kernel predicate is already stated on an arbitrary additive site group (§8). `a1_of_finite` is unaffected (K3); on (Z) A1 fails because the configuration space `(A×A)^{ℤ^d}` is uncountable |
| 2 | Stage 1 representation (Sub:121–141) | Finite S is constructed per finite context, not assumed of nature | (a) | A1-free as a per-window construction (A1-REMAINDER C6). On (Z) a finite window's finite-horizon law is again a finite law, and S ⇒ D represents it. The Stage 1 → Stage 2 identification of that finite dilation with the lattice carrier is open on both classes (A1-01, first row); finiteness does not change it |
| 3 | Stage 1 recurrence-cycle P-indivisibility on a finite representative (Sub:137) | Finite order of a permutation | (c) | Residue R2, outside A4. On (Z) the wave rule has infinite order (R1-INF Lemma 4; §11 part C: ring orders 4 to 22 for `L = 3..12` grow without bound, and `L`-periodic configurations embed each ring) |
| 4 | Stage 2(a): integer `d` as the rank of A4's lattice (Sub:157; SM:202) | "`|B(r)| ∼ r^d` below the system size" | (a) on (Z), (P∞) | On `ℤ^d`, `|B(r)| = Θ(r^d)` for every `r`, so `d` is the growth degree of the graph, a quasi-isometry invariant. On (F) the rank belongs to the presentation: the `L = 4` cubic torus is the 6-cube `Q_6` (§11 D), the simple Cayley graph of `ℤ^6/2ℤ^6` with generators `e_j`, if such quotients are admitted. (Z) removes the size qualifier |
| 5 | Stage 2(a): filters E5–E7 and Corollary SM:210 | "`d`-dimensional periodic lattice" | (b) A4∞ | The filters use `d` and continuum physics only. SM:210's statement says "periodic lattice" without "finite"; on (Z) it reads verbatim. The continuum step stays open on both classes: the cubic hop metric is exactly `ℓ_1` on `ℤ^3` as on every quotient (SM:150 (iv)) |
| 6 | Area-law lemma, mod-`q` part (SM:122) | Uniform state class | (b) H-μ(φ,Θ) | The Markov argument is local; with the uniform product law on (Z), `I(V; V^c)` (supremum over finite subsets of `V^c`) obeys the same bound `|∂V| log_2 q` |
| 7 | Dispersion lemma (SM:126), Theorem 1 (SM:278) | Fourier symbol | (a) | Fourier analysis on `ℤ^d` gives the symbol on the continuous Brillouin torus. On a torus the same symbol is sampled at the dual lattice |
| 8 | Wave-equation form lemma (SM:224) | None: center-free, cubic-isotropic, linear, nearest-neighbour | (a) | Local statement about `f`. A4's independence example (Sub:98, one omitted neighbour at a single site) works on `ℤ^3` |
| 9 | Theorem 1a (SM:242) | "Let `S` be finite" | (a) | The proof uses only `P + Q = I`, `P² = P` and linearity of `U`, so it holds for any linear `U` and idempotent `P` on any vector space of observables, and the commutation with `R_g` passes to `A, B, C, D` unchanged. Supplying a physical `P` needs a law (row 10) |
| 10 | Lemma 1c(i) (SM:252) | Counting measure of Main Lemma 3 | (b) H-μ(φ,Θ) | Conditional expectation commutes with a measure-preserving map that fixes the conditioning variable, for any probability space. On (Z), Lemma U supplies an invariant law; its selection (rather than existence) is R1-INF's (G3)+(G4) |
| 11 | Lemma 1c(ii) (SM:252), pole statement | `det(λ−U) = det(λ−D) det 𝒟(λ)`, cancellation of finite factors | (c) for Koopman compressions; (b) H-Bloch for translation-invariant linear operators | §6.1 countermodel: on rings the visible reduced resolvent has poles at the `ord`-th roots of unity; on `ℤ` it is `1/λ`. Under H-Bloch the determinant argument runs in each finite fibre |
| 12 | Lemma 1c(iii) companion (SM:252) | None beyond the block substitution | (b) H-Bloch | `B = −I, C = I, D = 0` per fibre; the dispersion `cos ω = Â(k)/2` holds at every `k` of the Brillouin torus |
| 13 | Corollary 1a (SM:258) | Translation invariance and `O_h` | (a) on (Z); on (F) needs a lift | Kernel `CubicIsotropy.corollary_1a` is stated for kernels on `Fin 3 → ℤ` with moment conditions (CENSUS §20.3), so it is natively a `ℤ^3` result. On (F) a kernel of range below half the side lifts uniquely to `ℤ^3`; `O_h` must act on the quotient (row 16) |
| 14 | Corollary 1b (SM:270) | Nearest-neighbour stencil normalization `p_0 + 2dp = 1` | (a) | Counts the `2d` stencil directions (CENSUS §17, SM:270); SM:222 already states the carrier as `ℤ^d` |
| 15 | Proposition 4b (SM:334) | "the selected counting measure" | (b) H-μ(sp) | The proof is equivariance plus Schur's lemma for the irreducible signed-permutation representation on `ℝ^6`; the uniform product law is signed-permutation invariant. Scalarity holds wherever the response is defined; its continuation inherits row 11 |
| 16 | `O_h` equivariance used in Theorems 1a, 5, 7, Corollaries 1a, 1b (SM:242–374) | Point group of the coupling graph | (a) on (Z); (b) on (F): `Λ` must be `O_h`-invariant | §7.1: `Aut_0(ℤ^3) = O_h` (order 48). On (F) the vertex stabilizer of the coupling graph is 720 for the `L = 4` torus and 2 for the skew quotient `⟨(5,0,0),(0,5,0),(1,2,5)⟩` (§11 D) |
| 17 | Theorems 5, 6, 7, 7b, 14, 15, 16 (SM:340–390, :575–603) | Finite groups: `O` (order 24), `O_h` (48), Bravais point groups | (a) | Finiteness of the point group only (Averaging, QuarterTurn: CENSUS §20.3). A1-11 records this local algebra as an A1-independent implication on supplied local data. No step averages over the translation group |
| 18 | Staggered structure: Theorems 2, 3, 8, 8b, 10, 12, 13 and SM:539 (SM:286–302, :434–456, :535–547) | Staggered phases, the eight Brillouin corners, the checkerboard | (a) on (Z); (b) on (F): `Λ ⊂ 2ℤ^3` for the corners, `Λ` in the even-sum sublattice for the checkerboard | §7.2: odd tori are not bipartite and carry one corner character of eight; the skew even-sum quotient `⟨(4,0,0),(0,4,0),(1,1,4)⟩` is bipartite and carries four. `ℤ^3` carries all eight |
| 19 | Theorems 17, 18 (SM:625, :633); Proposition 20 (SM:647) | None (local reversal; emergent Lagrangian; a finite Hamiltonian counterexample to an implication) | (a) | Proposition 20's counterexample concerns the emergent visible Hamiltonian, not the lattice carrier |
| 20 | **Theorem 19** (SM:641) | Counting-measure prior; the normalizer `1/|H|` | (b) H-μ(φ,Θ) | §5 |
| 21 | Theorem 21 (SM:651) | Inherits Theorems 18–20 | (b) H-μ(φ,Θ) | Through row 20 only |
| 22 | Stage 3: gap equation, H-count (Sub:175–185; GR:58) | A1 stated in H-count; finite energy shell | (c) as stated; not an A4 use | P7 and A1-REMAINDER R1 own this step. O-A4 does not reclassify it |
| 23 | Lemma 23.0 with Theorem 24(i) (Sub:253) | Uniform hidden prior `1/|C_H|` | (b) H-μ for the population law `T_ij(t)`; (c) for the coherent-channel form | A measure-preserving identical-fibre relabelling preserves `T_ij(t)` (row 10's argument). The coherent form uses the density matrix `𝟙/|C_H|`; on an infinite-dimensional hidden space there is no normalized maximally mixed state, and the Koopman-dilation channel family is A1-REMAINDER's open lemma L6 |
| 24 | Theorem 24(iii) (Sub:257) | Finite decoupled factor | (b) trace-class `σ_A`, unitary `W` | `Tr_A[(U⊗W)(X⊗σ_A)(U⊗W)^†] = UXU^† Tr σ_A` holds in any separable Hilbert space for trace-class `σ_A`; the base channel on `V × H` must already be defined (finite, or L6) |
| 25 | Theorem 24(ii), (iv) (Sub:255, :264) | Alphabet hypothesis; graph comparison | (a) | Neither uses the size of the site set; (iv)'s octahedral restriction is row 16 |
| 26 | Theorem 23 (Sub:193) | Lists A1 among its hypotheses | Mixed | Stage 2 and its observer branch: (a)/(b) under A4∞, LF, H-μ(φ,Θ), H-μ(sp), H-Bloch. Stage 3 (row 22) and the coherent form of Theorem 24(i) (row 23) keep finite-model premises that are not A4's |

## 5. Theorem 19: verdict on the normalizer

**What the normalizer is.** In SM:641 and in `Reciprocity.theorem_19`, "the hidden prior is the
counting measure", and the probability form divides the count equality `N_ij(n) = N_{θj,θi}(n)` by
`|H|` (`Reciprocity.lean`, statement of `theorem_19`; CENSUS §17, SM:641, "equal hidden fibre counts
and the finite normalizer"). The finite normalizer is `1/|H|`, the normalization of the counting
measure on a finite hidden set. No symmetry group, and no normalizer of a subgroup, occurs in the
statement or the proof. The kernel proof assumes `[Fintype H]` only; `V` is not assumed finite.

**Whether finiteness of a symmetry group is used.** No. The group-theoretic content of the chain
uses only the finite point group `O` or `O_h` acting on six local links or eight corners (rows 16–18),
which `ℤ^3` has. No step averages over, counts, or takes the order of the translation group. On
finite quotients the coupling graph's own symmetry can differ from `O_h` (row 16).

**What replaces the counting measure.** P6 proves reciprocal flux under any normalized law invariant
under φ and Θ, with a measurable carrier and no cardinality condition, and the unweighted
conditional form when the root masses are equal; the product specialization `u_V ⊗ ν` with
`θ_H`-invariant `ν` gives the Theorem 19 form. The kernel carries this as
`MeasuredReciprocity.reciprocal_flux` and `common_hidden_law_reciprocity` (family "P6 measured
reciprocity", status kernel-only), with `finite_uniform_reciprocity` recovering `theorem_19`'s count
equality.

**The `ℤ^d` instance.** Lemma U shows that the uniform Bernoulli law satisfies every hypothesis of
`common_hidden_law_reciprocity` for a finite visible window and any second-order rule: the window
marginal is uniform, the off-window law `ν` is the uniform product law, `θ_H` (the site-wise swap)
preserves `ν`, and φ preserves `u_V ⊗ ν`. Hence `T_ij(n) = T_{θj,θi}(n)` for all `n` on `ℤ^d`.
§11 part A computes these transition probabilities exactly on the hidden light cone for `d = 1, 2, 3`,
linear and nonlinear `F`, and finds no violation; the nonlinear `q = 3`, `n = 3` case has 12 distinct
values and 66 ordered pairs with `T_ij ≠ T_ji`, so the `(θj, θi)` form is not vacuous. A ring of side
`L ≥ 2n + 1` reproduces the `ℤ` values exactly; smaller rings give different values (finite-volume
values) and remain reciprocal. The countercontrol (Bernoulli(1/3) hidden law, which is Θ-invariant
but not φ-invariant) breaks reciprocity at `n = 2` for both rules.

**Verdict.** Theorem 19 is class (b): it survives on `ℤ^d` under H-μ(φ,Θ), and on `ℤ^d` that
hypothesis is satisfied by the uniform Bernoulli law for every second-order rule. Which law
nature's state follows is not decided here (P6's Q6; R1-INF).

## 6. Steps that hold for finite models only

### 6.1 Lemma 1c(ii): pole transfer from a finite representative

*Where finiteness is used.* The pole statement factors `det(λ−U) = det(λ−D) det 𝒟(λ)` and cancels
finite factors (SM:254; CENSUS row D18 / C07). On an infinite carrier `U` is a unitary on
`L²(μ)` whose spectrum may be continuous, and no determinant exists.

*Countermodel (§11 part C).* Wave rule, `q = 2`, `α = 1`, visible readout `X = x_0(t)`, `f = (−1)^X`,
`P = E_μ[· | σ(X)]`. On the mean-zero visible line `P U^n P f = m_n f` with
`m_n = E_μ[f · f∘φ^n] ∈ {0, 1}`, since `x_0(n) + x_0(0)` is a linear form over `GF(2)` and `μ` is
uniform. The reduced resolvent on that line is `R(λ) = Σ_n m_n λ^{−n−1}`.
- On the ring `ℤ/L` with counting measure, `φ` has finite order `ord_L` (6, 4, 10, 6, 14, 8, 18, 10,
  22, 12 for `L = 3..12`), and `m_n = 1` exactly when `ord_L | n`. So
  `R_L(λ) = λ^{ord−1}/(λ^{ord} − 1)`: poles at every `ord_L`-th root of unity, residue `1/ord_L`.
- On `ℤ` with the uniform product law, `x_0(n)` contains `x_n(0)` with coefficient `α^n = 1` (only the
  straight path reaches the edge of the cone), so `m_n = 0` for every `n ≥ 1` and `R_∞(λ) = 1/λ`.

Each finite statement is correct, and the finite pole sets do not converge to the infinite one. Each
residue tends to zero, and the poles fill the unit circle. The finite argument therefore transfers
nothing to `ℤ`. On infinite carriers the pole statement needs its own continuation argument. Under
H-Bloch (translation-invariant linear operators with finite cell data) that argument is the finite
one applied in each fibre, which covers the companion realization (iii).

### 6.2 Theorem 24(i), coherent-channel form

The channel `Φ_t(ρ_V) = Tr_H[φ̂^t(ρ_V ⊗ 𝟙/|C_H|)φ̂^{−t}]` uses the normalized maximally mixed state,
which exists only for finite `C_H` (`Tr 𝟙 = ∞` otherwise). The population form survives under H-μ
(row 23). A coherent form on infinite carriers needs a state and a channel family that are not yet
defined (A1-REMAINDER L6).

### 6.3 Stage 1 exact return and Stage 3 H-count

Both are A1 uses outside A4 (rows 3 and 22). They are listed so that the Theorem 23 entry (row 26)
is complete. O-A4 adds only the control that the wave rule has infinite order on `ℤ`.

## 7. Steps that hold on `ℤ^3` and fail on part of the printed finite class

The printed class (F) admits every finite-index sublattice `Λ`. Some Stage 2 inputs need conditions
on `Λ` that Sub:98 does not state, and `ℤ^3` meets them automatically.

### 7.1 The point group of the coupling graph

*`ℤ^3`.* An automorphism fixing `0` permutes the six neighbours and preserves antipodal pairs
(`±e_j` have one common neighbour; perpendicular pairs have two), so it induces some `g ∈ O_h`.
`g^{−1}` composed with it fixes the ball of radius 1 pointwise. A vertex `v` at distance `r + 1 ≥ 2`
is the unique vertex at that distance with its set of neighbours at distance `r`: with two or more
nonzero coordinates, two inner neighbours have only `v` and a vertex at distance `r − 1` in common;
on an axis, `v` is the only vertex at distance `r + 1` with a single inner neighbour. By induction the
composite is the identity, so `Aut_0(ℤ^3) = O_h`. §11 D confirms order 48 on the radius-3 ball.

*Finite quotients (§11 D).* `C_L^3` has vertex stabilizer of order 48 for `L = 3, 5, 6`. For `L = 4`
it has order 720: `C_4^3` is the 6-cube `Q_6`, whose stabilizer acts on the six links 2-transitively,
so the link representation of the graph's own symmetry is `1 ⊕ 5`. The wave rule is a function of
the adjacency, so the dynamics on that carrier commutes with this larger group. For the skew quotient
`⟨(5,0,0),(0,5,0),(1,2,5)⟩` (simple, 6-regular) the stabilizer has order 2, and `O_h` does not act on
the quotient at all, so the hypothesis `[U, R_g] = [P, R_g] = 0` of Theorem 1a has no `O_h`
representation `R_g` there. Theorems 5 and 7 name their group explicitly and remain true as algebra.
On such carriers `O_h` is a symmetry of the local stencil, not of the dynamics.

*Classification.* (a) on (Z). On (F), class (b), with the named condition that `Λ` be `O_h`-invariant
(for example `Lℤ^3`), and, for the graph-intrinsic reading of SM §2.4, a stabilizer equal to `O_h`
(which excludes `L = 4`).

### 7.2 Staggered phases, corners and the checkerboard

The corner characters `(−1)^{η·n}`, `η ∈ {0,1}^3`, are defined on `ℤ^3/Λ` iff `η·b` is even for
every `b ∈ Λ`; all eight exist iff `Λ ⊂ 2ℤ^3`. The checkerboard `(−1)^{n_1+n_2+n_3}` exists iff every
`b ∈ Λ` has even coordinate sum. §11 E: `L = 3, 5` tori are not bipartite and carry one corner;
`L = 4, 6` carry all eight; the bipartite skew quotient `⟨(4,0,0),(0,4,0),(1,1,4)⟩` carries four, so
the four taste pairs of Theorem 8 reduce to two. SM:539's statement that the cubic lattice is
bipartite "as a property of the dynamics (range-1 coupling on a hypercubic graph)" holds on `ℤ^3` and
on quotients with even-sum `Λ`, and fails on odd tori. Class (a) on (Z); class (b) on (F) with
`Λ ⊂ 2ℤ^3`.

## 8. Kernel reading (no build)

- `SubstratumInterfaceAudit.A4` (:98) quantifies over translations by elements of the site group
  `𝒮.ι`, an arbitrary `AddCommGroup`, with the gauge group as a parameter. It has no finiteness
  clause. `Rule` (`SecondOrderLayer.lean`:198) carries finite reading sets `N i : Finset ι` and no
  finiteness of `ι`.
- `waveSubstratum_A2`, `waveSubstratum_A3` (degree `2d`), `waveSubstratum_A4Exact` and
  `waveSubstratum_A5` (:190–216) are stated for every `L : ℕ` with no `[NeZero L]` hypothesis, while
  `waveSubstratum_A1` (:185) requires `[NeZero L] [NeZero q]`. In Mathlib `ZMod 0` is `ℤ` by
  definition, so at `L = 0` these four theorems are statements about the wave rule on `ℤ^d`. The
  kernel therefore already contains the (Z) instance of A2–A5, with A1 not claimed. This is a
  reading of the statements; an elaborated `example` at `L = 0` would confirm it mechanically and is
  not done here (no Lean implementation is authorized).
- `CubicIsotropy` is stated on `Fin 3 → ℤ` (row 13). `Reciprocity.theorem_19` assumes `[Fintype H]`
  only; `MeasuredReciprocity` has the measured form (§5).

## 9. Side finding: SM §4.1's linearity countermodel is finite-ring specific

SM:240 shows that A5 is not implied by A4 and affineness: on a ring of four sites over `ℤ/5`, the
rule `x_i(t+1) = x_{i−1} + x_{i+1} + 1 − x_i(t−1)` has no fixed point, so no time-independent
relabelling makes it linear. The obstruction is the ring sum `0 ≡ L (mod q)`: §11 F finds fixed
points on rings `L = 3..8` exactly when `5 | L`. On `ℤ` the rule has the fixed point
`c_i = −i(i−1)/2 mod 5`, and the site-wise shift by `c` conjugates it to the linear rule. That shift
is a site-wise bijection, the kind of gauge A4 allows. No constant fixed point exists, and a
translation-commuting conjugacy maps translation-invariant fixed points to translation-invariant
fixed points while the linear rule fixes `0`, so no translation-commuting relabelling linearizes the
rule on `ℤ`. Classification: the non-implication holds on (F) as stated. On (Z) it holds for
translation-commuting relabellings and fails for arbitrary ones. It concerns the independence of
A5, not a step of Theorem 23. A finite countermodel remains a countermodel in any class that keeps
finite models, as the disjunctive framing of #1055 does.

## 10. Pressure on the favourable branch, and productivity verdict

**Pressure (§A.31).** The favourable reading is "Stage 2 survives on `ℤ^3`". It is tested at five
points.
(1) Stage 2 inherits its graph from Stage 1. That identification is open on (F) as well (A1-01), so
(Z) neither loses nor gains here.
(2) The observer-kernel bridge to Corollary 1b's inputs is open on (F) (A1-01, row 2b). It stays open.
(3) Measure: on (F) the counting measure comes with A1. On (Z) an invariant law exists (Lemma U), but
selecting it needs translation invariance and the entropy-density functional (R1-INF (G3), (G4)), a
posited selection. The infinite version therefore names a hypothesis where the finite version had a
default. This is the price of the extension.
(4) Continuum and dimension: neutral (row 5).
(5) Lemma 1c(ii) does not survive for Koopman compressions (§6.1). The surviving part needs H-Bloch,
which covers the linear observer-level branch only.

**Verdict.** Gem under both prongs, with the following scope.
- (i) The A4-dependent part of the chain survives on `ℤ^d` (and on (P∞)) under A4∞, LF, H-μ(φ,Θ),
  H-μ(sp) and H-Bloch: Stage 2(a)–(f), SM Theorem 1a, Lemma 1c(i) and (iii), Corollaries 1a and 1b,
  Proposition 4b, Theorem 19 and Corollary SM:210. On `ℤ^d` the uniform Bernoulli law satisfies the
  measure hypotheses for the second-order rule class. Theorem 23 in full does not follow, because
  Stage 3 (H-count) and the coherent form of Theorem 24(i) keep A1 uses that are not A4's.
- (ii) Finite-model-only steps located, with reasons and countermodels: Lemma 1c(ii)'s pole transfer
  (§6.1) and Theorem 24(i)'s coherent prior (§6.2). Conversely, the printed finite class fails some
  Stage 2 inputs on part of its range. `O_h` equivariance needs an `O_h`-invariant `Λ`, and `L = 4`
  enlarges the graph's symmetry to `1 ⊕ 5` on the links (§7.1). The staggered and checkerboard steps
  need `Λ ⊂ 2ℤ^3` (§7.2).

**§A.31 output classification.** NEW: §7 (the printed finite class needs conditions on `Λ` that
`ℤ^3` meets automatically) and §6.1 (finite pole sets do not transfer). POSITIVE: §5 (Theorem 19's
measured form has a `ℤ^d` instance). ELABORATING: §8, §9.

**Assumption-watch markers.** (W1) Every use of `O_h` equivariance, staggered phases or the
checkerboard on a finite representative carries a condition on `Λ`. (W2) Spectral and pole
statements proved on a finite representative do not transfer to infinite volume by a limit in `L`.
(W3) A normalizer `1/|H|` is replaced by the specific invariant law the step uses, never by
"an invariant law" in general. For Theorem 19, that law must be invariant under both φ and Θ.

**§A.29.** Nothing here is adopted. A4∞ is the class on which the steps are checked, not a proposed
replacement premise, and it offers no prediction that separates it from A4 at accessible scales.

## 11. Reproducible computation

Command, from the repository root (stdlib Python 3, about one minute, deterministic):
`python3 -I verification/audits/foundations/o-a4-20261120/checks/o_a4_checks.py`, at the commit that
lands this record. Expected: exit status 0 and the output in
`verification/audits/foundations/o-a4-20261120/checks/o_a4_checks.out`, whose last line is
`ALL CHECKS PASS`. The verdict is the exit status; the printed lines are diagnostics.

| Part | What it checks | Supports |
|---|---|---|
| A | Exact `T_ij(n)` on the hidden light cone of `ℤ^d` under the uniform product law (`d = 1`: `n ≤ 4` at `q = 2`, `n ≤ 3` at `q = 3`, linear `α = 1, 2` and a nonlinear rule; `d = 2`: `n ≤ 2`; `d = 3`: `n = 1`). Ring comparison, and a non-invariant Bernoulli(1/3) countercontrol | §5 |
| B | The image of the uniform law on a cylinder under φ is uniform (fibre sizes constant), for nonlinear and linear `F` | Lemma U |
| C | Ring orders and visible autocorrelations (`L = 3..12`), and the cone-edge coefficient on `ℤ` for `n ≤ 40` | §6.1 |
| D | Vertex stabilizers and their rank on the six links for `C_L^3` (`L = 3..6`), the radius-3 ball of `ℤ^3`, and a skew quotient; the Gray-code isomorphism `C_4^3 ≅ Q_6` | §7.1, row 4 |
| E | Bipartiteness and corner characters on odd, even and skew quotients | §7.2 |
| F | The SM:240 ring countermodel, the ring table, the `ℤ` fixed point and conjugacy | §9 |

Part A is exact over the cone because the phase pair at the origin after `n` steps depends only on
`x(0)` on the `ℓ_1` ball of radius `n` and `x(−1)` on the ball of radius `n − 1`. A ring of side
`L ≥ 2n + 1` embeds that cone injectively, so its counting values equal the `ℤ` values, as the part
checks. The automorphism search in part D enumerates all maps that fix vertex `0` and preserve
distance from it and adjacency to assigned neighbours. It then keeps the maps that preserve every
edge.

## 12. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1055 comment 7030993647 | Authorization | Provenance; quoted with author and time |
| #1055 comment 7030887534 (A1-SCOPE proposal) | The R4/O-A4 framing | Provenance; the record's content does not use it |
| #1055, #1336 | Accountable Issue; related local-algebra unit A1-11 | Provenance |
| P6, A1-01, A1-11, A1-REMAINDER, CENSUS, R1-INF | Rows 2, 3, 10, 17, 20–23; §5; §10 | Support on `main` at the source pin. P6 and the `MeasuredReciprocity` module support §5; the other results are cited as their records scope them. R1-INF is cited only for its standard Lemma 4 and its (G3)/(G4) selection, and the record's own Lemma U does not rely on R1-INF |

External literature: G. A. Hedlund, "Endomorphisms and automorphisms of the shift dynamical system",
Math. Systems Theory 3 (1969) 320–375 (invariance of the uniform law under surjective cellular
automata).

## 13. Verification status and remediation (§A.46 item 4)

- **Evidence level.** Paper arguments (Lemma U, §5–§9), exact finite computations (§11), and reading
  of cited Lean statements (§8). Kernel support exists only where cited: `MeasuredReciprocity` for the
  measured reciprocity theorem. Lemma U, the `ℤ^3` stabilizer argument and the Bloch argument have no
  kernel or independent check.
- **Missing.** Independent non-author review of Lemma U, of §6.1's countermodel and of the §7
  classifications; mechanical confirmation of §8's `L = 0` reading.
- **Controls K1–K3.** `git diff --stat` against the source pin lists only files under
  `verification/audits/foundations/o-a4-20261120/`; no manuscript, Lean or registry file changes.
- **Accountable Issue.** #1055. **Resolution.** A review recorded on the guiding pull request. A1-SCOPE
  Phase 0 and Phase 1 may use the classifications only after that review, and only at the scope
  stated here. In particular Stage 3 and Theorem 24(i)'s coherent form are not covered.
