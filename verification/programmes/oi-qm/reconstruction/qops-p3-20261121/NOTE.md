# QOPS-P3: the next minimal native-mechanism test

**Standing. WIP / UNVERIFIED.** Writer's design record under `PLAN.md`, which was committed first
at `ba2f83a2`. It contains paper proofs and design only, and it has not been independently
reviewed. It runs no computation and adopts no premise. The test is in `PREREG.md` as rules only.

- **Authorization.**
  [#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306)
  (Group B, at design level).
- **Goal link.** The goal link is the one stated in `PLAN.md`.
- **Base.** The base is #1501 at `cd3672fa` (`P2`). Line numbers are at `main` `df6da1c6` unless
  stated otherwise.
- **Inputs used, at their reviewed standing.** They are cited and not redone:
  - OPRES (#1511 `7669e511`, `OP`): the classes `𝒩` and `𝒩⁺`, Lemma C, Theorem C and CC-1;
  - I3-SOURCE (#1508 `df520f3b`): S1;
  - P2's P4, P5 and J1.
- **R-READ is unresolved** (READOUT-ALG, #1513). No result below assumes either answer.

**Imports and inputs.**
- From P2: KIN, FLOW, READ, RES, PROD and FB.
- New here: **CTRL**, the selective application of a chosen native gate at a chosen time. This is
  the supplied control of QS H-QOPS-C, NU's question for the native form.
- **FLOW₁** is FLOW restricted to one native gate at one time: `unit g (1/2)` for one
  involution `g`.

***

## 0. Answers

1. **Q1, how the obligations relate. ESTABLISHED (Proposition Q-ind).** In one model, three
   obligations are mutually independent:
   - a non-MIO element;
   - a non-DIO element;
   - a ready-cell source.

   Theorem C allows the first two to be met by one element, but establishing one does not
   establish the other. No element of either kind supplies ready cells beyond the reservoir
   deficit. No ready-cell source is either kind of element.
2. **Q2, the smallest candidate. ESTABLISHED, in Q2's order.**
   - *O1:* **H-F1**, the executable half-flow `unit S_m (1/2)` of the single native swap gate at
     one site. It is one element outside `𝒩`, with support on one site and at one time, and it
     is both non-MIO and non-DIO.
   - *O3, in the same model:* **H-RC**. Ready cells are background cells of the uniform
     background (RES), used through a native shear-gate copy. By Lemma P6, each copy geometry
     needs exactly one pinned non-background *catalyst* cell, which is read and never written.
   - The only candidate that could tie H-F1 is a native readout outside the configuration
     algebra, if READOUT-ALG finds one (§2.3). It would then be a native element, not a
     hypothesis.
3. **Q3, the test. Designed (`PREREG.md`): T-WP, the native which-path interferometer.**
   - Its arms are built from whatever creators and detectors are available, so it is useful
     under either answer to R-READ.
   - It has three classical countercontrols. The diagonal shadow (CC-Δ) and the noninvasive
     memoryful simulator (CC-M) must each fail on a non-classical arm. OI's own invasive
     intervention dilation (CC-OI) must succeed, which marks the test's scope.
4. **Productivity (`PLAN.md`): INCONCLUSIVE.**
   - Criterion (i) holds.
   - Criterion (iii) holds: CC-M fails on a preregistered branch.
   - Criterion (ii) depends on R-READ. If R-READ holds, the only arm is FLOW × FLOW, whose
     outcome is derived here by hand (§3.2), so every branch is fixed. If READOUT-ALG finds a
     native readout outside the configuration algebra, the readout arms have outcomes that no
     known theorem fixes.
   - The missing input is READOUT-ALG's verdict.

***

## 1. Q1: three independent obligations

**Proposition Q-ind [W].** Take model M of P2 §4, with OPRES's class `𝒩` as the native operations.
1. *Ready-cell sources are neither creators nor detectors.* (N as algebra, with (I) on KIN for
   the matrix reading.) A ready-cell source appends configuration states or diagonal mixtures
   (`OP` (n2)). By OPRES Lemma C it is MIO-type and DIO-type, so it discharges neither half of O1.
2. *Creators and detectors are not ready-cell sources.* ((I): KIN, PROD, with a finite
   environment.) Let `U` be any unitary on register ⊗ environment, for instance a non-monomial
   flow, starting from a product state. By P5(2), the register entropy removed is at most
   `log|H| − S(σ)` for every `U`, monomial or not. A non-MIO or non-DIO unitary element therefore
   adds no ready cells beyond the deficit RES already holds.
   - A non-DIO *measurement* can lower the register's conditional entropy only by conditioning on
     its record, whose cost is `log₂ 1/μ(E)` (PR1).
   - Initial correlation, `+I(X:H)₀`, is outside P5's scope (P2 §2).
3. *The two halves of O1 are distinct.* (I), as in OPRES. MIO and DIO are different properties
   (`OP` §2). CC-1 meets them with two elements, a `|+⟩` ancilla and a destructive `⟨±|`
   readout, the first MIO-violating and DIO-type, the second DIO-violating and MIO-type. A
   non-monomial unitary meets both with one element (`OP` §4 table, row FLOW).

*Proof.* Items 1 and 3 are OPRES Lemma C and its route table. Item 2 is P5(2), which uses only
unitarity and a product initial state. ∎

*Consequence.* No single mechanism discharges both O1 and O3's ready-cell link. Model M needs at
least one O1 element and the RES input. The smallest O1 addition is one element that is both
non-MIO and non-DIO, and the smallest ready-cell addition is a law input with a native extraction
route (§2).

***

## 2. Q2: the smallest candidate in one model

### 2.1 O1: H-F1 (hypothesis)

**H-F1.** For one site `m` of a U₂ region, the half-flow `unit S_m (1/2)` of the native swap gate
`S_m : (p_m, c_m) ↦ (c_m, p_m)` (`SecondOrderCircuit.lean:313`, swap layer) is physically
executable, once, under CTRL. Every other operation stays in `𝒩`.

*Why it is minimal in Q2's order [W].*
- By Theorem C at least one element outside `𝒩` is needed, and H-F1 has exactly one.
- It is non-monomial, since `unit S (1/2)` has the entries `(1 ± i)/2` on `{|10⟩, |01⟩}`. So it is
  non-MIO and non-DIO (`OP` route table, `gateFlow_not_monomial`).
- Its support is one site, and the smallest native involution is a single-site gate.
- It acts at one time.

By J1, it acts on the two-point orbit `{10, 01}`, where `W_O` is the single direction
`(|10⟩ − |01⟩)/√2`. This is enough for interference, though not for encoded state preparation.

### 2.2 O3: H-RC and Lemma P6

**Lemma P6 [W; (N) with FB].** Take U₂ on a uniform background `c ∈ {0, 1}`. Let `r` be a cell and
`m` one of its neighbours. If every other neighbour of `r` holds the background value, then
`shear_r` is trivial. So a native copy of `c_m` into `p_r` needs at least one other neighbour `s`
of `r` in a pinned non-background state. With `m_r = 2` (neighbours `m` and `s`), the copy is
exact:
- at `c = 0`, `c_s = 1` gives `p_r ↦ p_r ⊕ c_m`;
- at `c = 1`, `c_s = 0` gives `p_r ↦ p_r ⊕ ¬c_m`.

The gate reads `s` and never writes it, so `s` is a catalyst.

*Proof.* `F(Σ) = 1` iff `Σ ∈ {2, 3, 4}` (P2, Lemma P4).
- With all other neighbours at background, `Σ = c_m` at `c = 0` and `Σ = 5 + c_m` at `c = 1`.
  Neither is ever in `{2, 3, 4}`.
- With `s` pinned, `Σ = c_m + 1` at `c = 0`, which lies in `{2, 3, 4}` iff `c_m = 1`.
- At `c = 1`, `Σ = 4 + c_m + 0`, which lies in `{2, 3, 4}` iff `c_m = 0`.

`shear_r` writes only `p_r`. ∎

**H-RC (hypothesis).** A uniform background region (RES) is a native reservoir of ready cells.
Each recorded bit consumes one background cell `r`, through the catalysed shear copy of P6 applied
under CTRL. The RES cost is the background, plus one pinned catalyst per copy geometry, plus the
register's own pinned initial bits. P5 bounds the number of records by the deficit. The
hypothesis content is in CTRL and FB: in the full native step, every gate acts at every tick, and
MEAS-Q MQ1–MQ3 make any use of the background a breach.

### 2.3 R-READ, under either answer

- **If R-READ holds** (every native readout effect lies in the configuration algebra), native
  readouts are MIO and DIO (`OP` (n3)), and the only O1 candidate is H-F1 or a larger FLOW.
- **If READOUT-ALG finds a native readout `R` with an effect outside the configuration algebra,**
  then `R` is a native non-DIO element. The following holds [W].
  - *Lemma.* A non-destructive Lüders instrument whose projector `P` is not diagonal is also
    non-MIO.
  - *Proof.* A Hermitian idempotent that is CM is also RM, hence monomial, and a monomial
    projector is diagonal. So some configuration `x` has `P|x⟩` not proportional to a
    configuration, and `P|x⟩⟨x|P` is not diagonal. ∎
  - A *non-destructive* `R` would therefore supply both halves of O1 natively.
  - A *destructive* `R` supplies the detector only, as `⟨±|` does in CC-1. O1 would then still
    need a creator.

***

## 3. Q3: the test T-WP (designed; see `PREREG.md`)

### 3.1 The protocol and its slots

- *Geometry (U₂, `c = 0`).* `m = (1,0,0)` is the register site. `r = (1,1,0)` is the ready
  (background) cell, with `p_r = c_r = 0`. `s = (1,2,0)` is the catalyst, with `c_s = 1`. `m` is
  pinned to `(p_m, c_m) = (1, 0)`. Every other site is background.
- *Steps.* Apply the creator `Φ₁`, then `h ∈ {id, COPY}` with `COPY = shear_r` (Lemma P6), then
  the detector `Φ₂`, then a configuration readout of `c_m`. The statistic is
  `W = P(c_m = 1)`.
- *Slots.* The creator is `Φ₁ ∈ {unit S_m (1/2), R_L}` and the detector is
  `Φ₂ ∈ {unit S_m (1/2), R}`. Here `R_L` is the Lüders form of a native readout found by
  READOUT-ALG, if one exists, and `R` is that readout. An arm is a pair `(Φ₁, Φ₂)` whose elements
  exist.

### 3.2 The FLOW × FLOW arm, derived by hand ((I): KIN, FLOW₁, CTRL, FB) [W]

Let `a = (1+i)/2` and `b = (1−i)/2`, so that `unit S (1/2) = a·1 + b·S` on site `m`.
- *`h = id`.* `unit S (1/2)² = S` (`unit_mul_unit`). `|10⟩ ↦ |01⟩`, so `W(id) = 1`.
- *`h = COPY`.* After `Φ₁` the state is `a|10⟩|0⟩_r + b|01⟩|0⟩_r`, and COPY turns it into
  `a|10⟩|0⟩ + b|01⟩|1⟩`. After `Φ₂` it is `a(a|10⟩ + b|01⟩)|0⟩ + b(b|10⟩ + a|01⟩)|1⟩`. So
  `W(COPY) = |ab|² + |ba|² = 1/2`.
- *CC-Δ.* Replacing each element `Φ` by `Δ∘Φ∘Δ` makes the half-step a fair mixing of
  `{10, 01}`. Then `W^Δ(id) = W^Δ(COPY) = 1/2`.

So this arm's outcome is fixed. It is a gap of 1/2 that the copy destroys: WP-NC in
`PREREG.md`'s rule. That is why it is a calibration arm and not evidence.

### 3.3 The classical-simulator countercontrols

- **CC-Δ, the diagonal (Markov) shadow.** It must give no gap on any arm. A WP-NC arm differs
  from it by construction.
- **CC-M, the noninvasive memoryful simulator.**

  **Proposition CC-M [W; (N) as a statement about stochastic maps].** Take any classical model
  with the following properties:
  - the creator and detector slots are fixed stochastic maps on `(x_m, λ)`, where `x_m` is site
    `m`'s configuration and `λ` a hidden memory of any size;
  - `COPY` is the fixed configuration permutation `p_r ↦ p_r ⊕ c_m`, which acts only on
    `(x_m, x_r)`;
  - nothing after `COPY` reads `x_r`.

  In every such model, `W(COPY) = W(id)`.

  *Proof.* `COPY` changes neither `x_m` nor `λ`, which are the only inputs of `Φ₂` and of the
  final readout. So the joint law of `(x_m, λ)` entering `Φ₂` is the same in both settings. ∎

  On any arm with `W(COPY) ≠ W(id)`, therefore, no CC-M model reproduces both laws. The FLOW ×
  FLOW arm is such an arm (§3.2).
- **CC-OI, the scope countercontrol, which must succeed.** OI's intervention dilation realizes
  every finite action-labelled family, with `h` as a setting whose transition law is indexed by
  the setting (`Main:694`; the gluing theorem, `Main:574`). It reproduces both `W(id) = 1` and
  `W(COPY) = 1/2` with supplied data, by an *invasive* copy that acts on the hidden memory. So
  T-WP separates FLOW₁ from noninvasive local-copy classical models only. It does not separate
  FLOW₁ from every OI realization: a classical realization can always match the record laws once
  its copy is allowed to be invasive and its data are supplied. This is I3-SOURCE S1's point that
  the operational target is not ruled out classically.

### 3.4 What T-WP decides and does not decide

- **It decides:**
  - for each available arm, whether the native elements, with the native copy and background
    ready cells in one model, give a non-classical which-path witness (WP-NC) in the senses of
    CC-Δ and CC-M;
  - on the readout arms, whether READOUT-ALG's readout acts as a detector, or as a creator and a
    detector, *operationally*;
  - the RES cost of the protocol, as a count of pinned cells.
- **It does not decide:**
  - whether FLOW₁ or CTRL is physically executable;
  - native timing, which would need autonomous dynamics in place of FB and CTRL;
  - anything at the reference member `q = 2^16`.

***

## 4. Established, Assumed, Missing

**Established** (all [W], unreviewed).

| Result | Class |
|---|---|
| Q-ind (1) | (N) as algebra; (I) on KIN for the matrix reading |
| Q-ind (2) | (I): KIN, PROD, finite environment |
| Q-ind (3) | (I), as OPRES |
| Minimality of H-F1 in Q2's order (§2.1) | (I): KIN, FLOW₁ |
| Lemma P6 | (N) with FB |
| The lemma that a non-diagonal non-destructive Lüders instrument is non-MIO (§2.3) | (I): KIN |
| The FLOW × FLOW arm's laws (§3.2) | (I): KIN, FLOW₁, CTRL, FB |
| Proposition CC-M | (N) as stochastic mathematics |
| The CC-OI scope statement | (P), from `Main:574` and `Main:694` |

**Assumed.**
- KIN: every coherent statement.
- FLOW₁: the creator and detector of the FLOW arms.
- CTRL: every selective application, of the copy and of the flows.
- FB: P6 and the geometry.
- RES: the background, the catalyst `s` and the pinned register bits.
- READ: configuration readout of `c_m`.
- PROD: Q-ind (2).
- R-READ: not assumed. The readout arms exist only if READOUT-ALG returns a counterexample.

**Missing.**
- *O1.* The earliest unsupported step is a native non-MIO element and a native non-DIO element.
  Both are physical mechanisms.
  - If R-READ holds, neither exists in `𝒩` (OPRES §5), and H-F1 is the smallest addition.
  - If R-READ fails non-destructively, both could be native, and T-WP's readout arms are the
    decisive test.
  - If R-READ fails destructively, the detector is native and a creator is still missing.
- *O3.* Given RES as a background, the earliest unsupported step is native extraction: replacing
  CTRL and FB by the autonomous rule. That is a physical mechanism inside the rule: NU's bounded
  breach (QS H-QOPS-M). P6 is the mathematics that settles the catalyst count.

***

## 5. Pressure test (§A.31)

1. *The calibration arm is favourable and fixed.* It is not counted as evidence (§3.2). The
   productivity verdict is INCONCLUSIVE, not GEM.
2. *CC-M is a narrow class.* Its no-go depends on noninvasiveness and on nothing reading `x_r`.
   CC-OI shows that dropping noninvasiveness restores classical reproduction. The test is scoped
   accordingly.
3. *H-RC's extraction is where the physics is.* CTRL and FB do the work in the protocol, and the
   native rule's own dynamics does not apply single gates.
4. *The readout-arm lemma* uses the configuration-basis Lüders form. If READOUT-ALG's readout has a
   different instrument form, the arm's classification is re-derived in an amendment before any
   run.
