"""s6 -- QE1 node N1.9b: the scope of DIM-1's native-gate relations inside two-qubit quantum theory.

The quantum gates whose conjugation acts as the classical CNOT on the four corner product states (DIM-1's `frame`)
are exactly U = CNOT . D with D diagonal unitary (written: Ad_U |ab><ab| = |a,a+b><a,a+b| for all a, b forces
U|ab> = phase . |a, a+b>).  Every such U is two-sided positive (unitary) and entangling (U|+>|0> =
(d00|00> + d10|11>)/sqrt2).  Question: for which D do the NOT relations hold
   (common)   exists N: IsNot(N) and relT(N) and relC(N, N)      -- DIM-1's NativeGate relations
   (two-NOT)  exists N_A, N_B: relT(N_B) and relC(N_A, N_B)      -- NB-1's two-NOT form
with N ranging over ALL linear maps of R^3 (unitary-induced, antiunitary-induced or neither).

Decision rule (fixed before running): the native-gate premise holds in QM "for every frame-class gate" iff every
sampled D admits a common N; otherwise it holds only existentially, and the first D without any solution is the
witness.  Control: D = I (the kernel's cnot) must admit the common N = Ad_X.
"""
import sys, itertools
from sympy import Matrix, I, Rational as R, symbols, linsolve, solve, simplify, eye, zeros, sqrt
from common import *

rep = Report("s6_gate_class")
P0 = Matrix([[1, 0], [0, 0]]); P1 = Matrix([[0, 0], [0, 1]])
CNOT = kron(P0, S0) + kron(P1, SX)


def gate(D):
    return CNOT * Matrix.diag(*D)


def eqs(M):
    return [e for e in M if e != 0]


def Nsym(p):
    return Matrix(3, 3, lambda i, j: symbols('%s%d%d' % (p, i, j), real=True))


def isnot_solutions(Ngen):
    """all involutive orthogonal specialisations of a linear family Ngen (free symbols solved)."""
    fs = sorted(Ngen.free_symbols, key=str)
    conds = eqs((Ngen * Ngen - eye(3)).applyfunc(simplify)) + eqs((Ngen * Ngen.T - eye(3)).applyfunc(simplify))
    if not fs:
        return [Ngen] if not conds else []
    sols = solve(conds, fs, dict=True)
    return [Ngen.subs(s) for s in sols]


def common_N(T):
    """relT is linear in N (given N^2 = I); relC with the same N is bilinear, so it is imposed afterwards, exactly,
    on the involutive orthogonal members of the relT family (solving any remaining free parameters)."""
    N = Nsym('n')
    sol = list(linsolve(eqs(actT16(N) * T - T * actT16(N)) + eqs(N * Z3 + Z3), list(N)))
    if not sol:
        return []
    out = []
    for Nc in isnot_solutions(N.subs(dict(zip(list(N), sol[0])))):
        cond = eqs((actC16(Nc) * T - actT16(Nc) * T * actC16(Nc)).applyfunc(simplify))
        fs = sorted(Nc.free_symbols, key=str)
        if not cond:
            out.append(Nc)
        elif fs:
            for sp in solve(cond, fs, dict=True):
                out.append(Nc.subs(sp))
    return out


def two_not(T):
    B = Nsym('b')
    solB = list(linsolve(eqs(actT16(B) * T - T * actT16(B)) + eqs(B * Z3 + Z3), list(B)))
    out = []
    if not solB:
        return out
    for NB in isnot_solutions(B.subs(dict(zip(list(B), solB[0])))):
        A = Nsym('a')
        solA = list(linsolve(eqs(actC16(A) * T - actT16(NB) * T * actC16(A)) + eqs(A * Z3 + Z3), list(A)))
        if solA:
            for NA in isnot_solutions(A.subs(dict(zip(list(A), solA[0])))):
                out.append((NA, NB))
    return out


corners = [Z3, -Z3]


def frame_ok(T):
    return all(unvec(T * vec(prodState(corners[a], corners[b]))) == prodState(corners[a], corners[(a + b) % 2])
               for a in range(2) for b in range(2))


phases = [1, I, -1, -I]
rows = []
n_common = n_two_only = n_none = 0
first_none = None
for d01, d10, d11 in itertools.product(phases, repeat=3):
    D = (1, d01, d10, d11)
    T = ptm2(gate(D))
    assert frame_ok(T)
    cN = common_N(T)
    tN = two_not(T) if not cN else None
    if cN:
        n_common += 1
        tag = "common N: %s" % [n.tolist() for n in cN][:2]
    elif tN:
        n_two_only += 1
        tag = "two-NOT only: %d pair families" % len(tN)
    else:
        n_none += 1
        tag = "NO NOT pair"
        if first_none is None:
            first_none = D
    rows.append("D = diag%s : %s" % (str(D), tag))

for r in rows:
    rep.note(r)
