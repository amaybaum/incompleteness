"""c7 (independent r7c check): F1 at QX-4 R4.9, exact over F_2.

Generic object only: the reciprocal coupling T(c, x, m, m') = (c, x + m', m + c, m') on F_2^4, pairs (c, x) and
(m, m'), omega(u, v) = u_c v_x - u_x v_c + u_m v_m' - u_m' v_m.  No OI mechanism is computed.  Standard library
only (fractions, itertools); imports no earlier probe.

SA-1(c) meter law: uniform on the line {l = k} of the (m, m') plane, l a nonzero functional, independent of the
carrier; carrier x uniform on {0, 1} on each branch c.
K_null: the exact channel on x on the silent branch c = 0, K[x][x'] = P(x' | x, c = 0), meter marginalized.
K_null = id iff that matrix is the 2x2 identity.
"""
import itertools
import sys
from fractions import Fraction

NF = 0


def check(name, cond, detail=""):
    global NF
    NF += (not cond)
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + str(detail)) if detail != "" else ""))


def T(y):
    c, x, m, mp = y
    return (c, (x + mp) % 2, (m + c) % 2, mp)


def omega(u, v):
    return (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % 2


E = [tuple(1 if k == i else 0 for k in range(4)) for i in range(4)]
check("0a T is a bijection of F_2^4", len({T(y) for y in itertools.product((0, 1), repeat=4)}) == 16)
check("0b T is linear and symplectic: omega(T e_i, T e_j) = omega(e_i, e_j) for all basis pairs",
      all(omega(T(E[i]), T(E[j])) == omega(E[i], E[j]) for i in range(4) for j in range(4)))
check("0c T is location-preserving (c' = c)", all(T(y)[0] == y[0] for y in itertools.product((0, 1), repeat=4)))

LAWS = {"m": (1, 0), "m'": (0, 1), "m+m'": (1, 1)}


def line(l, k):
    return [p for p in itertools.product((0, 1), repeat=2) if (l[0] * p[0] + l[1] * p[1]) % 2 == k]


def k_null(R):
    K = [[Fraction(0)] * 2 for _ in range(2)]
    for x in (0, 1):
        for (m, mp) in R:
            K[x][T((0, x, m, mp))[1]] += Fraction(1, len(R))
    return K


def mp_unknown_uniform(R):
    # the conjugate slot m' is unknown and uniform under the law
    return {mp for (_, mp) in R} == {0, 1} and all(
        sum(1 for (_, mp) in R if mp == v) * 2 == len(R) for v in (0, 1))


IDK = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
rows = []
for name, l in LAWS.items():
    for k in (0, 1):
        R = line(l, k)
        K = k_null(R)
        rows.append((name, k, mp_unknown_uniform(R), K == IDK, K))
        print("   l = %-5s k = %d: m' unknown & uniform %-5s K_null = %s" %
              (name, k, mp_unknown_uniform(R), [[str(a) for a in r] for r in K]))

# F1, known case: l = m' (m' known), k = 0 -> K_null = id
r = [x for x in rows if x[0] == "m'" and x[1] == 0][0]
check("1a SA-1(c) law l = m', k = 0 (m' known = 0): K_null = id", r[3] and not r[2])
r = [x for x in rows if x[0] == "m'" and x[1] == 1][0]
check("1b SA-1(c) law l = m', k = 1 (m' known = 1): K_null != id, a permutation (known displacement x -> x+1)",
      (not r[3]) and r[4] == [[0, 1], [1, 0]])
# F1, unknown case: every SA-1(c) law with m' unknown and uniform -> K_null != id (fully randomizing)
unk = [x for x in rows if x[2]]
check("1c every SA-1(c) law with m' unknown and uniform (l = m, m+m'; k = 0, 1): K_null != id",
      len(unk) == 4 and all(not x[3] for x in unk), len(unk))
check("1d ... and there K_null is the fully randomizing channel (every entry 1/2)",
      all(all(a == Fraction(1, 2) for rr in x[4] for a in rr) for x in unk))
check("1e the laws with m' unknown are exactly those with l != m'",
      {(x[0], x[1]) for x in unk} == {(n, k) for n in ("m", "m+m'") for k in (0, 1)})

# countercontrol: the K_null computation detects a nonzero kick and passes the identity map
def k_null_map(f, R):
    K = [[Fraction(0)] * 2 for _ in range(2)]
    for x in (0, 1):
        for (m, mp) in R:
            K[x][f((0, x, m, mp))[1]] += Fraction(1, len(R))
    return K


check("2a countercontrol: the identity map gives K_null = id under every law",
      all(k_null_map(lambda y: y, line(l, k)) == IDK for l in LAWS.values() for k in (0, 1)))
check("2b countercontrol: the unconditional flip x -> x+1 gives K_null != id under every law",
      all(k_null_map(lambda y: (y[0], 1 - y[1], y[2], y[3]), line(l, k)) != IDK
          for l in LAWS.values() for k in (0, 1)))

print("== %s" % ("all checks pass" if NF == 0 else "%d checks FAIL" % NF))
sys.exit(1 if NF else 0)
