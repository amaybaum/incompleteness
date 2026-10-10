"""Fill the preregistration draft's placeholders: runs table, controls blob, probe blob, mutation count, rehearsed roadmap blobs."""
import os, subprocess, sys, json
S = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(S, 'preregistration.draft.md'), encoding='utf-8').read()
runs = open(os.path.join(S, 'runs35.txt'), encoding='utf-8').read().strip()
cblob = subprocess.run(['git', 'hash-object', os.path.join(S, 'controls.py')], capture_output=True, text=True).stdout.strip()
pblob = subprocess.run(['git', 'hash-object', os.path.join(S, 'dita_defect_probe.py')], capture_output=True, text=True).stdout.strip()
nm = sys.argv[1]
rep = {'@@RUNS@@': runs, '@@CONTROLS_BLOB@@': cblob, '@@PROBE_BLOB@@': pblob, '@@NMUTS@@': nm,
       '@@ROAD_ST@@': '15a6cd4e243b61817a3a7c253324d412b1082cd0', '@@ROAD_NS@@': '61875bd48472bf03abf75ae1df3e1609c443e2db'}
for k, v in rep.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
assert '@@' not in t
os.makedirs(os.path.join(S, 'rec'), exist_ok=True)
open(os.path.join(S, 'rec', 'preregistration.md'), 'w', encoding='utf-8').write(t)
print('written; controls blob', cblob, 'probe blob', pblob)
