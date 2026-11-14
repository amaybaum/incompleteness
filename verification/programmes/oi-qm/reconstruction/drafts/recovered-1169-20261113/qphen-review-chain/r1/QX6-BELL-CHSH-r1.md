# QX-6: entanglement and Bell (CHSH), with complete-history no-signalling — Phase 1 experiment specification (draft)

## 0. Standing

Standing, snapshot (`origin/main` = `fd539e15`), evidence layers and requirement types are as in
`QX3-ANTIBUNCHING.md` §0. This is paper only, model-written and awaiting independent review. No mechanism is built, no
computation is run and no acceptance criterion is frozen (#1210 c.6736966265).

***

## 1. The phenomenon and its operational observables

**Phenomenon.** A source prepares two systems that are sent to two wings, `A` and `B`. Each wing chooses a setting
(`x`, `y ∈ {0, 1}`) and records an outcome (`a`, `b ∈ {±1}`). Quantum correlations exceed the local bound,
`|S| ≤ 2`, where `S = E₀₀ + E₀₁ + E₁₀ − E₁₁` (Clauser, Horne, Shimony and Holt, PRL 23, 880 (1969); L). They stay
within Tsirelson's bound `2√2` (Cirel'son, Lett. Math. Phys. 4, 93 (1980); L). Neither wing's accessible history
depends on the other wing's setting.

**Observer access.** Each wing is a separate observer with its own access map. That map covers:
- its own setting record;
- its own outcome records;
- the herald and preparation-status records, where a herald exists;
- its own apparatus records.

The other wing's setting, the source registers and every hidden cell are not registered (L-ACC per wing). Joint
statistics are formed only after the records are brought together, which is ordinary communication outside the
isolated stage.

**Observables.**
- `P(a, b | x, y)`, with full-mass accounting. A failure outcome `⊥` is kept in the law, and failure mass is not
  renormalized away. This follows the two-system interface record's rule (W).
- `E_xy` and `S`.
- **Complete-history no-signalling.** The law of `B`'s whole accessible history at fixed `y` is the same for every
  `x`, and symmetrically for `A`. The history includes repeated reads, timing, failures and apparatus records, not
  only the first outcome (NO-SIGNALLING.md §1 item 2 (W); two-system interface §2 (W)). Equality of one-read marginals
  is insufficient.
- **Quantum-set membership** for unbiased correlators (TLM; Landau, Phys. Lett. A 120, 54 (1987); L):
  `|E₀₀E₀₁ − E₁₀E₁₁| ≤ √((1−E₀₀²)(1−E₀₁²)) + √((1−E₁₀²)(1−E₁₁²))`, with marginal-bias corrections where needed.
  With rational `E` this can be decided exactly by squaring with sign tracking. No floating-point certification is
  used.
- **Reuse.** A second round on the same pair, as in the two-system interface record §4 (W). It checks repeatability
  and the history-level no-signalling.

**Validation layer**, from the construction:
- the coupling-graph distance between each wing's setting region and the other wing's readout region (Main §3.3's
  cone lemma);
- whether the setting generators are independent of the response-relevant pre-setting variable `Ω`, that is,
  measurement independence (iv);
- the ontic response functions `q_x(Ω)` and `r_y(Ω, x)`, and whether `r` depends on `x` (ontic parameter dependence);
- the preparation-law class over which no-signalling holds.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM's predictions** (comparators; IQ):
- `|Φ⁺⟩` with `A₀ = Z`, `A₁ = X` and `B_{0,1} = (Z ± X)/√2` gives `E_xy = (−1)^{xy}/√2`, `S = 2√2`, and fair
  marginals. No-signalling holds exactly, and so does repeatability under the local Lüders instruments (two-system
  interface eq. (1) (W)).
- **A rational-angle comparator.** With measurement angles at multiples of `π/3` (settings `0` and `2π/3`
  against `±π/3`) and `E = cos(θ_A − θ_B)`, the correlators are `1/2, 1/2, 1/2, −1`, so `S = 5/2`.
