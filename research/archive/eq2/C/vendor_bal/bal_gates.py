"""BAL thread: gate builders and the positivity-certificate identities (sympy, exact only).

Conventions are those of relt_common.py (copied verbatim from the REL-T thread, sha256 02cb7ddb...),
which mirror OIBridge.CompositeDimension: HVec d = R^{d+1} with index 0 the unit, W d = (d+1)x(d+1)
matrices omega[mu][nu] (mu control, nu target), prodState x y = hom x hom y^T, actT N w = w homMap(N)^T,
actC N w = homMap(N) w, pairVal a b w = a^T w b.  The corner axis is always z = e_d (homogeneous index d).
"""
from sympy import Matrix, Rational as R, eye, zeros, diag, symbols, expand
from relt_common import hom, homMap, gate_from_fun, apply, prod, pairVal


def cstruct(n, pairs):
    """(n x n) matrix of the complex structure e_i -> e_j, e_j -> -e_i for each (i, j) in pairs (homogeneous indices)"""
    M = zeros(n, n)
    for i, j in pairs:
        M[j, i] = 1
        M[i, j] = -1
    return M


def signs_N(d, plus_coords):
    """the NOT diag(+1 on the listed coordinates (0-based), -1 elsewhere) on R^d"""
    return diag(*[1 if c in plus_coords else -1 for c in range(d)])


def jk_gate_general(d, u, J, K):
    """The generalized J/K gate on W d (d odd >= 3).

    u     -- homogeneous index (1 <= u <= d-1) of the fixed axis u0 = e_u of sigma = 2 u0 u0^T - I
    J     -- (d+1)x(d+1) matrix: an orthogonal complex structure on the tangent indices 1..d-1, zero elsewhere
    K     -- (d+1)x(d+1) matrix: an orthogonal complex structure on the indices of E-(sigma) = {1..d} minus {u},
             zero on indices 0 and u
    The gate:  G(hom z (x) Y) = hom z (x) Y,  G(hom(-z) (x) Y) = hom(-z) (x) S Y  (S = homMap sigma),
               G(lift t (x) Y) = lift t (x) X P+ Y + (J lift t) (x) K P- Y   for t perp z,
    with P+ the projection on span(e_0, e_u), P- = I - P+, and X exchanging e_0 <-> e_u.
    """
    n = d + 1
    sigma = -eye(d)
    sigma[u - 1, u - 1] = 1
    S = homMap(sigma)
    z = zeros(d, 1)
    z[d - 1] = 1
    hz, hm = hom(z), hom(-z)
    Xs = zeros(n, n)
    Xs[0, u] = 1
    Xs[u, 0] = 1
    Pp = zeros(n, n)
    Pp[0, 0] = 1
    Pp[u, u] = 1
    Pm = eye(n) - Pp

    def G_basis(mu, Y):
        if mu == 0:
            return (hz * Y.T + hm * (S * Y).T) / 2
        if mu == d:
            return (hz * Y.T - hm * (S * Y).T) / 2
        X = zeros(n, 1)
        X[mu] = 1
        return X * (Xs * Pp * Y).T + (J * X) * (K * Pm * Y).T

    def fun(w):
        out = zeros(n, n)
        for mu in range(n):
            for nu in range(n):
                if w[mu, nu] != 0:
                    Y = zeros(n, 1)
                    Y[nu] = 1
                    out += w[mu, nu] * G_basis(mu, Y)
        return out

    return dict(G=gate_from_fun(fun, n), z=z, sigma=sigma, S=S, Xs=Xs, Pp=Pp, Pm=Pm, J=J, K=K, u=u, d=d)


# ---------------------------------------------------------------- the landed gC5, transcribed from
# verification/lean-mathlib/OIBridge/RelcSelectC5.lean at bcbc516f (sgnC5, pcC5, ptC5, nC5)

_pcC5 = [[0, 0, 5, 5, 5, 5], [1, 1, 2, 2, 2, 2], [2, 2, 1, 1, 1, 1],
         [3, 3, 4, 4, 4, 4], [4, 4, 3, 3, 3, 3], [5, 5, 0, 0, 0, 0]]
_ptC5 = [[0, 1, 2, 3, 4, 5], [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2],
         [1, 0, 5, 4, 3, 2], [1, 0, 5, 4, 3, 2], [0, 1, 2, 3, 4, 5]]


def _sgnC5(m, v):
    return -1 if ((m in (1, 3)) and (v in (4, 5))) or ((m in (2, 4)) and (v in (2, 3))) else 1


def landed_gC5():
    def f(w):
        return Matrix(6, 6, lambda m, v: _sgnC5(m, v) * w[_pcC5[m][v], _ptC5[m][v]])
    return gate_from_fun(f, 6)


def landed_nC5():
    # oddC5 = true at homogeneous indices 2..5: nC5 = diag(1, -1, -1, -1, -1)
    return diag(1, -1, -1, -1, -1)


def entW(n, p, q):
    E = zeros(n, n)
    E[p, q] = 1
    return E


# ---------------------------------------------------------------- the positivity certificate, as identities

