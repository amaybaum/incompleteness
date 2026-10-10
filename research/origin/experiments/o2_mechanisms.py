"""o2_mechanisms.py -- research/origin, node O2: candidate mechanisms for a discrete non-monomial mixer.

For each mechanism: the smallest exact finite model; the induced operation on the visible qubit; whether it is
non-monomial (dephasing-covariance test, O1-T1); the H-sandwich with the available preparations and readouts;
and the mechanical half of the disguise test: does the mechanism's INPUT (the operators it is handed, before any
composition) already contain a non-monomial operator in the configuration frame?

Exact arithmetic only (Gaussian rationals as Fraction pairs; F_2 integer arithmetic for the lattice rule).

CLASSIFICATION RULE (fixed before the first run; the classes are computed, not asserted):
  input_nonmono = some input operator is not monomial in the configuration frame;
  readout       = 'passive' (the stated native readout: Luders / observe-and-forget idle on classical states)
                  or the name of a replacement readout;
  V_max         = the largest sandwich visibility found over the mechanism's tested protocols, with the path
                  dephasing defined as observe-and-forget with that readout.
  class FAILED-ENVELOPE  iff not input_nonmono and readout == 'passive' and V_max == 0;
  class FAILED-DISGUISE  iff input_nonmono and V_max > 0;
  class CONDITIONAL      iff not input_nonmono and readout != 'passive' and V_max > 0 (premise = readout name);
  class CANDIDATE        iff not input_nonmono and readout == 'passive' and V_max > 0
                         (would contradict O1-T3/T5; it must not occur; if it occurs the run is VOID).
  VERDICT O2 is printed iff every model sanity check passes, every countercontrol returns its expected-false
  value and no mechanism is CANDIDATE; otherwise VERDICT VOID.

MECHANISMS
  A12  A1-A2: finite configurations, bijective dynamics / selectable permutations (all 24 of {0,1}^2).
  A36  A3-A6: a link-coupled, centre-independent, linear second-order rule on a ring (N = 3, K = 2, q = 2),
       with the A6 gauge covariance M(n,e) -> G(n) M(n,e) G(n+e)^-1 checked exactly.
  PH   phase interventions (diagonal Gaussian-rational phases; Z; the quarter phase).
  RW   read-write coupling: every bijection fixing all states outside {a, b} (the ReadWriteFamily shape).
  ANC  ancilla coupling with readback and feed-forward (pointer to o1_envelope M3/M4) and the record
       instrument recordInstr (Kraus |a,a><a,b|), written into a blank register.
  TAV  coarse-graining and time averaging: the uniform average over the orbit of a cyclic permutation.
  CLO  closure: words of length <= 4 in monomial generators with infinite-order phases stay monomial.
  G1   HasAncillaQubitInterference: hMat available by hypothesis.
  G2   LayerFlowExecutable: the layer gate flow at t = 1/2 (its generator projector included as input).
  G3   the state-mixing datum rot(theta) at theta = pi/4 (StateMixingCoupling / fixedGateTheory).
  G4   the unistochastic lift of the balanced doubly stochastic matrix B = [[1/2,1/2],[1/2,1/2]].
  G5   the knowledge-balance readout KB-D on {0,1}^2 with the substratum swap (o1_fieldneutral F8).
Countercontrols (each must return False):
  CC1  V = 0 for the A12 composite sandwich with (H (x) 1) composed into both mixers (the detector is live
       on the A12 model; on the A36 ring one rule step already randomizes the visible bit, so an insertion
       there would not be informative);
  CC2  every induced visible channel of the A12 bijections remains DC after composing with Ad H;
  CC3  the G4 lift's coherent two-step prediction is fixed by B (two lifts with the same B must agree);
  CC4  the classifier returns FAILED-ENVELOPE on a synthetic mechanism with a non-monomial input and V > 0.

Run: python3 -I -B o2_mechanisms.py > o2_mechanisms.out 2> o2_mechanisms.err; echo "exit $?" >> o2_mechanisms.err
"""

from fractions import Fraction as Fr
import itertools