- **Stabilizer settings** [A, unreviewed; standard]. For any stabilizer state with Pauli settings, `|S| ≤ 2`.
  - Each correlator is `±1` or `0`.
  - Suppose `A₀, A₁` anticommute and `B₀, B₁` anticommute. Then `A₀B₀` and `A₀B₁` cannot both be stabilizer
    elements, because their product `I ⊗ B₀B₁` is anti-Hermitian. So at most two of the four correlators are
    nonzero.
  - If either pair commutes, the inequality reduces to a trivial case.
  - **Consequence.** A QM-matching excess over 2 needs non-Pauli local settings or a non-stabilizer state. For a single
    qubit per wing this means non-Clifford local operations (MC).

**The witnesses and the classes each one excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| `|S| > 2`, with a `±1` outcome recorded in every run (full mass) and setting-independent `Ω` | local hidden-variable models with measurement independence: every response-complete deterministic completion that satisfies Main §3.3's (ii)–(iv) (Main §3.3 Theorem [P; exhaustive check 11]) | ontically parameter-dependent deterministic models: Bohmian mechanics, and OI's chosen branch (a); measurement-dependent models with `I_ont ≥ 0.0309` bits (Main §3.3(b)); retrocausal models; detection-loophole models if mass is renormalized; signalling models, which the next row excludes separately |
| complete-history no-signalling | models that signal across the isolated stage, for example the shared-parity candidate on reuse (two-system interface §4, eq. (10) (W)) | local models; QM; Popescu–Rohrlich boxes; non-equilibrium-masked nonlocal models whose restricted preparation class balances the histories |
| `|S| ≤ 2√2` (exact TLM membership) | supra-quantum no-signalling correlations. OI's unrestricted response-table construction realizes the PR law (Main §3.3 [P]), so this witness has teeth | — (an upper-bound check, not a nonclassicality witness) |
| GHZ / Mermin (optional; three wings) | local hidden variables, without inequalities | the same as the first row. It needs `Y`-type reads (the `Z₄` phase group: Coecke, Edwards and Spekkens, ENTCS 270, 15 (2011); abstract read), which the native toolkit lacks (`{0, π}` phases; AP1 type grading excludes a `Y` read) |

## 3. What OI's corpus already establishes about Bell (§A.19)

- **The Bell ceiling for a screened local completion** (Main §3.3, Theorem, Main:366-393; P, with the pointwise bound
  checked exhaustively). Take a deterministic completion with:
  - one-step own-wing read/write setting interventions (ii);
  - readouts outside the remote setting's graph cone, with a `±1` outcome in every run (iii);
  - a setting-independent ensemble (iv).

  It is Bell-local, with `|S| ≤ 2`. Its cone lemma uses the coupling graph read from `φ`, not the nearest-neighbour
  stipulation.
- **OI's chosen branch is ontic parameter dependence**, with operational no-signalling required (Main §3.3(a);
  Main:22; Substratum:467; Methodology:393).
  - Measurement independence is kept as a posit about the initial condition, not derived (Main:406-412).
  - Measurement dependence is recorded and not adopted, with the bound
    `S ≤ min{4, 2 + 4√(2 ln 2 · I_ont)}` (Main:421).
- **Corollary.** The reference nearest-neighbour cubic graph alone is Bell-local for wings outside its cone
  (Main:416). The proposed escape is **preparation-indexed adjacency**: bounded-degree, Bell-relevant long edges, or
  an equivalent nonlocal response map, supplied by an entangling preparation. Whether it supplies parameter dependence
  with operational no-signalling and the continuum-curvature limit is the open hypothesis **H-Bell** (Substratum:131;
  Main:416).
- **Bare representability is too broad.** Globally coupled setting-dependent hidden dynamics realizes PR-box behaviour
  (Main:362). "The selector in a Bell experiment is therefore causal locality, not representability." Tsirelson's
  `2√2` is attached to the cited stochastic causal-local indivisible layer, not to OI's deterministic completion
  (Substratum:481; book ch01:173, ch04:124). C1–C4 and graph locality do not enforce Tsirelson.
