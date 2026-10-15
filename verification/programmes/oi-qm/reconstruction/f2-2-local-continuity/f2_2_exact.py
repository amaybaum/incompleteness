#!/usr/bin/env python3
"""F2-2: exact computations for candidate E1-L (E1 with local continuity), as frozen in RULES.md.

Run:  python3 -I f2_2_exact.py > f2-2-exact-output.txt
Standard library only. Imports, by path and unchanged, the frozen F2-1 module
../f2-1-e1-consistency/e1_exact.py and the F2-1 correction-1 module
../f2-1-e1-consistency/corrections/root_scope_check.py, and prints their sha256.
Labels: [X] exact (every line unless tagged), [W] written argument, [L] literature, [K] kernel.
The output is deterministic (no randomness, no timing, no hash-order dependence).
"""
import hashlib
import importlib.util
import itertools
import os
from fractions import Fraction
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
E1_PATH = os.path.join(HERE, "..", "f2-1-e1-consistency", "e1_exact.py")
RS_PATH = os.path.join(HERE, "..", "f2-1-e1-consistency", "corrections", "root_scope_check.py")
E1_SHA = "e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


e1 = _load("e1_exact", E1_PATH)
rs = _load("root_scope_check", RS_PATH)
rs.e1 = e1

out = e1.out
header = e1.header
CTRL = []          # (name, bool) — every control; a failure voids every verdict
TOK = []           # (cell, size, token)


def control(name, ok):
    CTRL.append((name, bool(ok)))
    out("CONTROL %-46s %s" % (name, "PASS" if ok else "FAIL"))


def token(cell, size, tok):
    TOK.append((cell, size, tok))
    e1.token(cell, size, tok)


def summary(flags):
    return e1.summary_tag(flags)


def sym_rep(e, q):
    e %= q
    return e if 2 * e <= q else e - q


def root(F, r):
    """exp(2 pi i r) for rational r."""
    r = Fraction(r)
    return F.root(r.denominator, r.numerator % r.denominator) if r.denominator > 1 else F.one


def lcm(*xs):
    return e1.lcm(*xs)


# ============================================================================ local gates


class Gate:
    """A local gate with its spectral data.

    kind 'proj': projectors P_k (on the gate's own sites) for eigenvalue keys k, with principal
    theta0[k] (eigenphase / 2 pi in (-1/2, 1/2]).
    kind 'diag': exponent function expo(y) on the gate's sites, gate = diag(w^expo(y)); eigenvalue
    keys are the distinct exponents, theta0[e] = rep(e)/q with rep in (-q/2, q/2].
    A member is a tuple of integer lifts aligned with self.keys: theta = theta0 + lift.
    """

    def __init__(self, name, F, q, nsites, kind, data):
        self.name, self.F, self.q, self.nsites, self.kind = name, F, q, nsites, kind
        self.dim = q ** nsites
        if kind == "proj":
            spec, order = data
            self.keys = [j for j, _ in spec]
            self.P = {j: P for j, P in spec}
            self.theta0 = {j: e1.principal_theta(j, order) for j in self.keys}
            self.mult = {j: rs.trace_frac(F, self.P[j]) for j in self.keys}
        else:
            self.expo = data
            pts = list(itertools.product(range(q), repeat=nsites))
            vals = sorted({data(y) for y in pts})
            self.keys = vals
            self.theta0 = {e: Fraction(sym_rep(e, q), q) for e in vals}
            self.mult = {e: sum(1 for y in pts if data(y) == e) for e in vals}
            self.pts = pts

    def principal(self):
        return tuple(0 for _ in self.keys)

    def theta(self, member):
        return {k: self.theta0[k] + n for k, n in zip(self.keys, member)}

    def nondegenerate(self):
        return all(m == 1 for m in self.mult.values())

    def gen(self, member):
        th = self.theta(member)
        F = self.F
        if self.kind == "proj":
            G = e1.zeros(F, self.dim)
            for k in self.keys:
                if th[k] != 0:
                    G = e1.mat_add(F, G, e1.mat_scale(F, F.frac(th[k]), self.P[k]))
            return G
        G = e1.zeros(F, self.dim)
        for i, y in enumerate(self.pts):
            G[i][i] = F.frac(th[self.expo(y)])
        return G

    def flow(self, member, s):
        th = self.theta(member)
        F = self.F
        if self.kind == "proj":
            U = e1.zeros(F, self.dim)
            for k in self.keys:
                U = e1.mat_add(F, U, e1.mat_scale(F, root(F, s * th[k]), self.P[k]))
            return U
        U = e1.zeros(F, self.dim)
        for i, y in enumerate(self.pts):
            U[i][i] = root(F, s * th[self.expo(y)])
        return U

    def diag_theta(self, member):
        """For diag gates: y -> theta(expo(y))."""
        th = self.theta(member)
        return lambda y: th[self.expo(y)]


def one_site_u(Fq, q):
    C1 = e1.Carrier(q, 1, Fq)
    rho_J, _, _ = e1.canonical_weil(C1)
    return e1.rho_leap(C1, rho_J, ((0,),))


class GateSet:
    """The gates of E1-L at one alphabet q in field F: u, X, site chirps delta(m), pair chirps delta(m)."""

    def __init__(self, q, F):
        self.q, self.F = q, F
        Fq = e1.field(q)
        self.Fq = Fq
        h = pow(2, -1, q)
        self.h = h
        u = e1.mat_embed(F, one_site_u(Fq, q), Fq)
        self.u_mat = u
        C1 = e1.Carrier(q, 1, F)
        self.X_mat = C1.X(0)
        self.Z_mat = C1.Z(0)
        self.gates = {}
        self.gates["u"] = Gate("u", F, q, 1, "proj", (e1.spectral(F, u, 4), 4))
        self.gates["X"] = Gate("X", F, q, 1, "proj", (e1.spectral(F, self.X_mat, q), q))
        for m in range(1, q):
            self.gates[("site", m)] = Gate(("site", m), F, q, 1, "diag",
                                           (lambda mm: (lambda y: (-h * mm * y[0] * y[0]) % q))(m))
            self.gates[("pair", m)] = Gate(("pair", m), F, q, 2, "diag",
                                           (lambda mm: (lambda y: (-mm * y[0] * y[1]) % q))(m))

    def principal_member(self):
        return {k: g.principal() for k, g in self.gates.items()}

    def shifted_member(self):
        """Every theta lifted by +1 except the smallest principal one (per gate)."""
        mem = {}
        for k, g in self.gates.items():
            lo = min(g.keys, key=lambda kk: (g.theta0[kk], kk))
            mem[k] = tuple(0 if kk == lo else 1 for kk in g.keys)
        return mem


# ============================================================================ the N-site construction


