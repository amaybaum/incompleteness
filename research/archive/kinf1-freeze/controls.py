#!/usr/bin/env python3
"""controls.py -- round KINF-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the module's frozen header and declarations (every structure and definition
whole, every theorem statement), the census family, the workflow edit, the import line, the probe blob, the outcome
sentences and the clause.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; two synthetic
                                            rows (FOUNDATIONS-PROVED, UNDECIDED) that must hold; mutation controls
                                            that must fail with their named codes
"""
import hashlib, json, os, re, subprocess, sys

D = '98f5f08bad2d02aba00b9cfce51538c5e890cc18'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/'
MODULE = 'verification/lean-mathlib/OIBridge/KInfFoundations.lean'
PROBE = 'verification/lean/kinf_foundations_probe.py'
PROBE_BLOB = '3c1adfe7b5025ae72856cf18d5a2f9937e46bd4f'
REFERENCE_BLOB = '0c07f7950c36559ee02066c0e989b9c552777848'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LABELS = ('KINF-1-FOUNDATIONS-PROVED', 'KINF-1-UNDECIDED')
VERDICT = 'kinf1_kernel_core'
FROZEN = {'header': "/-\n  OIBridge/KInfFoundations.lean — round KINF-1: the field-neutral vocabulary of the pre-quantum\n  operational completion, and the elementary lemmas that vocabulary supports.\n\n  Nothing in this module mentions ℂ, a matrix carrier, or the substratum. It fixes definitions\n  over a real normed space `V` and proves the small logical facts that later rounds cite. It\n  sources nothing: the module does not derive drivability, supporting effects, singleton faces\n  or copy naturality from any OI construction, and it contains no reconstruction theorem.\n\n  Defined here.\n    §A  a finite observer stage: finitely many preparations and effects and a probability table\n        with a unit effect; its state body is the convex hull of the preparation vectors.\n    §B  effects on a convex body, the certain face of an effect, supporting-effect completeness\n        (SEC), singleton faces (SF), full effects, perfect distinguishability, central symmetry.\n    §C  elementary drivability: a continuous one-parameter family of affine automorphisms of\n        the body, starting at the identity, with a distinguished member `N` and a reversible\n        `J` that does not normalize the flow; and copy naturality of two NOTs under a copy\n        identification.\n    §G  `KInf1`, the statement of hypothesis K∞-1 as a proposition about a body and a family of\n        available effects. It is a definition and is proved for nothing here.\n\n  Proved here.\n    §A  `states_isCompact`, `states_unit`: the state body of a finite stage is compact and lies\n        on the unit hyperplane.\n    §D  Lemma C, `strictConvex_of_supporting_singleton`: a closed convex body with (SEC) and (SF)\n        is strictly convex.\n    §D  Lemma D, `card_le_two_of_centrallySymmetric`: a centrally symmetric body admits at most\n        two perfectly distinguishable states, whatever effects are available.\n    §E  Lemma B, `eq_closedBall_of_frontier_subset_sphere`: a compact convex body with `0` in\n        its interior whose frontier lies on the unit sphere is the closed unit ball.\n    §E  the finite-preparation bound, `exposed_mem_range` and `exposed_ncard_le`: every point of\n        a finite stage's body exposed by an effect with a singleton certain face is the vector\n        of one of its preparations, so at most `|P|` points are exposed.\n    §E′ Theorem F2, `classical_exposed_ncard_le`: a body realized on `N` ontic states, meeting\n        each coordinate facet in at most one point, has at most `N` points exposed by response\n        effects; `response_eq_one_forces` is the step that puts every exposed point on a facet.\n    §F  `qubit_certain_face`: for the imported qubit kinematics, the certain face of the effect\n        `ρ ↦ ρ 0 0` on density matrices is the single point `|0⟩⟨0|`. This is a theorem of matrix\n        kinematics, stated as such.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/\nimport Mathlib.Analysis.Convex.Gauge\nimport Mathlib.Analysis.Convex.Strict\nimport Mathlib.Analysis.Convex.Topology\nimport Mathlib.Analysis.Normed.Module.Basic\nimport Mathlib.Data.Set.Card\nimport Mathlib.LinearAlgebra.Matrix.PosDef\nimport Mathlib.LinearAlgebra.Matrix.Trace\nimport OIBridge.CoherentExtension\n\n", 'declarations': {'FiniteStage': ('structure', 'structure FiniteStage where\n  P : Type\n  E : Type\n  [fP : Fintype P]\n  [fE : Fintype E]\n  p : E → P → ℝ\n  unit : E\n  nonneg : ∀ e x, 0 ≤ p e x\n  le_one : ∀ e x, p e x ≤ 1\n  unit_eq : ∀ x, p unit x = 1'), 'vec': ('def', 'def vec (x : S.P) : S.E → ℝ := fun e => S.p e x'), 'states': ('def', 'def states : Set (S.E → ℝ) := convexHull ℝ (Set.range S.vec)'), 'states_isCompact': ('theorem', 'theorem states_isCompact : IsCompact S.states :='), 'states_isClosed': ('theorem', 'theorem states_isClosed : IsClosed S.states :='), 'states_convex': ('theorem', 'theorem states_convex : Convex ℝ S.states :='), 'states_unit': ('theorem', 'theorem states_unit : ∀ v ∈ S.states, v S.unit = 1 :='), 'IsEffectOn': ('def', 'def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=\n  ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1'), 'certainFace': ('def', 'def certainFace (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Set V :=\n  {x ∈ Ω | e x = 1}'), 'SupportingEffectComplete': ('def', 'def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x = 1'), 'SingletonFaces': ('def', 'def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  ∀ e ∈ avail, IsEffectOn Ω e → (certainFace Ω e).Subsingleton'), 'fullEffects': ('def', 'def fullEffects (Ω : Set V) : Set (V →ᵃ[ℝ] ℝ) :=\n  {e | IsEffectOn Ω e}'), 'PerfectlyDistinguishable': ('def', 'def PerfectlyDistinguishable (Ω : Set V) {ι : Type} [Fintype ι]\n    (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ) : Prop :=\n  (∀ i, x i ∈ Ω) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ y ∈ Ω, ∑ i, e i y = 1) ∧\n    (∀ i, e i (x i) = 1)'), 'CentrallySymmetric': ('def', 'def CentrallySymmetric (Ω : Set V) (c : V) : Prop :=\n  ∀ x ∈ Ω, c + (c - x) ∈ Ω'), 'affine_combo': ('theorem', 'theorem affine_combo (e : V →ᵃ[ℝ] ℝ) (x y : V) (a b : ℝ) (hab : a + b = 1) :\n    e (a • x + b • y) = a * e x + b * e y :='), 'affine_reflect': ('theorem', 'theorem affine_reflect (e : V →ᵃ[ℝ] ℝ) (c x : V) :\n    e (c + (c - x)) = 2 * e c - e x :='), 'convex_affine_le': ('theorem', 'theorem convex_affine_le (e : V →ᵃ[ℝ] ℝ) (m : ℝ) : Convex ℝ {y : V | e y ≤ m} :='), 'ElementaryDrivability': ('structure', 'structure ElementaryDrivability (Ω : Set V) where\n  flow : ℝ → V ≃ᵃ[ℝ] V\n  flow_zero : flow 0 = AffineEquiv.refl ℝ V\n  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2\n  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω\n  t₀ : ℝ\n  N_involutive : ∀ x, flow t₀ (flow t₀ x) = x\n  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x\n  J : V ≃ᵃ[ℝ] V\n  J_preserves : ∀ x ∈ Ω, J x ∈ Ω\n  J_off_axis : ∃ t, ∀ s, (J.symm.trans (flow t)).trans J ≠ flow s'), 'ElementaryDrivability.N': ('def', 'def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V :=\n  D.flow D.t₀'), 'CopyNatural': ('def', 'def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :=\n  N_B = (e.symm.trans N_A).trans e'), 'copyNatural_refl_iff': ('theorem', 'theorem copyNatural_refl_iff (N_A N_B : V ≃ᵃ[ℝ] V) :\n    CopyNatural N_A N_B (AffineEquiv.refl ℝ V) ↔ N_B = N_A :='), 'copyNatural_iff_apply': ('theorem', 'theorem copyNatural_iff_apply (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :\n    CopyNatural N_A N_B e ↔ ∀ x, N_B (e x) = e (N_A x) :='), 'strictConvex_of_supporting_singleton': ('theorem', 'theorem strictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω)\n    (hSEC : SupportingEffectComplete Ω avail) (hSF : SingletonFaces Ω avail) :\n    StrictConvex ℝ Ω :='), 'card_le_two_of_centrallySymmetric': ('theorem', 'theorem card_le_two_of_centrallySymmetric {Ω : Set V} {c : V} (hΩ : CentrallySymmetric Ω c)\n    (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ)\n    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :='), 'card_le_two_of_centrallySymmetric_full': ('theorem', 'theorem card_le_two_of_centrallySymmetric_full {Ω : Set V} {c : V}\n    (hΩ : CentrallySymmetric Ω c) (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V)\n    (e : ι → V →ᵃ[ℝ] ℝ) (_ : ∀ i, e i ∈ fullEffects Ω)\n    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :='), 'eq_closedBall_of_frontier_subset_sphere': ('theorem', 'theorem eq_closedBall_of_frontier_subset_sphere {Ω : Set V} (hconv : Convex ℝ Ω)\n    (hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)\n    (hfr : frontier Ω ⊆ Metric.sphere (0 : V) 1) : Ω = Metric.closedBall (0 : V) 1 :='), 'exists_vertex_of_certain': ('theorem', 'theorem exists_vertex_of_certain {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)\n    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)\n    (hx : x ∈ convexHull ℝ (Set.range v)) (hone : e x = 1) : ∃ k, e (v k) = 1 :='), 'exposed_mem_range': ('theorem', 'theorem exposed_mem_range {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)\n    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)\n    (hface : certainFace (convexHull ℝ (Set.range v)) e = {x}) : x ∈ Set.range v :='), 'exposedPoints': ('def', 'def exposedPoints (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Set V :=\n  {x | ∃ e ∈ avail, IsEffectOn Ω e ∧ certainFace Ω e = {x}}'), 'exposed_ncard_le': ('theorem', 'theorem exposed_ncard_le {ι : Type} [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)) :\n    (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι :='), 'FiniteStage.exposed_le_card': ('theorem', 'theorem FiniteStage.exposed_le_card (S : FiniteStage)\n    (avail : Set ((S.E → ℝ) →ᵃ[ℝ] ℝ)) :\n    (exposedPoints S.states avail).ncard ≤ Fintype.card S.P :='), 'of': ('structure', 'structure of §B, since the bound needs only the form `∑ cᵢ pᵢ`. -/'), 'simplex': ('def', 'def simplex (N : ℕ) : Set (Fin N → ℝ) :=\n  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1}'), 'ClassicallyExposed': ('def', 'def ClassicallyExposed (Ω : Set (Fin N → ℝ)) (x : Fin N → ℝ) : Prop :=\n  ∃ c : Fin N → ℝ, (∀ i, 0 ≤ c i ∧ c i ≤ 1) ∧ {p ∈ Ω | ∑ i, c i * p i = 1} = {x}'), 'response_eq_one_forces': ('theorem', 'theorem response_eq_one_forces {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N) {c : Fin N → ℝ}\n    (hc : ∀ i, 0 ≤ c i ∧ c i ≤ 1) {x : Fin N → ℝ} (hx : x ∈ Ω)\n    (hone : ∑ i, c i * x i = 1) : ∀ i, 0 < x i → c i = 1 :='), 'mem_of_classicallyExposed': ('theorem', 'theorem mem_of_classicallyExposed {Ω : Set (Fin N → ℝ)} {x : Fin N → ℝ}\n    (hx : ClassicallyExposed Ω x) : x ∈ Ω :='), 'exists_zero_of_classicallyExposed': ('theorem', 'theorem exists_zero_of_classicallyExposed {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)\n    (hnt : ¬ Ω.Subsingleton) {x : Fin N → ℝ} (hx : ClassicallyExposed Ω x) :\n    ∃ i, x i = 0 :='), 'classical_exposed_ncard_le': ('theorem', 'theorem classical_exposed_ncard_le {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)\n    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :\n    {x | ClassicallyExposed Ω x}.ncard ≤ N :='), 'qubit_certain_face': ('theorem', 'theorem qubit_certain_face (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hρ : ρ.PosSemidef)\n    (htr : ρ.trace = 1) (h00 : ρ 0 0 = 1) :\n    ρ = Matrix.of fun i j => if i = 0 ∧ j = 0 then (1 : ℂ) else 0 :='), 'KInf1': ('def', 'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=\n  Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail'), 'strictConvex_of_kInf1': ('theorem', 'theorem strictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}\n    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω) (hK : KInf1 Ω avail)\n    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :\n    StrictConvex ℝ Ω :='), 'kinf1_kernel_core': ('theorem', 'theorem kinf1_kernel_core :\n    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), Convex ℝ Ω → IsClosed Ω →\n      SupportingEffectComplete Ω avail → SingletonFaces Ω avail → StrictConvex ℝ Ω) ∧\n    (∀ (Ω : Set V) (c : V), CentrallySymmetric Ω c → c ∈ Ω →\n      ∀ (ι : Type) [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ),\n        PerfectlyDistinguishable Ω x e → Fintype.card ι ≤ 2) ∧\n    (∀ Ω : Set V, Convex ℝ Ω → IsCompact Ω → (0 : V) ∈ interior Ω →\n      frontier Ω ⊆ Metric.sphere (0 : V) 1 → Ω = Metric.closedBall (0 : V) 1) ∧\n    (∀ (ι : Type) [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)),\n      (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι) ∧\n    (∀ (N : ℕ) (Ω : Set (Fin N → ℝ)), Ω ⊆ simplex N →\n      (∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) → {x | ClassicallyExposed Ω x}.ncard ≤ N) :=')}}
PRINT = {'states_isCompact': 'OIBridge.KInfFoundations.FiniteStage.states_isCompact', 'states_isClosed': 'OIBridge.KInfFoundations.FiniteStage.states_isClosed', 'states_convex': 'OIBridge.KInfFoundations.FiniteStage.states_convex', 'states_unit': 'OIBridge.KInfFoundations.FiniteStage.states_unit', 'affine_combo': 'OIBridge.KInfFoundations.affine_combo', 'affine_reflect': 'OIBridge.KInfFoundations.affine_reflect', 'convex_affine_le': 'OIBridge.KInfFoundations.convex_affine_le', 'copyNatural_refl_iff': 'OIBridge.KInfFoundations.copyNatural_refl_iff', 'copyNatural_iff_apply': 'OIBridge.KInfFoundations.copyNatural_iff_apply', 'strictConvex_of_supporting_singleton': 'OIBridge.KInfFoundations.strictConvex_of_supporting_singleton', 'card_le_two_of_centrallySymmetric': 'OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric', 'card_le_two_of_centrallySymmetric_full': 'OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric_full', 'eq_closedBall_of_frontier_subset_sphere': 'OIBridge.KInfFoundations.eq_closedBall_of_frontier_subset_sphere', 'exists_vertex_of_certain': 'OIBridge.KInfFoundations.exists_vertex_of_certain', 'exposed_mem_range': 'OIBridge.KInfFoundations.exposed_mem_range', 'exposed_ncard_le': 'OIBridge.KInfFoundations.exposed_ncard_le', 'FiniteStage.exposed_le_card': 'OIBridge.KInfFoundations.FiniteStage.exposed_le_card', 'response_eq_one_forces': 'OIBridge.KInfFoundations.response_eq_one_forces', 'mem_of_classicallyExposed': 'OIBridge.KInfFoundations.mem_of_classicallyExposed', 'exists_zero_of_classicallyExposed': 'OIBridge.KInfFoundations.exists_zero_of_classicallyExposed', 'classical_exposed_ncard_le': 'OIBridge.KInfFoundations.classical_exposed_ncard_le', 'qubit_certain_face': 'OIBridge.KInfFoundations.qubit_certain_face', 'strictConvex_of_kInf1': 'OIBridge.KInfFoundations.strictConvex_of_kInf1', 'kinf1_kernel_core': 'OIBridge.KInfFoundations.kinf1_kernel_core'}
WORKFLOW_JOB = '  probes_kinf1:\n    name: Numerical probes / KINF-1 foundations\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: KINF-1 foundations probe\n        working-directory: verification/lean\n        run: |\n          echo "=== kinf_foundations_probe.py ==="\n          python3 kinf_foundations_probe.py\n'
WORKFLOW_EDITS = [('          python3 native_gate_ball_probe.py\n\n', '          python3 native_gate_ball_probe.py\n\n  probes_kinf1:\n    name: Numerical probes / KINF-1 foundations\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: KINF-1 foundations probe\n        working-directory: verification/lean\n        run: |\n          echo "=== kinf_foundations_probe.py ==="\n          python3 kinf_foundations_probe.py\n\n'), ('probes_nb1, probes_a42_witness', 'probes_nb1, probes_kinf1, probes_a42_witness'), ('          NB1_RESULT: ${{ needs.probes_nb1.result }}\n', '          NB1_RESULT: ${{ needs.probes_nb1.result }}\n          KINF1_RESULT: ${{ needs.probes_kinf1.result }}\n'), ('          echo "nb1=${NB1_RESULT}"\n', '          echo "nb1=${NB1_RESULT}"\n          echo "kinf1=${KINF1_RESULT}"\n'), ('          test "${NB1_RESULT}" = success\n', '          test "${NB1_RESULT}" = success\n          test "${KINF1_RESULT}" = success\n')]
IMPORT_EDIT = ('import OIBridge.NativeGateBall\n', 'import OIBridge.NativeGateBall\nimport OIBridge.KInfFoundations\n')
FAMILY = {'name': 'the field-neutral vocabulary of the pre-quantum operational completion and its elementary lemmas: finite stages, effects, supporting-effect completeness, singleton faces, elementary drivability, copy naturality, Lemmas B, C and D, the finite-exposure bounds, the qubit certain face, and hypothesis K-infinity-1 as a definition (round KINF-1, reconstruction)', 'modules': ['KInfFoundations'], 'status': 'kernel-only', 'manuscript': [], 'note': "Round KINF-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-kinf-1-foundations/preregistration.md. Definitions over a real normed space, with no field, matrix carrier or substratum object: FiniteStage with its state body, IsEffectOn, certainFace, SupportingEffectComplete, SingletonFaces, fullEffects, PerfectlyDistinguishable, CentrallySymmetric, ElementaryDrivability, CopyNatural, and KInf1, the statement of hypothesis K-infinity-1, proved for nothing. Theorems: states_isCompact and states_unit; Lemma C strictConvex_of_supporting_singleton; Lemma D card_le_two_of_centrallySymmetric; Lemma B eq_closedBall_of_frontier_subset_sphere; the finite-preparation bound exposed_ncard_le; Theorem F2 classical_exposed_ncard_le; qubit_certain_face, a theorem of the imported qubit matrix kinematics; verdict kinf1_kernel_core. The module sources none of its premises from any OI construction and contains no reconstruction theorem. The SIC, Caratheodory, torus, Stiefel and 3-ball instances are the round's probe kinf_foundations_probe.py, exact arithmetic and not the kernel. Carried by no manuscript."}
SENTENCES = {'KINF-1-FOUNDATIONS-PROVED': "In the kernel, at evidence level 2, over a real normed space and with no field, matrix carrier or substratum object: the state body of a finite observer stage is compact and lies on the unit hyperplane (`states_isCompact`, `states_unit`); a closed convex body with supporting-effect completeness and singleton faces is strictly convex (Lemma C, `strictConvex_of_supporting_singleton`); a centrally symmetric body admits at most two perfectly distinguishable states, with any family of effects and in particular with the full effects (Lemma D, `card_le_two_of_centrallySymmetric`, `card_le_two_of_centrallySymmetric_full`); a compact convex body with `0` in its interior whose frontier lies on the unit sphere is the closed unit ball (Lemma B, `eq_closedBall_of_frontier_subset_sphere`); a body generated by finitely many preparations exposes only their vectors (`exposed_mem_range`, `exposed_ncard_le`); a body realized on `N` ontic states and meeting each coordinate facet in at most one point exposes at most `N` states by response effects (Theorem F2, `classical_exposed_ncard_le`, through `response_eq_one_forces`); and, for the imported qubit kinematics, the certain face of the effect `ρ ↦ ρ 0 0` on density matrices is the single point `|0⟩⟨0|` (`qubit_certain_face`), joined in the verdict `kinf1_kernel_core`. Copy naturality is the pointwise conjugation identity (`copyNatural_iff_apply`), and hypothesis K∞-1 is stated as the definition `KInf1`, proved for nothing, with `strictConvex_of_kInf1` recording what it buys with singleton faces. In exact arithmetic replayed in CI, and not in the kernel, the round's probe instantiates the bounds and the lemmas: the SIC-embedded ball on four ontic states has exactly four exposed points, the tangency points, on a body with a continuum of extreme points; the Carathéodory orbitope `C₂` carries the exact capacity-three triple at `t = 0, 2π/3, 4π/3`; the torus and Stiefel orbitopes are centrally symmetric with flat faces exposed by valid effects, so singleton faces fail there while the capacity bound holds; and the 3-ball has singleton faces. Nothing here derives drivability, supporting effects, singleton faces or copy naturality from any OI construction, and nothing here is a reconstruction theorem.", 'KINF-1-UNDECIDED': 'The kernel verdict `kinf1_kernel_core` was not obtained. The statement at which the proof stopped is named, with what would settle it; the definitions stand as frozen, the exact layer stands as computed, and no lemma is stated as a result of this round beyond those the kernel checked.'}
CLAUSE = "Round KINF-1 fixes the field-neutral vocabulary of the pre-quantum operational completion — finite stages, effects and certain faces, supporting-effect completeness, singleton faces, full effects, perfect distinguishability, central symmetry, elementary drivability and copy naturality — and proves the elementary lemmas that vocabulary supports: Lemmas B, C and D, the finite-exposure bounds, and the qubit certain face as a theorem of the imported matrix kinematics. It states hypothesis K∞-1 as a definition and proves it for nothing. It sources none of its premises: it does not derive drivability, supporting effects, singleton faces or copy naturality from any OI construction, it does not decide whether the completion's effects are the full effects, and it contains no reconstruction theorem. It edits no manuscript and no roadmap row."
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PROBE_OK_PREFIX = 'kinf_foundations_probe: OK -- 384 checks'
FORBIDDEN_NOTE = ('OI supplies', 'OI derives', 'OI sources', 'sourced from OI', 'derived from the substratum', 'K∞-1 holds', 'K∞-1 is proved', 'KInf1 holds', 'proves K∞-1', 'reconstruction theorem for', 'the completion is a ball', 'full effects hold')
SYNTHETIC_PROBE = b'# synthetic probe for the self-test\n'
FORBIDDEN = ('sorry', 'admit', 'native_decide', 'axiom ', 'unsafe', 'opaque ', 'implemented_by', 'extern')
ALLOWED_OPTION = 'set_option linter.unusedSectionVars false'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


