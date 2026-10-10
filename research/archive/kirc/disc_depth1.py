"""Disc depth-1 no-go (exact where stated). Read-only.
Claim: no injective linear G on R^3 (x) R^3 acting as CNOT on the four corners maps the disc min tensor cone into the
max tensor cone. No local group, no involution, no G(C) = C: only G(min) <= max, injectivity and the frame.
 D1  (derivative at the corners) for Y_b = G(X (x) |b>): every product effect h vanishing on |0 b> or on |1, 1-b> has
     h(Y_b) = 0; this forces Y_b in X (x) R^3 (the kernel of u*, z* on the control side is span X).
 D2  (theta = pi/2) Y_b = X (x) w with w = (w0, wx, wz): the family of product-effect values contains, for
     a = (sin p, cos p), c = (+-sin p, -s cos p), the inequality |w0 +- wx sin p - s wz cos p| <= |sin p|, forcing
     w0 = wz = 0.
 D3  so G(X(x)|0>), G(X(x)|1>) are both multiples of X(x)X: G is singular on span{X(x)|0>, X(x)|1>}.
Checks: D2's value identity symbolically; controls: complex CNOT on the Bloch ball has Y_b = (XX - s YY)/2 in
span{X, Y} (x) R^4, independent (d = 3 escapes at D1); the measure-and-flip map has Y_b = 0 (singular, as D3 says);
a constructive witness routine finds an exact violated (state, effect) pair for random invertible G in the weak family."""
import sympy as sp, numpy as np
OUT = []
def rep(n, ok, det=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n + ('  ' + det if det else ''))
kron = sp.kronecker_product
u = sp.Matrix([1, 0, 0]); X = sp.Matrix([0, 1, 0]); Z = sp.Matrix([0, 0, 1]); k = [u + Z, u - Z]
ax, az, cx, cz, w0, wx, wz, p = sp.symbols('ax az cx cz w0 wx wz p', real=True)
for b in (0, 1):
    s = (-1) ** b
    base = (kron(k[0], k[b]) + kron(k[1], k[1 - b])) / 2          # G(u (x) |b>) by the frame
    f = sp.Matrix([1, ax, az]); g = sp.Matrix([1, cx, cz]); w = sp.Matrix([w0, wx, wz])
    val = (kron(f, g).T * (base + kron(X, w)))[0]
    rep('D2 b=%d value identity (f(x)g)(G(u(x)|b>) + X(x)w) = 1 + s az cz + ax (g.w)' % b,
        sp.expand(val - (1 + s * az * cz + ax * (g.T * w)[0])) == 0)
    for sg in (1, -1):
        sub = {ax: sp.sin(p), az: sp.cos(p), cx: sg * sp.sin(p), cz: -s * sp.cos(p)}
        rhs = sp.simplify((1 + s * az * cz).subs(sub))
        rep('D2 b=%d, c_x sign %+d: the effect choice makes the constant part sin(p)^2' % (b, sg), sp.simplify(rhs - sp.sin(p) ** 2) == 0)
# D1: kernel of the control-side functionals u*, z* (from <0| and <1|) is span X
rep('D1 ker(<0|) cap ker(<1|) on the disc is span{X}', sp.Matrix([[1, 0, 1], [1, 0, -1]]).nullspace() == [X])
rep('D1 control (ball): ker(<0|) cap ker(<1|) is 2-dimensional (span{X, Y})',
    len(sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1]]).nullspace()) == 2)
# control: complex CNOT on the Bloch ball
from disc_cnot_search import complex_cnot
GC = complex_cnot(); e = np.eye(4)
Yb = [GC @ np.kron(e[1], e[0] + (-1) ** b * e[3]) for b in (0, 1)]
XX = np.kron(e[1], e[1]); YY = np.kron(e[2], e[2])
rep('C complex CNOT: Y_b = XX - (-1)^b YY (in span{X,Y}(x)R^4) and the two are independent',
    np.allclose(Yb[0], XX - YY) and np.allclose(Yb[1], XX + YY) and np.linalg.matrix_rank(np.array(Yb)) == 2)
# control: measure-and-flip
kk = [np.array([1, 0, 1.]), np.array([1, 0, -1.])]; ee = [kk[0] / 2, kk[1] / 2]; NOT = np.diag([1., -1, -1])
M = sum(np.kron(np.outer(kk[a], ee[a]), np.linalg.matrix_power(NOT, a)) for a in (0, 1))
Xv = np.array([0, 1., 0])
rep('C measure-and-flip: Y_b = 0 for both b (singular, consistent with D3)',
    all(np.allclose(M @ np.kron(Xv, kk[b]), 0) for b in (0, 1)))
# constructive witnesses on random invertible weak-family G
from disc_cnot_setup import setup, affine_space
env = setup(3, 'rot'); g0, B = affine_space(env, False); rng = np.random.default_rng(0)
def witness(G):
    for th in [1e-3, -1e-3, np.pi - 1e-3, -(np.pi - 1e-3), np.pi / 2, -np.pi / 2]:
        for b in (0, 1):
            st = np.kron(np.array([1, np.sin(th), np.cos(th)]), kk[b]); v = G @ st
            for phi in np.linspace(0, 2 * np.pi, 721):
                for psi in np.linspace(0, 2 * np.pi, 73):
                    h = np.kron([1, np.sin(phi), np.cos(phi)], [1, np.sin(psi), np.cos(psi)])
                    if h @ v < -1e-9: return (th, b, phi, psi, h @ v)
    return None
found = 0; N = 40
for _ in range(N):
    G = (g0 + rng.normal(size=len(B)) @ B).reshape(9, 9)
    if abs(np.linalg.det(G)) > 1e-6 and witness(G) is not None: found += 1
rep('witness routine: a violated (product state, product effect) pair found for %d/%d random invertible G' % (found, N), found == N)
print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
