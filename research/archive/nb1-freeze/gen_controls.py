import json, re, sys, subprocess
sys.path.insert(0, '.')
import texts
WT = '../wt-nb1/'
module = open(WT + 'verification/lean-mathlib/OIBridge/NativeGateBall.lean', encoding='utf-8').read()
header = module[:module.index('namespace OIBridge')]
names = re.findall(r'^theorem (\S+)', module, re.M)
def statement(name):
    for sep in (' ', '\n'):
        k = module.find('theorem ' + name + sep)
        if k >= 0:
            return module[k:module.index(':=', k) + 2]
stmts = {n: statement(n) for n in names}
D = 'fdebc6e39498367e15a8352fe0f01f8f75ab3671'
def show(path):
    return subprocess.run(['git', '-C', WT, 'show', D + ':' + path], capture_output=True, check=True).stdout.decode()
wf_d = show('.github/workflows/verify.yml')
WORKFLOW_JOB = '''  probes_nb1:
    name: Numerical probes / NB-1 native-gate ball
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: NB-1 native-gate ball probe
        working-directory: verification/lean
        run: |
          echo "=== native_gate_ball_probe.py ==="
          python3 native_gate_ball_probe.py
'''
edits = [
 ('          python3 fixed_basis_ancilla_probe.py\n\n', '          python3 fixed_basis_ancilla_probe.py\n\n' + WORKFLOW_JOB + '\n'),
 ('probes_a45, probes_a42_witness', 'probes_a45, probes_nb1, probes_a42_witness'),
 ('          A45_RESULT: ${{ needs.probes_a45.result }}\n', '          A45_RESULT: ${{ needs.probes_a45.result }}\n          NB1_RESULT: ${{ needs.probes_nb1.result }}\n'),
 ('          echo "a45=${A45_RESULT}"\n', '          echo "a45=${A45_RESULT}"\n          echo "nb1=${NB1_RESULT}"\n'),
 ('          test "${A45_RESULT}" = success\n', '          test "${A45_RESULT}" = success\n          test "${NB1_RESULT}" = success\n'),
]
t = wf_d
for o, n in edits:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
assert t == open(WT + '.github/workflows/verify.yml').read(), 'workflow edit does not reproduce the design file'
imp_d = show('verification/lean-mathlib/OIBridge.lean')
IMPORT_EDIT = ('import OIBridge.HydroClosureBridge\n', 'import OIBridge.HydroClosureBridge\nimport OIBridge.NativeGateBall\n')
assert imp_d.count(IMPORT_EDIT[0]) == 1 and imp_d.replace(*IMPORT_EDIT) == open(WT + 'verification/lean-mathlib/OIBridge.lean').read()
census = json.load(open(WT + 'verification/lean-manuscript-census.json'))
FAMILY = census['families'][-1]
c = json.loads(show('verification/lean-manuscript-census.json')); c['families'].append(FAMILY)
assert json.dumps(c, indent=2, ensure_ascii=False) + '\n' == open(WT + 'verification/lean-manuscript-census.json').read()
def gblob(p):
    return subprocess.run(['git', 'hash-object', WT + p], capture_output=True, check=True, text=True).stdout.strip()
PROBE_BLOB = gblob('verification/lean/native_gate_ball_probe.py')
REFERENCE_BLOB = gblob('verification/lean-mathlib/OIBridge/NativeGateBall.lean')
doc = '''#!/usr/bin/env python3
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

'''
consts = [
 ('D', D),
 ('RDIR', 'verification/programmes/oi-qm/reconstruction/round-nb-1-native-gate-ball/'),
 ('MODULE', 'verification/lean-mathlib/OIBridge/NativeGateBall.lean'),
 ('PROBE', 'verification/lean/native_gate_ball_probe.py'),
 ('PROBE_BLOB', PROBE_BLOB),
 ('REFERENCE_BLOB', REFERENCE_BLOB),
 ('IMPORTS', 'verification/lean-mathlib/OIBridge.lean'),
 ('CENSUS', 'verification/lean-manuscript-census.json'),
 ('WORKFLOW', '.github/workflows/verify.yml'),
 ('LABELS', texts.LABELS),
 ('VERDICT', 'nb1_kernel_core'),
 ('FROZEN', {'header': header, 'statements': stmts}),
 ('WORKFLOW_JOB', WORKFLOW_JOB),
 ('WORKFLOW_EDITS', edits),
 ('IMPORT_EDIT', IMPORT_EDIT),
 ('FAMILY', FAMILY),
 ('SENTENCES', texts.SENTENCES),
 ('CLAUSE', texts.CLAUSE),
 ('CLAUSE_MENTION', texts.CLAUSE_MENTION),
 ('PROBE_OK_PREFIX', texts.PROBE_OK_PREFIX),
 ('FORBIDDEN_NOTE', texts.FORBIDDEN_NOTE),
 ('SYNTHETIC_PROBE', b'# synthetic probe for the self-test\n'),
 ('FORBIDDEN', ('sorry', 'admit', 'native_decide', 'axiom ', 'unsafe', 'opaque ', 'implemented_by', 'extern')),
 ('ALLOWED_OPTION', 'set_option linter.unusedSectionVars false'),
]
out = doc + ''.join('%s = %r\n' % (k, v) for k, v in consts) + '\n\n' + open('controls_body.py').read()
open('controls.py', 'w').write(out)
json.dump({'header': header, 'statements': stmts, 'WORKFLOW_JOB': WORKFLOW_JOB, 'FAMILY': FAMILY,
           'PROBE_BLOB': PROBE_BLOB, 'REFERENCE_BLOB': REFERENCE_BLOB}, open('frozen.json', 'w'), ensure_ascii=False, indent=1)
print(len(stmts), 'statements;', 'probe', PROBE_BLOB, 'reference', REFERENCE_BLOB)
