"""Independent exact audit of EQ3-P's six-copy results, its cheap foil C_H and the M_bs exclusion, plus two
hidden-assumption probes (coordinator; research only, base bcbc516f).

Imports nothing from scratchpad/eq3/P.  Operator form throughout (qubits ordered 0..5; triples (0,1,2), (3,4,5);
link pairs (0,3), (1,4), (2,5)); the kernel cnot, homMap and nflip are typed in as in audit_eq3_n1.py.
Usage:  python3 -I -B audit_eq3_n2.py

DECISION RULES (fixed before the first run; rules, not expected numbers):
  S  six-copy calculus: (S1) my index-sum conditional cond6(L03, L14, L25; F345) equals the explicit 64 x 64 partial
     trace tr_345[(1 (x) F)(L03 (x) L14 (x) L25)] on an exact Gaussian-rational instance; (S2) rank-one links with
     coefficients C, C', C'' give (C (x) C' (x) C'') F^T (C (x) C' (x) C'')^dag (symbolic F, exact C's) and a symbolic
     filter diag(1,u) on copy 0 with Bell links on copies 1, 2 gives Ad(diag(1,u) (x) 1 (x) 1)(F^T) (symbolic F, u);
     (S3) Bell links give F^T (symbolic F); (S4) Bell effects on the three link pairs give tr(X Y^T) (symbolic X, Y).
  B  M_bs exclusion under triple-level uniformity: (B1) GHZ is invariant under the six qubit permutations; for
     A|BC-biseparable pure a (x) chi, 1/2 (|a|^2 |chi|^2) - |<GHZ|a chi>|^2 is the sum of squares
     (1/2)(|a0|^2 + |a1|^2)(sum over the off-support entries of chi) + (1/2)|a0 chi11 - a1 chi00|^2 (symbolic), so
     W3 = 1/2 - GHZ is in BS* (biseparable hull dual), and GHZ (PSD) is in BS*; (B2) the six-copy value
     tr[(W3 (x) GHZ)(Phi+03 (x) Phi+14 (x) Phi+25)] is negative; (B3) control: a biseparable state in place of GHZ gives
     a nonnegative value.
  U  hidden assumption (triple-level uniformity), NOTE-level findings with exact ingredients: (U1) W3 has eigenvalue
     -1/2, so W3 is not in BS (BS <= PSD): when the triple (0,1,2) carries BS* and (3,4,5) carries BS, the B2 witness
     is not an effect of (0,1,2); (U2) the four-token group (1,4,2,5) effect G = Ad(CNOT_12)(Omega14 (x) Omega25)
     satisfies tr[(Omega03 (x) G)(x012 (x) y345)] = tr(x . Ad(CNOT)(y^T)) (three exact Gaussian-rational instances),
     and with x = W3 (in BS*), y = Phi+34 (x) |0><0|5 (in BS) the value is negative: through the full effect set of
     that group, IF G is one of its effects, the non-uniform assignment (BS*, BS) is excluded and K345 is forced to be
     Ad(CNOT)-invariant on (4,5) (written; the identity is the evidence).
  H  the order-8 foil C_H: (H1) the table maps of Ad(CNOT), Ad(X (x) 1), Ad(1 (x) X) in my dictionary equal the
     kernel cnot, actC nflip, actT nflip; the generated group has order 8; (H2) over the orbit of psi psi^dag
     (psi = (1,1,1,2)/sqrt7) the largest marginal Bloch norm^2 is < (24/25)^2; countercontrol: a product state's orbit
     reaches 1; (H3) the four-copy value with w = (49/50) 1 - psi psi^dag, f = psi psi^dag, Bell links is negative.
  Y  Cayley hyperdeterminant (my transcription): Det(GHZ) != 0, Det(W) = 0, Det(|0>(|00> + |11>)) = 0, and
     Det((C0 (x) C1 (x) C2) psi) = (det C0 det C1 det C2)^2 Det(psi) on two exact random instances.
VERDICT `AUDIT-EQ3-N2-EXACT` iff every check passes; otherwise VERDICT NOT RENDERED.  Exact arithmetic only.
"""
import itertools
import random
import sys
from functools import reduce

