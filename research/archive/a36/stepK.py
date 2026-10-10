"""Step J (exact): the outside-hull second-order directions w are straight lines: F(εw) ≡ 0 iff, for every pair (i,j), the
Gaussian-rational sums of c_k over each level set of k ↦ w_ik − w_jk vanish. Verify exactly; build exact points on the line with a
Gaussian-rational unit phase u = (3+4i)/5; run the full relabelled-Diţă orientation search at those points (column and row);
compute the affine family A_w = {w' : Δ' constant on Δ's level sets} through w."""
import pickle, random, time
from lib36 import *
random.seed(3630); t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
F = pickle.load(open('stepF.pkl', 'rb')); hulls = F['hulls']
Def = Tb + Rb
def Bidx(i, j): return list(BB[(min(i, j), max(i, j))])
def Bvec(x, y):
    out = [Fr(0)] * 64
    for i in range(49):
        if x[i] == 0: continue
        for j in range(49):
            if y[j] == 0: continue
            b = Bidx(i, j); c = x[i] * y[j]
            for l in range(64): out[l] += c * b[l]
    return out
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][31:]
def to_vec(x): return [sum(x[i] * Def[i][m] for i in range(49)) for m in range(256)]
T = TDITA; Tc = [T[0]] + T[1:5] + T[9:25]; Tr = [T[0]] + T[5:9] + T[25:41]
Cc = [coords_def(v) for v in Tc]; Cr = [coords_def(v) for v in Tr]
zero = [Fr(0)] * 64
HR = []
for nm, vecs in hulls:
    cs = [coords_def(v) for v in vecs]; cs = [c for c in cs if any(x != 0 for x in c)]
    HR.append((nm,) + tuple(rref(cs, 49)))
def in_hull(x):
    for nm, Rh, ph in HR:
        v = [Fr(c) for c in x]
        for i, p_ in enumerate(ph):
            if v[p_] != 0:
                f = v[p_]; v = [a - f * b for a, b in zip(v, Rh[i])]
        if all(c == 0 for c in v): return nm
    return None
def extension(v):
    for s_ in range(6):
        tc = [Fr(0)] * 49 if s_ == 0 else [sum(random.randint(-2, 2) * x[i] for x in Cc) for i in range(49)]
        vt = [v[i] + tc[i] for i in range(49)]
        rhs = Bvec(v, v); b2 = Bvec(v, tc); rhs = [rhs[l] + 2 * b2[l] for l in range(64)]
        cols = [Bvec(vt, y) for y in Cr]
        M = [[2 * cols[k][l] for k in range(len(Cr))] + [-rhs[l]] for l in range(64)]
        Rm, pv2 = rref(M, len(Cr) + 1)
        if len(Cr) not in pv2:
            x = [Fr(0)] * len(Cr)
            for i_, p_ in enumerate(pv2): x[p_] = Rm[i_][len(Cr)]
            tr = [sum(x[k] * Cr[k][i] for k in range(len(Cr))) for i in range(49)]
            return [vt[i] + tr[i] for i in range(49)]
    return None
def straight_line_exact(w):
    """F(εw) ≡ 0 for all real ε  ⇔  every level-set sum vanishes"""
    for (i, j) in PAIRS:
        sums = {}
        for k in range(16):
            d = w[i * 16 + k] - w[j * 16 + k]
            a, b = C_SIG[(i, j)][k]
            s = sums.get(d, (0, 0)); sums[d] = (s[0] + a, s[1] + b)
        if any(s != (0, 0) for s in sums.values()): return False
    return True
def affine_family(w):
    """A_w = {w' in R^256 : for all pairs (i,j), w'_ik − w'_jk is constant on each level set of w_ik − w_jk}; returns an integer basis"""
    rows = []
    for (i, j) in PAIRS:
        levels = {}
        for k in range(16): levels.setdefault(w[i * 16 + k] - w[j * 16 + k], []).append(k)
        for ks in levels.values():
            for k in ks[1:]:
                r = [0] * 256; r[i * 16 + ks[0]] += 1; r[j * 16 + ks[0]] -= 1; r[i * 16 + k] -= 1; r[j * 16 + k] += 1
                rows.append(r)
    return nullspace(rows, 256) if rows else None
# the orientation search (from step D2), exact
exec(open('stepD2.py', encoding='utf-8').read().split("HT = [list(c)")[0].split("B2 = pickle.load")[0].replace("A = pickle.load(open('stepA.pkl', 'rb')); K, LN = A['K'], A['LN']", ""))
src = open('stepD2.py', encoding='utf-8').read()
fn = src[src.index('def prop_partition'):src.index('HT = [list(c)')]
exec(fn)
U = G(Fr(3, 5), Fr(4, 5))
def upow(n):
    r = ONE
    for _ in range(abs(n)): r = r * (U if n > 0 else U.conj())
    return r
def is_unitary16(H):
    for i in range(16):
        for j in range(16):
            s = ZERO
            for k in range(16): s = s + H[i][k] * H[j][k].conj()
            if s != (G(16) if i == j else ZERO): return False
    return True
