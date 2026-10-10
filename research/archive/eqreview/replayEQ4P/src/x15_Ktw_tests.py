"""EQ4-P exploration x15 -- further necessary conditions on the c = 1 sector cone K_tw (p13).  EXPLORATION (exact
arithmetic, sampled instances: leads only).  Research only.

(a) E2 with twin links, case (n, a, b) = (2, 2, 1) (p3 U3; a five-token crossing of type (1,1,1,2)): for x, y in K3,
    M(x, y) = tr_U[(x (x) 1_Q)(1_R (x) y)] lies in the twin cone, i.e. PT_Q(M) is PSD.  Tested on all pairs of K_tw's
    36 generators (as GHZ-diagonal operators) and on random exact local-filter images.  Countercontrol: x = y = P_0
    (GHZ, which no c = 1 cone contains) is reported.
(b) twin-link networks (links SWAP/2): ring and the two K4 splits with random K_tw generators as nodes.
A failure is a lead (to be certified separately).  No VERDICT line (exploration).
"""
import random
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

rng = random.Random(2026100915)
X3 = (0, 1, 2)


def idx(x, y, z):
    return 4 * x + 2 * y + z


PJ = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = [0] * 8
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        PJ.append(L.ket_op(v, X3).scale(Fr(1, 2)))
GR = []
for perm in permutations(range(4)):
    for eps in product((0, 1), repeat=4):
        if sum(eps) % 2 == 0:
            GR.append(tuple(2 * perm[b] + (t ^ eps[b]) for b in range(4) for t in range(2)))


def act(g, v):
    w = [0] * 8
    for i in range(8):
        w[g[i]] = v[i]
    return tuple(w)


def orbit(v):
    return sorted(set(act(g, v) for g in GR))


def op_of(lam):
    out = L.Op(X3, {})
    for m in range(8):
        out = out + PJ[m].scale(lam[m])
    return out


VECS = sorted(set(orbit((1, 1, 0, 0, 0, 0, 0, 0)) + orbit((1, 1, 1, 1, 1, -1, 1, -1)) + orbit((-1, 3, 1, 1, 1, 1, 1, 1))))
GENS = [(v, op_of(v)) for v in VECS]
R, U1, U2, Q = 0, 1, 2, 3


def M_of(x, y):
    yq = L.reorder(L.relabel(y, {0: Q, 1: U1, 2: U2}), (Q, U1, U2))
    return L.ptrace(L.matmul(L.tensor(x, L.identity((Q,))), L.tensor(L.identity((R,)), yq)), (R, Q))


def twin_ok(M):
    return L.psd(L.ptranspose(M, [Q]))[0]


cc = twin_ok(M_of(PJ[0], PJ[0]))
print("countercontrol x = y = P_0 (GHZ): PT_Q(M) PSD = %s" % cc, flush=True)
bad = [(a, b) for a, x in GENS for b, y in GENS if not twin_ok(M_of(x, y))]
print("(a) generator pairs: %d, failing: %d %s" % (len(GENS) ** 2, len(bad), bad[:6]), flush=True)


def rand_local():
    return L.tensor(*[L.op([[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)], (q,)) for q in X3])


negs = [g for g in GENS if min(g[0]) < 0]
badf = []
for a, x in negs:
    for _ in range(3):
        b, y = rng.choice(negs)
        if not twin_ok(M_of(L.ad(rand_local(), x), L.ad(rand_local(), y))):
            badf.append((a, b))
print("(a) random filter images: %d trials, failing: %d %s" % (3 * len(negs), len(badf), badf[:6]), flush=True)


def rel(A, m, qs):
    return L.reorder(L.relabel(A, m), qs)


def place(A, qs):
    return rel(A, {0: qs[0], 1: qs[1], 2: qs[2]}, qs)


def ring(e, f, x, y):
    return L.pair(L.tensor(place(e, (0, 1, 2)), place(f, (3, 4, 5))), L.tensor(place(x, (0, 1, 3)), place(y, (2, 4, 5))))


a_, b_, ap, bp = 10, 11, 12, 13


def k4(s1, s2, e1, e2, split):
    x = place(s1, (a_, 1, 2))
    y = place(s2, (b_, 3, 4))
    xq, yq = ((place(e1, (ap, 1, 3)), place(e2, (bp, 2, 4))) if split == 0
              else (place(e1, (ap, 1, 4)), place(e2, (bp, 2, 3))))
    return L.pair(L.tensor(L.swap_half(a_, b_), xq, yq), L.tensor(x, y, L.swap_half(ap, bp)))


lo = {}
for _ in range(200):
    v = ring(*[rng.choice(GENS)[1] for _ in range(4)])
    lo["ring"] = min(lo.get("ring", v.re), v.re) if v.im == 0 else Fr(-10 ** 9)
for _ in range(100):
    for sp in (0, 1):
        v = k4(*[rng.choice(GENS)[1] for _ in range(4)], sp)
        key = "K4 split %d (twin links)" % sp
        lo[key] = min(lo.get(key, v.re), v.re) if v.im == 0 else Fr(-10 ** 9)
for k in sorted(lo):
    print("(b) %-24s minimum %s" % (k, lo[k]), flush=True)
