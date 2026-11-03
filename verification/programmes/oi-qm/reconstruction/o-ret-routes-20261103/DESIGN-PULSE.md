# O-RET pulse design: local storage versus transport through a multi-cell register

**Status.** WIP / UNVERIFIED, paper-only design under PO-1102 workstream B (owner authorization 2026-11-03, #1032).
Drafted against branch `research/o-ret-routes-20261103` at `473b5e34`, reading `ROUTES.md`, `DEFINITIONS.md`,
`SOURCES.md` and `ANNOTATION.md` in `verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/`. Not reviewed.

- *What it is.* A test design for the question: does a proposed retention mechanism store information locally,
  or does the information only travel through a multi-cell register `A`? It contains candidate definitions, hand-checked
  tiny controls, a decision table, an assumption audit, counterexamples, limits, and a computation specification.
- *What it is not.* No computation, enumeration, simulation or Lean was run, and no computational verdict is
  claimed. No criterion is adopted, no premise is added, no candidate is selected, and nothing is promoted to
  SOURCE-CANDIDATE. Every criterion introduced here is an unreviewed proposal.
- *Tolerance.* The owner's working threshold `ε* = 0.05` on the worst-case decoding error `ε_max` (D-MET) is used. In
  every control `f(P)` has `m = 2` values, so the blind bound `1 − 1/m = 1/2` lies above `ε*`, and `ε*` is not vacuous.
- *Support labels.* **[D]** paper derivation in this document (unreviewed). **[C]** text at checkpoint `473b5e34`
  (ROUTES.md or DEFINITIONS.md). **[U]** unreviewed proposal named at that checkpoint: S-1, J-1, countercontrol (h) and
  Remark C. **[L]** literature cited from memory, not re-read.

***

## 1. Four obligations, kept separate

| Obligation | What it would require | Discharged by anything here? |
|---|---|---|
| **O1 Physical source** | A derivation, from native dynamics and a law with an independent origin, of every preparation resource the mechanism uses: support restriction, readiness and quiet inputs. A declared prior, or a stipulated no-overwrite condition, is not a derived source. | No. Every control below imposes its law. |
| **O2 Retention** | D-RET (R-a)–(R-d) within `ε*` over `W_T` [C], together with this document's added requirement that the record is held in `A` rather than passing through it (§2.3). | Proposed criteria and controls only. |
| **O3 Accessible readback** | A physically accounted read of `A`, and of any clock `K`, by an embedded subsystem. H-cur (declared) is the baseline, and its physical sourcing is outstanding (D-ACC [C]). Reading across ticks names H-ret (D-SEN [C]). | No. |
| **O4 Observer formation** | An embedded subsystem whose partition, identity and location are derived rather than stipulated (O-OBS). | No. |

Every verdict in §3 and §4 concerns O2 alone. A positive O2 verdict says nothing about O1, O3 or O4.

***

## 2. Setting, notation, candidate definitions

### 2.1 Setting (reused, not redefined)

The setting is that of ROUTES §0.1 and the DEFINITIONS preamble [C]: a finite `S` that is a product of cells, a
time-homogeneous bijection `φ`, the law `μ = μ_Σ ⊗ ν` at `t₀`, a declared preparation set `P`, a property `f`, a fixed
decoder `g`, the window `W_T = {t₀+1, …, t₀+1+T}` whose hold ticks are `t → t+1` for `t = t₀+1, …, t₀+T`, and `ε_max`
and `TV_t` from D-MET. Also used: Lemmas S, S′, Q, L and C (ROUTES §0.3 [C]); HC-P and HC-F/HC-F0 [C]; the models
`M_F` and `M_T` [C]; and S-1, J-1, (h) and Remark C [U].

### 2.2 Structural dependence (native: computed from `φ` on all of `S`)

- `Par(i)` is the set of cells `j` such that some pair of states differing only at `j` gives different values of cell
  `i` of `φ(s)`. On the full product `S` this is the unique minimal set through which `φ(·)_i` factors.
- `R ⊆ A` is the **read set**: the cells on which `g∘ρ_A` depends. Let `Q := Par(R) ∖ R`, and let
  `f_R : config(R) × config(Q) → config(R)` be the `R`-part of `φ`.
- `supp Q_t` is the support of the vector `Q_t` under `μ_t`. This is the only place a law enters the exact criteria.
- **Observation D0 (support-restricted dependence is ill-posed) [D].** DEFINITIONS computes `B_t` "as functions of the
  state at `t` on the support". When the support imposes a relation among cells, that dependence is not unique.
  - In HC-P at `t₀+1` [C], the support has `u₀ = 0` and `u₁ = u₂ = c`.
  - On that support, `u₂(t₀+2) = u₁ ⊕ u₀` equals `u₁`, and it also equals `u₂`.
  - Flipping any single cell leaves the support, so a single-flip test finds dependence on **no** cell, although the
    value is not constant.
  - Every criterion in §2.3 therefore uses structural `Par` and `f_R`, and lets the law enter only through `supp Q_t`
    and the supported configurations of `R`.

### 2.3 Candidate criteria

**(i) Cell-history criteria.** Let `C_t` be the set of cells whose value at `t` is not independent of `κ`. For a linear
rule, the geometric part of `C_t` is fixed by `φ` and `Σ` (Lemma L [C]). For a nonlinear rule it depends on the law,
and a cell-by-cell `C_t` has the joint-information blind spot that J-1 addresses [U].
- **SCH (static holder).** At each hold tick, `Par(i) ∩ C_t ⊆ {i}` for every `i ∈ R`: a read cell takes carrier
  information only from itself.
- **ICH (internal history).** At each hold tick, `Par(R) ∩ C_t ⊆ R`. This is S-1 applied to the read set [U].
- **CHC (closed children).** At each hold tick, every `i ∈ R ∩ C_t` has all its children under supported `q` inside
  `R`.

**(ii) Cut test.** For a hold tick `t` and a cell set `X`, the *X-cut* replaces `s_t|_X` by an independent draw from
its own marginal law at `t`, then applies `φ`. Report `ε_max(t+1)` under the cut.
- An *outside cut* takes `X = cells ∖ R`. It tests inflow.
- An *inside cut* takes `X ⊆ R`. It locates the cell that holds the record.
- **Not native.** The cut is a counterfactual on the dynamics. Physically it needs an extra noise reservoir and a
  tick-scheduled swap. It also depends on the law, through the marginals.
- A "freeze" variant, `X_{t+1} := X_t`, is in general not a bijection, so it is further from native.
- Replacing the cut cells by uniform noise instead of their marginal is a different test. It destroys the quiet input
  of `M_F`, which then reads as a false negative.

**(iii) Conserved-locus criteria.**
- **(iii-a) ABL, autonomous bijective locus.** For every `q ∈ supp Q_t`, `f_R(·, q) = U_t`, a bijection of `config(R)`
  that does not depend on `q`.
- **(iii-b) DIL∃, decoder-invariant locus.** Let `𝒬_W` be the union of `supp Q_t` over the hold ticks of `W_T`. Let `~`
  be the equivalence relation on `config(R)` generated by `ℓ ~ f_R(ℓ, q)` for **all** `ℓ ∈ config(R)` and all
  `q ∈ 𝒬_W`. Let `𝓛_W` be the configurations of `R` that are supported at some tick of `W_T`.
  - **DIL∃ holds** iff no `~`-class contains two members of `𝓛_W` with different decoded values `g(ℓ)`.
  - Equivalently, some extension `g̃` of `g|_{𝓛_W}` satisfies `g̃∘f_R(·, q) = g̃` for all `q ∈ 𝒬_W`.
  - It is a finite connectivity check on `config(R)`.
  - **DIL∃-η, the approximate form.** Choose `G ⊆ 𝒬_W`, build `~` from `G` only, require the same consistency, and set
    `η_t(σ) := μ(Q_t ∉ G | σ)`.

**Lemma H (sufficiency, one direction) [D].** If DIL∃ holds on `W_T`, then `g(R_{t+1}) = g(R_t)` for every hold tick
`t` and every supported state. So exact decoding at `t₀+1` gives `ε_max = 0` on `W_T`. Under DIL∃-η,
`μ(g(R_{t+1}) ≠ f(σ) | σ) ≤ μ(g(R_t) ≠ f(σ) | σ) + η_t(σ)`.
*Proof.* `R_t, R_{t+1} ∈ 𝓛_W`, and `R_{t+1} = f_R(R_t, Q_t)` with `Q_t ∈ 𝒬_W` (or `∈ G`), so the two lie in one class,
on which `g` is constant. ∎

The converse fails: HC-TS below holds exactly on `W₁` and fails DIL∃. That gap is the transport-detecting content of
DIL∃. Two properties follow directly from the definition [D]:
- DIL∃ uses **supports only**, not probabilities. It is therefore immune to information carried jointly by
  individually independent inputs: invariance must hold for each `q` separately.
- DIL∃ fails on re-supply. If `Q` carries the carrier and the carrier varies over its support, `f_R` maps a supported
  configuration to configurations with different decoded values.

**Lemma D (exact DIL∃ needs a support that is not invariant) [D; CONFIRMING Lemma S′].** Let
`Wr := {q : g∘f_R(·, q) ≠ g}`. If `φ(supp μ) = supp μ` and `g(R)` changes over the write tick with positive
probability, then exact DIL∃ fails at the first hold tick.
*Proof.* A supported state with `g(f_R(ℓ, q)) ≠ g(ℓ)` at the write tick has `ℓ = R_{t₀}`, and `ℓ` is supported
at `t₀+1` because the support is invariant. Also `f_R(ℓ, q) = R_{t₀+1}`, and `q ∈ supp Q_{t₀} = supp Q_{t₀+1} ⊆ 𝒬_W`.
So `ℓ ~ f_R(ℓ, q)`: both lie in `𝓛_W` and decode differently. ∎

**Lemma E (exposure under an invariant law, one direction) [D; ELABORATING Lemma S].**
`{g(R_{t+1}) ≠ g(R_t)} ⊆ {Q_t ∈ Wr}`. If `μ` is φ-invariant, then
`μ(Q_{t₀+1} ∈ Wr) = μ(Q_{t₀} ∈ Wr) ≥ μ(g(R) changes at the write tick)`.
- The hold tick is exposed to write-enabling inputs at least as often as the write occurs.
- The lemma bounds exposure, not error.

**Lemma P (recurrence) [D; known in substance, L: finite recurrence].** If `φⁿ = id` on `supp μ` and (R-b) holds,
then at `t₀+n` the decoded value has the same law for every `σ`. So `ε_max(t₀+n) ≥ 1 − 1/m`, and exact retention over
`W_T` needs `T ≤ n − 2`.
*Proof.* `s_{t₀+n} = s_{t₀}`, and by (R-b) the law of `g(ρ_A(s_{t₀}))` given `σ` does not depend on `σ`. ∎
For a large period the bound is vacuous.

**Observation K (copy-form registers) [D; ELABORATING Lemma L and P2-G].** Take `R ⊆` the current slice of a rule with
`y′_R = D_R(y) − x_R` over `ℤ/q`, so that `x_R` lies in `Q`. This includes K1 (SM:296, as used in ROUTES §0.4). Then:
- **(K-0)** If `D_R` does not depend on `y_R`, as for a single cell under center-freeness, `f_R(·, q)` is constant in
  `ℓ`. DIL∃ fails for every nonconstant decoder at `T ≥ 1`.
- **(K-1)** Suppose `D_R(·, y_out)` is a bijection, and some `y_out` is jointly supported with every value of
  `x_R(t)`.
  - Then each `~`-class is closed under translation by `x − x′` for `x, x′ ∈ supp x_R(t)`.
  - So full support of `x_R(t₀+1) = y_R(t₀)` gives a single class: DIL∃ fails at the first hold tick unless the
    register's own content at `t₀` is restricted. That restriction is readiness, an H-sel-type resource.
- **(K-2)** At `t = t₀+2` we have `x_R = y_R(t₀+1)`. If one `y_out` is jointly supported with two record
  configurations `ℓ₀`, `ℓ₁` of different decoded value, then `ℓ₀ ~ ℓ₁`, by translation by `ℓ₁ − ℓ₀`. So DIL∃ fails for
  `T ≥ 2`.
- On K1 at K-18(b), `R` = sites 1–4 has `D_R` bijective, because the `P₄` adjacency matrix has determinant 1 mod 2.
  Whether the K-2 joint-support hypothesis holds there depends on the law. That is open and goes to §8.

**Proposed definitions [D, unreviewed].**
- **Storage in `R` over `W_T` (ST).** (R-a)–(R-c) hold within `ε*`, together with either exact DIL∃, or DIL∃-η with
  the Lemma H bound `≤ ε*` at every `t ∈ W_T`.
  - *Static* storage if SCH also holds.
  - *Circulating* storage otherwise: the record moves inside a closed `R`.
- **Transport through `R` (TR).** DIL∃ fails through a chain whose inputs `q` are carrier-independent: J-1 [U] holds
  at those ticks, and `R`'s own update carries supported content to a configuration with a different decoded value.
- **Re-supply (RS).** DIL∃ fails, or J-1 fails, through a carrier-dependent `q`.

### 2.4 Which parts are native (no imposed starting law)

| Criterion | From `φ` alone | Needs the law | Needs a modified dynamics |
|---|---|---|---|
| (i) SCH, ICH, CHC | `Par`, children | `C_t` (law-free in its geometric part for linear rules, by Lemma L); supported `q` | no |
| (ii) cuts | which cells are cut | marginals | **yes** |
| (iii) ABL, DIL∃ | `f_R` on all of `config(R)`; the relation `~` | `supp Q_t` and `𝓛_W` (exact); `η` (approximate) | no |

- **Exact verdicts.** Lemma D and Lemma Q [C] mean that no verdict of exact storage of a newly written record is
  available under a law with φ-invariant support. Exact storage therefore needs an imposed or sourced law.
- **Under `π₀`.** With no restriction beyond H-μ, only DIL∃-η is available, and its exposure is at least the
  probability that the write changes the record (Lemma E).
- **Who applies the criteria.** Every criterion is applied by the analyst. None is an observation an embedded
  subsystem makes: a readback across ticks names H-ret (D-SEN), and a cut is an intervention.

***

## 3. Controls (hand derivations [D] unless marked)

Arithmetic is over `𝔽₂`. The carrier property is `f = c` (or `v₀`), with `P` its two values, and `TV` is that of D-MET.
Shifts are `u_j ← u_{j−1}`.

### 3.1 Transport controls

**HC-TS (pure-shift pair; the transport member of the decisive pair).**
- *Dynamics.* Ring `ℤ/L`, `L ≥ 4`, pure shift. `φᴸ = id`.
- *Carrier and law.* `Σ = {u₀}`, `c = u₀(t₀)`, and `ν = π₀(· | u₁ = 0, u_{L−1} = 0)`, so `D = 2 log 2`.
- *Register and decoder.* `A = R = {u₁, u₂}`, `g = u₁ ⊕ u₂`.
- *Trajectory.*
  - `t₀+1`: `A = (u₀, u₁)(t₀) = (c, 0)`.
  - `t₀+2`: `A = (u_{L−1}(t₀), c) = (0, c)`.
  - `t₀+3`: `A = (u_{L−2}(t₀), 0) = (n, 0)`, with `n` uniform, since `L−2 ≥ 2` and `L−2 ≠ L−1`.
- *Metrics.* `ε_max = 0, 0, 1/2` and `TV = 1, 1, 0` at `t₀+1, t₀+2, t₀+3`. (R-a)–(R-c) hold exactly over `W₁` and
  fail over `W₂`.
- *(R-d), D-TRN.* `Q = Par(R) ∖ R = {u₀}`, and `u₀(t₀+1) = u_{L−1}(t₀) = 0`, so S-1, J-1 and D-TRN's "left" pass [U].
- *DIL∃ fails.*
  - `f_R(ℓ; 0) = (0, ℓ₁)`, which sends `11 → 01 → 00` and `10 → 01`.
  - So `~` has a single class, containing supported `00` (decoded 0) and `10`, `01` (decoded 1).
- *Cell-history.*
  - SCH fails: `Par(u₂) ∩ C_{t₀+1} = {u₁}`.
  - CHC passes at the only hold tick of `W₁`: `u₁ ∈ C` has child `u₂ ∈ R`, and `u₂ ∉ C_{t₀+1}`.
- *Cuts.*
  - Outside cut: `ε = 0`.
  - Inside cut of `u₁`: `ε = 1/2`.
  - Inside cut of `u₂` (marginal `δ₀`): `ε = 0`.

**HC-TM (HC-P generalized to an `m`-cell register).**
- *Dynamics.* HC-P's rule [C]: `u₁ ← u₁ ⊕ u₀`, then shift, on `ℤ/L` with `L ≥ m+3`.
- *Register, decoder and law.* `A = R = {u₁, …, u_m}` with `m ≥ 2`, `g = OR(A)`, and the ready law `ν = δ₀` on all
  non-carrier cells, so `D = (L−1) log 2`.
- *Imprint.* By linearity (Lemma L [C]) the imprint is native.
  - From `M₀ = e₀`, applying `G` then the shift gives `M₁ = e₁ + e₂`.
  - Since `M_k[0] = 0` for `1 ≤ k ≤ L−2`, `M_k = e_k + e_{k+1}` for those `k`.
  - Continuing: `M_{L−1} = e_{L−1} + e₀`, `M_L = e₀ + e₁ + e₂`, and `M_{L+1} = e₁ + e₃`.
  - With `ν = δ₀` the background part is `β ≡ 0`.
- *Metrics.*
  - `OR(A) = c` for `k = 1, …, m`. So `ε_max = 0` on `W_{m−1}`, with `TV = 1`.
  - `ε_max = 1` at `k = m+1, …, L−1`.
  - At `k = L` and `L+1` the decoder reads `c` again (re-entry through the wrap).
- *(R-d).* `Q = {u₀} = 0` at the hold ticks, so S-1, J-1 and D-TRN "left" pass [U]. ICH and the outside cut pass.
- *CHC fails* at the last hold tick: `u_m ∈ C` has child `u_{m+1} ∉ R`. For `m = 2` this happens already at `t₀+1`,
  through the leading copy.
- *DIL∃ fails.* `f_R(ℓ; 0) = (0, ℓ₁, …, ℓ_{m−1})`, so `m` iterations send every `ℓ` to `0`, and `e₁ + e₂` (decoded 1)
  `~ 0`.
  - The chain passes through `e_m`, which is supported only at `t₀+m`.
  - For `T < m−1` the verdict therefore rests on `R`'s structural behaviour beyond the window (§7 L1).
- *DEFINITIONS' limitation case.* The case `m = 2`, `g = u₂`, with HC-P's own law (DEFINITIONS limitation [C/U]) has
  `ε_max = 0, 0, 1/2` at `t₀+1, +2, +3`.
  - `f_R` is the same, so DIL∃ fails.
  - This is the case S-1 and J-1 admit. DIL∃ rejects it, and so does CHC.

### 3.2 Local-storage controls

**S1 = `M_F` under `μ_F` (HC-F [C]).**
- `R = {r}`, `Q = {p₀, v₀}`, and `f_R(r; 0, v) = r`. The supported `q` have `p₀ = 0`, so DIL∃ holds exactly.
- SCH holds: `C_{t₀+1} ∩ Par(r) = {r}`, because the arriving cell and the departed cell's `v` (the old `r`) are
  independent of `κ`.
- Classification: static storage over `W₁`, conditional on E-reg, H-sel (the quiet bit) and H-cur.

**HC-SW (swapped pair; the storage member of the decisive pair).**
- *Dynamics.* `M_F`'s channel with `L ≥ 2` [C] and a register `(r₁, r₂)`. Each tick: Fredkin (if `p₀ = 1`, swap `v₀`
  and `r₁`), then the register swap `r₁ ↔ r₂`, then the channel shift. It is a bijection and time-homogeneous.
