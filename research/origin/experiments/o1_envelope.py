"""o1_envelope.py -- research/origin, node O1, tier M (the matrix carrier, configuration frame).

QUESTION. Which classes of substratum access are monomial-only, and is monomiality (not ones-fixing) the
exact invariant that excludes a coherent mixer and the owner's H-sandwich witness?

OBJECTS (exact arithmetic only: Gaussian rationals as pairs of Fractions; sympy only where sqrt(2) occurs).
  Delta        complete dephasing in the configuration frame, X -> diag(X).
  DC           a linear map Phi with Phi o Delta = Delta o Phi ("dephasing-covariant").
  non-gen      Phi(E_ii) diagonal for every i (creates no coherence from the frame).
  non-det      Delta(Phi(E_ij)) = 0 for i != j (turns no coherence into populations).
  monomial     at most one nonzero entry per row and per column (SubstratumInterface.IsMonomial /
               StructuralClosure.IsSubmonomial; the kernel class `substratumClass`).
  ones-fixing  K * 1 = z * 1 (InstrumentRealization.OnesFixing, for one operator).
  sandwich     rho0 = |0><0|; P_coh(k) = [M2(M1 rho0)]_kk; P_deph(k) = [M2(D(M1 rho0))]_kk with D the
               path dephasing of the visible register (Delta_S (x) id on a composite); V = P_coh - P_deph.

DECISION RULE (fixed before the first run; the expected numbers are NOT fixed -- every verdict line is
generated from the measured values):
  VERDICT ENVELOPE-M HOLDS is printed iff every check below passes and every countercontrol returns its
  expected-false value; otherwise VERDICT VOID is printed and no envelope claim may be made from this run.
  Checks:
   M1  for every unitary in the test family: DC <-> non-gen <-> non-det <-> monomial (all four agree).
   M2  for every qubit unitary U = [[a,b],[c,d]] in the family: the sandwich (U, U^dagger) has
       P_coh(0) = 1, P_deph(0) = |a|^4 + |b|^4, V = 2|a|^2|b|^2; V = 0 exactly for the monomial ones;
       the owner's witness (P_coh = 1, P_deph = 1/2) holds exactly for the balanced ones (|a|^2 = 1/2).
   M3  closure: every protocol in the deterministic family (uniform or pure-seed ancilla attach, monomial
       step on the composite, Luders readout of a register, outcome-dependent monomial continuation,
       coarse-graining, discard) yields DC branches and a DC aggregate on the system.
   M4  reachable set: from diagonal preparations every intermediate state of every monomial protocol is
       diagonal, the fresh-record path dephasing equals Delta_S (x) id, and the composite sandwich
       visibility is exactly 0 for all 24 x 24 permutation pairs, both ancilla seeds and both visible seeds.
   M5  ones-fixing is independent of mixing: the four cells (ones-fixing / not) x (monomial / not) are each
       populated by an exact unitary, and V = 0 exactly in the two monomial cells and V > 0 in the two
       non-monomial cells; the layer gate flow gateFlow(swap, 1/2) (kernel `onesClass_gateFlow`) is
       ones-fixing, non-monomial and a balanced mixer on 2 and on 3 points; the transition flow at pi/4
       moves the all-ones ray on 3 points (kernel countercontrol `flow_realized_not_instrumentRealized`).
   M6  the kernel's interference exposure (AncillaInterference.tauChain_diag: branches 3/2, -1/2) is
       reproduced with the ones-fixing mixer sqrt(X) in place of hMat.
   M7  DC is a linear subspace of superoperators of dimension d^2 + (d^2 - d)^2 (so closed under sums,
       convex combinations and limits): computed by exact rank for d = 2, 3.
  Countercontrols (each must return False):
   CC1  DC(Ad H) ; CC2  DC of a monomial protocol with one H step inserted ; CC3  ones-fixing(H) ;
   CC4  ones-fixing(Z) ; CC5  V = 0 for the composite sandwich with the step (H (x) 1) as first mixer ;
   CC6  V = 0 for the sandwich with a coherent seed |+><+| (not reachable in the class), M1 = 1, M2 = H
        (the reachable-set lemma is load-bearing: outside it a non-monomial reader sees the coherence).

Run: python3 -I -B o1_envelope.py > o1_envelope.out 2> o1_envelope.err; echo "exit $?" >> o1_envelope.err
"""

