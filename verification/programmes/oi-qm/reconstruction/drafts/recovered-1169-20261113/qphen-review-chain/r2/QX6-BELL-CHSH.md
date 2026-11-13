# QX-6: entanglement and Bell (CHSH), with complete-history no-signalling — Phase 1 experiment specification (draft r2)

## 0. Standing

- **Conventions.** Standing, snapshot (`origin/main` = `fd539e15`), evidence layers, and the separate type and
  dependency columns are as in `QX3-ANTIBUNCHING.md` §0 (r2).
- **Status.** Paper only and model-written. No mechanism is built, no computation is run, and no criterion is frozen
  (#1210 c.6736966265).
- **Revisions.**
  - r1: `r1/QX6-BELL-CHSH-r1.md` (`1534b2c2…`), reviewed REVISE in `review/REVIEW-PHASE1.md` (`8d704712…`).
  - r2 applies B1, B3, N1–N5, N7, N9 and N13. Dispositions are in `DISPOSITIONS-r2.md`.

***

## 1. The phenomenon and its operational observables

**Phenomenon.** A source prepares two systems, which are sent to two wings, `A` and `B`.
- Each wing chooses a setting (`x, y ∈ {0, 1}`) and records an outcome.
- Quantum correlations exceed the local bound `|S| ≤ 2`, where `S = E₀₀ + E₀₁ + E₁₀ − E₁₁` (Clauser, Horne, Shimony
  and Holt, PRL 23, 880 (1969); L).
- They stay within Tsirelson's bound `2√2` (Cirel'son, Lett. Math. Phys. 4, 93 (1980); L).
- Neither wing's accessible history depends on the other wing's setting.

**Observer access.** Each wing is a separate observer with its own access map: its own setting record, its own outcome
records, the herald and preparation-status records where they exist, and its own apparatus records. The other wing's
setting, the source registers and every hidden cell are not registered (L-ACC per wing). Joint statistics are formed
only after the records are brought together, which is ordinary communication outside the isolated stage.

**Outcomes and the `⊥` rule.**
- A run can end in `⊥`: failure, or no click. Full-mass accounting keeps `⊥` in the law, and failure mass is never
  renormalized away (two-system interface record (W)).
- **`S` is computed with a fixed local assignment `⊥ ↦ +1` at each wing**, declared before any run. Each wing's
  outcome is then a `±1`-valued function of its own records in every run.
- Computing `S` over coincidences only is the detection loophole and is not admitted. The law over
  `{+1, −1, ⊥}²` is reported as well.

**Observables.**
- `P(a, b | x, y)` with `a, b ∈ {+1, −1, ⊥}`.
- `E_xy` under the `⊥` rule, and `S`.
- **Complete-history no-signalling.** At fixed `y`, the law of `B`'s whole accessible history (repeated reads,
  timing, failures, apparatus records) is the same for every `x`, and symmetrically for `A` (NO-SIGNALLING.md §1
  item 2 (W); two-system interface §2 (W)). Equality of one-read marginals is not sufficient.
- **Quantum-set membership of the correlator quadruple.** The TLM/Landau criterion characterizes the correlator
  projection of the quantum set exactly (Landau, Phys. Lett. A 120, 54 (1987); L):
  `|E₀₀E₀₁ − E₁₀E₁₁| ≤ √((1−E₀₀²)(1−E₀₁²)) + √((1−E₁₀²)(1−E₁₁²))`.
  - With rational `E`, it is decided exactly by squaring with sign tracking.
  - For full behaviours with biased marginals there is no closed-form exact criterion. Membership of the full
    behaviour is then not decided exactly; that limitation is reported, not hidden by floating-point SDP output.
- **Reuse.** A second round on the same pair (two-system interface §4 (W)).

**Validation layer** (from the construction):
- the graph distance, in the graph `G` of A6.1, from each wing's first setting tick region to the other wing's readout
  region;
- whether setting generators are independent of the response-relevant pre-setting variable `Ω` (iv);
- the ontic responses, and whether one wing's response depends on the remote setting;
- the preparation-law class over which no-signalling holds.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM predictions** (comparators; IQ).
- `|Φ⁺⟩` with `A₀ = Z`, `A₁ = X` and `B_{0,1} = (Z ± X)/√2` gives `E_xy = (−1)^{xy}/√2` and `S = 2√2`, with fair
  marginals, exact no-signalling, and repeatability under local Lüders instruments.
