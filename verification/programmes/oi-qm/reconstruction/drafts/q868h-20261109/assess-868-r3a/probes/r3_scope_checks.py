"""ASSESS-868 r3: exact generic checks (WIP / UNVERIFIED).

Generic 2x2 / 4x4 matrices and generic tables only. No OI update rule, encoding, record law or
mechanism is simulated or enumerated. Two kernel definitions are re-typed by hand as generic matrices:
the gate flow `unit g t = 1 + (exp(i pi t) - 1) (1 - g)/2` (SecondOrderCircuit.lean:356; gateFlow,
LiftAudit.lean:47) on Fin 2 with g = X, and the passive flow `exp(-i t H)` (ReachabilitySeam.lean:95)
of `transition a b` (LieRankSource.lean:199), the driven transition of PhaseFreeRichness
(MinimalRepertoire.lean:423). Imports no earlier probe. Run: python3 -I r3_scope_checks.py

Table convention: w[k][l] = <s_k (x) s_l>, s = (I, X, Y, Z); product value ahat^T w bhat with ahat = (1, a).
"Real" means real in the configuration basis.

N7/V1  W1  the dual cone of the six Pauli sharp effects equals the cube cone {|v_i| <= t}: both inclusions,
           by an explicit nonnegative decomposition over the eight cube vertices; control outside.
       W2  the octahedron cone lies in the cube cone; the cube vertex lies outside the octahedron and Lor.
N7/V3  W3  T = (I + XX + ZZ)/4: herald (1, a1, 0, a3); 1 - a1^2 - a3^2 = (1 - |a|^2) + a2^2; full-ball
           product value certificate 2(1 + a1 b1 + a3 b3) = (1-a1^2-a3^2) + (1-b1^2-b3^2) + (a1+b1)^2 + (a3+b3)^2;
           eigenvalue -1/4 on the singlet.
       W4  swap: <u (x) v| SW |u (x) v> = |<u|v>|^2 with real and imaginary parts explicit; eigenvalue -1 on
           the singlet.
N3     W5  operator identity <a (x) b| X |a (x) b> = <b| sigma_a |b>, sigma_a = (<a| (x) I) X (|a> (x) I), for a
           generic complex 4x4 X (both directions of "block-positive iff every conditional is PSD"); and the
           product value is invariant under transposing the table and exchanging the wings.
B1     W6  operations that keep real states real keep <Y> = 0: a generic real Kraus pair and real Lueders
           projectors on a generic real symmetric state; y+ is not real.
       W7  the kernel gate flow on Fin 2: unit(X, t) is unitary, non-real and non-monomial at t = 1/2, fixes
           the all-ones vector, commutes with X, and takes z+ to (0, -sin pi t, cos pi t): a non-real operation
           with no separate phase gate (the flow is itself complex). Controls: the quarter phase moves the all-ones ray; real H keeps <Y> = 0.
       W8  the driven transition exp(-i t X_ab) on four states (two two-state wings, index 2*first + second),
           no separate phase gate (the drive itself is complex): one drive at t = pi/4 takes |10> to y+ (x) z+; two drives and one exchange take |10>
           to x+ (x) z+. Controls: closed form equals the matrix exponential; the drive is unitary, non-real,
           non-monomial and moves the all-ones ray at t = pi/4.
B1     W10 the drive carries a phase (#1211 bridge r4 review, R4-B1): on three states,
           exp(-i th X_ab) = exp(-i th) G_(ab)(2 th / pi) diag(1, 1, exp(i th)), G the gate flow of the
           transposition (the content of `gateFlow_isolation`, LiftAudit.lean:660, read from the other side);
           at a quarter turn, drive * swap(a b) = -i diag(1, 1, i), the quarter phase on the third state as a
           channel. Countercontrol: the real rotation exp(th (E_ab - E_ba)) is non-monomial and moves the
           all-ones ray, and is real, so by W6 it keeps <Y> = 0 (moving the ray is not sufficient).
N6     W9  Python 3 `/` on integers is true division (a float), `//` is integer division; sympy 1.14 compares
           Rational(1, 2) with the float 0.5 as unequal under `==`.
"""
import itertools
import sympy as sp

R = sp.Rational
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
PAU = [I2, X, Y, Z]
kron = sp.kronecker_product
res = []

def chk(name, cond):
    res.append((name, bool(cond)))

def zero(M):
    return sp.simplify(M) == sp.zeros(*M.shape)

def table(rho):
    return [[sp.simplify((rho * kron(PAU[k], PAU[l])).trace()) for l in range(4)] for k in range(4)]

