# Node 9: which OI condition yields operational structure beyond the minimal tensor product? Preregistration

**DRAFT — NOT FROZEN; no computation may run against this draft.**

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. Freeze
requires the owner's choice of the first candidate model (§4; `NOTES.md` Q1) and the sha256 of the frozen bytes recorded
before any computation. The decision rules are fixed here; expected numbers are not (§A.29).

**Governing question (owner, 2026-10-21).** Which independently motivated OI condition, stated in OI's own terms
(visible and hidden cells, φ, coupling steps, ancillas, records), yields operational structure beyond the minimal tensor
product, and specifically C5-P, operational purification with essential uniqueness? C5-P is the primary target. C2
(persistence of hidden records) is admitted as a possible implementation mechanism. It is not a substitute for
demonstrating purification or contextuality.

**Tags.** [corpus] text quoted verbatim from the corpus at the base, with file:line; [rec] stated in a thread record, not
re-derived; [W] written argument, to be reviewed; [EC] exact computation (none run); [lit-read] literature read in full
and the claim verified against the text; [Q] literature not read, whether recalled or known only from a search summary.
No claim tagged [Q] decides a verdict (§9).

***

## 0. Base and state of knowledge

- Thread `research/missing-component-20261020` at `d924b5bb584f16a76508dfc0f7dcf15e8c3aa48a` (node 8 step 1 repair;
  PLAN = `../PLAN.md`, MC*k* = `../mc-nodek/`). `main` at `af8c59d6d61322853f5b456da2849890d5c790e7`. `papers/Main.md` is
  identical at both.
- **Node 8, context only** [rec, MC8 probe output r1 and the two reviews]. In the eight tested finite realizations every
  composite preparation is a mixture of allowed product preparations (the minimal tensor product). By the composition
  lemma, pure composites are products of pure states, and no mixed local state has a purification. The local marginals
  of budget-*m* composites are the budget-(*m*+1) local set. Enlarging that family cannot yield purification.
