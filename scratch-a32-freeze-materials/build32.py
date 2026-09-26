"""Fill A32's controls template (and, with 'prereg', the preregistration template)."""
import json, re, subprocess, sys, importlib.util
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/'
d = json.load(open(S + 'a32/props32.json', encoding='utf-8'))
spec = importlib.util.spec_from_file_location('p0', S + 'a32/p0_32.py'); P0 = importlib.util.module_from_spec(spec); spec.loader.exec_module(P0)
spec = importlib.util.spec_from_file_location('c31', S + 'a31/controls.py'); C31 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C31)
CLAUSE = C31.CLAUSE.replace('Act 31 classifies', 'Act 32 classifies', 1)
assert CLAUSE != C31.CLAUSE
SENT = json.load(open(S + 'a32/sentences32.json', encoding='utf-8'))
LEDGER = json.load(open(S + 'a32/ledger32.json', encoding='utf-8'))
def blob(path):
    return subprocess.run(['git', 'hash-object', path], capture_output=True, text=True).stdout.strip()
D = 'd61c6c5409db201e3c25abbf3ec0ecce1f530684'
lit = lambda x: json.dumps(x, ensure_ascii=False, indent=1)
t = open(S + 'a32/controls32.template.py', encoding='utf-8').read()
rep = {'@@D@@': D, '@@ROADMAP_BLOB_D@@': blob(S + 'a32/road-D.md'), '@@GUARD_BLOB_D@@': blob(S + 'a32/guard-D.py'),
       '@@GUARD_BLOB_RETIRED@@': blob(S + 'a32/guard-retired32.py'),
       '@@OPEN@@': lit(d['open']), '@@PROPS@@': lit(d['props']), '@@COMPONENTS@@': lit(d['components']),
       '@@SENTENCES@@': lit(SENT), '@@CLAUSE@@': lit(CLAUSE), '@@P0_STALE@@': lit(P0.CLAUSE),
       '@@P0_ADMITS@@': lit(P0.ADMITS), '@@P0_STANDING@@': lit(P0.STANDING), '@@P0_CASE@@': lit(P0.CASE),
       '@@P0_STANDING_32@@': lit(P0.STAND32), '@@LEDGER@@': lit(LEDGER)}
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'a32/controls.py', 'w', encoding='utf-8').write(t)
print('controls blob', blob(S + 'a32/controls.py'))
if sys.argv[1:] != ['prereg']:
    raise SystemExit
P = d['props']
spec = importlib.util.spec_from_file_location('c32', S + 'a32/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
bad, rows, dmuts, muts = C.self_test()
assert bad == ['agreement: preregistration.md not beside controls.py'], bad
SELFTEST = ('```text\ncontrols: the two verdict propositions are duals and every shared text has one source; '
            '%d duality mutations fail as required\ncontrols: %d rows hold as frozen, %d mutation controls fail '
            'as required\ncontrols: self-test OK\n```' % (dmuts, rows, muts))
open(S + 'a32/selftest-expected.txt', 'w').write('\n'.join(SELFTEST.split('\n')[1:-1]) + '\n')
LT = ['| entry | what it removes or rewrites | old text, SHA-256 | new text, SHA-256 |', '| --- | --- | --- | --- |']
for e in LEDGER:
    new = '`%s`' % e['new_sha256'] if e['new'] else 'empty, `%s`' % e['new_sha256']
    LT.append('| `%s` | %s | `%s` | %s |' % (e['entry'], e['reason'], e['old_sha256'], new))
gd = open(S + 'a32/guard-D.py', encoding='utf-8').read().count('\n')
gr = open(S + 'a32/guard-retired32.py', encoding='utf-8').read().count('\n')
pt = open(S + 'a32/prereg32.template.md', encoding='utf-8').read()
prep = {'@@CLAUSE_Q@@': '\n'.join('> ' + l for l in CLAUSE.split('\n')), '@@D@@': D,
        '@@ROADMAP_BLOB_D@@': rep['@@ROADMAP_BLOB_D@@'], '@@GUARD_BLOB_D@@': rep['@@GUARD_BLOB_D@@'],
        '@@GUARD_BLOB_RETIRED@@': rep['@@GUARD_BLOB_RETIRED@@'], '@@GUARD_LINES@@': str(gd - gr),
        '@@OPEN@@': d['open'], '@@EVIDENCE@@': open(S + 'a32/evidence32.filled.md', encoding='utf-8').read().rstrip('\n'),
        '@@S_R@@': SENT['A32-RIGID'], '@@S_NR@@': SENT['A32-NOT-RIGID'], '@@S_X@@': SENT['A32-UNDECIDED'],
        '@@P0_STALE@@': P0.CLAUSE.strip(), '@@P0_ADMITS@@': P0.ADMITS, '@@P0_STANDING@@': P0.STANDING,
        '@@P0_NR@@': P0.CASE['A32-NOT-RIGID'], '@@P0_R@@': P0.CASE['A32-RIGID'], '@@P0_STAND32@@': P0.STAND32,
        '@@ROAD_NR@@': blob(S + 'a32/road-notrigid.md'), '@@ROAD_R@@': blob(S + 'a32/road-rigid.md'),
        '@@LEDGER_TABLE@@': '\n'.join(LT), '@@CONTROLS_BLOB@@': blob(S + 'a32/controls.py'),
        '@@N_DMUTS@@': str(dmuts), '@@N_MUTS@@': str(muts), '@@SELFTEST@@': SELFTEST}
for k in ('P_R', 'P_N', 'S_EXIST', 'S_ISO', 'S_SEP', 'S_OVL', 'S_MOVE', 'S_GLOBAL', 'S_ID', 'S_QUARTER'):
    prep['@@%s@@' % k] = P[k]
order = ['@@EVIDENCE@@', '@@SELFTEST@@'] + [k for k in prep if k not in ('@@EVIDENCE@@', '@@SELFTEST@@')]
for k in order:
    assert pt.count(k) >= 1, k
    pt = pt.replace(k, prep[k])
assert '@@' not in pt, re.findall(r'@@\w+@@', pt)
open(S + 'a32/preregistration.md', 'w', encoding='utf-8').write(pt)
print('prereg blob', blob(S + 'a32/preregistration.md'), 'lines', pt.count('\n'))
