# Thread I — the F2 sufficiency target: one finite statement, its hypotheses, gap map and redundancies

**Base.** M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. Kernel `file:line` references were read in the detached
worktree `scratchpad/threads/wt-I` at M. Paths are under `verification/lean-mathlib/OIBridge/` unless another path
is given. Lean was not compiled here, no computation was run, nothing was pushed, and nothing in
`/home/user/incompleteness` was touched.

**Other sources, cited by exact object.**

- *Step-4 pair interface* `PairInterfaceDesign.lean` (PID). Compiled at `c9f16498` (blob `0981a3ff`) in run
  38606560943, job 115998853118, with 27 standard reports. The run is recorded in `statement.md` at `46ade360`
  :7–9, and the blob is unchanged at `46ade360`.
- *Relative-gate design* `RelativeGateTransport.lean`. Compiled at `c9f16498` in run 38606561330, recorded in
  `relative-gate-design/result.md` at `46ade360` :12–15.
- *KN-DESC design* `KnDescentDesign.lean` at `d3a95be6`. Runs 38457070337 and 38597304093 (C:153–167).
- *The F2 row as committed* on the session branch in `fe5c7fb5` (single parent M, not on main):
  - ROADMAP :69 and :1117–1135;
  - PROGRAMME :40, :521 and :537.
- *Thread drafts.* They are cited as A:line … G:line. The step-4 record is cited as SM:line, meaning
  `pair-interface-design/statement.md` at `46ade360`.

**Provenance note.** During this thread `origin/ccr-ac945020-v97mrh` moved from the design head `46ade360` to
`fe5c7fb5`, the F1-retirement commit. This was the other writer. The design commits are still reachable and are
cited by id. My worktree is clean at M.

**Labels.**

- **[K]** a kernel declaration at M. **[K-inst]** a one- or two-line composition of [K] declarations that is not
  itself a named theorem.
- **[D]** compiled design, at the commit and run stated.
- **[W]** a written argument, either in the cited draft or mine where marked.
- **[X]** an exact computation, where it lives.
- **[L]** literature. **[U]** unsourced.

Status words follow A:14–19: *derived*, *conditional*, *introduced*, *no predicate*. I add *free* for a fact that
needs no premise.

This is research only. It changes no status and proposes no manuscript text. Correctness bands are unchanged: this is
consistency-axis work.

***

## 0. Answer in brief

1. **The target has one statement, F2-fin(X)** (§1.3):

   > `OIStated ℛ ∧ Origin ℛ ε 𝔒 ∧ X ℛ ε 𝔒 ∧ Res ε 𝔒 ⟹ QMfin 𝔒`

   - X is a placeholder.
   - X enters only through its obligation R_X (§1.4). R_X is the set of table rows that need an operation
     outside `NonnegBounded`, plus the two rows the F2 row assigns to the extension.
   - `X ⊢ R_X` is the extension's own theorem. It is not part of this target.
2. **The conclusion QMfin is fixed** (§1.2). It is finite, typed exact QM (`ShadowQuantum`) with:
   - normalized states and probabilities;
   - available tests *defined* as the closure of the stage tests (`availOf`), not a free `avail`;
   - every finite product of types;
   - any finite local dimension;
   - n-party correlations equal to C_q.
3. **The matrix core is already in the kernel at M. None of threads A–G cites it.**
   - `sourcedOI_qm_iff_phaseFree` (SubstratumInterfaceAudit.lean:654) [K]: for any theory with `SourcedOI`, exact
     finite QM holds iff one pair of states is continuously driven at every level. No phase premise is needed.
   - `permTheory_sourcedOI` (:660) and `permTheory_not_phaseFree` (:711) [K]: OI's sourced theory has `SourcedOI`
     and fails the driven pair.
   - `qm_of_mixSourced` (StateMixingCoupling.lean:486) [K] is the class-level form on the two-valued carrier. It
     takes an extension of `permClass` with phases and the state-mixing datum.
   - So at the matrix level, sufficiency and *relative* necessity of the resource are [K]. The open content of
     F2-fin is the identification layer and `X ⊢ R_X`.
4. **R_X has three core rows: I5, H8 and H11b.** They are one resource, continuous coherent control, seen in three
   vocabularies, and no formal map relates them at M (H27 has no predicate).
   - All three cross the barrier: I5 with a [K] witness, H8 and H11b through a dictionary [W from K] (§2).
   - Two more rows are X's scope by the F2 row and do not cross the barrier: H-COMPAT and H22v.
5. **Redundancy** (§4):
   - H23 and H24 are conditional on drivability and compatibility [D].
   - The swap family is OI-sourced (`permClass_permMatrix` :406) as well as redundant by L8.
   - The quarter-phase family is a self-flow at `t = −π/4` [W from D], so `DrivesElementary` reduces to its flow
     conjunct.
   - H7 and H12 have no consumer [K, by grep]. H10 is free on the ball [K]. H13 and H22t follow from `availOf` [W].
6. **The gap map has 15 links** (§3). Γ0–Γ10 and Γ12 are mathematics only; Γ11 and Γ13 carry residuals; Γ14
   needs X. Five links carry the required marks: normalization (Γ6), tests tied to stages (Γ7), k-tokens with KN-DESC (Γ10),
   carriers that are not powers of two (Γ4, Γ11), and correlations at n ≥ 3 (Γ12).
7. **The cheapest next compiled step that does not depend on X** is Γ1 (§3.1). It states the matrix core in
   extension form, with both directions and two controls. Every proof is a composition of landed theorems.
8. **On the necessity side** (§1.6, [W], scoped), leaving `NonnegBounded` is necessary for R_X but not sufficient.
   - A token-level cross-flow together with all permutations fixes the ray of the uniform vector.
   - Real rotations together with `permClass` stay inside the scalar multiples of real matrices.
   - So the phase content is load-bearing in both fragments.

***

## 1. The target

### 1.1 OI as stated, in kernel objects

- **The substrate.**
  - `Substratum` SubstratumInterfaceAudit.lean:60, with the axioms A1 `Finite Conf` :84, A2 :87, A3 :91,
    A4Exact :94, A4 :98 and A5 :102.
  - A6Cov (BackgroundIndependence.lean:131) holds identically: `a6cov_all` :161 [K].
- **The interface.**
  - The sourced class `permClass` :236 (scaled partial permutations).
  - Its four closure clauses: `permClass_arch` :350, `permClass_contextStable` :358, `permClass_labelInvariant`
    :362, `permClass_daggerStable` :366 [K].
  - `permTheory` :606 and `obsTheory 𝒮 := permTheory 𝒮.Conf` :769.
  - `SourcedOI (permTheory A)` :660 [K].
- **The barrier.**
  - `NonnegBounded` FrozenSourcing.lean:65, which every observer theory satisfies: `obsTheory_nonnegBounded` :84 [K].
  - Hence `¬PhasesAvailable` and `¬DerivedOI` at every nonempty carrier (`nonnegBounded_not_phasesAvailable` :99,
    `nonnegBounded_not_derivedOI` :111), and `¬DenseUnitaryControl` on `Fin 2`, where that predicate is stated
    (`nonnegBounded_verdict` :327) [K].
  - The rule adds no availability: `sourcing_rule_independent` :295 [K].
  - Audit text: `verification/programmes/substratum/frozen-sourcing-audit.md` :251–334.
- **The field-neutral stage vocabulary**, which no OI construction instantiates at M:
  - `FiniteStage` KInfFoundations.lean:63, which has `p ∈ [0,1]` and a unit effect with `p unit x = 1`;
  - `DirectedStages` StageCompletion.lean:63, `stageEffects` :176, `body` :141;
  - `CompletionChart` CompletionAction.lean:144 and `chartBody` :166.
  - The only towers at M are the controls `badD` :342, `bitTower` :393 and `midD` CompletionAction.lean:404 (A:329).

### 1.2 The conclusion `QMfin 𝔒`

