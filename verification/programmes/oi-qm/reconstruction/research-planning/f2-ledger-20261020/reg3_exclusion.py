"""reg3_exclusion.py -- exact checks for the F2-reg dependency ledger (research only).

Question: which pair cones K (SEP <= K <= maxCone, the domain of pairCone_eq_Q3_of_drive_maxCone)
survive when native operations are allowed to act with ONE extra register token, i.e. under
register consistency between 2 and 3 tokens, with no drive (hA) and no cyclic action?

Conventions. Token basis |0>,|1>; 3-token index 4*x1 + 2*x2 + x3. Matrices are Hermitian
operators identified with pair/3-token tables through the Pauli dictionary (H-CAR, retained,
unsourced). Native operations act by conjugation with permutation matrices (the fixed
identification of F2 memo G3). Everything is exact (SymPy Rational, I).

Premise names used below (all UNSOURCED; see LEDGER.md):
  H1_3   products of token states lie in K3
  MAX_3  K3 lies in maxCone_3 (pure product tests are nonnegative)
  NC_3   K3 is invariant under the native CNOTs into token 3 (or a native permutation of 8 configs)
  RO_3   the selective native readout branch (I x I x P_k) . (I x I x P_k) maps K3 into K3
  ATT    rho in K2  =>  rho (x) |0><0| in K3      (attach a ready meter)
  DIS    X in K3    =>  Tr_3 X in K2              (discard)

Blocks: A (fixtures), B (upper route: ATT+NC_3+MAX_3), C (lower route: H1_3+NC_3+RO_3+DIS),
D (controls and mutations). Each check prints PASS/FAIL; rc != 0 iff any FAIL.
"""
import itertools
import sys

import sympy as sp
from sympy import I, Rational as R, Matrix, eye, zeros

FAILS = []
NCHK = [0]


def check(label, cond):
    NCHK[0] += 1
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        FAILS.append(label)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def dag(m):
    return m.conjugate().T


def simp(m):
    return m.applyfunc(lambda e: sp.nsimplify(sp.expand(e)))


def is_zero(m):
    return all(sp.simplify(sp.expand(e)) == 0 for e in m)


def eigvals_exact(m):
    ev = m.eigenvals()
    return {sp.nsimplify(k): v for k, v in ev.items()}


I2 = eye(2)
X = Matrix([[0, 1], [1, 0]])
Y = Matrix([[0, -I], [I, 0]])
Z = Matrix([[1, 0], [0, -1]])
P0 = Matrix([[1, 0], [0, 0]])
P1 = Matrix([[0, 0], [0, 1]])
e0 = Matrix([1, 0])
e1 = Matrix([0, 1])


def perm_matrix(n, sigma):
    """sigma: dict config->config on range(n); P|y> = |sigma(y)>."""
    P = zeros(n, n)
    for y in range(n):
        P[sigma[y], y] = 1
    return P


def bits3(i):
    return ((i >> 2) & 1, (i >> 1) & 1, i & 1)


def idx3(b):
    return 4 * b[0] + 2 * b[1] + b[2]


def cnot3(c, t):
    sig = {}
    for i in range(8):
        b = list(bits3(i))
        if b[c]:
            b[t] ^= 1
        sig[i] = idx3(b)
    return perm_matrix(8, sig)


def ptrace3(M):
    """Trace out token 3 of an 8x8 matrix -> 4x4."""
    out = zeros(4, 4)
    for x in range(4):
        for y in range(4):
            out[x, y] = M[2 * x, 2 * y] + M[2 * x + 1, 2 * y + 1]
    return out


