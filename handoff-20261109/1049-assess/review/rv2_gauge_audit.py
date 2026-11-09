"""REVIEW-1049-r2: reviewer's exact generic checks (WIP / UNVERIFIED; model-written).

Exact integer arithmetic over Z/q on generic local functions only. No OI mechanism, no observable,
no dynamics iterated (one-step identities only). Imports nothing from probes/ or earlier review
scripts; the d = 3 function is re-coded from its paper definition with a different slot order:
v = (x_{+x}, x_{+y}, x_{+z}, x_{-x}, x_{-y}, x_{-z}).
Run: python3 -I rv2_gauge_audit.py

R1  S1 by an independent witness: the mixed second difference
    D_q = f(e_{+x}+e_{+y}) - f(e_{+x}) - f(e_{+y}) + f(0) equals -1 at every prime 5 <= q < 1000
    (an affine function has D = 0). Paper value: -1/3 - 1/3 - 1/3 + 0 = -1.
R2  (R-uni) covariance f(lam v + c1) = lam f(v) + 2c at every prime 5 <= q <= 101, via the exact
    reduction: a',b',c' are shift-invariant (coefficient check) and G = C P^{-1} is unit-homogeneous
    of degree 1 on the whole plane a'+b'+c' = 0 (exhaustive per q); plus direct exhaustive
    covariance on (Z/q)^6 at q = 5, 7.
R3  SM:96 "the gauge group is the additive-automorphism group, a proper subgroup of all
    permutations": the uniform site-wise permutations sigma of Z/q that are exact symmetries of the
    second-order update x' = f(nbrs) - x_prev, i.e. sigma(f(v) - y) = f(sigma v) - sigma(y) for all
    v, y, are exactly the q(q-1) maps x -> lam x + c, for P1's f at q = 5, 7 (all q! permutations).
R4  Separable (link-sum) rules F = sum_j m_j(x_j), m_j arbitrary: uniform shift covariance
    sum m_j(x_j + c) = sum m_j(x_j) + 2c forces every m_j affine (exhaustive: 2 slots at
    q = 2, 3, 4; 3 slots at q = 3). P1's f is not separable (a nonzero cross difference).
R5  A6 readings at K = 1 (BackgroundIndependence.lean): A6-glob (constant unit g) holds for P1 by
    unit-homogeneity (exhaustive q = 5, 7); A6-inv (site-dependent units, fixed scalar coupling)
    fails for P1 and for the linear control alike (witness); the link-interface insertion
    w_j = M_j x_j with transported unit links is covariant for P1 (one-step identity on a 3x3x3
    torus, seeded cases; consistency check only, not the kernel's A6Cov, whose domain is linkF).
R6  F-8: P1's response to a perturbation about any uniform background is exactly unit-homogeneous
    in the perturbation's amplitude, f(c1 + t d) - f(c1) = t (f(c1 + d) - f(c1)) for every unit t
    (exhaustive q = 5), and is independent of the absolute level c; it is not additive in d.
Controls: linear (1/3)sum (passes R2, R3 = AddAut, R5 glob, R6, separable affine);
countercontrols (1/3)sum + x_{+x}^2 (fails R2, R3 group smaller, R6) and (1/3)sum + 1 (fails R2).
"""
import itertools
import random


def inv(a, q):
    a %= q
    return pow(a, -1, q) if a else 0


def make(q, kind='p1'):
    t = inv(3, q)

    def f(v):
        px, py, pz = v[0] + v[3], v[1] + v[4], v[2] + v[5]
        s = t * sum(v)
        if kind == 'lin':
            return s % q
        if kind == 'sq':
            return (s + v[0] * v[0]) % q
        if kind == 'off':
            return (s + 1) % q
        a = 2 * px - py - pz
        b = 2 * py - pz - px
        c = 2 * pz - px - py
        return (s + a * b * c * inv(a * a + b * b + c * c, q)) % q
    return f


def primes(lo, hi):
    return [n for n in range(lo, hi) if n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))]


res = {}