# ---- the expected tree ------------------------------------------------------------------------------------------
def expected_census(d_census):
    c = json.loads(d_census)
    c['families'].append(json.loads(json.dumps(FAMILY)))
    return (json.dumps(c, indent=2, ensure_ascii=False) + '\n').encode()


def expected_text(d_files, path):
    text = d_files[path].decode()
    if path == WORKFLOW:
        for old, new in WORKFLOW_EDITS:
            if text.count(old) != 1:
                raise ValueError('workflow anchor')
            text = text.replace(old, new)
        return text.encode()
    if path == IMPORTS:
        if text.count(IMPORT_EDIT[0]) != 1:
            raise ValueError('import anchor')
        return text.replace(*IMPORT_EDIT).encode()
    if path == CENSUS:
        return expected_census(d_files[path])
    return d_files[path]


# ---- the checks -------------------------------------------------------------------------------------------------
DECL_RE = re.compile(r'^(theorem|structure|def|noncomputable def|abbrev|instance|class|inductive) (\S+)', re.M)


def declaration(module, kind, name):
    """The frozen text of a declaration: a theorem from its keyword to the `:=` that opens its proof; a structure or
    a definition from its keyword to the blank line that ends it."""
    for sep in (' ', '\n'):
        k = module.find(kind + ' ' + name + sep)
        if k >= 0 and (k == 0 or module[k - 1] == '\n'):
            if kind == 'theorem':
                return module[k:module.index(':=', k) + 2]
            end = module.find('\n\n', k)
            return module[k:end if end >= 0 else len(module)]
    return None


