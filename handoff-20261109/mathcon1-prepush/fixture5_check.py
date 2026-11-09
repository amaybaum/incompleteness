"""Independent exact check of MATH-CON-1-S1B-1's fifth pre-F fixture (XC4's path on
B23's UNCONJUGATED attempt). Reconstructs, from BridgeFiniteProtocol.lean and
OperationalAssembly.lean at D = fd539e15, only: v, balancedCircuit, drivePhase,
correction, resetPerm/resetChannel, readProj, uniformAttach, ptraceAnc, conjChannel.
No O-3a-e object (no hdh, no conjugated attempt, no O-3a word) is computed.
Arithmetic in Q(i) as pairs of Fractions. Imports only fractions, itertools, sys."""
from fractions import Fraction as Fr
import itertools, sys

class G:  # Gaussian rational a + b i
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = g(o); return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __neg__(s): return G(-s.a, -s.b)
    def __sub__(s, o): return s + (-g(o))
    def __mul__(s, o): o = g(o); return G(s.a*o.a - s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def conj(s): return G(s.a, -s.b)
    def __eq__(s, o): o = g(o); return s.a == o.a and s.b == o.b
    def __repr__(s): return f"({s.a}+{s.b}i)"
def g(x): return x if isinstance(x, G) else G(x)
I = G(0, 1)

TOK = [0, 1]; ANC = [0, 1, 2, 3]
WORK = list(itertools.product(TOK, ANC))   # Work = Token x Fin 4, token first

def mat(f, idx): return {(r, c): g(f(r, c)) for r in idx for c in idx}
def mul(A, B, idx): return {(r, c): sum((A[(r, k)] * B[(k, c)] for k in idx), G()) for r in idx for c in idx}
def dag(A, idx): return {(r, c): A[(c, r)].conj() for r in idx for c in idx}
def conjch(V, X, idx): return mul(mul(V, X, idx), dag(V, idx), idx)
def add(A, B, idx): return {k: A[k] + B[k] for k in A}
def scal(c, A): return {k: g(c) * v for k, v in A.items()}
def zero(idx): return {(r, c): G() for r in idx for c in idx}
def eye(idx): return mat(lambda r, c: 1 if r == c else 0, idx)
def diag(f, idx): return mat(lambda r, c: f(r) if r == c else 0, idx)

def v(a): return -1 if a in (1, 2) else 1
def balancedCircuit(r, c):
    if r[0] != c[0]: return G()
    d = (G(1) if r[0] == 0 else I) if r[1] == c[1] else G()
    coef = (I - 1) if r[0] == 0 else (G(1) - I)
    return d + coef * G(Fr(1, 4)) * v(r[1]) * v(c[1])
U = mat(balancedCircuit, WORK)
drivePhase = diag(lambda s: G(1) if s == 0 else G(Fr(3, 5), Fr(4, 5)), TOK)
Z = diag(lambda s: 1 if s == 0 else -1, TOK)
def correction(j): return diag(lambda r: 1 if (j == 0 or r[0] == 0) else -1, WORK)
def readProj(j): return diag(lambda r: 1 if r[1] == j else 0, WORK)
def swap(j, a): return 0 if a == j else (j if a == 0 else a)
def resetPerm(j):  # permMatrix (resetEquiv j); swap is an involution so orientation is immaterial
    return mat(lambda r, c: 1 if (r[0] == c[0] and swap(j, r[1]) == c[1]) else 0, WORK)
def resetChannel(X):
    out = zero(WORK)
    for j in ANC: out = add(out, conjch(resetPerm(j), conjch(readProj(j), X, WORK), WORK), WORK)
    return out
def uniformAttach(X): return {(r, c): X[(r[0], c[0])] * G(Fr(1, 4) if r[1] == c[1] else 0) for r in WORK for c in WORK}
def ptraceAnc(M): return {(s, t): sum((M[((s, e), (t, e))] for e in ANC), G()) for s in TOK for t in TOK}

def branch(j, X, corrected=True):
    Y = conjch(U, resetChannel(uniformAttach(X)), WORK)
    Y = conjch(readProj(j), Y, WORK)
    if corrected: Y = conjch(correction(j), Y, WORK)
    return ptraceAnc(Y)

UNITS = [(a, b) for a in TOK for b in TOK]
def unit(a, b): return mat(lambda r, c: 1 if (r, c) == (a, b) else 0, TOK)
def eq(A, B): return all(A[k] == B[k] for k in A)

results = []
def rec(name, ok): results.append((name, ok)); print(("PASS " if ok else "FAIL ") + name)

# Control 0: reconstruction faithful to proved BFP:194 (correction kept).
for j in ANC:
    ok = True
    for a, b in UNITS:
        X = unit(a, b)
        exp = scal(Fr(5, 8), conjch(drivePhase, X, TOK)) if j == 0 else scal(Fr(1, 8), X)
        ok &= eq(branch(j, X), exp)
    rec(f"C0 BFP:194 outcome {j} (correction kept)", ok)
# Control 1: correction j = Z (x) 1 for j != 0, = 1 for j = 0 (BFP:170).
for j in ANC:
    exp = eye(WORK) if j == 0 else {(r, c): (Z[(r[0], c[0])] if r[1] == c[1] else G()) for r in WORK for c in WORK}
    rec(f"C1 correction {j} {'= 1' if j == 0 else '= Z(x)1'}", eq(correction(j), exp))
# Fixture 5: correction removed, outcomes 1-3, all four units: equals (1/8)Ad(Z), differs from (1/8)id.
xc4_fails_as_stated = True
for j in (1, 2, 3):
    br = {u: branch(j, unit(*u), corrected=False) for u in UNITS}
    isAdZ = all(eq(br[u], scal(Fr(1, 8), conjch(Z, unit(*u), TOK))) for u in UNITS)
    eqId = all(eq(br[u], scal(Fr(1, 8), unit(*u))) for u in UNITS)
    diffunits = [u for u in UNITS if not eq(br[u], scal(Fr(1, 8), unit(*u)))]
    rec(f"F5 outcome {j}: uncorrected branch = (1/8)Ad(Z) on all four units", isAdZ)
    rec(f"F5 outcome {j}: differs from (1/8)id exactly on off-diagonal units {diffunits}", (not eqId) and diffunits == [(0, 1), (1, 0)])
    xc4_fails_as_stated &= not eqId
rec("F5 XC4 (any-branch-equal => not failing) reports FAILING AS STATED on the fixture", xc4_fails_as_stated)
# Countercontrol: the same comparator on the CORRECTED branches (X3b's object) must report NOT failing.
nf = any(all(eq(branch(j, unit(*u)), scal(Fr(1, 8), unit(*u))) for u in UNITS) for j in (1, 2, 3))
rec("CC comparator on corrected branches reports NOT failing (comparator is not vacuous)", nf)
# Countercontrol: diagonal units alone cannot detect the difference.
diag_only = all(eq(branch(j, unit(a, a), corrected=False), scal(Fr(1, 8), unit(a, a))) for j in (1, 2, 3) for a in TOK)
rec("CC diagonal units alone equal (1/8)id (all four units are needed)", diag_only)
# Countercontrol: outcome 0 is unchanged by removing the correction (the original defect).
o0 = all(eq(branch(0, unit(*u), corrected=False), branch(0, unit(*u))) for u in UNITS)
rec("CC outcome 0 unchanged by removing correction (original XC4 defect reproduced)", o0)
# Quantifier contrast on a synthetic triple: one branch equal to (1/8)id, two differing.
trip = [True, False, False]   # equals (1/8)id ?
rec("Q 'any' rule flags not-failing when one of three branches equals (1/8)id", any(trip))
rec("Q 'all' rule would NOT flag it (weaker countercontrol)", not all(trip))
bad = [n for n, ok in results if not ok]
print(f"total {len(results)}, failing {len(bad)}")
sys.exit(1 if bad else 0)
