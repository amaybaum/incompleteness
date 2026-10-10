"""Assemble rec/controls.py from the frozen pieces: constants, the renderer, the ledger, the sentences, the workflow edit, the checks."""
import hashlib, json, os, re
S = os.path.dirname(os.path.abspath(__file__)) + '/'
def blob(b): return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
r = open(S + 'ledger/render41.py', encoding='utf-8').read()
def cut(a, b): i = r.index(a); j = r.index(b, i); return r[i:j]
render_code = (cut('SLOT = re.compile', '# the values measured at D41') + cut('def number(n):', '# ---------------------------------------------------------------- measurements.json')
               + "P_CASES = ('P = Pu(u60)', 'Pu(u5)')\n\n\n" + cut('def _unit(flat):', 'def measurements_from_logs'))
ledger = json.load(open(S + 'ledger/ledger41.json', encoding='utf-8'))
sentences = json.load(open(S + 'sentences41.json', encoding='utf-8'))
wf = {}; exec(open(S + 'workflow41.py', encoding='utf-8').read().split("def apply(text):")[0], wf)
probes = {'verification/lean/dita_index_map_probe.py': S + 'probes/dita_index_map_probe.py',
          'verification/lean/dita_index_map_independent.py': S + 'probes/dita_index_map_independent.py',
          'verification/lean/dita_index_map_hulls.py': S + 'probes/dita_index_map_hulls.py'}
new_blobs = {k: blob(open(v, 'rb').read()) for k, v in probes.items()}
TR = 'verification/programmes/oi-qm/track-b/'
head = '''"""Track B act 41 -- the round's own contracts (frozen with the control plane).

    python3 controls.py --self-test [measurements.json]   every shared text carried by the preregistration; the ledger and
                                                           the workflow edit apply to D; each check fails on a named mutation
    python3 controls.py agree <measurements.json>          the frozen decision function: the label and any disagreements
    python3 controls.py render <measurements.json> <dir>   every corrected surface rendered from the measurements
    python3 controls.py check <E>                          the round's contracts at the execution head E

It carries the edit ledger, the sentence templates and the workflow edit as data, so that its blob freezes them, and it
reads nothing but git objects and the files of the round's record.
"""
import ast, hashlib, json, os, re, subprocess, sys

D_COMMIT = '78ea3c39004e97aad027ee6153051c6d372bdd55'
RECORD = '%sact-41-index-map-semantics/'
RECORD_FILES = ['preregistration.md', 'controls.py', 'result.md']
NEW_FILE_BLOBS = %s
NEW_FILES = sorted(NEW_FILE_BLOBS)
WORKFLOW = '.github/workflows/verify.yml'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
OLD_PROBES = ['verification/lean/dita_hierarchy_probe.py', 'verification/lean/dita_arc_exclusivity_probe.py',
              'verification/lean/dita_local_escape_probe.py', 'verification/lean/dita_torus_probe.py',
              'verification/lean/dita_torus_locus_probe.py']
LEAN_PATHS = ['verification/lean-mathlib/OIBridge/DitaHierarchy.lean', 'verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean',
              'verification/lean-mathlib/OIBridge/DitaLocalEscape.lean', 'verification/lean-mathlib/OIBridge/DitaTorusLocus.lean']
SURFACE_PATHS = OLD_PROBES + LEAN_PATHS + [CENSUS, ROADMAP]
BUGFIX_PATH = 'verification/lean/dita_local_escape_probe.py'
BUGFIX_LINE = 541
HISTORICAL_PREFIXES = tuple('%s' + d + '/' for d in ('act-36-dita-hierarchy', 'act-37-arc-exclusivity', 'act-38-local-escape',
                                                   'act-39-realizable-torus', 'act-40-dita-locus'))
HISTORICAL_FILES = ['verification/receipts/A%%d.json' %% n for n in range(36, 41)]
N_CASES = 42
SHARD_NAMES = ['dita_index_map_probe', 'dita_index_map_independent', 'dita_index_map_hulls']

# ---------------------------------------------------------------- the renderer
''' % (TR, json.dumps(new_blobs, indent=1, sort_keys=True), TR)
data = ('\n# ---------------------------------------------------------------- the edit ledger, the sentence templates, the workflow edit\n'
        'LEDGER = json.loads(%r)\n' % json.dumps(ledger, ensure_ascii=False)
        + 'SENTENCES = json.loads(%r)\n' % json.dumps(sentences, ensure_ascii=False)
        + 'WORKFLOW_EDITS = %r\n' % ([list(x) for x in wf['EDITS']],))
body = open(S + '_controls_body.py', encoding='utf-8').read()
out = head + render_code + data + body
os.makedirs(S + 'rec', exist_ok=True)
open(S + 'rec/controls.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out)
print('controls.py', blob(out.encode('utf-8')), len(out.splitlines()), 'lines; probe blobs', new_blobs)
