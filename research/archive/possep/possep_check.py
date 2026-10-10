"""POS-SEP checks.  Run:  python3 possep_check.py   (from this directory)

Exact arithmetic (fractions.Fraction / sympy Rational) for every verdict.  Floating point is used ONLY
to *search* for witnesses and S-lemma multipliers; every float result is rationalized and re-verified
exactly before it is reported, and a float minimum is never reported as a certificate.
"""
import random
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.optimize import minimize

from possep_core import (ONE, ZERO, zeros, hom, prod_state, tens, pair_val, sharp_vec, corner,
                         actT, actC, eq, basis, matrix_of, mat_apply, mat_inverse, rank,
                         in_lor_exact, maxcone_certificate, sphere_point,
                         maxcone_certificate_algebraic)
from possep_gate import Squeezed

CHECKS = []


def check(name, cond, info=""):
    CHECKS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + info) if info else ""))
    return cond


# =====================================================================================
# Positive controls: reproduce landed facts at L
# =====================================================================================

def landed_gJ5_value():
    """ParityNot.gJ5_value (l.692): prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1/10."""
    odd5 = [False, False, False, True, True, True]
    perm5 = [5, 3, 4, 1, 2, 0]

    def sgate(om):  # ParityNot.sgate (l.428)
        return [[om[perm5[m]][v] if odd5[v] else om[m][v] for v in range(6)] for m in range(6)]
    x5 = [1, 0, 0, 0, 0]
    z5 = [0, 0, 0, 0, 1]
    w5 = [0, 0, Fr(-3, 5), 0, Fr(-4, 5)]
    om = sgate(prod_state(x5, z5))
    return om, pair_val(sharp_vec(w5), sharp_vec(z5), om)


def landed_cnot3():
    """CompositeDimension.cnotFun (l.758) with sgn, pc, pt; nflip (l.797); z3 (l.793)."""
    pc = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
    pt = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]

    def sgn(m, v):
        return -ONE if (m == 1 and v == 3) or (m == 2 and v == 2) else ONE

    def cnot(om):
        return [[sgn(m, v) * om[pc[m][v]][pt[m][v]] for v in range(4)] for m in range(4)]
    s = [ONE, ONE, -ONE, -ONE]  # homMap nflip
    z3 = [0, 0, 1]
    return cnot, s, z3


def gRev_value(k):
    """OddChar.gRev_value (l.258): = -1/10 for k >= 1."""
    d, n = 2 * k + 1, 2 * k + 2
    odd = [m > k for m in range(n)]

    def g(om):  # sgate (oddK k) Fin.rev
        return [[om[n - 1 - m][v] if odd[v] else om[m][v] for v in range(n)] for m in range(n)]
    xK = [ONE if j == 0 else ZERO for j in range(d)]
    zK = [ONE if j == 2 * k else ZERO for j in range(d)]
    wK = [Fr(-3, 5) if j == 2 * k - 1 else Fr(-4, 5) if j == 2 * k else ZERO for j in range(d)]
    return pair_val(sharp_vec(wK), sharp_vec(zK), g(prod_state(xK, zK)))


def positive_controls():
    print("\n== positive controls (landed facts reproduced) ==")
    om, v = landed_gJ5_value()
    check("PC1 gJ5_value = -1/10 (ParityNot l.692)", v == Fr(-1, 10), str(v))
    for k in (1, 2, 3):
        v = gRev_value(k)
        check(f"PC2 gRev_value k={k} = -1/10 (OddChar l.258)", v == Fr(-1, 10), str(v))
    cnot, s, z3 = landed_cnot3()
    fr = all(eq(cnot(prod_state(corner(z3, a), corner(z3, b))),
                prod_state(corner(z3, a), corner(z3, (a + b) % 2))) for a in (0, 1) for b in (0, 1))
    rt = all(eq(actT(s, cnot(actT(s, om))), cnot(om)) for om in basis(4))
    rc = all(eq(actC(s, cnot(actC(s, om))), actT(s, cnot(om))) for om in basis(4))
    check("PC3 cnot frame/relT/relC (CompositeDimension cnot_frame/relT/relC)", fr and rt and rc)
    return om


# =====================================================================================
# Main candidate: exact algebraic clauses
# =====================================================================================