# R1
e = lambda *idx: tuple(1 if k in idx else 0 for k in range(6))
ok = True
for q in primes(5, 1000):
    f = make(q)
    D = (f(e(0, 1)) - f(e(0)) - f(e(1)) + f(e())) % q
    ok &= D == (q - 1)
    if q in (5, 7):  # control: linear has D = 0
        g = make(q, 'lin')
        ok &= (g(e(0, 1)) - g(e(0)) - g(e(1)) + g(e())) % q == 0
res['R1 D_q = -1 at every prime 5..997 (linear control D = 0)'] = ok

# R2: reduction
coef = {'a': (2, -1, -1), 'b': (-1, 2, -1), 'c': (-1, -1, 2)}  # in terms of (px, py, pz)
res['R2a primed combinations shift-invariant (coefficients sum to 0)'] = all(
    sum(cf) == 0 for cf in coef.values())
ok = True
for q in primes(5, 102):
    units = range(1, q)
    for a in range(q):
        for b in range(q):
            c = (-a - b) % q
            G = a * b * c * inv(a * a + b * b + c * c, q) % q
            for lam in units:
                la, lb, lc = lam * a % q, lam * b % q, lam * c % q
                if la * lb * lc * inv(la * la + lb * lb + lc * lc, q) % q != lam * G % q:
                    ok = False
res['R2b G unit-homogeneous of degree 1 on the plane, every prime 5..101'] = ok


def covariant(f, q, kappa=2):
    for v in itertools.product(range(q), repeat=6):
        fv = f(v)
        for lam in range(1, q):
            for c in range(q):
                if f(tuple((lam * x + c) % q for x in v)) != (lam * fv + kappa * c) % q:
                    return False
    return True


for q in (5, 7):
    res[f'R2c P1 covariance exhaustive q={q}'] = covariant(make(q), q)
res['R2c control linear covariant q=5'] = covariant(make(5, 'lin'), 5)
res['R2c countercontrol square fails q=5'] = not covariant(make(5, 'sq'), 5)
res['R2c countercontrol offset fails q=5'] = not covariant(make(5, 'off'), 5)


# R3
def symmetry_group(f, q):
    table = {v: f(v) for v in itertools.product(range(q), repeat=6)}
    out = []
    for s in itertools.permutations(range(q)):
        good = True
        for v, fv in table.items():
            sv = tuple(s[x] for x in v)
            fsv = table[sv]
            for y in range(q):
                if s[(fv - y) % q] != (fsv - s[y]) % q:
                    good = False
                    break
            if not good:
                break
        if good:
            out.append(s)
    return out


def addaut(q):
    return sorted(tuple((lam * x + c) % q for x in range(q)) for lam in range(1, q) for c in range(q))


for q in (5, 7):
    grp = sorted(symmetry_group(make(q), q))
    res[f'R3 P1 uniform symmetry group == AddAut, q={q} ({len(grp)} maps)'] = grp == addaut(q)
grp = sorted(symmetry_group(make(5, 'lin'), 5))
res['R3 control linear group == AddAut, q=5'] = grp == addaut(5)
grp = symmetry_group(make(5, 'sq'), 5)
res[f'R3 countercontrol square group is smaller, q=5 ({len(grp)} maps)'] = len(grp) < 20


# R4
def is_affine1(m, q):
    return all((m[(x + 1) % q] - m[x]) % q == (m[1] - m[0]) % q for x in range(q))


def separable_check(q, slots):
    funcs = list(itertools.product(range(q), repeat=q))
    n_sol = 0
    for ms in itertools.product(funcs, repeat=slots):
        good = True
        for xs in itertools.product(range(q), repeat=slots):
            base = sum(ms[j][xs[j]] for j in range(slots))
            for c in range(1, q):
                if sum(ms[j][(xs[j] + c) % q] for j in range(slots)) % q != (base + 2 * c) % q:
                    good = False
                    break
            if not good:
                break
        if good:
            n_sol += 1
            if not all(is_affine1(m, q) for m in ms):
                return False, n_sol
    return True, n_sol


