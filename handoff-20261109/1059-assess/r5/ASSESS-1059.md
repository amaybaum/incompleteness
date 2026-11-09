# BORN-SEL (#1059): re-assessment of the open question against the #1210 / #1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r5, after the
independent reviews `review/REVIEW-1059.md` (r1, sha256 `8cbfe227…7446`, REVISE),
`review/REVIEW-1059-r2.md` (r2, sha256 `a262ad4f…9710`, REVISE, bounded),
`review/REVIEW-1059-r3.md` (r3, sha256 `d9d8fd93…325c`, REVISE, bounded) and
`review/REVIEW-1059-r4.md` (r4, sha256 `93ae3b17…ea87`, REVISE, bounded); pending a fresh,
independent review.** Nothing here is adopted, promoted or proposed for the manuscripts. A
review ACCEPT, if reached, authorizes nothing further. The r1–r4 texts are kept unchanged
at `r1/ASSESS-1059.md` (`d5b314af…d931`), `r2/ASSESS-1059.md` (`f99a4c3b…20d2`),
`r3/ASSESS-1059.md` (`85fd3d4b…8465`) and `r4/ASSESS-1059.md` (`7fa70fc0…c085`); each change is
mapped in `DISPOSITIONS-r2.md`, `DISPOSITIONS-r3.md`, `DISPOSITIONS-r4.md` and
`DISPOSITIONS-r5.md`.

- **Accountable home:** #1059. Feeds #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, recorded in #1059 c.6740117293 (posted
  2026-11-09T12:31:13Z), full record #1169 c.6740116927 (posted 2026-11-09T12:31:12Z). Option
  text, verbatim: "**#1059/#1049/#868 audits** — One paper-only unit each, re-assessing its open
  question against today's #1210/#1211 findings (Born exponent; linear vs affine dynamics;
  joint-test validity), each with a fresh review. Exact generic checks only." Not authorized
  (c.6740117293): "computation on an OI mechanism, new physical assumptions, freeze, dispatch,
  manuscript changes or merges". This unit makes no repo, git or GitHub write. Owner direction
  of 2026-11-09, recorded in #1169 c.6740778880 (posted 2026-11-09T13:05:46Z), applied from r2:
  three distinctions are kept ("Configuration carriers versus encoded carriers. Mathematical
  availability of an operation versus its derivation from OI. Generating coherent mixing versus
  establishing the complete quantum probability and composition rules."), and an affirmative
  answer on coherent non-monomial operations "would not by itself prove the Born exponent,
  H-Bell or full OI–QM equivalence". Wherever FI-1 or non-monomial mixing appears below it is
  stated as necessary, under the hypotheses named with it, and not sufficient for the exponent
  or the law.
- **Checks run.** Six scripts of exact checks on generic mathematical objects (permutation,
  Cayley and Kraus matrices; isometric dilations and their Gram matrices; matrix exponentials and
  the Lie algebras they generate; columns and vectors; stabilizer states; one real function), in
  `probes/` (§8). No
  computation was run on an OI mechanism. A statement supported only by such a check is marked
  *computation-supported*.
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09). Every `path:line` is at that commit unless marked otherwise. "Main" =
  `papers/Main.md`; "QB3" = `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`;
  "T3" = `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/probability-source-assessment.md`;
  "AP1" = `verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md`;
  "WMB" = `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/whole-model-bridge.md`;
  "A1R" = `verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/a1_reset_v6/REPORT.md`;
  "EQ" = `verification/lean-mathlib/OIBridge/Equivalence.lean`;
  "QP" = `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`;
  "GR", "SM", "Substratum", "Structure" = `papers/GR.md`, `papers/SM.md`, `papers/Substratum.md`,
  `papers/Structure.md`.
  "BORN-SRC-1" = the reviewed audit quoted verbatim in #914 c.6567870091 (audit) and c.6567879365
  (review with final check), summarized in #914 c.6567852459; it is at base `02009693`, and its line
  numbers are at that base.
