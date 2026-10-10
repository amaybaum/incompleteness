# COMP-1 — field-neutral composite interface: DESIGN (type round)

Read-only design note. Base `7c821261e2537a97b85ab78ae50c6998600bc019` (checkout `scratchpad/wt-r2`). Every
`file:line` below was verified by `grep`/`sed` against `verification/lean-mathlib/OIBridge/*.lean` at that commit.
Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, SC `StageCompletion`, CA
`CompletionAction`, IIP `InvariantInnerProduct`, NGB `NativeGateBall`, OA `OperationalAssembly`, ID
`InstrumentDilation`, MC `MonoidalCompletion`, RE `ReferenceExtension`, SB `SpectatorBridge`, AC `AncillaClosure`,
CO `CompletedOI`. Mathlib pinned `v4.33.0` (lean-toolchain `leanprover/lean4:v4.33.0`); no local Mathlib source tree,
so every Mathlib name is marked **to verify**. `TRB-1`, `ORD-1`, `COMP-1` occur in no file under `verification/` at
the base (grep), so nothing below can depend on them.

**Answer to the charter's typing question, in one paragraph.** Register attachment, joint reversible action, sharp
register readout, discard and their functorial laws *can* be typed without `ℂ`, matrices, Hilbert spaces or
`TensorProduct`: the composite is a structure over an arbitrary real carrier `V`, with a bi-affine *product-state*
map, a bilinear *product-effect* pairing, positivity of product effects on composite states, normalization, and
local tomography as a named field. Attachment is `x ↦ prodState x r₀`; discard is *defined* (not posited) in chart
coordinates as `ω ↦ (i ↦ prodEff (coord i) 1 ω)`; readout is `prodEff 1 (f k)`; joint reversible action is OG's
`PreservesBody Ω G` on the composite body. The laws "attach then discard is the identity", "readout is a test",
"readout on a product factorizes", "the marginal of a composite state is a state" and "reversible actions compose"
are theorems of the structure. What is *not* derivable is the existence of a composite with more than product
states: the field-neutral constructions available now give exactly the minimal body (convex hull of products) and
the maximal body (all normalized bi-affine functionals positive on product effects); the quantum body lies strictly
between and its selection is K2/NB-1 territory. The fiat is therefore relocated honestly: from "`V_A ⊗ V_B` is the
carrier" to "a composite with these fields exists" (FRONTIER F13, PREMISE), with the two extremal instances as
non-vacuity controls.

***

## 1. Census of composite notions at the base

