"""Exact helpers for the K2 ledger probes (sympy rationals / Gaussian rationals only; no floats).

Conventions follow CompositeDimension.lean: index 0 = unit, 1,2,3 = Bloch x,y,z.
W-coordinates of a 4x4 two-qubit operator rho: omega[mu][nu] = Tr((s_mu (x) s_nu) rho).
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


def W_of(rho, basis=PAULI):
    n = len(basis)
    return sp.Matrix(n, n, lambda m, v: sp.nsimplify(sp.simplify((kron(basis[m], basis[v]) * rho).trace())))


def rho_of_W(om, basis=PAULI):
    n = len(basis)
    r = sp.zeros(4, 4)
    for m in range(n):
        for v in range(n):
            r += om[m, v] * kron(basis[m], basis[v])
    return r / 4


def hom(x):
    return sp.Matrix([1] + list(x))


def prod_W(x, y):
    return hom(x) * hom(y).T


def pairval(a, b, om):
    return (a.T * om * b)[0, 0]


def ad(U):
    """Linear map rho -> U rho U^dagger, as a function."""
    return lambda r: U * r * U.H


def ptm(U, basis=PAULI):
    """Transfer matrix of Ad(U) in W-coordinates: (mu nu),(ka la) -> Tr((s_mu s_nu) U (s_ka s_la) U^H)/4."""
    n = len(basis)
    M = sp.zeros(n * n, n * n)
    for (m, v) in itertools.product(range(n), repeat=2):
        for (k, l) in itertools.product(range(n), repeat=2):
            val = (kron(basis[m], basis[v]) * U * kron(basis[k], basis[l]) * U.H).trace() / 4
            M[m * n + v, k * n + l] = sp.nsimplify(sp.simplify(val))
    return M


def vec(om):
    n = om.shape[0]
    return sp.Matrix([om[m, v] for m in range(n) for v in range(n)])


def unvec(w, n=4):
    return sp.Matrix(n, n, lambda m, v: w[m * n + v])


def parse_lean_table(path, name):
    """Parse a Lean pattern-matching table `def name : Fin 4 → Fin 4 → Fin 4 | a, b => c ...`."""
    src = open(path).read()
    i = src.index('def ' + name + ' :')
    j = src.index('\n\n', i)
    body = src[i:j]
    tab = {}
    for a, b, c in re.findall(r'\|\s*(\d)\s*,\s*(\d)\s*=>\s*(\d)', body):
        tab[(int(a), int(b))] = int(c)
    assert len(tab) == 16, (name, len(tab))
    return tab


def kernel_cnot_matrix(path):
    pc = parse_lean_table(path, 'pc')
    pt = parse_lean_table(path, 'pt')
    # sgn: -1 at (1,3) and (2,2) (CompositeDimension.lean:741); parse the line to avoid transcription.
    src = open(path).read()
    line = src[src.index('def sgn'):].split('\n')[0]
    pairs = re.findall(r'μ = (\d) ∧ ν = (\d)', line)
    neg = {(int(a), int(b)) for a, b in pairs}
    assert neg == {(1, 3), (2, 2)}, (line, neg)
    M = sp.zeros(16, 16)
    for m in range(4):
        for v in range(4):
            s = -1 if (m, v) in neg else 1
            M[m * 4 + v, pc[(m, v)] * 4 + pt[(m, v)]] = s
    return M


def actT_matrix(Nd):
    """actT N on W d as a matrix on vec(omega): target index transformed by homMap N."""
    h = sp.diag(1, *[1] * 0) if False else None
    n = Nd.shape[0] + 1
    H = sp.zeros(n, n)
    H[0, 0] = 1
    H[1:, 1:] = Nd
    M = sp.zeros(n * n, n * n)
    for m in range(n):
        for v in range(n):
            for l in range(n):
                M[m * n + v, m * n + l] += H[v, l]
    return M


def actC_matrix(Nd):
    n = Nd.shape[0] + 1
    H = sp.zeros(n, n)
    H[0, 0] = 1
    H[1:, 1:] = Nd
    M = sp.zeros(n * n, n * n)
    for m in range(n):
        for v in range(n):
            for k in range(n):
                M[m * n + v, k * n + v] += H[m, k]
    return M


def is_psd_exact(A):
    """Exact PSD test for a Hermitian matrix with exact entries: all principal minors >= 0."""
    n = A.shape[0]
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            d = sp.nsimplify(sp.simplify(A.extract(list(S), list(S)).det()))
            d = sp.re(d) if sp.im(d) == 0 else d
            if not (sp.im(d) == 0 and d >= 0):
                return False, (S, d)
    return True, None


CHECKS = []


def check(name, cond, detail=''):
    CHECKS.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name + ((' :: ' + str(detail)) if detail != '' else ''))
    return bool(cond)


def summary():
    nf = sum(1 for _, c in CHECKS if not c)
    print('SUMMARY: %d checks, %d failures' % (len(CHECKS), nf))
    return nf
