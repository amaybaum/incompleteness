# Independent check of `CONFIRM-r2.md` §6 (rule-free shared-record question)

**Standing.** Independent checker; not the writer of `L54-r2.md` and not the reviewer of
`CONFIRM-r2.md`. Read-only on the repository and both worktrees; nothing edited, committed, pushed
or posted. Hand reasoning only: no computation was written or run on any OI rule or model; the
time-stepping below is by hand and the tables are shown. Every derivation here is one hand
derivation. Items marked **checker-authored** are my own additions and have had no check at all.

**Pins.** `main` at `c3b5f37a` (`wt-mainread`); Step 3A r3 at `8228b3c2` (`wt-3a`, off `main`).

**Citation forms.** As in `L54-r2.md` (`P`, `AF`, `S2`–`S4`, `3A`, `M1`, `OA1`, `Main`, `r2:n`), and
`CF:n` = `l54/CONFIRM-r2.md`, `S1:n` = `TUNE-1-STEP2-SESSION1.md`, `SM:n` = `papers/SM.md`. The
posit ledger is at Main:724 in the pinned worktree (the proposal cites it as Main:726).

***

## 0. Verdicts

| # | Claim of `CONFIRM-r2.md` §6 | Verdict |
|---|---|---|
| 1 | Record-to-outcome map; what Q5′ compares | **CONFIRMED** |
| 2 | What the shared coordinate is | **CONFIRMED WITH CORRECTION** (wording against P:201; prior statement on `main`, S1:283–286) |
| 3 | Lemma S (`1 − 17ε`) and Corollary S1 (`ε ≥ 1/288`) | **CONFIRMED**, both constants; three hypotheses to be made explicit; "every rule" means every rule in pair form |
| 4 | Proposition E (non-additive rule, Q5′ at `ε = 0`, exchange mode, `τ = 4`) | **CONFIRMED** for Q5′ and nothing wider. Corrections: one undefined coupling; it is not an interface of the schema; it fails Q2 as well as Q3′ and Q6′ |
| 5 | Role of the target's form | **CONFIRMED WITH CORRECTION**: Theorem 1 depends on the product form of the target on the coordinates that carry the class, not on the absence of memory |
| 6 | Memory-tolerant target changes B1.1 and readmits post-hoc selection | **CONFIRMED WITH CORRECTION**: true of the unrestricted form only. Memory can be admitted with the selection requirement kept (§6.3), and Theorem 1 then stands unchanged |
| 7 | The four outcomes | (i) holds in a stated form; (ii) **REFUTED** as a universal statement, open for R-nl; (iii) holds for Lemma S, not for Theorem 1; (iv) **NOT ESTABLISHED**, and refuted for the one alternative that keeps the selection requirement |

**Headline at its exact scope.** My check supports it, and I re-derived Lemmas 1–3, Theorem 1 and
Corollary 1a of `L54-r2.md` by hand for this purpose (§7.1): *classes A, B and C fail Q5′ under its
specified target (AF:88–91 with AF:107) and record convention (D4, P:167–168, :272–277), under
hypotheses 1–7 of Theorem 1, at every `ε < 1/96` (`K ≥ 2`, empty preparation) or `ε < 1/128`
(`K ≥ 3`, Corollary 1a). That gives L5.4, L5.5 and L5.6 a definite negative answer within that
scope and no wider.* It carries H-μ, H-∞ on `ℤ^3` and H-write in exchange mode. It is a [W] result
after hand reviews, not a kernel check, and it mints no token.

***

## 1. Claim 1: the record-to-outcome map

**Source.**
- Record: "The record of the round is the **complete history of `O`**: its configuration at each of
  the `τ` ticks, `h_j ∈ ((V × V)^O)^τ`, together with `c_j`" (P:167–168).
- Outcome map: each read label "has a two-class split of its records and fixed conditional record
  laws, with Lüders target instrument `𝓘*_{c_a,h}(σ) = q_a(h|a1) P_a σ P_a` for `h ∈ a1` and
  `q_a(h|a0) (𝟙 − P_a) σ (𝟙 − P_a)` for `h ∈ a0`" (AF:88–91). The outcome is the class of the
  round's complete record.
- What is compared: "the direct total variation between the following two laws": "the world's law
  of `(r, records of T)`, conditional on the herald" and "`Σ_r w_r δ_r ⊗ 𝔔*(σ_r · T)`"
  (AF:127–130), where "`𝔔*(σ · T)` is the law of `T`'s records when the target instruments act on
  `σ`" (AF:107). Q5′ is "`F(ε; 𝒯_R)` holds for the declared target" (AF:153–154).
- The classes are not a readout: "The two-class coarse-grainings of Q5 test a property of the
  comparator `𝔔`; they are not a readout rule and do not change `d_K`, which compares complete
  records" (P:275–277).

**Derivation.** For a two-round test `(c_u, c_v)` on `σ`, composing the instruments gives
`L_uv(h_1, h_2) = π(k_1) π(k_2|k_1) q_u(h_1|k_1) q_v(h_2|k_2)` with `k_i` the class of `h_i`,
`π(k_1) = Tr(P^u_{k_1} σ)` and `π(k_2|k_1) = Tr(P^v_{k_2} P^u_{k_1})` (rank one). Given the two
classes the two records are independent, and `q_v` is one law per label and class, the same in
every round and every test ("fixed"). For a coordinate common to both records the target therefore
draws twice, independently given the classes.

**Verdict: CONFIRMED.** The reviewer's reading (CF:202–224) is the source's. Q5′ compares complete
records; the class is used only to state the target. AF:155–157 states the consequences in class
terms ("reproduces its class within `ε`"); those are consequences, not the test.

***

## 2. Claim 2: the shared coordinate

**From the definitions.** The phase space is "a pair (previous value, current value) at each site"
(P:74) and one step is `(y, x) ↦ (x, F(x) − y)` (P:78). The phase point at tick `t` is the pair of
slices `(x(t − 1), x(t))`, so consecutive phase points overlap in one slice. Round `j` lists the
phase points of `O` at ticks `(j − 1)τ + 1, …, jτ`. That these are the ticks is fixed by P:169–170:
the content moved out of `C` at the start of round `j` "is the configuration of `C` at the last
tick of round `j − 1`, part of `h_{j−1}`". Equivalently, round `j`'s record is the `τ + 1` slices
`x_O((j − 1)τ), …, x_O(jτ)`, and rounds `j` and `j + 1` share the slice `x_O(jτ)`. In exchange mode
the exchange replaces both components of `C` (P:155–157), so the shared part is `x_{O∖C}(jτ)`.

**What it is.** A state component present in both records. In the later record it sits in the
previous-value component, and the source's own words for how it gets there are "`Φ_F` copies each
cell's current value into its previous-value component" (P:201). It is not an added memory
register, not a newly measured outcome, and it carries nothing older than one tick. The same
overlap exists between any two consecutive ticks inside a round.

**Prior statement on `main`.** "without the exchange, consecutive round records share the boundary
configuration of `O` (the previous-value component of the first tick), and a qubit model cannot
carry that memory together with Q5's reads (argued, not proved)" (S1:283–286). The proposal used
the same copy effect to change a definition (P:200–205). So the observation is not new with
`REVIEW-r1.md`; Lemma S is its quantitative form (§A.31 class: ELABORATING).

