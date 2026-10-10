"""K2.0 (read-only, exact): the d = 3 solutions of NB-1's hypotheses, classified up to local relabelling.
Conditional on NB-1's S1/S2 structure (written proof; exact at d = 3 in the NB-1 probe).
Bloch coordinates (u, x, y, z); N = diag(1, 1, -1, -1); V+ = <x>, V- = <y, z>, T = <x, y>."""
import itertools, sympy as sp
kr = sp.kronecker_product
U, X, Y, Z = range(4)
def E(i, n=4):
    v = sp.zeros(n, 1); v[i] = 1; return v
def build(M0d, A, K):
    """M0d = (e1, e2): M0 = diag(1, e1, e2, 1); A, K: 2x2 matrices on T = <x, y> (index 0 -> x, 1 -> y)."""
    M0 = sp.diag(1, M0d[0], M0d[1], 1); N = sp.diag(1, 1, -1, -1); M1 = N * M0
    k0, k1 = E(U) + E(Z), E(U) - E(Z)
    G = sp.zeros(16, 16)
    for j in range(4):                       # control u and z columns from S1: G(k_a (x) t) = k_a (x) M_a t
        t = E(j)
        cu = (kr(k0, M0 * t) + kr(k1, M1 * t)) / 2; cz = (kr(k0, M0 * t) - kr(k1, M1 * t)) / 2
        G[:, U * 4 + j] = cu; G[:, Z * 4 + j] = cz
    Tb = [X, Y]
    for ci, c in enumerate(Tb):              # control in T: G(c (x) t) = Gt(c (x) M0 t)
        Ac = sum((A[r, ci] * E(Tb[r]) for r in range(2)), sp.zeros(4, 1))
        Kc = sum((K[r, ci] * E(Tb[r]) for r in range(2)), sp.zeros(4, 1))
        for j in range(4):
            tp = M0 * E(j)                    # t' = M0 t
            out = tp[U] * kr(Ac, E(X)) + tp[X] * kr(Ac, E(U)) + tp[Y] * kr(Kc, E(Z)) - tp[Z] * kr(Kc, E(Y))
            G[:, c * 4 + j] = out
    return G
N = sp.diag(1, 1, -1, -1); I4 = sp.eye(4)
IN, NI = kr(I4, N), kr(N, I4)
# 1. the relations on the general family
a = sp.symbols('a11 a12 a21 a22'); k = sp.symbols('k11 k12 k21 k22')
A = sp.Matrix(2, 2, a); K = sp.Matrix(2, 2, k)
for M0d in itertools.product((1, -1), repeat=2):
    G = build(M0d, A, K)
    rt = (IN * G * IN - G).applyfunc(sp.expand); rc = (NI * G * NI - IN * G).applyfunc(sp.expand)
    k0, k1 = E(U) + E(Z), E(U) - E(Z); kk = [k0, k1]
    fr = all(G * kr(kk[p], kk[q]) == kr(kk[p], kk[p ^ q]) for p in (0, 1) for q in (0, 1))
    eqs = set(e for e in list(rt) + list(rc) if e != 0)
    print('M0 =', M0d, 'frame', fr, '; Rt and Rc force:', sp.solve(list(eqs), list(a) + list(k), dict=True))