rep.check("all 64 sampled frame-class gates satisfy DIM-1's frame exactly", True)
rep.check("control: D = I (the kernel's cnot) admits the common N = Ad_X",
          any(n == NFLIP for n in common_N(ptm2(gate((1, 1, 1, 1))))))
rep.note("counts over the 64 Clifford-phase gates: common N %d, two-NOT only %d, none %d" % (n_common, n_two_only, n_none))
rep.check("the relations do NOT hold for every frame-class quantum gate (some sampled D admits no common N)",
          n_two_only + n_none > 0)

# the named witness: CNOT followed by S on the control = CNOT . diag(1,1,i,i)
Dw = (1, 1, I, I)
Tw = ptm2(gate(Dw))
Uw = gate(Dw)
SI = kron(Matrix([[1, 0], [0, I]]), S0)
rep.check("witness gate (S x I) CNOT = CNOT . diag(1,1,i,i)", SI * CNOT == Uw)
rep.check("witness: frame holds", frame_ok(Tw))
img = Uw * kron(Matrix([[1], [1]]) / sqrt(2), Matrix([[1], [0]]))
redA = Matrix(2, 2, lambda i, j: sum(img[2 * i + k] * img[2 * j + k].conjugate() for k in range(2)))
rep.check("witness: entangling (reduced state of U|+>|0> is I/2, maximally mixed)", redA.applyfunc(simplify) == eye(2) / 2)
cw = common_N(Tw)
tw = two_not(Tw)
rep.check("WITNESS: (S x I) CNOT admits NO common NOT (no linear N of R^3 with IsNot, relT, relC)", cw == [])
rep.note("two-NOT pairs for the witness: %s" % [(a.tolist(), b.tolist()) for a, b in tw])
rep.check("WITNESS: (S x I) CNOT admits no two-NOT pair whose control NOT has det +1 (no unitary-induced pair)",
          all(simplify(a.det()) != 1 for a, b in tw))

# a non-Clifford member of the common-N family: conjugate (cnot, Ad_X) by R_z(phi) x R_z(phi), cos phi = 3/5
u = (3 + 4 * I) / 5
Rz = Matrix([[1, 0], [0, u]])
Uphi = kron(Rz, Rz) * CNOT * kron(dag(Rz), dag(Rz))
rep.check("R_z(phi)xR_z(phi) CNOT R_z(phi)^dag x R_z(phi)^dag = CNOT . diag(1, 1, u, conj(u)), u = (3+4i)/5",
          (Uphi - gate((1, 1, u, u.conjugate()))).applyfunc(simplify) == zeros(4, 4))
cphi = common_N(ptm2(Uphi))
Nphi = ptm1(Rz)[1:, 1:] * NFLIP * ptm1(Rz)[1:, 1:].T
rep.check("its common NOT is the rotated NOT R_z(phi) Ad_X R_z(phi)^-1 (exact rational)",
          any((n - Nphi).applyfunc(simplify) == zeros(3, 3) for n in cphi), "N = %s" % Nphi.tolist())

# ---- the general statement, symbolically (all phases).  By PARITY-NOT-1 (`piRotation_three`, kernel), a common N
# with IsNot and both relations at d = 3 is a pi-rotation; with N z3 = -z3 its axis is horizontal, so N = Ad_V,
# V = [[0, 1/w], [w, 0]], |w| = 1.  Ad_A = Ad_B iff A = lambda B with |lambda| = 1.  On the unit circle conj(x) = 1/x.
a_, b_, c_, w_, lam_, mu_ = symbols('a b c w lam mu', nonzero=True)
Dg = Matrix.diag(1, a_, b_, c_)
Ug = CNOT * Dg
V = Matrix([[0, 1 / w_], [w_, 0]])
relT_eq = list(kron(S0, V) * Ug * kron(S0, V) - lam_ * Ug)
relC_eq = list(kron(V, S0) * Ug * kron(V, S0) - mu_ * kron(S0, V) * Ug)
sol = solve([e for e in relT_eq + relC_eq if e != 0], [a_, b_, c_, lam_, mu_], dict=True)
rep.note("symbolic solutions (d00 = 1): %s" % sol)
fam_ok = len(sol) > 0 and all(
    simplify(sp[lam_] ** 2 - 1) == 0 and simplify(sp[mu_] ** 2 - 1) == 0 and
    simplify(sp[a_] - sp[lam_]) == 0 and simplify(sp[b_] - sp[mu_] * w_) == 0 and
    simplify(sp[c_] - sp[mu_] * sp[lam_] / w_) == 0 for sp in sol)
rep.check("GENERAL (symbolic): CNOT.diag(1,a,b,c) has a common NOT Ad_V, V = [[0,1/w],[w,0]], iff "
          "a = lam, b = mu w, c = mu lam / w with lam, mu in {+1,-1}; i.e. U = CNOT . diag(1,1,u,conj u) . (I x Z)^k",
          fam_ok)

ok = rep.out()
sys.exit(0 if ok else 1)
