#!/usr/bin/env python3
"""R1-INF exact checks (stdlib only, deterministic).

Selected update (NR-1 (U)): x(t+1) = alpha*S x(t) - x(t-1) over Z_q, state (u, v) = (x(t), x(t-1)),
F(u, v) = (alpha*S u - v, u), S the nearest-neighbour sum.

Parts
  A  d = 1: the window trajectory of sites {0,1} is onto Z_q^{2(T+1)} (rank) and determines the
     time-0 state on a central interval (row-space membership)   [Proposition 5(i)]
  B  d = 2: rank growth per step of the box-window trajectory, q = 2 (illustration only)
  C  rooted maps under the uniform product prior: row and column sums (L3), with a countercontrol
     under the point-mass hidden prior delta_0 (Lemma 8)
  D  product laws that are not invariant
  E  real-valued additive conserved quantities of range <= 2 (rational linear algebra on tori),
     with positive controls (identity, rule 184), and the d = 1 mover identities for alpha^2 = 1
     (Proposition 6)
  F  finitely supported seeds do not return (illustration of Lemma 4; the proof is algebraic)
  G  U without translation invariance (Proposition 9): dim(Gamma ∩ R_Lambda_n) = 2n+2 for the
     closed subgroup H = {x : x_t(0) = 0 for all t}, d = 1, 2, stable in the horizon T; the
     site functionals are cross-checked against direct evolution; countercontrol alpha = 0;
     u(e_1) is not in Gamma (H is not translation invariant)
  H  d = 2: the two-plane trajectory is onto and determining (Proposition 5.2), countercontrol
     alpha = 0
Run:  python3 -I r1_inf_checks.py
"""
from fractions import Fraction
from itertools import product
import random

# ---------------------------------------------------------------- linear algebra helpers
def rank_mod_p(rows, p):
    """Rank over GF(p) of a list of integer row vectors."""
    rows = [[x % p for x in r] for r in rows]
    rank, ncols = 0, (len(rows[0]) if rows else 0)
    for c in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][c]), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        inv = pow(rows[rank][c], p - 2, p)
        rows[rank] = [(x * inv) % p for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][c]:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


class RatEchelon:
    """Incremental rational row echelon basis (for null-space dimension)."""
    def __init__(self, n):
        self.n, self.piv = n, {}  # pivot column -> row

    def add(self, row):
        row = [Fraction(x) for x in row]
        for c, r in self.piv.items():
            if row[c]:
                f = row[c]
                row = [a - f * b for a, b in zip(row, r)]
        c = next((i for i, x in enumerate(row) if x), None)
        if c is None:
            return False
        inv = 1 / row[c]
        row = [x * inv for x in row]
        for c2, r in list(self.piv.items()):
            if r[c]:
                f = r[c]
                self.piv[c2] = [a - f * b for a, b in zip(r, row)]
        self.piv[c] = row
        return True

    def rank(self):
        return len(self.piv)

# ---------------------------------------------------------------- linear evolution with symbolic coefficients
def evolve_linear_1d(q, alpha, sites, T, back=False):
    """Coefficient vectors (over Z_q) of x(t)(z) in terms of initial unknowns
    u0(s), v0(s) for s in `sites`, assuming everything outside `sites` is 0 (only used inside the
    light cone, where that assumption is irrelevant). Returns dict t -> dict z -> vector."""
    idx = {('u', s): i for i, s in enumerate(sites)}
    idx.update({('v', s): len(sites) + i for i, s in enumerate(sites)})
    n = 2 * len(sites)
    zero = [0] * n

    def unit(key):
        e = [0] * n
        e[idx[key]] = 1
        return e
    lo, hi = min(sites), max(sites)
    x = {0: {z: unit(('u', z)) for z in sites}, -1: {z: unit(('v', z)) for z in sites}}
    get = lambda t, z: x[t].get(z, zero)
    rng = range(1, T + 1)
    for t in rng:
        x[t] = {}
        for z in range(lo, hi + 1):
            a, b, c = get(t - 1, z - 1), get(t - 1, z + 1), get(t - 2, z)
            x[t][z] = [(alpha * (a1 + b1) - c1) % q for a1, b1, c1 in zip(a, b, c)]
    if back:  # x(t-1) = alpha*S x(t) - x(t+1)
        for t in range(-2, -T - 2, -1):
            x[t] = {}
            for z in range(lo, hi + 1):
                a, b, c = get(t + 1, z - 1), get(t + 1, z + 1), get(t + 2, z)
                x[t][z] = [(alpha * (a1 + b1) - c1) % q for a1, b1, c1 in zip(a, b, c)]
    return x, idx


