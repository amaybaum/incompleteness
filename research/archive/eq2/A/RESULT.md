# EQ2-A — operational equivalence across all finite composites, and the IE₂ bridge (design only)

Research and design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (manifest re-checked:
1317 files, no mismatch). Nothing here is adopted, frozen or governed. No Lean was built (no toolchain); every Lean
text is **UNBUILT** — the full candidate text is `EQ2A.candidate.lean`. "Kernel" means a landed identifier at
`bcbc516f` with `file:line` (paths under `verification/lean-mathlib/OIBridge/`). "Exact" means certified by a script
in this directory with exact arithmetic over green controls. "Written" means a proof on paper here. Floating-point
runs are labelled exploration and certify nothing. Running record: `NOTES.md` (productivity test N1, reading record
N2, inventory N3, node log N4).

Abbreviations: CD CompositeDimension, CI CompositeInterface, K2G K2Guard, RE ReferenceExtension, SB SpectatorBridge,
TC TypedCompletion, OA OperationalAssembly, CGOP CarrierGeneralOIPlus, COI CompletedOI, IL ImplementationLocality,
OS OrientationSelection. `Q` = Q3 (PSD two-qubit Pauli tables), `Tw = actT reflY '' Q` (the twin), `T` the global
transpose, `τ_ij` the native twist bit of the pair composite `{i,j}`.

## 1. Finding

The general theorem is designable without CX and without a fixed orientation per system type, but only with a coupling
principle that native observational independence does not supply. **Layer (I)** is formal once coherent charts are
given. The Pauli/twin package is fixed against the kernel definitions, and every identity it uses is exact (48/48).
The typed bridge is two lines: `TypedIdleExtension` plus the landed `relabel` rule and the landed `rfl`
`withSpectator R e Φ = transportT e e (amplRefL R Φ)` give `HasParallelReferenceExtension` of every shadow. Native IE₂
is equivalent to spectator closure of the presented family at the qubit-power, deterministic instance (17/17).
**Layer (II-3)** has a conditional all-copy theorem: H0, H1, H2, a spanning tree, and Theorem A′'s group-level
conclusion on each tree edge give per-token charts with `K_S = PSD_S`, unique up to the global transpose. Its Lie-free
route (exact universality: Givens, Gray code, Barenco, square roots, SWAP routing) holds exactly on instances (27/27,
8/8; end to end, a two-level unitary on (000,111) is an exact product over ℚ(i) of 53 gates, each on an edge of the
path 0–1–2).
**A4 (key question).** IE₂ is not derivable from the native statements the base supports. They are all at most
two-copy, and their n-token transports hold in exact three-copy countermodels that admit no coherent chart. The
transports are: marginal consistency H0, products of states and of effects on every pair|single bipartition,
conditional closure, local tomography, IE₁, exchange symmetry, pair-level CX, and entangling interactions on every
pair composite. The countermodels are the odd-cycle hull `M_odd`, equivalent to the S₃-symmetric all-twisted hull
`M_tw` (no per-token chart even for the pair composites), and the biseparable hull `M_bs` (pair-CX holds, but GHZ lies
outside every per-token image). IE₂ fails in all three: `(cnot on 01) ⊗ id` sends the generator `|+⟩⟨+| ⊗ Φ⁺₁₂` of
`M_odd` and `M_bs` to GHZ′, which pairs to −1/2 with a functional nonnegative on every generator; in `M_tw` the same
failure appears after transport by the reflection of copy 1. IE₂'s weakening to positivity on product effects is
automatic, so no product-effect test can detect the failure. The load-bearing coupling is IE₂ in **closure** form for
the interaction groups on a spanning tree. It has two separately witnessed roles: the parity rule and generation.
Part of it is kinematic. COMP-1 on 2|2 bipartitions, with all effects of the pair composites, forces every 4-cycle of
twist bits to be even, i.e. `τ = δε + c` (exact). That leaves one global bit `c`, which no test with factor bodies of
at most two tokens fixes. The six-copy 3|3 test forces (co-)self-duality of the three-copy composite (written; the
link identities are exact). The untwisted hull fails it (exact). The all-twisted hull `B_tw` contains the GHZ witness (`W ∈ B_tw`, exact) and still fails it:
`F = ½(1 − |000⟩⟨000| − |111⟩⟨111|) + (|000⟩⟨111| + h.c.)` and its local-unitary image `G = Ad_{S⊗S⊗1} F` both lie in
`B_tw*`, and `tr(FG) = −½` (exact). So when `c = 1`, the three-copy composite must satisfy `B_tw ⊊ K₃ = K₃* ⊊ B_tw*`.
Whether a local-unitary-invariant `K₃` of that kind exists is the named wall. The one-orbit argument does not close
it: `F + 1/10` lies in `B_tw*` but not in `B_tw`, and it pairs at least 9/50 with every unitary image of itself
(written bound; value, tightness and controls exact).
**Classification of A4:** INDEPENDENT PREMISE, with exact countermodels; THEOREM ROUTE for the product-effect shadow
(no content) and for 4-cycle parity (kinematic); OPEN beyond that (self-duality wall).
**A4(c):** an exact three-copy model with an odd twist cycle exists (`M_odd`; reflecting copy 1 gives the S₃-symmetric
`M_tw`). It satisfies H0, H1, H2, admissibility and pair interactions, and it has no coherent chart. CX does not
substitute for the coupling (`M_bs` satisfies pair-CX and has no chart at three copies). Of the principles examined,
tree-IE₂ in closure form is the one shown sufficient; whether KT∞ can replace it is the open wall.