class Sites:
    def __init__(self, GS, N):
        self.GS, self.N = GS, N
        q = GS.q
        self.q = q
        self.F = GS.F
        self.C = e1.Carrier(q, N, GS.F)
        self.d = q ** N
        self.pts = self.C.pts

    def kron_list(self, mats):
        A = mats[0]
        for B in mats[1:]:
            A = e1.kron(self.F, A, B)
        return A

    def embed1(self, A, site):
        I = e1.eye(self.F, self.q)
        return self.kron_list([A if i == site else I for i in range(self.N)])

    def free_flow(self, member, s):
        f = self.GS.gates["u"].flow(member["u"], s)
        return self.kron_list([f] * self.N)

    def coup_terms(self, M):
        """The coupling layer's gates: [(sites, gate)] for the self-couplings and the coupled pairs."""
        GS, N, q = self.GS, self.N, self.q
        terms = []
        for i in range(N):
            if M[i][i] % q:
                terms.append(((i,), GS.gates[("site", M[i][i] % q)]))
        for i in range(N):
            for j in range(i + 1, N):
                if M[i][j] % q:
                    terms.append(((i, j), GS.gates[("pair", M[i][j] % q)]))
        return terms

    def coup_theta(self, M, member):
        """y -> total theta of the coupling layer generator for coupling M."""
        terms = [(sites, g.diag_theta(member[g.name])) for sites, g in self.coup_terms(M)]

        def th(y):
            s = Fraction(0)
            for sites, f in terms:
                s += f(tuple(y[k] for k in sites))
            return s
        return th

    def coup_flow(self, M, member, s, extra=None):
        F = self.F
        th = self.coup_theta(M, member)
        D = e1.zeros(F, self.d)
        for i, y in enumerate(self.pts):
            t = th(y)
            if extra is not None:
                t += extra(y)
            D[i][i] = root(F, s * t)
        return D

    def U(self, M, member, t, extra=None):
        t = Fraction(t)
        n = t.numerator // t.denominator
        f = t - n
        F = self.F
        one = e1.mat_mul(F, self.free_flow(member, 1), self.coup_flow(M, member, 1, extra))
        if f == 0:
            R = e1.eye(F, self.d)
        else:
            sc = min(2 * f, Fraction(1))
            sf = max(2 * f - 1, Fraction(0))
            R = e1.mat_mul(F, self.free_flow(member, sf), self.coup_flow(M, member, sc, extra))
        for _ in range(n):
            R = e1.mat_mul(F, R, one)
        return R

    # generators, as matrices and as linear combinations of projector sums (for the touching test)
    def gen_free(self, member):
        G = self.GS.gates["u"].gen(member["u"])
        F = self.F
        tot = e1.zeros(F, self.d)
        for i in range(self.N):
            tot = e1.mat_add(F, tot, self.embed1(G, i))
        return tot

    def gen_coup(self, M, member):
        F = self.F
        th = self.coup_theta(M, member)
        D = e1.zeros(F, self.d)
        for i, y in enumerate(self.pts):
            D[i][i] = F.frac(th(y))
        return D

    def gen_X(self, member, k):
        return self.embed1(self.GS.gates["X"].gen(member["X"]), k)

    def lin_free(self):
        """[(param key, matrix)] with gen_free = sum (theta0 + n)[key] * matrix."""
        g = self.GS.gates["u"]
        res = []
        for kk in g.keys:
            tot = e1.zeros(self.F, self.d)
            for i in range(self.N):
                tot = e1.mat_add(self.F, tot, self.embed1(g.P[kk], i))
            res.append((("u", kk), tot))
        return res

    def lin_X(self, k):
        g = self.GS.gates["X"]
        return [(("X", kk), self.embed1(g.P[kk], k)) for kk in g.keys]

    def lin_coup(self, M):
        """[(param key, diagonal matrix)]: gen_coup = sum over keys of theta[key] * (count of the layer's
        terms of that gate taking that exponent at y)."""
        F = self.F
        acc = {}
        for sites, g in self.coup_terms(M):
            for idx, y in enumerate(self.pts):
                key = (g.name, g.expo(tuple(y[k] for k in sites)))
                dct = acc.setdefault(key, {})
                dct[idx] = dct.get(idx, 0) + 1
        res = []
        for key in sorted(acc, key=str):
            D = e1.zeros(F, self.d)
            for idx, c in acc[key].items():
                D[idx][idx] = F.frac(c)
            res.append((key, D))
        return res


def is_prop(F, A, B):
    return e1.proportional_scalar(F, A, B) is not None


# ============================================================================ classical helpers


def leap(M, q):
    return e1.leap_matrix(M, q)


def orbits(gens, q, n2):
    pts = [p for p in itertools.product(range(q), repeat=n2) if any(p)]
    seen = {}
    orbs = []
    for p in pts:
        if p in seen:
            continue
        orb = [p]
        seen[p] = len(orbs)
        fr = [p]
        while fr:
            nw = []
            for v in fr:
                for g in gens:
                    w = tuple(e1.cmat_vec(g, v, q))
                    if w not in seen:
                        seen[w] = len(orbs)
                        orb.append(w)
                        nw.append(w)
            fr = nw
        orbs.append(sorted(orb))
    return orbs, seen


