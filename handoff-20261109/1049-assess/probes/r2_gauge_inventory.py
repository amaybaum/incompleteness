"""ASSESS-1049 r2: exact generic checks for the gauge-assumption inventory (WIP / UNVERIFIED).

Generic functions over Z/q only; no OI mechanism, no dynamics iterated, no observable computed.
Imports no earlier probe (re-implements the d = 3 function from its paper definition).
Run: python3 -I r2_gauge_inventory.py

f(v) = (1/3) * sum(v) + C * P^{-1}  (P^{-1} := 0 at P = 0), v = (x_{+x}, x_{-x}, x_{+y}, x_{-y}, x_{+z}, x_{-z}),
p_a = x_{+a} + x_{-a}, a' = 2p_x - p_y - p_z (cyclic b', c'), C = a'b'c', P = a'^2 + b'^2 + c'^2.

G1  uniform-amplitude independence of every single-slot first difference:
    f(v + c1 + t e_j) - f(v + c1) = f(v + t e_j) - f(v), all v, c, t, j   (exhaustive, q = 5)
G2  base-point dependence: some single-slot first difference depends on v (non-affine), q = 5
G3  kappa-general uniform covariance f(lam v + c1) = lam f(v) + kappa c with kappa = 2 (exhaustive, q = 5)
G4  site-wise automorphisms as exact symmetries fail for the linear control too
    (shifting one neighbour slot changes the linear update), q = 5
G5  S1: on the plane a'+b'+c' = 0, G = C P^{-1} is not additive at every prime 5 <= q < 200:
    G(1,1,-2) = -1/3 != 0 = G(1,-1,0) + G(2,0,-2) - ... (exact modular)
Controls: linear (1/3)sum passes G1, has no base-point dependence (G2 control), passes G3;
countercontrol (1/3)sum + v_0^2 fails G1 (absolute-amplitude-dependent response).
"""
import itertools

def make(q, extra=None):
    inv = lambda a: pow(a % q, q - 2, q) if a % q else 0
    third = inv(3)
    def f(v):
        px, py, pz = v[0] + v[1], v[2] + v[3], v[4] + v[5]
        a = 2 * px - py - pz; b = 2 * py - pz - px; c = 2 * pz - px - py
        C = a * b * c; P = a * a + b * b + c * c
        base = third * sum(v)
        if extra == 'linear':
            return base % q
        if extra == 'square':
            return (base + v[0] * v[0]) % q
        return (base + C * inv(P)) % q
    return f

def g1(q, f):
    for v in itertools.product(range(q), repeat=6):
        for j in range(6):
            for t in range(1, q):
                vt = list(v); vt[j] = (vt[j] + t) % q
                d0 = (f(vt) - f(v)) % q
                for c in range(1, q):
                    vc = [(x + c) % q for x in v]; vct = list(vc); vct[j] = (vct[j] + t) % q
                    if (f(vct) - f(vc)) % q != d0:
                        return False
    return True

def g2(q, f):
    """True iff some single-slot first difference depends on the base point."""
    for j in range(6):
        for t in range(1, q):
            seen = set()
            for v in itertools.product(range(q), repeat=6):
                vt = list(v); vt[j] = (vt[j] + t) % q
                seen.add((f(vt) - f(v)) % q)
                if len(seen) > 1:
                    return True
    return False

def g3(q, f, kappa=2):
    for v in itertools.product(range(q), repeat=6):
        fv = f(v)
        for lam in range(1, q):
            for c in range(q):
                w = [(lam * x + c) % q for x in v]
                if f(w) != (lam * fv + kappa * c) % q:
                    return False
    return True

q = 5
F, L, Sq = make(q), make(q, 'linear'), make(q, 'square')
res = {}
res['G1 P1-function'] = g1(q, F)
res['G1 control linear'] = g1(q, L)
res['G1 countercontrol square fails'] = not g1(q, Sq)
res['G2 P1-function base-point dependent'] = g2(q, F)
res['G2 control linear not dependent'] = not g2(q, L)
res['G3 P1-function kappa=2'] = g3(q, F)
res['G3 control linear kappa=2'] = g3(q, L)
# G4: shifting one neighbour slot by c is not an exact symmetry of the linear update
v0 = (0,) * 6; v1 = (1, 0, 0, 0, 0, 0)
res['G4 site-wise shift not a symmetry of linear rule'] = (L(v1) - L(v0)) % q != 0
# G5
def is_prime(n):
    return n > 1 and all(n % k for k in range(2, int(n ** 0.5) + 1))
ok5 = True
for qq in [n for n in range(5, 200) if is_prime(n)]:
    inv = lambda a: pow(a % qq, qq - 2, qq) if a % qq else 0
    G = lambda a, b, c: (a * b * c * inv(a * a + b * b + c * c)) % qq
    x, y = (1, 1, -2), (1, -1, 0)
    s = tuple(i + j for i, j in zip(x, y))  # (2, 0, -2)
    ok5 &= G(*x) == (-inv(3)) % qq and G(*y) == 0 and G(*s) == 0 and G(*x) != 0
res['G5 non-additive at all primes 5..199'] = ok5

for k, v in res.items():
    print(k, 'PASS' if v else 'FAIL')
print('ALL PASS' if all(res.values()) else 'SOME FAIL')
raise SystemExit(0 if all(res.values()) else 1)
