"""Node 3 probe: classical substratum enlargement, observer settings, drop-one premises, antiunitary.

Exact arithmetic only: Python integers/Fractions for the exhaustive finite block, SymPy for the
continuum blocks. Run with `python3 -I -B enlarge.py`. Output is deterministic.
"""
import itertools
from fractions import Fraction

import sympy as sp

RESULTS = []


def check(tag, cond, note=""):
    RESULTS.append((tag, bool(cond)))
    print(f"{'PASS' if cond else 'FAIL'}  {tag}  {note}")


# ---------------------------------------------------------------------------------------------
# Block A: exhaustive finite core, two independent code paths.
#   Visible V = {0,1}; hidden H = {0,1,2}; every bijection b of V x H (720).
#   Path 1: full coherence-level action Ad_U on rho (x) |h><h|, then partial trace over H.
#   Path 2: predicted Kraus K_{h,x'} = sum_{v : x(v,h) = x'} |v'(v,h)><v|.
#   Checks: equality on all four matrix units; every Kraus is a 0/1 partial permutation;
#   every effect K^dag K is diagonal; nonnegativity preserved.
# ---------------------------------------------------------------------------------------------
V = (0, 1)
H = (0, 1, 2)
STATES = [(v, h) for v in V for h in H]
IDX = {s: i for i, s in enumerate(STATES)}


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def dag(A):  # entries here are real integers / Fractions
    return [list(r) for r in zip(*A)]


def path1_channel(b, h, E):
    """Ad_U (E (x) |h><h|) then trace over H; U the permutation matrix of b."""
    n = len(STATES)
    rho = [[0] * n for _ in range(n)]
    for v1 in V:
        for v2 in V:
            if E[v1][v2]:
                rho[IDX[(v1, h)]][IDX[(v2, h)]] = E[v1][v2]
    U = [[0] * n for _ in range(n)]
    for s in STATES:
        U[IDX[b[s]]][IDX[s]] = 1
    out = matmul(matmul(U, rho), dag(U))
    red = [[0, 0], [0, 0]]
    for (v1, x1) in STATES:
        for (v2, x2) in STATES:
            if x1 == x2:
                red[v1][v2] += out[IDX[(v1, x1)]][IDX[(v2, x2)]]
    return red


def path2_kraus(b, h):
    ks = {}
    for v in V:
        vp, xp = b[(v, h)]
        K = ks.setdefault(xp, [[0, 0], [0, 0]])
        K[vp][v] = 1
    return [ks[x] for x in sorted(ks)]


def apply_kraus(Ks, E):
    red = [[0, 0], [0, 0]]
    for K in Ks:
        M = matmul(matmul(K, E), dag(K))
        for i in range(2):
            for j in range(2):
                red[i][j] += M[i][j]
    return red


def is_partial_perm01(K):
    rows_ok = all(sum(1 for x in r if x) <= 1 for r in K)
    cols_ok = all(sum(1 for r in K if r[j]) <= 1 for j in range(len(K[0])))
    vals_ok = all(x in (0, 1) for r in K for x in r)
    return rows_ok and cols_ok and vals_ok


UNITS = []
for p in V:
    for q in V:
        E = [[0, 0], [0, 0]]
        E[p][q] = 1
        UNITS.append(E)

bijections = []
for perm in itertools.permutations(STATES):
    bijections.append({s: perm[i] for i, s in enumerate(STATES)})

agree = pp = diag_eff = nonneg = True
n_kraus_shapes = set()
for b in bijections:
    for h in H:
        Ks = path2_kraus(b, h)
        for K in Ks:
            pp &= is_partial_perm01(K)
            KK = matmul(dag(K), K)
            diag_eff &= (KK[0][1] == 0 and KK[1][0] == 0)
            n_kraus_shapes.add(tuple(map(tuple, K)))
        for E in UNITS:
            r1 = path1_channel(b, h, E)
            r2 = apply_kraus(Ks, E)
            agree &= (r1 == r2)
            nonneg &= all(x >= 0 for row in r1 for x in row)
