#!/usr/bin/env python3
"""controls.py -- act 45's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the module's frozen statements and definitions, the frozen manuscript and
roadmap insertions, the census transform, the workflow edit, the import line, the probe blob, the outcome sentences and
the clause.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; two synthetic
                                            rows (PROVED, UNDECIDED) that must hold; mutation controls that must fail
                                            with their named codes
"""
import hashlib, json, os, re, subprocess, sys

D = 'fa6ddf77703a8ce7f9eaf573ef48355194d72541'
RDIR = 'verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/'
MODULE = 'verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean'
PROBE = 'verification/lean/fixed_basis_ancilla_probe.py'
PROBE_BLOB = '8419549b598131a4bdef36e8c9ce82690cdaac6c'
REFERENCE_BLOB = '9d6086bbe3af28e576adf2fb51784b02a5d66e5f'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
ROADMAP = 'verification/ROADMAP.md'
MANUSCRIPTS = ['papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
               'book/The-Incompleteness-of-Observation-FULL.md']
BUILT = {'papers/Main.md': 'papers/Main', 'papers/Explainer.md': 'papers/Explainer',
         'book/The-Incompleteness-of-Observation-FULL.md': 'book/The-Incompleteness-of-Observation-FULL'}
LABELS = ('A45-BRIDGE-PROVED', 'A45-UNDECIDED')