**Verdict: CONFIRMED WITH CORRECTION.** CF:186–187 says it "is not a copy of earlier history made
by the rule", which reads against P:201. Replacement text: §9, K1.

***

## 3. Claim 3: Lemma S and Corollary S1

### 3.1 Lemma S, re-derived

**Hypotheses used (complete list).**
- (h1) Pair form: after one tick a cell's previous component equals its current component before
  the tick. Nothing else about the update.
- (h2) D4: a round's record lists the phase point of `O` at each of its `τ ≥ 1` ticks.
- (h3) `D = O` in initial-condition mode, `D = O ∖ C` in exchange mode, `D ≠ ∅`. `X = x_D(τ)`,
  `f(h_1)` its copy at the last tick of round 1, `f′(h_2)` its copy at the first tick of round 2.
- (h4) Target: `L_uv` as in §1, with rank-one projectors, `|a·b| ≤ 1/2`, the two classes of a label
  partitioning its records, `q_v(·|k)` supported in class `k` and the same in every test.
- (h5) Credit: for one cross test `(c_u, c_v)`, `u ≠ v`, some state has `TV(W_uv, L_uv) ≤ ε`, with
  `ε < 1/32`; and the test in which the conclusion is wanted is credited at `ε`.

**Proof.** In the world `f(h_1) = f′(h_2)` with probability 1, so `L_uv(f ≠ f′) ≤ ε`. Let `A_k`,
`B_k` be the laws of `f` under `q_u(·|k)` and of `f′` under `q_v(·|k)`, and
`s(k_1, k_2) = Σ_x A_{k_1}(x) B_{k_2}(x)`. Then `Σ π(k_1, k_2)(1 − s(k_1, k_2)) ≤ ε`. Take `k*` with
`π(k*) ≥ 1/2`; `π(k_2|k*) = (1 ± a·b)/2 ≥ 1/4`, so `π(k*, k_2) ≥ 1/8` and `1 − s(k*, k_2) ≤ 8ε` for
both `k_2`. Since `s ≤ max_x A_{k*}(x)`, the maximizer `x°` has `A_{k*}(x°) ≥ 1 − 8ε`. Since
`s ≤ A_{k*}(x°) B_{k_2}(x°) + (1 − A_{k*}(x°)) ≤ B_{k_2}(x°) + 8ε`, `B_{k_2}(x°) ≥ 1 − 16ε` for both
`k_2`. As `16ε < 1/2`, `x°` is the unique point with more than half of `B_0`, so it depends on `q_v`
only: `x^in_v`. In any credited test with second label `c_v` the target's law of `f′(h_2)` is a
mixture of `B_0, B_1`, so it gives `x^in_v` at least `1 − 16ε`; the world is within `ε`, and in the
world `f′(h_2) = X`. Hence `P_W(X = x^in_v) ≥ 1 − 17ε`. ∎

**The constant 17 is confirmed.** It is not claimed sharp and I did not try to sharpen it.

### 3.2 Corollary S1, re-derived

Initial-condition mode, `τ = 1`. `h_1` is the phase point at tick 1, `(x_O(0), x_O(1))`, and `x_O(0)`
is the current component of the fixed `r_O` (P:143). So `h_1` is a function of `X = x_O(1)`. In test
`(a, b)`, Lemma S makes `h_1` one fixed record with probability at least `1 − 17ε`, so its class is
fixed with that probability, and the target's first class has probability at least `1 − 18ε`:
`(1 − |α|)/2 ≤ 18ε`. Test `(b, a)` gives `(1 − |β|)/2 ≤ 18ε` for the same `σ`. Then
`α², β² ≥ 1 − 72ε` and `α² + β² ≤ 3/2` give `ε ≥ 1/288`. **Confirmed.** (Using
`|α| + |β| ≤ √3` instead gives `ε ≥ (2 − √3)/72 > 1/269`; the difference is immaterial.) For
`ε ≥ 1/32`, where Lemma S is not available, the conclusion holds trivially.

### 3.3 Is it independent of the rule and of the law?

- **Rule.** Yes within pair form: the proof uses (h1) and no other property of `G`. "Every rule"
  therefore means every rule on the phase space of P:74 with the update form of P:78 (which is all
  of 𝓡, and also the ring rule of SM:112). It says nothing about a first-order rule on a
  one-component state, which has no such overlap.
- **Law.** Yes. No property of `μ` is used, not even H-μ.
- **Heralds and adaptivity.** The lemma uses the world only through `f = f′`, which holds on every
  run, and the target only through the product form. `F` quantifies universally over the
  unheralded preparations (AF:134–137) and over "every `T ∈ 𝒯′`" that fits (AF:127), and the
  constant two-read tests are in `𝒯_R` (AF:104). Failing one required instance fails Q5′, so no
  herald or adaptive protocol elsewhere repairs it. **Confirmed.**
- **The empty preparation.** Corollary S1 as written needs `F` posed at `ℓ = 0`, which is the
  record's own reading (AF:389; S2:195, :200) and not a stated definition (r2:105–110).
  *Checker-authored extension, unchecked:* the proof of Lemma S goes through for any admissible
  preparation with weights `w_r` (replace `π` by `Σ_r w_r π_r`; `π_r(k_2|k_1)` does not depend on
  `r`). For an unheralded prefix of length `ℓ ≥ 1` with one weight vector for the tests `(a, b)` and
  `(b, a)`, `τ = 1`, `K ≥ 3`: `h_{ℓ+1}` is a function of `(r, x_O(ℓ + 1))`, so
  `Σ_r w_r (1 − |α_r|)/2 ≤ 18ε` and likewise for `β_r`, and `|α_r| + |β_r| ≤ √3` gives
  `ε ≥ (2 − √3)/72`.

### 3.4 What kind of result Corollary S1 is

The proposal met the same situation once and treated it as a defect of a definition, not as a
result about rules: blocks inside `O` "are excluded because the definitions alone would then fail
every rule" (P:200). By that standard Corollary S1 says that at `τ = 1` in initial-condition mode
the definitions alone fail every rule. It is a property of how D4 partitions ticks into rounds. It
is not evidence about any dynamics, and it should go to the owner in that form (r2:491–494 already
frames the question).

**Remark at CF:271–276 (R2 at every `τ`).** Checked: `x(τ) = P_τ(A)x(0) − P_{τ−1}(A)y(0)` with
`P_0 = 1`, `P_1 = A`, `P_{t+1} = A P_t − P_{t−1}`; `(A^τ)_{i, i+τe} = 1` and lower powers do not
reach distance `τ`. With that site outside `O ∪ P` under the uniform product law, `x_i(τ)` is
uniform and Lemma S gives `ε ≥ 1/34`. Correct as stated, with its stated restrictions.

**Verdict: CONFIRMED.** Additions to the hypothesis list: §9, K2.

***

## 4. Claim 4: Proposition E

### 4.1 The rule, and reversibility

`V = ℤ/2`. Sites: `O = {o, p, κ, κ₂}`, `C = {o}`; unread: `A`, `B`, `r_1, …, r_N`, `N ≥ 4K + 4`.
One tick: `x_s(t + 1) = G_s(x(t)) + x_s(t − 1)` (mod 2), with

