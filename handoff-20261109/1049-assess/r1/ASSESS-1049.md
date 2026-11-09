# ASSESS-1049 — what is open on #1049 (linear vs affine microscopic dynamics) after the #1210/#1211 findings of 2026-11-09

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Pending a fresh, independent
review.** Nothing here is adopted, promoted or proposed for the manuscripts, and no status changes.
A review ACCEPT, if reached, authorizes nothing further.

- **Accountable home.** #1049. Parent #983; related #914, #1029, #1210, #1211, #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1049 c.6740117832 (full record #1169
  c.6740116927): "One paper-only unit each, re-assessing its open question against today's
  #1210/#1211 findings … each with a fresh review. Exact generic checks only." Not authorized:
  computation on an OI mechanism, new physical assumptions, freeze, dispatch, manuscript changes,
  merges. This unit made no git or GitHub write and edited no manuscript.
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09; the same SHA as the #1211 unit 1 and #1210 Phase 1 drafts). `Sub`, `SM`, `Main` are
  `papers/{Substratum,SM,Main}.md` at that SHA; line numbers refer to it. `A5` =
  `verification/programmes/substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md`; `Q4` = the
  same directory's `A5-Q4-STAGE2D.md`; `Q3` = its `q3-a6-offsets-20261108/ASSESSMENT.md`; `QP` =
  `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`; `AP1` =
  `…/reconstruction/apparatus-1-20261107/DESIGN.md`; `MECH-1`, `MECH-2` = `…/mechanism-1-20261107/`,
  `…/mechanism-2-20261108/DESIGN.md`.