- **Today's drafts, used as hypotheses only (§A.46 item 7).** None is reviewed to ACCEPT at the
  hash read, and none is on `main`. They are cited for what they claim; no conclusion below rests
  on them alone.
  - "BRIDGE" = `scratchpad/bridge/r4/BRIDGE-UNIT1.md` r4, sha256 `4e97610d…85e2` (#1211 unit 1),
    reviewed REVISE in `scratchpad/bridge/review/REVIEW-UNIT1-r4.md` (`e489fc19…2bc7`). Every
    BRIDGE citation below was checked against r4; its phase/mixing passage is read as corrected
    by that review's R4-B1 and R4-B2 (§0 item 2). The current file
    `scratchpad/bridge/BRIDGE-UNIT1.md` holds r5 (`78f1098e…91a4`), reviewed ACCEPT WITH NITS in
    `scratchpad/bridge/review/REVIEW-UNIT1-r5.md` (`0ef5644f…8c76`), a draft review, not `main`;
    r5 was not read for this unit, and the BRIDGE citations stay pinned to r4. The r3 text, read for r2 of
    this unit, is `scratchpad/bridge/r3/BRIDGE-UNIT1.md` (`ee1c83c0…8219`), reviewed REVISE in
    `scratchpad/bridge/review/REVIEW-UNIT1-r3.md` (`7a6a7f1c…cc27`). The r2 review "REVIEW-r2" =
    `scratchpad/bridge/review/REVIEW-UNIT1-r2.md` (`3cdf7dc2…4eb3`, REVISE; it rejected the r2
    ordering of FI-1 as the earliest unsupported step, RB1). The r2 text read for r1 of this unit
    is `scratchpad/bridge/r2/BRIDGE-UNIT1.md` (`3905569b…103a`).
  - "SHM" = `scratchpad/qphen/r5/SHARED-MECHANISM.md` r5 §§8–9, sha256 `a7206701…cc4d` (#1210
    Phase 1). The r4 file is `qphen/r4/SHARED-MECHANISM.md` (`23ec1ef1…fd11`); the N2 row used
    in §6 F-a reads the same in both.

***

## 0. Summary

1. **#1059's question is unchanged in status.** No record on `main`, and no draft of
   2026-11-09, derives the quadratic exponent, or the Born probability law, from independently
   justified OI principles. (a)–(d) of BORN-SRC-1 stay open. The Born dictionary of $Q_{\rm fb}$
   is a definition (`QfbReal.born := ‖Q.U b' b‖ ^ 2`, EQ:205; Main:20, Main:556).
2. **Generating state mixing and deriving the exponent are different things.** Under the
   hypotheses H-LIN ∧ H-RF$_p$ (§1, both posited), a unitary that is non-monomial in the read
   basis is *necessary* for any record to discriminate the exponent: with phased-permutation
   unitaries only, every $p>0$ fits every record (R3-N). That necessity is for record
   discrimination and holds only within those hypotheses; a selection of $p$ need not be
   record-based, and outside H-LIN weighted monomial Kraus families also discriminate $p$ (§3,
   R3-N). Non-monomial mixing is *not sufficient*:
   - *for the exponent:* a column with two or more nonzero entries fixes $p$ at the exponent of
     its own normalisation (column lemma, §3; r3 check E1). Within H-LIN, the value 2 in R3-C is
     therefore supplied by H-LIN's posited unitarity, the quadratic invariant of the complex
     matrix kinematics that Main:218 takes as given, and H-RF$_p$ supplies only the power form.
     R3-C is a consistency condition between two posits and derives no exponent from OI. Without
     posited unitarity, a square (endomorphic) non-monomial linear operation with H-RF$_p$
     required on every amplitude vector also fixes $p=2$ and is then unitary (§3, *Without
     posited unitarity*); the 2 then comes from the posited linear amplitude kinematics, for
     complex amplitudes the one Main:218 takes as given. For a non-square operation, such as a
     Kraus family's dilation, H-RF$_p$ on every amplitude vector holds at each $p>0$ for some
     non-monomial family, and the 2 comes only from completeness, the posited quadratic
     normalisation (§3). For a general readout $f$, a
     non-monomial column does not fix $f$ (BORN-SRC-1 C1 at $n=2$ and C4 at $n=3$; at stabilizer
     points, P2 and $g$ of §4.3);
   - *for the law:* the Born law further needs the measure (b), preparations across settings
     (c) and context structure (d), and coherent mixing supplies none of them, nor the
     composition rules.
   
   FI-1 (BRIDGE §5.1 [D]) asks for a non-monomial admissible operator on the configuration
   carrier at level one; BRIDGE states it as a necessary condition, in one direction only, for
   exact finite endomorphic operational QM on that carrier (GR:270;
   K `exists_nonMonomial_of_layerFlowExecutable`). With R3's class read as the operations the
   stated access makes available, R3-N's necessary condition, on the configuration carrier,
   entails FI-1. FI-1 supplies R3-C's antecedent when its operator is unitary; when it is a
   Kraus operator of a complete family, the same forcing holds on the family's dilation, with
   H-RF$_p$ read on the outcome table (§3, *FI-1 and R3*: the dilation lemma, A, computed in r4
   check D1; the instruments, r3 check E2(b)). In either case the 2 is
   the posited quadratic normalisation. The phase, FI-1 and H-Bell are three unsupported
   implications, none derived from another in the sources read (BRIDGE §0 item 8, §5.1
   *Position* [D]). Their independence holds only in scoped forms. The phase is kernel-proved
   independent of the *layer flow* on the two-state carrier (K `obligations_independent`,
   C5Discovery.lean:59). In the driven-transition form of the mixing resource (phase-free
   richness, GR:250–258) the phase is not a separate input because the complex drive carries
   it. On three states $e^{-i\theta X_{ab}}$ is, up to a global phase, the transposition's layer
   flow times a continuous relative phase on the fixed state, and at a quarter turn, composed with
   the exchange, it is $-i\,{\rm diag}(1,1,i)$, the quarter phase on the third state (r3 check
   E4; REVIEW-UNIT1-r4 R4-B1 [D]); the kernel's isolation identity states the general relation,
   a diagonal phase times gate flows equal to the transition flow (K `gateFlow_isolation`,
   LiftAudit.lean:660). GR:250's "No phase operation
   enters" concerns the listed repertoire, not the drive's content. That form therefore folds
   the phase obligation into the mixing obligation, which must then be met by the complex drive
   and not by a real rotation: a real rotation is non-monomial and moves the all-ones ray, but
   with the exchanges it generates only $\mathfrak{so}(3)$ and no phase (r3 E4). Moving the
   all-ones ray is necessary for the phase (GR:260, which states that it "is not shown
   sufficient"), and it is not sufficient: the real rotation moves the ray and yields no phase
   (r3 E4). No independence theorem
   between H-Bell and FI-1 or the phase is stated.
3. **The three items named in the brief do not move (a).**
   - The complex structure $J$ off the null modes is a mathematically available
     *symmetry* of a dimension-$\ge3$ complex carrier (transitive unitary commutant). No
     record read derives it as an operation the observer executes, and it fixes no read
     basis.
   - H-Bell selects a Bell branch, not a correlation law. The exact quantum Bell values need
     weights that finite uniform resources cannot give (finite-accuracy realizations exist,
     Main:566, Main:584), and in that it shares an ingredient with (b).
     That is a shared ingredient, not an identification.
   - Today's stabilizer-scope route draws its probabilities from the counting measure, and no
     amplitude is read there, so it does not bear on (a) (§4.3). Even if it read amplitudes,
     stabilizer-point agreement would not select $f$ in the general class (a-gen): it
     exercises $f$ only at the points $2^{-k/2}$, which do not select $u^2$
     (computation-supported, P2 for $n\le3$; $g$ of §4.3 for all $n$). Within the power family
     the dyadic point $2^{-1/2}$ alone forces $p=2$ under H-RF$_p$ (K5), so this bullet is
     scoped to (a-gen). It holds whether or not SA-1(c) is ever justified.
4. **Measure (b).** On the two probability-outputting non-monomial routes found (§8), the
   continuum ontic carrier and the seed/response carrier, the Born law is fixed by a choice of
   measure or of response function. Neither choice is selected (AP1:1012–1016; A1R; T3 §5;
   WMB §1). There, (a) cannot be separated from (b).
5. **Smallest decisive next paper question** (§5): whether any operation the observer can
   execute acts, on a configuration-carrier block of dimension $\ge3$, by a unitary that is
   non-monomial and not stabilizer-only in the block's read basis. The candidate place to look
   is the $J$-complex sector of the real lift, under the stated access; the question also asks
   whether such an operation's unitarity is derived or posited. A negative answer leaves
   (a-gen) and (d) with no route on `main`. A positive answer supplies the necessary condition of
   R3-N, under H-LIN ∧ H-RF$_p$, for records to discriminate the exponent; it does not supply the
   exponent, and it is the first object on which O1's two candidate targets give different
   verdicts. By owner decision it is folded into #1211/#1217 NQ1 (§7 OQ-2).

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
- **Three distinctions kept apart** (owner direction, #1169 c.6740778880):
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
    state by admissible operations. Unitarity is the quadratic invariant $\sum_j|{\rm amp}_j|^2$
    of that kinematics, posited with it: the operational-completion characterization "takes the
    complex matrix kinematics as given, … and deriving that kinematics is open" (Main:218).
  - **H-RF$_p$** (*posited*; open as a sourcing question): the unrenormalised values
    $|{\rm amp}_j|^p$ are the outcome law, so $\sum_j|{\rm amp}_j|^p=1$ is required on every
    read. Where it is applied below to a Kraus family outside H-LIN, the sum runs over every
    outcome and output entry of the family's outcome table on one input. With $p=2$ it is the Born form, which Main carries as the dictionary of $Q_{\rm fb}$
    and does not select (Main:20, Main:226, Main:288). On the operational route the trace rule
    is an input of the realization: Main:580's QM → OI construction computes
    $q_o={\rm Tr}\,\mathcal I_o(\tilde\rho)$ and thresholds a seed against it (BORN-SRC-1 B10).
    BORN-SRC-1 review finding 9(i): the readout-as-outcome-law premise is the Born form, and "OI
    supplies it rather than sourcing it (B10; Main:580). The hypothesis is open, not weaker than
    what is open". H-RF$_p$ is a power family with no preferred exponent: it fixes no value of
    $p$ by itself (§3, column lemma). Its general-$f$ form **(d′)** is
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
| R3-N | **Necessity (antecedent: every admissible operation is monomial in the read basis).** Under H-LIN ∧ H-RF$_p$, if every admissible operation is a phased permutation in the read basis, every $p>0$ fits every record | A: unimodular entries and $p$-normalised preparations are preserved (below); BORN-SRC-1 C2 (Aaronson, quant-ph/0401062 §2, read via T3 §3.1, not first-hand here). X: P1(a); r2 K2 control | H-LIN (unitary operations; preparations as stated), H-RF$_p$ | yes | **no.** H-LIN and H-RF$_p$ are posited (§1). Within the stated access on the configuration carrier, the antecedent holds for its unitary members, whose observable operators are phased permutations ("a permutation of a diagonal", GR:260, K `bijectiveOperator_monomial`, `phaseOperator_monomial`; Main:556; BRIDGE §5.1 Status [D]). Its other members are monomial but not unitary: registrations (0/1 diagonals) and the Kraus operators $2^{-k/2}P_\sigma$ (QP:853–857). They lie outside H-LIN, and R3-N does not cover them (last column) | not applicable | Under H-LIN ∧ H-RF$_p$, a non-monomial admissible unitary in the read basis is necessary for any record to discriminate $p$. Scope: record discrimination, within those two hypotheses, which are the hypotheses of this necessity and not conditions it shows necessary. Outside H-LIN it fails: a weighted monomial Kraus family $\{2^{-k/2}P_\sigma\}$ discriminates $p$, its outcome table being normalised only at $p=2$ (r2 K2; BRIDGE §5.1 *Position* (d) [D]). That family is R3-C's column lemma applied to its Stinespring dilation, whose columns are non-monomial unit vectors (rv2 D2), so its 2 is the quadratic Kraus completeness $\sum K^\dagger K=1$ of the posited kinematics, as in R3-C. At QP:856–857 its amplitudes $2^{-k/2}$ are the square roots of the counting weights $2^{-k}$ of a uniform unknown, so its $p=2$ returns the inserted counting law: the √-insertion circularity of BORN-SRC-1 review 9(ii), with N2's numbers, measure (b) (§4.3; r3 E3) |
| R3-C | **Conditional forcing (antecedent: one admissible unitary has a visited column with at least two nonzero entries in the read basis).** Under H-LIN ∧ H-RF$_p$, that column forces $p=2$ | A: the column lemma below; BORN-SRC-1 L2. X: P1(b)–(c); r2 K4, K5; r3 E1 | H-LIN, H-RF$_p$ (unrenormalised); the antecedent | yes | **no.** A column with two or more nonzero entries fixes $p$ at the exponent of its own normalisation (column lemma). The 2 is therefore supplied by H-LIN's posited unitarity; H-RF$_p$, a power family with no preferred exponent, supplies only the power form. The forcing is a consistency condition between two posits, not a derivation of the exponent. The antecedent is not supplied for the stated access (below, *FI-1 and R3*) | yes | Inside the posited power family only, at the exponent of the posited kinematics. The unitary scope is sufficient, not necessary: outside H-LIN, any operation with a visited 2-normalised column, or dilation column, with at least two nonzero entries forces $p=2$ in the same way (rv2 D3; r3 E2(b)). For general $f$ the antecedent is not sufficient (R4; BORN-SRC-1 C4; §4.3's $g$) |
| R4 | General $f$: on $n\ge3$, if every point of $\Delta_n$ is the $\lvert\cdot\rvert^2$-profile of a column of some admissible $U$, and (d′) holds, then $f(u)=u^2$ | L/A: Logiurato–Smerzi, arXiv:1202.2728 (BORN-SRC-1 L1; the reviewer's exact rank checks); countercontrol C4 shows that one non-monomial $U$ is not enough | Density ("column-richness") of a *natively sourced* family; (d′); $n\ge3$ | yes | **no.** No native dense family is recorded on `main` (§8): on the configuration carrier one would need FI-1, which the stated access does not supply; on encoded carriers the operations in the records read form finite groups (stabilizer scope, QP:79–98; MECH-2's $A_4\wr S_n$, cited through BRIDGE §5.1 [D]). (d′) is O1, undecided. Applied to representational families such as Main:212's $W$, it is circular (BORN-SRC-1 review 9(ii)) | yes | Fixes the readout only after a dense family and O1; the law still needs (b)–(d) |
| R5 | Gleason/Busch: noncontextual frame functions on the projector (effect) lattice of $\dim\ge3$ give the trace rule | L [54] | (d1)–(d4) of BORN-SRC-1 §4(d) | yes | **no.** The one native context result, `complete_passive_iff_commutative` (CentralObservation), shows that passive observation reads one context. No frame-function predicate is found in the kernel (§8) | yes | Would give (a) only through (d) |
| R6 | Masanes–Galley–Müller: the measurement postulates are operationally redundant, given QM's pure-state, unitary and composite structure | L (via T3 §3.1) | Complex kinematics and tensor composites | yes | **no.** The operational-completion characterization "takes the complex matrix kinematics as given, … and deriving that kinematics is open" (Main:218; Main:564) | yes | Conditional on supplied kinematics |
| R7 | Continuum ontic carrier ($\lambda\in S^2$, sign read). Re-preparation uniform on the outcome hemisphere gives $P(+\mid a)=1-\theta/\pi$; only the cosine-weighted law gives $(1+\cos\theta)/2$ | P/A, AP1:1012–1016. A1R: two uniform vectors with an argmax rule give the cosine density, then fail on the next read (final Z+ probability 2/3, not 1/2) | The carrier, the re-preparation measure, the readout rule | yes | **no.** AP1 Q-B, "reads [that] re-prepare with the cosine-weighted law, without a supplied measure", is open (AP1:1082–1085) | the cosine choice does; the uniform-hemisphere choice does not | On this route the Born law is a choice of measure or carrier: (a) collapses into (b) |
| R8 | Seed/response carrier (B3/E-AR). The quadratic response $1[q<\lvert z_1\rvert^2/\lVert z\rVert^2]$ and the uniform seed are inputs. The carrier is two-mode, $z\in\mathbb C^2$ | P/A: WMB §1 ("The quadratic response and uniform law are explicit inputs, not a derivation of Born selection"); T3:246 | AR-1–AR-6 | yes | **no** | yes, by construction | At $n=2$, normalisation does not select $f$ (BORN-SRC-1 C1: $g(x)=x+x(1-x)(1-2x)$). (a) and (b) are one pushforward (T3:246) |
| R9 | Finite uniform resources with finite deterministic readout and positive conditioning give rational weights | A: T3 §6.1 (on `main`; see §6 F-c) | Finite counting | yes | no: posit (iv), not derived (Main:726) | no at irrational targets ($\cos^2\pi/8$; $2\sqrt2$) | An exact Born law at irrational points needs an atomless or calibrated source: a (b) ingredient, not an exponent selection |
| R10 | μ-form / μ-number: the Born *form* is invariant in μ; the *numbers* change with μ (swap, CE-8) | A (QB3 §§1, 4–5; reviewed ACCEPT in QB3-EVIDENCE-REVIEW) | Finite bijections; non-native examples only | yes | not applicable | not applicable | On the fixed-basis route the numbers are (b)'s, not (a)'s |

**Column lemma (R3-C).** Let $u$ be a column with at least two nonzero entries, all of modulus
in $(0,1)$. Each term of $h(p)=\sum_j|u_j|^p$ is strictly decreasing in $p$, so $h(p)=1$ has at
most one root, and if $\sum_j|u_j|^q=1$ the root is $q$. Under unrenormalised H-RF$_p$ such a
column therefore admits exactly the exponent of its own normalisation (r3 E1, exact; rv2 D1
is the same check):
- a unit ($\ell^2$) column, such as a column of a non-monomial unitary, admits only $p=2$;
- a stochastic ($\ell^1$) column admits only $p=1$, so a non-monomial doubly stochastic matrix
  acting linearly on an amplitude vector is admissible only at $p=1$;
- an $\ell^3$ column admits only $p=3$.

A unit column has every $|u_j|\le1$, so if it is not monomial it satisfies the hypothesis. Hence,
under unrenormalised H-RF$_p$ with $p\neq2$, every visited unit column must be monomial, and,
within H-LIN, the 2 is the exponent of the unitary (quadratic) invariant posited in H-LIN, not of
H-RF$_p$. For a
unitary, "some column has at least two nonzero entries" is the same as "non-monomial" (r2 K3:
an invertible matrix whose columns each have one nonzero entry is monomial). R2 does not use this
lemma.

*Without posited unitarity.* If H-LIN's unitarity is dropped but the operations stay linear and
square (endomorphic: maps of the amplitude space to itself) on real or complex amplitudes and
H-RF$_p$ is required on every amplitude vector (every $\ell^p$-unit vector a possible state),
then for $p\neq2$ every admissible operation is monomial (Aaronson's $p$-norm result, BORN-SRC-1
C2, quant-ph/0401062 §2, not read first-hand here; it concerns a map of a space to itself), so a
square non-monomial admissible operation forces $p=2$; at $p=2$ it preserves
$\sum_j|{\rm amp}_j|^2$ on every vector and so, by polarization, is an isometry, and, being square,
unitary (orthogonal on real amplitudes) (A; r4 check H3). The 2 is then fixed by the linear
amplitude kinematics together
with posited H-RF$_p$; for complex amplitudes that kinematics is the one Main:218 takes as given,
and in either case it is posited, not derived from OI, so column (ii) does not change. For a
non-square operation, such as a Kraus family read on its outcome table (§1) or its dilation,
H-RF$_p$ on every amplitude vector does not force $p=2$. For each $p>0$ the pair
$K_1=2^{-1/p}\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)$,
$K_2=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ has a non-monomial $K_1$ and an
outcome table with $\sum|\cdot|^p=|x_1|^p+|x_2|^p$ on every input, and is complete only at $p=2$;
r3 E3's family $\{w^{1/q}P_\sigma\}$, whose dilation columns have $2^k$ nonzero entries,
satisfies H-RF$_p$ on every vector at $p=q$ (rv4 G3; r5 check S1). For such an operation the 2
comes only from completeness $\sum_rK_r^\dagger K_r=1$, the posited quadratic normalisation
(*FI-1 and R3*, below). If H-RF$_p$ is required only on the states reachable from basis states,
the readout admits exactly the exponents in which every reachable state is normalised (the column
lemma applied to the reachable states), and the map's own normalisation sets that exponent, so
non-monomiality does not force 2 on that route. A non-monomial nonnegative map satisfies H-RF$_1$
on every reachable state (r4 H1; the nonnegative analogue in rv3 F4). The nonnegative,
non-monomial, singular map
$N_q=\bigl(\begin{smallmatrix}0&0&0\\a&1&0\\a&0&1\end{smallmatrix}\bigr)$, $a=2^{-1/q}$, admits
exactly $p=q$; at $q=2$ it forces $p=2$ with no sign and no cancellation, and it is not unitary.
The signed non-monomial map
$S=\bigl(\begin{smallmatrix}0&1&-1\\1/2&0&0\\-1/2&0&0\end{smallmatrix}\bigr)$ admits only $p=1$
(rv4 G4(a)–(b); r5 check S3). An instance with cancellation forces $p=2$ (r4 H2; rv3 F4; r5
check S3).

*If the antecedent were supplied.* An executed non-monomial unitary would bear on the exponent
beyond this consistency check only if its quadratic invariant were itself derived from OI
rather than posited with the complex matrix kinematics (Main:218). This is a condition on what
NQ-1059's positive branch would show (§5), not an added premise.

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
Two notions of "admissible" meet here. R3's is membership of H-LIN's class, read with a
$p$-normalised readout; FI-1's is "made available by the stated access" (BRIDGE §5.1: "'Supplies'
in FI-1 means 'makes available as an admissible operator'"). The first bullet reads R3's class
as the operations the stated access makes available.
- *R3-N's necessary condition, read on the configuration carrier, entails FI-1.* A non-monomial
  admissible unitary is a non-monomial admissible operator.
- *FI-1 entails R3-C's antecedent only for a unitary operator.* Inside H-LIN the operator would
  have to be unitary for R3-C to apply. Outside H-LIN the forcing does not need unitarity: for a
  Kraus operator of a complete family ($\sum_rK_r^\dagger K_r=1$), "non-monomial" implies that
  some column of the family's Stinespring dilation has at least two nonzero entries (dilation
  lemma, A). Proof: completeness makes the stacked dilation $V$ an isometry, so its columns are
  orthonormal. If each had exactly one nonzero entry, two of them at the same (operator, row)
  position would have nonzero inner product, so the positions are distinct; each $K_r$ then has
  at most one nonzero entry per row and per column, and a partial injection extends to a
  permutation, which is the kernel's `IsMonomial` shape $P_\sigma\,{\rm diag}(d)$ with zeros
  allowed (SubstratumInterface.lean:75). r4 check D1 computes the Gram matrix and decides that
  shape for every single-entry dilation with $n,m\le3$ over four exact entry values: Gram $=1$
  gives monomial blocks throughout, and the countercontrol finds single-entry dilations with
  Gram $\ne1$ and a non-monomial block (computation-supported for $n,m\le3$; the general case is
  the proof). Under H-RF$_p$ read on the outcome table, that dilation column forces $p=2$, again
  through the posited quadratic normalisation (the instruments
  $\{|0\rangle\langle+|,|1\rangle\langle-|\}$ and $\{|0\rangle\langle+|,|0\rangle\langle-|\}$,
  r3 E2(b); rv2 D3).
  $K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, which is non-monomial with monomial columns (r2 K1;
  BRIDGE K2 [D]), is not a contraction ($K^\dagger K$ has eigenvalue 2), so it lies in no complete
  family. It shows only that "non-monomial" and "some column has two nonzero entries" are
  different predicates, and nothing about admissible operations.
