"""Step C: the exact stabilizer of the certified rational stratum point in G_ext, and its representation on ker DF, Def and R."""
import pickle, time, itertools
from lib36 import *
t0 = time.time()
X, Y = F4(z), F4(w)
S4 = list(itertools.permutations(range(4)))
def deph(M):
    n = len(M); M = [[M[i][j] * M[i][0].conj() for j in range(n)] for i in range(n)]      # unimodular: 1/x = conj x (scaled entries have |x|=1 here)
    return [[M[i][j] * M[0][j].conj() for j in range(n)] for i in range(n)]
def key(M): return tuple(x.key() for r in M for x in r)
def relabel(M, pi, tau): return [[M[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
def conj4(M): return [[x.conj() for x in r] for r in M]
def tr4(M): return [list(c) for c in zip(*M)]
assert all(x.norm2() == 1 for r in X for x in r) and all(x.norm2() == 1 for r in Y for x in r)
kX, kY = key(deph(X)), key(deph(Y))
def stab_pairs(A, target_key):
    return [(pi, tau) for pi in S4 for tau in S4 if key(deph(relabel(A, pi, tau))) == target_key]
ops = {}
for sw in (0, 1):
    for cj in (0, 1):
        for tr in (0, 1):
            A, B = (Y, X) if sw else (X, Y)
            if cj: A, B = conj4(A), conj4(B)
            if tr: A, B = tr4(A), tr4(B)
            ops[(sw, cj, tr)] = (stab_pairs(A, kX), stab_pairs(B, kY))
            print('op (swap %d, conj %d, transpose %d): factor stabilizer counts %d x %d' % (sw, cj, tr, len(ops[(sw, cj, tr)][0]), len(ops[(sw, cj, tr)][1])))
order = sum(len(a) * len(b) for a, b in ops.values())
print('exact stabilizer order of the rational stratum point in G_ext:', order, '(%.0fs)' % (time.time() - t0))
# elements as actions on theta (256 coordinates): (permutation p, sign s) meaning (g.theta)[p[m]] = s * theta[m]
def action(op, g1, g2):
    sw, cj, tr = op; (p1, t1), (p2, t2) = g1, g2
    perm = [0] * 256; sign = -1 if cj else 1
    for i in range(16):
        for j in range(16):
            a, b, c, d = i // 4, i % 4, j // 4, j % 4
            if sw: a, b, c, d = b, a, d, c
            if tr: a, b, c, d = c, d, a, b
            # the relabelling H'[pi(i), tau(j)] = H[i][j] on the factor indices; inverse convention is immaterial for the group as a set
            i2 = 4 * p1.index(a) + p2.index(b); j2 = 4 * t1.index(c) + t2.index(d)
            perm[i * 16 + j] = i2 * 16 + j2
    return (tuple(perm), sign)
elems = [action(op, g1, g2) for op, (A, B) in ops.items() for g1 in A for g2 in B]
assert len(set(elems)) == order
def apply(e, v):
    p, s = e; out = [0] * 256
    for m, x in enumerate(v): out[p[m]] = s * x
    return out
def compose(e, f):   # e after f
    p, s = e; q, t = f
    return (tuple(p[q[m]] for m in range(256)), s * t)
ident = (tuple(range(256)), 1)
assert ident in elems
E = set(elems)
assert all(compose(e, f) in E for e in elems[:40] for f in elems)   # closure spot-check
print('group closure spot-check passed')
# conjugacy classes
inv = {}
for e in elems:
    p, s = e; q = [0] * 256
    for m in range(256): q[p[m]] = m
    inv[e] = (tuple(q), s)
classes = []; seen = set()
for e in elems:
    if e in seen: continue
    cl = set(compose(compose(g, e), inv[g]) for g in elems); seen |= cl; classes.append(sorted(cl))
print('conjugacy classes:', len(classes), 'sizes', sorted(len(c) for c in classes))
B = pickle.load(open('stepB.pkl', 'rb')) if os.path.exists('stepB.pkl') else None
pickle.dump({'elems': elems, 'classes': classes, 'ops': {k: (len(a), len(b)) for k, (a, b) in ops.items()}, 'order': order}, open('stepC.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
