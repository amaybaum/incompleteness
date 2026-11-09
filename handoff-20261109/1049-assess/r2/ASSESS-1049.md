# ASSESS-1049 — what is open on #1049 (linear vs affine microscopic dynamics) after the #1210/#1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r2, after the
independent review `review/REVIEW-1049.md` (sha256 `d56512e5…5344`, REVISE); pending a fresh,
independent review.** Nothing here is adopted, promoted or proposed for adoption, and no status
changes. The manuscript narrowings of §2.3 are proposals recorded in this file only, as the owner
directed; none is made. A review ACCEPT, if reached, authorizes nothing further. The r1 text is
kept unchanged at `r1/ASSESS-1049.md` (`9e60b0ae…0e040`); each change is mapped in
`DISPOSITIONS-r2.md`.

- **Accountable home.** #1049. Parent #983; related #914, #1029, #1210, #1211, #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1049 c.6740117832 (full record #1169
  c.6740116927): "One paper-only unit each, re-assessing its open question against today's
  #1210/#1211 findings … each with a fresh review. Exact generic checks only." Not authorized:
  computation on an OI mechanism, new physical assumptions, freeze, dispatch, manuscript changes,
  merges. This unit made no git or GitHub write and edited no manuscript. The owner's chat
  direction of 2026-11-09, relayed by the coordinator, is applied in r2: check the affine
  counterexamples against every stated gauge assumption, with its source, before weakening any
  manuscript claim, and propose a narrowing, in this file only, where every stated assumption is
  satisfied (§2.3). The coordinator's instruction on the generic-check boundary is also applied:
  P2(A), P2(C) and P3 are not used as support (§8).
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09). `Sub`, `SM`, `Main`, `Structure` are `papers/{Substratum,SM,Main,Structure}.md` at
  that SHA; line numbers refer to it. `A5` =
  `verification/programmes/substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md`; `Q4` = the
  same directory's `A5-Q4-STAGE2D.md`; `Q3` = its `q3-a6-offsets-20261108/ASSESSMENT.md`; `QP` =
  `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`; `AP1` =
  `…/reconstruction/apparatus-1-20261107/DESIGN.md`; `MECH-1`, `MECH-2` = `…/mechanism-1-20261107/`,
  `…/mechanism-2-20261108/DESIGN.md`.
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

1. **Affine over non-affine is not derived (§2.1).** The corpus route is: unobservability of
   absolute amplitude ⇒ "every first difference of the update is independent of its base point"
   ⇒ affine (SM:240; Main:726 (vii)). The second arrow is the linearity-equivalence lemma, proved
   in both directions. The first arrow is not proved, and in its uniform form it fails: for d = 2
   and d = 3 there are non-affine, centre-free, cubic-isotropic, translation-commuting,
   nearest-neighbour second-order rules for which **every** uniform map x ↦ λx + c𝟙 is an exact
   dynamical symmetry [A; X: P1]. The counterexample survives the κ-independent uniform reading
   (§2.1 (R-uni)). For d = 3 at every prime q ≥ 5 non-affinity has a complete paper proof [A].
   Read as relabellings, the amplitude maps constrain no rule [A; O-ext of owner Q2]. So the affine
   restriction rests on the site-wise base-point form, which is equivalent to it. Main (vii) and
   SM:240 state this scope. Sub:100, :104, :220, :272, :274, ch02:84, FULL:718 and Structure:219,
   :259 present the affine restriction as following from the gauge principle without it.
2. **Every stated gauge assumption, checked against P1's class (§2.3).** P1's class satisfies
   the relabelling reading, the uniform exact-symmetry reading, independence of the local response
   from the absolute amplitude and A4's translation clause, and A6 places no condition on it; it
   fails the site-wise
   base-point form, by construction, and the site-wise exact-symmetry reading, which the linear wave
   rule also fails. Its status under the alphabet-size hypothesis (SM:94; Structure:219, :301) is
   undetermined, because that hypothesis needs a cross-q correspondence the corpus does not
   construct and is posed for linear dynamics. Narrowings are proposed in this file for the seven
   sites that state only amplitude-scale gauge (§2.3); none for Structure:219, :259, :301, which
   state the alphabet-size hypothesis.
