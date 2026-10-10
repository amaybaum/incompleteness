#!/usr/bin/env python3
"""b9_spec.py -- node B9 of research/bridge: the SPEC side of HO-5.

DECISION RULE (fixed 2026-10-10T22:45:37Z, from `date -u` immediately before writing; before run 1).

Question (NOTES-B9): what a transfer of the certified matrix-level spectator theorem
`substratumClass_contextStable` (StructuralClosure.lean:261; class `IsMonomial`,
SubstratumInterface.lean:75) to the pair carrier W 3 needs, and whether it reduces A_miss to
SPEC_P(J) alone. The dictionary M(w) = (1/4) sum w[mu][nu] s_mu (x) s_nu is a comparison and
construction tool, never a premise. Tables: actC N w = Nh w, actT N w = w Nh^T, Nh = 1 (+) N.

Checks:
  Y1  Dictionary, product law: M(prodState x y) = rho(x) (x) rho(y), rho(x) = (I + x.s)/2,
      symbolically in x, y (6 real symbols).
  Y2  Dictionary, the DIM-1 gate: M(cnot w) = CNOT M(w) CNOT on all 16 basis tables, with the
      kernel's cnot (signed permutation sgn/pc/pt, CompositeDimension.lean:741-758) and
      CNOT = |0><0| (x) I + |1><1| (x) X; and nflip = B(X).
  Y3  Monomial class images: for U = diag(1, c + i s) (symbolic, c^2 + s^2 = 1), B(U) = R_z(c, s);
      the idle extension tensorOf 1 U (spectator on the left, as in ContextStable) pulls back to
      actT B(U) on all 16 basis tables, symbolically; likewise U (x) 1 to actC B(U).
  Y4  The transferred monomial class with cnot has abelian identity component: the real span of
      the generators {Z(x)I, I(x)Z} closed under conjugation by the finite generators
      {CNOT, X(x)I, I(x)X, SWAP} is spanned by diagonal matrices, all pairwise commutators vanish,
      and its dimension is 3 (Z(x)I, I(x)Z, Z(x)Z).
  Y5  Countercontrol: adjoining J's lift V (B(V) = cycEquiv) on token A makes the generated algebra
      nonabelian: V Z V^* is off-diagonal and [Z(x)I, V Z V^* (x) I] != 0.
  Y6  SPEC_P(J) alone is a finite group with cnot: the group generated on W 3 by cnot, actC B(V),
      actT B(V) consists of signed permutation matrices of the 16 table entries and is finite;
      its order is printed and divides 11520 (two-qubit Clifford group modulo phases).
  Y7  HO-5 item 1 identities: B(V) R_z(t) B(V)^-1 = R_x(t) (symbolic) and B(V) = R_z(pi/2) R_x(pi/2)
      or R_x(pi/2) R_z(pi/2) (the order is printed).

VERDICT B9-EXACT iff Y1-Y7 all PASS; otherwise VERDICT B9-FAILED with the failing ids.

Pre-run edit 2026-10-10T22:46:40Z (before run 1; rule text unchanged): the pc/pt tables are parsed from
CompositeDimension.lean at L instead of hand-transcribed (a draft transcription of pt was its
transpose).
"""
import sys

import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


I = sp.I
r2 = sp.sqrt(2)
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
kron = sp.kronecker_product
I2 = sp.eye(2)


def dag(M):
    return M.conjugate().T


def simp(M):
    return M.applyfunc(lambda z: sp.expand(z))


def Mdict(w):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            if w[mu, nu] != 0:
                out += w[mu, nu] * kron(SIG[mu], SIG[nu])
    return out / 4


def E(mu, nu):
    w = sp.zeros(4, 4)
    w[mu, nu] = 1
    return w


def hom(N):
    Nh = sp.zeros(4, 4)
    Nh[0, 0] = 1
    Nh[1:, 1:] = N
    return Nh


def bloch(U):
    B = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            B[j, k] = sp.expand((SIG[j + 1] * U * SIG[k + 1] * dag(U)).trace() / 2)
    return B