EDITS = {'papers/Main.md': [('can lie in different two-sided classes and differ in their relating evolution. A', "t one time that residue is not seen by the fixed-basis layer. Take a lift with trivial ancilla at one time and form the fixed-basis datum whose evolution is the lift's unitary, with uniform initial law and identity readout: its finite-horizon trajectory laws are determined by the visible law alone, and remain so after the unitary is composed on either side with contractively scaled partial permutations; two such data have equal trajectory laws exactly when their visible laws are equal; and each such law is fixed-basis realizable and stochastic, hence inside $S \\iff D \\iff Q_{\\mathrm{fb}}$ (kernel: `bridge_traj`, `rooted_eq_iff_slice_eq`, `realData_traj_stochastic`). The fixed-basis correspondence therefore acts on the quotient by visible equality, and two lifts of one visible law in different two-sided classes are not separated by it. The trivial ancilla is part of the statement: an ancilla attached as a tensor factor with its own unitary leaves the rooted family unchanged (kernel: `padData_rooted`), whereas an ancilla carried between steps as hidden basis states, in a lift that is not a tensor product, can separate two lifts of one visible law that share every column entering the visible law, already in the two-step law (exact computation). A")], 'papers/Explainer.md': [('two lifts of one visible law can differ in it and differ in relating evolution. ', "That residue does not reach the fixed-basis layer. With a trivial ancilla, the fixed-basis datum built from a lift's unitary at one time, with uniform initial law and identity readout, has finite-horizon trajectory laws fixed by the visible law alone, also after contractively scaled partial permutations on either side, and two such data have equal laws exactly when their visible laws are equal (kernel: `bridge_traj`, `rooted_eq_iff_slice_eq`); the fixed-basis correspondence acts on the quotient by visible equality. The trivial ancilla is part of that statement: an ancilla attached as a tensor factor with its own unitary leaves the rooted family unchanged, while an ancilla carried between steps as hidden basis states can separate two lifts that share every column entering the visible law, already in the two-step law. ")], 'book/ch01-observation.md': [('two lifts of one visible law can differ in it and differ in relating evolution. ', "That residue does not reach the fixed-basis layer. With a trivial ancilla, the fixed-basis datum built from a lift's unitary at one time, with uniform initial law and identity readout, has finite-horizon trajectory laws fixed by the visible law alone, also after contractively scaled partial permutations on either side, and two such data have equal laws exactly when their visible laws are equal; the fixed-basis correspondence acts on the quotient by visible equality. The trivial ancilla is part of that statement: an ancilla attached as a tensor factor with its own unitary leaves the rooted family unchanged, while an ancilla carried between steps as hidden basis states can separate two lifts that share every column entering the visible law, already in the two-step law. ")], 'book/ch19-open-problems.md': [('aw leaves at one time is exactly the off-diagonal fibre-Gram\ndata modulo phases.', " At one time that freedom does not reach the fixed-basis layer. With a trivial\nancilla, the fixed-basis datum built from a lift's unitary, with uniform initial law and identity\nreadout, has finite-horizon trajectory laws fixed by the visible law alone, also after contractively\nscaled partial permutations on either side, and two such data have equal laws exactly when their\nvisible laws are equal ([Main §3.4]). The trivial ancilla is part of the statement: an ancilla\ncarried between steps as hidden basis states can separate two lifts of one visible law already in\nthe two-step law, while an ancilla attached as a tensor factor with its own unitary cannot.")], 'book/The-Incompleteness-of-Observation-FULL.md': [('two lifts of one visible law can differ in it and differ in relating evolution. ', "That residue does not reach the fixed-basis layer. With a trivial ancilla, the fixed-basis datum built from a lift's unitary at one time, with uniform initial law and identity readout, has finite-horizon trajectory laws fixed by the visible law alone, also after contractively scaled partial permutations on either side, and two such data have equal laws exactly when their visible laws are equal; the fixed-basis correspondence acts on the quotient by visible equality. The trivial ancilla is part of that statement: an ancilla attached as a tensor factor with its own unitary leaves the rooted family unchanged, while an ancilla carried between steps as hidden basis states can separate two lifts that share every column entering the visible law, already in the two-step law. "), ('aw leaves at one time is exactly the off-diagonal fibre-Gram\ndata modulo phases.', " At one time that freedom does not reach the fixed-basis layer. With a trivial\nancilla, the fixed-basis datum built from a lift's unitary, with uniform initial law and identity\nreadout, has finite-horizon trajectory laws fixed by the visible law alone, also after contractively\nscaled partial permutations on either side, and two such data have equal laws exactly when their\nvisible laws are equal ([Main §3.4]). The trivial ancilla is part of the statement: an ancilla\ncarried between steps as hidden basis states can separate two lifts of one visible law already in\nthe two-step law, while an ancilla attached as a tensor factor with its own unitary cannot.")], 'verification/ROADMAP.md': [("ts 36 to 40 is classified, nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any realizable class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle. ", "The single-time residue does not reach the fixed-basis layer: for a trivial-ancilla lift at one time, the fixed-basis datum with the lift's unitary, uniform initial law and identity readout has finite-horizon trajectory laws determined by the visible law, also under `permClass` interventions on either side, two such data have equal laws exactly when their visible laws are equal, and each law lies inside `S ⇔ D ⇔ Q_fb` (act 45's kernel); a tensor-factor ancilla leaves the rooted family unchanged, and an ancilla carried between steps as hidden basis states separates lifts of one visible law at two steps; `P0`'s cross-time parts are untouched, no relation is adopted as the physical one, and nothing here names, endorses or excludes a selection principle. ")]}
FROZEN = {'header': "/-\n  OIBridge/TrackBQfbBridge.lean — Track B act 45: the fixed-basis image of a single-time lift.\n\n  For a trivial-ancilla admissible dilation `pad U` of a visible slice `G`, the fixed-basis datum\n  `realData U` takes `U` as its evolution, with a uniform initial law and the identity readout (the\n  initial law and readout of `hadData`); no field is added.\n\n  - `bridge`, `bridge_traj`: two such dilations of one slice, composed on either side with `permClass`\n    interventions, give equal Born weights, rooted families and root-conditioned trajectory laws.\n  - `rooted_eq_iff_slice_eq`: the rooted families agree exactly when the slices are equal; forward\n    `slice_eq_of_rooted_eq`, backward `visible_congr`.\n  - `realData_traj_stochastic`: each trajectory law of a unitary realization is `Q_fb`-realizable and\n    stochastic, by the landed `qfbRealizable_rootTraj` and `Qfb_imp_S`.\n  - The flat 16 × 16 instance: `UH_unitary`, `UH_born_eq_slice`, `UH_admissible`, `flat_bridge`.\n  - `a45_bridge_kernel`: the verdict, the conjunction the round freezes.\n\n  Scope.  Trivial ancilla; interventions in `permClass`; the relation proved is equality of the visible\n  slice.  Nothing here concerns an intervention outside `permClass`, a nontrivial ancilla, or a relation\n  finer than equality of the visible slice, and nothing recovers a realization's class from its data.\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/\nimport OIBridge.QuantumRepresentation\nimport OIBridge.DilationChoice\nimport OIBridge.SubstratumInterfaceAudit\nimport OIBridge.DitaHull\n\n", 'defs': {'realData': 'noncomputable def realData (U : Matrix V V ℂ) : QfbData V where\n  Bas := V\n  fB := inferInstance\n  dB := inferInstance\n  U := U\n  init := fun _ => 1 / (Fintype.card V : ℝ)\n  read := id', 'pad': 'def pad (U : Matrix V V ℂ) : Matrix (V × (Fin 1 × Fin 1)) (V × (Fin 1 × Fin 1)) ℂ :=\n  Matrix.of fun p q => U p.1 q.1', 'IsFlatHadamard': 'def IsFlatHadamard (H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) : Prop :=\n  (∀ i j, ‖H i j‖ = 1) ∧ H * Hᴴ = (16 : ℂ) • (1 : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)', 'UH': 'noncomputable def UH (H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) :\n    Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ :=\n  (4⁻¹ : ℂ) • H'}, 'statements': {'realData_born': "theorem realData_born (U : Matrix V V ℂ) (b b' : V) : (realData U).born b b' = ‖U b' b‖ ^ 2 :=", 'realData_isLaw': 'theorem realData_isLaw [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ) :\n    (realData U).IsLaw :=', 'realData_rootMass': 'theorem realData_rootMass (U : Matrix V V ℂ) (a : V) :\n    (realData U).rootMass a = 1 / (Fintype.card V : ℝ) :=', 'realData_positiveRootMass': 'theorem realData_positiveRootMass (U : Matrix V V ℂ) : (realData U).PositiveRootMass :=', 'realData_qstar': 'theorem realData_qstar [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ) :\n    QStar (fun t => Matrix.of fun a j => (realData U).rooted t a j) :=', 'bornPow_congr': "theorem bornPow_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (t : ℕ) :\n    ∀ b b' : V, (realData U).bornPow t b b' = (realData U').bornPow t b b' :=", 'rooted_congr': "theorem rooted_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2)\n    (t : ℕ) (a j : V) : (realData U).rooted t a j = (realData U').rooted t a j :=", 'slice_of_admissible': 'theorem slice_of_admissible {G : Matrix V V ℝ} {U : Matrix V V ℂ}\n    (h : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U)) (i j : V) :\n    G i j = ‖U i j‖ ^ 2 :=', 'visible_congr': "theorem visible_congr {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}\n    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))\n    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U')) :\n    (∀ b b', (realData U).born b b' = (realData U').born b b') ∧\n      ∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j :=", 'realData_bornPow_one': "theorem realData_bornPow_one (U : Matrix V V ℂ) (b b' : V) :\n    (realData U).bornPow 1 b b' = ‖U b' b‖ ^ 2 :=", 'realData_rooted_one': 'theorem realData_rooted_one (U : Matrix V V ℂ) (a j : V) :\n    (realData U).rooted 1 a j = ‖U j a‖ ^ 2 :=', 'slice_eq_of_rooted_eq': "theorem slice_eq_of_rooted_eq {U U' : Matrix V V ℂ}\n    (h : ∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j) (i j : V) :\n    ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2 :=", 'rooted_eq_iff_slice_eq': "theorem rooted_eq_iff_slice_eq {G G' : Matrix V V ℝ} {U U' : Matrix V V ℂ}\n    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))\n    (hU' : AdmissibleDilationAt G' ((0 : Fin 1), (0 : Fin 1)) (pad U')) :\n    (∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j) ↔ G = G' :=", 'exists_row_single': 'theorem exists_row_single {M : Matrix V V ℂ} (hM : IsSubmonomial M) (i : V) :\n    ∃ k₀, ∀ k, k ≠ k₀ → M i k = 0 :=', 'exists_col_single': 'theorem exists_col_single {N : Matrix V V ℂ} (hN : IsSubmonomial N) (j : V) :\n    ∃ l₀, ∀ l, l ≠ l₀ → N l j = 0 :=', 'mul_mul_apply_single': 'theorem mul_mul_apply_single (M U N : Matrix V V ℂ) {i j k₀ l₀ : V}\n    (hk : ∀ k, k ≠ k₀ → M i k = 0) (hl : ∀ l, l ≠ l₀ → N l j = 0) :\n    (M * U * N) i j = M i k₀ * U k₀ l₀ * N l₀ j :=', 'normSq_mul_mul_congr': "theorem normSq_mul_mul_congr {M N U U' : Matrix V V ℂ} (hM : IsSubmonomial M)\n    (hN : IsSubmonomial N) (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (i j : V) :\n    ‖(M * U * N) i j‖ ^ 2 = ‖(M * U' * N) i j‖ ^ 2 :=", 'bridge': "theorem bridge {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}\n    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))\n    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U'))\n    {M N : Matrix V V ℂ} (hM : permClass V M) (hN : permClass V N) :\n    (∀ i j, ‖(M * U * N) i j‖ ^ 2 = ‖(M * U' * N) i j‖ ^ 2) ∧\n      ∀ t a j, (realData (M * U * N)).rooted t a j = (realData (M * U' * N)).rooted t a j :=", 'rootTraj_congr': "theorem rootTraj_congr {U U' : Matrix V V ℂ} (h : ∀ i j, ‖U i j‖ ^ 2 = ‖U' i j‖ ^ 2) (K : ℕ) (a : V) :\n    (realData U).rootTraj K a = (realData U').rootTraj K a :=", 'bridge_traj': "theorem bridge_traj {G : Matrix V V ℝ} {U U' : Matrix V V ℂ}\n    (hU : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U))\n    (hU' : AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U'))\n    {M N : Matrix V V ℂ} (hM : permClass V M) (hN : permClass V N) (K : ℕ) (a : V) :\n    (realData (M * U * N)).rootTraj K a = (realData (M * U' * N)).rootTraj K a :=", 'realData_traj_stochastic': 'theorem realData_traj_stochastic [Nonempty V] {U : Matrix V V ℂ} (hU : U ∈ Matrix.unitaryGroup V ℂ)\n    (K : ℕ) (a : V) :\n    OIBridge.Equivalence.QfbRealizable ((realData U).rootTraj K a) ∧\n      OIBridge.Equivalence.Stochastic ((realData U).rootTraj K a) :=', 'UH_unitary': 'theorem UH_unitary {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) :\n    UH H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=', 'UH_norm': 'theorem UH_norm {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H)\n    (i j : Fin 4 × Fin 4) : ‖UH H i j‖ = 1 / 4 :=', 'UH_born_eq_slice': "theorem UH_born_eq_slice (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)\n    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))\n    {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) (b b' : Fin 4 × Fin 4) :\n    (realData (UH H)).born b b' = 1 / 16 ∧ (realData (UH H)).born b b' = Γ₀ b'.1 b.1 * Γ₀ b'.2 b.2 :=", 'UH_admissible': 'theorem UH_admissible (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)\n    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))\n    {H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H) :\n    AdmissibleDilationAt (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)\n      ((0 : Fin 1), (0 : Fin 1)) (pad (UH H)) :=', 'flat_bridge': "theorem flat_bridge (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)\n    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))\n    {H H' : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ} (hH : IsFlatHadamard H)\n    (hH' : IsFlatHadamard H') :\n    (realData (UH H)).IsLaw ∧ (realData (UH H)).PositiveRootMass ∧\n      (realData (UH H')).IsLaw ∧ (realData (UH H')).PositiveRootMass ∧\n      ∀ {M N : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ},\n        permClass (Fin 4 × Fin 4) M → permClass (Fin 4 × Fin 4) N →\n        (∀ i j, ‖(M * UH H * N) i j‖ ^ 2 = ‖(M * UH H' * N) i j‖ ^ 2) ∧\n          ∀ t a j, (realData (M * UH H * N)).rooted t a j\n            = (realData (M * UH H' * N)).rooted t a j :=", 'a45_bridge_kernel': "theorem a45_bridge_kernel :\n    (∀ (W : Type) [Fintype W] [DecidableEq W] (G : Matrix W W ℝ) (U U' : Matrix W W ℂ),\n      AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U) →\n      AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U') →\n      ∀ (M N : Matrix W W ℂ), permClass W M → permClass W N → ∀ (K : ℕ) (a : W),\n        (realData (M * U * N)).rootTraj K a = (realData (M * U' * N)).rootTraj K a) ∧\n    (∀ (W : Type) [Fintype W] [DecidableEq W] (G G' : Matrix W W ℝ) (U U' : Matrix W W ℂ),\n      AdmissibleDilationAt G ((0 : Fin 1), (0 : Fin 1)) (pad U) →\n      AdmissibleDilationAt G' ((0 : Fin 1), (0 : Fin 1)) (pad U') →\n      ((∀ t a j, (realData U).rooted t a j = (realData U').rooted t a j) ↔ G = G')) ∧\n    (∀ (W : Type) [Fintype W] [DecidableEq W] [Nonempty W] (U : Matrix W W ℂ),\n      U ∈ Matrix.unitaryGroup W ℂ → ∀ (K : ℕ) (a : W),\n        OIBridge.Equivalence.QfbRealizable ((realData U).rootTraj K a) ∧\n          OIBridge.Equivalence.Stochastic ((realData U).rootTraj K a)) ∧\n    (∀ H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, IsFlatHadamard H →\n      UH H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧\n        ∀ b b' : Fin 4 × Fin 4, (realData (UH H)).born b b' = 1 / 16) :="}}
WORKFLOW_EDITS = [('  probes_foundations:\n    name: Numerical probes / foundations\n', '  probes_a45:\n    name: Numerical probes / A45 ancilla\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: A45 fixed-basis ancilla probe\n        working-directory: verification/lean\n        run: |\n          echo "=== fixed_basis_ancilla_probe.py ==="\n          python3 fixed_basis_ancilla_probe.py\n\n  probes_foundations:\n    name: Numerical probes / foundations\n'), ('probes_a41_hulls, probes_foundations]', 'probes_a41_hulls, probes_a45, probes_foundations]'), ('          A41H_RESULT: ${{ needs.probes_a41_hulls.result }}\n', '          A41H_RESULT: ${{ needs.probes_a41_hulls.result }}\n          A45_RESULT: ${{ needs.probes_a45.result }}\n'), ('          echo "a41_hulls=${A41H_RESULT}"\n', '          echo "a41_hulls=${A41H_RESULT}"\n          echo "a45=${A45_RESULT}"\n'), ('          test "${A41H_RESULT}" = success\n', '          test "${A41H_RESULT}" = success\n          test "${A45_RESULT}" = success\n')]
IMPORT_EDIT = ('import OIBridge.DitaTorusLocus\n', 'import OIBridge.DitaTorusLocus\nimport OIBridge.TrackBQfbBridge\n')
FAMILY = {'name': 'the fixed-basis image of a single-time lift: trajectory laws determined by the visible law, stable under contractively scaled partial permutations, equal exactly when the visible laws are equal (act 45, Track B)', 'modules': ['TrackBQfbBridge'], 'status': 'current', 'manuscript': [{'file': 'papers/Main.md', 'anchor': '`bridge_traj`'}, {'file': 'papers/Main.md', 'anchor': '`rooted_eq_iff_slice_eq`'}, {'file': 'papers/Main.md', 'anchor': '`realData_traj_stochastic`'}, {'file': 'papers/Explainer.md', 'anchor': 'That residue does not reach the fixed-basis layer'}, {'file': 'book/ch01-observation.md', 'anchor': 'That residue does not reach the fixed-basis layer'}, {'file': 'book/ch19-open-problems.md', 'anchor': 'At one time that freedom does not reach the fixed-basis layer.'}], 'note': "Track B act 45, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/track-b/act-45-fixed-basis-image/preregistration.md. For a trivial-ancilla admissible dilation, realData takes the unitary as the evolution of a QfbData with uniform initial law and identity readout. bridge and bridge_traj: two dilations of one visible slice give equal Born weights, rooted families and root-conditioned trajectory laws after any permClass interventions on either side; rooted_eq_iff_slice_eq: equal rooted families exactly when the slices are equal (forward slice_eq_of_rooted_eq, backward visible_congr); realData_traj_stochastic: each trajectory law is QfbRealizable and Stochastic through the landed qfbRealizable_rootTraj and Qfb_imp_S. Flat 16 x 16 instance: UH_unitary, UH_born_eq_slice, UH_admissible, flat_bridge. Verdict a45_bridge_kernel. The carried- and tensor-factor-ancilla computations are the round's probe fixed_basis_ancilla_probe.py, not the kernel."}
OPSRC_ANCHOR = {'file': 'papers/Main.md', 'anchor': '`padData_rooted`'}
SENTENCES = {'A45-BRIDGE-PROVED': "For a trivial-ancilla admissible dilation `pad U` of a visible slice `G`, the fixed-basis datum `realData U` — evolution `U`, uniform initial law, identity readout — has root-conditioned trajectory laws determined by `G` alone, also after `permClass` interventions on either side of `U`; its rooted families agree with those of a second such datum exactly when the two slices are equal; and each of its trajectory laws is `Q_fb`-realizable and stochastic, so it lies in the class the landed equivalence `S ⇔ D ⇔ Q_fb` describes. At the product configuration every flat 16 × 16 Hadamard `H` gives the unitary `U_H = H/4`, whose Born weights are `1/16`, the entries of `Γ₀ ⊗ Γ₀`. These are kernel theorems at evidence level 2. The round's probe computes, in exact arithmetic and not in the kernel, that an ancilla carried between steps as hidden basis states separates two dilations of one slice that share every column entering the slice, at two steps, while an ancilla attached as a tensor factor leaves the rooted family equal to `Gᵗ`. This is a statement about the frozen mathematical objects; it recovers no realization's class from its data, adopts no relation, carrier or intervention class as the physical one, and leaves `P0`'s cross-time parts open.", 'A45-UNDECIDED': 'The kernel package `P_R` was not obtained. The step at which the proof stopped is named, with what would settle it.'}
CLAUSE = "Act 45 proves statements about the fixed-basis data that a single-time trivial-ancilla lift instantiates, and adopts none of them as anything but mathematics. A `BRIDGE-PROVED` verdict settles, for trivial-ancilla admissible dilations and the fixed-basis datum with the dilation's unitary as its evolution, a uniform initial law and the identity readout, that the root-conditioned trajectory laws are determined by the visible slice, also after `permClass` interventions on either side, that the rooted families agree exactly when the slices are equal, and that each trajectory law is fixed-basis realizable and stochastic. It recovers no realization's class from its data, proves nothing in the kernel about a nontrivial ancilla, adopts no relation, carrier or intervention class as the physical one, and leaves `P0`'s cross-time parts open; no principle gains physical status by appearing here, and nothing here names, endorses or excludes a selection principle."
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PROBE_OK_PREFIX = 'fixed_basis_ancilla_probe: OK -- 16 checks'
SYNTHETIC_PROBE = b'# synthetic probe for the self-test\n'
FORBIDDEN = ('sorry', 'admit', 'native_decide', 'axiom ', 'unsafe', 'opaque ', 'implemented_by', 'extern')
ALLOWED_OPTION = 'set_option linter.unusedSectionVars false'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


