# t5_axes.py -- T6 node C3: the flow law of t3 for every rotation axis of one token (not only the coordinate axes):
# does K(Z_F) admit any one-parameter rotation subgroup of one token?  Exact symbolic computation (sympy rationals).
# DECISION RULE (fixed before the first run, 19:15:27Z by date -u):
#  Symbols n1, n2, n3 (a unit axis: the ideal (n1²+n2²+n3²-1)), c, sn (cos t, sin t; no relation assumed).
#  R_n(c, sn) = c I + sn [n]x + (1 - c) n nᵀ (Rodrigues); Q_n = R_n(0, 1) (the quarter-turn).  Tables, actC, actT,
#  ipW, z_s, p_s exactly as in t3 (kernel transcription; p_s = table of the projector P_s).
#  A1 for τ in {C, T}, s in the four signs: ipW(R_n(c,sn)_τ z_s, (Q_n)_τ p_s) + sn/8 reduces to 0 modulo the sphere.
#  A2 y = (Q_n)_τ p_s lies in K(Z_F) for every unit n: (i) M(y)² - M(y) reduces to 0 and tr M(y) = 1 (a pure state);
#     (ii) for every t, ipW(y, z_t) is, after replacing its constant c0 by c0(n1²+n2²+n3²), a quadratic form in n
#     with a PSD coefficient matrix (exact principal minors), hence >= 0 on the sphere.
#  A3 control (Q3 kept, §A.21): M((Q_n)_τ p_s) reduced is a trace-one projector (A2(i)) -- the modeled action
#     preserves Q3; countercontrol: at n = e_x, the law of A1 must reproduce t3's coordinate law (value -sn/8), and
#     the half-turn value (c, sn) = (-1, 0) gives pairing 0 (no false witness at a symmetry of K(Z_F)).
#  VERDICT C3-ALL-AXES printed iff A1, A2 and A3 hold for both tokens and all four signs: then every member R_n(t)
#  with sin t ≠ 0, about every axis n, on either token, moves K(Z_F) out (witness y ∈ K, pairing -sin(t)/8 < 0
#  for sin t > 0; for sin t < 0 use the axis -n).  Else VERDICT NONE.
import sympy as sp

n1, n2, n3, c, sn = sp.symbols('n1 n2 n3 c sn')
SPH = n1**2 + n2**2 + n3**2 - 1
GENS = (n1, n2, n3, c, sn)
def red(e):
    e = sp.expand(e)
    if e == 0: return sp.Integer(0)
    return sp.reduced(e, [SPH], *GENS, order='lex')[1]
n = sp.Matrix([n1, n2, n3])
cross = sp.Matrix([[0, -n3, n2], [n3, 0, -n1], [-n2, n1, 0]])
def Rn(cc, ss): return cc * sp.eye(3) + ss * cross + (1 - cc) * n * n.T
def Hom(N): H = sp.eye(4); H[1:, 1:] = N; return H
def act(tok, N, w): return Hom(N) * w if tok == 'C' else w * Hom(N).T
def E(m, k): t = sp.zeros(4, 4); t[m, k] = 1; return t
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
def ps(s1, s2): return (E(0, 0) - s1 * E(1, 3) - s2 * E(2, 2) + s1 * s2 * E(3, 1)) / 4
def ip(a, b): return sp.expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
iu = sp.I
sg = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(sg[a], sg[b]) for b in range(4)] for a in range(4)]
def Mof(w): return sum((w[a, b] * SS[a][b] for a in range(4) for b in range(4)), sp.zeros(4, 4))
def psd_quadratic(e):
    e = red(e)
    poly = sp.Poly(e, n1, n2, n3)
    if any(sum(m) not in (0, 2) for m in poly.monoms()): return False
    c0 = poly.coeff_monomial(1)
    eh = sp.expand(e - c0 + c0 * (n1**2 + n2**2 + n3**2))
    Q = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 1 if i == j else 2) * sp.Poly(eh, n1, n2, n3).coeff_monomial(
        [n1, n2, n3][i] * [n1, n2, n3][j]))
    minors = [Q[i, i] for i in range(3)] + [Q.extract([i, j], [i, j]).det() for i in range(3) for j in range(i + 1, 3)] + [Q.det()]
    return all(sp.simplify(m) >= 0 for m in minors)
okA1, okA2, okA3 = True, True, True
for tok in 'CT':
    for s in SIGNS:
        z, p = zs(*s), ps(*s)
        y = act(tok, Rn(0, 1), p)
        okA1 &= red(ip(act(tok, Rn(c, sn), z), y) + sn / 8) == 0
        M = Mof(y)
        okA2 &= all(red(x) == 0 for x in (M * M - M)) and red(M.trace() - 1) == 0
        okA2 &= all(psd_quadratic(ip(y, zs(*t))) for t in SIGNS)
        # countercontrols at n = e_x and at the half-turn
        sub = {n1: 1, n2: 0, n3: 0}
        okA3 &= sp.expand(ip(act(tok, Rn(c, sn), z), y).subs(sub) + sn / 8) == 0
        okA3 &= red(ip(act(tok, Rn(-1, 0), z), y)) == 0
    print('token %s: A1 %s  A2 %s  A3 %s' % (tok, okA1, okA2, okA3))
ex = red(ip(act('C', Rn(c, sn), zs(1, 1)), act('C', Rn(0, 1), ps(1, 1))))
print('example (token C, s = (1,1)): reduced pairing = %s' % ex)
print('example pairings ipW(y, z_t), token C, s = (1,1): %s' % ', '.join(str(red(ip(act('C', Rn(0, 1), ps(1, 1)), zs(*t)))) for t in SIGNS))
if okA1 and okA2 and okA3:
    print('VERDICT C3-ALL-AXES: for every unit axis n and every t with sin t != 0, R_n(t) on either token moves K(Z_F) '
          'out; the witness Q_n p_s is a pure state in Q3 ∩ Z_F* and the pairing is -sin(t)/8 identically')
else:
    print('VERDICT NONE: A1 %s A2 %s A3 %s' % (okA1, okA2, okA3))