- *On encoded carriers* non-monomial encoded maps arise without FI-1 (BRIDGE §5.1 [D], citing
  QP:79–98, QP:846–877, at single-qubit stabilizer scope). There the probabilities are N2's
  (§4.3), not readings of an amplitude, so R3 does not apply to them.
- FI-1 is neither the earliest nor the only gap on the route to operational QM. It is the first
  unsupported step on that route only once the phase is taken as stated (Main:590, GR:268;
  BRIDGE §5.1 *Position* (b) [D]); its relation to the phase and to H-Bell is scoped in §0
  item 2.

**Answer to Q1.** Every result that constrains $p$ or $f$ does so conditionally:
- through posited H-RF$_p$ and a non-monomial admissible unitary, the value 2 being H-LIN's
  posited quadratic invariant (R3-C), or a dense native family with (d′) (R4);
- through a supplied context structure (R5);
- through supplied kinematics (R6);
- or through a supplied measure or response (R7–R9).

None of these antecedents is in column (ii). What holds without a posited readout form concerns
law classes: the class of realizable finite-horizon laws does not depend on $p$ (R2, conditional
on the normalisation restriction), so a selection of $p$, if any, has to come from a constraint
on admissible operations. Such a constraint (R3-C) exists only inside posited H-RF$_p$, and
the value it returns is the normalisation exponent of the posited kinematics.

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
   observer executes and reads. FI-1, which asks only for one non-monomial admissible operator
   on the configuration carrier, is not supplied by the stated access and is open for the
   candidate sources BRIDGE lists (§5.1 Status [D]). Main distinguishes a derived continuous path from
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

