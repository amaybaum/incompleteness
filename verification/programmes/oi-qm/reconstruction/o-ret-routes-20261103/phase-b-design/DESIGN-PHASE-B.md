# O-RET Phase B: native-retention design

**Status: WIP / UNVERIFIED.** A paper-only design under #1032 comment 6649418760. It is not
independently reviewed, not frozen and not authorized to run. It adopts no premise and selects no
candidate. No computation, enumeration, simulation, script or Lean build was run for it; every
value below is a hand derivation, marked as such.

**Support labels.**
- **[PA]** Phase A evidence on `main`: the frozen inputs at `F = 49f0bd41` and `phaseA/run-1/`.
- **[R]** `ROUTES.md` at `F`. It is in `main`'s history, but no review record of it is on `main`,
  so its lemmas are used here as design motivation, never as premises (programme `README.md:30–35`;
  AGENTS.md §A.46 item 7).
- **[DP]** `DESIGN-PULSE.md` r6, frozen at `F`. Its reviews are on PR #1078, off `main`; the same
  restriction applies.
- **[MR]** the frozen MR-1 record `../measurement-record-formation/amendments/MR-star.md`.
- **[O]** an owner decision recorded on #1032 or #914, quoted with its comment id.
- **[D]** a paper derivation made here. Unreviewed.
- **[L]** literature. Section 9 says which items were read directly.

`D:n`, `P:n`, `R:n`, `MR:n` are line numbers of `DESIGN-PULSE.md`, `PREREG-PHASE-A.md`, `ROUTES.md`
at `F`, and `MR-star.md`, all at `D` = `f5c281ae`.

***

## 1. Starting point (a)

### 1.1 What Phase A established

The owner's note to this unit (#1032 c.6649418760): "O-RET Phase A passed 49/49 frozen calibration
cases. That result validates the calibration implementation, not physical retention in native OI."

**The count is verified against the record.**
- `phaseA/run-1/phase-a/summary.json` has `tuples_frozen` 49, 49 entries in `tuples_evaluated`,
  `verdict` `PASS`, `exit` 0 and `first_failure` null. It was read, not regenerated.
- `phaseA/run-1/RESULT.md:42–45`: "`summary.json` has `verdict` PASS, `exit` 0, `first_failure` null,
  and 49 of 49 frozen tuples evaluated in the frozen order."
- `RESULT.md:49`: "The rows assigned were 2b ×14, 5 ×7, 1 ×6, 2a ×6, I-9 ×5, 6 ×4, 8 ×3, I-3 ×2, 3 ×1
  and 7 ×1." These sum to 49, and the per-tuple `row` fields of `summary.json` give the same tally.
- `phaseA/run-1/REVIEW.md:9–11`: "CONFIRMED PASS … an independent re-application of the frozen
  rule found 0 mismatches across 49/49 tuples."

**What the pass shows, in the record's own words.**
- PREREG §1 (P:41–43): "On these toy instances, under the conventions of §2, exact enumeration
  reproduces the hand derivations of DESIGN §3 and §6 and of §3 below, and the implemented §4
  precedence assigns the hand-assigned rows. This is a result on the consistency axis (§A.23)."
- Owner (RESULT.md:55–57): "The verified PASS establishes that the implementation agrees with its
  49 frozen calibration expectations. It does not establish physical retention in native OI
  dynamics or validate the classifier outside this test set."
- RESULT.md:59: "The agreement holds under the frozen conventions: `ε* = 1/20`, and conditioning on
  the declared preparation set `P`."

So Phase A shows that one implementation of the §4 classifier agrees with hand algebra on 49 toy
cases. The classifier itself (rows, precedence, DIL∃, J-1, the `G`-rule) is calibrated on those
cases and nowhere else.

### 1.2 What Phase A did not establish

- **Any retention mechanism, native or otherwise** (P:45). Every storage control imposes its law
  ("Every storage control imposes its preparation (quiet bits and ready registers)", P:696).
- **O1, O3, O4** (P:45–46): physical source of the preparation, accessible readback, observer
  formation.
- **Validity outside the control set.** P:666–668: "The controls are toy rules designed with known
  answers, and the expected values come from the same design. A pass shows that the implementation
  and the hand algebra agree. It does not show that the criteria separate storage from transport
  on cases outside the set."
- **Coverage** (RESULT.md:64–70; P:669–682): row 4 (I-8) is a declared constant; evidence rows I-1,
  I-2 and I-5 are not exercised; CX-4 is absent; row 3 is reached only through `ε_max > ε*`; no
  tuple has a J-1 failure in `H_{T′} ∖ H_T`; exit 4 is exercised only in the self-test.
- **Reproducibility.** `REPLAY.json`: "Not replayed … byte-for-byte reproduction outside that run
  has not been established." Python hash-seed independence and the reviewer's re-check script are
  not on `main` (RESULT.md:51–53).
