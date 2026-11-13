# QX-6: entanglement and Bell (CHSH), with complete-history no-signalling — Phase 1 experiment specification (draft r7b)

## 0. Standing

- **Conventions.** Standing, snapshot (`origin/main` = `fd539e15`), evidence layers, and the separate type and
  dependency columns are as in `QX3-ANTIBUNCHING.md` §0 (r7b).
- **Status.** Paper only and model-written. No mechanism is built, no computation on any proposed OI mechanism is
  run, and no criterion is frozen (#1210 c.6736966265). Exact checks of paper claims on generic mathematical objects
  are allowed when labelled as such: "Allowed: generic checks" (#1210 c.6739250392, owner, 2026-11-09). The checks
  cited here (probes P1–P6, P11 and P12 under `review/probes/`) are of that kind, and a result supported only by such a check is
  marked computation-supported in `SHARED-MECHANISM.md` §8.
- **Revisions.** Earlier texts are kept under `r1/`, `r2/`, `r3/`, `r4/`, `r5/`, `r6/`, `r7/` and `r7a/`. The
  revision record is `DISPOSITIONS-r7b.md`.
- **Claim status** of this file's claims (proved, disproved, open) is given in `SHARED-MECHANISM.md` §8, and the
  restrictions it uses in §9.

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
  projection of the quantum set exactly. Necessity: Landau, Phys. Lett. A 120, 54 (1987). Sufficiency: Landau,
  Found. Phys. 18, 449 (1988), and Masanes (2003). L, none read first-hand:
  `|E₀₀E₀₁ − E₁₀E₁₁| ≤ √((1−E₀₀²)(1−E₀₁²)) + √((1−E₁₀²)(1−E₁₁²))`.
  - With rational `E`, it is decided exactly by squaring with sign tracking.
  - For full behaviours with biased marginals there is no closed-form exact criterion. Membership of the full
    behaviour is then not decided exactly; that limitation is reported, not hidden by floating-point SDP output.
- **Reuse.** A second round on the same pair (two-system interface §4 (W)).

**Validation layer** (from the construction):
- whether every tick's map is independent of each wing's setting outside that wing's region (A6.1 (L′)), and the
  first ticks `t_A`, `t_B` at which a setting acts;
- the distances `d_{G_B}(B, R_A)` and `d_{G_A}(A, R_B)` of A6.1 (R), against `T_A − t_B` and `T_B − t_A`;
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
- **Stabilizer pair states with Pauli settings** [A; confirmed by the reviewer's exact probe P1 (X)]: `|S| ≤ 2`.
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
| `|S| > 2` under the `⊥ ↦ +1` rule, full mass, setting-independent `Ω` | local hidden-variable models with measurement independence. This includes every deterministic completion satisfying Main §3.3's hypotheses (Main §3.3 Theorem [P; exhaustive check 11]), and every completion satisfying the hypotheses of the extension A6.1 below, including its design assumptions (L′) and (R) [A] | ontically parameter-dependent deterministic models: Bohmian mechanics, and OI's chosen branch (a). Measurement-dependent models with `I_ont ≥ (S − 2)²/(32 ln 2)` bits for the observed `S` (Main:418-421), which is `0.0309` bits at `S = 2√2`. Retrocausal models. Detection-loophole models, if coincidence-only statistics were admitted. Signalling models, which the next row excludes separately |
| complete-history no-signalling | models that signal across the isolated stage, for example the shared-parity candidate on reuse (two-system interface §4, eq. (10) (W)) | local models; QM; Popescu–Rohrlich boxes; nonlocal models whose restricted preparation class balances the histories |
| `|S| ≤ 2√2` (TLM, exact on correlators) | correlator quadruples outside the quantum set, which Tsirelson's bound and the TLM criterion delimit for every bipartite tensor-product quantum strategy, whatever the measurements. OI's unrestricted response-table construction realizes the PR law (Main:362 [P]), so the check has teeth | — (an upper-bound check, not a nonclassicality witness) |
| an all-versus-nothing (GHZ-type) contradiction, optional, three wings; two protocols, GHZ-1 and GHZ-2 below | local hidden variables, without an inequality | the same models as the first row |

**The GHZ-type option: two protocols** [X, exact: reviewer P1 and P4(3); writer's probe P5-GHZ; computation-supported].
- **GHZ-1, the conventional protocol (Mermin).**
  - State: `|GHZ⟩ = (|000⟩ + |111⟩)/√2`.
  - Per-qubit read bases: `X` or `Y`.
  - Operators and QM predictions: `⟨XXX⟩ = +1`, `⟨XYY⟩ = ⟨YXY⟩ = ⟨YYX⟩ = −1`, so
    `⟨XXX⟩ − ⟨XYY⟩ − ⟨YXY⟩ − ⟨YYX⟩ = 4`, against a local maximum of 2 (exhaustive over 64 assignments).
  - On this state `X/Z` reads give no all-versus-nothing contradiction. The `X/Z` Pauli strings with nonzero
    expectation are `ZZI`, `IZZ`, `ZIZ` and `XXX`, all `+1`, and the single local assignment `x_i = z_i = +1`
    satisfies all of them. `XXX` is the only full-weight one.
- **GHZ-2, the rotated protocol.**
  - State: the triangle graph state `CZ₁₂CZ₁₃CZ₂₃|+++⟩`. It is real and Clifford-prepared, and
    `(SH ⊗ SH ⊗ SHS)|GHZ⟩ = e^{iπ/4} CZ₁₂CZ₁₃CZ₂₃|+++⟩` (operators act right to left).
  - Per-qubit read bases: `X` or `Z`.
  - Operators and QM predictions: `⟨XZZ⟩ = ⟨ZXZ⟩ = ⟨ZZX⟩ = +1`, `⟨XXX⟩ = −1`, so
    `⟨XZZ⟩ + ⟨ZXZ⟩ + ⟨ZZX⟩ − ⟨XXX⟩ = 4`, against a local maximum of 2 (exhaustive over 64 assignments).
- **Which protocol an `X/Z`-only access class can pose.** Only GHZ-2. GHZ-1 needs `Y` reads, which are not native
  under the one-cell identification (SHARED M11).
- **Prerequisites of either protocol.**
  - a three-party entangled source (R6.5-type, absent);
  - the cross-wing response (R6.7).

  A native `F_2` affine (toy-theory) class is itself a classical local model.

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
    - On reuse it signals: Bob's two-round history depends on Alice's settings at every `η` and every herald rate
      `h > 0` (eq. (11) and the text below it).
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
    - **Theorem NC.** Under an injective identification (R1^⊗n, or R-W at odd `q`) with spanning reads, "With
      product encoded effects it gives CHSH ≤ 2" (M2D:65-71; Theorem NC at M2D:483-497; Corollary NC-B at
      M2D:509-516). At `q = 2` spanning needs
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
  - (L′) Own-wing settings, failed by **region overlap**, or by a tick whose map outside a wing's region depends on
    that wing's setting, for example a setting operation composed with a coupling step within one tick (P4(1)).
  - (R) Separation, failed by **insufficient separation**: the regions are placed too close in the designed reference
    graph `G_ref`, the union over the ticks after `t_B` of the dependency graphs the design specifies (for OI, the
    bounded-range reference graph of Main §3.3(a), Main:414, with no preparation-indexed edge). Then
    `d_{G_ref}(B, R_A) ≤ T_A − t_B` and `d_{G_B}(B, R_A) ≤ T_A − t_B`.
  - (R) again, by a **coupling path between the wings' regions shorter than the run, with an edge outside `G_ref`**:
    `d_{G_B}(B, R_A) ≤ T_A − t_B < d_{G_ref}(B, R_A)`. Preparation-indexed long edges are OI's proposed instance.
- The first two are excluded by the experimental design (R6.2, R6.4), not by any theorem. The third is R6.7.
- For Level 2 (§9), any such dependence must also be invisible in each wing's complete accessible history. Under (D)
  and (MI), with the `⊥` rule, `|S| > 2` with complete-history no-signalling needs an admitted preparation class
  whose affine hull excludes the point mass at some `Ω` in the support (SHARED Q6-P12 [A]; prepared-pair-source §5 (W)
  states this for its balance map). That target therefore requires a restricted preparation class.
  - This is the structural role played by quantum equilibrium in de Broglie–Bohm theory, where non-equilibrium
    distributions signal (Valentini, Phys. Lett. A 297, 273 (2002); L).
  - In the present toolkit the only state restrictions are N2 and SA-1(c). Neither is shown to mask anything (A6.4).

## 4. What the experiment needs from an OI construction

| # | requirement | type | dependency | status |
| --- | --- | --- | --- | --- |
| R6.1 | the step, N2, the supplies | EN / CS | — | available (shared) |
| R6.2 | two wings: disjoint regions separated beyond the run's tick count in `G_B` and `G_A` (A6.1 (R)), with per-wing meters | design assumption of the Bell test (A6.1 (R)), not a consequence of OI. The design guarantees separation in the designed reference graph `G_ref` (§3.2); (R) on `G_B` and `G_A` is the assumption whose failure through edges outside `G_ref` is R6.7; the cone lemma it uses is P (Main §3.3); CS (SA-1(b) per wing) | — | the cone lemma is proved; per-wing apparatus exists only in single-system form |
| R6.3 | per-wing observer access maps, covering each wing's complete history | CS (ACC-R2-type, per wing) | — | supplied abstractly only (W) |
| R6.4 | setting choice: own-wing operations, possibly over several ticks (P3 arming inside the wing), with every tick's map independent of the setting outside the wing's region (A6.1 (L′)), independent of `Ω` | design assumption of the Bell test (A6.1 (L′)), not a consequence of OI; CS (P3, in tension with FIX); measurement independence is a posit (Main:406-412) | — | P3 available; MI posited |
| R6.5 | a pair source: a setting-independent correlated preparation of two carriers | untyped | MECH-OPEN | **absent** (prepared-pair-source §2 (W)). Outside M2D U2's scope if it is to be entangling (W) |
| R6.6 | local settings at non-Pauli directions, for QM-matching correlators at identified settings with a stabilizer pair state | — | MC | not native (`{0, π}`; A6.2) |
| R6.7 | **a cross-wing response**: preparation-indexed adjacency, or an equivalent nonlocal response map | CS as the named open hypothesis H-Bell (dynamics type) | MECH-OPEN | open (Substratum:131; Main:416). A Boolean specification exists without a physical source, and it fails on reuse (W) |
| R6.8 | **complete-history no-signalling** across the isolated stage, reuse included | a constraint on R6.7 together with the preparation class | MECH-OPEN | open; failed by the shared-parity candidate (W) |
| R6.9 | a restricted preparation class under which R6.7 balances in every wing's history | CS (a state restriction; the present toolkit offers N2 and SA-1(c)) | MECH-OPEN | open; no masking shown (A6.4). A class fixed only by the balance equations is fitted to no-signalling. It is creditable only if fixed in advance by a principle with an independent reason and a consequence of its own (§A.29; SHARED §9) |
| R6.10 | Tsirelson soundness: no admitted preparation gives `|S| > 2√2` | constraint; its only identified support is agreement with QM or a premise with quantum structure, so it is a hypothesis under test (SHARED §9) | MECH-OPEN | open. An enlarged source class reaches PR (two-system interface §6 (W); Main:362) |
| R6.11 | post-measurement state update and repeatability on the measured pair, with no silent fresh source | untyped | MECH-OPEN | open (two-system interface §4 (W)) |
| R6.12 | local tomography of the constructed composite | carried as a hypothesis (the COMP-1 premise field) | — | not sourced |
| R6.13 | the declared local `⊥ ↦ +1` rule | protocol | — | stated here (§1) |

**Derivations** (A; unreviewed unless marked).

**A6.1. A Bell ceiling for time-dependent local dynamics. This file's extension of Main §3.3, not Main's
statement** [A; complete proof below; each hypothesis checked against Main's text in the table that follows;
independently reviewed in `review/REVIEW-PHASE1-r3.md` (`448614ea…`). Proved conditional on (D), (L′), (R) and (MI).]

(L′) and (R) are design assumptions of the Bell test: own-wing settings and separation. They are not consequences of
OI. OI's chosen branch (a) gives up Main's (ii) and (iii), of which (L′) and (R) are the generalizations
(Main:403-406, :414), and H-Bell's preparation-indexed long edges are a failure of (R) (§3.2).

*Setting.*
- The sites form a finite set `V`, and the configuration space is `∏_{i∈V} S_i` with each `S_i` finite.
- Ticks are numbered `t = 1, 2, …`. `x_0` is the pre-setting configuration, and `x_t = φ_t^{(a,b)}(x_{t−1})`, where
  `φ_t^{(a,b)}` is the map applied at tick `t` under the settings `(a, b)`.
- The wing regions `A`, `B ⊂ V` are disjoint.
- The dependency graph `G_t` of tick `t` is defined as Main defines `G_φ` (Main:364): `i ∼ j` whenever the `i`th
  output component of `φ_t^{(a,b)}` depends on the `j`th input component for some configuration and some settings,
  symmetrized. `N̄_t(i)` is `i` together with its `G_t`-neighbours.
- For a graph `H` and `U ⊆ V`, `N^H_r(U)` is the set of sites within `H`-distance `r` of `U`.

*Hypotheses.*
- *(D)* The run is deterministic: each `φ_t^{(a,b)}` is a map of the configuration space. Bijectivity is not used.
- *(L′)* For every tick `t` and every `a`, the maps `φ_t^{(a,b)}` for different values of `b` agree on every
  component outside `B`: `φ_t^{(a,b)}(x)_i = φ_t^{(a,b′)}(x)_i` for every `x` and every `i ∉ B`. Symmetrically, the
  maps for different values of `a` agree on every component outside `A`.
  - `t_B` is the earliest tick at which any value of `b` acts: the least `t` with `φ_t^{(a,b)} ≠ φ_t^{(a,b′)}` for
    some `a, b, b′`. `t_A` is defined in the same way.
  - Multi-tick settings, and per-tick arming of edges with both ends in the wing's region, satisfy (L′).
  - An operation that reads and writes only `B`'s region does not satisfy (L′) when it is composed, within one tick,
    with a step that copies a `B`-site to a site outside `B` (P4(1); SHARED §8).
- *(R)* Wing `A`'s outcome is a fixed `±1`-valued function of the configuration on a readout region `R_A` after tick
  `T_A`, with the `⊥ ↦ +1` rule. With `G_B = ⋃_{t > t_B} G_t`, the readout region satisfies
  `d_{G_B}(B, R_A) > T_A − t_B`. Symmetrically, with `G_A = ⋃_{t > t_A} G_t`, `d_{G_A}(A, R_B) > T_B − t_A`.
- *(MI)* A pre-setting variable `Ω`, a function of `x_0`, fixes each wing's outcome for every setting pair, and
  `p(Ω | a, b) = p(Ω)`.

*Conclusion.* There are functions `q_a(Ω)` and `r_b(Ω)` with
`P(q, r | a, b) = Σ_Ω p(Ω) 1[q = q_a(Ω)] 1[r = r_b(Ω)]`, so `|S| ≤ 2`.

*Proof.*
1. *One tick is local.* Fix `t`, `i` and the settings. If `x` and `y` agree on `N̄_t(i)`, then
   `φ_t^{(a,b)}(x)_i = φ_t^{(a,b)}(y)_i`. To see this, change the components of `x` outside `N̄_t(i)` to those of `y`
   one at a time. `V` is finite, so this takes finitely many steps, and by the definition of `G_t` no step changes the
   `i`th output.
2. *Before `t_B`.* Fix `x_0` and `a`, and two values `b`, `b′`. Write `x_t` and `x′_t` for the two runs, and
   `Δ_t = {i : x_t(i) ≠ x′_t(i)}`. For `t < t_B` the two runs apply the same maps to the same `x_0`, so `Δ_t = ∅`.
3. *At `t_B`.* The inputs `x_{t_B−1}` and `x′_{t_B−1}` coincide, and by (L′) the two maps agree on every component
   outside `B`. So `Δ_{t_B} ⊆ B = N^{G_B}_0(B)`.
4. *After `t_B`.* Suppose `Δ_{t−1} ⊆ N^{G_B}_{t−1−t_B}(B)` for some `t > t_B`. Let `i ∈ Δ_t` with `i ∉ B`.
   - By (L′) the `i`th components of the two tick-`t` maps are one function.
   - So by step 1 the two inputs differ somewhere on `N̄_t(i)`: some `j ∈ N̄_t(i)` lies in `Δ_{t−1}`.
   - Since `G_t ⊆ G_B`, `d_{G_B}(i, B) ≤ 1 + d_{G_B}(j, B) ≤ t − t_B`.

   Sites of `B` lie in every ball around `B`. So `Δ_t ⊆ N^{G_B}_{t−t_B}(B)`, and by induction this holds for every
   `t ≥ t_B`.
5. *Readout.*
   - If `T_A < t_B`, then `Δ_{T_A} = ∅` by step 2.
   - Otherwise `Δ_{T_A} ⊆ N^{G_B}_{T_A−t_B}(B)` by steps 3 and 4, and (R) makes this set disjoint from `R_A`.

   Either way the configuration on `R_A` after tick `T_A` is the same for `b` and `b′`, so `A`'s outcome depends on
   `x_0` and `a` only. Symmetrically, `B`'s outcome depends on `x_0` and `b` only.
6. *Response functions.*
   - By (MI) each outcome is a function `F(Ω, a, b)`. For each `Ω` in the support, choose `x_0` with that value of
     `Ω`. Step 5 at that `x_0` gives `F_A(Ω, a, b) = F_A(Ω, a, b′)`, and symmetrically for `B`. This defines
     `q_a(Ω)` and `r_b(Ω)`.
   - Then `P(q, r | a, b) = Σ_Ω p(Ω | a, b) 1[q = q_a(Ω)] 1[r = r_b(Ω)]`, and (MI) replaces `p(Ω | a, b)` by `p(Ω)`.
   - Pointwise, `q_0(r_0 + r_1) + q_1(r_0 − r_1) ∈ {−2, 2}`. Averaging over `p(Ω)` gives `|S| ≤ 2`. ∎

*Checks* (probe P5-A61, X, reproduced by `p6_r3rev_a61.py`; exact, the random-construction check a finite sample;
they support the proof and do not replace it):
- **The one-tick composite of P4(1).** (L′) fails, and `S = 4`.
- **The same three operations on three separate ticks.** (L′) holds, (R) fails (`d_{G_B} = 2 = T_A − t_B`), and
  `S = 4`.
- **Random local reversible constructions satisfying (D) and (L′).**
  - Over 2,734 wing-cases where (R) holds, no readout depends on the remote setting.
  - Where (R) fails, 642 of 2,524 wing-cases show dependence, so (R) is not vacuous.

*Main §3.3's hypotheses checked against A6.1's* (Main:364-389):

| A6.1 | Main's text | does Main's setting satisfy it? |
| --- | --- | --- |
| finite `V`, `∏ S_i` | Main:364: "`S=∏_{i∈V}S_i`, with `V` and each `S_i` finite" | yes |
| `G_t` | Main:364: `G_φ` "by one-step dependency … symmetrized" | yes: the same definition, applied to each tick |
| (D) | (i) "the dynamics is deterministic" | yes. Main's `φ` is also a bijection (Main:56, Lemma 3), which A6.1 does not use |
| (L′) | (ii) "`u^A_a × u^B_b × id` … on disjoint regions `A` and `B` at one step, each intervention reading and writing only its own region" | yes. Tick 1 is the setting step. Outside `B` its components are `u^A_a` on `A` and the identity elsewhere, and neither depends on `b`; symmetrically for `A`. The later ticks are iterates of `φ`, which depend on no setting. So `t_A = t_B = 1` |
| (R) | (iii) outcome "a `±1`-valued function of the state on a readout region `R_A` `k_A` updates after the setting, with `d(B, R_A) > k_A`" | yes. `T_A = 1 + k_A`, so `T_A − t_B = k_A`. The ticks after `t_B` are iterates of `φ`, so `G_B = G_φ` and `d_{G_B}` is Main's `d` |
| `⊥ ↦ +1` | "If the protocol records a `±1` outcome in every run" | yes. No `⊥` occurs, so the rule is vacuous |
| (MI) | (iv) "`p(Ω∣a,b)=p(Ω)`", with `Ω` "a pre-setting variable that fixes each wing's response to every setting" | yes; the same condition |

So Main's theorem is the case of A6.1 with one setting tick followed by iterates of one fixed `φ` (P5-A61(4)).
- **Why `G_B` excludes the setting tick's edges.** If (R) were measured in one graph containing the setting tick's
  edges, it could fail where Main's (iii) holds. P5-A61(5) gives an instance with `d_φ(B, R_A) = ∞` and
  single-graph distance `2 ≤ k = 2`, in which the readout does not depend on `b`.

*Scope.* A6.1 needs (D), (L′), (R) with the `⊥` rule, and (MI). It says nothing about:
- constructions in which some tick's map outside a wing's region depends on that wing's setting;
- constructions with a `G_B`-path from `B` to `R_A` no longer than `T_A − t_B` (R6.7's preparation-indexed long edges
  are an instance);
- measurement dependence;
- coincidence-only statistics.

**Consequence for the ablations.** Consider constructions satisfying (D), (L′), (R) and (MI). In them, none of the
following can be credited with `|S| > 2`:
- construction B's access restrictions;
- state restrictions on a setting-independent ensemble;
- own-wing local operations, Obligation C's included;
- local registration rules.

This is narrower than "observational-incompleteness principles cannot give Bell violation". R6.7 is itself a
candidate OI principle (H-Bell), and A6.1 does not cover it.

**A6.2. Obligation C: necessary for QM-matching settings with stabilizer pair states when settings are identified as
local read directions, and not sufficient (under A6.1's hypotheses, including the design assumptions (L′) and (R)).**
- *Necessary, qualified.* Suppose settings are identified as local read directions (an L-CAL-type identification),
  the pair state is a stabilizer state, and local operations are Clifford-class. Then QM itself gives `|S| ≤ 2` (§2).
  A construction exceeding 2 there would disagree with QM. A non-stabilizer pair state with Pauli settings reaches
  `2√2`, so with such a source (R6.5) the requirement moves from the settings to the source.
- *Not sufficient.* Own-wing operations do not exceed 2 under A6.1's hypotheses.
- *Not needed for raw first-read correlations.* The shared-parity candidate reaches `S = 4(1 − 2η)` with abstract
  settings and no coherent operation (W).
- *For #1210.* "QX-6 blocked on QX-1" captures the setting requirement in the stabilizer-pair case. The binding
  prerequisites, each with its basis, are R6.5, which the protocol presupposes (§1); R6.7, necessary for `|S| > 2`
  under (D) and (MI), with the `⊥` rule, as a cross-wing response, and in H-Bell's form given (L′), separation in the
  designed reference graph and (R)'s readout clause (SHARED Q6-P12); and R6.8, a condition of Level-2 credit (§9).

**A6.3. Probabilities are rational.**
- N2 counting gives rational laws (dyadic at `q = 2` without conditioning), so `S = 2√2` and the correlators `±1/√2`
  are unreachable exactly, though approachable within `ε`.
- The rational comparator `S = 5/2` (at `π/3` angles) is exact and lies on the TLM boundary.
- C-EXPOSURE's R60 type gives `π/3`-grid local settings only if its rotation axis is orthogonal to the read plane.
  That is not computed here.

**A6.4. The supply restriction and no-signalling: a requirement, not a result.**
- Under (D) and (MI), with the `⊥` rule, `|S| > 2` with complete-history no-signalling needs an admitted preparation
  class whose affine hull excludes the point mass at some `Ω` in the support (SHARED Q6-P12 [A]). By
  prepared-pair-source §§4–5 (W; open, SHARED Q6-O8), a parameter-dependent deterministic completion is no-signalling
  only over preparation laws in the kernel of its balance map, and over an unrestricted class it is pointwise local.
- If construction B supplies R6.7 and is to meet Level 2's no-signalling target (§9), R6.9 must therefore be a state
  restriction of that kind. N2 and SA-1(c) are the only state restrictions in the present toolkit, and neither is
  shown to mask.
- A preparation class defined only as the kernel of the balance map is fitted to no-signalling. It would be
  creditable only if fixed in advance by a principle that has a reason independent of no-signalling and of agreement
  with QM, and a consequence of its own (§A.29; SHARED §9).
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
  and records. Expected `|S| ≤ 2`, a consequence of Main §3.3 (P) for one-step settings under its hypotheses, and of
  A6.1 [A] for multi-tick ones under A6.1's hypotheses ((D), (MI), and the design assumptions (L′) and (R)).
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
| ABL-NL: R6.7 removed | dynamics | `|S| ≤ 2` (A6.1, under its hypotheses, including the design assumptions (L′) and (R)). `pred_change` is true if `B_6-nl` exceeded 2 |
| ABL-SA1c / ABL-N2: sharp or non-uniform supply | state restriction; credit none | signals iff the supply leaves the kernel of the balance map (A6.4). Not predicted |
| ABL-ACC: a wing's access map widened | access | if no-signalling then fails, the balance was an access artefact. "Unread" fields may not be declared private (W). `access_only` true |
| ABL-ACC-narrow: access narrowed | access | no-signalling obtained this way is not creditable (NO-SIGNALLING.md item 5 (W)) |
| ABL-BOT: `⊥` rule varied (`⊥ ↦ +1` against `⊥ ↦ −1`) or coincidence-only | protocol | A6.1 holds for either of the first two, with `⊥ ↦ +1` in (R) replaced by that fixed local rule: the proof is unchanged, since steps 5–6 use only that each outcome is a function of its readout region. Coincidence-only is the detection loophole and is reported, never credited |
| ABL-MI: settings correlated with `Ω` | breaks (MI) | bounded by Main:421; reported, not adopted |
| ABL-C: C's local operation replaced by a Clifford-class one | dynamics (local) | QM-matching correlators are lost at identified settings with a stabilizer pair state (A6.2) |
| ABL-REUSE: a second round on the same pair | protocol | tests R6.8 and R6.11 |

## 7. Dependence on Q-C2-1's outcomes, and dependencies Q-C2-1 does not cover (decision tree)

```
Bell-specific prerequisites, independent of every Q-C2-1 token:
  R6.5 pair source (presupposed by the protocol), R6.7 cross-wing response (H-Bell), R6.8 history
  no-signalling, R6.10 Tsirelson.
  R6.5 or R6.7 missing → QX-6 is limited to A_6 / B_6-loc (|S| ≤ 2 by Main §3.3 and A6.1, under their
                         hypotheses) plus benchmark arms.
  R6.8 missing ────────── no Level-2 credit (§9); an excess over 2 is reported, not credited.
  R6.10 missing ───────── no Level-3 credit (§9); Level 2 does not require it.

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
2. **Local constructions are capped.** Under Main §3.3 (one-step settings) and A6.1 (multi-tick local settings under
   A6.1's hypotheses ((D), (MI), and the design assumptions (L′) and (R)), [A]), with the `⊥` rule, `|S| ≤ 2`.
   - Under (D) and (MI), with the `⊥` rule, a Bell excess needs a cross-wing response; given (L′), separation in the
     designed reference graph and (R)'s readout clause it needs one through an edge outside that graph, which is R6.7
     (H-Bell), open (SHARED Q6-P12).
   - The ROADMAP records H-Bell as downstream of an unmet curvature re-founding obligation (`verification/ROADMAP.md`
     :974-979 at `fd539e15`, quoted in HB-1 under its earlier line numbers 764-769).
3. **Reuse signalling.** The only explicit nonlocal candidate on record signals on reuse at every calibration (W).
4. **Preparation-class restriction.**
   - For Level 2, under (D) and (MI), with the `⊥` rule, `|S| > 2` with complete-history no-signalling needs an
     admitted class whose affine hull excludes some point mass (A6.4 [A]). Prepared-pair-source states this as a
     kernel condition on the balance map (W; open, SHARED Q6-O8).
   - For Level 3, the admitted class must also exclude PR-type sources (R6.10, a hypothesis under test).
   - No principle is known that bounds `S` at `2√2`.
5. **Calibration as import.** Matching `2√2` by choosing `η*` is IQ (W). Rational N2 laws cannot reach it exactly
   (A6.3).
6. **Settings.** QM-matching local settings with stabilizer pair states need Obligation C when settings are
   identified as local read directions, since Clifford-class local operations then give `|S| ≤ 2` in QM itself
   (A6.2). Measurement independence is posited (Main:406-412).
7. **P3 against FIX.** Per-tick arming as the setting switch is in tension with one fixed law (OICORE-1 §2;
   `DESIGN-DS.md` §2 [D]). A6.1 admits it only for edges with both ends inside one wing's region.
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
- **Q6-4.** What is HB-1's relation to QX-6 (#1060's frozen legacy H-Bell shape round)?
  - (a) Cite it as provenance.
  - (b) Make it a prerequisite.
- **Q6-5.** Which local `⊥` rule applies?
  - (a) `⊥ ↦ +1`.
  - (b) Another fixed local rule, declared before any run.

## 11. References to content off `main` (§A.42 item 8), traced one by one

| reference | claim it is attached to | classification |
| --- | --- | --- |
| #1210 c.6736966265 | §0 scope | provenance (authority) |
| #1169 c.6734304025, c.6734374076 | the A/B arms; ablation fields | owner records of direction; quoted in the programme |
| #1169 c.6735014875 (D15(a), D18(a) conditional) | §5; §7 | owner decision; quoted in QX-3 §0 |
| #1060 (HB-1's accountable Issue) | Q6-4 | provenance |
| Main:22, :56, :362-429, :652; Substratum:131, :467, :481; Methodology:393; book ch01:173, ch04:124 | §3; A6.1's base theorem | on `main` (P) |
| `verification/ROADMAP.md`:974-979 at `fd539e15` | §8 item 2 | on `main` (a frozen record) |
| `oi-qm-ext-1/two-system-interface.md`, `prepared-pair-source.md`; `correlation-recombination-20261107/NO-SIGNALLING.md` | §3; A6.2; A6.4; §8 | on `main` (W); not established premises (§A.46 item 7) |
| M2D Theorems U2 and NC | §3; §8 item 8 | on `main` (W), conditional |
| `round-comp-1-composite-interface/result.md` | §3.1 | on `main`; native round, kernel |
| `h-bell/round-hb-1-obligation-shape/preregistration.md` | §3; §8 item 2 | on `main` (frozen control plane) |
| `oicore/OICORE-1.md` §2 (FIX) | §8 item 7 | off `main` (D) |
| Q-C2-1 r13 drafts (`DESIGN-DS.md` §2; tokens; cone and Lemma P reviews; NR-11) | §§5, 7, 8 | off `main` (D) |
| `review/REVIEW-PHASE1.md`; probe `review/probes/p1_chsh_stabilizer.py` (`af34edb8…`) | §2: the stabilizer bound's confirmation, the triangle-graph contradiction, `S = 5/2` on the TLM boundary | off `main` (D); an exact finite computation on generic stabilizer objects |
| `review/REVIEW-PHASE1-r2.md` (`47af406f…`); probe `review/probes/p4_r2_checks.py` (`2e7c2de9…`) | A6.1: the counterexample P4(1) to the hypothesis set without (L′); §2 GHZ-1's values | off `main` (D); exact finite computations on generic objects |
| writer's probes `review/probes/p5_r3_a61.py`, `p5_r3_ghz.py` | A6.1's checks and Main instance; §2 GHZ-1 and GHZ-2 values, local maxima, `X/Z` content of GHZ-1, the local-Clifford map | off `main` (D); exact. A6.1's random-construction check is a finite sample, not a proof |
| M2D:65-71, :483-497, :509-516 | §3 Theorem NC and Corollary NC-B | on `main` (W), conditional |
| `review/REVIEW-PHASE1-r3.md` (`448614ea…`); reviewer probes `review/probes/p6_r3rev_a61.py`, `p6_r3rev_ghz_chsh.py` | A6.1's independent review and checks; §2's GHZ and CHSH values | off `main` (D); exact checks on generic objects |
| SHARED Q6-P12 (this programme); writer's probe `review/probes/p11_r6_checks.py` (3)–(4); `review/REVIEW-PHASE1-r6.md` (`86b69048…`) with reviewer probe `review/probes/p12_r6rev_checks.py` (4) | §3.2; A6.2; A6.4; §8 items 2 and 4 | off `main` (A in SHARED; D for the review; exact checks on generic response tables and graphs; each probe imports no earlier one) |
| #1210 c.6738866690 (amaybaum, 2026-11-09T11:25:06Z), decision O2 | Q6-5's identifier | owner decision, quoted: "Use **Q6-5** as the new unique identifier for the **⊥-rule** question" |
| CHSH 1969; Cirel'son 1980; Landau 1987, 1988; Masanes 2003; Valentini 2002; Fine 1982 | §§1–3 | literature, not read first-hand |
