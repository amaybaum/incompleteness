"""EQ4-P exploration x10 -- the E2 contraction condition (n, a, b) = (2, 2, 1) on the sector cone K_A.
EXPLORATION (exact arithmetic, but a search over instances: leads only).  Research only.

E2 (p3 U2, case (2,2,1); a five-token crossing of type (1,1,1,2) with Bell links, plus co-self-duality from six
tokens) gives, for uniform triple cones K3: for all x, y in K3,
    M(x, y) = tr_U[ (PT_U(x) (x) 1_Q) (1_R (x) y) ]  is in K2 = PSD4      (x on (R, U1, U2), y on (Q, U1, U2)),
i.e. the map (U1 U2) -> Q with Choi matrix y (U first) sends x to a PSD pair operator.  This is a network condition
the colouring lemma does not cover for kappa-type elements.  Test it on the 92 generators of K_A (all pairs, as
GHZ-diagonal operators), then on images under random exact local filters.  Controls: PSD x, y give PSD M; dropping
the partial transpose gives a non-PSD M for some PSD pair (the transpose is load-bearing).
Output: counts and any non-PSD instance (a lead to be certified separately).  No VERDICT line (exploration).
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

rng = random.Random(2026100910)
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
GENS = []
for j in range(8):
    for k in range(j + 1, 8):
        GENS.append(("pair%d%d" % (j, k), PJ[j] + PJ[k]))
for j in range(8):
    GENS.append(("m%d" % j, I8 - PJ[j].scale(2)))
    for p in range(8):
        if p != j:
            GENS.append(("n%d%d" % (j, p), I8 - PJ[j].scale(2) + PJ[p].scale(2)))
R, U1, U2, Q = 0, 1, 2, 3


def M_of(x, y, transpose=True):
    xp = L.ptranspose(x, [U1, U2]) if transpose else x
    yq = L.reorder(L.relabel(y, {0: Q, 1: U1, 2: U2}), (Q, U1, U2))
    prod_ = L.matmul(L.tensor(xp, L.identity((Q,))), L.tensor(L.identity((R,)), yq))
    return L.ptrace(prod_, (R, Q))


# controls
ok_ctrl = True
for _ in range(4):
    x = L.rand_psd(rng, X3, rank=2)
    y = L.rand_psd(rng, X3, rank=2)
    ok_ctrl &= L.psd(M_of(x, y))[0]
cc = False
for _ in range(10):
    x = L.rand_psd(rng, X3, rank=1)
    y = L.rand_psd(rng, X3, rank=1)
    if not L.psd(M_of(x, y, transpose=False))[0]:
        cc = True
        break
print("controls: PSD x, y give PSD M: %s; without the partial transpose some PSD pair gives non-PSD M: %s" % (ok_ctrl, cc),
      flush=True)

bad = []
for nx, x in GENS:
    for ny, y in GENS:
        if not L.psd(M_of(x, y))[0]:
            bad.append((nx, ny))
print("generator pairs: %d, non-PSD M: %d %s" % (len(GENS) ** 2, len(bad), bad[:10]), flush=True)


def rand_local():
    mats = []
    for q in X3:
        A = [[L.rand_gauss(rng) for _ in range(2)] for _ in range(2)]
        mats.append(L.op(A, (q,)))
    return L.tensor(*mats)


neg_types = [g for g in GENS if not g[0].startswith("pair")]
bad_f = []
trials = 0
for nx, x in neg_types:
    for _ in range(2):
        ny, y = rng.choice(neg_types)
        kx, ky = rand_local(), rand_local()
        Mx = L.ad(kx, x)
        My = L.ad(ky, y)
        trials += 1
        if not L.psd(M_of(Mx, My))[0]:
            bad_f.append((nx, ny))
print("random local-filter images (pairs of negative generators): %d trials, non-PSD M: %d %s"
      % (trials, len(bad_f), bad_f[:10]), flush=True)