def check_module(module, label):
    codes = []
    if not module.startswith(FROZEN['header']):
        codes.append('module:header')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok) + ('' if tok.endswith(' ') else r'(?![A-Za-z_])'), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    found = DECL_RE.findall(module)
    theorems = [n for k, n in found if k == 'theorem']
    for kind, n in found:
        if kind == 'theorem':
            if n not in FROZEN['declarations'] and not n.startswith('kinf1_shared_'):
                codes.append('module:unknown-name:' + n)
            line = PRINT.get(n, 'OIBridge.KInfFoundations.' + n)
            if module.count('#print axioms ' + line + '\n') != 1:
                codes.append('module:print-axioms:' + n)
        elif n not in FROZEN['declarations'] or FROZEN['declarations'][n][0] != kind:
            codes.append('module:unknown-definition:' + n)
    for n, (kind, text) in FROZEN['declarations'].items():
        if n == VERDICT and label != LABELS[0]:
            if n in theorems:
                codes.append('module:verdict-under-undecided')
            continue
        if declaration(module, kind, n) != text:
            codes.append('module:declaration:' + n)
    return codes


def check_note(note, label, module_blob):
    codes = []
    lines = note.split('\n')
    outs = [l for l in lines if l.startswith('**Outcome:**')]
    if outs != ['**Outcome:** `%s`' % label]:
        codes.append('note:outcome-line')
    for lab in LABELS:
        if note.count(SENTENCES[lab]) != (1 if lab == label else 0):
            codes.append('note:sentence:' + lab)
    if note.count(CLAUSE_MENTION) != 1 or note.count(CLAUSE) != 1 \
            or note.index(CLAUSE) < note.index(CLAUSE_MENTION):
        codes.append('note:clause')
    if sum(1 for l in lines if l.strip().strip('`').startswith(PROBE_OK_PREFIX)) != 1:
        codes.append('note:probe-line')
    if '`%s`' % REFERENCE_BLOB not in note or '`%s`' % module_blob not in note:
        codes.append('note:blobs')
    if module_blob != REFERENCE_BLOB and 'departure from the reference implementation' not in note:
        codes.append('note:departure')
    rest = note
    for t in list(SENTENCES.values()) + [CLAUSE]:
        rest = rest.replace(t, '')
    if any(ph.lower() in rest.lower() for ph in FORBIDDEN_NOTE):
        codes.append('note:forbidden-claim')
    return codes


