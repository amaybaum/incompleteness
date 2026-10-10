"""s8 -- QE4: one quantum model carrying every landed premise of the route at once, and the cross-premise checks
across charts, gauges (orientation), composites, ancillas/embeddings and horizons.

The model M_Q (two qubits, iota_Q): Omega = eball 3; G = rotations (SO(3) = PU(2) by conjugation; the rational
rotations for the dense form); avail = all effects; seed r = sharpEff z3; z = z3; N = nflip = Ad_X; native gate cnot;
drive R_x(t) with J = cyc3; composite body = two-qubit states on the coordinate carrier W 3; capacity two.

Decision rule (fixed before running): QE4 reports "no incompatible pair among the landed premises" iff every
cross-premise identity below holds exactly in M_Q (the universal parts are cited kernel theorems); every exhibited
incompatibility must come with an exact witness and must involve a premise OUTSIDE M_Q's choices.
"""
import sys
from sympy import Matrix, Rational as R, I, eye, zeros, sqrt, simplify, symbols, cos, sin, pi
from common import *

rep = Report("s8_one_model")
C = kernel_cnot16()
x0, x1, x2 = symbols('x0 x1 x2', real=True)
X = Matrix([x0, x1, x2])
sharp = lambda b, x: R(1, 2) + sum(Matrix(b)[j] * x[j] for j in range(3)) / 2

# ---------------- A. the premises cohere inside M_Q
rep.check("seed = corners: sharpEff z3 is 1 at z3 and 0 at -z3 (K-inf-Seed's certain/zero states are DIM-1's corners)",
          sharp(Z3, Z3) == 1 and sharp(Z3, -Z3) == 0)
rep.check("the NOT complements the seed: sharpEff z3 (N x) = 1 - sharpEff z3 (x) (symbolic)",
          simplify(sharp(Z3, NFLIP * X) - (1 - sharp(Z3, X))) == 0)
Rx = lambda t: Matrix([[1, 0, 0], [0, cos(t), -sin(t)], [0, sin(t), cos(t)]])
rep.check("K-inf-Drive's NOT = DIM-1's NOT: R_x(pi) = nflip, and nflip is in G (orthogonal, det +1 = Ad_X)",
          Rx(pi) == NFLIP and NFLIP * NFLIP.T == eye(3) and NFLIP.det() == 1)
rep.check("K-inf-Trans's G contains no reflection (det +1 throughout), so K2Guard's obstruction never applies in M_Q",
          all(M.det() == 1 for M in (Rx(pi / 2), Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), NFLIP)))
# the composite body of M_Q is a COMP-1 `Composite` on the coordinate carrier, which is DIM-1's W 3
rep.note("COMP-1's coordinate carrier `Carrier dA dB` (CompositeInterface:579) is `Fin (dA+1) -> Fin (dB+1) -> R`, "
         "definitionally DIM-1's `W d` (CompositeDimension:97) at dA = dB = d; its `pState` (CI:633) and DIM-1's "
         "`prodState` (CD:161) are both hom x mu * hom y nu. The two-qubit state set on it has convexity, products, "
         "product-effect positivity, normalisation (written) and local tomography (s7, rank 16): a `Composite`.")
y0, y1, y2 = symbols('y0 y1 y2', real=True)
rho_xy = kron(rho1([x0, x1, x2]), rho1([y0, y1, y2]))
rep.check("normalisation: the (0,0) coordinate of every product state is tr(rho) = 1 (prodEff unit unit = 1)",
          simplify(coeffs2(rho_xy)[0, 0]) == 1)

# ---------------- B. charts and orientation
G_glob = actC16(REFLY) * actT16(REFLY)
rep.check("global orientation change (transpose on both copies) maps cnot to cnot (CNOT is real): M_Q is closed "
          "under the global antiunitary gauge, as `operational_orientation_noGo` requires", G_glob * C * G_glob == C)
T2 = actT16(REFLY) * C * actT16(REFLY)        # one-copy orientation change of the gate
corners = [Z3, -Z3]
frame2 = all(unvec(T2 * vec(prodState(corners[a], corners[b]))) == prodState(corners[a], corners[(a + b) % 2])
             for a in range(2) for b in range(2))