- **Rational-angle comparator.** With angles at multiples of `π/3` (`0` and `2π/3` against `±π/3`) and
  `E = cos(θ_A − θ_B)`, the correlators are `1/2, 1/2, 1/2, −1`, so `S = 5/2`. This point lies on the TLM boundary
  (reviewer P1).
- **Stabilizer pair states with Pauli settings** [A; confirmed by the reviewer's exact probe P1 (D)]: `|S| ≤ 2`.
  - Each correlator is `±1` or `0`.
  - If both wings' pairs anticommute, at most two correlators are nonzero, since `A₀B₀` and `A₀B₁` cannot both be
    stabilizer elements (their product `I ⊗ B₀B₁` is anti-Hermitian).
  - If one wing's pair commutes, those two observables are jointly measurable, and Fine's theorem gives `|S| ≤ 2`.
    This argument covers multi-qubit wings as well.
  - P1: maximum `|S| = 2` over all 60 two-qubit stabilizer states with signed Pauli settings, and over all 1080
    three-qubit states split 1+2.
  - A **non-stabilizer** pair state with Pauli settings can reach `2√2`: for example `|Φ⁺⟩` with a local rotation on
    one side.

**The witnesses and the classes each one excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| `|S| > 2` under the `⊥ ↦ +1` rule, full mass, setting-independent `Ω` | local hidden-variable models with measurement independence. This includes every deterministic completion satisfying Main §3.3's hypotheses (Main §3.3 Theorem [P; exhaustive check 11]) and the extension A6.1 below [A] | ontically parameter-dependent deterministic models: Bohmian mechanics, and OI's chosen branch (a). Measurement-dependent models with `I_ont ≥ 0.0309` bits (Main:421). Retrocausal models. Detection-loophole models, if coincidence-only statistics were admitted. Signalling models, which the next row excludes separately |
| complete-history no-signalling | models that signal across the isolated stage, for example the shared-parity candidate on reuse (two-system interface §4, eq. (10) (W)) | local models; QM; Popescu–Rohrlich boxes; nonlocal models whose restricted preparation class balances the histories |
| `|S| ≤ 2√2` (TLM, exact on correlators) | supra-quantum correlator quadruples. OI's unrestricted response-table construction realizes the PR law (Main:362 [P]), so the check has teeth | — (an upper-bound check, not a nonclassicality witness) |
| an all-versus-nothing (GHZ-type) contradiction, optional, three wings | local hidden variables, without an inequality | the same models as the first row. **`Y` reads are not needed.** On the triangle graph state `CZ₁₂CZ₁₃CZ₂₃|+++⟩` (real, Clifford-prepared, local-Clifford equivalent to GHZ), `⟨XZZ⟩ = ⟨ZXZ⟩ = ⟨ZZX⟩ = +1` and `⟨XXX⟩ = −1`, so `XZZ + ZXZ + ZZX − XXX = 4` against a local maximum of 2 (reviewer P1 (D), exhaustive over 64 assignments). `Y` is needed only for Mermin's standard GHZ presentation, whose only full-weight `X/Z` stabilizer element is `XXX`. The option's real prerequisites are a three-party entangled source (R6.5-type, absent) and the cross-wing response (R6.7). A native `F_2` affine (toy-theory) class is itself a classical local model |

## 3. What OI's corpus already establishes about Bell (§A.19)

- **Main §3.3, Theorem (Bell ceiling for a screened local completion)** (Main:366-393; P, with the pointwise bound
  checked exhaustively). Its literal hypotheses:
  - (i) deterministic dynamics;
  - (ii) a **one-step** setting operation `u^A_a × u^B_b × id` on disjoint regions, each reading and writing only its
    own region;
  - (iii) wing `A`'s outcome a `±1` function of a readout region `R_A`, `k_A` iterates of **one fixed `φ`** after the
    setting, with `d(B, R_A) > k_A`, and symmetrically for `B`;
  - (iv) a common pre-setting ensemble, with a `±1` outcome recorded in every run.

  Under these, the model is Bell-local and `|S| ≤ 2`. The cone lemma (Main:364) uses the coupling graph read from
  `φ`. The extension to multi-step local operations and per-tick arming is A6.1 below; it is this file's derivation,
  not Main's.
- **OI's chosen branch is ontic parameter dependence**, with operational no-signalling required (Main §3.3(a);
  Main:22; Substratum:467; Methodology:393). Measurement independence is kept as a posit about the initial condition
  (Main:406-412). Measurement dependence is recorded and not adopted, with
  `S ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}` (Main:421).