*Effect on #1059.* None on status. The finding names the first record found (§8) of a $\dim\ge3$
complex carrier with a transitive unitary symmetry. Every other probability-outputting non-monomial route
found (§8) is two-mode (R8) or stabilizer-only (§4.3). `main` also carries non-monomial objects
that output no probability: the layer flows' intermediate-time points (K `gateFlow_not_monomial`,
CoherentContinuumSource.lean:74), the polarization candidate's Hadamard image
(K `hadamard_not_monomial`, C5Discovery.lean:162) and the postulated coupling of
`OIBridge/StateMixingCoupling.lean` ("the datum is a postulate, and nothing here derives it").
None is an available operation of the stated access. The layer flows at intermediate times are
not executable by it (GR:270; K `configurationLevel_not_layerFlowExecutable`,
`obs_not_layerFlowExecutable`). The stated interventions lie in the monomial class, which is
closed under the architecture operations (GR:260; K `substratumClass_structurallyClosed`,
StructuralClosure.lean:316, the class being `IsMonomial`, :180), so the non-monomial Hadamard is
not in it, and C5Discovery.lean's header lists "that the polarization map is available to the
observer" as not claimed. The coupling is a postulate adjoined to the stated access
(StateMixingCoupling.lean header). That makes $J$ the place where the next
question (§5) is posed.
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
- **Relation to FI-1.** H-Bell stands beside FI-1, not after it; neither is derived from the
  other in the sources read, and no independence theorem between them is stated (BRIDGE §5.1
  *Position* (c) [D]). The support runs one way only: quantum Bell statistics are realized to
  finite accuracy by fixed bijections, monomial on their configuration carrier, once ontic
  parameter dependence is given (Main:403–406, Main:566, Main:584), so that target needs no
  FI-1; those realizations have no spatial graph (Main:362), while H-Bell's clause (iii) is a
  curvature condition on the prepared graphs (Substratum:133).
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
- **(a-pow)**, the exponent in the power family. Under H-LIN ∧ H-RF$_p$, a non-monomial
  admissible unitary in the read basis is necessary for any record to discriminate $p$ (R3-N);
  on the configuration carrier it entails FI-1. H-LIN and H-RF$_p$ are the hypotheses of that
  necessity, not conditions it shows necessary, and the necessity concerns record
  discrimination only. The condition is not sufficient to *derive* the exponent: a mixing
  unitary fixes $p$ at the exponent of its own normalisation, so the 2 comes from H-LIN's
  posited unitarity, and supplying FI-1, or any mixing unitary, would establish only that the
  posited power readout and the posited kinematics agree at $p=2$ alone (column lemma, §3).
