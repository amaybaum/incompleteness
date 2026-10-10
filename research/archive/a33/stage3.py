"""Build stage-3 surfaces from D's files: the census with the A33 family appended, and check ROADMAP.
usage: python3 stage3.py <worktree>  (writes census into the worktree; ROADMAP copied from road-classified.md)"""
import json, sys, subprocess, importlib.util, shutil
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a33/'
spec = importlib.util.spec_from_file_location('c33', S + 'controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
wt = sys.argv[1]
D = C.D
cen_d = subprocess.run(['git', 'show', D + ':' + C.CENSUS], capture_output=True, text=True, cwd=wt, check=True).stdout
d = json.loads(cen_d)
NOTE = open(S + 'census_note.txt', encoding='utf-8').read().strip()
import re
mod = open(wt + '/' + C.MODULE, encoding='utf-8').read()
n = len(C.theorems(C.strip_comments(mod)))
NUM = {349: 'Three hundred and forty-nine', 350: 'Three hundred and fifty', 351: 'Three hundred and fifty-one', 352: 'Three hundred and fifty-two', 353: 'Three hundred and fifty-three', 354: 'Three hundred and fifty-four', 355: 'Three hundred and fifty-five'}
NOTE = NOTE.replace('@@NTHM@@', NUM[n])
assert '@@' not in NOTE
fam = {"name": "the isometry group of the normalized single-carrier space — the circle preservation, the normal form over the incidence graph K₃,₃ with nine conjugation bits, the group law, order 36864, and act 25's family as a subgroup of index 16 (act 33, Track B)",
       "modules": ["OrbitIsometryGroup"], "status": "kernel-only", "manuscript": [], "note": NOTE}
e = dict(d); e['families'] = d['families'] + [fam]
cen_e = json.dumps(e, indent=2, ensure_ascii=False) + '\n'
f = C.census_ok(cen_d, cen_e, 'A33-CLASSIFIED')
print('census findings', f)
assert not f
open(wt + '/' + C.CENSUS, 'w', encoding='utf-8').write(cen_e)
road_d = subprocess.run(['git', 'show', D + ':' + C.ROADMAP], capture_output=True, text=True, cwd=wt, check=True).stdout
road_e = C.expected_roadmap(road_d, 'A33-CLASSIFIED')
assert road_e == open(S + 'road-classified.md', encoding='utf-8').read(), 'road-classified.md differs from the expected cell'
open(wt + '/' + C.ROADMAP, 'w', encoding='utf-8').write(road_e)
print('roadmap blob', C.blob_id(road_e), 'census blob', C.blob_id(cen_e))
