"""Exact checks for thread B's interface lemmas (standard library only).

Arithmetic is exact in Q(sqrt2)(i): a number is (a, b, c, d) meaning
a + b*sqrt2 + i*(c + d*sqrt2) with Fractions.  Carriers are bit strings with
token 0 the most significant bit, matching Bits (n+1) = Bits n x Fin 2 of the
research module FinitePauli.lean (last token = rightmost factor).

Closed forms used (kernel facts, not re-derived here):
  flow (transition a b) s = 1 + (cos s - 1) P_ab - i sin s X_ab   (a != b; LiftAudit.lean:276)
  flow (transition a a) s = 1 + (exp(-2 i s) - 1) E_aa            (KnDescentDesign.lean:109)
"""
from fractions import Fraction as Fr
import itertools, sys

class Q:
    __slots__ = ("v",)
    def __init__(self, a=0, b=0, c=0, d=0):
        self.v = (Fr(a), Fr(b), Fr(c), Fr(d))
    def __add__(s, o): o = q(o); return Q(*(x + y for x, y in zip(s.v, o.v)))
    __radd__ = __add__
    def __neg__(s): return Q(*(-x for x in s.v))
    def __sub__(s, o): return s + (-q(o))
    def __rsub__(s, o): return q(o) - s
    def __mul__(s, o):
        o = q(o); a, b, c, d = s.v; e, f, g, h = o.v
        # (A + iC)(E + iG), A = a + b r, etc., r^2 = 2
        def m(x1, x2, y1, y2):  # (x1 + x2 r)(y1 + y2 r)
            return (x1 * y1 + 2 * x2 * y2, x1 * y2 + x2 * y1)
        re1 = m(a, b, e, f); re2 = m(c, d, g, h)
        im1 = m(a, b, g, h); im2 = m(c, d, e, f)
        return Q(re1[0] - re2[0], re1[1] - re2[1], im1[0] + im2[0], im1[1] + im2[1])
    __rmul__ = __mul__
    def conj(s): a, b, c, d = s.v; return Q(a, b, -c, -d)
    def __eq__(s, o): return s.v == q(o).v
    def iszero(s): return all(x == 0 for x in s.v)
    def __repr__(s): return "Q%s" % (tuple(str(x) for x in s.v),)

def q(x): return x if isinstance(x, Q) else Q(x)
I = Q(0, 0, 1, 0)
R2 = Q(0, 1)            # sqrt 2
INV_R2 = Q(0, Fr(1, 2))  # 1/sqrt2

def zeros(n): return [[Q() for _ in range(n)] for _ in range(n)]
def eye(n):
    m = zeros(n)
    for i in range(n): m[i][i] = Q(1)
    return m
def mul(A, B):
    n = len(A); C = zeros(n)
    for i in range(n):
        for k in range(n):
            if A[i][k].iszero(): continue
            for j in range(n):
                if not B[k][j].iszero():
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C
def prod(ms, n):
    out = eye(n)
    for m in ms: out = mul(out, m)
    return out
def dag(A):
    n = len(A); return [[A[j][i].conj() for j in range(n)] for i in range(n)]
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))
def kron(A, B):
    n, m = len(A), len(B); C = zeros(n * m)
    for i, j, k, l in itertools.product(range(n), range(n), range(m), range(m)):
        C[i * m + k][j * m + l] = A[i][j] * B[k][l]
    return C

# --- elementary generators (DrivesElementaryAt) ---
def transition_flow(n, a, b, c, s):  # cos, sin exact; a != b
    M = eye(n)
    for x in (a, b): M[x][x] = M[x][x] + (c - 1)
    M[a][b] = M[a][b] - s * I; M[b][a] = M[b][a] - s * I
    return M
def self_flow(n, a, z):  # flow (transition a a) s with exp(-2 i s) = z
    M = eye(n); M[a][a] = q(z); return M
def perm_swap(n, a, b):
    M = zeros(n)
    for x in range(n):
        y = b if x == a else a if x == b else x
        M[y][x] = Q(1)
    return M
def phase_gate(n, a):
    M = eye(n); M[a][a] = I; return M

# --- k-token cone generator lifts ---
def bit(a, j, k): return (a >> (k - 1 - j)) & 1
def flipbit(a, j, k): return a ^ (1 << (k - 1 - j))
def local(k, j, U):
    out = [[Q(1)]]
    for t in range(k):
        out = kron(out, U if t == j else eye(2))
    return out
def cnotK(k, i, j):
    n = 2 ** k; M = zeros(n)
    for a in range(n):
        b = flipbit(a, j, k) if bit(a, i, k) else a
        M[b][a] = Q(1)
    return M
