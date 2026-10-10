# b4_realization.py -- research/bridge node B4: an embedded-observer realization of the exotic pair K(Z_F), built
# exactly with the framework's own finite reversible machinery (Main.md:544-558) in its adopted Bell branch (a)
# (Main.md:392, ontic parameter dependence), and the exact obstruction to adding the token's off-frame operations.
# Exact arithmetic only (Fraction; sympy only for the comparison dictionary).
#
# DECISION RULE (fixed before the first run, 2026-10-10T20:37Z by date -u):
#  Model (finite, deterministic, reversible).  Visible sector: step counter t, the record of (instrument, outcome).
#  Hidden sector: two wing registers hA, hB, each holding a normalized joint table w in W 3 (branch (a): "the
#  composite ... carries the joint history in each wing", Main.md:392), one seed per measurement step in
#  {0,...,G-1}, G = 20, and a predecessor stack.  Instruments (each one fixed map, applied in every context):
#   G   : both registers <- cnot(w)                        (the native gate as a permutation of register values)
#   NA/NB: both registers <- actC/actT nflip (w)            (the NOT on either token)
#   MA a: q = pairVal(sharpVec a, unit, hA); outcome + iff seed < G q (exact integer threshold); both registers <-
#         prodState(o a, conditional Bloch vector of B)     (measure-and-prepare on A; A's local intervention updates
#         B's register: parameter dependence)
#   MB b: symmetric on B.
#   MJ y: the two-outcome joint measurement {y, E00 - y} with y certified in K(Z_F) and E00 - y certified in K(Z_F)
#         (K = K*): q = <y, hA>; outcome 1 iff seed < G q; both registers <- prodState(0, 0).
#   PROBE g: both registers <- actC g (w)   (the token's operation g applied in the pair context; tested, not adopted)
#  Preparation: w0 = 4 z_(1,1) (normalized Bell-type defect of K(Z_F)).  Settings A in {x,y,z}, B in {x,y,z,b0,b1},
#  b0 = (-3/5,0,4/5), b1 = (3/5,0,4/5).  Protocols: [MA a, MB b], [MB b, MA a], [G, MA a, MB b], [NA, MA a, MB b],
#  [MJ y], [G, MJ y].  Realized law = exact frequencies over all seeds of the measurement steps.
#  CHECKS:
#   R1 realized law == GPT law (pairVal of the effects on w0, cnot w0, actC nflip w0; <y, w0>) for every protocol;
#   R2 every threshold G q of every reachable step is an integer in [0, G] (validity of the realization);
#   R3 no-signalling: B's marginal in [MA a, MB b] does not depend on a; A's marginal in [MB b, MA a] not on b;
#   R4 local measurements commute operationally: law[MA a, MB b] == law[MB b, MA a] (as laws of (oA, oB));
#   R5 parameter dependence: after MA, the register hB depends on A's setting a (exhibited);
#   R6 the two wing registers agree on every reachable configuration;
#   R7 every step map is injective on its reachable configurations (stack + seeds kept);
#   R8 cnot, actC nflip, actT nflip are bijections of the reachable register set closed under them;
#   R9 non-quantum: the realized expectations on axis settings reconstruct w0 exactly, and (comparison dictionary)
#      tr(M(w0) P_(1,1)) < 0, so no two-qubit density matrix has these statistics;
#   R10 the realized CHSH value with a0 = x, a1 = z, b0, b1 is measured; pass iff > 2;
#   R11 OBSTRUCTION: for g in {S = R_z(pi/2), cyc3, R_z(th)} (cos th = 3/5): a certified y_g with E00 - y_g also
#       certified, such that [PROBE g, MJ y_g] has threshold q = <y_g, actC g w0> < 0 (no valid realization);
#       y_g is the most negative over the pool {act_tau(h) p_u : h in quarter turns about x,y,z (+-), cyc3^(+-1)}
#       and the constructed Bell-type table with correlation block -g T_s;
#   R12 Q3 CONTROL: with the preparation phiW (CD:1220) in place of w0, [PROBE g, MJ y_g] and [PROBE g, MA a, MB b]
#       have every threshold in [0, G q]-range, i.e. q in [0, 1], for the same g, y_g, a, b;
#   R13 ISOLATED TOKEN: S and cyc3 permute the six axis points (a finite token register), R_z(th) preserves the norm
#       of the listed rational points (available on the token alone).
#  Pre-run edit (20:39Z by date -u, before the first run): the R8 closure is iterated to a fixed point (one round could leave
#  it unclosed and fail spuriously).
#  VERDICT LINES: "EXOTIC PAIR K(Z_F) REALIZED BY EMBEDDED OBSERVERS (BRANCH (a), EXACT)" iff R1-R10 pass;
#  "THE TOKEN'S S, J, R_z(th) ARE NOT INSTRUMENTS OF THE REALIZED PAIR, THOUGH AVAILABLE TO THE ISOLATED TOKEN" iff
#  R11 and R13; "Q3 CONTROL: THE SAME MACHINERY ADMITS THEM" iff R12.  Overall "VERDICT B4-REALIZATION-EXACT" iff
#  R1-R13 pass; else "VERDICT NONE".
from fractions import Fraction as F
from itertools import product
import sympy as sp