check("A1", agree, "720 bijections x 3 hidden points: Ad_U + partial trace == partial-permutation Kraus form")
check("A2", pp, "every induced Kraus operator is a 0/1 partial permutation of V")
check("A3", diag_eff, "every induced effect K^dag K is diagonal")
check("A4", nonneg, "every induced map sends matrix units to entrywise-nonnegative matrices")
check("A5", len(n_kraus_shapes) <= 7, f"distinct nonzero Kraus shapes seen: {len(n_kraus_shapes)} (partial perms of Fin 2: 6 nonzero)")

# A6: a two-step protocol with configuration readout of V and feed-forward choice of the second
# bijection, hidden point carried; outcome maps keep partial-permutation Kraus.
second = bijections[::60]  # 12 fixed second-stage bijections, chosen by outcome
ok_ff = True
for b1 in bijections:
    for h in H:
        for c0, c1 in [(0, 1), (3, 7), (11, 5)]:
            choice = {0: second[c0], 1: second[c1]}
            for outcome in V:
                # Kraus: for each x' after b1 and readout `outcome` of v', apply choice[outcome]
                ks = {}
                for v in V:
                    vp, xp = b1[(v, h)]
                    if vp != outcome:
                        continue
                    vpp, xpp = choice[outcome][(vp, xp)]
                    # coherence survives only between v with identical final hidden point
                    K = ks.setdefault(xpp, [[0, 0], [0, 0]])
                    K[vpp][v] = 1
                for K in ks.values():
                    ok_ff &= is_partial_perm01(K)
check("A6", ok_ff, "two-step protocols with readout + feed-forward: Kraus stay 0/1 partial permutations")

# A7: grouping with a nonuniform rational prior: channel = sum_P w_P Ad_P, with sum_P w_P P^dag P = I.
prior = {0: Fraction(1, 2), 1: Fraction(1, 3), 2: Fraction(1, 6)}
ok_group = True
for b in bijections[:200]:
    w = {}
    for h in H:
        for K in path2_kraus(b, h):
            key = tuple(map(tuple, K))
            w[key] = w.get(key, 0) + prior[h]
    S = [[Fraction(0)] * 2 for _ in range(2)]
    for key, wt in w.items():
        K = [list(r) for r in key]
        KK = matmul(dag(K), K)
        for i in range(2):
            for j in range(2):
                S[i][j] += wt * KK[i][j]
    ok_group &= (S == [[1, 0], [0, 1]])
check("A7", ok_group, "with a nonuniform prior the channel is sum_P w_P Ad_P over finitely many P, trace preserving")

# ---------------------------------------------------------------------------------------------
# Block B: continuum hidden sector (h in [0,1)), continuous parameters and continuous time.
# ---------------------------------------------------------------------------------------------
t, th, s, s2, h_ = sp.symbols("t theta s s2 h", real=True)
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
a, b_, c, d = sp.symbols("a b c d")
RHO = sp.Matrix([[a, b_], [c, d]])


def mix_channel(p):
    return lambda R: (1 - p) * R + p * X * R * X


# B1: coupling family T_theta(v,h) = (v xor [h < theta], h), h uniform: weight of Kraus X is theta.
wX = sp.integrate(sp.Piecewise((1, h_ < th), (0, True)), (h_, 0, 1))
wX = sp.simplify(wX.subs(th, sp.Rational(3, 10)))
check("B1a", wX == sp.Rational(3, 10), "weight of Kraus X in T_theta at theta=3/10 by exact integration")


def choi(ch):
    M = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            E = sp.zeros(2, 2)
            E[i, j] = 1
            out = ch(E)
            for k in range(2):
                for l in range(2):
                    M[2 * i + k, 2 * j + l] = out[k, l]
    return M