| identifier | file:line | typing | consumable by COMP-1 without circularity? |
|---|---|---|---|
| `FiniteStage` (P, E, `p : E → P → ℝ`, `unit`) | KF:63 | field-neutral | **yes** — the product stage is definable from it (§2.1) |
| `StageMap`, `StageMap.Consistent`, `DirectedStages`, `SCInf` | SC:53/59/63/78 | field-neutral | **yes**; note `StageMap` is covariant in both `E` and `P`, so it types *attach* (`S → S×R`) but **not** *discard* (effects go the other way) — §2.1 |
| `body`, `prepVec`, `coord`, `stageEffects`, `CSpace = lp (fun _ => ℝ) ∞` | SC:141/135/157/176/128 | field-neutral | yes as the single-system input; the product tower's body is a candidate instance (§5, deferred) |
| `OpDatum`, `AffineRespect`, `after`, `Undoes`, `inducedEquiv`, `preservesBody_inducedEquiv`, `isEffectOn_pullback` | CA:46/58/305/325/333/352/364 | field-neutral | yes — supplies single-factor automorphisms `VA ≃ᵃ[ℝ] VA`; COMP-1 does not need them in round 1 |
| `CompletionChart`, `chartBody`, `chart`, `bodyR`, `effR` | CA:144/166, ON:357/397/400 | field-neutral | yes — fixes the finite-rank coordinates `Fin d → ℝ` in which discard is definable |
| `IsEffectOn`, `IsProperOn`, `IsBoundaryState`, `PerfectlyDistinguishable`, `SharpSeed` | KF:116/125/130/154, OG:65 | field-neutral | **yes** — readout is a `PerfectlyDistinguishable` register pair lifted by `prodEff` |
| `PreservesBody`, `BoundaryTransitive`, `SeedOrbitAvailable`, `seedTransport`, `words` | OG:69/79/74/49, ON:53 | field-neutral | **yes** — joint reversible action is `PreservesBody Ω G` on the composite carrier; `words` for composition |
| `ElementaryDrivability`, `.N` | KF:264/280 | field-neutral, one body | yes as the single-system NOT; the *common* `N` on two copies is `CopyNatural` |
| `CopyNatural N_A N_B e` | KF:284 | field-neutral, **one carrier `V`** | yes only for identical copies `Composite ΩA ΩA` on one `VA`; stated as conjugacy, no composite involved |
| `nb1_kernel_core` = `p_le_one ∧ parity ∧ dim_of_bounds` | NGB:255/176/194/248 | real, but typed in **block coordinates** (`A : Fin p → Matrix (Fin m) (Fin m) ℝ`, `B`, positivity as a scalar inequality over unit `b`) — the "two balls", "`G`", "common NOT" and "maximal tensor cone" exist only in the header (NGB:5–10) and the preregistration's `ℝⁿ ⊗ ℝⁿ` prose | **not a source**: it types no composite. Consumable *downstream* once a `Composite` instance supplies the blocks (K2 territory, §3D) |
| `FiniteOperationalTheory` (`avail`, `availExt n` on `Matrix (A × Fin n) (A × Fin n) ℂ`, `prepAvail`, `readout`, `prepAvail_discard`) | OA:594–655 | **ℂ / matrix**; levels are `A × Fin n` (one carrier + classical register), not two systems (RESULT §6.10) | **no**; and its docstring (OA:591–593) records that parallel extension of a system operation is deliberately absent even there |
| `local_tomography_physical (ρ σ : Matrix (A × B) (A × B) ℂ) …` | ID:440 | ℂ, presupposes the Kronecker carrier | **no** — reverse-direction witness only (RESULT §6.11) |
| `tensorOf`, `kronId`, `prodProj` | MC:193, ID:233, ID:359 (also Separability:61) | ℂ Kronecker | **no** |
| `MapSpectatorIndependent`, `localLuders`, `readout_is_localLuders` | OA:151/191, after OA:655 | ℂ | **no**; its field-neutral analogue (readout *with update* derived from spectator independence) is a COMP-2 candidate, not round-1 content |
| `ptraceAnc`, `ptraceAncL`, `uniformAttach`, `pureAttach`, `discardWith` | OA:453/480/492/500/515 | ℂ partial trace | **no** — discard is *defined* here from the pairing instead |
| `HasParallelReferenceExtension`, `withSpectator`, `ObservationalIndependence`, `parallelPair`, `parallel_of_observationalIndependence`, `InertSpectatorCompositionality` | RE:447/422, CO:129/137/147, SB:223 | ℂ | **no**; the field-neutral analogue (local extension of a factor action) is the named premise `LocalExt` (§3B) |
| `HasCompositeUnitaryControl`, `IteratedAncillaClosure`, `CompositeOperationalValidity`, `SystemToLevelOne`, `PhysicalCompletionConditions`, `PhaseFreeRichness` | OA:665, AC:247, OperationalValidity:88, LevelOneSeam:117, PhysicalCharacterization:295, MinimalRepertoire:423 | ℂ | **no**; K2 targets (§3D) |
| `HComp`, `SpectatorIndependent`, `ImplementationExtensionality`, `availability_not_implies_hComp` | MC:311/204/133/770 | ℂ | **no** |
| `KrausSoundExt`, `transposeMap`, `swapMat`, `HasQubitFactorExchange` | CompositeSoundness:123/286, FactorExchange:73/126 | ℂ | **no** |
| Mathlib `TensorProduct`/`⊗ₜ`/`kroneckerMap` | used in 10 modules (AncillaInterference, ClosureObstruction, DilationChoice, MinimalRepertoire, OperationalSourcing, RankGapTheory, SemigroupTransfer, SubstantiveCensus, UhlmannUniqueness, WordTraceSufficiency) | ℂ-matrix contexts | **no** |
| `ball3`, `ball3Drive`, `fullAut3`, `driveWords3`, `kInf1_ball3_full`, `segment2`, `bitTower`, `bitStage` | KF:311/449, OG:521, ON:571, KF:1076, IIP:491, SC:393/373 | field-neutral | **yes** — control instances (§7) |

