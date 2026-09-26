"""Fill A33's controls template -> controls.py; with 'prereg', also the preregistration template."""
import json, re, subprocess, sys, importlib.util
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/a33/'
d = json.load(open(S + 'props33.json', encoding='utf-8'))
spec = importlib.util.spec_from_file_location('t33', S + 'texts33.py'); T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
D = 'db82376dfc0e2ae561ec541fd0d3a915f082beda'
ROADMAP_BLOB_D, GUARD_BLOB_D = 'b1f6f9f728d07c0361302ed1994d43e848522372', 'd28e9b3cf2093984a1c453892204b9932a685b2e'
lit = lambda x: json.dumps(x, ensure_ascii=False, indent=1)
def blob(path):
    return subprocess.run(['git', 'hash-object', path], capture_output=True, text=True).stdout.strip()
t = open(S + 'controls33.template.py', encoding='utf-8').read()
rep = {'@@D@@': D, '@@ROADMAP_BLOB_D@@': ROADMAP_BLOB_D, '@@GUARD_BLOB_D@@': GUARD_BLOB_D,
       '@@OPEN@@': lit(d['open']), '@@PROPS@@': lit(d['props']), '@@COMPONENTS@@': lit(d['components']),
       '@@THEOREMS@@': lit(d['theorems']).replace('null', 'None'), '@@SENTENCES@@': lit(T.SENTENCES), '@@CLAUSE@@': lit(T.CLAUSE),
       '@@P0_END_D@@': lit(T.P0_END_D), '@@P0_CASE@@': lit(T.P0_CASE), '@@P0_STANDING_33@@': lit(T.P0_STANDING_33)}
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'controls.py', 'w', encoding='utf-8').write(t)
print('controls blob', blob(S + 'controls.py'))
if sys.argv[1:] != ['prereg']:
    raise SystemExit
spec = importlib.util.spec_from_file_location('c33', S + 'controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
bad, rows, dmuts, muts = C.self_test()
assert all(b.startswith('agreement:') for b in bad), bad
SELFTEST = ('```text\ncontrols: the two verdict propositions are duals and every shared text has one source; '
            '%d duality mutations fail as required\ncontrols: %d rows hold as frozen, %d mutation controls fail '
            'as required\ncontrols: self-test OK\n```' % (dmuts, rows, muts))
P = d['props']
L = json.load(open(S + 'locating33.json'))
FILES = {'OrbitGeometryRigidity': 'verification/lean-mathlib/OIBridge/OrbitGeometryRigidity.lean',
         'OrbitGeometryIsometries': 'verification/lean-mathlib/OIBridge/OrbitGeometryIsometries.lean',
         'OrbitGeometrySelector': 'verification/lean-mathlib/OIBridge/OrbitGeometrySelector.lean',
         'OrbitIsometryClassification': 'verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean',
         'OrbitLawGaps': 'verification/lean-mathlib/OIBridge/OrbitLawGaps.lean',
         'OrbitLawRigidityTwisted': 'verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean',
         'GramTrajectorySelection': 'verification/lean-mathlib/OIBridge/GramTrajectorySelection.lean',
         'TwoSidedGauge': 'verification/lean-mathlib/OIBridge/TwoSidedGauge.lean'}
rows = ['| what | where | line |', '| --- | --- | --- |']
byfile = {}
for n, (k, ln) in L['loc'].items():
    byfile.setdefault(k, []).append((ln, n))
for k in FILES:
    items = sorted(byfile.get(k, []))
    for i in range(0, len(items), 4):
        chunk = items[i:i + 4]
        rows.append('| %s | `%s` | %s |' % (', '.join('`%s`' % n for _, n in chunk), FILES[k] if i == 0 else 'the same file',
                                              ', '.join(str(ln) for ln, _ in chunk)))
LOCATING = '\n'.join(rows)
BLOBS = '\n'.join(['| file at `D` | blob |', '| --- | --- |'] + ['| `%s` | `%s` |' % (p.split('/')[-1] if p.startswith('verification/lean-mathlib/OIBridge/') else p, b)
                                                               for p, b in L['blobs'].items()])
RUN3, RUN3_OUTCOME = open(S + 'run3.txt').read().strip().split('\n', 1)
pt = open(S + 'prereg33.template.md', encoding='utf-8').read()
prep = {'@@CLAUSE_Q@@': '\n'.join('> ' + l for l in T.CLAUSE.split('\n')), '@@D@@': D,
        '@@ROADMAP_BLOB_D@@': ROADMAP_BLOB_D, '@@GUARD_BLOB_D@@': GUARD_BLOB_D, '@@OPEN@@': d['open'],
        '@@S_C@@': T.SENTENCES['A33-CLASSIFIED'], '@@S_NC@@': T.SENTENCES['A33-NOT-CLASSIFIED'], '@@S_X@@': T.SENTENCES['A33-UNDECIDED'],
        '@@P0_END_D@@': T.P0_END_D, '@@P0_C@@': T.P0_CASE['A33-CLASSIFIED'], '@@P0_NC@@': T.P0_CASE['A33-NOT-CLASSIFIED'],
        '@@P0_STAND33@@': T.P0_STANDING_33, '@@ROAD_C@@': blob(S + 'road-classified.md'), '@@ROAD_NC@@': blob(S + 'road-notclassified.md'),
        '@@CONTROLS_BLOB@@': blob(S + 'controls.py'), '@@N_DMUTS@@': str(dmuts), '@@N_MUTS@@': str(muts), '@@SELFTEST@@': SELFTEST,
        '@@LOCATING@@': LOCATING, '@@BLOBS@@': BLOBS, '@@RUN3@@': RUN3, '@@RUN3_OUTCOME@@': RUN3_OUTCOME}
for k in P:
    prep['@@%s@@' % k] = P[k]
order = ['@@SELFTEST@@'] + [k for k in prep if k != '@@SELFTEST@@']
for k in order:
    assert pt.count(k) >= 1 or k in ('@@ROADMAP_BLOB_D@@', '@@GUARD_BLOB_D@@'), k
    pt = pt.replace(k, prep[k])
assert '@@' not in pt, re.findall(r'@@\w+@@', pt)
open(S + 'preregistration.md', 'w', encoding='utf-8').write(pt)
print('prereg blob', blob(S + 'preregistration.md'), 'lines', pt.count('\n'))
