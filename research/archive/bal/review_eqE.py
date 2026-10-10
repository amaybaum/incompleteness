"""Coordinator's independent spot-check of two EQ-E claims (exact; written without EQ-E's code).

R1  DIM-1's kernel cnot (transcribed in relt_common, from CompositeDimension §K) equals the Pauli transfer matrix of
    the quantum CNOT (control = first factor), in the convention omega[mu][nu] = tr(rho sigma_mu (x) sigma_nu).
R2  With N_B = Ad_X = nflip on the target, relT(N_B) holds, and the two-NOT control relation
        actC N_A (G (actC N_A w)) = actT N_B (G w)
    holds for N_A = [[c, s, 0], [s, -c, 0], [0, 0, -1]] for every (c, s) on the unit circle (rational parametrization),
    in particular for N_A = Ad_Y = diag(-1, 1, -1); and N_A = Ad_Z-type / -id fail it (countercontrol).
R3  U = (S (x) I) CNOT: its transfer matrix has the frame and is positive (unitary), but no pair (N_A, N_B) of
    orthogonal involutions of R^3 with N z = -z satisfies relT(N_B) and the two-NOT relC.  (EQ-E claims more: no linear
    pair at all; this spot-check covers the IsNot candidates, parametrized exactly.)
"""
import sys
from sympy import Matrix, I, Rational as R, eye, zeros, symbols, expand, simplify, diag, cancel
from relt_common import dim1_cnot, homMap, gate_from_fun, apply, prod, frame

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


S0 = Matrix([[1, 0], [0, 1]])
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])
P = [S0, SX, SY, SZ]


def kron(A, B):
    out = zeros(A.shape[0] * B.shape[0], A.shape[1] * B.shape[1])
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            out[i * B.shape[0]:(i + 1) * B.shape[0], j * B.shape[1]:(j + 1) * B.shape[1]] = A[i, j] * B
    return out


def transfer(U):
    """16x16 matrix on vec(omega) (index 4 mu + nu): omega' = T omega for rho -> U rho U^dag"""
    T = zeros(16, 16)
    Ud = U.H
    for mu in range(4):
        for nu in range(4):
            Omn = Ud * kron(P[mu], P[nu]) * U
            for a in range(4):
                for b in range(4):
                    T[4 * mu + nu, 4 * a + b] = simplify((kron(P[a], P[b]) * Omn).trace() / 4)
    return T


CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Tc = transfer(CNOT)
check("R1 kernel cnot == Pauli transfer matrix of the quantum CNOT (control first)", (Tc - dim1_cnot()).is_zero_matrix)


def actT(N):
    H = homMap(N)
    return gate_from_fun(lambda w: w * H.T, 4)


def actC(N):
    H = homMap(N)
    return gate_from_fun(lambda w: H * w, 4)


def relT(G, NB):
    A = actT(NB)
    return (A * G * A - G).applyfunc(cancel).is_zero_matrix


def relC2(G, NA, NB):
    C = actC(NA)
    A = actT(NB)
    return (C * G * C - A * G).applyfunc(cancel).is_zero_matrix


nflip = diag(1, -1, -1)
m = symbols("m")
c, s = (1 - m ** 2) / (1 + m ** 2), 2 * m / (1 + m ** 2)
NAc = Matrix([[c, s, 0], [s, -c, 0], [0, 0, -1]])
G = dim1_cnot()
check("R2 relT(nflip) for cnot", relT(G, nflip))
check("R2 two-NOT relC holds for N_A on the whole circle (symbolic m), N_B = nflip", relC2(G, NAc, nflip))
check("R2 instance N_A = Ad_Y = diag(-1, 1, -1) (circle point c = -1, s = 0), N_A != N_B", relC2(G, diag(-1, 1, -1), nflip))
check("R2 countercontrols: N_A = diag(1, 1, -1) and N_A = -id fail", not relC2(G, diag(1, 1, -1), nflip)
      and not relC2(G, -eye(3), nflip))

# R3: U = (S (x) I) CNOT
Sg = Matrix([[1, 0], [0, I]])
U = kron(Sg, S0) * CNOT
Tu = transfer(U)
z3 = Matrix([0, 0, 1])
check("R3 (S(x)I)CNOT: frame holds on the z-corners", frame(Tu, z3))
check("R3 (S(x)I)CNOT: transfer matrix is real", all(v.is_real for v in Tu))
# IsNot candidates on R^3 with N z = -z are N = Rm (+) (-1), Rm an orthogonal involution of the plane:
# Rm in {I, -I} or a reflection F(m) = [[c, s], [s, -c]] (m rational parameter, plus the member m = oo: diag(-1, 1)).
from sympy import solve, numer, together


def F(mm):
    if mm == "oo":
        return diag(-1, 1, -1)
    cc, ss = (1 - mm ** 2) / (1 + mm ** 2), 2 * mm / (1 + mm ** 2)
    return Matrix([[cc, ss, 0], [ss, -cc, 0], [0, 0, -1]])


def solve_family(cond_matrix_fn, var):
    """values of var (as a list of concrete N) for which the symbolic family satisfies the identity"""
    Msym = cond_matrix_fn(F(var))
    eqs = [numer(together(cancel(e))) for e in Msym if cancel(e) != 0]
    if not eqs:
        return "identically"
    sols = solve(eqs, var, dict=True)
    return [d[var] for d in sols if d[var].is_real]


tt, mm2 = symbols("tt mm2")
fixed = [("diag(1,1,-1)", diag(1, 1, -1)), ("-id", -eye(3)), ("F(oo)=diag(-1,1,-1)", F("oo"))]
relT_fn = lambda NB: actT(NB) * Tu * actT(NB) - Tu
NB_list = [(nm, N) for nm, N in fixed if relT(Tu, N)]
fam = solve_family(relT_fn, tt)
print("     relT: fixed members admissible:", [nm for nm, _ in NB_list], "; reflection family F(t):", fam)
if fam == "identically":
    NB_list.append(("F(t) all t", None))
else:
    NB_list += [(f"F({v})", F(v)) for v in fam]
pairs = []
for nb_name, NB in NB_list:
    if NB is None:
        continue
    for na_name, NA in fixed:
        if relC2(Tu, NA, NB):
            pairs.append((na_name, nb_name))
    famA = solve_family(lambda NA: actC(NA) * Tu * actC(NA) - actT(NB) * Tu, mm2)
    if famA == "identically":
        pairs.append(("F(m) all m", nb_name))
    else:
        pairs += [(f"F({v})", nb_name) for v in famA]
print("     admissible (N_A, N_B) pairs among IsNot candidates:", pairs)
check("R3 (S(x)I)CNOT: no IsNot pair (N_A, N_B) satisfies relT(N_B) and the two-NOT relC "
      f"(relT-admissible N_B: {[nm for nm, _ in NB_list]})", pairs == [])
# the same solver finds the circle for CNOT (control for the solver)
famA_c = solve_family(lambda NA: actC(NA) * G * actC(NA) - actT(nflip) * G, mm2)
check(f"R3 solver control: for CNOT with N_B = nflip the reflection family is admissible identically ({famA_c})",
      famA_c == "identically")
# control: CNOT itself admits the pair (nflip, nflip)
check("R3 control: CNOT admits (nflip, nflip)", relT(G, nflip) and relC2(G, nflip, nflip))

npass = sum(1 for _, cc in checks if cc)
print(f"review_eqE: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
