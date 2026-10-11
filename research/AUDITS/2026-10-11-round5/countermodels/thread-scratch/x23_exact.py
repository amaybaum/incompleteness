# Scratch: exact (sympy) partners k0 and candidate rational tightness parameters (guidance; the record is c23_torus.py).
import sympy as sp
I = sp.I
def D(u, v): return sp.diag(1, u*v, u, v)
XB = sp.Matrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]])
def pyth(t):  # rational point on the unit circle
    t = sp.Rational(t); return (1 - t**2 + 2*I*t)/(1 + t**2)
def cj(x): return sp.conjugate(x)
def ip(a, b): return sp.simplify(sum(cj(a[i])*b[i] for i in range(4)))
def n2(a): return sp.simplify(ip(a, a))
def proj(v): return v*v.H/n2(v)
seeds = {"ii": sp.Matrix([2, 3*I, 1, 6]), "iii": sp.Matrix([3, 1, 2*I, 0]), "iv": sp.Matrix([3, 0, 2*I, 1])}
for name, h in seeds.items():
    al = cj(h[2])*h[3]; be = cj(h[0])*h[1]
    rows = []
    for t in ["0", "1/2", "2", "-1/3"]:
        u = pyth(t)
        den = cj(al) + u*cj(be)
        if sp.simplify(den) == 0: continue
        v = sp.simplify(-(be + u*al)/den)
        assert sp.simplify(v*cj(v)) == 1
        g = D(u, v)*XB
        gh = sp.simplify(g*h)
        assert ip(h, gh) == 0
        rows.append(gh.T)
    M = sp.Matrix.vstack(*rows)
    A = sp.Matrix.vstack(M.conjugate(), h.H)
    ns = A.nullspace()
    print(name, "rank", M.rank(), "nullity", len(ns))
    k = sp.simplify(ns[0])
    # scale k to Gaussian integers
    dens = [sp.fraction(sp.nsimplify(sp.re(x)))[1] for x in k] + [sp.fraction(sp.nsimplify(sp.im(x)))[1] for x in k]
    L = sp.ilcm(*dens); k = sp.simplify(k*L)
    print("  k0 =", list(k), " <h|k0> =", ip(h, k), " |h|^2 =", n2(h), " |k0|^2 =", n2(k))
