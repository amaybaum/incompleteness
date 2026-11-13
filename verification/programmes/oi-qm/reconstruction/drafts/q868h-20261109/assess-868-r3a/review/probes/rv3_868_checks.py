"""REVIEW-868-r3: reviewer's own exact generic checks (WIP / UNVERIFIED).

Generic matrices and generic tables only; no OI update rule, encoding, record law or mechanism.
Re-typed by hand from the kernel at fd539e15 (not imported): `unit` (SecondOrderCircuit.lean:356),
`gateFlow` (LiftAudit.lean:47), `signFun`/`phaseFun` (LiftAudit.lean:582-587), `gateFlow_isolation`
(LiftAudit.lean:660), `flow` (ReachabilitySeam.lean:95), `transition` (LieRankSource.lean:199),
`phaseGate` (LieRankSource.lean:209). Imports no earlier probe. Run: python3 -I rv3_868_checks.py

K1  drive closed form solves dU/dth = -i X_ab U, U(0) = 1 (generic th), on 3 states.
K2  W10 identity e^{-i th X_ab} = e^{-i th} G_(ab)(2th/pi) diag(1,1,e^{i th}), generic th; three mutations fail.
K3  kernel isolation identity, re-typed, on 4 states with tau = (01)(23), a = 0 (sign conjugation active),
    generic t; and on 3 states with tau = (01) it equals the W10 right side at th = pi t.
K4  quarter turn: drive(pi/2) swap_ab = -i phaseGate(c); equal channels on a generic Hermitian rho;
    drive(pi/2) is monomial and non-real; real-rotation control is real.
K5  operational non-reality: e^{i phi} R (non-real matrix, real up to a global phase) keeps real states real;
    real Kraus on system + uniform ancilla, then partial trace, keeps <Y> = 0.
K6  layer flow on Fin 2: unit(X,t) z+ has <Y> = -sin(pi t); non-real and non-monomial at t = 1/3.
N3  <a b|X|a b> = <b|sigma_a|b> for generic complex X, a, b; sigma_a Hermitian for Hermitian X;
    control: diag(1,-1,1,1) gives a non-PSD sigma_a and a negative product value at the same a, b;
    transposition: herald h_a(w) = toOp(w^T) ahat; asymmetric control w3 where the two orientations differ.
N7  W1: on a 5^3 rational grid of the cube cone (t = 1) every lambda_s >= 0 and reconstructs (t, v);
    six points just outside violate an effect. W3: the SOS identity; eigenvalues of T; mutation
    T_c = (I + c XX + c ZZ)/4, c = 11/10, negative product value.
"""
import itertools
import sympy as sp

R = sp.Rational
I, pi = sp.I, sp.pi
X2 = sp.Matrix([[0, 1], [1, 0]]); Y2 = sp.Matrix([[0, -I], [I, 0]]); Z2 = sp.Matrix([[1, 0], [0, -1]])
kron = sp.kronecker_product
res = []

def chk(n, c):
    res.append((n, bool(c)))

def z(M):
    return all(sp.simplify(sp.expand(sp.expand_complex(sp.expand(x).rewrite(sp.cos)))) == 0 for x in M)

def unit(g, s):  # SecondOrderCircuit.lean:356
    n = g.shape[0]
    return sp.eye(n) + (sp.exp(pi * I * s) - 1) * (sp.eye(n) - g) / 2

def perm(p, n):  # permutation matrix, column j -> row p[j]
    M = sp.zeros(n, n)
    for j in range(n):
        M[p[j], j] = 1
    return M

def trans(a, b, n):  # E_ab + E_ba
    M = sp.zeros(n, n); M[a, b] = 1; M[b, a] = 1
    return M

def drive(a, b, s, n):  # closed form of exp(-i s X_ab)
    M = sp.eye(n); M[a, a] = sp.cos(s); M[b, b] = sp.cos(s); M[a, b] = -I * sp.sin(s); M[b, a] = -I * sp.sin(s)
    return M