3. **Linear over affine stays unselected (§2.2).** Today's drafts add no selector. A5 R5 and Q3
   outcome (N) stand as the record, both WIP / UNVERIFIED.
4. **Most downstream results examined use affinity or only the bipartite read pattern, not
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
5. **The b = 0 content of the dynamical rows sits on one sector (§3.3).** It is the uniform
   (k = 0) A₁ sector at κ ≡ 2 (α ≡ 1/d for odd q with gcd(d, q) = 1). The same sector is #1049's
   resonance locus (A5 R3), Q4's open resonance condition (Q4c), and #1211's null-mode sector
   where no J exists (NQ1(a)). The kernel and Layer-2 rows of item 4 are statements made under A5
   as stated and are not located on that sector.
6. **Next question (§5, Q-NEXT).** Does any independently justified OI principle imply the
   site-wise base-point form in d = 3? Excluding P1's class is a necessary condition for a positive
   answer, not a sufficient one; a negative answer can be shown by P1-type witnesses. A companion
   question, for b = 0, is the resonance of the A₁ sector at k = 0 (Q4c and #1211 NQ1(a)).

***

## 1. Inputs and their standing (§A.46 item 7)

| Input | Standing | Used here as |
|---|---|---|
| Linearity-equivalence lemma (base-point-independent first differences ⇔ affine) | [P] Sub:274 (telescoping proof plus exhaustive checks); re-derived [A]: ⇒ by telescoping, ⇐ immediate | established, both directions |
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
  - **d = 2, 3: (R-uni) does not imply affinity [A; X: P1].**
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
  records that deriving amplitude unobservability from the observer architecture "is … circular";
  its reason, "a non-affine $F$ induces amplitude-dependent emergent dispersion", is false for P1's
  class at the level of absolute amplitude (F-8), and the circularity verdict holds with
  "affine" replaced by "uniformly covariant" (§2.3, Sub:272 row).

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
  class, which is defined uniformly in q at every prime q ≥ 5.

It therefore does not establish the base-point form, and it does not decide P1's class (§2.3,
GA8). Structure:301 itself records that amplitude-scale gauge is "an adjoined operational input
that the alphabet-size hypothesis of [SM §2.7] does not entail".

*Consequence.* The affine part of A5 is a posit in the form named by SM:240 and Main (vii). The
operational principle motivates it but does not entail it in d = 2 and d = 3.
- No corpus source read gives the base-point form an independent reason. The alphabet-size argument
  above is conditional on an unproved hypothesis and does not decide P1's class.
