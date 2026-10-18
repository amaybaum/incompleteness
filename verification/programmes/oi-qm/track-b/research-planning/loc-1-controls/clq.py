"""CL-Q, the exact classification of regional assignments of a linear rule when the closures leave a proper sum
(LOC-1 preregistration §3.2, §6 W-OBS, §7.S route 3), and its control SC-CLQ (§8).  Research development.

Notation of the preregistration.  Functionals on F_q^n are row vectors; the rule acts by f -> f M.  For region k
with register functionals R_k, Z_k = span{ f M^j : f in R_k, j >= 0 }, S = Z_1 + Z_2.  An invariant subspace of
Q = V*/S is an M-invariant subspace U of V* with S <= U, and Q_1 (+) Q_2 = Q is a pair (U_1, U_2) with
U_1 + U_2 = V* and U_1 & U_2 = S.

    decide(M, R1, R2, q)    the first route of §7.S that applies: 1 (Z_1 & Z_2 != 0: NONE), 2 (Z_1 (+) Z_2 = V*:
                            the unique assignment (Z_1, Z_2)), 3 (CL-Q), with the assignment set or UNRESOLVED
    clq(M, Z1, Z2, q)       route 3: invariant subspaces of Q by closure; complementary pairs; for each pair and
                            each k, the q^(dim Q_k dim Z_k') shifts of fixed representatives by Z_k'; the shifted spans
                            with Z_k that are M-invariant; A(M) the pairs of kept spans.  Stops at LIMIT subspaces or
                            choices and reports UNRESOLVED with the count.  Nothing is sampled.
    brute_splittings        every M-invariant splitting V* = Y_1 (+) Y_2 with Z_k <= Y_k, from all subspaces
    brute_decompositions    every linear decomposition (n independent functionals up to scalar) with a bipartition
                            W_1 | W_2 putting R_k in span W_k with span W_k invariant (the definition of §3.2)

All arithmetic is exact mod a prime q.  Standard library only.  This file evaluates no LOC-1 target configuration:
its self-test runs SC-CLQ's three synthetic rules on F_3^3 and seeded synthetic rules on F_2^4 and F_3^4.

Run:  python3 -I -B clq.py --self-test
"""
import itertools
import sys

LIMIT = 50000


# ------------------------------------------------------------------- linear algebra over F_q (row vectors)

def rref(vecs, q):
    """Reduced row echelon basis (a tuple of tuples) of the span of vecs: the canonical form of a subspace."""
    rows = [list(v) for v in vecs]
    n = len(rows[0]) if rows else 0
    out, col = [], 0
    for col in range(n):
        piv = next((r for r in rows if r[col] % q), None)
        if piv is None:
            continue
        rows.remove(piv)
        inv = pow(piv[col], -1, q)
        piv = [x * inv % q for x in piv]
        rows = [[(x - r[col] * y) % q for x, y in zip(r, piv)] for r in rows]
        out = [[(x - o[col] * y) % q for x, y in zip(o, piv)] for o in out]
        out.append(piv)
    out.sort(key=lambda r: next(i for i, x in enumerate(r) if x))
    return tuple(tuple(r) for r in out)


def dim(W):
    return len(W)


def span(vecs, q, n):
    vecs = [v for v in vecs if any(x % q for x in v)]
    return rref(vecs, q) if vecs else ()


def ssum(A, B, q, n):
    return span(list(A) + list(B), q, n)


def contains(W, v, q, n):
    return dim(ssum(W, [v], q, n)) == dim(W)


def act(f, M, q):
    n = len(M)
    return tuple(sum(f[i] * M[i][j] for i in range(n)) % q for j in range(n))


def invariant(W, M, q, n):
    return all(contains(W, act(f, M, q), q, n) for f in W)


def inv_closure(vecs, M, q, n):
    W = span(vecs, q, n)
    while True:
        W2 = ssum(W, [act(f, M, q) for f in W], q, n)
        if W2 == W:
            return W
        W = W2


def inter_dim(A, B, q, n):
    return dim(A) + dim(B) - dim(ssum(A, B, q, n))


def all_vectors(q, n):
    return list(itertools.product(range(q), repeat=n))


# ------------------------------------------------------------------- routes and CL-Q

def closures(M, R1, R2, q):
    n = len(M)
    return inv_closure(R1, M, q, n), inv_closure(R2, M, q, n)