for q, slots in ((2, 2), (3, 2), (4, 2), (3, 3)):
    ok, n = separable_check(q, slots)
    res[f'R4 separable + shift-covariant => affine, q={q}, {slots} slots ({n} solutions)'] = ok and n > 0
f5 = make(5)
cross = any((f5(tuple((v[k] + (k == 0) + (k == 1)) % 5 for k in range(6))) - f5(tuple((v[k] + (k == 0)) % 5 for k in range(6)))
             - f5(tuple((v[k] + (k == 1)) % 5 for k in range(6))) + f5(v)) % 5
            for v in itertools.product(range(5), repeat=6))
res['R4 P1 not separable (nonzero cross difference, q=5)'] = cross


# R5
def homogeneous(f, q):
    return all(f(tuple(g * x % q for x in v)) == g * f(v) % q
               for v in itertools.product(range(q), repeat=6) for g in range(1, q))


for q in (5, 7):
    res[f'R5 A6-glob (unit homogeneity) P1 q={q}'] = homogeneous(make(q), q)
# A6-inv witness: site-dependent g (only one neighbour rescaled), fixed scalar coupling
for kind in ('p1', 'lin'):
    f = make(5, kind)
    v = (1, 0, 0, 0, 0, 0)
    gv = (2, 0, 0, 0, 0, 0)  # g = 2 at the +x neighbour, g = 1 elsewhere (incl. centre)
    res[f'R5 A6-inv fails ({kind}) q=5'] = f(gv) != f(v)

rng = random.Random(1049)
ok = True
for q in (5, 7):
    f = make(q)
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    nb = lambda n, d: tuple((n[k] + d[k]) % L for k in range(3))
    for _ in range(20):
        x = {n: rng.randrange(q) for n in sites}
        xp = {n: rng.randrange(q) for n in sites}
        M = {(n, d): rng.randrange(1, q) for n in sites for d in dirs}
        g = {n: rng.randrange(1, q) for n in sites}
        step = lambda x, xp, M: {n: (f(tuple(M[(n, d)] * x[nb(n, d)] for d in dirs)) - xp[n]) % q for n in sites}
        out = step(x, xp, M)
        Mg = {(n, d): g[n] * M[(n, d)] * inv(g[nb(n, d)], q) % q for n in sites for d in dirs}
        outg = step({n: g[n] * x[n] % q for n in sites}, {n: g[n] * xp[n] % q for n in sites}, Mg)
        ok &= all(outg[n] == g[n] * out[n] % q for n in sites)
res['R5 link-interface insertion covariant (3x3x3 torus, q=5,7, 20 seeded cases each)'] = ok


# R6
def ray_homogeneous(f, q):
    for c in range(q):
        cv = (c,) * 6
        f0 = f(cv)
        for d in itertools.product(range(q), repeat=6):
            r1 = (f(tuple((c + x) % q for x in d)) - f0) % q
            for t in range(2, q):
                if (f(tuple((c + t * x) % q for x in d)) - f0) % q != t * r1 % q:
                    return False
    return True


def level_independent(f, q):
    for d in itertools.product(range(q), repeat=6):
        r0 = (f(d) - f((0,) * 6)) % q
        for c in range(1, q):
            if (f(tuple((c + x) % q for x in d)) - f((c,) * 6)) % q != r0:
                return False
    return True


q = 5
F, Lr, Sq = make(q), make(q, 'lin'), make(q, 'sq')
res['R6 P1 response unit-homogeneous about every uniform background q=5'] = ray_homogeneous(F, q)
res['R6 P1 response independent of absolute level q=5'] = level_independent(F, q)
res['R6 control linear homogeneous q=5'] = ray_homogeneous(Lr, q)
res['R6 countercontrol square not homogeneous q=5'] = not ray_homogeneous(Sq, q)
d1, d2 = e(0), e(1)
res['R6 P1 response not additive (q=5)'] = (F(e(0, 1)) - F(d1) - F(d2) + F(e())) % q != 0

for k, v in res.items():
    print(('PASS ' if v else 'FAIL ') + k)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
