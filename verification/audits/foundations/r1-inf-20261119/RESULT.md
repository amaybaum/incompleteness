# R1-INF — a default probability law on an infinite configuration space

**Status.** Writer's paper-only research record. Not yet reviewed; an independent non-author
review is required before any use. Paper proofs, standard citations and exact finite computations
(`r1_inf_checks.py`, §9) only. No Lean module, manuscript edit, premise adoption or merge. A1 (Main
posit ledger item (ii)) remains open and unadopted. No statement here is a premise of an
established claim.

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
the doubly stochastic corner (M:60, prong 1; "L3"); the uniform counting of GR:58 (H-count) and of
H-BD (GR:122, proof GR:126).

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
used here is: injective CA on a full site product. It contains the selected update.

**Selected update** (NR-1 §2 (U); M:730 item (xiii); SM:224–228): `A = Z_q^2`, state `(u, v)`,
`F(u, v) = (αSu − v, u)` with `(Sf)(z) = Σ_j f(z+e_j) + f(z−e_j)`. It is a bijective CA for every
`q, α`: `F^{-1}(u, v) = (v, αSv − u)`.

**Notation.** `β_A` is the uniform Bernoulli law on `Ω` (for the selected update, Haar measure of
the compact group `Ω`; NR-1 Lemma 2.1). `Per_L` is the finite set of configurations invariant under
`τ_{L e_j}` for all `j` (the cubic torus). `X_fin ⊂ Ω` is the countable set of finitely supported
configurations (relative to a quiescent symbol `0`). For a translation-invariant law `μ`, `H_n(μ)` is
the Shannon entropy of the marginal of `μ` on the cube `Λ_n = [0, n)^d`, and the **entropy
density** is `h(μ) = lim_k H_{2^k}(μ)/2^{dk}` (the limit exists by Lemma 2's monotonicity; it
agrees with the limit over all cubes, Georgii 1988, Ch. 15, which is not used).

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

For surjective, not necessarily injective, CA the invariance of `β_A` is classical (Hedlund 1969
for `d = 1`; Kari–Taati 2015 state it for surjective CA in general as the trivial-Hamiltonian case
of their theorem); it is not needed here. For the selected update (c) is NR-1 Lemma 2.1, and (b) is
NR-1 Prop. 4.3.

**Lemma 2 (U: uniqueness of maximal entropy density).** Among translation-invariant probability laws
on `Ω`, `h(μ) ≤ log|A|`, with equality iff `μ = β_A`.

*Proof.* `Λ_{2n}` is the disjoint union of `2^d` translates of `Λ_n`; subadditivity of Shannon
entropy and translation invariance give `H_{2n} ≤ 2^d H_n`, so `H_{2^k}/2^{dk}` is nonincreasing in
`k` and bounded by `log|A|`. If its limit is `log|A|`, every term equals `log|A|`, so every dyadic
cube marginal is uniform. Every finite set lies in a translate of a dyadic cube, and marginals of a
uniform law are uniform, so all finite marginals of `μ` are those of `β_A`. Conversely
`h(β_A) = log|A|`. `□`

**Proposition 3 (P-ED: a canonical selection).** Assume

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
gives (a) and (b). (c) A continuous automorphism of a compact abelian group is ergodic for Haar
measure iff the dual automorphism has no nontrivial finite orbit, and an ergodic one is (strongly)
mixing (Halmos 1943; textbook account Walters 1982, §1.6); apply (b). (d) `Fix(F^n)` is a closed
subgroup; if it had positive Haar measure it would be open, hence contain all configurations
vanishing on some finite box, among them nonzero elements of `X_fin`, contradicting (a). A countable
union of null sets is null. `□`

NR-1 does not state mixing: it proves invariance (Lemma 2.1) and that hidden data reach the window
at every time (Prop. 2.3), and it records that the RO-3 mixing unit it mentions is on an unmerged
branch and was not used (NR-1:27–29). Mixing is proved here.

**Proposition 5 (candidate (b): measures of maximal entropy of `F` as a `Z`-action).**
`q` prime, `α ≠ 0` unless stated.

