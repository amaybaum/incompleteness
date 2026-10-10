# y4_s3_cert.py -- thread Y (stage 4, Q-EX): exact unreachability certificates and EBF cap seeds for the
# exceptional one-parameter nodes at level (ii) (the S3 instance actC Rx and the other exceptional axes, and the
# native drive on both tokens).
#
# Setting (written argument, RESULT Y4): for a family with local generator(s) L and one non-local generator
# N = A(x)B (a two-qubit Pauli product) the group is G^ = T.G16, T = exp span{iL, iN} (abelian torus), and
# min over g in G^ of |det Psi(g phi0)|^2 = min over beta and psi in {phi0, CNOT phi0} of f_psi(beta),
# f_psi(beta) = (C,S) Q_psi (C,S)^T, (C,S) = (cos 2beta, sin 2beta).
#
# DECISION RULE (fixed before the first run; rules, not expected numbers):
#  * F-lines (structure, exact): G16 enumerated by closure of its generators has the order printed and every
#    element is local or CNOT.local; G16 maps span{L, N} into itself; CNOT exchanges L and N up to sign; the
#    identity det(cb Psi - i sb A Psi B^T) = (cb^2 - sb^2) D - i cb sb M holds symbolically.
#  * Witness: the first phi0 in the fixed candidate list for which Q_psi is positive definite (exact: Q00 > 0
#    and det Q > 0) for both psi and for every family is used for all families.
#  * Seed: the largest c in the fixed list C_LIST such that Q_psi - mu*(c) I is PSD for both psi, where
#    mu*(c) = |phi0|^4 (1 - (2/c - 1)^2)/4; then every g in G^ has c * (largest product overlap of g phi0) <= 1.
#    PASS iff such c > 1 exists; the seed table is printed and its non-PSD-ness checked exactly.
#  * Spot check (cross-check of the reduction, not part of the proof): for all h in G16 and 6 rational members
#    t of T, |det Psi(h t phi0)|^2 >= mu*(c) |phi0|^4 / |phi0|^4-normalized, exactly.
#  * Countercontrols: (cc1) a reachable state t0 (a(x)b) has det Q = 0 (certificate fails); (cc2) for the S3
#    instance every maximally entangled state with an all-maximally-entangled T-orbit is sent to a product by
#    CNOT (symbolic in the phase), and a generic maximally entangled state has some orbit member with
#    largest product overlap > 1/2 (Q - |psi|^4/4 I not PSD); (cc3) phi0 is reachable for an oblique control
#    axis (exact witness g = I(x)P+ + V(x)P-, V in SU(2)).
#  * "VERDICT Y4-CERT-EXACT" iff every line passes; otherwise "VERDICT Y4-CERT-FAILED" and the failing ids.
import sympy as sp

I = sp.I
S = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]),
     sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E2 = S[0]


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


SS = [[kron(S[m], S[n]) for n in range(4)] for m in range(4)]
table = lambda R: [[sp.expand((R * SS[m][n]).trace()) for n in range(4)] for m in range(4)]
ipW = lambda a, b: sp.expand(sum(a[m][n] * b[m][n] for m in range(4) for n in range(4)))
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
Pp, Pm = (E2 + S[1]) / 2, (E2 - S[1]) / 2
R_ = sp.Rational
fails = []


def report(cid, ok, text):
    print(("PASS " if ok else "FAIL ") + cid + " " + text)
    if not ok:
        fails.append(cid)


def canon(U):
    for x in U:
        if x != 0:
            return (U / x).applyfunc(sp.expand)
    raise ValueError


def compose(g1, g2):
    U1, k1 = g1; U2, k2 = g2
    return (canon(U1 * (U2.conjugate() if k1 else U2)), k1 ^ k2)


def key(g):
    return (tuple(g[0]), g[1])


def enum_group(gens):
    start = (canon(sp.eye(4)), 0)
    els = {key(start): start}
    frontier = [start]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = compose(h, g)
                if key(p) not in els:
                    els[key(p)] = p; new.append(p)
        frontier = new
    return list(els.values())


