"""F2-4: control of E1-L across generator choices and sizes. The exact runs fixed by RULES.md.

Imports ../f2-2-local-continuity/f2_2_exact.py (which imports the frozen F2-1 module) by path and
prints the sha256 of both. Every decisive line is exact over Q(zeta_{8q}) or over the integers, except
AD-X's modular Lie dimension, which is a lower bound [W] tied to an exact value by K-indep (ii).
numpy is used only for that modular computation (int64, every intermediate below 2^61).
"""
import hashlib
import importlib.util
import itertools
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
F22_PATH = os.path.join(HERE, "..", "f2-2-local-continuity", "f2_2_exact.py")
E1_PATH = os.path.join(HERE, "..", "f2-1-e1-consistency", "e1_exact.py")
E1_SHA = "e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6"
F22_SHA = "246adb2bc6590a3d84234f6937409f2042bba796d646eae633f6383a62a90e57"


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


f22 = _load("f2_2_exact", F22_PATH)
e1 = f22.e1
out = e1.out
header = e1.header
CTRL = []
TOK = {}
FR = Fraction


def control(name, ok):
    CTRL.append((name, bool(ok)))
    out("CONTROL %-66s %s" % (name, "PASS" if ok else "FAIL"))
    return bool(ok)


def token(name, val):
    TOK[name] = val
    out("TOKEN   %-30s %s" % (name, val))


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def f(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    def u(self, a, b):
        a, b = self.f(a), self.f(b)
        if a != b:
            self.p[a] = b

    def count(self):
        return len({self.f(i) for i in range(len(self.p))})


def free_patterns(GS):
    g = GS.gates["u"]
    return [(0,) + p for p in itertools.product((0, 1), repeat=len(g.keys) - 1)]


def with_u(GS, pat):
    mem = dict(GS.principal_member())
    mem["u"] = pat
    return mem


# ============================================================================ modular Lie dimension


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_factors(n):
    fs, k = [], 2
    while k * k <= n:
        if n % k == 0:
            fs.append(k)
            while n % k == 0:
                n //= k
        k += 1
    if n > 1:
        fs.append(n)
    return fs


def modulus_for(n):
    p = (1 << 25) - 1
    p -= (p - 1) % n
    while not is_prime(p):
        p -= n
    for a in range(2, p):
        g = pow(a, (p - 1) // n, p)
        if all(pow(g, n // r, p) != 1 for r in prime_factors(n)):
            return p, g
    raise RuntimeError("no primitive root")


def reducer(F, p, g):
    pw = [pow(g, k, p) for k in range(F.deg)]

    def red(a):
        c, d = a
        s = 0
        for ck, gk in zip(c, pw):
            if ck:
                s += ck * gk
        return s * pow(d, p - 2, p) % p
    return red


def to_mod(F, A, red):
    return np.array([[red(x) for x in row] for row in A], dtype=np.int64)


def lie_dim_mod(gens, p):
    """Dimension of the span of left-nested brackets of gens and I, reduced mod p (a lower bound)."""
    d = gens[0].shape[0]
    D = d * d
    B = np.zeros((0, D), dtype=np.int64)
    piv = []
    gl = list(gens) + [np.eye(d, dtype=np.int64)]
    queue = [("g", X) for X in gl]
    qi = 0
    while qi < len(queue) and len(piv) < D:
        kind, item = queue[qi]
        qi += 1
        X = item if kind == "g" else (item[0] @ item[1] - item[1] @ item[0]) % p
        v = X.reshape(D) % p
        if piv:
            c = v[piv]
            v = (v - (c @ B) % p) % p
        nz = np.nonzero(v)[0]
        if len(nz) == 0:
            continue
        j = int(nz[0])
        v = v * pow(int(v[j]), p - 2, p) % p
        if B.shape[0]:
            col = B[:, j].copy()
            B = (B - np.outer(col, v) % p) % p
        B = np.vstack([B, v])
        piv.append(j)
        for gg in gens:
            queue.append(("b", (gg, X)))
    return len(piv)


# ============================================================================ AD-X


def coupling_gen(S, M, mode, member):
    """The coupling-layer generator of M (R_cf: pair terms only), with the stated lift mode."""
    F, q, N = S.F, S.q, S.N
    if mode == "spec":
        return S.gen_coup(M, member)
    D = e1.zeros(F, S.d)
    for idx, y in enumerate(S.pts):
        t = FR(0)
        for i in range(N):
            for j in range(i + 1, N):
                m = M[i][j] % q
                if not m:
                    continue
                if mode == "bilinear":
                    t += FR(-m * y[i] * y[j], q)
                elif mode == "lifted":
                    expo = (-m * y[i] * y[j]) % q
                    t += S.GS.gates[("pair", m)].theta0[expo] + ((3 * y[i] + 5 * y[j] + m) % 3) - 1
                elif mode == "local":
                    t += FR(y[i] + y[j], q)
        D[idx][idx] = F.frac(t)
    return D


def ad_gens(S, rep, mode, member, translations=True):
    Ms = [M for M in f22.symmetric(S.q, S.N, rep == "cf") if any(x for r in M for x in r)]
    gens = [S.gen_free(member)] + [coupling_gen(S, M, mode, member) for M in Ms]
    if translations:
        gens += [S.gen_X(member, k) for k in range(S.N)]
    return gens


def ad_cells():
    header("AD-X  all-duration algebra: modular lower bound on the dimension modulo the identity")
    res = {}
    for q, N in ((3, 2), (3, 3), (5, 2)):
        F = e1.field(8 * q)
        GS = f22.GateSet(q, F)
        S = f22.Sites(GS, N)
        d = S.d
        full = d * d - 1
        p, g = modulus_for(F.n)
        red = reducer(F, p, g)
        out("(q,N)=(%d,%d): p = %d (p = 1 mod %d), zeta_%d -> %d; full = %d" % (q, N, p, F.n, F.n, g, full))
        P0 = GS.principal_member()
        pats = free_patterns(GS)
        m2 = dict(P0)
        m2["u"] = pats[-1]
        m2["X"] = tuple(k % 2 for k in GS.gates["X"].keys)
        members = (("M0 principal", "spec", P0), ("M1 bilinear", "bilinear", P0), ("M2 lifted", "lifted", m2))
        dims = {}
        for nm, mode, mem in members:
            gens = [to_mod(F, G, red) for G in ad_gens(S, "cf", mode, mem)]
            dims[nm] = lie_dim_mod(gens, p) - 1
            out("  R_cf %-14s dimension >= %d" % (nm, dims[nm]))
        res[(q, N)] = all(v == full for v in dims.values())
        token("F24-AD-FULL(%d,%d)" % (q, N), "yes" if res[(q, N)] else "no " + str(dims))
        if (q, N) in ((3, 2), (3, 3)):
            nox = lie_dim_mod([to_mod(F, G, red) for G in ad_gens(S, "cf", "spec", P0, translations=False)], p) - 1
            loc = lie_dim_mod([to_mod(F, G, red) for G in ad_gens(S, "cf", "local", P0)], p) - 1
            out("  K-AD-mut: translations removed >= %d; local pair generators >= %d" % (nox, loc))
            # a modular value is a lower bound; the mutations must fall short exactly, which K-indep ties down at (3,2)
            control("K-AD-mut both mutations below full at (%d,%d)" % (q, N), nox < full and loc < full)
            res[("mut", q, N)] = (nox, loc)
        if (q, N) == (3, 2):
            selfd = lie_dim_mod([to_mod(F, G, red) for G in ad_gens(S, "self", "spec", P0)], p) - 1
            selfnox = lie_dim_mod([to_mod(F, G, red) for G in ad_gens(S, "self", "spec", P0, translations=False)], p) - 1
            out("  R_self principal >= %d (positive control); R_self without translations >= %d" % (selfd, selfnox))
            control("K-frozen (3,2): principal 80 (R_cf, R_self); without translations 22 (R_cf), 40 (R_self)",
                    dims["M0 principal"] == 80 and selfd == 80 and nox == 22 and selfnox == 40)
            # K-indep (ii): exact closure over Q(zeta_24) for M1, M2 and the two mutations
            ex = {}
            for nm, mode, mem, tr in (("M1", "bilinear", P0, True), ("M2", "lifted", m2, True),
                                      ("noX", "spec", P0, False), ("local", "local", P0, True)):
                gens = ad_gens(S, "cf", mode, mem, translations=tr)
                ex[nm] = e1.lie_closure_dim(F, [[G] for G in gens], stop_at=d * d) - 1
            out("  K-indep (ii) exact dimensions: %s" % ex)
            control("K-indep (ii) modular dimension equals the exact one at (3,2)",
                    ex["M1"] == dims["M1 bilinear"] and ex["M2"] == dims["M2 lifted"]
                    and ex["noX"] == nox and ex["local"] == loc)
    return res


# ============================================================================ OD-1, OD-2, OD-3


def one_relation(C, g, zlist, wcols):
    """z -> set of z' with a nonzero W(z')-coefficient in g W(z) g^dagger (g alone; amendment 1)."""
    F = C.F
    gd = e1.adjoint(F, g)
    rel = {}
    for z in zlist:
        gW = [[F.zero] * C.d for _ in range(C.d)]
        for col, (t, e) in enumerate(wcols[z]):
            c = C.om[e]
            for r_ in range(C.d):
                a = g[r_][t]
                if not F.is_zero(a):
                    gW[r_][col] = F.mul(c, a)
        rel[z] = f22.coeff_nonzero_set(C, e1.mat_mul(F, gW, gd), zlist, wcols)
    return rel


def both(Rg, Rgd):
    return {z: Rg[z] | Rgd[z] for z in Rg}


def two_site_components(orbs, where, dirs, full):
    """Components of N = 2 lines: orbits joined by the links of g (x) g for each one-site relation in dirs.
    full=False uses the sound subset (each line to w2 = min, and to w1 = min), per direction."""
    uf = UF(len(orbs))
    for z in where:
        v1, v2 = (z[0], z[2]), (z[1], z[3])
        for R in dirs:
            R1 = R[v1] if any(v1) else {(0, 0)}
            R2 = R[v2] if any(v2) else {(0, 0)}
            if full:
                for w1 in R1:
                    for w2 in R2:
                        uf.u(where[z], where[(w1[0], w2[0], w1[1], w2[1])])
            else:
                m1, m2 = min(R1), min(R2)
                for w1 in R1:
                    uf.u(where[z], where[(w1[0], m2[0], w1[1], m2[1])])
                for w2 in R2:
                    uf.u(where[z], where[(m1[0], w2[0], m1[1], w2[1])])
    return uf.count()


def od_cells():
    res = {}
    header("OD-1  one site: D1 under R_cf (orbits + free half-layer), D2 certificates, D1 under R_self")
    for q in (3, 5, 7, 11, 13):
        F = e1.field(8 * q)
        GS = f22.GateSet(q, F)
        S1 = f22.Sites(GS, 1)
        C = S1.C
        zl = [z for z in itertools.product(range(q), repeat=2) if any(z)]
        wc = {z: f22.weyl_cols(C, z) for z in zl}
        Lg = [f22.leap(M, q) for M in f22.symmetric(q, 1, True)]
        orbs, where = f22.orbits(Lg, q, 2)
        Lself = [f22.leap(M, q) for M in f22.symmetric(q, 1, False)]
        orbs_self, _ = f22.orbits(Lself, q, 2)
        pats = free_patterns(GS)
        X, Z = C.X(0), C.Z(0)
        words = (("X", X), ("Z", Z), ("XZ", e1.mat_mul(F, X, Z)))
        rels, d1, d2 = {}, [], []
        kv = True
        for pat in pats:
            h = S1.free_flow(with_u(GS, pat), FR(1, 2))
            Rh, Rhd = one_relation(C, h, zl, wc), one_relation(C, e1.adjoint(F, h), zl, wc)
            R = both(Rh, Rhd)
            rels[pat] = (Rh, Rhd)
            if q in (3, 5):
                kv &= R == f22.adjoint_relation(C, h, zl, wc)
            uf = UF(len(orbs))
            for z, tos in R.items():
                for z2 in tos:
                    uf.u(where[z], where[z2])
            d1.append(uf.count() == 1)
            first = next((wn for wn, w in words if f22.certificate(F, e1.mat_mul(F, h, w))), None)
            d2.append(first)
        n = len(pats)
        out("q=%d: free patterns %d; R_cf orbits %d (sizes %s); R_self orbits %d" %
            (q, n, len(orbs), sorted(set(len(o) for o in orbs)), len(orbs_self)))
        out("  D1 (R_cf) per pattern: %s; first certified word per pattern: %s" % (d1, d2))
        # K-D1neg: no half-layer, and u in place of the half-layer
        if q in (3, 5):
            control("K-indep (v) q=%d: R_h | R_h-dagger equals F2-2's adjoint_relation, every pattern" % q, kv)
        Ru_dirs = (one_relation(C, GS.u_mat, zl, wc), one_relation(C, e1.adjoint(F, GS.u_mat), zl, wc))
        Ru = both(*Ru_dirs)
        res[("Ru", q)] = Ru_dirs
        uf = UF(len(orbs))
        for z, tos in Ru.items():
            for z2 in tos:
                uf.u(where[z], where[z2])
        control("K-D1neg q=%d: no half-layer gives %d = (q^2-1)/4 blocks; u gives the same" % (q, len(orbs)),
                len(orbs) == (q * q - 1) // 4 and uf.count() == len(orbs))
        u = GS.u_mat
        control("K-D2neg q=%d: no certificate on X, u, uX" % q,
                not (f22.certificate(F, X) or f22.certificate(F, u) or f22.certificate(F, e1.mat_mul(F, u, X))))
        if q in (3, 5, 7):
            control("K-frozen q=%d: %d free patterns, first certified word X for each" % (q, n),
                    n == {3: 4, 5: 8, 7: 8}[q] and all(w == "X" for w in d2))
        s_d1 = "ALL" if all(d1) else ("SOME" if any(d1) else "NONE")
        s_d2 = "ALL" if all(d2) else ("SOME" if any(d2) else "NONE")
        token("F24-OD1(%d)" % q, "D1(R_cf) %s; D2 %s; D1(R_self) %s" %
              (s_d1, s_d2, "yes" if len(orbs_self) == 1 else "no"))
        res[("od1", q)] = (s_d1, s_d2, len(orbs_self) == 1)
        res[("rels", q)] = rels
        res[("GS", q)] = GS

    header("OD-2  two sites, R_cf, coupling-free: orbits + free half-layer h (x) h")
    for q in (3, 5, 7, 11, 13):
        Lg = [f22.leap(M, q) for M in f22.symmetric(q, 2, True)]
        orbs, where = f22.orbits(Lg, q, 4)
        rels = res[("rels", q)]
        ok = []
        used_full = 0
        for pat, dirs in rels.items():
            n = two_site_components(orbs, where, dirs, full=False)
            if n != 1:
                used_full += 1
                n = two_site_components(orbs, where, dirs, full=True)
            ok.append(n == 1)
        out("q=%d: R_cf orbits at N=2: %d (sizes %s); one component per pattern: %s; full link set used for %d"
            % (q, len(orbs), sorted(len(o) for o in orbs), ok, used_full))
        nu = two_site_components(orbs, where, res[("Ru", q)], full=True)
        control("K-D1neg q=%d N=2: no half-layer gives %d blocks (> 1); u (x) u gives the same" % (q, len(orbs)),
                UF(len(orbs)).count() == len(orbs) > 1 and nu == len(orbs))
        if q == 3:
            control("K-frozen (3,2): R_cf orbit sizes 8, 8, 16, 48", sorted(len(o) for o in orbs) == [8, 8, 16, 48])
            # K-indep (i) and (iii): the product link set equals F2-2's exact relation of h (x) h
            GS = res[("GS", 3)]
            S2 = f22.Sites(GS, 2)
            C2 = S2.C
            zl2 = [z for z in itertools.product(range(3), repeat=4) if any(z)]
            wc2 = {z: f22.weyl_cols(C2, z) for z in zl2}
            eq, sub = True, True
            for pat, dirs in rels.items():
                hh = S2.free_flow(with_u(GS, pat), FR(1, 2))
                Rex = f22.adjoint_relation(C2, hh, zl2, wc2)
                for z in zl2:
                    v1, v2 = (z[0], z[2]), (z[1], z[3])
                    prod, soundset = set(), set()
                    for R in dirs:
                        R1 = R[v1] if any(v1) else {(0, 0)}
                        R2 = R[v2] if any(v2) else {(0, 0)}
                        prod |= {(w1[0], w2[0], w1[1], w2[1]) for w1 in R1 for w2 in R2}
                        m1, m2 = min(R1), min(R2)
                        soundset |= {(w1[0], m2[0], w1[1], m2[1]) for w1 in R1}
                        soundset |= {(m1[0], w2[0], m1[1], w2[1]) for w2 in R2}
                    eq &= prod == Rex[z]
                    sub &= soundset <= Rex[z]
            control("K-indep (i) product link set = exact relation of h (x) h at (3,2), every pattern", eq)
            control("K-indep (iii) the sound subset lies in the exact relation at (3,2)", sub)
        s = "ALL" if all(ok) else ("SOME" if any(ok) else "NONE")
        token("F24-OD2(%d)" % q, s)
        res[("od2", q)] = s

    header("OD-3  RED corroborated: every R_cf orbit contains a one-site vector")
    allred = True
    for q, N in ((3, 3), (5, 3), (7, 3), (3, 4)):
        zero = tuple(tuple(0 for _ in range(N)) for _ in range(N))
        edges = [tuple(tuple(1 if {a, b} == {i, j} else 0 for b in range(N)) for a in range(N))
                 for i in range(N) for j in range(i + 1, N)]
        Lg = [f22.leap(zero, q)] + [f22.leap(M, q) for M in edges]
        orbs, where = f22.orbits(Lg, q, 2 * N)
        if (q, N) == (3, 3):
            Lfull = [f22.leap(M, q) for M in f22.symmetric(q, N, True)]
            ofull, _ = f22.orbits(Lfull, q, 2 * N)
            control("K-indep (iv) (3,3): orbits of the reduced generators equal those of every R_cf leap",
                    sorted(map(sorted, ofull)) == sorted(map(sorted, orbs)))
        red_ok = all(any(sum(1 for i in range(N) if (v[i], v[N + i]) != (0, 0)) == 1 for v in o) for o in orbs)
        out("(q,N)=(%d,%d): orbits %d, sizes %s; every orbit has a one-site vector: %s"
            % (q, N, len(orbs), sorted(len(o) for o in orbs)[:8], red_ok))
        allred &= red_ok
    token("F24-OD3", "yes" if allred else "no")
    res["od3"] = allred
    return res


# ============================================================================ main and verdict


def main():
    header("F2-4 exact runs (RULES.md)")
    e1_sha, f22_sha = sha256(E1_PATH), sha256(F22_PATH)
    out("sha256 e1_exact.py   %s" % e1_sha)
    out("sha256 f2_2_exact.py %s" % f22_sha)
    st = e1.self_tests()
    control("K0 module hashes and F2-1 self-tests", e1_sha == E1_SHA and f22_sha == F22_SHA and st)
    ad = ad_cells()
    od = od_cells()
    header("Conclusions and verdict")
    qs = (3, 5, 7, 11, 13)
    cf = [q for q in qs if od[("od1", q)][0] == "ALL" and od[("od1", q)][1] == "ALL" and od[("od2", q)] == "ALL"]
    sf = [q for q in qs if od[("od1", q)][1] == "ALL" and od[("od1", q)][2]]
    for q in qs:
        token("F24-CF-DENSE-ALL-N(%d)" % q, "yes [CHAIN W]" if q in cf else "no")
        token("F24-SELF-DENSE-ALL-N(%d)" % q, "yes [SP, PROD W]" if q in sf else "no")
    adx = all(ad[s] for s in ((3, 2), (3, 3), (5, 2)))
    token("F24-AD-GENERAL", "[W] AD; corroborated exactly at (3,2), (3,3), (5,2): %s" % ("yes" if adx else "no"))
    failed = [n for n, ok in CTRL if not ok]
    if failed:
        out("VERDICT VOID: failed controls %s" % failed)
        return
    if len(cf) == len(qs) and len(sf) == len(qs) and od["od3"] and adx:
        out("VERDICT F24-ROBUST-GENERAL")
    else:
        out("VERDICT F24-PARTIAL: R_cf conclusion at q in %s; R_self at q in %s; OD-3 %s; AD-X %s"
            % (cf, sf, od["od3"], adx))
    out("classification: coupling generators universal (MONO); Gamma_spec(u) universal at the q listed; "
        "Gamma_all(u) minus Gamma_spec(u) not decided")


if __name__ == "__main__":
    main()