## 2. Target theorems (Lean-level, UNBUILT; full text `EQ2A.candidate.lean`)

| id | statement (abbreviated) | layer | direction |
|---|---|---|---|
| **TA1** Pauli/twin package | `pauliW (ω : W 3) := (1/4) • ∑ μ ν, (ω μ ν : ℂ) • tensorOf (pauli1 μ) (pauli1 ν)`, `pauli1 = ![1, X, Y, Z]` (index 0 the unit; `tensorOf` MonoidalCompletion:193 = `⊗ₖ`). `pauliW_prodState : pauliW (prodState x y) = tensorOf (rho x) (rho y)`; `pairVal_eq_trace : (pairVal a b ω : ℂ) = trace (tensorOf (effOp a) (effOp b) * pauliW ω)`; `pauliW_injective`; `Q3 := {ω \| (pauliW ω).PosSemidef}`; `phiW_mem_Q3`; `candidateCone_Q3 : CandidateCone Q3` (K2G:95); `transposeW` (explicit: `sgnY μ * sgnY ν * ω μ ν`, `sgnY = ![1,1,-1,1]`), `actC_actT_reflY : actC reflY (actT reflY ω) = transposeW ω`, `pauliW_transposeW : … = (pauliW ω)ᵀ`; `IsOrth`, `chart2 a b := actC a ∘ actT b`, `PresentedBy K a b := IsOrth a ∧ IsOrth b ∧ chart2 a b '' K = Q3`; `twin := actT reflY '' Q3`; `twin_presentedBy : PresentedBy twin id reflY`; `chart2_idW (ha : IsOrth a) : chart2 a a idW = idW`; `idW_not_mem_Q3`; `idW_mem_twin := ⟨phiW, phiW_mem_Q3, actT_reflY_phiW⟩`; `twin_not_uniformlyPresented : ¬ ∃ a, PresentedBy twin a a`; `swapW_image_twin : swapW '' twin = twin`; `chart_swap_twin : chart2 id reflY (swapW (chart2 id reflY ω)) = transposeW (swapW ω)`; three copies: `pauli3`, `QABC`, `idleExt₁₂`, explicit `ω₀` (= \|0⟩⟨0\| ⊗ Φ⁺), `idleExt_transposeSwap_not_mem : idleExt₁₂ (transposeW ∘ swapW) ω₀ ∉ QABC`, control `idleExt_swap_mem` | (I) ingredients | forward (two tokens) + converse (the twin is QM under a per-token chart) |
| **TA2** conditional all-copy theorem | native vocabulary over token **sets** `S : Finset Tok` (no type-level identification of tokens): `NC S := (S → Fin 4) → ℝ`, `uN`, `prodStateN`, `pairValN`, `maxConeN`, `margN` (= conditioning on unit effects = restriction of the table), `idleExt (h : S ⊆ S')`, `actAt`, `chartN S ε`, `pauliN`, `PSDN`; `structure NativeFamily` (convex cone, H1a products, H1b ⊆ max, **H0** `margN h '' K S' = K S`, **H2** local SO(3) at every composite); `EdgeGroupHyp F Γ τ` (Theorem A′ in group form with IE₂: after reflecting the second token when `τ i j`, every `adPair i j U`, `U ∈ unitaryGroup`, maps `K S` onto `K S`). `allCopy_charts (hΓ : Γ.IsTree) (hE : EdgeGroupHyp F Γ τ) : ∃ ε, ∀ S, chartN S ε '' F.K S = PSDN S`; `coherentCharts_unique : (∀ t, ε₁ t = ε₂ t) ∨ (∀ t, ε₁ t ≠ ε₂ t)` | (II-3), **conditional on (II-2)** | forward |
| **TA2-U** Lie-free universality | U1 two-level decomposition; U2 Gray code; U3 Barenco Lemma 6.1 and Lemma 7.2 recursion; U4 every 2×2 unitary has a unitary square root; U5 SWAP routing; U6 `Subgroup.closure {edge gates} ⊇ unitaryGroup (S → Fin 2) ℂ` | (II-3) generation step | forward |
| **TA3** typed bridge | `TypedIdleExtension 𝒯 := ∀ S S' R O F, 𝒯.availT S S' O F → 𝒯.availT (R × S) (R × S') O (amplRefL R ∘ F)`; `shadow_parallelReferenceExtension (h) (A) : HasParallelReferenceExtension (𝒯.shadow A)` (proof: `exact 𝒯.relabel _ _ _ _ e e O _ (h (A × Fin n) (A × Fin n) R O F hF)`); `shadow_observationalIndependence` (CGOP:73); `typedDiag_typedIdleExtension`; B1 `presentN_comp`, `presentN_injective`, `presentN_idleExt : presentN (idleExtSum R g) = transportT eRS.symm eRS.symm (amplRefL (R → Fin 2) (presentN g))`, `eRS := Equiv.sumArrowEquivProdArrow R S (Fin 2)`; B2 `nativeIE_iff_presentedIdleClosed` (family over `Finset Tok`, deterministic maps) | (I), conditional on coherent charts | forward; B2 both directions, each witnessed (⇒ B1; ⇐ B1 + injectivity) |
| **TA4** coupling limits | three-copy hulls `K_τ`, τ ∈ {0,1}³: `pairHull_H0/H1/H2/comp1/conditional`; `oddCycle_no_chart` (τ = (0,1,0)); `pairHull_not_IE2` (GHZ′ with witness `W′ = ½ − GHZ′`); `biseparable_no_chart` (GHZ ∉ χ_ε K_(0,0,0) for all ε); `ie2_productEffect_automatic : (a⊗b⊗c)((g ⊗ id) ω) = (a⊗b)(g (cond_c ω))`; `kinematic_fourCycle_parity` (COMP-1 on 2\|2 ⇒ every 4-cycle of τ even ⟺ τ = δε + c, n ≥ 4); `ghzWitness_mem_twistedHull : ½ − GHZ ∈ K_(1,1,1)`; `twistedHull_dual_mem : F ∈ K_(1,1,1)* ∧ G ∈ K_(1,1,1)*` with `G = Ad_{S⊗S⊗1} F`; `twistedHull_not_selfDual : tr (F * G) = -1/2`; `no_LU_selfPositive_cone_contains : ¬ ∃ K, K ⊆ K* ∧ LU-invariant K ∧ F ∈ K`; `sixCopy_link_twin : ⟨E ⊗ F, ⊗ᵢ PT_{i+3} Φ⁺⟩ = tr (E * F) / 8`; `orbitObstruction_fails : x ∈ K_(1,1,1)* ∧ x ∉ K_(1,1,1) ∧ ∀ U ∈ unitaryGroup, 9/50 ≤ tr (x * U * x * Uᴴ)` for `x = F + 1/10` | (II-3) boundary | forward (no-go for the stated class) |
| **TA5** per-type (separate, D1) | `uniform_presentation_iff : (∃ e, ε ≡ e presents every pair) ↔ ∀ p, τ p = 0`; sufficient: EX + IE₂ for the interaction group (Theorem C parity), uniform composition + IE₂, CX (EQ-C Theorem B); not sufficient: EX alone (twin), EX + IE₂ for the exchange only (`M_tw`) | separate theorem | forward + countermodels |

