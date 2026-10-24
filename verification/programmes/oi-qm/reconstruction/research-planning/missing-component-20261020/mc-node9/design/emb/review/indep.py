"""Independent reviewer engine (no import from the reviewed scripts).  Exact F2 bitmask algebra.
Coordinates: u_x = bit x, v_x = bit n+x.  A linear map is a list of row masks (row i = output
coordinate i as a functional of the inputs).  Heisenberg picture: rows of Phi = M_t ... M_1.
"""
import random
from itertools import combinations, product, permutations


def rk(rows):
    basis = {}
    r = 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in basis:
                v ^= basis[h]
            else:
                basis[h] = v
                r += 1
                break
    return r


def mul(A, B):
    """(A B) rows: row_i(A) combined over rows of B (apply B first)."""
    out = []
    for a in A:
        r = 0
        j = 0
        while a:
            if a & 1:
                r ^= B[j]
            a >>= 1
            j += 1
        out.append(r)
    return out


def ident(N):
    return [1 << i for i in range(N)]


def upd(n, L):
    """L: list of n row masks of a symmetric F2 matrix (diagonal allowed = self-loop).
    u'_x = sum_z L_xz u_z + v_x ; v'_x = u_x."""
    rows = [0] * (2 * n)
    for x in range(n):
        rows[x] = L[x] | (1 << (n + x))
        rows[n + x] = 1 << x
    return rows


def adj_from_edges(n, edges, xor=True):
    L = [0] * n
    for a, b in edges:
        if a == b:
            L[a] ^= 1 << a
        else:
            L[a] ^= 1 << b
            L[b] ^= 1 << a
    return L


def om(a, b, n):
    m = (1 << n) - 1
    return (bin((a & m) & (b >> n)).count("1") + bin((a >> n) & (b & m)).count("1")) & 1


def is_symp(P, n):
    N = 2 * n
    for i in range(N):
        for j in range(N):
            if om(P[i], P[j], n) != (1 if abs(i - j) == n else 0):
                return False
    return True


def support_exp(F, T, um):
    Fu = [f & um for f in F]
    return rk(Fu + [t & um for t in T]) - rk(Fu)


def prior_exp(T, um):
    return rk([t & um for t in T])


def period(M):
    N = len(M)
    I = ident(N)
    P = M
    k = 1
    while P != I:
        P = mul(M, P)
        k += 1
        if k > 10 ** 5:
            raise RuntimeError
    return k


def apply(T, s):
    out = 0
    for i, r in enumerate(T):
        if bin(r & s).count("1") & 1:
            out |= 1 << i
    return out


def step_state(n, L, s):
    """Forward simulation of one update directly from the defining equations (no matrix)."""
    u = [(s >> x) & 1 for x in range(n)]
    v = [(s >> (n + x)) & 1 for x in range(n)]
    nu = [(sum(u[z] for z in range(n) if (L[x] >> z) & 1) + v[x]) & 1 for x in range(n)]
    nv = u[:]
    out = 0
    for x in range(n):
        out |= nu[x] << x
        out |= nv[x] << (n + x)
    return out