def phaseMat(c, s): return [[Q(1), Q()], [Q(), q(c) + q(s) * I]]
cycMat = [[Q(Fr(1, 2), 0, Fr(-1, 2)), Q(Fr(-1, 2), 0, Fr(-1, 2))],
          [Q(Fr(1, 2), 0, Fr(-1, 2)), Q(Fr(1, 2), 0, Fr(1, 2))]]   # EqvK2Converse.lean:106
E_M = Q(0, Fr(1, 2), 0, Fr(-1, 2))  # e^{-i pi/4} = (1 - i)/sqrt2
E_P = Q(0, Fr(1, 2), 0, Fr(1, 2))   # e^{+i pi/4}

def is_monomial(M):
    n = len(M)
    rows = all(sum(not M[i][j].iszero() for j in range(n)) == 1 for i in range(n))
    cols = all(sum(not M[i][j].iszero() for i in range(n)) == 1 for j in range(n))
    return rows and cols
def is_diagonal(M):
    return all(M[i][j].iszero() for i in range(len(M)) for j in range(len(M)) if i != j)
def commutes(A, B): return meq(mul(A, B), mul(B, A))

checks, failures = [], []
def check(label, ok):
    (checks if ok else failures).append(label)
    print(("PASS " if ok else "FAIL ") + label)

C35, S35 = Fr(3, 5), Fr(4, 5)

# A0: arithmetic controls (the field operations themselves).
check("A0-FIELD", R2 * R2 == Q(2) and I * I == Q(-1) and E_M * E_P == Q(1)
      and E_M * E_M == Q(0, 0, -1) and INV_R2 * R2 == Q(1) and not (Q(1) == Q(0, 0, 1)))
# A1: k = 2 encodings agree with the landed pair matrices: cnotMat = P0 (x) 1 + P1 (x) X
# (BridgeDictionary.lean:66, control first) and target actions tensorOf 1 U (EqvK2Converse.lean:153,163).
P0 = [[Q(1), Q()], [Q(), Q()]]; P1 = [[Q(), Q()], [Q(), Q(1)]]
Xm = [[Q(), Q(1)], [Q(1), Q()]]
landed_cnot = [[kron(P0, eye(2))[i][j] + kron(P1, Xm)[i][j] for j in range(4)] for i in range(4)]
check("A1-PAIR-CNOT-ENCODING", meq(cnotK(2, 0, 1), landed_cnot))
check("A1-PAIR-TARGET-ENCODING", meq(local(2, 1, cycMat), kron(eye(2), cycMat)))

# X0: two-level Euler form of cycMat: cycMat = Rz(pi/2) Rx(pi/2), Rz(a)=diag(e^{-ia/2},e^{ia/2}).
Rx = transition_flow(2, 0, 1, INV_R2, INV_R2)              # flow(transition 0 1)(pi/4)
Rz = mul(self_flow(2, 0, E_M), self_flow(2, 1, E_P))
check("X0-CYC-EULER", meq(mul(Rz, Rx), cycMat))
check("X0-CYC-EULER-ORDER-MATTERS", not meq(mul(Rx, Rz), cycMat))
check("X0-CYC-UNITARY-DET1", meq(mul(dag(cycMat), cycMat), eye(2))
      and (cycMat[0][0] * cycMat[1][1] - cycMat[0][1] * cycMat[1][0]) == Q(1))