def check_tree(d_files, e_files, changed, probe_blob=PROBE_BLOB):
    """d_files/e_files: path -> bytes (None if absent) for every path consulted; changed: {path: 'A'|'M'|'D'}."""
    codes = []
    note = e_files.get(RDIR + 'result.md')
    if note is None:
        return ['note:absent']
    note = note.decode()
    m = re.search(r'^\*\*Outcome:\*\* `([^`]*)`', note, re.M)
    label = m.group(1) if m and m.group(1) in LABELS else None
    if label is None:
        return ['note:outcome-line']
    module = e_files.get(MODULE)
    if module is None:
        return ['module:absent']
    codes += check_module(module.decode(), label)
    codes += check_note(note, label, blob(module))
    if e_files.get(PROBE) is None or blob(e_files[PROBE]) != probe_blob:
        codes.append('probe:blob')
    for path in (WORKFLOW, IMPORTS, CENSUS):
        try:
            exp = expected_text(d_files, path)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
            MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if changed != want:
        codes.append('paths')
    return codes


# ---- git access -------------------------------------------------------------------------------------------------
def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def consulted():
    return [RDIR + 'result.md', RDIR + 'preregistration.md', MODULE, PROBE, WORKFLOW, IMPORTS, CENSUS]


def cmd_check(commit, freeze=None):
    d_files = {p: show(D, p) for p in consulted()}
    e_files = {p: show(commit, p) for p in consulted()}
    changed = {}
    for line in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, path = line.split('\t', 1)
        changed[path] = st
    codes = check_tree(d_files, e_files, changed)
    if freeze:
        fdiff = git('diff', '--no-renames', '--name-status', D, freeze).decode().split()
        if fdiff != ['A', RDIR + 'preregistration.md']:
            codes.append('freeze:delta')
        if show(freeze, RDIR + 'preregistration.md') != e_files[RDIR + 'preregistration.md']:
            codes.append('freeze:preregistration')
    if codes:
        print('controls: check FAILED: ' + '; '.join(codes))
        return 1
    print('controls: check OK')
    return 0


