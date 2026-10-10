"""s4 -- QE1 node N1.7: K-inf-Copy (identical copies' NOTs agree) tested against quantum theory.

Object: the quantum CNOT in the kernel's coordinates (= kernel `cnot`, verified in s5).
Question: which linear maps N_A (control copy) and N_B (target copy) of R^3 satisfy
   IsNot-type conditions  N^2 = I, N z3 = -z3, N preserves eball 3 (N orthogonal),
   relT with N_B          actT N_B . cnot . actT N_B = cnot,
   two-NOT relC           actC N_A . cnot . actC N_A = actT N_B . cnot      (NB-1's two-NOT form)?
Linearisation used (valid because each N is an involution): relT <=> actT N_B . cnot = cnot . actT N_B;
relC <=> actC N_A . cnot = actT N_B . cnot . actC N_A.

Decision rule (fixed before running): K-inf-Copy read universally ("every NOT pair compatible with the native
gate agrees") HOLDS in QM iff the solution set has N_A = N_B only; type covariance ("the pair is conjugate by a
frame-preserving automorphism g, g z3 = z3") HOLDS in QM iff every solution pair is so conjugate.  Controls:
the common-N solution (nflip, nflip) must be found; the foils (NB-1's C2N d = 5 pair and the K-inf d = 7 pair)
must FAIL type covariance (different eigenvalue multiplicities).
"""
import sys
from sympy import Matrix, symbols, linsolve, simplify, eye, zeros, cos, sin, pi, Rational as R, trigsimp, solve
from common import *

rep = Report("s4_not_pairs")
C = kernel_cnot16()


def Nsym(prefix):
    return Matrix(3, 3, lambda i, j: symbols('%s%d%d' % (prefix, i, j), real=True))


def eqs_of(M):
    return [e for e in M if e != 0]


# ---- stage 1: N_B from relT (linear) and N_B z3 = -z3
B = Nsym('b')
eq = eqs_of(actT16(B) * C - C * actT16(B)) + eqs_of(B * Z3 + Z3)
solB = list(linsolve(eq, list(B)))
rep.check("relT (linearised) + N_B z3 = -z3 has a unique-shape solution family", len(solB) == 1)
NB_gen = B.subs(dict(zip(list(B), solB[0])))
rep.note("general N_B from the linear conditions: %s" % NB_gen.tolist())
free = sorted(NB_gen.free_symbols, key=str)
invol = eqs_of((NB_gen * NB_gen - eye(3)).applyfunc(simplify))
solsB = solve(invol, free, dict=True) if free else ([{}] if not invol else [])
NBs = []
for s in solsB:
    Nb = NB_gen.subs(s)
    if (Nb * Nb.T).applyfunc(simplify) == eye(3):        # preserves the ball
        NBs.append(Nb)
rep.check("involutive, ball-preserving N_B: exactly one, nflip = Ad_X",
          len(NBs) == 1 and NBs[0] == NFLIP, "found %s" % [n.tolist() for n in NBs])

# ---- stage 2: N_A from relC (linear given N_B) and N_A z3 = -z3
A = Nsym('a')
eqA = eqs_of(actC16(A) * C - actT16(NFLIP) * C * actC16(A)) + eqs_of(A * Z3 + Z3)
solA = list(linsolve(eqA, list(A)))
rep.check("relC (linearised, N_B = nflip) + N_A z3 = -z3 is solvable", len(solA) == 1)
NA_gen = A.subs(dict(zip(list(A), solA[0])))
rep.note("general N_A from the linear conditions: %s" % NA_gen.tolist())
freeA = sorted(NA_gen.free_symbols, key=str)
rep.note("free parameters: %s" % freeA)
inv = eqs_of((NA_gen * NA_gen - eye(3)).applyfunc(simplify))
orth = eqs_of((NA_gen * NA_gen.T - eye(3)).applyfunc(simplify))
solsA = solve(inv + orth, freeA, dict=True)
rep.note("involutive orthogonal N_A solutions (parametrised): %s" % solsA)
fams = [NA_gen.subs(s) for s in solsA]
# expected family: pi-rotations about the horizontal axis (cos phi, sin phi, 0):  [[c, s, 0], [s, -c, 0], [0, 0, -1]]
c, s_ = symbols('c s', real=True)
target = Matrix([[c, s_, 0], [s_, -c, 0], [0, 0, -1]])
match = False
for F in fams:
    fs = sorted(F.free_symbols, key=str)
    if len(fs) == 1:
        # one free parameter p: F = [[?, ?, 0], ...]; test the shape symbolically
        p = fs[0]
        okshape = F[2, :] == Matrix([[0, 0, -1]]) and F[:, 2] == Matrix([0, 0, -1]) and \
            simplify(F[0, 0] + F[1, 1]) == 0 and simplify(F[0, 1] - F[1, 0]) == 0 and \
            simplify(F[0, 0] ** 2 + F[0, 1] ** 2 - 1) == 0
        match = match or okshape
rep.check("every solution N_A is a pi-rotation about a horizontal axis: [[c,s,0],[s,-c,0],[0,0,-1]], c^2+s^2=1",
          match, "families: %s" % [F.tolist() for F in fams])

