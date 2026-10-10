"""A39 pre-freeze gate (read-only, from certified D = 6e8ce41d): is SIG o u1^A u2^B u3^C unitary for all units u1, u2, u3?
Exactly: for every ordered row pair (r, s) and every joint difference triple t = (dA, dB, dC), the pair sum
  S(r, s, t) = sum_{j : (A_rj - A_sj, B_rj - B_sj, C_rj - C_sj) = t} SIG_rj conj(SIG_sj)
vanishes, for t != 0 and (with the diagonal) the t = 0 sums give 16 delta_rs. Checked in exact Gaussian rationals, and again
monomial by monomial in z, w (symbolic units), and against the landed A38 probe's own objects."""
import sys, time, itertools
from fractions import Fraction as Fr
src = open('a39/probe38_landed.py', encoding='utf-8').read()
cut = src.index("print('== 1. realizability")
NS = {'__name__': 'probe38head'}
exec(compile(src[:cut], 'probe38head', 'exec'), NS)
G, ZERO, ONE, SIG, SIGE = NS['G'], NS['ZERO'], NS['ONE'], NS['SIG'], NS['SIGE']
EA, EB, EC, EE = NS['EA'], NS['EB'], NS['EC'], NS['EE']
t0 = time.time()
A = [[EA(i, j) for j in range(16)] for i in range(16)]
B = [[EB(i, j) for j in range(16)] for i in range(16)]
C = [[EC(i, j) for j in range(16)] for i in range(16)]
assert EE == [[A[i][j] + B[i][j] + C[i][j] for j in range(16)] for i in range(16)]
def gate(mats, symbolic=False):
    """return (number of joint level sets checked, list of failures) for the multivariate unitarity identity"""
    n = 0; bad = []
    for r in range(16):
        for s in range(16):
            groups = {}
            for j in range(16):
                t = tuple(M[r][j] - M[s][j] for M in mats)
                groups.setdefault(t, []).append(j)
            for t, js in groups.items():
                n += 1
                if symbolic:
                    cnt = {}
                    for j in js:
                        a1, q1, r1 = SIGE[r][j]; a2, q2, r2 = SIGE[s][j]
                        assert (a1 - a2) % 2 == 0
                        key = (q1 - q2, r1 - r2); cnt[key] = cnt.get(key, 0) + (1 if (a1 - a2) % 4 == 0 else -1)
                    want = {(0, 0): 16} if (r == s and all(x == 0 for x in t)) else {}
                    got = {k: v for k, v in cnt.items() if v}
                    if got != want: bad.append((r, s, t, got))
                else:
                    tot = ZERO
                    for j in js: tot = tot + SIG[r][j] * SIG[s][j].conj()
                    want = G(16) if (r == s and all(x == 0 for x in t)) else ZERO
                    if tot != want: bad.append((r, s, t, (tot.a, tot.b)))
    return n, bad
print('== the joint gate for (A, B, C) ==')
n, bad = gate([A, B, C]); print('  exact Gaussian-rational: %d joint level sets, %d failures' % (n, len(bad)))
ns, bads = gate([A, B, C], symbolic=True); print('  symbolic z, w (monomial balance): %d joint level sets, %d failures' % (ns, len(bads)))
# the joint triples that occur
trip = sorted(set(tuple(M[r][j] - M[s][j] for M in (A, B, C)) for r in range(16) for s in range(16) for j in range(16)))
print('  joint difference triples occurring:', len(trip), trip)
# controls: the collapse to one variable reproduces A38; single pieces and pairs are straight in their own variables
print('== controls ==')
for nm, mats in (('E = A+B+C (one variable, A38)', [EE]), ('A', [A]), ('B', [B]), ('C', [C]), ('(A, B)', [A, B]), ('(A, C)', [A, C]), ('(B, C)', [B, C]),
                 ('(A+B, C)', [[[A[i][j] + B[i][j] for j in range(16)] for i in range(16)], C])):
    n1, b1 = gate(mats); print('  %-32s level sets %4d, failures %d' % (nm, n1, len(b1)))
# a countercontrol: a perturbed third piece must fail
Cp = [r[:] for r in C]; Cp[1][2] = 1 - Cp[1][2]
n2, b2 = gate([A, B, Cp]); print('  countercontrol (A, B, C with one entry of C flipped): failures %d (must be > 0)' % len(b2))
# numeric spot check: H(u1, u2, u3) unitary at three independent Gaussian-rational units
u1, u2, u3 = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17))
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
H = [[SIG[i][j] * gp(u1, A[i][j]) * gp(u2, B[i][j]) * gp(u3, C[i][j]) for j in range(16)] for i in range(16)]
print('  H(u5, w, (8+15i)/17) unitary exactly:', NS['is_unitary16'](H))
print('%.1fs' % (time.time() - t0))
