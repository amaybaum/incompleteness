"""z1_swap.py -- thread Z, node S1 (token exchange SWAP added to the even class G16). PT stage 4. EXACT.

Tables w in W 3 indexed (mu, nu), mu = control (first token), 0 = homogenizing coordinate, 1..3 = x, y, z;
pauliW w = 1/4 sum w_{mu nu} s_mu (x) s_nu; ipW w v = sum w_{mu nu} v_{mu nu}. Maps are 16x16 signed permutations.
Landed tables transcribed from CompositeDimension.lean:741-758 (sgn, pc, pt, cnotFun).
DECISION RULE (fixed before the first run). Every line prints PASS/FAIL; all arithmetic exact (sympy, integers).
  A1  the landed cnot equals conjugation by CNOT (control first) on all 16 basis tables.
  A2  Ad(Z(x)I), Ad(I(x)Z), Ad(X(x)I), Ad(I(x)X), SWAP (w_{mu nu} -> w_{nu mu}) equal conjugation by their unitaries,
      and T (sign (-1)^{[mu=2]+[nu=2]}) equals complex conjugation of pauliW, on all 16 basis tables.
  B1  |<cnot, Ad(ZI), Ad(IZ), T>| = 16 (G16).   B2 SWAP not in G16; |<G16, SWAP>| printed.
  B3  |Gbig| = |<cnot, Ad(XI), Ad(ZI), Ad(IX), Ad(IZ), T>| = 64 (stage 3's order-64 group); |<Gbig, SWAP>| printed.
  C1  Z_F = {e_s} exactly: pauliW(e_s) = (I - 2 psi_s psi_s^*)/8, psi_s = (1, s1 s2, s1, -s2)/2; ipW(e_s,e_t) = d_st/4;
      ipW(e_t, T_s) = -1/2 if t = s else +1/2 (T_s the pure table of psi_s).
  C2  H1 identity, symbolic in x, y: 4 ipW(e_s, prodState x y) = 1 - x.M_s y, and 2(1 - x.M_s y) = |x - M_s y|^2 +
      (1 - |x|^2) + (1 - |y|^2) (M_s a signed permutation).
  C3  SWAP maps Z_F onto Z_F (permutation printed); every element of <G16,SWAP> and of <Gbig,SWAP> maps Z_F onto Z_F.
  C4  the action of <G16,SWAP> on the four defects: image in S4 (order printed) and kernel (order printed).
  C5  the identity component of the stabilizer: U_D = sum_s c_s psi_s psi_s^* (c = 1, i, (3+4i)/5, (5+12i)/13)
      fixes every e_s, is unitary, and is not a product u (x) v (operator Schmidt rank > 1); T fixes every psi_s
      ray (real vectors); the permutation unitaries in the psi basis for a transposition and a 4-cycle permute Z_F.
 Countercontrols (each must be REJECTED by the corresponding test, as predicted):
  CC1 SWAP moves K(E0): v = g + (2/3) f3 gives P_v in Q3 n E0* (ipW(P_v, E0) = 3/13 >= 0) with ipW(SWAP E0, P_v) =
      -5/13 < 0, so SWAP E0 is not in K(E0) = K(E0)* (stage-3 self-duality).
  CC2 SWAP moves K({F, cnot F}): SWAP(cnot F) = e_(1,-1), and T_(1,-1) in Q3 n {F, cnot F}* pairs to -1/2 with it.
  CC3 the odd local actC reflY (control partial transpose) maps phiW (PSD) to a non-PSD table (singlet value < 0),
      so the Aut(Q3) test in A2 is discriminating.
  CC4 Ad(H(x)I) does not map Z_F onto Z_F (the Z_F-permutation test is discriminating).
VERDICT 'VERDICT S1-EXOTIC ...' printed only if every check PASSES and every countercontrol is REJECTED;
otherwise 'VERDICT S1-FAILED'.
"""
import itertools
import sympy as sp

