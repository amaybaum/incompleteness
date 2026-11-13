# REVIEW CONTROL (r3), not evidence: PC-NONSTAB planted laws -- images, ball/octahedron, NE-1 membership.
# Static algebra on the planted laws and their image under rule 0's free swap (an affine rule; no test rule).
import itertools
from fractions import Fraction as Fr
P = list(itertools.product((0,1), repeat=4))  # (z1,x1,z2,x2) = (u0,v0,u1,v1)
F = {'x': (0,1,0,0), 'y': (1,1,1,1), 'z': (1,0,0,0)}
ev = lambda c, w: sum(a*b for a, b in zip(c, w)) % 2
R = lambda mu: tuple(sum(p*(1-2*ev(F[a], w)) for w, p in mu.items()) for a in 'xyz')
def omega(f, g): return (f[0]*g[1]+f[1]*g[0]+f[2]*g[3]+f[3]*g[2]) % 2
def native_N_sup(mu):
    supp = [w for w in P if mu.get(w, 0)]
    if any(mu[w] != Fr(1, len(supp)) for w in supp): return False, "not uniform on support"
    D = [c for c in P if any(c) and len({ev(c, w) for w in supp}) == 1]
    if any(omega(a, b) for a in D for b in D): return False, "determined set not isotropic"
    return True, "uniform coset, isotropic"
b = lambda x, p: p if x else 1 - p
lawA = {w: b(w[0], Fr(1,5)) * b(w[1], Fr(1,5)) * Fr(1,4) for w in P}
supp = [w for w in P if w[1] == 0 and ev(F['y'], w) == 0]
lawB = {w: Fr(1, len(supp)) for w in supp}
swap = lambda mu: {(w[1], w[0], w[3], w[2]): p for w, p in mu.items()}  # rule 0: u_i' = v_i, v_i' = u_i
for name, mu in (("A Bern(1/5)", lawA), ("B {x1=0,f_y=0}", lawB)):
    for k in (0, 1):
        m = mu if k == 0 else swap(mu)
        r = R(m); l1 = sum(abs(x) for x in r); n2 = sum(x*x for x in r)
        print(name, "k", k, "r", tuple(str(x) for x in r), "l1", l1, "|r|^2", n2, "NE-1:", native_N_sup(m))