# ---------------- Y1 ----------------
x = sp.symbols("x0:3", real=True)
y = sp.symbols("y0:3", real=True)
hx = [1] + list(x)
hy = [1] + list(y)
prod_w = sp.Matrix(4, 4, lambda m, n: hx[m] * hy[n])
rho = lambda v: (s0 + v[0] * sx + v[1] * sy + v[2] * sz) / 2
ok1 = simp(Mdict(prod_w) - kron(rho(x), rho(y))) == sp.zeros(4, 4)
check("Y1", ok1, "M(prodState x y) = rho(x) (x) rho(y) symbolically")

# ---------------- Y2 ----------------
def sgn(mu, nu):
    return -1 if (mu, nu) in ((1, 3), (2, 2)) else 1


def read_pc_pt():
    import os
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                       "verification", "lean-mathlib", "OIBridge", "CompositeDimension.lean")
    text = open(src, encoding="utf-8").read()
    return text


SRC = read_pc_pt()
start = SRC.index("def pc : Fin 4 → Fin 4 → Fin 4")
mid = SRC.index("def pt : Fin 4 → Fin 4 → Fin 4")
end = SRC.index("def cnotFun")
block = SRC[start:end]
import re
PAT = re.compile(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)")


def parse(txt):
    T = [[None] * 4 for _ in range(4)]
    n = 0
    for a, b, v in PAT.findall(txt):
        T[int(a)][int(b)] = int(v)
        n += 1
    assert n == 16 and all(T[i][j] is not None for i in range(4) for j in range(4))
    return T


PC = parse(SRC[start:mid])
PT = parse(SRC[mid:end])


def cnot_tab(w):
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            out[mu, nu] = sgn(mu, nu) * w[PC[mu][nu], PT[mu][nu]]
    return out


CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ok2 = all(simp(Mdict(cnot_tab(E(m, n))) - CNOT * Mdict(E(m, n)) * CNOT) == sp.zeros(4, 4)
          for m in range(4) for n in range(4))
nflip_ok = bloch(sx) == sp.diag(1, -1, -1)
check("Y2", ok2 and nflip_ok,
      f"M(cnot w) = CNOT M(w) CNOT on all 16 basis tables (pc/pt as transcribed); B(X) = nflip")
print("     pc/pt source block at L:")
for line in block.splitlines()[:16]:
    print("       " + line)
print(f"     parsed pc = {PC}")
print(f"     parsed pt = {PT}")

# ---------------- Y3 ----------------
c, s = sp.symbols("c s", real=True)
U = sp.diag(1, c + I * s)
BU = bloch(U).applyfunc(lambda z: sp.expand(z.subs(c ** 2, 1 - s ** 2)))
Rz = sp.Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
ok3 = (BU - Rz).applyfunc(sp.simplify) == sp.zeros(3, 3)
Nh = hom(Rz)
for m in range(4):
    for n in range(4):
        w = E(m, n)
        lT = Mdict(w * Nh.T)
        rT = kron(I2, U) * Mdict(w) * dag(kron(I2, U))
        lC = Mdict(Nh * w)
        rC = kron(U, I2) * Mdict(w) * dag(kron(U, I2))
        dT = (lT - rT).applyfunc(lambda z: sp.simplify(sp.expand(z).subs(c ** 2, 1 - s ** 2)))
        dC = (lC - rC).applyfunc(lambda z: sp.simplify(sp.expand(z).subs(c ** 2, 1 - s ** 2)))
        if dT != sp.zeros(4, 4) or dC != sp.zeros(4, 4):
            ok3 = False
check("Y3", ok3, "B(diag(1, c+is)) = R_z(c,s); tensorOf 1 U pulls back to actT R_z and U (x) 1 to "
      "actC R_z on all 16 tables, symbolically under c^2 + s^2 = 1")

# ---------------- Y4 ----------------
ZI, IZ, ZZ = kron(sz, I2), kron(I2, sz), kron(sz, sz)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
FIN = [CNOT, kron(sx, I2), kron(I2, sx), SWAP]


def vec(M):
    return sp.Matrix([sp.expand(z) for z in M])


span = [ZI, IZ]
changed = True
while changed:
    changed = False
    for G in FIN:
        for A in list(span):
            Bm = simp(G * A * dag(G))
            mat = sp.Matrix.hstack(*[vec(Z) for Z in span])
            if sp.Matrix.hstack(mat, vec(Bm)).rank() > mat.rank():
                span.append(Bm)
                changed = True
