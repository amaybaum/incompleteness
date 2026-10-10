# EQ2-A — running notes (design only; base `bcbc516f`, read-only at `scratchpad/eq/base/`)

Track A: operational equivalence across all finite composites, and the IE₂ bridge.
Nothing here is adopted, frozen or governed. No Lean was built (no toolchain); every Lean text is UNBUILT.

## N0. Integrity at start

- `scratchpad/eq/base` checked against `scratchpad/eq/base.manifest.sha256`: 1317 files, `sha256sum -c --quiet` silent,
  exit 0. File count 1317 = manifest lines 1317.
- `scratchpad/eq2/A/` was empty at start.

## N1. Productivity test (fixed before the walk)

**A4 (key question) is a gem iff** it yields a fact strictly stronger than "IE₂ is the deterministic qubit-power
instance of `HasParallelReferenceExtension`" (that restatement is B2 of design v2, already known), AND one of:
- (i) a derivation of IE₂ (or of the coupling it supplies to chart existence) from landed native premises, with every
  step checked; or
- (ii) a proposed native principle strictly weaker than or more basic than IE₂, from which IE₂'s chart-relevant content
  follows, which holds in QM and fails on a named non-quantum foil (converse test); or
- (iii) an exact countermodel showing IE₂ independent of the landed native premises;
AND sub-question (c) decided: either an exact three-copy native model with an odd cycle of twist bits satisfying H1,
H2, admissibility and two-copy interactions on its pair composites (no per-token chart exists), or a proof that no such
model exists, with the load-bearing coupling principle identified exactly.

Below that bar: record-only (coherence relabelling).

**A1–A3, A5 (design items) are complete iff** every identity a proposed statement relies on is checked exactly
(Fractions / exact sympy / exact algebraic numbers) against transcriptions of the kernel definitions at the base, with
controls and countercontrols, and every statement type is fixed against the actual kernel signatures read at the base
(`file:line`).

Decision rules for every script are written into its header before its first run.

## N2. Reading record at the base (all paths under `verification/lean-mathlib/OIBridge/`; read, not built)

**Conventions fixed from the source (A1).**
- `W d := Fin (d+1) → Fin (d+1) → ℝ` (CompositeDimension:97); `ω μ ν`, `μ` = first copy (control/A), `ν` = second
  copy (target/B). `hom x = vecCons 1 x` (CD:100): **index 0 is the unit**, index `j.succ` is Bloch coordinate `j`.
- `homMap N v = vecCons (v 0) (N (vecTail v))` (CD:112). `actT N ω = fun μ => homMap N (ω μ)` (CD:198) = `ω Ñᵀ`
  (acts on the second index); `actC N ω μ ν = homMap N (fun κ => ω κ ν) μ` (CD:201) = `Ñ ω` (first index).
- `prodState x y μ ν = hom x μ * hom y ν` (CD:161); `pairVal a b ω = ∑ μ ∑ ν a μ * ω μ ν * b ν` (CD:164);
  `maxCone Ω` (CD:186) = nonneg on every `prodEffVal e f` with `e f` effects on `Ω`.
- `reflY = diag(1,-1,1)` on `Fin 3 → ℝ` (K2Guard:46): **flips Bloch coordinate 1, i.e. homogeneous index 2**.
  With the Pauli order 0 ↦ 1, 1 ↦ X, 2 ↦ Y, 3 ↦ Z, `homMap reflY` flips the Y index, so `actT reflY` is the partial
  transpose on copy B and `actC reflY ∘ actT reflY` the global transpose.
- `phiW = diag(1,1,-1,1)` (CD:1220) = Pauli table of Φ⁺; `idW = 1` (K2G:101); `actT_reflY_phiW` (K2G:106).
- `cnot` = signed permutation `sgn/pc/pt` (CD:741-786); `nflip = diag(1,-1,-1)` (CD:797).
- `transpose_not_inner` (OrientationSelection:239), over `{n : Type*} [Fintype n] [DecidableEq n]` (OS:102).
- Kernel matrix vocabulary to reuse: `MonoidalCompletion.tensorOf` (MonoidalCompletion:193) = `⊗ₖ` definitionally
  (AncillaInterference:131 uses `rfl`); `OperationalRigidity.psd_trace_mul_nonneg` (OperationalRigidity:917);
  `BoundaryAudit.psdFactorization_discharged` (BoundaryAudit:100); `SpectatorBridge.amplRef_tensorOf` (SB:98).