- **The node-8 assumption this node replaces.** Node 8 took preparations to be realization-datum priors with denominator
  ≤ 8, point masses included. Main.md:60 [corpus]: "a realization in the sense of §3.4 carries its own fixed hidden prior
  $\mu_H$ as part of the realization datum". One realization has one prior. Node 9 therefore fixes the prior of a
  realization, the counting measure of Lemma 3 (Main.md:56 [corpus]: "the counting measure is selected among invariant
  measures as the maximal-entropy one"), and generates every other preparation by allowed operations (§1.2). This
  reading is A-typed and is stated, not derived.
- **Node 6, context only** [rec, MC6 NODE.md:205–262]. P3: with exact parity obliviousness, preparation-noncontextual
  models reach POM success 3/4, computed by an exact LP. P4: a hidden-label model reaches 17/20, parity-oblivious on a
  selected readout set; Born weights coded into its table. P5: destructive complementary readouts on a classical two-bit
  ontology give (1 + *w*)/2 for a free prior weight *w*. Their contextuality needs a Y readout withheld that is a
  bijection on the same carrier (`c5y.py`). Under ε-agreement, PNC is vacuous (`leak.py`).
- **Drafting observations, disclosed because they shape the design; none is a verdict.**
  - Lemma F (§2.4): in a finite realization with a rational prior every outcome probability is rational, so no such
    realization attains (1+1/√2)/2 or 2√2 exactly.
  - For Option C of `NOTES.md` (a hidden direction under the counting measure), a triangle-inequality argument gives POM
    ≤ 3/4 in the continuum version [W, unreviewed].
  - For the default model of §4 (Option A), two things are already known or expected:
    - A hand argument suggests M1 holds at *n* = 2. The correlated record state is uniform on a coset of a Lagrangian
      subspace, and no preparable state has a support of two points, so it has no two-point preparable decomposition
      [W, unreviewed]. The literature expects the toy theory to satisfy purification [Q].
    - Its single system has a full-rank effect space (MC6 P2, rank 4/4 [rec]), so M3 is not expected to pass on it.
- Nothing else has been computed. `arxiv.org` and the journal sites were unreachable at drafting; no paper was read (§9).

***

## 1. Operational equivalence, the first definition

Declared once per model, printed with a digest before any computation (I-2). Every test reads this one relation:
purification, contextuality and Bell. **A preparation counts as the same state in one test only if it would count as
the same state in every test.**

### 1.1 The interface 𝓘 of a model

- **System boundary.** A system *S* is its visible cells V_S together with the hidden cells H_S assigned to it,
  including its record cells. Bath cells are hidden cells outside every system: each is fresh, used at most once, under
  the counting measure, and discarded after use.
- **Accessible records.** The configurations of visible cells, read by configuration readout (κ4). A readout does not
  change the ontic state.
- **Permitted operations.** Each one is a bijection of the realization's Ω:
  - permutations of visible cells, selectable by a setting;
  - the model's declared coupling steps, which may read or write hidden cells and may consume bath cells;
  - waiting, which applies φ;
  - feed-forward: the next operation may be any function of the records so far;
  - discarding a system;
  - composition, sequential and parallel, without a depth bound.

  Hidden cells change only through φ and the coupling steps (MC8 PREREG §2.2 option (B)).
- **Ancillas.** Independently supplied copies of any system type the model declares, in any preparable state (§1.2),
  with the model's joint operations. Equivalence is computed with *k* = 0, 1 and 2 ancillas (I-4).
- **Records left by preparation.** The model states, for each kind of hidden record, whether some coupling step reads
  it (flag R-yes or R-no). The flag belongs to the model and is fixed once. A test cannot choose it.
- **Composites.** Every declared joint operation of the model. Bell wings are restricted to local operations, and the
  model declares its Bell branch (M4).

### 1.2 Preparations are generated, never listed

The preparable set Prep(𝓘) is generated as follows. Start from the fixed prior: the counting measure on the hidden and
bath cells, with the visible cells at a point mass fixed by the protocol (condition O, MC7 PREREG §1). Prep(𝓘) is
everything reachable from it by deterministic protocols with feed-forward, followed by discarding. Mixtures arise
inside the same rule: a bath bit is read into a visible coin cell and steers the preparation. A budget of *m* coins
gives the weights *k*/2^*m*.

Heralded conditioning, keeping a run only for a given readout outcome, is computed as a separately labelled sensitivity
row and decides nothing. Preparations are not supplied as priors, and a test never adds one.

### 1.3 Equivalence, and how it is decided exactly

P ~ P′ iff every allowed experiment E gives identical outcome probabilities on P and on P′. E ranges over every
adaptive, finite-depth protocol of §1.1 on *S*, alone or with ancillas, and with any later intervention.

**Lemma W [W, pure mathematics].** Write F_S for the real functions on the configurations of *S*. An outcome branch of a
protocol has probability ⟨μ, f⟩, where μ is the preparation's distribution and *f* ∈ F_S is the branch function:
- the indicator of the branch, averaged over the bath cells consumed;
- on the protocol's other systems, which start in their fixed preparations.

Each primitive acts linearly on branch functions:
- an operation g gives T_g f = E_bath[f ∘ g];
- a readout of value v gives M_v f = 1[x = v] · f.

A branch function is a finite word in these operators applied to 1. So the span W(𝓘) of all branch functions is the
smallest subspace containing 1 and closed under every T_g and M_v. It is reached by iterating to a fixed point in at most
dim F_S rounds. Then **P ~ P′ iff μ_P − μ_P′ ⊥ W(𝓘)**. With ancillas, the condition is ⊥ W of the composite, tested
against a spanning set of Prep(ancilla).

The lemma decides equivalence over unbounded depth exactly. It replaces node 8's depth-≤2 enumeration (MC8 review F6).
Arithmetic is rational throughout.

### 1.4 History is not contextuality

Two preparations that leave different hidden records fall into exactly one of two cases:
- (a) they are **different operational states**, because some allowed experiment separates their statistics; this is
  the case when the record is response-relevant and reachable;
- (b) they are **operationally equivalent**, because no allowed experiment separates them. In case (b) the existence of
  the records establishes nothing.

Contextuality is decided only by M3's computed inequality. The countercontrols K-HL0 and K-HL1 (§5) must fail every
contextuality milestone. K-HL0 is a classical model with a preparation label that no allowed experiment reads. K-HL1
is the same model with the label readable.

### 1.5 Purity

A preparable state ψ is **pure** iff there are no two inequivalent preparable states ρ₁ ≁ ρ₂ and no generated weight *w*
∈ (0, 1) with ψ ~ *w*ρ₁ + (1 − *w*)ρ₂. Purity is never judged by the underlying ontic distribution. A state whose
ontic support has several points can be pure, and a point mass can be mixed only if it is equivalent to such a mixture.
Following MC8 A-1, three readings are reported separately:
- at the declared budget;
- across the model, as the union over budgets up to the stated cap;
- on the convex closure, where pure means extreme.

***

## 2. Admissibility rules for a candidate (§A.29)

### 2.1 One physically specified model, fixed before computing

A candidate model fixes every item below in the frozen text:
- its cells (visible, record, bath) and its φ;
- its coupling steps and its joint operations;
- what the observer can and cannot do;
- its ancilla types and its R-flags;
- its Bell branch;
- the principle Π from which the operation set is derived (§2.2).

The first computation is the smallest realization in which the candidate condition acts: for C5-P, one system with a
purifier of the same type.

### 2.2 R-MENU: the restriction is a principle, not a menu

A restriction counts only if it is stated as a physical or operational principle Π and the model's operations are
*derived* from Π. They are never listed by hand. The check computes Ops(Π) mechanically, as every bijection of the
declared carrier that satisfies Π. It then checks four things:
- (i) **closure**: Ops(Π) is closed under composition, under waiting (φ), under adjoining any declared ancilla (an
  operation on one factor with the identity on the other satisfies Π), and under composites of every declared size;
- (ii) **maximality**: the model withholds no bijection that satisfies Π;
- (iii) **generated preparations**: §1.2 holds;
- (iv) **invariance**: replacing the model's operation list by Ops(Π) changes no milestone output.

A milestone pass whose model fails R-MENU is printed "pass for the declared operation set; R-MENU fails at (i)–(iv)".
It does not count toward the governing question. K-MENU (§5) must fail (ii).

### 2.3 Preserved results (controls fixed in advance) and the beyond-target prediction

The candidate must reproduce each of the following, or the run halts:
- **node 8's eight answers.** Pur-E and Pur-U at budget *m* = 3 for ℛ₁ᵃ, ℛ₁ᵇ, ℛ₂ᵃ (1- and 2-bit observer), ℛ₂ᵇ (1- and
  2-bit observer), K-SWAP and CL-C4 [rec, MC8 `p8s1.r1.run1.out`]. These are recomputed with node 9's equivalence engine
  under node 8's own preparation menu, and agreement is required (K-N8). This controls the engine. It does not say
  that those classes satisfy §1.2;