rel2 = actT16(NFLIP) * T2 * actT16(NFLIP) == T2 and actC16(NFLIP) * T2 * actC16(NFLIP) == actT16(NFLIP) * T2
rep.check("T'' = (I x reflY) cnot (I x reflY) meets DIM-1's frame and both relations with the same z3 and nflip",
          frame2 and rel2)
rep.note("T'' is also two-sided positive on maxCone and entangling (local ball automorphisms preserve maxCone, "
         "jointStates and its extreme points -- written), so T'' satisfies every K1 premise.")
img = unvec(T2 * vec(prodState(XPLUS, Z3)))
rho_img = sum((img[m, n] * PAULI2[4 * m + n] for m in range(4) for n in range(4)), zeros(4, 4)) / 4
lam = symbols('lam')
rep.check("but T'' (prodState xplus z3) is the partial transpose of Phi+, eigenvalue -1/2: T'' is not a quantum "
          "operation in M_Q's chart", simplify((rho_img - lam * eye(4)).det().subs(lam, R(-1, 2))) == 0)
chain = unvec(T2 * C * vec(prodState(XPLUS, Z3)))
val = pairVal(sharpVec([-1, 0, 0]), sharpVec([0, 0, -1]), chain)
rep.check("INCOMPATIBILITY (outside M_Q): cnot and T'' -- two gates each satisfying every K1 premise with the same z, N "
          "-- admit no common K2Guard candidate cone: T'' (cnot (prodState xplus z3)) pairs -1/2 with "
          "sharp(-e1) (x) sharp(-e3), so it is outside maxCone", val == R(-1, 2))

# ---------------- C. embeddings: the qubit as the face span{|0>,|1>} of the qutrit
P01 = Matrix.diag(1, 1, 0)
face = lambda x: Matrix([[(1 + x[2]) / 2, (x[0] - I * x[1]) / 2, 0], [(x[0] + I * x[1]) / 2, (1 - x[2]) / 2, 0], [0, 0, 0]])
rep.check("embedding: the face state of Bloch vector x has qutrit value tr(P01 rho) = 1 for every x -- the qutrit's "
          "certain effect diag(1,1,0) restricts to the UNIT of the face (not proper), so SingletonFaces on the face holds",
          simplify(tr(P01 * face(X))) == 1)
Eq = Matrix([[R(1, 2), R(1, 2), 0], [R(1, 2), R(1, 2), 0], [0, 0, R(1, 3)]])
rep.check("restriction of a qutrit effect to the face is a qubit effect: E restricted = (I + X)/2 block gives sharpEff e1",
          simplify(tr(Eq * face(X)) - sharp([1, 0, 0], X)) == 0)
Uq = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
rep.check("the qutrit unitary X (+) 1 acts on the face as nflip (Ad_X): G of the face is inherited",
          (Uq * face(X) * dag(Uq) - face(NFLIP * X)).applyfunc(simplify) == zeros(3, 3))

# ---------------- D. horizons x effects: dense form with countable stage effects
Hh = lambda v: eye(3) - 2 * Matrix(v) * Matrix(v).T / (Matrix(v).T * Matrix(v))[0]
w = Matrix([R(2, 3), R(1, 3), R(2, 3)])
Rq = Hh(w.cross(Matrix([1, 0, 0]))) * Hh(Z3 - w)
transported = lambda x: sharp(Z3, Rq.T * x)
rep.check("dense form: a rational rotation transports the seed to sharpEff(2/3,1/3,2/3), a rational stage effect of "
          "the d <= 3 tower (s1) -- K-inf-V4 holds with avail = the countable stage effects and G = rational rotations",
          simplify(transported(X) - sharp(w, X)) == 0 and Rq.det() == 1)
rep.note("exact form: K-inf-Trans + K-inf-Seed + PreservesBody give seedOrbit G r = sharpFamily 3 (EffectSpace:401), "
         "and K-inf-V4 puts it inside avail (EffectSpace:374); sharpFamily 3 is uncountable (one effect per unit "
         "vector), so avail cannot be the stage effects of a countably indexed tower (written). M_Q takes avail = all "
         "effects for the exact form and the rational family for the dense form (DenseOrbit:299).")

ok = rep.out()
sys.exit(0 if ok else 1)