Layer (I) stays explicitly conditional: TA1/TA3 are about given charts. Chart existence (layer II) is TA2, itself
conditional on Theorem A′ (II-2; written, EQ-C T3), on H0–H2 and on IE₂ along a tree. None of these is sourced.

## 3. Hypotheses ledger

"QM?" = does finite-dimensional complex QM satisfy it. Countermodels are exact unless marked.

| hypothesis | status | QM? | independence / necessity evidence |
|---|---|---|---|
| LT (built into `NC S`) | kernel premise at two copies: `Composite.lt` CI:243 | yes | kernel `no_composite_over_paddedPre` CI:895; real QM fails LT (EQ-E s7, exact) |
| convex cone, closed slice | unsourced (COMP-1 `convex` CI:226) | yes | `K_nc` (EQ-C prior, written) |
| H1a products are states | unsourced at n copies (two-copy field CI:227) | yes | definitional of a composite |
| H1b `K_S ⊆ max_S` | unsourced (CI:228 + `subset_maxBody` CI:467, transported) | yes | `B3` (EQ-C P5.2) |
| H0 composite consistency | unsourced; no native n-copy statement at the base | yes (partial trace) | foil: `K₂ = Q`, `K₃ = min₃` (marginal `min₂ ≠ Q`); without H0 charts of different composites are unrelated (written) |
| conditional closure | derivable from COMP-1 on the bipartition plus closedness (written; two-factor kernel `condA_mem` CI:431) | yes | — |
| COMP-1 on every pair\|single bipartition | unsourced transport of CI:223-230 | yes | holds in `M_odd`, `M_tw`, `M_bs` (a4 C5), so it does not imply IE₂ |
| H2 = IE₁ (local SO(3) at every composite) | unsourced (EQ-C: composite lift of `driveWords3`, OrbitNormalization:571, 667) | yes | `K_heis` (EQ-C P5.1) |
| spanning tree Γ of interacting pairs | unsourced | yes | forest closures (a2 G countercontrol, n ≤ 6; prior n = 7); one pair only: closure 18 (EQ-C P6.1b) |
| Theorem A′ (II-2), group form | written (EQ-C T3 + design v2 §4.2); Yamabe and the closed-subgroup theorem: literature, unverified | yes | enters TA2 as a hypothesis |
| normalization `u ∘ g = u` | written (Lemma COMPACT, design v2 §4.1) | yes | positive scalars (design v2) |
| **tree-IE₂, closure form** (idle extensions of the interaction groups map `K_S` onto `K_S`) | **unsourced** | yes for CP maps (a1 A1.12 control); no for antiunitary (a1 A1.12, EQ-C P6.2a) | **`M_odd`, `M_tw`, `M_bs` satisfy every row above it and fail it (a4 C9; `M_tw` through the reflection of copy 1)** |
| IE₂, product-effect form | **derivable** (a4 C12: Step 0 + conditional closure) | yes | carries no content: holds in `M_odd` while IE₂ fails |
| IE₂ for local maps / for the exchange only | unsourced | yes | insufficient: `M_tw` (a5 E6, a4 C7) |
| KT₂ = COMP-1 on 2\|2 bipartitions (all effects of the factor bodies, as COMP-1 quantifies) | unsourced | yes (a4 D3, τ = 0) | foil: odd-4-cycle hull, value −2 (a4 D1); consequence τ = δε + c (a4 D1–D2; written for every n) |
| KT∞ = COMP-1 on every bipartition | unsourced | yes (PSD is self-dual; written) | foils: untwisted pairwise hull, −1/16 at six copies (a4 D4); all-twisted pairwise hull, not self-dual (a4c L1–L3); consequence: `K₃ = Λ(K₃*)` (written, link identities exact in a4c L5), so for `c = 1` (with H0 and H2), `B_tw ⊊ K₃ = K₃* ⊊ B_tw*`; the one-orbit exclusion of such a `K₃` fails (a4d); OPEN whether KT∞ gives `c = 0`, `K = PSD` |
| EX (composites invariant under token permutations) | unsourced | yes | foil `M_odd`; insufficient: twin (two copies), `M_tw` (three copies) |
| CX | unsourced (EQ-C T4) | yes (EQ-C T5; a4 C11 path) | foils: twin (Choi 16), rebits, bits, min/max (EQ-C P4); insufficient for three-copy chart existence: `M_bs` (a4 C10, C11) |
| uniform composition | unsourced | yes | insufficient alone: `M_tw`; with IE₂: τ = 0 (a5 E5) |
| coherent chart family (C1–C6) | layer (I) hypothesis | yes (identity charts) | the twin has one (a1); `M_odd` has none (a4 C8) |
| `TypedIdleExtension` | new predicate (TC:165 has no such rule) | yes: typed Kraus closed under `amplRefL` (a3 B3.e; kernel `amplRef_conjChannel` RE:170) | foil: typed positive theory, transpose (a3 B3.d); `typedDiag` satisfies it (no quantum content) |
| typed `relabel` | kernel field TC:184 | yes | — |
| qubit-power carriers, deterministic families (B2 scope) | scope restriction | — | beyond: Kₙ / FP-O (EQ-D Theorem L, written; FP-O independent, `𝔐₁` exact) |

