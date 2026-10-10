"""K2C exact helpers (sympy rationals / Gaussian rationals / python ints only; no floats as evidence).

Independent re-implementation (does not import k2d/k2lib.py; probe P1 cross-checks against it).
Conventions read from the kernel (CompositeDimension.lean at base 68b6df06):
  W 3 = Fin 4 -> Fin 4 -> R, index 0 = unit, 1,2,3 = coordinates 0,1,2 of the ball (Bloch x, y, z);
  hom x = vecCons 1 x;  homMap N v = vecCons (v 0) (N (vecTail v))  [matrix H(N) = diag(1, N)];
  prodState x y mu nu = hom x mu * hom y nu;  pairVal a b w = sum a_mu w_mu_nu b_nu;
  actT N w mu = homMap N (w mu)          [target = second index];
  actC N w mu nu = homMap N (w . nu) mu  [control = first index];
  cnotFun w mu nu = sgn mu nu * w (pc mu nu) (pt mu nu)  (tables parsed from the Lean file).
Vectorisation: vec(w)[4*mu + nu] = w[mu][nu].
Matrix-model dictionary (evidence layer [M], not kernel): w_mu_nu = Tr((s_mu (x) s_nu) rho).
"""
import itertools
import re
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, SX, SY, SZ]


def kron(a, b):
    return sp.kronecker_product(a, b)


# ---------------------------------------------------------------- kernel parsing (no transcription)
def _block(src, header):
    i = src.index(header)
    j = src.index('\n\n', i)
    return src[i:j]


def parse_tables(lean_path):
    src = open(lean_path, encoding='utf-8').read()
    tabs = {}
    for name in ('pc', 'pt'):
        body = _block(src, 'def ' + name + ' :')
        t = {}
        for a, b, c in re.findall(r'\|\s*(\d)\s*,\s*(\d)\s*=>\s*(\d)', body):
            t[(int(a), int(b))] = int(c)
        assert len(t) == 16, (name, len(t))
        tabs[name] = t
    line = src[src.index('def sgn'):].split('\n')[0]
    neg = {(int(a), int(b)) for a, b in re.findall(r'μ = (\d) ∧ ν = (\d)', line)}
    assert 'then -1 else 1' in line, line
    tabs['neg'] = neg
    return tabs


def parse_diag_map(lean_path, name):
    """Parse `def name : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where toFun x := fun i => (![a, b, c] ...) i * x i`."""
    src = open(lean_path, encoding='utf-8').read()
    i = src.index('def ' + name + ' :')
    seg = src[i:i + 400]
    m = re.search(r'toFun x := fun i => \(!\[([^\]]*)\]', seg)
    assert m, name
    vals = [sp.Integer(int(s.strip())) for s in m.group(1).split(',')]
    assert 'i * x i' in seg[m.end():m.end() + 60], name
    return sp.diag(*vals)


# ---------------------------------------------------------------- DIM-1 objects as exact matrices
def vec(om):
    return sp.Matrix([om[m, v] for m in range(4) for v in range(4)])


def unvec(w):
    return sp.Matrix(4, 4, lambda m, v: w[4 * m + v])


def hom(x):
    return sp.Matrix([1] + list(x))


def prod_W(x, y):
    return hom(x) * hom(y).T


def pairval(a, b, om):
    return sp.expand((sp.Matrix(a).T * om * sp.Matrix(b))[0, 0])


def Hmat(N):
    """homMap N as a 4x4 matrix: diag(1, N)."""
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:, 1:] = N
    return H


def homMap_fun(N, v):
    """Literal transcription of the kernel definition: vecCons (v 0) (N (vecTail v))."""
    tail = sp.Matrix(v[1:])
    return sp.Matrix([v[0]] + list(N * tail))


def actT_fun(N, om):
    """actT N w mu = homMap N (w mu) -- row mu transformed (literal)."""
    rows = [homMap_fun(N, [om[m, k] for k in range(4)]) for m in range(4)]
    return sp.Matrix(4, 4, lambda m, v: rows[m][v])


def actC_fun(N, om):
    """actC N w mu nu = homMap N (fun k => w k nu) mu -- column nu transformed (literal)."""
    cols = [homMap_fun(N, [om[k, v] for k in range(4)]) for v in range(4)]
    return sp.Matrix(4, 4, lambda m, v: cols[v][m])


def actT_mat(N):
    H = Hmat(N)
    M = sp.zeros(16, 16)
    for m in range(4):
        for v in range(4):
            for l in range(4):
                M[4 * m + v, 4 * m + l] += H[v, l]
    return M