def part_A():
    print("== A. d = 1: window {0,1} trajectory, onto and determining ==")
    for q, alpha in [(2, 1), (3, 1), (3, 2), (5, 1), (5, 3)]:
        T = 6
        sites = list(range(-T - 2, T + 4))
        x, idx = evolve_linear_1d(q, alpha, sites, T + 1, back=True)
        # onto: forward window trajectory t = 0..T has full rank 2(T+1)
        fwd = [x[t][z] for t in range(0, T + 1) for z in (0, 1)]
        onto = rank_mod_p(fwd, q) == 2 * (T + 1)
        # determining: trajectory over t in [-T, T] (light-cone exact for |t| <= T) contains, in its
        # row space, the coordinates u0(s), v0(s) for s in a central interval
        rows = [x[t][z] for t in range(-T, T + 1) for z in (0, 1)]
        r0 = rank_mod_p(rows, q)
        det = []
        for s in range(-T + 2, T):
            for key in (('u', s), ('v', s)):
                e = [0] * len(rows[0]); e[idx[key]] = 1
                det.append(rank_mod_p(rows + [e], q) == r0)
        print(f"q={q} alpha={alpha} T={T}: onto rank {rank_mod_p(fwd, q)}/{2*(T+1)} {'OK' if onto else 'FAIL'};"
              f" central interval [{-T+2},{T-1}] determined: {all(det)} ({sum(det)}/{len(det)} coords)")
    # countercontrol: alpha = 0 (F(u,v) = (-v,u)) -- the window does not determine neighbours
    q, alpha, T = 3, 0, 6
    sites = list(range(-T - 2, T + 4))
    x, idx = evolve_linear_1d(q, alpha, sites, T + 1, back=True)
    rows = [x[t][z] for t in range(-T, T + 1) for z in (0, 1)]
    r0 = rank_mod_p(rows, q)
    e = [0] * len(rows[0]); e[idx[('u', 2)]] = 1
    print(f"countercontrol q=3 alpha=0: window rank {r0} (bounded); u0(2) determined: {rank_mod_p(rows+[e], q)==r0}")


def part_B():
    print("== B. d = 2, q = 2, alpha = 1: rank increments of the n x n box-window trajectory ==")
    q, alpha = 2, 1
    for n in (1, 2, 3, 4):
        Tmax = 8
        R = Tmax + 1
        sites = [(i, j) for i in range(-R, n + R) for j in range(-R, n + R)]
        pos = {s: k for k, s in enumerate(sites)}
        N = 2 * len(sites)
        zero = [0] * N
        def unit(k):
            e = [0] * N; e[k] = 1; return e
        x = {0: {s: unit(pos[s]) for s in sites}, -1: {s: unit(len(sites) + pos[s]) for s in sites}}
        get = lambda t, s: x[t].get(s, zero)
        for t in range(1, Tmax):
            x[t] = {}
            for (i, j) in sites:
                acc = [0] * N
                for nb in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    acc = [a + b for a, b in zip(acc, get(t - 1, nb))]
                c = get(t - 2, (i, j))
                x[t][(i, j)] = [(alpha * a - b) % q for a, b in zip(acc, c)]
        W = [(i, j) for i in range(n) for j in range(n)]
        ranks = []
        for T in range(1, Tmax + 1):
            rows = [x[t][w] for t in range(T) for w in W]
            ranks.append(rank_mod_p(rows, q))
        inc = [ranks[0]] + [ranks[k] - ranks[k - 1] for k in range(1, len(ranks))]
        print(f"n={n}: rank(T), T=1..{Tmax}: {ranks}; increments {inc}")


