# OI-STAGE: packaging the OI construction as a field-neutral `DirectedStages` — RESULT (read-only)

**Base.** `0f2687b7b87925b53c6e3d8c6d1a233f36624dea`, read in the detached worktree `scratchpad/wt-drive`, which is
untouched.

**What was not done.** No branch, round, preregistration, repository edit or GitHub write.

**Evidence levels.**
- **kernel**: a landed identifier, given with file:line at the base.
- **exact**: one of the two scripts below, in exact rational arithmetic, replaying byte-identically.
  - `oistage_checks.py` prints `OK -- 20/20 checks, 3 countercontrols expected-false`. sha256 of the script
    `38bacf2b…7e1`, of the output `f466ff1f…b52`.
  - `leap_rank.py` computes integer counts and exact ranks. sha256 of the script `4e8f6dbb…793`, of the output
    `d2e6086c…ab3`.
- **written**: an argument given here.
- **citation**: literature.

Paths are under `verification/lean-mathlib/OIBridge/`. Abbreviations:

| abbreviation | module |
|---|---|
| PQ | PassiveQuotient |
| DG | DomainGlue |
| OQ | ObservabilityQuotient |
| CQ | ControlledQuotient |
| CM | CanonicalMeasure |
| SI | StochasticInterface |
| PC4 | PhysicalC4Discharge |
| RT | RegionTower |
| SOL | SecondOrderLayer |
| PO | PassiveObservation |
| CO | CentralObservation |
| SC | StageCompletion |
| CA | CompletionAction |

**Productivity test, fixed before starting (§A.31).** A finding counts as a gem only if it does more than restate
"OI-STAGE is missing", and either constrains what DRIVE needs from OI or exposes a hidden assumption.

***

## 0. Verdict

1. **Yes as a stage system.** The OI construction packages as a field-neutral `DirectedStages`, the *protocol
   tower*.
   - Its probabilities are conditional counting measures on substratum configurations.
   - Its forward maps are inclusions of protocol labels, so every `DirectedStages` law is `rfl`.
   - SC∞ holds:
     - by construction in the finite form;
     - in the lattice form, by the landed causal cone (RT:283) and uniform fibres (RT:398).
   - There is no trace, no ℂ and no Born rule anywhere.
   - None of this is landed. The ingredients are, and the remaining steps are kernel-cheap.
2. **OPACT-1 data come for free.** The OI-native operations are the time step and the observer's actions.
   - They are **Prep-valued and move each preparation to the next stage**, the shape F-D3 requires.
   - When the effect protocols are closed under prefixing by steps, every such operation acts on effects by a
     label map. AffineRespect is then automatic, and bijective actions supply the inverse data.
3. **FiniteRank sits exactly where DRIVE is impossible.**
   - **NEW, NG1.** For a finite substratum, FiniteRank is automatic, but there are only finitely many hidden
     posteriors. The completed body is then a polytope, and no drive exists.
   - For the infinite lattice form, FiniteRank is **not** automatic. It stays the open assumption, the one
     Main.md:542 already names.
   - OI-native exact data on the second-order rule: Hankel ranks 1, 1, 1 (trivial body) for the linear rule, and
     1, 4, 6, still growing, for the nonlinear rule.