- *Law.* `μ = π₀(· | p_{L−1} = 0, r₂ = 0)`, so `D = 2 log 2`, as in HC-TS.
- *Preparations, property and decoder.* `P = {(1,0), (1,1)}`, `f = v₀ =: c`, `g = r₁ ⊕ r₂`. (R-b) holds:
  `g(A_{t₀}) = r₁`, which is uniform.
- *Trajectory.*
  - `t₀+1`: the write gives `r₁ = c`, and the swap gives `A = (0, c)`.
  - Hold: the arriving cell has `p = 0`. After the swap, `A = (c, 0)` at `t₀+2`.
- *Metrics.* `ε_max = 0, 0` and `TV = 1, 1`. For `W₂`, add `p_{L−2} = 0` with `L ≥ 3`; then `A = (0, c)` and `ε = 0`.
- *DIL∃ holds.* `f_R(ℓ; 0, v) = swap(ℓ)`. The classes are `{00}`, `{01, 10}` and `{11}`, and the supported decoded
  values are consistent.
- *Other criteria.*
  - SCH fails, since the record moves from `r₂` to `r₁`. So this is circulating storage.
  - CHC, ICH, S-1, J-1 and the outside cut pass. The inside cut of `r₂` gives `ε = 1/2`.

**HC-SK (`M_F⁽ᵏ⁾` under `π₀`: approximate storage at `ε*`).**
- *Dynamics.* `M_F` with `k` presence bits per channel cell. The Fredkin acts iff all `k` bits are 1. This is the
  trigger variant of the ROUTES Comparison [C].
