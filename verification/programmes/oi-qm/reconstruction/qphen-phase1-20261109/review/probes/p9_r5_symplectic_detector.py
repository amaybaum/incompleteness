#!/usr/bin/env python3
"""p9_r5_symplectic_detector.py -- writer's exact check for SHARED Q4-D3 and Q4-P19 (QPHEN Phase 1 r5).

Generic objects only: affine maps of F_2^4 with coordinates (c, x, m, m'), symplectic form pairing (c, x) and (m, m').
No OI mechanism is computed. Imports no earlier probe. Exhaustive over all 4x4 matrices over F_2 and all translations.

A map T(y) = M y + b "interacts only when the cell is occupied" iff T is the identity on the branch c = 0.
It "records occupation" iff some point with c = 1 has a meter slot (m or m') changed by T.
"""
import itertools
import sys

C, X, MM, MP = 0, 1, 2, 3          # coordinate indices: c, x, m, m'
N = 4
POINTS = [tuple(p) for p in itertools.product((0, 1), repeat=N)]

fails = 0


def check(label, ok):
    global fails
    print(('PASS ' if ok else 'FAIL ') + label)
    if not ok:
        fails += 1


def apply(M, b, y):
    return tuple((sum(M[i][j] * y[j] for j in range(N)) + b[i]) % 2 for i in range(N))


def omega(u, v):
    # symplectic form pairing (c, x) and (m, m')
    return (u[C] * v[X] + u[X] * v[C] + u[MM] * v[MP] + u[MP] * v[MM]) % 2


def col(M, j):
    return tuple(M[i][j] for i in range(N))


def is_symplectic(M):
    E = [tuple(1 if k == j else 0 for k in range(N)) for j in range(N)]
    return all(omega(col(M, i), col(M, j)) == omega(E[i], E[j]) for i in range(N) for j in range(N))


def is_bijective(M):
    zero = (0,) * N
    return len({apply(M, zero, y) for y in POINTS}) == 2 ** N


def identity_on_empty(M, b):
    return all(apply(M, b, y) == y for y in POINTS if y[C] == 0)


def records_occupation(M, b):
    return any(apply(M, b, y)[MM:] != y[MM:] for y in POINTS if y[C] == 1)


TRANSLATIONS = POINTS
mats = []
for bits in itertools.product((0, 1), repeat=N * N):
    M = [list(bits[N * i:N * i + N]) for i in range(N)]
    if is_bijective(M):
        mats.append(M)
symp = [M for M in mats if is_symplectic(M)]

n_aff = len(mats) * len(TRANSLATIONS)
n_aff_sym = len(symp) * len(TRANSLATIONS)
both_aff = [(M, b) for M in mats for b in TRANSLATIONS if identity_on_empty(M, b) and records_occupation(M, b)]
both_sym = [(M, b) for M in symp for b in TRANSLATIONS if identity_on_empty(M, b) and records_occupation(M, b)]
idle_sym = [(M, b) for M in symp for b in TRANSLATIONS if identity_on_empty(M, b)]

print('     |GL(4,F2)| =', len(mats), '; |Sp(4,F2)| =', len(symp))
print('     affine bijections:', n_aff, '; affine-symplectic:', n_aff_sym)
print('     identity on c=0 and records occupation: affine', len(both_aff), '; affine-symplectic', len(both_sym))
print('     affine-symplectic maps that are the identity on c=0:', len(idle_sym))

check('|GL(4,F2)| = 20160', len(mats) == 20160)
check('|Sp(4,F2)| = 720', len(symp) == 720)
check('affine-symplectic maps = 720 x 16 = 11520', n_aff_sym == 720 * 16 == 11520)
check('affine maps (not necessarily symplectic) that are identity on c=0 and record occupation: 6', len(both_aff) == 6)
check('affine-symplectic maps that are identity on c=0 and record occupation: 0', len(both_sym) == 0)

# The argument: identity on {c = 0} forces b = 0 and M = I + d e_c^T with d_c = 0; symplectic forces d in span(e_x).
lin_idle = [(M, b) for (M, b) in idle_sym]
check('identity on c=0 forces b = 0 (affine-symplectic)', all(b == (0,) * N for _, b in lin_idle))
ds = sorted({tuple((col(M, C)[i] - (1 if i == C else 0)) % 2 for i in range(N)) for M, _ in lin_idle})
check('symplectic and identity on c=0: d in span(e_x), i.e. d in {0, e_x}', ds == [(0, 0, 0, 0), (0, 1, 0, 0)])
ds_aff = sorted({tuple((col(M, C)[i] - (1 if i == C else 0)) % 2 for i in range(N)) for M, _ in both_aff})
check('the 6 affine maps are M = I + d e_c^T, d_c = 0, with a meter component in d',
      len(ds_aff) == 6 and all(d[C] == 0 and (d[MM] or d[MP]) for d in ds_aff))

# The two couplings named in R4.9 and Q4-D3.
I4 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
copy = [r[:] for r in I4]
copy[MM][C] = 1                      # m <- m + c
recip = [r[:] for r in copy]
recip[X][MP] = 1                     # x <- x + m'
zero = (0,) * N
check('copy coupling m <- m + c is a linear bijection', is_bijective(copy))
check('copy coupling is not symplectic for (c, x), (m, m\')', not is_symplectic(copy))
check('copy coupling is identity on c=0 and records occupation', identity_on_empty(copy, zero) and records_occupation(copy, zero))
check('reciprocal coupling (copy and x <- x + m\') is symplectic', is_symplectic(recip))
check('reciprocal coupling records occupation and is not the identity on c=0',
      records_occupation(recip, zero) and not identity_on_empty(recip, zero))

print('ALL PASS' if fails == 0 else '%d FAIL' % fails)
sys.exit(1 if fails else 0)
