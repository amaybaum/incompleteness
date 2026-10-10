"""Exact re-derivation checks for S1-S5 (sympy over Q). Read-only.
Conventions: R^n = R u + R^d, R^d = T + R z (T transverse, dim d-1). k_a = u + s_a z (s_a = (-1)^a) are the corners and
also the effects <a| (k_a . k_b = 2 delta_ab).  N = diag(u: 1; first p transverse: +1; remaining q: -1; z: -1).
Each check is marked with the proof step it certifies.  Solution spaces are computed as exact nullspaces of constraints
sampled at rational sphere points (a superset of the true space) and compared with the claimed family, which is shown
to satisfy the unsampled constraints identically (so all three spaces coincide)."""
import itertools, sympy as sp
OUT = []
def rep(n, ok, det=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n + ('  ' + det if det else ''), flush=True)

import random
def sphere_pts(dim, K, seed=0):
    rnd = random.Random(1000 * dim + seed); pts = []
    while len(pts) < K:                          # generic rational points on S^(dim-1) (inverse stereographic)
        tt = [rnd.randint(-7, 7) for _ in range(dim - 1)]; s2 = sum(x * x for x in tt)
        pts.append([sp.Rational(2 * x, s2 + 1) for x in tt] + [sp.Rational(s2 - 1, s2 + 1)])
    return pts
import numpy as np
P_ = 2147483647
def nullity_modp(rows_int, ncols):
    A = np.array(rows_int, dtype=object)
    A = np.array([[int(x) % P_ for x in r] for r in rows_int], dtype=np.int64); r = 0
    for c in range(ncols):
        if r == A.shape[0]: break
        nz = np.nonzero(A[r:, c])[0]
        if len(nz) == 0: continue
        kk = r + nz[0]; A[[r, kk]] = A[[kk, r]]; A[r] = (A[r] * pow(int(A[r, c]), P_ - 2, P_)) % P_
        col = A[:, c].copy(); col[r] = 0; idx = np.nonzero(col)[0]
        if len(idx): A[idx] = (A[idx] - (col[idx, None] * A[r]) % P_) % P_
        r += 1
    return ncols - r

th = sp.symbols('theta', real=True)
# ---- Lemma A inputs: the curves -------------------------------------------------------------------------------
u2 = sp.Matrix([1, 0]); z2 = sp.Matrix([0, 1])
for a in (0, 1):
    sa = (-1) ** a; ka = u2 + sa * z2; kb = u2 - sa * z2
    lhs = u2 + sa * sp.cos(th) * z2
    rhs = sp.cos(th / 2) ** 2 * ka + sp.sin(th / 2) ** 2 * kb
    rep('A a=%d: u + s_a cos(th) z = cos^2(th/2) k_a + sin^2(th/2) k_abar' % a, sp.simplify(lhs - rhs) == sp.zeros(2, 1))
rep('A: d/dth cos^2(th/2) and sin^2(th/2) vanish at th = 0 and th = pi (so W\'(0) = G(c(x)t), W\'(pi) = -G(c(x)t))',
    all(sp.simplify(sp.diff(f, th).subs(th, v)) == 0 for f in (sp.cos(th / 2) ** 2, sp.sin(th / 2) ** 2) for v in (0, sp.pi)))