- *Law, preparations and decoder.* `π₀`, `D = 0`. `P` is the two fired preparations `(1…1, c)`, `g = r`, and
  `L ≥ T+1`.
- *First hold tick.* The arriving cell fires with probability `2⁻ᵏ` and swaps in a uniform `v`. So
  `ε_max(t₀+2) = 2⁻ᵏ⁻¹` and `TV = 1 − 2⁻ᵏ`. At `k = 1` this gives `1/4` and `1/2`, matching HC-F0 [C].
- *Window `T`.* `ε_max(t₀+1+T) = (1 − (1 − 2⁻ᵏ)ᵀ)/2`.
- *Against `ε* = 0.05`.*
  - `T = 1`: `k = 3` gives `1/16 = 0.0625` (fails), and `k = 4` gives `1/32 ≈ 0.031` (passes).
  - `T = 2`: `k = 4` gives `31/512 ≈ 0.061` (fails), and `k = 5` gives `63/2048 ≈ 0.031` (passes).
  - `T = 3`: `k = 5` gives `≈ 0.045` (passes).
- *Write probability and exposure.* `w = 2⁻ᵏ`, and `η = 2⁻ᵏ` per hold tick, which equals `w` (Lemma E). In this family,
  `ε_max(t₀+2) ≤ ε*` therefore forces `w ≤ 2ε* = 0.1`.
