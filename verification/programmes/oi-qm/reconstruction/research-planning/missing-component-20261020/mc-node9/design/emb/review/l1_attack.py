"""Attempts to break L1 (one visible site, both coordinates clean, rest uniform, prior support 4
=> posterior support >= 2).  Exact.  Also the mixed-declaration probe (two visible sites, only one
clean pair)."""
import random
import sys
from itertools import combinations, product
from indep import *

random.seed(20261021)
viol = 0
checked = 0


def check_phi(P, n, R0, toys, um, F_sites):
    """L1 check at one Heisenberg map P.  Visible set at the evaluation time = F_sites."""
    global viol, checked
    F = [P[x] for x in F_sites] + [P[n + x] for x in F_sites]
    hits = []
    for toy in toys:
        T = [P[toy], P[n + toy]]
        checked += 1
        if prior_exp(T, um) == 2 and support_exp(F, T, um) == 0:
            hits.append(toy)
    return hits


# 1. every symmetric L with diagonal (self-loops) at n <= 4, R = {r}, every toy, every t in period
for n in (2, 3, 4):
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
        L = adj_from_edges(n, edges)
        M = upd(n, L)
        assert is_symp(M, n)
        per = period(M)
        for r in range(n):
            um = ((1 << (2 * n)) - 1) & ~((1 << r) | (1 << (n + r)))
            P = ident(2 * n)
            for t in range(1, per):
                P = mul(M, P)
                h = check_phi(P, n, r, [x for x in range(n) if x != r], um, [r])
                if h:
                    viol += 1
                    print("VIOLATION self-loop graph", n, edges, r, t, h)
print(f"[1] self-loop graphs n<=4, every t in period: checked {checked}, violations {viol}")

# 2. E3 random gating words with self-loops and multi-edges (XOR multiplicity), n = 3..6
c0 = checked
for n in (3, 4, 5, 6):
    for trial in range(300):
        r = 0
        um = ((1 << (2 * n)) - 1) & ~((1 << r) | (1 << (n + r)))
        P = ident(2 * n)
        for d in range(40):
            edges = [(random.randrange(n), random.randrange(n)) for _ in range(random.randrange(0, 2 * n))]
            P = mul(upd(n, adj_from_edges(n, edges)), P)
            if check_phi(P, n, r, range(1, n), um, [r]):
                viol += 1
                print("VIOLATION E3 word", n, trial, d)
print(f"[2] random E3 words with self-loops/multi-edges: checked {checked - c0}, violations {viol}")

# 3. random symplectic maps: products of random transvections x -> x + om(a,x) a, plus the
#    lattice updates; visible site 0 clean at time 0, visible site at time t = any site s.
def transvection(a, n):
    N = 2 * n
    rows = []
    # matrix of x -> x + om(a, x) a : output coord i = x_i + a_i * om(a, x)
    # om(a, x) as a functional: f = (a_v, a_u) swapped
    m = (1 << n) - 1
    f = ((a >> n) & m) | ((a & m) << n)
    for i in range(N):
        rows.append((1 << i) ^ (f if (a >> i) & 1 else 0))
    return rows


c0 = checked
for n in (2, 3, 4, 5, 6):
    for trial in range(400):
        P = ident(2 * n)
        for _ in range(random.randrange(1, 30)):
            P = mul(transvection(random.randrange(1, 1 << (2 * n)), n), P)
        assert is_symp(P, n)
        um = ((1 << (2 * n)) - 1) & ~((1 << 0) | (1 << n))
        for s in range(n):
            if check_phi(P, n, 0, [x for x in range(n) if x != s], um, [s]):
                viol += 1
                print("VIOLATION random symplectic", n, trial, s)
print(f"[3] random symplectic maps (clean site 0, visible site s, any toy != s): checked {checked - c0}, violations {viol}")

# 4. control: a NON-symplectic bijection must be able to break the bound (the hypothesis is
#    load-bearing).  Visible site 0 clean; toy site 1.  Map: visible <- toy, toy <- (u_toy + ... )
n = 2
# rows: u0' = u1, v0' = v1, u1' = u1, v1' = v1 + u0 ... => toy unchanged, visible copies toy
P = [1 << 1, 1 << 3, 0, 0]
P = [0] * 4
P[0] = 1 << 1          # u0' = u1
P[2] = 1 << 3          # v0' = v1
P[1] = (1 << 1) ^ (1 << 0)  # u1' = u1 + u0
P[3] = (1 << 3) ^ (1 << 2)  # v1' = v1 + v0
um = 0b1010
F = [P[0], P[2]]
T = [P[1], P[3]]
print(f"[4] countercontrol (bijective={rk(P) == 4}, symplectic={is_symp(P, 2)}): prior 2^{prior_exp(T, um)},"
      f" posterior 2^{support_exp(F, T, um)}  -> {'breaks the bound (control RED-able, good)' if support_exp(F, T, um) == 0 and prior_exp(T, um) == 2 else 'does not break'}")

# 5. mixed declarations: two visible sites, only ONE clean pair (the other visible site uniform,
#    or only one coordinate of it clean); every graph n <= 5 (labelled, simple), every t in period.
res = {}
for n in (3, 4, 5):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        edges = [pairs[i] for i in range(len(pairs)) if (mask >> i) & 1]
        M = upd(n, adj_from_edges(n, edges))
        per = period(M)
        pw = [ident(2 * n)]
        for t in range(1, per):
            pw.append(mul(M, pw[-1]))
        for R in combinations(range(n), 2):
            a, b = R
            for decl, clean in (("a FULL, b NONE", [a, n + a]),
                                ("a FULL, b U", [a, n + a, b]),
                                ("a FULL, b V", [a, n + a, n + b]),
                                ("a U, b U", [a, b]),
                                ("a FULL, b FULL", [a, n + a, b, n + b])):
                um = ((1 << (2 * n)) - 1)
                for c in clean:
                    um &= ~(1 << c)
                for toy in range(n):
                    if toy in R:
                        continue
                    key = (n, decl)
                    res.setdefault(key, [0, 0, None])
                    res[key][0] += 1
                    for t in range(1, per):
                        P = pw[t]
                        F = [P[a], P[b], P[n + a], P[n + b]]
                        T = [P[toy], P[n + toy]]
                        if prior_exp(T, um) == 2 and support_exp(F, T, um) == 0:
                            res[key][1] += 1
                            if res[key][2] is None:
                                res[key][2] = (edges, R, toy, t)
                            break
for k in sorted(res):
    print(f"[5] n={k[0]} |R|=2 {k[1]:15s}: (labelled graph, R, toy) cases {res[k][0]}, learning {res[k][1]}, first {res[k][2]}")
print("L1 ATTACK:", "NO VIOLATION" if viol == 0 else f"{viol} VIOLATIONS")