`𝔒` is an extended observer model (§1.3). `QMfin 𝔒` holds when there is a `TypedOperationalTheory 𝒯`
(TypedCompletion.lean:165) with `𝒯.ShadowQuantum` (:291). By `typed_determined_iff` :850 [K], this means that
`availT S S' (Fin m) F ↔ IsTypedKrausInstrument F` (:448) for all nonempty finite carriers. There must also be a
`StageIso 𝔒 𝒯` (NEW) with the clauses below.

| clause | content |
|---|---|
| **(T1) finite** | each type τ has a nonempty finite carrier `S_τ`; finite outcome sets; finite protocols |
| **(T2) typed** | the observer's available instruments from τ to σ correspond to `𝒯.availT S_τ S_σ`. They are rectangular, normalized (`∑ Kᴴ K = 1`, :448) and between any two types |
| **(T3) composites** | for every finite list τ₁…τₙ the composite type has carrier `≃ Π S_τi`, products go to `ρ ⊗ ρ'` and `E ⊗ E'`, and every system ⊗ ancilla level `S × Fin (k+1)` carries exactly the Kraus instruments (`ExactCompositeQuantumOps` AncillaClosure.lean:364) |
| **(T4) normalized** | `Φ_τ : chartBody (𝔒.C τ) ≃ᵃ {ρ ⪰ 0, tr ρ = 1}`; for every stage i, test e and preparation x, `p e x = re tr(E_e · Φ_τ x)`; `E_unit = 1`; every stage family with `Σ_a p e_a x = 1` goes to a POVM |
| **(T5) tests from stages** | `Φ_τ` carries `availOf (𝔒.D τ) (𝔒.C τ) (𝔒.G τ)` onto `{ρ ↦ re tr(Eρ) : 0 ≤ E ≤ 1}`. `availOf` is the least set that contains the stage tests and the unit, is mixing-closed (EffectSpace.lean:591), and is closed under transport by the observer's reversible maps (G:273–281). It has no other members, and nothing else is called available |
| **(T6) local dimension** | every nonempty finite cardinality occurs as some `card S_τ`. In the register variant F2-reg it is `2^k` only |
| **(Corr)** | for every n, every assignment of types to parties and all finite setting and outcome sets, the behaviours of available protocols equal `C_q(n, (S_τi))`. Q-up and Q-down are separate theorems. Corollaries: NS, LT, and CHSH = 2√2 attained at n = 2 qubits (E:306–336) |

Excluded, as in A:445–464:

- quasilocal and continuum systems (H-∞), and the sets C_qa and C_qc;
- the relative-evolution question P0;
- hidden ontology beyond the origin relation;
- H-Bell, the spatial Bell realization (E:23–59).

The dense variant F2-fin-dense replaces "onto" in (T5) by "onto a dense subset" and `ShadowQuantum` by a density
endpoint. At M a density endpoint exists only on `Fin 2`: `DenseFiniteQM` DiscreteCompletion.lean:59 and
`fixedGateTheory_denseFiniteQM` DenseInstrumentBridge.lean:521 [K].

### 1.3 The statement F2-fin(X), sufficiency only

```lean
import OIBridge   -- aggregate at M. Design objects cited: PID @c9f16498, KnDescentDesign @d3a95be6
open OIBridge SubstratumInterfaceAudit FrozenSourcing ImplementationLocality SubstratumSource
open TypedCompletion StageCompletion CompletionAction OrbitGeneration EffectSpace

structure OIRealization where                       -- NEW packaging (A:136)
  𝒮 : Substratum                                    -- SubstratumInterfaceAudit.lean:60
  [fι : Fintype 𝒮.ι] [fV : Fintype 𝒮.V] [dV : DecidableEq 𝒮.V]
  obs : ObsData 𝒮 ; μ : Ensemble 𝒮                  -- NEW (H0); quantified, never selected

def OIStated (ℛ : OIRealization) : Prop :=           -- the frozen architecture, unchanged
  ℛ.𝒮.A1 ∧ ℛ.𝒮.A2 ∧ ℛ.𝒮.A5 ∧ (∃ D, ℛ.𝒮.A3 D)      -- :84 :87 :102 :91 (A4 as adopted); A6Cov free (:161)

structure Ext (ℛ : OIRealization) where              -- NEW: what an extension adds
  𝓘    : ImplementationClass                         -- ImplementationLocality.lean:244
  arch : Architecture 𝓘                              -- :506
  cons : ∀ (S) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → 𝓘 S K   -- CONS

noncomputable def extTheory (ε : Ext ℛ) (A) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A := genTheory ε.𝓘 ε.arch A          -- :852
-- OI's own observer theory is the instance 𝓘 = permClass at A = 𝒮.Conf (obsTheory, :769)

structure ObserverModel⁺ extends ObserverModel where   -- A's M0 sketch (A:124–134), NEW
  car     : Typ → FinCarrier                          -- S_τ (H-CAR, H26)
  carProd : ∀ τ σ, car (prod τ σ) ≃ car τ × car σ     -- composites (H-CAR)
  G       : ∀ τ, Set ((Fin (C τ).d → ℝ) ≃ᵃ[ℝ] (Fin (C τ).d → ℝ))   -- induced reversible maps (H5, H6)
  -- there is no `avail` field: available tests are defined below

def availOf (D : DirectedStages) (C : CompletionChart D) (G) : Set ((Fin C.d → ℝ) →ᵃ[ℝ] ℝ) :=   -- NEW
  ⋂₀ {F | effR C.L C.p0 '' stageEffects D ⊆ F ∧ unitEff C.d ∈ F ∧ MixingClosed F
          ∧ ∀ g ∈ G, ∀ f ∈ F, seedTransport f g ∈ F}   -- H11a, unit, mixing, H11b

def Origin (ℛ) (ε : Ext ℛ) (𝔒 : ObserverModel⁺) : Prop := …   -- NEW (H0, M1, H27), see below

theorem F2_fin_sufficiency
    (X  : ∀ ℛ, Ext ℛ → ObserverModel⁺ → Prop)        -- the extension principle, a placeholder
    (hX : ∀ ℛ ε 𝔒, X ℛ ε 𝔒 → RX ε 𝔒)                 -- X's obligation; proved per candidate, NOT here
    (ℛ : OIRealization) (ε : Ext ℛ) (𝔒 : ObserverModel⁺)
    (hOI : OIStated ℛ) (hO : Origin ℛ ε 𝔒) (hXε : X ℛ ε 𝔒) (hR : Res ε 𝔒) :
    QMfin 𝔒                                          -- §1.2
```

**`Origin ℛ ε 𝔒`** collects the rows H0, M1 and H27. It states four things:

- the stage tests of `𝔒` are the readouts of finite protocols of ℛ extended by ε, read through `obs` with
  reference ensemble `μ`;
- `𝔒.G τ` contains the chart maps induced by the unitaries of `ε.𝓘` at `S_τ`;
- composite types are products;
- the observer's typed instruments are the attach / protocol / discard words of `extTheory ε`.

It has two instantiations, and they decide the route:

- **Origin_K.** The stage data are field-neutral: a protocol tower whose stage maps are abstract operation data.
  This is the K chain as the assembly route, as the F2 row states (fe5c7fb5 ROADMAP:1130–1132). The complex
  structure first appears at the pair (P10, A:307). §2's table is written for Origin_K.
- **Origin_M.** The stage data are the protocol statistics of `extTheory ε`. The rows H1–H24 then become
  consequences (§4, R14). The complex field is inherited from the stated configuration-level interface, `permTheory`
  over `Matrix Conf Conf ℂ`, rather than derived. In ROADMAP's terms that is the K3 reading (:979), not K.

### 1.4 X's obligation `RX` and the residual `Res`

`RX ε 𝔒` is the conjunction of the rows marked **X** or **X·s** in §2:

