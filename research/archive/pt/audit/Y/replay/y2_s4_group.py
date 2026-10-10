# y2_s4_group.py -- thread Y (stage 4, Q-EX), node S4: the generated group exactly, reachability, controls.
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * Each check prints "PASS <id> ..." or "FAIL <id> ...". Identities PASS iff lhs - rhs reduces to exactly 0.
#  * Lie closure: the real span of the generators is closed under commutators by exact rank computation
#    over Q (iterate until no commutator raises the rank). The S4 node is called REACHABLE only if the
#    closure contains i s_k (x) P for all k = 1,2,3 for one block projector P of the stated decomposition
#    (target X-blocks P+/P- for control rotations; control Z-blocks P0/P1 for target rotations); the
#    written argument (RESULT Y2) turns that into reachability of every pure state.
#  * Reachability witnesses PASS iff g (a (x) b) is exactly proportional to the target, with g exhibited as
#    U (x) P+ + V (x) P- (or P0 (x) U + P1 (x) V), U, V checked exactly unitary with det 1.
#  * Countercontrols PASS iff the predicted failure occurs exactly: K(E0), K(Z_F) are moved out of
#    themselves by a member of the node's group (exact negative pairing with a member of the cone);
#    a commuting generator's closure is NOT reachable.
#  * "VERDICT Y2-S4-EXACT" iff all checks pass; otherwise "VERDICT Y2-S4-FAILED" and the failing ids.
import sympy as sp

I = sp.I
S = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E2 = S[0]


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
pauliW = lambda w: sum((w[m][n] * SS[m][n] for m in range(4) for n in range(4)), sp.zeros(4, 4)) / 4
table = lambda R: [[sp.expand((R * SS[m][n]).trace()) for n in range(4)] for m in range(4)]
ipW = lambda a, b: sp.expand(sum(a[m][n] * b[m][n] for m in range(4) for n in range(4)))
basis = lambda m, n: [[1 if (i, j) == (m, n) else 0 for j in range(4)] for i in range(4)]
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Pp, Pm = (E2 + S[1]) / 2, (E2 - S[1]) / 2          # target X-eigenprojectors
P0, P1 = (E2 + S[3]) / 2, (E2 - S[3]) / 2          # control Z-eigenprojectors
fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


zero = lambda e: sp.simplify(sp.expand(e)) == 0
mzero = lambda M: all(zero(x) for x in M)


def hatm(M):
    H = sp.eye(4)
    H[1:, 1:] = M
    return H


def actC(M, w):
    H = hatm(M)
    return [[sp.expand(sum(H[m, k] * w[k][n] for k in range(4))) for n in range(4)] for m in range(4)]


def actT(M, w):
    H = hatm(M)
    return [[sp.expand(sum(H[n, k] * w[m][k] for k in range(4))) for n in range(4)] for m in range(4)]


# G1: actC R(U) = Ad(U (x) I) and actT R(U) = Ad(I (x) U) on all 16 basis tables, U = a - i(bX + cY + dZ)
# symbolic (unnormalized, U^H U = N I), N R(U)_ij = tr(s_i U s_j U^H)/2; R(U) in SO(3).
qa, qb, qc, qd = sp.symbols('qa qb qc qd', real=True)
Uq = qa * E2 - I * (qb * S[1] + qc * S[2] + qd * S[3]); N = qa**2 + qb**2 + qc**2 + qd**2
NR = sp.Matrix(3, 3, lambda i, j: sp.expand((S[i + 1] * Uq * S[j + 1] * Uq.H).trace() / 2))
scal = lambda c0, w: [[sp.expand(c0 * x) for x in row] for row in w]
okC = all(table(kron(Uq, E2) * pauliW(basis(m, n)) * kron(Uq, E2).H) == actC(NR, basis(m, n))
          for m in range(4) for n in range(4) if m > 0) and \
      all(table(kron(Uq, E2) * pauliW(basis(0, n)) * kron(Uq, E2).H) == scal(N, basis(0, n)) for n in range(4))
okT = all(table(kron(E2, Uq) * pauliW(basis(m, n)) * kron(E2, Uq).H) == actT(NR, basis(m, n))
          for m in range(4) for n in range(4) if n > 0) and \
      all(table(kron(E2, Uq) * pauliW(basis(m, 0)) * kron(E2, Uq).H) == scal(N, basis(m, 0)) for m in range(4))
okR = mzero(NR.T * NR - N**2 * sp.eye(3)) and zero(NR.det() - N**3)
report("G1", okC and okT and okR, "actC R(U) = Ad(U(x)I), actT R(U) = Ad(I(x)U) (scaled by N); R(U) in SO(3); symbolic")
# G2: CNOT in the two block decompositions; the sketch's form is not CNOT; the factorization of the erratum.
report("G2a", mzero(CNOT - (kron(E2, Pp) + kron(S[3], Pm))) and mzero(CNOT - (kron(P0, E2) + kron(P1, S[1]))),
       "CNOT = I(x)P+ + Z(x)P- = P0(x)I + P1(x)X")
