"""REL-T thread, shared exact helpers (sympy Rational / exact symbolic only; no floats).

Conventions mirror OIBridge.CompositeDimension at L = e2426ba4:
  * HVec d = R^{d+1}, index 0 the unit, index j+1 coordinate j; hom x = (1, x).
  * W d = (d+1)x(d+1) real matrices omega[mu][nu], mu = control index, nu = target index.
  * prodState x y = hom x * hom y^T ;  tens X Y = X Y^T.
  * homMap N = 1 (+) N ;  actT N omega = omega * homMap(N)^T (row mu -> homMap N (omega mu));
    actC N omega = homMap(N) * omega.
  * pairVal a b omega = a^T omega b.
  * NativeGate.frame : G(prod(corner z a, corner z b)) = prod(corner z a, corner z (a+b)), corner z 0 = z, 1 = -z.
  * relT : actT N (G (actT N w)) = G w ;  relC : actC N (G (actC N w)) = actT N (G w).
A gate is stored as an n^2 x n^2 matrix acting on vec(omega) (row-major, index mu*n+nu).
"""
from sympy import Matrix, Rational, eye, zeros, diag, sqrt, symbols, expand, simplify

R = Rational


def hom(x):
    return Matrix([1] + list(x))


def homMap(N):
    n = N.shape[0] + 1
    H = zeros(n, n)
    H[0, 0] = 1
    H[1:, 1:] = N
    return H


def vec(w):
    n = w.shape[0]
    return Matrix([w[i, j] for i in range(n) for j in range(n)])


def unvec(v, n):
    return Matrix(n, n, lambda i, j: v[i * n + j])


