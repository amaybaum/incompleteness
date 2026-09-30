"""R2 path B(i): an independent enumeration of every realizing triple of SIG, and the exact identity test.

Imports nothing from the landed probes. SIG is built here from its definition (F4(z) (x) F4(w), z = (3+4i)/5,
w = (5+12i)/13, index (a,b) -> 4a+b) in exact Gaussian rationals.

A triple is (orientation, shape (m, n), m column blocks of n columns, n row classes of m rows, an alignment); in the row
orientation the same on the transpose. With row(a, b) the row of class b carrying label a and col(c, d) the column d of
block c, a matrix H with unimodular entries is Dita for the triple up to diagonal equivalence iff
  (i)  the rows of each class are proportional on each block, and
  (ii) with lam(a, b, c) = H[row(a,b)][col(c,0)] / H[row(0,b)][col(c,0)]:  lam(a,b,c) lam(a,b,0)^-1 = lam(a,0,c) lam(a,0,0)^-1.
For H(u) = SIG o u^E these hold for every unit u iff they hold for SIG and the exponent identities hold for E: the
additive forms of (i) and (ii) on E. `identity_eqs` returns those forms; `member(E, t)` tests them exactly.
"""
import itertools
from fractions import Fraction as Fr

# ---- exact Gaussian rationals as pairs ----------------------------------------------------------------------
def gm(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def gc(x): return (x[0], -x[1])
ONE, M1 = (Fr(1), Fr(0)), (Fr(-1), Fr(0))
def gneg(x): return (-x[0], -x[1])
z = (Fr(3, 5), Fr(4, 5)); w = (Fr(5, 13), Fr(12, 13))
def F4(t): return [[ONE, ONE, ONE, ONE], [ONE, t, M1, gneg(t)], [ONE, M1, ONE, M1], [ONE, gneg(t), M1, t]]
FZ, FW = F4(z), F4(w)
SIG = [[gm(FZ[i // 4][j // 4], FW[i % 4][j % 4]) for j in range(16)] for i in range(16)]
SIGT = [list(c) for c in zip(*SIG)]
def rat(x, y): return gm(x, gc(y))          # x / y for unimodular y

def partitions(M, m, n):
    """every (blocks, classes) with (i): m disjoint n-column blocks covering the columns, n row classes of m rows each
    proportional on every block"""
    usable = {}
    for S in itertools.combinations(range(16), n):
        keys = {}
        for r in range(16): keys.setdefault(tuple(rat(M[r][s], M[r][S[0]]) for s in S), []).append(r)
        if all(len(v) % m == 0 for v in keys.values()): usable[S] = [tuple(v) for v in keys.values()]
    covers = []
    def rec(rem, chosen):
        if not rem: covers.append(tuple(chosen)); return
        f = min(rem)
        for S in usable:
            if S[0] == f and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(frozenset(range(16)), [])
    out = []
    for blocks in covers:
        lab = {r: tuple(next(k for k, cl in enumerate(usable[S]) if r in cl) for S in blocks) for r in range(16)}
        meet = {}
        for r in range(16): meet.setdefault(lab[r], []).append(r)
        meet = [tuple(v) for v in meet.values()]
        if any(len(v) % m for v in meet): continue
        def split(cls):
            if not cls: yield []; return
            first, rest = cls[0][0], cls[0][1:]
            for grp in itertools.combinations(rest, m - 1):
                left = tuple(x for x in rest if x not in grp)
                for tail in split(([left] if left else []) + cls[1:]): yield [(first,) + grp] + tail
        for classes in split(sorted(meet)):
            out.append((tuple(sorted(blocks)), tuple(sorted(classes))))
    return out

def alignments(M, m, n, blocks, classes):
    """every alignment satisfying (ii): per class b >= 1, the bijections sigma_b: labels -> rows of class b (class 0
    labelled in sorted order) with lam(a,b,c)/lam(a,b,0) = lam(a,0,c)/lam(a,0,0); returns the list of threads-sets"""
    c0 = [B[0] for B in blocks]; R0 = sorted(classes[0])
    def lam(r, r0, c): return rat(M[r][c0[c]], M[r0][c0[c]])
    ref = [[rat(lam(R0[a], R0[0], c), lam(R0[a], R0[0], 0)) for c in range(m)] for a in range(m)]
    per = []
    for cl in classes[1:]:
        ok = []
        for sig in itertools.permutations(sorted(cl)):
            if all(rat(lam(sig[a], sig[0], c), lam(sig[a], sig[0], 0)) == ref[a][c] for a in range(m) for c in range(1, m)): ok.append(sig)
        per.append(ok)
    out = []
    for combo in itertools.product(*per):
        out.append(tuple(tuple([R0[a]] + [s[a] for s in combo]) for a in range(m)))
    return out, [len(p) for p in per]

def census():
    """{(form, (m, n), blocks, classes): [threads, ...]} over both orientations and the three shapes"""
    res = {}
    for form, M in (('column', SIG), ('row', SIGT)):
        for m, n in ((4, 4), (8, 2), (2, 8)):
            for blocks, classes in partitions(M, m, n):
                al, _ = alignments(M, m, n, blocks, classes)
                if al: res[(form, (m, n), blocks, classes)] = al
    return res

def identity_eqs(key, threads):
    """the exponent identities of (i) and (ii) for the triple, as lists of (coef, (row, col)) over the 256 positions of
    the orientation's matrix (row orientation: positions of the transpose, mapped back to E's (row, col))"""
    form, (m, n), blocks, classes = key
    def pos(r, c): return (r, c) if form == 'column' else (c, r)
    eqs = []
    for cl in classes:
        r0 = cl[0]
        for B in blocks:
            j0 = B[0]
            for r in cl[1:]:
                for j in B[1:]: eqs.append([(1, pos(r, j)), (-1, pos(r0, j)), (-1, pos(r, j0)), (1, pos(r0, j0))])
    c0 = [B[0] for B in blocks]
    # threads[a] = (row of class 0 with label a, row of class 1 with label a, ...), classes ordered as in `classes`
    row = {(a, b): threads[a][b] for a in range(m) for b in range(n)}
    def lam(a, b, c): return [(1, pos(row[(a, b)], c0[c])), (-1, pos(row[(0, b)], c0[c]))]
    for a in range(m):
        for b in range(1, n):
            for c in range(1, m):
                eq = lam(a, b, c) + [(-k, p) for k, p in lam(a, b, 0)] + [(-k, p) for k, p in lam(a, 0, c)] + lam(a, 0, 0)
                eqs.append(eq)
    return eqs

def member(E, key, threads):
    return all(sum(k * E[p[0]][p[1]] for k, p in eq) == 0 for eq in identity_eqs(key, threads))

def gauge_generators():
    out = []
    for i in range(16): out.append([[1 if r == i else 0 for c in range(16)] for r in range(16)])
    for j in range(16): out.append([[1 if c == j else 0 for c in range(16)] for r in range(16)])
    return out
