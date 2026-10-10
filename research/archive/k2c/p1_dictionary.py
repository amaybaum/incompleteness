"""K2C P1 -- the W 3 <-> Herm(C^2 (x) C^2) dictionary, derived from the kernel definitions.

Decision rule (fixed before running): PASS iff every identity below holds as an exact symbolic identity
(sympy, no floats). The kernel objects are read from the Lean sources (pc, pt, sgn, nflip, reflY parsed; actT/actC
transcribed literally from their definitions and compared with the matrix forms). The dictionary is the
matrix model [M]: it is evidence that the kernel objects ARE the Pauli images of the quantum objects; it is not a
derivation of anything in the kernel. Countercontrols: three wrong gates must NOT match the kernel cnot.

Usage: python -I p1_dictionary.py <CompositeDimension.lean> <K2Guard.lean> <k2d dir>
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k2clib import *  # noqa

CD, KG, K2D = sys.argv[1], sys.argv[2], sys.argv[3]
tabs = parse_tables(CD)
nflip = parse_diag_map(CD, 'nflip')
reflY = parse_diag_map(KG, 'reflY')
print('parsed nflip =', list(nflip.diagonal()), ' reflY =', list(reflY.diagonal()), ' sgn negatives =', sorted(tabs['neg']))

om = omega_symbols()
# 1.1 bijection
herm = sp.symbols('h0:16', real=True)
Hgen = sp.Matrix([[herm[0], herm[4] + sp.I * herm[5], herm[6] + sp.I * herm[7], herm[8] + sp.I * herm[9]],
                  [herm[4] - sp.I * herm[5], herm[1], herm[10] + sp.I * herm[11], herm[12] + sp.I * herm[13]],
                  [herm[6] - sp.I * herm[7], herm[10] - sp.I * herm[11], herm[2], herm[14] + sp.I * herm[15]],
                  [herm[8] - sp.I * herm[9], herm[12] - sp.I * herm[13], herm[14] - sp.I * herm[15], herm[3]]])
check('1.1a q(rho_of(w)) = w (symbolic, 16 real coordinates)', sp.expand(q_of(rho_of(om)) - om) == sp.zeros(4, 4))
check('1.1b rho_of(q(H)) = H for a general Hermitian H (16 real parameters)',
      sp.expand(rho_of(q_of(Hgen)) - Hgen) == sp.zeros(4, 4))
check('1.1c q(H) is real for Hermitian H', all(sp.im(e) == 0 for e in q_of(Hgen)))

# 1.2 product states
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
rx = (I2 + x[0] * SX + x[1] * SY + x[2] * SZ) / 2
ry = (I2 + y[0] * SX + y[1] * SY + y[2] * SZ) / 2
check('1.2 q(rho(x) (x) rho(y)) = prodState x y', sp.expand(q_of(kron(rx, ry)) - prod_W(x, y)) == sp.zeros(4, 4))

# 1.3 product effects
a = sp.symbols('a0:4', real=True)
b = sp.symbols('b0:4', real=True)
Ea = a[0] * I2 + a[1] * SX + a[2] * SY + a[3] * SZ
Fb = b[0] * I2 + b[1] * SX + b[2] * SY + b[3] * SZ
check('1.3a Tr(E_a rho(x)) = sum a_mu hom x mu  (so ehom e = a)', sp.expand((Ea * rx).trace() - (sp.Matrix(a).T * hom(x))[0, 0]) == 0)
check('1.3b Tr((E_a (x) F_b) rho_of(w)) = pairVal a b w', sp.expand((kron(Ea, Fb) * rho_of(om)).trace() - pairval(a, b, om)) == 0)

# 1.4 Lor <-> PSD on one copy
lam = sp.Symbol('lam')
cp = sp.expand(Ea.charpoly(lam).as_expr())
check('1.4 charpoly(E_a) = lam^2 - 2 a0 lam + (a0^2 - a1^2 - a2^2 - a3^2)  [so E_a >= 0 iff Lor a; written step: 2x2 PSD iff tr,det >= 0]',
      sp.expand(cp - (lam ** 2 - 2 * a[0] * lam + a[0] ** 2 - a[1] ** 2 - a[2] ** 2 - a[3] ** 2)) == 0)

# 1.5 the gate
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])          # control = copy A (first index)
CN_BA = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])       # control = copy B
CZ = sp.diag(1, 1, 1, -1)
K = cnot_mat(tabs)
check('1.5a literal cnotFun = matrix form', sp.expand(cnot_fun(tabs, om) - unvec(K * vec(om))) == sp.zeros(4, 4))
check('1.5b kernel cnot (parsed) = transfer matrix of Ad(CNOT_{A->B})', K == ptm(CN))
check('1.5c countercontrol: kernel cnot != Ad(CNOT_{B->A})', K != ptm(CN_BA))
check('1.5d countercontrol: kernel cnot != Ad(CZ)', K != ptm(CZ))
cnotp = actT_mat(reflY) * K * actT_mat(reflY)
check("1.5e countercontrol: kernel cnot != cnot' := actT reflY . cnot . actT reflY", K != cnotp)
sys.path.insert(0, os.path.abspath(K2D))
import k2lib  # k2d's independent parser
check('1.5f cross-check: identical to k2d k2lib.kernel_cnot_matrix (independent parser)', k2lib.kernel_cnot_matrix(CD) == K)

# 1.6 actT / actC literal vs matrix, symbolic N
Nsym = sp.Matrix(3, 3, lambda i, j: sp.Symbol('n%d%d' % (i, j), real=True))
check('1.6a literal actT N w = matrix form (symbolic N, w)', sp.expand(actT_fun(Nsym, om) - unvec(actT_mat(Nsym) * vec(om))) == sp.zeros(4, 4))
check('1.6b literal actC N w = matrix form (symbolic N, w)', sp.expand(actC_fun(Nsym, om) - unvec(actC_mat(Nsym) * vec(om))) == sp.zeros(4, 4))
check('1.6c actT N (prodState x y) = prodState x (N y)', sp.expand(actT_fun(Nsym, prod_W(x, y)) - prod_W(x, list(Nsym * sp.Matrix(y)))) == sp.zeros(4, 4))
check('1.6d actC N (prodState x y) = prodState (N x) y', sp.expand(actC_fun(Nsym, prod_W(x, y)) - prod_W(list(Nsym * sp.Matrix(x)), y)) == sp.zeros(4, 4))

# 1.7 local SU(2) <-> SO(3), symbolic quaternion
qs = sp.symbols('q0:4', real=True)
n = sum(t ** 2 for t in qs)
R = quat_R(qs)
check('1.7a R(q) R(q)^T = I (rational functions of q)', sp.simplify(R * R.T - sp.eye(3)) == sp.zeros(3, 3))
check('1.7b det R(q) = 1', sp.simplify(R.det() - 1) == 0)
U = quat_U(qs)
check('1.7c U~ U~^H = |q|^2 I', sp.expand(U * U.H - n * I2) == sp.zeros(2, 2))
check('1.7d U~ (x.s) U~^H = |q|^2 (R(q) x).s  (R is the Bloch action of U~)',
      sp.simplify(U * (x[0] * SX + x[1] * SY + x[2] * SZ) * U.H
                  - n * sum((((R * sp.Matrix(x))[i]) * [SX, SY, SZ][i] for i in range(3)), sp.zeros(2, 2)))
      == sp.zeros(2, 2))
check('1.7e actT R(q) = transfer matrix of Ad(I (x) U~)/|q|^2  (all of SU(2), symbolic)',
      sp.simplify(ptm(kron(I2, U), n) - actT_mat(R)) == sp.zeros(16, 16))
check('1.7f actC R(q) = transfer matrix of Ad(U~ (x) I)/|q|^2  (all of SU(2), symbolic)',
      sp.simplify(ptm(kron(U, I2), n) - actC_mat(R)) == sp.zeros(16, 16))

# 1.8 the NOT
check('1.8a actT nflip = Ad(I (x) X)', actT_mat(nflip) == ptm(kron(I2, SX)))
check('1.8b actC nflip = Ad(X (x) I)', actC_mat(nflip) == ptm(kron(SX, I2)))
check('1.8c nflip = R(q) at q = (0,1,0,0)  (U~ = -iX)', quat_R((0, 1, 0, 0)) == nflip)

# 1.9 reflections are (partial) transposes
rho = rho_of(om)


def ptB(r):
    out = sp.zeros(4, 4)
    for i, j, k, l in itertools.product(range(2), repeat=4):
        out[2 * i + l, 2 * j + k] = r[2 * i + k, 2 * j + l]
    return out


def ptA(r):
    out = sp.zeros(4, 4)
    for i, j, k, l in itertools.product(range(2), repeat=4):
        out[2 * j + k, 2 * i + l] = r[2 * i + k, 2 * j + l]
    return out


check('1.9a actT reflY w = q(rho(w)^{T_B})  (one-copy reflection = partial transpose on copy B)',
      sp.expand(q_of(ptB(rho)) - actT_fun(reflY, om)) == sp.zeros(4, 4))
check('1.9b actC reflY w = q(rho(w)^{T_A})', sp.expand(q_of(ptA(rho)) - actC_fun(reflY, om)) == sp.zeros(4, 4))
check('1.9c actC reflY . actT reflY w = q(rho(w)^T)  (both copies = global transpose)',
      sp.expand(q_of(rho.T) - actC_fun(reflY, actT_fun(reflY, om))) == sp.zeros(4, 4))

# 1.10 corners
z3 = (0, 0, 1)
check('1.10 rho(z3) = |0><0|, rho(-z3) = |1><1|', ((I2 + SZ) / 2 == sp.Matrix([[1, 0], [0, 0]])) and ((I2 - SZ) / 2 == sp.Matrix([[0, 0], [0, 1]])))

nf = summary()
print('VERDICT P1:', 'DICTIONARY-EXACT' if nf == 0 else 'NOT RENDERED')
sys.exit(nf)