- **Corollary.** The reference nearest-neighbour cubic graph alone is Bell-local for wings outside its cone
  (Main:416).
  - The proposed escape is preparation-indexed adjacency: bounded-degree Bell-relevant long edges, or an equivalent
    nonlocal response map, supplied by an entangling preparation.
  - Whether it gives parameter dependence with operational no-signalling and the continuum-curvature limit is the open
    hypothesis H-Bell (Substratum:131; Main:416).
- **Bare representability is too broad.** Globally coupled setting-dependent hidden dynamics realizes PR-box behaviour
  (Main:362): "The selector in a Bell experiment is therefore causal locality, not representability."
  - Tsirelson's `2√2` is attached to the cited stochastic causal-local indivisible layer (Substratum:481; book
    ch01:173, ch04:124).
  - C1–C4 and graph locality do not enforce it.
- **Records on `main`** (W, model-reviewed; none is an established premise):
  - `oi-qm-ext-1/two-system-interface.md`.
    - A shared-parity reversible candidate matches all four first-read quantum correlations only at the calibrated
      `η* = (1 − 1/√2)/2`, "an exact calibration, not a derivation". It needs a cross-wing controlled interaction,
      which gives up graph-cone isolation.
    - On reuse it signals: Bob's two-round history depends on Alice's settings at every `η`.
    - An *enlarged* source class admits PR behaviour at `η = 0`, as a separate conditional countercontrol. The fixed
      baseline source does not (§6 of that record).
  - `oi-qm-ext-1/prepared-pair-source.md`.
    - The source gate stops: no physical pair dynamics or preparation is specified.
    - For a fixed deterministic realization, complete-history no-signalling is a set of linear balance equations on
      the preparation law (§4). A supply law signals iff it leaves the kernel of that balance map.
    - Requiring the balance over a preparation family whose affine hull is the whole simplex makes both wings' records
      pointwise local, so `|S| ≤ 2` (§5).
  - `correlation-recombination-20261107/NO-SIGNALLING.md`. STOP: no physical experiment or interface is supplied.
    Passing no-signalling alone supplies no quantum distinction. Dropping accessible records to obtain no-signalling
    is forbidden (item 5).
  - `round-comp-1-composite-interface/result.md` (native round; receipt holds). Local tomography is the single premise
    field. No-signalling on products holds without it. The round sources no local tomography.
  - `mechanism-2-20261108/DESIGN.md` (M2D) §0 item 2, conditional on Lemma F's operation set and H-LIFT.
    - **Theorem U2.** Under R1^⊗n, every encoded unitary channel a fixed bijection at `q = 2` induces lies in
      `A_4 ≀ S_n`, with "no encoded `S`, `T`, CNOT, CZ, `rot`, or any entangling unitary".
    - **Theorem NC.** With spanning reads, "With product encoded effects it gives CHSH ≤ 2". At `q = 2` spanning needs
      a `Y` read, which is not native.
    - Within U2's scope there is no native entangling operation to prepare a pair from product supplies.
  - `h-bell/round-hb-1-obligation-shape/preregistration.md`. A control plane only, with no result.
    - It quotes the ROADMAP text recording that H-Bell is downstream of an unmet curvature re-founding obligation.
      HB-1 cites that text as ROADMAP:764-769 of an earlier ROADMAP.
    - At `fd539e15` the text is at `verification/ROADMAP.md`:974-979.

### 3.1 Is there a separable observer structure?

**Partly.** What exists:
- the causal separation of spatially separated visible regions (Main §3.4(ii), Main:652; P);
- a typed composite interface whose product laws hold without local tomography (COMP-1; K);
- per-wing access maps, supplied abstractly (two-system interface §2 (W)).