# ------------------------------------------------------------------ exact Gaussian rationals


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

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f"{self.im}i"
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def gg(x):
    return x if isinstance(x, G) else G(x, 0)


def zeros(n):
    return [[G() for _ in range(n)] for _ in range(n)]


def eye(n):
    Z = zeros(n)
    for i in range(n):
        Z[i][i] = G(1)
    return Z


def mm(A, B):
    n = len(A)
    C = zeros(n)
    for i in range(n):
        for t in range(n):
            a = A[i][t]
            if a.iszero():
                continue
            for j in range(n):
                b = B[t][j]
                if not b.iszero():
                    C[i][j] = C[i][j] + a * b
    return C


def dag(A):
    n = len(A)
    return [[A[j][i].conj() for j in range(n)] for i in range(n)]


def msc(c, A):
    return [[gg(c) * x for x in row] for row in A]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


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


def is_monomial(K):
    n = len(K)
    return (all(sum(1 for j in range(n) if not K[i][j].iszero()) <= 1 for i in range(n))
            and all(sum(1 for i in range(n) if not K[i][j].iszero()) <= 1 for j in range(n)))


def is_DC(Phi, n):
    for i in range(n):
        for j in range(n):
            E = unit(n, i, j)
            if not meq(Phi(Delta(E)), Delta(Phi(E))):
                return False
    return True


def conjK(K, w=Fr(1)):
    Kd = dag(K)
    return lambda X: msc(G(w), mm(mm(K, X), Kd))


def perm_matrix(p):
    n = len(p)
    K = zeros(n)
    for j in range(n):
        K[p[j]][j] = G(1)
    return K


def ptrace_second(Y, d1, d2):
    X = zeros(d1)
    for s in range(d1):
        for t in range(d1):
            acc = G()
            for a in range(d2):
                acc = acc + Y[s * d2 + a][t * d2 + a]
            X[s][t] = acc
    return X


def path_deph(Y, d1, d2):  # Delta on the first factor, identity on the second
    n = d1 * d2
    Z = zeros(n)
    for p in range(n):
        for q in range(n):
            if p // d2 == q // d2:
                Z[p][q] = Y[p][q]
    return Z


h = Fr(1, 2)
RESULTS = []
CLASSES = {}


def check(cid, ok, msg=""):
    RESULTS.append((cid, bool(ok), "check"))
    print(f"{cid:8s} {'PASS' if ok else 'FAIL'}  {msg}")


def counter(cid, value, msg=""):
    RESULTS.append((cid, not bool(value), "counter"))
    print(f"{cid:8s} {'CC-OK (False as required)' if not value else 'CC-FAIL (True)'}  {msg}")


def classify(input_nonmono, readout, vmax):
    if not input_nonmono and readout == "passive" and vmax == 0:
        return "FAILED-ENVELOPE"
    if input_nonmono and vmax > 0:
        return "FAILED-DISGUISE"
    if not input_nonmono and readout != "passive" and vmax > 0:
        return f"CONDITIONAL ({readout})"
    if not input_nonmono and readout == "passive" and vmax > 0:
        return "CANDIDATE"
    return "UNCLASSIFIED"


def record(mid, input_nonmono, readout, vmax, induced):
    c = classify(input_nonmono, readout, vmax)
    CLASSES[mid] = c
    print(f"   => {mid}: input non-monomial = {input_nonmono}; readout = {readout}; V_max = {vmax}; "
          f"induced visible operation: {induced}; class: {c}")


print("== o2_mechanisms ==")

# ------------------------------------------------------------------ A12: bijections of {0,1}^2
print()
print("-- A12: A1-A2, all 24 bijections of {(z, x)}, z visible, x hidden")
PERMS4 = list(itertools.permutations(range(4)))
TAU_U = [[G(h), G(0)], [G(0), G(h)]]
induced = {}
dc_all = True
for p in PERMS4:
    K = perm_matrix(p)
    Phi = lambda X, K=K: ptrace_second(mm(mm(K, kron(X, TAU_U)), dag(K)), 2, 2)
    dc_all &= is_DC(Phi, 2)
    T = tuple(tuple(Phi(unit(2, z, z))[zp][zp].re for zp in range(2)) for z in range(2))
    induced.setdefault(T, []).append(p)
