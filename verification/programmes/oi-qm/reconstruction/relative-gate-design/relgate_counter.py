"""Exact countercontrol for the relative-gate transport (scratch probe, not a round artifact).

Claim checked: at d = 3, with the one-axis family `axisFamily` (EffectSpace.lean:811), the gate
T_S = (actT S . actC S) . cnot, S = diag(2, 1, 1), meets every clause of K1Bridge.NativeGateOf
(eball 3) axisFamily z3 nflip (frame, relT, relC exactly; the two relative positivity clauses by
the coefficient identity C5 together with the landed cnot_prodState_mem_maxCone), while
T_S (prodState z3 xplus) takes the value -1/2 on the product of the sharp effects along e3 and
-e1, both effects of eball 3, so T_S is not a NativeGate (eball 3) z3 nflip: without the cone
equality the transport NativeGate(2)Of -> NativeGate(2) fails.

Python standard library only, exact rationals. Usage: python3 -I relgate_counter.py <CompositeDimension.lean>
"""
import re
import sys
from fractions import Fraction as Q
from itertools import product

src = open(sys.argv[1], encoding="utf-8").read()

# --- kernel cnot tables, parsed from CompositeDimension.lean -------------------------------
def table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)" % name, src)
    t = {}
    for a, b, c in re.findall(r"\| (\d), (\d) => (\d)", m.group(1)):
        t[(int(a), int(b))] = int(c)
    assert len(t) == 16, name
    return t

