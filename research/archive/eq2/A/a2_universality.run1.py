"""EQ2-A probe A2 -- the Lie-free exact-universality route for the conditional n-token theorem.  Exact.
Research only; base bcbc516f.  Usage: python3 -I -B a2_universality.py

Route (each lemma is standard; literature: Barenco et al., PRA 52, 3457 (1995); Nielsen-Chuang Sec. 4.5 --
unverified, egress blocked).  Qubit 0 is the most significant bit and the first tensor factor.
  U1  two-level decomposition: every U in U(N) is a product of two-level unitaries (Givens).
  U2  Gray code: a two-level unitary on (e_x, e_y) is P^-1 C^{n-1}(W) P, P a product of multi-controlled NOTs.
  U3  Barenco Lemma 6.1 (n = 2) and Lemma 7.2 (recursion): C^n(V^2) = C_{x_n->t}(V) C^{n-1}_{->x_n}(X)
      C_{x_n->t}(V^H) C^{n-1}_{->x_n}(X) C^{n-1}_{->t}(V).
  U4  square root of a 2x2 unitary: S = (U + d I)/sqrt(tr U + 2 d), d^2 = det U, when tr U + 2 d != 0.
  U5  SWAP routing along a path: G_(i,j) = SWAP_(i,k) G_(k,j) SWAP_(i,k);  SWAP = CNOT CNOT' CNOT.
  E2E an end-to-end exact decomposition, over Q(i), of a two-level unitary on (000, 111) of three qubits into
      gates each acting on an EDGE of the path tree 0-1-2.
  G   (independent re-implementation, not the coordinator's code) for every unlabelled tree on n = 3..6 vertices
      the edge Pauli strings close under anticommuting products to all 4^n - 1 strings; countercontrol: every
      one-edge-deleted forest closes at sum over components of (4^|C| - 1).

DECISION RULE (fixed before the first run): verdict `A2-ROUTE-LEMMAS-EXACT` iff every check passes, including the
countercontrols (each must FAIL the identity it is a control for: wrong order in U3, a missing conjugation in U5,
the wrong branch in U4 is allowed only where tr U + 2d = 0).  Zero tests: exact sympy arithmetic over Q(i); for U1,
entries with radicals are decided by `minimal_polynomial(e) == x` (exact algebraic zero test).  No floating point.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq2a_lib as L  # noqa: E402

check = L.check
X = L.SX


def is_zero_exact(M):
    xs = sp.Symbol("xs")
    for e in M:
        e = sp.expand(e)
        if e == 0:
            continue
        if sp.minimal_polynomial(e, xs) != xs:
            return False
    return True


def embed(n, U, qubits):
    """Embed a k-qubit gate U acting on the ordered qubit positions `qubits` into n qubits."""
    N = 2 ** n
    M = zeros(N, N)
    k = len(qubits)
    for b in range(N):
        bits = [(b >> (n - 1 - q)) & 1 for q in range(n)]
        sub_in = 0
        for q in qubits:
            sub_in = 2 * sub_in + bits[q]
        for sub_out in range(2 ** k):
            c = U[sub_out, sub_in]
            if c == 0:
                continue
            obits = list(bits)
            for pos, q in enumerate(qubits):
                obits[q] = (sub_out >> (k - 1 - pos)) & 1
            bo = 0
            for q in range(n):
                bo = 2 * bo + obits[q]
            M[bo, b] += c
    return M


def controlled(V):
    """2-qubit controlled-V, control first."""
    C = eye(4)
    C[2:, 2:] = V
    return C


def multi_controlled(n, controls, target, V):
    """C^{|controls|}(V): V on `target` iff every control bit is 1."""
    N = 2 ** n
    M = zeros(N, N)
    for b in range(N):
        bits = [(b >> (n - 1 - q)) & 1 for q in range(n)]
        if all(bits[c] == 1 for c in controls):
            tb = bits[target]
            for to in range(2):
                c = V[to, tb]
                if c == 0:
                    continue
                obits = list(bits)
                obits[target] = to
                bo = 0
                for q in range(n):
                    bo = 2 * bo + obits[q]
                M[bo, b] += c
        else:
            M[b, b] += 1
    return M


def two_level(N, i, j, G):
    M = eye(N)
    M[i, i], M[i, j], M[j, i], M[j, j] = G[0, 0], G[0, 1], G[1, 0], G[1, 1]
    return M


# ---------------------------------------------------------------- U1 Givens two-level decomposition, N = 4
U = L.exact_unitary(4, seed=11)
check("U1 the test matrix is an exact unitary over Q(i)", L.is_unitary(U))
Wk = U
factors = []
N = 4
for c in range(N - 1):
    for r in range(N - 1, c, -1):
        a, b = Wk[c, c], Wk[r, c]
        if sp.expand(b) == 0:
            continue
        s = sp.sqrt(sp.expand(a * sp.conjugate(a) + b * sp.conjugate(b)))
        G = Matrix([[sp.conjugate(a) / s, sp.conjugate(b) / s], [-b / s, a / s]])
        Gf = two_level(N, c, r, G)
        factors.append(Gf)
        Wk = (Gf * Wk).applyfunc(sp.expand)
upper_ok = all(is_zero_exact(Matrix([Wk[r, c]])) for c in range(N) for r in range(N) if r != c)
check(f"U1 after {len(factors)} two-level steps the remainder is diagonal (exact algebraic zero test)", upper_ok)
D = sp.diag(*[Wk[i, i] for i in range(N)])
prod = eye(N)
for Gf in factors:
    prod = prod * Gf.H
recon = (prod * D).applyfunc(sp.expand)
check("U1 U = G_1^H ... G_m^H D exactly (each G_k two-level, D diagonal unitary)", is_zero_exact(recon - U))
check("U1 every factor is two-level and unitary",
      all(sum(1 for i in range(N) if Gf[i, i] != 1 or any(Gf[i, j] != 0 for j in range(N) if j != i)) <= 2
          and is_zero_exact(Gf.H * Gf - eye(N)) for Gf in factors))

# ---------------------------------------------------------------- U3 Barenco 6.1 and 7.2
V = L.exact_unitary(2, seed=5)
check("U3 V is an exact unitary over Q(i)", L.is_unitary(V))
W = (V * V).applyfunc(sp.expand)
n = 3  # qubits (c1, c2, t) = (0, 1, 2)
lhs = multi_controlled(3, [0, 1], 2, W)
CNOT12 = embed(3, controlled(X), [0, 1])
rhs = embed(3, controlled(V), [1, 2]) * CNOT12 * embed(3, controlled(V.H), [1, 2]) * CNOT12 \
    * embed(3, controlled(V), [0, 2])
check("U3 Lemma 6.1: C^2(V^2) = C_{c2->t}(V) CNOT_{c1->c2} C_{c2->t}(V^H) CNOT_{c1->c2} C_{c1->t}(V)",
      (lhs - rhs).applyfunc(sp.expand).is_zero_matrix)
rhs_bad = embed(3, controlled(V), [0, 2]) * CNOT12 * embed(3, controlled(V.H), [1, 2]) * CNOT12 \
    * embed(3, controlled(V), [1, 2])
check("U3 countercontrol: the same five factors in reversed order do NOT give C^2(V^2)",
      not (lhs - rhs_bad).applyfunc(sp.expand).is_zero_matrix)
# Lemma 7.2 at n = 3 controls (4 qubits: x1, x2, x3, t = 0, 1, 2, 3)
lhs4 = multi_controlled(4, [0, 1, 2], 3, W)
rhs4 = embed(4, controlled(V), [2, 3]) * multi_controlled(4, [0, 1], 2, X) * embed(4, controlled(V.H), [2, 3]) \
    * multi_controlled(4, [0, 1], 2, X) * multi_controlled(4, [0, 1], 3, V)
check("U3 Lemma 7.2 recursion at three controls: C^3(V^2) = C_{x3->t}(V) C^2(X) C_{x3->t}(V^H) C^2(X) C^2_{->t}(V)",
      (lhs4 - rhs4).applyfunc(sp.expand).is_zero_matrix)

# ---------------------------------------------------------------- U4 square roots of 2x2 unitaries
SX_root = Matrix([[1 + I, 1 - I], [1 - I, 1 + I]]) / 2
check("U4 sqrt(X) = (1/2)[[1+i,1-i],[1-i,1+i]] is unitary and squares to X",
      L.is_unitary(SX_root) and (SX_root * SX_root - X).applyfunc(sp.expand).is_zero_matrix)
Uq = W
d = V.det()
den2 = sp.expand(Uq.trace() + 2 * d)
check("U4 tr(V^2) + 2 det V = (tr V)^2 (so the radicand is a square)", sp.expand(den2 - V.trace() ** 2) == 0)
S = ((Uq + d * eye(2)) / V.trace()).applyfunc(sp.expand)
check("U4 S = (U + d I)/tr(V), d = det V, is a square root of U = V^2 (Cayley-Hamilton)",
      (S * S - Uq).applyfunc(sp.expand).is_zero_matrix and L.is_unitary(S))

# ---------------------------------------------------------------- U5 SWAP routing on the path 0-1-2
CN = controlled(X)
SWAP2 = L.swap_matrix([2, 2], [1, 0])
CN_rev = SWAP2 * CN * SWAP2
check("U5 SWAP = CNOT_{0->1} CNOT_{1->0} CNOT_{0->1}", (CN * CN_rev * CN - SWAP2).is_zero_matrix)
G4 = L.exact_unitary(4, seed=23)
S01 = embed(3, SWAP2, [0, 1])
moved = (S01 * embed(3, G4, [1, 2]) * S01).applyfunc(sp.expand)
check("U5 routing: SWAP_(0,1) G_(1,2) SWAP_(0,1) = G_(0,2)", (moved - embed(3, G4, [0, 2])).applyfunc(sp.expand).is_zero_matrix)
check("U5 countercontrol: without the conjugation G_(1,2) != G_(0,2)",
      not (embed(3, G4, [1, 2]) - embed(3, G4, [0, 2])).applyfunc(sp.expand).is_zero_matrix)

# ---------------------------------------------------------------- E2E two-level unitary on (000, 111), path 0-1-2
Wt = W  # the 2x2 block, with square root V over Q(i)
target = two_level(8, 0, 7, Wt)
# Gray path 000 -> 001 -> 011 -> 111.  P1 swaps 000<->001 (flip q2 iff q0=0, q1=0); P2 swaps 001<->011 (flip q1 iff
# q0=0, q2=1).  Then 011 <-> 111 differ in q0: apply W on q0 controlled by q1 = 1, q2 = 1.
Xq = lambda q: embed(3, X, [q])  # noqa: E731
P1 = Xq(0) * Xq(1) * multi_controlled(3, [0, 1], 2, X) * Xq(1) * Xq(0)
P2 = Xq(0) * multi_controlled(3, [0, 2], 1, X) * Xq(0)
P = P2 * P1
core = multi_controlled(3, [1, 2], 0, Wt)
check("U2 Gray code: two-level W on (000,111) = P^-1 C^2_{q1 q2 -> q0}(W) P",
      ((P.H * core * P) - target).applyfunc(sp.expand).is_zero_matrix)


def c2_edges(controls, t, Vroot, Vfull):
    """C^2_{controls -> t}(Vfull), Vroot^2 = Vfull, as a list of 2-qubit gates (U3), each on an arbitrary pair."""
    c1, c2 = controls
    return [("cV", (c1, t), Vroot), ("cX", (c1, c2), X), ("cV", (c2, t), Vroot.H), ("cX", (c1, c2), X),
            ("cV", (c2, t), Vroot)]  # rightmost first when multiplied in list order from the right


def to_matrix(gates, n):
    M = eye(2 ** n)
    for kind, (a, b), Vg in gates:      # gates listed in time order: first applied first
        G = controlled(Vg)
        M = embed(n, G, [a, b]) * M
    return M


# time-ordered gate lists for C^2 via Lemma 6.1: first C_{c1->t}(V), CNOT, C_{c2->t}(V^H), CNOT, C_{c2->t}(V)
def c2_time(c1, c2, t, Vr):
    return [("cV", (c1, t), Vr), ("cX", (c1, c2), X), ("cV", (c2, t), Vr.H), ("cX", (c1, c2), X), ("cV", (c2, t), Vr)]


check("U3 time-ordered list for C^2 reproduces Lemma 6.1",
      (to_matrix(c2_time(0, 1, 2, V), 3) - multi_controlled(3, [0, 1], 2, W)).applyfunc(sp.expand).is_zero_matrix)
edges = {(0, 1), (1, 2)}


def route(gates):
    """Rewrite every 2-qubit gate on a non-edge pair of the path 0-1-2 by SWAP routing (U5)."""
    out = []
    swap01 = ("SW", (0, 1), None)
    for g in gates:
        kind, (a, b), Vg = g
        if (min(a, b), max(a, b)) in edges:
            out.append(g)
        else:   # the only non-edge pair is {0, 2}: route qubit 0 through 1
            a2 = 1 if a == 0 else a
            b2 = 1 if b == 0 else b
            out += [swap01, (kind, (a2, b2), Vg), swap01]
    return out


def to_matrix_routed(gates, n):
    M = eye(2 ** n)
    for kind, (a, b), Vg in gates:
        G = SWAP2 if kind == "SW" else controlled(Vg)
        M = embed(n, G, [a, b]) * M
    return M


SX_r = SX_root
# multi-controlled NOT gates C^2(X) via Lemma 6.1 with sqrt(X); conjugations by X are single-qubit (put on an edge)
def mcx_time(c1, c2, t):
    return c2_time(c1, c2, t, SX_r)


def xgate(q):
    other = 1 if q != 1 else 0
    return [("1q", (q, other), X)]


def to_matrix_any(gates, n):
    M = eye(2 ** n)
    for kind, (a, b), Vg in gates:
        if kind == "SW":
            G = SWAP2
        elif kind == "1q":
            G = L.kron(Vg, eye(2))
        else:
            G = controlled(Vg)
        M = embed(n, G, [a, b]) * M
    return M


P1_t = xgate(0) + xgate(1) + mcx_time(0, 1, 2) + xgate(1) + xgate(0)
P2_t = xgate(0) + mcx_time(0, 2, 1) + xgate(0)
P_t = P1_t + P2_t
Pinv_t = [(k, ab, (Vg.H if Vg is not None else None)) for (k, ab, Vg) in reversed(P_t)]
core_t = c2_time(1, 2, 0, V)
full_t = route(P_t + core_t + Pinv_t)
Mfull = to_matrix_any(full_t, 3).applyfunc(sp.expand)
all_edges = all((min(a, b), max(a, b)) in edges for (_, (a, b), _) in full_t)
check(f"E2E {len(full_t)} gates, every gate acts on an edge of the path 0-1-2", all_edges)
check("E2E the edge-gate product equals the two-level unitary on (000,111) exactly over Q(i)",
      (Mfull - target).applyfunc(sp.expand).is_zero_matrix)


# ---------------------------------------------------------------- G independent Pauli-string closure on trees
def tree_closure(n, edges_):
    def enc(sites):  # sites: dict q -> pauli index 1..3 ; encode (x bits, z bits)
        xb = zb = 0
        for q, p in sites.items():
            if p in (1, 2):
                xb |= 1 << q
            if p in (2, 3):
                zb |= 1 << q
        return (xb, zb)
    gens = set()
    for a, b in edges_:
        for pa in range(4):
            for pb in range(4):
                if pa == 0 and pb == 0:
                    continue
                s = {}
                if pa:
                    s[a] = pa
                if pb:
                    s[b] = pb
                gens.add(enc(s))
    members = set(gens)
    frontier = list(gens)
    while frontier:
        new = []
        for p in frontier:
            for q in list(members):
                if (bin((p[0] & q[1]) ^ (p[1] & q[0])).count("1") & 1):
                    r = (p[0] ^ q[0], p[1] ^ q[1])
                    if r != (0, 0) and r not in members:
                        members.add(r)
                        new.append(r)
        frontier = new
    return len(members)


def unlabelled_trees(n):
    seen, out = set(), []
    for seq in itertools.product(range(n), repeat=n - 2):
        deg = [1] * n
        for v in seq:
            deg[v] += 1
        es, sq = [], list(seq)
        for v in sq:
            leaf = min(i for i in range(n) if deg[i] == 1)
            es.append((leaf, v))
            deg[leaf] -= 1
            deg[v] -= 1
        u, w = [i for i in range(n) if deg[i] == 1]
        es.append((u, w))
        adj = {i: [] for i in range(n)}
        for a, b in es:
            adj[a].append(b)
            adj[b].append(a)

        def canon(v, par):
            return "(" + "".join(sorted(canon(c, v) for c in adj[v] if c != par)) + ")"
        key = min(canon(r, -1) for r in range(n))
        if key not in seen:
            seen.add(key)
            out.append(es)
    return out


def comps(n, es):
    par = list(range(n))

    def f(v):
        while par[v] != v:
            par[v] = par[par[v]]
            v = par[v]
        return v
    for a, b in es:
        par[f(a)] = f(b)
    cs = {}
    for v in range(n):
        cs.setdefault(f(v), []).append(v)
    return [len(c) for c in cs.values()]


expected = {3: 1, 4: 2, 5: 3, 6: 6}
for nn in range(3, 7):
    trees = unlabelled_trees(nn)
    sizes = [tree_closure(nn, t) for t in trees]
    check(f"G n = {nn}: {len(trees)} unlabelled trees, every closure = {4 ** nn - 1}",
          len(trees) == expected[nn] and all(s == 4 ** nn - 1 for s in sizes))
    okc = True
    for t in trees:
        for k in range(len(t)):
            forest = t[:k] + t[k + 1:]
            if tree_closure(nn, forest) != sum(4 ** c - 1 for c in comps(nn, forest) if c >= 2):
                okc = False
    check(f"G n = {nn} countercontrol: every one-edge-deleted forest closes at the component sum", okc)

ok = L.summary("a2_universality")
print("VERDICT " + ("A2-ROUTE-LEMMAS-EXACT" if ok else "A2-NOT-RENDERED"))
sys.exit(0 if ok else 1)
