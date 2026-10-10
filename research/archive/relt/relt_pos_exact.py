"""REL-T, nodes N2.3-N4: exact computation for the positivity branches.

(A) The tangent-vanishing core. If G is invertible with the frame and two-sided positivity, then (written proof,
    LEDGER N2.3) after normalization Gt = G (I (x) M0^{-1}) every control-tangent slice satisfies
        Gt(lift t (x) Y) = sum_k lift e_k (x) L_{k,t} Y ,   L_{k,t} in Lsig,
        Lsig = { L : (1,-y)^T L (1,y) = 0 and (1,-sigma y)^T L (1,y) = 0 for every unit y },
    where homMap sigma = S = M1 M0^{-1} and sigma is orthogonal with sigma z = -z.
    Here we compute Lsig EXACTLY from its defining polynomial identities (symbolic y, the identity
    'p(y) = c (|y|^2 - 1)'), and certify:
      A1  Lsig = { [[0, a^T],[a, A]] : sigma a = a, A^T = -A, sigma^T A = A sigma }  (dimension match + containment)
      A2  d = 2: for both sigma = diag(1,-1), -id, the generic element of Lsig has det 0 (so every block
          matrix over Lsig on T (x) H, T one-dimensional, is singular).
      A3  d = 3, relT: Lsig intersect comm(homMap N) kills lift z for N = refl3 and kills e0 for N = negId3,
          for sigma = diag(R, -1), R in O(2) rationally parametrized (rotations and reflections).
      A4  positive controls: DIM-1's cnot (d = 3) and the J/K gates (d = 3, 5, 7) have the normalized form with
          blocks in Lsig and invertible tangent block; countercontrols: gJ3, gJ5 and the controlled-N gate
          violate the tangent-vanishing identities (they are not positive, and the evaluator must see it).
(B) The J/K family C_d (d = 2m+1), NB-1's C5 at d = 5: IsNot, frame, relT, G^2 = I, relC (holds d=3, fails d>=5),
    the exact value decomposition used in the written positivity proof, the polynomial identity for PQ - alpha^2 -
    beta^2, and an exact rational sampled sanity check (not a certificate) with the gJ5 countercontrol.
"""
import sys, itertools, random
from sympy import Matrix, Rational as R, eye, zeros, symbols, Poly, expand, linsolve, simplify, diag, together, factor
from relt_common import *

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


# ---------------------------------------------------------------- (A) the core space Lsig

from relt_lsig import Lsig_exact, Lsig_formula_ok, generic, rot2, sig_from_R


print("== (A1) Lsig equals the formula space")
mm = symbols("m")
sigmas = {
    "d2 diag(1,-1)": sig_from_R(Matrix([[1]])),
    "d2 -id": sig_from_R(Matrix([[-1]])),
    "d3 diag(1,-1,-1) [nflip]": sig_from_R(diag(1, -1)),
    "d3 diag(1,1,-1)": sig_from_R(diag(1, 1)),
    "d3 -id": sig_from_R(diag(-1, -1)),
    "d3 rot(1/2)(+)(-1)": sig_from_R(rot2(R(1, 2))),
    "d4 diag(1,-1,-1,-1)": sig_from_R(diag(1, -1, -1)),
    "d4 diag(1,1,-1,-1)": sig_from_R(diag(1, 1, -1)),
}
bases = {}
for name, s in sigmas.items():
    B = Lsig_exact(s)
    bases[name] = B
    check(f"A1 {name}: Lsig dim {len(B)} matches [[0,a^T],[a,A]] formula", Lsig_formula_ok(s, B))

print("== (A2) d = 2: every element of Lsig is singular (all sigma with sigma z = -z)")
for name in ["d2 diag(1,-1)", "d2 -id"]:
    M, cs = generic(bases[name])
    check(f"A2 {name}: det(generic L) == 0 identically", expand(M.det()) == 0)
# countercontrol for A2: at d = 3 with sigma = nflip, Lsig contains an invertible element
M, cs = generic(bases["d3 diag(1,-1,-1) [nflip]"])
check("A2-countercontrol d3 nflip: det(generic L) not identically 0", expand(M.det()) != 0)