- **Today's drafts (off `main`, unverified; §A.46 item 7: hypotheses, not premises).**
  `BRIDGE` = `scratchpad/bridge/BRIDGE-UNIT1.md` (#1211 unit 1, r2), with its review
  `scratchpad/bridge/review/REVIEW-UNIT1.md` (REVISE, on r1) and `DISPOSITIONS-UNIT1-r2.md`;
  `QX3`, `QX4`, `SHARED` = `scratchpad/qphen/{QX3-ANTIBUNCHING,QX4-INCOMPATIBILITY-LG,SHARED-MECHANISM}.md`
  (#1210 Phase 1, r4).
- **Labels.** [K] kernel-checked on `main`; [P] reviewed record or paper text on `main`, cited;
  [A] exact algebra done here by hand; [D] derivation here, unreviewed; [X] exact generic check run
  here (`probes/`), a result supported only by it being *computation-supported*; [L] literature from
  memory, not re-read; [H] a hypothesis taken from today's unverified drafts; [O] owner decision.

***

## 0. Summary

1. **Affine over non-affine is not derived (§2.1).** The corpus route is: unobservability of
   absolute amplitude ⇒ "every first difference of the update is independent of its base point"
   ⇒ affine (SM:240; Main:726 (vii)). The second arrow is the linearity-equivalence lemma, an iff.
   The first arrow is not proved, and in its uniform form it fails: for d = 2, 3 there are
   non-affine, centre-free, cubic-isotropic, translation-commuting, nearest-neighbour second-order
   rules for which **every** uniform map x ↦ λx + c𝟙 is an exact dynamical symmetry [A; X: P1].
   Under the owner's relabelling reading of amplitude shifts [O, Q2], the gauge constrains no rule.
   So the affine restriction rests on the site-wise base-point form, which is equivalent to it.
   Main (vii) and SM:240 state this scope; Sub:100, :104, :220, :272, :274, ch02:84 and FULL:718
   present the affine restriction as following from the gauge principle without it.
2. **Linear over affine stays unselected (§2.2).** Today's drafts add no selector. A5 R5 and Q3
   outcome (N) stand as the record, both WIP / UNVERIFIED.
3. **Most downstream results use affinity or only the bipartite read pattern, not b = 0 (§3).**
   The quarter-phase obstruction's sector split holds for non-affine nearest-neighbour rules [X: P3].
   Lemma G2 needs affinity, not linearity [A; X: P2]. Lemma Q(i) needs b = 0, but Q(iii) does not
   [A; X: P2]. The positive-frequency J and SM's chirality identities are statements about the
   linear part and do not depend on b [A]. #1210's bounds are stated for the affine-symplectic class.
   b = 0 does work only at four sites: (A-lin) Stage 2(d), absolute labelled readouts,
   configuration-level conservation laws, and the resonant uniform sector.
4. **The b = 0 content sits on one sector (§3.3).** It is the uniform (k = 0) A₁ sector at
   κ ≡ 2 (α ≡ 1/d for odd q). The same sector is #1049's resonance locus (A5 R3), Q4's open resonance
   condition (Q4c), and #1211's null-mode sector where no J exists (NQ1(a)).
5. **Next question (§5, Q-NEXT).** Does any independently justified OI principle imply the
   site-wise base-point form in d = 3? Equivalently: does any such principle exclude P1's class of
   non-affine rules that have the uniform additive-automorphism group as an exact symmetry? A
   companion question, for b = 0, is the resonance of the A₁ sector at k = 0 (Q4c and #1211
   NQ1(a)).

***

## 1. Inputs and their standing (§A.46 item 7)

| Input | Standing | Used here as |
|---|---|---|
| Linearity-equivalence lemma (base-point-independent first differences ⇔ affine) | [P] Sub:274 (telescoping proof plus exhaustive checks); re-derived [A]: ⇒ by telescoping, ⇐ immediate | established, both directions |
| A5 (WIP / UNVERIFIED; model review ACCEPT at `f07f55d0`; merged `9e0560d8`) | record on `main`, not established | B0.1, B0.2 and Prop. 2.5 re-derived here [A] where used. R5 and R6 are cited as the record |
| Q4 (WIP / UNVERIFIED; model reviews; merged) | record | outcome (iii) for O1–O4 cited as the record |
| Q3 (outcome (N); merged `45eea51d`) | record | cited as the record |
| QP Lemmas G1, G2, Q | [P] paper proofs, model-reviewed per QP | statements read; extended in §3.2 [A; X] |
| BRIDGE "linear beyond affine has no independent justification" | [H]; it cites A5 R5 | checked against R5 (§2.2) |
| BRIDGE "quarter-phase obstruction shares premises (linearity, CI, bipartite NN graph) with SM chirality" | [H]; BRIDGE §0 item 6, §10 | refined in §3.2 |
| BRIDGE "positive-frequency J exists off the null modes" | [H]; J² = −1 re-derived here [A] | §3.3 |
| QX3 A3.1(b)–(c): affine routing under `NCONS_ready`; non-affine forced under `NCONS_global` | [H]; A3.1(c)'s core lemma re-derived here [A] (an affine bijection of F₂ⁿ preserving Hamming weight everywhere is a coordinate permutation: T(0) = 0, columns have weight 1, and the columns are distinct) | §2.1(iii), §3 row 9 |
| QX4 A4.1 affine-symplectic Leggett–Garg bounds | [H]; scope as stated ("with translations"), numbers not re-checked | §3 row 8 |
| SHARED §9 SA-1(a) row and column (ii) | [H] | §3 row 7 |
| Owner Q1/Q2 (#1049 c.6624263637, amaybaum, 2026-11-04T06:28:45Z) | [O] | binding readings |

***

## 2. Question 1 — what selects, on independent grounds

The three answers are kept separate. (i): is the restriction well-defined? (ii): does it follow
from independently justified OI principles? (iii): does it reproduce QM or the SM? A positive (iii)
is never cited for (ii).

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

*Three readings of the operational principle, and what each gives.*
- **(R-rel), relabelling.** Amplitude maps are conjugations of the description. This is the owner's
  reading [O, Q2]: "Treat amplitude shifts as mathematical relabellings unless their physical gauge
  status is justified." A conjugation carries every rule to an equivalent description of itself. So
  (R-rel) excludes no rule, affine or not [A].
- **(R-uni), uniform symmetry.** Every uniform x ↦ λx + c𝟙 (λ a unit) is an exact dynamical symmetry.
  For the second-order form this means F(λx + c𝟙) = λF(x) + 2c𝟙 [A].
  - **d = 1, odd prime q: (R-uni), with centre independence and reflection symmetry, forces
    F_i = x_{i−1} + x_{i+1}: linear, with b = 0 and α = 1 [A].** Proof: covariance under c gives
    F_i = s + G(y), where s = x_{i−1} + x_{i+1} and y = x_{i+1} − x_{i−1}, using 2 ∈ (ℤ/q)^×. Scaling
    gives G(λy) = λG(y), so G is linear. Reflection makes G even, so G = 0. Positive control: at q = 3,
    exhaustive over all 3⁹ functions, the only solution is f = s [X: P1].
  - **d = 2, 3: (R-uni) does not imply affinity [A; X: P1].**
    - *d = 3, prime q ∤ 6.* Let p_a = x_{+a} + x_{−a} for each axis a. Set a′ = 2p_x − p_y − p_z, with
      b′ and c′ its cyclic versions, C = a′b′c′ and P = a′² + b′² + c′². Then
      f = (1/3)Σ_nbrs x + C·P^{q−2} satisfies all of the following:
      - f(λv + c𝟙) = λf(v) + 2c, because a′, b′, c′ are shift-invariant and P^{q−2} is homogeneous
        of degree −2 on units;
      - it is O_h-invariant (the 48 elements act on (p_x, p_y, p_z) by permutation);
      - it reads no centre;
      - it is not affine (base-point witness in P1).
    - *d = 2, q = 7.* The same holds for f = (1/2)Σ x + y₃·χ(y₁² − y₂²), where χ is the Legendre
      symbol. With E, W, N, S the four neighbours, y₁ = x_E − x_W, y₂ = x_N − x_S and
      y₃ = x_E + x_W − x_N − x_S. It uses q ≡ 3 (mod 4).
    - *d = 3, q = 2* (the instance displayed in Main §3.2). Take f = Σ x + [all six neighbours equal].
    - P1 checks all four constructions exhaustively, with the linear rule as a control and an
      affine-offset rule as a countercontrol (the latter fails covariance).
    - Bijectivity is automatic for the second-order form: x(t−1) = F(x(t)) − x(t+1).
  - Continuum analogue [L]: shift-symmetric nonlinear field theories (Goldstone, P(X) and Galileon
    Lagrangians) have φ ↦ φ + c as an exact symmetry and nonlinear dynamics. Shift symmetry forces
    derivative couplings, not linearity.
- **(R-site), site-wise base-point independence.** This is the form SM:240 and Main (vii) name. It
  gives affinity by L2, and it is equivalent to affinity. As a principle it is A5-LINEAR-AFFINE's N2
  ("superposition of perturbations"), with "the background never changes the response". No corpus
  source gives it an independent reason. Sub:272 itself records that deriving amplitude
  unobservability from the observer architecture "is … circular".

*Consequence.* The affine part of A5 is a posit in the form named by SM:240 and Main (vii). The
operational principle motivates it but does not entail it in d ≥ 2.
- Main (vii) and SM:240 state the scope accurately.
- These sites present the affine restriction as following from the gauge principle, with no
  site-wise qualifier:
  - Sub:100 and Sub:104 ("restricts the update to an affine one via the linearity-equivalence lemma");
  - Sub:220 ("non-affine wave equations … are the separate class one obtains exactly when that gauge
    principle is dropped");
  - Sub:272 ("the input … is strictly weaker than the output … a non-affine F … the principle
    excludes");
  - Sub:274 ("yields an affine rule as a certified theorem");
  - ch02:84 and FULL:718.
- Read with (R-uni), the "exactly when" of Sub:220 and the "excludes" of Sub:272 are contradicted by
  P1 in d ≥ 2. Read with (R-site), they hold, but then the principle is affinity restated.
- This is a cross-document finding for #1029. It is not an edit (none is authorized).
- **Search scope for "no corpus source":** `git grep -i` for "base-point", "base point",
  "amplitude-scale", "affine" and "non-affine" over `papers/`, `book/` and `verification/` at
  `fd539e15`. The A5-specific records were read in full. The H-D record
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
- **New input from §2.1.** Under (R-uni) in d = 1, the uniform symmetry group does force b = 0 and
  κ = 2, but that is A5-LINEAR-AFFINE's N8 and N8′ jointly, and N8 is a symmetry reading the owner
  has not adopted (Q2). It adds no independent selector.

**(iii) Which QM/SM-reproducing results need b = 0?** See §3. In short, few do, and those few sit
on one sector.

***

## 3. Question 2 — downstream dependence

**Columns.**
- **Uses:** what the result actually consumes. B is the bipartite, centre-free read pattern with
  the second-order form. AFF is affinity. b0 is b = 0.
- **Without linearity:** affine dynamics, b ≠ 0.
- **Without affinity:** non-affine dynamics.

| # | Result | Uses | Without linearity (affine, b ≠ 0) | Without affinity | Support |
|---|---|---|---|---|---|
| 1 | Form lemma; dispersion; Theorem 4; Lorentz (SM:224–232) | AFF (linear part) | Form plus a constant. A uniform offset sources only k = 0; the non-uniform modes obey the linear equation exactly | No global operator. The linearization depends on the background: on the absolute value for G_SM-type rules, on gradients only for P1-type rules | [A]; A5 Prop. 2.5 re-derived |
| 2 | SM chirality: Theorems 3, 12, 13; SM:539 ("nearest-neighbor, so … bipartite"); SM:569 (ΓAΓ = −A) | B plus the linear part | Unchanged: these are identities of the linear operator A and its Schur complement. Γ carries the rule (A, b𝟙) to (−A, bε), just as it carries A to −A at b = 0 | Over the real lift, the Jacobian of an NN centre-free rule keeps the NN pattern at every background, so each linearization stays graded [D]. Not examined over ℤ/q. All of this sits behind the SM:232 / SM:306 bridges | [A]; [D] |
| 3a | QP Lemma G1, sector split | B only | Holds modulo constants: each slot is a single-type linear form plus a constant [A; X: P2(A)] | **The functional split holds for any NN centre-free rule on a bipartite graph:** each slot is a function of one sector's variables [A; X: P3]. The induction does not use linearity. Countercontrols: a centre read and an i+2 read break it | [A]; [X] |
| 3b | QP Lemma G2 (non-adaptive quarter-phase obstruction) | B plus AFF (step 3: R1 and R0 differ by a map linear in the state) | Holds: common offsets cancel from the difference of two runs [A; X: P2(C)]. QP's class N already contains supplied constant translations, and node 9 records that fixed offsets cancel | Not examined. Step 3 fails in general | [A]; [X] |
| 3c | QP Lemma Q(i), conservation of Q = Σ uᵢvᵢ at q = 2 | b0 | **Fails:** Q(step z) = Q(z) + b·u exactly [A; X: P2(B), exhaustive for n = 3, 4]. A uniform b = 1 (the complement rule) breaks it | — (MECH-2 and M-INACC already record that it fails for G_SM) | [A]; [X] |
| 3d | QP Lemma Q(iii), the Q* = 0 protection | the linear part (symplectic) | Holds. QP's own proof treats each branch as "symplectic center-free steps and constant translations", and "translations change values, not which functionals are determined" | Fails for G_σ (M-INACC RESULT §0, [P] record) | [P]; [A] |
| 4 | #1211 J (BRIDGE F4, NQ1) | the linear part, on the difference space | **Independent of b:** Φᵗz − Φᵗz′ = Lᵗ(z − z′) (B0.1 re-derived), so J commutes with Φ's action on differences wherever it commutes with L. The uniform offset's non-removable effect lies in the k = 0 sector, which at α = 1/d is a null mode where no J exists for b = 0 either. At the staggered null mode an offset is removable, and J is absent anyway | A tangent action that depends on the background. Any J would then also depend on the background. Not examined | [A] |
| 4′ | NQ1(b), whether Σ is J-Hermitian | depends on what Σ is | A centred covariance does not depend on b. A raw second moment ⟨φφ†⟩ picks up the A₁, k = 0 drift (H-b; bt²/2 at resonance) | — | [A] |
| 5 | Stage 2(d) and Theorem 5 (Q4) | b0 under (A-lin) | Q4 outcome (iii) for O1–O4: U(1)_S is lost, and G_v reproduces O1–O4 at group level only. Carrier-level agreement is conditional. O5 is open | — | [P] record |
| 6 | A6 extension (Q3) | — | Outcome (N): none of E1–E3 is justified | — | [P] record |
| 7 | #1210 SA-1(a) (SHARED §9: column (ii) "yes, conditional on (A4)–(A5)") | AFF plus symmetric coefficients | Unchanged. AP1's backaction identity treats a known displacement as no disturbance, and a native offset is a known displacement | Outside SA-1(a)'s class | [H]; [A] |
| 8 | #1210 QX4 A4.1, affine-symplectic LG bounds (`K₃ ≤ 1` scan, `K₃ = 2` witness) | AFF (stated "with translations") | Unchanged by construction | Outside scope | [H] |
| 9 | #1210 QX3 routing (A3.1) | — | Affine routing exists under `NCONS_ready` | Required under `NCONS_global` | [H]; core lemma [A] |
| 10 | M15 reciprocity | AFF (symplectic linear part) | Unchanged | Can fail: G_SM is not reciprocal | [H]; [P] MECH-2 |
| 11 | Main's interface: the absolute labelled readouts of the Q1 baseline | b0 | Labels differ by p_V(t) (A5 Thm 2.2). At prime q, when κ ≢ 2 the shift is static (uniform-shift conjugacy), and when κ ≡ 2 it can be time-dependent, with invariant content such as #Fix = 0 for S1 | — | A5 B0.2/B0.3 re-derived [A] |
| 12 | Main:726 (v): quadratic invariant and energy shells; D5, D6 | b0 | Q′ = Q − b(S_t + S_{t−1}) replaces Q. The shells differ | — | A5 N4 |
| 13 | Main §3.4 representation; C4 | none | Unchanged | Unchanged | [P] |
| 14 | Bijectivity; P-indivisibility (SM:106, :112) | second-order form only | Unchanged | Unchanged | [P] |

**3.1 Reading of the table.**
- **Linearity proper (b = 0) is used only at rows 3c, 5, 11 and 12, and at the raw-moment reading
  of 4′.**
- **Affinity is used at rows 1, 2, 3b, 3d, 4, 7, 8 and 10.**
- **Row 3a uses neither.**

**3.2 Correction to the #1211 premise claim [H].**
- **The claim.** BRIDGE §0 item 6 lists linearity among the premises the quarter-phase obstruction
  shares with SM chirality.
- **What the obstruction uses.** On rows 2, 3a and 3b, the shared premise is the bipartite,
  centre-free read pattern with the second-order form. Lemma G2 additionally uses affinity.
  Linearity beyond affine is used by neither.
- **Where the sector split fails.** By P3 it fails only when a rule reads its own site or a
  same-colour site.
- **Bearing on MECH-2:532.** MECH-2:532 attributes the failure of AP1's grading under G_SM to G_SM's
  "nonlinearity". Under P3 and the argument below, the decisive feature is G_SM's same-sublattice
  read, i+2. G_SM's non-affinity is not the decisive feature.
- **Argument [A].** Under the functional split, every record is a function of one sector's variables.
  With a prior that factorizes across sectors (N2), the conditional support is then a product set.
  On a product set a mixed functional z + x is constant only if z and x are each constant. So the
  support {01, 10} of P★ needs a slot that mixes sectors.
- **Scope.** This holds for priors that factorize across sectors. H-PREP preparations that correlate
  the sectors are not covered.

**3.3 Where b = 0 does work: one sector.**
- **The sector.** At prime q, the content of a uniform offset that no static uniform relabelling
  removes is confined to the uniform mode of the zero-mode locus κ ≡ 2 (mod q). For odd q this is
  α ≡ 1/d; at q = 2, κ ≡ 2 holds for every α (B0.3(b)–(c), re-derived [A]). On the real lift the same mode is the k = 0 mode. It is the mode of
  secular growth bt²/2, and at α = 1/d it is a null mode where no J exists (row 4). With the
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

***

## 4. What is open on #1049 now

**O-A. The affine part has no independent derivation.**
- Its status is a posit, in the site-wise base-point form (§2.1). The uniform operational form is
  satisfied by non-affine rules in d ≥ 2.
- This is new relative to A5, which scoped non-affine rules out. It moves the "partly derived" of
  Sub:100 and :104 to an open question.
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
- Each is therefore conditional on the posit of O-A, not on A5's linear clause.
- SHARED §9's "yes, conditional on (A4)–(A5)" for SA-1(a) column (ii) would read more precisely as
  "conditional on A4 and on the affine restriction (a posit); linearity beyond affine not used".
  That is a proposal for #1210's writer. No #1210 file was edited.

**O-E. Pressure against affinity from the programme's own needs.** Three items: G_SM (SM:112),
in-world setting selection (MECH-1), and global-conservation routing (QX3, owner Q3-2). If any of
them is adopted, it needs a non-affine element. Under §A.29 that element must carry its own
independent justification.

***

## 5. Smallest decisive next paper question

**Q-NEXT.** *Does any independently justified OI principle imply the site-wise base-point form in d
= 3? Equivalently: does any such principle exclude the P1 class of non-affine, centre-free,
O_h-isotropic, translation-commuting nearest-neighbour rules that carry the uniform
additive-automorphism group as an exact symmetry?*

The principles to test are these:
- A1–A4 and A6 as stated;
- E4;
- the trace-out interface of Main §1;
- amplitude-scale gauge in the owner's relabelling reading;
- the alphabet-size hypothesis (SM:94) as a candidate.

**Why it is decisive.**
- **A negative answer** makes A5 a posit in full: affinity and linearity alike, with an operational
  motivation for the affine part only. The "partly derived" wording becomes a #1029 item.
- **A positive answer** names a principle with a consequence beyond affinity. That principle is then
  judged under §A.29.
- Either answer settles O-A. O-A is upstream of O-D and of rows 1, 2, 3b, 4, 7 and 8.

**Why it is small.**
- P1 already reduces it to one function class.
- Each principle is checked by asking whether it constrains f beyond the uniform group, on paper.
- No mechanism computation is needed.
- An optional exact generic control is to extend P1 to the alphabet-size correspondence, which is
  not constructed in SM:94. That control would need its own authorization.

**Companion question, for b = 0 (smaller, but downstream of an open bridge).** This is §3.3's sector
question: *on the branch the observer uses, is the uniform A₁ sector at k = 0 resonant (κ ≡ 2,
μ_{A₁} = 1) and accessible?* It merges Q4c with #1211 NQ1(a). Its answer is conditional on SM:232's
unproved φ → L_obs bridge, which is why it is second.

***

## 6. Questions for the owner

1. **The "partly derived" wording (O-A).** Main (vii) and SM:240 carry the site-wise form. Sub:100,
   :104, :220, :272, :274, ch02:84 and FULL:718 do not. Should this be recorded under #1029 as a
   candidate correction (scope wording only), pending review of P1? No manuscript change is made or
   proposed for this unit.
2. **Q-NEXT as the next #1049 unit?** Should it be a separately authorized paper-only unit, or
   should #1049 rest at outcome 3 (a scoped negative) for both the affine and the linear clause?
3. **Routing to #1210 and #1211.** Should the refinements of §3.2 (shared premise B, not linearity;
   the MECH-2:532 attribution) and O-D (SA-1(a) column (ii)) be passed to the #1211 and #1210
   writers as review inputs? This unit made no edits to their files.
4. **Generic-check boundary.**
   - P2 and P3 run second-order steps with random coefficients and random local functions on cycle
     graphs. They check the scope of QP's lemmas, and are not a computation of any OI observable.
   - P1 constructs functions over ℤ/q as counterexamples to an implication. They are not proposed
     rules.
   - Does the owner read these as within "exact generic checks only"? If not, the statements they
     support fall back to their [A] paper arguments, which §2.1 and §3 give in full.

***

## 7. Classification of findings (§A.31) and pressure tests

**Classifications.** Each label is relative to a `git grep` of `papers/`, `book/` and
`verification/` at `fd539e15`, and to today's drafts.
- **F-1 (§2.1, P1): uniform amplitude covariance does not imply affinity in d ≥ 2; it does in
  d = 1. NEW, candidate.** No record separates the uniform form from the site-wise form. A5 scoped
  non-affine rules out. H-D U6 quotes the lemma only.
- **F-2 (§3.2, P3): the sector split survives non-affinity under a bipartite read pattern.**
  - Relative to MECH-2:532's attribution: NEW, candidate.
  - Relative to QP: ELABORATING, since QP proves G1 for linear updates and notes that "Lemma G1 uses
    only the finite update".
- **F-3 (rows 3b–3d): G2 and Q(iii) hold for affine rules; Q(i) fails. ELABORATING.** QP node 9
  and check c8 treat fixed offsets. Q(i)'s failure for b ≠ 0 was not found stated.
- **F-4 (§3.3): one sector carries the b = 0 content, and it coincides with NQ1(a) and Q4c.
  ELABORATING** (a merge of three open items).
- **F-5 (rows 4 and 4′): J does not depend on b; the centring of Σ matters for NQ1(b).
  ELABORATING.**
- **F-6 (§2.1(iii)): G_SM violates even the uniform form. ELABORATING.** MECH-2 records "A5 fails".

**Pressure test of the favourable branch.** The favourable reading is that "linear beyond affine
carries little weight" (§3.1). It lightens the cost of A5's unjustified clause. Five checks follow.
1. **What the reading needs.** It holds only when rows 2, 3b, 3d, 4, 7 and 8 are read as statements
   about linear parts or difference spaces.
   - At the owner's absolute baseline (row 11) and for configuration-level conservation (rows 3c and
     12), b = 0 does matter.
   - Under (A-lin), so does Stage 2(d)'s singlet U(1) (row 5).
2. **Where the weight goes.** The reading moves weight from "linear" to "affine", and §2.1 finds
   affine equally underived. The net effect is unfavourable: A5's two clauses are both posits, and
   the downstream results inherit the affine one.
3. **Row 2's non-affine column.** It is only a [D] remark on linearizations over the real lift. It
   is not offered as support for any chirality claim over ℤ/q.
4. **The F-1 counterexamples.** They are generic functions chosen to satisfy (R-uni). They test an
   implication; they are not offered as physics.
   - In d = 1 the implication holds. The claim is therefore scoped to d ≥ 2, and to the uniform
     symmetry group.
   - It does not show that some other independently justified principle fails to give affinity.
     That is Q-NEXT.
5. **The search is finite.** No universal negative is stated.

***

## 8. Verification scope

- **Paper.** Every [A] step above was done by hand. These include:
  - the d = 1 uniqueness;
  - the P1 covariance and isotropy arguments;
  - B0.1, B0.2 and B0.3(b)–(c), Prop. 2.5 and the J² = −1 identity;
  - the affine weight-preservation lemma;
  - the product-support argument;
  - the Q(i) offset identity.
- **Exact generic checks (`probes/`).** These are exact integer arithmetic over ℤ/q and are not a
  computation on an OI mechanism:
  - `p1_uniform_gauge_not_affine.py` — sha256
    `7f03a6ca37c887820d6fa92027ad484a210c19b4a255314ed59adefd5dd3a161`; output `p1.out`
    `309f38b8b00f5b081a260277d16ea1098519fc6914caeb039cccf46ebc061e76`; ALL PASS. Exhaustive over
    (ℤ/q)^{2d}, for:
    - d = 3 at q ∈ {2, 5, 7};
    - d = 2 at q = 7;
    - d = 1 at q = 3 (all 3⁹ functions);
    - with the linear control and the affine-offset countercontrol.
  - `p2_grading_affine.py` — sha256
    `26a8f26043afb3bc9738b2bb59312d10451118e7cfcade94fa9587baaef44dce`; output `p2.out`
    `b7d483b2118033edeb3f6c83076c2e2bca13be76324ae9e41767d135ee7c05f0`; ALL PASS.
    - (A): 20 seeded random affine runs on C₆ at q ∈ {2, 3, 5}, with self-term and odd-cycle
      countercontrols. The C₅ countercontrol uses an improper colouring, so it is a sensitivity
      control only.
    - (B): exhaustive over every symmetric zero-diagonal K, every b and every state, for n = 3, 4
      over F₂.
    - (C): 50 seeded random cases.
  - `p3_grading_nonaffine.py` — sha256
    `2edd0b311680243e0a0a2cea3758cb6dbfc6c53da700ee48ccbb919ed49ff1b3`; output `p3.out`
    `8346fa0f346ee37b6cee83f5526515bc1a34e59c1535d2bee63facd9805767ac`; ALL PASS.
    - Support-dependence, exhaustive over initial states, for C₆ at q = 2 (T = 5) and C₄ at q = 3
      (T = 4).
    - Random local tables per site and tick: 157 of the 230 tables were non-affine.
    - Centre-read and i+2-read countercontrols.
- **Not done.** Kernel builds, manuscript edits, the A5 §7 or Q4 §7 computations, and any edit to
  #1210 or #1211 files. No git or GitHub writes.
- **Reading coverage.**
  - Read in full: #1049 and all of its comments; A5; the Q4 results and §§1–2, 4–6; Sub:98–104,
    :159, :163, :220 and :270–274; SM:92–112, :224–242; Main:726; QP §1.2, nodes 1, 3 and 6, :690–745
    and :836–848.
  - Read in part: Q3 (outline and the outcome table), and MECH-1 and MECH-2 at the cited lines.
  - From the drafts: BRIDGE §0, F4 and §§9–12; REVIEW-UNIT1 (B3 and the verdict table);
    SHARED §9; QX3 A3.1; the QX4 affine passages.