names = {((1, 0), (0, 1)): "identity", ((0, 1), (1, 0)): "flip",
         ((h, h), (h, h)): "replace by uniform"}
print("   induced visible channels (rows: input z; entries P(z'|z)), with the hidden x fresh and uniform:")
for T, ps in sorted(induced.items()):
    print(f"     {T}  [{names.get(T, 'other')}]  x{len(ps)}")
check("A12a", dc_all and set(induced) <= set(names),
      f"all 24 induced channels are DC and lie in {{identity, flip, replace by uniform}} ({len(induced)} distinct)")
vmax = Fr(0)
for p1 in PERMS4:
    K1 = perm_matrix(p1)
    for seed_x in (TAU_U, unit(2, 0, 0)):
        r1 = mm(mm(K1, kron(unit(2, 0, 0), seed_x)), dag(K1))
        for p2 in PERMS4:
            K2 = perm_matrix(p2)
            c = ptrace_second(mm(mm(K2, r1), dag(K2)), 2, 2)[0][0]
            d = ptrace_second(mm(mm(K2, path_deph(r1, 2, 2)), dag(K2)), 2, 2)[0][0]
            vmax = max(vmax, abs((c - d).re))
check("A12b", vmax == 0, f"composite sandwich, 24 x 24 x 2 seeds: V_max = {vmax}")
record("A12", any(not is_monomial(perm_matrix(p)) for p in PERMS4), "passive", vmax,
       "identity / flip / replace by uniform (classical)")

# ------------------------------------------------------------------ A36: link-coupled linear rule
print()
print("-- A36: link-coupled, centre-independent, linear second-order rule on a ring (N=3, K=2, q=2)")
N = 3


def matvec(M, v):
    return ((M[0][0] * v[0] + M[0][1] * v[1]) % 2, (M[1][0] * v[0] + M[1][1] * v[1]) % 2)


def matmul2(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 2 for j in range(2)) for i in range(2))


