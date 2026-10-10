#!/usr/bin/env python3
"""REL-C probe (read-only research thread; nothing here is adopted, frozen or governed).

Exact arithmetic only (fractions.Fraction, sympy rationals).  Conventions follow
OIBridge/CompositeDimension.lean at L = e2426ba4:
  * W d  : (d+1)x(d+1) arrays w[mu][nu], mu = control index, nu = target index;
  * hom x = (1, x);  homMap N = diag(1, N);
  * actT N w : row mu -> homMap N (w[mu])          (= w H^T, "R_H")
  * actC N w : column nu -> homMap N (w[.][nu])    (= H w,   "L_H")
  * prodState x y = hom x (x) hom y;  pairVal a b w = a^T w b;
  * relT : actT N (G (actT N w)) = G w
  * relC : actC N (G (actC N w)) = actT N (G w)
Every verdict line is generated from measurements and printed only if all controls of its
section are green.
"""
from fractions import Fraction as Fr
import itertools, random, sys

random.seed(20261007)
FAIL = []


def check(name, cond):
    print(("  PASS  " if cond else "  FAIL  ") + name)
    if not cond:
        FAIL.append(name)
    return cond

# ----------------------------------------------------------------------------- linear algebra


def zeros(n, m=None):
    m = n if m is None else m
    return [[Fr(0)] * m for _ in range(n)]


def eye(n):
    A = zeros(n)
    for i in range(n):
        A[i][i] = Fr(1)
    return A


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                Ci = C[i]
                for j in range(m):
                    if Bt[j]:
                        Ci[j] += a * Bt[j]
    return C


def transpose(A):
    return [list(r) for r in zip(*A)]


