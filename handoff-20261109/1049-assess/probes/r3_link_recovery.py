"""ASSESS-1049 r3: exact generic checks for the link-sum recovery and the r3 inventory rows.

WIP / UNVERIFIED; model-written (Claude Code subagent, 2026-11-09).
Exact integer arithmetic over Z/q on generic local functions and one-step identities only.
No OI mechanism, no observable, no dynamics iterated. Imports nothing from probes/ or review/;
every construction is re-coded here from its definition in ASSESS-1049 section 2.1.
Run: python3 -I r3_link_recovery.py

K1  Non-separability. A function on (Z/q)^n is a sum of one-variable functions iff every mixed
    second difference between two distinct slots vanishes. All four constructions of P1's class
    (d = 3 at q = 2, 5, 7; d = 2 at q = 7) have a nonzero mixed difference. Controls: the linear
    rule and the separable non-affine rule sum_j x_j^2 have none (so the test detects
    separability, not affinity).
K2  Link-sum recovery, general form. For F = sum_j m_j(x_j) with arbitrary m_j : Z/q -> Z/q, if
    F(x + c1) - F(x) is independent of x for every c (no value of kappa assumed, lambda = 1 only),
    then every m_j is affine. Exhaustive: 2 slots at q = 2, 3, 4; 3 slots at q = 2, 3.
    Countercontrol: a non-separable, uniformly shift-covariant, non-affine rule exists already at
    q = 3 with 2 slots (F = 2 x1 + (x2 - x1)^2), so separability is load-bearing.
K3  (R-uni) is not implied by affinity: the affine rule (1/3) sum + 1 at q = 5 fails the
    kappa-general covariance F(lam v + c1) = lam F(v) + kappa c for every kappa (witness per kappa);
    the linear rule (1/3) sum passes it at kappa = 2. With P1 satisfying (R-uni), the two are
    incomparable.
K4  Uniform permutation symmetries of the second-order update x' = f(v) - y, i.e. sigma with
    sigma(f(v) - y) = f(sigma v) - sigma(y) for all v, y, over all q! permutations: exactly AddAut
    for the d = 2, q = 7 construction (42 maps) and for the d = 3, q = 2 construction (2 maps).
    Countercontrol: d = 2, q = 7 rule (1/2) sum + x_E^2 has a smaller group.
"""
import itertools


def inv(a, q):
    a %= q
    return pow(a, -1, q) if a else 0


def legendre(a, q):
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else q - 1  # -1 mod q


# d = 3: slots (x_{+x}, x_{-x}, x_{+y}, x_{-y}, x_{+z}, x_{-z})
def d3_prime(q):
    t = inv(3, q)

    def f(v):
        px, py, pz = v[0] + v[1], v[2] + v[3], v[4] + v[5]
        a, b, c = 2 * px - py - pz, 2 * py - pz - px, 2 * pz - px - py
        P = a * a + b * b + c * c
        return (t * sum(v) + a * b * c * pow(P % q, q - 2, q)) % q
    return f


def d3_q2(v):
    return (sum(v) + (1 if len(set(v)) == 1 else 0)) % 2


# d = 2: slots (x_E, x_W, x_N, x_S)
def d2_q7(kind='p1'):
    q, h = 7, inv(2, 7)

    def f(v):
        E, W, N, S = v
        base = h * (E + W + N + S)
        if kind == 'lin':
            return base % q
        if kind == 'sq':
            return (base + E * E) % q
        y1, y2, y3 = E - W, N - S, E + W - N - S
        return (base + y3 * legendre(y1 * y1 - y2 * y2, q)) % q
    return f


def mixed_nonzero(f, q, n):
    """Return a witness (j, k, x) with a nonzero mixed second difference, or None."""
    for x in itertools.product(range(q), repeat=n):
        fx = f(x)
        for j in range(n):
            xj = list(x)
            xj[j] = (xj[j] + 1) % q
            fj = f(tuple(xj))
            for k in range(j + 1, n):
                xk = list(x)
                xk[k] = (xk[k] + 1) % q
                xjk = list(xj)
                xjk[k] = (xjk[k] + 1) % q
                if (f(tuple(xjk)) - fj - f(tuple(xk)) + fx) % q:
                    return (j, k, x)
    return None


res = {}

# K1
for name, f, q, n in (('d=3 q=2', d3_q2, 2, 6), ('d=3 q=5', d3_prime(5), 5, 6),
                      ('d=3 q=7', d3_prime(7), 7, 6), ('d=2 q=7', d2_q7(), 7, 4)):
    w = mixed_nonzero(f, q, n)
    res[f'K1 P1 construction {name} not separable (witness {w})'] = w is not None
