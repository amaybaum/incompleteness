"""fixed_basis_ancilla_probe.py -- act 45's exact-computation layer.

Exact Gaussian-rational and rational arithmetic throughout; no floating point. Exits 1 on any mismatch with the
values frozen in act 45's preregistration, and ends with one summary line.

 1. Trivial ancilla, replayed at points (the kernel's objects; this does not stand in for the kernel). Six flat
    16 x 16 realizations of the visible slice J/16 at the product configuration: SIG, a two-sided gauge D1 SIG D2, a
    relabelling of SIG, a Dita point of act 39's family, act 42's support-40 line SIG o v^E40, and i SIG. For the
    fixed-basis datum with evolution U = H/4, uniform initial law and identity readout: equal Born weights, equal
    rooted families for t <= 3, and equal rooted families after three pairs of monomial interventions.
 2. Countercontrols of item 1. An off-slice unitary gives a different rooted family; a row-non-monomial
    intervention K = F4(i) (x) I4 separates some pair of the six.
 3. The ancilla boundary. Visible V = 4 values, ancilla {a0, a1}, slice G = J/4. Dilations with fixed (., a0)
    columns and completions W applied to the orthonormal complement; the CARRIED datum (basis V x A, evolution U,
    initial law uniform on V at a0, readout the visible coordinate). Every dilation unitary and admissible for G;
    the one-step rooted family equal to G on every dilation; at two steps D1 and D2 (angles varying, completions
    1 and F^T/2) differ, while sharing every (., a0) column; D3 and D4 (angle constant) agree.
 4. The tensor-factor ancilla. For U = (F/2) (x) W with W a rational 2 x 2 rotation, the carried datum's rooted
    family equals G^t for t <= 3, and so does the trivial-ancilla embedding.
"""
import itertools, random, sys
from fractions import Fraction as Fr

FAILS = []; COUNT = [0]
def check(name, cond):
    COUNT[0] += 1
    print(('PASS ' if cond else 'FAIL ') + name, flush=True)
    if not cond: FAILS.append(name)

class G:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def __add__(s, o): return G(s.a + o.a, s.b + o.b)
    def __neg__(s): return G(-s.a, -s.b)
    def conj(s): return G(s.a, -s.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def n2(s): return s.a * s.a + s.b * s.b
ZERO, ONE, I_ = G(0), G(1), G(0, 1)
N = range(16)
def F4(t): return [[ONE, ONE, ONE, ONE], [ONE, t, G(-1), -t], [ONE, G(-1), ONE, G(-1)], [ONE, -t, G(-1), t]]
z, w = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13))
FZ, FW = F4(z), F4(w)
SIG = [[FZ[i // 4][j // 4] * FW[i % 4][j % 4] for j in N] for i in N]
def gpow(u, k):
    out = ONE
    for _ in range(abs(k)): out = out * (u if k > 0 else u.conj())
    return out
def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in N] for i in N]
EB = piece(lambda a, b, c, d: int(a == 2 and d == 1))
EC = piece(lambda a, b, c, d: int((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))))
E40 = piece(lambda a, b, c, d: -int(b == 0 and c == 0) + int(a == 2 and b % 2 == 1 and d % 2 == 0) - int(a % 2 == 0 and c % 2 == 1 and d == 0))
v1, v2, v3 = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17))
rng = random.Random(45)
units = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), I_, G(-1), ONE]
d1 = [rng.choice(units) for _ in N]; d2 = [rng.choice(units) for _ in N]
pr = list(N); rng.shuffle(pr); pc = list(N); rng.shuffle(pc)
REAL = {
    'SIG': SIG,
    'D1 SIG D2': [[d1[i] * SIG[i][j] * d2[j] for j in N] for i in N],
    'relabelled SIG': [[SIG[pr[i]][pc[j]] for j in N] for i in N],
    'H3(1, v2, v3)': [[SIG[i][j] * gpow(v2, EB[i][j]) * gpow(v3, EC[i][j]) for j in N] for i in N],
    'SIG o v^E40': [[SIG[i][j] * gpow(v1, E40[i][j]) for j in N] for i in N],
    'i SIG': [[I_ * x for x in r] for r in SIG],
}
def mm(A, B): return [[sum((A[i][k] * B[k][j] for k in N), ZERO) for j in N] for i in N]
def flat_unitary(H):
    if any(x.n2() != 1 for r in H for x in r): return False
    return all(sum((H[i][j] * H[k][j].conj() for j in N), ZERO) == (G(16) if i == k else ZERO) for i in N for k in N)
