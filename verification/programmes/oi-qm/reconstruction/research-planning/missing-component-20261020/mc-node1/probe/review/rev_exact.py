"""Independent review of mc1 (exact, SymPy). Own conventions: tensor order (ancilla, data) -- deliberately the
reverse of mc_check.py -- so no matrix is shared with the reviewed code."""
import sys
import sympy as sp
from sympy import Matrix, I, sqrt, cos, sin, exp, eye, zeros, symbols, pi, Rational, simplify

R = []
def chk(name, ok):
    R.append((name, bool(ok))); print(('PASS ' if ok else 'FAIL ') + name)
def kr(A, B): return Matrix(sp.kronecker_product(A, B))
def zero(M): return all(sp.simplify(sp.expand(sp.expand_complex(x))) == 0 for x in M)
def prop(K, U):
    """return c with K == c U (or None)."""
    idx = [(i, j) for i in range(U.rows) for j in range(U.cols) if sp.simplify(U[i, j]) != 0]
    i, j = idx[0]; c = sp.simplify(K[i, j] / U[i, j])
    return c if zero(K - c * U) else None

phi, t = symbols('phi t', real=True)
X = Matrix([[0, 1], [1, 0]]); Z = Matrix([[1, 0], [0, -1]]); I2 = eye(2)
k0, k1 = Matrix([1, 0]), Matrix([0, 1])
pI, mI = Matrix([1, I]) / sqrt(2), Matrix([1, -I]) / sqrt(2)
P = lambda v: v * v.H
Rx = lambda a: cos(a / 2) * I2 - I * sin(a / 2) * X

# ---- A. |+i> preparation ----
c_minus = prop(X * mI, pI)
chk('A0 X|-i> = c|+i> with c = %s (|c|=1)' % c_minus, c_minus is not None and sp.simplify(abs(c_minus) - 1) == 0)
b1, b2 = P(pI) * k0, X * P(mI) * k0
chk('A1 both Y-test branches on |0> (with X on -i) are prop. to |+i>, each weight 1/2',
    prop(b1, pI) is not None and prop(b2, pI) is not None
    and sp.simplify((b1.H * b1)[0] - Rational(1, 2)) == 0 and sp.simplify((b2.H * b2)[0] - Rational(1, 2)) == 0)

# ---- A. gadget: ancilla (first factor) |+i>, CNOT control=ancilla target=data, test ancilla in (w, w_perp) ----
CN = kr(P(k0), I2) + kr(P(k1), X)          # ancilla-controlled X on data
w, wp = Matrix([cos(phi), sin(phi)]), Matrix([-sin(phi), cos(phi)])
attach = kr(pI, I2)                         # 4x2 : psi -> |+i> (x) psi
Kw = kr(w.H, I2) * CN * attach
Kwp = X * kr(wp.H, I2) * CN * attach
U = Rx(-2 * phi)
cw, cwp = prop(Kw, U), prop(Kwp, U)
chk('A2 branch w   = c_w  R_x(-2phi), c_w=%s, |c_w|^2=1/2' % sp.simplify(cw),
    cw is not None and sp.simplify(sp.expand_complex(cw * sp.conjugate(cw)) - Rational(1, 2)) == 0)
chk('A3 branch w_perp (after X) = c R_x(-2phi), c=%s, |c|^2=1/2' % sp.simplify(cwp),
    cwp is not None and sp.simplify(sp.expand_complex(cwp * sp.conjugate(cwp)) - Rational(1, 2)) == 0)
# uncorrected w_perp branch is X R_x(-2phi), i.e. NOT R_x(-2phi): correction is load-bearing
Kwp_raw = kr(wp.H, I2) * CN * attach
chk('A4 control: uncorrected w_perp branch is prop. to X R_x(-2phi), not to R_x(-2phi) (generic phi)',
    prop(Kwp_raw, X * U) is not None and prop(Kwp_raw.subs(phi, Rational(1, 3)), U.subs(phi, Rational(1, 3))) is None)
# relation with the kernel's unit g t = 1 + (e^{i pi t}-1)(1-g)/2
unitX = I2 + (exp(I * pi * t) - 1) * (I2 - X) / 2
cu = prop(unitX, Rx(pi * t))
chk('A5 unit(X,t) = e^{i pi t/2} R_x(pi t): c=%s' % sp.simplify(cu), cu is not None and zero(Matrix([cu - exp(I * pi * t / 2)])))
chk('A6 phi = -pi t/2 gives R_x(-2phi) = R_x(pi t): conjugation equals conj by gateFlow X t for every real t',
    zero(U.subs(phi, -pi * t / 2) - Rx(pi * t)))
# spectator: a second data token and a level ancilla are untouched (gadget is local) -- the branch tensor identity
chk('A7 with a spectator token, branch = (c R_x) (x) I exactly', zero(kr(Kw, I2) - cw * kr(U, I2)))

