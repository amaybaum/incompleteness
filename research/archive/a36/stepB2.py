"""Step B2: per-hull integrability controls (exact), and the four hull orientations through the point (fixed and swapped pairing)."""
import pickle, time
from lib36 import *
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); K, LN = A['K'], A['LN']
def Q(v, w):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * N; cj = j * N
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (w[ci + k] - w[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
T = TDITA
Xc = [T[0]]; Yc = T[1:5]; Ya = T[5:9]; Dc = T[9:25]; Ea = T[25:41]
Tc = Xc + Yc + Dc; Tr = Xc + Ya + Ea
print('rank mod gauge: T_c', rank(GAUGE + Tc) - 31, 'T_r', rank(GAUGE + Tr) - 31, 'T_c+T_r', rank(GAUGE + Tc + Tr) - 31, 'T_c ∩ T_r (mod gauge)', (rank(GAUGE + Tc) - 31) + (rank(GAUGE + Tr) - 31) - (rank(GAUGE + Tc + Tr) - 31))
z240 = [0] * 240
print('control: D²F(T_c, T_c) == 0 exactly:', all(Q(u, v) == z240 for u in Tc for v in Tc))
print('control: D²F(T_r, T_r) == 0 exactly:', all(Q(u, v) == z240 for u in Tr for v in Tr))
print('control: D²F(gauge, gauge) == 0 in coker:', all(all(dot(l, Q(g, h)) == 0 for l in LN) for g in GAUGE for h in GAUGE))
cross = [Q(u, v) for u in Tc for v in Tr]
print('cross terms D²F(T_c, T_r): nonzero exactly', sum(1 for q in cross if q != z240), 'of', len(cross), '| nonzero in coker', sum(1 for q in cross if any(dot(l, q) != 0 for l in LN)))
# swapped pairing: SW on theta
SW = [0] * 256
for i in range(16):
    for j in range(16):
        a, b, c, d = i // 4, i % 4, j // 4, j % 4
        SW[i * 16 + j] = (4 * b + a) * 16 + (4 * d + c)
def swap_vec(v):
    out = [0] * 256
    for m, x in enumerate(v): out[SW[m]] = x
    return out
Tcs = [swap_vec(v) for v in Tc]; Trs = [swap_vec(v) for v in Tr]
print('control: DF . T_c^sw == 0:', all(dot(r, t) == 0 for r in DF for t in Tcs), ' DF . T_r^sw == 0:', all(dot(r, t) == 0 for r in DF for t in Trs))
print('control: D²F(T_c^sw, T_c^sw) == 0 exactly:', all(Q(u, v) == z240 for u in Tcs for v in Tcs), ' D²F(T_r^sw, T_r^sw) == 0 exactly:', all(Q(u, v) == z240 for u in Trs for v in Trs))
for name, S in (('T_c^sw', Tcs), ('T_r^sw', Trs), ('T_c+T_r+T_c^sw', Tc + Tr + Tcs), ('T_c+T_r+T_r^sw', Tc + Tr + Trs), ('all four', Tc + Tr + Tcs + Trs)):
    print('rank mod gauge of %s: %d' % (name, rank(GAUGE + S) - 31))
print('residual after the four orientations: %d' % (49 - (rank(GAUGE + Tc + Tr + Tcs + Trs) - 31)))
pickle.dump({'Tc': Tc, 'Tr': Tr, 'Tcs': Tcs, 'Trs': Trs}, open('stepB2.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
