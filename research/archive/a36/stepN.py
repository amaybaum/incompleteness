"""Step N: explicit 2x8 factorization of P_u for W_rs at u60, checked against the guessed nested form."""
import time
from lib36 import *
src = open('stepK.py', encoding='utf-8').read()
exec(src[src.index('def is_unitary(M, s)'):src.index("for label, H in (")])
def unit_n(n): return G(Fr(n * n - 1, n * n + 1), Fr(2 * n, n * n + 1))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
u = unit_n(60)
W = [((1 if (i % 4) == 1 else 0) + (1 if (j % 4) == 1 else 0)) if ((i // 4) % 2 == 0 and (j // 4) % 2 == 0) else 0 for i in range(16) for j in range(16)]
P = [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
ng, ors = dita_orientations(P, 2, 8)
for cp, rws, ok, flags in ors:
    print('column 2x8: blocks', cp, 'rows', rws, 'exact', ok)
ng, orsT = dita_orientations([list(c) for c in zip(*P)], 2, 8)
for cp, rws, ok, flags in orsT:
    print('row 2x8: blocks', cp, 'rows', rws, 'exact', ok)
# guessed nested form: outer X = F2 on (a_hi, c_lo); inner Y_{c_lo}[(a_lo,b),(c_hi,d)] = (-1)^{a_lo c_hi} z^{a_lo c_lo} F4(w)[b,d] * u^{[c_lo=0][a_lo=0]([b=1]+[d=1])}
Fw = F4(w); Fz = F4(z)
def guess(i, j):
    a, b, c, d = i // 4, i % 4, j // 4, j % 4
    ahi, alo, chi, clo = a // 2, a % 2, c // 2, c % 2
    X2 = G(-1) if (ahi == 1 and clo == 1) else ONE
    inner = (G(-1) if (alo == 1 and chi == 1) else ONE) * (z if (alo == 1 and clo == 1) else ONE) * Fw[b][d]
    tw = gpow(u, ((1 if b == 1 else 0) + (1 if d == 1 else 0)) if (clo == 0 and alo == 0) else 0)
    return X2 * inner * tw
print('guessed nested form equals P entrywise:', all(guess(i, j) == P[i][j] for i in range(16) for j in range(16)))
# F4(z)[a,c] = (-1)^{a_hi c_lo + a_lo c_hi} z^{a_lo c_lo} check
print('F4(z) sign/twist formula:', all(Fz[a][c] == (G(-1) if ((a // 2) * (c % 2) + (a % 2) * (c // 2)) % 2 == 1 else ONE) * (z if (a % 2 == 1 and c % 2 == 1) else ONE) for a in range(4) for c in range(4)))
# the inner 8x8 factors as 2x4 row-Diţă forms: Y_0 rows (a_lo,b) cols (c_hi,d): X' = F2 on (a_lo, c_hi), inner F4(w)-twisted for a_lo=0, F4(w) for a_lo=1
Y0 = [[(G(-1) if (alo == 1 and chi == 1) else ONE) * Fw[b][d] * gpow(u, ((1 if b == 1 else 0) + (1 if d == 1 else 0)) if alo == 0 else 0) for chi in range(2) for d in range(4)] for alo in range(2) for b in range(4)]
Y1 = [[(G(-1) if (alo == 1 and chi == 1) else ONE) * (z if alo == 1 else ONE) * Fw[b][d] for chi in range(2) for d in range(4)] for alo in range(2) for b in range(4)]
print('Y_0 (8x8) unitary with |entry|^2=1:', is_unitary(Y0, 8), '| Y_1 unitary:', is_unitary(Y1, 8))
print('done')
