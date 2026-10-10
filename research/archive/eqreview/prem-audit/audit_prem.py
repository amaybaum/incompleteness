"""
audit_prem.py -- coordinator's independent exact checks of EQ5-PREM (scratchpad/eq5/PREM/RESULT.md).

Independent of the thread's scripts: no file of scratchpad/eq5/PREM is imported or read. The Pauli map, the
standard CNOT conjugation and the table actions are implemented here from their definitions. The repository's
`cnot` (sgn, pc, pt) is read from the base snapshot and compared with the standard CNOT.

Usage: python3 -I -B audit_prem.py <base OIBridge dir>

Checks (decision rule fixed before the first run):
  C1  one token: sigma_y rho^T sigma_y = (I - r.sigma)/2 for symbolic r            (theta = Ad(sigma_y) o T)
  C2  pauliW(actT diag(-1,1,-1) w) = (I(x)sy) pauliW(w) (I(x)sy) and
      pauliW(actT reflY w) = partial transpose on token 2 of pauliW(w), symbolic w   (theta(twin) = Q3)
  C3  base cnotFun (sgn, pc, pt) = standard CNOT conjugation, control token 1, symbolic w;
      the base lines defining sgn, pc, pt are exactly the ones transcribed here
  C4  cnot(prodState xplus z3) = phiW = diag(1,1,-1,1); pauliW(phiW) = |Phi+><Phi+| (trace 1, rank 1, idempotent)
  C5  actT reflY phiW = idW; pauliW(idW) = SWAP/2; v = (0,1,-1,0): v^T pauliW(idW) v = -1;
      eigenvalues {1/2,1/2,1/2,-1/2}; actT reflY fixes prodState xplus z3        (TWIN: hgate fails)
  C6  MAX: idW on product effects = e.f (Euclidean on R^4); generator values 1, 1/2, 1/2, (1+b.c)/4;
      cnot(idW) at sharp b = (-1,0,0), c = (0,0,-1) equals -1/2
  C7  MIN: F(prodState x y) = 1 - x.(reflY y); certificate 1 - x.w = |x-w|^2/2 + (1-|x|^2)/2 + (1-|w|^2)/2;
      F(phiW) = -2
  C8  CC2: T = hom z (x) hom z + E_xx/2: pure marginals, g and f sharp, T(g, f) = -1/40, T not a product
  C9  purity core: for T = hom z (x) hom y + C (C zero on row 0 and column 0), z.z = 1:
      T(g_z, f) = -(1/2) z^T C f and |cvec_f|^2 - c_f0^2 = 2 f(y) z^T C f + |C f|^2  (symbolic)
  C10 the homogenized e_x, e_y, e_z, -e_z form an invertible 4x4 matrix (256 four-fold products span W4)
  C11 -I commutes with every 3x3 matrix (symbolic)
  C12 fourVal on product generators factorizes: fourVal(x0(x)x1, x2(x)x3, e0(x)e2, e1(x)e3) = prod_t e_t.x_t
  C13 citations: each listed base line contains the token RESULT.md attributes to it
  C14 no float enters a checked quantity

VERDICT PREM-AUDIT-CHECKS-PASS iff C1-C14 all pass; otherwise VERDICT NOT RENDERED.
Print-only lines (marked INFO) are listed for the reader and are not checks.
"""
import os
import sys

import sympy as sp

OI = sys.argv[1]

results = []


def check(name, cond, detail=""):
    results.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))


def lines_of(fn):
    with open(os.path.join(OI, fn), encoding="utf-8") as fh:
        return fh.read().split("\n")


I2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, SX, SY, SZ]


def kron(a, b):
    return sp.kronecker_product(a, b)


def pauliW(w):
    m = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            m += w[mu][nu] * kron(SIG[mu], SIG[nu])
    return m / 4


def coeffs(rho):
    return [[sp.simplify((rho * kron(SIG[mu], SIG[nu])).trace()) for nu in range(4)] for mu in range(4)]