print("== (A3) d = 3 under relT: refl3 / negId3 force a common kernel")
refl3 = diag(1, 1, -1)
negId3 = diag(-1, -1, -1)
for Rname, Rm in [("rot(m)", rot2(mm)), ("refl diag(1,-1)", diag(1, -1)), ("id", eye(2)), ("-id", -eye(2))]:
    s = sig_from_R(Rm)
    B = Lsig_exact(s) if Rname != "rot(m)" else None
    if B is None:
        # symbolic rotation: solve with m symbolic (linear system over Q(m))
        B = Lsig_exact(s)
    if not B:
        check(f"A3 sigma={Rname}: Lsig = 0 (every tangent block vanishes; excluded for every N)", True)
        continue
    for Nname, N in [("refl3", refl3), ("negId3", negId3)]:
        Nh = homMap(N)
        M, cs = generic(B, "q")
        cons = list(M * Nh - Nh * M)
        sol = linsolve([together(c) for c in cons], cs) if cons and any(c != 0 for c in cons) else None
        if sol is None:
            Mc = M
        else:
            (vals,) = list(sol)
            Mc = M.subs(dict(zip(cs, vals)))
        if Nname == "refl3":
            kv = Mc * Matrix([0, 0, 0, 1])
            check(f"A3 sigma={Rname} N=refl3: every L in Lsig cap comm(N) kills lift z", simplify(kv).is_zero_matrix)
        else:
            kv = Mc * Matrix([1, 0, 0, 0])
            check(f"A3 sigma={Rname} N=negId3: every L in Lsig cap comm(N) kills e0", simplify(kv).is_zero_matrix)
# countercontrol for A3: with N = nflip and sigma = nflip, some L in Lsig cap comm(N) does not kill lift z nor e0
s = sigmas["d3 diag(1,-1,-1) [nflip]"]
B = bases["d3 diag(1,-1,-1) [nflip]"]
Nh = homMap(diag(1, -1, -1))
M, cs = generic(B, "q")
(vals,) = list(linsolve(list(M * Nh - Nh * M), cs))
Mc = M.subs(dict(zip(cs, vals)))
check("A3-countercontrol N=nflip: some L kills neither lift z nor e0",
      not (Mc * Matrix([0, 0, 0, 1])).is_zero_matrix and not (Mc * Matrix([1, 0, 0, 0])).is_zero_matrix)


# ---------------------------------------------------------------- the normalized-form extractor

def corner_maps(G, z):
    """M0, M1 with G(hz (x) Y) = hz (x) M0 Y, G(h(-z) (x) Y) = h(-z) (x) M1 Y, or None if not of that form"""
    n = z.shape[0] + 1
    hz, hm = hom(z), hom(-z)
    M = []
    for h in (hz, hm):
        cols = []
        for j in range(n):
            Y = zeros(n, 1); Y[j] = 1
            out = apply(G, h * Y.T)
            # out must be h (x) v : v = out^T e0 / h0 (h0 = 1)
            v = out[0, :].T
            if not (out - h * v.T).is_zero_matrix:
                return None
            cols.append(v)
        M.append(Matrix.hstack(*cols))
    return M


def tangent_blocks(G, z, M0):
    """blocks L_{k j} of Gt = G (I (x) M0^{-1}) on lift(e_j) (x) Y, control output in T = z-perp;
    returns (blocks dict, control_output_in_T?)"""
    n = z.shape[0] + 1
    d = n - 1
    # orthonormal basis of z-perp from coordinate vectors (z is a coordinate axis in all our examples)
    zi = [i for i in range(d) if z[i] != 0]
    assert len(zi) == 1
    Tidx = [i + 1 for i in range(d) if i != zi[0]]
    M0i = M0.inv()
    ok = True
    blocks = {}
    for j in Tidx:
        for col_ in range(n):
            Y = zeros(n, 1); Y[col_] = 1
            X = zeros(n, 1); X[j] = 1
            out = apply(G, X * (M0i * Y).T)
            # control output must lie in T: rows 0 and z-index vanish
            if not (out[0, :].is_zero_matrix and out[zi[0] + 1, :].is_zero_matrix):
                ok = False
            for k in Tidx:
                blocks.setdefault((k, j), zeros(n, n))
                blocks[(k, j)][:, col_] = out[k, :].T
    return blocks, Tidx, ok


def in_Lsig(L, sigma):
    a = L[1:, 0]
    A = L[1:, 1:]
    return (L[0, 0] == 0 and (L[0, 1:] - a.T).is_zero_matrix and (A + A.T).is_zero_matrix
            and (sigma * a - a).is_zero_matrix and (sigma.T * A - A * sigma).is_zero_matrix)


def normal_form_report(G, z, label, expect_positive):
    Ms = corner_maps(G, z)
    if Ms is None:
        check(f"A4 {label}: corner slices are product-form" + (" (expected)" if expect_positive else " FAIL expected -> countercontrol ok"),
              not expect_positive)
        return
    M0, M1 = Ms
    S = M1 * M0.inv()
    sigma = S[1:, 1:]
    autoS = S[0, 0] == 1 and S[0, 1:].is_zero_matrix and S[1:, 0].is_zero_matrix and (sigma.T * sigma - eye(sigma.shape[0])).is_zero_matrix
    blocks, Tidx, inT = tangent_blocks(G, z, M0)
    allL = inT and all(in_Lsig(L, sigma) for L in blocks.values())
    n = z.shape[0] + 1
    K = Matrix.vstack(*[Matrix.hstack(*[blocks[(k, j)] for j in Tidx]) for k in Tidx])
    inv = K.det() != 0
    if expect_positive:
        check(f"A4 {label}: S = 1(+)orthogonal, tangent outputs in T, all blocks in Lsig, tangent block invertible",
              autoS and inT and allL and inv)
    else:
        check(f"A4 {label}: violates the tangent-vanishing/Lsig necessary conditions (countercontrol)",
              not (autoS and inT and allL))


