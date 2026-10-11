"""E18 probe -- the power cone of Omega_star is self-dual: the polynomial form, exact (Fractions).

Written 2026-10-11T04:40Z (date -u read at 04:36:32Z for NOTES-E18 S0), after NOTES-E18 S0 and before the first run.

SETTING.  Points z = (u, v, X), X in Q^3, S = X.X.  P = {u >= 0, v >= 0, S^3 <= u^2 v^4} (the power cone
u^(1/3) v^(2/3) >= |X| in polynomial form).  The form B(z, z') = u u'/3 + 2 v v'/3 + X.X' (from
<z, w> = T T' + S S' - (1/3)(T S' + S T') + X.X' with u = T + S, v = T - S).  Pseudo-random rationals from a fixed seed.

CHECKS.
  W1  the form identity at 50 rational points: T T' + Sg Sg' - (T Sg' + Sg T')/3 + X.X' = B with u = T + Sg, v = T - Sg.
  W2  AM-GM's factorization (a + 2b)^3 - 27 a b^2 = (a - b)^2 (a + 8b) at 200 rational (a, b); B >= 0 on 400 pairs of
      exact rational points of P (boundary points u = p^3 w^3 q, v = p^3 ..., built so that S^3 = u^2 v^4, and inner
      points scaled into P), each point checked to lie in P.
  W3  for 300 rational z' with u', v' > 0 and S'^3 > u'^2 v'^4: rho = u'^2 v'^4 / S'^3 < 1, theta = (5 + rho)/6,
      s = theta S'/(u' v'), w = (v' s, u' s, -X') lies in P, theta^6 >= rho, and B(w, z') = (theta - 1) S' < 0.
  W4  boundary witnesses: for 100 rational z' with u' = 0, v' >= 0, S' > 0: w = ((v'+1)^2 (S'+1)/S', S'/(v'+1), -X') in P
      and B(w, z') < 0; for 100 with v' = 0, u' > 0, S' > 0: w = (S'/(u'+1), (S'+1)(u'+1), -X') in P and B(w, z') < 0.
  W5  the poles (1, 0, 0) and (0, 1, 0) lie in P; B((1,0,0), z') = u'/3 and B((0,1,0), z') = 2 v'/3, negative for 50
      rational z' with u' < 0 (resp. v' < 0).
COUNTERCONTROLS (each must fail as stated).
  XW1 "with theta = (1 + rho)/2 the interior witness lies in P" (at rho = 99/100).
  XW2 "AM-GM with weights 1/2, 1/2: ((a + b)/2)^3 >= a b^2 for all a, b >= 0" (at (a, b) = (1, 4)).

DECISION RULE (fixed before the first run).  VERDICT E18-POWERCONE-SELFDUAL-EXACT iff W1 ... W5 all pass and XW1, XW2
both fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says the instances agree with
the polynomial-form argument; the general statement is the design module's (NOTES-E18).
"""
import random
from fractions import Fraction as Fr

RESULTS = []
COUNTERS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


def counter(name, claim_holds, detail=''):
    COUNTERS.append((name, not claim_holds))
    print('COUNTER ' + name + (' fails as stated' if not claim_holds else ' HOLDS (unexpected)') +
          ((' -- ' + detail) if detail else ''), flush=True)


rng = random.Random(20261011)


def rq(lo=-9, hi=9, den=7):
    return Fr(rng.randint(lo, hi), rng.randint(1, den))


def dot(X, Y):
    return sum(x * y for x, y in zip(X, Y))


def inP(z):
    u, v, X = z
    S = dot(X, X)
    return u >= 0 and v >= 0 and S ** 3 <= u ** 2 * v ** 4


def B(z, w):
    return z[0] * w[0] / 3 + 2 * z[1] * w[1] / 3 + dot(z[2], w[2])


def unit_dir():
    while True:
        X = [rq() for _ in range(3)]
        if dot(X, X) != 0:
            return X


# ---------------------------------------------------------------- W1
ok1 = True
for _ in range(50):
    T, Sg, Tp, Sgp = rq(), rq(), rq(), rq()
    X, Xp = [rq() for _ in range(3)], [rq() for _ in range(3)]
    lhs = T * Tp + Sg * Sgp - (T * Sgp + Sg * Tp) / 3 + dot(X, Xp)
    ok1 = ok1 and lhs == B((T + Sg, T - Sg, X), (Tp + Sgp, Tp - Sgp, Xp))
check('W1', ok1, 'form identity at 50 rational points')

# ---------------------------------------------------------------- W2
ok2a = True
for _ in range(200):
    a, b = rq(0, 9), rq(0, 9)
    ok2a = ok2a and (a + 2 * b) ** 3 - 27 * a * b ** 2 == (a - b) ** 2 * (a + 8 * b)


