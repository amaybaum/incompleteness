#!/usr/bin/env python3
"""Coordinator's independent check of thread C5 (stage 5, BRIDGE-COUNTER).  Exact (sympy) unless a line says FLOAT.
Written from C5's RESULT claims, not from its code; different representations throughout (Pauli-string commutators
with discrete closure by exact conjugation; projective orbits by BFS on canonical rays with sympy Gaussian rationals;
the torus minimum of |det|^2 taken EXACTLY as the smallest eigenvalue of C5's 2x2 form, rather than bounded).
Run: python3 -I -B indep_checkC.py  from pt/audit/C5/ (reads nothing).
DECISION RULE (fixed before the first run): every line prints CONFIRMED or MISMATCH; countercontrols (ids ending 'c')
are CONFIRMED exactly when the tested property fails on them; INDEP-C-FIXED iff every line is CONFIRMED.

Claims checked (C5 RESULT section -> check id):
 T  transcription of the native data: U_J = (I - i(X+Y+Z))/2 realizes cyc3; J-conjugate of ball3Drive's flow (about z)
    is the flow about x, whose half-turn is nflip while rot3(pi) = diag(-1,-1,1) != nflip (T1); CNOT = I x P+ + Z x P-
    = I - 2|1-><1-| (T2); |G16| = 16, |<G16, SWAP>| = 48 projectively, with T antiunitary (T3).
 L  census Lie closures with discrete closure (R2 method), levels (i) and (ii): {flow}@C 2/2; {flow}@T 1/1; both 3/3;
    {flow,NOT}@C,@T 2/1; {J},{NOT,J} 0; {flow,J}@C 6/6; {flow,J}@T 6/6; flow@C+J@T 15; flow@T+J@C 1; ball3Drive z-flow
    @C/@T/both 1/2/3; {z-flow,J}@C,@T 6 (L1..L12).
 U  UNIQUE criterion: L({flow,J}@C) contains su(2) x |p><p| for p an X-eigenstate; L({flow,J}@T) contains |0><0| x su(2);
    the flow-only nodes contain neither (U1, U2, U1c); exact reachability witnesses: a product state carried to
    psi0 = phi0/4 and to psi_a = (15,-1,7,7)/18 by an element U+ x P+ + U- x P- of the connected group (U3, U4).
 O  projective orbits of the ray of phi0 = (1,2,3i,-1+i) under <U_J x I, CNOT> (768) and <I x U_J, CNOT> (384); the
    NOT adds nothing to the orbit (O1, O2, O3); d_low over these orbits = 5/256 (O4).
 S  torus seeds: for {flow}@C the exact minimum over beta and over the D-orbit of |det Psi(e^{-i beta XX} chi)|^2/n^2
    equals the smallest eigenvalue of C5's 2x2 form; C5's bound det Q/tr Q is <= it; the bound at the minimizing orbit
    element gives d_low = 1/2304 and alpha = 499783/500000 is admissible (r^2 >= 1 - 4 d_low, r < 1) (S1, S2, S3);
    for z@T (N = Z x Z) d_low = 1/8704 (S4); stage-4 seeds: c = 1/alpha-type values 4609/4608, 17409/17408 lie in the
    exact windows (S5); S6 FLOAT sanity: a scan over beta never goes below the exact minimum; S1c: a reachable Bell
    state gives minimum 0.
 K  K(Z_F) facts: every G16 generator, SWAP, X x I and I x X permute the defect set (K1); theta: 4 pairVal = a0 b0 +
    a^T M_s b with M_s a signed permutation (orthogonal) (K2); kappa: U(w) = I + (w-1)|1-><1-|, U(-1) = CNOT, the
    circles C1, C2 are mapped into C1 u C2 by U(w'), CNOT, Z x I, I x Z, T; every point maximally entangled; the
    Bell-type defect of C1(w=1) = (1,1,1,-1)/2 is z_(-1,-1) (K3); kappa-cc: at w = -i some defect leaves K(Z_F) with
    an exact pure witness, pairing -1/2 (K4); zeta: D(w) fixes x = T(psi_(1,-1) + psi_(-1,1)) while J D(-1) J^-1
    moves it, J a permutation unitary in the defect basis (K5); iota-cc: (5,-5,-1,-1) in Q3 n E0*, pairings 3/13 with
    E0 and -5/13 with SWAP E0 (K6); eta-cc: <E0, actT nflip E0> = -1 and <E0, actC nflip E0> = +1 (K7); FORM-J:
    (U_J x I) CNOT (U_J x I)^dag = I x P+ + X x P- and X, Z have no common eigenvector (K8); CL1: F = z_(-1,-1) pairs
    >= 0 with every product and every cnot-image of a product (symbolic), F not in Q3, F pairs -1/2 with its own
    state (K9); LAMBDA-tw: reflY R reflY is a rotation for a rotation R (K10); THETA-cc: chainW = cnot idW pairs
    -1/2 with the sharp effects of -e1, -e3 while idW is in maxCone on a grid of sharp effects (K11).
"""
import itertools, random
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, symbols, kronecker_product as kron
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]
KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
STR = [(a, b) for a in range(4) for b in range(4)]
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M): return Matrix(4, 4, lambda m, n: sp.nsimplify(simplify(expand((KR[(m, n)] * M).trace()))))
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def Ad(U, w): return tab(U * pauliW(w) * U.H)
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
SWAP = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
UJ = (I2 - I * (SX + SY + SZ)) / 2
P0 = Matrix([[1, 0], [0, 0]]); P1 = Matrix([[0, 0], [0, 1]]); Pp = (I2 + SX) / 2; Pm = (I2 - SX) / 2
def rotOf(U): return Matrix(3, 3, lambda i, j: sp.nsimplify(simplify(expand((SG[i + 1] * U * SG[j + 1] * U.H).trace() / 2))))
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T
def prodState(x, y): return Matrix([1] + list(x)) * Matrix([1] + list(y)).T
NF = Matrix.diag(1, -1, -1); CYC = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
def Rx(t): return Matrix([[1, 0, 0], [0, sp.cos(t), -sp.sin(t)], [0, sp.sin(t), sp.cos(t)]])
def Rz(t): return Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])

