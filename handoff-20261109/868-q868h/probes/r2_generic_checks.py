"""Q-868-H unit 1, revision r2: exact checks on GENERIC mathematical objects only.

WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).

Scope (owner rule, #868 c.6742050189; #1210 c.6739250392; #1211 c.6739843458):
no computation on an OI mechanism.  Nothing here simulates, enumerates or
encodes an OI update rule, a U' encoding, a coupling, a record law, a cell swap
or a native preparation.  Every object is a 2x2 / 4x4 complex matrix, a Pauli
correlation table or a Bloch vector.  Which tables the native construction
reaches (Lemma P, E3, E4) is decided by hand in Q868H-UNIT1.md; these checks
control only the comparator-side and table facts that the r2 text cites.

Run: python3 -I r2_generic_checks.py   (sympy 1.14.0).
Imports no earlier probe (only sympy, itertools, sys).
Every check asserting a failure carries an exact witness; controls are marked.
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
LAB = ["0", "x", "y", "z"]
HAD = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
SPH = sp.Matrix([[1, 0], [0, sp.I]])
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control = A (first factor)


def kron(a, b):
    return sp.kronecker_product(a, b)


def simp(M):
    return M.applyfunc(lambda e: sp.nsimplify(sp.simplify(e)))


def table_op(T):
    """rho_T = 1/4 sum T[a,b] sigma_a (x) sigma_b."""
    M = sp.zeros(4, 4)
    for (a, b), v in T.items():
        M += v * kron(P[a], P[b])
    return M / 4


def table_of(rho):
    """T[a,b] = Tr(rho sigma_a (x) sigma_b); zero entries dropped."""
    T = {}
    for a, b in itertools.product(LAB, repeat=2):
        v = sp.nsimplify(sp.simplify((rho * kron(P[a], P[b])).trace()))
        if v != 0:
            T[(a, b)] = v
    return T


def eigs(M):
    """All eigenvalues, repeated by algebraic multiplicity, sorted ascending."""
    out = []
    for e, m in M.eigenvals().items():
        out += [sp.nsimplify(sp.simplify(e))] * m
    return sorted(out, key=lambda e: float(e))


def min_eig(M):
    return eigs(M)[0]


def bloch(rho2):
    return tuple(sp.nsimplify(sp.simplify((rho2 * P[a]).trace())) for a in AX)


def ptrace_A(rho):
    """Trace out the first factor of a 4x4 operator."""
    R = sp.zeros(2, 2)
    for i, j in itertools.product(range(2), repeat=2):
        R[i, j] = rho[i, j] + rho[2 + i, 2 + j]
    return R


def proj(state):
    return state * state.H


results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail != "" else ""))


ket0 = sp.Matrix([1, 0])
ket00 = kron(ket0, ket0)

# ------------------------------------------------- R1: comparator side of Lemma P + H_A; CNOT
T_phi = {("0", "0"): 1, ("x", "x"): 1, ("y", "y"): -1, ("z", "z"): 1}
T_swap = {("0", "0"): 1, ("x", "x"): 1, ("y", "y"): 1, ("z", "z"): 1}
phi = simp(CNOT * kron(HAD, I2) * ket00)
rho_phi = simp(proj(phi))
check("R1a comparator: CNOT (H (x) I)|00> has table (I+XX-YY+ZZ)/4 (the Phi+ table)",
      table_of(rho_phi) == T_phi, table_of(rho_phi))
check("R1b the Phi+ table is PSD (eigenvalues 0,0,0,1)", eigs(table_op(T_phi)) == [0, 0, 0, 1],
      eigs(table_op(T_phi)))
check("R1c control: SWAP/2 = (I+XX+YY+ZZ)/4 has minimum eigenvalue -1/2", min_eig(table_op(T_swap)) == sp.Rational(-1, 2))
SWAP = (kron(I2, I2) + kron(X, X) + kron(Y, Y) + kron(Z, Z)) / 2
check("R1d SWAP = (II+XX+YY+ZZ)/2 is the swap, with eigenvalues -1,1,1,1; so every state has <XX>+<YY>+<ZZ> <= 1",
      SWAP == sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]) and eigs(SWAP) == [-1, 1, 1, 1],
      eigs(SWAP))

# ------------------------------------------------- R2: B2 property-level witness of QC =/=> (C)
c8, s8 = sp.cos(sp.pi / 8), sp.sin(sp.pi / 8)
psiB = sp.Matrix([c8, s8])
rho_prod = simp(proj(kron(ket0, psiB)))
rB = bloch(ptrace_A(rho_prod))
check("R2a |0>(x)(cos(pi/8)|0>+sin(pi/8)|1>) is a quantum state: Hermitian, trace 1, eigenvalues 0,0,0,1",
      rho_prod == rho_prod.H and sp.simplify(rho_prod.trace()) == 1 and eigs(rho_prod) == [0, 0, 0, 1])
check("R2b its B Bloch vector is (1/sqrt2, 0, 1/sqrt2)", rB == (1 / sp.sqrt(2), 0, 1 / sp.sqrt(2)), rB)
check("R2c that point is outside the octahedron: |x|+|y|+|z| = sqrt2 > 1",
      sp.simplify(sum(abs(c) for c in rB) - sp.sqrt(2)) == 0 and sp.sqrt(2) > 1)
ok = True
heralds = []
for a in AX:
    for e in (1, -1):
        Eff = kron((I2 + e * P[a]) / 2, I2)
        pr = sp.simplify((rho_prod * Eff).trace())
        if pr == 0:
            continue
        post = simp(ptrace_A(Eff * rho_prod) / pr)
        heralds.append(bloch(post))
        ok &= bloch(post) == rB
check("R2d every A Pauli read outcome of positive probability leaves B at the same point (no steering)", ok,
      len(heralds))
check("R2e control: (1/2, 0, 1/2) is inside the octahedron (|x|+|y|+|z| = 1)",
      sum(abs(c) for c in (sp.Rational(1, 2), 0, sp.Rational(1, 2))) == 1)

# ------------------------------------------------- R3: the P1-removed herald also fails QC
rho101 = (I2 + X + Z) / 2
check("R3a Bloch (1,0,1) is no qubit state: (I+X+Z)/2 has eigenvalue (1-sqrt2)/2 < 0",
      min_eig(rho101) == (1 - sp.sqrt(2)) / 2 and (1 - sp.sqrt(2)) / 2 < 0, eigs(rho101))
post_pts = []
for ex, ez in itertools.product((1, -1), repeat=2):
    EX = kron((I2 + ex * X) / 2, I2)
    st = EX * rho_phi * EX
    p1 = sp.simplify(st.trace())
    st = st / p1
    EZ = kron((I2 + ez * Z) / 2, I2)
    st2 = EZ * st * EZ
    p2 = sp.simplify(st2.trace())
    post_pts.append(bloch(simp(ptrace_A(st2 / p2))))
check("R3b comparator: on Phi+, A reads X then Z (Lueders); B's conditional is +-e_x for every record pair",
      post_pts == [(1, 0, 0), (1, 0, 0), (-1, 0, 0), (-1, 0, 0)], post_pts)

# ------------------------------------------------- R4: N3, CHSH with Pauli settings at stabilizer scope
# Two-qubit stabilizer states generated from |00> by H, S on each factor and CNOT (generic Clifford group action).
gens = [kron(HAD, I2), kron(I2, HAD), kron(SPH, I2), kron(I2, SPH), CNOT]


def canon(v):
    v = simp(v)
    k = next(i for i in range(4) if v[i] != 0)
    return tuple(sp.nsimplify(sp.simplify(x / v[k] * abs(v[k]))) for x in v)


seen = {canon(ket00): ket00}
frontier = [ket00]
while frontier:
    nxt = []
    for v in frontier:
        for g in gens:
            w = simp(g * v)
            key = canon(w)
            if key not in seen:
                seen[key] = w
                nxt.append(w)
    frontier = nxt
stab = list(seen.values())
check("R4a the generated set has the 60 two-qubit stabilizer states", len(stab) == 60, len(stab))
best = 0
for v in stab:
    rho = proj(v)
    T = {(a, b): sp.simplify((rho * kron(P[a], P[b])).trace()) for a in AX for b in AX}
    for a0, a1, b0, b1 in itertools.product(AX, repeat=4):
        S = T[(a0, b0)] + T[(a0, b1)] + T[(a1, b0)] - T[(a1, b1)]
        best = max(best, abs(S))
check("R4b every two-qubit stabilizer state with Pauli settings has |CHSH| <= 2 (max attained = 2)", best == 2, best)
chsh_op = kron(X, X) + kron(X, Z) + kron(Z, X) - kron(Z, Z)
check("R4c the Pauli-settings CHSH operator XX+XZ+ZX-ZZ has maximum eigenvalue 2*sqrt2 (non-stabilizer states exceed 2)",
      eigs(chsh_op)[-1] == 2 * sp.sqrt(2), eigs(chsh_op))

# ------------------------------------------------- R5: N7, the hH2 witness
rho_c = simp(CNOT * table_op(T_swap) * CNOT)
T_c = table_of(rho_c)
check("R5a cnot(SWAP/2) has table (I + X(x)I + I(x)Z - X(x)Z)/4",
      T_c == {("0", "0"): 1, ("x", "0"): 1, ("0", "z"): 1, ("x", "z"): -1}, T_c)
Emx = (I2 - X) / 2
Emz = (I2 - Z) / 2
val = sp.simplify((rho_c * kron(Emx, Emz)).trace())
check("R5b cnot(SWAP/2) takes -1/2 on the Pauli product effect (-x) (x) (-z)", val == sp.Rational(-1, 2), val)
okc = True
for a, b in itertools.product(AX, repeat=2):
    for e, f in itertools.product((1, -1), repeat=2):
        okc &= sp.simplify((table_op(T_swap) * kron((I2 + e * P[a]) / 2, (I2 + f * P[b]) / 2)).trace()) >= 0
check("R5c control: SWAP/2 itself is nonnegative on all 36 Pauli product effects", okc)

# ------------------------------------------------- R6: N8, comparator signs of CNOT on the 15 Pauli products
signs = {}
okperm = True
for a, b in itertools.product(LAB, repeat=2):
    if (a, b) == ("0", "0"):
        continue
    M = simp(CNOT * kron(P[a], P[b]) * CNOT)
    hit = [(c, d, s) for c, d in itertools.product(LAB, repeat=2) for s in (1, -1)
           if simp(M - s * kron(P[c], P[d])) == sp.zeros(4, 4)]
    okperm &= len(hit) == 1
    signs[(a, b)] = hit[0]
check("R6a CNOT conjugation maps each of the 15 Pauli products to one signed Pauli product", okperm)
want = {("x", "z"): ("y", "y", -1), ("y", "y"): ("x", "z", -1),
        ("x", "y"): ("y", "z", 1), ("y", "z"): ("x", "y", 1)}
check("R6b XZ -> -YY, YY -> -XZ, XY -> +YZ, YZ -> +XY",
      all(signs[k] == v for k, v in want.items()), {k: signs[k] for k in want})
check("R6c every other Pauli product maps with sign +1",
      all(signs[k][2] == 1 for k in signs if k not in (("x", "z"), ("y", "y"))))

nf = sum(1 for _, ok in results if not ok)
print(f"\n{len(results)} checks, {nf} failures")
sys.exit(1 if nf else 0)