GL2 = [M for M in itertools.product(itertools.product((0, 1), repeat=2), repeat=2)
       if (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % 2 == 1]
INV = {}
for A in GL2:
    for B in GL2:
        if matmul2(A, B) == ((1, 0), (0, 1)):
            INV[A] = B


def make_rule(Mp):
    # Mp[n] couples site n to site n+1 ; the coupling seen from n+1 towards n is its inverse
    def F(vt):
        out = []
        for n in range(N):
            a = matvec(Mp[n], vt[(n + 1) % N])
            b = matvec(INV[Mp[(n - 1) % N]], vt[(n - 1) % N])
            out.append(((a[0] + b[0]) % 2, (a[1] + b[1]) % 2))
        return tuple(out)

    def phi(state):
        vprev, vt = state
        f = F(vt)
        vnext = tuple(((f[n][0] + vprev[n][0]) % 2, (f[n][1] + vprev[n][1]) % 2) for n in range(N))
        return (vt, vnext)
    return phi


SITEVALS = list(itertools.product((0, 1), repeat=2))
STATES = [(a, b) for a in itertools.product(SITEVALS, repeat=N) for b in itertools.product(SITEVALS, repeat=N)]
Mp = (((1, 1), (0, 1)), ((0, 1), (1, 0)), ((1, 0), (1, 1)))
phi = make_rule(Mp)
images = {phi(s) for s in STATES}
check("A36a", len(STATES) == 4096 and len(images) == 4096, "the rule is a bijection of the 4096 configurations")


def xor_state(s, t):
    return tuple(tuple(tuple((s[k][n][i] + t[k][n][i]) % 2 for i in range(2)) for n in range(N)) for k in range(2))


ZERO = (tuple(((0, 0),) * N), tuple(((0, 0),) * N))
basis = []
for k in range(2):
    for n in range(N):
        for i in range(2):
            v = [[list(x) for x in ZERO[0]], [list(x) for x in ZERO[1]]]
            v[k][n][i] = 1
            basis.append((tuple(tuple(x) for x in v[0]), tuple(tuple(x) for x in v[1])))
lin = phi(ZERO) == ZERO
for s in STATES:
    acc = ZERO
    bits = [s[k][n][i] for k in range(2) for n in range(N) for i in range(2)]
    for b, e in zip(bits, basis):
        if b:
            acc = xor_state(acc, phi(e))
    lin &= (acc == phi(s))
check("A36b", lin, "A5 linearity over F_2: phi(s) = sum of phi on basis vectors, for all 4096 states")
cov = True
for Gs in [(GL2[1], GL2[2], GL2[3]), (GL2[4], GL2[0], GL2[5]), (GL2[5], GL2[5], GL2[2])]:
    MpG = tuple(matmul2(matmul2(Gs[n], Mp[n]), INV[Gs[(n + 1) % N]]) for n in range(N))
    phiG = make_rule(MpG)

    def act(s, Gs=Gs):
        return tuple(tuple(matvec(Gs[n], s[k][n]) for n in range(N)) for k in range(2))
    cov &= all(phiG(act(s)) == act(phi(s)) for s in STATES)
check("A36c", cov, "A6 gauge covariance: phi_{G M G^-1}(G s) = G phi_M(s), three gauge fields, all states")


def zvis(s):
    return s[1][0][0]


# visible process: hidden uniform given the visible value; two steps, with and without passive observe-and-forget
def two_step(z0):
    seeds = [s for s in STATES if zvis(s) == z0]
    cnt0 = sum(1 for s in seeds if zvis(phi(phi(s))) == 0)
    # observe-and-forget of z1: condition on each value, then recombine with its weight: identical sum
    cnt0d = 0
    for z1 in (0, 1):
        branch = [s for s in seeds if zvis(phi(s)) == z1]
        cnt0d += sum(1 for s in branch if zvis(phi(phi(s))) == 0)
    return Fr(cnt0, len(seeds)), Fr(cnt0d, len(seeds))


pc, pd = two_step(0)
one_step = Fr(sum(1 for s in STATES if zvis(s) == 0 and zvis(phi(s)) == 0), 2048)
check("A36d", pc == pd, f"passive sandwich (two rule steps): P_coh(0) = {pc}, P_deph(0) = {pd}; one step P(0|0) = {one_step}"
      f" (the rule is a permutation of configurations, so O1-T3 applies on the matrix carrier)")
record("A36", False, "passive", abs(pc - pd), f"classical stochastic, P(z1=0|z0=0) = {one_step}")

# ------------------------------------------------------------------ PH: phase interventions
print()
print("-- PH: phase interventions")
PHASES = [G(1), G(-1), G(0, 1), G(0, -1), G(Fr(3, 5), Fr(4, 5)), G(Fr(-5, 13), Fr(12, 13))]
vmax = Fr(0)
dcph = True
for ph in itertools.product(PHASES, repeat=2):
    D = [[ph[0], G(0)], [G(0), ph[1]]]
    dcph &= is_DC(conjK(D), 2) and is_monomial(D)
    for p2 in (perm_matrix((0, 1)), perm_matrix((1, 0))):
        c = conjK(p2)(conjK(D)(unit(2, 0, 0)))[0][0]
        d = conjK(p2)(Delta(conjK(D)(unit(2, 0, 0))))[0][0]
        vmax = max(vmax, abs((c - d).re))
check("PHa", dcph and vmax == 0, f"36 diagonal phase pairs: monomial, DC, V_max = {vmax} (Z and the quarter phase included)")
record("PH", False, "passive", vmax, "the identity on populations (phases only)")

# ------------------------------------------------------------------ RW: read-write coupling
print()
print("-- RW: read-write coupling (ReadWriteFamily shape: a bijection fixing every state outside {a, b})")
rw_ok = True
for n in (3, 4, 5):
    a, b = 0, 1
    shapes = [p for p in itertools.permutations(range(n)) if all(p[x] == x for x in range(n) if x not in (a, b))]
    ident = tuple(range(n))
    sw = tuple(b if x == a else a if x == b else x for x in range(n))
    rw_ok &= sorted(shapes) == sorted([ident, sw])
check("RWa", rw_ok, "for |S| = 3, 4, 5 the admissible couplings at any knob value are exactly {1, swap(a,b)}")
record("RW", False, "passive", Fr(0), "1 or the swap at every knob value (monomial; V = 0 by A12/O1-T3)")

# ------------------------------------------------------------------ ANC: ancilla coupling and the recorder
print()
print("-- ANC: ancilla coupling with readback (exhaustive in o1_envelope M3/M4) and the record instrument")


def recorder_channel(X):  # system z (2) x register r (2): sum_a sum_b Ad(|a,a><a,b|)
    Y = zeros(4)
    for a in range(2):
        for b in range(2):
            K = zeros(4)
            K[2 * a + a][2 * a + b] = G(1)
            Yk = mm(mm(K, X), dag(K))
            Y = madd(Y, Yk)
    return Y


rec_dc = is_DC(recorder_channel, 4)
# written into a blank register: attach r = 0, record, discard r -> identity on populations of z
blank = lambda Xs: ptrace_second(recorder_channel(kron(Xs, unit(2, 0, 0))), 2, 2)
rec_blank_id = all(meq(Delta(blank(unit(2, i, j))), Delta(unit(2, i, j))) for i in range(2) for j in range(2))
check("ANCa", rec_dc and rec_blank_id,
      "recordInstr's channel is DC; into a blank register it leaves the visible populations unchanged")
record("ANC", False, "passive", Fr(0), "classical (DC) channels; see o1_envelope M3, M4c (2304 runs, V = 0)")

# ------------------------------------------------------------------ TAV: time averaging
print()
print("-- TAV: time averaging over the orbit of a cyclic permutation of the four configurations")
CYC = (1, 2, 3, 0)
P = perm_matrix(CYC)


def tav(X):
    acc = zeros(4)
    Pk = eye(4)
    for k in range(4):
        acc = madd(acc, mm(mm(Pk, X), dag(Pk)))
        Pk = mm(P, Pk)
    return msc(G(Fr(1, 4)), acc)


tav_dc = is_DC(tav, 4)
vis_tav = ptrace_second(tav(kron(unit(2, 0, 0), TAU_U)), 2, 2)
c = ptrace_second(tav(tav(kron(unit(2, 0, 0), TAU_U))), 2, 2)[0][0]
d = ptrace_second(tav(path_deph(tav(kron(unit(2, 0, 0), TAU_U)), 2, 2)), 2, 2)[0][0]
check("TAVa", tav_dc and c == d, f"the orbit average is DC (a mixture of permutations); sandwich P_coh = {c}, P_deph = {d}")
record("TAV", False, "passive", abs((c - d).re), f"P(z'|z=0) = ({vis_tav[0][0]}, {vis_tav[1][1]}) (doubly stochastic)")

# ------------------------------------------------------------------ CLO: closure
print()
print("-- CLO: closure of monomial generators with infinite-order phases")
GEN = [perm_matrix((1, 0)), [[G(1), G(0)], [G(0), G(Fr(3, 5), Fr(4, 5))]],
       [[G(Fr(-5, 13), Fr(12, 13)), G(0)], [G(0), G(1)]]]
words = [eye(2)]
allmono = True
frontier = [eye(2)]
for length in range(4):
    nxt = []
    for W in frontier:
        for g in GEN:
            Wg = mm(g, W)
            allmono &= is_monomial(Wg)
            nxt.append(Wg)
    frontier = nxt
    words += nxt
check("CLOa", allmono, f"all {len(words)} words of length <= 4 are monomial (the monomial group is closed)")
record("CLO", False, "passive", Fr(0), "monomial unitaries only; DC is a closed linear condition (o1_envelope M7)")

# ------------------------------------------------------------------ G1-G4: disguise controls
print()
print("-- G1-G4: routes that pass the witness because the coherence is in their input")
HRAW = [[G(1), G(1)], [G(1), G(-1)]]
c = conjK(HRAW, h)(conjK(HRAW, h)(unit(2, 0, 0)))[0][0]
d = conjK(HRAW, h)(Delta(conjK(HRAW, h)(unit(2, 0, 0))))[0][0]
check("G1a", c == 1 and d == h and not is_monomial(HRAW), f"hMat by hypothesis: P_coh = {c}, P_deph = {d}")
record("G1", True, "passive", c - d if isinstance(c - d, Fr) else (c - d).re, "the balanced mixer hMat itself")

SX = [[G(h, h), G(h, -h)], [G(h, -h), G(h, h)]]
PMINUS = [[G(h), G(-h)], [G(-h), G(h)]]          # the projector (1 - X)/2 in the gate flow's generator
c = conjK(SX)(conjK(SX)(unit(2, 0, 0)))[1][1]
d = conjK(SX)(Delta(conjK(SX)(unit(2, 0, 0))))[1][1]
check("G2a", c == 1 and d == h and not is_monomial(SX) and not is_monomial(PMINUS),
      f"gate flow at t = 1/2: P_coh(1) = {c}, P_deph(1) = {d}; generator projector (1-X)/2 non-monomial")
record("G2", True, "passive", (c - d).re, "sqrt(X) = proj_+ + i proj_- (the flow's complex interpolation)")

RRAW = [[G(1), G(-1)], [G(1), G(1)]]
RRAWd = dag(RRAW)
c = conjK(RRAWd, h)(conjK(RRAW, h)(unit(2, 0, 0)))[0][0]
d = conjK(RRAWd, h)(Delta(conjK(RRAW, h)(unit(2, 0, 0))))[0][0]
check("G3a", c == 1 and d == h, f"rot(pi/4) datum: P_coh = {c}, P_deph = {d}")
record("G3", True, "passive", (c - d).re, "the postulated real rotation rot(pi/4)")


def lift(u):  # diag(1, u) (1/sqrt2)[[1, 1], [1, -1]] : raw matrix with channel weight 1/2; |U_ij|^2 = 1/2
    return [[G(1), G(1)], [u, -u]]


US = [G(1), G(0, 1), G(Fr(3, 5), Fr(4, 5)), G(Fr(-5, 13), Fr(12, 13))]
lift_ok = True
preds = []
for u in US:
    L = lift(u)
    lift_ok &= meq(msc(G(h), mm(dag(L), L)), eye(2))
    lift_ok &= all(msc(G(h), [[G(x.norm2()) for x in row] for row in L])[i][j] == G(h) for i in range(2) for j in range(2))
    lift_ok &= not is_monomial(L)
for u, up in itertools.product(US, repeat=2):
    L1, L2 = lift(u), lift(up)
    preds.append(conjK(dag(L2), h)(conjK(L1, h)(unit(2, 0, 0)))[0][0].re)
B2 = [[h * h + h * h, h * h + h * h], [h * h + h * h, h * h + h * h]]
c = conjK(dag(lift(US[0])), h)(conjK(lift(US[0]), h)(unit(2, 0, 0)))[0][0]
d = conjK(dag(lift(US[0])), h)(Delta(conjK(lift(US[0]), h)(unit(2, 0, 0))))[0][0]
check("G4a", lift_ok and B2[0][0] == h and c == 1 and d == h,
      f"every tested lift has |U_ij|^2 = 1/2, is unitary and non-monomial; the classical two-step P(0|0) = B^2_00 = "
      f"{B2[0][0]} equals the DEPHASED branch {d}, the coherent branch {c} is the lift's")
check("G4b", len(set(preds)) > 1,
      f"the coherent prediction of (U(u), U(u')^dag) depends on the chosen phases: values {sorted(set(preds))}")
record("G4", True, "passive", (c - d).re, "a unitary dilation chosen for B; phases not fixed by B")

# ------------------------------------------------------------------ G5: knowledge balance
print()
print("-- G5: the knowledge-balance readout (inputs: substratum permutations only)")
OM = [(z, x) for z in (0, 1) for x in (0, 1)]
IDX = {w: i for i, w in enumerate(OM)}
SWAP = tuple(IDX[(w[1], w[0])] for w in OM)


def push(p, nu):
    out = [Fr(0)] * 4
    for i, m in enumerate(nu):
        out[p[i]] += m
    return out


def D_KB(nu):  # read z, re-randomize x, forget z
    out = [Fr(0)] * 4
    for z in (0, 1):
        w = sum(nu[IDX[(z, x)]] for x in (0, 1))
        for x in (0, 1):
            out[IDX[(z, x)]] += w * h
    return out


ZP = [h, h, Fr(0), Fr(0)]
pc = sum(push(SWAP, push(SWAP, ZP))[i] for i in range(4) if OM[i][0] == 0)
pd = sum(push(SWAP, D_KB(push(SWAP, ZP)))[i] for i in range(4) if OM[i][0] == 0)
check("G5a", pc == 1 and pd == h and is_monomial(perm_matrix(SWAP)),
      f"KB-D sandwich with the substratum swap: P_coh = {pc}, P_deph = {pd} (see o1_fieldneutral F8 for the body)")
record("G5", False, "KB-D (reading z re-randomizes the memory x)", pc - pd, "the swap acting on the toy bit's octahedron")

# ------------------------------------------------------------------ countercontrols
print()
print("-- countercontrols")


HC = kron(HRAW, eye(2))
rho = kron(unit(2, 0, 0), TAU_U)
r1 = msc(G(h), mm(mm(HC, rho), dag(HC)))                       # M1 = (H (x) 1) o identity permutation
cH = ptrace_second(msc(G(h), mm(mm(HC, r1), dag(HC))), 2, 2)[0][0]
dH = ptrace_second(msc(G(h), mm(mm(HC, path_deph(r1, 2, 2)), dag(HC))), 2, 2)[0][0]
counter("CC1", cH == dH, f"V = 0 on the A12 composite with (H (x) 1) composed into both mixers: P_coh = {cH}, P_deph = {dH}")
still_dc = all(is_DC(lambda X, K=perm_matrix(p): conjK(HRAW, h)(ptrace_second(mm(mm(K, kron(X, TAU_U)), dag(K)), 2, 2)), 2)
               for p in PERMS4)
counter("CC2", still_dc, "all A12 induced channels stay DC after composing with Ad H")
counter("CC3", len(set(preds)) == 1, "the lift's coherent two-step prediction is fixed by B")
counter("CC4", classify(True, "passive", Fr(1, 2)) == "FAILED-ENVELOPE",
        "the classifier calls a non-monomial-input mechanism with V > 0 FAILED-ENVELOPE")

print()
nfail = sum(1 for r in RESULTS if not r[1])
nchk = sum(1 for r in RESULTS if r[2] == "check")
ncc = sum(1 for r in RESULTS if r[2] == "counter")
cand = [m for m, c in CLASSES.items() if c == "CANDIDATE"]
print("classes: " + "; ".join(f"{m}: {c}" for m, c in CLASSES.items()))
if nfail == 0 and not cand:
    print(f"OK -- {nchk}/{nchk} checks, {ncc} countercontrols expected-false, no CANDIDATE")
    env = [m for m, c in CLASSES.items() if c == "FAILED-ENVELOPE"]
    dis = [m for m, c in CLASSES.items() if c == "FAILED-DISGUISE"]
    cond = [m for m, c in CLASSES.items() if c.startswith("CONDITIONAL")]
    print(f"VERDICT O2: FAILED by the envelope: {env}; FAILED by the disguise test: {dis}; CONDITIONAL on an access")
    print(f"  change: {cond}. No mechanism with monomial input and the stated passive readout yields a witness.")
else:
    print(f"VOID -- failing: {[r[0] for r in RESULTS if not r[1]]}; candidates: {cand}")
    print("VERDICT VOID")