import sympy as sp
from sympy import I, Matrix, Rational as R, eye, zeros

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def note(text):
    print("NOTE " + text)
    sys.stdout.flush()


def Z(M):
    return M.applyfunc(sp.expand).is_zero_matrix


def kron(*Ms):
    return reduce(sp.kronecker_product, Ms)


def exact(*Ms):
    return all(not sp.Matrix(M).atoms(sp.Float) for M in Ms)


rng = random.Random(20261008 + 2)
s0, sx = eye(2), Matrix([[0, 1], [1, 0]])
sy, sz = Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def proj(v):
    return (v * v.H).applyfunc(sp.expand)


def herm(p, n):
    a = sp.symbols(p + "0:%d" % (n * n), real=True)
    M = zeros(n, n)
    k = 0
    for r in range(n):
        M[r, r] = a[k]
        k += 1
    for r in range(n):
        for c in range(r + 1, n):
            M[r, c] = a[k] + I * a[k + 1]
            M[c, r] = a[k] - I * a[k + 1]
            k += 2
    return M


def rgauss(n, m=None, lo=-3, hi=3):
    m = n if m is None else m
    return Matrix(n, m, lambda i, j: R(rng.randint(lo, hi), rng.randint(1, 3)) + I * R(rng.randint(lo, hi), 2))


# ------------------------------------------------------------------ S six-copy calculus
B3 = list(itertools.product(range(2), repeat=3))


def i3(b):
    return 4 * b[0] + 2 * b[1] + b[2]


def i6(b):
    return sum(v << (5 - q) for q, v in enumerate(b))


def cond6_sum(L03, L14, L25, F345):
    out = zeros(8, 8)
    for ii in B3:
        for jj in B3:
            s = 0
            for kk in B3:              # row indices of the second triple
                for ll in B3:          # column indices of the second triple
                    s += (L03[2 * ii[0] + kk[0], 2 * jj[0] + ll[0]] * L14[2 * ii[1] + kk[1], 2 * jj[1] + ll[1]]
                          * L25[2 * ii[2] + kk[2], 2 * jj[2] + ll[2]] * F345[i3(ll), i3(kk)])
            out[i3(ii), i3(jj)] = s
    return out.applyfunc(sp.expand)


def links6(L03, L14, L25):
    M = zeros(64, 64)
    B6 = list(itertools.product(range(2), repeat=6))
    for a in B6:
        for b in B6:
            M[i6(a), i6(b)] = (L03[2 * a[0] + a[3], 2 * b[0] + b[3]] * L14[2 * a[1] + a[4], 2 * b[1] + b[4]]
                               * L25[2 * a[2] + a[5], 2 * b[2] + b[5]])
    return M


def herm_num(n):
    G = rgauss(n)
    return (G + G.H).applyfunc(sp.expand)


Ln = [herm_num(4) for _ in range(3)]
Fn = herm_num(8)
M6 = links6(*Ln)
cond_exp = Matrix(8, 8, lambda r, c: sp.expand(sum(Fn[k, kp] * M6[8 * r + kp, 8 * c + k]
                                                   for k in range(8) for kp in range(8))))
check("S1 the index-sum six-copy conditional equals the explicit 64 x 64 partial trace tr_345[(1 (x) F)(L03 (x) L14 "
      "(x) L25)] (exact Gaussian-rational instance)", Z(cond_exp - cond6_sum(*Ln, Fn)) and exact(cond_exp))
Fs = herm("f", 8)
Cn = [rgauss(2) for _ in range(3)]


def vec2(C):
    return Matrix([C[0, 0], C[0, 1], C[1, 0], C[1, 1]])


