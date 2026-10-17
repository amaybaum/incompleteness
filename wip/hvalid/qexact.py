"""Exact Q(i) linear algebra and the kernel's pair vocabulary (EqvK2Schema / CompositeDimension /
EffectSpace at origin/main 66a981d5), transcribed independently.  Standard library only."""
from fractions import Fraction as Fr
from itertools import combinations, permutations, product

class G:
    __slots__ = ("re", "im")
    def __init__(self, re=0, im=0):
        self.re = Fr(re); self.im = Fr(im)
    def __add__(s, o): o = cg(o); return G(s.re + o.re, s.im + o.im)
    __radd__ = __add__
    def __sub__(s, o): o = cg(o); return G(s.re - o.re, s.im - o.im)
    def __rsub__(s, o): return cg(o) - s
    def __mul__(s, o): o = cg(o); return G(s.re*o.re - s.im*o.im, s.re*o.im + s.im*o.re)
    __rmul__ = __mul__
    def __neg__(s): return G(-s.re, -s.im)
    def conj(s): return G(s.re, -s.im)
    def n2(s): return s.re*s.re + s.im*s.im
    def __truediv__(s, o):
        o = cg(o); d = o.n2()
        if d == 0: raise ZeroDivisionError
        p = s * o.conj(); return G(p.re/d, p.im/d)
    def __eq__(s, o): o = cg(o); return s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def iszero(s): return s.re == 0 and s.im == 0
    def __repr__(s):
        if s.im == 0: return str(s.re)
        return f"({s.re}{'+' if s.im >= 0 else ''}{s.im}i)"

def cg(x): return x if isinstance(x, G) else G(x, 0)
I_ = G(0, 1)

def zeros(n, m=None): m = n if m is None else m; return [[G() for _ in range(m)] for _ in range(n)]
def eye(n): M = zeros(n); [M[i].__setitem__(i, G(1)) for i in range(n)]; return M
def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t]*B[t][j] for t in range(k)), G()) for j in range(m)] for i in range(n)]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msc(c, A): return [[cg(c)*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def tr(A): return sum((A[i][i] for i in range(len(A))), G())
def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n*m)] for i in range(n*m)]
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def is_herm(A): return meq(A, dag(A))

def det(A):
    n = len(A); M = [row[:] for row in A]; d = G(1)
    for c in range(n):
        p = next((r for r in range(c, n) if not M[r][c].iszero()), None)
        if p is None: return G(0)
        if p != c: M[c], M[p] = M[p], M[c]; d = -d
        d = d * M[c][c]
        for r in range(c+1, n):
            f = M[r][c] / M[c][c]
            if not f.iszero():
                M[r] = [M[r][j] - f*M[c][j] for j in range(n)]
    return d

