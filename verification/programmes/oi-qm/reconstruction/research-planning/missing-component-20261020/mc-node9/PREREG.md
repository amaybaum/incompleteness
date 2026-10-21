# Node 9: which OI condition yields operational structure beyond the minimal tensor product? Preregistration

**DRAFT — NOT FROZEN; no computation may run against this draft.**

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. Freeze
requires the items of §11 and the sha256 of the frozen bytes recorded before any computation. The decision rules are
fixed here; expected numbers are not (§A.29). Revision 2 of the draft.

**Governing question (owner, 2026-10-21).** Which independently motivated OI condition, stated in OI's own terms
(visible and hidden cells, φ, coupling steps, ancillas, records), yields operational structure beyond the minimal tensor
product, and specifically C5-P, operational purification with essential uniqueness? C5-P is the primary target. C2
(persistence of hidden records) is admitted as a possible implementation mechanism. It is not a substitute for
demonstrating purification or contextuality.

**Owner decisions (2026-10-21).**
- **Q1.** Option A (the boundary toy bit under symplectic back-action, §4) is the first model. Option B follows on the
  same engine; Option C is a side calibration (`NOTES.md`).
- **Q2.** The three-way hidden-label control is accepted: K-HL0, K-HL1, K-MENU (§5), with the premise check of §1.4 in
  K-HL1.
- **Q3.** The hidden prior is fixed within a realization. The model starts from the counting measure and generates every
  other preparation operationally (§1.2). This is a model choice: Main.md:60 makes the fixed prior a realization datum
  and the counting measure the default, and permits structured preparations (§0).
- **Q4.** Heralded conditioning is a generator from the start (§1.2), not a sensitivity row.

**Tags.** [corpus] text quoted verbatim from the corpus at the base, with file:line; [rec] stated in a thread record, not
re-derived; [rec, owner …] a check or reading supplied by the owner, not re-derived in this session; [W] written
argument, to be reviewed; [EC] exact computation (none run); [lit-read] literature read in full and the claim verified
against the text; [Q] literature not read, whether recalled or known only from a search summary; [rec, coordinator
check 2026-10-21] verified in this session by the exact check stated (script and output kept off-repo as provenance).
No claim tagged [Q] decides a verdict (§9).

***

## 0. Base and state of knowledge

- Thread `research/missing-component-20261020`; revision 2 drafted at `c81f2df4c174bd305e496d01e7e83429479765bc`,
  whose node-8 records are those of the close-out `789134678aac771466f4443f8d053bdf084a5b18` with amendment A-5 (PLAN =
  `../PLAN.md`, MC*k* = `../mc-nodek/`). `main` at `af8c59d6d61322853f5b456da2849890d5c790e7`. `papers/Main.md` is
  identical at both.
- **Node 8, context only** [rec, MC8 probe outputs r1 and r2, `probe/CHANGES-r2.md`, and the reviews]. In the eight
  tested finite realizations every composite preparation is a mixture of allowed product preparations (the minimal
  tensor product). By the composition lemma (budget *m* ≥ 1, MC8 A-5), pure composites are products of pure states, and
  no mixed local state has a purification. The local marginals of budget-*m* composites are the budget-(*m*+1) local
  set; enlarging that family cannot yield purification. The Pur-E and Pur-U answers are identical in r1 and r2.
- **The node-8 assumption this node replaces.** Node 8 took preparations to be realization-datum priors with denominator
  ≤ 8, point masses included. Main.md:60 [corpus]: "a realization in the sense of §3.4 carries its own fixed hidden
  prior $\mu_H$ as part of the realization datum", and "the counting measure is the default, not a constraint on
  representations"; the same remark states that Lemma 3 "does not preclude structured preparations". Main.md:56
  [corpus]: "the counting measure is selected among invariant measures as the maximal-entropy one". Node 9 fixes the
  prior of a realization to the counting measure and generates every other preparation by allowed operations (§1.2), a
  model choice (Q3).
- **Node 6, context only** [rec, MC6 NODE.md:205–262]. P3: with exact parity obliviousness, preparation-noncontextual
  models reach POM success 3/4, computed by an exact LP. P4: a hidden-label model reaches 17/20, parity-oblivious on a
  selected readout set; Born weights coded into its table. P5: destructive complementary readouts on a classical two-bit
  ontology give (1 + *w*)/2 for a free prior weight *w*. Their contextuality needs a Y readout withheld that is a
  bijection on the same carrier (`c5y.py`). Under ε-agreement, PNC is vacuous (`leak.py`).
- **Calibration readings on the Spekkens toy bit** [rec, review of 390e252f and owner check]. (i) The seven-state
  single-toy-bit menu with the tested one-toy-bit partner: every state has a purification. (ii) Its convex closure,
  against the tested pure joint states: some mixed states have no purification. Each reading holds for its stated
  preparation set and purifying system only.
- **Drafting observations, disclosed because they shape the design; none is a verdict.**
  - For Option C (`NOTES.md`), a triangle-inequality argument gives POM ≤ 3/4 in the continuum version [W, unreviewed].
  - For Option A [W, unreviewed]: the correlated record state at *n* = 2 is uniform on a coset of a Lagrangian subspace
    and has no two-point preparable decomposition, for the tested partner and provided the restriction survives the
    closure (M0, §4.1; under ρ₀ it does not, K-SYMP). Its single system has a full-rank effect space (MC6 P2, rank 4/4
    [rec]).
- Nothing else has been computed beyond the checks tagged [rec, coordinator check 2026-10-21]. No paper was read in
  this session (§9).

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
- **Permitted operations.** Each one is a bijection of the realization's Ω, or a selection on a record (heralding):
  - permutations of visible cells, selectable by a setting;
  - the model's declared coupling steps, which may read or write hidden cells and may consume bath cells;
  - waiting, which applies φ;
  - feedback and feed-forward: the next operation may be any function of the records so far;
  - discarding a system;
  - heralded conditioning (§1.2);
  - composition, sequential and parallel, without a depth bound.

  Hidden cells change only through φ and the coupling steps (MC8 PREREG §2.2 option (B)).