def pt2(M):
    """Partial transpose on token 2 of a 4x4 matrix (Gamma)."""
    out = zeros(4, 4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    out[2 * a + b, 2 * c + d] = M[2 * a + d, 2 * c + b]
    return out


def defect(s, t):
    return (eye(4) + s * kron(X, Z) + t * kron(Y, Y) - s * t * kron(Z, X)) / 4


ZF = {(s, t): defect(s, t) for s in (1, -1) for t in (1, -1)}

print("== A. pair fixtures ==")
# A1 defect spectra
for k, z in ZF.items():
    ev = eigvals_exact(z)
    check(f"A1 defect{k} Hermitian, trace 1, spectrum {{1/2:3,-1/2:1}}",
          z == dag(z) and z.trace() == 1 and ev == {R(1, 2): 3, R(-1, 2): 1})

# A2 every one of the 24 native pair permutations permutes Z_F
zf_list = list(ZF.values())
allperm_ok = True
for perm in itertools.permutations(range(4)):
    P = perm_matrix(4, dict(enumerate(perm)))
    for z in zf_list:
        img = P * z * P.T
        if not any(img == w for w in zf_list):
            allperm_ok = False
check("A2 all 24 native pair permutations map Z_F onto Z_F (so K(Z_F) is PC24-invariant)", allperm_ok)

# A3 block positivity of defects: bilinear coefficient matrix is a signed permutation, M^T M = I
for (s, t) in ZF:
    M = zeros(3, 3)
    M[0, 2] = s      # X(x)Z
    M[1, 1] = t      # Y(x)Y
    M[2, 0] = -s * t  # Z(x)X
    check(f"A3 defect({s},{t}): coefficient matrix orthogonal (|a.Mb|<=1 => <ab|z|ab>=(1+a.Mb)/4>=0) [EC+W]",
          M.T * M == eye(3))

# A4 P_m = I/2 - z_m is a rank-one projector in Q3, and z_m is in K(Z_F)* with Tr(z_m P_m) = -1/2
zm = ZF[(1, 1)]
Pm = eye(4) / 2 - zm
check("A4a P_m = I/2 - z_(1,1) is a rank-one projector (pure state in Q3)", simp(Pm * Pm - Pm) == zeros(4, 4) and Pm.trace() == 1)
gram_ok = all((zm * w).trace() >= 0 for w in zf_list)
check("A4b Tr(z_m z_j) >= 0 for all four defects (z_m in Z_F*, hence z_m in K(Z_F)* by L <= Z_F*) [EC+W]", gram_ok)
check("A4c Tr(z_m P_m) = -1/2 < 0, so P_m notin K(Z_F): Q3 is not contained in K(Z_F)", sp.simplify((zm * Pm).trace()) == R(-1, 2))
check("A4d z_m has eigenvalue -1/2, so K(Z_F) is not contained in Q3", R(-1, 2) in eigvals_exact(zm))

# Gamma(Bell) and the K_B generator, for later blocks
phi_plus = Matrix([1, 0, 0, 1])
B = phi_plus * dag(phi_plus) / 2
GB = pt2(B)
check("A5 Gamma(Phi+) = SWAP/2 has eigenvalue -1/2 (Gamma(Q3) not in Q3)", R(-1, 2) in eigvals_exact(GB))

print("== B. upper route: ATT + NC_3 (CNOTs into token 3) + MAX_3  =>  K2 <= Q3 ==")
C = cnot3(1, 2) * cnot3(0, 2)   # CNOT 1->3 then CNOT 2->3 (affine, 'CNOTs into a later token')
check("B0 C = CNOT23.CNOT13 is a permutation matrix and unitary", C * C.T == eye(8))

# B1 symbolic identity: <phi| C (Xm (x) |0><0|) C^dag |phi> = <u|Xm|u>, u = diag(c0,c1,c1,c0)(a (x) b)
a0, a1, b0, b1, c0, c1 = sp.symbols("a0 a1 b0 b1 c0 c1")
xs = sp.symbols("x0:16")
Xm = Matrix(4, 4, xs)
phi = kron(Matrix([a0, a1]), Matrix([b0, b1]), Matrix([c0, c1]))
lhs = (dag(phi) * C * kron(Xm, P0) * dag(C) * phi)[0, 0]
u = Matrix([a0 * b0 * c0, a0 * b1 * c1, a1 * b0 * c1, a1 * b1 * c0])
rhs = (dag(u) * Xm * u)[0, 0]
check("B1 symbolic: test value after (attach |0>, CNOT13, CNOT23) equals <u|X|u>, u = D_c(a(x)b), D_c=diag(c0,c1,c1,c0)",
      sp.expand(lhs - rhs) == 0)

# B2 density of the family u = D_c(a (x) b): any u with nonzero entries is reached (constructive, exact instance)
t2 = Matrix([1, 2, 8, 4])                              # u01*u10/(u00*u11) = 4 -> c1 = 2
cc0, cc1 = 1, 2
# a0 = 1, b0 = u00/c0, b1 = u01/c1, a1 = u10/(c1*b0)
B0v = t2[0] / cc0
B1v = t2[1] / cc1
A1v = t2[2] / (cc1 * B0v)
recon = Matrix([1 * B0v * cc0, 1 * B1v * cc1, A1v * B0v * cc1, A1v * B1v * cc0])
check("B2 constructive density instance: u = (1,2,8,4) equals D_c(a(x)b) with c=(1,2), a=(1,4), b=(1,1) [EC; general: W]",
      recon == t2)

# B3 exact witnesses: a negative product-test value on the native image of X (x) |0><0|
def three_token_value(Xmat, av, bv, cv, CC=C):
    ph = kron(av, bv, cv)
    return sp.nsimplify(sp.expand((dag(ph) * CC * kron(Xmat, P0) * dag(CC) * ph)[0, 0]))


ypl = Matrix([1, I])     # |+i> (unnormalized)
ymi = Matrix([1, -I])    # |-i>
xpl = Matrix([1, 1])
xmi = Matrix([1, -1])

wit = {}
# K(Z_F) defect z_(1,1)
v = three_token_value(zm, ypl, ymi, ypl)
wit["z(1,1)"] = v
check(f"B3a K(Z_F): z_(1,1) (x)|0><0| -> CNOT13,CNOT23 -> test |+i>|-i>|+i> gives {v} < 0 (8 = norm^2 of unnormalized test)",
      v.is_real and v < 0)
# all four defects
for k, z in ZF.items():
    best = None
    for av, bv, cv in itertools.product([xpl, xmi, ypl, ymi, e0, e1], repeat=3):
        val = three_token_value(z, av, bv, cv)
        if best is None or val < best:
            best = val
    check(f"B3b defect{k}: minimum over 216 sharp-axis product tests after (ATT, CNOT13, CNOT23) is {best} < 0", best < 0)
# Gamma(Bell)
v = None
best = None
for av, bv, cv in itertools.product([xpl, xmi, ypl, ymi, e0, e1], repeat=3):
    val = three_token_value(GB, av, bv, cv)
    if best is None or val < best:
        best = val
check(f"B3c Gamma(Phi+) (generator of K_Gamma, element of Gamma(Q3)): minimum over the same 216 tests is {best} < 0", best < 0)

# B4 general non-affine route (exact, no density): sigma maps {(x,0)} onto the weight<=1 set T
T = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
slice0 = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)]   # (x1,x2,0) for x = 00,01,10,11
rest_src = [b for b in itertools.product((0, 1), repeat=3) if b not in slice0]
rest_dst = [b for b in itertools.product((0, 1), repeat=3) if b not in T]
sig = {idx3(s_): idx3(t_) for s_, t_ in zip(slice0, T)}
sig.update({idx3(s_): idx3(t_) for s_, t_ in zip(rest_src, rest_dst)})
Ptoff = perm_matrix(8, sig)
aff = True
# affine test: sigma is affine iff sigma(x)+sigma(y)+sigma(z)+sigma(x+y+z) = 0 for all x,y,z
for p, q, r_ in itertools.product(range(8), repeat=3):
    s4 = sig[p] ^ sig[q] ^ sig[r_] ^ sig[p ^ q ^ r_]
    if s4 != 0:
        aff = False
        break