1. *`d = 1`: E+N+U hold.* The map `Φ(u,v) = (x_t(0), x_t(1))_{t∈Z}`, `x_t` the first component of
   `F^t(u,v)`, is a topological conjugacy of `F` onto the full shift on `q²` symbols and a group
   isomorphism. *Proof.* The rule `x_{t+1}(z) + x_{t−1}(z) = α(x_t(z−1) + x_t(z+1))` can be solved
   for `x_t(z+1)` and for `x_t(z−1)` because `α` is invertible; given two full columns, the
   remaining columns are determined, and any pair of column sequences extends to a space-time
   configuration satisfying the rule at every site (each new column enforces the rule on its
   neighbour). `Φ` is a continuous bijection of compact metric spaces commuting with the dynamics.
   `□` Hence `h_top(F) = 2 log q` and the unique measure of maximal entropy is `Φ^{-1}` of the
   uniform Bernoulli law, which is Haar (a group isomorphism carries Haar to Haar). Uniqueness for
   the full shift is Lemma 2 with `d = 1`, since the Kolmogorov–Sinai entropy of a shift-invariant
   law on a full shift equals its entropy density along `Z` (the time-zero partition generates).
   In `d = 1` candidate (b) therefore coincides with P-ED.
2. *`d ≥ 2`: U fails.* Let `Y_p` be the configurations that are `p`-periodic along `e_2` and
   constant along `e_3, …, e_d`; it is closed and `F`-invariant. On `Y_p` the rule reads
   `x_{t+1}(z,k) + x_{t−1}(z,k) = α[x_t(z±1,k) + x_t(z,k±1) + 2(d−2)x_t(z,k)]`, `k ∈ Z_p`, and the
   same column argument (columns now carry `Z_p`) conjugates `F|Y_p` to the full shift on
   `q^{2p}` symbols, so `h_top(F) ≥ h_top(F|Y_p) = 2p log q` for every `p` (monotonicity under
   restriction to a closed invariant set: every `F|Y_p`-invariant law is `F`-invariant, and the
   variational principle, Walters 1982, Ch. 8). So `h_top(F) = ∞`. If some invariant `μ` had
   `h_μ(F) = ∞`, then so would `(μ + δ_0)/2` (affinity of entropy, Walters 1982, Ch. 8); otherwise
   no maximizer exists. Either way no unique measure of maximal entropy exists. (Whether Haar itself
   has infinite entropy is not needed and is not settled here.)
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
`α² = 1`; checked in §9 E). The homomorphism `Ψ: (u,v) ↦ (a,b)` is onto with finite kernel `K`
(given `(a,b)`, `v_{z+2} = v_z + α(b_z − a_{z+1})` with `v_0, v_1` free, then `u` is determined), and
it intertwines `F` with `αR × αL` (`R`, `L` the right and left shifts). Lifting any law `λ` of
`(a,b)` by the uniform law on the fibres `Ψ^{-1}(y)` (cosets of `K`, which `F` and the translations
permute affinely) gives a law that is `F`-invariant iff `λ` is `αR × αL`-invariant, and translation
invariant iff `λ` is. Taking `λ = π_a^{⊗Z} ⊗ π_b^{⊗Z}` with marginals invariant under `x ↦ αx`
gives a family of `F`- and translation-invariant laws with `2(q−1)` free parameters when `α = 1`
(two for `q = 3`, `α = 2`). Their entropy density is `H(π_a) + H(π_b)` (finite fibres do not change
the density), maximal exactly at uniform marginals, i.e. at `β_A`. The mover densities are additive
real-valued conserved quantities of range 2; the rational linear algebra of §9 E finds that, on the
tori tested, the conserved range-2 quantities exceed the trivial ones (constants and coboundaries)
by exactly the mover count. (c) For a nonzero Hamiltonian, the simplex of shift-invariant Gibbs
measures is invariant under a surjective CA iff the CA conserves the Hamiltonian (Kari–Taati 2015,
J. Stat. Phys. 160:1198–1243; stated here at the level of the paper's abstract, for the class of
Hamiltonians treated there; theorem number not rechecked). So (E) for constrained Gibbs selection
is a question about conservation laws of `F`, and where conservation laws exist, (U) needs the
conserved densities, which are free parameters.