# ---------------------------------------------------------------- (B) the J/K family

def jk_gate(d):
    """C_d, d = 2m+1 >= 3: basis u=0, x=1, tangent 2..d-1, z=d.  N = diag(1, 1, -1, ..., -1) on (u, x, rest).
    G(h(+-z) (x) Y) per the frame with M0 = I, M1 = homMap N; G(e_c (x) Y) = e_c (x) X P+ Y + (J e_c) (x) K P- Y."""
    n = d + 1
    signs = [1] + [-1] * (d - 1)  # on coordinates x, ..., z
    N = diag(*signs)
    Nh = homMap(N)
    z = zeros(d, 1); z[d - 1] = 1
    hz, hm = hom(z), hom(-z)
    Xs = zeros(n, n); Xs[0, 1] = 1; Xs[1, 0] = 1  # exchange u <-> x on E+
    Pp = zeros(n, n); Pp[0, 0] = 1; Pp[1, 1] = 1
    Pm = eye(n) - Pp
    J = zeros(n, n)  # on T = indices 1..d-1, pairs (1,2),(3,4),...
    for i in range(1, d - 1, 2):
        J[i + 1, i] = 1; J[i, i + 1] = -1
    Kc = zeros(n, n)  # on V- = indices 2..d, pairs (2,d),(3,4),(5,6),...
    Kc[d, 2] = 1; Kc[2, d] = -1
    for i in range(3, d - 1, 2):
        Kc[i + 1, i] = 1; Kc[i, i + 1] = -1
    e0 = zeros(n, 1); e0[0] = 1
    ez = zeros(n, 1); ez[d] = 1

    def G_basis(mu, Y):
        X = zeros(n, 1); X[mu] = 1
        if mu == 0:
            return (hz * Y.T + hm * (Nh * Y).T) / 2
        if mu == d:
            return (hz * Y.T - hm * (Nh * Y).T) / 2
        return X * (Xs * Pp * Y).T + (J * X) * (Kc * Pm * Y).T

    def fun(w):
        out = zeros(n, n)
        for mu in range(n):
            for nu in range(n):
                if w[mu, nu] != 0:
                    Y = zeros(n, 1); Y[nu] = 1
                    out += w[mu, nu] * G_basis(mu, Y)
        return out
    return gate_from_fun(fun, n), z, N, J, Kc, Xs


