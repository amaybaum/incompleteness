"""Step B: the second-order form B : Sym^2(ker DF) -> coker DF, its controls, and the residual census by direction."""
import pickle, time, sys
from lib36 import *
import numpy as np
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); K, LN = A['K'], A['LN']
def Q(v, w):
    """coker-side vector of -(1/2) D^2F(v,w) up to the positive factor 1/2:  sum_k c_k (v_ik - v_jk)(w_ik - w_jk), as (Re, Im) per pair"""
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0
        ci = i * N; cj = j * N
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (w[ci + k] - w[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
def Bclass(v, w):
    q = Q(v, w); return tuple(dot(l, q) for l in LN)
# adapted basis: gauge (31) < gauge+T (57) < ker (80)
def extend(basis, cands, target):
    cur = list(basis); r = rank(cur) if cur else 0; chosen = []
    for c in cands:
        if r >= target: break
        r2 = rank(cur + [c])
        if r2 > r: cur.append(c); chosen.append(c); r = r2
    assert r == target, (r, target)
    return chosen
Gb = extend([], GAUGE, 31); Tb = extend(Gb, TDITA, 57); Rb = extend(Gb + Tb, K, 80)
print('adapted basis: gauge %d, Diţă %d, residual %d (%.0fs)' % (len(Gb), len(Tb), len(Rb), time.time() - t0))
# controls
zero = tuple([0] * len(LN))
c1 = all(Bclass(g, v) == zero for g in Gb for v in Gb + Tb + Rb)
print('control: B(gauge, ker) == 0 in coker:', c1)
c2 = all(Bclass(t, u) == zero for t in Tb for u in Tb)
print('control: B(T, T) == 0 in coker (Diţă directions integrate):', c2)
# the form on Def = T + R
BT = {(i, j): Bclass(Tb[i], Rb[j]) for i in range(len(Tb)) for j in range(len(Rb))}
BR = {(i, j): Bclass(Rb[i], Rb[j]) for i in range(len(Rb)) for j in range(i, len(Rb))}
for i in range(len(Rb)):
    for j in range(i): BR[(i, j)] = BR[(j, i)]
print('B computed (%.0fs)' % (time.time() - t0))
rows_R = [list(BR[(i, j)]) for i in range(23) for j in range(i, 23)]
rows_T = [list(BT[(i, j)]) for i in range(26) for j in range(23)]
print('rank of B on Sym^2(R):', rank(rows_R, 64), ' rank of B on T x R:', rank(rows_T, 64), ' rank of B on Sym^2(Def):', rank(rows_R + rows_T, 64))
# per-direction census
fates = []
for i in range(23):
    self_ob = BR[(i, i)] != zero
    coupT = [j for j in range(26) if BT[(j, i)] != zero]
    coupR = [j for j in range(23) if j != i and BR[(i, j)] != zero]
    # solvability of B(r_i, r_i) + 2 sum_j x_j B(t_j, r_i) = 0
    cols = [list(BT[(j, i)]) for j in range(26)]
    rk_T = rank(cols, 64)
    rk_aug = rank(cols + [list(BR[(i, i)])], 64)
    solvable = (rk_aug == rk_T)
    fates.append((i, self_ob, solvable, len(coupT), rk_T, len(coupR)))
    print('r_%2d: self-obstruction %s | solvable with a Diţă correction: %s | couples to %2d Diţă directions (rank %2d) | couples to %2d other residual directions' % (i, 'yes' if self_ob else 'no ', 'yes' if solvable else 'no ', len(coupT), rk_T, len(coupR)))
print('summary: %d of 23 basis directions self-unobstructed; %d of 23 second-order extendable after a Diţă correction' % (sum(1 for f in fates if not f[1]), sum(1 for f in fates if f[2])))
# float control of the ranks (independent replay)
M = np.array(DF, dtype=float)
print('float control: rank DF', np.linalg.matrix_rank(M), '| rank gauge+T', np.linalg.matrix_rank(np.array(GAUGE + TDITA, float)), '| rank B on Sym^2(R)', np.linalg.matrix_rank(np.array(rows_R, float)) if rows_R else 0, '| rank on Sym^2(Def)', np.linalg.matrix_rank(np.array(rows_R + rows_T, float)))
pickle.dump({'Gb': Gb, 'Tb': Tb, 'Rb': Rb, 'BT': BT, 'BR': BR, 'fates': fates}, open('stepB.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
