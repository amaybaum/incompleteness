"""Fill preregistration.draft.md -> rec/preregistration.md. usage: python3 fill_prereg39.py (reads runs39_prereg.txt)"""
import hashlib, importlib.util, os, re, sys
S = os.path.dirname(os.path.abspath(__file__)) + '/'
def blob_of(path):
    b = open(path, 'rb').read()
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
PROBE_BLOB = blob_of(S + 'dita_torus_probe.py')
spec = importlib.util.spec_from_file_location('c39', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
assert C.PROBE_BLOB == PROBE_BLOB, (C.PROBE_BLOB, PROBE_BLOB)
CONTROLS_BLOB = blob_of(S + 'rec/controls.py')
log = open(S + 'probe39.log', encoding='utf-8').read()
npass = len(re.findall(r'(?m)^\s+PASS\s', log)); nfail = len(re.findall(r'(?m)^\s+FAIL\s', log))
assert nfail == 0 and 'dita_torus_probe: OK' in log, (npass, nfail)
road = {lab: blob_of(S + 'roadmap-%s.md' % lab) for lab in ('A39-REALIZABLE-PROVED', 'A39-REALIZABLE-FAILS')}
bad, rows, dmuts, muts = C.self_test()
assert [b for b in bad if not b.startswith('agreement')] == [], bad
assert dmuts == 12, dmuts
RUNS = open(S + 'runs39_prereg.txt', encoding='utf-8').read().strip().replace('@@NPASS@@', str(npass))
t = open(S + 'preregistration.draft.md', encoding='utf-8').read()
rep = {'@@RUNS@@': RUNS, '@@PROBE_BLOB@@': PROBE_BLOB, '@@CONTROLS_BLOB@@': CONTROLS_BLOB, '@@NMUTS@@': str(muts),
       '@@NPASS@@': str(npass), '@@ROAD_PV@@': road['A39-REALIZABLE-PROVED'], '@@ROAD_FL@@': road['A39-REALIZABLE-FAILS']}
for k, v in rep.items():
    assert t.count(k) >= 1, k; t = t.replace(k, v)
assert '@@' not in t, re.findall(r'@@[A-Z0-9_]+@@', t)
open(S + 'rec/preregistration.md', 'w', encoding='utf-8').write(t)
print('preregistration.md written; probe', PROBE_BLOB, 'controls', CONTROLS_BLOB, 'muts', muts, 'npass', npass)