- **X-1 = I5′.** Every transition flow is admitted: `∀ S (a b : S) t, ε.𝓘 S (flow (transition a b) t)`, with
  `a = b` allowed. This is the flow conjunct of `DrivesElementary` SubstratumSource.lean:77.
  - By §4 R3–R4 the other two conjuncts follow, given CONS and `Architecture.mul`.
  - Admissible weaker forms, each with its math gap:
    - the theory-level `DrivenPair` at every level and carrier (Γ1, [K] iff);
    - the token-level U(2) flows at `Fin 2` (Γ3, [W+L]).
- **X-2 = H8.** `BoundaryTransitive (chartBody (𝔒.C τ)) (𝔒.G τ)` at elementary τ, or its dense form. This is the
  field-neutral image of X-1.
- **X-3 = content of H11b.** The transporting group in `availOf` is X-2's group. For the exact (T5) it must be
  uncountable (§2, H11b; §5 AW-I2).
- **X-4 = H-COMPAT_k and X-5 = H22v_k.** These are the "compatible state transformations" and "valid measurements"
  that the F2 row places in the extension (fe5c7fb5 ROADMAP:1125–1129). Neither crosses the barrier.

`Res ε 𝔒` is the conjunction of the rows marked **RES**: H1, H2, H4, H5 (form), H14 or H18, H19, H21, H-CAR (pair
and k), H25, H26 (or the F2-reg scope), CL and H27. **OI** rows reach the field-neutral side through H27. **MATH**
and **DEF** rows are not premises.

### 1.5 What the kernel already proves toward it

