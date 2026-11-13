"""MIXED-PATH-1 Stage 2: separate exact verifier of locality certificates (STAGE2-PREREG.md section 3).

A table is N[a][b][x][y] (integer counts, a, b in {0,1}) with total H per (a,b).  Fractions only.
"""
import itertools
from fractions import Fraction


def verify_certificate(N, H, cert):
    nA = len(N[0][0])
    nB = len(N[0][0][0])
    kind = cert.get("type")
    if kind == "LOCAL":
        acc = [[[[Fraction(0)] * nB for _ in range(nA)] for _ in range(2)] for _ in range(2)]
        for x0, x1, y0, y1, w in cert["weights"]:
            w = Fraction(w)
            if w < 0:
                return False
            xs = (x0, x1)
            ys = (y0, y1)
            for a in (0, 1):
                for b in (0, 1):
                    if not (0 <= xs[a] < nA and 0 <= ys[b] < nB):
                        return False
                    acc[a][b][xs[a]][ys[b]] += w
        for a in (0, 1):
            for b in (0, 1):
                for x in range(nA):
                    for y in range(nB):
                        if acc[a][b][x][y] != Fraction(int(N[a][b][x][y]), H):
                            return False
        return True
    if kind == "NONLOCAL":
        beta = [[[[Fraction(v) for v in row] for row in cert["beta"][a][b]] for b in (0, 1)] for a in (0, 1)]
        lhs = Fraction(0)
        for a in (0, 1):
            for b in (0, 1):
                if len(beta[a][b]) != nA:
                    return False
                for x in range(nA):
                    if len(beta[a][b][x]) != nB:
                        return False
                    for y in range(nB):
                        lhs += beta[a][b][x][y] * Fraction(int(N[a][b][x][y]), H)
        best = None
        for x0, x1 in itertools.product(range(nA), repeat=2):
            for y0, y1 in itertools.product(range(nB), repeat=2):
                val = beta[0][0][x0][y0] + beta[0][1][x0][y1] + beta[1][0][x1][y0] + beta[1][1][x1][y1]
                if best is None or val > best:
                    best = val
        return lhs > best
    return False