def nz(M, sub):  # exact nonzero witness at a point (guards "not z(...)" against simplify failures)
    return any(sp.nsimplify(sp.simplify(sp.expand_complex(sp.expand(x.subs(sub))))).is_zero is False for x in M)

def real_mat(M):
    return all(sp.simplify(sp.im(sp.expand_complex(x))) == 0 for x in M)

def monomial(M):
    return all(sum(1 for x in M.row(i) if sp.simplify(x) != 0) == 1 for i in range(M.rows))

th, tt, phi = sp.symbols('th tt phi', real=True)

# K1
U3 = drive(0, 1, th, 3)
chk('K1 closed form: dU/dth = -i X_ab U and U(0) = 1 (so it is exp(-i th X_ab))',
    z(U3.diff(th) + I * trans(0, 1, 3) * U3) and U3.subs(th, 0) == sp.eye(3))

# K2
G = unit(perm([1, 0, 2], 3), 2 * th / pi)
rhs = sp.exp(-I * th) * G * sp.diag(1, 1, sp.exp(I * th))
chk('K2 W10 identity holds for generic th', z(U3 - rhs))
m1 = sp.exp(-I * th) * G * sp.diag(1, 1, sp.exp(-I * th))
m2 = sp.exp(-I * th) * unit(perm([1, 0, 2], 3), th / pi) * sp.diag(1, 1, sp.exp(I * th))
m3 = G * sp.diag(1, 1, sp.exp(I * th))
chk('K2 mutations fail: conjugate phase / gate time th/pi / missing prefactor',
    nz(U3 - m1, {th: pi / 3}) and nz(U3 - m2, {th: pi / 3}) and nz(U3 - m3, {th: pi / 3}))

# K3: kernel isolation identity, re-typed
def isolation_lhs(tau, a, n, t):
    enum = list(range(n))
    sign = sp.diag(*[(-1 if (tau[x] != x and x not in (a, tau[a]) and enum[x] < enum[tau[x]]) else 1) for x in range(n)])
    phase = sp.diag(*[(1 if tau[x] == x else sp.exp(-pi * I * t)) for x in range(n)])
    Gt = unit(perm(tau, n), t)
    return phase * Gt * (sign * Gt * sign)
L4 = isolation_lhs([1, 0, 3, 2], 0, 4, tt)
chk('K3 isolation identity on 4 states, tau = (01)(23): lhs = exp(-i pi t X_01), generic t',
    z(L4 - drive(0, 1, pi * tt, 4)))
L4bad = unit(perm([1, 0, 3, 2], 4), tt) ** 2 * sp.diag(*[sp.exp(-pi * I * tt)] * 4)
chk('K3 control: without the sign conjugation the (23) block does not cancel',
    nz(L4bad - drive(0, 1, pi * tt, 4), {tt: R(1, 3)}))
L3 = isolation_lhs([1, 0, 2], 0, 3, tt)
chk('K3 on 3 states, tau = (01): kernel lhs equals the W10 right side at th = pi t',
    z(L3 - rhs.subs(th, pi * tt)))

# K4
Dq = drive(0, 1, pi / 2, 3); SWab = perm([1, 0, 2], 3)
phaseGate_c = sp.diag(1, 1, I)  # LieRankSource.lean:209 with a = third state
chk('K4 drive(pi/2) * swap_ab = -i phaseGate(c)', z(Dq * SWab + I * phaseGate_c))
hs = sp.symbols('h0:9', real=True)
rho = sp.Matrix([[hs[0], hs[1] + I * hs[2], hs[3] + I * hs[4]],
                 [hs[1] - I * hs[2], hs[5], hs[6] + I * hs[7]],
                 [hs[3] - I * hs[4], hs[6] - I * hs[7], hs[8]]])
