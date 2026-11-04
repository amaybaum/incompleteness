# O-RET Phase A preregistration: exact replay of the pulse-design controls

**Status.** WIP / UNVERIFIED preregistration, revision r3. Candidate freeze; frozen on the owner's designation of the
exact commit `F`. **Not authorized to run.** A run needs the owner's go on the reviewed `F` (#1032, Q9).
- **Frozen inputs at `F`**, all in this directory:
  - this file, `PREREG-PHASE-A.md`;
  - `DESIGN-PULSE.md`, at design revision r6;
  - `PHASEA-TUPLES.json`, the tuple list, total order, models, decoders and compared fields;
  - `PHASEA-EXPECTED.json`, the expected rows and values.
- The design was reviewed ACCEPT at `e8dfe25e`. r4 and r5 were checked by the freeze reviews of `6735ef89`. r6 applies
  those reviews and is unreviewed.
- Owner decisions: #1032, 2026-11-03/04. Q7 review: `REVIEW-Q7.md` (2026-11-04).

Support labels: **[D]** derivation in DESIGN (`D:n` = line of `DESIGN-PULSE.md` at `e8dfe25e`; `r6:n` = line of
`DESIGN-PULSE.md` at r6). **[C]** checkpoint text in ROUTES.md or DEFINITIONS.md. **[O]** owner decision, #1032. **[U]**
unreviewed: a derivation or specification made here, or wording frozen from the Q7 review.

***

## 1. Objective and non-objectives