print("== T  transcription")
t = symbols('t', real=True)
okT1 = rotOf(UJ) == CYC and simplify(CYC * Rz(t) * CYC.T - Rx(t)) == zeros(3, 3) and Rx(sp.pi) == NF and Rz(sp.pi) == Matrix.diag(-1, -1, 1) and Rz(sp.pi) != NF
rec('T1', okT1, 'U_J realizes cyc3; cyc3 . rot3(t) . cyc3^-1 = R_x(t); R_x(pi) = nflip; rot3(pi) = diag(-1,-1,1) != nflip')
ket1m = kron(Matrix([0, 1]), Matrix([1, -1]) / sqrt(2))
rec('T2', simplify(CNOT - (kron(I2, Pp) + kron(SZ, Pm))) == zeros(4, 4) and simplify(CNOT - (eye(4) - 2 * ket1m * ket1m.H)) == zeros(4, 4), 'CNOT = I x P+ + Z x P- = I - 2|1-><1-|')
# projective group orders with an antiunitary generator: elements (M, flag); compose (M1,f1)(M2,f2) = (M1 * conj^{f1}(M2), f1 xor f2)
def canon(M):
    M = M.applyfunc(lambda z: sp.nsimplify(simplify(z)))
    for i in range(4):
        for j in range(4):
            if M[i, j] != 0:
                return sp.ImmutableMatrix((M / M[i, j]).applyfunc(lambda z: sp.nsimplify(simplify(z))))
def gcompose(a, b):
    M1, f1 = a; M2, f2 = b
    M2c = M2.conjugate() if f1 else M2
    return (canon(M1 * M2c), f1 ^ f2)
def group_order(gens):
    grp = {gcompose((eye(4), False), g) for g in gens}; frontier = list(grp)
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                for r in (gcompose(g, h), gcompose(h, g)):
                    if r not in grp: grp.add(r); nxt.append(r)
        frontier = nxt
    return len(grp)
Tgen = (eye(4), True)
G16_gens = [(canon(CNOT), False), (canon(kron(SZ, I2)), False), (canon(kron(I2, SZ)), False), Tgen]
n16 = group_order(G16_gens); n48 = group_order(G16_gens + [(canon(SWAP), False)])
rec('T3', n16 == 16 and n48 == 48, 'projective orders: |G16| = 16, |<G16, SWAP>| = 48', 'orders %d, %d' % (n16, n48))