diag_only = all(all(Z[i, j] == 0 for i in range(4) for j in range(4) if i != j) for Z in span)
comm0 = all(simp(A * Bm - Bm * A) == sp.zeros(4, 4) for A in span for Bm in span)
dim = sp.Matrix.hstack(*[vec(Z) for Z in span]).rank()
check("Y4", diag_only and comm0 and dim == 3,
      f"closure of {{Z(x)I, I(x)Z}} under CNOT, X(x)I, I(x)X, SWAP: dimension {dim}, all diagonal, "
      f"all commutators zero (identity component abelian: the diagonal torus)")

# ---------------- Y5 ----------------
H = sp.Matrix([[1, 1], [1, -1]]) / r2
Sg = sp.diag(1, I)
CYC = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
# find the cyc3 lift among H, S words of length <= 6
from itertools import product as iprod
V = None
for L in range(0, 7):
    for word in iprod((H, Sg), repeat=L):
        W = sp.eye(2)
        for G in word:
            W = G * W
        W = simp(W)
        if bloch(W).applyfunc(sp.nsimplify) == CYC:
            V = W
            break
    if V is not None:
        break
VZV = simp(V * sz * dag(V))
offdiag = any(VZV[i, j] != 0 for i in range(2) for j in range(2) if i != j)
comm = simp(ZI * kron(VZV, I2) - kron(VZV, I2) * ZI)
check("Y5", V is not None and offdiag and comm != sp.zeros(4, 4),
      f"cyc3 lift found; V Z V^* = {VZV.tolist()} (off-diagonal); [Z(x)I, VZV^*(x)I] != 0")

# ---------------- Y6 ----------------
def table_rep(L):
    """16x16 real matrix of w -> M^-1(L M(w) L^*) on the basis tables (Pauli coefficients)."""
    R = sp.zeros(16, 16)
    for m in range(4):
        for n in range(4):
            img = simp(L * Mdict(E(m, n)) * dag(L))
            for a in range(4):
                for b in range(4):
                    coeff = sp.nsimplify(sp.expand((kron(SIG[a], SIG[b]) * img).trace()))
                    R[4 * a + b, 4 * m + n] = coeff
    return R


gens = [table_rep(CNOT), table_rep(kron(V, I2)), table_rep(kron(I2, V))]


def is_signed_perm(R):
    for row in R.tolist():
        nz = [z for z in row if z != 0]
        if len(nz) != 1 or nz[0] not in (1, -1):
            return False
    return True


sp_ok = all(is_signed_perm(R) for R in gens)


def as_tuple(R):
    return tuple(int(z) for z in R)


seen = {as_tuple(sp.eye(16))}
frontier = [sp.eye(16)]
gi = [sp.Matrix(R) for R in gens]
while frontier and len(seen) <= 20000:
    nxt = []
    for A in frontier:
        for G in gi:
            Bm = G * A
            t = as_tuple(Bm)
            if t not in seen:
                seen.add(t)
                nxt.append(Bm)
    frontier = nxt
order = len(seen)
check("Y6", sp_ok and not frontier and 11520 % order == 0,
      f"<cnot, actC cyc3, actT cyc3> on W 3: signed permutations, finite, order {order} "
      f"(divides 11520: {11520 % order == 0})")

# ---------------- Y7 ----------------
t = sp.symbols("t", real=True)
Rz_t = sp.Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])
Rx_t = sp.Matrix([[1, 0, 0], [0, sp.cos(t), -sp.sin(t)], [0, sp.sin(t), sp.cos(t)]])
conj_ok = (CYC * Rz_t * CYC.inv() - Rx_t).applyfunc(sp.simplify) == sp.zeros(3, 3)
Rz90 = Rz_t.subs(t, sp.pi / 2)
Rx90 = Rx_t.subs(t, sp.pi / 2)
o1 = (Rz90 * Rx90 == CYC)
o2 = (Rx90 * Rz90 == CYC)
check("Y7", conj_ok and (o1 or o2),
      f"cyc3 R_z(t) cyc3^-1 = R_x(t); cyc3 = R_z(pi/2) R_x(pi/2): {o1}; cyc3 = R_x(pi/2) R_z(pi/2): {o2}")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B9-EXACT" if not FAIL else "VERDICT B9-FAILED " + " ".join(FAIL))
sys.exit(0)