## 4. Missing lemmas

**Kernel vocabulary absent at `bcbc516f`** (grep at the base):
- No carrier with three or more copies. `W d` is two-copy (CD:97) and COMP-1 is two-factor (CI:210-246). No `pauliW`,
  `Q3`/`certW`, `swapW` or `transposeW` exists.
- Every native joint dynamics is `JointReversible` (CI:445: arbitrary affine maps of the joint body), with no notion of
  a local or idle map; `actT`/`actC` (CD:198, 201) are the only one-copy actions, at two copies.
- `TypedOperationalTheory` has no idle-extension rule (TC:165-200). `FiniteOperationalTheory` omits parallel extension
  "deliberately" (OA:594 docstring); its spectator property is `HasParallelReferenceExtension` (RE:447).
- No typed QM instance: only `typedDiag` (TC:916); EQ-E T3 (`typedKraus_theory`) is still open.

**Kernel lemmas reused:** `tensorOf` (MonoidalCompletion:193); `amplRef_tensorOf` (SB:98); `withSpectator_eq_transport`
(SB:381); `transportT_self` (TC:109); `relabel` (TC:184); `shadow_availExt` (TC:261); `psd_trace_mul_nonneg`
(OperationalRigidity:917); `psdFactorization_discharged` (BoundaryAudit:100); `actT_reflY_phiW` (K2G:106); `actT_actT`
(CD:471); `reflY_reflY` (K2G:73); `lor_ehom` (CD:930); `prodState_mem_maxCone` (K2G:165); `actT_prodState` (K2G:173);
`transpose_not_inner` (OS:239); `amplRef_conjChannel` (RE:170); `isSpectatorExtension_iff` (SB:188).

