"""Exploration only. Separation of phi (conj on C0 only) from every family member through the
coordinate-permutation-invariant multilinear forms T_k(x1..xk) = sum_p prod_l mixedTriple(G_l) p
= tr(K^3), K = sum_i (G_1)_i o ... o (G_k)_i (entrywise).  Members act on features by x -> x o s
(shapes 1,4) or x -> conj(x o s) (shapes 2,3), so T_k(h..) = T_k(..) or conj T_k(..)."""
import itertools
from fractions import Fraction
from bilinear import tuple_at, conjT, gmul, gadd, gconj, ZERO, ONE, I, B_direct
P = {"1": ONE, "i": I, "-1": (Fraction(-1), Fraction(0)), "-i": (Fraction(0), Fraction(-1))}

def Tk(Gs):
    K = [[None]*4 for _ in range(4)]
    for j in range(4):
        for k in range(4):
            acc = ZERO
            for i in range(4):
                prod = ONE
                for G in Gs:
                    prod = gmul(prod, G[i][j][k])
                acc = gadd(acc, prod)
            K[j][k] = acc
    tr = ZERO
    for a in range(4):
        for b in range(4):
            for c in range(4):
                tr = gadd(tr, gmul(gmul(K[a][b], K[b][c]), K[c][a]))
    return tr

def phi(r, G):
    return conjT(G) if r == 0 else G

pts = [(r, n) for r in range(9) for n in P]
res14, res23 = [], []
for combo in itertools.combinations_with_replacement(pts, 3):
    Gs = [tuple_at(r, P[n]) for (r, n) in combo]
    t = Tk(Gs)
    tp = Tk([phi(r, G) for (r, _), G in zip(combo, Gs)])
    if tp != t:
        res14.append((combo, t, tp))
    if tp != gconj(t):
        res23.append((combo, t, tp))
print("T3 triples refuting shapes 1,4:", len(res14))
for x in res14[:5]: print("  ", x)
print("T3 triples refuting shapes 2,3:", len(res23))
for x in res23[:5]: print("  ", x)
both = set(c for c, _, _ in res14) & set(c for c, _, _ in res23)
print("triples refuting all four:", len(both))
for c in list(sorted(both))[:10]: print("  ", c)
