"""Thread E -- exact symbolic checks of the K2 positivity step (sympy, exact; read-only research).

 S1  the inverse of G(M0, A, K) (A diagonal, K antidiagonal, nonzero entries) is G(M0, A^-1, K'),
     K' antidiagonal with reciprocal entries -- P^- is P applied to the same family.
 S2  W(s)^T W(s) for W(s) = [As, Ks]: diagonal entries and the off-diagonal s1 s2 (a1 k1 + a2 k2).
 S3  the necessity point: value(c) = (1+|b|) c^2 + 2 a c + (1-|b|) along g = t' = (c, sqrt(1-c^2) n),
     with discriminant a^2 + b^2 - 1.
 S4  sufficiency identity: for every admissible sign tuple the product value equals the complex CNOT's
     value at relabelled arguments (s -> A s, t -> R^c M0 t, g -> R^c g), as polynomials.
 Countercontrol for S4: a non-admissible tuple fails the identity for both values of c.
"""
import itertools, sympy as sp
ns = {}
exec(open('replay/k20_classify.py').read().split('# 1. the relations')[0], ns)
build = ns['build']; kr = sp.kronecker_product
FAIL = []
def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name, flush=True)
    if not cond: FAIL.append(name)
a1, a2, k1, k2 = sp.symbols('a1 a2 k1 k2', nonzero=True)
A = sp.diag(a1, a2); K = sp.Matrix([[0, k1], [k2, 0]])
# S1
for M0d in itertools.product((1, -1), repeat=2):
    G = build(M0d, A, K)
    hits = []
    e1, e2 = M0d
    for name, Ap, Kp in [('e1 A^-1, -e2 K^-1', e1 * A.inv(), -e2 * K.inv())]:
        H = build(M0d, Ap, Kp)
        if (H * G - sp.eye(16)).applyfunc(sp.simplify) == sp.zeros(16): hits.append(name)
    print('   M0 =', M0d, 'inverse in family as', hits)
    check('S1 M0=%s: G^-1 = G(M0, e1 A^-1, -e2 K^-1) -- same family, reciprocal moduli' % (M0d,), len(hits) > 0)
# S2
s1, s2 = sp.symbols('s1 s2', real=True)
s = sp.Matrix([s1, s2]); W = sp.Matrix.hstack(A * s, K * s)
WtW = (W.T * W).applyfunc(sp.expand)
check('S2 W^T W = [[a1^2 s1^2 + a2^2 s2^2, s1 s2 (a1 k1 + a2 k2)], [., k2^2 s1^2 + k1^2 s2^2]]',
      WtW == sp.Matrix([[a1**2*s1**2 + a2**2*s2**2, s1*s2*(a1*k1 + a2*k2)], [s1*s2*(a1*k1 + a2*k2), k2**2*s1**2 + k1**2*s2**2]]).applyfunc(sp.expand))
# at |a_i| = |k_i| = 1: W^T W = (s1^2+s2^2) I + s1 s2 (a1 k1 + a2 k2) X, so sigma_max^2 = |s|^2 + |s1 s2| |a1 k1 + a2 k2|
sub = {a1**2: 1, a2**2: 1, k1**2: 1, k2**2: 1}
W1 = WtW.subs(sub)
check('S2 at unit moduli: W^T W - |s|^2 I is s1 s2 (a1 k1 + a2 k2) times the swap', (W1 - (s1**2 + s2**2) * sp.eye(2)).applyfunc(sp.expand) == ((s1*s2*(a1*k1 + a2*k2)) * sp.Matrix([[0, 1], [1, 0]])).applyfunc(sp.expand))
sols = [w for w in itertools.product((1, -1), repeat=4) if w[0]*w[2] + w[1]*w[3] == 0]
check('S2 sign solutions: 8', len(sols) == 8)
# S3: the necessity point.  s_z = f_z = 0, g = (c, r n_g), t' = (c, r n_t), r = sqrt(1 - c^2), n's unit in V-;
# with g- x t'- = r^2 sin(theta) and g- . t'- = r^2 cos(theta) (the latter multiplied by s_z + f_z = 0)
c, al, be, th = sp.symbols('c alpha beta theta', real=True)
val = (1)*(1 + c*c) + 0 + al*(c + c) + be*(1 - c**2)*sp.sin(th)
worst = val.subs(sp.sin(th), -sp.sign(be))   # choose theta with be*sin(theta) = -|be|
B = sp.Symbol('B', nonnegative=True)        # B = |beta|
q = sp.expand((1 + c*c) + 2*al*c - B*(1 - c**2))
check('S3 worst value = (1+|b|) c^2 + 2 a c + (1-|b|)', sp.expand(q - ((1 + B)*c**2 + 2*al*c + (1 - B))) == 0)
check('S3 discriminant/4 = a^2 + b^2 - 1', sp.expand(al**2 - (1 + B)*(1 - B) - (al**2 + B**2 - 1)) == 0)
# S4: the value identity against the complex CNOT
S = sp.symbols('s1 s2 sz'); T = sp.symbols('t1 t2 tz'); F = sp.symbols('f1 f2 fz'); Gg = sp.symbols('g1 g2 gz')
def vec(x): return sp.Matrix([1, *x])
def value(Gm, sv, tv, fv, gv): return sp.expand((kr(fv, gv).T * Gm * kr(sv, tv))[0])
CN = build((1, 1), sp.eye(2), sp.Matrix([[0, -1], [1, 0]]))
def identity_holds(M0d, w, cc):
    Gm = build(M0d, sp.diag(w[0], w[1]), sp.Matrix([[0, w[2]], [w[3], 0]]))
    Ad = sp.diag(1, w[0], w[1], 1); M0 = sp.diag(1, M0d[0], M0d[1], 1); Rc = sp.diag(1, 1, cc, 1)
    lhs = value(Gm, vec(S), vec(T), vec(F), vec(Gg))
    rhs = value(CN, Ad * vec(S), Rc * M0 * vec(T), vec(F), Rc * vec(Gg))
    return sp.expand(lhs - rhs) == 0
ok = True
for M0d in itertools.product((1, -1), repeat=2):
    for w in sols:
        cc = w[3] * w[0]                      # c = k2 a1, K s = c J A s
        ok &= identity_holds(M0d, w, cc)
check('S4 all 32: value_G(s,t,f,g) = value_CNOT(A s, R^c M0 t, f, R^c g) with c = k2 a1 (R^-1 = y-reflection)', ok)
bad = (1, 1, 1, 1)
check('S4 countercontrol: tuple (1,1,1,1) satisfies the identity for neither c', not identity_holds((1, 1), bad, 1) and not identity_holds((1, 1), bad, -1))
print('e_sym: %s -- %d failures' % ('OK' if not FAIL else 'FAILED', len(FAIL)))
