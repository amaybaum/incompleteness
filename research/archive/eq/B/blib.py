"""EQ-B exact carrier library.

Mirrors the landed Lean definitions of OIBridge.CompositeDimension / RelcSelect (base bcbc516f):
  HVec d = Fin (d+1) -> R  (index 0 = unit), W d = (d+1) x (d+1) real matrices (control row, target column),
  hom x = (1, x), homMap N = 1 (+) N, prodState x y = hom x hom y^T,
  actT N w = w Ntil^T   (each row mapped by Ntil = homMap N),    i.e. operator I (x) Ntil on vec(w),
  actC N w = Ntil w     (each column mapped by Ntil),            i.e. operator Ntil (x) I on vec(w),
  pairVal a b w = a^T w b,  Lor v : v0 >= 0 and sum_{j>=1} v_j^2 <= v0^2.
A linear map of W d is an n^2 x n^2 matrix (n = d+1) acting on vec(w) with row-major index mu*n+nu.

Exact arithmetic: Fraction everywhere. No floats are used for any verdict.
"""
from fractions import Fraction as Fr
from itertools import product


# ---------------------------------------------------------------- small exact linear algebra
def zeros(r, c):
    return [[Fr(0)] * c for _ in range(r)]


def eye(n):
    m = zeros(n, n)
    for i in range(n):
        m[i][i] = Fr(1)
    return m


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    b = Bt[j]
                    if b:
                        oi[j] += a * b
    return out


def matvec(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v)) if A[i][j] and v[j]), Fr(0)) for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def madd(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c * x for x in r] for r in A]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    out = zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            a = A[i][j]
            if a:
                for k in range(rb):
                    for l in range(cb):
                        b = B[k][l]
                        if b:
                            out[i * rb + k][j * cb + l] = a * b
    return out


def rank(A):
    M = [list(r) for r in A]
    if not M:
        return 0
    rows, cols = len(M), len(M[0])
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / pv
                Mi, Mr = M[i], M[r]
                for j in range(c, cols):
                    if Mr[j]:
                        Mi[j] -= f * Mr[j]
        r += 1
        if r == rows:
            break
    return r


def inverse(A):
    n = len(A)
    M = [list(A[i]) + [Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next((i for i in range(c, n) if M[i][c] != 0), None)
        if piv is None:
            raise ValueError("singular")
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[c][j] for j in range(2 * n)]
    return [r[n:] for r in M]


def nullspace(A):
    """Exact basis of {v : A v = 0} (columns returned as lists)."""
    M = [list(r) for r in A]
    rows, cols = len(M), len(M[0])
    pivcols = []
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(cols)]
        pivcols.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in pivcols]
    basis = []
    for f in free:
        v = [Fr(0)] * cols
        v[f] = Fr(1)
        for i, pc in enumerate(pivcols):
            v[pc] = -M[i][f]
        basis.append(v)
    return basis


# ---------------------------------------------------------------- the carrier
def homvec(x):
    return [Fr(1)] + [Fr(t) for t in x]


def liftvec(c):
    return [Fr(0)] + [Fr(t) for t in c]


def homMap(N):
    """N: d x d matrix (list of lists) -> (d+1) x (d+1) homogenized map 1 (+) N."""
    d = len(N)
    H = zeros(d + 1, d + 1)
    H[0][0] = Fr(1)
    for i in range(d):
        for j in range(d):
            H[i + 1][j + 1] = Fr(N[i][j])
    return H


def diag(signs):
    n = len(signs)
    m = zeros(n, n)
    for i, s in enumerate(signs):
        m[i][i] = Fr(s)
    return m


def outer(a, b):
    return [[Fr(x) * Fr(y) for y in b] for x in a]


def vecW(w):
    return [x for r in w for x in r]


def unvecW(v, n):
    return [list(v[i * n:(i + 1) * n]) for i in range(n)]


def apply(G, w):
    n = len(w)
    return unvecW(matvec(G, vecW(w)), n)


def prodState(x, y):
    return outer(homvec(x), homvec(y))


def pairVal(a, b, w):
    return sum((Fr(a[m]) * w[m][n] * Fr(b[n]) for m in range(len(a)) for n in range(len(b))), Fr(0))


def isLor(v):
    return v[0] >= 0 and sum(t * t for t in v[1:]) <= v[0] * v[0]


def actT_op(Nt):
    """actT N as an operator on vec(W): I (x) Ntil."""
    return kron(eye(len(Nt)), Nt)


def actC_op(Nt):
    """actC N as an operator on vec(W): Ntil (x) I."""
    return kron(Nt, eye(len(Nt)))


def signed_perm_op(n, sgn, pc, pt):
    """(G w)(mu, nu) = sgn(mu,nu) * w(pc(mu,nu), pt(mu,nu)) as an n^2 x n^2 operator."""
    G = zeros(n * n, n * n)
    for mu in range(n):
        for nu in range(n):
            G[mu * n + nu][pc(mu, nu) * n + pt(mu, nu)] = Fr(sgn(mu, nu))
    return G


# ---------------------------------------------------------------- the landed witnesses (transcribed)
def cnot3():
    """CompositeDimension.cnot (CompositeDimension.lean:741-786)."""
    sg = lambda m, n: -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1
    PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
    PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
    return signed_perm_op(4, sg, lambda m, n: PC[m][n], lambda m, n: PT[m][n])


def nflip():
    """CompositeDimension.nflip: diag(1,-1,-1) on Fin 3; axis z3 = (0,0,1)."""
    return diag([1, -1, -1])


Z3 = [0, 0, 1]


def cnot1():
    """CompositeDimension.cnot1: (G w)(mu,nu) = w(mu+nu mod 2, nu)."""
    return signed_perm_op(2, lambda m, n: 1, lambda m, n: (m + n) % 2, lambda m, n: n)


def neg1():
    return diag([-1])


Z1 = [1]


def gC5():
    """RelcSelect.gC5 (RelcSelectC5.lean:89-145)."""
    def sg(m, n):
        return -1 if ((m in (1, 3)) and (n in (4, 5))) or ((m in (2, 4)) and (n in (2, 3))) else 1
    PC = [[0, 0, 5, 5, 5, 5], [1, 1, 2, 2, 2, 2], [2, 2, 1, 1, 1, 1],
          [3, 3, 4, 4, 4, 4], [4, 4, 3, 3, 3, 3], [5, 5, 0, 0, 0, 0]]
    PT = [[0, 1, 2, 3, 4, 5], [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2],
          [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2], [0, 1, 2, 3, 4, 5]]
    return signed_perm_op(6, sg, lambda m, n: PC[m][n], lambda m, n: PT[m][n])


def nC5():
    """RelcSelect.nC5 = diag(1,-1,-1,-1,-1) on Fin 5 (oddC5: hom indices 2..5 negative)."""
    return diag([1, -1, -1, -1, -1])


Z5 = [0, 0, 0, 0, 1]   # ParityNot.z5: the last coordinate (hom index 5)


def entW(n, i, j):
    w = zeros(n, n)
    w[i][j] = Fr(1)
    return w