What is not established:
- statistical product structure after conditioning, local tomography, and one common tensor-product instrument
  category (Main:652);
- local tomography of any constructed composite (COMP-1);
- a native pair source (prepared-pair-source §2);
- a second observer as an embedded subsystem registering through `φ`. Main's Definition has one observer `V`, and the
  two-system interface states for a third observer: "No separate apparatus or access map is supplied".

### 3.2 Locality against OI's hidden sector

- OI's hidden sector `H = S ∖ V` is spatial wherever the substratum is, and its components obey the cone lemma. A
  shared hidden preparation is therefore a common cause.
- Under A6.1's hypotheses it cannot raise `|S|` above 2.
- Escaping A6.1 under measurement independence means one of these fails:
  - (ii) Own-wing settings, failed by **region overlap**.
  - (iii) Separation, failed by **insufficient separation** (`d ≤` the ticks elapsed).
  - The cone premise itself, by a **coupling path between the wings' regions shorter than the run**. Preparation-indexed
    long edges are OI's proposed instance.
- The first two are excluded by the experimental design (R6.2), not by any theorem. The third is R6.7.
- Any such dependence must then be invisible in each wing's complete accessible history. Over an unrestricted
  preparation class this is impossible (prepared-pair-source §5 (W)), so a restricted preparation class is required.
  - This is the structural role played by quantum equilibrium in de Broglie–Bohm theory, where non-equilibrium
    distributions signal (Valentini, Phys. Lett. A 297, 273 (2002); L).
  - In the present toolkit the only state restrictions are N2 and SA-1(c). Neither is shown to mask anything (A6.4).

## 4. What the experiment needs from an OI construction

| # | requirement | type | dependency | status |
| --- | --- | --- | --- | --- |
| R6.1 | the step, N2, the supplies | EN / CS | — | available (shared) |
| R6.2 | two wings: disjoint regions separated beyond the run's tick count in `G`, with per-wing meters | EN (the cone lemma, Main §3.3 P); CS (SA-1(b) per wing) | — | the cone lemma is proved; per-wing apparatus exists only in single-system form |
| R6.3 | per-wing observer access maps, covering each wing's complete history | CS (ACC-R2-type, per wing) | — | supplied abstractly only (W) |
| R6.4 | setting choice: own-wing operations, possibly over several ticks (P3 arming inside the wing), independent of `Ω` | CS (P3, in tension with FIX); measurement independence is a posit (Main:406-412) | — | P3 available; MI posited |
| R6.5 | a pair source: a setting-independent correlated preparation of two carriers | untyped | MECH-OPEN | **absent** (prepared-pair-source §2 (W)). Outside M2D U2's scope if it is to be entangling (W) |
| R6.6 | local settings at non-Pauli directions, for QM-matching correlators at identified settings with a stabilizer pair state | — | MC | not native (`{0, π}`; A6.2) |
| R6.7 | **a cross-wing response**: preparation-indexed adjacency, or an equivalent nonlocal response map | CS as the named open hypothesis H-Bell (dynamics type) | MECH-OPEN | open (Substratum:131; Main:416). A Boolean specification exists without a physical source, and it fails on reuse (W) |
| R6.8 | **complete-history no-signalling** across the isolated stage, reuse included | a constraint on R6.7 together with the preparation class | MECH-OPEN | open; failed by the shared-parity candidate (W) |
| R6.9 | a restricted preparation class under which R6.7 balances in every wing's history | CS (a state restriction; the present toolkit offers N2 and SA-1(c)) | MECH-OPEN | open; no masking shown (A6.4) |
| R6.10 | Tsirelson soundness: no admitted preparation gives `|S| > 2√2` | constraint | MECH-OPEN | open. An enlarged source class reaches PR (two-system interface §6 (W); Main:362) |
| R6.11 | post-measurement state update and repeatability on the measured pair, with no silent fresh source | untyped | MECH-OPEN | open (two-system interface §4 (W)) |
| R6.12 | local tomography of the constructed composite | carried as a hypothesis (the COMP-1 premise field) | — | not sourced |
| R6.13 | the declared local `⊥ ↦ +1` rule | protocol | — | stated here (§1) |

