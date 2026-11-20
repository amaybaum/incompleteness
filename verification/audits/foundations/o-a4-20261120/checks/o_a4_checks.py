#!/usr/bin/env python3
"""O-A4 exact checks (stdlib only, deterministic). Exit status 0 iff every check passes.

Second-order rule, phase form: state (p, c) = (x(t-1), x(t)),
    phi(p, c) = (c, F(c) - p),   Theta(p, c) = (c, p),   phi^{-1} = Theta phi Theta.

Parts
  A  SM Theorem 19 on Z^d under the uniform Bernoulli law, computed exactly on the hidden light
     cone (d = 1, 2, 3; linear and nonlinear F); finite-torus counting comparison (ring, d = 1);
     countercontrol: a non-invariant Bernoulli(1/3) hidden law breaks reciprocity.
  B  Cylinder check that the uniform product law is preserved by phi and by Theta (d = 1, nonlinear F).
  C  Lemma 1c(ii) pole transfer: visible autocorrelation of the wave rule (q = 2, alpha = 1) on rings
     has a nonzero periodic tail (a pole at lambda = 1 with residue 1/ord-type weight); on Z it is
     zero for every n >= 1 (cone-edge coefficient), so the reduced resolvent is 1/lambda.
  D  Graph symmetry of finite cubic quotients Z^3/Lambda versus Z^3: vertex-stabilizer orders and
     the rank of the action on the six links; C_4^3 is the 6-cube Q_6; a skew quotient.
  E  Checkerboard (bipartite) and Brillouin-corner characters on finite quotients.
  F  SM section 4.1 linearity countermodel: ring L = 4, q = 5 has no fixed point; on Z the same rule
     has a site-dependent fixed point and is conjugate to the linear rule by a site-wise shift, but
     has no translation-invariant fixed point.
Run:  python3 -I verification/audits/foundations/o-a4-20261120/checks/o_a4_checks.py
"""
from fractions import Fraction
from itertools import product, permutations
import sys

FAIL = []


