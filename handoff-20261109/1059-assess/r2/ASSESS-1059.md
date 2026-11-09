# BORN-SEL (#1059): re-assessment of the open question against the #1210 / #1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r2, after the
independent review `review/REVIEW-1059.md` (sha256 `8cbfe227…7446`, REVISE); pending a fresh,
independent review.** Nothing here is adopted, promoted or proposed for the manuscripts. A
review ACCEPT, if reached, authorizes nothing further. The r1 text is kept unchanged at
`r1/ASSESS-1059.md` (`d5b314af…d931`); each change is mapped in `DISPOSITIONS-r2.md`.

- **Accountable home:** #1059. Feeds #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, recorded in #1059 c.6740117293 (posted
  2026-11-09T12:31:13Z), full record #1169 c.6740116927 (posted 2026-11-09T12:31:12Z). Option
  text, verbatim: "**#1059/#1049/#868 audits** — One paper-only unit each, re-assessing its open
  question against today's #1210/#1211 findings (Born exponent; linear vs affine dynamics;
  joint-test validity), each with a fresh review. Exact generic checks only." Not authorized
  (c.6740117293): "computation on an OI mechanism, new physical assumptions, freeze, dispatch,
  manuscript changes or merges". This unit makes no repo, git or GitHub write. The owner's
  chat direction of 2026-11-09, relayed by the coordinator, is applied in r2: generating state
  mixing does not by itself establish the Born exponent ("The former does not automatically
  establish the latter"), and wherever FI-1 or non-monomial mixing appears it is stated as
  necessary under the stated hypotheses and not sufficient for the exponent or the law.
- **Checks run.** Three exact checks on generic mathematical objects (permutation, Cayley and
  Kraus matrices; columns; stabilizer states; one real function), in `probes/` (§8). No
  computation was run on an OI mechanism. A statement supported only by such a check is marked
  *computation-supported*.
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09). Every `path:line` is at that commit unless marked otherwise. "Main" =
  `papers/Main.md`; "QB3" = `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`;
  "T3" = `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/probability-source-assessment.md`;
  "AP1" = `verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`;
  "WMB" = `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md`;
  "A1R" = `verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a1_reset_v6/REPORT.md`;
  "EQ" = `verification/lean-mathlib/OIBridge/Equivalence.lean`.
  "BORN-SRC-1" = the reviewed audit quoted verbatim in #914 c.6567870091 (audit) and c.6567879365
  (review with final check), summarized in #914 c.6567852459; it is at base `02009693`, and its line
  numbers are at that base.
- **Today's drafts, used as hypotheses only (§A.46 item 7).** None is reviewed to ACCEPT at the
  hash read, and none is on `main`. They are cited for what they claim; no conclusion below rests
  on them alone.
  - "BRIDGE" = `scratchpad/bridge/BRIDGE-UNIT1.md` r3, sha256 `a5d7aad1…78c1` (#1211 unit 1;
    pending a fresh review). Its r2 review "REVIEW-r2" = `scratchpad/bridge/review/REVIEW-UNIT1-r2.md`,
    sha256 `3cdf7dc2…4eb3` (REVISE; it rejected the r2 ordering of FI-1 as the earliest
    unsupported step, RB1). The r2 text read for r1 of this unit is `scratchpad/bridge/r2/BRIDGE-UNIT1.md`
    (`3905569b…103a`).
  - "SHM" = `scratchpad/qphen/SHARED-MECHANISM.md` r5 §§8–9, sha256 `a7206701…cc4d` (#1210
    Phase 1). The r4 file is `qphen/r4/SHARED-MECHANISM.md` (`23ec1ef1…fd11`); the N2 row used
    in §6 F-a reads the same in both.

***

## 0. Summary

1. **#1059's question is unchanged in status.** No record on `main`, and no draft of
   2026-11-09, derives the quadratic exponent, or the Born probability law, from independently
   justified OI principles. (a)–(d) of BORN-SRC-1 stay open. The Born dictionary of $Q_{\rm fb}$
   is a definition (`QfbReal.born := ‖Q.U b' b‖ ^ 2`, EQ:205; Main:20, Main:556).
2. **Generating state mixing and deriving the exponent are different things.** Under the
   linearity hypothesis H-LIN (§1), a unitary that is non-monomial in the read basis is
   *necessary* for any record to discriminate the exponent: with monomial unitaries only,
   every $p>0$ fits every record (R3-N). It is *not sufficient*:
   - *for the exponent:* the forcing of $p=2$ by one non-monomial column (R3-C) holds only
     under H-RF$_p$, which posits the Born form up to its exponent; it tests the consistency of
     a posited form and derives nothing. For a general readout $f$, a non-monomial column does
     not fix $f$ (BORN-SRC-1 C4 at $n=2$; at stabilizer points, P2 and $g$ of §4.3);
   - *for the law:* the Born law further needs the measure (b), preparations across settings
     (c) and context structure (d), and coherent mixing supplies none of them, nor the
     composition rules.
   
   FI-1 (BRIDGE §5.1 [D]) asks for a non-monomial admissible operator on the configuration
   carrier at level one; BRIDGE states it as a necessary condition, in one direction only, for
   exact finite endomorphic operational QM on that carrier (GR:270;
   K `exists_nonMonomial_of_layerFlowExecutable`). R3-N's necessary condition, read on the
   configuration carrier, entails FI-1. FI-1 does not supply R3-C's antecedent: a
   non-unitary non-monomial operator can have only monomial columns (§3, R3; r2 check K1).
   FI-1 is neither the earliest nor the only gap: the phase and the flow are independent
   obligations (K `obligations_independent`, C5Discovery.lean:59), and H-Bell is a third,
   independent gap (BRIDGE §5.1 *Position* [D]).