- **(a-gen)**, the readout function in general, needs a dense native family on $n\ge3$ with
  (d′) (R4), or the (d1)–(d4) context structure (R5). O1 decides which target applies.
  Today's findings supply none of these antecedents.
- **The law**, beyond the readout, needs (b)–(d) and composites; coherent mixing supplies none
  of them (§0 item 2).
- **One §A.34 point about BRIDGE.** Its r2 §6 "Born statistics" row read "An independently
  justified selection of the quadratic functional on non-monomial (state-mixing) operations;
  equivalently a source of non-monomial admissible operators". Only the necessity direction
  holds, under R3-N's hypotheses; sufficiency fails for general $f$ (C4; P2; $g$), and within
  the power family a source of such operators fixes $p$ only at the posited kinematics'
  exponent (column lemma). BRIDGE r3 and r4 (§6, row "Born statistics") read "which presupposes
  a source of non-monomial admissible operators", which is the necessity direction (§6 F-b).

**ELABORATING.** The necessity direction is stated in BORN-SRC-1 §4(a) and BRIDGE §5.1 *Position* (d).
This unit adds the conditional converse with its scope, the location of its value 2 in H-LIN's
posited unitarity, the relation of FI-1 to R3-C's antecedent through unitarity or the
dilation, and the class version R2.