| Site | `G_s(x)` |
|---|---|
| `o`, `κ` | `0` |
| `κ₂` | `1` |
| `p` | `(1 + x_κ)·[(1 + x_o) x_A + x_o x_B]` |
| `A` | `x_κ (1 + x_{κ₂}) · x_o · x_{r_1}` |
| `B` | `x_κ (1 + x_{κ₂}) · (1 + x_o) · x_{r_1}` |
| `r_1` | `x_{r_2}` |
| `r_i`, `2 ≤ i ≤ N − 1` | `x_{r_{i+1}} + x_{r_{i−1}}` |
| `r_N` | not given at CF:291; take `x_{r_{N−1}}` (it is never reached within the horizon) |

Ready: `p = (0, 0)`, `κ = (1, 0)`, `κ₂ = (0, 0)` as (previous, current). Unread cells uniform, both
components. Read labels `c_a = (0, 0)`, `c_b = (1, 1)`.

**Bijection.** For any `G`, `(y, x) ↦ (x, G(x) − y)` has the inverse `(y′, x′) ↦ (G(y′) − x′, y′)`.
Checked: `y′ = x`, `x′ = G(x) − y`, so `G(y′) − x′ = y`. Reversible, for every `G`. `G` is not
additive (products `x_o x_A`, `x_o x_B`, `x_o x_{r_1}`), and no `G_s` depends on `x_s`.

### 4.2 Time-stepping, by hand

*Clocks.* `x_κ(−1) = 1`, `x_κ(0) = 0`, `x_κ(t + 1) = x_κ(t − 1)`: `x_κ(t) = t mod 2`.
`x_{κ₂}(−1) = x_{κ₂}(0) = 0`, `x_{κ₂}(t + 1) = 1 + x_{κ₂}(t − 1)`: `0, 1, 1, 0, 0, 1, 1, 0, …` for
`t = 0, 1, 2, …`, period 4. So `1 + x_κ = 1` exactly at even `t`, and `x_κ(1 + x_{κ₂}) = 1` exactly
at `t ≡ 3 (mod 4)`.

*One round, starting at `T ≡ 0 (mod 4)` with label `(c^y, c^x)`.* Entering: `x_p(T − 1) = x_p(T) = 0`;
`β_A, β_B` the values of `x_A, x_B` at even times, `γ_A, γ_B` at odd times;
`k := (1 + c^x) β_A + c^x β_B`; `f := x_{r_1}(T + 3)`.

| `t` | `x_κ` | `x_{κ₂}` | `x_o` | `x_A` | `x_B` | `G_p` | `G_A` | `G_B` | `x_p(t)` |
|---|---|---|---|---|---|---|---|---|---|
| `T` | 0 | 0 | `c^x` | `β_A` | `β_B` | `k` | 0 | 0 | 0 |
| `T+1` | 1 | 1 | `c^y` | `γ_A` | `γ_B` | 0 | 0 | 0 | `k + x_p(T−1) = k` |
| `T+2` | 0 | 1 | `c^x` | `β_A` | `β_B` | `k` | 0 | 0 | `0 + x_p(T) = 0` |
| `T+3` | 1 | 0 | `c^y` | `γ_A` | `γ_B` | 0 | `c^y f` | `(1 + c^y) f` | `k + k = 0` |
| `T+4` | 0 | 0 | `c^x` | `β_A + c^y f` | `β_B + (1 + c^y) f` | | | | `0 + x_p(T+2) = 0` |

Each entry of a row is computed from the two rows above it. The entering assumption on `p` holds
again at `T + 4`; initially it holds by the ready configuration. The odd-time register values
`γ_A, γ_B` never enter `G_p` (the factor `1 + x_κ` vanishes at odd times) and never change.

*Record of the round* (phase points of `O` at `T + 1, …, T + 4`, with `c_j`):
`o`: `(c^x, c^y), (c^y, c^x), (c^x, c^y), (c^y, c^x)`; `p`: `(0, k), (k, 0), (0, 0), (0, 0)`;
`κ`: `(0, 1), (1, 0), (0, 1), (1, 0)`; `κ₂`: `(0, 1), (1, 1), (1, 0), (0, 0)`. It is a fixed injective
function of `(c_j, k)`, the same function in every round because the clocks have period `4 = τ`.

*Fresh bits.* The chain is autonomous and linear. By induction on `t`, `x_{r_i}(t)` contains
`x_{r_{i+t}}(0)` with coefficient 1 and no cell beyond `r_{i+t}`: true at `t = 0, 1`
(`x_{r_i}(1) = x_{r_{i+1}}(0) + x_{r_{i−1}}(0) + y_{r_i}(0)`), and
`x_{r_i}(t + 1) = x_{r_{i+1}}(t) + x_{r_{i−1}}(t) + x_{r_i}(t − 1)` carries it forward. So the bit
used in round `j`, `f_j = x_{r_1}(4j − 1)`, is `x_{r_{4j}}(0)` plus a function of lower cells. The
map to `(f_1, …, f_K)` is triangular, so these are independent fair bits, independent of
`x_A(0), x_B(0)`. Everything recorded through round `j` and the registers before its last tick are
functions of `x_A(0), x_B(0), f_1, …, f_{j−1}` and the labels.

*The four menu labels.* Reading the table:

| Label `(c^y, c^x)` | shows | re-randomizes |
|---|---|---|
| `(0, 0) = c_a` | `β_A` | `β_B` |
| `(1, 1) = c_b` | `β_B` | `β_A` |
| `(0, 1)` | `β_B` | `β_B` (after showing it) |
| `(1, 0)` | `β_A` | `β_A` (after showing it) |

*A numerical run.* `β_A = 1, β_B = 0`. Round 1, `c_a`, `f_1 = 1`: `k = 1`, `x_p = 0, 1, 0, 0, 0`,
then `β_B = 1`. Round 2, `c_b`, `f_2 = 0`: `k = β_B = 1`, `x_p = 0, 1, 0, 0, 0`, `β_A` stays 1.
Round 3, `c_b`: `k = 1` again.

### 4.3 Q5′, clause by clause

- *Target.* `a·b = 0 ∈ [−1/2, 1/2]`. Split of `c_u`'s records by `k`; `q_u(·|k)` the point mass on
  the record of `(c_u, k)`; supports disjoint; the same in every round. (AF:88–91.)
- *Admissible preparations.* Every prefix of a protocol of `Π_K`, adaptive, with any of the four
  labels (AF:116; P:147–148, :172–173). No heralded preparation is used by any proof here, so none
  is quantified over (AF:118–120).
- *Hidden situation after a prefix record.* One of: `S_A(v)` (`β_A = v` known, `β_B` uniform and
  independent of the record), `S_B(v)`, `S_∅` (both uniform, independent). Start: `S_∅`. The twelve
  transitions, re-derived:

  | From | `(0,0)` | `(1,1)` | `(0,1)` | `(1,0)` |
  |---|---|---|---|---|
  | `S_∅` | fair `k` → `S_A(k)` | fair `k` → `S_B(k)` | fair `k` → `S_∅` | fair `k` → `S_∅` |
  | `S_A(v)` | `k = v` → `S_A(v)` | fair `k` → `S_B(k)` | fair `k` → `S_A(v)` | `k = v` → `S_∅` |
  | `S_B(v)` | fair `k` → `S_A(k)` | `k = v` → `S_B(v)` | `k = v` → `S_∅` | fair `k` → `S_B(v)` |

  The set is closed, and given the record the future depends on it only through the situation.