def born(H, scale=16): return [[H[b2][b].n2() / scale for b2 in N] for b in N]       # born(b, b2) = |U b2 b|^2
def rooted(H, T=3, scale=16):
    M = born(H, scale); P = [[Fr(int(i == j)) for j in N] for i in N]; out = []
    for _ in range(T + 1):
        out.append(tuple(tuple(r) for r in P)); P = [[sum(P[i][k] * M[k][j] for k in N) for j in N] for i in N]
    return tuple(out)
def perm_diag():
    p = list(N); rng.shuffle(p); d = [rng.choice(units) for _ in N]
    return [[d[i] if p[i] == j else ZERO for j in N] for i in N]
def scaled_partial_perm():
    p = list(N); rng.shuffle(p); keep = set(rng.sample(list(N), 11)); c = rng.choice(units)
    return [[c if (p[i] == j and i in keep) else ZERO for j in N] for i in N]

# 1. trivial ancilla, replayed at points
names = list(REAL)
check('1a six realizations flat unitary', all(flat_unitary(H) for H in REAL.values()))
check('1b Born weights equal on all 15 pairs', len({tuple(tuple(r) for r in born(H)) for H in REAL.values()}) == 1)
RT = {nm: rooted(H) for nm, H in REAL.items()}
check('1c rooted families t <= 3 equal on all 15 pairs', len(set(RT.values())) == 1)
check('1d one-step rooted family equals the slice J/16', RT['SIG'][1] == tuple(tuple(Fr(1, 16) for _ in N) for _ in N))
MN = [(perm_diag(), perm_diag()), (scaled_partial_perm(), scaled_partial_perm()), (perm_diag(), scaled_partial_perm())]
def monomial(M): return all(sum(1 for x in r if x != ZERO) <= 1 for r in M) and all(sum(1 for r in M if r[j] != ZERO) <= 1 for j in N)
check('1e the three intervention pairs are monomial', all(monomial(a) and monomial(b) for a, b in MN))
check('1f rooted families after each monomial pair equal on all 15 pairs',
      len({tuple(rooted(mm(mm(a, H), b)) for a, b in MN) for H in REAL.values()}) == 1)
