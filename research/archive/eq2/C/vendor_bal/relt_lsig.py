"""REL-T: the core space Lsig (exact) and sigma helpers, shared by relt_pos_exact and relt_d4_rank_probe."""
from sympy import Matrix, Rational as R, eye, zeros, symbols, Poly, expand, simplify, diag, fraction, cancel, together


def Lsig_exact(sigma):
    """solve the defining identities of Lsig symbolically; returns a basis (list of matrices)"""
    d = sigma.shape[0]
    n = d + 1
    ys = symbols(f"y0:{d}")
    y = Matrix(ys)
    Ls = symbols(f"l0:{n*n}")
    L = Matrix(n, n, Ls)
    c1, c2 = symbols("c1 c2")
    r2 = sum(v ** 2 for v in ys)
    hy = Matrix([1] + list(ys))
    sy = sigma * y
    p1 = expand((Matrix([1] + [-v for v in ys]).T * L * hy)[0, 0] - c1 * (r2 - 1))
    p2 = expand((Matrix([1] + [-v for v in sy]).T * L * hy)[0, 0] - c2 * (r2 - 1))
    eqs = Poly(p1, *ys).coeffs() + Poly(p2, *ys).coeffs()
    unknowns = list(Ls) + [c1, c2]
    # linear system
    rows = []
    for e in eqs:
        num, den = fraction(cancel(together(e)))
        pe = Poly(expand(num), *unknowns)
        rows.append([pe.coeff_monomial(u) for u in unknowns])
    A = Matrix(rows).applyfunc(cancel)
    ns = A.nullspace(iszerofunc=lambda x: cancel(x) == 0, simplify=cancel)
    ns = [v.applyfunc(cancel) for v in ns]
    basis = [Matrix(n, n, list(v[: n * n])) for v in ns]
    return basis


def Lsig_formula_ok(sigma, basis):
    d = sigma.shape[0]
    n = d + 1
    # every basis element has the form [[0,a^T],[a,A]], sigma a = a, A antisym, sigma^T A = A sigma
    for L in basis:
        if L[0, 0] != 0:
            return False
        a = L[1:, 0]
        if (L[0, 1:] - a.T).is_zero_matrix is False:
            return False
        A = L[1:, 1:]
        if not (A + A.T).is_zero_matrix:
            return False
        if not (sigma * a - a).is_zero_matrix:
            return False
        if not simplify(sigma.T * A - A * sigma).is_zero_matrix:
            return False
    # dimension of the formula space, computed independently
    av = symbols(f"a0:{d}")
    Av = symbols(f"A0:{d*d}")
    a = Matrix(av)
    A = Matrix(d, d, Av)
    cons = list(sigma * a - a) + list(A + A.T) + list(sigma.T * A - A * sigma)
    unk = list(av) + list(Av)
    M = Matrix([[simplify(e).coeff(u) if True else 0 for u in unk] for e in [expand(c) for c in cons]])
    dimF = len(unk) - M.rank(simplify=True)
    return dimF == len(basis)


def generic(basis, tag="g"):
    cs = symbols(f"{tag}0:{len(basis)}")
    M = zeros(*basis[0].shape)
    for c, B in zip(cs, basis):
        M += c * B
    return M, cs


def rot2(m):
    """rotation of the plane with rational parameter m (cos = (1-m^2)/(1+m^2))"""
    c = (1 - m ** 2) / (1 + m ** 2)
    s = 2 * m / (1 + m ** 2)
    return Matrix([[c, -s], [s, c]])


def sig_from_R(Rm):
    d = Rm.shape[0] + 1
    S = zeros(d, d)
    S[: d - 1, : d - 1] = Rm
    S[d - 1, d - 1] = -1
    return S


