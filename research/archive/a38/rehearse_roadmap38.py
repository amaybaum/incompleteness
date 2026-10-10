"""Rehearse the two decided P0 cells at D: write roadmap-<label>.md and run the guard against each in the D worktree."""
import importlib.util, os, subprocess, hashlib, shutil
S = os.path.dirname(os.path.abspath(__file__)); WT = os.path.join(S, '..', 'wt-d38')
spec = importlib.util.spec_from_file_location('c38', os.path.join(S, 'rec', 'controls.py')); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
road_path = os.path.join(WT, 'verification/ROADMAP.md'); road = open(road_path, encoding='utf-8').read()
def blob_of(t):
    b = t.encode('utf-8'); return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
assert blob_of(road) == C.ROADMAP_BLOB_D
for lab in (C.PROVED, C.FAILS):
    new = C.expected_roadmap(road, lab); assert new and new != road
    open(os.path.join(S, 'roadmap-%s.md' % lab), 'w', encoding='utf-8').write(new)
    open(road_path, 'w', encoding='utf-8').write(new)
    r = subprocess.run(['python3', 'edge_rigidity_probe.py'], cwd=os.path.join(WT, 'verification/lean'), capture_output=True, text=True)
    open(os.path.join(S, 'guard-%s.log' % lab), 'w').write(r.stdout + r.stderr)
    tail = [l for l in r.stdout.splitlines() if 'PASS' in l or 'FAIL' in l][-1:]
    print(lab, 'roadmap blob', blob_of(new), 'guard rc', r.returncode, 'PASS lines', r.stdout.count('PASS'), 'FAIL lines', r.stdout.count('FAIL'), tail)
open(road_path, 'w', encoding='utf-8').write(road)
assert blob_of(open(road_path, encoding='utf-8').read()) == C.ROADMAP_BLOB_D
print('roadmap restored')
