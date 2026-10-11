"""E20 probe -- E16's residual: odd chart dimension at least five with K_inf-Geom.  Exact checks on the sector family
and on the strictly convex bodies Omega*^5, eball 5 (negative control) and eball 3 (positive control): the count, the
two kernel forms of K_inf-Geom, the linear gate clauses (frame, relT, relC) solved exactly, and the positivity relaxation
(posFwd) as a cutting-plane LP with an exactly verified Farkas certificate when infeasible.
(exact: Fractions / Gaussian rationals for every recorded fact; floating point only inside the LP search, whose
infeasibility verdicts count only when exactified)

S0 (written 2026-10-11T08:27Z by `date -u`, before run 1; predictions in NOTES-E20.md S0).
Pre-run review (2026-10-11T10:17Z, after the session's interruption, before run 1 and before the first commit of this
file; draft sha256 5743149f...): SF3's non-product test corrected to the rank of the 4 x 4 table block (the first draft
took the rank of the block's density matrix, which is 1 for the pure entangled image, so SF3 would have failed on a
harness error); a vacuous clause (`... or True`) removed from C1.  The decision rule is unchanged.

SETTING (kernel vocabulary at L).  A token body Omega in R^D (chart dimension D); HVec D = R^{D+1} with hom x = (1, x);
W D = tables w[mu][nu] (control, target); prodState x y = hom x (x) hom y; a NOT N (linear involution preserving Omega,
N z = -z, |z| = 1); H = homMap N = 1 (+) N; actT N = 1 (x) H, actC N = H (x) 1; NativeGate clauses: frame
G(prodState(corner a, corner b)) = prodState(corner a, corner (a+b)) (corner z 0 = z, corner z 1 = -z), relT
actT N G actT N = G, relC actC N G actC N = actT N G, posFwd G(prodState x y) in maxCone (nonnegative on every product
of effects), posInv the same for G^-1; K_inf-Geom: SingletonFaces (every proper effect certain on at most one state) or
RelStrictConvex (points strictly between two distinct states are states and not boundary states).

BODIES AND CHECKS.
  SF1  the sector family Omega(k; d_1..d_k) with the sector NOTs (m_i minus signs): the count H has (D+1)/2 eigenvalues
       +1 iff 1 + (k-1) + sum (d_i - m_i) = (k + sum d_i)/2; verdict for (2;3,3), (3;3,3,3), (4;3,3,3,3), (2;3,1),
       (2;3,5), (2;5,5), (2;1,1), with the natural m_i (3-ball: 2; bit: 1; 5-ball: 3).
  SF2  K_inf-Geom fails for every sector body with k >= 2, exact witnesses in the chart (t_1..t_{k-1}, r~_0..r~_{k-1}):
       two distinct pure sector-0 states x != y, their midpoint m in Omega, and y' a pure sector-1 state with
       t_1(m + eps (m - y')) = -eps t_1(y') < 0 for every eps > 0 (IsBoundaryState m; RelStrictConvex fails); the effect t_0
       (an effect: 0 <= t_0 <= 1 on Omega; proper: t_0(y') = 0) is certain on x and on y (SingletonFaces fails).
  SF3  the sector gate for (3; 3, 3, 3) (D = 11): G = (Phi (x) Phi)(cnot (x) id)(Phi (x) Phi)^-1 with the kernel's cnot
       (parsed) on the qubit factor, N = Phi (nflip (+) id) Phi^-1, z = (sector 0, +z): frame, relT, relC on all 144 basis
       tables, G^2 = 1; posFwd on 25 exact product pairs through blockwise PSD (each sector-pair block of the tensor-side
       image is PSD); Entangling: the image of (sector 0, +x) (x) (sector 0, +z) has a rank-4 block.
  C0   control of the linear-clause machinery: for eball 3 with N = nflip, z = z3, the parsed cnot lies exactly in the
       solution set F of frame + relT + relC (every entry outside the free pattern is 0; the frame holds).
  C1   the count for eball 3, eball 5, Omega*^5 with their natural (z, N).
  C2   Omega*^5 = {|X|^3 <= (1+S)(1-S)^2}: relative strict convexity on instances -- the midpoint of two distinct exact
       boundary points is strictly inside (F < 0); z = e_2 is a boundary state (S = 0, |X| = 1).
  C3   the linear clauses for eball 3, eball 5, Omega*^5: the free pattern h_nu = h_nu', h_mu = h_mu' h_nu'
       ((D+1)^4/4 entries), the frame system solved exactly (consistent; rank; nullity = dim F).
  C4   the positivity relaxation, each body: pools of exact states and effects (balls: Pythagorean unit vectors, the
       tight effects (1 + v.x)/2; Omega*^5: exact boundary rings S in {0, 7/9, -7/9} and the poles, supporting effects at
       boundary points with a rational upper bound of the support value, loose directional effects, (1 +- S)/2); the
       cutting-plane LP (HiGHS) over F; outcome FEASIBLE(pool) (a float candidate; recorded, not a proof),
       INFEASIBLE-CERTIFIED (an exact Farkas certificate over the support of the dual solution, verified in Fractions:
       y >= 0, sum y_i a_i = 0, sum y_i b_i > 0), or INFEASIBLE-UNCERTIFIED (float only; undecided).  Rule: eball 3 must
       be FEASIBLE(pool) (cnot); the verdicts of eball 5 and Omega*^5 are recorded.
COUNTERCONTROLS (each must fail as stated).
  XO1  "eball 3 is INFEASIBLE" -- must fail.
  XO2  "the sector body (2;3,3) is relatively strictly convex at the probed midpoint" -- must fail.
  XO3  "the frame equations are inconsistent for eball 3" -- must fail.
DECISION RULE (fixed before run 1).  VERDICT E20-ODD-BODIES-EXACT iff SF1-SF3, C0-C4 print PASS (C4 passes when every
body's LP terminates with one of the three outcomes and eball 3 is FEASIBLE(pool); the other outcomes are recorded, not
required), no FAIL is printed, XO1-XO3 each print "COUNTER ... fails as stated", and the last line before the verdict is
"checks: 8, failures: 0".  Otherwise "VERDICT NOT RENDERED".  The node's outcome (A, B', C of NOTES-E20 S0) is read from the
recorded table by the rule fixed there; the verdict does not assert it.
"""
import itertools
import random
import re
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog

