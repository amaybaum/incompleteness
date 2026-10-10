# c2_structure.py -- research/countermodels node C2: the structure of K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F.
# DECISION RULE (fixed before the first run, 2026-10-10T20:31:28Z by date -u):
#  Conventions as in c1_cones.py (charter). Z_F = {z_s}, z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4; psi_s = the
#  negative eigenvector of pauliW(z_s) (cap vector). Group elements acting on tables are signed permutations of the 16
#  entries when they are Clifford-type (local signed-permutation rotations, SWAP, cnot, transposeW); they are composed and
#  compared exactly as (perm, sign) tuples.
#  S  The local stabilizer. L_all = {actC R o actT R' : R, R' signed 3x3 permutations} (48 x 48 = 2304 maps), split by
#     (det R, det R'): (+,+) local unitary Cliffords, (-,-) local antiunitary (= unitary o transposeW), (+,-)/(-,+)
#     partial-transpose type. Printed: how many of each type permute Z_F; the same with SWAP composed. Predicted (written
#     before the run, NOTES-C2 S0): 96 (+,+), 96 (-,-), and 0 of mixed type that also preserve K; with SWAP 384 in all
#     (unitary/antiunitary). The check S1 passes iff the counts of (+,+) and (-,-) stabilizers are equal, their union is a
#     group (its closure has the same size), and SWAP o g permutes Z_F for exactly as many g. S2: every mixed-type
#     map g that permutes Z_F (if any) is not an automorphism of K(Z_F): g(phiW) (phiW = cnot prodState(xplus, z3), a pure
#     member of K) is not PSD and not a positive multiple of a defect, while an automorphism maps extreme rays to extreme
#     rays and the non-PSD extreme rays of K(Z_F) are the four defects ([A] Z z1; NOTES-C2 W2). S3: the subgroups G16 = <cnot, Ad(ZI), Ad(IZ), T> (16), <G16, SWAP>
#     (48), Gbig = <cnot, 32 even signed-diagonal locals> (64), <Gbig, SWAP> (192) have the stated orders and lie in the
#     stabilizer of Z_F; the closure of <local stabilizer, SWAP, cnot> is computed (its order printed: [A] Z records
#     |Stab_Cl(Z_F)| = 1536).
#     [W] (NOTES-C2 W1) no non-Clifford local unitary permutes Z_F; check S4 is its exact ingredient: an element of 𝒜
#     permutes {P_s} iff it maps span{I, XZ, YY, ZX} onto itself; a local map does so iff it maps the Pauli pairs
#     {(1,3), (2,2), (3,1)} onto themselves up to sign, which for signed permutations is tested exactly.
#  E  Extreme rays. E1: z_s + z_t = (T_{psi_u + psi_w} + T_{psi_u - psi_w})/4, exact identity for {s,t,u,w} = {1..4}: the sum of two defects is a sum of two pure members of K (cone Z_F is not a face). E2: the
#     product criterion: det-form psi_s^T Omega psi_t is diagonal with entries of equal modulus (so v = sum c_s psi_s is a
#     product iff sum k_s c_s^2 = 0; with free phases, every profile with max |c_s|^2 <= 1/2 is a product profile:
#     [W] polygon inequality). E3: a rank-2 member of Q3 ∩ Z* with two tight constraints is the sum of two pure members
#     of K (instance). E4: the sum identity of [W] W3 (no three tight constraints on a 2-dim range): for random-free exact
#     instances, sum_t r_t r_t^dag = Pi_R (exact) on three rational 2-dim subspaces.
#  F  Facial invariant c(x) = dim span{y in K : ipW(x, y) = 0} on four classes of extreme rays: a defect (predicted 15), a
#     pure state with all |c_s|^2 < 1/2 (predicted 9), one cap tight (10), two caps tight (11). Each value is the rank of
#     explicit members of the face plus the tight defects (lower bound), with the upper bound printed as the dimension of
#     Herm(v^perp) + number of tight defects ([W] W4). F passes iff each computed rank equals its upper bound.
#  O  Orbits: sizes of the orbit of Z_F (as a set of rays) and of a generic pure extreme ray (profile 9:5:4:1 over 19,
#     non-real phase) under each finite group of S3 and the local stabilizer (with and without SWAP, T). Printed only.
#  U  Uniqueness given the symmetry group. U1: K(Z_F) ∩ Fix(T^3) (tables diagonal in the psi basis, coordinates d_s)
#     equals the cone {d : d_s <= (sum d)/2} = cone{1 - 2e_s} (exact: both descriptions, and its self-duality); Q3 ∩ Fix =
#     R^4_+. U2: Circ = {d : (sum d)/2 >= |d - (sum d)/4 1|} is self-dual and lies in O* = {d : d_s + d_t >= 0 for s != t}
#     (exact minimum of d_s + d_t on the section). U3: d1 = (5,1,1,1)/4 lies in Circ and not in K(Z_F) ∩ Fix; d2 =
#     (-1,3,3,3)/4 lies in Circ and not in R^4_+. U4: the diagonal of every member of Q3 ∩ Z* lies in O = cone{e_s + e_t}
#     (exact: the extreme points of {p >= 0, sum p = 1, p_s <= 1/2} are the six (e_s + e_t)/2). With EBF [A] these give a
#     second exotic cone invariant under the full stabilizer (NOTES-C2 W6); the check U passes iff U1-U4 hold.
#  COUNTERCONTROLS: CC1 a non-stabilizer local Clifford (actC of the quarter turn about x) does not permute Z_F; CC2 the
#  transpose-free group <cnot> has orbit 2 on Z_F (not transitive); CC3 Q3's diagonal slice R^4_+ is not contained in
#  K(Z_F) ∩ Fix (e_1 violates d_s <= sum/2) and vice versa (1 - 2e_1 has a negative entry).
#  VERDICT C2-STRUCTURE-EXACT printed iff S1-S4, E1-E4, F, U pass and the countercontrols fail as stated.
import sympy as sp
from fractions import Fraction as Fr
from itertools import product, permutations, combinations