**A3 objects.**
- `amplRef R Φ M = of fun p q => Φ (refBlockR M p.1 q.1) p.2 q.2` (ReferenceExtension:91), spectator **first**
  (`R × S`); `amplRefL` (RE:131) is typed (`Φ : M_S → M_S'`).
- `withSpectator R e Φ = reindexLinearEquiv e e ∘ₗ amplRefL R Φ ∘ₗ reindexLinearEquiv e.symm e.symm` (RE:422).
- `HasParallelReferenceExtension T` (RE:447): `∀ (R : Type) [Fintype R] [DecidableEq R] n m (e : R × (A × Fin n) ≃
  A × Fin m) (O : Type) … F, T.availExt n O F → T.availExt m O (fun a => withSpectator R e (F a))`.
- `transportT e e' Φ` (TypedCompletion:96) has the same body as `withSpectator` with `e' := e`.
  Definitional facts **landed**: `SpectatorBridge.withSpectator_eq_transport` (SB:381, `rfl`):
  `withSpectator R e Φ = transport e (amplRefL R Φ)`; `TypedCompletion.transportT_self` (TC:109, `rfl`):
  `transportT e e Φ = transport e Φ`. Hence `withSpectator R e Φ = transportT e e (amplRefL R Φ)` by `rfl`.
- `TypedOperationalTheory` (TC:165): `availT`, `id`, `coarse`, `bind`, `relabel` (TC:184), `attach`, `discard`,
  `readout`, `readout_avail`, `readout_local`. **No idle-extension rule.** `shadow A` (TC:231) with
  `availExt n O F := 𝒯.availT (A × Fin n) (A × Fin n) O F` (definitional, TC:261 `Iff.rfl`).
- `typedDiag` (TC:916): `availT … F := ∀ a, PreservesDiag (F a)`; `PreservesDiag Φ := ∀ w, ∃ w', Φ (diagonal w) =
  diagonal w'` (DiagonalTheory:68).
- `FiniteOperationalTheory` (OperationalAssembly:594) docstring: "DELIBERATELY ABSENT: parallel extension of a SYSTEM
  operation to the composite."
- `ObservationalIndependence T := HasParallelReferenceExtension T` (CarrierGeneralOIPlus:73; qubit form
  CompletedOI:129). `OIPlus` (CGOP:185), `oiPlus_iff_qm` (CGOP:207).
- `InertSpectatorCompositionality` (SpectatorBridge:223) = existence form; `IsSpectatorExtension` (SB:180);
  `isSpectatorExtension_iff` (SB:188): **locality fixes the form uniquely**; `inertSpectator_iff_
  parallelReferenceExtension` (SB:233).