report("G2b", not mzero(CNOT - (kron(E2, Pp) + kron(S[1], Pm))), "countercontrol: I(x)P+ + X(x)P- != CNOT")
F1 = kron(E2, Pp) + kron(-I * S[3], Pm); F2 = kron(E2, Pp + I * Pm)
report("G2c", mzero(CNOT - F1 * F2) and mzero((Pp + I * Pm) * (Pp + I * Pm) - S[1]),
       "CNOT = [I(x)P+ + (-iZ)(x)P-][I(x)(P+ + iP-)], (P+ + iP-)^2 = X")
Rx90 = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
okr = all(table(F2 * pauliW(basis(m, n)) * F2.H) == actT(Rx90, basis(m, n)) for m in range(4) for n in range(4))
report("G2d", okr, "Ad(I(x)(P+ + iP-)) = actT Rx(pi/2) on all 16 basis tables")
# G3: delta(A(x)P+ + B(x)P-) = det A / det B: +1 on SU(2)(x)I, -1 on CNOT and on I(x)(P+ + iP-); a phase lam
# with lam*I in SU(2) and lam*i*I in SU(2) would need lam^2 = 1 and -lam^2 = 1 (no solution).
lam = sp.symbols('lam')
nosol = sp.solve([lam**2 - 1, -lam**2 - 1], lam) == []
report("G3", nosol and sp.Matrix([[1, 0], [0, 1]]).det() / (I * E2).det() == -1 and E2.det() / S[3].det() == -1,
       "delta(CNOT) = delta(I(x)(P+ + iP-)) = -1, delta(SU(2)(x)I) = +1; Ad(I(x)Rx(pi/2)) not in the connected part")
# G4: the explicit word (V^-1 (x) I) CNOT (V (x) I) CNOT = I(x)P+ + V^-1 Z V Z (x) P-, axis of V^-1ZVZ in the XY plane.
Vadj = qa * E2 + I * (qb * S[1] + qc * S[2] + qd * S[3])          # = N V^-1 for V = Uq
lhs = kron(Vadj, E2) * CNOT * kron(Uq, E2) * CNOT
W = Vadj * S[3] * Uq * S[3]
report("G4", mzero(lhs - (N * kron(E2, Pp) + kron(W, Pm))) and zero((W * S[3]).trace()),
       "word = N[I(x)P+] + (N V^-1 Z V Z)(x)P-; tr(V^-1ZVZ Z) = 0 (rotation axis in the XY plane), symbolic")


def vec(A):
    out = []
    for m in range(4):
        for n in range(4):
            x = sp.expand((SS[m][n] * A).trace() / (4 * I))
            assert sp.im(x) == 0, "non-anti-Hermitian generator"
            out.append(sp.re(x))
    return out


def kv(a, b):
    return sp.Matrix([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]])


def closure(gens):
    B, V = [], []
    def add(A):
        v = vec(A)
        if sp.Matrix(V + [v]).rank() > len(V):
            V.append(v); B.append(A); return True
        return False
    for g in gens:
        add(g)
    grown = True
    while grown:
        grown = False
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                if add(B[i] * B[j] - B[j] * B[i]):
                    grown = True
    return B, V


def contains(V, mats):
    r = sp.Matrix(V).rank()
    return sp.Matrix(V + [vec(A) for A in mats]).rank() == r


genC = [I * kron(S[k], E2) for k in (1, 2, 3)]
genC += [CNOT * g * CNOT for g in genC]
BC, VC = closure(genC)
blockC = [I * kron(S[k], P) for k in (1, 2, 3) for P in (Pp, Pm)]
report("L1", len(VC) == 6 and contains(VC, blockC) and sp.Matrix([vec(A) for A in blockC]).rank() == 6,
       "Lie closure of su(2)(x)I and its CNOT conjugate: dim %d = su(2)(x)P+ (+) su(2)(x)P-" % len(VC))
genT = [I * kron(E2, S[k]) for k in (1, 2, 3)]
genT += [CNOT * g * CNOT for g in genT]
BT, VT = closure(genT)
blockT = [I * kron(P, S[k]) for k in (1, 2, 3) for P in (P0, P1)]
report("L2", len(VT) == 6 and contains(VT, blockT) and sp.Matrix([vec(A) for A in blockT]).rank() == 6,
       "Lie closure of I(x)su(2) and its CNOT conjugate: dim %d = P0(x)su(2) (+) P1(x)su(2)" % len(VT))
IZ, conjA = kron(E2, S[3]), lambda A: A.conjugate()
report("L3", contains(VC, [IZ * A * IZ for A in BC] + [conjA(A) for A in BC]) and
       contains(VT, [kron(S[3], E2) * A * kron(S[3], E2) for A in BT] + [conjA(A) for A in BT]),
       "both closures are invariant under the level-(ii) generators Ad(I(x)Z), Ad(Z(x)I) and the transpose")
_, Vz = closure([I * kron(S[3], E2), CNOT * I * kron(S[3], E2) * CNOT])
report("L4", len(Vz) == 1 and not contains(Vz, blockC[0:1]), "countercontrol: commuting generator iZ(x)I closes at dim %d" % len(Vz))

