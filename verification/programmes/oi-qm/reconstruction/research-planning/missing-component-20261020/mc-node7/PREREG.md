# Node 7 (A2 track, node 2): does a principle stated in the corpus fix the size of the nonclassicality? Preregistration

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This file is
the node's preregistration. It is written, and its sha256 recorded, before any computation on a candidate principle.
No value of S, POM success or w has been computed under any candidate. The decision rule, the tolerance, the
architecture classes, the controls and the classification criteria are fixed here; the expected numbers are not
(§A.29).

**Owner's framing (2026-10-20).** The objective is to derive why observational limits applied to a single underlying
reality produce exactly quantum behaviour, rather than to make quantum behaviour one of many possible outcomes. Central
question: can the limitations of observation themselves select the laws of quantum mechanics? Rejecting PR boxes while
allowing QM is not enough, because many post-quantum correlations lie between the quantum and PR limits. A rigorous
negative result that identifies exactly which OI principle is insufficient is a valuable outcome. Establishing the
quantum CHSH and POM boundaries, with quantum values reachable and classical models kept, is a necessary milestone, not
a derivation of QM.

**Tags.** [AT] adopted kernel theorem; [W] written argument; [EC] exact computation (to be run in step 2, none run
here); [NUM] floating-point evidence, never evidence of exactness; [L] literature, cited from memory unless stated, not
read in full unless stated; [rec] recorded in the cited record, not re-derived; [Q] quoted corpus text.

***

## 0. Base

- Thread: `research/missing-component-20261020` at `8fb6a5ec53a704cea1000e776a94e36da49d291e` (PLAN = `../PLAN.md`;
  MC6 = `../mc-node6/NODE.md` with its review outcome; MC1–MC5, N1 as in PLAN).
- `main` at drafting: `0fb020c7f39548fe13d09315da21e0c622ffb029`. `papers/`, `book/` and `verification/lean-mathlib/`
  are identical between the thread head and `main` (`git diff --quiet origin/main 8fb6a5ec -- papers book
  verification/lean-mathlib`), and `papers/` and `verification/lean-mathlib/` are identical to the thread's base
  `df9e601e`. Every file:line below holds at all three commits.
- Worktree used for drafting: a detached checkout of `8fb6a5ec`. Nothing was run in it except `git` and text search.

***

## 1. Frozen admissibility condition: one substratum, one dynamics (owner, 2026-10-20)

Every realization the node considers, for a candidate, a control, a family member or the follow-up class, must satisfy
condition **O**:

- **O1 (one state space).** There is one finite substratum state space Ω = 𝒞_V × 𝒞_H. The visible and hidden sectors
  are the two factors of a partition of Ω (Main.md:50, Lemma 2). No degree of freedom lies outside Ω.
- **O2 (one dynamics).** The realization's evolution is a composition of bijections of Ω: the fundamental step φ and,
  for protocols, configuration bijections of Ω selected by visible settings (κ2). Bijectivity is checked on all of Ω.
  The hidden coordinates change only through these bijections. There is no separate rule for the hidden sector: no
  stochastic update, amplitude, phase, Born weight or instrument attached to hidden data.
