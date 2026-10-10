"""u5_kf.py -- thread U, level (ii): the cone K_F = (Q3 ∩ Z_F*) + cone(Z_F), Z_F = G16-orbit of F, exactly.

Decision rule (fixed before the first run):
- PASS/FAIL per check; countercontrols PASS only when the altered construction FAILS the property.
- `VERDICT KF-INGREDIENTS-EXACT` prints only if every check passes; else `VERDICT KF-INGREDIENTS-FAILED`.
- Exact arithmetic only.
Checked: F is a member of Z_F; Z_F mutually orthogonal, in maxCone, not PSD, pauliW z_s = (1/8)(I - 2 P_f(-s));
H1 by an SOS identity per member; at most one Z_F-constraint fails on any PSD q (diagonal-sum identity);
the projection lemma per member (determinant identity + positive principal block); the order-16 group of the
(even, even) native gates permutes Z_F; its generators are Q3-automorphisms (exact dictionary identities);
countercontrol: the non-orthogonal orbit {aE00 ± E13 ± E22}, a = 3/2, has y ∈ K_Z* \\ K_Z.
"""
import sympy as sp

I = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
X, Y, Z = S[1], S[2], S[3]


def kron(A, B):
    return sp.Matrix(A.rows * B.rows, A.cols * B.cols,
                     lambda i, j: A[i // B.rows, j // B.cols] * B[i % B.rows, j % B.cols])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m, n) in ((1, 3), (2, 2)) else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def pauliW(w):
    R = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            R += w[m, n] * SS[m][n]
    return R / 4


def table(R):
    return sp.Matrix(4, 4, lambda m, n: sp.expand((R * SS[m][n]).trace()))


def ipW(w, v):
    return sp.expand(sum(w[i] * v[i] for i in range(16)))


def Eunit(m, n):
    E = sp.zeros(4, 4)
    E[m, n] = 1
    return E


def homMap(N):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:4, 1:4] = N
    return H


def actC(N, w):
    return homMap(N) * w


def actT(N, w):
    return w * homMap(N).T


RES = []


def check(cid, kind, ok, detail=""):
    ok = bool(ok)
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + cid + "  [" + kind + "] " + detail)


E00 = Eunit(0, 0)
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def zF(s1, s2):
    return (E00 + s1 * Eunit(1, 3) + s2 * Eunit(2, 2) - s1 * s2 * Eunit(3, 1)) / 4


ZF = [zF(*s) for s in SIGNS]
fb = {(1, -1): sp.Matrix([-1, 1, -1, -1]) / 2, (1, 1): sp.Matrix([1, 1, 1, -1]) / 2,
      (-1, -1): sp.Matrix([1, 1, -1, 1]) / 2, (-1, 1): sp.Matrix([-1, 1, 1, 1]) / 2}   # (XZ, YY) eigenbasis
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
F = E00 / 2 - actT(RH, sp.diag(1, 1, -1, 1)) / 4

print("== S1  the family Z_F")
check("F1", "exact", F == zF(-1, -1), "F = E00/2 - T_psi/4 is the member s = (-1,-1) of Z_F")
check("F2", "exact", all(kron(X, Z) * fb[k] == k[0] * fb[k] and kron(Y, Y) * fb[k] == k[1] * fb[k] for k in fb),
      "f(x,y) are joint eigenvectors of X(x)Z (eigenvalue x) and Y(x)Y (eigenvalue y)")
proj_ok = all(pauliW(zF(*s)) == (sp.eye(4) - 2 * fb[(-s[0], -s[1])] * fb[(-s[0], -s[1])].T) / 8 for s in SIGNS)
check("F3", "identity", proj_ok, "pauliW z_s = (1/8)(I - 2 |f(-s)><f(-s)|): spectrum (1,1,1,-1)/8, so z_s ∉ Q3")
gram = sp.Matrix(4, 4, lambda i, j: ipW(ZF[i], ZF[j]))
check("F4", "exact", gram == sp.eye(4) / 4, "Gram matrix of Z_F = (1/4) I: mutually orthogonal, self-positive")
mc_ok = True
for zz in ZF:
    Mb = sp.Matrix(3, 3, lambda j, k: zz[j + 1, k + 1])
    loc = [zz[0, k] for k in range(1, 4)] + [zz[k, 0] for k in range(1, 4)]
    mc_ok = mc_ok and all(t == 0 for t in loc) and Mb.T * Mb == sp.eye(3) / 16 and zz[0, 0] == sp.Rational(1, 4)
check("F5", "exact", mc_ok, "each z_s: no local part, bilinear part (1/4) x signed permutation, so sigma_max = z_00 "
      "and z_s ∈ maxCone (on its boundary)")