# ---- the expected tree ------------------------------------------------------------------------------------------
def expected_census(d_census, label):
    c = json.loads(d_census)
    fam = json.loads(json.dumps(FAMILY))
    if label == 'A45-BRIDGE-PROVED':
        for f in c['families']:
            if f['modules'] == ['OperationalSourcing']:
                f['status'] = 'current'
                f['manuscript'] = [OPSRC_ANCHOR]
    else:
        fam['status'] = 'kernel-only'
        fam['manuscript'] = []
    c['families'].append(fam)
    return (json.dumps(c, indent=2, ensure_ascii=False) + '\n').encode()


def apply_edits(text, edits):
    for anchor, ins in edits:
        if text.count(anchor) != 1:
            raise ValueError('anchor not unique')
        text = text.replace(anchor, anchor + ins)
    return text


def expected_text(d_files, path, label):
    text = d_files[path].decode()
    if path == WORKFLOW:
        for old, new in WORKFLOW_EDITS:
            if text.count(old) != 1:
                raise ValueError('workflow anchor')
            text = text.replace(old, new)
        return text.encode()
    if path == IMPORTS:
        return text.replace(*IMPORT_EDIT).encode()
    if path == CENSUS:
        return expected_census(d_files[path], label)
    if label == 'A45-BRIDGE-PROVED' and path in EDITS:
        return apply_edits(text, EDITS[path]).encode()
    return d_files[path]


