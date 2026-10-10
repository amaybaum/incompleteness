"""A36 pre-freeze measurement library: exact objects at the certified rational stratum point, from D36's frozen probe.
All arithmetic is exact (Python ints / Fractions, Gaussian rationals); numpy appears only in the float controls."""
import re, sys, os, itertools
from fractions import Fraction as Fr
from math import gcd
S = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(S, 'probe_d36.py'), encoding='utf-8').read()
head = src[:src.index("print('== 1.")]
sec1 = src[src.index("print('== 1."):src.index("print('== 2.")]
defs = '\n'.join(l for l in sec1.split('\n') if re.match(r'^[A-Za-z_][A-Za-z0-9_]* = ', l) and 'check(' not in l)
ns = {}; exec(head + '\n' + defs, ns)
G, ONE, ZERO, I_, F4, circle, dita, kron, unitD = (ns[k] for k in ('G', 'ONE', 'ZERO', 'I_', 'F4', 'circle', 'dita', 'kron', 'unitD'))
ID4, R = ns['ID4'], ns['R']
SIG = ns['SIG']            # kron(F4(z), F4(w)), z = (3+4i)/5, w = (5+12i)/13, scaled by 4 (unimodular entries)
z, w = ns['z'], ns['w']
N = 16
PAIRS = [(i, j) for i in range(N) for j in range(i + 1, N)]     # 120 constraint pairs, in the probe's order
# c^{ij}_k = H_ik conj(H_jk), scaled to Gaussian integers by the common denominator
def cvals(H):
    C = {}
    den = 1
    for (i, j) in PAIRS:
        for k in range(N):
            c = H[i][k] * H[j][k].conj()
            for x in (c.a, c.b): den = den * x.denominator // gcd(den, x.denominator)
    for (i, j) in PAIRS:
        C[(i, j)] = [(int(c.a * den), int(c.b * den)) for c in (H[i][k] * H[j][k].conj() for k in range(N))]
    return C, den
C_SIG, DEN = cvals(SIG)

def df_rows(C):
    """the 240 integer rows of DF: for each pair (i,j), Re and Im of  i * sum_k c_k (th_ik - th_jk)  ->  Re: -sum c.b(...), Im: sum c.a(...)"""
    rows = []
    for (i, j) in PAIRS:
        re = [0] * (N * N); im = [0] * (N * N)
        for k, (a, b) in enumerate(C[(i, j)]):
            re[i * N + k] -= b; re[j * N + k] += b
            im[i * N + k] += a; im[j * N + k] -= a
        rows.append(re); rows.append(im)
    return rows
DF = df_rows(C_SIG)

# ---- exact linear algebra over Q (Fraction rref) -------------------------------------------------------
def rref(rows, ncols):
    M = [[Fr(x) for x in r] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    return M[:r], piv
def rank(rows, ncols=None):
    if not rows: return 0
    return len(rref(rows, ncols or len(rows[0]))[0])
def nullspace(rows, ncols):
    """integer basis of {x : rows . x = 0}"""
    Rr, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)] * ncols; v[f] = Fr(1)
        for i, p in enumerate(piv): v[p] = -Rr[i][f]
        out.append(intvec(v))
    return out
def intvec(v):
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    w = [int(x * den) for x in v]; g = 0
    for x in w: g = gcd(g, abs(x))
    return [x // g for x in w] if g > 1 else w
def transpose(rows): return [list(c) for c in zip(*rows)]
def dot(u, v): return sum(a * b for a, b in zip(u, v))

# ---- the gauge and the fixed-pairing Diţă tangents (as in the frozen probe) -----------------------------
def flat(v): return [x for r in v for x in r]
def gauge_vecs():
    out = []
    for i in range(16):
        v = [0] * 256
        for k in range(16): v[i * 16 + k] = 1
        out.append(v)
    for k in range(16):
        v = [0] * 256
        for i in range(16): v[i * 16 + k] = 1
        out.append(v)
    return out
def expo(pi, tau): return [[1 if (pi[a] % 2 == 1 and tau[c] % 2 == 1) else 0 for c in range(4)] for a in range(4)]
EX = expo(ID4, ID4)
def dita_tangents():
    """the 41 directions of the two fixed-pairing hulls at the Σ point: X on its circle, Y_c on theirs (column hull),
    Y_a on theirs (row hull), the column twists D[c][b] and the row twists E[a][d]"""
    vecs = []
    vecs.append(flat([[EX[i // 4][j // 4] for j in range(16)] for i in range(16)]))
    for c in range(4): vecs.append(flat([[EX[i % 4][j % 4] if j // 4 == c else 0 for j in range(16)] for i in range(16)]))
    for a in range(4): vecs.append(flat([[EX[i % 4][j % 4] if i // 4 == a else 0 for j in range(16)] for i in range(16)]))
    for c in range(4):
        for b in range(4): vecs.append(flat([[1 if (j // 4 == c and i % 4 == b) else 0 for j in range(16)] for i in range(16)]))
    for a in range(4):
        for d in range(4): vecs.append(flat([[1 if (i // 4 == a and j % 4 == d) else 0 for j in range(16)] for i in range(16)]))
    return vecs
GAUGE = gauge_vecs()
TDITA = dita_tangents()