for k in (2, 3):
    n = 2 ** k
    # X1 (L3b): each cone generator lift is an exact finite product of DrivesElementaryAt generators.
    ok = True
    for i, j in itertools.permutations(range(k), 2):
        word = [perm_swap(n, a, flipbit(a, j, k)) for a in range(n)
                if bit(a, i, k) == 1 and bit(a, j, k) == 0]
        ok &= meq(prod(word, n), cnotK(k, i, j))
    check(f"X1-CNOT-FROM-SWAPS-k{k}", ok)
    ok = True
    for j in range(k):
        word = [self_flow(n, a, q(C35) + q(S35) * I) for a in range(n) if bit(a, j, k) == 1]
        ok &= meq(prod(word, n), local(k, j, phaseMat(C35, S35)))
    check(f"X1-ROT-FROM-SELF-FLOWS-k{k}", ok)
    ok = True
    for j in range(k):
        word = []
        for a in range(n):
            if bit(a, j, k) == 0:
                p, r = a, flipbit(a, j, k)
                word += [self_flow(n, p, E_M), self_flow(n, r, E_P),
                         transition_flow(n, p, r, INV_R2, INV_R2)]
        ok &= meq(prod(word, n), local(k, j, cycMat))
    check(f"X1-CYC-FROM-TWO-LEVEL-k{k}", ok)
    # countercontrol: dropping one block of the cyclic word must fail
    word = []
    for a in range(n):
        if bit(a, k - 1, k) == 0 and a != 0:
            p, r = a, flipbit(a, k - 1, k)
            word += [self_flow(n, p, E_M), self_flow(n, r, E_P),
                     transition_flow(n, p, r, INV_R2, INV_R2)]
    check(f"X1-CYC-MISSING-BLOCK-REJECTED-k{k}", not meq(prod(word, n), local(k, k - 1, cycMat)))

    # X3 (L3a obstruction): the triangular inventory (CNOT(i->j), i<j; rotations and cyc off token 0)
    # commutes with Z on token 0; the transitions and swaps across token 0 do not.
    Z0 = local(k, 0, [[Q(1), Q()], [Q(), Q(-1)]])
    gens = [cnotK(k, i, j) for i, j in itertools.combinations(range(k), 2)]
    gens += [local(k, j, phaseMat(C35, S35)) for j in range(1, k)]
    gens += [local(k, j, cycMat) for j in range(1, k)]
    check(f"X3-TRIANGULAR-COMMUTES-Z0-k{k}", all(commutes(g, Z0) for g in gens))
    across = [(a, flipbit(a, 0, k)) for a in range(n) if bit(a, 0, k) == 0]
    check(f"X3-TRANSITION-ACROSS-TOKEN0-NOT-k{k}",
          all(not commutes(transition_flow(n, a, b, C35, S35), Z0) for a, b in across))
    check(f"X3-SWAP-ACROSS-TOKEN0-NOT-k{k}",
          all(not commutes(perm_swap(n, a, b), Z0) for a, b in across))
    within = [(a, b) for a in range(n) for b in range(n) if a < b and bit(a, 0, k) == bit(b, 0, k)]
    check(f"X3-WITHIN-TOKEN0-SECTOR-COMMUTES-k{k}",
          all(commutes(transition_flow(n, a, b, C35, S35), Z0) for a, b in within)
          and all(commutes(phase_gate(n, a), Z0) for a in range(n)))
    # LabelInvariant breaks it: relabel tokens 0<->1 (a bijection of basis states).
    sw = zeros(n)
    for a in range(n):
        b0, b1 = bit(a, 0, k), bit(a, 1, k)
        b = a
        if b0 != b1: b = flipbit(flipbit(a, 0, k), 1, k)
        sw[b][a] = Q(1)
    relabelled = mul(mul(sw, local(k, 1, cycMat)), dag(sw))
    check(f"X3-RELABEL-GIVES-TOKEN0-CYC-k{k}", meq(relabelled, local(k, 0, cycMat))
          and not commutes(relabelled, Z0))
    check(f"X3-REVERSE-CNOT-NOT-k{k}", not commutes(cnotK(k, 1, 0), Z0))

    # X4: substratumClass (monomial) admits CNOT and rotation lifts, not cyc or a generic flow.
    check(f"X4-MONOMIAL-CNOT-ROT-k{k}",
          all(is_monomial(cnotK(k, i, j)) for i, j in itertools.permutations(range(k), 2))
          and all(is_monomial(local(k, j, phaseMat(C35, S35))) for j in range(k)))
    check(f"X4-NOT-MONOMIAL-CYC-k{k}", all(not is_monomial(local(k, j, cycMat)) for j in range(k)))
    check(f"X4-NOT-MONOMIAL-FLOW-k{k}", not is_monomial(transition_flow(n, 0, 1, C35, S35)))
    check(f"X4-NOT-DIAGONAL-CNOT-k{k}", not is_diagonal(cnotK(k, 0, 1)))

# X2 (L8): swap = phaseGate a * phaseGate b * flow(transition a b)(pi/2), all a != b.
for n in (2, 3, 4, 5):
    ok = all(meq(prod([phase_gate(n, a), phase_gate(n, b), transition_flow(n, a, b, 0, 1)], n),
                 perm_swap(n, a, b)) for a in range(n) for b in range(n) if a != b)
    check(f"X2-SWAP-REDUNDANT-n{n}", ok)
    bad = not meq(mul(phase_gate(n, 0), transition_flow(n, 0, 1, 0, 1)), perm_swap(n, 0, 1))
    check(f"X2-ONE-PHASE-REJECTED-n{n}", bad)

# X5 (L7): divisor descent by block alone: ancBlock (f,f) of each generator on S x Fin m
# supported in the slice {(s,f)} is the generator on S.
def ancblock(M, nS, m, f, e):
    return [[M[s * m + f][t * m + e] for t in range(nS)] for s in range(nS)]
for nS, m in ((3, 2), (3, 4), (2, 2), (5, 2)):
    n = nS * m; ok = True
    for f in range(m):
        for a in range(nS):
            ok &= meq(ancblock(phase_gate(n, a * m + f), nS, m, f, f), phase_gate(nS, a))
            for b in range(nS):
                if a == b: continue
                ok &= meq(ancblock(transition_flow(n, a * m + f, b * m + f, C35, S35), nS, m, f, f),
                          transition_flow(nS, a, b, C35, S35))
                ok &= meq(ancblock(perm_swap(n, a * m + f, b * m + f), nS, m, f, f),
                          perm_swap(nS, a, b))
    check(f"X5-BLOCK-DESCENT-S{nS}-m{m}", ok)
