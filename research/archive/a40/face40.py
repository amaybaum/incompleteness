"""Explicit whole-face Dita factorizations of H3 on the five faces, built and checked in the exact monomial calculus.
A monomial is (k, c): u^k * i^p z^q w^r with k = (k1, k2, k3) and c = (p mod 4, q, r); 4 H3[i][j] = (K[i][j], SIGE[i][j])."""
import itertools
from named40 import SIGE, EA, EB, EC, CLASSES, M_COL, M_ROW, NAMED
def madd(x, y): return (tuple(a + b for a, b in zip(x[0], y[0])), ((x[1][0] + y[1][0]) % 4, x[1][1] + y[1][1], x[1][2] + y[1][2]))
def mneg(x): return (tuple(-a for a in x[0]), ((-x[1][0]) % 4, -x[1][1], -x[1][2]))
def msub(x, y): return madd(x, mneg(y))
K = [[(EA(i, j), EB(i, j), EC(i, j)) for j in range(16)] for i in range(16)]
PHI = [[(K[i][j], SIGE[i][j]) for j in range(16)] for i in range(16)]
FACES = {  # face: (coordinate, value in {1,-1}), structure name, orientation
 'u1=+1': (0, 0, 't2', 'column'), 'u1=-1': (0, 2, 'M_COL', 'column'), 'u2=+1': (1, 0, 't1', 'column'),
 'u3=+1': (2, 0, 't1', 'row'), 'u3=-1': (2, 2, 'M_ROW', 'row')}
def on_face(x, coord, p):
    """substitute u_coord = i^p (p = 0 for 1, 2 for -1)"""
    k, (a, q, r) = x
    kk = list(k); e = kk[coord]; kk[coord] = 0
    return (tuple(kk), ((a + p * e) % 4, q, r))
def struct(nm, form):
    for n_, f, mn, cp, rows in NAMED:
        if n_ == nm and f == form: return mn, cp, rows
def build(face):
    coord, p, nm, form = FACES[face]
    (m, n), cp, rows = struct(nm, form)
    M = PHI if form == 'column' else [list(c) for c in zip(*PHI)]
    F = [[on_face(M[i][j], coord, p) for j in range(16)] for i in range(16)]
    # index maps: row i -> (a, b) = (position in class, class); column j -> (c, d) = (block, position in block)
    rmap = {i: (cl.index(i), b) for b, cl in enumerate(rows) for i in cl}
    cmap = {j: (c, bl.index(j)) for c, bl in enumerate(cp) for j in bl}
    rinv = {v: k for k, v in rmap.items()}; cinv = {v: k for k, v in cmap.items()}
    # X (the ratio to the class representative), Y (representative rows), D = -i
    X = {}
    ok = True
    for a in range(m):
        for c in range(m):
            vals = set(msub(F[rinv[(a, b)]][cinv[(c, d)]], F[rinv[(0, b)]][cinv[(c, d)]]) for b in range(n) for d in range(n))
            if len(vals) != 1: ok = False
            X[(a, c)] = sorted(vals)[0]
    Y = {(c, b, d): F[rinv[(0, b)]][cinv[(c, d)]] for c in range(m) for b in range(n) for d in range(n)}
    # identity: F[i][j] == X[a,c] + Y[c,b,d] (monomials multiply = add)
    ident = all(F[i][j] == madd(X[(rmap[i][0], cmap[j][0])], Y[(cmap[j][0], rmap[i][1], cmap[j][1])]) for i in range(16) for j in range(16))
    return dict(face=face, nm=nm, form=form, m=m, n=n, cp=cp, rows=rows, rmap=rmap, cmap=cmap, X=X, Y=Y, ratio_ok=ok, ident=ident, F=F)
def unitary_levelsets(entries, size):
    """entries[(r, s)] monomials of a size x size matrix; checks sum_s e[r,s] conj e[r',s] = size * delta, level set by level set
    in the u-exponents and monomial by monomial in z, w (exact, symbolic units)"""
    bad = 0; nsets = 0
    for r in range(size):
        for r2 in range(size):
            groups = {}
            for s in range(size):
                x = msub(entries[(r, s)], entries[(r2, s)])
                groups.setdefault(x[0], {}).setdefault((x[1][1], x[1][2]), 0)
                groups[x[0]][(x[1][1], x[1][2])] += {0: 1, 2: -1}.get(x[1][0], None) if x[1][0] in (0, 2) else 10**6
            for k, cnt in groups.items():
                nsets += 1
                want = {(0, 0): size} if (r == r2 and not any(k)) else {}
                got = {kk: v for kk, v in cnt.items() if v}
                if got != want: bad += 1
    return nsets, bad
if __name__ == '__main__':
    for face in FACES:
        B = build(face)
        yu = [unitary_levelsets({(b, d): B['Y'][(c, b, d)] for b in range(B['n']) for d in range(B['n'])}, B['n']) for c in range(B['m'])]
        xu = unitary_levelsets({(a, c): B['X'][(a, c)] for a in range(B['m']) for c in range(B['m'])}, B['m'])
        free = sorted(set(k for x in list(B['X'].values()) + list(B['Y'].values()) for k in [x[0]]))
        print(face, B['nm'], B['form'], 'ratio independent', B['ratio_ok'], 'identity', B['ident'], '| Y unitary (sets, bad)', yu, '| X unitary', xu)
        print('   X =', {k: v for k, v in B['X'].items()})
        print('   u-exponents occurring in X, Y:', free)