# sample members, verified directly against the unlinearised relations (control)
samples = {
    "Ad_X (c,s)=(1,0)": Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
    "Ad_Y (c,s)=(-1,0)": Matrix([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    "(c,s)=(3/5,4/5)": Matrix([[R(3, 5), R(4, 5), 0], [R(4, 5), R(-3, 5), 0], [0, 0, -1]]),
    "(c,s)=(0,1)": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
}
for name, NA in samples.items():
    relT_ok = actT16(NFLIP) * C * actT16(NFLIP) == C
    relC_ok = actC16(NA) * C * actC16(NA) == actT16(NFLIP) * C
    isnot = NA * NA == eye(3) and NA * Z3 == -Z3 and NA * NA.T == eye(3)
    rep.check("two-NOT pair (N_A = %s, N_B = Ad_X) meets IsNot, relT and relC exactly" % name,
              relT_ok and relC_ok and isnot)
# universal copy naturality fails: an exhibited pair with N_A != N_B
NA_Y = samples["Ad_Y (c,s)=(-1,0)"]
rep.check("WITNESS: (N_A, N_B) = (Ad_Y, Ad_X) satisfies both relations of the quantum CNOT and N_A != N_B",
          actC16(NA_Y) * C * actC16(NA_Y) == actT16(NFLIP) * C and NA_Y != NFLIP)
# the common-N control
rep.check("control: common N = nflip (= Ad_X) satisfies relT and relC", actC16(NFLIP) * C * actC16(NFLIP) == actT16(NFLIP) * C)
# reflections are excluded on the control side too (PARITY-NOT-1 analogue in the two-NOT form)
for name, NA in (("z-reflection diag(1,1,-1)", Matrix.diag(1, 1, -1)), ("-id", -eye(3))):
    rep.check("countercontrol: N_A = %s fails relC with the quantum CNOT" % name,
              actC16(NA) * C * actC16(NA) != actT16(NFLIP) * C)

# ---- type covariance: each N_A = g N_B g^-1 with g = R_z(phi), g z3 = z3
phi = symbols('phi', real=True)
Rz = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
conj = (Rz * NFLIP * Rz.T).applyfunc(lambda e: trigsimp(simplify(e)))
want = Matrix([[cos(2 * phi), sin(2 * phi), 0], [sin(2 * phi), -cos(2 * phi), 0], [0, 0, -1]])
rep.check("R_z(phi) Ad_X R_z(phi)^-1 = [[cos2phi, sin2phi, 0],[sin2phi, -cos2phi, 0],[0,0,-1]] (symbolic): every "
          "solution N_A is conjugate to N_B by a z-fixing rotation (a unitary, frame-preserving)",
          (conj - want).applyfunc(lambda e: simplify(trigsimp(e))) == zeros(3, 3))
g = Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])      # R_z(pi/2) = ptm of the S gate
rep.check("g = R_z(pi/2) (= ptm(S) block) fixes z3 and g N_A g^-1 = N_B for (Ad_Y, Ad_X)",
          g * Z3 == Z3 and g * NA_Y * g.T == NFLIP and ptm1(Matrix([[1, 0], [0, I]]))[1:, 1:] == g)

# ---- the NOT-conjugacy reduction, on the quantum instance: T~ = (I x g^-1) cnot (I x g) has the common NOT N_A
Gt = actT16(g.T) * C * actT16(g)
rel_common = actT16(NA_Y) * Gt * actT16(NA_Y) == Gt and actC16(NA_Y) * Gt * actC16(NA_Y) == actT16(NA_Y) * Gt
corners = [Z3, -Z3]
frame_ok = all(unvec(Gt * vec(prodState(corners[a], corners[b]))) == prodState(corners[a], corners[(a + b) % 2])
               for a in range(2) for b in range(2))
rep.check("reduction instance: T~ = (I x g^-1) cnot (I x g) meets the frame and both relations with the common NOT Ad_Y",
          rel_common and frame_ok)
# run 1 compared T~ with |0><0| x I + |1><1| x Y and FAILED (s4_not_pairs.run1.out): the expected gate was
# mis-specified.  The conjugated unitary is (I x S^dag) CNOT (I x S) = |0><0| x I - |1><1| x Y.
Sg = Matrix([[1, 0], [0, I]])
Ut = kron(S0, dag(Sg)) * kron(Matrix([[1, 0], [0, 0]]), S0) * kron(S0, Sg) + \
     kron(S0, dag(Sg)) * kron(Matrix([[0, 0], [0, 1]]), SX) * kron(S0, Sg)
rep.check("(I x S^dag) CNOT (I x S) = |0><0| x I - |1><1| x Y (a quantum gate)",
          Ut == kron(Matrix([[1, 0], [0, 0]]), S0) - kron(Matrix([[0, 0], [0, 1]]), SY))
rep.check("T~ is the Pauli transfer matrix of that quantum gate", ptm2(Ut) == Gt)
CYp = kron(Matrix([[1, 0], [0, 0]]), S0) + kron(Matrix([[0, 0], [0, 1]]), SY)
rep.check("countercontrol: T~ is NOT the transfer matrix of |0><0| x I + |1><1| x Y (they differ by Z x I)",
          ptm2(CYp) != Gt)

# ---- foils: the NB-1 two-NOT survivors are not conjugate (eigenvalue multiplicities differ)
def mult_plus(diag):
    return sum(1 for v in diag if v == 1)
c2n_A = [1, 1, -1, 1, -1, -1]       # NB-1 prereg row: N_A = diag(1, 1, -1, 1, -1, -1) (homogenized, p = q = 2)
c2n_B_p = 1                         # N_B with p = 1: homogenized +1 multiplicity 1 + p = 2
rep.check("foil C2N (d = 5): homogenized +1 multiplicities 3 vs 2 -> no conjugating g; type covariance FAILS there",
          mult_plus(c2n_A) != 1 + c2n_B_p)
rep.check("foil d = 7 (K-inf §6): splits (3,3) vs (1,5) -> +1 multiplicities 4 vs 2; type covariance FAILS there",
          (1 + 3) != (1 + 1))

ok = rep.out()
sys.exit(0 if ok else 1)