def defect_of(H):
    C, den = cvals(H); rows = df_rows(C); return 256 - rank(rows, 256) - 31

def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))          # (n+i)/(n-i), angle 2*atan(1/n)
def gpow(u, n):
    r = ONE
    for _ in range(abs(n)): r = r * (u if n > 0 else u.conj())
    return r
import math
found = None
for si in (2,):
    V = spaces[si]; vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    for trial in range(4):
        v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
        if all(c == 0 for c in v): continue
        w = extension(v)
        if w is None or in_hull(w) is not None: continue
        wv = to_vec(w); den = 1
        for x in wv: den = den * Fr(x).denominator // gcd(den, Fr(x).denominator)
        W = [int(Fr(x) * den) for x in wv]; g = 0
        for x in W: g = gcd(g, abs(x))
        W = [x // g for x in W] if g > 1 else W
        if straight_line_exact(W): found = (si, trial, W); break
    if found: break
si, trial, W = found
nn = 60
"""Step K: Diţă factorizations with factor sizes (m, n), m·n = 16, m in {2, 4, 8}: H[(a,b),(c,d)] = X[a,c] D[c,b] Y_c[b,d], a,c in [m],
b,d in [n]: m column blocks of n columns, n row classes of m rows, rows of a class proportional within each block, rank-one twist,
X (m×m) and every Y_c (n×n) unimodular unitary. Exact, at the certified point and at the new points on the straight line."""
def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
u = unit_n(nn)
P = [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
U5 = G(Fr(3, 5), Fr(4, 5))
P1 = [[SIG[i][j] * gpow(U5, W[i * 16 + j]) for j in range(16)] for i in range(16)]
def is_unitary(M, s):
    k = len(M)
    for i in range(k):
        for j in range(k):
            t = ZERO
            for l in range(k): t = t + M[i][l] * M[j][l].conj()
            if t != (G(s) if i == j else ZERO): return False
    return True
def prop_partition(H, S):
    keys = {}
    for i in range(16):
        base = H[i][S[0]]
        keys.setdefault(tuple((H[i][s] * base.conj()).key() for s in S), []).append(i)
    return sorted(tuple(v) for v in keys.values())
def dita_orientations(H, m, n):
    """all (column blocks, row classes) with the proportionality structure; returns list with exact factorization verdicts"""
    good = {}
    for S in itertools.combinations(range(16), n):
        Pp = prop_partition(H, S)
        if all(len(cl) == m for cl in Pp): good[S] = Pp
    parts = []
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for S in good:
            if first in S and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(set(range(16)), [])
    out = []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[S]) if i in cl) for S in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if not all(len(g) == m for g in rows): continue
        # factorization
        col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}
        row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
        lam = {}; Y = []
        for c in range(m):
            Yc = []
            for b in range(n):
                i0 = row[(0, b)]; base = [H[i0][col[(c, d)]] for d in range(n)]; Yc.append(base)
                for a in range(m): lam[(a, b, c)] = H[row[(a, b)]][col[(c, 0)]] * base[0].conj()
            Y.append(Yc)
        rank1 = all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(m) for b in range(n) for c in range(m))
        X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]
        okX = is_unitary(X, m); okY = all(is_unitary(Yc, n) for Yc in Y)
        out.append((cp, rows, rank1 and okX and okY, (rank1, okX, okY)))
    return len(good), out
for label, H in (('SIG (certified point)', SIG), ('P (near point, u=(60+i)/(60-i))', P), ('P_1 (u=(3+4i)/5)', P1)):
    print('==', label, 'Hadamard:', is_unitary(H, 16))
    HT = [list(c) for c in zip(*H)]
    for (m, n) in ((2, 8), (8, 2), (4, 4)):
        for kind, HH in (('column', H), ('row', HT)):
            ng, ors = dita_orientations(HH, m, n)
            print('   %s-Diţă %dx%d: admissible column %d-blocks %d | orientations %d | exact factorizations %d %s' % (kind, m, n, n, ng, len(ors), sum(1 for o in ors if o[2]), [o[3] for o in ors if not o[2]][:3]))
    print('   (%.0fs)' % (time.time() - t0))
# is the 4x4 pattern of W the circle direction of F4(w) modulo gauge?
M = [[W[(0 * 4 + b) * 16 + (0 * 4 + d)] for d in range(4)] for b in range(4)]
G4 = []
for i in range(4):
    v = [0] * 16
    for k in range(4): v[i * 4 + k] = 1
    G4.append(v)
for k in range(4):
    v = [0] * 16
    for i in range(4): v[i * 4 + k] = 1
    G4.append(v)
ex = [1 if (b % 2 == 1 and d % 2 == 1) else 0 for b in range(4) for d in range(4)]
Mf = [M[b][d] for b in range(4) for d in range(4)]
print('4x4 pattern M in the even-even blocks; rank(G4 + ex) = %d, rank(G4 + ex + M) = %d -> M is gauge + circle direction: %s' % (rank(G4 + [ex], 16), rank(G4 + [ex, Mf], 16), rank(G4 + [ex, Mf], 16) == rank(G4 + [ex], 16)))
print('done (%.0fs)' % (time.time() - t0))