- **Clean ancillas.** The model declares every clean ancilla, a cell or system supplied in a declared initial state
  other than the counting measure (a visible pointer at 0, a known-zero bit), and states that declaration as a physical
  principle (R-MENU (v)). Visible cells fixed by the protocol (condition O) are clean ancillas and are declared as such.
- **Ancillas.** Independently supplied copies of any system type the model declares, in any preparable state (§1.2),
  with the model's joint operations. Equivalence is computed with *k* = 0, 1 and 2 ancillas (I-4).
- **Records left by preparation.** The model states, for each kind of hidden record, whether some coupling step reads
  it (flag R-yes or R-no). The flag belongs to the model and is fixed once. A test cannot choose it.
- **Composites.** Every declared joint operation of the model. Bell wings are restricted to local operations, and the
  model declares its Bell branch (M4).

### 1.2 Preparations are generated, never listed

Whether a fixed prior keeps hidden point masses out of the preparable set depends on the operations, the dynamics and
the ancillary resources, not on the partition alone. **Example** [rec, owner check 2026-10-21]: a fair hidden bit
becomes a definite 0 after an allowed swap with a known-zero ancilla bit, with no postselection.

Prep(𝓘) is therefore the closure of the fixed prior (the counting measure on the hidden and bath cells, the declared
clean ancillas in their declared states) under every generator:
- (g1) adjoining any declared clean ancilla in its declared state;
- (g2) every coupling step and every permitted visible permutation;
- (g3) feedback and feed-forward on the records so far;
- (g4) waiting under φ;
- (g5) discarding;
- (g6) heralded conditioning with back-action.

Mixtures arise inside the same rule: a bath bit is read into a visible coin cell and steers the preparation. A budget of
*m* coins gives the weights *k*/2^*m*. Preparations are not supplied as priors, and a test never adds one.

**Heralding (g6).** Selection is allowed on every physically recorded outcome of nonzero probability. The record keeps
that outcome's success probability and the actual post-measurement state: the full coupling step, back-action included,
is applied to the joint distribution, which is then conditioned on the recorded value. The state is never inferred from
what the record reveals about the earlier hidden value. Required control K-HERALD [rec, owner check 2026-10-21]:
- a read that leaves h unchanged: conditioning on outcome b gives h = b definitely;
- a read that copies h and then replaces it with an independent fair bit: conditioning on b leaves h uniform.

Both reads reveal the previous h; only the first prepares a definite current h. A restriction that survived only
because ordinary heralding is excluded would establish a narrower theory, which is why (g6) is a generator.

**Reachability is not equivalence.** Lemma W (§1.3) decides equivalence within the declared model; it does not make
Prep(𝓘) finite. K-REACH [rec, owner check 2026-10-21]: two states, fair prior; an operation reports "success" with
probability 1 in state 0 and ½ in state 1, leaving the state unchanged. Retaining *k* successes gives P(0 | *k*) =
2^*k*/(2^*k* + 1) = ½, 2/3, 4/5, 8/9, …, infinitely many preparations, while W has full dimension 2 after one expansion.
This applies whenever fresh randomness or ancillas come without a fixed total budget. Three layers are decided
separately, each at its own checkpoint (§7):
1. **equivalence**, by Lemma W within the declared model (I-5);
2. **preparation reachability**, at a stated resource scope (*n*, *k*, a budget b_r on fresh bath bits and b_h on
   heralding repetitions), by a termination proof or a mathematical characterization of Prep at that scope; otherwise
   the result is PARKED (I-20);
3. **purity and purification**, evaluated on the resulting preparation set with its resource limits and any completion
   stated (I-7).

### 1.3 Equivalence, and how it is decided exactly

P ~ P′ iff every allowed experiment E gives identical outcome probabilities on P and on P′. E ranges over every
adaptive, finite-depth protocol of §1.1 on *S*, alone or with ancillas, and with any later intervention.

**Lemma W [W, pure mathematics].** Let Ω be the declared finite state space of the model, of size *N*, including its
declared ancillas and pointers. Distributions are column vectors *p*. Each action *a* with outcome *o* is represented by
an unnormalized transition matrix T_{a,o} ≥ 0 on Ω (consumed bath cells averaged in), with Σ_o T_{a,o} stochastic.
The outcome sequence (a₁,o₁), …, (a_k,o_k) has probability 1ᵀ T_{a_k,o_k} ⋯ T_{a₁,o₁} *p*.
- *Iteration.* W₀ = span{1ᵀ}, W_{j+1} = span(W_j ∪ {w T_{a,o} : w ∈ W_j, all a, o}). By induction W_j is the span of the
  functionals of all sequences of length ≤ *j*. The chain W₀ ⊆ W₁ ⊆ … lies in ℝ^N, so its dimension stabilizes; once
  W_{j+1} = W_j every later term equals W_j. Starting from dimension 1, it stabilizes after at most *N* − 1 strict steps.
  The stable space W contains the probability functional of every finite outcome sequence.
- *Adaptive protocols.* Each completed branch of an adaptive protocol specifies one finite action-and-outcome sequence,
  and every outcome event is a finite sum of branches, so its probability functional lies in W.
- *(⇐)* If W annihilates *p* − *p*′, every sequence functional, and hence every protocol's statistics, agrees on P and P′.
- *(⇒)* If some w ∈ W does not annihilate *p* − *p*′, some spanning sequence functional separates them, and the
  non-adaptive protocol that runs that sequence is an allowed experiment. So **P ~ P′ iff W(𝓘)(*p* − *p*′) = 0**.

With *k* ancillas the condition is W of the composite applied to (*p* − *p*′) ⊗ *q*, for *q* over a spanning set of
Prep(ancilla^*k*). Arithmetic is rational throughout. The lemma replaces node 8's depth-≤2 enumeration (MC8 review F6).