def bloch(rho):
    return [sp.simplify((rho * s).trace()) for s in (X, Y, Z)]

def is_real_matrix(M):
    return all(sp.simplify(sp.im(sp.expand_complex(x))) == 0 for x in M)

def monomial(M):
    return all(sum(1 for x in M.row(i) if sp.simplify(x) != 0) == 1 for i in range(M.rows))

# ---- W1: dual of the six Pauli sharp effects = cube cone ----
t = sp.symbols('t', positive=True)
v = sp.symbols('v1:4', real=True)
signs = list(itertools.product((1, -1), repeat=3))
lam = {s: sp.Mul(*[(t + s[i] * v[i]) for i in range(3)]) / (8 * t ** 2) for s in signs}
recon_t = sp.simplify(sum(lam[s] for s in signs) - t)
recon_v = [sp.simplify(sum(lam[s] * s[i] for s in signs) - v[i]) for i in range(3)]
# each lambda_s is a product of the dual's own inequalities t + s_i v_i >= 0, divided by 8 t^2 > 0
factors_are_dual_ineqs = all(set(sp.Mul.make_args(sp.factor(lam[s] * 8 * t ** 2))) <=
                             {t + s[i] * v[i] for i in range(3)} | {sp.Integer(1)} for s in signs)
chk('W1 dual subset cube cone: (t, v) = sum_s lambda_s (1, s), lambda_s = prod_i (t + s_i v_i) / (8 t^2)',
    recon_t == 0 and all(r == 0 for r in recon_v) and factors_are_dual_ineqs)
eff = [(1,) + tuple(sg if j == i else 0 for j in range(3)) for i in range(3) for sg in (1, -1)]
cube_verts = [(1,) + s for s in signs]
chk('W1 cube cone subset dual: every cube vertex is nonnegative on all six effects',
    all(sum(e[k] * h[k] for k in range(4)) >= 0 for e in eff for h in cube_verts))
pt = {t: 1, v[0]: R(101, 100), v[1]: 0, v[2]: 0}
chk('W1c control: (1, 101/100, 0, 0) violates one effect and gets a negative lambda',
    any(sum(e[k] * h for k, h in enumerate((1, R(101, 100), 0, 0))) < 0 for e in eff)
    and any(lam[s].subs(pt) < 0 for s in signs))

# ---- W2 ----
in_cube = lambda h: all(h[0] - abs(x) >= 0 for x in h[1:])
in_oct = lambda h: h[0] - sum(abs(x) for x in h[1:]) >= 0
in_lor = lambda h: h[0] >= 0 and h[0] ** 2 - sum(x * x for x in h[1:]) >= 0
chk('W2 octahedron generators (1, +-e_i) in the cube cone; (1,1,1,1) outside octahedron and Lor',
    all(in_cube(e) for e in eff) and not in_oct((1, 1, 1, 1)) and not in_lor((1, 1, 1, 1)))

# ---- W3: node-10 table T, validity holds, not a state ----
a1, a2, a3, b1, b2, b3 = sp.symbols('a1 a2 a3 b1 b2 b3', real=True)
T = (kron(I2, I2) + kron(X, X) + kron(Z, Z)) / 4
wT = table(T)
hT = [sp.expand(sum(([1, a1, a2, a3])[k] * wT[k][l] for k in range(4))) for l in range(4)]
chk('W3 herald of T by a is (1, a1, 0, a3)', hT == [1, a1, 0, a3])
chk('W3 1 - a1^2 - a3^2 = (1 - |a|^2) + a2^2 (so the herald is in Lor for |a| <= 1)',
    sp.expand((1 - a1 ** 2 - a3 ** 2) - ((1 - a1 ** 2 - a2 ** 2 - a3 ** 2) + a2 ** 2)) == 0)
pv = sp.expand(sum(([1, a1, a2, a3])[k] * wT[k][l] * ([1, b1, b2, b3])[l] for k in range(4) for l in range(4)))
cert = (1 - a1 ** 2 - a3 ** 2) + (1 - b1 ** 2 - b3 ** 2) + (a1 + b1) ** 2 + (a3 + b3) ** 2
chk('W3 product value 1 + a1 b1 + a3 b3, and 2 * value = sum of terms each >= 0 on the ball',
    pv == 1 + a1 * b1 + a3 * b3 and sp.expand(2 * pv - cert) == 0)
singlet = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
chk('W3 T singlet = -1/4 singlet', zero(T * singlet + singlet / 4))

