# GAUGE-A1 trace, r2: where total finiteness (A1) enters the Substratum lattice and gauge-structure derivation

**Status.** Paper-only, read-only and unreviewed in this form. No repository file was edited, committed or pushed. No GitHub record was written. No Lean build, simulation or computation was run. No premise is adopted, no status is changed and no recovery credit is given: every "candidate" below is a candidate only.

r2 is r1 revised against its independent review, `REVIEW-GAUGE-A1-TRACE-r1.md` (REVISE: B1, R1–R5, r1–r9). Each finding was checked first-hand against `main` before it was applied. The response table is at the end. r1 is kept unchanged.

All `file:line` references are to `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Abbreviations: Sub = `papers/Substratum.md`, SM = `papers/SM.md`, Struct = `papers/Structure.md`, ch02 = `book/ch02-substratum.md`. **[IR]** marks a reading made here that is not stated on `main`. "Not written" means that the step the label implies does not appear in the text.

**Owner request (2026-11-15).** "We should also investigate the Substratum discussion about gauge representation. I think this was the part of the original A1 argument." This trace fills the gap that audit r9 records under AM-11 ("Stages 2(a)–(e) and 3 are not traced for A1") and that EF-1 r7 N3.8 leaves open.

**Classes.**

| Class | Meaning |
|---|---|
| (V) | Only a finite visible or boundary sector is used (Lemma 1, or E3's bound on `C_V × C_B`). |
| (L) | A finite periodic lattice is used as a model class. |
| (T) | Total finiteness of `S` is used in a proof step, through counting measure, recurrence, finite cardinality or a finite count. |
| (T-def) | No proof step uses it, but the object a step is stated on is constructed in the corpus only for finite `S`. |
| (T-just) | Used in the justification of an input, not in a derivation step. |
| (N) | No use. |

***

## 0. Summary

**Finding.**

- **No written proof step of Stage 2 (a)–(e) uses total finiteness of `S`.** Each proof was read; the proofs use local link geometry, representation theory, anomaly algebra and named premises.
- **The observer-level objects are built only for finite `S`.** Step (b)'s normalization α = 1/d and steps (d)–(e) are stated on the observer-level branch of Corollary 1b (SM:270, :312). The only written construction of that branch is a finite-`S` projection: Theorem 1a ("Let $S$ be finite", SM:242), and Lemma 1c, with "the counting measure of [Main] Lemma 3, or a stated structured prior" and a finite-dimensional Schur identity (SM:252). Its relation to φ is the open bridge (SM:232).
- **On an infinite carrier, these objects need inputs the corpus does not supply.** The Markov part, the kinetic structure and the condensate `Σ = ⟨φφ†⟩` need either a normalized measure or state, or must be carried as posited observer-level data. That is a dependence through definition, not a premise in a proof step.
- **As A4 stands, the lattice model is already finite.** A4 says "finite periodic lattice" (Sub:98). With site factorization (viii) and the finite alphabet of ledger item (xiii), it makes `S` finite. A1 is therefore redundant for the lattice model, not absent from it.
- **Validity on `Z^d` is a reading.** That (a)–(e) hold on `Z^d` with the same local rule is [IR]. It is not written for the substratum, and it belongs to unit U-A4 or changemap r3 OQ-6 (b).

**Where total finiteness is genuinely used.** In the derivation steps of Theorem 23's chain, (T) occurs in five places:

1. Stage 1's recurrence-cycle sentence (Sub:137).
2. The C2 necessity forms (Sub:129).
3. Theorem 19's reciprocal counts, used in Stage 2(f) (SM:641–643).
4. The shell counting behind Stage 3 (GR:58, :70).
5. Proposition 4b's counting measure (SM:334). This is a use only if H-cust's kinetic clause is taken from Proposition 4b, since Theorem 5 states H-cust as a premise.

Two further kinds of use sit in the chain without being proof steps:
- (T-just): A2's justification (Sub:94).
- (T-def): Theorem 1a and Lemma 1c, as the construction of the observer-level branch.

Outside the chain, (T) occurs in Theorem 24 (i), the recurrence clause of the Corollary's (iii), and Proposition 9.5.

**Answer to the owner.** The original A1 argument does not sit in a proof step of the gauge representation. Where it reaches the gauge sector at all, it does so through the finite construction of the observer-level objects, and through A4's finite lattice.

| Stage / result | Use | Replacement candidate (candidate only) | Gap |
|---|---|---|---|
| A2's justification (Sub:94) | T-just | `a2_every_substratum` (bijectivity automatic for the second-order form, no finiteness) for Stage 2's needs | the dilemma's eventual-image prong is finite; Q5 (a) treats bijectivity as a model condition |
| Stage 1: constructed triple, C1, C3, C4 | V | Main §3.4 per horizon (Main:60: needs only Lemma 1) | none |
| §3.2 forward dilation (Sub:110) | V | on a constructed finite realization | none |
| Stage 1: recurrence-cycle sentence (Sub:137) | T | none (EF-1 r7 N3.1) | stays finite-model; Stages 2–3 do not cite it |
| Stage 1: C2 forms | T (uniform prior) | P5a, P5b (audit; not written) | reference prior is a Q6-type premise |
| Stage 1 → 2 interface | partly written | — | the M1-T temporal dilation is not identified with the lattice model |
| 2(a) dimension | L | [IR] the same argument on a rank-`d` lattice (U-A4) | continuum step on finite families `G_N`, `N → ∞` |
| 2(b) form lemma | N | — | nearest-neighbour premise |
| 2(b) α = 1/d; the observer-level branch (Thm 1a, Lemma 1c, Cor. 1b) | T-def | Lemma 1c's "stated structured prior", or the branch as a posit | bridge φ → L_obs open (SM:232) |
| 2(c) K = 6 | N | — | H-link, m = 1 |
| 2(d) (3,2,1), Theorem 7 | N (kernel `theorem_7`, link set only) | — | — |
| 2(d) stabilizer, Theorem 5 | N in its proof; T-def through the observer-level objects | — | H-link, H-cust, equivariant generic Σ, condensate state |
| H-cust kinetic clause via Prop. 4b | T (counting measure) | P13 with `uniform_family_consistent` | resummed response on an infinite carrier not written; prior is Q6 |
| SU reduction and hypercharges | N | — | matter action, family pattern, Y_Q ≠ 0 |
| Local promotion by A6 | N (polymorphic kernel) | — | — |
| Theorem 7b | N; converse is a paper argument | — | no kernel witness found |
| 2(e) tastes, chirality (Thms 8–13) | L / N | [IR] `Z^d` | H-spin', H-χ', light-spectrum selection |
| 2(f) Thms 17, 18, 20, 21 | N | — | H-top, H-det |
| 2(f) Theorem 19 | T | (α) P6, general; (β) narrower: native rule, per horizon [IR, unchecked] | product prior (Q6); T-invariance on the infinite carrier (Q5) |
| Stage 3 | T | P7 (not written) | boundary-shell microreversibility with a coupled deep sector |
| Lemma 23.0 | N for Stage-2 invariants; T for ħ | — | as Stage 3 |
| Theorem 23 | union of the rows above | P12 | as above |
| Thm 24 (i) / (ii) / (iii) / (iv) | T / N / N / V and N | P11 (needs proof) / — / EF-1 Lemma PM (draft) / — | Q6 / alphabet-size hypothesis / equal patch marginals / — |
| Corollary (i), (ii) / (iii) | V / T (recurrence clause) | — | U-23 sentence |
| Prop. 9.5 | T (uniform prior on finite `C_H`, and the declared trace-out prior) | P11 (needs proof) | as Thm 24 (i) |

***

## 1. The trace, stage by stage

### 1.1 Stage 1 (Sub:121–141) and its inputs

- **A2's justification (Sub:94).** "every map on a finite set restricting to a bijection on that image". **(T-just).** It is total finiteness, used to justify an input.
  - Stage 2 does not need it: bijectivity of the second-order form is automatic and uses no finiteness (`a2_every_substratum`, `SubstratumInterfaceAudit.lean:106`).
  - Under Q5 (a), bijectivity is a model condition.
- **The forward dilation (Sub:110; Main §3.2).** It acts on a constructed finite realization. **(V).**
- **Output "with $S$ finite" (Sub:125); derivation (Sub:137).** The triple is a constructed realization on "an enlarged finite space $\mathcal{C}_V \times \mathcal{C}_H$". Main:60: the §3.4 equivalence, "in which a finite hidden space is constructed, not assumed", uses only Lemma 1. **(V).**
  - C1 and C4 hold per horizon.
  - C3 holds per horizon, and is vacuous for an infinite hidden sector (AM-31).
  - (C2-structural) is supplied by reversibility.
- **Recurrence-cycle sentence (Sub:137).** "on a fixed finite representative … somewhere in the recurrence cycle". **(T).** No fixed-horizon form carries it (EF-1 r7 N3.1), and Stages 2–3 do not cite it.
- **C2 necessity (Sub:129).** It is stated for the uniform-prior bijection marginal (AM-21). **(T)** through the prior. Candidates P5a and P5b are not written.
- **Stage-1 gauge statement (Sub:139).** It concerns a constructed finite datum. **(V).**

### 1.2 The Stage 1 → Stage 2 interface

Sub:157 opens: "The coupling graph inherited from Stage 1". Two parts of the interface are addressed in the corpus:
- The Bell-inclusive identification is assumed under H-Bell (Sub:145).
- SM §2.3 adds the local factorization and the coupling data to the triple as data.

But no step identifies the M1-T temporal dilation `C_V × C_H` with the Stage 2 lattice model. The graph that Stage 2 uses comes from four sources: site factorization (viii), A3, A4's lattice, and the nearest-neighbour premise (x). A1 is not involved in this gap.

### 1.3 Stage 2 (Sub:143–173)

**(a) Dimension (Sub:157; SM:170–214).**

- **Where finiteness enters.** Through A4's "finite periodic lattice" (Sub:98, :157). **(L).**
- **Growth exponent.** It is "below the system size" on the finite quotient (SM:202).
- **The three filters.**
  - E5 and E6 are continuum physics.
  - E7's ratio uses GR §3.1's classical temperature, which rests on Lemma 1 (GR:98–102). The factors `ε` and `σ` cancel (GR:422–426). SM:196's import of the GR §5 coefficient, which is conditional on H-slope and the detailed-balance ratio, is not needed for the ratio. E7 is redundant for d = 3 (SM:200).
- **The continuum step.** d = 3 is conditional on it, and it is formulated on finite graph families `G_N`, `N → ∞`: the mesoscopic Ollivier construction (SM:150) and the contamination diagnostic (SM:152). Even on a rank-`d` lattice, the existing argument is a limit of finite graphs.
- **Runs on `Z^d` with the same local rule:** [IR], not written. Unit U-A4, or OQ-6 (b) in changemap r3.

**(b) Wave equation (Sub:159; SM:222–278).**

- **Form lemma (SM:224–228).** It is local: `f` as a function of the `2d` neighbours, lattice symmetry, additivity. **(N).**
- **Coefficient remark (SM:230).** It is Fourier analysis of the observer-level real lift.
  - SM:222 reads in full: "The OI substratum is represented here by a $d$-dimensional hypercubic coupling graph $\Lambda=\mathbb Z^d$ … The finite bijection is fundamental; a real/complex wave operator is an observer-level lift whose derivation must be stated separately."
  - So SM §4 represents the observer-level lift on `Z^d` while stating that the finite bijection is fundamental.
- **The observer-level branch.**
  - Corollary 1b's hypothesis concerns "the observer-level Markov part $T$" (SM:270).
  - SM's only written construction of that object is `A = PUP` of Theorem 1a, which has hypothesis "Let $S$ be finite" (SM:242).
  - It uses the canonical projection `P_μ` of Lemma 1c (SM:252). Lemma 1c is (T) through its counting-measure option, and through (ii)'s finite-dimensional determinant/Schur identity whichever option is taken.
  - Theorem 1a's displayed identity does not use finiteness [IR]. Its hypothesis fixes the setting in which the object exists.
  - **(T-def)** for α = 1/d and for everything stated on this branch.
- **Not counted here.** Theorem 13(iii)'s momentum-space Schur complement `K_eff = D_eo G_oo D_oe` (SM:569) is another observer-level construction on the free lift, with no finiteness of `S`. It is not Corollary 1b's branch.
- **Conditions that remain:** the nearest-neighbour premise (SM:226); observer-level centre-freedom (SM:276); the bridge φ → L_obs, "not proved anywhere in this framework" (SM:232).

**(c) K = 6 (Sub:161; SM:360–366).** Theorem 6 is conditional on H-link only. **(N).**

**(d) Gauge group (Sub:163; SM:340–428, :575–610).**

- **Theorem 7.** The kernel `theorem_7` (`LinkDecomposition.lean:479`) acts on `Fin 3 × Bool`, which is the link set, not `S`. **(N).**
- **Theorem 5 (SM:340–342).** The proof uses Theorem 7, Schur's lemma, and the unitary stabilizer of a block-diagonal Σ, under H-link (m = 1), H-cust, O-equivariance of Σ and genericity of Σ. None of these mentions `|S|`, a counting measure or recurrence. **(N) in the proof.**
  - `Σ = ⟨φφ†⟩` presupposes a condensate state. Theorem 5 takes its O-equivariance as a hypothesis, so the proof consumes no measure. But no state is supplied on an infinite carrier, and the kinetic structure is stated on the branch of (b). **(T-def)** through the observer-level objects.
  - On the kernel: `cx3b_complex_not_A1` (`A6Instantiation.lean:512`) proves only that the packaged link-coupled carrier with `ℂ^6` values, on a finite torus of sites, does not satisfy the interface's finiteness predicate. It is infinite only through `ℂ`. Its module states that SM Theorems 5 and 7, H-link, H-cust and the condensate stabilizer "are neither consumed nor judged" (`A6Instantiation.lean:64–67`). It is not evidence about A1 in the gauge steps.
  - **Layer contradiction (a corpus finding outside the A1 question).**
    - SM:312 and :340 state the gauge structure at observer level. Sub:288 says `S` has "no complex structure". Sub:294 places SU(3)×SU(2)×U(1) as "the gauge group acting on the emergent fields".
    - SM:428 says the group "lives at the substratum … a literal algebraic structure on the lattice, existing before any trace-out is performed". SM:511 says: "At the bijection level, $V_K = V_3 \oplus V_2 \oplus V_1$ is correct and the commutant … acts block-diagonally on it."
    - Sub:298 adds that "a map from $\mathcal{G}_{\text{sub}}$ onto the Standard Model gauge group" is not established.
- **H-cust kinetic clause, Proposition 4b (SM:334–336).** "take the selected counting measure". **(T).**
  - The clause is a theorem only for a component-complete site observer. For other observer classes, H-blind is the named condition.
  - Candidate: P13 with the A1-free uniform product family (`uniform_family_consistent`, `RegionTower.lean:447`, which needs a finite alphabet and allows any site type).
  - Gap: the resummed response on an infinite carrier is not written, and the prior is a Q6 premise.
  - Fallback: H-cust stays a premise, as Theorem 5 states it.
- **Amplitude-scale gauge.** An operational premise that removes only the common phase. **(N).**
- **SU reduction and hypercharges (Thms 14–15, Props 14a, 15a).** Group algebra and the anomaly conditions. **(N).**
- **Local promotion by A6.** `a6cov_all` and `as1_leap_covariant` take any site type (`{ι V : Type} [DecidableEq ι] [AddCommGroup V]`, with no `Fintype`). **(N).** `cx3a_complex_axioms` and `as1_complex` are stated on a finite torus of sites, and `cx3a` gives A4Exact only under the translation-invariance hypothesis `hM`.
- **Theorem 7b (SM:390–416).** **(N).** The two directions are separate (§A.34):
  - forward, SC ⇒ U(3)×U(2)×U(1) for a generic equivariant Σ: Theorems 7 and 5, under H-link and H-cust;
  - converse, "SM group ⇒ SC": a paper argument, with no kernel witness found by a search for "Bravais".

**(e) Matter content (Sub:165; SM:430–571).**

- Theorems 8–13 and §4.7.1.2 are momentum-space and representation statements. **(N)** in content.
- **(L)** for the model class. A torus is bipartite and has the momentum-π corners only if every side is even [IR]. The corpus states the even-side condition only for the staggered null modes (SM:292). Theorem 12's remark asserts "the cubic lattice is bipartite" without it (SM:539). A4's illustration admits "a periodic cubic lattice of side at least $3$" (Sub:98), which includes odd sides.
- On `Z^d` there is no such restriction [IR].

**(f) Discrete symmetries (Sub:167; SM:621–673).**

- Theorems 17, 18, 20 and 21. **(N).**
- **Theorem 19 is (T).** It assumes "the hidden prior be the counting measure" and divides by $|\mathcal{C}_H|$. The kernel `theorem_19` has `[Fintype H]`. Candidates:
  - **(α) P6 (AM-30).** It would keep Theorem 19's generality: any partition-preserving, T-invariant bijection on a measurable carrier with an invariant prior. Not written; gated on Q5 and Q6.
  - **(β) [IR, not checked; no credit].** A narrower replacement, for the native nearest-neighbour linear rule and one horizon at a time:
    1. Take torus `theorem_19` with `L > 2n + diam(V)`. The step-1 hypothesis was checked by the review: `𝒯φ𝒯 = φ⁻¹` for `𝒯(p,c) = (c,p)`.
    2. Transfer to `Z^3` by EF-1 r7 N1.8. That is an unreviewed draft, and the uniform product prior is "a premise of this comparison … not a derived property".

**Uniqueness at Stage 2 (Sub:169).**

- The forward derivations of (b)–(e) are as above.
- The uniqueness clauses rest on named premises: the nearest-neighbour class, m = 1, a generic Σ (a non-generic Σ has a larger stabilizer), and Y_Q ≠ 0.
- None of the uniqueness clauses uses `|S|`.

### 1.4 Stage 3 (Sub:175–185)

GR:58: "Restrict the finite total system to a conserved energy shell … uniform counting". GR:70: `N_ij = |{x∈M_i: φ(x)∈M_j}|`, with time reversal giving `N_ij = N_ji`. Both were read directly. **(T).**

The candidate is P7 (AM-22), which is not written. The gap is GR:70's microreversibility on the boundary shell when the deep sector couples. EF-1 r7 N3.7: the fixed-horizon lemma does not carry it.

### 1.5 Lemma 23.0 and Theorem 23 (Sub:189–195)

- **Lemma 23.0.** Its proof cites "E4–E7, A3–A6 and the nearest-neighbor premise" for the Stage-2 invariants (Sub:191). The `G_sub` sentence, which uses Theorem 24 (i) and (iii), is not needed for "same invariants" [IR]. **(N)** for d, K, (3,2,1), the group and the hypercharges. **(T)** for ħ, through Stage 3.
- **Theorem 23.** Its finiteness uses are:
  - in derivation steps: Sub:137's recurrence clause, the C2 forms, Theorem 19, Stage 3, and Proposition 4b if H-cust's kinetic clause is taken from it;
  - in the justification of an input: A2 (Sub:94);
  - by definition: Theorem 1a and Lemma 1c, through the observer-level branch;
  - and, as A4 stands, finiteness is entailed by A4 with (viii) and (xiii).
- **Mirrors.** Struct:47, GR:342 and ch02:88–122 restate the labels. Keeping "finiteness of $S$" explicit in the changemap's W4a rows is accurate. Changemap r3 notes that under OQ-6 (a) it is redundant with A4.

### 1.6 Theorem 24, its Corollary, Proposition 9.5

- **(i) (Sub:253).** "with uniform hidden prior $\omega_H = \mathbb{1}/|\mathcal{C}_H|$". **(T).** The proof (Sub:266) would run for any normalized σ-invariant prior [IR]. P11 is a candidate that needs a proof.
- **(ii).** **(N).** It is conditional on the alphabet-size hypothesis.
- **(iii).** The proof uses $\operatorname{Tr}\sigma_A=1$. **(N)** on the original carrier. The candidate is EF-1 r7 Lemma PM (b), (c), a draft that needs equal patch marginals.
- **(iv).** **(V)** for finite visible laws. **(N)** for the local point-group qualification.
- **Corollary (Sub:268).** Parts (i) and (ii) are **(V)**; the sentence "interpretive premise of A1" is not a derivation (U-23). Part (iii) is **(T)** for its recurrence clause only.
- **Proposition 9.5 (Struct:646).** It consumes Theorem 24 (i)'s uniform prior on a finite `C_H`, and "the Main paper's trace-out construction", whose hidden prior is a declared realization datum (Main:58). **(T).** Changemap T-08 ("finite substrata satisfying A2-A6") is accurate. Dropping finiteness would need P11, which is not proved.

### 1.7 Mirror finding (not A1)

- ch02:106 matches FULL:740 word for word, and FULL:1224 matches `book/ch04-methodology.md:116`. All three say "T-invariance … combined with detailed balance gives reciprocal visible transition counts".
- In SM, detailed balance is the θ = id case of Theorem 19's conclusion (SM:641), not an input.
- Sub:167 gives the direction correctly. But Sub:167 and the three mirrors all omit Theorem 19's counting hidden prior, which is the hypothesis through which A1 enters.

***

## 2. The excluded continuum class (Sub:205–207; ch02:122)

**As A4 stands, A1 adds nothing to the lattice model.**

- A4 says "the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice" (Sub:98).
- Site factorization (viii) and ledger item (xiii), "a finite abelian group" per site, then give a finite `S` (Main:728; changemap r3 OQ-6).
- A1 constrains only objects without site factorization, such as Stage 1's dilation.
- Under changemap r3 OQ-6 (a), with A4 unchanged, intrinsically continuum theories are excluded by A4 itself as a model condition. U-21's "(violate the finiteness hypothesis of Theorem 23)" is then accurate.

**If A4 is restated for an infinite lattice** (U-A4; OQ-6 (b)), the exclusion rests on these premises:

| Premise | Excludes | Status |
|---|---|---|
| A4's lattice clause (rank-`d` translations) | a continuum of sites | structural assumption |
| (viii) site factorization and (xiii) finite abelian group alphabet | continuous field values at the substratum | "a posit of the selected lattice model, not derived and not an axiom of OI" (Main:728) |
| A3 with (xiii)'s finitely many reads | unbounded local coupling | structural assumption; gains content on a single infinite lattice (Main:728 (ix)) |
| Lemma 1; E3 read under H-BD | a continuum in the visible and boundary sectors only | Main:46; Sub:92, :268 (i) |

- **The exclusion is posited, not established.**
- **Field values are discrete only at the substratum.** The gauge steps themselves use `ℂ`-valued observer-level fields (SM:312; Theorem 5's U(6)).
- **SM §2.4 is not cited.** "$S = S_1\times\dots\times S_N$, a product of finite sets", over `N` sites, entails A1.

**What does not exclude the class:**

- **E3 alone.** "This bound alone does not establish finiteness of every underlying sector" (Sub:92).
- **A2.** SM:44 says that "A continuous Hamiltonian system on a compact phase space is also deterministic and bijective".
- **A6.** It "restricts no rule" (Main:728).
- **E4–E7.**
- **The gauge mechanism.** Under O(3) the multiplicities are (3,3) (SM §4.6). That excludes a mechanism, not the class, and the gauge group is "a universality-class invariant" (SM §2.2).

**A tension that predates A1's retirement.** SM:44 and Main:60 ("in the continuum limit, becomes the Liouville measure") contemplate continuum deterministic carriers.

***

## 3. Bottom line for the gauge-group selection

**Answer.**

- **No written proof step uses total finiteness of `S`.** This covers SU(3)×SU(2)×U(1), (3,2,1), and the multiplet structure (three candidate sectors, link-carrier representations, anomaly-free hypercharges).
- **The finite setting enters in three ways:**
  - through A4's wording ("finite periodic lattice"), which as it stands makes `S` finite, so retiring A1 changes nothing for Stage 2 while A4 stands;
  - through SM §3.1's continuum step on finite graph families;
  - through the finite-`S` construction of the observer-level objects (Theorem 1a, Lemma 1c, Proposition 4b's counting measure), on which (b)'s normalization and (d)–(e) are stated.
- **Validity on `Z^d` is a reading [IR].** Writing it, under U-A4 or OQ-6 (b), would need the observer-level branch, the kinetic structure and the condensate state either carried as posits or defined through a named normalized prior (a Q6-type input).

**Skeptical pass (§A.31).**

1. *Through Stage 1?* No step of (b)–(e) cites Stage 1 content (§1.2).
2. *Through the carrier?* r1's kernel argument is withdrawn (§1.3 (d)). A step on an infinite carrier can still depend on A1 through how that carrier is linked to `S`. That question is item 5.
3. *Through the uniqueness clauses?* No. They rest on named premises and genericity.
4. *Through the lattice?* The local objects (links, point group, corners, checkerboard) make sense on `Z^d` [IR]. As A4 stands, the lattice is finite.
5. *Through the definition of the observer-level objects?* **Yes.** The only written construction is a finite-`S` projection (Theorem 1a, Lemma 1c), and its relation to φ is open (SM:232). This is (T-def), not a use in a proof step.

The favourable reading survives only in the narrowed form above.

**Conditions the selection depends on regardless of A1:**

1. Site factorization (viii) and the nearest-neighbour premise (x) (SM:70, :348).
2. A4: as written, a finite periodic lattice; as restated under U-A4, a rank-`d` lattice. Also centre-freedom, A5 linearity (Sub:274), and E4.
3. d = 3 from E5–E7 within A4's class, conditional on the continuum step on finite families `G_N`.
4. The simple-cubic Bravais type, selected empirically (Theorem 7b; Sub:203).
5. The bridge φ → L_obs, open (SM:232). Corollary 1b's observer-level branch, with observer-level centre-freedom, is a premise wherever it is not built from the finite-`S` projection.
6. H-link, with m = 1.
7. H-cust:
   - kinetic clause: a theorem only at the symmetric point for a component-complete observer (Proposition 4b, finite model); otherwise a premise, or H-blind for other observer classes;
   - condensate clause: a premise, namely the condensate state, its O-equivariance, and genericity of Σ.
8. Amplitude-scale gauge (Sub:272).
9. A specified charged matter action, the family pattern, family-universal charges, anomaly cancellation, the Y_Q ≠ 0 branch and the electromagnetic identification (SM:585).
10. H-spin', H-χ', light-spectrum selection, and the Higgs doublet as an input. A6 carries no further content (`a6cov_all`).
11. M1 and the mixing hypothesis, as hypotheses of Theorem 23. Sub:129 says the gauge derivation "inherits this conditional", but no written step of (a)–(e) consumes C2, M1 or mixing [IR]. This is not an A1 matter and is recorded only.

***

## 4. Open questions for the owner

**4.1 Wording of U-21: Sub:205, :207, :212, :223, :233 (ch02:122 mirror).**

- (a) Changemap r3 U-21 as proposed. Under OQ-6 (a), A4 entails finiteness, so "(violate the finiteness hypothesis of Theorem 23)" is accurate.
- (b) Name the actual excluders. Because (viii) and (xiii) are not among A1–A6, this needs Sub:205's lead restated, for example "The structural assumptions A2–A6, with the selected lattice model's posits (viii) and (xiii), exclude …", with :207 as "(violate A4's lattice structure or the finite local alphabet)".
- (c) Delete the :207 bullet.

**Recommendation: (a) now, consistent with OQ-6 (a); (b) when A4 is restated (U-A4, OQ-6 (b)) or when P12 drops the hypothesis.** Option (b)'s rationale already holds as A4 stands, but it is a larger change than the minimum.

**4.2 Gauge part of P12.** Cross-reference changemap r3 OQ-6, which asks the overlapping question.

- (a) Keep Stage 2 on the finite periodic lattice. This is consistent with OQ-6 (a).
- (b) Under U-A4 or OQ-6 (b), restate Stage 2 (a)–(e) on the rank-`d` lattice. H-cust's kinetic clause, Corollary 1b's observer-level branch and the condensate state would be carried as premises, so no measure is introduced. Theorem 1a, Lemma 1c and Proposition 4b would be cited as finite-model results.
- (c) As (b), but define the branch and the kinetic clause through a named normalized product prior. That is Lemma 1c's "stated structured prior" or P13, and a Q6-type input.

**Recommendation: (a) now; (b) as P12's gauge part when U-A4 is authorized.** Option (b) adds posited observer-level data but no probability premise. Option (c) adds a Q6 premise.

**4.3 Three corpus findings outside A1** (Q11 (a)):
- the mixing and M1 inheritance (Sub:129);
- the unwritten identification of the M1-T dilation with the lattice model (§1.2);
- the layer contradiction (SM:312/:340 and Sub:294, against SM:428 and :511).

Options: (a) the owner opens one Issue for them (a planning act, §A.45); (b) no action. **Recommendation: (a).** No status changes before that Issue's own review.

**4.4 Theorem 19 route, for AM-30.**

- (a) P6.
- (b) (β) first.
- (c) Both.

**Recommendation: (b) as sequencing only.** (β) is narrower (native rule, one horizon at a time); P6, if proved, would restore the general statement. Both need the product prior (Q6) and T-invariance on the infinite carrier (Q5).

***

## 5. Sources read

- **Read for r1** (unchanged): `AGENTS.md`; Sub:60–300; SM §2, §3.1–§3.2, §4.1–§4.6, §4.9, §5; Struct:47, :640–652; GR:340–344; Main:44–64, :728; ch02:72–124; the Lean sources listed in r1.
- **Read first-hand for r2:**
  - SM:428, :511, :569 (in part), :150–152 (in part), :196, :200, :292, :535–539;
  - Sub:94, :110, :294, :298;
  - GR:58, :70, :98–102, :414–440;
  - Main:58;
  - `A6Instantiation.lean:60–77`, :484, :565;
  - `book/ch04-methodology.md:116`.
- **Records off `main`, cited as drafts:** `A1-IMPACT-AUDIT-r9.md`; `DECISIONS.md`; `EF-1-r7.md`; `CHANGEMAP-A1C-r3.md` (W4, U-09a, U-09b, U-21, G-12, OQ-6, F.2); `REVIEW-GAUGE-A1-TRACE-r1.md`.
- **Not read or not checked:**
  - SM §4.7.1.2 (I relied on the review, which read it in full);
  - Main §2.3 and §3.4 proofs;
  - `DEPENDENCY-AUDIT.md`;
  - route (β), P6, P7, P11 and P13.

***

## Response table

| Finding | Checked against | Verdict | Applied in |
|---|---|---|---|
| B1 | `A6Instantiation.lean:64–67`, :498–524; SM:312, :340–342, :428, :511; Sub:288, :294, :298 | Accepted. Refinement: Sub:288 says `S` has no complex structure; the explicit observer-level placement is Sub:294, which is added | §0, §1.3 (d), §3 pass 2, §4.3 |
| R1 | SM:222, :242, :252, :270, :312 | Accepted. Refinement: Theorem 13(iii)'s momentum-space Schur complement (SM:569) is another observer-level construction with no finite `S`, but it is not Corollary 1b's branch, so R1 stands | §0, §1.3 (b), §3 pass 5, (T-def) class |
| R2 | Sub:98; Main:728 (viii), (xiii); SM §2.4; changemap r3 OQ-6 | Accepted | §2, §3 condition 2 |
| R3 | Sub:94, :110; AM-11 | Accepted | table; §1.1; §1.5 |
| R4 | Sub:157; SM:150–152, :202 | Accepted | §0, §1.3 (a), §3 |
| R5 | SM:252, :270, :340 | Accepted | §4.2 |
| r1 | `book/ch04-methodology.md:116`; FULL:740, :1224; Sub:167 | Accepted | §1.7 |
| r2 | SM:292, :539; Sub:98 | Accepted | §1.3 (e) |
| r3 | Sub:145; SM §2.3 | Accepted | §1.2 |
| r4 | Sub:104 | Accepted (argument from silence deleted) | §1.5 |
| r5 | SM:252 | Accepted | §1.3 (b) |
| r6 | `A6Instantiation.lean:484`, :565 | Accepted | §1.3 (d) |
| r7 | GR:98–102, :422–426; SM:196, :200 | Accepted; confirmed first-hand | §1.3 (a) |
| r8 | changemap r3 (U-21 unchanged from r2; OQ-6) | Accepted | §4.1, §4.2, §5 |
| r9, plus the folded Prop. 9.5 point | SM:641; EF-1 r7 N1.8; Struct:646; Main:58 | Accepted | §1.3 (f), §1.6, §4.4 |

Counts: 15 findings (1 blocking, 5 required, 9 recommended), with the folded Prop. 9.5 point applied within r9. All 15 were accepted. Two carry a refinement (B1, R1), and none is disputed.
