#!/usr/bin/env python3
"""G3-W1 cross-check (not preregistered): exact rational ranks for the small polynomial classes.

Independent of g3w1_checks.py (imports nothing from it): its own rule, feature map and Gaussian
elimination over Fractions.  For each reduction and (m, D) it reports rank over Q of the equation
matrix and the excess n - rank - dim T, with dim T = number of monomials of degree <= D in
2(m - 1) variables (constant plus coboundaries).  Expected from g3w1_checks.py: excess 0 for ax and
fd, positive for bd.

Run:  python3 -I xcheck_rational.py      (a few seconds; exit 0 iff ax/fd excess 0 and bd excess > 0)
"""
import itertools
import random
import sys
from fractions import Fraction


def G(s):
    return (s + 1) // 3


def step(p, y, kind):
    L = len(y)
    out = []
    for k in range(L):
        a, b, c = y[(k - 1) % L], y[k], y[(k + 1) % L]
        s = {"ax": a + c + 4 * b, "fd": 2 * (a + b + c), "bd": 3 * (a + c)}[kind]
        out.append(G(s) - p[k])
    return list(y), out


def mons(nv, D):
    return [e for e in itertools.product(range(D + 1), repeat=nv) if sum(e) <= D]


def feats(p, y, m, M):
    L = len(y)
    f = {}
    for k in range(L):
        w = []
        for j in range(m):
            w += [p[(k + j) % L], y[(k + j) % L]]
        for e in M:
            v = 1
            for x, ei in zip(w, e):
                v *= x ** ei
            f[e] = f.get(e, 0) + v
    return f


def rank(rows):
    rows = [r[:] for r in rows]
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / rows[r][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def main():
    random.seed(5)
    ok = True
    for kind in ("bd", "ax", "fd"):
        for (m, D) in ((2, 2), (3, 2), (2, 3)):
            M = mons(2 * m, D)
            rows = []
            for _ in range(400):
                L = random.randint(1, 12)
                p = [random.randint(-9, 9) for _ in range(L)]
                y = [random.randint(-9, 9) for _ in range(L)]
                f0 = feats(p, y, m, M)
                p2, y2 = step(p, y, kind)
                f1 = feats(p2, y2, m, M)
                rows.append([Fraction(f1.get(e, 0) - f0.get(e, 0)) for e in M])
            n, rk, dT = len(M), rank(rows), len(mons(2 * (m - 1), D))
            ex = n - rk - dT
            ok &= (ex > 0) if kind == "bd" else (ex == 0)
            print(f"{kind} m={m} D={D}: n={n} rank_Q={rk} dimT={dT} excess={ex}")
    print("XCHECK", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