def algebraic_clauses(G, tag):
    print(f"\n== {tag}: exact algebraic clauses ==")
    s, z, n, d = G.signs(), G.z(), G.n, G.d
    c = G.c_signs()
    check(f"{tag} IsNot.unit", sum(t * t for t in z) == 1)
    check(f"{tag} IsNot.invol (signs^2 = 1)", all(t * t == 1 for t in c))
    check(f"{tag} IsNot.flips", all(c[j] * z[j] == -z[j] for j in range(d)))
    # preserves: diagSign with entries +-1 preserves sum of squares, hence the ball (written fact)
    frame = all(eq(G(prod_state(corner(z, a), corner(z, b))),
                   prod_state(corner(z, a), corner(z, (a + b) % 2))) for a in (0, 1) for b in (0, 1))
    check(f"{tag} frame", frame)
    check(f"{tag} relT on all basis vectors", all(eq(actT(s, G(actT(s, om))), G(om)) for om in basis(n)))
    check(f"{tag} relC on all basis vectors",
          all(eq(actC(s, G(actC(s, om))), actT(s, G(om))) for om in basis(n)))
    M = matrix_of(G, n)
    check(f"{tag} G is a linear equivalence (rank = (d+1)^2)", rank(M) == n * n, f"rank {rank(M)}")
    Minv = mat_inverse(M)

    def Gs(om):
        return mat_apply(Minv, om)
    check(f"{tag} G.symm o G = id on basis", all(eq(Gs(G(om)), om) for om in basis(n)))
    # N1 computationally: G.symm satisfies frame, relT, relC
    frame_s = all(eq(Gs(prod_state(corner(z, a), corner(z, b))),
                     prod_state(corner(z, a), corner(z, (a + b) % 2))) for a in (0, 1) for b in (0, 1))
    rt_s = all(eq(actT(s, Gs(actT(s, om))), Gs(om)) for om in basis(n))
    rc_s = all(eq(actC(s, Gs(actC(s, om))), actT(s, Gs(om))) for om in basis(n))
    check(f"{tag} N1: G.symm has frame, relT, relC", frame_s and rt_s and rc_s)
    # S1 corner form: G(tens(hom z, Y)) = tens(hom z, K Y); Mfwd = K
    hz = hom(z)
    K = G.Kdiag()
    cf = True
    for nu in range(n):
        Y = [ONE if i == nu else ZERO for i in range(n)]
        cf &= eq(G(tens(hz, Y)), tens(hz, [K[i] * Y[i] for i in range(n)]))
    check(f"{tag} corner form G(hom z (x) Y) = hom z (x) K Y  (Mfwd = K_lam)", cf)
    x1 = [ONE if j == 0 else ZERO for j in range(d)]
    MinvY = [hom(x1)[i] / K[i] for i in range(n)]
    if G.lam < 1:
        check(f"{tag} Minv = K^-1 does not preserve Lor: Minv(hom e1) not in Lor (lor_Minv fails)",
              not in_lor_exact(MinvY), str([str(t) for t in MinvY]))
    else:
        check(f"{tag} (no squeeze) Minv = id preserves Lor at hom e1, as lor_Minv requires",
              in_lor_exact(MinvY))
    return Gs


def posinv_witness(G, Gs, tag):
    """posInv fails: G.symm(prodState z e1) paired with sharp effects of z and -e1."""
    z, d = G.z(), G.d
    x1 = [ONE if j == 0 else ZERO for j in range(d)]
    om = Gs(prod_state(z, x1))
    a, b = sharp_vec(z), sharp_vec([-t for t in x1])
    v = pair_val(a, b, om)
    unit_ok = sum(t * t for t in z) == 1 and sum(t * t for t in x1) == 1
    expected = Fr(1, 2) - 1 / (2 * G.lam)          # (sharpVec z . hom z) * (1/2 - 1/(2 lam))
    check(f"{tag} posInv FAILS: prodEffVal (sharpEff z) (sharpEff -e1) (G.symm (prodState z e1)) = {v}",
          unit_ok and v < 0 and v == expected, f"expected {expected}")
    return v


# =====================================================================================
# The decomposition identity used in the written proof of posFwd (exact, symbolic)
# =====================================================================================

