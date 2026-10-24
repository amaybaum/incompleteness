# Node 9: which OI condition yields operational structure beyond the minimal tensor product? Preregistration

**DRAFT — NOT FROZEN; no computation may run against this draft.**

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. Freeze
requires the items of §11 and the sha256 of the frozen bytes recorded before any computation. The decision rules are
fixed here; expected numbers are not (§A.29). Revision 3 of the draft.

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
- **Q10.** Model A is finished as a bounded calibration, with C-i covering the whole record lifecycle; Option B follows.
- **Q11.** Pointer reuse need not be forbidden if recording has the appropriate back-action (the copy X′ = X + Q,
  P′ = P + Y, Y fresh and never accessed). Single use is the default; the back-acting copy is the tested alternative.
- **Q12.** Independence: Pr(P = r | h, H) = ½ for the current target h and accessible history H; a discarded pointer
  stays unavailable to later interactions.
- **Q13.** The biased state (3/8, 3/8, 1/8, 1/8) is carried as a control for Option B (§4, K-BIAS).
- **Q14 (owner, 2026-10-22).** M0's restriction is membership in Kₙ, not support size (§4). It was adopted after the
  native-memory results of 2026-10-22 were seen: the biased-mask family keeps support 2ⁿ while a conjugate toy
  coordinate becomes predictable with probability arbitrarily close to 1 (99/100 tested). It is a calibration condition of model A, not a
  candidate C5. Three qualifications apply:
  - M0 tests the preparations the closure actually generates. A preparation is never admitted because it passes Kₙ
    (I-6).
  - Membership is kept separate from reachability. Closure inside Kₙ does not show that every member of Kₙ is
    preparable (I-20).
  - The generated finite menu is kept separate from its convex completion, in M2's purification lines above all.

**Tags.** [corpus] text quoted verbatim from the corpus at the base, with file:line; [rec] stated in a thread record, not
re-derived; [rec, owner …] a check or reading supplied by the owner, not re-derived in this session; [W] written
argument, to be reviewed; [EC] exact computation (none run); [lit-read] literature read in full and the claim verified
against the text; [Q] literature not read, whether recalled or known only from a search summary; [rec, coordinator
check 2026-10-21] verified in this session by the exact check stated (script and output kept off-repo as provenance);
[rec, design/… at SHA] a pre-freeze design report on this branch at that commit, with its review status stated. No
claim tagged [Q], and no claim from a design report under review, decides a verdict (§9).

***

## 0. Base and state of knowledge

- Thread `research/missing-component-20261020`; revision 3 drafted at `b71199a86eeb8e600905c369c89731de3c43d05a`,
  whose node-8 records are those of the close-out `789134678aac771466f4443f8d053bdf084a5b18` with amendment A-5 (PLAN =
  `../PLAN.md`, MC*k* = `../mc-nodek/`). `main` at `af8c59d6d61322853f5b456da2849890d5c790e7`. `papers/Main.md` is
  identical at both. Pre-freeze design inputs, disclosed in §4: design/c1 at
  `49033a3e61233dcfa342c2cce59992c53ee9d6fa` (reviewed, ACCEPT WITH CORRECTIONS) and design/emb at
  `3f11c8f7ecfa043016833595dfa1dcf17a4b857b` (tree `6afbdab5`; corrected; re-review ACCEPT WITH CORRECTIONS; N1–N7
  applied in the commit that adds this line); the pre-freeze review of `6cf71e0e`; design/cards at `edf17209`
  (reviewed at `a9af8ef0`, ACCEPT WITH CORRECTIONS; corrections applied in place, not yet re-reviewed), which motivates
  M1's spectator-stability clause (§3).
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
- Nothing else has been computed beyond the [rec] checks, the pre-freeze review's scripts and the two design reports
  (§4). No paper was read in this session (§9).

***

## 1. Operational equivalence, the first definition

Declared once per model, printed with a digest before any computation (I-2). Every test reads this one relation:
purification, contextuality and Bell. **A preparation counts as the same state in one test only if it would count as
the same state in every test.**

### 1.1 The interface 𝓘 of a model

- **System boundary.** A system *S* is its visible cells V_S together with the hidden cells H_S assigned to it,
  including its record cells. Bath cells are hidden cells outside every system: each is fresh, used at most once, under
  the counting measure, and discarded after use.