print("== L  census Lie closures (Pauli coordinates; discrete closure under exact conjugation)")
def pmul1(a, b):
    if a == 0: return (1, b)
    if b == 0: return (1, a)
    if a == b: return (1, 0)
    c = ({1, 2, 3} - {a, b}).pop()
    return (I if (a, b) in [(1, 2), (2, 3), (3, 1)] else -I, c)
def pmul(P, Qs):
    c1, r1 = pmul1(P[0], Qs[0]); c2, r2 = pmul1(P[1], Qs[1])
    return (expand(c1 * c2), (r1, r2))
IX = {s: k for k, s in enumerate(STR)}
def comm(u, v):
    out = [0] * 16
    for p in STR:
        if u[IX[p]] == 0: continue
        for q in STR:
            if v[IX[q]] == 0: continue
            c, r = pmul(p, q); c2, _ = pmul(q, p)
            d = expand(-(c - c2) / I)
            if d != 0: out[IX[r]] += u[IX[p]] * v[IX[q]] * d
    return [sp.nsimplify(x) for x in out]
def to_matrix(v): return sum((v[IX[s]] * KR[s] for s in STR if v[IX[s]] != 0), zeros(4, 4))
def from_matrix(M): return [sp.nsimplify(simplify((KR[s] * M).trace() / 4)) for s in STR]
def ad_discrete(d, v, anti=False):
    M = to_matrix(v)
    if anti: M = -M.conjugate()          # i H -> T (i H) T^-1 = -i conj(H)
    return from_matrix(d * M * d.H)
def closure(flows, discretes, anti=False):
    basis = [list(f) for f in flows]
    def rk(vs): return Matrix(vs).rank() if vs else 0
    r = rk(basis); changed = True
    while changed:
        changed = False
        cands = []
        for a in basis:
            for b in basis: cands.append(comm(a, b))
            for d in discretes: cands.append(ad_discrete(d, a))
            if anti: cands.append(ad_discrete(eye(4), a, anti=True))
        for c in cands:
            if any(x != 0 for x in c) and rk(basis + [c]) > r:
                basis.append(c); r += 1; changed = True
    return basis
def vec(s): v = [0] * 16; v[IX[s]] = 1; return v
X_, Y_, Z_ = 1, 2, 3
XI, IX_, ZI, IZ = vec((X_, 0)), vec((0, X_)), vec((Z_, 0)), vec((0, Z_))
UJI, IUJ = kron(UJ, I2), kron(I2, UJ); XI_m, IX_m = kron(SX, I2), kron(I2, SX)
lvl2 = [kron(SZ, I2), kron(I2, SZ)]
def dims(flows, discretes):
    d1 = len(closure(flows, [CNOT] + discretes))
    d2 = len(closure(flows, [CNOT] + discretes + lvl2, anti=True))
    return d1, d2
nodes = [('L1 {flow}@C', [XI], [], (2, 2)), ('L2 {flow}@T', [IX_], [], (1, 1)), ('L3 {flow both}', [XI, IX_], [], (3, 3)),
         ('L4 {flow,NOT}@C', [XI], [XI_m], (2, 2)), ('L5 {flow,NOT}@T', [IX_], [IX_m], (1, 1)),
         ('L6 {J}@C / {NOT,J}@C', [], [UJI, XI_m], (0, 0)), ('L7 {flow,J}@C', [XI], [UJI], (6, 6)),
         ('L8 {flow,J}@T', [IX_], [IUJ], (6, 6)), ('L9 flow@C + J@T', [XI], [IUJ], (15, 15)),
         ('L10 flow@T + J@C', [IX_], [UJI], (1, 1)), ('L11 z-flow @C / @T / both', None, None, (1, 2, 3)),
         ('L12 {z-flow,J}@C / @T', None, None, (6, 6))]
for name, flows, discs, exp_ in nodes:
    if name.startswith('L11'):
        got = (dims([ZI], [])[0], dims([IZ], [])[0], dims([ZI, IZ], [])[0]); rec(name.split()[0], got == exp_, name + ' (level i)', 'dims %s' % (got,)); continue
    if name.startswith('L12'):
        got = (dims([ZI], [UJI])[0], dims([IZ], [IUJ])[0]); rec(name.split()[0], got == exp_, name + ' (level i)', 'dims %s' % (got,)); continue
    got = dims(flows, discs)
    rec(name.split()[0], got == exp_, name + ' (i)/(ii)', 'dims %s' % (got,))