- **O3 (one source of probability).** Record probabilities are prior-weighted counts of microstates: P(record) =
  μ({ω ∈ Ω : the protocol's bijections carry ω to a configuration with that record}). The prior μ on Ω is the only
  probabilistic input, and it is the prior the candidate admits (§3). The visible initial configuration (settings,
  preparer cells and pointers included) is a point mass fixed by the protocol: it is the prior's visible marginal, not
  the output of a step. The hidden marginal μ_H does not depend on the settings (measurement independence, Main.md:82).
- **O4 (configuration readout).** Records are configurations of visible cells, read after the protocol's bijections
  (κ4).

A realization that violates O is not admissible under any candidate and is not counted for or against any candidate.
The condition is measured by checkpoint I-2 (§8).

***

## 2. The two families and the scenarios

The families are `mc-node6`'s B2b and P5 (MC6 §2.1, §2.2; `probe/p6.py` lines 281–330 and 480–530 [rec]), restated as
architectures so that the prior weight is produced by an O-admissible prior rather than entered by hand.

- **Long edge, LE(n, k), 1 ≤ n, 0 ≤ k ≤ n.** Visible cells: settings a, b; outcome pointers q, r; preparer cells p₁, p₂.
  The visible initial configuration has q = r = p₁ = p₂ = 0 (a point mass fixed by the protocol, O3). Hidden cells: λ ∈
  {0,1}; control register u ∈ ℤ_n. Steps (each a bijection of Ω): p₁ ^= λ; p₂ ^= λ (the shared pair, as B2's l₁ = l₂ =
  λ); q ^= p₁; r ^= p₂; r ^= a·b·[u < k] (the long edge, B2's block (0, 5, 6, 4) with s replaced by [u < k]). The
  structured-prior version LE(w) is `mc-node6`'s B2b exactly: u a single bit with prior P(u = 1) = w set as a
  realization datum (Main.md:60). CHSH as in `p6.py`: S = Σ_{a,b} (−1)^{ab} E(a, b). S_max is the maximum over the eight
  CHSH expressions Σ_{a,b} (−1)^{ab ⊕ αa ⊕ βb ⊕ γ} E(a, b), α, β, γ ∈ {0, 1}; clauses (i) and (F1) bound S_max, so the
  bound is |S| ≤ 2√2 in every orientation. The Tsirelson correlation in (ii-Q) is E(a, b) = (−1)^{ab}/√2 or its image
  under one of these relabellings.
- **Destructive complementary readouts, DR(n, k).** Hidden ontic pair (b₀, b₁), fresh disturbance bits r_t, control
  register u ∈ ℤ_n; visible preparer register x ∈ {0,1}² (its value fixed by the protocol as part of the visible initial
  configuration, O3), visible pointers initially 0. Preparation: a swap of
  (b₀, b₁) with x controlled by [u < k] (a bijection; the displaced ontic pair goes to the preparer's record register,
  which no readout reads). Readout y ∈ {0,1}: pointer ^= b_y, then b_{1−y} ^= r_t (P5's step, `p6.py` lines 506–510).
  With the counting measure on the hidden cells the preparation prior is w·δ_x + (1 − w)·uniform with w = k/n, which
  is P5's `prep(x, w)`. The structured-prior version DR(w) is P5 exactly. POM success as in `p6.py`: the average over
  x ∈ {0,1}² and y of P(pointer = x_y).
- **Quantum, classical and maximal values.** CHSH: 2, 2√2, 4. POM: 3/4, (1+1/√2)/2, 1. The affine map
  POM = 1/2 + S/8 carries 2 ↦ 3/4, 2√2 ↦ (1+1/√2)/2 and 4 ↦ 1 [W, arithmetic; Spekkens et al. 2009, L].
- **A fact about the long-edge family, recorded before any candidate is examined [W].** In LE, q = λ and
  r = λ ⊕ a·b·[u < k], so E(a, b) = 1 for ab ≠ 11, E(1, 1) = 1 − 2w, and both marginals are uniform. In quantum theory,
  E(0,0) = E(0,1) = E(1,0) = 1 forces A₀|ψ⟩ = B₀|ψ⟩ = A₁|ψ⟩ = B₁|ψ⟩ (from ‖Aψ − Bψ‖² = 2 − 2⟨AB⟩ for ±1
  observables; POVMs by dilation, mixed states by purification) and hence E(1,1) = 1. So the only quantum member
  of LE is w = 0. Every member with 0 < w ≤ √2 − 1 has S ≤ 2√2 and is post-quantum. In particular LE at S = 2√2 is not
  the quantum Tsirelson correlation, which has |E(a, b)| = 1/√2 for every (a, b) [L, Tsirelson 1980; self-testing
  literature, not read in full]. This fact rests on the [W] perfect-correlation argument above, not on [L].
  Consequence for the rule: a value within ε of 2√2 in LE shows that the value is reachable, not that a quantum
  correlation is reachable. Quantum achievability is therefore tested separately, in the
  follow-up class (§4.3, clause (ii-Q)). This fact concerns the family, not any candidate. Step 2 re-checks it as
  control K-7.

***

## 3. Candidates

For each candidate: the exact corpus text, the formalization as a constraint on O-admissible realizations, why that
reading is faithful, any interpretive choice, and the parameters with how OI fixes each one.

**Parameters versus quantified data.** A *parameter* is a number the principle needs to be given before it constrains
anything (a tolerance, a temperature, a degree bound, a moment value). A parameter not fixed by OI's own structure
disqualifies the candidate as stated (Failure-as-stated, §6). *Architecture data* (carrier sizes n, thresholds k,
gates, number of cells) are not parameters: a principle admits or rejects each architecture, and its admitted set is
the union over all architectures it admits. An architecture restricted in order to obtain a value is a tuned parameter
(§6).

**Scenario silence.** A candidate whose corpus text does not address a scenario admits every O-admissible realization
in it. It then fails clause (i) for that scenario. A pass on one scenario only is reported as a partial result
("CHSH only" or "POM only") and is not a pass.

### 3.1 Lemma 3's selection of the counting measure (and the measure posit)

Corpus text [Q]:
- Main.md:56: "*On each accessible orbit the invariant measure is unique (uniform on the cycle); globally, the counting
  measure is selected among invariant measures as the maximal-entropy one — a selection principle, not uniqueness from
  invariance alone.*"
- Main.md:60: "Lemma 3 fixes the canonical measure — invariant, maximal-entropy — and the framework's baseline
  transition matrices (§2.3) and the physical realization use it. It does not preclude structured preparations: a
  realization in the sense of §3.4 carries its own fixed hidden prior $\mu_H$ as part of the realization datum … the
  counting measure is the default, not a constraint on representations."
- Main.md:62: "on the orbit of the actual microstate, the uniform measure is the unique $\varphi$-invariant measure; the
  selection among orbits is fixed by maximal entropy compatible with the observer's records".
- Main.md:708, posit (iv): "the measure selection is a maximal-entropy principle ("the maximal-entropy invariant measure
  compatible with the observer's records") — a standard but substantive epistemic postulate, not derived".
- Cycle equilibrium, the same selection read dynamically: Main.md:345 ("Born rule | Equilibrium of indivisible
  process"); Main.md:666 ("The equilibrium-of-the-cycle reading is the cosmological realization's mechanism proposal
  rather than a theorem of this paper"); book/ch18-beyond.md:34 ("Born-rule probabilities as the stationary statistics
  of the cycle").
- Computation.md:120: "the substratum measure is the unique $\varphi$-invariant maximal-entropy measure ([Main], Lemma 3
  and posit (iv) of the posit ledger), which excludes a planted-measure escape".

The texts admit five readings, preregistered as separate candidates. Main.md:60 and Computation.md:120 pull in opposite
directions (structured priors allowed as realization data, against planted measures excluded), so both directions are
kept.

- **L3-0, the realization-datum reading (Main.md:60).** No constraint: μ_H is a free realization datum and the counting
  measure is a default. Admitted: every O-admissible realization with any prior, including LE(w) and DR(w) for every
  real w. Faithful because Main.md:60 says so in terms. Parameters: none.
- **L3-A, the strict counting-measure reading (Main.md:56; Computation.md:120).** The prior on 𝒞_H is the counting
  measure on the realization's hidden carrier. Preparations act only through visible settings and bijections (no
  conditioning on records, no structured μ_H). Admitted: LE(n, k) and DR(n, k) for all n, k, and any O-admissible
  architecture with counting measure on its hidden cells. Faithful to "the counting measure is selected" read as a
  constraint, and to "excludes a planted-measure escape". Interpretive choice: the selection is read as binding on every
  realization, contrary to Main.md:60's "not a constraint on representations"; Main.md:60's reading is L3-0.
  Parameters: none. Carrier size and threshold are architecture data.
- **L3-B, the record-conditioned reading (posit (iv); Main.md:62).** The prior is the maximal-entropy measure compatible
  with the observer's records: the counting measure on Ω conditioned on the set of microstates compatible with the
  visible records at preparation time. Preparations may be heralded by records (conditioning only on records fixed
  before the settings are chosen; MC2's rule concerns available operations and is not applied to the prior). Admitted:
  L3-A's realizations plus record-conditioned ones. Faithful: "maximal entropy compatible with the observer's records"
  read with compatibility as a support constraint, whose maximal-entropy solution is uniform on the compatible set [W].
  Interpretive choice: "compatible" read as support restriction; the alternative, moment constraints, is L3-D.
  Parameters: none.
- **L3-C, the orbit-invariant reading (Main.md:56, :62; cycle equilibrium).** The prior is φ-invariant, where φ is the
  realization's whole protocol cycle written as one bijection of Ω (a clock register indexing the protocol's stages
  included in Ω): a mixture of orbit-uniform measures, with the orbits selected by maximal entropy compatible with the
  records (the counting measure restricted to the union of record-compatible orbits). Record statistics are stationary
  statistics of the cycle, as in book/ch18-beyond.md:34. Faithful: "on each accessible orbit the invariant measure is
  unique (uniform on the cycle)" with the selection among orbits as Main.md:62 states it. Interpretive choice: φ is the
  protocol cycle including a clock. A preparation cannot be structured by conditioning at one time unless the
  conditioning set is a union of orbits. Settings are visible registers that the cycle leaves fixed, and μ must be
  invariant under the cycle for every setting value. The visible initial configuration is imposed by restricting to
  orbits through it; records are read at the readout phase of the clock. If any further choice is needed to define the
  cycle, L3-C is Parked with that choice named. Parameters: none.
- **L3-D, the moment-constraint (Jaynes) reading.** The prior maximizes entropy subject to expectation constraints that
  the observer's records fix. Constraint values are parameters. If they are free, OI does not fix them and the candidate
  is disqualified as stated. If they are the target statistics, the candidate is circular and is Reproduction at best
  (§6). Preregistered so that the reading is recorded. It is not computed unless a constraint value fixed by OI is found
  in the corpus.
- **L3-PR, partition-relativity (Main.md:86), as a dependent candidate.** [Q] "*Under the canonical measure of Lemma 3,
  the emergent description is uniquely determined by the partition; any parameters of the emergent theory depend only
  on the geometric and thermodynamic properties of the partition boundary.*" Formalization: L3-A's constraint, plus the
  requirement that the realization's law be a function of (φ, partition) alone. Faithful: its proof (Main.md:88) uses
  Lemma 3 and Lemma 2 only. Rule fixed now: if step 2 finds that no corpus text fixes the "geometric and thermodynamic
  properties of the partition boundary" for the families' architectures, L3-PR's admitted set is L3-A's. It then
  inherits L3-A's verdict and is recorded as not independent. Parameters: none beyond L3-A.

### 3.2 Partition covariance of reduced descriptions (the Wigner's-friend treatment)

Corpus text [Q]:
- Main.md:668: "The framework treats the observer partition $V \subsetneq S$ as a choice, not an absolute. … each
  partition satisfying the characterization conditions produces its own C1–C4-quantum description of the remaining
  degrees of freedom. … it is a covariance property of the framework under observer-partition choice".
- Main.md:674: "**Joint description.** The marginal transition matrix … exists and is unique given $\varphi$.
  Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively."
- Main.md:676: "neither Friend nor Wigner has epistemic access to the complete state, and this epistemic limitation
  produces their respective quantum descriptions through the same mechanism in §2–§3. … observer identity is
  partition-gauge, not absolute, and framework predictions are covariant under choice of observer partition."
- Methodology.md:395: "each choice yields its own internally consistent reduced description … predictions are covariant
  under choice of observer partition."

Readings, preregistered as separate candidates:
- **PC-1, marginal consistency.** For any two observer partitions of one admitted realization, each reduced description
  is the trace-out of the same (φ, μ), and the joint description's marginals equal each party's description
  (Main.md:674). Applied to the Bell scenario with partitions V_A (wing A with its setting and pointer), V_B, and V_A ∪
  V_B. Faithful: this is the content Main.md:674 states. Parameters: none. Expected countercontrol: any two trace-outs
  of one (φ, μ) are marginals of one law, so PC-1 is expected to hold for every admitted realization; step 2 measures
  this rather than assuming it.
- **PC-2, determination by one's own partition (no-signalling form).** Each wing's reduced description is fixed by its
  own partition (Main.md:676 with Main.md:86): with the remote setting treated as an intervention outside the wing's
  partition, the wing's record law does not depend on that setting. Formally: operational no-signalling in both
  directions, P(q | a, b) independent of b and P(r | a, b) independent of a. In the POM scenario: each readout's record
  law depends only on the preparation and that readout. Faithful: a description "covariant under choice of observer
  partition" and fixed by the partition cannot vary with an intervention outside it. Interpretive choice: the remote
  setting is an intervention, not a hidden datum averaged by the prior. Under the averaged reading PC-2 reduces to PC-1.
  Parameters: none.
- **PC-3a, "quantum description" as fixed-basis representability.** Each partition satisfying C1–C4 has a Q_fb
  representation (Main.md:82: S ⟺ D ⟺ Q_fb on every finite horizon). Faithful to "C1–C4-quantum description" in the
  sense Main proves. Parameters: none.
- **PC-3b, "quantum description" as membership of the standard quantum set.** Each partition's reduced law lies in the
  standard quantum correlation set (for the composite, the quantum Bell set; for one system, the quantum
  prepare-and-measure set). This reading puts the quantum set into the principle. It is preregistered because the text
  "quantum-mechanical" (Main.md:672–673) admits it. Any pass is Reproduction by construction (§6). It also serves as
  the checker's positive control K-P (§5).

  Implementation, fixed now:
  - *Bell scenario.* The inner set is the boxes with an exhibited exact quantum realization. For zero marginals it is
    the correlators satisfying TLM, certified exactly as in (b1) (the direction TLM ⇒ quantum, §4.4). The outer set is
    NPA level 1+AB. An exclusion counts only with an exact witness as in (b2), by the perfect-correlation argument of
    §2, or by an exactly certified TLM violation (quantum ⇒ TLM, (b1)); NPA level 1 ⇒ TLM as well, since its correlator
    block is a unit-vector Gram matrix (Tsirelson's theorem), so the violation also certifies exclusion from the outer
    set.
  - *Which set decides which clause.* Exclusions in (i), (F1) and (b1) use the outer set. Admissions in (ii-S), (ii-Q),
    (iii) and (iii-𝒜) use the inner set. A box in the outer set and not the inner set is reported undetermined and
    counts for no clause.
  - *POM scenario.* The quantum set is the statistics of quantum states ρ_x and two binary measurements with
    ρ_00 + ρ_11 = ρ_01 + ρ_10, that is, parity obliviousness over every quantum measurement. Exclusion uses the
    quantum bound (1+1/√2)/2 [L: Spekkens et al. 2009, not read in full]. Admission needs an exhibited exact
    realization.
  - *Sequential records.* The delay line, the toy bit and DR sequences are admitted on an exhibited exact realization
    by projective measurements with Lüders update.
  - *OI members.* In 𝒜_POM and DR, an OI member's parity obliviousness is over its accessible readouts, as defined
    there.
- **PC-4, nested reversible re-description.** One observer's measurement, described by an observer whose hidden sector
  contains the first observer's pointer, is a reversible transformation in the realization's own operational theory.
  Formally: let Th(R) be the operational theory of realization R (states: record-law vectors of R's admitted
  preparations over its accessible protocols; transformations: maps induced by accessible bijections). For each wing
  readout β (a bijection on wing cells and a pointer), there is an accessible protocol that maps every admitted
  preparation's post-readout law on wing ∪ pointer back to its pre-readout law. Sub-readings by the accessible set:
  PC-4a, closed under inverses (κ2: the inverse of a configuration bijection is a configuration bijection); PC-4b,
  as specified by the family. Interpretive choice: this lifts "the same mechanism" (Main.md:676) from the substratum to
  the operational theory. The corpus does not state it in these terms. Parameters: none. Rules fixed now:
  - If Th(R) cannot be defined for a family without a further choice, PC-4 is Parked with that choice named as the gap.
  - Under κ2 the inverse bijection β⁻¹ is accessible and restores the microstate, so PC-4a is expected to hold for every
    realization. If step 2 confirms this, PC-4a is recorded as vacuous (over-generation) with that reason.

### 3.3 H-Bell: preparation-indexed bounded-degree long edges and the continuum-curvature condition

Corpus text [Q]:
- Main.md:392: "the natural branch-(a) target is therefore **preparation-indexed adjacency**, in which the reference
  vacuum/uniform graph remains geometric and bounded-range while a Bell preparation supplies bounded-degree long edges
  or an equivalent nonlocal response map. The open cost is not the graph-boundary area law by itself, but the
  continuum-curvature limit of those prepared graphs."
- Main.md:394: "What remains to be proved is H-Bell: the prepared graph family must preserve operational no-signaling
  and satisfy a curvature/metric convergence condition strong enough for the Ollivier--Ricci continuum step used by the
  Einstein reconstruction. … the hop-metric curvature route FAILS for the reference family, before any Bell edge is
  added … What must be re-founded is the curvature functional, on the propagation/Laplacian geometry rather than on
  shortest-path counts [SM §3.2]."
- Substratum.md:132: "the preparation-indexed graphs must (i) supply the required ontic parameter dependence, (ii)
  preserve operational no-signaling, and (iii) satisfy a metric/Ollivier--Ricci stability condition strong enough that
  the continuum-curvature step of [SM §3.1] remains valid on the state classes to which the Einstein reconstruction is
  applied. … H-Bell is therefore an explicit curvature-stability/composite-existence hypothesis".
- SM.md:152–156: the local-contamination diagnostic. The display at SM.md:154, "$$\frac{L_Nm_N}{N}\longrightarrow0$$",
  and SM.md:156, "is a sufficient sparsity condition for *typical local neighborhoods* to retain the reference graph
  geometry. … This is not a theorem that $\kappa_{OR}$ converges everywhere".
- SM.md:150: the mesoscopic Ollivier step; "On the degree-$6$ simple-cubic graph the hop metric is exactly the $\ell_1$
  metric"; route (A), "Re-found the curvature functional on the low-energy wave/Laplacian operator …
  ($\Gamma_2$/Bakry-Émery is the obvious candidate class)"; "Kelly et al. [9] control the integrated curvature limit,
  but under a Gromov–Hausdorff closeness hypothesis on the whole graph sequence, which a macroscopic metrically cheap
  preparation-indexed edge destroys outright".
- SM.md:48, :108, :110: bounded degree and the reference constraints (i)–(iii) on G(x).

Embedding used by every HB reading: LE's long edge (r ^= a·b·[u < k]) is the preparation-indexed edge. In microstate ω
the prepared graph G(ω) contains the edge {wing A, wing B} iff [u < k] = 1, so w is the probability under the prior that
the prepared graph carries the edge. Wings sit at antipodal sites of a periodic simple-cubic reference graph of side L
(degree 6, SM.md:14); the number of Bell pairs P ≥ 1 is architecture data.

Convergence as L → ∞ is decided only by a reviewed written argument [W]. The evaluations at L ∈ {4, 6, 8} are [EC]
instances and never decide a convergence clause. Without the argument, the clause is incomplete (§4.3).

Readings, preregistered as separate candidates:
- **HB-1, clauses (i)–(ii).** Admitted: long-edge realizations with ontic parameter dependence, operational
  no-signalling, and added degree ≤ D at each vertex. Faithful: the explicit clauses of Substratum.md:132 and
  Main.md:392. Parameter D: the corpus says "bounded-degree" and fixes no number. HB-1 is formalized with D universally
  quantified over finite values, which is not a tuned parameter. As a sensitivity row, D = 1 (the single added edge) is
  also computed.
- **HB-2, clause (iii) by the corpus's sufficient diagnostic, per prepared graph.** HB-1 plus, along the sequence
  L → ∞ with P fixed or growing, L_N·m_N/N → 0 for each prepared graph G(ω) (SM.md:154), with m_N as SM.md:152 defines
  it, for some schedule r_N with r_N → ∞ and r_N/L → 0 (the reading; "for every such schedule" is reported as a
  sensitivity row). Faithful: the only quantitative form of (iii) the corpus states. Interpretive choice: the
  diagnostic, which SM.md:156 calls sufficient and "not a theorem that κ_OR converges everywhere", is used as the
  condition. Parameters: none; the radius schedule is quantified as stated.
- **HB-3α, clause (iii) as curvature stability of the ensemble-weighted graph, hop-metric Ollivier functional.** HB-1
  plus: the graph whose long edge carries weight w (its probability under the prior) has mesoscopic Ollivier curvature
  converging, at every vertex including the edge's endpoints, to the reference value as L → ∞. Functional: the cited
  hop-metric mesoscopic Ollivier curvature (SM.md:150). Faithful: the functional Main.md:394 and Substratum.md:132 name.
  Interpretive choice: ensemble weighting; per-graph evaluation is HB-2 and HB-4. Note fixed now: SM.md:150 and
  Main.md:394 state that this route fails for the reference family before any Bell edge is added. If step 2 confirms
  that the condition fails at w = 0, HB-3α excludes the classical model and fails (iii). That outcome is recorded with
  its cause and is not repaired by changing the functional after the fact. Mesoscopic radius: for some schedule r_N
  with r_N → ∞ and r_N/L → 0 (the reading; "for every such schedule" is reported as a sensitivity row). Parameters:
  none beyond that schedule.
- **HB-3β, as HB-3α with a generator-based (Bakry–Émery Γ₂) curvature of the graph Laplacian, route (A) of SM.md:150.**
  Parameters: the dimension parameter N_BE of the curvature-dimension condition CD(K, N_BE). It is not fixed by the
  corpus: route (A) is unconstructed (SM.md:150), and in the graph Γ₂ literature a lattice's dimension parameter tracks
  its vertex degree rather than d (Lin–Yau [L, from memory, not re-verified]). Rule fixed now: the functional is
  evaluated at N_BE ∈ {3, 6, ∞}; HB-3β receives a verdict only if all three give the same result, and is otherwise
  Parked with N_BE named as the gap. The scale schedule is as in HB-3α. Interpretive choice: route (A) is proposed and
  not constructed in the corpus. The node uses the standard graph Γ₂ calculus (Bakry–Émery; Lin–Yau 2010 [L, not read in
  full]) with the combinatorial Laplacian and edge weights as in HB-3α. If a further choice is needed to define the
  functional (normalization, mesoscopic averaging), it is named and the candidate is parked with that gap. The choice is
  never made by its result.
- **HB-4, clause (iii) as metric closeness, per prepared graph.** HB-1 plus: for every ω of positive prior weight, the
  Gromov–Hausdorff distance between G(ω) with its hop metric scaled by 1/L and the equally scaled reference graph tends
  to 0 as L → ∞. This is the hypothesis of Kelly et al. as SM.md:150 describes it. (Bounded distance alone would be
  vacuous, since d_GH(X, Y) ≤ max(diam X, diam Y)/2 and both rescaled diameters are O(1).) Faithful: SM.md:150 names
  this as what a convergence theorem of that type needs. Parameters: none.

H-Bell is stated for Bell composites only. Under each HB reading the POM scenario is silent: every DR member is admitted
there, and a pass can only be "CHSH only".

### 3.4 Barandes–Hasan–Kagan stochastic causal locality, found under §A.19

Corpus text [Q]:
- Main.md:382–387: "their causal-independence condition constrains the stochastic law and is strictly weaker than
  factorization, which is what lets a causally local indivisible process occupy the quantum interval. A deterministic
  response-complete completion supplies more than they assume, and the surplus costs precisely the interval between
  $2$ and $2\sqrt2$."
- Explainer.md:347: "Barandes–Hasan–Kagan bound a weaker class of causally local indivisible *stochastic* processes by
  $2\sqrt2$. … stochastic causal locality belongs to the weaker reduced-law description."
- Methodology.md:393: "The stochastic causal-local indivisible construction can obey Tsirelson because its
  causal-independence condition is weaker than Bell factorization; that result is retained at the stochastic layer
  only."
- Substratum.md:430: "Bare C1–C4 or graph locality do not enforce Tsirelson."

- **CL.** Formalization: OI's reduced Bell-scenario law of an admitted realization, as an indivisible stochastic process
  on the visible configurations, satisfies Barandes–Hasan–Kagan causal independence. The corpus does not define the
  condition. The source (arXiv:2512.18105, Main ref. [24]) has not been read, and at drafting `arxiv.org` did not
  resolve from the container. Rules fixed now:
  - Step 2 attempts to retrieve the definition. If it cannot, CL is parked with the named gap "definition not
    retrieved", and no verdict is given.
  - If retrieved, the definition is quoted, and step 2 records whether it is stated on the stochastic law alone or
    through the stochastic–quantum correspondence's local Hilbert-space structure. In the second case CL puts local
    quantum structure into the principle (the operational-lifting problem Main.md:534 leaves open), and a pass is
    Reproduction (§6).
  - CL counts as an OI principle only if a corpus text asserts that OI's reduced descriptions satisfy it. At drafting
    the texts assert it of "the cited **stochastic causal-local indivisible** sector" (Substratum.md:430) and place it
    at "the weaker reduced-law description". If step 2 finds no stronger assertion, CL is classified as an external
    principle, and a pass is recorded as an external pass, never as Emergence from OI.
  - Parameters: as in the definition. Any parameter not fixed by OI disqualifies CL as stated.

### 3.5 Countercontrol candidates (expected vacuous, measured, not assumed)

- **C3 (Main.md:78).** [Q] "The hidden sector has enough distinguishable states to encode the observed conditional
  past–future information: $\log_2 |\mathcal{C}_H| \geq I^*$, the per-process bound of §3.4." I* as in Main.md:492,
  I* = sup_t I(X_{<t}; X_{>t} | X_t), computed from each member's visible process. Formalization: admitted iff some
  O-admissible realization of that member's law satisfies log₂|𝒞_H| ≥ I*. It is a lower bound on capacity.
  Parameters: none.
- **The patch budget (Computation.md:122, :130).** [Q] "the holographic patch: $\mathrm{bits}(T) = \pi (cT)^2/l_p^2$";
  "realizable correlations are those approximable by finite-dimensional strategies". An upper bound on capacity, about
  10^145 for a day-scale computation. Formalization: admitted iff the realization's carrier is at most the budget.
  Parameters: T, the wall time, fixed by the experiment's duration (an experimental datum, not tuned). The corollary at
  Computation.md:130 presupposes quantum strategies, so it constrains which quantum correlations are realizable, not
  the CHSH magnitude. It is kept as a countercontrol only.
- **Passive-observation obstruction (book/appendix-c-objections.md:226).** [Q] "it holds in every finite operational
  theory with two or more states, whether or not the framework's core conditions hold". Kept as a countercontrol: by
  this corpus statement it should admit the gbit.

### 3.6 Excluded under §A.19, with reasons

Search: `git grep` over `papers/*.md`, `book/ch*.md`, `book/appendix-*.md` for Tsirelson, Cirel'son, 2√2, quantum
set/interval, information causality, macroscopic locality, local orthogonality, maximal entropy, equilibrium, partition
covariance and relativity, and H-Bell; over `verification/lean-mathlib/OIBridge` and `verification/lean` for CHSH,
Tsirelson, PR box, maximal-entropy and counting-measure declarations. The kernel search found no relevant declarations
(the one maximal-entropy pattern match, `maxEntVec` at DimensionalObstruction.lean:161, is the maximally entangled
vector and does not bear on the measure). Information
causality, macroscopic locality and local orthogonality appear nowhere in the corpus, so they are not candidates. The
search does not prove absence; reviewers may add candidates before step 2 (§9).

- **Double stochasticity (Main.md:62; D1 of MC6).** A theorem for every bijection under the counting measure. Under a
  non-uniform prior the corpus uses it only as an empirical selector "in the uniform-prior doubly stochastic scope", not
  as a constraint. It is a consequence of L3-A/L3-B with bijectivity and adds no constraint of its own.
- **The measurement-dependence bound (Main.md:396–403).** S ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}. I_ont is free, so it is a
  parameter OI does not fix, and branch (b) is "recorded, not adopted".
- **Q_fb representability (Main.md:82, :356).** Universal at R0, PR included, as the corpus states. Kept only as PC-3a.
- **The five completion conditions (Main.md:352; GR §3.3).** They characterize the full Kraus-instrument algebra, which
  is quantum structure. The corpus states that "Bare finite OI therefore does not select quantum mechanics" and that
  none of the conditions is supplied by bare finite OI. Using them is positing QM (E0). Not an OI principle in this
  node's sense.
- **E1 (unitary QM) and M1-B (Substratum.md:122, :128).** E1 is an empirical input that imports QM. M1-B maps E2 to
  branch (a) and fixes no magnitude.
- **Causal locality as the Bell selector (Main.md:356).** [Q] "The selector in a Bell experiment is therefore causal
  locality, not representability." Two readings:
  - As pointwise graph-cone locality with a setting-independent ensemble (Main.md:358 and the Bell-ceiling theorem
    there), it gives |S| ≤ 2 and excludes the quantum value. This is Main's theorem [rec] and MC6 B1, recorded as
    under-generation without computation.
  - Read operationally (Main.md:407), it is PC-2.
- **C1–C4 imposed at every observer partition.** Substratum.md:430: "Bare C1–C4 or graph locality do not enforce
  Tsirelson." On the one-shot families C4 also needs a temporal embedding that the corpus does not specify.
- **Implementation-fixedness of labelled instruments (Main.md:550).** It constrains how labelled instruments act (one
  fixed map per label). LE and DR use one fixed map per label by construction ([rec], `p6.py` lines 282–287 and
  506–510), so it does not bear on w.
- **Knowledge balance (Spekkens toy theory; appendix-c:232).** Cited as a precedent, not adopted. The corpus states
  "restricted access does not by itself single out quantum theory". MC6 P2 [rec].

***

## 4. Decision rule

Adopted from MC6 §12, strengthened per the owner's direction of 2026-10-20.

### 4.1 Tolerance

ε = 1/100 in CHSH units. In POM units the tolerance is ε/8 = 1/800, by the affine map of §2 that carries the classical,
quantum and maximal values onto each other. This is chosen before any computation. It is two orders below the gaps
between the classical, quantum and maximal values (2√2 − 2 ≈ 0.83, 4 − 2√2 ≈ 1.17), and coarse enough that (ii) can be
tested with finite carriers. A sensitivity row at ε = 1/1000 is reported and does not bear on the decision.

All comparisons with 2√2 and (1+1/√2)/2 are exact: rational S is compared through S² against 8 with the sign of S
fixed, and POM through the equivalent rational inequality. 3√3 is compared via 27, √(8 + 2α²) via squares, and members
with real w (LE(w), DR(w)) in exact ℚ(√2) arithmetic. No floating-point comparison enters a verdict.

### 4.2 Family stage (necessary, not sufficient)

The families are LE(n, k) and DR(n, k) for every n ≥ 1 and 0 ≤ k ≤ n, together with LE(w) and DR(w) for real w ∈ [0, 1]
where a candidate admits structured priors. A candidate passes the family stage iff:
- **(i)** among the members it admits, none has S_max in (2√2 + ε, 4] and none has POM success in
  ((1+1/√2)/2 + ε/8, 1];
- **(ii-S)** it admits a realization with |S_max − 2√2| ≤ ε and one with |POM − (1+1/√2)/2| ≤ ε/8, either a family
  member or a member of the corresponding follow-up class (𝒜_CHSH, 𝒜_POM, or the long-edge gate class for HB-2 to HB-4;
  §4.3). The report states which. The rule (MC6 §12 (ii)) says "admits realizations within ε" and does not restrict them
  to family members. That matters because LE's only quantum member is w = 0 (§2): a principle that admits only quantum
  correlations admits no LE member near 2√2;
- **(iii)** it admits every classical record law, in both forms below. A classical record law is one that some
  O-admissible realization reproduces exactly whose induced ontological model is local and measurement-independent
  (Bell scenario) or preparation noncontextual with exact parity obliviousness (POM scenario). The candidate admits it
  iff it admits at least one O-admissible realization reproducing it; that realization need not be the family member.
  DR members with 0 < w ≤ 1/2 are preparation contextual as realizations and count through this record-law form.
  - Exact form: the record laws of the named controls are admitted (CHSH: LE at w = 0; POM: DR at w = 0 and w = 1/2,
    the delay line, MC6 P1, and the toy bit, MC6 A1/P2).
  - Dense form: every classical record law in the families (LE with w = 0; DR with w ≤ 1/2) is within ε of an
    admitted one. In CHSH, each correlator and marginal expectation is within ε/4; in POM, total variation is ≤ ε/8 on
    the record law of every readout sequence of length ≤ 3.

A finite computation covers n ≤ 100 for every k. A pass for all n needs a written argument [W] beyond the computed
range. A failure needs one admitted member in violation, exhibited exactly.

### 4.3 Follow-up stage (triggered per scenario)

Passing the family stage is necessary, not sufficient. The follow-up runs per scenario:
- The CHSH follow-up ((F1), (ii-Q) and (iii-𝒜) on 𝒜_CHSH, or on the long-edge gate class for HB-2 to HB-4) runs iff
  the candidate passes the CHSH clauses of the family stage: (i) and (ii-S) for S, and (iii) for the CHSH classical
  controls.
- The POM follow-up ((F2), (ii-Q-POM) and (iii-𝒜) on 𝒜_POM) runs iff it passes the POM clauses.

A candidate that passes the clauses of one scenario only is still reported "CHSH only" or "POM only" and does not pass
the family stage. (ii-S) is evaluated first over the admitted family members and, only if none meets it, over the
corresponding follow-up class. That search is part of the family stage, and an incomplete search makes (ii-S) incomplete
(no-reduction clause below).

- **Class 𝒜_CHSH(N_max), N_max = 100.** Two-wing realizations: binary settings and outcomes; hidden register λ ∈ ℤ_n, n
  ≤ N_max; response-complete deterministic responses q = f(a, b, λ) and r = g(a, b, λ), with ontic parameter dependence
  allowed (branch (a), Main.md:392); implemented by bijections that XOR into visible pointers (the response-table
  construction, Main §3.4), so condition O holds. Operational no-signalling is required (Main.md:407). The prior on λ is
  whatever the candidate admits. Under counting-type priors the class is the set of no-signalling boxes that are
  mixtures of the 256 deterministic response pairs with weights in (1/n)ℤ. Exhaustive in the following sense: for each n
  ≤ N_max, an exact integer program over the 256 count variables subject to the candidate's constraint, solved with
  exact rational arithmetic, or by enumeration where the constraint makes that feasible. Each optimum is certified by an
  independent code path (an exact check of the solution, and an exact dual bound or a complete enumeration). Before any
  candidate is computed, step 2 checks as control K-8 that the class contains a point whose four correlators are each
  within ε/4 of the Tsirelson correlation (±1/√2) and which is itself quantum (TLM certified exactly). The PR/anti-PR
  mixture with correlators ±v, v = 12/17, at n = 34 is such a point: v² = 144/289 ≤ 1/2 because 288 ≤ 289, and |v −
  1/√2| < ε/4 [W, arithmetic; review check `structural.py`]. The (1/82)ℤ point v = 29/41 is post-quantum (v² > 1/2) and
  does not serve.
- **Reduction, verified as control K-10 before any candidate.** Under counting-type priors a box is in 𝒜_CHSH(n) iff it
  is no-signalling with every entry in (1/n)ℤ. The integer program is solved over the eight free box coordinates; the
  256-count form is the same program. 𝒜_CHSH(100) has about 2·10¹³ members (review check `classsize.py`), so no clause
  is decided by listing boxes unless the candidate's constraint makes its admitted set enumerable.
- **Class 𝒜_POM(N_max), N_max = 100.** Hidden carrier of size n ≤ N_max; preparations x ∈ {0,1}² given by priors the
  candidate admits; deterministic responses for y ∈ {0,1}; exact parity obliviousness over the two readouts.
- **Follow-up checks:**
  - (F1) S_max ≤ 2√2 + ε over every realization the candidate admits in 𝒜_CHSH (all eight orientations, §2);
  - (F2) POM ≤ (1+1/√2)/2 + ε/8 over 𝒜_POM;
  - (ii-Q) the candidate admits a realization in 𝒜_CHSH whose four correlators are each within ε/4 of the Tsirelson
    correlation, with zero marginals within ε/4. This shows that a correlation within ε/4 of the Tsirelson
    correlation, not only a value within ε of 2√2, is reachable;
  - (ii-Q-POM) the candidate admits a member of DR or 𝒜_POM whose single-readout statistics are within ε/8 in total
    variation, for each (x, y), of those of an exhibited quantum protocol with ρ_00 + ρ_11 = ρ_01 + ρ_10;
  - (iii-𝒜) every local measurement-independent box in 𝒜_CHSH, and every preparation-noncontextual model in 𝒜_POM, is
    admitted in the dense form, with the CHSH distance of (iii).
- **For candidates whose constraint is not expressible on 𝒜** (HB-2 to HB-4), the follow-up class is the long-edge gate
  class: one preparation-indexed edge whose gate is r ^= F(a, b, c) for each of the 256 Boolean functions F of the two
  settings and a hidden control c (a register ℤ_n, n ≤ N_max, read through [c < k]), with local readouts as in LE,
  embedded in the periodic cubic reference graph at L ∈ {4, 6, 8} for the finite part of the curvature evaluation. It
  is exhaustive over F and over (n, k). G(ω) contains the edge {wing A, wing B} iff F(a, b, c(ω)) is nonconstant in a
  for some b (the coupling-graph rule of Main.md:358 applied at ω). Control K-8 is also run on this class (PR/anti-PR
  via F(a, b, 0) = ab, F(a, b, 1) = ab ⊕ 1).
- **No reduction after results.** If a solver cannot complete within §A.40's local bounds, the check is reported
  incomplete and moved to CI with owner approval. The class is never reduced after any candidate's result is known.
  An incomplete check is not a pass. The clauses that depend on it are reported "incomplete beyond n_done"; outcome
  (a), (a-POM) or the (b) clause concerned is not established; and the candidate is classified Parked (follow-up
  incomplete), with the completed range stated.

### 4.4 Two separately reported outcomes (owner, 2026-10-20)

- **Outcome (a), the CHSH boundary.** Established for a candidate iff it passes the family stage on the CHSH clauses,
  (F1), (ii-Q) and (iii-𝒜) on 𝒜_CHSH. The POM boundary is reported beside it as outcome (a-POM): the family-stage POM
  clauses, (F2), (ii-Q-POM) and (iii-𝒜) on 𝒜_POM. The owner's family rule requires both scenarios, so a candidate with
  (a) and not (a-POM) is "CHSH only".
- **Outcome (b), a more general exclusion of post-quantum correlations.** Tested only for candidates with outcome (a).
  It is never inferred from (a). The tests are fixed now:
  - **(b1) Post-quantum points with CHSH ≤ 2√2, two-setting scenario, zero marginals.** The quantum set of correlators
    with zero marginals is exactly the set satisfying the Tsirelson–Landau–Masanes inequalities (TLM),
    namely |asin E₀₀ + asin E₀₁ + asin E₁₀ − asin E₁₁| ≤ π for all four placements of the minus sign.
    Directions (§A.34): quantum ⇒ TLM [L: Tsirelson 1980; Landau 1988]; TLM ⇒ quantum for zero marginals [L: Landau
    1988; Masanes 2003]; none read in full. (b1) uses only quantum ⇒ TLM (a violation certifies post-quantumness).
    K-P's inner set uses TLM ⇒ quantum. T1's post-quantumness rests on the [W] perfect-correlation argument of §2, not
    on [L]. Test points:
    - T1 = LE(5, 2), that is w = 2/5: correlators (1, 1, 1, 1/5), S = S_max = 14/5 ≤ 2√2. TLM gives 3π/2 − asin(1/5) >
      π, so T1 is post-quantum [W];
    - every LE member with 0 < w ≤ √2 − 1 (§2);
    - every box the candidate admits in 𝒜_CHSH, with any marginals, whose correlators violate TLM and have S_max ≤ 2√2
      (a TLM violation certifies post-quantumness whatever the marginals), searched over the correlator grid E(a, b) ∈
      {(n − 2d)/n} for each n ≤ N_max. TLM involves asin, so each violation is certified by an exact inequality: by the
      perfect-correlation argument of §2 when three correlators equal 1, otherwise by interval arithmetic with a
      rigorous enclosure. Numerical TLM values alone are [NUM].

    (b1) holds iff the candidate excludes all of these and still admits (ii-Q) and the classical boxes.
  - **(b2) Post-quantum points with nonzero marginals.** NPA level 1 and level 1+AB [L: Navascués, Pironio, Acín, PRL
    98, 010401 (2007) and NJP 10, 073013 (2008); Navascués, Guryanova, Hoban, Acín, Nat. Commun. 6, 6288 (2015), the
    almost-quantum set; not read in full]. Test functionals, fixed now: the tilted CHSH expressions I_α = α⟨A₀⟩ + S for
    α ∈ {1/2, 1}, each maximized over relabellings of settings and outcomes (relabellings are symmetries of the quantum
    set, so the quantum maximum is unchanged), with quantum maximum √(8 + 2α²) [L: Acín, Massar, Pironio, PRL 108,
    100402 (2012), cited from memory by the reviewer, not read in full], local maximum 2 + α and no-signalling
    maximum 4. (b2) holds iff the admitted maximum of each I_α over 𝒜_CHSH is ≤ √(8 + 2α²) + ε, compared exactly through
    squares; each maximizing box is reported with its NPA 1+AB status. A violation counts only with an exact rational
    dual witness (a Bell functional with a rational quantum bound certified by an exact sum-of-squares or rational
    semidefinite certificate). SDP output alone is [NUM] and is reported as such. A box that passes NPA 1+AB and is not
    certified quantum is reported as "almost-quantum, not certified quantum", never as quantum.
  - **(b3) An inequality whose quantum bound differs from its no-signalling bound, not used to state any candidate.**
    The chained Bell inequality with three settings per side (Pearle 1970; Braunstein–Caves 1990 [L]): local bound 4,
    quantum bound 6 cos(π/6) = 3√3 (Wehner 2006 [L, not read in full]), no-signalling bound 6. Class: 𝒜 with three
    settings per wing, n ≤ N_max. Sign convention: I₃ = E(0,0) + E(1,0) + E(1,1) + E(2,1) + E(2,2) − E(0,2), maximized
    over relabellings of settings and outcomes. (b3) holds iff the admitted maximum is ≤ 3√3 + ε and a value within ε of
    3√3 is admitted.

  Outcome (b) is reported clause by clause. "General exclusion of post-quantum correlations" is stated only for the
  clauses that hold, and only for the classes tested. A pass on (a) is never reported as (b).
- **POM and (b).** No characterization of the quantum set of parity-oblivious POM statistics analogous to TLM is fixed
  here, so outcome (b) is tested in Bell scenarios only. This is stated as a limit of the node.

***

## 5. Controls

Every control runs before any candidate's verdict is generated. A verdict printed over a failed control is void. Verdict
text is generated from the measurements.

| # | control | type | expectation |
|---|---|---|---|
| K-1 | LE(w) reproduces S = 2 + 2w and DR(w) reproduces POM = (1+w)/2 at MC6's weights (replay of B2b and P5) | must-hold, two code paths (the architecture with counting measure, and `p6.py`'s structured-prior form) | holds |
| K-2 | PR box (LE at w = 1, S = 4) and gbit (DR at w = 1, POM = 1) | must-fail: rejected by the positive-control principle K-P and by any candidate that passes | rejected |
| K-3 | S = 3 at w = 1/2 (LE(2, 1), the uniform control bit) | must-fail, as K-2 | rejected |
| K-4 | delay line (MC6 P1) and toy bit (MC6 A1, P2) | must-hold: admitted by K-P and by any candidate that passes | admitted |
| K-5 | C3 (§3.5) | countercontrol: shown vacuous, every family member admitted, from computed I* and an exhibited realization | vacuous |
| K-5b | patch budget and passive-observation obstruction (§3.5) | countercontrol, as K-5 | vacuous |
| K-P | positive control: PC-3b (the quantum set itself) | must pass the family stage, (a), (a-POM) and (b1). Shows the checker can pass a correct principle | passes; classified Reproduction |
| K-N1 | negative control: synthetic principle "S_max ≤ 3, POM ≤ 7/8 on every admitted realization" | must fail (i). Shows the checker detects a principle that admits a post-quantum value | fails (i) |
| K-N2 | negative control: synthetic principle "w ≤ 1/2 in LE, w ≤ 1/√2 in DR" | must fail (i) in CHSH (admits S = 3) | fails (i) |
| K-N3 | negative control: synthetic principle "S_max ≤ 2, POM ≤ 3/4 on every admitted realization, family or follow-up class" | must fail (ii-S) in both scenarios | fails (ii-S), CHSH and POM |
| K-N4 | negative control: synthetic principle "1/4 ≤ w ≤ √2 − 1 in LE, 1/2 ≤ w ≤ 1/√2 in DR" | must fail (iii) (excludes w = 0 in LE) | fails (iii) |
| K-N5 | negative control for the follow-up: synthetic principle "in LE, S ≤ 2√2; DR as K-P; every other architecture unrestricted" | passes the family stage, must fail (F1) in 𝒜_CHSH | fails (F1) |
| K-N6 | negative control for (b): synthetic principle "S_max ≤ 2√2 on every admitted box; POM scenario as K-P" | must pass (a) and (a-POM), and fail (b1), since it admits T1 | fails (b1) |
| K-7 | §2's fact: LE's only quantum member is w = 0 | must-hold, by the exact TLM certificate for T1 and the perfect-correlation argument | holds |
| K-8 | 𝒜_CHSH(100), and the long-edge gate class, each contain a TLM-certified quantum point within ε/4 of the Tsirelson correlation (in 𝒜_CHSH: v = 12/17 at n = 34) | must-hold, before any candidate | holds |
| K-9 | condition O on every realization used (I-2) | must-hold | holds |
| K-10 | the reduction of §4.3: under counting-type priors, membership of 𝒜_CHSH(n) equals no-signalling with entries in (1/n)ℤ, and the eight-coordinate integer program equals the 256-count program | must-hold, checked exhaustively by both forms at n ≤ 3 locally (about 2.8·10⁶ multisets); the n = 4 check (about 1.8·10⁸, C(259, 4)) runs in CI under §A.40, with owner approval for the dispatch; and by a written argument [W] for all n. No decision class is narrowed by this split | holds |
| K-11 | K-P's POM witness: ρ_x = ½(I + w((−1)^{x₀}Z + (−1)^{x₁}X)), readouts y = 0 → Z and y = 1 → X with Lüders update, reproduces DR(w) exactly on every readout sequence of length ≤ 3 for w ∈ {0, 1/2, 12/17} (Bloch length² 2w² ≤ 1; for 12/17, 288/289), with ρ_00 + ρ_11 = ρ_01 + ρ_10 | must-hold, before any candidate | holds |

The synthetic principles K-N1 to K-N6 test the checker only. They are not candidates and are not classified.

***

## 6. The three outcomes, for this node

Criteria fixed now. Each candidate gets exactly one class, with sub-labels; Parked is reported in place of a class.

- **Emergence.** All of the following:
  - the formalization is the preregistered one, and its interpretive choices were not made by their results;
  - every parameter is fixed by OI's structure as §3 states;
  - every realization is O-admissible;
  - the principle's statement contains no quantum ingredient: no quantum set, no Born probabilities, no quantum
    instruments or Hilbert-space structure, no E1, and no tuned correlation strength, unless that ingredient is
    independently derived within the node;
  - it passes the family stage and outcome (a), and also (a-POM) under the owner's two-scenario rule.

  Even then the node claims only "the CHSH and POM boundaries follow from principle X within the classes tested".
  Outcome (b) is reported separately. Neither is a derivation of QM.
- **Reproduction.** No required clause fails (precedence below), and at least one of:
  - it assumes Born probabilities, quantum instruments, the quantum set, local quantum structure (PC-3b; CL through
    the correspondence) or a tuned correlation strength, and the ingredient is not independently derived within the
    node;
  - it reaches 2√2 or (1+1/√2)/2 only through a parameter chosen for that purpose. That is Reproduction at best,
    whatever else it does;
  - it reaches them through an architecture or reading selected because it gives those values;
  - the constraint values are the target statistics (L3-D, circular).
- **Failure.** It fails (i), (ii-S) or (iii) in the family stage, or (F1), (F2), (ii-Q), (ii-Q-POM) or (iii-𝒜) after a
  family pass.
  Sub-labels, all reported:
  - over-generation (admits a post-quantum value);
  - vacuous (admits every O-admissible member, a case of over-generation);
  - under-generation (excludes the quantum value);
  - classical exclusion (fails (iii));
  - Failure-as-stated (a parameter not fixed by OI, with the parameter named).

  A Failure is scoped to the formalization examined. It is not a claim about every reading of the corpus text, nor
  about every observer-level extension.
- **Parked.** Not formalizable from the corpus text without a choice the corpus does not make (CL without its
  definition; PC-4, L3-C or HB-3β needing an unnamed choice; HB-3β with disagreeing N_BE values), or a required check
  incomplete (§4.3, follow-up incomplete, with the completed range stated). The gap is named, and no class is
  assigned.

For every Failure the node states the structural reason: which property of the principle lets the post-quantum or
classical-excluding members through, or excludes the quantum value.

**Precedence, fixed now.**
1. Parked, if a formalization gap or an incomplete check (§4.3) prevents a decision.
2. Otherwise Failure, if any required clause fails, including by scenario silence. Attach "CHSH only" or "POM only"
   when the other scenario's clauses and follow-up pass. Attach "quantum ingredient" when a Reproduction condition
   also holds.
3. Otherwise Reproduction, if any Reproduction condition holds.
4. Otherwise Emergence.

***

## 7. Productivity test and G6

**Productivity test (fixed now, from MC6 §12).** The node is a gem iff:
- a principle passes (Emergence or Reproduction with outcome (a)); or
- a principle fails for an identified structural reason that propagates to N1–N3 of MC6.

"Identified structural reason" means a written or computed statement, strictly stronger than "candidate X does not fix
w", that names the property responsible for the failure and states what it implies for N1 (invisible
response-relevant preparation memory), N2 (parameter dependence, nonaffine in the settings) or N3 (a magnitude-fixing
principle). For example, a principle constrains graph geometry and not prior weights; or a principle's admitted
weights are dense in [0, 1] for an identified reason. A failure already recorded in MC6 (C3 vacuous; restriction with
free w) is a non-gem, a coherence relabelling, record-only. A Failure whose reason is that the candidate constrains
the prior and not the architecture, so that threshold registers make its admitted weights dense, restates MC6 §12 and
is a non-gem unless the node adds a statement strictly stronger than that record (for example, one identified property
responsible for the failure of every §3.1 reading).

**G6, a distinguishing prediction, if a principle passes.** Decision rule (MC5 §7 control 5; MC6 §3): a candidate
prediction counts iff:
- it is a finite-precision statistic, raw-direct under §A.24, on which the principle's admitted set differs from QM by
  more than ε;
- its size is fixed by OI quantities with no free parameter;
- both outcomes are possible.

Scenarios fixed now, none of them used to state a candidate:
- the chained Bell value with three settings, (b3);
- I3322 (Collins–Gisin 2004 [L]; its quantum maximum is known only numerically [NUM, L], so a G6 there needs an exact
  separating value);
- the NPA 1+AB boundary, (b2);
- the temporal CHSH and Leggett–Garg bounds (Le et al. 2017, Main ref. [26] [L, not read]);
- the POM success with three bits (Spekkens et al. 2009 [L]).

The candidate prediction is the principle's admitted extremum against QM's, in each scenario. If the principle's
admitted set lies strictly inside the quantum set somewhere, the prediction is that observed quantum correlations there
falsify it. If it lies strictly outside, the prediction is a super-quantum value of fixed size. Either is G6 only under
the rule above.

***

## 8. Invariant→checkpoint table (§A.41)

| # | property the node will assert | checkpoint that measures it |
|---|---|---|
| I-1 | the preregistration preceded every computation on a candidate and is unchanged | sha256 of this file recorded in NODE.md and in the commit message; the step-2 commit contains this file byte-identical (digest compared); amendments, if any, are appended under `amendments/` with time and reason, each before the first computation of the candidate it touches; the probe's first line of output prints this file's sha256 |
| I-2 | condition O holds for every realization used | the probe represents each realization only as (Ω, list of bijections of Ω, visible readout projection, prior on Ω); exhaustive bijectivity check on Ω for every step; law functions take only (prior, steps, readout), checked by a static test that the law code reads no other input; the reviewer reads the realization constructors |
| I-3 | each candidate is computed by its preregistered formalization with the parameters of §3 | a parameter table in the probe, transcribed from §3, with the rule parameters ε, N_max and L ∈ {4, 6, 8}, and compared by the reviewer; each candidate's admit-function cites its §3 label |
| I-4 | S, POM and correlators are exact; no floating point in any verdict | rational arithmetic throughout (`fractions` or SymPy rationals); comparisons with 2√2 via S² against 8; a static grep of the verdict path for float literals and `float(`; any [NUM] value labelled and excluded from verdicts |
| I-5 | the probe is deterministic | two runs, byte-identical output, `SHA256SUMS` |
| I-6 | no verdict is printed over a failed control | verdict generation is gated on K-1 to K-11, K-P and K-N1 to K-N6 all passing; mutation test: breaking one control suppresses every verdict (reviewer) |
| I-7 | the checker detects post-quantum admission, under-generation and classical exclusion | K-N1 to K-N6 fail as §5 states, and K-P passes |
| I-8 | the family-stage result for all n, beyond n ≤ 100 | computed rows for n ≤ 100, plus a written argument [W] for all n, reviewed; a failure exhibits one exact admitted violator |
| I-9 | each scenario's follow-up runs iff that scenario's family clauses pass (§4.3), over the whole class | probe log of the trigger; per-n optimum with an independent certificate (exact solution check, and an exact dual bound or complete enumeration); K-8 green first |
| I-10 | outcome (b) is reported apart from (a) | separate output blocks and NODE.md sections; the probe never derives a (b) line from an (a) result; TLM violations certified exactly (I-4), NPA violations only with an exact rational witness |
| I-11 | classification follows §6 | a table mapping each candidate's measured clauses to its class under the §6 rules, checked by the reviewer against §6 |
| I-12 | corpus quotes are verbatim at the stated file:line at `8fb6a5ec` | a script that checks each quoted string at its stated line or line range of the stated file at the base commit. Normalization: whitespace collapsed; each quote split at "…"; each fragment matched case-sensitively within the stated range |
| I-13 | the result is independently reviewed before use | review outcome section in NODE.md, as in MC1–MC6 |
| I-14 | the §2 fact about LE (only w = 0 is quantum) | K-7: exact perfect-correlation argument and the TLM certificate for T1 |
| I-15 | no class, tolerance or rule parameter changed after a candidate's result | before any candidate the probe prints ε, N_max, the L set, the function families and the class definitions with their digest, compared with this file by the reviewer; incomplete checks logged with n_done |
| I-16 | productivity and G6 verdicts follow §7 | a table naming, for each claimed structural reason, the statement or computation it rests on and the N1–N3 item it bears on, checked against §7 including the MC6-recorded non-gem cases |
| I-17 | the §6 classifier maps clauses to classes as fixed | unit tests before candidates: K-P and K-N1 to K-N6 return their expected labels, and a synthetic clause vector for each class, Emergence included, returns that class |

***

## 9. Procedure and freeze

- Step 2 runs in this order: (1) controls K-1 to K-11, K-P, K-N1 to K-N6, and the classifier unit tests (I-17); (2)
  candidates in the order L3-0, L3-A, L3-B, L3-C, L3-D, L3-PR, PC-1, PC-2, PC-3a, PC-3b (as K-P), PC-4a, PC-4b, HB-1,
  HB-2, HB-3α, HB-3β, HB-4, CL; (3) each scenario's follow-up for any candidate that passes that scenario's family
  clauses (§4.3), and outcome (b) for any candidate with outcome (a); (4) productivity verdict and G6.
- Additions before step 2 starts (a reviewer's added candidate or a corrected quote) are appended under `amendments/`
  with time and reason, and the new sha256 is recorded. After the first candidate computation, the formalizations, ε,
  the classes, the rule and the classification criteria are frozen. A discrepancy found later is recorded, not
  repaired.
- Negative results are acceptable outcomes and are scoped to the formalization examined.
