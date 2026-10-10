"""Apply A30's execution stages 1-6 on claude/a30-product-strict-lift from the designated F."""
import hashlib, importlib.util, json, os, subprocess, sys
S = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/user/incompleteness'
F = '3f337a95df6009102948690533d877ee1e4bf90d'
D = '48450428f528fe489d454458e21c9394aef6a02f'
spec = importlib.util.spec_from_file_location('c', os.path.join(S, 'controls.py'))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
TRAILER = ('\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
           'Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1\n')

def sh(*a, inp=None):
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True, input=inp)
    if r.returncode:
        print(r.stdout, r.stderr); raise SystemExit('failed: %s' % (a,))
    return r.stdout.strip()

def write(p, t):
    open(os.path.join(REPO, p), 'w', encoding='utf-8').write(t)

def read(p):
    return open(os.path.join(REPO, p), encoding='utf-8').read()

def commit(msg, paths):
    for p in paths:
        sh('git', 'add', p)
    staged = sh('git', 'diff', '--cached', '--name-only').splitlines()
    assert sorted(staged) == sorted(paths), (staged, paths)
    sh('git', 'commit', '-q', '-F', '-', inp=msg + TRAILER)
    h = sh('git', 'rev-parse', 'HEAD')
    assert len(sh('git', 'rev-list', '--parents', '-n', '1', h).split()) == 2
    return h

assert sh('git', 'rev-parse', 'HEAD') == F and sh('git', 'status', '--porcelain') == ''
# C1
assert sh('git', 'rev-parse', F + ':' + C.RDIR + 'preregistration.md') == 'c637999c884328cb085cb9dbbf27a39bb44e6643'
heads = []
# stage 1
write(C.RDIR + 'controls.py', open(os.path.join(S, 'controls.py'), encoding='utf-8').read())
write(C.MODULE, open(os.path.join(S, 'stage1.lean'), encoding='utf-8').read())
write(C.ROOT, read(C.ROOT).replace(C.WIRE_AFTER, C.WIRE_AFTER + C.WIRE, 1))
assert sh('git', 'hash-object', C.RDIR + 'controls.py') == '718e33b3cde5653e277734e337f4b931a237e907'
heads.append(commit('A30 stage 1: the module with the shared lemmas, its import, and the frozen controls',
                    [C.RDIR + 'controls.py', C.MODULE, C.ROOT]))
for n, msg in ((2, 'A30 stage 2: A30-S, a30_s_strictify'), (3, 'A30 stage 3: A30-T, a30_t_transfer'),
               (4, 'A30 stage 4: the corollaries, A30-N (a30_n_lifts) and A30-0 (a30_0_admits)')):
    write(C.MODULE, open(os.path.join(S, 'stage%d.lean' % n), encoding='utf-8').read())
    heads.append(commit(msg, [C.MODULE]))
vec, f = C.module_labels(read(C.MODULE))
assert f == [] and vec == C.ROWS[0], (vec, f)
# stage 5
g = C.retired_guard(read(C.GUARD)); assert C.blob_id(g) == C.GUARD_BLOB_RETIRED
write(C.GUARD, g)
r = C.expected_roadmap(read(C.ROADMAP), vec); assert C.blob_id(r) == 'e6779380f858bcb905fc9877ed2f11bf5de75c95'
write(C.ROADMAP, r)
cen = json.loads(read(C.CENSUS))
cen['families'].append(json.load(open(os.path.join(S, 'census-family.json'), encoding='utf-8')))
write(C.CENSUS, json.dumps(cen, indent=2, ensure_ascii=False) + '\n')
heads.append(commit('A30 stage 5: the census family, the P0 cell for A30-0-ADMITS, and the frozen guard ledger',
                    [C.CENSUS, C.ROADMAP, C.GUARD]))
# result note
write(C.RDIR + 'result.md', open(os.path.join(S, 'result.md'), encoding='utf-8').read())
heads.append(commit('A30 result note (E): A30-S-HOLD, A30-T-HOLD, A30-N-LIFTS, A30-0-ADMITS',
                    [C.RDIR + 'result.md']))
print('\n'.join(heads))
