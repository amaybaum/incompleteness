"""Thread D exact helpers (sympy rationals / Gaussian rationals / python ints; no float is evidence).

Self-contained: re-implements the few DIM-1 objects needed, parsing the gate tables from the base's
CompositeDimension.lean (no transcription of the tables).  Conventions (CompositeDimension.lean at
06b6f94e, unchanged since 68b6df06):
  W 3 = Fin 4 -> Fin 4 -> R, index 0 = unit, 1,2,3 = ball coordinates (Bloch x, y, z);
  prodState x y mu nu = hom x mu * hom y nu;  pairVal a b w = sum a_mu w_mu_nu b_nu;
  actT N acts on the second (target) index, actC N on the first (control) index;
  cnotFun w mu nu = sgn mu nu * w (pc mu nu) (pt mu nu).
Matrix-model dictionary (layer [M], not kernel): w_mu_nu = Tr((s_mu (x) s_nu) rho).
Two-qubit vector order |00>,|01>,|10>,|11> (first factor = control copy = first W index).
"""
import itertools
import re
import sympy as sp

I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
PAULI = [I2, SX, SY, SZ]
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def kron(a, b):
    return sp.kronecker_product(a, b)


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


def hom(x):
    return sp.Matrix([1] + list(x))


def prod_W(x, y):
    return hom(x) * hom(y).T


def pairval(a, b, om):
    return sp.expand((sp.Matrix(a).T * om * sp.Matrix(b))[0, 0])


def sharpVec(b):
    return sp.Matrix([sp.Rational(1, 2)] + [sp.Rational(1, 2) * bi for bi in b])


def vec(om):
    return sp.Matrix([om[m, v] for m in range(4) for v in range(4)])


def unvec(w):
    return sp.Matrix(4, 4, lambda m, v: w[4 * m + v])


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


def Hmat(N):
    H = sp.zeros(4, 4)
    H[0, 0] = 1
    H[1:, 1:] = N
    return H


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


# ---------------------------------------------------------------- matrix model [M]
def q_of(rho):
    return sp.Matrix(4, 4, lambda m, v: sp.expand((kron(PAULI[m], PAULI[v]) * rho).trace()))


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
            M[4 * m + v, 4 * k + l] = sp.nsimplify(sp.expand(val))
    return M


def quat_U(q):
    """Unnormalised SU(2) element U~ = q0 I - i (q1 X + q2 Y + q3 Z);  U~ U~^H = |q|^2 I."""
    q0, q1, q2, q3 = q
    return q0 * I2 - sp.I * (q1 * SX + q2 * SY + q3 * SZ)


def quat_R(q):
    U = quat_U(q)
    n = sum(qi ** 2 for qi in q)
    S3 = [SX, SY, SZ]
    return sp.Matrix(3, 3, lambda i, j: sp.expand((S3[i] * U * S3[j] * U.H).trace()) / (2 * n))


def is_gauss_rational(z):
    z = sp.expand(z)
    re_, im_ = sp.re(z), sp.im(z)
    return re_.is_rational is True and im_.is_rational is True


def segre(psi):
    """det of the 2x2 coefficient matrix [[p00, p01], [p10, p11]]: zero iff psi is a product (rank <= 1)."""
    return sp.expand(psi[0] * psi[3] - psi[1] * psi[2])


class Checks:
    def __init__(self, name):
        self.name = name
        self.n = 0
        self.fail = 0

    def check(self, tag, cond, detail=''):
        self.n += 1
        ok = bool(cond)
        if not ok:
            self.fail += 1
        print(('PASS ' if ok else 'FAIL ') + tag + ((' :: ' + detail) if detail else ''))
        return ok

    def note(self, text):
        print('     ' + text)

    def summary(self, verdict_ok, verdict_bad):
        print('---')
        print('%s: %d checks, %d failures' % (self.name, self.n, self.fail))
        print('VERDICT ' + (verdict_ok if self.fail == 0 else verdict_bad))