- *Classification.* DIL∃ fails exactly. DIL∃-η holds with `G = {not all ones}` and `η = 2⁻ᵏ`, so this is approximate
  static storage. It is candidate-specific evidence only: designed E-reg, `P` conditioned on a fired trigger, `w*`
  unset (D-SML).

### 3.3 Delayed-readback controls

**HC-R1 (continuing transport plus recurrence: HC-TS read late).**
- `φᴸ = id` gives `A(t₀+1+L) = (c, 0)` and `ε_max = 0`. Every tick from `t₀+3` to `t₀+L` has `ε_max = 1/2`.
- At `t₀+L` the register is blind, as Lemma P requires.
- A single readback at `t₀+1+L` reports exact retention, while a gap-free readback over the same span rejects it.

**HC-R2 (re-supply: a static carrier feeding a conveyor).**
- *Dynamics.* Carrier `c` with `c′ = c`, and conveyor `w ∈ 𝔽₂^{ℤ/L}`. Each tick: `w₀ ← w₀ ⊕ c`, then shift. It is a
  bijection.
- *Law, register and decoder.* `c` uniform, `ν = δ₀`, `A = R = {w₁}`, `g = w₁`.
- *Trajectory.* `w = c(e₁ + … + e_k)` at `t₀+k` for `k ≤ L−1`, and every cell equals `c` at `t₀+L`. So `w₁ = c` for
  `t₀+1, …, t₀+L`, with `ε_max = 0` there.
