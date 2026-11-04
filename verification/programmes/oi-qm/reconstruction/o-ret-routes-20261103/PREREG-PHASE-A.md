# O-RET Phase A preregistration: exact replay of the pulse-design controls

**Status.** WIP / UNVERIFIED preregistration draft. **Not frozen. Not authorized to run.** A run needs the owner's go
on a reviewed freeze of this file (#1032, Q9). Design: `DESIGN-PULSE.md` at `e8dfe25e` (reviewed ACCEPT), with
revision r4 (`DESIGN-PULSE-r4.md`, unreviewed) that applies the reviewer's two nits, the Q1 and Q5 rulings and the
Q7 narrowing. Owner decisions: #1032, 2026-11-03/04. Q7 review: `REVIEW-Q7.md` (2026-11-04).

Support labels: **[D]** derivation in DESIGN (`D:n` = line of `DESIGN-PULSE.md` at `e8dfe25e`; `r4:n` = line of r4).
**[C]** checkpoint text in ROUTES.md or DEFINITIONS.md. **[O]** owner decision, #1032. **[U]** unreviewed: a
derivation or specification made in this file, or wording frozen from the Q7 review.

***

## 1. Objective and non-objectives

**Objective.** Replay, by exhaustive exact enumeration, every control instance of DESIGN §8 Phase A (D:537–549,
r4:553–566), plus the controls the Q7 review adds, and check two things for each tuple: that the assigned §4 row
(r4:379–411) equals the frozen expected row, and that every frozen hand-derived value is reproduced exactly. The aim
is to establish that the decision procedure separates the storage controls from the transport, re-supply and export
controls before it is applied to any native dynamics [O, Q9].

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
the hand derivations of DESIGN §3 and of §3 below, and the implemented §4 precedence assigns the hand-assigned rows.
This is a result on the consistency axis (§A.23).

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
  - `τ` is computed from `𝒬_{W_T}` and `𝓛_{W_T}` (r4:158–164).
- **Carrier and law [U, Q7 F2].**
  - The carrier law `μ_Σ` is uniform on Σ's configurations.
  - `κ := σ`.
  - Every independence statement, `C_t`, `supp Q_t`, `𝓛` and `η` is evaluated under `μ^P_t := μ_t(· | σ ∈ P)`.
  - `ε_max(t) := max_{σ∈P} μ(g(A_t) ≠ f(σ) | σ)`, and `TV_t` is that of the two `σ`-conditioned laws of the full
    readout `A_t` (D-MET [C]).
- **Dependence [U, Q7 F1].**
  - `B_t := Q := Par(A) ∖ A`, computed from `φ` on all of `S`. This repairs the ill-posed "on the support" text of
    DEFINITIONS:77–78 (D0, D:57–64). The law enters only through the joint law of `(κ, A_t, B_t)`.
  - In every tuple `A` equals its read set.
- **Arithmetic.**
  - Probabilities are exact rationals, computed from exact integer counts over the enumerated support with exact
    rational weights.
  - Any floating-point value in the verdict path is a failure (§5, exit 2).
- **Enumeration method [U].**
  - *Full:* every state of `S`. This is used for every tuple with `|S| ≤ 2¹⁶`.
  - *Sequential:* exact sequential marginalization. This is used only for the six HC-SK tuples with `|S| > 2¹⁶`:
    `(k, T) ∈ {(5,2), (6,2), (3,3), (4,3), (5,3), (6,3)}`.
    - At each tick, the law of `(σ, r)` is updated by the exact law of the arriving cell, which is fresh and
      independent.
    - It is valid because the law at `t₀` is a product over cells, and with `L = T+1` no cell enters `Q` twice within
      `t₀, …, t₀+T`.
    - The program checks both conditions from `φ` and the law, and exits 5 if either fails.
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
It is not static cell storage. Operationally this is r4 row 6 (r4:402): ST without SCH, with row 1 failing. HC-SW and
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
- `τ` is computed exactly. Iterate the reachable sets `ℛ₀ = supp R_{t₀+1}` and `ℛ_k = {f_R(ℓ, q) : ℓ ∈ ℛ_{k−1}, q ∈ 𝒬}`,
  following each start `ℓ` separately, until the family of sets repeats. `τ = ∞` if no hit occurs before the repeat.
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
  - Independence is evaluated under `μ_t(·|σ∈P)` at each hold tick.
  - S-1: every cell of `B_t` is independent of `κ`.
  - J-1: (J-i) `B_t ⫫ κ`, and (J-ii) `κ ⫫ B_t | A_t`.
  - These are inflow screens only.
  - Known false admits: advection inside `A`, and outflow.
  - Known false rejects: carrier-correlated inputs whose coupling is disabled on the support (F4).
- **Row 1's window (F6): the extension is stated.**
  - Row 1 applies J-1 at each hold tick of `W_{T′}` (r4:396), which extends (R-d), stated on `W_T` at
    DEFINITIONS:51. A row-1 verdict from a hold tick in `W_{T′} ∖ W_T` records inflow in the extension, not re-supply
    over `W_T`.
  - *Choice.* Both options leave every expected row in §3 unchanged, because no Phase A tuple has a J-1 failure in
    `W_{T′} ∖ W_T`. The stated extension keeps r4 §4's precedence and coverage proof unchanged. Restricting row 1 to
    `W_T` would leave one case with no row: J-1 holding on `W_T`, failing on `W_{T′} ∖ W_T`, with a record lost. That
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
  - No Phase A tuple has a clock decoder, so r4 row 4 is never assigned.
- **Scope notes.**
  - (F3) DEFINITIONS:82 "rejects … K1 generally" holds at K-18(b) under `δ₀` and `δ_b` only. Under `π₀` the inflow is
    padded and (R-c) excludes K1. K1 is not a Phase A instance.
  - (F8) DEFINITIONS:102 "B is empty" holds for a bare swap only. In HC-SW, `B = {p₀, v₀}`, which is quiet and
    independent at the hold ticks, and J-1 passes.
- **Effect on §3.** Every expected row in §3 is derived under this wording.
  - (F2) HC-R3 on `W₂` is EX under `μ(·|σ∈P)`. It would be RS under the full-support `μ` (r4:350–352).
  - (F4) The false-reject class affects no tuple: HC-R3's unfired branch is excluded by conditioning on `P`, and every
    other carrier-correlated `B` in §3 has an active coupling.
  - (F5) Controls HCP-h and SC are added.
  - (F1) Under `B = Par(A) ∖ A`:
    - J-1 fails only in HCP-h (J-i), SC (J-ii) and R2 (J-i at every hold tick).
    - J-1 passes at every evaluated hold tick of every other tuple.
    - S-1 is implied by J-i and is not computed. It would fail exactly in HCP-h and R2.

### 2.8 Q8, decoder [O; Phase A reading U]
- The decoder is frozen at the write tick and never chosen from later retention outcomes.
- **Phase A uses the decoders fixed in DESIGN §3**, listed per tuple in §3. They are part of each control's
  definition and are fixed before any run.
- Each listed decoder attains the minimum worst-case write-time error over the decoders of `A`. The exception is
  MD-xor, whose decoder the mutation fixes. This is checked through the frozen `ε_max(t₀+1)` values.
- Q8's lexicographic tie-break is not applied to Phase A controls. The tie-break sets the decoder on configurations
  unsupported at `t₀+1`, and those values decide rows [U]:
  - With the truth-table-minimal tie-break, HC-SW gets `g(10) = 0` and becomes TR.
  - With the same tie-break, HC-TS gets `g(01) = 0` and becomes TR on `W₁` itself.
  - With the maximal tie-break, both keep their DESIGN rows.
- Q8's full rule therefore governs only later phases. This reading is part of what the owner's go confirms (§8).

### 2.9 Q9, authorization [O]
- Phase A only, controls only.
- The run is authorized only by the owner's go on the reviewed freeze.
- Phase B needs a separate owner decision.

### 2.10 Qualifications [O]
- `w*` and `T*` are **unset and unused**.
- The ST clause "`w ≥ w*` and `T ≥ T*`" (r4:165–166) and row 8's second clause are inactive.
- No D-SML comparison is issued.
- Both of the reviewer's nits are applied in r4.

***

## 3. The frozen control set

The expected values below are **replay checks of hand derivations**, which is a control function. §A.29's "rule, not
numbers" applies to the decision rule of §4, which is frozen without reference to these numbers. A value derived in
this file rather than in DESIGN is marked [U]. Notation:
- `ε` and `TV` list the values at `t₀+1, t₀+2, …` through the end of the evaluated window.
- `J` lists J-1 per hold tick, as `+` (both parts pass) or `i−` / `ii−` (that part fails).
- `G*` is defined in §4.

For every tuple, (R-a) and (R-b) hold. The decoder is the one listed, and `f(σ) = c` is the carrier value bit
(`v₀` for channel models).

### 3.1 Models (cells in `𝔽₂`; shift means `x_j ← x_{j−1}` with indices mod `L`)

- **HC-TS(L)** (D:204–229).
  - Ring `u₀…u_{L−1}`, pure shift. `Σ = {u₀}`.
  - Law: uniform on `{u₁ = u_{L−1} = 0}`.
  - `A = (u₁, u₂)`, `g = u₁ ⊕ u₂`.
- **HC-TM(m, L = m+3)** (D:231–251).
  - Rule: `u₁ ← u₁ ⊕ u₀`, then shift. Law: `u₀` uniform, all other cells 0.
  - `A = (u₁…u_m)`, `g = OR`. `T = m−1` [U: the largest exact window].
- **TMP** (D:252–255). HC-TM's rule with `m = 2`, `L = 5`. Law: uniform on `{u₁ = u₄ = 0}`. `A = (u₁, u₂)`,
  `g = u₂`. `T = 1`.
- **HCP-h** [U; Q7 F5; ROUTES:170–177].
  - HC-P with `L = 4`, which is HC-TM's rule. Law: uniform on `{u₁ = u₃ = 0}`.
  - `A = (u₂)`, `g = u₂`. `T = 1`.
- **SC, share completion with a biased pad** [U; Q7 F5; DEFINITIONS:98–99].
  - Cells `a, z₀, z₁, z₂`. Rule: `a ← a ⊕ z₀`, then shift `z` mod 3. `Σ = {z₀}`.
  - Law: `z₀` uniform; `n ~ Bernoulli(1/20)`, with `a = z₂ = n`; `z₁ = 0`.
  - `A = (a)`, `g = a`. `T = 1`.
  - `p = ε*` makes (R-c) hold at the boundary, so only J-ii rejects the case. It also exercises exact `≤`.
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
- **HC-R1** = HC-TS(4), read late (D:312–315).
- **HC-R2** (D:317–333).
  - Cells `c, w₀…w₃`. Rule: `w₀ ← w₀ ⊕ c`, then shift `w`; `c` is unchanged. `Σ = {c}`.
  - Law: `c` uniform, `w = 0`.
  - `A = (w₁)`, `g = w₁`.
- **HC-R3** = S1(2), read over longer windows (D:335–345).
- **MA(L)**, mutation (a) (D:568): S1(L) under `π₀`. MA(2) is HC-SK(1, 1); MA(3) is the same model with `L = 3`.
- **MB**, mutation (b) [U] (D:569).
  - HC-SW at `L = 3`, with `r₁ ↔ r₂` replaced by the 3-cycle `r₁ ← v₁, r₂ ← r₁, v₁ ← r₂`. The cycle is applied after
    the Fredkin and before the shift; `r₂` shifts out into the channel.
  - Law: uniform on `{p₂ = 0, r₂ = 0, v₁ = 0}`. `T = 1`.
  - The extra quiet `v₁` keeps the write exact, so the mutation tests DIL∃ rather than the write.
- **MC(m)**, mutation (c) [U] (D:570).
  - HC-TM(m, L = m+3) with the shift closed inside `R`: `u₁ ← u_m`, and `u_j ← u_{j−1}` for `2 ≤ j ≤ m`.
  - The outside cells form their own ring: `u_{m+1} ← u₀`, `u_j ← u_{j−1}` for `m+2 ≤ j ≤ L−1`, and `u₀ ← u_{L−1}`.
  - The gate `u₁ ← u₁ ⊕ u₀` comes first. `T = m−1`. The carrier returns to `u₀` at `t₀+3`, outside every evaluated
    hold tick.
- **MD**, mutation (d) (D:571).
  - HC-SW at `L = 3` under the law uniform on `{p₂ = 0}`, so `r₂` is uniform. `T = 1`.
  - MD-xor uses `g = r₁ ⊕ r₂`.
  - MD-sweep ranges over all 16 decoders of `(r₁, r₂)`.

### 3.2 Expected results (window mode unless stated)

The column "noext" gives the row of the separate noext tuple, with the extension not computed. That mode uses `ε`,
`TV` and `J` on `W_T` only, and exists only for TS, TM and TMP, where `T < τ`. The `D` column gives the ledger in
bits, `D = log₂|S| − H(μ)`.

| Tuple | `ε` | `TV` | DIL∃ on `W_T` | `τ` | `T′` | `J` | `G*_{T′}` | SCH | `D` | Row | noext | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TS(4), TS(5), T=1 | 0, 0, 1/2 | 1, 1, 0 | fail | 2 | 2 | +, + | ∅ | fail | 2 | 2a TR | I-9 | D:212–229, 351 |
| TM(2), T=1 | 0, 0, 1 | 1, 1, 0 | fail | 2 | 2 | +, + | ∅ | fail | 4 | 2a TR | I-9 | D:241–251, 352 |
| TM(3), T=2 | 0, 0, 0, 1 | 1, 1, 1, 0 | fail | 3 | 3 | +, +, + | ∅ | fail | 5 | 2a TR | I-9 | same |
| TMP | 0, 0, 1/2 | 1, 1, 0 | fail | 2 | 2 | +, + | ∅ | — | 2 | 2a TR [U] | I-9 [U] | D:252–255 |
| HCP-h | 0, 0 | 1, 1 | fail | 1 | 1 | i− | — | — | 2 | 1 RS | — | Q7 F5 |
| SC | 1/20, 0 | 9/10, 1 | fail | 1 | 1 | ii− | — | — | — | 1 RS | — | Q7 F5 |
| S1(2), S1(3) | 0, 0 | 1, 1 | pass | ∞ | 1 | + | — | pass | 1 | 5 static | — | D:259–263 |
| SW, T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | — | fail | 2 | 6 I-4 | — | D:265–280 |
| SW, T=2 | 0, 0, 0 | 1, 1, 1 | pass | ∞ | 2 | +, + | — | fail | 3 | 6 I-4 | — | D:274 |
| R2, T=3 | 0, 0, 0, 0 | 1, 1, 1, 1 | fail | 1 | 3 | i− ×3 | — | fail | 4 | 1 RS | — | D:317–333 |
| R2, T=4 | 0, 0, 0, 0, 1 | 1, 1, 1, 1, 0 | fail | 1 | 4 | i− ×4 | — | fail | 4 | 1 RS | — | same |
| R3, T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | — | pass | 1 | 5 static | — | D:344 |
| R3, T=2 | 0, 0, 1/2 | 1, 1, 0 | fail | 1 | 2 | +, + | `{p₀ = 0}` | pass | 1 | 2b EX | — | D:335–345; Q7 F2 |
| MA(2), MA(3) | 0, 1/4 | 1, 1/2 | fail | 1 | 1 | + | `{p₀ = 0}` | pass | 0 | 2b EX | — | D:568; DEFINITIONS:152–153 |
| MB | 0, 1/2 | 1, 0 | fail | 1 | 1 | + | ∅ | — | 3 | 2a TR [U] | — | D:569 |
| MC(2), T=1 | 0, 0 | 1, 1 | pass | ∞ | 1 | + | — | fail | 4 | 6 I-4 [U] | — | D:570 |
| MC(3), T=2 | 0, 0, 0 | 1, 1, 1 | pass | ∞ | 2 | +, + | — | fail | 5 | 6 I-4 [U] | — | D:570 |
| MD-xor | 1/2, 1/2 | 1, 1 | pass | ∞ | 1 | + | — | — | 1 | 3 no retention [U] | — | D:571 |

- In SC, `ε* = 1/20 = ε(t₀+1)`, so (R-c) holds.
- **MD-sweep [U].** `min over g of max_{t∈W₁} ε_max(t) = 1/2`, so every fixed decoder fails (R-c). No row is assigned.
- **Span mode** (no row; recurrence flags per §4 step 0).
  - R1 over `t₀+1…t₀+5`: `ε = 0, 0, 1/2, 1/2, 0`; `TV = 1, 1, 0, 0, 1`; flag `{t₀+5}` (D:313–315).
  - R3 over `t₀+1…t₀+6`: `ε = 0, 0, 1/2, 1/2, 0, 0`; `TV = 1, 1, 0, 0, 1, 1`; flags `{t₀+5, t₀+6}` (D:337–338).
- **Readback mode** (row I-3, r4:407).
  - R1 at `{t₀+1, t₀+5}`: `ε = 0, 0`.
  - R3 at `{t₀+1, t₀+5, t₀+6}`: `ε = 0, 0, 0` (D:315, 343).
- The rows of the span modes over the full gap-free span are not frozen. DESIGN derives none, and the evaluated
  windows above do not need them.

### 3.3 HC-SK (`k = 1…6`, `T = 1, 2, 3`) (D:287–307, 562–564)

- `ε(t₀+1) = 0` and `TV(t₀+1) = 1`.
- For `j = 1…T`, `ε(t₀+1+j) = (1 − (1 − w)^j)/2` and `TV(t₀+1+j) = (1 − w)^j`, with `w = 2⁻ᵏ`.
- DIL∃ fails, `τ = 1` and `T′ = T`.
- `J = +` at every hold tick, and SCH passes.
- `G*_T = G*_{T′} = {q : not all k bits are 1}`, and it is consistent.
- `max_σ η_t = w` at each hold tick, and the Lemma H bound at the window's end is `T·w`.
- `w = 2⁻ᵏ` and `w_chg = 2⁻ᵏ⁻¹` are reported. `D = 0`.

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

**Tuple count.** 44 tuples are frozen in window or noext mode:
- 4 TS and 4 TM (each with ext and noext), 2 TMP (ext and noext);
- 1 HCP-h, 1 SC, 2 S1, 2 SW, 2 R2, 2 R3, 2 MA, 1 MB, 2 MC and 1 MD-xor;
- the 18 HC-SK tuples.

Add 1 sweep, 2 span and 2 readback tuples, for **49 in total**. The frozen tuple list states them in order:
- the small tuples first;
- then the HC-SK tuples by increasing `|S|`, so that the method validation of §2.0 precedes the sequential use.

***

## 4. Decision rule

The rule applies r4 §4's precedence (r4:379–411) as follows.

**Computed objects.** Every object below is computed from `φ`, the law and the decoder only, by full or sequential
enumeration (§2.0):
- `Par`, `Q` and `f_R`;
- `ε_max(t)` and `TV_t`;
- `supp Q_t` and `supp R_t` under `μ^P_t`;
- `𝒬_W` and `𝓛_W` for `W = W_T, W_{T′}`;
- the classes of `~_G` on `config(R)`, built by union of `ℓ` with `f_R(ℓ, q)`, `q ∈ G`;
- exact DIL∃ (`G = 𝒬_{W_T}`);
- `τ` (§2.4);
- J-1 at each hold tick, from the exact joint table of `(σ, A_t, B_t)`;
- `C_t` and SCH at each hold tick of `H_T`.

**The `G`-rule [U].**
- For a window `W`, let `G*_W := {q ∈ 𝒬_W : ~_{{q}} is consistent on 𝓛_W}`.
- Every consistent `G` is contained in `G*_W`, because a subset of a consistent set is consistent.
- If `G*_W` is nonempty and `~_{G*_W}` is inconsistent, the tuple halts with exit 4.
- Otherwise `G*_W` is the unique largest consistent set, and it minimizes every `η_t(σ) = μ^P(Q_t ∉ G | σ)` at once.
- DIL∃-η uses `G*_{W_T}`. The Lemma H bound at `t` is `ε_max(t₀+1) + Σ_{s ∈ H_T, s < t} max_σ η_s`.
- TR holds iff `G*_{W_{T′}} = ∅`; otherwise EX.

**Row assignment.** The first matching step decides.

0. **Span, readback and sweep modes.**
   - Span mode assigns no row. It flags each `t` with `ε_max(t) ≤ ε*` that follows some `t′ < t` in the span with
     `ε_max(t′) > ε*` (the recurrence rule).
   - Readback mode assigns I-3.
   - Sweep mode assigns no row.
1. **Noext mode.** With the extension not computed, row 1 applies if J-1 fails at a hold tick of `H_T`. Otherwise
   I-9 applies if `T < τ < ∞`. Otherwise `T′ = T`, and evaluation continues at step 2.
2. **RS (row 1)** if J-1 fails (J-i or J-ii) at a hold tick of `H_{T′}`.
3. **TR (row 2a) or EX (row 2b)** if `τ < ∞` and `ε_max(t) > ε*` for some `t ∈ W_{T′}`. The case is TR iff
   `G*_{W_{T′}} = ∅`.
4. **No retention (row 3)** if (R-a) or (R-b) fails, or `ε_max(t) > ε*` for some `t ∈ W_T`.
5. **Row 4 (I-8)** if the decoder reads a clock. This is false for every Phase A tuple.
6. **Storage** if ST holds: `ε_max ≤ ε*` on `W_T`, and either exact DIL∃ on `W_T`, or `G*_{W_T} ≠ ∅` with the Lemma H
   bound `≤ ε*` at every `t ∈ W_T`. Then:
   - **row 5 (static)** if SCH holds at every hold tick of `H_T`;
   - **row 6 (I-4, circulating, register-level)** otherwise.
7. **TI (row 7)** if `ε_max = 0` on `W_T`.
8. **I-6 (row 8)** otherwise.

**PASS.** A run passes iff every tuple's computed row equals its frozen expected row, every compared value equals its
frozen value exactly, and every exit status is 0.
- Fields that §3 does not list are recorded and not compared.
- Any mismatch or nonzero exit halts the run at that tuple, and the run is void.
- There is no partial pass, no rerun within a freeze and no amendment after `F`.
- The verdict text is generated from `summary.json` alone (§5).

***

## 5. Outputs (§A.44)

**Per tuple**, the file `phase-a/<tuple_id>.json` has schema `oret-phase-a/1`.

*Identification and settings:*
- `tuple_id`, `control`, `mode` (one of `window`, `noext`, `span`, `readback`, `sweep`) and `params`;
- `eps_star` (`"1/20"`), `w_star` (`null`) and `T_star` (`null`);
- `kappa` (`"sigma"`), `independence_law` (`"mu_t(.|sigma in P)"`) and `B_def` (`"Par(A)\\A on S"`);
- `method` (`full` or `sequential`);
- `law` (constraints and weights) and `D_bits`;
- `P`, `f`, `g` (formula and truth table), `T`, `T_prime` and `ticks`.

*Metrics and failures:*
- `eps_max`, `tv`, `eta` and `lemma_h_bound`, each a map from tick to rational;
- `failures`, the D-MET item 4 list of `(σ, t, configuration, probability)`.

*Criteria:*
- `Ra`, `Rb`;
- `dil_exact_T`, `classes_T` and `Wr`;
- `tau` (an integer or `"inf"`);
- `J1`, a map from tick to `{Ji, Jii}`;
- `SCH`, a map from tick to boolean;
- `G_star_T`, `G_star_Tprime` and `G_status`;
- `recurrence_flags`;
- `sweep_min_max_eps`;
- `w`, `w_chg`.

*Verdict and provenance:*
- `row`;
- `expected`, `comparisons` (a list of `{field, expected, computed, match}`) and `match`;
- `rd_test` (`"J-1, Q7-narrowed"`) and `access` (`"H-cur (declared)"`);
- `hashes`: the sha256 of this file, of r4, of the frozen tuple list and of the expected table;
- `run`: commit and `run_attempt`.

**Encodings.**
- Every probability is a string matching `^(0|[1-9][0-9]*)(/[1-9][0-9]*)?$` in lowest terms. A JSON number in any of
  these fields is a schema violation.
- `D_bits` is an integer, or `null` for SC.

**`phase-a/summary.json`** carries:
- `tuples_frozen` (49);
- `tuples_evaluated` (the ids, in order);
- `first_failure` (`null`, or `{tuple_id, field, expected, computed, exit}`);
- `verdict` (`PASS` or `HALT`);
- `verdict_text`.

The verdict text is rendered from these fields only:
- PASS: "Phase A: all 49 frozen tuples reproduced their expected rows and values."
- HALT: "Phase A halted at <tuple_id>: <field> expected <e>, computed <c>. The run is void."

**Exit status.**

| Code | Meaning |
|---|---|
| 0 | all tuples match |
| 1 | row or value mismatch |
| 2 | schema violation or floating-point value |
| 3 | hash mismatch of a frozen input |
| 4 | `G` undetermined |
| 5 | an enumeration-method condition fails, or full and sequential disagree |
| other nonzero | error |

**Where the verdict is read from.** The verdict reads three things:
- the exit status of the check job;
- the host's job and step conclusions, read from its API;
- `summary.json`.

It never reads log text.

***

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted in this file | Checkpoint |
|---|---|
| exact rationals; no floating point in the verdict path | schema step: rational regex on every probability field; exit 2 |
| frozen inputs unchanged after `F` | hashes of this file, of r4, of the tuple list and of the expected table, compared at start; exit 3; hashes recorded in every output |
| 49 tuples in frozen order; no adaptive extension | `summary.tuples_frozen`; the tuple-list hash; `tuples_evaluated` is a prefix of the frozen list |
| one pass | the host run record shows `run_attempt = 1` |
| halt on first red | `tuples_evaluated` ends at `first_failure.tuple_id`; the job exits nonzero |
| decoders fixed before testing (§2.8) | the decoder truth table of each tuple is in the expected table, and `g` is a compared field |
| each control decoder attains the minimum write-time error | the frozen `ε(t₀+1)` values (all 0, except SC 1/20 and MD-xor 1/2) |
| window convention: `W_T` for storage, `W_{T′}` for TR/EX | separate fields `G_star_T` and `G_star_Tprime`; a step re-applies §4 to the JSON fields and compares with `row` |
| `κ := σ`, independence under `μ(·|σ∈P)`, `B = Par(A)∖A` | fixed strings in every output; `J1` compared per tick, R3 at `T = 2` included |
| `τ` exact; `τ = ∞ ⇒ T′ = T` | `tau` and `T_prime` compared; the re-application step asserts the implication |
| TR/EX only with an observed failure (Q2) | the re-application step asserts that some `t ∈ W_{T′}` has `ε > ε*` for every 2a/2b row |
| `w*` and `T*` unset and unused (§2.10) | `w_star` and `T_star` are `null`; the schema rejects any other value |
| sequential method valid and validated (§2.0) | its conditions are checked per tuple; full and sequential agree on every HC-SK tuple with `|S| ≤ 2¹⁶`; exit 5 |
| `G`-rule well defined | `G_status`; exit 4 |
| Q5 quantities kept distinct | `w` and `w_chg` compared for every HC-SK tuple |
| verdict text generated only from structured output | a step regenerates `verdict_text` from `summary.json` and compares it byte for byte |
| no K1, nonlinear rule or Phase B | the workflow has a single Phase A job; the tuple list hash covers §3 only; the host's job list for the run |
| resource limits | the job's `timeout-minutes`; its conclusion is read from the host |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run, not the tuple set.
- **One pass**, halting on the first red. A void run is not repaired by re-running.
- **Roles.** One designated writer, the coordinating session, writes the tool and the workflow. An independent
  reviewer reviews this file, the tool and the workflow before the owner's go, and reviews the result.
- **Branch and workflow.**
  - A disposable research branch and a workflow file are written only after the owner's go.
  - Any `workflow_dispatch` launch is a separate, owner-approved special launch (§A.43).
  - The push-triggered workflows are inspected before any push.
- **Budget.** An estimate only. The six sequential HC-SK tuples are linear in `T`, and the largest full enumeration
  is `2¹⁶` states. A few minutes is expected and has not been measured. The job timeout is 30 minutes; a timeout is
  red, and there is no extension.
- **Evidence (§A.42).** The result note states:
  - the commit;
  - the command;
  - `summary.json`, which is small, with its digest;
  - the owner's designations, quoted with author and time.
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

1. **Q7 transcription.** §2.7 is filled from `REVIEW-Q7.md`, and the coordinator confirms the transcription before
   freeze.
2. **The owner's go on the reviewed freeze.** The go:
   - designates the freeze commit;
   - states the run's governance: a research run on a disposable branch, or a native round under §A.39;
   - confirms in particular the Phase A reading of Q8 (§2.8).

***

## 9. Remaining limitations: what Phase A cannot show

- **Calibration, not validation.** The controls are toy rules designed with known answers, and the expected values
  come from the same design. A pass shows that the implementation and the hand algebra agree. It does not show that
  the criteria separate storage from transport on cases outside the set.
- **Unexercised rows.** Rows 4 (I-8) and 7 (TI) and evidence rows I-1, I-2 and I-5 are not exercised. CX-4 and CX-4b,
  the known storage cases that DIL∃ over-rejects (D:438–454), are not in the set.
- **Known false admits and rejects remain:**
  - J-1 admits advection inside `A`; DIL∃ catches it here.
  - J-1 false-rejects disabled couplings (Q7 F4).
  - DIL∃ over-rejects through pooling (CX-4) and through joint support (CX-4b).
  - The siding of CX-7 is undecided.
- **Conventions decide verdicts.**
  - Under the full-support `μ`, HC-R3 on `W₂` would be RS, not EX.
  - Every verdict is relative to the cell decomposition and to `A` (CX-3), and I-5 is not evaluated.
- **Decoder dependence [U].** The rows of HC-TS and HC-SW depend on decoder values at configurations that are
  unsupported at the write tick (§2.8). A write-time decoder rule does not fix those values, so Phase B's decoder rule
  needs this resolved before it is used.
- **Imposed laws.** Every storage control imposes its preparation (quiet bits and ready registers). Phase A says
  nothing about where such a preparation could come from (O1), about access (O3) or about observers (O4).
- **Scope.** A pass says nothing about native dynamics, K1 or any nonlinear rule.