*Consequence for the selected update in `d = 1`.* "Maximal entropy at fixed conserved densities" is a
`2(q−1)`-parameter generalized Gibbs family; "maximal entropy among invariant laws" without
constraint is P-ED. Whether the selected update has real-valued additive conserved quantities for
`d ≥ 2` is not determined here. SM:292 records that the exact linear rule conserves its quadratic
energy only modulo `q`, and that neither that fact nor the rounded rule supplies "the required real
positive-definite conserved energy"; the movers are not such an energy and are specific to `d = 1`,
so this record makes no finding against SM:292.

**Proposition 7 (candidate (e) and the orbit-level measures).** `q` prime, `α ≠ 0`, `β_A` Haar.

1. *μ-O.* For Haar-almost every microstate the orbit is infinite (Lemma 4 (d)) and its empirical
   measures `(1/n)Σ_{t<n} δ_{F^t x}` converge weak-* to Haar (ergodicity, Lemma 4 (c), and
   Birkhoff's theorem applied to a countable dense set of continuous functions). The orbit-level law
   of a typical microstate is Haar itself, and the orbit capacity `log₂ p` of M:60 has no finite
   value. This supplies A1-REMAINDER's lemma L2 for this rule in the form "the ergodic component of
   a typical point is Haar".
2. *μ-R collapses.* For a record cylinder `[P]` of positive measure, the union of the orbits
   meeting it, `E = ∪_{t∈Z} F^{-t}[P]`, is `F`-invariant with `β_A(E) ≥ β_A([P]) > 0`, so
   `β_A(E) = 1` by ergodicity. "Uniform on the record-compatible orbits" is Haar: at the orbit level
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
|V| μ(π = b) = |V| ν(b) = 1`, by invariance. `□` Under P-ED, `β_A = Unif(V) ⊗ β_A|_H` for every
window readout, so the doubly stochastic corner of M3 and the premise of prong 1 at M:60 ("the
marginal of a bijection under the uniform prior is doubly stochastic") hold for every injective CA
on a full site product, with no finiteness of the carrier. The §9 C countercontrol shows the
conclusion failing under the non-invariant product `Unif(V) ⊗ δ_0`.

## 4. E/N/U table

| Candidate | (E) existence | (N) normalization | (U) selection | Scope |
|---|---|---|---|---|
| (a) product Haar / uniform Bernoulli `β_A` | Yes for every injective CA on a full product (Lemma 1); selected update NR-1 Lemma 2.1 | Yes | Not by itself: declared, it is H-μ. Selected by P-ED or (d) | Full product carrier |
| (b) measure of maximal entropy of `F` (Z-action), potential 0 | `d = 1`: yes. `d ≥ 2`: `h_top = ∞`, maximizer may not exist | Yes when it exists | `d = 1`, `q` prime, `α ≠ 0`: yes, Haar (Prop. 5.1). `d ≥ 2`: no (5.2). `F^N = id` cases: no, every law (5.3) | Selected update |
| (b′) **P-ED**: maximal entropy density among laws invariant under `F` and translations | Yes (Lemma 1) | Yes | Yes, `β_A` (Lemma 2, Prop. 3) | (G1)–(G4) |
| (c) Gibbs/DLR, zero interaction | Yes | Yes | Yes, `β_A` (= P-ED) | Full product |
| (c) Gibbs/DLR, nonzero interaction | Iff `F` conserves it (Kari–Taati 2015) | Yes | No in general: conserved densities are free parameters (Prop. 6, `d = 1`); phase coexistence (countermodel C5) | — |
| (d) cylinder limit of counting laws on `Per_L` | Yes (Lemma 1) | Yes | Yes: the limit is unique and is `β_A` | Injective CA on full product |
| (e) maximal entropy compatible with records | Needs a reference law | — | Ill-posed without reference; with `β_A` it is conditioning (a preparation), and at the orbit level it collapses to `β_A` (Prop. 7) | — |

## 5. Countermodels

| # | Target | Countermodel | Status |
|---|---|---|---|
| C1 | E fails (no invariant probability) | The selected update (`q` prime, `α ≠ 0`) restricted to the countable carrier `X_fin \ {0}`: a bijection with no finite orbit (Lemma 4 (a)); an invariant probability on a countable set is constant on orbits, hence zero. The counting measure on `X_fin` is invariant, σ-finite and infinite (N fails) | Proved |
| C2 | E fails, infinite local alphabet | `F(x)(z) = x(z) + 1` on `Z^{Z^d}`: local and bijective; an invariant probability would have a site marginal that is a translation-invariant probability on `Z` | Proved |
| C3 | E on compact carriers | Not a countermodel: every continuous map of a compact metrizable space has an invariant Borel probability (Krylov–Bogolyubov; Walters 1982, Ch. 6). E fails only off compactness (C1, C2) | Cited |
| C4 | Several measures of maximal entropy | (i) `F^N = id` members of the OI form (`q = 4`, `α = 2`; `α = 0`): every invariant law (Prop. 5.3). (ii) Selected update, `d ≥ 2`: `h_top = ∞`, no unique maximizer (Prop. 5.2). (iii) Constrained carrier: strongly irreducible `Z²` subshifts of finite type with two ergodic measures of maximal entropy (Burton–Steif 1994, ETDS 14:213–235); the identity CA on such a carrier makes both P-ED maximizers admissible, so (G1) is load-bearing. In `d = 1` irreducible SFTs have a unique one (Parry 1964) | Proved / cited |
| C5 | U fails for constrained (Gibbs) selection | (i) Selected update `d = 1`, `α² = 1`: generalized Gibbs family (Prop. 6). (ii) `F` = a lattice translation or the identity (injective CA): every translation-invariant law is admissible, so maximal entropy density at fixed nearest-neighbour Ising energy density in `d = 2` below the critical temperature has the two extremal phases (Georgii 1988, Ch. 6) | Proved / cited |
| C6 | U fails without translation invariance (G3) | `F = id`: the law `δ_a` at the origin `⊗ β_A` elsewhere is `F`-invariant, has entropy density `log|A|` along centred cubes, and differs from `β_A`. For the selected update, U without (G3) is open | Proved |
| C7 | Product law not invariant | (i) Selected update `q = 2`, `α = 1`, with `Bern(1/4)` for `u` and `v`: `P(u'(0) = 1) = 7/16` (§9 D). (ii) The AND rule (not surjective, outside the class): `β_A` is not invariant (`1/4` vs `1/2`). (iii) A non-local bijection: exchange the clopen sets `[1]` and `[00]` of `{0,1}^Z` by a homeomorphism and fix the rest; measurable involution, not `β_A`-preserving (`1/2` vs `1/4`). (ii) and (iii) show surjectivity and locality are load-bearing for Lemma 1 | Proved |

## 6. Pressure on the favourable branch (P-ED), and what it restores

1. *(G3) is a new hypothesis.* Lemma 3 of Main needs no translation invariance on a finite carrier
   (where `μ_L` is translation invariant automatically). In infinite volume U fails without it (C6).
   (G3) is a homogeneity posit on the admissible laws, not a finiteness posit; it is not derived from
   the Definition or the axioms.
2. *(G1) is load-bearing.* With local constraints the analogous selection can be non-unique (C4
   (iii)). OI's site factorization (M:730 (viii), (xiii)) gives a full product.
3. *The literal counting measure survives only without normalization.* On `X_fin` it is invariant
   and infinite (C1); on `Ω` it is not σ-finite. The normalized continuation is `β_A`, which gives
   `X_fin` measure zero.
4. *Is it H-μ relabelled?* No in logical role: H-μ declares a law, P-ED selects one with no free
   parameter under (G1)–(G4). Yes in observability: P-ED's finite-window content (i.i.d. uniform
   substratum frequencies by the strong law of large numbers; temporal decorrelation by Lemma 4 (c))
   equals that of the torus counting law on every window and horizon inside the light cone (NR-1
   Prop. 4.1), and substratum cells are not observed (M:706 states that `ε` is stipulated). It does
   not discriminate P-ED from A1 at accessible scales.

**R1 consumers under P-ED.**

| Consumer | Restored? | Basis |
|---|---|---|
| Lemma 3 selection clause (M:54, M:58); μ-G | Yes, in entropy-density form, under (G1)–(G4) | Prop. 3 |
| Doubly stochastic corner (M3, L3); prong 1 premise (M:60) | Yes, any injective CA, any window readout | Lemma 8 |
| μ-O (L2) | Yes for the selected update, `q` prime, `α ≠ 0`: Haar | Prop. 7.1 |
| μ-R; orbit selection "compatible with the observer's records" (M:60; M:730 (iv)) | Collapses to Haar; the orbit-level selection is vacuous | Prop. 7.2 |
| Typicality | Substratum level only: spatial frequencies (strong law, `β_A` i.i.d.), temporal averages (ergodic theorem). Not M:762's canonical typicality (quantum, finite-dimensional) | Lemma 4 (c) |
| GR:58 H-count | No: P-ED is the unconstrained (`β = 0`) law; no shell and no temperature. A shell analogue needs a real conserved energy and a density, which are free parameters (Prop. 6) | — |
| P7B node 6.3 (invariant shell law, coupled case) | Not closed; in `d = 1`, `α² = 1`, invariant laws at fixed mover densities exist (Prop. 6), which are not GR's energy shell | — |
| H-BD (GR:122, proof GR:126; L10) | Partly: P-ED supplies a normalized deep law; the proof's counting step (injectivity makes `D` components distinct, then a fraction bound) has no measure-theoretic transfer here | — |

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
- *Independent consequence beyond replacing A1.* With the infinite lattice and the selected update
  (`q` prime, `α ≠ 0`), P-ED fixes NR-1's hidden prior (Haar) without positing it. NR-1's verdicts
  then follow: no near-return, no rigidity (Prop. 2.3), and for lattice-convex windows no revival
  and P-divisibility at every horizon (Thm. 3.3). This is a theoretical consequence that removes
  the A1-free recovery of recurrence-scale P-indivisibility for that class. It is not an empirical
  prediction.
- *Empirical content.* None that discriminates it from A1 at accessible scales (§6 item 4).
- *Variability.* No free parameter under (G1)–(G4). The variants (local constraints, conserved
  densities, potentials, non-translation-invariant laws) each add parameters or lose uniqueness
  (C4–C6, Prop. 5.4, Prop. 6) and are excluded as fit-anything.
- *Verdict.* P-ED is hard to vary but supplies no independent empirical prediction, so it does not
  meet §A.29's prediction clause for a Layer-0 revision. It is recorded as a mathematical selection
  result, not a proposed premise.

## 8. Productivity verdict and classification

**Gem under (i), scoped.** P-ED satisfies E+N+U for the class of injective CA on a full finite-alphabet
site product in any dimension, which contains the selected update for every `q, α`, under the
explicit hypotheses (G1)–(G4). It restores Lemma 3's selection role in entropy-density form, the
doubly stochastic corner (L3), and μ-O for the selected update with `q` prime, `α ≠ 0`. It does not
restore GR:58, H-BD's counting step or canonical typicality. **(ii) also holds for the other
readings:** maximal entropy of `F` as a dynamical system fails U for `d ≥ 2` and for zero-entropy
members of the OI form; constrained (Gibbs) selection fails U whenever conserved densities exist
(the selected update in `d = 1`); dropping (G3) or (G1) loses U.

§A.31 classes: **NEW** — the entropy-density form of L1 with (G3) as its added hypothesis; the
`d ≥ 2` failure of the dynamical-entropy reading for the selected update; the `d = 1` mover
conservation laws and generalized Gibbs family of the selected update; the collapse of orbit-level
record selection (μ-R) to Haar. **POSITIVE** — L3 is immediate from invariance (Lemma 8), as the
A1-REMAINDER record expected.

**Assumption-watch markers.** (1) Any infinite-volume reading of "the maximal-entropy invariant
measure" must state its admissible symmetry class (G3) and its entropy functional (G4); the two
natural readings (entropy density, dynamical entropy) differ for `d ≥ 2`. (2) M:60's orbit-level
"selection among orbits … compatible with the observer's records" uses finite orbits; under an
ergodic infinite-volume law it selects nothing. (3) The parameters `(q, α)` decide both the mixing
property (Lemma 4) and the zero-entropy branch (Prop. 5.3), extending NR-1's node 5 marker.

**Open.** U without (G3) for the selected update; real-valued conserved quantities of the selected
update for `d ≥ 2`; composite `q` with unit `α` (Lemma 4 uses a field); whether Haar has infinite
dynamical entropy for `d ≥ 2`; a measure-theoretic H-BD (L10); the GR:58 shell in infinite volume.

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
```

**What each part supports.** A: both halves of the `d = 1` conjugacy (Prop. 5.1) at `T = 6`
(finite instances of the proof's column argument), with the `α = 0` countercontrol, where the window
is uninformative. B: illustration only of Prop. 5.2; the proof is the `Y_p` argument, and finite
ranks prove no limit. C: Lemma 8 by brute force over the hidden light cone, using no linearity, and
its countercontrol. D: C7 (i), (ii). E: controls detect the known conserved quantities (all
functions for the identity; particle number for rule 184); the excess dimensions for the selected
update (2, 4, 2) equal the mover counts of Prop. 6 (`2(q−1)` for `α = 1`; one even nonconstant
function per mover for `q = 3`, `α = 2`); the identification is checked on random tori. Torus
equations are necessary conditions for conservation on `Z`, so they bound the conserved space from
above; the movers bound it from below. F: illustration of Lemma 4 (a), whose proof is algebraic.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7023834853 | Authorization | Provenance; quoted with author and time |
| PR #1421 (A1-REMAINDER) | The list of R1 consumers and the lemma names L1, L2, L3, L10 | Support on `main`: the record is on `main` from `2be3cfad` at the path in the source pin; it frames the question only, and no result here uses its content as a premise |
| #1055 | Accountable Issue | Provenance |

External literature: Bowen, *Equilibrium States and the Ergodic Theory of Anosov Diffeomorphisms*,
LNM 470 (1975); Burton and Steif, Ergodic Theory Dynam. Systems 14 (1994) 213–235; Csiszár, Ann.
Probab. 3 (1975) 146–158; Georgii, *Gibbs Measures and Phase Transitions* (de Gruyter, 1988), Chs. 6
and 15; Halmos, Bull. Amer. Math. Soc. 49 (1943) 619–624; Hedlund, Math. Systems Theory 3 (1969)
320–375; Kari and Taati, J. Stat. Phys. 160 (2015) 1198–1243 (arXiv:1311.2319); Lind and Marcus,
*An Introduction to Symbolic Dynamics and Coding* (CUP, 1995), Chs. 1–4 (shifts, sliding block
codes, conjugacy, entropy); Parry, Trans. Amer. Math. Soc. 112 (1964) 55–66; Walters, *An
Introduction to Ergodic Theory*, GTM 79 (Springer, 1982), §1.6 and Chs. 6, 8. Textbook statements
are cited by chapter; their theorem numbers were not rechecked.

## 11. Verification status and remediation (§A.46 item 4)

Evidence layers: paper proofs (Lemmas 1, 2, 4, 8; Props. 3, 5, 6, 7), citations (Halmos 1943,
Kari–Taati 2015, Burton–Steif 1994, Parry 1964, Georgii, Walters), exact finite computations (§9).
Missing: an independent non-author review. Accountable Issue: #1055. Resolution: a review that
checks the items below and records its verdict on the guiding PR.

**What the reviewer must check.**

1. Lemma 1 (c): the cylinder identity at `L` larger than the side of `B + N`, and that injectivity,
   not bijectivity on `Ω`, is all that is used.
2. Lemma 2: the dyadic monotonicity and that it alone yields uniqueness without the full-cube limit.
3. Lemma 4: the dual matrix, the characteristic polynomial, the use of "`F_q` is algebraically
   closed in `F_q(x_1, …, x_d)`", and that Halmos 1943 states ergodicity iff no nontrivial finite
   dual orbit, and ergodic ⇒ mixing, for continuous automorphisms of compact abelian groups.
4. Prop. 5.1 and 5.2: the column-reconstruction conjugacies (onto and injective), including the
   `Y_p` form with `k ∈ Z_p`, and the affinity argument for non-uniqueness.
5. Prop. 6: the mover identities, the kernel of `Ψ`, the fibre-uniform lift, and the entropy-density
   equality across finite fibres; that the Kari–Taati citation is used only at abstract level.
6. Prop. 7.2: that the saturation of a positive-measure cylinder has full measure under ergodicity,
   and the reading that M:60's orbit-level selection becomes vacuous.
7. That (G3) is correctly flagged as a hypothesis absent from Main, and that C6 shows it is
   load-bearing for the class.
8. §7: that the NR-1 consequence is correctly scoped (prime `q`, `α ≠ 0`, lattice-convex windows,
   window readout) and that no empirical discrimination from A1 is claimed.
9. That the script's controls are not vacuous (§9, "What each part supports").
