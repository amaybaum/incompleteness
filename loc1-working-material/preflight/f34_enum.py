"""LOC-1 preflight, leg S, F_3^4: every linear decomposition and its coupling graph, SYNTHETIC rules only.

Design evidence for the budget decision; not a measurement of any frozen rule. Standard library only;
all arithmetic is integer arithmetic mod 3. Timing and memory go to stderr, so stdout is deterministic.

Run:  python3 -I f34_enum.py            (main run: controls, synthetic rules, mutation harness)
      python3 -I f34_enum.py --kdep-all  (K-dep over every decomposition instead of a seeded sample)

Definitions used (stated so the round can reuse them):
  * A linear decomposition of F_q^n is an unordered set of n linearly independent linear functionals,
    each taken up to a nonzero scalar; equivalently an independent n-subset of the projective points of
    PG(n-1, q).  It is represented by an invertible matrix B whose rows f_1..f_n are the functionals.
  * A linear rule M acts on states (column vectors) by x -> M x; a functional f is pulled back by
    f -> f M (the functional read after one step).  In the decomposition B, write
        f_i M = sum_j G[i][j] f_j,   i.e.  G = B M B^{-1}.
    G[i][j] != 0 means: coordinate i after one step depends on coordinate j before it.
  * The coupling graph of M in the decomposition has the n functionals as vertices and an undirected
    edge {i, j}, i != j, iff G[i][j] != 0 or G[j][i] != 0.  deg_max is its maximum vertex degree,
    e its edge count; self counts i with G[i][i] != 0 (not edges).
  * Rescaling f_i -> l_i f_i replaces G by L G L^{-1} (same zero pattern); reordering the f_i conjugates G
    by a permutation matrix (same graph, relabelled).  So the graph up to isomorphism, deg_max and e are
    functions of the decomposition.  For S invertible, G_{B S}(S^{-1} M S) = G_B(M): the multiset of
    graphs over all decompositions is a conjugacy invariant of M.
Synthetic rules (none is a frozen rule; all have det 2 = -1 mod 3 except the identity, whereas every
second-order rule (p, c) -> (c, F c - p) has det 1, so no synthetic rule other than the identity is
conjugate to such a rule, and the identity is not of that form):
  R-id     the identity;
  R-rand   a fixed-seed random invertible matrix with det 2;
  R-block  S^{-1} (M1 (+) M2) S: two fixed-seed random invertible 2x2 blocks, det(M1) det(M2) = 2, in a
           fixed-seed random basis S; in the planted decomposition rows(S), G = M1 (+) M2.
"""
import sys
import time
import itertools
import resource

Q, N = 3, 4
MASK = (1 << 64) - 1


class SM64:
    """SplitMix64, integer only, so the seeded draws do not depend on the Python version."""

    def __init__(self, seed):
        self.s = seed & MASK

    def next(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & MASK
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK
        return z ^ (z >> 31)

    def below(self, k):
        lim = (1 << 64) - ((1 << 64) % k)
        while True:
            x = self.next()
            if x < lim:
                return x % k


OUT = []
FAIL = []


def say(*a):
    OUT.append(" ".join(str(x) for x in a))


def check(name, ok, detail=""):
    say("CONTROL", name, "PASS" if ok else "FAIL", detail)
    if not ok:
        FAIL.append(name)
    return ok


def tlog(*a):
    print("TIMING", *a, file=sys.stderr)


# ---------------------------------------------------------------- arithmetic mod 3

def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) % Q for j in range(p)] for i in range(n)]