- *Gap-free readback.* It passes.
- *Criteria that reject it.*
  - J-1 fails: `Q = {w₀, c}` contains the carrier.
  - DIL∃ fails: `f_R = w₀ ⊕ c` takes both values over `supp Q`.
  - The outside cut of `c` gives `ε = 1/2`.
  - D-TRN's "left" fails.
- Classification: re-supply. No readback schedule detects it.

**HC-R3 (`M_F` at `L = 2`: storage, release, then return of the carrier).**
- *Setup.* Cells `C = (1, c)` and `D = (0, v_D)`, with `r = ρ` uniform.
- *Trajectory.* Following ROUTES' note [C], the record `r` reads `c, c, ρ, ρ, c, c` at `t₀+1, …, t₀+6`, with period 4.
  Then `ε_max = 0, 0, 1/2, 1/2, 0, 0`.
- *Per-tick criteria.*
  - At the hold tick `t₀+2 → t₀+3`, the arriving `C = (1, ρ)` passes J-1, but DIL∃ fails: an overwrite.
  - At `t₀+4 → t₀+5`, the arriving `C = (1, c)` fails J-1: re-supply by the returning carrier.
- Lemma P gives `n = 4`, so `T ≤ 2`, which is consistent with failure at `t₀+3`.
- A readback at `{t₀+1, t₀+5, t₀+6}` alone would report retention.

### 3.4 Classification matrix

| Control | (R-a)–(R-c) on `W₁` | S-1 / J-1 [U] | ICH | SCH | CHC | outside cut | DIL∃ | gap-free `W_T` | single late readback |
|---|---|---|---|---|---|---|---|---|---|
| HC-TS | pass, exact | pass | pass | fail | pass | pass | **fail** | fails at `W₂` | passes at `t₀+1+L` |
| HC-TM | pass on `W_{m−1}` | pass | pass | fail | fail | pass | **fail** | fails at `W_m` | passes at `t₀+L` |
| S1 | pass, exact | pass | pass | pass | pass | pass | pass | quiet bits needed | — |
| HC-SW | pass, exact | pass | pass | fail | pass | pass | pass | quiet bits needed | — |
| HC-SK, `k = 4` | `ε = 1/32` | pass | pass | pass | pass | pass | DIL∃-η, `η = 1/16` | `T = 1` only | — |
| HC-R2 | pass | **fail** | fail | fail | n/a | **fail** | **fail** | passes | passes |
| HC-R3 | pass | fails at `t₀+4` | — | fails at `t₀+4` | — | — | fails at `t₀+2` | fails at `W₂` | passes at `t₀+5` |

***

## 4. Decision table