KERNEL_CD = '../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'
RESULTS = []
random.seed(20261011)


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


# ------------------------------------------------------------------ the kernel's cnot, parsed
def parse_table(src, name):
    m = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src)
    entries = re.findall(r'(\d), (\d) => (\d)', m.group(1))
    T = {(int(a), int(b)): int(c) for a, b, c in entries}
    assert len(T) == 16
    return T


def parse_sgn(src):
    m = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', src)
    neg = {(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))}
    return {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}


src_cd = open(KERNEL_CD, encoding='utf-8').read()
PC, PT, SGN = parse_table(src_cd, 'pc'), parse_table(src_cd, 'pt'), parse_sgn(src_cd)
m_nf = re.search(r'def nflip : \(Fin 3 → ℝ\) →ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun x := fun i => \(!\[(-?1), (-?1), (-?1)\] : Fin 3 → ℝ\) i \* x i', src_cd)
NFLIP = [int(m_nf.group(k)) for k in (1, 2, 3)]
print('parsed: pc, pt, sgn; nflip = diag%s' % (tuple(NFLIP),), flush=True)


def cnot_matrix16():
    """the kernel's cnotFun as a 16 x 16 signed permutation on the table coordinates (mu, nu) -> 4 mu + nu"""
    M = [[Fr(0)] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            M[4 * m + n][4 * PC[(m, n)] + PT[(m, n)]] = Fr(SGN[(m, n)])
    return M


# ------------------------------------------------------------------ exact linear algebra
def rref_solve(rows, rhs, nvar):
    """exact Gaussian elimination: rows (list of dict col->Fr) with rhs; returns (consistent, particular, nullspace basis, rank)"""
    A = [dict(r) for r in rows]
    b = list(rhs)
    pivots = []
    r = 0
    m = len(A)
    for c in range(nvar):
        piv = None
        for i in range(r, m):
            if A[i].get(c, Fr(0)) != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        b[r], b[piv] = b[piv], b[r]
        inv = 1 / A[r][c]
        A[r] = {k: v * inv for k, v in A[r].items()}
        b[r] = b[r] * inv
        for i in range(m):
            if i != r and A[i].get(c, Fr(0)) != 0:
                f = A[i][c]
                for k, v in A[r].items():
                    nv = A[i].get(k, Fr(0)) - f * v
                    if nv == 0:
                        A[i].pop(k, None)
                    else:
                        A[i][k] = nv
                b[i] = b[i] - f * b[r]
        pivots.append(c)
        r += 1
        if r == m:
            break
    for i in range(r, m):
        if b[i] != 0 and not A[i]:
            return False, None, None, r
        if b[i] != 0 and all(v == 0 for v in A[i].values()):
            return False, None, None, r
    pivset = set(pivots)
    free = [c for c in range(nvar) if c not in pivset]
    part = [Fr(0)] * nvar
    for i, c in enumerate(pivots):
        part[c] = b[i]
    basis = []
    for fcol in free:
        v = [Fr(0)] * nvar
        v[fcol] = Fr(1)
        for i, c in enumerate(pivots):
            coef = A[i].get(fcol, Fr(0))
            if coef != 0:
                v[c] = -coef
        basis.append(v)
    return True, part, basis, r


def nullspace_cols(cols, n):
    """exact kernel of the map y -> sum_i y_i cols[i] (each col a length-n list of Fr): basis of {y}"""
    m = len(cols)
    rows = [{} for _ in range(n)]
    for i, col in enumerate(cols):
        for j in range(n):
            if col[j] != 0:
                rows[j][i] = col[j]
    ok, part, basis, rank = rref_solve(rows, [Fr(0)] * n, m)
    return basis


# ------------------------------------------------------------------ SF1: the count for the sector family
def sector_count(k, dims, ms):
    D = (k - 1) + sum(dims)
    plus = 1 + (k - 1) + sum(d - m for d, m in zip(dims, ms))
    return D, plus, (D % 2 == 1) and (2 * plus == D + 1)


NATURAL_M = {3: 2, 1: 1, 5: 3}
members = [(2, (3, 3)), (3, (3, 3, 3)), (4, (3, 3, 3, 3)), (2, (3, 1)), (2, (3, 5)), (2, (5, 5)), (2, (1, 1))]
sf1_rows = []
for k, dims in members:
    ms = tuple(NATURAL_M[d] for d in dims)
    D, plus, ok = sector_count(k, dims, ms)
    sf1_rows.append(((k, dims), D, plus, ok))
sf1_expect = [True] * 7
check('SF1', [r[3] for r in sf1_rows] == sf1_expect,
      'the count for the sector family: ' + '; '.join('%s: D = %d, +1 count %d, meets: %s' % (str(r[0]), r[1], r[2], r[3]) for r in sf1_rows))


# ------------------------------------------------------------------ the sector body: chart, membership, Geom witnesses
class Sector:
    def __init__(self, k, dims):
        self.k, self.dims = k, list(dims)
        self.D = (k - 1) + sum(dims)
        self.off = []
        pos = k - 1
        for d in dims:
            self.off.append(pos)
            pos += d

    def state(self, i, r):
        """the pure/mixed state of sector i with Bloch vector r (|r| <= 1), as a chart vector"""
        x = [Fr(0)] * self.D
        if i >= 1:
            x[i - 1] = Fr(1)
        for j, v in enumerate(r):
            x[self.off[i] + j] = Fr(v)
        return x

    def weights(self, x):
        t = [Fr(0)] * self.k
        for i in range(1, self.k):
            t[i] = x[i - 1]
        t[0] = 1 - sum(t[1:])
        return t

    def member(self, x):
        t = self.weights(x)
        if any(ti < 0 for ti in t):
            return False
        for i, d in enumerate(self.dims):
            r = x[self.off[i]:self.off[i] + d]
            if sum(v * v for v in r) > t[i] * t[i]:
                return False
        return True


def sf2_witness(k, dims):
    S = Sector(k, dims)
    d0 = dims[0]
    e1 = [Fr(0)] * d0
    e1[0] = Fr(1)
    e1n = [Fr(-1)] + [Fr(0)] * (d0 - 1)
    x, y = S.state(0, e1), S.state(0, e1n)
    m = [(a + b) / 2 for a, b in zip(x, y)]
    d1 = dims[1]
    yp = S.state(1, [Fr(1)] + [Fr(0)] * (d1 - 1))
    tm, typ = S.weights(m), S.weights(yp)
    # t_1(m + eps (m - y')) = t_1(m) + eps (t_1(m) - t_1(y')) = 0 - eps * 1
    boundary = (x != y and S.member(x) and S.member(y) and S.member(m) and tm[1] == 0 and (tm[1] - typ[1]) < 0)
    # SingletonFaces: the effect t_0 is certain on x and y, proper at y', an effect on sampled states
    t0 = lambda v: S.weights(v)[0]
    samples = [x, y, yp, m, S.state(0, [Fr(0)] * d0), S.state(1, [Fr(0)] * d1)]
    effect_ok = all(0 <= t0(v) <= 1 for v in samples)
    sf = (t0(x) == 1 and t0(y) == 1 and t0(yp) == 0 and effect_ok)
    return boundary and sf, boundary, sf


sf2 = all(sf2_witness(k, dims)[0] for k, dims in members if k >= 2)
check('SF2', sf2, 'for every member with k >= 2: the midpoint of two distinct pure sector-0 states is a boundary state '
      '(RelStrictConvex fails) and the effect t_0 is proper and certain on both (SingletonFaces fails)')

# ------------------------------------------------------------------ SF3: the (3; 3, 3, 3) gate
Z0, O1, II = (Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))


