"""s5 -- QE1 node N1.9: the Pauli identification of DIM-1's d = 3 witnesses with two-qubit quantum theory.

Decision rule (fixed before running): the identification iota_Q (Bloch / Pauli expectation coordinates) is
CONFIRMED for K1 iff every listed identity holds exactly AND both countercontrols (a deliberately wrong
identification, a perturbed kernel table) FAIL the same comparison.
"""
import sys
from sympy import Matrix, I, Rational as R, symbols, simplify, expand, eye, zeros, sqrt, factor
from common import *

rep = Report("s5_pauli_adapter")

P0 = Matrix([[1, 0], [0, 0]])
P1 = Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, S0) + kron(P1, SX)          # control = first factor (index mu), target = second (nu)
CNOT_rev = kron(S0, P0) + kron(SX, P1)      # countercontrol: control/target exchanged

C16 = ptm2(CNOT)
K16 = kernel_cnot16()
rep.check("kernel cnot (CD:741-786) equals the Pauli transfer matrix of the quantum CNOT", C16 == K16)
rep.check("countercontrol: the CNOT with control and target exchanged does NOT match the kernel cnot",
          ptm2(CNOT_rev) != K16)
Kbad = K16.copy()
Kbad[4 * 1 + 3, 4 * 2 + 2] = -Kbad[4 * 1 + 3, 4 * 2 + 2]
rep.check("countercontrol: the kernel table with the sign at (1,3) flipped does NOT match", C16 != Kbad)

# one-copy objects
rep.check("ptm(X) = homMap nflip (the kernel NOT is the quantum NOT Ad_X)", ptm1(SX) == homMap(NFLIP))
rep.check("ptm(Y) = homMap diag(-1,1,-1)", ptm1(SY) == homMap(Matrix.diag(-1, 1, -1)))
rep.check("ptm(Z) = homMap diag(-1,-1,1)  (the NOT of the kernel's control drive ball3Drive, rot3 pi)",
          ptm1(SZ) == homMap(Matrix.diag(-1, -1, 1)))
ket0 = Matrix([1, 0]); ketp = Matrix([1, 1]) / sqrt(2)
bloch = lambda k: Matrix([simplify(tr((k * dag(k)) * P)) for P in (SX, SY, SZ)])
rep.check("Bloch(|0>) = z3 and Bloch(|+>) = xplus", bloch(ket0) == Z3 and bloch(ketp) == XPLUS)

# Bell image
rho_in = kron(rho1(XPLUS), rho1(Z3))
rho_out = CNOT * rho_in * dag(CNOT)
rep.check("coeffs(CNOT (|+><+| x |0><0|) CNOT^dag) = phiW (CD:1220), the Bell state Phi+",
          coeffs2(rho_out) == PHIW)
rep.check("kernel cnot (prodState xplus z3) = phiW", unvec(K16 * vec(prodState(XPLUS, Z3))) == PHIW)

# symbolic identities: prodState, effects, pairings
x0, x1, x2, y0, y1, y2 = symbols('x0 x1 x2 y0 y1 y2', real=True)
X = [x0, x1, x2]; Y = [y0, y1, y2]
rep.check("prodState x y = coefficient matrix of rho(x) (x) rho(y)  (symbolic)",
          (coeffs2(kron(rho1(X), rho1(Y))) - prodState(X, Y)).applyfunc(simplify) == zeros(4, 4))
b0, b1, b2 = symbols('b0 b1 b2', real=True)
Bv = [b0, b1, b2]
E_b = (S0 + b0 * SX + b1 * SY + b2 * SZ) / 2
sharp_val = R(1, 2) + sum(Bv[j] / 2 * X[j] for j in range(3))
rep.check("sharpEff b x = tr(rho(x) (I + b.sigma)/2)  (symbolic, EffectSpace:65)",
          simplify(tr(rho1(X) * E_b) - sharp_val) == 0)
a = symbols('a0:4', real=True); c = symbols('c0:4', real=True)
w = Matrix(4, 4, lambda m, n: symbols('w%d%d' % (m, n), real=True))
rho_w = zeros(4, 4)
for m in range(4):
    for n in range(4):
        rho_w += w[m, n] * PAULI2[4 * m + n] / 4