W = Dq * SWab
chk('K4 as channels: (drive swap) rho (drive swap)^H = phaseGate rho phaseGate^H, generic Hermitian rho',
    z(W * rho * W.H - phaseGate_c * rho * phaseGate_c.H))
chk('K4 drive at the quarter turn is monomial and non-real (non-monomiality needs generic times)',
    monomial(Dq) and not real_mat(Dq) and not monomial(drive(0, 1, pi / 3, 3)))
Rq = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
chk('K4 control: the real rotation at the quarter turn times the swap is real, so not the phase channel',
    real_mat(Rq * SWab) and nz((Rq * SWab) * rho * (Rq * SWab).H - phaseGate_c * rho * phaseGate_c.H,
                               {hs[k]: k + 1 for k in range(9)}))

# K5
r = sp.symbols('r0:3', real=True)
rr = sp.Matrix([[r[0], r[1]], [r[1], r[2]]])
Rg = sp.Matrix(2, 2, sp.symbols('q0:4', real=True))
Up = sp.exp(I * phi) * Rg
out = Up * rr * Up.H
chk('K5 e^{i phi} R is a non-real matrix but keeps real states real (definition must be operational)',
    not real_mat(Up) and real_mat(out) and sp.simplify((out * Y2).trace()) == 0)
K = sp.Matrix(4, 4, sp.symbols('k0:16', real=True))
big = K * kron(rr, sp.eye(2) / 2) * K.T
red = sp.Matrix(2, 2, lambda i, j: big[2 * i, 2 * j] + big[2 * i + 1, 2 * j + 1])
chk('K5 real Kraus on system + uniform ancilla, partial trace: output real, <Y> = 0',
    real_mat(red) and sp.simplify((red * Y2).trace()) == 0)

# exact nonzero witnesses certify the "fails" checks above (K2 mutations at th = pi/3; K3 at t = 1/3; K4 at h_k = k+1)
# K6
Uf = unit(X2, tt); z0 = sp.Matrix([1, 0]); psi = Uf * z0
chk('K6 layer flow on Fin 2: <Y>(unit(X,t) z+) = -sin(pi t)',
    z(sp.Matrix([(psi.H * Y2 * psi)[0] + sp.sin(pi * tt)])))
U13 = unit(X2, R(1, 3))
chk('K6 unit(X,1/3) non-real, non-monomial', not real_mat(U13) and not monomial(U13))

# N3
xs = sp.symbols('x0:16', real=True); ys = sp.symbols('y0:16', real=True)
Xg = sp.Matrix(4, 4, [xs[i] + I * ys[i] for i in range(16)])
ar = sp.symbols('ar0:2', real=True); ai = sp.symbols('ai0:2', real=True)
br = sp.symbols('br0:2', real=True); bi = sp.symbols('bi0:2', real=True)
av = sp.Matrix([ar[0] + I * ai[0], ar[1] + I * ai[1]]); bv = sp.Matrix([br[0] + I * bi[0], br[1] + I * bi[1]])
sig = kron(av.H, sp.eye(2)) * Xg * kron(av, sp.eye(2))
chk('N3 <a b|X|a b> = <b|sigma_a|b>, generic complex X, a, b (real and imaginary parts explicit)',
    sp.expand((kron(av, bv).H * Xg * kron(av, bv))[0] - (bv.H * sig * bv)[0]) == 0)
Xh = (Xg + Xg.H) / 2
sh = kron(av.H, sp.eye(2)) * Xh * kron(av, sp.eye(2))
chk('N3 sigma_a Hermitian for Hermitian X', sp.expand(sh - sh.H) == sp.zeros(2, 2))
Xc = sp.diag(1, -1, 1, 1); e0 = sp.Matrix([1, 0]); e1 = sp.Matrix([0, 1])
sc = kron(e0.H, sp.eye(2)) * Xc * kron(e0, sp.eye(2))
chk('N3 control: X = diag(1,-1,1,1): sigma_e0 = diag(1,-1) not PSD and <e0 e1|X|e0 e1> = -1',
    sc == sp.diag(1, -1) and (kron(e0, e1).H * Xc * kron(e0, e1))[0] == -1)