check("B4a sigma (slice x3=0 -> weight<=1 set) is a native permutation of 8 configs that is NOT affine", not aff)
u1, u2, u3 = sp.symbols("u1 u2 u3")
phiT = kron(Matrix([1, u1]), Matrix([1, u2]), Matrix([1, u3]))
lhsT = sp.expand((dag(phiT) * Ptoff * kron(Xm, P0) * dag(Ptoff) * phiT)[0, 0])
uT = Matrix([1, u1, u2, u3])
rhsT = sp.expand((dag(uT) * Xm * uT)[0, 0])
check("B4b symbolic: after (attach |0>, sigma) the product test (1,u1)(x)(1,u2)(x)(1,u3) reads <u|X|u>, u=(1,u1,u2,u3): every u with u_00 != 0, exactly",
      sp.expand(lhsT - rhsT) == 0)
# exact instance for P_m-type and K(Z_F): eigenvector of z_m for -1/2
ev_neg = (zm - R(-1, 2) * eye(4)).nullspace()[0]
check("B4c the -1/2 eigenvector of z_(1,1) has a nonzero first entry (so B4b applies with no density step)", ev_neg[0] != 0)
evn = simp(ev_neg / ev_neg[0])
valT = sp.nsimplify(sp.expand((dag(kron(Matrix([1, evn[1]]), Matrix([1, evn[2]]), Matrix([1, evn[3]]))) * Ptoff * kron(zm, P0) * dag(Ptoff) * kron(Matrix([1, evn[1]]), Matrix([1, evn[2]]), Matrix([1, evn[3]])))[0, 0]))
check(f"B4d non-affine route on z_(1,1): value {valT} = -1/2 * |u|^2 < 0", valT == R(-1, 2) * sp.nsimplify(sp.expand((dag(evn) * evn)[0, 0])))

