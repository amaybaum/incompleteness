# ASSESS-1049 — what is open on #1049 (linear vs affine microscopic dynamics) after the #1210/#1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r5, after the
independent review `review/REVIEW-1049-r4.md` (sha256 `6c0414f0…629c4c`, REVISE); pending a fresh,
independent review.** Nothing here is adopted, promoted or proposed for adoption, and no status
changes. The manuscript corrections and narrowings of §2.3 and §2.4 are proposals recorded in this
file only, as the owner directed; none is made. A review ACCEPT, if reached, authorizes nothing
further. Earlier revisions are kept unchanged: r1 at `r1/ASSESS-1049.md` (`9e60b0ae…0e040`), r2
at `r2/ASSESS-1049.md` (`1628cc78…a893`), r3 at `r3/ASSESS-1049.md` (`75d6af06…2fa9`) and r4 at
`r4/ASSESS-1049.md` (`14c2279f…199a`). Each change is mapped in `DISPOSITIONS-r2.md` (r1 → r2),
`DISPOSITIONS-r3.md` (r2 → r3), `DISPOSITIONS-r4.md` (r3 → r4) and `DISPOSITIONS-r5.md` (r4 → r5).

- **Accountable home.** #1049. Parent #983; related #914, #1029, #1210, #1211, #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1049 c.6740117832 (full record #1169
  c.6740116927): "One paper-only unit each, re-assessing its open question against today's
  #1210/#1211 findings … each with a fresh review. Exact generic checks only." Not authorized:
  computation on an OI mechanism, new physical assumptions, freeze, dispatch, manuscript changes,
  merges. This unit made no git or GitHub write and edited no manuscript. The owner's chat
  direction of 2026-11-09, relayed by the coordinator, is applied in r2: check the affine
  counterexamples against every stated gauge assumption, with its source, before weakening any
  manuscript claim, and propose a narrowing, in this file only, where every stated assumption is
  satisfied (§2.3). REVIEW-1049-r2 cites it as #1169 c.6740778880: "Check the affine
  counterexamples against every stated gauge assumption before weakening the manuscript claim."
  The coordinator's instruction on the generic-check boundary is also applied: P2(A), P2(C) and P3
  are not used as support (§8).