- **Decisions left open for Phase B.**
  - The decoder rule off the write-tick support (owner, #1032 c.6622434587: "a separate decision, to
    be made before Phase B"). PREREG §2.8 shows that those values decide rows: with the minimal
    tie-break, HC-SW becomes TR, and HC-TS becomes TR on `W₁` itself (P:212–215).
  - `w*` and `T*` (P:223, "unset and unused").
  - The nonlinear rule and its instance (D:559).
- **Conventions that decide verdicts** (P:689–692): the support conditioning `μ(·|σ∈P)`, the cell
  decomposition and the choice of `A` (I-5 not evaluated).
- **Known blind spots** (P:683–688): J-1 admits advection inside `A` and outflow; DIL∃ over-rejects
  through pooling (CX-4) and joint support (CX-4b); the siding of CX-7 is undecided.
- **The paper lemmas are not premises.** Lemmas S, S′, Q, C and L [R] have no review record on
  `main` (programme `README.md:30–35`). They motivate this design and appear in it only as hand
  checks to be re-derived.

### 1.3 Two new paper observations that bear on Phase B [D]

Both are stated in one direction only, and both are offered for independent review.

**Lemma PAD (the register's own previous slice is a one-time pad at the write tick).**
- *Setting.* A copy-form bijection `φ(x, y) = (y, G(y) − x)` on cells with values in a finite
  abelian group `𝐑`, where `G_i` depends on the current slice `y` only. K1 (SM:296; `R:18–19`), the
  SM:112 ring rule, and rule h (`⊕` on `𝔽₂³`) all have this form (SM:106: "x_i(t+1) =
  f(neighbors of i at time t) − x_i(t−1)").
- *Hypotheses.* `A` is a set of sites disjoint from the carrier sites. Under the law `μ` at `t₀`,
  `x_A(t₀)` is uniform on `𝐑^A` and independent of `W := (y(t₀), x_{Λ∖A}(t₀))`. The carrier
  variable `κ` is a function of `W`.
- *Claim.* `y_A(t₀+1)` is uniform and independent of `W`, hence of `κ`. So the current-slice
  readout of `A` at `t₀+1` has the same law under every carrier preparation: `TV_{t₀+1} = 0`, and
  every decoder has `ε_max(t₀+1) ≥ 1 − 1/m`, the blind bound of D-MET.
- *Proof.* Given `W`, `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` is a fixed translate of a uniform variable
  independent of `W`. ∎
- *Consequence.* Under `π₀`, or any law that leaves `x_A(t₀)` free, uniform and independent, no
  current-slice register of a copy-form rule is written at all, exactly or approximately, whatever
  the rule's nonlinearity. Native retention through an H-cur register therefore needs, at least, a
  restriction on the register's own previous slice at `t₀`: a ready register, the resource that
  MR★ C-3 names ("the absence of a physically sourced quiet, ready region", MR:1344–1345).
- *Classification (§A.31).* CONFIRMING. It is the CN control (#1032 c.6567189236) and the remark
  "K1's `y′_V = drive − x_V`, with `x_V` as the one-time pad" (R:314–315), extended from K1 to every
  copy-form rule. It is used below as a control with an exact expected value, not as a premise.

**Observation W1 (on copy-form rules, a one-tick hold is exposed to a channel that opens one tick
later).**
- *Hand instance.* K1 at K-18(b): `ℤ/5`, `q = 2`, `a = 1`, carrier `Σ` = site 0 (both slices),
  background `δ₀`, register `A` = sites 1–4. The carrier imprint is HC-K1 (R:130–137).
- With the carrier's previous slice fixed to 0 (preparations `(x₀, y₀) ∈ {(0,0), (0,1)}`) and the
  decoder `g = OR(y₁, …, y₄)`:
  - `y(t₀+1) = (0, c, 0, 0, c)` and `y(t₀+2) = (c, 0, c, c, 0)`, with `c = y₀(t₀)`, by HC-K1.
  - At the first hold tick the only input from outside `A`, `y₀(t₀+1) = x₀ = 0`, is quiet. J-1
    passes, and DIL∃ holds on `W₁`: with that input fixed at 0, the two-slice register update
    `(x_A, y_A) ↦ (y_A, Adj_{P₄} y_A − x_A)` is a bijection whose orbit through `(0000, 1001)` is
    `(0000,1001) → (1001,0110) → (0110,0110) → (0110,1001) → (1001,0000) → (0000,1001)`, and it never
    meets the supported blank `(0000,0000)`.
  - The Phase A rule therefore reaches its storage step at `T = 1`. SCH fails at `t₀+1`
    (`Par(y₂) ∩ C_{t₀+1} ∋ y₁`), so the row is 6 (I-4, register-level circulating storage).
  - At `t₀+2`, `y₀(t₀+2) = c`: the carrier's own site carries the value again (the 1D wake of
    MR★ C-2, MR:1322–1332). J-1 (J-i) fails, and at `T = 2` the row is 1 (RS).
- *Reading.* What the frozen rule calls one-tick circulating storage here is the K1 wavefront
  crossing a register that covers four of five sites, and it is classified as re-supply one tick
  later. Two features did it: the register is nearly the whole system, and the carrier's
  previous-slice channel reaches `Σ`'s neighbourhood one tick after the write.
- *Consequences for the design.* A locality gate (§3.2, LOC), a minimum window of two hold ticks for
  a native positive (§6.4, `T* = 2`, an owner decision), and this instance as a control (§6.3,
  NK-Wq).
- *Classification (§A.31).* NEW (candidate): a T = 1 blind spot of the Phase A classifier on
  copy-form rules. It is one instance, not a theorem about all copy-form registers.

***

## 2. The candidate mechanism (b)

### 2.1 What the reviewed routes leave

From `ROUTES.md` [R] and DESIGN-PULSE [DP]:
- **Route I** (state-selected access) is blocked for exact retention under every law with
  φ-invariant support (Lemma S′), and undecided outside (R:233–240).
- **Route II** (a restricted prior on an existing rule):
  - on linear K1 at K-18(b): blocked under RET-st, undecided under D-RET (R:317–327);
  - on nonlinear copy-form rules: undecided, ceiling CONDITIONAL[H-sel, H-cur (declared)]
    (R:328–335).
  - The Comparison names it "Open native route with no added interaction" (R:462–463).
- **Route III** (`M_F`, `M_T`): CONDITIONAL on a new, unjustified F2 extension E-reg, designed for
  the purpose; "not a candidate while E-reg is unjustified (§A.29)" (R:421–426).
- **The resource every exact route needs** (annotation, #914 c.6612951653): a law whose support is
  not φ-invariant and excludes overwrites at the hold tick. It is unsourced (MR★ C-3).
- **Lemma PAD** (§1.3) adds that, for copy-form current-slice registers, readiness of the register's
  own previous slice is needed for a write at all.

So no route offers a sourced mechanism. The smallest candidate that uses native dynamics and adds
no interaction is route II, made concrete with a register, a write, a law family and a decoder that
are all fixed in advance.

### 2.2 The candidate: NRR-1, native ready-register retention

**Definition.** NRR-1 is the following family of tuples, fixed before any evaluation.

| Element | Specification | Status |
|---|---|---|
| Dynamics | an in-corpus copy-form bijection `φ(x, y) = (y, G(y) − x)`: K1, or the SM:112 ring rule (§2.3) | K1: OI-native under posit (vii) (Main:726). SM:112 ring: in-corpus construction; as physics, F2 extension E-SDC (§2.3) |
| Carrier | `Σ` = one site, both slices, at `t₀`; `μ_Σ` uniform; `P` = all carrier values; `f(σ) = y_Σ(t₀)` | declared preparation |
| Register | a fixed set `A` of sites disjoint from `Σ`; locus `R` = both slices of `A`; read cells = the current slice of `A` | declared (H-cur), as in D-ACC |
| Write | the native step `t₀ → t₀+1`. No gate is added. | native (the dynamics row) |
| Hold | the native step at every hold tick | native |
| Law | `μ = μ_Σ ⊗ ν_r`, with `ν_r` from the ready-region family of §6.2 (`r = −1` is `π₀`) | `π₀`: conditional on H-μ. `r ≥ 0`: imposed, H-sel |
| Decoder | fixed at the write tick by rule D2 (§6.2), never by later outcomes | imposed rule |
| Criteria | the Phase A classifier with amendments B-1 to B-4 (§6.2) | imposed rule, calibrated by controls |

**Why it is the smallest native candidate.**
- It adds no interaction to the native step (route III adds E-reg).
- It adds no access mechanism beyond the declared baseline H-cur (route I would need one).
- It places all imposed structure in the starting law, in one parameter: the radius `r` of the
  ready region around `A`. The ledger `D(ν_r)` is the number of constrained bits, and the
  probability that `π₀` produces the ready region spontaneously is `2^{−D(ν_r)}`. That is OQ-8's
  preparation column, and the write probability of the same event (§6.6).
- It adopts DESIGN-PULSE's §8 Phase B target (D:576–582): K1 at K-18(b) with every nonempty
  `A ⊆` sites 1–4 and the laws `π₀`, `δ₀` and `δ_b`; a nonlinear copy-form rule at `|S| ≤ 2¹⁶`;
  `T = 1, 2`. It refines it with the locus, the law family and `T = 3`.

**What NRR-1 is not.**
- Not a SOURCE-CANDIDATE: `ν_r` for `r ≥ 0` is imposed, and access is declared.
- Not selected: K1 and the SM:112 ring rule are evaluated under one preregistered rule, and neither
  is preferred in advance (#1032: "tested without choosing the winner post hoc").
- Not a claim that native retention exists. It is the object Phase B would test.

### 2.3 OI-native parts and F2 extensions

- **K1** (`φ(x, y) = (y, Ay − x)`, `(Ay)_i = Σ_{j∼i} y_j`, `a = 1`, `ℤ/q`). Native under posit (vii),
  "linearity of the substratum update (A5)" (Main:726). That this is the physics is a posit
  (MR★ C-1, MR:1309–1320). On K1, by Lemma L [R] and S-C1 [MR], the transfer to any region does not
  depend on any other region's state, so a prior can supply offsets but cannot gate the write.
- **The SM:112 ring rule.** `x_i(t+1) = x_{i−1}(t) + x_{R(i,x(t))}(t) − x_i(t−1)` mod `q`, with
  `R(i, x) = i+2` if `x_{i+1} = 0` and `i+1` otherwise (SM:112). It is an in-corpus construction
  satisfying SM §3.1's constraints (i)–(iii). Its transfer to site `i` depends on the value at
  `i+1`, which is what K1 lacks. It is nonlinear, so taking it as the physical update departs
  from posit (vii).
  - **F2 extension E-SDC (unadopted):** "the native step has SM §3.1-type state-dependent
    coupling, realized by the SM:112 ring rule". The O-OBSMU record states the same idea as
    proposal P-SDC (branch `research/o-obsmu-20261104` at `f67b9f0c`, `ANALYSIS.md` §4.4,
    provenance only). It has no independent consequence identified, and its switching rule is
    unconstrained, so it fails §A.29's hard-to-vary test as it stands. Phase B would test it only
    as a named hypothesis; a positive under it is CONDITIONAL[E-SDC].
- **Rule h.** `U_{t+1}(v) = U_{t−1}(v) ⊕ h(⊕_{w∼v} U_t(w))`, `h(A,B,D) = (B, D, A ⊕ BD)` on `𝔽₂³` per
  site, six neighbours (`../native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md`,
  dynamics block). It is also outside posit (vii). Its smallest torus has `|S| ≥ 2⁴⁸`, beyond
  exhaustive enumeration; it is not in the default instance set (owner decision G-1).
- **Not native, and not used:** E-reg (`M_F`, `M_T`), any clock register, any adaptive or moving
  readout, any decoder chosen after the write tick.

***

## 3. Discrimination (c)

Each failure mode has an operational criterion, evaluated by the classifier on structured fields,
and at least one countercontrol whose expected row is fixed in advance. The criteria are Phase A's
(DESIGN-PULSE §2.3–§4; PREREG §4) unless marked as a Phase B amendment.

### 3.1 Travelling pulse

**Criterion TP.** A storage row (5 or 6) requires all of the following:
- DIL∃ on `W_T` exactly, or DIL∃-η with the Lemma H bound `≤ ε*` on `W_T` (ST, D:170–173);
- no observed `ε_max > ε*` on the gap-free extension window `W_{T′}`, `T′ = max(T, τ)`. Otherwise
  the case is TR (no consistent `G`) or EX (some consistent `G`) (P:468–469);
- for copy-form rules, DIL∃ on the two-slice locus (amendment B-1), so the register's own previous
  slice is part of `R` and not a quiet input;
- the locality gate LOC (amendment B-4);
- for the mechanism verdict, `T ≥ T*` with `T* = 2` (§6.4).

**Why each part is needed.**
- DIL∃ is the only Phase A criterion that separates HC-TS from HC-SW on `W₁` (D:507–525, L1).
- The observed failure prevents DIL∃'s over-rejections (CX-4, CX-4b) from being read as transport
  (P:125).
- W1 (§1.3) shows that on a copy-form register a one-tick window can be passed by a wavefront.

**Countercontrols.** HC-TS and HC-TM [PA] (expected TR, P:341–346); MB [PA] (TR); NK-W and NK-Wq
(§6.3, native K1, expected RS, and I-5G at `T = 1` for NK-Wq).

### 3.2 Recurrence

**Criterion RC.**
- Every window is gap-free: `ε_max` and J-1 are evaluated at every tick of `W_{T′}`.
- A readback success at a tick after an observed failure is flagged and never supports rows 5 or 6
  (the recurrence rule, P:456–463).
- Phase B adds a reported field `n_supp`, the period of `φ` on the support of `μ`. By Lemma P [DP]
  (D:141–145), exact retention over `W_T` needs `T ≤ n_supp − 2`. A storage row with
  `T′ ≥ n_supp − 1` is a recorded inconsistency and halts the run (exit 6, §6.7), because Lemma P
  forbids it.

**Countercontrols.** HC-R1 and HC-R3 [PA]: a single late readback passes, while the gap-free
window gives RS (P:354, :359). They are cited, not re-run; their role in Phase B is carried by the
recurrence-flag field and the exit-6 check.

### 3.3 Continual re-supply

**Criterion RS.**
- J-1 with `B_t := Q = Par(R) ∖ R`, computed from `φ` on all of `S` (P:81–86), at every hold tick of
  `H_{T′}`: (J-i) `Q_t ⫫ κ` jointly, and (J-ii) `κ ⫫ Q_t | R_t`. A failure is row 1 and takes
  precedence over every storage row.
- With the two-slice locus (B-1), `Q` is the current slice of `A`'s outside neighbours, including
  the state-dependent neighbours of the SM:112 rule. For a register adjacent to `Σ`, `Q` contains
  the carrier's current slice. So J-1 tests the requirement of D-TRN (T-2) that the hold ticks
  come after "the incoming carrier has left".
- J-1 is an inflow screen only (P:164–166). Advection inside `A` and outflow are left to TP.

**Countercontrols.** HC-R2 and SC [PA] (RS; SC through J-ii alone, the joint-information case the
owner asked for); NK-W (native K1 under `δ₀`: J-i fails at `t₀+1`, because `y₀(t₀+1) = x₀`); NK-K3
(HC-K3, countercontrol (g): its planted-marker decoder holds `y₀` while J-i fails at `t₀+1`).

### 3.4 What the three criteria cannot separate

- **A dwell in a closed locus** (CX-7, the siding). Storage here means "a dwell at a closed locus
  covering `W_T`" (D:489–490). Phase B inherits that reading.
- **Information carried jointly by `Q` and cells beyond it.** J-1 tests `Q` only. Uniform cells
  outside the ready region can one-time-pad the carrier's influence so that `Q` looks independent
  of it (Lemma PAD's mechanism, applied to `Q`). The case is then decided by DIL∃ and the observed
  window, not by J-1.
- **Coordinates.** Every verdict is relative to the cell decomposition and to `A` (CX-3, I-5). The
  robustness criterion (§6.4) varies `N` and `T`, not the coordinates.
- **Wakes on the infinite line.** On `ℤ` the K1 wake fills the light cone (MR★ C-2). On a ring of 5
  or 8 sites the cone wraps within a few ticks, so a ring result does not settle the infinite-line
  question.

***

## 4. Assumptions (d)

Label key: **S** physically sourced (locator given); **C[h]** conditional on the named hypothesis
`h`; **I** imposed.

### 4.1 Starting law

| Assumption | Label | Locator or reason |
|---|---|---|
| Finite `S` | C[posit (ii)] | Main:726 item (ii) |
| One time-homogeneous bijection | S, given the update | SM:106: bijectivity "is automatic for any second-order reversible dynamics" |
| Product form `μ = μ_Σ ⊗ ν` (carrier independent of background) | I | requirement 3 of #1032; DEFINITIONS preamble |
| `μ_Σ` uniform, `P` = all carrier values | I | a declared preparation; requirement 2 asks for "at least two independently available incoming carrier preparations" and gives no source for them |
| `ν_{−1} = π₀` | C[H-μ] | Main:56: "a selection principle, not uniqueness from invariance alone"; #914 c.6563412926 §0 code H-μ |
| `ν_r`, `r ≥ 0` (ready register and collar) | I, C[H-sel] | MR★ C-3: no physically sourced quiet, ready region in the sources read (as scoped by C.1-1) |
| `δ_b` (NK-K3 only) | I | HC-K3's planted marker; a countercontrol, never a candidate law |

### 4.2 Write

| Assumption | Label | Locator or reason |
|---|---|---|
| K1 as the update | C[posit (vii)] | Main:726 item (vii); SM:296; MR★ C-1 |
| The SM:112 ring rule as the update | C[E-SDC], an unadopted F2 extension | SM:112 (construction); §2.3 |
| Write tick `t₀ → t₀+1`, preparation at `t₀` | I | declared timing (DEFINITIONS preamble) |
| The carrier's value enters only through the native step | S under the update's label | no gate is added |
| `f = y_Σ(t₀)` | I, forced by the form | a copy-form step can imprint only the carrier's current slice on a disjoint register at `t₀+1`, since `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` [D] |

### 4.3 Readback

| Assumption | Label | Locator or reason |
|---|---|---|
| H-cur (declared): the current slice of `A` is readable | C[H-cur] | #914 c.6566997020 K-8 ("H-cur is declared, not native"); D-ACC (#1032 c.6611966162, OQ-3). Physical sourcing of access outstanding |
| Identity of `A` across ticks (a fixed declared region) | I | Main:88 ("the partition is fixed"); requirement 1 says identity across time "does not count" as a derived register |
| Two-slice locus `R` with current-slice read | I (amendment B-1) | the register's previous slice is physically part of its sites' state (SM:106); it is not read |
| Reading across ticks | evaluated by the analyst, not an embedded read | D-SEN: a path-law comparison "must not silently supply physical access across time" (#1032 c.6611966162) |
| No clock register | I | row 4 stays a declared constant (§6.8) |

### 4.4 Decoder

| Assumption | Label | Locator or reason |
|---|---|---|
| A deterministic decoder of the read cells, fixed at the write tick | I | Q8 (#1032 c.6621961326): "Frozen at the write tick … Never optimized using later retention outcomes" |
| Values off the write-tick support by rule D2, with D1 and D1′ as sensitivity | I, owner decision G-4 | #1032 c.6622434587 leaves this rule to be decided before Phase B |
| `ε* = 1/20` | I | owner, #1032 c.6612956983: "a preregistered engineering criterion, not a derived physical constant" |

***

## 5. Sourced versus imposed under NRR-1 (e)

The five requirements of #1032's "Precisely missing" list.

| # | Requirement | Status under NRR-1 | Why |
|---|---|---|---|
| 1 | Physical rule, not access by declaration | **Imposed.** The dynamics is native (K1) or conditional (E-SDC). The register, its identity and its readable σ-algebra are declared. | H-cur is the declared baseline; requirement 1 is not met by it (D-ACC). No state-selected or derived register is tested. |
| 2 | Nontrivial transfer | **Tested, not sourced.** The write is the native step; carrier sensitivity is NB-1 at `t₀+1` (the write gate, B-2); simple advection is rejected by TP and re-supply by RS. | The outcome depends on the computation. A positive shows transfer for the declared register and law only. |
| 3 | Availability and independence | **Imposed** for `r ≥ 0` (H-sel); **conditional** on H-μ for `π₀`. The full joint prior is stated: `μ_Σ ⊗ ν_r`. | Under `π₀`, Lemma PAD predicts no write. No source for `ν_r` exists in the sources read (MR★ C-3, C.1-1). Ready state is never inferred from the record. |
| 4 | Retention | **Tested** over gap-free windows `T ∈ {1, 2, 3}`, with `ε* = 1/20`, the `W_{T′}` extension, the recurrence rule and Lemma P's bound. Persistence, renewal and reusable supply are **not addressed**. | One-step retention is tested; multi-tick persistence beyond `T = 3` is not. |
| 5 | No circularity | **Not circular as stated, and not met.** No observer, instrument, noncommutative algebra or Born rule is assumed. The ready region is assumed, labelled, and never claimed to arise from the record. | A ready reservoir that generates itself is excluded by construction; one that is supplied is the open premise. |

***

## 6. The proposed Phase B test (f)

### 6.1 Objective and non-objectives

**Objective.** For the NRR-1 family on two in-corpus copy-form rules, decide by exhaustive exact
enumeration which tuples, if any, the Phase A classifier (amended by B-1 to B-4 and calibrated by
the controls of §6.3) assigns a storage row, and report the preparation resource each one needs.

**Non-objectives.** Sourcing any law (O1); access (O3); observers (O4); rule h; `d = 3`; clocks;
moving or adaptive registers; a D-SML ranking while `w*` is unset; any premise adoption,
SOURCE-CANDIDATE promotion, merge or publication.

### 6.2 Fixed instances and parameters

**Rules.**
- `K1`: `φ(x, y) = (y, Ay − x)`, `(Ay)_i = y_{i−1} + y_{i+1}`, over `𝔽₂`, on `ℤ/N`.
- `SMR`: `y′_i = y_{i−1} + y_{R(i,y)} − x_i`, `R(i, y) = i+2` if `y_{i+1} = 0` and `i+1` otherwise,
  over `𝔽₂`, on `ℤ/N`.
- Ring sizes `N ∈ {5, 8}`, so `|S| = 2¹⁰` and `2¹⁶`. `N = 5` with K1 is K-18(b).
- Injectivity of `φ` on `S` is checked for every instance before any tuple (exit 5).

**Carrier.** `Σ` = site 0, both slices. `μ_Σ` uniform on `𝔽₂²`. `P` = all four values. `f = y₀(t₀)`,
so `m = 2` and the blind bound is `1/2 > ε*`.

**Registers.**
- `N = 5`: all 15 nonempty `A ⊆ {1, 2, 3, 4}`.
- `N = 8`: all arcs `{a, …, a+w−1} ⊆ {1, …, 7}` with `w ∈ {1, 2, 3}`, which is 18 registers.
- A register's shape key is `(a, w)` for an arc and the site set for a non-arc at `N = 5`.

**Laws.** For `r ∈ {−1, 0, 1, 2, ∞}`:
- `ν_{−1} = π₀` on the non-carrier cells;
- for `0 ≤ r < ∞`, `ν_r` is uniform on the non-carrier cells conditioned on: both slices of every
  site at ring distance `≤ r` from `A`, other than site 0, are 0;
- `ν_∞ = δ₀` on all non-carrier cells.
- Laws with the same constraint set are evaluated once and listed under every `r` that gives
  them. `D(ν_r)` is the number of constrained bits.
- One additional law, `δ_b` of HC-K3, is used only in control NK-K3.

**Windows.** `T ∈ {1, 2, 3}`, window mode only (the extension `W_{T′}` is always computed).

**Decoders.**
- *D1* (Q8 as written): minimize the worst-case write-tick error over `P`; on read configurations
  outside the write-tick support, output the least value.
- *D1′*: as D1, with the greatest value off the support.
- *D2* (primary): as D1 on the write-tick support. Then let `~₁` be the equivalence on `config(R)`
  generated by `ℓ ~ f_R(ℓ, q)` for `q ∈ supp Q_{t₀+1}`, and give each read configuration in the
  `~₁`-class of a write-tick-supported `ℓ` the value `g(ρ(ℓ))`. If two values would be assigned to
  one read configuration, D2 is `undetermined` for the tuple, and D1's values are used off the
  support. The remaining read configurations take D1's value.
- D2 reads only `φ`, `supp R_{t₀+1}` and `supp Q_{t₀+1}`. It reads no `ε` and no tick after
  `t₀+1`.
- Each tuple is classified under D2. The rows under D1 and D1′ are recorded as `row_D1` and
  `row_D1p`, and a tuple whose three rows differ carries `decoder_sensitive = true`.

**Amendments to the Phase A decision rule.**
- **B-1, locus.** For copy-form rules, `R` = both slices of `A`, the read cells = the current slice
  of `A`, and `Q = Par(R) ∖ R` from `φ` on all of `S`. SCH ranges over the read cells.
- **B-2, write gate.** Before PREREG §4 step 1, the tuple takes row **3w (no write)** if
  `TV_{t₀+1}(σ, σ′) = 0` for every pair in `P`. Rows 2a and 2b presuppose a record; without the gate
  a blind register with a failing DIL∃ would be labelled TR or EX.
- **B-3, decoder.** D2, as above, for every NRR-1 tuple. Controls keep the decoders their
  definitions fix.
- **B-4, locality.** At PREREG §4 step 6, a storage row (5 or 6) whose environment
  `E := Λ ∖ (Σ ∪ sites(R) ∪ sites(Q))` is empty becomes row **I-5G (global register: not a local
  record)**. For the Phase A toy models, `E` is counted in cells.
- Unchanged: `ε* = 1/20`; independence and support conditioning under `μ(·|σ∈P)` (which is `μ`
  itself under `P` = all values); J-1 in the Q7-narrowed wording (P:159–166); the `G`-rule (P:440–
  452); `W_T` for storage and `W_{T′}` for TR/EX; the recurrence rule; row 4 as the declared
  constant `false`; exit 4 at step 6 only.

**Backward compatibility with Phase A [D].**
- B-2 changes no Phase A row: every Phase A tuple has `TV_{t₀+1} ∈ {1, 9/10}` (P:341–365, :383).
- B-4 changes no Phase A row: every Phase A storage tuple (S1, R3 at `T = 1`, HC-SW, MC, HC-SK at
  `k ≥ 5`) has a nonempty environment in cells. For example, MC(3) has `u₄, u₅` outside
  `Σ ∪ R ∪ Q`.
- B-1 does not apply to any Phase A model, since none is copy-form.
- B-3 does not apply to Phase A models, whose decoders are part of their definitions.
- These are inspections of the frozen tables, to be re-checked by the reviewer; they are not runs.

**Tuple count.** Per rule, at most `15 × 5 × 3 = 225` tuples at `N = 5` and `18 × 5 × 3 = 270` at
`N = 8`, before laws are deduplicated. At most 990 NRR-1 tuples, plus the controls of §6.3.

### 6.3 Controls

All controls run first, in a fixed order, and the run halts at the first mismatch (exit 1). Their
expected values are hand derivations [D] that the reviewer re-derives. No native verdict text is
rendered unless every control is green.

| Id | Instance | Expected (compared fields) | Tests |
|---|---|---|---|
| C-INJ | every rule instance | `φ` injective on `S` | the rules as specified (exit 5) |
| C-PAD-K1 | K1, `N = 5`, `π₀`, `A = {1}`, `T = 1` | `ε_max(t₀+1) = 1/2`; `TV_{t₀+1} = 0` for all pairs; row 3w; `Q_cells = {y₀, y₂}` | Lemma PAD; B-2; B-1's `Q` |
| C-PAD-SMR | SMR, `N = 5`, `π₀`, `A = {1}`, `T = 1` | `ε_max(t₀+1) = 1/2`; `TV_{t₀+1} = 0`; row 3w; `Q_cells = {y₀, y₂, y₃}` | Lemma PAD on the nonlinear rule; state-dependent `Par` |
| C-PAD-ALL | every NRR-1 tuple with `r = −1` | `TV_{t₀+1} = 0` for all pairs, and row 3w | Lemma PAD as a universal prediction over all such tuples |
| NK-W | K1, `N = 5`, `δ₀`, `P` all values, `A = {1,2,3,4}`, D2, `T = 1` and `T = 2` | `Q_cells = {y₀}`; J-i fails at `t₀+1`; row 1 at both `T`; `ε_max(t₀+1) = 0`; `TV_{t₀+1}(σ, σ′) = 1` if `y₀ ≠ y₀′` and 0 otherwise | RS on a native rule; the carrier's previous-slice channel (`y₀(t₀+1) = x₀`) |
| NK-Wq | K1, `N = 5`, `δ₀`, `P = {(0,0), (0,1)}`, `A = {1,2,3,4}`, decoder fixed as `OR(y_A)`, `T = 1` and `T = 2` | `T = 1`: DIL∃ holds, `τ = ∞`, SCH fails at `t₀+1`, pre-gate row 6, row I-5G; `ε = 0, 0`. `T = 2`: J-i fails at `t₀+2`, row 1; `ε = 0, 0, 0` | B-4; the W1 blind spot; the reason for `T* = 2` |
| NK-K3 | K1, `N = 5`, `δ_b`, `P` all values, `A = {1,2,3,4}`, HC-K3's decoder, `T = 1` | `ε_max = 0, 0`; J-i fails at `t₀+1`; row 1 | countercontrol (g) (R:154–161, :325–326) |
| DEC-SW | HC-SW model (PREREG §3.1, `T = 1`) | D2 table `{00:0, 01:1, 10:1, 11:0}`; `d2_status = consistent`. No retention is evaluated | D2 recovers a circulating decoder |
| DEC-TS | HC-TS(4) model | D2 `undetermined`; table `{00:0, 10:1, 01:0, 11:0}` (D1). No retention is evaluated | D2 falls back on transport |

**Positive-path coverage.**
- NK-Wq at `T = 1` reaches the storage step (row 6 before B-4) on a native rule.
- DEC-SW shows D2 reproducing the decoder that gives HC-SW its row 6 in Phase A.
- Row 5 (static storage) has no Phase B control unless the owner admits regression tuples (G-10).

**Hand derivations behind the native controls [D].**
- *NK-W.* Under `δ₀`, HC-K1 gives `y(t₀+1) = (x₀, y₀, 0, 0, y₀)`. With the two-slice locus on sites
  1–4, `Q = {y₀}` (site 0 is the only outside neighbour of the arc 1–4 on `ℤ/5`). `Q_{t₀+1} = x₀`
  varies with `κ = (x₀, y₀)`, so J-i fails at `t₀+1 ∈ H_T` for every `T ≥ 1`, and step 2 assigns
  row 1. On the write-tick support `{0000, 1001}` any write-tick decoder gives `ε_max(t₀+1) = 0`.
- *NK-Wq.* §1.3, Observation W1. `y(t₀+3) = (0, c, c, c, c)` gives `ε_max(t₀+3) = 0` under `OR`.
- *NK-K3.* Under `δ_b` (`x₂ = x₄ = 1`, all else 0), `y₀(t₀+1) = y₄(t₀) + y₁(t₀) + x₀(t₀) = x₀`, so J-i
  fails at `t₀+1`. The decoder values are R:155–159.
- *C-PAD-SMR's `Q`.* `y′₁ = y₀ + y₃ − x₁` if `y₂ = 0` and `y₀ + y₂ − x₁` otherwise, and `x′₁ = y₁`. So
  `Par(R) = {y₀, y₁, y₂, y₃, x₁}` and `Q = {y₀, y₂, y₃}`.

**Countercontrols (a)–(f) of #1032, and (g), (h).**

| Countercontrol | How Phase B meets it |
|---|---|
| (a) bare previous-slice copy / H-2s | Read cells are the current slice only. The previous slice is in `R` (B-1) but never read. |
| (b) static declarative decoder | The decoder is fixed by D2 from `φ` and write-tick supports. Its sensitivity to D1 and D1′ is recorded per tuple. NK-K3 shows a declared decoder that reads a planted clock is rejected by RS. |
| (c) quiet background imported through the prior | Not avoided: `ν_r` is that import, labelled H-sel. Its size is reported as `D(ν_r)` and `2^{−D}`. A positive at radius `r` is conditional on it. |
| (d) moving readout fixed in advance | Not used: `A` is fixed, and there is no clock. |
| (e) passive wave or wake | TP and RS. NK-W and NK-Wq are native wake controls. |
| (f) conditioning that makes the carrier indistinguishable | `P` is all carrier values, `f = y_Σ(t₀)`, and the write gate B-2 reports a blind register as row 3w. Lemma PAD predicts it for `π₀`, and C-PAD-ALL checks it. |
| (g) fixed decoder that reads a tick marker | NK-K3. |
| (h) a duplicated passing pulse | HCP-h [PA] (row 1, P:349). Under B-1 the analogous native case is NK-W. |

### 6.4 Decision rule (preregistered: rules, not numbers)

**Per tuple.** PREREG §4's steps 0–8 with amendments B-1 to B-4, in this order:
0. recurrence flags (readback mode and PREREG's noext step 1 are not used: every tuple is in window
   mode);
1. B-2 write gate (row 3w);
2. RS (row 1) if J-1 fails at a hold tick of `H_{T′}`;
3. TR (2a) or EX (2b) if `τ < ∞` and `ε_max > ε*` at some tick of `W_{T′}`;
4. no retention (row 3);
5. row 4 (declared `false`);
6. storage if ST holds, then B-4 (I-5G) and SCH (row 5 or 6);
7. TI (row 7) if `ε_max = 0` on `W_T`;
8. I-6 (row 8).

**Per rule (the mechanism verdict).** Computed from `summary.json` fields only.
- **VOID** if any control mismatches, any exit is nonzero, or C-PAD-ALL fails anywhere. No
  mechanism verdict is rendered.
- A tuple **counts** iff its D2 row is 5 or 6 and `T ≥ T*`, with `T* = 2` by default (G-5).
- **STORAGE-ROBUST[rule]** iff some register shape key and some `r ≤ 2` count at both `T = 2` and
  `T = 3`, and at both `N = 5` and `N = 8`, wherever the shape exists at both sizes.
- **STORAGE-ISOLATED[rule]** iff some tuple counts and none is robust.
- **NO-STORAGE[rule]** iff no tuple counts.
- Every verdict also reports, separately: tuples with storage at `T = 1` only; I-5G tuples;
  decoder-sensitive tuples; tuples whose only storage is at `r = ∞`; and the full row tally by
  (rule, `N`, `r`, `T`).

**Verdict text.** Rendered from `summary.json` by fixed templates, for example "Phase B, `<rule>`:
`<verdict>`; `<k>` of `<n>` tuples count; smallest ready radius among counting tuples `<r>`
(`D` = `<bits>` bits)." The templates are frozen with the preregistration, and a check step
regenerates the text and compares it byte for byte (§A.44).

**Interpretation, fixed in advance.**
- STORAGE-ROBUST on K1: a conditional witness of one-step register-level retention under native
  dynamics, CONDITIONAL[H-sel (`ν_r`, `D` bits), H-cur (declared), D2, J-1 and DIL∃ as calibrated].
  Not a SOURCE-CANDIDATE. It would be subjected to §6.8's skepticism checks before any further
  step.
- STORAGE-ROBUST on SMR only: the same, also CONDITIONAL[E-SDC].
- STORAGE-ISOLATED: a reported witness whose dependence on `N` or `T` is itself the finding. No
  mechanism claim.
- NO-STORAGE: a scoped negative (§6.7).

### 6.5 Positive and negative controls, summarized

- *Negative (must reject):* C-PAD-K1, C-PAD-SMR, C-PAD-ALL (no write); NK-W, NK-K3 (re-supply);
  NK-Wq at `T = 2` (re-supply after a one-tick pass); NK-Wq at `T = 1` (global register).
- *Positive path (must reach storage):* NK-Wq at `T = 1` before B-4.
- *Decoder rule:* DEC-SW (D2 consistent), DEC-TS (D2 undetermined).
- *Optional regression (owner decision G-10):* S1(2) (row 5) and HC-SW at `T = 1` (row 6) with their
  frozen decoders and their expected values read from `PHASEA-EXPECTED.json` at `F`.

### 6.6 Resource reporting (D-SML)

For every counting tuple, the record carries one row of OQ-8's table:
- added dynamical assumptions: none (K1) or E-SDC (SMR);
- access and clock: H-cur (declared) on the current slice of `A`; no clock;
- preparation restriction: `ν_r`, `r`, `D(ν_r)` in bits, and `2^{−D(ν_r)}`;
- register and interaction size: `|A|`, `|Q|`, the rule's range;
- write probability: under the conditioned law the native write occurs with probability 1, since
  there is no trigger; the probability that `π₀` produces the ready region is `2^{−D(ν_r)}`;
- retention duration `T` and `T′`; `ε_max` and `TV` at every tick; failures (D-MET item 4).

No ranking is issued while `w*` is unset (P:223). For NRR-1 the write probability under `π₀` and
the ledger are one quantity, so OQ-8's rule that "a vanishing write probability must not win
merely by reducing the preparation ledger" is met by reporting both and ranking by neither.

### 6.7 Possible outcomes and what each would and would not establish

| Outcome | Would establish | Would not establish |
|---|---|---|
| VOID (a control red, C-PAD-ALL fails, or an exit) | that the implementation, the hand algebra or a convention is wrong | anything about native retention |
| NO-STORAGE on both rules | for K1 and SMR on rings `N ∈ {5, 8}`, `q = 2`, one-site carrier, these registers, these laws, `T ≤ 3`, `ε* = 1/20`, H-cur, D2 and the amended classifier: no tuple is assigned storage | a no-go for native retention; anything at `d = 3`, other `N`, `q` or `a`; non-arc registers at `N = 8`; moving, derived or clocked registers; other laws; rule h; observers |
| NO-STORAGE on K1, STORAGE-ROBUST on SMR | a conditional native-form witness, conditional on E-SDC and H-sel, of the kind route II calls UNDECIDED | that E-SDC is the physics (§A.29: no independent consequence); a source for `ν_r`; access |
| STORAGE-ROBUST on K1 | a conditional witness under posit (vii) and H-sel | sourcing, access, persistence beyond `T = 3`, `d = 3` |
| Storage only at `r = ∞` | that local readiness of radius 2 does not suffice in these instances | anything about larger radii on larger rings |
| Storage only at `T = 1` | the W1 pattern recurring; no counting tuple | retention |
| Every `r = −1` tuple row 3w, as predicted | Lemma PAD's prediction holds on these instances (a consistency check) | anything about laws that restrict `x_A` |
| All storage decoder-sensitive | that the verdict depends on the off-support decoder rule | storage |

A negative or inconclusive result is acceptable if its scope is precise (owner, #1032
c.6610742427). No outcome moves a correctness band: every outcome sits on the consistency axis
until a counting tuple is confronted with something independent of its construction (§A.23).

### 6.8 Skepticism on a favourable outcome (§A.31)

Fixed before any run, for any counting tuple:
1. Re-derive the tuple by hand from its recorded classes, `Q` supports and `ε` values, and check
   Lemma H's direction (F-2, D:496–497).
2. Check that `Q` at every hold tick is the current slice of outside neighbours only, and that no
   previous-slice cell of `A` is read.
3. Check decoder sensitivity: report the D1 and D1′ rows.
4. Check that the counting tuple's environment `E` exceeds one site, and report `|E| / N`.
5. Check whether the counting tuple's DIL∃ certificate rests on an input fixed only by `ν_r` at
   ticks inside `W_T` (the W1 pattern), by reporting `𝒬_{W_T}` by tick.
6. Check whether a φ-invariant global functional is being read (S-C4b [MR]): a register covering
   the support of an invariant functional is not a local record.
7. Report the result as CONDITIONAL with every hypothesis in §4 carried into it.

### 6.9 Invariant → checkpoint (§A.41)

| Invariant | Checkpoint |
|---|---|
| exact rationals; no floating point in a verdict | schema check on every probability field (regex as P:529); exit 2 |
| the frozen Phase B inputs are those reviewed at `F_B` | git blob ids at `F_B` compared with loaded bytes at start; exit 3; recorded in every output |
| Phase A's frozen files are read only | the tool opens them read only, and the job's final step checks their blob ids at the run commit against `F`; exit 3 |
| every rule instance is a bijection | C-INJ; exit 5; `injective` per tuple |
| the tuple family is fixed in advance | the family is generated from the frozen parameter file; its canonical list's hash is in the freeze and in `summary.json`; `tuples_evaluated` equals the list |
| controls first, halt on first red | controls carry the first orders; `first_failure`; exit 1 |
| Lemma PAD checked on every `r = −1` tuple | per-tuple assertion `pad_ok`; exit 1 on failure |
| decoder fixed at the write tick | D2 is computed by a function whose recorded inputs are `φ`'s id, `supp R_{t₀+1}` and `supp Q_{t₀+1}`; their hash and the decoder table's hash are in each record |
| no decoder reads a later tick | the self-test runs D2 on a tuple whose later ticks are altered and checks the table is unchanged |
| B-1 locus | `Q_cells` per tuple; NK-W and C-PAD controls compare it |
| B-2 write gate | `TV_t0p1` per pair and `write_gate` per tuple; C-PAD controls |
| B-4 LOC | `E_sites` per tuple and `row_pre_loc`; NK-Wq compares it |
| Lemma P consistency | `n_supp` per tuple; a storage row with `T′ ≥ n_supp − 1` exits 6 |
| `T*` used only in the mechanism verdict | `T_star` in `summary.json`; the regeneration step recomputes `counts` from per-tuple rows |
| decoder sensitivity recorded | `row_D1`, `row_D1p`, `decoder_sensitive` per tuple |
| mechanism verdict from structured data | a check step recomputes the verdict and its text from per-tuple JSON and compares byte for byte |
| one pass, no adaptive extension | host run record `run_attempt = 1`; no tuple outside the frozen list |
| resource limits | each shard's `timeout-minutes`; its conclusion read from the host |

### 6.10 Output schema (§A.44)

**Per tuple:** `phase-b/<tuple_id>.json`, schema `oret-phase-b/1`, with:
- identity: `tuple_id`, `order`, `rule` (`K1` or `SMR`), `N`, `q`, `Sigma`, `A`, `shape_key`,
  `locus` (`two-slice`), `read_cells`, `Q_cells`, `r_values`, `law`, `D_bits`, `p_ready` (`2^−D`),
  `P`, `f`, `T`, `T_prime`, `ticks`;
- decoder: `decoder_rule` (`D2`), `d2_status`, `decoder_table`, `decoder_inputs_hash`, `row_D1`,
  `row_D1p`, `decoder_sensitive`;
- metrics: `eps` and `TV` per tick (rational strings); `TV_t0p1` per pair; `failures`;
- criteria: `Ra`, `Rb`, `write_gate`, `J1` per hold tick, `SCH` per hold tick, `DIL`, `tau`,
  `classes_T`, `Q_supp_by_tick`, `G_star_T`, `G_star_Tprime`, `G_status`, `eta`, `lemma_h_bound`,
  `recurrence_flags`, `n_supp`, `E_sites`, `pad_ok` (for `r = −1`);
- result: `row_pre_loc`, `row`, `counts` (Boolean);
- `expected` and `comparisons` for control tuples only;
- `frozen_inputs`, `run`.

**`summary.json`:** `schema`, `tuples_frozen`, `family_hash`, `tuples_evaluated`, `first_failure`,
`controls_green`, `exit`, `eps_star` (`"1/20"`), `T_star`, `w_star` (`null`), a row tally per
(rule, `N`, `r`, `T`), the per-rule mechanism verdict, the lists named in §6.4, and `verdict_text`.

**Exits.** 0 complete; 1 control mismatch or `pad_ok` false; 2 schema or floating point; 3 a
frozen input differs from its blob id; 4 `G*` undetermined at the storage step; 5 injectivity or
method check; 6 Lemma P inconsistency; other nonzero error. A verdict reads exit statuses, the
host's job and step conclusions, and `summary.json`; never log text.

### 6.11 Budget and execution form (for a later authorization)

- CI only (§A.40), sharded by (rule, `N`), with the controls in every shard's prefix. One pass; no
  adaptive extension; halt on first red.
- The largest state space is `2¹⁶`, as in Phase A. The run time is not estimated here: nothing was
  run. A later implementation unit states a measured bound from its self-test before any dispatch
  request.
- Implementation reuse: `phaseA/phasea.py` provides exact enumeration, J-1, DIL∃, `τ`, the
  `G`-rule and §4 row assignment (IMPLEMENTATION-NOTES §1). A Phase B tool would import nothing it
  cannot hash-pin and would add B-1 to B-4, D2, `n_supp`, LOC and the mechanism verdict. Whether
  Phase A's tool may be imported is G-10.

### 6.12 Hard-to-vary checks (§A.29)

- **Nothing new is adopted.** The F2 items are E-SDC (unadopted, tested only as a named hypothesis)
  and `ν_r` (imposed, H-sel). Neither is presented as established, and a positive under either is
  conditional on it.
- **Results the amendments preserve, stated in advance (their controls).** Every Phase A row and
  value: B-1 and B-3 do not apply to Phase A models, and B-2 and B-4 change no Phase A row (§6.2,
  by inspection). The design asks the reviewer to confirm this from `PHASEA-EXPECTED.json`.
- **Independent prediction.** The amendments come with one prediction not used to build them:
  Lemma PAD's exact values on every `r = −1` tuple of both rules (C-PAD-ALL), including the
  nonlinear rule, on which nothing in Phase A was calibrated. NRR-1 itself makes no independent
  prediction. So even a robust positive could not be adopted; it would be a conditional witness.
- **No variant fits any outcome.** The rules, rings, registers, laws, windows, decoder rule, `T*`,
  `ε*` and verdict templates are frozen before any evaluation. The law family has one parameter,
  `r`, and every value is reported. Adding a law, register, rule, ring size or decoder after
  results is a new freeze, and a robust positive must hold at two ring sizes and two windows.
- **Refuting outcomes for the design.** C-PAD-ALL failing on any tuple refutes Lemma PAD or the
  implementation. NK-Wq at `T = 1` assigned anything other than I-5G refutes Observation W1 or the
  implementation. Either halts the run.

***

## 7. Owner decisions needed (g)

Each has a recommended default; under the defaults the test of §6 is decision-complete.

- **G-1. Rules.**
  - (a) K1 and SMR. *Default.*
  - (b) K1 only (native under posit (vii), no F2 extension).
  - (c) Add rule h through a non-exhaustive method, which would be a separate design.
- **G-2. SMR's status.**
  - (a) Test it under the named, unadopted extension E-SDC. *Default.*
  - (b) Exclude it until E-SDC has a hard-to-vary form.
- **G-3. Register locus for copy-form rules.**
  - (a) Two-slice locus, current-slice read (B-1). *Default.*
  - (b) Phase A's convention (the read set as `A`; the previous slice in `Q`).
  - (c) Both, reported side by side; the verdict under (a).
- **G-4. Decoder off the write-tick support (Q8's deferred rule).**
  - (a) D2, with D1 and D1′ recorded. *Default.*
  - (b) D1 only (Q8 as written; HC-SW-type circulation is then rejected).
  - (c) Count a tuple only if D1, D1′ and D2 agree.
- **G-5. `T*` and `w*`.**
  - (a) `T* = 2`, with `T = 1` reported only; `w*` unset, with `2^{−D}` reported. *Default.*
  - (b) `T* = 1` (the owner's one-step reading, accepting the W1 blind spot).
  - (c) `T* = 3`.
- **G-6. Laws and preparations.**
  - (a) `ν_r`, `r ∈ {−1, 0, 1, 2, ∞}`; `P` all carrier values; `δ_b` in NK-K3 only. *Default.*
  - (b) Also `P` with the carrier's previous slice fixed to 0, as a separate, labelled family.
  - (c) A different ready-region shape (for example one-sided).
- **G-7. Write gate B-2.** (a) Adopt. *Default.* (b) Keep Phase A's precedence, under which an
  unwritten register can be labelled TR or EX.
- **G-8. Locality gate B-4.**
  - (a) Nonempty environment. *Default.*
  - (b) An environment of at least `|A|` sites, for NRR-1 tuples only. This changes no Phase A
    row, since it is not applied to the toy controls.
- **G-9. Robustness.**
  - (a) Both `N` and both `T ∈ {2, 3}`, at one `r ≤ 2`. *Default.*
  - (b) Both `N` only.
- **G-10. Phase A material.**
  - (a) No Phase A tuple is re-evaluated. Row 5 then has no Phase B control. *Default, in line with
    "Do not repeat Phase A".*
  - (b) Admit S1(2) and HC-SW at `T = 1` as regression controls, labelled as implementation checks
    and not as Phase A results. This may count as a replay under D9 (#1032 c.6629059049).
  - Separately: whether a Phase B tool may import `phaseA/phasea.py` at its landed blob
    (`3d5edd97`).
- **G-11. Scope extensions, each a separate design if wanted.**
  - K1 on a `d = 3` torus by exact linear algebra over `𝔽₂`. Every `ν_r` is uniform on a subspace,
    so supports and J-1 reduce to rank computations; it would be validated against full
    enumeration at `N = 5, 8`.
  - Larger rings, `q > 2`.
- **G-12. Governance form.** (a) A research run on a disposable branch, with an owner-designated
  freeze `F_B`, as for Phase A. *Default.* (b) A native V3 round under §A.39.
- **G-13. Review of the inherited premises.** Whether the lemmas of `ROUTES.md` used as hand checks
  here (S′, Q, L, P, H) need a review record on `main` before Phase B's freeze, or only the specific
  derivations of §1.3 and §6.3.

***

## 8. Review packet

The independent reviewer is asked to check, at the exact head:

1. **§1.1.** The 49/49 count against `summary.json`, `RESULT.md:42–49` and `REVIEW.md:9–11`, and
   each quotation verbatim.
2. **Lemma PAD (§1.3).** The proof; that K1, SMR and rule h have the stated copy form; that `κ` is a
   function of `W`; and that the conclusion covers approximate retention as stated.
3. **Observation W1 (§1.3) and NK-Wq.** `y(t₀+1)`, `y(t₀+2)`, `y(t₀+3)` on `ℤ/5`; the two-slice orbit
   of period 5; DIL∃ on `W₁`; `τ = ∞`; SCH failing at `t₀+1`; J-i failing at `t₀+2`.
4. **NK-W, NK-K3, C-PAD-K1, C-PAD-SMR.** Each expected value and row, and each `Q_cells`.
5. **DEC-SW and DEC-TS.** The D2 classes and tables.
6. **Backward compatibility (§6.2).** That B-2 and B-4 change no Phase A row, from
   `PHASEA-EXPECTED.json` at `F`; in particular the environments of MC(3) and HC-SK.
7. **Precedence.** That inserting the write gate before RS, and LOC inside step 6, keeps PREREG §4's
   coverage argument (D:391–399): every tuple still takes exactly one row.
8. **D2 and Q8.** Whether D2's use of `supp Q_{t₀+1}` respects "never optimized using later
   retention outcomes".
9. **The claim/evidence boundary.** That no statement presents NRR-1, E-SDC or `ν_r` as
   established; that §6.7 scopes every negative to the class tested; that "smallest" in §2.2 is
   argued from added structure, not proved minimal.
10. **§2.3.** The labels: K1 native under posit (vii); SMR an F2 extension E-SDC as physics; rule h
    outside posit (vii).
11. **§9.** Each off-`main` reference and its classification.
12. **Feasibility.** Whether the stated instance set is enumerable at `2¹⁶` per state space as in
    Phase A. No run time is claimed.

***

## 9. References off `main`, and literature (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1032 comments (6610742427, 6611966162, 6612956983, 6614257383, 6621961326, 6622018720, 6622434587, 6623962802, 6628404473, 6629059049, 6649418760) | owner decisions and authorization, quoted | provenance; owner records quoted with author and time where relied on |
| #914 c.6563412926, c.6566997020, c.6612951653, c.6562546850, c.6563417740, c.6561476122 | matrix rows, K-8, H-μ, the annotation, K1-PERS-1 scope, rule h's statement | provenance. Rule h's definition used here is the one on `main` (`INTERFACE-CONTRACT.md`) |
| PR #1078 (closed) and its reviews | the review history of `ROUTES.md` and DESIGN-PULSE | provenance. The texts used are on `main` at `F`; their reviews are not, so they are labelled [R] and [DP] and used as motivation only |
| PR #1093 (merged) | how Phase A's evidence reached `main` | provenance; the evidence itself is on `main` |
| `research/o-obsmu-20261104` at `f67b9f0c`, `ANALYSIS.md` §4.4 and §4.6.2 | the name P-SDC; the reading that retained records on K1 are tied to O-RDY | provenance. No claim here uses its content as support: E-SDC is stated from SM:112 on `main`, and the readiness point rests on MR★ C-3 on `main` |
| #1110, #1112 | the O-OBSMU review status; the arrow-of-time pointer | provenance |
| `REVIEW-Q7.md` | cited by PREREG for the J-1 wording | not located (programme `README.md:37–43`); the wording used is the one frozen in PREREG §2.7 on `main` |

**Literature.**
- J. T. Lizier, M. Prokopenko, A. Y. Zomaya, "A framework for the local information dynamics of
  distributed computation in complex systems", arXiv:0811.2690v2 (v1 2008-11-17, v2 2013-10-10).
  **Read directly: abstract page only.** It states that "blinkers embody information storage" and
  "particles are information transfer agents" in cellular automata. Its measures are statistical
  and per cell; they are closest to SCH and ICH here, and they do not separate a blinker held by a
  quiet neighbourhood from one re-supplied by it. Not used as support.
- Landauer 1961, Bennett 1982 (as in `SOURCES.md`); Fredkin and Toffoli 1982; Toffoli and Margolus,
  *Cellular Automata Machines* (1987), on second-order reversible rules; Margolus's billiard-ball
  model, on memory by circulation: **cited from memory, not re-read.** None is used as support.