**Mathlib**, checked against a local checkout at tag `v4.33.0` (commit `db584cd6`, `git grep` on the tag tree; the
remote tag could not be confirmed): `Matrix.PosSemidef.kronecker` (Analysis/Matrix/Order.lean:213); `PosSemidef.
transpose/.submatrix/.smul/.add/.dotProduct_mulVec_nonneg/.trace_nonneg`, `posSemidef_vecMulVec_self_star`
(LinearAlgebra/Matrix/PosDef.lean:85/80/107/102/305/349/412); `Matrix.kronecker`, `trace_kronecker`,
`mul_kronecker_mul`, `conjTranspose_kronecker`, `kroneckerMap_transpose`, `kronecker_assoc`
(LinearAlgebra/Matrix/Kronecker.lean:274/398/382/408/64/388); `IsHermitian.spectral_theorem`, `eigenvectorUnitary`
(Analysis/Matrix/Spectrum.lean:141/87); `Matrix.unitaryGroup`, `orthogonalGroup`, `specialOrthogonalGroup`
(LinearAlgebra/UnitaryGroup.lean:60/295/315); `SimpleGraph.IsTree`, `IsTree.existsUnique_path`
(Combinatorics/SimpleGraph/Acyclic.lean:60/265); `Subgroup.closure` (Algebra/Group/Subgroup/Lattice.lean:329);
`IsAlgClosed.exists_pow_nat_eq` (FieldTheory/IsAlgClosed/Basic.lean:81); `Real.mul_self_sqrt`
(Analysis/Real/Sqrt.lean:149); `Equiv.sumArrowEquivProdArrow` (Logic/Equiv/Prod.lean:367); `Finset.piFinsetUnion`
(Data/Finset/Basic.lean:637). Not found under the searched names: a PSD trace-product lemma (the kernel's
`psd_trace_mul_nonneg` covers it), Yamabe's theorem, a closed-subgroup theorem for matrix groups, two-local
universality, Barenco-type decompositions — **unverified absence**.

**New lemmas to prove** (each with its exact certificate):
- A1: the TA1 list (a1 A1.1–A1.15).
- A2: Step 0 (a2b S0a/S0b); untwisting `T Ad_U T = Ad_Ū`, `PT_A Ad_U PT_A = PT_B Ad_Ū PT_B` (a2b S3a/b); the
  τ-twisted colouring of a tree (a2b S3d; via `IsTree.existsUnique_path`); U1–U6 (a2); cone bounds (spectral theorem);
  uniqueness through the Bell witness (a1 A1.7, A1.14).
- A3: B1 (a3 B1.a–d), pull-back (a3 B2), `PreservesDiag` under amplification (a3 B3.b).
- A4: the K_τ facts (a4 C1–C12, a4b K1–K5), the 4-cycle parity (a4 D1–D2), the six-copy value (a4 D4), the
  six-copy link identities and the failure of self-duality of `B_tw` (a4c L1–L5: sum-of-squares conditionals, the
  local-unitary relation, `tr(FG) = −½`, the one-family certificate `W = PT_1(ρ′)`), and the orbit bound for
  `F + 1/10` (a4d M1–M5; the bound itself is written: two rank-one parts, cross term at least −3/2).

## 5. Formalization strategy (rounds proposed for review; nothing is frozen)

| round | content | cost | controls / countercontrols a governed round needs |
|---|---|---|---|
| R1 `OperationalCharts` | TA1 (two tokens) | §B–§D cheap (`fin_cases`, explicit witnesses); §A moderate (Pauli algebra; `candidateCone_Q3` needs 2×2 PSD for \|x\| ≤ 1 and `PosSemidef.kronecker`) | control: chart (I,R) does not present Q3 (phiW ↦ idW); diag(2,1,1) does not fix idW; Q3 is uniformly presented by id; `idleExt_swap_mem`. Countercontrol: `T_AB ⊗ id` not positive |
| R2 `TypedIdleBridge` | TA3 | B3 cheap (two-line proof; `typedDiag` moderate); B1/B2 moderate (Pauli strings over a general `Fintype`, orthogonality `tr(P_s P_t) = 2ⁿ δ`, reindexing by `sumArrowEquivProdArrow`) | control: the `rfl` facts; foil: typed positive theory (transpose) fails `TypedIdleExtension`; countercontrol conj(H) ∉ PreservesDiag |
| R3 `NativeTokens` | TA2 vocabulary: `NC`, `margN`, `idleExt`, `actAt`, `chartN`, `pauliN`, Step 0, chart naturality | moderate | Step 0 symbolic certificate (a2b); product states ↦ ⊗ rho |
| R4 `CouplingLimits` | TA4 | `oddCycle_no_chart` cheap (ℤ/2 + two witnesses); hull facts moderate; the W′ witness moderate (4×4 PSD for every Bloch vector, by an explicit factorization); parity cheap (explicit tables, value −2); `twistedHull_not_selfDual` cheap (each conditional is block-diagonal with one 2×2 block, PSD by AM–GM for every one-qubit state; then `psd_trace_mul_nonneg`; one trace); `orbitObstruction_fails` cheap (one trace; the orbit bound from two rank-one projectors) | controls: D1 even cases nonnegative; M_bs presentable at pair level; the GHZ′ marginals; `W = PT_1(ρ′)` with `tr(WF), tr(WG) ≥ 0`. Countercontrol: coherence 2 leaves `B_tw*` |
| R5 `ExactUniversality` | TA2-U | **heavy but elementary** (explicit matrix identities, Givens with `Real.sqrt`, square roots via `IsAlgClosed.exists_pow_nat_eq`) | a2 certificates as CI-replayable probes; countercontrols (V^H → V; missing SWAP conjugation) |
| R6 `AllCopyCharts` | TA2 theorem from R3 + R5 + the `EdgeGroupHyp` hypothesis | moderate given R3, R5 | uniqueness witness (Bell, −1/2); forest countercontrol |
| R7 `PerTypeSeparation` | TA5 | cheap | twin and `M_tw` as countermodels |
| last | Theorem A′ itself (II-2): exact ingredients first (EQ-C T2 V1 classification as a probe), then the Lie glue | heavy (Lie route: Yamabe and closed-subgroup theorems not found in Mathlib) | as EQ-C |

