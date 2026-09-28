"""Analysis of the complete-membership run (state_complete) against the first run (state_full): deterministic replay
match of the orbit table, built-in controls, classification under three membership tests, distributions, and the
per-orbit data file orbits.tsv.gz. Writes census_summary.json."""
import json, gzip, collections, time
from lib41 import *
t0 = time.time()
S20 = json.load(open('structures20.json')); NAMES = S20['names']
REC2 = np.dtype([('key', '<u8', 11), ('first', '<u2', 16), ('n_sol', '<u8'), ('n_gauge', '<u8'), ('n_strict', '<u8'), ('n_hrep', '<u8'),
                 ('n_strict18', '<u8'), ('relmask_canon', '<u4'), ('strictmask_union', '<u4'), ('min_dsupp', '<u2'), ('canon_nnz', '<u2'),
                 ('min_gn_nnz', '<u2'), ('orbit_gauge', '<u2'), ('used', 'u1'), ('pad', 'u1', 7)])
H2 = ['magic', 'next_branch', 'b_end', 'n_orbits', 'sol', 'gauge', 'hrep', 'strict', 'relaxonly_sol', 'non_sol', 'ctrl_relax_mismatch',
      'ctrl_canon_not_idemp', 'ctrl_canon_checked', 'nodes', 'complete', 'nstruct', 'strict18', 'non18_sol', 'relaxonly18_sol',
      'ctrl_relax_popc_mismatch', 'ctrl_relax_mismatch18', 'sizeof_rec', 'x', 'y']
raw = open('state_complete/state.bin', 'rb').read()
h2 = dict(zip(H2, np.frombuffer(raw[:192], dtype='<u8').tolist()))
assert h2['sizeof_rec'] == REC2.itemsize, (h2['sizeof_rec'], REC2.itemsize)
R2 = np.frombuffer(raw[192:], dtype=REC2)
h1, R1 = load_table('state_full/state.bin')
print('header complete run', h2)
res = {}; bad = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-72s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    res[name] = {'ok': ok, 'got': str(got), 'want': str(want)}
    if not ok: bad.append(name)
chk('complete run finished, 20 structures', (h2['next_branch'], h2['complete'], h2['nstruct']), (1327, 1, 20))
chk('complete run: D-solutions, gauge classes, H_dom reps, orbits', (h2['sol'], h2['gauge'], h2['hrep'], h2['n_orbits']), (171552256, 30594431, h1['hrep'], h1['n_orbits']))
o1 = np.lexsort(R1['key'].T[::-1]); o2 = np.lexsort(R2['key'].T[::-1]); A1 = R1[o1]; A2 = R2[o2]
chk('replay: identical orbit keys', bool((A1['key'] == A2['key']).all()), True)
for f in ('first', 'n_sol', 'n_gauge', 'n_hrep', 'min_dsupp', 'canon_nnz', 'min_gn_nnz', 'orbit_gauge'):
    chk('replay: identical per-orbit %s' % f, bool((A1[f] == A2[f]).all()), True)
chk('built-in (complete): relaxed any-20 / any-18 / popcount mismatches', (h2['ctrl_relax_mismatch'], h2['ctrl_relax_mismatch18'], h2['ctrl_relax_popc_mismatch']), (0, 0, 0))
chk('built-in (complete): canonical-form idempotence failures', (h2['ctrl_canon_not_idemp'], h2['ctrl_canon_checked']), (0, h2['n_orbits']))
N = len(A2)
# ---- classifications -------------------------------------------------------------------------------------------
def classify(relany, nstrict):
    return np.where(~relany, 'NON-DITA', np.where(nstrict > 0, 'DITA', 'RELAXED-ONLY'))
cls = {
  'sorted18 (act-38 test)': classify(A1['relmask_canon'] != 0, A1['n_strict']),
  'complete18': classify((A2['relmask_canon'] & 0x3FFFF) != 0, A2['n_strict18']),
  'complete20': classify(A2['relmask_canon'] != 0, A2['n_strict']),
}
summary = {'domain_solutions': 171552256, 'gauge_classes': 30594431, 'hdom_reps': int(h2['hrep']), 'orbits': int(N), 'classes': {}, 'solutions_by_class': {}}
for k, c in cls.items():
    cnt = collections.Counter(c.tolist()); summary['classes'][k] = dict(cnt)
    sol = {z: int(A2['n_sol'][c == z].sum()) for z in ('DITA', 'RELAXED-ONLY', 'NON-DITA')}
    summary['solutions_by_class'][k] = sol
    print('  %-24s orbits %s | D-solutions by orbit class %s' % (k, dict(cnt), sol))
summary['per_solution'] = {'sorted18': {'strict': h1['strict'], 'relaxed_not_strict': h1['relaxonly_sol'], 'outside_relaxed': h1['non_sol']},
                           'complete20': {'strict': h2['strict'], 'relaxed_not_strict': h2['relaxonly_sol'], 'outside_relaxed': h2['non_sol']},
                           'complete18': {'strict': h2['strict18'], 'relaxed_not_strict': h2['relaxonly18_sol'], 'outside_relaxed': h2['non18_sol']}}