# 2. countercontrols
F41 = F4(ONE)
X = [[F41[i // 4][j // 4] * G(2) if i % 4 == j % 4 else ZERO for j in N] for i in N]
check('2a off-slice unitary: flat check fails, rooted family differs',
      (not flat_unitary(X)) and rooted(X) != RT['SIG'])
F4i = F4(I_)
K = [[F4i[i // 4][j // 4] if i % 4 == j % 4 else ZERO for j in N] for i in N]
KH = {nm: tuple(tuple(x.n2() for x in r) for r in mm(K, H)) for nm, H in REAL.items()}
sep = sum(1 for a, b in itertools.combinations(names, 2) if KH[a] != KH[b])
check('2b row-non-monomial K separates some pair (%d of 15)' % sep, (not monomial(K)) and sep > 0)

# 3. the ancilla boundary
V, A = range(4), range(2)
F = [[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]]
idx = [(i, a) for i in V for a in A]
def dil(cs, W):
    U = {(r, c): Fr(0) for r in idx for c in idx}
    for j in V:
        for i in V:
            ci, si = cs[i]
            U[((i, 0), (j, 0))] += Fr(F[i][j], 2) * ci; U[((i, 1), (j, 0))] += Fr(F[i][j], 2) * si
    for j in V:
        for k in V:
            for m in V:
                cm, sm = cs[m]
                U[((m, 0), (j, 1))] += W[k][j] * Fr(F[m][k], 2) * (-sm); U[((m, 1), (j, 1))] += W[k][j] * Fr(F[m][k], 2) * cm
    return U
I4 = [[Fr(int(i == j)) for j in V] for i in V]
FT2 = [[Fr(F[j][i], 2) for j in V] for i in V]
vary = [(Fr(3, 5), Fr(4, 5)), (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(5, 13), Fr(12, 13))]
const = [(Fr(3, 5), Fr(4, 5))] * 4
DIL = {'D0': dil([(Fr(1), Fr(0))] * 4, I4), 'D1': dil(vary, I4), 'D2': dil(vary, FT2), 'D3': dil(const, I4), 'D4': dil(const, FT2)}
GV = [[Fr(1, 4)] * 4 for _ in V]
def unitary(U): return all(sum(U[(r, c)] * U[(r, c2)] for r in idx) == Fr(int(c == c2)) for c in idx for c2 in idx)
def admissible(U): return all(sum(U[((i, a), (j, 0))] ** 2 for a in A) == GV[i][j] for i in V for j in V)
def carried(U, T=3):
    rows = []
    for a in V:
        p = {b: Fr(int(b == (a, 0))) for b in idx}; row = []
        for _ in range(T + 1):
            row.append(tuple(sum(p[(j, x)] for x in A) for j in V))
            p = {b2: sum(p[b] * U[(b2, b)] ** 2 for b in idx) for b2 in idx}
        rows.append(row)
    return [tuple(rows[a][t] for a in V) for t in range(T + 1)]
def gpow_v(T=3):
    P = I4; out = []
    for _ in range(T + 1):
        out.append(tuple(tuple(r) for r in P)); P = [[sum(P[i][k] * GV[k][j] for k in V) for j in V] for i in V]
    return out
C = {nm: carried(U) for nm, U in DIL.items()}
check('3a five dilations unitary and admissible for G = J/4', all(unitary(U) and admissible(U) for U in DIL.values()))
check('3b carried one-step rooted family equals G on all five', all(C[nm][1] == tuple(tuple(r) for r in GV) for nm in DIL))
check('3c D1 and D2 share every (., a0) column and differ in a completion column',
      all(DIL['D1'][(r, (j, 0))] == DIL['D2'][(r, (j, 0))] for r in idx for j in V)
      and any(DIL['D1'][(r, (j, 1))] != DIL['D2'][(r, (j, 1))] for r in idx for j in V))
D2ROW = (Fr(17187, 67600), Fr(6371, 67600), Fr(23271, 67600), Fr(20771, 67600))
check('3d carried two-step rooted family: D1 row 0 uniform, D2 row 0 = (17187, 6371, 23271, 20771)/67600',
      C['D1'][2][0] == (Fr(1, 4),) * 4 and C['D2'][2][0] == D2ROW)
check('3e carried two-step rooted family equal for D3 and D4', C['D3'][2] == C['D4'][2])

# 4. the tensor-factor ancilla
W2 = [[Fr(3, 5), Fr(-4, 5)], [Fr(4, 5), Fr(3, 5)]]
UP = {((i, a), (j, b)): Fr(F[i][j], 2) * W2[a][b] for i in V for a in A for j in V for b in A}
check('4a tensor-factor dilation unitary and admissible for G', unitary(UP) and all(
    sum(UP[((i, a), (j, 0))] ** 2 for a in A) == GV[i][j] for i in V for j in V))
check('4b tensor-factor carried rooted family equals G^t for t <= 3', carried(UP) == gpow_v())
check('4c trivial-ancilla embedding (D0) carried rooted family equals G^t for t <= 3', C['D0'] == gpow_v())

n = COUNT[0]
if FAILS:
    print('fixed_basis_ancilla_probe: FAILED (%d of %d checks): %s' % (len(FAILS), n, '; '.join(FAILS)))
    sys.exit(1)
print('fixed_basis_ancilla_probe: OK -- %d checks: six flat realizations of one slice give equal rooted families '
      'before and after monomial interventions; carried ancilla separates at two steps; tensor-factor ancilla does not' % n)
