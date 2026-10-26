#!/usr/bin/env python3
"""E2: independent exact recomputation of every number in Introduction Appendix B (4a260ca9,
L219-L253), of the three-hidden-state variant and the Theorem 3 witness counts quoted in
FINDINGS R-04, written without reference to the audit's b5_check.py. Rational arithmetic
(fractions.Fraction) throughout; the x0-law dependence is carried as exact linear
polynomials in a; entropies of dyadic laws are evaluated exactly in bits. sympy is used only
for the 2x2 operator identities of B.3.

Usage: python3 -I E2_appendixB.py [out.json]
"""
import itertools, json, os, sys
from fractions import Fraction as F

checks = {}
def check(name, cond, value=None):
    checks[name] = {"ok": bool(cond), "value": value if value is None else str(value)}

def rooted(phi, V, H, prior, t):
    G = [[F(0)] * len(V) for _ in V]
    for ai, a in enumerate(V):
        for h, w in zip(H, prior):
            s = (a, h)
            for _ in range(t):
                s = phi[s]
            G[ai][V.index(s[0])] += w
    return G

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def inv2(M):
    d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return d, [[M[1][1] / d, -M[0][1] / d], [-M[1][0] / d, M[0][0] / d]]

I2 = [[F(1), F(0)], [F(0), F(1)]]

def cond_laws(phi, H):
    """P(x2=0|x1=1,x0=0) for x0 uniform; P(x2=0|x1=1) as linear polynomials (c0 + c1 a) in a = P(x0=0)."""
    num = [F(0), F(0)]; den = [F(0), F(0)]; n00 = d00 = F(0)
    for x0 in (0, 1):
        for h in H:
            s1 = phi[(x0, h)]; s2 = phi[s1]
            w = F(1, len(H))
            coef = [F(0), w] if x0 == 0 else [w, -w]          # P(x0=0)=a, P(x0=1)=1-a
            if s1[0] == 1:
                den = [den[0] + coef[0], den[1] + coef[1]]
                if s2[0] == 0:
                    num = [num[0] + coef[0], num[1] + coef[1]]
                if x0 == 0:
                    d00 += w
                    n00 += w * (s2[0] == 0)
    return n00 / d00, num, den

def b1_family(phi, V, H, tag):
    assert sorted(phi.values()) == sorted(phi.keys())
    check(tag + ": phi is a bijection", True)
    check(tag + ": phi is an involution", all(phi[phi[k]] == k for k in phi))
    pr = [F(1, len(H))] * len(H)
    G1, G2 = rooted(phi, V, H, pr, 1), rooted(phi, V, H, pr, 2)
    check(tag + ": Gamma_1 = [[2/3,1/3],[1/3,2/3]]", G1 == [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]], G1)
    check(tag + ": Gamma_2 = I", G2 == I2, G2)
    d, Gi = inv2(G1)
    L = mul(Gi, G2)
    check(tag + ": Gamma_1^-1 Gamma_2 = [[2,-1],[-1,2]]", L == [[2, -1], [-1, 2]], L)
    check(tag + ": unique divisor (det Gamma_1 != 0) has a negative entry", d != 0 and min(min(r) for r in L) < 0, d)
    check(tag + ": Gamma_1^2 = [[5/9,4/9],[4/9,5/9]]", mul(G1, G1) == [[F(5, 9), F(4, 9)], [F(4, 9), F(5, 9)]])
    c00, num, den = cond_laws(phi, H)
    check(tag + ": P(x2=0|x1=1,x0=0) = 1", c00 == 1, c00)
    a = F(1, 2)
    u = (num[0] + num[1] * a) / (den[0] + den[1] * a)
    check(tag + ": P(x2=0|x1=1) = 1/3 at x0 uniform", u == F(1, 3), u)
    # a/(2-a) identity as polynomials: num*(2-a) == a*den, coefficientwise (degree <= 2)
    lhs = [2 * num[0], 2 * num[1] - num[0], -num[1]]
    rhs = [F(0), den[0], den[1]]
    check(tag + ": P(x2=0|x1=1) = a/(2-a) for every a", lhs == rhs, (num, den))

# B.1, six hidden states (Introduction L221)
V = [0, 1]
H6 = [1, 2, 3, 4, 5, 6]
phi6 = {(x, h): ((1 - x, h) if h in (1, 2) else (x, {3: 4, 4: 3, 5: 6, 6: 5}[h])) for x in V for h in H6}
b1_family(phi6, V, H6, "B.1")
# three-hidden-state variant (FINDINGS R-04): h=1 flips x; h=2,3 swap
H3 = [1, 2, 3]
phi3 = {(x, h): ((1 - x, h) if h == 1 else (x, {2: 3, 3: 2}[h])) for x in V for h in H3}
b1_family(phi3, V, H3, "R-04 three-hidden")