print('  per-solution', summary['per_solution'])
chk('sum over orbits of n_sol by class = total', sum(summary['solutions_by_class']['complete20'].values()), 171552256)
# differences between tests
d1 = int((cls['sorted18 (act-38 test)'] != cls['complete18']).sum()); d2 = int((cls['complete18'] != cls['complete20']).sum())
summary['orbits_reclassified'] = {'sorted18_vs_complete18': d1, 'complete18_vs_complete20': d2}
print('  orbits reclassified: sorted18 -> complete18: %d ; complete18 -> complete20: %d' % (d1, d2))
# ---- object orbits -------------------------------------------------------------------------------------------
C = decode_keys(A2['key']); keyidx = {bytes(C[x].reshape(256).astype(np.int8)): x for x in range(N)}
Mf = lambda f: [[f(i, j) for j in range(16)] for i in range(16)]
A, B, Cm = Mf(EA), Mf(EB), Mf(EC)
add = lambda *Xs: [[sum(X[i][j] for X in Xs) for j in range(16)] for i in range(16)]
objs = {'A': A, 'B': B, 'C': Cm, 'A+B': add(A, B), 'A+C': add(A, Cm), 'B+C': add(B, Cm), 'A+B+C': add(A, B, Cm), 'zero': Mf(lambda i, j: 0)}
summary['objects'] = {}
for k, E in objs.items():
    x = keyidx[bytes(np.array(canon_np(E), dtype=np.int8))]
    summary['objects'][k] = {z: str(cls[z][x]) for z in cls} | {'n_sol': int(A2['n_sol'][x]), 'min_dsupp': int(A2['min_dsupp'][x]),
                             'canon_nnz': int(A2['canon_nnz'][x]), 'min_gn_nnz': int(A2['min_gn_nnz'][x]), 'orbit_gauge': int(A2['orbit_gauge'][x])}
    print('  object', k, summary['objects'][k])
chk('C1: witness orbit NON-DITA under all three tests', [summary['objects']['A+B+C'][z] for z in cls], ['NON-DITA'] * 3)
chk('C3: zero orbit DITA under all three tests', [summary['objects']['zero'][z] for z in cls], ['DITA'] * 3)
chk('C2: A, B, C, A+B, A+C, B+C orbits DITA under all three tests', all(summary['objects'][k][z] == 'DITA' for k in ('A', 'B', 'C', 'A+B', 'A+C', 'B+C') for z in cls), True)
# ---- distributions ---------------------------------------------------------------------------------------------
def hist(v): return {int(a): int(b) for a, b in sorted(collections.Counter(v.tolist()).items())}
summary['hist'] = {}
for z in ('DITA', 'RELAXED-ONLY', 'NON-DITA'):
    m = cls['complete20'] == z
    summary['hist'][z] = {'min_dsupp': hist(A2['min_dsupp'][m]), 'canon_nnz': hist(A2['canon_nnz'][m]), 'min_gn_nnz': hist(A2['min_gn_nnz'][m]),
                          'orbit_gauge': hist(A2['orbit_gauge'][m]), 'n_sol': hist(A2['n_sol'][m])}
    print('  %s min_dsupp histogram (first 12):' % z, list(summary['hist'][z]['min_dsupp'].items())[:12])
summary['relaxed_structures_of_canon'] = {NAMES[k]: int(((A2['relmask_canon'] >> k) & 1).sum()) for k in range(20)}
summary['strict_union_structures'] = {NAMES[k]: int(((A2['strictmask_union'] >> k) & 1).sum()) for k in range(20)}
summary['controls'] = res; summary['failed'] = bad
json.dump(summary, open('census_summary.json', 'w'), indent=1)
# ---- per-orbit data file ---------------------------------------------------------------------------------------
with gzip.open('orbits.tsv.gz', 'wt') as f:
    f.write('# A41 census orbit table: one line per orbit of gauge x stabilizer x sign meeting D. first = a D-solution of the orbit, rows 1..15 as '
            '16-bit column masks (hex, bit j = column j; row 0 = 0); canonical form = lexmin gauge normal form (recompute from first with lib41.canon_np).\n')
    f.write('\t'.join(['orbit', 'first', 'n_sol', 'n_gauge', 'n_hrep', 'orbit_gauge', 'class_complete20', 'class_complete18', 'class_sorted18',
                       'relaxed_mask20_canon', 'strict_mask20_union', 'n_strict20', 'n_strict18_complete', 'n_strict18_sorted', 'min_dsupp', 'canon_nnz', 'min_gn_nnz']) + '\n')
    for x in range(N):
        r = A2[x]
        f.write('\t'.join([str(x), ','.join('%04x' % int(v) for v in r['first'][1:]), str(r['n_sol']), str(r['n_gauge']), str(r['n_hrep']), str(r['orbit_gauge']),
                           cls['complete20'][x], cls['complete18'][x], cls['sorted18 (act-38 test)'][x], '%05x' % r['relmask_canon'], '%05x' % r['strictmask_union'],
                           str(r['n_strict']), str(r['n_strict18']), str(A1['n_strict'][x]), str(r['min_dsupp']), str(r['canon_nnz']), str(r['min_gn_nnz'])]) + '\n')
print('FAILED' if bad else 'ALL GREEN', bad, '%.0fs' % (time.time() - t0))
