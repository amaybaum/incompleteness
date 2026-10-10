"""EQ4-P exploration x11 -- Bell-link network values with nodes from the sector cone K_A.
EXPLORATION (exact arithmetic, but a random search over node choices: leads only).  Research only.

Nodes are generators of K_A as GHZ-diagonal operators (P_j + P_k, I - 2P_j, I - 2P_j + 2P_p); with co-self-duality
and T fixing the sector, each is admissible both as a state and as an effect.  Networks (as in p7 / p11): ring
(states on (0,1,3), (2,4,5); effects on (0,1,2), (3,4,5)), K4 with Bell pair links (both splits), the nine-token
3 x 3 Latin square (row states, column effects).  Also the ring and K4 with local-filter images of the nodes (random
exact filters).  A negative value is a lead (to be certified separately).  No VERDICT line (exploration).
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

rng = random.Random(2026100911)
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
I8 = L.identity(X3)
NEG = [I8 - PJ[j].scale(2) for j in range(8)]
NEG += [I8 - PJ[j].scale(2) + PJ[p].scale(2) for j in range(8) for p in range(8) if p != j]
POS = [PJ[j] + PJ[k] for j in range(8) for k in range(j + 1, 8)]
ALL = NEG + POS


def rel(A, m, qs):
    return L.reorder(L.relabel(A, m), qs)


def place(A, qs):
    return rel(A, {0: qs[0], 1: qs[1], 2: qs[2]}, qs)


def rand_local():
    return L.tensor(*[L.op([[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)], (q,)) for q in X3])


def ring(e, f, x, y):
    return L.pair(L.tensor(place(e, (0, 1, 2)), place(f, (3, 4, 5))), L.tensor(place(x, (0, 1, 3)), place(y, (2, 4, 5))))


a_, b_, ap, bp = 10, 11, 12, 13


def k4(s1, s2, e1, e2, split):
    x = place(s1, (a_, 1, 2))
    y = place(s2, (b_, 3, 4))
    if split == 0:
        xq, yq = place(e1, (ap, 1, 3)), place(e2, (bp, 2, 4))
    else:
        xq, yq = place(e1, (ap, 1, 4)), place(e2, (bp, 2, 3))
    return L.pair(L.tensor(L.phi_plus(a_, b_), xq, yq), L.tensor(x, y, L.phi_plus(ap, bp)))


rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
cols = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]


def latin(R, C):
    return L.pair(L.tensor(*[place(c, q) for c, q in zip(C, cols)]), L.tensor(*[place(r, q) for r, q in zip(R, rows)]))


stats = {}


def rec(name, v):
    lo, n, negs = stats.get(name, (None, 0, 0))
    vr = v.re
    stats[name] = (vr if lo is None or vr < lo else lo, n + 1, negs + int(v.im != 0 or vr < 0))


for _ in range(400):
    rec("ring", ring(*[rng.choice(NEG) for _ in range(4)]))
    rec("ring mixed", ring(*[rng.choice(ALL) for _ in range(4)]))
for _ in range(150):
    for sp in (0, 1):
        rec("K4 split %d" % sp, k4(*[rng.choice(NEG) for _ in range(4)], sp))
for _ in range(60):
    rec("Latin", latin([rng.choice(NEG) for _ in range(3)], [rng.choice(NEG) for _ in range(3)]))
for _ in range(60):
    nodes = [L.ad(rand_local(), rng.choice(NEG)) for _ in range(4)]
    rec("ring filtered", ring(*nodes))
    nodes = [L.ad(rand_local(), rng.choice(NEG)) for _ in range(4)]
    rec("K4 split 0 filtered", k4(*nodes, 0))
for k, (lo, n, negs) in sorted(stats.items()):
    print("%-22s instances %4d  minimum %-14s  negative or complex: %d" % (k, n, lo, negs), flush=True)