def rational_sphere_point(d, rng):
    """inverse stereographic projection of a random rational point: exact rational unit vector in R^d"""
    t = [R(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(d - 1)]
    s2 = sum(v ** 2 for v in t)
    return Matrix([2 * v / (1 + s2) for v in t] + [(s2 - 1) / (1 + s2)])


def sampled_min(G, d, rng, trials, extra=()):
    """exact rational sanity sampling of pairVal over pure products and boundary effects (NOT a certificate)"""
    worst = None
    pts = list(extra)
    for _ in range(trials):
        x = rational_sphere_point(d, rng); y = rational_sphere_point(d, rng)
        e = hom(rational_sphere_point(d, rng)); f = hom(rational_sphere_point(d, rng))
        pts.append((x, y, e, f))
    for (x, y, e, f) in pts:
        v = pairVal(e, f, apply(G, prod(x, y)))
        worst = v if worst is None or v < worst else worst
    return worst


rng = random.Random(20261007)
print("== (B) the J/K family")
for d in (3, 5, 7):
    G, z, N, J, Kc, Xs = jk_gate(d)
    n = d + 1
    check(f"B C{d}: IsNot", all(isNot(z, N).values()))
    check(f"B C{d}: frame", frame(G, z))
    check(f"B C{d}: relT", relT(G, N))
    check(f"B C{d}: G^2 = I", (G * G - eye(n * n)).is_zero_matrix)
    rc = relC(G, N)
    check(f"B C{d}: relC {'holds (d=3: complex CNOT)' if d == 3 else 'FAILS'}", rc == (d == 3))
    p, m = eig_dims(N)
    check(f"B C{d}: eigenspaces of homMap N = ({p},{m}), balanced iff d = 3", (p == m) == (d == 3))
    JT = J[1:d, 1:d]; KV = Kc[2:, 2:]
    check(f"B C{d}: J, K orthogonal complex structures", (JT * JT + eye(d - 1)).is_zero_matrix and (JT.T * JT - eye(d - 1)).is_zero_matrix
          and (KV * KV + eye(d - 1)).is_zero_matrix and (KV.T * KV - eye(d - 1)).is_zero_matrix)
    normal_form_report(G, z, f"C{d} (positive control)", True)
    # the value decomposition used in the written proof, as a polynomial identity
    xs = Matrix(symbols(f"x0:{d}")); ys = Matrix(symbols(f"y0:{d}"))
    es = Matrix(symbols(f"e0:{n}")); fs = Matrix(symbols(f"f0:{n}"))
    val = pairVal(es, fs, apply(G, hom(xs) * hom(ys).T))
    hy = hom(ys)
    P = (fs.T * hy)[0, 0]; Q = (fs.T * homMap(N) * hy)[0, 0]
    Pp = zeros(n, n); Pp[0, 0] = 1; Pp[1, 1] = 1
    alpha = (fs.T * Xs * Pp * hy)[0, 0]
    beta = (fs.T * Kc * (eye(n) - Pp) * hy)[0, 0]
    xz = xs[d - 1]; ez_ = es[d]
    xT = zeros(n, 1)
    for i in range(1, d):
        xT[i] = xs[i - 1]
    eT = zeros(n, 1)
    for i in range(1, d):
        eT[i] = es[i]
    rhs = (R(1, 2) * (1 + xz) * (es[0] + ez_) * P + R(1, 2) * (1 - xz) * (es[0] - ez_) * Q
           + (eT.T * xT)[0, 0] * alpha + (eT.T * J * xT)[0, 0] * beta)
    check(f"B C{d}: value = 1/2(1+x_z)(e0+e_z)P + 1/2(1-x_z)(e0-e_z)Q + (e_T.x_T) alpha + (e_T.J x_T) beta",
          expand(val - rhs) == 0)
    # PQ - alpha^2 - beta^2 = (f0^2-fx^2-|f-|^2)|y-|^2 + [|f-|^2|y-|^2-(f-.y-)^2-(f-.Ky-)^2] + (f0^2-fx^2)(1-|y|^2)
    fm = Matrix([fs[i] for i in range(2, n)]); ym = Matrix([ys[i - 1] for i in range(2, n)])
    fm2 = (fm.T * fm)[0, 0]; ym2 = (ym.T * ym)[0, 0]
    bessel = fm2 * ym2 - (fm.T * ym)[0, 0] ** 2 - (fm.T * KV * ym)[0, 0] ** 2
    y2 = (ys.T * ys)[0, 0]
    ident = (fs[0] ** 2 - fs[1] ** 2 - fm2) * ym2 + bessel + (fs[0] ** 2 - fs[1] ** 2) * (1 - y2)
    check(f"B C{d}: PQ - alpha^2 - beta^2 identity (cone slack + Bessel bracket + sphere term)",
          expand(P * Q - alpha ** 2 - beta ** 2 - ident) == 0)
    # Bessel bracket nonnegativity ingredients: y.Ky = 0, |Ky| = |y|
    check(f"B C{d}: y.Ky = 0 and |Ky|^2 = |y|^2 identically",
          expand((ym.T * KV * ym)[0, 0]) == 0 and expand(((KV * ym).T * (KV * ym))[0, 0] - ym2) == 0)
    # exact rational sampling sanity (not a certificate)
    w = sampled_min(G, d, rng, 150 if d < 7 else 60)
    check(f"B C{d}: sampled exact values over rational pure products/boundary effects >= 0 (min {w})", w >= 0)

# countercontrols for the evaluator: gJ5 at PARITY-NOT-1's witness, and the controlled-N gate
odd5 = [False, False, False, True, True, True]
perm5 = [5, 3, 4, 1, 2, 0]
gJ5 = sgate(odd5, perm5, 6)
z5 = Matrix([0, 0, 0, 0, 1]); x5 = Matrix([1, 0, 0, 0, 0]); w5 = Matrix([0, 0, R(-3, 5), 0, R(-4, 5)])
v = pairVal(sharpVec(w5), sharpVec(z5), apply(gJ5, prod(x5, z5)))
check("CC gJ5_value = -1/10 reproduced by the evaluator", v == R(-1, 10))
normal_form_report(gJ5, z5, "gJ5 (countercontrol)", False)
gJ3 = sgate([False, False, True, True], [3, 2, 1, 0], 4)
normal_form_report(gJ3, Matrix([0, 0, 1]), "gJ3 (countercontrol)", False)
Gc, Pa, Pb = controlled_N_gate(Matrix([0, 1]), diag(1, -1))
normal_form_report(Gc, Matrix([0, 1]), "controlled-N d=2 (countercontrol)", False)
normal_form_report(dim1_cnot(), Matrix([0, 0, 1]), "DIM-1 cnot (positive control)", True)

npass = sum(1 for _, c in checks if c)
print(f"relt_pos_exact: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