print("== C. lower route: H1_3 + NC_3 + RO_3 + DIS  =>  pure states in K2 ==")
# C1 symbolic: (I (x) I (x) P0) C |a b c> = (D_c(a(x)b)) (x) |0>, then discard -> |u><u|
ket = kron(Matrix([a0, a1]), Matrix([b0, b1]), Matrix([c0, c1]))
branch = kron(I2, I2, P0) * C * ket
expect = kron(u, e0)
check("C1 symbolic: selective readout 0 on token 3 after CNOT13,CNOT23 gives D_c(a(x)b) (x)|0>", sp.expand(branch - expect) == zeros(8, 1))
rho_out = ptrace3(branch * dag(branch))
check("C1b discard of that branch is |u><u|", sp.expand(rho_out - u * dag(u)) == zeros(4, 4))


def gen_affine(av, bv, cv):
    k_ = kron(av, bv, cv)
    br = kron(I2, I2, P0) * C * k_
    return simp(ptrace3(br * dag(br)))


# C2 targets excluded from x-screen fixtures
singlet = Matrix([0, 1, -1, 0])
out = gen_affine(xpl, Matrix([-1, 1]), Matrix([0, 1]))
check("C2a P_singlet (absent from K_H*) generated exactly: a=(1,1), b=(-1,1), c=(0,1)", out == singlet * dag(singlet))
out = gen_affine(xpl, xpl, e0)
check("C2b Phi+ (absent from K_S, which fails MI) generated exactly: a=b=(1,1), c=(1,0)", out == phi_plus * dag(phi_plus))
czpp = Matrix([1, 1, 1, -1])
outT = None
# non-affine route for CZ|++> and for P_m (exact, no density step)


def gen_nonaffine(uvec):
    uvec = simp(uvec / uvec[0])
    k_ = kron(Matrix([1, uvec[1]]), Matrix([1, uvec[2]]), Matrix([1, uvec[3]]))
    br = kron(I2, I2, P0) * dag(Ptoff) * k_      # apply sigma^{-1}: weight<=1 set -> slice x3=0
    return simp(ptrace3(br * dag(br))), uvec


outT, un = gen_nonaffine(czpp)
check("C2c CZ|++> (not a native-permutation image of a product: no pairing of its entries has equal products [W]) generated exactly via the non-affine native sigma^-1", outT == un * dag(un))
outT, un = gen_nonaffine(evn)
check("C2d P_m (pure state absent from K(Z_F), A4c) generated exactly via sigma^-1", simp(outT - un * dag(un)) == zeros(4, 4))
check("C2e and it is proportional to P_m", simp(outT * Pm - outT) == zeros(4, 4) and outT != zeros(4, 4))