**Derivations** (A; unreviewed unless marked).

**A6.1. A Bell ceiling for time-dependent local dynamics. This file's extension of Main §3.3, not Main's
statement.**

Hypotheses:
- *(D)* The run is deterministic. At tick `t` the map applied is a bijection `φ_t`. Every `φ_t` has its one-step
  dependency graph contained in one fixed graph `G` on the sites. `G` includes every edge that any arming ever
  switches on.
- *(L)* Wing `A`'s setting `a` acts only through operations that, at each tick, read and write only `A`'s region, or
  arm only edges of `G` inside `A`'s region. The first such tick is `t_A`. The same holds for `B`, with `t_B`.
  Multi-tick settings and per-tick P3 arming inside the wing are included.
- *(R)* Wing `A`'s outcome is a fixed `±1` function of its own records at tick `T_A`, with `⊥ ↦ +1`. The records lie
  in a region `R_A` with `d_G(B's region, R_A) > T_A − t_B`, and symmetrically for `B`.
- *(MI)* The pre-setting variable `Ω` that fixes both wings' responses to every setting is independent of `(a, b)`.

Conclusion: there are deterministic local response functions, so `|S| ≤ 2`.

*Proof sketch.*
1. By induction on ticks, for maps whose dependency graphs lie in `G`, the state at site `i` and tick `t` depends only
   on the tick-`s` state in the `G`-ball of radius `t − s` around `i`.
2. Two runs differing only in `b` agree everywhere until `t_B`. After that, `B`'s operations act within `B`'s region,
   and every other map is `b`-independent with dependency in `G`.
3. So the runs can differ at tick `t` only within distance `t − t_B` of `B`'s region. By (R) they agree on `R_A` at
   `T_A`.
4. Hence `A`'s `±1` outcome is a function of `(Ω, a)`, and symmetrically for `B`. Measurement independence and the
   pointwise CHSH bound over the sixteen deterministic response tables give `|S| ≤ 2`, as in Main's proof. ∎

*Scope.* A6.1 needs (D), (L), (R) with the `⊥` rule, and (MI). It says nothing about constructions with a cross-wing
edge in `G` that is reachable within the run (R6.7), measurement dependence, or coincidence-only statistics.

**Consequence for the ablations.** Consider constructions satisfying (D), (L), (R) and (MI). In them, none of the
following can be credited with `|S| > 2`:
- construction B's access restrictions;
- state restrictions on a setting-independent ensemble;
- own-wing local operations, Obligation C's included;
- local registration rules.

This is narrower than "observational-incompleteness principles cannot give Bell violation". R6.7 is itself a
candidate OI principle (H-Bell), and A6.1 does not cover it.

**A6.2. Obligation C: necessary for QM-matching settings with stabilizer pair states, and not sufficient.**
- *Necessary, qualified.* Suppose settings are identified as local read directions (an L-CAL-type identification),
  the pair state is a stabilizer state, and local operations are Clifford-class. Then QM itself gives `|S| ≤ 2` (§2).
  A construction exceeding 2 there would disagree with QM. A non-stabilizer pair state with Pauli settings reaches
  `2√2`, so with such a source (R6.5) the requirement moves from the settings to the source.
- *Not sufficient.* Own-wing operations do not exceed 2 under A6.1's hypotheses.
- *Not needed for raw first-read correlations.* The shared-parity candidate reaches `S = 4(1 − 2η)` with abstract
  settings and no coherent operation (W).
- *For #1210.* "QX-6 blocked on QX-1" captures the setting requirement in the stabilizer-pair case. The binding
  prerequisites are R6.5, R6.7 and R6.8.

**A6.3. Probabilities are rational.**
- N2 counting gives dyadic laws, so `S = 2√2` and the correlators `±1/√2` are unreachable exactly, though approachable
  within `ε`.
- The rational comparator `S = 5/2` (at `π/3` angles) is exact and lies on the TLM boundary.
- C-EXPOSURE's R60 type gives `π/3`-grid local settings only if its rotation axis is orthogonal to the read plane.
  That is not computed here.

**A6.4. The supply restriction and no-signalling: a requirement, not a result.**
- By prepared-pair-source §§4–5 (W), a parameter-dependent deterministic completion is no-signalling only over
  preparation laws in the kernel of its balance map. Over an unrestricted class the completion is pointwise local.
