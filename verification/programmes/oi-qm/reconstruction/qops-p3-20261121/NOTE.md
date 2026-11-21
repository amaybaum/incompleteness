# QOPS-P3: the next minimal native-mechanism test

**Standing. WIP / UNVERIFIED.** Writer's design record under `PLAN.md`, which was committed first
at `ba2f83a2`. It contains paper proofs and design only. It runs no computation and adopts no
premise.
- **Review.** Independent non-author review at `826cb00d`: REVISE
  ([#1518 c.7066768898](https://github.com/amaybaum/incompleteness/pull/1518#issuecomment-7066768898)).
  R1–R4 and n1–n6 are answered in appended commits, together with the owner's provisional
  constraint on R-READ (§2.3).
- **Changes to the frozen plan.** They are in `amendments/A01-twp-standing.md`. `PREREG.md` is
  unchanged.

- **Authorization.**
  [#1169 c.7066630306](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066630306)
  (Group B, at design level).
- **Goal link.** The goal link is the one stated in `PLAN.md`.
- **Base.** The base is #1501 at `cd3672fa` (`P2`). Line numbers are at `main` `df6da1c6` unless
  stated otherwise.
- **Inputs used.** They are cited and not redone.
  - OPRES (#1511, head `7669e511`, `OP`): the classes `𝒩` and `𝒩⁺`, Lemma C, Theorem C and CC-1.
    - The owner records OPRES as a reviewed stopping point, CONFIRMED WITH NITS (c.7066452685,
      final nit verified; #1169 c.7066541026).
    - Its own text still labels Lemma C through Remark D′ "pending review" (`NOTE.md:46`, `:400`
      at `7669e511`).
    - They are used here at that standing.
  - I3-SOURCE (#1508 `df520f3b`): S1.
  - P2's P1, P4, P5 and J1.
- **R-READ is unresolved** (READOUT-ALG, #1513 at `0ba83cff`, provisional and under review). It is
  treated as the owner's provisional constraint (§2.3), not as a theorem.

**Imports and inputs.**
- From P2: KIN, FLOW, READ, RES, PROD and FB.
- New here: **CTRL**, the selective application of a chosen native gate at a chosen time. This is
  the supplied control of QS H-QOPS-C, NU's question for the native form.
- **FLOW₁** is FLOW restricted to one native gate at one time `t ∈ (0, 1)`.

***

## 0. Answers

1. **Q1, how the obligations relate. ESTABLISHED for the cases stated; one case OPEN
   (Proposition Q-ind).**
   - Ready-cell sources are neither non-MIO nor non-DIO.
   - Unitary elements are not ready-cell sources beyond the reservoir deficit.
   - Non-MIO does not imply non-DIO, and non-DIO does not imply non-MIO. Each non-implication has
     a named witness.
   - **Open:** whether an *appended-state* creator, a supply of pure coherent ancillas, can be
     converted by native operations into ready cells. Such a supply is itself a zero-entropy
     resource, and P5 does not exclude the conversion.
2. **Q2, the smallest candidates. ESTABLISHED, in `PLAN.md`'s order.** The order counts elements
   outside `𝒩`, then support, then RES cost, with support counted in sites, as `PLAN.md` states.
   - *O1.* The minimum is one element. H-F1, the half-flow of the native swap at one site, is
     *a* minimal representative, not the unique one.
     - It ties with the half-flow of an unconditional-NOT shear gate at one site (H-F1′) and with
       every `t ∈ (0, 1)`.
     - At site granularity H-F1 wins on RES, since it needs no catalyst while H-F1′ needs at
       least two.
     - At cell granularity, H-F1′ is smaller, acting on one cell where H-F1 acts on two.
   - *O3, in the same model:* **H-RC**. Ready cells come from a reservoir supplied by RES, the
     uniform background, through a native shear-gate copy. Lemma P6: a copy needs **at least one**
     pinned non-background catalyst, and **one suffices**.
3. **Q3. T-WP is kept as a paper protocol that defines the operational witness.** Under either
   R-READ answer, its computation reduces to hand calculations:
   - FF is fixed (§3.2);
   - each readout arm is fixed once its instrument is named.

   The hypotheses that matter (FLOW₁ executable; `R` native and of a given form) are inputs of
   the test, never outputs.
4. **Productivity (`PLAN.md`): NON-GEM as a computation.** Criterion (ii) fails on both R-READ
   branches. Criteria (i) and (iii) hold. The decision-relevant uncertainty is at the instrument
   level of R-READ (§2.3), which is a paper question for READOUT-ALG and the next unit, and not a
   computation of T-WP.

***

## 1. Q1: what is and is not implied

**Proposition Q-ind [W].** Take model M of P2 §4, with OPRES's class `𝒩` as the native operations.

| # | Non-implication | Witness or proof | Class |
|---|---|---|---|
| 1 | ready-cell source ⇏ non-MIO, and ready-cell source ⇏ non-DIO | appending a configuration state or a diagonal mixture (`OP` (n2)) is MIO and DIO (OPRES Lemma C) | (N) as algebra; (I) on KIN for the matrix reading |
| 2 | unitary non-MIO or non-DIO element ⇏ ready cells beyond the deficit | P5(2): for every unitary on register ⊗ environment from a product state, with a finite environment, removal is at most `log|H| − S(σ)` | (I): KIN, PROD |
| 3 | non-MIO ⇏ non-DIO | appending a fixed coherent `ω` (`𝒩⁺`) is DIO and non-MIO (OPRES Lemma C) | (I), as OPRES |
| 4 | non-DIO ⇏ non-MIO | the destructive readout `⟨±|` is MIO and non-DIO (OPRES CC-1) | (I), as OPRES |
| — | **open:** appended-state creator ⇒ ready cells? | not covered by P5, see below | — |

*The open case.* A supply of pure `|+⟩` ancillas is a creator (row 3), and it is also a
zero-entropy supply. Modelled as an environment in a pure state, it has the full deficit, so P5
permits extracting ready cells from it. Whether `𝒩`, with READ, performs that extraction without
consuming an equal number of fresh record cells is not shown. One route is configuration readout,
then a feedforward NOT, then discard of the record; the readout's record needs a cell of its own.
So row 2 covers unitary elements only, and the appended-state case is **open**.

*Consequence.* Rows 1 and 2 show that no ready-cell source and no *unitary* O1 element discharges
the other obligation. Rows 3 and 4 show that the two halves of O1 are distinct, and one element can
meet both (a non-monomial unitary, `OP` §4). For a *coherent supply*, whether it also serves as
RES is open.

***

## 2. Q2: the smallest candidates in one model

### 2.1 O1: H-F1 and its ties (hypotheses)

**H-F1.** For one site `m` of a U₂ region, the half-flow `unit S_m (1/2)` of the native swap gate
`S_m : (p_m, c_m) ↦ (c_m, p_m)` (`SecondOrderCircuit.lean:313`, swap layer) is physically
executable once, under CTRL. Every other operation stays in `𝒩`.

**Ties.** In `PLAN.md`'s order, with support counted in sites, all of the following tie with H-F1
on the first two criteria: one element, one site.
- **H-F1′.** `unit shear_m (1/2)` at a site whose pinned neighbours make `shear_m` an unconditional
  NOT on `p_m`. By the count in §2.2, that needs two or three pinned non-background neighbours.
- **H-F1(t).** The same flows at any `t ∈ (0, 1)`. `unit g t` is non-monomial there
  (`gateFlow_not_monomial`, `CoherentContinuumSource.lean:74`).

The third criterion, RES, separates them. H-F1 needs no catalyst, because the swap is native at
every site, while H-F1′ needs at least two. So H-F1 is the representative chosen at site
granularity. At cell granularity H-F1′ (one cell, `p_m`) is smaller than H-F1 (two cells), and the
order would choose it instead.

Each is non-monomial, hence non-MIO and non-DIO (`OP` route table). By Lemma P1, H-F1 acts on the
two-point orbit `{10, 01}`, whose `W_O` is the single direction `(|10⟩ − |01⟩)/√2`. That is enough
for interference, though not for encoded state preparation (J1).

### 2.2 O3: H-RC and Lemma P6

**Lemma P6 [W; (N) with FB].** Take U₂ on a uniform background `c ∈ {0, 1}`, a cell `r` and a
neighbour `m` of `r`. Let `k` be the number of other neighbours of `r` held in a pinned
non-background state, with the rest at background.
- **At least one is needed.** If `k = 0`, then `shear_r` is trivial.
- **One suffices.**
  - At `c = 0`, `Σ = k + c_m`. `k = 1` gives the copy `p_r ↦ p_r ⊕ c_m`, `k = 2` or `3` gives an
    unconditional NOT, `k = 4` gives the negated copy, and `k = 5` gives nothing.
  - At `c = 1`, with the pinned neighbours at 0, `Σ = 5 − k + c_m`. `k = 1` gives the negated copy,
    `k = 2` or `3` gives an unconditional NOT, `k = 4` gives the copy, and `k = 5` gives nothing.

Every catalyst is read and never written.

*Proof.* `F(Σ) = 1` iff `Σ ∈ {2, 3, 4}` (P2, Lemma P4). Each case above is that window applied to
`Σ`. `shear_r` writes only `p_r`. ∎

**H-RC (hypothesis).** Ready cells come from a reservoir **supplied by RES**: the uniform
background's zero entropy is the RES input. Each recorded bit consumes one background cell `r`,
through the catalysed shear copy of P6 applied under CTRL. The RES cost is the background, plus at
least one pinned catalyst per copy geometry (one suffices), plus the register's own pinned initial
bits. P5 bounds the number of records by the deficit. The hypothesis content is in CTRL and FB: in
the full native step, every gate acts at every tick, and MEAS-Q MQ1–MQ3 make any use of the
background a breach.

### 2.3 R-READ at three levels (the owner's provisional constraint)

The three levels are kept distinct, as the owner requires (#1169, in the Phase-3 addendum).
1. **Observable effects.** READOUT-ALG (#1513 `0ba83cff`, provisional, under review) finds that,
   under its stated hypotheses, native readout effects lie in the configuration algebra. This is
   treated as a question under review, not a theorem.
2. **Complete instruments and their state updates.** Instruments are DIO only for the listed
   monomial-Kraus cases (OPRES Lemma C). Diagonal effects do not imply DIO, since the update can
   still detect coherence. For example, a one-outcome instrument `Ad_H` has effect `1`, which is
   diagonal, and it is not DIO. Whether all native instruments are DIO is **open**, and so is
   whether bare OI supplies a non-DIO element. Native non-DIO is open, not impossible.
3. **Operationally accessible observable algebras.** The corpus states that the observable algebra
   on each finite region is, or may be taken to be, the full matrix algebra on the configuration
   space (`papers/Structure.md:742`, "may be taken to be"; `:788`; `Main:722`; `GR:366`). These
   are statements about the representation's observable algebra. They do not instantiate a native
   readout or instrument, and a mathematically available algebra is not a physically implementable
   measurement. Nothing here uses the full algebra as if it supplied operations.

**The instrument-level lemma [W; (I): KIN].** A non-destructive Lüders instrument whose projector
`P` is not diagonal is non-MIO.

*Proof.* A Hermitian idempotent that is CM is also RM, hence monomial, and a monomial projector is
diagonal. So some configuration `x` has `P|x⟩` not proportional to a configuration, and
`P|x⟩⟨x|P` is not diagonal. ∎

The lemma is a statement at level 2 about instruments *of that form*. No native instrument of that
form is known. If READOUT-ALG or a successor found a native instrument with a non-diagonal Lüders
projector, it would meet both halves of O1. A destructive one would meet the detector half only.

***

## 3. Q3: T-WP as a paper protocol

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

  **Proposition CC-M [W; (N) as a statement about stochastic maps; CONFIRMING].** This is the
  standard noninvasive-measurability argument behind the Leggett–Garg inequalities (Leggett and
  Garg 1985) and no-signalling in time (Kofler and Brukner 2013) [LIT2], stated for this protocol.
  Take any classical model with the following properties:
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

### 3.4 Standing of T-WP

- **What it defines.** An operational witness: a gap against the diagonal shadow (CC-Δ),
  together with sensitivity to a native, noninvasive copy (CC-M). It also defines the RES count of
  a native interferometer.
- **What it does not do.**
  - It is not a decisive computation. FF is fixed by §3.2. Each readout arm is fixed by a hand
    calculation once its instrument is named in an amendment.
  - It decides no physical executability: not that of FLOW₁ or CTRL, not native timing, and
    nothing at `q = 2^16`.
  - CC-OI shows that it does not separate the hypotheses from invasive classical realizations
    with supplied data.
- **Where a decisive next step lies.** At level 2 of §2.3: does the native rule, with its stated
  access, define any instrument whose update is non-DIO, or non-MIO? That is a paper question about
  instruments and their updates, and T-WP does not compute it. It is the owner's sharper target:
  an admissible mechanism that both generates coherence and operationally detects it, without
  importing that capability.

***

## 4. Established, Assumed, Missing

**Established** (all [W], unreviewed).

| Result | Class |
|---|---|
| Q-ind rows 1–4 (row 2 for unitary elements only) | as in §1 |
| H-F1 and its ties, with the ordering criterion stated (§2.1) | (I): KIN, FLOW₁ |
| Lemma P6 (at least one catalyst; one suffices; full count table) | (N) with FB |
| The instrument-level Lüders lemma (§2.3) | (I): KIN |
| The FF arm's laws (§3.2) | (I): KIN, FLOW₁, CTRL, FB |
| Proposition CC-M | (N) as stochastic mathematics; CONFIRMING [LIT2] |
| The CC-OI scope statement | (P), from `Main:574` and `Main:694` |

**Assumed.**
- KIN: every coherent statement.
- FLOW₁: H-F1 and its ties, and the FF arm.
- CTRL: every selective application.
- FB: P6 and the geometry.
- RES: the background, the catalysts and the pinned register bits.
- READ: configuration readout.
- PROD: Q-ind row 2.
- R-READ: not assumed. It is kept at three levels (§2.3).

**Missing.**
- *O1.* The earliest unsupported step is a native non-MIO element and a native non-DIO element,
  both physical mechanisms. At level 2 of §2.3 whether either exists is open.
- *O3.* **RES remains the earliest input**: a producer of known-state cells (P2). Given RES, the
  earliest unsupported *mechanism* is extraction, which means replacing CTRL and FB by the
  autonomous rule. That is a physical mechanism inside the rule: NU's bounded breach (QS
  H-QOPS-M). P6 is the mathematics that settles the catalyst count.
- *Q-ind.* Whether a coherent supply can serve as RES (§1) is open, and it needs mathematics:
  extraction within `𝒩` with READ.

***

## 5. Pressure test (§A.31)

1. *Every branch of T-WP is fixed.* The productivity verdict is NON-GEM as a computation, recorded
   honestly. PLAN admitted INCONCLUSIVE, and the review showed that both branches resolve.
2. *CC-M is standard and narrow.* It is a Leggett–Garg-type argument, CONFIRMING. CC-OI shows that
   invasive classical realizations reproduce every arm.
3. *H-RC's extraction is where the physics is.* CTRL and FB do the work.
4. *The ties of H-F1 depend on granularity.* The site-granularity choice follows `PLAN.md`, and
   both orders are reported.
5. *§2.3 resists the favourable inference.* The full-matrix-algebra statements do not supply
   instruments.

| Item | Proposed class |
|---|---|
| Q-ind | ELABORATING (combines OPRES and P5), with one OPEN case |
| H-F1 with its ties | ELABORATING |
| P6 | ELABORATING (P4's window, counted) |
| The Lüders lemma | ELABORATING |
| CC-M | CONFIRMING |
| The unit | NON-GEM as a computation; it defines a protocol and locates the next node (level 2) |