# R: reachability witnesses (control side): psi = (u'(x)(1,1) + v'(x)(1,-1))/2, g = U(x)P+ + V(x)P-, a = |0>.
targets = {'psi_a': [1, 2, 3 * I, -1 + I], 'bell': [1, 0, 0, 1], 'singlet': [0, 1, -1, 0], 'psi_d': [3, 1 - 2 * I, 2 + I, 1]}
for name, t in targets.items():
    psi = sp.Matrix(t)
    u = sp.Matrix([psi[0] + psi[1], psi[2] + psi[3]]); v = sp.Matrix([psi[0] - psi[1], psi[2] - psi[3]])
    nu, nv = sp.sqrt(sp.expand((u.H * u)[0])), sp.sqrt(sp.expand((v.H * v)[0]))
    U = sp.Matrix([[u[0], -sp.conjugate(u[1])], [u[1], sp.conjugate(u[0])]]) / nu
    V = sp.Matrix([[v[0], -sp.conjugate(v[1])], [v[1], sp.conjugate(v[0])]]) / nv
    b = (nu * sp.Matrix([1, 1]) + nv * sp.Matrix([1, -1])) / sp.sqrt(2)
    g = kron(U, Pp) + kron(V, Pm)
    out = g * kv(sp.Matrix([1, 0]), b)
    ok = (mzero(U.H * U - E2) and mzero(V.H * V - E2) and zero(U.det() - 1) and zero(V.det() - 1)
          and mzero(out - sp.sqrt(2) * psi))
    report("R-" + name, ok, "g(|0>(x)b) = sqrt2 * psi exactly, g = U(x)P+ + V(x)P-, U, V in SU(2)")
# Target side: psi = P0(x)u + P1(x)v, g = P0(x)U + P1(x)V, b = |0>, a = (|u|, |v|).
psi = sp.Matrix(targets['psi_a'])
u, v = psi[0:2, 0], psi[2:4, 0]
nu, nv = sp.sqrt(sp.expand((u.H * u)[0])), sp.sqrt(sp.expand((v.H * v)[0]))
U = sp.Matrix([[u[0], -sp.conjugate(u[1])], [u[1], sp.conjugate(u[0])]]) / nu
V = sp.Matrix([[v[0], -sp.conjugate(v[1])], [v[1], sp.conjugate(v[0])]]) / nv
out = (kron(P0, U) + kron(P1, V)) * kv(sp.Matrix([nu, nv]), sp.Matrix([1, 0]))
report("R-T", mzero(out - psi) and zero(U.det() - 1) and zero(V.det() - 1), "target side: (P0(x)U + P1(x)V)(a(x)|0>) = psi_a exactly")

# K: countercontrols on the stage-3 cones. E0 = E00 + E13 - E22; Z_F = {(E00 + s1 E13 + s2 E22 - s1 s2 E31)/4}.
E0 = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, 0, 0]]
Rz180, Rx180 = sp.diag(-1, -1, 1), sp.diag(1, -1, -1)
v1 = ipW(actC(Rz180, E0), E0); v2 = ipW(actT(Rx180, E0), E0)
report("K1", v1 < 0 and v2 < 0, "<actC Rz(pi) E0, E0> = %s, <actT Rx(pi) E0, E0> = %s: both < 0, so K(E0) is not S4-invariant" % (v1, v2))
ZF = []
for s1 in (1, -1):
    for s2 in (1, -1):
        ZF.append([[sp.Rational(1, 4), 0, 0, 0], [0, 0, 0, sp.Rational(s1, 4)], [0, 0, sp.Rational(s2, 4), 0],
                   [0, -sp.Rational(s1 * s2, 4), 0, 0]])
caps = []
for z in ZF:
    ev = pauliW(z).eigenvects()
    neg = [vv for (val, mult, vs) in ev if val < 0 for vv in vs]
    caps.append(neg[0])
U3 = (E2 - I * (S[1] + S[2] + S[3])) / 2                     # order-3 rotation about (1,1,1), in SU(2)
okK = True
for side, G in (("C", kron(U3, E2)), ("T", kron(E2, U3))):
    for z, f in zip(ZF, caps):
        gf = G * f
        nf = sp.expand((f.H * f)[0])
        P = gf * gf.H / nf
        inK = all(ipW(table(P), zz) >= 0 for zz in ZF)                 # P in Q3 and in Z_F^*: P in K(Z_F)
        neg = ipW(table(G * pauliW(z) * G.H), table(P))
        okK = okK and inK and neg < 0
report("K2", okK, "for each z in Z_F and each side, P = P_{g f_z} lies in K(Z_F) and <g z, P> < 0 (g = Ad of the order-3 rotation)")
psi = sp.Matrix(targets['psi_a']); G = kron(U3, E2)
Pg = G * psi * psi.H * G.H
report("Q1", all(ev >= 0 for ev in Pg.eigenvals().keys()), "retention: Ad(U3(x)I) maps the pure state psi_a to a PSD table")

if fails:
    print("VERDICT Y2-S4-FAILED " + " ".join(fails))
else:
    print("VERDICT Y2-S4-EXACT")
