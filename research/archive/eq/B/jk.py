"""EQ-B: the J/K flow G_t on W d (odd d), exact (Fraction) and symbolic (sympy) builders.

J/K data at odd d = 2m+1 (homogeneous indices 0 = u, 1 = x, d = z; tangent T = 1..d-1; E+ = {u, x}, E- = {2..d}):
  X : u <-> x on E+ ;  K : y=2 -> z=d -> -y,  (3 -> 4 -> -3), (5 -> 6 -> -5), ... on E-  (orthogonal complex structure);
  J : (1 -> 2 -> -1), (3 -> 4 -> -3), ... on T (orthogonal complex structure);  N = P+ - P-  (homogenised NOT).
At d = 5 this is the data of the landed gC5 (RelcSelectC5.lean doc comment, checked against its tables in b4).
Flow (c = cos t, s = sin t):
  G_t(hom z (x) Y)  = hom z (x) Y
  G_t(hom -z (x) Y) = hom -z (x) R_t Y,                R_t = P+ + c P- + s K P-
  G_t(c' (x) Y)     = c' (x) A_t Y + J c' (x) B_t Y   (c' in T),
     A_t = (1+c)/2 I + (1-c)/2 X P+ + (s/2) K P-,
     B_t = (s/2)(P+ - X P+) + (s/2) P- + (1-c)/2 K P-.
"""
from fractions import Fraction as Fr


def jk_mats(d, one=Fr(1), zero=Fr(0)):
    n = d + 1
    Z = lambda: [[zero] * n for _ in range(n)]
    X = Z(); X[0][1] = one; X[1][0] = one
    K = Z(); K[d][2] = one; K[2][d] = -one
    for a in range(3, d - 1, 2):
        K[a + 1][a] = one; K[a][a + 1] = -one
    J = Z()
    for a in range(1, d - 1, 2):
        J[a + 1][a] = one; J[a][a + 1] = -one
    Pp = Z(); Pp[0][0] = one; Pp[1][1] = one
    Pm = Z()
    for i in range(2, n):
        Pm[i][i] = one
    return X, K, J, Pp, Pm


def mm(A, B, zero):
    n, k, m = len(A), len(B), len(B[0])
    out = [[zero] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            a = A[i][t]
            if a == 0:
                continue
            for j in range(m):
                b = B[t][j]
                if b == 0:
                    continue
                out[i][j] = out[i][j] + a * b
    return out


def lin(coeffs, mats, zero):
    n = len(mats[0])
    out = [[zero] * n for _ in range(n)]
    for c, M in zip(coeffs, mats):
        for i in range(n):
            for j in range(n):
                if M[i][j] != 0:
                    out[i][j] = out[i][j] + c * M[i][j]
    return out


def flow_blocks(d, c, s, one=Fr(1), zero=Fr(0), half=Fr(1, 2)):
    X, K, J, Pp, Pm = jk_mats(d, one, zero)
    n = d + 1
    I = [[one if i == j else zero for j in range(n)] for i in range(n)]
    XP = mm(X, Pp, zero)
    KP = mm(K, Pm, zero)
    R = lin([one, c, s], [Pp, Pm, KP], zero)
    A = lin([(one + c) * half, (one - c) * half, s * half], [I, XP, KP], zero)
    B = lin([s * half, -s * half, s * half, (one - c) * half], [Pp, XP, Pm, KP], zero)
    return R, A, B, J


def flow_op(d, c, s, one=Fr(1), zero=Fr(0), half=Fr(1, 2)):
    """n^2 x n^2 operator of G_t on vec(W) (row-major), entries in the coefficient ring."""
    n = d + 1
    R, A, B, J = flow_blocks(d, c, s, one, zero, half)
    G = [[zero] * (n * n) for _ in range(n * n)]
    # control basis decomposition: e0 = (hz + hmz)/2, e_d = (hz - hmz)/2, tangent e_k (k = 1..d-1)
    for mu in range(n):
        for nu in range(n):
            col = mu * n + nu
            out = [[zero] * n for _ in range(n)]
            Y = [one if j == nu else zero for j in range(n)]
            RY = [sum((R[i][j] * Y[j] for j in range(n)), zero) for i in range(n)]
            AY = [sum((A[i][j] * Y[j] for j in range(n)), zero) for i in range(n)]
            BY = [sum((B[i][j] * Y[j] for j in range(n)), zero) for i in range(n)]
            if mu in (0, d):
                sg = one if mu == 0 else -one
                hz = [zero] * n; hz[0] = one; hz[d] = one
                hmz = [zero] * n; hmz[0] = one; hmz[d] = -one
                # e0 = (hz + hmz)/2 ; e_d = (hz - hmz)/2
                for i in range(n):
                    for j in range(n):
                        out[i][j] = half * hz[i] * Y[j] + sg * half * hmz[i] * RY[j]
            else:
                cvec = [zero] * n; cvec[mu] = one
                Jc = [sum((J[i][j] * cvec[j] for j in range(n)), zero) for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        out[i][j] = cvec[i] * AY[j] + Jc[i] * BY[j]
            for i in range(n):
                for j in range(n):
                    G[i * n + j][col] = out[i][j]
    return G