Kc = kron(*Cn)
ur, ui = sp.symbols("ur ui", real=True)
u = ur + I * ui
OM = Matrix([1, 0, 0, 1])
OMP = OM * OM.T
Du = sp.diag(1, u)
Kd = kron(Du, eye(2), eye(2))
check("S2 rank-one links with coefficients C, C', C'' give (C (x) C' (x) C'') F^T (C (x) C' (x) C'')^dag (symbolic F, "
      "exact C's), and a filter diag(1,u) on copy 0 with Bell links on copies 1, 2 gives Ad(diag(1,u) (x) 1 (x) 1)(F^T) "
      "(symbolic F, u)",
      Z(cond6_sum(*[proj(vec2(C)) for C in Cn], Fs) - Kc * Fs.T * Kc.H)
      and Z(cond6_sum(proj(vec2(Du)), OMP, OMP, Fs) - Kd * Fs.T * Kd.H))
check("S3 Bell links |Omega><Omega| on (0,3), (1,4), (2,5) give the conditional F^T (symbolic F): T3(K345*) <= K012 "
      "with closedness", Z(cond6_sum(OMP, OMP, OMP, Fs) - Fs.T))
Xs, Ys = herm("x", 8), herm("y", 8)
val_bell = 0
for a in B3:
    for b in B3:
        # nonzero entries of Omega03 Omega14 Omega25: row (a, a), column (b, b)
        val_bell += Xs[i3(b), i3(a)] * Ys[i3(b), i3(a)]
check("S4 Bell effects on (0,3), (1,4), (2,5) give tr[(Omega Omega Omega)(X012 (x) Y345)] = tr(X Y^T) (symbolic X, Y; "
      "the 64 nonzero entries of the effect are those with equal link indices): K012 <= T3(K345*)",
      sp.expand(val_bell - (Xs * Ys.T).trace()) == 0)

# ------------------------------------------------------------------ B M_bs exclusion (uniform triples)
GHZv = Matrix([1, 0, 0, 0, 0, 0, 0, 1]) / sp.sqrt(2)
GHZ = proj(GHZv).applyfunc(sp.nsimplify)


def perm_op(p):                                 # permutation of three qubits as an 8 x 8 matrix
    P = zeros(8, 8)
    for b in B3:
        P[i3([b[p[0]], b[p[1]], b[p[2]]]), i3(b)] = 1
    return P


ok_perm = all(perm_op(p) * GHZ * perm_op(p).T == GHZ for p in itertools.permutations(range(3)))
a0r, a0i, a1r, a1i = sp.symbols("a0r a0i a1r a1i", real=True)
ch = sp.symbols("cr0:4", real=True), sp.symbols("ci0:4", real=True)
a = Matrix([a0r + I * a0i, a1r + I * a1i])
chi = Matrix([ch[0][k] + I * ch[1][k] for k in range(4)])
psi_bs = kron(a, chi)
fid = sp.expand((GHZv.H * psi_bs)[0, 0] * sp.conjugate((GHZv.H * psi_bs)[0, 0]))
na = sp.expand((a.H * a)[0, 0])
nchi = sp.expand((chi.H * chi)[0, 0])
off = sp.expand(sum(chi[k] * sp.conjugate(chi[k]) for k in (1, 2)))
lag = sp.expand((a[0] * chi[3] - a[1] * chi[0]) * sp.conjugate(a[0] * chi[3] - a[1] * chi[0]))
check("B1 GHZ is invariant under the six qubit permutations, and for A|BC-biseparable a (x) chi: "
      "(1/2)|a|^2|chi|^2 - |<GHZ|a chi>|^2 = (1/2)|a|^2(|chi01|^2 + |chi10|^2) + (1/2)|a0 chi11 - a1 chi00|^2 "
      "(symbolic), so W3 = 1/2 - GHZ is in BS*",
      ok_perm and sp.expand(R(1, 2) * na * nchi - fid - (R(1, 2) * na * off + R(1, 2) * lag)) == 0)