# rank of the Choi matrix: 2 for 0<theta<1, 1 at theta in {0,1}
r_mid = choi(mix_channel(sp.Rational(1, 3))).rank()
r_end0 = choi(mix_channel(0)).rank()
r_end1 = choi(mix_channel(1)).rank()
check("B1b", (r_mid, r_end0, r_end1) == (2, 1, 1), "T_theta channel: Choi rank 2 inside (0,1), rank 1 only at theta in {0,1}")
diff = sp.simplify(mix_channel(th)(RHO) - mix_channel(s)(RHO))
check("B1c", sp.simplify(diff[0, 1] - (s - th) * (b_ - c)) == 0, "distinct theta give distinct channels: uncountably many available maps, finitely many unitary ones")

# B2: circle flow. S = [0,2) with visible v = floor(x); hidden h = x - v; phi_t(x) = x + t mod 2.
# Prior density on h: f(h) = (pi/2) sin(pi h), the same for both visible starts.
f = sp.pi / 2 * sp.sin(sp.pi * h_)
check("B2a", sp.simplify(sp.integrate(f, (h_, 0, 1)) - 1) == 0, "prior density normalized")
p_lo = sp.simplify(sp.integrate(f, (h_, 1 - t, 1)))     # t in [0,1]: v=0 crosses iff h >= 1-t
p_hi = sp.simplify(sp.integrate(f, (h_, 0, 2 - t)))     # t in [1,2]: v=0 lands in [1,2) iff h < 2-t
target = sp.sin(sp.pi * t / 2) ** 2
check("B2b", sp.simplify(p_lo - target) == 0 and sp.simplify(p_hi - target) == 0,
      "flip probability of the flow is exactly sin^2(pi t/2) on [0,2]")
# Kraus: for each h the final hidden point (h+t) mod 1 does not depend on v, so coherence between
# v=0 and v=1 survives and the Kraus operator is I or X; the channel is the mixture.
Rx = lambda x: sp.cos(x / 2) * I2 - sp.I * sp.sin(x / 2) * X
U = Rx(sp.pi * t)
rooted = sp.simplify(sp.Abs((U * sp.Matrix([1, 0]))[1]) ** 2)
check("B2c", sp.simplify(sp.expand_complex(rooted) - target) == 0,
      "the layer flow Ad R_x(pi t) has the same rooted flip probability")
E00 = sp.Matrix([[1, 0], [0, 0]])
flow_out = mix_channel(target)(E00)
qm_out = sp.simplify(U * E00 * U.H)
off = sp.simplify(qm_out[0, 1] - flow_out[0, 1])
check("B2d", sp.simplify(off.subs(t, sp.Rational(1, 2))) != 0 and flow_out[0, 1] == 0,
      f"channels differ off the diagonal: Ad R_x gives {sp.simplify(qm_out[0,1])}, flow gives 0")
J = sp.ones(2, 2)
# PreservesNonneg quantifies over all entrywise-nonnegative inputs; a linear map preserves it iff
# it sends every matrix unit to an entrywise-nonnegative matrix. (J itself is not a witness: every
# R_x fixes the all-ones ray.)
flow_half = mix_channel(target.subs(t, sp.Rational(1, 2)))
flow_nonneg = all(sp.simplify(e) >= 0 for Eu in [sp.Matrix(2, 2, lambda i, j: int((i, j) == pq))
                                                 for pq in [(0, 0), (0, 1), (1, 0), (1, 1)]]
                  for e in flow_half(Eu))
rx_e00 = sp.simplify(Rx(sp.pi / 2) * E00 * Rx(sp.pi / 2).H)
rx_J = sp.simplify(Rx(sp.pi / 2) * J * Rx(sp.pi / 2).H)
check("B2e", flow_nonneg and sp.im(rx_e00[0, 1]) != 0 and rx_J == J,
      f"flow channel at t=1/2 preserves nonnegativity on all matrix units; Ad R_x(pi/2) sends E00 to off-diagonal {rx_e00[0,1]} and fixes J")
