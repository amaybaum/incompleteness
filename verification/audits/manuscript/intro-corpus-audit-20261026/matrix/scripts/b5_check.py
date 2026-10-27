"""B5 exact checks for Introduction Appendix B (rational arithmetic only)."""
from fractions import Fraction as F
from itertools import permutations, product
import sympy as sp

def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def rooted(phi, V, H, prior, t):
    """Gamma_t[a][j] = P(x_t=j | x_0=a), hidden prior independent of x_0."""
    G = [[F(0)] * len(V) for _ in V]
    for ai, a in enumerate(V):
        for h, ph in zip(H, prior):
            s = (a, h)
            for _ in range(t):
                s = phi[s]
            G[ai][V.index(s[0])] += ph
    return G

def is_perm(G):
    return all(sorted(r) == [0] * (len(r) - 1) + [1] for r in G)

out = {}
# ---------------- B.1 ----------------
V = [0, 1]; H = [1, 2, 3, 4, 5, 6]
phi = {}
for x in V:
    for h in H:
        if h in (1, 2):
            phi[(x, h)] = (1 - x, h)
        else:
            phi[(x, h)] = (x, {3: 4, 4: 3, 5: 6, 6: 5}[h])
assert sorted(phi.values()) == sorted(phi.keys())  # bijection
pr = [F(1, 6)] * 6
G1 = rooted(phi, V, H, pr, 1); G2 = rooted(phi, V, H, pr, 2)
out['B1_G1'] = G1; out['B1_G2'] = G2
M1 = sp.Matrix(G1); M2 = sp.Matrix(G2)
out['B1_det_G1'] = M1.det()
out['B1_G1inv_G2'] = (M1.inv() * M2).tolist()
out['B1_G1sq'] = matmul(G1, G1)
# conditionals with x0 law P(x0=0)=a
a = sp.Symbol('a')
def joint(pa):
    J = {}
    for x0, px0 in ((0, pa), (1, 1 - pa)):
        for h in H:
            s1 = phi[(x0, h)]; s2 = phi[s1]
            key = (x0, s1[0], s2[0])
            J[key] = J.get(key, 0) + px0 * sp.Rational(1, 6)
    return J
J = joint(sp.Rational(1, 2))
num = sum(v for k, v in J.items() if k[0] == 0 and k[1] == 1 and k[2] == 0)
den = sum(v for k, v in J.items() if k[0] == 0 and k[1] == 1)
out['B1_P(x2=0|x1=1,x0=0)'] = num / den
num = sum(v for k, v in J.items() if k[1] == 1 and k[2] == 0)
den = sum(v for k, v in J.items() if k[1] == 1)
out['B1_P(x2=0|x1=1) uniform'] = num / den
Ja = joint(a)
num = sum(v for k, v in Ja.items() if k[1] == 1 and k[2] == 0)
den = sum(v for k, v in Ja.items() if k[1] == 1)
out['B1_P(x2=0|x1=1) general a'] = sp.simplify(num / den)
# P-indivisibility on {0,1,2}: unique divisor for (1,2) has a negative entry
out['B1_divisor_negative'] = any(e < 0 for r in (M1.inv() * M2).tolist() for e in r)

# three-hidden-state variant reproducing every B.1 number
H3 = [1, 2, 3]
phi3 = {}
for x in V:
    for h in H3:
        phi3[(x, h)] = (1 - x, h) if h == 1 else (x, {2: 3, 3: 2}[h])
g1 = rooted(phi3, V, H3, [F(1, 3)] * 3, 1); g2 = rooted(phi3, V, H3, [F(1, 3)] * 3, 2)
J3 = {}
for x0 in V:
    for h in H3:
        s1 = phi3[(x0, h)]; s2 = phi3[s1]
        J3[(x0, s1[0], s2[0])] = J3.get((x0, s1[0], s2[0]), 0) + F(1, 2) * F(1, 3)
c1 = sum(v for k, v in J3.items() if k[:3] == (0, 1, 0)) / sum(v for k, v in J3.items() if k[:2] == (0, 1))
c2 = sum(v for k, v in J3.items() if k[1:] == (1, 0)) / sum(v for k, v in J3.items() if k[1] == 1)
J3a = {}
for x0, px0 in ((0, a), (1, 1 - a)):
    for h in H3:
        s1 = phi3[(x0, h)]; s2 = phi3[s1]
        key = (x0, s1[0], s2[0])
        J3a[key] = J3a.get(key, 0) + px0 * sp.Rational(1, 3)
