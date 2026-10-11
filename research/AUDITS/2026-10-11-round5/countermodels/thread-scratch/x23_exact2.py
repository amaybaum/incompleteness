# Scratch: exact search (Fractions) for tightness instances; guidance for c23_torus.py's fixed parameters.
from fractions import Fraction as Fr
import itertools, math
def gc(a, b=0): return (Fr(a), Fr(b))
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def sub(x, y): return (x[0]-y[0], x[1]-y[1])
def mul(x, y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def cj(x): return (x[0], -x[1])
def ab2(x): return x[0]*x[0]+x[1]*x[1]
def ip(a, b):
    s = gc(0)
    for p, q in zip(a, b): s = add(s, mul(cj(p), q))
    return s
def mv(M, v): return [sum_([mul(M[i][j], v[j]) for j in range(4)]) for i in range(4)]
def sum_(xs):
    s = gc(0)
    for x in xs: s = add(s, x)
    return s
def outer(v, w, s):  # s * v w^dagger
    return [[mul((s, Fr(0)), mul(v[i], cj(w[j]))) for j in range(4)] for i in range(4)]
def defect2(h, k, c):
    nh, nk = ip(h, h)[0], ip(k, k)[0]
    M = [[gc(1 if i == j else 0) for j in range(4)] for i in range(4)]
    Ph = outer(h, h, Fr(1)/nh); Pk = outer(k, k, Fr(1)/nk)
    return [[sub(sub(M[i][j], mul((c, Fr(0)), Ph[i][j])), mul((2-c, Fr(0)), Pk[i][j])) for j in range(4)] for i in range(4)]
def conjU(Ud, d):  # U d U^dagger with U = diag(Ud)
    return [[mul(mul(Ud[i], d[i][j]), cj(Ud[j])) for j in range(4)] for i in range(4)]
def qf(M, x): return ip(x, mv(M, x))[0]
def pyth(t):
    t = Fr(t); den = 1 + t*t
    return ((1 - t*t)/den, 2*t/den)
seeds = {"ii": ([gc(2), gc(0,3), gc(1), gc(6)], [gc(1), gc(0,-6), gc(-2), gc(3)]),
         "iii": ([gc(3), gc(1), gc(0,2), gc(0)], [gc(3), gc(1), gc(0,-5), gc(0)]),
         "iv": ([gc(3), gc(0), gc(0,2), gc(1)], [gc(-5), gc(0), gc(0,6), gc(3)])}
for name, (h, k) in seeds.items():
    assert ip(h, k) == gc(0)
    nh, nk = ip(h, h)[0], ip(k, k)[0]
    for c in (Fr(3, 2), Fr(101, 100)):
        d = defect2(h, k, c)
        found = None
        for teps in (Fr(1, 10), Fr(-1, 10), Fr(1, 20), Fr(-1, 20)):
            ue = pyth(teps)
            Ud = [gc(1), ue, ue, gc(1)]   # D(u_eps, 1) = diag(1, u, u, 1)
            dU = conjU(Ud, d)
            for tphi in [Fr(p, q) for q in (1, 2, 3, 4, 5, 10) for p in range(-3*q, 3*q+1)]:
                ph = pyth(tphi)
                ratio = math.sqrt(nh/nk)
                for r in (Fr(99, 100), Fr(995, 1000), Fr(9, 10)):
                    # b = r * ph * ratio, rationalized to 3 decimals
                    br = Fr(round(float(r*ph[0])*ratio*1000), 1000); bi = Fr(round(float(r*ph[1])*ratio*1000), 1000)
                    b = (br, bi)
                    if not ab2(b)*nk < nh: continue
                    u = [add(h[i], mul(b, k[i])) for i in range(4)]
                    if not qf(d, u) < 0: continue
                    # x = k - (<u|k>/<u|u>) u
                    uu = ip(u, u)[0]; uk = ip(u, k)
                    coef = (uk[0]/uu, uk[1]/uu)
                    x = [sub(k[i], mul(coef, u[i])) for i in range(4)]
                    val = qf(dU, x) / ip(x, x)[0]
                    if val < 0 and (found is None or val < found[0]):
                        pair = sum_([mul(d[i][j], dU[j][i]) for i in range(4) for j in range(4)])[0]
                        found = (val, teps, b, pair, qf(d, x)/ip(x, x)[0])
        print(name, "c", c, "->", None if found is None else (float(found[0]), str(found[1]), (str(found[2][0]), str(found[2][1])), float(found[3]), float(found[4])))