- **Records on `main`** (W; model-reviewed; none is an established premise):
  - `oi-qm-ext-1/two-system-interface.md`. A shared-parity reversible candidate matches all four first-read quantum
    correlations only at a calibrated source parameter `η* = (1 − 1/√2)/2`, "an exact calibration, not a derivation".
    It needs a cross-wing controlled interaction, which gives up graph-cone isolation. On reuse it signals: Bob's
    two-round history depends on Alice's settings, at every `η` and at `h > 0`. Its source class admits PR behaviour at
    `η = 0`.
  - `oi-qm-ext-1/prepared-pair-source.md`. The source gate stops: no physical pair dynamics or preparation is
    specified. For a fixed deterministic realization, complete-history no-signalling is a set of linear balance
    equations on the preparation law. Requiring it over a preparation family whose affine hull is the whole simplex
    makes both wings' records pointwise local, so `|S| ≤ 2` (§§4–5).
  - `correlation-recombination-20261107/NO-SIGNALLING.md`. STOP: no physical experiment or interface is supplied. A
    Bell-local classical control "should pass no-signalling while obeying the classical Bell ceiling"; "passing
    no-signalling alone supplies no quantum distinction".
  - `round-comp-1-composite-interface/result.md` (native round, receipt holds). The composite interface carries local
    tomography as its single premise field. No-signalling on products holds without it. It sources no local tomography
    and does not identify the quantum composite.
  - `h-bell/round-hb-1-obligation-shape/preregistration.md`. A control plane only, with no result. It records
    (ROADMAP:764-769) that H-Bell is downstream of an unmet curvature re-founding obligation.
  - `mechanism-2-20261108/DESIGN.md` (M2D) §0 item 2. Both results are conditional on Lemma F's operation set and
    H-LIFT.
    - **Theorem U2.** Under the product frame R1^⊗n, every encoded unitary channel a fixed bijection at `q = 2`
      induces lies in `A_4 ≀ S_n`. That group holds local tetrahedral rotations and cell permutations, and contains
      "no encoded `S`, `T`, CNOT, CZ, `rot`, or any entangling unitary".
    - **Theorem NC.** Under an injective identification with spanning reads, the configuration model is noncontextual,
      and "With product encoded effects it gives CHSH ≤ 2". At `q = 2` spanning needs a `Y` read, which is not
      native.
    - **Consequence.** Within U2's scope, no native entangling operation exists to prepare a pair from product
      supplies. R6.5 must lie outside that scope: another frame, a failure of H-LIFT, or a pair supplied as a
      preparation.

### 3.1 Is there a separable observer structure?

**Partly.** What exists:
- the causal separation of spatially separated visible regions (Main §3.4(ii), Main:652), proved from the coupling
  graph;
- a typed composite interface whose product laws hold without local tomography (COMP-1, K);
- per-wing access maps, as supplied abstract restrictions (two-system interface §2 (W)).

What is not established:
- statistical product structure after conditioning, local tomography, and one common tensor-product instrument
  category (Main:652, verbatim: "It does not alone establish …");
- local tomography of any constructed composite (COMP-1);
- a native pair source (prepared-pair-source §2);
- a second observer as an embedded subsystem with its own registration through `φ`. Main's Definition has one
  observer `V`. The two-system interface states, for a third observer, that "No separate apparatus or access map is
  supplied".

QX-6 therefore needs two-observer access maps typed as CS (ACC per wing) and a pair source typed NX. Local tomography
is carried as a hypothesis, not a result.

### 3.2 Locality against OI's hidden sector

- OI's hidden sector `H = S ∖ V` is spatial wherever the substratum is. Its components obey the same cone lemma, so a
  shared hidden preparation is a common cause and cannot by itself exceed `|S| ≤ 2` under (ii)–(iv).
- Exceeding 2 under measurement independence needs the hidden response at one wing to depend on the remote setting
  within the run. That means a coupling path between the wings' hidden sectors shorter than the run: preparation-indexed
  long edges.