PHI = proj(OM / sp.sqrt(2)).applyfunc(sp.nsimplify)
W3 = R(1, 2) * eye(8) - GHZ
cond_ghz = cond6_sum(PHI, PHI, PHI, GHZ)
v_bs = sp.expand((W3 * cond_ghz).trace())
check("B2 six-copy value tr[(W3 (x) GHZ)(Phi+03 Phi+14 Phi+25)] = tr(W3 GHZ^T)/8 = %s < 0: with BS on both triples "
      "the instance fails" % v_bs, v_bs < 0 and Z(cond_ghz - GHZ.T / 8))
bis = kron(proj(Matrix([1, 0])), proj(OM / sp.sqrt(2))).applyfunc(sp.nsimplify)
v_ctrl = sp.expand((W3 * cond6_sum(PHI, PHI, PHI, bis)).trace())
check("B3 control: a biseparable state |0><0| (x) Phi+ in place of GHZ gives %s >= 0" % v_ctrl, v_ctrl >= 0)

# ------------------------------------------------------------------ U the triple-level uniformity probes
ev = W3.eigenvals()
check("U1 W3 = 1/2 - GHZ has eigenvalue -1/2, so W3 is not in BS (BS <= PSD8): with BS* on (0,1,2) and BS on "
      "(3,4,5), the B2 witness is not an effect of (0,1,2)  [eigenvalues %s]" % dict(sorted(ev.items())),
      R(-1, 2) in ev)


def place(ops_by_qubits, n=6):
    """Tensor product of operators placed on disjoint qubit tuples; returns the 2^n x 2^n matrix."""
    M = zeros(2 ** n, 2 ** n)
    Bn = list(itertools.product(range(2), repeat=n))
    for x in Bn:
        for y in Bn:
            v = 1
            for qs, op in ops_by_qubits:
                r = sum(x[q] << (len(qs) - 1 - k) for k, q in enumerate(qs))
                c = sum(y[q] << (len(qs) - 1 - k) for k, q in enumerate(qs))
                v *= op[r, c]
                if v == 0:
                    break
            M[i6(x), i6(y)] = v
    return M


C12 = place([((1, 2), CNOT), ((0,), eye(2)), ((3,), eye(2)), ((4,), eye(2)), ((5,), eye(2))])
LINKS = place([((0, 3), OMP), ((1, 4), OMP), ((2, 5), OMP)])
EFF_G = C12 * LINKS * C12.T                     # Omega03 (x) Ad(CNOT_12)(Omega14 (x) Omega25)
EFF_NZ = [(i, j, EFF_G[i, j]) for i in range(64) for j in range(64) if EFF_G[i, j] != 0]


