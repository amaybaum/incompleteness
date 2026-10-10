"""EQ4-SIX probe s4 -- the glue network (A4) on the GHZ-diagonal sector models, exhaustively and exactly.

Usage:  python3 -I -B s4_glue_sector.py <base>/verification/lean-mathlib/OIBridge
Imports the copied library eq4_lib.py (sha256 cc2c6aca94007ac8) for the transcription control and an independent
cross-check; the bulk contraction uses numpy int64 einsum on integer tensors (exact: all entries are integers and the
magnitudes stay far below 2^53; a bound is checked).

Glue network, crossing split, links w (state glue) and z (effect glue):
  N = sum e[s r1 u1; s' r1' u1'] f[s r2 u2; s' r2' u2'] x[p' r1' r2'; p r1 r2] y[p' u1' u2'; p u1 u2] * link factors.
c = 0: Bell links (w = z = Phi+), effects e = T(e~) = e~ for GHZ-diagonal e~ (T fixes GD).  c = 1: twin links
(w = z = SWAP/2), effects in K3* = K3 directly.
Integer scaling: nodes 2 P_j (entries 0, +-1); links 2 Phi+ = sum |ii><jj| and 2 SWAP/2 = SWAP; so the integer
network value is 2^4 * 2^2 = 64 times the true value for unit-scaled P_j nodes and normalized links.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S4-GLUE-SECTOR-EXACT` iff all:
  K  transcription control.
  X  cross-check of the integer contraction against eq4_lib operators (cond / pair) on 6 random GHZ-projector
     quadruples (c = 0 and c = 1).
  A  c = 0: the glue value is >= 0 for all 92^4 ordered quadruples of K_A generators (exhaustive); minimum printed.
  W  c = 1: the twin-link glue value is >= 0 for all 36^4 ordered quadruples of K_tw generators (exhaustive).
  C  countercontrols: (i) c = 0 with all four nodes from S* = cone{e_j, m_j} (the GD shadow of BS*, which holds GHZ
     and W3 together): some quadruple is negative; (ii) c = 1 with the twin links replaced by Bell links on K_tw: the
     minimum differs from the twin minimum (the link type matters).
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s4_glue_sector")
rng = random.Random(2026100954)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])


def idx(x, y, z):
    return 4 * x + 2 * y + z


VEC = []
for b in range(4):
    b1, b2 = b >> 1, b & 1
    for t in range(2):
        v = [0] * 8
        v[idx(0, b1, b2)] = 1
        v[idx(1, 1 - b1, 1 - b2)] = 1 if t == 0 else -1
        VEC.append(v)
P2 = [np.outer(np.array(v), np.array(v)).astype(np.int64) for v in VEC]   # 2 P_j, integer


def t6(M):
    return M.reshape(2, 2, 2, 2, 2, 2)


BELL2 = np.zeros((2, 2, 2, 2), dtype=np.int64)    # 2 Phi+ [ket p, ket q; bra p, bra q]
SWAP = np.zeros((2, 2, 2, 2), dtype=np.int64)
for a in range(2):
    for b in range(2):
        BELL2[a, a, b, b] = 1
        SWAP[a, b, b, a] = 1


def glue_int(x, y, e, f, link):
    """integer glue value with integer nodes and integer links (link applied to (p,q) as an effect and to (s,t) as a
    state).  Glue_s[R U; R' U'] = sum w[p q; p' q'] x[p' R; p R'] y[q' U; q U'];
    Glue_e[R U; R' U'] = sum z[s t; s' t'] e[s' r1 u1; s r1' u1'] f[t' r2 u2; t r2' u2']  (tr_st[(z (x) 1)(e (x) f)])."""
    gs = np.einsum("pqPQ,PabpAB,QcdqCD->abcdABCD", link, t6(x), t6(y))
    ge = np.einsum("stST,SacsAC,TbdtBD->abcdABCD", link, t6(e), t6(f))
    return int(np.einsum("abcdABCD,ABCDabcd->", ge, gs))


# cross-check against eq4_lib
P_, Q_, R1, R2, U1, U2, S_, T_ = 10, 11, 12, 13, 14, 15, 16, 17


def lib_op(M, qs):
    return L.op([[int(M[r][c]) for c in range(8)] for r in range(8)], qs)


def glue_lib(x, y, e, f, link_kind):
    if link_kind == "bell":
        w = L.phi_plus(P_, Q_).scale(2)
        z = L.phi_plus(S_, T_).scale(2)
    else:
        w = L.swap_half(P_, Q_).scale(2)
        z = L.swap_half(S_, T_).scale(2)
    gs = L.cond(w, L.tensor(lib_op(x, (P_, R1, R2)), lib_op(y, (Q_, U1, U2))))
    ge = L.cond(z, L.tensor(lib_op(e, (S_, R1, U1)), lib_op(f, (T_, R2, U2))))
    return L.pair(ge, gs)


ok_x = True
for kind, link in (("bell", BELL2), ("twin", SWAP)):
    for _ in range(3):
        ii = [rng.randrange(8) for _ in range(4)]
        v_int = glue_int(P2[ii[0]], P2[ii[1]], P2[ii[2]], P2[ii[3]], link)
        v_lib = glue_lib(P2[ii[0]], P2[ii[1]], P2[ii[2]], P2[ii[3]], kind)
        ok_x &= v_lib == L.G(v_int)
rep.check("X integer contraction = eq4_lib operator contraction on 6 random GHZ-projector quadruples (Bell and twin)", ok_x)

# tau tensors
TAU = {}
for kind, link in (("bell", BELL2), ("twin", SWAP)):
    tau = np.zeros((8, 8, 8, 8), dtype=np.int64)
    for i, j, k, l in itertools.product(range(8), repeat=4):
        tau[i, j, k, l] = glue_int(P2[i], P2[j], P2[k], P2[l], link)
    TAU[kind] = tau


def gens_KA():
    G = []
    for j, k in itertools.combinations(range(8), 2):
        G.append([1 if i in (j, k) else 0 for i in range(8)])
    for j in range(8):
        G.append([1 - 2 * (i == j) for i in range(8)])
    for j in range(8):
        for p in range(8):
            if p != j:
                G.append([1 - 2 * (i == j) + 2 * (i == p) for i in range(8)])
    return np.array(G, dtype=np.int64)


gens = [(1, 0, 3, 2, 5, 4, 7, 6), (6, 7, 4, 5, 2, 3, 0, 1), (4, 5, 6, 7, 0, 1, 2, 3), (2, 3, 0, 1, 6, 7, 4, 5),
        (1, 0, 3, 2, 4, 5, 6, 7), (0, 1, 2, 3, 6, 7, 4, 5), (0, 1, 4, 5, 2, 3, 6, 7)]
group = {tuple(range(8))}
frontier = [tuple(range(8))]
while frontier:
    nf = []
    for g in frontier:
        for h in gens:
            c = tuple(g[h[i]] for i in range(8))
            if c not in group:
                group.add(c)
                nf.append(c)
    frontier = nf


def orbit(vec):
    return sorted({tuple(vec[g[i]] for i in range(8)) for g in group})


def gens_Ktw():
    return np.array(orbit((1, 1, 0, 0, 0, 0, 0, 0)) + orbit((1, 1, 1, 1, 1, -1, 1, -1))
                    + orbit((-1, 3, 1, 1, 1, 1, 1, 1)), dtype=np.int64)


def min_over(tau, Gx, Gy, Ge, Gf):
    # value(a, b, c, d) = sum tau[i,j,k,l] Gx[a,i] Gy[b,j] Ge[c,k] Gf[d,l]; bound check for int64 exactness
    bound = int(np.abs(tau).sum()) * int(np.abs(Gx).max() * np.abs(Gy).max() * np.abs(Ge).max() * np.abs(Gf).max())
    assert bound < 2 ** 62
    t3 = np.einsum("ijkl,dl->ijkd", tau, Gf)
    t2 = np.einsum("ijkd,ck->ijcd", t3, Ge)
    best = None
    for a in range(Gx.shape[0]):
        t1 = np.einsum("ijcd,i->jcd", t2, Gx[a])
        vals = np.einsum("jcd,bj->bcd", t1, Gy)
        m = int(vals.min())
        best = m if best is None else min(best, m)
    return best


GA = gens_KA()
GT = gens_Ktw()
mA = min_over(TAU["bell"], GA, GA, GA, GA)
rep.check("A c = 0: glue network >= 0 on all %d^4 quadruples of K_A generators (min integer value %d; true value = /64)"
          % (len(GA), mA), mA >= 0)
mT = min_over(TAU["twin"], GT, GT, GT, GT)
rep.check("W c = 1: twin-link glue network >= 0 on all %d^4 quadruples of K_tw generators (min integer value %d)"
          % (len(GT), mT), mT >= 0)
Spair = np.array([[1 if i in (j, k) else 0 for i in range(8)] for j, k in itertools.combinations(range(8), 2)],
                 dtype=np.int64)
Sstar = np.array([[1 if i == j else 0 for i in range(8)] for j in range(8)]
                 + [[1 - 2 * (i == j) for i in range(8)] for j in range(8)], dtype=np.int64)
mC1 = min_over(TAU["bell"], Sstar, Sstar, Sstar, Sstar)
mC2 = min_over(TAU["bell"], GT, GT, GT, GT)
rep.check("C countercontrols: (i) all four nodes in S* (GD shadow of BS*, GHZ and W3 together) reach %d < 0; "
          "(ii) K_tw with Bell links instead of twin links: min %d (differs from the twin minimum %d)"
          % (mC1, mC2, mT), mC1 < 0 and mC2 != mT)
rep.verdict("S4-GLUE-SECTOR-EXACT")
