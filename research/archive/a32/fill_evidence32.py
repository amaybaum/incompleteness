import hashlib, json, subprocess, sys
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a32/'
cfg = json.load(open(S + 'evidence-cfg.json', encoding='utf-8'))
t = open(S + 'evidence32.md', encoding='utf-8').read()
def blob(p): return subprocess.run(['git', 'hash-object', p], capture_output=True, text=True).stdout.strip()
scripts = ['gen_props32.py', 'gen_elab32.py', 'gen_sep32.py', 'build_retire32.py', 'p0_32.py', 'ctlcheck.py',
           'sepenc.py', 'sim_a32.py']
rows = '\n'.join('| `%s` | `%s` |' % (s, hashlib.sha256(open(S + s, 'rb').read()).hexdigest()) for s in scripts)
rep = {'@@ELAB_BLOB@@': cfg['elab_blob'], '@@RUN_NR@@': cfg['run_nr'], '@@OUT_NR@@': cfg['out_nr'],
       '@@RUN_R@@': cfg['run_r'], '@@OUT_R@@': cfg['out_r'], '@@GUARD_BLOB_RETIRED@@': blob(S + 'guard-retired32.py'),
       '@@ROAD_NR@@': blob(S + 'road-notrigid.v1.md'), '@@ROAD_R@@': blob(S + 'road-rigid.v1.md'),
       '@@ROAD_NR_FROZEN@@': blob(S + 'road-notrigid.md'), '@@ROAD_R_FROZEN@@': blob(S + 'road-rigid.md'),
       '@@SIMS@@': open(S + 'sims.md', encoding='utf-8').read().rstrip('\n'), '@@SCRIPTS@@': rows}
for k, v in rep.items():
    assert t.count(k) >= 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'evidence32.filled.md', 'w', encoding='utf-8').write(t)