| Row | Observation or criterion | Exact / approximate | Required assumptions | Does NOT establish |
|---|---|---|---|---|
| **Storage, static** | ST together with SCH | exact: DIL∃ on the declared supports. Approximate: DIL∃-η with the bound `≤ ε* = 0.05` on all of `W_T` | H-cur (declared) read of `R`; preparation (`supp Q_t` excluding `Wr`, by Lemma Q); E-reg if designed; DIL∃ adopted | O1 (the law is imposed), O3, O4; persistence beyond `W_T` (Lemma P); the "smallest" ranking (D-SML); independence from the choice of cells |
| **Storage, circulating** | ST without SCH | as above | as above; with a clock decoder, Remark C [U] and an accounted `K` | as above; locality below the scale of `R` |
| **Transport established** | TR: DIL∃ fails through carrier-independent inputs; its prediction is R-c failure at the first tick after the transit time `τ(R)`, which a gap-free window `T ≥ τ(R)` confirms | exact for linear rules, where the imprint is native (Lemma L); otherwise on declared supports | H-cur (`R` declared); supports | that no other `R′` or decoder stores the record; any rule-wide no-go |
| **Not storage: re-supply** | J-1 fails, or DIL∃ fails via a carrier-dependent `q`; the outside cut of `Q` destroys the record | exact | J-1 [U]; supports | that the carrier is itself a record (a display, requirement 2) |
| **Not storage: recurrence** | the readback succeeds only at isolated ticks; Lemma P blind tick; per-tick DIL∃ or J-1 failure | exact | knowledge of the period on the support | anything about retention |
| **Inconclusive I-1** | only trajectory-level data over `W_T` with `T < τ(R)` (the HC-TS / HC-SW pair, §7 L1) | — | — | either verdict |
| **Inconclusive I-2** | only inflow tests (S-1, J-1, ICH, the outside cut), or CHC over the window's own ticks; CHC separates HC-TM but not HC-TS | — | — | separation of HC-TS from S1 / HC-SW |
| **Inconclusive I-3** | only a non-contiguous delayed readback | — | — | anything (HC-R1, HC-R3) |
| **Inconclusive I-4** | closed circulation, where DIL∃ passes and SCH fails, and the owner has not ruled on circulation | — | — | "local" storage |
| **Inconclusive I-5** | a verdict that changes under a change of cell coordinates or of `R` (§6 CX-3) | — | cell decomposition fixed only as a datum | a φ-intrinsic distinction |
| **Inconclusive I-6** | approximate: `ε_max ≤ ε*` but the Lemma H bound `> ε*`, or `w < w*`, or `T < T*` (both unset) | — | — | D-SML comparison |
| **Inconclusive I-7** | a nonlinear rule whose `C_t` is law-dependent; time-varying `q`-supports that make the union `𝒬_W` over-connect (§6 CX-4) | — | — | transport (a possible false positive) |
| **Inconclusive I-8** | the decoder needs a clock and Remark C is unreviewed | — | Remark C [U] | fixed-decoder status |

***

## 5. Assumption audit

| Assumption | Where it enters | Can native dynamics supply it? | What fails without it |
|---|---|---|---|
| **H-cur (declared)** | The choice of `A`, `R` and `ρ_A`; every criterion takes `R` as given; DIL∃ quantifies over `config(R)` | No. The readable σ-algebra is a datum (O-ACC, via SOURCES [C]). | No register and no criterion. The cell decomposition itself is part of the datum (§6 CX-3). |
| **E-reg** | S1, HC-SW, HC-SK and HC-R3 are designed registers with a Fredkin gate; HC-TS, HC-TM and HC-R2 are toy rules outside the corpus | No. Route III is CONDITIONAL on an unjustified E-reg [C]. | The storage controls do not exist as native objects. They calibrate the criteria and are not candidates. For native copy-form rules, Observation K shows what a register would need. |
| **Preparation and support restriction (Lemma Q)** | `supp Q_t ∩ Wr = ∅` for exact DIL∃; ready values for decoding (`r₂ = 0` in HC-SW, `u₁ = u_{L−1} = 0` in HC-TS, `δ₀` in HC-TM) | Not for exact verdicts: Lemmas S′ and D rule out laws with φ-invariant support. Under `π₀` (H-μ) only DIL∃-η, with exposure `≥` the write probability (Lemma E). | Exact storage is impossible. Approximate storage needs `w ≲ 2ε*` in the HC-SK family. |
| **Tick-dependent readout (Remark C [U])** | Circulating storage without an invariant decoder (HC-SW with `r₂` uniform) | Only through an accounted clock `K` whose phase is prepared, a support restriction that enters D-SML. | Conditionally on Remark C, apply DIL∃ to `R ∪ K` with `g′(ℓ, k) = ℓ_k`. On the swap with `k′ = 3 − k`, `g′∘f = g′` [D]. Without Remark C, the clocked case is I-8. |
| **Overwrite exclusion** | The same condition as preparation, read as "no `q ∈ Wr` arrives at the hold ticks" (`M_F`'s quiet bit, HC-SW's `p_{L−1} = 0`) | No. It is stipulated in every control, and a stipulated quiet input is not a source (O1). | HC-SK and HC-F0: the error grows by `≤ η_t` per hold tick (Lemma H). |

***

## 6. Counterexamples and falsification criteria

The branches favourable to OI are pressure-tested first (§A.31).

- **CX-1 (favourable branch: "DIL∃ is native, so native storage is in reach").**
  - DIL∃'s structural part is native. Its verdict is not: it needs supports, and the exact verdict needs a support
    that is not invariant (Lemma D).
  - On copy-form registers DIL∃ demands readiness (K-1) and, under the K-2 hypothesis, fails at `T ≥ 2`.
  - Nothing here moves route II from CONDITIONAL[H-sel].
- **CX-2 (favourable branch: HC-SK meets `ε*` under `π₀`).**
  - It is a designed E-reg, and `P` is conditioned on a fired trigger.
  - `w = 1/16`, and `T = 1` holds only at `k = 4`.
  - `η = w` by construction (Lemma E).
  - It shows that the metric is satisfiable, not that a mechanism exists.