# The qubit-power-spectator class: every matrix at sizes 2^j, unit-disk diagonals elsewhere.
X = [[Q(), Q(1)], [Q(1), Q()]]
check("X5-ODD-SPECTATOR-BREAKS-DIAGONAL", not is_diagonal(kron(eye(3), X)))
d3 = [[Q(Fr(1, 2)), Q(), Q()], [Q(), Q(0, 0, 1), Q()], [Q(), Q(), Q(-1)]]
check("X5-POW2-SPECTATOR-KEEPS-DIAGONAL", is_diagonal(kron(eye(2), d3)) and is_diagonal(kron(eye(4), d3)))
check("X5-FIN3-FLOW-NOT-DIAGONAL", not is_diagonal(transition_flow(3, 0, 1, C35, S35)))
check("X5-NO-POW2-MULTIPLE-OF-3", all((2 ** j) % 3 != 0 for j in range(64)))

# X6: pair-level monomial-hull countermodel K_mono = cone(monomial-unitary conjugates of pure
# products).  Supports of monomial images of two-qubit pure products have size 1, 2 or 4
# (rectangles S0 x S1, permuted); v = phaseGate(1,1)|++> is such an image; (1 (x) cycMat) v has
# support 3, so its projector is no positive multiple of a generator (rank-one summand argument,
# written), hence lies outside K_mono although it is PSD.
def support(vec): return [i for i, x in enumerate(vec) if not x.iszero()]
rect_sizes = {len(S0) * len(S1) for S0 in ([0], [1], [0, 1]) for S1 in ([0], [1], [0, 1])}
check("X6-PRODUCT-SUPPORT-SIZES", rect_sizes == {1, 2, 4})
v = [Q(1), Q(1), Q(1), I]                                    # phaseGate (1,1) applied to |++>
check("X6-SEED-IS-MONOMIAL-IMAGE", meq(phase_gate(4, 3), [[Q(1) if (i == j and i < 3) else (I if i == j == 3 else Q()) for j in range(4)] for i in range(4)]))
Ucyc = kron(eye(2), cycMat)
w = [sum((Ucyc[i][j] * v[j] for j in range(4)), Q()) for i in range(4)]
check("X6-CYC-IMAGE-SUPPORT-3", len(support(w)) == 3 and w == w and
      all(w[i] == x for i, x in enumerate([Q(0, 0, -1), Q(1), Q(1, 0, -1), Q()])))
check("X6-CYC-IMAGE-NOT-IN-HULL", len(support(w)) not in rect_sizes)
check("X6-MONOMIAL-PRESERVES-SUPPORT-SIZE",
      all(len(support([sum((mul(perm_swap(4, a, b), phase_gate(4, c))[i][j] * v[j] for j in range(4)), Q())
                       for i in range(4)])) == 4 for a in range(4) for b in range(4) for c in range(4)))

# X7 (L3b two-level form of su_euler, EqvK2Generation.lean:323, U = dUnit a * rotRe c s * dUnit b):
# two-level rotRe(c,s) on (p,q) = phaseGate q * flow(transition p q)(theta) * phaseGate q ^ 3, and
# two-level dUnit a = self-flow at p (phase a) times self-flow at q (phase conj a).
ok = True
for n in (2, 3, 4):
    for p, r in itertools.permutations(range(n), 2):
        S = phase_gate(n, r)
        lhs = prod([S, transition_flow(n, p, r, C35, S35), S, S, S], n)
        rot = eye(n); rot[p][p] = Q(C35); rot[r][r] = Q(C35); rot[p][r] = Q(-S35); rot[r][p] = Q(S35)
        ok &= meq(lhs, rot)
        a = q(C35) + q(S35) * I
        du = eye(n); du[p][p] = a; du[r][r] = a.conj()
        ok &= meq(mul(self_flow(n, p, a), self_flow(n, r, a.conj())), du)
check("X7-TWO-LEVEL-EULER-FACTORS", ok)
check("X7-SIGN-COUNTERCONTROL", not meq(prod([phase_gate(3, 1), transition_flow(3, 0, 1, C35, S35)], 3),
                                        prod([phase_gate(3, 1), transition_flow(3, 0, 1, C35, S35), phase_gate(3, 1), phase_gate(3, 1), phase_gate(3, 1)], 3)))

print(f"checks: {len(checks) + len(failures)}, failures: {len(failures)}")
sys.exit(1 if failures else 0)
