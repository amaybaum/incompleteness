# OI-QM-APPROX-1, unit 1: operational equivalence at finite precision, assessed against Main §3.4

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r2, pending a fresh,
independent full-text review.** r2 answers the review of r1 (`review/REVIEW-APPROX-UNIT1.md`, sha256
`b131792e…10c2`, verdict REVISE); each finding's disposition is in `DISPOSITIONS-r2.md`, and r1 is kept
unchanged as `r1/APPROX-UNIT1.md`. Nothing here is adopted, promoted or proposed for the manuscripts. A
review ACCEPT, if reached, authorizes no computation, new physical premise, manuscript change or merge
(#1216 body, "Unit 1").

- **Accountable home:** #1216 (OI-QM-APPROX-1). Parent programme #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1216 c.6741763726 (posted 2026-11-09T13:53:51Z),
  option "Create + start unit 1 (Recommended)", scope verbatim: "Unit 1 (paper-only): does Main's
  existing approximation result meet Level A? What prevents Level B? Is continuous coherent mixing
  still necessary? It ends with a fresh independent review. No new computation beyond labelled exact
  generic checks, no physical premises, no manuscript change, no merge." The coordinator's brief adds:
  no computation on an OI mechanism, and no git or GitHub write. This unit made no git, repository or
  GitHub write.
- **Inherited requirements.** Owner (amaybaum), #1216 c.6742051100 (posted 2026-11-09T14:07:19Z),
  three distinctions from #868, "each … reported separately, and none implies another without proof":
  validity ("every permitted product test gives a valid result"), closure ("every permitted
  preparation and heralded continuation stays in the admissible state space") and quantum
  compatibility ("the resulting joint states correspond to quantum states under the stated
  comparison"); and the question "whether approximate joint-state closure can be achieved with finite
  shuffle-only dynamics, even where exact closure needs a complex operation", "to be investigated, not
  assumed". Answered in §5.
- **Owner decisions bearing on §7.** #1169 c.6742190154 (amaybaum, posted 2026-11-09T14:13:27Z),
  decision 4: "The matrix records scoped relations: phase is independent of the layer flow only; the
  complex drive carries the phase; no H-Bell implication." Decision 8: "§A.29 candidate-condition
  scoring goes into the dependency matrix, paper-only." No scoring is done here; §7 is kept usable for
  it. "None of decisions 1–8 authorizes a scientific computation".
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (2026-11-09
  08:36 +0200). `origin/main` is now `cac5d264`, which differs from `fd539e15` only in `papers/SM.*`,
  so every citation below is current. "Main" = `papers/Main.md` (sha256 `6144cd4a…6366`), "GR" =
  `papers/GR.md` (`a475a2a8…4992`), "OB/" = `verification/lean-mathlib/OIBridge/`, and under
  `verification/programmes/oi-qm/reconstruction/`: "MECH-2" = `mechanism-2-20261108/DESIGN.md`, "AP1" =
  `apparatus-1-20261107/DESIGN.md`, "QP" = `quarter-phase-native-20261107/DESIGN.md` (MECH-2 calls it
  "QA"). All `path:line` citations are at `fd539e15`.
- **Line-number mapping (finding F0).** #1216's body cites "the exact-arithmetic theorems (:544, :576)
  and the density corollary (:578)" and #945's "negativity-ledger step at :556". These are pre-shift
  numbers. #945 c.6567863298 states that the narrowing "moved the theorem from Main:556 to
  Main:566–:580 at `02009693`"; the uniform +22 offset is this unit's inference, checked on `main`'s
  history: at `7c6ceaaa` and its parent the gluing theorem, Rounding Lemma, uniform theorem and density
  Corollary are at :544, :556, :576, :578, and at `02009693` at :566, :578, :598, :600 (both commits are
  ancestors of `fd539e15`). At `fd539e15` the gluing theorem is Main:566–:580, the uniform theorem
  Main:598, the density corollary Main:600; no per-parent negativity estimate remains (the one
  occurrence of "negativity" at Main:578 describes check 16), and Main:578 instead states that the
  clip-and-normalize estimate "is not established for the simulator's Hermitian branches" and that the
  finite-b bound is open. Main:556 at `fd539e15` is the Remark "what this equivalence does and does not
  say".

## 0. Answers in one place

1. **Level A: met, in three forms, none OI-derived.** (a) *Exactly*, by a per-experiment table: the
   action-labelled comb with a product prior carrying the quantum conditionals (Main:482–:484, :520,
   :602). (b) *Within ε, exact-ring arithmetic*, by the gluing realization (Main:566–:580): any
   finite-dimensional system, fixed initial state, finite family of finite-Kraus instruments, every
   adaptive protocol to horizon K, TV ≤ K(|O_max|−1)/G. (c) *Uniformly within ε* over all ≤m-outcome
   instruments on ℂ^d at horizon K (Main:596–:600), exact-ring budget. Access in (b)–(c): the observer
   writes instrument labels into the visible record and reads visible outcome registers; the quantum
   state is held in hidden registers. Paper proofs with probe certification; no kernel module
   formalizes gluing or rounding. **At finite b (fixed-point registers) the realized-law bound is open**
   (Main:568, :578, :580, :602); #945's per-parent negativity ledger is refuted by a record off `main`
   (support off `main`, §1.1); on `main` that step is stated as not established (Main:578).
2. **Level B.** Main's gluing/uniform construction is a reusable mechanism, not a prediction table (one
   fixed map per instrument, every protocol, gluing by restriction; the comb of (a) *is* a table). At
   fixed (d, m, K, ε) it meets Level B's *shape* for one fixed system, a composite counting only as one
   d_A d_B system built with the tensor rule (Main:574; §3.2 B-3); it is not a compositional mechanism,
   since the composite's realization is not assembled from the components' realizations. It is a
   discretized ψ-ontic classical simulator (state description plus seeds):
   "Quantum mechanics enters as the instrument data and as the state held in the hidden register"
   (Main:582), the same machinery realizes non-quantum families (Main:584, :600), and the substratum
   contributes only finiteness and reversibility. What prevents an OI-derived Level B is that the rule
   family (density register, Kraus update, Born trace, tensor composition, instrument dictionary) is
   supplied, plus four scope limits: declared K and ε (unavoidable at a fixed finite carrier, §3.2 B-2),
   fixed d (no union over d), |N|-independent capacity only at the open finite b, composites via one
   joint register built with the tensor rule.
3. **Smallest missing operational property (§4): NX-1.** Some *valid* native procedure (OI dynamics and
   stated access, no quantum data as parameter or input) induces on the declared encoding a
   transformation at an ε-independent positive distance from that encoding's closed, composition-stable
   classical class: the diagonal-preserving maps on the configuration carrier; the nonnegative-frame
   maps under a fixed linear frame identification. Necessary for an OI-derived Level B on those two
   routes, relative to the identification (configuration-level dynamics with hidden memory reproduce
   the laws, A1–A2), at the instrument level and at the law level (§4.2). On the configuration route it
   implies a non-monomial admissible operator at the level of its branch (FI-1 when that level is one),
   is strictly stronger than FI-1 (theory-level counter-model: the column-monomial class) and strictly
   weaker than layer-flow executability (three kernel lemmas composed; §4.2). Not sufficient. On
   the third route (a ψ-ontic
   register encoding, as in Main's simulator) no operational property is missing — the simulator is a
   finite bijection using "no property of the substratum beyond finiteness and reversibility"
   (Main:582) — and the gap is selection (Main:602).
4. **Continuous coherent mixing (§6).** Not necessary for Level A or for Level B's shape (exact-ring
   proofs; the mixing sits in the supplied Kraus data). For an OI-native approximate target on the
   configuration carrier, continuity and the kernel's uncountability strengthening are not necessary,
   but the discrete core is: an available operation that does not preserve diagonal states (which
   implies a non-monomial admissible operator, FI-1 at level one) and a non-real operation [A + G1]. The complex drive supplies both at once; that it can
   carry the phase does not show that OI supplies the drive. On fixed-linear-frame encoded carriers
   configuration-level mixing is not the operative resource; the identification is (MECH-2 Lemma F, W).
5. **Dependency matrix:** §7. Unit 1's OI-derived question does not depend on #945's outcome; #945 bears
   only on the simulator's fixed-format capacity.
6. **Owner requirements (§5).** Validity, closure and quantum compatibility are reported separately for
   each claim, with coverage of the target class as a fourth, separate entry; finite b is a natural
   witness that validity holds while closure fails. Approximate joint-state closure under finite
   shuffle-only dynamics:
   - *configuration carrier:* closure, validity and compatibility hold trivially (every reachable state
     is diagonal); coverage of the needed joint states fails, ε-robustly (trace distance ≥ 1/2 at any
     carrier size);
   - *fixed tetrahedral frame:* frame-dependent. Under R1 (AP1 §4.2, the frame Lemma F is stated for)
     quantum states, Φ⁺ included, are not all representable (coordinates (1−√3)/4 and −1/8); under
     Main:562's SIC frame every quantum state is representable. Entangling continuation fails under
     both, conditional on Lemma F (on its [A] extension, under SIC);
   - *register-encoded route:* **yes** (exact ring, proved on paper), with the complex structure
     supplied as data.

***

## 1. Conventions

**Evidence layers.**
- [K] kernel-checked Lean on `main` (identifier and module given).
- [P] paper proof in a manuscript on `main`.
- [X] exact computation recorded on `main` (probe named in the manuscript).
- [G] this unit's labelled exact generic checks (`probes/approx_generic_checks.py`, groups G1–G5, and
  `probes/r2_frames.py`, `r2_routeC.py`, `r2_finiteb.py`, groups F, C, N5; §11); a result supported
  only by [G] is *computation-supported*.
- [RV] an exact check by the reviewer of r1 (`review/rv_*.py`), re-run here with byte-identical
  output; cited beside a [G] check of this unit, or (rv_Er, §5.2) as an instance corroborating a [P]
  statement, never as the sole support of a claim.
- [A] this unit's own hand argument, unreviewed.
- [L] external literature, recalled, not re-read here; bibliographic details to be checked by the
  reviewer.
- [W] model-written research record on `main`, not established under §A.46 item 1.
- [D] unreviewed or in-revision draft in the session scratchpad, used as a hypothesis only
  (§A.46 item 7): BRIDGE = `bridge/BRIDGE-UNIT1.md` (r5, sha256 `78f1098e…`, reviewed ACCEPT WITH
  NITS per the coordinator); SHM = `qphen/SHARED-MECHANISM.md` (#1210 r7); A868 =
  `reassess/868/ASSESS-868.md` (r3a, `d97c4b6b…`, reviewed ACCEPT WITH NITS per the coordinator);
  A1059 = `reassess/1059/ASSESS-1059.md`.
- [OFF] support off `main`: a claim that uses content held only off `main` (§1.1). Each such use is a
  gap under §A.42 item 8 if this record lands; nothing here lands.

**Carriers.**
- **Configuration (C).** The finite configuration set S, read as the quantum carrier ℂ^S under Main:564's
  operational interface, with no memory outside ℂ^S. Substratum interventions are monomial operators
  (OB/SubstratumInterface.lean:75, `IsMonomial`; GR:260).
- **Configuration-level dynamics (C-dyn).** Dynamics on a finite configuration set that includes hidden
  memory, with only part of the configuration read as the visible record; not read as the quantum
  carrier. Main's comb (A1) and simulator (A2, A3) are of this kind, and they reproduce the laws (D2,
  D3), so route C's obstructions are relative to the route-C identification, not to configuration-level
  dynamics as such.
- **Encoded, frame (E_f).** A d-level system identified *linearly* with distributions over
  configurations through a fixed identification. Configurations are treated classically. Three named
  identifications occur, kept apart because their results differ (§4.2, §5.2):
  - **E_f(R1)**: AP1 §4.2's one-cell identification R1 and MECH-2's product R1^⊗n. A point (z, x) of
    F₂² ↔ the Bloch-type vector v = ((−1)^z, (−1)^x, (−1)^{z+x}) (|v| = √3), a law μ ↔
    ρ = Σ μ_λ (I + v_λ·σ)/2, so μ_λ = (1 + v_λ·r)/4. The reconstruction frame is orthogonal
    (tr A_k A_l = 2δ_kl) and the coordinate functionals are not positive [G: r2 F1].
  - **E_f(SIC)**: Main:562's embedding p_i = (1 + a_i·r)/4, a_i = v_i/√3 (a SIC POVM, the same vertex
    set), with reconstruction D_i = (I + 3a_i·σ)/2, which is not orthogonal (tr D₀D₁ = −1) [G: r2 F1].
    Main:562 states the single-qubit embedding "with restricted preparations"; its product extension to
    composites is this unit's [A].
  - **E_f(U′)**: QP node 5's encoding of two same-colour cells by the functionals f_z = z₁, f_x = x₁,
    f_y = z₁ + x₁ + z₂ + x₂ (eight points, linear, not injective; QP:448–450). QP node 10's composite
    uses it.