*Scope.* The lemma covers arbitrary depth within the declared finite model, its declared ancillas included. It decides
equivalence only, not which preparations are reachable (§1.2, K-REACH). It does not cover arbitrarily large ancillas,
new couplings, or apparatus memory that Ω does not represent. K-ANC (*k* = 1 vs 2) is the extension checkpoint: a
result computed at *k* ancillas is reported for *k* ancillas only. Passing selected ancilla controls is evidence for
those extensions only; stability under arbitrary ancillary systems needs a proof, given and reviewed.

### 1.4 History is not contextuality

Two preparations that leave different hidden records fall into exactly one of two cases:
- (a) they are **different operational states**, because some allowed experiment separates their statistics; this is
  the case when the record is response-relevant and reachable;
- (b) they are **operationally equivalent**, because no allowed experiment separates them. In case (b) the existence of
  the records establishes nothing.

Contextuality is decided only by M3's computed inequality. K-HL0 is a classical model with a preparation label that no
allowed experiment reads; K-HL1 is the same model with the label readable. **Premise check.** In every POM computation,
and in K-HL1 in particular, parity obliviousness is checked first through §1.3. If an allowed experiment (reading the
label included) separates the two parity mixtures, the POM premise fails: the score is printed "POM premise not met" and
is not compared with 3/4.

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
- its clean ancillas with their initial states, its ancilla types and its R-flags;
- its Bell branch;
- the principle Π from which the operation set is derived (§2.2).

The first model computation is the decisive closure question (§4.1); then the smallest realization in which the
candidate condition acts: for C5-P, one system with a purifier of the same type.

### 2.2 R-MENU: the restriction is a principle, not a menu

A restriction counts only if it is stated as a physical or operational principle Π and the model's operations are
*derived* from Π. They are never listed by hand. The check computes Ops(Π) mechanically, as every bijection of the
declared carrier that satisfies Π. It then checks five things:
- (i) **closure**: Ops(Π) is closed under composition, under waiting (φ), under adjoining any declared ancilla (an
  operation on one factor with the identity on the other satisfies Π), and under composites of every declared size;
- (ii) **maximality**: the model withholds no bijection that satisfies Π;
- (iii) **generated preparations**: §1.2 holds with all of (g1)–(g6), and the restriction Π asserts on preparations
  survives that closure (§4.1);
- (iv) **invariance**: replacing the model's operation list by Ops(Π) changes no milestone output;
- (v) **declared resources**: which clean ancillas exist, and in which states, is stated as part of Π, not as an
  unstated absence.

A milestone pass whose model fails R-MENU is printed "pass for the declared operation set; R-MENU fails at (i)–(v)".
It does not count toward the governing question. K-MENU (§5) must fail (ii).

**Two failure classifications, kept distinct.** An explicit violating preparation is **M0 lost**. An operation
restriction that is stated but not independently justified is **R-MENU unmet**, even when M0 holds within the
restricted model. "Only the declared read coupling may write hidden cells" is largely a menu; it counts as a principle
only if derived, e.g. from the substratum dynamics, which is open (§4, claim table). Under Option A's revision-1 rule
ρ₀, M0 is lost by K-SYMP's witness; under the candidate Π_ω, both classifications are open.

### 2.3 Preserved results (controls fixed in advance) and the beyond-target prediction

The candidate must reproduce each of the following, or the run halts:
- **node 8's eight answers.** Pur-E and Pur-U at budget *m* = 3 for ℛ₁ᵃ, ℛ₁ᵇ, ℛ₂ᵃ (1- and 2-bit observer), ℛ₂ᵇ (1- and
  2-bit observer), K-SWAP and CL-C4, as pinned in K-N8 (§5). They are recomputed with node 9's equivalence engine
  under node 8's own preparation menu, and agreement is required. This controls the engine. It does not say that those
  classes satisfy §1.2;
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

- **Lemma F (rational models) [W].** An exact finite protocol whose preparations and transition probabilities are
  rational has rational outcome probabilities: each is a finite sum of finite products of rational entries. Such a
  protocol therefore cannot attain an irrational value, such as (2+√2)/4 or 2√2, exactly. The lemma excludes exact
  attainment only. It does not exclude contextuality, Bell violation or approximation. Example: *p* = 17/20 gives S =
  14/5 under Lemma S, and 2 < 14/5 < 2√2 since 196/25 < 8. M5-A's exact form (A1) is
  decided negative for every such model as the lemma's consequence; only its A2 form, a limit along a declared family,
  is open.
- **Lemma A** [rec, MC8 PREREG §6.1] is applied where its hypotheses are checked: full access with full preparations
  gives classical probability.
- **The composition lemma** [rec, MC8 A-3 F1, A-4, A-5]. If every composite preparation is a mixture of product
  preparations, with one weight set containing ½ for the local and composite purity tests, pure composites are
  products of pure states.