print("== U  UNIQUE criterion and reachability witnesses")
def contains(basis, targets):
    return Matrix(basis).rank() == Matrix(basis + targets).rank()
LC = closure([XI], [CNOT, UJI]); LT = closure([IX_], [CNOT, IUJ]); Lflow = closure([XI], [CNOT])
su2_xPp = [from_matrix(kron(SG[k], Pp)) for k in (1, 2, 3)]; su2_xPm = [from_matrix(kron(SG[k], Pm)) for k in (1, 2, 3)]
P0_su2 = [from_matrix(kron(P0, SG[k])) for k in (1, 2, 3)]; P1_su2 = [from_matrix(kron(P1, SG[k])) for k in (1, 2, 3)]
rec('U1', contains(LC, su2_xPp) and contains(LC, su2_xPm), 'L({flow,J}@C) contains su(2) x P+ and su(2) x P- (p = X-eigenstates)')
rec('U2', contains(LT, P0_su2) and contains(LT, P1_su2), 'L({flow,J}@T) contains |0><0| x su(2) and |1><1| x su(2)')
rec('U1c', not contains(Lflow, su2_xPp) and not contains(Lflow, P0_su2) and not contains(Lflow, P1_su2) and not contains(Lflow, su2_xPm), 'the flow-only node contains neither (criterion fails on the S3 instance)')
def witness_control(psi):   # psi unit 4-vector; find product u x (a|+> + b|->) and U+, U- in SU(2) with (U+ x P+ + U- x P-) product = psi
    ket_p = Matrix([1, 1]) / sqrt(2); ket_m = Matrix([1, -1]) / sqrt(2)
    psi_p = Matrix([(kron(I2, ket_p.T) * psi)[k] for k in range(2)]); psi_m = Matrix([(kron(I2, ket_m.T) * psi)[k] for k in range(2)])
    a = sqrt(simplify((psi_p.H * psi_p)[0])); b = sqrt(simplify((psi_m.H * psi_m)[0]))
    u = Matrix([1, 0])
    def su2_taking_e0_to(v):   # unit v -> SU(2) matrix with first column v
        return Matrix([[v[0], -sp.conjugate(v[1])], [v[1], sp.conjugate(v[0])]])
    Up = su2_taking_e0_to(psi_p / a) if a != 0 else I2; Um = su2_taking_e0_to(psi_m / b) if b != 0 else I2
    G = kron(Up, Pp) + kron(Um, Pm)
    prod = kron(u, a * ket_p + b * ket_m)
    ok = simplify(expand(G * G.H - eye(4))) == zeros(4, 4) and all(simplify(expand(x)) == 0 for x in (G * prod - psi)) and simplify(Up.det()) == 1 and simplify(Um.det()) == 1
    return ok, a, b
phi0 = Matrix([1, 2, 3 * I, -1 + I]); psi0 = phi0 / 4; psi_a = Matrix([15, -1, 7, 7]) / 18
ok3, a3, b3 = witness_control(psi0); ok4, a4, b4 = witness_control(psi_a)
rec('U3', ok3 and simplify((psi0.H * psi0)[0]) == 1, 'exact witness: (U+ x P+ + U- x P-) carries a product to psi0 = phi0/4', 'weights %s, %s' % (a3, b3))
rec('U4', ok4 and simplify((psi_a.H * psi_a)[0]) == 1, 'exact witness: (U+ x P+ + U- x P-) carries a product to psi_a = (15,-1,7,7)/18', 'weights %s, %s' % (a4, b4))

print("== O  projective orbits of phi0's ray under the finite native groups")
def canon_vec(v):
    v = v.applyfunc(lambda z: sp.nsimplify(simplify(z)))
    for k in range(4):
        if v[k] != 0: return sp.ImmutableMatrix((v / v[k]).applyfunc(lambda z: sp.nsimplify(simplify(z))))
def orbit(gens, v0):
    start = canon_vec(v0); orb = {start}; frontier = [start]
    while frontier:
        nxt = []
        for v in frontier:
            for g in gens:
                w = canon_vec(g * Matrix(v))
                if w not in orb: orb.add(w); nxt.append(w)
        frontier = nxt
    return orb
