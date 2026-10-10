# c8_bell_sets.py -- research/countermodels node C8 (round 2): non-orthogonal Bell-type sets with three or more members.
# DECISION RULE (fixed before the first run, 2026-10-10T23:08Z by date -u; predictions in NOTES-C8 S0):
#  Exact arithmetic (sympy Rational and exact radicals sqrt(2), sqrt(3); guard EX: no Float). Matrix normalization
#  d_g = I - 2 g g^dag = 8 pauliW(z_g); psi_s as in c2_structure.py / indep_checkC.py (the (-1/8)-eigenvectors of
#  pauliW(z_s), order SS = [(1,1),(1,-1),(-1,1),(-1,-1)]). For each instance Z = {g_1, ..., g_n} (g_1 the defect the
#  witness is tight against, g_2 its chosen partner) the script builds, as in NOTES-C8 S0 item 2,
#     W = span(g_1, g_2), a unit e in W^perp (listed per instance), v = g_1 + eps e, lambda = (1 - eps^2)/(4 c_12),
#     y = v v^dag + lambda d_{g_2},  x = g_2 - (<g_1|g_2>/eps) e,
#  and checks exactly: B (every g_k maximally entangled: reduced state I/2; the g_k pairwise distinct rays; c_12 in (0,1));
#  L1 <y, d_1> = 0; L2 <v v^dag, d_k> >= 0 for every k != 1; L3 x^dag y x < 0; L4 x^dag d_j x >= 0 for every j != 1 with
#  g_j orthogonal to g_1. CHECK <instance> PASS iff B, L1-L4 all hold; by the witness lemma C8-L ([W], NOTES-C8) the
#  instance's K(Z) is then not self-dual (y in K(Z)* \ K(Z)).
#  Instances: T16 line triple {psi_1, (4psi_1+3psi_3)/5, psi_3}, eps = 9/10; T9 line triple {psi_1, (3psi_1+4psi_3)/5,
#  psi_3}, eps = 3/4; TRI the trine {psi_1, (psi_1+sqrt3 psi_3)/2, (-psi_1+sqrt3 psi_3)/2}, eps = 3/4; SQ the square
#  {psi_1, (psi_1+psi_3)/sqrt2, psi_3, (psi_1-psi_3)/sqrt2}, eps = 3/4; HEX the regular hexagon {cos(k pi/6) psi_1 +
#  sin(k pi/6) psi_3}, partner k = 1, eps = 9/10; NC triple {psi_1, (4psi_1+3psi_3)/5, (3psi_1+4i psi_2)/5} with
#  e = psi_4, eps = 9/10; NO triple {psi_1, (4psi_1+3psi_3)/5, (3psi_2+4psi_4)/5} with e = (4psi_2-3psi_4)/5, eps = 9/10;
#  ZF+ the five-member set Z_F u {(4psi_1+3psi_3)/5} with e = (psi_2+psi_4)/sqrt2, eps = 9/10.
#  For every instance except ZF+, e is psi_2 unless listed (psi_2 lies in W^perp for W inside span(psi_1, psi_3)).
#  COUNTERCONTROLS: CC1 the T16 construction at eps = 1/2 (eps^2 < 2c - 1 = 7/25) violates L2 at k = 2;
#  CC2 for Z_F, <d_k, d_1> = 0 for all k != 1, so L1 is unsatisfiable (no witness of this form exists, consistent with
#  Theorem S); CC3 for an orthogonal pair the construction degenerates (c_12 = 0 makes lambda undefined) -- checked as
#  <psi_1|psi_3> = 0.
#  VERDICT C8-BELL-SETS-EXACT iff every CHECK and COUNTERCONTROL passes; verdict text generated from the measurements.
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, expand, conjugate, kronecker_product as kron

R_ = []
def rec(kind, cid, ok, text, detail=""):
    ok = bool(ok); R_.append(ok)
    print(f"{kind} {cid:<5} {'PASS' if ok else 'FAIL'} {text}" + (f" -- {detail}" if detail else ""))

I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = [sp.simplify(negvec(zdef(*s))) for s in SS]
def comb(c): return sum((c[k] * PSI[k] for k in range(4)), zeros(4, 1))
def nsq(v): return sp.nsimplify(sp.simplify(expand((v.H * v)[0])))
def ov(a, b): return sp.simplify(expand((a.H * b)[0]))
def ov2(a, b): o = ov(a, b); return sp.nsimplify(sp.simplify(expand(o * conjugate(o))))
def dg(g): return eye(4) - 2 * g * g.H
def ip(A, B): return sp.nsimplify(sp.simplify(expand((A * B).trace())))
def quad(x, M): return sp.nsimplify(sp.simplify(expand((x.H * M * x)[0])))
def red_A(g):
    rho = g * g.H; return Matrix(2, 2, lambda i, j: sum(rho[2 * i + k, 2 * j + k] for k in range(2)))
def max_ent(g): return sp.simplify(red_A(g) - eye(2) / 2) == zeros(2, 2)