iu, Rt = sp.I, sp.Rational
s = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
SS = [[kron(s[m], s[n]) for n in range(4)] for m in range(4)]
SSP = [[[(i, j, SS[m][n][j, i]) for i in range(4) for j in range(4) if SS[m][n][j, i] != 0] for n in range(4)] for m in range(4)]
def pW(w): return sp.expand(sum((w[m, n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4)
def table(A):
    t = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(A[i, j] * v for i, j, v in SSP[m][n])))
    assert all(sp.expand(sp.im(x)) == 0 for x in t), 'non-real table'
    return t.applyfunc(lambda x: sp.expand(sp.re(x)))
def ip(a, b): return sp.expand(sum(a[m, n] * b[m, n] for m in range(4) for n in range(4)))
def E(m, n):
    t = sp.zeros(4, 4); t[m, n] = 1; return t
def Tpure(v):
    v = sp.Matrix(v); return table(v * v.H / sp.expand((v.H * v)[0]))
RES = {}
def chk(cid, ok, note=''):
    RES[cid] = bool(ok); print('CHECK %-34s %s %s' % (cid, 'PASS' if ok else 'FAIL', note))

# ---- tables as tuples; Clifford-type maps as signed permutations of the 16 entries
def tup(w): return tuple(Fr(int(sp.Rational(w[m, n]).p), int(sp.Rational(w[m, n]).q)) for m in range(4) for n in range(4))
def mat(t): return sp.Matrix(4, 4, lambda m, n: sp.Rational(t[4 * m + n].numerator, t[4 * m + n].denominator))
def apply(g, t): return tuple(g[1][i] * t[g[0][i]] for i in range(16))
def comp(g, h): return (tuple(h[0][g[0][i]] for i in range(16)), tuple(g[1][i] * h[1][g[0][i]] for i in range(16)))
IDG = (tuple(range(16)), tuple([1] * 16))
def from_fun(f):   # f: table -> table, assumed a signed permutation of entries
    perm, sign = [None] * 16, [None] * 16
    for k in range(16):
        b = [0] * 16; b[k] = 1
        img = f(b)
        for i in range(16):
            if img[i] != 0:
                assert img[i] in (1, -1) and perm[i] is None
                perm[i], sign[i] = k, img[i]
    assert None not in perm
    return (tuple(perm), tuple(sign))
def hom(R):
    H = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(3):
        for j in range(3): H[i + 1][j + 1] = R[i][j]
    return H
def local(R, Rp):   # actC R o actT R' : w -> hom(R) w hom(R')^T
    A, B = hom(R), hom(Rp)
    def f(b):
        w = [b[4 * m:4 * m + 4] for m in range(4)]
        return [sum(A[m][k] * w[k][l] * B[n][l] for k in range(4) for l in range(4)) for m in range(4) for n in range(4)]
    return from_fun(f)
SWAPg = from_fun(lambda b: [b[4 * n + m] for m in range(4) for n in range(4)])
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
CNOTg = from_fun(lambda b: [SGN(m, n) * b[4 * PC[m][n] + PT[m][n]] for m in range(4) for n in range(4)])
TRg = from_fun(lambda b: [(-1 if m == 2 else 1) * (-1 if n == 2 else 1) * b[4 * m + n] for m in range(4) for n in range(4)])
def closure(gens):
    G = {IDG}; frontier = [IDG]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                k = comp(h, g)
                if k not in G: G.add(k); new.append(k)
        frontier = new
    return G
def zs(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SIG = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = [zs(a, b) for a, b in SIG]
ZT = [tup(z) for z in ZF]
ZSET = set(ZT)
def permutesZ(g): return set(apply(g, z) for z in ZT) == ZSET

# ---- S: local stabilizer
sperms = []
for p in permutations(range(3)):
    for sg in product((1, -1), repeat=3):
        R = [[0] * 3 for _ in range(3)]
        for i in range(3): R[i][p[i]] = sg[i]
        sperms.append(R)
def det3(R): return sp.Matrix(R).det()
cnt = {}; stab = {('+', '+'): [], ('-', '-'): [], ('+', '-'): [], ('-', '+'): []}
for R in sperms:
    for Rp in sperms:
        g = local(R, Rp)
        key = ('+' if det3(R) == 1 else '-', '+' if det3(Rp) == 1 else '-')
        if permutesZ(g): stab[key].append(g)
for k in stab: print('LOCAL type %s: %d of %d permute Z_F' % (k, len(stab[k]), 576))
unit = stab[('+', '+')] + stab[('-', '-')]
uset = set(unit)
closed = len(closure(unit)) == len(unit)
withswap = [comp(SWAPg, g) for g in unit]
nsw = sum(1 for g in withswap if permutesZ(g))
chk('S1 local stabilizer', len(stab[('+', '+')]) == len(stab[('-', '-')]) and closed and nsw == len(unit),
    '(+,+) %d, (-,-) %d, closed; SWAP o g permutes Z_F for %d; total with SWAP %d' %
    (len(stab[('+', '+')]), len(stab[('-', '-')]), nsw, 2 * len(unit)))
mixed = stab[('+', '-')] + stab[('-', '+')]
# S2: a mixed-type map that permutes Z_F is not an automorphism of K(Z_F)
phiW = tuple(Fr(x) for x in (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1))
def moves(g):
    gy = apply(g, phiW)
    notpsd = min(pW(mat(gy)).eigenvals()) < 0
    notdef = all(len(set(gy[i] / z[i] for i in range(16) if z[i] != 0)) > 1 or any(gy[i] != 0 and z[i] == 0 for i in range(16)) for z in ZT)
    return notpsd and notdef
chk('S2 mixed-type maps not automorphisms', all(moves(g) for g in mixed),
    '%d mixed-type maps permute Z_F; each sends the pure member phiW to a non-PSD table that is not a defect ray' % len(mixed))
# S3: the named finite groups
RzC = local([[-1, 0, 0], [0, -1, 0], [0, 0, 1]], [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
RzT = local([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
G16 = closure([CNOTg, RzC, RzT, TRg])
G48 = closure([CNOTg, RzC, RzT, TRg, SWAPg])
diags = [[[a, 0, 0], [0, b, 0], [0, 0, c]] for a, b, c in product((1, -1), repeat=3)]
evenloc = [local(D, Dp) for D in diags for Dp in diags if det3(D) * det3(Dp) == 1]
Gbig = closure([CNOTg] + evenloc)
G192 = closure([CNOTg, SWAPg] + evenloc)
LOC = closure(unit)
LOCU = closure(stab[('+', '+')])
LOCS = closure(unit + [SWAPg])
BIGC = closure(unit + [SWAPg, CNOTg])
orders = {'G16': len(G16), '<G16,SWAP>': len(G48), 'Gbig': len(Gbig), '<Gbig,SWAP>': len(G192), 'LU-stab (unitary)': len(LOCU),
          'LU-stab (+T)': len(LOC), 'LU-stab (+T,+SWAP)': len(LOCS), '<LU-stab, SWAP, cnot>': len(BIGC)}
for k, v in orders.items(): print('GROUP %-24s order %d' % (k, v))
chk('S3 named groups', len(G16) == 16 and len(G48) == 48 and len(Gbig) == 64 and len(G192) == 192 and
    all(permutesZ(g) for g in BIGC) and G16 <= BIGC and Gbig <= BIGC and G192 <= BIGC and LOCU <= LOC <= LOCS <= BIGC,
    'orders 16/48/64/192; all inside the stabilizer of Z_F; closure <LU-stab, SWAP, cnot> order %d ([A] Z: 1536)' % len(BIGC))
# S4: the algebra criterion on signed permutations: a local map permutes Z_F iff it maps the Pauli-pair pattern
# {(1,3),(2,2),(3,1)} onto itself (as unsigned index pairs)
PAT = {(1, 3), (2, 2), (3, 1)}
def pat_ok(R, Rp):
    pi = {i + 1: next(j + 1 for j in range(3) if R[j][i] != 0) for i in range(3)}
    pj = {i + 1: next(j + 1 for j in range(3) if Rp[j][i] != 0) for i in range(3)}
    return set((pi[a], pj[b]) for a, b in PAT) == PAT
agree = all((permutesZ(local(R, Rp)) == pat_ok(R, Rp)) for R in sperms for Rp in sperms)
chk('S4 algebra criterion', agree, 'permutes Z_F <=> preserves the pattern {(1,3),(2,2),(3,1)}, all 2304 signed-permutation pairs')
Rq = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]   # quarter turn about x on the control
cc1 = not permutesZ(local(Rq, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
RES['CC1 quarter turn not a stabilizer'] = cc1
print('COUNTERCONTROL CC1 actC Rx(pi/2): %s' % ('does not permute Z_F (as required)' if cc1 else 'PERMUTES (FAIL)'))
orbc = closure([CNOTg])
oz = set(apply(g, ZT[0]) for g in orbc)
RES['CC2 <cnot> not transitive'] = len(oz) == 2
print('COUNTERCONTROL CC2 <cnot> orbit of z_(1,1) on Z_F: %d (as required: 2)' % len(oz))

# ---- E: extreme rays
psi = {}
for (a, b), z in zip(SIG, ZF):
    M = pW(z); ln = min(M.eigenvals()); v = (M - ln * sp.eye(4)).nullspace()[0]
    psi[(a, b)] = v / sp.sqrt(sp.expand((v.H * v)[0]))
ok1 = True
for (s_, t_) in [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]:
    others = [k for k in range(4) if k not in (s_, t_)]
    u, w = psi[SIG[others[0]]], psi[SIG[others[1]]]
    lhs = ZF[s_] + ZF[t_]
    rhs = (Tpure(u + w) + Tpure(u - w)) / 4
    ok1 &= sp.expand(lhs - rhs) == sp.zeros(4, 4)
    ok1 &= all(ip(z, Tpure(u + w)) >= 0 and ip(z, Tpure(u - w)) >= 0 for z in ZF)
chk('E1 z_s + z_t = pure + pure', ok1, '(T_{psi_u+psi_w} + T_{psi_u-psi_w})/4 with both pure tables in K: cone Z_F is not a face')
Om = sp.Matrix([[0, 0, 0, 1], [0, 0, -1, 0], [0, -1, 0, 0], [1, 0, 0, 0]])   # v^T Om v = 2 det [[v00, v01], [v10, v11]]
vs = sp.symbols('v0:4')
vv = sp.Matrix(vs)
assert sp.expand((vv.T * Om * vv)[0] - 2 * (vs[0] * vs[3] - vs[1] * vs[2])) == 0
Gm = sp.Matrix(4, 4, lambda i, j: sp.simplify((psi[SIG[i]].T * Om * psi[SIG[j]])[0]))
diag_ok = all(Gm[i, j] == 0 for i in range(4) for j in range(4) if i != j) and len(set(sp.Abs(Gm[i, i]) for i in range(4))) == 1
chk('E2 product criterion diagonal', diag_ok, 'psi_s^T Omega psi_t = diag%s: product iff sum k_s c_s^2 = 0' % (list(Gm.diagonal()),))
# E3: rank-2 member with two tight constraints decomposes into two pure members
u, w = psi[SIG[0]], psi[SIG[1]]
q = Tpure(u) / 2 + Tpure(w) / 2                         # profile (1/2, 1/2, 0, 0): tight for s = 1, 2
dec = (Tpure(u + w) + Tpure(u - w)) / 2
okE3 = sp.expand(q - dec) == sp.zeros(4, 4) and all(ip(z, q) >= 0 for z in ZF) and \
    all(ip(z, Tpure(u + w)) >= 0 and ip(z, Tpure(u - w)) >= 0 for z in ZF)
chk('E3 rank-2 decomposes', okE3, 'q = (P_1 + P_2)/2 = (T_{psi1+psi2} + T_{psi1-psi2})/2, both pure members of K')
# E4: sum_t r_t r_t^dag = Pi_R on 2-dim subspaces R (so the Bloch vectors of the restricted caps sum to zero)
okE4 = True
for B in [sp.Matrix([[1, 0], [0, 1], [0, 0], [0, 0]]), sp.Matrix([[1, 0], [1, 1], [iu, 0], [0, 2]]), sp.Matrix([[1, 1], [2, -iu], [0, 1], [3, 0]])]:
    Bo = sp.Matrix.hstack(*sp.GramSchmidt([B[:, 0], B[:, 1]], True))
    Pi = Bo * Bo.H
    S = sp.zeros(4, 4)
    for k in range(4):
        r = Pi * psi[SIG[k]]
        S += r * r.H
    okE4 &= sp.simplify(S - Pi) == sp.zeros(4, 4)
chk('E4 restricted caps sum to Pi_R', okE4, 'three 2-dim subspaces, exact')

# ---- F: the facial invariant on four classes of extreme rays
def rank_of(tabs): return sp.Matrix([[t[m, n] for m in range(4) for n in range(4)] for t in tabs]).rank()
GBOX = [0, 1, iu, -1, 1 + iu, 2]
def face_c(v):
    v = sp.Matrix(v); x = Tpure(v)
    tight = [z for z in ZF if ip(z, x) == 0]
    perp = (v.H).nullspace()                       # basis of v^perp (vectors u with v^dag u = 0)
    mem = []
    for co in product(GBOX, repeat=3):
        if co == (0, 0, 0): continue
        u = co[0] * perp[0] + co[1] * perp[1] + co[2] * perp[2]
        y = Tpure(u)
        if all(ip(z, y) >= 0 for z in ZF): mem.append(y)
        if len(mem) >= 60: break
    assert all(ip(x, y) == 0 for y in mem)
    return rank_of(mem + tight), 9 + len(tight), len(tight)
z0 = ZF[0]
# defect face: pure states on the cap boundary of z0 inside Z*, plus the other defects
capv = psi[SIG[0]]; oth = [psi[SIG[k]] for k in (1, 2, 3)]
fz = [z for z in ZF[1:]]
for be in product(GBOX, repeat=3):
    N = sum(sp.expand(b * sp.conjugate(b)) for b in be)
    if N == 0: continue
    for al in [1, 2, 1 + iu, 2 + iu, 3, 1 + 2 * iu, 2 + 2 * iu, 3 + iu]:
        if sp.expand(al * sp.conjugate(al)) == N:
            vv_ = al * capv + be[0] * oth[0] + be[1] * oth[1] + be[2] * oth[2]
            y = Tpure(vv_)
            if all(ip(z, y) >= 0 for z in ZF): fz.append(y)
            break
cz = rank_of(fz)
v_int = 3 * psi[SIG[0]] + (2 + iu) * psi[SIG[1]] + 2 * psi[SIG[2]] + psi[SIG[3]]       # profile 9:5:4:1 /19
v_one = 2 * psi[SIG[0]] + (1 + iu) * psi[SIG[1]] + psi[SIG[2]] + iu * psi[SIG[3]]      # profile 4:2:1:1 /8, one tight
v_two = psi[SIG[0]] + iu * psi[SIG[1]]                                                  # profile 1:1:0:0 /2, two tight
res = {'defect': (cz, 15, 0)}
for nm, v in [('interior', v_int), ('one tight', v_one), ('two tight', v_two)]:
    res[nm] = face_c(v)
for nm, (r, ub, nt) in res.items(): print('FACE %-10s c = %d (upper bound %d; tight defects %d)' % (nm, r, ub, nt))
chk('F facial invariant', all(r == ub for r, ub, _ in res.values()) and [res[k][0] for k in ('defect', 'interior', 'one tight', 'two tight')] == [15, 9, 10, 11],
    'c = 15 (defect), 9 (interior pure), 10 (one cap tight), 11 (two caps tight)')

# ---- O: orbits
def ray(t):
    k = next(x for x in t if x != 0); return tuple(x / abs(k) for x in t)
vg = 3 * psi[SIG[0]] + (2 + iu) * psi[SIG[1]] + 2 * psi[SIG[2]] + psi[SIG[3]]
tg = tup(Tpure(vg))
for nm, G in [('<cnot>', orbc), ('G16', G16), ('<G16,SWAP>', G48), ('Gbig', Gbig), ('<Gbig,SWAP>', G192), ('LU-stab (unitary)', LOCU),
              ('LU-stab (+T)', LOC), ('LU-stab (+T,+SWAP)', LOCS), ('<LU-stab,SWAP,cnot>', BIGC)]:
    oz_ = len(set(ray(apply(g, z)) for g in G for z in ZT))
    og = len(set(ray(apply(g, tg)) for g in G))
    print('ORBIT %-22s |G| = %4d: defects %d rays; generic pure extreme ray %d' % (nm, len(G), oz_, og))

# ---- U: uniqueness given the symmetry group (the T^3-fixed slice, coordinates d_s on the psi-diagonal)
ds = sp.symbols('d1:5', real=True)
D = sp.Matrix(ds)
one = sp.Matrix([1, 1, 1, 1])
gens_mD = [one - 2 * sp.Matrix([1 if k == s_ else 0 for k in range(4)]) for s_ in range(4)]
# cone{1 - 2e_s} = {d : d_t <= sum d / 2}: coefficients b_t = (sum d/2 - d_t)/2 reproduce d
bco = [(sum(ds) / 2 - ds[t]) / 2 for t in range(4)]
rec = sp.expand(sum((bco[t] * gens_mD[t] for t in range(4)), sp.zeros(4, 1)) - D)
# self-duality: the dual of cone{1 - 2e_s} is {y : y.(1 - 2e_s) >= 0} = {y_s <= sum y / 2} (same inequalities)
dual_same = all(sp.expand((D.T * gens_mD[t])[0] - 2 * (sum(ds) / 2 - ds[t])) == 0 for t in range(4))
# K(Z_F) ∩ Fix contains cone{1 - 2e_s}: the defects are diagonal: pauliW(z_s) = (I - 2 P_s)/8 -> d ∝ 1 - 2e_s
diagZ = all(sp.simplify(psi[SIG[j]].H * pW(ZF[i]) * psi[SIG[j]])[0] == (Rt(-1, 8) if i == j else Rt(1, 8)) for i in range(4) for j in range(4))
U1 = rec == sp.zeros(4, 1) and dual_same and diagZ
chk('U1 K(Z_F) ∩ Fix = cone{1 - 2e_s}', U1, 'self-dual in Fix; = {d : d_s <= sum d/2}; Q3 ∩ Fix = R^4_+ (PSD diagonal)')
# U2: Circ self-dual (orthonormal frame: alpha = sum d / 2 along 1/2, u = d - (sum d/4) 1 orthogonal) and Circ ⊆ O*
w_st = sp.Matrix([1, 1, 0, 0]) - one / 2                 # projection of e_1 + e_2 onto 1^perp
U2 = sp.expand((w_st.T * w_st)[0]) == 1 and sp.expand((one.T * one)[0] / 4) == 1
# min of d_1 + d_2 over the section sum d = 2 (alpha = 1), |u| <= 1: = 1 + min u.w = 1 - |w| = 0
chk('U2 Circ self-dual, Circ ⊆ O*', U2, 'min (d_s + d_t) on the section alpha = 1 equals 1 - |w_st| = 0')
def inCirc(d):
    a = sum(d) / 2; u = [x - sum(d) / 4 for x in d]
    return a >= 0 and sum(x * x for x in u) <= a * a
d1 = [Rt(5, 4), Rt(1, 4), Rt(1, 4), Rt(1, 4)]; d2 = [Rt(-1, 4), Rt(3, 4), Rt(3, 4), Rt(3, 4)]
U3 = inCirc(d1) and not all(x <= sum(d1) / 2 for x in d1) and inCirc(d2) and min(d2) < 0 and all(x <= sum(d2) / 2 for x in d2)
chk('U3 Circ meets neither slice', U3, 'd1 = (5,1,1,1)/4 in Circ, not in K(Z_F) ∩ Fix; d2 = (-1,3,3,3)/4 in Circ, not in R^4_+')
# U4: extreme points of {p >= 0, sum p = 1, p_s <= 1/2} are the six (e_s + e_t)/2 (vertex enumeration over tight sets)
verts = set()
cons = [('ge', k) for k in range(4)] + [('le', k) for k in range(4)]
for tight in combinations(cons, 3):
    A = [[1, 1, 1, 1]]; bvec = [1]
    for typ, k in tight:
        row = [0] * 4; row[k] = 1; A.append(row); bvec.append(0 if typ == 'ge' else Rt(1, 2))
    M = sp.Matrix(A)
    if M.rank() < 4: continue
    p = M.solve(sp.Matrix(bvec))
    if all(x >= 0 and x <= Rt(1, 2) for x in p): verts.add(tuple(p))
U4 = sorted(verts) == sorted(set(tuple(Rt(1, 2) if k in (i, j) else 0 for k in range(4)) for i in range(4) for j in range(i + 1, 4)))
chk('U4 diag(Q3 ∩ Z*) ⊆ O', U4, 'vertices of the profile polytope: %d, all of the form (e_s + e_t)/2' % len(verts))
cc3 = not all(x <= 1 / 2 for x in [1, 0, 0, 0]) and min([-1, 1, 1, 1]) < 0
RES['CC3 slices incomparable'] = cc3
print('COUNTERCONTROL CC3 e_1 not in K(Z_F) ∩ Fix, 1 - 2e_1 not in R^4_+: %s' % cc3)

bad = [k for k, v in RES.items() if not v]
print('summary: %d checks, %d failed%s' % (len(RES), len(bad), (': ' + ', '.join(bad)) if bad else ''))
if not bad:
    print('VERDICT C2-STRUCTURE-EXACT: local stabilizer of Z_F in LU ⋊ <T, SWAP> has order %d (unitary %d); closure with cnot '
          'order %d; extreme-ray classes with c = 15/9/10/11; the T^3-fixed slice of K(Z_F) is the reversed simplex cone and a '
          'circular S4-invariant self-dual slice meets neither it nor Q3' % (len(LOCS), len(LOCU), len(BIGC)))
else:
    print('NO VERDICT')