# Indivisibility signature: Phi_{1/2} o Phi_{1/2} != Phi_1 (the flow is a group on S, not on V).
p_half = target.subs(t, sp.Rational(1, 2))
comp = mix_channel(p_half)(mix_channel(p_half)(E00))
one = mix_channel(target.subs(t, 1))(E00)
check("B2f", sp.simplify(comp - one) != sp.zeros(2, 2), "Phi_1/2 o Phi_1/2 != Phi_1: the visible family is not a semigroup")

# B3: observer settings as a continuum. Outcome 1 iff (v=0 and h<s) or (v=1 and h<s2), h uniform:
# effect diag(s, s2); every such effect commutes with every other; sharp only at s,s2 in {0,1}.
Eff = lambda u, w: sp.diag(u, w)
r, r2 = sp.symbols("r r2", real=True)
comm = sp.simplify(Eff(s, s2) * Eff(r, r2) - Eff(r, r2) * Eff(s, s2))
check("B3a", comm == sp.zeros(2, 2), "setting-indexed effects diag(s,s2) pairwise commute")
sharp = sp.solve([sp.Eq(s ** 2, s), sp.Eq(s2 ** 2, s2)], [s, s2], dict=True)
check("B3b", sorted((d_[s], d_[s2]) for d_ in sharp) == [(0, 0), (0, 1), (1, 0), (1, 1)],
      "sharp members of the setting continuum are the configuration projectors only")
Pplus = sp.Matrix([[1, 1], [1, 1]]) / 2
check("B3c", Pplus[0, 1] != 0, "the X-basis projector has an off-diagonal entry: not in the setting continuum")

# ---------------------------------------------------------------------------------------------
# Block C: drop-one premises. Each removal breaks the conclusion; cardinality removal (Block B)
# does not.
# ---------------------------------------------------------------------------------------------
CNOT_vh = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control v, target h


def ptrace_h(M):
    out = sp.zeros(2, 2)
    for i in range(2):
        for j in range(2):
            out[i, j] = sum(M[2 * i + k, 2 * j + k] for k in range(2))
    return out


def chan_with_hidden(sigma):
    return lambda R: sp.simplify(ptrace_h(CNOT_vh * sp.kronecker_product(R, sigma) * CNOT_vh.T))


minus = sp.Matrix([1, -1]) / sp.sqrt(2)
plus = sp.Matrix([1, 1]) / sp.sqrt(2)
coh_minus = chan_with_hidden(minus * minus.T)
coh_plus = chan_with_hidden(plus * plus.T)
classical = chan_with_hidden(sp.diag(sp.Rational(1, 2), sp.Rational(1, 2)))
check("C1a", sp.simplify(coh_minus(RHO) - Z * RHO * Z) == sp.zeros(2, 2),
      "coherent hidden prior |-> with CNOT v->h: the visible channel is Ad Z exactly")
check("C1b", coh_minus(J)[0, 1] == -1, "Ad Z sends J to a matrix with entry -1 (nonnegativity broken)")
check("C1c", sp.simplify(classical(RHO) - sp.diag(a, d)) == sp.zeros(2, 2),
      "the same coupling with a distribution prior is the dephasing channel")
check("C1d", sp.simplify(coh_plus(RHO) - RHO) == sp.zeros(2, 2), "control: coherent prior |+> gives the identity")
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
E01 = sp.Matrix([[0, 1], [0, 0]])
check("C2", any(e < 0 for e in (Hd * E01 * Hd.T)), "non-permutation process (Hadamard): a matrix unit goes to a matrix with a negative entry")
W = Hd
Xw = W * X * W.T
check("C3", sp.simplify(Xw - Z) == sp.zeros(2, 2) and (Xw * J * Xw.T)[0, 1] == -1,
      "identification by a fixed basis change W=H: native X acts as Ad Z, nonnegativity broken")