# ---- self-test --------------------------------------------------------------------------------------------------
def synthetic_module(label):
    parts = [FROZEN['header'], 'namespace OIBridge\nnamespace KInfFoundations\n\n']
    names = []
    for n, (kind, text) in FROZEN['declarations'].items():
        if n == VERDICT and label != LABELS[0]:
            continue
        if kind == 'theorem':
            parts.append(text + ' by\n  exact placeholder\n\n')
            names.append(n)
        else:
            parts.append(text + '\n\n')
    parts.append('end KInfFoundations\nend OIBridge\n\n')
    for n in names:
        parts.append('#print axioms %s\n' % PRINT[n])
    return ''.join(parts).encode()


def synthetic_row(d_files, label):
    e = dict(d_files)
    module = synthetic_module(label)
    e[MODULE] = module
    e[PROBE] = SYNTHETIC_PROBE
    for path in (WORKFLOW, IMPORTS, CENSUS):
        e[path] = expected_text(d_files, path)
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % label, '', SENTENCES[label], '', CLAUSE_MENTION, '', CLAUSE, '',
            '`' + PROBE_OK_PREFIX + ' (synthetic)`', '',
            'reference `%s`, module at E `%s`, departure from the reference implementation' % (REFERENCE_BLOB, blob(module))]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
               MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    return e, changed


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    bad = []
    for lab in LABELS:
        if prereg.count(SENTENCES[lab]) != 1:
            bad.append('prereg:sentence:' + lab)
    if prereg.count(CLAUSE) < 1:
        bad.append('prereg:clause')
    if FROZEN['header'].rstrip('\n') not in prereg:
        bad.append('prereg:header')
    for n, (kind, text) in FROZEN['declarations'].items():
        if text not in prereg:
            bad.append('prereg:declaration:' + n)
    if WORKFLOW_JOB not in prereg:
        bad.append('prereg:workflow')
    if FAMILY['name'] not in prereg or FAMILY['note'] not in prereg:
        bad.append('prereg:census-family')
    for b in (PROBE_BLOB, REFERENCE_BLOB):
        if b not in prereg:
            bad.append('prereg:blob:' + b)
    if prereg.count(PROBE_OK_PREFIX) < 1:
        bad.append('prereg:probe-line')
    if bad:
        print('controls: self-test FAILED (constants): ' + '; '.join(bad))
        return 1
    print('controls: the frozen constants match the preregistration beside this file')

    d_files = {p: show(D, p) for p in consulted()}
    rows = {}
    for lab in LABELS:
        e, ch = synthetic_row(d_files, lab)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if codes:
            print('controls: self-test FAILED: synthetic row %s: %s' % (lab, codes))
            return 1
        rows[lab] = (e, ch)
    print('controls: 2 rows hold as frozen')

    muts = []
    def mut(name, code, label, fn):
        muts.append((name, code, label, fn))
    P, U = LABELS
    def edit_file(path, old, new):
        def f(e, ch):
            if old.encode() not in e[path]:
                raise AssertionError('mutation anchor absent: ' + old)
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    def append_note(text):
        return lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + text.encode())
    mut('verdict removed under FOUNDATIONS-PROVED', 'module:declaration:' + VERDICT, P,
        edit_file(MODULE, 'theorem ' + VERDICT, 'theorem kinf1_other'))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['declarations'][VERDICT][1].encode()
                                    + b' by\n  x\n#print axioms ' + PRINT[VERDICT].encode() + b'\n'))
    mut('K-infinity-1 made a theorem', 'module:declaration:KInf1', P,
        edit_file(MODULE, 'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=',
                  'def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := True ∧'))
    mut('supporting-effect completeness weakened', 'module:declaration:SupportingEffectComplete', P,
        edit_file(MODULE, '∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x = 1',
                  '∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x ≤ 1'))
    mut('singleton faces weakened', 'module:declaration:SingletonFaces', P,
        edit_file(MODULE, '(certainFace Ω e).Subsingleton', '(certainFace Ω e).Nonempty'))
    mut('Lemma C without singleton faces', 'module:declaration:strictConvex_of_supporting_singleton', P,
        edit_file(MODULE, '(hSEC : SupportingEffectComplete Ω avail) (hSF : SingletonFaces Ω avail) :\n    StrictConvex ℝ Ω :=',
                  '(hSEC : SupportingEffectComplete Ω avail) :\n    StrictConvex ℝ Ω :='))
    mut('Lemma D loosened', 'module:declaration:card_le_two_of_centrallySymmetric', P,
        edit_file(MODULE, '(hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :=',
                  '(hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 3 :='))
    mut('Lemma B without the interior hypothesis', 'module:declaration:eq_closedBall_of_frontier_subset_sphere', P,
        edit_file(MODULE, '(hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)', '(hcomp : IsCompact Ω)'))
    mut('Theorem F2 without the facet hypothesis', 'module:declaration:classical_exposed_ncard_le', P,
        edit_file(MODULE, '    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :\n    {x | ClassicallyExposed Ω x}.ncard ≤ N :=',
                  '    {x | ClassicallyExposed Ω x}.ncard ≤ N :='))
    mut('the header claims a sourcing', 'module:header', P,
        edit_file(MODULE, 'It\n  sources nothing', 'It\n  sources drivability'))
    mut('an import added to the header', 'module:header', P,
        edit_file(MODULE, 'import OIBridge.CoherentExtension\n', 'import OIBridge.CoherentExtension\nimport OIBridge.SubstratumSource\n'))
    mut('a definition added', 'module:unknown-definition:extra', P,
        edit_file(MODULE, 'end KInfFoundations', 'def extra : Nat := 0\n\nend KInfFoundations'))
    mut('a missing #print axioms', 'module:print-axioms:strictConvex_of_supporting_singleton', P,
        edit_file(MODULE, '#print axioms OIBridge.KInfFoundations.strictConvex_of_supporting_singleton\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an axiom declared', 'module:forbidden:axiom', P,
        edit_file(MODULE, 'end KInfFoundations', 'axiom kinf : True\n\nend KInfFoundations'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        edit_file(MODULE, 'end KInfFoundations', 'theorem helper : True := trivial\n\nend KInfFoundations'))
    mut('a set_option', 'module:set_option', P,
        edit_file(MODULE, 'namespace KInfFoundations\n', 'namespace KInfFoundations\nset_option maxHeartbeats 0\n'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${KINF1_RESULT}" = success\n', ''))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.KInfFoundations\n'))
    mut('the census family made current', 'surface:' + CENSUS, P,
        lambda e, ch: e.__setitem__(CENSUS, b'"status": "current"'.join(e[CENSUS].rsplit(b'"status": "kernel-only"', 1))))
    mut('a manuscript touched', 'paths', P, lambda e, ch: ch.__setitem__('papers/Main.md', 'M'))
    mut('the roadmap touched', 'paths', P, lambda e, ch: ch.__setitem__('verification/ROADMAP.md', 'M'))
    mut('a governed path missing', 'paths', P, lambda e, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line', P, append_note('\n**Outcome:** `%s`\n' % U))
    mut("the other label's sentence", 'note:sentence:' + U, P, append_note('\n' + SENTENCES[U]))
    mut('the clause missing', 'note:clause', P, edit_file(RDIR + 'result.md', CLAUSE, ''))
    mut('the clause before its mention', 'note:clause', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', CLAUSE.encode() + b'\n' + e[RDIR + 'result.md'].replace(CLAUSE.encode(), b'')))
    mut('the probe line missing', 'note:probe-line', P, edit_file(RDIR + 'result.md', PROBE_OK_PREFIX, 'probe'))
    mut('the blobs missing', 'note:blobs', P, edit_file(RDIR + 'result.md', REFERENCE_BLOB, 'x'))
    mut('the departure unreported', 'note:departure', P,
        edit_file(RDIR + 'result.md', 'departure from the reference implementation', ''))
    mut('the note claims OI supplies the premises', 'note:forbidden-claim', P,
        append_note('\nHence OI supplies drivability.\n'))
    mut('the note claims K-infinity-1 holds', 'note:forbidden-claim', U, append_note('\nSo K∞-1 holds.\n'))
    mut('no result note', 'note:absent', P, lambda e, ch: e.__setitem__(RDIR + 'result.md', None))
    failed = 0
    for name, code, lab, fn in muts:
        e, ch = synthetic_row(d_files, lab)
        fn(e, ch)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if code not in codes:
            print('controls: self-test FAILED: mutation "%s" did not fail with %s (got %s)' % (name, code, codes))
            failed += 1
    if failed:
        return 1
    print('controls: %d mutation controls fail as required' % len(muts))
    print('controls: self-test OK')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) in (2, 4) and a[0] == 'check' and (len(a) == 2 or a[2] == '--freeze'):
        sys.exit(cmd_check(a[1], a[3] if len(a) == 4 else None))
    print(__doc__)
    sys.exit(2)
