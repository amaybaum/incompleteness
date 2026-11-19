"""Probe P8 (QPHEN Phase 1 r4, independent reviewer). Imports no earlier probe (P1-P7).

Exact checks on generic mathematical objects only (no OI mechanism):
  (1) Leggett-Garg target-mode configurations of QX-4 A4.1(c) / SHARED Q4-P4, Q4-D6, computed two independent ways
      (Schroedinger picture with Lueders projectors, and the Heisenberg formula C_ij = Re<psi|Q_i Q_j|psi>), under the
      stated tensor order carrier (x) mediator, and the other placement / other tensor reading for contrast.
  (2) Q4-D5: C12 = cos 2 theta.
  (3) Q4-D4: measure-and-reprepare Kraus instruments are trace preserving; K3 = 3 and 6w - 3.
  (4) Q4-D7: maximally mixed state, Lueders X read at t2, G = I.
  (5) Q4-D2 and Q4-D1: the F_2 witness G (symplectic check), sharp / environment mediators, mixture 3/4, NSIT at t2.
  (6) Q4-D3: copy coupling is linear but not symplectic; exhaustive count of affine-symplectic and of affine maps on
      (c, x), (m, m') that act as the identity on the c = 0 branch and change a meter slot on the c = 1 branch.
  (7) Q4-P3: integrality and K3 <= 1 for two-qubit Clifford G, all 60 two-qubit pure stabilizer states (numerical,
      with an integrality tolerance check; numerical evidence only).
  (8) Q3-D1 membership of L; QX-3 counts (6 global-weight affine, 48 affine routers, 8 global routers, 64 field-only).
      Q3-P11's law.
  (9) Q6-D1: a one-tick op_A . phi . op_B model: (D), (L), single-graph (R), (MI) hold; (L') fails; S = 4.
 (10) Q6-D2 / Q6-D3: GHZ-2 values, local maximum; GHZ-1 X/Z strings with nonzero expectation.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

ok_all = []
def check(label, cond):
    ok_all.append(bool(cond))
    print(('PASS ' if cond else 'FAIL ') + label)

# ---------------------------------------------------------------- (1) LG configurations, exact
th, b = sp.symbols('theta b', real=True)
I2 = sp.eye(2); Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
Zm = sp.diag(1, -1); Xm = sp.Matrix([[0, 1], [1, 0]])
def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out
def ket(bits):  # computational basis ket, first bit = first tensor factor
    v = sp.zeros(2 ** len(bits), 1); v[int(''.join(map(str, bits)), 2)] = 1; return v
def perm_unitary(f, n):  # unitary of a classical bijection f on n bits (first bit = first factor)
    U = sp.zeros(2 ** n, 2 ** n)
    for bits in itertools.product((0, 1), repeat=n):
        U += ket(f(bits)) * ket(bits).T
    return U
# order "carrier (x) mediator": bits = (c, m). CNOT control m, target c.
CNOT_m_c = perm_unitary(lambda t: ((t[0] + t[1]) % 2, t[1]), 2)
SWAP = perm_unitary(lambda t: (t[1], t[0]), 2)
def lueders_C(rho, G, Zc, i, j):
    P = [(sp.eye(rho.shape[0]) + Zc) / 2, (sp.eye(rho.shape[0]) - Zc) / 2]
    r = rho
    for _ in range(i - 1):
        r = G * r * G.H
    tot = 0
    for a, Pa in zip((1, -1), P):
        r1 = Pa * r * Pa
        for _ in range(j - i):
            r1 = G * r1 * G.H
        for bb, Pb in zip((1, -1), P):
            tot += a * bb * (Pb * r1).trace()
    return sp.simplify(sp.expand(sp.simplify(tot)))
def heis_C(psi, G, Zc, i, j):
    Gi = G ** (i - 1); Gj = G ** (j - 1)
    Qi = Gi.H * Zc * Gi; Qj = Gj.H * Zc * Gj
    v = (psi.H * Qi * Qj * psi)[0]
    return sp.simplify(sp.re(sp.expand(sp.simplify(v))))
def K3(psi, G, Zc):
    rho = psi * psi.H
    cs = [lueders_C(rho, G, Zc, 1, 2), lueders_C(rho, G, Zc, 2, 3), lueders_C(rho, G, Zc, 1, 3)]
    hs = [heis_C(psi, G, Zc, 1, 2), heis_C(psi, G, Zc, 2, 3), heis_C(psi, G, Zc, 1, 3)]
    agree = all(sp.simplify(sp.trigsimp(c - h)) == 0 for c, h in zip(cs, hs))
    return [sp.trigsimp(c) for c in cs], sp.simplify(sp.trigsimp(cs[0] + cs[1] - cs[2])), agree
bl = lambda beta: sp.Matrix([sp.cos(beta / 2), sp.sin(beta / 2)])   # Bloch (sin beta, 0, cos beta)
plus = sp.Matrix([1, 1]) / sp.sqrt(2); zero = sp.Matrix([1, 0])
Zc = kron(Zm, I2)                                                   # carrier is the first factor
target = sp.cos(b) + sp.sin(b)
G1 = kron(I2, Hd) * CNOT_m_c
G2 = kron(I2, Hd) * SWAP * CNOT_m_c
for name, G, psi, want in [
        ('(1a) G1=(I(x)H)CNOT_{m->c}, carrier |+>, mediator (sin b,0,cos b)', G1, kron(plus, bl(b)), target),
        ('(1b) G2=(I(x)H)SWAP CNOT_{m->c}, carrier (sin b,0,cos b), mediator |0>', G2, kron(bl(b), zero), target),
        ('(1c) H on carrier: (H(x)I)CNOT_{m->c}', kron(Hd, I2) * CNOT_m_c, kron(plus, bl(b)), -sp.cos(b)),
        ('(1d) H on carrier: (H(x)I)SWAP CNOT_{m->c}', kron(Hd, I2) * SWAP * CNOT_m_c, kron(bl(b), zero), 0)]:
    cs, k, agree = K3(psi, G, Zc)
    print('    ', name, ': (C12,C23,C13) =', tuple(cs), ' K3 =', k)
    check(name + ': Lueders = Heisenberg', agree)
    check(name + ': K3 as stated', sp.simplify(sp.trigsimp(k - want)) == 0)
    if want is target:
        check(name + ': K3(pi/4) = sqrt2', sp.simplify(k.subs(b, sp.pi / 4) - sp.sqrt(2)) == 0)
        check(name + ': K3 at (4/5,3/5) = 7/5',
              sp.simplify(k.subs(b, sp.atan2(sp.Rational(3, 5), sp.Rational(4, 5))) - sp.Rational(7, 5)) == 0)
# Unitarity and Clifford property of G1, G2 (Pauli conjugation; Hermitian images so only +-1 phases)
paul = [I2, Xm, sp.Matrix([[0, -sp.I], [sp.I, 0]]), Zm]
two = [kron(p, q) for p in paul for q in paul]
def clifford(U):
    for Pm in two[1:]:
        V = sp.simplify(U * Pm * U.H)
        if not any(sp.simplify(V - s * Q) == sp.zeros(4, 4) for Q in two for s in (1, -1)):
            return False
    return True
check('(1) G1, G2 unitary', all(sp.simplify(G * G.H) == sp.eye(4) for G in (G1, G2)))
check('(1) G1, G2 Clifford', clifford(G1) and clifford(G2))
# The other tensor reading of the same symbols (mediator (x) carrier, H on the second factor = carrier)
CNOT_mc_rev = perm_unitary(lambda t: (t[0], (t[0] + t[1]) % 2), 2)   # bits (m, c): control m, target c
Zc_rev = kron(I2, Zm)
_, k_rev, _ = K3(kron(bl(b), plus), kron(I2, Hd) * CNOT_mc_rev, Zc_rev)
check('(1e) mediator(x)carrier reading gives K3 = -cos b (so the stated order is needed)',
      sp.simplify(k_rev + sp.cos(b)) == 0)
# The stated configuration with non-stabilizer mediator: is the mediator state non-stabilizer at b = pi/4?  (yes:
# Bloch (1/sqrt2, 0, 1/sqrt2) is not a Pauli axis); at b with (cos, sin) = (4/5, 3/5) likewise.

# ---------------------------------------------------------------- (2) Q4-D5
anc = sp.Matrix([sp.cos(th), sp.sin(th)])
psi = kron(zero, anc)                    # carrier |0>, ancilla
c12 = lueders_C(psi * psi.H, CNOT_m_c, Zc, 1, 2)
check('(2) Q4-D5: CNOT ancilla->carrier gives C12 = cos 2theta', sp.simplify(sp.trigsimp(c12 - sp.cos(2 * th))) == 0)

# ---------------------------------------------------------------- (3) Q4-D4 instruments
w = sp.symbols('w', nonnegative=True)  # instrument entries are real: use transposes below
k0 = sp.Matrix([[1, 0], [0, 0]]); k1 = sp.Matrix([[0, 0], [0, 1]])
up = sp.Matrix([[0, 0], [1, 0]]); dn = sp.Matrix([[0, 1], [0, 0]])          # |1><0|, |0><1|
inst = {+1: [sp.sqrt(w) * up, sp.sqrt(1 - w) * k0], -1: [sp.sqrt(w) * dn, sp.sqrt(1 - w) * k1]}
tp = sp.simplify(sum((K.T * K for ks in inst.values() for K in ks), sp.zeros(2, 2)))
check('(3) Q4-D4: weight-w instrument trace preserving', tp == sp.eye(2))
povm_ok = all(sp.simplify(sum((K.T * K for K in inst[o]), sp.zeros(2, 2)) - (k0 if o == 1 else k1)) == sp.zeros(2, 2)
              for o in (1, -1))
check('(3) Q4-D4: outcome effects are the Z projectors (dichotomic Z read)', povm_ok)
def instr_C(rho, G, i, j):
    r = rho
    for _ in range(i - 1):
        r = G * r * G.H
    tot = 0
    for a in (1, -1):
        r1 = sum((K * r * K.T for K in inst[a]), sp.zeros(2, 2))
        for _ in range(j - i):
            r1 = G * r1 * G.T
        for bb in (1, -1):
            tot += a * bb * sum((K * r1 * K.T for K in inst[bb]), sp.zeros(2, 2)).trace()
    return sp.simplify(tot)
r0 = zero * zero.T
kk = sp.simplify(instr_C(r0, Xm, 1, 2) + instr_C(r0, Xm, 2, 3) - instr_C(r0, Xm, 1, 3))
check('(3) Q4-D4: K3 = 6w - 3 (so 3 at w = 1 and 2 at w = 5/6)', sp.simplify(kk - (6 * w - 3)) == 0)

# ---------------------------------------------------------------- (4) Q4-D7
rm = sp.eye(2) / 2
PX = [(sp.eye(2) + Xm) / 2, (sp.eye(2) - Xm) / 2]
with_read = sum((P * rm * P for P in PX), sp.zeros(2, 2))
check('(4) Q4-D7: P(z3=+1) = 1/2 with and without a Lueders X read (G = I)',
      (k0 * with_read).trace() == sp.Rational(1, 2) and (k0 * rm).trace() == sp.Rational(1, 2))
check('(4) Q4-D7: X does not commute with Z', Xm * Zm != Zm * Xm)

# ---------------------------------------------------------------- (5) F_2 Leggett-Garg witness (Q4-D2, Q4-D1)
# variables (z, x, v, w); symplectic pairs (z, x), (v, w); omega(u, u') = z x' + x z' + v w' + w v'
OM = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
def is_symp(M):
    return np.array_equal((M.T @ OM @ M) % 2, OM)
Wt = np.array([[1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0]])   # rows: z', x', v', w'
check('(5) Q4-D2: witness invertible over F_2', round(abs(np.linalg.det(Wt))) % 2 == 1)
check('(5) Q4-D2: witness symplectic for (z,x),(v,w)', is_symp(Wt))
def lg_affine(G, supply):
    """supply: list of (prob, (z,x,v,w)) exact; Z read records z and adds a uniform kick to x."""
    def run(state, reads):
        # reads: set of times among {1,2,3}; returns list of (prob, {t: z_t})
        outs = [(Fr(1), tuple(state), {})]
        for t in (1, 2, 3):
            new = []
            for p, s, rec in outs:
                if t in reads:
                    rec2 = dict(rec); rec2[t] = s[0]
                    for k in (0, 1):
                        s2 = (s[0], (s[1] + k) % 2, s[2], s[3])
                        new.append((p / 2, s2, rec2))
                else:
                    new.append((p, s, rec))
            outs = new
            if t < 3:
                outs = [(p, tuple(int(v) for v in (G @ np.array(s)) % 2), r) for p, s, r in outs]
        return outs
    def C(i, j):
        tot = Fr(0)
        for q, st in supply:
            for p, _, rec in run(st, {i, j}):
                tot += q * p * (1 if rec[i] == rec[j] else -1)
        return tot
    def Pz3(read2):
        tot = Fr(0)
        for q, st in supply:
            for p, _, rec in run(st, {1, 2, 3} if read2 else {1, 3}):
                tot += q * p * (1 if rec[3] == 0 else 0)
        return tot
    return C(1, 2), C(2, 3), C(1, 3), Pz3(True), Pz3(False)
carrier_Xplus = [(Fr(1, 2), (z, 0)) for z in (0, 1)]
def supply(carrier, med):
    return [(pc * pm, (c[0], c[1], m[0], m[1])) for pc, c in carrier for pm, m in med]
sharp = [(Fr(1), (0, 0))]
env = [(Fr(1, 4), (v, ww)) for v in (0, 1) for ww in (0, 1)]
mix = [(Fr(3, 4) * p, m) for p, m in sharp] + [(Fr(1, 4) * p, m) for p, m in env]
res = {}
for nm, med in (('sharp', sharp), ('environment', env), ('mixture 3/4', mix)):
    c12, c23, c13, pz_w, pz_wo = lg_affine(Wt, supply(carrier_Xplus, med))
    res[nm] = (c12, c23, c13, c12 + c23 - c13, pz_w, pz_wo)
    print('     (5)', nm, ': C12,C23,C13 =', c12, c23, c13, ' K3 =', c12 + c23 - c13,
          ' P(z3=0) with/without t2 read =', pz_w, pz_wo)
check('(5) Q4-D2: sharp mediator K3 = 2', res['sharp'][3] == 2)
check('(5) Q4-P7: environment mediator K3 = 0', res['environment'][3] == 0)
check('(5) Q4-D1: mixture K3 = 3/2', res['mixture 3/4'][3] == Fr(3, 2))
check('(5) Q4-D1: t2 read leaves P(z3) unchanged in each branch and in the mixture',
      all(r[4] == r[5] for r in res.values()))
# Stronger than the marginal: z3 is independent of the t2 kick pointwise (the kick enters only x2, and row z' of
# G^1 has no x component), checked on G itself:
check('(5) Q4-D1: z-row of G has zero x coefficient (t2 kick never enters z3)', Wt[0, 1] == 0)

# ---------------------------------------------------------------- (6) Q4-D3 and its affine-symplectic form
# coordinates (c, x, m, m'); pairs (c, x), (m, m')
def all_invertible(n):
    for bits in itertools.product((0, 1), repeat=n * n):
        M = np.array(bits).reshape(n, n)
        if round(abs(np.linalg.det(M))) % 2 == 1:
            yield M
copy = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]])
check('(6) Q4-D3: copy coupling m <- m + c is linear and invertible', round(abs(np.linalg.det(copy))) % 2 == 1)
check('(6) Q4-D3: copy coupling is NOT symplectic', not is_symp(copy))
recip = np.array([[1, 0, 0, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 0, 0, 1]])   # m <- m + c, x <- x + m'
check('(6) R4.9: reciprocal coupling (copy + x <- x + m\') is symplectic', is_symp(recip))
n_aff_only = n_sym_only = n_sym = 0
pts = list(itertools.product((0, 1), repeat=4))
for M in all_invertible(4):
    symp = is_symp(M)
    n_sym += symp
    for t in itertools.product((0, 1), repeat=4):
        t = np.array(t)
        img = {p: tuple(int(v) for v in (M @ np.array(p) + t) % 2) for p in pts}
        id_on_c0 = all(img[p] == p for p in pts if p[0] == 0)
        meter_changes_on_c1 = any((img[p][2], img[p][3]) != (p[2], p[3]) for p in pts if p[0] == 1)
        if id_on_c0 and meter_changes_on_c1:
            n_aff_only += 1
            n_sym_only += symp
print('     (6) |Sp(4,F2)| =', n_sym, '; affine bijections, identity on c=0, meter changes on c=1:', n_aff_only,
      '; of which affine-symplectic:', n_sym_only)
check('(6) |Sp(4,F2)| = 720', n_sym == 720)
check('(6) affine maps acting only when occupied exist (Q4-D3 holds for affine maps)', n_aff_only > 0)
check('(6) no affine-SYMPLECTIC map acts only when occupied and changes the meter', n_sym_only == 0)

# ---------------------------------------------------------------- (7) Q4-P3, numerical evidence
Hn = np.array([[1, 1], [1, -1]]) / np.sqrt(2); Sn = np.diag([1, 1j]); In = np.eye(2)
CZn = np.diag([1, 1, 1, -1]).astype(complex)
gens = [np.kron(Hn, In), np.kron(In, Hn), np.kron(Sn, In), np.kron(In, Sn), CZn]
def canon(U):
    k = np.flatnonzero(np.abs(U.ravel()) > 1e-9)[0]
    V = U * (abs(U.ravel()[k]) / U.ravel()[k])
    return tuple(np.round(V.ravel(), 6))
group = {canon(np.eye(4, dtype=complex)): np.eye(4, dtype=complex)}
frontier = list(group.values())
while frontier:
    nf = []
    for U in frontier:
        for g in gens:
            V = g @ U; key = canon(V)
            if key not in group:
                group[key] = V; nf.append(V)
    frontier = nf
cliffs = list(group.values())
states = {}
for U in cliffs:
    v = U[:, 0]; k = np.flatnonzero(np.abs(v) > 1e-9)[0]; v = v * abs(v[k]) / v[k]
    states[tuple(np.round(v, 6))] = v
stab = list(states.values())
Zcn = np.kron(np.diag([1, -1]), In)
maxK, nonint = -9, 0
for G in cliffs:
    G2_ = G @ G
    A12 = Zcn @ G.conj().T @ Zcn @ G
    A13 = Zcn @ G2_.conj().T @ Zcn @ G2_
    for s in stab:
        g1 = G @ s
        c12 = np.real(s.conj() @ A12 @ s); c13 = np.real(s.conj() @ A13 @ s); c23 = np.real(g1.conj() @ A12 @ g1)
        for c in (c12, c23, c13):
            if abs(c - round(c)) > 1e-9:
                nonint += 1
        maxK = max(maxK, c12 + c23 - c13)
print('     (7) |C_2 / U(1)| =', len(cliffs), '; pure stabilizer states =', len(stab), '; max K3 =', round(maxK, 9),
      '; non-integer correlators =', nonint)
check('(7) Q4-P3 (numerical): 11,520 Cliffords x 60 states: integer correlators and K3 <= 1',
      len(cliffs) == 11520 and len(stab) == 60 and nonint == 0 and maxK <= 1 + 1e-9)

# ---------------------------------------------------------------- (8) QX-3
def Lmap(s, c1, c2):
    return (s, (s + c1) % 2, (s + c2) % 2)
ready = [(s, 1, 0) for s in (0, 1)]
imgs = [Lmap(*p) for p in ready]
check('(8) Q3-D1: L bijective on F_2^3', len({Lmap(*p) for p in itertools.product((0, 1), repeat=3)}) == 8)
check('(8) Q3-D1: ready support -> (0,1,0), (1,0,1)', imgs == [(0, 1, 0), (1, 0, 1)])
check('(8) Q3-D1: field weight 1 after, own-cell clicks exclusive, alpha = 0',
      all(i[1] + i[2] == 1 for i in imgs))
check('(8) Q3-D1: total weight conserved on ready support', all(sum(p) == sum(Lmap(*p)) for p in ready))
pts3 = list(itertools.product((0, 1), repeat=3))
affine3 = set()
for bits in itertools.product((0, 1), repeat=12):
    M = np.array(bits[:9]).reshape(3, 3); t = np.array(bits[9:])
    img = tuple(tuple(int(v) for v in (M @ np.array(p) + t) % 2) for p in pts3)
    if len(set(img)) == 8:
        affine3.add(img)
def routes(img):  # routes on the ready support: s=0 and s=1 send the excitation to different single field cells
    f = dict(zip(pts3, img))
    a, bb = f[(0, 1, 0)], f[(1, 1, 0)]
    return a[1] + a[2] == 1 and bb[1] + bb[2] == 1 and a[1:] != bb[1:]
wt = lambda p: sum(p)
fwt = lambda p: p[1] + p[2]
n_glob_aff = sum(all(wt(f) == wt(p) for p, f in zip(pts3, img)) for img in affine3)
n_route_aff = sum(routes(img) and all(wt(dict(zip(pts3, img))[p]) == wt(p) for p in [(0, 1, 0), (1, 1, 0)])
                  for img in affine3)
allbij = [tuple(pm) for pm in itertools.permutations(pts3)]
glob_routers = [img for img in allbij if routes(img) and all(wt(f) == wt(p) for p, f in zip(pts3, img))]
field_routers = [img for img in allbij if routes(img) and all(fwt(f) == fwt(p) for p, f in zip(pts3, img))]
print('     (8) affine bijections:', len(affine3), '; global-weight affine:', n_glob_aff, '; affine routers:',
      n_route_aff, '; global-weight routers:', len(glob_routers), '(affine:',
      sum(r in affine3 for r in glob_routers), '); field-weight routers:', len(field_routers), '(affine:',
      sum(r in affine3 for r in field_routers), ')')
check('(8) 6 / 48 / 8 (0 affine) / 64 (0 affine)', (n_glob_aff, n_route_aff, len(glob_routers),
      sum(r in affine3 for r in glob_routers), len(field_routers), sum(r in affine3 for r in field_routers))
      == (6, 48, 8, 0, 64, 0))
PA, PB, PAB = Fr(9 + 151, 256), Fr(9 + 71, 256), Fr(9, 256)
check('(8) Q3-P11: cells 9,151,71,25 valid law; P_A=5/8, P_B=5/16, alpha=9/50',
      9 + 151 + 71 + 25 == 256 and PA == Fr(5, 8) and PB == Fr(5, 16) and PAB / (PA * PB) == Fr(9, 50))

# ---------------------------------------------------------------- (9) Q6-D1
# sites: a1, a2 (A), b1, b2 (B); x0: a1 = b1 = lam, a2 = b2 = 0
A, B = {0, 1}, {2, 3}; RA, RB = {0}, {2}
def tick(xv, xs, ys):
    a1, a2, b1, b2 = xv
    b2 = (b2 + ys) % 2            # op_B: reads/writes B only
    a2 = (a2 + b2) % 2            # phi: copies a B-site onto a site outside B
    a1 = (a1 + xs * a2) % 2       # op_A: reads/writes A only
    return (a1, a2, b1, b2)
cfgs = list(itertools.product((0, 1), repeat=4))
bij = all(len({tick(c, xs, ys) for c in cfgs}) == 16 for xs in (0, 1) for ys in (0, 1))
edges = set()
for xs, ys in itertools.product((0, 1), repeat=2):
    for c in cfgs:
        for jj in range(4):
            c2 = list(c); c2[jj] ^= 1
            o1, o2 = tick(c, xs, ys), tick(tuple(c2), xs, ys)
            for ii in range(4):
                if o1[ii] != o2[ii] and ii != jj:
                    edges.add(frozenset((ii, jj)))
def dist(S, T):
    if S & T:
        return 0
    seen, fr, d = set(S), set(S), 0
    while fr:
        d += 1
        fr = {k for e in edges for k in e if (e & fr) and k not in seen}
        seen |= fr
        if fr & T:
            return d
    return float('inf')
Lprime = all(tick(c, xs, 0)[i] == tick(c, xs, 1)[i] for c in cfgs for xs in (0, 1) for i in range(4) if i not in B) \
    and all(tick(c, 0, ys)[i] == tick(c, 1, ys)[i] for c in cfgs for ys in (0, 1) for i in range(4) if i not in A)
E = {}
for xs, ys in itertools.product((0, 1), repeat=2):
    tot = Fr(0)
    for lam in (0, 1):
        o = tick((lam, 0, lam, 0), xs, ys)
        tot += Fr(1, 2) * (-1) ** (o[0] + o[2])
    E[(xs, ys)] = tot
S = E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]
print('     (9) edges:', sorted(tuple(sorted(e)) for e in edges), '; d_G(B,R_A) =', dist(B, RA),
      '; d_G(A,R_B) =', dist(A, RB), '; S =', S)
check('(9) Q6-D1: (D) bijective for every setting', bij)
check('(9) Q6-D1: single-graph (R): d_G(B,R_A) = 1 > 0 and d_G(A,R_B) > 0', dist(B, RA) == 1 and dist(A, RB) > 0)
check('(9) Q6-D1: (L\') fails', not Lprime)
check('(9) Q6-D1: S = 4 with lam uniform and setting independent (MI)', S == 4)

# ---------------------------------------------------------------- (10) GHZ
Xn = np.array([[0, 1], [1, 0]]); Zn = np.diag([1, -1]); Yn = np.array([[0, -1j], [1j, 0]])
def op(s):
    m = {'I': In, 'X': Xn, 'Y': Yn, 'Z': Zn}
    out = np.array([[1]])
    for ch in s:
        out = np.kron(out, m[ch])
    return out
plus3 = np.ones(8) / np.sqrt(8)
CZ = lambda i, j: np.diag([(-1) ** (((k >> (2 - i)) & 1) * ((k >> (2 - j)) & 1)) for k in range(8)])
tri = CZ(0, 1) @ CZ(0, 2) @ CZ(1, 2) @ plus3
ev = lambda s, v: np.real(v.conj() @ op(s) @ v)
vals = [ev(s, tri) for s in ('XZZ', 'ZXZ', 'ZZX', 'XXX')]
loc = max(xa[0] * za[1] * za[2] + za[0] * xa[1] * za[2] + za[0] * za[1] * xa[2] - xa[0] * xa[1] * xa[2]
          for xa in itertools.product((1, -1), repeat=3) for za in itertools.product((1, -1), repeat=3))
check('(10) Q6-D2: triangle state gives +1,+1,+1,-1 (value 4); local max 2',
      np.allclose(vals, [1, 1, 1, -1]) and loc == 2)
ghz = np.zeros(8); ghz[0] = ghz[7] = 1 / np.sqrt(2)
nz = [s for s in (''.join(t) for t in itertools.product('IXZ', repeat=3)) if s != 'III' and abs(ev(s, ghz)) > 1e-9]
check('(10) Q6-D3: GHZ-1 nonzero X/Z strings are XXX, ZZI, IZZ, ZIZ, all +1',
      sorted(nz) == sorted(['XXX', 'ZZI', 'IZZ', 'ZIZ']) and all(abs(ev(s, ghz) - 1) < 1e-9 for s in nz))

print('ALL PASS' if all(ok_all) else 'SOME FAILED', '(%d checks)' % len(ok_all))