from fractions import Fraction as Fr
import itertools
import sympy as sp

# ---------------------------------------------------------------- exact Gaussian rationals


class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = gg(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = gg(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return gg(o) - self

    def __mul__(self, o):
        o = gg(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def norm2(self):
        return self.re * self.re + self.im * self.im

    def __eq__(self, o):
        o = gg(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __truediv__(self, o):
        o = gg(o)
        n = o.norm2()
        return self * G(o.re / n, -o.im / n)

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f"{self.im}i"
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


I_ = G(0, 1)


def zeros(n, m=None):
    m = n if m is None else m
    return [[G() for _ in range(m)] for _ in range(n)]


def eye(n):
    Z = zeros(n)
    for i in range(n):
        Z[i][i] = G(1)
    return Z


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if a.iszero():
                continue
            Bt = B[t]
            Ci = C[i]
            for j in range(m):
                b = Bt[j]
                if not b.iszero():
                    Ci[j] = Ci[j] + a * b
    return C


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msc(c, A):
    return [[gg(c) * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    n, m = len(A), len(B)
    C = zeros(n * m)
    for i in range(n):
        for j in range(n):
            if A[i][j].iszero():
                continue
            for k in range(m):
                for l in range(m):
                    C[i * m + k][j * m + l] = A[i][j] * B[k][l]
    return C


def unit(n, i, j):
    E = zeros(n)
    E[i][j] = G(1)
    return E


def Delta(X):
    n = len(X)
    Y = zeros(n)
    for i in range(n):
        Y[i][i] = X[i][i]
    return Y


def is_diag(X):
    return all(X[i][j].iszero() for i in range(len(X)) for j in range(len(X)) if i != j)


def conjK(K, w=Fr(1)):
    Kd = dag(K)
    return lambda X: msc(G(w), mm(mm(K, X), Kd))


def is_unitary(K):
    return meq(mm(dag(K), K), eye(len(K)))


def is_monomial(K):
    n = len(K)
    rows = all(sum(1 for j in range(n) if not K[i][j].iszero()) <= 1 for i in range(n))
    cols = all(sum(1 for i in range(n) if not K[i][j].iszero()) <= 1 for j in range(n))
    return rows and cols


def ones_fixing(K):
    v = [sum((K[i][j] for j in range(len(K))), G()) for i in range(len(K))]
    return all(x == v[0] for x in v)


def is_DC(Phi, n):
    for i in range(n):
        for j in range(n):
            E = unit(n, i, j)
            if not meq(Phi(Delta(E)), Delta(Phi(E))):
                return False
    return True


def non_gen(Phi, n):
    return all(is_diag(Phi(unit(n, i, i))) for i in range(n))


def non_det(Phi, n):
    return all(all(Phi(unit(n, i, j))[k][k].iszero() for k in range(n))
               for i in range(n) for j in range(n) if i != j)


# ---------------------------------------------------------------- bookkeeping

RESULTS = []


def check(cid, ok, msg=""):
    RESULTS.append((cid, bool(ok), msg, "check"))
    print(f"{cid:8s} {'PASS' if ok else 'FAIL'}  {msg}")


def counter(cid, value, msg=""):
    # countercontrol: the predicate must be False
    RESULTS.append((cid, not bool(value), msg, "counter"))
    print(f"{cid:8s} {'CC-OK (False as required)' if not value else 'CC-FAIL (True)'}  {msg}")


# ---------------------------------------------------------------- the unitary test family

h = Fr(1, 2)
SX = [[G(h, h), G(h, -h)], [G(h, -h), G(h, h)]]               # gateFlow(swap, 1/2) = sqrt(X)
SXd = dag(SX)
X_ = [[G(0), G(1)], [G(1), G(0)]]
Z_ = [[G(1), G(0)], [G(0), G(-1)]]
S_ = [[G(1), G(0)], [G(0), I_]]                                  # quarter phase (phaseGate)
P35 = [[G(Fr(3, 5)), G(0, Fr(-4, 5))], [G(0, Fr(-4, 5)), G(Fr(3, 5))]]  # exp(-itX), cos t = 3/5
R35 = [[G(Fr(3, 5)), G(Fr(-4, 5))], [G(Fr(4, 5)), G(Fr(3, 5))]]       # real rotation, cos = 3/5
PH = [[G(0), G(Fr(3, 5), Fr(4, 5))], [G(0, 1), G(0)]]            # monomial with a rational phase

# H and rot(pi/4) carry 1/sqrt2: their channels are (1/2) Ad(raw) with integer raw matrices.
HRAW = [[G(1), G(1)], [G(1), G(-1)]]
RRAW = [[G(1), G(-1)], [G(1), G(1)]]

FAMILY2 = [  # (name, Kraus matrix, channel weight) -- the operator is sqrt(w) * K
    ("I", eye(2), Fr(1)), ("X", X_, Fr(1)), ("Z", Z_, Fr(1)), ("S", S_, Fr(1)), ("PH", PH, Fr(1)),
    ("sqrtX", SX, Fr(1)), ("sqrtX^dag", SXd, Fr(1)), ("Xrot(3/5)", P35, Fr(1)), ("Rot(3/5)", R35, Fr(1)),
    ("H", HRAW, h), ("rot(pi/4)", RRAW, h),
]

ORTH3 = [[G(Fr(1, 3)), G(Fr(2, 3)), G(Fr(2, 3))], [G(Fr(2, 3)), G(Fr(1, 3)), G(Fr(-2, 3))],
         [G(Fr(2, 3)), G(Fr(-2, 3)), G(Fr(1, 3))]]
MON3 = [[G(0), G(0), G(0, 1)], [G(Fr(3, 5), Fr(4, 5)), G(0), G(0)], [G(0), G(-1), G(0)]]
GF3 = [[G(h, h), G(h, -h), G(0)], [G(h, -h), G(h, h), G(0)], [G(0), G(0), G(1)]]  # gateFlow on 3 points
FAMILY3 = [("ORTH3", ORTH3, Fr(1)), ("MON3", MON3, Fr(1)), ("gateFlow3", GF3, Fr(1)), ("I3", eye(3), Fr(1))]


def unitary_scaled(K, w):
    return meq(msc(G(w), mm(dag(K), K)), eye(len(K)))


print("== o1_envelope: tier M (matrix carrier, configuration frame) ==")
print()
print("-- M1: DC <-> non-generating <-> non-detecting <-> monomial, for unitaries")
m1_ok = True
for name, K, w in FAMILY2 + FAMILY3:
    n = len(K)
    assert unitary_scaled(K, w), name
    Phi = conjK(K, w)
    dc, ng, nd, mo = is_DC(Phi, n), non_gen(Phi, n), non_det(Phi, n), is_monomial(K)
    agree = (dc == ng == nd == mo)
    m1_ok &= agree
    print(f"   {name:10s} d={n}  unitary=True  DC={dc}  non-gen={ng}  non-det={nd}  monomial={mo}  agree={agree}")
check("M1", m1_ok, "the four predicates agree on all 15 unitaries")

print()
print("-- M2: the qubit sandwich (U, U^dagger) from |0><0|, path dephasing Delta")
rho0 = unit(2, 0, 0)
m2_ok = True
owner = []
for name, K, w in FAMILY2:
    U1 = conjK(K, w)
    U2 = conjK(dag(K), w)
    coh = U2(U1(rho0))
    deph = U2(Delta(U1(rho0)))
    pc, pd = coh[0][0], deph[0][0]
    a2 = (K[0][0].norm2()) * w
    b2 = (K[0][1].norm2()) * w
    form_ok = (pc == G(1)) and (pd == G(a2 * a2 + b2 * b2))
    V = pc - pd
    vform = (V == G(2 * a2 * b2))
    mono = is_monomial(K)
    zero_iff_mono = (V.iszero() == mono)
    m2_ok &= form_ok and vform and zero_iff_mono
    if pd == G(h):
        owner.append(name)
    print(f"   {name:10s} P_coh(0)={pc}  P_deph(0)={pd}  V={V}  |a|^2={a2}  monomial={mono}")
check("M2a", m2_ok, "P_coh=1, P_deph=|a|^4+|b|^4, V=2|a|^2|b|^2, V=0 iff monomial (11 qubit unitaries)")
bal = [name for name, K, w in FAMILY2 if K[0][0].norm2() * w == h]
check("M2b", sorted(owner) == sorted(bal),
      f"owner's witness (1, 1/2) holds exactly for the balanced unitaries: {sorted(owner)}")
# the same-mixer-twice form of the witness for H: H H = 1
coh = conjK(HRAW, h)(conjK(HRAW, h)(rho0))
deph = conjK(HRAW, h)(Delta(conjK(HRAW, h)(rho0)))
check("M2c", coh[0][0] == G(1) and deph[0][0] == G(h), f"H then H: P_coh(0)={coh[0][0]}, P_deph(0)={deph[0][0]}")

print()
print("-- M3: closure of DC under the instrument constructors (system qubit, ancilla qubit)")


class LCG:
    def __init__(self, seed):
        self.s = seed

    def next(self, n):
        self.s = (1103515245 * self.s + 12345) % (2 ** 31)
        return self.s % n


PHASES = [G(1), G(-1), I_, G(0, -1), G(Fr(3, 5), Fr(4, 5)), G(Fr(3, 5), Fr(-4, 5)), G(Fr(-5, 13), Fr(12, 13)),
          G(Fr(8, 17), Fr(15, 17))]
PERMS4 = list(itertools.permutations(range(4)))


def monomial_from(perm, phases):
    n = len(perm)
    K = zeros(n)
    for j in range(n):
        K[perm[j]][j] = phases[j]
    return K


def attach(X, tau):
    return kron(X, tau)


def ptrace_anc(Y, ds=2, da=2):
    X = zeros(ds)
    for s in range(ds):
        for t in range(ds):
            acc = G()
            for a in range(da):
                acc = acc + Y[s * da + a][t * da + a]
            X[s][t] = acc
    return X


def proj_reg(k, reg):
    # Luders projector of the composite (s, a): reg 'a' reads the ancilla, reg 's' reads the system
    P = zeros(4)
    for s in range(2):
        for a in range(2):
            v = a if reg == "a" else s
            if v == k:
                P[2 * s + a][2 * s + a] = G(1)
    return P


TAU_U = [[G(h), G(0)], [G(0), G(h)]]
TAU_0 = unit(2, 0, 0)

rng = LCG(20261010)
m3_ok = True
nprot = 0
for trial in range(60):
    tau = TAU_U if trial % 2 == 0 else TAU_0
    reg = "a" if (trial // 2) % 2 == 0 else "s"
    K0 = monomial_from(PERMS4[rng.next(24)], [PHASES[rng.next(8)] for _ in range(4)])
    Kc = [monomial_from(PERMS4[rng.next(24)], [PHASES[rng.next(8)] for _ in range(4)]) for _ in range(2)]

    def branch(k, X, K0=K0, Kc=Kc, tau=tau, reg=reg):
        Y = attach(X, tau)
        Y = mm(mm(K0, Y), dag(K0))
        P = proj_reg(k, reg)
        Y = mm(mm(P, Y), P)
        Y = mm(mm(Kc[k], Y), dag(Kc[k]))
        return ptrace_anc(Y)

    b0 = lambda X: branch(0, X)
    b1 = lambda X: branch(1, X)
    agg = lambda X: madd(branch(0, X), branch(1, X))
    ok = is_DC(b0, 2) and is_DC(b1, 2) and is_DC(agg, 2)
    # trace preservation of the aggregate (instrument normalization)
    tp = all(sum((agg(unit(2, i, j))[t][t] for t in range(2)), G()) == (G(1) if i == j else G(0))
             for i in range(2) for j in range(2))
    m3_ok &= ok and tp
    nprot += 1
check("M3", m3_ok, f"{nprot} deterministic protocols: both branches and the aggregate are DC and trace-preserving")

print()
print("-- M4: reachable set and composite sandwich, exhaustive over permutation pairs")
# fresh-record path dephasing: attach blank register r, CNOT s -> r, discard r ; compare with Delta_S (x) id
CNOT_SR = monomial_from((0, 1, 3, 2), [G(1)] * 4)  # on (s, r): |s,r> -> |s, r xor s>


def fresh_record(X2):  # on the 2-dim system alone (ancilla handled by composite below)
    Y = attach(X2, TAU_0)
    Y = mm(mm(CNOT_SR, Y), dag(CNOT_SR))
    return ptrace_anc(Y)


fr_ok = all(meq(fresh_record(unit(2, i, j)), Delta(unit(2, i, j))) for i in range(2) for j in range(2))
check("M4a", fr_ok, "fresh-record path dephasing (blank register, CNOT, discard) equals Delta on the visible qubit")


def path_deph(Y):  # Delta_S (x) id on the composite (s, a)
    Z = zeros(4)
    for p in range(4):
        for q in range(4):
            if p // 2 == q // 2:
                Z[p][q] = Y[p][q]
    return Z


all_diag = True
vis_zero = True
count = 0
for seed_s in (unit(2, 0, 0), unit(2, 1, 1)):
    for tau in (TAU_U, TAU_0):
        rho = attach(seed_s, tau)
        for p1 in PERMS4:
            K1 = monomial_from(p1, [G(1)] * 4)
            r1 = mm(mm(K1, rho), dag(K1))
            all_diag &= is_diag(r1)
            for p2 in PERMS4:
                K2 = monomial_from(p2, [G(1)] * 4)
                coh = ptrace_anc(mm(mm(K2, r1), dag(K2)))
                dph = ptrace_anc(mm(mm(K2, path_deph(r1)), dag(K2)))
                all_diag &= is_diag(coh)
                vis_zero &= meq(Delta(coh), Delta(dph))
                count += 1
check("M4b", all_diag, f"every intermediate and final state diagonal ({count} runs)")
check("M4c", vis_zero, f"composite sandwich visibility exactly 0 for all {count} runs (24 x 24 x 2 x 2)")
# the swap-with-memory protocol singled out: SWAP twice returns the seed, dephasing the path changes nothing
SWAP = monomial_from((0, 2, 1, 3), [G(1)] * 4)
rho = attach(unit(2, 0, 0), TAU_U)
r1 = mm(mm(SWAP, rho), dag(SWAP))
coh = ptrace_anc(mm(mm(SWAP, r1), dag(SWAP)))
dph = ptrace_anc(mm(mm(SWAP, path_deph(r1)), dag(SWAP)))
check("M4d", coh[0][0] == G(1) and dph[0][0] == G(1),
      f"swap-with-memory: P_coh(0)={coh[0][0]}, P_deph(0)={dph[0][0]} (memory, not coherence)")

print()
print("-- M5: ones-fixing versus mixing (the four cells)")
cells = {}
for name, K, w in FAMILY2:
    U1 = conjK(K, w)
    U2 = conjK(dag(K), w)
    V = U2(U1(rho0))[0][0] - U2(Delta(U1(rho0)))[0][0]
    of = ones_fixing(K)
    mo = is_monomial(K)
    cells.setdefault((of, mo), []).append((name, V))
    print(f"   {name:10s} ones-fixing={of}  monomial={mo}  V={V}")
populated = all(len(cells.get((a, b), [])) > 0 for a in (True, False) for b in (True, False))
mono_zero = all(V.iszero() for key in cells for (_, V) in cells[key] if key[1])
nonmono_pos = all((not V.iszero()) and V.re > 0 for key in cells for (_, V) in cells[key] if not key[1])
check("M5a", populated and mono_zero and nonmono_pos,
      "all four cells populated; V = 0 in both monomial cells, V > 0 in both non-monomial cells")
print("   cells: " + "; ".join(f"(ones-fixing={a}, monomial={b}): {[n for n, _ in cells[(a, b)]]}"
                                for a in (True, False) for b in (True, False)))
# gate flow on 2 and 3 points: unitary, ones-fixing with z = 1, non-monomial, balanced mixer
gf_ok = True
for K in (SX, GF3):
    n = len(K)
    one = [sum((K[i][j] for j in range(n)), G()) for i in range(n)]
    gf_ok &= is_unitary(K) and all(x == G(1) for x in one) and not is_monomial(K)
r = conjK(SX)(rho0)
gf_ok &= (r[0][0] == G(h) and r[1][1] == G(h))
rr = conjK(SX)(conjK(SX)(rho0))
rd = conjK(SX)(Delta(conjK(SX)(rho0)))
gf_ok &= (rr[1][1] == G(1) and rd[1][1] == G(h))
r3 = conjK(GF3)(unit(3, 0, 0))
gf_ok &= (r3[0][0] == G(h) and r3[1][1] == G(h) and r3[2][2] == G(0))
check("M5b", gf_ok, "gateFlow(swap,1/2): ones-fixing (K*1 = 1), non-monomial, balanced; sqrtX sqrtX |0> = |1> "
      "(P=1), dephased 1/2; same on 3 points")
# transition flow at pi/4 on 3 points: cos(pi/4) 1_pair - i sin(pi/4) X_pair (+) 1  moves the all-ones ray
c = sp.sqrt(2) / 2
TF = sp.Matrix([[c, -sp.I * c, 0], [-sp.I * c, c, 0], [0, 0, 1]])
v = TF * sp.Matrix([1, 1, 1])
moves = sp.simplify(v[0] - v[2]) != 0
unit3 = sp.simplify(TF.H * TF - sp.eye(3)) == sp.zeros(3)
nonmono3 = sum(1 for j in range(3) if TF[0, j] != 0) > 1
# on 2 points the same flow fixes the all-ones ray (eigenvalue e^{-i pi/4})
TF2 = sp.Matrix([[c, -sp.I * c], [-sp.I * c, c]])
v2 = TF2 * sp.Matrix([1, 1])
fixes2 = sp.simplify(v2[0] - v2[1]) == 0
check("M5c", moves and unit3 and nonmono3 and fixes2,
      f"transition flow at pi/4: unitary, non-monomial, moves the ones ray on 3 points "
      f"(K*1 = {list(sp.simplify(x) for x in v)}), fixes it on 2 points")

print()
print("-- M6: the interference exposure with the ones-fixing mixer sqrt(X)")


def anc_scale(t):
    return [[t[0][0], G(2) * t[0][1]], [G(2) * t[1][0], t[1][1]]]


tau1 = conjK(SX)(rho0)
tau2 = conjK(SXd)(anc_scale(tau1))
tau2b = conjK(SX)(anc_scale(tau1))
check("M6", tau2[0][0] == G(Fr(3, 2)) and tau2[1][1] == G(Fr(-1, 2)),
      f"seed, sqrtX, surplus, sqrtX^dag: branches {tau2[0][0]}, {tau2[1][1]} (kernel tauChain_diag with hMat: 3/2, -1/2);"
      f" with sqrtX as return mixer: {tau2b[0][0]}, {tau2b[1][1]}")

print()
print("-- M7: DC is a linear subspace of dimension d^2 + (d^2-d)^2")


def dc_dim(d):
    # unknown superoperator Phi with Phi(E_ij) = sum_kl c[kl,ij] E_kl ; constraints of Phi o Delta = Delta o Phi
    idx = [(k, l, i, j) for k in range(d) for l in range(d) for i in range(d) for j in range(d)]
    pos = {t: n for n, t in enumerate(idx)}
    rows = []
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    # coefficient of E_kl in Phi(Delta E_ij) - Delta(Phi E_ij)
                    row = [0] * len(idx)
                    if i == j:
                        row[pos[(k, l, i, i)]] += 1
                    if k == l:
                        row[pos[(k, k, i, j)]] -= 1
                    if any(row):
                        rows.append(row)
    M = sp.Matrix(rows)
    return len(idx) - M.rank()


d2, d3 = dc_dim(2), dc_dim(3)
check("M7", d2 == 4 + 4 and d3 == 9 + 36, f"dim DC: d=2 -> {d2} (of 16), d=3 -> {d3} (of 81)")

print()
print("-- countercontrols")
counter("CC1", is_DC(conjK(HRAW, h), 2), "DC(Ad H)")
Hc = kron(HRAW, eye(2))


def prot_with_H(X):
    Y = attach(X, TAU_U)
    Y = msc(G(h), mm(mm(Hc, Y), dag(Hc)))
    K = monomial_from((1, 0, 3, 2), [G(1)] * 4)
    Y = mm(mm(K, Y), dag(K))
    return ptrace_anc(Y)


counter("CC2", is_DC(prot_with_H, 2), "DC of a monomial protocol with one (H (x) 1) step")
counter("CC3", ones_fixing(HRAW), "ones-fixing(H)")
counter("CC4", ones_fixing(Z_), "ones-fixing(Z)")
rho = attach(unit(2, 0, 0), TAU_U)
r1 = msc(G(h), mm(mm(Hc, rho), dag(Hc)))
coh = ptrace_anc(msc(G(h), mm(mm(Hc, r1), dag(Hc))))
dph = ptrace_anc(msc(G(h), mm(mm(Hc, path_deph(r1)), dag(Hc))))
counter("CC5", meq(Delta(coh), Delta(dph)), f"V = 0 with (H (x) 1) twice: P_coh(0)={coh[0][0]}, P_deph(0)={dph[0][0]}")
plus = [[G(h), G(h)], [G(h), G(h)]]
coh = conjK(HRAW, h)(plus)
dph = conjK(HRAW, h)(Delta(plus))
counter("CC6", (coh[0][0] - dph[0][0]).iszero(),
        f"V = 0 with coherent seed |+>, M1 = 1, M2 = H: P_coh(0)={coh[0][0]}, P_deph(0)={dph[0][0]}")

print()
nfail = sum(1 for r in RESULTS if not r[1])
nchk = sum(1 for r in RESULTS if r[3] == "check")
ncc = sum(1 for r in RESULTS if r[3] == "counter")
if nfail == 0:
    print(f"OK -- {nchk}/{nchk} checks, {ncc} countercontrols expected-false")
    print("VERDICT ENVELOPE-M HOLDS: on the configuration carrier, DC <-> monomial for unitaries; every protocol of the")
    print("  monomial class tested (attach, step, readout, feed-forward, coarse, discard) is DC; the sandwich visibility")
    print(f"  of a qubit unitary is 2|a|^2|b|^2 (owner's 1 vs 1/2 exactly for the balanced ones: {sorted(owner)});")
    print("  ones-fixing is independent of mixing (all four cells populated; gateFlow(swap,1/2) is a ones-fixing")
    print("  balanced mixer); DC is a linear subspace, hence closed under mixtures and limits.")
else:
    print(f"VOID -- {nfail} failing item(s): " + ", ".join(r[0] for r in RESULTS if not r[1]))
    print("VERDICT VOID")
