# OI-QM-APPROX-1, unit 1: operational equivalence at finite precision, assessed against Main §3.4

**WIP. Revision r4a: editorial cleanup of independently reviewed r4 (ACCEPT WITH NITS); focused diff check and green ordinary CI required. Integration requires separate owner approval.** Only N1–N3 from `REVIEW-APPROX-UNIT1.r4.md` and revision/publication metadata are changed; see `DISPOSITIONS-APPROX-UNIT1.r4a.md`. The r4 source revises the immutable r3 source (`APPROX-UNIT1.r3.md`, SHA-256 `ee432c1b7db91c8e3e0aa3a1e11de68818c8090fa6e1eb34cca478d8be01c659`) against the fresh independent r3 review (`REVIEW-APPROX-UNIT1.r3.md`, verdict **REVISE**, R1–R6). See `DISPOSITIONS-APPROX-UNIT1.r4.md` for those writer dispositions. Claude Code wrote r1 and r2; Codex wrote r3. The [immutable r2 draft](https://github.com/amaybaum/incompleteness/blob/820519cf/handoff-20261109/1216-approx/APPROX-UNIT1.md) has SHA-256 `5ea3f0e4b2fcb20117b9d7d58b8156aae27a526299c3c0ada02e349ff2e4ffd5`. Nothing here is adopted, promoted, or proposed for the manuscripts. Independent acceptance authorizes no computation, new physical premise, manuscript change or merge (#1216 body, "Unit 1").

- **Accountable home:** #1216 (OI-QM-APPROX-1). Parent programme #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1216 c.6741763726 (posted 2026-11-09T13:53:51Z),
  option "Create + start unit 1 (Recommended)", scope verbatim: "Unit 1 (paper-only): does Main's
  existing approximation result meet Level A? What prevents Level B? Is continuous coherent mixing
  still necessary? It ends with a fresh independent review. No new computation beyond labelled exact
  generic checks, no physical premises, no manuscript change, no merge." The original coordinator's
  no-git/GitHub-write boundary describes the paper-only r4 source. Owner (amaybaum), current Codex
  instruction, 2026-11-09: r4a is limited to the three editorial corrections, a focused diff-only
  check and green CI, followed by integration approval. Ordinary draft-PR publication and CI do not
  authorize scientific execution, a new physical premise, freeze, designation, dispatch or merge.
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
  08:36 +0200). At the r3 review snapshot, `origin/main` was `cac5d264`, differing from
  `fd539e15` only in `papers/SM.*`. The r4 writer retains citations pinned to `fd539e15` rather
  than claiming a fresh current-main inventory. "Main" = `papers/Main.md` (sha256 `6144cd4a…6366`), "GR" =
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
2. **Level B: NOT MET as the accountable OI-derived target.** #1216's central question already
   requires a reusable mechanism derived from OI, independently justified observer access and no
   quantum-prediction-selected premise. Main's gluing/uniform construction has Level B's *reusable
   operational shape* at fixed (d, m, K, ε) for one fixed system: one map per supplied instrument,
   adaptivity and gluing by restriction. A composite is treated as one d_A d_B register constructed
   with a *supplied* tensor rule, not as a composite built from independent component realizations.
   It is a discretized ψ-ontic classical simulator: the density register, Kraus maps, Born traces,
   composition and procedure dictionary come from quantum mechanics (Main:582, :584, :600, :602).
   It is a comparison control, **not** a sourced OI mechanism. The OI target needs one physically
   justified recipe defining preparations, access, codecs, interventions and correspondence across
   declared resource budgets, with quantum data used only as the benchmark. Coverage and soundness
   over *complete accessible histories* are distinct obligations (§7.1). The exact-ring simulator's
   capacity depends on its reachable state/net; its finite-b accuracy is open for that implementation.
3. **Candidate single-operation obstruction (§4): NX-1, route-relative.** A valid native
   procedure must escape the configuration route's diagonal-preserving class, or a fixed linear
   frame route's nonnegative-frame class, to approximate *target states or instruments* outside those
   classes under that declared identification. These separations do **not** automatically give a
   floor on *accessible histories*. A fixed two-configuration, fixed-Z-read, repeatedly used-H
   interface has a proved observable-law gap g = (√2 − 1)/2; extending it to a larger carrier,
   coarse decoder or memory needs a distinct proof. On route C the induced **system branch** in a
   generated theory yields a nonmonomial **bare-S** admissible block via architecture soundness and
   discard, but the exact FI-1 on S × Fin 1 also needs `LabelInvariant` transport or a
   `SystemToLevelOne` bridge. With that hypothesis, NX-1 implies FI-1; FI-1 alone is insufficient.
   The polarized countermodel only separates availability properties, not native OI sourcing.
   NX-1 is necessary for the specified state/instrument comparison and not sufficient for Level B.
   On the ψ-ontic register route the abstract simulator already has supplied quantum operations;
   physical source and selection, not a proven OI implementation, remain open.
4. **Continuous coherent mixing (§6).** Not necessary for Level A or for the reusable *shape*
   of the supplied exact-ring simulator. An approximate native target does not logically require
   a continuum of primitive gate times; a physically sourced discrete generating recipe with
   controlled adaptive errors could suffice, but none is established here. On route C, diagonal
   and real-state invariance obstruct coverage in their respective **state/instrument** metrics;
   real-state invariance can be broken by a preparation or map, not necessarily by a particular
   complex Kraus representation. For exact FI-1 at level one the transport seam remains explicit.
   GR's complex drive carries phase under its stated control package; OI has not been shown to
   source that drive. Frame-route behavior depends on the chosen identification.
5. **Dependency matrix (§7).** §7.1 reuses the existing #1169 tests and separates their bounded
   findings from the further coverage and soundness bounds needed for Level B. #945 bears only on
   the simulator's fixed-format capacity.
6. **Owner requirements (§5).** Validity of permitted tests, closure of allowed
   preparations and heralded continuations, quantum compatibility and separate target coverage
   each receive independent verdicts. A clipped/normalized finite-b decoder has valid record
   probabilities by construction while the **internal** exact PSD condition fails at one recorded
   b=12 step; whether the branch approaches the PSD cone or its complete observable law
   converges as b grows remains open. On the directly identified configuration carrier, diagonal
   quantum-state closure holds but quantum-state coverage has a trace-distance floor; the only
   law-level floor proved here is for the specified two-configuration interface. On R1 the fixed
   frame excludes certain quantum states; on SIC those states are representable, but physically
   permitted effects and native continuation remain unresolved. The R1/SIC CNOT channel exclusion
   is conditional on Lemma F (and its SIC extension); it is **not** a no-go for all entangling
   channels or accessible correlations. The register simulator realizes joint laws with supplied
   quantum data, not an OI-derived source.

***

## 1. Conventions

