#!/usr/bin/env python3
"""F2-1 correction 1: the scope of the square-root scans, decided exactly.

Run:  python3 -I root_scope_check.py > root-scope-check-output.txt
Imports the frozen F2-1 arithmetic (../e1_exact.py) by path and changes nothing in it.
Every line is exact unless tagged; [W] marks a written argument.

The F2-1 scans cover the spectral square roots of U_0: one sign per eigenspace. Any square root V
of U commutes with U = V^2, so it preserves each eigenspace E_l of U, and V|E_l squares to l; hence
V|E_l = sqrt(l) R_l with R_l Hermitian unitary, R_l = 2Q - 1 for a projector Q inside E_l [W]. The
spectral roots are the cases R_l = +-1. They exhaust the square roots iff every eigenspace is
one-dimensional.
"""
import importlib.util
import itertools
import os
from fractions import Fraction

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("e1_exact", os.path.join(_here, "..", "e1_exact.py"))
e1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e1)

out = e1.out
SIZES = [(3, 1), (5, 1), (3, 2)]


def trace_frac(F, P):
    s = F.zero
    for i in range(len(P)):
        s = F.add(s, P[i][i])
    return F.to_frac(s)


def inner(F, a, b):
    """<a|b>, antilinear in a."""
    s = F.zero
    for x, y in zip(a, b):
        if not F.is_zero(x) and not F.is_zero(y):
            s = F.add(s, F.mul(F.conj(x), y))
    return s


def vscale(F, c, v):
    return [F.mul(c, x) for x in v]


def first_nz(F, v):
    return next((i for i, x in enumerate(v) if not F.is_zero(x)), None)


def stabilizer_rays(C, gens):
    """Orbit of the ray of |0...0> under the given generators (exact, by ray keys)."""
    F = C.F
    v0 = C.basis_vec((0,) * C.N)
    seen = {e1.ray_key(F, v0): v0}
    frontier = [v0]
    while frontier:
        new = []
        for v in frontier:
            for g in gens:
                w = e1.mat_vec(F, g, v)
                k = e1.ray_key(F, w)
                if k not in seen:
                    seen[k] = w
                    new.append(w)
        frontier = new
    return [seen[k] for k in sorted(seen)]


def reachable_by_root(F, spec, dims, sq, v0, psi, spectral_only):
    """Is psi proportional to V v0 for some square root V of U (all roots, or spectral roots only)?

    V v0 = sum_l sqrt(l) R_l v_l with v_l = P_l v0. For dim E_l = 1, R_l = +-1. For dim E_l >= 2,
    R_l v_l ranges over the w in E_l with <w|w> = <v_l|v_l> and <v_l|w> real (reflection through
    the line of v_l + w; -v_l by R_l = -1) [W]; spectral roots allow only w = +-v_l.
    """
    comps = []
    for (j, P), dl in zip(spec, dims):
        comps.append((dl, sq[j], e1.mat_vec(F, P, v0), e1.mat_vec(F, P, psi)))
    for dl, s, vl, pl in comps:
        if (first_nz(F, vl) is None) != (first_nz(F, pl) is None):
            return False
    one = [(s, vl, pl) for dl, s, vl, pl in comps if dl == 1 and first_nz(F, vl) is not None]
    many = [(s, vl, pl) for dl, s, vl, pl in comps if dl >= 2 and first_nz(F, vl) is not None]
    c = None
    for s, vl, pl in one:
        i = first_nz(F, vl)
        r = F.div(F.mul(s, vl[i]), pl[i])            # r * pl = s * vl  (both in a line)
        if c is None:
            c = r
        elif r != c and r != F.neg(c):
            return False
    if c is None:
        # no one-dimensional component fixes the phase: norms must agree up to one common |c|^2, and
        # one phase must make every <v_l | psi_l / sqrt(l)> real
        if not many:
            return True
        if spectral_only:
            # c psi_l / sqrt(l) = +-v_l for one common c: fix c on the first component
            s, vl, pl = many[0]
            i = first_nz(F, vl)
            if F.is_zero(pl[i]):
                return False                         # psi_l is not proportional to v_l
            c = F.div(F.mul(s, vl[i]), pl[i])
            for s, vl, pl in many:
                w = vscale(F, F.div(c, s), pl)
                if w != vl and w != vscale(F, F.neg(F.one), vl):
                    return False
            return True
        ratios = set()
        a = []
        for s, vl, pl in many:
            ratios.add(F.div(inner(F, vl, vl), inner(F, pl, pl)))
            a.append(inner(F, vl, vscale(F, F.inv(s), pl)))
        if len(ratios) != 1:
            return False
        nz = [x for x in a if not F.is_zero(x)]
        if not nz:
            return True
        return all(F.is_real(F.div(x, nz[0])) for x in nz)
    for s, vl, pl in many:
        w = vscale(F, F.div(c, s), pl)
        if spectral_only:
            if w != vl and w != vscale(F, F.neg(F.one), vl):
                return False
            continue
        if inner(F, w, w) != inner(F, vl, vl):
            return False
        if not F.is_real(inner(F, vl, w)):
            return False
    return True