PC, PT = table("pc"), table("pt")
m = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if (.*) then -1 else 1", src)
NEG = {(int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", m.group(1))}
assert NEG == {(1, 3), (2, 2)}, NEG
m = re.search(r"def nflip[^\n]*\n  toFun x := fun i => \(!\[(.*?)\]", src)
NFLIP = [Q(int(s)) for s in m.group(1).split(",")]
m = re.search(r"def z3 : Fin 3 → ℝ := !\[(.*?)\]", src)
Z3 = [Q(int(s)) for s in m.group(1).split(",")]
m = re.search(r"def xplus : Fin 3 → ℝ := !\[(.*?)\]", src)
XPLUS = [Q(int(s)) for s in m.group(1).split(",")]

def sgn(mu, nu):
    return -1 if (mu, nu) in NEG else 1

def cnot(w):
    return [[sgn(mu, nu) * w[PC[(mu, nu)]][PT[(mu, nu)]] for nu in range(4)] for mu in range(4)]

# --- carrier ------------------------------------------------------------------------------
def diag(v):
    return [[v[i] if i == j else Q(0) for j in range(3)] for i in range(3)]

def apply(M, x):
    return [sum(M[i][j] * x[j] for j in range(3)) for i in range(3)]

def hom(x):
    return [Q(1)] + list(x)

def homMap(M, v):
    return [v[0]] + apply(M, v[1:])

def actT(M, w):
    return [homMap(M, w[mu]) for mu in range(4)]

def actC(M, w):
    cols = [homMap(M, [w[k][nu] for k in range(4)]) for nu in range(4)]
    return [[cols[nu][mu] for nu in range(4)] for mu in range(4)]

def prodState(x, y):
    hx, hy = hom(x), hom(y)
    return [[hx[mu] * hy[nu] for nu in range(4)] for mu in range(4)]

def pairVal(a, b, w):
    return sum(a[mu] * w[mu][nu] * b[nu] for mu in range(4) for nu in range(4))

def sharpVec(b):  # EffectSpace.sharpVec: (1/2, b/2)
    return [Q(1, 2)] + [Q(c) / 2 for c in b]

UNIT = [Q(1), Q(0), Q(0), Q(0)]
AXIS = [UNIT, sharpVec([0, 0, 1]), sharpVec([0, 0, -1])]  # axisFamily, EffectSpace.lean:811

N = diag(NFLIP)
S = diag([Q(2), Q(1), Q(1)])
Sinv = diag([Q(1, 2), Q(1), Q(1)])
ID = diag([Q(1)] * 3)

def gate(M):
    return lambda w: actT(M, actC(M, cnot(w)))

def gate_inv(Minv):
    return lambda w: cnot(actC(Minv, actT(Minv, w)))

def neg(x):
    return [-c for c in x]

def basis():
    for i, j in product(range(4), range(4)):
        yield [[Q(1) if (a, b) == (i, j) else Q(0) for b in range(4)] for a in range(4)]

checks, failures = 0, 0

def check(name, ok, detail=""):
    global checks, failures
    checks += 1
    if not ok:
        failures += 1
    print(("PASS " if ok else "FAIL ") + name + (" " + detail if detail else ""))

corner = [Z3, neg(Z3)]

def frame_ok(T):
    return all(T(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
               for a in range(2) for b in range(2))

def relT_ok(T):
    return all(actT(N, T(actT(N, w))) == T(w) for w in basis())

def relC_ok(T):
    return all(actC(N, T(actC(N, w))) == actT(N, T(w)) for w in basis())

# P0: the parsed kernel cnot meets the one-NOT clauses (cnot_frame, cnot_relT, cnot_relC)
T0 = gate(ID)
check("P0 kernel cnot: frame, relT, relC with nflip",
      frame_ok(cnot) and relT_ok(cnot) and relC_ok(cnot) and all(T0(w) == cnot(w) for w in basis()))

TS, TSinv = gate(S), gate_inv(Sinv)
check("C1 T_S frame at the four corners", frame_ok(TS))
check("C2 T_S relT with nflip", relT_ok(TS))
check("C3 T_S relC with nflip", relC_ok(TS))
check("C4 T_S^-1 is the inverse of T_S",
      all(TS(TSinv(w)) == w and TSinv(TS(w)) == w for w in basis()))

# C5: hat(S)^T a = a for every axisFamily coefficient vector a, so
# pairVal a b (actT S (actC S w)) = pairVal a b w for a, b in axisFamily
def hatT_apply(M, a):
    return [a[0]] + [sum(M[j][k] * a[j + 1] for j in range(3)) for k in range(3)]

check("C5 axisFamily coefficients fixed by hat(S)^T",
      all(hatT_apply(S, a) == a for a in AXIS) and
      all(pairVal(a, b, actT(S, actC(S, w))) == pairVal(a, b, w)
          for a in AXIS for b in AXIS for w in basis()))

# C6: sample of rational ball points; relative positivity of T_S and T_S^-1 on product states
pts = []
grid = [Q(k, 4) for k in range(-4, 5)]
for x in product(grid, repeat=3):
    if sum(c * c for c in x) <= 1:
        pts.append(list(x))
ok = True
for x in pts[::7]:
    for y in pts[::11]:
        for w in (TS(prodState(x, y)), TSinv(prodState(x, y))):
            if any(pairVal(a, b, w) < 0 for a in AXIS for b in AXIS):
                ok = False
check("C6 sampled relative positivity (axisFamily) of T_S and T_S^-1", ok,
      "(%d x %d sampled pairs; universal by C5 + cnot_prodState_mem_maxCone)" %
      (len(pts[::7]), len(pts[::11])))

# C7: the violation
w = TS(prodState(Z3, XPLUS))
e, f = sharpVec([0, 0, 1]), sharpVec([-1, 0, 0])
val = pairVal(e, f, w)
check("C7 T_S (prodState z3 xplus) on sharpEff e3 (x) sharpEff (-e1) is -1/2", val == Q(-1, 2),
      "value %s" % val)
check("C7b T_S (prodState z3 xplus) = prodState z3 (S xplus)", w == prodState(Z3, apply(S, XPLUS)))

# C8: control for C7 -- the same evaluation on the kernel cnot is nonnegative
val0 = pairVal(e, f, cnot(prodState(Z3, XPLUS)))
check("C8 same pair on cnot (prodState z3 xplus) is nonnegative", val0 >= 0, "value %s" % val0)

# C9: S does not preserve the ball (the conjugator hypotheses of #822 are not met by S)
check("C9 S xplus lies outside eball 3", sum(c * c for c in apply(S, XPLUS)) > 1)

print("checks: %d, failures: %d" % (checks, failures))
print("VERDICT " + ("TRANSPORT-NEEDS-CONE-EQUALITY" if failures == 0 else "NOT-ESTABLISHED"))
