import json, re, sys, subprocess
sys.path.insert(0, '.')
import texts
WT = '../wt-kinf1/'
MODULE = 'verification/lean-mathlib/OIBridge/KInfFoundations.lean'
module = open(WT + MODULE, encoding='utf-8').read()
header = module[:module.index('namespace OIBridge')]
DECL_RE = re.compile(r'^(theorem|structure|def|noncomputable def|abbrev|instance|class|inductive) (\S+)', re.M)
found = DECL_RE.findall(module)
def declaration(kind, name):
    for sep in (' ', '\n'):
        k = module.find(kind + ' ' + name + sep)
        if k >= 0 and (k == 0 or module[k - 1] == '\n'):
            if kind == 'theorem':
                return module[k:module.index(':=', k) + 2]
            end = module.find('\n\n', k)
            return module[k:end if end >= 0 else len(module)]
    raise KeyError(name)
decls = {}
for kind, n in found:
    assert n not in decls, 'duplicate declaration name ' + n
    decls[n] = (kind, declaration(kind, n))
prints = re.findall(r'^#print axioms (OIBridge\.KInfFoundations\.(\S+))$', module, re.M)
PRINT = {}
for full, tail in prints:
    short = tail if tail in decls else tail.split('.')[-1]
    assert short in decls and decls[short][0] == 'theorem', full
    assert short not in PRINT, full
    PRINT[short] = full
theorems = [n for k, n in found if k == 'theorem']
missing = [n for n in theorems if n not in PRINT]
assert not missing, 'theorems without #print axioms: %s' % missing
D = '98f5f08b'
D = subprocess.run(['git', '-C', WT, 'rev-parse', D], capture_output=True, check=True, text=True).stdout.strip()
def show(path):
    return subprocess.run(['git', '-C', WT, 'show', D + ':' + path], capture_output=True, check=True).stdout.decode()
wf_d = show('.github/workflows/verify.yml')
WORKFLOW_JOB = '''  probes_kinf1:
    name: Numerical probes / KINF-1 foundations
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: KINF-1 foundations probe
        working-directory: verification/lean
        run: |
          echo "=== kinf_foundations_probe.py ==="
          python3 kinf_foundations_probe.py
'''
edits = [
 ('          python3 native_gate_ball_probe.py\n\n', '          python3 native_gate_ball_probe.py\n\n' + WORKFLOW_JOB + '\n'),
 ('probes_nb1, probes_a42_witness', 'probes_nb1, probes_kinf1, probes_a42_witness'),
 ('          NB1_RESULT: ${{ needs.probes_nb1.result }}\n', '          NB1_RESULT: ${{ needs.probes_nb1.result }}\n          KINF1_RESULT: ${{ needs.probes_kinf1.result }}\n'),
 ('          echo "nb1=${NB1_RESULT}"\n', '          echo "nb1=${NB1_RESULT}"\n          echo "kinf1=${KINF1_RESULT}"\n'),
 ('          test "${NB1_RESULT}" = success\n', '          test "${NB1_RESULT}" = success\n          test "${KINF1_RESULT}" = success\n'),
]
t = wf_d
for o, n in edits:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
assert t == open(WT + '.github/workflows/verify.yml').read(), 'workflow edit does not reproduce the design file'
imp_d = show('verification/lean-mathlib/OIBridge.lean')
IMPORT_EDIT = ('import OIBridge.NativeGateBall\n', 'import OIBridge.NativeGateBall\nimport OIBridge.KInfFoundations\n')
assert imp_d.count(IMPORT_EDIT[0]) == 1 and imp_d.replace(*IMPORT_EDIT) == open(WT + 'verification/lean-mathlib/OIBridge.lean').read()
census = json.load(open(WT + 'verification/lean-manuscript-census.json'))
FAMILY = census['families'][-1]
assert FAMILY['modules'] == ['KInfFoundations']
c = json.loads(show('verification/lean-manuscript-census.json')); c['families'].append(FAMILY)
assert json.dumps(c, indent=2, ensure_ascii=False) + '\n' == open(WT + 'verification/lean-manuscript-census.json').read()
def gblob(p):
    return subprocess.run(['git', 'hash-object', WT + p], capture_output=True, check=True, text=True).stdout.strip()
PROBE_BLOB = gblob('verification/lean/kinf_foundations_probe.py')
REFERENCE_BLOB = gblob(MODULE)
doc = '''#!/usr/bin/env python3
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

'''
consts = [
 ('D', D),
 ('RDIR', 'verification/programmes/oi-qm/reconstruction/round-kinf-1-foundations/'),
 ('MODULE', MODULE),
 ('PROBE', 'verification/lean/kinf_foundations_probe.py'),
 ('PROBE_BLOB', PROBE_BLOB),
 ('REFERENCE_BLOB', REFERENCE_BLOB),
 ('IMPORTS', 'verification/lean-mathlib/OIBridge.lean'),
 ('CENSUS', 'verification/lean-manuscript-census.json'),
 ('WORKFLOW', '.github/workflows/verify.yml'),
 ('LABELS', texts.LABELS),
 ('VERDICT', 'kinf1_kernel_core'),
 ('FROZEN', {'header': header, 'declarations': decls}),
 ('PRINT', PRINT),
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
json.dump({'header': header, 'declarations': decls, 'PRINT': PRINT, 'WORKFLOW_JOB': WORKFLOW_JOB, 'FAMILY': FAMILY,
           'PROBE_BLOB': PROBE_BLOB, 'REFERENCE_BLOB': REFERENCE_BLOB, 'D': D},
          open('frozen.json', 'w'), ensure_ascii=False, indent=1)
kinds = {}
for k, _ in decls.values():
    kinds[k] = kinds.get(k, 0) + 1
print(kinds, 'probe', PROBE_BLOB, 'reference', REFERENCE_BLOB)
