import json, re, subprocess, sys
S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/'
d = json.load(open(S + 'a31/props31.json', encoding='utf-8'))
p0 = json.load(open(S + 'a31/p0-31.json', encoding='utf-8'))
spec = __import__('importlib.util').util.spec_from_file_location('c30', S + 'a30/controls.py')
C30 = __import__('importlib.util').util.module_from_spec(spec); spec.loader.exec_module(C30)
CLAUSE = C30.CLAUSE.replace('Act 30 classifies', 'Act 31 classifies', 1)
assert CLAUSE != C30.CLAUSE
SENT = {
 'A31-1-NONUNIQUE': "At the frozen product configuration, for the pair of local class bijections act 28 fixed in advance, two exhibited transition families each satisfy all eight prefix conjuncts and factorization with factor families realizing that pair, and take `GramPhaseEquiv`-inequivalent values at time zero on an exhibited tuple realizable at the product visible family whose class lies outside the product locus, at evidence level 2. This is a nonuniqueness statement about two exhibited laws at that pair and that time. It does not say that factorization is empty, has no content, or fails to restrict anything, and it reports nothing about any other pair or configuration.",
 'A31-1-UNIQUE': "At the frozen product configuration, for the pair of local class bijections act 28 fixed in advance, any two transition families satisfying all eight prefix conjuncts and factorization with factor families realizing that pair take `GramPhaseEquiv`-equivalent values at time zero on every tuple realizable at the product visible family whose class lies outside the product locus, at evidence level 2. The agreement asserted is agreement up to `GramPhaseEquiv` at time zero, not equality of families, and it is asserted for that pair alone.",
 'A31-1-UNDECIDED': "Neither the nonuniqueness nor the uniqueness was obtained. The step at which the proof stopped is named, with what would settle it.",
}
def blob(path):
    return subprocess.run(['git', 'hash-object', path], capture_output=True, text=True).stdout.strip()
D = 'd61c6c5409db201e3c25abbf3ec0ecce1f530684'
lit = lambda x: json.dumps(x, ensure_ascii=False, indent=1)
t = open(S + 'a31/controls31.template.py', encoding='utf-8').read()
rep = {'@@D@@': D, '@@ROADMAP_BLOB_D@@': blob(S + 'a31/road-D.md'),
       '@@GUARD_BLOB_D@@': subprocess.run(['git', '-C', '/home/user/incompleteness', 'rev-parse', D + ':verification/lean/edge_rigidity_probe.py'], capture_output=True, text=True).stdout.strip(),
       '@@OPEN@@': lit(d['open']), '@@PROPS@@': lit(d['props']), '@@COMPONENTS@@': lit(d['components']),
       '@@SENTENCES@@': lit(SENT), '@@CLAUSE@@': lit(CLAUSE), '@@P0_STANDING@@': lit(p0['STANDING']),
       '@@P0_ADMITS@@': lit(p0['ADMITS']),
       '@@P0_CASE@@': lit({'A31-1-NONUNIQUE': p0['NONUNIQUE'], 'A31-1-UNIQUE': p0['UNIQUE']})}
for k, v in rep.items():
    assert t.count(k) == 1, k
    t = t.replace(k, v)
assert '@@' not in t
open(S + 'a31/controls.py', 'w', encoding='utf-8').write(t)
if sys.argv[1:] == ['controls']:
    raise SystemExit
pt = open(S + 'a31/prereg31.template.md', encoding='utf-8').read()
P = d['props']
prep = {'@@CLAUSE_Q@@': '\n'.join('> ' + l for l in CLAUSE.split('\n')), '@@D@@': D,
        '@@ROADMAP_BLOB_D@@': rep['@@ROADMAP_BLOB_D@@'], '@@GUARD_BLOB_D@@': rep['@@GUARD_BLOB_D@@'],
        '@@OPEN@@': d['open'], '@@P_N@@': P['P_N'], '@@P_U@@': P['P_U'], '@@S_W@@': P['S_W'],
        '@@S_TAU@@': P['S_TAU'], '@@S_PRE@@': P['S_PRE'],
        '@@EVIDENCE@@': open(S + 'a31/evidence31.md', encoding='utf-8').read().rstrip('\n'),
        '@@S_N@@': SENT['A31-1-NONUNIQUE'], '@@S_U@@': SENT['A31-1-UNIQUE'], '@@S_X@@': SENT['A31-1-UNDECIDED'],
        '@@P0_ADMITS@@': p0['ADMITS'], '@@P0_STANDING@@': p0['STANDING'], '@@P0_N@@': p0['NONUNIQUE'],
        '@@P0_U@@': p0['UNIQUE'], '@@ROAD_N@@': blob(S + 'a31/road-nonunique.md'),
        '@@ROAD_U@@': blob(S + 'a31/road-unique.md'), '@@CONTROLS_BLOB@@': blob(S + 'a31/controls.py'),
        '@@N_DMUTS@@': open(S + 'a31/ndm.txt').read().strip(), '@@N_MUTS@@': open(S + 'a31/nm.txt').read().strip(),
        '@@SELFTEST@@': open(S + 'a31/selftest31.md', encoding='utf-8').read().rstrip('\n')}
for k in ('@@EVIDENCE@@', '@@SELFTEST@@') + tuple(x for x in prep if x not in ('@@EVIDENCE@@', '@@SELFTEST@@')):
    assert pt.count(k) >= 1, k
    pt = pt.replace(k, prep[k])
assert '@@' not in pt, re.findall(r'@@\w+@@', pt)
open(S + 'a31/preregistration.md', 'w', encoding='utf-8').write(pt)
print('prereg blob', blob(S + 'a31/preregistration.md'), 'controls blob', blob(S + 'a31/controls.py'))