def decomposition_identity(G, tag):
    print(f"\n== {tag}: symbolic decomposition identity (sympy, exact) ==")
    n, d, k = G.n, G.d, G.k
    M = matrix_of(G, n)
    Ms = sp.Matrix(n * n, n * n, lambda i, j: sp.Rational(M[i][j].numerator, M[i][j].denominator))
    xs = sp.symbols(f"x0:{d}")
    ys = sp.symbols(f"y0:{d}")
    a = sp.symbols(f"a0:{n}")
    b = sp.symbols(f"b0:{n}")
    hx = [1] + list(xs)
    hy = [1] + list(ys)
    vec = sp.Matrix([hx[m] * hy[v] for m in range(n) for v in range(n)])
    out = Ms * vec
    V = sum(a[m] * out[m * n + v] * b[v] for m in range(n) for v in range(n))
    eps, lam = sp.Rational(G.eps.numerator, G.eps.denominator), sp.Rational(G.lam.numerator, G.lam.denominator)
    s = [1 if not G.odd(m) else -1 for m in range(n)]
    al = xs[d - 1]
    cvec = {m: xs[m - 1] for m in range(1, d)}               # control tangent coordinates
    Y = [1] + [lam * ys[j] for j in range(d - 1)] + [ys[d - 1]]   # Y = K hom y = hom (K y)
    A = sum(b[v] * Y[v] for v in range(n))
    B = sum(b[v] * s[v] * Y[v] for v in range(n))
    p, q = a[0] + a[d], a[0] - a[d]
    Se = sum(Y[v] * b[G.sigma(v)] for v in range(n) if not G.odd(v))
    So = sum(Y[v] * b[G.sigma(v)] for v in range(n) if G.odd(v))
    Ce = sum(cvec[m] * a[m] for m in range(1, d))
    Co = sum(cvec[m] * a[G.permT(m)] for m in range(1, d))
    formula = (1 + al) / 2 * p * A + (1 - al) / 2 * q * B + eps * (Se * Ce + So * Co)
    diff = sp.expand(V - formula)
    check(f"{tag} V(a,b,x,y) == (1+al)/2 p A + (1-al)/2 q B + eps (Se Ce + So Co)  identically", diff == 0)


# =====================================================================================
# Sample certification of posFwd (finite; evidence, not proof)
# =====================================================================================

def find_mu(om):
    """Float search for an S-lemma multiplier, then rationalize. Returns a Fraction or None."""
    n = len(om)
    W = np.array([[float(v) for v in r] for r in om])
    J = np.diag([1.0] + [-1.0] * (n - 1))
    Q = W @ J @ W.T
    best, bm = -1e9, 0.0
    for mu in np.concatenate([[0.0], np.geomspace(1e-6, 1e3, 400)]):
        e = np.linalg.eigvalsh(Q - mu * J).min()
        if e > best:
            best, bm = e, mu
    # local refinement
    lo, hi = bm / 1.5, bm * 1.5 + 1e-9
    for _ in range(80):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if np.linalg.eigvalsh(Q - m1 * J).min() < np.linalg.eigvalsh(Q - m2 * J).min():
            lo = m1
        else:
            hi = m2
    cands = [Fr(0)]
    for den in (10 ** 6, 10 ** 9, 10 ** 12):
        cands += [Fr((lo + hi) / 2).limit_denominator(den), Fr(bm).limit_denominator(den)]
    # tight cases: multipliers that zero one diagonal entry of om J om^T - mu J exactly
    Jx = [ONE] + [-ONE] * (n - 1)
    for i in range(n):
        qii = sum(om[i][k] * Jx[k] * om[i][k] for k in range(n))
        cands.append(qii * Jx[i])
    for m in cands:
        if m >= 0 and maxcone_certificate(om, m):
            return m
    return None


def certify(om):
    """Exact sufficient certificate of om in maxCone(eball d): a rational S-lemma multiplier, or,
    at tight points, an algebraic one (maxcone_certificate_algebraic)."""
    return find_mu(om) is not None or maxcone_certificate_algebraic(om)


def rand_ball_point(d, rng, boundary):
    u = [Fr(rng.randint(-40, 40), rng.randint(1, 40)) for _ in range(d - 1)]
    p = sphere_point(u)
    if boundary:
        return p
    r = Fr(rng.randint(0, 20), 20)
    return [r * t for t in p]