4. **NEW, NG2 (field-neutral form of the corpus's passive-observation theorems).**
   - Reading the visible sector passively makes observe-and-forget equal to idle (exact A5).
   - With FiniteRank and a time step reversible on the body, the body is either a single point or has no d+2
     extreme points in general position. So it is not strictly convex, and in particular not a ball.
   - **Consequence for Route Γ:** on a ball-like body the generator g cannot be the passive time step. A
     ball-like body with reversible free evolution needs **record-writing, invasive** observation.
   - The positive control (exact Q1–Q4) shows that FiniteRank, a non-polytope body and an infinite-order
     reversible idle coexist, but only invasively.

**Revised location of the DRIVE premise inside OI-STAGE.** Three premises remain:
- FiniteRank of the infinite-substratum completion;
- invasive (record-writing) observation;
- an infinite-order local action with OFF.

The stage packaging itself is not a bottleneck.

***

## 1. The candidates

### 1.1 The finite protocol tower PT(Ω, φ, π, μ, A)

**Data.**
- Ω, a finite set of configurations.
- φ : `Equiv.Perm Ω`, the dynamics.
- π : Ω → V, with V finite, the visible readout.
- μ, a probability weight on Ω. The canonical choice is `unif` (CM:106), which is invariant under every
  permutation (`counting_invariant` CM:205). Invariance does not select it (`stochastic_interface_gap` SI:182);
  the counting choice is the corpus's maximal-entropy selection (`counting_maximal_entropy` CM:227).
- A finite action menu `acts : A → Equiv.Perm Ω` (CQ:56 `actWord`).

`cutRealization` (PC4:582) supplies (V×H, step, prior) from a substratum and a visible region.

**Steps.** The step alphabet is Σ = {obs, idle} ∪ A.
- obs records π(ω), then applies φ.
- idle applies φ.
- a applies `acts a`.

**The stage system.**

| field | candidate |
|---|---|
| ι | ℕ, the protocol length n; directed by `max` |
| P_n | pairs (σ, r) with σ ∈ Σ^{≤n} and r ∈ V^{#obs σ}, such that μ(C_{σ,r}) > 0, where C_{σ,r} = {ω : the record of σ from ω is r} |
| E_n | pairs (σ′, B) with σ′ ∈ Σ^{≤n} and B ⊆ V^{#obs σ′} |
| p | p((σ′, B), (σ, r)) = μ{ω ∈ C_{σ,r} : the record of σ′, run from the state σ leaves, lies in B} / μ(C_{σ,r}) |
| unit | ((), {()}) |
| map (n ≤ m) | `onE = id`, `onP = id` on labels, so P_n ⊆ P_m and E_n ⊆ E_m |

The landed ingredients:
- `trajProb` (PQ:339) is the passive special case: σ′ = obs^T and the preparation is μ itself.
- `itiIndicator` (DG:149).
- `BranchDomainK` (OQ:108) has the constructors `mono` (OQ:110, the inclusion P_K ⊆ P_{K+1}), `evolve` (OQ:112,
  the time step, which raises the stage) and `branch` (OQ:114, conditioning on a visible value). These generate
  exactly the unnormalized preparation weights of the passive part of P_n.

### 1.2 The lattice cone tower CT (the faithful OI form: infinite substratum)

**Data.**
- A finite-range reversible rule on ι → Q with a `CouplingGraph` G (RT:254).
- A visible window W, together with the supports of the actions, which are local bijections: `gateEquiv` (SOL:279),
  extended to larger regions by `extPerm` (SOL:87, `extPerm_gateEquiv` SOL:301).

**Stage n.**
- Configurations are Conf(B_n) with B_n = `ball G W (2n)` (RT:259), carrying the uniform counting measure.
- Preparations, effects and the table are as in PT, computed on Conf(B_n).
- **Well-defined:** every protocol record of total length ≤ 2n depends only on B_n (`iterate_dependsOnlyOn_ball`
  RT:283, `readout_unaffected_outside_ball` RT:304).
- **SC∞ from n to m:**
  - the uniform measure on Conf(B_m) restricts to the uniform measure on Conf(B_n), because every fibre has
    |Q|^{|B_m∖B_n|} elements (`card_fibre` RT:398);
  - together with cone dependence, the counts agree.

**What is missing.**
- the cone lemma for protocols that interleave local actions;
- a transitivity lemma for `extPerm` along Λ ⊆ Λ′ ⊆ Λ″;
- the packaging itself.

**The completion.** The completion is the infinite-volume visible protocol process under the uniform product
measure. Every bijective cellular automaton preserves that measure (Hedlund, citation; not landed).

***

## 2. The `DirectedStages` laws and their dependencies

| law | PT | CT |
|---|---|---|
| `directed` | `max` | `max` |
| `comp_E`, `comp_P` | `rfl` (inclusions) | `rfl` |
| `unit_map` | `rfl` | `rfl` |
| `nonneg`, `le_one` | ratio of a subset weight to the conditioning weight | the same, with counting |
| `unit_eq` | the empty protocol: B = {()} has full weight | the same |
| Fintype P_n, E_n | Σ, V and the length bound are finite | the same |
| **SC∞** | `rfl`: one global p | `card_fibre` RT:398 + `iterate_dependsOnlyOn_ball` RT:283 |
| positivity of the conditioning events | built into P_n | built into P_n |

Exact checks T0–T5 cover PT stages 0–3 on a toy: Ω = Z₄ × Z₂, readout = phase parity, actions = flip or swap of
the hidden bit.

***

## 3. FiniteRank

- **PT (finite Ω): automatic (written).** prepVec(σ, r) = R(ν_{σ,r}), with R linear from ℝ^Ω, so the rank is at
  most |Ω| − 1. NG1 then makes the body a polytope.
- **CT (infinite volume): an assumption.**
  - It is the obligation Main.md:542 names: "Any exact-completion reconstruction beyond a fixed finite carrier must
    additionally show that its chosen completion retains finite predictive dimension".
  - Exact data on the OI substratum's own second-order (leap) rule, with readout v₀ and the counting measure on the
    cone:
    - linear F = v_{i−1} + v_{i+1}: Hankel ranks 1, 1, 1 for n = 1, 2, 3, i.e. an i.i.d. visible process and a
      trivial body;
    - nonlinear F = v_{i−1}v_{i+1} + v_i: ranks 1, 4, 6, still growing at n = 3.
  - Exact R1 is a generic model: a hidden irrational rotation (cos a = 3/5) read through a first-harmonic emission.
    Its ranks are 2, 4, 6, 8; conditioning generates higher harmonics.
  - No OI rule is known whose cone tower has finite rank and a non-polytope body.

***

## 4. Field-neutrality

- PT and CT use only sets, permutations, counting and real ratios.
- Every ℂ object in the corpus is avoidable here: `QfbReal`, `IsUnistochastic`, `quasiState`, `localAlg` and the
  matrix `restrict`.
- The real objects listed (PQ, DG, OQ, CQ, CM, RT's `Conf`/`ball`/`card_fibre`, SOL's `gateEquiv`/`extPerm`) are
  ℂ-free in content. Some of their modules import ℂ transitively. A kernel round should import only the ℂ-free
  pieces or re-derive them.

***

## 5. Operations that move to finer stages

1. **Prep-valued and stage-raising (exact).**
   - For a ∈ A ∪ {idle}, τ_a(σ, r) := prepVec(σ·a, r). It maps P_n → P_{n+1}.
   - Observe-and-forget equals idle (passivity, exact A5).
   - This is the F-D3 shape: these operations cross stages.
2. **AffineRespect (exact A1; written proof).**
   - τ_a(x)(e) = p(a·e | x). On CSpace this is the label map e ↦ a·e, which is linear, so every finite relation is
     preserved.
   - It needs **PREFIX-CLOSURE**: a·e must be an effect whenever e is.
   - Countermodel (exact A3): with observation-only effects, the hidden-bit swap breaks a relation among
     preparations that pin the hidden bit. The hidden-bit flip respects it (A4).
3. **Inverse data (exact A2).**
   - On a finite Ω, the inverse of an action is a power of it.
   - In the lattice form, the gates are involutions (`depth_two_circuit`), so a menu closed under inverses is
     natural.
   - `Undoes` holds because a⁻¹·a·e and e have the same probability.
4. **Order.**
   - On a finite Ω every such operation has finite order (P2, and NG1).
   - In CT, a lattice translation or the update itself can have infinite order. Whether it does **on the body**
     depends on FiniteRank.

***

## 6. NG1: a finite substratum gives a polytope (NEW; written proof, exact P1)

**Claim.** For PT with Ω finite, every hidden posterior after a protocol is (μ∘σ⁻¹)·1_C, normalized, for some
permutation σ and subset C. Hence there are at most |Ω|!·2^{|Ω|} posteriors and finitely many preparation vectors.
So the body is a polytope, its automorphism group is finite, and no drive exists (no infinite-order g).

**Proof.**
- Each step either pushes the weight forward by a bijection or restricts it to a set and renormalizes.
- These two kinds of step commute up to relabelling.

**Exact check (P1).** On six random substrata with non-uniform μ, every posterior up to horizon 5 has this form:
273, 353, 289, 335, 171 and 105 posteriors.

**Relation to Main.md:540.** Main notes that "finitely many ontic states do not force a polytope state space".
That remark concerns *arbitrary* preparations, such as the SIC embedding. OI's preparations are conditionings and
pushforwards of one measure, which is what NG1 uses.

***

## 7. NG2: passive observation versus reversible free evolution (NEW in field-neutral form; written proof, exact L1–L2)

**Setting.**
- A protocol tower whose readout is passive: observe-and-forget equals idle. Every tower built by conditioning a
  classical substratum is passive (exact A5).
- FiniteRank holds, and the time-step datum W has an inverse datum, so W is an automorphism of the body cone.
- τ_v is the unnormalized branch "observe and see v". Each τ_v is positive and linear (a label map), and
  Σ_v τ_v = W.

**Proof.**
1. Set M_v = W⁻¹ τ_v. Each M_v is positive and Σ_v M_v = I.
2. Let u be an extreme ray. Then u = Σ_v M_v u with each M_v u in the cone, so M_v u lies on the ray of u: every
   extreme ray is an eigenvector of every M_v.
3. If the body has d+2 extreme points in general position, M_v = λ_v I (exact L1–L2, the eigenvector argument).
4. Every readout then has a state-independent law, and conditioning on it leaves W x unchanged. So every effect is
   constant and the body is a point.

**Conclusion.** Passive + FiniteRank + reversible time step ⇒ the body is a point or has no d+2 extreme points in
general position. That excludes strictly convex bodies of dimension at least 2, the ball among them.

**Corpus link.** This is the body-level, field-neutral form of `passive_branch_scalar` (PO:215) and
`complete_passive_iff_commutative` (CO:620). The corpus's own resolution, `recordInstr_writes` and
`recordInstr_not_passive` (InternalObserver), is that measurement is record writing.

**Positive control (exact Q1–Q4, an imported model).**
- The model is a rebit with an unsharp readout (λ = 3/5) and the Pythagorean rotation.
- Its rank is 3.
- Its idle is an isometry of infinite order, so the body is not a polytope.
- It is **invasive**: observe-and-forget is R·diag(1, 1, 4/5), which differs from idle = R.

***

## 8. Countermodels for the new compatibility premises

| premise | model | what fails | evidence |
|---|---|---|---|
| PREFIX-CLOSURE (effects closed under step prefixes) | observation-only effects with the hidden-bit swap | AffineRespect | exact A3 |
| positive conditioning events | a record of weight 0 | p undefined; excluded from P_n | written |
| inverse-closed action menu (lattice form) | a menu holding a gate but not its inverse | `Undoes` has no datum (finite Ω: automatic, by powers) | written |
| infinite substratum (needed for DRIVE) | any finite Ω | polytope body, finite Aut | NG1, exact P1 |
| FiniteRank (CT) | nonlinear leap rule; rotation model | ranks 1, 4, 6 and 2, 4, 6, 8 growing | exact `leap_rank.py`, R1 |
| invasive observation (for a reversible time step on a ball-like body) | any passive tower | body trivial or without d+2 extreme points in general position | NG2, exact A5, L1–L2; control Q4 |
| choice of measure | linear substrata | invariance leaves the ensemble undetermined | kernel SI:182 |

***

## 9. Circularity audit

| excluded item | verdict |
|---|---|
| **Qfb** | Not used. `QfbReal` and `IsUnistochastic` are avoided. |
| **Trace or Born probabilities** | Absent. p is conditional counting or measure. The only quadratic-looking formula is in the imported positive control Q, which is labelled as such. |
| **Bloch geometry** | Absent from every premise. The ball appears only as an excluded target in NG2's corollary and as the body of control Q. |
| **DRIVE** | Absent. There is no flow, parameter or continuity premise; time is discrete steps. |
| **DIM3** | Absent. |

***

## 10. Classification (§A.31)

- **NEW, F-S1.** Prefix-closed protocol effects make every OI operation AffineRespect, through a label-map dual. This
  is the field-neutral replacement for tomographic completeness, and it removes the forcing found in DRIVE's F-D1.
- **NEW, F-S2.** NG1: a finite substratum gives a polytope body, so there is no drive. Combined with automatic
  FiniteRank there, FiniteRank and DRIVE live in disjoint regimes unless the substratum is infinite.
- **NEW (field-neutral), F-S3.** NG2: passive reads with a reversible time step exclude strictly convex bodies. The
  drive generator on a ball-like body cannot be passive free evolution, and observation must write records.
- **ELABORATING, F-S4.** FiniteRank of the lattice completion is the sole open stage-level premise. The first exact
  OI-native ranks are 1, 1, 1 and 1, 4, 6.
- **CONFIRMING, F-S5.** Main.md:542's obligation, and the corpus's passive-observation results.

***

## 11. Consequence for the roadmap (for the owner)

**Stages.** OI-STAGE as a stage system is cheap and could be kernelized:
- PT, with its laws and NG1;
- CT, which needs the action-interleaved cone lemma and `extPerm` transitivity.

**As a source for DRIVE**, it reduces Route Γ's needs to three named premises:
1. FiniteRank of the infinite-volume completion;
2. invasive (record-writing) observation, needed whenever the target body is strictly convex with reversible free
   evolution;
3. an infinite-order local action with OFF.

AffineRespect and inverses are supplied by the construction once the protocol effects are prefix-closed.