- Main (vii) and SM:240 state the scope accurately.
- These sites present the affine restriction as following from the gauge principle, with no
  site-wise qualifier:
  - Sub:100 and Sub:104 ("restricts the update to an affine one via the linearity-equivalence lemma");
  - Sub:220 ("non-affine wave equations … are the separate class one obtains exactly when that gauge
    principle is dropped");
  - Sub:272 ("the input … is strictly weaker than the output … a non-affine F … the principle
    excludes"; "a non-affine F induces amplitude-dependent emergent dispersion");
  - Sub:274 ("yields an affine rule as a certified theorem");
  - ch02:84 and FULL:718 (identical text);
  - Structure:219 ("An affine rule is therefore forced *given* that operational principle");
  - Structure:259 ("amplitude-scale gauge invariance yields the affine restriction, weaker than A5
    ([Main §4.5], item (vii))", which cites Main (vii) without its base-point qualifier).
- `.tex` mirrors of these sites at `fd539e15`: Substratum.tex:750, :783, :1407–1410, :1732, :1778;
  Structure.tex:981–983, :1145, :1273; The-Incompleteness-of-Observation-FULL.tex:3312–3314.
- Read with (R-uni), the "exactly when" of Sub:220 and the "excludes" of Sub:272 are contradicted by
  P1 in d = 2, 3. Read with (R-site), they hold, but then the principle is affinity restated.
- This is a cross-document finding for #1029. The narrowings that pass the owner's test are
  proposed in §2.3; none is made.
- **Search scope for "no corpus source":** `git grep -i` for "base-point", "base point",
  "amplitude-scale", "affine", "non-affine", "partly derived", "certified theorem", "therefore
  forced", "weaker than A5" and "generically produce" over `papers/` (`.md` and `.tex`), `book/` and
  `verification/` at `fd539e15`. The A5-specific records were read in full. The H-D record
  (`round-h-d-a5-status-adjudication/result.md`) quotes the lemma (U6) and does not separate the
  uniform from the site-wise form.

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

"P1's class" is the four constructions of §2.1: d = 3 at q = 2 and at every prime q ≥ 5, and d = 2 at
q = 7. Every gauge assumption the corpus states that bears on which rules are admitted is listed,
with its source.

| ID | Gauge assumption as stated | Source | Reading | P1's class satisfies it? | Support |
|---|---|---|---|---|---|
| GA1 | The additive-group automorphisms (rescalings and shifts) preserve the emergent observables; they are "relabellings of the alphabet" | SM:96; Sub:270 | (R-rel): conjugations of the description | **yes**, as every rule does: a conjugate rule describes the same orbits | [A]; [O-ext] |
| GA2 | "Operationally the *absolute scale* of the field value is unobservable"; "a global rescaling of the field value φ"; rescalings and shifts "leave every observable unchanged"; "the alphabet's additive automorphisms are gauge" | SM:96; Sub:163; Sub:270; Sub:274 | (R-uni): every uniform x ↦ λx + c𝟙 is an exact symmetry of the dynamics (κ = 2 form; also the κ-general form) | **yes** | [A] (§2.1); [X: P1; rv_p1 A–B; r2 G3] |
| GA3 | Amplitude-independent emergent dispersion: the affine relabellings preserve "the field-amplitude dispersion ω(k)"; "amplitude-independent dispersion ⟺ affine dynamics"; "a non-affine F induces amplitude-dependent emergent dispersion" | Sub:270; Sub:272 | (a) the local response is independent of the absolute (uniform) amplitude; (b) the response is independent of the whole background state, which Sub:270 identifies with affinity through the lemma | (a) **yes**: every single-slot first difference is unchanged by uniform shifts (from GA2 with λ = 1). (b) **no**: (b) is the base-point form (GA4). P1's response depends on background gradients, not on the absolute amplitude | [A]; [X: r2 G1, G2] |
| GA4 | Every first difference of the update is independent of its base point | SM:240; Main:726 (vii) | (R-site) | **no**, by construction: GA4 is equivalent to affinity (lemma, Sub:274) | [P]; [A] |
| GA5 | "Site-wise relabellings" | Sub:270 | as exact symmetries of the dynamics (site-dependent shifts) | **no**, and neither does the linear wave rule: shifting one neighbour slot changes the update. As relabellings it is GA1 | [X: rv_p1 D; r2 G4] |
| GA6 | A4: φ "commutes with lattice translations up to gauge", gauge acting by site-wise bijections of each site's (previous, current) pair; the update contains no copy of the site's present value | Sub:98 | as stated | **yes**: P1's rules commute with translations exactly and read no centre | [A]; [X: rv_p1 C] |
| GA7 | A6: covariance under site-dependent internal-index transformations with link-valued coupling; "once it is in place the local transformation law imposes no further condition on the rule" | Sub:102 | as stated | **not excluded**: A6 places no condition on the rule (Sub:102). P1's rules are scalar; an internal-index extension is not constructed | [P] |
| GA8 | Alphabet-size hypothesis: systems differing only in q "produce the same emergent transition probabilities"; "Non-linear dynamics over ℤ/qℤ generically produce q-dependent observable physics … violating the gauge equivalence" | SM:94; SM §2.7; Structure:217, :219, :301 | as stated | **undetermined.** It needs a cross-q correspondence that "is not constructed" (SM:94); it is "posed for linear dynamics" (Structure:217); at cycle-type level it excludes the linear rule too (A5 N10, "Undetermined"). It is not evaluated on P1's class here | [P]; A5 N10 |

Two further statements are not assumptions on the rule: whether the q-size gauge entails
amplitude-scale gauge (open at SM:96, Sub:100, Sub:104; answered in the negative at Sub:274 and
Structure:301; see F-7).

**The test, per site.** A narrowing is proposed for a site only if P1's class satisfies every gauge
assumption that site states, so that P1 is a counterexample to the site's statement as made. GA4 is
not an assumption of any overstating site: the overstating sites omit it, and the sites that state it
(SM:240, Main (vii)) are accurate. If the owner reads the test as corpus-wide instead, no narrowing
passes, since P1 fails GA4 by construction and GA8 is undetermined (§6 Q1).

| Site (and `.tex` mirror) | Gauge assumptions it states | All satisfied by P1's class? | Proposal (not made) |
|---|---|---|---|
| Sub:100 (Substratum.tex:750) | GA2 ("that the field-value scale is unphysical"); the q-size entailment is stated as open, not assumed | yes | Replace "its affine part is necessary *given* that gauge principle" with "its affine part is necessary given that gauge principle in the form that every first difference of the update is independent of its base point ([Main §4.5], item (vii)); global rescalings and shifts as exact symmetries do not imply it for $d=2,3$" |
| Sub:104 (Substratum.tex:783) | GA2 | yes | After "restricts the update to an affine one via the linearity-equivalence lemma of [SM §4.1]", add "when it is taken in the base-point form of that lemma" |
| Sub:220 (Substratum.tex:1407–1410) | GA2 | yes | Replace "exactly when that gauge principle is dropped" with "exactly when that gauge principle, in the base-point form of [SM §4.1], is dropped; non-affine, center-free, isotropic nearest-neighbour rules keep its uniform form for $d=2,3$" |
| Sub:272 (Substratum.tex:1732) | GA2, GA3 | yes (GA3 in reading (a), the reading its "absolute amplitude" names) | Replace "a non-affine $F$ on the same alphabet is a coherent object the principle *excludes*" with "a non-affine $F$ is excluded by the principle in its base-point form; uniform rescalings and shifts as exact symmetries do not exclude it for $d=2,3$"; replace "a non-affine $F$ induces amplitude-dependent emergent dispersion, which *is* observable), so "absolute amplitude is unobservable" already presupposes an affine rule" with "a non-affine $F$ can induce background-dependent emergent dispersion, which *is* observable), so "absolute amplitude is unobservable" already presupposes a rule for which uniform rescalings and shifts are exact symmetries, a class that contains non-affine rules for $d=2,3$". The sentence's conclusion, that the observer-architecture route is circular, is unaffected |
| Sub:274 (Substratum.tex:1778) | GA2 ("the alphabet's additive automorphisms are gauge") | yes | Replace "yields an affine rule as a certified theorem" with "yields an affine rule as a certified theorem when gauge is taken in the base-point form of the linearity-equivalence lemma" |
| ch02:84 and FULL:718 (FULL.tex:3312–3314) | GA2 ("the unobservability of the absolute field scale") | yes | After "restricts the rule to an affine one", add "in the form that the update's first differences do not depend on the base point" (book register; same edit in both parallel sources, §A.14) |
| Structure:219 (Structure.tex:981–983) | GA2 and GA8 | **no: GA8 undetermined** | None proposed |
| Structure:259 (Structure.tex:1145) | GA2 via Main (vii); GA8 named among A1–A6's motivation | **no: GA8 undetermined** | None proposed. Its divergence from the Main (vii) it cites is a citation-fidelity point independent of P1 (§6 Q1) |
| Structure:301 (Structure.tex:1273) | GA8 | **no: GA8 undetermined** | None proposed |

Each proposal narrows a statement to the scope its own cited lemma proves and is in the register of
§A.32–§A.33 for `papers/`. Its support is §2.1's paper proof (d = 3, prime q ≥ 5) and P1's exhaustive
checks (d = 2, q = 7; d = 3, q = 2, 5, 7). Any edit would need owner authorization, propagation to
the `.tex`/`.pdf` derivatives (§A.25 step 5) and review; none is authorized here.

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

**O-A. The affine part has no independent derivation.**
- Its status is a posit, in the site-wise base-point form (§2.1). The uniform operational form is
  satisfied by non-affine rules in d = 2 and d = 3.
- This is new relative to A5, which scoped non-affine rules out. It bears on the "partly derived"
  of Sub:100 and :104; §2.3 proposes narrowings at the seven sites where P1's class satisfies every
  stated gauge assumption.
- Owner question 1 (§6) asks how to record it.
- It is not a refutation of affinity. It is the absence of an entailment.

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
- SHARED r5 §9's "yes, conditional on Substratum (A4)–(A5)" for SA-1(a) column (ii) would read more
  precisely as "conditional on A4, on the affine restriction (whose derivation from amplitude-scale
  gauge needs the site-wise base-point form), and on the form, symmetric coefficients and
  symplecticity; linearity beyond affine not used". That is a proposal for #1210's writer. No #1210
  file was edited.

**O-E. Pressure against affinity from the programme's own needs.** Three items: G_SM (SM:112),
in-world setting selection (MECH-1), and global-conservation routing (QX3, owner Q3-2). If any of
them is adopted, it needs a non-affine element. Under §A.29 that element must carry its own
independent justification.

**O-F. GA8 on P1's class.** Whether the alphabet-size hypothesis excludes P1's class is
undetermined (§2.3). It cannot be decided without the cross-q correspondence SM:94 says is not
constructed. Until it is, no narrowing is proposed for Structure:219, :259 and :301.

***

## 5. Smallest decisive next paper question

**Q-NEXT.** *Does any independently justified OI principle imply the site-wise base-point form in
d = 3?*

A positive answer requires the principle to exclude P1's class of non-affine, centre-free,
O_h-isotropic, translation-commuting nearest-neighbour rules that carry the uniform
additive-automorphism group as an exact symmetry. That exclusion is a **necessary condition**, a
cheap screen, and not a sufficient one: P1's class is a set of witnesses, not the complement of the
affine class, so a principle that excludes it need not exclude every non-affine rule.

The principles to test are these:
- A1–A4 and A6 as stated;
- E4;
- the trace-out interface of Main §1;
- amplitude-scale gauge in the owner's relabelling reading;
- the alphabet-size hypothesis (SM:94; Structure:219, :301) as a candidate, which first needs the
  cross-q correspondence SM:94 says is not constructed (O-F).

**Why it is decisive.**
- **A negative answer** makes A5 a posit in full: affinity and linearity alike, with an operational
  motivation for the affine part only. The "partly derived" wording becomes a #1029 item.
- **A positive answer** names a principle with a consequence beyond affinity. That principle is then
  judged under §A.29.
- Either answer settles O-A. O-A is upstream of O-D and of rows 1, 2, 3b, 4, 7 and 8.

**Why it is small.**
- For each principle, the screen (does it exclude P1's class?) is a paper check on one family of
  witnesses. A principle that fails the screen gives a negative answer for that principle, shown by
  P1-type witnesses.
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

1. **The "partly derived" wording (O-A) and the §2.3 proposals.** Main (vii) and SM:240 carry the
   site-wise form. Sub:100, :104, :220, :272, :274, ch02:84, FULL:718 and Structure:219, :259 do not.
   - Should the §2.3 proposals for the seven sites that pass the per-site test be recorded under
     #1029 as candidate corrections (scope wording only), pending review of P1?
   - Is the per-site reading of the test the intended one? Under a corpus-wide reading no narrowing
     passes (GA4 fails by construction; GA8 is undetermined).
   - Structure:259 cites Main (vii) without its base-point qualifier. Restoring it is a citation
     fidelity point that does not depend on P1; should it be treated separately from the GA8 hold?
   No manuscript change is made by this unit.
2. **Q-NEXT as the next #1049 unit?** Should it be a separately authorized paper-only unit, or
   should #1049 rest at outcome 3 (a scoped negative) for both the affine and the linear clause?
3. **Routing to #1210 and #1211.** Should the refinements of §3.2 (shared premise B, not linearity;
   the MECH-2:532 attribution) and O-D (SA-1(a) column (ii)) be passed to the #1211 and #1210
   writers as review inputs? BRIDGE r3 already states the §3.2 premise point. This unit made no
   edits to their files.

***

## 7. Classification of findings (§A.31) and pressure tests

**Classifications.** Each label is relative to a `git grep` of `papers/`, `book/` and
`verification/` at `fd539e15`, and to today's drafts.
- **F-1 (§2.1, P1): uniform amplitude covariance does not imply affinity in d = 2, 3; in d = 1
  (centre-free, nearest-neighbour, odd q, with reflection) it forces linearity. NEW, candidate.** No
  record separates the uniform form from the site-wise form. A5 scoped non-affine rules out. H-D U6
  quotes the lemma only.
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
  ways.** SM:96 calls it "an identified open structural question", and Sub:100 and :104 "an
  identified open step"; Sub:274 says it "resolves in the negative, and sharply", and Structure:301
  that the alphabet-size hypothesis "does not entail" it. A cross-document status inconsistency for
  #1029 (§A.25). CONFIRMING of an existing inconsistency, not new mathematics.
- **F-8 (§2.3, GA3): Sub:272's "a non-affine F induces amplitude-dependent emergent dispersion" is
  false for absolute amplitude.** P1's local response is independent of the uniform amplitude and
  depends on gradients [A; X: r2 G1, G2]. NEW, candidate; a consequence of F-1.

**Pressure test of the favourable branch.** The favourable reading is that "linear beyond affine
carries little weight" (§3.1). It lightens the cost of A5's unjustified clause. Six checks follow.
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
   gauge assumptions found by the search of §2.1; GA8 is undetermined, and a principle not stated in
   the corpus is outside it.
6. **The search is finite.** No universal negative is stated.

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
    offsets.
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
- **Non-evidential records.** `probes/p2_grading_affine.py` parts (A) and (C) and
  `probes/p3_grading_nonaffine.py` (`2edd0b311680243e0a0a2cea3758cb6dbfc6c53da700ee48ccbb919ed49ff1b3`;
  output `p3.out` `8346fa0f346ee37b6cee83f5526515bc1a34e59c1535d2bee63facd9805767ac`) iterate the
  native second-order update over several ticks. They are kept unchanged as records of what was run
  for r1 and are **not evidence for any statement here**. Rows 3a and 3b, and the "fails only when"
  statement, rest on their complete [A] proofs.
- **Not done.** Kernel builds, manuscript edits, the A5 §7 or Q4 §7 computations, any evaluation of
  the alphabet-size hypothesis, and any edit to #1210 or #1211 files. No git or GitHub writes.
- **Reading coverage.**
  - Read in full: #1049 and all of its comments; A5; the Q4 results and §§1–2, 4–6; Sub:98–104,
    :159, :163, :220 and :270–274; SM:92–112, :224–242; Main:726; QP §1.2, nodes 1, 3, 6 and 9,
    :362–369, :690–745 and :836–848; this unit's review in full (r2).
  - Read at the cited lines (r2): Structure:210–219, :259, :301; SM:1416; A5 rows D7, D12, D13,
    D15 and N10; ch02:84; FULL:718; the `.tex` mirror lines listed in §2.1.
  - Read in part: Q3 (outline and the outcome table), and MECH-1 and MECH-2 at the cited lines.
  - From the drafts: BRIDGE r2 §0, F4 and §§9–12; BRIDGE r3 §0 item 6 and the §10 G1/MECH-2
    passages (r2); REVIEW-UNIT1 (B3 and the verdict table); SHARED §9 (re-located in r5); QX3 A3.1;
    the QX4 affine passages (re-located in r5).
