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
print('direction W (sector %d trial %d), integer 16x16 (rows (a,b) = 4a+b, columns (c,d) = 4c+d):' % (si, trial))
for i in range(16): print('   ', ' '.join('%3d' % W[i * 16 + j] for j in range(16)))
# reduce W modulo gauge to a canonical form: subtract row constants and column constants (first column / first row)
Wm = [[W[i * 16 + j] - W[i * 16] for j in range(16)] for i in range(16)]
Wm = [[Wm[i][j] - Wm[0][j] for j in range(16)] for i in range(16)]
print('W dephased (row 0 and column 0 removed):')
for i in range(16): print('   ', ' '.join('%3d' % Wm[i][j] for j in range(16)))
Aw = affine_family(W)
print('affine family A_w: dim %d, mod gauge %d' % (len(Aw), rank(GAUGE + Aw) - 31))
for nm, S in (('T_c', Tc), ('T_r', Tr)):
    print('   dim(A_w ∩ %s) mod gauge: %d' % (nm, (rank(GAUGE + Aw) - 31) + (rank(GAUGE + S) - 31) - (rank(GAUGE + Aw + S) - 31)))
famspans = {}
for nm, vecs in hulls: famspans.setdefault(nm, []).extend(vecs)
for nm, S in famspans.items():
    d = (rank(GAUGE + Aw) - 31) + (rank(GAUGE + S) - 31) - (rank(GAUGE + Aw + S) - 31)
    print('   dim(A_w ∩ span of %s hulls) mod gauge: %d' % (nm, d))
# a near exact point: u = (n+i)/(n-i), n = 60: angle 2*atan(1/60) = 1.9°, times max|W| entries
n = 60; u = unit_n(n); ang = 2 * math.atan(1 / n) * 180 / math.pi
P = [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
print('near point P = SIG ∘ u^W with u = (%d+i)/(%d-i): max phase angle %.1f°, Hadamard exactly: %s' % (n, n, ang * max(abs(x) for x in W), is_unitary16(P)))
print('   defect of P: %d' % defect_of(P))
PT = [list(c) for c in zip(*P)]
for kind, H_, tr in (('column', P, False), ('row', PT, True)):
    ors = orientations_of(H_); oks = []
    for cp, rows_ in ors:
        try: okf, _, flags = factor_and_tangent(H_, cp, rows_, transposed=tr); oks.append(okf)
        except AssertionError: oks.append(False)
    print('   relabelled %s-Diţă orientations through P: candidates %d, exact factorizations %d' % (kind, len(ors), sum(oks)))
# the A35 membership signature at P for the fixed pairing (cross ratios rows (a,b),(a,b') cols (c,d),(c',d) equal 1): count violations
viol = 0
for a in range(4):
    for b in range(4):
        for b2 in range(b + 1, 4):
            for c in range(4):
                for c2 in range(c + 1, 4):
                    for d in range(4):
                        i1, i2, j1, j2 = 4 * a + b, 4 * a + b2, 4 * c + d, 4 * c2 + d
                        if P[i1][j1] * P[i2][j2] != P[i1][j2] * P[i2][j1]: viol += 1
print('   fixed-pairing cross-ratio identity violations at P: %d of %d' % (viol, 4 * 6 * 6 * 4))
pickle.dump({'W': W, 'n': n}, open('stepJ2.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