# ---- the checks -------------------------------------------------------------------------------------------------
def statement(module, name):
    for sep in (' ', '\n'):
        k = module.find('theorem ' + name + sep)
        if k >= 0:
            return module[k:module.index(':=', k) + 2]
    return None


def check_module(module, label):
    codes = []
    if not module.startswith(FROZEN['header']):
        codes.append('module:header')
    for name, text in FROZEN['defs'].items():
        if module.count(text) != 1:
            codes.append('module:def:' + name)
    if len(re.findall(r'^(?:noncomputable )?def ', module, re.M)) != len(FROZEN['defs']) \
            or re.search(r'^(?:abbrev|instance|structure|class|inductive) ', module, re.M):
        codes.append('module:definition-budget')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    names = re.findall(r'^theorem (\S+)', module, re.M)
    for n in names:
        if n not in FROZEN['statements'] and not n.startswith('a45_shared_'):
            codes.append('module:unknown-name:' + n)
        if module.count('#print axioms ' + n + '\n') != 1:
            codes.append('module:print-axioms:' + n)
    for n, text in FROZEN['statements'].items():
        if n == 'a45_bridge_kernel' and label != 'A45-BRIDGE-PROVED':
            if n in names:
                codes.append('module:verdict-under-undecided')
            continue
        if statement(module, n) != text:
            codes.append('module:statement:' + n)
    return codes


