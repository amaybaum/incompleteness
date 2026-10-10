"""P4 (node N4) -- continuous exchange (CX): SWAP lies in the identity component of the group of normalization-
preserving automorphisms of the joint state space.  Converse test in quantum theory and the foils.

Checks:
  4.1 Choi-rank controls (layer [M]): elements of PU(4) = {Ad U} have Choi rank 1 (SWAP, cnot, a local rotation,
      the exchange path at rational points); the global transpose T and the partial transpose R_B do not.
  4.2 the twisted composite: R_B SWAP R_B has Choi rank != 1, so SWAP is not in R_B PU(4) R_B.
  4.3 quantum theory: an exact rational path tau -> Ad(c I - i s SWAP), c = (1-tau^2)/(1+tau^2), s = 2tau/(1+tau^2),
      from the identity (tau = 0) to SWAP (tau = 1), of Choi rank 1 throughout (unitary conjugations); its
      generator is in M1 (the Heisenberg exchange sum_i s_i (x) s_i).
  4.4 real two-rebit composite: the exchange permutation has determinant -1, so Ad(SWAP) is not Ad of SO(4).
  4.5 two classical bits: the symmetry group of the joint simplex is finite (S_4), so its identity component is
      trivial and contains no exchange.
Decision rule (fixed before the run): the CX verdict (QM satisfies CX; twisted, min, max (P3), real, classical fail)
is printed only if every control in 4.1 passes.
Usage: python3 -I p4_continuous_exchange.py <path to CompositeDimension.lean>
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa
import sympy as sp

rep = Report("P4 continuous exchange")
CN, *_ = parse_kernel_cnot(sys.argv[1])
RB = actT_mat(REFLY)
RA = actC_mat(REFLY)
q = (1, 2, -1, 3)
a, b, c, d = map(Fr, q)
n2 = a * a + b * b + c * c + d * d
Rq = [[(a*a+b*b-c*c-d*d)/n2, 2*(b*c-a*d)/n2, 2*(b*d+a*c)/n2],
      [2*(b*c+a*d)/n2, (a*a-b*b+c*c-d*d)/n2, 2*(c*d-a*b)/n2],
      [2*(b*d-a*c)/n2, 2*(c*d+a*b)/n2, (a*a-b*b-c*c+d*d)/n2]]
TT = matmul(RA, RB)

ranks = {name: crank(choi(g)) for name, g in [("SWAP", SWAP16), ("cnot", CN), ("actT R(q)", actT_mat(Rq)),
                                              ("actC R(q) cnot", matmul(actC_mat(Rq), CN)),
                                              ("T", TT), ("R_B", RB), ("identity", eye(16))]}
rep.note(f"Choi ranks: {ranks}")
rep.check("4.1a controls: identity, SWAP, cnot, a local rotation and a word in them have Choi rank 1 (Ad U)",
          all(ranks[k] == 1 for k in ("identity", "SWAP", "cnot", "actT R(q)", "actC R(q) cnot")))
rep.check("4.1b countercontrols: the global transpose T and the partial transpose R_B do not have Choi rank 1",
          ranks["T"] != 1 and ranks["R_B"] != 1)
tw = matmul(matmul(RB, SWAP16), RB)
r_tw = crank(choi(tw))
rep.check("4.2 R_B SWAP R_B has Choi rank != 1, so it is not in PU(4); hence SWAP is not in R_B PU(4) R_B, "
          "the identity component of Aut_u(R_B Q3) (by P2: its Lie algebra is l + M2)", r_tw != 1, f"rank {r_tw}")
rep.check("4.2b exact identity: R_B SWAP R_B = T SWAP (T = R_A R_B, the global transpose)", tw == matmul(TT, SWAP16))

# 4.3 the exchange path in quantum theory
SWU = cmat([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])


def path_unitary(tau):
    tau = Fr(tau)
    c_, s_ = (1 - tau * tau) / (1 + tau * tau), 2 * tau / (1 + tau * tau)
    return [[G(c_) * (G(1) if i == j else G(0)) + G(0, -s_) * SWU[i][j] for j in range(4)] for i in range(4)]


ok = True
for tau in (Fr(0), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(1)):
    U = path_unitary(tau)
    UU = cmul(U, cdag(U))
    ok &= all(UU[i][j] == (G(1) if i == j else G(0)) for i in range(4) for j in range(4))
    g = conj_unitary(U)
    ok &= crank(choi(g)) == 1
rep.check("4.3a the path members U(tau) = c I - i s SWAP are unitary and their W-maps have Choi rank 1 "
          "(tau = 0, 1/3, 1/2, 2/3, 1)", ok)
rep.check("4.3b endpoints: tau = 0 gives the identity, tau = 1 gives SWAP16",
          conj_unitary(path_unitary(0)) == eye(16) and conj_unitary(path_unitary(1)) == SWAP16)
Hh = cadd(cadd(SIG2[(1, 1)], SIG2[(2, 2)]), SIG2[(3, 3)])
rep.check("4.3c the generator: sum_i s_i (x) s_i = 2 SWAP - I (so U(tau) = exp(-i theta (2 SWAP - I)) up to phase, "
          "and ad of it lies in M1)", Hh == cadd(SWU, [[G(1) if i == j else G(0) for j in range(4)] for i in range(4)], 2, -1))
# symbolic: the W-matrix of the path is continuous (rational) in tau
tau = sp.symbols("tau", real=True)
rep.note("4.3d [written] tau -> conj_unitary(U(tau)) is a rational, hence continuous, path in Aut_u(Q3) from the "
         "identity to SWAP; so SWAP lies in Aut_u(Q3)_0 = PU(4). The same holds for every transposition of n copies.")

# 4.4 real rebits
P4 = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
rep.check("4.4a the real exchange matrix has det -1 (and det(-SWAP) = -1 in dimension 4)",
          det_frac(P4) == -1 and det_frac([[-x for x in r] for r in P4]) == -1)
# commutant of real symmetric 4x4 matrices: scalars (exact)
rows = []
syms = []
for i in range(4):
    for j in range(i, 4):
        S = [[Fr(0)] * 4 for _ in range(4)]
        S[i][j] = S[j][i] = Fr(1)
        syms.append(S)
for S in syms:
    for i in range(4):
        for j in range(4):
            row = [Fr(0)] * 16
            for k in range(4):
                row[i * 4 + k] += S[k][j]
                row[k * 4 + j] -= S[i][k]
            rows.append(row)
rep.check("4.4b the commutant of the real symmetric 4x4 matrices is the scalars (dimension 1), so Ad(O) = Ad(SWAP) "
          "forces O = +-SWAP, of determinant -1: Ad(SWAP) is not in Ad(SO(4)), the identity component of the "
          "rebit composite's automorphism group O(4)/{+-1} (Kadison-type fact for real PSD cones: literature)",
          16 - rank(rows, 16) == 1)
rep.note("4.5 [written] two classical bits: the joint state space is the 3-simplex; its affine automorphisms "
         "permute the 4 vertices (S_4, finite), so the identity component is trivial and the exchange (a nontrivial "
         "vertex permutation) is not in it.  Boxworld: reversible maps are local symmetries and system permutations "
         "(Gross-Mueller-Colbeck-Dahlsten 2010, literature, unverified here), a finite group for square bits.")
rep.verdict("CX-CONVERSE-AND-FOILS-EXACT: QM satisfies continuous exchange (exact rational path, Choi rank 1); the "
            "twisted composite fails it (Choi rank of R_B SWAP R_B is not 1); real rebits fail it (det -1); "
            "min and max fail it (P3: identity components are local)")