def check(label, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {label}{(': ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(label)


# ---------------------------------------------------------------- lattice helpers
def ball(d, r):
    """l1 ball of radius r in Z^d, as a sorted list of tuples (r < 0 gives the empty set)."""
    if r < 0:
        return []
    out = [v for v in product(range(-r, r + 1), repeat=d) if sum(abs(a) for a in v) <= r]
    return sorted(out)


def unit_vectors(d):
    es = []
    for j in range(d):
        e = [0] * d
        e[j] = 1
        es.append(tuple(e))
        e = [0] * d
        e[j] = -1
        es.append(tuple(e))
    return es


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


# ---------------------------------------------------------------- local rules
def F_linear(alpha):
    def F(c, i, d, q):
        return (alpha * sum(c[add(i, e)] for e in unit_vectors(d))) % q
    return F


def F_nonlinear(c, i, d, q):
    # an arbitrary non-additive range-1 rule (d = 1 only): c_{i-1} * c_{i+1} + c_{i+1}
    return (c[add(i, (-1,))] * c[add(i, (1,))] + c[add(i, (1,))]) % q


def visible_after(n, d, q, F, p0, c0):
    """Exact phase pair at the origin after n steps on Z^d.

    p0 = x(-1) on B_{n-1}, c0 = x(0) on B_n (dicts). Only the light cone is evolved."""
    zero = tuple([0] * d)
    prev, cur = dict(p0), dict(c0)
    for t in range(n):
        r = n - t - 1  # radius on which x(t+1) is needed
        nxt = {i: (F(cur, i, d, q) - prev[i]) % q for i in ball(d, r)}
        prev, cur = {i: cur[i] for i in ball(d, r)}, nxt
    return (prev[zero], cur[zero])


def cone_transition_weights(n, d, q, F, hidden_weight=None):
    """Weights W[(i, j)] of {visible i at time 0 -> visible j at time n} on Z^d.

    Visible = phase pair at the origin. Hidden cells = x(0) on B_n minus origin, x(-1) on B_{n-1}
    minus origin. hidden_weight(value) gives a per-cell product law; None means uniform. Returns
    conditional probabilities T[(i, j)] as Fractions (the visible root is conditioned on)."""
    zero = tuple([0] * d)
    cells_c = [v for v in ball(d, n) if v != zero]
    cells_p = [v for v in ball(d, n - 1) if v != zero]
    m = len(cells_c) + len(cells_p)
    T = {}
    for i in product(range(q), repeat=2):
        acc = {}
        for h in product(range(q), repeat=m):
            w = Fraction(1, q ** m) if hidden_weight is None else _prod_w(h, hidden_weight)
            c0 = dict(zip(cells_c, h[:len(cells_c)]))
            p0 = dict(zip(cells_p, h[len(cells_c):]))
            p0[zero], c0[zero] = i
            j = visible_after(n, d, q, F, p0, c0)
            acc[j] = acc.get(j, 0) + w
        for j in product(range(q), repeat=2):
            T[(i, j)] = acc.get(j, Fraction(0))
    return T


def _prod_w(h, wf):
    w = Fraction(1)
    for a in h:
        w *= wf(a)
    return w


def theta(v):
    return (v[1], v[0])


def reciprocity_holds(T, q):
    bad = [(i, j) for i in product(range(q), repeat=2) for j in product(range(q), repeat=2)
           if T[(i, j)] != T[(theta(j), theta(i))]]
    return bad


def ring_transition(n, L, q, F):
    """Counting-measure transition probabilities of the origin phase pair on the ring Z/L (d = 1)."""
    T = {}
    for i in product(range(q), repeat=2):
        acc = {}
        m = 2 * L - 2
        for h in product(range(q), repeat=m):
            p = [0] * L
            c = [0] * L
            p[0], c[0] = i
            p[1:] = h[:L - 1]
            c[1:] = h[L - 1:]
            for _ in range(n):
                cd = {(k,): c[k % L] for k in range(-1, L + 1)}
                nxt = [(F(cd, (k,), 1, q) - p[k]) % q for k in range(L)]
                p, c = c, nxt
            j = (p[0], c[0])
            acc[j] = acc.get(j, 0) + 1
        for j in product(range(q), repeat=2):
            T[(i, j)] = Fraction(acc.get(j, 0), q ** m)
    return T


def part_A():
    print("== A. SM Theorem 19 on Z^d under the uniform Bernoulli law (exact, light cone) ==")
    cases = [(1, 2, "linear a=1", F_linear(1), [1, 2, 3, 4]),
             (1, 3, "linear a=1", F_linear(1), [1, 2, 3]),
             (1, 3, "linear a=2", F_linear(2), [1, 2, 3]),
             (1, 2, "nonlinear", F_nonlinear, [1, 2, 3, 4]),
             (1, 3, "nonlinear", F_nonlinear, [1, 2, 3]),
             (2, 2, "linear a=1", F_linear(1), [1, 2]),
             (3, 2, "linear a=1", F_linear(1), [1])]
    for d, q, name, F, ns in cases:
        for n in ns:
            T = cone_transition_weights(n, d, q, F)
            bad = reciprocity_holds(T, q)
            rows_ok = all(sum(T[(i, j)] for j in product(range(q), repeat=2)) == 1
                          for i in product(range(q), repeat=2))
            # non-vacuity: theta matters (some T_ij != T_ji) and the law is not constant
            sym_fail = sum(1 for i in product(range(q), repeat=2) for j in product(range(q), repeat=2)
                           if T[(i, j)] != T[(j, i)])
            distinct = len(set(T.values()))
            check(f"d={d} q={q} {name} n={n}: T_ij(n) = T_(theta j, theta i)(n)",
                  not bad and rows_ok,
                  f"rows stochastic {rows_ok}; pairs with T_ij != T_ji: {sym_fail}; distinct values {distinct}")
    print("-- ring comparison (d = 1, counting measure on Z/L) --")
    diffs = []
    for q, name, F, n in [(2, "linear a=1", F_linear(1), 2), (2, "nonlinear", F_nonlinear, 2),
                          (2, "linear a=1", F_linear(1), 3), (3, "linear a=1", F_linear(1), 2)]:
        Tz = cone_transition_weights(n, 1, q, F)
        for L in sorted({2 * n + 1, n + 1, 3}):
            if L < 3:
                continue
            TL = ring_transition(n, L, q, F)
            same = TL == Tz
            bad = reciprocity_holds(TL, q)
            if L >= 2 * n + 1:
                check(f"q={q} {name} n={n} ring L={L} (>= 2n+1): reciprocity on the ring; equals the Z value",
                      (not bad) and same)
            else:
                check(f"q={q} {name} n={n} ring L={L} (< 2n+1): reciprocity on the ring",
                      not bad, f"equals the Z value: {same} (not required)")
            diffs.append(not same)
    check("some small ring differs from the Z value (finite-volume values are not the Z values)", any(diffs))
    print("-- countercontrol: hidden Bernoulli(1/3) law (q = 2), not phi-invariant --")
    wf = lambda a: Fraction(2, 3) if a == 0 else Fraction(1, 3)
    for name, F in [("linear a=1", F_linear(1)), ("nonlinear", F_nonlinear)]:
        viol = []
        for n in [1, 2, 3]:
            T = cone_transition_weights(n, 1, 2, F, hidden_weight=wf)
            viol.append(len(reciprocity_holds(T, 2)))
        check(f"Bernoulli(1/3) hidden law, d=1 q=2 {name}: reciprocity fails at some lag (detector live)",
              any(v > 0 for v in viol), f"violating ordered pairs at n=1,2,3: {viol}")


# ---------------------------------------------------------------- B
def part_B():
    print("== B. uniform product law preserved by phi and Theta on cylinders (d = 1) ==")
    for q, name, F in [(3, "nonlinear", F_nonlinear), (3, "linear a=2", F_linear(2)),
                       (2, "nonlinear", F_nonlinear)]:
        w = 3
        W = [(k,) for k in range(w)]
        Wplus = [(k,) for k in range(-1, w + 1)]
        counts = {}
        for pv in product(range(q), repeat=w):
            for cv in product(range(q), repeat=w + 2):
                c = dict(zip(Wplus, cv))
                out = tuple(c[i] for i in W) + tuple((F(c, i, 1, q) - pv[k]) % q for k, i in enumerate(W))
                counts[out] = counts.get(out, 0) + 1
        uniform = len(counts) == q ** (2 * w) and len(set(counts.values())) == 1
        check(f"q={q} {name}: image of uniform (p on W, c on W+-1) under phi is uniform on W x W",
              uniform, f"{len(counts)} outputs, fibre sizes {sorted(set(counts.values()))}")
    check("Theta (site-wise swap) permutes cylinder coordinates, so preserves every product law",
          True, "structural")


# ---------------------------------------------------------------- C
def part_C():
    print("== C. Lemma 1c(ii): visible poles on rings versus Z (wave rule, q = 2, alpha = 1) ==")
    # Linear forms over GF(2) on the initial data, as Python int bitmasks.
    for L in range(3, 13):
        # variables: p_k -> bit k, c_k -> bit L + k
        p = [1 << k for k in range(L)]
        c = [1 << (L + k) for k in range(L)]
        init = (tuple(p), tuple(c))
        x0 = c[0]
        hits, n, state = [], 0, init
        order = None
        while True:
            if n > 0 and state == init:
                order = n
                break
            if state[1][0] == x0:
                hits.append(n)
            pp, cc = state
            nxt = tuple(cc[(k - 1) % L] ^ cc[(k + 1) % L] ^ pp[k] for k in range(L))
            state = (cc, nxt)
            n += 1
            if n > 10 ** 6:
                break
        residue = Fraction(len(hits), order)
        check(f"ring L={L}: phi has finite order {order}; visible autocorrelation m_n = 1 at "
              f"{len(hits)} of {order} lags; pole at lambda=1 with residue {residue}",
              order is not None and residue > 0)
    # On Z: x_0(n) as a linear form contains x_{+n}(0) with coefficient alpha^n = 1, so
    # m_n = 0 for all n >= 1. Check the cone-edge coefficient exactly for n <= 40.
    ok = True
    N = 40
    cur = {k: {("c", k)} for k in range(-N - 1, N + 2)}
    prev = {k: {("p", k)} for k in range(-N - 1, N + 2)}
    for n in range(1, N + 1):
        nxt = {}
        for k in range(-N + n - 1, N - n + 2):
            if k - 1 in cur and k + 1 in cur and k in prev:
                nxt[k] = cur[k - 1] ^ cur[k + 1] ^ prev[k]
        prev, cur = cur, nxt
        form = cur[0]
        if ("c", n) not in form or form == {("c", 0)}:
            ok = False
    check(f"Z: x_0(n) contains x_n(0) with coefficient 1 for 1 <= n <= {N}, so m_n = 0 and the "
          f"reduced resolvent on the visible mean-zero line is 1/lambda", ok)


# ---------------------------------------------------------------- D, E graph helpers
def hnf_reduce(v, B):
    """Reduce v in Z^3 modulo the lattice whose basis row k vanishes after column k (B[k][k] > 0)."""
    v = list(v)
    for k in reversed(range(3)):
        row = B[k]
        f = v[k] // row[k]
        v = [v[t] - f * row[t] for t in range(3)]
    return tuple(v)


def quotient_graph(B):
    """Cubic nearest-neighbour graph on Z^3 / Lambda, Lambda spanned by rows of B.

    B must be lower-triangular in the sense row k has zeros after column k (row k = (.., .., B[k][k]))
    so that coordinate k is reduced by row k, last coordinate first."""
    reps = [(a, b, c) for a in range(B[0][0]) for b in range(B[1][1]) for c in range(B[2][2])]
    idx = {r: t for t, r in enumerate(reps)}
    es = unit_vectors(3)
    adj = []
    simple = True
    for r in reps:
        nb = [idx[hnf_reduce(add(r, e), B)] for e in es]
        if len(set(nb)) != 6 or idx[r] in nb:
            simple = False
        adj.append(nb)
    return reps, adj, simple


def bfs_dist(adj, s):
    dist = {s: 0}
    order = [s]
    for u in order:
        for w in adj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                order.append(w)
    return dist, order


def stabilizer_maps(adj, s=0, limit=10 ** 6):
    """All automorphisms fixing s of the graph adj (list of neighbour lists)."""
    nbset = [set(a) for a in adj]
    dist, order = bfs_dist(adj, s)
    n = len(adj)
    by_dist = {}
    for v, dv in dist.items():
        by_dist.setdefault(dv, []).append(v)
    out = []
    img = {s: s}
    used = {s}

    def rec(k):
        if len(out) >= limit:
            return
        if k == len(order):
            out.append(dict(img))
            return
        v = order[k]
        if v in img:
            rec(k + 1)
            return
        assigned_nb = [w for w in adj[v] if w in img]
        cands = by_dist[dist[v]]
        for x in cands:
            if x in used:
                continue
            if all(img[w] in nbset[x] for w in assigned_nb):
                # non-adjacency to assigned non-neighbours is checked at the end
                img[v] = x
                used.add(x)
                rec(k + 1)
                del img[v]
                used.discard(x)

    rec(0)
    good = []
    for m in out:
        if all(m[w] in nbset[m[v]] for v in range(n) for w in adj[v]):
            good.append(m)
    return good


def link_rank(adj, maps, s=0):
    links = adj[s]
    pairs = set()
    seen = set()
    orbits = 0
    for a in links:
        for b in links:
            if (a, b) in seen:
                continue
            orbits += 1
            for m in maps:
                seen.add((m[a], m[b]))
    return orbits


def ball_graph(R):
    vs = ball(3, R)
    idx = {v: t for t, v in enumerate(vs)}
    adj = [[idx[add(v, e)] for e in unit_vectors(3) if add(v, e) in idx] for v in vs]
    return vs, adj


def part_D():
    print("== D. vertex stabilizers: cubic quotients Z^3/Lambda versus Z^3 ==")
    vs, adj = ball_graph(3)
    s0 = vs.index((0, 0, 0))
    maps = stabilizer_maps(adj, s0)
    check("Z^3 control: automorphisms of the radius-3 ball fixing 0", len(maps) == 48,
          f"order {len(maps)}; rank on the 6 links {link_rank(adj, maps, s0)} (O_h: 3 = 1+1+1 -> A1g+Eg+T1u)")
    expected = {3: (48, 3), 4: (720, 2), 5: (48, 3), 6: (48, 3)}
    for L in [3, 4, 5, 6]:
        B = [[L, 0, 0], [0, L, 0], [0, 0, L]]
        reps, adj, simple = quotient_graph(B)
        maps = stabilizer_maps(adj, 0)
        rk = link_rank(adj, maps, 0)
        check(f"cubic torus L={L}: simple 6-regular {simple}; |Stab(0)| = {len(maps)}; rank on links {rk}",
              simple and (len(maps), rk) == expected[L],
              "rank 2 means the links decompose as 1+5 (2-transitive)" if rk == 2 else "")
    # C_4^3 is the 6-cube: Gray code 0->00, 1->01, 2->11, 3->10
    gray = {0: (0, 0), 1: (0, 1), 2: (1, 1), 3: (1, 0)}
    B = [[4, 0, 0], [0, 4, 0], [0, 0, 4]]
    reps, adj, _ = quotient_graph(B)
    f = {t: gray[r[0]] + gray[r[1]] + gray[r[2]] for t, r in enumerate(reps)}
    iso = len(set(f.values())) == 64 and all(
        sum(a != b for a, b in zip(f[u], f[w])) == 1 for u in range(64) for w in adj[u])
    check("C_4^3 (cubic torus L=4, presented with rank 3) is the 6-cube Q_6 (rank-6 presentation)", iso)
    # skew quotient: Lambda spanned by rows (5,0,0), (0,5,0), (1,2,5) -> lower-triangular form
    B = [[5, 0, 0], [0, 5, 0], [1, 2, 5]]
    reps, adj, simple = quotient_graph(B)
    maps = stabilizer_maps(adj, 0)
    check(f"skew quotient Lambda=<(5,0,0),(0,5,0),(1,2,5)>: simple {simple}; |Stab(0)| = {len(maps)} < 48",
          simple and len(maps) < 48, f"rank on links {link_rank(adj, maps, 0)}")


def part_E():
    print("== E. checkerboard and Brillouin-corner characters on finite quotients ==")
    lattices = [("L=3", [[3, 0, 0], [0, 3, 0], [0, 0, 3]]), ("L=4", [[4, 0, 0], [0, 4, 0], [0, 0, 4]]),
                ("L=5", [[5, 0, 0], [0, 5, 0], [0, 0, 5]]), ("L=6", [[6, 0, 0], [0, 6, 0], [0, 0, 6]]),
                ("skew even-sum <(4,0,0),(0,4,0),(1,1,4)>", [[4, 0, 0], [0, 4, 0], [1, 1, 4]])]
    expect = {"L=3": (False, 1), "L=4": (True, 8), "L=5": (False, 1), "L=6": (True, 8),
              "skew even-sum <(4,0,0),(0,4,0),(1,1,4)>": (True, 4)}
    for name, B in lattices:
        reps, adj, simple = quotient_graph(B)
        # bipartite by 2-colouring
        col = {0: 0}
        order = [0]
        bip = True
        for u in order:
            for w in adj[u]:
                if w not in col:
                    col[w] = 1 - col[u]
                    order.append(w)
                elif col[w] == col[u]:
                    bip = False
        # corner characters (-1)^{eta.n} well defined iff eta.b even for every basis row b
        corners = sum(1 for eta in product((0, 1), repeat=3)
                      if all(sum(e * x for e, x in zip(eta, b)) % 2 == 0 for b in B))
        check(f"{name}: bipartite {bip}; well-defined corner characters {corners} of 8",
              simple and (bip, corners) == expect[name])
    check("Z^3: bipartite (parity of n1+n2+n3) and all 8 corner characters defined", True, "structural")


# ---------------------------------------------------------------- F
def part_F():
    print("== F. SM section 4.1 linearity countermodel: ring versus Z ==")
    q = 5
    # ring L=4: fixed points of the phase map are (x, x) with 2x_i - x_{i-1} - x_{i+1} = 1
    L = 4
    fp = [x for x in product(range(q), repeat=L)
          if all((2 * x[i] - x[(i - 1) % L] - x[(i + 1) % L]) % q == 1 for i in range(L))]
    check("ring L=4, q=5, x(t+1)=x_{i-1}+x_{i+1}+1-x(t-1): no fixed point", len(fp) == 0)
    table = []
    for L in range(3, 11):
        n = sum(1 for x in product(range(q), repeat=L)
                if all((2 * x[i] - x[(i - 1) % L] - x[(i + 1) % L]) % q == 1 for i in range(L))) if L <= 8 else None
        table.append((L, n))
    ok = all((n > 0) == (L % q == 0) for L, n in table if n is not None)
    check("ring L=3..8, q=5: a fixed point exists iff q divides L", ok,
          ", ".join(f"L={L}:{n}" for L, n in table if n is not None))
    # Z: c_i = -binom(i, 2) mod 5 solves 2c_i - c_{i-1} - c_{i+1} = 1
    c = {i: (-(i * (i - 1) // 2)) % q for i in range(-60, 61)}
    fix = all((2 * c[i] - c[i - 1] - c[i + 1]) % q == 1 for i in range(-59, 60))
    check("Z: c_i = -i(i-1)/2 mod 5 is a fixed point on [-59, 59]", fix)
    # conjugacy tau phi_aff tau^{-1} = phi_lin with tau(p, c) = (p - c*, c - c*), on random windows
    import random
    rng = random.Random(20261120)
    ok = True
    for _ in range(200):
        p = {i: rng.randrange(q) for i in range(-30, 31)}
        x = {i: rng.randrange(q) for i in range(-30, 31)}
        for i in range(-29, 30):
            # phi_lin(p, x) at site i, second slot
            lin = (x[i - 1] + x[i + 1] - p[i]) % q
            # tau phi_aff tau^{-1}: shift back, apply affine, shift forward
            pp = (p[i] + c[i]) % q
            xx = {k: (x[k] + c[k]) % q for k in (i - 1, i, i + 1)}
            aff = (xx[i - 1] + xx[i + 1] + 1 - pp) % q
            if (aff - c[i]) % q != lin:
                ok = False
    check("Z: the site-wise shift by c conjugates the affine rule to the linear rule (200 random windows)", ok)
    const = [a for a in range(q) if (2 * a - 2 * a) % q == 1]
    check("Z: no translation-invariant (constant) fixed point, so no translation-commuting conjugacy",
          len(const) == 0)


if __name__ == "__main__":
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    print("== SUMMARY ==")
    print(f"{'ALL CHECKS PASS' if not FAIL else 'FAILURES: ' + '; '.join(FAIL)}")
    sys.exit(0 if not FAIL else 1)
