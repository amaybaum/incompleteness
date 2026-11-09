"""EXACT GENERIC CHECKS FOR BRIDGE-UNIT1 r3 (generic mathematical objects only).

Run under the owner's permission in #1211 c.6739843458 ("Allow generic checks (as #1210)").
Labelled controls on algebra stated in the r3 text; not evidence for any physical result.
No OI mechanism is run: no cubic lattice, no ring rule of the corpus, no encoding of the corpus.
Imports no earlier script. Exact arithmetic only (Python integers over F_2; sympy rationals).

K1  Functional sector split for second-order rules on a bipartite graph (r3 §10, point (a)).
    Graph: a fixed bipartite graph on 6 vertices (colour 0: a0,a1,a2; colour 1: b0,b1,b2),
    edges a0-b0, a0-b1, a1-b1, a1-b2, a2-b2, a2-b0, a0-b2 (not a ring of the corpus: a0 has
    degree 3). Rule over F_2: u_i(t+1) = g_i(u_j(t) : j ~ i) + v_i(t), v_i(t+1) = u_i(t),
    with per-vertex NONLINEAR g_i (AND/OR/majority mixtures) reading only neighbours.
    Types: u_i(0) has type chi_i, v_i(0) has type chi_i + 1 (mod 2).
    Claim checked exhaustively over all 2^12 initial configurations, for t = 1..5: u_i(t)
    depends only on initial variables of type t + chi_i (mod 2).
    Controls: the linear rule (g_i = XOR of neighbours) passes as well.
    Countercontrols (must FAIL the split): (c1) a self-term (g_i also reads u_i);
    (c2) a same-colour read (g_a0 also reads u_a1, through an AND).
K2  n1: K = [[1,1],[0,0]] is non-monomial and X -> K X K^dag maps diagonal to diagonal;
    a real rotation preserves diagonals under conjugation iff c*s = 0 (monomial).
K3  n2: weighted monomial Kraus family {2^(-1/2) P, 2^(-1/2) Q} (P, Q distinct permutations of
    3 points): |K|^p transition table is column-normalized iff p = 2; on permutation matrices
    alone every p > 0 gives the same 0/1 table.
K4  RB1: a non-monomial real orthogonal matrix fixing the all-ones vector, and a monomial
    unitary moving the all-ones ray (operator-level illustration of two independent conditions).
"""
import itertools
import sympy as sp

ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


# ---------------- K1 ----------------
V = ['a0', 'a1', 'a2', 'b0', 'b1', 'b2']
chi = {'a0': 0, 'a1': 0, 'a2': 0, 'b0': 1, 'b1': 1, 'b2': 1}
E = [('a0', 'b0'), ('a0', 'b1'), ('a1', 'b1'), ('a1', 'b2'), ('a2', 'b2'), ('a2', 'b0'), ('a0', 'b2')]
nbr = {x: [] for x in V}
for x, y in E:
    nbr[x].append(y)
    nbr[y].append(x)
for x in V:
    nbr[x].sort()
assert all(chi[x] != chi[y] for x, y in E)  # bipartite by construction


def maj(bits):
    return 1 if 2 * sum(bits) > len(bits) else 0


def g_nonlinear(x, u):
    n = [u[y] for y in nbr[x]]
    if x in ('a0', 'b1'):
        return maj(n) if len(n) % 2 else (n[0] & n[1])
    if x in ('a1', 'b2'):
        return n[0] | n[-1]
    return (n[0] & n[-1]) ^ n[0]


def g_linear(x, u):
    s = 0
    for y in nbr[x]:
        s ^= u[y]
    return s


def g_selfterm(x, u):
    return g_nonlinear(x, u) ^ (u[x] if x == 'a0' else 0)


def g_samecolour(x, u):
    if x == 'a0':
        return g_nonlinear(x, u) ^ (u['b0'] & u['a1'])
    return g_nonlinear(x, u)


VARS = [('u', x) for x in V] + [('v', x) for x in V]
vtype = {('u', x): chi[x] for x in V}
vtype.update({('v', x): (chi[x] + 1) % 2 for x in V})


def run(g, init, T):
    u = {x: init[('u', x)] for x in V}
    v = {x: init[('v', x)] for x in V}
    hist = []
    for _ in range(T):
        un = {x: g(x, u) ^ v[x] for x in V}
        v = u
        u = un
        hist.append(dict(u))
    return hist


