"""Disc-composite no-go -- exact certificate (sympy over Q). Read-only; nothing touches the repository.

Claim. Let C be a closed cone in R^3 (x) R^3 with L3 (x)min L3 <= C <= L3 (x)max L3, invariant under the local rotations
T = SO(2) x SO(2). Then every normalization-preserving linear automorphism G of C normalizes T. In particular no G acts
as CNOT on the four classical products (no involution or native relation is used).

Proof skeleton, each step checked below.
 N1  Aut(C) (normalization-preserving) is compact; K0 is its identity component, K0 >= T; k = Lie(K0).
 N2  First order: X in k => (f_v (x) I) X (p_v (x) p_w) = 0 = (I (x) f_w) X (p_v (x) p_w) and (u(x)u)^T X = 0 (boundary
     argument: f_v (x) g >= 0 on C for every g, value 0 at s = 0). The solution space Lam (sampled -> superset) is 7-dim.
 N3  Lam = t (+) W10 (+) W01 (+) span(E4): Ad(T)-weight blocks (1,0), (0,1), 0.
 N4  [W10, W10] and [W01, W01] leave Lam, so a Lie subalgebra k with t <= k <= Lam meets W10 and W01 trivially.
 N5  E4 commutes with t and has eigenvalue 1 on a real eigenvector; T is orthogonal, so exp(s(aT1 + bT2 + cE4)) is
     unbounded for c != 0: E4 components are excluded from a compact k. Hence k = t, K0 = T, T normal in Aut(C).
 N6  G normalizing T maps each real T-isotypic block onto one block; CNOT-on-corners sends zu (block (0,1)) to zz,
     which lies in no single block. Contradiction.
Controls: C1 (Bloch ball, n = 4): the complex CNOT satisfies the frame, involution and native relations, and all 15 su(4)
generators satisfy the n = 4 first-order conditions -- the method does not exclude complex QM. C2: swap and local
reflections normalize T and preserve min and max -- the method does not exclude the discrete symmetries the min tensor
product actually has. C3: the four nonlocal antisymmetric first-order solutions are the projections of real QM's
nonlocal so(4) generators onto the locally tomographic span -- the first-order space is where real QM leaks in, and N4 is
where it is cut off.
"""
import itertools, pickle, sympy as sp
from disc_lie import run

OUT = []
def rep(name, ok, detail=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''), flush=True)

kron = sp.kronecker_product
lab = ['%s%s' % (a, b) for a in 'uxz' for b in 'uxz']; ix = {l: i for i, l in enumerate(lab)}
def E(i, j): M = sp.zeros(9); M[ix[i], ix[j]] = 1; return M
J = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])              # rotation generator of the disc (x, z)
I3 = sp.eye(3); T1, T2 = kron(J, I3), kron(I3, J)
br = lambda a, b: a * b - b * a

# N2 -------------------------------------------------------------------------------------------------------------
ns = run(3); B = [sp.Matrix(9, 9, list(v)) for v in ns]
Lam = sp.Matrix([list(M) for M in B]).T
def inspan(Mat, M):
    try: Mat.gauss_jordan_solve(sp.Matrix(list(M))); return True
    except ValueError: return False
rep('N2 first-order solution space (superset of the true one) has dimension 7', len(B) == 7)
rep('N2 local rotation generators T1, T2 lie in it', inspan(Lam, T1) and inspan(Lam, T2))

# N3 -------------------------------------------------------------------------------------------------------------
# complement to t inside Lam, chosen as the explicit elements printed by disc_lie2.py
W10 = [E('uz', 'xx') - E('xx', 'uz') - E('ux', 'xz') + E('xz', 'ux'),
       E('uz', 'zx') - E('zx', 'uz') - E('ux', 'zz') + E('zz', 'ux')]
W01 = [E('zu', 'xx') - E('xx', 'zu') - E('xu', 'zx') + E('zx', 'xu'),
       E('zu', 'xz') - E('xz', 'zu') - E('xu', 'zz') + E('zz', 'xu')]
E4 = E('xx', 'zz') + E('zz', 'xx') - E('xz', 'zx') - E('zx', 'xz')
basis = [T1, T2] + W10 + W01 + [E4]
Bm = sp.Matrix([list(M) for M in basis]).T
rep('N3 {T1, T2, W10, W01, E4} is a basis of the first-order space', Bm.rank() == 7 and
    all(inspan(Bm, M) for M in B) and all(inspan(Lam, M) for M in basis))
rep('N3 W10 is a weight-(1,0) block: ad T1 rotates it, ad T2 kills it',
    br(T1, W10[0]) == W10[1] and br(T1, W10[1]) == -W10[0] and br(T2, W10[0]) == sp.zeros(9) and br(T2, W10[1]) == sp.zeros(9))
rep('N3 W01 is a weight-(0,1) block', br(T2, W01[0]) == W01[1] and br(T2, W01[1]) == -W01[0] and
    br(T1, W01[0]) == sp.zeros(9) and br(T1, W01[1]) == sp.zeros(9))
rep('N3 E4 has weight 0 (commutes with T1, T2)', br(T1, E4) == sp.zeros(9) and br(T2, E4) == sp.zeros(9))

