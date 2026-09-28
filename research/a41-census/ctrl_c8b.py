"""C8 (complete notion) and C11: (a) the stabilizer permutes the 20 Dita index structures of SIG (act 37's transport,
extended by k5) -- classes; (b) for sampled D-solutions E, group elements g and every structure S:
member(E, S) == member(g.E + gauge, g(S)) for the complete (all-matchings) relaxed test, while the act-38 sorted-matching
test is shown to violate the same identity (the mechanism of the red C8); (c) matchlib's sorted-only conditions
reproduce lib41's struct_eqs membership exactly (the two implementations agree when restricted to the identity)."""
import json, random
from lib41 import *
from matchlib import prop_eqs, lam_eqs, satisfies
S20 = json.load(open('structures20.json')); ST = S20['structures']; NAMES = S20['names']
def canon_idx(form, mn, blocks, groups):
    return (form, tuple(mn), tuple(sorted(tuple(sorted(b)) for b in blocks)), tuple(sorted(tuple(sorted(g)) for g in groups)))
KEY = {canon_idx(st['form'], st['shape'], st['blocks'], st['groups']): k for k, st in enumerate(ST)}
assert len(KEY) == 20
def perm_pair(e):
    p, s_ = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', rp, cq
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    assert all(p[i * 16 + j] == phi[j] * 16 + psi[i] for i in range(16) for j in range(16))
    return 'transposed', psi, phi
def transport(k, e):
    st = ST[k]; kind = st['form']; mn = st['shape']; cp, rows = st['blocks'], st['groups']
    form, f1, f2 = perm_pair(e)
    if form == 'product':
        rp, cq = f1, f2
        if kind == 'column': return KEY[canon_idx('column', mn, [[cq[j] for j in b] for b in cp], [[rp[i] for i in r] for r in rows])]
        return KEY[canon_idx('row', mn, [[rp[i] for i in b] for b in cp], [[cq[j] for j in r] for r in rows])]
    psi, phi = f1, f2
    if kind == 'column': return KEY[canon_idx('row', mn, [[phi[j] for j in b] for b in cp], [[psi[i] for i in r] for r in rows])]
    return KEY[canon_idx('column', mn, [[psi[i] for i in b] for b in cp], [[phi[j] for j in r] for r in rows])]
res = {}; bad = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-70s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    res[name] = {'ok': ok, 'got': str(got)}
    if not ok: bad.append(name)
TR = [[transport(k, e) for k in range(20)] for e in elems]
chk('every stabilizer element maps each of the 20 index structures to one of the 20', all(sorted(t) == list(range(20)) for t in TR), True)
orbs = []; seen = set()
for k in range(20):
    if k in seen: continue
    o = sorted(set(t[k] for t in TR)); seen |= set(o); orbs.append([NAMES[x] for x in o])
print('  classes:', orbs)
chk('classes modulo the stabilizer: 10 of size 2 (column/row pairs)', sorted(len(o) for o in orbs), [2] * 10)
# cached equations
PE = [prop_eqs(st['blocks'], st['groups'], st['transpose']) for st in ST]
LE = {(k, rel): [[lam_eqs(st['blocks'], st['groups'], b, tuple(sb), rel, st['transpose']) for sb in st['relaxed' if rel else 'strict'][b]] for b in range(1, len(st['groups']))] for k, st in enumerate(ST) for rel in (False, True)}
LE_ID = {(k, rel): [lam_eqs(st['blocks'], st['groups'], b, tuple(range(st['shape'][0])), rel, st['transpose']) for b in range(1, len(st['groups']))] for k, st in enumerate(ST) for rel in (False, True)}
def mem(flat, k, rel, complete=True):
    if not satisfies(flat, PE[k]): return False
    if complete: return all(any(satisfies(flat, L) for L in Ls) for Ls in LE[(k, rel)])
    return all(satisfies(flat, L) for L in LE_ID[(k, rel)])
# (c) sorted-only matchlib == lib41 struct_eqs on the 18
F = np.load('first_solutions.npy'); random.seed(8)
sample = random.sample(range(len(F)), 300)
names18 = [(nm, f) for nm, f, s, tr in STRUCTS18]
mism = 0
for x in sample:
    E = F[x].tolist(); flat = [v for r in E for v in r]
    for rel in (False, True):
        a = set(members(E, rel)); b = set(tuple(NAMES[k].split('-')) for k in range(18) if mem(flat, k, rel, complete=False))
        if a != b: mism += 1
chk('C11: matchlib sorted-only conditions == lib41 struct_eqs (300 solutions, strict and relaxed)', mism, 0)
# (b) transport identity
viol_c = 0; viol_s = 0; checks = 0
for x in sample[:150]:
    E = F[x].tolist(); flat = [v for r in E for v in r]
    for _ in range(4):
        gi = random.randrange(1024); e = elems[gi]
        for sgn in (1, -1):
            Y = act((e[0], e[1] * sgn), E)
            r_ = [random.randint(-2, 2) for _ in range(16)]; c_ = [random.randint(-2, 2) for _ in range(16)]
            Y = [[Y[i][j] + r_[i] + c_[j] for j in range(16)] for i in range(16)]
            fy = [v for r in Y for v in r]
            for k in range(20):
                checks += 1
                if mem(flat, k, True) != mem(fy, TR[gi][k], True): viol_c += 1
                if k < 18 and TR[gi][k] < 18 and mem(flat, k, True, False) != mem(fy, TR[gi][k], True, False): viol_s += 1
chk('C8b: complete relaxed membership transported by the group (%d checks)' % checks, viol_c, 0)
print('  sorted-matching relaxed test: transport violations %d (the mechanism of the red C8)' % viol_s)
res['sorted_transport_violations'] = viol_s
json.dump({'controls': res, 'failed': bad, 'classes': orbs}, open('ctrl_c8b.json', 'w'), indent=1)
print('FAILED' if bad else 'ALL GREEN', bad)
