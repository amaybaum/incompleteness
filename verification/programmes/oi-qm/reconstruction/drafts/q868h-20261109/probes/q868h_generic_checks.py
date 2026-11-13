"""Q-868-H unit 1: exact checks on GENERIC mathematical objects only.

WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).

Scope (owner rule, #868 c.6742050189; #1210 c.6739250392; #1211 c.6739843458):
no computation on an OI mechanism.  Nothing here simulates, enumerates or
encodes an OI update rule, a U' encoding, a coupling, a record law or a native
preparation.  Every object below is a 2x2 / 4x4 complex matrix, a Pauli
correlation table, or a vector of +-1 values.  Which tables the native
construction reaches is decided by hand in Q868H-UNIT1.md; these checks only
control the matrix facts that paper analysis then cites.

Run: python3 -I q868h_generic_checks.py   (sympy 1.14.0).  Imports no earlier probe.
Every check that asserts a failure carries an exact nonzero witness.
"""
import itertools
import sys

import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
P = {"0": I2, "x": X, "y": Y, "z": Z}
AX = ["x", "y", "z"]


def kron(a, b):
    return sp.kronecker_product(a, b)


def table_op(T):
    """rho_T = 1/4 sum_{a,b in {0,x,y,z}} T[a,b] sigma_a (x) sigma_b."""
    M = sp.zeros(4, 4)
    for (a, b), v in T.items():
        M += v * kron(P[a], P[b])
    return M / 4


def min_eig(M):
    ev = M.eigenvals()
    return min(sp.nsimplify(sp.re(sp.simplify(e))) for e in ev)


results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((" :: " + detail) if detail else ""))


# ---------------------------------------------------------------- A: named tables
T_A1 = {("0", "0"): 1, ("x", "x"): 1, ("z", "z"): 1}  # (I+XX+ZZ)/4
T_A2 = {("0", "0"): 1, ("x", "x"): 1, ("y", "y"): 1, ("z", "z"): 1}  # (I+XX+YY+ZZ)/4
T_A3 = {("0", "0"): 1, ("x", "x"): 1, ("y", "y"): -1, ("z", "z"): 1}  # Phi+ table
r1, r2, r3 = table_op(T_A1), table_op(T_A2), table_op(T_A3)
check("A1 (I+XX+ZZ)/4 has minimum eigenvalue -1/4", min_eig(r1) == sp.Rational(-1, 4), str(r1.eigenvals()))
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
check("A2 (I+XX+YY+ZZ)/4 equals SWAP/2, minimum eigenvalue -1/2",
      r2 == SWAP / 2 and min_eig(r2) == sp.Rational(-1, 2), str(r2.eigenvals()))
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
check("A3 (I+XX-YY+ZZ)/4 equals |Phi+><Phi+|", sp.simplify(r3 - phi * phi.T) == sp.zeros(4, 4))

# ------------------------------------------- B: sign rule over 48 signed permutations
# T = (I + sum_a s_a sigma_a (x) sigma_{pi(a)})/4.  Claim: PSD iff s_x s_y s_z = -sgn(pi);
# PSD cases are rank 1; non-PSD cases have minimum eigenvalue -1/2.
def sgn(perm):
    s = 1
    p = list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


ok_rule, ok_rank, ok_neg, n = True, True, True, 0
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        T = {("0", "0"): 1}
        for i, a in enumerate(AX):
            T[(a, AX[perm[i]])] = signs[i]
        M = table_op(T)
        m = min_eig(M)
        psd = m >= 0
        pred = signs[0] * signs[1] * signs[2] == -sgn(perm)
        ok_rule &= (psd == pred)
        if psd:
            ok_rank &= (M.rank() == 1)
        else:
            ok_neg &= (m == sp.Rational(-1, 2))
        n += 1
check("B1 48 signed-permutation tables: PSD iff s_x s_y s_z = -sgn(pi)", ok_rule, f"{n} tables")
check("B2 the PSD ones are rank 1 (pure)", ok_rank)
check("B3 the non-PSD ones have minimum eigenvalue exactly -1/2", ok_neg)

# two correlators in a partial-permutation pattern, zero marginals: never PSD, minimum -1/4
ok4, n4 = True, 0
for perm in itertools.permutations(range(3)):
    for keep in [(0, 1), (0, 2), (1, 2)]:
        for signs in itertools.product([1, -1], repeat=2):
            T = {("0", "0"): 1}
            for k, i in enumerate(keep):
                T[(AX[i], AX[perm[i]])] = signs[k]
            ok4 &= (min_eig(table_op(T)) == sp.Rational(-1, 4))
            n4 += 1
check("B4 every two-correlator zero-marginal signed table has minimum eigenvalue -1/4 (never PSD)", ok4, f"{n4} tables")