- **CX-3 (every criterion is relative to the cell coordinates).**
  - In HC-SW, replace the cells `(r₁, r₂)` by `w₁ = r₁ ⊕ r₂` and `w₂ = r₁`. The swap becomes `w₁′ = w₁` and
    `w₂′ = w₁ ⊕ w₂`.
  - The record is then the static cell `w₁`, and SCH passes.
  - In the original cells SCH fails. The verdict of (i) depends on the coordinates, and DIL∃ depends on `R` as a set
    of cells.
  - Native dynamics fixes the cells only through the declared lattice model.
- **CX-4 (DIL∃ over-rejection).**
  - `𝒬_W` takes the union over ticks, and `~` composes maps from different ticks.
  - So a leak that opens only at ticks when `R` sits in other configurations can connect classes that the actual
    dynamics never connects.
  - DIL∃ would then report transport while R-c holds. A tick-ordered variant is a design option, not developed here.
- **CX-5 (ABL over-rejects error correction; DIL∃ does not).**
  - Take `R = {r₁, r₂}` with the code `{00, 11}`, ancilla `z` (ready, supplied fresh), and the tick
    `z ← z ⊕ r₁ ⊕ r₂; r₂ ← r₂ ⊕ z`.
  - With `z = 0`: `(r₁, r₂) ↦ (r₁, r₁)`, which is not a bijection, so ABL fails. CHC also fails: `r₂`'s content
    goes to `z`.
  - With `g = r₁`: the classes are `{00, 01}` and `{10, 11}`, so DIL∃ holds.
  - This is why (iii-b) is preferred to (iii-a). Literature, from memory and not re-read: stable memories exporting
    entropy, as in Toom's rule and Gács's construction; erasure costs, as in Landauer 1961 and Bennett 1982.
- **CX-6 (law-level masquerade).**
  - On HC-TS's support the update of `A` coincides with a swap of `A`, since `(c, 0) ↦ (0, c)`.
  - So any criterion computed from supported configurations alone reads transport as circulation (D0, §7 L1).
- **CX-7 (where all criteria misclassify).**
  - A closed delay loop inside `A`, entered through a gate and left later: a "siding".
  - DIL∃ calls the dwell storage, and SCH calls it transport. Under the reading "information travelling through `A`",
    both answers are defensible.
  - By Lemma P, every finite-bijection record is eventually re-exported, so storage here means a dwell at a closed
    locus covering `W_T`. That is a difference of duration and closure, not of kind.
  - Historical delay-line memories (from memory, L) are of this kind.

**Falsification criteria for this design.**
- **F-1.** In some control, DIL∃ reports transport through carrier-independent inputs, yet R-c holds on every
  `W_{T′}` up to the bound of Lemma P. Then DIL∃'s structural extrapolation is wrong there, and DIL∃ is demoted to an
  indicator.
- **F-2.** Exact DIL∃ holds on `W_T` while `ε_max > 0` at some `t ∈ W_T`, given an exact write. This contradicts Lemma
  H, so either the lemma or the evaluation is wrong.
- **F-3.** Some trajectory-level quantity over `W₁` separates HC-TS from HC-SW, contradicting §7 L1.
- **F-4 (scoped negative, not a no-go).** In a preregistered instance and law class, DIL∃ fails for every
  `R ⊆` the declared region and every decoder. The negative holds for that instance only.
- **F-5.** HC-TS's predicted R-c failure at `t₀+3`, or HC-TM's at `t₀+m+1`, does not occur. Then the hand algebra
  is wrong.

***

## 7. Limits: when the controls cannot separate storage from transport

- **L1 (the decisive pair) [D].** Over `W₁`, HC-TS and HC-SW agree, after relabelling `r₂ ↦ u₁` and `r₁ ↦ u₂`, on:
  - the joint law of `(κ, A_t)`, `t ∈ W₁`;
  - `ε_max` and `TV`;
  - NB-1;
  - the ledger `D = 2 log 2`;
  - (R-a)–(R-c);
  - S-1, J-1 and D-TRN's "left";
  - ICH and CHC (both pass); SCH (both fail);
  - outside and inside cuts.

  `B_t` is independent of `(κ, A)` in both. Only DIL∃, which evaluates `φ` on configurations that do not occur in
  `W₁`, separates them, and so does the gap-free window `W₂`. So no criterion that reads the trajectory over `W₁`
  alone can separate storage from transport here.
- **L2.** Inflow tests (S-1, J-1, ICH, the outside cut) cannot separate an open pulse from storage for any
  `T < τ(R)`. For HC-TM, `τ(R) = m`. The cell-level outflow test CHC catches a pulse whose leading cell exits
  inside the window (HC-TM). It does not catch HC-TS, and it over-rejects redundant codes (CX-5).
- **L3.** A readback at ticks that are not contiguous cannot separate storage from recurrence (HC-R1, HC-R3). Beyond
  the period on the support, Lemma P makes every register blind.
- **L4.** No readback schedule separates re-supply (HC-R2). Only J-1, DIL∃ or a cut of `Q` does.
- **L5.** Closed circulation is not decided by any criterion here (I-4, CX-7).
- **L6.** Verdicts are relative to the cell decomposition and to `R` (CX-3), both declared.
- **L7.** For nonlinear rules `C_t` depends on the law and is computed cell by cell. SCH, ICH and CHC inherit the
  joint-information blind spot. DIL∃ uses supports only and avoids it, but it carries CX-4.
- **L8.** For approximate retention, separation is no finer than the exposure `η`. Under `π₀`, `η ≥` the probability
  that the write changes the record (Lemma E).
- **L9.** Under a law with φ-invariant support, the classification is vacuous for exact retention: there is nothing to
  classify (Lemma S′).