3. **The three items named in the brief do not move (a).**
   - The complex structure $J$ off the null modes is a mathematically available
     *symmetry* of a dimension-$\ge3$ complex carrier (transitive unitary commutant). It is
     not an operation derived from OI or executable by the observer, and it fixes no read
     basis.
   - H-Bell selects a Bell branch, not a correlation law. The quantum Bell values need weights
     that finite uniform resources cannot give, and in that it shares an ingredient with (b).
     That is a shared ingredient, not an identification.
   - Today's stabilizer-scope route draws its probabilities from the counting measure, and no
     amplitude is read there, so it does not bear on (a) (§4.3). Even if it read amplitudes,
     stabilizer-point agreement would not select $f$ in the general class (a-gen): it
     exercises $f$ only at the points $2^{-k/2}$, which do not select $u^2$
     (computation-supported, P2 for $n\le3$; $g$ of §4.3 for all $n$). Within the power family
     the dyadic point $2^{-1/2}$ alone forces $p=2$ under H-RF$_p$ (K5), so this bullet is
     scoped to (a-gen). It holds whether or not SA-1(c) is ever justified.
4. **Measure (b).** On the two non-monomial routes on `main` that output a probability, the
   continuum ontic carrier and the seed/response carrier, the Born law is fixed by a choice of
   measure or of response function. Neither choice is selected (AP1:1012–1016; A1R; T3 §5;
   WMB §1). There, (a) cannot be separated from (b).
5. **Smallest decisive next paper question** (§5): whether any operation the observer can
   execute acts, on a configuration-carrier block of dimension $\ge3$, by a unitary that is
   non-monomial and not stabilizer-only in the block's read basis. The candidate place to look
   is the $J$-complex sector of the real lift, under the stated access. A negative answer leaves
   (a-gen) and (d) with no route on `main`. A positive answer supplies a necessary condition for
   (a), not the exponent, and is the first object on which O1's two candidate targets give
   different verdicts.

***

## 1. Conventions