def inverse(B):
    """Gauss-Jordan mod Q; None if singular."""
    n = len(B)
    A = [list(B[i]) + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] % Q), None)
        if piv is None:
            return None
        A[c], A[piv] = A[piv], A[c]
        iv = pow(A[c][c], Q - 2, Q)
        A[c] = [(x * iv) % Q for x in A[c]]
        for r in range(n):
            if r != c and A[r][c]:
                f = A[r][c]
                A[r] = [(x - f * y) % Q for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def det(B):
    """Leibniz expansion mod Q (used only to fix the synthetic rules' determinants)."""
    n = len(B)
    s = 0
    for perm in itertools.permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        t = 1
        for i in range(n):
            t *= B[i][perm[i]]
        s += -t if inv % 2 else t
    return s % Q


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def rand_invertible(rng, n, want_det):
    while True:
        M = [[rng.below(Q) for _ in range(n)] for _ in range(n)]
        if det(M) == want_det:
            return M


def block(M1, M2):
    M = [[0] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            M[i][j], M[i + 2][j + 2] = M1[i][j], M2[i][j]
    return M


# ---------------------------------------------------------------- decompositions

def projective_points(mut=None):
    pts = []
    for v in itertools.product(range(Q), repeat=N):
        nz = [x for x in v if x]
        if nz and nz[0] == 1:
            pts.append(v)
    if mut == "duppoint":          # normalization bug: one point also listed as its other scalar multiple
        pts.append(tuple((2 * x) % Q for x in pts[-1]))
    if mut == "droppoint":
        pts = pts[:-1]
    return pts


def enumerate_decomps(mut=None):
    pts = projective_points(mut)
    out = []
    for combo in itertools.combinations(pts, N):
        B = [list(v) for v in combo]
        if mut == "noindep":
            out.append((B, None))
            continue
        Bi = inverse(B)
        if Bi is not None:
            out.append((B, Bi))
    return pts, out


def coupling(G, mut=None):
    n = len(G)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if mut == "and":
                if G[i][j] and G[j][i]:
                    edges.append((i, j))
            elif G[i][j] or G[j][i]:
                edges.append((i, j))
    deg = [0] * n
    for i, j in edges:
        deg[i] += 1
        deg[j] += 1
    return max(deg), len(edges), sum(1 for i in range(n) if G[i][i]), tuple(edges)


def gmat(B, Bi, M, mut=None):
    if mut == "conj":              # wrong convention: B^{-1} M B
        return matmul(matmul(Bi, M), B)
    return matmul(matmul(B, M), Bi)


def brute_dependency(B, M):
    """Independent route to the coupling graph: tabulate y = B x -> y' = B M x over all 81 states and test,
    for each pair (i, j), whether changing coordinate j alone changes coordinate i after one step.
    Uses no inverse and no G."""
    table = {}
    for x in itertools.product(range(Q), repeat=N):
        y = tuple(sum(B[r][k] * x[k] for k in range(N)) % Q for r in range(N))
        Mx = [sum(M[r][k] * x[k] for k in range(N)) % Q for r in range(N)]
        y2 = tuple(sum(B[r][k] * Mx[k] for k in range(N)) % Q for r in range(N))
        table[y] = y2
    dep = set()
    for y, y2 in table.items():
        for j in range(N):
            for t in range(1, Q):
                ya = list(y)
                ya[j] = (ya[j] + t) % Q
                y2a = table[tuple(ya)]
                for i in range(N):
                    if y2[i] != y2a[i]:
                        dep.add((i, j))
    return tuple(sorted({(min(i, j), max(i, j)) for i, j in dep if i != j}))


# ---------------------------------------------------------------- one full run

def gl_order(n, q):
    r = 1
    for i in range(n):
        r *= q ** n - q ** i
    return r


KDEP_ALL = False


def run(mut=None, verbose=True):
    """Return the set of failed control names for this (possibly mutated) run."""
    global OUT, FAIL
    OUT, FAIL = [], []
    t0 = time.perf_counter()
    pts, decs = enumerate_decomps(mut)
    t1 = time.perf_counter()
    expect = gl_order(N, Q) // (24 * 2 ** N)
    say("points of PG(3,3):", len(pts))
    say("decompositions enumerated:", len(decs), " formula |GL(4,3)|/(4! 2^4) =", expect,
        " (|GL(4,3)| =", gl_order(N, Q), ")")
    check("K-count", len(decs) == expect == 63180, "%d vs %d" % (len(decs), expect))
    if mut in ("noindep", "duppoint", "droppoint"):
        return set(FAIL), t1 - t0
    keys = {frozenset(tuple(r) for r in B) for B, _ in decs}
    check("K-distinct", len(keys) == len(decs), "%d distinct sets" % len(keys))
    check("K-inverse", all(matmul(B, Bi) == eye(N) for B, Bi in decs))

    rng = SM64(0x4C4F43312D463334)          # "LOC1-F34"
    R_id = eye(N)
    R_rand = rand_invertible(rng, N, 2)
    M1 = rand_invertible(rng, 2, 1)
    M2 = rand_invertible(rng, 2, 2)
    S = rand_invertible(rng, N, rng.below(2) + 1)
    Si = inverse(S)
    R_block = matmul(matmul(Si, block(M1, M2)), S)
    rules = [("R-id", R_id), ("R-rand", R_rand), ("R-block", R_block)]
    check("K-rules", det(R_rand) == 2 and det(R_block) == 2 and det(block(M1, M2)) == 2,
          "R-rand=%s R-block=%s M1=%s M2=%s S=%s" % (R_rand, R_block, M1, M2, S))

    # normalise rows(S) to projective representatives (first nonzero = 1) to locate the planted decomposition
    def normrow(v):
        f = next(x for x in v if x)
        iv = pow(f, Q - 2, Q)
        return tuple((x * iv) % Q for x in v)
    planted_key = frozenset(normrow(r) for r in S)
    natural_key = frozenset(tuple(r) for r in eye(N))
    check("K-special-present", planted_key in keys and natural_key in keys)

    t2 = time.perf_counter()
    results = {}
    for name, M in rules:
        hist, hist2 = {}, {}
        minima = None
        rec = []
        for B, Bi in decs:
            G = gmat(B, Bi, M, mut)
            dm, e, s, E = coupling(G, mut)
            rec.append((dm, e, s, E))
            hist[dm] = hist.get(dm, 0) + 1
            hist2[(dm, e)] = hist2.get((dm, e), 0) + 1
        results[name] = rec
        say("rule", name, "deg_max histogram:", sorted(hist.items()))
        say("rule", name, "(deg_max, e) histogram:", sorted(hist2.items()))
        dmin = min(hist)
        emin = min(e for dm, e in hist2 if dm == dmin)
        say("rule", name, "min deg_max =", dmin, " minimizers:", hist[dmin],
            " lexicographic (deg_max, e) minimizers:", hist2[(dmin, emin)], "at e =", emin)
        for lab, key in (("natural", natural_key), ("planted rows(S)", planted_key)):
            idx = next(k for k, (B, _) in enumerate(decs) if frozenset(tuple(r) for r in B) == key)
            say("rule", name, lab, "decomposition: deg_max=%d e=%d self=%d edges=%s" % results[name][idx])
    t3 = time.perf_counter()

    # K-planted: in rows(S) the block rule's graph has no edge across {0,1} | {2,3} (rows taken in S's order)
    Gp = matmul(matmul(S, R_block), Si)
    cross = [(i, j) for i in range(4) for j in range(4) if (i < 2) != (j < 2) and Gp[i][j]]
    check("K-planted", Gp == block(M1, M2) and not cross)
    check("K-identity", all(r[0] == 0 and r[1] == 0 for r in results["R-id"]))

    # K-invariance: rescaling and reordering rows leaves deg_max, e and the graph (relabelled) unchanged
    rng2 = SM64(0x4C4F43312D494E56)
    bad = 0
    sample = [rng2.below(len(decs)) for _ in range(500)]
    for k in sample:
        B, _ = decs[k]
        perm = list(range(N))
        for i in range(N - 1, 0, -1):
            j = rng2.below(i + 1)
            perm[i], perm[j] = perm[j], perm[i]
        sc = [rng2.below(Q - 1) + 1 for _ in range(N)]
        B2 = [[(sc[i] * x) % Q for x in B[perm[i]]] for i in range(N)]
        B2i = inverse(B2)
        for name, M in rules:
            dm, e, s, E = results[name][k]
            dm2, e2, s2, E2 = coupling(gmat(B2, B2i, M, mut), mut)
            Emap = tuple(sorted((min(perm[i], perm[j]), max(perm[i], perm[j])) for i, j in E2))
            if (dm, e, s, E) != (dm2, e2, s2, Emap):
                bad += 1
    check("K-invariance", bad == 0, "500 seeded decompositions x 3 rules, %d mismatches" % bad)

    # K-dep: brute-force dependency over all 81 states equals the coupling graph from G
    t4 = time.perf_counter()
    rng3 = SM64(0x4C4F43312D444550)
    dsample = sorted({rng3.below(len(decs)) for _ in range(2000)})
    special = [k for k, (B, _) in enumerate(decs) if frozenset(tuple(r) for r in B) in (natural_key, planted_key)]
    dsample = sorted(set(dsample) | set(special))
    if KDEP_ALL and mut is None:
        dsample = list(range(len(decs)))
    bad = 0
    for name, M in rules:
        for k in dsample:
            if brute_dependency(decs[k][0], M) != results[name][k][3]:
                bad += 1
    t5 = time.perf_counter()
    check("K-dep", bad == 0, "%d %s decompositions x 3 rules, %d mismatches"
          % (len(dsample), "(all)" if len(dsample) == len(decs) else "seeded", bad))
    if verbose:
        tlog("enumeration_s %.3f" % (t1 - t0))
        tlog("coupling_graphs_3_rules_s %.3f  per_decomposition_per_rule_us %.2f"
             % (t3 - t2, 1e6 * (t3 - t2) / (3 * len(decs))))
        tlog("brute_dependency_s %.3f for %d checks" % (t5 - t4, 3 * len(dsample)))
    return set(FAIL), t3 - t0


def main():
    global KDEP_ALL
    KDEP_ALL = "--kdep-all" in sys.argv[1:]
    T0 = time.perf_counter()
    failed, _ = run(None)
    main_out = OUT[:]
    T1 = time.perf_counter()
    # mutation harness: every mutation must make its named control fail
    muts = [("noindep", "K-count"), ("duppoint", "K-count"), ("droppoint", "K-count"),
            ("conj", "K-dep"), ("and", "K-dep")]
    mut_lines = []
    mut_ok = True
    for mname, ctl in muts:
        f, _ = run(mname, verbose=False)
        hit = ctl in f
        mut_ok &= hit
        mut_lines.append("MUTATION %-10s expected failure of %-8s : %s (failed controls: %s)"
                         % (mname, ctl, "DETECTED" if hit else "NOT DETECTED", ",".join(sorted(f)) or "none"))
    T2 = time.perf_counter()
    for line in main_out:
        print(line)
    for line in mut_lines:
        print(line)
    green = not failed and mut_ok
    print("F34 PREFLIGHT:", "CONTROLS GREEN" if green else "VOID (failed: %s)" % sorted(failed))
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    tlog("main_run_s %.3f  mutation_harness_s %.3f  peak_rss_kB %d" % (T1 - T0, T2 - T1, ru))


if __name__ == "__main__":
    main()
