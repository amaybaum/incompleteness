# GAUGE-A1 trace, r1: where total finiteness (A1) enters the Substratum lattice and gauge-structure derivation

**Status.** Paper-only, read-only and unreviewed. No repository file was edited, committed or pushed. No GitHub record was written. No Lean build, simulation or computation was run. No premise is adopted, no status is changed and no recovery credit is given: every "candidate" below is a candidate only. All `file:line` references are to `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Abbreviations: Sub = `papers/Substratum.md`, SM = `papers/SM.md`, Struct = `papers/Structure.md`, ch02 = `book/ch02-substratum.md`. **[IR]** marks a reading made here that is not stated on `main`. "Not written" means that the step the label implies does not appear in the text.

**Owner request (2026-11-15).** "We should also investigate the Substratum discussion about gauge representation. I think this was the part of the original A1 argument." This trace fills the gap that audit r9 records under AM-11 ("Stages 2(a)–(e) and 3 are not traced for A1") and that EF-1 r7 N3.8 leaves open ("the theorems of the SM paper that Stage 2 (b)–(e) cite were not traced").

**Classes.** (V): only a finite visible or boundary sector is used (Lemma 1, or E3's bound on `C_V × C_B`). (L): a finite periodic lattice is used as a model class. (T): total finiteness of `S` is genuinely used, for example through counting measure, recurrence, finite cardinality or a finite count. (N): no use, meaning A1 is listed or nearby but nothing consumes it.

***

## 0. Summary

**Finding.** No written step of the gauge-group selection, Stage 2 (a)–(e), uses total finiteness of `S`. Where the finite lattice appears, it is a model class. It constrains the argument and does not support it: the growth exponent is defined only "below the system size" (SM:202), and the bipartite and staggered structure needs even torus sides [IR]. Both steps run cleanly on `Z^d`, which is the lattice SM §4 already uses: "a $d$-dimensional hypercubic coupling graph $\Lambda=\mathbb Z^d$" (SM:222). The gauge derivation is carried out on the observer-level complex lift. The kernel proves that this carrier is outside A1 (`cx3b_complex_not_A1`, `A6Instantiation.lean:512`).

A1 is genuinely used (T) in five places in the reconstruction:

1. the recurrence-cycle sentence of Stage 1 (Sub:137);
2. the C2 necessity forms (Sub:129);
3. Theorem 19's reciprocal counts, used in Stage 2(f) (SM:641–643);
4. the shell counting behind Stage 3 (GR:58, :70);
5. the selected counting measure in Proposition 4b (SM:334). Proposition 4b discharges only the kinetic clause of H-cust, a premise that Theorem 5 states anyway.

The "original A1 argument" therefore does not sit in the gauge representation. It sits in the discrete-symmetry step (f), in Stage 3, and in Stage 1's recurrence and C2 clauses. The gauge selection depends on other conditions, listed in §3, and none of them is relaxed by retiring A1. The open coarse-graining bridge `φ → L_obs` (SM:232) is load-bearing, with or without A1.

| Stage / result | Use | Replacement candidate (candidate only) | Gap |
|---|---|---|---|
| Stage 1: constructed triple, C1, C3, C4 (Sub:125–139) | V | Main §3.4 per-horizon realization; Main:60 says it needs only Lemma 1 | none for the constructed realization |
| Stage 1: recurrence-cycle sentence (Sub:137) | T | none; EF-1 r7 N3.1: not carried by a fixed-horizon form | stays a finite-model statement; Stages 2–3 do not consume it |
| Stage 1: C2 necessity forms (Sub:129, :137) | T (uniform-prior marginal) | P5a, P5b (audit AM-21; not written) | reference prior `π_H` is a Q6-type premise |
| Stage 1 → Stage 2 interface (Sub:157, "inherited from Stage 1") | not written | — | the coupling graph comes from A3, A4, (viii) and (x), not from the Stage 1 object |
| 2(a) dimension | L | the same argument on the rank-`d` lattice (`Z^d`) [IR]; unit U-A4 (changemap, 2b) | none from A1; the continuum conditions of SM §3.1–§3.2 remain |
| 2(b) wave-equation form, α = 1/d | N (form lemma); L/T labels in the supporting Theorem 1a and Lemma 1c | SM §4.1 is already stated on `Z^d` | Lemma 1c's counting measure and finite-dimensional resolvent identity are not consumed by the form selection |
| 2(c) K = 6 | N | — | H-link with m = 1 (premise) |
| 2(d) (3,2,1), Theorem 7 | N (kernel `theorem_7`, link geometry only) | — | — |
| 2(d) stabilizer U(3)×U(2)×U(1), Theorem 5 | N (complex carrier, outside A1 by kernel) | — | H-link, H-cust, equivariant generic Σ |
| H-cust kinetic clause via Prop. 4b | T (selected counting measure) | P13 (audit) with the uniform product family (`uniform_family_consistent`, on `main`) | resummed response on an infinite carrier not written; prior is a premise (Q6) |
| SU reduction and hypercharges (Thms 14–15, Props 14a, 15a) | N | — | charged matter action, family pattern, Y_Q ≠ 0 branch |
| Local promotion, A6 | N (kernel `a6cov_all`, `as1_leap_covariant`, polymorphic in sites) | — | — |
| Theorem 7b, simple-cubic selection | N | — | converse direction is a paper argument; no kernel witness found |
| 2(e) tastes and chirality (Thms 8–13) | L (torus needs even sides [IR]) / N | `Z^d` | H-spin', H-χ', light-spectrum selection |
| 2(f) Theorems 17, 18, 20, 21 | N | — | H-top, H-det |
| 2(f) Theorem 19, reciprocity | T (counting prior, divide by `|C_H|`) | (α) P6 (audit AM-30); (β) torus `theorem_19` plus EF-1 r7 N1.8 per horizon [IR, not checked] | product prior is a premise (Q6); T-invariance on the infinite carrier (Q5) |
| Stage 3, ħ relation | T (GR:58, :70 shell counting) | P7 (audit AM-22; not written) | microreversibility on the boundary shell when the deep sector couples; EF-1 N3.7: not carried |
| Lemma 23.0 | N for the Stage-2 invariants (its proof does not list A1); T through Stage 3 | — | as Stage 3 |
| Theorem 23 | union of the rows above | P12 (audit) | as rows above |
| Thm 24 (i) | T as stated (uniform prior on a finite `C_H` of a realization) | P11 (audit; routine) | Q6 for any reading about nature |
| Thm 24 (ii) | N | — | alphabet-size hypothesis |
| Thm 24 (iii) | N on the original carrier; the finite factor is the statement's own scope | EF-1 r7 Lemma PM (b), (c), draft | equal patch marginals (D1) |
| Thm 24 (iv) | V and N | — | the gauge content uses the local point group |
| Corollary (i), (ii) | V | — | sentence "interpretive premise of A1" (U-23) |
| Corollary (iii) | T for its recurrence clause only | — | not consumed by the gauge selection |
| Prop. 9.5 (Struct:646) | T inherited from Thm 24 (i) as stated | P11 | as Thm 24 (i) |

***

## 1. The trace, stage by stage

### 1.1 Stage 1 (Sub:121–141)

- **A1 as an input (Sub:123).** A1 is listed. Its consumers inside Stage 1 are the next three bullets.
- **Output "with $S$ finite" (Sub:125); derivation (Sub:137).** The triple is a constructed realization on "an enlarged finite space $\mathcal{C}_V \times \mathcal{C}_H$", built by Main's process dilation and response tables. Main:60 states that the equivalence of §3.4, "in which a finite hidden space is constructed, not assumed", uses only Lemma 1. **(V).** C1, C4 (Sub:129) and C3 ("$\log_2|\mathcal{C}_H| \geq I^*$", Sub:137) follow per horizon. C3 holds for every faithful realization and is vacuous for an infinite hidden sector (audit AM-31). (C2-structural) is supplied by reversibility, which is A2, a model condition under Q5 (a).
- **Recurrence-cycle sentence (Sub:137).** "[Main §2.3] then proves that on a fixed finite representative a non-permutation rooted map … forces indivisibility somewhere in the recurrence cycle." **(T).** It is not carried by any fixed-horizon form (EF-1 r7 N3.1). Nothing in Stages 2–3 cites it.
- **C2 necessity (Sub:129).** The forms are stated for the uniform-prior bijection marginal (audit AM-21). **(T)** through the prior. Candidates: P5a (any reference prior) and P5b (the slow-bath form, gated on Q6). Neither is written.
- **Stage-1 gauge statement (Sub:139).** It concerns the "finite channel/dilation datum actually used". This finite datum is constructed. **(V).**

### 1.2 The Stage 1 → Stage 2 interface (not written)

Sub:145 lists "Stage 1 output" among the inputs, and Sub:157 begins "The coupling graph inherited from Stage 1". Stage 1's object is `C_V × C_H` with no site factorization, so it has no coupling graph in the sense of SM §2.4. The graph that Stage 2 actually uses comes from site factorization (ledger item (viii)), A3, A4's lattice and the nearest-neighbour premise (x). No step identifies the Stage 1 dilation with the Stage 2 lattice model. Theorem 23 is therefore a conjunction of two separately specified objects. A1 is not involved in that identification. Retiring A1 neither creates nor closes this gap.

### 1.3 Stage 2 (Sub:143–173)

**(a) Dimension (Sub:157; SM §3.2, SM:170–214).**

- The finiteness used is A4's "finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice" (Sub:98, :157). **(L).**
- On the finite quotient, the growth law holds only "$|B(r)| \sim r^d$ below the system size" (SM:202). On the rank-`d` lattice itself, it holds at every scale.
- The three filters are continuum physics: the Weyl tensor, Ehrenfest/Tangherlini, and the d-dimensional Friedmann ratio. None of them uses `|S|`.
- **Runs on `Z^d` with the same local rule:** yes [IR]. The integer `d` is the rank of the translation lattice. Gromov's theorem is not invoked (SM:208).
- The changemap keeps Sub:98 and :157 unchanged (U-09a). The restatement for an infinite lattice is unit U-A4 (U-09b, stage 2b).

**(b) Wave equation (Sub:159; SM:224–228).**

- The form lemma's proof is local. It uses `f` as a function of the `2d` neighbours, symmetry under lattice symmetries, and additivity. **(N).**
- The coefficient remark (SM:230) is Fourier analysis of the real lift on `Z^d`, with stability at α ≤ 1/d and gaplessness at α = 1/d. **(N).**
- SM §4.1's supporting results carry finiteness labels:
  - Theorem 1a has "Let $S$ be finite" (SM:242), but its proof is the P/Q block algebra and does not use the hypothesis [IR].
  - Lemma 1c uses "the counting measure of [Main] Lemma 3" and a finite-dimensional determinant/Schur identity (SM:252–258). That is (T) through the measure.
- The Stage 2(b) selection cites neither result. They support observer-level isotropy (Corollary 1a, kernel `OIBridge/CubicIsotropy.lean`, no `|S|`) and the normalized branch (Corollary 1b, conditional on observer-level centre-freedom).
- Conditions that remain without A1: the nearest-neighbour premise (SM:226), center independence, linearity, and the open bridge "the map $\varphi\to L_{\rm obs}\to\Delta_g$ is not proved anywhere in this framework" (SM:232).

**(c) K = 6 (Sub:161; SM:360–366).** Theorem 6 is "Under H-link, $K=2dm$". No use is made of finiteness. **(N).** The step is conditional on H-link and its single-copy clause m = 1.

**(d) Gauge group (Sub:163; SM:340, :374–416, :575–610).**

- *Theorem 7.* The six signed links decompose under O as `T₁ ⊕ E ⊕ A₁`. The kernel `theorem_7` (`LinkDecomposition.lean:479`) is built "on the links themselves", on functions on `Fin 3 × Bool`, with no lattice size and no `S`. **(N).**
- *Theorem 5.* The stabilizer of a generic O-equivariant Σ in U(6) is U(3)×U(2)×U(1). This is Schur's lemma plus a unitary stabilizer, carried out on the observer-level six-component complex field, "not the $\mathbb{Z}/q\mathbb{Z}$ alphabet of the substratum" (SM:312). The kernel records that this carrier "is not a substratum satisfying A1 … finiteness is the first of the interface's axioms and the complex carrier is infinite" (`A6Instantiation.lean:498–524`). **(N).** The conditions are H-link (m = 1), H-cust, O-equivariance of Σ (the condensate clause, "a hypothesis on the solution", SM §3.1), and genericity (distinct block values).
- *H-cust kinetic clause, Proposition 4b (SM:334–336).*
  - The proposition says "take the selected counting measure". The proof uses a product of six identical systems, a product measure and an equivariant conditional expectation, and from these derives that the response is `I_6 ⊗` scalar. **(T)** through the measure of Main Lemma 3.
  - Candidate: P13 (audit AM-4.4), "the memory-resummed response is defined for a normalized signed-permutation-equivariant product measure". On `main`, an A1-free uniform product family exists on any site type: `uniform_family_consistent` (`RegionTower.lean:447`) and `uniformFamily_isStateFamily` (`QuasilocalAlgebra.lean:887`).
  - Gap: the resummed response on an infinite carrier is not written, because Lemma 1c (ii) is a finite-dimensional identity. A probability law for nature is a named premise under Q6 (a)+(e).
  - Fallback with no new premise: H-cust's kinetic clause stays a premise, as Theorem 5 already states it. Changemap S-15 keeps Proposition 4b as a finite-model statement.
- *Amplitude-scale gauge.* It "removes only the common overall phase" (Sub:163). It is an operational premise (Sub:272). **(N).**
- *Reduction to SU(3)×SU(2)×U(1) and hypercharges.* Theorem 14, Proposition 14a, Theorem 15 and Proposition 15a are group algebra and the anomaly conditions. **(N).** The conditions are a specified charged matter action, the five-representation family pattern with family-universal charges, the Y_Q ≠ 0 branch and the electromagnetic identification.
- *Local promotion by A6.*
  - The kernel `a6cov_all` and `as1_leap_covariant` are stated for any site type `ι` with `Finset` neighbourhoods and any additive alphabet. `cx3a_complex_axioms` holds A2, A3, A5 and A4Exact at the complex carrier. **(N).**
  - The kernel interface also has `a2_every_substratum`: bijectivity is automatic for the second-order form, with no finiteness (`SubstratumInterfaceAudit.lean:106`).
- *Theorem 7b (simple-cubic selection; SM:390–416).* The argument is a point-group irrep census on nearest-neighbour links. **(N).** Its two directions are separate (§A.34):
  - forward, SC ⇒ U(3)×U(2)×U(1) for a generic equivariant Σ: Theorems 7 and 5, under H-link and H-cust;
  - converse, "SM group ⇒ SC among the 14 Bravais lattices under the commutant construction": a paper argument (crystallographic irrep dimensions, the BCC/FCC tables, the uniqueness of `S_4` among finite rotation groups with both a genuine 2-dimensional and a 3-dimensional irrep). A search for "Bravais" in `OIBridge/` found no kernel witness.
  - Sub:203 already says that the inference here "runs from observed physics back to the commitment".

**(e) Matter content (Sub:165; SM:430–571).**

- Theorems 8 and 8b (BZ corners), 9, 10, 12 (the checkerboard equals the ε-grading) and 13 are momentum-space and representation statements. Kernel `theorem_8` (`TasteBranching.lean:230`) is a group action on corner labels. **(N)** in content.
- The finite torus is a constraint here, not a support [IR, standard]: a torus is bipartite, and has the momentum-π corners, only if every side is even. The corpus does not state this. On `Z^d` there is no restriction. **(L)** for the model class.
- The conditions are H-spin', H-χ', light-spectrum selection, the Higgs doublet as an input (Theorem 11), and the exceptional branch Y_Q = 0.

**(f) Discrete symmetries (Sub:167; SM:621–673).**

- Theorem 17 (the local rule is symmetric in t) and Theorem 18 (θ is T-odd, and the partition commutes with T) use no finiteness. **(N).**
- Proposition 20 and Theorem 21 are a counterexample and linear algebra. **(N).**
- **Theorem 19 is (T).** It requires "let the hidden prior be the counting measure". The proof counts fibres and divides "by $|\mathcal{C}_H|$" (SM:641–643). The kernel `theorem_19` uses `Fintype.card H` (`Reciprocity.lean:129–134`). Candidates:
  - **(α) P6 (audit AM-30).** A measurable-carrier statement under φ-invariance of (counting ⊗ μ_H) and T-invariance on the infinite carrier. Not written; gated on Q5 and Q6.
  - **(β) [IR, not checked; no recovery credit].** For the native nearest-neighbour linear rule, with a site-wise reversal `(p,c) ↦ (c,p)`, fix `n`:
    1. On a torus `T_L` with `L > 2n + diam(V)`, `theorem_19` gives `T_ij(n) = T_{θj,θi}(n)` under the counting prior.
    2. EF-1 r7 N1.8 (a draft, [IR] there) gives equality of the torus and `Z^3` observation laws on `[0,n]` under the uniform product prior.
    3. Composing the two gives reciprocity on `Z^3` at each horizon `n`, under that prior.
    - Gaps: the uniform product prior is a premise (Q6); N1.8 is off `main` and unreviewed in its r7 form; the composition itself is unchecked.

**Uniqueness at Stage 2 (Sub:169).** "Each step (a)–(f) is a uniqueness statement". Read one direction at a time:

- Steps (b), (c), (d) and (e) derive the structure from their inputs (the forward direction).
- The uniqueness clauses rest on the stated premises: the nearest-neighbour class, m = 1, a generic Σ (a non-generic Σ, for example with two equal block values, has a larger stabilizer), and the Y_Q ≠ 0 branch.
- None of the uniqueness clauses uses `|S|`.

**Bell compatibility (Sub:171).** It concerns the reference cone and H-Bell. **(N)** for A1.

### 1.4 Stage 3 (Sub:175–185)

The gap equation is that of GR §3. Its counting link is GR:58 ("Restrict the finite total system to a conserved energy shell … uniform counting") and GR:70 (finite reversible counting, `N_ij = N_ji`). **(T)** (audit AM-22). Candidate P7: shell counting on `C_V × C_B`, with the boundary layer finite by GR's own mode count rather than by A1. P7 is not written. The gap is GR:70's microreversibility on the boundary shell when the deep sector couples. EF-1 r7 N3.7 states that the fixed-horizon lemma does not carry this. Changemap OQ-2 holds the interim wording.

### 1.5 Lemma 23.0 and Theorem 23 (Sub:189–195)

- **Lemma 23.0.** Its hypothesis lists A1–A6. Its proof says "Stage 2 selects the same … invariants from E4–E7, A3–A6 and the nearest-neighbor premise" (Sub:191), so the proof itself does not cite A1 for the Stage-2 invariants. The sentence about the `G_sub` generators uses Theorem 24 (i) and (iii), which are finite-model statements, but the conclusion "same invariants" does not need them, since Stage 2's outputs are functions of its inputs [IR]. **(N)** for d, K, (3,2,1), the gauge group and the hypercharges. **(T)** for the ħ clause, through Stage 3.
- **Theorem 23.** Its proof routes through the stages. Its A1 consumers are exactly the (T) rows above: Sub:137's recurrence clause, C2, Theorem 19 and Stage 3. Proposition 4b is a consumer only if H-cust's kinetic clause is taken from it. Sub:104 already says "removing any of A3–A6 either requires new derivations or weakens the uniqueness"; A1 is not in that list.
- **Mirrors.** Struct:47, GR:342 and ch02:88–122 restate the labels and consume nothing further. Changemap rows U-10, U-18, U-19, T-03 and K-ch02-88/118/122 keep "finiteness of $S$" as an explicit hypothesis. This is accurate, because Theorem 23 does consume total finiteness through the four (T) rows. The trace shows that none of these rows lies on the gauge-selection path.

### 1.6 Theorem 24, its Corollary, Proposition 9.5

- **(i) (Sub:253).** "with uniform hidden prior $\omega_H = \mathbb{1}/|\mathcal{C}_H|$": a finite `C_H`, which is a realization's hidden sector. **(T)** as stated. The proof ("conjugation by $\mathbb{1}_V \otimes P_\sigma$ leaves $\omega_H$ invariant", Sub:266) works for any normalized σ-invariant prior [IR]. Candidate P11.
- **(ii) (Sub:255).** **(N).** The step is conditional on the alphabet-size hypothesis.
- **(iii) (Sub:257–262).** The proof uses $\operatorname{Tr}\sigma_A=1$ and no finiteness of `V × H` (audit AM-12). **(N)** on the original carrier. Finiteness of `A` is the statement's own scope, and Sub:262 already declines the infinite extension. Candidate: EF-1 r7 Lemma PM (b), (c), applied per horizon. It is a draft and needs equal patch marginals.
- **(iv) (Sub:264–266).** "the finite-law representation [Main §3.4] holds for any finite bijection" refers to finite visible laws. **(V).** The gauge qualification ("the local point group is *not* a quasi-isometry invariant") is local. **(N).** The corpus's own statement that the gauge content is local.
- **Corollary (Sub:268).** Part (i) is E3's bound on `C_V × C_B`. **(V)**; its last sentence, "This reading is the interpretive premise of A1", is not a derivation, and changemap U-23 deletes it. Part (ii) is **(V)** plus H-BD. Part (iii) is exact transfer for finite decoupled extensions. **(T)** only for its recurrence clause, which the gauge selection does not consume.
- **Sub:288.** "$S$ is a finite set with no complex structure": the finiteness is idle. **(N)** (U-24).
- **Proposition 9.5 (Struct:646).** Its proof sketch uses Theorem 24 (i) and (iii). The hypothesis "satisfying A1-A6" is consumed only through (i)'s finite `C_H`. **(T)** inherited. Changemap T-08 ("finite substrata satisfying A2-A6") is accurate. With P11 the finiteness could be dropped.

### 1.7 Mirror finding (not A1)

ch02:106 and FULL:740 say "T-invariance of the bijection $\varphi$ combined with detailed balance gives reciprocal visible transition counts". FULL:1224 has the same wording. In SM, detailed balance is the θ = id *case* of Theorem 19's conclusion (SM:641), not an input. Sub:167 gives the direction correctly. This is a wording inconsistency in the direction of the inference. It is recorded for whoever drafts the ch02 rows, and nothing is proposed here.

***

## 2. The excluded continuum class (Sub:205–207; ch02:122)

Sub:207 says "Intrinsically continuum theories (violate A1)". Changemap U-21 proposes "(violate the finiteness hypothesis of Theorem 23)". That wording is true as an entailment while Theorem 23 keeps the hypothesis. The question here is what excludes the class when total finiteness is not assumed.

**What still excludes intrinsically continuum theories:**

| Source | What it excludes | Where |
|---|---|---|
| A4's lattice clause | a continuum of sites: translations form a rank-`d` lattice | Sub:98 |
| Site factorization (viii) and the finite local alphabets | continuous field values | Main:728 item (xiii): "a finite abelian group"; SM §2.4: "a product of finite sets" |
| A3 with (xiii)'s finitely many reads | unbounded local coupling | Sub:96; Main:728 |
| Lemma 1, and E3 read under H-BD | a continuum in the visible and boundary sectors only | Main:46; Sub:92, :268 (i) |

The first three are properties of the selected lattice model. They exclude continuum theories with or without total finiteness. What A1 adds beyond them is the exclusion of *infinitely many* sites, for example `Z^d` with finite alphabets. That is not an intrinsically continuum theory.

**Retiring A1 makes A3 contentful.** Main:728 item (ix) says that "at a single finite lattice the bound holds automatically, so the item has content only in family form". On a single infinite lattice A3 has content on its own.

**What does not exclude them:**

- **E3 alone.** It bounds only `C_V × C_B`: "This bound alone does not establish finiteness of every underlying sector" (Sub:92). It does not restrict a deep sector.
- **A2.** Continuum bijections exist. SM:44 itself says "A continuous Hamiltonian system on a compact phase space is also deterministic and bijective".
- **A6.** It "restricts no rule" (Main:728). The kernel holds A6 at the complex carrier.
- **E4–E7.** Continuum physics satisfies them.
- **The gauge mechanism.** The (3,2,1) split needs the discrete group O. "Under the continuous group $\mathrm{O}(3)$ … multiplicities $(3, 3)$" (SM §4.6 Remark). This excludes continuum-isotropic theories from *this mechanism*, not from the class. Theorem 24 (iv) and SM §2.2 call the gauge group "a universality-class invariant, shared with any Standard-Model-reproducing class through different machinery".

**Corpus tension.** SM:44 and Main:60 ("in the continuum limit, becomes the Liouville measure") contemplate continuum deterministic carriers. Sub:207 lists the class as excluded. Retiring A1 does not create this tension; it was already present.

***

## 3. Bottom line for the gauge-group selection

**Answer.** The SU(3)×SU(2)×U(1) selection, with multiplicities (3,2,1) and the multiplet structure (three candidate sectors, link-carrier representations, anomaly-free hypercharges), depends on **neither** total finiteness **nor** the finite-lattice model class, in any written step.

- The finite-lattice class appears only through A4's wording.
- In two places the finite lattice adds a constraint: the growth law below the system size, and even sides for the staggered and bipartite structure [IR].
- One qualification: if H-cust's kinetic clause is taken from Proposition 4b rather than carried as a premise, the selection uses Main Lemma 3's counting measure on a finite model. Candidate P13 would replace it under a named product prior.

**Skeptical pass (§A.31).** "A1 is not needed for the gauge group" is favourable to OI, so it was pressure-tested.

- *(1) Is A1 smuggled in through Stage 1?* No step of (b)–(e) cites Stage 1 content. The only link is the phrase "inherited from Stage 1", which is not written (§1.2).
- *(2) Through the carrier?* The gauge steps are carried out on the complex lift, which the kernel proves is infinite.
- *(3) Through the uniqueness clauses?* They rest on genericity and named premises, not on `|S|`.
- *(4) Through the lattice?* Every local object used is defined on `Z^d`: links, the point group, BZ corners and the checkerboard.

The favourable reading survives; its cost is that the support is exactly the list below.

**Conditions the selection depends on regardless of A1** (none is relaxed by retiring A1):

1. Site factorization (ledger (viii)) and the nearest-neighbour premise (x). The cubic link set exists only relative to them (SM:70, :348).
2. A4: translations of a rank-`d` lattice, and centre-freedom. A5 linearity, an affine rule from amplitude-scale gauge plus the further restriction to linear (Sub:274). E4 isotropy.
3. d = 3 from E5–E7 within A4's class, conditional on the continuum step of SM §3.1–§3.2.
4. The simple-cubic Bravais type, selected empirically (Theorem 7b; Sub:203). This direction is from the observed group to SC.
5. **The coarse-graining bridge `φ → L_obs`, open.** "not proved anywhere in this framework" (SM:232). The whole of §4.4–§4.9 is stated for the observer-level branch, and Corollary 1b needs observer-level centre-freedom.
6. **H-link** with its single-copy clause m = 1 (SM:360–366).
7. **H-cust.** Its kinetic clause is a theorem only at the symmetric point for a component-complete observer (Proposition 4b, finite model), and otherwise a premise. Its condensate clause (O-equivariant Σ) is a premise. Genericity of Σ is also required.
8. Amplitude-scale gauge, an operational input (Sub:272). It removes only the common phase.
9. A specified charged matter action, the five-representation family pattern, family-universal charges, anomaly cancellation, the Y_Q ≠ 0 branch, and the electromagnetic identification (Theorems 14–15, Props 14a, 15a). The SU reduction needs the matter action; amplitude-scale gauge does not supply it (SM:585).
10. For the multiplets: H-spin', H-χ', light-spectrum selection, and the Higgs doublet as an input (Theorem 11). For the local reading: A6, which carries no content beyond the interface (`a6cov_all`).
11. **M1 and the hidden-sector mixing hypothesis** are hypotheses of Theorem 23, and Sub:129 says "The framework's gauge-group derivation through Stage 2 inherits this conditional". No written step of (a)–(e) consumes C2, M1 or the mixing hypothesis [IR]. The inheritance is through Theorem 23's hypothesis list, not through a step. This is not an A1 matter, so under Q11 (a) it is recorded here and not acted on (question 4.3).

***

## 4. Open questions for the owner

**4.1 Wording of Sub:207 (changemap U-21; ch02:122 mirror).**

- (a) U-21 as proposed: "(violate the finiteness hypothesis of Theorem 23)". True while Theorem 23 keeps that hypothesis.
- (b) Name the premise that excludes the class whatever the total cardinality: "(violate A4's lattice structure or the finite local alphabet of the selected model)".
- (c) Delete the bullet.

**Recommendation: (a) in the stage-2a correction, with (b) recorded as part of P12's scope.** Option (a) is the minimal accurate change while finiteness stays a hypothesis. Option (b) becomes necessary once P12 drops it, because otherwise the bullet would name a premise the theorem no longer has (§A.30, "fix the root cause, not the label").

**4.2 Gauge part of P12.**

- (a) Keep Stage 2 on the finite periodic lattice as a model condition (Q3's qualification), recording only that (a)–(e) do not consume finiteness.
- (b) When P12 is authorized, restate Stage 2 (a)–(e) on the rank-`d` lattice (unit U-A4), with H-cust's kinetic clause carried as a premise. Proposition 4b would be cited as the finite-torus theorem it is. No new probability premise would be added.
- (c) As (b), but discharge the kinetic clause through P13 under a named product prior.

**Recommendation: (b).** It follows this trace with no new premise (Q11, §A.29). Option (c) adds a Q6-type premise in order to discharge a clause that Theorem 5 already states as a hypothesis.

**4.3 The mixing and M1 inheritance (Sub:129) and the Stage 1 → 2 interface (§1.2).** These are outside A1, under Q11 (a).

- (a) Open a separate Issue covering both findings: the gauge outputs do not consume C2, M1 or mixing in any written step, and the identification of Stage 1's object with Stage 2's lattice model is not written.
- (b) Take no action.

**Recommendation: (a).** Under (b), Theorem 23's premise list overstates what the gauge outputs use, and it leaves the one-object identification unstated. Either way, no status changes until the Issue's own review.

**4.4 Theorem 19 route, for AM-30, when a unit is authorized.**

- (a) P6 (measure-theoretic).
- (b) Route (β) of §1.3(f): per horizon, from tori.
- (c) Both.

**Recommendation: (b) first.** It reuses the kernel's `theorem_19` and the patch-matching comparison, and it is limited to the native rule. Both routes need the product prior as a named premise (Q6 (a)+(e)), and both need T-invariance on the infinite carrier (Q5).

***

## 5. Sources read

- **Repository at `e4c6ba7f`.**
  - `AGENTS.md`.
  - `papers/Substratum.md` lines 60–300: §3 complete (E1–E7, A1–A6, the critical dependencies, Stages 1–3, Lemma 23.0, Theorem 23, the Remarks) and §4 to the gauge hierarchy (Theorem 24 (i)–(iv), its proof, the Corollary, the amplitude-scale Remark and Status, Prop. 24.2, the subsumed family).
  - `papers/SM.md`: §2.1–§2.7 (40–98); §3.1 (100–168, partly skimmed in the long Lorentz paragraphs); §3.2 (170–214); §4.1–§4.6 (216–428); §4.9 (573–599); §5.1–§5.5 (621–673). Searched only, for finiteness terms: §4.7–§4.8 (Theorems 8, 8b, 10, 12 and the checkerboard Remark read).
  - `papers/Structure.md:47`, `:640–652`; `papers/GR.md:340–344`; `papers/Main.md:44–64` and `:728` (the posit ledger).
  - `book/ch02-substratum.md:72–124`. FULL was searched for one phrase.
  - Lean source, not built: `OIBridge/A6Instantiation.lean` (header, `CX3`, `AS1`); `OIBridge/SubstratumInterfaceAudit.lean:40–112`; `OIBridge/LinkDecomposition.lean` (header, `theorem_7` statement); `OIBridge/TasteBranching.lean:230`; `OIBridge/Reciprocity.lean:125–142`. Theorem-name searches in `RegionTower.lean` and `QuasilocalAlgebra.lean`. A search for "Bravais" in `OIBridge/` returned nothing.
- **Records off `main`, cited as drafts:**
  - `A1-IMPACT-AUDIT-r9.md`: AM-11, AM-12, AM-14, AM-16, AM-21, AM-22, AM-30, AM-31, AM-32, N-1 to N-3, Q3, and the P12/P13 table rows.
  - `DECISIONS.md` (the owner decisions of 2026-11-15).
  - `EF-1-r7.md`: header, Lemma PM, N1.8, N3.3, N3.8, N3.9. It is a reviewed draft whose r7 form is unreviewed.
  - `CHANGEMAP-A1C-r1.md`: header, U-09a to U-26, S-15, S-16, T-03 to T-08, the K-ch02 rows, Part F (unreviewed).
- **Not read or not checked.**
  - The rest of SM §3.1 and §4.7–§4.8, beyond the searched and listed lines.
  - SM §4.7.1.2's link-carrier construction in full.
  - GR:58 and :70 directly; Stage 3 relies on audit AM-22's reading.
  - Main §2.3 and §3.4 proofs; their A1-free status relies on Main:60.
  - `DEPENDENCY-AUDIT.md`.
  - Route (β), P11 and P13 are not checked. The even-side requirement for tori is a standard graph fact and is not stated in the corpus.