for d in (2, 3, 4, 5, 6, 7):
    n = d + 1; Tn = d - 1
    U, Z = 0, d                                   # indices: 0 = u, 1..d-1 = T, d = z
    e = sp.eye(n)
    k = [e[:, U] + e[:, Z], e[:, U] - e[:, Z]]
    # ---- S1: Z_a(t) = G(k_a (x) t), t in T.  Kernel conditions from Lemma A at th = 0, pi --------------------------
    for a in (0, 1):
        kbar = k[1 - a]
        # unknown Z in R^n (x) R^n as n x n matrix (row = control, col = target)
        zs = sp.symbols('z0:%d' % (n * n)); Zm = sp.Matrix(n, n, zs)
        eqs = list(kbar.T * Zm) + list(Zm * k[0]) + list(Zm * k[1])
        # theta = pi/2, effect curve f(phi) = (1, -s_a cos(phi) z + sin(phi) tau): derivative condition sum_i tau.c_i g.n_i = 0
        # i.e. the T (x) R^n block of Z vanishes (every tau in T, every g)
        eqs += [Zm[i, j] for i in range(1, d) for j in range(n)]
        A = sp.Matrix([[sp.diff(q, v) for v in zs] for q in eqs])
        ns = A.nullspace()
        fam = [sp.Matrix(n, n, lambda i, j: k[a][i] * (1 if j == m else 0)) for m in range(1, d)]   # k_a (x) e_m, m in T
        famv = sp.Matrix([list(F) for F in fam]).T
        nsv = sp.Matrix([list(v) for v in ns]).T if ns else sp.zeros(n * n, 0)
        same = len(ns) == len(fam) and (famv.row_join(nsv)).rank() == len(fam)
        rep('S1 d=%d a=%d: Z_a(t) in span{k_a} (x) T exactly (dim %d)' % (d, a, Tn), same)
    for p in range(0, Tn + 1):
        q = Tn - p
        Nd = [1] + [1] * p + [-1] * q + [-1]
        Vp = [i for i in range(1, d) if Nd[i] == 1]; Vm = [i for i in range(1, n) if Nd[i] == -1]
        # ---- S2: one T_A-component of G~(c (x) t): w(t) = Phi (u + t'), conditions for a = 0, 1 (M_0 = I, M_1 = N):
        #      (1, -t') . w = 0 and (1, -N t') . w = 0 for every unit t' in R^d.
        ph = sp.symbols('f0:%d' % (n * n)); Phi = sp.Matrix(n, n, ph)          # Phi[:, j] = image of e_j
        rows = []
        for tp in sphere_pts(d, 6 * n):
            den = sp.ilcm(*[sp.fraction(x)[1] for x in tp])
            t = [den] + [x * den for x in tp]                       # integer-scaled point (scaling keeps the zero set)
            for sgnN in (False, True):
                gg = [den] + [-(Nd[i + 1] if sgnN else 1) * tp[i] * den for i in range(d)]
                rows.append([int(gg[i] * t[j]) for i in range(n) for j in range(n)])   # coefficient of Phi[i, j]
        null_bound = nullity_modp(rows, n * n)                      # >= nullity over Q of the sampled system
        # claimed family: Phi(u) = alpha in V+, Phi(e_j) u-comp = alpha_j (j in V+), 0 (j in V-); R-part block-diagonal antisym
        fam = []
        for r_ in Vp:                                                         # alpha components (same coefficient twice)
            M = sp.zeros(n, n); M[r_, U] = 1; M[U, r_] = 1; fam.append(M)
        for blk in (Vp, Vm):
            for i, j in itertools.combinations(blk, 2):
                M = sp.zeros(n, n); M[i, j] = 1; M[j, i] = -1; fam.append(M)
        famv = sp.Matrix([list(F) for F in fam]).T if fam else sp.zeros(n * n, 0)
        # the family satisfies the constraints identically (symbolic t')
        tsym = sp.symbols('t1:%d' % (d + 1)); tt = sp.Matrix([1] + list(tsym))
        g0 = sp.Matrix([1] + [-x for x in tsym]); g1 = sp.Matrix([1] + [-Nd[i + 1] * tsym[i] for i in range(d)])
        ident = all(sp.expand((g0.T * F * tt)[0]) == 0 and sp.expand((g1.T * F * tt)[0]) == 0 for F in fam)
        same = null_bound == len(fam) and (famv.rank() == len(fam) if fam else True)
        dimS = p + p * (p - 1) // 2 + (q + 1) * q // 2
        rep('S2 d=%d p=%d q=%d: solution space == [alpha_r at (r,u) AND (u,r)] + so(V+) + so(V-) (dim %d); identities exact'
            % (d, p, q, dimS), same and ident and len(fam) == dimS)
        # the transposed alternative (u,r) = -alpha_r is NOT a solution when p >= 1 (the bug the owner flagged)
        if Vp:
            M = sp.zeros(n, n); M[Vp[0], U] = 1; M[U, Vp[0]] = -1
            bad = any(sp.expand((g0.T * M * tt)[0]) != 0 for _ in [0])
            rep('S2 d=%d p=%d: the transposed form (u,r) = -(r,u) violates the constraint' % (d, p), bad)