def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def csub(x, y): return (x[0] - y[0], x[1] - y[1])
def cmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def cconj(x): return (x[0], -x[1])
def cadd_all(it):
    s = Z0
    for v in it:
        s = cadd(s, v)
    return s
def mmul(A, B): return [[cadd_all(cmul(A[i][t], B[t][j]) for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A, B): return [[cadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mscale(r, A): return [[(r * x[0], r * x[1]) for x in row] for row in A]
def adj(A): return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def kron2(A, B): return [[cmul(A[i // 2][j // 2], B[i % 2][j % 2]) for j in range(4)] for i in range(4)]


S0m = [[O1, Z0], [Z0, O1]]
SX = [[Z0, O1], [O1, Z0]]
SY = [[Z0, (Fr(0), Fr(-1))], [II, Z0]]
SZ = [[O1, Z0], [Z0, (Fr(-1), Fr(0))]]
SIG = [S0m, SX, SY, SZ]
TT = [[kron2(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def dict_of(w):
    H = [[Z0] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            if w[m][n] != 0:
                H = madd(H, mscale(Fr(w[m][n]) / 4, TT[m][n]))
    return H


def det_c(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    s = Z0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        term = cmul(M[0][j], det_c(minor))
        s = cadd(s, term) if j % 2 == 0 else csub(s, term)
    return s


def is_psd_herm(H):
    if H != adj(H):
        return False
    for r in range(1, len(H) + 1):
        for idx in itertools.combinations(range(len(H)), r):
            d = det_c([[H[i][j] for j in idx] for i in idx])
            if d[1] != 0 or d[0] < 0:
                return False
    return True


def rank_c(M):
    # exact rank of a Gaussian-rational matrix by elimination on real/imag pairs: use complex Fractions as tuples
    A = [[x for x in row] for row in M]
    n, m = len(A), len(A[0])
    rank = 0
    row = 0
    for c in range(m):
        piv = next((i for i in range(row, n) if A[i][c] != Z0), None)
        if piv is None:
            continue
        A[row], A[piv] = A[piv], A[row]
        pv = A[row][c]
        inv = (pv[0] / (pv[0] ** 2 + pv[1] ** 2), -pv[1] / (pv[0] ** 2 + pv[1] ** 2))
        A[row] = [cmul(inv, x) for x in A[row]]
        for i in range(n):
            if i != row and A[i][c] != Z0:
                f = A[i][c]
                A[i] = [csub(A[i][j], cmul(f, A[row][j])) for j in range(m)]
        rank += 1
        row += 1
        if row == n:
            break
    return rank


def sector_gate_data(k):
    """the (k; 3,...,3) body: Phi (tensor coordinates (mu, i) -> homogenized chart), the gate, N, z"""
    n = 4 * k
    # tensor index (mu, i) -> mu * k + i ; chart hom index: 0 = T, 1..k-1 = t_i, k + 3 i + (mu - 1) = r~_i[mu-1]
    Phi = [[Fr(0)] * n for _ in range(n)]
    for i in range(k):
        Phi[0][0 * k + i] = Fr(1)            # T = sum_i c[0, i]
        if i >= 1:
            Phi[i][0 * k + i] = Fr(1)        # t_i = c[0, i]
        for mu in (1, 2, 3):
            Phi[k + 3 * i + (mu - 1)][mu * k + i] = Fr(1)
    # inverse: c[0,0] = T - sum_{i>=1} t_i; c[0,i] = t_i; c[mu,i] = r~_i[mu-1]
    Phinv = [[Fr(0)] * n for _ in range(n)]
    Phinv[0][0] = Fr(1)
    for i in range(1, k):
        Phinv[0][i] = Fr(-1)
        Phinv[i][i] = Fr(1)
    for i in range(k):
        for mu in (1, 2, 3):
            Phinv[mu * k + i][k + 3 * i + (mu - 1)] = Fr(1)
    # H on the tensor side: nflip_hom (x) id_k with nflip_hom = diag(1, 1, -1, -1) (the kernel's nflip homogenized)
    nh = [Fr(1), Fr(NFLIP[0]), Fr(NFLIP[1]), Fr(NFLIP[2])]
    Ht = [[Fr(0)] * n for _ in range(n)]
    for mu in range(4):
        for i in range(k):
            Ht[mu * k + i][mu * k + i] = nh[mu]
    return Phi, Phinv, Ht


def matmulF(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[Fr(0)] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for t in range(m):
            a = Ai[t]
            if a != 0:
                Bt = B[t]
                row = out[i]
                for j in range(p):
                    if Bt[j] != 0:
                        row[j] += a * Bt[j]
    return out


def kronF(A, B):
    n, m = len(A), len(B)
    out = [[Fr(0)] * (n * m) for _ in range(n * m)]
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                for p in range(m):
                    for q in range(m):
                        if B[p][q] != 0:
                            out[i * m + p][j * m + q] = A[i][j] * B[p][q]
    return out


def sf3_check(k):
    Phi, Phinv, Ht = sector_gate_data(k)
    n = 4 * k
    N2 = n * n
    # cnot (x) id on the tensor side: table index ((mu, i), (mu', i')) -> (mu k + i) n + (mu' k + i')
    C16 = cnot_matrix16()
    Gt = [[Fr(0)] * N2 for _ in range(N2)]
    for mu in range(4):
        for nu in range(4):
            r = 4 * mu + nu
            for c in range(16):
                if C16[r][c] != 0:
                    mu2, nu2 = divmod(c, 4)
                    for i in range(k):
                        for ip in range(k):
                            Gt[(mu * k + i) * n + (nu * k + ip)][(mu2 * k + i) * n + (nu2 * k + ip)] = C16[r][c]
    PP = kronF(Phi, Phi)
    PPi = kronF(Phinv, Phinv)
    G = matmulF(matmulF(PP, Gt), PPi)
    H = matmulF(matmulF(Phi, Ht), Phinv)
    I_n = [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    actT = kronF(I_n, H)
    actC = kronF(H, I_n)
    relT = matmulF(matmulF(actT, G), actT) == G
    relC = matmulF(matmulF(actC, G), actC) == matmulF(actT, G)
    invol = matmulF(G, G) == kronF(I_n, I_n)
    # homMap form: H fixes the unit coordinate and has no mixing with it
    homok = H[0][0] == 1 and all(H[0][j] == 0 for j in range(1, n)) and all(H[j][0] == 0 for j in range(1, n))
    # z: sector 0, Bloch (0,0,1): chart coordinates
    S = Sector(k, [3] * k)
    z = S.state(0, [Fr(0), Fr(0), Fr(1)])
    unit = sum(v * v for v in z) == 1
    Nz = [sum(H[i + 1][j + 1] * z[j] for j in range(n - 1)) for i in range(n - 1)]
    flips = Nz == [-v for v in z]

    def hom(x): return [Fr(1)] + list(x)

    def prod(x, y):
        hx, hy = hom(x), hom(y)
        return [hx[a] * hy[b] for a in range(n) for b in range(n)]

    def apply(M, v): return [sum(M[i][j] * v[j] for j in range(len(v)) if M[i][j] != 0) for i in range(len(M))]
    corner = {0: z, 1: [-v for v in z]}
    frame = all(apply(G, prod(corner[a], corner[b])) == prod(corner[a], corner[(a + b) % 2]) for a in (0, 1) for b in (0, 1))
    # posFwd on instances: pull back G(prodState x y) to the tensor side; each sector-pair block is a qubit table; PSD via dict
    bloch = [[Fr(0), Fr(0), Fr(1)], [Fr(0), Fr(0), Fr(-1)], [Fr(3, 5), Fr(0), Fr(4, 5)], [Fr(0), Fr(3, 5), Fr(-4, 5)], [Fr(1, 3), Fr(2, 3), Fr(2, 3)]]
    states = []
    for i in range(k):
        for r in bloch[:3]:
            states.append(S.state(i, r))
    # mixed-sector states: t_0 = 1/2, t_1 = 1/2 with Bloch parts scaled
    mixed = [Fr(0)] * S.D
    mixed[0] = Fr(1, 2)
    mixed[S.off[0] + 2] = Fr(1, 2)
    mixed[S.off[1] + 0] = Fr(1, 2)
    states.append(mixed)
    pos_ok = True
    rank4 = False
    pairs = [(a, b) for a in states for b in states][:25]
    pairs.append((S.state(0, [Fr(1), Fr(0), Fr(0)]), S.state(0, [Fr(0), Fr(0), Fr(1)])))
    for idx, (x, y) in enumerate(pairs):
        img = apply(G, prod(x, y))
        tens = apply(PPi, img)
        for i in range(k):
            for ip in range(k):
                w = [[tens[(mu * k + i) * n + (nu * k + ip)] for nu in range(4)] for mu in range(4)]
                Hd = dict_of(w)
                if not is_psd_herm(Hd):
                    pos_ok = False
                # not a product: the (0,0) block, as a 4 x 4 table w[mu][nu], has rank 4 (a product table has
                # rank 1); the block's density matrix Hd is pure (rank 1) -- the rank test is on the table
                if idx == len(pairs) - 1 and i == 0 and ip == 0 and rank_c([[(v, Fr(0)) for v in row] for row in w]) == 4:
                    rank4 = True
    return relT, relC, invol, homok, unit, flips, frame, pos_ok, rank4, len(pairs)


sf3 = sf3_check(3)
check('SF3', all(sf3[:9]), '(3;3,3,3), D = 11: relT %s, relC %s, G^2 = 1 %s, H a homMap %s, |z| = 1 %s, N z = -z %s, frame %s; '
      'posFwd blockwise PSD on %d product pairs %s; the image of the pure product (sector 0, +x) (x) (sector 0, +z) is not a '
      'product -- its (0,0) block has table rank 4 %s (extremality in jointStates not checked)'
      % (sf3[0], sf3[1], sf3[2], sf3[3], sf3[4], sf3[5], sf3[6], sf3[9], sf3[7], sf3[8]))


# ------------------------------------------------------------------ the strictly convex bodies
def pythag_units(D, extra=()):
    """Pythagorean unit vectors of R^D: signed permutations of the given integer tuples scaled by their norms"""
    base = {3: [(1, 0, 0), (3, 4, 0), (1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8)],
            4: [(1, 0, 0, 0), (3, 4, 0, 0), (1, 2, 2, 0), (1, 1, 1, 1), (1, 2, 2, 4), (2, 3, 6, 0), (2, 2, 1, 4)],
            5: [(1, 0, 0, 0, 0), (3, 4, 0, 0, 0), (1, 2, 2, 0, 0), (1, 1, 1, 1, 0), (1, 2, 2, 4, 0), (2, 3, 6, 0, 0),
                (1, 1, 3, 5, 0), (2, 2, 1, 4, 0)]}[D]
    out = set()
    for t in base + list(extra):
        nrm2 = sum(a * a for a in t)
        nrm = int(round(nrm2 ** 0.5))
        assert nrm * nrm == nrm2
        for perm in set(itertools.permutations(t)):
            for signs in itertools.product((1, -1), repeat=D):
                v = tuple(Fr(s * a, nrm) for s, a in zip(signs, perm))
                out.add(v)
    return sorted(out)


class Body:
    """a token body with its natural (z, N), exact state and effect pools, membership test"""

    def __init__(self, name, D, h, z, states, effects, member):
        self.name, self.D, self.h, self.z = name, D, h, z   # h: the D signs of N on the chart; H = (1, h)
        self.states, self.effects, self.member = states, effects, member
        self.hh = [Fr(1)] + [Fr(s) for s in h]


def ball_body(D, hsigns, zidx):
    units = pythag_units(D)
    random.shuffle(units)
    states = units[:36] + [tuple([Fr(0)] * D)] + [tuple(v / 2 for v in u) for u in units[36:42]]
    effects = [tuple([Fr(1, 2)] + [v / 2 for v in u]) for u in units[42:78]]       # (1 + v.x)/2
    z = [Fr(0)] * D
    z[zidx] = Fr(1)
    return Body('eball %d' % D, D, hsigns, z, states, effects, lambda x: sum(v * v for v in x) <= 1)


def omega_star5():
    """Omega*^5 = {(X, S): |X|^3 <= (1+S)(1-S)^2}, chart (X1..X4, S)"""
    def F(x):
        X, S = x[:4], x[4]
        n2 = sum(v * v for v in X)
        return n2 ** 3 - ((1 + S) * (1 - S) ** 2) ** 2       # sign of |X|^3 - (1+S)(1-S)^2 for (1+S)(1-S)^2 >= 0
    def member(x):
        S = x[4]
        if S < -1 or S > 1:
            return False
        return F(x) <= 0
    u4 = pythag_units(4)
    random.shuffle(u4)
    rings = [(Fr(0), Fr(1)), (Fr(7, 9), Fr(4, 9)), (Fr(-7, 9), Fr(8, 9))]
    states, bpoints = [], []
    for (S, rho) in rings:
        for u in u4[:10]:
            p = tuple([rho * v for v in u] + [S])
            states.append(p)
            bpoints.append(p)
    states += [tuple([Fr(0)] * 4 + [Fr(1)]), tuple([Fr(0)] * 4 + [Fr(-1)]), tuple([Fr(0)] * 5),
               tuple([Fr(0)] * 4 + [Fr(1, 2)]), tuple([Fr(0)] * 4 + [Fr(-1, 2)])]
    states += [tuple([v / 2 for v in u] + [Fr(0)]) for u in u4[10:14]]
    effects = []
    for p in bpoints:
        X, S = p[:4], p[4]
        nX2 = sum(v * v for v in X)
        rho = next(r for (s, r) in rings if s == S)
        g = [3 * rho * v for v in X] + [(1 - S) * (1 + 3 * S)]
        gp = sum(a * b for a, b in zip(g, p))
        kappa = gp + 3 * nX2 * Fr(11, 10) + abs(g[4])
        e = [1 - gp / kappa] + [v / kappa for v in g]
        effects.append(tuple(e))
    for u in u4[14:26]:
        for s in (Fr(0), Fr(1), Fr(-1)):
            v = list(u) + [s]
            M = Fr(11, 10) + abs(s)
            effects.append(tuple([Fr(1, 2)] + [c / (2 * M) for c in v]))
    effects.append(tuple([Fr(1, 2), Fr(0), Fr(0), Fr(0), Fr(0), Fr(1, 2)]))
    effects.append(tuple([Fr(1, 2), Fr(0), Fr(0), Fr(0), Fr(0), Fr(-1, 2)]))
    z = [Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]
    return Body('Omega*^5', 5, [1, -1, -1, -1, 1], z, states, effects, member), F, bpoints


B3 = ball_body(3, [NFLIP[0], NFLIP[1], NFLIP[2]], 2)
B5 = ball_body(5, [1, 1, -1, -1, -1], 2)
OM, F_om, bpoints_om = omega_star5()


def effects_valid(body):
    return all(0 <= sum(e[0:1]) + sum(e[j + 1] * x[j] for j in range(body.D)) <= 1 for e in body.effects for x in body.states)


def states_valid(body):
    return all(body.member(list(x)) for x in body.states)


# ------------------------------------------------------------------ the linear clauses: free pattern and frame
def hom(x): return [Fr(1)] + list(x)


def free_pattern(body):
    n = body.D + 1
    hh = body.hh
    free = []
    for mu in range(n):
        for nu in range(n):
            for mu2 in range(n):
                for nu2 in range(n):
                    if hh[nu] == hh[nu2] and hh[mu] == hh[mu2] * hh[nu2]:
                        free.append((mu * n + nu, mu2 * n + nu2))
    return free


def frame_system(body, free):
    n = body.D + 1
    z = body.z
    corner = {0: z, 1: [-v for v in z]}
    pos = {pq: i for i, pq in enumerate(free)}
    rows, rhs = [], []
    consistent_zero = True
    for a in (0, 1):
        for b in (0, 1):
            hx, hy = hom(corner[a]), hom(corner[(a + b) % 2])
            hx0, hy0 = hom(corner[a]), hom(corner[b])
            w = [hx0[i] * hy0[j] for i in range(n) for j in range(n)]
            u = [hx[i] * hy[j] for i in range(n) for j in range(n)]
            for p in range(n * n):
                row = {}
                for q in range(n * n):
                    if w[q] != 0 and (p, q) in pos:
                        row[pos[(p, q)]] = w[q]
                if not row:
                    if u[p] != 0:
                        consistent_zero = False
                    continue
                rows.append(row)
                rhs.append(u[p])
    ok, part, basis, rank = rref_solve(rows, rhs, len(free))
    return ok and consistent_zero, part, basis, rank


def matrix_from_vec(gvec, free, n):
    G = [[Fr(0)] * (n * n) for _ in range(n * n)]
    for (p, q), v in zip(free, gvec):
        if v != 0:
            G[p][q] = v
    return G


def frame_check_matrix(body, G):
    n = body.D + 1
    z = body.z
    corner = {0: z, 1: [-v for v in z]}
    for a in (0, 1):
        for b in (0, 1):
            hx0, hy0 = hom(corner[a]), hom(corner[b])
            w = [hx0[i] * hy0[j] for i in range(n) for j in range(n)]
            hx, hy = hom(corner[a]), hom(corner[(a + b) % 2])
            u = [hx[i] * hy[j] for i in range(n) for j in range(n)]
            img = [sum(G[p][q] * w[q] for q in range(n * n) if G[p][q] != 0) for p in range(n * n)]
            if img != u:
                return False
    return True


# C0: cnot lies in F for eball 3
free3 = free_pattern(B3)
C16 = cnot_matrix16()
freeset3 = set(free3)
outside_zero = all(C16[p][q] == 0 for p in range(16) for q in range(16) if (p, q) not in freeset3)
c0 = outside_zero and frame_check_matrix(B3, C16) and len(free3) == 64
check('C0', c0, 'eball 3 with N = nflip, z = z3: the parsed cnot is zero outside the %d-entry free pattern (%s) and meets the frame (%s)'
      % (len(free3), outside_zero, frame_check_matrix(B3, C16)))


# C1: the count for the strictly convex bodies
def count_ok(body):
    plus = sum(1 for s in body.hh if s == 1)
    return plus, 2 * plus == body.D + 1


c1 = all(count_ok(b)[1] for b in (B3, B5, OM)) and all(sum(v * v for v in b.z) == 1 for b in (B3, B5, OM))
nz_ok = all(all((b.hh[j + 1] * b.z[j]) == -b.z[j] for j in range(b.D)) for b in (B3, B5, OM))
check('C1', c1 and nz_ok, 'the count: ' + '; '.join('%s: +1 count %d of %d, meets %s' % (b.name, count_ok(b)[0], b.D + 1, count_ok(b)[1]) for b in (B3, B5, OM))
      + '; |z| = 1 and N z = -z for each: %s' % nz_ok)

# C2: Omega*^5 strict convexity on instances; z a boundary state
mid_ok = True
cnt = 0
for p, q in itertools.combinations(bpoints_om[:12], 2):
    m = tuple((a + b) / 2 for a, b in zip(p, q))
    cnt += 1
    if not (F_om(m) < 0 and OM.member(list(m))):
        mid_ok = False
zb = F_om(tuple(OM.z)) == 0 and OM.member(OM.z)
c2 = mid_ok and zb and states_valid(OM) and effects_valid(OM) and states_valid(B3) and effects_valid(B3) and states_valid(B5) and effects_valid(B5)
check('C2', c2, 'Omega*^5: %d midpoints of distinct exact boundary points strictly inside (F < 0) %s; z = e_2 on the boundary %s; '
      'every pooled state is a state and every pooled effect takes values in [0, 1] on the pooled states, all three bodies' % (cnt, mid_ok, zb))

# C3: the frame system for each body
Fdata = {}
c3 = True
c3txt = []
for b in (B3, B5, OM):
    free = free_pattern(b)
    ok, part, basis, rank = frame_system(b, free)
    Fdata[b.name] = (free, ok, part, basis, rank)
    c3 = c3 and ok and len(free) == (b.D + 1) ** 4 // 4
    c3txt.append('%s: %d free entries, frame consistent %s, rank %d, dim F = %d' % (b.name, len(free), ok, rank, len(basis) if basis else -1))
check('C3', c3, '; '.join(c3txt))


# C4: the positivity relaxation
def lp_relaxation(body, max_iter=40, seed=1):
    free, ok, part, basis, rank = Fdata[body.name]
    n = body.D + 1
    nn = n * n
    nfree = len(free)
    nvar = len(basis)
    # float representations
    G0 = np.zeros((nn, nn))
    for (p, q), v in zip(free, part):
        G0[p, q] = float(v)
    Nmat = np.zeros((nfree, nvar))
    for k, bv in enumerate(basis):
        for i, v in enumerate(bv):
            if v != 0:
                Nmat[i, k] = float(v)
    fp = np.array([p for p, q in free])
    fq = np.array([q for p, q in free])
    S = np.array([[float(v) for v in hom(x)] for x in body.states])       # ns x n
    E = np.array([[float(v) for v in e] for e in body.effects])           # ne x n
    ns, ne = len(body.states), len(body.effects)
    prods = [(i, j) for i in range(ns) for j in range(ns)]
    epairs = [(a, b) for a in range(ne) for b in range(ne)]
    Omega = np.array([np.outer(S[i], S[j]).reshape(nn) for i, j in prods])            # np x nn

    def coeff_rows(cons):
        """for constraints (pi, ei): rows a (nvar) and const c such that value = c + a . lambda"""
        A = np.zeros((len(cons), nvar))
        cvec = np.zeros(len(cons))
        for r, (pi, ei) in enumerate(cons):
            i, j = prods[pi]
            a, b = epairs[ei]
            w = Omega[pi]
            ef = np.outer(E[a], E[b]).reshape(nn)
            dvec = ef[fp] * w[fq]                      # over free entries
            A[r] = dvec @ Nmat
            cvec[r] = dvec @ np.array([float(v) for v in part])
        return A, cvec

    def all_values(lam):
        gvec = np.array([float(v) for v in part]) + Nmat @ lam
        G = np.zeros((nn, nn))
        G[fp, fq] = gvec
        GO = Omega @ G.T                                   # np x nn
        M = GO.reshape(len(prods), n, n)
        vals = np.einsum('ai,pij,bj->pab', E, M, E)        # np x ne x ne
        return vals.reshape(len(prods), ne * ne)

    rng = random.Random(seed)
    cons = set()
    while len(cons) < min(1500, len(prods) * len(epairs)):
        cons.add((rng.randrange(len(prods)), rng.randrange(len(epairs))))
    cons = list(cons)
    status = None
    lam = np.zeros(nvar)
    for it in range(max_iter):
        A, cvec = coeff_rows(cons)
        # maximise t: c + A lam >= t  <=>  -A lam + t <= c ; t <= 1
        c_obj = np.zeros(nvar + 1)
        c_obj[-1] = -1.0
        A_ub = np.hstack([-A, np.ones((len(cons), 1))])
        res = linprog(c_obj, A_ub=A_ub, b_ub=cvec, bounds=[(None, None)] * nvar + [(None, 1.0)], method='highs')
        if res.status != 0:
            status = 'LP-ERROR(%d)' % res.status
            break
        lam = res.x[:nvar]
        tstar = res.x[-1]
        if tstar < -1e-7:
            status = 'INFEASIBLE'
            break
        vals = all_values(lam)
        viol = np.argwhere(vals < -1e-9)
        if len(viol) == 0:
            status = 'FEASIBLE(pool)'
            break
        order = np.argsort(vals[viol[:, 0], viol[:, 1]])[:600]
        for o in order:
            cons.append((int(viol[o, 0]), int(viol[o, 1])))
    if status is None:
        status = 'UNDECIDED(iterations)'
    cert = None
    if status == 'INFEASIBLE':
        # Farkas: max y.b s.t. A^T y = 0, sum y = 1, y >= 0 with constraints a_i . lam >= b_i, b_i = -c_i
        A, cvec = coeff_rows(cons)
        bvec = -cvec
        m = len(cons)
        A_eq = np.vstack([A.T, np.ones((1, m))])
        b_eq = np.zeros(nvar + 1)
        b_eq[-1] = 1.0
        res = linprog(-bvec, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * m, method='highs')
        if res.status == 0 and -res.fun > 1e-9:
            y = res.x
            supp = [i for i in range(m) if y[i] > 1e-12]
            # exact rows for the support
            exact_cols, exact_b = [], []
            for i in supp:
                pi, ei = cons[i]
                si, sj = prods[pi]
                ea, eb = epairs[ei]
                hx, hy = hom(body.states[si]), hom(body.states[sj])
                w = [hx[u] * hy[v] for u in range(n) for v in range(n)]
                ef = [body.effects[ea][u] * body.effects[eb][v] for u in range(n) for v in range(n)]
                dvec = [ef[p] * w[q] for (p, q) in free]
                arow = [sum(dvec[t] * bv[t] for t in range(nfree) if dvec[t] != 0 and bv[t] != 0) for bv in basis]
                cconst = sum(dvec[t] * part[t] for t in range(nfree) if dvec[t] != 0 and part[t] != 0)
                exact_cols.append(arow)
                exact_b.append(-cconst)
            ker = nullspace_cols(exact_cols, nvar)
            verified = False
            yx = None
            if len(ker) >= 1:
                # express the float certificate in the exact kernel (least squares), round, verify exactly
                K = np.array([[float(v) for v in kv] for kv in ker]).T   # |supp| x dimker
                yf = np.array([y[i] for i in supp])
                coef, *_ = np.linalg.lstsq(K, yf, rcond=None)
                for den in (10 ** 6, 10 ** 9, 10 ** 12):
                    cr = [Fr(float(c)).limit_denominator(den) for c in coef]
                    yx = [sum(cr[k] * ker[k][t] for k in range(len(ker))) for t in range(len(supp))]
                    if all(v >= 0 for v in yx) and any(v > 0 for v in yx):
                        pair = sum(yx[t] * exact_b[t] for t in range(len(supp)))
                        combo = [sum(yx[t] * exact_cols[t][k] for t in range(len(supp))) for k in range(nvar)]
                        if pair > 0 and all(v == 0 for v in combo):
                            verified = True
                            break
                if not verified and len(ker) == 1:
                    kv = ker[0]
                    sgn = 1 if sum(kv[t] * exact_b[t] for t in range(len(supp))) > 0 else -1
                    yx = [sgn * v for v in kv]
                    if all(v >= 0 for v in yx):
                        pair = sum(yx[t] * exact_b[t] for t in range(len(supp)))
                        combo = [sum(yx[t] * exact_cols[t][k] for t in range(len(supp))) for k in range(nvar)]
                        verified = pair > 0 and all(v == 0 for v in combo)
            cert = {'support': len(supp), 'dimker': len(ker), 'verified': verified, 'float_gap': float(-res.fun)}
            status = 'INFEASIBLE-CERTIFIED' if verified else 'INFEASIBLE-UNCERTIFIED'
        else:
            status = 'INFEASIBLE-UNCERTIFIED'
    return status, len(cons), lam, cert


c4txt = []
c4_status = {}
for b in (B3, B5, OM):
    st, ncons, lam, cert = lp_relaxation(b)
    c4_status[b.name] = st
    c4txt.append('%s: %s (%d constraints%s)' % (b.name, st, ncons, (', certificate support %d, kernel dim %d, float gap %.3g' % (cert['support'], cert['dimker'], cert['float_gap'])) if cert else ''))
c4 = all(st in ('FEASIBLE(pool)', 'INFEASIBLE-CERTIFIED', 'INFEASIBLE-UNCERTIFIED') for st in c4_status.values()) and c4_status['eball 3'] == 'FEASIBLE(pool)'
check('C4', c4, '; '.join(c4txt))

# ------------------------------------------------------------------ countercontrols
xo1 = c4_status['eball 3'].startswith('INFEASIBLE')
print('COUNTER XO1 %s: "eball 3 is INFEASIBLE" -- status %s' % ('fails as stated' if not xo1 else 'DOES NOT FAIL', c4_status['eball 3']), flush=True)
_, bnd, _ = sf2_witness(2, (3, 3))
xo2 = not bnd
print('COUNTER XO2 %s: "the sector body (2;3,3) is relatively strictly convex at the probed midpoint" -- the midpoint is a boundary state: %s'
      % ('fails as stated' if not xo2 else 'DOES NOT FAIL', bnd), flush=True)
xo3 = not Fdata['eball 3'][1]
print('COUNTER XO3 %s: "the frame equations are inconsistent for eball 3" -- consistent: %s' % ('fails as stated' if not xo3 else 'DOES NOT FAIL', Fdata['eball 3'][1]), flush=True)

nf = sum(1 for _, ok in RESULTS if not ok)
print('checks: %d, failures: %d' % (len(RESULTS), nf), flush=True)
counters_ok = (not xo1) and (not xo2) and (not xo3)
if nf == 0 and len(RESULTS) == 8 and counters_ok:
    print('VERDICT E20-ODD-BODIES-EXACT', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s%s' % ([n for n, ok in RESULTS if not ok], '' if counters_ok else ' (a countercontrol did not fail as stated)'), flush=True)
print('exit 0' if nf == 0 and counters_ok else 'exit 1')
sys.exit(0 if nf == 0 and counters_ok else 1)