Order: R1 → R2 (layer I closes, conditionally) → R3 → R4 and R7 (independent; they fix the limits) → R5 → R6 →
Theorem A′. **Route comparison for the generation step.** The Lie route needs Lie-algebra generation (the leaf-removal
Pauli closure: moderate), plus "an arcwise-connected subgroup whose Lie algebra contains su(N) is SU(N)" (Yamabe, or
the closed-subgroup theorem with exp-surjectivity). Neither was found at the pin, so that route is heavy and partly
blocked. The Lie-free route needs only finite products of explicit matrices plus two existence lemmas (2×2 square
roots, Givens steps), all with Mathlib support. Recommended: Lie-free for TA2. Theorem A′ itself still needs Lie
theory, which EQ-C's elementary-KAK remark may reduce for the explicit `cnot`.

## 6. Research questions

| question | classification | evidence / wall |
|---|---|---|
| A1 Pauli/twin package | **THEOREM ROUTE** | a1 48/48 exact: every identity the statements use, with T0 transcription and K landed-fact controls |
| A2 conditional n-token theorem | **THEOREM ROUTE**, conditional on (II-2) | written proof (design v2 §5 Steps 0–7, with the Lie-free generation); a2 27/27 (U1–U5, end-to-end 53-gate decomposition), a2b 8/8 (untwisting, colouring, Step 0); tree generation n ≤ 6 re-implemented independently, n = 7 replayed from prior work |
| A3 typed bridge | **THEOREM ROUTE** for B1–B3 within scope; **OPEN** beyond | B3: two-line proof on landed `relabel` and `rfl` facts; a3 17/17. Wall: non-qubit-power spectators and non-deterministic families need Kₙ/FP-O and kernel vocabulary for systems and faces (EQ-D) |
| **A4(b)** is IE₂ derivable from native observational independence? | **INDEPENDENT PREMISE** (closure form, tree of interaction groups) — exact countermodels `M_odd ≅ M_tw` and `M_bs`; **THEOREM ROUTE** for (i) its product-effect shadow (a4 C12; no content) and (ii) the 4-cycle part of its parity content from KT₂ (a4 D1–D2: τ = δε + c); **OPEN** for the rest | named wall: does KT∞ (COMP-1 on every bipartition) with H0–H2 and pair interactions force `c = 0` and `K_S = PSD_S`? The six-copy 3\|3 test gives the necessary condition `K₃ = Λ(K₃*)` (written; link identities exact, a4c L5). Both minimal candidates fail: the untwisted hull (a4 D4, −1/16) and the all-twisted hull, which contains the GHZ witness (a4b) yet is not self-dual (a4c: `F, G ∈ B_tw*`, `tr(FG) = −½`). Remaining question: is there a local-unitary-invariant self-dual `K₃` with `B_tw ⊊ K₃ ⊊ B_tw*` (it excludes `F`, `G`), and a tower above it? The one-orbit exclusion fails: `F + 1/10 ∈ B_tw* \ B_tw` pairs at least 9/50 with each of its unitary images (a4d), so `B_tw` has strictly larger LU-invariant extensions inside their own duals. The float exploration x3 reported no violation; that was a false negative, superseded by a4c |
| **A4(c)** is a coupling principle necessary for chart existence at three copies? | **COUNTEREXAMPLE** to "no coupling needed": `M_odd = K_(0,1,0)` satisfies H0, H1, H2, admissibility, LT, COMP-1 on every bipartition, conditional closure and pair interactions (cnot, cnot′ and flows), and no per-token chart presents its pair composites (a4 C8); `M_tw` adds EX; `M_bs` adds pair-CX and fails at the triple (a4 C10). **Load-bearing principle:** IE₂ in closure form for the interaction groups on a spanning tree; parity role (Theorem C; kills `M_odd`) and generation role (kills `M_bs`) | prior: EQ-C Theorem C and its QC2 row (IE₂ independent; a one-pair-only model closes at 18); review_pass2 C3 |
| A5 per-type theorem | **THEOREM ROUTE**: uniform presentation ⟺ all twist bits vanish (a5 E2: exhaustive n = 3, 4); sufficient: EX + IE₂ for the interaction, uniform composition + IE₂, CX. **COUNTEREXAMPLE**: EX alone at two copies (twin, a1/a5 E4), and EX + IE₂ for the exchange only at three copies (`M_tw`, a5 E6) | — |