def sample_posfwd(G, tag, nsamp, seed=1):
    print(f"\n== {tag}: posFwd sample certificates (exact S-lemma certificate per sample) ==")
    rng = random.Random(seed)
    d = G.d
    z = G.z()
    pts = []
    for i in range(nsamp):
        pts.append((rand_ball_point(d, rng, i % 2 == 0), rand_ball_point(d, rng, i % 3 != 0)))
    # structured samples: corners, near-corner controls, targets at +-z and near +-z
    for t in (Fr(1, 2), Fr(1, 10), Fr(1, 100)):
        u = [t] + [ZERO] * (d - 2)
        near = sphere_point([1 / t] + [ZERO] * (d - 2))  # close to +z
        for sg in (1, -1):
            pts.append(([sg * v for v in near], z))
            pts.append(([sg * v for v in near], [-v for v in z]))
            pts.append((near, sphere_point(u)))
    ok = 0
    fails = []
    for x, y in pts:
        om = G(prod_state(x, y))
        if certify(om):
            ok += 1
        else:
            fails.append((x, y))
    check(f"{tag} posFwd certified exactly on {ok}/{len(pts)} sample product states", ok == len(pts),
          "uncertified: %d" % len(fails))
    return fails


# =====================================================================================
# Float search for violations (exploratory) + exact rational witness
# =====================================================================================

def np_gate(G):
    M = matrix_of(G, G.n)
    return np.array([[float(v) for v in r] for r in M])


def search_violation(G, seeds=60, rng_seed=7):
    n, d = G.n, G.d
    Mf = np_gate(G)

    def unpack(t):
        parts = [t[0:d], t[d:2 * d], t[2 * d:3 * d], t[3 * d:4 * d]]
        return [p / max(np.linalg.norm(p), 1e-12) for p in parts]

    def V(t):
        x, y, al, be = unpack(t)
        hx, hy = np.concatenate([[1], x]), np.concatenate([[1], y])
        om = (Mf @ np.outer(hx, hy).reshape(-1)).reshape(n, n)
        return np.concatenate([[1], al]) @ om @ np.concatenate([[1], be])
    rng = np.random.default_rng(rng_seed)
    best = (np.inf, None)
    for _ in range(seeds):
        r = minimize(V, rng.normal(size=4 * d), method="Nelder-Mead",
                     options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-12})
        if r.fun < best[0]:
            best = (r.fun, r.x)
    return best[0], unpack(best[1])


def rational_sphere_near(v, den=10 ** 4):
    """Rational unit vector near float unit vector v (inverse stereographic of rationalized chart)."""
    v = np.asarray(v, float)
    if v[-1] > 0.999999:
        v = v + 1e-6
        v = v / np.linalg.norm(v)
    u = v[:-1] / (1 - v[-1])
    return sphere_point([Fr(float(t)).limit_denominator(den) for t in u])


def exact_witness(G, tag, label):
    fmin, (x, y, al, be) = search_violation(G)
    xr, yr, ar, br = (rational_sphere_near(v) for v in (x, y, al, be))
    om = G(prod_state(xr, yr))
    v = pair_val(sharp_vec(ar), sharp_vec(br), om)
    units = all(sum(t * t for t in w) == 1 for w in (xr, yr, ar, br))
    print("     witness x =", [str(t) for t in xr], "\n     y =", [str(t) for t in yr],
          "\n     a-direction =", [str(t) for t in ar], "\n     b-direction =", [str(t) for t in br],
          "\n     exact value =", v)
    check(f"{tag} {label}: exact rational witness with unit x,y and sharp effects, value {float(v):.6f} < 0",
          units and v < 0, f"float min of (1,a).om.(1,b) = {fmin:.6f}")
    return fmin, v, (xr, yr, ar, br)


def adversarial_certify(G, tag, seeds=40):
    """Product states at which the float search drives the pairing towards its minimum, rationalized
    onto the sphere and certified exactly (finite evidence for posFwd at its tightest points)."""
    n, d = G.n, G.d
    Mf = np_gate(G)

    def unpack(t):
        parts = [t[0:d], t[d:2 * d], t[2 * d:3 * d], t[3 * d:4 * d]]
        return [p / max(np.linalg.norm(p), 1e-12) for p in parts]

    def V(t):
        x, y, al, be = unpack(t)
        hx, hy = np.concatenate([[1], x]), np.concatenate([[1], y])
        om = (Mf @ np.outer(hx, hy).reshape(-1)).reshape(n, n)
        return np.concatenate([[1], al]) @ om @ np.concatenate([[1], be])
    rng = np.random.default_rng(99)
    ok = tot = 0
    worst = np.inf
    for _ in range(seeds):
        r = minimize(V, rng.normal(size=4 * d), method="Nelder-Mead",
                     options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-12})
        worst = min(worst, r.fun)
        x, y, _, _ = unpack(r.x)
        xr, yr = rational_sphere_near(x), rational_sphere_near(y)
        tot += 1
        if certify(G(prod_state(xr, yr))):
            ok += 1
    check(f"{tag} posFwd certified exactly at {ok}/{tot} float-adversarial product states", ok == tot,
          f"float minimum found {worst:.3e}")


