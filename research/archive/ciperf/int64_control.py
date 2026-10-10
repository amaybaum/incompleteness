"""Control for the Python-int normalization contract of the exact integer-echelon rank.
Feeds numpy int64 rows whose elimination products exceed 2**63; the unnormalized path (int64 arithmetic) must disagree
with a trusted exact calculation (Fraction elimination on Python ints), and the normalized path must agree."""
import sys, os, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util

def rank_frac(rows):
    M = [[Fr(int(x)) for x in r] for r in rows if any(int(x) for x in r)]; r = 0; ncol = len(M[0]) if M else 0
    for c in range(ncol):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / pv; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r

def echelon_rank(rows, normalize):
    from math import gcd
    basis = []
    for v in rows:
        v = [int(x) for x in v] if normalize else list(v)
        for c, r in basis:
            if v[c]:
                a, b = r[c], v[c]
                v = [a * x - b * y for x, y in zip(v, r)]
                if normalize:
                    g = 0
                    for x in v: g = gcd(g, x)
                    if g > 1: v = [x // g for x in v]
        if any(v):
            c = next(i for i, x in enumerate(v) if x); basis.append((c, v))
    return len(basis)

# int64 wraps modulo 2**64, a ring homomorphism: elimination stays correct unless a true nonzero value is a multiple of
# 2**64, which wraps to 0 and silently drops the rank. Here the second row eliminates to [0, 2**32 * 2**32] = [0, 2**64].
rows = np.array([[2 ** 32, 0], [2 ** 32, 2 ** 32]], dtype=np.int64)
trusted = rank_frac(rows)
with np.errstate(over='ignore'):
    import warnings; warnings.simplefilter('ignore')
    raw = echelon_rank(rows, normalize=False)
norm = echelon_rank(rows, normalize=True)
print('trusted (Fraction on Python ints):', trusted)
print('echelon on raw int64             :', raw)
print('echelon on normalized Python ints:', norm)
ok = (norm == trusted) and (raw != trusted)
print('int64_control:', 'OK -- normalization required and sufficient' if ok else 'FAILED')
sys.exit(0 if ok else 1)