def boundary_point():
    # S^3 = u^2 v^4 exactly: take |X|^2 = S = p^2 with X = p * (rational unit vector with rational norm) -- use
    # Pythagorean directions: X = p * (3/13, 4/13, 12/13) up to sign/permutation, so S = p^2; choose u = p^3 / v^2 * k^...
    # simplest exact family: v = q, u = p^3 / q^2 with p, q > 0 rational: u^2 v^4 = p^6 = S^3.
    p, q = rq(1, 9), rq(1, 9)
    signs = [rng.choice((-1, 1)) for _ in range(3)]
    base = [Fr(3, 13), Fr(4, 13), Fr(12, 13)]
    rng.shuffle(base)
    X = [signs[i] * p * base[i] for i in range(3)]
    return (p ** 3 / q ** 2, q, X)


def inner_point():
    z = boundary_point()
    lam = Fr(rng.randint(0, 9), 10)
    return (z[0], z[1], [lam * x for x in z[2]])


pts = [boundary_point() for _ in range(20)] + [inner_point() for _ in range(20)]
allin = all(inP(z) for z in pts)
pairs = [(pts[i], pts[j]) for i in range(len(pts)) for j in range(len(pts))][:400]
minB = min(B(z, w) for z, w in pairs)
check('W2', ok2a and allin and minB >= 0 and len(pairs) == 400,
      'AM-GM factorization at 200 points; 40 exact points of P; minimum B over 400 pairs %s' % minB)

# ---------------------------------------------------------------- W3
ok3, n3 = True, 0
while n3 < 300:
    up, vp = rq(1, 9), rq(1, 9)
    Xp = unit_dir()
    Sp = dot(Xp, Xp)
    if not Sp ** 3 > up ** 2 * vp ** 4:
        continue
    n3 += 1
    rho = up ** 2 * vp ** 4 / Sp ** 3
    theta = (5 + rho) / 6
    s = theta * Sp / (up * vp)
    w = (vp * s, up * s, [-x for x in Xp])
    ok3 = ok3 and rho < 1 and theta ** 6 >= rho and inP(w) and B(w, (up, vp, Xp)) == (theta - 1) * Sp < 0
check('W3', ok3, '300 exterior points with u\', v\' > 0: witness in P, Bernoulli, pairing (theta - 1) S\' < 0')

# ---------------------------------------------------------------- W4
ok4 = True
for _ in range(100):
    vp = rq(0, 9)
    Xp = unit_dir()
    Sp = dot(Xp, Xp)
    w = ((vp + 1) ** 2 * (Sp + 1) / Sp, Sp / (vp + 1), [-x for x in Xp])
    ok4 = ok4 and inP(w) and B(w, (Fr(0), vp, Xp)) < 0
for _ in range(100):
    up = rq(1, 9)
    Xp = unit_dir()
    Sp = dot(Xp, Xp)
    w = (Sp / (up + 1), (Sp + 1) * (up + 1), [-x for x in Xp])
    ok4 = ok4 and inP(w) and B(w, (up, Fr(0), Xp)) < 0
check('W4', ok4, 'boundary witnesses: u\' = 0 (100 points) and v\' = 0 (100 points), in P and pairing negatively')

# ---------------------------------------------------------------- W5
poleU, poleV = (Fr(1), Fr(0), [Fr(0)] * 3), (Fr(0), Fr(1), [Fr(0)] * 3)
ok5 = inP(poleU) and inP(poleV)
for _ in range(50):
    zp = (rq(-9, -1), rq(), [rq() for _ in range(3)])
    ok5 = ok5 and B(poleU, zp) == zp[0] / 3 < 0
    zq = (rq(), rq(-9, -1), [rq() for _ in range(3)])
    ok5 = ok5 and B(poleV, zq) == 2 * zq[1] / 3 < 0
check('W5', ok5, 'poles in P; negative u\' (v\') detected by the pole at 50 points each')

# ---------------------------------------------------------------- countercontrols
rho = Fr(99, 100)
th = (1 + rho) / 2
counter('XW1', th ** 6 >= rho, 'at rho = 99/100: ((1 + rho)/2)^6 = %s < rho' % float(th ** 6))
a, b = Fr(1), Fr(4)
counter('XW2', ((a + b) / 2) ** 3 >= a * b ** 2, 'at (1, 4): ((a + b)/2)^3 = %s < a b^2 = %s' % (((a + b) / 2) ** 3, a * b ** 2))

fails = [n for n, ok in RESULTS if not ok]
cfails = [n for n, ok in COUNTERS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if not fails and not cfails:
    print('VERDICT E18-POWERCONE-SELFDUAL-EXACT')
else:
    print('VERDICT NOT RENDERED -- failing: %s' % ', '.join(fails + cfails))