**Evidence layers.**
- [K] kernel-checked Lean on `main` (identifier and module given).
- [P] paper proof in a manuscript on `main`.
- [X] exact computation recorded on `main` (probe named in the manuscript).
- [N] numerical floating-point instance check recorded on `main`; not an exact certificate.
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
- [D] unreviewed or in-revision off-main working draft, used as a hypothesis only
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
A state/instrument norm comparison is not a demonstrated complete-accessible-record comparison;
for Level B the latter needs a fixed, physically sourced separating menu and bounds uniform in resources.
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
| #945 c.6567879503 §2 (assessment/comment with exact checks R-1, R-2) | D4a and §2.2: two-outcome per-parent ledger step refuted (d = 4, b = 24, 6.9063 against 4.0000); the *earlier* `6d494e30` proof review has distinct instances (including 8.0022 against 4.0016), not this number | Support off `main` |
| #945 c.6567879503 §2 (i)–(ii) | §2.2: "the counterexample refutes a proof step, not the final TV bound; reachability … not shown" | Support off `main` (a limitation of the refutation) |
| #945 c.6567879503 §3(b) | D4b: stopping-time repair, Kη ≤ 1/64, 14K²C_{d,R}2^{−b}, graded Motivated | Support off `main` |
| #945 c.6567887681 | Final check of the #945 assessment, ACCEPT-WITH-NITS (D4a, D4b grading) | Support off `main` |
| `proofs/eps-realization/` on `audit/intro-corpus-20261026` at `6d494e30` (head `16fc745d` per #945 c.6657435508; neither is an ancestor of `main`) | Earlier proof-review refutations, including its *different* d=4 witness; not the specific 6.9063/4.0000 assessment figure | Support off `main` |
| #945 c.6657435508 | F945-R "not authorized"; readiness "blocked: owner questions" (§2.2, D4b, D5) | Provenance (planning status) |
| #945 c.6567879503 §1 "No Lean module formalizes gluing, rounding or clipping" | §2.1 A2 evidence row | Support on `main`: this unit's grep of OB/ at `fd539e15` |
| `7c6ceaaa:papers/Main.md` (line 556 states two other exact failures of the per-parent estimate, d = 3 and d = 4) | None: removed by `4cef4200` the same day ("the instance numbers and the undefined estimate are gone") | On `main`'s history, superseded; not used |
| BRIDGE, SHM, A868, A1059 (off-main drafts, [D]) | Rows marked [D] | Support off `main`; used as hypotheses only (§A.46 item 7). Where this unit re-derived a [D] item from `main` or by [G], the row cites that and the [D] use becomes provenance (QP node 10's non-quantumness, §5.1, C7) |
| #868 (J1–J13), #1210 (M-labels), #1211, #1059 | Labels for requirements and planning homes (§4.2, §7 "Shared with") | Provenance |
| Literature [L] | §2, §6, D19 | External sources outside item 8's list; recalled, not re-read |

***

## 2. Question 1: does Main meet Level A?

Level A (#1216): "Any specified finite quantum experiment's observable law is reproduced within ε."

### 2.1 The three constructions

| | A1. Comb with response-table prior | A2. Gluing realization (ε-form) | A3. Uniform continuum realization |
| --- | --- | --- | --- |
| Source | Main:482–:486 (theorem, proof), :520 (Extension, real kernels), :602 ("a fixed finite instrument family is realized exactly by the intervention dilation above, with a product prior carrying the quantum conditionals") | Main:566–:580: theorem, clauses (1)–(5), Rounding Lemma, proof; Main:582 single-dynamics Corollary | Main:596 (adaptive diamond telescoping Lemma), :598 (theorem), :600 (density Corollary) |
| Experiments | Any finite action alphabet and finite-horizon action-labelled family P(x_{k+1} \| x_{≤k}, a_{≤k}); adaptive choice is covered because every context (x_{≤k}, a_{≤k}) is a coordinate [A: the chain-rule reading; Main:482 states "every action sequence", and the contexts are distinct and the prior a product] | A d-dimensional system, a fixed initial state (other preparations enter as outcome-free channels), a finite family F of instruments, each outcome a CP map with finitely many Kraus operators, horizon K ≥ 1; every adaptive protocol over F through K; spatially separated parts via the product construction on a joint register (clause (4)) | Every adaptive protocol of horizon ≤ K with arbitrary ≤m-outcome instruments on ℂ^d, preparations included as channels, by rounding each instrument to a δ-net member, δ = ε/(2K) (K ≥ 1) |
| Accuracy | Exact for arbitrary real kernels (:520); ε only for the rational uniform-tape presentation | TV ≤ K(\|O_max\|−1)/G with exact-arithmetic registers over the instruments' entry ring, G ≥ 1; at finite b **open** (:568) | TV ≤ Kδ + K(m−1)/G ≤ ε with G ≥ max(1, ⌈2K(m−1)/ε⌉), exact regime; m = 1 needs no nontrivial seed grid; R-laws within ε/2 of quantum laws; finite b **open** (:598) |
| Access | Agent writes the action ledger (bijections I_a), reads visible x | Controlled form: visible step counter, agent-written intervention labels and read outcome registers; hidden branch register, predecessor stack and K pre-loaded seeds. Autonomous form (:582): **separately charged read-only program in the enlarged hidden sector**, not a writable visible intervention label | As A2, with net labels: ⌈log₂\|N\|⌉ = O(m d⁴ log(2K/ε)) bits per step of visible intervention record |
| Where quantum content enters | The product prior *is* the quantum conditionals | Instrument data (Kraus operators) in the step maps; the state in the hidden register; Born trace q_o = Tr I_o(ρ̃) computed by the step map (:580, :582) | As A2, over the whole net |
| Carrier | C-dyn (classical response coordinates in hidden memory) | C-dyn: finite bijection on configurations; system in E_r | As A2 |
| Evidence | [P]; [X] `intervention_probes.py` (n_V = \|A\| = K = 2, exact), `lg_comb_probes.py`; real-kernel Extension: [P], rational instance [X] `review4_probes.py` P-G. Passive (action-free) law: [K] `S_imp_D`, OB/Equivalence.lean:422 | [P]; [X] `opglue_probes.py` at (d, K, \|F\|) = (2, {2,3}, 4), exact over ℚ(√2), checks 11–13. No Lean module formalizes gluing, rounding or clipping (#945 c.6567879503 §1; this unit's grep of OB/ for "gluing", "rounding", "opglue" found none relevant) | [P]; [N] `opglue_probes.py` checks 8–9 (floating-point qubit instances, tolerance 1e−12). Telescoping Lemma: [P], standard |
| Resources | Main:520 gives \|C_H\| = n^N (n+1)^K (K+1), N = Σ_{k=1}^{K} n^k, for the passive (action-free) comb. For the action-labelled comb N counts the (x_{≤k}, a_{≤k}) contexts and the action ledger adds its own factor [A]; exponential in K either way | Exact ring: log₂\|C_H\| ≤ (K+1) log₂\|V_reach(F,K)\| + K log₂ G (:576). Fixed point: O(K d² b + K log₂ G), whose accuracy form depends on the open finite-b bound | Exact ring: capacity grows with the net (:598). Reading [A]: \|V_reach\| ≤ Σ_{k≤K}(\|N\|m)^k, so log₂\|C_H\| = O(K² m d⁴ log(K/ε)), polynomial; the transition law's description scales with |N| = exp(O(m d⁴ log(1/δ))) (:598); this does not bound the bit complexity of arbitrary real instrument entries or priors |

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
  bound 4.0000 [OFF: #945 c.6567879503 §2, assessment-review checks R-1/R-2]. The counterexample refutes a proof
  step, not the final TV bound; reachability of a negativity-dominated register from an exact initial
  register is not shown [OFF]. These **two-outcome numbers are from the #945 assessment comment**;
  the earlier proof review at `6d494e30` records different witnesses (one d=4 case gives 8.0022
  against 4.0016), and must not be cited for the quoted pair. A stopping-time repair is graded
  Motivated and is not authorized (F945-R). This unit does not duplicate it.
- *Precision distinction.* Arbitrary finite accuracy of finite observable histories (A1 with a
  real prior, A2/A3 with exact-ring branch entries and a finite seed grid) does not require a
  proved error bound for the clipped/normalized fixed-point E_r implementation. The latter is
  one hardware/accounting route, not a general no-go for finite-precision observable laws.
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

**B-1. The rule family is supplied, not derived (decisive failure of accountable Level B).** The step maps apply supplied CP maps to a
supplied state and compute supplied Born traces (Main:580, :582). The construction "is an operational
realization theorem, not a uniqueness theorem: the same reversible machinery can realize non-quantum
finite instrument families" (Main:584), and D_finite's closure contains non-quantum theories (Main:600).
Main itself names what remains: "What remains is selection" (Main:602). Column (iii) holds within ε;
column (ii) is empty. **Consequence:** Main meets the abbreviated Level-B row's *reusable
operational shape*, but **does not satisfy #1216's Level B target**, whose central question already
requires OI-sourced mechanism, independently justified access and a single rule across resources.
The shape alone is non-discriminating for the same reason Q_fb representability is (Main:556:
"representability alone is not the framework's discriminating content"). Quantum formalism may
specify the benchmark; it cannot be chosen as the physical implementation rule. The remaining
implementation evidence question is OQ1, not permission to add the derivation requirement.

**B-2. An all-horizon target containing sufficiently rich rotations fails on a fixed finite carrier; the resource envelope remains explicit.**
Main:640 proves the exact form: a bijection on a finite set has finite order L, so a fixed realization's
multi-time law is exactly L-periodic. *Approximate form [A + G2]:* let a fixed finite realization on S
realize "repeat the rotation K times" by repeating one fixed bijection K times (repetition is
compositional), and set L := lcm(1, …, |S|). Every bijection of S has order dividing L, so the
realized law at horizon K is L-periodic in K. If the target class contains the rotation by π/L about y
(it does if it contains all rotations about one axis), the qubit protocol "|0⟩, K such rotations, then
Z" has P(0) = cos²(Kπ/(2L)), which is 0 at K = L and 1 at K = 2L [G2b], while the realization gives the
same law at both; so it errs by ≥ 1/2 in TV at one of them. **Scope:** one fixed S and prior, one fixed bijection repeated for the operation, the stated
preparation and readout, a target class containing the rotation by π/L selected for that S, and
horizons L and 2L (not a fixed-depth witness uniform over resource sizes). It does not exclude a
restricted periodic target class, a carrier growing with K, or implementations whose procedure for
a repeated operation changes with K. It proves no error floor at fixed experimental depth when
resources increase. #1216 already requires declared dependencies on (K, ε, memory); the question
is which physically sourced resource envelope can carry the common operational correspondence.
Classification: ELABORATING (approximate extension of Main:640).

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
the single-dynamics form the read-only policy is in the enlarged **hidden** sector, with size up to
Θ(|O_max|^K log₂|F|) bits, separately charged as an initial condition (Main:582). This is not the
agent-written visible intervention label of the controlled form.

***

## 4. Question 3: the smallest missing operational property

### 4.1 Three routes, kept apart

- **Route E_r (ψ-ontic register).** Main's simulator is a finite bijection and "uses no property of the
  substratum beyond finiteness and reversibility" (Main:582); the characterization's realization datum
  is an existentially chosen bijection on 𝒞_V × 𝒞_H (Main:544). Whether the simulator also meets C1, C3
  and C4 is not checked here. Within this **abstract finite-reversible simulator with its supplied E_r state register,
  instrument inputs and dictionary**, no further gate operation is required to construct the
  representation. That does **not** establish C1/C3/C4 or physical availability under native access.
  The remaining gap is sourcing and selection — why actual OI dynamics and access implement the
  same rule rather than some other finite bijection (Main:602).
  That is a derivation obligation, not an operational one.
- **Route C (configuration carrier as the quantum carrier, Main:564's interface, no memory outside ℂ^S).**
- **Route E_f (fixed linear identification: R1, SIC or U′, §1).**

### 4.2 NX-1, stated for routes C and E_f

**NX-1 (candidate one-operation obstruction, in a specified state/instrument norm).** Relative
to a declared carrier, encoding and observer interface, some native procedure — built from OI
dynamics and access without quantum instrument data as parameter or input — induces a valid
(completely positive, trace-non-increasing **branch of a normalized instrument**) transformation
at positive distance from the encoding's *classical class*:
- route C: the maps that preserve diagonal states (`PreservesDiag`, OB/DiagonalTheory.lean:68);
- route E_f, under an injective identification (R1 or SIC): the maps whose frame matrix is entrywise
  nonnegative (MECH-2 Lemma F's class). For the non-injective U′ the frame matrix of a map is not
  unique (MECH-2 node 7), and no class is fixed here.

**Necessity for identified states/channels [A]; operational transfer not automatic.** The two
classes are closed and composition-stable **as classes of fixed linear maps on subnormalized
branches**. A realized record history composes selected linear branches; forgetting a record sums
branches of a legal instrument. Such a sum stays in the underlying diagonal/frame cone, but an
**arbitrary** sum of trace-nonincreasing maps need not itself be trace-nonincreasing or constitute
a valid instrument. Conditioning on a herald of positive probability normalizes only afterward,
by division by its probability (a generally nonlinear step). Route-C attachment/discard preserves
diagonality for the specified access. Route-E_f attachment and discard require a **fixed product
identification, the operation set and H-LIFT at every intermediate cut**, or a map retaining the
correlated joint system; the claim is conditional on those hypotheses (MECH-2 Lemma F [W] and the
SIC extension [A]). If all admitted branches remain in 𝒞, target states or channels a positive
distance from 𝒞 cannot be approximated **in that matrix comparison**, at the corresponding
carrier and instrument norm. A gap in complete accessible histories requires an accessible
distinguishing menu and a uniform quantitative transfer under resource scaling, not merely a
mathematical separating observable or an injective frame. The target contains such matrix examples:
- *Route C:* for every diagonal D, tr((|+⟩⟨+| − D) σ_x) = 1, so ‖|+⟩⟨+| − D‖₁ ≥ 1; the Hadamard
  channel is at trace distance ≥ 1/2 on the input |0⟩⟨0| from every diagonal-preserving map [G1a–b];
  likewise for composites, x+ ⊗ z+ against every diagonal D with witness X⊗Z [G4].
- *Route E_f (R1 or SIC):* the two identifications share the vertex set, and a single-qubit rotation O
  acts by M_ij = (1 + 3 a_i·O a_j)/4 in both: the frame matrices of all 24 single-qubit Clifford
  unitaries coincide in the two frames [G: r2 F2; RV rv_frames R1b]. The 12 rotations of A₄ give
  permutation matrices; each of the other 12, the Hadamard and S among them, has an entry −1/2 [G3;
  r2 F2]. The nonnegative matrices form a closed set and, the identification being injective, the frame
  matrix of a channel is determined by its action on states, so each such rotation sits at a positive
  distance from Lemma F's class **in the fixed linear-map comparison** [A, compactness]; injectivity
  alone gives no physically accessible law separation or uniform-in-resource reconstruction bound. For composites the two frames differ: the CNOT
  conjugation's frame matrix has minimum entry −1/4 under R1 and 1/4 − √3/3 ≈ −0.327 under SIC, in
  either orientation [G5b (SIC); r2 F3 (both); RV rv_frames R1c]; SWAP, which preserves Pauli weight,
  has the same (permutation) matrix in both [r2 F3].

*Law level (only the fixed two-configuration route-C interface).* The channel/state matrix gaps
above are not themselves observable-law gaps. Here there is a specific accessible witness with no
hidden internal configurations: prepare the identified basis state |0⟩, apply the **same**
outcome-free stochastic map T as the implementation of H once or twice, then make the exact Z
basis read. Write p = T(0|0), q = T(0|1). Quantum probabilities for outcome 0 are 1/2 and 1;
the stochastic one-step deviation is |p − 1/2| and the two-step deviation is
1 − p² − (1−p)q ≥ p(1−p). Let g = (√2 − 1)/2, so g = 1/4 − g². Either
|p − 1/2| ≥ g or p(1−p) ≥ g; equality is attained at p = 1/√2, q = 1
[G: r2 C5; RV rv_routeC C5]. This is a **TV floor on the recorded Z outcome** for that
specified fixed-preparation, fixed-readout, closed two-configuration interface. It does not
extend to larger carriers whose extra configurations are hidden by a coarser decoder, altered
preparations or reads, retained memory, or E_f frames. Absence of memory **outside** ℂ^S is
insufficient for that extension, because S itself may conceal degrees of freedom under the decoder.
At a resource family Level B needs a proof of uniform separation on the same accessible protocol
correspondence, or a uniformly conditioned reconstruction bound. The X, Y and X⊗Z observables used
for state trace-norm witnesses elsewhere need not be native accessible effects. Main:562's SIC
embedding, which holds all qubit states but lacks some sharp effects as valid responses, is a
countercheck. The P★ frame non-PSD diagnostic likewise requires the specified Y read (MECH-2).

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
- *NX-1 ⇒ nonmonomial bare-S operator; exact FI-1 conditional* [A from K-lemmas, not
  itself a kernel theorem]. A system-induced branch non-preserving of diagonals, whether obtained
  directly or by Main:564 rule (f), is **itself an available instrument branch on bare S** in
  `genTheory`: compose uniform ancilla attachment/preparation with the level instrument and apply
  `InstAvail.discard`. By `realized_of_instAvail` and `Architecture.block`/scalar closure, it is a
  finite sum of conjugations by **bare-S** admissible Kraus operators; the uniform discard formula
  `discardWith_uniform_conjChannel` expresses the summands as `1/n`-weighted ancilla blocks.
  If every such operator were monomial, the branch would preserve diagonals. Therefore some
  bare-S admissible block is nonmonomial. **The exact FI-1 predicate** is on `S × Fin 1`, not bare S.
  `Architecture` has no relabelling axiom: moving the witness to `S × Fin 1` needs
  `LabelInvariant` transport of the implementation or an appropriate `SystemToLevelOne` theory
  bridge followed by soundness. Under one of those named hypotheses, system-NX-1 ⇒ exact FI-1.
  For an *arbitrary higher-level* off-diagonal branch, a system reduction detecting it must first
  be shown; partial trace may remove its coherence. This is a scoped implication, not one proved
  by a missing implicit relabelling rule.
- *FI-1 ⇏ system-NX-1* [A + G, at kernel-definition level; not kernel-checked]. Counter-model: the
  column-monomial class CM (at most one nonzero entry in each column).
  - CM satisfies the five fields of `Architecture` (OB/ImplementationLocality.lean:506–515): identity,
    products, scalar multiples, ancilla projectors and ancilla blocks `ancBlock K f e`
    (OB/AncillaClosure.lean:457) of CM matrices are CM [A; G: r2 C1].
  - K = |0⟩(⟨0| + ⟨1|)/√2 (on S × Fin 1) is CM and not monomial, so FI-1 holds [G: r2 C3].
  - Every CM conjugation maps diagonal matrices to diagonal ones [A; G: r2 C2], so by
    `realized_of_instAvail` and `preservesDiag_sum` every branch of `genTheory CM` at every level
    preserves diagonals, and so does every system map built by rule (f); NX-1 fails.
  - `InstAvail.op` requires Kᴴ K = 1 (OB/ImplementationLocality.lean:271–272), and CM's isometries are
    exactly the monomial ones [A; G: r2 C3]. K is an admissible nonmonomial FI-1 witness, not an
    isometric primitive; no availability of its conjugation is claimed or needed. Every available
    branch of `genTheory CM` preserves diagonals. The reviewer's C4 (rv_routeC) checks the same model.
- *Layer-flow executability ⇒ level-one availability version of NX-1* [A from K-lemmas]. If T executes the layer flow of an involution σ
  with σ x ≠ x (`LayerFlowExecutable`, OB/LiftAudit.lean:112), then at level one and t = ½ the
  gate-flow conjugation is available, it is unitary (`gateFlow_unitary`, OB/LiftAudit.lean:69, which
  needs σ involutive), and it does not preserve diagonals (`gateFlow_half_not_preservesDiag`,
  OB/LiftAudit.lean:155, at (x, 0)).
- *Level-one availability version of NX-1 ⇏ layer-flow executability* [A from K-lemmas]. In `polarizedTheory (Fin 2)`
  (= `genTheory PolGen polGen_arch`, OB/C5Discovery.lean:247) the gate flow of the swap at t = ½ is
  available at level one (`polarizedTheory_swap_half_level_one`, OB/C5Discovery.lean:325) and does not
  preserve diagonals (`gateFlow_half_not_preservesDiag`), so NX-1 holds there; and
  `polarizedTheory S` executes the layer flow of no σ with a moved point
  (`polarizedTheory_not_layerFlowExecutable`, OB/PolarizationClosure.lean:395). Three kernel theorems,
  composed here; not stated as one theorem. r2 C4 checks the half-time entries (1 ± i)/2 as a control.
  `polarizedTheory` adds two operator images to the stated access, so this separates the two
  properties and says nothing about OI's access.

**Comparison scope.** With the named level-one transport and an admissible system-induced
non-diagonal-preserving branch, NX-1 implies FI-1, and the column-monomial countermodel shows
FI-1 alone is insufficient. For witnesses *already at level one*, the polarized example also
separates the availability property from full layer-flow executability. These are statements
about generated architectures/available operations, not independent evidence that OI sources
the polarized witness. Without transport, no unqualified strict-order claim using the exact
FI-1 predicate is made. NX-1 is a **single-operation obstruction candidate**, not an absolutely
minimal missing premise: no order over all possible obligations is established. The E_r simulator
escapes these route-relative identifications through supplied register arithmetic.

**Not sufficient.** NX-1 does not give:
- *density* — the next link, **NCG** (native compositional generation): native procedures whose induced
  instruments have adaptive compositions ε-dense in the class for every ε, with resources scaling by a
  declared rule. At a fixed finite carrier, the encoded maps induced by single bijections (with fixed
  ancilla initialization and fixed heralds) form a finite set, so NCG needs adaptive procedures of
  unbounded length **with records/fresh supply or other added operational resources**, a carrier
  refined with ε by a target-independent rule, or non-bijective native operations [A]. Words
  of any length in a *fixed finite permutation group* remain a finite set when only the terminal
  permutation is observed, so word length alone is not enough. Under MECH-2 U2 [W] the encoded unitaries under R1^⊗n stay in A₄ ≀ S_n at every n;
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

"Admissible state space" and the comparison are stated for each claim. The owner's definitions
remain separate: (i) **validity of every permitted product test**, (ii) **closure of all admitted
preparations and positive-probability heralded continuations**, and (iii) **quantum compatibility of
the resulting joint states under the specified comparison**. *Coverage* of the required target
class is a fourth column, not inferred from the three. Recorded native probabilities may be valid
while their **chosen decoded representation** is not a quantum state. A model's own classical
posterior closure is not automatically quantum-state closure. All branch-composition statements
refer to **subnormalized linear maps**; normalize only positive-probability postselected branches,
not zero-probability heralds. The source level is attached to each cell. States/channels and the
laws of accessible complete records are different comparisons (§4.2, §7.1).

| Claim | Admissible space / comparison | Validity of permitted tests | Closure under permitted continuations | Quantum compatibility | Coverage of target |
| --- | --- | --- | --- | --- | --- |
| A1 comb / response table (Main:482, :520, :602) | Loaded response-coordinate simplex; **observable conditional laws**, not decoded quantum joint states | **Holds for the loaded family:** product-prior measures and their nonnegative conditional laws [P] | **Classical posterior closure holds** on positive-mass histories [P]; **quantum-state closure unassessed/inapplicable** with no decoded quantum state | **Observable laws match exactly** if quantum conditionals are loaded; non-quantum data (e.g., PR-box) are also legal stochastic tables [P] | Only the loaded family, not a shared independent OI implementation |
| A2 gluing, exact ring (Main:566–:580) | PSD **subnormalized** branch matrices in E_r; quantum laws over F | **Holds** for legal instruments: CP preserves nonnegative branch traces; aggregate trace-preserving instruments and finite seed thresholds give valid realized outcome frequencies [P] | **Exact PSD closure** under CP linear branches, legal coarse-grainings and positive-probability conditioned continuation, including joint-register tensor instruments [P] | **Complete adaptive realized laws** within K(\|O_max\|−1)/G TV of the supplied QM laws [P,X]; instrument rules imported | Every protocol over F through K in the stated grid regime [P] |
| A2 fixed-point b (Main:568, :578, :580) | Clipped/normalized output **decoder** versus possibly non-PSD Hermitian internal E_r matrices | **Decoder record probabilities valid by construction** [P]; this does not imply a valid internal quantum state or a valid wider product-test menu | **Exact internal PSD closure fails in an instance:** b=12, K=1, digitized y-rotation from exact \|0⟩⟨0\| has determinant −325/2097152 under stated rounding [G N5; RV]. **Approximate PSD closure as b→∞ open**; no uniform lower floor shown | **Finite-b complete-law TV approximation open**, not refuted by N5 and not proved by valid clipped probabilities | Finite-b capacity/accuracy claim open; no general obstruction to finite-accuracy laws follows |
| A3 uniform, exact ring (Main:598) | PSD E_r net-register branches | **Holds** as exact A2 for each legal net instrument [P] | **Holds** as exact A2 for positive-probability histories [P] | **Observable laws within ε** for fixed (d,m,K), supplied net dictionary [P] | All ≤m-outcome protocols at horizon ≤K for fixed d, exact ring [P]; no all-d claim |
| A3/A4 density (Main:600) | Fixed-(d,m) finite-test topology of operational law sets | Holds in each construction R^Q_n [P] | Holds in each exact-ring quantum-shadow register [P] | Each shadow is within its declared error of QM laws [P] | **Density** at fixed (d,m); closure of the larger finite-deterministic class also includes non-quantum theories [P] |
| Route C, stated substratum and access | Diagonal density matrices on directly identified ℂ^S; native configuration read and permitted instrument families | **Holds for specified native legal instruments**: positive branches **and aggregate trace preservation**, plus diagonal reads; not inferred from CP alone [A from K-lemmas, instrument normalization] | **Holds exactly** inside the diagonal quantum subset under permitted preparation, read, coarse-graining and positive-mass heralding [A from K-lemmas] | **Each generated, legal diagonal-preserving instrument** is a quantum instrument in this interface; no claim of all quantum instruments [A]; complete record laws quantum-compatible within this restricted class | **State/instrument coverage fails** for coherent states at trace distance ≥1/2 in directly identified C; **accessible-law floor proved only** for fixed two-config H/H,Z interface, g=(√2−1)/2. Neither floor automatically transfers to growing carriers or coarser reads |
| Route E_f(U′), QP node 10 composite | Recorded native Pauli table versus candidate joint quantum state | **Pauli-fragment validity only** for the specified zero-completion table, per A868 [D]; unrestricted product-test validity unassessed | **Unassessed** for the node-10 table; positivity on a limited set of reads does not imply closure [D] | **Fails for specified table:** XX=ZZ=1 demands Φ⁺ and YY=−1, while table gives YY=0 [W; G r2 C7] | Claimed table-CNOT action fails on (x+, z+) per A868 [D]; other instruments unassessed |
| Route E_f(R1), MECH-2 P★ one cell | Native record probabilities versus R1-decoded quantum Bloch ball | **Native recorded read frequencies** 5/8 and 3/8 are valid [W]; **all permitted product-test validity unassessed**; no inference of CP or positivity from frequencies | **Decoded quantum closure fails** for record-1 non-PSD r=(1/3,−1/3,−1), \|r\|²=11/9 [W]; other cuts unassessed | **Fails in R1 decoder on record 1** by direct state calculation [W]; a stated Y read is needed to distinguish by the relevant diagnostic, so observable compatibility has its own access condition | R1 excludes certain target states at fixed-frame trace-norm distance; U2 excludes specified encoded unitary permutations under its hypotheses [W]; no general accessible-law/entangling-channel no-go |

**Independence and limits.** The finite-b example separates **validity of decoded record
probabilities** from **exact internal PSD closure**; it does not decide approximate closure,
finite-b law accuracy, or arbitrary product-test validity. QP node 10 separates reported
Pauli-fragment validity from quantum completion of that same table, not validity of an unrestricted
menu. P★ has valid native recorded frequencies but a non-PSD decoded branch, with broader
product-test validity open. A1 posterior closure is in its classical model, not an asserted
quantum-state-space closure. On route C, legal normalized instruments are required; diagonal
CP alone is not enough. Even where all three owner-defined outcomes hold for a restricted
class, target coverage remains independent.

### 5.2 Can approximate joint-state closure be reached with finite shuffle-only dynamics, where exact closure needs a complex operation?

"Shuffle-only" is read as: each native dynamical step permutes a finite configuration set;
no nonmonomial coherent operation is generated merely by these permutations. State-space
**closure**, **validity**, **quantum compatibility**, and **coverage** are assessed independently.
For approximate closure, an exact finite-b PSD counterexample alone is not a nonzero asymptotic
error floor. Every trace-norm witness below concerns a **specified identification**, not
necessarily an accessible native test. This is a carrier-relative analysis, not a global no-go.

1. **Route C: diagonal-state closure, legal-test validity and restricted QM compatibility; target
   state coverage fails in the directly identified carrier.** Monomial branches preserve diagonal
   quantum states under the stated preparations and reads [A from K-lemmas]. The product-target
   witnesses x+⊗z+ and y+⊗z+ have trace distance ≥1/2 from every diagonal density matrix under the
   stated identification [G4; r2 C6]. The witness observables X⊗Z and Y⊗Z must be implemented as
   native reads before this becomes a complete-law no-go; they are not shown accessible here.
   The one **accessible Z-record** floor is instead the fixed two-configuration repeated-H
   interface of §4.2. These bounds do not automatically persist under growing carrier sizes,
   internal hidden configurations, coarser decoders or new access. The requirement for a
   non-diagonal-preserving and a reality-breaking **preparation or operation** therefore survives
   only at the corresponding identified state/instrument target, subject to physically specified
   preparations/reads, not as a proved full Level-B lower bound.
2. **Route E_f: frame-dependent representation and conditional channel obstructions.**
   - *SIC state representation*: every quantum joint state has nonnegative product-SIC
     coordinates, since they are product POVM probabilities [A; G5a for Φ⁺]. Rational counting laws
     can approximate those coordinates, but whether OI supplies the preparations and sharp effects
     is a separate question. Main:562 expressly notes that sharp effects lack valid four-ontic-point
     responses in its SIC embedding. Representation does not imply operational availability.
   - *R1 state representation*: r=−v₀/√3 has coordinate (1−√3)/4, and Φ⁺ has product-frame coordinate
     −1/8 [G r2 F4; RV]. Their fixed-frame trace-norm distance from any represented state is
     ≥2−√3 [G r2 F5]. This is **state representation** separation, not automatically separation
     of native permitted records; a frame-coordinate witness may be unphysical/inaccessible.
   - *Encoded quantum closure*: point-mass classical laws can decode to non-PSD matrices in both
     frames [G5d; r2 controls], so restricting admitted states and retaining a fixed product
     identification, access and herald rule is substantive. P★ records an R1 instance [W]; its
     non-PSD diagnostic needs the stated Y read to become a record-level distinction.
   - *CNOT channel*: its fixed-frame matrix has a negative entry (R1 min −1/4; SIC
     min 1/4−√3/3) [G5b; r2 F3; RV]. Under MECH-2 Lemma F (R1 [W]) or its claimed SIC extension
     [A], and their operation/H-LIFT/product-identification hypotheses **at every cut**, no
     native frame-nonnegative branch approximates **the CNOT channel in the fixed channel norm**
     below some positive distance. This does **not** exclude every entangling channel, generation
     of any given entangled state, or complete accessible CNOT correlations without a separating
     test and uniform resource bound. MECH-2 U2's narrower no-entangling-unitary-*permutation*
     conclusion remains conditional on its orthogonal R1 hypotheses, not extended to SIC.
3. **Route E_r: supplied-data register simulator reaches exact PSD closure in exact-ring arithmetic.**
   Main's finite reversible bijection implements given Kraus data on a digitized density register;
   under exact-ring entries each legal instrument's subnormalized branch is PSD, normalized
   positive-mass heralds are quantum states and its adaptive observable laws approach quantum
   predictions as G increases [P]. Joint-register tensor rules are *imported*. This is
   mathematical representation and a control for Level A, **not OI-derived Level B**. In fixed-point
   b registers the N5 one-step instance disproves **exact internal PSD closure** under its stated
   rounding, but does not establish a uniform PSD-cone error floor; **approximate closure and
   complete-law accuracy remain open** for that clipped/normalized implementation. Its decoded
   record probabilities can be nonnegative even when the internal state is non-PSD.

**Answer.** Pure permutations on the **same directly identified configuration carrier** preserve
its diagonal quantum state subset but fail to cover coherent target states in the specified
matrix norm. Under R1, even representation of some joint states fails; under SIC the state
coordinates exist but physical effects/continuations remain the obstacle. An E_r simulator can
represent the laws using finite shuffles, because it **stores quantum structure as data**.
The results do not decide whether a common OI-sourced family attains arbitrary finite accuracy
on complete accessible histories, and the unproved finite-b register approximation cannot be
promoted to a general obstruction.

***

## 6. Question 4: is continuous coherent mixing still necessary?

| Target / comparison | Continuum of native gate times | Diagonal-invariance escape | Reality-invariance escape / phase | Evidence and qualification |
| --- | --- | --- | --- | --- |
| Exact endomorphic operational QM on C (existing #1169 architecture) | The stated kernel *route* assumes a continuous layer flow at every intermediate time; this unit does not weaken the exact characterization | Layer flow implies a nonmonomial level-one operator, but the converses are not established | Phase intervention is stated, not sourced by OI | [K] `uncountableNonMonomialRays_of_layerFlowExecutable`, `exists_nonMonomial_of_layerFlowExecutable`, `obligations_independent`; GR:250–260 |
| Level A and reusable shape of supplied simulator | **No**: Main's exact-ring finite reversible realization does not require a continuum of primitive native coherent controls | Not required on the visible configuration carrier | Complex Kraus data and Born traces are **inputs**, not native coherent operations | [P] Main:566, :580, :598. This does **not** meet OI-derived Level B |
| OI-native approximation with direct C state/instrument identification | No general requirement of continuous **primitive** controls follows from the approximation criterion; a physically sourced, compositional discrete family may work, but is open | **Required** to approximate named non-diagonal states/channels in this norm; system branch yields nonmonomial bare-S operator, exact FI-1 needs transport (§4.2) | **Required to escape real-state invariance if** preparations, attachment and operations are all real-preserving and target y+ is included. Could be a preparation **or** an operation; the existence of complex Kraus entries alone is not the property | [A+G1,G4] for matrix comparison. Accessible-history lower bound proved only in the fixed two-state H/H,Z setup. Discrete generation also needs uniform adaptive errors and physical source |
| Fixed-linear-frame E_f | No: native configuration-level coherent mixing is not by itself the operative resource | Depends on physically selected frame and access, and Lemma F's product/H-LIFT hypotheses | A phase-capable complex drive can be supplied in GR but no native source is derived here | [W] MECH-2 R1, [A] SIC extension; separate channel norm from record laws |

A non-real **Kraus representation** does not imply a channel breaks reality: real-state-preserving
channels may admit complex Kraus decompositions. The invariant formulation is that all allowed
preparations and subnormalized branches preserve the real symmetric states; a specified target
such as |+i⟩ is at trace distance ≥1/2 from that set by a Y witness **in the identified
state comparison** [G1c; A]. To make it a Level-B observable-law obstruction requires a native
accessible Y-sensitive test, or a bounded reconstruction map, uniform across resources.

Finite words in a fixed finite permutation group cannot be dense in an infinite unitary group
when only the terminal permutation is read; adaptive records, fresh supply, changes in the
carrier or observer-access structure are additional resources that must be counted. In
principle a discrete native generator family and a repeatable implementation could approximate
continuous target gates through composition, but no such family or uniform error analysis is
sourced from OI here. The complex drive **carries the phase** under GR's specified control
package; the phase is independently sourced from the layer flow **only in the scoped
`obligations_independent` statement on Fin 2**. Neither claim derives the drive from native OI
(Main:590). These are not H-Bell implications (#1169 decision 4).

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
| D4 | Clipped/normalized finite-b **complete-law** TV bound and capacity–accuracy | open | Main:568, :578, :580, :602 [P] | E_r | fixed-point b bits; window rule; valid clipped decoder probabilities do not prove closeness or PSD register | #945 only |
| D4a | Old per-parent negativity estimate | disproved **off `main`**; Main:578 now explicitly not established | [OFF] two-outcome assessment instance 6.9063 vs 4.0000, #945 c.6567879503; earlier **different** proof-review instances at `6d494e30` (one 8.0022 vs 4.0016) | E_r | d=4, b=24 for assessment pair; reachability of negativity-dominated parent not demonstrated | #945 only |
| D4b | Stopping-time repair, TV ≤ K(\|O\|−1)/G + 14K²C_{d,R}2^{−b} | conditional (**Motivated**, unreviewed, unauthorized) | [OFF] #945 c.6567879503 §3(b) | E_r | Kη ≤ 1/64; exact initial register; Rounding-Lemma constant | #945 only |
| D4c | One-step failure of **exact internal PSD closure** in finite b | counterexample at b=12 only; **asymptotic approximate closure open** | [G] r2 N5; [RV] rv_finiteb; no realized-law counterexample | E_r | specified digitization/rounding, K=1, exact initial register | #945 (scope only) |
| D5 | Rounding Lemma, instrument level (Main:578) | stated proved on `main` (Main:578: "the instrument-level inequality is proved"); the complex-entry constant is contested off `main` (#945 owner question 6, undecided) | [P]; [OFF] for the qualifier (support off `main`, §1.1) | E_r | fixed-point dyadic model | #945 only |
| D6 | Uniform continuum, exact budget (Main:598) | proved; \|N\|-independent capacity open | [P]; [N] `opglue_probes.py` checks 8–9 (floating-point instances, tolerance 1e−12) | E_r | fixed (d, m, K, ε); δ-net rounding as dictionary | #945 (capacity), #1169 |
| D7 | Finite-test density at fixed (d, m) (Main:600) | proved; union over (d, m) open | [P] | E_r | exact ring | #1169 |
| D8 | Classical-dimension obstruction to exact equivalence (Main:560) | proved (factorization half); unboundedness imported [55] | [P], [X] `nogo_probes.py` | any finite ontic carrier | ordinary prepare–ontic–measure interface | #1169 |
| D9 | No uniform finite realization of the instrument algebra (Main:488); finite-order periodicity (Main:640) | proved | [P] | C-dyn | fixed finite S | #1169 |
| D10 | No fixed-carrier all-horizon approximation for a target **including the carrier-dependent rotation** π/L | paper argument, unreviewed; **no fixed-depth resource-uniform floor** | [A+G2] | C-dyn | fixed S and prior, fixed bijection for each repeated step, declared basis prep/read, horizons L and 2L, class containing this rotation | Ind (elaborates D9) |
| D11 | Non-uniqueness: the realization machinery realizes non-quantum families (Main:584, :600, :362) | proved | [P] | C-dyn / E_r | — | #1169, #1210 (selection) |
| D12 | Selection: why the substratum's bijection is a quantum-shadow one (Main:602) | open | — | E_r route | — | #1169, #1210 |
| D13 | Five completion conditions characterize exact finite operational QM (Main:564) | proved, exact target | [K] `exactAll_iff_physical_general` (OB/GeneralCarrier.lean:100), `five_way_minimality` (OB/RankGapTheory.lean:702) | C (complex kinematics given) | complex matrix kinematics taken as given | #1169 (exact; not altered here) |
| D14 | Approximate analogue of the five conditions | open (not stated anywhere read) | — | C | — | Ind |
| D15 | FI-1 necessary for the exact target | proved, one direction | [K] OB/ExecSource.lean:52 | C | structural architecture | #1211, #1169 |
| D16 | Monomial generating substratum/observer access supplies no nonmonomial implementation in the stated interface; wave lift unresolved | proved for configuration-level class; wave lift open | [K] `substratumClass_configurationLevel` (OB/ManuscriptAxioms.lean:129), `obs_availExt_le_substratum` (OB/SubstratumInterfaceAudit.lean:837), `realized_of_instAvail` and monomial preservation; layer-flow absence is separate [K]; BRIDGE [D] for wave lift | C | stated read/write access, generating theory | #1211 |
| D17 | NX-1 necessary for C **state/channel target**; system branch gives nonmonomial **bare-S** block; exact FI-1 needs `LabelInvariant` transport or `SystemToLevelOne`; two-config H/H,Z supplies g record-law gap only on that interface; FI-1 insufficient, and polarized counterexample conditional on added generators | paper argument, unreviewed; no general Level-B law-floor | [A from K-lemmas +G1,G4; r2 C1–C6], `Architecture.block`/`discardWith_uniform_conjChannel` and level-one transport seam | C | declared direct identification, legal system-induced branch, matched tests/reads; extra assumption to move S→S×Fin1 | Ind, refines #1211 |
| D18 | Real-state preservation obstructs preparing/transforming y+ **in state comparison**; no accessible-law floor established | paper argument, unreviewed | [A + G1c] | C | native preparations, attachments and maps **all** preserve real symmetric states; Y-sensitive native read needs proof; complex Kraus alone not decisive | #1211 (O1), #868 J3 [D] |
| D19 | Dense *physically sourced* discrete generation as possible route | conditional in unitary/state comparison; **adaptive law error open** | §6 [A] | C | one rule across resource sizes, generators available physically; adaptive/side-system error bounds, preparations, ancillas, records and reads; terminal finite-group words alone insufficient | Ind (contrast with #1211 exact) |
| D20 | MECH-2 Lemma F, Theorem U2, Theorem NC | conditional (W record; open per SHM Q6-O8 [D]) | [W] MECH-2 §0 | E_f(R1) | orthogonal frame (R1^⊗n), H-LIFT, injective identification, spanning-read certification | #1210, #1169 |
| D21 | E_f(R1): fixed-frame state representation has positive trace-norm gap for Φ⁺ and r=−v₀/√3; CNOT **channel** is outside frame-nonnegative maps; no universal accessible-law or all-entangling-channel no-go | state comparison: exact calculation, unreviewed; channel exclusion conditional on D20 | [A + G3; r2 F2–F5]; AP1:872–878 [W] | E_f(R1) | fixed R1 product identification, H-LIFT at each cut; accessible separating menu/uniform reconstruction not established | #1210 (M11, M12), #868 |
| D22 | Native encoded non-Clifford operation (M12); repeated composition (M13) | open | SHM [D] | E_f | — | #1210 |
| D23 | Composite rules: pair source, local tomography, entangling operation, joint-test validity (J1, J2, J5, J7, J13; M17, M18) | open | A868 [D], SHM [D] | C / E_f | — | #1210, #1169, #868 |
| D24 | H-Bell / cross-wing response (M19) | open | Sub:131–133; Main §3.3 [P] for the one-step ceiling | C-dyn (ontic graph) | — | #1210, #1211. Finite-accuracy Bell statistics exist on E_r (Main:574) [P]; no row here implies H-Bell (#1169 decision 4) |
| D25 | Born probability rule / exponent | supplied on E_r (Tr I_o(ρ̃)); open for OI derivation | Main:580 [P]; A1059 [D] | E_r / C | — | #1059 (outside the four; recorded) |
| D26 | Phase intervention. Scoped relations (#1169 decision 4): the phase is independent of the layer flow only (`obligations_independent`, OB/C5Discovery.lean:59, on Fin 2); the complex drive carries the phase (GR:250, :258) | stated assumption, not derived | [K] `PhaseSource.lean` (GR:260); [K] OB/C5Discovery.lean:59 | C | — | #1211, #1169 |
| D27 | E_f(SIC): all quantum states representable as product-SIC coordinates; some sharp effects lack valid 4-point responses; CNOT **channel** matrix negative, not an observable-law no-go | representation exact, [A] general + [G5a]; channel exclusion conditional on Lemma F SIC extension [A] | [A + G5a,G5b; r2 F1,F3,F4]; Main:562 [P] | E_f(SIC) | fixed product identification, restricted preparations, operation set and H-LIFT at each cut; access to separating tests unproved | #1210, #868 |

**Independence of #945.** Every OI-derived question in this unit (D12, D14, D17–D23, D27) is independent of
#945's outcome. #945 decides only whether the E_r simulator has a proved finite-b, fixed-format,
\|N\|-independent form (D4–D6).


### 7.1 Reuse of #1169 tests for OI-derived Level B (r4 writer assessment)

The following maps *pinned preregistrations*, not completed scientific outcomes. The existing
rounds are kept in #1169, with no new measurement or change to their gates. Finite observations
must not be silently promoted into resource-uniform error floors, quantum coverage or sourced
physical explanations. Every test retains its own preparation, access and record alphabet.

| Existing work | Bounded question actually tested | What a Level-B result still needs |
| --- | --- | --- |
| **Q-C2-1 P**, with sham controls; secondary B/C | **Primary P is detector-OFF versus detector-ON interference contrast**, with separately validated marker attribution. The two shams are **controls**, not the primary comparison; if a sham also suppresses interference, the marker-attribution verdict must reflect that independently. B concerns the specified fragment-relative noncontextuality question; C concerns a bounded encoded operation and stated compositions on **owner-typed records**. Validation-only variables do not automatically become accessible records. | One predeclared native/quantum comparison for the **complete admitted records** on the same source and chosen access; controlled ablations and contrasts do not themselves bound the worst-case errors of an entire target class. Uniform-in-resource witness required to infer an obstruction. |
| **Q-C2-2 F1**, with separately supplied completions | Exact LP feasibility/infeasibility of the **specified prepare–measure fragment**, with one read per run, stated herald and finite sizes/equivalences. Each completion changes a declared supply/access and must be compared **separately**. The larger-supply F1+R-S case is included only if authorized under its own decision. One-read samples expose herald–read joint distributions, not arbitrary longitudinal record histories. | A robust law-level margin under the common full-record alphabet, controlled slack for any varying operational equivalences, and a fixed decoder/resource family. Exact infeasibility in one fragment is neither a margin nor an all-depth obstruction. Report herald masses and joint herald–read laws; conditional-only gaps need a herald probability floor or joint inequality. |
| **MATH-CON-1 Stage 1B, first stage** | O-1, O-2 and O-3a–e only, on the specified polarized construction, under its declared assumptions. It may establish fixed finite-depth availability for that **witness**. | Circularity/source test (excluded O-8), spectator-form composition (excluded O-9), uniform approximation errors and native source of generators remain separate. This stage cannot by itself establish continuous/discrete dense control or Level B. |
| **#1211 bridge and #868 joint-system assessment** | The bridge isolates the direct configuration-carrier mixing gap. The joint assessment separates permitted-test validity, joint-state closure and quantum compatibility. | Transport only within the same declared carrier, source and read menu. Separately demonstrate quantum coverage and soundness, and do not infer complete-history no-signalling or compositionality from a single wing or single fragment. |

Design provenance: [Q-C2-1 r14c](https://github.com/amaybaum/incompleteness/blob/820519cf/handoff-20261109/qc21/preregistration.draft.md),
[Q-C2-2 r14b](https://github.com/amaybaum/incompleteness/blob/820519cf/handoff-20261109/qc22/preregistration.draft.md),
and the [MATH-CON-1 control plane at a44c0206](https://github.com/amaybaum/incompleteness/blob/a44c0206f2c3519944eb31a5eca361eeff2c4be8/verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/preregistration.md).
These are off-`main` planning records, not independent scientific results.

**Common comparison recipe (a proposed *test obligation*, not a new OI physical premise).**
For each declared envelope (system dimension/subsystems, measurement outcomes and depth T),
fix **before** evaluating any quantum protocol:
- One physically justified native rule generating all admitted operations and observers as a
  function of the declared resource budget r; one family of encodings/decoders/identifications
  supplied by that rule, not separately fitted to favorable targets or to ε. The recipe declares
  which logical system a larger carrier represents, and how shared preparations, local subsystems,
  interventions and compositional uses compare across r. No unreviewed promotion of a validation-
  only variable into a visible record at larger r.
- A common **accessible-history alphabet** and stopping/abort rule, including every admitted
  preparation label, setting, readout, herald, failed attempt, continuation, discard and reset
  where it is an observable part of the procedure. Align experimental coarse-grainings only when
  permitted by the declared access; charge fresh supply, initialization, control, memory, reads,
  discards and resets explicitly. The quantum benchmark can use quantum formulas to specify target
  probabilities, but those formulas do not generate the OI implementation dictionary.
- **Coverage**: supremum over the bounded target quantum protocols of the **best admissible match
  selected by that common recipe**, comparing complete-history laws in TV. No admissible match is
  a coverage failure (or a declared out-of-scope protocol if excluded *before* testing), not an
  invisible success.
- **Soundness**: supremum over **all admitted native uses**, including failed/non-target uses,
  adaptive compositions and composites, of TV error to the recipe-compatible quantum law. A
  native use with no quantum comparator is a soundness failure (or explicitly outside the
  predeclared envelope), not ignored by restricting to a successful subdictionary.

The per-budget coverage and soundness errors are distinct quantities. An arbitrary-finite-
precision **OI-derived** Level B demands a coherent family of physically sourced recipes and,
for each fixed envelope and ε>0, a resource budget with **both** errors ≤ε, with explicit
resource scaling and complete history. This is a proposed quantified assessment of the existing
target, not a claim proved by the current rounds or an additional premise about OI.

**Observable inequalities.** For a statistic 0≤f≤1 on the **complete accessible record**,
|E_P f−E_Q f|≤TV(P,Q). A baseline class with a bound separated from the quantum statistic by
δ>0 at **every** admitted resource budget gives a δ observable error floor *provided the same
statistic, read and correspondence exist at each budget*. A fixed-size mismatch has no scaling
conclusion. If both remote settings' **complete isolated local history** laws are each within ε
of a quantum law whose local marginal is equal between settings, their local TV difference is
at most 2ε; this only bounds leakage on that defined envelope/depth. A branch-conditioned
witness has no uniform full-law floor absent a lower bound on herald mass or a direct
joint-herald–read inequality. §4.2's two-config stochastic record witness is **not** a witness
on arbitrary new decoders. Likewise, separation of states/channels by a potentially inaccessible
observable does not certify accessible-history TV separation.

**Adaptive upper bounds.** A per-step instrument approximation can telescope over depth T
only if each error bound is uniform in the same adaptive context and retained side systems;
then the total bound is at most the sum of per-step bounds. A fixed-depth availability theorem
does not prove such errors. Main's adaptive diamond telescoping lemma (Main:596) is a
comparison template, not an OI-native bound. No pending Q-C2 or MATH-CON-1 outcome is assumed.

**Writer disposition.** Reuse the pinned test scopes in #1169; keep the common-recipe,
all-admitted-uses coverage/soundness proof obligation in #1216. At the re-review check the
quantifier order, availability of every claimed accessible read, the source of each codec,
and the uniformity required to extend a matrix or fixed-size result across resources.

***

## 8. Restriction ledger (three columns)

| Restriction | (i) well-defined? | (ii) from independently justified OI principles? | (iii) reproduces QM? |
| --- | --- | --- | --- |
| Declared horizon K and accuracy ε per realization | yes | required by #1216's test scope; a **rich all-horizon target** cannot be uniformly approximated at a fixed finite carrier under D10's fixed-repeat hypotheses, but **finiteness alone** imposes neither horizon cutoff nor ε-dependence for every restricted model | scope/accounting rule, not quantum reproduction |
| Exact-ring registers | yes | no; an idealization of the simulator | yes within the grid (D3) |
| Fixed-point b-bit registers | yes | no; a hardware choice | open (D4) |
| Exactly stored initial register (#945 repair (b)) | yes | no | conditional (D4b) |
| δ-net rounding of instruments (dictionary) | yes | **none identified**; supplied to the machine | yes (D6) |
| Product prior carrying quantum conditionals | yes | **none**; chosen from QM | yes, by construction — column (iii) supports nothing in (ii) |
| Monomial (configuration-level) substratum operations | yes | yes for the stated access [K] | no (D17, D18) |
| Fixed linear identification R1^⊗n with H-LIFT | mathematical construction | a modelling choice in AP1/MECH-2 [W], not independently sourced | some target **states** have fixed-frame trace-norm gap; Lemma F conditionally excludes the **CNOT channel** in fixed map norm, U2 certain unitary permutations; no automatic accessible-history or all-entanglement no-go (D21) |
| SIC identification (Main:562) with restricted preparations | yes | representation choice, not physically sourced here | all quantum states have product-SIC coordinates, but some sharp effects lack valid ontic responses; under Lemma F SIC extension the **CNOT channel** is excluded in fixed norm, not all entangling or accessible law behavior (D27) |
| Restriction to A₄ ≀ S_n **unitary-permutation** continuations (under R1 U2 hypotheses) | yes, conditional modelling restriction | none identified | preserves the stated encoded state set but its limited unitary-permutation class does not generate entangling unitaries; not an exclusion of every possible nonunitary entangling protocol |
| Fixed (d, m) | yes | no | yes at each fixed (d, m) (D7) |

***

## 9. §A.31 classification of this unit's findings

- **F0** (line-number mapping in #1216's body): BORDERLINE, editorial; planning record only.
- **F1** (Main's E_r realization has a reusable quantum-simulator *shape* but **fails the OI-derived
  Level-B research target already defined by #1216**): NEW as a comparison of operational target
  versus simulator; Main:582/:584/:602 support the distinction, not a new definition of Level B.
- **F2** (fixed-carrier approximate *all-horizon* obstruction, under a target class containing the
  resource-dependent rotation and fixed-repetition interface, not a fixed-depth scaling floor):
  ELABORATING (Main:640).
- **F3** (NX-1 as route-relative **state/channel** single-operation obstruction; exact FI-1 conditional
  on level-one transport for system-generated branches; column-monomial insufficiency;
  fixed two-config H/H,Z law witness only; no general accessible-history or resource-uniform floor):
  NEW, narrowed following r3 independent review R2/R3.
- **F4** (finite-b decoder has nonnegative record probabilities and an exact internal PSD closure
  counterexample in one instance; asymptotic approximate closure and finite-b realized-law accuracy
  both **open**, no general finite-accuracy law obstruction): NEW, scope corrected after review R4/R6.
- **F5** (shuffle-only comparison depends on identified carrier and frame; C state coverage floor;
  R1 representation restriction; SIC representation without sourced sharp effects; CNOT *channel*
  excluded under conditional Lemma F; E_r only with imported quantum data): NEW, no all-entangling
  nor law-level generalized no-go.
- **F6** (#945's fixed-b register repair not on the critical path to an OI-sourced mechanism):
  POSITIVE (scheduling), **not** a proof that finite precision is impossible.
- **F7** (R1 versus SIC state and fixed-channel differences; trace-norm state gap ≥2−√3 under R1):
  NEW from r1 review B2 and r2 generic checks, restricted to the fixed identifications; no
  implication for physically accessible full histories without a test-separation bound.
- **F8** (coverage is distinct from owner validity, closure and quantum compatibility): ELABORATING;
  distinguish closure of classical response posteriors and decoder-record validity from
  quantum-state closure and broad product-test validity.
- **F9** (system-level NX-1 yields nonmonomial **bare-S** block through available system instrument;
  exact `S × Fin 1` FI-1 needs transport or theory bridge; P★ only supplies a non-PSD decoded
  branch and specifically recorded frequencies, not universal product-test failure): BORDERLINE.

Passes/status: r1's independent review introduced F7 and F8; r2's writer checks refined F9;
r3's fresh independent full-text review returned REVISE (R1–R6) and narrowed several interpretations.
The r4 writer corrections above are **not** an independent verification or a new kernel result.
The independent full-text review of r4 returned **ACCEPT WITH NITS**; r4a addresses N1–N3.
§A.31's fixed-point criterion is not declared satisfied. The r4a gate is a focused diff-only
check and green ordinary CI, with separate owner approval required for integration.

***

## 10. Questions for the owner (neutral)

- **OQ1 (implementation evidence, not target definition).** What source evidence and
  measurements should certify a **single OI-derived recipe** for preparations, instrument
  labels, decoders and scaling, across resources? Derivation from OI is already required by
  #1216; Main's simulator is the imported-data comparison control.
- **OQ2 (routes).** Which native carrier/access families should receive priority as **candidates**:
  direct C, physically specified E_f (R1, SIC or U′), or a genuinely OI-sourced E_r implementation?
  Selecting a candidate is not adopting its encoding as a physical premise.
- **OQ3 (resource envelope).** What bounded class of subsystem sizes, outcomes, depths, failures,
  heralds and reads should be declared first for the common-recipe coverage/soundness test?
  Resource dependence on K, ε and memory is already required by #1216; no additional permission
  is sought for that bookkeeping.
- **OQ4 (editorial maintenance).** Should #1216's pre-shift Main line numbers be corrected under
  §A.45? This has no effect on the science.
- **OQ5 (possible unit 2, separately gated).** Should the next paper question seek a sourced
  direct-C operation that breaks diagonal preservation **with accessible test separation**, or
  compare physically sourced fixed-frame identifications and the allowed effect menu?
  No new computation, physical premise or follow-on unit is authorized by this writer draft.

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
- **r3 writer checks (inherited):** verified r2 against handoff hashes and read pinned round scopes;
  §7.1 was a hand comparison, not an independent review.
- **r3 independent review:** full-text paper-only verdict REVISE (R1–R6), file
  `REVIEW-APPROX-UNIT1.r3.md`; independently checked pinned Main, Lean statements, round scopes,
  recorded outputs, #945 assessment and the fixed-interface inequalities. Its evidence is review
  only, not new native scientific computation.
- **r4 writer pass:** changes are prose, classification and quantified comparison only. All six
  review requirements R1–R6 have explicit dispositions in
  `DISPOSITIONS-APPROX-UNIT1.r4.md`. No computations or Lean were performed in r4; the numeric checks,
  formal claims and source pins are inherited. The requested fresh independent full-text review
  returned **ACCEPT WITH NITS**, with no blocking scientific findings; see
  `REVIEW-APPROX-UNIT1.r4.md` for its evidence and comparison limits.
- **r4a writer pass:** only N1's citation, N2's numerical/exact evidence labels, N3's
  admissibility/availability wording and revision/publication metadata change. No scientific computation,
  simulation or Lean was run; inherited probe outputs and scientific source pins are unchanged.
  Focused diff-only review and green ordinary CI precede the separate integration decision.
- **Not done:** the inherited r2 N5 digitized step and earlier reviewer re-runs are identified
  above, not rerun in r4 or r4a. No scientific execution, new physical premise, freeze, dispatch,
  scientific designation, manuscript change or merge is authorized by this cleanup.

## 12. Hashes

- `probes/approx_generic_checks.py`: sha256 `12aac10f6e8f8d6a7bfb7603b35aac8253132534e353791508c3cda443f172c0`
- `probes/approx_generic_checks.out`: sha256 `4337d4afc70c4fdd22deafda2eefeaa926abe044f3b7993ad47b37e9d2865c35`
- `probes/r2_frames.py`: sha256 `aa02e479a0d93ba7ccb6ccb5f9a40c7b0e2065e5f3d7c30d3bdbb2d78010548a`
- `probes/r2_frames.out`: sha256 `a116e91999a566f9d409f857325be4e1d94a47c24da62f7ec6eb73e491be0209`
- `probes/r2_routeC.py`: sha256 `b71749e47f742338d6373aaccae08bdaa96c985c29172b36ba1267e60ac72f97`
- `probes/r2_routeC.out`: sha256 `5626b5a8db40d7ade57542ea297c1c6afb2da32bcd5838ed013d9b02d2e538ec`
- `probes/r2_finiteb.py`: sha256 `383c21567671c73e9565b65c8846dfdc4ab385bf285321cd22b83b72c9b6e07c`
- `probes/r2_finiteb.out`: sha256 `6350b5c11822166bff80b9eacde330a14513390cbda0dc117cc45f26ed4df7b1`
- r3 source: SHA-256 `ee432c1b7db91c8e3e0aa3a1e11de68818c8090fa6e1eb34cca478d8be01c659`.
- r3 independent review (separate local file): SHA-256 to be reported with the handoff.
- The reviewed r4 and r4a SHA-256 digests are reported in `DISPOSITIONS-APPROX-UNIT1.r4a.md`, not self-recorded.