def witness(gs, e, eps):
    g1, g2 = gs[0], gs[1]
    c12 = ov2(g1, g2)
    v = g1 + eps * e
    lam = (1 - eps ** 2) / (4 * c12)
    y = v * v.H + lam * dg(g2)
    x = g2 - (ov(g1, g2) / eps) * e
    L1 = ip(y, dg(g1))
    L2 = [ip(v * v.H, dg(g)) for g in gs[1:]]
    L3 = quad(x, y)
    orth = [g for g in gs[1:] if ov2(g1, g) == 0]
    L4 = [quad(x, dg(g)) for g in orth]
    distinct = all(ov2(gs[i], gs[j]) != 1 for i in range(len(gs)) for j in range(i + 1, len(gs)))
    B = all(nsq(g) == 1 and max_ent(g) for g in gs) and distinct and 0 < c12 < 1 and nsq(e) == 1 \
        and ov(g1, e) == 0 and ov(g2, e) == 0
    ok = B and L1 == 0 and all(t >= 0 for t in L2) and L3 < 0 and all(t >= 0 for t in L4)
    return ok, dict(c12=c12, lam=lam, L1=L1, L2=L2, L3=L3, L4=L4, n=len(gs), northo=len(orth))

r3 = sqrt(3); r2 = sqrt(2)
inst = [
    ("T16", [PSI[0], comb([Q(4, 5), 0, Q(3, 5), 0]), PSI[2]], PSI[1], Q(9, 10), "line triple c = 16/25"),
    ("T9", [PSI[0], comb([Q(3, 5), 0, Q(4, 5), 0]), PSI[2]], PSI[1], Q(3, 4), "line triple c = 9/25"),
    ("TRI", [PSI[0], comb([Q(1, 2), 0, r3 / 2, 0]), comb([-Q(1, 2), 0, r3 / 2, 0])], PSI[1], Q(3, 4), "trine (pairwise c = 1/4)"),
    ("SQ", [PSI[0], comb([1 / r2, 0, 1 / r2, 0]), PSI[2], comb([1 / r2, 0, -1 / r2, 0])], PSI[1], Q(3, 4), "square (c = 1/2, 0, 1/2)"),
    ("HEX", [PSI[0], comb([r3 / 2, 0, Q(1, 2), 0]), comb([Q(1, 2), 0, r3 / 2, 0]), PSI[2], comb([-Q(1, 2), 0, r3 / 2, 0]),
             comb([-r3 / 2, 0, Q(1, 2), 0])], PSI[1], Q(9, 10), "regular hexagon on the circle"),
    ("NC", [PSI[0], comb([Q(4, 5), 0, Q(3, 5), 0]), comb([Q(3, 5), 4 * I / 5, 0, 0])], PSI[3], Q(9, 10),
     "triple, third vector outside W, non-orthogonal to g_1"),
    ("NO", [PSI[0], comb([Q(4, 5), 0, Q(3, 5), 0]), comb([0, Q(3, 5), 0, Q(4, 5)])], comb([0, Q(4, 5), 0, -Q(3, 5)]), Q(9, 10),
     "triple, third vector in W^perp (orthogonal to g_1)"),
    ("ZF+", [PSI[0], comb([Q(4, 5), 0, Q(3, 5), 0]), PSI[1], PSI[2], PSI[3]], comb([0, 1 / r2, 0, 1 / r2]), Q(9, 10),
     "Z_F plus (4psi_1+3psi_3)/5 (five members)"),
]
res = {}
for name, gs, e, eps, txt in inst:
    ok, d = witness(gs, e, eps)
    res[name] = d
    rec("CHECK", name, ok, txt + ": y = v v^dag + lambda d_2 in K(Z)* \\ K(Z)",
        "n %d, c12 %s, lambda %s, L1 %s, L2 %s, L3 %s, L4 %s" % (d['n'], d['c12'], d['lam'], d['L1'], d['L2'], d['L3'], d['L4']))

okCC1, dCC1 = witness(inst[0][1], PSI[1], Q(1, 2))
rec("COUNTERCONTROL", "CC1", (not okCC1) and dCC1['L2'][0] < 0,
    "T16 at eps = 1/2 (eps^2 < 2c - 1): L2 fails at k = 2", "L2 %s" % dCC1['L2'])
cc2 = all(ip(dg(PSI[k]), dg(PSI[0])) == 0 for k in range(1, 4))
rec("COUNTERCONTROL", "CC2", cc2, "Z_F: <d_k, d_1> = 0 for k != 1, so L1 cannot be met (no witness of this form; Theorem S)")
rec("COUNTERCONTROL", "CC3", ov(PSI[0], PSI[2]) == 0, "orthogonal pair: c_12 = 0, the construction is undefined")

recorded = []
for d in res.values():
    recorded += [d['c12'], d['lam'], d['L1'], d['L3']] + d['L2'] + d['L4']
rec("CHECK", "EX", not any(sp.sympify(t).has(sp.Float) for t in recorded), "no Float in any recorded value (%d values)" % len(recorded))

nfail = R_.count(False)
print("summary: %d checks, %d failed" % (len(R_), nfail))
if nfail == 0:
    print("VERDICT C8-BELL-SETS-EXACT: K(Z) is not self-dual for %s (witness x^dag y x = %s); the window eps^2 >= 2c - 1 is "
          "necessary in the construction (CC1); Z_F admits no witness of this form" %
          (", ".join(res.keys()), ", ".join("%s" % res[k]['L3'] for k in res)))
else:
    print("NO VERDICT")