def inv(A):
    n = len(A); M = [A[i][:] + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if not M[r][c].iszero())
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and not M[r][c].iszero():
                f = M[r][c]; M[r] = [M[r][j] - f*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def is_psd(H):
    """Exact: a Hermitian matrix is PSD iff every principal minor is >= 0."""
    assert is_herm(H)
    n = len(H)
    for k in range(1, n+1):
        for S in combinations(range(n), k):
            d = det([[H[i][j] for j in S] for i in S])
            assert d.im == 0
            if d.re < 0: return False
    return True

def charpoly(H):
    """Faddeev-LeVerrier, exact: coefficients [1, c1, ..., cn] of det(tI - H)."""
    n = len(H); c = [G(1)]; Mk = zeros(n)
    for k in range(1, n+1):
        Mk = madd(mmul(H, Mk), msc(c[-1], eye(n)))
        c.append(msc(Fr(-1, k), [[tr(mmul(H, Mk))]])[0][0])
    return c

# ---------------------------------------------------------------- the kernel's pair vocabulary
PAULI = [ [[G(1),G(0)],[G(0),G(1)]],
          [[G(0),G(1)],[G(1),G(0)]],
          [[G(0),G(0,-1)],[G(0,1),G(0)]],
          [[G(1),G(0)],[G(0),G(-1)]] ]          # EqvK2Schema.lean:25-26
PT = [[kron(PAULI[m], PAULI[n]) for n in range(4)] for m in range(4)]

def dict_(w, scale=Fr(1, 4)):
    """EqvK2Schema.lean:78: dict w = sum (w_mn / 4) sigma_m (x) sigma_n, basis (a1,a2) -> 2*a1+a2."""
    M = zeros(4)
    for m in range(4):
        for n in range(4):
            if w[m][n] != 0: M = madd(M, msc(G(Fr(w[m][n]))*scale, PT[m][n]))
    return M

def coordOf(H):
    """EqvK2Schema.lean:157: coordOf H = Re tr((sigma_m (x) sigma_n) H)."""
    out = [[Fr(0)]*4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            t = tr(mmul(PT[m][n], H)); assert t.im == 0; out[m][n] = t.re
    return out

def hom(x): return [Fr(1)] + [Fr(c) for c in x]                     # CompositeDimension.lean:100
def prodState(x, y): hx, hy = hom(x), hom(y); return [[hx[m]*hy[n] for n in range(4)] for m in range(4)]
def pairVal(a, b, w): return sum(a[m]*w[m][n]*b[n] for m in range(4) for n in range(4))  # :164
def sharpVec(b): return [Fr(1, 2)] + [Fr(c)/2 for c in b]            # EffectSpace.lean:57
UNIT = [Fr(1), Fr(0), Fr(0), Fr(0)]                                  # ehom of the unit effect
def eff_at(ehat, x): return ehat[0] + sum(ehat[j+1]*Fr(x[j]) for j in range(3))
def lor(v): return v[0] >= 0 and v[1]**2 + v[2]**2 + v[3]**2 <= v[0]**2   # CompositeDimension.lean:869

def margA(w): return [w[m][0] for m in range(4)]   # pairing with the unit on the target index
def margB(w): return [w[0][n] for n in range(4)]
def mv_ok(w): return lor(margA(w)) and lor(margB(w))

def ptrace_B(H):
    return [[H[2*a][2*b] + H[2*a+1][2*b+1] for b in range(2)] for a in range(2)]
def ptrace_A(H):
    return [[H[a][b] + H[2+a][2+b] for b in range(2)] for a in range(2)]

def A2(H):
    """Additive compound on the antisymmetric square: eigenvalues lambda_a + lambda_b, a < b."""
    pairs = list(combinations(range(len(H)), 2))
    M = zeros(len(pairs))
    for r, (i, j) in enumerate(pairs):
        for c, (k, l) in enumerate(pairs):
            v = G()
            if j == l: v = v + H[i][k]
            if i == k: v = v + H[j][l]
            if j == k: v = v - H[i][l]
            if i == l: v = v - H[j][k]
            M[r][c] = v
    return M

def in_Q3(w): return is_psd(dict_(w))
def in_K2(w): return is_psd(A2(dict_(w)))

def rat_sphere(u, v):
    u, v = Fr(u), Fr(v); d = u*u + v*v + 1
    return [2*u/d, 2*v/d, (u*u + v*v - 1)/d]

def cayley(A):
    """U = (I - iA)(I + iA)^{-1} for Hermitian A: an exact unitary over Q(i)."""
    n = len(A); iA = msc(I_, A)
    return mmul(msub(eye(n), iA), inv(madd(eye(n), iA)))

def conj_by(U, H): return mmul(mmul(U, H), dag(U))
def perm_matrix(p):
    n = len(p); M = zeros(n)
    for j in range(n): M[p[j]][j] = G(1)
    return M
def diagm(vals):
    M = zeros(len(vals))
    for i, v in enumerate(vals): M[i][i] = G(Fr(v))
    return M