# B.2
J = {(x0, x1, x0 ^ x1): F(1, 4) for x0 in (0, 1) for x1 in (0, 1)}
def two_time(i, j):
    M = [[F(0)] * 2 for _ in range(2)]
    for k, v in J.items():
        M[k[i]][k[j]] += v
    return [[e / sum(r) for e in r] for r in M]
half = [[F(1, 2)] * 2 for _ in range(2)]
check("B.2: P(X1|X0) = P(X2|X1) = P(X2|X0) = J/2", two_time(0, 1) == two_time(1, 2) == two_time(0, 2) == half)
G1, G2 = two_time(0, 1), two_time(0, 2)
check("B.2: P-divisible on {0,1,2} (Gamma_2 = Gamma_1 I; Gamma_t = Gamma_0 Gamma_t)", mul(G1, I2) == G2 and mul(I2, G1) == G1)
def log2_dyadic(p):
    k = 0
    while p < 1:
        p *= 2; k -= 1
    assert p == 1, "non-dyadic probability"
    return k
def cond_entropy(target, given):
    joint, marg = {}, {}
    for k, v in J.items():
        g = tuple(k[i] for i in given); t = (g, k[target])
        joint[t] = joint.get(t, 0) + v; marg[g] = marg.get(g, 0) + v
    return -sum(v * log2_dyadic(v / marg[g]) for (g, _), v in joint.items())
cmi = cond_entropy(2, (1,)) - cond_entropy(2, (0, 1))
check("B.2: I(X0;X2|X1) = 1 bit (exact, dyadic)", cmi == 1, cmi)

# B.3 card table: state (hole, burn); street = swap; peek variants
def card(protocol, anti=False):
    hit = tot = F(0)
    for h0, b0, c in itertools.product((0, 1), repeat=3):
        if anti and b0 != 1 - h0:
            continue
        w = F(1, 8) if not anti else F(1, 4)
        hole, burn = h0, b0
        for step in protocol:
            if step == "S":
                hole, burn = burn, hole
            elif step == "P":            # reveal hole, overwrite burn with fresh card c
                burn = c
            elif step == "Q":            # replace the hole card with fresh card c
                hole = c
            elif step == "R":            # reveal only
                pass
        tot += w; hit += w * (hole == h0)
    return hit / tot
check("B.3: one shuffle = 1/2", card("S") == F(1, 2), card("S"))
check("B.3: two shuffles = 1", card("SS") == 1, card("SS"))
check("B.3: two shuffles with a peek = 1/2", card("SPS") == F(1, 2), card("SPS"))
g1 = [[F(1, 2)] * 2 for _ in range(2)]
check("B.3: Markov prediction (Gamma_1^2)_hh = 1/2", mul(g1, g1)[0][0] == F(1, 2) and mul(g1, g1)[1][1] == F(1, 2))
phic = {(h, b): (b, h) for h in (0, 1) for b in (0, 1)}
pr = [F(1, 2), F(1, 2)]
check("B.3: Gamma_1 = J/2, Gamma_2 = I", rooted(phic, [0, 1], [0, 1], pr, 1) == g1 and rooted(phic, [0, 1], [0, 1], pr, 2) == I2)
check("B.3: rows of Gamma_1 Lambda equal for every Lambda (Gamma_1 has equal rows), so != I", g1[0] == g1[1])
check("B.3: reveal-only peek = 1", card("SRS") == 1)
check("B.3: replace-hole peek = 1", card("SQS") == 1)
anti_ok = True
for t in range(1, 7):
    Gt = [[F(0)] * 2 for _ in range(2)]
    for h0 in (0, 1):
        hole, burn = h0, 1 - h0
        for _ in range(t):
            hole, burn = burn, hole
        Gt[h0][hole] = F(1)
    anti_ok &= sorted(map(tuple, Gt)) == [(0, 1), (1, 0)] if t % 2 else Gt == I2
check("B.3: anticorrelated b=1-h: Gamma_t alternates permutation/I for t<=6 (divisors are permutations)", anti_ok)
check("B.3: anticorrelated one-shuffle match probability = 0", card("S", anti=True) == 0)