# ---------------------------------------------------------------- rooted maps (brute force, no linearity used)
def step_1d(state, q, alpha, lo, hi):
    u, v = state
    nu = {}
    for z in range(lo, hi + 1):
        nu[z] = (alpha * (u.get(z - 1, 0) + u.get(z + 1, 0)) - v.get(z, 0)) % q
    return nu, dict(u)


def rooted_map(q, alpha, t, hidden_law):
    """Gamma_t(a, b) for window W = {0,1}, d = 1, hidden coordinates on the light cone [-t, t+1]
    minus W (both u and v), law = product of `hidden_law` (dict value -> prob).  Exact Fractions."""
    W = (0, 1)
    hid = [z for z in range(-t, t + 2) if z not in W]
    lo, hi = -t, t + 1
    V = list(product(range(q), repeat=4))
    G = {}
    for a in V:
        row = {}
        for h in product(range(q), repeat=2 * len(hid)):
            w = Fraction(1)
            for val in h:
                w *= hidden_law[val]
            if w == 0:
                continue
            u = {0: a[0], 1: a[1]}; v = {0: a[2], 1: a[3]}
            for k, z in enumerate(hid):
                u[z] = h[k]; v[z] = h[len(hid) + k]
            st = (u, v)
            for _ in range(t):
                st = step_1d(st, q, alpha, lo, hi)
            b = (st[0][0], st[0][1], st[1][0], st[1][1])
            row[b] = row.get(b, 0) + w
        G[a] = row
    rows_ok = all(sum(G[a].values()) == 1 for a in V)
    cols = {b: sum(G[a].get(b, 0) for a in V) for b in V}
    return rows_ok, cols


def part_C():
    print("== C. rooted maps, d = 1, W = {0,1}: row sums and column sums (L3) ==")
    for q, alpha, tmax in [(2, 1, 3), (3, 1, 2)]:
        uni = {k: Fraction(1, q) for k in range(q)}
        for t in range(1, tmax + 1):
            rows_ok, cols = rooted_map(q, alpha, t, uni)
            colok = all(c == 1 for c in cols.values())
            print(f"uniform hidden prior q={q} alpha={alpha} t={t}: rows sum to 1: {rows_ok}; columns sum to 1: {colok}")
    # countercontrol: point-mass hidden prior delta_0 (Unif(V) x delta_0 is not invariant)
    for q in (2, 3):
        point = {k: (Fraction(1) if k == 0 else Fraction(0)) for k in range(q)}
        rows_ok, cols = rooted_map(q, 1, 2, point)
        print(f"countercontrol hidden delta_0 q={q} t=2: rows sum to 1: {rows_ok};"
              f" column sums {sorted(str(c) for c in set(cols.values()))}")


def part_D():
    print("== D. product laws that are not invariant ==")
    p = Fraction(1, 4)
    # u'(0) = u(-1) + u(1) + v(0) mod 2, three independent Bern(p) inputs
    P1 = sum(Fraction(1) * (p if a else 1 - p) * (p if b else 1 - p) * (p if c else 1 - p)
             for a, b, c in product((0, 1), repeat=3) if (a + b + c) % 2 == 1)
    print(f"selected rule q=2 alpha=1 under Bern(1/4)^Z for u and v: P(u'(0)=1) = {P1} (input marginal {p})")
    # non-surjective CA (outside the OI class): y(z) = x(z) AND x(z+1) under the uniform law
    P2 = Fraction(sum(1 for a, b in product((0, 1), repeat=2) if a & b), 4)
    print(f"AND rule (not surjective) under uniform Bernoulli: P(y(0)=1) = {P2} (input marginal 1/2)")


# ---------------------------------------------------------------- additive conserved quantities
def conserved_dim(alphabet, step_torus, k, Ls):
    """Dimension of {f : A^k -> Q : sum_z f(window_z(F x)) = sum_z f(window_z(x)) on tori of the
    given lengths}.  Unknown index = pattern on k consecutive sites."""
    A = list(alphabet)
    pats = list(product(A, repeat=k))
    pidx = {p: i for i, p in enumerate(pats)}
    n = len(pats)
    ech = RatEchelon(n)
    for L in Ls:
        for x in product(A, repeat=L):
            y = step_torus(x)
            row = [0] * n
            for z in range(L):
                row[pidx[tuple(y[(z + j) % L] for j in range(k))]] += 1
                row[pidx[tuple(x[(z + j) % L] for j in range(k))]] -= 1
            if any(row):
                ech.add(row)
    return n - ech.rank(), len(A) ** (k - 1)