def clq(M, Z1, Z2, q, limit=LIMIT, shift=True):
    """Route 3.  Returns ('ok', set of (Y1, Y2)) or ('unresolved', reason).  shift=False is a negative control
    (representatives are never shifted by the other region's closure)."""
    n = len(M)
    S = ssum(Z1, Z2, q, n)
    full = span([tuple(int(i == j) for j in range(n)) for i in range(n)], q, n)
    vecs = all_vectors(q, n)
    # invariant subspaces U, S <= U <= V*, by closure from S
    found, frontier = {S}, [S]
    while frontier:
        nxt = []
        for U in frontier:
            for v in vecs:
                if contains(U, v, q, n):
                    continue
                U2 = inv_closure(list(U) + [v], M, q, n)
                if U2 not in found:
                    found.add(U2)
                    nxt.append(U2)
                    if len(found) > limit:
                        return "unresolved", "more than %d invariant subspaces of Q" % limit
        frontier = nxt
    pairs = [(U1, U2) for U1 in found for U2 in found
             if ssum(U1, U2, q, n) == full and dim(U1) + dim(U2) - dim(S) == n]
    A, choices = set(), 0
    Z = (Z1, Z2)
    for U1, U2 in pairs:
        kept = []
        for k, U in enumerate((U1, U2)):
            Zk, Zo = Z[k], Z[1 - k]
            reps, W = [], Zk
            base = ssum(S, (), q, n)
            for v in U:                                   # representatives of a basis of Q_k = U / S
                if not contains(base, v, q, n):
                    reps.append(v)
                    base = ssum(base, [v], q, n)
            zo = [()] if not Zo else list(itertools.product(range(q), repeat=dim(Zo)))
            elems = [tuple(sum(c * z[j] for c, z in zip(cs, Zo)) % q for j in range(n)) for cs in zo] \
                if Zo else [tuple([0] * n)]
            if not shift:
                elems = [tuple([0] * n)]
            ks = []
            for combo in itertools.product(elems, repeat=len(reps)):
                choices += 1
                if choices > limit:
                    return "unresolved", "more than %d choices" % limit
                Y = ssum(Zk, [tuple((a + b) % q for a, b in zip(r, s)) for r, s in zip(reps, combo)], q, n)
                if invariant(Y, M, q, n):
                    ks.append(Y)
            kept.append(set(ks))
        for Y1 in kept[0]:
            for Y2 in kept[1]:
                A.add((Y1, Y2))
    return "ok", A


def decide(M, R1, R2, q, limit=LIMIT):
    n = len(M)
    Z1, Z2 = closures(M, R1, R2, q)
    S = ssum(Z1, Z2, q, n)
    info = {"dimZ1": dim(Z1), "dimZ2": dim(Z2), "dimSum": dim(S), "dimMeet": inter_dim(Z1, Z2, q, n)}
    if info["dimMeet"]:
        return 1, "S-I2-NONE", set(), info
    if dim(S) == n:
        return 2, "S-I2-UNIQUE", {(Z1, Z2)}, info
    st, A = clq(M, Z1, Z2, q, limit)
    if st != "ok":
        return 3, "S-I2-UNRESOLVED", A, info
    tok = "S-I2-NONE" if not A else "S-I2-UNIQUE" if len(A) == 1 else "S-I2-NONUNIQUE"
    return 3, tok, A, info


# ------------------------------------------------------------------- brute force (small spaces only)

def all_subspaces(q, n):
    subs = {()}
    frontier = [()]
    vecs = all_vectors(q, n)
    while frontier:
        nxt = []
        for W in frontier:
            for v in vecs:
                W2 = ssum(W, [v], q, n)
                if W2 not in subs:
                    subs.add(W2)
                    nxt.append(W2)
        frontier = nxt
    return subs


def brute_splittings(M, Z1, Z2, q):
    n = len(M)
    full = span([tuple(int(i == j) for j in range(n)) for i in range(n)], q, n)
    subs = [W for W in all_subspaces(q, n) if invariant(W, M, q, n)]
    out = set()
    for Y1 in subs:
        if ssum(Y1, Z1, q, n) != Y1:
            continue
        for Y2 in subs:
            if ssum(Y2, Z2, q, n) == Y2 and dim(Y1) + dim(Y2) == n and ssum(Y1, Y2, q, n) == full:
                out.add((Y1, Y2))
    return out


def projective_points(q, n):
    pts = []
    for v in all_vectors(q, n):
        if any(v):
            lead = next(x for x in v if x)
            if lead == 1:
                pts.append(v)
    return pts


def normalize(v, q):
    lead = next(x for x in v if x % q)
    inv = pow(lead, -1, q)
    return tuple(x * inv % q for x in v)


def brute_decompositions(M, R1, R2, q):
    """The definition of §3.2: decompositions containing every register (I1), with a bipartition putting each
    region's registers in span W_k and making each span W_k invariant (I2); returns (|I2|, set of assignments)."""
    n = len(M)
    regs = {normalize(r, q) for r in list(R1) + list(R2)}
    pts = [p for p in projective_points(q, n) if p not in regs]
    count, A = 0, set()
    for extra in itertools.combinations(pts, n - len(regs)):
        F = sorted(regs) + list(extra)
        if dim(span(F, q, n)) != n:
            continue
        for mask in range(1 << n):
            W1 = [F[i] for i in range(n) if mask >> i & 1]
            W2 = [F[i] for i in range(n) if not mask >> i & 1]
            s1, s2 = span(W1, q, n), span(W2, q, n)
            if all(contains(s1, r, q, n) for r in R1) and all(contains(s2, r, q, n) for r in R2) and \
                    invariant(s1, M, q, n) and invariant(s2, M, q, n):
                count += 1
                A.add((s1, s2))
    return count, A