- **Layers.** K kernel; A exact algebra or written proof; X exact or exhaustive computation on a
  generic object (this unit's probes); L literature, with an indication of whether it was read
  first-hand here; P prose only; D an unreviewed draft (hypothesis only).
- **Three columns** for each result or restriction:
  - (i) mathematically well-defined;
  - (ii) follows from independently justified OI principles;
  - (iii) reproduces the QM prediction.

  Column (iii) is never cited as support for column (ii). A posit is not a column-(ii) "yes".
- **Three distinctions kept apart** (owner direction, 2026-11-09):
  - *configuration carrier* (the substratum's configuration space at level one, on which FI-1
    is posed) versus *encoded carriers* (logical states encoded in configurations, on which
    non-monomial encoded maps arise without FI-1; BRIDGE §5.1 [D], citing QP:79–98 and
    QP:846–877);
  - *mathematical availability* of an operation or structure (a symmetry, a derived flow, a
    path) versus its *derivation from OI* as an operation the observer executes (Main:274,
    Main:590);
  - *coherent mixing* versus the *full quantum probability and composition rules* (the
    exponent, the measure, preparations, contexts, composites).
- **§A.34.** Every two-way statement is given as two separately supported directions, each named
  by its antecedent.
- **§A.31 labels** for this unit's own findings: NEW, POSITIVE, ELABORATING, CONFIRMING,
  BORDERLINE.
- **Hypotheses used below**, with status in the Code Review Rules' vocabulary.
  - **H-LIN** (*posited*): the admissible operations are unitary in one fixed read basis and act
    linearly on an amplitude vector; preparations are basis states, or are generated from a basis
    state by admissible operations. Complex matrix kinematics is "taken as given … deriving that
    kinematics is open" (Main:218).
  - **H-RF$_p$** (*posited*; open as a sourcing question): the unrenormalised values
    $|{\rm amp}_j|^p$ are the outcome law, so $\sum_j|{\rm amp}_j|^p=1$ is required on every
    read. With $p=2$ it is the Born form, which Main carries as the dictionary of $Q_{\rm fb}$
    and does not select (Main:20, Main:226, Main:288). BORN-SRC-1 review finding 9(i): the
    readout-as-outcome-law premise is the Born form, which "OI supplies rather than sourcing it
    … The hypothesis is open, not weaker than what is open". Its general-$f$ form **(d′)** is
    modulus-only, context-free and normalised (BORN-SRC-1 O1). The renormalised reading
    $|{\rm amp}_j|^p/\sum_k|{\rm amp}_k|^p$ is excluded: it is a law for every $p$ and selects
    nothing (r2 check K4).

***

## 2. Baseline: what was open on #1059 before today

All of this is on `main`, or is BORN-SRC-1, which is reviewed and ACCEPTed in #914:

- **(a) Exponent 2.** Open, kept on the list pending O1 (BORN-SRC-1 §4(a)).
  - (QM ⇒ normalisation): K, `QfbReal.sum_born` (EQ:227).
  - (OI ⇒ exponent 2): open. Native step unitaries are permutations, so every $f$ with
    $f(0)=0$ and $f(1)=1$ fits (Main:556, check 6 of `equivalence_recovery_probes.py`).
- **(b) The hidden-sector measure.** Open.
  - The numbers carried by the Born form are the measure's (QB3 §1, μ-number).
  - On each finite cycle the invariant measure is unique and uniform; the global counting
    selection is posit (iv), "a standard but substantive epistemic postulate, not derived"
    (Main:726; Main:56, Lemma 3, "a selection principle, not uniqueness from invariance alone").
  - Invariance does not select it for non-transitive φ (K, `invariance_does_not_select`).
  - QB3 header: "OI has not yet been shown to derive the Born rule or select the physical
    probability measure."
- **(c) Preparations across settings.** Open; blocked on O-INS.
- **(d) Gleason-type context independence.** No kernel result. [54] is listed in Main but not
  cited in its body (BORN-SRC-1 F6).
- **Measure-analysis thread (#1082).** Paused, with C-1 unfrozen and unrun (#1059 c.6651648653,
  c.6712164307). This unit does not touch it.
- **T3 (#1173).** "Physical exponent/context selection" is listed as open (T3:380). Finite uniform
  resources give rational weights (T3 §6.1). A coordinate change moves density between seed and
  response, so only the pushforward is physical (T3:246).

***

## 3. Question 1: results that constrain the exponent, and under which hypotheses

"Constrains the exponent" means that the result restricts which readout $f$ (or $p$) is
compatible with its hypotheses. Every row was traced to its source. Column (ii) asks whether the
row's *antecedent* follows from independently justified OI principles.

| ID | Result (scope) | Support | Hypotheses | (i) | (ii) | (iii) | What it does to (a) |
|---|---|---|---|---|---|---|---|
| R1 | $S\iff D\iff Q_{\rm fb}$, finite horizon | K, `finite_horizon_equivalence` (EQ:462); Main:552–554 | The Born dictionary is in the definition of $Q_{\rm fb}$ (EQ:205) | yes | not applicable: the dictionary is a definition (EQ:205) | yes, by definition | Exhibits the form and selects nothing (Main:20, Main:556) |
| R2 | The class version: for every $p>0$, $Q_{\rm fb}^{p}=S$. Here $Q_{\rm fb}^{p}$ is $Q_{\rm fb}$ with readout $\lVert U\rVert^p$, restricted to realizations whose readout is normalised on every visited column | A (below): $S\subseteq D\subseteq Q_{\rm fb}^p$ by `D_imp_Qfb`'s 0/1 weights (EQ:302); $Q_{\rm fb}^p\subseteq S$ by the normalisation restriction, as in `sum_chain` (EQ:99). X: P1(a)–(b), at the stated grid | H-LIN on the fixed basis; measurement at every step from a diagonal initial law (Main:552); the normalisation restriction | yes | not applicable | not applicable | The realizable law class does not depend on $p$, so no criterion on which finite-horizon laws are realizable selects $p$. A selection must come from a constraint on admissible operations (R3). Conditional on the normalisation restriction. ELABORATING |
| R3-N | **Necessity (antecedent: every admissible operation is monomial in the read basis).** Under H-LIN ∧ H-RF$_p$, if every admissible operation is a phased permutation in the read basis, every $p>0$ fits every record | A: unimodular entries and $p$-normalised preparations are preserved (below); BORN-SRC-1 C2 (Aaronson, quant-ph/0401062 §2, read via T3 §3.1, not first-hand here). X: P1(a); r2 K2 control | H-LIN (unitary operations; preparations as stated), H-RF$_p$ | yes | **no.** H-LIN and H-RF$_p$ are posited (§1). The antecedent itself holds for the stated interventions on the configuration carrier, whose observable operators are monomial (GR:260; Main:556; BRIDGE §5.1 Status [D]) | not applicable | A non-monomial unitary in the read basis is necessary for any record to discriminate $p$. Scope: unitary operations. A weighted monomial Kraus family $\{2^{-k/2}P_\sigma\}$ is normalised under $|K|^p$ only at $p=2$ (r2 K2; BRIDGE §5.1 *Position* (d) [D]), because the weights are fixed by the quadratic completeness $\sum K^\dagger K=1$, which puts the exponent in by hand |
| R3-C | **Conditional forcing (antecedent: one admissible unitary has a visited column with at least two nonzero entries in the read basis).** Under H-LIN ∧ H-RF$_p$, that column forces $p=2$ | A: the column lemma below; BORN-SRC-1 L2. X: P1(b)–(c); r2 K4, K5 | H-LIN, H-RF$_p$ (unrenormalised); the antecedent | yes | **no.** H-RF$_p$ posits the Born form up to its exponent; the forcing is a consistency condition on that posit, not a derivation of the exponent. The antecedent is not supplied for the stated access (below, *FI-1*) | yes | Inside the posited power family only. For general $f$ the antecedent is not sufficient (R4; BORN-SRC-1 C4; §4.3's $g$) |
| R4 | General $f$: on $n\ge3$, if every point of $\Delta_n$ is the $\lvert\cdot\rvert^2$-profile of a column of some admissible $U$, and (d′) holds, then $f(u)=u^2$ | L/A: Logiurato–Smerzi, arXiv:1202.2728 (BORN-SRC-1 L1; the reviewer's exact rank checks); countercontrol C4 shows that one non-monomial $U$ is not enough | Density ("column-richness") of a *natively sourced* family; (d′); $n\ge3$ | yes | **no.** No native dense family exists, since even FI-1 is not supplied. (d′) is O1, undecided. Applied to representational families such as Main:212's $W$, it is circular (BORN-SRC-1 review 9(ii)) | yes | Fixes the readout only after a dense family and O1; the law still needs (b)–(d) |
| R5 | Gleason/Busch: noncontextual frame functions on the projector (effect) lattice of $\dim\ge3$ give the trace rule | L [54] | (d1)–(d4) of BORN-SRC-1 §4(d) | yes | **no.** The one native context result, `complete_passive_iff_commutative` (CentralObservation), shows that passive observation reads one context. No frame-function predicate exists in the kernel | yes | Would give (a) only through (d) |
| R6 | Masanes–Galley–Müller: the measurement postulates are operationally redundant, given QM's pure-state, unitary and composite structure | L (via T3 §3.1) | Complex kinematics and tensor composites | yes | **no.** "Complex matrix kinematics" is "taken as given … deriving that kinematics is open" (Main:218, Main:564) | yes | Conditional on supplied kinematics |
| R7 | Continuum ontic carrier ($\lambda\in S^2$, sign read). Re-preparation uniform on the outcome hemisphere gives $P(+\mid a)=1-\theta/\pi$; only the cosine-weighted law gives $(1+\cos\theta)/2$ | P/A, AP1:1012–1016. A1R: two uniform vectors with an argmax rule give the cosine density, then fail on the next read (final Z+ probability 2/3, not 1/2) | The carrier, the re-preparation measure, the readout rule | yes | **no.** AP1 Q-B, "reads [that] re-prepare with the cosine-weighted law, without a supplied measure", is open (AP1:1082–1085) | the cosine choice does; the uniform-hemisphere choice does not | On this route the Born law is a choice of measure or carrier: (a) collapses into (b) |
| R8 | Seed/response carrier (B3/E-AR). The quadratic response $1[q<\lvert z_1\rvert^2/\lVert z\rVert^2]$ and the uniform seed are inputs. The carrier is two-mode, $z\in\mathbb C^2$ | P/A: WMB §1 ("The quadratic response and uniform law are explicit inputs, not a derivation of Born selection"); T3:246 | AR-1–AR-6 | yes | **no** | yes, by construction | At $n=2$, normalisation does not select $f$ (BORN-SRC-1 C1: $g(x)=x+x(1-x)(1-2x)$). (a) and (b) are one pushforward (T3:246) |
| R9 | Finite uniform resources with finite deterministic readout and positive conditioning give rational weights | A: T3 §6.1 (on `main`; see §6 F-c) | Finite counting | yes | no: posit (iv), not derived (Main:726) | no at irrational targets ($\cos^2\pi/8$; $2\sqrt2$) | An exact Born law at irrational points needs an atomless or calibrated source: a (b) ingredient, not an exponent selection |
| R10 | μ-form / μ-number: the Born *form* is invariant in μ; the *numbers* change with μ (swap, CE-8) | A (QB3 §§1, 4–5; reviewed ACCEPT in QB3-EVIDENCE-REVIEW) | Finite bijections; non-native examples only | yes | not applicable | not applicable | On the fixed-basis route the numbers are (b)'s, not (a)'s |

**Column lemma (R3-C).** Let $u$ be a unit column, $\sum_j|u_j|^2=1$, so $|u_j|\le1$.
- For $0<p<2$: $|u_j|^p\ge|u_j|^2$, with equality iff $|u_j|\in\{0,1\}$. So $\sum_j|u_j|^p=1$ iff
  exactly one $|u_j|=1$.
- For $p>2$ the inequality reverses, with the same equality case.

Hence, under unrenormalised H-RF$_p$ with $p\neq2$, every visited column must be monomial. For
a unitary, "some column has at least two nonzero entries" is the same as "non-monomial" (r2 K3:
an invertible matrix whose columns each have one nonzero entry is monomial). R2 does not use this
lemma.

**R3-N, preparations included.** With phased-permutation dynamics only, a $p$-normalised
preparation stays $p$-normalised, and a basis state is $p$-normalised for every $p$. Each read
then returns $|{\rm amp}|^p$, which is a law for every $p$, so no record discriminates $p$. A
*supplied* 2-normalised coherent preparation is outside H-LIN's preparation class: for
$(2^{-1/2},2^{-1/2})$, $\sum|a|^p=2^{1-p/2}$, which is 1 only at $p=2$ (r2 K5). Such a
preparation is a non-monomial column in disguise.

**FI-1 and R3.** FI-1 (BRIDGE §5.1 [D]) is: the finite bijective dynamics, with the
visible/hidden trace-out and the observer's stated read/write access, supplies a non-monomial
admissible operator on the configuration carrier at level one. BRIDGE states it as a necessary
condition, in one direction only, for exact finite endomorphic operational QM within the
structural architecture on that carrier (GR:270; K `exists_nonMonomial_of_layerFlowExecutable`),
not for finite-accuracy reproduction of quantum statistics (Main:566), and not as sufficient for
it (K `polarizedTheoryC_not_qm`).
- *R3-N's necessary condition, read on the configuration carrier, entails FI-1.* A non-monomial
  admissible unitary is a non-monomial admissible operator.
- *FI-1 does not entail R3-C's antecedent.* $K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is
  non-monomial and both its columns are monomial, so its column readout fits every $p$ (r2 K1;
  BRIDGE K2 [D]). FI-1 would have to be supplied by a unitary for R3-C to apply.
- *On encoded carriers* non-monomial encoded maps arise without FI-1 (BRIDGE §5.1 [D], citing
  QP:79–98, QP:846–877, at single-qubit stabilizer scope). There the probabilities are N2's
  (§4.3), not readings of an amplitude, so R3 does not apply to them.
- FI-1 is not the earliest or the only gap on the route to operational QM (§0 item 2).

**Answer to Q1.** Every result that constrains $p$ or $f$ does so conditionally:
- through posited H-RF$_p$ and a non-monomial admissible unitary (R3-C), or a dense native family
  with (d′) (R4);
- through a supplied context structure (R5);
- through supplied kinematics (R6);
- or through a supplied measure or response (R7–R9).

None of these antecedents is in column (ii). What holds without a posited readout form concerns
law classes: the class of realizable finite-horizon laws does not depend on $p$ (R2, conditional
on the normalisation restriction), so a selection of $p$, if any, has to come from a constraint
on admissible operations. Such a constraint (R3-C) exists only inside posited H-RF$_p$.

***

## 4. Question 2: do today's findings change the open question?

### 4.1 The complex structure $J$ off the null modes (BRIDGE F4 [D]; REVIEW B3, probes R1/R1b [D])

*What is claimed.* On one non-null Fourier mode of the real lift, the positive-frequency
$J=(f-\cos\omega)/\sin\omega$ satisfies the following:
- $J^2=-1$;
- $J$ commutes with the mode map and with the cubic action;
- the symplectic commutant of the update on six components is $\mathfrak u(6)$.

No such $J$ exists at the null modes of $\alpha=1/d$. It is defined mode by mode and is nonlocal
in space. Two items are open: whether $\Sigma$ is $J$-Hermitian, and the lift itself (S13;
SM:232).

*The favourable reading, pressure-tested (§A.31).* "A complex carrier of dimension 6 with a
transitive unitary group supplies R4's dense family on $n\ge3$, so (d′) would give $u^2$." Four
gaps block it, and each is a premise of R4:
1. **Mathematical availability versus derivation.** $\mathfrak u(6)$ is the commutant of the
   dynamics, a mathematically available symmetry. R4 needs operations derived from OI that the
   observer executes and reads. FI-1, which asks only for one non-monomial admissible operator,
   is itself not supplied (§3, *FI-1 and R3*). Main distinguishes a derived continuous path from
   an available operation (Main:274, Main:590).
2. **Read basis.** (d′) is modulus-only in a fixed read basis.
   - In the $J$-mode basis the update acts diagonally, by mode phases. It is therefore monomial
     there, and every $p$ fits (R3-N).
   - The site basis carries no $J$-amplitudes, because $J$ is nonlocal in space.

   Which basis, if any, the observer's records read is not stated anywhere read.
3. **Null modes.** The candidate fails on the sector at $\alpha=1/d$.
4. **The lift.** The real lift's derivation from φ is open (SM:232).

Even with all four supplied, a dense family would be coherent mixing; the law would still need
(d′) or (d1)–(d4), and (b)–(c).

*Effect on #1059.* None on status. The finding names the first record of a $\dim\ge3$ complex
carrier with a transitive unitary symmetry. Every other non-monomial route on `main` is two-mode
(R8) or stabilizer-only (§4.3). That makes it the place where the next question (§5) is posed.
**ELABORATING.**

### 4.2 H-Bell as the Bell selection (BRIDGE F2, B20 [D]; SHM §8.3, §9 [D]; Main §3.3)

- **What it selects.** H-Bell selects the branch that gives up ontic parameter independence
  (Main:403–406, Main:414; Substratum:131–133). Its clauses (i)–(iii) are:
  - ontic parameter dependence;
  - operational no-signalling;
  - curvature stability.

  They name no numerical correlation law.
- **What it does not select.** The unrestricted response-table class reaches the PR box
  (Main:362). Parameter dependence alone therefore does not select the quantum set. Tsirelson
  soundness is a separate hypothesis with QM-only support (SHM §9 [D]; Substratum:481: "Bare
  C1–C4 or graph locality do not enforce Tsirelson").
- **What it shares with #1059.** Exact quantum Bell values need irrational weights, which finite
  uniform resources do not supply (R9; SHM T6 [D]). Any exact H-Bell realization would therefore
  need the same unsourced ingredient as #1059(b)'s atomless or calibrated branch. That is a
  shared necessary ingredient. No formal map identifies H-Bell's obligation with (a) or (b), and
  none is asserted here (Code Review Rules, "Bridge and no-go scope").
- **Relation to FI-1.** H-Bell is a gap independent of FI-1, not after it: quantum Bell
  statistics are realized to finite accuracy by fixed bijections once ontic parameter dependence
  is given (Main:403–406, Main:566, Main:584; BRIDGE §5.1 *Position* (c) [D]).
- **Effect on #1059.** None on (a). It adds a planning cross-reference to (b) only.
  **CONFIRMING.**

### 4.3 Access restrictions with only QM-matching support (SHM §9 [D]: SA-1(c), Tsirelson soundness, null-result invasiveness)

- **Where the probabilities come from.** On the SA-1 route the probabilities of the
  stabilizer-scope sequential $Z/X$ law come from N2, the uniform law on unknown slots, that is,
  from the measure (b). The amplitude dictionary appears only in the comparator. So the route
  never reads $f$ off an amplitude, and R3 and R4 do not apply to it. This is why the route does
  not bear on (a). AP1 already scopes out "Born-rule selection beyond the values `0, ½, 1`"
  (AP1:1062). The route's carrier is an encoded one.
- **Stabilizer agreement would not select $f$ in the general class (a-gen).** Even if the route
  did read amplitudes, stabilizer-scope agreement would constrain a general $f$ only on
  $\{2^{-k/2}\}$:
  - *$n\le3$ (P2, computation-supported).* Every $n\le3$ stabilizer state (6, 60 and 1080 states,
    matching the known counts) has computational-basis moduli that are equal on a support of size
    $2^k$. $f(u)=u^2+u^2\prod_{k=0}^{3}(u^2-2^{-k})^2$ is nonnegative by construction (a sum of
    $u^2$ and $u^2$ times a square) and has $f(0)=0$; it is not $u^2$, normalises every one of these
    states exactly, and fails on $(\cos\frac\pi8,\sin\frac\pi8)$. Mutation control: removing the
    $k=3$ factor breaks normalisation on an 8-element support.
  - *All $n$ (computation-supported).* $g(u)=u^2\bigl(1+\sin^2(\pi\log_2u^2)\bigr)$, $g(0)=0$,
    equals $u^2$ at every $2^{-k/2}$ (exact for $k\le40$; immediate for all $k$, since
    $\sin(-k\pi)=0$), so it normalises every flat support of size $2^k$; and
    $g(\cos\frac\pi8)+g(\sin\frac\pi8)\in[1.43249507…]$, not 1 (r2 K6, interval arithmetic;
    the reviewer's rv C5 reports the same function).

  This is the stabilizer-scope analogue of BORN-SRC-1's C4. *Within the power family* the
  position is different: the single dyadic point $2^{-1/2}$ on a support of size 2 forces $p=2$
  under H-RF$_p$ (r2 K5), and the Hadamard is a non-monomial stabilizer operation. If the route
  read amplitudes under H-LIN ∧ H-RF$_p$, R3-C would apply to it. It does not read amplitudes.
- **Effect on #1059.** None on status. The SA-1 route does not bear on (a), because its
  probabilities are N2's; and stabilizer-point agreement would not select $f$ in (a-gen) beyond
  the dyadic points, whether or not SA-1(c) is ever independently justified. Its numbers belong
  to (b): they apply N2 to supplied ready cells through H-PREP, which is an open hypothesis
  (AP1:418; SHM §9 [D] cites it as AP1:417).
  **ELABORATING** (P2 and $g$ are new as checks; the scope statement was already at AP1:1062).
- **One inconsistency between drafts** (§6 F-a). SHM §9's N2 row answers column (ii) "yes for the
  counting measure, Main's maximal-entropy selection". Main:726 (iv) calls that selection "not
  derived", and BRIDGE B3 types it Op. Under §1's columns it is a posit, not a column-(ii) "yes".

### 4.4 FI-1 and non-monomial mixing: necessary under the stated hypotheses, not sufficient (BRIDGE §5.1 [D])

BRIDGE §5.1 *Position* (d) states one direction: on permutation unitaries "$\lvert U\rvert^p$ gives the same
table for every $p>0$" (Main:556). R3-N is that direction, extended to phased permutations and to
the preparation class of H-LIN. R3-C is the conditional converse inside posited H-RF$_p$, with a
unitary antecedent stronger than FI-1 (§3). Consequences:
- **(a-pow)**, the exponent in the power family, has as *necessary* conditions H-LIN, posited
  H-RF$_p$ and a non-monomial admissible unitary in the read basis, which on the configuration
  carrier entails FI-1. These conditions are not sufficient to *derive* the exponent: what
  forces $p=2$ under them is the posited form, so supplying FI-1, or any mixing unitary, would
  establish only that the posited power readout is consistent at $p=2$ alone.
- **(a-gen)**, the readout function in general, needs a dense native family on $n\ge3$ with
  (d′) (R4), or the (d1)–(d4) context structure (R5). O1 decides which target applies.
  Today's findings supply none of these antecedents.
- **The law**, beyond the readout, needs (b)–(d) and composites; coherent mixing supplies none
  of them (§0 item 2).
- **One §A.34 point about BRIDGE.** Its r2 §6 "Born statistics" row read "An independently
  justified selection of the quadratic functional on non-monomial (state-mixing) operations;
  equivalently a source of non-monomial admissible operators". Only the necessity direction
  holds (R3-N); sufficiency fails for general $f$ (C4; P2; $g$) and for non-unitary operators
  (r2 K1). BRIDGE r3 (§6, row "Born statistics") reads "which presupposes a source of
  non-monomial admissible operators", which is the necessity direction (§6 F-b).

**ELABORATING.** The necessity direction is stated in BORN-SRC-1 §4(a) and BRIDGE §5.1 *Position* (d).
This unit adds the conditional converse with its unitary scope, the separation of FI-1 from
R3-C's antecedent, and the class version R2.

### 4.5 What is open on #1059 after today

| Part | Status at `fd539e15` | Prerequisites, after today | Change |
|---|---|---|---|
| (a-pow) exponent in the power family | open | Necessary: H-LIN, H-RF$_p$ (both posited) and a non-monomial admissible unitary in the read basis (on the configuration carrier, this entails FI-1, #1211). Not sufficient to derive the exponent: under them $p=2$ is forced by the posited form | Necessary conditions located; not reduced to FI-1 |
| (a-gen) full quadratic dictionary | open | A native dense family on $n\ge3$ (which needs FI-1) + O1's target ((d′), or (d1)–(d4)) | None. $J$ names a candidate carrier only (§4.1) |
| (b) hidden-sector measure | open; analysis paused | Unchanged. On the continuum and seed routes it carries the Born law itself (R7, R8) | None. SHM's N2 column (ii) is overstated (§4.3) |
| (c) preparations across settings | open; blocked on O-INS | Unchanged. Exact irrational targets need a non-finite source (R9) | None |
| (d) context independence | no kernel result | Native contexts on $\dim\ge3$. At two-qubit stabilizer scope (60 states, 105 stabilizer bases) every frame function is a trace form $\langle s\lvert X\rvert s\rangle$ with ${\rm Tr}\,X=1$, but nonnegativity on those states does not force $X\ge0$ (reviewer's check rv C6, generic, two-qubit only, re-run here with identical output; its nonnegativity step is numeric at 30 digits). The stabilizer-scope Gleason route therefore fixes the form and fails at state positivity and at (d1)'s covering | None |

The QB3 limitation stands as stated: "OI has not yet been shown to derive the Born rule or select
the physical probability measure."

***

## 5. Question 3: the smallest decisive next paper question

**NQ-1059.** *Under the observer's stated access (AP1's P1–P3 with H-PREP, or any access stated
on `main`), is there an executable operation that acts on a configuration-carrier block of
dimension $\ge3$ by a unitary that is non-monomial in the block's read basis and not
stabilizer-only? Not stabilizer-only means that some column has a $|\cdot|^2$-profile that is not
uniform on its support. The first place to pose this is the $J$-complex non-null sector of the
real lift (§4.1). The question also asks which read basis, if any, the records use there.*

- **Why it is decisive.** Either answer changes what #1059 can do.
  - *No* (on the classes examined): (a-gen) and (d) have no route on `main` whatever O1
    decides, and (a-pow) lacks a necessary condition for the stated access. #1059's own content
    is then (b) and (c), with (a) and (d) carried as open and conditional on access that the
    corpus does not supply.
  - *Yes*: it supplies a necessary condition for (a), not the exponent and not the law. It is
    the first object on which O1's two targets differ in content: (d′) with density would give
    $u^2$ by R4; Gleason/Busch would further need the projector lattice of (d1). O1 then becomes
    decidable on content rather than in the abstract. The law would still need (b)–(d).
- **Why it is small.**
  - It needs no measure, no preparation law and no comparator.
  - Its negative branch can be checked against existing records: the quarter-phase bounds;
    MECH-1, MECH-2 and M-INACC-1 (cited at BRIDGE §10 [D]); the kernel negatives for the stated
    access at Main:590 and GR:270.
  - Its positive branch needs one exhibited operation, shown to be derived from OI and
    executable rather than mathematically available, plus a read-basis statement.
  - Generic parts, such as the stabilizer criterion and the profile test, are exact checks of
    the P2 kind.
- **Scope guards.**
  - It is posed for the stated access on the configuration carrier. A negative answer is not a
    no-go for extended mechanisms, for encoded carriers or for the unresolved site-space
    formulation (Main:590).
  - It overlaps #1211's NQ1 (the $J$ question) and FI-1. It must not duplicate them. It adds the
    dimension-$\ge3$, unitary, non-stabilizer and read-basis conditions that #1059 needs.
  - It adopts no premise. (d′) and Gleason remain O1's to choose.

*Alternative, if the owner prefers to stay within (b):* AP1's Q-B (AP1:1082–1085), stated for
#1059. Which of Main's measure branches (α–δ), applied to the minimal continuum carrier with
conditioning on the record, yields the cosine-weighted re-preparation without a supplied
density? This was ranked second: the one-vector outcome under γ looks predictable from AP1:1013,
so it risks being a relabelling rather than a test (§A.31). A pre-registered decision rule would
be needed first.

***

## 6. Findings for other records (recorded only; no edit made)

- **F-a (SHM §9, N2 row, draft r5; same in r4).** Column (ii) reads "yes for the counting
  measure, Main's maximal-entropy selection". On each finite cycle the uniform law is unique
  (Lemma 3's first clause, Main:56; K `ensembleDetermined_of_transitive` for transitive φ). The
  global counting selection is posit (iv): "a standard but substantive epistemic postulate, not
  derived" (Main:726); Main:56 calls it "a selection principle". Suggest "posit (Op) for the
  global selection" to the #1210 reviewers.
- **F-b (BRIDGE §6, "Born statistics" row).** The r2 row's "equivalently a source of
  non-monomial admissible operators" asserted an equivalence of which only the necessity direction
  holds (R3-N; the sufficiency counterexamples are C4, P2, $g$ and r2 K1). §A.34. BRIDGE r3
  (`a5d7aad1…`) reads "which presupposes a source of non-monomial admissible operators", which
  states the necessity direction only. No further suggestion.
- **F-c (T3 on `main`).** The landed file's header (T3:3) still reads "independent review
  pending, 2026-11-07". #1059 c.6705021068 records a separate independent ACCEPT on #1173 for
  `8e764171`, blob `b31d0549`. The landed blob at `fd539e15` is `1c077f62`, which has the same
  content apart from the author-label line (`/root/writer_probability` → `writer_probability`).
  This is a stale status line in a mutable record (§A.46 item 4). Its use above is limited to
  statements it cites from `main` and to T3 §6.1's rationality argument, which is elementary.
- **F-d (Main; BORN-SRC-1 F1/F2 overtaken by `484006b1`).** Commit `484006b1` (2026-11-07), an
  ancestor of `fd539e15`, rewrote Main:226 ("The Born form $p=|U|^2$ is the dictionary of
  $Q_{\rm fb}$ (§3.4); its quadratic exponent is a frontier item") and Main:351 ("Representation
  dictionary of $Q_{\rm fb}$, not selected (§3.4)", in the Barandes-route (§3.1) column). §3.1
  therefore now carries an exponent frontier clause, and the "(§3.1)" pointers at Main:20, the
  §3.1 discussion that Main:556 refers to, and ch18:34 resolve to it. BORN-SRC-1 F2's premise
  ("§3.1 … contains no exponent clause") no longer holds. One candidate for O2 remains:
  Main:648, "The characterization theorem establishes the Hilbert space, unitary dynamics, and
  Born-rule transition probabilities", can be read as available → derived against Main:20. It is
  not in BORN-SRC-1's site list (whose lines are at `02009693`), and it belongs to O2's remit, not
  #1059's.
- **F-e (book glossary; BORN-SRC-1 F3, still present).** `book/glossary.md:21` reads "The
  framework therefore does not list a separate 'quadratic-exponent selector' as an unresolved
  foundational theorem at that layer", while Main:20 and Main:226 name the quadratic exponent as
  a frontier item. This is a cross-document status inconsistency for O2's remit (§A.25). It
  selects no exponent.

***

## 7. Owner questions

- **OQ-1.** Should #1059 record a non-monomial admissible unitary in the read basis (on the
  configuration carrier, entailing FI-1, #1211 §5.1) as a *necessary* prerequisite of (a), with
  the explicit statement that it is not sufficient for the exponent or the law, and (a-gen) as
  needing a dense native family and O1?
- **OQ-2.** Is NQ-1059 (§5) the next #1059 unit, given that it overlaps #1211's NQ1? Or should it
  be folded into #1211 as an added condition (dimension $\ge3$, unitary, non-stabilizer, read
  basis)?
- **O1 and O5 (existing, undecided).** Today's findings supply neither O1 target's antecedent
  (§4.5). If NQ-1059's answer is wanted first, O1 can wait for it. O5 (drop BORN-1 for a cited
  scope remark) is unaffected; R3 and R4 here are cited known results, not a new lemma.

***

## 8. Verification scope

- **Read in full:**
  - #1059's body and all 23 comments;
  - #914 c.6567852459, c.6567870091 and c.6567879365 (BORN-SRC-1 and its review);
  - #1169 c.6740116927;
  - QB3 §1;
  - BRIDGE r2 §§0–3, §5.1, §6 (ingredient rows), F4 and §11; BRIDGE r3 §0 item 8, §5.1 and the
    §6 "Born statistics" row (r2 of this unit);
  - REVIEW (bridge r1) in full; REVIEW-r2 RB1–RB3 (r2 of this unit);
  - SHM §0, §8 rules, §8.3, §8.4 and §9; SHM r5's first line and the r4/r5 N2 row (r2);
  - this unit's review, REVIEW-1059, in full (r2).
- **Read at the cited lines:**
  - Main:20, 56, 208–226, 288, 345–351, 552–556, 576–580, 590, 646–656, 684, 726;
  - T3:1–160 and 240–270; T3 at `8e764171` vs `fd539e15` (diff, r2);
  - AP1:240–250, 830–845, 975–1095;
  - WMB:1–40 and 205–222;
  - A1R:1–90;
  - Structure:1117; Substratum:16–68, 131–145, 481;
  - EQ:99, 147, 190–340, 462;
  - `book/ch18-beyond.md`:16, 30–36 and `book/glossary.md`:21 (r2);
  - the H-Bell round-1 preregistration head.
- **Searched at `fd539e15`** (`git grep -i` over `verification/`, `papers/` and `book/`): "born",
  "quadratic exponent / functional / sensor / rule", "|U|^p", "hemisphere", "cosine-weighted".
  The negatives stated in §§3–5 ("no native dense family", "no frame-function predicate", "no
  record stating a read basis for $J$-amplitudes") are scoped to that search, to BORN-SRC-1's
  search at `02009693`, and to the files read. The §A.19 sweep also covers the read-write-cycle
  equilibrium mechanism proposal (Main:684, "the cosmological realization's mechanism proposal";
  ch18 §18.2, ch18:34, "structural commitment") and `book/glossary.md:21` (F-e): neither selects
  the exponent. Lean files were read only at EQ's lines. No kernel build was run.
- **Probes** (generic objects only; exact sympy, Gaussian-integer and interval arithmetic; run
  with `python3 -I`; exit status 0):
  - `probes/p1_fixed_basis_power.py`, sha256 `82361ef8…a3d2`, output `probes/p1.out`. Checks:
    permutation tables at $p\in\{1/2,1,2,3,7\}$ for $n\le4$; the column lemma at $p=1,4$ on 28
    grid profiles; a Cayley unitary with column $|U|^4$-sums 81/169, 21105/48841 and 1341/3757
    (control).
  - `probes/p2_stabilizer_points.py`, sha256 `90efad3b…a94c`, output `probes/p2.out`. Checks:
    stabilizer counts 6/60/1080 (control); uniform-modulus supports; normalisation of the
    countercontrol $f$; the non-stabilizer control; the mutation control. Scope: $n\le3$.
  - `probes/r2_fi1_scope.py` (r2), sha256 `3f32e79f…1091`, output `probes/r2_fi1_scope.out`
    (`bbe270c0…3e70`). Imports no earlier probe. Checks: K1 non-monomial operator with monomial
    columns; K2 weighted monomial Kraus families (complete, normalised only at $p=2$) with the
    phased-permutation control; K3 column-monomial invertible ⇒ monomial (exhaustive support
    patterns, $n\le4$); K4 unrenormalised versus renormalised readout on $(1/3,2/3,2/3)$; K5
    $2^{1-p/2}$; K6 the function $g$ (exact at $2^{-k/2}$, $k\le40$; interval enclosure at
    $\cos\frac\pi8$).
  - The reviewer's `review/rv_1059_checks.py` (`3960d7c8…2264`) was re-run here with
    `python3 -I`: exit 0, output byte-identical to `review/rv_1059_checks.out`. Only C6 is
    relied on (§4.5, row (d)), as the reviewer's check.

  R2's and §4.3's statements rest on the paper argument plus these checks, and are marked
  computation-supported where the check is the only support.
- **Not done:** no computation on any OI mechanism, the real lift or $J$ included. No literature
  source was re-read first-hand: Logiurato–Smerzi, Aaronson and Masanes–Galley–Müller are cited
  as BORN-SRC-1 and T3 report them. QP was not read here; its lines are cited through BRIDGE
  [D]. No #1082 file was opened beyond what QB3 lands. No #1210 or #1211 file was edited.
