# O-RET first deliverable: route pages I, II, III

**Status.** WIP / UNVERIFIED; revised after independent review of ff4d4beb; criteria refined under the owner's decisions at #1032 c.6611966162 (see `DEFINITIONS.md`). Paper-only draft for #1032 under PO-1102 workstream B. Authority: the owner's authorization recorded at
#1032 c.6610742427. Base: `main` `ac558b570d0012a73369ebc1fbc1c09ac523ca94`. This revision has not been re-reviewed. It runs no
computation, Lean or search. Its hand checks (HC-K1 to HC-K4, HC-P, HC-F, HC-F0) are small enough to redo with pencil and paper, and
every step is written out. It adopts no premise and promotes nothing. The new interactions in route III are labelled
**new F2 extensions**. No candidate is selected. Selection needs an independent review of this exact text. Anchors are
listed in `SOURCES.md`, and all line numbers refer to `ac558b57`.

***

## 0. Common setting, criteria and lemmas (fixed before the route pages)

### 0.1 Setting

- **Model class.** A finite state set `S`, a bijection `φ : S → S` applied at every tick (time-homogeneous), and the
  joint law `μ` of the whole state at the preparation tick `t₀`. The second-order rules are of copy form
  `φ(x,y) = (y, F(x,y))`, where `x` is the previous slice and `y` the current slice (SM:106). K1 is
  `F(x,y) = Ay − x` (SM:296). The fixed instance is K-18(b): `(d,N,q,a) = (1,5,2,1)`, `Λ = ℤ/5`, carrier
  `Σ = {x₀, y₀}` (site 0, both slices), with `V ⊆` the current slice of sites 1–4.
- **Preparation (requirement 3).** `μ = μ_Σ ⊗ ν`. The carrier law `μ_Σ` has **full support on Σ's cells**, and the
  background law `ν` is independent of the carrier. "Background held fixed" means that `ν` is the same for every
  carrier preparation. A carrier preparation is a value `σ` of Σ at `t₀` with `μ_Σ(σ) > 0`.
- **Window (requirement 4).** Write tick `t₀ → t₀+1`. Hold tick `t₀+1 → t₀+2`. "One-step retention" means holding
  over the hold tick.
- **Readout.** A time-independent function `ρ` of the state. For a declared region this is an **H-cur (declared)** read
  of current-slice cells (K-8). A state-selected region (route I) is still a fixed function `ρ(s)`.
- **Ledger.** `D(μ) = D_KL(μ ‖ π₀)`, where `π₀` is the normalized counting measure (the uniform probability on `S`), so `D(μ) = log|S| − H(μ)`.

### 0.2 Criteria (my operationalization of requirements 2 and 4; see OQ-2)

The adopted operational criteria are now those of `DEFINITIONS.md` (D-RET, D-MET, D-TRN, D-ACC, D-SEN, D-SML), under
the owner's decisions at #1032 c.6611966162. RET-fd and RET-st below are kept as the criteria the route analyses used. RET-st is
not the adopted definition of retention (OQ-2 decision).