**§A.31 classification.**
- NEW:
  - the three-copy odd-cycle model with H0 and EX (no coherent chart);
  - CX does not substitute for coupling (`M_bs`);
  - IE₂ is blind to product effects (C12): its content is closure;
  - kinematic 4-cycle parity (τ = δε + c);
  - the six-copy self-duality condition, and `½ − GHZ ∈ B_tw`;
  - `B_tw` is not self-dual, and no local-unitary-invariant cone inside its own dual contains `F`, so a `c = 1`
    composite must lie strictly between `B_tw` and `B_tw*`;
  - the hidden-EX hazard of indexing a native theory by abstract types (§2 TA2 design note).
- POSITIVE: every A1/A3 identity behind design v2 §6 is exact; the Lie-free route's lemmas hold on instances.
- ELABORATING: B2 is formal given B1 + injectivity; the one-orbit argument does not close the self-duality wall
  (a4d).
- Fixed point not reached: node A4c still produced a NEW finding, and A4d only elaborated it. The next pass should
  decide whether a maximal local-unitary-invariant cone inside its own dual and containing `B_tw` can be self-dual,
  and then the four-copy tower. The GHZ-twirled sector reduces the three-copy question to a polyhedral problem in 8
  dimensions, but that reduction gives a necessary condition only (NOTES A4c.1).
- Consistency axis only; bands unchanged.

**Assumption-watch markers.**
1. A native theory indexed by abstract finite **types** carries exchange symmetry through relabelling naturality.
   Index composites by token **sets** to keep "one chart per token" honest. (The typed interface's `relabel` is
   matrix-side and harmless.)
2. "IE₂ holds" checked only against product effects is vacuous (C12).
3. Statements that "CX removes the twist" must not be read as "CX gives chart existence": at three copies it does not
   (`M_bs`).
4. A floating-point search that finds no violation of a cone property is not evidence for it. The x3 search over the
   twirled sector reported none, and an exact pair `F`, `G` lies in that sector (a4c).

## 7. Evidence and probe log

Run as `python3 -I -B <script> [args]` from this directory. The two `.lean` arguments are the base's
`CompositeDimension.lean` and `K2Guard.lean`. Hashes are the first 16 hex digits of sha256. All exact probes print
their decision rule in the header and a verdict line only over green controls. Every exact probe imports
`eq2a_lib.py` (`93de2833598b2290`), the shared exact library with the parsed kernel tables and their hand-transcription
controls.