- That dependence must then be invisible in each wing's complete accessible history. By prepared-pair-source §5 (W),
  this cannot hold over an unrestricted preparation class. It needs a **restricted preparation class**: a state
  restriction on the hidden supply under which the nonlocal responses balance out.
  - This is the structural role played by quantum equilibrium in de Broglie–Bohm theory, where non-equilibrium
    distributions signal (Valentini, Phys. Lett. A 297, 273 (2002); L).
  - In OI the candidates for this role are N2 and SA-1(c)-type supply restrictions (A6.4).

## 4. What the experiment needs from an OI construction

| # | requirement | type | status |
| --- | --- | --- | --- |
| R6.1 | the step, N2 and the supplies | EN / CS | available (shared) |
| R6.2 | two wings: spatially separated regions with the cone lemma, and per-wing meters with terminal registration | EN (cone lemma, Main §3.3 P); CS (SA-1(b) per wing) | the cone lemma is proved. Per-wing apparatus exists only in single-system form |
| R6.3 | per-wing observer access maps (each wing's complete history) | CS (ACC-R2-type, per wing) | supplied abstractly only (two-system interface §2 (W)) |
| R6.4 | setting choice: own-wing, one-step interventions, independent of `Ω` | CS (P3 arming, in tension with FIX); measurement independence is a posit (Main:406-412) | P3 available; measurement independence is posited |
| R6.5 | a pair source: a setting-independent correlated preparation of two carriers | NX | **absent**: the source gate stops (prepared-pair-source §2 (W)) |
| R6.6 | local settings at non-Pauli directions, for QM-matching correlators at identified settings | MC | not available natively (`{0, π}`; A6.2) |
| R6.7 | **ontic parameter dependence**: a cross-wing response through preparation-indexed adjacency or an equivalent nonlocal map | CS as named open hypothesis H-Bell (dynamics type) | **open** (Substratum:131; Main:416). A Boolean specification exists in the two-system interface record, without a physical source, and fails on reuse |
| R6.8 | **complete-history no-signalling** across the isolated stage, including reuse | a constraint on R6.7 together with the preparation class | open. Fails for the shared-parity candidate (W) |
| R6.9 | a restricted preparation class that masks R6.7 in every wing's history | CS (state restriction: N2 / SA-1(c)-type) | open (A6.4) |
| R6.10 | Tsirelson soundness: no reachable preparation gives `|S| > 2√2` | constraint | open. The unrestricted class reaches PR (Main:362; two-system interface (W)) |
| R6.11 | post-measurement state update and repeatability on the measured pair, with no silent fresh source | CS / NX | open: "a physical state-update mechanism remains necessary" (two-system interface §4 (W)) |
| R6.12 | local tomography of the constructed composite | carried as a hypothesis (COMP-1 premise field) | not sourced |

**Paper derivations** (A; unreviewed).

**A6.1. Access-only and local principles cannot raise `|S|` above 2.**
- **Claim.** Construction B cannot exceed 2 while it keeps (ii)–(iv) and a `±1` outcome in every run, whatever it adds
  among:
  - access restrictions;
  - state restrictions on a setting-independent ensemble;
  - local coherent operations confined to each wing's region, Obligation C's included;
  - local registration rules.
- **Reason.** This is Main §3.3's theorem applied as stated. Its hypotheses do not mention these principles. An access
  restriction changes which local functions are read, and they remain local.
- **Consequence for the ablations.** No principle with `dynamics_credit` none can be credited with `|S| > 2`. A CHSH
  excess needs at least one of:
  - a dynamics-type principle that breaks (ii)/(iii), that is, ontic parameter dependence;
  - a breach of (iv), measurement dependence, not adopted (Main:421);
  - a breach of the every-run `±1` clause, which full-mass accounting forbids.
- **Scope.** This is the strongest structural statement QX-6 inherits, and it is an application of a result on
  `main`, not a new theorem.

**A6.2. Obligation C is necessary for QM-matching settings and not sufficient.**
- **Necessary.** With settings identified as local read directions (L-CAL-type identification) and Clifford-class
  local operations, QM itself predicts `|S| ≤ 2` (§2, stabilizer settings). A construction exceeding 2 at those
  settings would disagree with QM there.
- **Not sufficient.** By A6.1, local coherent operations do not exceed 2 without R6.7.
- **Not necessary for raw first-read correlations.** The shared-parity candidate reaches any `S = 4(1 − 2η)` with
  abstract settings and no coherent operation, through hidden-noise calibration (W).
- **Consequence for #1210.** The dependency "QX-6 blocked on QX-1" captures the setting requirement. The binding
  prerequisites are R6.5, R6.7 and R6.8.

**A6.3. Probabilities are rational.** N2 counting gives dyadic laws. `S = 2√2` and the correlators `±1/√2` are
unreachable exactly, though approachable within `ε`. The rational QM comparator at `π/3` angles (`S = 5/2`) is exact.
Combining C-EXPOSURE's R60 type with the octahedral group yields `π/3`-grid local settings only if the rotation axis is
orthogonal to the read plane; that is not computed here.

**A6.4. The supply restriction carries no-signalling, and its ablation predicts signalling.**
- By prepared-pair-source §5 (W), a parameter-dependent deterministic completion is no-signalling only over a
  restricted preparation class. If construction B's restriction is an N2 / SA-1(c)-type supply restriction, then
  ABL-SA1c and ABL-N2 replace it with a sharper or non-uniform supply. They are predicted to produce signalling in a
  wing's history: `pred_change` true, while `dynamics_credit` remains none.
- This is a consequence beyond the Bell target: a hard-to-vary corollary in the §A.29 sense, if the restriction is
  fixed in advance. Non-equilibrium supplies signal.
- It is stated as a requirement any QX-6 construction B must meet, not as a result.

## 5. Reuse of the single shared construction

**Shared with every QX:**
- the step;
- N2 and the supply restrictions;
- SA-1(b) meters;
- P3 arming, or its FIX-compatible replacement;
- the typed identifications.

**Shared with QX-1, QX-4c and QX-7.** The local non-Clifford operation that sets the read directions (R6.6), which is
Obligation C's operation. A QX-6-specific local gate is not admissible.

**Shared with QX-3's W3 and Q-C2-1's NR-11:**
- two systems and a composite;
- the pair source;
- local tomography as a hypothesis.

**Specific to QX-6:**
- R6.7, a cross-wing response;
- R6.8 and R6.10, the history balance and the Tsirelson bound;
- the per-wing access maps.

**Flagged experiment-specific quantum assumptions** (IQ, benchmark only):
- the calibrated source parameter `η*`, selected from the QM comparator (two-system interface eq. (5) (W));
- any supplied entangled pair law;
- local Lüders instruments imported for the continuation.

## 6. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_6`.** Two wings under the reference nearest-neighbour substratum, with B's scaffolding needed for settings and
  records. The expectation is `|S| ≤ 2`. This is not a prediction to be tested but a consequence of Main §3.3 (P).
- **`B_6-loc`.** Construction B with every single-system principle and C's local operation, and no cross-wing
  response. The expectation is `|S| ≤ 2` (A6.1). It shows that observational incompleteness principles alone do not
  give Bell violation.
- **`B_6-nl`.** `B_6-loc` plus R6.7 (H-Bell-type response) and R6.9 (the supply restriction). The open question is
  `|S| > 2` with complete-history no-signalling, reuse included, and `|S| ≤ 2√2`. No value is predicted.
- **Benchmark (IQ, labelled).** The shared-parity candidate at `η*`, or a supplied `|Φ⁺⟩` law.
- **Comparators** (gating nothing):
  - LHV-6: a Bell-local shared variable with independent settings, `|S| ≤ 2`, no-signalling;
  - PR-6: the unrestricted response table, `S = 4`, no-signalling first read (Main:362);
  - SIG-6: the shared-parity reuse, which signals (W);
  - QM-6: `S = 2√2`, and `5/2` at the rational settings.

**Candidate ablations.** Each reports `pred_change`, `mech_change` and `access_only`.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-NL: R6.7 removed | dynamics | `|S| ≤ 2` (A6.1). `pred_change` true if `B_6-nl` exceeded 2 |
| ABL-SA1c / ABL-N2: a sharp or non-uniform supply | state restriction; credit none | no-signalling expected to fail (A6.4) |
| ABL-ACC: a wing's access map widened, for example to read its own apparatus's full records | access | if no-signalling then fails, the balance was an access artefact. "Unread" fields may not be declared private (two-system interface §2 (W)). `access_only` true |
| ABL-ACC-narrow: access narrowed | access | no-signalling may appear by dropping records. This is not creditable, since NO-SIGNALLING.md item 5 forbids dropping accessible records |
| ABL-MI: settings correlated with `Ω` | breaks (iv) | `S` bounded by Main:421. Reported, not adopted |
| ABL-C: C's local operation replaced by a Clifford-class one | dynamics (local) | QM-matching correlators lost at identified settings (A6.2) |
| ABL-REUSE: second round on the same pair | protocol | tests R6.8 and R6.11 |

## 7. Dependence on Q-C2-1's outcomes, and the dependencies Q-C2-1 does not cover (decision tree)

```
Bell-specific prerequisites, independent of every Q-C2-1 token:
  R6.5 pair source, R6.7 ontic parameter dependence (H-Bell), R6.8 history no-signalling, R6.10 Tsirelson.
  If any is missing → QX-6 is limited to A_6 / B_6-loc (|S| ≤ 2 by Main §3.3) plus benchmark arms.

Q-C2-1 C token (governs R6.6, the local settings)
├─ C-EXPOSURE, R60 type (STAB true) ── π/3-grid local settings candidate. The QM comparator is S = 5/2. They are
│                          usable only if the axis is orthogonal to the read plane (A6.3), and only inside B_6-nl.
├─ C-EXPOSURE, S_3 type ── improper. No rotation of read directions. R6.6 stays open.
├─ C-EXPOSURE, STAB false ── an irrational-angle rotation (e.g. arccos(3/5)) gives other rational S comparators.
├─ C-SIZE-DEPENDENT ─────── local settings need 1–2 applications per run. Usable under the same conditions.
├─ C-NONSTABILIZER ──────── non-stabilizer local states, no non-Clifford operation. A QM-matching excess at fixed
│                          Pauli reads would need non-stabilizer pair states, which needs R6.5 anyway.
├─ C-SURVIVAL ───────────── R6.6 unavailable natively. QM-matching settings are benchmark-only. A6.1 is unaffected:
│                          B_6-loc is still ≤ 2.
└─ C-VOID ───────────────── no reading.

Q-C2-1 P token
├─ P-COMPLEMENTARITY ──── the per-wing meters and backaction are validated (needed for R6.11's continuation).
└─ otherwise ───────────── per-wing apparatus validation is missing. QX-6 waits on it, whatever the C token.

Q-C2-1 B token and D15 typing → the per-wing access maps (R6.3) take the same owner typing. A B-CONTEXTUAL fragment
does not transfer to the two-wing fragment.

Q-C2-1 A/B readings → if SA-1(c) carries the universality reading in P, A6.4 makes the same restriction a candidate
for R6.9. That is a shared-mechanism economy, still to be tested.
```

## 8. Known feasibility obstacles

1. **Two-system structure.** There is no native pair source (R6.5), no constructed composite with local tomography
   (R6.12), and no embedded second observer. Main's Definition has one `V` (§3.1).
2. **Main §3.3's theorem.** Every construction satisfying (ii)–(iv) with full mass gives `|S| ≤ 2` (A6.1). A Bell
   excess needs a cross-wing dynamics principle, R6.7, which is H-Bell. H-Bell is open, and it is recorded as
   downstream of an unmet curvature re-founding obligation (ROADMAP:764-769, quoted in HB-1).
3. **Reuse signalling.** The only explicit nonlocal candidate on record signals on reuse at every calibration (W). A
   successor must supply an interaction-derived post-measurement state whose whole local histories stay independent of
   remote choices (two-system interface §6).
4. **Preparation-class restriction** (A6.4; prepared-pair-source §5 (W)). No-signalling needs a restricted supply
   class. That class must also exclude PR-type sources (R6.10), and no principle is known to bound `S` at `2√2`.
5. **Calibration as import.** Matching `2√2` by choosing `η*` from the comparator is IQ (W). Rational N2 laws cannot
   reach it exactly (A6.3).
6. **Settings.** QM-matching local settings need Obligation C (A6.2), and the measurement-independence posit
   (Main:406-412) has to be supplied.
7. **P3 against FIX.** Setting choice through per-tick arming is in tension with one fixed law (OICORE-1 §2;
   `DESIGN-DS.md` §2 [D]).
8. **No native entangling operation within U2's scope** (M2D Theorem U2 (W), conditional on R1^⊗n, Lemma F and
   H-LIFT). A pair source must come from outside that scope (§3).