- **Owner direction applied in r3** (relayed by the coordinator, 2026-11-09): "If the reviewer
  confirms that the Substratum sentence is false, it should receive a narrowly scoped correction,
  not merely a qualification." §2.3.1 states what is false in Sub:270–274 under each reading and
  the narrowly scoped correction for each false clause. The theorem-recovery rule of the Code
  Review Rules is applied before any narrowing (§2.4). r4 applies the same direction to the clause
  REVIEW-1049-r3 found missed in Sub:272's second sentence (F6). r5 applies it to the three clauses
  REVIEW-1049-r4 found missed by F7 (R4-B1).
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09). `Sub`, `SM`, `Main`, `Structure` are `papers/{Substratum,SM,Main,Structure}.md` at
  that SHA; line numbers refer to it. `A5` =
  `verification/programmes/substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md`; `Q4` = the
  same directory's `A5-Q4-STAGE2D.md`; `Q3` = its `q3-a6-offsets-20261108/ASSESSMENT.md`; `QP` =
  `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`; `AP1` =
  `…/reconstruction/apparatus-1-20261107/DESIGN.md`; `MECH-1`, `MECH-2` = `…/mechanism-1-20261107/`,
  `…/mechanism-2-20261108/DESIGN.md`.
  (r4) `origin/main` has since moved to `cac5d264` (#1212, "correct SM ring degree bounds"). It
  changes only the degree-bound sentence of SM:112 (`SM.md`, `.tex`, `.pdf`). The `SM.md` edit is in
  place, so no `SM.md` line number moves; `SM.tex` gains one line within :781–794, after the one
  `SM.tex` line cited here (:717). Every other file in the tree has the same blob at both commits,
  and no clause cited or proposed for correction here changed. SM:112 is cited only for G_SM's
  non-affinity and its switch on x_{i+1} = 0, which are unchanged. (r5) The one cited `SM.tex`
  line after the insertion is SM:811's clause, at :4683–4685 at `fd539e15` and :4684–4686 at
  `cac5d264`; both coordinates are given where it is cited (F7).
- **Today's drafts (off `main`, unverified; §A.46 item 7: hypotheses, not premises).**
  `BRIDGE` = `scratchpad/bridge/BRIDGE-UNIT1.md` (#1211 unit 1), r3, sha256 `a5d7aad1…78c1`,
  with its r2 review `scratchpad/bridge/review/REVIEW-UNIT1-r2.md` (`3cdf7dc2…4eb3`, REVISE);
  r1 of this unit read BRIDGE r2 (`bridge/r2/BRIDGE-UNIT1.md`, `3905569b…103a`). `QX3`, `QX4`,
  `SHARED` = `scratchpad/qphen/{QX3-ANTIBUNCHING,QX4-INCOMPATIBILITY-LG,SHARED-MECHANISM}.md`
  (#1210 Phase 1, r5: `e231a795…dd71`, `7f4cd21d…a5a5`, `a7206701…cc4d`). The passages cited
  (QX3 A3.1, QX4 A4.1, SHARED §9 SA-1(a)) were re-located in r5.
- **Labels.** [K] kernel-checked on `main`; [P] reviewed record or paper text on `main`, cited;
  [A] exact algebra done here by hand; [D] derivation here, unreviewed; [X] exact generic check run
  here or by the reviewer and re-run here, a result supported only by it being
  *computation-supported*; [L] literature from memory, not re-read; [H] a hypothesis taken from
  today's unverified drafts; [O] owner decision; [O-ext] this unit's extension of an owner decision
  beyond the question it decided.

***

## 0. Summary

1. **Affine over non-affine is not derived from uniform gauge alone (§2.1); it is, within the
   link-sum class with link maps not assumed additive (GA7-α; §2.4).** The corpus route is:
   unobservability of absolute amplitude ⇒ "every first difference of the update is independent of
   its base point" ⇒ affine (SM:240; Main:726 (vii)). The second arrow is the linearity-equivalence
   lemma, proved in both directions.
   - Among all centre-free nearest-neighbour rules the first arrow fails in its uniform form: for
     d = 2 and d = 3 there are non-affine, centre-free, cubic-isotropic, translation-commuting,
     nearest-neighbour second-order rules for which **every** uniform map x ↦ λx + c𝟙 is an exact
     dynamical symmetry [A; X: P1]. Their uniform permutation symmetry group is exactly the
     additive-automorphism group that SM:96 names as the gauge group [A; X: rv2 R3, r3 K4]. For d = 3
     at every prime q ≥ 5 non-affinity has a complete paper proof [A]. Read as relabellings, the
     amplitude maps constrain no rule [A; O-ext of owner Q2].
   - Among **link-sum** rules, F_i = Σ_j m_ij(x_j) with the link maps not assumed additive, uniform
     shift covariance alone forces affinity, at every d and q (one component; for K components,
     with shifts by every c, G4) [A; X: rv2 R4, r3 K2]. The corpus writes A6's interface as a link
     sum only with additive links; the class with link maps not assumed additive (GA7-α) is not
     stated in the corpus. P1's constructions are not link sums [X: r3 K1].
2. **Theorem recovery (§2.4): not refuted; conditionally recovered.** The sites are those that
   state the affine restriction among the structural assumptions A1–A6 (Sub:100, :104, :220;
   ch02:84 = FULL:718; Structure:259). Two results are kept apart.
   - **Withdrawal (shown).** Every written form of A6's interface is a link sum with linear links.
     P1's constructions are not link sums, so they are not candidate rules at those sites: excluded
     by A6, or outside its domain. **r2's narrowings at Sub:100, :104, :220 and
     ch02:84 = FULL:718 are withdrawn.**
   - **Recovery of the sites' route, "gauge ⇒ base-point form ⇒ affine" (conditional on GA7-α).**
     Uniform gauge plus the link sum gives the base-point form, hence affinity by the lemma, only
     when the link maps are not assumed additive (E3). The corpus never states that class. Under
     the written, additive interface the rule is linear by type ([K] `linkSubstratum_A5`), the gauge
     principle does no work, and the "precisely to the extent" and "exactly when" clauses hold in
     one direction only (G1).
   - Even under GA7-α, link-separability is equivalent to affinity among uniformly covariant rules.
     So it relocates the premise rather than deriving it, unless it has independent warrant (§A.29;
     G2).
3. **Sites that state the gauge principle alone (§2.3.1).** Sub:272 and Sub:274 are not recovered.
   - Sub:272's argument for "so 'absolute amplitude is unobservable' already presupposes an affine
     rule" fails under either reading of "amplitude-dependent dispersion" (F-8). Its clauses "strictly
     weaker than the output" and "excludes" a non-affine F are jointly false under every reading of
     the principle. Its second sentence's "the one route that would make the affine restriction
     *unconditional*" is false under the uniform reading for d = 2, 3 (F6).
   - Sub:274's "delivers the affine restriction" and "certified theorem" clauses are false for the
     uniform group the corpus states (Sub:270, SM:96).
   - Narrowly scoped corrections are proposed, each with a variant that puts no new negative claim
     into paper prose. At Sub:274 a subject-changing variant (V1′) is also offered.
   - A scope point independent of P1 (F7). At q = 2, 3 every permutation of ℤ/q is affine, so five
     clauses at three sites that contrast the additive-automorphism group with arbitrary or
     nonlinear relabellings of ℤ/q are false there: "a proper subgroup of all permutations"
     (Sub:274; SM:96), "not arbitrary relabellings of ℤ/qℤ" (SM:96, first sentence; SM:811), and
     "the strong reading … *overshoots*" (Sub:274). SM:92's "large-q statement" does not scope
     SM:811's clause. A qualifier "for $q \ge 4$" in each clause is proposed; at q ≥ 4 the qualified
     clauses hold on the sources' own reading (F7).
   - Sub:270's "amplitude-independent dispersion ⟺ affine dynamics" is the lemma under the reading
     its own attribution supports, and needs no correction.
   - Structure:219 is held on the alphabet-size hypothesis. Structure:301 makes no overstatement.
4. **Every stated gauge assumption, checked against P1's class (§2.3).**
   - P1's class satisfies, exactly: the relabelling reading, uniform exact symmetry, independence
     of the response from the absolute level, A4's translation clause, and SM:96's gauge group.
   - It fails the site-wise base-point form, by construction. It also fails the site-wise
     exact-symmetry reading, which the linear wave rule fails too.
   - A6 is reading-dependent. P1's class is excluded or outside the domain under the written
     link-sum interface, and satisfies A6 only under a joint-insertion extension that no source
     writes.
   - Its status under the alphabet-size hypothesis is undetermined, because that hypothesis needs a
     cross-q correspondence the corpus does not construct.
5. **Linear over affine stays unselected (§2.2).** Today's drafts add no selector. A5 R5 and Q3
   outcome (N) stand as the record, both WIP / UNVERIFIED.
6. **Most downstream results examined use affinity or only the bipartite read pattern, not
   b = 0 (§3).** The quarter-phase obstruction's sector split holds for non-affine
   nearest-neighbour rules that read only opposite-colour sites [A]. Lemma G2 needs affinity, not
   linearity [A]. Lemma Q(i) needs b = 0 [A; X: P2(B)], but Q(iii) does not [P; A]. The
   positive-frequency J and SM's chirality identities are statements about the linear part and do
   not depend on b [A]. #1210's bounds are stated for the affine-symplectic class. Among the rows
   examined (§3, including A5 rows D7, D12, D13, D15), b = 0 is used at: (A-lin) Stage 2(d),
   absolute labelled readouts, configuration-level conservation laws, the resonant uniform sector,
   the kernel statements `StochasticInterface` gap and `HydroSourceAudit` advection gate as they
   stand (their affine extensions are unreviewed [D] in A5), and SM:1416's Layer-2 candidate
   classes; whether Theorem A.1's period uses it is not examined.
7. **The b = 0 content of the dynamical rows sits on one sector (§3.3).** It is the uniform
   (k = 0) A₁ sector at κ ≡ 2 (α ≡ 1/d for odd q with gcd(d, q) = 1). The same sector is #1049's
   resonance locus (A5 R3), Q4's open resonance condition (Q4c), and #1211's null-mode sector
   where no J exists (NQ1(a)). The kernel and Layer-2 rows of item 6 are statements made under A5
   as stated and are not located on that sector.
8. **Next question (§5, Q-NEXT).** Is link-separability of the update — the link-sum form of A6's
   interface, with the link maps not assumed additive — independently justified as a premise on
   every candidate rule in d = 3?
   - It is the one candidate known to close the implication from uniform gauge to affinity.
   - Its sufficiency is settled. Since on the covariant class it is equivalent to affinity, the
     open question is its warrant.
   - Failing it: does any other independently justified OI principle imply the site-wise
     base-point form? Excluding P1's class is a necessary condition for a positive answer, not a
     sufficient one.
   - A companion question, for b = 0, is the resonance of the A₁ sector at k = 0 (Q4c and #1211
     NQ1(a)).

***

## 1. Inputs and their standing (§A.46 item 7)

| Input | Standing | Used here as |
|---|---|---|
| Linearity-equivalence lemma (base-point-independent first differences ⇔ affine) | [P] Sub:274 (telescoping proof plus exhaustive checks); re-derived [A]: ⇒ by telescoping, ⇐ immediate | established, both directions |
| A6 in the kernel: `OIBridge/BackgroundIndependence.lean` (`A6Inv`, `A6Cov`, `A6Glob`; A6-sd named, no predicate) and `OIBridge/A6Instantiation.lean` | [K] on `main`. `A6Cov` is defined on `linkF N M c i = ∑ j ∈ N i, M i j (c j)` with `M i j : V →+ V`; `a6cov_all` (D3-a: it "restricts no link-coupled rule; its content is the interface"); `linkSubstratum_A5` (every link-coupled carrier satisfies the kernel's A5, additivity of F). The module "adopts no reading" | definitions and theorems as stated (§2.3 GA7; §2.4) |
| Reviewer's checks `review/rv2_gauge_audit.py` R1–R6 (`2422bd13…6faf6cd`) | [X] exact generic checks; re-run here with `python3 -I`, output byte-identical (`372a2c17…16ab2`) | cited where named |
| A5 (WIP / UNVERIFIED; model review ACCEPT at `f07f55d0`; merged `9e0560d8`) | record on `main`, not established | B0.1, B0.2 and Prop. 2.5 re-derived here [A] where used. R5, R6, N10 and rows D7, D12, D13, D15 are cited as the record |
| Q4 (WIP / UNVERIFIED; model reviews; merged) | record | outcome (iii) for O1–O4 cited as the record |
| Q3 (outcome (N); merged `45eea51d`) | record | cited as the record |
| QP Lemmas G1, G2, Q | [P] paper proofs, model-reviewed per QP | statements read; extended in §3.2 [A] |
| BRIDGE "linear beyond affine has no independent justification" | [H]; it cites A5 R5 | checked against R5 (§2.2) |
| BRIDGE r3 §0 item 6 and §10: the premise the quarter-phase obstruction shares with SM chirality is the bipartite, centre-free read pattern, not linearity | [H]; BRIDGE r3 cites its own check K1 | agrees with §3.2 here; r2 of BRIDGE listed linearity |
| BRIDGE "positive-frequency J exists off the null modes" | [H]; J² = −1 re-derived here [A] | §3.3 |
| QX3 A3.1(b)–(c): affine routing under `NCONS_ready`; non-affine forced under `NCONS_global` | [H]; A3.1(c)'s core lemma re-derived here [A] (an affine bijection of F₂ⁿ preserving Hamming weight everywhere is a coordinate permutation: T(0) = 0, columns have weight 1, and the columns are distinct) | §2.1(iii), §3 row 9 |
| QX4 A4.1 affine-symplectic Leggett–Garg bounds | [H]; scope as stated ("with translations"), numbers not re-checked | §3 row 8 |
| SHARED §9 SA-1(a) row and column (ii) | [H] | §3 row 7 |
| Owner Q1/Q2 (#1049 c.6624263637, amaybaum, 2026-11-04T06:28:45Z) | [O] for amplitude shifts in the b = 0 question; [O-ext] where applied to rescalings or to the affine question | binding readings within their scope |

***

## 2. Question 1 — what selects, on independent grounds

The three answers are kept separate. (i): is the restriction well-defined? (ii): does it follow
from independently justified OI principles? (iii): does it reproduce QM or the SM? A positive (iii)
is never cited for (ii). Mathematical availability of a rule class, or of a structure on it, is
kept apart from its derivation from OI.

### 2.1 Affine over non-affine

**(i) Well-defined: yes.** An affine function on (ℤ/q)ⁿ is F(x) = F(0) + Σᵢ cᵢxᵢ. The class is
closed under composition and conjugation by affine bijections.

**(ii) Follows from independently justified OI principles: not established.**

*The corpus route, traced.* SM:240 reads: "if the embedded observer has no access to an absolute
field-amplitude scale, in the form that every first difference of the update over ℤ/qℤ is
independent of its base point, the rule is affine". Main:726 (vii) reads: "the affine restriction
that amplitude-scale gauge invariance yields in the form that every first difference of the update
is independent of its base point". The chain has two links:

- **L1:** the operational principle ("absolute amplitude unobservable", SM:96, Sub:270) implies the
  site-wise base-point form (for every site j, F(x + c e_j) − F(x) does not depend on x).
- **L2:** the site-wise base-point form is equivalent to affinity. This is the lemma, proved in both
  directions.

L2 makes the site-wise form *equivalent* to the conclusion. All the derivational weight therefore
falls on L1.

*Readings of the operational principle, and what each gives.* §2.3 lists every stated gauge
assumption with its source; the three readings that bear on L1 are these.
- **(R-rel), relabelling.** Amplitude maps are conjugations of the description. The owner decided
  this reading for amplitude shifts in the b = 0 question [O, Q2]: "Treat amplitude shifts as
  mathematical relabellings unless their physical gauge status is justified." Its application here
  to rescalings and to the affine question is this unit's extension [O-ext]. A conjugation carries
  every rule to an equivalent description of itself. So (R-rel) excludes no rule, affine or not [A].
- **(R-uni), uniform symmetry.** Every uniform x ↦ λx + c𝟙 (λ a unit) is an exact dynamical symmetry.
  For the second-order form, with the shift acting on both time slices, this means
  F(λx + c𝟙) = λF(x) + 2c𝟙 [A]. For a linear rule this forces κ = 2dα ≡ 2, so (R-uni) is not implied
  by affinity. The counterexamples below do not rest on that strength: the κ-independent reading
  F(λx + c𝟙) = λF(x) + κc𝟙 is also satisfied by a non-affine, O_h-invariant, centre-free rule at
  α = 1 in d = 3 (reviewer's check rv_p1 part B, re-run here).
  - **d = 1, odd q: (R-uni), with centre independence, the nearest-neighbour range and reflection
    symmetry, forces F_i = x_{i−1} + x_{i+1}: linear, with b = 0 and α = 1 [A].** Proof: covariance
    under c gives F_i = s + G(y), where s = x_{i−1} + x_{i+1} and y = x_{i+1} − x_{i−1}, using
    2 ∈ (ℤ/q)^×. The unit λ = −1 makes G odd; reflection makes G even; so 2G = 0 and G = 0. This holds
    at every odd q, composite included. At odd prime q, scaling alone also gives G(λy) = λG(y) and so
    G linear, and without reflection the solutions are exactly the q linear rules
    (1 − g)x_{i−1} + (1 + g)x_{i+1}; at composite odd q, G need not be linear without reflection
    (rv_p1 part E: 27 and 225 solutions at q = 9, 15). Positive control: at q = 3, exhaustive over all
    3⁹ functions, the only solution with reflection is f = s [X: P1]. The result depends on there being
    exactly two read variables: a centre read or a range-2 read in d = 1 reopens non-affine solutions.
    At q = 2, (R-uni) is vacuous in d = 1 (the complement rule 1 + a + b and the constants pass).
  - **d = 2, 3: (R-uni) does not imply affinity among centre-free nearest-neighbour rules [A; X: P1].**
    Among link-sum rules with link maps not assumed additive (GA7-α) it does, at every d (§2.4);
    none of the constructions below is a link sum [X: r3 K1].
    - *d = 3, prime q ∤ 6.* Let p_a = x_{+a} + x_{−a} for each axis a. Set a′ = 2p_x − p_y − p_z, with
      b′ and c′ its cyclic versions, C = a′b′c′ and P = a′² + b′² + c′². Then
      f = (1/3)Σ_nbrs x + C·P^{q−2} satisfies all of the following:
      - f(λv + c𝟙) = λf(v) + 2c, because a′, b′, c′ are shift-invariant and P^{q−2} is homogeneous
        of degree −2 on units;
      - it is O_h-invariant (the 48 elements act on (p_x, p_y, p_z) by permutation);
      - it reads no centre;
      - it is not affine, at every prime q ≥ 5 [A]. Let G = C·P^{q−2} on the plane
        a′ + b′ + c′ = 0. Then G(1, 1, −2) = −2·6^{−1} = −1/3, while G(1, −1, 0) = G(2, 0, −2) = 0 since
        C = 0 there; (2, 0, −2) = (1, 1, −2) + (1, −1, 0), so G is not additive, and G(0) = 0, so G is
        not affine. The map x ↦ (a′, b′, c′) is linear onto that plane (3 is a unit), so f is not
        affine. (Reviewer's S1; checked exactly for every prime 5 ≤ q < 200 [X: r2 G5]; P1's base-point
        witnesses at q = 5, 7 are controls on it.)
    - *d = 2, q = 7.* The same holds for f = (1/2)Σ x + y₃·χ(y₁² − y₂²), where χ is the Legendre
      symbol. With E, W, N, S the four neighbours, y₁ = x_E − x_W, y₂ = x_N − x_S and
      y₃ = x_E + x_W − x_N − x_S. It uses q ≡ 3 (mod 4).
    - *d = 3, q = 2* (the instance displayed in Main §3.2). Take f = Σ x + [all six neighbours equal]
      (covariance with λ = 1 only, the one unit).
    - P1 checks all four constructions exhaustively, with the linear rule as a control and an
      affine-offset rule as a countercontrol (the latter fails covariance). The reviewer's rv_p1
      re-codes them independently (parts A–C), re-run here with identical output.
    - Bijectivity is automatic for the second-order form: x(t−1) = F(x(t)) − x(t+1).
    - Only d = 2 (q = 7) and d = 3 (q = 2 and prime q ≥ 5) are exhibited. No construction for
      d ≥ 4 is given.
  - Continuum analogue [L]: shift-symmetric nonlinear field theories (Goldstone, P(X) and Galileon
    Lagrangians) have φ ↦ φ + c as an exact symmetry and nonlinear dynamics. Shift symmetry forces
    derivative couplings, not linearity.
- **(R-site), site-wise base-point independence.** This is the form SM:240 and Main (vii) name. It
  gives affinity by L2, and it is equivalent to affinity. As a principle it is A5-LINEAR-AFFINE's N2
  ("superposition of perturbations"), with "the background never changes the response". Sub:272
  records that deriving amplitude unobservability from the observer architecture "is … circular".
  The argument it gives for that verdict fails for P1's class under either reading of
  "amplitude-dependent emergent dispersion": under (b) the inference is invalid, and under (a) its
  premise is false (F-8; §2.3.1). The circularity verdict holds with "an
  affine rule" replaced by "a rule for which uniform rescalings and shifts are exact symmetries".

*The one other corpus argument against non-affine rules.* Structure:219 and :301 argue from the
alphabet-size hypothesis: "Non-linear dynamics over ℤ/qℤ generically produce q-dependent observable
physics (x² mod 3 and x² mod 5 have different algebraic structure), violating the gauge
equivalence". Disposition:
- the hypothesis is "not proved for every observable", and comparing two alphabets "requires a
  correspondence between them, which is not constructed here" (SM:94);
- it is "posed for linear dynamics" (Structure:217);
- at the one level A5 checked by hand, cycle type, it excludes the linear rule too, since the linear
  ring period is qL (A5 N10; SM:92, Theorem A.1); A5 N10's verdict is "Undetermined";
- the argument is stated for generic nonlinear rules ("generically") and is not evaluated on P1's
  class. Nothing about that class favours q-independence: the d = 3 construction's nonlinear term
  C·P^{q−2} has degree growing with q, so on Structure:219's own heuristic it is if anything a
  candidate for q-dependent physics. The verdict below rests on the correspondence SM:94 says is not
  constructed, not on any property of P1.

It therefore does not establish the base-point form, and it does not decide P1's class (§2.3,
GA8). Structure:301 itself records that amplitude-scale gauge is "an adjoined operational input
that the alphabet-size hypothesis of [SM §2.7] does not entail".

*Consequence.* The affine part of A5 is a posit in the form named by SM:240 and Main (vii). Among
all centre-free nearest-neighbour rules the operational principle motivates it but does not entail
it in d = 2 and d = 3. Among link-sum rules with link maps not assumed additive (GA7-α, not stated
in the corpus), uniform shift gauge does entail it (§2.4). The corpus writes A6's interface as a link
sum only with additive links, where the rule is linear by type and the gauge principle does no work
(§2.4, G1).
- No corpus source read gives the base-point form an independent reason. The alphabet-size argument
  above is conditional on an unproved hypothesis and does not decide P1's class.
- Main (vii) and SM:240 state the scope accurately.
- The sites that present the affine restriction as following from the gauge principle, with no
  site-wise qualifier, fall into two groups. §2.3 gives the per-site test.
  - *Stated among the structural assumptions A1–A6* ("restrictions on the class of candidate
    substrates", Sub:90; "six properties", ch02:74), with A6 in the same list or sentence. The claim
    is not refuted there: under every written form of A6's interface, P1's rules are not candidate
    rules. Its route through gauge is recovered only conditionally, on GA7-α (§2.4).
    - Sub:100 and Sub:104: "restricts the update to an affine one via the linearity-equivalence lemma".
    - Sub:220: "non-affine wave equations … are the separate class one obtains exactly when that
      gauge principle is dropped".
    - ch02:84 = FULL:718 (identical text).
    - Structure:259: "amplitude-scale gauge invariance yields the affine restriction, weaker than A5
      ([Main §4.5], item (vii))".
  - *Stated for the gauge principle alone.*
    - Sub:272: "the input … is strictly weaker than the output … a non-affine F … the principle
      excludes"; "a non-affine F induces amplitude-dependent emergent dispersion … so … presupposes
      an affine rule".
    - Sub:274: "The principled object that delivers the affine restriction … is the
      additive-automorphism group"; "yields an affine rule as a certified theorem".
    - Structure:219: "An affine rule is therefore forced *given* that operational principle". The
      same paragraph states the alphabet-size hypothesis.
- Sub:270's "amplitude-independent dispersion ⟺ affine dynamics" is the lemma under the reading its
  attribution to [SM §4.1] supports. Under the other reading its ⟹ fails (§2.3.1, F-8).
- `.tex` mirrors of these sites at `fd539e15`:
  - Substratum.tex:743–752 (Sub:100's parenthetical; "restricts the update to an affine one" at
    :744); :783–785 (Sub:104; "linearity-equivalence lemma" at :785); :1407–1410 (Sub:220); :1719–1720 (Sub:270); :1729–1732 and
    :1733–1739 (Sub:272, first and second sentences; F6's clause at :1733–1735); :1768–1773 and
    :1776–1778 (Sub:274; "more primitive" at :1776 and :1782–1783);
  - Structure.tex:980–982 (Structure:219's claim), :1144–1145 (Structure:259), :1269–1271
    (Structure:301's claim; the next sentence begins at the end of :1271);
  - The-Incompleteness-of-Observation-FULL.tex:3312–3314.
  No book passage restates the Sub:272 or Sub:274 clauses (`git grep` for "strictly weaker than the
  output", "presupposes an affine", "delivers the affine", "certified theorem", "amplitude-dependent
  emergent", "amplitude-independent dispersion": hits only in Substratum `.md`/`.tex`).
- How the site claims fare under each reading:
  - With (R-uni) and no A6 interface, P1 contradicts the "exactly when" of Sub:220 and the "excludes"
    of Sub:272 in d = 2, 3.
  - With (R-site), they hold, but then the principle is affinity restated.
  - With (R-uni) and A6's interface as written (additive links), P1 is excluded, and Sub:220's
    "exactly when" holds in one direction only (G1). Under GA7-α it holds in both directions for
    q ≥ 3 (§2.4). Sub:272 does not state A6.
- This is a cross-document finding for #1029. The corrections that pass the owner's test are
  proposed in §2.3.1; none is made.
- **Search scope for "no corpus source".**
  - r2's terms, by `git grep -i`: "base-point", "base point", "amplitude-scale", "affine",
    "non-affine", "partly derived", "certified theorem", "therefore forced", "weaker than A5" and
    "generically produce".
  - r3 added: "amplitude-independent", "amplitude-dependent", "master principle",
    "additive-automorphism", "additive automorphism", "link-sum", "link sum", "separab", "affine link",
    "non-additive", "joint insertion".
  - Scope: `papers/` (`.md` and `.tex`), `book/` and `verification/` (records, and
    `lean-mathlib/OIBridge` for A6), at `fd539e15`.
  - The A5-specific records were read in full. The H-D record (`round-h-d-a5-status-adjudication/result.md`)
    quotes the lemma (U6) and does not separate the uniform from the site-wise form.
  - No source writes A6's interface for non-additive link maps, either as a link sum or by joint
    insertion. Q3 records "Corpus: none" for relaxing the link typing even to affine maps (Q3 A4, E2).

**(iii) Reproduces QM/SM: it cuts both ways, and is not support for (ii) either way.**
- **For affinity.**
  - The operator-spectral chain reads only linear parts: the form lemma, dispersion, Theorem 4, the
    staggered operator and the (3,2,1) multiplets. SM §4.2's "reads only the linear part" is quoted
    in H-D U8.
  - AP1's backaction identity, M15 reciprocity and QX4's bounds are stated for the affine-symplectic
    class.
- **Against affinity, from the programme's own needs.** All three of these are on record or in
  today's drafts:
  - SM's explicit state-dependent-geometry rule (SM:112, G_SM) is not affine, and "A5 fails"
    (MECH-2:42, [P] record);
  - "Any in-world source of setting selection must make the rule non-affine in the joint state"
    (MECH-1 node 1, :434);
  - QX3 A3.1(c) [H]: a router that conserves number globally (`NCONS_global`) must be non-affine.
- **G_SM and SM:96 [A].** G_SM tests x_{i+1} = 0, so a uniform shift changes its coupling graph.
  SM:96 lists coupling structure among the observables. Under G_SM, absolute amplitude is therefore
  observable through the graph, so G_SM violates even (R-uni), not only (R-site).
  - Pointer only, not developed: a state-dependent graph that switches on differences (centre-free,
    shift-invariant) would satisfy (R-uni) and not (R-site).

### 2.2 Linear over affine (b = 0)

**(i) Well-defined: yes.**

**(ii) Not established.**
- Today's drafts add no candidate. BRIDGE B8 and §9 cite A5 R5 for this and classify it "St"
  (stipulation). That classification agrees with R5 and with Q3 (N).
- Status of the R5 search. N1–N11 were re-read. The N8 and N9 nodes were spot-checked [A]:
  - N8: λ = −1 forces b = 0 at odd q;
  - N8: for every even q, b = q/2 is fixed by every unit, so N8 does not force b = 0 at any even q.
- R5 remains a finite search, so it is not an impossibility result.
- **New input from §2.1.** Under (R-uni) in d = 1 (centre-free, nearest-neighbour, odd q), the
  uniform symmetry group does force b = 0 and κ = 2, but that is A5-LINEAR-AFFINE's N8 and N8′
  jointly, and N8 is a symmetry reading the owner has not adopted (Q2). It adds no independent
  selector.

**(iii) Which QM/SM-reproducing results need b = 0?** See §3.

### 2.3 Every stated gauge assumption, checked against P1's class (owner direction, 2026-11-09)

"P1's class" means the four constructions of §2.1: d = 3 at q = 2 and at every prime q ≥ 5, and d = 2
at q = 7. The table lists, with its source, every gauge assumption the corpus states that bears on
which rules are admitted. The list after the table gives the gauge statements that place no
condition on the rule. Together they cover every stated gauge statement the search of §2.1 found.

| ID | Gauge assumption as stated | Source | Reading | P1's class satisfies it? | Support |
|---|---|---|---|---|---|
| GA1 | The additive-group automorphisms (rescalings and shifts) preserve the emergent observables; they are "relabellings of the alphabet"; amplitude-scale invariance "is realized as the additive (affine) relabellings φ ↦ λφ of the alphabet being gauge" | SM:96; Sub:270; ch05:45 = FULL:1363 | (R-rel): conjugations of the description | **yes**, as every rule does: a conjugate rule describes the same orbits | [A]; [O-ext] |
| GA2 | "Operationally the *absolute scale* of the field value is unobservable"; "a global rescaling of the field value φ"; rescalings and shifts "leave every observable unchanged"; "the alphabet's additive automorphisms are gauge"; "the unobservability of the absolute field scale" | SM:96; Sub:163; Sub:270; Sub:274; ch02:84 = FULL:718; ch05:45 = FULL:1363 | (R-uni): every uniform x ↦ λx + c𝟙 is an exact symmetry of the dynamics (κ = 2 form; also the κ-general form) | **yes** | [A] (§2.1); [X: P1; rv_p1 A–B; r2 G3; rv2 R2] |
| GA3 | Amplitude-independent emergent dispersion: the affine relabellings preserve "the field-amplitude dispersion ω(k)"; "amplitude-independent dispersion ⟺ affine dynamics"; "a non-affine F induces amplitude-dependent emergent dispersion" | Sub:270; Sub:272 | One reading serves both phrases (§2.3.1). (a) The local response does not depend on the absolute (uniform) level. (b) The response does not depend on the background state at all, which is GA4 | (a) **yes**, and more: every single-slot first difference is unchanged by uniform shifts, and the response about every uniform background is exactly unit-homogeneous in the perturbation's amplitude. Only additivity fails. (b) **no** | [A]; [X: r2 G1, G2; rv2 R6] |
| GA4 | Every first difference of the update is independent of its base point | SM:240; Main:726 (vii) | (R-site) | **no**, by construction: GA4 is equivalent to affinity (lemma, Sub:274) | [P]; [A] |
| GA5 | "Site-wise relabellings" | Sub:270 | as exact symmetries of the dynamics (site-dependent shifts) | **no**, and neither does the linear wave rule: shifting one neighbour slot changes the update. As relabellings it is GA1 | [X: rv_p1 D; r2 G4] |
| GA6 | A4: φ "commutes with lattice translations up to gauge", gauge acting by site-wise bijections of each site's (previous, current) pair; the update contains no copy of the site's present value | Sub:98 | as stated | **yes**: P1's rules commute with translations exactly and read no centre | [A]; [X: rv_p1 C] |
| GA7-inv | A6 "is not the stronger fixed-background condition that the same transformations leave the dynamics invariant with the coupling held fixed" | Sub:102; kernel `A6Inv` | the reading Sub:102 excludes | **no**, and neither does the linear rule. Not A6 by Sub:102's own text; no discriminator | [K] D2-i; [X: rv2 R5] |
| GA7-cov | A6: "covariant under spatially-varying internal-index transformations … provided the coupling data carried on the links are transformed with it"; "The content of the assumption is this covariant interface"; "fixes the interface through which the gauge symmetry is read locally" | Sub:102; ch02:86 = FULL:720; Main:726 (xii); SM:114–118; kernel `A6Cov`, `linkF` | the interface as the corpus writes it: F_i = Σ_{j∈N(i)} M_ij(x_j) with additive (matrix) links (substratum level: kernel `linkF`, and `linkSubstratum` at `Fin 6 → ZMod q`; prose: SM:116, and SM:312–314 on the observer-level branch). Covariance is then automatic (`a6cov_all`) | **no, or outside the domain.** P1's constructions are not link sums, so they lack the interface. Every rule that has it is additive | [K] `linkSubstratum_A5`; [X: r3 K1; rv2 R4] |
| GA7-glob | The global commutant symmetry, "the specialization of A6 in which nothing needs transporting" | Sub:102; kernel `A6Glob` | constant g commuting with the coupling; at K = 1, g is a unit | **yes** at K = 1 (unit homogeneity). The kernel records the K = 1 rescalings as A5's amplitude freedom, not A6's internal-index freedom (D2-ii; `A6Instantiation` bounded reading), so this is GA2 again | [K]; [X: rv2 R5] |
| GA7-sd | The state-dependent coupling graph, "a separate principle that shares the name and is not A6" | Sub:102; kernel (named, no predicate) | not an invariance | places no condition on the rule | [P] |
| GA7-α | GA7-cov extended to non-additive rules, keeping the link sum: F_i = Σ_j m_ij(x_j), with m_ij not assumed additive | **not stated in the corpus.** It is this unit's and the reviewer's extension; the nearest record is A5 N9's E2 (affine link maps), for which Q3 finds "Corpus: none" | — | **no**: P1's constructions are not link sums. Within this class, uniform shift gauge forces affinity (§2.4) | [A]; [X: r3 K1, K2; rv2 R4] |
| GA7-β | GA7-cov extended to non-additive rules by joint insertion: F_i = f(M_i1 x_1, …, M_i,2d x_2d), with transported links | **not stated in the corpus** | — | **yes** at K = 1, since f is unit-homogeneous. Weak support: the K = 1 transformations are A5's amplitude freedom (kernel D2-ii), and no K > 1 extension of P1 is constructed | [X: rv2 R5] |
| GA8 | Alphabet-size hypothesis: systems differing only in q "produce the same emergent transition probabilities"; "Non-linear dynamics over ℤ/qℤ generically produce q-dependent observable physics … violating the gauge equivalence" | SM:94; SM §2.7; Structure:217, :219, :301; Theorem 24 (ii) (Sub:255) | as stated | **undetermined.** The hypothesis needs a cross-q correspondence that "is not constructed" (SM:94). It is "posed for linear dynamics" (Structure:217). At cycle-type level it excludes the linear rule too (A5 N10, "Undetermined"). The verdict rests on the unconstructed correspondence. Nothing about P1's class favours q-independence: its d = 3 nonlinearity has degree growing with q (§2.1) | [P]; A5 N10 |
| GA9 | "the gauge group is the additive-automorphism group, a proper subgroup of all permutations"; "A nonlinear relabelling … changes the fluctuation dispersion, so it is not a symmetry of the physical observables" | SM:96; Sub:274 ("a proper subgroup of all permutations") | the uniform permutations σ of ℤ/q that are exact symmetries of the second-order update: σ(f(v) − y) = f(σv) − σ(y) for all v, y | **yes, exactly.** P1's uniform symmetry group is precisely {x ↦ λx + c}, the same group as the linear rule's; P1 does not enlarge it | [A] (below); [X: rv2 R3 (d = 3, q = 5, 7); r3 K4 (d = 2, q = 7; d = 3, q = 2)] |

*GA9, paper argument [A].*
- Fix v and put w = f(v). The symmetry condition says σ(w − y) + σ(y) = f(σv) for every y. Setting
  y = 0 gives σ(w − y) + σ(y) = σ(w) + σ(0).
- f takes every value of ℤ/q. At prime q ≥ 5 (d = 3) and at q = 7 (d = 2), f(c𝟙) = 2c and 2 is a
  unit. At d = 3, q = 2, f takes both values.
- So τ = σ − σ(0) satisfies τ(w − y) + τ(y) = τ(w) for all w, y, that is, τ is additive. An additive
  bijection of ℤ/q is x ↦ λx with λ a unit, so σ = λx + σ(0).
- Conversely, each x ↦ λx + c is a symmetry, by (R-uni) with κ = 2:
  λ(f(v) − y) + c = (λf(v) + 2c) − (λy + c).
- The argument needs only that f is onto and uniformly covariant. GA9 therefore does not
  discriminate affine from non-affine rules.

**Gauge statements that place no condition on the rule.**
1. Whether the q-size gauge entails amplitude-scale gauge. It is open at SM:96, Sub:100 and Sub:104,
   and answered in the negative at Sub:274 and Structure:301 (F-7).
2. Theorem 24's generators other than (ii) (Sub:251–266).
   - (i), hidden-sector relabelling, holds for every φ, by conjugation with 𝟙_V ⊗ P_σ.
   - (iii), finite decoupled ancillary enlargement, holds for every φ, with product dynamics U ⊗ W.
   - (iv) is "a structural graph comparison, not a family of 𝒢_sub".
   - None conditions F. Generator (ii) is GA8.
3. The master principle "observationally indistinguishable transformations are gauge" (Sub:270;
   ch05:45 = FULL:1363). It classifies transformations. Applied to the amplitude maps it gives GA1,
   GA2 and GA9.
4. SM:585 and SM:811. The additive-automorphism gauge constrains the gauge *map*: the induced
   connection must be a homomorphism of the additive ℤ/q structure. It does not constrain the update.
   SM:811's "not arbitrary relabellings of ℤ/qℤ" is an F7 scope point (§2.3.1).
5. Amplitude-scale gauge in the reduction to SU(3) × SU(2) × U(1), where the global rescaling removes
   the common phase. Sites: Sub:163; SM:344, :374; ch02:102; ch03:74; ch05:17, :125, :129, :143,
   :190, :192; ch06:8; appendix-c:289; and their FULL mirrors. None conditions F, and none makes an
   affine claim.

**The test, per site.** A narrowing or correction is proposed for a site only if P1's class
satisfies every gauge assumption the site states, so that P1 is a counterexample to the statement
as made.
- **A6.** A site states A6 when its statement sits in the list of structural assumptions A1–A6, or
  names A1–A6 in the same sentence. The list is headed "restrictions on the class of candidate
  substrates" (Sub:90) and "six properties" (ch02:74). For A6 the reading is the interface as the
  corpus writes it (GA7-cov). GA7-α and GA7-β are shown for comparison.
- **GA4** is not an assumption of any overstating site.
- **Other readings of the test** (§6 Q1(b)):
  - corpus-wide, under which no narrowing passes (GA4 fails by construction; GA8 is undetermined);
  - clause-wise, under which only the assumptions stated in the clause that carries the claim count.
    This changes the verdict at Structure:219 only.

| Site (`.tex` mirror) | Gauge assumptions stated | A6 stated? P1 under A6 | All satisfied? | Disposition (no edit made) |
|---|---|---|---|---|
| Sub:100 (Substratum.tex:743–752) | GA2; the q-size entailment is stated as open | **yes**: A5 in the A1–A6 list, with A6 at Sub:102. GA7-cov: outside the domain. GA7-α: excluded. GA7-β: satisfied | **no**, under the written interface | **No narrowing (r2 proposal withdrawn).** Not refuted; its gauge route is recovered conditionally on GA7-α (§2.4). P1 does not contradict the clause "non-affine alternatives are excluded precisely to the extent amplitude-scale gauge is assumed". Under GA7-α the clause holds in both directions for q ≥ 3: link-sum rules that satisfy A1–A4 and are not affine exist, e.g. the centre-free isotropic Σ_j x_j², and they are excluded exactly when uniform shift gauge is imposed (§2.4). At q = 2 every map ℤ/2 → ℤ/2 is affine, so every link sum is affine (Σ_j x_j² = Σ_j x_j) and the clause holds in one direction only [A; X: rv3 V1 (n = 1); r4 C1]. Under the interface as typed, with additive links, it holds in one direction only, because the typing excludes non-affine rules whether or not gauge is assumed (G1). Under GA7-β both clauses would need the base-point qualifier (§2.4 item 4) |
| Sub:104 (Substratum.tex:783–785) | GA2 | **yes**: "A1–A6 jointly", same sentence | **no** | **No narrowing (withdrawn).** Not refuted. Its route "via the linearity-equivalence lemma" (uniform gauge plus link sum ⇒ base-point form ⇒ affine) holds conditionally on GA7-α. Under the written interface the conclusion holds by typing and gauge is idle (G1) |
| Sub:220 (Substratum.tex:1407–1410) | GA2 | **yes**: a bullet of the *Remark (Hypothesis dependencies)* on A1–A6 (Sub:214–221); A6 is the next bullet | **no** | **No narrowing (withdrawn).** Not refuted; its gauge route is recovered conditionally on GA7-α. Under GA7-α and q ≥ 3, non-affine link-sum rules are admitted exactly when uniform gauge is dropped (at q = 2 there are none). Under the interface as typed, the "exactly when" holds in one direction only (G1) |
| ch02:84 = FULL:718 (FULL.tex:3312–3314) | GA2 | **yes**: A5 in the book's list of six structural assumptions (ch02:74); A6 at ch02:86 = FULL:720 | **no** | **No narrowing (withdrawn).** As Sub:100, including its clause "excluded exactly to the extent that input is assumed" |
| Structure:259 (Structure.tex:1144–1145) | GA2 via Main (vii); GA8 named among A1–A6's motivation | **yes**: A1–A6 listed in the same paragraph | **no** (A6; GA8 undetermined) | **None.** Not refuted under A6; its gauge route is conditional on GA7-α, as at Sub:104. Its citation of Main (vii) without the base-point qualifier is a citation-fidelity point independent of P1 (§6 Q1(c)) |
| Sub:270 (Substratum.tex:1719–1720) | GA3 ("amplitude-independent dispersion ⟺ affine dynamics") | no | reading (b): the ⟺ is the lemma, true. Reading (a): ⟹ fails for P1 | **None under reading (b)**, which the sentence's attribution to [SM §4.1] supports (§2.3.1). If the owner reads (a), a qualifier-only correction: replace "(amplitude-independent dispersion $\iff$ affine dynamics)" with "(base-point-independent first differences of the update $\iff$ affine dynamics)" |
| Sub:272 (Substratum.tex:1729–1732, :1733–1739) | GA2, GA3 | no: a Remark/Status note on amplitude-scale gauge after Theorem 24 | **yes** | **Corrections proposed:** four clauses are false (§2.3.1, F1–F3, F6) |
| Sub:274 (Substratum.tex:1762–1768, :1768–1773, :1776–1778) | GA2, GA9 | no: the formalization-status note | **yes** | **Corrections proposed:** two clauses are false for the uniform group (§2.3.1, F4–F5). Two more, "the strong reading … *overshoots*" (:1762–1768) and "a proper subgroup of all permutations" (:1771–1772), are false at q = 2, 3 independently of P1 (F7) |
| Structure:219 (Structure.tex:980–982) | GA2 and GA8 (same paragraph) | no | **no: GA8 undetermined** | **None under the per-site test.** Under the clause-wise test, "An affine rule is therefore forced *given* that operational principle" states GA2 only and would pass. The qualifier-only correction would then be "given that operational principle in the form that every first difference of the update is independent of its base point ([Main §4.5], item (vii))" (§6 Q1(b)) |
| Structure:301 (Structure.tex:1269–1271) | amplitude-scale gauge; GA8 | no | — | **None: no overstatement.** "OI's [SM §4.1] argument for an affine rule rests on amplitude-scale gauge" is accurate, because SM §4.1 (SM:240) states the base-point form |

SM:96 and SM:811 state no affine restriction to test against P1, so they have no row. Three of
their clauses are F7 scope points (§2.3.1).

#### 2.3.1 Sub:270–274: what is false under each reading, and the proposed corrections

*One reading for one phrase family.* Sub:270's "amplitude-independent dispersion" and Sub:272's
"amplitude-dependent emergent dispersion" are negations of each other within one Remark/Status
block, so one reading has to serve both. Write "response" for the single-slot first differences of
the update, which are the "dispersion" over ℤ/q.
- **(a) Absolute level.** The response does not change under uniform shifts of the background.
- **(b) Base point.** The response does not depend on the background state at all (GA4).
- A third, physical reading is dependence on the perturbation's own amplitude. It splits into the
  first two.
  - Its scale part is unit homogeneity, which P1 has about every uniform background (rv2 R6).
  - Its superposition part is base-point independence. Superposition fails about c,
    F(c + d₁ + d₂) − F(c + d₁) ≠ F(c + d₂) − F(c), exactly when the first difference along d₂
    depends on the base point (c + d₁ versus c).

**The sources support (b).** Sub:270 attaches the phrase to "the linearity equivalence of
[SM §4.1]". That result is stated in the base-point form: SM:240, and Sub:274's "all first
finite-differences … are base-point-independent iff the rule is affine".

| Clause | Under (a) | Under (b) |
|---|---|---|
| Sub:270: "amplitude-independent dispersion ⟺ affine dynamics" | ⟸ true; ⟹ **false** for P1's class, d = 2, 3 [A; X: r2 G1; rv2 R6] | true: it is the lemma [P; A] |
| Sub:272 parenthetical: "a non-affine F induces amplitude-dependent emergent dispersion" | **false** for P1's class, d = 2, 3 (same checks) | true for every non-affine F (the lemma, ⇐) |
| Sub:272 conclusion: "so 'absolute amplitude is unobservable' already presupposes an affine rule" | **false** with the antecedent read as (R-uni) (d = 2, 3) or as (R-rel) (every d). True only as (R-site), where it is affinity restated | the same |
| The inference from the parenthetical to the conclusion | the inference is valid, but the argument is unsound: its premise is false for P1, and so is the conclusion | **the inference is invalid.** Background dependence does not make the absolute amplitude observable. P1's response depends on the background, does not depend on the absolute level (rv2 R6; r2 G1), and every uniform x ↦ λx + c𝟙 is an exact symmetry (rv2 R2) |

The parenthetical's "which *is* observable" is neither proved nor refuted here.

*Sub:272's first sentence, by reading of the principle (R2-B2).*

| Clause | (R-rel) | (R-uni) | (R-site) |
|---|---|---|---|
| "the input (absolute amplitude is unobservable) is strictly weaker than the output (affine dynamics)" | true: it excludes nothing, so every rule satisfies it | **false**. At odd q the two are incomparable: affine rules with b ≠ 0 fail (R-uni) for every κ (λ = −1 forces b = 0; r3 K3), and P1 satisfies it (d = 2, 3). At q = 2 the comparative is true in the κ-general form: every affine rule satisfies the κ-general uniform form, and P1's q = 2 rule satisfies it without being affine; there only the "excludes" clause fails [X: rv3 V6; r4 C2]. In the κ = 2 form, the record's primary (R-uni), it holds at q = 2 only among affine rules with Σa even, which include the isotropic centre-free ones; the affine rule x₊ₓ fails it [X: r4 C2; rv4 W5; r5 S5]. The clause is stated for every q | **false**: the two are equivalent (lemma) |
| "a non-affine F on the same alphabet is a coherent object the principle *excludes*" | **false**: it excludes no rule | **false** for P1's class (d = 2, 3). It excludes some non-affine rules, e.g. (1/3)Σ + x₊ₓ² (rv2 R2c), but not every one | true |

Each reading falsifies at least one of the two clauses, so the pair is false under every reading.
Within the link-sum class (§2.4) the first clause is still false: there (R-uni) implies affinity. At
odd q affinity does not imply (R-uni), so the input is stronger than the output, not weaker; at
q = 2 every link sum is affine and satisfies the κ-general form, so the two coincide.

**What is false, stated narrowly.** The statements below use the reading the sources support:
reading (b) for the phrase, and the principle as Sub:270 and SM:96 state it, with uniform maps. Each
is scoped to d = 2, 3 and to centre-free nearest-neighbour rules outside the link-sum class. No
construction for d ≥ 4 is given.
- **F1.** Sub:272: "the input … is strictly weaker than the output (affine dynamics)". At odd q the
  two are incomparable. At q = 2 the comparative holds and only F2 fails; the clause is general in
  q, so it is false as stated.
- **F2.** Sub:272: "a non-affine F … is a coherent object the principle *excludes*". This holds for
  some non-affine F, not for every one.
- **F3.** Sub:272: "so "absolute amplitude is unobservable" already presupposes an affine rule". Its
  premise is true and does not support it.
- **F4.** Sub:274: "The principled object that delivers the affine restriction without overshooting
  is the additive-automorphism group". As uniform exact symmetries the group does not deliver it, and
  P1 does not enlarge the group (GA9). It delivers it only in the base-point form, where a shift at
  one site changes the update by an amount independent of the state. Only the shifts enter that
  form; the rescalings play no part in the affine restriction.
- **F5.** Sub:274: "'the alphabet's additive automorphisms are gauge' yields an affine rule as a
  certified theorem". False in the uniform reading. True, as the lemma, in the base-point form.
- **F6.** Sub:272, second sentence: "The one route that would make the affine restriction
  *unconditional* — deriving the unobservability of absolute amplitude from the observer
  architecture itself". The clause needs "absolute amplitude is unobservable ⇒ affine". In the
  uniform reading, derived unobservability would not make the affine restriction unconditional: for
  d = 2, 3 P1's class satisfies it and is not affine [A; X: P1; rv_p1 A–C; rv3 V5]. Under (R-rel)
  it is false at every d, since the principle then excludes no rule. It is true only under (R-site),
  where the principle is affinity restated, or under GA7-α, which Sub:272 does not state. After the
  second sentence's V1 below, the clause would also no longer connect to that sentence's
  conclusion, which concerns rules with exact uniform symmetries, not affine rules.
- Under reading (a) two more falsities hold: the ⟹ direction of Sub:270's ⟺, and F3's parenthetical
  premise.
- **F7 (scope; elementary, not a P1 finding).** Sub:274 and SM:96 call the additive-automorphism
  group x ↦ λx + c (λ a unit) "a proper subgroup of all permutations". On the alphabet ℤ/q that
  group has q·φ(q) elements, which equals q! exactly when q ≤ 3. At q = 2 and q = 3 every
  permutation of ℤ/q is of that form, so the clause is false there, and SM:96's "A nonlinear
  relabelling …" is vacuous [A; X: r4 C4]. On the kernel's six-component alphabet
  (ℤ/q)⁶ the affine group is proper at every q. A qualifier-only correction is "for $q \ge 4$" at
  Sub:274 (Substratum.tex:1771–1772) and SM:96 (SM.tex:717). It bears on no other finding here.

**Proposed corrections (none made).** Each comes in two variants.
- **V1** adds only qualifiers, or removes the false comparative. It puts no new negative claim into
  paper prose (REVIEW-1049-r2 N7).
- **V2** also states the uniform-form limitation. That is a new negative mathematical claim whose
  proof (§2.1; P1) is off `main`, so it would have to land on `main` with the edit (§A.42 item 2;
  §A.46 item 1).

*Sub:272, first sentence (F1, F2).*
- **V1.** Replace "the input (absolute amplitude is unobservable) is strictly weaker than the output
  (affine dynamics), and a non-affine $F$ on the same alphabet is a coherent object the principle
  *excludes* rather than presupposes" with "a non-affine $F$ on the same alphabet is a coherent
  object that the principle, in the base-point form of the linearity-equivalence lemma, *excludes*
  rather than presupposes". The sentence's opening, "Stated operationally it is *not* viciously
  circular:", is then supported by the remaining reason: the principle excludes a coherent object
  rather than presupposing it. That reason is true only because, in the base-point form, the
  principle is affinity restated. Whether that support is adequate is §6 Q1(d).
- **V2.** V1, followed by "; in its uniform form, with rescalings and shifts as exact symmetries of
  the dynamics, it is not implied by affine dynamics and, for $d=2,3$, does not exclude every
  non-affine $F$".

*Sub:272, second sentence (F3; the r2 parenthetical).*
- **V1.** Replace "(a non-affine $F$ induces amplitude-dependent emergent dispersion, which *is*
  observable), so "absolute amplitude is unobservable" already presupposes an affine rule" with "(a
  rule for which uniform rescalings and shifts are not exact symmetries of the dynamics
  distinguishes, in its evolution, states that differ only in absolute amplitude), so "absolute
  amplitude is unobservable" already presupposes a rule for which they are exact symmetries".
  - With "unobservable" read as dynamical indistinguishability, the new premise restates "not an
    exact symmetry", and the inference is valid.
  - The sentence frames "unobservable" as "what the embedded observer can resolve through the
    trace-out". Read that way, the inference also needs the step "distinguished by the dynamics ⇒
    resolvable by the observer". That step is open, and it is the question the Status note already
    flags for external review. So V1's inference is valid in the dynamical reading and conditional
    on that open step in the observer-resolution reading.
  - The verdict that the observer-architecture route is circular, and the rest of the paragraph,
    are unchanged.
- **V2.** V1, followed by ", a class that for $d=2,3$ contains non-affine rules".

*Sub:272, second sentence, opening clause (F6).*
- **V1.** Replace "The one route that would make the affine restriction *unconditional*" with "The
  one route that would make the principle itself *unconditional*". This is the smallest change, and
  it agrees with V1's new conclusion for the same sentence, which concerns rules with exact uniform
  symmetries. It is also what the paragraph's last sentence concludes: amplitude-scale gauge "has
  the status of an operational input …, not a theorem".
- **V2.** V1, with "— deriving the unobservability of absolute amplitude from the observer
  architecture itself, which for $d=2,3$ would not by itself make the affine restriction
  unconditional —" in place of the dash clause. Like the other V2 texts, this adds a new negative
  claim whose proof is off `main`.
- The alternative, keeping "the affine restriction" and reading "unobservability" in the base-point
  form (REVIEW-1049-r3 §3.3 option (β)), is not taken. The sentence's conclusion would then also
  have to be in base-point form, and "states that differ only in absolute amplitude" is not a
  base-point notion.

*Which reading each sentence of the corrected paragraph uses (V1 throughout).*
- The first sentence uses the base-point form: "the principle, in the base-point form of the
  linearity-equivalence lemma, *excludes*".
- The second sentence uses uniform symmetries: "the principle itself", and "a rule for which
  [uniform rescalings and shifts] are exact symmetries".
- The third sentence ("an operational input …, not a theorem") is about the principle as Sub:270
  states it, with uniform maps.
- Each sentence names its form in its own text, so the paragraph says which it uses, and no further
  text is proposed. The cost of the mix (REVIEW-1049-r3 N6) is that the opening "Stated
  operationally it is *not* viciously circular" is then supported by the base-point form, which is
  affinity restated rather than the operational statement (§6 Q1(d)).
- **r2's parenthetical is withdrawn.** It read "a non-affine $F$ can induce background-dependent
  emergent dispersion, which *is* observable", and it did not support its own conclusion: P1 has
  background-dependent dispersion and is uniformly covariant (REVIEW-1049-r2 R2-B1).

*Sub:274 (F4, F5).*
- **V1, part (i).** Replace "The principled object that delivers the affine restriction without
  overshooting is the **additive-automorphism** group $x \mapsto \lambda x + c$ ($\lambda$ a unit)"
  with "The principled object that delivers the affine restriction without overshooting is the
  **additive-automorphism** group $x \mapsto \lambda x + c$ ($\lambda$ a unit), taken in the
  base-point form of the linearity-equivalence lemma, in which a shift at one site changes the
  update by an amount independent of the state".
- **V1, part (ii).** Replace "yields an affine rule as a certified theorem" with "yields, in that
  base-point form, an affine rule as a certified theorem".
- **V2.** V1, with "; as exact uniform symmetries of the dynamics the same automorphisms do not yield
  it for $d=2,3$" after part (ii).
- **V1′ (subject-changing; REVIEW-1049-r3 N6).** Replace the whole sentence "The principled object
  that delivers the affine restriction without overshooting is the **additive-automorphism** group
  $x \mapsto \lambda x + c$ ($\lambda$ a unit) — a proper subgroup of all permutations that preserves
  the alphabet's "+", hence the dispersion." (Substratum.tex:1768–1773) with "The principled
  condition that delivers the affine restriction without overshooting is that a shift at one site
  changes the update by an amount independent of the state (the base-point form of the
  linearity-equivalence lemma); the **additive-automorphism** group $x \mapsto \lambda x + c$
  ($\lambda$ a unit) is, for $q \ge 4$, a proper subgroup of all permutations, and it preserves the
  alphabet's "+", hence the dispersion." Part (ii) is then V1's part (ii), whose "that base-point
  form" now refers to the condition.
  - V1′ states what delivers the restriction instead of narrowing what does not. It adds no
    negative claim about the uniform group.
  - "for $q \ge 4$" is F7's qualifier. Without it V1′ would restate a clause that is false at
    q = 2, 3.
  - Under V1 and V1′ alike, "the more primitive and better-motivated assumption" (Substratum.tex:1776)
    and "relocates the irreducible assumption … to a more primitive and more defensible place"
    (:1781–1783) attach to a condition equivalent to affinity. That is an evaluative point, not a
    mathematical falsity, and it is put to the owner (§6 Q1(d)).

*Why V1 is a correction and not merely a qualification.*
- Each qualifier sits inside the false clause and changes what the clause asserts. At Sub:274, for
  example, the subject changes from the uniform group to its base-point form.
- No false statement survives, and nothing is asserted and then disclaimed (§A.30).
- At Sub:272 the false comparative is removed, not qualified. In F6's clause the subject changes from
  the affine restriction to the principle itself.
- These are the smallest changes that make each clause true. Whether the owner reads V1 as a
  "narrowly scoped correction" in the sense of the direction is §6 Q1(d).

*Requirements of any edit.* The register is that of §A.32–§A.33 for `papers/`. Any edit needs owner
authorization, propagation to the `.tex` and `.pdf` derivatives (§A.25 step 5) and review. No book
passage restates these clauses (§2.1). None of this is authorized here.

### 2.4 Theorem recovery before concession: the affine claim in the link-sum class

**The claim, and why this note comes first.** The claim is "amplitude-scale gauge restricts the
update to an affine one". It is made at Sub:100, :104, :220, ch02:84 = FULL:718 and Structure:259
among A1–A6, and at Sub:272, :274 and Structure:219 for the gauge principle alone. P1 refutes it
among all centre-free nearest-neighbour rules in d = 2, 3 (§2.1). Under the Code Review Rules
(theorem recovery before concession), this note comes before any narrowing. It records the strongest
result that survives, its hypotheses, whether those hypotheses are the corpus's own, and the precise
gap.

**1. Strongest existing results.**
- **(E1) The lemma.** Base-point form ⟺ affine [P Sub:274; A]. It holds for every q and every
  finite arity.
- **(E2) Kernel.**
  - Every link-coupled carrier with additive links satisfies the kernel's A5, additivity of F
    (`A6Instantiation.linkSubstratum_A5`) [K].
  - A6-cov restricts no link-coupled rule (`a6cov_all`, D3-a) [K].
  - So, for rules with A6's interface as formalized, linearity and hence affinity hold by the
    interface's typing, and the gauge principle is not used.
- **(E3) Proposition (link-sum recovery) [A].** Let F_i(x) = Σ_{j∈N(i)} m_ij(x_j) with arbitrary
  maps m_ij : ℤ/q → ℤ/q, for any q ≥ 2, any finite neighbourhoods and any d. Suppose that for every
  c the difference F(x + c𝟙) − F(x) does not depend on x. Then every m_ij is affine, so F is affine.
  - Only uniform shifts are used (λ = 1). No value of κ is assumed, and rescalings are not needed.
  - *Proof.* Fix i and k ∈ N(i). In Σ_j [m_ij(x_j + c) − m_ij(x_j)] = h_i(c), vary x_k alone: this
    shows that m_ik(x_k + c) − m_ik(x_k) does not depend on x_k. By the one-variable case of the
    lemma, m_ik is affine. (Telescoping with c = 1 gives m(x) = m(0) + x·(m(1) − m(0)), which is
    consistent on ℤ/q because q·(m(1) − m(0)) ≡ 0.) ∎ The argument is REVIEW-1049-r2 §3.5's,
    stated here without the κ = 2 restriction.
  - *Verification [X].* rv2 R4 checks the κ = 2 form: 2 slots at q = 2, 3, 4, and 3 slots at
    q = 3. r3 K2 checks the case of any state-independent shift effect: 2 slots at q = 2, 3, 4, and
    3 slots at q = 2, 3. In K2 every solution is affine, and the solutions are exactly the affine
    separable maps: (q²)^slots = 16, 81, 256, 64 and 729. Countercontrol: 2x₁ + (x₂ − x₁)² at
    q = 3 is shift-covariant, not a link sum and not affine (r3 K2), so separability is
    load-bearing.
  - *Corollary [A].* Under the same hypothesis, each single-slot difference is
    m_ik(x_k + c) − m_ik(x_k), which, as just shown, does not depend on the state. So F has the site-wise
    base-point form. In the link-sum class with link maps not assumed additive (GA7-α), the route
    that Sub:100 and Sub:104 name — uniform gauge ⇒ base-point form ⇒ affine (lemma) — holds as
    stated.
  - *Converse [A].* Every affine F is a link sum. So among rules whose uniform-shift effect does not
    depend on the state, link-separability is **equivalent** to affinity.
- **P1's class is outside the link-sum class.** Each construction has a nonzero mixed second
  difference between two neighbour slots: r3 K1 (d = 3 at q = 2, 5, 7; d = 2 at q = 7) and rv2 R4
  (d = 3, q = 5).

**2. Is the link sum the corpus's intended reading of A6?** The sources at `fd539e15`:
- A6's content is its interface.
  - Sub:102 and ch02:86 = FULL:720: "The content of the assumption is this covariant interface —
    the coupling is link-valued data on which the transformations act".
  - Main:726 (xii): A6 "fixes the interface through which the gauge symmetry is read locally".
  - Kernel D3-a: "its content is the interface, not a constraint".
- Everywhere the corpus writes the interface out, it is a link sum with linear links.
  - Substratum level: the kernel's `linkF N M c i = ∑ j ∈ N i, M i j (c j)`, with `M i j : V →+ V`,
    instantiated by `A6Instantiation.linkRule` and `linkSubstratum` at the alphabet
    `Fin 6 → ZMod q`.
  - Prose: the transformation law of the matrix link M(n, ê_j) (SM:116; Sub:102), and SM:312–314's
    general and isotropic linear updates, e.g. φ(n, t+1) = (1/d) M Σ_j [φ(n + ê_j, t) +
    φ(n − ê_j, t)] − φ(n, t−1). SM:312 states these "on the observer-level branch …, not the
    ℤ/qℤ alphabet of the substratum", so the substratum-level written instance is the kernel's.
  - Q3: "The corpus links are matrices (SM:116, SM:523)". A5 D14: additivity "is built into the
    carrier's type".
- No source writes the interface for non-additive link maps, either as a link sum or by joint
  insertion (§2.1 search scope). Q3 finds "Corpus: none" for relaxing the typing even to affine maps.
- "Imposes no restriction on the rule" (Sub:102; Main (xii)) is scoped in the kernel to rules that
  already have the interface: A6-cov "restricts no link-coupled rule" (D3-a). r2's GA7 verdict read
  it as admitting every rule. The kernel's own scope does not support that reading.
- The kernel module adopts no reading of A6 ("No reading is 'the' A6").

**Assessment.**
- The written interface is the link sum. The joint-insertion form (GA7-β) is written nowhere.
- So at the sites that state the affine restriction among A1–A6, P1's class is in one of two
  positions:
  - *excluded by A6*, if the interface is a condition on candidate rules, which is what Sub:90 says
    of all six assumptions; or
  - *outside A6's domain*, if the interface only describes how gauge is read on rules that have it.
- In neither case is P1 a counterexample to those sites' statements as made.
- A vacuous-conditional reading — A6 as "if a rule carries link data, it is covariant", which P1,
  carrying none, would satisfy vacuously — is not the written one. Sub:102 and
  ch02:86 = FULL:720 assert that "the coupling is link-valued data on which the transformations
  act". A rule with no link-valued coupling does not satisfy A6 as stated, so "outside A6's domain"
  does not mean "satisfies A6".
- **P1 is not a counterexample at Sub:100, :104, :220, ch02:84 = FULL:718 and Structure:259 under
  any written reading of A6, so r2's narrowings at Sub:100, :104, :220 and ch02:84 = FULL:718 are
  withdrawn. The sites' attribution of the affine part to amplitude-scale gauge "via the
  linearity-equivalence lemma" holds in the link-sum class with link maps not assumed additive
  (GA7-α, which the corpus does not state; E3). Under the interface as written, with additive links, the conclusion holds by
  typing, the gauge principle is idle, and the "precisely to the extent" and "exactly when" clauses
  hold in one direction only (G1). The claim is therefore not refuted, and conditionally recovered.
  Which reading applies is §6 Q2.**

**3. The precise remaining gap.**
- **(G1) Additive typing.**
  - With the interface typed as the corpus types it, with additive links, the rule is linear by type
    (E2) and the gauge principle does no work.
  - The sites attribute the affine part to amplitude-scale gauge "via the linearity-equivalence
    lemma". That attribution holds only when the link maps are not assumed additive (E3), an
    extension the corpus does not state.
  - If the typed interface is a condition on rules, A5 follows from A6's typing. That sits badly
    with "the further restriction to linear is imposed" (Sub:100) and with "imposes no further
    condition on the rule" (Sub:102).
  - It also leaves two clauses true in one direction only. Dropping gauge would admit no non-affine
    rule either. The two clauses are Sub:100's and ch02:84 = FULL:718's "excluded precisely (exactly)
    to the extent [gauge] is assumed", and Sub:220's "exactly when that gauge principle is dropped".
    Under GA7-α both directions hold for q ≥ 3. At q = 2 every map ℤ/2 → ℤ/2 is affine, so every
    link sum is affine and the clauses hold one way there too [A; X: rv3 V1; r4 C1].
  - This is not a P1 counterexample, and no correction is proposed for it. It is part of O-G (§6 Q2).
  - This is A5 N9's assumption-watch marker ("additivity relocated to the links"), seen from the
    affine side.
- **(G2) Warrant.**
  - Among uniformly shift-covariant rules, link-separability is equivalent to affinity (the converse
    above).
  - So the recovery moves the affine premise into the interface. It derives affinity from gauge only
    if link-separability has independent warrant (§A.29).
  - The corpus offers none beyond the link sum's being the form of the linear wave equation.
- **(G3) Sites not recovered.** Sub:272, Sub:274 and Structure:219 state the gauge principle without
  A6, and E3 does not reach them. Their dispositions in §2.3 stand.
- **(G4) Scope.**
  - E3 concerns the update F of the second-order form, with per-link maps.
  - A centre read would be one more slot and is covered, but A4 excludes it.
  - Rules whose links carry state-dependent data are not covered, for example G_SM's switched graph.
  - E3 is proved for K = 1. The same paper proof holds for link maps A → A on any abelian group A,
    including the kernel carrier's (ℤ/q)^K, provided the shifts range over every c ∈ A [A; X: rv3 V2,
    q = 2, 3]. Diagonal shifts c(1, …, 1) alone do not suffice: at q = 3, K = 2 the link map
    x ↦ ((x₁ − x₂)², 0) is not affine and is unchanged by every diagonal shift [A; X: rv3 V2; r4 C3].
    Which shifts the amplitude gauge includes on a K-component carrier is not settled here.

**4. Contingent text if the owner reads A6 by joint insertion (GA7-β).**
- Under GA7-β, P1 satisfies every stated assumption at Sub:100, :104, :220 and ch02:84 = FULL:718,
  A6 included (weakly, at K = 1), so narrowings would pass.
- They would then have to cover every contradicted clause of each passage (REVIEW-1049-r2 R2-B2).
  The qualifier-only texts would be:
  - **Sub:100.** Three clauses.
    - After "restricts the update to an affine one via the linearity-equivalence lemma of
      [SM §4.1]", add "when it is taken in the base-point form of that lemma".
    - "its affine part is necessary *given* that gauge principle in that form".
    - "non-affine alternatives are excluded precisely to the extent amplitude-scale gauge is assumed
      in that form".
  - **ch02:84 = FULL:718.** Two clauses, with the same edit in both parallel sources (§A.14).
    - After "restricts the rule to an affine one", add "in the form that the update's first
      differences do not depend on the base point".
    - "excluded exactly to the extent that input is assumed in that form".
  - **Sub:104.** One clause. After "via the linearity-equivalence lemma of [SM §4.1]", add "when it
    is taken in the base-point form of that lemma".
  - **Sub:220.** Two clauses.
    - "restricts the rule to an affine one in the base-point form of the linearity-equivalence lemma
      ([SM §4.1])".
    - "exactly when that gauge principle, in that form, is dropped".
- None of these is proposed unless the owner adopts GA7-β (§6 Q2).

**Labels.** The kernel results are [K]. E3, its corollary and its converse are [A], with [X]
controls. The reading assessment is [P], with the sources quoted. The recovery is a favourable
branch and is pressure-tested in §7, item 7.

***

## 3. Question 2 — downstream dependence

**Columns.**
- **Uses:** what the result actually consumes. B is the bipartite, centre-free read pattern with
  the second-order form. AFF is affinity. b0 is b = 0.
- **Without linearity:** affine dynamics, b ≠ 0.
- **Without affinity:** non-affine dynamics.

Rows 1–14 are the results examined in r1. Rows D7, D12, D13 and D15 are A5's dependency-inventory
rows that r1 omitted. Every statement is about the configuration-level update; where a row concerns
an encoded carrier (QP's encoded S, the J-complex carrier), that is said.

| # | Result | Uses | Without linearity (affine, b ≠ 0) | Without affinity | Support |
|---|---|---|---|---|---|
| 1 | Form lemma; dispersion; Theorem 4; Lorentz (SM:224–232) | AFF (linear part) | Form plus a constant. A uniform offset sources only k = 0; the non-uniform modes obey the linear equation exactly | No global operator. The linearization depends on the background: on the absolute value for G_SM-type rules, on gradients only for P1-type rules | [A]; A5 Prop. 2.5 re-derived |
| 2 | SM chirality: Theorems 3, 12, 13; SM:539 ("nearest-neighbor, so … bipartite"); SM:569 (ΓAΓ = −A) | B plus the linear part | Unchanged: these are identities of the linear operator A and its Schur complement. Γ carries the rule (A, b𝟙) to (−A, bε), just as it carries A to −A at b = 0 | Over the real lift, the Jacobian of an NN centre-free rule keeps the NN pattern at every background, so each linearization stays graded [D]. Not examined over ℤ/q. All of this sits behind the SM:232 / SM:306 bridges | [A]; [D] |
| 3a | QP Lemma G1, sector split | B only | Holds modulo constants: each slot is a single-type linear form plus a constant [A] | **The functional split holds for any NN centre-free rule that reads only opposite-colour sites on a bipartite graph:** each slot is a function of one sector's variables. The induction does not use linearity. It fails only when a rule reads its own site or a same-colour site (the contrapositive of the induction) | [A] |
| 3b | QP Lemma G2 (non-adaptive quarter-phase obstruction, an encoded-carrier statement) | B plus AFF (step 3: R1 and R0 differ by a map linear in the state, QP:362–369) | Holds: common offsets cancel from the difference of two runs, Φᵗz − Φᵗz′ = Lᵗ(z − z′) (B0.1). G2's class already contains supplied constant translations. (QP node 9 and PROOF-RECOVERY §5, that the available t₋ₐ cancels a fixed coupling offset and recovers L, are a separate-availability fact, cited as context only) | Not examined. Step 3's identity is not available | [A] |
| 3c | QP Lemma Q(i), conservation of Q = Σ uᵢvᵢ at q = 2 | b0 | **Fails:** Q(step z) = Q(z) + b·u exactly [A; X: P2(B), exhaustive for n = 3, 4; rv_p2]. A uniform b = 1 (the complement rule) breaks it | — (MECH-2 and M-INACC already record that it fails for G_SM) | [A]; [X] |
| 3d | QP Lemma Q(iii), the Q* = 0 protection | the linear part (symplectic) | Holds. QP's own proof treats each branch as "symplectic center-free steps and constant translations", and "translations change values, not which functionals are determined" (QP node 6) | Fails for G_σ (M-INACC RESULT §0, [P] record); G_σ reads i ± 2 | [P]; [A] |
| 4 | #1211 J (BRIDGE F4, NQ1), a mathematically available complex structure, not an operation derived from OI | the linear part, on the difference space | **Independent of b:** Φᵗz − Φᵗz′ = Lᵗ(z − z′) (B0.1 re-derived), so J commutes with Φ's action on differences wherever it commutes with L. The uniform offset's non-removable effect lies in the k = 0 sector, which at α = 1/d is a null mode where no J exists for b = 0 either. At the staggered null mode an offset is removable, and J is absent anyway | A tangent action that depends on the background. Any J would then also depend on the background. Not examined | [A] |
| 4′ | NQ1(b), whether Σ is J-Hermitian | depends on what Σ is | A centred covariance does not depend on b. A raw second moment ⟨φφ†⟩ picks up the A₁, k = 0 drift (H-b; bt²/2 at resonance) | — | [A] |
| 5 | Stage 2(d) and Theorem 5 (Q4) | b0 under (A-lin) | Q4 outcome (iii) for O1–O4: U(1)_S is lost, and G_v reproduces O1–O4 at group level only. Carrier-level agreement is conditional. O5 is open | — | [P] record |
| 6 | A6 extension (Q3) | — | Outcome (N): none of E1–E3 is justified | — | [P] record |
| 7 | #1210 SA-1(a) (SHARED r5 §9: column (ii) "yes, conditional on Substratum (A4)–(A5)") | AFF plus the form, symmetric coefficients and symplecticity | Unchanged. AP1's backaction identity treats a known displacement as no disturbance, and a native offset is a known displacement | Outside SA-1(a)'s class | [H]; [A] |
| 8 | #1210 QX4 A4.1, affine-symplectic LG bounds (`K₃ ≤ 1` scan, `K₃ = 2` witness) | AFF (stated "with translations") | Unchanged by construction | Outside scope | [H] |
| 9 | #1210 QX3 routing (A3.1) | — | Affine routing exists under `NCONS_ready` | Required under `NCONS_global` | [H]; core lemma [A] |
| 10 | M15 reciprocity | AFF (symplectic linear part) | Unchanged | Can fail: G_SM is not reciprocal | [H]; [P] MECH-2 |
| 11 | Main's interface: the absolute labelled readouts of the Q1 baseline | b0 | Labels differ by p_V(t) (A5 Thm 2.2). At prime q, when κ ≢ 2 the shift is static (uniform-shift conjugacy), and when κ ≡ 2 it can be time-dependent, with invariant content such as #Fix = 0 for S1 | — | A5 B0.2/B0.3 re-derived [A] |
| 12 | Main:726 (v): quadratic invariant and energy shells; D5, D6 | b0 | Q′ = Q − b(S_t + S_{t−1}) replaces Q. The shells differ | — | A5 N4 |
| 13 | Main §3.4 representation; C4 | none | Unchanged | Unchanged | [P] |
| 14 | Bijectivity; P-indivisibility (SM:106, :112) | second-order form only | Unchanged | Unchanged | [P] |
| D7 | SM:92, Theorem A.1 (period qL of the wave map on a ring) | the linear wave map | Not examined (A5: "Not transferred, and not examined") | — | [P] A5 row D7 |
| D12 | `StochasticInterface` gap (kernel) | A5 as hypothesis (b0 as the kernel statement stands) | A5 Proposition B3.1 extends the conclusion to uniform-offset affine rules by another route: [D] in A5, unreviewed | — | [K] for A5; [D] extension |
| D13 | `HydroSourceAudit` advection gate (kernel) | A5 as hypothesis (b0 as the kernel statement stands) | A5 Proposition B3.4: an affine closure is degree ≤ 1 in n, [D] in A5, unreviewed | — | [K] for A5; [D] extension |
| D15 | SM:1416, Layer 2 candidate classes, "linear dynamics (A5)" | b0 (A5 as stated) | Conditional on A5 as stated | — | [P] A5 row D15 |

**3.1 Reading of the table (among the rows examined).**
- **b = 0 is used at rows 3c, 5, 11, 12, D12, D13 and D15, and at the raw-moment reading of 4′.**
  At D12 and D13 that is the kernel statements as they stand; their affine extensions are
  unreviewed [D]. Row D7 is not examined.
- **Affinity is used at rows 1, 2, 3b, 3d, 4, 7, 8 and 10.**
- **Row 3a uses neither.**
- This is a classification of the rows listed, not of every result in the corpus that uses A5.

**3.2 The premise the quarter-phase obstruction shares with SM chirality.**
- **The claim at r1's reading.** BRIDGE r2 §0 item 6 [H] listed linearity among the premises the
  quarter-phase obstruction shares with SM chirality. That is literally true of QP's stated class N,
  which is linear. BRIDGE r3 [H] (§0 item 6, §10) now names the bipartite, centre-free read pattern,
  not linearity, with its own check K1. The analysis below agrees and is independent of it.
- **What the obstruction uses.** On rows 2, 3a and 3b, the shared premise is the bipartite,
  centre-free read pattern with the second-order form. Lemma G2 additionally uses affinity.
  Linearity beyond affine is used by neither.
- **Where the sector split fails.** It fails only when a rule reads its own site or a same-colour
  site. This is the contrapositive of the [A] induction (row 3a).
- **Bearing on MECH-2:532.** MECH-2:532 reads "That exclusion does not carry over to `G_SM`, whose
  nonlinearity breaks the grading". It attributes to nonlinearity what, under product priors,
  requires the same-colour read: in G_SM's closed form f_i = u_{i−1} ⊕ (u_{i+1} ∨ u_{i+2}) (MECH-2:40)
  the non-affinity and the i+2 read are the same term, and by the induction above nonlinearity alone
  keeps the sector split. A linear rule with an i+2 read can also determine a mixed functional.
- **Argument [A].** Under the functional split, every record is a function of one sector's variables.
  With a prior that factorizes across sectors (N2), the conditional support is then a product set.
  On a product set a mixed functional z + x is constant only if z and x are each constant. So the
  support {01, 10} of P★ needs a slot that mixes sectors.
- **Scope.** This holds for priors that factorize across sectors; P★'s prior does (MECH-2 node 6).
  H-PREP preparations that correlate the sectors are not covered.

**3.3 Where b = 0 does work in the dynamical rows: one sector.**
- **The sector.** At prime q, the content of a uniform offset that no static uniform relabelling
  removes is confined to the uniform mode of the zero-mode locus κ ≡ 2 (mod q). For odd q with
  gcd(d, q) = 1 this is α ≡ 1/d; at d = 3, q = 3 the locus κ ≡ 2 is empty; at q = 2, κ ≡ 2 holds for
  every α (B0.3(b)–(c), re-derived [A]). On the real lift the same mode is the k = 0 mode. It is the
  mode of secular growth bt²/2, and at α = 1/d it is a null mode where no J exists (row 4). With the
  internal index and H-b, the offset lies in A₁ (Q4 N0).
- **One question in four places:**
  - #1049's resonance locus (A5 R3);
  - Q4c ("Is the A₁ block resonant (μ_{A₁} = 1) on the maintained branch?");
  - #1211 NQ1(a) (the null modes at α = 1/d: "excluded …, constrained, or the place where the
    complex structure fails");
  - SM:232's open question of whether α = 1/d belongs to the substratum or to the observer level.
- **What turns on it.** Off this sector, b ≠ 0 is a static uniform relabelling, for which owner Q2
  is "a mathematical relabelling". On it, b ≠ 0 has invariant content: no fixed point (S1), secular
  drift, and the loss of the singlet U(1)'s linear part under (A-lin).
- **Scope.** This locates the b = 0 content of rows 3c, 5, 11, 12 and 4′. Rows D12, D13 and D15 are
  statements made under A5 as stated; whether their b = 0 use reduces to this sector depends on the
  unreviewed [D] extensions.

***

## 4. What is open on #1049 now

**O-A. The affine part has no derivation from the gauge principle alone.**
- Its status is a posit in the site-wise base-point form (§2.1). Among centre-free
  nearest-neighbour rules, non-affine rules in d = 2 and d = 3 satisfy the uniform operational form.
- Among link-sum rules with link maps not assumed additive (GA7-α) the uniform form does entail
  affinity (§2.4, E3). But there link-separability is equivalent to affinity, so the premise is
  relocated, not removed (G2).
- This is new relative to A5, which scoped non-affine rules out.
  - At the A1–A6 sites (Sub:100, :104, :220; ch02:84 = FULL:718; Structure:259) the claim is not
    refuted: under every written form of A6's interface P1's rules are not candidate rules (§2.4).
    The "partly derived" route through gauge is recovered only conditionally, on GA7-α, which the
    corpus does not state. Under the written, additive interface the affine part holds by typing and
    the attribution to gauge is idle (G1). Gap G2 applies in either case.
  - At Sub:272 and Sub:274, which state the gauge principle alone, corrections are proposed
    (§2.3.1).
- Owner questions 1 and 2 (§6) ask how to record it.
- It is not a refutation of affinity. It is the absence of an entailment from the gauge principle
  alone.

**O-B. Linear over affine.**
- Criterion 1 is not reached (R5; Q3 (N); today's drafts add nothing).
- Criterion 2 is reached for 𝒜_W and 𝒜_C (A5 R6).
- At the owner's absolute baseline (Q1), the open residue is the resonant uniform sector of §3.3.
  Off it, the equivalence is a static relabelling at prime q.

**O-C. Three open items from the earlier units:**
- Stage 2(d) O5 (Q4-8), not authorized;
- Q4a (does E4 apply to the offset?);
- Q4b (whether the stabilizer is taken with respect to the rule or the coupling).
Q3 is closed with outcome (N).

**O-D. Conditional status of today's conditional results.**
- These depend on affinity, not on linearity:
  - #1210's SA-1(a) column (ii) and the affine-symplectic bounds;
  - Lemma G2;
  - SM's chirality identities (as identities of the linear part);
  - #1211's J.
- Each is therefore conditional on the affine restriction, not on A5's linear clause.
- SHARED r5 §9 gives SA-1(a) column (ii) as "yes, conditional on Substratum (A4)–(A5)". It would read
  more precisely as: "conditional on A4, on the affine restriction (whose derivation from
  amplitude-scale gauge needs the site-wise base-point form, or a link-sum interface), and on the
  form, symmetric coefficients and symplecticity; linearity beyond affine not used".
- That is a proposal for #1210's writer. No #1210 file was edited.

**O-E. Pressure against affinity from the programme's own needs.** Three items: G_SM (SM:112),
in-world setting selection (MECH-1), and global-conservation routing (QX3, owner Q3-2). If any of
them is adopted, it needs a non-affine element. Under §A.29 that element must carry its own
independent justification.

**O-F. GA8 on P1's class.** Whether the alphabet-size hypothesis excludes P1's class is
undetermined (§2.3). It cannot be decided without the cross-q correspondence that SM:94 says is not
constructed. Until it is, no correction is proposed for Structure:219 under the per-site test.
Structure:259 is not refuted under A6, and Structure:301 makes no overstatement, so neither depends
on GA8.

**O-G. What A6's interface is, for non-additive rules.**
- The corpus writes A6's interface only with additive links (§2.4, item 2). Three questions are open:
  - whether that interface is a condition on candidate rules, or a description of the rules that
    have it;
  - whether it extends to non-additive link maps as a link sum (GA7-α);
  - or whether it extends by joint insertion (GA7-β).
- The answers decide where the affine restriction at the A1–A6 sites comes from:
  - under GA7-α it comes from gauge, through the link sum;
  - as typed, it comes from A6's typing alone (G1);
  - under GA7-β it is open again, and the contingent narrowings of §2.4 item 4 apply.
- This is the affine-side counterpart of A5 N9 and Q3, which concern b = 0.

***

## 5. Smallest decisive next paper question

**Q-NEXT.** *Is link-separability of the update — F_i = Σ_j m_ij(x_j), the link-sum form of A6's
interface, with the link maps not assumed additive — independently justified as a premise on every
candidate rule in d = 3? If it is not, does any other independently justified OI principle imply the
site-wise base-point form?*

**Link-separability first.** It is the one candidate already known to close the implication.
- With uniform shift gauge it implies affinity (§2.4, E3).
- It excludes P1's class (r3 K1).
- On the covariant class it is also necessary, since every affine rule is a link sum, so there it is
  equivalent to affinity.
- Its sufficiency is therefore settled, and the whole question is its warrant. The candidate warrant
  is A6's link-valued coupling (O-G): why each neighbour should contribute separately when the link
  maps are not additive.

**Other principles.** For any other principle, excluding P1's class is a **necessary condition** for
a positive answer, a cheap screen. It is not a sufficient one: P1's class is a set of witnesses, not
the complement of the affine class, so a principle that excludes it need not exclude every non-affine
rule. The principles to test are these:
- A1–A4, and A6 as stated (with O-G);
- E4;
- the trace-out interface of Main §1;
- amplitude-scale gauge in the owner's relabelling reading;
- the alphabet-size hypothesis (SM:94; Structure:219, :301) as a candidate, which first needs the
  cross-q correspondence SM:94 says is not constructed (O-F).

**Why it is decisive.**
- **A negative answer**, for link-separability and the rest, makes the affine part a posit at every
  site. It is located either in the base-point form (SM:240, Main (vii)) or in A6's interface (as
  typed). The "partly derived" wording becomes a #1029 item.
- **A positive answer for link-separability** makes the affine claim at the A1–A6 sites a
  consequence of gauge together with an independently warranted interface. That premise is then
  judged under §A.29, which requires an independent prediction beyond affinity.
- **A positive answer for another principle** names a principle with a consequence beyond affinity,
  judged under §A.29 likewise.
- Either answer settles O-A and O-G. O-A is upstream of O-D and of rows 1, 2, 3b, 4, 7 and 8.

**Why it is small.**
- Link-separability is a question about the interface and its motivation. Its mathematics is
  already done (§2.4).
- For each other principle, the screen (does it exclude P1's class?) is a paper check on one family
  of witnesses. A principle that fails the screen gives a negative answer for that principle, shown
  by P1-type witnesses.
- A principle that passes the screen still has to be shown to imply the base-point form for every
  rule; the screen does not do that.
- No mechanism computation is needed.
- An optional exact generic control is to extend P1 to the alphabet-size correspondence, which is
  not constructed in SM:94. That control would need its own authorization.

**Companion question, for b = 0 (smaller, but conditional on an open bridge).** This is §3.3's
sector question: *on the branch the observer uses, is the uniform A₁ sector at k = 0 resonant (κ ≡ 2,
μ_{A₁} = 1) and accessible?* It merges Q4c with #1211 NQ1(a). Its answer is conditional on SM:232's
unproved φ → L_obs bridge, which is why it is second.

***

## 6. Questions for the owner

1. **The §2.3 dispositions (O-A).** Main (vii) and SM:240 carry the site-wise form.
   (a) **Sub:272 and Sub:274.** Should the corrections of §2.3.1 be recorded under #1029 as
       candidate corrections, pending review of P1? In which variant: V1, which uses qualifiers and
       removes the false comparative and adds no new negative claim to paper prose; or V2, which also
       states the uniform-form limitation and needs P1's proof to land on `main` with the edit?
       F7's "for $q \ge 4$" at Sub:274 and SM:96 does not depend on P1. Should it be recorded with
       them, or separately?
   (b) **The reading of the test.** It is applied per site here. A clause-wise reading would admit a
       V1 correction at Structure:219. A corpus-wide reading passes no narrowing (GA4 fails by
       construction; GA8 is undetermined).
   (c) **Structure:259** cites Main (vii) without its base-point qualifier. Restoring it is a
       citation-fidelity point that does not depend on P1. Should it be treated separately?
   (d) **V1 at Sub:274** puts the base-point qualifier inside the false clause, so that the clause is
       true. Is that a "narrowly scoped correction" in the sense of the direction? Or should the
       clause be rewritten to say what does deliver the restriction (V1′, §2.3.1)? A related point
       applies to both sites. After V1, the support left for three passages is true but hollow,
       because in the base-point form the principle is affinity restated:
       - Sub:272's opening, "Stated operationally it is *not* viciously circular", rests on the
         base-point form, which is not the operational statement;
       - Sub:274's "the more primitive and better-motivated assumption", and
       - Sub:274's "relocates the irreducible assumption … to a more primitive and more defensible
         place", which under V1 and V1′ attach to a condition equivalent to affinity.
       Should these stay, be reworded, or be removed? That is an editorial and evaluative decision.
       This unit proposes no text for it.
   No manuscript change is made by this unit.
2. **A6's interface (O-G; §2.4).** Is A6's link-coupled interface a condition on candidate rules? If
   so, P1's class is excluded and is no counterexample at the A1–A6 sites. Is it meant to extend
   to non-additive link maps as a link sum (GA7-α, under which gauge does the work), or by joint
   insertion (GA7-β, under which the narrowings of §2.4 item 4 return)? As typed in the kernel, with
   additive links, the interface makes the rule linear and the gauge principle does no work (G1).
3. **Sub:270.** Is reading (b) of "amplitude-independent dispersion" the intended one? The sentence's
   attribution to [SM §4.1] supports it, and under it no correction is needed at Sub:270. If not,
   the qualifier-only correction of §2.3 applies.
4. **Q-NEXT as the next #1049 unit?** Should it be a separately authorized paper-only unit, or should
   #1049 rest at outcome 3 (a scoped negative) for both the affine and the linear clause?
5. **Routing to #1210 and #1211.** Should the refinements of §3.2 and O-D be passed to the #1211 and
   #1210 writers as review inputs? §3.2's refinements are that the shared premise is B, not
   linearity, and the MECH-2:532 attribution; O-D concerns SA-1(a) column (ii). BRIDGE r3 already
   states the §3.2 premise point. This unit made no edits to their files.

***

## 7. Classification of findings (§A.31) and pressure tests

**Classifications.** Each label is relative to a `git grep` of `papers/`, `book/` and
`verification/` at `fd539e15`, and to today's drafts.
- **F-1 (§2.1, P1): uniform amplitude covariance does not imply affinity in d = 2, 3 among
  centre-free nearest-neighbour rules; in d = 1 (centre-free, nearest-neighbour, odd q, with
  reflection) it forces linearity. NEW, candidate.**
  - No record separates the uniform form from the site-wise form. A5 scoped non-affine rules out.
    H-D U6 quotes the lemma only.
  - The constructions are not link sums, and in the link-sum class the implication holds (F-9).
- **F-2 (§3.2): the sector split survives non-affinity under a bipartite read pattern.**
  - Relative to MECH-2:532's attribution: NEW, candidate. BRIDGE r3 [H] reaches the same point.
  - Relative to QP: ELABORATING, since QP proves G1 for linear updates and notes that "Lemma G1 uses
    only the finite update".
- **F-3 (rows 3b–3d): G2 and Q(iii) hold for affine rules; Q(i) fails. ELABORATING.** QP node 6
  treats translations in Q(iii). Q(i)'s failure for b ≠ 0 was not found stated.
- **F-4 (§3.3): one sector carries the b = 0 content of the dynamical rows, and it coincides with
  NQ1(a) and Q4c. ELABORATING** (a merge of three open items).
- **F-5 (rows 4 and 4′): J does not depend on b; the centring of Σ matters for NQ1(b).
  ELABORATING.**
- **F-6 (§2.1(iii)): G_SM violates even the uniform form. ELABORATING.** MECH-2 records "A5 fails".
- **F-7 (§2.3): the corpus answers "does the q-size gauge entail amplitude-scale gauge?" in two
  ways.**
  - Open form: SM:96, "an identified open structural question"; Sub:100 and :104, "an identified
    open step".
  - Negative form: Sub:274, "resolves in the negative, and sharply"; Structure:301, the alphabet-size
    hypothesis "does not entail" it.
  - **CONFIRMING of an inconsistency already on the record**, not new mathematics. H-D D6 and H-D-SR
    `SR-1` record "four in the open form, one resolved in the negative". H-D-SR `SR-3` concludes that
    "The disagreement stands on the record unadjudicated". A5 C8 cites `SR-3`.
  - The only statement added since is Structure:301's negative form. It is absent from the Structure
    blob that H-D-SR pins (`84a7ede4`), which contains no "does not entail".
  - H-D-SR's coordinates are at its own base. At `fd539e15` the open form stands at SM:96, Sub:100 and
    Sub:104, the inherited-status statement at SM:585, and the negative form at Sub:274 and
    Structure:301.
  - A cross-document status inconsistency for #1029 (§A.25).
- **F-8 (§2.3.1): Sub:272's argument fails under either reading of "amplitude-dependent emergent
  dispersion": under (b) the inference is invalid; under (a) its premise is false.** The argument
  runs from "a non-affine F induces amplitude-dependent emergent dispersion" to "'absolute amplitude
  is unobservable' already presupposes an affine rule".
  - *Reading (b)*, which Sub:270's attribution to [SM §4.1] supports. The parenthetical is true (the
    lemma). The conclusion is false for d = 2, 3 when its antecedent is the uniform form, so the
    inference is invalid. P1's response depends on the background but not on the absolute level
    [A; X: r2 G1, G2; rv2 R6].
  - *Reading (a).* The inference would be valid, but the argument is unsound: the parenthetical is
    false for P1's class, and Sub:270's ⟺ fails in the ⟹ direction.
  - Sub:272's "strictly weaker" and "excludes" clauses are jointly false under every reading of the
    principle.
  - The second sentence's opening clause, "the one route that would make the affine restriction
    *unconditional*", is false under the uniform reading for d = 2, 3 (F6).
  - NEW, candidate; a consequence of F-1.
- **F-9 (§2.4): link-sum recovery.**
  - In the link-sum class with link maps not assumed additive, uniform shift covariance forces
    affinity at every d and q (K = 1; for K > 1 with shifts by every c, G4). It needs λ = 1 only and
    no value of κ.
  - Among uniformly covariant rules, link-separability is equivalent to affinity.
  - **POSITIVE under GA7-α** (not stated in the corpus) for the A1–A6 sites' route through gauge.
    Under the written interface the relevant results are E2 and the kernel's typing, with the gauge
    principle idle (G1). Gaps G1 and G2 stand. The withdrawal of the P1-based narrowings does not
    depend on GA7-α (§2.4 item 2).
  - The one-line proof is REVIEW-1049-r2's. The κ-free form, the converse and the reading of the
    corpus are this unit's.
  - **Assumption-watch marker.** Wherever the affine restriction is attributed to gauge, record
    whether a link-sum interface is assumed, and whether its links are typed additive. If they are,
    the gauge principle does no work. This is the affine-side form of A5 N9's marker.
- **F-10 (§2.3, GA9): P1's uniform symmetry group is exactly the additive-automorphism group that
  SM:96 names as the gauge group.** The gauge-group statement does not discriminate affine from
  non-affine rules; the paper argument needs only that the rule is onto and uniformly covariant.
  ELABORATING.

**Pressure test of the favourable branch.** The favourable reading is that "linear beyond affine
carries little weight" (§3.1). It lightens the cost of A5's unjustified clause. Six checks follow,
then a seventh on the §2.4 recovery, which is favourable in a different way.
1. **What the reading needs.** It holds only when rows 2, 3b, 3d, 4, 7 and 8 are read as statements
   about linear parts or difference spaces.
   - At the owner's absolute baseline (row 11) and for configuration-level conservation (rows 3c and
     12), b = 0 does matter.
   - Under (A-lin), so does Stage 2(d)'s singlet U(1) (row 5).
   - The kernel statements D12 and D13 use A5 as stated; their affine extensions are unreviewed.
2. **Where the weight goes.** The reading moves weight from "linear" to "affine", and §2.1 finds
   affine equally underived. The net effect is unfavourable: A5's two clauses are both posits, and
   the downstream results inherit the affine one.
3. **Row 2's non-affine column.** It is only a [D] remark on linearizations over the real lift. It
   is not offered as support for any chirality claim over ℤ/q.
4. **The F-1 counterexamples.** They are generic functions chosen to satisfy (R-uni). They test an
   implication; they are not offered as physics.
   - In d = 1 the implication holds under the stated hypotheses. The claim is therefore scoped to
     d = 2, 3, and to the uniform symmetry group.
   - It does not show that some other independently justified principle fails to give affinity.
     That is Q-NEXT.
5. **The inventory is the corpus's stated assumptions, not every conceivable one.** §2.3 lists the
   gauge assumptions and gauge statements found by the search of §2.1, including the items of
   REVIEW-1049-r2 §3.2 and the Stage 2(d) uses found in r3's sweep. GA7 is reading-dependent, GA8 is
   undetermined, and a principle not stated in the corpus is outside the inventory.
6. **The search is finite.** No universal negative is stated.
7. **The recovery of §2.4 is favourable to the framework, so it was pressed hardest.**
   - *Does the corpus intend the link sum for non-additive rules?* No source says so (§2.1 search).
     The recovery uses an extension of the written interface, labelled as such (GA7-α).
   - *Does it smuggle the conclusion in?* In part. Among uniformly covariant rules link-separability
     is equivalent to affinity (§2.4, converse), so it relocates the premise and does not derive
     affinity from gauge alone. Under the kernel's typing it does less still: linearity is built in,
     and gauge is idle (G1).
   - *Does it rescue more than it should?* It reaches only the sites whose statement sits among
     A1–A6. Sub:272, Sub:274 and Structure:219 are not rescued, and their dispositions stand.
   - *Was the withdrawal decided by the favourable reading?* No. P1 is not a counterexample at those
     sites whichever status the interface has, a condition on rules or a description of their
     domain. Only the joint-insertion extension, which no source writes, would restore the
     narrowings (§2.4 item 4), and that choice is put to the owner (§6 Q2).

***

## 8. Verification scope

- **Paper.** Every [A] step above was done by hand. These include:
  - the d = 1 uniqueness (every odd q with reflection; odd prime q without);
  - the P1 covariance and isotropy arguments, and the d = 3 non-additivity at every prime q ≥ 5;
  - B0.1, B0.2 and B0.3(b)–(c), Prop. 2.5 and the J² = −1 identity;
  - the affine weight-preservation lemma;
  - the product-support argument;
  - the Q(i) offset identity;
  - the G1 induction for functions of opposite-colour variables, and G2's step 3 under common
    offsets;
  - (r3) the link-sum recovery E3, its corollary and its converse (§2.4); the GA9 argument that a
    uniformly covariant rule taking every value has exactly the additive-automorphism group as its
    uniform permutation symmetries (§2.3); the truth tables of §2.3.1 for Sub:270–274 under readings
    (a)/(b) and (R-rel)/(R-uni)/(R-site), including the b ≠ 0 incomparability (λ = −1).
  - (r4) F6 under each reading; the q = 2 cases of F1 and of the G1 clauses; E3's extension to
    (ℤ/q)^K with every shift, and the diagonal-shift witness ((x₁ − x₂)², 0); F7's count
    |{x ↦ λx + c}| = q·φ(q), which equals q! exactly when q ≤ 3.
- **Exact generic checks used as support.** These are exact integer arithmetic over ℤ/q on generic
  functions or one-step identities, and are not a computation on an OI mechanism:
  - `probes/p1_uniform_gauge_not_affine.py` — sha256
    `7f03a6ca37c887820d6fa92027ad484a210c19b4a255314ed59adefd5dd3a161`; output `p1.out`
    `309f38b8b00f5b081a260277d16ea1098519fc6914caeb039cccf46ebc061e76`; ALL PASS. Exhaustive over
    (ℤ/q)^{2d}, for:
    - d = 3 at q ∈ {2, 5, 7};
    - d = 2 at q = 7;
    - d = 1 at q = 3 (all 3⁹ functions);
    - with the linear control and the affine-offset countercontrol.
  - `probes/p2_grading_affine.py`, part (B) only — sha256
    `26a8f26043afb3bc9738b2bb59312d10451118e7cfcade94fa9587baaef44dce`; output `p2.out`
    `b7d483b2118033edeb3f6c83076c2e2bca13be76324ae9e41767d135ee7c05f0`. (B): the one-step Q(i) offset
    identity, exhaustive over every symmetric zero-diagonal K, every b and every state, for n = 3, 4
    over F₂.
  - `probes/r2_gauge_inventory.py` (r2) — sha256
    `3ca85833990e1f35438296f7ef4d7ec3bad80311b2be53ac11221edd9eb2aef2`; output
    `r2_gauge_inventory.out` `63c0c7f03f676f84a4786ee79369bc8ed108ad322c84bba0c4204e21db2855fa`; ALL
    PASS, exit 0. Imports no earlier probe; re-implements the d = 3 function from its definition. G1
    uniform-amplitude independence of every single-slot first difference (exhaustive, q = 5); G2
    base-point dependence; G3 κ = 2 covariance (exhaustive, q = 5); G4 site-wise shift is not a
    symmetry of the linear rule; G5 non-additivity at every prime 5 ≤ q < 200. Controls: the linear
    rule; countercontrol (1/3)Σ + v₀², which fails G1.
  - The reviewer's `review/rv_p1.py` (`2d2753f5…b551a`) and `review/rv_p2.py` (`a72f1c87…3034`)
    were re-run here with `python3 -I`: exit 0, outputs byte-identical to `rv_p1.out` and
    `rv_p2.out`. Parts A–E of rv_p1 and the Q(i) part of rv_p2 are cited where named.
  - `probes/r3_link_recovery.py` (r3) — sha256
    `349032103f7f8bbc8eba2e58eb2cad43eb85214f3fbc51090bc61db3d789d5e4`; output
    `r3_link_recovery.out` `ab2b278651d89de8cacfd71c1e565118ee8287911d7ca69c40106f1b87a90b44`; ALL
    PASS, exit 0, about 1 s. Imports nothing from `probes/` or `review/`; every construction is
    re-coded from its §2.1 definition, with the d = 3 slots ordered (+x, −x, +y, −y, +z, −z).
    Iterates no dynamics.
    - K1: none of the four P1 constructions is a link sum (a nonzero mixed second difference between
      two neighbour slots); controls: the linear rule and the separable non-affine Σ x_j² have none.
    - K2: separable rules whose uniform-shift effect is state-independent (no κ assumed) are exactly
      the affine separable rules, exhaustively for 2 slots at q = 2, 3, 4 and 3 slots at q = 2, 3;
      countercontrol 2x₁ + (x₂ − x₁)² at q = 3 (shift-covariant, non-separable, non-affine).
    - K3: the affine rule (1/3)Σ + 1 at q = 5 fails (R-uni) for every κ; control: (1/3)Σ satisfies it
      at κ = 2, exhaustively.
    - K4: the uniform permutation symmetry group of the second-order update is exactly AddAut for the
      d = 2, q = 7 construction (42 of 7! maps) and the d = 3, q = 2 construction (2 maps);
      countercontrol (1/2)Σ + x_E² at q = 7 (1 map).
  - The reviewer's `review/rv2_gauge_audit.py` (`2422bd13…6faf6cd`) was re-run with `python3 -I`
    into `reassess/rerun-1049-r3/`, outside the unit's directory: exit 0, output byte-identical to
    `rv2_gauge_audit.out` (`372a2c17…16ab2`). R1–R6 are cited where named.
  - `probes/r4_scope_checks.py` (r4) — sha256
    `23c659f42756c5d8ab710bd64eedf8f5af73ba6c134d1beaa9099cca9df8b991`; output
    `r4_scope_checks.out` `d5bc1d8d5cfe29fe6e819aeff36f04784efe4aa217c580726158f2d90c63492c`; ALL
    PASS, exit 0, under 1 s, run with `python3 -I`. It imports only `itertools`, `math` and `sys`,
    imports nothing from `probes/` or `review/`, and iterates no dynamics.
    - C1: at q = 2 all four maps ℤ/2 → ℤ/2 are affine and Σ x_j² = Σ x_j (n = 4, 6); at q = 3, 5,
      Σ x_j² (n = 4) is not affine and has a state-dependent shift effect; control Σ x_j.
    - C2: at q = 2, n = 6, all 128 affine rules satisfy the κ-general uniform form, and the κ = 2 form
      exactly when Σa is even; P1's q = 2 rule satisfies the κ = 2 form and is not affine;
      countercontrol 2Σx + 1 at q = 3, d = 2 (fails λ = −1); control 2Σx.
    - C3: at q = 3, K = 2, ((x₁ − x₂)², 0) is not affine, is unchanged by every diagonal shift, and
      has a state-dependent effect under (1, 0); control: an affine map.
    - C4: for q = 2–7, the permutations x ↦ λx + c number q·φ(q), and are all q! permutations
      exactly when q ≤ 3.
  - The reviewer's `review/rv3_link_affinity.py` (`a260d6dd…536f`) was re-run with `python3 -I`
    into `reassess/rerun-1049-r4/`: exit 0, about 17 s, output byte-identical to
    `rv3_link_affinity.out` (`49e4b993…4a28`). V1, V2, V5 and V6 are cited where named.
- **Non-evidential records.** `probes/p2_grading_affine.py` parts (A) and (C) and
  `probes/p3_grading_nonaffine.py` (`2edd0b311680243e0a0a2cea3758cb6dbfc6c53da700ee48ccbb919ed49ff1b3`;
  output `p3.out` `8346fa0f346ee37b6cee83f5526515bc1a34e59c1535d2bee63facd9805767ac`) iterate the
  native second-order update over several ticks. They are kept unchanged as records of what was run
  for r1 and are **not evidence for any statement here**. Rows 3a and 3b, and the "fails only when"
  statement, rest on their complete [A] proofs.
- **Not done.** Kernel builds (the kernel statements cited are read from `main`, not rebuilt),
  manuscript edits, the A5 §7 or Q4 §7 computations, any evaluation of the alphabet-size
  hypothesis, and any edit to #1210 or #1211 files. No git or GitHub writes.
- **Reading coverage.**
  - Read in full: #1049 and all of its comments; A5; the Q4 results and §§1–2, 4–6; Sub:98–104,
    :159, :163, :220 and :270–274; SM:92–112, :224–242; Main:726; QP §1.2, nodes 1, 3, 6 and 9,
    :362–369, :690–745 and :836–848; this unit's review in full (r2).
  - Read at the cited lines (r2): Structure:210–219, :259, :301; SM:1416; A5 rows D7, D12, D13,
    D15 and N10; ch02:84; FULL:718; the `.tex` mirror lines listed in §2.1.
  - Read in full in r3, at `fd539e15`: REVIEW-1049-r2; Sub:96–104 and :268–274;
    SM:94–96, :114–118; ch05:45; `OIBridge/BackgroundIndependence.lean`:1–135; A5 nodes N8′ and N9;
    Substratum.tex:743–752, :783–786, :1405–1411, :1717–1740, :1768–1778.
  - Read in r3 at the quoted passages only (long paragraphs, or `git grep` context): Sub:90, :104–110,
    :210–221 and :249–266 (Theorem 24 statement and proof opening); SM:112, :240, :314, :344, :374, :523,
    :585, :811, :1416; Main:726 (xii); ch02:74–86 (FULL:718 and :720 compared byte-wise with ch02:84
    and :86, FULL:1363 with ch05:45); Structure:219, :259, :301; `OIBridge/A6Instantiation.lean`
    (`linkSubstratum_A5` and the bounded reading at :317–321); A5 rows D14 and C8 and node N2; Q3
    A3–A4; H-D result D6; H-D-SR `SR-1`, `SR-3` and its pinned Structure blob `84a7ede4` (searched
    for "does not entail"); the r3 sweep hits listed in §2.3 (item 5).
  - Read in r4, at `fd539e15`: REVIEW-1049-r3 in full; Sub:100, :102, :104, :220, :270, :272 and
    :274 in full; Substratum.tex:742–752, :1728–1740, :1765–1786; Structure.tex:979–984,
    :1143–1146, :1268–1274; SM:96 (the "proper subgroup" sentence), :312, :314, :116; SM.tex:717;
    ch02:86 and FULL:720 (the "link-valued data" clause); `A6Instantiation.lean` (the `linkRule`,
    `linkSubstratum` and `Fin 6 → ZMod q` instances). `git diff fd539e15 cac5d264` in full.
  - Read in part: Q3 (outline, the outcome table, A3–A4), and MECH-1 and MECH-2 at the cited lines.
  - From the drafts: BRIDGE r2 §0, F4 and §§9–12; BRIDGE r3 §0 item 6 and the §10 G1/MECH-2
    passages (r2); REVIEW-UNIT1 (B3 and the verdict table); SHARED §9 (re-located in r5); QX3 A3.1;
    the QX4 affine passages (re-located in r5).