oC = orbit([UJI, CNOT], phi0); oT = orbit([IUJ, CNOT], phi0)
rec('O1', len(oC) == 768, 'orbit of phi0 under <U_J x I, CNOT>: 768 rays', 'size %d' % len(oC))
rec('O2', len(oT) == 384, 'orbit of phi0 under <I x U_J, CNOT>: 384 rays', 'size %d' % len(oT))
oCN = orbit([UJI, CNOT, XI_m], phi0); oTN = orbit([IUJ, CNOT, IX_m], phi0)
rec('O3', len(oCN) == 768 and len(oTN) == 384, 'adding the NOT (X x I resp. I x X) leaves both orbits unchanged', 'sizes %d, %d' % (len(oCN), len(oTN)))
def det2(v): return v[0] * v[3] - v[1] * v[2]
def dlow_finite(orb):
    return min(simplify(expand(det2(v) * sp.conjugate(det2(v))) / (v.H * v)[0]) for v in orb)
dC, dT = dlow_finite(oC), dlow_finite(oT)
rec('O4', dC == Q(5, 256) and dT == Q(5, 256), 'd_low = min |det|^2/n^2 over both orbits = 5/256', '%s, %s' % (dC, dT))

print("== S  torus seeds: exact minimum of |det|^2 along the non-local flow direction")
def torus_min_exact(chi, Nmat):
    # e^{-i beta N} chi = cos(beta) chi - i sin(beta) N chi ; det is u cos2b + v sin2b with u = det(chi), v = (det(chi - i N chi) )/2 ... derived generally:
    cb, sb = symbols('cb sb', real=True)
    w = cb * chi - I * sb * (Nmat * chi)
    d = expand(det2(w))
    # write d = A cb^2 + B sb^2 + C cb sb ; with cb^2 = (1+c2)/2, sb^2 = (1-c2)/2, cb sb = s2/2  (c2 = cos 2b, s2 = sin 2b)
    pol = sp.Poly(d, cb, sb); A = pol.coeff_monomial(cb ** 2); B = pol.coeff_monomial(sb ** 2); Cc = pol.coeff_monomial(cb * sb)
    const = simplify((A + B) / 2); u = simplify((A - B) / 2); v = simplify(Cc / 2)
    # claim: const = 0 (homogeneous in (cos 2b, sin 2b))
    Qm = Matrix([[simplify(u * sp.conjugate(u)), simplify(sp.re(u * sp.conjugate(v)))], [simplify(sp.re(u * sp.conjugate(v))), simplify(v * sp.conjugate(v))]])
    tr = simplify(Qm.trace()); de = simplify(Qm.det())
    lam_min = simplify((tr - sqrt(tr ** 2 - 4 * de)) / 2)
    bound = simplify(de / tr) if tr != 0 else 0
    n2 = simplify((chi.H * chi)[0])
    return const, lam_min / n2, bound / n2, Qm
