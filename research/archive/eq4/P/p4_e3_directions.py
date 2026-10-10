"""EQ4-P probe p4 -- coordinator expectation E3 (the Choi lever), one direction at a time, exact.  Research only.

Usage:  python3 -I -B p4_e3_directions.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py.

Statements (aligned c = 0, uniform co-self-dual hierarchy derived by p1/p2).
  (i)   K3 = PSD8.          (ii)  K3 contains a GHZ-class state (Cayley hyperdeterminant != 0).
  (iii) K4 contains the CNOT Choi state C = |c><c|, c = sum_ab |a>_in1 |b>_in2 |a>_out1 |a+b>_out2.
  (iv)  K3 is invariant under the native gate on two of its tokens (IE2 for the gate).
Each direction gets its own witness (section A.34); the cycle is (i)=>(iii)=>(iv)=>(ii)=>(i), plus (i)=>(iv).

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P4-E3-DIRECTIONS-EXACT` iff all:
  K   transcription control; the kernel cnot acting on the first two indices of a three-token table equals Ad(CNOT (x) 1)
      in the Pauli dictionary on all 64 unit tables (the native gate on two tokens of a triple).
  IV2 (iv)=>(ii) witness: Ad(CNOT_01)(|+><+|_0 (x) Phi+_12) = |psi><psi| with psi = (|000>+|011>+|101>+|110>)/2, and
      Det(psi) != 0; control: Det(GHZ) != 0, Det(W) = 0, Det(|0>(|00>+|11>)) = 0; the input is a biseparable product.
  II1 (ii)=>(i) ingredients: (a) Det(psi) equals the discriminant of q(s,t) = det(s M0 + t M1), psi = |0>M0 + |1>M1
      (symbolic); (b) Det vanishes on every vector that is a product across any of the three cuts (symbolic); (c) the
      constructive orbit lemma on 3 exact instances: from psi = (A (x) B (x) C)(|000> + |111>) with rational A, B, C, the
      rational roots of q give rank-one slices N_k = v_k w_k^T and the reconstructed A', B', C' satisfy
      (A' (x) B' (x) C')(|000> + |111>) = psi exactly; (d) filters from five tokens: with the pair state
      (1 (x) A)Phi+(1 (x) A)^dag on (z,q) (a PSD pair operator, so a state of the Q3 pair) and the Bell effect on (z,p),
      the conditional of every unit y on (p,s,t) is (1/4) Ad(A)_q(y(p -> q)) (3 random rational A, one of them
      singular); countercontrol: Ad(A^T) differs for a non-symmetric A.
  I4  (i)=>(iv) control: Ad(CNOT (x) 1) maps 3 random exact PSD operators to PSD operators (immediate in writing).
  III4 (iii)=>(iv): six-token crossing (A|B, C|D) = (012|345, 03|1245) with the Bell link on (0,3) and y = the CNOT Choi
      state on D (inputs (4,5), outputs (1,2), Choi(Phi_y) = y): for every unit g on (3,4,5),
      cond_B[T(g); Phi+_03 (x) y] = (1/2) (rename 3->0 (x) Ad(CNOT)_(4,5)->(1,2))(g); countercontrol: the identity Choi
      state gives the rename only (differs on some unit).
  I3  (i)=>(iii): seven-token crossing (0123|456, 0145|236) with Bell links (0,4), (1,5) and y = 2 GHZ on (6,2,3) (the
      Choi state of the copy isometry V: 6 -> (2,3)): for every unit g on (4,5,6),
      cond_B[T(g); links (x) y] = (1/4)(rename 45->01 (x) Ad(V))(g); with g = |psi3><psi3|, psi3 = sum_ij |j>_4 |i+j>_5
      |i>_6 (PSD, Det != 0, so in PSD8 under (i)), the conditional is (1/4) times the CNOT Choi state on (0,1,2,3)
      (inputs 2, 0; outputs 3, 1); and that state equals the coordinator's (CNOT_12 (x) 1)(Omega_14 Omega_25) after
      relabelling.
  D   the owner's distinction: C is PSD, C^2 = 4 C, T(C) = C (so state and effect forms agree under K4 = T(K4*)); the
      functional rho -> tr(C rho)/4 lies in [0, 1] on normalized PSD states (eigenvalues 0 and 4); countercontrol: an
      explicit Hermitian w with tr w = 1, nonnegative on every product of two-token PSD operators across every 2|2 cut
      and on every product of one-token and three-token PSD operators, has tr(C w) < 0, so whether C is an effect of a
      four-token body depends on the body.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p4_e3_directions")
rng = random.Random(20261009 + 4)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])


# ------------------------------------------------------------------------------------------------ K gate on a triple
def coords3(rho):
    a, b, c = rho.qs
    return [[[L.pair(L.tensor(L.sig_op(m, a), L.sig_op(n, b), L.sig_op(k, c)), rho) for k in range(4)]
             for n in range(4)] for m in range(4)]


def pauli3(T, qs):
    out = L.Op(qs, {})
    for m in range(4):
        for n in range(4):
            for k in range(4):
                t = L.G.of(T[m][n][k])
                if not t.is_zero():
                    out = out + L.tensor(L.sig_op(m, qs[0]), L.sig_op(n, qs[1]), L.sig_op(k, qs[2])).scale(t)
    return out.scale(Fr(1, 8))


ok_k = True
CN3 = L.op(L.CNOT, (0, 1))
for m in range(4):
    for n in range(4):
        for k in range(4):
            T = [[[1 if (i, j, l) == (m, n, k) else 0 for l in range(4)] for j in range(4)] for i in range(4)]
            # kernel cnot on indices (0,1), slice by slice in the third index
            Tk = [[[None] * 4 for _ in range(4)] for _ in range(4)]
            for l in range(4):
                sl = L.kernel_cnot_tab([[T[i][j][l] for j in range(4)] for i in range(4)])
                for i in range(4):
                    for j in range(4):
                        Tk[i][j][l] = sl[i][j]
            rhs = coords3(L.ad(CN3, pauli3(T, (0, 1, 2))))
            ok_k &= all(L.G.of(Tk[i][j][l]) == rhs[i][j][l] for i in range(4) for j in range(4) for l in range(4))
rep.check("K1 the kernel cnot on the first two indices of a three-token table equals Ad(CNOT (x) 1) (64 unit tables)",
          ok_k)


# ------------------------------------------------------------------------------------------------ IV2
def vec_of_rank1(Pop):
    """a vector v with Pop = v v^dag (Pop rank one, exact): column of the first nonzero diagonal entry."""
    N = 2 ** Pop.n
    for r in range(N):
        d = Pop.get(r, r)
        if not d.is_zero():
            return [Pop.get(i, r) for i in range(N)], d
    return None, None


plus = L.ket_op([1, 1], (0,)).scale(Fr(1, 2))
inp = L.tensor(plus, L.phi_plus(1, 2))
outp = L.ad(CN3, inp)
psi = [Fr(0)] * 8
for b in ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)):
    psi[L.bits_index(b)] = Fr(1, 2)
det_psi = L.hyperdet(psi)
ctrl = (L.hyperdet([1, 0, 0, 0, 0, 0, 0, 1]), L.hyperdet([0, 1, 1, 0, 1, 0, 0, 0]),
        L.hyperdet([1, 0, 0, 1, 0, 0, 0, 0]))
rep.check("IV2 (iv)=>(ii): Ad(CNOT_01)(|+><+| (x) Phi+_12) = |psi><psi|, psi = (|000>+|011>+|101>+|110>)/2, "
          "Det(psi) = %s != 0 (input biseparable); controls Det(GHZ), Det(W), Det(|0>Phi+) = %s, %s, %s"
          % ((det_psi,) + ctrl),
          outp == L.ket_op(psi, (0, 1, 2)) and not det_psi.is_zero() and not ctrl[0].is_zero()
          and ctrl[1].is_zero() and ctrl[2].is_zero())

# ------------------------------------------------------------------------------------------------ II1 (ii)=>(i)
av = sp.symbols("a0:8")
a = lambda i, j, k: av[4 * i + 2 * j + k]
s_, t_ = sp.symbols("s t")
M = lambda i: sp.Matrix([[a(i, 0, 0), a(i, 0, 1)], [a(i, 1, 0), a(i, 1, 1)]])
q = sp.expand((s_ * M(0) + t_ * M(1)).det())
cA, cB, cC = q.coeff(s_, 2).coeff(t_, 0), q.coeff(s_, 1).coeff(t_, 1), q.coeff(s_, 0).coeff(t_, 2)
disc = sp.expand(cB ** 2 - 4 * cA * cC)
Det_sym = (a(0, 0, 0) ** 2 * a(1, 1, 1) ** 2 + a(0, 0, 1) ** 2 * a(1, 1, 0) ** 2 + a(0, 1, 0) ** 2 * a(1, 0, 1) ** 2
           + a(1, 0, 0) ** 2 * a(0, 1, 1) ** 2
           - 2 * (a(0, 0, 0) * a(1, 1, 1) * a(0, 0, 1) * a(1, 1, 0) + a(0, 0, 0) * a(1, 1, 1) * a(0, 1, 0) * a(1, 0, 1)
                  + a(0, 0, 0) * a(1, 1, 1) * a(1, 0, 0) * a(0, 1, 1) + a(0, 0, 1) * a(1, 1, 0) * a(0, 1, 0) * a(1, 0, 1)
                  + a(0, 0, 1) * a(1, 1, 0) * a(1, 0, 0) * a(0, 1, 1) + a(0, 1, 0) * a(1, 0, 1) * a(1, 0, 0) * a(0, 1, 1))
           + 4 * (a(0, 0, 0) * a(0, 1, 1) * a(1, 0, 1) * a(1, 1, 0) + a(1, 1, 1) * a(1, 0, 0) * a(0, 1, 0) * a(0, 0, 1)))
# the same polynomial as the library's hyperdet (on 2 exact instances) and as the discriminant (symbolic)
lib_ok = all(L.hyperdet(v) == L.G.of(int(Det_sym.subs(dict(zip(av, v))))) for v in
             ([1, 2, -1, 3, 0, 1, 2, -2], [3, -1, 1, 1, 2, 0, -3, 1]))
u_ = sp.symbols("u0:2")
x_ = sp.symbols("x0:4")
prod_ok = True
for cut in range(3):
    subs = {}
    for i, j, k in itertools.product(range(2), repeat=3):
        idx = (i, j, k)
        single = idx[cut]
        rest = [idx[m] for m in range(3) if m != cut]
        subs[a(i, j, k)] = u_[single] * x_[2 * rest[0] + rest[1]]
    prod_ok &= sp.expand(Det_sym.subs(subs, simultaneous=True)) == 0
rep.check("II1a Det = discriminant of q(s,t) = det(s M0 + t M1) (symbolic); the library hyperdet agrees (2 instances)",
          sp.expand(Det_sym - disc) == 0 and lib_ok)
rep.check("II1b Det vanishes on vectors that are products across each of the three cuts (symbolic)", prod_ok)


def kron_vec(*vs):
    out = [Fr(1)]
    for v in vs:
        out = [x * y for x in out for y in v]
    return out


def mat_apply_ghz(A, B, C):
    """(A (x) B (x) C)(|000> + |111>) as an 8-vector (A, B, C as 2x2 nested lists, columns = images of |0>, |1>)."""
    col = lambda Mx, k: [Fr(Mx[0][k]), Fr(Mx[1][k])]
    v0 = kron_vec(col(A, 0), col(B, 0), col(C, 0))
    v1 = kron_vec(col(A, 1), col(B, 1), col(C, 1))
    return [v0[i] + v1[i] for i in range(8)]


def orbit_lemma(psi_v):
    """constructive proof steps on an exact instance with rational roots; returns reconstructed (A, B, C) or None."""
    M0 = [[psi_v[0], psi_v[1]], [psi_v[2], psi_v[3]]]
    M1 = [[psi_v[4], psi_v[5]], [psi_v[6], psi_v[7]]]
    qa = M0[0][0] * M0[1][1] - M0[0][1] * M0[1][0]
    qc = M1[0][0] * M1[1][1] - M1[0][1] * M1[1][0]
    qb = M0[0][0] * M1[1][1] + M1[0][0] * M0[1][1] - M0[0][1] * M1[1][0] - M1[0][1] * M0[1][0]
    D = qb * qb - 4 * qa * qc
    sq = sp.sqrt(sp.Rational(D.numerator, D.denominator))
    if not sq.is_rational or D == 0:
        return None
    sq = Fr(int(sp.fraction(sq)[0]), int(sp.fraction(sq)[1]))
    roots = []
    if qa != 0:
        roots = [((-qb + sq) / (2 * qa), Fr(1)), ((-qb - sq) / (2 * qa), Fr(1))]       # (s : t) with t = 1
    else:
        roots = [(Fr(1), Fr(0)), (-qc / qb, Fr(1))]
    Ns = []
    for (s, t) in roots:
        N = [[s * M0[i][j] + t * M1[i][j] for j in range(2)] for i in range(2)]
        if N[0][0] * N[1][1] - N[0][1] * N[1][0] != 0:
            return None
        # rank-one factor N = v w^T
        if N[0][0] != 0 or N[0][1] != 0:
            r = 0
        else:
            r = 1
        w = [N[r][0], N[r][1]]
        k = 0 if w[0] != 0 else 1
        v = [N[0][k] / w[k], N[1][k] / w[k]]
        Ns.append((v, w))
    # M_i = sum_k c_ik N_k with [N1; N2] = [[s1, t1], [s2, t2]] [M0; M1]
    (s1, t1), (s2, t2) = roots
    det = s1 * t2 - s2 * t1
    inv = [[t2 / det, -t1 / det], [-s2 / det, s1 / det]]                # inverse of [[s1, t1], [s2, t2]]
    # [M0; M1] = inv [N1; N2]:  M_i = inv[i][0] N1 + inv[i][1] N2  ->  u_k = (inv[0][k], inv[1][k])
    A = [[inv[0][0], inv[0][1]], [inv[1][0], inv[1][1]]]
    B = [[Ns[0][0][0], Ns[1][0][0]], [Ns[0][0][1], Ns[1][0][1]]]
    C = [[Ns[0][1][0], Ns[1][1][0]], [Ns[0][1][1], Ns[1][1][1]]]
    return A, B, C


orb_ok = True
n_inst = 0
tries = 0
while n_inst < 3 and tries < 200:
    tries += 1
    A0 = [[Fr(rng.randint(-3, 3)), Fr(rng.randint(-3, 3))] for _ in range(2)]
    B0 = [[Fr(rng.randint(-3, 3)), Fr(rng.randint(-3, 3))] for _ in range(2)]
    C0 = [[Fr(rng.randint(-3, 3)), Fr(rng.randint(-3, 3))] for _ in range(2)]
    if any(Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0] == 0 for Mx in (A0, B0, C0)):
        continue
    pv = mat_apply_ghz(A0, B0, C0)
    if L.hyperdet(pv).is_zero():
        orb_ok = False
    res = orbit_lemma(pv)
    if res is None:
        continue
    A1, B1, C1 = res
    invertible = all(Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0] != 0 for Mx in (A1, B1, C1))
    orb_ok &= invertible and mat_apply_ghz(A1, B1, C1) == pv
    n_inst += 1
rep.check("II1c constructive orbit lemma on %d exact instances: the rational roots of q give rank-one slices and "
          "invertible A', B', C' with (A' (x) B' (x) C')(|000> + |111>) = psi" % n_inst, orb_ok and n_inst == 3)


def tele(y, z, p, q_, st, state_link):
    return L.reorder(L.cond(L.phi_plus(z, p), L.tensor(state_link, y)), (q_,) + tuple(st))


ok_f = True
cc_f = False
filters = [[[L.G(1), L.G(2, -1)], [L.G(0), L.G(3)]], [[L.G(Fr(1, 2)), L.G(0, 1)], [L.G(-1), L.G(2)]],
           [[L.G(1), L.G(2)], [L.G(2), L.G(4)]]]                       # the last one is singular
z, p, q_, st = 4, 0, 3, (1, 2)
for Am in filters:
    Aop = L.op(Am, (q_,))
    link = L.ad(Aop, L.phi_plus(z, q_))
    AT = L.op([[Am[0][0], Am[1][0]], [Am[0][1], Am[1][1]]], (q_,))
    for _, y in L.units((p,) + st):
        lhs = tele(y, z, p, q_, st, link)
        ren = L.reorder(L.relabel(y, {p: q_}), (q_,) + st)
        ok_f &= lhs == L.reorder(L.ad(Aop, ren), (q_,) + st).scale(Fr(1, 4))
        if not cc_f and lhs != L.reorder(L.ad(AT, ren), (q_,) + st).scale(Fr(1, 4)):
            cc_f = True
rep.check("II1d filters from five tokens: pair state (1 (x) A)Phi+(1 (x) A)^dag on (z,q), Bell effect on (z,p): "
          "conditional = (1/4) Ad(A)_q(y(p -> q)) on all units (3 rational A, one singular); countercontrol Ad(A^T) "
          "differs", ok_f and cc_f)

# ------------------------------------------------------------------------------------------------ I4
ok_i4 = True
for _ in range(3):
    rho = L.rand_psd(rng, (0, 1, 2), rank=2)
    ok_i4 &= L.psd(L.ad(CN3, rho))[0]
rep.check("I4 (i)=>(iv) control: Ad(CNOT (x) 1) maps 3 random exact PSD operators to PSD operators", ok_i4)


# ------------------------------------------------------------------------------------------------ III4
def choi_state_of_unitary(U, ins, outs):
    """Choi(Ad U) = sum_ij |i><j|_in (x) U|i><j|U^dag on outs (ins first)."""
    n = len(ins)
    v = [L.ZERO] * (2 ** (2 * n))
    Um = [[L.G.of(x) for x in r] for r in U]
    for i in range(2 ** n):
        for o in range(2 ** n):
            v[(i << n) | o] = Um[o][i]
    return L.ket_op(v, tuple(ins) + tuple(outs))


Ccnot = choi_state_of_unitary(L.CNOT, (4, 5), (1, 2))
J_id = choi_state_of_unitary([[1 if i == j else 0 for j in range(4)] for i in range(4)], (4, 5), (1, 2))
Xs = L.tensor(L.phi_plus(0, 3), Ccnot)
Xid = L.tensor(L.phi_plus(0, 3), J_id)
CN12 = L.op(L.CNOT, (1, 2))
ok_34 = True
cc_34 = False
for _, g in L.units((3, 4, 5)):
    lhs = L.reorder(L.cond(L.transpose(g), Xs), (0, 1, 2))
    ren = L.reorder(L.relabel(g, {3: 0, 4: 1, 5: 2}), (0, 1, 2))
    rhs = L.reorder(L.ad(CN12, ren), (0, 1, 2)).scale(Fr(1, 2))
    ok_34 &= lhs == rhs
    lid = L.reorder(L.cond(L.transpose(g), Xid), (0, 1, 2))
    ok_34 &= lid == ren.scale(Fr(1, 2))
    if not cc_34 and lid != lhs:
        cc_34 = True
rep.check("III4 (iii)=>(iv): six-token crossing (012|345, 03|1245): cond[T(g); Phi+_03 (x) C] = (1/2)(rename (x) "
          "Ad CNOT)(g) on all 64 units; countercontrol: the identity Choi state gives the rename only (differs)",
          ok_34 and cc_34)

# ------------------------------------------------------------------------------------------------ I3
V = [[1, 0], [0, 0], [0, 0], [0, 1]]                    # |i> -> |ii>, as a 4 x 2 matrix
yV = L.ket_op([1, 0, 0, 0, 0, 0, 0, 1], (6, 2, 3))      # sum_ij |i><j|_6 (x) |ii><jj|_23 = 2 GHZ
X7 = L.tensor(L.phi_plus(0, 4), L.phi_plus(1, 5), yV)
ok_13 = True
for _, g in L.units((4, 5, 6)):
    lhs = L.reorder(L.cond(L.transpose(g), X7), (0, 1, 2, 3))
    ren = L.relabel(g, {4: 0, 5: 1})                     # on (0, 1, 6)
    # Ad(V) on token 6 -> (2,3): sum over matrix entries
    d = {}
    for (r, c), v in L.reorder(ren, (0, 1, 6)).d.items():
        r01, r6 = r >> 1, r & 1
        c01, c6 = c >> 1, c & 1
        rr = (r01 << 2) | (3 * r6)
        cc_ = (c01 << 2) | (3 * c6)
        d[(rr, cc_)] = d.get((rr, cc_), L.ZERO) + v
    rhs = L.Op((0, 1, 2, 3), d).scale(Fr(1, 4))
    ok_13 &= lhs == rhs
psi3 = [Fr(0)] * 8
for i in range(2):
    for j in range(2):
        psi3[L.bits_index((j, (i + j) % 2, i))] = Fr(1)
g3 = L.ket_op(psi3, (4, 5, 6))
out = L.reorder(L.cond(L.transpose(g3), X7), (0, 1, 2, 3))
cvec = [Fr(0)] * 16
for aa in range(2):
    for bb in range(2):
        # inputs: token 2 (control) = aa, token 0 (target) = bb; outputs: token 3 = aa, token 1 = aa + bb
        cvec[L.bits_index((bb, (aa + bb) % 2, aa, aa))] = Fr(1)
Cout = L.ket_op(cvec, (0, 1, 2, 3))
# coordinator's form (CNOT_12 (x) 1)(Omega_14 Omega_25) on tokens (1,2,4,5): sum_ab |a>_1 |a+b>_2 |a>_4 |b>_5
coord = [Fr(0)] * 16
for aa in range(2):
    for bb in range(2):
        coord[L.bits_index((aa, (aa + bb) % 2, aa, bb))] = Fr(1)
Ccoord = L.ket_op(coord, (1, 2, 4, 5))
same = L.reorder(L.relabel(Ccoord, {1: 3, 2: 1, 4: 2, 5: 0}), (0, 1, 2, 3)) == Cout
rep.check("I3 (i)=>(iii): seven-token crossing (0123|456, 0145|236): cond[T(g); links (x) Choi(V)] = (1/4)(rename (x) "
          "Ad V)(g) on all 64 units; psi3 is PSD with Det = %s != 0; its conditional is (1/4) the CNOT Choi state; "
          "equal to the coordinator's (CNOT_12 (x) 1)(Omega_14 Omega_25) after relabelling" % L.hyperdet(psi3),
          ok_13 and not L.hyperdet(psi3).is_zero() and out == Cout.scale(Fr(1, 4)) and same
          and L.psd(L.ket_op(psi3, (4, 5, 6)))[0])

# ------------------------------------------------------------------------------------------------ D owner's distinction
C4 = Cout
C2 = L.matmul(C4, C4)
rep.check("D1 C is PSD, C^2 = 4C (eigenvalues 0 and 4: tr(C rho)/4 in [0,1] on normalized PSD states), T(C) = C",
          L.psd(C4)[0] and C2 == C4.scale(4) and L.transpose(C4) == C4)
# countercontrol: w = (1/16)(1 - C/2) normalized; positivity on products across 2|2 and 1|3 cuts via max overlaps
# exact: |c>/2 has maximal overlap 1/2 with products across 01|23, 02|13, 03|12 and 1|3 cuts  (Schmidt coefficients)
cn = [x / 2 for x in cvec]                                      # normalized |c>/2


def schmidt_max2(vec, qs, part):
    """largest eigenvalue squared-overlap bound: the max of <phi|rho_part|phi> over unit phi = lambda_max(rho_part);
    returned as the exact largest eigenvalue of the reduced density matrix when it is diagonalizable over Q by a
    rational check: we return the reduced matrix itself."""
    rho = L.ket_op(vec, qs)
    return L.ptrace(rho, part)


cuts = [(0, 1), (0, 2), (0, 3), (0,), (1,), (2,), (3,)]
lam_ok = True
for part in cuts:
    red = schmidt_max2(cn, (0, 1, 2, 3), part)
    # lambda_max(red) <= 1/2  <=>  1/2 - red is PSD
    lam_ok &= L.psd(L.identity(part).scale(Fr(1, 2)) - red)[0]
w = L.identity((0, 1, 2, 3)).scale(Fr(1, 16)) - C4.scale(Fr(1, 32)) + L.Op((0, 1, 2, 3), {})
trw = L.trace(w)
w = w.scale(L.ONE / trw)
vCw = L.pair(C4, w)
rep.check("D2 countercontrol: every reduced state of |c>/2 on the 2|2 and 1|3 cuts has largest eigenvalue <= 1/2 "
          "(so w = (1/16)(1 - C/2), normalized, is >= 0 on all products across those cuts) and tr(C w) = %s < 0" % vCw,
          lam_ok and vCw.re < 0 and vCw.im == 0)

rep.verdict("P4-E3-DIRECTIONS-EXACT")