xs = sp.symbols("x1:4", real=True)
ys = sp.symbols("y1:4", real=True)
P = sp.Matrix(4, 4, lambda m, n: ([1] + list(xs))[m] * ([1] + list(ys))[n])
nx2, ny2 = sum(t ** 2 for t in xs), sum(t ** 2 for t in ys)
h1 = True
for (s1, s2), zz in zip(SIGNS, ZF):
    sos = ((1 - nx2) + (1 - ny2) + (xs[0] + s1 * ys[2]) ** 2 + (xs[1] + s2 * ys[1]) ** 2
           + (xs[2] - s1 * s2 * ys[0]) ** 2) / 8
    h1 = h1 and sp.expand(ipW(P, zz) - sos) == 0
check("F6", "identity", h1, "8<prodState x y, z_s> = (1-|x|^2) + (1-|y|^2) + (x1+s1 y3)^2 + (x2+s2 y2)^2 "
      "+ (x3-s1 s2 y1)^2 for all four s (H1 on the ball)")
hs = sp.Matrix(4, 4, lambda i, j: sp.Symbol("r%d%d" % (min(i, j), max(i, j)), real=True) if i == j else
               (sp.Symbol("r%d%d" % (i, j), real=True) + I * sp.Symbol("u%d%d" % (i, j), real=True) if i < j else
                sp.Symbol("r%d%d" % (j, i), real=True) - I * sp.Symbol("u%d%d" % (j, i), real=True)))
cap_ok = True
for s in SIGNS:
    f = fb[(-s[0], -s[1])]
    lhs = ipW(table(hs), zF(*s))
    cap_ok = cap_ok and sp.expand(lhs - (hs.trace() - 2 * (f.T * hs * f)[0]) / 2) == 0
dsum = sp.expand(sum((fb[k].T * hs * fb[k])[0] for k in fb) - hs.trace())
check("F7", "identity", cap_ok and dsum == 0,
      "<q, z_s> = (tr q - 2 <f(-s)|q|f(-s)>)/2 and the four f-diagonal entries sum to tr q (generic Hermitian q): "
      "a PSD q violates at most one Z_F constraint")

print("== S2  the projection lemma for each member (spectrum (1,1,1,-1)/8)")
cs = [sp.Symbol("a%d" % j, real=True) + I * sp.Symbol("b%d" % j, real=True) for j in range(4)]
nn = [sp.expand(c * sp.conjugate(c)) for c in cs]
pl_ok = True
for s in SIGNS:
    zz = zF(*s)
    neg = (-s[0], -s[1])
    others = [k for k in fb if k != neg]
    Vb = sp.Matrix.hstack(*([fb[k] for k in others] + [fb[neg]]))
    psi = Vb * sp.Matrix(cs)
    q = table(psi * psi.H)
    Pq = q - (ipW(q, zz) / ipW(zz, zz)) * zz
    Dm = sp.expand(Vb.T * pauliW(Pq) * Vb)
    Bp = nn[3] - nn[0] - nn[1] - nn[2]
    det_ok = sp.expand(Dm.det() - 3 * Bp ** 4 / 256) == 0
    blk_ok = sp.expand(Dm[0:3, 0:3] - (Bp / 4 * sp.eye(3) + sp.Matrix(cs[0:3]) * sp.Matrix(cs[0:3]).H)) \
        == sp.zeros(3, 3)
    pl_ok = pl_ok and det_ok and blk_ok
check("PL", "identity", pl_ok, "for each z_s and psi = sum c_k f_k: det pauliW(Pi_s q) = 3 B'^4/256 and the block on "
      "the three non-cap vectors is (B'/4) I + c c^H, B' = n_cap - sum n_other (> 0 in the cap): Pi_s q ≻ 0")
qb = table(fb[(1, 1)] * fb[(1, 1)].T)
zz = zF(1, 1)
Pb = pauliW(qb - (ipW(qb, zz) / ipW(zz, zz)) * zz)
check("PLc", "countercontrol", ipW(qb, zz) > 0 and (fb[(1, -1)].T * Pb * fb[(1, -1)])[0] < 0,
      "outside the cap the projection is not PSD (psi = f(1,1) against z_(1,1); f(1,-1)^T rho' f(1,-1) = %s)"
      % (fb[(1, -1)].T * Pb * fb[(1, -1)])[0])

print("== S3  level (ii): the order-16 group permutes Z_F and consists of Q3-automorphisms")
diag3 = [sp.diag(s1, s2, 1) for s1 in (1, -1) for s2 in (1, -1)]