- *Assignment.* `S_A(v) ↦` the eigenstate of `a` of class `v`; `S_B(v) ↦` that of `b`;
  `S_∅ ↦ 𝟙/2`. One assignment per preparation, the same for every test (AF:125–127).
- *Tests.* Under `c_a, c_b` the first two columns are the Lüders kernel for `a·b = 0` on these five
  states, record by record. A test whose labels depend on its own records (AF:99–100) is a
  composition of the same kernels. So the world's law of `(r, records of T)` equals
  `Σ_r w_r δ_r ⊗ 𝔔*(σ_r · T)` for every `T ∈ 𝒯_R` with `ℓ + |T| ≤ K`. `F(0; 𝒯_R)` holds.
- *Consistency with the necessary conditions.* `x_{O∖C}(4j) = (0, 0, 0)`, one configuration
  (Lemma S). `(c_a, c_a)` has 2 atoms and `(c_a, c_b)` has 4, so (T) fails (Lemma 5).

**Verdict: CONFIRMED.** Independently checked scope, stated exactly: *for this one rule, on this
site set, under the uniform law, in exchange mode under H-write with `τ = 4`, complete-history
records (D4) satisfy Q5′ at `ε = 0` for a target with `a·b = 0`, at every `K` with `N ≥ 4K + 4`.*
Two hand derivations now exist (the reviewer's and this one).

### 4.4 Admissibility, and what it does not meet

- **H-write.** Required. Exchange mode's write access is "assumed as the named hypothesis
  **H-write** … and carried into every conclusion obtained in exchange mode" (P:158–160). It is not
  adopted.
- **`τ = 4`.** Allowed: "`τ ≥ 1`, the duration of one round, in ticks, the same for every label"
  (P:142).
- **Not an interface of the schema.** `Λ` is not a torus or `ℤ^3` (P:123–129) and `G` is not in 𝓡
  (P:85–112). D2 and D7 fail; the family is "supplied" (P:226). CF:329–331 says the rule is not in
  𝓡; it should also say the carrier is not in 𝓛.
- **Q3′ and Q6′ fail.** Four labels: no label has a record law independent of the prepared state
  (each shows a register), so no `c(0)`; credited means lie in the plane of `a, b`. NL-C applies
  (`|C| = 1`). As CF:331 says.
- **Q2 fails too** (*checker-authored, unchecked;* not in CF). Take `K ≥ 3` and `ε = 0`. After
  `(1,1)` the label `(0,1)` repeats the class, so its two class effects annihilate each other's
  input states; in `ℂ²` they are then complementary rank-one projectors, and every instrument
  element under a rank-one effect is measure-and-prepare: the post-state does not depend on the
  input. But `(0,0), (0,1), (0,0)` gives `k_3 = k_1` with `k_2` fair and independent: after `(0,1)`
  the state still determines `k_1`. No qubit model has both. (A positive floor in `ε` was not
  derived.) The world is a two-bit model with one bit hidden at a time, not a qubit.
- **The target is incomplete as a declaration.** B1.1 requires a gate label `c(θ)` for each `θ`
  (AF:86–87). Q5′ does not test them, so this does not affect §4.3.

**What it shows, exactly.** One reversible pair-form rule meets one requirement. It is a
counterexample to the universal statement "pair form, D4 records, the AF target and exchange mode
together make Q5′ fail", and to nothing else. It is not a rule meeting the single-qubit target T1:
Q2, Q3′ and Q6′ fail.

**Relation to `main`.** The proposal already stipulates a second-order rule outside 𝓡 that passes:
C-PROG's `F_U`, for which the Q-conditions are "not derived; `F_U` is assumed to reproduce the
compiled controller's record law" (P:687). Session 4 draws the consequence: a proof against R-nl
"must also use a property of R-nl that some reversible rule with an unread uniform environment
lacks … A property shared by every second-order rule would contradict that row" (S4:399–402).
Proposition E is an explicit, hand-stepped instance of that statement for Q5′ alone (§A.31 class:
ELABORATING). Corollary S1 bounds the stipulation: no such rule can have `τ = 1` in
initial-condition mode.

### 4.5 Coordinator's addition B: class D, and the native dynamics

**Class D** is "every R-nl family, under every law on the list, both modes and both carriers", with
R-nl `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q` under H-nl and `sup_n |C_n| = ∞` (3A:714–717).

| Assumption of class D | Proposition E's rule |
|---|---|
| second-order pair form (P:78; ledger item (xiii)) | meets |
| reversible | meets |
| finite alphabet `ℤ/q`, site-factorized configuration space (item (viii)) | meets (`q = 2`) |
| D4 complete-history records, fixed `r_O`, `τ` the same for every label | meets |
| a law on the D3 list, H-μ | meets (uniform) |
| exchange mode under H-write | meets (this mode only) |
| the map is R-nl: one rounded nearest-neighbour sum at every site | **does not meet**: `G` differs from site to site and multiplies chosen cells |
| nearest-neighbour range on the simple-cubic graph (item (x)); translation covariance (item (xi), first clause) | **does not meet** |
| bounded coupling degree (item (ix)); `G_s` independent of `x_s` | meets |
| carrier in 𝓛 (torus or `ℤ^3`) | **does not meet** |
| unbounded control regions, `sup_n` of the size of `C_n` infinite (the undecided part of the class) | **does not meet** (one control cell) |

It is not a member of class D and supplies no evidence that an R-nl family meets Q5′. Its bearing
on class D is the one S4:399–402 already states, now with an explicit instance: any proof that
class D fails Q5′ must use a property of R-nl beyond pair form, D4, the AF target, the uniform law
and exchange mode. 3A's caution applies to it as to OA-2's designed computer: "non-affinity, or even
G3 at bounded horizon, is not evidence of a quantum-capable interface" (3A:757–758).

**The linear rule.** No bearing. R-lin is additive and Theorem 1 covers it; Proposition E is not
additive. Its only role for R-lin is as a control that Theorem 1's interface does not prove too
much.

**The ring rule** (SM:112: on a ring of `L ≥ 4` sites,
`x_i(t+1) = x_{L(i)}(t) + x_{R(i,x(t))}(t) − x_i(t−1) mod q`, `R(i, x) = i + 2` if `x_{i+1} = 0` and
`i + 1` otherwise). Shared with Proposition E: second-order form, hence bijectivity ("automatic
for any second-order reversible dynamics, regardless of whether the coupling is state-dependent",
SM:106); non-additivity; `G_i` independent of `x_i` (SM's constraint (ii)); bounded coupling
degree. Not shared: translation invariance, one local map at every site, the ring carrier.
Proposition E does not instantiate the ring rule and says nothing about what the ring rule does
under any interface. Two things do apply to the ring rule, to R-nl and to R-lin alike, because they
use pair form only: Lemma S and Corollary S1, if those rules are read through this interface. The
ring rule is not in TUNE-1's 𝓡, whose carriers are three-dimensional (P:85–129), so even that is
outside the schema.

### 4.6 Initial-condition mode (*checker-authored; one hand derivation; unchecked*)

CF:333–338 gives a sketch only. I completed one construction by hand. It is offered for checking
and is relied on nowhere above.

**Construction E′.** `V = ℤ/2`, `τ = 14`. `O = {p, m_0, …, m_13}`. Blocks: a cyclic tape
`b_0, …, b_{n−1}`, `n = K_n ≥ max(K, 3)`, with `P_j = {b_{j−1}}` and a label `(c^y, c^x)` the
content of one cell. Unread: `A, B, r_1, …, r_N`, `N ≥ 14K`, uniform. Ready: `p = (0, 0)`,
`m_i = (δ_{i,13}, δ_{i,0})`. Write `u_φ = x_{m_φ}`.

| Site | `G_s(x)` (indices of `m` mod 14, of `b` mod `n`) |
|---|---|
| `m_i` | `x_{m_{i−1}} + x_{m_{i+1}}` |
| `p` | `(u_0 + u_2)·[(1 + x_{b_0}) x_A + x_{b_0} x_B]` |
| `A` | `u_3 · x_{b_0} · x_{r_1}` |
| `B` | `u_3 · (1 + x_{b_0}) · x_{r_1}` |
| `b_i` | `(u_4 + u_5 + u_6 + u_9 + u_10 + u_11) x_{b_i} + (u_6 + u_7 + u_8) x_{b_{1−i}} + (u_11 + u_12 + u_13) x_{b_{−i}}` |
| `r_i` | as in Proposition E |

**Verification.**
1. *Clock.* `x_{m_i}(t) = [i ≡ t mod 14]`: the right-hand side `[i ≡ t+1]` equals
   `[i−1 ≡ t] + [i+1 ≡ t] + [i ≡ t−1] = [i ≡ t+1] + 2[i ≡ t−1]`. So `u_φ(t) = 1` exactly in phase
   `φ = t mod 14`, and the clock's record has period `14 = τ`.
2. *Read phase* (`φ = 0, …, 3`). `G_{b_i} = 0`, so `x_{b_0}` is `c^x, c^y, c^x, c^y, c^x`. `G_p` is
   on at `φ = 0, 2` and `G_A, G_B` at `φ = 3`. This is the table of §4.2 with `b_0` in place of `o`:
   `x_p = 0, k, 0, 0, 0`, then one register re-randomized. `p` stays `0` for the rest of the round.
3. *Shift phase* (`φ = 4, …, 13`). Let `(E, Z)` be the tape's (previous, current) layers at
   `T + 4`; they are the layers at `T`. For an involution `ρ` of the positions with matrix `P`
   (`(Pv)_i = v_{ρ(i)}`, `P² = 1`), five ticks with `G = x`, `x`, `(P + 1)x`, `Px`, `Px` give

   | after tick | (previous, current) |
   |---|---|
   | 1 | `(Z, Z + E)` |
   | 2 | `(Z + E, E)` |
   | 3 | `(E, PE + Z)` |
   | 4 | `(PE + Z, PZ)` |
   | 5 | `(PZ, PE)` |

   Phases 4–8 do this with `ρ_1(i) = 1 − i`, phases 9–13 with `ρ_2(i) = −i`, giving
   `(P_2 P_1 E, P_2 P_1 Z)` at `T + 14`, and `(P_2 P_1 v)_i = v_{ρ_1(ρ_2(i))} = v_{i+1}`. The whole
   tape, both layers, has moved one position towards `b_0`, whatever its content. In round `j` the
   cell `b_0` holds the label of block `j`.
4. *Records.* The record of a round is a fixed function of `k`, the same in every round. Records
   before round `j` do not depend on the label of block `j`. `x_O(14j)` is one configuration.
5. *Q5′.* The hidden process is that of §4.3 (protocols are non-adaptive in this mode, P:199).
   `F(0; 𝒯_R)` holds for `a·b = 0` at every `K ≤ K_n`.

It uses no H-write. It has every limitation of §4.4: not in 𝓡, not in 𝓛, Q2, Q3′ and Q6′ fail.

***

## 5. Claim 5: the role of the target's form

**(a) "The target has no persistent memory."** Confirmed, stated more exactly: between rounds the
target carries the qubit state and nothing else, and after a Lüders read that is the class, one
bit; a round's record law depends on label and class only (§1). This is not peculiar to B1.1. Q2's
comparator has the same shape, instruments on `ℂ²` whose outcomes are the round records
(P:433–437), and it bounds visible retention by itself. *Checker-authored, unchecked:* if in a test
`(c_a, c_b, c)` from `𝟙/2` with `a·b = 0` the third record determines both earlier classes, then for
any qubit model the event "decoded pair = actual pair" has probability at most
`Σ_i p_i Tr(E_i) ≤ 2 max_i p_i ≤ 1/2 + 2 d_K`, against 1 in the world, so `d_K ≥ 1/6`.

**(b) "Theorem 1 depends on that."** Correct as a statement about the proof: step 3 uses
`dep(L_aa) ≠ dep(L_ab)`, which is Lemma 3 and needs the product form given the classes. It needs
correction as a statement about memory: the proof uses the product form only for the coordinates
that carry the class. Proposition M (§6.3) shows the theorem survives a target that has a declared
place for retained history.

**(c) The two-round additive example (CF:367–372).** Checked. Give every record the coordinates
`(g_a, g_b, t_a, t_b, λ)`, with `λ` null in round 1. Class of a `v`-round: `g_v` if `λ` is null or
`λ = v`, else `t_v`. Then `(a, a)`: `(g_a, g_a)`; `(a, b)`: `(g_a, t_b)`, independent fair bits, and
`t_b` is independent of the whole first record; likewise `(b, b)`, `(b, a)`. Those are the Lüders
class laws for `a·b = 0` from `𝟙/2`. The label enters only as the shift `λ`. **Confirmed**, with its
scope: an abstract additive world, two rounds, four tests, classes only. It is not an R-lin
interface of the schema, and r2's control K4 (r2:366–370) already makes the same point with a
smaller toy. *Checker-authored, unchecked:* with one fresh pair per round and the label history as
the shift, the class "`t^i_v`, `i` the first round of the current run of `v`" gives the Lüders
class law on every non-adaptive test of `𝒯_R`, so the limitation to two rounds is not essential at
class level.

**(d) Dynamics, or the comparison?** Decided as follows.
- *Not the comparison alone.* The same comparison, complete-history records against the same
  target, is passed at `ε = 0` by a non-additive rule (§4). Complete-history records do not force a
  rule to retain history in `O`: Proposition E returns `O` to one configuration and keeps the
  memory in unread cells.
- *Not "no place for retained history".* The proof of Theorem 1 never uses the shared slice or any
  retained coordinate. It holds unchanged with the duplicated slice removed (CF:391, checked: the
  reduced records are still additive images) and with a declared place for retained history
  (Proposition M).
- *What it does need from the interface.* That classes are carried by record coordinates fixed
  independently of the label and compared at the level of complete records, with no decoder. Under
  a class-level comparison the conclusion is unavailable (the toy of (c)); that is the removal of
  the decoder guard of D4 (P:272–277), not the admission of memory.

So Theorem 1's failure comes from the dynamics, namely property (T), which additivity implies
(Lemma 1) and a passing rule must lack (Lemma 5), read under a comparison that admits no decoder.

**Verdict: CONFIRMED WITH CORRECTION.** Replacement text: §9, K5 and K7.

***

## 6. Claim 6 and the coordinator's addition A

### 6.1 What B1.1 says, and why it is there

B1.1 (AF:82–112) makes the target part of the family's specification and gives each read label "a
two-class split of its records and fixed conditional record laws" with a Lüders instrument
(AF:88–91). Its stated reason is Session 1's root cause RC-1: "Components of `𝔔` that no record of
`Π_K` tests can be chosen freely" (S1:148–151), with Rd-3, Q5 read through effects only so that "No
post-measurement update is required" (S1:94–96). The amendment's summary: the tests "were checked
on a freely chosen quantum model of the records … reads must behave like ideal repeatable
measurements" (AF:36–40), and "No freely chosen model enters it" (AF:139–140). B1.1 was not written
as a guard against memory or against post-hoc selection. The guard against a chosen decoder is
older and sits in D4.

### 6.2 The clause that connects memory and selection, and the step

**The clause.** AF:88–91: "Each has a two-class split of its records and fixed conditional record
laws". One clause states both the split and the fixed laws on the *whole* round record. D4 states
what that protects: "No pointer function, response function, threshold or decoder is chosen. …
The two-class coarse-grainings of Q5 test a property of the comparator `𝔔`; they are not a readout
rule and do not change `d_K`, which compares complete records" (P:272–277). The source's names for
the excluded thing are M1 Corollary A′, "Choosing afterwards which record to consult" (M1:424), and
OA-1 D7, "every 'selectable' read is a coarse-graining of one joint record" (OA1:204–205). No
sentence of the source links memory to selection; the link is that one clause does both jobs.

**The step.** Relax AF:88–91 only by deleting "fixed": let `q_v(h_j | k_j, h_1, …, h_{j−1})` be any
declared kernel, with the split still a split of whole records. A target of that form is
`Π_j π(k_j | k_{<j}) q(h_j | k_j, h_{<j})`. Any world law factors as
`Π_j W(k_j | h_{<j}) W(h_j | k_j, h_{<j})`. A family that declares `q := W(· | k_j, h_{<j})` has total
variation 0 exactly when `W(k_j | h_{<j}) = π(k_j | k_{<j})`. So the relaxed test is: *the classes
follow the Lüders law given the complete earlier records.* Nothing about the records beyond their
classes is tested, the split is then the only tested function of the record, and it may read the
retained coordinates. It has become the readout rule that P:275–277 says it is not. The additive
toy of §5(c) passes this test. That is the route from unrestricted memory tolerance to post-hoc
selection.

### 6.3 Does memory tolerance necessarily weaken the selection requirement?

**No.** The two are separable, and memory can be admitted with the selection requirement kept as
written. The form of target that does it (*checker-authored, unchecked*):

> 1. One split of the coordinates (cells and ticks) of a round record into a retained part and an
>    outcome part, `h = (m, e)`, the same for every label and every round.
> 2. AF:88–91 verbatim on `e`: a two-class split of the outcome parts, fixed conditional laws
>    `q_u(e | class)`, the Lüders instrument.
> 3. For `m_j`, a declared kernel given the earlier complete records and labels (in the strictest
>    form a declared function: a log). No split reads `m`.
> 4. Credit as in AF:125–130: direct total variation on complete records, `m` and `e` together.

**Proposition M.** Assume hypotheses 1–5 of Theorem 1 and D4 records. Let `ρ` be a coordinate
projection of round records, the same for both read labels and both rounds, and let each `L_uv` be
any law on `(h_1, h_2)` whose image under `ρ × ρ` has the form of Lemma 3 for one `σ`, with
`|a·b| ≤ 1/2`. If `TV(W_uv, L_uv) ≤ ε` for the four tests, then `ε ≥ 1/96`.
*Proof.* `ρ × ρ` does not increase total variation. `ρ` is a group homomorphism, so by Lemma 1 the
projected law of `(a, b)` is a coordinatewise shift of that of `(a, a)`. Lemmas 2 and 3 and steps
2–5 of Theorem 1 apply to the projected laws. ∎

So under the target of items 1–4 every additive rule fails exactly as before, whatever the retained
part holds: the duplicated boundary slice, a log of earlier classes, the label history. AF as
written is the case `e = h`; the reviewer's "drop the duplicated slice" row (CF:391) is the case
`m =` the first-tick previous component.

**Item 1 is the selection guard.** If the outcome coordinates may depend on the label, a static
world passes: every record is `(g_a, g_b)`, fair and independent, labels act on nothing, an
`a`-round's outcome part is the first coordinate and a `b`-round's the second. The four two-round
class laws are then exactly Lüders for `a·b = 0`. That is "choosing afterwards which record to
consult" in its plainest form, and it is what item 1 excludes.

### 6.4 Available in the schema, or an interface change? Is information discarded?

- **The schema as written already keeps the full accessible history and distinguishes the current
  outcome**, at the level of rounds: the history is the held list `(h_1, …, h_K)` whose joint law
  is compared (P:181–182; 3A:501 calls this the imported convention MP-0b, "the visible history
  counts as held"), and the current outcome is the class of the current record.
- **What it does not allow** is a round record part of which is retained history with a law that
  depends on earlier records. That is not a reading of AF:88–91; it is a change to B1.1, and to
  more than B1.1: Q2's comparator has no place for it either (§5(a)), and Q1 counts what
  continuation records distinguish (P:450–453). It is an interface change and an owner decision.
  The reviewer's "a change to AF B1.1" (CF:400) is right and incomplete.
- **Neither form discards information** an embedded observer can access: credit is on complete
  records in both. The class-only and thresholded alternatives do discard it and are contrary to D4
  and D5 (CF:393, confirmed).
- For comparison, Main's own finite realization keeps its record inside the visible sector: the
  step "writes the outcome to the visible register" and the instrument is "selected by the protocol
  from the retained record" (Main:578, :580). TUNE-1 represents the same retention as a held list
  outside the lattice. The two are different representations of the observer's memory; neither is
  lossy.

**Verdict: CONFIRMED WITH CORRECTION.** "A memory-tolerant target would readmit post-hoc selection"
holds for the unrestricted form of §6.2 and fails for the form of §6.3. Replacement text: §9, K6.

***

## 7. Claim 7: which of the four outcomes holds

### 7.1 Theorem 1, re-derived for the headline

- *Lemma 1.* `Φ_F` with additive `F` is a group endomorphism; the time-zero configuration is the
  sum of `r_O`, the labels and `u`; an exchange `x ↦ (I − Π_C)x + ι(c_j)` is additive in `(x, c_j)`.
  So `h(c′, u) = h(c, u) + H(c′ − c)`, and by H-μ the record laws are coordinatewise shifts. ✓
- *Lemma 2.* `dep` is invariant under coordinatewise bijections; `|dep(P) − dep(P′)| ≤ 3 TV(P, P′)`. ✓
- *Lemma 3.* With disjoint class supports, `dep(L_uv) = ½ Σ |π(k_1, k_2) − π(k_1)π(k_2)|`, four
  equal moduli. For `aa` the modulus is `p − p²`. For `ab` it is
  `p(1+c)/2 − p[p(1+c)/2 + (1−p)(1−c)/2] = p(1 − p)c`. ✓
- *Theorem 1.* `2p_a(1 − p_a)(1 − |c|) ≤ 6ε`, so `1 − α² ≤ 24ε`; likewise `β`;
  `α² + β² ≤ 1 + |c| ≤ 3/2`; `ε ≥ 1/96`. ✓
- *Corollary 1a.* `D(Q) = TV(Q, Q̃)`, `TV(Q̃, Q̃′) ≤ 3 TV(Q, Q′)` (checked by a hybrid),
  `Σ_r w_r (1 − α_r²) ≤ 32ε`, `ε ≥ 1/128`. ✓ It assumes one weight vector on the prefix records for
  the four tests, as r2:246–248 states.

### 7.2 The four outcomes

- **(i) Specific to additive dynamics.** *Holds in this form:* the failure Theorem 1 proves is
  caused by a property of the dynamics, (T), which every additive rule has under hypotheses 1–5,
  and the interface does not impose that failure on every second-order rule (§4). *Does not hold*
  as "only additive rules fail": any rule with (T) fails (Lemma 5), any rule at `τ = 1` in
  initial-condition mode fails (Corollary S1), and nothing is known about R-nl.
- **(ii) Every rule under the complete-history interface.** *Refuted* as a statement about every
  pair-form rule, in exchange mode under H-write (§4, two derivations) and in initial-condition
  mode (§4.6, one derivation, unchecked). *True* in the corner `τ = 1`, initial-condition mode
  (§3.2). *Checker-authored, unchecked:* also at `τ = 1` in exchange mode under the uniform law. By
  Lemma M (S4:94–101) the unread cells at tick 1 are uniform and independent of `x(0)`, hence of
  `h_1`; `h_2` is a function of `c_2`, `x_{O∖C}(1)` and those cells; by Lemma S `x_{O∖C}(1)` is
  fixed up to `17ε`; so `dep(W_uu) ≤ 34ε`, `(1 − α²)/2 ≤ 37ε`, likewise `β`, and `ε ≥ 1/296`.
  *Within the schema,* whose rules are R-lin and R-nl, (ii) is equivalent to "R-nl fails Q5′",
  which is open.
- **(iii) A shared record read against a target without memory.** *Holds for Lemma S and Corollary
  S1:* those constraints exist only because one slice is listed in two records that the target
  draws independently. *Does not hold for Theorem 1:* §5(d).
- **(iv) Disappears under a valid alternative representation.** *For Corollary S1:* its proof needs
  the duplicated slice and does not survive removing it; whether some rule at `τ = 1` then passes
  was not derived. *For Theorem 1:* not established for any alternative, and refuted for the one
  alternative I can state that admits memory and keeps the selection requirement (Proposition M).
  Under a class-level comparison an abstract additive world passes (§5(c)); that alternative gives
  up D4's guard, and no R-lin interface realizing it is exhibited.

### 7.3 Strongest statement I can prove

1. (Theorem 1, Corollary 1a; three hand derivations.) Under hypotheses 1–7, every interface with an
   additive rule fails Q5′ at `ε < 1/96` (`K ≥ 2`, empty preparation) or `ε < 1/128` (`K ≥ 3`).
2. (Proposition M; one derivation.) Statement 1 holds for every target whose restriction to a
   label-independent set of record coordinates has the form of AF:88–91.
3. (Lemma S, Corollary S1; two derivations.) For every pair-form rule and every law, a credited
   interface has `x_D(jτ)` on one configuration up to `17ε`, and none exists with `τ = 1` in
   initial-condition mode below `1/288`.
4. (Proposition E; two derivations.) There is a reversible pair-form rule, outside 𝓡 and 𝓛, that
   meets Q5′ at `ε = 0` in exchange mode under H-write. It fails Q2, Q3′ and Q6′.

Statements 1–4 hold together with no conflict: the interface constrains every rule (3), excludes
every additive rule (1, 2), and does not exclude every rule (4).

### 7.4 Exact open questions

1. Is there an R-nl interface in 𝓛, in either mode, that meets Lemma S and Lemma 5 at small `ε`?
   (Part of NL-P; owner decision 4 authorizes no work on it, S4:608–611.)
2. An independent check of §4.6. Then: the least `τ` at which some pair-form rule meets Q5′, in
   initial-condition mode (`2 ≤ τ ≤ 13`) and in exchange mode (`τ = 1` under a non-uniform law;
   `τ = 2, 3`).
3. Can any pair-form rule meet Q2 and Q5′ together under D4, so that every menu label is a qubit
   instrument? Proposition E does not. C-PROG stipulates it and derives nothing (P:687).
4. A translation-invariant rule of range one on a carrier of 𝓛, in place of the designed ones.
5. Is there an R-lin interface realizing the class-level toy of §5(c)? This is outside TUNE-1 (D4,
   D5) and is r2's open item 3 (r2:506–508).
6. Owner questions: whether the `τ = 1` corner is intended (P:200–205 is the precedent for changing
   a definition); and, if a memory-tolerant target is ever wanted, whether items 1–4 of §6.3 are
   its form, with the matching change to Q2.

***

## 8. Checker-authored items (none checked by anyone)

| Item | Where | Derivations |
|---|---|---|
| Lemma S for any admissible preparation; Corollary S1 without the empty preparation, `(2 − √3)/72` | §3.3 | 1 |
| Proposition E fails Q2 at `ε = 0`, `K ≥ 3` | §4.4 | 1 |
| Construction E′ (initial-condition mode, `τ = 14`) | §4.6 | 1 |
| Visible retention of two classes gives `d_K ≥ 1/6` | §5(a) | 1 |
| Class-level additive world on all non-adaptive tests of `𝒯_R` | §5(c) | 1 (sketch) |
| Reduction of the unrestricted memory-tolerant test to a class-level test | §6.2 | 1 |
| Proposition M and the label-independence countercase | §6.3 | 1 |
| `τ = 1`, exchange mode, uniform law: `ε ≥ 1/296` | §7.2 (ii) | 1 |

Controls I ran on my own additions (§A.21): Proposition M is applied to the toy of §5(c) and to
r2's K4 toy and excludes both for every label-independent choice of outcome coordinates, as it
must; it does not exclude Proposition E (take `m` empty); and its hypothesis of label independence
is necessary (the static world of §6.3).

***

## 9. Corrections to `CONFIRM-r2.md`, with replacement text

**K1 (CF:186–187).** Replace "It is a physical state component that the record lists twice. It is
not a copy of earlier history made by the rule, and it is not a newly measured outcome." by:

> It is one time slice of the state, `x_D(jτ)`, listed in both records. The phase point of a
> second-order rule is two consecutive slices (P:74), consecutive phase points overlap in one, and
> D4 lists every phase point of `O`. In the later record the slice sits in the previous-value
> component, which the rule fills by copying the current value (P:201). It is not an added memory
> register and not a newly measured outcome, and it carries nothing older than one tick. The
> overlap is stated on `main` for initial-condition mode (S1:283–286, "argued, not proved");
> Lemma S is its quantitative form.

**K2 (CF:240, after (S5)).** Insert:

> - (S6) The projectors of (S4) have rank one; the two classes of a label partition its records
>   and `q_v(·|k)` is supported in class `k` (AF:88–91); `D` is not empty (for `O = C` in exchange
>   mode the statement is empty). Corollary S1 also uses that `r_O` is fixed (P:143) and that `F`
>   is posed for the empty preparation (AF:389; S2:195, :200).

and at CF:269, after "∎", add:

> By the standard of P:200 ("the definitions alone would then fail every rule") this is a property
> of the tick partition at `τ = 1`, not of any dynamics.

**K3 (CF:291).** After "for `i ≥ 2`" add "(`G_{r_N} = x_{r_{N−1}}`; the end of the chain is not
reached within the horizon)".

**K4 (CF:329–331).** Replace the paragraph "What the construction is not." by:

> **What the construction is not.** It is not an interface of the schema: `G` is designed,
> site-dependent and not nearest-neighbour, so `F ∉ 𝓡`, and the site set is not in 𝓛; D2 and D7
> fail. It is not R-nl and not a member of class D. It is of the kind the proposal stipulates for
> control C-PROG (P:687), and is an explicit instance, for Q5′ alone, of the constraint at
> S4:399–402. It does not meet Q3′ or Q6′ (four labels; NL-C). It does not meet Q2 at `ε = 0` for
> `K ≥ 3`: the labels `(0,1)` and `(1,0)` show one register and leave the other known, which no
> qubit instrument does (`CHECK-RULEFREE.md` §4.4, unchecked). It meets Q5′ and nothing else is
> claimed.

**K5 (CF:344–350).** Replace "Three things, none available to an additive rule:" by "Three things:"
and the last sentence of the item by:

> The first two change the dependence between successive complete records with the label, which
> Lemma 5 demands and Lemma 1 forbids for an additive rule. The third is available to some
> additive maps (for example `G = 0` on `O`), and by the Remark of §6.3 not to R-lin under the
> uniform law where a site of `O` has an unshielded lattice path of length `τ`.

**K6 (CF:392, and CF:395–402).** Replace the table row "Keep complete records; let a round's record
law depend on earlier records …" by two rows:

> | Keep complete records; let a round's record law depend on earlier records in any declared way; classes Lüders | all | no: it is the test "classes are Lüders given the complete earlier records", so the split becomes the readout (contrary to P:275–277) and the additive world of §6.6 passes | no: changes AF:88–91, :107 and Q2's comparator (P:433–437). An owner decision |
> | Keep complete records; one label-independent split of each record into a retained part with a declared law given earlier records and an outcome part carrying AF:88–91 verbatim | all | for additive rules, the same: Theorem 1 holds with the same constant (`CHECK-RULEFREE.md` Proposition M, unchecked); Lemma S holds for the outcome part only | no: the same clauses change. An owner decision |

and replace CF:398–402 ("What the schema does not allow … none is on record.") by:

> What the schema does not allow is to declare part of the *current* round's record to be retained
> history, so that its law may depend on earlier records. That is a change to AF B1.1 and to Q2's
> comparator, not a reading of either. Admitting memory and admitting post-hoc selection are
> separate: the change readmits the decoder of §6.6 only if the class split may read the retained
> coordinates or the outcome coordinates may depend on the label. A form that excludes both is
> stated in `CHECK-RULEFREE.md` §6.3; under it Theorem 1 is unchanged. It is unchecked.

**K7 (CF:434–442, outcomes (iii) and (iv)).** Replace by:

> - **(iii) A mismatch between the record encoding and the quantum target.** Present for the
>   shared-record constraint: AF's target draws each round's complete record afresh given its
>   class, so a slice listed in two records must be degenerate (Lemma S). It is a constraint on
>   every pair-form rule, not a failure of every rule. It is not the source of Theorem 1's failure:
>   that proof uses the product form of the target only on the coordinates that carry the class,
>   and holds with the duplicated slice removed.
> - **(iv) Survives under a valid alternative representation.** Theorem 1 survives every
>   alternative in which a label-independent set of record coordinates carries the classes with
>   AF's form, retained history included (`CHECK-RULEFREE.md` Proposition M, unchecked). It is not
>   available under a class-level comparison, which is a weaker test and gives up the guard of D4.
>   Whether an R-lin interface passes a class-level test is not derived.

**K8 (CF:431–433, outcome (ii)).** Replace "At other `τ` in initial-condition mode: open, with a
sketch against." by:

> At other `τ` in initial-condition mode: a construction at `τ = 14` is written out in
> `CHECK-RULEFREE.md` §4.6; it has one hand derivation and no check, and until it is checked this
> is open. Within the schema, whose rules are R-lin and R-nl, (ii) is the open question whether
> R-nl fails Q5′.

No change is requested to Lemma S's proof, to Corollary S1's proof or constant, or to Proposition
E's verification steps 1–8.

***

## 10. What may and may not be concluded

**The linear rule.** It may be concluded, as a hand-derived and hand-reviewed [W] result, that
every R-lin interface of the TUNE-1 schema fails Q5′ as AF defines it, under hypotheses 1–7 with
H-μ (and H-∞ or H-write where used), so classes A, B and C fail T1 and L5.4–L5.6 are answered in
the negative within that scope. The failure is a property of additive dynamics under a comparison
that admits no decoder; it is not produced by the duplicated boundary slice and it survives a
target with a declared place for retained history. It may not be concluded that the linear rule
fails under a class-level or thresholded readout, under a target whose reads are not of the form of
AF:88–91, or outside this schema; that the rows of S3 §5 are restated (an owner decision); or
anything on the correctness axis (§A.23). **Non-linear rules.** Nothing may be concluded about R-nl
(class D) or about the ring rule of SM §3.1, for or against, beyond three necessary conditions that
use pair form only: Lemma 5, Lemma S, and no `τ = 1` in initial-condition mode. Proposition E shows
that the record convention and the target do not by themselves exclude a non-additive pair-form
rule from Q5′; its rule is designed, is in neither 𝓡 nor 𝓛, is not a member of class D, and fails
Q2, Q3′ and Q6′, so it is not evidence that any OI rule yields a qubit. **The observer interface.**
Complete-history records in pair form list one slice in two consecutive records, and the target
then requires the read region to return to one configuration at every round boundary, with
everything that persists between rounds held in unread cells; at `τ = 1` in initial-condition mode
this fails every rule by definition, which is a matter for the owner in the same way as P:200–205.
The schema as written keeps the whole accessible history and distinguishes the current outcome at
the level of rounds. A target that also tolerates history retained inside the read region is an
interface change (B1.1 and Q2), is the owner's to make, discards no accessible information, and
need not weaken the selection requirement; in the form that keeps that requirement it changes
nothing for the linear rule.

***

## 11. Read, not checked, disclosure

**Read.** `l54/CONFIRM-r2.md` and `l54/L54-r2.md`, whole. `TUNE-1-STEP2-AMENDMENT-1-final.md`, whole,
and its two addenda. `TUNE-1-STEP2-PROPOSAL.md` 55–314, 395–504, 687–712. `TUNE-1-STEP2-SESSION1.md`
90–100, 146–158, 240–292, 516–531. `TUNE-1-STEP2-SESSION4.md` 86–106, 156–190, 380–410, 568–615.
`TUNE-1-STEP3A-r3.md` 205–221, 462–530, 712–780. `mechanism-1-20261107/DESIGN.md` 396–430.
`oa-1-20261112/OA-1-REPORT-r5.md` 200–212. `papers/Main.md` 575–590 and the ledger items (vii)–(xiii)
at 724. `papers/SM.md` 106–112, 294–298.

**Not checked.** `CONFIRM-r2.md` §§1–5 and §7 (C1–C5), except Theorem 1, its lemmas and Corollary
1a. Proposition 2, Lemma 4, R3. OA-2 and OA-3 at source (quoted through 3A only). Q1 for
Proposition E. Any positive floor in `ε` for Proposition E's failure of Q2.

**Commands.** `ls`, `wc`, `sed -n`, `grep`, `cut`, `fold`, `awk`, `git rev-parse` (read-only), and
the file reads. One `python3` call made a single text replacement in this file (a table row of §4.5); it computed nothing. No computation was run on any OI rule or model. All arithmetic and all time-stepping were done by hand.