NXX = kron(SX, SX); NZZ = kron(SZ, SZ)
res = [torus_min_exact(chi, NXX) for chi in (phi0, CNOT * phi0)]
okS1 = all(simplify(c) == 0 for c, _, _, _ in res)
true_min = min((r[1] for r in res), key=lambda e: float(e)); bnd_min = min((r[2] for r in res), key=lambda e: float(e))
rec('S1', okS1 and float(bnd_min) <= float(true_min) + 1e-15, '{flow}@C: |det|^2 along e^{-i b XX} is a homogeneous form in (cos 2b, sin 2b); det Q/tr Q <= exact lambda_min over the D-orbit {phi0, CNOT phi0}', 'exact min %s ~ %.8f; bound min %s' % (true_min, float(true_min), bnd_min))
rec('S2', bnd_min == Q(1, 2304), "C5's d_low for {flow}@C (level i) = 1/2304 (the bound at the minimizing orbit element)", 'bound %s' % bnd_min)
alpha = Q(499783, 500000); r = 2 * alpha - 1
rec('S3', r < 1 and r ** 2 >= 1 - 4 * Q(1, 2304) and alpha < 1, 'alpha = 499783/500000: r = 2 alpha - 1 < 1 and r^2 >= 1 - 4 d_low (seed admissible on the whole reachable set)')
resZ = [torus_min_exact(chi, NZZ) for chi in (phi0, CNOT * phi0)]
bndZ = min((rr[2] for rr in resZ), key=lambda e: float(e)); trueZ = min((rr[1] for rr in resZ), key=lambda e: float(e))
rec('S4', bndZ == Q(1, 8704) and float(bndZ) <= float(trueZ) + 1e-15, 'z-flow@T (N = Z x Z): d_low = 1/8704', 'bound %s, exact min %s ~ %.8f' % (bndZ, trueZ, float(trueZ)))
# stage-4 seed values inside the exact windows: c <= 1/m with m = (1 + sqrt(1 - 4 dmin))/2 using the EXACT minimum
def window_ok(c, dmin): return c > 1 and c <= 2 and simplify(c * (1 + sqrt(1 - 4 * dmin)) / 2) < 1
rec('S5', window_ok(Q(4609, 4608), true_min) and window_ok(Q(17409, 17408), trueZ) and window_ok(Q(4609, 4608), Q(1, 2304)) and window_ok(Q(17409, 17408), Q(1, 8704)), 'stage-4 seeds c = 4609/4608 (actC Rx), 17409/17408 (actT Rz) lie in the windows from the exact minima and from the bounds')
random.seed(11); worst = 10.0
import cmath, math
phi0f = [complex(1, 0), complex(2, 0), complex(0, 3), complex(-1, 1)]
NXXf = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
for chi in (phi0f, [phi0f[0], phi0f[1], phi0f[3], phi0f[2]]):
    for k in range(20000):
        b = 2 * math.pi * k / 20000
        Nchi = [sum(NXXf[i][j] * chi[j] for j in range(4)) for i in range(4)]
        w = [math.cos(b) * chi[i] - 1j * math.sin(b) * Nchi[i] for i in range(4)]
        dd = abs(w[0] * w[3] - w[1] * w[2]) ** 2 / 256
        worst = min(worst, dd)
rec('S6', worst >= float(true_min) - 1e-9, 'FLOAT sanity: a 20000-point scan of beta over the D-orbit never goes below the exact minimum', 'scan min %.8f vs exact %.8f' % (worst, float(true_min)))
bell = CNOT * kron(Matrix([1, 1]) / sqrt(2), Matrix([1, 0]))
cB, lamB, bndB, _ = torus_min_exact(bell, NXX)
rec('S1c', simplify(lamB) == 0 and simplify(bndB) == 0, 'countercontrol: the reachable Bell state CNOT|+0> gives exact minimum 0 (no seed)')

print("== K  K(Z_F) and the named countercontrols")
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = {s: zdef(*s) for s in SS}; ZSET = set(sp.ImmutableMatrix(ZF[s]) for s in SS)
def negvec(M):
    ns = (M + eye(4) / 8).nullspace(); v = ns[0]; return v / sqrt((v.H * v)[0])
PSI = {s: negvec(pauliW(ZF[s])) for s in SS}
def permutes(f): return all(sp.ImmutableMatrix(f(ZF[s])) in ZSET for s in SS) and len({sp.ImmutableMatrix(f(ZF[s])) for s in SS}) == 4
gensK = {'CNOT': lambda w: Ad(CNOT, w), 'ZxI': lambda w: Ad(kron(SZ, I2), w), 'IxZ': lambda w: Ad(kron(I2, SZ), w),
         'T': lambda w: tab(pauliW(w).conjugate()), 'SWAP': lambda w: Ad(SWAP, w), 'XxI': lambda w: Ad(kron(SX, I2), w), 'IxX': lambda w: Ad(kron(I2, SX), w)}
rec('K1', all(permutes(f) for f in gensK.values()), 'every generator of <G16, SWAP> and both NOTs permute the defect set Z_F (K(Z_F) invariant)')
a1, a2, a3, b1, b2, b3 = symbols('a1 a2 a3 b1 b2 b3', real=True)
okK2 = True
for s in SS:
    Ms = Matrix(3, 3, lambda i, j: 4 * ZF[s][i + 1, j + 1])
    val = 4 * ipW(prodState([a1, a2, a3], [b1, b2, b3]), ZF[s])
    okK2 = okK2 and simplify(val - (1 + (Matrix([[a1, a2, a3]]) * Ms * Matrix([b1, b2, b3]))[0])) == 0 and simplify(Ms * Ms.T - eye(3)) == zeros(3, 3)