Field-neutral modules contain no `ℂ` (grep count 0 in OG, ON, SC, CA, IIP, NGB; KF's four hits are comments). No
field-neutral composite, register, discard or marginal notion exists at the base (grep over those six modules: the
only hit is CA:318's "composite of the induced maps", meaning function composition).

***

## 2. The typed proposal

### 2.1 Candidate (i) — composite of two `DirectedStages` (stage level)

Definable now, no premise: `FiniteStage.prod S T` with `P := S.P × T.P`, `E := S.E × T.E`,
`p (e, f) (x, y) := S.p e x * T.p f y`, `unit := (S.unit, T.unit)` (bounds by `mul_nonneg`, `mul_le_one`
**to verify** name). `DirectedStages.prod DA DB` on `ι := DA.ι × DB.ι` with the product preorder (`Prod.instPreorder`
**to verify**), `directed` from both factors, componentwise `map`, `comp_E`/`comp_P` by `Prod.ext`. Theorems:
`SCInf (prod DA DB) ← SCInf DA ∧ SCInf DB` (multiplicative table), `val_prod : val (prod) ⟨(i,j),(a,b)⟩ ⟨(i',j'),(x,y)⟩
= val DA ⟨i,a⟩ ⟨i',x⟩ * val DB ⟨j,b⟩ ⟨j',y⟩` (needs SC∞ on both: read at the chosen upper stage, then `val_eq_at`
SC:117), `BinaryVisible (prod) ← BinaryVisible DA` (`v_k ⊗ unit`). Register attachment is the `StageMap`
`attach r₀ : StageMap S (S.prod R)` with `onP x := (x, r₀)`, `onE e := (e, R.unit)`, and it is `Consistent`
(`S.p e x * 1`). **Finding:** discard is *not* a `StageMap`: `StageMap` (SC:53) carries effects and preparations in
the *same* direction, while discard marginalizes preparations (`S×R → S`) and embeds effects (`S → S×R`). A
stage-level discard needs a new two-directional arrow (`onP : T.P → S.P`, `onE : S.E → T.E`, consistent); it is
definable for the product stage (`fst`, `(·, R.unit)`) but adds vocabulary.

**Verdict on (i):** it sources exactly the *minimal* composite — product preparations and product effects only. No
entangled preparation can arise from a product of stage towers, so (i) cannot be the interface the qubit composite
needs; it is the right *instance generator* for the weak version's controls and for a later bridge theorem
(§5 strong version), and the right place for the attach `StageMap`. Not the interface.

### 2.2 Candidate (ii) — composite of two chart bodies (body level) — **chosen**

Carrier conventions: factor bodies live in finite-rank chart coordinates `Fin dA → ℝ`, `Fin dB → ℝ` (what
`CompletionChart` CA:144 / `exists_chart_of_finiteRank` SC:304 deliver); the composite carrier `V` is an arbitrary
real vector space, **not** `TensorProduct`, not a function space by fiat. Lean-style (sketch; `1` is
`AffineMap.const ℝ _ (1:ℝ)`, `coordA i : (Fin dA → ℝ) →ᵃ[ℝ] ℝ` is `(LinearMap.proj i).toAffineMap`):

```lean
structure Composite {dA dB : ℕ} (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) where
  V : Type
  [grp : AddCommGroup V] [mod : Module ℝ V]
  Ω : Set V
  convex : Convex ℝ Ω
  -- product states: bi-affine, lands in Ω on ΩA × ΩB
  prodState : (Fin dA → ℝ) → (Fin dB → ℝ) → V
  prodState_affL : ∀ y x x' (a b : ℝ), a + b = 1 →
    prodState (a • x + b • x') y = a • prodState x y + b • prodState x' y
  prodState_affR : ∀ x y y' (a b : ℝ), a + b = 1 →
    prodState x (a • y + b • y') = a • prodState x y + b • prodState x y'
  prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω
  -- product effects: bilinear pairing into affine functionals of V
  prodEff : ((Fin dA → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin dB → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ)
  prodEff_apply : ∀ e f x y, prodEff e f (prodState x y) = e x * f y
  prodEff_effect : ∀ e f, IsEffectOn ΩA e → IsEffectOn ΩB f → IsEffectOn Ω (prodEff e f)   -- Ω ⊆ max
  prodEff_unit : ∀ ω ∈ Ω, prodEff 1 1 ω = 1                                                 -- normalization
  -- local tomography, as a named field (PREMISE)
  lt : ∀ ω ∈ Ω, ∀ ω' ∈ Ω,
    (∀ e f, IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω') → ω = ω'
```

Derived operations (definitions, no new fields):

```lean
def attach (C : Composite ΩA ΩB) (r₀ : Fin dB → ℝ) : (Fin dA → ℝ) →ᵃ[ℝ] C.V      -- x ↦ prodState x r₀
def margA  (C : Composite ΩA ΩB) : C.V →ᵃ[ℝ] (Fin dA → ℝ)                           -- ω ↦ (i ↦ prodEff (coordA i) 1 ω)
def readout (C : Composite ΩA ΩB) (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) : C.V →ᵃ[ℝ] ℝ := prodEff 1 (f k)
def condA  (C : Composite ΩA ΩB) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : C.V) : Fin dA → ℝ   -- i ↦ prodEff (coordA i) f ω / prodEff 1 f ω
abbrev JointReversible (C : Composite ΩA ΩB) (G : Set (C.V ≃ᵃ[ℝ] C.V)) : Prop := PreservesBody C.Ω G   -- OG:69
```

`attach` is affine by `prodState_affL`; `margA` is affine because each `prodEff (coordA i) 1` is (`AffineMap.pi`
**to verify**, else build from `AffineMap.decomp`). `margA` is *defined* in chart coordinates; the only use of the
basis is reflexivity of `Fin dA → ℝ`.

Laws, with their status:

| law | statement | status | proof idea |
|---|---|---|---|
| L1 marginal of a product | `y ∈ ΩB → margA (prodState x y) = x` | **theorem** | coordinatewise `prodEff_apply`, `1 y = 1` |
| L2 attach-then-discard | `r₀ ∈ ΩB → ∀ x, margA (attach r₀ x) = x` | **theorem** | L1 |
| L3 marginal pairing | `ω ∈ Ω → ∀ e, e (margA ω) = prodEff e 1 ω` | **theorem** | `e = e 0 • 1 + ∑ᵢ (e.linear (Pi.single i 1)) • coordA i` in the module `(Fin dA → ℝ) →ᵃ[ℝ] ℝ` (**to verify**: `AffineMap.instModule`/`AddCommGroup` on affine maps into a module), linearity of `prodEff` in `e`, `prodEff_unit` |
| L4 marginal is a state | `IsCompact ΩA → Convex ℝ ΩA → ω ∈ Ω → margA ω ∈ ΩA` | **theorem** (conditional on compactness) | if `margA ω ∉ ΩA`, separate by an affine `e` with `e (margA ω) < 0 ≤ e` on ΩA (`geometric_hahn_banach_point_closed` **to verify**), rescale by `IsCompact.exists_isMaxOn` to make `e` an effect on ΩA; then `prodEff e 1 ω < 0` contradicts `prodEff_effect`. This is the GPT fact "`Ω ⊆ max` ⇒ marginals are states" |
| L5 readout is a test | `PerfectlyDistinguishable ΩB ![y0,y1] ![f0,f1] → ∀ ω ∈ Ω, readout f 0 ω + readout f 1 ω = 1` | **theorem** | `f0 + f1 = 1` on ΩB only; need `f0 + f1 = 1` *as functionals* — **gap**: `PerfectlyDistinguishable` (KF:154) gives the sum on ΩB only. Either add the hypothesis `f 0 + f 1 = 1` (functional equality; true when ΩB spans the chart, `affineSpan_gen` CA:218 + `AffineMap.ext_on`) or state L5 on the image `prodState '' (ΩA ×ˢ ΩB)` only. Recommend the functional hypothesis, derived once from `affineSpan ℝ ΩB = ⊤` |
| L6 readout factorizes | `readout f k (prodState x y) = f k y` for `x` with `1 x = 1` (always) | **theorem** | `prodEff_apply` |
| L7 readout after attach is certain | `readout f k (attach (y k) x) = 1` given `f k (y k) = 1` | **theorem** | L6 |
| L8 conditional state is a state | `readout f k ω ≠ 0 → ω ∈ Ω → IsEffectOn ΩB (f k) → condA (f k) ω ∈ ΩA` (ΩA compact convex) | **theorem** | L4's argument with `prodEff e (f k) ≥ 0` |
| L9 no-signalling on products | `f y ≠ 0 → condA f (prodState x y) = x` | **theorem** | `prodEff_apply`, `div_self` |
| L10 reversible actions compose | `PreservesBody Ω G → PreservesBody Ω (words G)` | **theorem** | `Subgroup.closure_induction` (**to verify**) on ON:53's `words`; one-step cases from the definition |
| L11 LT embeds in the max body | `Function.Injective (fun ω : Ω => fun e f => prodEff e f ω)` and `minBody ⊆ Ω ⊆ maxBody` (defs §4) | **theorem** | `lt`, `prod_mem`, `convex`, `prodEff_effect`, `prodEff_unit` |
| P-LocalExt (not a law of the structure) | `∀ g, PreservesBody ΩA {g} → ∃ ĝ, PreservesBody Ω {ĝ} ∧ ∀ x y, ĝ (prodState x y) = prodState (g x) y` | **premise** | existence needs the universal property of a tensor product (every bi-affine map factors); positing it is the fiat the charter forbids — named, not consumed in round 1 |

### 2.3 Candidate (iii) — the corpus's other framings

- NB-1's preregistration frames the composite as cones `ℝⁿ ⊗ ℝⁿ`, `min = cone(L ⊗ L)`, `max` its dual (NB-1
  prereg lines 178–181), with `G` a linear map of `ℝⁿ ⊗ ℝⁿ`. That is (ii) in cone form with the carrier fixed to a
  tensor product; the kernel never typed it (NGB works in blocks). (ii) is its affine-section version with the
  carrier abstract.
- `FiniteOperationalTheory`'s `A × Fin n` levels field-neutralized (stages indexed by a classical register size):
  rejected — a register is `Fin n`, not a second body; it cannot type two balls (RESULT §6.10).
- Thread P's `(eff, trans)` availability record (FRONTIER F9): orthogonal (single-system availability); COMP-1 does
  not need it.

***

## 3. Separation: defined / premise / theorem / deferred

**(A) Definable field-neutrally now.** `FiniteStage.prod`, `DirectedStages.prod`, `attach` (stage level, a
`Consistent StageMap`); the structure `Composite`; `attach`, `margA`, `readout`, `condA`, `JointReversible`;
`minBody ΩA ΩB := convexHull ℝ (prodState '' (ΩA ×ˢ ΩB))` and `maxBody := {ω | prodEff 1 1 ω = 1 ∧ ∀ e f effects,
0 ≤ prodEff e f ω}` for any `Composite` (and the concrete function-space model `Fin (dA+1) → Fin (dB+1) → ℝ` in
§4); the control instances of §7.

**(B) Named premises (structure fields or hypotheses, never concluded).** F13-LT: `lt`; composite existence:
`Nonempty (Composite ΩA ΩB)` with `Ω ⊋ minBody` (no field-neutral source — every construction in (A) gives `min` or
`max`); F14: existence of a nonlocal reversible `G` (`PreservesBody Ω G` with a stated nonlocality witness);
F15 common `N`: `CopyNatural N_A N_B e` (KF:284) on `Composite ΩA ΩA`; P-LocalExt; compactness/convexity of the
factor bodies (F3 adapter) where L4/L8 need them; availability of the derived operations (SEQ/TRANS±-type, F9–F11)
— *not typed in COMP-1 at all*, so no law here says anything is *available*.

**(C) Theorem candidates for COMP-1 itself.** L1–L11 above; `SCInf_prod`, `val_prod`, `attach_consistent`,
`binaryVisible_prod` at stage level; non-vacuity: the two instances build the structure; non-redundancy: `lt` is
not implied by the other fields (the padded control of §7).

**(D) Deferred to the complex-composite classification.** Which `Ω` between `min` and `max` is the physical one
(K2); NB-1's gate relations as equations on a `Composite` instance (`G (prodState kₐ k_b) = prodState kₐ k_{a⊕b}`,
`(I⊗N)G(I⊗N) = G` typed through `LocalExt`), hence `d ∈ {1,3}`; readout *with state update* and its Lüders form
(the field-neutral analogue of `readout_is_localLuders`); the Bloch adapter (F18) identifying the two-qubit `Ω`;
functoriality across *three* factors (associativity of `prod`, needed for K2's "composition is functorial"); the
reverse-direction instance "the quantum two-qubit body is a `Composite`" beyond `min`/`max`.

***

## 4. Anti-circularity audit

For each ℂ-typed object considered: `FiniteOperationalTheory` (OA:594) fixes the carrier `Matrix (A × Fin n) ℂ`, so
any premise read off it presupposes the quantum tensor product and a classical register, not a second system;
`local_tomography_physical` (ID:440) is a theorem *about* `Matrix (A × B) (A × B) ℂ` — using it for `lt` would be
proving LT from the Kronecker carrier that LT is supposed to select; `tensorOf`/`kronId`/`prodProj` define
products *by* the Kronecker formula; `ptraceAnc`/`discardWith` define discard *by* the partial trace;
`HasParallelReferenceExtension`/`ObservationalIndependence`/`InertSpectatorCompositionality` state spectator
inertness for ℂ-channels on `A × Fin n`; `HasCompositeUnitaryControl`/`PhaseFreeRichness`/`IteratedAncillaClosure`
are the K2-side conditions; `MapSpectatorIndependent`→`readout_is_localLuders` derives the readout form by spanning
with matrix units (OA header §B) — the spanning argument is exactly the tensor-product fact we refuse to assume.
None is imported; the import whitelist in §6 enforces it mechanically. `nb1_kernel_core` is real-typed but a block
lemma; consuming it would not be circular, but it supplies no composite notion, so COMP-1 does not import NGB.

**Tensor product check.** The proposal has no primitive of the form `V_A ⊗ V_B`: `V` is a structure field; the
only product-shaped objects are the bi-affine `prodState` and bilinear `prodEff`, both fields with laws, not
constructions. `minBody`/`maxBody` are defined from `prodState`/`prodEff` (`convexHull` of product states; the set of
normalized points nonnegative on product effects). The concrete carrier used by the instances,
`Fin (dA+1) → Fin (dB+1) → ℝ` with `prodState x y := fun μ ν => x̂ μ * ŷ ν` (`x̂ := Fin.cons 1 x`) and
`prodEff e f ω := ∑ μ ν, ê μ * f̂ ν * ω μ ν` (`ê` the coefficients of `e` in the basis `1, coordA i`), is a function
space on index pairs — it *realizes* a tensor product but is written as a function type; §7 flags this as the one
place where "tensor product by another name" is a fair criticism, and why it is confined to *instances*, never to
the interface. LT is **not** derived from this carrier: on the abstract `Composite` it is a field; on the concrete
instances it is a theorem about *those* instances (coordinates are product-effect values).

**Where the fiat now sits.** Composite existence beyond `min` (F13), P-LocalExt (the universal property), and `lt`
are the three places structure is *assumed*. All three are named; none is concluded by any theorem of the round
(guard S2/S3).

***

## 5. Two versions

**Strong (derived from composition principles).** Composite preparations/effects come from the observer's own
stage towers: `DirectedStages.prod` with `SCInf_prod`, completed by CMP-1, charted by OPACT-1, and shown to be an
instance of `Composite` (bridge theorem: `body (prod DA DB)` in a product chart satisfies the fields, with
`prodState` the pointwise product of preparation vectors and `prodEff` on coordinates). Hypotheses: `SCInf DA`,
`SCInf DB`, `FiniteRank` of both bodies and of the product body, the F3 compactness adapter. **What it proves:** the
*minimal* composite exists and satisfies L1–L11 with no composite premise. **What it cannot prove:** any `Ω ⊋ min`,
`lt` for a *joint* tower (a joint stage tower with non-product preparations is an OI-construction object — L3B
territory, absent at the base: DEPENDENCY §0 "any `DirectedStages` instance built from an OI construction:
absent"), `LocalExt`, any nonlocal `G`. So the strong version is honest but delivers only the separable composite;
it is the second execution round's bridge, not the first's.

**Weak (explicit composite package).** The structure `Composite` with its nine fields as the package; theorems
L1–L11; instances `bitComposite` (min = max) and `ball3MinComposite`, `ball3MaxComposite`; the LT-padding control.
Hypothesis list = exactly the structure fields plus, per theorem, `IsCompact ΩA ∧ Convex ℝ ΩA` (L4, L8), a
`PerfectlyDistinguishable` register pair with functional sum `1` (L5–L7), `PreservesBody` (L10). No availability,
no `G`, no `N`, no `d`.

**Recommendation:** the first execution round targets the **weak** version (types + provable laws + instances),
exactly as CMP-1 and OPACT-1 did for their layers; the strong version's bridge theorem is COMP-2, after the F3
chart-compactness adapter lands (it is needed by L4 anyway and by the TRANS/IIP route of OWNER-AMENDMENT-1 §2).

***

## 6. Dependency map, guards, freeze boundary, outcomes, Mathlib names

**Dependencies (all landed at the base).** Imports: `OIBridge.StageCompletion` (for `FiniteStage.prod`,
`DirectedStages.prod`, and transitively KF, OG, ON), `OIBridge.CompletionAction` (only if the chart-body
`CompletionChart` is referenced in round 1 — recommend *not*, keep `Fin d → ℝ` bare). Not imported: NGB, IIP, any
ℂ module. No dependence on TRB-1/ORD-1 (absent at the base; nothing here concerns transitivity, ORD∞, or the
ball). Consumers downstream: COMP-2 (strong bridge), a future NB-1-on-`Composite` round, K2.

**Semantic guards for `controls.py` (IIP-1 style: `check(code, name, cond)` over `split_statement` of each frozen
declaration, cf. IIP-1 `controls.py:393–427`):**
- **S1 field-neutral.** The module text contains none of `ℂ`, `Complex`, `TensorProduct`, `⊗ₜ`, `⊗ₖ`,
  `kroneckerMap`, `Kronecker`, `Matrix.trace`, `Hilbert`, `InnerProductSpace`; its `import` lines are a subset of the
  whitelist `{OIBridge.StageCompletion, OIBridge.CompletionAction, Mathlib.*}`.
- **S2 premises named, never concluded.** `lt`, `prodEff_effect`, `prod_mem`, `prodEff_unit` occur only as
  structure fields or as hypotheses; no theorem's conclusion is `C.lt …`, `Nonempty (Composite …)` or
  `PreservesBody … {g}` for a non-control object, except the named instance declarations (`bitComposite`,
  `ball3MinComposite`, `ball3MaxComposite`) and the padding control.
- **S3 no fiat tensor.** No `def`/`structure` whose body mentions `TensorProduct`; `minBody` is defined by
  `convexHull ℝ (… prodState …)` and `maxBody` by a set-builder over `prodEff`; `prodState`/`prodEff` are structure
  fields of `Composite` and are defined only inside the named instances.
- **S4 scope.** No declaration name, theorem conclusion or header claim about `d = 3`, CNOT, a nonlocal gate's
  existence, "quantum tensor product", Bell, K2, availability, a drive, transitivity or a dimension; header carries
  the disclaimer "nothing here constructs a composite larger than the minimal body, sources local tomography, or
  identifies the quantum composite".
- **S5 laws are theorems.** `margA_prodState`, `attach_margA`, `margA_eff`, `margA_mem`, `readout_test`,
  `readout_prod`, `readout_attach`, `condA_mem`, `condA_prod`, `preservesBody_words`, `lt_injective_max` are of kind
  `theorem` with their `#print axioms` lines; `margA`, `attach`, `readout`, `condA` are `def`s, not fields (the
  mutation "make discard a field" must fail S5).
- **S6 non-vacuity and non-redundancy.** The three instances elaborate; the control `¬ (∀ ω ω' ∈ paddedΩ, … → ω = ω')`
  (the LT-padded composite) is a theorem — so `lt` is not implied by the other eight fields.
- Plus the standard P, N1–N3, I, C, F as in CMP-1/IIP-1.

**Freeze boundary.** In scope: new module `OIBridge/CompositeInterface.lean`; the import line inserted directly
after `import OIBridge.CompletionAction` (OIBridge.lean:251); one `kernel-only` census family after the OPACT-1
family; `controls.py`; result note. Frozen out: any source of LT or of a composite beyond `min`; any nonlocal `G`,
`N`, `d`, CNOT, Bloch adapter; readout with update; `LocalExt` as a definition (it may be *named* in the header as
a premise only); availability; any edit to NGB, OA, ID, MC, CO or manuscripts/ROADMAP.

**Outcomes vocabulary.** `COMP-1-INTERFACE-PROVED` (controls OK at `E`, every frozen `#print axioms` within
`[propext, Classical.choice, Quot.sound]`, result note states: LT is a field, composite existence beyond `min` is
not sourced, the instances are `min`/`max`/classical only); `COMP-1-HALTED` (anything else, under `S12`). If L4/L8
cannot be closed with the pinned Mathlib, they are dropped from the frozen surface *before* `F` (a type round's
surface must be exactly what compiles), not weakened after.

**Mathlib names to verify (v4.33.0).** `AffineMap.instModule` / `AddCommGroup (P →ᵃ[k] V)`; `AffineMap.pi`;
`AffineMap.ext_on` (used CA:256, exists); `AffineMap.decomp` (used CA:87, exists); `Convex.combo_affine_apply`
(used SC:184, exists); `geometric_hahn_banach_point_closed` or `geometric_hahn_banach_closed_point`;
`IsCompact.exists_isMaxOn`; `Subgroup.closure_induction` (statement shape changed across versions);
`convexHull_min`, `subset_convexHull` (used SC:168/173, exist); `Prod.instPreorder`/`Prod.le_def`; `mul_le_one₀`
vs `mul_le_one'`; `Finset.sum_mul_sum`; `Fin.cons`, `Fin.sum_univ_succ`; `LinearMap.proj`; `Pi.single`.

***

## 7. Risks and the minimal first execution round

**Where typing is likely to fail.** (a) `prodEff` as an iterated `→ₗ[ℝ]` into `V →ᵃ[ℝ] ℝ` needs the module
instance on affine maps; fallback: a plain function with four additivity/homogeneity laws (more fields, same
content). (b) `prodState` bi-affine as a function with two laws is robust; the alternative
`(Fin dA → ℝ) →ᵃ[ℝ] ((Fin dB → ℝ) →ᵃ[ℝ] V)` is cleaner but doubles the instance risk. (c) L3 needs the basis
expansion of an affine functional on `Fin d → ℝ`; elementary but fiddly (`Finset.sum` over `Pi.single`). (d) L4/L8
depend on a Hahn–Banach name and compactness; if awkward, state them with the hypothesis "`ΩA` is the intersection
of its effect half-spaces" (`∀ x, (∀ e, IsEffectOn ΩA e → 0 ≤ e x) → x ∈ ΩA`) and prove that hypothesis for the
instances — this keeps L4 a theorem of the structure and moves the analysis to COMP-2. (e) L5 needs the functional
identity `f 0 + f 1 = 1`, which `PerfectlyDistinguishable` does not give; derive it from `affineSpan ℝ ΩB = ⊤` or
take it as a hypothesis.

**Where structure could be smuggled.** The concrete carrier `Fin (dA+1) → Fin (dB+1) → ℝ` of the instances is a
tensor product written as a function type; keep it out of the interface (S3) and say so in the header. `margA`
uses the coordinate basis — innocuous (reflexivity of finite-dimensional spaces), but L3 is what certifies
basis-independence; freeze L3. `prodEff_effect` + `lt` + `convex` is silently "`min ⊆ Ω ⊆ max`" — fine, but it means
the structure already *excludes* non-LT theories (real QM); the header must say the interface is LT-only by choice
of premise, and the padded control shows the choice is a choice. Nothing in the structure says the composite is
*available* or *unique*; two composites of the same factors can differ (min vs max) — L11 says only that each
embeds in max. "Sharp readout" here is an effect pair, not an instrument; no state update is typed.

**Minimal first execution round (recommended content).** One module: `FiniteStage.prod`, `DirectedStages.prod`,
`SCInf_prod`, `attach` (stage) + `attach_consistent`; `Composite`; `attach`, `margA`, `readout`, `condA`;
theorems L1, L2, L3, L6, L7, L9, L10, L11 (robust), L4, L5, L8 (if the names check out before `F`, else dropped);
instances: `bitComposite : Composite simplex2 simplex2` (classical bit × bit in `Fin 2 → ℝ` probability
coordinates, `Ω` the 4-simplex, where `min = max` and `lt` is a theorem), `ball3MinComposite`,
`ball3MaxComposite : Composite ball3 ball3` (KF:311) on `Fin 4 → Fin 4 → ℝ`; the LT-padding control
(`V × ℝ`, `Ω := Ω_min ×ˢ Icc 0 1`, products at `0`, `lt` fails). Not in round 1: the two-qubit *quantum* body
(needs PSD of a 4×4 Hermitian matrix in real Pauli coordinates — definable without `ℂ` but an adapter of its own),
any `G`, `N`, `d`, update rule, availability, the strong bridge. Expected size ≈ 450–600 lines, comparable to
CMP-1 (460) and CA (539).