- **Lemma S (POM to CHSH by steering) [W; the owner's derivation, 2026-10-21].** P_uv are the POM preparations and D_x
  the decoders (M3). If a common extension lets the other party choose y, obtain a fair outcome b and thereby prepare
  P_{b,b⊕y}, then P(a, b | x, y) = ½ P(a | P_{b,b⊕y}, D_x). POM success means a = (b, b⊕y)_x = b ⊕ xy, the CHSH winning
  condition; (b, y) ↦ (b, b⊕y) is a bijection, so the winning probability is *p* and S_CHSH = 8*p* − 4 (equal to
  4(2*p* − 1)). The first party's marginal at y is that of ½(P₀₀ + P₁₁) (y = 0) or ½(P₀₁ + P₁₀) (y = 1), independent
  of y by parity equivalence; the other marginal is uniform; the table is no-signalling. Endpoints [rec, coordinator
  check 2026-10-21, exact]: *p* = 3/4 → 2, (2+√2)/4 → 2√2, 17/20 → 14/5. *Physical qualification:* building the table
  does not show that OI implements it; the common extension and its steering measurements must exist in the model
  (I-22).

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
sizes and ancilla count *k*. Every M1/M2 statement, verdict or expectation names its preparation set (Prep(𝓘) at the
stated budget and generators, a finite menu, or a convex closure) and its allowed purifying systems (type, size,
ancillas). A pass holds for that preparation set and those purifiers only.

**M1. An operationally pure composite with a mixed marginal.**
- *Question:* is there a composite AB of the model and a pure ψ ∈ Prep(AB) (§1.5) whose A-marginal is not pure?
- *Rule:* PASS iff an exact witness is found, with ψ's purity certified over all of Prep(AB) at the declared budget and
  across the model. FAIL iff exhaustive enumeration of Prep(AB) at the declared sizes finds no witness. PARKED if the
  enumeration exceeds §8's bound.
- *Establishes:* the model escapes the node-8 composition obstruction at that size.
- *Does not establish:* purification for every state, uniqueness, contextuality, Bell violation, or QM. K-SPK's two
  readings (§0) are reported separately, each with its preparation set and purifying system.

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
- *Establishes:* C5-P for this model, with these preparations and purifiers, at those sizes.
- *Does not establish:* QM or the other CDP axioms. A pass on the preparable set does not establish a pass on the
  convex closure, where Lemma K (MC8 §6.1) applies.

**M3. A preparation-contextuality witness (two-bit parity-oblivious multiplexing).**
- *Task:* the sender receives uniform (b₀, b₁) and prepares P_b ∈ Prep(S). The receiver receives a uniform y ∈ {0, 1}
  and guesses b_y by a binary-outcome allowed experiment D_y. Success = ¼ Σ_b ½ Σ_y Pr(guess = b_y | P_b, D_y).
- *Parity obliviousness (premise):* ½(P₀₀ + P₁₁) ~ ½(P₀₁ + P₁₀) under §1.3, checked over **all** allowed experiments
  through W(𝓘), at *k* = 0, 1 and 2 ancillas, before any score is compared (§1.4). Agreement on a selected readout set
  is never sufficient.
- *Threshold:* the preparation-noncontextual bound is 3/4 [rec, owner read 2026-10-21: Spekkens et al. 2009, Theorem 2].
  It is recomputed in house by K-PNC.
- *Rule:* PASS iff exact preparable P_b and realizable D_y satisfy the premise exactly and success > 3/4, with both
  properties following from the model's dynamics and interface. FAIL iff the exhaustive maximum over premise-meeting
  encodings is ≤ 3/4 over Prep(S) at the budget and over decoders of depth ≤ D. That maximum must be stable from D to
  D + 1, and a universal claim needs a reviewed [W]. PARKED otherwise.
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
  (POM ≤ 3/4, |S| ≤ 2) is printed "vacuous".
- Respecting the quantum bounds is necessary for a quantum model and does not identify the quantum correlation set.
  Where one construction (Lemma S, §2.4) connects the POM and CHSH tests in the model, their bounds are linked:
  the M5-L block prints the link, and the two lines count as one piece of evidence, not two (§6). M5 together with
  M1–M4 does not establish QM.

***

## 4. The first candidate model: Option A (owner decision Q1)

**The boundary toy bit, under the candidate principle Π_ω.**
- *System T.* A visible pointer x ∈ {0, 1}, initially 0, and record cells h ∈ ℤ₂²; for *n* systems, h ∈ ℤ₂^{2n} with the
  standard symplectic form ω. φ = identity. Bath bits follow the counting measure; the fixed prior on h is uniform.
- *Read coupling [A-typed].* A coupling step that makes the record functional ω(u, ·) readable writes it into a pointer
  and shifts the record along u by a fresh bath bit: R_u is x ^= ω(u, h), then h ^= r·u. Read physically: the pointer's
  conjugate variable is hidden, so reading a record kicks the record's conjugate content.
- *Record-only rule ρ₀ (revision 1):* a coupling step that reads nothing is a record bijection mapping the readable
  functionals onto themselves. **ρ₀ admits an exact M0 violation** (K-SYMP) [rec, owner check 2026-10-21; coordinator
  check 2026-10-21, exact replay]. Two toy bits, h = (q₁, p₁, q₂, p₂), uniform prior: (1) read q₁, keep 0 → support 8;
  (2) read q₂, keep 0 → 4; (3) record-only swap p₁ ↔ q₂ → q₁ = p₁ = 0, support 4; (4) read q₂, keep 0 → q₁ = p₁ = q₂ =
  0, support 2 < 2² = 4; branch probability 1/8, back-action included. The swap is bijective and permutes all 15 nonzero
  readable linear functionals but is not symplectic (ω(e_q₁, e_p₁) = 1 becomes 0), so it breaks the pairing between a
  readout and its disturbance. Excluding pointer swaps alone cannot save the restriction.
- *Candidate principle Π_ω (to be evaluated, not adopted).* Allowed reversible record transformations preserve the full
  read/disturb relationship; in the linear setting, they preserve the symplectic pairing ω. Option A is computed under
  Π_ω, with ρ₀ run only as K-SYMP's arm. Whether Π_ω is a principle or a menu is decided by §2.2.
- *Observations; none is a verdict.*
  - (i) *What symplecticity does and does not establish.* Main.md:290 [corpus]: "$$u'_x = \sum_{z \sim x} u_z + v_x,
    \qquad v'_x = u_x ,$$". Its matrix on (u, v) is M = [[L, I], [I, 0]], L the symmetric adjacency; MᵀJM = J for
    J = [[0, I], [I, 0]] because Lᵀ + L = 2L = 0 over F₂ [rec, coordinator check 2026-10-21: exact over F₂ for every
    symmetric L at *n* ≤ 3 and 200 random ones at *n* = 4, 5, 474 matrices; a non-symmetric L fails]. Main.md:320
    [corpus]: "All of this concerns the realization displayed above and is not a property of arbitrary finite
    bijections." Symplecticity of the update does not establish that every available intervention preserves the
    pairing, that every symplectic map is physically available, or that the observer cannot learn both conjugate
    coordinates [rec, owner 2026-10-21].

    | claim | support |
    |---|---|
    | the displayed binary update preserves a symplectic pairing | established algebraically [rec, owner check; coordinator check 2026-10-21] |
    | Option A's read-and-disturb rule admits a symplectic implementation | established in the elementary construction below [rec, owner check 2026-10-21; coordinator re-check 2026-10-21] |
    | OI's available operations and preparation resources enforce that rule and its restriction | open: needs an explicit construction from the declared substratum dynamics and a closure argument |

  - *Elementary construction.* The pointer has a visible coordinate Q and a hidden conjugate P; the coupling is Q′ =
    Q + ω(u, h), h′ = h + P·u, P′ = P. It is symplectic for each of the three nonzero u of one toy bit; with Q = 0, P an
    independent fair bit and P discarded, it reproduces R_u; with P known, the same coupling reads without disturbance
    [rec, owner check; coordinator re-check 2026-10-21, exact]. The load-bearing resource assumption is named
    **pointer conjugates are never supplied clean**: a candidate independent postulate, not a consequence of
    symplecticity, carried in the clean-ancilla declaration and R-MENU (v). Its precise form [rec, owner 2026-10-21]:
    *each fresh pointer is supplied with Q = 0, its conjugate P uniformly distributed and independent of the system and
    of every accessible preparation record.* The independence clause is load-bearing. If an accessible record carries
    P, the observer knows the disturbance P·u and, where the corrective displacement is available, can undo it, so
    marginal uniformity of P alone does not supply the restriction.
  - *Diagnostic K-SYMP2* [rec, owner check; coordinator re-check 2026-10-21, exact]. Main.md:290's update on two sites,
    u₁′ = u₂ + v₁, v₁′ = u₁, u₂′ = u₁ + v₂, v₂′ = u₂, is bijective and symplectic. With the visible site at (u₁, v₁) =
    (0, 0) and the hidden site uniform, after two steps the visible site is (v₂, u₂), revealing both hidden coordinates,
    and the hidden site is (0, v₂), determined by the record; each branch has probability 1/4. Symplectic evolution with
    a clean, fully readable canonical pair breaks the support bound, so the distinction between a visible pointer and its
    inaccessible conjugate is load-bearing. It is a diagnostic, not a certified C1–C4 witness.
  - (ii) *Expected M3 consequence.* Under Π_ω, Option A is close to Spekkens' toy theory, which has a
    preparation-noncontextual ontological model [Q, pending PC-SPK]. Option A is therefore expected to FAIL M3 by
    construction. Its value lies in M0–M2 and in whether the pairing is inherited (§6).
- *Clean ancillas (draft declaration, to be fixed at freeze):* the visible pointer coordinates, each at 0, are the only
  clean ancillas. Pointer conjugates and hidden cells are supplied only under the counting measure, each fresh pointer
  conjugate independent of the system and of every accessible preparation record (the postulate above). This is a
  restriction on primitive resources, not a prohibition on states prepared later. Its statement as a principle is part
  of R-MENU (v) and is open (`NOTES.md` QA′).
- *The proposed preparation restriction:* let *N* be the number of canonical pairs present: the *n* toy bits and the
  pointers not yet discarded. Every preparable state of all hidden coordinates jointly (each toy bit's two, each
  present pointer's P), conditioned on all accessible records (each present pointer's Q included), has support of size
  ≥ 2^*N*. Discarding a pointer removes its pair from *N*. With no pointer present, *N* = *n*. A fresh
  pointer (Q = 0 recorded, P uniform) and one read R_u followed by conditioning on Q both meet it with equality
  [coordinator hand check 2026-10-21]. It is evaluated on the information available about the whole pair, never on whether a
  coordinate carrying a given name is definite. A permitted symplectic exchange can turn (Q = 0, P unknown) into
  (Q unknown, P = 0) without creating a jointly known pair [rec, owner 2026-10-21]; such a state is not a violation.
  It is an invariant to test, neither a general necessity nor a sufficient condition for purification. The number of
  record functionals a state determines is printed beside it as a diagnostic and decides nothing.
- *Derived operations.* Ops(Π_ω) are computed mechanically under R-MENU (ii); the affine symplectic maps are not
  assumed. Joint readouts of ω(u, ·) with u ∈ ℤ₂^{2n} are the joint operations.
- *R-flag:* R-yes. Every record functional is reachable by some R_u. Bell branch: local.
- *Smallest realization for C5-P:* *n* = 2 (A = one toy bit, B = one toy bit). Sizes computed: *n* ≤ 4.
- *Beyond-target postdiction (independent postdiction, not a new quantum prediction):* repeatability of a read before
  and after an intervening complementary read, derived from the frozen read coupling: the exact probability that two
  reads of ω(u, ·) agree around a read of ω(v, ·), for ω(u, v) = 0 and 1, against the quantum value of the
  corresponding Pauli sequence; a mismatch is a miss. Also prerecorded: in its local branch the model predicts |S_CHSH|
  ≤ 2 for every composite, a raw-direct conflict with loophole-free Bell tests [Q]. The model is a step toward the
  question, not a candidate theory of nature.

### 4.1 The decisive first question (M0)

- *Question:* starting from the fixed prior, does the full operational preparation closure of §1.2, with clean ancillas
  (g1), couplings (g2), feedback (g3), waiting (g4), discarding (g5) and heralding with back-action (g6), retain the
  proposed preparation restriction (§4)?
- *Rule:* **retained** iff the closure computation is shown complete for its stated resource scope (*n*, *k*, b_r, b_h),
  by a termination proof or a mathematical characterization of Prep at that scope (§1.2, layer 2), and every state in
  it, every heralded branch of nonzero probability included, satisfies the restriction. Completeness is never inferred
  from Lemma W or from the stabilization of W. **Lost** iff an exact witness preparation violates it; the witness is
  printed as its generator sequence, with its success probability and post-measurement state. PARKED if completeness is
  not shown within §8's bound, with the completed depth.
- *First construction task, two results kept separate:*
  - *(C-i) Mechanism.* Implement the pointer coupling from the declared substratum (lattice) dynamics and resources,
    with clean resources accounted for explicitly. Success establishes only that the measurement mechanism is
    available in the model. Any further resource or access condition it needs is recorded as an independent
    postulate, not attributed to symplecticity.
  - *(C-ii) Closure.* Show that every allowed continuation, conditioning and feedback included, preserves the proposed
    preparation restriction: this is M0's rule above. Success establishes that the restriction survives the rest of
    the interface at the stated scope.
  - Each is reported with its own verdict line. (C-i) passing does not establish (C-ii), and (C-ii) is computed only
    over the mechanism (C-i) actually delivers.
- *Pressure tests (§A.31), required for "retained":* K-CLN-A (a heralded read, then a clean-bit swap), K-SYMP's ρ₀ arm
  and K-SYMP2 must each print "lost" with its witness (§5).
- *Scope:* either outcome is a result about the specified construction at the stated *n* and *k* (K-ANC). "Lost" fails
  R-MENU (iii) and names the operation responsible; M1–M5 still run on the closure as generated. "Retained" does not
  establish M1 or M2.

***

## 5. Controls (each computed exactly; roles explicit; a red control voids its milestone)

| id | role | construction | must |
|---|---|---|---|
| K-QPOM | positive (M3, M5) | qubit: ρ_b = ½(I + ((−1)^{b₁}X + (−1)^{b₀}Z)/√2); D₀ = Z, D₁ = X | ½(ρ₀₀+ρ₁₁) = ½(ρ₀₁+ρ₁₀) = I/2 as matrices, which is the complete invariant for every POVM, ancilla and composite; success = (2+√2)/4 exactly in ℚ(√2) |
| K-PNC | calibration (threshold) | exact LP over ontological models on the four response pairs with every deterministic response function, PNC imposed (MC6 P3 recomputed) | maximum exactly 3/4; without parity obliviousness, 1 |
| K-CBIT | countercontrol (M3) | classical bit, full access | maximum POM success with exact parity obliviousness = 3/4, attained by m = b₀ |
| K-HL0 | countercontrol (M1, M3; §1.4 case b) | classical bit plus a hidden preparation label that no allowed experiment reads (R-no, response-irrelevant) | preparations differing only in the label are equivalent; POM ≤ 3/4; M1 and M3 FAIL |
| K-HL1 | countercontrol (§1.4 case a; premise check) | K-HL0 with a coupling step that reads the label | label-different preparations inequivalent; the §1.4 premise check runs on every encoding; premise-meeting encodings ≤ 3/4; M3 not PASS |
| K-SPK | calibration (M1, M2, M3) | Spekkens toy bit, original form (MC8 PREREG §6.5 reading; 6 + 1 states; 60/30/1 for two) | M3: POM ≤ 3/4, verified by computing W's rank and the maximum, not assumed; M1 and M2 printed for "the seven-state single-toy-bit menu with the tested one-toy-bit partner" and for "its convex closure, against the tested pure joint states", against the two readings of §0 |
| K-MENU | countercontrol (R-MENU, M5-L) | MC6 P5: destructive complementary readouts on ℤ₂², Y withheld, generated preparations; and its *w* = 1 member (the gbit) | passes M3 for its declared set; R-MENU (ii) fails, naming the withheld Y readout; at *w* = 1, M5-L FAIL (POM = 1 > (2+√2)/4) |
| K-PR6 | countercontrol (M4, M5-L) | MC7 LE(1,1) / MC6 B2 [rec]: A = λ, B = λ ⊕ ab | M4 PASS with S = 4 and no-signalling; M5-L FAIL |
| K-BL | preserved result | every local-branch composite of the model | |S| ≤ 2 exactly; otherwise the run is VOID |
| K-CL | countercontrol (M1, M2) | classical bit pair, full access | M1 FAIL; Pur-E fails for every mixed state |
| K-QSTAB | positive (M1, M2) | MC8 §6.5's stabilizer instance (7 one-qubit and 91 two-qubit states, ℚ(i, √2)) | M1 PASS; Pur-E and Pur-U hold for A = one qubit |
| K-N8 | preserved result (engine) | node 8's eight classes under node 8's menu; reference MC8 `probe/p8s1.r2.run1.out`, sha256 `b5ce288c3ed13658198a3a605387a06d76e6270b18923d6129350265426bd951`, at `78913467` (reviewed, ACCEPT WITH NOTES; carries the N1/N2 countercontrols); its 46 realization lines equal r1's byte for byte [rec, coordinator check 2026-10-21, sha256 and line comparison] | the eight Pur-E/Pur-U answers reproduced |
| K-ANC | engine; extension guard (§1.3) | equivalence at *k* = 0, 1, 2 ancillas | any change from *k* = 1 to *k* = 2 halts (PARKED, gap named); every equivalence-dependent line prints its *k*; a pass is evidence for the tested extensions only; no line claims *k* > 2 without a reviewed proof |
| K-REACH | engine (reachability, §1.2) [rec, owner check 2026-10-21] | the example of §1.2 | with no heralding budget the reachability layer prints PARKED while W has dimension 2 after one round; at b_h = *j* it lists exactly *j* + 1 conditional states |
| K-HERALD | engine (g6) [rec, owner check 2026-10-21] | fair hidden bit h, pointer x = 0, bath bit r. Arm 1: x ^= h. Arm 2: x ^= h, then h ↔ r | both arms: Pr(x = b) = 1/2. Arm 1: state given x = b is h = b. Arm 2: state given x = b is h uniform |
| K-CLN | countercontrol (M0 detector) [rec, owner check 2026-10-21] | fair hidden bit, declared clean bit at 0, swap allowed, no heralding; restriction: h is not a point mass | M0 prints "lost" with the swap as witness |
| K-CLN0 | positive (M0 detector) | fair hidden bit, no clean ancilla, bijections on h only, no readout; same restriction | M0 prints "retained" at a fixed point |
| K-CLN-A | pressure test (M0) | Option A, *n* = 1, plus one clean hidden bit; a direct swap leaves support 2, within the bound, so first a heralded read of q, keep 0, then the clean bit swapped into p: support 1 [rec, coordinator check 2026-10-21, exact] | M0 prints "lost" with that two-step witness |
| K-SYMP | countercontrol (M0, operation rule) [rec, owner check 2026-10-21] | Option A, *n* = 2, the four-step witness of §4 | under ρ₀, M0 prints "lost" with that witness; under Π_ω, the swap p₁ ↔ q₂ is absent from Ops(Π_ω) and the witness is excluded |
| K-SYMP2 | diagnostic (M0 detector) [rec, owner check 2026-10-21] | the two-site update of §4 as φ, visible site clean at (0, 0), hidden site uniform | under every rule, M0 prints "lost" with the two waiting steps as witness (hidden support 1) |

A control result that merely reproduces the formula it is meant to check is vacuous. K-QPOM computes the density
matrices from ρ_b, not from the success formula; K-PNC's LP is solved, not the value inserted; K-HERALD's states come
from the engine's joint update, not from the stated answer.

***

## 6. Productivity test (§A.31), fixed before execution

**Baseline.** The following are restatements and do not count:
- node 8's composition lemma and eight answers;
- MC6 P3–P5 and N1–N5;
- MC7's verdicts;
- Lemma F, Lemma A, Lemma K and Lemma W;
- the outcomes of K-HERALD, K-CLN, K-CLN0, K-REACH, K-SYMP and K-SYMP2, the calibration readings of §0, and Lemma S;
- the observations of §4: the first two rows of its claim table, the elementary construction, and an M3 FAIL of Option
  A under Π_ω, which is expected by construction [Q] and is not a finding;
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
- (d) R-MENU fails for a candidate whose principle was stated in advance, M0 "lost" included (other than K-SYMP's
  witness under ρ₀), and the computation names the operation or witness preparation that breaks it. This exposes a
  hidden assumption. It is recorded as an assumption-watch marker for later nodes;
- (e) M0 prints "retained" under Π_ω with K-CLN-A, K-SYMP and K-SYMP2 green and completeness shown, so that the
  restriction is shown to rest on Π_ω and the declared clean-ancilla principle at the stated resource scope.

M5-L lines linked by one construction count as one item. Anything else is a non-gem (record-only). A favourable branch,
any PASS or "retained", gets the skeptical pressure test of §A.31 before it is recorded: the controls are rerun with the
decisive object perturbed. Output classes are NEW, POSITIVE, ELABORATING, CONFIRMING or BORDERLINE.

***

## 7. Invariant→checkpoint table (§A.41)

| # | invariant | checkpoint |
|---|---|---|
| I-1 | this file preceded every computation and is unchanged | sha256 recorded at freeze, printed first by the probe; amendments under `amendments/` with time, reason and state of knowledge, before the computation they touch |
| I-2 | the interface and model are fixed before computing | 𝓘, Π, Ops(Π), clean-ancilla declaration, R-flags and Bell branch printed with digest before any milestone; every milestone line cites the digest |
| I-3 | one equivalence relation for every test | a single function computes ~ from W(𝓘); a static scan refuses any other equivalence code path; mutant KM-1 |
| I-4 | equivalence covers ancillas; results scoped to *k* and to the tested extensions | K-ANC at *k* = 0, 1, 2; every equivalence-dependent line prints *k*; KM-2, KM-16 |
| I-5 | Lemma W's closure is complete | fixed-point iteration logged with its dimension per round, ≤ *N* rounds; cross-check against explicit enumeration to depth 4 on K-SPK and K-HL0 (spans equal); KM-3 |
| I-6 | preparations generated, never listed, with all six generators | Prep(𝓘) built only by the §1.2 generator; a static check that (g1)–(g6) are each invoked; a static scan refuses a literal state list outside controls; KM-4, KM-13 |
| I-7 | purity by preparable decomposition | §1.5's three readings printed separately; MC8 A-2's KM-32 fixture rerun; KM-5 |
| I-8 | parity obliviousness over all experiments, checked as a premise | M3's check calls I-3's relation before any score comparison; K-HL1 green; KM-6 replaces it by a fixed readout set, and K-MENU's Y readout must then pass falsely and be caught; KM-15 |
| I-9 | exactness | `Fraction` and sympy ℚ(√2) only; an AST scan for floats on the verdict path; a missing dependency fails, never skips |
| I-10 | verdicts only over green controls | each milestone block is gated on its controls (§5); a red control prints VOID; KM-7 |
| I-11 | milestones never merged | separate generated blocks; a static check that no milestone reads another's status; KM-8 |
| I-12 | verdict text generated from measurements | every count and status is computed; scanned against MC8 A-1's word list (extended: "theorem", "impossible", "no-go", "universal", "for every realization"); every M1/M2 line names its preparation set and purifiers; KM-9 |
| I-13 | R-MENU is computed | Ops(Π) enumerated from Π's predicate; (v) printed; K-MENU must fail (ii); KM-10 |
| I-14 | preserved results hold | K-N8, K-BL, condition O, no-signalling, the C2 check printed before milestones |
| I-15 | determinism | two runs byte-identical; `SHA256SUMS`; no randomness |
| I-16 | resource bound | wall time printed per phase; §8's limits |
| I-17 | literature never decides | each line lists its [Q] dependencies; a line depending on an unmet PC gate prints "provisional" |
| I-18 | heralding uses the post-measurement state | K-HERALD green before any preparation is generated; KM-14 |
| I-19 | the decisive closure question is decided first, by its rule | M0 block printed before M1, with completeness certificate or witness; K-CLN, K-CLN0 green; "retained" printed only with K-CLN-A (heralded read, then swap) , K-SYMP and K-SYMP2 green; KM-17, KM-20 |
| I-20 | reachability decided separately from equivalence | M0 and Prep print their resource scope (*n*, *k*, b_r, b_h) and a completeness certificate, never W's dimension; K-REACH green; KM-18 |
| I-21 | the operation rule preserves read/disturb; the conjugate-resource assumption is visible | Ops(Π_ω) contains only ω-preserving record maps (checked on every element); K-SYMP's two arms and K-SYMP2 green; the clean-ancilla printout names the pointer-conjugate postulate; KM-19, KM-22 |
| I-22 | Lemma S's link computed, not assumed | a linked POM/CHSH pair prints the steering table from the model's own extension, its S and marginals; K-QPOM's extension gives S = 2√2 exactly; KM-21 |

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
- KM-12: a float enters the success computation;
- KM-13: generator (g1) dropped (K-CLN must then print "retained" and be caught);
- KM-14: the heralded state inferred from the revealed value (K-HERALD arm 2 must then print h = b and be caught);
- KM-15: a premise-failing encoding compared with 3/4 (K-HL1 must catch it);
- KM-16: a line printed without its *k*;
- KM-17: M0's "retained" printed with K-CLN-A suppressed;
- KM-18: M0's completeness inferred from W's stabilization (K-REACH must then print a finite closure and be caught);
- KM-19: Ops(Π_ω) replaced by ρ₀'s functional-permutation test (K-SYMP's Π_ω arm must then find the witness);
- KM-20: K-CLN-A run as a direct swap without the heralded read (it must then fail to print "lost" and be caught);
- KM-21: the CHSH value of a linked pair inserted as 8*p* − 4 instead of computed from the table (I-22's scan);
- KM-22: M0's generators without waiting (g4) (K-SYMP2 must then print "retained" and be caught).

***

## 8. Order, resources and replay

**Order (depth-first, §A.12):**
1. the engine and the controls: K-HERALD, K-REACH, K-CLN, K-CLN0, K-ANC, K-PNC, K-QPOM, K-CBIT, K-HL0, K-HL1, K-SPK,
   K-CL, K-QSTAB, K-N8, K-MENU, K-PR6;
2. the model's interface printout and R-MENU;
3. M0, the decisive first question, with K-CLN-A, K-SYMP and K-SYMP2, after the first construction task (§4.1);
4. M1, then M2 at *n* = 2;
5. M3;
6. M4;
7. M5;
8. M2 at the larger sizes;
9. the mutants;
10. productivity and the independent review.

A FAIL at M1 does not stop M3 or M4, since they are separate questions; nor does M0 "lost" stop M1–M5. Each is reported.

**Resources (§A.40).** The local run must stay under about 60 minutes. Each phase prints its wall time and halts
reporting its completed range if it exceeds its share. Anything larger, such as *n* = 4 enumerations or deeper decoder
stability, becomes a CI plan proposed on the guiding PR and runs only with owner approval.

**Replay.** Two runs from a clean checkout of the frozen commit must be byte-identical. `SHA256SUMS` covers the probe and
both outputs, and a reviewer replays with `python3 -I -B`.

***

## 9. Literature: narrow claims and gates

No paper was read in this session (WebFetch to arXiv failed, DNS, 2026-10-21). The two POM values rest on the owner's
read; every other entry is [Q].

| source | claim used here | status | gate |
|---|---|---|---|
| Spekkens, Buzacott, Keehn, Toner, Pryde, PRL 102, 010401 (2009), arXiv:0805.1463 | the two-bit POM task; with exact parity obliviousness, PNC success ≤ 3/4; quantum (2+√2)/4 | values 3/4 and (2+√2)/4: [rec, owner read 2026-10-21: Theorem 2 and its two-bit quantum example]; task wording: [Q] | PC-POM: an amendment quoting the task definition. The numbers that decide M3 come from K-PNC and K-QPOM |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | preparation-noncontextual ontological models of quantum theory do not exist, a proof that applies already in dimension 2 | [Q] (abstract-level search summary) | PC-S05 before any verdict text cites it |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | the toy theory; knowledge balance; it has a preparation-noncontextual ontological model | [Q] | K-SPK is built from MC8's combinatorial reading; PC-SPK as in MC8, also before §4 (ii) is cited as more than an expectation |
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

Every negative result concerns the specified model, its interface 𝓘 (clean ancillas included), the sizes and ancilla
count computed and the declared readings. A FAIL does not establish that observational incompleteness cannot yield
purification, contextuality, Bell violation or QM. A PASS establishes the milestone's stated content for that model,
its preparation set and its purifiers, and nothing beyond it. Lemma W decides equivalence exactly within the declared
finite model, not reachability; beyond it, K-ANC and a reviewed extension argument govern. Finite-model success is
never classified as an exact quantum reconstruction (MC8 A-1). No equivalence is claimed. M5's two directions are
reported separately.

***

## 11. Procedure and freeze

- **Before freeze:**
  - the owner fixes Option A's clean-ancilla declaration, with the pointer-conjugate postulate, its statement as a
    principle and the status of Π_ω (§4; `NOTES.md` QA′), and the resource scope b_r, b_h (Q5);
  - the remaining questions of `NOTES.md` are disposed;
  - an independent pre-freeze review runs.
- **Freeze:** the sha256 of this file is recorded in the commit message and on the guiding PR. After freeze the file is
  not edited. Changes go to `amendments/` with time, reason and state of knowledge, before the computation they touch.
  No amendment changes a decision rule in a candidate's favour.
- **After a milestone's first computation:** its rules are frozen. A later discrepancy is recorded, not repaired.