def rref(A):
    """Exact reduced row echelon form; returns (R, pivots)."""
    R = [list(r) for r in A]
    rows, cols = len(R), len(R[0]) if R else 0
    piv, r = [], 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if R[i][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        inv = 1 / R[r][c]
        R[r] = [x * inv for x in R[r]]
        for i in range(rows):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [x - f * y for x, y in zip(R[i], R[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return R, piv


def rank(A):
    return len(rref(A)[1])


def nullspace(A):
    R, piv = rref(A)
    cols = len(A[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * cols
        v[f] = Fr(1)
        for i, p in enumerate(piv):
            v[p] = -R[i][f]
        basis.append(v)
    return basis


def inverse(A):
    n = len(A)
    R, piv = rref([list(A[i]) + eye(n)[i] for i in range(n)])
    assert piv[:n] == list(range(n)), "singular"
    return [row[n:] for row in R[:n]]

# ----------------------------------------------------------------------------- the carrier


def homMap(Nm):
    d = len(Nm)
    H = zeros(d + 1)
    H[0][0] = Fr(1)
    for i in range(d):
        for j in range(d):
            H[i + 1][j + 1] = Fr(Nm[i][j])
    return H


def diagN(signs):
    d = len(signs)
    N = zeros(d)
    for i, s in enumerate(signs):
        N[i][i] = Fr(s)
    return N


def actT(Nm, w):  # row mu -> homMap N (w[mu])
    H = homMap(Nm)
    return [[sum(H[nu][k] * w[mu][k] for k in range(len(w))) for nu in range(len(w))] for mu in range(len(w))]


def actC(Nm, w):  # column nu -> homMap N (column)
    return matmul(homMap(Nm), w)


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def lift(c):
    return [Fr(0)] + [Fr(v) for v in c]


def tens(X, Y):
    return [[X[m] * Y[n] for n in range(len(Y))] for m in range(len(X))]


def prodState(x, y):
    return tens(hom(x), hom(y))


def pairVal(a, b, w):
    n = len(w)
    return sum(a[m] * w[m][k] * b[k] for m in range(n) for k in range(n))


def unit_basis(n):
    for i in range(n):
        for j in range(n):
            w = zeros(n)
            w[i][j] = Fr(1)
            yield (i, j), w


def gate_matrix(G, n):
    """n^2 x n^2 matrix of a linear map on W d, column (i,j) = vec G(E_ij)."""
    M = zeros(n * n)
    for (i, j), w in unit_basis(n):
        out = G(w)
        for a in range(n):
            for b in range(n):
                M[a * n + b][i * n + j] = out[a][b]
    return M


def apply_matrix(M, n):
    def G(w):
        v = [w[i][j] for i in range(n) for j in range(n)]
        o = [sum(M[r][c] * v[c] for c in range(n * n) if M[r][c]) for r in range(n * n)]
        return [o[a * n:(a + 1) * n] for a in range(n)]
    return G


def eq(w1, w2):
    return all(a == b for r1, r2 in zip(w1, w2) for a, b in zip(r1, r2))


def holds_relT(Nm, G, n):
    return all(eq(actT(Nm, G(actT(Nm, w))), G(w)) for _, w in unit_basis(n))


def holds_relC(Nm, G, n):
    return all(eq(actC(Nm, G(actC(Nm, w))), actT(Nm, G(w))) for _, w in unit_basis(n))


def corner(z, a):
    return list(z) if a == 0 else [-v for v in z]


def holds_frame(G, z):
    return all(eq(G(prodState(corner(z, a), corner(z, b))),
                  prodState(corner(z, a), corner(z, (a + b) % 2))) for a in (0, 1) for b in (0, 1))


def isNot(Nm, z):
    d = len(Nm)
    unit = sum(Fr(v) ** 2 for v in z) == 1
    NN = matmul(Nm, Nm)
    invol = all(NN[i][j] == (1 if i == j else 0) for i in range(d) for j in range(d))
    orth = all(sum(Nm[k][i] * Nm[k][j] for k in range(d)) == (1 if i == j else 0) for i in range(d) for j in range(d))
    flips = all(sum(Nm[i][j] * z[j] for j in range(d)) == -z[i] for i in range(d))
    # a linear map preserving the Euclidean ball is exactly an orthogonal one (contraction + involution)
    return unit and invol and orth and flips

# ----------------------------------------------------------------------------- landed gates (transcribed from Lean)

SGN = lambda m, n: Fr(-1) if (m == 1 and n == 3) or (m == 2 and n == 2) else Fr(1)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def cnot(w):
    return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]


NFLIP = diagN([1, -1, -1])
Z3 = [0, 0, 1]
REFL3 = diagN([1, 1, -1])
NEGID3 = diagN([-1, -1, -1])


def sgate(odd, p):
    def G(w):
        n = len(w)
        return [[w[p[m]][nu] if odd[nu] else w[m][nu] for nu in range(n)] for m in range(n)]
    return G


ODD5 = [False, False, False, True, True, True]
PERM5 = [5, 3, 4, 1, 2, 0]
GJ5 = sgate(ODD5, PERM5)
N5 = diagN([1, 1, -1, -1, -1])
Z5 = [0, 0, 0, 0, 1]


def cnot1(w):
    return [[w[(m + n) % 2][n] for n in range(2)] for m in range(2)]


NEG1 = diagN([-1])
Z1 = [1]

# ============================================================================= SECTION 1: Q1 parity


def LH_Theta(Nm):
    n = len(Nm) + 1
    LH = gate_matrix(lambda w: actC(Nm, w), n)
    TH = gate_matrix(lambda w: actC(Nm, actT(Nm, w)), n)
    return LH, TH


def trace(M):
    return sum(M[i][i] for i in range(len(M)))


def section1():
    print("\n=== SECTION 1 (Q1): relC alone versus the eigenspace balance ===")
    # (1.0) operator identity behind the argument: relC  <=>  G o L_H = (L_H o R_H) o G
    # checked as matrices for the landed cnot (positive control: must hold) and gJ3-free sanity.
    n = 4
    LH, TH = LH_Theta(NFLIP)
    Gm = gate_matrix(cnot, n)
    check("C1.0 landed cnot satisfies relC (reproduces cnot_relC)", holds_relC(NFLIP, cnot, n))
    check("C1.0' relC as matrix identity G.L_H = Theta.G for cnot", matmul(Gm, LH) == matmul(TH, Gm))
    check("C1.0'' landed gJ5 satisfies relC with n5 (reproduces gateRel_gJ5.relC)", holds_relC(N5, GJ5, 6))
    check("C1.0''' landed cnot1 satisfies relC with neg1", holds_relC(NEG1, cnot1, 2))
    # (1.1) trace invariant for every diagonal NOT type, d = 1..5
    rows = []
    allok = True
    for d in range(1, 6):
        n = d + 1
        for P in range(1, d + 1):  # P = dim E+ = 1 + #(+1 coordinates); last coordinate is the flipped axis
            Q = n - P
            signs = [1] * (P - 1) + [-1] * (Q)
            Nm = diagN(signs)
            z = [0] * (d - 1) + [1]
            ok_not = isNot(Nm, z)
            LH, TH = LH_Theta(Nm)
            tL, tT = trace(LH), trace(TH)
            # eigen-dimensions measured as ranks (exact), not by formula
            mLp = n * n - rank([[LH[i][j] - (1 if i == j else 0) for j in range(n * n)] for i in range(n * n)])
            mTp = n * n - rank([[TH[i][j] - (1 if i == j else 0) for j in range(n * n)] for i in range(n * n)])
            similar_possible = (mLp == mTp)
            rows.append((d, P, Q, ok_not, tL, tT, mLp, mTp, similar_possible))
            allok &= ok_not
            # formula cross-check (the formula is the claim; the measured ranks are the evidence)
            allok &= (mLp == n * P) and (mTp == P * P + Q * Q) and (tL == n * (P - Q)) and (tT == (P - Q) ** 2)
            allok &= (similar_possible == (P == Q))
    print("   d  P  Q  IsNot  tr(L_H)  tr(L_H R_H)  dim+1(L_H)  dim+1(L_H R_H)  invertible-relC-possible")
    for r in rows:
        print("  %2d %2d %2d  %5s  %7s  %11s  %10s  %14s  %s" % r)
    check("C1.1 for d<=5, every diagonal NOT type: +1-eigendims of L_H and L_H R_H agree iff P = Q", allok)
    # (1.2) direct exact solve of the relC system (d <= 3): solution space and maximal rank
    print("  direct exact solve of the linear system G.L_H = Theta.G (unknown G, n^2 x n^2):")
    direct_ok = True
    for d in (1, 2, 3):
        n = d + 1
        for P in range(1, d + 1):
            Q = n - P
            Nm = diagN([1] * (P - 1) + [-1] * Q)
            LH, TH = LH_Theta(Nm)
            m = n * n
            # equations: (G L_H - Theta G)[r][c] = 0, unknowns G[r][c] flattened
            # L_H, Theta are diagonal here; build the system generally anyway
            eqs = []
            for r in range(m):
                for c in range(m):
                    row = [Fr(0)] * (m * m)
                    for k in range(m):
                        if LH[k][c]:
                            row[r * m + k] += LH[k][c]
                        if TH[r][k]:
                            row[k * m + c] -= TH[r][k]
                    if any(row):
                        eqs.append(row)
            ns = nullspace(eqs) if eqs else [[Fr(int(i == j)) for i in range(m * m)] for j in range(m * m)]
            dimsol = len(ns)
            # random rational element; its rank is an exact lower bound for the maximal rank
            coeffs = [Fr(random.randint(-9, 9)) for _ in ns]
            Gv = [sum(cf * v[i] for cf, v in zip(coeffs, ns)) for i in range(m * m)]
            Gr = [Gv[r * m:(r + 1) * m] for r in range(m)]
            rk = rank(Gr)
            upper = min(n * P, P * P + Q * Q) + min(n * Q, 2 * P * Q)  # sum over eigenvalues of min multiplicities
            pred_dim = n * P * (P * P + Q * Q) + n * Q * (2 * P * Q)
            ok = (dimsol == pred_dim) and (rk == upper) and ((rk == m) == (P == Q))
            direct_ok &= ok
            print("   d=%d P=%d Q=%d  dim(solutions)=%d (pred %d)  rank(random solution)=%d  max-rank bound=%d  n^2=%d"
                  % (d, P, Q, dimsol, pred_dim, rk, upper, m))
    check("C1.2 direct solve: invertible relC solution found exactly when P = Q (d <= 3)", direct_ok)
    # (1.3) countercontrol: relT alone does NOT balance; frame + relT exist at even d = 2
    Nm2 = diagN([1, -1])
    z2 = [0, 1]
    ident = lambda w: [list(r) for r in w]
    check("X1.3a countercontrol: id satisfies relT with an unbalanced NOT at d=2 (P=2,Q=1)",
          holds_relT(Nm2, ident, 3) and isNot(Nm2, z2))

    def swapgate(w):  # exchange the entries (0,2) and (2,2): classical CNOT on the z-bit
        o = [list(r) for r in w]
        o[0][2], o[2][2] = w[2][2], w[0][2]
        return o
    fr = holds_frame(swapgate, z2)
    rt = holds_relT(Nm2, swapgate, 3)
    rc = holds_relC(Nm2, swapgate, 3)
    inv = rank(gate_matrix(swapgate, 3)) == 9
    check("X1.3b countercontrol: d=2 gate with frame + relT + invertible exists", fr and rt and inv)
    check("X1.3c ... and it fails relC (as balance forces)", not rc)
    # exploratory: does that d=2 gate fail forward positivity? exact witness search on a rational grid
    # rational points of the unit circle (pure states / sharp effects)
    pts = [(Fr(1), Fr(0)), (Fr(-1), Fr(0)), (Fr(0), Fr(1)), (Fr(0), Fr(-1))] + \
          [(Fr(s1 * p, 5), Fr(s2 * q, 5)) for p, q in ((3, 4), (4, 3)) for s1 in (1, -1) for s2 in (1, -1)]
    wit = None
    for x in pts:
        for y in pts:
            w = swapgate(prodState(list(x), list(y)))
            for a in pts:
                for b in pts:
                    v = pairVal(hom(list(a)), hom(list(b)), w)
                    if v < 0 and (wit is None or v < wit[0]):
                        wit = (v, x, y, a, b)
    print("   d=2 frame+relT gate, most negative grid value:", None if wit is None else
          "%s at x=%s y=%s a=%s b=%s" % tuple(map(str, wit)))
    S1 = not any(f.startswith(("C1", "X1")) for f in FAIL)
    if S1:
        print("  VERDICT S1: RELC-ALONE-BALANCES (measured: invertible relC solutions exist iff P=Q, d<=5 diag types;"
              " relT+frame admits even d=2)")
    return wit

# ============================================================================= SECTION 2: Q3 d = 3


def section2():
    print("\n=== SECTION 2 (Q3): d = 3 under relC alone ===")
    out = {}
    for name, Nm in (("nflip", NFLIP), ("refl3", REFL3), ("negId3", NEGID3)):
        LH, TH = LH_Theta(Nm)
        n = 4
        mLp = 16 - rank([[LH[i][j] - (1 if i == j else 0) for j in range(16)] for i in range(16)])
        mTp = 16 - rank([[TH[i][j] - (1 if i == j else 0) for j in range(16)] for i in range(16)])
        det = Nm[0][0] * Nm[1][1] * Nm[2][2]
        out[name] = (isNot(Nm, Z3), trace(LH), trace(TH), mLp, mTp, det)
        print("  %-7s IsNot=%s tr L_H=%s tr Theta=%s dim+1 L_H=%s dim+1 Theta=%s det=%s" % ((name,) + out[name]))
    check("C2.1 positive control nflip: traces agree, det 1 (reproduces det_nflip_rel)",
          out["nflip"][1] == out["nflip"][2] and out["nflip"][5] == 1)
    check("C2.2 refl3: IsNot, traces differ => no invertible G with relC alone (strengthens not_gateRel_refl3)",
          out["refl3"][0] and out["refl3"][1] != out["refl3"][2] and out["refl3"][5] == -1)
    check("C2.3 negId3: IsNot, traces differ => no invertible G with relC alone (strengthens not_gateRel_negId3)",
          out["negId3"][0] and out["negId3"][1] != out["negId3"][2] and out["negId3"][5] == -1)

# ============================================================================= SECTION 3: relT is independent of frame+relC+P±


R3 = [[Fr(3, 5), Fr(-4, 5), Fr(0)], [Fr(4, 5), Fr(3, 5), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
R3T = transpose(R3)


def GR(w):  # cnot o (I (x) homMap R)
    return cnot(actT(R3, w))


def GR_inv(w):  # (I (x) homMap R^T) o cnot   (cnot is an involution)
    return actT(R3T, cnot(w))


def lop_kernel_dim(G, Nm):
    """dim ker of DIM-1's Lop for diagonal N: f in Hom(E-, V) -> (G(f o projMinus))|E-."""
    n = len(Nm) + 1
    H = homMap(Nm)
    Em = [k for k in range(n) if H[k][k] == -1]
    cols = []
    for k in Em:
        for m in range(n):
            F = zeros(n)
            F[m][k] = Fr(1)  # f(b_k) = e_m
            out = G(F)
            cols.append([out[r][kk] for kk in Em for r in range(n)])
    M = transpose(cols)
    return len(cols) - rank(M)


def section3():
    print("\n=== SECTION 3: relT is not implied by frame + relC + positivity (d = 3) ===")
    n = 4
    check("C3.0 R fixes z3 and is orthogonal, R does not commute with nflip",
          [sum(R3[i][j] * Z3[j] for j in range(3)) for i in range(3)] == Z3
          and matmul(R3, R3T) == eye(3) and matmul(R3, NFLIP) != matmul(NFLIP, R3))
    check("C3.1 G_R = cnot o (I(x)R): frame", holds_frame(GR, Z3))
    check("C3.2 G_R: relC", holds_relC(NFLIP, GR, n))
    bad = [(ij) for ij, w in unit_basis(n) if not eq(actT(NFLIP, GR(actT(NFLIP, w))), GR(w))]
    check("C3.3 G_R: relT FAILS (mismatch on %d of 16 matrix units)" % len(bad), len(bad) > 0)
    check("C3.4 G_R invertible with inverse (I(x)R^T) o cnot",
          all(eq(GR_inv(GR(w)), w) and eq(GR(GR_inv(w)), w) for _, w in unit_basis(n)))
    # identity behind the positivity reduction: G_R(prodState x y) = cnot(prodState x (R y)) (symbolic, exact)
    import sympy as sp
    xs = sp.symbols('x0:3'); ys = sp.symbols('y0:3')
    Ry = [sum(sp.Rational(R3[i][j].numerator, R3[i][j].denominator) * ys[j] for j in range(3)) for i in range(3)]

    def toS(w):
        return [[sp.nsimplify(v) for v in r] for r in w]
    X = [1] + list(xs); Y = [1] + list(ys); RY = [1] + Ry
    w_in = [[X[m] * Y[k] for k in range(4)] for m in range(4)]
    w_rot = [[X[m] * RY[k] for k in range(4)] for m in range(4)]
    # apply GR symbolically
    Hm = homMap(R3)
    w_actT = [[sum(sp.Rational(Hm[k][j].numerator, Hm[k][j].denominator) * w_in[m][j] for j in range(4)) for k in range(4)] for m in range(4)]
    lhs = [[SGN(m, k) * w_actT[PC[m][k]][PT[m][k]] for k in range(4)] for m in range(4)]
    rhs = [[SGN(m, k) * w_rot[PC[m][k]][PT[m][k]] for k in range(4)] for m in range(4)]
    check("C3.5 identity G_R(prodState x y) = cnot(prodState x (R y)) for symbolic x, y",
          all(sp.expand(lhs[m][k] - rhs[m][k]) == 0 for m in range(4) for k in range(4)))
    # landed-proof route: Lop injectivity under relC only
    k_cnot = lop_kernel_dim(cnot, NFLIP)
    k_GR = lop_kernel_dim(GR, NFLIP)
    print("  dim ker Lop: cnot=%d  G_R=%d" % (k_cnot, k_GR))
    check("C3.6 positive control: Lop injective for cnot (reproduces Lop_injective_rel)", k_cnot == 0)
    return k_GR

# ============================================================================= SECTION 4: the relT-free replacement lemma


def KG_factory():
    # K exchanges the matrix units x(x)x = E_11 and y(x)y = E_22 (both +1 for L_H R_H with nflip); KG = K o cnot
    def KG(w):
        o = cnot(w)
        o = [list(r) for r in o]
        o[1][1], o[2][2] = o[2][2], o[1][1]
        return o
    return KG


def corner_maps(G, Ginv, z):
    d = len(z)
    n = d + 1
    hz = hom(z)

    def cornerMap(GG):
        M = zeros(n)
        for nu in range(n):
            e = [Fr(int(i == nu)) for i in range(n)]
            out = GG(tens(hz, e))
            for mu in range(n):
                M[mu][nu] = out[0][mu]
        return M
    return cornerMap(G), cornerMap(Ginv)


def Phi(G, Minv, a, c, f, t):
    n = len(t)
    Mt = [sum(Minv[i][j] * t[j] for j in range(n)) for i in range(n)]
    return pairVal(a, f, G(tens(lift(c), Mt)))


def lemma_defect(G, Ginv, Nm, z):
    """max |Phi(e_mu, c; u, hom 0)| over mu, c in a basis of z^perp, u in a basis of E-."""
    d = len(z)
    n = d + 1
    Mfwd, Minv = corner_maps(G, Ginv, z)
    H = homMap(Nm)
    # bases (diagonal N, z a coordinate axis)
    zc = [i for i in range(d) if z[i] != 0][0]
    cs = [[Fr(int(i == j)) for i in range(d)] for j in range(d) if j != zc]
    us = [[Fr(int(i == k)) for i in range(n)] for k in range(n) if H[k][k] == -1]
    e = lambda mu: [Fr(int(i == mu)) for i in range(n)]
    vals = {}
    for ci, c in enumerate(cs):
        for ui, u in enumerate(us):
            for mu in range(n):
                v = Phi(G, Minv, e(mu), c, u, hom([0] * d))
                if v != 0:
                    vals[(ci, ui, mu)] = v
    return vals, Mfwd, Minv


def section4(k_GR):
    print("\n=== SECTION 4: the relT-free replacement for DIM-1's single relT step ===")
    n = 4
    KG = KG_factory()
    # inverse of KG: cnot o K (both involutions)
    def KGinv(w):
        o = [list(r) for r in w]
        o[1][1], o[2][2] = o[2][2], o[1][1]
        return cnot(o)
    check("C4.0 KG o KGinv = id", all(eq(KG(KGinv(w)), w) for _, w in unit_basis(n)))
    LH, TH = LH_Theta(NFLIP)
    def K(w):
        o = [list(r) for r in w]
        o[1][1], o[2][2] = w[2][2], w[1][1]
        return o
    Km = gate_matrix(K, n)
    check("C4.1 K commutes with Theta = L_H R_H (so relC is preserved)", matmul(Km, TH) == matmul(TH, Km))
    check("C4.2 KG: frame", holds_frame(KG, Z3))
    check("C4.3 KG: relC", holds_relC(NFLIP, KG, n))
    check("C4.4 KG: relT fails", not holds_relT(NFLIP, KG, n))
    # the lemma: Phi(a, c; u, hom 0) = 0 for u in E-, c perp z
    for name, G, Gi in (("cnot", cnot, cnot), ("G_R", GR, GR_inv), ("KG", KG, KGinv)):
        vals, Mf, Mi = lemma_defect(G, Gi, NFLIP, Z3)
        ok_inv = matmul(Mf, Mi) == eye(4)
        print("  %-5s Mfwd.Minv = I: %s ; nonzero Phi(e_mu, c; u, hom0) entries: %s" % (name, ok_inv, vals))
        if name == "cnot":
            check("C4.5 positive control (GateRel+positive): lemma conclusion holds for cnot", ok_inv and not vals)
        if name == "G_R":
            check("C4.6 positive control (relC-only, positive): lemma conclusion holds for G_R", ok_inv and not vals)
        if name == "KG":
            check("X4.7 countercontrol (relC-only, frame): lemma conclusion FAILS for KG", ok_inv and bool(vals))
    # --- the proof chain of the replacement lemma, step by step ---------------------------------
    # (i) eigen-sign: relC gives H w H = (+/-) w for w = G(lift c (x) Minv t), c in T+ / T-;
    # (ii) mixed symmetry Phi(a; h0, u) = Phi(a; u, h0) (landed Phi_sphere.2, a consequence of positivity);
    # (iii) supports: Phi(.; u, h0) and Phi(.; h0, u) live on complementary eigenspaces of H, so (ii) forces 0.
    H = homMap(NFLIP)
    e = lambda mu: [Fr(int(i == mu)) for i in range(4)]
    h0 = hom([0, 0, 0])
    Tp = [[1, 0, 0]]          # c in T+ (N c = c, c perp z3)
    Tm = [[0, 1, 0]]          # c in T- (N c = -c, c perp z3)
    Em = [e(2), e(3)]         # E- of homMap nflip
    for name, G, Gi in (("cnot", cnot, cnot), ("G_R", GR, GR_inv), ("KG", KG, KGinv)):
        Mf, Mi = corner_maps(G, Gi, Z3)
        sign_ok = True
        for cs, sgn in ((Tp, 1), (Tm, -1)):
            for c in cs:
                for t in [e(k) for k in range(4)]:
                    Mt = [sum(Mi[i][j] * t[j] for j in range(4)) for i in range(4)]
                    w = G(tens(lift(c), Mt))
                    HwH = matmul(matmul(H, w), H)
                    sign_ok &= eq(HwH, [[sgn * v for v in r] for r in w])
        mixed = all(Phi(G, Mi, e(mu), c, h0, u) == Phi(G, Mi, e(mu), c, u, h0)
                    for c in Tp + Tm for u in Em for mu in range(4))
        concl = all(Phi(G, Mi, e(mu), c, u, h0) == 0 for c in Tp + Tm for u in Em for mu in range(4))
        print("  %-5s (i) eigen-sign: %s  (ii) mixed symmetry: %s  conclusion Phi(.;u,h0)=0: %s"
              % (name, sign_ok, mixed, concl))
        if name in ("cnot", "G_R"):
            check("C4.8 %s: (i), (ii) and the conclusion hold" % name, sign_ok and mixed and concl)
        else:
            check("X4.8 KG: (i) holds (relC), (ii) fails, conclusion fails -- the chain is not vacuous",
                  sign_ok and (not mixed) and (not concl))
    # (iv) KG is excluded by positivity: explicit rational witness.  Control input hom x, target input
    # hom(-y), target effect hom(-y), control effect hom(0, 4/5, -3/5).  (A pre-computation that applied
    # the identity (ii) to KG predicted -6/5; (ii) fails for KG, and the exact value is measured here.)
    x_in = [1, 0, 0]
    y_in = [0, -1, 0]
    a_eff = [0, Fr(4, 5), Fr(-3, 5)]
    b_eff = [0, -1, 0]
    v = pairVal(hom(a_eff), hom(b_eff), KG(prodState(x_in, y_in)))
    v1 = pairVal(hom(a_eff), hom(b_eff), cnot(prodState(x_in, y_in)))
    print("  witness value: KG=%s  cnot=%s" % (v, v1))
    check("X4.9 KG fails posFwd at an explicit rational witness (value %s < 0)" % v, v < 0)
    check("C4.10 the same inputs/effects on cnot give a nonnegative value (%s)" % v1, v1 >= 0)
    # (v) the slice formula of the alternative (tangent-curve) proof on the positive gates:
    #     F(a) = pairVal(a, h0-u, G(hom c (x) Minv(h0-u))) = a0 + a_z - 2 Phi(a; u, h0)
    form_ok = True
    for G, Gi in ((cnot, cnot), (GR, GR_inv)):
        Mf, Mi = corner_maps(G, Gi, Z3)
        for c in Tp + Tm:
            for u in Em:
                t = [h0[i] - u[i] for i in range(4)]
                Mt = [sum(Mi[i][j] * t[j] for j in range(4)) for i in range(4)]
                hc = hom(c)
                for mu in range(4):
                    F = pairVal(e(mu), t, G(tens(hc, Mt)))
                    pred = e(mu)[0] + e(mu)[3] - 2 * Phi(G, Mi, e(mu), c, u, h0)
                    form_ok &= (F == pred)
    check("C4.11 slice formula of the alternative proof holds on cnot and G_R", form_ok)
    # (vi) step (i) at d = 5 on the landed relC gate gJ5 (n5, z5): H w H = +/- w for w = G(lift c (x) t)
    H5 = homMap(N5)
    sign5 = True
    for j, sg in ((0, 1), (1, 1), (2, -1), (3, -1)):  # coordinates 0,1 in T+, 2,3 in T- (4 is z5)
        c = [Fr(int(i == j)) for i in range(5)]
        for k in range(6):
            t = [Fr(int(i == k)) for i in range(6)]
            w = GJ5(tens(lift(c), t))
            sign5 &= eq(matmul(matmul(H5, w), H5), [[sg * v for v in r] for r in w])
    check("C4.12 step (i) eigen-sign holds at d = 5 for the landed relC gate gJ5", sign5)
    k_KG = lop_kernel_dim(KG, NFLIP)
    print("  dim ker Lop: G_R=%d  KG=%d" % (k_GR, k_KG))
    S4 = not any(f.startswith(("C4", "X4")) for f in FAIL)
    if S4:
        print("  VERDICT S4: the replacement lemma holds on both positive controls (relT and relC-only) and its proof's "
              "witness refutes positivity on the relC-only countercontrol")
    return k_KG


if __name__ == "__main__":
    wit = section1()
    section2()
    k_GR = section3()
    k_KG = section4(k_GR)
    print("\nSUMMARY: %d failed checks" % len(FAIL))
    for f in FAIL:
        print("  FAILED:", f)
    sys.exit(1 if FAIL else 0)