# ---- W4: swap ----
ur = sp.symbols('ur0 ur1', real=True); ui = sp.symbols('ui0 ui1', real=True)
vr = sp.symbols('vr0 vr1', real=True); vi = sp.symbols('vi0 vi1', real=True)
u = sp.Matrix([ur[0] + sp.I * ui[0], ur[1] + sp.I * ui[1]])
vv = sp.Matrix([vr[0] + sp.I * vi[0], vr[1] + sp.I * vi[1]])
SW = sp.Matrix(4, 4, lambda r, c: 1 if (r, c) in {(0, 0), (1, 2), (2, 1), (3, 3)} else 0)
uv = kron(u, vv)
val = sp.expand((uv.H * SW * uv)[0])
ip = (u.H * vv)[0]
chk('W4 swap on products: <u v|SW|u v> = |<u|v>|^2 (real and imaginary parts explicit)',
    sp.expand(val - sp.expand(ip * sp.conjugate(ip))) == 0)
chk('W4 swap singlet = -singlet', zero(SW * singlet + singlet))

# ---- W5: conditional matrices; transposition ----
xs = sp.symbols('x0:16'); ys = sp.symbols('y0:16')
Xg = sp.Matrix(4, 4, [xs[i] + sp.I * ys[i] for i in range(16)])
al = sp.Matrix(sp.symbols('al0 al1')); be = sp.Matrix(sp.symbols('be0 be1'))
lhs = (kron(al, be).H * Xg * kron(al, be))[0]
sigma = kron(al.H, I2) * Xg * kron(al, I2)
rhs = (be.H * sigma * be)[0]
chk('W5 <a b|X|a b> = <b|sigma_a|b> for generic complex X', sp.expand(lhs - rhs) == 0)
ws = sp.Matrix(4, 4, sp.symbols('w0:16'))
ah = sp.Matrix([1, a1, a2, a3]); bh = sp.Matrix([1, b1, b2, b3])
chk('W5 ahat^T w bhat = bhat^T w^T ahat (maxCone(eball d) x maxCone(eball d) is transpose-invariant)',
    sp.expand((ah.T * ws * bh)[0] - (bh.T * ws.T * ah)[0]) == 0)

# ---- W6: real operations keep <Y> = 0 ----
r00, r01, r11 = sp.symbols('r00 r01 r11', real=True)
rho = sp.Matrix([[r00, r01], [r01, r11]])
K1 = sp.Matrix(2, 2, sp.symbols('k0:4', real=True)); K2 = sp.Matrix(2, 2, sp.symbols('m0:4', real=True))
out = K1 * rho * K1.T + K2 * rho * K2.T
P0 = sp.diag(1, 0); P1 = sp.diag(0, 1)
chk('W6 real Kraus pair: output real symmetric and <Y> = 0; real Lueders branches also',
    zero(out - out.T) and all(x.is_real for x in out) and sp.simplify((out * Y).trace()) == 0
    and all(sp.simplify((P * rho * P * Y).trace()) == 0 for P in (P0, P1)))
yplus = sp.Matrix([1, sp.I]) / sp.sqrt(2)
chk('W6 y+ is not real (<Y> = 1)', sp.simplify((yplus * yplus.H * Y).trace()) == 1)

# ---- W7: the kernel gate flow on Fin 2 ----
tt = sp.symbols('tt', real=True)
unit = lambda g, s: sp.eye(g.shape[0]) + (sp.exp(sp.pi * sp.I * s) - 1) * (sp.eye(g.shape[0]) - g) / 2
U = sp.simplify(unit(X, R(1, 2)))
z0 = sp.Matrix([1, 0]); ones = sp.Matrix([1, 1])
chk('W7 unit(X,1/2): unitary, non-real, non-monomial, fixes (1,1)',
    zero(U * U.H - I2) and not is_real_matrix(U) and not monomial(U) and zero(U * ones - ones))
Ut = unit(X, tt)
chk('W7 unit(X,t) commutes with X (so <X> is conserved under it)', zero(Ut * X - X * Ut))
bt = [sp.simplify(sp.expand_complex(x)) for x in bloch(Ut * z0 * (Ut * z0).H)]
chk('W7 unit(X,t) z+ has Bloch vector (0, -sin pi t, cos pi t); at t = 1/2 this is y-',
    bt == [0, -sp.sin(sp.pi * tt), sp.cos(sp.pi * tt)] and bloch(U * z0 * (U * z0).H) == [0, -1, 0])
Sg = sp.diag(1, sp.I); H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
chk('W7c controls: quarter phase S takes (1,1) off its ray; real H gives <Y> = 0 from z+',
    sp.Matrix.hstack(Sg * ones, ones).rank() == 2 and bloch(H * z0 * (H * z0).H)[1] == 0)