def certificate_identities(g):
    """Exact polynomial identities behind the written positivity proof of a generalized J/K gate g.

    With symbolic x, y in R^d and e, f in R^{d+1}:
      value    = pairVal e f (G (prodState x y))
      P = f^T hom y,  Q = f^T S hom y,  alpha = f^T X P+ hom y,  beta = f^T K P- hom y,
      A = 1/2 (1 + x_z)(e0 + e_z) P,  B = 1/2 (1 - x_z)(e0 - e_z) Q,  C = (e_T.x_T) alpha + (e_T.J x_T) beta.
    Returns a dict of booleans:
      I1  value = A + B + C
      I2  P Q - alpha^2 - beta^2 = (f0^2 - fu^2 - |f-|^2)|y-|^2 + Bes_K + (f0^2 - fu^2)(1 - |y|^2)
      I3  |y-|^2 Bes_K = |g_K|^2,  g_K = |y-|^2 f- - (f-.y-) y- - (f-.K y-) K y-
      I4  |x_T|^2 Bes_J = |g_J|^2, with Bes_J = |e_T|^2|x_T|^2 - (e_T.x_T)^2 - (e_T.J x_T)^2
      I5  4AB - C^2 = [(1-x_z^2)(e0^2-e_z^2) - |x_T|^2|e_T|^2] P Q + |x_T|^2|e_T|^2 (PQ - alpha^2 - beta^2)
                      + [|x_T|^2|e_T|^2 (alpha^2+beta^2) - C^2]
      I6  |x_T|^2|e_T|^2(alpha^2+beta^2) - C^2 = (alpha^2+beta^2) Bes_J + ((e_T.x_T) beta - (e_T.J x_T) alpha)^2
    Nonnegativity of every bracket then follows from the cone and ball conditions (written proof, LEDGER).
    """
    d, u = g["d"], g["u"]
    n = d + 1
    G, S, Xs, Pp, Pm, J, K = g["G"], g["S"], g["Xs"], g["Pp"], g["Pm"], g["J"], g["K"]
    xs = Matrix(symbols(f"x0:{d}"))
    ys = Matrix(symbols(f"y0:{d}"))
    es = Matrix(symbols(f"e0:{n}"))
    fs = Matrix(symbols(f"f0:{n}"))
    val = pairVal(es, fs, apply(G, hom(xs) * hom(ys).T))
    hy = hom(ys)
    P = (fs.T * hy)[0, 0]
    Q = (fs.T * S * hy)[0, 0]
    alpha = (fs.T * Xs * Pp * hy)[0, 0]
    beta = (fs.T * K * Pm * hy)[0, 0]
    xz, ez = xs[d - 1], es[d]
    xT = Matrix([0] + [xs[i - 1] for i in range(1, d)] + [0])
    eT = Matrix([0] + [es[i] for i in range(1, d)] + [0])
    A = R(1, 2) * (1 + xz) * (es[0] + ez) * P
    B = R(1, 2) * (1 - xz) * (es[0] - ez) * Q
    eTxT = (eT.T * xT)[0, 0]
    eTJxT = (eT.T * J * xT)[0, 0]
    C = eTxT * alpha + eTJxT * beta
    out = {}
    out["I1 value = A + B + C"] = expand(val - (A + B + C)) == 0
    minus = [i for i in range(1, n) if i != u]
    fm = Matrix([fs[i] for i in minus])
    ym = Matrix([hy[i] for i in minus])
    Km = K.extract(minus, minus)
    fm2 = (fm.T * fm)[0, 0]
    ym2 = (ym.T * ym)[0, 0]
    besK = fm2 * ym2 - (fm.T * ym)[0, 0] ** 2 - (fm.T * Km * ym)[0, 0] ** 2
    y2 = (ys.T * ys)[0, 0]
    rhs2 = (fs[0] ** 2 - fs[u] ** 2 - fm2) * ym2 + besK + (fs[0] ** 2 - fs[u] ** 2) * (1 - y2)
    out["I2 PQ - alpha^2 - beta^2 decomposition"] = expand(P * Q - alpha ** 2 - beta ** 2 - rhs2) == 0
    gK = ym2 * fm - (fm.T * ym)[0, 0] * ym - (fm.T * Km * ym)[0, 0] * (Km * ym)
    out["I3 |y-|^2 Bes_K = |g_K|^2"] = expand(ym2 * besK - (gK.T * gK)[0, 0]) == 0
    tang = list(range(1, d))
    xt = Matrix([xs[i - 1] for i in tang])
    et = Matrix([es[i] for i in tang])
    Jt = J.extract(tang, tang)
    xt2 = (xt.T * xt)[0, 0]
    et2 = (et.T * et)[0, 0]
    besJ = et2 * xt2 - (et.T * xt)[0, 0] ** 2 - (et.T * Jt * xt)[0, 0] ** 2
    gJ = xt2 * et - (et.T * xt)[0, 0] * xt - (et.T * Jt * xt)[0, 0] * (Jt * xt)
    out["I4 |x_T|^2 Bes_J = |g_J|^2"] = expand(xt2 * besJ - (gJ.T * gJ)[0, 0]) == 0
    i5 = ((1 - xz ** 2) * (es[0] ** 2 - ez ** 2) - xt2 * et2) * P * Q + xt2 * et2 * (P * Q - alpha ** 2 - beta ** 2) \
        + (xt2 * et2 * (alpha ** 2 + beta ** 2) - C ** 2)
    out["I5 4AB - C^2 decomposition"] = expand(4 * A * B - C ** 2 - i5) == 0
    i6 = (alpha ** 2 + beta ** 2) * besJ + (eTxT * beta - eTJxT * alpha) ** 2
    out["I6 Cauchy-Schwarz/Bessel bracket"] = expand(xt2 * et2 * (alpha ** 2 + beta ** 2) - C ** 2 - i6) == 0
    out["J, K orthogonal complex structures on their blocks"] = (
        (Jt * Jt + eye(d - 1)).is_zero_matrix and (Jt.T * Jt - eye(d - 1)).is_zero_matrix
        and (Km * Km + eye(len(minus))).is_zero_matrix and (Km.T * Km - eye(len(minus))).is_zero_matrix)
    return out