RES = []
def check(name, ok, info=""):
    RES.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'} {info}")

G = 20
def tup(w): return tuple(tuple(F(c) for c in r) for r in w)
def hom(x): return [F(1)] + [F(v) for v in x]
def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return tup([[hx[m] * hy[n] for n in range(4)] for m in range(4)])
def Hom(N):
    H = [[F(0)] * 4 for _ in range(4)]
    H[0][0] = F(1)
    for i in range(3):
        for j in range(3):
            H[i + 1][j + 1] = F(N[i][j])
    return H
def mm(a, b): return [[sum(F(a[i][k]) * F(b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def T_(a): return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def actC(N, w): return tup(mm(Hom(N), w))
def actT(N, w): return tup(mm(w, T_(Hom(N))))
def act(tau, N, w): return actC(N, w) if tau == "C" else actT(N, w)
def SGN(m, n): return -1 if (m, n) in ((1, 3), (2, 2)) else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def cnot(w): return tup([[SGN(m, n) * F(w[PC[m][n]][PT[m][n]]) for n in range(4)] for m in range(4)])
def pairVal(a, b, w): return sum(F(a[m]) * F(w[m][n]) * F(b[n]) for m in range(4) for n in range(4))
def ip(a, b): return sum(F(a[i][j]) * F(b[i][j]) for i in range(4) for j in range(4))
def sharpVec(v): return [F(1, 2)] + [F(c) / 2 for c in v]
UNIT = [F(1), F(0), F(0), F(0)]
def E(m, n): return tup([[F(1) if (i, j) == (m, n) else F(0) for j in range(4)] for i in range(4)])
def lin(*terms):
    out = [[F(0)] * 4 for _ in range(4)]
    for c, M in terms:
        for i in range(4):
            for j in range(4):
                out[i][j] += F(c) * F(M[i][j])
    return tup(out)
I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
nflip = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
Sg = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
def Rx(c, s): return [[1, 0, 0], [0, c, -s], [0, s, c]]
def Ry(c, s): return [[c, 0, s], [0, 1, 0], [-s, 0, c]]
def Rz(c, s): return [[c, -s, 0], [s, c, 0], [0, 0, 1]]
th = (F(3, 5), F(4, 5))
SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def zs(s1, s2): return lin((F(1, 4), E(0, 0)), (F(s1, 4), E(1, 3)), (F(s2, 4), E(2, 2)), (F(-s1 * s2, 4), E(3, 1)))
def ps(s1, s2): return lin((F(1, 4), E(0, 0)), (F(-s1, 4), E(1, 3)), (F(-s2, 4), E(2, 2)), (F(s1 * s2, 4), E(3, 1)))
ZF = {s: zs(*s) for s in SIGNS}
PS = {s: ps(*s) for s in SIGNS}
w0 = lin((4, ZF[(1, 1)]))
phiW = tup([[F(1) if i == j and i != 2 else (F(-1) if i == j == 2 else F(0)) for j in range(4)] for i in range(4)])
X_, Y_, Z_ = [1, 0, 0], [0, 1, 0], [0, 0, 1]
b0, b1 = [F(-3, 5), F(0), F(4, 5)], [F(3, 5), F(0), F(4, 5)]
ASET = {"x": X_, "y": Y_, "z": Z_}
BSET = {"x": X_, "y": Y_, "z": Z_, "b0": b0, "b1": b1}

# ---------- comparison dictionary (verification tool only) ----------
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
SIG = [I2, X, Y, Z]
SS = [[sp.kronecker_product(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
def Mdict(w): return sum((sp.Rational(F(w[m][n]).numerator, F(w[m][n]).denominator) * SS[m][n]
                          for m in range(4) for n in range(4)), sp.zeros(4, 4))
lam = sp.symbols('lam')
def is_psd(Mx):
    cp = sp.Poly(sp.expand((Mx - lam * sp.eye(4)).det()), lam).all_coeffs()
    return all(sp.im(c) == 0 and (-1) ** k * c >= 0 for k, c in enumerate(cp))
def in_K(y): return is_psd(Mdict(y)) and all(ip(y, z) >= 0 for z in ZF.values())

# ---------- the machine ----------
class Invalid(Exception):
    pass
def threshold(q):
    t = G * q
    if t.denominator != 1 or t < 0 or t > G:
        raise Invalid(f"threshold {t}")
    return int(t)
def step(conf, instr, seed):
    t, rec, hA, hB, stack = conf
    kind = instr[0]
    out = None
    if kind == "G":
        new = cnot(hA)
    elif kind == "NA":
        new = actC(nflip, hA)
    elif kind == "NB":
        new = actT(nflip, hB)
    elif kind == "PROBE":
        new = actC(instr[1], hA)
    elif kind == "MA":
        a = instr[1]
        qp = pairVal(sharpVec(a), UNIT, hA)
        out = 1 if seed < threshold(qp) else -1
        q = qp if out == 1 else 1 - qp
        s = sharpVec([out * c for c in a])
        cond = [sum(s[m] * F(hA[m][n]) for m in range(4)) / q for n in range(1, 4)]
        new = prodState([out * F(c) for c in a], cond)
    elif kind == "MB":
        b = instr[1]
        qp = pairVal(UNIT, sharpVec(b), hB)
        out = 1 if seed < threshold(qp) else -1
        q = qp if out == 1 else 1 - qp
        s = sharpVec([out * c for c in b])
        cond = [sum(F(hB[m][n]) * s[n] for n in range(4)) / q for m in range(1, 4)]
        new = prodState(cond, [out * F(c) for c in b])
    elif kind == "MJ":
        y = instr[1]
        qp = ip(y, hA)
        out = 1 if seed < threshold(qp) else 0
        new = prodState([0, 0, 0], [0, 0, 0])
    else:
        raise ValueError(kind)
    return (t + 1, rec + ((instr[0], out),), new, new, stack + ((hA, hB),))
def is_meas(instr): return instr[0] in ("MA", "MB", "MJ")
def run(protocol, winit):
    nm = sum(1 for i in protocol if is_meas(i))
    law, confs = {}, [set() for _ in range(len(protocol) + 1)]
    steps = [dict() for _ in range(len(protocol))]
    for seeds in product(range(G), repeat=nm):
        conf = (0, (), winit, winit, ())
        confs[0].add((conf, seeds))
        k = 0
        for i, instr in enumerate(protocol):
            sd = seeds[k] if is_meas(instr) else None
            if is_meas(instr):
                k += 1
            new = step(conf, instr, sd)
            key = (conf, seeds)
            if key in steps[i] and steps[i][key] != new:
                raise RuntimeError("non-deterministic")
            steps[i][key] = new
            conf = new
            confs[i + 1].add((conf, seeds))
        outs = tuple(o for (_, o) in conf[1] if o is not None)
        law[outs] = law.get(outs, F(0)) + F(1, G ** nm)
    inj = all(len(set((v, k[1]) for k, v in steps[i].items())) == len(steps[i]) for i in range(len(protocol)))
    sync = all(c[2] == c[3] for lev in confs for (c, _) in lev)
    regs = set(c[2] for lev in confs for (c, _) in lev)
    return law, inj, sync, regs

# ---------- GPT laws ----------
def law_AB(w, a, b):
    return {(oA, oB): pairVal(sharpVec([oA * c for c in a]), sharpVec([oB * c for c in b]), w)
            for oA in (1, -1) for oB in (1, -1)}

# ---------- R1-R8 ----------
r1 = r2 = r6 = r7 = True
REG = set()
laws = {}
try:
    for an, a in ASET.items():
        for bn, b in BSET.items():
            for pname, prot, wexp in (("AB", [("MA", a), ("MB", b)], w0), ("BA", [("MB", b), ("MA", a)], w0),
                                      ("GAB", [("G",), ("MA", a), ("MB", b)], cnot(w0)),
                                      ("NAB", [("NA",), ("MA", a), ("MB", b)], actC(nflip, w0))):
                law, inj, sync, regs = run(prot, w0)
                REG |= regs
                if pname == "BA":
                    law = {(oA, oB): p for (oB, oA), p in law.items()}
                laws[(pname, an, bn)] = law
                exp = law_AB(wexp, a, b)
                r1 &= all(law.get(k, F(0)) == v for k, v in exp.items()) and sum(law.values()) == 1
                r7 &= inj
                r6 &= sync
except Invalid as e:
    r2 = False
    print(f"INFO invalid threshold in the K(Z_F) family: {e}")
# joint measurement y_J chosen in R11 below; here the plain [MJ y] and [G, MJ y] use the pool element of R11
# ---------- R11 pool and witnesses ----------
QT = [Rx(0, 1), Rx(0, -1), Ry(0, 1), Ry(0, -1), Rz(0, 1), Rz(0, -1), cyc3, T_(cyc3), I3]
POOL = []
for h in QT:
    for tau in "CT":
        for u in SIGNS:
            POOL.append(act(tau, h, PS[u]))
def T_of(w): return [[F(w[i + 1][j + 1]) / F(w[0][0]) for j in range(3)] for i in range(3)]
Ts = T_of(w0)
def bell_from_block(Tb): return lin((F(1, 4), E(0, 0)), *[(F(-Tb[i][j], 4), E(i + 1, j + 1)) for i in range(3) for j in range(3)])
def mul3(A, B): return [[sum(F(A[i][k]) * F(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
PROBES = {"S": Sg, "cyc3": cyc3, "R_z(th)": Rz(*th)}
YG = {}
r11 = True
for gn, g in PROBES.items():
    cands = POOL + [bell_from_block(mul3(g, Ts))]
    best = None
    for y in cands:
        if not all(ip(y, z) >= 0 for z in ZF.values()):
            continue
        q = ip(y, actC(g, w0))
        if best is None or q < best[0]:
            best = (q, y)
    y = best[1]
    comp = lin((1, E(0, 0)), (-1, y))
    cert = in_K(y) and in_K(comp)
    YG[gn] = y
    neg = False
    try:
        run([("PROBE", g), ("MJ", y)], w0)
    except Invalid as e:
        neg = True
    r11 &= cert and best[0] < 0 and neg
    print(f"INFO probe {gn}: q = <y_g, actC g w0> = {best[0]}; y_g and E00 - y_g certified in K: {cert}; "
          f"realization raises an invalid threshold: {neg}")
# the joint measurements themselves are valid instruments of the K(Z_F) family on w0 and on cnot w0
try:
    for gn, y in YG.items():
        for prot, wexp in (([("MJ", y)], w0), ([("G",), ("MJ", y)], cnot(w0))):
            law, inj, sync, regs = run(prot, w0)
            REG |= regs
            r1 &= law.get((1,), F(0)) == ip(y, wexp)
            r7 &= inj
            r6 &= sync
except Invalid as e:
    r2 = False
    print(f"INFO invalid threshold in a joint measurement of the K(Z_F) family: {e}")
check("R1 realized law equals the K(Z_F) law on every protocol", r1)
check("R2 every threshold of the K(Z_F) family is an integer in [0, G]", r2)
r3 = all(sum(p for (oA, oB), p in laws[("AB", an, bn)].items() if oB == ob) ==
         sum(p for (oA, oB), p in laws[("AB", "x", bn)].items() if oB == ob)
         for an in ASET for bn in BSET for ob in (1, -1)) and \
     all(sum(p for (oA, oB), p in laws[("BA", an, bn)].items() if oA == oa) ==
         sum(p for (oA, oB), p in laws[("BA", an, "x")].items() if oA == oa)
         for an in ASET for bn in BSET for oa in (1, -1))
check("R3 operational no-signalling (both directions)", r3)
r4 = all(laws[("AB", an, bn)] == laws[("BA", an, bn)] for an in ASET for bn in BSET)
check("R4 local measurements commute operationally", r4)
cx = step((0, (), w0, w0, ()), ("MA", X_), 0)
cz = step((0, (), w0, w0, ()), ("MA", Z_), 0)
r5 = cx[3] != cz[3]
check("R5 parameter dependence: B's register after MA depends on A's setting", r5,
      f"hB after MA(x) = {[[str(c) for c in r] for r in cx[3]]} vs MA(z) = {[[str(c) for c in r] for r in cz[3]]}")
check("R6 the two wing registers agree on every reachable configuration", r6)
check("R7 every step map is injective on its reachable configurations", r7)
closure = set(REG)
while True:
    grown = set(closure)
    for f in (cnot, lambda w: actC(nflip, w), lambda w: actT(nflip, w)):
        grown |= set(f(w) for w in closure)
    if grown == closure:
        break
    closure = grown
r8 = all(len(set(f(w) for w in closure)) == len(closure) and set(f(w) for w in closure) == closure
         for f in (cnot, lambda w: actC(nflip, w), lambda w: actT(nflip, w)))
check("R8 cnot and both NOTs are bijections of the closed reachable register set", r8, f"(|set| = {len(closure)})")
# ---------- R9 ----------
def exp1(law, who):
    return sum((oA if who == "A" else oB) * p for (oA, oB), p in law.items())
def expAB(law): return sum(oA * oB * p for (oA, oB), p in law.items())
axes = ["x", "y", "z"]
what = [[F(0)] * 4 for _ in range(4)]
what[0][0] = F(1)
for i, an in enumerate(axes):
    what[i + 1][0] = exp1(laws[("AB", an, "x")], "A")
    what[0][i + 1] = exp1(laws[("AB", "x", an)], "B")
    for j, bn in enumerate(axes):
        what[i + 1][j + 1] = expAB(laws[("AB", an, bn)])
P11 = (sp.eye(4) - SS[1][3] - SS[2][2] + SS[3][1]) / 4
negq = sp.expand((Mdict(w0) * P11).trace())
check("R9 realized axis statistics reconstruct w0; tr(M(w0) P_(1,1)) < 0 (not quantum)", tup(what) == w0 and negq < 0,
      f"tr = {negq}")
# ---------- R10 ----------
def Eab(an, bn): return expAB(laws[("AB", an, bn)])
S_real = Eab("x", "b0") + Eab("x", "b1") + Eab("z", "b0") - Eab("z", "b1")
check("R10 realized CHSH exceeds 2", S_real > 2, f"S = {S_real}")
check("R11 S, cyc3, R_z(th) on A raise an invalid threshold before a valid K(Z_F) joint measurement", r11)
# ---------- R12 ----------
r12 = True
for gn, g in PROBES.items():
    try:
        run([("PROBE", g), ("MJ", YG[gn])], phiW)
    except Invalid as e:
        r12 = False
        print(f"INFO Q3 control failed for {gn}: {e}")
    for an, a in ASET.items():
        for bn, b in BSET.items():
            q = law_AB(actC(g, phiW), a, b)
            r12 &= all(F(0) <= v <= 1 for v in q.values())
    q = ip(YG[gn], actC(g, phiW))
    print(f"INFO Q3 control {gn}: <y_g, actC g phiW> = {q}")
    r12 &= F(0) <= q <= 1
check("R12 Q3 control: the same probes and measurements are valid on phiW", r12)
# ---------- R13 ----------
axpts = [tuple(F(c) for c in v) for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1])]
def ap(N, v): return tuple(sum(F(N[i][k]) * v[k] for k in range(3)) for i in range(3))
r13 = all(set(ap(N, v) for v in axpts) == set(axpts) for N in (Sg, cyc3)) and \
    all(sum(c * c for c in ap(Rz(*th), v)) == sum(c * c for c in v) for v in axpts + [(F(1, 3), F(2, 3), F(-2, 3))])
check("R13 isolated token: S, cyc3 permute the axis register; R_z(th) preserves the ball", r13)

ok = dict(RES)
if all(ok[k] for k in ok if k.startswith(("R1 ", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"))):
    print("RESULT EXOTIC PAIR K(Z_F) REALIZED BY EMBEDDED OBSERVERS (BRANCH (a), EXACT)")
if r11 and r13:
    print("RESULT THE TOKEN'S S, J, R_z(th) ARE NOT INSTRUMENTS OF THE REALIZED PAIR, THOUGH AVAILABLE TO THE ISOLATED TOKEN")
if r12:
    print("RESULT Q3 CONTROL: THE SAME MACHINERY ADMITS THEM")
allok = all(o for _, o in RES)
print(f"SUMMARY {sum(o for _, o in RES)}/{len(RES)} checks pass")
print("VERDICT B4-REALIZATION-EXACT" if allok else "VERDICT NONE")