def wigner_nonneg(C, v):
    W = e1.wigner(C, v)
    return all(e1.real_sign(C.F, x) >= 0 for x in W.values())


def spectral_roots(F, spec, order):
    th = [e1.principal_theta(j, order) for j, _ in spec]
    roots = []
    for sg in itertools.product((1, -1), repeat=len(spec)):
        roots.append(e1.sqrt_from(F, spec, order, th, sg))
    return roots


def run(q, N):
    size = "q=%d,N=%d" % (q, N)
    e1.header("[%s] square roots of U_0, the canonical image of the zero-coupling leap" % size)
    Fq = e1.field(q)
    Cq = e1.Carrier(q, N, Fq)
    rho_J, _, _ = e1.canonical_weil(Cq)
    M0 = tuple(tuple(0 for _ in range(N)) for _ in range(N))
    L0 = e1.leap_matrix(M0, q)
    o0 = e1.cmat_order(L0, q)
    F = e1.field(e1.lcm(q, 2 * o0))
    C = e1.Carrier(q, N, F)
    U0 = e1.mat_embed(F, e1.rho_leap(Cq, rho_J, M0), Fq)
    spec = e1.spectral(F, U0, o0)
    dims = [trace_frac(F, P) for _, P in spec]
    sq = {j: F.root(2 * o0, j) for j, _ in spec}         # a square root of zeta_o0^j
    out("field Q(zeta_%d); U_0 has order %d; eigenvalue zeta_%d^j : multiplicity  %s"
        % (F.n, o0, o0, "  ".join("j=%d:%s" % (j, dl) for (j, _), dl in zip(spec, dims))))
    k = len(spec)
    nondeg = all(dl == 1 for dl in dims)
    out("spectral square roots (one sign per eigenspace): %d, i.e. %d modulo global phase" % (2 ** k, 2 ** (k - 1)))
    out("every eigenspace one-dimensional: %s -> the spectral roots are %s the square roots [W]"
        % (nondeg, "all of" if nondeg else "a proper subset of (a continuum exists)"))
    res = {"nondeg": nondeg}

    # Clifford square roots: V Clifford with V^2 = c U_0 needs a symplectic S with S^2 = J'_N (the
    # linear part of L_0) [W]: (a, S)^2 = (a + S a, S^2) in ASp; a = 0 then works, and V is rephased.
    gens = [e1.leap_matrix(M, q) for M in e1.symmetric_couplings(q, N)]
    Sp = e1.group_closure(gens, q)
    assert len(Sp) == e1.sp_order(N, q)
    sqrtS = [S for S in Sp if e1.cmat_mul(S, S, q) == L0]
    out("Sp(%d, %d) enumerated (%d elements); symplectic S with S^2 = J'_N: %d"
        % (2 * N, q, len(Sp), len(sqrtS)))
    res["clifford_root_exists"] = bool(sqrtS)
    out("-> a Clifford square root of U_0 (up to rephasing) %s [W from the count]"
        % ("exists" if sqrtS else "does not exist: every square root of U_0 is non-Clifford"))

    # stabilizer states and which of them a square root of U_0 can reach from |0...0>
    Ugens = [e1.mat_embed(F, e1.rho_leap(Cq, rho_J, M), Fq) for M in e1.symmetric_couplings(q, N)]
    Ugens += [C.X(i) for i in range(N)] + [C.Z(i) for i in range(N)]
    rays = stabilizer_rays(C, Ugens)
    v0 = C.basis_vec((0,) * N)
    by_all = [psi for psi in rays if reachable_by_root(F, spec, dims, sq, v0, psi, False)]
    by_spec = [psi for psi in rays if reachable_by_root(F, spec, dims, sq, v0, psi, True)]
    out("stabilizer rays (Clifford orbit of |0...0>): %d" % len(rays))
    out("stabilizer rays equal to V|0...0> for some square root V of U_0: %d; for a spectral root: %d"
        % (len(by_all), len(by_spec)))
    # cross-check of the spectral count against the explicit spectral roots
    sroots = spectral_roots(F, spec, o0)
    keys = {e1.ray_key(F, psi) for psi in rays}
    hits = sum(1 for V in sroots if e1.ray_key(F, e1.mat_vec(F, V, v0)) in keys)
    out("cross-check: explicit spectral roots (%d) mapping |0...0> to a stabilizer ray: %d" % (len(sroots), hits))
    res["xcheck"] = (hits == 0) == (len(by_spec) == 0)
    # positive control of the reachability test: every explicit spectral root's image of |0...0>
    # must be reported reachable, by the all-roots test and by the spectral-only test
    pos = all(reachable_by_root(F, spec, dims, sq, v0, e1.mat_vec(F, V, v0), so)
              for V in sroots for so in (False, True))
    out("positive control: the test reports V|0...0> reachable for each of the %d spectral roots V, "
        "in both modes: %s" % (len(sroots), pos))
    res["pos"] = pos
    nonneg_ok = all(wigner_nonneg(C, psi) for psi in by_all)
    out("those reached by some root have nonnegative Wigner function (stabilizer states): %s" % nonneg_ok)
    res["by_all"] = len(by_all)
    res["by_spec"] = len(by_spec)
    res["stab_nonneg"] = nonneg_ok

    if N == 2:
        e1.header("[%s] the two square roots named in the owner's review" % size)
        F1 = e1.field(q)
        C1 = e1.Carrier(q, 1, F1)
        rho_J1, _, _ = e1.canonical_weil(C1)
        U1 = e1.mat_embed(F, e1.rho_leap(C1, rho_J1, ((0,),)), F1)
        out("U_0 = U (x) U with U the one-site image: %s" % e1.mat_eq(U0, e1.kron(F, U1, U1)))
        sp1 = e1.spectral(F, U1, 4)
        V1 = e1.sqrt_from(F, sp1, 4, [e1.principal_theta(j, 4) for j, _ in sp1], [1] * len(sp1))
        P = e1.kron(F, V1, V1)
        I1 = e1.eye(F, q)
        SW = e1.zeros(F, q * q)
        for a in range(q):
            for b in range(q):
                SW[b * q + a][a * q + b] = F.one
        Cm = e1.mat_mul(F, e1.kron(F, U1, I1), SW)
        for name, V in (("V (x) V, V the principal root of U", P), ("C = (U (x) 1) SWAP", Cm)):
            sq_ok = e1.mat_eq(e1.mat_mul(F, V, V), U0)
            un = e1.unitary_check(F, V)
            spectral_member = any(e1.proportional_scalar(F, V, R) is not None for R in sroots)
            nf = e1.normalizer_failures(C, V)
            rk = e1.schmidt_rank(F, V, q)
            st = e1.mat_vec(F, V, v0)
            nn = wigner_nonneg(C, st)
            found = e1.ray_key(F, st) in {e1.ray_key(F, psi) for psi in by_all}
            out("  %s|00> is among the stabilizer rays the all-roots test reports reachable: %s" % (name[:1], found))
            res["found " + name] = found or not nn
            out("%-38s V^2 = U_0: %s | unitary: %s | proportional to a spectral root: %s | operator-Schmidt "
                "rank %d | Clifford: %s | Wigner of V|00> nonnegative: %s"
                % (name, sq_ok, un, spectral_member, rk, not nf, nn))
            res[name] = (sq_ok and un and not spectral_member, rk, not nf, nn)
    return res