def dependencies(g, T):
    deps = {(t, x): set() for t in range(1, T + 1) for x in V}
    configs = list(itertools.product((0, 1), repeat=len(VARS)))
    table = {}
    for c in configs:
        table[c] = run(g, dict(zip(VARS, c)), T)
    for c in configs:
        for k in range(len(VARS)):
            c2 = list(c)
            c2[k] ^= 1
            c2 = tuple(c2)
            h1, h2 = table[c], table[c2]
            for t in range(T):
                for x in V:
                    if h1[t][x] != h2[t][x]:
                        deps[(t + 1, x)].add(VARS[k])
    return deps


def split_holds(deps):
    return all(vtype[w] == (t + chi[x]) % 2 for (t, x), D in deps.items() for w in D)


T = 5
d_nl = dependencies(g_nonlinear, T)
check("K1 nonlinear bipartite-read rule: every u_i(t) depends only on type t+chi_i (t=1..5)",
      split_holds(d_nl))
check("K1 non-vacuous: some u_i(t) depends on >= 3 initial variables",
      any(len(D) >= 3 for D in d_nl.values()))
# nonlinearity witness: g_a1 = OR is not affine over F_2
check("K1 non-vacuous: OR is not affine over F_2 (OR(1,1) != OR(1,0)+OR(0,1)+OR(0,0))",
      (1 | 1) != ((1 | 0) ^ (0 | 1) ^ (0 | 0)))
check("K1 control: linear (XOR) rule also satisfies the split", split_holds(dependencies(g_linear, T)))
check("K1 countercontrol c1: a self-term breaks the split", not split_holds(dependencies(g_selfterm, T)))
check("K1 countercontrol c2: a same-colour read breaks the split",
      not split_holds(dependencies(g_samecolour, T)))

# ---------------- K2 ----------------
a, b = sp.symbols('a b')
Dg = sp.diag(a, b)
K = sp.Matrix([[1, 1], [0, 0]])


def is_monomial(M):
    return (all(sum(1 for j in range(M.cols) if M[i, j] != 0) == 1 for i in range(M.rows)) and
            all(sum(1 for i in range(M.rows) if M[i, j] != 0) == 1 for j in range(M.cols)))


out = sp.expand(K * Dg * K.H)
check("K2 K non-monomial", not is_monomial(K))
check("K2 K D K^dag diagonal for symbolic diagonal D", out[0, 1] == 0 and out[1, 0] == 0)
c, s = sp.symbols('c s', real=True)
U = sp.Matrix([[c, -s], [s, c]])
off = sp.expand((U * Dg * U.T)[0, 1])
check("K2 rotation: off-diagonal entry of U D U^T equals c*s*(a-b)", sp.expand(off - c * s * (a - b)) == 0)

# ---------------- K3 ----------------
p = sp.symbols('p', positive=True)
P = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
Q = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
w = 1 / sp.sqrt(2)
colsum = sp.simplify(sum((w ** p) * (P[j, 0] + Q[j, 0]) for j in range(3)))
check("K3 weighted monomial family: column sum 2^(1-p/2)", sp.simplify(colsum - 2 ** (1 - p / 2)) == 0)
check("K3 normalized only at p = 2", sp.solve(sp.Eq(colsum, 1), p) == [2])
perms = [sp.eye(3)[list(r), :] for r in itertools.permutations(range(3))]
check("K3 permutation matrices: |U|^p identical for p in {1/2, 1, 2, 3}",
      all(m.applyfunc(lambda e: sp.Abs(e) ** q) == m for m in perms for q in (sp.Rational(1, 2), 1, 2, 3)))

# ---------------- K4 ----------------
G = sp.Rational(2, 3) * sp.ones(3, 3) - sp.eye(3)
one3 = sp.ones(3, 1)
check("K4 G orthogonal, non-monomial, fixes all-ones",
      G.T * G == sp.eye(3) and not is_monomial(G) and G * one3 == one3)
Ph = sp.diag(1, sp.I)
vv = Ph * sp.ones(2, 1)
check("K4 diag(1,i) unitary, monomial, moves the all-ones ray",
      sp.simplify(Ph.H * Ph) == sp.eye(2) and is_monomial(Ph) and vv[0] * 1 != vv[1] * 1)

print("ALL PASS" if ok else "SOME CHECK FAILED")