- If construction B supplies R6.7, R6.9 must be some state restriction. N2 and SA-1(c) are the only state restrictions
  in the present toolkit, and neither is shown to mask.
- Whether ABL-SA1c or ABL-N2 leaves the kernel, and so signals, depends on the construction and is not predicted here.
- §A.31 note: the reading that "non-equilibrium supplies signal" would be a consequence beyond the Bell target, a
  §A.29-type corollary. Because it favours the framework, it is recorded as a hypothesis to be tested against a fixed
  construction, not as a prediction.

## 5. Reuse of the single shared construction

**Shared with every QX:**
- the step;
- N2 and the supply restrictions;
- the SA-1(b) meters;
- P3 arming or its FIX-compatible replacement;
- the typed identifications (D18(a), conditional; #1169 c.6735014875).

**Shared with QX-1, QX-4c and QX-7.** The local non-Clifford operation that sets read directions (R6.6), which is
Obligation C's. A QX-6-specific local gate is not admissible.

**Shared with QX-3's W3 and Q-C2-1's NR-11.** Two systems, a composite, a pair source, and local tomography as a
hypothesis.

**Specific to QX-6:**
- R6.7, the cross-wing response;
- R6.8 and R6.10, the history balance and the Tsirelson bound;
- the per-wing access maps;
- the `⊥` rule;
- the GHZ-type option, which needs a three-party source.

**Flagged imported quantum assumptions** (IQ, benchmark only): the calibrated `η*`; any supplied entangled pair law;
local Lüders instruments imported for the continuation.

## 6. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_6`.** Two wings under the reference nearest-neighbour substratum, with the B scaffolding needed for settings
  and records. Expected `|S| ≤ 2`, a consequence of Main §3.3 (P) for one-step settings and of A6.1 [A] for
  multi-tick ones.
- **`B_6-loc`.** Construction B with every single-system principle and C's local operation, satisfying A6.1's
  hypotheses with the `⊥` rule. Expected `|S| ≤ 2`. This shows that access restrictions, state restrictions on a
  setting-independent ensemble, own-wing operations and local registration rules do not give Bell violation in that
  class. It shows nothing about R6.7.
- **`B_6-nl`.** `B_6-loc` plus R6.7 and R6.9. The questions are whether `|S| > 2` with complete-history no-signalling,
  reuse included, and whether `|S| ≤ 2√2`. No value is predicted.
- **Benchmark** (IQ, labelled): the shared-parity candidate at `η*`, or a supplied `|Φ⁺⟩` law.
- **Comparators** (gate nothing):
  - LHV-6: `|S| ≤ 2`, no-signalling;
  - PR-6: `S = 4`, an enlarged source class (Main:362; W);
  - SIG-6: shared-parity reuse, which signals (W);
  - QM-6: `2√2`, and `5/2` at the rational settings.

**Candidate ablations.** Each reports `pred_change`, `mech_change` and `access_only`.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-NL: R6.7 removed | dynamics | `|S| ≤ 2` (A6.1). `pred_change` is true if `B_6-nl` exceeded 2 |
| ABL-SA1c / ABL-N2: sharp or non-uniform supply | state restriction; credit none | signals iff the supply leaves the kernel of the balance map (A6.4). Not predicted |
| ABL-ACC: a wing's access map widened | access | if no-signalling then fails, the balance was an access artefact. "Unread" fields may not be declared private (W). `access_only` true |
| ABL-ACC-narrow: access narrowed | access | no-signalling obtained this way is not creditable (NO-SIGNALLING.md item 5 (W)) |
| ABL-BOT: `⊥` rule varied (`⊥ ↦ +1` against `⊥ ↦ −1`) or coincidence-only | protocol | the first two keep A6.1's hypothesis. Coincidence-only is the detection loophole and is reported, never credited |
| ABL-MI: settings correlated with `Ω` | breaks (MI) | bounded by Main:421; reported, not adopted |
| ABL-C: C's local operation replaced by a Clifford-class one | dynamics (local) | QM-matching correlators are lost at identified settings with a stabilizer pair state (A6.2) |
| ABL-REUSE: a second round on the same pair | protocol | tests R6.8 and R6.11 |

## 7. Dependence on Q-C2-1's outcomes, and dependencies Q-C2-1 does not cover (decision tree)

```
Bell-specific prerequisites, independent of every Q-C2-1 token:
  R6.5 pair source, R6.7 cross-wing response (H-Bell), R6.8 history no-signalling, R6.10 Tsirelson.
  If any is missing → QX-6 is limited to A_6 / B_6-loc (|S| ≤ 2 by Main §3.3 and A6.1) plus benchmark arms.

Q-C2-1 C token (governs R6.6, the local settings, in the stabilizer-pair case)
├─ C-EXPOSURE, R60 type (STAB true) ── a π/3-grid local-setting candidate; the QM comparator is S = 5/2. Usable only
│                          if the axis is orthogonal to the read plane (A6.3), and only inside B_6-nl.
├─ C-EXPOSURE, S_3 type ── improper; no rotation of read directions; R6.6 stays open.
├─ C-EXPOSURE, STAB false ── irrational-angle rotations (e.g. arccos(3/5)) give other rational S comparators.
│   (C-EXPOSURE's W-CL conclusions rest on Theorem C [D] and Lemma P, proved conditional on Theorem C(ii), L1–L3.)
├─ C-SIZE-DEPENDENT ─────── local settings need 1–2 applications per run; same conditions.
├─ C-NONSTABILIZER ──────── non-stabilizer local states, no non-Clifford operation. A QM-matching excess at Pauli reads
│                          then needs a non-stabilizer pair state, which needs R6.5 anyway.
├─ C-SURVIVAL ───────────── R6.6 not native; QM-matching settings are benchmark-only. B_6-loc stays ≤ 2 (A6.1).
└─ C-VOID ───────────────── no reading.

Q-C2-1 P token
├─ P-COMPLEMENTARITY ──── per-wing meters and backaction are validated (needed for R6.11's continuation).
└─ otherwise ───────────── per-wing apparatus validation is missing; QX-6 waits on it, whatever the C token.

Q-C2-1 D15 typing (Acc typed CS, D15(a), c.6735014875) → the per-wing access maps (R6.3) take the same kind of owner
typing. A B-CONTEXTUAL fragment does not transfer to the two-wing fragment.

Q-C2-1 A/B readings → if SA-1(c) carries P's universality reading, it is a candidate for R6.9 (A6.4). Not a result.
```

## 8. Known feasibility obstacles

1. **Two-system structure.** There is no native pair source (R6.5), no constructed composite with local tomography
   (R6.12), and no embedded second observer (§3.1).
2. **Local constructions are capped.** Under Main §3.3 (one-step settings) and A6.1 (multi-tick local settings, [A]),
   with the `⊥` rule, `|S| ≤ 2`.
   - A Bell excess needs R6.7 (H-Bell), which is open.
   - The ROADMAP records H-Bell as downstream of an unmet curvature re-founding obligation (`verification/ROADMAP.md`
     :974-979 at `fd539e15`, quoted in HB-1 under its earlier line numbers 764-769).
3. **Reuse signalling.** The only explicit nonlocal candidate on record signals on reuse at every calibration (W).
4. **Preparation-class restriction.**
   - No-signalling needs supply laws in the kernel of the balance map (A6.4; W).
   - The admitted class must also exclude PR-type sources (R6.10).
   - No principle is known that bounds `S` at `2√2`.
5. **Calibration as import.** Matching `2√2` by choosing `η*` is IQ (W). Rational N2 laws cannot reach it exactly
   (A6.3).
6. **Settings.** QM-matching local settings with stabilizer pair states need Obligation C (A6.2). Measurement
   independence is posited (Main:406-412).
7. **P3 against FIX.** Per-tick arming as the setting switch is in tension with one fixed law (OICORE-1 §2;
   `DESIGN-DS.md` §2 [D]). A6.1 admits it only inside each wing's region.
8. **No native entangling operation within U2's scope** (M2D Theorem U2 (W), conditional on R1^⊗n, Lemma F and
   H-LIFT).