Ea = sum((a[m] * PAULI[m] for m in range(4)), zeros(2, 2))
Ec = sum((c[m] * PAULI[m] for m in range(4)), zeros(2, 2))
rep.check("prodEffVal e f omega = tr(rho_omega (E_e (x) E_f))  (symbolic, CD:182)",
          simplify(tr(rho_w * kron(Ea, Ec)) - pairVal(Matrix(a), Matrix(c), w)) == 0)

# ball <-> PSD, effect set <-> EFF-1's effect_eq_affine
lam = symbols('lam')
cp = (rho1(X) - lam * eye(2)).det()
rep.check("charpoly(rho(x)) = lam^2 - lam + (1 - |x|^2)/4: eigenvalues (1 +- |x|)/2, so PSD iff x in eball 3",
          simplify(cp - (lam ** 2 - lam + (1 - (x0 ** 2 + x1 ** 2 + x2 ** 2)) / 4)) == 0)
a0, v0, v1, v2 = symbols('a0 v0 v1 v2', real=True)
Ev = a0 * S0 + v0 * SX + v1 * SY + v2 * SZ
cpe = (Ev - lam * eye(2)).det()
rep.check("charpoly(a0 I + v.sigma) = (lam - a0)^2 - |v|^2: 0 <= E <= I iff |v| <= min(a0, 1 - a0) (EFF-1 effect_eq_affine)",
          simplify(cpe - ((lam - a0) ** 2 - (v0 ** 2 + v1 ** 2 + v2 ** 2))) == 0)

# rotations: unitary conjugation acts as SO(3); the transpose acts with det -1
Uz = Matrix([[1, 0], [0, (3 + 4 * I) / 5]])
Hd = Matrix([[1, 1], [1, -1]]) / sqrt(2)
for name, U in (("phase (3+4i)/5", Uz), ("Hadamard", Hd), ("S", Matrix([[1, 0], [0, I]]))):
    Cm = ptm1(U)
    Rm = Cm[1:, 1:]
    ok = Cm[0, :] == Matrix([[1, 0, 0, 0]]) and Cm[:, 0] == Matrix([1, 0, 0, 0]) and \
        (Rm * Rm.T).applyfunc(simplify) == eye(3) and simplify(Rm.det()) == 1
    rep.check("ptm(%s) = diag(1, R) with R in SO(3)" % name, ok)
Tmap = zeros(4, 4)
for m in range(4):
    for n in range(4):
        Tmap[m, n] = simplify(tr(PAULI[m] * PAULI[n].T) / 2)
rep.check("the transpose rho -> rho^T acts as homMap diag(1,-1,1) = homMap reflY (det -1): antiunitary, not an operation",
          Tmap == homMap(REFLY))

# relations of the d = 3 witness, re-verified through the quantum identification
HT = actT16(NFLIP); HC = actC16(NFLIP)
rep.check("relT: actT nflip . cnot . actT nflip = cnot  (exact 16x16)", HT * K16 * HT == K16)
rep.check("relC: actC nflip . cnot . actC nflip = actT nflip . cnot  (exact 16x16)", HC * K16 * HC == HT * K16)
rep.check("unitary form: (I x X) CNOT (I x X) = CNOT and (X x I) CNOT (X x I) = (I x X) CNOT",
          kron(S0, SX) * CNOT * kron(S0, SX) == CNOT and kron(SX, S0) * CNOT * kron(SX, S0) == kron(S0, SX) * CNOT)

# two-qubit states lie in maxCone: Bell state against sharp products (spot check; the general statement is
# tr(rho E (x) F) >= 0 for PSD rho, E, F -- written)
axes = [Matrix([s * (i == 0), s * (i == 1), s * (i == 2)]) for i in range(3) for s in (1, -1)]
vals = [pairVal(sharpVec(u), sharpVec(v), PHIW) for u in axes for v in axes]
rep.check("phiW pairs nonnegatively with all 36 products of axis sharp effects; minimum 0",
          min(vals) == 0 and all(v >= 0 for v in vals), "min=%s" % min(vals))

ok = rep.out()
sys.exit(0 if ok else 1)