w = sp.Matrix(4, 4, sp.symbols('w0:16', real=True))
a = sp.symbols('a1:4', real=True); b = sp.symbols('b1:4', real=True)
ah = sp.Matrix([1, *a]); bh = sp.Matrix([1, *b])
chk('N3 transposition: h_a(w) = (ahat^T w)^T = toOp(w^T) ahat, and pairVal(w,a,b) = pairVal(w^T,b,a)',
    (ah.T * w).T == w.T * ah and sp.expand((ah.T * w * bh)[0] - (bh.T * w.T * ah)[0]) == 0)
w3 = sp.zeros(4, 4); w3[0, 0] = 1; w3[1, 1] = 1; w3[1, 2] = 1
ex = sp.Matrix([1, 1, 0, 0])
chk('N3 orientation matters: w3 herald by +x on A is (1,1,1,0), on B is (1,1,0,0)',
    list(ex.T * w3) == [1, 1, 1, 0] and list(w3 * ex) == [1, 1, 0, 0])

# N7: W1 grid, W3
eff = [(1,) + tuple(s if j == i else 0 for j in range(3)) for i in range(3) for s in (1, -1)]
grid = [R(k, 2) for k in range(-2, 3)]
ok = True
for v in itertools.product(grid, repeat=3):
    lam = {s: sp.Mul(*[(1 + s[i] * v[i]) for i in range(3)]) / 8 for s in itertools.product((1, -1), repeat=3)}
    ok &= all(x >= 0 for x in lam.values())
    ok &= sum(lam.values()) == 1 and all(sum(lam[s] * s[i] for s in lam) == v[i] for i in range(3))
    ok &= all(sum(e[k] * h for k, h in enumerate((1,) + v)) >= 0 for e in eff)
chk('N7 W1 on 125 grid points of the cube cone (t = 1): lambda_s >= 0, reconstruction exact, all effects >= 0', ok)
outs = [tuple(R(11, 10) * (s if j == i else 0) for j in range(3)) for i in range(3) for s in (1, -1)]
chk('N7 W1 control: six points with one |v_i| = 11/10 each violate some effect',
    all(any(sum(e[k] * h for k, h in enumerate((1,) + v)) < 0 for e in eff) for v in outs))
cert = (1 - a[0]**2 - a[2]**2) + (1 - b[0]**2 - b[2]**2) + (a[0] + b[0])**2 + (a[2] + b[2])**2
chk('N7 W3 SOS: 2(1 + a1 b1 + a3 b3) equals the certificate', sp.expand(2 * (1 + a[0]*b[0] + a[2]*b[2]) - cert) == 0)
T = (sp.eye(4) + kron(X2, X2) + kron(Z2, Z2)) / 4
chk('N7 W3 eigenvalues of T are {3/4, 1/4, 1/4, -1/4}', T.eigenvals() == {R(3, 4): 1, R(1, 4): 2, R(-1, 4): 1})
Pa = (sp.eye(2) + X2) / 2; Pb = (sp.eye(2) - X2) / 2
Tc = (sp.eye(4) + R(11, 10) * kron(X2, X2) + R(11, 10) * kron(Z2, Z2)) / 4
chk('N7 W3 mutation: T with c = 11/10 gives a negative product probability at (+x, -x); T itself gives 0',
    (Tc * kron(Pa, Pb)).trace() < 0 and (T * kron(Pa, Pb)).trace() == 0)

for n, o in res:
    print(('PASS ' if o else 'FAIL ') + n)
print('%d checks, %d failures' % (len(res), sum(1 for _, o in res if not o)))
raise SystemExit(0 if all(o for _, o in res) else 1)