# ---- W8: the driven transition on four states, no separate phase gate ----
def transition(i, j, n=4):
    M = sp.zeros(n, n); M[i, j] = 1; M[j, i] = 1
    return M
def drive(i, j, s, n=4):
    M = sp.eye(n); M[i, i] = sp.cos(s); M[j, j] = sp.cos(s); M[i, j] = -sp.I * sp.sin(s); M[j, i] = -sp.I * sp.sin(s)
    return M
def exch(i, j, n=4):
    M = sp.eye(n); M[i, i] = 0; M[j, j] = 0; M[i, j] = 1; M[j, i] = 1
    return M
i00, i10, i11 = 0, 2, 3
De = (-sp.I * (sp.pi / 4) * transition(i00, i10)).exp()
D = drive(i00, i10, sp.pi / 4)
# sympy's simplify leaves (-1)**(1/4) forms unreduced; expand_complex reduces them (run 1 compared without it)
chk('W8c closed form of exp(-i t X_ab) at t = pi/4 equals the matrix exponential',
    zero((De - D).applyfunc(sp.expand_complex)))
ones4 = sp.ones(4, 1)
chk('W8c drive at pi/4: unitary, non-real, non-monomial, moves the all-ones ray',
    zero(D * D.H - sp.eye(4)) and not is_real_matrix(D) and not monomial(D)
    and sp.Matrix.hstack(D * ones4, ones4).rank() == 2)
k10 = sp.zeros(4, 1); k10[i10] = 1
psi1 = D * k10
tgt1 = kron(yplus, sp.Matrix([1, 0]))
chk('W8 one drive, |10> -> y+ (x) z+ (no separate phase gate; the drive is complex)', zero(psi1 * psi1.H - tgt1 * tgt1.H))
psi2 = exch(i10, i11) * drive(i10, i11, sp.pi / 2) * drive(i00, i10, sp.pi / 4) * k10
tgt2 = kron(sp.Matrix([1, 1]) / sp.sqrt(2), sp.Matrix([1, 0]))
chk('W8 two drives and one exchange, |10> -> x+ (x) z+ (no separate phase gate; the drive is complex)', zero(psi2 * psi2.H - tgt2 * tgt2.H))

# ---- W10: the drive carries a phase; a real rotation does not ----
th = sp.symbols('th', real=True)
def drive3(s_):
    M = sp.eye(3); M[0, 0] = sp.cos(s_); M[1, 1] = sp.cos(s_); M[0, 1] = -sp.I * sp.sin(s_); M[1, 0] = -sp.I * sp.sin(s_)
    return M
P01 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
G = unit(P01, 2 * th / sp.pi)
rhs3 = sp.exp(-sp.I * th) * G * sp.diag(1, 1, sp.exp(sp.I * th))
chk('W10 exp(-i th X_ab) = exp(-i th) G_(ab)(2 th/pi) diag(1,1,exp(i th)) on three states',
    zero((drive3(th) - rhs3).applyfunc(lambda x: sp.simplify(sp.expand_complex(sp.expand(x))))))
chk('W10 quarter turn: drive(pi/2) * swap(a b) = -i diag(1, 1, i)',
    zero(drive3(sp.pi / 2) * P01 - (-sp.I) * sp.diag(1, 1, sp.I)))
Rot = sp.Matrix([[sp.cos(sp.pi / 4), -sp.sin(sp.pi / 4), 0], [sp.sin(sp.pi / 4), sp.cos(sp.pi / 4), 0], [0, 0, 1]])
Rot_exp = (sp.pi / 4 * sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])).exp()
ones3 = sp.ones(3, 1)
chk('W10c real rotation exp(th(E_ab - E_ba)) at pi/4: real, non-monomial, moves the all-ones ray',
    zero((Rot - Rot_exp).applyfunc(sp.expand_complex)) and is_real_matrix(Rot) and not monomial(Rot)
    and sp.Matrix.hstack(Rot * ones3, ones3).rank() == 2)

# ---- W9: N6 ----
half = 1 / 2
chk('W9 Python 3: 1/2 is a float 0.5 (true division); 1//2 == 0 (integer division)',
    isinstance(half, float) and half == 0.5 and (1 // 2) == 0)
chk('W9 sympy: (Rational(1,2) == 0.5) is False; exact Rational(1,2) == Rational(1,2)',
    (R(1, 2) == half) is False and R(1, 2) == R(1, 2))

for n, ok_ in res:
    print(('PASS ' if ok_ else 'FAIL ') + n)
print('%d checks, %d failures' % (len(res), sum(1 for _, o in res if not o)))
raise SystemExit(0 if all(o for _, o in res) else 1)
