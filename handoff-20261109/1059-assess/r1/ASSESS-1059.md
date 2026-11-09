# BORN-SEL (#1059): re-assessment of the open question against the #1210 / #1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Pending a fresh,
independent review.** Nothing here is adopted, promoted or proposed for the manuscripts. A
review ACCEPT, if reached, authorizes nothing further.

- **Accountable home:** #1059. Feeds #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, recorded in #1059 c.6740117293 (posted
  2026-11-09T12:31:13Z), full record #1169 c.6740116927 (posted 2026-11-09T12:31:12Z). Option
  text, verbatim: "**#1059/#1049/#868 audits** — One paper-only unit each, re-assessing its open
  question against today's #1210/#1211 findings (Born exponent; linear vs affine dynamics;
  joint-test validity), each with a fresh review. Exact generic checks only." Not authorized
  (c.6740117293): "computation on an OI mechanism, new physical assumptions, freeze, dispatch,
  manuscript changes or merges". This unit makes no repo, git or GitHub write.
- **Checks run.** Two exact checks on generic mathematical objects (permutation and Cayley
  unitaries; stabilizer states), in `probes/` (§8). No computation was run on an OI mechanism.
  A statement supported only by such a check is marked *computation-supported*.
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
  - "BRIDGE" = `scratchpad/bridge/BRIDGE-UNIT1.md` r2, sha256 `3905569b…103a` (#1211 unit 1;
    pending a fresh review). Its r1 review "REVIEW" = `scratchpad/bridge/review/REVIEW-UNIT1.md`,
    sha256 `e242a794…a1ef7` (REVISE).
  - "SHM" = `scratchpad/qphen/SHARED-MECHANISM.md` r4 §§8–9, sha256 `a7206701…cc4d` (#1210
    Phase 1).

***

## 0. Summary

1. **#1059's question is unchanged in status.** No record on `main`, and no draft of
   2026-11-09, derives the quadratic exponent, or the Born probability law, from independently
   justified OI principles. (a)–(d) of BORN-SRC-1 stay open. The Born dictionary of $Q_{\rm fb}$
   is a definition (`QfbReal.born := ‖Q.U b' b‖ ^ 2`, EQ:205; Main:20, Main:556).
2. **What today's findings change is where (a) sits, not whether it is open.** Under two stated
   readout-form hypotheses, the power-family part of (a) is equivalent to the first unsupported
   forward implication FI-1 of BRIDGE §5.1: that some admissible operation on the observer's
   carrier is non-monomial. Each direction is a known, elementary result (§3, R3). So (a) has no
   content of its own until FI-1 is supplied. For a general readout function, FI-1 is not enough:
   a dense family on dimension $\ge3$ is also needed (Logiurato–Smerzi), and so is O1's choice of
   target.
3. **The three items named in the brief do not move (a).**
   - The complex structure $J$ off the null modes supplies a dimension-$\ge3$ complex carrier
     with a transitive unitary *symmetry*. It is not an executable operation, and it fixes no
     read basis.
   - H-Bell selects a Bell branch, not a correlation law. The quantum Bell values need weights
     that finite uniform resources cannot give, and in that it shares an ingredient with (b).
     That is a shared ingredient, not an identification.
   - Today's stabilizer-scope route draws its probabilities from the counting measure. It
     exercises the readout only at the points $2^{-k/2}$, which do not select $u^2$
     (computation-supported, P2). This holds whether or not SA-1(c) is ever justified.
4. **Measure (b).** On the two non-monomial routes on `main` that output a probability, the
   continuum ontic carrier and the seed/response carrier, the Born law is fixed by a choice of
   measure or of response function. Neither choice is selected (AP1:1012–1016; A1R; T3 §5;
   WMB §1). There, (a) cannot be separated from (b).
5. **Smallest decisive next paper question** (§5): whether any operation the observer can
   execute acts non-monomially, and not stabilizer-only, on a carrier of dimension $\ge3$. The
   candidate place to look is the $J$-complex sector of the real lift, under the stated access.
   A negative answer leaves (a) and (d) with no route on `main`. A positive answer is the first
   object on which O1's two candidate targets give different verdicts.

***

## 1. Conventions

