"""s7 -- QE1 node N1.10: K2's premises (local tomography, the composite cone, compatible local actions) against QM.

Decision rule (fixed before running): K2's premise HOLDS in QM iff (i) product effects separate two-qubit states
(rank 16), (ii) the two-qubit state cone is a K2Guard `CandidateCone` (contains the product states, lies in maxCone)
invariant under cnot and under local rotations, exactly on generators; the foil (real QM) must FAIL local tomography
with an exact pair of states; and the one-copy reflection reflY must FAIL to preserve the quantum cone (the
partial transpose), reproducing K2Guard's chain value -1/2.
"""
import sys
from sympy import Matrix, Rational as R, I, eye, zeros, sqrt, simplify, symbols
from common import *

rep = Report("s7_k2_composite")
C = kernel_cnot16()

# (i) local tomography of the complex composite
basis = Matrix.hstack(*[Matrix([simplify(e) for e in (P.as_real_imag()[0])] + [simplify(e) for e in P.as_real_imag()[1]])
                        for P in PAULI2])
rep.check("complex two-qubit LT: the 16 Pauli products are R-linearly independent in Herm(4) (rank 16 = 4 x 4)",
          basis.rank() == 16)
# foil: real QM (rebits): local real effects span {I, X, Z}; Y (x) Y is invisible to products
rho1_ = eye(4) / 4
rho2_ = (eye(4) + kron(SY, SY)) / 4
lam = symbols('lam')
ev = (rho2_ - lam * eye(4)).det().factor()
rep.check("foil states are real symmetric two-rebit states: (I + Y(x)Y)/4 is real symmetric with spectrum {1/2,1/2,0,0}",
          rho2_ == rho2_.T and all(e.is_real for e in rho2_) and
          simplify(ev - (lam ** 2 * (lam - R(1, 2)) ** 2)) == 0)
real_loc = [S0, SX, SZ]
same = all(simplify(tr(rho1_ * kron(A, B)) - tr(rho2_ * kron(A, B))) == 0 for A in real_loc for B in real_loc)
rep.check("FOIL: real QM fails LT -- I/4 and (I + Y(x)Y)/4 agree on every product of real local effects", same and rho1_ != rho2_)

# (ii) the quantum cone as a candidate cone, invariant under cnot and local rotations
rep.note("written: tr(rho E (x) F) >= 0 for PSD rho, E, F, so the PSD cone lies in maxCone; products of states are PSD.")
Hd = Matrix([[1, 1], [1, -1]]) / sqrt(2)
Sg = Matrix([[1, 0], [0, I]])
gens = {"CNOT": kron(Matrix([[1, 0], [0, 0]]), S0) + kron(Matrix([[0, 0], [0, 1]]), SX),
        "H (x) I": kron(Hd, S0), "I (x) H": kron(S0, Hd), "S (x) I": kron(Sg, S0), "I (x) S": kron(S0, Sg)}
for name, U in gens.items():
    T = ptm2(U)
    # an invertible linear map of W 3 that is the transfer matrix of a unitary maps PSD states to PSD states;
    # check the unitarity that underlies it and that the transfer matrix is real orthogonal on the coefficient space
    rep.check("%s: unitary, and its transfer matrix is real with T T^T = I (it permutes the cone of states)" % name,
              (U * dag(U)).applyfunc(simplify) == eye(4) and all(e.is_real for e in T) and
              (T * T.T).applyfunc(simplify) == eye(16))
# (iii) the one-copy reflection reflY is the partial transpose and leaves the quantum cone
PT = actT16(REFLY)
bell = vec(PHIW)
rho_pt = sum((unvec(PT * bell)[m, n] * PAULI2[4 * m + n] for m in range(4) for n in range(4)), zeros(4, 4)) / 4
evpt = (rho_pt - lam * eye(4)).det().factor()
rep.check("actT reflY (the partial transpose on copy B) maps Phi+ to an operator with eigenvalue -1/2 (outside the cone)",
          simplify(evpt.subs(lam, R(-1, 2))) == 0)
chain = unvec(C * PT * C * vec(prodState(XPLUS, Z3)))
chainW = Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
val = pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), chain)
rep.check("K2Guard's chain (K2Guard:104,134) reproduced through the quantum identification: cnot . actT reflY . cnot "
          "(prodState xplus z3) = chainW, pairing -1/2 with sharp(-e1) (x) sharp(-e3)", chain == chainW and val == R(-1, 2))
rep.check("with nflip (= Ad_X, a rotation) in place of reflY the chain stays in the cone (value 0, as K2Guard records)",
          pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), unvec(C * actT16(NFLIP) * C * vec(prodState(XPLUS, Z3)))) == 0)
rep.note("reading: K2Guard's obstruction is the failure of positivity of the partial transpose; QM's local reversible "
         "group is SO(3) (det +1) and never contains reflY, so QM satisfies K2's compatible-local-action premise.")

ok = rep.out()
sys.exit(0 if ok else 1)