Ppi = sp.Matrix([[1, -sp.I], [sp.I, 1]]) / 2
check("C4", sp.im((Ppi * J * Ppi.H)[0, 1]) != 0 or sp.im(Ppi[0, 1]) != 0,
      "non-configuration (Y-basis) Lueders branch: complex off-diagonal Kraus entries")

# ---------------------------------------------------------------------------------------------
# Block D: the global antiunitary.
# ---------------------------------------------------------------------------------------------
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
check("D1", choi(lambda R: R.T) == SWAP and min(SWAP.eigenvals()) == -1,
      "transpose (time reversal on descriptions) has Choi matrix SWAP with eigenvalue -1: positive, not CP")
perms4 = []
for perm in itertools.permutations(range(4)):
    P = sp.zeros(4, 4)
    for i, j in enumerate(perm):
        P[j, i] = 1
    perms4.append(P)
R4 = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"x{i}{j}"))
check("D2", all(((P * R4.T * P.T).T - P * R4 * P.T) == sp.zeros(4, 4) for P in perms4),
      "tau o Ad_P o tau = Ad_P for all 24 pair permutations")
k = sp.symbols("k0:8")
K1 = sp.Matrix([[k[0], k[1]], [k[2], k[3]]])
K2 = sp.Matrix([[k[4], k[5]], [k[6], k[7]]])
one2 = sp.Matrix([1, 1])
lhs = K1.conjugate().H * one2 + K2.conjugate().H * one2
rhs = (K1.H * one2 + K2.H * one2).conjugate()
check("D3", sp.simplify(lhs - rhs) == sp.zeros(2, 1),
      "sum conj(K)^dag 1 = conj(sum K^dag 1): OnesNormal is invariant under entrywise conjugation of Kraus lists")
al, be = sp.symbols("alpha beta", real=True)
u = sp.Matrix([1, 1]) / sp.sqrt(2)
Uof = sp.exp(sp.I * al) * u * u.T + sp.exp(sp.I * be) * minus * minus.T
check("D4", sp.simplify(Uof.conjugate() * one2 - sp.exp(-sp.I * al) * one2) == sp.zeros(2, 1),
      "conj(U) of a ones-fixing unitary fixes the all-ones ray")
# D5: group generated by complex conjugation and the 24 pair permutations (pairs (U, flag)).
gens = [(P, 0) for P in perms4] + [(sp.eye(4), 1)]


def mul(g1, g2):
    U1, f1 = g1
    U2, f2 = g2
    return (U1 * (U2.conjugate() if f1 else U2), f1 ^ f2)


elems = {(tuple(sp.eye(4)), 0): (sp.eye(4), 0)}
frontier = list(elems.values())
while frontier:
    new = []
    for g in frontier:
        for q in gens:
            m = mul(g, q)
            key = (tuple(m[0]), m[1])
            if key not in elems:
                elems[key] = m
                new.append(m)
    frontier = new
unit_parts_perm = all(all(x in (0, 1) for x in g[0]) for g in elems.values())
check("D5", len(elems) == 48 and unit_parts_perm, f"generated group has {len(elems)} elements; every unitary part is a permutation")
thv = sp.symbols("vartheta", real=True)
Dg = sp.diag(1, sp.exp(-sp.I * thv))
branch_sum = (Dg.H * one2 + (Z * Dg).H * one2) / sp.sqrt(2)
branch_sum_rev = (Dg.conjugate().H * one2 + (Z * Dg).conjugate().H * one2) / sp.sqrt(2)
check("D6", sp.simplify(branch_sum_rev - branch_sum.conjugate()) == sp.zeros(2, 1),
      "time reversal of the heralded phase gadget conjugates its OnesNormal sum; no deterministic phase appears")

npass = sum(1 for _, ok in RESULTS if ok)
print(f"SUMMARY  {npass} PASS  {len(RESULTS) - npass} FAIL")