| form | theorem | scope | directions |
|---|---|---|---|
| theory level, any finite carrier | `sourcedOI_qm_iff_phaseFree` SubstratumInterfaceAudit.lean:654: `SourcedOI T → (ExactAll T ↔ PhaseFreeRichness T)`, with `PhaseFreeRichness` at MinimalRepertoire.lean:423 | relative to `SourcedOI` | both [K]; uses `oiPlusMin_iff_qm` MinimalRepertoire.lean:569 |
| OI's sourced theory | `permTheory_sourcedOI` :660; `permTheory_not_phaseFree` :711; `permTheory_not_qm` :716 | carrier-general | [K] |
| theory level, `Fin 2` | `qm_iff_derivedOI_pairFlowSourced` PairFlowEquivalence.lean:199. Witnesses `derivedOI_pairFlowSourced_of_qm` :93 and `qm_of_derivedOI_pairFlowSourced` :190. Cardinality: `countable_not_pairFlowSourced` :218 | real pair flow plus `DerivedOI` (phases included) | both [K] |
| class level, `Fin 2` | `qm_of_mixSourced` StateMixingCoupling.lean:486 (CL, `permClass ≤ 𝓘`, phases at every level, the mixing datum at every level and angle). Model: `mixTheory_endpoint` :506. Controls: `mixTheoryR_not_qm` :679 (countable angle set) and `mixTheory_empty_not_qm` :689 | two-valued alphabet with ancilla levels | sufficiency [K] |
| class level, any carrier | `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean:136 | all of `DrivesElementary` | sufficiency [K]; matrix converse `qm_generated_by_quantumArchitecture` :161 |

**Skeptical pass on this favourable reading (§A.31).**

1. These theorems state what follows *once* the resource is present. They source nothing.
   - The F2 row says: "Assuming the resource as a premise states it and does not source it" (fe5c7fb5
     ROADMAP:1128–1129).
   - The StateMixingCoupling header says: "the datum is a postulate, and nothing here derives it"
     (StateMixingCoupling.lean:7).
2. Necessity is *relative* to `SourcedOI` or `DerivedOI` and to the generated-theory form. It is not
   "X is necessary for QM".
3. Every form lives on matrix carriers, so none of them touches stage data, (T4)–(T6) or (Corr).
4. `PhaseFreeRichness` asks for a single-pair flow at *every* level `A × Fin n`.
   - `ContextStable` turns a flow on one carrier into `1 ⊗ flow`, which is a product of commuting flows on several
     pairs. It is not a single-pair flow.
   - So a token-level X reaches the theory-level form only through Γ3 and Γ4 [W, mine].
5. The extension form of `SourcedOI` (every closure-respecting extension of `permClass`) is not stated at M. It is
   the proof of :660 with CONS in front of `permClass_permMatrix` (:406) and `permClass_readWrite` (:412) [W]. That
   is Γ1.

### 1.6 Necessity: the separate questions

Each row of §2 carries its own question in column (iv). Three questions are global.

- **N-X (relative necessity of the core resource).**
  - At the theory level the answer is [K]: QM ⟹ `PhaseFreeRichness` (the `.mp` direction of :654), and QM ⟹
    `ElementaryTransitionRichness` (`elementary_of_control` LieRankSource.lean:517 with `physical_of_exactAll`
    PhysicalCharacterization.lean:301).
  - At the field-neutral level the answer is open. Only the elementary instances (A:313–320) and A's M8 exist.
- **N-min (which part of the flow family is load-bearing).** Two scoped observations [W, mine]:
  - **Uniform ray.** Every permutation matrix P has `P u = u`, where u is the uniform vector. Each token-level
    cross-flow is `exp(−itQ)` for a permutation involution Q, and `exp(−itQ) u = e^{−it} u`. So the products of
    permutations and token-level cross-flows fix the ray of u.
    - A single-pair flow on a carrier of size N ≥ 3 sends u to `u + (e^{−it} − 1)(e_a + e_b)/√N`. That vector is off
      the ray for t ∉ 2πℤ. A self-flow on one state also leaves the ray.
    - So the cross-flows of one token alone, with OI's permutations, do not reach `PhaseFreeRichness` by products.
    - Scope: products only. `proj`, `block` and the instrument protocols are not covered. This is the same scope as
      B's L3a(i) (B:229–233), with a different invariant.
  - **Reality.** Every clause of `Architecture` (`one`, `mul`, `smul`, `proj`, `block`), together with
    `ContextStable`, `LabelInvariant` and `DaggerStable`, preserves the set `{c·M : c ∈ ℂ, M real}`. That set
    contains `permClass` and the real rotations `rot θ` (StateMixingCoupling.lean:45). So the closure of the two
    contains no `phaseGate`.
    - This covers the full closure.
    - It is the class-level reason that `qm_of_mixSourced` needs its phase premise `hph`. It also agrees with the
      phase ceiling (`phaseOperator_outside_ceiling` FrozenSourcing.lean:285).
    - No kernel theorem states it.
  - Classification: **NEW**, scoped and uncompiled. Leaving `NonnegBounded` is necessary for R_X and not
    sufficient.
- **N-route.** Under Origin_M, the X·s rows are consequences (unitaries preserve PSD; effects are positive), so
  they are not independent premises. Under Origin_K they are substantive. Is that difference physical, or an
  artefact of where the stage data come from? Owner decision 1 (§6).

***

## 2. Hypothesis table

Column (ii) codes:

- **X** must come from X, because it crosses the barrier.
- **X·s** belongs to X's scope by the F2 row, but does not cross the barrier.
- **OI** is supplied by the stated architecture. On the field-neutral side it arrives through H27.
- **RES** is a separate residual.
- **MATH** is implied by other rows (§4).
- **DEF** is definitional once M0 fixes the object.
- **—** is used only by the converse.

In column (iii), "yes" means the row needs an operation outside `NonnegBounded`. The label says how that is known:
[K] for a kernel witness, [W] for a written argument through a dictionary that has no predicate at M.

**0 — origin**

| id | hypothesis | (i) status at M | (ii) | (iii) barrier | (iv) necessity question |
|---|---|---|---|---|---|
| H0 | `Origin`: 𝔒 is the observer model of ℛ extended by ε, for every admissible (Obs, μ) | no predicate [U]. `ensemble_underdetermined` [K] StochasticInterface.lean:118. PT-STAGE-1 is a draft only (A:227) | RES | No: the origin is not an operation. But the passive finite-Ω tower has finite-orbit bodies and so no drive (`isEmpty_drivability_of_finite_orbits` [K] OrbitNormalization.lean:124; NG1 [W+X], A:412–425). The origin must therefore route ε's operations into the tower | Does QMfin hold for every admissible (Obs, μ), or does it single out μ, for example one giving a faithful reference state? [U] |

**S — the single elementary system (K∞, K1)**

| id | hypothesis | (i) status at M | (ii) | (iii) | (iv) |
|---|---|---|---|---|---|
| H1 | SC∞ `SCInf` | [K] StageCompletion.lean:78, introduced; only `bitTower_scInf` :401 | RES (DEF under Origin_M) | no | Implied by QMfin's stage presentation [W]. Not automatic for towers (`not_scInf_bad` [K] :350) |
| H2 | `FiniteRank` | [K] :299, introduced. Automatic for finite Ω [W+X, research archive] | RES (DEF under Origin_M) | no | Implied by finite carriers, where the rank is `card S ^ 2 − 1` [W] |
| H3 | `BinaryVisible` on Elem | [K] :244, introduced | MATH: no consumer once H9′ replaces H9 (G:345–351) | no; a register readout is OI (`Architecture.proj` ImplementationLocality.lean:506) | Is it needed at all? Its only consumer is `perfectlyDistinguishable_visible` :274 [K] |
| H4 | `Elem τ`, the elementary scope | no predicate [U] (ROADMAP:1024) | RES | no | It scopes H8 and H14–H18. The converse needs it: the qutrit body fails Trans and Geom (A:231; [X] kn census §4) |
| H5 | K∞-Act: `OpDatum` pairs with `AffineRespect` and `Undoes`, with `G τ` the induced maps | [K] CompletionAction.lean:46, :58, :325, :333, introduced (existence is trivial) | RES (form); its content is X, since `G τ` must contain ε's unitaries | yes [W] through H8 | Implied by QMfin's unitaries [W]. A drive's generator must cross stages (`not_stagePreserving_of_infiniteOrderOn` [K] CompositionOrder.lean:378) |
| H6 | `PreservesBody (G τ)` | conditional on H5: `preservesBody_inducedEquiv` [K] :352 | MATH | no | none separate |
| H7 | K∞-Drive `ElementaryDrivability` | [K] KInfFoundations.lean:264, introduced; A's Independent-verdict flag (A:234) | MATH-redundant: no chain theorem consumes it (it appears only at OrbitGeneration.lean:150, :161 and OrbitNormalization.lean:107, :124 [K, grep]). Its pair role is played by I5 with H-COMPAT [D] | yes [W] (finite-orbit bodies have no drive [K] :124) | Moot for sufficiency. QM satisfies it (`ball3_drivable` [K] :490) |
| H8 | K∞-Trans `BoundaryTransitive (chartBody C) (G τ)`, or `DenseBoundaryOrbit` | [K] OrbitGeneration.lean:79 and DenseOrbit.lean:53, introduced. Ω₄ separation [D run 38096511360] (D:236–263). `not_boundaryTransitive_flow` [K] :620 | **X** (field-neutral image of X-1) | yes [W from K]: the exact form at d = 3 needs `#G ≥ 𝔠` (`not_boundaryTransitive_of_countable` EffectSpace.lean:858), while OI's reversible maps on an elementary system are conjugations by scaled permutations (`realized_of_instAvail` [K] ImplementationLocality.lean:530 with `permClass_bijectionLevel` [K] SubstratumInterfaceAudit.lean:488; diagonal case `permTheory_diagonal_only_scalar` [K] :674) and form a finite group | QM satisfies it [K] (`boundaryTransitive_fullAut3` OrbitGeneration.lean:537). It is independent of Drive, Seed and Geom [D Ω₄]. The dense form is strictly weaker [K] (DenseOrbit.lean:398). Is the dense form enough for exact (T5)? No: `hsharp` has no dense form (G:322–329) |
| H9′ | one stage effect with `p e x1 = 1`, `p e x0 = 0` (G's single-effect correction; H9 ⇒ H9′) | hypothesis of `sharpSeed_completion` [K] StageCompletion.lean:224; no named predicate | OI through H27 (a register readout: `localLuders` OperationalAssembly.lean:191, `Architecture.proj`) | no (diagonal) | QM satisfies it [W]. Load-bearing: `not_seedOrbit_unsharp_eq` [K] OrbitGeneration.lean:670 |
| H10 | K∞-Seed | free on the ball: `sharpEff_sharpSeed` [K] EffectSpace.lean:118. Stage form: #821 theorem 1 `sharpSeed_eball_of_stage` [D blob b6369153, run 38091534622 at L]. Depends on H1, H2, H9′ and P5, not H3 (G:345–351) | MATH | no | none separate: at the cone step its content is V4's (D:84–90 [W]) |
| H11a | `availOf` contains the stage tests | no predicate (G:355) | DEF (`availOf`, M0) | no | Is the "nothing else" clause necessary? Under QMfin `availOf` = all effects (`avail_eq_fullEffects` [K] EffectSpace.lean:727, after Γ7) |
| H11b | `availOf` is closed under transport by `G τ` | no predicate (G:357). Matrix analogue: `InstAvail.bind` [K] ImplementationLocality.lean:268 | DEF as a closure clause; **X** for its content, since the group is X-2's and must be uncountable | yes: tests off the readout basis need an operation outside the class (every available effect of a monomial theory is diagonal: E:205–213 [W from K `realized_of_instAvail` :530]). Cardinality at `Fin 2`: `countable_not_pairFlowSourced` [K] PairFlowEquivalence.lean:218 | QM satisfies it [W]. Load-bearing for countable towers: `not_sharpFamily_subset_of_countable` [D PID:500 @c9f16498] |
| H12 | K∞-Geom `SingletonFaces` / `RelStrictConvex` | [K] KInfFoundations.lean:139, :144, introduced. No consumer outside KInfFoundations [K, grep] | MATH-redundant (no consumer) | no | False for QM at level ≥ 3 [X, kn census §4]. Not needed |
| H13 | `EffectsOn (eball d) availOf` | conditional [K]: `stageEffects_isEffectOn` StageCompletion.lean:193, `isEffectOn_seedTransport` OrbitGeneration.lean:94 | MATH. G's correction: A's reading "stage ∪ seed orbit" made H11 definitional (G:294–301); `availOf` replaces it | no | none |
| H14 | `2 ≤ d` (two sharp tests) | [K] SharpTests.lean:41, :155, introduced; `two_le_not_implied` :197 | RES (one of H14 and H18) | no (geometric) | QM has d = 3 [K]. One of H14 and H18 is needed (K2Guard.lean:253 or K1Bridge.lean:138) |
| H15 | `IsNot (eball d) z N` | [K] CompositeDimension.lean:210, introduced | OI through H27: the bit flip is a permutation (`permClass_permMatrix` [K] :406) acting on the ball as `isNot_nflip` [K] :838 [W] | no | QM satisfies it [K] :838 |
| H16 | K∞-Copy: one N for both copies, or type covariance | `CopyNatural` [K] KInfFoundations.lean:284; built into `NativeGateOf`'s single N (K1Bridge.lean:49). Type covariance [D #822, run 38091534622]; relative form [D run 38606561330 @c9f16498] | OI through H-CAR and `LabelInvariant`, since identical tokens carry the same permutation [W]. MATH as a separate row | no | Load-bearing: the d = 5 two-NOT countermodels (NB-1 [X]). Is type covariance enough for the chain's selector? Yes in the relative form [D] |
| H17 | `NativeGateOf (eball d) avail z N T` | [K] K1Bridge.lean:49, introduced. Instance `nativeGate_cnot` [K] CompositeDimension.lean:1160; transport `nativeGate_of_cone_eq` [K] K1Bridge.lean:73 | OI for the gate (T = CNOT is a permutation: `dict_cnot` [K] BridgeDictionary.lean:71; `cnotMat_eq_swap` [D PID:152]). MATH for positivity, via P7. That the observer's gate is cnot (A's M3b) is part of H27 | no | QM satisfies it [K]. There is no uniqueness theorem for native gates (A:340) |
| H18 | `EntanglingOf` | [K] K1Bridge.lean:64; `entangling_cnot` [K] :1380 | OI, as H17 | no | as H14 |