def hom(x):
    return [sp.Integer(1)] + list(x)


def tens(a, b):
    return [[a[mu] * b[nu] for nu in range(4)] for mu in range(4)]


def homMap(N, v):
    tail = sp.Matrix(v[1:])
    return [v[0]] + list(N * tail)


def actT(N, w):
    return [homMap(N, w[mu]) for mu in range(4)]


def actC(N, w):
    cols = [homMap(N, [w[k][nu] for k in range(4)]) for nu in range(4)]
    return [[cols[nu][mu] for nu in range(4)] for mu in range(4)]


def eq_tab(a, b):
    return all(sp.simplify(a[i][j] - b[i][j]) == 0 for i in range(4) for j in range(4))


def pair(e, w, f):
    return sp.expand(sum(e[mu] * w[mu][nu] * f[nu] for mu in range(4) for nu in range(4)))


syms = sp.symbols("w0:16", real=True)
W = [[syms[4 * i + j] for j in range(4)] for i in range(4)]
reflY = sp.diag(1, -1, 1)
antipode = sp.diag(-1, -1, -1)

# C1
r = sp.symbols("r1:4", real=True)
rho1 = (I2 + r[0] * SX + r[1] * SY + r[2] * SZ) / 2
lhs = SY * rho1.T * SY
rhs = (I2 - r[0] * SX - r[1] * SY - r[2] * SZ) / 2
check("C1 one token: sigma_y rho^T sigma_y = (I - r.sigma)/2", sp.simplify(lhs - rhs) == sp.zeros(2, 2))

# C2
D = antipode * reflY
P = pauliW(W)
U = kron(I2, SY)
c2a = sp.simplify(pauliW(actT(D, W)) - U * P * U.H) == sp.zeros(4, 4)