9. **Access artefacts.** Narrowing a wing's access can manufacture no-signalling. ABL-ACC-narrow is not creditable, and
   `access_only` must be printed (NO-SIGNALLING.md item 5 (W)).

## 9. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.** Quantum-compatible two-wing correlations with complete-history no-signalling, at `|S| ≤ 2`. `B_6-loc`
  can reach this.
- **Level 2.** `|S| > 2` with full mass, measurement independence and complete-history no-signalling, reuse included.
  - This excludes local hidden-variable models with measurement independence.
  - It is printed with "it does not exclude ontically parameter-dependent deterministic models, of which this
    construction is one".
  - It needs `B_6-nl`.
- **Level 3.** R6.7 and R6.6 are generated natively, not calibrated. The supply restriction R6.9 is fixed in advance
  (§A.29), and Tsirelson soundness holds over the admitted preparation class.
- **Level 4.** Repeated rounds and local instruments composed under one rule. Not addressed.

## 10. Owner questions (neutral)

- **Q6-1.** Which items are QX-6's prerequisites in #1210's table? (a) Keep "blocked: QX-1" as recorded. (b) Add
  "H-Bell (R6.7), pair source (R6.5), complete-history no-signalling (R6.8)" beside QX-1 (A6.2).
- **Q6-2.** How is R6.7 typed? (a) CS (named open hypothesis H-Bell, dynamics). (b) NX until a physical source is
  specified.