# N4 -------------------------------------------------------------------------------------------------------------
rep('N4 [W10_a, W10_b] is not in the first-order space', not inspan(Lam, br(W10[0], W10[1])))
rep('N4 [W01_a, W01_b] is not in the first-order space', not inspan(Lam, br(W01[0], W01[1])))

# N5 -------------------------------------------------------------------------------------------------------------
v = sp.zeros(9, 1); v[ix['xx']] = 1; v[ix['zz']] = 1
rep('N5 E4 v = v for a real vector v (real eigenvalue 1)', E4 * v == v)
rep('N5 T1, T2 are antisymmetric (exp(sT) orthogonal in the standard basis)', T1.T == -T1 and T2.T == -T2)

# N6 -------------------------------------------------------------------------------------------------------------
e = {'u': sp.Matrix([1, 0, 0]), 'x': sp.Matrix([0, 1, 0]), 'z': sp.Matrix([0, 0, 1])}
ket = [e['u'] + e['z'], e['u'] - e['z']]
c = {(a, b): kron(ket[a], ket[b]) for a in (0, 1) for b in (0, 1)}
Cm = sp.Matrix.hstack(*[c[k] for k in sorted(c)]); Im = sp.Matrix.hstack(*[c[(a, a ^ b)] for a, b in sorted(c)])
zu = kron(e['u'], e['z']); zz = kron(e['z'], e['z'])
coef = Cm.solve(zu)
rep('N6 frame forces G(u(x)z) = z(x)z', Im * coef == zz)
# real isotypic blocks of T on the rho(x)rho part: (1,1) where T1 v = T2 v, (1,-1) where T1 v = -T2 v
rep('N6 z(x)z lies in neither the (1,1) nor the (1,-1) block', T1 * zz != T2 * zz and T1 * zz != -T2 * zz)
rep('N6 u(x)z lies in the (0,1) block', T1 * zu == sp.zeros(9, 1) and T2 * zu != sp.zeros(9, 1))

# C2 -------------------------------------------------------------------------------------------------------------
S = sp.zeros(9)
for i in range(3):
    for j in range(3): S[j * 3 + i, i * 3 + j] = 1
R = sp.diag(1, 1, -1); RI = kron(R, I3)
rep('C2 swap normalizes T (S T1 S = T2) and local reflection does (R T1 R = -T1)',
    S * T1 * S == T2 and RI * T1 * RI == -T1 and RI * T2 * RI == T2)

# C3 -------------------------------------------------------------------------------------------------------------
X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.diag(1, -1); Y = sp.Matrix([[0, -1], [1, 0]])   # real antisymmetric "iY"
P = {'u': sp.eye(2), 'x': X, 'z': Z}
basis4 = [kron(P[a], P[b]) for a in 'uxz' for b in 'uxz']
def proj_gen(A):        # d/ds of exp(sA) rho exp(-sA), projected to the local span, in the (u,x,z)^2 coordinates
    M = sp.zeros(9)
    for j, Bj in enumerate(basis4):
        img = A * Bj - Bj * A
        for i, Bi in enumerate(basis4): M[i, j] = (img * Bi).trace() / 4
    return M
gens = [kron(Y, X), kron(Y, Z), kron(X, Y), kron(Z, Y)]
rep('C3 the four nonlocal real so(4) generators project into W10 + W01',
    all(inspan(sp.Matrix([list(M) for M in W10 + W01]).T, proj_gen(A)) for A in gens) and
    sp.Matrix([list(proj_gen(A)) for A in gens]).rank() == 4)

# C1 -------------------------------------------------------------------------------------------------------------
ns4 = run(4); Lam4 = sp.Matrix([list(v) for v in ns4]).T
Xc = sp.Matrix([[0, 1], [1, 0]]); Yc = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Zc = sp.diag(1, -1)
Pc = [sp.eye(2), Xc, Yc, Zc]
b16 = [kron(a, b) for a in Pc for b in Pc]
def gen16(H):
    M = sp.zeros(16)
    for j, Bj in enumerate(b16):
        img = sp.I * (H * Bj - Bj * H)
        for i, Bi in enumerate(b16): M[i, j] = sp.simplify((img * Bi).trace() / 4)
    return M
gs = [gen16(b) for b in b16[1:]]
rep('C1 all 15 su(4) generators (Pauli coordinates) satisfy the n = 4 first-order conditions',
    all(inspan(Lam4, g) for g in gs) and sp.Matrix([list(g) for g in gs]).rank() == 15, 'dim Lam4 = %d' % len(ns4))
CN = sp.eye(4)[[0, 1, 3, 2], :]
Gc = sp.zeros(16)
for j, Bj in enumerate(b16):
    img = CN * Bj * CN.T
    for i, Bi in enumerate(b16): Gc[i, j] = (img * Bi).trace() / 4
Gc = Gc.applyfunc(sp.nsimplify)
k4 = [sp.Matrix([1, 0, 0, 1]), sp.Matrix([1, 0, 0, -1])]
frame_ok = all(Gc * kron(k4[a], k4[b]) == kron(k4[a], k4[a ^ b]) for a in (0, 1) for b in (0, 1))
rep('C1 complex CNOT (Bloch ball) acts as CNOT on the classical products and is an involution',
    frame_ok and Gc * Gc == sp.eye(16))

print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