def rank_mod(vecs, q):
    rows = [list(v) for v in vecs]
    r = 0
    ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        p = next((i for i in range(r, len(rows)) if rows[i][c] % q), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        iv = pow(rows[r][c], -1, q)
        rows[r] = [(x * iv) % q for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % q:
                f = rows[i][c]
                rows[i] = [(x - f * y) % q for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def symmetric(q, N, centre_free):
    Ms = e1.symmetric_couplings(q, N)
    if centre_free:
        Ms = [M for M in Ms if all(M[i][i] == 0 for i in range(N))]
    return Ms


def fmtM(M):
    return e1.fmtM(M)


# ============================================================================ integer feasibility


def egcd(a, b):
    """(g, x, y) with x a + y b = g = gcd(a, b) >= 0."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        qt = a // b
        a, b = b, a - qt * b
        x0, x1 = x1, x0 - qt * x1
        y0, y1 = y1, y0 - qt * y1
    if a < 0:
        a, x0, y0 = -a, -x0, -y0
    return a, x0, y0


def int_solve(A, b):
    """Integer solutions n of A n = b (A rational r x k, b rational). Returns None if there is none,
    else (particular solution, kernel basis) with integer vectors."""
    r = len(A)
    k = len(A[0]) if r else 0
    rows = []
    rhs = []
    for row, bi in zip(A, b):
        L = 1
        for x in list(row) + [bi]:
            L = L * Fraction(x).denominator // gcd(L, Fraction(x).denominator)
        rows.append([int(Fraction(x) * L) for x in row])
        rhs.append(int(Fraction(bi) * L))
    U = [[int(i == j) for j in range(k)] for i in range(k)]
    pc = 0
    piv = {}
    for i in range(r):
        if pc < k:
            for c in range(pc + 1, k):
                if rows[i][c] != 0:
                    a, bb = rows[i][pc], rows[i][c]
                    g, x, y = egcd(a, bb)
                    ag, bg = a // g, bb // g
                    for R in rows:
                        cp, cc = R[pc], R[c]
                        R[pc], R[c] = x * cp + y * cc, -bg * cp + ag * cc
                    for R in U:
                        cp, cc = R[pc], R[c]
                        R[pc], R[c] = x * cp + y * cc, -bg * cp + ag * cc
            if pc < k and rows[i][pc] != 0:
                piv[i] = pc
                pc += 1
    yv = [0] * k
    for i in range(r):
        s = sum(rows[i][c] * yv[c] for c in range(k) if rows[i][c] and c < pc and (i not in piv or c < piv[i]))
        if i in piv:
            c = piv[i]
            num = rhs[i] - s
            if num % rows[i][c]:
                return None
            yv[c] = num // rows[i][c]
        else:
            if s != rhs[i]:
                return None
    n_p = [sum(U[a][c] * yv[c] for c in range(k)) for a in range(k)]
    kern = [[U[a][c] for a in range(k)] for c in range(pc, k)]
    # verification of the particular solution, exactly
    for row, bi in zip(A, b):
        assert sum(Fraction(x) * v for x, v in zip(row, n_p)) == Fraction(bi)
    return n_p, kern


def lattice_points(sol, limit=8, box=2):
    n_p, kern = sol
    pts = set()
    for cs in itertools.product(range(-box, box + 1), repeat=len(kern)):
        v = tuple(n_p[a] + sum(c * kv[a] for c, kv in zip(cs, kern)) for a in range(len(n_p)))
        pts.add(v)
    return sorted(pts, key=lambda v: (max([abs(x) for x in v] + [0]), v))[:limit]


# ============================================================================ touching (adjoint support)


def weyl_cols(C, z):
    N = C.N
    return C.weyl_mono(tuple(z[:N]), tuple(z[N:]))


def coeff_nonzero_set(C, A, zlist, wcols):
    """Set of z in zlist with tr(W(z)^dagger A) != 0."""
    F = C.F
    res = set()
    for z in zlist:
        s = F.zero
        for col, (t, e) in enumerate(wcols[z]):
            a = A[t][col]
            if not F.is_zero(a):
                s = F.add(s, F.mul(C.om[(-e) % C.q], a))
        if not F.is_zero(s):
            res.add(z)
    return res


def adjoint_relation(C, h, zlist, wcols):
    """z -> set of z' with nonzero W(z')-coefficient in h W(z) h^dagger (and the same for h^dagger)."""
    F = C.F
    rel = {}
    for hh in (h, e1.adjoint(F, h)):
        hd = e1.adjoint(F, hh)
        for z in zlist:
            # hh W(z): column col of W(z) is w^e e_t, so (hh W)[:, col] = w^e hh[:, t]
            hW = [[F.zero] * C.d for _ in range(C.d)]
            for col, (t, e) in enumerate(wcols[z]):
                c = C.om[e]
                for r_ in range(C.d):
                    a = hh[r_][t]
                    if not F.is_zero(a):
                        hW[r_][col] = F.mul(c, a)
            A = e1.mat_mul(F, hW, hd)
            rel.setdefault(z, set()).update(coeff_nonzero_set(C, A, zlist, wcols))
    return rel


def components(C, mats, zlist, wcols):
    """comp[z][i] = tr(W(z)^dagger mats[i]) / d (exact)."""
    F = C.F
    inv_d = F.frac(Fraction(1, C.d))
    comp = {}
    for z in zlist:
        row = []
        for A in mats:
            s = F.zero
            for col, (t, e) in enumerate(wcols[z]):
                a = A[t][col]
                if not F.is_zero(a):
                    s = F.add(s, F.mul(C.om[(-e) % C.q], a))
            row.append(F.mul(s, inv_d))
        comp[z] = row
    return comp


def coords(F, a):
    c, d = a
    return [Fraction(x, d) for x in c]


# ============================================================================ L cells


def locality_cells(R):
    q = 3
    Floc = e1.field(72)
    GS = GateSet(q, Floc)
    members = [("principal", GS.principal_member()), ("shifted", GS.shifted_member())]
    times = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(3, 2)]

    header("L0  factorization rho(L_M) = u^(x)N D(M), exact")
    Fq = e1.field(q)
    l0 = True
    for (qq, N) in [(3, 1), (5, 1), (7, 1), (3, 2), (3, 3)]:
        Fs = e1.field(qq)
        Cs_ = e1.Carrier(qq, N, Fs)
        rho_J, _, _ = e1.canonical_weil(Cs_)
        Fx = e1.field(4 * qq)
        GSx = GateSet(qq, Fx)
        Sx = Sites(GSx, N)
        if N < 3:
            Ms = e1.symmetric_couplings(qq, N)
        else:
            Ms = symmetric(qq, N, True)
            Ms += [((0, a, 0), (a, 0, 0), (0, 0, m)) for a in range(qq) for m in range(1, qq)]
        ok = True
        unit = True
        mem = GSx.principal_member()
        for M in Ms:
            rho = e1.mat_embed(Fx, e1.rho_leap(Cs_, rho_J, M), Fs)
            fac = Sx.U(M, mem, 1)
            ok &= e1.mat_eq(rho, fac)
            unit &= e1.unitary_check(Fx, rho)
        out("(q,N)=(%d,%d): couplings tested %d; identity exact for all: %s; images unitary: %s"
            % (qq, N, len(Ms), ok, unit))
        l0 &= ok and unit
        R.setdefault("L0", {})[(qq, N)] = ok and unit
    token("L0", "all sizes", "E1L-FACTORIZED" if l0 else "E1L-NOT-FACTORIZED")
    R["L0ok"] = l0
    out("[W] U(1) = u^(x)N D(M) for every member of Gamma_all: e^{2 pi i G_g} = g for each gate, by definition")

    header("L1  uncoupled independence: U_AB(t) ~ U_A(t) (x) U_B(t), two code paths, exact")
    S1 = Sites(GS, 1)
    S2 = Sites(GS, 2)
    S3 = Sites(GS, 3)
    l1 = True
    cases = []
    for m1 in range(q):
        for m2 in range(q):
            cases.append((S2, ((m1, 0), (0, m2)), S1, ((m1,),), S1, ((m2,),)))
    for a in range(q):
        for m in range(q):
            cases.append((S3, ((0, a, 0), (a, 0, 0), (0, 0, m)), S2, ((0, a), (a, 0)), S1, ((m,),)))
    ncheck = 0
    for name, mem in members:
        okm = True
        for SN, M, SA, MA, SB, MB in cases:
            for t in times:
                UN = SN.U(M, mem, t)
                UP = e1.kron(Floc, SA.U(MA, mem, t), SB.U(MB, mem, t))
                okm &= is_prop(Floc, UN, UP)
                ncheck += 1
        out("member %-9s: %d block-diagonal couplings ((3,2): %d, (3,3): %d) x %d times: all equal up to "
            "phase: %s" % (name, len(cases), q * q, q * q, len(times), okm))
        l1 &= okm
    out("checks: %d" % ncheck)
    out("[W] for every member of Gamma_all: a block-diagonal coupling has no gate across the blocks, so each "
        "layer generator is G_A (x) 1 + 1 (x) G_B, and its flow factorizes for every duration")
    # countercontrol K-L1: F2-1's composite principal-log rule at (3,2), M = 0
    Fk = e1.field(144)            # the composite rule at t = 3/4 needs zeta_16
    U0 = e1.mat_embed(Fk, S2.U(((0, 0), (0, 0)), GS.principal_member(), 1), Floc)
    spec0 = e1.spectral(Fk, U0, 4)
    th0 = [e1.principal_theta(j, 4) for j, _ in spec0]
    u1 = e1.mat_embed(Fk, GS.u_mat, Floc)
    spec1 = e1.spectral(Fk, u1, 4)
    th1 = [e1.principal_theta(j, 4) for j, _ in spec1]

    def pflow(spec, th, t):
        Uo = e1.zeros(Fk, len(spec[0][1]))
        for (j, P), x in zip(spec, th):
            Uo = e1.mat_add(Fk, Uo, e1.mat_scale(Fk, root(Fk, t * x), P))
        return Uo
    fails = []
    for t in times:
        UT = pflow(spec0, th0, t)
        UA = pflow(spec1, th1, t)
        if not is_prop(Fk, UT, e1.kron(Fk, UA, UA)):
            fails.append(str(t))
    out("K-L1: F2-1's composite principal-log rule at (3,2), M = 0: independence fails at t = %s" % fails)
    control("K-L1 composite-log countercontrol detected", bool(fails))
    token("L1", "(3,2),(3,3)", "E1L-INDEPENDENT" if l1 else "E1L-NOT-INDEPENDENT")
    R["L1ok"] = l1

    header("L3  strict causal cone at (3,3): chains [[0,a,0],[a,0,b],[0,b,0]], exact")
    C3 = S3.C
    X1, Z1, X3, Z3 = C3.X(0), C3.Z(0), C3.X(2), C3.Z(2)
    l3 = True
    tcone = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]

    def heis(Ut, O):
        return e1.mat_mul(Floc, e1.adjoint(Floc, Ut), e1.mat_mul(Floc, O, Ut))

    def comm(A, B):
        return e1.mat_eq(e1.mat_mul(Floc, A, B), e1.mat_mul(Floc, B, A))

    chains = [((0, a, 0), (a, 0, b), (0, b, 0)) for a in (1, 2) for b in (1, 2)]
    for name, mem in members:
        okm = True
        for M in chains:
            for t in tcone:
                Ut = S3.U(M, mem, t)
                for O, others in ((X1, (X3, Z3)), (Z1, (X3, Z3)), (X3, (X1, Z1)), (Z3, (X1, Z1))):
                    H = heis(Ut, O)
                    okm &= all(comm(H, P) for P in others)
        out("member %-9s: %d chains x %d times: images of X_1, Z_1 commute with X_3, Z_3 and images of X_3, "
            "Z_3 commute with X_1, Z_1: %s" % (name, len(chains), len(tcone), okm))
        l3 &= okm
    out("[W] for every member of Gamma_all: the coupling layer is a product of commuting gates on sites and "
        "edges, so it maps an operator on site i into the algebra of i's closed neighbourhood; the free "
        "layer is a product of one-site gates; so for t <= 1 the support grows by at most one edge")
    # K-L3 mutation
    g13 = GS.gates[("pair", 1)]
    th13 = g13.diag_theta(g13.principal())

    def extra(y):
        return th13((y[0], y[2]))
    det = True
    for M in chains:
        Ut = S3.U(M, GS.principal_member(), Fraction(1, 2), extra=extra)
        H = heis(Ut, X1)
        det &= not (comm(H, X3) and comm(H, Z3))
    out("K-L3: with a delta_13(1) generator term added to the coupling layer, the image of X_1 at t = 1/2 "
        "fails to commute with X_3 or Z_3 on every chain: %s" % det)
    control("K-L3 long-range mutation detected", det)
    # comparison: F2-1's composite principal-log rule on the chains, t = 1/2
    comp = []
    for M in chains:
        L = leap(M, q)
        o = e1.cmat_order(L, q)
        Fb = e1.field(lcm(72, 2 * o))
        Cb = e1.Carrier(q, 3, Fb)
        rho_J, _, _ = e1.canonical_weil(e1.Carrier(q, 3, e1.field(q)))
        Ub = e1.mat_embed(Fb, e1.rho_leap(e1.Carrier(q, 3, e1.field(q)), rho_J, M), e1.field(q))
        sp = e1.spectral(Fb, Ub, o)
        Uh = e1.zeros(Fb, 27)
        for j, P in sp:
            Uh = e1.mat_add(Fb, Uh, e1.mat_scale(Fb, root(Fb, e1.principal_theta(j, o) / 2), P))
        Hb = e1.mat_mul(Fb, e1.adjoint(Fb, Uh), e1.mat_mul(Fb, Cb.X(0), Uh))
        inside = e1.mat_eq(e1.mat_mul(Fb, Hb, Cb.X(2)), e1.mat_mul(Fb, Cb.X(2), Hb)) and \
            e1.mat_eq(e1.mat_mul(Fb, Hb, Cb.Z(2)), e1.mat_mul(Fb, Cb.Z(2), Hb))
        comp.append((fmtM(M), o, inside))
    out("comparison (not a control): F2-1's composite principal-log rule, t = 1/2, image of X_1 commutes with "
        "X_3 and Z_3: " + " ".join("%s(order %d):%s" % c for c in comp))
    token("L3", "(3,3)", "E1L-CAUSAL" if l3 else "E1L-NOT-CAUSAL")
    R["L3ok"] = l3


# ============================================================================ C-OI at (7,1)


def c_oi_q7(R):
    q, N = 7, 1
    size = "q=7,N=1"
    header("[%s] C-OI  F2-1's C1 battery and C2 checks at a new alphabet, through F2-1's functions" % size)
    Fq = e1.field(q)
    C = e1.Carrier(q, N, Fq)
    d = C.d
    rho_J, s, G = e1.canonical_weil(C)
    Ms = e1.symmetric_couplings(q, N)
    Ls = {M: leap(M, q) for M in Ms}
    ords = {M: e1.cmat_order(Ls[M], q) for M in Ms}
    U = {M: e1.rho_leap(C, rho_J, M) for M in Ms}
    w0 = all(e1.unitary_check(Fq, U[M]) and e1.intertwines(C, U[M], Ls[M]) and
             e1.mat_eq(e1.mat_pow(Fq, U[M], ords[M]), e1.eye(Fq, d)) for M in Ms)
    out("genuineness: every image unitary, U W(z) U^+ = W(L z), U^ord(L) = I: %s; orders %s"
        % (w0, " ".join("%s:%d" % (fmtM(M), ords[M]) for M in Ms)))

    def key(A):
        return tuple(x for r in A for x in r)
    I = e1.eye(Fq, d)
    seen = {key(I)}
    fr = [I]
    while fr:
        nw = []
        for A in fr:
            for g in U.values():
                B = e1.mat_mul(Fq, A, g)
                kk = key(B)
                if kk not in seen:
                    seen.add(kk)
                    nw.append(B)
        fr = nw
    grp_ok = len(seen) == e1.sp_order(1, q)
    out("matrix group generated by the images: order %d; |SL(2,7)| = %d; SL(2,7) is perfect, so the genuine "
        "lift is unique [W]" % (len(seen), e1.sp_order(1, q)))
    dims = {M: len(C.intertwiners(Ls[M])) for M in Ms}
    c1a = all(v == 1 for v in dims.values())
    out("(i) intertwiner dimension per coupling: " + " ".join("%s:%d" % (fmtM(M), dims[M]) for M in Ms))
    sums, rays = [], {}
    c1b = True
    total = 0
    for M in Ms:
        ok, fst, cnts = e1.c1_words(C, U[M], Ls[M], collect=rays, sums=sums)
        c1b &= ok
        total += sum(cnts)
        out("(ii) M=%s alphabet {L_M, tau_1}: words per length 0..6 = %s, total %d, Born = rooted law: %s%s"
            % (fmtM(M), cnts, sum(cnts), ok, "" if ok else " first counterexample %s" % (fst,)))
    out("    words over all couplings: %d (x %d registered starts)" % (total, d))
    Cs = e1.Carrier(q, N + 1, Fq)
    c1c = True
    tt_sums = []
    post_meter = []
    for M in Ms:
        for x0 in C.pts:
            Jc, Jq, post, _ = e1.two_time(Cs, U[M], Ls[M], 0, x0)
            keys = set(Jc) | set(Jq)
            c1c &= all(Jq.get(kk, Fq.zero) == Fq.frac(Jc.get(kk, 0)) for kk in sorted(keys))
            tot = Fq.zero
            for kk in sorted(Jq):
                tot = Fq.add(tot, Jq[kk])
            tt_sums.append(tot == Fq.one)
            post_meter.extend(post)
    out("(iii) two-time law with the symplectic meter equals the classical law for every M and x0: %s (%d "
        "protocols)" % (c1c, len(Ms) * d))
    s_ok = all(sums) and all(tt_sums)
    ba = True
    nchk = 0
    for key_, v in sorted(rays.items()):
        for xval in range(q):
            proj = [v[i] if C.pts[i][0] == xval else Fq.zero for i in range(d)]
            if all(Fq.is_zero(x) for x in proj):
                continue
            W = e1.wigner(C, proj)
            marg = {}
            for z, w in W.items():
                marg[z[1]] = Fq.add(marg.get(z[1], Fq.zero), w)
            ba &= all(marg[t] == Fq.frac(Fraction(1, q)) for t in range(q))
            nchk += 1
    bm = True
    for rec, proj in post_meter:
        W = e1.wigner(Cs, proj)
        marg = {}
        for z, w in W.items():
            marg[z[3]] = Fq.add(marg.get(z[3], Fq.zero), w)
        bm &= all(marg[t] == Fq.frac(Fraction(1, q)) for t in range(q))
    out("C2: probabilities sum to 1 on %d of %d word states and %d of %d two-time laws; previous-component "
        "Wigner marginal = 1/7 after registration on %d post-registration states (%d rays): %s; meter: %d, %s"
        % (sum(sums), len(sums), sum(tt_sums), len(tt_sums), nchk, len(rays), ba, len(post_meter), bm))
    ok = w0 and grp_ok and c1a and c1b and c1c and s_ok and ba and bm
    # C4(a) at (7,1): u maps |e1><e1| to a matrix with an entry that is not a nonnegative real
    u = U[((0,),)]
    e_ = 1
    entries = [Fq.mul(u[i][e_], Fq.conj(u[j][e_])) for i in range(d) for j in range(d)]
    bad = [x for x in entries if not Fq.is_real(x) or e1.real_sign(Fq, x) < 0]
    out("C4(a) at (7,1): u |e_1><e_1| u^+ has %d of %d entries that are not nonnegative reals" % (len(bad), d * d))
    R["C4a7"] = bool(bad)
    R["COI7"] = ok
    token("C-OI", size, "E1L-CONSISTENT" if ok else "E1L-INCONSISTENT")


# ============================================================================ control cells


def certificate(F, g):
    """True iff |tr g|^2 is not an algebraic integer (then g has infinite order modulo scalars)."""
    t = F.zero
    for i in range(len(g)):
        t = F.add(t, g[i][i])
    m = F.mul(t, F.conj(t))
    return not F.is_alg_integer(m)


def control_size(q, N, R):
    size = "q=%d,N=%d" % (q, N)
    res = R.setdefault(size, {})
    Fc = e1.field(8 * q)
    GS = GateSet(q, Fc)
    S = Sites(GS, N)
    C = S.C
    d = S.d
    n2 = 2 * N
    full = d * d - 1
    P0 = GS.principal_member()
    Fq = e1.field(q)
    Cq = e1.Carrier(q, N, Fq)
    rho_J, _, _ = e1.canonical_weil(Cq)

    header("[%s] gates and their spectra" % size)
    for k, g in GS.gates.items():
        out("gate %-12s eigenvalue keys %s multiplicities %s principal theta %s nondegenerate %s"
            % (str(k), g.keys, [str(g.mult[kk]) for kk in g.keys], [str(g.theta0[kk]) for kk in g.keys],
               g.nondegenerate()))
    sqrtS = [Smat for Smat in e1.group_closure([leap(((m,),), q) for m in range(q)], q)
             if e1.cmat_mul(Smat, Smat, q) == leap(((0,),), q)]
    out("one-site: S in SL(2,%d) with S^2 = J': %d -> every square root of u is %s"
        % (q, len(sqrtS), "non-Clifford (Gamma_all) [W]" if not sqrtS else "not necessarily non-Clifford"))
    res["no_clifford_root"] = not sqrtS

    zlist = [z for z in itertools.product(range(q), repeat=n2) if any(z)]
    wcols = {z: weyl_cols(C, z) for z in zlist}

    for rep in ("self", "cf"):
        Ms = symmetric(q, N, rep == "cf")
        Mnz = [M for M in Ms if any(x for r in M for x in r)]
        tag = "R_" + rep
        header("[%s] %s: integer-time group" % (size, tag))
        Lg = [leap(M, q) for M in Ms]
        Sgrp = e1.group_closure(Lg, q)
        orbs, where = orbits(Lg, q, n2)
        span = [tuple(e1.cmat_vec(g, tuple(int(i == k) for i in range(N)) + (0,) * N, q))
                for g in Sgrp for k in range(N)]
        weyl_all = rank_mod(span, q) == n2
        out("symplectic part generated: order %d (|Sp(%d,%d)| = %d); orbits on nonzero vectors: %d, sizes %s"
            % (len(Sgrp), n2, q, e1.sp_order(N, q), len(orbs), sorted(len(o) for o in orbs)))
        out("translation orbit spans F_q^%d (every Weyl operator in the group modulo phases): %s" % (n2, weyl_all))
        clifford = len(Sgrp) == e1.sp_order(N, q) and weyl_all
        out("integer-time group modulo phases: order %d%s [W: Schur, as F2-1 (c1)]"
            % (q ** n2 * len(Sgrp), " = the full Clifford group" if clifford else ""))
        res[rep + "_clifford"] = clifford
        res[rep + "_orbits"] = len(orbs)

        # ---------------------------------------------------------------- C3(a) all durations
        header("[%s] %s C3(a)  all durations: Lie algebra of the layer and translation generators" % (size, tag))
        gens = [S.gen_free(P0)] + [S.gen_coup(M, P0) for M in Mnz] + [S.gen_X(P0, k) for k in range(N)]
        dim = e1.lie_closure_dim(Fc, [[G] for G in gens], stop_at=d * d) - 1
        out("principal member: %d generators (free layer, %d coupling layers, %d translations); dimension modulo "
            "the identity %d (full = %d)" % (len(gens), len(Mnz), N, dim, full))
        gens_nt = gens[:1 + len(Mnz)]
        dim_nt = e1.lie_closure_dim(Fc, [[G] for G in gens_nt], stop_at=d * d) - 1
        out("K-Lie: translations removed: dimension modulo the identity %d" % dim_nt)
        control("K-Lie dropped translations %s %s" % (tag, size), dim_nt < full)
        res[rep + "_dim"] = dim
        if rep == "self":
            trans = len(orbs) == 1
            out("Sp(%d,%d) transitive on nonzero vectors: %s -> the Clifford adjoint action on sl(%d) is irreducible "
                "[W]" % (n2, q, trans, d))
            robust = clifford and trans and dim == full
            out("[W] robustness over Gamma_all: for any generator choice the algebra contains a non-scalar element "
                "and is invariant under the Clifford adjoint action, hence contains su(%d): %s" % (d, robust))
            token("C3(a-self)", size, ("E1L-SELF-FULL [principal X; Gamma_all W]" if robust else
                                       ("E1L-SELF-FULL [principal X]" if dim == full else "E1L-SELF-NOT-FULL")))
            res["self_full"] = dim == full
            res["self_full_scope"] = "Gamma_all" if robust else "principal"
        else:
            out("touching analysis over the orbits of the integer-time group (precondition: every Weyl operator "
                "present: %s)" % weyl_all)
            types = [("free", S.lin_free())] + [("coup" + fmtM(M), S.lin_coup(M)) for M in Mnz] + \
                    [("X_%d" % (k + 1), S.lin_X(k)) for k in range(N)]
            gate_of = {}
            for g in GS.gates.values():
                for kk in g.keys:
                    gate_of[(g.name, kk)] = g
            # parameters: every (gate, key) except each gate's first key (the common shift is the identity)
            allkeys = sorted({key for _, lin in types for key, _ in lin}, key=str)
            params = [kk for kk in allkeys if kk[1] != gate_of[kk].keys[0]]
            comp = {}
            for nm, lin in types:
                comp[nm] = components(C, [A for _, A in lin], zlist, wcols)

            def system(names, orb):
                A, b = [], []
                for nm, lin in types:
                    if nm not in names:
                        continue
                    for z in orb:
                        cz = comp[nm][z]
                        D = Fc.deg
                        for bb in range(D):
                            row = [Fraction(0)] * len(params)
                            rhs = Fraction(0)
                            for (key, _), val in zip(lin, cz):
                                cv = coords(Fc, val)[bb]
                                if cv == 0:
                                    continue
                                g = gate_of[key]
                                rhs -= g.theta0[key[1]] * cv
                                if key in params:
                                    row[params.index(key)] += cv
                            if any(row) or rhs:
                                A.append(row)
                                b.append(rhs)
                return A, b
            all_names = [nm for nm, _ in types]
            per_orbit = []
            for oi, orb in enumerate(orbs):
                robust_types = []
                for nm, lin in types:
                    A, b = system([nm], orb)
                    feas = int_solve(A, b) if A else ([0] * len(params), [[int(i == j) for i in range(len(params))]
                                                                         for j in range(len(params))])
                    if feas is None:
                        nondeg = all(gate_of[key].nondegenerate() for key, _ in lin)
                        robust_types.append((nm, nondeg))
                joint = None
                if not robust_types:
                    A, b = system(all_names, orb)
                    joint = int_solve(A, b) if A else ([0] * len(params), [])
                per_orbit.append((oi, len(orb), robust_types, joint))
                out("  orbit %d (size %d): touched for every Gamma_spec member by %s%s"
                    % (oi, len(orb), [nm + ("[Gamma_all]" if nd else "") for nm, nd in robust_types] or "no single type",
                       "" if robust_types else ("; joint system: %s" % ("no lattice point (touched for every "
                                                                          "member)" if joint is None else
                                                                          "lattice points exist"))))
            all_robust_all = all(any(nd for _, nd in rt) for _, _, rt, _ in per_orbit)
            all_robust_spec = all(rt or jt is None for _, _, rt, jt in per_orbit)
            # principal touching consistency (K-touch)
            touched_principal = True
            for orb in orbs:
                hit = False
                for nm, lin in types:
                    for z in orb:
                        s = Fc.zero
                        for (key, _), val in zip(lin, comp[nm][z]):
                            s = Fc.add(s, Fc.mul(Fc.frac(gate_of[key].theta0[key[1]]), val))
                        if not Fc.is_zero(s):
                            hit = True
                            break
                    if hit:
                        break
                touched_principal &= hit
            control("K-touch principal touching implies full %s" % size, (not touched_principal) or dim == full)
            failing = []
            if not all_robust_spec:
                pts = []
                for oi, ln, rt, jt in per_orbit:
                    if not rt and jt is not None:
                        pts.extend(lattice_points(jt))
                pts = sorted(set(pts), key=lambda v: (max([abs(x) for x in v] + [0]), v))[:8]
                for pnt in pts:
                    mem = {k: list(g.principal()) for k, g in GS.gates.items()}
                    for kk, v in zip(params, pnt):
                        g = gate_of[kk]
                        mem[g.name][g.keys.index(kk[1])] = v
                    mem = {k: tuple(v) for k, v in mem.items()}
                    gm = [S.gen_free(mem)] + [S.gen_coup(M, mem) for M in Mnz] + [S.gen_X(mem, k) for k in range(N)]
                    dm = e1.lie_closure_dim(Fc, [[G] for G in gm], stop_at=d * d) - 1
                    failing.append((pnt, dm))
                    out("  member with lifts %s on %s: dimension modulo the identity %d" % (pnt, [str(p) for p in params], dm))
            scope = "Gamma_all" if all_robust_all else ("Gamma_spec" if all_robust_spec else "principal")
            notfull = [p for p, dm in failing if dm < full]
            if dim == full and not notfull:
                tok = "E1L-CF-FULL [%s%s]" % (scope, "" if all_robust_spec else "; plus %d listed members" % len(failing))
            else:
                tok = "E1L-CF-NOT-FULL [principal %s; deficient members %s]" % (dim, notfull)
            token("C3(a-cf)", size, tok)
            res["cf_full"] = dim == full and not notfull
            res["cf_full_scope"] = scope

        # ---------------------------------------------------------------- C3(b) one duration
        header("[%s] %s C3(b)  one duration: integer-time images and the half-layer gates" % (size, tag))
        words = [("X_1", C.X(0)), ("Z_1", C.Z(0)), ("X_1Z_1", e1.mat_mul(Fc, C.X(0), C.Z(0)))]
        for M in Ms:
            words.append(("L" + fmtM(M), e1.mat_embed(Fc, e1.rho_leap(Cq, rho_J, M), Fq)))
        # K-D2: no certificate for integer-time elements
        U0c = words[3][1]
        k_d2 = not any(certificate(Fc, w) or certificate(Fc, e1.mat_mul(Fc, U0c, w)) for _, w in words)
        control("K-D2 no certificate on integer-time words %s %s" % (tag, size), k_d2)
        # gate types relevant to the repertoire and their sign patterns (lifts in {0,1}, first fixed)
        gtypes = ["u"]
        for M in Mnz:
            for i in range(N):
                if M[i][i]:
                    gtypes.append(("site", M[i][i]))
            for i in range(N):
                for j in range(i + 1, N):
                    if M[i][j]:
                        gtypes.append(("pair", M[i][j]))
        gtypes = sorted(set(gtypes), key=str)
        pats = {}
        for gt in gtypes:
            g = GS.gates[gt]
            pats[gt] = [(0,) + p for p in itertools.product((0, 1), repeat=len(g.keys) - 1)]
        nmem = 1
        for gt in gtypes:
            nmem *= len(pats[gt])
        out("gate types %s; sign patterns per type %s; members of Gamma_spec (one-duration): %d"
            % ([str(g) for g in gtypes], [len(pats[g]) for g in gtypes], nmem))

        def half_single(gt, pat):
            mem = dict(P0)
            mem[gt] = pat
            if gt == "u":
                return S.free_flow(mem, Fraction(1, 2))
            if gt[0] == "site":
                M = tuple(tuple(gt[1] if (i == j == 0) else 0 for j in range(N)) for i in range(N))
            else:
                M = tuple(tuple(gt[1] if {i, j} == {0, 1} else 0 for j in range(N)) for i in range(N))
            return S.coup_flow(M, mem, Fraction(1, 2))
        cert = {}
        for gt in gtypes:
            for pat in pats[gt]:
                h = half_single(gt, pat)
                first = None
                for wn, w in words:
                    if certificate(Fc, e1.mat_mul(Fc, h, w)):
                        first = wn
                        break
                cert[(gt, pat)] = first
        free_cert = [cert[("u", p)] for p in pats["u"]]
        out("D2 certificates of the free half-layer per sign pattern (first certified word): %s" % free_cert)
        # non-Clifford of the free half per pattern, and C4(b)
        nc = []
        neg = []
        for p in pats["u"]:
            mem = dict(P0)
            mem["u"] = p
            v = S.free_flow(mem, Fraction(1, 2))
            nc.append(bool(e1.normalizer_failures(C, v)))
            W = e1.wigner(C, e1.mat_vec(Fc, v, C.basis_vec((0,) * N)))
            neg.append(any(e1.real_sign(Fc, x) < 0 for x in W.values()))
        out("free half-layer non-Clifford per sign pattern: %s; Wigner of (free half)|0...0> negative: %s" % (nc, neg))
        res[rep + "_free_nc"] = nc
        res[rep + "_C4b"] = neg
        dense_members = 0
        undecided = []
        if rep == "self":
            d1 = res["self_clifford"] and res["self_orbits"] == 1
            control("K-D1 Clifford integer-time group irreducible %s" % size, d1)
            unc_pats = {gt: [p for p in pats[gt] if not cert[(gt, p)]] for gt in gtypes}
            n_unc = 1
            for gt in gtypes:
                n_unc *= len(unc_pats[gt])
            dense_members = nmem - n_unc
            out("single-gate half-layers: members with no certified single-gate half: %d" % n_unc)
            uncert = []
            if N >= 2 and n_unc:
                uncert = [dict(zip(gtypes, combo)) for combo in itertools.product(*[unc_pats[gt] for gt in gtypes])]
            elif n_unc:
                undecided = [None] * n_unc     # at N = 1 every coupling's half-layer is a single-gate half
            # members not certified by single-gate halves: try every coupling's half-layer
            for memp in uncert:
                mem = dict(P0)
                mem.update(memp)
                got = None
                for M in Mnz:
                    h = S.coup_flow(M, mem, Fraction(1, 2))
                    for wn, w in words:
                        if certificate(Fc, e1.mat_mul(Fc, h, w)):
                            got = (fmtM(M), wn)
                            break
                    if got:
                        break
                if got:
                    dense_members += 1
                else:
                    undecided.append(memp)
            out("D1 holds for every member (the integer-time group is the full Clifford group, irreducible): %s" % d1)
            out("D2 certified for %d of %d members; %d without a certificate on the preregistered words"
                % (dense_members, nmem, len(undecided)))
            lit = res["self_clifford"] and (res["no_clifford_root"] or all(nc))
            out("[L] route (Campbell-Anwar-Browne App. D, owner's reading): Clifford group generated %s; free half "
                "non-Clifford for every Gamma_spec member %s%s" % (res["self_clifford"], all(nc),
                                                                  "; for every Gamma_all member (no S^2 = J')" if
                                                                  res["no_clifford_root"] else ""))
            summ = "ALL" if (d1 and dense_members == nmem) else ("SOME" if dense_members else "NONE")
            token("C3(b-self)", size, "%s [D1,D2 over Gamma_spec: %s (%d/%d); L route: %s]"
                  % ("E1L-SELF-DENSE" if summ == "ALL" else "E1L-SELF-NOT-DENSE", summ, dense_members, nmem,
                     "Gamma_all" if (lit and res["no_clifford_root"]) else ("Gamma_spec" if lit else "no")))
            res["self_dense"] = summ == "ALL"
        else:
            # D1 via the touching closure; relations per (gate, pattern)
            rels = {}
            for gt in gtypes:
                for pat in pats[gt]:
                    rels[(gt, pat)] = adjoint_relation(C, half_single(gt, pat), zlist, wcols)
            nob = len(orbs)

            def components_with(hs):
                parent = list(range(nob))

                def fp(a):
                    while parent[a] != a:
                        parent[a] = parent[parent[a]]
                        a = parent[a]
                    return a
                for h in hs:
                    for z, tos in adjoint_relation(C, h, zlist, wcols).items():
                        for z2 in tos:
                            ra, rb = fp(where[z]), fp(where[z2])
                            if ra != rb:
                                parent[ra] = rb
                return len({fp(i) for i in range(nob)})
            # K-D1 (negative): the integer-time generators of R_cf merge no orbit
            it_cf = [e1.mat_embed(Fc, e1.rho_leap(Cq, rho_J, M), Fq) for M in Ms] + [C.X(k) for k in range(N)]
            neg_c = components_with(it_cf)
            out("K-D1 negative: touching closure over R_cf's orbits with R_cf's own integer-time generators: %d "
                "blocks (orbits %d)" % (neg_c, nob))
            control("K-D1 integer-time generators merge no orbit %s" % size, neg_c == nob)
            # K-D1 (positive): adding one self-coupling leap must merge exactly as the classical orbits of the
            # enlarged group predict
            Mx = tuple(tuple(1 if (i == j == 0) else 0 for j in range(N)) for i in range(N))
            orbs_x, _ = orbits(Lg + [leap(Mx, q)], q, n2)
            pos_c = components_with([e1.mat_embed(Fc, e1.rho_leap(Cq, rho_J, Mx), Fq)])
            out("K-D1 positive: adding the leap of %s: %d blocks; classical orbits of the enlarged group: %d"
                % (fmtM(Mx), pos_c, len(orbs_x)))
            control("K-D1 touching closure reproduces classical orbit merging %s" % size, pos_c == len(orbs_x))
            irr = 0
            certd = 0
            both = 0
            fails = []
            for combo in itertools.product(*[pats[gt] for gt in gtypes]):
                memp = dict(zip(gtypes, combo))
                parent = list(range(nob))

                def findp(a):
                    while parent[a] != a:
                        parent[a] = parent[parent[a]]
                        a = parent[a]
                    return a
                for gt in gtypes:
                    for z, tos in rels[(gt, memp[gt])].items():
                        for z2 in tos:
                            ra, rb = findp(where[z]), findp(where[z2])
                            if ra != rb:
                                parent[ra] = rb
                comps = len({findp(i) for i in range(nob)})
                i_ok = comps == 1
                c_ok = any(cert[(gt, memp[gt])] for gt in gtypes)
                irr += i_ok
                certd += c_ok
                both += i_ok and c_ok
                if not i_ok:
                    fails.append((memp, comps))
            out("members: %d; D1 irreducible: %d; D2 certified: %d; both (dense): %d" % (nmem, irr, certd, both))
            for memp, comps in fails[:8]:
                out("  D1 fails: %s -> %d invariant blocks" % ({str(k): v for k, v in memp.items()}, comps))
            summ = "ALL" if both == nmem else ("SOME" if both else "NONE")
            token("C3(b-cf)", size, "%s [Gamma_spec members: %s (%d/%d)]"
                  % ("E1L-CF-DENSE" if summ == "ALL" else "E1L-CF-NOT-DENSE", summ, both, nmem))
            res["cf_dense"] = summ
            if fails:
                fraction_cells(q, N, GS, S, fails, orbs, where, zlist, res)
        res[rep + "_members"] = nmem

    # ---------------------------------------------------------------- C4(b) over Gamma_all
    header("[%s] C4  escape from the known obstructions" % size)
    if N == 1:
        u = GS.u_mat
        spec = e1.spectral(Fc, u, 4)
        dims = [rs.trace_frac(Fc, P) for _, P in spec]
        sq = {j: Fc.root(8, j) for j, _ in spec}
        Ugens = [e1.mat_embed(Fc, e1.rho_leap(Cq, rho_J, M), Fq) for M in e1.symmetric_couplings(q, N)]
        Ugens += [C.X(0), C.Z(0)]
        rays = rs.stabilizer_rays(C, Ugens)
        v0 = C.basis_vec((0,))
        reach = [p for p in rays if rs.reachable_by_root(Fc, spec, dims, sq, v0, p, False)]
        out("(b) Gamma_all: stabilizer rays %d; reachable as v|0> for some square root v of u: %d" % (len(rays), len(reach)))
        res["C4b_all"] = not reach
    else:
        out("(b) Gamma_all at N = 2: the free half-layer is v (x) v with v a square root of u; v|0> is Wigner-negative "
            "for every square root at q = 3 (correction 1), so the product state is negative at (z0, z1) with "
            "W(z0) < 0 < W(z1) [W]")
        res["C4b_all"] = True
    out("(a) u preserves no nonnegativity: F2-1 C4(a) at q = 3, 5; at q = 7 see C-OI")
    out("(c) one-duration generating sets are finite (integer-time images, translations and the half-layer gates of "
        "the selectable couplings), so their groups are countable [W]; the all-duration repertoires are continua")


def fraction_cells(q, N, GS, S, fails, orbs, where, zlist, res):
    """A3-style separated failure cells: layer fractions 1/3 and 1/4 for members failing D1."""
    for frac in (Fraction(1, 3), Fraction(1, 4)):
        Ff = e1.field(lcm(8 * q, 4 * frac.denominator, q * frac.denominator))
        GSf = GateSet(q, Ff)
        Sf = Sites(GSf, N)
        Cf = Sf.C
        wc = {z: weyl_cols(Cf, z) for z in zlist}
        nob = len(orbs)
        okc = 0
        for memp, _ in fails:
            mem = GSf.principal_member()
            mem.update(memp)
            gates = [Sf.free_flow(mem, frac)]
            for M in symmetric(q, N, True):
                if any(x for r in M for x in r):
                    gates.append(Sf.coup_flow(M, mem, frac))
            parent = list(range(nob))

            def findp(a):
                while parent[a] != a:
                    parent[a] = parent[parent[a]]
                    a = parent[a]
                return a
            for h in gates:
                rel = adjoint_relation(Cf, h, zlist, wc)
                for z, tos in rel.items():
                    for z2 in tos:
                        ra, rb = findp(where[z]), findp(where[z2])
                        if ra != rb:
                            parent[ra] = rb
            comps = len({findp(i) for i in range(nob)})
            okc += comps == 1
        out("  separated cell, layer fraction %s, lifts of the failing sign patterns: D1 irreducible for %d of %d"
            % (frac, okc, len(fails)))
        res.setdefault("fraction_cells", []).append((str(frac), okc, len(fails)))


# ============================================================================ driver


def main():
    out("F2-2 exact run: RULES.md (f2-2-local-continuity) committed before this script")
    out("Labels: [X] exact (all lines unless tagged), [W] written argument, [L] literature, [K] kernel theorem cited.")
    h1 = sha256(E1_PATH)
    h2 = sha256(RS_PATH)
    out("imported F2-1 module sha256 %s; correction-1 module sha256 %s" % (h1, h2))
    control("K0 F2-1 module unchanged", h1 == E1_SHA)
    control("K0 exactness self-tests", e1.self_tests())
    out("K-mod p: no reduction modulo a prime is used in this run; every decisive line is exact over Q(zeta_n)")
    R = {}
    e1.run_K1(R)
    control("K1 q = 2 layer images contradict the visible law (limitation)", R["K1"])
    locality_cells(R)
    c_oi_q7(R)
    sizes = [(3, 1), (5, 1), (7, 1), (3, 2)]
    for q, N in sizes:
        control_size(q, N, R)
    verdict(R, sizes)


def verdict(R, sizes):
    header("Summary and verdict")
    for name, ok in CTRL:
        out("control %-50s %s" % (name, "PASS" if ok else "FAIL"))
    for cell, size, tok in TOK:
        out("token %-12s %-14s %s" % (cell, size, tok))
    if not all(ok for _, ok in CTRL):
        out("VERDICT VOID")
        return
    loc = R["L0ok"] and R["L1ok"] and R["L3ok"]
    cons = R["L0ok"] and R["COI7"]
    if not (R["L1ok"] and R["L3ok"]):
        out("VERDICT E1L-NONLOCAL")
        return
    if not cons:
        out("VERDICT E1L-INCONSISTENT")
        return
    selfc = all(R["q=%d,N=%d" % s]["self_full"] and R["q=%d,N=%d" % s]["self_dense"] for s in sizes)
    for q, N in sizes:
        r = R["q=%d,N=%d" % (q, N)]
        out("q=%d,N=%d: R_self all-duration full %s [%s], one-duration dense %s | R_cf all-duration full %s [%s], "
            "one-duration %s" % (q, N, r["self_full"], r["self_full_scope"], r["self_dense"], r["cf_full"],
                                 r["cf_full_scope"], r["cf_dense"]))
    out("outcome rule: L0, L1, L3 and C-OI hold%s" %
        ("; E1L-SELF-FULL and E1L-SELF-DENSE at every control size" if selfc else ""))
    out("VERDICT " + ("E1L-LOCAL-AND-SELF-CONTROLLING" if (loc and selfc) else "E1L-LOCAL-CONSISTENT"))


if __name__ == "__main__":
    main()
