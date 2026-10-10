"""The independent computation (draft): at each point of the frozen point list, act 36's exhaustive partition search on
the numeric matrix, then every alignment counted by a pruned matching search of its own, strict with factor unitarity and
relaxed. No flat calculus, no act-40 candidate enumeration, no production canonical form. Read-only, local."""
import itertools, json, sys, time
from fractions import Fraction as Fr
exec(open('probe_head.py', encoding='utf-8').read())
src = open('../a40/dita_torus_locus_probe.py', encoding='utf-8').read()
exec(src[src.index('def H3(u1, u2, u3)'):src.index('K2, K8, DD')])
exec(src[src.index('TESTU = '):src.index('face_ok = []')])
exec(src[src.index('PTS = ['):src.index('agree = []; counts = []')])
t1 = time.time()

def matchings(allowed):
    """number of perfect matchings a -> distinct rows, allowed[a] the admissible rows of label a"""
    m = len(allowed); cnt = 0
    def rec(a, used):
        nonlocal cnt
        if a == m: cnt += 1; return
        for r in allowed[a]:
            if r not in used: used.add(r); rec(a + 1, used); used.discard(r)
    rec(0, set()); return cnt

def valid_alignments(H, m, n, cp, rows, relaxed):
    col0 = [cp[c][0] for c in range(m)]
    lam0 = [[H[rows[0][a]][col0[c]] * H[rows[0][0]][col0[c]].conj() for c in range(m)] for a in range(m)]
    if not relaxed:
        if not is_unitary_s(lam0, m): return 0
    per_b = []                       # for each class b >= 1: {reference row r0: number of label matchings}
    for b in range(1, n):
        d = {}
        for r0 in rows[b]:
            allowed = [[r0]]
            for a in range(1, m):
                ok = []
                for r in rows[b]:
                    lb = [H[r][col0[c]] * H[r0][col0[c]].conj() for c in range(m)]
                    if not relaxed: good = all(lb[c] == lam0[a][c] for c in range(m))
                    else: good = all(lb[c] * lam0[a][0] == lam0[a][c] * lb[0] for c in range(1, m))
                    if good: ok.append(r)
                allowed.append(ok)
            k = matchings(allowed)
            if k: d[r0] = k
        per_b.append(d)
    if any(not d for d in per_b): return 0
    total = 0
    for combo in itertools.product(*[sorted(d) for d in per_b]):
        refs = [rows[0][0]] + list(combo)
        if not relaxed and not all(is_unitary_s([[H[r][cp[c][dd]] for dd in range(n)] for r in refs], n) for c in range(m)): continue
        k = 1
        for b, r0 in enumerate(combo): k *= per_b[b][r0]
        total += k
    return total

def census(H):
    out = {}
    HT = [list(c) for c in zip(*H)]
    for relaxed in (False, True):
        res = []
        for form, M in (('column', H), ('row', HT)):
            for (m, n) in SHAPES3:
                for cp, rws, ok, _, _ in dita_orientations(M, m, n):
                    k = valid_alignments(M, m, n, cp, rws, relaxed)
                    if k: res.append([form, [m, n], sorted(map(sorted, cp)), sorted(map(sorted, rws)), k])
        out['relaxed' if relaxed else 'strict'] = sorted(res)
    return out

def Pu(u): return [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
def gval_pt(ang, s, t):
    v = ONE
    for _ in range(int(ang * 4) % 4): v = v * I_
    for _ in range(abs(s)): v = v * (z if s > 0 else z.conj())
    for _ in range(abs(t)): v = v * (w if t > 0 else w.conj())
    return v
u60 = G(Fr(3599, 3601), Fr(120, 3601)); u5 = G(Fr(3, 5), Fr(4, 5))
POINTS = [('SIG', H3(ONE, ONE, ONE)), ('Pu(-1)', Pu(G(-1))), ('P = Pu(u60)', Pu(u60)), ('Pu(u5)', Pu(u5)), ('Hu(-1)', H3(G(-1), G(-1), G(-1)))]
POINTS += [('act40 %d %s' % (i, nm), H3(*u)) for i, (nm, u) in enumerate(PTS)]
for ang, s, t in [(0, -1, -1), (Fr(1, 2), -1, -1), (0, -1, 0), (Fr(1, 2), -1, 0), (0, -1, 1), (Fr(1, 2), -1, 1), (0, 0, -1), (Fr(1, 2), 0, -1),
                  (0, 0, 0), (Fr(1, 4), 0, 0), (Fr(1, 2), 0, 0), (Fr(3, 4), 0, 0), (0, 0, 1), (Fr(1, 2), 0, 1), (0, 1, -1), (Fr(1, 2), 1, -1),
                  (0, 1, 0), (Fr(1, 2), 1, 0), (0, 1, 1), (Fr(1, 2), 1, 1)]:
    u = gval_pt(Fr(ang), s, t); POINTS.append(('Hu zeta(%s) z^%d w^%d' % (ang, s, t), H3(u, u, u)))
only = sys.argv[1:] if len(sys.argv) > 1 else None
res = {}
for nm, H in POINTS:
    if only and not any(o in nm for o in only): continue
    res[nm] = census(H)
    print('%-34s strict %2d (alignments %s)  relaxed %2d (alignments %s)   (%.0fs)' % (nm, len(res[nm]['strict']), sum(x[4] for x in res[nm]['strict']),
          len(res[nm]['relaxed']), sum(x[4] for x in res[nm]['relaxed']), time.time() - t1), flush=True)
json.dump(res, open('indep41.json', 'w'), sort_keys=True)