def check_note(note, label, module_blob):
    codes = []
    lines = note.split('\n')
    outs = [l for l in lines if l.startswith('**Outcome:**')]
    if outs != ['**Outcome:** `%s`' % label]:
        codes.append('note:outcome-line')
    for lab in LABELS:
        n = note.count(SENTENCES[lab])
        if n != (1 if lab == label else 0):
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
    for path in (WORKFLOW, IMPORTS, CENSUS) + tuple(MANUSCRIPTS):
        try:
            exp = expected_text(d_files, path, label)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    road_exp = apply_edits(d_files[ROADMAP].decode(), EDITS[ROADMAP]).encode() if label == 'A45-BRIDGE-PROVED' \
        else d_files[ROADMAP]
    if e_files.get(ROADMAP) != road_exp:
        codes.append('surface:' + ROADMAP)
    for md, stem in BUILT.items():
        tex, pdf = e_files.get(stem + '.tex'), e_files.get(stem + '.pdf')
        stamp = re.search(rb'^% source-sha256: ([0-9a-f]{64})\s*$', tex or b'', re.M)
        if not stamp or stamp.group(1).decode() != hashlib.sha256(e_files[md]).hexdigest():
            codes.append('built:stamp:' + stem)
        if label == 'A45-BRIDGE-PROVED' and (pdf is None or pdf == d_files[stem + '.pdf']):
            codes.append('built:pdf:' + stem)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
            MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if label == 'A45-BRIDGE-PROVED':
        want[ROADMAP] = 'M'
        for md in MANUSCRIPTS:
            want[md] = 'M'
        for stem in BUILT.values():
            want[stem + '.tex'] = 'M'
            want[stem + '.pdf'] = 'M'
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
    paths = [RDIR + 'result.md', RDIR + 'preregistration.md', MODULE, PROBE, WORKFLOW, IMPORTS, CENSUS, ROADMAP]
    paths += MANUSCRIPTS
    for stem in BUILT.values():
        paths += [stem + '.tex', stem + '.pdf']
    return paths


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
    parts = [FROZEN['header'], 'namespace OIBridge\n\nnamespace TrackBQfbBridge\n\n' + ALLOWED_OPTION + '\n\n']
    for text in FROZEN['defs'].values():
        parts.append(text + '\n\n')
    for n, text in FROZEN['statements'].items():
        if n == 'a45_bridge_kernel' and label != 'A45-BRIDGE-PROVED':
            continue
        parts.append(text + ' by\n  exact placeholder\n#print axioms %s\n\n' % n)
    parts.append('end TrackBQfbBridge\n\nend OIBridge\n')
    return ''.join(parts).encode()