rec('K2', okK2, 'theta: 4 <prodState(a,b), z_s> = 1 + a^T M_s b with M_s orthogonal (symbolic), so every defect is in maxCone')
u = symbols('u', real=True); w = (1 - u ** 2 + 2 * I * u) / (1 + u ** 2); w2 = symbols('w2')
def Uf(wv): return eye(4) + (wv - 1) * ket1m * ket1m.H
k0p = kron(Matrix([1, 0]), Matrix([1, 1]) / sqrt(2)); k0m = kron(Matrix([1, 0]), Matrix([1, -1]) / sqrt(2)); k1p = kron(Matrix([0, 1]), Matrix([1, 1]) / sqrt(2))
C1 = lambda ww: k0p + ww * ket1m; C2 = lambda ww: k0m + ww * k1p
def on_circles(v):   # is v proportional to C1(w') or C2(w') for some unit w'?  check by the pattern of components
    v = v.applyfunc(lambda z: simplify(expand(z)))
    for Cf in (C1, C2):
        base = Cf(w2)
        # solve for scale and w2 from the two nonzero component families
        sol = sp.solve([v[k] - symbols('lam0') * base[k] for k in range(4)], [symbols('lam0'), w2], dict=True)
        for sdict in sol:
            if all(simplify(v[k] - sdict[symbols('lam0')] * base[k].subs(w2, sdict[w2])) == 0 for k in range(4)) and simplify(sdict[w2] * sp.conjugate(sdict[w2]) - 1) == 0:
                return True
    return False
pt_ = C1(w)
maps = [lambda v: Uf(w).subs(u, Q(1, 3)) * v, lambda v: CNOT * v, lambda v: kron(SZ, I2) * v, lambda v: kron(I2, SZ) * v, lambda v: v.conjugate()]
okK3 = simplify(expand(w * sp.conjugate(w) - 1)) == 0 and simplify(Uf(-1) - CNOT) == zeros(4, 4)
okK3 = okK3 and all(on_circles(m(C1(w).subs(u, Q(2, 5)))) and on_circles(m(C2(w).subs(u, Q(2, 5)))) for m in maps)
for Cf in (C1, C2):
    v = Cf(w); dv = det2(v); okK3 = okK3 and simplify(expand(dv * sp.conjugate(dv) / ((v.H * v)[0]) ** 2) - Q(1, 4)) == 0
psiF = C1(1) / sqrt(2)
okK3 = okK3 and tab((eye(4) - 2 * psiF * psiF.H) / 8) == ZF[(-1, -1)]
rec('K3', okK3, 'kappa: U(-1) = CNOT; C1, C2 mapped into C1 u C2 by U(w), CNOT, Z x I, I x Z, T (at a rational point); every circle point maximally entangled (symbolic); defect of C1(1)/sqrt2 = z_(-1,-1)')
Umi = Uf(-I); found = None
for s in SS:
    phi = Umi * PSI[s]; ovs = [simplify(abs((PSI[tt].H * phi)[0]) ** 2) for tt in SS]
    pairing = simplify(ipW(tab(phi * phi.H), Ad(Umi, ZF[s])))
    if all(o <= Q(1, 2) for o in ovs) and pairing < 0: found = (s, ovs, pairing); break