c3 = sp.simplify(sum(v for k, v in J3a.items() if k[1:] == (1, 0)) / sum(v for k, v in J3a.items() if k[1] == 1))
out['H3_variant'] = dict(G1=g1, G2=g2, cond_x0=c1, cond=c2, cond_general_a=c3,
                         cond_general_a_is_a_over_2_minus_a=sp.simplify(c3 - a / (2 - a)) == 0)
# Countercontrols: the a-test rejects a/(1+a) and the constant 1/3, and c3 takes 1/3, 1, 0 at a = 1/2, 1, 0.
out['H3_variant_countercontrols'] = (sp.simplify(c3 - a / (1 + a)) != 0, sp.simplify(c3 - sp.Rational(1, 3)) != 0,
                                     [c3.subs(a, v) for v in (sp.Rational(1, 2), 1, 0)] == [sp.Rational(1, 3), 1, 0])

# ---------------- minimality search ----------------
def theorem3_witness(phi, V, H, prior, nmax):
    """Exists s<n<=nmax with Gamma_n = I and two distinct rows of Gamma_s overlapping."""
    Gs = [rooted(phi, V, H, prior, t) for t in range(nmax + 1)]
    I = [[F(int(i == j)) for j in range(len(V))] for i in range(len(V))]
    for n in range(1, nmax + 1):
        if Gs[n] != I:
            continue
        for s in range(n):
            G = Gs[s]
            for i in range(len(V)):
                for k in range(i + 1, len(V)):
                    if any(G[i][c] > 0 and G[k][c] > 0 for c in range(len(V))):
                        return (s, n)
    return None

summary = {}
for nv, nh in ((1, 2), (2, 1), (1, 3), (3, 1), (2, 2), (2, 3)):
    Vs = list(range(nv)); Hs = list(range(nh)); states = list(product(Vs, Hs))
    cnt = 0; cnt_inv = 0; tot = 0
    # every prior on a grid is unnecessary for the (|V|=1 or |H|=1) impossibility; use uniform
    for img in permutations(states):
        ph = dict(zip(states, img)); tot += 1
        w = theorem3_witness(ph, Vs, Hs, [F(1, nh)] * nh, 12)
        if w:
            cnt += 1
            G1 = rooted(ph, Vs, Hs, [F(1, nh)] * nh, w[0])
            if sp.Matrix(G1).det() != 0 and not is_perm(G1):
                cnt_inv += 1
    summary[(nv, nh)] = (tot, cnt, cnt_inv)
out['theorem3_search_uniform_prior (total, witnesses, witnesses with invertible non-perm Gamma_s)'] = summary
# |H|=1: Gamma_t always a permutation (proof: hidden coordinate constant, phi acts as a permutation of V)

# ---------------- B.2 ----------------
J = {}
for x0, x1 in product((0, 1), repeat=2):
    J[(x0, x1, x0 ^ x1)] = F(1, 4)
def cond(i, j):
    M = [[F(0)] * 2 for _ in range(2)]
    for k, v in J.items():
        M[k[i]][k[j]] += v
    return [[e / sum(r) for e in r] for r in M]
out['B2_P(x1|x0)'] = cond(0, 1); out['B2_P(x2|x1)'] = cond(1, 2); out['B2_P(x2|x0)'] = cond(0, 2)
import math
def H_(ps):
    return -sum(p * math.log2(p) for p in ps if p > 0)
# I(X0;X2|X1) = H(X2|X1) - H(X2|X0,X1), computed exactly from J (sympy logarithms base 2)
def H_cond(J, given, target):
    """H(X_target | X_given) in bits, exactly."""
    pg, pj = {}, {}
    for k, v in J.items():
        g = tuple(k[i] for i in given)
        pg[g] = pg.get(g, 0) + v
        pj[(g, k[target])] = pj.get((g, k[target]), 0) + v
    return -sum(sp.Rational(v) * sp.log(sp.Rational(v) / sp.Rational(pg[g]), 2) for (g, _), v in pj.items() if v)
def cmi(J):
    return sp.simplify(H_cond(J, (1,), 2) - H_cond(J, (0, 1), 2))
out['B2_I(X0;X2|X1)_bits'] = cmi(J)
# Countercontrols for cmi: X2 independent of (X0, X1) gives 0; X2 = X1 gives 0; a noisy copy of X0 gives 1 - h(1/4).
from itertools import product as _prod
_noisy = {(x0, x1, x2): sp.Rational(1, 4) * (sp.Rational(3, 4) if x2 == x0 else sp.Rational(1, 4))
          for x0, x1, x2 in _prod((0, 1), repeat=3)}