def float_min(G):
    fmin, _ = search_violation(G)
    return fmin


def main():
    positive_controls()
    om_gj5, _ = landed_gJ5_value()

    # certifier controls
    print("\n== certifier controls ==")
    cnot, s3, z3 = landed_cnot3()
    rng = random.Random(3)
    certified = 0
    pts3 = [(rand_ball_point(3, rng, True), rand_ball_point(3, rng, i % 2 == 0)) for i in range(40)]
    for x, y in pts3:
        if certify(cnot(prod_state(x, y))):
            certified += 1
    check("CC0+ certifier certifies landed nativeGate_cnot on 40 samples (positive control)",
          certified == len(pts3), f"{certified}/{len(pts3)}")
    rej = all(not maxcone_certificate(om_gj5, Fr(m, 8)) for m in range(0, 200))
    check("CC0- certifier rejects the gJ5 image (not in maxCone by ParityNot.gJ5_not_mem_maxCone)",
          rej and not certify(om_gj5))

    # ---------------- d = 5, eps = 1/10, lam = 1/2 ----------------
    G5 = Squeezed(2, Fr(1, 10), Fr(1, 2))
    tag = "d=5(eps=1/10,lam=1/2)"
    Gs5 = algebraic_clauses(G5, tag)
    posinv_witness(G5, Gs5, tag)
    decomposition_identity(G5, tag)
    sample_posfwd(G5, tag, 200)
    adversarial_certify(G5, tag)
    fmin = float_min(G5)
    print(f"INFO {tag} exploratory float minimum of the normalized pairing over unit x,y and sharp a,b: "
          f"{fmin:.3e} (not a certificate)")

    # ---------------- countercontrols at d = 5 ----------------
    print("\n== countercontrols at d = 5 (each must FAIL posFwd with an exact witness) ==")
    Gnosq = Squeezed(2, Fr(1, 10), Fr(1))            # no squeeze: Mfwd = id
    algebraic_clauses(Gnosq, "d=5(eps=1/10,lam=1)")
    exact_witness(Gnosq, "d=5(eps=1/10,lam=1)", "no-squeeze countercontrol fails posFwd")
    # the clean witness predicted by the decomposition identity (A = B = 0, S_e = -1):
    x5 = [ONE, ZERO, ZERO, ZERO, ZERO]
    y2 = [ZERO, ONE, ZERO, ZERO, ZERO]
    v = pair_val(sharp_vec(x5), sharp_vec([-t for t in y2]), Gnosq(prod_state(x5, y2)))
    check("d=5(eps=1/10,lam=1) clean witness prodEffVal (sharpEff e1) (sharpEff -e2) (G (prodState e1 e2)) = -eps/4",
          v == -Gnosq.eps / 4, str(v))
    v2 = pair_val(sharp_vec(x5), sharp_vec([-t for t in y2]), G5(prod_state(x5, y2)))
    check("d=5(eps=1/10,lam=1/2) same test on the squeezed gate: ((1-lam) - eps*lam)/4 = 9/80 >= 0",
          v2 == ((1 - G5.lam) - G5.eps * G5.lam) / 4, str(v2))
    Gbig = Squeezed(2, Fr(1), Fr(1, 2))               # eps too large
    exact_witness(Gbig, "d=5(eps=1,lam=1/2)", "large-eps countercontrol fails posFwd")

    # ---------------- other odd d ----------------
    for k, ns in ((1, 80), (3, 60)):
        Gk = Squeezed(k, Fr(1, 16), Fr(1, 2))
        tagk = f"d={2 * k + 1}(eps=1/16,lam=1/2)"
        Gsk = algebraic_clauses(Gk, tagk)
        posinv_witness(Gk, Gsk, tagk)
        decomposition_identity(Gk, tagk)
        sample_posfwd(Gk, tagk, ns, seed=11 + k)
    G5b = Squeezed(2, Fr(1, 16), Fr(1, 2))
    sample_posfwd(G5b, "d=5(eps=1/16,lam=1/2)", 60, seed=5)

    nfail = sum(1 for _, ok in CHECKS if not ok)
    print(f"\nTOTAL {len(CHECKS)} checks, {nfail} failed")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