def gate_from_fun(fun, n):
    """matrix of a linear map on W given as a python function on n x n matrices"""
    cols = []
    for k in range(n * n):
        E = zeros(n, n)
        E[k // n, k % n] = 1
        cols.append(vec(fun(E)))
    return Matrix.hstack(*cols)


def apply(G, w):
    return unvec(G * vec(w), w.shape[0])


def actT_mat(N):
    n = N.shape[0] + 1
    Nh = homMap(N)
    return gate_from_fun(lambda w: w * Nh.T, n)


def actC_mat(N):
    n = N.shape[0] + 1
    Nh = homMap(N)
    return gate_from_fun(lambda w: Nh * w, n)


def corner(z, a):
    return z if a % 2 == 0 else -z


def prod(x, y):
    return hom(x) * hom(y).T


# ---------------- the hypotheses -----------------

def isNot(z, N):
    """IsNot (eball d) z N, exact: unit, involution, preserves the ball (N orthogonal suffices;
    for a linear involution preserving the ball orthogonality is also necessary, CompositeDimension §E),
    flips."""
    d = N.shape[0]
    unit = sum(zi ** 2 for zi in z) == 1
    invol = (N * N - eye(d)).is_zero_matrix
    orth = (N.T * N - eye(d)).is_zero_matrix
    flips = (N * z + z).is_zero_matrix
    return dict(unit=unit, invol=invol, preserves_via_orthogonal=orth, flips=flips)


def frame(G, z):
    n = z.shape[0] + 1
    ok = True
    for a in range(2):
        for b in range(2):
            lhs = apply(G, prod(corner(z, a), corner(z, b)))
            rhs = prod(corner(z, a), corner(z, a + b))
            ok = ok and (lhs - rhs).is_zero_matrix
    return ok


def relT(G, N):
    T = actT_mat(N)
    return (T * G * T - G).is_zero_matrix


def relC(G, N):
    T = actT_mat(N)
    C = actC_mat(N)
    return (C * G * C - T * G).is_zero_matrix


def invertible(G):
    return G.det() != 0


def eig_dims(N):
    """(dim +1 eigenspace, dim -1 eigenspace) of homMap N"""
    Nh = homMap(N)
    n = Nh.shape[0]
    plus = n - (Nh - eye(n)).rank()
    minus = n - (Nh + eye(n)).rank()
    return plus, minus


def pairVal(a, b, w):
    return (a.T * w * b)[0, 0]


def lor(v):
    """the cone Lor of CompositeDimension: v0 >= 0 and |tail|^2 <= v0^2 (exact)"""
    return v[0] >= 0 and sum(v[i] ** 2 for i in range(1, v.shape[0])) <= v[0] ** 2


def sharpVec(b):
    return Matrix([R(1, 2)] + [bi / 2 for bi in b])


# ---------------- the parity map of CompositeDimension §H-§I, exactly -----------------

def parity_map_data(G, N):
    """Returns (injective?, anti?) for Lop G and Pop N on OpSpace N = Hom(minusSpace N, HVec d),
    built exactly as in CompositeDimension: Lop f = (opGate G (f o projMinus)) restricted to minusSpace,
    opGate G F = toOp (G (fromOp F)), toOp w = the matrix w; Pop f = homMap N o f."""
    Nh = homMap(N)
    n = Nh.shape[0]
    Bm = Matrix.hstack(*(Nh + eye(n)).nullspace())  # basis of minusSpace, n x k
    k = Bm.shape[1]
    Pm = (eye(n) - Nh) / 2  # projMinus as an operator on HVec (values in minusSpace)
    # coordinates map C with Bm*C = Pm  (Bm full column rank)
    C = (Bm.T * Bm).inv() * Bm.T * Pm
    assert (Bm * C - Pm).is_zero_matrix
    dimOp = n * k
    def Lop(F):  # F: n x k matrix representing f (f(Bm c) = F c)
        full = F * C  # f o projMinus as n x n operator
        out = apply(G, full)  # toOp (G (fromOp full)) as a matrix
        return out * Bm  # restriction to minusSpace
    def Pop(F):
        return Nh * F
    def basisF(i):
        E = zeros(n, k)
        E[i // k, i % k] = 1
        return E
    def flat(F):
        return Matrix([F[i, j] for i in range(n) for j in range(k)])
    Lmat = Matrix.hstack(*[flat(Lop(basisF(i))) for i in range(dimOp)])
    Pmat = Matrix.hstack(*[flat(Pop(basisF(i))) for i in range(dimOp)])
    injective = Lmat.rank() == dimOp
    anti = (Lmat * Pmat + Pmat * Lmat).is_zero_matrix
    return dict(dimOp=dimOp, injective=injective, anti=anti,
                ker_P_minus_1=dimOp - (Pmat - eye(dimOp)).rank(),
                ker_P_plus_1=dimOp - (Pmat + eye(dimOp)).rank())


# ---------------- the controlled-N gate (the REL-T countermodel family) -----------------

def controlled_N_gate(z, N):
    """G = Pi_a (x) I + Pi_b (x) homMap N, Pi_a = 1/2 hom z hom z^T, Pi_b = I - Pi_a.
    On matrices: G(w) = Pi_a w + Pi_b w homMap(N)^T."""
    n = z.shape[0] + 1
    hz = hom(z)
    Pa = hz * hz.T / 2
    Pb = eye(n) - Pa
    Nh = homMap(N)
    return gate_from_fun(lambda w: Pa * w + Pb * w * Nh.T, n), Pa, Pb


# ---------------- DIM-1's cnot at d = 3 (positive control), transcribed from §K -----------------

def dim1_cnot():
    sgn = lambda m, v: -1 if (m == 1 and v == 3) or (m == 2 and v == 2) else 1
    pc = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
    pt = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
    def f(w):
        return Matrix(4, 4, lambda m, v: sgn(m, v) * w[pc[m][v], pt[m][v]])
    return gate_from_fun(f, 4)


def sgate(odd, p, n):
    """PARITY-NOT-1's sign-free permutation gate"""
    def f(w):
        return Matrix(n, n, lambda m, v: w[p[m], v] if odd[v] else w[m, v])
    return gate_from_fun(f, n)


def diagN(signs):
    return diag(*signs)


def col(*xs):
    return Matrix(list(xs))