9. **Access artefacts.** Narrowing a wing's access can manufacture no-signalling. ABL-ACC-narrow is not creditable,
   and `access_only` must be printed.
10. **Biased marginals.** For full behaviours, quantum-set membership has no exact closed-form test (§1).

## 9. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.** Quantum-compatible two-wing correlations with complete-history no-signalling and `|S| ≤ 2`, the `⊥`
  rule stated. `B_6-loc` can reach this.
- **Level 2.** `|S| > 2` with the `⊥` rule, full mass, measurement independence and complete-history no-signalling,
  reuse included.
  - This excludes local hidden-variable models with measurement independence.
  - It is printed with: "it does not exclude ontically parameter-dependent deterministic models, of which this
    construction is one". It needs `B_6-nl`.
- **Level 3.** R6.7 and R6.6 are generated natively, not calibrated. The supply restriction R6.9 is fixed in advance
  (§A.29), and Tsirelson soundness holds over the admitted preparation class.
- **Level 4.** Repeated rounds and local instruments composed under one rule. Not addressed.

## 10. Owner questions (neutral)

- **Q6-1.** Which prerequisites should #1210's table list for QX-6?
  - (a) Keep "blocked: QX-1".
  - (b) Add "H-Bell (R6.7), pair source (R6.5), complete-history no-signalling (R6.8)" (A6.2).