def main():
    out("F2-1 correction 1 (2026-10-15): scope of the square-root scans. Imports ../e1_exact.py unchanged.")
    R = {}
    for q, N in SIZES:
        R[(q, N)] = run(q, N)
    e1.header("Summary")
    ok = True
    for (q, N), r in R.items():
        ok &= r["xcheck"] and r["stab_nonneg"] and r["pos"]
        out("q=%d,N=%d: spectral family exhaustive %s | Clifford root exists %s | stabilizer rays reached by some "
            "root %d, by a spectral root %d" % (q, N, r["nondeg"], r["clifford_root_exists"], r["by_all"], r["by_spec"]))
    r2 = R[(3, 2)]
    a = r2["V (x) V, V the principal root of U"]
    b = r2["C = (U (x) 1) SWAP"]
    ok &= a[0] and b[0] and r2["found C = (U (x) 1) SWAP"]
    out("q=3,N=2: V (x) V is a non-spectral square root of operator-Schmidt rank %d, Clifford %s; "
        "C is a non-spectral square root, Clifford %s, Wigner of C|00> nonnegative %s" % (a[1], a[2], b[2], b[3]))
    out("controls (spectral cross-check, positive reachability control, stabilizer nonnegativity, both named roots "
        "genuine and non-spectral, C|00> found by the all-roots test): %s"
        % ("PASS" if ok else "FAIL"))


if __name__ == "__main__":
    main()
