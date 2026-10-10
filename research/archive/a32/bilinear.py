"""Exploration only. Search exact Gaussian test pairs separating the single-circle conjugation phi
(conj on the Fourier circle C0, identity elsewhere) from every family member through the
permutation-invariant bilinear form B(G,H) = sum_p mixedTriple G p * mixedTriple H p.
Every family member acts on features as x -> x o s or x -> conj(x o s), s a bijection of the 4096
coordinates, so B(hG,hH) = B(G,H) (shapes 1,4) or conj B(G,H) (shapes 2,3).
Also checks B = tr(K^3), K = sum_i G_i o H_i (Hadamard), against the direct 4096-term sum."""
from fractions import Fraction
import itertools
from circles import R, entry

# Gaussian rationals as (re, im) Fractions
def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])

def gconj(a):
    return (a[0], -a[1])

ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def gpow(z, e):
    if e >= 0:
        r = ONE
        for _ in range(e):
            r = gmul(r, z)
        return r
    return gpow(gconj(z), -e)  # unit z


def tuple_at(r, z):
    """(pi,tau)F(z) as G[i][j][k] Gaussian rationals, z a unit Gaussian rational."""
    pi, tau = R[r]
    G = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                s, e = entry(pi[i], tau[j], tau[k])
                v = gpow(z, e)
                G[i][j][k] = (v[0] * s / 4, v[1] * s / 4)
    return G


def conjT(G):
    return [[[gconj(G[i][j][k]) for k in range(4)] for j in range(4)] for i in range(4)]


def B_trace(G, H):
    K = [[ZERO] * 4 for _ in range(4)]
    for j in range(4):
        for k in range(4):
            acc = ZERO
            for i in range(4):
                acc = gadd(acc, gmul(G[i][j][k], H[i][j][k]))
            K[j][k] = acc
    tr = ZERO
    for a in range(4):
        for b in range(4):
            for c in range(4):
                tr = gadd(tr, gmul(gmul(K[a][b], K[b][c]), K[c][a]))
    return tr


def B_direct(G, H):
    tot = ZERO
    for i1, i2, i3, j1, j2, j3 in itertools.product(range(4), repeat=6):
        x = gmul(gmul(G[i1][j1][j2], G[i2][j2][j3]), G[i3][j3][j1])
        y = gmul(gmul(H[i1][j1][j2], H[i2][j2][j3]), H[i3][j3][j1])
        tot = gadd(tot, gmul(x, y))
    return tot


def phi(r, G):
    return conjT(G) if r == 0 else G


if __name__ == "__main__":
    P = [ONE, I, (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1)), (Fraction(3, 5), Fraction(4, 5))]
    names = ["1", "i", "-1", "-i", "(3+4i)/5"]
    # control: trace formula equals the direct sum on a few pairs
    for (r, z), (s, w) in [((0, I), (4, I)), ((3, P[4]), (7, I)), ((0, P[4]), (0, P[4]))]:
        assert B_trace(tuple_at(r, z), tuple_at(s, w)) == B_direct(tuple_at(r, z), tuple_at(s, w))
    print("trace formula control: ok")
    # (i) shapes 1,4: need B(phiG,phiH) != B(G,H); (ii) shapes 2,3: need != conj B(G,H)
    found_i, found_ii = [], []
    for r, s in itertools.product(range(9), repeat=2):
        for a, b in itertools.product(range(4), repeat=2):
            G, H = tuple_at(r, P[a]), tuple_at(s, P[b])
            B0 = B_trace(G, H)
            B1 = B_trace(phi(r, G), phi(s, H))
            if B1 != B0:
                found_i.append((r, names[a], s, names[b], B0, B1))
            if B1 != gconj(B0):
                found_ii.append((r, names[a], s, names[b], B0, B1))
    print("pairs refuting shapes 1,4 (params in 1,i,-1,-i):", len(found_i))
    for t in found_i[:6]:
        print("  ", t)
    print("pairs refuting shapes 2,3:", len(found_ii))
    for t in found_ii[:6]:
        print("  ", t)
    both = [t for t in found_i if t[:4] in [u[:4] for u in found_ii]]
    print("single pairs refuting all four shapes:", len(both))
    for t in both[:6]:
        print("  ", t)