**Mathlib pin.** `verification/lean-mathlib/lake-manifest.json` does **not exist** at the base (harness note: the
protocol's pointer is off by one file); the pin is `lakefile.toml` `rev = "v4.33.0"`, toolchain
`leanprover/lean4:v4.33.0`. A local Mathlib checkout exists at `scratchpad/ml-v433-src/m` with `HEAD = db584cd6…`,
`git tag --points-at HEAD` = `v4.33.0`, commit subject "chore: bump toolchain to v4.33.0 (#42604)". Lemma names are
checked with `git grep … v4.33.0 -- Mathlib/` (the tag's tree object, independent of the working tree). The remote tag
could not be confirmed (GitHub API not enabled for that repository in this session), so these are labelled
"verified against the local v4.33.0 snapshot". Lemmas the base kernel already uses are verified in the strong sense.

| lemma | location at v4.33.0 |
|---|---|
| `Matrix.PosSemidef.kronecker` | Mathlib/Analysis/Matrix/Order.lean:213 (uses `⊗ₖ`) |
| `Matrix.PosSemidef.transpose`, `.submatrix`, `.smul`, `.add`, `.conjTranspose` | Mathlib/LinearAlgebra/Matrix/PosDef.lean:85, 80, 107, 102, 95 |
| `Matrix.posSemidef_vecMulVec_self_star` | PosDef.lean:412 (also used by the kernel, RE:226) |
| `Matrix.PosSemidef.dotProduct_mulVec_nonneg` | PosDef.lean:305 (used by the kernel, RE:317) |
| `Matrix.PosSemidef.trace_nonneg`, `mul_mul_conjTranspose_same` | PosDef.lean:349, 321 |
| `Matrix.posSemidef_submatrix_equiv`, `Matrix.posSemidef_sum` | PosDef.lean:144, 148 |
| `Matrix.kronecker`, `trace_kronecker`, `mul_kronecker_mul`, `conjTranspose_kronecker`, `kroneckerMap_transpose`, `kronecker_assoc`, `one_kronecker_one` | Mathlib/LinearAlgebra/Matrix/Kronecker.lean:274, 398, 382, 408, 64, 388, 368 |
| `Matrix.IsHermitian.spectral_theorem`, `eigenvectorUnitary` | Mathlib/Analysis/Matrix/Spectrum.lean:141, 87 |
| `Matrix.unitaryGroup`, `mem_unitaryGroup_iff` | Mathlib/LinearAlgebra/UnitaryGroup.lean:60, 72 |
| `Equiv.sumArrowEquivProdArrow` | Mathlib/Logic/Equiv/Prod.lean:367 |
| `Finset.piFinsetUnion`, `Equiv.sumCompl` | Mathlib/Data/Finset/Basic.lean:637; Mathlib/Logic/Equiv/Sum.lean:261 |
| no lemma "trace of a product of two PSD matrices is ≥ 0" found under the searched names | kernel has it: `psd_trace_mul_nonneg` (OperationalRigidity:917) |

## N3. A4(a) inventory of native (pre-matrix) statements bearing on composition / independence

Native = stated over real carriers, convex bodies and affine effects, with no `Matrix _ _ ℂ`.

| # | statement | location | arity | bears on |
|---|---|---|---|---|
| 1 | `ProductData`: bi-affine product states, bilinear product effects, evaluation law | CompositeInterface:210 | 2 factors | independent preparations / observations combine |
| 2 | `PreComposite.prod_mem` (products are states), `prodEff_effect` (products of effects are effects), `prodEff_unit` | CI:223-230 | 2 | joint performability of independent tests (effect-level idle extension with `f = unit`) |
| 3 | `LocallyTomographic` / `Composite.lt` (premise field; independent: `no_composite_over_paddedPre` CI:895) | CI:235, 243 | 2 | local tomography |
| 4 | `attach`, `margA` (discard), `condA`, `readout` (definitions) and laws L1-L11: `condA_prodState` "no signalling on products" (CI:332), `condA_mem` (conditional states are states, CI:431) | CI:252-468 | 2 | marginals, conditioning, no-signalling |
| 5 | `JointReversible G := PreservesBody P.Ω G` (any affine automorphisms of the joint body); `jointReversible_words` | CI:445, 449 | 2 | joint dynamics — **no notion of a local or idle map** |
| 6 | `W d`, `actT`, `actC` (one-copy actions on the two-copy carrier = idle extension of a one-copy map **to two copies**), `maxCone`, `IsProduct`, `NativeGate` (posFwd/posInv two-sided positivity on products), `Entangling` | CompositeDimension:97-231 | 2 | IE₁ vocabulary at two copies; interactions |
| 7 | `CandidateCone` (products ⊆ K ⊆ maxCone); `no_candidateCone_cnot_reflY` | K2Guard:95, 143 | 2 | composite orientation obstruction |
| 8 | `CopyNatural` (identification of two copies' NOTs; no consumer) | KInfFoundations:284 | 2 copies, 1 map | copy identification |
| 9 | `IsEffectOn`, `PerfectlyDistinguishable`, `ElementaryDrivability` | KF:116, 154, 264 | 1 | — |
| 10 | `StageCompletion` (SCInf, BinaryVisible, FiniteRank), `CompletionAction` (OpDatum, AffineRespect), `OrbitGeneration` | SC, CA, OG | 1 | single-system only |
| 11 | `SubstratumSource` / `ImplementationLocality` / `StructuralClosure`: `ContextStable 𝓘 := 𝓘 S K → 𝓘 (R×S) (1_R ⊗ K)` (ImplementationLocality:359), `substratumClass_contextStable` (StructuralClosure:261) | matrix side (operators over ℂ) | — | the **matrix/substratum** form of "stability under an uncoupled spectator"; not pre-matrix |

**Manuscript.** `papers/Main.md:564` (OI⁺ formulation: "observational independence … equivalent … to inert
spectators", "each added principle is independently necessary"; the substratum-source form lists "stability under an
uncoupled spectator" among what the concrete substratum supplies — that is `substratumClass_contextStable`, matrix
side). `Main.md:352, 542, 628`: "inert spectators" named among the five completion conditions; graph locality gives
the causal cone only, "It does not alone establish statistical product structure after conditioning, local tomography,
or one common tensor-product instrument category."

**Finding N3.** No native statement in the base has three or more factors, and none states an idle extension of a
map on a composite to a larger composite. IE₂ is not expressible in the landed native vocabulary; the matrix-side
counterpart is a property (`HasParallelReferenceExtension`), kernel-independent of the other OI⁺ principles
(`independence_independent`, CompletedOI:475; `redundancy_fails`, ImplementationLocality:207). So the derivation
question has to be posed in a proposed native n-token vocabulary (A2), with the landed two-copy premises transported
to every bipartition.

## N4. Node log

**Node A1 (Pauli/twin package).** `a1_pauli_twin.py` (decision rule in header), run 1: 48/48, verdict
`A1-IDENTITIES-EXACT`. The cnot tables, `idW`, `chainW`, `phiW`, `reflY` are parsed from the base files and agree with
independent hand transcriptions (T0); the landed facts K1–K6 are reproduced (controls). Every identity the §6.1
statements rely on holds exactly: pauliW of products, the pairing, Pauli orthogonality (n ≤ 3), the coordinates of
`actT reflY` (= PT_B), `actC reflY` (= PT_A), `transposeW` (= global transpose = `actC reflY ∘ actT reflY`),
`swapW` (= Ad SWAP), `cnot` (= Ad CNOT, control first); `chart2 a a idW = diag(1, a aᵀ)` symbolically (so idW is
fixed iff a is orthogonal; control diag(2,1,1)); singlet value −1 at |v|² = 2; phiW = ½ww†; the presented exchange is
`transposeW ∘ swapW`; its idle extension to a third copy has value −1 (|v|² = 2) at v = e₀₀₁ − e₁₀₀; control Ad SWAP
stays rank-one PSD; countercontrol T_AB ⊗ id negative. Verdict at the node: **all A1 identities exact**.

**Node A2 (Lie-free route).** `a2_universality.py`. Run 1 (kept: `a2_universality.run1.{py,out,err}`): 25/26, verdict
**not rendered**. The failing check was a countercontrol of my own design: "the five Lemma-6.1 factors in reversed
order do not give C²(V²)". By hand on the four control values, the reversed product is also C²(V²) (it is the same
identity with the two halves exchanged). Harness error, not a mathematical one. Run 2: countercontrol replaced by
"V^H → V in the middle factor" (must fail, does) and the reversed order kept as a recorded note check; 27/27, verdict
`A2-ROUTE-LEMMAS-EXACT` (~4.5 min, dominated by the n = 6 closure). Verdict at the node: **the route's lemmas U1–U5
hold exactly on instances; end-to-end, a two-level unitary on (000,111) is an exact product over Q(i) of 53 gates each
on an edge of the path 0–1–2.** My independent Pauli-closure code reproduces the tree generation result for
n = 3..6 with the forest countercontrol (the coordinator's n = 7 is not re-run here; see replay below).

**Node A3 (typed bridge).** `a3_bridge.py`. Pre-run design defect, caught before any run: the first draft's B3.a
computed `withSpectator` and `transportT` with the same expression (a vacuous check). Replaced, before the first run,
by a convention control (withSpectator acts as id ⊗ Φ on reindexed products, with `reindex` implemented from the
index map), and the definitional identity itself is recorded as a reading of two landed `rfl` lemmas (SB:381,
TC:109). Run 1: 17/17, verdict `A3-BRIDGE-INSTANCES-EXACT`. Verdict at the node: B1 (presentation of idle extension
= amplification, composition, chart naturality, injectivity) and the B2 pull-back step hold exactly on instances;
`PreservesDiag` is stable under amplification (random CP-like and the non-CP transpose), countercontrol conj(H) fails;
typed foil: the positive non-CP transpose's amplification has singlet value −1 (so a "typed positive" theory fails
`TypedIdleExtension`).

**Node A4 (key question), depth-first.**
- A4.1 Inventory (N3): no native statement with ≥ 3 factors; IE₂ is not expressible in the landed native vocabulary.
  Verdict: the derivation has to be posed for n-token transports of the landed premises.
- A4.2 Do the transports (H0 marginals, H1, H2 = IE₁, LT, COMP-1 on every pair|single bipartition, conditional
  closure, EX, pair-CX, pair interactions) give chart existence at three copies? `a4_coupling.py` run 1: 29/29.
  **No.** M_odd = K_(0,1,0) (odd twist cycle; ≅ M_tw = K_(1,1,1) by reflecting copy 1; M_tw is S₃-symmetric): no
  per-token chart presents its three pair composites (C8, all 8 ε). M_bs = K_(0,0,0) (pair-CX holds): GHZ is outside
  every per-token image (C10). IE₂ fails in all of them: (cnot on (0,1)) ⊗ id sends the generator |+⟩⟨+| ⊗ Φ⁺₁₂ of
  M_odd and M_bs to GHZ′ with tr(W GHZ′) = −1/2 for a functional W ≥ 0 on every generator (C9); in M_tw = R_1 M_odd
  the failure is the transport by R_1 (state |+⟩⟨+| ⊗ PT_1(Φ⁺)₁₂, interaction R_1 cnot R_1 of the twisted pair 01).
  Verdict: **INDEPENDENT** of the transports; exact countermodels.
- A4.3 Which weakening of IE₂ would suffice? (i) idle extension of local maps (H2): holds in M_*, insufficient.
  (ii) idle extension of the exchange: holds in M_tw (S₃-invariance), insufficient. (iii) "probabilistic" idle
  extension (image nonnegative on product effects): **automatic** from Step 0 + conditional closure (C12, run 2,
  31/31; a scope extension, run 1 kept), so it carries no content and cannot detect the failure. (iv) closure of K_S
  under the idle extension of the interaction groups on a spanning tree: sufficient by the written Kₙ-COPIES proof
  (conditional on Theorem A′). Verdict: **the load-bearing coupling is tree-IE₂ in closure form**, with two roles —
  parity (M_odd) and generation (M_bs).
- A4.4 (favourable branch, maximum skepticism) Can observation-level (kinematic) independence supply the coupling?
  By C12 no test with product effects can; entangled multi-token effects are needed. COMP-1 on 2|2 bipartitions
  (KT₂; all effects of the pair composites, which COMP-1's quantifier already includes) forces every 4-cycle of twist
  bits to be even (D1: negative value iff odd parity, 16 assignments), equivalently τ = δε + c𝟙 (D2: exhaustive on
  K₄, K₅). Pressure test: the derivation uses only prod_mem on (01)|(23), prodEff_effect on (12)|(03), H0 to identify
  the factor bodies with the pair composites, and Bell tables of the pair cones; no dynamics; even cases give no
  negative value among the candidates (consistency control) and D3 spot checks are nonnegative. The global bit c is
  not fixed by KT₂: in a contraction of pair/single states with pair/single effects every cycle alternates and has even
  length (written), so the all-twisted pairwise hull passes. Verdict: **partial THEOREM ROUTE** (4-cycle parity from
  kinematics) and **one residual bit**.
- A4.5 COMP-1 on every bipartition (KT∞): at six copies the 012|345 test through three Bell pairs gives
  ⟨E ⊗ F, Φ⁺Φ⁺Φ⁺⟩ = ⟨E, T F⟩, so KT∞ forces K₃ ⊇ T(K₃*) (untwisted) or K₃ ⊇ K₃* (all-twisted), and with the dual test
  (Bell effects) K₃ = T(K₃*) — (co-)self-duality. The pairwise hulls fail it (D4: −1/16, untwisted, exact). Whether
  KT∞ with H0, H1, H2 and pair interactions forces c = 0 and K_S = PSD_S is **OPEN**; named wall: the classification of
  SO(3)³-invariant cones K₃ with pair conditionals in {Q, Tw}, min ⊆ K₃ ⊆ max and K₃ = Λ(K₃*), and of the towers
  above them.

Classification at the node: A4(b) **INDEPENDENT PREMISE** (countermodels M_odd/M_tw, M_bs), with a partial THEOREM
ROUTE (KT₂ ⇒ 4-cycle parity) and an OPEN wall (KT∞); A4(c) **COUNTEREXAMPLE** exists (odd cycle with H0 and EX),
load-bearing coupling identified (tree-IE₂ in closure form). §A.31: NEW findings this pass (odd-cycle model; CX does
not substitute for coupling; product-effect blindness of IE₂; KT₂ parity; KT∞ self-duality) — fixed point not reached.

**Node A2b (chart steps).** `a2b_chart_steps.py` run 1: 8/8, `A2b-CHART-STEPS-EXACT`. T∘Ad_U∘T = Ad_Ū and
PT_A∘Ad_U∘PT_A = PT_B∘Ad_Ū∘PT_B (symbolic input, exact U over Q(i)), so the per-token reflections untwist edge groups
as Step 3 needs; countercontrol: PT_B∘Ad_CNOT∘PT_B is not multiplicative (not inner). The τ-twisted 2-colouring exists
for all 43 614 (labelled tree, τ) cases with n = 2..6; countercontrol: odd triangle has none. Step 0 (conditioning
commutes with idle extension and with per-token charts) holds symbolically.

**Node A4b (the GHZ witness in the all-twisted hull).** Float exploration first (labelled, no evidential weight):
`x1_twisted_selfdual_float.py` (finite-family LP: decomposition infeasible, separating vector not valid on random
generators — inconclusive); `x2_twisted_cutting_plane_float.py` run 1 (kept as `x2_*.run1.*`) had a harness error
(the identity/trace coordinate was dropped, so the LP tested a cone condition and returned y = 0); run 2 with affine
separation: the margin converged to ~ −3.5e−9 and the convex-combination LP became feasible — W = ½ − |GHZ⟩⟨GHZ|
appears to lie in B_tw. A hand derivation in stabilizer coordinates then gave an explicit decomposition, verified
exactly by `a4b_twisted_hull.py` (6/6, `A4b-GHZ-WITNESS-IN-TWISTED-HULL`): twirl over the GHZ stabilizer of
(1/9) Σ_p (α_p + β_p + δ_p) equals W/3, with α = twisted singlet ⊗ |+⟩, β = twisted rotated singlet ⊗ |+i⟩,
δ = twisted (Ψ⁻+Ψ⁺)/2 ⊗ ½; countercontrol: without β the twirl is not a multiple of W. Verdict at the node: the
natural witness does **not** separate B_tw from its dual; the six-copy test for the all-twisted hull reduces to
self-duality of B_tw, undecided at this node. `x3_twisted_selfdual_twirled_float.py` probes self-duality on the
twirled subspace (float, exploration only); outcome under node A4c.

**Node A4c (is B_tw self-dual?), depth-first continuation of A4.5.**
- A4c.1 Reduction to the GHZ-twirled sector (written). The GHZ stabilizer group consists of local Pauli products, which
  preserve B_tw (B_tw is invariant under every local unitary: Ad_{u⊗v⊗w} sends PT_j(σ) ⊗ ρ to PT_j(Ad_{u⊗v̄}σ) ⊗
  Ad_w ρ). Its twirl T is self-adjoint and idempotent, so T(K)* within the fixed space equals T(K*), and self-duality
  of B_tw would force self-duality of T(B_tw) in the 8-dimensional space of GHZ-diagonal operators. In coordinates
  d_b = (λ_{0b} + λ_{1b})/2, c_b = (λ_{0b} − λ_{1b})/2 (b ∈ Z₂², λ the GHZ-basis eigenvalues), PT_j fixes d and
  translates c by v_j (v_0 = 11, v_1 = 10, v_2 = 01); PSD is d_b ≥ |c_b|; T(B_tw) ⊆ Σ_pairs {PT_i Y ⪰ 0, PT_j Y ⪰ 0},
  whose dual is {d ≥ 0, d_a + d_b ≥ |c_x| + |c_y| for every pair {a,b} with complementary pair {x,y}}.
- A4c.2 In that dual: f = (d = (0, ½, ½, ½), c = (1, 0, 0, 0)) and g = (same d, c = (−1, 0, 0, 0)), with f·g = −¼, i.e.
  the operators F = ½(1 − |000⟩⟨000| − |111⟩⟨111|) + (|000⟩⟨111| + h.c.) and G = Ad_{S⊗S⊗1}F, tr(FG) = −½. Float
  sanity check (not recorded as evidence): conditionals of PT_j F, PT_j G have minimum eigenvalue 0, tr(FG) = −0.5.
  The hand derivations behind a4c (the sum-of-squares form of the conditionals, the separable decomposition below,
  the relation G = Ad_{S⊗S⊗1}F) were pre-checked in floating point before the decision rule was written.
- A4c.3 `a4c_twisted_selfduality.py` run 1: 15/15, `A4c-TWISTED-HULL-NOT-SELF-DUAL`. Every conditional
  ⟨φ|_k PT_j(F)|φ⟩_k (and of G), computed from the operator with symbolic φ, equals an explicit sum of squares, so F,
  G ∈ B_tw* without the twirl reduction; G = Ad_{S⊗S⊗1}F; tr(FG) = −½. Controls: W = PT_1(ρ′) with ρ′ an explicit
  positive sum of products across 01|2 (a one-family certificate that W ∈ B_tw, simpler than a4b's); tr(WF) = ½,
  tr(WG) = 5/2; 40 random exact generators pair nonnegatively with F and G. Countercontrols: coherence 2 instead of 1
  gives value −½ on PT_1(Ψ⁻) ⊗ |+⟩⟨+|; GHZ pairs to −½ with W. The six-copy link identities behind the written
  reduction hold exactly: twin links give tr(EF)/8, untwisted links tr(EFᵀ)/8 (they differ on the sample).
- Verdict at the node: **B_tw is not self-dual** (G ∈ B_tw* \ B_tw), and no local-unitary-invariant cone K with
  K ⊆ K* contains F or G. Consequence for the c = 1 world under KT∞, H0, H2 and COMP-1 on pair|single bipartitions:
  its three-copy composite satisfies B_tw ⊊ K₃ = K₃* ⊊ B_tw*, with F, G ∉ K₃. Whether such a local-unitary-invariant
  self-dual K₃ exists (and extends to a tower) is the refined wall, **OPEN**. Pressure test of this favourable branch:
  the result removes the minimal candidate only; it does not exclude c = 1. Barker–Foran-type completion (a cone
  inside its dual extends to a self-dual cone; literature, unverified; the Zorn argument is elementary) gives
  self-dual cones between B_tw and B_tw*, but not obviously local-unitary-invariant ones: an invariant extension can
  add an element only when its whole orbit pairs nonnegatively, which F's orbit does not.
- A4c.4 (pressure test of the wall itself: does the one-orbit argument close it?) The simplest exclusion of c = 1
  would be: every x ∈ B_tw* \ B_tw pairs negatively with some local-unitary image of itself, so an LU-invariant
  K₃ with B_tw ⊆ K₃ ⊆ K₃* equals B_tw, which is not self-dual. Written check: B_tw ⊆ B_tw* (two generators on the
  same pair pair to tr(σσ′)tr(ρρ′) ≥ 0; on different pairs the trace contracts to tr(AB) with A, B conditional
  states, PSD), so the question is not trivially decided. Candidate x_t = F + t·1: in B_tw* for t ≥ 0; tr(G x_t) =
  3t − ½, so x_t ∉ B_tw for t < 1/6; x_t = (½ + t)·1 + ½|G+⟩⟨G+| − (3/2)|G−⟩⟨G−|, so for EVERY unitary U,
  tr(x_t U x_t U†) ≥ 8t² + 6t − ½ (the cross term of the two rank-one parts is at least −3/2), which is ≥ 0 for
  t ≥ (√13 − 3)/8 ≈ 0.076. `a4d_orbit_extension.py` run 1: 7/7, `A4d-ORBIT-OBSTRUCTION-FAILS` (t = 1/10: sum of
  squares for the conditionals, tr(G x) = −1/5, the decomposition, bound 9/50 attained at S⊗S⊗1, random exact
  global and local unitaries above it; countercontrol t = 1/20 gives −9/50). Verdict at the node: B_tw + cone(LU·x)
  is a strictly larger LU-invariant cone inside its own dual, so **the one-orbit argument does not close the wall**;
  deciding it needs the structure of maximal LU-invariant self-positive extensions of B_tw (and the four-copy tower).
  Classification: ELABORATING (it sharpens the wall; no status change).
- x3 outcome (float, exploration): "0 of 10 boundary points of the twirled dual base lie robustly outside B8". This is
  a **false negative**, superseded by the exact a4c: F and G lie in the twirled sector x3 searched (L2) and G is
  outside B8. The random directions missed the region B8^ \ B8 and the nonsmooth optimizer reported the trivial value
  at z = 0. Harness lesson (§A.21): a float search that finds no violation is not evidence of self-duality.
  Harness record for x3: the first launch (a larger grid and trial budget, output block-buffered behind a pipe) was
  stopped before it printed anything, to stay inside the time budget; the script was edited in place (budget only:
  grid 600, 10 trials; that first version is not kept) and relaunched unbuffered. The recorded output is from the
  relaunch, with the shell's `exit=0` line appended.

**Replays.** `run_all.prelim.out`: a first replay with the probe list as it stood (six probes: a2b had been left
out of the list by oversight, a4c and a4d did not yet exist) plus the coordinator's `review_pass2.py`, all
identical. `run_all.prelim2.out`: a second replay with
eight probes (a4d not yet written), all identical. `run_all.out`: the final replay of all nine exact probes plus
`review_pass2.py`. `run_explorations.out`: the float explorations x1, x2 (both runs) and x3, replayed for the
determinism record only.

**Node A5 (per-type).** `a5_pertype.py`. Pre-run defect caught before the first run: the first draft's E6 checked
only that permutations map pairs to pairs (vacuous); replaced by symbolic generator-table permutations. Run 1: 16/16;
the last E6 label claimed more than its check computed (it checks `swapW idW = idW` only) — label corrected, run 2
16/16 (`a5_pertype.run1.*` kept). Verdict at the node: per-token chart ⟺ τ coboundary, uniform chart ⟺ τ = 0
(exhaustive n = 3, 4); EX-symmetric τ = c presentable iff c = 0; the twin and M_tw satisfy EX (and M_tw IE₂ for the
exchange) and are not uniformly presentable.