# ---- B. OnesNormal is "1 in span{K_j^H 1}" (Kraus splitting); unsharp Lueders instruments generically satisfy it ----
ones2 = Matrix([1, 1])
E0 = sp.diag(Rational(1, 4), Rational(3, 4)); E1 = eye(2) - E0
K0, K1 = E0.applyfunc(sp.sqrt), E1.applyfunc(sp.sqrt)
s = symbols('s0 s1')
sol = sp.solve(list(s[0] * K0.H * ones2 + s[1] * K1.H * ones2 - ones2), s, dict=True)[0]
s0, s1 = sp.nsimplify(sol[s[0]]), sp.nsimplify(sol[s[1]])
def split(sv, L):
    """c in C^L with ||c||=1 and sum conj(c_l) = sv  (needs |sv| <= sqrt L)."""
    base = [sp.conjugate(sv) / L] * L
    r2 = 1 - sp.Abs(sv) ** 2 / L
    rvec = [sqrt(r2 / 2), -sqrt(r2 / 2)] + [0] * (L - 2)
    return [sp.simplify(base[l] + rvec[l]) for l in range(L)]
L = 2
c0, c1 = split(s0, L), split(s1, L)
Ks = [(c * K0, 0) for c in c0] + [(c * K1, 1) for c in c1]
rho = Matrix(2, 2, symbols('a b c d'))
same = all(zero(sum((K * rho * K.H for K, o in Ks if o == k), zeros(2, 2)) - (KK * rho * KK.H))
           for k, KK in [(0, K0), (1, K1)])
tot = sum((K.H * ones2 for K, o in Ks), zeros(2, 1))
chk('B1 unsharp Lueders E0=diag(1/4,3/4): explicit split decomposition (s0=%s, s1=%s, L=2) gives the same instrument'
    ' and sum K^H 1 = 1, i.e. OnesNormal HOLDS' % (s0, s1), same and zero(tot - ones2))
# B6-of-node instrument: CNOT data->anc on |0>_anc, unsharp readout on ancilla, configuration discard
CNd = kr(I2, P(k0)) * 0  # placeholder to keep ancilla-first convention explicit below
CN_d2a = kr(P(k0), I2) + kr(P(k1), X)       # here first factor = DATA control, second = ancilla target
att0 = kr(I2, k0)
vecs = []
for EE in (K0, K1):
    for cv in (k0, k1):
        K = kr(I2, cv.H) * kr(I2, EE) * CN_d2a * att0
        vecs.append(K.H * ones2)
M = Matrix.hstack(*vecs)
chk('B2 the node\'s B6 unsharp instrument: 1 lies in span{K^H 1} (rank %d), so OnesNormal HOLDS for it under splitting'
    % M.rank(), Matrix.hstack(M, ones2).rank() == M.rank())
# negative: Z, |-> preparation fail (span criterion is not vacuous)
chk('B3 control: Z^H 1 not prop. 1 -> unitary channel Z is not OnesNormal', Matrix.hstack(Z.H * ones2, ones2).rank() == 2)
mn = Matrix([1, -1]) / sqrt(2)
prepm = [mn * k0.T, mn * k1.T]   # replace-by-|-> channel
chk('B4 control: deterministic |-> preparation has all K^H 1 = 0 -> not OnesNormal',
    all(zero(K.H * ones2) for K in prepm))
# B5: |+i> preparation (replace channel) IS OnesNormal (overlap <+i|1> != 0) -- consistency with A1
prepi = [pI * k0.T, pI * k1.T]
Mi = Matrix.hstack(*[K.H * ones2 for K in prepi])
chk('B5 replace-by-|+i> channel: 1 in span{K^H 1} -> OnesNormal (not a ray breaker)', Matrix.hstack(Mi, ones2).rank() == Mi.rank())

# ---- B6. every orthogonal projector lies in the kernel's onesClass (InstrumentRealization.lean:446):
# P = c E^H W F with c=1, W=1 on R = T (+) T, E = [P; 1-P], F = [1; 0]; OnesCompatible E, F.
# So TU's projectors sit in an Architecture that is OnesFixing (onesClass_arch :628, isometry_fixes_ones :833).
a_, b_ = symbols('alpha beta', real=True)
v = Matrix([cos(a_), exp(I * b_) * sin(a_)])          # generic token vector (complex)
for name, PP in [('rank-1 token projector', P(v)), ('P(v) (x) I on two tokens', kr(P(v), I2))]:
    n = PP.rows; one_T = Matrix([1] * n); one_R = Matrix([1] * (2 * n))
    E = Matrix.vstack(PP, eye(n) - PP); F = Matrix.vstack(eye(n), zeros(n, n))
    okc = (zero(E.H * E - eye(n)) and zero(E.H * one_R - one_T) and zero(F.H * F - eye(n))
           and zero(F.H * one_R - one_T) and zero(E.H * F - PP))
    chk('B6 %s = E^H W F with ones-compatible E,F, W=1: in onesClass' % name, okc)

fails = [n for n, ok in R if not ok]
print('SUMMARY', len(R) - len(fails), 'PASS', len(fails), 'FAIL')
sys.exit(1 if fails else 0)