def mat(f):
    M = sp.zeros(16, 16)
    for j in range(16):
        e = sp.zeros(4, 4)
        e[j // 4, j % 4] = 1
        r = f(e)
        for i in range(16):
            M[i, j] = r[i // 4, i % 4]
    return M


def vec(w):
    return sp.Matrix([w[i // 4, i % 4] for i in range(16)])


def close(gens):
    grp, front = [sp.eye(16)], [sp.eye(16)]
    while front:
        new = []
        for A in front:
            for Gm in gens:
                Bm = Gm * A
                if all(Bm != H for H in grp):
                    grp.append(Bm)
                    new.append(Bm)
        front = new
    return grp


gates = []
for D in (sp.eye(3), sp.diag(-1, -1, 1)):
    for Dp in diag3:
        for R0 in diag3:
            if Dp.det() * R0.det() == 1:
                gates.append(mat(lambda w, D=D, Dp=Dp, R0=R0: actC(D, cnot(actC(Dp, actT(R0, w))))))
G16 = close(gates)
Cm = mat(cnot)
Zc = mat(lambda w: actC(sp.diag(-1, -1, 1), w))
Zt = mat(lambda w: actT(sp.diag(-1, -1, 1), w))
Tg = mat(lambda w: actC(sp.diag(1, -1, 1), actT(sp.diag(1, -1, 1), w)))
H4 = close([Cm, Zc, Zt, Tg])
same = len(G16) == 16 and len(H4) == 16 and all(any(A == B for B in H4) for A in G16)
check("G1", "exact", same, "the (even, even) gates generate the same order-16 group as {cnot, Z_c, Z_t, T}")
zv = [vec(zz) for zz in ZF]
def perm_of(Gm):
    idx = []
    for v in zv:
        hits = [k for k, u in enumerate(zv) if u == Gm * v]
        if len(hits) != 1:
            return None
        idx.append(hits[0])
    return idx


perm_ok = all(perm_of(Gm) is not None and sorted(perm_of(Gm)) == [0, 1, 2, 3] for Gm in G16)
check("G2", "exact", perm_ok, "every one of the 16 elements maps Z_F onto Z_F")
wsym = sp.Matrix(4, 4, lambda m, n: sp.Symbol("w%d%d" % (m, n), real=True))
UC = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
R = pauliW(wsym)
dic = [cnot(wsym) == table(UC * R * UC),
       actC(sp.diag(-1, -1, 1), wsym) == table(kron(Z, sp.eye(2)) * R * kron(Z, sp.eye(2))),
       actT(sp.diag(-1, -1, 1), wsym) == table(kron(sp.eye(2), Z) * R * kron(sp.eye(2), Z)),
       actC(sp.diag(1, -1, 1), actT(sp.diag(1, -1, 1), wsym)) == table(R.T)]
check("G3", "identity", all(dic), "cnot = Ad(CNOT), Z_c = Ad(Z(x)I), Z_t = Ad(I(x)Z), T = global transpose on "
      "generic tables: each generator preserves Q3")

print("== S4  countercontrol: the non-orthogonal orbit {a E00 ± E13 ± E22}, a = 3/2, is not self-dual")
a = sp.Rational(3, 2)


def zE(s1, s2):
    return a * E00 + s1 * Eunit(1, 3) + s2 * Eunit(2, 2)


ZE = [zE(*s) for s in SIGNS]
s0 = (2 - a) / a ** 2
yv = table(fb[(-1, -1)] * fb[(-1, -1)].T) + s0 * zE(1, -1)
in_dual = all(ipW(yv, zz) >= 0 for zz in ZE) and ipW(yv, zE(1, 1)) == 0
pos_pair = all(ipW(zz, zE(1, 1)) > 0 for zz in ZE) and min(ipW(u, v) for u in ZE for v in ZE) >= 0
notpsd = (fb[(-1, 1)].T * pauliW(yv) * fb[(-1, 1)])[0] < 0
check("CC", "countercontrol", in_dual and pos_pair and notpsd,
      "y = P_e3 + (2-a)/a^2 z_(1,-1) ∈ (Q3 + cone Z) ∩ Z*, <y, z_(1,1)> = 0, every <z_s, z_(1,1)> > 0 and y ∉ Q3 "
      "(g^T y g = %s): y ∉ K_Z, so K_Z ≠ K_Z*; orthogonality of the orbit is load-bearing" %
      (fb[(-1, 1)].T * pauliW(yv) * fb[(-1, 1)])[0])

print("== S5  distinctness")
Tpsi = actT(RH, sp.diag(1, 1, -1, 1))
E0 = E00 + Eunit(1, 3) - Eunit(2, 2)
check("D1", "exact", ipW(Tpsi, F) == sp.Rational(-1, 2) and (pauliW(Tpsi) ** 2 == pauliW(Tpsi)),
      "T_psi is pure with <T_psi, F> = -1/2: T_psi ∈ Q3 \\ K_F, F ∈ K_F \\ Q3 (K_F incomparable with Q3)")
check("D2", "exact", ipW(E0, actC(sp.diag(-1, -1, 1), E0)) == -1,
      "E0 ∉ K_F (K_F is level-(ii) invariant and <E0, Z_c E0> = -1), so K_F ≠ K*")

print()
nfail = RES.count(False)
print("checks: %d, failed: %d" % (len(RES), nfail))
print("VERDICT " + ("KF-INGREDIENTS-EXACT" if nfail == 0 else "KF-INGREDIENTS-FAILED") + " -- %d checks" % len(RES))