- **Encoded, register (E_r).** A d-level system whose state is stored as data (a digitized density
  matrix) in hidden registers, one state per configuration, beside pre-loaded seeds: a discretized
  ψ-ontic, ψ-supplemented ontological model in the sense of Harrigan–Spekkens, Found. Phys. 40, 125
  (2010) [L], for pure preparations entered as channels from the fixed initial state; precisely, it
  stores an unnormalized density register ("ρ-ontic"), with the seeds and the stack as the supplement.
  Main's gluing realization is of this kind. E_f and E_r are both "encoded" in the brief's sense; they are kept apart because their
  obstructions differ.

**Three distinctions kept throughout (#1169 c.6740778880, as quoted in A1059):** configuration vs
encoded carriers; mathematically available vs derived from OI; coherent mixing vs the full probability
and composition rules.

**Three-column separation** for every restriction (§8): (i) well-defined; (ii) follows from
independently justified OI principles; (iii) reproduces QM. Column (iii) never supports column (ii).

**Three outcomes** for every Level-A/B claim (§5), in the owner's words (#1216 c.6742051100):
*validity*, "every permitted product test gives a valid result"; *closure*, "every permitted
preparation and heralded continuation stays in the admissible state space"; *quantum compatibility*,
"the resulting joint states correspond to quantum states under the stated comparison". Each claim
states its admissible state space and its comparison. A fourth entry, *coverage*, is reported
separately: the states and instruments the target class needs are reached within the stated accuracy.
Coverage is not one of the three outcomes and is not folded into closure. No outcome is inferred from
another without a proof stated at the place (A868 §4.1, r3a).

### 1.1 References off `main` (§A.42 item 8)

Each reference to content not on `main` is classified by the claim it is attached to: *provenance*
(the claim does not use the content), *support on `main`* (what the claim uses is on `main`), or
*support off `main`* (a gap if this record lands). Nothing here lands, so no gap is closed; the
classification is recorded.

| Reference | Attached claim | Classification |
| --- | --- | --- |
| #1216 c.6741763726 | Authorization and scope of this unit (header) | Provenance (owner designation, quoted with author and time) |
| #1216 c.6742051100 | The three outcomes and the shuffle-only question (§1, §5) | Provenance (owner requirement, quoted); the outcomes' content in each row rests on the row's own evidence |
| #1169 c.6742190154, decisions 4 and 8 | Scoping of §6's drive sentence and of D26; §7's later use | Provenance (owner decisions, quoted) |
| #1169 c.6740778880, as quoted in A1059 | The three distinctions (§1) | Provenance (working conventions) |
| #1216 body, #945 body | F0: pre-shift line numbers | Provenance; the shift is supported on `main` by `7c6ceaaa` and `02009693`, both ancestors of `main` |
| #945 c.6567863298; c.6567879503 §6 | F0's "moved … at `02009693`"; D5's "complex-entry constant only estimated" (#945 owner question 6, undecided) | F0: provenance (checked on `main`'s history). D5 qualifier: support off `main` |
| #945 c.6567879503 §2 (with its exact checks R-1, R-2) | D4a and §2.2: per-parent ledger step refuted (d = 4, b = 24, 6.9063 against 4.0000) | Support off `main` |
| #945 c.6567879503 §2 (i)–(ii) | §2.2: "the counterexample refutes a proof step, not the final TV bound; reachability … not shown" | Support off `main` (a limitation of the refutation) |
| #945 c.6567879503 §3(b) | D4b: stopping-time repair, Kη ≤ 1/64, 14K²C_{d,R}2^{−b}, graded Motivated | Support off `main` |
| #945 c.6567887681 | Final check of the #945 assessment, ACCEPT-WITH-NITS (D4a, D4b grading) | Support off `main` |
| `proofs/eps-realization/` on `audit/intro-corpus-20261026` at `6d494e30` (head `16fc745d` per #945 c.6657435508; neither is an ancestor of `main`) | D4a: the refuting record | Support off `main` |
| #945 c.6657435508 | F945-R "not authorized"; readiness "blocked: owner questions" (§2.2, D4b, D5) | Provenance (planning status) |
| #945 c.6567879503 §1 "No Lean module formalizes gluing, rounding or clipping" | §2.1 A2 evidence row | Support on `main`: this unit's grep of OB/ at `fd539e15` |
| `7c6ceaaa:papers/Main.md` (line 556 states two other exact failures of the per-parent estimate, d = 3 and d = 4) | None: removed by `4cef4200` the same day ("the instance numbers and the undefined estimate are gone") | On `main`'s history, superseded; not used |
| BRIDGE, SHM, A868, A1059 (scratchpad drafts, [D]) | Rows marked [D] | Support off `main`; used as hypotheses only (§A.46 item 7). Where this unit re-derived a [D] item from `main` or by [G], the row cites that and the [D] use becomes provenance (QP node 10's non-quantumness, §5.1, C7) |
| #868 (J1–J13), #1210 (M-labels), #1211, #1059 | Labels for requirements and planning homes (§4.2, §7 "Shared with") | Provenance |
| Literature [L] | §2, §6, D19 | External sources outside item 8's list; recalled, not re-read |

***

## 2. Question 1: does Main meet Level A?

Level A (#1216): "Any specified finite quantum experiment's observable law is reproduced within ε."

### 2.1 The three constructions

| | A1. Comb with response-table prior | A2. Gluing realization (ε-form) | A3. Uniform continuum realization |
| --- | --- | --- | --- |
| Source | Main:482–:486 (theorem, proof), :520 (Extension, real kernels), :602 ("a fixed finite instrument family is realized exactly by the intervention dilation above, with a product prior carrying the quantum conditionals") | Main:566–:580: theorem, clauses (1)–(5), Rounding Lemma, proof; Main:582 single-dynamics Corollary | Main:596 (adaptive diamond telescoping Lemma), :598 (theorem), :600 (density Corollary) |
| Experiments | Any finite action alphabet and finite-horizon action-labelled family P(x_{k+1} \| x_{≤k}, a_{≤k}); adaptive choice is covered because every context (x_{≤k}, a_{≤k}) is a coordinate [A: the chain-rule reading; Main:482 states "every action sequence", and the contexts are distinct and the prior a product] | A d-dimensional system, a fixed initial state (other preparations enter as outcome-free channels), a finite family F of instruments, each outcome a CP map with finitely many Kraus operators, horizon K; every adaptive protocol over F through K; spatially separated parts via the product construction on a joint register (clause (4)) | Every adaptive protocol of horizon ≤ K with arbitrary ≤m-outcome instruments on ℂ^d, preparations included as channels, by rounding each instrument to a δ-net member, δ = ε/(2K) |
| Accuracy | Exact for arbitrary real kernels (:520); ε only for the rational uniform-tape presentation | TV ≤ K(\|O_max\|−1)/G with exact-arithmetic registers over the instruments' entry ring; at finite b **open** (:568) | TV ≤ Kδ + K(m−1)/G ≤ ε, exact regime; R-laws within ε/2 of quantum laws; finite b **open** (:598) |
| Access | Agent writes the action ledger (bijections I_a), reads visible x | Visible: step counter, intervention record (labels written by the agent, or a read-only program register prepared once, :582), outcome registers (read). Hidden: branch register, predecessor stack, K pre-loaded seeds | As A2, with net labels: ⌈log₂\|N\|⌉ = O(m d⁴ log(2K/ε)) bits per step of visible intervention record |
| Where quantum content enters | The product prior *is* the quantum conditionals | Instrument data (Kraus operators) in the step maps; the state in the hidden register; Born trace q_o = Tr I_o(ρ̃) computed by the step map (:580, :582) | As A2, over the whole net |
| Carrier | C-dyn (classical response coordinates in hidden memory) | C-dyn: finite bijection on configurations; system in E_r | As A2 |
| Evidence | [P]; [X] `intervention_probes.py` (n_V = \|A\| = K = 2, exact), `lg_comb_probes.py`; real-kernel Extension: [P], rational instance [X] `review4_probes.py` P-G. Passive (action-free) law: [K] `S_imp_D`, OB/Equivalence.lean:422 | [P]; [X] `opglue_probes.py` at (d, K, \|F\|) = (2, {2,3}, 4), exact over ℚ(√2), checks 11–13. No Lean module formalizes gluing, rounding or clipping (#945 c.6567879503 §1; this unit's grep of OB/ for "gluing", "rounding", "opglue" found none relevant) | [P]; [X] checks 8–9 (qubit instance). Telescoping Lemma: [P], standard |
| Resources | Main:520 gives \|C_H\| = n^N (n+1)^K (K+1), N = Σ_{k=1}^{K} n^k, for the passive (action-free) comb. For the action-labelled comb N counts the (x_{≤k}, a_{≤k}) contexts and the action ledger adds its own factor [A]; exponential in K either way | Exact ring: log₂\|C_H\| ≤ (K+1) log₂\|V_reach(F,K)\| + K log₂ G (:576). Fixed point: O(K d² b + K log₂ G), whose accuracy form depends on the open finite-b bound | Exact ring: capacity grows with the net (:598). Reading [A]: \|V_reach\| ≤ Σ_{k≤K}(\|N\|m)^k, so log₂\|C_H\| = O(K² m d⁴ log(K/ε)), polynomial; the transition law's description scales with \|N\| = exp(O(m d⁴ log(1/δ))) (:598) |

### 2.2 Verdict on Level A

**Met, with three qualifications.**

- *Scope.* Finite-dimensional systems, finitely many outcomes, a finite horizon declared in advance, a
  fixed initial state with alternative preparations as channels. Continuous-variable systems and
  continuous outcome sets are outside every construction above.
- *Precision regime.* Exact (A1) or within ε in **exact-ring arithmetic** (A2, A3). In fixed-point
  b-bit registers the realized-law bound is open: Main:568 ("a bound on the realized outcome law of the
  clipped and normalized simulator at finite b is open"), :578, :580, :598, :602 item 4. #945's finding
  agrees: the exact-arithmetic theorems (Main:566, :598) and the density Corollary (Main:600) survive;
  the finite-b constants are unproved. The former negativity-ledger step (pre-shift Main:556) is
  refuted per parent by a dyadic two-outcome instance at d = 4, b = 24, error 6.9063 against the old
  bound 4.0000 [OFF: #945 c.6567879503 §2, record at `6d494e30`]. The counterexample refutes a proof
  step, not the final TV bound; reachability of a negativity-dominated register from an exact initial
  register is not shown [OFF]. A stopping-time repair is graded Motivated and is not authorized (F945-R).
  This unit does not duplicate it.
- *What meeting Level A shows.* Little about OI (§A.31, favourable reading pressure-tested):
  - A1 is the "preloaded table of quantum predictions" #1216 warns about. Its hidden prior is the
    quantum conditional table, and it realizes any finite stochastic comb, quantum or not (Main:362,
    :600). It explains nothing quantum.
  - A2/A3 import the quantum formalism (Main:582) and need nothing of the substratum beyond finiteness
    and reversibility. They show compatibility of finite-accuracy quantum statistics with one fixed
    reversible law, not derivation. Classification on #1216's axes: consistency-axis compatibility, no
    correctness content (§A.23).

***

## 3. Question 2: what prevents Level B?

Level B (#1216): "One reusable mechanism and rule family approximates a whole specified class of
experiments, including adaptive measurement and composition."

### 3.1 Table or mechanism?

| Criterion | A1 comb/response table | A2/A3 gluing simulator |
| --- | --- | --- |
| Description size | Lists a conditional for every context: (n\|A\|)^K entries | Lists the Kraus data of F (poly in d, \|F\|), or of the net N |
| Same description serves unseen protocols? | Only those whose contexts were loaded | Every adaptive protocol over F / over all ≤m-outcome instruments (net rounding), "the construction never asks which protocol is running" (:580) |
| Context-independent per-instrument mechanism | — | Yes, clause (3) (:572) |
| Gluing / restriction | Automatic within one table | Clause (2): overlapping families agree identically (:570) |
| Longer horizon, new instrument | New table | Exact ring: new carrier (V_reach changes). The *rule* (apply Kraus, threshold the seed) extends unchanged |
| Verdict | **Per-experiment table** | **Reusable mechanism**, whose compression is quantum mechanics itself |

**Skeptical note.** On a finite carrier every bijection is extensionally a lookup table; in the exact-ring
regime the register's alphabet V_reach is determined by (ρ₀, F, K) and the stack holds the full branch
history. "Mechanism vs table" is therefore a statement about *description* (compression and reuse on
cases not used to build it), not about the extension of the map. Under that criterion A2/A3 are a
mechanism; the mechanism is a classical simulator of QM.

### 3.2 What prevents an OI-derived Level B

**B-1. The rule family is supplied, not derived (decisive).** The step maps apply supplied CP maps to a
supplied state and compute supplied Born traces (Main:580, :582). The construction "is an operational
realization theorem, not a uniqueness theorem: the same reversible machinery can realize non-quantum
finite instrument families" (Main:584), and D_finite's closure contains non-quantum theories (Main:600).
Main itself names what remains: "What remains is selection" (Main:602). Column (iii) holds within ε;
column (ii) is empty. **Consequence:** Level B *as worded* is non-discriminating for the same reason
Q_fb representability is (Main:556: "representability alone is not the framework's discriminating
content"): a universal classical simulator of QM meets it. Level B carries information about OI only if
its mechanism is derived from OI with independently justified access (#1216's central question) — owner
question OQ1.

**B-2. Horizon and accuracy are declared per realization; this is forced at a fixed finite carrier.**
Main:640 proves the exact form: a bijection on a finite set has finite order L, so a fixed realization's
multi-time law is exactly L-periodic. *Approximate form [A + G2]:* let a fixed finite realization on S
realize "repeat the rotation K times" by repeating one fixed bijection K times (repetition is
compositional), and set L := lcm(1, …, |S|). Every bijection of S has order dividing L, so the
realized law at horizon K is L-periodic in K. If the target class contains the rotation by π/L about y
(it does if it contains all rotations about one axis), the qubit protocol "|0⟩, K such rotations, then
Z" has P(0) = cos²(Kπ/(2L)), which is 0 at K = L and 1 at K = 2L [G2b], while the realization gives the
same law at both; so it errs by ≥ 1/2 in TV at one of them. **Scope:** fixed finite S, compositional
repetition, a class containing that rotation. It does not touch realizations whose carrier grows with K (Main's) or whose
procedure for the repeat depends on K. Level B must therefore be per declared (K, ε) with declared
resource scaling, as #1216 already requires. Classification: ELABORATING (approximate extension of
Main:640).

**B-3. Composition is covered only at fixed d, with the tensor rule supplied.** Clause (4) composes
spatially separated experiments "by applying the local instruments' CP maps as I_a ⊗ I_b on the joint
branch register", "necessarily joint for entangled preparations" (Main:574). The composite is a new
realization on a d_A d_B register, not built from the components' realizations, and Main:574 relates no
component's realization to the composite's marginal; its rule is the quantum tensor product. Level B's
shape is therefore met for one fixed system, a composite counting as one such system (§0 item 2). The
uniform theorem and the density Corollary hold "at each fixed system dimension d and outcome bound m …
the union over (d, m) is a further limit, not taken here" (Main:600), so
repeated composition over an unbounded number of subsystems is outside every proved statement.

**B-4. Fixed-format hardware only in the open regime.** A hidden-state capacity independent of |N| is
obtained only with fixed-point registers, "whose finite-b accuracy bound is open" (Main:598). In the
exact ring the carrier is indexed by the net's reachable set. So the regime in which the simulator's
hardware is independent of the target class is exactly the regime whose accuracy is unproved (#945).
This bears on the simulator, not on the OI-derived question (§7, row D4).

**B-5. Instrument dictionary.** Net rounding maps a continuum instrument to a net label (Main:598 (i)).
The map from a physical intervention to "the quantum instrument it is" is supplied to the machine. In
the single-dynamics form the policy is a program register of up to Θ(|O_max|^K log₂|F|) bits, charged
as an initial condition (Main:582).

***

## 4. Question 3: the smallest missing operational property

### 4.1 Three routes, kept apart

- **Route E_r (ψ-ontic register).** Main's simulator is a finite bijection and "uses no property of the
  substratum beyond finiteness and reversibility" (Main:582); the characterization's realization datum
  is an existentially chosen bijection on 𝒞_V × 𝒞_H (Main:544). Whether the simulator also meets C1, C3
  and C4 is not checked here. Here **no operational
  property is missing**: the gap is selection — showing, from OI principles, that the substratum's
  dynamics and stated access implement such an encoding rather than another finite bijection (Main:602).
  That is a derivation obligation, not an operational one.
- **Route C (configuration carrier as the quantum carrier, Main:564's interface, no memory outside ℂ^S).**
- **Route E_f (fixed linear identification: R1, SIC or U′, §1).**

### 4.2 NX-1, stated for routes C and E_f

**NX-1 (one robustly nonclassical, valid native transformation).** Relative to a declared encoding and
the stated access, some native procedure — built from the OI dynamics and access, with no quantum
instrument data as parameter or input — induces on the encoded system a valid (completely positive,
trace-non-increasing) transformation at a positive, ε-independent distance from the encoding's
*classical class*:
- route C: the maps that preserve diagonal states (`PreservesDiag`, OB/DiagonalTheory.lean:68);
- route E_f, under an injective identification (R1 or SIC): the maps whose frame matrix is entrywise
  nonnegative (MECH-2 Lemma F's class). For the non-injective U′ the frame matrix of a map is not
  unique (MECH-2 node 7), and no class is fixed here.

**Necessity [A].** Both classes are closed and stable under composition, sums (coarse-graining,
outcome-conditioned continuation) and attachment/discard of a diagonal or frame-represented ancilla. If
every native procedure's branches lie in such a class 𝒞, every adaptive composite procedure's branches
lie in 𝒞, and a target instrument at distance c > 0 from 𝒞 is approximated by none of them for ε < c,
at every horizon and every resource level. The target class contains such instruments:
- *Route C:* for every diagonal D, tr((|+⟩⟨+| − D) σ_x) = 1, so ‖|+⟩⟨+| − D‖₁ ≥ 1; the Hadamard
  channel is at trace distance ≥ 1/2 on the input |0⟩⟨0| from every diagonal-preserving map [G1a–b];
  likewise for composites, x+ ⊗ z+ against every diagonal D with witness X⊗Z [G4].
- *Route E_f (R1 or SIC):* the two identifications share the vertex set, and a single-qubit rotation O
  acts by M_ij = (1 + 3 a_i·O a_j)/4 in both: the frame matrices of all 24 single-qubit Clifford
  unitaries coincide in the two frames [G: r2 F2; RV rv_frames R1b]. The 12 rotations of A₄ give
  permutation matrices; each of the other 12, the Hadamard and S among them, has an entry −1/2 [G3;
  r2 F2]. The nonnegative matrices form a closed set and, the identification being injective, the frame
  matrix of a channel is determined by its action on states, so each such rotation sits at a positive
  distance from Lemma F's class [A, compactness]. For composites the two frames differ: the CNOT
  conjugation's frame matrix has minimum entry −1/4 under R1 and 1/4 − √3/3 ≈ −0.327 under SIC, in
  either orientation [G5b (SIC); r2 F3 (both); RV rv_frames R1c]; SWAP, which preserves Pauli weight,
  has the same (permutation) matrix in both [r2 F3].

*Law level (route C).* Level B is a law-level target. On route C the gap transfers to laws, because
the identified carrier holds the whole state, with no memory outside ℂ^S: an instrument reused across
protocols is one fixed diagonal-preserving map, which acts on the reachable (diagonal) states as a
stochastic matrix. Witness: on two configurations, any stochastic map used for H errs by at least
g = (√2 − 1)/2 ≈ 0.207 in TV on (|0⟩, H, Z-read) or on (|0⟩, H, H, Z-read); g is attained
(T(0|0) = 1/√2, T(0|1) = 1), and the coherent Hadamard has gap 0 [G: r2 C5; RV rv_routeC C5].
*Scope:* this necessity is relative to the route-C identification. Configuration-level dynamics with
hidden memory (C-dyn) are not covered, and A1 and A2 are such dynamics that reproduce the laws (D2, D3).

**Where native constructions sit.**
- *Route C* [K-lemmas, composed here (A)]: in the theory a configuration-level architecture generates,
  every branch of every available instrument is a finite sum of conjugations by admissible monomial
  operators (`realized_of_instAvail`, OB/ImplementationLocality.lean:530), hence preserves diagonal
  states (`preservesDiag_conj_of_monomial`, OB/SubstratumInterface.lean:126; `preservesDiag_sum`,
  OB/DiagonalTheory.lean:84). The substratum class is configuration-level
  (`substratumClass_configurationLevel`, OB/ManuscriptAxioms.lean:129), and the substratum theory is the
  theory it generates (`substratumTheory`, OB/RouteB.lean:284). The stated observer theory lies inside
  it at every level (`obs_availExt_le_substratum`, OB/SubstratumInterfaceAudit.lean:837, as used at
  OB/ExecSource.lean:129). A native system-level procedure built by Main:564's rule (f) is an available
  preparation, a family at its level and the partial trace; attaching the uniform ancilla and the
  partial trace map diagonal matrices to diagonal ones, so the induced system map preserves diagonals
  when the level family does [A]. The composition is the same argument as the kernel's
  `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52); it is not stated as one theorem.
  So the stated substratum with its access fails NX-1 on route C.
- *Route E_f(R1)* [W, conditional]: MECH-2 Lemma F (every encoded branch nonnegative on frame
  coordinates, under a fixed linear identification by an orthogonal frame, R1^⊗n at q = 2) and Theorem
  U2 (under R1^⊗n, encoded unitary channels induced by fixed bijections lie in A₄ ≀ S_n, which is finite
  and Clifford). If Lemma F holds, route E_f(R1) fails NX-1 for every dynamics, and MECH-2's own
  conclusion follows: "a nonclassical observer-level theory needs a change in the identification and
  access, not in the dynamics alone".
- *Route E_f(SIC)* [A, this unit's extension of Lemma F]: Lemma F's proof of (a)–(b) uses only that
  every operation acts on laws as a nonnegative matrix and that the identification is linear (and
  injective, for uniqueness), not that the frame is orthogonal (MECH-2 node 2). With the same hypotheses
  (the operation set and H-LIFT) it applies to Main:562's SIC frame, and route E_f(SIC) then fails NX-1
  likewise. Theorem U2's proof uses orthogonality (MECH-2 node 3) and is not extended.

**Relation to FI-1 and to layer-flow executability (route C).** FI-1 (BRIDGE [D]; its content is the
conclusion of `exists_nonMonomial_of_layerFlowExecutable`): some K on S × Fin 1 with 𝓘 K and
¬IsMonomial K, for the generating architecture 𝓘. Each direction is stated separately (§A.34).
- *NX-1 ⇒ FI-1* [A from K-lemmas]. In a theory generated by an architecture, an available branch that
  does not preserve diagonals is a finite sum of conjugations by 𝓘-operators on the carrier of its level
  (`realized_of_instAvail`), not all monomial (`preservesDiag_conj_of_monomial`, `preservesDiag_sum`).
  At level one this is FI-1 verbatim; a system-level branch arising by rule (f) has a level family that
  does not preserve diagonals (above), so in general NX-1 gives a non-monomial admissible operator at
  some level n, i.e. 𝓘 is not configuration-level, and FI-1 itself when n = 1.
- *FI-1 ⇏ NX-1* [A + G, at kernel-definition level; not kernel-checked]. Counter-model: the
  column-monomial class CM (at most one nonzero entry in each column).
  - CM satisfies the five fields of `Architecture` (OB/ImplementationLocality.lean:506–515): identity,
    products, scalar multiples, ancilla projectors and ancilla blocks `ancBlock K f e`
    (OB/AncillaClosure.lean:457) of CM matrices are CM [A; G: r2 C1].
  - K = |0⟩(⟨0| + ⟨1|)/√2 (on S × Fin 1) is CM and not monomial, so FI-1 holds [G: r2 C3].
  - Every CM conjugation maps diagonal matrices to diagonal ones [A; G: r2 C2], so by
    `realized_of_instAvail` and `preservesDiag_sum` every branch of `genTheory CM` at every level
    preserves diagonals, and so does every system map built by rule (f); NX-1 fails.
  - `InstAvail.op` requires Kᴴ K = 1 (OB/ImplementationLocality.lean:271–272), and CM's isometries are
    exactly the monomial ones [A; G: r2 C3], so K enters `genTheory CM` only through products and
    ancilla blocks, never as an isometric step. The reviewer's C4 (rv_routeC) checks the same model.
- *Layer-flow executability ⇒ NX-1* [A from K-lemmas]. If T executes the layer flow of an involution σ
  with σ x ≠ x (`LayerFlowExecutable`, OB/LiftAudit.lean:112), then at level one and t = ½ the
  gate-flow conjugation is available, it is unitary (`gateFlow_unitary`, OB/LiftAudit.lean:69, which
  needs σ involutive), and it does not preserve diagonals (`gateFlow_half_not_preservesDiag`,
  OB/LiftAudit.lean:155, at (x, 0)).
- *NX-1 ⇏ layer-flow executability* [A from K-lemmas]. In `polarizedTheory (Fin 2)`
  (= `genTheory PolGen polGen_arch`, OB/C5Discovery.lean:247) the gate flow of the swap at t = ½ is
  available at level one (`polarizedTheory_swap_half_level_one`, OB/C5Discovery.lean:325) and does not
  preserve diagonals (`gateFlow_half_not_preservesDiag`), so NX-1 holds there; and
  `polarizedTheory S` executes the layer flow of no σ with a moved point
  (`polarizedTheory_not_layerFlowExecutable`, OB/PolarizationClosure.lean:395). Three kernel theorems,
  composed here; not stated as one theorem. r2 C4 checks the half-time entries (1 ± i)/2 as a control.
  `polarizedTheory` adds two operator images to the stated access, so this separates the two
  properties and says nothing about OI's access.

So, on route C, NX-1 is strictly stronger than FI-1 and strictly weaker than layer-flow executability.

**Why "smallest".** NX-1 is a single-operation property, necessary on routes C and E_f, and it is
exactly where native constructions (kernel-level on C; MECH-2 on E_f) and Main's simulator part: the
simulator escapes only because its encoding is E_r with imported arithmetic.

**Not sufficient.** NX-1 does not give:
- *density* — the next link, **NCG** (native compositional generation): native procedures whose induced
  instruments have adaptive compositions ε-dense in the class for every ε, with resources scaling by a
  declared rule. At a fixed finite carrier, the encoded maps induced by single bijections (with fixed
  ancilla initialization and fixed heralds) form a finite set, so NCG needs adaptive procedures of
  unbounded length, a carrier refined with ε by a target-independent rule, or non-bijective native
  operations [A]. Under MECH-2 U2 [W] the encoded unitaries under R1^⊗n stay in A₄ ≀ S_n at every n;
- the probability rule (#1059; A1059 §0 [D]);
- the composition rules: local tomography, pair source, entangling operation, validity on joint tests
  (A868 J1, J2, J5, J7, J13 [D]; SHM M17, M18 [D]);
- validity/C-CP: MECH-2's P★ leaves the stabilizer octahedron in branches that are not positive maps
  (the record-0 branch sends Z₋ to a non-PSD state; the record-1 branch outputs a non-PSD state), and
  its unconditioned background channel is not CP (MECH-2 node 6) [W]; whether some protocol leaves the
  octahedron with every branch CP is left open there. That is why NX-1 requires validity.

***

## 5. Owner requirements: validity, closure and quantum compatibility, and shuffle-only joint closure

### 5.1 The three outcomes per Level-A/B claim, with coverage reported separately

"Admissible state space" and the comparison are stated per claim, since closure and quantum
compatibility are relative to them. Each entry gives the outcome, its status and its own reason; no
entry is derived from another unless the derivation is written in it. Coverage (§1) is a separate
column and is not one of the owner's three outcomes.

| Claim | Admissible state space | Validity | Closure | Quantum compatibility (comparison) | Coverage of the target class |
| --- | --- | --- | --- | --- | --- |
| A1 comb / response table (Main:482, :520, :602) | Visible conditional laws generated by the loaded prior (classical simplex on the response coordinates) | **Holds, by construction**: realized probabilities are measures of a product prior [P] | **Holds in the realization's own space** (any heralded continuation is the loaded conditional) [P]. Closure in the *quantum* state space holds only because quantum conditionals were loaded — column (iii) | Realized conditional laws against quantum laws: **holds exactly** when quantum conditionals are loaded; **fails** for non-quantum data: PR-box data give validity and closure with no quantum compatibility (Main:362) [P] | **The loaded family only**, exactly; nothing outside it |
| A2 gluing, exact ring (Main:566–:580) | PSD branch matrices ρ̃ in the register | **Holds**: q_o = Tr I_o(ρ̃) ≥ 0 for CP I_o on PSD ρ̃ — derived from closure here, by complete positivity — and realized frequencies are seed counts [P] | **Holds exactly**: exact CP maps keep the register PSD; composites by I_a ⊗ I_b on the joint register stay PSD [P] | Realized laws against the register state's quantum laws, in TV: **holds within K(\|O_max\|−1)/G** [P, X]; per instrument the maps are the quantum ones by construction (column iii) | **Every adaptive protocol over F through K**, within the same bound (clause (1)) [P] |
| A2 at finite b (Main:568, :578, :580) | As above | **Holds for realized laws, by construction**: clipping and normalization give nonnegative pre-grid probabilities and seed thresholds give frequencies (Main:578 Corollary text) [P] | **Fails**: "digitized branches are Hermitian but not positive" (Main:578) [P]; a reachable instance: one digitized y-rotation (θ = π/4) applied to the exact register \|0⟩⟨0\| gives det = −325/2097152 < 0 at b = 12, inside the window b ≥ 11 (K = 1), under a stated round-to-nearest reading of Main:578's model; floor rounding and a rational rotation give further instances [G: r2 N5; RV rv_finiteb]. The per-parent ledger meant to control this is refuted [OFF] | Realized laws in TV: **open**, the realized-law bound at finite b (Main:568) | **Open** (same bound) |
| A3 uniform, exact ring (Main:598) | PSD register over the net's reachable set | Holds, as A2 exact | Holds, as A2 exact | **Within ε** at fixed (d, m, K), exact ring [P]; fixed-point variant open | **Every protocol of horizon ≤ K over ≤m-outcome instruments on ℂ^d**, within ε [P] |
| A3/A4 density Corollary (Main:600) | Operational theories at fixed (d, m) in the finite-test topology | Holds for every R^Q_n (as A2) | Holds for R^Q_n (as A2); D_finite's closure also contains non-quantum theories (Main:600) | Holds for every R^Q_n (as A2) | **Density at fixed (d, m)** [P]; union over (d, m) not taken |
| Route C, stated substratum + access (OI-native) | Density matrices on ℂ^S reachable under Main:564's rules | **Holds**: diagonal reachable states give nonnegative probabilities on configuration reads [A from K-lemmas] | **Holds trivially**: every reachable state is diagonal with nonnegative entries [A from K-lemmas] | Reachable states and branches against quantum states and instruments: **holds trivially**: every reachable state is diagonal, hence a quantum state, and every branch is a CP diagonal-preserving map, so every realized law is a quantum law [A from K-lemmas; G: r2 C6 control] | **Fails, ε-robustly**: no coherent preparation within trace distance < 1/2, at any carrier size [G1, G4; r2 C6]; law level: (√2 − 1)/2 (§4.2) [r2 C5] |
| Route E_f(U′), QP node 10 composite | Encoded joint tables on the native body (stabilizer octahedron per QP) | Holds on native Pauli tests for QP node 10's zero-completion table (A868 §4.3 [D], which grades it A + X) | Not assessed for node 10's table. In general, closure of the octahedron under heralding is sufficient, not necessary, for validity on native tests (A868 §4.1, witness w3 [D]) | Joint table against quantum states: **fails**: ⟨XX⟩ = ⟨ZZ⟩ = 1 forces Φ⁺, which has ⟨YY⟩ = −1, so QP's ⟨YY⟩ = 0 has no quantum completion (QP:746–768 [W]; G: r2 C7) | The native gate does not act as the table CNOT on (x+, z+) (A868 §4.3 [D]) |
| Route E_f(R1), MECH-2 P★ (one cell) | Quantum states of the encoded qubit, through R1 | Holds for the native configuration records (probabilities 5/8, 3/8) and reads (Lemma F(c)) [W] | **Fails**: the record-1 branch gives r = (1/3, −1/3, −1), \|r\|² = 11/9, not PSD (MECH-2 node 6) [W] | Encoded state against the Bloch ball: **fails** for record 1, read off the same computation as closure (not inferred from it); record 0 gives a valid non-stabilizer state from a branch that is not a positive map [W] | No encoded entangling unitary under R1^⊗n (Theorem U2 [W]); quantum states with negative R1 coordinates, Φ⁺ among them, are not represented (§5.2) [G: r2 F4–F5] |

**Independence witnessed.** Finite b: validity holds, closure fails, quantum compatibility open. QP node
10: validity holds, quantum compatibility fails. A1 with non-quantum data: validity and closure hold,
quantum compatibility fails. The only derivation used between outcomes is closure ⇒ validity for exact
CP maps on a PSD register (A2, A3), stated where used; in the P★ row closure and compatibility are read
off one computation, as stated there. Route C is not a witness among the three: validity, closure and
compatibility all hold there, and only coverage fails, so the three outcomes together do not give
coverage.

### 5.2 Can approximate joint-state closure be reached with finite shuffle-only dynamics, where exact closure needs a complex operation?

"Shuffle-only" is read as: every dynamical step is a bijection of a finite configuration set (no
phase operation, no non-monomial operator; adding the phases, which are monomial, changes none of the
conclusions below). The question is answered with the owner's outcomes kept apart: *closure* (every
permitted preparation and heralded continuation stays within ε of the admissible, quantum, state
space), *validity*, *quantum compatibility*, and, separately, *coverage* (every needed joint state —
full-ball products, and the continuations the class requires — is reached within ε). #868's J3 joins
coverage and closure in one requirement; here they are reported separately. The answer is assessed per
carrier, without assuming it.

1. **Route C — closure, validity and compatibility hold trivially; coverage fails, ε-robustly, at every
   carrier size.** Under Main:564's rules with monomial operations, every reachable state is diagonal
   [A from K-lemmas; A868 G7a [D] agrees], so it is a quantum state and stays one under every
   continuation. Coverage fails: for x+ ⊗ z+ and y+ ⊗ z+, tr((ρ − D) W) = 1 for every diagonal D with
   W = X⊗Z or Y⊗Z [G4; r2 C6], so the trace distance is ≥ 1/2 whatever the carrier size or ε. The exact
   requirement (A868 J3: a non-monomial *and* a non-real operation) therefore persists at finite accuracy
   in its discrete form, as a coverage requirement; only continuity drops (§6).
2. **Route E_f — frame-dependent.** R1 and Main:562's SIC frame share the vertex set and agree on
   single-qubit Clifford maps (§4.2), but they differ on states and on entangling maps.
   - *States under SIC — representable.* Every quantum state, entangled ones included, has nonnegative
     joint SIC coordinates (they are the probabilities of the product POVM {E_i ⊗ E_j}, E_i ≥ 0) [G5a for
     Φ⁺; r2 F1, F4; general fact A]. Counting-measure distributions are rational, and with growing counts
     they approximate any such coordinates [A]. Which preparations are *available* is a separate
     hypothesis (H-PREP; A868 J3 [D]).
   - *States under R1 — not all representable, ε-robustly.* The pure state r = −v₀/√3 has R1 coordinate
     (1 − √3)/4 < 0, and Φ⁺ has a product-frame coordinate −1/8 [G: r2 F4; RV rv_frames R1d]; every
     R1-represented state is at trace-norm distance ≥ 2 − √3 from each of them (Hölder with
     ‖F₀‖_op = (1 + √3)/4 and ‖F_l ⊗ F_m‖_op = (2 + √3)/8) [G: r2 F5]. AP1 records the single-qubit
     instances (the target of `rot` and the parity-oblivious-multiplexing states have negative weights;
     "the 4-point carrier cannot hold the in-plane boundary of the disk", AP1:872–878 [W]).
   - *Closure in the quantum state space* is not automatic in either frame: a nonnegative frame
     distribution can reconstruct a non-PSD operator (a point mass reconstructs D₀ ⊗ D₀, resp. A₀ ⊗ A₀,
     with a negative eigenvalue [G5d; r2 controls]), so preparations must be restricted (Main:562's
     "restricted preparations"); under R1, MECH-2's P★ reaches a non-PSD encoded state natively (§5.1)
     [W].
   - *Entangling continuation.* The CNOT conjugation's frame matrix has a negative entry in both frames:
     minimum −1/4 under R1 and 1/4 − √3/3 ≈ −0.327 under SIC [G5b; r2 F3; RV rv_frames R1c]; local A₄
     rotations give permutation frame matrices in both [G5c; r2 controls]. If Lemma F holds (under R1
     [W]; under SIC by this unit's extension [A], §4.2), every native encoded branch is frame-nonnegative,
     so no native continuation approximates CNOT below a positive constant [A, compactness]. Shuffles
     that mix ontic pairs beyond A₄ ≀ S_n can leave the quantum state space while keeping product-test
     validity (QP node 10, under U′; A868 §4.3 [D]).
   - *Verdict.* Under R1: coverage of the needed joint states fails, ε-robustly, already at the level of
     representation (Φ⁺), and, conditional on Lemma F, the entangling continuation #868's J7 needs is not
     reached. Under SIC: joint states are representable, and, conditional on Lemma F's extension, the
     entangling continuation is not reached. In both, restricting the dynamics to A₄ ≀ S_n keeps closure
     exactly but generates no entanglement.
3. **Route E_r — yes, proved on paper in exact ring.** Main's simulator *is* finite shuffle-only
   dynamics: each step is one bijection of a finite configuration set (Main:566, :580). In exact ring its
   register stays PSD (closure), joint registers included (clause (4)), its pre-grid probabilities are
   valid, and its realized laws are within K(|O_max|−1)/G of the quantum ones [P]; the reviewer's
   instance check of the construction with complex instruments (H, S, CNOT) agrees [RV rv_Er, re-run].
   Complex amplitudes, coherent mixing and entangling CNOT are all present — as the stored Kraus data and
   register entries (the instruments' entry ring), not as an operation on any carrier. In exact ring this
   is exact closure, not an approximation phenomenon. At finite b closure fails and the accuracy bound is
   open (§5.1).

**Verdict on the question.** Where exact closure with coverage needs a complex operation (route C),
shuffle-only dynamics on that carrier keep closure, validity and compatibility, trivially, but do not
reach the needed joint states: the coverage obstruction is ε-robust. Shuffle-only dynamics on a
*different* carrier (E_r) reach them with exact closure, the complex structure supplied as data —
"mathematically available", not "derived from OI" (column (iii), not (ii)). On E_f the answer depends on
the frame: under R1 the needed joint states are not representable even approximately; under SIC they are,
and for both the entangling continuation turns on MECH-2 Lemma F (under SIC, on its [A] extension), which
is not established on `main` (§A.46 item 1); if it holds, the answer there is no for entangling
continuation.

***

## 6. Question 4: is continuous coherent mixing still necessary?

| Target | Continuity (layer flow at every t; uncountably many non-monomial rays) | Non-monomial operation on C (FI-1) | Non-diagonal-preserving operation on C (NX-1, route C) | Non-real operation on C (phase / complex drive) |
| --- | --- | --- | --- | --- |
| Exact finite endomorphic operational QM on C (#1169's exact target; not altered here) | Necessary for the kernel's route: `uncountableNonMonomialRays_of_layerFlowExecutable` (OB/CoherentContinuumSource.lean:163) [K], within the structural architecture | Necessary, one direction: `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52) [K]; not sufficient (`polarizedTheoryC_not_qm`, OB/PolarizationClosure.lean:620) [K] | Necessary (gate flow at t = ½ does not preserve diagonals: `gateFlow_half_not_preservesDiag`, OB/LiftAudit.lean:155) [K] | Phase stated as an intervention principle, not derived (Main:590; GR:260, `PhaseSource.lean`) [K] |
| Level A, and Level B's shape (any carrier, rules may be supplied) | **Not necessary** [P: Main:566, :598, exact ring] | **Not necessary** on the configuration carrier: the realization is a bijection [P] | Not necessary [P] | Not necessary as an operation; the complex entries are in the supplied data [P] |
| OI-native approximate target on route C (all instruments on ℂ^S within ε) | **Not necessary** [A + L]: a countable set suffices for ε-density; one fixed generic non-monomial unitary with the permutations of S generically generates a dense subgroup [A, by analogy with Lloyd, PRL 75, 346 (1995) and Deutsch–Barenco–Ekert, Proc. R. Soc. A 449, 669 (1995), which concern almost every two-qubit gate applied to chosen qubit pairs [L]]; for an inverse-closed generating set, word lengths O(log^c(1/ε)) (Solovay–Kitaev; Dawson–Nielsen, QIC 6, 81 (2006) [L]; inverse-free versions exist, recalled, not checked). The kernel's uncountability strengthening is specific to the exact target | **Necessary** (implied by the next column, at the level of its branch; §4.2) [A from K-lemmas + G1] | **Necessary** [A from K-lemmas + G1, G4] | **Necessary**: real-Kraus operations keep real states real, and tr((\|+i⟩⟨+i\| − R) σ_y) = 1 for every real symmetric R [G1c; A]. The stated phase supplies it (monomial, non-real); the complex drive (GR:250) supplies both this and the previous column at once |
| OI-native approximate target on route E_f | Not the operative resource: configuration-level mixing does not enter a frame identification that treats configurations classically [A] | Not the operative resource [A]; encoded non-monomial maps arise without FI-1 at stabilizer scope (BRIDGE §5.1 [D], citing QP) | — (route C notion) | — |

**Answer.** Continuous coherent mixing is not necessary for any approximate target considered here.
For Level A and Level B's shape nothing of FI-1 is necessary, because the mixing is moved into supplied
data (E_r). For an OI-native approximate target on the configuration carrier, its discrete core stays
necessary: one available operation that does not preserve diagonal states (⇒ a non-monomial admissible
operator, FI-1 at level one; §4.2) and one non-real
operation; the continuity and uncountability that the exact target forces are not. BRIDGE's statement
that FI-1 is "not necessary for finite-accuracy reproduction of quantum statistics (Main:566, Main:584,
Main:600)" is correct for statistics on E_r and does not extend to an OI-native approximate target on
the configuration carrier.

**Skepticism (§A.31), since "continuity is not necessary" favours the framework.** Dropping continuity
removes no obligation the stated substratum meets: the stated access supplies no operation that fails to
preserve diagonals (§4.2, route C), so the discrete core is as unsupplied as the continuous one. The
complex drive carries the phase (BRIDGE r5; A868 §4.4; GR:258), and the phase is independent of the
layer flow only (`obligations_independent`, OB/C5Discovery.lean:59); both scoped relations are those
#1169 decision 4 records. A drive that can generate the phase does not show that OI supplies the drive
[A]: Main:590 adds the state-mixing operation "as an empirical controllability resource".

***

## 7. Question 5: dependency matrix

Columns: **status** (proved / conditional / disproved / open), **evidence**, **carrier** (C, C-dyn,
E_f(R1 / SIC / U′), E_r; §1), **assumptions**, **shared with** #1169 / #945 / #1210 / #1211, or
independent (Ind). Row IDs are identifiers, not ordinals, and are not reused. For #1169 decision 8's
later §A.29 scoring, a candidate condition's preserved results (its controls) can be named by these IDs
with their status, carrier and assumptions; no row records a candidate condition, a premise adopted
here or a score.

| ID | Dependency | Status | Evidence | Carrier | Assumptions | Shared with |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | S ⇔ D ⇔ Q_fb at every finite horizon (Main:548) | proved | [K] `finite_horizon_equivalence`, OB/Equivalence.lean:462 | C-dyn | finite alphabet and horizon; fixed-basis readout | #1169 (baseline), #1211 (frontier) |
| D2 | Exact Level A by comb + response-table prior (Main:482, :520, :602) | proved | [P], [X] `intervention_probes.py`; passive half [K] `S_imp_D` | C-dyn | target conditionals loaded as product prior; per family and horizon | #1169 (intervention dilation, classical rung) |
| D3 | ε-Level A by gluing, exact ring (Main:566–:580) | proved | [P], [X] `opglue_probes.py` (d = 2); no Lean | C-dyn dynamics, E_r system | exact-ring registers; supplied instrument data and initial state; finite Kraus; fixed K, G | #945 (survives) |
| D4 | Finite-b realized-law bound | open | Main:568, :578, :580, :602 [P] | E_r | fixed-point registers; window rule | #945 only |
| D4a | Old negativity-ledger step (per parent) | disproved off `main` [OFF]; on `main` stated as not established (Main:578) | [OFF] #945 c.6567879503 §2, record at `6d494e30` (support off `main`, §1.1) | E_r | in-window dyadic instance d = 4, b = 24 | #945 only |
| D4b | Stopping-time repair, TV ≤ K(\|O\|−1)/G + 14K²C_{d,R}2^{−b} | conditional (Motivated, unreviewed, not authorized) | [OFF] #945 c.6567879503 §3(b) (support off `main`, §1.1) | E_r | Kη ≤ 1/64; exact initial register; Rounding-Lemma constant | #945 only |
| D5 | Rounding Lemma, instrument level (Main:578) | stated proved on `main` (Main:578: "the instrument-level inequality is proved"); the complex-entry constant is contested off `main` (#945 owner question 6, undecided) | [P]; [OFF] for the qualifier (support off `main`, §1.1) | E_r | fixed-point dyadic model | #945 only |
| D6 | Uniform continuum, exact budget (Main:598) | proved; \|N\|-independent capacity open | [P], [X] checks 8–9 | E_r | fixed (d, m, K, ε); δ-net rounding as dictionary | #945 (capacity), #1169 |
| D7 | Finite-test density at fixed (d, m) (Main:600) | proved; union over (d, m) open | [P] | E_r | exact ring | #1169 |
| D8 | Classical-dimension obstruction to exact equivalence (Main:560) | proved (factorization half); unboundedness imported [55] | [P], [X] `nogo_probes.py` | any finite ontic carrier | ordinary prepare–ontic–measure interface | #1169 |
| D9 | No uniform finite realization of the instrument algebra (Main:488); finite-order periodicity (Main:640) | proved | [P] | C-dyn | fixed finite S | #1169 |
| D10 | Approximate horizon no-go (§3.2 B-2) | proved here, unreviewed | [A + G2] | C-dyn | fixed finite S; compositional repetition | Ind (elaborates D9) |
| D11 | Non-uniqueness: the realization machinery realizes non-quantum families (Main:584, :600, :362) | proved | [P] | C-dyn / E_r | — | #1169, #1210 (selection) |
| D12 | Selection: why the substratum's bijection is a quantum-shadow one (Main:602) | open | — | E_r route | — | #1169, #1210 |
| D13 | Five completion conditions characterize exact finite operational QM (Main:564) | proved, exact target | [K] `exactAll_iff_physical_general` (OB/GeneralCarrier.lean:100), `five_way_minimality` (OB/RankGapTheory.lean:702) | C (complex kinematics given) | complex matrix kinematics taken as given | #1169 (exact; not altered here) |
| D14 | Approximate analogue of the five conditions | open (not stated anywhere read) | — | C | — | Ind |
| D15 | FI-1 necessary for the exact target | proved, one direction | [K] OB/ExecSource.lean:52 | C | structural architecture | #1211, #1169 |
| D16 | FI-1 not supplied by stated access / landing lift formulations | proved; open for the wave lift | [K] `obs_not_layerFlowExecutable` (OB/ExecSource.lean:129), `configurationLevel_not_layerFlowExecutable` (OB/LiftAudit.lean:183); BRIDGE [D] for the open part | C | stated read/write access | #1211 |
| D17 | NX-1 (route C) necessary for an OI-native approximate target, at instrument and law level; NX-1 ⇒ a non-monomial admissible operator at its branch's level (FI-1 at level one); FI-1 ⇏ NX-1; NX-1 strictly weaker than layer-flow executability | proved here, unreviewed, each direction separately (§4.2) | [A from K-lemmas + G1, G4; r2 C1–C6]; counter-models: the column-monomial class (A + G, kernel-definition level), `polarizedTheory (Fin 2)` (three K-lemmas composed) | C | Main:564's interface, no memory outside ℂ^S; generated theory of an architecture | Ind; refines #1211 |
| D18 | Non-real operation necessary for the same target | proved here, unreviewed | [A + G1c] | C | as D17 | #1211 (O1), #868 J3 [D] |
| D19 | Continuity / uncountability not necessary for approximate targets | conditional | [A + L] | C | a generic non-diagonal-preserving operation available; a gate set generating a dense subgroup (inverse-closed, for the stated rate) | Ind (sharpens #1211's exact-only statement) |
| D20 | MECH-2 Lemma F, Theorem U2, Theorem NC | conditional (W record; open per SHM Q6-O8 [D]) | [W] MECH-2 §0 | E_f(R1) | orthogonal frame (R1^⊗n), H-LIFT, injective identification, spanning-read certification | #1210, #1169 |
| D21 | Route E_f(R1): joint-state representation fails ε-robustly (Φ⁺ coordinate −1/8; r = −v₀/√3 coordinate (1−√3)/4; trace-norm distance ≥ 2 − √3 from every represented state); robust obstruction to NX-1 and to entangling continuation (CNOT minimum −1/4) | representation: proved here, unreviewed (exact); NX-1 and entangling: conditional on D20 | [A + G3; r2 F2–F5]; AP1:872–878 [W] for single-qubit instances | E_f(R1) | R1 (AP1 §4.2), H-LIFT | #1210 (M11, M12), #868 |
| D22 | Native encoded non-Clifford operation (M12); repeated composition (M13) | open | SHM [D] | E_f | — | #1210 |
| D23 | Composite rules: pair source, local tomography, entangling operation, joint-test validity (J1, J2, J5, J7, J13; M17, M18) | open | A868 [D], SHM [D] | C / E_f | — | #1210, #1169, #868 |
| D24 | H-Bell / cross-wing response (M19) | open | Sub:131–133; Main §3.3 [P] for the one-step ceiling | C-dyn (ontic graph) | — | #1210, #1211. Finite-accuracy Bell statistics exist on E_r (Main:574) [P]; no row here implies H-Bell (#1169 decision 4) |
| D25 | Born probability rule / exponent | supplied on E_r (Tr I_o(ρ̃)); open for OI derivation | Main:580 [P]; A1059 [D] | E_r / C | — | #1059 (outside the four; recorded) |
| D26 | Phase intervention. Scoped relations (#1169 decision 4): the phase is independent of the layer flow only (`obligations_independent`, OB/C5Discovery.lean:59, on Fin 2); the complex drive carries the phase (GR:250, :258) | stated assumption, not derived | [K] `PhaseSource.lean` (GR:260); [K] OB/C5Discovery.lean:59 | C | — | #1211, #1169 |
| D27 | Route E_f(SIC, Main:562): every quantum state representable (nonnegative product-SIC coordinates); robust obstruction to NX-1 and to entangling continuation (CNOT minimum 1/4 − √3/3) | representation: proved (standard; exact); NX-1 and entangling: conditional on Lemma F's extension to SIC [A] | [A + G5a, G5b; r2 F1, F3, F4] | E_f(SIC) | Main:562's identification with restricted preparations; its product extension [A]; Lemma F's operation set and H-LIFT | #1210, #868 |

**Independence of #945.** Every OI-derived question in this unit (D12, D14, D17–D23, D27) is independent of
#945's outcome. #945 decides only whether the E_r simulator has a proved finite-b, fixed-format,
|N|-independent form (D4–D6).

***

## 8. Restriction ledger (three columns)

| Restriction | (i) well-defined? | (ii) from independently justified OI principles? | (iii) reproduces QM? |
| --- | --- | --- | --- |
| Declared horizon K and accuracy ε per realization | yes | yes, from finiteness: forced at a fixed finite carrier (D9, D10) | no (QM has no horizon); a scope, not a reproduction |
| Exact-ring registers | yes | no; an idealization of the simulator | yes within the grid (D3) |
| Fixed-point b-bit registers | yes | no; a hardware choice | open (D4) |
| Exactly stored initial register (#945 repair (b)) | yes | no | conditional (D4b) |
| δ-net rounding of instruments (dictionary) | yes | **none identified**; supplied to the machine | yes (D6) |
| Product prior carrying quantum conditionals | yes | **none**; chosen from QM | yes, by construction — column (iii) supports nothing in (ii) |
| Monomial (configuration-level) substratum operations | yes | yes for the stated access [K] | no (D17, D18) |
| Fixed linear identification R1^⊗n with H-LIFT | yes | a modelling choice in AP1/MECH-2 [W] | no: quantum states with negative R1 coordinates, Φ⁺ among them, are not represented, ε-robustly; and, if Lemma F holds, no entangling and no non-A₄ operation (D21) |
| SIC identification (Main:562) with restricted preparations | yes | none identified; a representation choice | represents every state; carries no sharp effect (Main:562); no entangling continuation if Lemma F extends [A] (D27) |
| Restriction to A₄ ≀ S_n continuations (to keep closure) | yes | none identified | keeps closure, generates no entanglement — no |
| Fixed (d, m) | yes | no | yes at each fixed (d, m) (D7) |

***

## 9. §A.31 classification of this unit's findings

- **F0** (line-number mapping in #1216's body): BORDERLINE, editorial; planning record only.
- **F1** (Main's construction is a ψ-ontic simulator; Level B as worded is met by any universal
  simulator of QM, so it is non-discriminating unless its mechanism is derived): NEW as a statement about
  Level B; it restates Main:582/:584/:602 for the operational target.
- **F2** (approximate horizon no-go, D10): ELABORATING (Main:640).
- **F3** (NX-1; NX-1 ⇒ a non-monomial admissible operator, FI-1 at level one; FI-1 ⇏ NX-1 and NX-1 ⇏
  layer-flow executability, each with a theory-level counter-model; continuity not necessary for the
  approximate target while the discrete core is, at instrument and law level): NEW. It refines BRIDGE's
  "FI-1 is not necessary at finite accuracy" to the E_r route only.
- **F4** (validity holds while closure fails at finite b; three-outcome table): NEW as a separation
  witness inside Main's own construction.
- **F5** (shuffle-only approximate joint closure: on C closure, validity and compatibility hold and
  coverage fails ε-robustly; on E_f frame-dependent, entangling continuation conditional no; yes on E_r
  with supplied complex data): NEW.
- **F6** (#945 off the OI-derived critical path): POSITIVE (scheduling).
- **F7** (E_f depends on the frame: R1 and Main:562's SIC frame agree on every single-qubit Clifford map
  and differ on CNOT and on states; under R1, Φ⁺ and non-stabilizer states are not represented, at
  trace-norm distance ≥ 2 − √3): NEW. Found by the review of r1 (its B2), verified and extended here
  (r2 F1–F5). Assumption-watch marker: any statement about an "encoded" carrier names its identification,
  since tetrahedral identifications on the same vertex set give different answers.
- **F8** (coverage reported apart from the owner's three outcomes; route C satisfies all three and fails
  coverage): ELABORATING (review B1).
- **F9** (two scope corrections from r2's own checking: NX-1 ⇒ FI-1 holds at the level of the branch, FI-1
  verbatim at level one; MECH-2's P★ shows non-positive escape in one instance, and CP escape is left open
  there): BORDERLINE.

Passes: two by the writer after the first draft; one independent review of r1, which produced one NEW
finding (F7) and one ELABORATING (F8); r2's own checking produced no NEW finding (F9). §A.31's fixed point
(about three to four passes without a NEW finding) is not reached; the next review is the next pass.

***

## 10. Questions for the owner (neutral)

- **OQ1.** Should Level B's definition require that the rule family and the procedure dictionary be
  derived from OI, with no quantum instrument data as parameter or input? Without that clause, Main:598
  meets Level B's shape at fixed (d, m, K, ε) in exact ring by simulating QM (§3.2 B-1), for one fixed
  system, composites counting as one d_A d_B system built with the tensor rule (B-3).
- **OQ2.** Which routes count for an OI-derived Level B: C, E_f (under which identification: R1, SIC or
  U′), E_r? On E_r nothing operational is
  missing and the question becomes selection (§4.1).
- **OQ3.** Is Level B per declared (K, ε) with declared resource scaling acceptable, given that
  all-horizon uniformity is impossible at a fixed finite carrier (D9, D10)?
- **OQ4.** Should #1216's body be corrected for F0 (pre-shift line numbers), under §A.45 maintenance?
- **OQ5.** If a unit 2 is authorized, should its smallest decisive paper question be NX-1 on route C
  (does any access compatible with the stated substratum supply a valid operation that fails to preserve
  diagonal states?) or the E_f identification question (MECH-2's "change in the identification and
  access")?

***

## 11. Verification scope

- **Read in full:** #1216 body and comments c.6741763726, c.6742051100, c.6742191828; #1169
  c.6742190154; #945 body and all five comments; Main:538–:606, :480–:498, :520, :640; Main at
  `7c6ceaaa`, its parent and `02009693` (theorem positions) and `4cef4200`'s change to the Rounding Lemma;
  GR:248–:272; MECH-2 standing, §0, nodes 2, 3 (proof of U2), 6 and 7; AP1 §4.2 and :870–:878; QP nodes
  5 and 10; the Lean statements cited in §§4, 6, 7 (bodies of
  `exists_nonMonomial_of_layerFlowExecutable`, `configurationLevel_not_layerFlowExecutable`,
  `gateFlow_half_not_preservesDiag`, `obs_not_layerFlowExecutable`, `realized_of_instAvail`,
  `polarizedTheory_swap_half_level_one`, `polarizedTheory_not_layerFlowExecutable`; the definitions
  `PreservesDiag`, `IsMonomial`, `ConfigurationLevel`, `LayerFlowExecutable`, `ImplementationClass`,
  `Realized`, `InstAvail`, `Architecture`, `ancBlock`, `genTheory`, `substratumTheory`, `PolGen`,
  `polarizedTheory`; the statements of `obs_availExt_le_substratum` and `gateFlow_unitary`; the other
  identifiers were confirmed to exist only). #1210, #1211: planning heads. Drafts [D]: BRIDGE §0, §5.1
  (parts), §5.3 row; SHM §§1–4; A868 §§0, 4; A1059 §0. No kernel build was run.
- **Checks.** Run `python3 -I -B` from `/tmp`; exact sympy and `Fraction` arithmetic on generic matrices,
  permutations and zero patterns; no OI mechanism. Each group has a control or countercontrol.
  - `probes/approx_generic_checks.py` (r1, unchanged): groups G1–G5, ALL PASS (25 checks).
    Implementation failures, all in the checking code and none in a checked statement: r0 failed G1a
    because sympy did not simplify `Abs` of symbolic eigenvalues (replaced by a determinant test); r1 is
    a passing run of G1–G3 only; two intermediate G4–G5 versions were not retained (the first used
    `simplify` on 512 matrix traces and was stopped unfinished; the second stopped on an assertion
    because one trace was not expanded to ±1, fixed with `expand`). Only r0, r1 and the final version
    are kept, with their outputs.
  - `probes/r2_frames.py`: F1–F5 and controls, ALL PASS (30 checks).
  - `probes/r2_routeC.py`: C1–C7, ALL PASS (24 checks).
  - `probes/r2_finiteb.py`: N5a–c, ALL PASS (3 checks). An instance check of one digitized step of
    Main:578's fixed-point model under a stated reading; it bears on closure, not on the open law-level
    bound.
  - Each r2 output was regenerated twice, byte-identical. The four `review/rv_*.py` were re-run and
    reproduce their recorded outputs byte for byte.
- **Not done:** no computation on any OI mechanism; no simulation of Main's construction beyond the one
  digitized step of r2 N5 (the reviewer's rv_Er was re-run, not extended); no Lean; no git or GitHub
  write; no manuscript change.

## 12. Hashes

- `probes/approx_generic_checks.py`: sha256 `12aac10f6e8f8d6a7bfb7603b35aac8253132534e353791508c3cda443f172c0`
- `probes/approx_generic_checks.out`: sha256 `4337d4afc70c4fdd22deafda2eefeaa926abe044f3b7993ad47b37e9d2865c35`
- `probes/r2_frames.py`: sha256 `aa02e479a0d93ba7ccb6ccb5f9a40c7b0e2065e5f3d7c30d3bdbb2d78010548a`
- `probes/r2_frames.out`: sha256 `a116e91999a566f9d409f857325be4e1d94a47c24da62f7ec6eb73e491be0209`
- `probes/r2_routeC.py`: sha256 `b71749e47f742338d6373aaccae08bdaa96c985c29172b36ba1267e60ac72f97`
- `probes/r2_routeC.out`: sha256 `5626b5a8db40d7ade57542ea297c1c6afb2da32bcd5838ed013d9b02d2e538ec`
- `probes/r2_finiteb.py`: sha256 `383c21567671c73e9565b65c8846dfdc4ab385bf285321cd22b83b72c9b6e07c`
- `probes/r2_finiteb.out`: sha256 `6350b5c11822166bff80b9eacde330a14513390cbda0dc117cc45f26ed4df7b1`
- This file's own hash is reported to the coordinator, not recorded in it.