_h = -(sp.Rational(1, 4) * sp.log(sp.Rational(1, 4), 2) + sp.Rational(3, 4) * sp.log(sp.Rational(3, 4), 2))
out['B2_countercontrols (independent 0, copy-of-X1 0, noisy copy 1-h(1/4))'] = (
    cmi({k: sp.Rational(1, 8) for k in _prod((0, 1), repeat=3)}) == 0,
    cmi({(x0, x1, x1): sp.Rational(1, 4) for x0, x1 in _prod((0, 1), repeat=2)}) == 0,
    sp.simplify(cmi(_noisy) - (1 - _h)) == 0)
# RHP14 Eq.(15) support (x1,x2,x3): (1,0,0),(0,1,0),(0,0,1),(1,1,1) -> x3 = NOT(x1 xor x2)
rhp = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)]
out['RHP15_is_xor_flipped'] = all(x3 == 1 - (x1 ^ x2) for x1, x2, x3 in rhp)

# ---------------- B.3 card game ----------------
def enumerate_protocol(prot, anti=False):
    hits = F(0); total = F(0)
    for h0, b0 in product((0, 1), repeat=2):
        if anti and b0 != 1 - h0:
            continue
        w = F(1, 2) if anti else F(1, 4)
        for c in (0, 1):  # fresh card for a peek
            hole, burn = h0, b0
            for step in prot:
                if step == 'S':
                    hole, burn = burn, hole
                elif step == 'P':      # reveal hole, overwrite burn
                    burn = c
                elif step == 'R':      # reveal only
                    pass
                elif step == 'Q':      # replace the hole card
                    hole = c
            total += w / 2
            hits += (w / 2) * (hole == h0)
    return hits / total
out['card_one_shuffle'] = enumerate_protocol('S')
out['card_two_shuffles'] = enumerate_protocol('SS')
out['card_two_with_peek'] = enumerate_protocol('SPS')
out['card_two_reveal_only'] = enumerate_protocol('SRS')
out['card_two_replace_hole'] = enumerate_protocol('SQS')
G1 = [[F(1, 2)] * 2 for _ in range(2)]
out['card_markov_G1sq_diag'] = matmul(G1, G1)[0][0]
out['card_anticorrelated_one_shuffle'] = enumerate_protocol('S', anti=True)

# quantum: swap channel, Pauli identity, instrument
s0 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
X = sp.Matrix(2, 2, sp.symbols('x0:4'))
lhs = sum((s * X * s for s in (s0, sx, sy, sz)), sp.zeros(2))
out['pauli_identity'] = sp.simplify(lhs - 2 * X.trace() * sp.eye(2)) == sp.zeros(2)
two_step = sum(((s * (sp.Rational(1, 4) * s * X * s) * s) for s in (s0, sx, sy, sz)), sp.zeros(2))
out['pauli_instrument_then_correct_is_identity'] = sp.simplify(two_step - X) == sp.zeros(2)
# swap channel with burn card in I/2 and in |0><0|
def kron(A, B):
    return sp.Matrix(sp.BlockMatrix([[A[i, j] * B for j in range(A.cols)] for i in range(A.rows)]))
SW = sp.zeros(4)
for i in range(2):
    for j in range(2):
        SW[2 * j + i, 2 * i + j] = 1
def ptrace_hidden(M):
    return sp.Matrix(2, 2, lambda i, k: sum(M[2 * i + l, 2 * k + l] for l in range(2)))
rho = X
one = ptrace_hidden(SW * kron(rho, sp.eye(2) / 2) * SW.T)
two = ptrace_hidden(SW * SW * kron(rho, sp.eye(2) / 2) * SW.T * SW.T)
out['swap_uniform_one_step'] = sp.simplify(one - X.trace() * sp.eye(2) / 2) == sp.zeros(2)
out['swap_uniform_two_step_identity'] = sp.simplify(two - X) == sp.zeros(2)
P0 = sp.Matrix([[1, 0], [0, 0]])
onef = ptrace_hidden(SW * kron(rho, P0) * SW.T)
out['swap_fixed_one_step'] = sp.simplify(onef - X.trace() * P0) == sp.zeros(2)
# Choi of the constant channel is separable (product) -> entanglement-breaking
for k, v in out.items():
    print(k, '=', v)