def part_E():
    print("== E. real-valued additive conserved quantities of range k (tori), dim vs trivial dim ==")
    def second_order(q, alpha):
        A = [(a, b) for a in range(q) for b in range(q)]
        def stp(x):
            L = len(x)
            return tuple(((alpha * (x[(z - 1) % L][0] + x[(z + 1) % L][0]) - x[z][1]) % q, x[z][0])
                         for z in range(L))
        return A, stp
    ident = ([0, 1], lambda x: x)
    def r184(x):
        L = len(x)
        out = []
        for z in range(L):
            l, c, r = x[(z - 1) % L], x[z], x[(z + 1) % L]
            out.append((184 >> (4 * l + 2 * c + r)) & 1)
        return tuple(out)
    cases = [("identity (control)", ident[0], ident[1], 2, range(3, 9)),
             ("rule 184 (control)", [0, 1], r184, 2, range(3, 11)),
             ("selected q=2 alpha=1", *second_order(2, 1), 1, range(3, 9)),
             ("selected q=2 alpha=1", *second_order(2, 1), 2, range(3, 8)),
             ("selected q=3 alpha=1", *second_order(3, 1), 1, range(3, 6)),
             ("selected q=3 alpha=1", *second_order(3, 1), 2, range(3, 6)),
             ("selected q=3 alpha=2", *second_order(3, 2), 2, range(3, 6))]
    for name, A, stp, k, Ls in cases:
        dim, triv = conserved_dim(A, stp, k, Ls)
        print(f"{name}, k={k}, L={Ls.start}..{Ls.stop-1}: solution dim {dim}, trivial dim {triv}"
              f" -> {'nontrivial conserved quantity' if dim > triv else 'only trivial'}")
    # identification (d = 1, alpha = +-1): movers a_z = u_z - alpha v_{z+1}, b_z = u_{z+1} - alpha v_z
    # satisfy a'_z = alpha a_{z-1}, b'_z = alpha b_{z+1}; checked on random tori
    rnd = random.Random(7)
    for q, alpha in [(2, 1), (3, 1), (3, 2), (5, 1), (5, 4)]:
        A, stp = second_order(q, alpha)
        ok = True
        for _ in range(200):
            L = rnd.randint(3, 40)
            x = tuple(rnd.choice(A) for _ in range(L))
            y = stp(x)
            a = lambda s, z: (s[z % L][0] - alpha * s[(z + 1) % L][1]) % q
            b = lambda s, z: (s[(z + 1) % L][0] - alpha * s[z % L][1]) % q
            ok &= all(a(y, z) == (alpha * a(x, z - 1)) % q and b(y, z) == (alpha * b(x, z + 1)) % q
                      for z in range(L))
        print(f"movers q={q} alpha={alpha} (alpha^2 = 1 mod q): a'_z = alpha a_(z-1), b'_z = alpha b_(z+1): {ok}")


def part_F():
    print("== F. finitely supported seeds: no return (illustration) ==")
    for q, alpha, T in [(2, 1, 400), (3, 1, 400), (5, 2, 400)]:
        u = {0: 1}; v = {}
        start = (tuple(sorted(u.items())), tuple(sorted(v.items())))
        ret = None; maxsupp = 0
        for t in range(1, T + 1):
            lo = min(list(u) + list(v)) - 1; hi = max(list(u) + list(v)) + 1
            nu = {z: (alpha * (u.get(z - 1, 0) + u.get(z + 1, 0)) - v.get(z, 0)) % q for z in range(lo, hi + 1)}
            nu = {z: c for z, c in nu.items() if c}
            v, u = {z: c for z, c in u.items() if c}, nu
            maxsupp = max(maxsupp, len(u) + len(v))
            if (tuple(sorted(u.items())), tuple(sorted(v.items()))) == start:
                ret = t; break
        print(f"d=1 q={q} alpha={alpha}: single-site seed returns within {T} steps: {ret is not None}; final support {len(u)+len(v)}")