**Exact probes** (canonical output = the last run; every kept `.runN.out` of that run is byte-identical to it; every
probe `.err` file is empty, and the harness `.err` files hold only the shell's `exit=0` line):

| script | sha | output | sha | checks | verdict | run history |
|---|---|---|---|---|---|---|
| `a1_pauli_twin.py` (CD, K2G) | `bb4a827fde78107e` | `a1_pauli_twin.out` | `580798dbb1fd7c76` | 48/48 | `A1-IDENTITIES-EXACT` | run 1 |
| `a2_universality.py` | `5abcfdf59694bb07` | `a2_universality.out` | `c121cf3e677cd0fa` | 27/27 | `A2-ROUTE-LEMMAS-EXACT` | run 1 not rendered, 25/26: harness error in a countercontrol of my design (`a2_universality.run1.py` `e1dd9081238090f2`, `.run1.out` `4920d5073ae6fd0a`); run 2 |
| `a2b_chart_steps.py` | `fbd18762272673aa` | `a2b_chart_steps.out` | `2f2debf6d0cca7b0` | 8/8 | `A2b-CHART-STEPS-EXACT` | run 1 |
| `a3_bridge.py` | `9fa6147eee64b324` | `a3_bridge.out` | `effa2f1d34b4a95b` | 17/17 | `A3-BRIDGE-INSTANCES-EXACT` | run 1 (a vacuous draft check was replaced before it) |
| `a4_coupling.py` (CD, K2G) | `edb3e25136dd79f1` | `a4_coupling.out` | `ce1490eb2875aca9` | 31/31 | `A4-COUNTERMODELS-EXACT` | run 1 29/29 (`a4_coupling.run1.py` `3a5e7274b2ef58b4`, `.run1.out` `fec3426792c9d9de`); run 2 adds C12 |
| `a4b_twisted_hull.py` | `9a243919c37727a3` | `a4b_twisted_hull.out` | `f31bb3b8bda7c782` | 6/6 | `A4b-GHZ-WITNESS-IN-TWISTED-HULL` | run 1 |
| `a4c_twisted_selfduality.py` | `99e9a506a0185664` | `a4c_twisted_selfduality.out` | `4ab240d2377c4d2e` | 15/15 | `A4c-TWISTED-HULL-NOT-SELF-DUAL` | run 1 |
| `a4d_orbit_extension.py` | `a47eaa2278a85b6c` | `a4d_orbit_extension.out` | `8ee4c06566bd84bb` | 7/7 | `A4d-ORBIT-OBSTRUCTION-FAILS` | run 1 |
| `a5_pertype.py` (CD, K2G) | `6b7350f6f0c096cc` | `a5_pertype.out` | `6a4af4b5d93039b4` | 16/16 | `A5-PERTYPE-EXACT` | run 1 16/16 with one label claiming more than its check (`a5_pertype.run1.py` `8077e9e7d39b91da`, `.run1.out` `b3b56c972e484f18`); run 2 (a vacuous draft check was replaced before run 1) |

**Replay.** `run_all.py` (`0495a81b1ef2e22a`) re-runs the nine probes from `replay/` and compares stdout byte for
byte with the canonical outputs. It also replays the coordinator's prior `eqreview/review_pass2.py`
(`24316e9c3f28ec7e`, recorded output `4b58a33e0bb3ff7c`), which carries the n = 7 tree-generation check this thread
does not re-implement. Result: `run_all.out` (`94c8d9e65299b78c`): all ten entries exit 0 and are identical,
`run_all: OK`. Two earlier replays are kept, each with the probe list as it stood: `run_all.prelim.out`
(`229de5deb0438ccc`; six probes: a2b had been left out of the list, and a4c and a4d were not yet written) and
`run_all.prelim2.out` (`186d48daaaa26fd3`; eight probes, before a4d was written). Every entry in both is identical,
`run_all: OK`.

**Floating-point explorations.** They certify nothing. `run_explorations.py` (`bca0709419e67383`) replays them for
the determinism record only; result `run_explorations.out` (`394e0f6462f62cd6`): all four identical,
`run_explorations: OK`.

| script | sha | output | sha | outcome |
|---|---|---|---|---|
| `x1_twisted_selfdual_float.py` | `73407316c3608194` | `x1_twisted_selfdual_float.out` | `6cbefc5e2a485739` | finite-family LP inconclusive |
| `x2_twisted_cutting_plane_float.run1.py` | `71a00322222cc0d8` | `x2_twisted_cutting_plane_float.run1.out` | `a5a652b2692affcc` | harness error: the trace coordinate was dropped, so the LP tested the wrong condition and returned y = 0 |
| `x2_twisted_cutting_plane_float.py` | `e681cfc57f1d1a1c` | `x2_twisted_cutting_plane_float.out` | `e6280f98f2fd9fad` | pointed to `W ∈ B_tw`; proved exactly in a4b |
| `x3_twisted_selfdual_twirled_float.py` | `25a93b70abc5a50c` | `x3_twisted_selfdual_twirled_float.out` | `835c362b8c2a31e0` | "0 of 10" violations of twirled self-duality: a false negative, superseded by a4c (first launch stopped and its budget edited in place; NOTES A4c) |

**Harness errors and defects** (each recorded at its node in NOTES N4): the a2 run-1 countercontrol; the vacuous
draft checks in a3 and a5, replaced before their first runs; the a5 run-1 label; the x2 run-1 dropped coordinate;
the x3 first launch and its false negative; a2b left out of the first replay list. Two protocol-side notes:
`verification/lean-mathlib/lake-manifest.json` does not exist at the base (the pin was read from `lakefile.toml`,
`rev = "v4.33.0"`). The GitHub API could not
confirm the remote Mathlib tag (403), so the Mathlib lemmas are checked against the local `v4.33.0` snapshot only.

**Other files.** `EQ2A.candidate.lean` (UNBUILT, `d07014777e7befb1`); `NOTES.md` (`9b6595b7f07d380b` at completion).

**Integrity.** The base was re-checked at the end: 1317 files, `sha256sum -c --quiet` silent, exit 0, no
`__pycache__`. No file under `/home/user/incompleteness` outside `.git` is newer than `eq2/PROTOCOL.md`. This
thread wrote only inside `eq2/A/`. During the thread, files in the coordinator's `eqreview/` changed (review files for
the other threads, 15:10–16:25; `review_eq2a_cm.*`, 17:18–17:20), and so did the Mathlib checkout's `.git/index`
(16:10:48). These are not this thread's writes. Its only process run on `eqreview/` content is `review_pass2.py`,
which writes no files and was first replayed at 16:32. Its git commands on the checkout were read-only (`rev-parse`,
`tag --points-at`, `log -1`, `cat-file`, `show`, `grep` on the tag tree) and ran at 15:22–15:24 and 16:26. To keep
this thread independent of B and C, it did not read their review files. At the end it read only the output of the
coordinator's in-progress review of this thread (`review_eq2a_cm.run1.out`/`.err`). That output reproduces the
countermodel facts (hull marginals, conditionals, COMP-1, IE₁, the parity criterion for per-token charts, the GHZ′
witness), and its run 1 stopped on an unevaluated symbolic comparison in its own spot check. Nothing here was changed
because of it.