# B.3 operator identities (sympy, exact symbolic)
import sympy as sp
x = sp.Matrix(2, 2, sp.symbols("r0:4"))
paulis = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
check("B.3: sum_o s_o X s_o = 2 tr(X) I", sp.simplify(sum((s * x * s for s in paulis), sp.zeros(2)) - 2 * x.trace() * sp.eye(2)) == sp.zeros(2))
check("B.3: sum_o s_o (s_o X s_o / 4) s_o = X", sp.simplify(sum((s * (s * x * s / 4) * s for s in paulis), sp.zeros(2)) - x) == sp.zeros(2))
SW = sp.zeros(4)
for i in range(2):
    for j in range(2):
        SW[2 * i + j, 2 * j + i] = 1
def tr_hidden(M):   # system = first factor
    return sp.Matrix(2, 2, lambda i, k: sum(M[2 * i + l, 2 * k + l] for l in range(2)))
kr = lambda A, B: sp.kronecker_product(A, B)
one = tr_hidden(SW * kr(x, sp.eye(2) / 2) * SW.T)
two = tr_hidden(SW * SW * kr(x, sp.eye(2) / 2) * SW.T * SW.T)
fixed = tr_hidden(SW * kr(x, sp.Matrix([[1, 0], [0, 0]])) * SW.T)
check("B.3: one-step channel = tr(rho) I/2", sp.simplify(one - x.trace() * sp.eye(2) / 2) == sp.zeros(2))
check("B.3: two-step map = identity", sp.simplify(two - x) == sp.zeros(2))
check("B.3: fixed |0> burn card: one-step map = tr(rho)|0><0|", sp.simplify(fixed - x.trace() * sp.Matrix([[1, 0], [0, 0]])) == sp.zeros(2))

# Theorem 3 witnesses (FINDINGS R-04): exhaustive over bijections and over every prior support
def order(phi):
    L, cur = 1, {k: phi[k] for k in phi}
    while any(cur[k] != k for k in cur):
        cur = {k: phi[cur[k]] for k in cur}; L += 1
    return L
def witness(phi, Vs, support):
    L = order(phi)
    def pattern(t):
        P = [[False] * len(Vs) for _ in Vs]
        for ai, a in enumerate(Vs):
            for h in support:
                s = (a, h)
                for _ in range(t):
                    s = phi[s]
                P[ai][Vs.index(s[0])] = True
        return P
    pats = [pattern(t) for t in range(2 * L + 1)]
    ident = [[i == j for j in range(len(Vs))] for i in range(len(Vs))]
    for s in range(L):
        ov = any(pats[s][i][c] and pats[s][k][c] for i in range(len(Vs)) for k in range(i + 1, len(Vs)) for c in range(len(Vs)))
        if ov and any(pats[n] == ident for n in range(s + 1, s + L + 1)):
            return True
    return False
census = {}
for nv, nh in ((2, 1), (3, 1), (2, 2), (2, 3), (3, 2)):
    Vs, Hs = list(range(nv)), list(range(nh)); states = list(itertools.product(Vs, Hs))
    full = anysupp = 0; total = 0
    for img in itertools.permutations(states):
        phi = dict(zip(states, img)); total += 1
        wfull = witness(phi, Vs, Hs)
        full += wfull
        anysupp += any(witness(phi, Vs, S) for r in range(1, nh + 1) for S in itertools.combinations(Hs, r))
    census["%dx%d" % (nv, nh)] = {"bijections": total, "witness_full_support_prior": full, "witness_some_prior": anysupp}
check("Thm3: |H| = 1 gives no witness (|V| = 2, 3)", census["2x1"]["witness_some_prior"] == 0 and census["3x1"]["witness_some_prior"] == 0)
check("Thm3: (2,2): 16 of 24 bijections are witnesses under a full-support (e.g. uniform) prior",
      census["2x2"]["witness_full_support_prior"] == 16 and census["2x2"]["bijections"] == 24, census["2x2"])
phi_card = {(h, b): (b, h) for h in (0, 1) for b in (0, 1)}
phi_xor = {(v, h): (v ^ h, h) for v in (0, 1) for h in (0, 1)}
check("Thm3: card swap and (v xor h, h) are (2,2) witnesses", witness(phi_card, [0, 1], [0, 1]) and witness(phi_xor, [0, 1], [0, 1]))
check("Thm3: B.1 phi (6 hidden) and the 3-hidden variant are witnesses", witness(phi6, V, H6) and witness(phi3, V, H3))

out = {"checks": checks, "theorem3_census": census, "all_ok": all(c["ok"] for c in checks.values())}
js = json.dumps(out, indent=1, sort_keys=True)
if len(sys.argv) > 1:
    if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
        sys.exit("refusing to overwrite this script")
    open(sys.argv[1], "w").write(js + "\n")
print(js)
sys.exit(0 if out["all_ok"] else 1)