# ---------------------------------------------------------------- site functionals x_t(0) (any d)
def site_functionals(q, alpha, d, tmin, tmax):
    """P[t] = (U, V): sparse dicts site -> coefficient with x_t(0) = sum U(z) u(z) + V(z) v(z),
    x_t the first component of F^t.  Recurrences x_{t+1}(0) = alpha*sum_nb x_t(nb) - x_{t-1}(0) and
    x_{t-1}(0) = alpha*sum_nb x_t(nb) - x_{t+1}(0); x_t(nb) is the translate of x_t(0) by nb."""
    units = [tuple((1 if k == j else 0) * sgn for k in range(d)) for j in range(d) for sgn in (1, -1)]
    o = tuple([0] * d)
    def comb(Pt, Pother):
        out = []
        for part in range(2):
            acc = {}
            for z, c in Pt[part].items():
                for e in units:
                    w = tuple(a + b for a, b in zip(z, e))
                    acc[w] = (acc.get(w, 0) + alpha * c) % q
            for z, c in Pother[part].items():
                acc[z] = (acc.get(z, 0) - c) % q
            out.append({z: c for z, c in acc.items() if c})
        return tuple(out)
    P = {0: ({o: 1}, {}), -1: ({}, {o: 1})}
    for t in range(1, tmax + 1):
        P[t] = comb(P[t - 1], P[t - 2])
    for t in range(-2, tmin - 1, -1):
        P[t] = comb(P[t + 1], P[t + 2])
    return P


def eval_functional(Pt, u, v):
    s = 0
    for z, c in Pt[0].items():
        s += c * u.get(z, 0)
    for z, c in Pt[1].items():
        s += c * v.get(z, 0)
    return s


def vec(Pt, coords, q, shift=None):
    shift = shift or tuple([0] * len(next(iter(coords))[1]))
    r = [0] * len(coords)
    for part in range(2):
        for z, c in Pt[part].items():
            r[coords[(part, tuple(a + b for a, b in zip(z, shift)))]] = c % q
    return r


def box(d, R):
    return list(product(range(-R, R + 1), repeat=d))