***

## 8. Proposed computational experiment (for separate owner authorization)

This is a specification only. It is not authorized (OQ-4 decision [C]) and nothing has been run.

- **Objective.** First, exact replay of the §3 controls under every §2.3 criterion. Then the same criteria on the open
  native route.
- **Phase A, controls.** Exhaustive enumeration in exact rational arithmetic, with no floating point in any verdict.
  - Instances:
    - HC-TS: `L = 4, 5`.
    - HC-TM: `m = 2, 3`, with `L = m+3`, plus the `g = u₂` HC-P-law case.
    - S1: `L = 2, 3`.
    - HC-SW: `L = 3`.
    - HC-SK: `k = 1, …, 5`, `T = 1, 2, 3`.
    - HC-R1: `L = 4`.
    - HC-R2: `L = 4`.
    - HC-R3: `L = 2`.
  - Each value derived in §3 is a replay check. A mismatch halts the run (§A.26 item 3).
- **Phase B, target.**
  - *K1 at K-18(b).* `|S| = 2¹⁰`; all 15 nonempty `R ⊆` the current slice of sites 1–4; the laws `π₀`, `δ₀` on the
    background, and HC-K3's `δ_b`; `T = 1, 2`.
  - *One nonlinear copy-form rule.* The SM:112 ring or rule h, at the smallest instance with `|S| ≤ 2¹⁶`, fixed in the
    preregistration, under the same law classes.
  - *Computations.* DIL∃ classes by union-find on `config(R)`. The decoder is fixed by a preregistered rule (which
    rule is an owner question, §9). Also `ε_max`, `TV` and J-1.
- **Decision rule (preregistered: the rule, not the numbers).** Each tuple (rule, `R`, law, `T`) is assigned one §4
  row by the §2.3 definitions. The verdict text is generated from the structured output.
- **Controls that must be green.**
  - HC-TS and HC-TM give TR.
  - S1 and HC-SW give ST; HC-SW gives circulating.
  - HC-R2 gives RS.
  - HC-R1 and HC-R3 give a Lemma P blind tick.
  - Countercontrol mutations:
    - (a) remove S1's quiet bit, and exact DIL∃ must fail;
    - (b) replace HC-SW's swap by a shift-out into the channel, and DIL∃ must fail;
    - (c) close HC-TM's ring inside `R`, and DIL∃ must pass as circulating;
    - (d) give HC-SW `r₂` uniform with no clock, and the fixed decoder must fail R-c.
  - A verdict over a red control is void.
- **Outputs (§A.44).** A JSON file per tuple with the fields of D-MET's required report, the DIL∃ classes, `Wr`, `η`,
  J-1 and the assigned row, plus the exit status. No verdict is read from log text.
- **Budget and stopping.** One pass and no adaptive extension. Estimated under 10 minutes in CI (§A.40). Halt on the
  first red control or replay mismatch.

| Invariant (§A.41) | Checkpoint |
|---|---|
| exact arithmetic | the type check of every probability as a rational, in the output schema |
| replay of §3 values | a Phase A comparison against the frozen table, by exit status |
| controls green before Phase B | the Phase B job depends on the Phase A job's conclusion |
| decoder fixed before testing | the decoder rule's hash recorded in the freeze and in each output |

***

## 9. Open questions for the owner

1. Does closed circulation inside `A` (HC-SW, CX-7) count as storage for O-RET, as D-RET's "fixed function of changing
   cells" suggests? Or does requirement 2's "simple advection" exclude it?
2. Is a criterion admissible that evaluates `φ` on register configurations which do not occur during the window
   (DIL∃, §7 L1)? Without one, the HC-TS / HC-SW pair is inconclusive at `W₁`.
3. Should DIL∃ take the union of `q`-supports, which is conservative and carries CX-4, or a tick-ordered form?
4. Should `T*` be tied to the register's transit time `τ(R)`, so that a gap-free window always exceeds it?
5. In view of Lemma E and HC-SK, where `w ≤ 2ε* = 0.1` in that family, what is `w*`?
6. Is the cut test admitted only as a diagnostic, given that it is not native? And with law-preserving resampling
   rather than uniform noise?
7. Should S-1, J-1, (h) and Remark C be reviewed before DIL∃ is built on them, and should DIL∃ be offered as the
   candidate operational test for (R-d) together with requirement 2's advection clause?
8. For §8 Phase B: which decoder rule, fixed before testing, is admissible (for example, the maximum-likelihood
   decoder at `t₀+1` computed from `(φ, μ)`)?
9. Is the computation of §8 authorized?

**Findings under §A.31.**
- DIL∃ (the outflow side of (R-d)) and the §7 L1 indistinguishability: NEW (candidate).
- Observation D0: NEW (candidate).
- Lemma E and Observation K: ELABORATING.
- Lemmas D and P: CONFIRMING.
- Assumption-watch marker: any claimed retention whose (R-d) test reads only inflow (S-1, J-1, ICH, outside cuts)
  admits HC-TM-type transport, and must be re-checked for outflow.

Literature, from memory and not re-read [L]: Landauer 1961 and Bennett 1982 (as in SOURCES); Fredkin and Toffoli,
"Conservative logic" (1982), for the Fredkin gate; Toffoli and Margolus, *Cellular Automata Machines* (1987), for
second-order reversible rules; Lizier, Prokopenko and Zomaya (Phys. Rev. E 77, 026110, 2008; Inf. Sci. 208, 2012) on
local information storage versus transfer in cellular automata. Their measures are statistical and per cell, and are
closest to SCH and ICH here.