- **Q6-3.** Does QX-6 include the reuse round (R6.11) in its no-signalling test? (a) Yes. (b) First round only, with
  the limitation printed.
- **Q6-4.** Should QX-6 be coordinated with #1060's frozen legacy H-Bell shape round (HB-1)? (a) Cite it as provenance.
  (b) Make it a prerequisite.

## 11. References to content off `main` (§A.42 item 8)

| reference | claim | classification |
| --- | --- | --- |
| Main §3.3 (Main:360-429), §3.4(ii) (Main:652); Substratum:131, :467, :481 | §3; A6.1 | on `main` (P) |
| `oi-qm-ext-1/two-system-interface.md`, `prepared-pair-source.md`; `correlation-recombination-20261107/NO-SIGNALLING.md` | §3; A6.2; A6.4; §8 | on `main` (W), model-reviewed, not established premises (§A.46 item 7) |
| `mechanism-2-20261108/DESIGN.md` (M2D) Theorems U2 and NC | §3; §8 item 8 | on `main` (W), conditional on its stated hypotheses |
| `round-comp-1-composite-interface/result.md` | §3.1 | on `main`; native round, kernel |
| `h-bell/round-hb-1-obligation-shape/preregistration.md`; ROADMAP:764-769 | §8 item 2 | on `main` (a frozen control plane; ROADMAP is frozen) |
| Q-C2-1 r13 drafts | §7 | off `main` (D) |
| CHSH 1969; Cirel'son 1980; Landau 1987; Valentini 2002; Coecke–Edwards–Spekkens 2011 | §§1–3 | literature. The Coecke–Edwards–Spekkens abstract was read; the others were not read first-hand |