res['K1 control linear d=2 q=7 separable'] = mixed_nonzero(d2_q7('lin'), 7, 4) is None
res['K1 control sum x_j^2 (q=5, 3 slots) separable'] = mixed_nonzero(
    lambda v: sum(x * x for x in v) % 5, 5, 3) is None


# K2
def affine1(m, q):
    return all((m[(x + 1) % q] - m[x]) % q == (m[1] - m[0]) % q for x in range(q))


def recovery(q, slots):
    funcs = list(itertools.product(range(q), repeat=q))
    states = list(itertools.product(range(q), repeat=slots))
    zero = (0,) * slots
    n_sol = 0
    for ms in itertools.product(funcs, repeat=slots):
        F = lambda x: sum(ms[j][x[j]] for j in range(slots)) % q
        ok = True
        for c in range(1, q):
            h = (F(tuple(c for _ in range(slots))) - F(zero)) % q
            for x in states:
                if (F(tuple((xi + c) % q for xi in x)) - F(x)) % q != h:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            n_sol += 1
            if not all(affine1(m, q) for m in ms):
                return False, n_sol
    return True, n_sol


for q, slots in ((2, 2), (3, 2), (4, 2), (2, 3), (3, 3)):
    ok, n = recovery(q, slots)
    res[f'K2 separable + state-independent shift effect => affine, q={q}, {slots} slots '
        f'({n} solutions)'] = ok and n > 0
q = 3
G = lambda x: (2 * x[0] + (x[1] - x[0]) ** 2) % q
cov = all((G(((a + c) % q, (b + c) % q)) - G((a, b))) % q == 2 * c % q
          for a in range(q) for b in range(q) for c in range(q))
nonaff = (G((1, 1)) - G((1, 0)) - G((0, 1)) + G((0, 0))) % q != 0
res['K2 countercontrol 2x1+(x2-x1)^2 at q=3: shift-covariant, non-separable, non-affine'] = (
    cov and nonaff and mixed_nonzero(G, 3, 2) is not None)

# K3
q = 5
t = inv(3, q)
aff = lambda v: (t * sum(v) + 1) % q
lin = lambda v: (t * sum(v)) % q


def fails_every_kappa(f):
    for kappa in range(q):
        found = False
        for v in itertools.product(range(q), repeat=6):
            for lam in range(1, q):
                for c in range(q):
                    if f(tuple((lam * x + c) % q for x in v)) != (lam * f(v) + kappa * c) % q:
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            return False
    return True


res['K3 affine (1/3)sum+1 at q=5 fails kappa-general (R-uni) for every kappa'] = fails_every_kappa(aff)
res['K3 control linear (1/3)sum at q=5 satisfies (R-uni) at kappa=2 (exhaustive)'] = all(
    lin(tuple((lam * x + c) % q for x in v)) == (lam * lin(v) + 2 * c) % q
    for v in itertools.product(range(q), repeat=6) for lam in range(1, q) for c in range(q))


# K4
def uniform_group(f, q, n):
    table = {v: f(v) for v in itertools.product(range(q), repeat=n)}
    out = []
    for s in itertools.permutations(range(q)):
        good = True
        for v, fv in table.items():
            fsv = table[tuple(s[x] for x in v)]
            for y in range(q):
                if s[(fv - y) % q] != (fsv - s[y]) % q:
                    good = False
                    break
            if not good:
                break
        if good:
            out.append(s)
    return sorted(out)


def addaut(q):
    return sorted({tuple((lam * x + c) % q for x in range(q)) for lam in range(1, q) if
                   all((lam * k) % q for k in range(1, q)) for c in range(q)})


g = uniform_group(d2_q7(), 7, 4)
res[f'K4 d=2 q=7 construction: uniform symmetry group == AddAut ({len(g)} maps)'] = g == addaut(7)
g = uniform_group(d3_q2, 2, 6)
res[f'K4 d=3 q=2 construction: uniform symmetry group == AddAut ({len(g)} maps)'] = g == addaut(2)
g = uniform_group(d2_q7('sq'), 7, 4)
res[f'K4 countercontrol (1/2)sum+x_E^2 at q=7: group smaller ({len(g)} maps)'] = len(g) < 42

for k, v in res.items():
    print(('PASS ' if v else 'FAIL ') + k)
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