**P — the pair (K2 and the step-4 interface)**

| id | hypothesis | (i) status at M | (ii) | (iii) | (iv) |
|---|---|---|---|---|---|
| H19 | local tomography and the carrier `W d` | `Composite.lt` [K] CompositeInterface.lean:243, introduced; `W d` CompositeDimension.lean:97; M4 has no predicate | RES (part of H-CAR) | no | QM is locally tomographic [L]. LT is independent of the other composite fields (`not_locallyTomographic_paddedBall3` [K] :912) |
| H20 | products of `eball 3` in `prep` | introduced (`hH1` EqvK2MaxCone.lean:153; `hprod` [D PID:430]) | MATH, given one basis product (OI: `instAvail_reset` [K] BridgeFiniteProtocol.lean:111), ε's local unitaries, H-COMPAT and H21 (B L9, B:315 [W]) | yes for products of non-basis states [W] (E:254–255) | QM satisfies it [K: products lie in Q3]. With L9 it is not a separate premise |
| H21 | cone closure (`hadd`, `hsmul`) | introduced (EqvK2MaxCone.lean:153); controls [W] (A:248) | RES; DEF if `prep` is defined as the conic hull of the normalized available joint preparations | no (classical mixing) | Q3 is a convex cone [K]. Load-bearing (A:248) |
| H22v | `hvalid : prep ⊆ maxConeOf avail` | introduced, unsourced (#836 is a plan only) | **X·s** ("valid measurements") | no (a positivity statement) | QM satisfies it [W]. Does it follow from H11a, H11b and H-COMPAT? Open. Availability does not give preservation (K_B, #820 [W+X]) |
| H22t | the sharp or dense family is contained in `avail` | `hsharp` is conditional on H6, H8, H10 and H11 [K] EffectSpace.lean:374. It is false for countable `avail` [D PID:500]. `hdense` suffices for the cone half [D PID:418, :430] | MATH from H8, H9′ and `availOf` (Γ7, N5 [W]) | yes, through H11b | The exact form is needed only for exact (T5) and for the eight exact CHSH settings (`chshTests` [D PID:509]) |
| H23 | `hH2`: cnot-invariance of `prep` | introduced at M. Conditional [D]: `driveClauses_of_admitted` PID:223 @c9f16498 (from `hswap` and `PairCompat`) | MATH | no (CNOT is OI) | `Q3_cnot` [K] EqvK2Generation.lean:503 |
| H24 | `hA`: the `rotLin` flow and `cycEquiv` on the target token | introduced at M. Conditional [D], same theorem (from `hflow` at `Fin 2`, `ContextStable`, `Architecture.mul` and `PairCompat`) | MATH; the content is in I5 | yes [K] for the phase half (`phaseMat_eq_flow` [D PID:99] gives `phaseGate` at s = π/2, outside by `phaseGate_not_preservesNonneg` [K] SubstratumInterfaceAudit.lean:559). For the cyc half the monomial class misses it ((substratumClass, K_mono) [X+W] B:268–279) | `Q3_aMiss` [K] EqvK2Converse.lean:174; `driveInvariant_of_eq_Q3` [K] EqvK2MaxCone.lean:165 |
| H-COMPAT | `PairCompat ε.𝓘 prep` and `ConeCompat_k` | [D] PID:206 @c9f16498, introduced, unsourced. `pairCompat_Q3` [D] PID:286 | **X·s** ("compatible state transformations") | no as a statement, since every unitary preserves Q3. Its non-trivial instances are ε's own operations | QM satisfies it [D PID:286]. Availability does not imply it (K_B, #820). Step 4's converse is refuted (`diagClass_pairControl` [D] PID:304; `not_drives_of_pairCompat` :313) |
| H-CAR | the physical pair (or k tokens) is implemented on `Fin 2 × Fin 2` (or `Fin 2^k`) through `dict` (or `dictK`), and adjoining a token is the right factor | introduced [U]. Its mathematical part L1-M is plausibly provable (FinitePauli inverse pair [D run 38457070337]; B:143–168) | RES | no | QM composites are tensor products [W]. The token order is fixed once (B:166–168) |

**C — composites and carriers**

| id | hypothesis | (i) status at M | (ii) | (iii) | (iv) |
|---|---|---|---|---|---|
| H25 | k-token composition, consistent across groupings (FCC) | no predicate. #829 is a draft [U]; KT4 theorem [D run 37948419430] | RES | no | QM satisfies FCC [W]. Is FCC independent of H19 and H-CAR_k? Open |
| hpow | `∀ k, DrivesElementaryAt ε.𝓘 (Fin (2^k))` | [D] KnDescentDesign.lean:51 @d3a95be6 | MATH from X-1's token form by synthesis (Γ3 [W+L]); otherwise X | yes [K] (it contains the phases) | `fullClass` satisfies it [D `drivesElementaryAt_fullClass`] |
| H26 | every type is a subsystem of a register (for sizes ≠ 2^k) | no predicate on the field-neutral side. Matrix compression [D]: `compress_mem` KnDescentDesign.lean:64, `drivesElementary_of_pow` :173 | RES at the type level; MATH at the matrix level (Γ4) | no | Needed only for local dimensions ≠ 2^k as types; F2-reg drops it. `ContextStable` at odd spectators is load-bearing for descent (B L7 [W+X], B:294–308) |

**O — operations (K3)**

| id | hypothesis | (i) status at M | (ii) | (iii) | (iv) |
|---|---|---|---|---|---|
| CL | `Architecture`, `ContextStable`, `LabelInvariant` and `DaggerStable` of `ε.𝓘` | [K] definitions ImplementationLocality.lean:506, :359, :364; MicroscopicReversibility.lean:216. `permClass` has all four [K] (:350, :358, :362, :366). Generated model at `Fin 2`: `MixC` [K] StateMixingCoupling.lean:74, :81, :380, :442 | RES. Satisfiable by generation: the least class that contains `permClass` and ε's generators and satisfies these Horn clauses [W]. Their content then moves into H27 | no (`permClass` satisfies them) | `fullClass` satisfies them [K]. Carrier-general `ContextStable` is load-bearing off qubit powers (B L7) |
| CONS | `permClass ≤ ε.𝓘` | no predicate (it is what "extension" means). It appears as `hperm` in `qm_of_mixSourced` [K] :486 | DEF | no | definitional |
| SOI | `SourcedOI (genTheory ε.𝓘 ε.arch A)` | [K] for `permTheory` (SubstratumInterfaceAudit.lean:660). For an extension: [W], the proof of :660 from CL and CONS | MATH | no | QM ⟹ `SourcedOI` [K] (`sourcedOI_of_qm` :636) |
| I5 | `DrivesElementary ε.𝓘`: transition flows (`a = b` allowed), swaps and quarter phases at every carrier | [K] definition SubstratumSource.lean:77, unsourced. False for the substratum class (`substratum_residual` [K] StructuralClosure.lean:383) | **X**, the resource. Reduced obligation: the flow conjunct alone (§4 R3, R4) | yes [K]: `phaseGate_not_preservesNonneg` :559; `mixImage_not_preservesNonneg` FrozenSourcing.lean:199; `nonnegBounded_verdict` :327 | Relative necessity [K] at the theory level (:654 `.mp`). Is the token-level flow family enough? [W+L] (Γ3). The token's cross-flows alone are not, by products (§1.6 [W]) |
| I6 | `QuantumArchitecture ε.𝓘` | conditional [K] SubstratumSource.lean:86 | MATH (CL and I5) | as I5 | none |
| H27 | the observer's states, tests and operations are those of `extTheory ε` (soundness and completeness of the dictionary) | no predicate | RES (with H0) | no (an identification) | QM theories are implementation-generated [K] (`generated_of_qm` ImplementationLocality.lean:1004; `qm_generated_by_quantumArchitecture` SubstratumSource.lean:161) |
| H28 | typed operational closure, and a typed lift | the fields of `TypedOperationalTheory` [K] TypedCompletion.lean:165. No typed theory is built from a class at M; the only instance is `typedDiag` :916 | MATH (Γ5) | no | `ShadowQuantum` ⟺ typed Kraus [K] :850 |
| H-GEN, H-OPSAT | cone-gate admission; preservation implies admission | introduced (B:237, :252) | — (converse only) | — | Used only to go from the cone to drivability (B L3a, L4 reverse) |

**B — correlations (E's H-Corr 1–7, E:338–358)**

| id | content | (i) status | (ii) | (iii) | (iv) |
|---|---|---|---|---|---|
| HC1 | carrier and multi-token LT | = H19 + H-CAR_k + H25 | RES | no | as H19 and H25 |
| HC2 | products preparable, mixing available | = H20 + H21 read as availability | MATH (L9) and RES (H21) | yes for products of non-basis states [W] | as H20 |
| HC3 | sharp family on every token; product-test validity | = H22t + H22v | MATH and X·s | yes for H22t, through H11b | as H22t and H22v |
| HC4 | CNOT(i→j), and the rotation flow and cyc on each token, as available operations | CNOT is OI [K :406; D PID:152]; the rotations and cyc are I5 | OI for CNOT, X for the rest | yes for the rotations and cyc [K] | as I5 |
| HC5 | `bind`, `coarse`, spectator locality | [K] `InstAvail` ImplementationLocality.lean:268; CL | OI for `permClass`; RES (CL) for ε | no | as CL |
| HC6 | every available local instrument preserves the joint cone | unsourced. Conditional through PreservationInduction [D #831, run 38450187534 per B:260–264, not re-verified] | MATH, given H-COMPAT and a cone family on every `S × Fin m` (B L10, open) | no | Does preservation on qubit-power carriers suffice? Open (B:317–319) |
| HC7 | the bridge between operational states and tests and the tables | = H-CAR + H27 | RES | no | as H27 |

**Counts** (47 rows).

| class | rows |
|---|---|
| X, the core resource in three vocabularies | 3: I5, H8, H11b (content). X content also sits in H5, H24 and hpow |
| X·s, extension scope without crossing the barrier | 2: H22v, H-COMPAT |
| OI, through H27 | 5: H9′, H15, H16, H17, H18; also the CNOT of HC4 and HC5 for `permClass` |
| RES | 15: H0, H1, H2, H4, H5 (form), H14, H19, H21, H-CAR, H25, H26, CL, H27, HC1, HC7 |
| MATH, not a premise | 16: H3, H6, H7, H10, H12, H13, H20, H22t, H23, H24, hpow, SOI, I6, H28, HC2, HC6 |
| DEF | 2: H11a, CONS |
| converse only | 1: H-GEN / H-OPSAT |

***

## 3. Gap map, in build order

| # | link | proves | math only / needs X | evidence now | marks |
|---|---|---|---|---|---|
| Γ0 | definitions | `OIRealization`, `Ext`, `extTheory`, `ObserverModel⁺`, `availOf`, `Origin`, `StageIso`, `QMfin`, `CorrClause` | math (definitions) | A's M0 sketch (A:124–138) | — |
| Γ1 | **matrix core in extension form** | `sourcedOI_of_extension`; `DrivenPair`; QM ⟺ `DrivenPair` for every closure-respecting extension of `permClass`; the barrier placement `¬NonnegBounded` | math | [K-inst] of :654, :660, RouteB.lean:223 and FrozenSourcing.lean:99 | — |
| Γ2 | repertoire reduction | `phaseGate a = flow (transition a a) (−π/4)`; swaps ∈ `permClass` (or L8); `drivesElementary_of_flows`; L3b on a generic carrier (B:203–225) | math | [W from D] `flow_transition_self` PID:67; [K] :406; [X] L8 for n ≤ 5 (B:309–313) | — |
| Γ3 | register synthesis | token U(2) flows, OI's CNOT and CL give `DrivesElementaryAt (Fin 2^k)` for every k (L3a(ii)) | math | [W+L] Barenco et al. 1995; [D] FiniteWalsh and FiniteCircuit (run 38457070337); formalization.md obligations 1–3 still open (B:234–238) | **k-tokens** |
| Γ4 | descent to every carrier | `hpow` with carrier-general `ContextStable`, `LabelInvariant` and `Architecture.block` gives `DrivesElementary`. Also L7 divisor descent, with the qubit-power-spectator control (B:294–308) | math | [D] KN-DESC: `drivesElementary_of_pow` KnDescentDesign.lean:173, `quantumArchitecture_iff_pow` :190 (runs 38457070337 and 38597304093) | **KN-DESC descent; carriers that are not powers of two (operation side)** |
| Γ5 | typed lift | `typedGen 𝓘 : TypedOperationalTheory` (attach / protocol / discard) and `QuantumArchitecture 𝓘 → (typedGen 𝓘).ShadowQuantum`, via P11 and soundness (`realized_of_instAvail` :530) | math | no object at M; [K] for the endpoints (:136, TypedCompletion.lean:850) | (T2), (T3) |
| Γ6 | **normalization** | (a) Pair: `tr (dict ω) = ω 0 0` (from `trace_T_mul_dict` EqvK2Schema.lean:129 at (0,0)); `jointStates` (CompositeDimension.lean:190) ∩ Q3 = dict⁻¹(density matrices); sharp outcome probabilities lie in [0,1] and sum to 1 (`sharpProj_add_neg` [D PID:582], `prodEffVal_sharp_eq_trace` [D PID:614]). (b) M5 as a theorem: `eball 3 ≅ D(ℂ²)` by `tokMat` (EqvK2Schema.lean:74). (c) k tokens through `dictK` (L5). (d) Stage tables `p = re tr(Eρ)` with the unit going to 1 (`FiniteStage.unit_eq` KInfFoundations.lean:63) | math | [K-inst] for (a); [W] for (b)–(d) | **normalization** |
| Γ7 | **tests tied to stages** | `availOf`; the N4 and N5 composite `sharpFamily_subset_avail_of_stage` (G:251–281: `hypotheses_tr` OrbitNormalization.lean:295 followed by `sharpFamily_subset_avail` EffectSpace.lean:374); then `avail_eq_fullEffects` EffectSpace.lean:727; and the guard `Countable D.ι → (stageEffects D).Countable` [W] with `not_sharpFamily_subset_of_countable` [D PID:500] | math. X's content enters only as H8 and H11b premises | [K] + [W] | **tests tied to stages** |
| Γ8 | the single-system chain on `availOf` | P1–P8 (A:299–305), with `availOf` in place of the free `avail`; dense variants (DenseOrbit.lean:209, :243) | math | [K] | — |
| Γ9 | the pair | adopt step 4 (`pair_available_eq_Q3` PID:430, `pair_sharp_behaviours` :628, `chsh_attained_of_available` :394, `marginal_independent` :545); the joint-test clause (joint tests = all two-qubit effects, from product tests, joint unitaries and mixing) | math | [D] @c9f16498 run 38606560943; [W] for the joint-test clause | (T3), (Corr) at n = 2 |
| Γ10 | **arbitrary finite composites via k-tokens** | L1-M and `pairCarrierEquiv` (B:143–160); L5 `dictK` intertwinings (B:285–288); #829's `kCone_eq_QK_of_drive_maxCone`; L4′ (B:245–248); L2 `kToken_cone_and_descent` (B:170–199; SM:117–136) | math. Premises: H-CAR_k (RES), H-COMPAT_k (X·s), `hpow` (Γ3) | k-token cone theorem [U] (no object at any head: B:30–34); KN-DESC side [D] | **k-tokens with KN-DESC** |
| Γ11 | local dimensions ≠ 2^k as types | a subspace principle (types as compressions of registers) or the F2-reg scope. L10, a cone family beyond qubit powers, is open (B:317–319) | RES (H26) plus math | none | **carriers that are not powers of two (state and type side)** |
| Γ12 | **correlations at n ≥ 3** | Q-up from `prep k = QK k` through `dictK`, not from `maxConeK` (Acín et al., PRL 104, 140404 (2010) [L]; E:183–186, AW-E2). Q-down from availability of every PSD k-table (the state-level reading, as in step 4 (D)) and local POVMs on groups (Naimark: local dimension 2^m embeds every finite C_q [W], E:279). NS at k for general outcome families (W4, E:194–198). GHZ/Mermin attainment at n = 3 [W; an exact check is cheap] | math, given Γ10 and the X-supplied tests (H11b) as premises | [W] + [L] | **correlations at n ≥ 3** |
| Γ13 | origin and identification | `Origin` (M1, H0, H27) and the assembly of `StageIso`. PT-STAGE-1's ℕ-indexed tower is too small for exact (T5) unless the transporting group is uncountable (G:303–320) | RES (no predicates); owner decisions 1–3 | none | — |
| Γ14 | `X ⊢ R_X` | the extension's own theorem: its sourcing argument and one consequence beyond the resource (§A.29; fe5c7fb5 ROADMAP:1125–1129) | **needs X** | none | outside this target |

Final assembly: F2-fin is a short composition once Γ0–Γ12 are compiled (Γ11 with its RES premise or the F2-reg
scope) and Γ13's relations are stated. Under Origin_M the target needs only Γ0, Γ1, Γ2–Γ5 and Γ6(d), apart from
`X ⊢ R_X` and H0/H27.

### 3.1 The cheapest next compiled step that does not depend on X

**Γ1, a disposable design module.** X appears in it only as a premise. Every proof is a composition of landed
theorems; the only new matrix identity is a one-liner, and it goes in Γ2.

```lean
import OIBridge.SubstratumInterfaceAudit   -- SourcedOI :619, :654, :660, :711
import OIBridge.FrozenSourcing             -- NonnegBounded :65, nonnegBounded_not_phasesAvailable :99
import OIBridge.RouteB                     -- derivedOI_of_qm :223
import OIBridge.SubstratumSource           -- genTheory_avail_conj :103, fullClass_quantumArchitecture :151

def Extends (𝓘 : ImplementationClass) : Prop :=
  ∀ (S) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → 𝓘 S K
theorem sourcedOI_of_extension (arch) (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (hd : DaggerStable 𝓘) (he : Extends 𝓘) : SourcedOI (genTheory 𝓘 arch A)     -- the proof of :660, with `he`
def DrivenPair (T : FiniteOperationalTheory A) : Prop :=
  ∀ n, 2 ≤ Fintype.card (A × Fin n) → ∃ a b : A × Fin n, a ≠ b ∧
    ∀ t : ℝ, T.availExt n Unit (fun _ => conjChannel (flow (transition a b) t))
theorem phaseFree_iff_drivenPair (h : SourcedOI T) : PhaseFreeRichness T ↔ DrivenPair T    -- exchanges from h.2.2.1
theorem qm_of_extension [Nonempty A] … (hX : DrivenPair (genTheory 𝓘 arch A)) :
    ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch A)            -- sufficiency (:654 .mpr)
theorem drivenPair_of_extension_qm [Nonempty A] … :
    ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch A) → DrivenPair (genTheory 𝓘 arch A)   -- separate witness (:654 .mp)
theorem not_nonnegBounded_of_drivenPair [Nonempty A] … (hX : DrivenPair (genTheory 𝓘 arch A)) :
    ¬ NonnegBounded (genTheory 𝓘 arch A)               -- RouteB.lean:223, then FrozenSourcing.lean:99
theorem permClass_control [Nonempty A] : Extends permClass ∧ ¬ DrivenPair (permTheory A)   -- :711 via the iff
theorem fullClass_control  [Nonempty A] : Extends fullClass ∧ DrivenPair (genTheory fullClass fullClass_arch A)
```

- **Why it is decisive.** It fixes R_X at the theory level, with one witness per direction relative to OI's closure
  (§A.34). It proves that R_X lies outside `NonnegBounded`, which is the barrier placement column (iii) asserts for
  I5. And it makes CONS a stated premise.
- **Controls.**
  - `permClass` meets every premise except the driven pair and is not QM. This makes the driven pair load-bearing.
  - `fullClass` is the positive control.
  - Mutation: dropping `he` must break `sourcedOI_of_extension`. `diagClass` meets CL (LieRankSource.lean:90,
    :104, :112, :117) but does not contain the exchanges.
- **Natural companions in the same run** (also X-free and cheap):
  - Γ2: `phaseGate_eq_flow_self` from `flow_transition_self` (PID:67), and `drivesElementary_of_flows`. Mutation:
    `t = +π/4` gives the conjugate phase.
  - Γ6(a): `trace_dict` and `mem_jointStates_Q3_iff`. This needs `tensorOf 1 1 = 1`, which is not at M and is one
    line. Mutation: `2·ω` fails trace 1.
- **The next step after it** is Γ7, the stage-tie composites and the countability guard.

***

## 4. Redundancy check

| # | redundancy | evidence |
|---|---|---|
| R1 | H23 is conditional on `hswap` and `PairCompat` | [D] `driveClauses_of_admitted` PID:223 @c9f16498, run 38606560943 |
| R2 | H24 is conditional on `hflow` at `Fin 2`, `ContextStable`, `Architecture.mul` and `PairCompat` | [D] same theorem (SM:33–53) |
| R3 | The swap family is not an X-row. Swaps are permutations, so they are OI-sourced (`permClass_permMatrix` [K] SubstratumInterfaceAudit.lean:406), and under CONS they lie in `ε.𝓘`. Without CONS they still follow from flows and phases (L8) | [K]; [X] for n ≤ 5 and [W] in general (B:309–313) |
| R4 | The quarter-phase family is redundant given the flow conjunct: `flow (transition a a) t = 1 + (e^{−2it} − 1) E_aa`, so at `t = −π/4` it is `phaseGate a`. `DrivesElementary` therefore reduces to its first conjunct, given CONS (or L8) and `Architecture.mul` | [W from D] `flow_transition_self` PID:67 @c9f16498 (= KnDescentDesign.lean:109) |
| R5 | At the theory level, relative to `SourcedOI`, all of `DrivesElementary` reduces to one driven pair per level, with no phase premise | [K] `sourcedOI_qm_iff_phaseFree` :654; extension form [W] (Γ1) |
| R6 | `hpow` (KN-DESC) follows from X-1's token form by exact synthesis | [W+L] (Γ3); [D] partial |
| R7 | H10 is free on the ball. At the cone step, `∃ G r` with `PreservesBody ∧ SharpSeed ∧ Trans ∧ V4` is equivalent to `sharpFamily ⊆ avail`, with each direction witnessed | [K] `sharpEff_sharpSeed` EffectSpace.lean:118; [W] D:84–90 (forward :374; backward :230, :337, :362) |
| R8 | H13 follows from `availOf` (H11a, H11b, mixing) and H6 | [W from K] StageCompletion.lean:193, OrbitGeneration.lean:94 |
| R9 | H22t follows from H8, H9′ and `availOf` through N5. The cone half needs only the countable dense family | [W] G:273–290; [D] PID:418, :430 |
| R10 | H3 is not needed for H10, and its only consumer is `perfectlyDistinguishable_visible` | [W] G:350; [K] grep |
| R11 | H7 and H12 have no consumer in the chain | [K] grep (ElementaryDrivability: OrbitGeneration.lean:150, :161 and OrbitNormalization.lean:107, :124; SingletonFaces and RelStrictConvex: KInfFoundations only) |
| R12 | H16 is built into H17's single N. Type covariance is a strictly weaker sufficient form | [K] K1Bridge.lean:49; [D] run 38606561330 (`hcov_of_copyNatural`, `dim_of_nativeGate2Of_conj`) |
| R13 | H20 follows from one basis product, ε's local unitaries, H-COMPAT and H21 | [W] B L9 (B:315) |
| R14 | Under Origin_M, H1, H2, H5–H24, H-COMPAT and H22v are consequences of Γ1 and Γ6(d). Compatibility holds because unitary conjugation preserves PSD (`pairCompat_Q3` [D] PID:286). Validity holds because effects on states are positive. H8 holds because every unitary is available. So R_X collapses to I5 alone | [W from K + D]; scope flag: kinematics inherited (§1.3) |
| R15 | At the pair, `LabelInvariant`, `DaggerStable` and the quarter phases are unused. In KN-DESC, `DaggerStable` serves only the iff | [D] SM:51–52; C:118 |
| R16 | NS is automatic by bilinearity. At n = 2, Q-up follows from `hmax` alone; at n ≥ 3 it does not | [D] `marginal_independent` PID:545; [W] W4 (E:194–198); [W+L] W1 and W2 (E:163–186) |
| R17 | The CNOT part of H-Corr 4 is OI. Only the local rotations and cyc are X | [K] :406; [D] PID:152 |
| R18 | CL is satisfiable by generation, so the four clauses are not independent hypotheses on a generated `ε.𝓘`. Their content moves to H27. At `Fin 2` the generated model exists | [W]; [K] `MixC` StateMixingCoupling.lean:72–84, :380, :442 |
| R19 | H-GEN and H-OPSAT are not needed for sufficiency | [W] B:227–238, :252–254 |

**Not redundant (load-bearing), each with its control.**

- Drivability at the pair: (substratumClass, K_mono) [X+W] B:268–279.
- H-COMPAT is not implied by availability: K_B (#820) [W+X].
- `ContextStable` at odd spectators: the qubit-power-spectator class [W+X] B:302–308.
- The converse of step 4: `diagClass_pairControl` [D] PID:304.
- The sharp stage test: `not_seedOrbit_unsharp_eq` [K] :670.
- The closure for countable towers: [D] PID:500.
- SC∞: `not_scInf_bad` [K] :350.
- H8: Ω₄ [D] and `not_boundaryTransitive_flow` [K] :620.
- H16: NB-1 d = 5 [X].
- An uncountable resource for the exact target: `mixTheoryR_not_qm` [K] StateMixingCoupling.lean:679,
  `countable_not_pairFlowSourced` [K] :218, `fixedGateTheory_not_qm` [K] DiscreteCompletion.lean:1948.

***

## 5. Assumption-watch markers (cross-propagation)

- **AW-I1 — `DrivesElementary` overstates X's obligation.**
  - At the theory level, relative to `SourcedOI`, one single-pair transition flow per level is equivalent to exact
    QM [K] :654.
  - At the class level the flow conjunct alone suffices (R3, R4).
  - Any statement naming the swaps or the quarter phases as part of the extension principle should drop them, or
    name the reduction it declines.
- **AW-I2 — the exact target needs an uncountable X.** G's AW-G2 (G:459–463) now has kernel witnesses at `Fin 2`:
  `mixTheoryR_not_qm` :679, `countable_not_pairFlowSourced` :218 and `fixedGateTheory_not_qm` :1948.
  - So an X with countably many operations (one fixed gate, a countable menu) can reach at most F2-fin-dense, and
    that endpoint exists only at `Fin 2` (DenseInstrumentBridge.lean:521).
  - With `availOf` over a countable tower, exact (T5) holds only through an uncountable transporting group
    (G:303–320).
- **AW-I3 — one resource, three images, no map.**
  - X-1 (matrix), X-2 (chart transitivity) and X-3 (test closure) are one physical resource. H27 has no predicate,
    so they are three premises at M.
  - This is a shared ingredient, not an identification (code-review bridge rule). The same holds for E's AW-E3
    (E:390–391).
- **AW-I4 — the short route inherits the complex field.** Under Origin_M every field-neutral row is a consequence
  (R14). But `ℂ` and the Hilbert carriers come from the stated configuration-level interface (`permTheory` over
  `Matrix Conf Conf ℂ`). They are not derived. Read through Origin_M, an F2 claim is a K3-type statement (A:257–258).
- **AW-I5 — "valid measurements" and "compatible state transformations" are identification content.**
  - In the F2 row they are placed in the extension (fe5c7fb5 ROADMAP:1125–1127).
  - Neither crosses the barrier. Each is substantive only under Origin_K (R14).
  - An extension principle that is claimed to supply them should say which origin it assumes.
- **AW-I6 — leaving `NonnegBounded` is necessary for R_X, not sufficient** (§1.6, [W]). The uniform-ray invariant
  and the reality invariant each exclude a fragment that lies outside the barrier. The phase content is
  load-bearing both in "token cross-flows only" and in "real mixing only".

***

## 6. Owner decisions this exposes

1. **Origin_K or Origin_M.**
   - Origin_M makes the sufficiency target nearly all mathematics, but with inherited kinematics.
   - Origin_K keeps the K chain as the assembly route, as the F2 row states, but leaves 15 residual rows.
   - The table is written for Origin_K, and R14 records what collapses under Origin_M.
2. **Exact or dense (T5).** The exact target forces an uncountable X (AW-I2). The dense target has no
   carrier-general endpoint at M.
3. **F2-fin or F2-reg.** F2-reg drops H26 and Γ11. F2-fin needs a subspace principle for types of size ≠ 2^k.
4. **X's vocabulary.** If X may be stated as an admission into the implementation class, R_X is I5. If it must be
   stated on stage data, R_X is H8 with H11b, and I5 must be derived through H27 and H-GEN, which is the converse
   machinery of B L3a(ii).

***

## 7. Summary (10 lines)

1. F2-fin(X): `OIStated ℛ ∧ Origin ℛ ε 𝔒 ∧ X ∧ Res ⟹ QMfin 𝔒`, with X a placeholder entering only through R_X; `X ⊢ R_X` is the extension's own theorem, outside this target (§1.3).
2. QMfin: typed exact QM (`ShadowQuantum`, TypedCompletion.lean:291), normalized states and probabilities, tests defined as `availOf` (stage tests closed under the observer's maps, mixing and unit), every finite product of types, any finite local dimension, C_q at every n (§1.2).
3. The matrix core is [K] at M and uncited by A–G: `sourcedOI_qm_iff_phaseFree` (SubstratumInterfaceAudit.lean:654), `qm_iff_derivedOI_pairFlowSourced` (PairFlowEquivalence.lean:199), `qm_of_mixSourced` (StateMixingCoupling.lean:486).
4. Relative to OI's closure, one continuously driven pair per level is necessary and sufficient for exact finite QM at the theory level [K]. The open content is the identification layer and `X ⊢ R_X`.
5. R_X's core is I5, H8 and H11b, one resource in three vocabularies, each crossing the barrier (I5 [K]; H8, H11b [W from K]). H-COMPAT and H22v are X's scope by the F2 row but do not cross it.
6. Corrections per G: H9 → H9′; H10 free and H3-independent; H11 → H11a (DEF) + H11b (X content); H13 derived from `availOf`, which replaces the free `avail` everywhere.
7. Redundancies: H23 and H24 conditional on drivability plus compatibility [D]; swaps OI-sourced [K]; phases are self-flows at −π/4 [W from D]; H7 and H12 unconsumed [K]; H10 free [K]; H13 and H22t from `availOf` [W]; under Origin_M all of H1–H24 [W].
8. Gap map Γ0–Γ14: Γ0–Γ10 and Γ12 mathematics only, Γ11 and Γ13 residual, Γ14 needs X. Marks: normalization Γ6, stage tests Γ7, k-tokens with KN-DESC Γ3/Γ4/Γ10, carriers that are not powers of two Γ4/Γ11, correlations at n ≥ 3 Γ12.
9. Cheapest X-free compiled step: Γ1, the matrix core in extension form, both directions plus the barrier placement, controls `permClass` and `fullClass`. Γ2 and Γ6(a) fit in the same run.
10. NEW (scoped, [W]): leaving `NonnegBounded` is not enough. Token-level cross-flows with permutations fix the uniform ray, and real mixing with `permClass` stays within scalar multiples of real matrices, so the phase content is load-bearing in both fragments.