print("== D. controls and mutations ==")
# D1 positive control: Q3 satisfies the route premises: C unitary, readout branches and discards are CP
check("D1a C is unitary, so Ad_C maps PSD to PSD (QK3 satisfies NC_3)", C * dag(C) == eye(8))
rho_q = Matrix([[R(1, 2), R(1, 4), 0, R(1, 8)], [R(1, 4), R(1, 4), 0, 0], [0, 0, R(1, 8), 0], [R(1, 8), 0, 0, R(1, 8)]])
check("D1b sample rational rho is PSD (positive control input)", rho_q.is_positive_semidefinite)
img = simp(C * kron(rho_q, P0) * dag(C))
check("D1c its native 3-token image is PSD (no false exclusion of Q3)", img.is_positive_semidefinite)
minq = min(three_token_value(rho_q, av, bv, cv) for av, bv, cv in itertools.product([xpl, xmi, ypl, ymi, e0, e1], repeat=3))
check(f"D1d minimum over the 216 tests on the Q3 sample is {minq} >= 0", minq >= 0)
# D2 classical cone: satisfies the upper route, fails the lower route
diagX = sp.diag(R(1, 2), R(1, 6), R(1, 6), R(1, 6))
imgd = simp(C * kron(diagX, P0) * dag(C))
check("D2a classical: native image of a diagonal state stays diagonal and nonnegative (upper route excludes nothing classical)",
      all(imgd[i, j] == 0 for i in range(8) for j in range(8) if i != j) and all(imgd[i, i] >= 0 for i in range(8)))
check("D2b classical: lower route output Phi+ is not diagonal (classical cone excluded by H1_3+NC_3+RO_3+DIS; it already fails H1)",
      gen_affine(xpl, xpl, e0)[0, 3] != 0)
# D3 locality control: without a native coupling into token 3, no exclusion
Cid = eye(8)
mn = min(three_token_value(zm, av, bv, cv, Cid) for av, bv, cv in itertools.product([xpl, xmi, ypl, ymi, e0, e1], repeat=3))
check(f"D3a control: identity in place of C (spectator token 3) gives minimum {mn} >= 0 over the 216 tests", mn >= 0)
C13 = cnot3(0, 2)
lhs13 = sp.expand((dag(phi) * C13 * kron(Xm, P0) * dag(C13) * phi)[0, 0])
uprod = kron(Matrix([a0 * c0, a1 * c1]), Matrix([b0, b1]))
check("D3b control: CNOT13 alone yields a PRODUCT test vector (a*c)(x)b, so it cannot exclude any maxCone element [EC+W]",
      sp.expand(lhs13 - (dag(uprod) * Xm * uprod)[0, 0]) == 0)
locmin = None
for perm in itertools.permutations(range(4)):
    Pp = kron(perm_matrix(4, dict(enumerate(perm))), I2)
    for av, bv, cv in itertools.product([xpl, ypl, ymi, e0], repeat=3):
        val = three_token_value(zm, av, bv, cv, Pp)
        locmin = val if locmin is None or val < locmin else locmin
check(f"D3c control: the 24 pair permutations (x) id on token 3 give minimum {locmin} >= 0 (exclusion needs coupling into the extra token)",
      locmin >= 0)
# D4 which token tests carry the exclusion
mnr = min(three_token_value(zm, av, bv, cv) for av, bv, cv in itertools.product([xpl, xmi, ypl, ymi, e0, e1], [xpl, xmi, ypl, ymi, e0, e1], [xpl, xmi]))
check(f"D4a mutation: ancilla tests restricted to the x-axis states give minimum {mnr} >= 0 over that family (the axis witness of B3a uses a non-real ancilla test)",
      mnr >= 0)