def synthetic_row(d_files, label):
    e = dict(d_files)
    module = synthetic_module(label)
    e[MODULE] = module
    e[PROBE] = SYNTHETIC_PROBE
    for path in (WORKFLOW, IMPORTS, CENSUS) + tuple(MANUSCRIPTS):
        e[path] = expected_text(d_files, path, label)
    if label == 'A45-BRIDGE-PROVED':
        e[ROADMAP] = apply_edits(d_files[ROADMAP].decode(), EDITS[ROADMAP]).encode()
    for md, stem in BUILT.items():
        e[stem + '.tex'] = b'% source-sha256: ' + hashlib.sha256(e[md]).hexdigest().encode() + b'\n'
        if label == 'A45-BRIDGE-PROVED':
            e[stem + '.pdf'] = b'%PDF synthetic ' + stem.encode()
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % label, '', SENTENCES[label], '', CLAUSE_MENTION, '', CLAUSE, '',
            '`' + PROBE_OK_PREFIX + ' (synthetic)`', '',
            'reference `%s`, module at E `%s`, departure from the reference implementation' % (REFERENCE_BLOB, blob(module))]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
               MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if label == 'A45-BRIDGE-PROVED':
        changed[ROADMAP] = 'M'
        for md in MANUSCRIPTS:
            changed[md] = 'M'
        for stem in BUILT.values():
            changed[stem + '.tex'] = 'M'
            changed[stem + '.pdf'] = 'M'
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
    for n, text in FROZEN['statements'].items():
        if text not in prereg:
            bad.append('prereg:statement:' + n)
    for n, text in FROZEN['defs'].items():
        if text not in prereg:
            bad.append('prereg:def:' + n)
    for path, eds in EDITS.items():
        for _, ins in eds:
            if ins.strip() not in prereg:
                bad.append('prereg:insertion:' + path)
    for b in (PROBE_BLOB, REFERENCE_BLOB):
        if b not in prereg:
            bad.append('prereg:blob:' + b)
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
    P, U = 'A45-BRIDGE-PROVED', 'A45-UNDECIDED'
    def edit_file(path, old, new):
        def f(e, ch):
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    first_ins = lambda p: EDITS[p][0][1]
    mut('verdict removed under PROVED', 'module:statement:a45_bridge_kernel', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'theorem a45_bridge_kernel', b'theorem a45_other')))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['statements']['a45_bridge_kernel'].encode()
                                    + b' by\n  x\n#print axioms a45_bridge_kernel\n'))
    mut('a frozen statement weakened', 'module:statement:bridge_traj', P,
        edit_file(MODULE, 'permClass V M) (hN : permClass V N) (K : ℕ)', 'permClass V M) (hN : permClass V N) (K : ℕ) (hK : 0 < K)'))
    mut('a definition changed', 'module:def:realData', P, edit_file(MODULE, 'read := id', 'read := fun b => b'))
    mut('an extra definition', 'module:definition-budget', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'end TrackBQfbBridge', b'def extra : Nat := 0\n\nend TrackBQfbBridge')))
    mut('a missing #print axioms', 'module:print-axioms:bridge', P,
        edit_file(MODULE, '#print axioms bridge\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'end TrackBQfbBridge', b'theorem helper : True := trivial\n#print axioms helper\n\nend TrackBQfbBridge')))
    mut('an extra set_option', 'module:set_option', P,
        edit_file(MODULE, ALLOWED_OPTION, ALLOWED_OPTION + '\nset_option maxHeartbeats 0'))
    mut('the header changed', 'module:header', P, edit_file(MODULE, 'import OIBridge.DitaHull', 'import OIBridge.DitaTorus'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.TrackBQfbBridge\n'))
    mut('the census family left kernel-only under PROVED', 'surface:' + CENSUS, P,
        lambda e, ch: e.__setitem__(CENSUS, expected_census(d_files[CENSUS], U)))
    mut('a word changed in Main', 'surface:papers/Main.md', P,
        edit_file('papers/Main.md', 'contractively scaled partial permutations', 'scaled partial permutations'))
    mut('the FULL mirror missing ch19 insertion', 'surface:book/The-Incompleteness-of-Observation-FULL.md', P,
        edit_file('book/The-Incompleteness-of-Observation-FULL.md', first_ins('book/ch19-open-problems.md'), ''))
    mut('manuscripts edited under UNDECIDED', 'surface:papers/Main.md', U,
        lambda e, ch: e.__setitem__('papers/Main.md', rows[P][0]['papers/Main.md']))
    mut('a stale .tex stamp', 'built:stamp:papers/Main', P,
        lambda e, ch: e.__setitem__('papers/Main.tex', b'% source-sha256: ' + b'0' * 64 + b'\n'))
    mut('the pdf not rebuilt', 'built:pdf:book/The-Incompleteness-of-Observation-FULL', P,
        lambda e, ch: e.__setitem__('book/The-Incompleteness-of-Observation-FULL.pdf',
                                    d_files['book/The-Incompleteness-of-Observation-FULL.pdf']))
    mut('the roadmap sentence altered', 'surface:' + ROADMAP, P,
        edit_file(ROADMAP, 'no relation is adopted', 'a relation is adopted'))
    mut('the roadmap touched under UNDECIDED', 'surface:' + ROADMAP, U,
        lambda e, ch: e.__setitem__(ROADMAP, rows[P][0][ROADMAP]))
    mut('an extra path changed', 'paths', P, lambda e, ch: ch.__setitem__('papers/GR.md', 'M'))
    mut('a governed path missing', 'paths', P, lambda e, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + b'\n**Outcome:** `A45-UNDECIDED`\n'))
    mut("the other label's sentence", 'note:sentence:A45-UNDECIDED', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + b'\n' + SENTENCES[U].encode()))
    mut('the clause missing', 'note:clause', P, edit_file(RDIR + 'result.md', CLAUSE, ''))
    mut('the probe line missing', 'note:probe-line', P, edit_file(RDIR + 'result.md', PROBE_OK_PREFIX, 'probe'))
    mut('the blobs missing', 'note:blobs', P, edit_file(RDIR + 'result.md', REFERENCE_BLOB, 'x'))
    mut('the departure unreported', 'note:departure', P,
        edit_file(RDIR + 'result.md', 'departure from the reference implementation', ''))
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