# ---------------------------------- C: full-ball product values of zero-marginal tables
a1, a2, a3, b1, b2, b3 = sp.symbols("a1 a2 a3 b1 b2 b3", real=True)
avec, bvec = sp.Matrix([a1, a2, a3]), sp.Matrix([b1, b2, b3])


def eff(v):
    return (I2 + v[0] * X + v[1] * Y + v[2] * Z) / 2


def pairval(M):
    return sp.expand(sp.simplify((M * kron(eff(avec), eff(bvec))).trace()))


def corr_block(T):
    C = sp.zeros(3, 3)
    for i, a in enumerate(AX):
        for j, b in enumerate(AX):
            C[i, j] = T.get((a, b), 0)
    return C


ok_formula, ok_norm = True, True
cases = 0
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        for keep in [(0, 1, 2), (0, 1), (0, 2), (1, 2)]:
            T = {("0", "0"): 1}
            for i in keep:
                T[(AX[i], AX[perm[i]])] = signs[i]
            C = corr_block(T)
            pv = pairval(table_op(T))
            ok_formula &= sp.simplify(pv - (1 + (avec.T * C * bvec)[0]) / 4) == 0
            # |C^T a|^2 <= |a|^2, with equality for a full permutation
            d = sp.expand((C.T * avec).dot(C.T * avec) - avec.dot(avec))
            ok_norm &= (d == 0) if len(keep) == 3 else (sp.expand(-d) in [a1**2, a2**2, a3**2])
            cases += 1
check("C1 zero-marginal tables: product value = (1 + a^T C b)/4 on symbolic a, b", ok_formula, f"{cases} tables")
check("C2 signed (partial) permutation blocks: |C^T a| <= |a| exactly (hence 1 + a^T C b >= 1 - |a||b| >= 0 on the ball)", ok_norm)
# countercontrol: two entries in one row, |C| = sqrt 2, negative on a ball product
T_bad = {("0", "0"): 1, ("x", "x"): 1, ("x", "z"): 1}
val = pairval(table_op(T_bad)).subs({a1: -1, a2: 0, a3: 0, b1: 1 / sp.sqrt(2), b2: 0, b3: 1 / sp.sqrt(2)})
check("C3 control: (I+XX+XZ)/4 is negative on a full-ball product, value (1-sqrt2)/4",
      sp.simplify(val - (1 - sp.sqrt(2)) / 4) == 0 and val < 0, str(sp.nsimplify(val)))

# -------------------------------------------------- D: quantum CNOT on Pauli products
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control = first factor


def conj(a, b):
    return CN * kron(P[a], P[b]) * CN.T


expect = {("x", "0"): (1, "x", "x"), ("0", "z"): (1, "z", "z"), ("y", "0"): (1, "y", "x"),
          ("0", "y"): (1, "z", "y"), ("z", "0"): (1, "z", "0"), ("0", "x"): (1, "0", "x"),
          ("y", "y"): (-1, "x", "z")}
ok = all(conj(a, b) == s * kron(P[c], P[d]) for (a, b), (s, c, d) in expect.items())
check("D1 CNOT: XI->XX, IZ->ZZ, YI->YX, IY->ZY, ZI->ZI, IX->IX, YY->-XZ", ok)
check("D2 control: YY -> +XZ is false", conj("y", "y") != kron(X, Z))

# ------------------------------------------------------- E: partial transpose on A
syms = {(a, b): sp.Symbol(f"t_{a}{b}", real=True) for a in "0xyz" for b in "0xyz"}
syms[("0", "0")] = sp.Integer(1)
R = table_op(syms)


def pt_A(M):
    out = sp.zeros(4, 4)
    for i, j, k, l in itertools.product(range(2), repeat=4):
        out[2 * j + k, 2 * i + l] = M[2 * i + k, 2 * j + l]
    return out


flipped = {(a, b): (-v if a == "y" else v) for (a, b), v in syms.items()}
check("E1 partial transpose on wing A = sign flip of every T_{y,b} (generic symbolic table)",
      sp.simplify(pt_A(R) - table_op(flipped)) == sp.zeros(4, 4))
check("E2 partial transpose of the Phi+ table is SWAP/2", sp.simplify(pt_A(r3) - SWAP / 2) == sp.zeros(4, 4))

# ------------------------------- F: comparator for the two sequences of section 7 (QC-2)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
S = sp.Matrix([[1, 0], [0, sp.I]])
k00 = sp.Matrix([1, 0, 0, 0])
out1 = CN * kron(H, I2) * k00
out2 = CN * kron(H * S, I2) * k00
check("F1 comparator: CNOT(H x I)|00> = Phi+", sp.simplify(out1 - phi) == sp.zeros(4, 1))
check("F2 comparator: CNOT(HS x I)|00> = Phi+ (S|0> = |0>)", sp.simplify(out2 - phi) == sp.zeros(4, 1))
check("F3 control: the two sequences differ on |10> (F2 is not an identity of maps)",
      sp.simplify(CN * kron(H * S, I2) * sp.Matrix([0, 0, 1, 0]) - CN * kron(H, I2) * sp.Matrix([0, 0, 1, 0])) != sp.zeros(4, 1))