def actC_mat(N):
    H = Hmat(N)
    M = sp.zeros(16, 16)
    for m in range(4):
        for v in range(4):
            for k in range(4):
                M[4 * m + v, 4 * k + v] += H[m, k]
    return M


def cnot_fun(tabs, om):
    pc, pt, neg = tabs['pc'], tabs['pt'], tabs['neg']
    return sp.Matrix(4, 4, lambda m, v: (-1 if (m, v) in neg else 1) * om[pc[(m, v)], pt[(m, v)]])


def cnot_mat(tabs):
    pc, pt, neg = tabs['pc'], tabs['pt'], tabs['neg']
    M = sp.zeros(16, 16)
    for m in range(4):
        for v in range(4):
            M[4 * m + v, 4 * pc[(m, v)] + pt[(m, v)]] = -1 if (m, v) in neg else 1
    return M


def sharpVec(b):
    """EffectSpace.sharpVec: vecCons (1/2) (b/2)."""
    return sp.Matrix([sp.Rational(1, 2)] + [sp.Rational(1, 2) * bi for bi in b])


# ---------------------------------------------------------------- matrix model [M]
def q_of(rho):
    return sp.Matrix(4, 4, lambda m, v: sp.expand(sp.simplify((kron(PAULI[m], PAULI[v]) * rho).trace())))


def rho_of(om):
    r = sp.zeros(4, 4)
    for m in range(4):
        for v in range(4):
            r += om[m, v] * kron(PAULI[m], PAULI[v])
    return r / 4


def ptm(U, scale=1):
    """Transfer matrix of rho -> U rho U^H in W coordinates, divided by `scale`."""
    M = sp.zeros(16, 16)
    for (m, v) in itertools.product(range(4), repeat=2):
        A = (kron(PAULI[m], PAULI[v]) * U)
        for (k, l) in itertools.product(range(4), repeat=2):
            val = (A * kron(PAULI[k], PAULI[l]) * U.H).trace() / 4 / scale
            M[4 * m + v, 4 * k + l] = sp.simplify(sp.expand(val))
    return M


def quat_U(q):
    """Unnormalised SU(2) element U~ = q0 I - i (q1 X + q2 Y + q3 Z);  U~ U~^H = |q|^2 I."""
    q0, q1, q2, q3 = q
    return q0 * I2 - sp.I * (q1 * SX + q2 * SY + q3 * SZ)


def quat_R(q):
    """Bloch rotation of U~: R_ij = Tr(s_i U~ s_j U~^H) / (2 |q|^2), so U~ (x.s) U~^H = |q|^2 (R x).s."""
    U = quat_U(q)
    n = sum(qi ** 2 for qi in q)
    S3 = [SX, SY, SZ]
    return sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.expand((S3[i] * U * S3[j] * U.H).trace()) / (2 * n)))


def realify(M):
    """Complex n x n -> real 2n x 2n: v^H M v = [u;w]^T realify(M) [u;w] for Hermitian M, v = u + i w."""
    n = M.shape[0]
    R = sp.zeros(2 * n, 2 * n)
    for i in range(n):
        for j in range(n):
            re_, im_ = sp.re(sp.expand(M[i, j])), sp.im(sp.expand(M[i, j]))
            R[i, j] = re_
            R[n + i, n + j] = re_
            R[i, n + j] = -im_
            R[n + i, j] = im_
    return R


def S_of(om):
    """The real 8x8 symmetric matrix whose PSD-ness is PSD-ness of rho(om)."""
    return realify(rho_of(om))


def is_psd_exact(A):
    """Exact PSD test for a real symmetric matrix with exact entries (all principal minors >= 0)."""
    n = A.shape[0]
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            d = sp.nsimplify(A.extract(list(S), list(S)).det())
            if not d >= 0:
                return False, (S, d)
    return True, None


def omega_symbols():
    return sp.Matrix(4, 4, lambda m, v: sp.Symbol('w%d%d' % (m, v), real=True))


# ---------------------------------------------------------------- reporting
CHECKS = []


def check(name, cond, detail=''):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(('PASS ' if cond else 'FAIL ') + name + ((' :: ' + str(detail)) if detail != '' else ''))
    return cond


def summary():
    nf = sum(1 for _, c in CHECKS if not c)
    print('SUMMARY: %d checks, %d failures' % (len(CHECKS), nf))
    return nf