- **Q6-2.** How is R6.7 typed?
  - (a) CS (named open hypothesis H-Bell, dynamics).
  - (b) Untyped until a physical source is specified.
- **Q6-3.** Is the reuse round (R6.11) part of the no-signalling test?
  - (a) Yes.
  - (b) First round only, with the limitation printed.
- **Q6-4.** Which local `⊥` rule applies?
  - (a) `⊥ ↦ +1`.
  - (b) Another fixed local rule, declared before any run.
- **Q6-5.** What is HB-1's relation to QX-6 (#1060's frozen legacy H-Bell shape round)?
  - (a) Cite it as provenance.
  - (b) Make it a prerequisite.

## 11. References to content off `main` (§A.42 item 8), traced one by one

| reference | claim it is attached to | classification |
| --- | --- | --- |
| #1210 c.6736966265 | §0 scope | provenance (authority) |
| #1169 c.6734304025, c.6734374076 | the A/B arms; ablation fields | owner records of direction; quoted in the programme |
| #1169 c.6735014875 (D15(a), D18(a) conditional) | §5; §7 | owner decision; quoted in QX-3 §0 |
| #1060 (HB-1's accountable Issue) | Q6-5 | provenance |
| Main:22, :362-429, :652; Substratum:131, :467, :481; Methodology:393; book ch01:173, ch04:124 | §3; A6.1's base theorem | on `main` (P) |
| `verification/ROADMAP.md`:974-979 at `fd539e15` | §8 item 2 | on `main` (a frozen record) |
| `oi-qm-ext-1/two-system-interface.md`, `prepared-pair-source.md`; `correlation-recombination-20261107/NO-SIGNALLING.md` | §3; A6.2; A6.4; §8 | on `main` (W); not established premises (§A.46 item 7) |
| M2D Theorems U2 and NC | §3; §8 item 8 | on `main` (W), conditional |
| `round-comp-1-composite-interface/result.md` | §3.1 | on `main`; native round, kernel |
| `h-bell/round-hb-1-obligation-shape/preregistration.md` | §3; §8 item 2 | on `main` (frozen control plane) |
| `oicore/OICORE-1.md` §2 (FIX) | §8 item 7 | off `main` (D) |
| Q-C2-1 r13 drafts (`DESIGN-DS.md` §2; tokens; cone and Lemma P reviews; NR-11) | §§5, 7, 8 | off `main` (D) |
| `review/REVIEW-PHASE1.md`; probe `review/probes/p1_chsh_stabilizer.py` (`af34edb8…`) | §2: the stabilizer bound's confirmation, the triangle-graph contradiction, `S = 5/2` on the TLM boundary | off `main` (D); an exact finite computation on generic stabilizer objects |
| CHSH 1969; Cirel'son 1980; Landau 1987; Valentini 2002; Fine 1982; Coecke–Edwards–Spekkens 2011 | §§1–3 | literature. The Coecke–Edwards–Spekkens abstract was read; it is no longer cited for the GHZ claim. The others were not read first-hand |