**Objective.** Replay, by exhaustive exact enumeration, every control instance of DESIGN §8 Phase A (D:537–549,
r6:563–575), plus the controls the Q7 review adds and CX-4b. For each tuple, check two things: that the assigned §4 row
(r6:386–418) equals the frozen expected row, and that every frozen hand-derived value is reproduced exactly. The aim
is to establish that the test correctly distinguishes storage from transport before it is applied to OI's native
dynamics [O, #1032 c.6622018720].

**Non-objectives.** The run does not cover:
- K1 or any native rule;
- a nonlinear target;
- Phase B;
- a D-SML resource ranking;
- choosing `w*` or `T*`;
- a new premise;
- SOURCE-CANDIDATE promotion;
- merge or publication.

"Demonstrating a register-level invariant under an imposed preparation is not the same as deriving the physical
availability of that preparation." [O]

**What a full pass establishes.** On these toy instances, under the conventions of §2, exact enumeration reproduces
the hand derivations of DESIGN §3 and §6 and of §3 below, and the implemented §4 precedence assigns the hand-assigned
rows. This is a result on the consistency axis (§A.23).

**What a full pass does not establish.** Any retention mechanism. O1, O3 or O4 (D:23–32). That the criteria classify
correctly outside the control set (§9). Any movement of a correctness band. A failed or void run establishes nothing
about OI. It identifies a hand-algebra error, an implementation error or a convention gap, and that is diagnosed
off-run. Any re-run is a new freeze.

***

## 2. Frozen preconditions

### 2.0 Conventions common to every tuple

- **Tolerance.** `ε* = 1/20` exactly [O]. Every comparison `≤ ε*` and `> ε*` is exact.
- **Window.** `W_T = {t₀+1, …, t₀+1+T}`, with hold ticks `H_T = {t₀+1, …, t₀+T}` [C].
- **Window convention (nit 2) [O].**
  - Storage certification uses `W_T`: exact DIL∃, DIL∃-η, the Lemma H bound, ST and SCH.
  - TR/EX classification uses the evaluated extension `W_{T′}`: `𝒬_{W_{T′}}`, `𝓛_{W_{T′}}` and the `G`-consistency
    test.
  - `τ` is computed from `𝒬_{W_T}` and `𝓛_{W_T}` (r6:163–169).
- **Evaluated ticks.**
  - Window mode: `W_{T′}`, with hold ticks `H_{T′}`.
  - Noext mode: `W_T`, with hold ticks `H_T`.
  - Readback mode: the listed readback ticks.
- **Preparations.**
  - For the one-bit carriers, `P` is both carrier values, so `μ(·|σ∈P) = μ`.
  - For the channel models (S1, HC-SW, HC-SK, HC-R3, MA, MB, MD), `P` is the two fired preparations.
  - The carrier law `μ_Σ` is uniform on Σ's configurations, and `κ := σ` [U, Q7 F2].
- **Independence law [U, Q7 F2].** Every independence statement of J-1 (and S-1) is evaluated under
  `μ^P_t := μ_t(· | σ ∈ P)`.
- **Support conditioning [U, a separate convention, not fixed by Q7 F2].**
  - `supp Q_t`, `supp R_t`, and so `𝒬`, `𝓛`, and also `C_t` and `η`, are evaluated under `μ^P_t` too.
  - This decides `𝒬`, DIL∃, `τ` and `G*` wherever the support under `μ` differs from that under `μ^P`. In Phase A
    that can happen only in the channel models, whose `P` omits the unfired preparations.
  - The rows under the unconditioned alternative are not derived here, except HC-R3 on `W₂`, which would be RS
    (r6:357–359).
- **Metrics.** `ε_max(t) := max_{σ∈P} μ(g(A_t) ≠ f(σ) | σ)`, and `TV_t` is that of the two `σ`-conditioned laws of the
  full readout `A_t` (D-MET [C]).
- **Dependence [U, Q7 F1].**
  - `B_t := Q := Par(A) ∖ A`, computed from `φ` on all of `S`. This repairs the ill-posed "on the support" text of
    DEFINITIONS:77–78 (D0, D:57–64). The law enters only through the joint law of `(κ, A_t, B_t)`.
  - `Q` is always built from `A` as a whole.
  - The read cells, over which SCH ranges, are listed per tuple in `PHASEA-TUPLES.json`. `A` equals its read set
    except in TMP (read cell `u₂`) and CX-4b (read cell `r`).
- **Arithmetic.**
  - Probabilities are exact rationals, computed from exact integer counts over the enumerated support with exact
    rational weights.
  - Any floating-point value in the verdict path is a failure (§5, exit 2).
- **Enumeration method [U].**
  - *Full:* every state of `S`. This is used for every tuple with `|S| ≤ 2¹⁶`.
  - *Sequential:* exact sequential marginalization. This is used only for the six HC-SK tuples with `|S| > 2¹⁶`:
    `(k, T) ∈ {(3,3), (5,2), (4,3), (6,2), (5,3), (6,3)}`.
    - At each tick, the law of `(σ, r)` is updated by the exact law of the arriving cell, which is fresh and
      independent.
    - It is valid because the law at `t₀` is a product over cells, and with `L = T+1` no cell enters `Q` at any hold
      tick of `H_T` more than once.
    - The program checks both conditions from `φ` and the law, and exits 5 if either fails.
    - It emits every compared field.
  - *Validation:* every HC-SK tuple with `|S| ≤ 2¹⁶` is computed by both methods, and all compared fields must agree
    exactly (exit 5 otherwise). These tuples run before the six sequential tuples.
- **Not computed in Phase A:**
  - cuts (Q6);
  - tick-ordered DIL∃ (Q3);
  - ICH, CHC, ABL and S-1;
  - D-TRN "left";
  - the I-5 qualifier.

  None of these enters §4.

### 2.1 Q1, circulation [O]
Closed circulation within a fixed `A`, with a stable decoder and no external re-supply, is register-level storage.
It is not static cell storage. Operationally this is r6 row 6 (r6:409): ST without SCH, with row 1 failing. HC-SW and
mutation (c) are expected in row 6. The identifier `I-4` is kept and only the label changes.

### 2.2 Q2, DIL∃ [O]
- DIL∃ is admitted as a sufficient structural certificate.
- Its counterfactual evaluations of the unmodified `φ` on all of `config(R)` are mathematical analysis. They are not a
  physically implemented measurement.
- Passing certifies invariance on `W_T` (Lemma H, D:99–104).
- Failing never yields TR or EX by itself: §4 step 3 requires an observed `ε_max > ε*` on `W_{T′}`.

### 2.3 Q3, supports [O]
`𝒬` is the pooled union of `supp Q_t` over the hold ticks of the window concerned. Tick-ordered results are not
computed in Phase A.

### 2.4 Q4, transit window [O]
- `T′ = max(T, τ)` if `τ < ∞`; otherwise `T′ = T`.
- `τ` is computed exactly (r6:163–167).
  - For each start `ℓ ∈ supp R_{t₀+1}`, let `ℛ₀(ℓ) = {ℓ}` and `ℛ_k(ℓ) = {f_R(x, q) : x ∈ ℛ_{k−1}(ℓ), q ∈ 𝒬_{W_T}}`.
  - A *hit* at step `k ≥ 1` is an `ℓ` and an `ℓ_k ∈ ℛ_k(ℓ)` with `ℓ_k ∈ 𝓛_{W_T}` and `g(ℓ_k) ≠ g(ℓ)`.
  - `τ` is the least `k` with a hit. The iteration stops when the family `(ℛ_k(ℓ))_ℓ` repeats an earlier family, and
    `τ = ∞` if no hit occurred before the first repeat.
- A storage row is scoped to `W_T` only. `τ = ∞` never implies storage beyond `W_T`.

### 2.5 Q5, write probability [O]
- `w := 2⁻ᵏ` is the probability under the unconditioned `π₀` that the write trigger fires at `t₀`. This is D-SML's
  declared write event, and DEFINITIONS:239 gives `w = 1/2` at `k = 1`.
- `w_chg := w/2 = 2⁻ᵏ⁻¹` is the probability that the write actually changes the record bit.
- ROUTES:460 reads "a trigger on `k` presence bits lowers the ledger to `log(2^k/(2^k−1))`, at write probability
  `2^{−k−1}`". DEFINITIONS:250 restates "at write probability `2^{−k−1}`". Both label `w_chg` as "write probability".
  That label is superseded for this design and this preregistration by the definitions above. ROUTES.md and
  DEFINITIONS.md are unchanged under this authorization.
- HC-SK uses the two quantities as follows:
  - `η` per hold tick `= w` (the arriving cell's trigger);
  - the Lemma H bound `= T·w`;
  - `ε_max(t₀+2) = w_chg`;
  - `w` and `w_chg` are reported, and neither is compared with any threshold.

### 2.6 Q6, cut test [O]
The cut test is a diagnostic only, with law-preserving marginal resampling, and is never native dynamics. It is not
computed in Phase A.

### 2.7 Q7, frozen wording (from `REVIEW-Q7.md`; each CONFIRMED WITH NARROWED SCOPE) [U]
- **S-1 and J-1.**
  - `B := Par(A) ∖ A`, computed from `φ` on all of `S`, and `κ := σ`.
  - Independence is evaluated under `μ_t(·|σ∈P)` at each hold tick of `W_T`.
  - S-1: every cell of `B_t` is independent of `κ`.
  - J-1: (J-i) `B_t ⫫ κ`, and (J-ii) `κ ⫫ B_t | A_t`.
  - These are inflow screens only.
  - Known false admits: advection inside `A`, and outflow.
  - Known false rejects: carrier-correlated inputs whose coupling is disabled on the support (F4).
- **Row 1's window (F6): the extension is stated [U].**
  - Row 1 also applies J-1 at each hold tick of `H_{T′} ∖ H_T` (r6:403), which extends (R-d), stated on `W_T` at
    DEFINITIONS:51. A row-1 verdict from such a tick records inflow in the extension, not re-supply over `W_T`.
  - *Choice.* Both options leave every expected row in §3 unchanged, because no Phase A tuple has a J-1 failure in
    `H_{T′} ∖ H_T`. The stated extension keeps r6 §4's precedence and coverage proof unchanged. Restricting row 1 to
    `H_T` would leave one case with no row: J-1 holding on `H_T`, failing on `H_{T′} ∖ H_T`, with a record lost. That
    would require edits to rows 2a, 2b and 7 and to the coverage proof.
- **(h).** HC-P with `A = {u₂}`, `g = u₂` on `W₁` must not be classified as retention. Expected result: J-i fails at
  `t₀+1`. The `A = {u₁,u₂}` variant is outside (h). This is control HCP-h in §3; TMP is the `{u₁,u₂}` variant.
- **Remark C.**
  - Given conditions (i)–(iii) (DEFINITIONS:58–65) and (iv), with `A ∪ K` taken as the register for (R-a)–(R-d) and
    `K` disjoint from Σ, `g′(ρ_A, ρ_K) := h(ρ_K, ρ_A)` is a fixed decoder, and Lemma S′ applies to it.
    - (iv): there is an `h` with `g_t = h(ρ_K(s_t), ·)` on `supp μ_t` for every `t ∈ W_T`.
  - The reduction holds for exact and approximate retention alike.
  - A clock whose supported readings separate two ticks of the window has support that is not φ-invariant.
  - *Superseded reading.* ROUTES:238–240 lists decoders that change with the tick as UNDECIDED. For this design and
    this preregistration, accounted-clock decoders under laws with φ-invariant support are BLOCKED[Lemma S′] for exact
    retention. ROUTES.md is unchanged.
  - No Phase A tuple has a clock decoder, so r6 row 4 is never assigned.
- **Scope notes.**
  - (F3) DEFINITIONS:82 "rejects … K1 generally" holds at K-18(b) under `δ₀` and `δ_b` only. Under `π₀` the inflow is
    padded and (R-c) excludes K1. K1 is not a Phase A instance.
  - (F8) DEFINITIONS:102 "B is empty" holds for a bare swap only. In HC-SW, `B = {p₀, v₀}`, which is quiet and
    independent at the hold ticks, and J-1 passes.
- **Effect on §3.** Every expected row in §3 is derived under this wording.
  - (F2) HC-R3 on `W₂` is EX under `μ(·|σ∈P)`. It would be RS under the full-support `μ` (r6:357–359).
  - (F4) The false-reject class affects no tuple. HC-R3's unfired branch is excluded by conditioning on `P`. Every
    other carrier-correlated `B` in §3 has an active coupling, including the returning carrier of R1 and R3 at `t₀+4`.
  - (F5) Controls HCP-h and SC are added.
  - (F1) Under `B = Par(A) ∖ A`:
    - J-1 fails only in HCP-h (J-i), SC (J-ii), R2 (J-i at every hold tick), and R1 at `T = 4` and R3 at `T = 5`
      (J-i and J-ii at `t₀+4`).
    - J-1 passes at every evaluated hold tick of every other tuple.
    - S-1 is implied by J-i and is not computed. It would fail exactly in HCP-h, R2, R1 at `T = 4` and R3 at `T = 5`.

### 2.8 Q8, decoder [O, #1032, 2026-11-04]
- Phase A uses the decoders fixed in DESIGN §3, given as truth tables in `PHASEA-TUPLES.json`. They are part of each
  control's definition and are frozen before any run.
- Q8's lexicographic tie-break is not applied in Phase A.
- The rule for decoder values on configurations unsupported at the write tick is a separate owner decision before
  Phase B.
- **Minimality.** Each listed decoder attains `write_min_eps`, the minimum over all decoders of `A` of `ε_max(t₀+1)`:
  `0` everywhere, and `1/20` for SC. This is a compared field.
  - The MD-xor exception [U] reinterprets Q8's "each such decoder minimizes …" (c.6622434587): MD-xor keeps HC-SW's
    decoder `r₁ ⊕ r₂` because the mutation fixes it. Its `ε_max(t₀+1)` is `1/2`, against a `write_min_eps` of `0`.
- Why the tie-break is excluded [U]: the off-support values decide rows.
  - With the truth-table-minimal tie-break, HC-SW gets `g(10) = 0` and becomes TR.
  - With the same tie-break, HC-TS gets `g(01) = 0` and becomes TR on `W₁` itself.
  - With the maximal tie-break, both keep their DESIGN rows.

### 2.9 Q9, authorization [O]
- Phase A only, controls only.
- The run is authorized only by the owner's go on the reviewed `F`.
- Phase B needs a separate owner decision.

### 2.10 Qualifications [O]
- `w*` and `T*` are **unset and unused**.
- The ST clause "`w ≥ w*` and `T ≥ T*`" (r6:170–171) and row 8's second clause are inactive.
- No D-SML comparison is issued.
- Both of the reviewer's nits are applied in r4 and carried into r6.

***

## 3. The frozen control set

The expected values are **replay checks of hand derivations**, which is a control function. §A.29's "rule, not
numbers" applies to the decision rule of §4, which is frozen without reference to these numbers.

**Authority.** `PHASEA-TUPLES.json` and `PHASEA-EXPECTED.json` are the run's authoritative inputs. The tables below
transcribe them. A value derived here rather than in DESIGN is marked [U].

**Compared fields.**
- Every compared field of every tuple is listed in `PHASEA-EXPECTED.json`, under the field list for its mode in
  `PHASEA-TUPLES.json`.
- In that file, `null` means the computed value must be `null`.
- A computed field that is not on the mode's list is recorded and not compared.
- In the tables, `null` means the same as in the JSON; there is no "—".

**Notation.**
- `ε` and `TV` list the values at the evaluated ticks.
- `J` lists J-1 per hold tick: `+` (both parts pass), `i−` or `ii−` (that part fails), or `i−ii−` (both fail).
- SCH lists `P` (pass) or `F` (fail) per hold tick of `H_T`.

For every tuple, (R-a) and (R-b) hold, and `f(σ) = c` is the carrier value bit (`v₀` for channel models).

### 3.1 Models

Cells are in `𝔽₂`. "Shift" means `x_j ← x_{j−1}`, with indices mod `L`. Each step's assignments are **simultaneous**:
every right-hand side reads the state before the step. This matters for MB's 3-cycle and MC's rings; a sequential
reading of MB's cycle is not a bijection. Full specifications, including the cell order, laws and decoder truth
tables, are in `PHASEA-TUPLES.json`.

- **HC-TS(L)** (D:204–229).
  - Ring `u₀…u_{L−1}`, pure shift. `Σ = {u₀}`.
  - Law: uniform on `{u₁ = u_{L−1} = 0}`.
  - `A = (u₁, u₂)`, `g = u₁ ⊕ u₂`.
- **HC-TM(m, L = m+3)** (D:231–251).
  - Rule: `u₁ ← u₁ ⊕ u₀`, then shift. Law: `u₀` uniform, all other cells 0.
  - `A = (u₁…u_m)`, `g = OR`. `T = m−1` [U: the largest exact window].
- **TMP** (D:252–255).
  - HC-TM's rule with `m = 2`, `L = 5`. Law: uniform on `{u₁ = u₄ = 0}`.
  - `A = (u₁, u₂)`, `g = u₂`, with read cell `u₂`. `T = 1`.
- **HCP-h** [U; Q7 F5; ROUTES:170–177].
  - HC-P with `L = 4`, which is HC-TM's rule. Law: uniform on `{u₁ = u₃ = 0}`.
  - `A = (u₂)`, `g = u₂`. `T = 1`.
- **SC, share completion with a biased pad** [U; Q7 F5; DEFINITIONS:98–99].
  - Cells `a, z₀, z₁, z₂`. Rule: `a ← a ⊕ z₀`, then shift `z` mod 3. `Σ = {z₀}`.
  - Law: `z₀` uniform; `n ~ Bernoulli(1/20)`, with `a = z₂ = n`; `z₁ = 0`.
  - `A = (a)`, `g = a`. `T = 1`.
  - `p = ε*` makes (R-c) hold at the boundary, which exercises exact `≤`.
  - J-ii is the only criterion that yields a rejecting row. Without J-1 the case would fall to row 8, not storage:
    `G* = {z₀ = 0}`, `η = 1/20`, and the bound at `t₀+2` is `1/10 > ε*`.
- **S1(L)** (D:259–263; HC-F [C]).
  - Channel cells `(p_j, v_j)` and register `r`. Rule: if `p₀ = 1`, swap `v₀ ↔ r`; then shift the channel.
  - `Σ = (p₀, v₀)`, and `P = {(1,0), (1,1)}`.
  - Law: uniform on `{p_{L−1} = 0}`.
  - `A = (r)`, `g = r`. `T = 1`.
- **HC-SW(T)** (D:265–280).
  - `L = 3`, register `(r₁, r₂)`. Rule: Fredkin on `(p₀; v₀, r₁)`, then `r₁ ↔ r₂`, then the channel shift.
  - Law: uniform on `{p₂ = 0, r₂ = 0}`, plus `p₁ = 0` when `T = 2` (D:274).
  - `A = (r₁, r₂)`, `g = r₁ ⊕ r₂`, and `P` as for S1.
- **HC-SK(k, T)** (D:282–308).
  - Channel cells with `k` presence bits and `v`, `L = T+1` [U: the minimal `L`, D:286], and register `r`.
  - Rule: swap `v₀ ↔ r` iff all `k` bits of cell 0 are 1; then shift.
  - Law: `π₀`. `P` is the two fired preparations `(1…1, c)`. `g = r`.
- **HC-R1** = HC-TS(4) (D:312–315).
  - Evaluated over the gap-free window `W₄` (`T = 4`), with its row given at r6:331–332, and by readback.
  - At hold tick `t₀+4`, `B = u₀(t₀+4) = u₀(t₀) = c`.
- **HC-R2** (D:317–333).
  - Cells `c, w₀…w₃`. Rule: `w₀ ← w₀ ⊕ c`, then shift `w`; `c` is unchanged. `Σ = {c}`.
  - Law: `c` uniform, `w = 0`.
  - `A = (w₁)`, `g = w₁`. In cell order, `Q = (c, w₀)`.
- **HC-R3** = S1(2) (D:335–345).
  - Evaluated at `T = 1, 2, 5` and by readback.
  - At hold tick `t₀+4` the arriving cell is `(1, c)`, and `A = r = ρ` (D:340–341).
- **MA(L)**, mutation (a) (D:568): S1(L) under `π₀`. MA(2) is HC-SK(1, 1); MA(3) is the same model with `L = 3`.
- **MB**, mutation (b) [U] (D:569).
  - HC-SW at `L = 3`, with `r₁ ↔ r₂` replaced by the simultaneous 3-cycle `(r₁, r₂, v₁) ← (v₁, r₁, r₂)`. The cycle is
    applied after the Fredkin and before the shift; `r₂` shifts out into the channel.
  - Law: uniform on `{p₂ = 0, r₂ = 0, v₁ = 0}`. `T = 1`.
  - The extra quiet `v₁` keeps the write exact, so the mutation tests DIL∃ rather than the write.
- **MC(m)**, mutation (c) [U] (D:570).
  - HC-TM(m, L = m+3) with the shift replaced by simultaneous rings:
    - inside `R`: `u₁ ← u_m`, and `u_j ← u_{j−1}` for `2 ≤ j ≤ m`;
    - outside: `u_{m+1} ← u₀`, `u_j ← u_{j−1}` for `m+2 ≤ j ≤ L−1`, and `u₀ ← u_{L−1}`.
  - The gate `u₁ ← u₁ ⊕ u₀` comes first. `T = m−1`. The carrier returns to `u₀` at `t₀+3`, outside every evaluated
    hold tick.
- **MD-xor**, mutation (d) (D:571).
  - HC-SW at `L = 3` under the law uniform on `{p₂ = 0}`, so `r₂` is uniform. `T = 1`, `g = r₁ ⊕ r₂`.
  - The tuple also carries the decoder-sweep value: the minimum, over all 16 decoders of `(r₁, r₂)`, of
    `max_{t∈W₁} ε_max(t)` [U].
- **CX-4b** [U: a concretization of D:443–454, with a ready write conveyor added].
  - Register `A = (r, s)`, `g = r`, with read cell `r`. A carrier conveyor `y₀, y₁` and an input conveyor `z₀, z₁`,
    each a ring of 2. `Σ = {y₀}`.
  - Rule: `r ← r ⊕ y₀ ⊕ (z₀ ∧ s)`, with `s` unchanged; then shift `y` and `z`.
  - Law: `y₀` uniform; `r = y₁ = 0`; `s` uniform; given `s = 0`, `z₀, z₁` i.i.d. uniform; given `s = 1`,
    `z₀ = z₁ = 0`. `T = 1`.
  - `Q = (y₀, z₀)`, and at the hold tick `(y₀, z₀) = (0, z₁(t₀))`.
  - The write is exact because `z₀ ∧ s = 0` on the support.
  - The input `z = 1`, with `s = 1`, would map `(1,1) ↦ (0,1)` but is never jointly supported with `s = 1`.

### 3.2 Expected results

These fields are also frozen in `PHASEA-EXPECTED.json` for every window and noext tuple:
- `G*` on both windows, `G_status`, and the `𝒬` sets;
- `η` and the Lemma H bound;
- the recurrence flags;
- `write_min_eps`;
- for HC-SK, `w` and `w_chg`.

`D` is the ledger in bits, `D = log₂|S| − H(μ)`, or `null` when that is not an integer.

| Tuple | `ε` | `TV` | DIL∃ | `τ` | `T′` | `J` | SCH | `D` | Row | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| TS(4), TS(5), T=1 | 0, 0, 1/2 | 1, 1, 0 | fail | 2 | 2 | +, + | F | 2 | 2a TR | D:212–229, 351 |
| TS(4), TS(5), noext | 0, 0 | 1, 1 | fail | 2 | null | + | F | 2 | I-9 | same |
| TM(2), T=1 | 0, 0, 1 | 1, 1, 0 | fail | 2 | 2 | +, + | F | 4 | 2a TR | D:241–251, 352 |
| TM(2), noext | 0, 0 | 1, 1 | fail | 2 | null | + | F | 4 | I-9 | same |
| TM(3), T=2 | 0, 0, 0, 1 | 1, 1, 1, 0 | fail | 3 | 3 | +, +, + | F, F | 5 | 2a TR | same |
| TM(3), noext | 0, 0, 0 | 1, 1, 1 | fail | 3 | null | +, + | F, F | 5 | I-9 | same |
| TMP | 0, 0, 1/2 | 1, 1, 0 | fail | 2 | 2 | +, + | F | 2 | 2a TR [U] | D:252–255 |
| TMP, noext | 0, 0 | 1, 1 | fail | 2 | null | + | F | 2 | I-9 [U] | same |
| HCP-h | 0, 0 | 1, 1 | fail | 1 | 1 | i− | F | 2 | 1 RS | Q7 F5 |
| SC | 1/20, 0 | 9/10, 1 | fail | 1 | 1 | ii− | P | null | 1 RS | Q7 F5 |
| S1(2), S1(3) | 0, 0 | 1, 1 | pass | ∞ | 1 | + | P | 1 | 5 static | D:259–263 |
| SW, T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | F | 2 | 6 I-4 | D:265–280 |
| SW, T=2 | 0, 0, 0 | 1, 1, 1 | pass | ∞ | 2 | +, + | F, F | 3 | 6 I-4 | D:274 |
| R1, T=4 | 0, 0, 1/2, 1/2, 0 | 1, 1, 0, 0, 1 | fail | 1 | 4 | +, +, +, i−ii− | F, P, P, F | 2 | 1 RS [U] | D:313–315; r6:331–332 |
| R2, T=3 | 0, 0, 0, 0 | 1, 1, 1, 1 | fail | 1 | 3 | i− ×3 | F, F, F | 4 | 1 RS | D:317–333 |
| R2, T=4 | 0, 0, 0, 0, 1 | 1, 1, 1, 1, 0 | fail | 1 | 4 | i− ×4 | F, F, F, F | 4 | 1 RS | same |
| R3, T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | P | 1 | 5 static | D:344 |
| R3, T=2 | 0, 0, 1/2 | 1, 1, 0 | fail | 1 | 2 | +, + | P, P | 1 | 2b EX | D:335–345; Q7 F2 |
| R3, T=5 | 0, 0, 1/2, 1/2, 0, 0 | 1, 1, 0, 0, 1, 1 | fail | 1 | 5 | +, +, +, i−ii−, + | P, P, P, F, P | 1 | 1 RS | D:337–341, 358; r6:364 |
| MA(2), MA(3) | 0, 1/4 | 1, 1/2 | fail | 1 | 1 | + | P | 0 | 2b EX | D:568; DEFINITIONS:152–153 |
| MB | 0, 1/2 | 1, 0 | fail | 1 | 1 | + | P | 3 | 2a TR [U] | D:569 |
| MC(2), T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | F | 4 | 6 I-4 [U] | D:570 |
| MC(3), T=2 | 0, 0, 0 | 1, 1, 1 | pass | ∞ | 2 | +, + | F, F | 5 | 6 I-4 [U] | D:570 |
| MD-xor | 1/2, 1/2 | 1, 1 | pass | ∞ | 1 | + | F | 1 | 3 no retention [U] | D:571 |
| CX-4b | 0, 0 | 1, 1 | fail | 1 | 1 | + | P | 3 | 7 TI | D:443–454 |

- In SC, `ε* = 1/20 = ε(t₀+1)`, so (R-c) holds.
- MD-xor: the decoder-sweep value is `1/2`, so every fixed decoder fails (R-c) [U].
- CX-4b [U values; row D:454]:
  - `G*_{W_T} = {(y₀, z₀) = (0, 0)}`, and it is consistent.
  - `η_{t₀+1} = 1/4`, and the Lemma H bound at `t₀+2` is `1/4 > ε*`.
  - DIL∃ fails through `(y₀, z₀) = (0, 1)`, which joins the supported `(1,1)` and `(0,1)`.
- **Recurrence flags**, compared for every tuple:
  - R1 at `T = 4`: `{t₀+5}`.
  - R3 at `T = 5`: `{t₀+5, t₀+6}`.
  - Every other tuple, readback tuples included: `∅`.
- **Readback mode** (row I-3, r6:414).
  - R1 at `{t₀+1, t₀+5}`: `ε = 0, 0` and `TV = 1, 1`.
  - R3 at `{t₀+1, t₀+5, t₀+6}`: `ε = 0, 0, 0` and `TV = 1, 1, 1` (D:315, 343).

### 3.3 HC-SK (`k = 1…6`, `T = 1, 2, 3`) (D:287–307, 562–564)

- `ε(t₀+1) = 0` and `TV(t₀+1) = 1`.
- For `j = 1…T`, `ε(t₀+1+j) = (1 − (1 − w)^j)/2` and `TV(t₀+1+j) = (1 − w)^j`, with `w = 2⁻ᵏ`.
- DIL∃ fails, `τ = 1` and `T′ = T`.
- `J = +` and SCH `= P` at every hold tick.
- `G*_T = G*_{T′} = {q : not all k bits are 1}`, and it is consistent.
- `η_t = w` at each hold tick, and the Lemma H bound at `t₀+1+j` is `j·w`.
- `w = 2⁻ᵏ` and `w_chg = 2⁻ᵏ⁻¹`. `D = 0`.

| `k` | `ε` at `j = 1, 2, 3` | `TV` at `j = 1, 2, 3` | Row `T=1` (bound `w`) | Row `T=2` (`2w`) | Row `T=3` (`3w`) |
|---|---|---|---|---|---|
| 1 | 1/4, 3/8, 7/16 | 1/2, 1/4, 1/8 | 2b EX | 2b EX | 2b EX |
| 2 | 1/8, 7/32, 37/128 | 3/4, 9/16, 27/64 | 2b EX | 2b EX | 2b EX |
| 3 | 1/16, 15/128, 169/1024 | 7/8, 49/64, 343/512 | 2b EX | 2b EX | 2b EX |
| 4 | 1/32, 31/512, 721/8192 | 15/16, 225/256, 3375/4096 | 8 I-6 (1/16) | 2b EX | 2b EX |
| 5 | 1/64, 63/2048, 2977/65536 | 31/32, 961/1024, 29791/32768 | 5 static (1/32) | 8 I-6 (1/16) | 8 I-6 (3/32) |
| 6 | 1/128, 127/8192, 12097/524288 | 63/64, 3969/4096, 250047/262144 | 5 static (1/64) | 5 static (1/32) | 5 static (3/64) |

Only the values for `j ≤ T` are compared for each tuple. That gives 18 tuples. They have no noext tuple, because
`T′ = T`.

**Tuple count and order.** 47 tuples are frozen in window or noext mode:
- 4 TS and 4 TM (each with ext and noext), 2 TMP (ext and noext);
- 1 HCP-h, 1 SC, 2 S1, 2 SW, 1 R1, 2 R2, 3 R3, 2 MA, 1 MB, 2 MC, 1 MD-xor and 1 CX-4b;
- the 18 HC-SK tuples.

Add 2 readback tuples, for **49 in total**. Every tuple has a frozen expected row.

The total order [U] is the `order` field of `PHASEA-TUPLES.json`:
- orders 1–31 are the non-HC-SK tuples, in the listed sequence;
- orders 32–49 are the HC-SK tuples, sorted by `n_bits = (T+1)(k+1)+1 = log₂|S|` ascending, with ties broken by `k`
  ascending. Since `(n_bits, k)` determines `T`, the order is total;
- so the 12 HC-SK tuples with `|S| ≤ 2¹⁶` (orders 32–43) precede the six sequential ones (44–49).

***

## 4. Decision rule

The rule applies r6 §4's precedence (r6:386–418) as follows.

**Computed objects.** Every object below is computed from `φ`, the law and the decoder only, by full or sequential
enumeration (§2.0), for every tuple and unconditionally:
- (R-a), which needs `A ∩ Σ = ∅` and `ρ_A(s_{t₀}) ⫫ κ` under `μ^P`; and (R-b), which needs the law of `g(A_{t₀})` given
  `σ` to be the same for both `σ ∈ P`;
- `Par`, `Q` (from `A`) and `f_R`;
- `ε_max(t)` and `TV_t` at the evaluated ticks;
- `supp Q_t` and `supp R_t` under `μ^P_t`;
- `𝒬_W` and `𝓛_W` for `W = W_T`, and, in window mode, `W = W_{T′}`;
- the classes of `~_G` on `config(R)`, built by union of `ℓ` with `f_R(ℓ, q)`, `q ∈ G`;
- exact DIL∃ (`G = 𝒬_{W_T}`);
- `τ` (§2.4);
- J-1 at each evaluated hold tick, from the exact joint table of `(σ, A_t, B_t)`;
- `C_t` and SCH at each hold tick of `H_T`, over the read cells;
- `G*`, `G_status`, `η` and the Lemma H bound (below);
- the recurrence flags;
- `write_min_eps` and, for MD-xor, the decoder sweep.

**The `G`-rule [U].**
- For a window `W`, let `G*_W := {q ∈ 𝒬_W : ~_{{q}} is consistent on 𝓛_W}`.
- Every consistent `G` is contained in `G*_W`, because a subset of a consistent set is consistent.
- `G_status_W` is:
  - `empty` if `G*_W = ∅`;
  - `consistent` if `G*_W ≠ ∅` and `~_{G*_W}` is consistent on `𝓛_W`;
  - `inconsistent` otherwise.
- When `G_status_W` is `empty` or `consistent`, `G*_W` is the unique largest consistent set. It then minimizes every
  `η_t(σ) = μ^P(Q_t ∉ G | σ)` at once.
- `η_t := max_σ μ^P(Q_t ∉ G*_{W_T} | σ)` for `t ∈ H_T`. With `G*_{W_T} = ∅`, `η_t = 1`.
- The Lemma H bound at `t ∈ W_T` is `ε_max(t₀+1) + Σ_{s ∈ H_T, s < t} η_s`.
- `G*_{W_T}` and `G*_{W_{T′}}` (window mode) are computed for every tuple. If `G_status_{W_T}` is `inconsistent`,
  `η` and the bound are reported as `null`.

**Row assignment.** The first matching step decides.

0. **Recurrence flags and readback mode.**
   - Flag each evaluated tick `t` with `ε_max(t) ≤ ε*` that follows some evaluated `t′ < t` with `ε_max(t′) > ε*`
     (the recurrence rule). No tuple with a flag may take row 5 or 6.
   - Readback mode assigns I-3.
1. **Noext mode.** With the extension not computed, row 1 applies if J-1 fails at a hold tick of `H_T`. Otherwise
   I-9 applies, with `T_prime = null`, if `T < τ < ∞`. Otherwise `T′ = T`, and evaluation continues at step 2.
2. **RS (row 1)** if J-1 fails (J-i or J-ii) at a hold tick of `H_{T′}`.
3. **TR (row 2a) or EX (row 2b)** if `τ < ∞` and `ε_max(t) > ε*` for some `t ∈ W_{T′}`. The case is TR iff
   `G*_{W_{T′}} = ∅`; this needs no joint consistency.
4. **No retention (row 3)** if (R-a) or (R-b) fails, or `ε_max(t) > ε*` for some `t ∈ W_T`.
5. **Row 4 (I-8)** if the decoder reads a clock `K` that does not meet Remark C in the scope narrowed by the Q7 review:
   (i)–(iv), with (R-a), (R-b) and (R-d) applied to `A ∪ K`, and `K` disjoint from Σ (r6:407).
   - In Phase A this is a declared constant, `false`, because no tuple has a clock decoder.
6. **Storage** if ST holds: `ε_max ≤ ε*` on `W_T`, and either exact DIL∃ on `W_T`, or `G*_{W_T} ≠ ∅` with the Lemma H
   bound `≤ ε*` at every `t ∈ W_T`.
   - If this step is reached with `G_status_{W_T} = inconsistent`, the tuple halts with exit 4. This is the only
     exit-4 condition.
   - Then **row 5 (static)** applies if SCH holds at every hold tick of `H_T`, and **row 6 (I-4, circulating,
     register-level)** otherwise.
7. **TI (row 7)** if `ε_max = 0` on `W_T`.
8. **I-6 (row 8)** otherwise.

**PASS.** The run passes iff all four of these hold:
- the host's conclusion for the Phase A job is `success`;
- the job's check step exits 0;
- `summary.json` has `verdict = PASS`;
- the `verdict_text` regenerated from `summary.json` equals the stored one byte for byte.

Any other combination is a void run.
- Within a pass, every tuple's computed row equals its frozen expected row, and every compared field equals its
  frozen value exactly.
- Any mismatch or nonzero exit halts the run at that point, and the run is void.
- There is no partial pass, no rerun within a freeze and no amendment after `F`.

***

## 5. Outputs (§A.44)

**Per tuple**, the file `phase-a/<tuple_id>.json` has schema `oret-phase-a/1`. It carries every field named in
`PHASEA-TUPLES.json` `compared_fields` for its mode, plus:
- `tuple_id`, `order`, `mode`, `params`;
- `eps_star` (`"1/20"`), `w_star` (`null`) and `T_star` (`null`);
- `kappa` (`"sigma"`), `independence_law` (`"mu_t(.|sigma in P)"`), `support_conditioning` (`"mu_t(.|sigma in P)"`) and
  `B_def` (`"Par(A)\\A on S"`);
- `Q_cells` and `read_cells`;
- `law`, `P`, `f`, `T` and `ticks`;
- `failures`, the D-MET item 4 list of `(σ, t, configuration, probability)`;
- `classes_T` and `Wr`;
- `expected`, `comparisons` (a list of `{field, expected, computed, match}`) and `match`;
- `rd_test` (`"J-1, Q7-narrowed"`) and `access` (`"H-cur (declared)"`);
- `frozen_inputs`, giving for each of the four frozen files its path, its git blob id at `F`, and the git blob id of
  the bytes the tool read;
- `run`: `F`, the run commit and `run_attempt`.

**Frozen-input check.**
- At start, the tool reads `F` and computes, for each of the four frozen files, the git blob id at `F`
  (`git rev-parse F:<path>`) and the git blob id of the bytes it loads.
- Any difference exits 3 before any tuple is evaluated.

**Encodings.**
- Every probability is a string matching `^(0|[1-9][0-9]*)(/[1-9][0-9]*)?$` in lowest terms. A JSON number in any of
  these fields is a schema violation.
- Every other encoding is that of `PHASEA-TUPLES.json` `conventions` and `field_definitions`.

**`phase-a/summary.json`** carries:
- `tuples_frozen` (49);
- `tuples_evaluated` (the ids, in order);
- `first_failure` (`null`, or `{exit, tuple_id, field, expected, computed, detail}`, where any part may be `null`);
- `verdict` (`PASS` or `HALT`);
- `verdict_text`.

The verdict text is rendered from these fields only:
- PASS: "Phase A: all 49 frozen tuples reproduced their expected rows and values."
- Exit 1: "Phase A halted at <tuple_id>: <field> expected <expected>, computed <computed>. The run is void."
- Exit 2: "Phase A halted at <tuple_id or 'start'>: schema violation in <field>. The run is void."
- Exit 3: "Phase A halted at start: frozen input <detail> does not match its git blob id at F. The run is void."
- Exit 4: "Phase A halted at <tuple_id>: G* undetermined on W_T at storage step. The run is void."
- Exit 5: "Phase A halted at <tuple_id>: enumeration-method check failed (<detail>). The run is void."
- Any other exit: "Phase A halted with exit <exit>. The run is void."

**Exit status.**

| Code | Meaning |
|---|---|
| 0 | all tuples match |
| 1 | row or value mismatch |
| 2 | schema violation or floating-point value |
| 3 | frozen input does not match its git blob id at `F` |
| 4 | `G*` undetermined at step 6 |
| 5 | an enumeration-method condition fails, or full and sequential disagree |
| other nonzero | error |

**Where the verdict is read from.** The verdict reads three things:
- the exit status of the check step;
- the host's job and step conclusions, read from its API;
- `summary.json`.

It never reads log text.

***

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted in this file | Checkpoint |
|---|---|
| exact rationals; no floating point in the verdict path | schema step: rational regex on every probability field; exit 2 |
| the four frozen inputs exist at `F` and are unchanged | the git blob ids at `F` are compared with the loaded bytes at start; exit 3; recorded in `frozen_inputs` in every output |
| 49 tuples in the frozen total order, each with an expected row; no adaptive extension | `tuples_frozen`; `order` compared with `PHASEA-TUPLES.json`; the schema rejects a missing expected row; `tuples_evaluated` is a prefix of the frozen order |
| one pass | the host run record shows `run_attempt = 1` |
| halt on first red | `tuples_evaluated` ends at `first_failure.tuple_id`; the step exits nonzero |
| decoders fixed before testing (§2.8) | the truth tables are in `PHASEA-TUPLES.json` at `F`; `g` is a compared field |
| decoder minimality, SC included (§2.8) | `write_min_eps` compared for every window and noext tuple; the MD-xor exception is visible as `ε(t₀+1) = 1/2` against `write_min_eps = 0` |
| `Q` built from `A`; SCH over the read cells | `Q_missing` and `G_star_out` are configurations of `Q`, so a `Q` built from the read cells changes them for TMP and CX-4b; `SCH` compared per tick |
| (R-a) and (R-b) computed | `Ra` and `Rb` compared for every window and noext tuple |
| enumeration method as frozen | `method` compared for every tuple |
| window convention: `W_T` for storage, `W_{T′}` for TR/EX | separate `_T` and `_Tprime` fields; a step re-applies §4 to the JSON fields and compares with `row` |
| `κ := σ`; independence and support conditioning under `μ(·|σ∈P)`; `B = Par(A)∖A` | fixed strings in every output; `J1` compared per tick, including R3 at `T = 2` and `T = 5` |
| `τ` exact; `τ = ∞ ⇒ T′ = T`; `T_prime = null` for I-9 | `tau` and `T_prime` compared; the re-application step asserts the implication |
| TR/EX only with an observed failure (Q2) | the re-application step asserts that some `t ∈ W_{T′}` has `ε > ε*` for every 2a/2b row |
| recurrence never supports rows 5 or 6 | `recurrence_flags` compared; the re-application step asserts that no flagged tuple has row 5 or 6 |
| `G*`, `η` and the bound computed for every tuple | the `_T` and `_Tprime` `G` fields, `eta` and `lemma_h_bound` compared for every window tuple |
| `w*` and `T*` unset and unused (§2.10) | `w_star` and `T_star` are `null`; the schema rejects any other value |
| sequential method valid and validated (§2.0) | its conditions are checked per tuple; full and sequential agree on orders 32–43; exit 5 |
| `G`-rule well defined | `G_status` compared; exit 4 at step 6 only |
| every fixed decoder fails (R-c) in mutation (d) | `sweep_min_max_eps` compared on MD-xor |
| Q5 quantities kept distinct | `w` and `w_chg` compared for every HC-SK tuple |
| PASS combines four signals | the check reads the job conclusion, the exit status, `summary.verdict` and the regenerated `verdict_text` |
| verdict text generated only from structured output | a step regenerates `verdict_text` from `summary.json` and compares it byte for byte |
| no K1, nonlinear rule or Phase B | the workflow has a single Phase A job; the frozen tuple list covers §3 only; the host's job list for the run |
| resource limits | the job's `timeout-minutes`; its conclusion is read from the host |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run, not the tuple set.
- **One pass**, halting on the first red. A void run is not repaired by re-running.
- **Order of steps.**
  1. The owner designates `F` and gives the go (§8).
  2. Only then does the designated writer, the coordinating session, write the tool and the workflow, on a disposable
     research branch.
  3. An independent reviewer reviews the tool and the workflow at their exact commit, before any dispatch.
  4. Dispatch is a separate owner approval (§A.43), and any `workflow_dispatch` launch is a special launch.
  5. The push-triggered workflows are inspected before any push.
  6. The independent reviewer also reviews the result.
- **Budget.** An estimate only. The six sequential HC-SK tuples are linear in `T`, and the largest full enumeration
  is `2¹⁶` states. A few minutes is expected and has not been measured. The job timeout is 30 minutes; a timeout is
  red, and there is no extension.
- **Evidence (§A.42).**
  - The result note states the commit, the command, `summary.json` (small, with its digest) and the owner's
    designations, quoted with author and time.
  - A run on a disposable branch leaves `summary.json` off `main`. It is provenance only until it lands on `main`.
- **Exclusions.** The run does not include:
  - K1;
  - a nonlinear target;
  - Phase B;
  - a new premise;
  - SOURCE-CANDIDATE promotion;
  - merge or publication;
  - edits to ROUTES.md or DEFINITIONS.md.

***

## 8. Open items blocking freeze

1. **Independent review of the exact frozen commit `F`.** The review covers:
   - this file, `DESIGN-PULSE.md`, `PHASEA-TUPLES.json` and `PHASEA-EXPECTED.json`;
   - the agreement of §3 with the two data files;
   - the transcription of the Q7 wording in §2.7.
2. **The owner's go on that reviewed `F`.** The go designates `F`. It explicitly accepts each [U] choice that the
   run depends on:
   - (a) the F6 choice: row 1 applies J-1 on `H_{T′} ∖ H_T` (§2.7);
   - (b) the support-conditioning convention: `supp Q_t`, `𝓛`, `C_t` and `η` under `μ(·|σ∈P)` (§2.0);
   - (c) CX-4b as a control. It lies outside the owner's boundary "the frozen controls and the specified mutations"
     (c.6621961326);
   - (d) the MD-xor exception to Q8's decoder minimality (§2.8);
   - (e) the `G`-rule (§4);
   - (f) the sequential enumeration method (§2.0);
   - (g) the HC-SK tie-break order (§3.3);
   - (h) the model specifications made here: MB and MC, HCP-h, SC, the CX-4b concretization, `T = m−1` for HC-TM,
     `L = T+1` for HC-SK, and HC-R1's row at `T = 4`.

***

## 9. Remaining limitations: what Phase A cannot show

- **Calibration, not validation.** The controls are toy rules designed with known answers, and the expected values
  come from the same design. A pass shows that the implementation and the hand algebra agree. It does not show that
  the criteria separate storage from transport on cases outside the set.
- **Rows exercised and not exercised.**
  - Exercised: rows 1, 2a, 2b, 3, 5, 6, 7 and 8, and evidence rows I-3 and I-9.
  - **Row 4 (I-8) has no control.** In Phase A, step 5 is a declared constant, not a computed predicate, so no tuple
    could exercise it.
    - The one clocked case in DESIGN (§5 audit: HC-SW with `r₂` uniform and an accounted clock) meets Remark C, so it
      would fall in row 6, not row 4.
    - The in-corpus candidate, HC-K3's planted-marker decoder (DEFINITIONS:242), is K1-based and out of scope.
  - Evidence rows I-1, I-2 and I-5 are not exercised.
  - CX-4 is not in the set, because DESIGN gives it only schematically and no hand-derived instance exists. CX-4b is in
    the set.
- **Coverage gaps within the exercised rows.**
  - Row 3 is reached only through `ε_max > ε*`, never through a failure of (R-a) or (R-b).
  - No tuple has a J-1 failure in `H_{T′} ∖ H_T`, and none takes the row-1 branch of noext step 1.
  - Exit 4 is never exercised.
- **Known false admits and rejects remain:**
  - J-1 admits advection inside `A`; DIL∃ catches it here.
  - J-1 false-rejects disabled couplings (Q7 F4).
  - DIL∃ over-rejects through pooling (CX-4) and through joint support (CX-4b); the latter is classified TI, which is
    inconclusive, not storage.
  - The siding of CX-7 is undecided.
- **Conventions decide verdicts.**
  - The independence law and the support conditioning both use `μ(·|σ∈P)`. Under the full-support `μ`, HC-R3 on `W₂`
    would be RS, not EX, and the other channel-model rows are not derived under that alternative.
  - Every verdict is relative to the cell decomposition and to `A` (CX-3), and I-5 is not evaluated.
- **Decoder dependence [U].** The rows of HC-TS and HC-SW depend on decoder values at configurations that are
  unsupported at the write tick (§2.8). Phase A fixes them by the DESIGN decoders [O]. The rule for them in later
  phases is a separate owner decision before Phase B.
- **Imposed laws.** Every storage control imposes its preparation (quiet bits and ready registers). Phase A says
  nothing about where such a preparation could come from (O1), about access (O3) or about observers (O4).
- **Scope.** A pass says nothing about native dynamics, K1 or any nonlinear rule.
- **Governance form.** Phase A is not a §A.39 native V3 round. It carries no `v3-round` or `v3-governed-paths` block.
  Its freeze is the owner-designated exact commit `F`, as for the earlier frozen preregistrations here.