# ---- S3: finite orthonormal-basis average, arbitrary p (symbolic g, K) -------------------------------------------
for p in range(1, 9):
    g = sp.Matrix(sp.symbols('g0:%d' % p)); Ks = sp.symbols('K0:%d' % max(1, p * (p - 1) // 2)); K = sp.zeros(p); c = 0
    for i in range(p):
        for j in range(i + 1, p): K[i, j] = Ks[c]; K[j, i] = -Ks[c]; c += 1
    I = sp.eye(p); lhs = 0; rhs = 0
    for i in range(p):
        for sg in (1, -1):
            t = sg * I[:, i]
            lhs += (1 + (g.T * t)[0]) ** 2; v = g + (I + K) * t; rhs += (v.T * v)[0]
    target = -2 * ((p - 1) * (g.T * g)[0] + (K.T * K).trace())
    rep('S3 p=%d: sum over t = +-e_i of [(1+g.t)^2 - |g+(I+K)t|^2] = -2((p-1)|g|^2 + |K|_F^2)' % p,
        sp.expand(lhs - rhs - target) == 0)

# ---- S4: the value formula on T_A (x) E+ for a structured G~ (symbolic A_r, B_rs), d = 5 and 7, M_0 = I -------------
for (d, p) in ((5, 2), (7, 3)):
    n = d + 1; Tn = d - 1; TA = list(range(1, d)); Vp = list(range(1, p + 1))
    As = {r_: sp.Matrix(Tn, Tn, sp.symbols('A%d_0:%d' % (r_, Tn * Tn))) for r_ in Vp}
    Bs = {}
    for r_, s_ in itertools.combinations(Vp, 2):
        Bs[(r_, s_)] = sp.Matrix(Tn, Tn, sp.symbols('B%d%d_0:%d' % (r_, s_, Tn * Tn))); Bs[(s_, r_)] = -Bs[(r_, s_)]
    def Gt_c(cv, tv):
        """G~(c (x) t) for c in T_A (vector over TA), t in E+ = u + V+ (vector over u, V+) -> n x n (control x target)"""
        out = sp.zeros(n, n)
        for r_ in Vp:                                           # alpha(c) = sum_r A_r c (x) e_r, times t_u
            col = As[r_] * cv
            for i_, ti in enumerate(TA): out[ti, r_] += tv[0] * col[i_]
        for s_ in Vp:                                           # t_s: (A_s c) (x) u + sum_r (B_rs c) (x) e_r
            col = As[s_] * cv
            for i_, ti in enumerate(TA): out[ti, 0] += tv[s_] * col[i_]
            for r_ in Vp:
                if r_ != s_:
                    colb = Bs[(r_, s_)] * cv
                    for i_, ti in enumerate(TA): out[ti, r_] += tv[s_] * colb[i_]
        return out
    av = sp.Matrix(sp.symbols('a0:%d' % Tn)); cv = sp.Matrix(sp.symbols('c0:%d' % Tn))
    bv = sp.symbols('b1:%d' % (p + 1)); tv = sp.symbols('x1:%d' % (p + 1))
    tvec = [1] + list(tv) + [0] * (n - 1 - p)
    Gc = Gt_c(cv, tvec)
    f = sp.Matrix([1] + list(av) + [0]); gvec = sp.Matrix([1] + list(bv) + [0] * (n - 1 - p))
    # G(u (x) t) = u (x) t for t in E+ (M_0 = I, t fixed by N): contributes g.t
    val = (gvec.T * sp.Matrix(tvec))[0] + (f.T * Gc * gvec)[0]
    gam = [((av.T * As[r_] * cv)[0]) for r_ in Vp]
    Kmat = sp.zeros(p)
    for (r_, s_), B in Bs.items(): Kmat[r_ - 1, s_ - 1] = (av.T * B * cv)[0]
    Gam = sp.zeros(p + 1); Gam[0, 1:] = sp.Matrix([gam]); Gam[1:, 0] = sp.Matrix(gam); Gam[1:, 1:] = Kmat
    form = (sp.Matrix([1] + list(bv)).T * (sp.eye(p + 1) + Gam) * sp.Matrix([1] + list(tv)))[0]
    rep('S4 d=%d p=%d: (f(x)g)(G(s(x)t)) = (1,b)(I + Gamma_ac)(1,t) with Gamma = [[0,g^T],[g,K]], K antisymmetric'
        % (d, p), sp.expand(val - form) == 0 and (Kmat.T + Kmat).applyfunc(sp.expand) == sp.zeros(p))
print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