- **Accessible records.** The configurations of visible cells, read by configuration readout (κ4), unless the model
  declares a narrower readout rule as a postulate (R-MENU (v); Option A's PP-2). A readout does not change the ontic
  state. Retention of every record and a disturbance-free visible copy are grants of this interface, not of the
  lattice dynamics [rec, design/c1].
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
  other than the counting measure (a visible pointer at 0, a known-zero bit), with its count, and states that
  declaration as a physical principle (R-MENU (v)). Visible cells fixed by the protocol (condition O) are clean
  ancillas and are declared as such. The declaration states two counts separately, each a postulate: (i) the number of
  visible read-out sites, and (ii) the number of clean coordinates, stating for each whether its conjugate is also
  supplied clean. Coordinates are counted, not pairs: in the lattice two visible sites with one clean coordinate each
  and no clean pair can learn the toy. Counting clean coordinates suffices only for independent product preparations.
  If correlated preparations are admitted, known relations count too. For preparations specified by affine
  constraints, A s₀ = a, the initial constraint information is counted by rank A. More general preparations need
  their actual support and probability law, because rank A misses nonlinear correlation. Example: (x, y, xy) with x
  and y fair satisfies no nontrivial affine constraint (rank A = 0), yet retaining x and y determines the third bit
  [rec, owner 2026-10-21; `design/emb/common-spec/aht.py`]. For example, the support {(0,0),(1,1)}
  has no clean coordinate, but its known parity x ⊕ y = 0 becomes a known-zero coordinate under the reversible map
  (x, y) ↦ (x, x ⊕ y) [rec, owner 2026-10-21; `design/emb/common-spec/aht.py`]. In the linear binary model, the target T s₀
  at a stated time, given A and the physically retained records H s₀ (never an external list of past observations), has
  conditional support 2^(rank[A;H;T] − rank[A;H]) under a uniform affine ensemble [rec, owner; checked against
  enumeration in `design/emb/common-spec/aht.py`]. Write d_prior = rank[A;T] − rank A and d_posterior = rank[A;H;T]
  − rank[A;H]. Then d_posterior = 0 means the retained memory determines the target. d_prior = 0 means the target was
  determined without reading that memory, possibly by overwrite. d_prior − d_posterior is the information the
  retained memory supplies about the target, in bits. For a toy pair, "learnt" in design/emb's sense means
  d_posterior = 0 with d_prior = 2 (prior support 4). d_posterior = 0 with d_prior = 1 is mixed: one bit comes from
  memory and one is fixed without it. The common specification prints both dimensions and these labels. Coin cells (§1.2) are visible cells with no clean coordinate; they are not
  counted under (i), because no coupling step brings one into contact with the toy, a pointer or another record cell.
  Withholding any clean resource is a postulate. Neither count bounds what is learnt by itself: a second visible site
  with no clean coordinate can lift L1, and so can a second clean pair read through one site [rec, design/emb at
  `3f11c8f7` (tree `6afbdab5`), corrected; re-review ACCEPT WITH CORRECTIONS; N1–N7 applied in the commit that adds
  this line].
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

Mixtures arise inside the same rule: a bath bit is read into a visible coin cell and steers the preparation. A coin
cell takes part in no coupling step with the toy, a pointer or another record cell; its value enters only through
feed-forward (g3). A budget of *m* coins gives the weights *k*/2^*m*. Preparations are not supplied as priors, and a
test never adds one.

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
2. **preparation reachability**, at a stated resource scope (for Option A, S of §4.1), by a completeness certificate
   (§4.1: a fixed point of the closure search with the remaining budgets in the state, or an exact period); otherwise
   the result is PARKED at deterministic caps (I-20). The engine has no characterization path;
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
new couplings, or apparatus memory that Ω does not represent, such as pointers or memory pairs beyond the declared
scope (W4 shows that pointer memory matters). K-ANC (*k* = 1 vs 2) is the extension checkpoint: a
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
∈ (0, 1) with ψ ~ *w*ρ₁ + (1 − *w*)ρ₂. The generated weights at a scope are fixed as the dyadic *k*/2^*m* with *m* ≤
b_r together with every branch probability the reachability layer prints at b_h (non-dyadic under heralding, K-REACH),
printed with the scope. Purity is never judged by the underlying ontic distribution. A state whose
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
- (v) **declared resources**: which clean ancillas exist, in which states and how many, and any pointer or record
  policy (Option A's PP), are stated as independent postulates beside Π, not as unstated absences.

A milestone pass whose model fails R-MENU is printed "pass for the declared operation set; R-MENU fails at (i)–(v)".
It does not count toward the governing question. K-MENU (§5) must fail (ii).

**Two failure classifications, kept distinct.** An explicit violating preparation is **M0 lost**. An operation
restriction that is stated but not independently justified is **R-MENU unmet**, even when M0 holds within the
restricted model. "Only the declared read coupling may write hidden cells" is largely a menu; it counts as a principle
only if derived, e.g. from the substratum dynamics, which is open (§4, claim table). Under Option A's revision-1 rule
ρ₀, M0 is lost by K-SYMP's witness. Under Π_ω, M0 is decided by §4.1 for each PP form; PP and the clean-resource
declaration are postulates under (v), so R-MENU is printed green on the record carrier only.

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

**M1. An operationally pure composite with a mixed marginal, stable under an independent spectator.**
- *Question:* is there a composite AB of the model and a pure ψ ∈ Prep(AB) (§1.5) whose A-marginal is not pure, and
  whose purity survives adjoining an independently prepared spectator system (the clause below)?
- *Spectator-stability clause (draft; the owner confirms it at freeze).* Let S be one system of the model's smallest
  declared system type (for Option A one toy bit with its declared interface; for a card theory one hidden slot). For
  every pure σ ∈ Prep(S), the product ψ ⊗ σ (an ABS preparation equivalent, §1.3, to one whose ontic distribution is
  the product of representatives of ψ and σ) must lie in Prep(ABS) and be pure there, on the same readings as ψ.
- *Why the clause.* A classical theory without preparable product states passes M1 as worded without it. The card
  theory Π_B of `design/cards/` (one shared depleting deck, destructive reads) has a simplex for every state space and
  no preparable non-monochrome product state; its M1 witness E(RRRB) is a vertex of that simplex whose A-marginal is
  not a vertex, and its purity is global: it holds only while AB holds every card in play [rec, design/cards at
  `edf17209`: `CARDS-REPORT.md` (b), (c), H-1, H-2, H-9, corrected in place after `REVIEW-CARDS-a9af8ef0.md`, ACCEPT
  WITH CORRECTIONS, N7–N8; corrections not yet re-reviewed]. The bare M1 rule therefore does not separate a simplicial
  theory without products from a quantum-like composite.
- *Two readings of the clause, and the choice.*
  - (P) *Product preparability:* the model admits product preparations of A and B, at least α ⊗ β ∈ Prep(AB) for the
    local pure states α, β involved in ψ's marginals.
  - (S) *Spectator stability:* as stated above.

  (S) is adopted. It is a property of the witness itself: it asks whether ψ's purity is a global artefact, which is
  exactly how Π_B passes the bare rule (H-2: one unrevealed spectator card makes AB mixed). (P) is a property of the
  menu, which a model could meet with products unrelated to the witness, and its scope depends on which decomposition
  of ψ's marginals names the "involved" states; the decomposition is not unique (the card witness's A-marginal has two,
  ½E(RR) + ½E(RB) and ¾E(RRB)|_A + ¼RR), a free choice that §A.29 rejects. (S) contains the product preparability that
  bears on the witness, since ψ ⊗ σ is itself a product preparation of AB with S, and it is stated in the interface's
  own terms (§1.1's independently supplied ancillas and fresh bath). It shares an ingredient with the corpus's "inert
  spectators" condition (`papers/GR.md:216`, item (iii)); that is a shared ingredient, not an identification. (P) is
  printed as a reported line and decides nothing.
- *Rule:* the M1 block prints two lines. The bare-witness line: the count of pure ψ ∈ Prep(AB) with a mixed A-marginal,
  ψ's purity certified over all of Prep(AB) at the declared budget and across the model. The clause line: for each such
  ψ, each pure σ ∈ Prep(S) with the certificate that ψ ⊗ σ ∈ Prep(ABS) and is pure there, or the first σ for which it
  fails. PASS iff some exact witness satisfies the clause. FAIL iff exhaustive enumeration at the declared sizes finds no
  witness satisfying it; a FAIL with a nonzero bare-witness count is printed "M1 witness without spectator stability".
  PARKED if the enumeration of Prep(AB) or Prep(ABS) exceeds §8's bound.
- *Establishes:* the model escapes the node-8 composition obstruction at that size, with a witness whose purity is not
  an artefact of the absence of independently prepared systems.
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

## 4. The first candidate model: Option A, a bounded calibration (Q1, Q10)

Model A calibrates the engine, the record lifecycle and M0 on a model whose closure is expected to restate Spekkens'
toy theory. It is not offered as an answer to the governing question. Option B follows on the same engine (`NOTES.md`).

**System, coupling, principle.**
- *System T.* Record cells h ∈ ℤ₂^{2n} (*n* toy bits) with the standard symplectic form ω; φ = identity; the fixed
  prior on h is uniform; bath bits follow the counting measure. Pointers and memory pairs are declared below.
- *Read coupling (a model postulate of Option A).* C_u acts on h and one pointer (Q visible, P hidden): Q′ = Q +
  ω(u, h), h′ = h + P·u, P′ = P, for u ≠ 0. With Q = 0 and P fresh and then discarded it is R_u (x the pointer's Q,
  r its P): x ^= ω(u, h), then h ^= r·u. C_u is symplectic for every u; with P known the displacement is known and the
  read loses no information [rec, owner check; coordinator re-check 2026-10-21, exact].
- *Π_ω, mechanical (B3).* Carrier: the record space ℤ₂^{2n} only. Ops(Π_ω) is the normalizer of the read family in
  Sym(ℤ₂^{2n}): every bijection g of the records, identity on every other cell, such that for each u ≠ 0 there are
  u′ ≠ 0 and a bijection V of the pointer's visible cell with g R_u g⁻¹ = V ∘ R_{u′} as stochastic maps. It is computed
  by exhaustive backtracking over bijections of the carrier, the predicate checked on partial assignments; no structural
  lemma is used for completeness. [W, to be reviewed]: the clause forces g(k + u) = g(k) + σ(u) for all k and u ≠ 0, so
  σ is additive and g affine, and the readout part gives ω(σu, σk) = ω(u, k); hence Ops(Π_ω) = ASp(2*n*, 2). The run
  prints the group's order beside this; a mismatch is reported, not repaired. At *n* = 1 every one of the 24 bijections
  of ℤ₂² is affine symplectic, so Π_ω excludes nothing there; its first content is K-SYMP's swap at *n* = 2. Maps on
  pointer, memory or bath cells other than C_u and the copy are outside the carrier and are not operations; that
  exclusion belongs to the pointer policy, not to Π_ω. R-MENU (ii) is computed on the record carrier and is not claimed
  on the full carrier.
- *ρ₀ (revision 1), kept only as K-SYMP's arm:* a record bijection mapping the readable functionals onto themselves,
  such as the non-symplectic swap p₁ ↔ q₂ of K-SYMP's witness.

**Pointer policy PP (R-MENU (v); an independent postulate, Q11).**
- *Independence (both forms).* A pointer is supplied with Q = 0 and P with Pr(P = r | h, H) = ½ for the current target
  h and the accessible history H. A discarded pointer stays unavailable: no later coupling, readout, map or bath draw
  involves its P.
- *PP-1, single use (the default).* Each pointer takes part in exactly one coupling step; its Q is read (κ4) and the
  pointer is discarded.
- *PP-2, the back-acting copy (the tested alternative).* A pointer may be reused if every retained reading passes
  through the copy X′ = X + Q, P′ = P + Y, with (X, Y) a fresh memory pair, X visible at 0 and Y under the independence
  clause and never accessed afterwards. The pointer's Q is not otherwise an accessible record. Memory pairs are neither
  reused as pointers nor exchanged.
- Neither form follows from symplecticity or from Π_ω. M0, M1 and M2 print one line per form.

**Clean resources (declared; each withholding is a postulate, R-MENU (v)).** The only clean cells are the pointer Q
cells (*b_p* of them) and, under PP-2, the memory X cells (*b_m*), each at 0 and used only under PP. No other clean cell
exists: no clean hidden cell, and no further clean visible cell that any operation can bring into contact with a
pointer or the records. Hidden cells and pointer and memory conjugates are supplied only under the counting measure.
Two counts are postulates of model A's interface, declared separately as §1.1 requires: (i) the number of visible
read-out sites, the *b_p* pointers and, under PP-2, the *b_m* memory cells (coin cells are excluded by §1.2); and (ii)
the number of clean coordinates, *b_p* + *b_m* (the Q and X cells), none supplied with a clean conjugate. These are the
counts of the declaration above, which they leave unchanged. Model A has clean coordinates and no clean pair, the
analogue of the lattice case in which two visible sites with one clean coordinate each can learn. Withholding a second
clean pair does not by itself bound what is learnt, since in the lattice a second visible site with no clean coordinate
can lift L1. Nor does a single read-out site, since a second clean pair read through one site can also lift L1. Both
counts are therefore declared [rec, design/emb at `3f11c8f7` (tree `6afbdab5`), corrected; re-review ACCEPT WITH
CORRECTIONS; N1–N7 applied in the commit that adds this line]. L1 is stated for a read-out that is a whole canonical
pair (the site-level partition); model A's pointer, Q visible with P hidden, is outside its hypotheses, so this
declaration rests on the two postulates, not on L1.

**Implementation (B6).** M0–M2 run on the abstract pointer model above, not on a lattice construction. The disclosed
construction C1 delivers only the read of the toy's current u coordinate within its search bounds, so model A's free
choice of u is an assumption. AP-1 to AP-5 [rec, design/c1] are assumptions of this implementation: AP-1 (fresh kick
source at every read), AP-2 (one step of contact), AP-3 (choice of read), and for PP-2 AP-4 (no retention except
through the back-acting copy) and AP-5 (memory conjugates fresh, never accessed).

**M0's restriction (B1; Kₙ form, Q14).** At each evaluation point and for every nonzero-probability accessible record
r (§1.1), the conditional distribution P(h | r) of the retained toy coordinates h, with the P of every used pointer
(and under PP-2 every Y) marginalized, lies in Kₙ. Here h consists of whole retained toy pairs. Kₙ is closed under
marginals onto any set of whole pairs, but a single coordinate of a pair lies outside its definition.
- **Kₙ** is the convex hull of the uniform distributions on affine subsets of ℤ₂^{2*n*} whose constraint space is
  isotropic under the symplectic pairing of the n toy pairs. There are 7 such uniform states at n = 1 and 91 at n = 2
  (`design/kn/kn_controls.py`). For one pair, K₁ = {p : p_x ≤ ½ for each x}.
- **Membership** is decided exactly. The test is an exact rational linear-feasibility problem over those uniform states,
  and its result is printed with a certificate: the mixture weights if P(h | r) is a member, a separating functional if
  it is not.
  - Neither direction is accepted without its certificate.
  - Every certificate is re-verified by code separate from the solver.
  - A separating functional is valid only against the complete generator list. That list is therefore checked against
    the counting formula before any verdict: 7, 91, 2,467 and 150,451 uniform isotropic states at n = 1–4.
  - Equivalently, the Lagrangian cosets can serve as generators: 6, 60, 1,080 and 36,720. Every uniform isotropic
    state is an equal mixture of them (`design/kn/review/`).
- **Diagnostics, deciding nothing:** the support size, the maximum point probability, the optimal guessing probability
  of each toy coordinate, and each single-toy marginal's K₁ membership.
- **Coarser records.** Kₙ is convex. A coarser record's conditional distribution is a mixture of finer ones; for
  example, marginalizing a pointer P mixes the P(h | r, P) with weights P(P | r). So marginalizing or discarding never
  creates a violation, though it can hide one (W1, W6).
- **Diagnostics feed no verdict** (I-19).

Evaluation points: after each completed read-and-discard (PP-1) or read-and-copy (PP-2), and at every stopping time of
every protocol, heralded branches included, a pointer still present counting as used. The joint (h, P) form of
revision 2 is withdrawn, with its claim that a pointer exchange is a permitted non-violation: Q is visible, so an
exchange followed by a readout determines the pair (W3′). The joint support and the number of determined record
functionals are printed as diagnostics and decide nothing. The restriction is an invariant to test, neither a
general necessity nor a sufficient condition for purification.

**Disclosed baseline (pre-freeze design inputs; none is a verdict of this node).**
- *Pre-freeze review of 6cf71e0e* [rec, exact scripts kept off-repo]: W6 (two single-use complementary reads, joint
  support 2 < 4), W1, W3′, W4 (one pointer reused three times: toy point mass with probability 1), W5 (exchange before
  single use: toy support 1), W2 (transvection: toy support 1). Under PP-1 without pointer-internal maps the closure
  reaches exactly the isotropic subspaces of ℤ₂^{2*n*}, 4, 31 and 514 at *n* = 1, 2, 3, and never violates the toy
  form. Counted as states, an isotropic W with outcome values on W (a coset of W^⊥), they number 7 and 91 at *n* = 1,
  2 [rec, owner 2026-10-21], K-SPK's 6 + 1 and 60 + 30 + 1. The counts agree: 1 + 3·2 = 7, 1 + 15·2 + 15·4 = 91.
- *C-i* [rec, design/c1 at `49033a3e`, reviewed ACCEPT WITH CORRECTIONS], covering the whole record lifecycle (C1-REPORT
  §9.1). Under the region partition a visible coordinate's lattice conjugate is visible, so "Q visible, P hidden" has no
  lattice referent; the kick comes from a bath site; C1 reads only the toy's current u coordinate. The free copy and
  free retention come from the interface rule (§1.1: κ4 readout, feedback on all records, visible permutations), not
  from the lattice. The history used by C-i's waiting counterexample (toy point mass at step 4) is the interface's
  permanent record. The back-acting copy is not realized by the lattice dynamics in the searched space; in the abstract
  model it gives support 2 on W4 and no point mass over the bounded alphabet of C1-REPORT §9.2 (iv).
- *emb* [rec, design/emb at `3f11c8f7` (tree `6afbdab5`), corrected; re-review ACCEPT WITH CORRECTIONS; N1–N7 applied
  in the commit that adds this line]:
  - L1: one visible read-out site with one clean pair never completely learns a toy pair of prior support 4 (site-level
    partition, every graph, t and symplectic evolution). It rests on two separate limits, one read-out pair and one
    clean pair; relaxing either alone can lift it, and neither relaxation does in every arrangement. One clean pair
    with two visible sites can learn (9, 96 and 1650 of 24, 768 and 30 720 labelled cases at *n* = 3, 4, 5; at *n* = 3
    the path 1–0–2 with the FULL site 0 in the centre, R = {0 FULL, 1 NONE}, toy 2, t = 2), and two clean pairs read
    through the pointer alone can learn (W-E2). Two clean coordinates with no clean pair can also learn (one clean u
    coordinate at each of two visible sites: 6, 24 and 300 cases at *n* = 3, 4, 5).
  - Complete learning of *m* target pairs needs at least 2*m* clean coordinates and at least *m* visible pairs (L2).
  - In some arrangements two clean visible sites determine the current toy state from the current visible cells alone,
    at isolated stopping times (W-E2, t = 4 and 12 of period 16); what is learnt there is a bath mode the pointer
    shares. In others they never do: a memory chain behind the pointer on a path, and the cycles, grids and cube
    with |R| = 2; at *n* = 6 with |R| = 2, 857 of 8524 cases learn. Retained records are shown only under external gating
    (W-E3, AP-2).
  - C-i's waiting counterexample depends on external history (K-EXTHIST), as C1-REPORT §9.1 records; emb computes the
    dependence exactly.
  - No decision rule rests on these until a diff check confirms the re-review's required correction N1 as applied,
    which the re-review makes its condition for citing the findings.
- *Biased state* [rec, owner 2026-10-21]: (3/8, 3/8, 1/8, 1/8) on one toy bit, a ½-mixture of a two-point state with
  the uniform state, has no purification by its finite toy-system composites in the repaired family. Control K-BIAS
  (§5), carried to Option B. The obstruction comes from the family's affine operation rule (Π_ω, §4: Ops = ASp(2*n*, 2)),
  not from its size and not from OI access. In the qubit calibration, H on two qubits followed by one non-affine
  configuration exchange |110⟩ ↔ |111⟩ gives a pure three-qubit state whose target marginal is exactly diag(3/4, 1/4)
  [EC, `design/map/MAP.md`]; that construction uses H, which model A does not have.

**Claim table.** Main.md:290 [corpus]: "$$u'_x = \sum_{z \sim x} u_z + v_x, \qquad v'_x = u_x ,$$". Its matrix
M = [[L, I], [I, 0]] satisfies MᵀJM = J for J = [[0, I], [I, 0]] because Lᵀ + L = 2L = 0 over F₂ [rec, coordinator
check 2026-10-21, exact; a non-symmetric L fails].
Main.md:320 [corpus]: "All of this concerns the realization displayed above and is not a property of arbitrary finite
bijections."

| claim | support |
|---|---|
| the displayed binary update preserves a symplectic pairing | established algebraically [rec, owner check; coordinator check 2026-10-21] |
| Option A's read-and-disturb rule admits a symplectic implementation | in the abstract pointer model [rec, owner check; coordinator re-check 2026-10-21]; on the lattice for one read functional, with a bath kick, up to stated corrections [rec, design/c1] |
| OI's available operations and resources enforce that rule and its restriction | open; PP and the clean-resource declaration are postulates |

**Further declarations.**
- R-flag R-yes; Bell branch local; joint operations C_u with u ∈ ℤ₂^{2*n*}. Smallest realization for C5-P: *n* = 2;
  sizes *n* ≤ 4 (Q5).
- *Expected M3 consequence.* Under Π_ω and PP-1 model A is expected to be close to Spekkens' toy theory, which has a
  preparation-noncontextual model [Q, pending PC-SPK], and so is expected to FAIL M3. With reuse and free readout the
  closure is classical full access (W4) [rec, review of 6cf71e0e], where M3 also fails by Lemma A.
- *Postdiction, at most CONFIRMING.* The probability that two reads of ω(u, ·) agree around a read of ω(v, ·), for
  ω(u, v) = 0 and 1, against the quantum value of the Pauli sequence; a mismatch is a miss. It is built into the read
  coupling (MC6 already reproduced sequential Pauli records), so a match is at most CONFIRMING (§A.29). Also
  prerecorded: in its local branch the model gives |S_CHSH| ≤ 2 for every composite, a raw-direct conflict with
  loophole-free Bell tests [Q].

### 4.1 The decisive first question (M0)

- *Question:* does the closure of §1.2 from the fixed prior, with clean resources (g1), couplings (g2), feedback (g3),
  waiting (g4), discarding (g5) and heralding with back-action (g6), under Π_ω, the clean-resource declaration and PP-1
  or PP-2, retain M0's restriction (§4) at every evaluation point? This is the closure task C-ii; C-i is the disclosed
  design input above.
- *Scope S = (n, k, b_p, b_m, b_r, b_h).* *n* toy bits; *k* ancillas; *b_p* pointers supplied; *b_m* memory pairs (0
  under PP-1); *b_r* fresh uniform bits, counting every pointer P, every memory Y and every coin; *b_h* heralding
  events. *Ordinary conditioning* records an outcome and keeps every branch, each evaluated separately; it costs no
  budget. *Heralding* keeps a subset of one operation's outcomes and renormalizes, yielding a new preparation; each such
  selection costs one unit of *b_h*. Deterministic caps *s_max* (closure states) and *d_max* (levels) are fixed at
  freeze (Q5).
- *Completeness certificate.* Either (a) a fixed point of the breadth-first closure search over branch states (the
  exact conditional distribution on the cells present, the remaining budgets, the pointers present), every generator
  applied to every state, which covers feedback; or (b) for fixed linear dynamics with no other generator, an exact
  period M^k = I, which covers every stopping time. Completeness is never inferred from Lemma W or W's stabilization,
  and no written characterization is a certificate.
- *Rule.* **retained** iff a certificate is printed and every state of the closure satisfies the restriction at every
  evaluation point. **lost** iff an exact witness violates it, printed as its generator sequence with its success
  probability and post-measurement state. **PARKED** iff *s_max* or *d_max* is reached first, printed with the
  completed level and state count. Each line names its PP form and S.
- *Required for "retained":* K-CLN-A, K-SYMP's ρ₀ arm, K-SYMP2, K-MEM4, K-MEM5, K-POS-RET, K-PIND, K-REUSE and K-PEX
  each print "lost" with its witness, a separating functional for the Kₙ test, and support as a diagnostic; K-CLN,
  K-CLN0 and K-POS are green; and the Kₙ test classifies K-BIAS-MASK, K-COMP2, K-MIX2 and K-CORR2 as stated, each with
  a verified certificate (§5).
- Passing these controls validates the checker's sensitivity. It does not prove closure.
- *Scope:* either outcome concerns the specified model, PP form and S (K-ANC). "lost" fails R-MENU (iii) and names the
  operation responsible; M1–M5 still run on the closure as generated. "retained" establishes neither M1, M2 nor row 3
  of the claim table.

***

## 5. Controls (each computed exactly; roles explicit; a red control voids its milestone)

| id | role | construction | must |
|---|---|---|---|
| K-QPOM | positive (M3, M5) | qubit: ρ_b = ½(I + ((−1)^{b₁}X + (−1)^{b₀}Z)/√2); D₀ = Z, D₁ = X | ½(ρ₀₀+ρ₁₁) = ½(ρ₀₁+ρ₁₀) = I/2 as matrices, which is the complete invariant for every POVM, ancilla and composite; success = (2+√2)/4 exactly in ℚ(√2) |
| K-PNC | calibration (threshold) | exact LP over ontological models on the four response pairs with every deterministic response function, PNC imposed (MC6 P3 recomputed) | maximum exactly 3/4; without parity obliviousness, 1 |
| K-CBIT | countercontrol (M3) | classical bit, full access | maximum POM success with exact parity obliviousness = 3/4, attained by m = b₀ |
| K-HL0 | countercontrol (M1, M3; §1.4 case b) | classical bit plus a hidden preparation label that no allowed experiment reads (R-no, response-irrelevant) | preparations differing only in the label are equivalent; POM ≤ 3/4; M1 and M3 FAIL |
| K-HL1 | countercontrol (§1.4 case a; premise check) | K-HL0 with a coupling step that reads the label | label-different preparations inequivalent; the §1.4 premise check runs on every encoding; premise-meeting encodings ≤ 3/4; M3 not PASS |
| K-SPK | calibration (M1, M2, M3) | Spekkens toy bit, original form (MC8 PREREG §6.5 reading; 6 + 1 states; 60/30/1 for two) | M3: POM ≤ 3/4, verified by computing W's rank and the maximum, not assumed; M1 (bare-witness and clause lines, spectator one toy bit) and M2 printed for "the seven-state single-toy-bit menu with the tested one-toy-bit partner" and for "its convex closure, against the tested pure joint states", against the two readings of §0 |
| K-MENU | countercontrol (R-MENU, M5-L) | MC6 P5: destructive complementary readouts on ℤ₂², Y withheld, generated preparations; and its *w* = 1 member (the gbit). Stated Π_K: a coupling step reads one nonzero linear functional of the two cells and refreshes a complementary one from the bath, so Ops(Π_K) contains the Y readout (the control's Π, not Option B's) | passes M3 for its declared set; R-MENU (ii) fails, naming the withheld Y readout; at *w* = 1, M5-L FAIL (POM = 1 > (2+√2)/4) |
| K-PR6 | countercontrol (M4, M5-L) | MC7 LE(1,1) / MC6 B2 [rec]: A = λ, B = λ ⊕ ab | M4 PASS with S = 4 and no-signalling; M5-L FAIL |
| K-BL | preserved result | every local-branch composite of the model | |S| ≤ 2 exactly; otherwise the run is VOID |
| K-CL | countercontrol (M1, M2) | classical bit pair, full access | M1 FAIL; Pur-E fails for every mixed state |
| K-QSTAB | positive (M1, M2) | MC8 §6.5's stabilizer instance (7 one-qubit and 91 two-qubit states, ℚ(i, √2)), and for M1's clause its three-qubit products ψ ⊗ σ with a one-qubit spectator, generated by the instance's own operations (the extension fixed at freeze) | M1 PASS under the clause; Pur-E and Pur-U hold for A = one qubit |
| K-CARD | countercontrol (M1's spectator-stability clause) | the card theory Π_B of `design/cards/` (one shared deck of known composition, MC-1 to MC-4; destructive reads; heralding, feed-forward and discards), rebuilt in this engine, at the realizations with a 3/4 witness and at least five cards (3R2B, 4R1B, 3R3B, 4R2B, 5R1B; A = B = 2 hidden slots; S = 1 hidden slot) | the bare-witness line is nonzero (E(RRRB) on A = {a1, a2}, B = {b1, b2}); under the clause M1 FAILs, ψ ⊗ σ ∉ Prep(ABS) for both pure σ, printed "M1 witness without spectator stability"; reading (P) also fails (no non-monochrome preparable product state). Computed by this engine, not read from design/cards' outputs |
| K-N8 | preserved result (engine) | node 8's eight classes under node 8's menu; node 8's relation is depth-2 enumeration, node 9's is Lemma W at unbounded depth, so the two relations are first compared on each carrier; reference MC8 `probe/p8s1.r2.run1.out`, sha256 `b5ce288c3ed13658198a3a605387a06d76e6270b18923d6129350265426bd951`, at `78913467` (reviewed, ACCEPT WITH NOTES; carries the N1/N2 countercontrols); its 46 realization lines equal r1's byte for byte [rec, coordinator check 2026-10-21, sha256 and line comparison] | the eight Pur-E/Pur-U answers reproduced wherever the relations coincide; where W separates states that depth 2 does not, the changed answer is reported as a refinement with its separating sequence, not as a halt |
| K-ANC | engine; extension guard (§1.3) | equivalence at *k* = 0, 1, 2 ancillas | any change from *k* = 1 to *k* = 2 halts (PARKED, gap named); every equivalence-dependent line prints its *k*; a pass is evidence for the tested extensions only; no line claims *k* > 2 without a reviewed proof |
| K-REACH | engine (reachability, §1.2) [rec, owner check 2026-10-21] | the example of §1.2 | with no heralding budget the reachability layer prints PARKED while W has dimension 2 after one round; at b_h = *j* ≥ 1 it lists exactly *j* + 2 conditional states (2^*k*/(2^*k*+1) for *k* ≤ *j*, and δ₁), 1 at *j* = 0 |
| K-HERALD | engine (g6) [rec, owner check 2026-10-21] | fair hidden bit h, pointer x = 0, bath bit r. Arm 1: x ^= h. Arm 2: x ^= h, then h ↔ r | both arms: Pr(x = b) = 1/2. Arm 1: state given x = b is h = b. Arm 2: state given x = b is h uniform |
| K-CLN | countercontrol (M0 detector) [rec, owner check 2026-10-21] | fair hidden bit, declared clean bit at 0, swap allowed, no heralding; restriction: h is not a point mass | M0 prints "lost" with the swap as witness |
| K-CLN0 | positive (M0 detector) | fair hidden bit, no clean ancilla, bijections on h only, no readout; same restriction | M0 prints "retained" at a fixed point |
| K-CLN-A | pressure test (M0) | Option A, *n* = 1, plus one clean hidden bit with the swap declared allowed for this test (as in K-CLN); a direct swap leaves a toy state in K₁, so first a heralded read of q, keep 0, then the clean bit swapped into p: a point mass, outside K₁ [rec, coordinator check 2026-10-21, exact] | M0 prints "lost" with that two-step witness |
| K-SYMP | countercontrol (M0, operation rule) [rec, owner check 2026-10-21] | Option A, *n* = 2, h = (q₁, p₁, q₂, p₂) uniform: read q₁, keep 0 (support 8); read q₂, keep 0 (4); ρ₀'s swap p₁ ↔ q₂ (4); read q₂, keep 0: support 2 < 4, branch probability 1/8 [rec, coordinator check 2026-10-21, exact replay] | under ρ₀, M0 prints "lost" with that witness; under Π_ω, the swap p₁ ↔ q₂ is absent from Ops(Π_ω) and the witness is excluded |
| K-SYMP2 | diagnostic (M0 detector) [rec, owner check; coordinator re-check 2026-10-21] | Main.md:290 on two sites as φ (u₁′ = u₂ + v₁, v₁′ = u₁, u₂′ = u₁ + v₂, v₂′ = u₂); visible site clean at (0, 0), hidden site uniform, as the toy | under every rule, M0 prints "lost" with the two waiting steps as witness (hidden support 1) |
| K-MEM4 | countercontrol (M0 detector) [rec, owner report 6; coordinator check 2026-10-22] | Main.md:290 on the edges (0, 1), (1, 2), (0, 3); site 1 hidden, sites 0, 2, 3 visible; core uniform, memory site 3 at (0, 0); one whole-site read at t = 3 (`design/owner-checks/report6/`) | M0 prints "lost" with hidden support 1; the preparation's known constraints are not isotropic |
| K-MEM5 | countercontrol (M0 detector) [rec, owner report 7; coordinator check 2026-10-22] | Main.md:290 on the edges (0, 1), (1, 2), (0, 3), (1, 4); site 1 hidden; u₃ = u₄ = 0, all else uniform; one whole-site read at t = 3 (`design/owner-checks/report7/`) | M0 prints "lost" with hidden support 1; the preparation is isotropic, but the deciding records V₀ ⊕ V₂ and U₀ pair to 1 |
| K-POS | positive (M0 detector) [rec, owner 2026-10-22; coordinator check] | K-MEM4's and K-MEM5's preparations, with a record policy admitting only the visible u coordinates at one terminal time t, for every t in the period (10 and 16) (`design/owner-checks/report8/`) | M0 prints "retained": every terminal record leaves the hidden pair in K₁ at every t, weights included [review check, `design/kn/review/`]. For K-MEM5 this follows from the compatible-records argument; for K-MEM4, whose preparation is not isotropic, it is a checked property of the example |
| K-POS-RET | countercontrol (M0 detector; records across time) [rec, owner 2026-10-22; coordinator check] | K-POS's preparations, with the visible u coordinates at t = 2 retained undisturbed and read together with those at t = 3 | M0 prints "lost" with hidden support 1 in both. Each snapshot is isotropic and their union is not, since v_x(t) = u_x(t − 1) |
| K-BIAS-MASK | countercontrol (M0 test, weights) [rec, owner 2026-10-22; coordinator check] | one toy pair given directly as a distribution, not as a reachable preparation: a line support with weights p, 1 − p, for p ∈ {1/4, 99/100}, and p = ½ as its paired positive control (`design/kn/`) | for p ≠ ½: support 2, so the support diagnostic is met, and Kₙ-M0 prints "lost" with a separating functional. For p = ½: "retained" with mixture weights |
| K-COMP2 | countercontrol (M0 test, joint compatibility) [rec, owner 2026-10-22; coordinator check] | two toy pairs given directly: uniform on q₁ = q₂, p₁ = 0, with p₂ free (`design/kn/`) | support 4, maximum point probability ¼, and both single-toy marginals in K₁, yet Kₙ-M0 prints "lost": the two constraints have bracket 1, so no isotropic uniform state has support inside the set. A checker that tests only support, point probability or marginals fails this control |
| K-MIX2 | positive (M0 test, mixtures) [rec, review of `1dcbde1d`] | two toy pairs given directly: ½U[q₁ = q₂ = 0] + ½U[p₁ = p₂ = 0]. The support has 7 points and is not an affine set | Kₙ-M0 prints "retained" with mixture weights. A checker that accepts only uniform isotropic states, or requires an isotropic affine support, fails this control |
| K-CORR2 | countercontrol (M0 test, weights on a compatible support) [rec, review of `1dcbde1d`] | two toy pairs given directly: support q₁ = q₂ = 0, weights 3/8, 1/8, 1/8, 3/8 on p₁p₂ = 00, 01, 10, 11 | both single-toy marginals in K₁, and the support is isotropic affine, yet Kₙ-M0 prints "lost" with a separating functional. A checker that tests support containment plus marginals fails this control |
| K-CLN, K-CLN0 note | — | — | their restriction is "h is not a point mass"; they exercise the M0 search, not the Kₙ membership test |
| K-PIND | countercontrol (PP independence) | Option A, *n* = 1, PP-1, the pointers' P also written into accessible visible cells | M0 prints "lost": with the displacement known, a read of q and a read of p leave toy support 1 |
| K-REUSE | countercontrol (PP single use) and positive arm (PP-2) | W4: one pointer, reads of p, q, p. Arm 1: reuse with free readout. Arm 2: PP-2, the copy after each read | arm 1: "lost", toy point mass in all 8 branches; arm 2: the toy marginal in K₁ in all 8 branches (weights to be checked at execution; the support was 2) |
| K-PEX | countercontrol (pointer-internal maps) | Option A, *n* = 1, PP-1 with the pointer exchange (Q, P) → (P, Q) (W5) or the transvection (Q, P) → (Q + P, P) (W2) admitted | each arm prints "lost" with toy support 1; under Π_ω and PP both maps are absent and the witnesses excluded |
| K-BIAS | calibration (M2); carried to Option B [rec, owner 2026-10-21] | (3/8, 3/8, 1/8, 1/8) on one toy bit, generated by a ½ coin | Pur-E prints "no purification" for it against every composite at the declared sizes |

A control result that merely reproduces the formula it is meant to check is vacuous. K-QPOM computes the density
matrices from ρ_b, not from the success formula; K-PNC's LP is solved, not the value inserted; K-HERALD's and
K-REUSE's states come from the engine's joint update, not from the stated answer.

***

## 6. Productivity test (§A.31), fixed before execution

**Baseline.** The following are restatements and do not count:
- node 8's composition lemma and eight answers;
- MC6 P3–P5 and N1–N5;
- MC7's verdicts;
- Lemma F, Lemma A, Lemma K and Lemma W;
- the outcomes of K-HERALD, K-CLN, K-CLN0, K-REACH, K-SYMP, K-SYMP2, K-PIND, K-REUSE, K-PEX, K-BIAS and K-CARD, the
  calibration readings of §0, and Lemma S;
- design/cards' results for Π_B [rec, design/cards at `edf17209`]: the pure-state lemma for a known deck composition
  (exchangeability, simplex state spaces), the bare-rule M1 pass of a simplicial theory without products, and the
  positive-dependence, denominator and non-monochrome pure-state obstructions to Pur-E. An M1 or M2 outcome of a
  Π_B-type model that only restates these is not a gem;
- §4's disclosed baseline: the pre-freeze witnesses W1–W6 (W3′ included), the isotropic-subspace closure under PP-1
  (Spekkens' toy-theory closure, MC8's SPK-orig reading), the C-i and emb findings, and the biased state;
- the observations of §4: the first two rows of its claim table, the abstract pointer construction, the postdiction,
  an M2 FAIL on the biased state, and an M3 FAIL of Option A under Π_ω, which is expected [Q] and is not a finding;
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
- (d) R-MENU fails for a candidate whose principle was stated in advance, M0 "lost" included, and the computation names
  the operation or witness preparation that breaks it, the witness not being one of W1, W2, W3′, W4, W5, W6, K-SYMP's
  or K-SYMP2's. This exposes a hidden assumption, recorded as an assumption-watch marker for later nodes;
- (e) M0 prints "retained" under PP-2 with a certificate, at a scope exceeding C1-REPORT §9.2 (iv)'s bounded check,
  with every control of §4.1 green. This is sufficiency of the declared interface at that scope (Π_ω on the records,
  PP-2, the readout rule that admits the pointer's Q only through the copy, and the clean-resource declaration), not an
  attribution to Π_ω alone, and it does not establish row 3 of the claim table; output class POSITIVE. "Retained"
  under PP-1 restates the toy-theory closure and is CONFIRMING, not a gem.

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
| I-9 | exactness | `Fraction` only: ℚ(√2) as pairs (a, b) of Fractions for a + b√2, ℚ(i, √2) as pairs of those, in house, with a self-test (√2·√2 = 2, exact sign comparison); no third-party dependency; an AST scan for floats on the verdict path; KM-12 |
| I-10 | verdicts only over green controls | each milestone block is gated on its controls (§5); a red control prints VOID; KM-7 |
| I-11 | milestones never merged | separate generated blocks; a static check that no milestone reads another's status; KM-8 |
| I-12 | verdict text generated from measurements | every count and status is computed; scanned against MC8 A-1's word list (extended: "theorem", "impossible", "no-go", "universal", "for every realization"); every M1/M2 line names its preparation set and purifiers, and every M1 line its spectator system; KM-9 |
| I-13 | R-MENU is computed | Ops(Π) enumerated from Π's predicate; (v) printed; K-MENU must fail (ii); KM-10 |
| I-14 | preserved results hold | K-N8 (refinements reported, §5), K-BL, condition O, no-signalling, the C2 check printed before milestones; KM-34 |
| I-15 | determinism | two runs byte-identical; `SHA256SUMS`; no randomness; the replayed output carries no timing |
| I-16 | resource bound, deterministic | every closure and enumeration runs to fixed caps (*s_max*, *d_max* and §8's sizes); PARKED depends on the caps only; wall times go to a separate log outside the replayed output and `SHA256SUMS` |
| I-17 | literature and unreviewed design inputs never decide | each line lists its [Q] and [rec, design/emb] dependencies; a line depending on an unmet PC gate or an unreviewed report prints "provisional"; KM-35 |
| I-18 | heralding uses the post-measurement state | K-HERALD green before any preparation is generated; KM-14 |
| I-19 | the decisive closure question is decided first, by its rule | M0 block printed before M1 for each PP form, with certificate or witness; the Kₙ restriction evaluated on the toy coordinates at every evaluation point of §4, each verdict with its membership certificate (mixture weights or separating functional), re-verified by code separate from the solver; the generator census checked against the counting formula before any verdict; K-BIAS-MASK, K-COMP2, K-MIX2 and K-CORR2 classified as stated; a static check that no diagnostic (support, point probability, guessing probability, marginal membership) enters a verdict; mutants KM-38 to KM-41; K-CLN, K-CLN0 green; "retained" printed only with K-CLN-A, K-SYMP, K-SYMP2, K-PIND, K-REUSE and K-PEX green; KM-17, KM-20, KM-23 |
| I-20 | reachability decided separately from equivalence | M0 and Prep print S = (*n*, *k*, *b_p*, *b_m*, *b_r*, *b_h*), the heralding count apart from ordinary conditioning, and a certificate, never W's dimension; K-REACH green; KM-18, KM-33 |
| I-21 | Ops(Π_ω) is computed, on its declared carrier | the normalizer predicate evaluated on every candidate bijection of the records; its order printed; no map on pointer, memory or bath cells in Ops(Π_ω); K-SYMP's two arms and K-SYMP2 green; KM-19, KM-22, KM-25 |
| I-22 | Lemma S's link computed, not assumed | a linked POM/CHSH pair prints the steering table from the model's own extension, its S and marginals; K-QPOM's extension gives S = 2√2 exactly; KM-21 |
| I-23 | the pointer policy and the clean-resource declaration are enforced | PP and the clean cells printed with the digest (I-2); a static check that no operation touches a discarded pointer's P or an accessed Y; K-PIND, K-REUSE, K-PEX green; KM-23, KM-24, KM-25 |
| I-24 | each control is sensitive, not only gated | the sensitivity mutants KM-26 to KM-32 |
| I-25 | M1's spectator-stability clause is evaluated, never assumed; M1 PASS only with it | the M1 block prints the bare-witness line and the clause line separately, the clause line with S, every pure σ, and a certificate that ψ ⊗ σ ∈ Prep(ABS) is pure, or the first failing σ; ψ ⊗ σ generated by §1.2, never listed; K-CARD (bare witness nonzero, clause FAIL) and K-QSTAB (PASS under the clause) green; KM-36, KM-37 |

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
- KM-22: M0's generators without waiting (g4) (K-SYMP2 must then print "retained" and be caught);
- KM-23: P marginalized before conditioning on records that carry it (K-PIND must then print "retained" and be caught);
- KM-24: a reused pointer silently refreshed (K-REUSE arm 1 must then miss W4 and be caught);
- KM-25: Ops(Π_ω) computed on the carrier with the pointer cells (K-PEX's Π_ω arm must then find W5 and be caught);
- sensitivity mutants, each caught by its control's "must": KM-26, K-PNC's LP without the PNC constraints; KM-27, one
  ρ_b of K-QPOM with a sign flipped; KM-28, K-CBIT given a second readable bit; KM-29, K-HL0 with K-HL1's reading
  coupling; KM-30, one Lagrangian coset removed from K-SPK's joint menu (60/30/1); KM-31, K-PR6's composite declared
  local-branch (K-BL must print VOID), and its M5-L comparator clipped at 2√2; KM-32, K-QSTAB's Pur-U group cut to
  Paulis, K-CL's mixed states dropped from its Pur-E table (caught as vacuous), and K-CLN0 printed "retained" at the
  depth cap without a fixed point;
- KM-33: a heralding event counted as ordinary conditioning (K-REACH must then list the wrong count and be caught);
- KM-34: K-BL disabled (the I-14 printout must show it missing and halt);
- KM-35: a [Q] dependency dropped from a line's list (I-17's scan against the static dependency table must catch it);
- KM-36: M1 decided on the bare-witness line alone, the clause skipped (K-CARD must then print M1 PASS and be caught);
- KM-37: ψ ⊗ σ inserted as a listed state instead of generated (I-6's static scan must refuse it), and, separately,
  its purity judged against Prep(AB) × Prep(S) instead of Prep(ABS) (K-CARD's clause line must then change and be
  caught);
- KM-38: the Kₙ test replaced by support ≥ 2ⁿ (K-BIAS-MASK and K-CORR2 must then print "retained" and be caught);
- KM-39: the Kₙ test replaced by "is a uniform isotropic state" (K-MIX2 must then print "lost" and be caught);
- KM-40: the Kₙ test replaced by "support contains an isotropic support, and every single-toy marginal is in K₁"
  (K-CORR2 must then print "retained" and be caught);
- KM-41: one generator dropped from the census (the census check must halt, or a separating functional must fail
  re-verification against the full list).

***

## 8. Order, resources and replay

**Order (depth-first, §A.12):**
1. the engine and the controls: K-HERALD, K-REACH, K-CLN, K-CLN0, K-ANC, K-PNC, K-QPOM, K-CBIT, K-HL0, K-HL1, K-SPK,
   K-CL, K-QSTAB, K-CARD, K-N8, K-MENU, K-PR6;
2. the model's interface printout (Π_ω, PP, clean resources, S) and R-MENU;
3. M0, the decisive first question, with K-CLN-A, K-SYMP, K-SYMP2, K-PIND, K-REUSE and K-PEX, under PP-1 then PP-2
   (§4.1);
4. M1 (the bare-witness line, then the spectator-stability clause on ABS), then M2 at *n* = 2, with K-BIAS;
5. M3;
6. M4;
7. M5;
8. M2 at the larger sizes;
9. the mutants;
10. productivity and the independent review.

A FAIL at M1 does not stop M3 or M4, since they are separate questions; nor does M0 "lost" stop M1–M5. Each is reported.

**Resources (§A.40).** Every phase runs to deterministic caps fixed at freeze (Q5) and, on reaching one, prints PARKED
with its completed range. The caps are chosen so that the local run is expected to stay under about 60 minutes; wall
times are logged outside the replayed output (I-16). Anything larger, such as *n* = 4 enumerations or deeper decoder
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
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | the toy theory; knowledge balance; it has a preparation-noncontextual ontological model | [Q] | K-SPK is built from MC8's combinatorial reading; PC-SPK as in MC8, also before §4's expected M3 consequence is cited as more than an expectation |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | Gaussian QM reconstructed from one specific epistemic restriction on Liouville mechanics | [Q] (search summary) | PC-BRS |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | five axioms (causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning) plus purification select QM | [Q] (search summary lists the axioms) | PC-CDP (inherited from MC8 §6.8) gates M2's wording |

**Narrow claims, and only these.**
- Bartlett, Rudolph and Spekkens (2012) reconstruct Gaussian QM from one specific epistemic restriction on Liouville
  mechanics [Q].
- Spekkens (2005) excludes preparation-noncontextual models of full QM [Q].

Together these constrain the route. They do not rule out contextual, epistemically restricted constructions. Nothing
here states that epistemic restrictions in general stop at stabilizer or Gaussian physics.

***

## 10. Scope

Every negative result concerns the specified model, its interface 𝓘 (clean ancillas included), the sizes and ancilla
count computed, the declared PP form and resource scope S, and the declared readings. A FAIL does not establish that
observational incompleteness cannot yield purification, contextuality, Bell violation or QM. A PASS establishes the
milestone's stated content for that model, its preparation set and its purifiers, and nothing beyond it. Lemma W decides
equivalence exactly within the declared finite model, not reachability; beyond it, K-ANC and a reviewed extension
argument govern. Finite-model success is never classified as an exact quantum reconstruction (MC8 A-1). No equivalence
is claimed. M5's two directions are reported separately.

***

## 11. Procedure and freeze

- **Before freeze:**
  - the owner confirms §4's PP text, clean-resource declaration and Π_ω definition (`NOTES.md` QA′), and fixes the
    values of S, *s_max* and *d_max* (Q5);
  - the remaining questions of `NOTES.md` (Q6–Q9) are disposed, and node 8's `quotecheck.py` is run with a node-9
    fragment list (Q8);
  - a diff check confirms the design/emb correction N1 as applied (the re-review of `a9af8ef0` returned ACCEPT WITH
    CORRECTIONS and makes N1 its condition for citing the findings; N1–N7 applied in the commit that adds this line);
    until then its findings decide nothing (I-17);
  - the owner confirms M1's spectator-stability clause and its reading (S), with K-CARD and KM-36/KM-37 (§3, §5, §7);
  - an independent re-review of this revision against the pre-freeze checklist of the review of `6cf71e0e` runs.
- **Freeze:** the sha256 of this file is recorded in the commit message and on the guiding PR. After freeze the file is
  not edited. Changes go to `amendments/` with time, reason and state of knowledge, before the computation they touch.
  No amendment changes a decision rule in a candidate's favour.
- **After a milestone's first computation:** its rules are frozen. A later discrepancy is recorded, not repaired.