### 4.5 What is open on #1059 after today

| Part | Status at `fd539e15` | Prerequisites, after today | Change |
|---|---|---|---|
| (a-pow) exponent in the power family | open | Under H-LIN ∧ H-RF$_p$ (both posited), a non-monomial admissible unitary in the read basis is necessary for any record to discriminate $p$ (R3-N; on the configuration carrier it entails FI-1, #1211). Not sufficient to derive the exponent: the 2 it would force is H-LIN's posited unitarity (R3-C) | A conditional necessary condition for record discrimination located; not reduced to FI-1 |
| (a-gen) full quadratic dictionary | open | A native dense family on $n\ge3$ (on the configuration carrier, which needs FI-1) + O1's target ((d′), or (d1)–(d4)) | None. $J$ names a candidate carrier only (§4.1) |
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
real lift (§4.1). The question also asks which read basis, if any, the records use there, and,
if such an operation exists, whether its unitarity in that basis is derived from OI or taken with
the complex matrix kinematics (Main:218). The second case includes unitarity forced by the
operation's linearity, as a square (endomorphic) map on complex amplitudes, together with H-RF$_p$
required on every amplitude vector (§3, *Without posited unitarity*; BORN-SRC-1 C2, Aaronson), since that kinematics is the
one taken as given. Only a derived quadratic invariant would bear on the exponent beyond R3-C's
consistency check (§3).*

- **Why it is decisive.** Either answer changes what #1059 can do.
  - *No* (on the classes examined): (a-gen) and (d) have no route on `main` whatever O1
    decides, and under H-LIN ∧ H-RF$_p$ no record of the stated access discriminates $p$ (R3-N).
    This is not a no-go for a selection of $p$ that is not record-based, or for operations
    outside H-LIN. #1059's own content is then (b) and (c), with (a) and (d) carried as open and conditional on access that the
    corpus does not supply.
  - *Yes*: it supplies, under H-LIN ∧ H-RF$_p$, the necessary condition of R3-N, not the
    exponent and not the law. It would bear on the exponent beyond R3-C's consistency check only
    if the exhibited operation's quadratic invariant were itself derived from OI rather than
    posited with the complex matrix kinematics (§3, column lemma); this states what the branch
    would show and adds no premise. It is the first object on which O1's two targets differ in
    content: (d′) with density would give $u^2$ by R4; Gleason/Busch would further need the projector lattice of (d1). O1 then becomes
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
  - It overlaps #1211's NQ1 (the $J$ question) and FI-1, and by owner decision it is folded into
    #1211/#1217 NQ1 (#1169 c.6742190154; §7 OQ-2). It adds the
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
  holds, under R3-N's hypotheses (the sufficiency counterexamples are C4, P2 and $g$; within the
  power family the forced value is the posited kinematics' exponent, §3). §A.34. BRIDGE r3
  (`ee1c83c0…8219`) and r4 (`4e97610d…85e2`, §6 row "Born statistics") read "which presupposes a
  source of non-monomial admissible operators", which states the necessity direction only. No
  further suggestion.
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
- **F-e (book glossary and its FULL mirror; BORN-SRC-1 F3 as sharpened by its review finding 4,
  still present).** `book/glossary.md:21` and its mirror
  `book/The-Incompleteness-of-Observation-FULL.md:6604` (§A.14) read identically. Their first
  sentence, "The framework therefore does not list a separate 'quadratic-exponent selector' as an
  unresolved foundational theorem at that layer", agrees with Main:556 when "that layer" is the
  finite fixed-basis layer: there the dictionary "is not an open choice at all". The
  inconsistency is the next sentence, "What remains is operational", which omits the
  exponent-origin frontier item that Main:20, Main:226, Main:556 and ch18:34 keep; Main:556 adds
  that the operational question "is an operational question, not the exponent question of §3.1,
  and the two should not be conflated". The line was edited between `02009693` and `fd539e15`:
  the first sentence and the clause "What remains is operational" are unchanged; the second
  sentence's tail was rewritten, still without the exponent item (`git diff --word-diff 02009693
  fd539e15 -- book/glossary.md`). This
  confirms BORN-SRC-1 F3 and review finding 4 ("unless 'that layer' is read narrowly"); it is a
  cross-document status inconsistency for O2's remit (§A.25), and it selects no exponent.
  **CONFIRMING.**

***

## 7. Owner questions

- **OQ-1.** Should #1059 record that, under H-LIN ∧ H-RF$_p$ (both posited), a non-monomial
  admissible unitary in the read basis (on the configuration carrier, entailing FI-1, #1211 §5.1)
  is necessary for any record to discriminate the exponent, with the explicit statements that
  this necessity holds only within those hypotheses and for record discrimination, that it is
  not sufficient for the exponent or the law, and that the value 2 such a unitary would force is
  that of H-LIN's posited unitarity; and (a-gen) as needing a dense native family and O1?
- **OQ-2 (resolved).** Asked: is NQ-1059 (§5) the next #1059 unit, given that it overlaps
  #1211's NQ1, or should it be folded into #1211 as an added condition (dimension $\ge3$,
  unitary, non-stabilizer, read basis)? Owner decision 5, #1169 c.6742190154 (amaybaum,
  2026-11-09T14:13:27Z), verbatim: "#1059's next question is folded into #1211/#1217 NQ1."
  NQ-1059 is therefore folded into #1211/#1217 NQ1. The same comment states that none of its
  decisions authorizes a scientific computation, an F or E designation, a dispatch, a freeze or a
  merge. This also bears on the owner's question in #1169 c.6741291498 (amaybaum,
  2026-11-09T13:30:54Z), "Decide whether #1059 and #868 need independent follow-up experiments
  rather than treating success on FI-1 as solving both": on #1059's side, FI-1 is necessary
  under named hypotheses and not sufficient for the exponent or the law (§0 item 2, §4.4,
  OQ-1).
- **OQ-3 (resolved).** The owner direction (#1169 c.6740778880) calls the phase, FI-1 and H-Bell
  "independent unresolved obligations". The sources read support that only in scoped forms
  (§0 item 2): none is derived from another; the phase is kernel-independent of the layer flow;
  in the driven-transition form the phase is carried by the complex drive, so that form folds
  the phase obligation into the mixing obligation; no independence theorem involving H-Bell is
  stated. Asked: should the planned dependency matrix record these scoped relations rather than
  an unqualified independence? The matrix is the one of #1169 c.6741291498, each dependency
  carrying "a status: proved, conditional, disproved or open; its carrier: configuration or
  encoded; its assumptions". Owner decision 4, #1169 c.6742190154, verbatim: "The matrix records
  scoped relations: phase is independent of the layer flow only; the complex drive carries the
  phase; no H-Bell implication."
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
  - REVIEW-UNIT1-r4 (`e489fc19…2bc7`) R4-B1, R4-B2 and its §2 phase passage (r3);
  - BRIDGE r2 §§0–3, §5.1, §6 (ingredient rows), F4 and §11; BRIDGE r3 §0 item 8, §5.1 and the
    §6 "Born statistics" row (r2 of this unit); BRIDGE r4 header, §0 and §5.1, and its §6 "Born
    statistics" row (r3 of this unit);
  - REVIEW (bridge r1) in full; REVIEW-r2 RB1–RB3 (r2 of this unit); REVIEW-UNIT1-r3's verdict
    line (r3);
  - SHM §0, §8 rules, §8.3, §8.4 and §9; SHM r5's first line and the r4/r5 N2 row (r2);
  - this unit's reviews, REVIEW-1059 (r2), REVIEW-1059-r2 (r3) and REVIEW-1059-r3 (r4), in full,
    with the reviewer's `review/rv3_1059_checks.py` (r4);
  - #1169 c.6740778880, the owner direction (r3);
  - REVIEW-1059-r4 in full, with `review/rv4_1059_checks.py` (`cf6f2b38…a967`); #1169
    c.6741291498 and c.6742190154, read with `gh api` (read only); REVIEW-UNIT1-r5
    (`0ef5644f…8c76`) header and verdict (r5).
- **Read at the cited lines:**
  - Main:20, 56, 208–226, 288, 345–351, 552–556, 576–580, 590, 646–656, 684, 726;
  - T3:1–160 and 240–270; T3 at `8e764171` vs `fd539e15` (diff, r2);
  - AP1:240–250, 830–845, 975–1095;
  - WMB:1–40 and 205–222;
  - A1R:1–90;
  - Structure:1117; Substratum:16–68, 131–145, 481;
  - EQ:99, 147, 190–340, 462;
  - `book/ch18-beyond.md`:16, 30–36 and `book/glossary.md`:21 (r2);
    `book/The-Incompleteness-of-Observation-FULL.md`:6604 and
    `git diff 02009693 fd539e15 -- book/glossary.md` (r3);
  - Main:218, 362, 403–406, 566, 580, 584 (r3, for the quotations used);
  - GR:250–270 (r3);
  - QP:846–877 (r3);
  - kernel identifiers at `fd539e15` (r3): `IsMonomial` (SubstratumInterface.lean:75),
    `gateFlow_not_monomial` (CoherentContinuumSource.lean:74), `obligations_independent` and
    `hadamard_not_monomial` (C5Discovery.lean:59, :162), `gateFlow_isolation`
    (LiftAudit.lean:660), the header of StateMixingCoupling.lean;
  - the H-Bell round-1 preregistration head;
  - r4: GR:260 and GR:270 in full; StructuralClosure.lean:180 and :316; C5Discovery.lean:1–40;
    `git diff --word-diff 02009693 fd539e15 -- book/glossary.md`; QP's path; BORN-SRC-1 C2
    (`src/914-bornsrc.txt`:209–210, :317–318);
  - r5: BORN-SRC-1 C1 and C4 (`src/914-bornsrc.txt`:213–216, :325–328); Main:218 again.
- **Searched at `fd539e15`** (`git grep -i` over `verification/`, `papers/` and `book/`): "born",
  "quadratic exponent / functional / sensor / rule", "|U|^p", "hemisphere", "cosine-weighted".
  The negatives stated in §§3–5 ("no native dense family recorded", "no frame-function
  predicate", "no record stating a read basis for $J$-amplitudes", "every other
  probability-outputting non-monomial route found") are scoped to that search, to BORN-SRC-1's
  search at `02009693`, and to the files read. The §A.19 sweep also covers the read-write-cycle
  equilibrium mechanism proposal (Main:684, "the cosmological realization's mechanism proposal";
  ch18 §18.2, ch18:34, "structural commitment") and `book/glossary.md:21` (F-e): neither selects
  the exponent. Lean files were read only at the lines listed. No kernel build was run.
- **Probes** (generic objects only; exact sympy, Gaussian-integer, Gaussian-rational and interval arithmetic; run
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
  - `probes/r3_exponent_source.py` (r3), sha256 `34db77f2…e758`, output
    `probes/r3_exponent_source.out` (`3b54c129…c8a0`). Imports no earlier script. Checks: E1 the
    forced exponent is the column's own normalisation exponent ($\ell^2$ → 2, $\ell^1$ → 1,
    $\ell^3$ → 3; doubly stochastic non-monomial matrix → 1; each fails at the other exponents);
    E2(a) encodes the dilation lemma's case split and is not a verification of it: it compares
    two encodings of one predicate and computes no Gram matrix, so it cannot fail; it is replaced
    as support by r4 D1. E2(b) the instruments
    $\{|0\rangle\langle+|,|1\rangle\langle-|\}$ and $\{|0\rangle\langle+|,|0\rangle\langle-|\}$
    admissible only at $p=2$; E2(c) the control that the unscaled $K$ is not a contraction; E3 the
    family $\{w^{1/q}P_\sigma\}$ with counting weight $w=2^{-k}$ is admissible only at $p=q$,
    and complete only at $q=2$; E4 the complex drive carries a phase
    ($e^{-i\theta X}=e^{-i\theta}G(2\theta/\pi)\,{\rm diag}(1,1,e^{i\theta})$, symbolic $\theta$;
    the quarter-turn identity $e^{-i\pi X/2}\,{\rm swap}=-i\,{\rm diag}(1,1,i)$), with the
    control that a real rotation moves the all-ones ray and, with permutation conjugates,
    generates a Lie algebra of real dimension 3 against 8 for $iX$. Mutation-tested: six
    single-line mutants (wrong exponent, wrong completeness exponent, inverted orthogonality, an
    incomplete instrument, the phase factor dropped, the real Lie dimension set to 8) each fail;
    the inverted-orthogonality mutant negates one copy of E2(a)'s predicate and so tests nothing
    about the lemma.
  - `probes/r4_dilation_gram.py` (r4), sha256 `22e0fdb3…8998`, output
    `probes/r4_dilation_gram.out` (`d66f0b58…a34b`). Imports no earlier script. Exact Gaussian
    rationals and sympy. Checks: D0 self-tests of the monomial and Gram deciders; D1 for every
    single-entry dilation with $n,m\le3$ and entry values in $\{1,i,(3+4i)/5,1/2\}$ (63128
    cases), the Gram matrix is computed and each block's `IsMonomial` shape decided by search over
    $\sigma$: Gram $=1$ (17424 cases) gives monomial blocks; countercontrols: Gram $\ne1$ with a
    non-monomial block (22080 cases), and distinct positions with Gram $\ne1$ (23624 cases); D2
    three exact complete families with a non-monomial block each have a dilation column with
    two or more nonzero entries; H1 the nonnegative non-monomial $\bigl(\begin{smallmatrix}1/3&2/3\\
    2/3&1/3\end{smallmatrix}\bigr)$ keeps every state reachable from $e_1$ (and, by its swap
    symmetry, from $e_2$) nonnegative with entry sum 1 (symbolic power), and fails $p=2$; H2 $M_p=2^{-1/p}\bigl(\begin{smallmatrix}1&-1\\1&1
    \end{smallmatrix}\bigr)$ has $\ell^p$ columns for every $p$, and $M_p^2e_1$ has
    $\sum|\cdot|^p=2^{p-2}$, 1 only at $p=2$; H3 for a generic complex $2\times2$ matrix the
    four norm defects at $e_1,e_2,e_1+e_2,e_1+ie_2$ determine $A^\dagger A-1$ (polarization).
    Mutation-tested: eight single-line mutants (the Gram test removed; monomiality decided by
    columns only; the H2 root set to 3; the H3 polarization sign flipped; a sign put into H1's
    matrix; an incomplete D2 family; the non-unit value removed from D1's values; H1's $p=2$
    failure negated) each fail.
  - `probes/r5_scope_checks.py` (r5), sha256 `ecda6683…582e`, output
    `probes/r5_scope_checks.out` (`9459e693…79c8`). Imports no earlier script. Exact sympy.
    Checks: S1 non-square operations under H-RF$_p$ on every amplitude vector: for symbolic $p$,
    moduli and phases, the pair $K_1=2^{-1/p}\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)$,
    $K_2=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ has outcome-table sum
    $|x_1|^p+|x_2|^p$, a non-monomial $K_1$, and completeness only at $p=2$; the family
    $\{2^{-k/q}P_\sigma\}$ ($k=1,2$; $q=2,3,4$) has table sum $2^{k(1-p/q)}\sum|x_i|^p$, dilation
    columns with $2^k$ nonzero entries, and completeness only at $q=2$; S2 square controls
    (instances, not a proof of the endomorphic form): the Hadamard and the 3-4-5 rotation ⊕ 1 fail
    on a basis vector at each sampled $p\ne2$, a phased permutation preserves $\sum|x_i|^p$ for
    symbolic $p$, and $K_1$ alone fails on $e_2$; S3 the reachable-state readout, its admissible
    exponents computed two ways (intersection of each reachable state's own normalisation
    exponent; direct test at sampled exponents): $N_q$ ($q=2,3$; nonnegative, non-monomial,
    singular) gives $\{q\}$, $S$ (signed) gives $\{1\}$, the rotation
    $2^{-1/2}\bigl(\begin{smallmatrix}1&-1\\1&1\end{smallmatrix}\bigr)$ (cancellation) gives
    $\{2\}$, and a signed permutation (control) gives every $p$. Mutation-tested: ten single-line
    mutants (S1 ×4: $K_2$ rescaled, $K_1$'s scale fixed at $2^{-1/2}$, the $2^{k(1-p/q)}$ factor
    dropped, the dilation entry count; S2 ×2: $K_1$ tested on $e_1$, the Hadamard's sign removed;
    S3 ×4: $N_q$'s corner entry zeroed, $S$'s sign removed, the control's expected set changed,
    the direct test restricted to one state) each fail.
  - The reviewers' `review/rv_1059_checks.py` (`3960d7c8…2264`) and `review/rv2_1059_checks.py`
    (`a13582b2…d304`) were re-run here with `python3 -I`: exit 0, outputs byte-identical to the
    recorded `.out` files. Of the first, only C6 is relied on (§4.5, row (d)); of the second,
    D1–D3 are cited as rv2 D1–D3. P1, P2 and `r2_fi1_scope.py` were also re-run in
    r3, with byte-identical outputs. In r4, P1, P2, `r2_fi1_scope.py`, `r3_exponent_source.py`
    and `review/rv3_1059_checks.py` (`b0d99862…0151`) were re-run, all byte-identical; F4 of the
    last is cited as rv3 F4. In r5, P1, P2, `r2_fi1_scope.py`, `r3_exponent_source.py`,
    `r4_dilation_gram.py` and the reviewers' `rv_`, `rv2_`, `rv3_` and `rv4_1059_checks.py` were
    re-run from a scratch directory, all exit 0 and byte-identical to their recorded `.out`
    files; G3 and G4 of the last are cited as rv4 G3 and G4.

  R2's and §4.3's statements rest on the paper argument plus these checks, and are marked
  computation-supported where the check is the only support.
- **Not done:** no computation on any OI mechanism, the real lift or $J$ included. No literature
  source was re-read first-hand: Logiurato–Smerzi, Aaronson and Masanes–Galley–Müller are cited
  as BORN-SRC-1 and T3 report them. QP was read only at QP:846–877 (r3); its other lines are
  cited through BRIDGE [D]. No #1082 file was opened beyond what QB3 lands. No #1210 or #1211 file was edited.
