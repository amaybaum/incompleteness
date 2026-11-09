# OI-QM-APPROX-1, unit 1: operational equivalence at finite precision, assessed against Main §3.4

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09). Revision r1, pending a fresh,
independent full-text review.** Nothing here is adopted, promoted or proposed for the manuscripts. A
review ACCEPT, if reached, authorizes no computation, new physical premise, manuscript change or merge
(#1216 body, "Unit 1").

- **Accountable home:** #1216 (OI-QM-APPROX-1). Parent programme #1169.
- **Authorization.** Owner (amaybaum), 2026-11-09, #1216 c.6741763726 (posted 2026-11-09T13:53:51Z),
  option "Create + start unit 1 (Recommended)", scope verbatim: "Unit 1 (paper-only): does Main's
  existing approximation result meet Level A? What prevents Level B? Is continuous coherent mixing
  still necessary? It ends with a fresh independent review. No new computation beyond labelled exact
  generic checks, no physical premises, no manuscript change, no merge." The coordinator's brief adds:
  no computation on an OI mechanism, and no git or GitHub write. An owner-approved addition, relayed by
  the coordinator during this unit (its #1216 comment was being written; not seen by this writer), asks
  for three separately reported outcomes per Level-A/B claim (validity, closure, quantum compatibility)
  and an assessment of approximate joint-state closure under finite shuffle-only dynamics. It is
  answered in §5. This unit made no git, repository or GitHub write.
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (2026-11-09
  08:36 +0200). "Main" = `papers/Main.md` (sha256 `6144cd4a…6366`), "GR" = `papers/GR.md`
  (`a475a2a8…4992`), "OB/" = `verification/lean-mathlib/OIBridge/`, "MECH-2" =
  `verification/programmes/oi-qm/reconstruction/mechanism-2-20261108/DESIGN.md`. All `path:line`
  citations are at `fd539e15`.
- **Line-number mapping (finding F0).** #1216's body cites "the exact-arithmetic theorems (:544, :576)
  and the density corollary (:578)" and #945's "negativity-ledger step at :556". These are #945's
  pre-shift numbers (#945 c.6567863298: the text moved by +22 lines after `7c6ceaaa`). At `fd539e15`
  the gluing theorem is Main:566–:580, the uniform theorem Main:598, the density corollary Main:600;
  the negativity-ledger text no longer exists, and Main:578 instead states that the clip-and-normalize
  estimate "is not established for the simulator's Hermitian branches" and that the finite-b bound is
  open. Main:556 at `fd539e15` is the Remark "what this equivalence does and does not say".

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
   (Main:568, :578, :580, :602); #945's per-parent negativity ledger is refuted by an off-`main` record.
2. **Level B.** Main's gluing/uniform construction is a reusable mechanism, not a prediction table (one
   fixed map per instrument, every protocol, gluing by restriction; the comb of (a) *is* a table). At
   fixed (d, m, K, ε) it meets Level B's *shape* (§3). It is a discretized ψ-ontic classical simulator (state description plus seeds):
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
   routes; implies FI-1 on the configuration route; not sufficient. On the third route (a ψ-ontic
   register encoding, as in Main's simulator) no operational property is missing — the simulator is a
   finite bijection using "no property of the substratum beyond finiteness and reversibility"
   (Main:582) — and the gap is selection (Main:602).
4. **Continuous coherent mixing (§6).** Not necessary for Level A or for Level B's shape (exact-ring
   proofs; the mixing sits in the supplied Kraus data). For an OI-native approximate target on the
   configuration carrier, continuity and the kernel's uncountability strengthening are not necessary,
   but the discrete core is: an available operation that does not preserve diagonal states (which
   implies FI-1) and a non-real operation [A + G1]. The complex drive supplies both at once; that it can
   carry the phase does not show that OI supplies the drive. On fixed-linear-frame encoded carriers
   configuration-level mixing is not the operative resource; the identification is (MECH-2 Lemma F, W).
5. **Dependency matrix:** §7. Unit 1's OI-derived question does not depend on #945's outcome; #945 bears
   only on the simulator's fixed-format capacity.
6. **Owner addition (§5).** Validity, closure and quantum compatibility are reported separately for each
   claim; finite b is a natural witness that validity holds while closure fails. Approximate joint-state
   closure under finite shuffle-only dynamics: **no** on the configuration carrier (ε-robust, any carrier
   size); **states yes, entangling continuation no** under a fixed tetrahedral frame (conditional on
   Lemma F); **yes** on the register-encoded route (exact ring, proved on paper), with the complex
   structure supplied as data.

***

## 1. Conventions

**Evidence layers.**
- [K] kernel-checked Lean on `main` (identifier and module given).
- [P] paper proof in a manuscript on `main`.
- [X] exact computation recorded on `main` (probe named in the manuscript).
- [G] this unit's labelled exact generic check (`probes/approx_generic_checks.py`, §11); a result
  supported only by [G] is *computation-supported*.
- [A] this unit's own hand argument, unreviewed.
- [L] external literature, recalled, not re-read here; bibliographic details to be checked by the
  reviewer.
- [W] model-written research record on `main`, not established under §A.46 item 1.
- [D] unreviewed or in-revision draft in the session scratchpad, used as a hypothesis only
  (§A.46 item 7): BRIDGE = `bridge/BRIDGE-UNIT1.md` (r5, sha256 `78f1098e…`, reviewed ACCEPT WITH
  NITS per the coordinator); SHM = `qphen/SHARED-MECHANISM.md` (#1210 r7); A868 =
  `reassess/868/ASSESS-868.md` (r3a, `d97c4b6b…`, reviewed ACCEPT WITH NITS per the coordinator);
  A1059 = `reassess/1059/ASSESS-1059.md`.
- [OFF] off-`main`: #945's records `verification/audits/manuscript/intro-corpus-audit-20261026/proofs/eps-realization/`
  on branch `audit/intro-corpus-20261026` at `6d494e30`, and #945's comments c.6567863298,
  c.6567879503, c.6567887681 (model assessment and model review, ACCEPT-WITH-NITS). Provenance and
  support off `main`; nothing here lands.

**Carriers.**
- **Configuration (C).** The finite configuration set S, read as the quantum carrier ℂ^S under Main:564's
  operational interface. Substratum interventions are monomial operators (OB/SubstratumInterface.lean:75,
  `IsMonomial`; GR:260).
- **Encoded, frame (E_f).** A d-level system identified *linearly* with distributions over
  configurations through a fixed frame (QP's U′, MECH-2's R1^⊗n). Configurations are treated classically.
- **Encoded, register (E_r).** A d-level system whose state is stored as data (a digitized density
  matrix) in hidden registers, one state per configuration, beside pre-loaded seeds: a discretized
  ψ-ontic, ψ-supplemented ontological model in the sense of Harrigan–Spekkens (2010) [L]. Main's gluing realization is
  of this kind. E_f and E_r are both "encoded" in the brief's sense; they are kept apart because their
  obstructions differ.

**Three distinctions kept throughout (#1169 c.6740778880, as quoted in A1059):** configuration vs
encoded carriers; mathematically available vs derived from OI; coherent mixing vs the full probability
and composition rules.

**Three-column separation** for every restriction (§8): (i) well-defined; (ii) follows from
independently justified OI principles; (iii) reproduces QM. Column (iii) never supports column (ii).

**Three outcomes** for every Level-A/B claim (§5): *validity* (every permitted product test gives a
valid result), *closure* (every permitted preparation and heralded continuation stays in the
admissible state space), *quantum compatibility* (the realized laws are, within the stated accuracy,
laws of quantum instruments on quantum states). No outcome is inferred from another without a proof
stated at the place (A868 §4.1, r3a).

***

## 2. Question 1: does Main meet Level A?

Level A (#1216): "Any specified finite quantum experiment's observable law is reproduced within ε."

### 2.1 The three constructions

| | A1. Comb with response-table prior | A2. Gluing realization (ε-form) | A3. Uniform continuum realization |
| --- | --- | --- | --- |
| Source | Main:482–:486 (theorem, proof), :520 (Extension, real kernels), :602 ("a fixed finite instrument family is realized exactly by the intervention dilation above, with a product prior carrying the quantum conditionals") | Main:566–:580: theorem, clauses (1)–(5), Rounding Lemma, proof; Main:582 single-dynamics Corollary | Main:596 (adaptive diamond telescoping Lemma), :598 (theorem), :600 (density Corollary) |
| Experiments | Any finite action alphabet and finite-horizon action-labelled family P(x_{k+1} \| x_{≤k}, a_{≤k}); adaptive choice is covered because every context (x_{≤k}, a_{≤k}) is a coordinate | A d-dimensional system, a fixed initial state (other preparations enter as outcome-free channels), a finite family F of instruments, each outcome a CP map with finitely many Kraus operators, horizon K; every adaptive protocol over F through K; spatially separated parts via the product construction on a joint register (clause (4)) | Every adaptive protocol of horizon ≤ K with arbitrary ≤m-outcome instruments on ℂ^d, preparations included as channels, by rounding each instrument to a δ-net member, δ = ε/(2K) |
| Accuracy | Exact for arbitrary real kernels (:520); ε only for the rational uniform-tape presentation | TV ≤ K(\|O_max\|−1)/G with exact-arithmetic registers over the instruments' entry ring; at finite b **open** (:568) | TV ≤ Kδ + K(m−1)/G ≤ ε, exact regime; R-laws within ε/2 of quantum laws; finite b **open** (:598) |
| Access | Agent writes the action ledger (bijections I_a), reads visible x | Visible: step counter, intervention record (labels written by the agent, or a read-only program register prepared once, :582), outcome registers (read). Hidden: branch register, predecessor stack, K pre-loaded seeds | As A2, with net labels: ⌈log₂\|N\|⌉ = O(m d⁴ log(2K/ε)) bits per step of visible intervention record |
| Where quantum content enters | The product prior *is* the quantum conditionals | Instrument data (Kraus operators) in the step maps; the state in the hidden register; Born trace q_o = Tr I_o(ρ̃) computed by the step map (:580, :582) | As A2, over the whole net |
| Carrier | C (classical response coordinates) | Finite bijection on configurations; system in E_r | As A2 |
| Evidence | [P]; [X] `intervention_probes.py` (n_V = \|A\| = K = 2, exact), `lg_comb_probes.py`; real-kernel Extension: [P], rational instance [X] `review4_probes.py` P-G. Passive (action-free) law: [K] `S_imp_D`, OB/Equivalence.lean:422 | [P]; [X] `opglue_probes.py` at (d, K, \|F\|) = (2, {2,3}, 4), exact over ℚ(√2), checks 11–13. No Lean module formalizes gluing, rounding or clipping (#945 c.6567879503 §1; this unit's grep of OB/ for "gluing", "rounding", "opglue" found none relevant) | [P]; [X] checks 8–9 (qubit instance). Telescoping Lemma: [P], standard |
| Resources | \|C_H\| = n^N (n+1)^K (K+1), N the number of contexts, exponential in K | Exact ring: log₂\|C_H\| ≤ (K+1) log₂\|V_reach(F,K)\| + K log₂ G (:576). Fixed point: O(K d² b + K log₂ G), whose accuracy form depends on the open finite-b bound | Exact ring: capacity grows with the net (:598). Reading [A]: \|V_reach\| ≤ Σ_{k≤K}(\|N\|m)^k, so log₂\|C_H\| = O(K² m d⁴ log(K/ε)), polynomial; the transition law's description scales with \|N\| = exp(O(m d⁴ log(1/δ))) (:598) |

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
realization on a d_A d_B register, not built from the components' realizations; its rule is the quantum
tensor product. The uniform theorem and the density Corollary hold "at each fixed system dimension d
and outcome bound m … the union over (d, m) is a further limit, not taken here" (Main:600), so
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
- **Route C (configuration carrier as the quantum carrier, Main:564's interface).**
- **Route E_f (fixed linear frame identification).**

### 4.2 NX-1, stated for routes C and E_f

**NX-1 (one robustly nonclassical, valid native transformation).** Relative to a declared encoding and
the stated access, some native procedure — built from the OI dynamics and access, with no quantum
instrument data as parameter or input — induces on the encoded system a valid (completely positive,
trace-non-increasing) transformation at a positive, ε-independent distance from the encoding's
*classical class*:
- route C: the maps that preserve diagonal states (`PreservesDiag`, OB/DiagonalTheory.lean:68);
- route E_f: the maps whose frame matrix is entrywise nonnegative (MECH-2 Lemma F's class).

**Necessity [A].** Both classes are closed and stable under composition, sums (coarse-graining,
outcome-conditioned continuation) and attachment/discard of a diagonal or frame-represented ancilla. If
every native procedure's branches lie in such a class 𝒞, every adaptive composite procedure's branches
lie in 𝒞, and a target instrument at distance c > 0 from 𝒞 is approximated by none of them for ε < c,
at every horizon and every resource level. The target class contains such instruments:
- *Route C:* for every diagonal D, tr((|+⟩⟨+| − D) σ_x) = 1, so ‖|+⟩⟨+| − D‖₁ ≥ 1; the Hadamard
  channel is at trace distance ≥ 1/2 on the input |0⟩⟨0| from every diagonal-preserving map [G1a–b];
  likewise for composites, x+ ⊗ z+ against every diagonal D with witness X⊗Z [G4].
- *Route E_f:* under the tetrahedral frame of Main:562 (p_i = (1 + a_i·r)/4), a rotation O acts by
  M_ij = (1 + 3 a_i·O a_j)/4. The 12 rotations of A₄ give permutation matrices; each of the other 12
  octahedral (Clifford) rotations, the Hadamard and S rotations among them, has an entry −1/2 [G3]. The
  nonnegative matrices form a closed set and the frame matrix of a channel is determined by its action
  on states, so each such rotation sits at a positive distance from Lemma F's class [A, compactness].
  For composites, the CNOT conjugation's frame matrix has a negative entry [G5b].

**Where native constructions sit.**
- *Route C* [K-lemmas, composed here (A)]: in the theory a configuration-level architecture generates,
  every branch of every available instrument is a finite sum of conjugations by admissible monomial
  operators (`realized_of_instAvail`, OB/ImplementationLocality.lean:530), hence preserves diagonal
  states (`preservesDiag_conj_of_monomial`, OB/SubstratumInterface.lean:126; `preservesDiag_sum`,
  OB/DiagonalTheory.lean:84). The substratum class is configuration-level
  (`substratumClass_configurationLevel`, OB/ManuscriptAxioms.lean:129). The composition is the same
  argument as the kernel's `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52); it is
  not stated as one theorem. So the stated substratum with its access fails NX-1 on route C.
- *Route E_f* [W, conditional]: MECH-2 Lemma F (every encoded branch nonnegative on frame coordinates,
  under a fixed linear identification by an orthogonal frame) and Theorem U2 (encoded unitary channels
  induced by fixed bijections lie in A₄ ≀ S_n, which is finite and Clifford). If they hold, route E_f
  fails NX-1 for every dynamics, and MECH-2's own conclusion follows: "a nonclassical observer-level
  theory needs a change in the identification and access, not in the dynamics alone".

**Relation to FI-1 (route C).** FI-1 (BRIDGE [D]): a non-monomial admissible operator on the
configuration carrier at level one. NX-1 on route C ⇒ FI-1 by the kernel argument above (a branch that
does not preserve diagonals has a non-monomial admissible summand). FI-1 ⇏ NX-1: the Kraus operator
|0⟩(⟨0| + ⟨1|)/√2 is non-monomial and sends every diagonal state to a diagonal one [A]. So NX-1 is
strictly stronger than FI-1 and strictly weaker than layer-flow executability.

**Why "smallest".** NX-1 is a single-operation property, necessary on routes C and E_f, and it is
exactly where native constructions (kernel-level on C; MECH-2 on E_f) and Main's simulator part: the
simulator escapes only because its encoding is E_r with imported arithmetic.

**Not sufficient.** NX-1 does not give:
- *density* — the next link, **NCG** (native compositional generation): native procedures whose induced
  instruments have adaptive compositions ε-dense in the class for every ε, with resources scaling by a
  declared rule. At a fixed finite carrier, the encoded maps induced by single bijections (with fixed
  ancilla initialization and fixed heralds) form a finite set, so NCG needs adaptive procedures of
  unbounded length, a carrier refined with ε by a target-independent rule, or non-bijective native
  operations [A]. Under MECH-2 U2 [W] the encoded unitaries stay in A₄ ≀ S_n at every n;
- the probability rule (#1059; A1059 §0 [D]);
- the composition rules: local tomography, pair source, entangling operation, validity on joint tests
  (A868 J1, J2, J5, J7, J13 [D]; SHM M17, M18 [D]);
- validity/C-CP: MECH-2's P★ escapes the stabilizer octahedron only through a channel that is not CP
  [W]. That is why NX-1 requires validity.

***

## 5. Owner addition: validity, closure and quantum compatibility, and shuffle-only joint closure

### 5.1 The three outcomes per Level-A/B claim

"Admissible state space" is stated per claim, since closure is relative to it. Each entry gives the
outcome, its status and its own reason; no entry is derived from another unless the derivation is
written in it.

| Claim | Admissible state space | Validity | Closure | Quantum compatibility |
| --- | --- | --- | --- | --- |
| A1 comb / response table (Main:482, :520, :602) | Visible conditional laws generated by the loaded prior (classical simplex on the response coordinates) | **Holds, by construction**: realized probabilities are measures of a product prior [P] | **Holds in the realization's own space** (any heralded continuation is the loaded conditional) [P]. Closure in the *quantum* state space holds only because quantum conditionals were loaded — column (iii) | **Exact for the loaded family only**; none outside it. Loading PR-box data gives validity and closure with no quantum compatibility (Main:362) [P] |
| A2 gluing, exact ring (Main:566–:580) | PSD branch matrices ρ̃ in the register | **Holds**: q_o = Tr I_o(ρ̃) ≥ 0 for CP I_o on PSD ρ̃ — derived from closure here, by complete positivity — and realized frequencies are seed counts [P] | **Holds exactly**: exact CP maps keep the register PSD; composites by I_a ⊗ I_b on the joint register stay PSD [P] | **Within K(\|O_max\|−1)/G** in TV [P, X]; per-instrument the maps are the quantum ones by construction (column iii) |
| A2 at finite b (Main:568, :578, :580) | As above | **Holds for realized laws, by construction**: clipping and normalization give nonnegative pre-grid probabilities and seed thresholds give frequencies (Main:578 Corollary text) [P] | **Fails**: "digitized branches are Hermitian but not positive" (Main:578) [P]; the per-parent ledger meant to control this is refuted [OFF] | **Open**: the realized-law bound at finite b (Main:568) |
| A3 uniform, exact ring (Main:598) | PSD register over the net's reachable set | Holds, as A2 exact | Holds, as A2 exact | **Within ε** at fixed (d, m, K), exact ring [P]; fixed-point variant open |
| A3/A4 density Corollary (Main:600) | Operational theories at fixed (d, m) in the finite-test topology | Holds for every R^Q_n (as A2) | Holds for R^Q_n (as A2); D_finite's closure also contains non-quantum theories (Main:600) | **Density at fixed (d, m)** [P]; union over (d, m) not taken |
| Route C, stated substratum + access (OI-native) | Density matrices on ℂ^S reachable under Main:564's rules | **Holds**: diagonal reachable states give nonnegative probabilities on configuration reads [A from K-lemmas] | **Holds trivially** (every reachable state is diagonal, hence a quantum state) [A from K-lemmas] | **Fails at finite accuracy**: no coherent preparation within trace distance < 1/2 [G1, G4] |
| Route E_f, native encodings under R1 (MECH-2, QP node 10) | Encoded body (stabilizer octahedron per QP) | Holds on native Pauli tests for QP node 10's zero-completion table (A868 §4.3 [D], which grades it A + X) | Closure of the octahedron under heralding is sufficient, not necessary, for validity on native tests (A868 §4.1, witness w3 [D]); P★ leaves the octahedron via a non-CP channel (MECH-2 [W]) | **Fails** for QP node 10's composite table: ⟨XX⟩ = ⟨ZZ⟩ = 1 with ⟨YY⟩ = 0 has no quantum completion (A868 §4.3 [D], from QP's reported values) |

**Independence witnessed.** Finite b: validity holds, closure fails, quantum compatibility open. QP node
10: validity holds, quantum compatibility fails. A1 with non-quantum data: validity and closure hold,
quantum compatibility fails. Route C: validity and closure hold, quantum compatibility fails. The only
derivation used between outcomes is closure ⇒ validity for exact CP maps on a PSD register (A2, A3),
stated where used.

### 5.2 Can approximate joint-state closure be reached with finite shuffle-only dynamics, where exact closure needs a complex operation?

"Shuffle-only" is read as: every dynamical step is a bijection of a finite configuration set (no
phase operation, no non-monomial operator; adding the phases, which are monomial, changes none of the
conclusions below). "Approximate joint-state closure" is read as #868's J3 with
closure: every needed joint state (full-ball products, and the continuations the class requires) is
reached within ε, and every permitted heralded continuation stays within ε of the admissible (quantum)
state space. The answer is assessed per carrier, without assuming it.

1. **Route C — no, robustly, at every carrier size.** Under Main:564's rules with monomial
   operations, every reachable state is diagonal [A from K-lemmas; A868 G7a [D] agrees]. Closure holds
   trivially, but inclusion fails: for x+ ⊗ z+ and y+ ⊗ z+, tr((ρ − D) W) = 1 for every diagonal D
   with W = X⊗Z or Y⊗Z [G4], so the trace distance is ≥ 1/2 whatever the carrier size or ε. The exact
   requirement (A868 J3: a non-monomial *and* a non-real operation) therefore persists at finite
   accuracy in its discrete form; only continuity drops (§6).
2. **Route E_f (tetrahedral frame) — states yes, entangling continuation no (conditional).**
   - *States.* Every quantum state, entangled ones included, has nonnegative joint frame coordinates
     (they are the probabilities of the product SIC-type POVM {E_i ⊗ E_j}) [G5a for Φ⁺; general fact
     A]. Counting-measure distributions are rational, and with growing counts they approximate any such
     coordinates [A]. So representing approximate joint states is not obstructed by the frame; which
     preparations are *available* is a separate hypothesis (H-PREP; A868 J3 [D]).
   - *Closure in the quantum state space* is not automatic: a nonnegative frame distribution can
     reconstruct a non-PSD operator (a point mass on one ontic pair gives D₀ ⊗ D₀ with a negative
     eigenvalue [G5d]), so preparations must be restricted (Main:562's "restricted preparations").
   - *Entangling continuation.* The CNOT conjugation's frame matrix has a negative entry, minimum
     1/4 − √3/3 ≈ −0.327 [G5b]; local
     A₄ rotations give nonnegative (permutation) frame matrices [G5c]. Under MECH-2 Lemma F [W] every
     native encoded branch is frame-nonnegative, so no native continuation approximates CNOT below a
     positive constant [A, compactness]. Shuffles that do mix ontic pairs beyond A₄ ≀ S_n can leave the
     quantum state space while keeping product-test validity (QP node 10, A868 §4.3 [D]).
   - *Verdict.* Conditional on Lemma F: approximate closure under the entangling continuation that
     #868's J7 needs is not reached by shuffle-only dynamics under a fixed linear frame; restricting the
     dynamics to A₄ ≀ S_n keeps closure exactly but generates no entanglement.
3. **Route E_r — yes, proved on paper in exact ring.** Main's simulator *is* finite shuffle-only
   dynamics: each step is one bijection of a finite configuration set (Main:566, :580). In exact ring its
   register stays PSD (closure), joint registers included (clause (4)), its pre-grid probabilities are
   valid, and its realized laws are within K(|O_max|−1)/G of the quantum ones [P]. Complex amplitudes,
   coherent mixing and entangling CNOT are all present — as the stored Kraus data and register entries
   (the instruments' entry ring), not as an operation on any carrier. At finite b closure fails and the
   accuracy bound is open (§5.1).

**Verdict on the question.** Where exact closure needs a complex operation (route C), approximate
closure is not reached by shuffle-only dynamics on that carrier: the obstruction is ε-robust. It is
reached by shuffle-only dynamics on a *different* carrier (E_r), where the complex structure is supplied
as data — "mathematically available", not "derived from OI" (column (iii), not (ii)). On E_f the answer
turns on MECH-2 Lemma F, which is not established on `main` (§A.46 item 1); if Lemma F holds, the
answer there is no for entangling continuation.

***

## 6. Question 4: is continuous coherent mixing still necessary?

| Target | Continuity (layer flow at every t; uncountably many non-monomial rays) | Non-monomial operation on C (FI-1) | Non-diagonal-preserving operation on C (NX-1, route C) | Non-real operation on C (phase / complex drive) |
| --- | --- | --- | --- | --- |
| Exact finite endomorphic operational QM on C (#1169's exact target; not altered here) | Necessary for the kernel's route: `uncountableNonMonomialRays_of_layerFlowExecutable` (OB/CoherentContinuumSource.lean:163) [K], within the structural architecture | Necessary, one direction: `exists_nonMonomial_of_layerFlowExecutable` (OB/ExecSource.lean:52) [K]; not sufficient (`polarizedTheoryC_not_qm`, OB/PolarizationClosure.lean:620) [K] | Necessary (gate flow at t = ½ does not preserve diagonals: `gateFlow_half_not_preservesDiag`, OB/LiftAudit.lean:155) [K] | Phase stated as an intervention principle, not derived (Main:590; GR:260, `PhaseSource.lean`) [K] |
| Level A, and Level B's shape (any carrier, rules may be supplied) | **Not necessary** [P: Main:566, :598, exact ring] | **Not necessary** on the configuration carrier: the realization is a bijection [P] | Not necessary [P] | Not necessary as an operation; the complex entries are in the supplied data [P] |
| OI-native approximate target on route C (all instruments on ℂ^S within ε) | **Not necessary** [A + L]: a countable set suffices for ε-density; one fixed generic non-monomial unitary with the permutations generically generates a dense subgroup (Lloyd 1995; Deutsch–Barenco–Ekert 1995 [L]); word lengths O(log^c(1/ε)) (Solovay–Kitaev; Dawson–Nielsen 2006 [L]). The kernel's uncountability strengthening is specific to the exact target | **Necessary** (implied by the next column) [A from K-lemmas + G1] | **Necessary** [A from K-lemmas + G1, G4] | **Necessary**: real-Kraus operations keep real states real, and tr((\|+i⟩⟨+i\| − R) σ_y) = 1 for every real symmetric R [G1c; A]. The stated phase supplies it (monomial, non-real); the complex drive (GR:250) supplies both this and the previous column at once |
| OI-native approximate target on route E_f | Not the operative resource: configuration-level mixing does not enter a frame identification that treats configurations classically [A] | Not the operative resource [A]; encoded non-monomial maps arise without FI-1 at stabilizer scope (BRIDGE §5.1 [D], citing QP) | — (route C notion) | — |

**Answer.** Continuous coherent mixing is not necessary for any approximate target considered here.
For Level A and Level B's shape nothing of FI-1 is necessary, because the mixing is moved into supplied
data (E_r). For an OI-native approximate target on the configuration carrier, its discrete core stays
necessary: one available operation that does not preserve diagonal states (⇒ FI-1) and one non-real
operation; the continuity and uncountability that the exact target forces are not. BRIDGE's statement
that FI-1 is "not necessary for finite-accuracy reproduction of quantum statistics (Main:566, Main:584,
Main:600)" is correct for statistics on E_r and does not extend to an OI-native approximate target on
the configuration carrier.

**Skepticism (§A.31), since "continuity is not necessary" favours the framework.** Dropping continuity
removes no obligation the stated substratum meets: the stated access supplies no operation that fails to
preserve diagonals (§4.2, route C), so the discrete core is as unsupplied as the continuous one. The
complex drive carries the phase (BRIDGE r5; A868 §4.4; GR:258), and the phase is independent of the
layer flow only (`obligations_independent`, OB/C5Discovery.lean:59); a drive that can generate the phase
does not show that OI supplies the drive (coordinator relay of the owner addition; Main:590 adds the
state-mixing operation "as an empirical controllability resource").

***

## 7. Question 5: dependency matrix

Columns: **status** (proved / conditional / disproved / open), **evidence**, **carrier** (C, E_f,
E_r), **assumptions**, **shared with** #1169 / #945 / #1210 / #1211, or independent (Ind).

| ID | Dependency | Status | Evidence | Carrier | Assumptions | Shared with |
| --- | --- | --- | --- | --- | --- | --- |
| D1 | S ⇔ D ⇔ Q_fb at every finite horizon (Main:548) | proved | [K] `finite_horizon_equivalence`, OB/Equivalence.lean:462 | C | finite alphabet and horizon; fixed-basis readout | #1169 (baseline), #1211 (frontier) |
| D2 | Exact Level A by comb + response-table prior (Main:482, :520, :602) | proved | [P], [X] `intervention_probes.py`; passive half [K] `S_imp_D` | C | target conditionals loaded as product prior; per family and horizon | #1169 (intervention dilation, classical rung) |
| D3 | ε-Level A by gluing, exact ring (Main:566–:580) | proved | [P], [X] `opglue_probes.py` (d = 2); no Lean | C dynamics, E_r system | exact-ring registers; supplied instrument data and initial state; finite Kraus; fixed K, G | #945 (survives) |
| D4 | Finite-b realized-law bound | open | Main:568, :578, :580, :602 [P] | E_r | fixed-point registers; window rule | #945 only |
| D4a | Old negativity-ledger step (per parent) | disproved | [OFF] #945 c.6567879503 §2, record at `6d494e30` | E_r | in-window dyadic instance d = 4, b = 24 | #945 only |
| D4b | Stopping-time repair, TV ≤ K(\|O\|−1)/G + 14K²C_{d,R}2^{−b} | conditional (Motivated, unreviewed, not authorized) | [OFF] #945 c.6567879503 §3(b) | E_r | Kη ≤ 1/64; exact initial register; Rounding-Lemma constant | #945 only |
| D5 | Rounding Lemma, instrument level (Main:578) | proved for real entries; complex-entry constant open (#945 owner question 6) | [P], [OFF] | E_r | fixed-point dyadic model | #945 only |
| D6 | Uniform continuum, exact budget (Main:598) | proved; \|N\|-independent capacity open | [P], [X] checks 8–9 | E_r | fixed (d, m, K, ε); δ-net rounding as dictionary | #945 (capacity), #1169 |
| D7 | Finite-test density at fixed (d, m) (Main:600) | proved; union over (d, m) open | [P] | E_r | exact ring | #1169 |
| D8 | Classical-dimension obstruction to exact equivalence (Main:560) | proved (factorization half); unboundedness imported [55] | [P], [X] `nogo_probes.py` | any finite ontic carrier | ordinary prepare–ontic–measure interface | #1169 |
| D9 | No uniform finite realization of the instrument algebra (Main:488); finite-order periodicity (Main:640) | proved | [P] | C | fixed finite S | #1169 |
| D10 | Approximate horizon no-go (§3.2 B-2) | proved here, unreviewed | [A + G2] | C | fixed finite S; compositional repetition | Ind (elaborates D9) |
| D11 | Non-uniqueness: the realization machinery realizes non-quantum families (Main:584, :600, :362) | proved | [P] | C / E_r | — | #1169, #1210 (selection) |
| D12 | Selection: why the substratum's bijection is a quantum-shadow one (Main:602) | open | — | E_r route | — | #1169, #1210 |
| D13 | Five completion conditions characterize exact finite operational QM (Main:564) | proved, exact target | [K] `exactAll_iff_physical_general` (OB/GeneralCarrier.lean:100), `five_way_minimality` (OB/RankGapTheory.lean:702) | C (complex kinematics given) | complex matrix kinematics taken as given | #1169 (exact; not altered here) |
| D14 | Approximate analogue of the five conditions | open (not stated anywhere read) | — | C | — | Ind |
| D15 | FI-1 necessary for the exact target | proved, one direction | [K] OB/ExecSource.lean:52 | C | structural architecture | #1211, #1169 |
| D16 | FI-1 not supplied by stated access / landing lift formulations | proved; open for the wave lift | [K] `obs_not_layerFlowExecutable` (OB/ExecSource.lean:129), `configurationLevel_not_layerFlowExecutable` (OB/LiftAudit.lean:183); BRIDGE [D] for the open part | C | stated read/write access | #1211 |
| D17 | NX-1 (route C) necessary for an OI-native approximate target; NX-1 ⇒ FI-1, FI-1 ⇏ NX-1 | proved here, unreviewed | [A from K-lemmas + G1, G4] | C | Main:564's interface; generated theory of an architecture | Ind; refines #1211 |
| D18 | Non-real operation necessary for the same target | proved here, unreviewed | [A + G1c] | C | as D17 | #1211 (O1), #868 J3 [D] |
| D19 | Continuity / uncountability not necessary for approximate targets | conditional | [A + L] | C | a generic non-diagonal-preserving operation available | Ind (sharpens #1211's exact-only statement) |
| D20 | MECH-2 Lemma F, Theorem U2, Theorem NC | conditional (W record; open per SHM Q6-O8 [D]) | [W] MECH-2 §0 | E_f | R1^⊗n, H-LIFT, injective identification, spanning-read certification | #1210, #1169 |
| D21 | Route E_f robust obstruction to NX-1 and to entangling closure | conditional on D20 | [A + G3, G5] | E_f | tetrahedral frame as R1's frame [A, assumed reading] | #1210 (M11, M12), #868 |
| D22 | Native encoded non-Clifford operation (M12); repeated composition (M13) | open | SHM [D] | E_f | — | #1210 |
| D23 | Composite rules: pair source, local tomography, entangling operation, joint-test validity (J1, J2, J5, J7, J13; M17, M18) | open | A868 [D], SHM [D] | C / E_f | — | #1210, #1169, #868 |
| D24 | H-Bell / cross-wing response (M19) | open | Sub:131–133; Main §3.3 [P] for the one-step ceiling | C (ontic graph) | — | #1210, #1211. Finite-accuracy Bell statistics exist on E_r (Main:574) [P] |
| D25 | Born probability rule / exponent | supplied on E_r (Tr I_o(ρ̃)); open for OI derivation | Main:580 [P]; A1059 [D] | E_r / C | — | #1059 (outside the four; recorded) |
| D26 | Phase intervention | stated assumption, not derived | [K] `PhaseSource.lean` (GR:260) | C | — | #1211, #1169 |

**Independence of #945.** Every OI-derived question in this unit (D12, D14, D17–D23) is independent of
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
| Fixed linear frame identification R1^⊗n with H-LIFT | yes | a modelling choice in MECH-2/QP [W] | no for entangling and non-A₄ operations, if Lemma F holds (D21) |
| Restriction to A₄ ≀ S_n continuations (to keep closure) | yes | none identified | keeps closure, generates no entanglement — no |
| Fixed (d, m) | yes | no | yes at each fixed (d, m) (D7) |

***

## 9. §A.31 classification of this unit's findings

- **F0** (line-number mapping in #1216's body): BORDERLINE, editorial; planning record only.
- **F1** (Main's construction is a ψ-ontic simulator; Level B as worded is met by any universal
  simulator of QM, so it is non-discriminating unless its mechanism is derived): NEW as a statement about
  Level B; it restates Main:582/:584/:602 for the operational target.
- **F2** (approximate horizon no-go, D10): ELABORATING (Main:640).
- **F3** (NX-1; NX-1 ⇒ FI-1, FI-1 ⇏ NX-1; continuity not necessary for the approximate target while the
  discrete core is): NEW. It refines BRIDGE's "FI-1 is not necessary at finite accuracy" to the E_r
  route only.
- **F4** (validity holds while closure fails at finite b; three-outcome table): NEW as a separation
  witness inside Main's own construction.
- **F5** (shuffle-only approximate joint closure: no on C, conditional no on E_f for entangling
  continuation, yes on E_r with supplied complex data): NEW.
- **F6** (#945 off the OI-derived critical path): POSITIVE (scheduling).

Two passes over §§2–5 after the first draft produced no further NEW item; §A.31's fixed point (about
three to four passes without a NEW finding) is therefore not yet reached, and the review is the next pass.

***

## 10. Questions for the owner (neutral)

- **OQ1.** Should Level B's definition require that the rule family and the procedure dictionary be
  derived from OI, with no quantum instrument data as parameter or input? Without that clause, Main:598
  meets Level B's shape at fixed (d, m, K, ε) in exact ring by simulating QM (§3.2 B-1).
- **OQ2.** Which routes count for an OI-derived Level B: C, E_f, E_r? On E_r nothing operational is
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

- **Read in full:** #1216 body and comment c.6741763726; #945 body and all comments; Main:538–:606,
  :480–:498, :520, :640; GR:248–:272; MECH-2 standing and §0; the Lean statements cited in §§4, 6, 7
  (bodies of `exists_nonMonomial_of_layerFlowExecutable`, `configurationLevel_not_layerFlowExecutable`,
  `gateFlow_half_not_preservesDiag`, and the definitions `PreservesDiag`, `IsMonomial`,
  `ConfigurationLevel`, `LayerFlowExecutable`; the other identifiers were confirmed to exist only).
  #1169, #1210, #1211: planning heads. Drafts [D]: BRIDGE §0, §5.1 (parts), §5.3 row; SHM §§1–4;
  A868 §§0, 4; A1059 §0. No kernel build was run.
- **Checks.** `probes/approx_generic_checks.py`, run `python3 -I -B` from `/tmp`: exact sympy and
  `Fraction` arithmetic on generic matrices and permutations only; no OI mechanism. Groups G1–G5, each
  with a control or countercontrol. Implementation failures, all in the checking code and none in a
  checked statement: r0 failed G1a because sympy did not simplify `Abs` of symbolic eigenvalues (replaced
  by a determinant test, r1 all pass); the first G4–G5 version used `simplify` on 512 matrix traces and
  was stopped unfinished; the second stopped on an assertion because one trace was not expanded to ±1
  (fixed with `expand`). r0 and r1 scripts and outputs are kept beside the current one; the current
  output is ALL PASS (25 checks).
- **Not done:** no computation on any OI mechanism, no simulation of Main's construction, no
  enumeration, no Lean, no git or GitHub write, no manuscript change.

## 12. Hashes

- `probes/approx_generic_checks.py`: sha256 `12aac10f6e8f8d6a7bfb7603b35aac8253132534e353791508c3cda443f172c0`
- `probes/approx_generic_checks.out`: sha256 `4337d4afc70c4fdd22deafda2eefeaa926abe044f3b7993ad47b37e9d2865c35`
- This file's own hash is reported to the coordinator, not recorded in it.