def is_local(U):
    M = sp.Matrix(4, 4, lambda r, c: U[2 * (r // 2) + (c // 2), 2 * (r % 2) + (c % 2)])
    return M.rank() == 1


def apply(g, v):
    U, k = g
    return U * (v.conjugate() if k else v)


def detpsi(v):
    return sp.expand(v[0] * v[3] - v[1] * v[2])


absq = lambda z: sp.expand(z * sp.conjugate(z))
norm2 = lambda v: sp.expand((v.H * v)[0])
G16gens = [(CNOT, 0), (kron(S[3], E2), 0), (kron(E2, S[3]), 0), (sp.eye(4), 1)]
G16 = enum_group([(canon(U), k) for U, k in G16gens])
okloc = all(is_local(U) or is_local(CNOT * U) for U, k in G16)
report("F1", len(G16) == 16 and okloc, "G16 enumerated: order %d; every element is local or CNOT.local" % len(G16))

FAM = {'S3:actC-Rx': ([kron(S[1], E2)], kron(S[1], S[1])), 'actC-Ry': ([kron(S[2], E2)], kron(S[2], S[1])),
       'actT-Ry': ([kron(E2, S[2])], kron(S[3], S[2])), 'actT-Rz': ([kron(E2, S[3])], kron(S[3], S[3])),
       'drive-both': ([kron(S[1], E2), kron(E2, S[1])], kron(S[1], S[1]))}
PAULI_OF = {'S3:actC-Rx': (1, 1), 'actC-Ry': (2, 1), 'actT-Ry': (3, 2), 'actT-Rz': (3, 3), 'drive-both': (1, 1)}


def in_span(A, basis_):
    vec = lambda X: [sp.expand((SS[m][n] * X).trace()) for m in range(4) for n in range(4)]
    M = sp.Matrix([vec(X) for X in basis_])
    return sp.Matrix([vec(X) for X in basis_] + [vec(A)]).rank() == M.rank()


for name, (Ls, N) in FAM.items():
    span = Ls + [N]
    okn = all(in_span(U * (X.conjugate() if k else X) * U.H, span) for (U, k) in G16gens for X in span)
    okc = in_span(CNOT * N * CNOT, Ls) and all(in_span(CNOT * X * CNOT, span) for X in Ls) \
        and any(in_span(CNOT * X * CNOT, [N]) for X in Ls)
    comm = all((X * Y - Y * X) == sp.zeros(4, 4) for X in span for Y in span)
    report("F2-" + name, okn and okc and comm, "G16 normalizes span(L,N); CNOT exchanges a local generator with N; torus abelian")

ps = sp.symbols('r0:4', real=True); qs = sp.symbols('i0:4', real=True); cb, sb = sp.symbols('cb sb', real=True)
Psi = sp.Matrix([[ps[0] + I * qs[0], ps[1] + I * qs[1]], [ps[2] + I * qs[2], ps[3] + I * qs[3]]])


def Dm(Psi_, a, b):
    Q = S[a] * Psi_ * S[b].T
    D = Psi_.det()
    M = Psi_[0, 0] * Q[1, 1] + Psi_[1, 1] * Q[0, 0] - Psi_[0, 1] * Q[1, 0] - Psi_[1, 0] * Q[0, 1]
    return Q, D, M


okid = True
for name, (a, b) in PAULI_OF.items():
    Q, D, M = Dm(Psi, a, b)
    lhs = (cb * Psi - I * sb * Q).det()
    okid = okid and sp.expand(lhs - ((cb**2 - sb**2) * D - I * cb * sb * M)) == 0
report("F3", okid, "det(cb Psi - i sb A Psi B^T) = (cb^2 - sb^2) det Psi - i cb sb M, symbolic, all five families")


def Qform(v, a, b):
    Psi_ = sp.Matrix([[v[0], v[1]], [v[2], v[3]]])
    _, D, M = Dm(Psi_, a, b)
    w = sp.expand(-I * M / 2)
    off = sp.expand(sp.re(sp.expand(D * sp.conjugate(w))))
    return sp.Matrix([[absq(D), off], [off, absq(w)]])


pd = lambda Q: Q[0, 0] > 0 and Q.det() > 0
psd = lambda Q: Q[0, 0] >= 0 and Q[1, 1] >= 0 and Q.det() >= 0
CANDS = [[1, 2, 3 * I, -1 + I], [2, 1 + I, -I, 3], [1, 3, 2 * I, -2 + I], [3, -1, 1 + 2 * I, 2 * I]]
phi0 = None
for cand in CANDS:
    v = sp.Matrix(cand)
    if all(pd(Qform(x, *PAULI_OF[nm])) for nm in FAM for x in (v, CNOT * v)):
        phi0 = v; break
report("W1", phi0 is not None, "witness phi0 = %s: Q positive definite for phi0 and CNOT phi0, all five families" % (list(phi0) if phi0 is not None else None))
C_LIST = [R_(2), R_(3, 2), R_(5, 4), R_(9, 8), R_(17, 16), R_(33, 32), R_(65, 64), R_(129, 128), R_(257, 256), R_(513, 512)]
N0 = norm2(phi0)
for name in FAM:
    Qs = [Qform(x, *PAULI_OF[name]) for x in (phi0, CNOT * phi0)]
    cbest = None
    for c in C_LIST:
        mu = N0**2 * (1 - (2 / c - 1)**2) / 4
        if all(psd(Q - mu * sp.eye(2)) for Q in Qs):
            cbest = c; break
    ok = cbest is not None and cbest > 1
    detail = "c = %s" % cbest
    if ok:
        Pn = phi0 * phi0.H / N0
        e = table((sp.eye(4) - cbest * Pn) / 8)
        notpsd = ipW(e, table(Pn)) < 0
        mu = N0**2 * (1 - (2 / cbest - 1)**2) / 4
        Ls, N = FAM[name]
        spot = True
        for (cc, ss) in [(R_(3, 5), R_(4, 5)), (R_(5, 13), R_(12, 13)), (R_(8, 17), R_(15, 17))]:
            for (ca, sa) in [(1, 0), (R_(4, 5), R_(3, 5))]:
                t = (cc * sp.eye(4) - I * ss * N) * (ca * sp.eye(4) - I * sa * Ls[0])
                for h in G16:
                    v = apply(h, t * phi0)
                    spot = spot and absq(detpsi(v)) * N0**2 >= mu * norm2(v)**2
        ok = ok and notpsd and spot
        detail += "; seed e = table((I - c P_phi0)/8), <e, P_phi0> = %s < 0; spot check over 16 x 6 members: %s" % (
            ipW(e, table(Pn)), spot)
    report("C-" + name, ok, "cap seed: " + detail)

a0, b0 = sp.Matrix([1, 2]), sp.Matrix([1, -1 + I])
t0 = R_(3, 5) * sp.eye(4) - I * R_(4, 5) * kron(S[1], S[1])
phr = t0 * sp.Matrix([a0[0] * b0[0], a0[0] * b0[1], a0[1] * b0[0], a0[1] * b0[1]])
Qr = Qform(phr, 1, 1)
report("cc1", Qr.det() == 0, "reachable state t0(a(x)b) (S3 instance): det Q = %s, the certificate fails as it must" % Qr.det())
w = sp.symbols('w')
ok2 = True
for v in (sp.Matrix([1, 1, -1, -1]) + w * sp.Matrix([1, -1, 1, -1]), sp.Matrix([1, 1, 1, 1]) + w * sp.Matrix([1, -1, -1, 1])):
    ok2 = ok2 and sp.expand(detpsi(CNOT * v)) == 0
vme = sp.Matrix([1, 1, 1, -1])                      # (H(x)I)Phi+: maximally entangled, u ~ |0>, v ~ |1>

Qm = Qform(vme, 1, 1)
nme = norm2(vme)
ok3 = absq(detpsi(vme)) * 4 == nme**2 and not psd(Qm - nme**2 / 4 * sp.eye(2))
report("cc2", ok2 and ok3, "Bell-type route for the S3 instance: |-+> + w|+->, |++> + w|--> go to products under CNOT; "
       "(1,1,1,-1) is max. entangled but its T-orbit has a member with product overlap > 1/2")
u = sp.Matrix([phi0[0] + phi0[1], phi0[2] + phi0[3]]); v = sp.Matrix([phi0[0] - phi0[1], phi0[2] - phi0[3]])
nu, nv = sp.sqrt(norm2(u)), sp.sqrt(norm2(v))
ah, vh = u / nu, v / nv
perp = lambda x: sp.Matrix([-sp.conjugate(x[1]), sp.conjugate(x[0])])
V = sp.Matrix.hstack(vh, perp(vh)) * sp.Matrix.hstack(ah, perp(ah)).H
bvec = (nu * sp.Matrix([1, 1]) + nv * sp.Matrix([1, -1])) / sp.sqrt(2)
g = kron(E2, Pp) + kron(V, Pm)
out = g * sp.Matrix([ah[0] * bvec[0], ah[0] * bvec[1], ah[1] * bvec[0], ah[1] * bvec[1]])
okV = all(sp.simplify(x) == 0 for x in (V.H * V - E2)) and sp.simplify(V.det() - 1) == 0
report("cc3", okV and all(sp.simplify(x) == 0 for x in (out - sp.sqrt(2) * phi0)),
       "phi0 is reachable for an oblique control axis: (I(x)P+ + V(x)P-)(a(x)b) = sqrt2 phi0, V in SU(2), exact")
if fails:
    print("VERDICT Y4-CERT-FAILED " + " ".join(fails))
else:
    print("VERDICT Y4-CERT-EXACT")