def cross_check_functionals():
    """Evaluate x_t(0) from the functionals and by direct evolution on a torus (light cone inside)."""
    rnd = random.Random(11)
    ok = True
    for q, alpha, d, T in [(2, 1, 2, 4), (3, 2, 2, 3), (5, 3, 1, 6)]:
        P = site_functionals(q, alpha, d, -T - 1, T)
        L = 2 * T + 5
        sites = list(product(range(L), repeat=d))
        u = {z: rnd.randrange(q) for z in sites}; v = {z: rnd.randrange(q) for z in sites}
        def F(u, v, inv=False):
            nu = {}
            src = v if inv else u
            for z in sites:
                acc = 0
                for j in range(d):
                    for sgn in (1, -1):
                        w = list(z); w[j] = (w[j] + sgn) % L; acc += src[tuple(w)]
                nu[z] = (alpha * acc - (u if inv else v)[z]) % q
            return (src, nu) if inv else (nu, u)
        cen = lambda z: tuple(((a + L // 2) % L) for a in z)
        uc = {zz: u[cen(zz)] for zz in box(d, T + 1)}; vc = {zz: v[cen(zz)] for zz in box(d, T + 1)}
        fu, fv = dict(u), dict(v)
        for t in range(0, T + 1):
            ok &= eval_functional(P[t], uc, vc) % q == fu[cen(tuple([0] * d))]
            fu, fv = F(fu, fv)
        bu, bv = dict(u), dict(v)
        for t in range(-1, -T - 2, -1):
            bu, bv = F(bu, bv, inv=True)
            ok &= eval_functional(P[t], uc, vc) % q == bu[cen(tuple([0] * d))]
    return ok


def part_G():
    print("== G. U without translation invariance: H = {x : x_t(0) = 0 for all t} ==")
    print(f"functionals x_t(0) agree with direct evolution on tori: {cross_check_functionals()}")
    for d, nmax in [(1, 5), (2, 3)]:
        for q, alpha in [(2, 1), (3, 1), (3, 2), (0, 0)]:
            if q == 0:
                q, alpha, tag = 3, 0, " [countercontrol alpha=0]"
            else:
                tag = ""
            res = []
            for n in range(1, nmax + 1):
                defs = []
                for T in (n + 1, n + 3, n + 5):
                    P = site_functionals(q, alpha, d, -T - 1, T)
                    R = T + 2
                    coords = {}
                    for part in range(2):
                        for z in box(d, R):
                            coords[(part, z)] = len(coords)
                    rows = [vec(P[t], coords, q) for t in range(-T - 1, T + 1)]
                    outside = [i for (part, z), i in coords.items() if max(abs(a) for a in z) > n]
                    r_all = rank_mod_p(rows, q)
                    r_out = rank_mod_p([[r[i] for i in outside] for r in rows], q)
                    defs.append(r_all - r_out)  # dim(Gamma_T intersect R_{Lambda_n})
                res.append(defs[0] if len(set(defs)) == 1 else defs)
            target = [2 * n + 2 for n in range(1, nmax + 1)]
            print(f"d={d} q={q} alpha={alpha}{tag}: deficit dim(Gamma ∩ R_Lambda_n), n=1..{nmax}: {res};"
                  f" equals 2n+2: {res == target}")
    # translation non-invariance: u(e_1) is not in Gamma (d = 2, q = 2, alpha = 1; T = 6)
    q, alpha, d, T = 2, 1, 2, 6
    P = site_functionals(q, alpha, d, -T - 1, T)
    coords = {}
    for part in range(2):
        for z in box(d, T + 2):
            coords[(part, z)] = len(coords)
    rows = [vec(P[t], coords, q) for t in range(-T - 1, T + 1)]
    e = [0] * len(coords); e[coords[(0, (1, 0))]] = 1
    print(f"d=2 q=2 alpha=1: u(e_1) in span{{x_t(0): |t|<=7}}: {rank_mod_p(rows + [e], q) == rank_mod_p(rows, q)}")


def part_H():
    print("== H. d = 2: two-plane trajectory {z_1 in {0,1}} x [-m,m] is onto and determining ==")
    for q, alpha in [(2, 1), (3, 1), (3, 2), (5, 3)]:
        T, m = 3, 3
        P = site_functionals(q, alpha, 2, -T - 1, T + 1)
        R = T + m + 4
        coords = {}
        for part in range(2):
            for z in box(2, R):
                coords[(part, z)] = len(coords)
        plane = [(z1, y) for z1 in (0, 1) for y in range(-m, m + 1)]
        fwd = [vec(P[t], coords, q, shift=s) for t in range(0, T + 1) for s in plane]
        rows = [vec(P[t], coords, q, shift=s) for t in range(-T, T + 1) for s in plane]
        r0 = rank_mod_p(rows, q)
        det = []
        for key in ((0, (2, 0)), (1, (2, 0)), (0, (-1, 0)), (1, (-1, 1))):
            e = [0] * len(coords); e[coords[key]] = 1
            det.append(rank_mod_p(rows + [e], q) == r0)
        print(f"q={q} alpha={alpha}: forward rank {rank_mod_p(fwd, q)}/{len(fwd)};"
              f" u0,v0 at (2,0), u0 at (-1,0), v0 at (-1,1) determined: {all(det)}")
    # countercontrol alpha = 0: the planes do not determine the neighbouring plane
    q, alpha, T, m = 3, 0, 3, 3
    P = site_functionals(q, alpha, 2, -T - 1, T + 1)
    coords = {}
    for part in range(2):
        for z in box(2, T + m + 4):
            coords[(part, z)] = len(coords)
    plane = [(z1, y) for z1 in (0, 1) for y in range(-m, m + 1)]
    rows = [vec(P[t], coords, q, shift=s) for t in range(-T, T + 1) for s in plane]
    e = [0] * len(coords); e[coords[(0, (2, 0))]] = 1
    print(f"countercontrol q=3 alpha=0: u0 at (2,0) determined: {rank_mod_p(rows + [e], q) == rank_mod_p(rows, q)}")


if __name__ == "__main__":
    random.seed(0)
    part_A(); part_B(); part_C(); part_D(); part_E(); part_F(); part_G(); part_H()
