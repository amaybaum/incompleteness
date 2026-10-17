"""Independent exact check of the decisive witnesses.  Shares no code with qexact.py / hvalid_search.py:
complex matrices are realified (a + ib -> [[a,-b],[b,a]]), PSD is tested by an LDL^T elimination on the real
symmetric realification, and product-test values are computed only by the trace route on matrices.
Same author as the search; the independence is of code and arithmetic path, not of construction."""
from fractions import Fraction as F
from itertools import product

def cplx(re, im=0): return (F(re), F(im))
def cm(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def ca(a, b): return (a[0] + b[0], a[1] + b[1])
def cc(a): return (a[0], -a[1])
Z0 = (F(0), F(0))

def mat(rows): return [[cplx(*e) if isinstance(e, tuple) else cplx(e) for e in r] for r in rows]
def mul(A, B):
    return [[ (lambda i, j: __import__('functools').reduce(ca, (cm(A[i][t], B[t][j]) for t in range(len(B))), Z0))(i, j)
              for j in range(len(B[0]))] for i in range(len(A))]
def H_(A): return [[cc(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def kr(A, B):
    n, m = len(A), len(B)
    return [[cm(A[i // m][j // m], B[i % m][j % m]) for j in range(n*m)] for i in range(n*m)]
def trace(A):
    t = Z0
    for i in range(len(A)): t = ca(t, A[i][i])
    return t
def scal(c, A): return [[cm(cplx(c) if not isinstance(c, tuple) else c, x) for x in r] for r in A]
def add(A, B): return [[ca(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
def realify(A):
    n = len(A); R = [[F(0)]*(2*n) for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            a, b = A[i][j]
            R[i][j] = a; R[i][j+n] = -b; R[i+n][j] = b; R[i+n][j+n] = a
    return R
def psd_ldl(S):
    """Real symmetric PSD test by LDL^T with symmetric pivoting on the largest diagonal."""
    n = len(S); M = [r[:] for r in S]; idx = list(range(n))
    while idx:
        d = {i: M[i][i] for i in idx}
        if min(d.values()) < 0: return False
        p = max(idx, key=lambda i: M[i][i])
        if M[p][p] == 0:
            return all(M[i][j] == 0 for i in idx for j in idx)
        idx.remove(p)
        for i in idx:
            f = M[i][p] / M[p][p]
            for j in idx: M[i][j] -= f * M[p][j]
    return True
def psd(A): return psd_ldl(realify(A))

I2 = mat([[1, 0], [0, 1]]); X = mat([[0, 1], [1, 0]]); Y = mat([[0, (0, -1)], [(0, 1), 0]]); Zm = mat([[1, 0], [0, -1]])
PA = [I2, X, Y, Zm]
def Pi(a): return add(scal(F(1, 2), I2), add(scal(F(a[0], 2), X), add(scal(F(a[1], 2), Y), scal(F(a[2], 2), Zm))))
def val(H, a, b):
    t = trace(mul(kr(Pi(a), Pi(b)), H)); assert t[1] == 0; return t[0]
def tr_B(H): return [[ca(H[2*a][2*b], H[2*a+1][2*b+1]) for b in range(2)] for a in range(2)]
def tr_A(H): return [[ca(H[a][b], H[2+a][2+b]) for b in range(2)] for a in range(2)]

out = []
def rec(code, ok, info=""): out.append(ok); print(("ok  " if ok else "FAIL") + f" {code} {info}")

# I1  the K2 witness diag(-1,1,1,1): value of the z3 (x) z3 sharp test, marginals
Hst = mat([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
z = (0, 0, 1)
rec("I1a", val(Hst, z, z) == -1, f"tr((Π_z⊗Π_z)·diag(-1,1,1,1)) = {val(Hst, z, z)}")
rec("I1b", psd(tr_B(Hst)) and psd(tr_A(Hst)) and not psd(Hst), "both marginals PSD (diag(0,2)), the matrix itself not PSD")
# I1c  Ky Fan bound route: for every pair of orthonormal basis vectors the diagonal sum is >= 0 (A2 of a diagonal)
d = [-1, 1, 1, 1]
rec("I1c", min(d[i] + d[j] for i in range(4) for j in range(4) if i < j) == 0, "λ1+λ2 = 0 for diag(-1,1,1,1)")

# I2  the K(Z_F) defect e_(1,1) = (I + X⊗Z + Y⊗Y - Z⊗X)/16 and its Bell-type eigenbasis
e11 = scal(F(1, 16), add(kr(I2, I2), add(kr(X, Zm), add(kr(Y, Y), scal(-1, kr(Zm, X))))))
# eigenvectors written independently from the stabilizer generators X⊗Z, Y⊗Y (joint eigenvalues a, b):
# value of s X⊗Z + t Y⊗Y - st Z⊗X at s=t=1 is a + b - ab; the -3 eigenvector has a = b = -1.
XZ, YY = kr(X, Zm), kr(Y, Y)
basis = [cplx(0)]*4
found = {}
for v in product([cplx(0), cplx(1), cplx(-1), cplx(0, 1), cplx(0, -1)], repeat=4):
    if all(x == Z0 for x in v): continue
    col = [[x] for x in v]
    a = mul(XZ, col); b = mul(YY, col)
    for sa, sb in product((1, -1), repeat=2):
        if all(a[i][0] == cm(cplx(sa), v[i]) for i in range(4)) and all(b[i][0] == cm(cplx(sb), v[i]) for i in range(4)):
            found.setdefault((sa, sb), v)
rec("I2a", len(found) == 4, f"joint eigenvectors of X⊗Z and Y⊗Y found for sign pairs {sorted(found)}")
ok = True
for (sa, sb), v in found.items():
    lam = F(1 + sa + sb - sa*sb, 16)
    ev = mul(e11, [[x] for x in v])
    ok &= all(ev[i][0] == cm(cplx(lam), v[i]) for i in range(4))
rec("I2b", ok, "e_(1,1) v = (1 + a + b - ab)/16 · v on each: eigenvalues -2/16 once, 2/16 three times")
# unitary V whose first row is the normalized -1/8 eigenvector (conjugated), the rest the others
order = [(-1, -1)] + [k for k in sorted(found) if k != (-1, -1)]
rows = []
for k in order:
    v = found[k]; n2 = sum(x[0]**2 + x[1]**2 for x in v)
    s = {1: 1, 4: 2, 9: 3, 16: 4}.get(int(n2)) if n2.denominator == 1 else None
    rows.append([cc((x[0]/s, x[1]/s)) for x in v])
V = rows
rec("I2c", mul(V, H_(V)) == [[cplx(1 if i == j else 0) for j in range(4)] for i in range(4)], "V is exactly unitary")
VeV = mul(mul(V, e11), H_(V))
rec("I2d", val(VeV, z, z) == F(-1, 8) and psd(tr_B(VeV)) and psd(tr_A(VeV)),
    f"(V e V†): z3⊗z3 sharp value {val(VeV, z, z)}, both marginals PSD")
grid = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (F(3, 5), F(4, 5), 0), (0, F(-4, 5), F(3, 5))]
rec("I2e", all(val(e11, a, b) >= 0 for a in grid for b in grid), "e_(1,1) itself is nonnegative on an 8×8 sharp grid")

# I3  CM-4: I + 2 X⊗X
Hx = add(kr(I2, I2), scal(2, kr(X, X)))
stage_ok = all(val(Hx, (0, 0, s), (0, 0, t)) >= 0 for s in (1, -1) for t in (1, -1))
rec("I3", stage_ok and val(Hx, (1, 0, 0), (-1, 0, 0)) == -1 and psd(tr_B(Hx)) and psd(tr_A(Hx)),
    f"z-stage products ≥ 0, marginals PSD, x⊗(-x) value {val(Hx, (1, 0, 0), (-1, 0, 0))}")

# I4  FCC on 16×16 matrices: F10 and the uniform-K2 violation, by the trace route only
def reorder(M):
    def ix(b): return b[0]*8 + b[1]*4 + b[2]*2 + b[3]
    R = [[Z0]*16 for _ in range(16)]
    for r in product((0, 1), repeat=4):
        for c in product((0, 1), repeat=4):
            R[ix(r)][ix(c)] = M[ix((r[0], r[2], r[1], r[3]))][ix((c[0], c[2], c[1], c[3]))]
    return R
def fcc_value(rhoX, rhoY, effE, effF):
    t = trace(mul(reorder(kr(effE, effF)), kr(rhoX, rhoY))); assert t[1] == 0
    return 16 * t[0]   # famI in table units = 16 · trace (independent normalization: see the search's S5.X)
bell = scal(F(1, 4), add(kr(I2, I2), add(kr(X, X), add(scal(-1, kr(Y, Y)), kr(Zm, Zm)))))   # dict phiW
E_bell = scal(F(1, 4), bell)           # dict (phiW/4)
F_tw = scal(F(1, 16), add(kr(I2, I2), add(scal(-1, kr(X, X)), add(kr(Y, Y), scal(-1, kr(Zm, Zm))))))  # dict diag(1,-1,1,-1)/4
rec("I4a", fcc_value(bell, bell, E_bell, F_tw) == F(-1, 8), f"F10 = {fcc_value(bell, bell, E_bell, F_tw)}")
P00 = mat([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])           # dict prodState z3 z3
Ezu = scal(F(1, 4), kr(Pi(z), I2))                                             # dict of the table ẑ ⊗ û = Π_z ⊗ I / 4
rec("I4b", fcc_value(Hst, P00, Ezu, Ezu) == -1, f"uniform-K2 FCC violation = {fcc_value(Hst, P00, Ezu, Ezu)}")

print(f"FINAL: {len(out)} exact checks, {out.count(False)} failed")