rec('K4', found is not None and found[2] == Q(-1, 2), 'kappa-cc: at w = -i a defect leaves K(Z_F): witness U psi_s in K(Z_F), pairing -1/2', '%s' % (found,))
psi11, psi1m, psim1 = PSI[(1, 1)], PSI[(1, -1)], PSI[(-1, 1)]
Dw = eye(4) + (w - 1) * psi11 * psi11.H
x = (psi1m + psim1) / sqrt(2)
B = Matrix.hstack(*[PSI[s] for s in SS])        # defect basis (orthonormal)
Pperm = B * Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) * B.H   # exchanges psi_(1,1) and psi_(1,-1)
JDJ = Pperm * (eye(4) - 2 * psi11 * psi11.H) * Pperm.H
okK5 = all(simplify(expand(z)) == 0 for z in (Dw * x - x)) and all(sp.ImmutableMatrix(Ad(Pperm, ZF[s])) in ZSET for s in SS)
okK5 = okK5 and simplify(expand(abs((x.H * (JDJ * x))[0]) ** 2)) != 1
rec('K5', okK5, 'zeta: D(w) fixes x = T(psi_(1,-1) + psi_(-1,1)) for all w (symbolic); J = permutation unitary in the defect basis is an automorphism of K(Z_F); J D(-1) J^-1 moves x')
v6 = Matrix([5, -5, -1, -1]); rho6 = tab(v6 * v6.H / (v6.H * v6)[0]); E0 = E(0, 0) + E(1, 3) - E(2, 2)
rec('K6', simplify(ipW(rho6, E0)) == Q(3, 13) and simplify(ipW(rho6, Ad(SWAP, E0))) == Q(-5, 13), 'iota-cc: (5,-5,-1,-1) in Q3 n E0* (3/13) pairs -5/13 with SWAP E0')
rec('K7', ipW(E0, actT(NF, E0)) == -1 and ipW(E0, actC(NF, E0)) == 1, 'eta-cc: <E0, actT nflip E0> = -1 and <E0, actC nflip E0> = +1')
okK8 = simplify(expand(UJI * CNOT * UJI.H - (kron(I2, Pp) + kron(SX, Pm)))) == zeros(4, 4)
okK8 = okK8 and all(not (simplify(SX * v - lam * v) == zeros(2, 1)) for lam in (1, -1) for v in [Matrix([1, 0]), Matrix([0, 1])])
rec('K8', okK8, 'FORM-J: (U_J x I) CNOT (U_J x I)^dag = I x P+ + X x P-; Z-eigenvectors are not X-eigenvectors (no common eigenvector)')
F = ZF[(-1, -1)]
valp = 4 * ipW(prodState([a1, a2, a3], [b1, b2, b3]), F); valc = 4 * ipW(Ad(CNOT, prodState([a1, a2, a3], [b1, b2, b3])), F)
def is_orth_form(expr):
    M = Matrix(3, 3, lambda i, j: sp.Poly(expr, a1, a2, a3, b1, b2, b3).coeff_monomial([a1, a2, a3][i] * [b1, b2, b3][j]))
    return simplify(expr - (1 + (Matrix([[a1, a2, a3]]) * M * Matrix([b1, b2, b3]))[0])) == 0 and simplify(M * M.T - eye(3)) == zeros(3, 3)
okK9 = is_orth_form(expand(valp)) and is_orth_form(expand(valc)) and min(pauliW(F).eigenvals().keys(), key=lambda e: float(e)) == Q(-1, 8)
okK9 = okK9 and simplify(ipW(tab(psiF * psiF.H), F)) == Q(-1, 2)
rec('K9', okK9, 'CL1: F pairs >= 0 with products and with cnot-images of products (orthogonal forms, Cauchy-Schwarz); F not in Q3 (eigenvalue -1/8); F pairs -1/2 with its own state')
reflY = Matrix.diag(1, -1, 1); Rgen = Rx(t) * Rz(symbols('s', real=True))
RR = reflY * Rgen * reflY
rec('K10', simplify(RR * RR.T - eye(3)) == zeros(3, 3) and simplify(RR.det()) == 1, 'LAMBDA-tw: reflY R reflY is a rotation for a rotation R (symbolic)')
idW = eye(4); chainW = Ad(CNOT, idW)
def sharp(n): return Matrix([Q(1, 2), n[0] / 2, n[1] / 2, n[2] / 2])
val_chain = (sharp([-1, 0, 0]).T * chainW * sharp([0, 0, -1]))[0]
grid = [sp.Matrix(n) for n in itertools.product([-1, 0, 1], repeat=3) if sum(abs(k) for k in n) == 1] + [Matrix([Q(3, 5), 0, Q(4, 5)]), Matrix([0, Q(3, 5), Q(-4, 5)])]
okK11 = chainW == Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) and val_chain == Q(-1, 2)
okK11 = okK11 and all((sharp(n).T * idW * sharp(m))[0] >= 0 for n in grid for m in grid)
rec('K11', okK11, 'THETA-cc: chainW = cnot idW (K2Guard:104) pairs -1/2 with the sharp effects of -e1, -e3; idW pairs >= 0 with sharp-effect products on a grid')

n_ok = sum(R); print(f"SUMMARY {n_ok}/{len(R)} CONFIRMED")
print("INDEP-C-FIXED" if all(R) else "INDEP-C-MISMATCH")
