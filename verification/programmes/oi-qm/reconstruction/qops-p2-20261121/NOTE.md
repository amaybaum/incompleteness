# QOPS-P2: coherent operation and native preparation, readout and records in one model

**Standing. WIP / UNVERIFIED.** Writer's research record for the P1 thread on native physical
mechanisms. It contains paper proof exploration and paper readings only, and it has not been
independently reviewed. It runs no computation and adopts no physical assumption. It edits no
manuscript, Lean module or registry. The decisive computations are written as preregistrations in
`PREREG.md`, and none has been run.

- **Authorization.** Owner `amaybaum`:
  - [#1169 c.7064767045](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064767045)
    makes the "Native physical mechanisms" thread P1 and authorizes research, proof exploration,
    planning and preregistration;
  - [#1169 c.7064843184](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064843184)
    adds the (N)/(I) requirement;
  - [#1169 c.7064859041](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064859041)
    sets O1 (a physical source of coherent operations) as the highest priority, with O3 (native
    preparation, readout, records and access closure) alongside it, assessed in one model. It
    approves U3 (the paper reading for T3 and T7) and U4 (the T1 preregistration), but not the T1
    computation.

  Computational experiments, CI dispatches, manuscript changes, merges and the adoption of new
  premises are not authorized.
- **Revision.** Independent non-author review at `4aea2dd0`: REVISE (minor)
  ([#1501 c.7064987170](https://github.com/amaybaum/incompleteness/pull/1501#issuecomment-7064987170)).
  R1, R2 and n1–n6 are answered in appended commits. The changes to the frozen plan are in
  `amendments/A01-t1a-pc-rules.md`, and `PREREG.md` itself is unchanged.
- **Goal link (§A.47).** This record serves #1169's target, `QM ⊆ OI + E`. For O1 and O3 it
  decides which members of `E` the native dynamics derives, which it imports, and where the
  earliest unsupported link lies. It does not decide whether any physical mechanism holds.
- **Accountable Issue.** #1490. The predecessor is #1491, QOPS scoping (`QS`), CONFIRMED WITH NITS
  at `f84bd746` with its nits applied at `88b21a32`. #1491 stays as reviewed. This branch is
  stacked on `88b21a32`.
- **Line numbers.** Corpus line numbers are at `main` `df6da1c6101e811acdc7952d5748aff57028e8ed`;
  `88b21a32` changes nothing outside its record directory. Lean paths are relative to
  `verification/lean-mathlib/`. `QS` is
  `verification/programmes/oi-qm/reconstruction/qops-scoping-20261121/NOTE.md`.

**Labels.**
- *Results* are labelled by the owner's two classes:
  - **(N)** is a theorem proved from OI's native assumptions. Native assumptions are the substratum
    rule (finite alphabet, bijective second-order update, the stated member) and the ledger's
    posits; a posit used is named.
  - **(I)** is a conditional theorem that needs imported quantum or operational assumptions. Each
    import is named from the list below.
- *Verification layer* is marked separately: [K] for a Lean declaration on `main`, cited and not
  rebuilt; [P] for a manuscript statement; [R] for a research record; [W] for a proof in this
  note, unreviewed and not kernel-checked; [LIT2] for literature from memory, used as background.

**Named imports and inputs.** Two of the items below are not quantum imports, but they are inputs
that the native dynamics does not supply: RES is an input on the law, and FB is a modelling
choice. They are named so that every dependency is visible.

| Code | Import or input | Where the corpus states it |
|---|---|---|
| KIN | complex matrix kinematics on configuration carriers, and coherent states as physical states | `Main:572` ("a kinematics whose derivation from operational premises is open"), `Main:218` |
| FLOW | the continuous layer flow `unit g t` of a native involution is physically executable at intermediate `t` (H-QOPS-G) | not supplied: `GR:269`; `LiftAudit.lean:200` |
| PH | the phase intervention | an assumption on the class: `GR:267` |
| READ | the native readout rule (rule (e) of `FiniteOperationalTheory`) | a field of the structure: `OperationalAssembly.lean:594` |
| LT | local tomography, or tensor-product composite kinematics | the premise field `lt`: `CompositeInterface.lean`; `Main:218` |
| RES | a non-uniform reservoir law: μ-R, a boundary law, NEQ-T or NEQ-O, or a small actual orbit under μ-O | ledger posits or contingent facts; PR1 (`RC/prep-regress-1-20261119/RESULT.md:70`) |
| PROD | a product initial state of register and environment | a hypothesis of the dilation constructions (`Main:318`, "initially uncorrelated") |
| FB | a frozen uniform boundary around a finite region | a modelling choice of T1 (QS §3.1) |

***

## 0. Answers to the three questions

### 0.1 Established

| # | Result | Class | Layer |
|---|---|---|---|
| E1 | **Lemma P1.** The flows of permutation involutions annihilate every orbit indicator `1_O`, and their real Lie algebra lies in `⊕_O u(W_O)`, where `W_O = 1_O^⊥ ∩ ℂ^O` | (I): KIN, FLOW. The algebra statement itself is plain matrix algebra | W |
| E2 | **Lemma P2.** For single transpositions whose graph is connected on `O`, the algebra on `ℂ^O` is all of `u(W_O)` | (I): KIN, FLOW | W |
| E3 | **Corollary P3.** No transition drive `iX_ab` is in any such flow algebra. The phase is what supplies it in the kernel's exact route (`DerivedQ3.lean:81`) | (I): KIN, FLOW | W, with [K] cited |
| E4 | **Lemma P4.** For U₂ on a frozen uniform boundary: a site's shear gate is trivial unless the site has at least two neighbours in the region, a site with a trivial shear gate conserves its local weight, and orbits have size at most `2^a 4^b`. The line of three gives `X, X, SWAP, CCX` on a 16-point orbit | (N), with FB. These are statements about permutations | W |
| E5 | **Lemma P5.** Take a reversible map of register × environment from a product initial law. A uniform environment gives a doubly stochastic (unital) register map. The entropy removed from the register is at most `log|H| − S(σ)`. Initial register–environment correlation is outside its scope | classical form (N), with PROD; coherent form (I): KIN, PROD | W |
| E6 | **Proposition J1 (joint O1 ∧ O3).** Under FLOW, a register prepared in a configuration `x ∈ O` keeps the component `1_O/√|O|` under every flow word. Every state reachable from `x` has fidelity at most `1 − 1/|O|` with every unit vector of `W_O`. The bound depends on `|O|` itself, and is attained only where there is control on `W_O`. It concerns flow words on the register alone, not ancilla-assisted preparation | (I): KIN, FLOW | W |
| E7 | **U3, reading for T3.** The corpus's effective channels are unital in both constructions stated with a uniform environment: the frozen-bath mixture of conditioned unitaries (`Main:346`), and the linear member's Weyl-mixture normal form (`Main:306–318`). The bath-motion correction's unitality is not stated | reading of (P) theorems; L₂'s normal form is (N) with PROD and μ-G-type uniform hidden law, at the representation level (KIN for coherent inputs) | P, W |
| E8 | **U3, reading for T7.** No locality decomposition or per-location norm is stated for the frozen-bath term. The corpus states none for L₂ either, so under QS's T7 rule the decision is **absent** throughout. A candidate reading [W], inferred from `Main:300` and `Main:306–310` and not stated there, is recorded beside it. For L₂ at one step the noise acts only near the region's boundary, and the error distribution is uniform over the Weyl group `G`. That keeps every Weyl operator commuting with all of `G` and erases every other one. It is a full-strength error distribution, not weak noise | decision: absent. The candidate reading would be (N) for L₂ with PROD and a uniform hidden law | P, W |
| E9 | **Composition.** The configuration carrier factorizes over sites, and causal cones are exact. COMP-1's laws hold given a pre-composite. Under FLOW, uncoupled regions compose encoded constituents by the tensor product | (N) for the site factorization and cones; (I) LT for COMP-1's composite; (I) KIN, FLOW for the encoded remark | P, K, W |

### 0.2 Assumed (where each import enters)

- **KIN.** It enters wherever a coherent state or a matrix-valued operation is a physical object:
  E1–E3, E6, and the coherent form of E5. It is the earliest import in every O1 chain (§4).
- **FLOW.** It enters at the first coherent operation: E1–E3, E6, and the encoded part of E9. In
  Lean it is the hypothesis `LayerFlowExecutable T σ` of `derivedOI_qm_iff_layerFlowExecutable'`
  (`DerivedQ3.lean:222`).
- **PH.** No result here uses it. E3 shows what it does in the exact route.
- **READ.** It enters every readout in O3 (§3). It is a structure field, not a theorem.
- **LT.** It enters only COMP-1's composite (E9).
- **RES.** It enters every preparation, reset and fresh record cell (§2, §3). By E5, nothing below
  works without it.
- **PROD.** It enters E5, E7 and E8.
- **FB.** It enters E4 and T1.

### 0.3 Missing (the earliest unsupported step)

- **O1.**
  - The earliest import is KIN: the corpus takes complex kinematics as given. Deriving it is
    *mathematics plus a physical identification*.
  - The earliest unsupported physical step is FLOW: an executable non-monomial operation. It needs
    a **physical mechanism**, because the stated dynamics provably does not supply one
    (`LiftAudit.lean:200`, `GR:269`).
  - Given FLOW, what remains is *mathematics*: the linking question for native gates (§1.4, P-A)
    and Lie-rank reachability on an invariant subspace, which is not in the kernel.
- **O3.**
  - The earliest unsupported step is a native producer of ready (known-state) cells. That is a
    preparation and reset resource, and it needs a **physical input**, RES. By E5 and PR1 it
    cannot come from the dynamics under a uniform law. This matches the record that "the first
    missing operation is a native producer of the joint ready precursor"
    (`RC/repeatable-measurement-feasibility-20261118/DECISION.md:3`).
  - Above it are READ, a supplied rule, and a localized, re-armable record: a **physical
    mechanism** on Q (MEAS-Q AW-MQ-2; QS H-QOPS-M).
- **Joint.** One model needs FLOW, RES, READ and a latch on the same rule at once. E6 adds a
  quantitative link. Without PH, preparation fidelity from configurations, by flow words on the
  register alone, is capped at `1 − 1/|O|`. The cap tends to 1 iff the absolute size of the
  largest orbit grows with the region. The fraction `|O|/N` does not matter. So O1's absolute
  orbit growth (T1a, as amended in A01) and control on `W_O` (T1b) decide whether O3's
  preparation can be made accurate.

**Scalability safeguard.** E1–E6 are stated for every finite region and every orbit, on one rule:
the same `F` and the same gates at every size. E4 and T1 use FB, which is a per-region modelling
choice and not a native interface. A construction that meets the safeguard would have to replace FB
with the native dynamics outside the region. That is not done here.

***

## 1. O1: coherent operations from layer flows without the phase

### 1.1 Setting

- `Ω` is a finite configuration set and `{P_g}` a set of permutation involutions of `Ω`.
- `π_g = (1 − P_g)/2` is a real symmetric projector, `X_g = iπ_g`, and the flow is
  `unit g t = exp(iπt·π_g)` (`SecondOrderCircuit.lean:356`).
- The flow has period 2, `unit g 2 = 1`, since `e^{2πi} = 1`. Flows at nonnegative times therefore
  include inverses.
- `𝔏 = Lie_ℝ⟨X_g⟩`. `G = ⟨P_g⟩`, with orbits `O` and indicators `1_O`.
- `W_O = 1_O^⊥ ∩ ℂ^O`.

### 1.2 Results (each (I): KIN, FLOW) [W]

**Lemma P1.** `𝔏 ⊆ ⊕_O u(W_O)`, acting as zero on every `1_O`.

*Proof.* Each `P_g` permutes each orbit, so it preserves `ℂ^O`, and `P_g 1_O = 1_O`. Hence
`π_g 1_O = 0`. `X_g` therefore preserves each `ℂ^O`, annihilates `1_O`, and, being
anti-Hermitian, preserves `W_O`. These properties are closed under real linear combination and
commutator. ∎

**Lemma P2.** Let `T` be a set of transpositions and `O` a connected component of the graph with
edge set `T`. Then `𝔏|_{ℂ^O} = u(W_O)`, of dimension `(|O| − 1)²`. If every element of `T` is a
single transposition, `𝔏 = ⊕_O u(W_O)`.

*Proof.* For `τ = (ab)`, `π_τ = v vᵀ/2` with `v = e_a − e_b`. The proof is by induction along an
ordering of a spanning tree of `O`, adding one leaf at a time.
- *Base.* One edge: `W = span(v)`, and `ℝ X_τ = u(W)`.
- *Step.* Suppose `u(W) ⊆ 𝔏` for the current vertex set `O'`, with `W = W_{O'}`. Add the leaf `c`
  joined to `b ∈ O'`, and let `v = e_b − e_c`.
  - Write `v = w₀ + αu`, with `u` the unit vector of `W_{O'∪{c}}` orthogonal to `W`. Then
    `w₀ ≠ 0`: it is the projection of `e_b` onto `W`, and `|O'| ≥ 2`. Also `α ≠ 0`.
  - For Hermitian `H` on `W`, `[X_v, iH] = −[v v†, H]/2`. Its block between `u` and `W` is
    `−(α u (Hw₀)† − ᾱ (Hw₀) u†)/2`.
  - Since `w₀ ≠ 0`, `{Hw₀ : H Hermitian on W}` is a real hyperplane of `W`, because
    `⟨w₀, Hw₀⟩` is real. It contains `w₀` (take `H = 1_W`) but not `i·w₀`. The bracket with
    `i·1_W ∈ u(W)` sends the block `x u† − u x†` to `(ix) u† − u (ix)†`, which supplies the missing
    direction. So these brackets give every anti-Hermitian operator coupling `u` to `W`.
  - With `u(W)` they generate `su(W_{O'∪{c}}) ⊕ ℝ·i1_W`, which is `u(W_{O'∪{c}})`.
  - P1 gives `⊆`.

Generators supported on different components act on orthogonal blocks and commute, so the algebra
is the direct sum. ∎

**Corollary P3.** For `a ≠ b` in `O`, `iX_ab = i(|a⟩⟨b| + |b⟩⟨a|) ∉ 𝔏`, since
`X_ab 1_O = e_a + e_b ≠ 0`. So the driven transition of phase-free richness
(`MinimalRepertoire.lean:423`) is never supplied by flows and exchanges alone.
`gateFlow_isolation_flip` (`DerivedQ3.lean:81`) gets the transition flow on one pair from the gate
flow, its time reversal and the sign flip, and the sign flip does two jobs there:
- it cancels the scalar `(i/2)1_{ab}`;
- it cancels the flow on every other moved pair.

Without PH the first job is impossible on `ℂ^O` (P1). Inside `W_O` it is not needed.

**Corollary (encoded control).** Suppose some unlinked irreducible constituent `V` has
`𝔏|_V ⊇ su(V)`. Then positive words of flows reach every unitary on `V`, up to a phase on `V`.
This rests on a Lie-rank reachability theorem restricted to an invariant subspace, which is not in
the kernel (§1.5). It covers real-amplitude control, since `so(V) ⊆ su(V)`. P2 supplies such a
`V = W_O` for transposition gate sets, but not for native gates.

### 1.3 Native gates of U₂ on small regions, (N) with FB [W]

**Lemma P4.** Take U₂ (`q = 2`), a region `R`, a frozen uniform boundary `c ∈ {0, 1}`, and let
`m_i` be the number of neighbours of `i` inside `R`.
1. `shear_i` is the identity unless `m_i ≥ 2`. Otherwise it is a NOT on `p_i`, conditioned on a
   Boolean function of the interior neighbours' current values.
2. If `shear_i` is trivial, `w_i = p_i + c_i` is invariant under every native gate of `R`.
3. Every orbit has size at most `2^a 4^b`, where `a` is the number of trivial shear gates and `b`
   the number of nontrivial ones.
4. On the line of three `l, m, r`, the gates are `SWAP_l, SWAP_m, SWAP_r` and the Toffoli gate
   `(c_l, c_r) → p_m`, with both controls negated at `c = 1`. The largest orbit (`w_l = w_r = 1`)
   has 16 points, and on it the gates act as `X_a, X_b, SWAP_{p_m c_m}, CCX_{ab→p_m}`.

*Proof.*
1. At `q = 2` the shear step is `p_i ↦ F(Σ) + p_i`, with `F(Σ) = ⌊(Σ+1)/3⌋ mod 2`. For
   `Σ = 0, …, 6`, `F` takes the values `0, 0, 1, 1, 1, 0, 0`. This agrees with NU at `2572854b`
   ("flip iff the neighbour sum is 2, 3 or 4"). With `Σ = (6 − m_i)c + s` and `0 ≤ s ≤ m_i`:
   - for `c = 0`, `Σ ≤ m_i`;
   - for `c = 1`, `Σ ∈ [6 − m_i, 6]`.

   Either range meets `{2, 3, 4}` iff `m_i ≥ 2`.
2. `SWAP_i` preserves `w_i`, and `shear_j` writes only `p_j`.
3. This follows from item 2.
4. The middle site has `m = 2`; at `c = 0` it flips iff `c_l = c_r = 1`, and at `c = 1` iff both
   are 0. On `w = 1`, `SWAP` acts as `X` on `{01, 10}`.

Both uniform backgrounds are fixed points at `q = 2`. ∎

### 1.4 The gap for native gates: linking of copies

A native involution is a product of disjoint transpositions, so `π_g` is a sum of commuting rank-one
projectors. On the 16-point orbit of P4(4), for example, `X_a`'s generator acts identically on 8
copies. P2 does not apply. Whether the other generators separate the copies is the constituent
question. It is *mathematics*, preregistered as P-A (`PREREG.md`), and it is not run. BQ's reviewed
saturation results for hand-chosen gates show only that saturation is generic, which is why P-A
measures orbit scaling and constituent structure, not saturation (QS §3.1).

### 1.5 The Lean statements relied on, and the missing interfaces

| Use | Statement | Standing |
|---|---|---|
| native gates are commuting involutions | `SecondOrderCircuit.lean:313` `depth_two_circuit` | [K], (N) |
| the flow: group law, unitarity, commutation | `SecondOrderCircuit.lean:356`, `:377`, `:392`, `:427`, `:496`; `:800` `quasilocal_drive` | [K], algebra only. `unit g 2 = 1` follows from `:392` and is not stated |
| the all-ones case of P1 | `InstrumentRealization.lean:180` `OnesFixing`, `:398` | [K] |
| the quarter phase is lost for ones-fixing classes | `PhaseSource.lean:55` | [K] |
| the Lie algebra lies in `u(D)` | `ControlLie.lean:216` | [K] |
| Lie rank gives reachability on the full carrier | `OrbitReachability.lean:631`, `PositiveReachability.lean:996`, `MicroscopicReversibility.lean:114` | [K]; full carrier only |
| transport by permutations, and brackets of drives | `MinimalRepertoire.lean:156`, `:56`; `LieRankSource.lean:199` | [K] |
| the role of the phase | `DerivedQ3.lean:81`, `:222` (hypotheses `DerivedOI T`, which includes `PhasesAvailable`, and `LayerFlowExecutable T σ`) | [K] |
| the monomial no-go, with phases | `LiftAudit.lean:200`; `RouteB.lean:297` | [K], (N) |

Interfaces between the conditional Lean results and the missing witnesses. These are for the Lean
thread, as designs only:
1. P1 in per-orbit form, generalizing `OnesFixing`.
2. P2, transposition graphs.
3. Lie-rank reachability on an invariant subspace.
4. A predicate `FlowExecutable` for a *native* gate (not an arbitrary involution), separate from
   `DerivedOI`, so that a phase-free encoded route can be stated with FLOW as its only physical
   hypothesis.

***

## 2. O3 resources: entropy removal (AW-QOPS-2) and the U3 readings

**Lemma P5 [W].** Let the register `X` and environment `H` be finite, let `U` be a reversible map
of `X × H` (a permutation unitary for the native step), and let the initial law be the product
`ρ ⊗ σ` (PROD).
1. If `σ` is uniform, the register map is doubly stochastic in the classical form, and unital in
   the coherent form: `Φ(1/|X|) = Tr_H[U(1/(|X||H|))U†] = 1/|X|`.
2. The entropy removed from the register satisfies `S(ρ) − S(X_T) ≤ S(H_T) − S(σ) ≤ log|H| − S(σ)`,
   by conservation of joint entropy and subadditivity (Shannon or von Neumann).

*Scope, including the excluded escape.* Initial correlation between register and environment is
**outside P5's scope**. Without PROD the same argument gives `S(ρ) − S(X_T) ≤ log|H| − S(σ) + I(X:H)₀`,
so initial mutual information is a third resource beside fresh supply and non-unital noise. Under
the uniform counting law on a finite product configuration set, PROD holds automatically, because
the uniform law on `X × H` is the product of the uniform laws. That strengthens the (N) reading
there.

The classical form is (N) with PROD; the coherent form is (I) with KIN and PROD.

**Classification of entropy removal.** It is **not derivable from the native dynamics alone**.
This is stated for product initial laws and finite environments, and P5 is the obstruction. It is
**conditional on RES**: some non-uniform reservoir, whose deficit `log|H| − S(σ)` bounds all
removal, whether by fresh supply (S1) or by non-unital noise (S2). Under the uniform counting law
neither exists in law, and only conditioning, at a cost of `log₂ 1/μ(E)` (PR1), remains. With A1
open and the environment not finite, `log|H|` gives no bound, and an incoming stream is PR1's
escape. P5 refines PR1 Node 1 and AW-QOPS-2. Whatever RES may be, it is an input.

**U3: reading for T3 (is the effective channel unital?).**
- *Frozen-bath term* (`Main:346`). The text describes it as "a mixture over the bath ensemble of
  bath-conditioned visible unitaries". A mixture of unitaries is unital, so this term is unital.
- *Linear member L₂ with an uncorrelated, maximally mixed hidden sector* (`Main:306–318`). The
  visible channel is `Ad_{V_A} ∘ Φ_G`, a Clifford permutation conjugate of a uniform Weyl mixture.
  It is unital, consistent with P5(1).
- *Diagonal preservation* (`Main:328`). Permutation dilations with a diagonal `μ_H` preserve
  diagonal states; this is the classical form.
- *Bath-motion correction* (`Main:346`, order `(τ_S/τ_B)²`). Its unitality is not stated.
- *Decision under QS's T3 rule.*
  - The ABIN-form conditional is **not established**. ABIN's i.i.d. per-wire noise has no
    counterpart for OI's quasi-static, correlated `𝒟` (`Comp:142`).
  - BGH's escape S2 is **not available** in the two constructions that have a uniform environment,
    since both are unital.
  - P5 replaces the noise-model-dependent mapping with a statement that holds for every noise
    model in the class: removal is bounded by the reservoir deficit.

**U3: reading for T7 (locality and per-location norm).**
- *Frozen-bath term.* Its spread is "of order `‖V_int‖²`", and "its magnitude for the cosmological
  partition awaits the substratum interaction structure" (`Main:346`). No locality decomposition
  and no per-location norm are stated: **absent**, which agrees with `Comp:142`.
- *L₂ at one step.* Lemma 1 (`Main:300`) factors the cross-blocks through boundary coordinates.
  The Weyl group `G` of Lemma 2 is generated by translations in `im(A^{-1}B)` and phases in
  `im Cᵀ`. The reading [W], inferred here and not stated in the corpus, is that the noise acts only
  near the region's boundary: within one site of the inner boundary, because `A^{-1}` is one-step
  local. `Φ_G` keeps every Weyl operator that commutes with all of `G`, including the elements of
  `G` itself, and erases every one that does not. The error distribution is uniform over
  `g ∈ G`, so it has full strength and is not a weak-noise model.
  - Corollary 2 (`Main:320`) gives a non-entanglement-breaking channel when the block has a bulk
    (side `ℓ ≥ 3` in `d = 3`, `Main:324`).
  - Multi-step behaviour is not derived here. Each step admits the environment one more layer,
    which suggests that an unshielded register shrinks at the light-cone speed. Without a reservoir
    this does not fit a fault-tolerance threshold model. This is a reading, (N) with PROD and a
    uniform hidden law for one step, and not shown beyond that.
- *Decision under QS's T7 rule* ("supplied if both are stated with a derivation"): **absent**, for
  L₂, for Q and for the general frozen-bath term. The L₂ locality reading above is a [W] candidate
  recorded beside the decision. It would become "supplied" only if a derivation of it were reviewed
  and stated.

***

## 3. O3: preparation, readout, records and access closure

| Step | What the native dynamics gives | Class | Missing |
|---|---|---|---|
| Ready cell (a known-state cell, for preparation, a fresh ancilla or a record slot) | Under a uniform law, no net supply in a fixed block (PR1 Node 1, reviewed); P5's deficit bound | (N) for the obstruction (PR1 [R]; P5 [W]) | RES: a physical input |
| Copy into a record cell | the native shear gate is a conditional NOT. With all but one control fixed, it is a copy at the configuration level (P4) | (N) as a permutation | selective application, which is control; NU's question for Q |
| Readout | the readout rule (e), with Lüders branches derived from the rule (`OperationalAssembly.lean:658`) | (I): READ | a native readout mechanism |
| Persistence and re-arm | C2-structural persistence (`Main:80`), (N). No localized, re-armable record in MEAS-Q's searched classes (AW-MQ-2) | (N) for C2; bounded negatives [R] | a latch, the bounded-breach node shared with NU (QS H-QOPS-M) |
| Re-arm cost | re-arming erases the previous record into the environment, which by P5 uses deficit unless the record is uncomputed. PR1: retained results keep their budget committed | (N) [R, W] | RES |
| Access closure | the observer's record is a configuration of its own cells, so access reduces to the rows above: a copy at a chosen time, a ready cell and persistence | reduction [W] | as above |

The **earliest O3 step that lacks support** is the ready cell. It needs RES, a physical input, and
mathematics cannot supply it under the class of P5.

***

## 4. O1 and O3 in one model

**The candidate model, M.**
- The native rule (U₂ or Q, with L₂ as a comparison), on one lattice and with no frozen boundary
  in the physical statement.
- FLOW for its native gates, for coherent operation (O1).
- RES, for ready cells (O3: preparation, fresh ancillas and re-arm).
- READ, for readout.
- A latch, for persistence.
- No PH.

**Assessment of M as a whole [W].**
1. *Preparation and coherent operation interact.* Native preparation gives configurations `x`, by
   RES and copy. Under FLOW, Proposition J1 holds.

   **Proposition J1.** Every state reachable from `x ∈ O` by flow words has the component
   `⟨1_O/√|O|, ·⟩ = 1/√|O|`. Its fidelity with any unit vector of `W_O` is at most `1 − 1/|O|`.

   *Proof.* Lemma P1 fixes the `1_O` component. ∎

   *Tightness and scope.*
   - The bound is attained only if the `W_O` part can be steered onto the target. That needs
     control on `W_O`, as P2 gives for transposition gate sets or T1b-S would give for native
     gates.
   - The bound concerns flow words acting on the register alone. With an ancilla, the relevant
     orbit is the joint orbit, and the reduced register state is not covered.

   So, without PH, the accuracy of preparation from configurations by flow words on the register
   is bounded by `1 − 1/|O|`. The bound depends on the absolute orbit size, and tends to 1 iff the
   largest orbit grows with the region. Whether native gate orbits grow is P-A's T1a, as amended
   in A01.
2. *Readout of an encoded result* uses flows followed by configuration readout (READ). The
   indicator component of J1 carries weight `1/|O|` in every reachable state. The trace distance
   from every encoded state is therefore at least `1/√|O|`. Given control on `W_O`, it is exactly
   `1/√|O|` for the target along the `W_O` part, and that bounds the distortion of readout
   statistics in total variation by `1/√|O|` for that target. It does not bound it for other
   targets.
3. *Fault tolerance in M* needs entropy removal at a positive rate. By P5 it draws on RES. By the
   T3 reading, the corpus's uniform-environment channels are unital, so the BGH escape needs RES as
   well. On the [W] candidate reading for L₂, which T7 does not supply, the error distribution at a region's boundary is uniform over `G`, at full strength rather than weak.
4. *Control*, meaning when gates, copies and reads happen, is NU's question for Q or a supplied
   program register (QS H-QOPS-C).

**Verdict for M.** M is a single model in which O1 and O3 are assessed together. Every coherent
operation in it is (I), importing KIN and FLOW, and every O3 step past the copy needs RES, READ or
a latch. No member of `E` among these is derived. Two links in M are *mathematics*, and both are
preregistered: orbit scaling and the linking of copies. Two are *physical mechanisms*: FLOW and
RES. The latch is also a physical mechanism, but one that could exist inside the native rule. So
it is a question about Q, not a new input.

***

## 5. Composition

| Item | Statement | Site | Class | Layer |
|---|---|---|---|---|
| CP1 | The configuration set is a product over sites, so its configuration space factorizes over sites | ledger (viii)–(xiii) (`Main:736` per QS); POSIT-MIN records site factorization as presupposed (`verification/audits/foundations/posit-min-20261120/AUDIT.md:27`) | (N), definitional, given site factorization | P |
| CP2 | Exact causal cones | `Main:662` | (N) | P |
| CP3 | Kinematic locality does not prove local tomography, statistical product structure after conditioning, or one common tensor-product instrument category | `Main:218`, `Main:662` | absent as a derivation | P |
| CP4 | COMP-1: attachment, discard, joint reversible action, sharp readout and no-signalling on products, given a pre-composite; local tomography is a premise field | `CompositeInterface.lean:926` `comp1_core`; `RC/round-comp-1-composite-interface/result.md` | (I): LT, with the composite structure supplied | K, R |
| CP5 | Inert spectators and iterated composition are among the completion conditions; the tensor-product kinematics is taken as given | `Main:362`, `:572`; `GeneralCarrier.lean:100` | (I): KIN, LT | K, P |
| CP6 | Embedded observation gives iterated composition and trivial-ancilla consistency; bare OI does not supply it | `EmbeddedObservation.lean` header; `GR:253` | (I): the embedded-observation principle | K |
| CP7 | A typed theory's endomorphic shadow is an embedded-observation family | `TypedCompletion.lean` (`shadow_embeddedObservation`) | (I): a typed operational theory | K |
| CP8 | The native gate theorem on two balls takes one common NOT on both factors (identical-copy covariance) as a premise | `NativeGateBall.lean` and `CompositeDimension.lean` headers | (I): identical-copy covariance | K (core) |
| CP9 | For L₂ with a maximally mixed uncorrelated environment, the one-step visible channel is a Clifford-conjugated Weyl mixture. It is not entanglement-breaking when the region has a bulk | `Main:306–324` | (N) with PROD and a uniform hidden law, at the representation level; coherent inputs need KIN | P |
| CP10 | CHSH ≤ 2 under wing-local interventions and setting independence; exceeding it needs H-Bell | `Main:20`, `Main:662` | (N) bound; H-Bell open | P |
| CP11 | Under FLOW, regions with no gate reading across the cut have `G = G₁ × G₂`. Their orbits are products, and `V₁ ⊗ V₂` is invariant | this note | (I): KIN, FLOW | W |

**The composition gap.**
- *At the substratum level*, tensor structure and causal separation are (N) (CP1, CP2).
- *For visible composites*, it is imported (LT, KIN) or absent (CP3, CP5, CP8).
- *For encoded registers under FLOW*, it is derived for uncoupled regions (CP11). It is open
  across a coupling gate, which may mix `V₁ ⊗ V₂` with indicator directions. That is
  preregistered as P-C, a mathematics question.
- CP9 is the corpus's one native statement about a composite with a reference system:
  entanglement survives a single step for a region with a bulk.

***

## 6. Pressure test (§A.31) and proposed classification

1. *P2 is favourable and narrow.* It covers single transpositions, which are not native gates. Its
   use is to locate the phase's role and the linking gap, not to support universality.
2. *J1 is unfavourable to the phase-free route only at small orbits.* It is favourable if orbits
   grow, and that is exactly what P-A tests. It is not read as either outcome here.
3. *P5 is elementary.* Its value is the classification it supports: RES is an input. Its class is a
   product initial law and a finite environment.
4. *The T7 reading for L₂* holds at one step only. The multi-step "light-cone shrinkage" is a
   suggestion, not a result.
5. *M assembles imports.* It shows what one model needs; it is not a proposal to adopt them.

| Item | Proposed class (§A.31) |
|---|---|
| P1 | ELABORATING |
| P2, P3 | NEW (candidate) |
| P4 | NEW, minor (a design input for T1) |
| P5 | ELABORATING (refines PR1) |
| J1 | NEW (candidate): it couples O1's absolute orbit growth to O3's preparation accuracy |
| U3 readings | CONFIRMING (T3); T7 absent, with an ELABORATING [W] candidate for L₂ |
| §5 | CONFIRMING collation, plus CP11 |

**Fixed point.** One pass. Not reached.

***

## 7. What review must check

- The proofs of P1, P2 (`w₀ ≠ 0`, and the block-generation step), P4 (the table of `F` and the
  `m_i ≥ 2` criterion), P5 and J1.
- That P3's reading matches `DerivedQ3.lean:81`.
- That the U3 readings quote `Main:300–328` and `Main:346` at their standing. The T7 reading for
  L₂ (noise within one site of the boundary, with errors uniform over `G`) is an inference from
  Lemma 1 and Lemma 2, not a manuscript statement. T7 is therefore decided as absent.
- Each (N)/(I) label and its import list.
- That the "not in the kernel" interfaces of §1.5 are absent from `OIBridge/`.
- That `PREREG.md` contains rules only, with no outcomes.
