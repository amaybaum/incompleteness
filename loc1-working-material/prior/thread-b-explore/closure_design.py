"""EXPLORATORY DESIGN CHECK (not a result). For P2's configurations, the phi*-closure Z_k of region k's register
functionals c_i: is Z_1 + Z_2 direct and complete, and does Z_k equal the natural span of region k's coordinates?
Used only to decide whether C-cut and C-chain can serve as countercontrols in RULES-draft.md. Exact over F_3."""
Q = 3


def rule_matrix(L, nbrs, q=Q):
    n = 2 * L                                    # order (p_0..p_{L-1}, c_0..c_{L-1})
    M = [[0] * n for _ in range(n)]
    for i in range(L):
        M[i][L + i] = 1
        M[L + i][i] = (-1) % q
        for j, m in nbrs[i]:
            M[L + i][L + j] = (M[L + i][L + j] + m) % q
    return M


def rref_basis(vecs, q=Q):
    rows, basis = [list(v) for v in vecs], []
    piv = []
    for v in rows:
        v = v[:]
        for b, pc in zip(basis, piv):
            if v[pc]:
                f = v[pc]
                v = [(x - f * y) % q for x, y in zip(v, b)]
        k = next((i for i, x in enumerate(v) if x), None)
        if k is None:
            continue
        inv = pow(v[k], q - 2, q)
        v = [(x * inv) % q for x in v]
        nb, npv = [], []
        for b, pc in zip(basis, piv):
            if b[k]:
                f = b[k]
                b = [(x - f * y) % q for x, y in zip(b, v)]
            nb.append(b)
            npv.append(pc)
        basis, piv = nb + [v], npv + [k]
    return basis


def rank(vecs):
    return len(rref_basis(vecs))


def closure(gens, M, q=Q):
    n = len(M)
    span = rref_basis(gens)
    frontier = list(gens)
    while frontier:
        new = []
        for f in frontier:
            g = [sum(f[k] * M[k][j] for k in range(n)) % q for j in range(n)]   # f o phi = f M
            if rank(span + [g]) > len(span):
                span = rref_basis(span + [g])
                new.append(g)
        frontier = new
    return span


def unit(n, k):
    return [1 if i == k else 0 for i in range(n)]


def analyse(name, L, nbrs, R1, R2):
    M = rule_matrix(L, nbrs)
    n = 2 * L
    Z1 = closure([unit(n, L + i) for i in R1], M)
    Z2 = closure([unit(n, L + i) for i in R2], M)
    d1, d2, ds = len(Z1), len(Z2), rank(Z1 + Z2)
    direct = ds == d1 + d2
    nat1 = [unit(n, i) for i in R1] + [unit(n, L + i) for i in R1]
    nat2 = [unit(n, i) for i in R2] + [unit(n, L + i) for i in R2]
    eq1 = rank(Z1) == rank(nat1) == rank(Z1 + nat1)
    eq2 = rank(Z2) == rank(nat2) == rank(Z2 + nat2)
    print(f"{name}: dim Z1={d1} Z2={d2} sum={ds}/{n} direct={direct} complete={ds == n} "
          f"Z1=natural1:{eq1} Z2=natural2:{eq2}")


iso = lambda: {0: []}
analyse("U-free(3)", 2, {0: [], 1: []}, [0], [1])
for a in (1, 2):
    for b in (1, 2):
        analyse(f"U-edge(3,{a},{b})", 4, {0: [(1, a)], 1: [(0, a)], 2: [(3, b)], 3: [(2, b)]}, [0, 1], [2, 3])
chain = lambda L: {i: [(j, 1) for j in (i - 1, i + 1) if 0 <= j < L] for i in range(L)}
analyse("C-cut", 4, chain(4), [0, 1], [2, 3])
analyse("C-chain {0}|{5}", 6, chain(6), [0], [5])
analyse("one 2-site edge a=1, regions {0}|{1} (coupled)", 2, {0: [(1, 1)], 1: [(0, 1)]}, [0], [1])