# ------------------------------------------------------------------- SC-CLQ and further synthetic controls

def rule_from_images(images, n):
    """M with e_i M = images[i] (row i of M)."""
    return [list(images[i]) for i in range(n)]


SC_CLQ = [  # F_3^3, e1 register of region 1, e2 of region 2, e1 M = 0
    ("(i)   e0 M = e1 + e2, e2 M = 0", [(0, 1, 1), (0, 0, 0), (0, 0, 0)], 0),
    ("(ii)  e0 M = e1,      e2 M = e2", [(0, 1, 0), (0, 0, 0), (0, 0, 1)], 1),
    ("(iii) e0 M = e1,      e2 M = 0", [(0, 1, 0), (0, 0, 0), (0, 0, 0)], 3),
]


def lcg(seed):
    s = seed
    while True:
        s = (s * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        yield s >> 33


def self_test():
    lines, ok = [], True

    def rep(name, passed, detail=""):
        nonlocal ok
        ok &= bool(passed)
        lines.append("%s %-72s %s" % ("PASS" if passed else "FAIL", name, detail))

    q, n = 3, 3
    e = [tuple(int(i == j) for j in range(n)) for i in range(n)]
    sizes, infos = [], []
    for name, imgs, expect in SC_CLQ:
        M = rule_from_images(imgs, n)
        R1, R2 = [e[1]], [e[2]]
        route, tok, A, info = decide(M, R1, R2, q)
        Z1, Z2 = closures(M, R1, R2, q)
        S = ssum(Z1, Z2, q, n)
        bs = brute_splittings(M, Z1, Z2, q)
        cnt, bd = brute_decompositions(M, R1, R2, q)
        meet_ok = all(inter_dim(Y, S, q, n) == dim(Z) and ssum(Z, Y, q, n) == Y
                      for Y1, Y2 in A for Y, Z in ((Y1, Z1), (Y2, Z2)))
        sizes.append(len(A))
        infos.append(tuple(sorted(info.items())))
        rep("SC-CLQ %s: route 3, |A(M)| = %d" % (name, expect),
            route == 3 and len(A) == expect and info["dimMeet"] == 0 and info["dimSum"] == 2,
            "%s, |A| = %d, dim Z1 = %d, dim Z2 = %d, dim S = %d" % (tok, len(A), info["dimZ1"], info["dimZ2"],
                                                                     info["dimSum"]))
        rep("SC-CLQ %s: CL-Q = invariant splittings (W-OBS (a), brute force)" % name[:5], A == bs, "%d" % len(bs))
        rep("SC-CLQ %s: CL-Q = assignments from decompositions (§3.2 definition)" % name[:5], A == bd,
            "%d assignments from %d (decomposition, bipartition) pairs" % (len(bd), cnt))
        rep("SC-CLQ %s: every assignment has Y_k & S = Z_k" % name[:5], meet_ok)
    rep("SC-CLQ: closure alone does not decide a proper sum (same closure data, sizes 0, 1, 3)",
        len(set(infos)) == 1 and sizes == [0, 1, 3], "closure data %s" % (dict(infos[0]),))
    # negative controls
    M = rule_from_images(SC_CLQ[2][1], n)
    Z1, Z2 = closures(M, [e[1]], [e[2]], q)
    _, A_noshift = clq(M, Z1, Z2, q, shift=False)
    rep("NEG CL-Q without the shifts by Z_k' loses assignments on (iii)", len(A_noshift) != 3,
        "%d instead of 3" % len(A_noshift))
    st, why = clq(M, Z1, Z2, q, limit=2)
    rep("NEG CL-Q under a limit of 2 stops UNRESOLVED (never sampled, never read as empty)",
        st == "unresolved", why)
    # seeded synthetic rules on F_2^4 and F_3^4 with proper sums: CL-Q against both brute forces
    agree = total = proper = 0
    for q2, seed, trials in ((2, 0x5C1, 40), (3, 0x5C2, 25)):
        g = lcg(seed)
        n2 = 4
        e2 = [tuple(int(i == j) for j in range(n2)) for i in range(n2)]
        for _ in range(trials):
            M2 = [[next(g) % q2 if next(g) % 3 == 0 else 0 for _ in range(n2)] for _ in range(n2)]
            R1, R2 = [e2[0]], [e2[1]]
            route, tok, A, info = decide(M2, R1, R2, q2)
            if route != 3:
                continue
            proper += 1
            Z1, Z2 = closures(M2, R1, R2, q2)
            bs = brute_splittings(M2, Z1, Z2, q2)
            _, bd = brute_decompositions(M2, R1, R2, q2)
            total += 1
            agree += A == bs == bd
    rep("CL-Q = brute force on seeded synthetic rules with a proper sum (F_2^4, F_3^4)", total > 0 and agree == total,
        "%d/%d agree" % (agree, total))
    lines.append("clq self-test: %s" % ("ALL PASS" if ok else "FAILURE"))
    return ok, lines


def main(argv):
    if argv[:1] == ["--self-test"]:
        ok, lines = self_test()
        print("\n".join(lines))
        return 0 if ok else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