I, R = sp.I, sp.Rational
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
KR = [[sp.kronecker_product(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
results = []


def check(name, ok, note=''):
    results.append((name, bool(ok)))
    print(f"{name:5s} {'PASS' if ok else 'FAIL'}  {note}")


def pauliW(w):  # w: dict or 16-list indexed 4*mu+nu
    return sp.simplify(sum((w[4 * m + n] * KR[m][n] for m in range(4) for n in range(4)), sp.zeros(4)) / 4)


def table(rho):
    return [sp.simplify((rho * KR[m][n]).trace()) for m in range(4) for n in range(4)]


def ipW(a, b):
    return sp.nsimplify(sum(a[k] * b[k] for k in range(16)))


# ---- landed cnot (CompositeDimension.lean:741-758)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]


def sgn(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


def sp_map(f):  # build a signed permutation from f(m, n) -> (sign, m', n')
    return tuple((4 * f(m, n)[1] + f(m, n)[2], f(m, n)[0]) for m in range(4) for n in range(4))


CNOT_T = sp_map(lambda m, n: (sgn(m, n), PC[m][n], PT[m][n]))
ZI = sp_map(lambda m, n: (-1 if m in (1, 2) else 1, m, n))
IZ = sp_map(lambda m, n: (-1 if n in (1, 2) else 1, m, n))
XI = sp_map(lambda m, n: (-1 if m in (2, 3) else 1, m, n))
IX = sp_map(lambda m, n: (-1 if n in (2, 3) else 1, m, n))
TT = sp_map(lambda m, n: ((-1) ** ((m == 2) + (n == 2)), m, n))
SW = sp_map(lambda m, n: (1, n, m))
HI = sp_map(lambda m, n: ((-1 if m == 2 else 1), {0: 0, 1: 3, 2: 2, 3: 1}[m], n))
PTC = sp_map(lambda m, n: (-1 if m == 2 else 1, m, n))
ID = tuple((k, 1) for k in range(16))


def act(g, w):
    return [g[k][1] * w[g[k][0]] for k in range(16)]


def comp(g, h):  # (g o h) w = g(h(w))
    return tuple((h[g[k][0]][0], g[k][1] * h[g[k][0]][1]) for k in range(16))


def closure(gens):
    seen, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for a in frontier:
            for g in gens:
                b = comp(g, a)
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
        frontier = nxt
    return seen


E = [[1 if k == j else 0 for k in range(16)] for j in range(16)]
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
SWU = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
Hm = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
UNIT = {'cnot': (CNOT_T, CN, False), 'ZI': (ZI, sp.kronecker_product(sz, s0), False),
        'IZ': (IZ, sp.kronecker_product(s0, sz), False), 'XI': (XI, sp.kronecker_product(sx, s0), False),
        'IX': (IX, sp.kronecker_product(s0, sx), False), 'SWAP': (SW, SWU, False), 'T': (TT, sp.eye(4), True),
        'HI': (HI, sp.kronecker_product(Hm, s0), False)}


def conj_ok(g, U, anti):
    for j in range(16):
        rho = pauliW(E[j])
        lhs = pauliW(act(g, E[j]))
        rhs = U * (rho.conjugate() if anti else rho) * U.H
        if sp.simplify(lhs - rhs) != sp.zeros(4):
            return False
    return True


print('== A  generators as conjugations (exact, all 16 basis tables)')
check('A1', conj_ok(CNOT_T, CN, False), 'landed cnot = Ad(CNOT), control first')
okA2 = all(conj_ok(*UNIT[k]) for k in ('ZI', 'IZ', 'XI', 'IX', 'SWAP', 'T'))
check('A2', okA2, 'Ad(ZI), Ad(IZ), Ad(XI), Ad(IX), SWAP = Ad(SWAP), T = complex conjugation')
check('A2h', conj_ok(*UNIT['HI']), 'Ad(H(x)I) as a signed permutation (used in CC4)')

print('== B  groups (closure of signed permutations)')
G16 = closure([CNOT_T, ZI, IZ, TT])
check('B1', len(G16) == 16, f'|G16| = {len(G16)}')
G48 = closure([CNOT_T, ZI, IZ, TT, SW])
check('B2', SW not in G16 and G16 <= G48, f'SWAP not in G16; |<G16, SWAP>| = {len(G48)}')
GB = closure([CNOT_T, XI, ZI, IX, IZ, TT])
GBS = closure([CNOT_T, XI, ZI, IX, IZ, TT, SW])
check('B3', len(GB) == 64 and G16 <= GB and GB <= GBS, f'|Gbig| = {len(GB)}; |<Gbig, SWAP>| = {len(GBS)}')

print('== C  the defect orbit Z_F and its stabilizer')
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def e_s(s):
    w = [0] * 16
    w[0], w[4 * 1 + 3], w[4 * 2 + 2], w[4 * 3 + 1] = R(1, 4), R(-s[0], 4), R(-s[1], 4), R(-s[0] * s[1], 4)
    return w


def psi(s):
    return sp.Matrix([1, s[0] * s[1], s[0], -s[1]]) / 2


ZF = {tuple(e_s(s)) for s in SS}
okC1 = True
for s in SS:
    okC1 &= sp.expand(pauliW(e_s(s)) - (sp.eye(4) - 2 * psi(s) * psi(s).H) / 8) == sp.zeros(4)
    for t in SS:
        okC1 &= ipW(e_s(s), e_s(t)) == (R(1, 4) if s == t else 0)
        okC1 &= ipW(e_s(t), table(psi(s) * psi(s).H)) == (R(-1, 2) if s == t else R(1, 2))
check('C1', okC1, 'pauliW(e_s) = (I - 2 psi psi*)/8; Gram I/4; ipW(e_t, T_s) = -1/2 (t = s), +1/2 (t != s)')

x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
okC2 = True
for s in SS:
    hx, hy = [1] + list(x), [1] + list(y)
    val = sum(e_s(s)[4 * m + n] * hx[m] * hy[n] for m in range(4) for n in range(4))
    My = [s[0] * y[2], s[1] * y[1], s[0] * s[1] * y[0]]
    okC2 &= sp.expand(4 * val - (1 - sum(x[i] * My[i] for i in range(3)))) == 0
    sos = sum((x[i] - My[i]) ** 2 for i in range(3)) + (1 - sum(v ** 2 for v in x)) + (1 - sum(v ** 2 for v in y))
    okC2 &= sp.expand(8 * val - sos) == 0
check('C2', okC2, '4 ipW(e_s, prodState x y) = 1 - x.M_s y and 2(1 - x.M_s y) = SOS + (1-|x|^2) + (1-|y|^2)')

perm_sw = {SS.index(s): [tuple(e_s(t)) for t in SS].index(tuple(act(SW, e_s(s)))) if tuple(act(SW, e_s(s))) in ZF
           else None for s in SS}
okC3 = all(v is not None for v in perm_sw.values())
okC3 &= all({tuple(act(g, list(z))) for z in ZF} == ZF for g in G48)
okC3 &= all({tuple(act(g, list(z))) for z in ZF} == ZF for g in GBS)
check('C3', okC3, f'SWAP permutes Z_F (index map {perm_sw}); every element of <G16,SWAP> and <Gbig,SWAP> does')

idx = {tuple(e_s(s)): i for i, s in enumerate(SS)}
images = {tuple(idx[tuple(act(g, e_s(s)))] for s in SS) for g in G48}
kernel = [g for g in G48 if all(tuple(act(g, e_s(s))) == tuple(e_s(s)) for s in SS)]
check('C4', len(images) * len(kernel) == len(G48),
      f'<G16,SWAP> -> S4: image order {len(images)}, kernel order {len(kernel)}')

cs = [sp.Integer(1), I, (3 + 4 * I) / 5, (5 + 12 * I) / 13]
UD = sum((cs[i] * psi(s) * psi(s).H for i, s in enumerate(SS)), sp.zeros(4))
okC5 = sp.expand(UD * UD.H - sp.eye(4)) == sp.zeros(4)
for s in SS:
    T_s = table(psi(s) * psi(s).H)
    okC5 &= table(UD * pauliW(T_s) * UD.H) == T_s
realign = sp.Matrix(4, 4, lambda r, c: UD[2 * (r // 2) + (c // 2), 2 * (r % 2) + (c % 2)])
okC5 &= realign.rank() > 1
okC5 &= all(psi(s).conjugate() == psi(s) for s in SS)
for pi in ((1, 0, 2, 3), (1, 2, 3, 0)):
    UP = sum((psi(SS[pi[i]]) * psi(s).H for i, s in enumerate(SS)), sp.zeros(4))
    okC5 &= {tuple(table(UP * pauliW(list(z)) * UP.H)) for z in ZF} == ZF
check('C5', okC5, f'U_D unitary, fixes every e_s, operator Schmidt rank {realign.rank()} (not local); '
      'T fixes each psi_s; transposition and 4-cycle unitaries permute Z_F')

print('== CC countercontrols (each must be REJECTED)')
E0 = [0] * 16
E0[0], E0[4 * 1 + 3], E0[4 * 2 + 2] = 1, 1, -1
g = sp.Matrix([1, -1, -1, -1]) / 2
f3 = sp.Matrix([1, -1, 1, 1]) / 2
v = g + R(2, 3) * f3
Pv = table(v * v.H / (v.H * v)[0])
a1, a2 = ipW(Pv, E0), ipW(Pv, act(SW, E0))
rej1 = a1 >= 0 and a2 < 0
print(f"CC1   {'REJECTED' if rej1 else 'NOT REJECTED'}  ipW(P_v, E0) = {a1}, ipW(P_v, SWAP E0) = {a2}")
cnotF = act(CNOT_T, e_s((1, 1)))
img = act(SW, cnotF)
Tm = table(psi((1, -1)) * psi((1, -1)).H)
rej2 = (tuple(cnotF) == tuple(e_s((-1, -1))) and tuple(img) == tuple(e_s((1, -1))) and
        ipW(Tm, e_s((1, 1))) >= 0 and ipW(Tm, e_s((-1, -1))) >= 0 and ipW(Tm, img) < 0)
print(f"CC2   {'REJECTED' if rej2 else 'NOT REJECTED'}  SWAP(cnot F) = e_(1,-1); ipW(T_(1,-1), e_(1,-1)) = "
      f"{ipW(Tm, img)}")
phiW = [1 if (k // 4 == k % 4 and k // 4 != 2) else (-1 if k == 10 else 0) for k in range(16)]
sing = sp.Matrix([0, 1, -1, 0])
vb = (sing.H * pauliW(phiW) * sing)[0]
vp = (sing.H * pauliW(act(PTC, phiW)) * sing)[0]
rej3 = vb >= 0 and vp < 0
print(f"CC3   {'REJECTED' if rej3 else 'NOT REJECTED'}  singlet value on phiW = {vb}, on its control "
      f"partial transpose = {vp}")
rej4 = {tuple(act(HI, list(z))) for z in ZF} != ZF
print(f"CC4   {'REJECTED' if rej4 else 'NOT REJECTED'}  Ad(H(x)I) image of Z_F differs from Z_F")

allpass = all(ok for _, ok in results) and rej1 and rej2 and rej3 and rej4
print(f"SUMMARY checks {sum(ok for _, ok in results)}/{len(results)} PASS; countercontrols rejected "
      f"{sum([rej1, rej2, rej3, rej4])}/4")
if allpass:
    print(f"VERDICT S1-EXOTIC K(Z_F) invariant under <G16,SWAP> (order {len(G48)}) and <Gbig,SWAP> "
          f"(order {len(GBS)})")
else:
    print('VERDICT S1-FAILED')
