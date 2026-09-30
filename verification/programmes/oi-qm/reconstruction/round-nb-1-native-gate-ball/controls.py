#!/usr/bin/env python3
"""controls.py -- round NB-1's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the module's frozen header and statements, the census family, the workflow
edit, the import line, the probe blob, the outcome sentences and the clause.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; two synthetic
                                            rows (CORE-PROVED, UNDECIDED) that must hold; mutation controls that must
                                            fail with their named codes
"""
import hashlib, json, os, re, subprocess, sys

D = 'fdebc6e39498367e15a8352fe0f01f8f75ab3671'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/'
MODULE = 'verification/lean-mathlib/OIBridge/NativeGateBall.lean'
PROBE = 'verification/lean/native_gate_ball_probe.py'
PROBE_BLOB = '203446ece72e4420d32007e0d79f78f401279337'
REFERENCE_BLOB = '6d3ad5e7a1eb28bb327e9f2212519a2b80e5187a'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
LABELS = ('NB-1-CORE-PROVED', 'NB-1-UNDECIDED')
VERDICT = 'nb1_kernel_core'
FROZEN = {'header': "/-\n  OIBridge/NativeGateBall.lean — round NB-1: the dimension-free core of the finite native-gate\n  ball no-go.\n\n  The theorem this module serves. For two locally tomographic d-ball systems with their full\n  self-dual effect cones and one common NOT involution `N`, an invertible linear map `G` with the\n  classical CNOT action on the corners, the two native relations `(I⊗N) G (I⊗N) = G` and\n  `(N⊗I) G (N⊗I) = (I⊗N) G`, and `G`, `G⁻¹` both sending product states into the maximal tensor\n  cone, force `d ∈ {1, 3}`. That theorem is not a kernel theorem: its proof is layered, and this\n  module certifies one layer of it.\n\n  Proved here, the steps whose reasoning does not depend on `d`:\n    §A  the averaging bound (S3) and its consequence for `p ≥ 2`;\n    §B  the Lorentz test: a vector every unit effect keeps nonnegative lies in the cone;\n    §C  the E₊ block vanishes for `p ≥ 2` (S4, entrywise), hence `p ≤ 1` given a nonzero block;\n    §D  parity (S5): an injective map anticommuting with a linear map equates its ±1 eigenspaces;\n    §E  a contraction with a contracting left inverse is an isometry (the last step of S1);\n    §F  the count: `p ≤ 1`, `p = q`, `p + q + 1 = d` give `d = 1 ∨ d = 3`;\n    `nb1_kernel_core`, the conjunction of `p_le_one`, `parity` and `dim_of_bounds`.\n\n  Not proved here. The controlled form (S1), the block structure (S2) and the value identity that\n  turns positivity of `G` into the hypothesis of `blocks_vanish` (S4) are proved by hand for every\n  `d`; the round's probe checks the S1 and S2 solution spaces in exact arithmetic for `d = 2,…,7`\n  and the value identity for `d = 5, 7`. Nothing here concerns whether OI supplies the common `N`\n  on both factors (identical-copy covariance).\n\n  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build\n-/\nimport Mathlib.Analysis.SpecialFunctions.Pow.Real\nimport Mathlib.LinearAlgebra.FiniteDimensional.Basic\nimport Mathlib.Tactic.Linarith\nimport Mathlib.Tactic.Ring\n\n", 'statements': {'col_sq': 'theorem col_sq (p : ℕ) (K : Matrix (Fin p) (Fin p) ℝ) (i : Fin p) :\n    (∑ j, ((if j = i then (1:ℝ) else 0) + K j i) ^ 2) = 1 + 2 * K i i + ∑ j, K j i ^ 2 :=', 'averaging_bound': 'theorem averaging_bound (p : ℕ) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)\n    (hK : ∀ i j, K i j = - K j i)\n    (h : ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →\n      (∑ j, (g j + s * ((if j = i then (1:ℝ) else 0) + K j i)) ^ 2) ≤ (1 + s * g i) ^ 2) :\n    ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 :=', 'vanish_of_bound': 'theorem vanish_of_bound (p : ℕ) (hp : 2 ≤ p) (g : Fin p → ℝ) (K : Matrix (Fin p) (Fin p) ℝ)\n    (h : ((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0) :\n    (∀ j, g j = 0) ∧ (∀ i j, K j i = 0) :=', 'lorentz_of_effects': 'theorem lorentz_of_effects (p : ℕ) (hp : 1 ≤ p) (x0 : ℝ) (v : Fin p → ℝ)\n    (h : ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 → 0 ≤ x0 + ∑ j, b j * v j) :\n    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2 :=', 'blocks_vanish': 'theorem blocks_vanish (p m : ℕ) (hp : 2 ≤ p)\n    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)\n    (hB : ∀ r s, B r s = - B s r)\n    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →\n      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →\n        0 ≤ (1 + s * A i k l)\n          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) :\n    (∀ r, A r = 0) ∧ (∀ r s, B r s = 0) :=', 'p_le_one': 'theorem p_le_one (p m : ℕ)\n    (A : Fin p → Matrix (Fin m) (Fin m) ℝ) (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ)\n    (hB : ∀ r s, B r s = - B s r)\n    (hpos : ∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →\n      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →\n        0 ≤ (1 + s * A i k l)\n          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l)))\n    (hne : ∃ r k l, A r k l ≠ 0) : p ≤ 1 :=', 'parity': 'theorem parity {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]\n    (P L : V →ₗ[ℝ] V) (hL : Function.Injective L)\n    (hanti : ∀ v, L (P v) = - P (L v)) :\n    Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))\n      = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id)) :=', 'isometry_of_contractions': "theorem isometry_of_contractions {E : Type*} [SeminormedAddCommGroup E] (M M' : E → E)\n    (hM : ∀ v, ‖M v‖ ≤ ‖v‖) (hM' : ∀ v, ‖M' v‖ ≤ ‖v‖) (hinv : ∀ v, M' (M v) = v) :\n    ∀ v, ‖M v‖ = ‖v‖ :=", 'dim_of_bounds': 'theorem dim_of_bounds (p q d : ℕ) (hp : p ≤ 1) (hpq : p = q) (hd : p + q + 1 = d) :\n    d = 1 ∨ d = 3 :=', 'nb1_kernel_core': 'theorem nb1_kernel_core :\n    (∀ (p m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ)\n      (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ),\n      (∀ r s, B r s = - B s r) →\n      (∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →\n        ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →\n          0 ≤ (1 + s * A i k l)\n            + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) →\n      (∃ r k l, A r k l ≠ 0) → p ≤ 1) ∧\n    (∀ (V : Type) [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V] (P L : V →ₗ[ℝ] V),\n      Function.Injective L → (∀ v, L (P v) = - P (L v)) →\n      Module.finrank ℝ (LinearMap.ker (P - LinearMap.id))\n        = Module.finrank ℝ (LinearMap.ker (P + LinearMap.id))) ∧\n    (∀ p q d : ℕ, p ≤ 1 → p = q → p + q + 1 = d → d = 1 ∨ d = 3) :='}}
WORKFLOW_JOB = '  probes_nb1:\n    name: Numerical probes / NB-1 native-gate ball\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: NB-1 native-gate ball probe\n        working-directory: verification/lean\n        run: |\n          echo "=== native_gate_ball_probe.py ==="\n          python3 native_gate_ball_probe.py\n'
WORKFLOW_EDITS = [('          python3 fixed_basis_ancilla_probe.py\n\n', '          python3 fixed_basis_ancilla_probe.py\n\n  probes_nb1:\n    name: Numerical probes / NB-1 native-gate ball\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: \'3.11\'\n\n      - name: NB-1 native-gate ball probe\n        working-directory: verification/lean\n        run: |\n          echo "=== native_gate_ball_probe.py ==="\n          python3 native_gate_ball_probe.py\n\n'), ('probes_a45, probes_a42_witness', 'probes_a45, probes_nb1, probes_a42_witness'), ('          A45_RESULT: ${{ needs.probes_a45.result }}\n', '          A45_RESULT: ${{ needs.probes_a45.result }}\n          NB1_RESULT: ${{ needs.probes_nb1.result }}\n'), ('          echo "a45=${A45_RESULT}"\n', '          echo "a45=${A45_RESULT}"\n          echo "nb1=${NB1_RESULT}"\n'), ('          test "${A45_RESULT}" = success\n', '          test "${A45_RESULT}" = success\n          test "${NB1_RESULT}" = success\n')]
IMPORT_EDIT = ('import OIBridge.HydroClosureBridge\n', 'import OIBridge.HydroClosureBridge\nimport OIBridge.NativeGateBall\n')
FAMILY = {'name': 'the dimension-free core of the finite native-gate ball no-go: the averaging bound, the Lorentz test, the vanishing of the E+ block for p >= 2, parity, and the count d in {1, 3} (round NB-1, reconstruction)', 'modules': ['NativeGateBall'], 'status': 'kernel-only', 'manuscript': [], 'note': 'Round NB-1, a native round under AGENTS.md §A.39, executed under the frozen control plane programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/preregistration.md. The kernel layer of the finite native-gate ball theorem: the steps whose reasoning does not depend on d, averaging_bound and vanish_of_bound (S3), lorentz_of_effects, blocks_vanish and p_le_one (S4), parity (S5), isometry_of_contractions (the last step of S1) and dim_of_bounds. The controlled form, the block structure and the S4 value identity are proved by hand for every d, and checked in exact arithmetic by native_gate_ball_probe.py (S1 and S2 for d = 2..7, the value identity for d = 5, 7); they are not kernel statements, and the theorem for general d is not a kernel theorem. Carried by no manuscript. Its reading for OI is conditional on identical-copy covariance of the local NOT, which the corpus does not derive.'}
SENTENCES = {'NB-1-CORE-PROVED': "In the kernel, at evidence level 2: the averaging bound and its consequence for `p ≥ 2` (`averaging_bound`, `vanish_of_bound`), the Lorentz test (`lorentz_of_effects`), the vanishing of every `E₊` block entry for `p ≥ 2` and hence `p ≤ 1` whenever an entry is nonzero (`blocks_vanish`, `p_le_one`), the equality of the `±1` eigenspace dimensions of a linear map under an injective map anticommuting with it (`parity`), the isometry step (`isometry_of_contractions`) and the count (`dim_of_bounds`), joined in the verdict `nb1_kernel_core`. In exact rational arithmetic replayed in CI, and not in the kernel, the round's probe computes the S1 and S2 solution spaces for `d = 2, …, 7` and every split `p + q = d − 1`, the S4 value identity for `d = 5` and `d = 7`, and the three minimality countermodels: without the control-NOT relation, the `d = 5` J/K map meets the frame, `G² = I` and the target relation, and its value on product states and effects obeys the complex CNOT's reduction formula exactly; with different NOTs `N_A ≠ N_B`, the same map meets both native relations; keeping the frame, `G² = I` and both relations, the `d = 7` candidate sends the product state `(u + x)⊗(u + v₃)` outside the maximal tensor cone, with minimum `1 − √3` over target effects. The theorem these layers serve — two locally tomographic `d`-balls with their full self-dual effect cones, one common NOT involution `N`, and an invertible `G` acting as CNOT on the corners, satisfying `(I⊗N)G(I⊗N) = G` and `(N⊗I)G(N⊗I) = (I⊗N)G`, with `G` and `G⁻¹` sending product states into the maximal tensor cone, force `d ∈ {1, 3}` — holds by the round's written proof, in which S1, S2 and the S4 value identity are proved by hand for every `d`; it is not a kernel theorem, and the two surviving countermodels are positive by the written reduction to the complex CNOT. Read for OI, the theorem is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, which the corpus does not derive; nothing here claims that OI selects `d = 3`.", 'NB-1-UNDECIDED': 'The kernel verdict `nb1_kernel_core` was not obtained. The step at which the proof stopped is named, with what would settle it; the exact layer stands as computed, and the theorem for general `d` is not stated as a result of this round.'}
CLAUSE = "Round NB-1 proves statements about finite native gates on two copies of a d-ball and adopts none of them as anything but mathematics. A `CORE-PROVED` verdict settles in the kernel the dimension-free steps of the ball theorem, certifies in exact arithmetic the S1 and S2 solution spaces for d = 2 to 7, the S4 value identity for d = 5 and 7 and the three minimality countermodels, and leaves the theorem for general d resting on the round's written proof; that theorem is not a kernel theorem. Its reading for OI is conditional on identical-copy covariance, `Σ(N⊗I)Σ⁻¹ = I⊗N`, a premise the corpus does not derive and this round does not supply, stated as a covariance and not as the availability of SWAP. The round does not claim that OI selects d = 3; it uses no SWAP, composite unitary control, continuous local group, `G² = I`, normalization of `G` or intermediate cone; and it edits no manuscript and no roadmap row."
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PROBE_OK_PREFIX = 'native_gate_ball_probe: OK -- 51 checks'
FORBIDDEN_NOTE = ('OI selects', 'OI implies d', 'OI forces d', 'OI ⇒ d', 'OI => d', 'kernel theorem for every d', 'kernel-proved for every d', 'kernel proof of the theorem for every d')
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
    if re.search(r'^(?:noncomputable )?(?:def|abbrev|instance|structure|class|inductive) ', module, re.M):
        codes.append('module:definition-budget')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    names = re.findall(r'^theorem (\S+)', module, re.M)
    for n in names:
        if n not in FROZEN['statements'] and not n.startswith('nb1_shared_'):
            codes.append('module:unknown-name:' + n)
        if module.count('#print axioms OIBridge.NativeGateBall.' + n + '\n') != 1:
            codes.append('module:print-axioms:' + n)
    for n, text in FROZEN['statements'].items():
        if n == VERDICT and label != LABELS[0]:
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
    parts = [FROZEN['header'], 'namespace OIBridge\nnamespace NativeGateBall\n\n']
    names = []
    for n, text in FROZEN['statements'].items():
        if n == VERDICT and label != LABELS[0]:
            continue
        parts.append(text + ' by\n  exact placeholder\n\n')
        names.append(n)
    parts.append('end NativeGateBall\nend OIBridge\n\n')
    for n in names:
        parts.append('#print axioms OIBridge.NativeGateBall.%s\n' % n)
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
    for n, text in FROZEN['statements'].items():
        if text not in prereg:
            bad.append('prereg:statement:' + n)
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
    mut('verdict removed under CORE-PROVED', 'module:statement:' + VERDICT, P,
        edit_file(MODULE, 'theorem ' + VERDICT, 'theorem nb1_other'))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['statements'][VERDICT].encode()
                                    + b' by\n  x\n#print axioms OIBridge.NativeGateBall.' + VERDICT.encode() + b'\n'))
    mut('parity weakened by an involution hypothesis', 'module:statement:parity', P,
        edit_file(MODULE, '(P L : V →ₗ[ℝ] V) (hL', '(P L : V →ₗ[ℝ] V) (hP : P ∘ₗ P = LinearMap.id) (hL'))
    mut('the averaging bound weakened', 'module:statement:averaging_bound', P,
        edit_file(MODULE, '((p : ℝ) - 1) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 :=',
                  '((p : ℝ) - 2) * (∑ j, g j ^ 2) + (∑ i, ∑ j, K j i ^ 2) ≤ 0 :='))
    mut('the count loosened', 'module:statement:dim_of_bounds', P,
        edit_file(MODULE, '(hd : p + q + 1 = d) :\n    d = 1 ∨ d = 3 :=', '(hd : p + q + 1 = d) :\n    d ≤ 3 :='))
    mut('the header claims a kernel theorem', 'module:header', P,
        edit_file(MODULE, 'That theorem is not a kernel theorem', 'That theorem is a kernel theorem'))
    mut('an import added to the header', 'module:header', P,
        edit_file(MODULE, 'import Mathlib.Tactic.Ring\n', 'import Mathlib.Tactic.Ring\nimport OIBridge.FactorExchange\n'))
    mut('a definition added', 'module:definition-budget', P,
        edit_file(MODULE, 'end NativeGateBall', 'def extra : Nat := 0\n\nend NativeGateBall'))
    mut('a missing #print axioms', 'module:print-axioms:parity', P,
        edit_file(MODULE, '#print axioms OIBridge.NativeGateBall.parity\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an axiom declared', 'module:forbidden:axiom', P,
        edit_file(MODULE, 'end NativeGateBall', 'axiom oneN : True\n\nend NativeGateBall'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        edit_file(MODULE, 'end NativeGateBall', 'theorem helper : True := trivial\n\nend NativeGateBall'))
    mut('a set_option', 'module:set_option', P,
        edit_file(MODULE, 'namespace NativeGateBall\n', 'namespace NativeGateBall\nset_option maxHeartbeats 0\n'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the probe shard left out of the aggregate', 'surface:' + WORKFLOW, P,
        edit_file(WORKFLOW, '          test "${NB1_RESULT}" = success\n', ''))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.NativeGateBall\n'))
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
    mut('the note claims OI selects d = 3', 'note:forbidden-claim', P, append_note('\nHence OI selects d = 3.\n'))
    mut('the note calls the theorem kernel-proved for every d', 'note:forbidden-claim', U,
        append_note('\nThe ball theorem is a kernel theorem for every d.\n'))
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