- **condition O** for the model (MC7 PREREG §1);
- **the Bell-local ceiling.** In any composite of the local branch, where Main.md:361–365's hypotheses (i)–(iv) hold, the
  model must give |S_CHSH| ≤ 2 exactly (K-BL). Main.md:82 [corpus]: "for a response-complete deterministic completion,
  measurement independence plus ontic parameter independence would force $|S_{\rm CHSH}|\le2$";
- **operational no-signalling** on the wing records of every composite (Main.md:407 [corpus]: "a later local setting
  cannot produce an operational signal at the remote wing").

C1, C3 and C4 are measured as in MC8 step 1, and **C2-structural** by the operational check of §2.5. Each is reported,
and none is an admission criterion. A model said to satisfy C*i* must pass that measurement.

**Beyond-target prediction.** The frozen model states at least one statistic, outside the M1–M5 targets, that it
predicts before computation, with its decision rule. Under §A.24, a raw-direct conflict with experiment is reported as a
miss. A model whose free parameters can be set to fit any outcome of its milestones is rejected, by MC6's N3 pattern.

### 2.4 Lemmas fixed in advance (pure mathematics; reported as consequences, never as findings)

- **Lemma F (field) [W].** In a finite realization whose prior is rational (the counting measure included), every
  outcome probability is μ of a finite set, and so rational. Hence no experiment attains (2+√2)/4 or 2√2 exactly. M5's
  exact attainment question (M5-A) is therefore decided negative for every such model. Only its A2 form, a limit along
  a declared family, is open.
- **Lemma A** [rec, MC8 PREREG §6.1] is applied where its hypotheses are checked: full access with full preparations
  gives classical probability.
- **The composition lemma** [rec, MC8 A-3 F1]. If every composite preparation is a mixture of product preparations, pure
  composites are products of pure states.

### 2.5 Operational C2 check (preregistered, as MC8 A-3 required)

Main.md:76 [corpus] defines C2-structural: "a hidden record of visible history, once written, persists to the readback
that uses it".

The check, for each declared record cell set R and each protocol of depth ≤ 4: after the step that writes the visible
history into R, take every subsequent step up to the first readback that reads R, provided no coupling step on R
intervenes. At each such step the mutual information between that visible history and R must equal its value just after
writing, computed exactly.

C2 holds on the model iff the equality holds for some memory witness of C4. Bijectivity of a step alone is not evidence
of C2 (MC8 A-3).

***

## 3. Milestones: each its own question, rule and status, never merged

Statuses are PASS, FAIL, PARKED (with the gap named), or VOID (a governing control is red). Each milestone prints its
own block. No milestone status is inferred from another. A PASS is recorded only for the model computed, at the stated
sizes.

**M1. An operationally pure composite with a mixed marginal.**
- *Question:* is there a composite AB of the model and a pure ψ ∈ Prep(AB) (§1.5) whose A-marginal is not pure?
- *Rule:* PASS iff an exact witness is found, with ψ's purity certified over all of Prep(AB) at the declared budget and
  across the model. FAIL iff exhaustive enumeration of Prep(AB) at the declared sizes finds no witness. PARKED if the
  enumeration exceeds §8's bound.
- *Establishes:* the model escapes the node-8 composition obstruction at that size.
- *Does not establish:* purification for every state, uniqueness, contextuality, Bell violation, or QM. Spekkens' toy
  theory and boxworld are expected by [Q] literature to pass M1. They are controls (§5).

**M2. Purification for every state, with essential uniqueness (C5-P for the specified model).**
- *Question:* for every preparable state ρ of A, A ∈ {one system, two systems} with a purifier B of the same type, two
  clauses must hold:
  - **Pur-E**: some pure ψ ∈ Prep(AB) has A-marginal ~ ρ;
  - **Pur-U**: any two such ψ, ψ′ satisfy (id_A ⊗ U_B)ψ ~ ψ′ for some reversible U_B ∈ Ops(Π) acting on B alone.
- *Rule:* Pur-E and Pur-U are separate lines in the MC8 r1 form: counts generated from the purification table;
  unconnected pairs named; an undecided status distinct from failure (MC8 review N2); and a Pur-U countercontrol (N1).
  Three readings are reported separately (§1.5). M2 is PASS iff both lines hold on the declared readings for both sizes
  of A. Larger A is PARKED unless a reviewed [W] covers it.
- *Wording gate:* the verdict text is provisional pending PC-CDP (§9).
- *Establishes:* C5-P for this model at those sizes.
- *Does not establish:* QM or the other CDP axioms. A pass on the preparable set does not establish a pass on the
  convex closure, where Lemma K (MC8 §6.1) applies.

**M3. A preparation-contextuality witness (two-bit parity-oblivious multiplexing).**
- *Task:* the sender receives uniform (b₀, b₁) and prepares P_b ∈ Prep(S). The receiver receives a uniform y ∈ {0, 1}
  and guesses b_y by a binary-outcome allowed experiment D_y. Success = ¼ Σ_b ½ Σ_y Pr(guess = b_y | P_b, D_y).
- *Parity obliviousness:* ½(P₀₀ + P₁₁) ~ ½(P₀₁ + P₁₀) under §1.3. This is checked over **all** allowed experiments
  through W(𝓘), at *k* = 0, 1 and 2 ancillas. Agreement on a selected readout set is never sufficient.
- *Threshold:* the preparation-noncontextual bound is 3/4 [Q: Spekkens et al. 2009]. It is recomputed in house by K-PNC.
- *Rule:* PASS iff exact preparable P_b and realizable D_y satisfy exact parity obliviousness and success > 3/4, with
  both properties following from the model's dynamics and interface. FAIL iff the exhaustive maximum is ≤ 3/4 over
  Prep(S) at the budget and over decoders of depth ≤ D. That maximum must be stable from D to D + 1, and a universal
  claim needs a reviewed [W]. PARKED otherwise.
- *Additional output:* a PASS also prints the success value against (2+√2)/4 in ℚ(√2): below, equal, or above.
- *Establishes:* the model's operational theory is preparation contextual.
- *Does not establish:* C5-P, QM, or the quantum magnitude. A gbit-type model passes M3 with success 1 (K-MENU).

**M4. Bell violation under declared assumptions.**
- *Branch:* the composite declares its Bell branch from Main.md §3.3 [corpus, Main.md:392]. Branch (a), "one wing's
  response depends on the remote setting", or the local branch (hypotheses (i)–(iv) of Main.md:361–365).
- *Question:* is there a composite preparation and local settings with |S_CHSH| > 2, computed exactly in ℚ(√2), with
  operational no-signalling verified exactly on the wing records?
- *Rule:* PASS iff such a witness exists and no-signalling holds. FAIL iff the exhaustive maximum is ≤ 2. In the local
  branch, a value above 2 voids the run (K-BL).
- *Establishes:* a Bell violation in the declared branch.
- *Does not establish:* QM. A PR-capable realization passes M4 with S = 4 and must be detected as exceeding 2√2
  (K-PR6, §5).

**M5. Quantum limits and quantum attainability, as two questions (§A.34).**
- *M5-L, limit:* over the model's allowed experiments at the computed sizes, is POM success ≤ (2+√2)/4 and |S_CHSH| ≤
  2√2? PASS iff both hold, exactly. FAIL iff an exact violator is found. Universal claims need a reviewed [W].
- *M5-A, attainment:* does the model attain (2+√2)/4 and 2√2 with parity obliviousness and no-signalling exactly
  (A1)? Under Lemma F the answer is no for every finite rational model, and this is printed as the lemma's consequence.
  The A2 form, a limit along a declared family of models, is a separate line. It is PASS only with an exact sequence and
  a reviewed [W] limit.
- Neither direction is inferred from the other. A PASS on M5-L for a model that never leaves the classical bounds
  (POM ≤ 3/4, |S| ≤ 2) is printed "vacuous". M5 together with M1–M4 does not establish QM. It bounds two statistics.

***

## 4. The first candidate model: owner's choice required before freeze

**Proposed default (Option A in `NOTES.md`; pending owner choice, Q1): the boundary toy bit, under principle Π_BA.**
- *System T.* A visible pointer x ∈ {0, 1}, initially 0, and record cells h ∈ ℤ₂²; for *n* systems, h ∈ ℤ₂^{2n} with the
  standard symplectic form ω. φ = identity. Bath bits follow the counting measure; the fixed prior on h is uniform.
- *Principle Π_BA (symplectic back-action) [A-typed].* A coupling step that makes the record functional ω(u, ·)
  readable writes it into a pointer and shifts the record along u by a fresh bath bit. In symbols, R_u is x ^= ω(u, h),
  then h ^= r·u. A coupling step that reads nothing is a record bijection that maps the readable functionals onto
  themselves. Read physically: the pointer's conjugate variable is hidden, so reading a record kicks the record's
  conjugate content.
- *Derived operations.* Ops(Π_BA) are computed mechanically under R-MENU (ii); the affine symplectic maps are expected
  but are not assumed. Joint readouts of ω(u, ·) with u ∈ ℤ₂^{2n} are the joint operations.
- *R-flag:* R-yes. Every record functional is reachable by some R_u. Bell branch: local.
- *Smallest realization for C5-P:* *n* = 2 (A = one toy bit, B = one toy bit). Sizes computed: *n* ≤ 4.
- *Beyond-target prediction:* to be stated by the owner at freeze (`NOTES.md` Q1 lists the candidates). Prerecorded
  here: in its local branch the model predicts |S_CHSH| ≤ 2 for every composite, a raw-direct conflict with
  loophole-free Bell tests [Q]. The model is a step toward the question, not a candidate theory of nature.

If the owner chooses Option B or C, this section is replaced by that option's specification at the same level of
detail before freeze.

***

## 5. Controls (each computed exactly; roles explicit; a red control voids its milestone)

| id | role | construction | must |
|---|---|---|---|
| K-QPOM | positive (M3, M5) | qubit: ρ_b = ½(I + ((−1)^{b₁}X + (−1)^{b₀}Z)/√2); D₀ = Z, D₁ = X | ½(ρ₀₀+ρ₁₁) = ½(ρ₀₁+ρ₁₀) = I/2 as matrices, which is the complete invariant for every POVM, ancilla and composite; success = (2+√2)/4 exactly in ℚ(√2) |
| K-PNC | calibration (threshold) | exact LP over ontological models on the four response pairs with every deterministic response function, PNC imposed (MC6 P3 recomputed) | maximum exactly 3/4; without parity obliviousness, 1 |
| K-CBIT | countercontrol (M3) | classical bit, full access | maximum POM success with exact parity obliviousness = 3/4, attained by m = b₀ |
| K-HL0 | countercontrol (M1, M3; §1.4 case b) | classical bit plus a hidden preparation label that no allowed experiment reads (R-no, response-irrelevant) | preparations differing only in the label are equivalent; POM ≤ 3/4; M1 and M3 FAIL |
| K-HL1 | countercontrol (§1.4 case a) | K-HL0 with a coupling step that reads the label | label-different preparations inequivalent; every encoding with label = b breaks parity obliviousness; M3 FAIL |
| K-SPK | calibration (M1, M2, M3) | Spekkens toy bit, original form (MC8 PREREG §6.5 reading; 6 + 1 states; 60/30/1 for two) | M3: POM ≤ 3/4, verified by computing W's rank and the maximum, not assumed; M1 and M2 outputs printed against MC8's poscontrol |
| K-MENU | countercontrol (R-MENU, M5-L) | MC6 P5: destructive complementary readouts on ℤ₂², Y withheld, generated preparations; and its *w* = 1 member (the gbit) | passes M3 for its declared set; R-MENU (ii) fails, naming the withheld Y readout; at *w* = 1, M5-L FAIL (POM = 1 > (2+√2)/4) |
| K-PR6 | countercontrol (M4, M5-L) | MC7 LE(1,1) / MC6 B2 [rec]: A = λ, B = λ ⊕ ab | M4 PASS with S = 4 and no-signalling; M5-L FAIL |
| K-BL | preserved result | every local-branch composite of the model | |S| ≤ 2 exactly; otherwise the run is VOID |
| K-CL | countercontrol (M1, M2) | classical bit pair, full access | M1 FAIL; Pur-E fails for every mixed state |
| K-QSTAB | positive (M1, M2) | MC8 §6.5's stabilizer instance (7 one-qubit and 91 two-qubit states, ℚ(i, √2)) | M1 PASS; Pur-E and Pur-U hold for A = one qubit |
| K-N8 | preserved result (engine) | node 8's eight classes under node 8's menu | the eight Pur-E/Pur-U answers reproduced |
| K-ANC | engine | equivalence at *k* = 0, 1, 2 ancillas | any change from *k* = 1 to *k* = 2 halts (Parked, gap named) |

A control result that merely reproduces the formula it is meant to check is vacuous. K-QPOM computes the density
matrices from ρ_b, not from the success formula; K-PNC's LP is solved, not the value inserted.

***

## 6. Productivity test (§A.31), fixed before execution

**Baseline.** The following are restatements and do not count:
- node 8's composition lemma and eight answers;
- MC6 P3–P5 and N1–N5;
- MC7's verdicts;
- Lemma F, Lemma A and Lemma K;
- appendix-c:232 [corpus]: "restricted access does not by itself single out quantum theory";
- Main.md:550 [corpus], which disclaims Spekkens noncontextuality ("not Spekkens noncontextuality, which concerns
  operationally equivalent procedures and is not claimed");
- every [Q] literature statement.

**The node is a gem iff at least one of the following holds:**
- (a) M1 or M2 reaches PASS on a model with R-MENU green, and the pass is traced to a named, stated principle. This
  constrains the form of the missing component beyond node 8;
- (b) M1 or M2 reaches FAIL on an R-MENU-green model, with the named interface property that blocks it, and that
  property is not the node-8 menu or Lemma A;
- (c) M3 reaches PASS on an R-MENU-green model;
- (d) R-MENU fails for a candidate whose principle was stated in advance, and the computation names the operation that
  breaks it. This exposes a hidden assumption. It is recorded as an assumption-watch marker for later nodes.

Anything else is a non-gem (record-only). A favourable branch, any PASS, gets the skeptical pressure test of §A.31
before it is recorded: the controls are rerun with the decisive object perturbed. Output classes are NEW, POSITIVE,
ELABORATING, CONFIRMING or BORDERLINE.

***

## 7. Invariant→checkpoint table (§A.41)

| # | invariant | checkpoint |
|---|---|---|
| I-1 | this file preceded every computation and is unchanged | sha256 recorded at freeze, printed first by the probe; amendments under `amendments/` with time, reason and state of knowledge, before the computation they touch |
| I-2 | the interface and model are fixed before computing | 𝓘, Π, Ops(Π), R-flags and Bell branch printed with digest before any milestone; every milestone line cites the digest |
| I-3 | one equivalence relation for every test | a single function computes ~ from W(𝓘); a static scan refuses any other equivalence code path; mutant KM-1 |
| I-4 | equivalence covers ancillas | K-ANC at *k* = 0, 1, 2; KM-2 |
| I-5 | Lemma W's closure is complete | fixed-point iteration logged with its dimension per round; cross-check against explicit enumeration to depth 4 on K-SPK and K-HL0 (spans equal); KM-3 |
| I-6 | preparations generated, never listed | Prep(𝓘) built only by the §1.2 generator; a static scan refuses a literal state list outside controls; KM-4 |
| I-7 | purity by preparable decomposition | §1.5's three readings printed separately; MC8 A-2's KM-32 fixture rerun; KM-5 |
| I-8 | parity obliviousness over all experiments | M3's check calls I-3's relation; KM-6 replaces it by a fixed readout set, and K-MENU's Y readout must then pass falsely and be caught |
| I-9 | exactness | `Fraction` and sympy ℚ(√2) only; an AST scan for floats on the verdict path; a missing dependency fails, never skips |
| I-10 | verdicts only over green controls | each milestone block is gated on its controls (§5); a red control prints VOID; KM-7 |
| I-11 | milestones never merged | separate generated blocks; a static check that no milestone reads another's status; KM-8 |
| I-12 | verdict text generated from measurements | every count and status is computed; scanned against MC8 A-1's word list (extended: "theorem", "impossible", "no-go", "universal", "for every realization"); KM-9 |
| I-13 | R-MENU is computed | Ops(Π) enumerated from Π's predicate; K-MENU must fail (ii); KM-10 |
| I-14 | preserved results hold | K-N8, K-BL, condition O, no-signalling, the C2 check printed before milestones |
| I-15 | determinism | two runs byte-identical; `SHA256SUMS`; no randomness |
| I-16 | resource bound | wall time printed per phase; §8's limits |
| I-17 | literature never decides | each line lists its [Q] dependencies; a line depending on an unmet PC gate prints "provisional" |

**Mutation plan.** Each mutant runs on a scratch copy and must be caught by the named check, which then prints FAIL and
suppresses the governed lines:
- KM-1: the POM test computes equivalence on single readouts only;
- KM-2: *k* = 0 only;
- KM-3: the closure stops after one round;
- KM-4: a point mass is added to Prep;
- KM-5: purity by real convex combination;
- KM-6: parity obliviousness on a fixed readout list;
- KM-7: K-QPOM forced red;
- KM-8: M2 inherits M1's status;
- KM-9: a hard-coded "holds";
- KM-10: Ops(Π) replaced by the hand list without Y;
- KM-11: the Pur-U status forced to "holds" (MC8 review N1's mutant M6 must now be killed);
- KM-12: a float enters the success computation.

***

## 8. Order, resources and replay

**Order (depth-first, §A.12):**
1. the engine and the controls: K-PNC, K-QPOM, K-CBIT, K-HL0, K-HL1, K-SPK, K-CL, K-QSTAB, K-N8, K-ANC, K-MENU, K-PR6;
2. the model's interface printout and R-MENU;
3. M1, then M2 at *n* = 2;
4. M3;
5. M4;
6. M5;
7. M2 at the larger sizes;
8. the mutants;
9. productivity and the independent review.

A FAIL at M1 does not stop M3 or M4, since they are separate questions. Each milestone is reported.

**Resources (§A.40).** The local run must stay under about 60 minutes. Each phase prints its wall time and halts
reporting its completed range if it exceeds its share. Anything larger, such as *n* = 4 enumerations or deeper decoder
stability, becomes a CI plan proposed on the guiding PR and runs only with owner approval.

**Replay.** Two runs from a clean checkout of the frozen commit must be byte-identical. `SHA256SUMS` covers the probe and
both outputs, and a reviewer replays with `python3 -I -B`.

***

## 9. Literature: narrow claims and gates

Nothing was read. WebFetch and the proxy could not reach arXiv or the APS journals. Web searches returned bibliographic
summaries only. Every entry is therefore [Q].

| source | claim used here | status | gate |
|---|---|---|---|
| Spekkens, Buzacott, Keehn, Toner, Pryde, PRL 102, 010401 (2009), arXiv:0805.1463 | the two-bit POM task; with exact parity obliviousness, PNC success ≤ 3/4; quantum (1+1/√2)/2 | [Q] (search summary confirms title, authors and venue; values not seen) | PC-POM: an amendment quoting the task definition, the PNC bound and the quantum value. The numbers that decide M3 come from K-PNC and K-QPOM, so only the attribution waits |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | preparation-noncontextual ontological models of quantum theory do not exist, a proof that applies already in dimension 2 | [Q] (abstract-level search summary) | PC-S05 before any verdict text cites it |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | the toy theory; knowledge balance | [Q] | K-SPK is built from MC8's combinatorial reading; PC-SPK as in MC8 |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | Gaussian QM reconstructed from one specific epistemic restriction on Liouville mechanics | [Q] (search summary) | PC-BRS |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | five axioms (causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning) plus purification select QM | [Q] (search summary lists the axioms) | PC-CDP (inherited from MC8 §6.8) gates M2's wording |

**Narrow claims, and only these.**
- Bartlett, Rudolph and Spekkens (2012) reconstruct Gaussian QM from one specific epistemic restriction on Liouville
  mechanics.
- Spekkens (2005) excludes preparation-noncontextual models of full QM.

Together these constrain the route. They do not rule out contextual, epistemically restricted constructions. Nothing
here states that epistemic restrictions in general stop at stabilizer or Gaussian physics.

***

## 10. Scope

Every negative result concerns the specified model, its interface 𝓘, the sizes computed and the declared readings. A
FAIL does not establish that observational incompleteness cannot yield purification, contextuality, Bell violation or
QM. A PASS establishes the milestone's stated content for that model, and nothing beyond it. Finite-model success is
never classified as an exact quantum reconstruction (MC8 A-1). No equivalence is claimed. M5's two directions are
reported separately.

***

## 11. Procedure and freeze

- **Before freeze:**
  - the owner chooses the model (§4) and its beyond-target prediction;
  - the open questions of `NOTES.md` are disposed;
  - an independent pre-freeze review runs.
- **Freeze:** the sha256 of this file is recorded in the commit message and on the guiding PR. After freeze the file is
  not edited. Changes go to `amendments/` with time, reason and state of knowledge, before the computation they touch.
  No amendment changes a decision rule in a candidate's favour.
- **After a milestone's first computation:** its rules are frozen. A later discrepancy is recorded, not repaired.