def tr_eff(x8, y8):                             # tr[E (x8 (x) y8)] over the nonzero entries of E
    return sp.expand(sum(v * x8[j // 8, i // 8] * y8[j % 8, i % 8] for i, j, v in EFF_NZ))


CN3 = kron(eye(2), CNOT)                        # CNOT on qubits (1, 2) of a triple
ok_lever = True
for _ in range(3):
    x8, y8 = herm_num(8), herm_num(8)
    ok_lever &= sp.expand(tr_eff(x8, y8) - (x8 * (CN3 * y8.T * CN3.T)).trace()) == 0
y_bs = kron(proj(OM / sp.sqrt(2)), proj(Matrix([1, 0]))).applyfunc(sp.nsimplify)
v_lever = tr_eff(W3, y_bs)
check("U2 the four-token effect Omega03 (x) Ad(CNOT_12)(Omega14 (x) Omega25) pairs as tr[E (x012 (x) y345)] = "
      "tr(x Ad(CNOT)(y^T)) (3 exact instances), and with x = W3 (in BS*), y = Phi+34 (x) |0><0|5 (in BS) the value is "
      "%s < 0" % v_lever, ok_lever and v_lever < 0)
note("U2 reading: the six-copy families of the thread use only product effects of the link pairs; the full effect set "
     "of the four-token group (1,4,2,5) would add E = Ad(CNOT_12)(Omega14 Omega25) IF it is an effect of that group "
     "(true when its cone lies in PSD16). With it, KT(6) excludes the non-uniform (BS*, BS) and forces Ad(CNOT) "
     "invariance of K345 on (4,5), i.e. IE2 for cnot; sourcing that effect is an effect-level idle extension at four "
     "tokens, so the wall moves up one level and is not closed")

# ------------------------------------------------------------------ H the order-8 foil C_H
def sgn_hand(m, n):
    return -1 if (m == 1 and n == 3) or (m == 2 and n == 2) else 1


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]


def coords(rho):
    return Matrix(4, 4, lambda m, n: sp.expand((rho * SS[m][n]).trace()))


def pauli(T):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            out += T[m, n] * SS[m][n]
    return out / 4


def tab_matrix(f):
    M = zeros(16, 16)
    for k in range(16):
        E = zeros(4, 4)
        E[k // 4, k % 4] = 1
        img = f(E)
        for j in range(16):
            M[j, k] = img[j // 4, j % 4]
    return M


def H(A):
    M = eye(4)
    M[1:, 1:] = A
    return M


NFLIP = sp.diag(1, -1, -1)
k_cnot = tab_matrix(lambda T: Matrix(4, 4, lambda m, n: sgn_hand(m, n) * T[PC[m][n], PT[m][n]]))
k_actC = tab_matrix(lambda T: H(NFLIP) * T)
k_actT = tab_matrix(lambda T: T * H(NFLIP).T)
GENU = [CNOT, kron(sx, s0), kron(s0, sx)]
GEN = [tab_matrix(lambda T, U=U: coords(U * pauli(T) * U.H)) for U in GENU]
key = lambda M: tuple(int(v) for v in M)
seen = {key(eye(16)): eye(16)}
frontier = [eye(16)]
while frontier:
    nxt = []
    for M in frontier:
        for g in GEN:
            P_ = g * M
            if key(P_) not in seen:
                seen[key(P_)] = P_
                nxt.append(P_)
    frontier = nxt
check("H1 Ad(CNOT), Ad(X (x) 1), Ad(1 (x) X) act on tables as the kernel cnot, actC nflip, actT nflip; the group they "
      "generate has order %d" % len(seen),
      GEN[0] == k_cnot and GEN[1] == k_actC and GEN[2] == k_actT and len(seen) == 8)
psi = Matrix([1, 1, 1, 2])
rho_psi = psi * psi.T / 7
tvec = Matrix([coords(rho_psi)[k // 4, k % 4] for k in range(16)])


def bloch_max(v):
    best = 0
    for M in seen.values():
        w = M * v
        best = max(best, w[4] ** 2 + w[8] ** 2 + w[12] ** 2, w[1] ** 2 + w[2] ** 2 + w[3] ** 2)
    return best


bm = bloch_max(tvec)
pt_ = coords(kron(proj(Matrix([1, 0])), proj(Matrix([1, 0]))))
bm_p = bloch_max(Matrix([pt_[k // 4, k % 4] for k in range(16)]))
check("H2 over the 8-element orbit of psi psi^dag the largest marginal Bloch norm^2 is %s < (24/25)^2, so w = (49/50) "
      "1 - psi psi^dag is in C_H*; countercontrol: a product state's orbit reaches %s" % (bm, bm_p),
      bm < R(24, 25) ** 2 and bm_p == 1)


def cond4(L02, L13, F23):
    out = zeros(4, 4)
    for i0, i1, j0, j1 in itertools.product(range(2), repeat=4):
        s = 0
        for i2, i3_, j2, j3 in itertools.product(range(2), repeat=4):
            s += L02[2 * i0 + i2, 2 * j0 + j2] * L13[2 * i1 + i3_, 2 * j1 + j3] * F23[2 * j2 + j3, 2 * i2 + i3_]
        out[2 * i0 + i1, 2 * j0 + j1] = s
    return out.applyfunc(sp.expand)


v_h = sp.expand(((R(49, 50) * eye(4) - rho_psi) * cond4(PHI, PHI, rho_psi)).trace())
check("H3 the four-copy value tr[(w01 (x) f23)(Phi+02 (x) Phi+13)] = %s < 0 with f = psi psi^dag (PSD, so in C_H* "
      "since C_H <= PSD) and Phi+ = Ad(CNOT)(|+><+| (x) |0><0|) in C_H" % v_h,
      v_h < 0 and Z(CNOT * kron(proj(Matrix([1, 1]) / sp.sqrt(2)), proj(Matrix([1, 0]))) * CNOT.T - PHI))

# ------------------------------------------------------------------ Y Cayley hyperdeterminant
def hyperdet(p):
    a_ = lambda i, j, k: p[4 * i + 2 * j + k]
    return sp.expand(a_(0, 0, 0) ** 2 * a_(1, 1, 1) ** 2 + a_(0, 0, 1) ** 2 * a_(1, 1, 0) ** 2
                     + a_(0, 1, 0) ** 2 * a_(1, 0, 1) ** 2 + a_(1, 0, 0) ** 2 * a_(0, 1, 1) ** 2
                     - 2 * (a_(0, 0, 0) * a_(0, 0, 1) * a_(1, 1, 0) * a_(1, 1, 1)
                            + a_(0, 0, 0) * a_(0, 1, 0) * a_(1, 0, 1) * a_(1, 1, 1)
                            + a_(0, 0, 0) * a_(1, 0, 0) * a_(0, 1, 1) * a_(1, 1, 1)
                            + a_(0, 0, 1) * a_(0, 1, 0) * a_(1, 0, 1) * a_(1, 1, 0)
                            + a_(0, 0, 1) * a_(1, 0, 0) * a_(0, 1, 1) * a_(1, 1, 0)
                            + a_(0, 1, 0) * a_(1, 0, 0) * a_(0, 1, 1) * a_(1, 0, 1))
                     + 4 * (a_(0, 0, 0) * a_(0, 1, 1) * a_(1, 0, 1) * a_(1, 1, 0)
                            + a_(0, 0, 1) * a_(0, 1, 0) * a_(1, 0, 0) * a_(1, 1, 1)))


ghz_u = Matrix([1, 0, 0, 0, 0, 0, 0, 1])
w_u = Matrix([0, 1, 1, 0, 1, 0, 0, 0])
bis_u = kron(Matrix([1, 0]), Matrix([1, 0, 0, 1]))
ok_cov = True
for _ in range(2):
    Cs = [rgauss(2) for _ in range(3)]
    pv = rgauss(8, 1)
    lhs = hyperdet(kron(*Cs) * pv)
    rhs = sp.expand((Cs[0].det() * Cs[1].det() * Cs[2].det()) ** 2 * hyperdet(pv))
    ok_cov &= sp.expand(lhs - rhs) == 0
check("Y my Cayley hyperdeterminant: Det(|000> + |111>) = %s != 0, Det(W) = %s, Det(|0>(|00> + |11>)) = %s, and "
      "Det((C0 (x) C1 (x) C2) psi) = (det C0 det C1 det C2)^2 Det(psi) (2 exact random instances)"
      % (hyperdet(ghz_u), hyperdet(w_u), hyperdet(bis_u)),
      hyperdet(ghz_u) != 0 and hyperdet(w_u) == 0 and hyperdet(bis_u) == 0 and ok_cov)

npass = sum(1 for _, c in checks if c)
print("--- audit_eq3_n2: %d/%d checks pass" % (npass, len(checks)))
print("VERDICT AUDIT-EQ3-N2-EXACT" if npass == len(checks) else "VERDICT NOT RENDERED")