# -------------------------------------------------------------- G: Mermin-Peres
check("G1 (X(x)Z)(Z(x)X)(Y(x)Y) = +I", kron(X, Z) * kron(Z, X) * kron(Y, Y) == sp.eye(4))
check("G2 (X(x)X)(Z(x)Z)(Y(x)Y) = -I", kron(X, X) * kron(Z, Z) * kron(Y, Y) == -sp.eye(4))
check("G3 the three operators in each line commute pairwise",
      all(A * B == B * A for A, B in itertools.combinations([kron(X, Z), kron(Z, X), kron(Y, Y)], 2)) and
      all(A * B == B * A for A, B in itertools.combinations([kron(X, X), kron(Z, Z), kron(Y, Y)], 2)))

# ------------------------------------------- H: completions of {I,X,Z}-only sub-tables
okH, okHc = True, True
for s, t in itertools.product([1, -1], repeat=2):
    good1 = table_op({("0", "0"): 1, ("x", "x"): s, ("z", "z"): t, ("y", "y"): -s * t})
    good2 = table_op({("0", "0"): 1, ("x", "z"): s, ("z", "x"): t, ("y", "y"): s * t})
    bad1 = table_op({("0", "0"): 1, ("x", "x"): s, ("z", "z"): t, ("y", "y"): s * t})
    okH &= min_eig(good1) >= 0 and min_eig(good2) >= 0
    okHc &= min_eig(bad1) == sp.Rational(-1, 2)
check("H1 every sign pattern of {XX,ZZ} or {XZ,ZX} has a PSD completion (YY = -st, resp. +st)", okH)
check("H2 control: the opposite YY sign gives minimum eigenvalue -1/2", okHc)

# ------------------------------- I: cube-vertex mixtures (local deterministic assignments)
# A deterministic assignment v_A, v_B in {+-1}^3 gives the product table T_ab = v_A[a] v_B[b].
# Its value on a product of Pauli sharp effects (1 + e v_A[a])/2 (1 + f v_B[b])/2 is 0 or 1.
def mixture_table(assignments):
    T = {}
    w = sp.Rational(1, len(assignments))
    for vA, vB in assignments:
        ext_A = {"0": 1, "x": vA[0], "y": vA[1], "z": vA[2]}
        ext_B = {"0": 1, "x": vB[0], "y": vB[1], "z": vB[2]}
        for a in "0xyz":
            for b in "0xyz":
                T[(a, b)] = T.get((a, b), 0) + w * ext_A[a] * ext_B[b]
    return {k: v for k, v in T.items() if v != 0}


# uniform over v_Ax, v_Az, v_Ay, v_By independent, with v_Bx = v_Ax, v_Bz = v_Az
asg = [((x, ya, z), (x, yb, z)) for x, ya, z, yb in itertools.product([1, -1], repeat=4)]
check("I1 (I+XX+ZZ)/4 is the uniform mixture of 16 products of cube vertices (Pauli-product LHV)",
      mixture_table(asg) == T_A1)
asg2 = [((x, y, z), (x, y, z)) for x, y, z in itertools.product([1, -1], repeat=3)]
check("I2 SWAP/2 = (I+XX+YY+ZZ)/4 is the uniform mixture of 8 products of equal cube vertices",
      mixture_table(asg2) == T_A2)
okI = True
for vA, vB in asg2:
    for a, b in itertools.product(range(3), repeat=2):
        for e, f in itertools.product([1, -1], repeat=2):
            v = sp.Rational(1, 4) * (1 + e * vA[a]) * (1 + f * vB[b])
            okI &= v in (0, 1)
check("I3 a product of cube vertices gives 0 or 1 on every product of Pauli sharp effects", okI)
check("I4 control: the equal-vertex mixture has T_yy = +1, not the Phi+ value -1",
      mixture_table(asg2).get(("y", "y")) == 1 and T_A3[("y", "y")] == -1)

# ---------------------------------------------------------- J: body memberships
r = sp.Matrix([1, 0, 1])
check("J1 Bloch (1,0,1): in the cube, outside the octahedron and outside the ball",
      max(abs(c) for c in r) == 1 and sum(abs(c) for c in r) == 2 and r.dot(r) == 2)

nf = sum(1 for _, ok in results if not ok)
print(f"\n{len(results)} checks, {nf} failures")
sys.exit(1 if nf else 0)