- **NB-1 (carrier sensitivity, single time).** There are carrier preparations `σ ≠ σ′` and a tick
  `t ∈ {t₀+1, t₀+2}` at which the law of `ρ(s_t)` given `σ` differs from its law given `σ′`, with `ν` fixed. A
  single-time law is used because a *path* law over `T ≥ 1` ticks (K1-RDY's `NB`) already presupposes reading across
  time, which is H-ret.
- **RET-fd (fixed decoder).** Some decoder `g` and some function `f` sensitive to the carrier satisfy
  `f = g(ρ(s_{t₀+1})) = g(ρ(s_{t₀+2}))` `μ`-a.s.
- **RET-st (static register).** A set `A` of readable cells takes **unchanged values** over the hold tick on the whole
  support, and its value at `t₀+1` satisfies NB-1. The carrier law is full support on Σ (as in 0.1).

RET-st implies RET-fd (take `g` = the projection onto `A`). The converse fails, and HC-K3 below gives the
counterexample. RET-st excludes the following by construction:
- the H-2s copy `x_{t+1} = y_t`, which changes cells (countercontrol (a));
- advection of a single imprint through `V`, which changes cells;
- a decoder that reads the tick from the state (HC-K3);
- the static-carrier field trick in the form of HC-K4, which full carrier support excludes.

RET-st does not exclude a passing imprint that a ready background has duplicated over consecutive cells (HC-P): such a
pulse holds a cell for one tick on the whole support with full carrier support. Requirement 4's separation of record
from passing field needs a condition beyond RET-st (OQ-2).

### 0.3 Lemmas (paper proofs, each in the stated direction only)

**Lemma S (a hold under a stationary law excludes a write).**
- *Hypotheses.* `S` is finite. `φ` is a bijection. `μ` is φ-invariant. `ρ` is time-independent, and `a := g∘ρ`.
  `κ` is a carrier variable with `a(s_{t₀}) ⫫ κ(s_{t₀})` under `μ`. Let `δ := P_μ(a∘φ ≠ a)`.
- *Claim.* For any carrier values `k, k′` of positive mass,
  `TV( L(a(s_{t₀+1}) | κ=k), L(a(s_{t₀+1}) | κ=k′) ) ≤ δ / min(μ(κ=k), μ(κ=k′))`.
  In particular, exact RET-fd (`δ = 0`) leaves the retained function blind to the carrier.
- *Proof.*
  - Because `μ` is invariant, `s_t ~ μ` at every tick. So the probability that `a` changes over a tick is the same
    `δ` at every tick, the write tick included.
  - Put `δ_k := P(a(s_{t₀+1}) ≠ a(s_{t₀}) | κ=k)`. Then
    `TV(L(a_{t₀+1}|k), L(a_{t₀}|k)) ≤ δ_k`, and `L(a_{t₀}|k) = L(a_{t₀})` by the independence hypothesis.
  - So the TV in the claim is at most `δ_k + δ_{k′}`. Also
    `δ = Σ_j μ(κ=j) δ_j ≥ min(μ(k), μ(k′)) (δ_k + δ_{k′})`. ∎
- *Scope.* The lemma covers every rule (copy form or not), every time-independent readout (fixed region or
  state-selected region), `π₀`, and every member of K-17(a)'s invariant class for which the independence hypothesis
  holds.
- *Not covered.* For the approximate bound, non-invariant `μ`. For exact retention, laws whose support is not
  φ-invariant (Lemma S′). Decoders that depend on the tick. A readout that already depends on the carrier
  at `t₀` (overlap).
- *Controls.*
  - `φ = id`: every `a` is held, and none is written. Consistent.
  - The H-2s copy on K1 retains (O-ACC hand check: 1 bit), but only through a change of decoder from `y` to `x`, so
    it lies outside the lemma. This is consistent: the lemma must not exclude H-2s.
  - The sealed core σ: `b` is held, inert and blind. Consistent.
  - The global energy `E` (SM:296), read in full, is conserved and carrier-sensitive: the independence hypothesis is
    load-bearing.
  - `M_F` under `π₀` attains the bound with equality (HC-F0).
- *Related claims.* Main §4.6 is related in spirit but is conditional on (EM) and coarse-grained. Lemma S neither
  derives it nor is derived from it.

**Lemma S′ (exact form, support only).** `S` finite, `φ` a bijection, `φ(supp μ) = supp μ`, `a = g∘ρ`
time-independent. If `a(s_{t₀+2}) = a(s_{t₀+1})` μ-a.s., then `a(s_{t₀+1}) = a(s_{t₀})` μ-a.s. Hence
`L(a(s_{t₀+1}) | κ=k) = L(a(s_{t₀}) | κ=k)` for every carrier variable `κ`: the write tick transfers nothing. If also
`a(s_{t₀}) ⫫ κ`, the retained function is blind.
*Proof.* `s_{t₀+1}` ranges over `φ(supp μ) = supp μ`, so the hold gives `a∘φ = a` on `supp μ`. Apply this at
`s_{t₀}`. ∎

**Lemma Q (a written-and-held record needs a support restriction).**
- *Hypotheses.* `φ` is a bijection of a finite `S`, `a` is a function on `S`, and `K` is a set of values of `a`.
- *Claim.* If `a(φs) = a(s)` for **every** `s` with `a(s) ∈ K`, then no state with `a ∉ K` is ever mapped into
  `a ∈ K`. So a record value written from a blank value cannot be held unconditionally. Exact holding requires the
  support at the hold tick to exclude the configurations that overwrite it.
- *Proof.* `φ(a⁻¹K) ⊆ a⁻¹K`, and `φ` is injective on a finite set, so `φ(a⁻¹K) = a⁻¹K`. The preimage of `a⁻¹K` is
  therefore `a⁻¹K`. ∎

**Lemma C (copy bound; known in substance: Bennett 1982; Landauer 1961, background).**
- *Hypotheses.* `W` is a bijection on `C × R`, `(c′, r′) = W(c, r)`, and `c ⫫ r`.
- *Claim.* `I(c; r′) ≤ D(μ_R ‖ u_R) + H(c′ | c)`.
- *Proof.* At fixed `c`, `r ↦ (c′, r′)` is injective. So `H(r) = H(c′, r′ | c) ≤ H(r′|c) + H(c′|c)`, and
  `I(c; r′) ≤ log|R| − H(r) + H(c′|c)`. ∎
- *Reading.* Under a register of maximal entropy (`D = 0`), a write that preserves the carrier (`c′ = h(c)`) is
  blind. A write that is sensitive to the carrier must export at least as much entropy into the carrier as it gains.
  This generalizes the CNOT control of #1032 c.6567189236 (`D = log 2`, `I = log 2`, `H(c′|c) = 0`).
  The inequality is an entropy trade-off, not a uniqueness statement. It does not single out exchange: writes that
  disturb the carrier partially, and writes that use readiness (`D > 0`) instead of disturbance, also satisfy it.

**Lemma L (for linear rules, the transfer does not depend on the prior).**
- *Hypotheses.* K1 with any additive `A` over `ℤ/q`, and a product prior with full carrier support.
- *Superposition.* By superposition `y_i(t₀+k) = M_{k,i}·c + β_{k,i}(b)`, where `c` is the carrier and `b` the
  background.
- *Both directions.*
  - Cell `i` is static over `(t₀+k, t₀+k+1)` on the support ⟺ `(M_{k+1}−M_k)_i = 0` **and**
    `(β_{k+1}−β_k)_i = 0` on `supp ν`. (⇒: set `c = 0`, then vary `c`. ⇐: immediate.)
  - The cell is carrier-sensitive ⟺ `M_{k,i}(c−c′) ≠ 0` for some `c, c′`, **and** the `ν`-law of `β_{k,i}` is not
    invariant under translation by that element.
- *Consequence.* The geometric condition on `M` is fixed by `(φ, Σ, i, k)` alone. A prior can supply the
  `β`-conditions (readiness and quiet) but cannot create static transfer.

### 0.4 Hand checks on the K-18(b) instance

Arithmetic is mod 2, with `x′ = y` and `y′_i = y_{i−1} + y_{i+1} + x_i`, indices mod 5.

**HC-K1: carrier imprint.** By superposition only the carrier cells are nonzero: `x = (x₀,0,0,0,0)` and
`y = (y₀,0,0,0,0)`.

| tick | `y` (sites 0–4) | `x` |
|---|---|---|
| `t₀+1` | `(x₀, y₀, 0, 0, y₀)` | `(y₀,0,0,0,0)` |
| `t₀+2` | `(y₀, x₀, y₀, y₀, x₀)` | `(x₀, y₀, 0, 0, y₀)` |
| `t₀+3` | `(x₀, y₀, x₀+y₀, x₀+y₀, y₀)` | `(y₀, x₀, y₀, y₀, x₀)` |

**HC-K2: no static current-slice cell, for any background law.**
- The carrier parts at sites 1–4 over ticks 1, 2, 3 are:
  - site 1: `y₀, x₀, y₀`
  - site 2: `0, y₀, x₀+y₀`
  - site 3: the same as site 2
  - site 4: the same as site 1
- At tick `t₀` the cells of `V` carry no carrier part (`M₀ = 0`), so no cell is carrier-sensitive at `t₀`.
- For `k ∈ {1,2}`, consecutive entries differ at every site, so `(M_{k+1} − M_k)_i ≠ 0` for every
  `i ∈ {1,…,4}`. (For `k = 1`, sites 2 and 3 have `M_{1,i} = 0` and are not carrier-sensitive at `t₀+1` either.)
- By Lemma L, no cell of `V ⊆ {1,…,4}` meets RET-st over any consecutive pair in `[t₀, t₀+3]`, for **any** product
  background law `ν`, including the fully ready `ν = δ₀`.
- For the single cell `V = {1}`, RET-fd fails as well. With background terms,
  `y₁(t₀+1) = y₀ + (x₁+y₂)` and `y₁(t₀+2) = x₀ + (x₂+y₁+y₃+y₄)`. A function of the first depends only on `y₀`, and a
  function of the second only on `x₀`. So `f` is constant.

**HC-K3: a fixed decoder is not retention (proposed countercontrol (g)).**
- Take `V` = sites 1–4, and `ν = δ_b` with `b`: `x₂ = x₄ = 1`, all other background cells 0.
- The background-only evolution is `y(t₀+1) = (0,0,1,0,1)` and `y(t₀+2) = (1,1,0,0,0)`.
- Adding HC-K1 gives `R₁ = (y₀, 1, 0, y₀+1)` and `R₂ = (x₀+1, y₀, y₀, x₀)`.
- The decoder `g(u) = u₁ if u₂ ≠ u₃, else u₂` returns `y₀` at both ticks, for all `(x₀, y₀)`. So RET-fd holds.
- But `y₀` is a wavefront moving from sites 1 and 4 to sites 2 and 3, and the decoder reads the tick from a
  background marker (`u₂ ≠ u₃`). No cell is static, so RET-st fails.
- Under non-invariant priors, RET-fd alone therefore admits advection with an internal clock.

**HC-K4: the static-carrier field trick (countercontrol (e)).**
- Restrict the carrier to `{x₀ = y₀}`, i.e. to the two preparations `(0,0)` and `(1,1)`, and take `ν = δ₀`.
- Then site 1 reads `y₀` at `t₀+1` and `x₀ = y₀` at `t₀+2`, so it looks static.
- The value at `t₀+2` comes from `x₀`, the carrier's other slice arriving at site 1. Release `x₀` and site 1 tracks
  `x₀`.
- This is the passing field, which is why RET-st requires full carrier support.

**HC-P: a duplicated pulse passes RET-st (proposed countercontrol (h); proposed by the review, not yet reviewed).**
- Cells `u_j ∈ 𝔽₂`, `j ∈ ℤ/L`, `L ≥ 4`. One tick is `u₁ ← u₁ ⊕ u₀` followed by the shift `u_j ← u_{j−1}`: a
  time-homogeneous bijection.
- The carrier is `Σ = {u₀}`, with full support. `ν = π₀(· | u₁ = 0, u_{L−1} = 0)`, a product law with `D = 2 log 2`.
- The evolution is `u₂(t₀+1) = u₁(t₀) ⊕ c = c` and `u₂(t₀+2) = c ⊕ u_{L−1}(t₀) = c`, after which the pulse moves on.
- `A = {u₂}` therefore satisfies RET-st, yet this is countercontrol (e). The value at `t₀+2` is re-supplied from
  `u₁(t₀+1)`, which carries the carrier. It is not held from `u₂(t₀+1)`.
- The ledger equals `M_T`'s, so the ledger does not separate the two cases either.

***

## Route I: native access geometry

### 1. Mechanism
- **Smallest version.** A read region selected by the state through a rule fixed in advance from `φ` alone:
  `V_t := {i : e_i(x_t, y_t) ≠ 0}`, where `e_i` is a local density of a conserved quadratic invariant of the
  second-order rule. SM:296 gives `E(u,v)`, `Q_B` and `P_C` as "sums of local densities" on pairs
  `(x(t−1), x(t))`.
- The readout is `ρ(s) = (V(s), y|_{V(s)})`, an H-cur read on the selected sites. Identity across time is supplied by
  the selection rule.
- **Variants.** (I-y) a selector that depends on `y_t` only. (I-xy) a selector that depends on both slices, as above.
  (I-ad) an adaptive selector `V_{t+1} = g(R_t)`. (I-gl) a region that moves with a localized excitation.

### 2. Dependency it breaks
- P2-G's hypothesis that `R_t` is a fixed function of `y_t` alone, and O-ACC's fixed declared region (Main:88: "the
  partition is fixed"). P2-G's proof "breaks if `V_{t+1}` or `ρ_{t+1}` depends on `R_t` … or on `x_t`" (P2-G §2).
- (I-y) breaks nothing, because P2-G covers `V_t` chosen from `y_t`. (I-xy) and (I-ad) are the only variants outside
  P2-G.

### 3. Justified starting law
- `π₀`, the corpus's canonical measure (Main:56: "a selection principle, not uniqueness from invariance alone").
  Status: **CONDITIONAL[H-μ]**. No further selection is made.
- Route I by definition changes the access, not the law. A law whose support is not φ-invariant turns it into route II.

### 4. Record witness
- **None exists in this route's scope.** Under `π₀`, or any law with φ-invariant support, Lemma S′ applies to every
  time-independent `ρ`, state-selected regions included.
  - Exact RET-fd forces the retained `a` to be a constant of motion on the support.
  - If `a(s_{t₀})` does not depend on the carrier, then `a` is blind.
  - If `a(s_{t₀})` does depend on the carrier, which under a product preparation requires `a` to read Σ's cells at `t₀`, then the "record"
    already existed at `t₀`. No transfer occurs (requirement 2), and the readout overlaps the carrier (the matrix
    excludes overlap; MM O-RET row).
- An exact witness is possible only with decoders that change with the tick (outside Lemma S′). Those are H-2s-type re-reads of
  `x_t`, or need a clock.
- No candidate passes requirement 2 together with requirement 4.

### 5. Strongest counterexample
The strongest attack: the selector `e_i(x,y)` is a function of the previous slice, so `ρ` is a declared read of
previous-slice information. That is H-2s expressed through a nonlinear statistic. O-ACC found that "the readable
σ-algebra is always a datum (Sub:44; Lemma 1c)", and choosing `e_i` as the read is that datum.
- (a) bare copy / H-2s: **fails.** (I-xy) reads `x_t` through `e_i`, and with a decoder that changes by tick it
  reduces to the H-2s copy.
- (b) static declarative decoder: **fails.** Picking `e_i` (or any invariant) as "what V reads" is a declared decoder.
  SM:296 supplies many invariants and does not choose one.
- (c) quiet background through the prior: **not applicable** under `π₀`. It applies once a restricted law is added
  (route II).
- (d) prescribed moving readout: **passes as a distinction, blocked anyway.** P2-G covers schedules fixed by `t` or
  `y_t`. (I-xy) differs from (d), but Lemma S′ blocks it.
- (e) passive wave/wake: **fails for (I-gl).** A co-moving region reads the carried excitation itself. The register is
  then the carrier (overlap), not a record.
- (f) indistinguishable carrier: **not applicable.** Nothing is conditioned under `π₀`.
- CN (#1032 c.6567189236): **not applicable.** No gate is added.

### 6. Classification
- **BLOCKED[Lemma S′].** Scope: finite `S`, any bijection, any law with φ-invariant support (`π₀`, every K-17(a)
  member, every full-support law), exact retention, any time-independent readout (fixed or state-selected). With
  `a(s_{t₀}) ⫫ κ` the retained function is blind; otherwise the write tick transfers nothing.
- With `a(s_{t₀})` depending on the carrier, the route fails requirement 2 (no transfer; overlap).
- **UNDECIDED** outside this scope: decoders that change with the tick (they need a clock; under the OQ-2 decision they
  are admissible only with an accounted clock, and `DEFINITIONS.md` Remark C, unreviewed, shows that Lemma S′ then
  applies to exact retention), approximate retention (Lemma S's bound only), laws whose support is not φ-invariant (that is route II), and derived observers (O-OBS).
- **Circularity (requirement 5).**
  - (I-ad) presupposes that `R_t` is retained, which is circular: H-ret.
  - (I-gl) and an "observer = selected region" reading presuppose the observer, which is O-OBS.
  - (I-xy) is not circular, but it is a declaration, not a derivation.

***

## Route II: independently sourced prior

### 1. Mechanism
- **Smallest version.** Keep a rule already in the corpus. K1 at K-18(b) is the rule of SM:224's form. Keep a fixed
  declared `V` with an H-cur (declared) read.
- Change only the law at `t₀`: `μ = μ_Σ ⊗ ν`, with `μ_Σ` full support and `ν` a non-counting background law (a ready
  register, a quiet neighbourhood).
- Read `V`'s current slice at `t₀+1` and `t₀+2`.
- The next version up applies the same construction to the nonlinear copy-form rules in the corpus: the SM ring rule
  (SM:112) and rule h.

### 2. Dependency it breaks
- The full-support prior of P2-G (E), and the uniform prior of A′.
- Lemma S′ adds a requirement: an exact static record requires a law whose support is not φ-invariant (Lemma S′): in
  particular a non-invariant law that is not of full support. Every measure that Main Lemma 3
  selects or makes canonical (`π₀`, the uniform measure on a cycle) is invariant.
- Lemma Q adds that the law must exclude the configurations that overwrite at the hold tick. P2-G's necessary
  condition must also hold: every `y`-section `X_y` is proper.

### 3. Justified starting law
- **No SOURCED law exists in the corpus.**
- The invariant laws are blocked for exact retention by Lemma S′: the write tick transfers nothing. These are `π₀`
  (Main:56), the members of K-17(a), the energy shells (SM:296, SM:811 candidate) and Main:62's selection among orbits.
  Only `π₀` is a product law; for the others `a(s_{t₀}) ⫫ κ` can fail, and the exclusion is the no-transfer form, not
  blindness.
- Main:60 permits structured preparations as a "realization datum", which is admissible but not sourced.
- Main:62 fixes the selection among orbits by "maximal entropy compatible with the observer's records". Used for
  O-RET, this **presupposes the records** it would explain, which is circular (requirement 5). In K1-RDY it is H-sel
  (K-5).
- The persistence-conditioned P3 law is H-sel (K-12(b)). The unreviewed diagnostic in #1031 finds NB failing at
  K-18(b).
- Main §4.6 is a conditional selection of *where* observers can exist under (EM), not a preparation law.
- **Ceiling: CONDITIONAL[H-sel].**

### 4. Record witness
- **K1 (linear): none, for any background law.**
  - By Lemma L, the carrier's imprint on `V` does not depend on `ν`. The prior adds offsets only.
  - HC-K2 shows that no current-slice cell of sites 1–4 is static and carrier-sensitive over any consecutive pair in
    `[t₀, t₀+3]`, under every product `ν`, `δ₀` included. That is maximal readiness, `D = 8 log 2` on the background.
  - Readiness gives a *display*: `V = {1}` reads `y₀`, then `x₀` (NB-1 holds). It does not give retention.
  - This refines #914 c.6567198108, which says workstreams A and B are not interchangeable. On this instance a ready
    supply, which is workstream A's target, does not produce retention.
- **Nonlinear copy-form rules: none found, none excluded.**
  - The background can modulate the transfer there, so Lemma L does not apply.
  - Center-freeness (SM:112 constraint (ii); SM:224) means a cell's next value does not depend on its current value.
    A static cell therefore needs `drive_i(t) − x_i(t) = y_i(t)` on the support. The neighbourhood and the previous
    slice must jointly track the record.
  - I have no witness and no exclusion.

### 5. Strongest counterexample
- HC-K2: on the linear instance, the prior cannot do the job at all.
- HC-K3 and HC-K4 show the two ways a restricted law fakes retention: a background clock with a fixed decoder, and a
  static carrier.

Against the countercontrols:
- (a) H-2s: **passes.** Only current-slice cells are read.
- (b) static declarative decoder: **passes under RET-st.** It **fails under RET-fd**: HC-K3 is a decoder that reads a
  marker the prior planted.
- (c) quiet background through the prior: **fails without a source.** Lemma Q makes a support restriction necessary,
  and route II consists of exactly that restriction. Only a source for `ν` would separate it from (c).
- (d) prescribed moving readout: **not applicable.** `V` is fixed.
- (e) passive wave/wake: **fails on K1.** Everything carrier-sensitive at `V` is the propagating imprint
  (HC-K1, HC-K4).
- (f) conditioning that hides the carrier: **avoided by construction** (product law, full-support carrier). A
  conditioned `ν` can still make `V` blind, as in #1031's diagnostic: P3 at K-18(b) gives weak bias, and NB fails.
  Any law fixed later must be checked for this.
- CN: **applies** to the write. Under `D = 0` a write that preserves the carrier is blind (Lemma C). K1's
  `y′_V = drive − x_V` is of this kind, with `x_V` as the one-time pad.

### 6. Classification
- **Under RET-st: BLOCKED[Lemma L + HC-K2]** for linear K1 at K-18(b). Scope: `V ⊆` the current slice of sites 1–4,
  every product law with full carrier support, RET-st, consecutive pairs in `[t₀, t₀+3]`. It is not extended to other
  N, q, V, Σ or ticks. Under RET-fd a fixed-decoder witness exists (HC-K3); it reads a tick marker and fails
  countercontrol (g).
- **Under D-RET (adopted): UNDECIDED** for linear K1 at K-18(b), in the same scope.
  - *Reason for the change.* The OQ-2 decision (#1032 c.6611966162) does not adopt static cells as the definition, so the
    RET-st block no longer classifies the route.
  - HC-K3 is a fixed-decoder candidate. Its admissibility turns on (R-d), whose test (S-1 or J-1) is unadopted, and on
    requirement 2's rejection of simple advection.
  - Approximate retention at this instance is not addressed.
- **BLOCKED[Lemma S′]** for every law with φ-invariant support (RET-st/RET-fd, exact), every invariant and every
  full-support law included.
- **UNDECIDED** for nonlinear copy-form rules (SM:112 ring, rule h) under a law named in advance whose support is not
  φ-invariant.
  - *What would decide it:* a paper proof, or a bounded exact check preregistered at a fixed small instance with a
    fixed law. Lemmas S and Q, HC-K3 and HC-K4 would serve as controls. That check is computational and is not
    authorized (OQ-4).
  - Its ceiling is **CONDITIONAL[H-sel, H-cur (declared)]**, never SOURCED from present sources.
- **Circularity (requirement 5).**
  - Main:62's record-compatible selection is circular for O-RET.
  - A `ν` chosen to make E ready is Z1 (a record supplying readiness) if it is the record's own region.
  - A P3-type persistence event is not memory (Z2).
  - The ready state cannot be inferred from the record whose production needs it (requirement 3).

***

## Route III: observer/substate interaction (new F2 extension)

### 1. Mechanism
**Smallest version: model `M_F`, a new F2 extension.**
- A track of `L ≥ 2` channel cells `(p_j, v_j) ∈ 𝔽₂²` moves one step per tick. `p` is a presence bit and `v` a value.
- One register bit `r` sits at track position 0, and its self-update is the identity.
- At each tick a Fredkin gate acts: if `p₀ = 1`, swap `v₀` and `r`. The channel then shifts.
- `φ` is bijective: an involution followed by a permutation. It is time-homogeneous.
- `r` is read (H-cur declared) at `t₀+1` and `t₀+2`. The carrier is Σ = `(p₀, v₀)` at `t₀`.

**Variant `M_T`.** A Toffoli write `r ← r ⊕ p₀v₀`. The carrier keeps its value. This is the CNOT control with a
presence switch.

### 2. Dependency it breaks
- Copy form (SM:106; SM:224's form lemma). The register's identity self-update is center-dependent, contrary to
  SM:112 constraint (ii), and the gate is not of the second-order form.
- O-ACC §6.2 records leaving copy form as a change of premise, and that is what this route makes.

### 3. Justified starting law
- **`M_F`:** `μ_F = π₀(· | p_{L−1} = 0)` at `t₀`. One quiet bit: the channel cell arriving at the hold tick is
  empty. `D = log 2`.
- **`M_T`:** additionally `r = 0` (a ready register). `D = 2 log 2`.
- Neither law is sourced: each is **CONDITIONAL[H-sel]**. Under `π₀`, Lemma S excludes exact retention in both
  models (both are time-homogeneous bijections), the CNOT control blinds `M_T`, and `M_F` retains approximately (HC-F0).

### 4. Record witness
**HC-F (in `M_F`).**
- *Write.* At `t₀`, if `p₀ = 1`, then `r(t₀+1) = v₀` and the carrier leaves with `r`'s old value. If `p₀ = 0`, `r` is
  unchanged.
- *Hold.* At `t₀+1` the cell at position 0 has `p = 0` (the quiet bit), so `r(t₀+2) = r(t₀+1)` on the whole support.
  RET-st holds.
- *Carrier sensitivity.* For `σ = (1,0)` and `σ′ = (1,1)`, the laws of `r(t₀+1)` are `δ₀` and `δ₁`, with disjoint
  supports. NB-1 holds with `ν` fixed and full carrier support.
- *Consistency with the lemmas.*
  - Lemma C is tight: with the uniform carrier `c = (p₀, v₀)` of `μ_F`, `I(c; r′) = H(c′|c) = ½ log 2` and
    `D(μ_R ‖ u_R) = 0`; conditionally on `p₀ = 1`, `I = H(c′|c) = log 2`.
  - Lemma Q: the quiet bit excludes the overwriting configuration.
  - Lemmas S and S′: `μ_F` is not invariant, and its support is not φ-invariant.
- *Budget in this model.* A hold of `k` ticks needs `k` quiet cells and `L ≥ k+1`. At `L = 2` the carrier's cell
  returns at `t₀+2` with `p = 1` and swaps the record back at the next tick. Persistence, renewal and reusable
  supply are not addressed.

**`M_T`** gives the same with the carrier undisturbed, at a ledger one bit larger.

**HC-F0: `M_F` under π₀.**
- Take `σ = (1,0)`. Then `r(t₀+1) = 0`. Over the hold tick the arriving cell has `p = 1` with probability 1/2 and
  then swaps in a uniform `v`, so `P(r(t₀+2) = 0 | σ) = 3/4`. Symmetrically for `σ′ = (1,1)`.
- The TV between the two carrier laws goes from 1 to 1/2, and the record is lost with probability 1/4 per tick.
- So `M_F` gives genuine **approximate** one-step retention under the canonical law, with no quiet bit.
- With `κ = (p₀, v₀)` (four values, mass 1/4 each), `δ = P(p₀ = 1, v₀ ≠ r) = 1/4`, and the TV at `t₀+1` between
  `(1,0)` and `(1,1)` is 1 `= (1/4)/(1/4)`: Lemma S's bound is attained with equality.
- Under maximum skepticism this branch still rests on E-reg (unjustified), on H-cur (declared), and on an exchange
  write (admissible as transfer under the OQ-1 decision, D-TRN). It is favorable only to the extent that H-sel drops out.

### 5. Strongest counterexample
- `M_F` and `M_T` are an apparatus designed for this purpose, so requirement 5 is the first attack.
- Under `π₀` neither retains exactly (Lemma S), `M_T` is blind (CN), and `M_F` retains approximately (HC-F0).
- `M_F`'s carrier-sensitive write is an exchange: the register takes the carrier's value. Under the OQ-1 decision an
  exchange counts as transfer, given a distinct readable register and retention after the carrier has left
  (`DEFINITIONS.md` D-TRN). `M_F`'s register `r` is distinct, and HC-F shows the hold after the carrier cell has moved
  on. Its (R-d) status is provisional: S-1 and J-1 are unadopted.

Against the countercontrols:
- (a) H-2s: **passes.** `r` is a current cell and its self-update is the identity.
- (b) declarative decoder: **passes.** The decoder is `r` itself, with RET-st. `r`'s readability is still declared
  (OQ-3).
- (c) quiet background through the prior: **fails without a source.** The quiet bit (and `r = 0` in `M_T`) is exactly
  (c). Lemma Q makes some such restriction unavoidable.
- (d) prescribed schedule: **passes.** The gate is time-homogeneous and triggered by the state. A switch-off by schedule
  would fail (d).
- (e) passive wake: **passes given (c).** `r` holds after the carrier has left, independently of later channel values
  on the support.
- (f) indistinguishable carrier: **passes.** The carrier law is full support, and no event touches the carrier.
- CN: **`M_T` fails under `D = 0`** and passes only with `r = 0`. `M_F` avoids readiness by exporting `r`'s entropy
  into the carrier (Lemma C).

### 6. Classification
- **CONDITIONAL[new F2 extension E-reg (designed register and gate, unjustified under §A.29: no preserved results stated,
  no independent prediction); H-sel (quiet bit; plus `r = 0` for `M_T`); H-cur (declared) read of `r`]**.
  Scope: the toy models `M_F` and `M_T`, exact, one hold tick.
  CONDITIONAL classifies `M_F` and `M_T` as toy witnesses of what such an apparatus needs from the law. As an O-RET
  mechanism route III is not a candidate while E-reg is unjustified (§A.29) and designed for the purpose.
- **BLOCKED[Lemma S′]** for exact retention under any law with φ-invariant support.
- Under `π₀`, `M_F` gives approximate one-step retention with no quiet bit (HC-F0: `ε_max` = 1/4 at `t₀+2`). The OQ-7
  decision makes this admissible in principle.
  - Whether it is a witness is **UNDECIDED[`ε*` not set]**, under E-reg, H-μ and H-cur (declared). The ¼ error is a
    result, not a threshold (`DEFINITIONS.md` D-MET).
  - *Reason for the change from CONDITIONAL.* The OQ-7 decision (#1032 c.6611966162) makes success relative to a tolerance fixed
    in advance.
- It is not a SOURCE-CANDIDATE.
- **Circularity (requirement 5).** E-reg *is* observer-level apparatus (MR★ M.3(iii); O-ACC §6.2), built to have a
  register and a trigger. As designed here, that presupposes the instrument; an interaction justified independently of
  this purpose needs its own assessment. The ready `r` in `M_T` presupposes a ready reservoir. It
  generates neither the observer nor the record. It shows only what such an apparatus minimally needs from the law.

***

## Comparison

- **No SOURCE-CANDIDATE on any route.**
- **The cross-route constraint (candidate NEW, for review).**
  - By Lemma S′, every exact fixed-decoder record, and so every RET-st record, under a law with φ-invariant support is
    never written: the write tick transfers nothing, and with a readout independent of the carrier the record is blind.
    This holds for any rule and any time-independent readout.
  - By Lemma Q, a written-and-held record needs a support restriction that excludes overwrites at the hold tick.
  - So routes I and III are **not independent of route II's sourcing problem**. Each exact mechanism here needs a
    law whose support is not φ-invariant, with a quiet restriction at the hold tick, and the corpus's canonical and selected laws are
    invariant.
  - This bears on MM's O-RET edge "O-ACC or O-RDY". For exact retention with a time-independent decoder under a
    time-homogeneous bijection, O-ACC, being a convention, does not discharge it, and a law whose support is not
    φ-invariant (a resource of O-RDY type) is necessary. Approximate retention is not covered: `M_F` under `π₀` retains
    approximately (HC-F0). The resource is a quiet hold, not necessarily E-readiness. The
    owner decides whether to record this (OQ-6).
- **Witnesses found on paper.** Under the OQ-8 decision these are compared by the resource table of `DEFINITIONS.md`
  D-SML, not by one scalar. No ranking is issued while `T*`, `ε*` and `w*` are unset. The witnesses are route III's `M_F`, with one quiet bit and an exchange write. Minimality is not
  shown: a trigger on `k` presence bits lowers the ledger to `log(2^k/(2^k−1))`, at write probability `2^{−k−1}`. With a copy write it is
  `M_T`, with two bits. It is CONDITIONAL on a new, unjustified F2 extension and on H-sel. It is not selected.
- **Open native route with no added interaction:** route II on a nonlinear copy-form rule already in the corpus. It adds no interaction,
  is UNDECIDED, and has ceiling CONDITIONAL[H-sel]. On linear K1 at K-18(b) it is BLOCKED.
- **Open:**
  - a source for a quiet law whose support is not φ-invariant;
  - nonlinear native rules;
  - approximate retention (realized outside copy form by `M_F` under `π₀`, HC-F0; open for native rules);
  - records whose decoder changes with the tick (they need a clock);
  - derived observers;
  - persistence and renewal beyond one tick.
- **Findings under §A.31.**
  - Lemma S: NEW (candidate).
  - Lemma S′: NEW (candidate; found in review).
  - Countercontrol (g) / HC-K3: NEW (a proposed countercontrol).
  - Lemma L and HC-K2: ELABORATING (they sharpen the A/B separation at the instance).
  - Lemma Q: ELABORATING.
  - Lemma C: CONFIRMING (Bennett 1982 in substance; Landauer 1961 background; it generalizes CN).
- **Assumption-watch marker.** Any positive claimed under an invariant law for O-REC, O-SET displays or the rule-h S3
  analogue must change decoders, retain only approximately within Lemma S's bound, or transfer nothing (the retained
  function already depended on the carrier at `t₀`).

## Owner questions and decisions

Each question below is followed by the owner's decision at #1032 c.6611966162, in one line. The operational form is in
`DEFINITIONS.md`.

- **OQ-1.** Does an exchange write (the register takes the carrier's value and the carrier leaves with the register's
  old content) count as "nontrivial transfer", or as the "simple advection" that requirement 2 rejects? Under a
  register of maximal entropy, Lemma C bounds the information a carrier-sensitive write can gain by the entropy it
  exports into the carrier. That is an entropy trade-off and does not single out exchange.
  *Partial source answer (found by the review).* The CN comment (#1032 c.6567189236) treats `m′ = c` with a ready
  memory as "a perfect one-bit readable record" conditional on the readiness resource, so "simple advection/copy" most
  plausibly targets countercontrol (a). Exchange stays open.
  *Decision (#1032 c.6611966162):* exchange can count as nontrivial transfer, with a distinct readable register and retention after the carrier has left; carrier preservation is a separate property (D-TRN).
- **OQ-2.** Adopt RET-st (static readable cells, full carrier support) as the operational reading of requirement 4?
  Or also admit records whose decoder depends on the tick? Those need a clock, and (d) applies to them.
  RET-st is too weak and too strict for this purpose. It admits the duplicated pulse of HC-P. It excludes a record
  held in an invariant function of changing cells, such as `r₁ ⊕ r₂` under a register swap, which a fixed decoder
  reads without a clock. A screening condition (proposed by the review, not yet reviewed), under which `A`'s hold-tick
  update reads only `A` and cells whose `t₀+1` values are independent of the carrier, separates these cases on HC-K3,
  HC-K4, HC-P, `M_F` and the swapped pair. It is offered for review, not adopted.
  *Decision (#1032 c.6611966162):* static cells are not the definition; a record may persist in a fixed, physically readable function of changing cells, not continually re-supplied by the carrier; readouts that change with the tick need an accounted clock, identity and access; S-1 awaits independent review, with joint-information checks (D-RET).
- **OQ-3.** O-ACC makes the readable σ-algebra a datum for a fixed region, so requirement 1 ("derivable accessible
  register") is unmet by every route. Is H-cur (declared) on a fixed register the admissible baseline, carried as a
  named hypothesis? Or is requirement 1 to be read as unmeetable in the present architecture?
  *Partial source answer (found by the review).* K-8 ("H-cur is **declared**, not native") and the owner's record at
  #1032 c.6610742427 ("D-07(a) discharges the O-ACC prerequisite for this scoped unit") make H-cur (declared), carried
  as a named hypothesis, the recorded baseline. Whether requirement 1 can be met remains the owner's question.
  *Decision (#1032 c.6611966162):* H-cur (declared) is the named conditional baseline; physical sourcing of access stays an outstanding obligation for any SOURCE-CANDIDATE (D-ACC).
- **OQ-4.** Authorize, separately, a preregistered bounded exact check of route II on the SM ring or rule h, with a law
  fixed in advance? This needs computation and is not requested here.
  *Decision (#1032 c.6611966162):* no computational check yet; the criterion and metric are to be settled and reviewed first, then a proposal is presented for separate authorization.
- **OQ-5.** For O-RET, use NB-1 (a single-time law) rather than K1-RDY's path-law NB, which presupposes H-ret?
  *Partial source answer (found by the review).* Requirement 2's wording, "some future readable register law
  differs", is a single-time law, which largely answers this.
  *Decision (#1032 c.6611966162):* NB-1 is accepted; a path-law comparison is additional evidence only and never supplies access across time (D-SEN).
- **OQ-6.** Record the cross-route constraint (Lemmas S′ and Q) against MM's O-RET L-edge after review?
  *Decision (#1032 c.6611966162):* record the constraint as a scoped annotation with its hypotheses, not a replacement of the edge (`ANNOTATION.md`, draft).
- **OQ-7.** Is approximate retention admissible for O-RET, and in which metric? `M_F` under `π₀` realizes it (HC-F0).
  *Decision (#1032 c.6611966162):* approximate retention is admissible; the primary metric is worst-case decoding error, with TV reported per tick; the tolerance `ε*` is to be set from the record's requirements before testing (D-MET).
- **OQ-8.** What does "smallest" measure? `D` has no minimum attained by one quiet bit (Comparison, witnesses
  found on paper).
  *Decision (#1032 c.6611966162):* use a resource comparison at fixed performance requirements, not one scalar; a vanishing write probability cannot win by the ledger alone (D-SML).

## Review requests (for the independent reviewer)

1. Check Lemmas S, Q, C and L, including their hypotheses and the one-direction statements.
2. Recompute HC-K1 to HC-K4 and HC-F by hand.
3. Test whether RET-st is too strict (it might exclude a legitimate record) or too weak (it might admit an advective
   one).
4. Check that no classification states a no-go beyond its scope.
5. Check the literature attributions. Lemma C (Landauer 1961; Bennett 1982) and the link to records requiring an
   initialized memory (e.g. Wolpert 1992) are cited from memory and were not re-read here.