vr = three_token_value(zm, Matrix([2, 1]), Matrix([1, 2]), Matrix([3, 1]))
check(f"D4b real non-axis tests suffice for the real fixture z_(1,1): a=(2,1), b=(1,2), c=(3,1) give {vr} < 0 (normalized {vr / 250})",
      vr < 0)
mnc = min(three_token_value(z, av, bv, cv) for z in zf_list + [GB] for av, bv, cv in itertools.product([e0, e1], repeat=3))
check(f"D4c configuration-only tests (all three tokens in {{|0>,|1>}}) give minimum {mnc} >= 0 on every defect and on Gamma(Phi+): the exclusion needs non-configuration token tests",
      mnc >= 0)
# D5 Gamma kill test (fixed identification): Gamma-transported CNOT action is not conjugation by a permutation
Gam3 = lambda M: Matrix(8, 8, lambda i, j: M[idx3((bits3(i)[0], bits3(j)[1], bits3(i)[2])), idx3((bits3(j)[0], bits3(i)[1], bits3(j)[2]))])
Eij = zeros(8, 8)
Eij[idx3((0, 1, 0)), idx3((1, 0, 0))] = 1
imgG = Gam3(C * Gam3(Eij) * dag(C))
check("D5a the Gamma(token 2)-transported action of the same native bijection differs from Ad_C on a matrix unit",
      imgG != C * Eij * dag(C))
diag_ok = True
for k_ in range(8):
    Ek = zeros(8, 8)
    Ek[k_, k_] = 1
    if Gam3(C * Gam3(Ek) * dag(C)) != C * Ek * dag(C):
        diag_ok = False
check("D5b ... while agreeing with Ad_C on every configuration-diagonal matrix unit: the exclusion of Gamma(Q3) holds relative to the fixed identification only",
      diag_ok)

print("== E. ingredients of the drop-one models (LEDGER.md section 4.4) ==")
# For g in G = <CNOT13, CNOT23> and any token state tau: Tr_3[g (M (x) tau) g^dag] = (1+r)/2 M + (1-r)/2 Z_l M Z_l,
# r = 2 Re tau01, Z_l a LOCAL unitary (Z(x)I, I(x)Z, Z(x)Z or I). Local unitaries preserve maxCone and SEP, so
# discards of G-images of maxCone(x)tau (resp. products) stay in maxCone (resp. SEP).
t00, t11 = sp.symbols("t00 t11", real=True)
t01 = sp.Symbol("t01")
tau = Matrix([[t00, t01], [sp.conjugate(t01), t11]])
rr = t01 + sp.conjugate(t01)
G = {"I": (eye(8), eye(4)), "CNOT13": (cnot3(0, 2), kron(Z, I2)), "CNOT23": (cnot3(1, 2), kron(I2, Z)), "C": (C, kron(Z, Z))}
for name, (g, Zl) in G.items():
    lhsE = ptrace3(g * kron(Xm, tau) * dag(g))
    if name == "I":
        rhsE = (t00 + t11) * Xm
    else:
        rhsE = (t00 + t11 + rr) / 2 * Xm + (t00 + t11 - rr) / 2 * Zl * Xm * Zl
    check(f"E1 discard formula for g = {name} (symbolic M, tau)", sp.expand(lhsE - rhsE) == zeros(4, 4))
# the selective readout branch is what breaks it: branch k of C(M (x) |c><c|)C^dag is D M D^dag, D = diag(c_{k+p(x)})
kk = 0
brE = ptrace3(kron(I2, I2, P0) * C * kron(Xm, Matrix([c0, c1]) * dag(Matrix([c0, c1]))) * dag(C) * kron(I2, I2, P0))
Dc = sp.diag(c0, c1, c1, c0)
check("E2 readout branch 0 of C(M (x)|c><c|)C^dag, discarded, equals D_c M D_c^dag (the filter of block B)",
      sp.expand(brE - Dc * Xm * dag(Dc)) == zeros(4, 4))

print(f"== SUMMARY: {NCHK[0]} checks, {len(FAILS)} FAIL ==")
sys.exit(1 if FAILS else 0)