- **Layers.** K kernel; A exact algebra or written proof; X exact or exhaustive computation on a
  generic object (this unit's probes); L literature, with an indication of whether it was read
  first-hand here; P prose only; D an unreviewed draft (hypothesis only).
- **Three columns** for each result or restriction:
  - (i) mathematically well-defined;
  - (ii) follows from independently justified OI principles;
  - (iii) reproduces the QM prediction.

  Column (iii) is never cited as support for column (ii).
- **§A.34.** Every equivalence is given as two separately supported directions.
- **§A.31 labels** for this unit's own findings: NEW, POSITIVE, ELABORATING, CONFIRMING,
  BORDERLINE.
- **Hypotheses used below.** Both are named because they are the Born *form*, which OI supplies
  rather than sources (BORN-SRC-1 review finding 9(i); Main:580).
  - **H-LIN:** the admissible operations act linearly on an amplitude vector, read in one fixed
    basis.
  - **H-RF$_p$:** a record's probability is $|{\rm amp}|^p$, normalised. Its general-$f$ form
    **(d′)** is modulus-only, context-free and normalised (BORN-SRC-1 O1).

***

## 2. Baseline: what was open on #1059 before today

All of this is on `main`, or is BORN-SRC-1, which is reviewed and ACCEPTed in #914:

- **(a) Exponent 2.** Open, kept on the list pending O1 (BORN-SRC-1 §4(a)).
  - (QM ⇒ normalisation): K, `QfbReal.sum_born` (EQ:227).
  - (OI ⇒ exponent 2): open. Native step unitaries are permutations, so every $f$ with
    $f(0)=0$ and $f(1)=1$ fits (Main:556, check 6 of `equivalence_recovery_probes.py`).
- **(b) The hidden-sector measure.** Open.
  - The numbers carried by the Born form are the measure's (QB3 §1, μ-number).
  - The counting measure is selected by posit (iv), "a standard but substantive epistemic
    postulate, not derived" (Main:726; Main:56, Lemma 3).
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
| R1 | $S\iff D\iff Q_{\rm fb}$, finite horizon | K, `finite_horizon_equivalence` (EQ:462); Main:552–554 | The Born dictionary is in the definition of $Q_{\rm fb}$ (EQ:205) | yes | not applicable: the dictionary is a definition (St) | yes, by definition | Exhibits the form and selects nothing (Main:20, Main:556) |
| R2 | The class version: for every $p>0$, $Q_{\rm fb}^{p}=S$. Here $Q_{\rm fb}^{p}$ is $Q_{\rm fb}$ with readout $\lVert U\rVert^p$, restricted to realizations whose readout is normalised on every visited column | A (below) + X (P1(a)–(b), computation-supported at the stated grid) | H-LIN on the fixed basis; measurement at every step from a diagonal initial law (Main:552) | yes | not applicable | not applicable | **No fixed-basis argument can select $p$.** This strengthens Main:556's "the construction does not select" to the class, at the finite-law layer. ELABORATING |
| R3 | **(a-pow) ⟺ FI-1, given H-LIN ∧ H-RF$_p$.** (⇒) one admissible non-monomial column with normalised $p$-readout forces $p=2$. (⇐) if every admissible operation is monomial, every $p$ fits every record, coherent preparations included | (⇒) A: the column lemma below; BORN-SRC-1 L2; X P1(b)–(c). (⇐) A: BORN-SRC-1 C2 (Aaronson, quant-ph/0401062 §2, read via T3 §3.1, not first-hand here) | H-LIN, H-RF$_p$; FI-1 as the antecedent | yes | **no.** The antecedent FI-1 is "not supplied" for the stated substratum dynamics with read/write access and for the stated lift formulations that land in the operational interface. It is open for the site-space wave-operator formulation (Main:590; BRIDGE §5.1 [D]). H-LIN and H-RF$_p$ are supplied (BORN-SRC-1 review 9(i)) | yes | Moves the power-family part of (a) onto FI-1 (§4.4) |
| R4 | General $f$: on $n\ge3$, if every point of $\Delta_n$ is the $\lvert\cdot\rvert^2$-profile of a column of some admissible $U$, and (d′) holds, then $f(u)=u^2$ | L/A: Logiurato–Smerzi, arXiv:1202.2728 (BORN-SRC-1 L1; the reviewer's exact rank checks); countercontrol C4 shows that one non-monomial $U$ is not enough | Density ("column-richness") of a *natively sourced* family; (d′); $n\ge3$ | yes | **no.** No native dense family exists, since even FI-1 is not supplied. (d′) is O1, undecided. Applied to representational families such as Main:212's $W$, it is circular (BORN-SRC-1 review 9(ii)) | yes | Fixes the full dictionary only after FI-1, density and O1 |
| R5 | Gleason/Busch: noncontextual frame functions on the projector (effect) lattice of $\dim\ge3$ give the trace rule | L [54] | (d1)–(d4) of BORN-SRC-1 §4(d) | yes | **no.** The one native context result, `complete_passive_iff_commutative` (CentralObservation), shows that passive observation reads one context. No frame-function predicate exists in the kernel | yes | Would give (a) only through (d) |
| R6 | Masanes–Galley–Müller: the measurement postulates are operationally redundant, given QM's pure-state, unitary and composite structure | L (via T3 §3.1) | Complex kinematics and tensor composites | yes | **no.** "Complex matrix kinematics" is "taken as given … deriving that kinematics is open" (Main:218, Main:564) | yes | Conditional on supplied kinematics |
| R7 | Continuum ontic carrier ($\lambda\in S^2$, sign read). Re-preparation uniform on the outcome hemisphere gives $P(+\mid a)=1-\theta/\pi$; only the cosine-weighted law gives $(1+\cos\theta)/2$ | P/A, AP1:1012–1016. A1R: two uniform vectors with an argmax rule give the cosine density, then fail on the next read (final Z+ probability 2/3, not 1/2) | The carrier, the re-preparation measure, the readout rule | yes | **no.** AP1 Q-B, "reads [that] re-prepare with the cosine-weighted law, without a supplied measure", is open (AP1:1082–1085) | the cosine choice does; the uniform-hemisphere choice does not | On this route the Born law is a choice of measure or carrier: (a) collapses into (b) |
| R8 | Seed/response carrier (B3/E-AR). The quadratic response $1[q<\lvert z_1\rvert^2/\lVert z\rVert^2]$ and the uniform seed are inputs. The carrier is two-mode, $z\in\mathbb C^2$ | P/A: WMB §1 ("The quadratic response and uniform law are explicit inputs, not a derivation of Born selection"); T3:246 | AR-1–AR-6 | yes | **no** | yes, by construction | At $n=2$, normalisation does not select $f$ (BORN-SRC-1 C1: $g(x)=x+x(1-x)(1-2x)$). (a) and (b) are one pushforward (T3:246) |
| R9 | Finite uniform resources with finite deterministic readout and positive conditioning give rational weights | A: T3 §6.1 (on `main`; see the header note, §6 F-c) | Finite counting | yes | yes for the counting default, as a posit (Main:726 (iv)) | no at irrational targets ($\cos^2\pi/8$; $2\sqrt2$) | An exact Born law at irrational points needs an atomless or calibrated source: a (b) ingredient, not an exponent selection |
| R10 | μ-form / μ-number: the Born *form* is invariant in μ; the *numbers* change with μ (swap, CE-8) | A (QB3 §§1, 4–5; reviewed ACCEPT in QB3-EVIDENCE-REVIEW) | Finite bijections; non-native examples only | yes | not applicable | not applicable | On the fixed-basis route the numbers are (b)'s, not (a)'s |

**Column lemma (R2, R3 ⇒).** Let $u$ be a unit column, $\sum_j|u_j|^2=1$, so $|u_j|\le1$.
- For $0<p<2$: $|u_j|^p\ge|u_j|^2$, with equality iff $|u_j|\in\{0,1\}$. So $\sum_j|u_j|^p=1$ iff
  exactly one $|u_j|=1$.
- For $p>2$ the inequality reverses, with the same equality case.

Hence normalised $p$-readout, for $p\neq2$, holds exactly on monomial columns, on every visited
column. Under measurement at every step from a diagonal law, only visited columns enter. So
$Q_{\rm fb}^{p}$ realizes exactly the laws of phased-permutation dynamics on the reachable
support. These are $D$'s laws, which equal $S$'s (R1). Conversely, $S\subseteq D\subseteq
Q_{\rm fb}^p$ through `D_imp_Qfb`, whose weights are 0/1 (EQ:302).

**(⇐) of R3, coherent preparations included.** With monomial dynamics only, a $p$-normalised
preparation stays $p$-normalised. Each read then returns $|{\rm amp}|^p$, which is a law for
every $p$. So no record discriminates $p$.

**Answer to Q1.** Every result that constrains $p$ or $f$ does so conditionally:
- through a non-monomial admissible family (R3, R4);
- through a supplied context structure (R5);
- through supplied kinematics (R6);
- or through a supplied measure or response (R7–R9).

None of these antecedents is in column (ii). The constraint that does hold unconditionally runs
the other way. At the fixed-basis level, $p$ is not merely unselected by the construction; it is
unselectable (R2).

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
1. **Symmetry versus operation.** $\mathfrak u(6)$ is the commutant of the dynamics, a symmetry. R4
   needs operations the observer executes and reads. FI-1, which asks only for one such
   non-monomial operation, is itself not supplied (R3). Main distinguishes a derived continuous
   path from an executable operation (Main:274, Main:590).
2. **Read basis.** (d′) is modulus-only in a fixed read basis.
   - In the $J$-mode basis the update acts diagonally, by mode phases. It is therefore monomial
     there, and every $p$ fits (R3 ⇐).
   - The site basis carries no $J$-amplitudes, because $J$ is nonlocal in space.

   Which basis, if any, the observer's records read is not stated anywhere read.
3. **Null modes.** The candidate fails on the sector at $\alpha=1/d$.
4. **The lift.** The real lift's derivation from φ is open (SM:232).

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
- **Effect on #1059.** None on (a). It adds a planning cross-reference to (b) only.
  **CONFIRMING.**

### 4.3 Access restrictions with only QM-matching support (SHM §9 [D]: SA-1(c), Tsirelson soundness, null-result invasiveness)

- **Where the probabilities come from.** On the SA-1 route the probabilities of the
  stabilizer-scope sequential $Z/X$ law come from N2, the uniform law on unknown slots, that is,
  from the measure (b). The amplitude dictionary appears only in the comparator. So the route
  never reads $f$ off an amplitude, and R3 and R4 do not apply to it. AP1 already scopes out
  "Born-rule selection beyond the values `0, ½, 1`" (AP1:1062).
- **Stabilizer agreement pins $f$ only at dyadic points (P2, computation-supported).** Even if
  the route did read amplitudes, stabilizer-scope agreement would constrain $f$ only on
  $\{2^{-k/2}\}$:
  - Every $n\le3$ stabilizer state (6, 60 and 1080 states, matching the known counts) has
    computational-basis moduli that are equal on a support of size $2^k$.
  - $f(u)=u^2+u^2\prod_{k=0}^{3}(u^2-2^{-k})^2$ satisfies $f\ge0$ and $f(0)=0$, is not $u^2$,
    and normalises every one of these states exactly.
  - It fails on $(\cos\frac\pi8,\sin\frac\pi8)$.
  - Mutation control: removing the $k=3$ factor breaks normalisation on an 8-element support.

  This is the stabilizer-scope analogue of BORN-SRC-1's C4.
- **Effect on #1059.** None on status. The SA-1 route cannot select (a) beyond the dyadic points,
  whether or not SA-1(c) is ever independently justified. Its numbers belong to (b): they apply
  N2 to supplied ready cells through H-PREP, which is an open hypothesis (AP1:418; SHM §9 [D] cites it as AP1:417).
  **ELABORATING** (P2 is new as a check; the scope statement was already at AP1:1062).
- **One inconsistency between drafts** (§6 F-a). SHM §9's N2 row answers column (ii) "yes for the
  counting measure, Main's maximal-entropy selection". Main:726 (iv) calls that selection "not
  derived", and BRIDGE B3 types it Op. Under §1's columns it is a posit, not a column-(ii) "yes".

### 4.4 FI-1, the first unsupported forward implication (BRIDGE §5.1 [D])

BRIDGE §5.1(c) states one direction: "on monomial operations $|U|^p$ gives the same table for
every $p>0$". R3 supplies the other direction, under H-LIN ∧ H-RF$_p$. Together they give
**(a-pow) ⟺ FI-1**, each direction elementary and known. Consequences:
- **(a-pow)** has no content independent of FI-1. That makes (a) downstream of #1211's FI-1 in
  the dependency graph. Recording that edge is a planning decision (§7 OQ-1).
- **(a-gen)**, the full dictionary, needs FI-1 together with density on $n\ge3$ and (d′) (R4),
  or the (d1)–(d4) context structure (R5). O1 decides which target applies. Today's findings
  supply none of these antecedents.
- **One §A.34 point about BRIDGE.** Its §6 "Born statistics" row reads "An independently
  justified selection of the quadratic functional on non-monomial (state-mixing) operations;
  equivalently a source of non-monomial admissible operators". Only one direction holds:
  - A source of non-monomial operators is *necessary* for any selection (R3 ⇐).
  - It is sufficient only inside the power family under H-RF$_p$ (R3 ⇒).
  - For general $f$ it is not sufficient (C4; P2).

  "Equivalently" should read "requires" (§6 F-b).

**ELABORATING.** The reduction is stated in BORN-SRC-1 §4(a) and BRIDGE §5.1(c). This unit adds
the two directions together and the class version R2.

### 4.5 What is open on #1059 after today

| Part | Status at `fd539e15` | Prerequisites, after today | Change |
|---|---|---|---|
| (a-pow) exponent in the power family | open | FI-1 (#1211), under H-LIN ∧ H-RF$_p$, which are supplied | Relocated: equivalent to FI-1 under the named hypotheses |
| (a-gen) full quadratic dictionary | open | FI-1 + a native dense family on $n\ge3$ + O1's target ((d′), or (d1)–(d4)) | None. $J$ names a candidate carrier only (§4.1) |
| (b) hidden-sector measure | open; analysis paused | Unchanged. On the continuum and seed routes it carries the Born law itself (R7, R8) | None. SHM's N2 column (ii) is overstated (§4.3) |
| (c) preparations across settings | open; blocked on O-INS | Unchanged. Exact irrational targets need a non-finite source (R9) | None |
| (d) context independence | no kernel result | Native contexts on $\dim\ge3$, beyond stabilizer scope (P2) | None |

The QB3 limitation stands as stated: "OI has not yet been shown to derive the Born rule or select
the physical probability measure."

***

## 5. Question 3: the smallest decisive next paper question

**NQ-1059.** *Under the observer's stated access (AP1's P1–P3 with H-PREP, or any access stated
on `main`), is there an executable operation whose action on a carrier block of dimension $\ge3$
is non-monomial in the block's read basis and not stabilizer-only? Not stabilizer-only means
that some column has a $|\cdot|^2$-profile that is not uniform on its support. The first place to
pose this is the $J$-complex non-null sector of the real lift (§4.1). The question also asks which
read basis, if any, the records use there.*

- **Why it is decisive.** Either answer changes what #1059 can do.
  - *No* (on the classes examined): (a-gen) and (d) have no route on `main` whatever O1
    decides, and (a-pow) waits on FI-1 alone. #1059(a) and (d) can then be planned as
    downstream of #1211, leaving (b) and (c) as #1059's own content.
  - *Yes*: this is the first object on which O1's two targets differ in content. (d′) with
    density would give $u^2$ by R4. Gleason/Busch would further need the projector lattice of
    (d1). O1 then becomes decidable on content rather than in the abstract.
- **Why it is small.**
  - It needs no measure, no preparation law and no comparator.
  - Its negative branch can be checked against existing records: the quarter-phase bounds;
    MECH-1, MECH-2 and M-INACC-1 (cited at BRIDGE §10); FI-1's kernel negatives at Main:590.
  - Its positive branch needs one exhibited operation plus a read-basis statement.
  - Generic parts, such as the stabilizer criterion and the profile test, are exact checks of
    the P2 kind.
- **Scope guards.**
  - It is posed for the stated access. A negative answer is not a no-go for extended mechanisms
    or for the unresolved site-space formulation (Main:590).
  - It overlaps #1211's NQ1 (the $J$ question) and FI-1. It must not duplicate them. It adds the
    dimension-$\ge3$, non-stabilizer and read-basis conditions that #1059 needs.
  - It adopts no premise. (d′) and Gleason remain O1's to choose.

*Alternative, if the owner prefers to stay within (b):* AP1's Q-B (AP1:1082–1085), stated for
#1059. Which of Main's measure branches (α–δ), applied to the minimal continuum carrier with
conditioning on the record, yields the cosine-weighted re-preparation without a supplied
density? This was ranked second: the one-vector outcome under γ looks predictable from AP1:1013,
so it risks being a relabelling rather than a test (§A.31). A pre-registered decision rule would
be needed first.

***

## 6. Findings for other records (recorded only; no edit made)

- **F-a (SHM §9, N2 row, draft).** Column (ii) reads "yes for the counting measure, Main's
  maximal-entropy selection". Main:726 (iv): "a standard but substantive epistemic postulate,
  not derived"; Main:56 calls it "a selection principle". Suggest "posit (Op)" to the #1210
  reviewers.
- **F-b (BRIDGE §6, "Born statistics" row, draft r2).** "equivalently a source of non-monomial
  admissible operators" asserts an equivalence of which only the necessity direction holds (R3 ⇐;
  the sufficiency counterexamples are C4 and P2). §A.34. Suggest "requires".
- **F-c (T3 on `main`).** The landed file's header (T3:3) still reads "independent review
  pending, 2026-11-07". #1059 c.6705021068 records a separate independent ACCEPT on #1173 for the
  same blob (the file is unchanged between `23150480` and `fd539e15`). This is a stale status line
  in a mutable record (§A.46 item 4). Its use above is limited to statements it cites from `main`
  and to T3 §6.1's rationality argument, which is elementary.
- **F-d (Main, unchanged since BORN-SRC-1).** Main:20 and Main:556 still point to "§3.1" for the
  exponent frontier; BORN-SRC-1 F2 gives §3.4. Main:226 and Main:351 are as BORN-SRC-1 found them.
  Main:648, "The characterization theorem establishes the Hilbert space, unitary dynamics, and
  Born-rule transition probabilities", can be read as available → derived against Main:20. It is
  not in BORN-SRC-1's site list (whose lines are at `02009693`), and it belongs to O2's remit, not
  #1059's.

***

## 7. Owner questions

- **OQ-1.** Should #1059 record a prerequisite edge from (a) to FI-1 (#1211 §5.1), with (a-pow)
  stated as equivalent to FI-1 under H-LIN ∧ H-RF$_p$ (R3), and (a-gen) as needing FI-1, a dense
  native family and O1?
- **OQ-2.** Is NQ-1059 (§5) the next #1059 unit, given that it overlaps #1211's NQ1? Or should it
  be folded into #1211 as an added condition (dimension $\ge3$, non-stabilizer, read basis)?
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
  - BRIDGE §§0–3, §5.1, §6 (ingredient rows), F4 and §11;
  - REVIEW in full;
  - SHM §0, §8 rules, §8.3, §8.4 and §9.
- **Read at the cited lines:**
  - Main:20, 56, 226, 288, 351, 552–556, 590, 646–656, 726;
  - T3:1–160 and 240–270;
  - AP1:240–250, 830–845, 975–1095;
  - WMB:1–40 and 205–222;
  - A1R:1–90;
  - Structure:1117; Substratum:16–68, 131–145, 481;
  - EQ:190–340, 462;
  - the H-Bell round-1 preregistration head.
- **Searched at `fd539e15`** (`git grep -i` over `verification/`, `papers/` and `book/`): "born",
  "quadratic exponent / functional / sensor / rule", "|U|^p", "hemisphere", "cosine-weighted".
  The negatives stated in §§3–5 ("no native dense family", "no frame-function predicate", "no
  record stating a read basis for $J$-amplitudes") are scoped to that search, to BORN-SRC-1's
  search at `02009693`, and to the files read. Lean files were read only at EQ's lines. No kernel
  build was run.
- **Probes** (generic objects only; exact sympy and Gaussian-integer arithmetic; run with
  `python3 -I`; exit status 0):
  - `probes/p1_fixed_basis_power.py`, sha256 `82361ef8…a3d2`, output `probes/p1.out`. Checks:
    permutation tables at $p\in\{1/2,1,2,3,7\}$ for $n\le4$; the column lemma at $p=1,4$ on 28
    grid profiles; a Cayley unitary with column $|U|^4$-sums 81/169, 21105/48841 and 1341/3757
    (control).
  - `probes/p2_stabilizer_points.py`, sha256 `90efad3b…a94c`, output `probes/p2.out`. Checks:
    stabilizer counts 6/60/1080 (control); uniform-modulus supports; normalisation of the
    countercontrol $f$; the non-stabilizer control; the mutation control.

  Neither probe was reproduced by a second writer. R2 and §4.3's statements rest on the paper
  argument plus these checks, and are marked computation-supported where the check is the only
  support.
- **Not done:** no computation on any OI mechanism, the real lift or $J$ included. No literature
  source was re-read first-hand: Logiurato–Smerzi, Aaronson and Masanes–Galley–Müller are cited
  as BORN-SRC-1 and T3 report them. No #1082 file was opened beyond what QB3 lands. No #1210 or
  #1211 file was edited.