def ptB(m):
    out = sp.zeros(4, 4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    out[2 * a + b, 2 * c + d] = m[2 * a + d, 2 * c + b]
    return out


c2b = sp.simplify(pauliW(actT(reflY, W)) - ptB(P)) == sp.zeros(4, 4)
check("C2 theta o actT reflY = actT diag(-1,1,-1) is Ad(I(x)sigma_y); actT reflY is the token-2 partial transpose",
      c2a and c2b, f"Ad {c2a}, PT {c2b}")

# C3
L = lines_of("CompositeDimension.lean")
want = {
    741: "def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1",
    744: "def pc : Fin 4 → Fin 4 → Fin 4",
    745: "  | 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 3 | 0, 3 => 3",
    746: "  | 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2",
    747: "  | 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1",
    748: "  | 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 0 | 3, 3 => 0",
    751: "def pt : Fin 4 → Fin 4 → Fin 4",
    752: "  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3",
    753: "  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 3 | 1, 3 => 2",
    754: "  | 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 3 | 2, 3 => 2",
    755: "  | 3, 0 => 0 | 3, 1 => 1 | 3, 2 => 2 | 3, 3 => 3",
    758: "def cnotFun (ω : W 3) : W 3 := fun μ ν => sgn μ ν * ω (pc μ ν) (pt μ ν)",
}
lines_ok = all(L[k - 1] == v for k, v in want.items())
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(mu, nu):
    return -1 if (mu == 1 and nu == 3) or (mu == 2 and nu == 2) else 1


def cnot_repo(w):
    return [[sgn(mu, nu) * w[PC[mu][nu]][PT[mu][nu]] for nu in range(4)] for mu in range(4)]


P0 = sp.Matrix([[1, 0], [0, 0]])
P1 = sp.Matrix([[0, 0], [0, 1]])
CN = kron(P0, I2) + kron(P1, SX)


def cnot_std(w):
    return coeffs(CN * pauliW(w) * CN.H)


c3 = eq_tab(cnot_repo(W), cnot_std(W))
check("C3 base cnotFun = standard CNOT conjugation (control token 1); transcribed lines match the base",
      c3 and lines_ok, f"equal {c3}, lines {lines_ok}")

# C4
xplus = [1, 0, 0]
z3 = [0, 0, 1]
pXZ = tens(hom(xplus), hom(z3))
phiW = [[1 if (m == n and m != 2) else (-1 if m == n == 2 else 0) for n in range(4)] for m in range(4)]
c4a = eq_tab(cnot_std(pXZ), phiW) and eq_tab(cnot_repo(pXZ), phiW)
Pphi = pauliW(phiW)
bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
c4b = sp.simplify(Pphi - bell * bell.T) == sp.zeros(4, 4) and Pphi.trace() == 1
check("C4 cnot(prodState xplus z3) = phiW = diag(1,1,-1,1); pauliW(phiW) = |Phi+><Phi+|", c4a and c4b,
      f"gate {c4a}, Bell {c4b}")

# C5
idW = [[1 if m == n else 0 for n in range(4)] for m in range(4)]
c5a = eq_tab(actT(reflY, phiW), idW)
Pid = pauliW(idW)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
c5b = sp.simplify(Pid - SWAP / 2) == sp.zeros(4, 4)
v = sp.Matrix([0, 1, -1, 0])
val = sp.simplify((v.T * Pid * v)[0, 0])
ev = Pid.eigenvals()
c5c = val == -1 and ev == {sp.Rational(1, 2): 3, sp.Rational(-1, 2): 1}
c5d = eq_tab(actT(reflY, pXZ), pXZ)
check("C5 actT reflY phiW = idW; pauliW(idW) = SWAP/2 with v^T pauliW(idW) v = -1; actT reflY fixes prodState xplus z3",
      c5a and c5b and c5c and c5d, f"{c5a} {c5b} value {val} eig {ev} {c5d}")

# C6
e = sp.symbols("e0:4", real=True)
f = sp.symbols("f0:4", real=True)
c6a = sp.expand(pair(list(e), idW, list(f)) - sum(e[i] * f[i] for i in range(4))) == 0
b = sp.symbols("b1:4", real=True)
c = sp.symbols("c1:4", real=True)
u = [1, 0, 0, 0]
sh_b = [sp.Rational(1, 2)] + [bi / 2 for bi in b]
sh_c = [sp.Rational(1, 2)] + [ci / 2 for ci in c]
g1 = pair(u, idW, u) == 1
g2 = sp.simplify(pair(u, idW, sh_c) - sp.Rational(1, 2)) == 0
g3 = sp.simplify(pair(sh_b, idW, u) - sp.Rational(1, 2)) == 0
g4 = sp.simplify(pair(sh_b, idW, sh_c) - (1 + sum(b[i] * c[i] for i in range(3))) / 4) == 0
chainW = cnot_std(idW)
cnot_same = eq_tab(chainW, cnot_repo(idW))
sb = [sp.Rational(1, 2), sp.Rational(-1, 2), 0, 0]
sc = [sp.Rational(1, 2), 0, 0, sp.Rational(-1, 2)]
v6 = pair(sb, chainW, sc)
check("C6 MAX: idW pairs as the Euclidean product; generator values 1, 1/2, 1/2, (1+b.c)/4; cnot(idW) at sharp "
      "(-x, -z) is -1/2", c6a and g1 and g2 and g3 and g4 and cnot_same and v6 == sp.Rational(-1, 2),
      f"value {v6}, chainW {chainW}")

# C7
x = sp.symbols("x1:4", real=True)
y = sp.symbols("y1:4", real=True)
pxy = tens(hom(x), hom(y))


def Fmin(w):
    return w[0][0] - w[1][1] + w[2][2] - w[3][3]


wv = list(reflY * sp.Matrix(y))
c7a = sp.expand(Fmin(pxy) - (1 - sum(x[i] * wv[i] for i in range(3)))) == 0
xs = sp.Matrix(x)
ws = sp.Matrix(wv)
cert = (xs - ws).dot(xs - ws) / 2 + (1 - xs.dot(xs)) / 2 + (1 - ws.dot(ws)) / 2
c7b = sp.expand(cert - (1 - xs.dot(ws))) == 0 and sp.expand(ws.dot(ws) - sp.Matrix(y).dot(sp.Matrix(y))) == 0
c7c = Fmin(phiW) == -2
check("C7 MIN: F(prodState x y) = 1 - x.(reflY y), certificate |x-w|^2/2 + (1-|x|^2)/2 + (1-|w|^2)/2 with |w| = |y|; "
      "F(phiW) = -2", c7a and c7b and c7c)

# C8
hz = hom(z3)
T8 = [[hz[m] * hz[n] + (sp.Rational(1, 2) if (m == 1 and n == 1) else 0) for n in range(4)] for m in range(4)]
g8 = [sp.Rational(1, 2), sp.Rational(3, 10), 0, sp.Rational(-2, 5)]
f8 = [sp.Rational(1, 2), sp.Rational(-1, 2), 0, 0]
sharp_g = (2 * g8[0]) ** 2 == sum((2 * g8[i]) ** 2 for i in range(1, 4))
sharp_f = (2 * f8[0]) ** 2 == sum((2 * f8[i]) ** 2 for i in range(1, 4))
marg = [T8[0][n] for n in range(4)] == hz and [T8[m][0] for m in range(4)] == hz
v8 = pair(g8, T8, f8)
notprod = not eq_tab(T8, tens(hz, hz))
check("C8 CC2: pure marginals (z, z), g and f sharp, T(g, f) = -1/40, T is not hom z (x) hom z",
      sharp_g and sharp_f and marg and v8 == sp.Rational(-1, 40) and notprod, f"T(g,f) = {v8}")

# C9
z = sp.symbols("z1:4", real=True)
yy = sp.symbols("yy1:4", real=True)
Cs = sp.symbols("C11:14 C21:24 C31:34", real=True)
Cm = sp.Matrix(4, 4, lambda i, j: 0 if (i == 0 or j == 0) else Cs[3 * (i - 1) + (j - 1)])
T9 = sp.Matrix(4, 4, lambda i, j: hom(z)[i] * hom(yy)[j]) + Cm
fv = sp.Matrix(sp.symbols("ff0:4", real=True))
gz = sp.Matrix([sp.Rational(1, 2)] + [-zi / 2 for zi in z])
zz = sum(zi ** 2 for zi in z)
zC_f = (sp.Matrix([0] + list(z)).T * Cm * fv)[0, 0]
lhs9a = (gz.T * T9 * fv)[0, 0]
c9a = sp.simplify(sp.expand(lhs9a - (-zC_f / 2)).subs(z[0] ** 2, 1 - z[1] ** 2 - z[2] ** 2)) == 0
cf = T9 * fv
fy = (sp.Matrix(hom(yy)).T * fv)[0, 0]
Cf = Cm * fv
lhs9b = sum(cf[i] ** 2 for i in range(1, 4)) - cf[0] ** 2
rhs9b = 2 * fy * zC_f + sum(Cf[i] ** 2 for i in range(1, 4))
c9b = sp.expand(sp.expand(lhs9b - rhs9b).subs(z[0] ** 2, 1 - z[1] ** 2 - z[2] ** 2)) == 0
check("C9 purity core: T(g_z, f) = -(1/2) z^T C f and |cvec_f|^2 - c_f0^2 = 2 f(y) z^T C f + |C f|^2 modulo z.z = 1",
      c9a and c9b, f"{c9a} {c9b}")

# C10
M10 = sp.Matrix([hom([1, 0, 0]), hom([0, 1, 0]), hom([0, 0, 1]), hom([0, 0, -1])])
d10 = M10.det()
check("C10 homogenized e_x, e_y, e_z, -e_z are linearly independent", d10 != 0, f"det = {d10}")

# C11
R = sp.Matrix(3, 3, sp.symbols("R0:9"))
check("C11 -I commutes with every 3x3 matrix", (antipode * R - R * antipode) == sp.zeros(3, 3))

# C12
xs4 = [hom(sp.symbols(f"p{t}_1:4", real=True)) for t in range(4)]
es4 = [list(sp.symbols(f"q{t}_0:4", real=True)) for t in range(4)]
X12 = tens(xs4[0], xs4[1])
Y12 = tens(xs4[2], xs4[3])
E12 = tens(es4[0], es4[2])
F12 = tens(es4[1], es4[3])
fv12 = sum(X12[a][bb] * Y12[cc][d] * E12[a][cc] * F12[bb][d]
           for a in range(4) for bb in range(4) for cc in range(4) for d in range(4))
prod12 = 1
for t in range(4):
    prod12 *= sum(es4[t][i] * xs4[t][i] for i in range(4))
check("C12 fourVal factorizes on product generators", sp.expand(fv12 - prod12) == 0)

# C13
cites = [
    ("CompositeDimension.lean", 186, "maxCone"),
    ("CompositeDimension.lean", 869, "Lor"),
    ("CompositeDimension.lean", 930, "lor_ehom"),
    ("CompositeDimension.lean", 916, "isEffectOn_affOf"),
    ("CompositeDimension.lean", 222, "posFwd"),
    ("CompositeDimension.lean", 223, "posInv"),
    ("CompositeInterface.lean", 445, "JointReversible"),
    ("CompositeInterface.lean", 306, "margA_prodState"),
    ("CompositeInterface.lean", 332, "condA_prodState"),
    ("CompositeInterface.lean", 148, "exists_effect_rescale"),
    ("CompositeInterface.lean", 290, "prodEff_expand"),
    ("OrbitGeneration.lean", 69, "PreservesBody"),
    ("CompletionAction.lean", 202, "body_isClosed"),
    ("EmbeddedObservation.lean", 98, "RegroupingInvariant"),
    ("EmbeddedObservation.lean", 106, "RelabellingInvariant"),
    ("MonoidalCompletion.lean", 311, "HComp"),
]
bad = []
for fn, ln, tok in cites:
    try:
        line = lines_of(fn)[ln - 1]
    except (OSError, IndexError):
        line = None
    ok = line is not None and tok in line
    if not ok:
        bad.append(f"{fn}:{ln} lacks {tok!r}: {line!r}")
check("C13 cited base lines carry the attributed names", not bad, "; ".join(bad) if bad else f"{len(cites)} citations")

info = [
    ("CompositeDimension.lean", 838), ("CompositeDimension.lean", 1160), ("CompositeDimension.lean", 1380),
    ("CompositeInterface.lean", 226), ("OrbitGeneration.lean", 74), ("StageCompletion.lean", 141),
    ("StageCompletion.lean", 142), ("CompletionAction.lean", 46), ("CompletionAction.lean", 352),
    ("CarrierGeneralOIPlus.lean", 73), ("ReferenceExtension.lean", 447), ("SpectatorBridge.lean", 223),
    ("EffectSpace.lean", 415),
]
for fn, ln in info:
    try:
        line = lines_of(fn)[ln - 1]
    except (OSError, IndexError):
        line = "<missing>"
    print(f"INFO {fn}:{ln}: {line.strip()[:110]}")

# C14
floats = [q for q in [v6, v8, d10, val] if isinstance(q, sp.Float)]
check("C14 no float in the checked quantities", not floats)

n_pass = sum(results)
print(f"--- audit_prem: {n_pass}/{len(results)} checks pass")
print("VERDICT PREM-AUDIT-CHECKS-PASS" if all(results) else "VERDICT NOT RENDERED")
